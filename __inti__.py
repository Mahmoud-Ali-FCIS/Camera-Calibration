import argparse
from helper import read_data, write_data_in_yaml
from Calibration import camera_calibration


if __name__ == '__main__':
    # Construct the argument parse and parse the arguments
    # We can get all the parameters of this program using terminal
    ap = argparse.ArgumentParser()
    ap.add_argument("-ptr1", "--path_data", type=str,
                    default='Data3',
                    help="name the folder of data for calibration [Data1, Data2, Data3]")
    ap.add_argument("-flag", "--flag_my_data", type=bool,
                    default=False,
                    help="set True if you need create your data")
    args = vars(ap.parse_args())

    images = read_data(args["path_data"], args["flag_my_data"])

    try:
        data = camera_calibration(images, args["path_data"])
        write_data_in_yaml(data, 'Result/Camera_Calibration' + args["path_data"] + '.yaml')
    except:
        print("Oops!  Your Data not good for calibration.  Please,Try again!")
