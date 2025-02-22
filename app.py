#streamlit
import streamlit as st
st.button("Click me")

st.set_page_config(page_title="growth mindset project", project_icon="★")
st.title("✨Growth Mindset Challenge: Web App With Streamlit")

st.header("Welcome to your Growth Journey!")
st.write("Embrace challenges,learn from miistakes,and unlock your full potential.This Al-powered app helps you build a growth mindset with reflection,challenges, and achievements!")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final,failures is not fatal:it is courage to continue that counts.- winston churchill")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you are facing:")

#condition
if user_input:
    st.success(f"you are facing:{user_input}.keep pushing forward toward towords your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your learning")
reflection=st.text_area("Write your reflections here:")

if reflection:
    st.success(f"Great Insight! Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

#achievements
st.header("celebrate your wins!")
acheivment=st.text_input("Share something you've recently accomplished: ")

if acheivment:
    st.success(f"🙌Amazing! You achieved:{acheivment}")
else:
    st.info("Big or Small , every acheivemen counts! Share one now😍")

    #footer
    st.write("- - -")
    st.write("Keep believing in yourself.Growth is a journey,not a destination!🌟")
    st.write("© Created by Mehak shahbaz ✌")
