import streamlit
import pandas
import requests
import snowflake.connector


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.title('My parents New Healthy Dinner')
streamlit.header('Breakfast Favorities')
streamlit.text('🥣 Omega 3 & Blueberry Oat Meal')
streamlit.text('🥗 Kale,spainch Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('  🥑 🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.
streamlit.dataframe(fruit_show)

streamlit.title('Fruityvyce fruity advice')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# fryity advice
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# showing
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

#streamlit.write('Thanks for adding fruit', 'add my fruit')

my_cur = my_cnx.cursor()
my_cur.execute(" select * from fruit_load_list")

#this is will not work correctly 

#my_cur.execute(" insert into fruit_load_list values('from streamlit)")

my_data_rows= my_cur.fetchall()

#my_cur.execute("inert into fruit_load_list values ('from streamlit')")
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)
fruit_choice1 = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('Thanks for adding Jackfruit ', fruit_choice1)








