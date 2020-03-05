[//]: # (Image References)

[image1]: ./static/images/BostonHousingPic.JPG "Boston Housing Image"

## Machine Learning Project: Boston Housing Median House Value Prediction

![Boston Housing Image][image1]

## Deployment Details

The project is actively deployed on Heroku at the following link: https://boston-housing-data-prediction.herokuapp.com/

The application makes use of Heroku, an open source PaaS, with a Bootstrap framework. The CSS and HTML was customized for simplicity, but maintain the connectivity between the various components. All documents maintained on Github.

In order for the application to work, we need to provide the (1) model, our Decision Tree Regressor, (2) the fitted StandardScaler and (3) supporting data to the application, so that they can be re-compiled and used. The specific python packages that were used in code development, are also provided in requirement.txt for the Heroku Flask application to use.

The Flask directory layout has "Templates", "Static", procfile, and app.py. The "templates" directory contains the HTML framework for each site, and the appropriate code to interact with the app.py (which loads data, model artifacts, predicts, and renders/returns the site as designed.) "Static" contains statics files, images, models, and data. Procfile is a supporting file instructing which application (here app.py) to use. All are uploaded to Heroku in which this application is hosted.

## General Project Details

## Proposal and Final Project Paper

Problem Statement: The aim is to accurately predict the median housing values using machine learning algorithms.

Evaluation Metrics: Evaluation metrics will be using r-squared for this regression task. Rather than using RMSE or MSE, r-squared is interpretable and common.

The final model selected was a Decision Tree Regression, with 81% and 77% on the train and test data, respectively. 

## Requirements
See the requirements.txt file for necessary packages. 

## Data
See directories "static" for supporting data/files, and "templates" for HTML templates.

## Outputs

The jupyter notebook will house all data, and contain code for creating all model outputs.
The "app.py" file contains the flask application code, using the HTML templates, saved models, and stored (pickled) data.

## Motivation
  
Fun project to practice various machine learning algorithms.

## License
### The MIT License (MIT)
### Copyright (c) 2020 Ben Jacobson
```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```