import streamlit as st
import pandas as pd
import os
import streamlit.components.v1 as components



st.set_page_config(
    page_title="🥗 Food Waste Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Global Page Background and Text Styling ---
st.markdown("""
<style>
    /* --- Global Background & Text --- */
    html, body, .main, .block-container {
        background-color: #abdbe3 !important;  /* Slightly darker than #f5e8ff */
        color: #000000;
        font-family: 'Segoe UI', sans-serif;
    }

    /* --- Headings: All in Violet --- */
    h1, h2, h3, h4, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #4B0082 !important;
    }

    /* --- Sidebar Container Styling --- */
    [data-testid="stSidebar"] {
        background:  background: linear-gradient(#044a88);

 /* Matches main background */
        padding: 10px 15px !important;
        margin: 0;
        border-radius: 0;
        box-shadow: none;
    }

    /* --- Sidebar Buttons with Gradient Text --- */
    .sidebar .sidebar-content {
        background-color: transparent;
    }

   .sidebar-nav button {
    width: 100%;
    padding: 12px 20px;
    margin: 6px 0;
    background-color: transparent !important;  /* Fully transparent */
    border: none !important;
    text-align: left;
    font-weight: bold;
    font-size: 1.1rem;
    font-family: 'Segoe UI', sans-serif;
    cursor: pointer;

    background-image: linear-gradient(to right, #4B0082, #9575CD);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 1px;
    box-shadow: none;
    transition: 0.3s ease;
}

.sidebar-nav button:hover {
    background-color: transparent !important;  /* No white hover */
    transform: translateX(2px);
}

.sidebar-selected {
    background-color: transparent !important;
}


    /* --- Sidebar Inner Text --- */
    [data-testid="stSidebar"] * {
        color: #3C0066 !important;
    }

    /* --- Download Button --- */
    .stDownloadButton>button {
        background-color: #E8EAF6;
        color: #283593;
        border: 1px solid #C5CAE9;
        padding: 8px 16px;
        border-radius: 8px;
        font-weight: bold;
    }

    .stDownloadButton>button:hover {
        background-color: #C5CAE9;
        color: #1A237E;
    }

    /* --- Caption --- */
    .caption {
        color: #6A1B9A;
        font-style: italic;
        text-align: center;
    }

    /* --- Data Table Container --- */
    .dataframe {
        background-color: white;
        border-radius: 12px;
        padding: 10px;
    }

    /* --- Lavender Card --- */
    .lavender-card {
        background-color: #F3E5F5;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        font-size: 1.1rem;
        color: #000000;
        line-height: 1.7;
        margin-top: 20px;
    }

    /* --- Dropdown Label Styling --- */
    label {
        font-size: 1.1rem !important;
        font-weight: 600;
        color: #4B0082 !important;
    }

    /* --- Multiselect Selected Items --- */
    .stMultiSelect span {
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)





if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Overview"

def set_page(page_name):
    st.session_state.selected_page = page_name

with st.sidebar:
    st.markdown("""
    <div class="sidebar-title">🥗Dashboard</div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="sidebar-nav">', unsafe_allow_html=True)
    if st.button("📽️ Project Overview"):
        set_page("Overview")
    if st.button("🧱 View Tables"):
        set_page("View Tables")
    if st.button("🔍 SQL Query Insights"):
        set_page("SQL Queries")
    if st.button("📈 My Analytics"):
        set_page("Analytics")
    if st.button("➕ Add / Update Records"):
        set_page("Add Update")
    if st.button("👩🏻 Profile Overview"):
        set_page("My Profile")
    st.markdown('</div>', unsafe_allow_html=True)

# Load datasets
@st.cache_data
def load_data():
    return {
        "claims": pd.read_csv("./Preprocessed_Datasets/cleaned_claims_data.csv"),
        "food": pd.read_csv("./Preprocessed_Datasets/cleaned_food_listings_data.csv"),
        "providers": pd.read_csv("./Preprocessed_Datasets/cleaned_providers_data.csv"),
        "receivers": pd.read_csv("./Preprocessed_Datasets/cleaned_receivers_data.csv"),
    }

data = load_data()
claims_df = data["claims"]
food_listings_df = data["food"]
providers_df = data["providers"]
receivers_df = data["receivers"]

def download_button(df, filename):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download as CSV", csv, filename, "text/csv")
# --- Global Page Background and Text Styling ---
st.markdown("""
    <style>
        body {
            background-color: #FAFAFA;
        }
        .main {
            background-color: #FAFAFA;
            color: #2E7D32;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3 {
            font-family: 'Segoe UI', sans-serif;
        }
        
/* --- Style for Streamlit Tabs (text color & size) --- */
        /* --- Sidebar Title Styling --- */
.sidebar-title {
    font-size: 1.4rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 20px;
    background: linear-gradient(to right, #4B0082, #9575CD);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Segoe UI', sans-serif;
    letter-spacing: 1px;
}



[data-baseweb="tab"] {
    border-bottom: 3px solid transparent !important;
}

[data-baseweb="tab"][aria-selected="true"] {
    border-bottom: 3px solid #4B0082 !important; /* Active tab underline */
    color: #4B0082 !important;
}
            /* --- Custom Tab Text Style --- */
[data-baseweb="tab-list"] button {
    color: #4B0082 !important;
    font-size: 1.2rem !important;
    font-family: 'Segoe UI', sans-serif' !important;
    font-weight: 600;
    padding: 10px 18px;
    background: transparent;
    border: none !important;
}

/* --- Hover Effect --- */
[data-baseweb="tab-list"] button:hover {
    color: #7b1fa2 !important;
}

/* --- Active Tab Underline --- */
[data-baseweb="tab"][aria-selected="true"] {
    border-bottom: 3px solid #4B0082 !important;
    color: #4B0082 !important;
}

/* --- Remove Red Focus Outline on Click --- */
[data-baseweb="tab"] button:focus,
[data-baseweb="tab"] button:active {
    outline: none !important;
    box-shadow: none !important;
    border: none !important;
}


    </style>
""", unsafe_allow_html=True)



page = st.session_state.selected_page

# --- OVERVIEW PAGE ---

# --- OVERVIEW PAGE ---
if page == "Overview":
    # Inject styles
    st.markdown("""
        <style>
        .title-style {
            text-align: center;
            font-size: 36px;
            font-weight: 800;
            color: #5c1d8a;
            margin-bottom: 20px;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 30px;
            font-weight: bold;
            color: #5c1d8a;
        }
        .tab-container {
            background-color: white;
            border-radius: 20px;
            padding: 30px;
            margin-top: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        }
        h3 {
            color: #5c1d8a;
            margin-bottom: 15px;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
            font-size: 17px;
        }
        p {
            font-size: 17px;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Page title
    st.markdown('<div class="title-style">🍽️ Local Food Wastage Management System</div>', unsafe_allow_html=True)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📌 Introduction", 
        "🎯 Objective", 
        "📦 Modules", 
        "🛠️ Technology Stack"
    ])

    with tab1:
        st.markdown("""
        <div class="tab-container">
            <h3>📌 Introduction</h3>
            <p>
                The <strong>Local Food Wastage Management System</strong> is an innovative initiative designed to address the issue of food surplus in urban environments.
                It bridges the gap between <em>food donors</em> (like restaurants, canteens, hostels, and event organizers) and <em>those in need</em> such as NGOs and underprivileged communities.
            </p>
            <p>
                This platform promotes responsible consumption by enabling the safe, timely, and efficient redistribution of excess food—ultimately minimizing waste and maximizing impact.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="tab-container">
            <h3>🎯 Project Objective</h3>
            <ul>
                <li>Promote responsible consumption and reduce food wastage.</li>
                <li>Create a transparent, accountable, and real-time food donation process.</li>
                <li>Support NGOs, shelters, and communities with accessible food resources.</li>
                <li>Align with <strong>SDG Goal 12: Responsible Consumption and Production</strong>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="tab-container">
            <h3>📦 Modules</h3>
            <ul>
                <li><strong>Provider & Receiver Registration</strong><br>Onboard food donors and receivers through secure, structured sign-up.</li>
                <li><strong>Food Listings & Claims</strong><br>Donors list available surplus food, and receivers can claim items in real-time.</li>
                <li><strong>Real-time SQL Dashboard</strong><br>Interact with live food data using custom SQL queries.</li>
                <li><strong>Data Visual Analytics</strong><br>Visualize data trends like food expiry, claims, and impact analytics.</li>
                <li><strong>Contact & Support</strong><br>Dedicated channel for help, FAQs, and feedback.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <div class="tab-container">
            <h3>🛠️ Technology Stack</h3>
            <ul>
                <li><strong>Python</strong> – Core programming language</li>
                <li><strong>Streamlit</strong> – Interactive frontend dashboard</li>
                <li><strong>PostgreSQL</strong> – Relational database for structured food data</li>
                <li><strong>Pandas & Plotly</strong> – Data manipulation and dynamic charts</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)






    
elif page == "View Tables":
    dataset_option = st.selectbox("Select a dataset to view", ["Claims", "Food Listings", "Providers", "Receivers"])
    
    if dataset_option == "Claims":
        st.subheader("🔍 Filter: Claim Records")
        status = st.multiselect("Select Status", options=claims_df["Status"].unique())
        receiver_id = st.multiselect("Select Receiver ID", options=claims_df["Receiver_ID"].unique())
        filtered_df = claims_df.copy()
        if status:
            filtered_df = filtered_df[filtered_df["Status"].isin(status)]
        if receiver_id:
            filtered_df = filtered_df[filtered_df["Receiver_ID"].isin(receiver_id)]
        st.dataframe(filtered_df, use_container_width=True)
        download_button(filtered_df, "filtered_claims.csv")

    elif dataset_option == "Food Listings":
        st.subheader("🔍 Filter: Food Listings")
        provider_type = st.multiselect("Provider Type", options=food_listings_df["Provider_Type"].unique())
        location = st.multiselect("Location", options=food_listings_df["Location"].unique())
        food_type = st.multiselect("Food Type", options=food_listings_df["Food_Type"].unique())
        meal_type = st.multiselect("Meal Type", options=food_listings_df["Meal_Type"].unique())
        filtered_df = food_listings_df.copy()
        if provider_type:
            filtered_df = filtered_df[filtered_df["Provider_Type"].isin(provider_type)]
        if location:
            filtered_df = filtered_df[filtered_df["Location"].isin(location)]
        if food_type:
            filtered_df = filtered_df[filtered_df["Food_Type"].isin(food_type)]
        if meal_type:
            filtered_df = filtered_df[filtered_df["Meal_Type"].isin(meal_type)]
        st.dataframe(filtered_df, use_container_width=True)
        download_button(filtered_df, "filtered_food_listings.csv")

    elif dataset_option == "Providers":
        st.subheader("🔍 Filter: Providers List")
        city = st.multiselect("City", options=providers_df["City"].unique())
        provider_type = st.multiselect("Type", options=providers_df["Type"].unique())
        filtered_df = providers_df.copy()
        if city:
            filtered_df = filtered_df[filtered_df["City"].isin(city)]
        if provider_type:
            filtered_df = filtered_df[filtered_df["Type"].isin(provider_type)]
        st.dataframe(filtered_df, use_container_width=True)
        download_button(filtered_df, "filtered_providers.csv")

    elif dataset_option == "Receivers":
        st.subheader("🔍 Filter: Receivers List")
        receiver_type = st.multiselect("Receiver Type", options=receivers_df["Type"].unique())
        city = st.multiselect("City", options=receivers_df["City"].unique())
        filtered_df = receivers_df.copy()
        if receiver_type:
            filtered_df = filtered_df[filtered_df["Type"].isin(receiver_type)]
        if city:
            filtered_df = filtered_df[filtered_df["City"].isin(city)]
        st.dataframe(filtered_df, use_container_width=True)
        download_button(filtered_df, "filtered_receivers.csv")

elif page == "SQL Queries":
    import plotly.express as px
    import pandas as pd
    from db import get_connection

    st.markdown("### 🧠 SQL Query Insights")

    # Establish DB connection
    try:
        con = get_connection()
        cur = con.cursor()
        st.success("✅ Connected to PostgreSQL database")
    except Exception as e:
        st.error(f"❌ Failed to connect to database: {e}")
        st.stop()

    # Helper: Load unique cities from CSV for dropdown filter
    @st.cache_data
    def get_unique_provider_cities():
        df = pd.read_csv("./Preprocessed_Datasets/cleaned_providers_data.csv")
        return sorted(df["City"].dropna().unique().tolist())

    # SQL Descriptive Questions and Queries
    question_map = {
    "Total number of food providers": 
        "SELECT COUNT(*) AS Total_Providers FROM Providers;",

    "Total number of receivers": 
        "SELECT COUNT(*) AS Total_Receivers FROM Receivers;",

    "Contact details of food providers located in a selected city": 
        "SELECT Name, Contact, Address, City FROM Providers WHERE City = '{City}';",

    "Top 5 food listings with highest quantity": 
        "SELECT Food_Name, MAX(Quantity) AS Max_Quantity FROM Food_Listings GROUP BY Food_Name ORDER BY Max_Quantity DESC LIMIT 5;;",

    "Average quantity of food listed per provider": 
        "SELECT P.Name, AVG(F.Quantity) AS Avg_Quantity FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.Name;",

    "Total number of food listings by type": 
        "SELECT Meal_Type, COUNT(*) AS Total_Listings FROM Food_Listings GROUP BY Meal_Type;",

    "Receivers by city (count)": 
        "SELECT City, COUNT(*) AS Total_Receivers FROM Receivers GROUP BY City ORDER BY Total_Receivers DESC;",

    "Distribution of claims by status": 
        "SELECT Status, COUNT(*) AS Total_Claims FROM Claims GROUP BY Status;",

    "Most active food receiver (by number of claims)": 
        "SELECT R.Name, COUNT(*) AS Total_Claims FROM Receivers R JOIN Claims C ON R.Receiver_ID = C.Receiver_ID GROUP BY R.Name ORDER BY Total_Claims DESC LIMIT 1;",

    "Food listing with maximum claimed quantity": 
        " SELECT F.Food_Name, COUNT(*) AS Claim_Count FROM Food_Listings F JOIN Claims C ON F.Food_ID = C.Food_ID GROUP BY F.Food_Name ORDER BY Claim_Count DESC ;",

    "Number of claims per meal type": 
        "SELECT F.Meal_Type, COUNT(*) AS Total_Claims FROM Food_Listings F JOIN Claims C ON F.Food_ID = C.Food_ID GROUP BY F.Meal_Type;",

    "Cities with most food listings": 
        "SELECT C.City, C.Total_Listings FROM (SELECT P.City, COUNT(*) AS Total_Listings FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.City) C JOIN (SELECT MAX(Total_Listings) AS Max_Listing FROM (SELECT P.City, COUNT(*) AS Total_Listings FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.City) AS Temp) M ON C.Total_Listings = M.Max_Listing;",

    "Pending claims older than 2 days": 
        "SELECT Claim_ID, Food_ID, Receiver_ID, Status, Timestamp FROM Claims WHERE Status = 'Pending' AND Timestamp <= CURRENT_DATE - INTERVAL '2 days';",

    "Receivers who have not made any claim": 
        "SELECT Name FROM Receivers WHERE Receiver_ID NOT IN (SELECT DISTINCT Receiver_ID FROM Claims);",

    "Total food quantity claimed vs listed": 
        "SELECT (SELECT SUM(Quantity) FROM Food_Listings) AS Total_Listed,COUNT(Food_ID) AS Total_Claimed_Items FROM Claims;"
    }
    chartable_questions = [
        "Top 5 food listings with highest quantity",
        "Total number of food listings by type",
        "Receivers by city (count)",
        "Food listing with maximum claimed quantity",
        "Distribution of claims by status",
        "Number of claims per meal type",
        "Cities with most food listings"
    ]


    # Select question
    question_labels = list(question_map.keys())
    question = st.selectbox("📌 Select a question to analyze", question_labels)

    # If selected query needs a city input
    city_filter_needed = (question == "Contact details of food providers located in a selected city")

    selected_city = None
    if city_filter_needed:
        cities = get_unique_provider_cities()
        selected_city = st.selectbox("🏙️ Select a city to filter providers", cities)

    if question in chartable_questions:
        chart_type = st.radio("📊 Choose visualization type", ["Table Only", "Bar Chart", "Pie Chart"], horizontal=True)
    else:
        chart_type = "Table Only"

    # Build final SQL query
    base_query = question_map[question]
    

    try:
     if city_filter_needed:
        final_query = "SELECT Name, Contact, Address, City FROM Providers WHERE City = %s;"
        df = pd.read_sql_query(final_query, con, params=(selected_city,))
     else:
        final_query = question_map[question]
        df = pd.read_sql_query(final_query, con)

     st.success("✅ Query executed successfully.")
     st.dataframe(df, use_container_width=True)

     if chart_type != "Table Only":
        if df.shape[1] >= 2:
            col1, col2 = df.columns[0], df.columns[1]

            if chart_type == "Bar Chart":
                fig = px.bar(df, x=col1, y=col2, color=col2, title="Bar Chart View")
            elif chart_type == "Pie Chart":
                fig = px.pie(df, names=col1, values=col2, title="Pie Chart View")

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ Not enough data columns for visualization.")
    except Exception as e:
     st.error(f"❌ Query failed: {e}")





elif page == "Analytics":
    import plotly.express as px
    import pandas as pd
    from db import get_connection

    st.markdown("### 📊 In-Depth Analytics Dashboard")

    # DB connection
    try:
        con = get_connection()
        st.success("✅ Connected to PostgreSQL database")
    except Exception as e:
        st.error(f"❌ Database connection error: {e}")
        st.stop()

    # Query Categories
    category_map = {
        "Provider Insights": [
            "List of active providers (who have listed food)",
            "Provider with maximum food listed",
            "Top 5 providers by quantity listed",
            "Average quantity listed per provider",
            "Providers who listed more than 100 units of food"
        ],
        "Receiver Insights": [
            "Receiver with highest number of claims",
            "Receivers who claimed from multiple cities",
            "Receivers with zero pending claims",
            "Top 3 most frequent receivers",
            "Receiver distribution across cities"
        ],
        "Food Listing Insights": [
            "Most frequently listed food item",
            "Meal types with highest average quantity",
            "Total quantity of each meal type",
            "List of unique food items listed",
            "Food items listed by more than 3 providers"
        ],
        "Claim Insights": [
            "Food items with more than 5 claims",
            "Food items never claimed",
            "Most claimed food item by quantity",
            "Claims grouped by receiver and status",
            "Claim frequency per provider"
        ],
        "City-based Insights": [
            "Top 3 cities with highest claims",
            "Total listings city-wise",
            "Claims vs listings per city",
            "Providers per city",
            "Receivers per city"
        ],
        "Temporal Trends": [
            "Number of listings per day (last 7 days)",
            "Number of claims per day (last 7 days)",
            "Claims over time (monthly trend)",
            "Listings over time (monthly trend)",
            "Claims vs Listings daily ratio (last 14 days)"
        ]
    }

    # Chartable queries
    chartable_questions = [
        "Top 5 providers by quantity listed",
        "Receiver distribution across cities",
        "Meal types with highest average quantity",
        "Total quantity of each meal type",
        "Food items with more than 5 claims",
        "Top 3 cities with highest claims",
        "Total listings city-wise",
        "Claims vs listings per city",
        "Providers per city",
        "Receivers per city",
        "Number of listings per day (last 7 days)",
        "Number of claims per day (last 7 days)",
        "Claims vs Listings daily ratio (last 14 days)"
    ]

    # Full query map
    query_map = {
        # Provider Insights
        "List of active providers (who have listed food)":
            "SELECT DISTINCT P.Name FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID;",

        "Provider with maximum food listed":
            "SELECT P.Name, SUM(F.Quantity) AS Total_Quantity FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.Name ORDER BY Total_Quantity DESC LIMIT 1;",

        "Top 5 providers by quantity listed":
            "SELECT P.Name, SUM(F.Quantity) AS Total_Quantity FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.Name ORDER BY Total_Quantity DESC LIMIT 5;",

        "Average quantity listed per provider":
            "SELECT P.Name, AVG(F.Quantity) AS Avg_Quantity FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.Name;",

        "Providers who listed more than 100 units of food":
            "SELECT P.Name, SUM(F.Quantity) AS Total FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.Name HAVING SUM(F.Quantity) > 100;",

        # Receiver Insights
        "Receiver with highest number of claims":
            "SELECT R.Name, COUNT(*) AS Total_Claims FROM Receivers R JOIN Claims C ON R.Receiver_ID = C.Receiver_ID GROUP BY R.Name ORDER BY Total_Claims DESC LIMIT 1;",

        "Receivers who claimed from multiple cities":
            "SELECT DISTINCT R.Name FROM Receivers R JOIN Claims C ON R.Receiver_ID = C.Receiver_ID JOIN Food_Listings F ON C.Food_ID = F.Food_ID JOIN Providers P ON P.Provider_ID = F.Provider_ID GROUP BY R.Name HAVING COUNT(DISTINCT P.City) > 1;",

        "Receivers with zero pending claims":
            "SELECT R.Name FROM Receivers R WHERE R.Receiver_ID NOT IN (SELECT Receiver_ID FROM Claims WHERE Status = 'Pending');",

        "Top 3 most frequent receivers":
            "SELECT R.Name, COUNT(*) AS Total_Claims FROM Receivers R JOIN Claims C ON R.Receiver_ID = C.Receiver_ID GROUP BY R.Name ORDER BY Total_Claims DESC LIMIT 3;",

        "Receiver distribution across cities":
            "SELECT City, COUNT(*) AS Total_Receivers FROM Receivers GROUP BY City;",

        # Food Listing Insights
        "Most frequently listed food item":
            "SELECT Food_Name, COUNT(*) AS Frequency FROM Food_Listings GROUP BY Food_Name ORDER BY Frequency DESC LIMIT 1;",

        "Meal types with highest average quantity":
            "SELECT Meal_Type, AVG(Quantity) AS Avg_Quantity FROM Food_Listings GROUP BY Meal_Type ORDER BY Avg_Quantity DESC;",

        "Total quantity of each meal type":
            "SELECT Meal_Type, SUM(Quantity) AS Total_Quantity FROM Food_Listings GROUP BY Meal_Type;",

        "List of unique food items listed":
            "SELECT DISTINCT Food_Name FROM Food_Listings ORDER BY Food_Name ASC;",

        "Food items listed by more than 3 providers":
            "SELECT Food_Name, COUNT(DISTINCT Provider_ID) AS Provider_Count FROM Food_Listings GROUP BY Food_Name HAVING COUNT(DISTINCT Provider_ID) > 3;",

        # Claim Insights
        "Food items with more than 5 claims":
            "SELECT F.Food_Name, COUNT(*) AS Claim_Count FROM Food_Listings F JOIN Claims C ON F.Food_ID = C.Food_ID GROUP BY F.Food_Name HAVING COUNT(*) > 5;",

        "Food items never claimed":
            "SELECT Food_Name FROM Food_Listings WHERE Food_ID NOT IN (SELECT DISTINCT Food_ID FROM Claims);",

        "Most claimed food item by quantity":
            "SELECT F.Food_Name, COUNT(C.Claim_ID) AS Total_Claims FROM Food_Listings F JOIN Claims C ON F.Food_ID = C.Food_ID GROUP BY F.Food_Name ORDER BY Total_Claims DESC LIMIT 1;",

        "Claims grouped by receiver and status":
            "SELECT R.Name, C.Status, COUNT(*) AS Count FROM Receivers R JOIN Claims C ON R.Receiver_ID = C.Receiver_ID GROUP BY R.Name, C.Status ORDER BY R.Name;",

        "Claim frequency per provider":
            "SELECT P.Name, COUNT(*) AS Total_Claims FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID JOIN Claims C ON C.Food_ID = F.Food_ID GROUP BY P.Name ORDER BY Total_Claims DESC;",

        # City-based Insights
        "Top 3 cities with highest claims":
            "SELECT P.City, COUNT(*) AS Claim_Count FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID JOIN Claims C ON F.Food_ID = C.Food_ID GROUP BY P.City ORDER BY Claim_Count DESC LIMIT 3;",

        "Total listings city-wise":
            "SELECT P.City, COUNT(*) AS Total_Listings FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID GROUP BY P.City;",

        "Claims vs listings per city":
            "SELECT P.City, COUNT(DISTINCT F.Food_ID) AS Listings, COUNT(C.Claim_ID) AS Claims FROM Providers P JOIN Food_Listings F ON P.Provider_ID = F.Provider_ID LEFT JOIN Claims C ON F.Food_ID = C.Food_ID GROUP BY P.City;",

        "Providers per city":
            "SELECT City, COUNT(*) AS Total_Providers FROM Providers GROUP BY City;",

        "Receivers per city":
            "SELECT City, COUNT(*) AS Total_Receivers FROM Receivers GROUP BY City;",

        # Temporal Trends
        "Number of listings per day (last 7 days)":
            "SELECT DATE(Expiry_Date) AS Date, COUNT(*) AS Listings FROM Food_Listings WHERE Expiry_Date >= CURRENT_DATE - INTERVAL '7 days' GROUP BY Date ORDER BY Date;",

        "Number of claims per day (last 7 days)":
            "SELECT DATE(Timestamp) AS Date, COUNT(*) AS Claims FROM Claims WHERE Timestamp >= CURRENT_DATE - INTERVAL '7 days' GROUP BY Date ORDER BY Date;",

        "Claims over time (monthly trend)":
            "SELECT DATE_TRUNC('month', Timestamp) AS Month, COUNT(*) AS Claims FROM Claims GROUP BY Month ORDER BY Month;",

        "Listings over time (monthly trend)":
            "SELECT DATE_TRUNC('month', Expiry_Date) AS Month, COUNT(*) AS Listings FROM Food_Listings GROUP BY Month ORDER BY Month;",

        "Claims vs Listings daily ratio (last 14 days)":
            "SELECT D.Date, COALESCE(L.Listings, 0) AS Listings, COALESCE(C.Claims, 0) AS Claims FROM (SELECT generate_series(CURRENT_DATE - INTERVAL '13 days', CURRENT_DATE, interval '1 day') AS Date) D LEFT JOIN (SELECT DATE(Expiry_Date) AS Date, COUNT(*) AS Listings FROM Food_Listings GROUP BY Date) L ON D.Date = L.Date LEFT JOIN (SELECT DATE(Timestamp) AS Date, COUNT(*) AS Claims FROM Claims GROUP BY Date) C ON D.Date = C.Date ORDER BY D.Date;"
    }

    # Step 1: Category selection
    category = st.selectbox("📂 Select Category", list(category_map.keys()))

    # Step 2: Question selection
    selected_question = st.selectbox("📌 Select Question", category_map[category])

    # Step 3: Chart selection
    if selected_question in chartable_questions:
        chart_type = st.radio("📊 Visualization Type", ["Table Only", "Bar Chart", "Pie Chart"], horizontal=True)
    else:
        chart_type = "Table Only"

    # Step 4: Execute Query
    try:
        df = pd.read_sql_query(query_map[selected_question], con)
        st.success("✅ Query executed successfully!")
        st.dataframe(df, use_container_width=True)

        if chart_type != "Table Only" and df.shape[1] >= 2:
            col1, col2 = df.columns[:2]
            if chart_type == "Bar Chart":
                fig = px.bar(df, x=col1, y=col2, color=col2, title=selected_question)
            elif chart_type == "Pie Chart":
                fig = px.pie(df, names=col1, values=col2, title=selected_question)
            st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"❌ Query failed: {e}")

elif page == "Add Update":
    from db import get_connection

    st.markdown("## 🛠️ Add / Update / Delete Records")

    # Step 1: Table and Action Selection
    table_options = ["Providers", "Receivers", "Food_Listings", "Claims"]
    action_options = ["Add", "Read", "Update", "Delete"]

    selected_table = st.selectbox("📋 Select a Table", table_options)
    selected_action = st.radio("⚙️ Choose Action", action_options, horizontal=True)

    conn = get_connection()
    cursor = conn.cursor()

    # Step 2: Add Provider Form
    if selected_table == "Providers" and selected_action == "Add":
        st.markdown("### ➕ Add New Provider")

        name = st.text_input("Provider Name")
        provider_type = st.selectbox("Provider Type", ["Individual", "Restaurant", "NGO", "Organization"])
        contact = st.text_input("Contact Number")
        address = st.text_area("Address")
        city = st.text_input("City")

        if st.button("Add Provider"):
            try:
                cursor.execute(
                    "INSERT INTO Providers (Name, Type, Address, City, Contact) VALUES (%s, %s, %s, %s, %s);",
                    (name, provider_type, address, city, contact)
                )
                conn.commit()
                st.success("✅ Provider added successfully!")
            except Exception as e:
                conn.rollback()
                st.error(f"❌ Failed to add provider: {e}")
        # Step 3: Read Provider Records
    if selected_table == "Providers" and selected_action == "Read":
        st.markdown("### 📖 View All Providers")
        try:
            cursor.execute("SELECT * FROM Providers;")
            records = cursor.fetchall()
            if records:
                st.dataframe(records, use_container_width=True)
            else:
                st.info("ℹ️ No providers found.")
        except Exception as e:
            st.error(f"❌ Failed to fetch records: {e}")
    # Step 4: Update Provider Record
    if selected_table == "Providers" and selected_action == "Update":
      st.markdown("### 🔄 Update Provider Details")
      try:
            cursor.execute("SELECT Provider_ID, Name FROM Providers ORDER BY Provider_ID;")
            provider_choices = cursor.fetchall()
            provider_dict = {f"{pid} - {pname}": pid for pid, pname in provider_choices}

            selected_provider = st.selectbox("Select Provider to Update", list(provider_dict.keys()))
            provider_id = provider_dict[selected_provider]

            new_name = st.text_input("New Name (leave blank to keep unchanged)")
            new_type = st.selectbox("New Type (optional)", ["", "Individual", "Restaurant", "NGO", "Organization"])
            new_contact = st.text_input("New Contact Number (leave blank to keep unchanged)")
            new_address = st.text_area("New Address (leave blank to keep unchanged)")
            new_city = st.text_input("New City (leave blank to keep unchanged)")

            if st.button("Update Provider"):
             update_fields = []
             values = []

             if new_name:
                update_fields.append("Name = %s")
                values.append(new_name)
             if new_type:
                update_fields.append("Type = %s")
                values.append(new_type)
             if new_address:
                update_fields.append("Address = %s")
                values.append(new_address)
             if new_city:
                update_fields.append("City = %s")
                values.append(new_city)
             if new_contact:
                update_fields.append("Contact = %s")
                values.append(new_contact)

             if update_fields:
                values.append(provider_id)
                query = f"UPDATE Providers SET {', '.join(update_fields)} WHERE Provider_ID = %s;"
                cursor.execute(query, values)
                conn.commit()
                st.success("✅ Provider updated successfully!")
             else:
                st.info("ℹ️ No changes were made.")
      except Exception as e:
         conn.rollback()
         st.error(f"❌ Failed to update provider: {e}")


    # Step 5: Delete Provider Record
    if selected_table == "Providers" and selected_action == "Delete":
         st.markdown("### ❌ Delete Provider")
         try:
            cursor.execute("SELECT Provider_ID, Name FROM Providers ORDER BY Provider_ID;")
            provider_choices = cursor.fetchall()
            provider_dict = {f"{pid} - {pname}": pid for pid, pname in provider_choices}

            selected_provider = st.selectbox("Select Provider to Delete", list(provider_dict.keys()))
            provider_id = provider_dict[selected_provider]

            if st.button("Delete Provider"):
                cursor.execute("DELETE FROM Providers WHERE Provider_ID = %s;", (provider_id,))
                conn.commit()
                st.success("✅ Provider deleted successfully!")
         except Exception as e:
            conn.rollback()
            st.error(f"❌ Failed to delete provider: {e}")

# --------------------- RECEIVERS CRUD ---------------------
    if selected_table == "Receivers":
     if selected_action == "Add":
        st.markdown("### ➕ Add New Receiver")
        name = st.text_input("Receiver Name")
        receiver_type = st.selectbox("Receiver Type", ["Individual", "Shelter", "NGO", "Orphanage"])
        city = st.text_input("City")
        contact = st.text_input("Contact Number")

        if st.button("Add Receiver"):
            try:
                cursor.execute(
                    "INSERT INTO Receivers (Name, Type, City, Contact) VALUES (%s, %s, %s, %s);",
                    (name, receiver_type, city, contact)
                )
                conn.commit()
                st.success("✅ Receiver added successfully!")
            except Exception as e:
                conn.rollback()
                st.error(f"❌ Failed to add receiver: {e}")

     elif selected_action == "Read":
        st.markdown("### 📖 View All Receivers")
        try:
            cursor.execute("SELECT * FROM Receivers;")
            st.dataframe(cursor.fetchall(), use_container_width=True)
        except Exception as e:
            st.error(f"❌ Failed to fetch records: {e}")

     elif selected_action == "Update":
        st.markdown("### 🔄 Update Receiver")
        try:
            cursor.execute("SELECT Receiver_ID, Name FROM Receivers ORDER BY Receiver_ID;")
            receivers = cursor.fetchall()
            receiver_dict = {f"{rid} - {rname}": rid for rid, rname in receivers}
            selected = st.selectbox("Select Receiver", list(receiver_dict.keys()))
            rid = receiver_dict[selected]

            new_name = st.text_input("New Name")
            new_type = st.selectbox("New Type", ["", "Individual", "Shelter", "NGO", "Orphanage"])
            new_city = st.text_input("New City")
            new_contact = st.text_input("New Contact")

            updates, values = [], []
            if new_name: updates.append("Name = %s"); values.append(new_name)
            if new_type: updates.append("Type = %s"); values.append(new_type)
            if new_city: updates.append("City = %s"); values.append(new_city)
            if new_contact: updates.append("Contact = %s"); values.append(new_contact)

            if updates:
                values.append(rid)
                query = f"UPDATE Receivers SET {', '.join(updates)} WHERE Receiver_ID = %s;"
                cursor.execute(query, values)
                conn.commit()
                st.success("✅ Receiver updated successfully!")
            else:
                st.info("ℹ️ No changes made.")
        except Exception as e:
            conn.rollback()
            st.error(f"❌ Failed to update receiver: {e}")

     elif selected_action == "Delete":
        st.markdown("### ❌ Delete Receiver")
        try:
            cursor.execute("SELECT Receiver_ID, Name FROM Receivers ORDER BY Receiver_ID;")
            receivers = cursor.fetchall()
            receiver_dict = {f"{rid} - {rname}": rid for rid, rname in receivers}
            selected = st.selectbox("Select Receiver", list(receiver_dict.keys()))
            rid = receiver_dict[selected]

            if st.button("Delete Receiver"):
                cursor.execute("DELETE FROM Receivers WHERE Receiver_ID = %s;", (rid,))
                conn.commit()
                st.success("✅ Receiver deleted successfully!")
        except Exception as e:
            conn.rollback()
            st.error(f"❌ Failed to delete receiver: {e}")

# --------------------- FOOD_LISTINGS CRUD ---------------------
    if selected_table == "Food_Listings":
     if selected_action == "Add":
        st.markdown("### ➕ Add New Food Listing")

        food_name = st.text_input("Food Name")
        quantity = st.number_input("Quantity", min_value=1, step=1)
        expiry_date = st.date_input("Expiry Date")
        provider_id = st.number_input("Provider ID", min_value=1, step=1)
        provider_type = st.selectbox("Provider Type", ["Individual", "Restaurant", "NGO", "Organization"])
        location = st.text_input("Location")
        food_type = st.selectbox("Food Type", ["Raw", "Cooked", "Packaged"])
        meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])

        if st.button("Add Food Listing"):
            try:
                cursor.execute(
                    '''INSERT INTO Food_Listings 
                       (Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s);''',
                    (food_name, quantity, expiry_date, provider_id, provider_type, location, food_type, meal_type)
                )
                conn.commit()
                st.success("✅ Food listing added successfully!")
            except Exception as e:
                conn.rollback()
                st.error(f"❌ Failed to add food listing: {e}")

     elif selected_action == "Read":
        st.markdown("### 📖 View All Food Listings")
        try:
            cursor.execute("SELECT * FROM Food_Listings;")
            st.dataframe(cursor.fetchall(), use_container_width=True)
        except Exception as e:
            st.error(f"❌ Failed to fetch records: {e}")

     elif selected_action == "Update":
        st.markdown("### 🔄 Update Food Listing")
        try:
            cursor.execute("SELECT Food_ID, Food_Name FROM Food_Listings ORDER BY Food_ID;")
            items = cursor.fetchall()
            food_dict = {f"{fid} - {fname}": fid for fid, fname in items}
            selected = st.selectbox("Select Food Item", list(food_dict.keys()))
            fid = food_dict[selected]

            new_name = st.text_input("New Food Name")
            new_qty = st.number_input("New Quantity", min_value=0, step=1)
            new_expiry = st.date_input("New Expiry Date")
            new_provider_id = st.number_input("New Provider ID", min_value=0, step=1)
            new_provider_type = st.selectbox("New Provider Type", ["", "Individual", "Restaurant", "NGO", "Organization"])
            new_location = st.text_input("New Location")
            new_food_type = st.selectbox("New Food Type", ["", "Raw", "Cooked", "Packaged"])
            new_meal_type = st.selectbox("New Meal Type", ["", "Breakfast", "Lunch", "Dinner", "Snacks"])

            update_fields = []
            values = []

            if new_name: update_fields.append("Food_Name = %s"); values.append(new_name)
            if new_qty: update_fields.append("Quantity = %s"); values.append(new_qty)
            if new_expiry: update_fields.append("Expiry_Date = %s"); values.append(new_expiry)
            if new_provider_id: update_fields.append("Provider_ID = %s"); values.append(new_provider_id)
            if new_provider_type: update_fields.append("Provider_Type = %s"); values.append(new_provider_type)
            if new_location: update_fields.append("Location = %s"); values.append(new_location)
            if new_food_type: update_fields.append("Food_Type = %s"); values.append(new_food_type)
            if new_meal_type: update_fields.append("Meal_Type = %s"); values.append(new_meal_type)

            if update_fields:
                values.append(fid)
                query = f"UPDATE Food_Listings SET {', '.join(update_fields)} WHERE Food_ID = %s;"
                cursor.execute(query, values)
                conn.commit()
                st.success("✅ Food listing updated successfully!")
            else:
                st.info("ℹ️ No changes made.")
        except Exception as e:
            conn.rollback()
            st.error(f"❌ Failed to update food listing: {e}")

     elif selected_action == "Delete":
        st.markdown("### ❌ Delete Food Listing")

        try:
        # Get all food items
         cursor.execute("SELECT Food_ID, Food_Name FROM Food_Listings ORDER BY Food_ID;")
         food_choices = cursor.fetchall()
         food_dict = {f"{fid} - {fname}": fid for fid, fname in food_choices}

         selected_food = st.selectbox("Select Food Listing to Delete", list(food_dict.keys()))
         food_id = food_dict[selected_food]

         if st.button("Delete Food Listing"):
            # Step 1: Delete related claims first
            cursor.execute("DELETE FROM Claims WHERE Food_ID = %s;", (food_id,))
            conn.commit()  # Make sure to commit here

            # Step 2: Then delete the food listing
            cursor.execute("DELETE FROM Food_Listings WHERE Food_ID = %s;", (food_id,))
            conn.commit()

            st.success("✅ Food listing and related claims deleted successfully!")

        except Exception as e:
         conn.rollback()
         st.error(f"❌ Failed to delete food listing: {e}")


# --------------------- CLAIMS CRUD ---------------------
    if selected_table == "Claims":
     if selected_action == "Add":
        st.markdown("### ➕ Add New Claim")

        food_id = st.number_input("Food ID", min_value=1, step=1)
        receiver_id = st.number_input("Receiver ID", min_value=1, step=1)
        status = st.selectbox("Status", ["Pending", "Approved", "Rejected"])

        if st.button("Add Claim"):
            try:
                cursor.execute(
                    "INSERT INTO Claims (Food_ID, Receiver_ID, Status, Timestamp) VALUES (%s, %s, %s, NOW());",
                    (food_id, receiver_id, status)
                )
                conn.commit()
                st.success("✅ Claim added successfully!")
            except Exception as e:
                conn.rollback()
                st.error(f"❌ Failed to add claim: {e}")

     elif selected_action == "Read":
        st.markdown("### 📖 View All Claims")
        try:
            cursor.execute("SELECT * FROM Claims;")
            st.dataframe(cursor.fetchall(), use_container_width=True)
        except Exception as e:
            st.error(f"❌ Failed to fetch claims: {e}")

     elif selected_action == "Update":
        st.markdown("### 🔄 Update Claim")
        try:
            cursor.execute("SELECT Claim_ID, Status FROM Claims ORDER BY Claim_ID;")
            claims = cursor.fetchall()
            claim_dict = {f"{cid} - {status}": cid for cid, status in claims}
            selected = st.selectbox("Select Claim", list(claim_dict.keys()))
            cid = claim_dict[selected]

            new_food_id = st.number_input("New Food ID", min_value=0, step=1)
            new_receiver_id = st.number_input("New Receiver ID", min_value=0, step=1)
            new_status = st.selectbox("New Status", ["", "Pending", "Approved", "Rejected"])

            update_fields = []
            values = []

            if new_food_id: update_fields.append("Food_ID = %s"); values.append(new_food_id)
            if new_receiver_id: update_fields.append("Receiver_ID = %s"); values.append(new_receiver_id)
            if new_status: update_fields.append("Status = %s"); values.append(new_status)

            if update_fields:
                values.append(cid)
                query = f"UPDATE Claims SET {', '.join(update_fields)} WHERE Claim_ID = %s;"
                cursor.execute(query, values)
                conn.commit()
                st.success("✅ Claim updated successfully!")
            else:
                st.info("ℹ️ No changes made.")
        except Exception as e:
            conn.rollback()
            st.error(f"❌ Failed to update claim: {e}")

     elif selected_action == "Delete":
        st.markdown("### ❌ Delete Claim")
        try:
            cursor.execute("SELECT Claim_ID FROM Claims ORDER BY Claim_ID;")
            claims = cursor.fetchall()
            claim_dict = {f"{cid}": cid for (cid,) in claims}
            selected = st.selectbox("Select Claim ID", list(claim_dict.keys()))
            cid = claim_dict[selected]

            if st.button("Delete Claim"):
                cursor.execute("DELETE FROM Claims WHERE Claim_ID = %s;", (cid,))
                conn.commit()
                st.success("✅ Claim deleted successfully!")
        except Exception as e:
            conn.rollback()
            st.error(f"❌ Failed to delete claim: {e}")




elif page == "My Profile":
    st.markdown("## 👩‍💼 My Profile Overview")
    

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "About Me", "Education", "Experience", "Skills", "Projects", "Certifications", "Achievements"
    ])

    with tab1:
        st.markdown("""
### 👋 Hello, I'm **Yamini S**

MCA student passionate about applying Data Science to solve real-world problems.  
Skilled in **Python**, **SQL**, **Data Analysis**, and **Streamlit**, with hands-on experience building intelligent systems for social good.

📍 Coimbatore, India  
📧 syamini1428@gmail.com  
📞 +91 8610717748  
🔗 [LinkedIn](https://www.linkedin.com/in/yamini-s-886572371/) | [GitHub](https://www.github.com)
        """)

    with tab2:
        st.markdown("""
### 🎓 Education

- **MCA – Coimbatore Institute of Technology (2024–2026)**  
  CGPA: 9.39 / 10 *(Till 2nd semester)*

- **B.Sc. in Computer Technology – KG College of Arts and Science (2021–2024)**  
  CGPA: 9.163 / 10  
  🥇 *University 3rd Rank Holder*

- **HSC – Metro Matriculation Higher Secondary School**  
  Percentage: 89%
        """)

    with tab3:
        st.markdown("""
### 💼 Professional Experience

**Technical Lead & Mentor**  
*AWS DeepRacer Community – KG College of Arts and Science*  
📆 Feb 2023 – Jun 2024

- Led projects on AI racing using AWS DeepRacer.
- Mentored juniors in Python, Data Analysis, and teamwork skills.
        """)

    with tab4:
        st.markdown("""
### 🛠️ Technical Skills

- **Python**: Data Structures, Loops, File Handling  
- **SQL**: CRUD, Joins, Query Optimization  
- **Data Analysis**: Cleaning, EDA, Visualization, Trend Analysis  
- **Streamlit**, **PostgreSQL**  
- **Soft Skills**: Communication, Team Mentoring
        """)

    with tab5:
        st.markdown("""
### 📁 Project

#### Local Food Wastage Management System  
⏳ July 2025 – Present  
📌 *Built using Python, SQL, Streamlit*  

An intelligent platform that redistributes surplus food from providers to receivers in need.  
It includes data visualization, real-time SQL insights, and dynamic dashboard components.
        """)

    with tab6:
        st.markdown("""
### 📜 Certifications

- **Core Python Course** – Level A  
- **Generative AI** – GUVI  

        """)

    with tab7:
        st.markdown("""
### 🏆 Achievements

- 🥇 **University 3rd Rank Holder** – Bharathiar University  
- 🏁 **Internal Hackathon Finalist** – Smart India Hackathon 2022 (Team Sparkers)  
- 🥇 **1st Place – Paper Presentation**, KPR Institute of Engineering & Technology  
  - Won ₹2,000 cash + ₹3,000 internship from *Emgitz Technology*
        """)

    
