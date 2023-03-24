# %% [markdown]
# # REIT STOCK ANALYSIS

# %% [markdown]
# In this project, you will analyze Real Estate Investment Trusts, commonly known as REITs. REITs are companies that own or operate real estate that produces income. REITs, like the stocks of regular public companies, are traded on different stock exchanges. Investing in a REIT allows you to invest in portfolios of real estate assets the same way you can invest in a company by buying its stock.
# 
# Using financial statistics and NumPy you will analyze two REITs: [Sabra Health Care REIT Inc. (NASDAQ: SBRA)](https://finance.yahoo.com/quote/SBRA/), which invests in health care real estate, and [Equity Residential (NASDAQ:EQR)](https://finance.yahoo.com/quote/EQR/), which invests in rental apartment properties.

# %% [markdown]
# The time period for analysis we will be using is `Jan 1 2018` to `Dec 31 2018`. The REIT data for SBRA (`SBRA.csv`) and EQR (`EQR.csv`) can be found in the same folder as this file.

# %% [markdown]
# 1. Import the numpy module as np

# %%
import numpy as np

# %% [markdown]
# 2. Load the adjusted closings for SBRA

# %%
adj_closings_SBRA = np.loadtxt("SBRA.csv", delimiter=',')
print(adj_closings_SBRA)

# %% [markdown]
# 3. Load the adjusted closings for EQR

# %%
adj_closings_EQR = np.loadtxt("EQR.csv", delimiter=',')
print(adj_closings_EQR)

# %% [markdown]
# ## Simple Rate of Return Function

# %% [markdown]
# 4. To calculate the daily rate of return for the SBRA stock, we need the daily adjusted closing price. The formula we are using for the daily rate of return is out[n] = a[n+1] - a[n] 

# %% [markdown]
# 5. Create a function that returns the daily rate of return
# 
#     step 1. define a function named `rate_of_return`
#     
#     step 2. create parameter for  `adj_closings`
#     
#     step 3. Within the function use np.diff() and set it to the variable `daily_simple_ror`
#     
#     step 4. return `daily_simple_ror`

# %%
def simple_rate_of_return(adj_closings):
    daily_simple_ror = np.diff(adj_closings)/adj_closings[:-1]
    return daily_simple_ror


# %% [markdown]
# ## Calculate Daily Rate of Return for SBRA

# %% [markdown]
# 6. Call the function `simple_rate_of_return` with the arguments `adj_closings_sbra`. Then print the results. 

# %%
daily_simple_rate_of_return_SBRA = simple_rate_of_return(adj_closings_SBRA)
print(daily_simple_rate_of_return_SBRA)

# %% [markdown]
# ## Calculate Daily Rate of Return for EQR

# %% [markdown]
# 7. Call the function `simple_rate_of_return` with the arguments `adj_closings_eqr`. Then print the results. 

# %%
daily_simple_rate_of_return_EQR = simple_rate_of_return(adj_closings_EQR)
print(daily_simple_rate_of_return_EQR)

# %% [markdown]
# ## Calculate Average Daily Return for SBRA

# %% [markdown]
# 8. Use `np.mean()` with the argument `daily_simple_returns_sbra` to calculate the average daily return for SBRA. Then set it to the variable name `average_daily_simple_return_sbra`

# %%
average_daily_simple_return_SBRA = np.mean(daily_simple_rate_of_return_SBRA)
print(average_daily_simple_return_SBRA)

# %% [markdown]
# ## Calculate Average Daily Return for EQR

# %% [markdown]
# 9. Use `np.mean()` with the argument `daily_simple_returns_eqr` to calculate the average daily return for EQR. Then set it to the variable name `average_daily_simple_return_eqr`

# %%
average_daily_simple_return_EQR = np.mean(daily_simple_rate_of_return_EQR)
print(average_daily_simple_return_EQR)

# %% [markdown]
# ## Compare the Average Daily Return between EQR and SBRA

# %% [markdown]
# 10. Based on the average daily simple returns of EQR and SBRA, which stock is more likely to be profitable in the future?

# %% [markdown]
# 

# %% [markdown]
# ## Daily Log Returns Function

# %% [markdown]
# 11. Create a function that returns the daily rate of return
# 
#     step 1. define a function named log_returns
#     
#     step 2. create parameter for  `adj_closings`
#     
#     step 3. use np.log() to get the log of each adjusted closing price and set it to the variable `log_adj_closings`
#     
#     step 4. use np.diff() to get the diff of each daily log adjusted closing price and set it to the variable `daily_log_returns`
#     
#     step 5. return `daily_log_returns`

# %%
def log_returns(adj_closings):
    log_adj_closings = np.log(adj_closings)
    daily_log_returns = np.diff(log_adj_closings)
    return daily_log_returns

# %% [markdown]
# ## Calculate Daily Log Returns for SBRA

# %% [markdown]
# 12. Call the function `log_returns` with the arguments `adj_closings_sbra`. Set it to the variable `daily_log_returns_sbra`. Then print the results. 

# %%
daily_log_returns_SBRA = log_returns(adj_closings_SBRA)
print(daily_log_returns_SBRA)

# %% [markdown]
# ## Calculate Daily Log Returns for EQR

# %% [markdown]
# 13. Call the function `log_returns` with the arguments `adj_closings_eqr`. Set it to the variable `daily_log_returns_eqr`. Then print the results. 

# %%
daily_log_returns_EQR = log_returns(adj_closings_EQR)
print(daily_log_returns_EQR)

# %% [markdown]
# ## Annualize Daily Log Return Function

# %% [markdown]
# 14. Create a function that returns the daily rate of return
# 
#     step 1. define a function named `annualize_log_return`
#     
#     step 2. create parameter for  `daily_log_returns`
#     
#     step 3. use `np.mean()` with the argument `daily_log_returns` to calculate the average daily return. Then set it to the variable name `average_daily_log_returns`
#     
#     step 4. then multiply `average_daily_log_returns` by 250 and set it to the variable `annualized_log_return`
#     
#     step 5. return `annualized_log_return`

# %%
def annualize_log_return(daily_log_returns):
    average_daily_log_returns = np.mean(daily_log_returns)
    annualized_log_return = 250*average_daily_log_returns
    return annualized_log_return

# %% [markdown]
# ## Calculate Annualize Daily Log Return for SBRA

# %% [markdown]
# 10. Call the function `annualize_log_return` with the arguments `daily_log_returns_sbra`. Set it to the variable `annualized_log_return_sbra`. Then print the results. 

# %%
annualized_log_return_SBRA = annualize_log_return(daily_log_returns_SBRA)
print(annualized_log_return_SBRA)

# %% [markdown]
# ## Calculate Annualize Daily Log Return for EQR

# %% [markdown]
# 11. Call the function `annualize_log_return` with the arguments `daily_log_returns_eqr`. Set it to the variable `annualized_log_return_eqr`. Then print the results. 

# %%
annualized_log_return_EQR = annualize_log_return(daily_log_returns_EQR)
print(annualized_log_return_EQR)

# %% [markdown]
# ## Compare the Annualize Daily Log Return between EQR and SBRA

# %% [markdown]
# 12. Based on the differences between the Annualize Daily Log Return for EQR and SBRA, Which could be more profitable in the future and why?

# %% [markdown]
# 

# %% [markdown]
# ## Calculate Variance of Daily Log Return for SBRA

# %% [markdown]
# 13. Calculate the variance of the daily logarithmetic return for SBRA. Use the function `.var()` with the argument `log_daily_ror`. Set it to the variable `daily_varaince_sbra`. Then print the results. 

# %%
daily_variance_SBRA = np.var(daily_log_returns_SBRA)
print(daily_variance_SBRA)


# %% [markdown]
# ## Calculate Variance of Daily Log Return for EQR

# %% [markdown]
# 14. Calculate the variance of the daily logarithmetic return for EQR. Use the function `.var()` with the argument `daily_log_returns_eqr`. Set it to the variable `daily_varaince_eqr`. Then print the results. 

# %%
daily_variance_EQR = np.var(daily_log_returns_EQR)
print(daily_variance_EQR)

# %% [markdown]
# ## Compare the Variance of Daily Log Return between EQR and SBRA

# %% [markdown]
# 15. Explain which investment is more riskier based on the Variance of daily log return between EQR and SBRA ?

# %% [markdown]
# 

# %% [markdown]
# ## Calculate the Daily Standard Deviation for SBRA

# %% [markdown]
# 16. Calculate the Standard Deviation of the daily logarithmetic return for SBRA. Use the function `.std()` with the argument `daily_log_returns_sbra`. Set it to the variable `daily_sd_sbra`. Then print the results. 

# %%
daily_sd_SBRA = np.std(daily_log_returns_SBRA)
print(daily_sd_SBRA)

# %% [markdown]
# ## Calculate the Daily Standard Deviation for EQR

# %% [markdown]
# 17. Calculate the Standard Deviation of the daily logarithmetic return for EQR. Use the function `.std()` with the argument `daily_log_returns_eqr`. Set it to the variable `daily_sd_eqr`. Then print the results. 

# %%
daily_sd_EQR = np.std(daily_log_returns_EQR)
print(daily_sd_EQR)

# %% [markdown]
# ## Compare the Daily Standard Deviation between EQR and SBRA

# %% [markdown]
# 18. Has your previous variance risk assessment changed based on the Daily Standard Deviation and why?

# %% [markdown]
# 

# %% [markdown]
# ## Calculate the Correlation between SBRA and EQR

# %% [markdown]
# 19. Calculate the Correlation of the daily logarithmetic return between SBRA and ERQ assets. Use the function `.corrcoef()` with the arguments `daily_log_returns_sbra` and `daily_log_returns_eqr`. Set it to the variable `corr_sbra_eqr`. Then print the results. 

# %%
corr_SBRA_EQR = np.corrcoef(daily_log_returns_SBRA,daily_log_returns_EQR)
print(corr_SBRA_EQR)

# %% [markdown]
# ## Interpret the Correlation between SBRA and EQR

# %% [markdown]
# 20. Interpret and explain the correlation between the stocks SBRA and EQR?

# %% [markdown]
# ## Final Analysis

# %% [markdown]
# 21. Which stock would you invest in based on risk and profitability?


