# Python program which grabs download links of episodes of any anime from https://www10.gogoanime.io and copies all of them to
# the clipboard
# Usage - python animed.py <name of anime> <starting ep> <ending ep>
# Time of link grabbing reduced to 1/n of original time by multithreading!!! where n = no. of episodes
# Warning! : Doesn't work well on slow connections since it uses multithreading to make multiple connections to server.

import bs4 , pyperclip , sys , threading
import requests , subprocess , time

def epfetcher(url , durls):
    ep = requests.get(url)
    epsoup = bs4.BeautifulSoup(ep.text , "lxml")
    l = epsoup.select(".anime_video_body_cate > a")
    epurl = l[1].get("href")
    dpage = requests.get(epurl)
    dsoup = bs4.BeautifulSoup(dpage.text , "lxml")
    e = dsoup.select(".mirror_link > div > a")
    durls.append(e[0].get("href"))

starttime = time.time()
animename = "-".join(sys.argv[1:len(sys.argv) - 2])
url = "https://www10.gogoanime.io/" + animename + "-episode-"
durls = []
threads = []

print("Getting links...")
for i in range(int(sys.argv[-2]) , int(sys.argv[-1]) + 1):
    threads.append(threading.Thread(target=epfetcher , args=[url + str(i) , durls]))
    threads[-1].start()
for thread in threads:
        thread.join()

pyperclip.copy("\n".join(durls)) 
print("Links copied to clipboard!")

subprocess.Popen("D:\\Programs\\Internet Download Manager\\IDman.exe")
endtime = time.time()
print("Time taken for grabbing links by the program: " + str(endtime - starttime))