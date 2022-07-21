"""Date: 7/18
Author:  Majeed Musah
Version: 1.1
Name:    Intrinsic Value Calculation 
Summary: A program that values a company using the DCF Model.
         This is done first by calculating past revenue generated 
         and then forecast future company revenues
         to see whether it will have a return on investment 5% or above"""



import yfinance as yf 
"uploading yahoofinance realtime information"


#Apple intrinsic value calculation
"Retrieve relevant information of company 'Apple' and store in variable aapl"
aapl = yf.Ticker("aapl") 
outstandingShares = aapl.info['SharesOutstanding'] #Fetches number of shares

#Assumptions:
required_rate = 0.05 #rate the investor wants to have to invest
perpetual_rate= 0.02 #rate over time horizon
cashflowgrowthrate =0.03 #rate at which company  growing in valaution

years = [1,2,3,4] #Number of years in the past to be used to calculate same amount of years in the future

"To calculate cashflow, we must subtract operations from expenses"
OperatingCashFlow = [104038000, 80674000, 69391000, 77434000] #amount of cash from operations in 1000s of $ (billions)
CAPEX =  [10633000, 11085000, 73090000, 10495000, 13313000 ]   #CAPEX is short form of capital expenditure - expenses made to create operating cashflows

"Subtract cash from expenses in every year, respectively" # a loop may be required to subtract and store it in a new list 
freeCashFlow = OperatingCashFlow - CAPEX

futurefreecashflow= [] 
"expected money for the next 4 years"
discountfactor = []  
"interest rates and inflation reduces the value of money"
discountedfuturecash = [] 
"cash free of inflation and inerest"