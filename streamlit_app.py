import streamlit as st
import requests
from datetime import datetime, timedelta

def get_earthquakes_data(start_date, end_date):
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    parameters = {
        "format": "geojson",
        "starttime": start_date,
        "endtime": end_date,
        "minmagnitude": 4.0,  # You can adjust the minimum magnitude as needed
    }
    response = requests.get(base_url, params=parameters)
    return response.json()

def main():
    st.title("Last Month Earthquakes Around the Globe")

    # Calculate start and end dates for the last month
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    earthquakes_data = get_earthquakes_data(start_date.isoformat(), end_date.isoformat())

    if "features" in earthquakes_data.keys():
        st.map(earthquakes_data, zoom=2)
    else:
        st.warning("No earthquake data available for the selected period.")

if __name__ == "__main__":
    main()
