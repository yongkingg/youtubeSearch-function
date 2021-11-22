import pafy
url = 'https://www.youtube.com/watch?v=zzTthzmfbe8'
try:
    video = pafy.new(url)
except KeyError:
    pass
print(video.viewcount)
print(video.category)
print(video.length)
print(video.author)
print(video.thumb)