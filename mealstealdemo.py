import streamlit as st

# CSS for card styling
st.markdown("""
<style>
/* Cards for meal plan */
.card {
    position: relative;
    width: 220px; /* Adjust width as needed */
    height: 320px; /* Adjust height as needed */
    background: mediumturquoise;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
    font-weight: bold;
    border-radius: 15px;
    cursor: pointer;
    transition: all 0.5s; /* Smooth transitions */
}

/* Styling for card hover effects */
.card::before,
.card::after {
    position: absolute;
    content: "";
    width: 20%;
    height: 20%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
    font-weight: bold;
    background-color: lightblue;
    transition: all 0.5s; /* Smooth transitions */
}

.card::before {
    top: 0;
    right: 0;
    border-radius: 0 15px 0 100%; /* Top right corner rounded */
}

.card::after {
    bottom: 0;
    left: 0;
    border-radius: 0 100% 0 15px; /* Bottom left corner rounded */
}

/* Hover effects for cards */
.card:hover::before,
.card:hover::after {
    width: 100%; /* Expand on hover */
    height: 100%; /* Expand on hover */
    border-radius: 15px; /* Rounded corners on hover */
}

.card:hover:after {
    content: "Meal Plan"; /* Show meal plan text on hover */
    color: #fff; /* Text color for visibility */
}

/* General styles for meal plan section */
.meal-plan-section {
    margin-top: 20px; /* Space above meal plan section */
    padding: 20px; /* Padding for content */
    border-radius: 10px; /* Rounded corners */
    backdrop-filter: blur(20px); /* Frosted effect */
    background: rgba(255, 255, 255, 0.1); /* Slightly transparent background */
    color: #DAD7CD; /* Light text color */
}
</style>
""", unsafe_allow_html=True)

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

# Create header
st.markdown('<h2 style="text-align: center;">Your Personalized Meal Plan</h2>', unsafe_allow_html=True)

# Render cards for meal plans
day_count = len(meal_plan)  # Show all days, or you can limit this with a variable
cols = st.columns(3)  # Create three columns

# Placeholder for displaying selected meal
selected_meal = st.empty() 

for idx, (day, meals) in enumerate(meal_plan.items()):
    with cols[idx % 3]:  # Distribute the days across columns
        if st.button(day, key=day):  # Make buttons for each day
            selected_meal.markdown(f'### {day} Meal Plan:\n- ' + '\n- '.join(meals))  # Display selected meals
        
        # Render the card using HTML
        st.markdown(f"""
        <div class="card" style="cursor: pointer;" onclick="this.click();">
            <div class="card-content">
                <h3>{day}</h3>
                <p>Click for meals</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Meal Plan Display Section
st.markdown('<div class="meal-plan-section">', unsafe_allow_html=True)
st.subheader('Selected Meal Plan')
if selected_meal:
    st.write(selected_meal)  # Display meals for the selected day
else:
    st.write("Click on a meal plan to view details here.")
st.markdown('</div>', unsafe_allow_html=True)

