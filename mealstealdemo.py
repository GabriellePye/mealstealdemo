import streamlit as st

# Sample meal plan data
meal_plan = {
    'Day 1': ['Oatmeal with fruit', 'Grilled chicken salad', 'Apple', 'Quinoa with veggies'],
    'Day 2': ['Greek yogurt with honey', 'Turkey sandwich', 'Carrot sticks', 'Salmon with rice'],
    'Day 3': ['Smoothie', 'Pasta with tomato sauce', 'Nuts', 'Stir-fried tofu with broccoli'],
    # Add more days as needed
}

# Create three columns
col1, col2, col3 = st.columns([1, 1, 2])  # Adjust the column widths as necessary

# Column 1: Cards for each day
with col1:
    st.subheader('Meal Plans')
    selected_day = st.selectbox('Select a day:', list(meal_plan.keys()))

    for day in meal_plan.keys():
        if st.button(f"{day} Meal Plan"):
            selected_day = day  # Update the selected day

# Column 2: Placeholder for additional content
with col2:
    st.subheader('Additional Content')
    st.write("This column can hold other information.")

# Column 3: Display the selected meal plan
with col3:
    st.subheader(f"Meal Plan for {selected_day}")
    if selected_day:
        st.write('\n- '.join(meal_plan[selected_day]))  # Display meals for the selected day

