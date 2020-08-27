import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

#from bokeh.plotting import figure, show
#from bokeh.io import output_notebook
#from bokeh.tile_providers import CARTODBPOSITRON, get_provider
# output_notebook()

st.title('Covid 19 Dashboard')

df_usconf = pd.read_csv('covid19_small.csv')
#df_usconf = df_usconf[df_usconf['Province'].isin(['California', 'New York'])]
#df_usconf.to_csv('covid19_small.csv')

ca = df_usconf[df_usconf['Province'] == 'California']
ny = df_usconf[df_usconf['Province'] == 'New York']

st.text('California')
st.write(ca.tail())

st.text('New York')
st.write(ny.tail())

st.text('plot using streamlit line chart')
st.line_chart(ca.Cases)
st.line_chart(ny.Cases)

st.text('plot using bokeh')
df_ca = pd.DataFrame({
    'date': pd.to_datetime(ca.Date),
    'cases': ca.Cases
})

df_ny = pd.DataFrame({
    'date': pd.to_datetime(ny.Date),
    'cases': ny.Cases
})


# if you don't have bokeh installed, you can comment these out.
#p = figure(plot_width=800, plot_height=400, x_axis_type='datetime')
#p.line(df_ca['date'], df_ca['cases'], line_width=4, color='blue', alpha=0.3)
#p.line(df_ny['date'], df_ny['cases'], line_width=4, color='red', alpha=0.3)
# p.line(ny['Date'], ny['Cases'], line_width=4, color='red')
#st.bokeh_chart(p, use_container_width=True)

