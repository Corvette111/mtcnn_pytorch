import os
import common
import preprocessing.assemble as assemble

if __name__ == '__main__':
    os.chdir(common.ROOT_DIR)
    anno_list = []

    # rnet_landmark_file = os.path.join(config.ANNO_STORE_DIR,config.RNET_LANDMARK_ANNO_FILENAME)
    rnet_postive_file = os.path.join(common.ANNO_STORE_DIR, common.RNET_POSTIVE_ANNO_FILENAME)
    rnet_part_file = os.path.join(common.ANNO_STORE_DIR, common.RNET_PART_ANNO_FILENAME)
    rnet_neg_file = os.path.join(common.ANNO_STORE_DIR, common.RNET_NEGATIVE_ANNO_FILENAME)

    anno_list.append(rnet_postive_file)
    anno_list.append(rnet_part_file)
    anno_list.append(rnet_neg_file)
    # anno_list.append(rnet_landmark_file)

    imglist_file = os.path.join(common.ANNO_STORE_DIR, common.RNET_TRAIN_IMGLIST_FILENAME)

    chose_count = assemble.assemble_data(imglist_file, anno_list)
    print("PNet train annotation result file path:%s, total num of imgs: %d" % (imglist_file, chose_count))
