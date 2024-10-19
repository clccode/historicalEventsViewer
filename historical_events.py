import streamlit as st
import requests

# function to get events
def get_events(month, day):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    events = data["data"]["Events"]
    return events

# set up Streamlit web app
st.set_page_config(
    page_title="Historical Events"
)

st.title("Historical Events Viewer")
st.write("Enter a date to get historical events: ")
month = st.number_input("Enter the month (1-12):", min_value=1, max_value=12, step=1)
day = st.number_input("Enter the day (1-31:", min_value=1, max_value=31, step=1)

if st.button("Show Events"):
    events = get_events(month, day)
    if events:
        st.subheader(f"Historical events on {month}/{day}:")
        for event in events:
            st.write(f"Year: {event['year']}")
            st.write(f"Description: {event["text"]}")
            st.write(f"Link: {event['links'][0]['link']}")
            st.divider()
