import streamlit as st

# -------------------------
# 1. Styling and Background
# -------------------------
st.markdown("""
<style>
/* Background GIF */
.stApp {
    background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif');
    background-size: cover; 
    background-position: top;
}

/* Styling for subheader with background for readability */
.subheader-container {
    background-color: rgba(51, 93, 59, 0.8); /* Dark green with 80% opacity */
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

/* Styling for tabs and tab content */
.stTabs [role="tab"] {
    background-color: rgba(51, 93, 59, 0.8);  /* Dark green with 80% opacity */
    color: #DAD7CD;  /* Light text */
    border-radius: 10px;
    margin: 0 5px;  /* Space between tabs */
}

.stTabs [role="tabpanel"] {
    background-color: rgba(51, 93, 59, 0.8);  /* Dark green with 80% opacity */
    color: #DAD7CD;  /* Light text */
    border-radius: 10px;
    padding: 20px; /* Padding inside tab content */
}

/* Container for the main content */
.content-section {
    background-color: rgba(255, 255, 255, 0.8);  /* Light background for readability */
    border-radius: 10px;
    padding: 20px;
    max-width: 80%;
    margin: 20px auto; /* Center the container */
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

# -------------------------
# 2. Title Section with Logo
# -------------------------
st.markdown("""
<div class="text-container">
    <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo">
    <div class="subheader-container">
        <h2>Get Fit, Eat Smart, Spend Less</h2>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------------
# 3. Tabs
# -------------------------
tab1, tab2, tab3, tab4 = st.tabs(['Meal Plan', 'Recipes', 'Ingredients', 'Meal Wrap'])

# -------------------------
# 4. Meal Plan Tab Content
# -------------------------
with tab1:
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("Your Personalized Meal Plan")

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

    # Displaying meal plans in cards
    for day, meals in meal_plan.items():
        st.markdown(f"""
            <div class="card" onclick="alert('{day} Meal Plan: \\n- {'\\n- '.join(meals)}')">
                <div class="card-content">
                    <h3>{day}</h3>
                    <p>Click to see meals</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# 5. Recipes Tab Content
# -------------------------
with tab2:
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("Recipes")
    st.write("Fill in later.")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# 6. Ingredients Tab Content
# -------------------------
with tab3:
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("Ingredients")
    st.write("Fill in later.")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# 7. Meal Wrap Tab Content
# -------------------------
with tab4:
    st.markdown('<div class="content-section">', unsafe_allow_html=True)
    st.subheader("Meal Wrap - Your Meal Plan Stats")
    st.write("Fill in later.")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# 8. Footer
# -------------------------
st.markdown("""
<footer>
    <p style="text-align: center; color: #DAD7CD;">© 2024 Meal Steal. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)
