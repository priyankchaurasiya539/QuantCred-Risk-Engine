import streamlit as st
import joblib
import numpy as np

# 1. Global Page Configuration
st.set_page_config(
    page_title="QuantCred Risk Engine", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# Premium Global Custom UI Glassmorphism Styling
st.markdown("""
<style>
    .stNumberInput, .stTextInput {
        background-color: rgba(255, 255, 255, 0.02) !important;
        padding: 10px !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #4A00E0, #8E2DE2) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# 2. Secure Math Model Artifacts Loading Layer
@st.cache_resource
def load_saved_artifacts():
    sca_reg = joblib.load("models/scaler_reg.pkl")
    sca_clf = joblib.load("models/scaler_clf.pkl")
    model_reg = joblib.load("models/ridge_model.pkl")
    model_clf = joblib.load("models/logistic_model.pkl")
    return sca_reg, sca_clf, model_reg, model_clf

try:
    sca_reg, sca_clf, model_reg, model_clf = load_saved_artifacts()
except Exception as e:
    st.error(f"❌ Checkpoint Error: Run model_training.py first to generate .pkl files inside 'models/' directory. Context: {e}")
    st.stop()

# 3. Dynamic Session State Routing Control
if "page" not in st.session_state:
    st.session_state.page = "form"

if st.session_state.page == "form":
    st.title("💳 QuantCred: Intelligent Credit Risk Engine")
    st.write("Enter applicant credentials below to trigger dual-engine predictive underwriting.")
    st.markdown("---")
    
    # Block A: Personal Demographics Matrix (Attractive Additions)
    st.subheader("👤 Personal Credentials")
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        user_name = st.text_input("Full Name" , value="" , key="Name")
    with c2:
        user_age = st.number_input("Age", min_value=18, max_value=100 , key = "Age")
    with c3:
        pincode = st.text_input("Pincode", max_chars=6 , key="Pin")
        
    c4, c5 = st.columns(2)
    with c4:
        city = st.text_input("City" , key="City")
    with c5:
        state = st.text_input("State" , key="State")
        
    st.markdown("---")
    
    # Block B: Tight 2-Column Grid for Core Predictive Operational Features
    st.subheader("📊 Operational & Bureau Risk Metrics")
    col1, col2 = st.columns(2)
    with col1:
        Monthly_App_Orders = st.number_input("Monthly Orders", min_value=2, max_value=50, value=2)
        Average_Order_Value = st.number_input("Average Order Value", min_value=150.0, max_value=2000.0, value=200.0)
        Account_Age_Months = st.number_input("Customer Vintage (Months)", min_value=1, max_value=60, value=10)
    with col2:
        Delayed_Payments_Count = st.number_input("Delayed Payments Count", min_value=0, max_value=10, value=0)
        CIBIL_score = st.number_input("Bureau CIBIL Score", min_value=300, max_value=900, value=300)
        Monthly_Income_Lakhs = st.number_input("Monthly Income (In Lakhs)", min_value=0.3, max_value=5.0, value=1.0)

    st.markdown("---")
    
    # Block C: Mathematical Core Execution Inside Button Click
    if st.button("Evaluate Credit Risk & Generate Report"):
        # Transient state logging mapping
        st.session_state.user_name = user_name
        st.session_state.user_age = user_age
        st.session_state.pincode = pincode
        st.session_state.city = city
        st.session_state.state = state
        
        # Array creation keeping the exact index order expected by trained sklearn weights
        features = np.array([[
            Monthly_App_Orders,
            Average_Order_Value,
            Account_Age_Months,
            Delayed_Payments_Count,
            CIBIL_score,
            Monthly_Income_Lakhs
        ]])
        
        # Core Engine 1: Execution Level (Risk Triage)
        scaled_clf = sca_clf.transform(features)
        risk_state = model_clf.predict(scaled_clf)[0]
        st.session_state.risk_state = risk_state
        
        # Core Engine 2: Execution Level (Dynamic Allocation Pricing)
        if risk_state == 0:
            scaled_reg = sca_reg.transform(features)
            raw_limit = model_reg.predict(scaled_reg)[0]
            st.session_state.final_limit = max(0.0, round(raw_limit, 2))
        else:
            st.session_state.final_limit = 0.0
            
        # UI State Shift & Rerun Trigger
        st.session_state.page = "report"
        st.rerun()


elif st.session_state.page == "report":
    st.title("📊 Official Credit Underwriting Report")
    st.markdown("---")
    
    # 1. Complete Demographic Printing Dashboard Panel
    st.subheader("📋 Customer Personal Dossier Summary")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write(f"👤 **Applicant Name:** {st.session_state.user_name}")
        st.write(f"⏳ **Applicant Age:** {st.session_state.user_age} Years")
        st.write(f"📍 **Target Area Pincode:** {st.session_state.pincode}")
    with col_b:
        st.write(f"🌆 **Registered City:** {st.session_state.city}")
        st.write(f"🗺️ **Registered State:** {st.session_state.state}")
        
    st.markdown("---")
    st.subheader("🛡️ Algorithmic Policy Boundary Evaluation")
    
    # 2. Centered High Impact CSS Gradients Rendering
    if st.session_state.risk_state == 1:
        critical_card = """
        <div style="
            background: linear-gradient(135deg, #FF416C, #FF4B2B); 
            padding: 30px; 
            border-radius: 12px; 
            color: white; 
            text-align: center;
            box-shadow: 0 10px 20px rgba(255,65,108,0.25);
            font-family: sans-serif;
        ">
            <h3 style="margin: 0; font-size: 14px; letter-spacing: 2px; opacity: 0.9;">APPLICATION STATUS: REJECTED</h3>
            <h1 style="margin: 15px 0 5px 0; font-size: 45px; font-weight: 800;">₹0.00</h1>
            <p style="margin: 0; font-size: 14px; opacity: 0.75;">High Default Probability Signature Detected. Policy Blocked.</p>
        </div>
        """
        st.markdown(critical_card, unsafe_allow_html=True)
    else:
        approved_card = f"""
        <div style="
            background: linear-gradient(135deg, #00B4DB, #0083B0); 
            padding: 35px; 
            border-radius: 12px; 
            color: white; 
            text-align: center;
            box-shadow: 0 10px 20px rgba(0,180,219,0.25);
            font-family: sans-serif;
        ">
            <h3 style="margin: 0; font-size: 14px; letter-spacing: 2px; opacity: 0.9;">APPLICATION STATUS: APPROVED</h3>
            <h1 style="margin: 15px 0 5px 0; font-size: 45px; font-weight: 800;">₹{st.session_state.final_limit:,.2f}</h1>
            <p style="margin: 0; font-size: 14px; opacity: 0.75;">Dynamic Line of Credit Provisioned Safely.</p>
        </div>
        """
        st.markdown(approved_card, unsafe_allow_html=True)

        
        
    st.markdown("---")
    

    # 3. Dynamic Router Reset State Backtrack Trigger
    if st.button("⬅️ Process New Applicant Entry"):
        st.session_state.page = "form"
        st.rerun()