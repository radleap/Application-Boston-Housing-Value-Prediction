import numpy as np
from flask import Flask, request, jsonify, render_template,Response
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
model = pickle.load(open('static/artifacts/model.pkl', 'rb'))
scaler_f =  pickle.load(open('static/artifacts/std_scaler_final_model.pkl', 'rb')) #unstable, not work

# loading original dataset for use in plotting visual
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

    # extracting and preparing our categorical variable RAD, so it matches required model input of shape 15 encoded
    # log(CRIM) NOX RM lg(DIS) PTRATIO log(B LSTAT RAD - only RAD is categorical
    rad_list = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0 ,8.0 ,24.0] # possible values
    match = final_features[-1][-1] #taking RAD user input only
    rad_user = [1.0 if i==match else 0.0 for i in rad_list] # recreating list with 1.0 where true, else 0

    # applying log transformations to CRIM, DIS and B, pverwriting in place
    final_features = list(final_features[-1][:-1])
    final_features[0] = np.log(final_features[0]) #log applied to CRIM, position 0
    final_features[3] = np.log(final_features[3]) #log applied to DIS, position 3
    final_features[5] = np.log(final_features[5]) #log applied to B, position 5

    # applying the saved/loaded StandardScaler object to the new continuous,logged data
    final_features = scaler_f.transform(np.asarray(final_features).reshape(1, -1)) #returns non-list, need to correct

    final_features = final_features.tolist()[0] + rad_user #recreating the list, getting correct format, and combining

    final_features = np.asarray(final_features).reshape(1, -1) # reshaping for prediction object requirements, back to array

    prediction = model.predict(final_features)
    plot_png(prediction)
    output_prediction = round(prediction[0], 2)*1000 #to put in thousands of dollars

    if output_prediction >= 0:
        output_prediction = round(prediction[0], 2)*1000
    else:
        output_prediction = 0
    return render_template('output.html', prediction_text='The predicted median housing value is $ {}'.format(output_prediction)) #, prediction_image = plot2)

#needed to set the xlim to fix a bug but ok, could not reroute the prediction out before visual page loaded

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return render_template('about.html')

if __name__ == "__main__":
    app.run()
