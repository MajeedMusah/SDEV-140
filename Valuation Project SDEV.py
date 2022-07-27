"""Date: 7/18
Author:  Majeed Musah
Version: 1.1
Name:    Intrinsic Value of stock Calculation 
Summary: A program that values a company using the Discount Cash Flow Model.
         This is done first by calculating past revenue generated 
         and then forecast future company revenues
         to see whether it will have a return on investment 5% or above"""

import yfinance as yf #upload yahoofinance realtime information
import pandas as pd

#Apple intrinsic value calculation 

aapl = yf.Ticker("aapl") #Retrieve relevant information of company 'Apple' and store in variable aapl
outstandingShares = aapl.info['sharesOutstanding'] #Fetches number of shares
cashflowdata = aapl.cashflow
rounded = (cashflowdata / 1000)
print (rounded)


#Assumptions:
required_rate = 0.05 #rate the investor wants to have to invest
perpetual_rate= 0.02 #rate at which we expect the company to grow indefinitley (GDP growth rate of US)
cashflowgrowthrate =0.03 #rate at which company has grown in cash till now

years = [1,2,3,4] #Number of years in the past to be used to calculate same amount of years in the future

"To calculate cashflow, we must subtract operations from expenses"
OperatingCashFlow  = [ 77434000, 69391000, 80674000, 104038000]  #amount of cash from operations in 1000s of $ (billions) #2017-2021               
CapitalExpenditure = [ 13313000, 10495000, 73090000, 11085000] #capital expenditure - expenses made to create operating cashflows #2017-2021                  
freeCashflow = [(77434000 - 13313000), (69391000 - 10495000), (80674000 - 73090000), (104038000 - 11085000)]   #difference between lists
"could not figure out how to subtract int between lists, thus had to do it manually to get freeCashflow"
print (freeCashflow)

"Using the perpetual rate to find the perpetual value of Apple company" #(beyond year 4)
companyValue = freeCashflow[-1] * (1 + perpetual_rate) / (required_rate - perpetual_rate)  #Terminal Value (We always use most recent cashflow to calculate this)
print("the perpetual value of company is" , companyValue)  #The answer should be in trillions, since apple is a trillion dollar company



futurefreecashflow = []
"expected money for the next 4 years"
discountfactor = [] 
"remove inflation and interest rate factors"
DiscountedCash= []


"Predicting how much true cash will be coming in the next 4 years "
for year in years:                                                    # loop starts with cashflow apple earned in 2021 until years end
    """Formula for calculating future cashflow below"""
    cashflow = freeCashflow[-1]  * (1+ cashflowgrowthrate)**year   
    futurefreecashflow.append(cashflow)                            #adding the above calculated amount to variable #futurefreecashflow
    discountfactor.append((1+required_rate)**year)                 #calculating discount factor (how much we are reducing the cashflow due to inflation and interest rate)
print("Projected amount of cash for the next 4 years respectively: ", futurefreecashflow)
print("cashflow will be reduced  yearly by the following rates:   " , discountfactor)



"Here we discount the future cashflow with the predicted inflation factors to get the real value of cashflows"
"A loop will be used, and an append method to record the discounted cash flows for the next 4 years"
for i in range( 0, len(years)):  
    DiscountedCash.append(futurefreecashflow[i]/discountfactor[i])  
print("YEAR: ", years, " Discounted cashflow: ", DiscountedCash)


"Discounting the company value apple to reflect inflation and interest rate effects"
DiscountedCompanyValue = companyValue/(1 + required_rate)**4  #discount factor at year 4
"Adding this new value to our discounted values"
DiscountedCash.append(DiscountedCompanyValue)  
print("New Discount is", DiscountedCash)    

"Calculating today's values" 
todaysvalue = sum(DiscountedCash)
print("Today's value of company is ", todaysvalue)

"calculating stock price"
fairvalue = (todaysvalue * 1000 ) / outstandingShares               
print("The fair value of AAPL is ${}".format(round(fairvalue,2)))