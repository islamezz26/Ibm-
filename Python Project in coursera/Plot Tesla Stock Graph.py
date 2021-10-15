import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

make_graph(tesla_data, tesla_revenue, 'Tesla Stock Data Graph')
make_graph(gme_data, gme_revenue, 'GameStop Stock Data Graph')
