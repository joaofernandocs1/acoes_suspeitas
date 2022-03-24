import pandas as pd

# INPUT: msc.xlsx
# OUTPUT: atributes handled to directly upload in dynamodb table 'FlaggedVideos'

def msc_to_df(count_videos):

    msc_df = pd.read_excel(r"C:\Users\joaofernando\Documents\Roda\git_acoes_suspeitas\acoes_suspeitas\v_acoes_susp\manage_videos\msc\msc.xlsx") #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    #print (msc_df[0:count_videos])

    return msc_df[0:count_videos]

def gen_df_to_upload(df_from_msc):

    return

if __name__ == '__main__':

    count_videos = 2

    print(msc_to_df(count_videos))