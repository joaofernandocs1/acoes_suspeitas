import pandas as pd

def return_msc(count_videos):

    msc_df = pd.read_excel(r"C:\Users\joaofernando\Documents\Roda/repo acoes suspeitas\acoes_suspeitas\v_acoes_susp\manage_videos\msc\msc.xlsx") #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    #print (msc_df[0:count_videos])

    return msc_df[0:count_videos]

if __name__ == '__main__':

    return_msc(count_videos)