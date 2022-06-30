import streamlit
streamlit.title('My Parents New Healthy Dinner')
import streamlit
streamlit.header('Breakfast Menu')
import streamlit
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
import streamlit
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
import streamlit
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
import streamlit
streamlit.text('🥑🍞 Avocado Toast')
import streamlit
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
