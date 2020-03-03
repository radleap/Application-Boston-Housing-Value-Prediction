import numpy as np
from flask import Flask, request, jsonify, render_template,Response
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
model = pickle.load(open('static/artifacts/model.pkl', 'rb'))

# loading original dataset for use in plotting
with open('static/dataset.pkl', 'rb') as file:
    original_data = pickle.load(file)

# original homepage
@app.route('/')
def home():
    return render_template('index.html')

# function to take the prediction and return the plot

def create_figure(prediction):

    sns.set(color_codes=True) #need to load seaborn
    sns.set(rc={'figure.figsize':(12,10)})
    ax = sns.distplot(original_data) # from pickled data
    plt.axvline(prediction, 0,0.75, linestyle='--', color='r', label='Prediction')
    plt.xlabel('Median Home Value (USD, Thousands)')
    plt.ylabel('Density')
    plt.xlim(0, 55)
    figure = ax.get_figure()
    return figure

@app.route('/plot.png')
def plot_png(prediction=60):
    fig = create_figure(prediction)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

# after receiving prediction renders output page
@app.route('/predict',methods=['POST'])
def predict():
    #taking the function input and using model to predict
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    plot_png(prediction)
    output_prediction = round(prediction[0], 2)*1000 #to put in thousands of dollars

    if output_prediction >= 0:
        output_prediction = round(prediction[0], 2)*1000
    else:
        output_prediction = 0
    #plot = create_figure(float(prediction))
    #plot2 = makeimgdata(plot)
    return render_template('output.html', prediction_text='The predicted median housing value is $ {}'.format(output_prediction)) #, prediction_image = plot2)

# https://stackoverflow.com/questions/50728328/python-how-to-show-matplotlib-in-flask
#needed to set the xlim to fix a bug but ok, could not reroute the prediction out before visual page loaded

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

if __name__ == "__main__":
    app.run()
