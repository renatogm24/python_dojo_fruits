from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total = int(request.form["strawberry"]) + int(request.form["apple"]) +int(request.form["raspberry"]) 
    print(f"Cobrando a {request.form['first_name']} por {total} frutas")
    return render_template("checkout.html", data = request.form)

@app.route('/fruits')         
def fruits():
    fruits = ["apple.png","blackberry.png","raspberry.png","strawberry.png"]
    return render_template("fruits.html", fruits = fruits)

if __name__=="__main__":   
    app.run(debug=True)    