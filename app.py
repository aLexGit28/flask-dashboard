from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Sample data for pie chart
    pie_data = {'Category': ['Love', 'Work', 'Sleep', 'Play'], 'Hours': [6, 8, 7, 3]}
    pie_df = pd.DataFrame(pie_data)
    pie_chart = px.pie(pie_df, names='Category', values='Hours', title='How You Spend Your Day 💖')
    pie_html = pio.to_html(pie_chart, full_html=False)

    # Sample data for histogram
    values = [5, 10, 12, 15, 17, 20, 21, 23, 23, 25, 27, 30]
    hist_chart = px.histogram(values, nbins=6, title='Sample Value Distribution 📊')
    hist_html = pio.to_html(hist_chart, full_html=False)

    return render_template("dashboard.html", pie_chart=pie_html, hist_chart=hist_html)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
