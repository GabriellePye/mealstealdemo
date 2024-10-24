import streamlit as st

# Sample meal plan data
meal_plan = {
    'Day 1': ['Oatmeal with fruit', 'Grilled chicken salad', 'Apple', 'Quinoa with veggies'],
    'Day 2': ['Greek yogurt with honey', 'Turkey sandwich', 'Carrot sticks', 'Salmon with rice'],
    'Day 3': ['Smoothie', 'Pasta with tomato sauce', 'Nuts', 'Stir-fried tofu with broccoli'],
    'Day 4': ['Eggs and toast', 'Chickpea salad', 'Granola bar', 'Beef stir-fry'],
    'Day 5': ['Pancakes', 'Veggie wrap', 'Yogurt', 'Baked chicken with potatoes'],
}

# Create two main columns that take up the whole page
col1, col2 = st.columns([1, 2])  # Adjust the ratios as necessary

# Column 1: Meal Plan Cards
with col1:
    st.header('Meal Plans')
    
    # Create buttons as cards for each day
    selected_day = None  # Variable to hold the selected day

    for day in meal_plan.keys():
        if st.button(day):
            selected_day = day  # Update selected day when button is clicked
            st.session_state.selected_day = selected_day  # Store in session state

# Column 2: Display Selected Meal Plan
with col2:
    st.header('Selected Meal Plan')

    if selected_day:
        st.subheader(f"Meal Plan for {selected_day}")
        st.write('\n- '.join(meal_plan[selected_day]))  # Display meals for the selected day
    else:
        st.write("Click on a meal plan to view details here.")
