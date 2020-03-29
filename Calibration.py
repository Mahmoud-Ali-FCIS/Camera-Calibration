import cv2
import numpy as np

CHECKERBOARD = {"Data1": (7, 6),
                "Data2": (9, 6),
                "Data3": (5, 4),
                "Data4": (5, 4)}


def camera_calibration(data, path_data):

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # Creating vector to store vectors of 3D points for each checkerboard image
    obj_points = []
    # Creating vector to store vectors of 2D points for each checkerboard image
    img_points = []

    # Defining the world coordinates for 3D points
    obj_p = np.zeros((1, CHECKERBOARD[path_data][0] * CHECKERBOARD[path_data][1], 3), np.float32)
    obj_p[0, :, :2] = np.mgrid[0:CHECKERBOARD[path_data][0], 0:CHECKERBOARD[path_data][1]].T.reshape(-1, 2)

    for img in data:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Find the chess board corners
        # If desired number of corners are found in the image then ret = true
        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD[path_data], cv2.CALIB_CB_ADAPTIVE_THRESH +
                                                 cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)

        if ret:
            obj_points.append(obj_p)
            # refining pixel coordinates for given 2d points.
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

            img_points.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, CHECKERBOARD[path_data], corners2, ret)

        cv2.imshow('img', img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

    ret, mtx, dist, r_vecs, t_vecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

    # transform the matrix and distortion coefficients to writable lists
    data = {'camera_matrix': np.asarray(mtx).tolist(),
            'dist_coefficient': np.asarray(dist).tolist()}

    return data
