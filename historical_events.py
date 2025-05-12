import streamlit as st
import requests

# function to get events
def get_events(month, day):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    events = data["data"]["Events"]
    return events

# function to get the date (i.e, June 1)
def get_date(month, day):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    mon_day = data["date"]
    return mon_day

# set up Streamlit web app
st.set_page_config(
    page_title="Historical Events",
    page_icon="📖"
)

# set up the page title and the user input
st.title("Historical Events")
st.write("Enter a date to get historical events on that day: ")
month = st.number_input("Enter the month (1-12):", min_value=1, max_value=12, step=1)
day = st.number_input("Enter the day (1-31:", min_value=1, max_value=31, step=1)

# conditional for once the user selects a date
if st.button("Show Events"):
    events = get_events(month, day)
    date = get_date(month, day)

    if events:
        st.subheader(f"Historical events on {date}:")
        for event in events:
            st.write(f"Year: {event['year']}")
            st.write(f"Description: {event["text"]}")
            st.write(f"Link: {event['links'][0]['link']}")
            st.divider()
