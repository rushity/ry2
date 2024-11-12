from flask import Flask, render_template, request
from prettytable import PrettyTable
import cl  # Import your logic from cl.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Retrieve data from the form
    total_leaves = int(request.form['total_leaves'])
    leaves_per_month = int(request.form['leaves_per_month'])
    months = int(request.form['months'])

    # Initialize data as done in cl.py
    aa = total_leaves
    l = leaves_per_month
    n = months
    a = [[0 for _ in range(5)] for _ in range(n)]

    # Logic from cl.py to populate 'a' array
    for i in range(n):
        a[i][1] = int(request.form[f'leaves_month_{i+1}'])
        a[i][0] = i + 1

    for i in range(n):
        a[i][4] = aa

        if a[i][1] >= l:
            if a[i][4] <= (l - 1):
                a[i][2] = a[i][4]
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]
            else:
                a[i][2] = l
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]
        else:
            if a[i][4] < (l - 1):
                a[i][2] = a[i][4]
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]
            else:
                a[i][2] = a[i][1]
                a[i][3] = a[i][1] - a[i][2]
                a[i][4] = aa - a[i][2]
                aa = a[i][4]

    # Prepare data for HTML table
    table_data = []
    for i in range(n):
        table_data.append([i + 1, a[i][1], a[i][2], a[i][3], a[i][4]])

    return render_template('result.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
