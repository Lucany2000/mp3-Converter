from pytube import YouTube
#from main import main
import os

def ytmp3(url):
    video = YouTube(url).streams
    audio = video.filter(type="audio")
    print("Processing....")
    song = audio.first().download(output_path="music")
    base, ext = os.path.splitext(song)
    outfile = base + ".mp3"
    os.rename(song, outfile)
    return "Finished"
    #answer = str(input("Would you like to convert another song Y/N?"))
    # if answer.lower() == "y" or answer.lower() == "yes":
    #     main()
    # else:
    #     pass    