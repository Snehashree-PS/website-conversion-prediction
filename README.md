# Website User Behavior & Conversion Prediction

## Objective
To predict whether a website visitor will make a purchase based on their browsing behavior.

## Dataset
Online Shoppers Intention Dataset (Kaggle)

Dataset Link:
https://www.kaggle.com/datasets/henrysue/online-shoppers-intention

## Features Used
- PageValues
- ExitRates
- BounceRates
- ProductRelated
- ProductRelated_Duration

## Model Used
Random Forest Classifier

## Methodology
1. Data preprocessing and label encoding  
2. Train-test split  
3. Model training using Random Forest  
4. Evaluation using accuracy and classification report  

## Deployment
- Model saved using pickle (model.pkl)  
- Web application built using Streamlit (app.py)  
- Users enter values and get real-time prediction  

## Output
- User WILL Purchase  
- User will NOT Purchase  

## How to Run
streamlit run app.py

## Result
The model achieved an accuracy of approximately **89%**, indicating strong performance in predicting user purchase behavior.

## Conclusion
The developed model effectively identifies potential customers based on their browsing patterns.  
This can help businesses:
- Improve targeted marketing strategies  
- Enhance user experience  
- Increase overall conversion rates  
