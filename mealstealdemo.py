import streamlit as st
import pandas as pd

# -------------------------
# 1. App Title, Background, and Custom Styling
# -------------------------

st.markdown("""
    <style>
    /* ----
    Background GIF without an opaque overlay
    ---- */
    .stApp {
        background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif');
        background-size: cover;
        background-position: top;
        color: #DAD7CD;
    }

    /* ----
    Styling for title, subheader, and other text elements
    ---- */
    .text-container {
        text-align: center;
        margin: 50px auto;
    }

    .text-container img {
        width: 300px;
    }

    /* ----
    Frosted glass effect for general containers (e.g., subheader, welcome box, tabs, and pages)
    ---- */
    .container {
        border: 2px solid white;
        backdrop-filter: blur(20px);  /* Blur effect */
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        max-width: 80%;
        margin: 0 auto;
        color: #DAD7CD;
    }

    /* ----
    Styling for meal plan day boxes to appear in rows
    ---- */
    .box-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    /* ----
    Individual day boxes with hover effect
    ---- */
    .box {
        background-color: #67944C;  /* Dark green */
        color: white;
        width: 150px;
        height: 150px;
        margin: 20px;
        cursor: pointer;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: opacity 0.6s ease, transform 0.3s ease-in-out;
    }

    .box:hover {
        transform: scale(1.05);  /* Zoom on hover */
    }

    /* ----
    Hover effect to dim non-hovered boxes
    ---- */
    .box-container:hover > :not(:hover) {
        opacity: 0.4;
    }

    /* ----
    Styling for form input elements (dark green background)
    ---- */
    input, select, textarea, .stNumberInput, .stSelectbox, .stMultiselect {
        background-color: #67944C !important;  /* Highlight inputs */
        color: white;
    }

    /* ----
    Slider Handle Color (no carrot image, just dark green)
    ---- */
    .stSlider > div:first-of-type > div:first-of-type {
        background-color: #67944C !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----
# Title Section with logo image
# ----
st.markdown("""
    <div class="text-container">
        <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo">
        <div class="container">
            <h2>Get Fit, Eat Smart, Spend Less</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# ----
# 2. Sidebar User Input Form (with dark green background for input fields)
# ----
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
days = st.sidebar.slider("Meal Plan Duration (days)", 1, 7, 7)  # Slider for setting meal plan duration

# ----
# 3. Main Content - Tabs Wrapped Inside Frosted Container
# ----
# ----
# This is for the container around the tabs and their content
# ----
st.markdown('<div class="container">', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Meal Plan", "Basket", "Meal Wrap"])

# ----
# Meal Plan Tab Content (with dynamic day boxes and horizontal layout)
# ----
with tab1:
    st.markdown("<h2 style='text-align: center;'>Your Personalized Meal Plan</h2>", unsafe_allow_html=True)

    # Sample meal plan (mock data)
    meal_plan = {
        'Day 1': ['Oatmeal with fruit', 'Grilled chicken salad', 'Apple', 'Quinoa with veggies'],
        'Day 2': ['Greek yogurt with honey', 'Turkey sandwich', 'Carrot sticks', 'Salmon with rice'],
        'Day 3': ['Smoothie', 'Pasta with tomato sauce', 'Nuts', 'Stir-fried tofu with broccoli'],
        'Day 4': ['Eggs and toast', 'Chickpea salad', 'Granola bar', 'Beef stir-fry'],
        'Day 5': ['Pancakes', 'Veggie wrap', 'Yogurt', 'Baked chicken with potatoes'],
        'Day 6': ['Cereal with milk', 'Quinoa salad', 'Fruit', 'Fish tacos'],
        'Day 7': ['Toast with avocado', 'Rice and beans', 'Dark chocolate', 'Grilled shrimp with veggies'],
    }

    # ----
    # Dynamic rendering of the day boxes based on slider selection
    # ----
    st.markdown('<div class="box-container">', unsafe_allow_html=True)
    
    # Initialize a variable to capture the clicked day
    selected_day = st.empty()

    day_count = min(days, len(meal_plan))  # Adjust box count based on user slider input

    # Create a button for each day that reveals the meal plan on click
    for i, (day, meals) in enumerate(meal_plan.items()):
        if i < day_count:  # Show only the number of boxes based on slider
            if st.button(day):  # Button click event to show meal plan
                selected_day.markdown(f"### {day} Meal Plan: \n- " + "\n- ".join(meals))
    
    st.markdown('</div>', unsafe_allow_html=True)

# ----
# Basket Tab - Placeholder
# ----
with tab2:
    st.subheader("Grocery Price Optimization")
    st.write("Fill in later.")

# ----
# Meal Wrap Tab - Placeholder
# ----
with tab3:
    st.subheader("Meal Wrap Analysis")
    st.write("Fill in later.")

# ----
# Closing the frosted container for the tabbed content
# ----
st.markdown('</div>', unsafe_allow_html=True)

# ----
# Footer
# ----
st.markdown("""
    <footer>
        <p style="text-align: center;">© 2024 Meal Steal. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
