from pytrends.request import TrendReq
import plotly.express as px
import time
from tqdm import tqdm

pytrends = TrendReq(hl='fr', tz=360)

multiply_args_list = ["sécurité", "services", "entreprise", "développement"]
pytrends.build_payload(multiply_args_list, cat=0, timeframe='today 12-m')
for item in tqdm(multiply_args_list):
    data = pytrends.interest_over_time()
    data = data.reset_index()
    fig = px.line(
                  data,
                  x="date",
                  y=multiply_args_list,
                  title='Tendances des tags Ticapsoriginal - France'
                  )
    time.sleep(30)
fig.show()
