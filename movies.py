import requests
import json
import random

movie_genres_dict = {
    28: "Action",
    12: "Abenteuer",
    16: "Animation",
    35: "Komödie",
    80: "Krimi",
    99: "Dokumentarfilm",
    18: "Drama",
    10751: "Familie",
    14: "Fantasy",
    36: "Historie",
    27: "Horror",
    10402: "Musik",
    9648: "Mystery",
    10749: "Liebesfilm",
    878: "Science Fiction",
    10770: "TV-Film",
    53: "Thriller",
    10752: "Kriegsfilm",
    37: "Western"
}

TV_genres_dict = {
    10759: "Action & Adventure",
    16: "Animation",
    35: "Komödie",
    80: "Krimi",
    99: "Dokumentarfilm",
    18: "Drama",
    10751: "Familie",
    10762: "Kids",
    9648: "Mystery",
    10763: "News",
    10764: "Reality",
    10765: "Sci-Fi & Fantasy",
    10766: "Soap",
    10767: "Talk",
    10768: "War & Politics",
    37: "Western"
}

def get_movie_rec_list(user_selected_genre, random_page=1):
    # print("random page", random_page)
    movie_url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page="+ str(random_page) +"&sort_by=vote_count.desc.desc&with_genres=" + str(user_selected_genre)
    # print(movie_url)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer <API KEY>"
    }
    response = requests.get(movie_url, headers=headers)
    return response


def json_parse(response):
    data = response.json()
    # print(json.dumps(data, indent=4))
    data_json = json.dumps(data, indent=4)
    reply = json.loads(data_json)
    results = reply["results"]
    total_pages = reply.get("total_pages")
    return results, total_pages

def select_from_list(results, total_pages, user_selected_genre):
    # print( "total pages", total_pages)
    random_page = random.randint(0, total_pages//25)
    response = get_movie_rec_list(user_selected_genre, random_page)
    # print(response)
    results, total_pages = json_parse(response)
    titles = [movie['title'] for movie in results]
    # for i in titles:
    #     print(i)
    random_movie = random.randint(0, len(titles) - 1)
    recommendation = titles[random_movie]
    return recommendation

def main():
    for i in movie_genres_dict.keys():
        print(i, ": ", movie_genres_dict.get(i))

    user_selected_genre = input("which genre of movie would you like to watch: ")

    response = get_movie_rec_list(user_selected_genre)
    results, total_pages = json_parse(response)
    recommendation = select_from_list(results, total_pages, user_selected_genre)
    print("recommendation:", recommendation)

main()