#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cal_avg_precision(actual, predicted):
    '''
    @actual: array; groundtruth/the products the user actual purchased
    @predicted: array; the recommended products ordered in decreasing order of scores/probability
    
    @return: float; average precision score 
    '''
    score = 0.0
    num_hits = 0.0

    for i,p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)

    if num_hits == 0.0:
        return 0.0

    return score / num_hits

def get_user_product_matrix(user_product_prior):
    '''
    Create Product User Matrix with entries as quantities / number of orders containing the product by the user
    '''
    user_product_matrix = scipy.sparse.coo_matrix((user_product_prior['quantity'],
                                             (user_product_prior['product_id'].astype('category').cat.codes.copy(),
                                              user_product_prior['user_id'].astype('category').cat.codes.copy())))
    return user_product_matrix

