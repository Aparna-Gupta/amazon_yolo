# Linguistic harbingers of sales on e-commerce websites

#### Abstract
Millions of users buy regular household items from the Amazon Marketplace every day. Most of these products are not much different from their competitors in terms of brand, pricing or specifications. Various product factors influence a user to choose one product among many similar products, product description and reviews being the two most prominent factors. We want to find out how much these two factors influence a user’s decision in choosing a product over its competitors.

Report (Work-In-Progress) : [Report.pdf](https://github.com/pratikone/amazon_yolo/blob/master/Report.pdf)

#### Dataset 

[ Amazon Product Reviews Dataset (Beauty, Food, Health) ](http://jmcauley.ucsd.edu/data/amazon/) 


#### Data Pipeline
![alt text](https://github.com/pratikone/amazon_yolo/blob/master/images/data_regression.jpg "Data pipeline  Regression")

![alt text](https://github.com/pratikone/amazon_yolo/blob/master/images/data_classification.jpg "Data pipeline  Classification")

#### Models and Results   

![alt text](https://github.com/pratikone/amazon_yolo/blob/master/images/model_classification.jpg "Data pipeline  Regression")

![alt text](https://github.com/pratikone/amazon_yolo/blob/master/images/ROC.jpg "ROC")

![alt text](https://github.com/pratikone/amazon_yolo/blob/master/images/words.jpg "ROC")


## How to run

1. Install Jupyter Notebook
2. Install required libraries of scikit-learn, numpy, pandas, keras, tensorflow, empath, vader, stanford-nlp
3. For classification, run `ClassificationAnalysisPipeline.ipynb`
4. For regression, run `RegressionAnalysisPipeline.ipynb`
5. For BOW, run `BOWModel.ipynb`