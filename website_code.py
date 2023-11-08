import streamlit as st
import streamlit_lottie as stl
import requests

def load_lottie(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

st.set_page_config(page_title="My Webpage", page_icon=":hundred_points:",layout="wide")

#Website Header
with st.container():
  st.subheader("Hi, I am Danny Miller")
  st.title("A Data Scientist in Chicago")
  st.write("I am looking to learn more about web development")
  st.write("[Learn More ->] (https://github.com/dmillerbt/)")

#Who Am I?
with st.container():
  left_column, right_column = st.columns(2)
  st.write("---")
  st.header("Who am I>")
  st.write("##")
  st.write("I work at Baker Tilly as a consultant")

#Lottie file
lottie_animation = load_lottie("https://lottie.host/e338d336-1460-44d6-8cd1-cee4ebf70337/SUJkYtg7kK.json")
with right_column:
  stl(lottie_animation, height = 250, key = "data_viz")

