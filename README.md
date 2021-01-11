# housing-prices-prediction
Predicting Housing Prices of King County, USA


In this project, we use Linear Regression to predict housing prices.
We use [this](https://www.kaggle.com/harlfoxem/housesalesprediction) dataset from kaggle. This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015. It's a good dataset for implementing regression models.

### Column in the dataset:  <BR>
id - Unique ID for each home sold <BR>
date - Date of the home sale <BR>
price - Price of each home sold <BR>
bedrooms - Number of bedrooms <BR>
bathrooms - Number of bathrooms, where .5 accounts for a room with a toilet but no shower <BR>
sqft_living - Square footage of the apartments interior living space <BR>
sqft_lot - Square footage of the land space <BR>
floors - Number of floors <BR>
waterfront - A dummy variable for whether the apartment was overlooking the waterfront or not <BR>
view - An index from 0 to 4 of how good the view of the property was <BR>
condition - An index from 1 to 5 on the condition of the apartment, <BR>
grade - An index from 1 to 13, where 1-3 falls short of building construction < and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.<BR>
sqft_above - The square footage of the interior housing space that is above ground level <BR>
sqft_basement - The square footage of the interior housing space that is below ground level <BR>
yr_built - The year the house was initially built <BR>
yr_renovated - The year of the house’s last renovation <BR>
zipcode - What zipcode area the house is in <BR>
lat - Lattitude <BR>
long - Longitude <BR>
sqft_living15 - The square footage of interior housing living space for the nearest 15 neighbors <BR>
sqft_lot15 - The square footage of the land lots of the nearest 15 neighbors
  

### Feature Selection:
We need to chose only the pertinent features for our multi-variate linear regression. 
We implement a correlation matrix of features and choose the features that are highly correlated with the "price", which is our target (i.e. the column we wish to predict). 

#### Correlation Matrix: 
![Correlation Matrix](/images/correlation_matrix.png)

From the correlation matrix we can see that following features are highly correlated with the target. 

*   Bathrooms. (0.53)
*   sqft_living (0.7)
*   sqft_above (0.61)
*   grade(0.67)
*   sqft_living15 (0.59)

We only chose features whose absolute correlation is greater than 0.5.

Let us visualize how these features vary with the target:

![Features Visualization](/images/features_visualization.png)

### Model Evaluation:

The R^2 training score for our model is 0.5822.
The R^2 testing score for our model is 0.5868.

This is an alright score. It means that the model is able to explain 58% of variability of the prediction. 
Higher R^2 score doesn't necessarily indicate a better predicting model.
[This](https://statisticsbyjim.com/regression/interpret-r-squared-regression/) article does a good job of explaining how to interpret the R^2 score .

#### Other Scores:

Mean Absolute Error (MAE) 0.2752744094198206 <br>
Mean Squared Error (MSE) 0.11730201062197114 <br>
Root Mean Squared Error (RMSE) 0.3424938110710486 <br>

### Resulting Predictions:

![Predictions](/images/predictions.png)


This scatter plot by far gives the best visual idea of the performance of the model. Ideally we should've obtained a straight (x=y) line, as that would imply that predicted prices are equal to actual prices. 





#### Instructions to run:

##### Softare Prerequisites: None

1) Open the "King_County_Housing_Prices.ipynb" notebook in google colab by clicking the 'Open in Colab' badge. 
2) Run all the cells by clicking "Runtime>>Run all" from the file menu.




