from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

@app.route('/products')
def display_products():
    source = request.args.get('source', '')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = read_json_file('products.json')
    else:
        products = read_csv_file('products.csv')

    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
