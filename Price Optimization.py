import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
%matplotlib inline

# load data
import pandas as pd
beef = pd
beef.head()

# revenue
revenue = quantity * price 

# profit
profit = revenue - cost

# revised profit function
profit = quantity * price - cost

# demand curve
sns.lmplot(x = "Price", y = "Quantity", 
data = beef, fig_reg = True, size = 4)

# fit OLS model
model = ols("Quantity ~ Price", data = beef).fit()
# print model summary
print(model.summary())

# plugging regression coefficients
quantity = 30.05 - 0.0465 * price 
# profit function 
profit = (30.05 - 0.0465 * price) * price - cost

 # a range of diffferent prices to find the optimum one
Price = [320, 330, 340, 350, 360, 370, 380, 390]
# assuming a fixed cost
cost = 80
Revenue = []
for i in Price:
     quantity_demanded = 30.05 - 0.0465 * i   
     # profit function
     Revenue.append((i-cost) * quantity_demanded)
# create data frame of price and revenue
profit = pd.DataFrame({"Price": Price, "Revenue": Revenue})
#plot revenue against price
plt.plot(profit["Price"], profit["Revenue"])

 # price at which revenue is maximum
profit[profit['Revenue'] == profit[['Revenue'].max()]
