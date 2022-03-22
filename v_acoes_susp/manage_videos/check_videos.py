import boto3
from pprint import pprint
import glob
import os
import pathlib2
import crud_video
import open_msc
import pandas as pd

def check_videos_to_upload():
    videos_to_insert = glob.glob('**/*.mp4', recursive=True)
    #print(videos_to_insert)
    videos_df = open_msc.return_msc(len(videos_to_insert))
    #print(videos_df)
    videos_df = videos_df.iloc[:, 1:]
    #print(videos_df)
    videos_df = videos_df.assign(arquivo = videos_to_insert)
    #print(videos_df)

    for n in range(len(videos_to_insert)):
        video_resp = crud_video.insert_video(str(n), str(videos_df.loc[n, 'duration']), str(videos_df.loc[n, 'date']), str(videos_df.loc[n, 'location id']), str(videos_df.loc[n, 'location_name']), str(videos_df.loc[n, 'arquivo']))
        print("Insert video succeeded:")
        pprint(video_resp, sort_dicts=False)

if __name__ == '__main__':

    check_videos_to_upload()