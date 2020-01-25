# import requests
#
# if __name__ == '__main__':
#     r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
#     rjson = r.json()
#     print(rjson['RealtimeCityAir']['row'][0])


import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    r = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909')

    soup = BeautifulSoup(r.text, 'html.parser')

    movies = soup.select('#old_content > table > tbody > tr')
    ##old_content > table > tbody > tr:nth-child(1)  -----> tr 뒷 부분은 지우기
    #movies는 자동으로 리스트로 선언됨

    res=[]

    i=1
    for movie in movies:
    #for i in range(len(movies)):
    #   movie = movies[i]

        movie_name = movie.select_one('.title a')
        if movie_name is not None:
            movie_rating = movie.select_one('.point')
            if movie_rating is not None:
                # print(i, movie_name.text, "|", movie_rating.text)

                movie_info = {'rank':i, 'name':movie_name.text, 'rating':movie_rating.text}
                res.append(movie_info)
                i+=1
    print(res)


    # movies=soup.select('#old_content > table > tbody > tr')[0]
    #
    # print(soup)

