import glob
import os
import pathlib2

def check_videos_to_upload():
    videos_to_insert = glob.glob('**/*.mp4', recursive=True)
    print(videos_to_insert)

    for video_to_insert in videos_to_insert:
        pre_process_data = video_to_insert.split("\\")[1]
        pre_process_data = pre_process_data.split("_")[0]
        pre_process_data = pre_process_data[0:8]
        year = str(pre_process_data[0:4])
        month = str(pre_process_data[4:6])
        day = str(pre_process_data[6:8])
        data = day + "/" + month + "/" + year

check_videos_to_upload()