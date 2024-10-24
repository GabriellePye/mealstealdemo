import streamlit as st

# CSS for full-page layout
st.markdown("""
<style>
    /* Full height for the app */
    .stApp {
        background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif');
        background-size: cover; 
        background-position: center;
        height: 100vh; /* Full viewport height */
        color: #DAD7CD; /* Set text color */
    }

    /* Header styling */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px 0; /* Add some margin */
    }

    .header-container img {
        width: 100px; /* Adjust size */
        margin-right: 20px; /* Space between logo and subheader */
    }

    /* Meal Plan Cards */
    .card {
        background-color: rgba(51, 93, 59, 0.8);
        color: #DAD7CD;
        width: 100%; /* Make the cards full width */
        height: 160px;
        margin: 20px 0; /* Space between cards */
        cursor: pointer;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        transition: transform 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .card:hover {
        transform: scale(1.05);
    }

    /* Meal Plan Section */
    .meal-plan-section {
        padding: 20px;
        border-radius: 10px;
        backdrop-filter: blur(20px);
        background: rgba(255, 255, 255, 0.1);
        color: #DAD7CD;
        height: calc(100vh - 160px); /* Fill remaining height */
        overflow-y: auto; /* Enable scrolling */
    }
</style>
""", unsafe_allow_html=True)

# Header with logo and subheader
st.markdown("""
<div class="header-container">
    <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo">
    <h2>Get Fit, Eat Smart, Spend Less</h2>
</div>
""", unsafe_allow_html=True)

# Sample meal plan data
meal_plan = {
    'Day 1': ['Oatmeal with fruit', 'Grilled chicken salad', 'Apple', 'Quinoa with veggies'],
    'Day 2': ['Greek yogurt with honey', 'Turkey sandwich', 'Carrot sticks', 'Salmon with rice'],
    'Day 3': ['Smoothie', 'Pasta with tomato sauce', 'Nuts', 'Stir-fried tofu with broccoli'],
    'Day 4': ['Eggs and toast', 'Chickpea salad', 'Granola bar', 'Beef stir-fry'],
    'Day 5': ['Pancakes', 'Veggie wrap', 'Yogurt', 'Baked chicken with potatoes'],
}

# Main layout
st.title("Meal Plans")
selected_day = None

# Create meal plan buttons
for day in meal_plan.keys():
    if st.button(day, key=day):
        selected_day = day  # Update selected day when button is clicked

# Meal Plan Display Section
st.markdown('<div class="meal-plan-section">', unsafe_allow_html=True)
st.subheader('Selected Meal Plan')
if selected_day:
    st.write(f"**{selected_day}**")
    st.write('\n- '.join(meal_plan[selected_day]))  # Display meals for the selected day
else:
    st.write("Click on a meal plan to view details here.")
st.markdown('</div>', unsafe_allow_html=True)

