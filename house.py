# flask , pandas, scikit-learn , pickle-mixin
from flask import Flask , render_template , request
import pandas as pd
import pickle

app = Flask(__name__)

model=pickle.load(open("houserent1.pkl",'rb'))
house = pd.read_csv("clean22houselast.csv")

@app.route('/')
def index():
    bhk = sorted(house['BHK'].unique())
    size = sorted(house['Size'].unique())
    city = sorted(house['City'].unique())
    furnish = sorted(house['Furnishing Status'].unique())
    tenant = sorted(house['Tenant Preferred'].unique())
    bath = sorted(house['Bathroom'].unique())

    return render_template('index.html', BHK=bhk , Size=size , City=city ,Furnished=furnish, Tenant=tenant,Bathroom=bath )


@app.route('/predict', methods=['POST'])
def predict():
    bhk = request.form.get('BHK')
    size = int(request.form.get('size'))
    city = request.form.get('City')
    furnishing_status = request.form.get('Furnishing Status')
    tenant_preferred = request.form.get('Tenant Preferred')
    bathroom = request.form.get('Bathroom')
    print(bhk, size, city, furnishing_status, tenant_preferred, bathroom)

    prediction = model.predict(pd.DataFrame([[bhk, size, city, furnishing_status, tenant_preferred, bathroom]], columns= ['BHK', 'Size'
    , 'City','Furnishing Status', 'Tenant Preferred', 'Bathroom']))

    return str(prediction[0])



if __name__=="__main__":
    app.run(debug=True)
