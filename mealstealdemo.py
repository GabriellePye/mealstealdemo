import streamlit as st

# -------------------------
# 1. Styling and Background
# -------------------------

# Custom CSS for styling
st.markdown("""
    <style> 
    /* App Background */
    .stApp {
        background: url('https://i.ibb.co/MpbbQDx/meal-steal-bg.gif'); /* Replace with your GIF URL */
        background-size: cover; 
        background-position: top;
    }

    /* Centered logo and subheader container */
    .text-container {
        text-align: center;
        margin: 50px auto;
    }

    .text-container img { 
        width: 200px;
    }

    /* Subheader with solid background for readability */
    .subheader {
        background-color: rgba(255, 255, 255, 0.8); /* White transparent background */
        padding: 20px;
        border-radius: 10px;
        display: inline-block;
        margin-top: 20px;
    }

    /* Styling for the individual tabs */
    .stTabs [role='tablist'] .stTab {
        background-color: #2E8B57; /* Background for each tab */
        border-radius: 10px; /* Rounded corners */
        padding: 10px;
        margin: 0 5px;
    }

    /* Hover effect for tabs */
    .stTabs [role='tablist'] .stTab:hover {
        background-color: #67944C; /* Hover color */
    }

    /* Active tab style */
    .stTabs [role='tablist'] .stTab[aria-selected="true"] {
        background-color: #4CAF50; /* Active tab color */
        color: white;
    }

    /* Tab content pages with a full solid background */
    .tab-content {
        background-color: rgba(255, 255, 255, 0.9); /* White solid background */
        padding: 20px;
        border-radius: 15px; /* Rounded corners */
        margin-top: 20px;
        max-width: 80%;
        margin-left: auto;
        margin-right: auto;
    }

    </style>
""", unsafe_allow_html=True)

# -------------------------
# 2. Logo and Subheader
# -------------------------

st.markdown("""
    <div class="text-container">
        <img src="https://i.ibb.co/tmQpKH2/1-removebg-preview.png" alt="Meal Steal Logo"> <!-- Your logo URL -->
        <div class="subheader">
            <h2>Get Fit, Eat Smart, Spend Less</h2>
        </div>
    </div>
""", unsafe_allow_html=True)

# -------------------------
# 3. Tabs and Content
# -------------------------

# Creating tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(['Meal Plan', 'Recipes', 'Ingredients', 'Meal Wrap'])

# Apply individual backgrounds to the tabs' content
with tab1:
    st.markdown("<div class='tab-content'><h3>Your Personalized Meal Plan</h3></div>", unsafe_allow_html=True)
    st.write("Content for the meal plan goes here...")

with tab2:
    st.markdown("<div class='tab-content'><h3>Recipes</h3></div>", unsafe_allow_html=True)
    st.write("Content for recipes goes here...")

with tab3:
    st.markdown("<div class='tab-content'><h3>Ingredients</h3></div>", unsafe_allow_html=True)
    st.write("Content for ingredients goes here...")

with tab4:
    st.markdown("<div class='tab-content'><h3>Meal Wrap</h3></div>", unsafe_allow_html=True)
    st.write("Content for meal wrap stats goes here...")

# -------------------------
# 4. Footer
# -------------------------

st.markdown("""
    <footer>
        <p style="text-align: center;">© 2024 Meal Steal. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
