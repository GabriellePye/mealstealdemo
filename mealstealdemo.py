import streamlit as st
import pandas as pd

# -------------------------
# 1. App Background, Containers, and Styling
# -------------------------

# Applying custom CSS for styling
st.markdown("""
    <style> 
    .stApp {
        background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif');
        background-size: cover; 
        background-position: top;
    }

    /* Styling for title, subheader, and other text elements */
    .text-container {
        text-align: center;
        margin: 50px auto;
    }

    .text-container img { 
        width: 300px;
    }

    /* Frosted glass effect for containers */
    .container {
        border: 2px solid white;
        backdrop-filter: blur(20px);
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        max-width: 80%;
        margin: 0 auto;
    }

    /* Boxes for meal plan days */
    .box {
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
        line-height: 160px;
    }

    /* Hover effect for meal plan boxes */
    .box:hover {
        transform: scale(1.05);
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #335D3B;
        color: #DAD7CD;
    }

    /* Slider handle color */
    .stSlider > div:first-of-type > div:first-of-type {
        background-color: #67944C !important;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# 2. Logo and Subheader
# -------------------------

st.markdown("""
    <div class='text-container'>
        <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo">
        <div class='container'>
            <h2>Get Fit, Eat Smart, Spend Less</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# -------------------------
# 3. User Input Form (Sidebar)
# -------------------------

st.sidebar.header('User Input')

# User health information inputs
age = st.sidebar.number_input('Age', min_value=10, max_value=90)
gender = st.sidebar.selectbox('Gender Identity', ['Male', 'Female', 'Trans', 'Other'])
weight = st.sidebar.number_input('Weight (kg)', min_value=30, max_value=200)
height = st.sidebar.number_input('Height (cm)', min_value=120, max_value=300)
goal = st.sidebar.selectbox('Health Goal', ['Weight Loss', 'Maintain Weight', 'Muscle Gain', 'Eat Healthier', 'Create Meal Routine'])
dietary_pref = st.sidebar.multiselect('Dietary Preferences', ['Vegetarian', 'Vegan', 'Halal', 'Gluten-Free', 'Dairy-Free', 'Pescetarian', 'None'])
allergies = st.sidebar.text_input('Allergies (comma-separated)', '')
exercise_level = st.sidebar.selectbox('Exercise Level', ['Sedentary', 'Lightly Active', 'Active', 'Very Active'])

# Meal Plan Duration Slider
st.sidebar.markdown('### Set Meal Plan Duration')
days = st.sidebar.slider('Meal Plan Duration (days)', 1, 7, 7)

# -------------------------
# 4. Tabs Section
# -------------------------

# Container for the tabs and their content
st.markdown('<div class="container">', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(['Meal Plan', 'Recipes', 'Ingredients', 'Meal Wrap'])

# -------------------------
# 5. Meal Plan Tab
# -------------------------

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

    # Dynamic rendering of meal plan boxes based on slider selection
    day_count = min(days, len(meal_plan))  # Adjust box count based on user slider input
    cols = st.columns(3)  # Create a 3-column layout for meal plan boxes

    selected_day = st.empty()  # Placeholder for selected day’s meal details

    for idx, day in enumerate(list(meal_plan.keys())[:day_count]):
        with cols[idx % 3]:  # Place in the right column
            if st.button(day):
                # Display meal plan for selected day
                selected_day.markdown(f"### {day} Meal Plan:\n- " + "\n- ".join(meal_plan[day]))

# -------------------------
# 6. Recipes Tab (Placeholder)
# -------------------------

with tab2:
    st.subheader('Recipes')
    st.write('Recipes will be filled in later.')

# -------------------------
# 7. Ingredients Tab (Placeholder)
# -------------------------

with tab3:
    st.subheader('Ingredients')
    st.write('This will also include the grocery basket.')

# -------------------------
# 8. Meal Wrap Tab (Placeholder)
# -------------------------

with tab4:
    st.subheader('Meal Wrap - Your Meal Plan Stats')
    st.write('Visualize and analyze your meal plan stats here.')

# -------------------------
# 9. Close Container for Tabs Section
# -------------------------

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# 10. Footer
# -------------------------

st.markdown("""
    <footer>
        <p style="text-align: center;">© 2024 Meal Steal. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
