import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. App Title, Background GIF, and Custom Styling
# 1. App Title, Background, and Custom Styling
# -------------------------

st.markdown("""
    <style>
    /* Page Background with GIF */
    /* Page Background with GIF - removed opaque layer */
    .stApp {
        background: linear-gradient(
            rgba(103, 148, 76, 0.8), rgba(103, 148, 76, 0.8)
        ), url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif'); /* Background GIF */
        background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif');
        background-size: cover;
        background-position: top;
        color: #DAD7CD; /* Light text */

        width: 300px;
    }
    .subheader-container {
        background-color: rgba(51, 93, 59, 0.8);  /* Opaque box behind subheader */
    /* Applying new container styling for subheader and welcome box */
    .container {
        border: 2px solid white;
        backdrop-filter: blur(20px);  /* Blur effect */
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        max-width: 80%;
        margin: 0 auto;
        color: #DAD7CD;
        display: inline-block; /* To ensure text fits within the box */
    }
    /* Box behind 'Welcome to Meal Steal' text */
    .welcome-box {
        background-color: rgba(103, 148, 76, 0.8);  /* Opaque background */
        padding: 20px;
        border-radius: 15px;
        max-width: 90%;
        margin: 0 auto;
        text-align: center;
    }
    /* Curved edges and solid background for the tabs and cards */
    .stTabs [role="tab"] {
        background-color: #335D3B;
        color: #DAD7CD;
        border-radius: 20px;
        padding: 12px;
        font-weight: bold;
        text-align: center;
    }
    .stTabs [role="tabpanel"] {
        background-color: #335D3B; /* Dark green background */
        color: #DAD7CD;  /* Light text */
        border-radius: 20px;
        padding: 20px;
    }
    /* New box style: borders and backdrop blur */
    /* Box hover effect for meal plan day boxes */
    .container {
        border: 2px solid #335D3B;
        backdrop-filter: blur(20px);
        display: flex;
        justify-content: space-evenly;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        padding: 10px;
    }
    .card {
    .box {
        width: 200px;
        height: 300px;
        border-radius: 20px;
        position: relative;
        height: 200px;
        margin: 20px;
        background-color: #ffffffcc;
        cursor: pointer;
        transition: transform 0.5s ease-in-out;
    }
    .card:hover {
        transform: scale(1.05); /* Hover effect: zoom */
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        transition: opacity 0.6s ease;
    }
    .profile-image img {
        width: 100%;
        height: 150px;
        object-fit: cover;
    .box:hover {
        transform: scale(1.05);  /* Zoom on hover */
        transition: transform 0.3s ease-in-out;
    }
    /* User input sidebar styling */
    .stSidebar {
        background-color: #335D3B;
        color: #DAD7CD;
    /* Apply hover effect for other boxes */
    .container:hover > :not(:hover) {
        opacity: 0.4;
    }
    .stNumberInput, .stTextInput, .stSelectbox, .stMultiselect {
        background-color: rgba(103, 148, 76, 0.8); /* Background blur effect */
        color: #DAD7CD;
    /* Meal day box arrow effect */
    .card .details::before {
        content: '';
        position: absolute;
        left: 0px;
        width: 0;
        height: 0;
        border-top: 10px solid transparent;
        border-bottom: 10px solid transparent;
        border-left: 10px solid #fff;
        z-index: 1;
    }
    /* Tab navigation button custom style */
    button {
        padding: 12.5px 30px;
        border: 0;
        border-radius: 100px;
        background-color: #2ba8fb;
        color: #ffffff;
        font-weight: Bold;
        transition: all 0.5s;
    /* Form input styling */
    input, select, textarea, .stNumberInput, .stSelectbox, .stMultiselect {
        background-color: #67944C !important;  /* Highlight inputs */
        color: white;
    }
    button:hover {
        background-color: #6fc5ff;
        box-shadow: 0 0 20px #6fc5ff50;
        transform: scale(1.1);
    /* Custom Toggle Switch (dark green) */
    .stToggle > div:first-of-type {
        background-color: #335D3B !important;
    }
    button:active {
        background-color: #3d94cf;
        transition: all 0.25s;
        box-shadow: none;
        transform: scale(0.98);
    }
    </style>
""", unsafe_allow_html=True)

# Title Section with image
st.markdown("""
    <div class="text-container">
        <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo">
        <div class="subheader-container">
        <div class="container">
            <h2>Get Fit, Eat Smart, Spend Less</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# Opaque box for welcome message
st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
# Welcome Box
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown("""
    Welcome to Meal Steal! This app helps you create personalized meal plans tailored to your dietary needs and health goals while finding the best grocery deals.
""")


# Meal Plan Tab
with tab1:
    st.subheader("Your Personalized Meal Plan")
    st.markdown("<h2 style='text-align: center;'>Your Personalized Meal Plan</h2>", unsafe_allow_html=True)

    # Sample meal plan (mock data)
    meals = ['Breakfast', 'Lunch', 'Snack', 'Dinner']

        'Day 7': ['Toast with avocado', 'Rice and beans', 'Dark chocolate', 'Grilled shrimp with veggies'],
    }

    # Meal Plan Day Boxes (horizontal or grid layout)
    for day, meals in meal_plan.items():
        st.markdown(f"<h3>{day}</h3>", unsafe_allow_html=True)
        st.markdown('<div class="container">', unsafe_allow_html=True)
        # Display each meal as a card
        for meal in meals:
            st.markdown(f"""
                <div class="card">
                    <div class="profile-image">
                        <img src="https://via.placeholder.com/200x150.png" alt="{meal}">
                    </div>
                    <div class="card-content">
                        <h2>{meal}</h2>
                        <p>{meal}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
# Basket Tab
    # Display meal plan days in a horizontal layout with clickable boxes
    st.markdown('<div class="container">', unsafe_allow_html=True)
    for day in meal_plan:
        st.markdown(f"""
            <div class="box">
                <h3>{day}</h3>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
# Basket Tab - Placeholder
with tab2:
    st.subheader("Grocery Price Optimization")
    st.write("Fetching the best deals across major UK supermarkets...")
    # Mockup data for grocery prices
    grocery_data = {
        "Item": ["Oatmeal", "Fruit", "Chicken", "Salad", "Apple", "Quinoa", 
                 "Greek Yogurt", "Turkey", "Carrot", "Nuts", "Tofu", "Broccoli", 
                 "Eggs", "Chickpeas", "Granola", "Beef", "Pancakes", "Veggies", 
                 "Rice", "Fish", "Avocado"],
        "Price (Aldi)": np.random.uniform(1, 5, 20),
        "Price (Tesco)": np.random.uniform(1, 5, 20),
        "Price (Sainsbury's)": np.random.uniform(1, 5, 20),
        "Price (Waitrose)": np.random.uniform(1, 5, 20),
    }
    st.write("Fill in later.")

    grocery_df = pd.DataFrame(grocery_data)
    st.write(grocery_df)
# Meal Wrap Tab
# Meal Wrap Tab - Placeholder
with tab3:
    st.subheader("Meal Wrap Analysis")
    st.write("This section will provide a summary of your meals, nutrition breakdown, and wrap-up suggestions.")
    st.write("Fill in later.")

# Footer
st.markdown("""
    <footer>
        <p style="text-align: center;">© 2024 Meal Steal. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
