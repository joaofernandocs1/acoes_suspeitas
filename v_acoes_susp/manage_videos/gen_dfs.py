import pandas as pd

# INPUT: msc.xlsx
# OUTPUT: atributes handled to directly upload in dynamodb table 'FlaggedVideos'

def msc_to_df(count_videos):

    msc_df = pd.read_excel(r"C:\Users\joaofernando\Documents\Roda\git_acoes_suspeitas\acoes_suspeitas\v_acoes_susp\manage_videos\msc\msc.xlsx") #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    #print (msc_df[0:count_videos])

    return msc_df[0:count_videos]

def append_into_msc_df(videos_url_list, video_files_list, df_to_join):

    # adiciona a lista de nomes dos arquivos de video como uma nova coluna ao dataframe
    df_to_join['arquivo'] = video_files_list
    # adiciona a lista de urls de cada video como uma nova coluna ao dataframe
    df_to_join['url'] = videos_url_list

    return df_to_join

if __name__ == '__main__':

    count_videos = 2  # teste

    df_to_insert_urls = msc_to_df(count_videos)