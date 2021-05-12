# Machine Learning Project - Instacart Market Basket Analysis 
This is a school project at Singapore Management University in 2020. 

Authors: Bu Wende, Jiang Hanyu, Qi Haodi, Wang Yixing and Zhang Chengzi. 

## Introduction
The goal of the project is, given past purchases of different users, to predict the products purchased by the user in the next order.

Our approach splits the purchased products into repurchased products (i.e. the user purchase them before) and new goods. We used different models to predict each of them: <ol>
  <li>Repurchased products: XGBoost</li>
  <li>New products: Collaborative filtering using TF-IDF, Matrix Factorization, Co-Clustering</li>
</ol>

## Data
The data source is obtained from <a href='https://www.kaggle.com/c/instacart-market-basket-analysis'>Instacart Market Basket Analysis on Kaggle</a>. As we do not have the groundtruth (products purchased in the orders) for the test dataset (only prior and train), we used the train and prior set only.

The prior set contains all users' prior purchases (assuming n orders in total) and the train set contains exactly 1 order per user.  

As such, the data is split as the following: <ul>
  <li>Order 1 to n-1 from prior set is used as the training set</li>
  <li>Order n from prior set is used as the validation set</li>
  <li>Train set is used as the test set for final evaluation</li>
</ul>

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
