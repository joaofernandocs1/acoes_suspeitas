import os
import glob
import time
from datetime import datetime

def check_videos_to_upload():
    downloaded_videos_list = glob.glob('*.mp4', recursive=True)
    #print("downloaded_videos_list: ", downloaded_videos_list)

    for path_to_video in downloaded_videos_list:
        print("VIDEO NAME: ", path_to_video)
        # print("last changed time: ", os.path.getctime(path_to_video))
        # print("formatted last changed time: ", time.ctime(os.path.getctime(path_to_video)))
        last_mod_time = os.path.getmtime(path_to_video)
        date_time = datetime.fromtimestamp(last_mod_time)
        print("last mod time: ", last_mod_time) # melhor para colocar em ordem cronologica (maior diferenca entre os arquivos)
        print("date last mod time: ", date_time) # formatacao ainda melhor para pegar os microssegundos
        print("date_time seconds: {0} microseconds: {1}".format(date_time.second, date_time.microsecond))
        print("formatted last mod time: ", time.ctime(last_mod_time)) # nao e a melhor formatacao
        print(" ")

    pass

if __name__ == "__main__":

    check_videos_to_upload()