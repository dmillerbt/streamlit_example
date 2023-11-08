import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":hundred_points:",layout="wide")

with st.container():
  st.subheader("Hi, I am Danny Miller")
  st.title("A Data Scientist in Chicago")
  st.write("I am looking to learn more about web development")
  st.write("[Learn More ->] (https://github.com/dmillerbt/)")

with st.container():
  st.write("---")
  st.header("Who am I>")
  st.write("##")
  st.write("I work at Baker Tilly as a consultant")
