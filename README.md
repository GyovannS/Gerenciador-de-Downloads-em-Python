# Youtube & Instagram Downloader

Este projeto é um programa em Python que permite baixar músicas e vídeos do YouTube, além de vídeos do Instagram, diretamente pelo terminal. O usuário escolhe o tipo de download através de um menu interativo.

## Funcionalidades

- **Baixar músicas do YouTube:**  
  Faz o download apenas do áudio de um vídeo do YouTube.

- **Baixar vídeos do YouTube:**  
  Faz o download do vídeo completo na melhor resolução disponível.

- **Baixar vídeos do Instagram:**  
  Faz o download de vídeos públicos do Instagram a partir do link.

## Como usar

1. **Instale as dependências:**
   - No terminal, execute:
     ```
     pip install pytube instaloader
     ```

2. **Execute o programa:**
   - Rode o arquivo Python:
     ```
     python Youtube_video_music_download_projeto.py
     ```

3. **Escolha a opção desejada no menu:**
   - Digite o número da opção para baixar música, vídeo do YouTube ou vídeo do Instagram.
   - Cole o link do vídeo/música quando solicitado.

## Observações

- Os arquivos baixados serão salvos na mesma pasta do script.
- O programa utiliza as bibliotecas [pytube](https://pytube.io/) para YouTube e [instaloader](https://instaloader.github.io/) para Instagram.
- O download de vídeos privados do Instagram pode não funcionar.
- Caso o pytube apresente erros devido a mudanças no YouTube, considere usar [yt-dlp](https://github.com/yt-dlp/yt-dlp) como alternativa.

## Licença

Este projeto é livre para uso educacional e pessoal.
Um gerenciador de downloads, que baixar arquivos de áudio e vídeo do YouTube e baixa arquivos de vídeo do Instagram.
