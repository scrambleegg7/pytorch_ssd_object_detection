from utils import create_data_lists

if __name__ == '__main__':

    data_dir = "L:/Miyuki/VOC_PASCAL/miyuki_prescription_output"
    print(data_dir)

    create_data_lists(voc07_path=data_dir, output_folder='./')
