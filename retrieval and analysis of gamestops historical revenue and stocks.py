import os
# Set the working directory
os.chdir("C:/Users/kalab/OneDrive/Desktop/py4e/assignment 7/")
print("Current Working Directory:", os.getcwd())  # Check if the working directory is correct



import urllib.request, urllib.parse, urllib.error
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)





#using yfinance to extract gamestop stock data  
gamestop = yf.Ticker("GME")
gme_companyinfo= gamestop.info

#gme_companyinfo= gamestop.info
print("\n\nGamestop Company info:")
#Loop through the dictionary and print key and value
for index,(key, value) in enumerate(gme_companyinfo.items()):
    if index == 10:
        break
    print(f"{key}: {value}")


gme_data = gamestop.history(period="max")
data= gme_data.reset_index(inplace=True)
overview= gme_data.head()
print(overview)
    
    
    
url= input("Enter  URL")
if len(url) < 1:
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
    
# Step 1: Use pandas to directly read the tables from the URL, panda focuses on tables so first element it finds is a table
shit = pd.read_html(url)

# Since the revenue table on the page is the second table, we take [1] from the list
gme_revenue = shit[1]


#change the column name because both coulumns named the same
gme_revenue.columns = gme_revenue.columns.str.strip()
gme_revenue = gme_revenue.rename(columns={"GameStop Quarterly Revenue (Millions of US $)": "Date"})
gme_revenue = gme_revenue.rename(columns={"GameStop Quarterly Revenue (Millions of US $).1": "Revenue"})



#Execute the following line to remove the comma and dollar sign from the Revenue column.
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r',|\$',"", regex=True)

#Execute the following lines to remove an null or empty strings in the Revenue column.
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

# Step 2: Display the last five rows of the DataFrame
print(gme_revenue.tail())    








#defines the function make_graph. You don't have to know how the function works, you should only care about the inputs.
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    
make_graph(gme_data, gme_revenue, 'Gamestop')    