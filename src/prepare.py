from datetime import date
import pandas as pd
from io import StringIO
import sys
import logging

logging.basicConfig(
    format='%{asctime}s %{levelname}s:%{name}: {message}s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logging.info('Fetching data ...')

#movie_data