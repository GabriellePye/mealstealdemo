# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# -------------------------
# 1. App Title and Description
# -------------------------
import streamlit as st

# Title and Subheader
st.markdown("""
    <style>
    /* Import Sergio Trendy font from Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Sergio+Trendy&display=swap');
    
    /* Custom styling for the title */
    .title {
        font-family: 'Sergio Trendy', sans-serif;
        color: #DAD7CD;  /* Light color for title */
        font-size: 64px;
        text-align: center;
        margin-top: 0;
    }

    /* Custom styling for the subheader */
    .subheader {
        font-family: 'Sergio Trendy', sans-serif;
        color: #DAD7CD;  /* Light color for subheader */
        font-size: 32px;
        text-align: center;
        margin-top: -20px;
    }

    /* Background image setup, tiled across the app */
    .stApp {
        background-image: url('https://i.ibb.co/TWyRv88/Meal-Steal-Logo-1.png');
        background-size: 200px 200px; /* Size of each tile */
        background-repeat: repeat;  /* Tiling the image */
        background-position: center; /* Center the image */
    }
    </style>
    
    <h1 class="title">Meal Steal</h1>
    <h2 class="subheader">Get Fit, Eat Smart, Spend Less</h2>
    """, 
    unsafe_allow_html=True
)

# App description (you can add more functionality here as needed)
st.markdown("""
    Welcome to Meal Steal! This app helps you create personalized meal plans tailored to your dietary needs and health goals while finding the best grocery deals.
""")

# -------------------------
# 2. User Input Section
# -------------------------
st.sidebar.header("User Input")

# -------------------------
# 2. User Input Section
# -------------------------
st.sidebar.header("User Input")


# User Health Information
age = st.sidebar.number_input("Age", min_value=1, max_value=100)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200)
height = st.sidebar.number_input("Height (cm)", min_value=120, max_value=250)
goal = st.sidebar.selectbox("Health Goal", ["Weight Loss", "Maintain Weight", "Muscle Gain"])
dietary_pref = st.sidebar.multiselect("Dietary Preferences", ["Vegetarian", "Vegan", "Gluten-Free", "None"])

# Additional Inputs for Personalization
allergies = st.sidebar.text_input("Allergies (comma-separated)", "")
exercise_level = st.sidebar.selectbox("Exercise Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])

st.sidebar.markdown("### Set Meal Plan Duration")
days = st.sidebar.slider("Meal Plan Duration (days)", 1, 7, 7)

# Submit Button
if st.sidebar.button("Generate Meal Plan"):
    # -------------------------
    # 3. Mock Meal Plan Generation
    # -------------------------
    st.header("Your Personalized Meal Plan")

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

    # Display the meal plan
    for day in range(1, days + 1):
        st.subheader(f"Day {day}")
        st.write(meal_plan[f'Day {day}'])

    # -------------------------
    # 4. Dynamic Grocery List and Price Comparison (Mockup)
    # -------------------------
    st.header("Grocery Price Optimization")
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

    # -------------------------
    # 5. Visualization (Calorie Intake Mockup)
    # -------------------------
    st.header("Meal Plan Nutrition Stats")
    
    # Mockup data for calorie breakdown
    calories = np.random.randint(300, 800, size=(days, 4))
    meals_labels = ['Breakfast', 'Lunch', 'Snack', 'Dinner']
    
    fig, ax = plt.subplots()
    ax.bar(meals_labels, calories.sum(axis=0), color=['green', 'blue', 'orange', 'red'])
    ax.set_ylabel('Total Calories')
    ax.set_title('Total Calories per Meal Over 7 Days')
    
    st.pyplot(fig)
     # -------------------------
    # 6. Download Options (CSV)
    # -------------------------
    st.header("Download Your Meal Plan & Grocery List")
    
    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(df_grocery)

    st.download_button(
        label="Download Grocery List as CSV",
        data=csv,
        file_name='grocery_list.csv',
        mime='text/csv',
    )

