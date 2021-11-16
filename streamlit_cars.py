# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:55:29 2021

@author: annel
"""

import streamlit as st
st.title('Hello Wilders, welcome to my df_cars!')

st.write("I enjoy to show you streamlit possibilities")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.write("Here is df_cars:")
df_cars = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
st.write(df_cars)

'''
'''
continent_car = st.radio("Which continent of origin would you like to explore?", ('US', 'Europe', 'Japan'))
if continent_car == 'US':
    df_cars = df_cars[df_cars.continent == ' US.']
if continent_car == 'Europe':
    df_cars = df_cars[df_cars.continent == ' Europe.']
if continent_car == 'Japan':
    df_cars = df_cars[df_cars.continent == ' Japan.']


cars_scatter = sns.scatterplot(data=df_cars, x='hp', y='cubicinches')
plt.xlabel('Horsepower')
plt.ylabel('Cubic inches')
plt.title('Cars distribution by continent given there horsepower and cubic inches')
st.pyplot(cars_scatter.figure)

'''Cubic inches and horsepower seem to be positively correlated. The most powerfull cars are american cars.'''

'''
'''

cars_heatmap = sns.heatmap(data = df_cars.corr(), cmap="RdYlGn", vmax=1, vmin=-1, center=0, linewidths=.5)
plt.title('Corelation between different cars features')
st.pyplot(cars_heatmap.figure)

'''
Car power and mpg consumption are negatively correlated: the more powerfull is the car, the more important consumption is.
Car weight and power are positively correlated : the heavier a car is, the most powerfull it will be.
These correlations are stronger for american cars.
'''
