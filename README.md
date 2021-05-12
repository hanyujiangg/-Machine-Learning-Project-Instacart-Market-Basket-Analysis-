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

## Evaluation 
Evaluation metric used: Mean average precision (mAP)

## Predict repurchased products using XGBoost
### Features 
- Total buy 
- Period withour repurchase 
- Chance and Ratio 

## Predict new products with collaborative filtering
We explored four different approaches for collaborative filtering to predict new products purchased by users:
- TF-IDF
- Probabilistic matrix factorization (PMF)
- Non-negative matrix factorization (NMF)
- NMF with co-clustering 

### TFIDF
This approach adapts from the project done by <a href='http://cs229.stanford.edu/proj2020spr/report/Qian_Xu_You.pdf'>Kun, Xu and You</a>, where each user is treated as a document and each product is treated as a word. With TF-IDF vectors constructed, we are able to find similar users and believe they would have similar preferences and needs to recommend new products that are purchased by some to those who did not purchase before.

### PMF
We factorize the original matrix _R_, that contains _M_ products and _N_ users into latent matrices _U_ (NxK) and _V_ (MxK) where K is the number of latent factors. The original matrix _R_ is first normalized with _(x-1)/(X-1)_ where _X_ is the maximum number of purchases by a user on a product in _R_, to avoid non-convergence. Stochastic Gradient Descend is used for optimization. The performance is very poor with extremely low mAP values even after tuning.

### NMF
We employed the Scikit-Learn NMF module to factorize the matrix _R_ into _U_ and _V_. 

### Co-Clustering
As users and products are two key entities that co-exist in our case, we employed co-clustering to find clusters with both similar users and products, with <a href='https://coclust.readthedocs.io/en/v0.2.1/'>CoClust package</a>. Given a user id, we can obtain the corresponding user cluster, followed by the best user-product cluster based on _delta_kl_ value. NMF is done on the selected best user-product cluster.

One possible reason is the lack of products in the user-product cluster and therefore we explored using the user cluster with all products. However, the performance drops to 0% for some unknown reasons.

## Final Model
The recommendation consists of top 5 products from part 1 (reordered) and top 3 new products from part 2. 
The test performance is 47.32%, indicating that with our models, the user will purchase every second product recommended on average.

## Reference 
- Instacart Market Basket Analysis Kaggle competition, including detailed requirements and data:
- https://www.kaggle.com/c/instacart-market-basket-analysis/overview

- Adapt from 2nd place solution: 
- https://github.com/KazukiOnodera/Instacart 
- https://medium.com/kaggle-blog/instacart-market-basket-analysis-feda2700cded
