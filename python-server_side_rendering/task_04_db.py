from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def read_sqlite_data():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    data = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return data

@app.route('/products')
def display_products():
    source = request.args.get('source', '')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    try:
        if source == 'json':
            products = read_json_file('products.json')
        elif source == 'csv':
            products = read_csv_file('products.csv')
        else:  # source == 'sql'
            products = read_sqlite_data()

        if product_id:
            products = [p for p in products if str(p['id']) == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")

        return render_template('product_display.html', products=products)
    except Exception as e:
        return render_template('product_display.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
