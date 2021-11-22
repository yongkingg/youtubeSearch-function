import urllib.request
import re
import Config

search_keyword = input("영상을 검색하세요 : ")
if search_keyword.encode().isalpha(): # 영어로만 이루어진 경우
    html =  urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])
else: # 혼합
    search = str(search_keyword.encode('utf-8'))
    search = search.replace("\\x","%")
    search = search.replace("'","")
    html =  urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search[1:])
    video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
    print("https://www.youtube.com/watch?v=" + video_ids[0])

