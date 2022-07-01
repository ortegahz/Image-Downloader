from shutil import copyfile
import glob
import os

dir_in = '/media/manu/kingstop/workspace/Image-Downloader/download_images'
dir_out = '/media/manu/kingstop/matting-data/Backgrounds/train'

sub_dirs = os.listdir(dir_in)

cnt = 0
for sub_dir in sub_dirs:
    for path in glob.glob(os.path.join(dir_in, sub_dir, '*')):
        cnt += 1
        _, file_name = os.path.split(path)
        file_name_out = sub_dir + '_' + file_name
        copyfile(path, os.path.join(dir_out, file_name_out))
        print(f'copying {cnt}th path {path}')
