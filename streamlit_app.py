created the main python file
import stream lit 
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
