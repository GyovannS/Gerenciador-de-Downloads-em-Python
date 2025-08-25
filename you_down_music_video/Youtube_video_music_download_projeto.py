from pytube import YouTube
import instaloader

#   /   /Download de música youtube/   /   /
def baixar_musica_youtube(url):
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()
    print("Música baixada com sucesso!")

#   /   /Download de video youtube/   /   / 
def baixar_video_youtube(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    print("Video baixado com sucesso")

#   /   /Download de video instagram/   /   / 
def baixar_video_instagram(url):
    insta = instaloader.Instaloader()
    insta.download_url(url, target="instagram_video")
    print("Video do baixado com sucesso")

#   /   /MENU DOWNLOAD/   /   /
def menu():
    while True:
        print("---------MENU DO DOWNLOAD DE ARQUIVO-----------")
        print("\n 1. Baixar músicas do Youtube",
              "\n 2. Baixar videos do Youtube",
              "\n 3. Baixar videos do Instagram",
              "\n 4. Sair do programa")
        opcao = input("Digite o número da opção para fazer o download da sua escolha: ")

        if opcao == '1':
            url = input("Coloque o link para fazer o download:")
            baixar_musica_youtube(url)
        elif opcao == '2':
            url = input("Coloque o link para fazer o download:")
            baixar_video_youtube(url)
        elif opcao == '3':
            url = input("Coloque o link para fazer o download")
            baixar_video_instagram(url)
        elif opcao == '4':
            break
        else:
            print("Opção Inválida")
menu()                    
        
              




    


    