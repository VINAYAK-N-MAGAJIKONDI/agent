import streamlit as st
import requests

BASE_URL = "http://localhost:8000"  

st.set_page_config(page_title="Business Dashboard", layout="wide")
st.title("Business Dashboard")


if st.button("Get Total Revenue"):
    response = requests.post(f"{BASE_URL}/dashboard", json={"prompt": "revenue"})
    try:
        st.success(f"Total Revenue: ₹{response.json()['result']}")
    except Exception:
        st.error(f"Error: {response.text}")


if st.button("Get Inactive Clients"):
    response = requests.post(f"{BASE_URL}/dashboard", json={"prompt": "inactive clients"})
    try:
        st.info(f"Inactive Clients: {response.json()['result']}")
    except Exception:
        st.error(f"Error: {response.text}")


if st.button("Top Courses by Enrollment"):
    response = requests.post(f"{BASE_URL}/dashboard", json={"prompt": "top courses by enrollment"})
    try:
        st.info(response.json()['result'])

    except Exception:
        st.error(f"Error: {response.text}")


st.subheader("Check Course Attendance")
course_title = st.text_input("Course Name", "Yoga Beginner")
if st.button("Check Attendance %"):
    response = requests.post(f"{BASE_URL}/dashboard", json={"prompt": f"attendance for {course_title}"})
    try:
        st.write(f"{response.json()['result']}")
    except Exception:
        st.error(f"Error: {response.text}")
