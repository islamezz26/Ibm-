# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:39:05 2021

@author: Eslam Ezz
"""
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

gamestop = yf.Ticker("GME")
gme_data=gamestop.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()