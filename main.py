from youtube import ytmp3
from soundcloud import stmp3

def main():
    url = str(input("Input url: "))
    ytmp3(url)
    # if url.find("youtube") == 1:
    #     print("youtube")
    #     ytmp3(url)
    # elif url.find("soundcloud") == 1:
    #     print("soundcloud")
    #     # stmp3(url)
    # elif url.find("bilibili") == 1:
    #     print("bilibili")
    # elif url.find("dailymotion") == 1:
    #     print("dailymotion")
    # else:
    #     print("Can't identify url")            

