created the main python file
import streamlit 
streamlit.title('My parents new healty diner')
stramlit.header('Breakfast menu')
streamlit.text('🥣omega 3 & burbury oatmeal')
streamlit.text('🥗 kale,spinach & rockect smoothie')
stramlit.text('🐔 hard boiled free-range egg')
streamlit.text('🥑🍞 Avocado toast')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocodo','strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())



fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
