#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install --upgrade yfinance pandas plotly')
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().system('pip install --upgrade pandas')
get_ipython().system('pip install beautifulsoup4')


# In[27]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[28]:


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# ## Question 1: Use yfinance to Extract Telsa Data
# 

# Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.
# 

# In[29]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[30]:


tesla_ticker_symbol = "TSLA"


tesla_ticker = yf.Ticker(tesla_ticker_symbol)


# Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to `max` so we get information for the maximum amount of time.

# In[31]:


import yfinance as yf

tesla_ticker = yf.Ticker("TSLA")

tesla_historical_data = tesla_ticker.history(period="max")

print(tesla_historical_data)


# **Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.
# 

# In[32]:


tesla_historical_data.reset_index(inplace=True)

tesla_historical_data.head()



# ## Question 2 - Extracting Tesla Revenue Data Using Webscraping - 1 Points

# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named html_data.

# In[33]:


import requests

url_1 = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

response_TSLA = requests.get(url_1)

if response_TSLA.status_code == 200:
    
    html_data_TSLA = response_TSLA.text
    print("Webpage downloaded successfully.")
else:
    print(f"Failed to download webpage. Status code: {response.status_code}")


# Parse the html data using `beautiful_soup`.
# 

# In[34]:


from bs4 import BeautifulSoup

soup= BeautifulSoup(html_data_TSLA, "html.parser")

table_TSLA=soup.find('table')

tesla_revenue = pd.read_html(str(table_TSLA))[0]

print(tesla_revenue.columns)


# ### Telsa Revenue `[Tail Function]`

# Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.
# 

# In[35]:


tesla_revenue.columns = ['Date', 'Tesla Revenue (millions)']

## Execute the following line to remove the comma and dollar sign from the `Revenue` column. (Need to use `BeautifulSoup`) 
tesla_revenue['Tesla Revenue (millions)'] = tesla_revenue['Tesla Revenue (millions)'].str.replace(',|\$', '', regex=True)


print(tesla_revenue.tail()) 


# ## Question 3 - Extracting GameStop GME Data Using yfinance - 2 Points
# 

# Using the ticker object and the function history extract stock information and save it in a dataframe named tesla_data. Set the period parameter to MAX so we get information for the maximum amount of time.

# In[36]:


import yfinance as yf

Gamestop_ticker = yf.Ticker("GME")

Gamestop_historical_data = Gamestop_ticker.history(period="max")


print(Gamestop_historical_data)


# **Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.
# 

# In[37]:


Gamestop_historical_data.reset_index(inplace=True)
Gamestop_historical_data.head()


# ## Question 4 -  Use Webscraping to Extract GME Revenue Data - 1 Points

# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named html_data.

# In[38]:


import requests 

url_2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

response_Gamestop = requests.get(url_2)

if response_Gamestop.status_code== 200:

    html_data_Gamestop= response_Gamestop.text
    print("Webpage downloaded successfully")
else:
    print(f"Failed to download webpage. Status code: {response.status_code}")


# ### Using `BeautifulSoup` to convert html into dataframe for annual revenue 

# In[39]:


from bs4 import BeautifulSoup

soup= BeautifulSoup(html_data_Gamestop, "html.parser")

table_GME=soup.find('table')

GME_revenue = pd.read_html(str(table_GME))[0]

print(GME_revenue.columns)


# ### GameStop Revenue `[Tail Function]`
# 

# In[40]:


GME_revenue.columns = ['GameStop Date', 'GameStop Revenue (millions)']

##Execute the following line to remove the comma and dollar sign from the `Revenue` column. (Need to use `BeautifulSoup`) 
GME_revenue['GameStop Revenue (millions)'] = GME_revenue['GameStop Revenue (millions)'].str.replace(',|\$', '', regex=True)


print(GME_revenue.tail())


# # Question 5 -  Plot Tesla Stock Graph

# In[41]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
import pandas as pd


stock_symbol_TSLA = "TSLA"


start_date = "2009-01-01"
end_date = "2021-09-30"


stock_data_TSLA = yf.download(stock_symbol_TSLA, start=start_date, end=end_date, progress=False)
revenue_data_TSLA = yf.download(stock_symbol_TSLA, start=start_date, end=end_date, progress=False)


stock_data_TSLA.reset_index(inplace=True)
revenue_data_TSLA.reset_index(inplace=True)

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, 
                        shared_xaxes=True, 
                        subplot_titles=("Historical Share Price", "Historical Revenue"), 
                        vertical_spacing=.3)
    
    stock_data_specific = stock_data[stock_data['Date'] <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data['Date'] <= '2021-04-30']
    
    fig.add_trace(go.Scatter(
        x=stock_data_specific['Date'],
        y=stock_data_specific['Close'].astype("float"), name="Share Price"), row=1, col=1)
    
    fig.add_trace(go.Scatter(x=revenue_data_specific['Date'], 
                             y=revenue_data_specific['Close'].astype("float"),  # Use 'Close' for revenue data
                             name="Revenue"), row=2, col=1)
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    
    fig.show()

make_graph(stock_data_TSLA, revenue_data_TSLA, stock_symbol_TSLA)


# # Question 6 - GameStop Stock and Revenue Graph
# 

# In[42]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
import pandas as pd


stock_symbol_gme = "GME"


start_date = "2004-01-01"
end_date = "2021-09-30"


stock_data = yf.download(stock_symbol_gme, start=start_date, end=end_date, progress=False)
revenue_data = yf.download(stock_symbol_gme, start=start_date, end=end_date, progress=False)
stock_data.reset_index(inplace=True)
revenue_data.reset_index(inplace=True)

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, 
                        shared_xaxes=True, 
                        subplot_titles=("Historical Share Price", "Historical Revenue"), 
                        vertical_spacing=.3)
    
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    
    fig.add_trace(go.Scatter(
        x=pd.to_datetime(stock_data_specific.Date, format='%Y-%m-%d'),
        y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, format='%Y-%m-%d'), 
                             y=revenue_data_specific.Close.astype("float"),  # Use 'Close' for revenue data
                             name="Revenue"), row=2, col=1)
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    
    fig.show()
    
make_graph(stock_data, revenue_data, stock_symbol_gme)

