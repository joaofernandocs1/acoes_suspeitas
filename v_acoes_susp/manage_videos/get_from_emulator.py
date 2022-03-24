import os 

# O EMULADOR PRECISA ESTAR ABERTO NO ANDROID STUDIO

def get_videos_from_emulator(path_from, path_to):

    command = "adb pull {0} {1}".format(path_from, path_to)
    print(command)
    os.system(command)

def copy_to_modules_path():

    # funcao para copiar da pasta "video/" criada ao fazer o adb pull para a pasta dos modulos

    return

if __name__ == '__main__':

    # exp.: /mnt/sdcard/MiboCam/4149925/video/
    complete_path_from = input("path completo da pasta do emulador para baixar videos: ")
    # exp.: C:\Users\joaofernando\Documents\Roda\git_acoes_suspeitas\acoes_suspeitas\v_acoes_susp\manage_videos
    complete_path_to = input("path local para colocar os vídeos baixados: ")

    get_videos_from_emulator(complete_path_from, complete_path_to)