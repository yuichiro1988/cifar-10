import os
import shutil
import random
import pandas as pd


def make_subclass_dir(src_dir, subclass_dir, label_idx):
    if os.path.exists(subclass_dir):
        shutil.rmtree(subclass_dir)

    os.mkdir(subclass_dir)

    for i in label_idx:
        label = train_labels.ix[i, "label"]

        if not os.path.exists(os.path.join(subclass_dir, label)):
            os.mkdir(os.path.join(subclass_dir, label))

            shutil.copyfile("{}/{}.png".format(src_dir, i+1),
                "{}/{}/{}.png".format(subclass_dir, label, i+1))

if __name__ ==  "__main__":
    train_labels = pd.read_csv("./data/trainLabels.csv", delimiter=",")

    label_idx = list(range(len(train_labels)))
    label_idx = random.sample(label_idx, k=len(label_idx))
    train_label_idx = label_idx[: 45000]
    val_label_idx = label_idx[45000: ]

    scr_dir = "./data/train"
    train_subclass_dir = "./processed/train"
    val_subclass_dir = "./processed/validation"

    make_subclass_dir(scr_dir, train_subclass_dir, train_label_idx)
    make_subclass_dir(scr_dir, val_subclass_dir, val_label_idx)
