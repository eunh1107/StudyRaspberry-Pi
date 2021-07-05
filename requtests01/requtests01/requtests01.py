import requests
url='https://blog.naver.com/1107ku'
movie=requests.get(url)
print(movie.text)
