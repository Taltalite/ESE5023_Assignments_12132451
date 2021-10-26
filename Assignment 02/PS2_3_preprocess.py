import pandas as pd
import os


def mergeAllDatas(root_dir):
    files = os.listdir(root_dir)
    cnt = 0
    num_file = 0
    for file in files:
        cnt += 1
        try:
            file_path = os.path.join(root_dir, file)
            pd_t = pd.read_csv(file_path)
            if os.path.isdir(file_path):
                continue
            if cnt % 1000 == 1:
                gsoy = pd.read_csv(file_path)
                continue
            gsoy = pd.merge(gsoy, pd.read_csv(file_path), how="outer")
            # gsoy = pd.concat([gsoy, pd_t])
        except:
            continue

        if cnt % 1000 == 0:
            num_file += 1
            file_name = "./gsoy_temp/gsoy_%04d.csv" % num_file
            gsoy.to_csv(file_name)
            print("save files %s" % file_name)
            print("processing %d %% , cnt: %d" % (cnt / len(files), cnt))
    num_file += 1
    file_name = "./gsoy_temp/gsoy_%04d.csv" % num_file
    gsoy.to_csv(file_name)
    print("save files %s" % file_name)
    print("processing %d %% , cnt: %d" % (cnt / len(files), cnt))

    return gsoy

print("==========================================================================")
print("1st merge")
gsoy = mergeAllDatas('D:\ESE5023\gsoy-latest')
print("==========================================================================")


def mergeLargeAllDatas(root_dir):
    files = os.listdir(root_dir)
    cnt = 0
    num_file = 0
    for file in files:
        cnt += 1
        try:
            file_path = os.path.join(root_dir, file)
            pd_t = pd.read_csv(file_path)
            if os.path.isdir(file_path):
                continue
            if cnt % 10 == 1:
                gsoy = pd.read_csv(file_path)
                continue
            gsoy = pd.merge(gsoy, pd.read_csv(file_path), how="outer")
            # gsoy = pd.concat([gsoy, pd_t])
        except:
            continue

        if cnt % 10 == 0:
            num_file += 1
            file_name = "./gsoy_big_temp/gsoy_%04d.csv" % num_file
            gsoy.to_csv(file_name)
            print("save files %s" % file_name)
            print("processing %d %% , cnt: %d" % (cnt / len(files), cnt))
    num_file += 1
    file_name = "./gsoy_big_temp/gsoy_%04d.csv" % num_file
    gsoy.to_csv(file_name)
    print("save files %s" % file_name)
    print("processing %d %% , cnt: %d" % (cnt / len(files), cnt))

    return gsoy

print("==========================================================================")
print("2nd merge")
gsoy = mergeLargeAllDatas('D:\ESE5023\ESE5023_Assignments_12132451\Assignment 02\gsoy_temp')
print("==========================================================================")

def mergeMaxAllDatas(root_dir):
    files = os.listdir(root_dir)
    cnt = 0
    num_file = 0
    for file in files:
        cnt += 1
        try:
            file_path = os.path.join(root_dir, file)
            pd_t = pd.read_csv(file_path)
            if os.path.isdir(file_path):
                continue
            if cnt % 2 == 1:
                gsoy = pd.read_csv(file_path)
                continue
            gsoy = pd.merge(gsoy, pd.read_csv(file_path), how="outer")
            # gsoy = pd.concat([gsoy, pd_t])
        except:
            continue

        if cnt % 2 == 0:
            num_file += 1
            file_name = "./gsoy_max_temp/gsoy_%04d.csv" % num_file
            gsoy.to_csv(file_name)
            print("save files %s" % file_name)
            print("processing %d %% , cnt: %d" % (cnt / len(files), cnt))

    if cnt % 2 != 0:
        num_file += 1
        file_name = "./gsoy_max_temp/gsoy_%04d.csv" % num_file
        gsoy.to_csv(file_name)
        print("save files %s" % file_name)
        print("processing %d %% , cnt: %d" % (cnt / len(files), cnt))

    return gsoy

print("==========================================================================")
print("3rd merge")
gsoy = mergeMaxAllDatas('D:\ESE5023\ESE5023_Assignments_12132451\Assignment 02\gsoy_big_temp')
print("==========================================================================")


def mergeFinalAllDatas(root_dir):
    files = os.listdir(root_dir)
    cnt = 0
    num_file = 0
    for file in files:
        cnt += 1
        try:
            file_path = os.path.join(root_dir, file)
            pd_t = pd.read_csv(file_path)
            if os.path.isdir(file_path):
                continue
            if cnt == 1:
                gsoy = pd.read_csv(file_path)
                continue
            gsoy = pd.merge(gsoy, pd.read_csv(file_path), how="outer")
            # gsoy = pd.concat([gsoy, pd_t])
        except:
            continue

    file_name = "./gsoy.csv"
    gsoy.to_csv(file_name)

    return gsoy

print("==========================================================================")
print("4th merge")
gsoy = mergeFinalAllDatas('D:\ESE5023\ESE5023_Assignments_12132451\Assignment 02\gsoy_max_temp')
print("==========================================================================")

print("==========================================================================")
print("drop useless cols")
df = pd.read_csv("./gsoy.csv", low_memory=False)
df.drop(columns=['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1','Unnamed: 0.1.1.1'], axis=1, inplace=True)
df.to_csv('./gsoy.csv')
print("==========================================================================")