# Python program which grabs download links of episodes of any anime from https://www10.gogoanime.io and copies all of them to
# the clipboard
# Usage - python animed.py <name of anime> <starting ep> <ending ep>

import bs4 , pyperclip , sys , threading
import requests , subprocess , time

starttime = time.time()
animename = "-".join(sys.argv[1:len(sys.argv) - 2])
url = "https://www10.gogoanime.io/" + animename + "-episode-"
durls = []

print("Getting links...")
for i in range(int(sys.argv[-2]) , int(sys.argv[-1]) + 1):
    ep = requests.get(url + str(i))
    epsoup = bs4.BeautifulSoup(ep.text , "lxml")
    l = epsoup.select(".anime_video_body_cate > a")
    epurl = l[1].get("href")
    dpage = requests.get(epurl)
    dsoup = bs4.BeautifulSoup(dpage.text , "lxml")
    e = dsoup.select(".mirror_link > div > a")
    durls.append(e[0].get("href"))

pyperclip.copy("\n".join(durls)) 
print("Links copied to clipboard!")
subprocess.Popen("D:\\Programs\\Internet Download Manager\\IDman.exe")
endtime = time.time()
print("Time taken for grabbing links by the program: " + str(endtime - starttime))
#for url in durls:
#    subprocess.Popen(["D:\\Programs\\Internet Download Manager\\IDman.exe" , "/n" , "/s" , url])

