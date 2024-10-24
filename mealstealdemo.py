import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# 1. Background, containers, styling
# -------------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif');
    background-size: cover; 
    background-position: top;
}

/* Styling for subheader + other text elements */
.subheader-container {
    text-align: center;
    margin: 50px auto;
}

.subheader-container img { 
    width: 300px;
}

/* Frosted effect for containers */
.frosted-container {
    border: 2px solid white;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    max-width: 80%;
    margin: 0 auto;  /* Center the container */
}

/* Styling for tabs + tab content */
.stTabs [role='tab'] {
    border: 2px solid white;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin: 0 5px;
}

/* Container for main content */
.content-section {
    border: 2px solid white;
    backdrop-filter: blur(20px);
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 10px;
    margin: 20px auto;  /* Center the container */
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
}

.card-content { 
    color: #DAD7CD;
    padding: 10px;
    text-align: center;
}

/* Hover effect for meal plan boxes */
.card:hover {
    transform: scale(1.05);
}

/* Centering and fade-out effect for non-hovered boxes */
.card:hover > :not(:hover) {
    opacity: 0.4;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 2. Logo, subheader
# -------------------------
st.markdown("""
<div class='text-container'>
    <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo">
    <div class='subheader-container'>
        <h2>Get Fit, Eat Smart, Spend Less</h2>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# 3. User input form/sidebar
# -------------------------
st.sidebar.header('User Input')

# Health information
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
# The slider will dictate how many boxes i.e., meal plans appear.

# -------------------------
# 4. Tabs
# -------------------------
st.markdown('<div class="frosted-container">', unsafe_allow_html=True)
# The tabs will be contained within the frosted container

tab1, tab2, tab3, tab4 = st.tabs(['Meal Plan', 'Recipes', 'Ingredients', 'Meal Wrap'])

# -------------------------
# 5. Meal Plan Tab & Page
# -------------------------
with tab1:
    st.markdown('<h2 style="text-align: center;">Your Personalised Meal Plan</h2>', unsafe_allow_html=True)

    # Sample meal plan with mock data
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

    # Rendering of cards based on slider selection
    st.markdown('<div class="content-section">', unsafe_allow_html=True)

    # Display correct number of cards based on slider
    day_count = min(days, len(meal_plan))
    cols = st.columns(day_count)

    for idx, day in enumerate(meal_plan):
        if idx < days:  # Only display the cards based on selected days
            with cols[idx % day_count]:
                st.markdown(f"""
                <div class="card" onclick="alert('{day} Meal Plan: \\n- {'\\n- '.join(meal_plan[day])}')">
                    <div class="card-content">
                        <h3>{day}</h3>
                        <p>Click for meals</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

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
# 9. Close frosted container
# ----
st.markdown('</div>', unsafe_allow_html=True)

# ----
# 10. Footer
# ----
st.markdown("""
<footer>
    <p style="text-align: center; color: #DAD7CD;">© 2024 Meal Steal. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)
