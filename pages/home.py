import streamlit as st
import time

# project title 
st.markdown("""
<h1 style='
text-align: center;
font-size: 60px;
margin-top: 215px;
'>
Decoding Delhi’s Air Quality

</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='
text-align: center;
font-size: 22px;
'>
Exploring Air Pollution (AQI) Patterns and Weather Influence in 2025
</p>
""", unsafe_allow_html=True)


# making the button 
c1,c2,c3=st.columns([1,1,1])
with c2.container():
    btn=st.button("Let's Analyze", width="stretch")
    if btn:
        # st.balloons()
        # time.sleep(1.7)
        st.switch_page("pages/about_project.py")
        
