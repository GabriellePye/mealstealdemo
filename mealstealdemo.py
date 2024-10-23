import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. App Title and Description with Custom Background and Styling
# -------------------------

st.markdown("""
    <style>
    /* Page Background with gradient and image */
    .stApp {
        background: linear-gradient(
            rgba(103, 148, 76, 0.8), rgba(103, 148, 76, 0.8)
        ), url('https://i.ibb.co/82HxvBk/meal-steal-bg-2.jpg');
        background-size: cover;
        background-position: top;
        color: #DAD7CD; /* Light text */
    }

    /* Custom styling for the title and subheader */
    .text-container {
        text-align: center;
        margin: 50px auto;
    }

    .text-container img {
        width: 300px;
    }

    .subheader-container {
        background-color: rgba(51, 93, 59, 0.8);  /* 335D3B color with 80% opacity */
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        max-width: 80%;
        margin: 0 auto;  /* Center the box */
        color: #DAD7CD;
    }

    /* Styling for the rest of the page (section below the title) */
    .content-section {
        background-color: #67944C; /* Main body background */
        padding: 30px;
        border-radius: 20px;
    }

    /* Styling for tabs and cards */
    .stTabs [role="tab"] {
        background-color: rgba(51, 93, 59, 0.8);  /* Dark green with 80% opacity */
        color: #DAD7CD;  /* Light text */
    }

    .stTabs [role="tabpanel"] {
        background-color: rgba(51, 93, 59, 0.8);  /* Dark green with 80% opacity */
        color: #DAD7CD;  /* Light text */
    }

    .container {
        width: 100%;
        max-width: 1000px;
        display: flex;
        gap: 20px;
        justify-content: center;
        margin: 20px auto; /* Center the container */
        flex-wrap: wrap;
    }

    /* Card styling */
    .card {
        width: 200px;
        height: 300px;
        border-radius: 20px;
        overflow: hidden;
        display: flex;
        align-items: flex-end;
        position: relative;
        transition: transform 0.5s ease-in-out;
        background-color: #67944C;
        cursor: pointer;
    }

    /* Card content */
    .card-content {
        color: #DAD7CD; /* Text color */
        padding: 10px;
        text-align: center;
    }

    /* Profile image styling */
    .profile-image > img {
        width: 100%;
        height: 150px; /* Fixed height for images */
        object-fit: cover;
    }

    /* Card hover effect */
    .card:hover {
        transform: scale(1.05); /* Slight zoom on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Title section with image
st.markdown("""
    <div class="text-container">
        <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo">
        <div class="subheader-container">
            <h2>Get Fit, Eat Smart, Spend Less</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# Main content section
st.markdown('<div class="content-section">', unsafe_allow_html=True)

# App description
st.markdown("""
    Welcome to Meal Steal! This app helps you create personalized meal plans tailored to your dietary needs and health goals while finding the best grocery deals.
""")

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
# 3. Main Content - Tabs
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

    # Get the current day index (Day 1 = 0)
    current_day_index = 3  # Adjust this for the actual current day

    # Display meals for yesterday, today, and tomorrow
    for offset in range(-1, 2):  # -1 for yesterday, 0 for today, +1 for tomorrow
        day_index = current_day_index + offset
        day_index = max(0, min(day_index, len(meal_plan) - 1))  # Ensure valid index

        # Create container for meal cards
        st.markdown('<div class="container">', unsafe_allow_html=True)

        # Display each meal as a card
        for meal in meals:
            meal_index = meals.index(meal)
            st.markdown(f"""
                <div class="card">
                    <div class="profile-image">
                        <img src="https://via.placeholder.com/200x150.png" alt="{meal}">
                    </div>
                    <div class="card-content">
                        <h2>{meal}</h2>
                        <p>{meal_plan[f'Day {day_index + 1}'][meal_index]}</p>
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

    df_grocery = pd.DataFrame(grocery_data)
    st.dataframe(df_grocery)

# Meal Wrap Tab
with tab3:
    st.subheader("Meal Plan Nutrition Stats")

    # Mockup data for calorie breakdown
    calories = np.random.randint(300, 800, size=(7, 4))  # for 7 days and 4 meals
    meals_labels = ['Breakfast', 'Lunch', 'Snack', 'Dinner']

    fig, ax = plt.subplots()
    ax.bar(meals_labels, calories.sum(axis=0), color=['green', 'blue', 'orange', 'red'])
    ax.set_ylabel('Total Calories')
    ax.set_title('Total Calories per Meal Over 7 Days')

    st.pyplot(fig)

# -------------------------
# 4. Download Options (CSV)
# -------------------------
st.header("Download Your Meal Plan & Grocery List")

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df_grocery)

st.download_button(
    label="Download Grocery List as CSV",
    data=csv,
    file_name='grocery_list.csv',
    mime='text/csv',
)

st.markdown('</div>', unsafe_allow_html=True)  # Close content section div
