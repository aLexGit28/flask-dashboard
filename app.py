from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Load CSV
    df = pd.read_csv('data.csv')

    # Create Pie Chart
    pie = px.pie(df, names='Category', values='Hours', title='Time Spent Per Category')
    pie_html = pie.to_html(full_html=False)

    # Create Histogram
    hist = px.histogram(df, x='Category', y='Hours', title='Hours by Category', color='Category')
    hist_html = hist.to_html(full_html=False)

    return render_template('dashboard.html', pie_chart=pie_html, histogram=hist_html)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
