import os
import common
import preprocessing.assemble as assemble

if __name__ == '__main__':
    os.chdir(common.ROOT_DIR)
    anno_list = []

    pnet_postive_file = os.path.join(
        common.ANNO_STORE_DIR, common.PNET_POSTIVE_ANNO_FILENAME)
    pnet_part_file = os.path.join(
        common.ANNO_STORE_DIR, common.PNET_PART_ANNO_FILENAME)
    pnet_neg_file = os.path.join(
        common.ANNO_STORE_DIR, common.PNET_NEGATIVE_ANNO_FILENAME)

    anno_list.append(pnet_postive_file)
    anno_list.append(pnet_part_file)
    anno_list.append(pnet_neg_file)

    imglist_filename = common.PNET_TRAIN_IMGLIST_FILENAME
    anno_dir = common.ANNO_STORE_DIR
    imglist_file = os.path.join(anno_dir, imglist_filename)

    chose_count = assemble.assemble_data(imglist_file, anno_list)
    print("PNet train annotation result file path:%s" % imglist_file)
