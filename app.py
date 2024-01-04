from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Tour Itenerary generator")
st.header("Your Trip Advisor")
input_place = st.text_input("Enter your destination: ",key="destination_ input")
input_native = st.text_input("Enter your starting place: ",key="starting_place_input")
input_date = st.selectbox("No of days", list(range(1, 16)), index=0)
input_transport_type = st.selectbox("Mode of Transportation", ["Own Car", "Taxi" ,"Train", "Flight", "Ship"])
input_day = str(input_date)
input_trip_type = st.selectbox("Trip Type", ["Solo trip", "Couple", "Friends", "Colleague"])
input_expense = st.selectbox("Expense Scale", ["Low budget", "Medium Budget", "High budget"])
input_food = st.selectbox("Food Preference", ["Veg only", "NonVeg only", "both Veg/NonVeg"])
from_date = st.date_input("From Date")
to_date = st.date_input("To Date")
from_date_str = str(from_date)
to_date_str = str(to_date)


input_final = "i need ",input_day," days itinerary for ", input_place ," trip, it should include the list of places to stay for all ", input_day ," days in single place at beginning along with rating of that places and facilities given by them. if the visiting place is outside india, please add the travelling city's local currency and compare with indian rupees based on forex values on the top. else, the city is inside india, please skip the currency concept and skip to next part. Next, add the travelling expense for ", input_transport_type ," detailly with type of ticket, fare of ticket from ", input_native ," to ", input_place ," For the fare details use google. Also try to add the cost to stay from ", from_date_str ," to ", to_date_str ," from google. The budget or cost included should be in the tour place local currency. The hotel recommending by you should be in ", input_expense ," So that the website looks more interesting. And make sure that i need single list of places to stay for the days and i will not change my stay hotel for each day. For rating details, use google maps and i need genuine review not fake ones. Below that i need the weather forecasting detail for each day, then give me the places for the ", input_day ," days, especially for ", input_trip_type ," that should have 3 columns, first column should have place name, 2nd column should be description of that place or any historical information if available. 3rd column should have the number of durations do we need to explore that place. Try to give me atleast 3 to 4 places per day and i wont spend more than 1.5 hours in any place. Also add the list of ", input_food ," restaurants for lunch and dinner for each day at the required timing including famous dishes to try over in ", input_expense ," over there and make this as the most memorable trip of my life. Also try to provide the contents in tabular form for beter view."
submit = st.button("Submit")
header = f"Your {input_day} days itinerary for {input_place} is ready.!"
if submit:
    response = get_gemini_response(input_final)
    st.subheader(header)
    st.write(response)

st.markdown("---")
st.markdown("Implemented LLM technique using Google Gemini Pro. Thank you, Google!")