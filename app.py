from flask import Flask,request,render_template
import pickle


app=Flask(__name__)
model=pickle.load(open('rf_ht.pkl','rb'))


@app.route('/',methods=['GET'])
def display():
    return render_template('display.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        year=int(request.form['year'])
        year=2020-year
        present_price=float(request.form['present_price'])
        kms_driven=int(request.form['kms_driven'])
        owner=int(request.form['owner'])
        fuel_type=request.form['fuel_type']
        if fuel_type=='Petrol':
            fuel_type_petrol=1
            fuel_type_diesel=0
        elif fuel_type=='Diesel':
            fuel_type_petrol = 0
            fuel_type_diesel = 1
        else:
            fuel_type_petrol = 0
            fuel_type_diesel = 0
        seller_type=request.form['seller_type']
        if seller_type=='Individual':
            seller_type_individual=1
        else:
            seller_type_individual = 0
        transmission_type=request.form['transmission_type']
        if transmission_type=='Manual':
            transmission_type_manual=1
        else:
            transmission_type_manual=0

        prediction=model.predict([[present_price,kms_driven,owner,year,fuel_type_diesel,fuel_type_petrol,seller_type_individual,transmission_type_manual]])
        output=round(prediction[0],2)
        print(output)

        if output<0:
            return render_template('display.html',prediction_texts="Sorry u can't sell the car")
        else:
            return render_template('display.html', prediction_texts="YOU CAN SELL THE CAR AT {}".format(output))

    else:
        return render_template('display.html')



if __name__=='__main__':
    app.run(port=8000)

