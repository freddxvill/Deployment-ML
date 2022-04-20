import requests

url = 'https://ml-movie-prediction.herokuapp.com/v1/prediction'

json = {
        "opening_gross": 30681,
        "screens": 2271,
        "production_budget": 106000,
        "title_year": 2010,
        "aspect_ratio": 1.85,
        "duration": 70,
        "cast_total_facebook_likes": 3907,
        "budget": 10000000,
        "imdb_score": 7.2
}

response = requests.post(url, json=json)
print(f'url: {url} \nstatus: {response.status_code}')
print('Prediction '.center(50,'='))
print('Worldwide gross: {:.2f} $'.format(response.json()['worldwide_gross']))
print('='.center(50,'='))

