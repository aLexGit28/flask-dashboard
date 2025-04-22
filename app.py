from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    df = pd.read_csv('data.csv')

    selected_categories = request.form.getlist('categories')  # Get list of selected checkboxes

    if selected_categories:
        df = df[df['Category'].isin(selected_categories)]

    # Charts
    pie = px.pie(df, names='Category', values='Hours', title='Time Spent Per Category')
    pie_html = pie.to_html(full_html=False)

    hist = px.histogram(df, x='Category', y='Hours', title='Hours by Category', color='Category', histfunc='sum')
    hist.update_layout(bargap=0.2)
    hist_html = hist.to_html(full_html=False)

    bar = px.bar(df, x='Category', y='Hours', title='Time Spent by Category', color='Category', text='Hours')
    bar.update_traces(texttemplate='%{text}', textposition='outside', hoverinfo='x+y')
    bar_html = bar.to_html(full_html=False)

    return render_template('dashboard.html', pie_chart=pie_html, histogram=hist_html, bar_chart=bar_html)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
