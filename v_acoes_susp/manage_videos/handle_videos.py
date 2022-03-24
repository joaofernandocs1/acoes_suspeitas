import boto3
from botocore.exceptions import ClientError
from pprint import pprint
import glob
import crud_video
import gen_dfs
#import pandas as pd
import logging
import os
import sys
import threading


# INPUT:
# OUTPUT:

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

def check_videos_to_upload():
    downloaded_videos_list = glob.glob('**/*.mp4', recursive=True)
    #downloaded_videos_list = glob.glob('*.mp4', recursive=True)
    #print("downloaded_videos_list: ", downloaded_videos_list)

    index = 0
    for path_to_video in downloaded_videos_list:
        relative_path = path_to_video[0:7]
        #print("relative_path: ", relative_path)
        video_name = path_to_video[7:]
        #print("video_name: ", video_name)
        downloaded_videos_list[index] = relative_path + video_name
        #print("downloaded_videos_list[index]: ", downloaded_videos_list[index])
        index =+ 1

    #print(downloaded_videos_list)

    return downloaded_videos_list

def upload_file(file_name, bucket, folder, object_name=None):
    ''' Upload a file to an S3 bucket
        :param file_name: File to upload
        :param bucket: Bucket to upload to # "flagged-videos"
        :param folder: folder in bucket to upload to # "videos"
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False '''
    
    s3_client = boto3.client('s3')

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    #print("file name: ", file_name)

    # Upload the file
    try:
        #s3_client.upload_file(file_name, bucket, folder + '/' + file_name, Callback=ProgressPercentage(file_name)) # talvez a funcao nao retorne este "response" e nao haja o que printar
        print("uploaded")

    except ClientError as e:
        logging.error(e)
        return False

    object_url = "https://" + bucket + ".s3.amazonaws.com/" + "folder" + "/" + file_name

    return True, object_url

if __name__ == '__main__':

    videos_list = check_videos_to_upload()
    #print(videos_list)
    url_list = [None]*len(videos_list)
    
    index_url = 0
    for video in videos_list:

        response, obj_url = upload_file(video, "flagged-videos", "videos")

        if (response):
            print(" upload OK ", obj_url)
            url_list[index_url] = obj_url
        else:
            print(" upload FAILED")
        index_url =+ 1

    #print(url_list)
    df_to_join_urls = gen_dfs.msc_to_df(len(url_list))
    final_df = gen_dfs.append_into_msc_df(url_list, videos_list, df_to_join_urls)
    #print(final_df)

    final_df = final_df.iloc[:, 1:] # recorta a primeira coluna que nao tem utilidade
    print(final_df)

    for row in range(len(url_list)):

        insert_resp = crud_video.insert_video(str(row), str(final_df.loc[row, 'duration']), str(final_df.loc[row, 'date']), str(final_df.loc[row, 'location id']), str(final_df.loc[row, 'location_name']), str(final_df.loc[row, 'arquivo']), str(final_df.loc[row, 'url']))
        print("video insert response:", insert_resp)