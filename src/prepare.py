from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Fetching data...')

movie_data_path = api.read('dataset/movies.csv', remote='dataset-track', mode='rb')
finantial_data_path = api.read('dataset/finantials.csv', remote='dataset-track', mode='rb')
opening_data_path = api.read('dataset/opening_gross.csv', remote='dataset-track', mode='rb')

movie_data = pd.read_csv(StringIO(str(movie_data_path, encoding='utf-8')))
fin_data = pd.read_csv(StringIO(str(finantial_data_path, encoding='utf-8')))
opening_data = pd.read_csv(StringIO(str(opening_data_path,encoding='utf-8')))

colnames_numerics = movie_data.select_dtypes('number').columns.tolist()
movie_data = movie_data[colnames_numerics+['movie_title']]

fin_data = fin_data[['movie_title','production_budget','worldwide_gross']]

fin_movie_data = pd.merge(fin_data, movie_data, on= 'movie_title', how='left')
full_movie_data = pd.merge(opening_data, fin_movie_data, on = 'movie_title', how='left')

full_movie_data = full_movie_data.drop(['movie_title','gross'],axis=1)

full_movie_data.to_csv('dataset/full_data.csv', index=False)

logger.info('Data Fetched and Prepared...')