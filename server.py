from flask import Flask, render_template, request
import datetime as dt

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    nombre = request.form['first_name']
    apellido = request.form['last_name'] 
    id = request.form['student_id']
    strawberry = request.form['strawberry']
    raspberry = request.form['raspberry']
    apple = request.form['apple']
    suma = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    current_datetime=dt.datetime.now()
    string_date = current_datetime.strftime("%A, %B %d, %Y")
    print(f'Cobrando a {nombre} {apellido} por {suma} frutas')
    
    return render_template("checkout.html", nombre=nombre, apellido=apellido, id=id, apple = apple, raspberry =raspberry, strawberry=strawberry, suma=suma, string_date=string_date )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")



if __name__=="__main__":   
    app.run(debug=True)    