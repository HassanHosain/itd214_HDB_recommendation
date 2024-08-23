# itd214_HDB_recommendation
This is a recommendation model using Association rules which connects to a streamlit application where user selects the preferences
---
layout: post
author: Name
title: "Applied Data Science Project Documentation"
categories: ITD214
---
## Project Background
My team worked on the the HDB resale prices, as we realise couples in Singapore require insights into the every increasing cost of HDB resale prices in Singapore. Therefore to give some form of insights to HDB purchase prices will be extremely helpful.

Thus our business objective is "Empowering married couples with predictive insights into HDB resale prices to best prepare them in decision-making and strategic planning."
The individual objective for me to provide a form of recommendation model to the married couples by delving into the data and see which flats wil be suitable for them.

## Work Accomplished
I manage to create a Streamlit application which consist a few drop down fields (distance to mrt, town location, floor area, flat type and etc) that the users can select. The fields are non mandatory and they may select No preference as the option. Once the user selects the required fields and click submit. The Streamlit application will then communicate with the model.

The model is an association rule model, using the FPGrowth algorithm. FP-Growth is an alternative to Apriori that avoids the costly candidate generation step by using a compact data structure called the FP-tree (Frequent Pattern Tree). It recursively extracts frequent itemsets from the tree structure.

**Benefits of FP-Growth are:**
- More efficient than Apriori algorithm, especially for large datasets with many items and transactions.
- Reduces the need to scan the database multiple times.

### Data Exploration
In the 1015618c_Reccomendation_prep.ipynb file, firstly i did some exploratory analysis first to understand better, utilizing libraries like pandas, numpy, matplotlib etc. There are 5 csv files, and went merged there are a total of 826,581 rows, 11 columns, year spanning from 1990-2020, 7 unique flat types, 20 unique flat models and 27 unique towns in the dataset.
![alt text](images/EDA_pt1.JPG) ![alt text](images/EDA_pt2.JPG)

I have also plotted visualization barcharts to showcase in year 1997,1998 thera are huge spikes of transactions of hdb purchases , but the average throughout the months is mostly consistent.
![alt text](images/EDA_pt3.JPG)

Observations like the 4-room flats followed by 3-room flats are most popular flat types, also Model A, Improved is the top 2 popular flat models.
![alt text](images/EDA_pt4.JPG)

### Data Preparation

### Modelling
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce bibendum neque eget nunc mattis eu sollicitudin enim tincidunt. Vestibulum lacus tortor, ultricies id dignissim ac, bibendum in velit. Proin convallis mi ac felis pharetra aliquam. Curabitur dignissim accumsan rutrum. In arcu magna, aliquet vel pretium et, molestie et arcu. Mauris lobortis nulla et felis ullamcorper bibendum. Phasellus et hendrerit mauris. Proin eget nibh a massa vestibulum pretium. Suspendisse eu nisl a ante aliquet bibendum quis a nunc. Praesent varius interdum vehicula. Aenean risus libero, placerat at vestibulum eget, ultricies eu enim. Praesent nulla tortor, malesuada adipiscing adipiscing sollicitudin, adipiscing eget est.

### Evaluation
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce bibendum neque eget nunc mattis eu sollicitudin enim tincidunt. Vestibulum lacus tortor, ultricies id dignissim ac, bibendum in velit. Proin convallis mi ac felis pharetra aliquam. Curabitur dignissim accumsan rutrum. In arcu magna, aliquet vel pretium et, molestie et arcu. Mauris lobortis nulla et felis ullamcorper bibendum. Phasellus et hendrerit mauris. Proin eget nibh a massa vestibulum pretium. Suspendisse eu nisl a ante aliquet bibendum quis a nunc. Praesent varius interdum vehicula. Aenean risus libero, placerat at vestibulum eget, ultricies eu enim. Praesent nulla tortor, malesuada adipiscing adipiscing sollicitudin, adipiscing eget est.

## Recommendation and Analysis
Explain the analysis and recommendations

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce bibendum neque eget nunc mattis eu sollicitudin enim tincidunt. Vestibulum lacus tortor, ultricies id dignissim ac, bibendum in velit. Proin convallis mi ac felis pharetra aliquam. Curabitur dignissim accumsan rutrum. In arcu magna, aliquet vel pretium et, molestie et arcu. Mauris lobortis nulla et felis ullamcorper bibendum. Phasellus et hendrerit mauris. Proin eget nibh a massa vestibulum pretium. Suspendisse eu nisl a ante aliquet bibendum quis a nunc. Praesent varius interdum vehicula. Aenean risus libero, placerat at vestibulum eget, ultricies eu enim. Praesent nulla tortor, malesuada adipiscing adipiscing sollicitudin, adipiscing eget est.

## AI Ethics
Discuss the potential data science ethics issues (privacy, fairness, accuracy, accountability, transparency) in your project. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce bibendum neque eget nunc mattis eu sollicitudin enim tincidunt. Vestibulum lacus tortor, ultricies id dignissim ac, bibendum in velit. Proin convallis mi ac felis pharetra aliquam. Curabitur dignissim accumsan rutrum. In arcu magna, aliquet vel pretium et, molestie et arcu. Mauris lobortis nulla et felis ullamcorper bibendum. Phasellus et hendrerit mauris. Proin eget nibh a massa vestibulum pretium. Suspendisse eu nisl a ante aliquet bibendum quis a nunc. Praesent varius interdum vehicula. Aenean risus libero, placerat at vestibulum eget, ultricies eu enim. Praesent nulla tortor, malesuada adipiscing adipiscing sollicitudin, adipiscing eget est.

## Source Codes and Datasets
Upload your model files and dataset into a GitHub repo and add the link here. 
