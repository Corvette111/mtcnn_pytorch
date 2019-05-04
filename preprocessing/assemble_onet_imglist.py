import os
import common
import preprocessing.assemble as assemble

if __name__ == '__main__':
    os.chdir(common.ROOT_DIR)
    anno_list = []

    net_landmark_file = os.path.join(common.ANNO_STORE_DIR, common.ONET_LANDMARK_ANNO_FILENAME)
    net_postive_file = os.path.join(common.ANNO_STORE_DIR, common.ONET_POSTIVE_ANNO_FILENAME)
    net_part_file = os.path.join(common.ANNO_STORE_DIR, common.ONET_PART_ANNO_FILENAME)
    net_neg_file = os.path.join(common.ANNO_STORE_DIR, common.ONET_NEGATIVE_ANNO_FILENAME)

    anno_list.append(net_postive_file)
    anno_list.append(net_part_file)
    anno_list.append(net_neg_file)
    anno_list.append(net_landmark_file)

    imglist_file = os.path.join(common.ANNO_STORE_DIR, common.ONET_TRAIN_IMGLIST_FILENAME)

    chose_count = assemble.assemble_data(imglist_file, anno_list)
    print("PNet train annotation result file path:%s" % imglist_file)
