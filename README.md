# Machine Learning Project - Instacart Market Basket Analysis 
The models make predictions on each user's next order items based on history orders 

## Introduction 
Our approach consists two parts: 
1. Predict repurchased products using XGBoost 
2. Predict new products with collaborative filtering

## Predict repurchased products using XGBoost
### Features 
- Total buy 
- Period withour repurchase 
- Chance and Ratio 

## Predict new products with collaborative filtering
### Models 
- TF-IDF
- Probabilistic matrix factorization 
- Non-negative matrix factorization
- NMF with co-clustering 

## Evaluation 
evaluation metric used: Mean average precision
![Screenshot 2021-05-11 at 12 40 08 PM](https://user-images.githubusercontent.com/35590255/117759239-070a9e00-b256-11eb-9ecf-f7a99be8d983.jpg)

The recommendation consists of top 5 products from part 1 (reordered) and top 3 new products from part 2. 
The test performance is 47.32%, indicating that with our models, the user will purchase every second product recommended on average.

## Content 
This repo contains source code for XGBoost model to predict repurchased products and project report. Please refer to the report for further details. 

## Reference 
- Instacart Market Basket Analysis Kaggle competition, including detailed requirements and data:
- https://www.kaggle.com/c/instacart-market-basket-analysis/overview

- Adapt from 2nd place solution: 
- https://github.com/KazukiOnodera/Instacart 
- https://medium.com/kaggle-blog/instacart-market-basket-analysis-feda2700cded
