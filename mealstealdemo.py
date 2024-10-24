import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# 1. Background, containers, styling
# -------------------------

# CSS styles
st.markdown("""
<style>
/* background */
.stApp {
    background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif');
    background-size: cover; 
    background-position: top;
}

/* styling for subheader + other text elements */
.subheader-container {
    border: 2px solid white;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    max-width: 80%;  /* Adjusted for centering */
    margin: 0 auto;
}

.subheader-container img { 
    width: 300px;
}

/* styling for tabs + tab content */
.stTabs [role='tab'] {
    border: 2px solid white;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    max-width: 80px;
    margin: 0 5px;
}

/* Container for main content */
.content-section {
    border: 2px solid white;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    max-width: 80%;  /* Adjusted for centering */
    margin: 20px auto;  /* Centered with margin */
}

/* Cards for meal plan */
.card {
    background-color: #335D3B;
    color: #DAD7CD;
    width: 160px;
    height: 160px;
    margin: 20px;
    cursor: pointer;
    text-align: center;
    padding: 20px;
    border-radius: 10px;
    transition: opacity 0.6s ease, transform 0.3s ease-in-out;
    display: inline-block;
    justify-content: center;
    line-height: 160px;
    position: relative; /* Added for the arrow effect */
}

/* hover effect for meal plan boxes */
.card:hover {
    transform: scale(1.05);
}

/* centering and fade-out effect for non-hovered boxes */
.card:hover > :not(:hover) {
    opacity: 0.4;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #335D3B;
    color: #DAD7CD;
}

.box.details::before {
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
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. Logo, subheader
# -------------------------
st.markdown("""
<div class='text-container'>
    <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo" style="display: block; margin: 0 auto;">
    <div class='subheader-container'>
        <h2>Get Fit, Eat Smart, Spend Less</h2>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# 3. User input form/sidebar
# -------------------------
st.sidebar.header('User Input')

# Sidebar health information
age = st.sidebar.number_input('Age', min_value=10, max_value=90)
gender = st.sidebar.selectbox('Gender Identity', ['Male', 'Female', 'Trans', 'Other'])
weight = st.sidebar.number_input('Weight (kg)', min_value=30, max_value=200)
height = st.sidebar.number_input('Height (cm)', min_value=120, max_value=300)
goal = st.sidebar.selectbox('Health Goal', ['Weight Loss', 'Maintain Weight', 'Muscle Gain', 'Eat Healthier', 'Create Meal Routine'])
dietary_pref = st.sidebar.multiselect('Dietary Preferences', ['Vegetarian', 'Vegan', 'Halal', 'Gluten-Free', 'Dairy-Free', 'Pescetarian', 'None'])
allergies = st.sidebar.text_input('Allergies (comma-separated)', '')
exercise_level = st.sidebar.selectbox('Exercise Level', ['Sedentary', 'Lightly Active', 'Active', 'Very Active'])

st.sidebar.markdown('### Set Meal Plan Duration')
days = st.sidebar.slider('Meal Plan Duration (days)', 1, 7, 7)

# -------------------------
# 4. Tabs
# -------------------------
st.markdown('<div class="content-section">', unsafe_allow_html=True)  # Container for the tabs

tab1, tab2, tab3, tab4 = st.tabs(['Meal Plan', 'Recipes', 'Ingredients', 'Meal Wrap'])

# -------------------------
# 5. Meal Plan Tab & Page
# -------------------------
with tab1:
    st.markdown('<h2 style="text-align: center;">Your Personalized Meal Plan</h2>', unsafe_allow_html=True)

    # Sample meal plan with mock data
    meal_plan = {
        'Day 1': ['Oatmeal with fruit', 'Grilled chicken salad', 'Apple', 'Quinoa with veggies'],
        'Day 2': ['Greek yogurt with honey', 'Turkey sandwich', 'Carrot sticks', 'Salmon with rice'],
        'Day 3': ['Smoothie', 'Pasta with tomato sauce', 'Nuts', 'Stir-fried tofu with broccoli'],
        'Day 4': ['Eggs and toast', 'Chickpea salad', 'Granola bar', 'Beef stir-fry'],
        'Day 5': ['Pancakes', 'Veggie wrap', 'Yogurt', 'Baked chicken with potatoes'],
        'Day 6': ['Cereal with milk', 'Quinoa salad', 'Fruit', 'Fish tacos'],
        'Day 7': ['Toast with avocado', 'Rice and beans', 'Dark chocolate', 'Grilled shrimp with veggies'],
    }

    # Render cards based on slider selection
    day_count = min(days, len(meal_plan))
    cols = st.columns(3)  # Create three columns

    # Placeholder for displaying selected meal
    selected_meal = st.empty() 

    for idx, (day, meals) in enumerate(meal_plan.items()):
        if idx < day_count:  # Only show the selected number of days
            with cols[idx % 3]:  # Distribute the days across columns
                if st.button(day, key=day):  # Make cards clickable
                    selected_meal.markdown(f'### {day} Meal Plan:\n- ' + '\n- '.join(meals))
                st.markdown(f"""
                <div class="card" style="cursor: pointer;" onclick="this.click();">
                    <div class="card-content">
                        <h3>{day}</h3>
                        <p>Click to see meals</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# -------------------------
# 6. Recipes - placeholder
# -------------------------
with tab2:
    st.subheader('Recipes')
    st.write('Fill in later.')

# -------------------------
# 7. Ingredients - placeholder
# -------------------------
with tab3:
    st.subheader('Ingredients')
    st.write('Fill in later - this will also be the basket.')

# -------------------------
# 8. Meal Wrap - placeholder 
# -------------------------
with tab4:
    st.subheader('Meal Wrap - Your Meal Plan Stats')
    st.write('Fill in later.')

# ----
# 9. Close container
# ----
st.markdown('</div>', unsafe_allow_html=True)  # Close the frosted container

# ----
# 10.Footer
# ----
st.markdown("""
    <footer>
        <p style="text-align: center; color: #DAD7CD;">© 2024 Meal Steal. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
