import cv2
import yaml
import glob


def read_data(path_data, flag_my_data):
    if flag_my_data:
        return create_my_data()
    else:
        data = glob.glob(path_data + '/*')
        images = []
        for f_name in data:
            img = cv2.imread(f_name)
            images.append(img)
        return images


def create_my_data():
    camera = cv2.VideoCapture(0)
    data = []
    i = 0
    while i < 15:
        input('Press Enter to capture')
        return_value, image = camera.read()
        cv2.imshow('img', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(i)
        data.append(image)
        cv2.imwrite('Data4/opencv'+str(i)+'.png', image)
        i += 1
    del camera
    return data


def write_data_in_yaml(data, name_file):
    with open(name_file, "w") as f:
        yaml.dump(data, f)
