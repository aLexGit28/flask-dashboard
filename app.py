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
    pie = px.pie(
        df,
        names='Category',
        values='Hours',
        title='Time Spent Per Category',
        hole=0.4,  # optional: donut style
    )

    pie.update_traces(
    textinfo='percent+label',
    hoverinfo='label+percent+value',
    marker=dict(line=dict(color='#000000', width=2), colors=['#ff9999', '#66b3ff', '#99ff99'])  # Adding color gradient to slices
)


    pie.update_layout(
        legend_title_text='Activity Category',
        title_x=0.5,  # center the title
        title_y=0.95,  # adjust the title position
        margin=dict(t=50, b=50, l=50, r=50),  # adjust margins
        height=400,  # adjust height
        width=600,  # adjust width  
    )
    
    pie_html = pie.to_html(full_html=False)


    hist = px.histogram(
    df,
    x='Category',
    y='Hours',
    title='Hours by Category',
    color='Category',
    histfunc='sum'
)

    hist.update_layout(
        bargap=0.0,  # pure histogram style (you already loved this 😘)
        legend_title_text='Activity Category'
    )

    hist.update_traces(
        hovertemplate='Category: %{x}<br>Total Hours: %{y}'
    )
    hist_html = hist.to_html(full_html=False)


    bar = px.bar(
        df,
        x='Category',
        y='Hours',
        title='Time Spent by Category',
        color='Category',
        text='Hours'
    )

    bar.update_traces(
        texttemplate='%{text}',
        textposition='outside',
        hovertemplate='Category: %{x}<br>Hours: %{y}'
    )

    bar.update_layout(
        uniformtext_minsize=8,
        uniformtext_mode='hide',
        bargap=0.2,
        legend_title_text='Activity Category'
    )

    bar_html = bar.to_html(full_html=False)


    from_date = request.form.get('from_date')
    to_date = request.form.get('to_date')

    # Convert the Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    if from_date:
        df = df[df['Date'] >= pd.to_datetime(from_date)]
    if to_date:
        df = df[df['Date'] <= pd.to_datetime(to_date)]

    return render_template('dashboard.html', pie_chart=pie_html, histogram=hist_html, bar_chart=bar_html)


if __name__ == '__main__':
    app.run(debug=True, port=5500)
