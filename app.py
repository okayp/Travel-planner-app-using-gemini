import google.generativeai as genai
import os
import streamlit as st
api_key=os.environ['GOOGLE_CLOUD_API_KEY']
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom,#007BFF, #000000);
        font-family: 'Arial', sans-serif;
    }
    .content-box {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            
    </style>
    """, unsafe_allow_html=True)

# Streamlit app title and description
st.title("**TripTrek : Gemini-Driven Travel Exploration**")

st.markdown("""
**TripTrek** revolutionizes travel planning with AI. Tailored itineraries combine advanced algorithms and rich travel data, offering personalized recommendations for accommodations, activities, dining, and more. Say goodbye to manual research—enjoy a seamless, stress-free planning experience
""")

st.markdown("""
### **Your family's Travel Compnanion**

**TripTrek** assists families in planning vacations by using destination and duration inputs to create detailed itineraries. It recommends family-friendly attractions, dining options catering to diverse needs, and provides a day-by-day schedule with timings for attractions, meal breaks, and leisure activities, ensuring a balanced and enjoyable trip for everyone.
""")

st.markdown("""
### **At your service on your Business Trips**

**TripTrek** optimizes business travel by creating detailed itineraries based on destination and duration. It suggests conference centers, meeting venues, and local attractions for relaxation. With curated suggestions for business-friendly dining, professionals receive a day-by-day schedule including meeting times, locations, and meal breaks, ensuring efficient use of time and sustained productivity throughout their trip.
""")

st.markdown("""
### **Best friend to the students**

**TripTrek** aids in planning educational trips for students based on destination and duration inputs. It recommends educational sites, museums, universities, and science centers aligned with trip objectives. Additionally, it suggests student-friendly dining options, including affordable restaurants and food courts. The output includes a day-by-day itinerary with visit timings, meal breaks at recommended venues, and leisure activities, ensuring a well-rounded and engaging educational experience for students.
""")

# User inputs
place = st.text_input("Where do you wanna go ?")
days = st.number_input("How long is your trip ? (in days)", min_value=1)
prompt_family=f"""
You are a travel expert. Give me an itenary for {place}, for {days} days. Plan a trip for a family vacation recommending key tourist spots. Account for each day.
The output is a day-by-day itinerary that includes timings for visits to attractions, meal breaks at recommended food places, and suggested activities for relaxation and entertainment, ensuring a balanced and enjoyable trip for all family members.
"""
prompt_business=f"""
You are a travel expert. Give me an itenary for {place}, for {days} days. Plan a business trip recommending key business venues such as conference centers and meeting locations, along with local attractions for downtime.
Additionally, provide suggestions for nearby restaurants and cafes suitable for business lunches and dinners.
The output is a detailed day-by-day schedule that includes meeting times, locations, and meal breaks at recommended food places, helping professionals maximize their time and maintain productivity during their trip.
"""
prompt_education=f"""
You are a travel expert. Give me an itenary for {place}, for {days} days. Plan an educational trip for stduents recommeding ducational and historical sites, museums, universities, and science centers that align with the trip's educational goals.
Additionally, provide recommendations for student-friendly dining options, including affordable restaurants and food courts.
The output is a day-by-day itinerary that includes timings for visits to educational sites, meal breaks at recommended food places, and leisure activities, ensuring a balanced and engaging trip for students.
"""

# Scenario selection
scenario = st.radio(
    "Select a scenario",
    ('Family Vacation', 'Business Travel Planning for Professionals', 'Educational Trip for Students')
)
response=""

if st.button("Generate Itinerary"):
    if scenario == 'Family Vacation':
        response = model.generate_content(prompt_family)
    elif scenario == 'Business Travel Planning for Professionals':
        response = model.generate_content(prompt_business)
    elif scenario == 'Educational Trip for Students':
        response = model.generate_content(prompt_education)

    st.write(response.text)

st.markdown("""
### **Wanna plan your travel ?**
            
Check below for details :"""
)

placeo = st.text_input("Enter the place of origin")
prompt_travel = f"""Give details for travel from {placeo} to {place} through train,bus and flight (based on availability),provide their timings and other details"""
if st.button("Plan Travel"):
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGU2emx2cncybHVxMTFvdHBsNDRnOWJzdDR4dHY0a2pxZno3OXFuayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT1R9Wi1RULmbAUk2k/giphy.webp",
    width = 400
    )
    response = model.generate_content(prompt_travel)
    st.write(response.text)

st.markdown("""
### **Wanna check for accommodation ?**
            
Enter the following details :"""
)
price_from = st.number_input("Lower bound of your price range",min_value=1000)
price_to = st.number_input("Upper bound of your price range",max_value=100000)
prompt_travel = f"""Give details of hotels for accommodation in {place} in the price range {price_from} to {price_to} per night"""
if st.button("Check Accommodation"):
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTRjdGo0anM3bnhwcGJxNHBtd3c2eHlqbzlzbTlsM3AyYWU1NDJweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NDEVHw57wMU5a/giphy.webp",
    width = 400
    )
    response = model.generate_content(prompt_travel)
    st.write(response.text)
    
