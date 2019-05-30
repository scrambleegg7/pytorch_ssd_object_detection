from utils import create_data_lists

if __name__ == '__main__':

    data_dir = "/home/donchan/Documents/DATA/PASCAL_VOC/miyuki_prescription_output"

    create_data_lists(voc07_path=data_dir,
                      output_folder='./')
