import streamlit as st
st.set_page_config(page_title='dogs')
st.header("Types of dogs")

col1,col2=st.columns(2)
with col1:
     st.subheader("Pomeranian")
     st.image("./pomeranian.jpg",caption="Pomeranian",width=300,use_column_width=True)
     st.write("Pomeranian are cute")
with col2:
      st.subheader("GoldenRetriever")
      st.image("./GoldenRetriever.jpg",caption="GoldenRetriever",width=300,use_column_width=True)
      st.write("GoldenRetriever  are cute")
