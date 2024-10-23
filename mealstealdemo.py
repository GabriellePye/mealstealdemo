import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. App Title, Background GIF, and Custom Styling
# -------------------------

st.markdown("""
    <style>
    /* Page Background with GIF */
    .stApp {
        background: linear-gradient(
            rgba(103, 148, 76, 0.8), rgba(103, 148, 76, 0.8)
        ), url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif'); /* Background GIF */
        background-size: cover;
        background-position: top;
        color: #DAD7CD; /* Light text */
    }

    /* Styling for the title and subheader */
    .text-container {
        text-align: center;
        margin: 50px auto;
    }

    .text-container img {
        width: 300px;
    }

    .subheader-container {
        background-color: rgba(51, 93, 59, 0.8);  /* Opaque box behind subheader */
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
    .container {
        border: 2px solid #335D3B;
        backdrop-filter: blur(20px);
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        padding: 10px;
    }

    .card {
        width: 200px;
        height: 300px;
        border-radius: 20px;
        position: relative;
        background-color: #ffffffcc;
        cursor: pointer;
        transition: transform 0.5s ease-in-out;
    }

    .card:hover {
        transform: scale(1.05); /* Hover effect: zoom */
    }

    .profile-image img {
        width: 100%;
        height: 150px;
        object-fit: cover;
    }

    /* User input sidebar styling */
    .stSidebar {
        background-color: #335D3B;
        color: #DAD7CD;
    }

    .stNumberInput, .stTextInput, .stSelectbox, .stMultiselect {
        background-color: rgba(103, 148, 76, 0.8); /* Background blur effect */
        color: #DAD7CD;
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
    }

    button:hover {
        background-color: #6fc5ff;
        box-shadow: 0 0 20px #6fc5ff50;
        transform: scale(1.1);
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
            <h2>Get Fit, Eat Smart, Spend Less</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# Opaque box for welcome message
st.markdown('<div class="welcome-box">', unsafe_allow_html=True)
st.markdown("""
    Welcome to Meal Steal! This app helps you create personalized meal plans tailored to your dietary needs and health goals while finding the best grocery deals.
""")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# 2. Sidebar User Input Form
# -------------------------
st.sidebar.header("User Input")

# User Health Information
age = st.sidebar.number_input("Age", min_value=1, max_value=100)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200)
height = st.sidebar.number_input("Height (cm)", min_value=120, max_value=250)
goal = st.sidebar.selectbox("Health Goal", ["Weight Loss", "Maintain Weight", "Muscle Gain"])
dietary_pref = st.sidebar.multiselect("Dietary Preferences", ["Vegetarian", "Vegan", "Gluten-Free", "None"])
allergies = st.sidebar.text_input("Allergies (comma-separated)", "")
exercise_level = st.sidebar.selectbox("Exercise Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])

st.sidebar.markdown("### Set Meal Plan Duration")
days = st.sidebar.slider("Meal Plan Duration (days)", 1, 7, 7)

# -------------------------
# 3. Main Content - Tabs with Curved Style
# -------------------------
tab1, tab2, tab3 = st.tabs(["Meal Plan", "Basket", "Meal Wrap"])

# Meal Plan Tab
with tab1:
    st.subheader("Your Personalized Meal Plan")

    # Sample meal plan (mock data)
    meals = ['Breakfast', 'Lunch', 'Snack', 'Dinner']
    meal_plan = {
        'Day 1': ['Oatmeal with fruit', 'Grilled chicken salad', 'Apple', 'Quinoa with veggies'],
        'Day 2': ['Greek yogurt with honey', 'Turkey sandwich', 'Carrot sticks', 'Salmon with rice'],
        'Day 3': ['Smoothie', 'Pasta with tomato sauce', 'Nuts', 'Stir-fried tofu with broccoli'],
        'Day 4': ['Eggs and toast', 'Chickpea salad', 'Granola bar', 'Beef stir-fry'],
        'Day 5': ['Pancakes', 'Veggie wrap', 'Yogurt', 'Baked chicken with potatoes'],
        'Day 6': ['Cereal with milk', 'Quinoa salad', 'Fruit', 'Fish tacos'],
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

    grocery_df = pd.DataFrame(grocery_data)

    st.write(grocery_df)

# Meal Wrap Tab
with tab3:
    st.subheader("Meal Wrap Analysis")
    st.write("This section will provide a summary of your meals, nutrition breakdown, and wrap-up suggestions.")

# Footer
st.markdown("""
    <footer>
        <p style="text-align: center;">© 2024 Meal Steal. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)

