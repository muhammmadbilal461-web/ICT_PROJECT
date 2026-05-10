import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- HEADER SECTION ---
st.title("🛠️ Mechanical Unit & Density Hub")
st.subheader("Developed by: Muhammad Bilal")
st.info("📌 Roll Number: 25-ME-124")

st.divider()

# --- SIDEBAR NAVIGATION ---
option = st.sidebar.selectbox(
    "Choose a Functionality",
    ("Unit Converter", "Material Density Checker")
)

# --- UNIT CONVERTER LOGIC ---
if option == "Unit Converter":
    st.header("🔄 Unit Converter")
    
    category = st.selectbox("Select Category", ["Pressure", "Power", "Force"])
    value = st.number_input("Enter Value", value=1.0)

    if category == "Pressure":
        # Bar to Pascal
        result = value * 100000
        st.success(f"{value} Bar = {result:,} Pascals (Pa)")
        
    elif category == "Power":
        # Horsepower to Watts
        result = value * 745.7
        st.success(f"{value} HP = {result:.2f} Watts (W)")
        
    elif category == "Force":
        # Newton to Pound-force
        result = value * 0.224809
        st.success(f"{value} Newtons = {result:.4f} lbf")

# --- DENSITY CHECKER LOGIC ---
elif option == "Material Density Checker":
    st.header("⚖️ Material Density Checker")
    st.write("Find the density of common engineering materials.")
    
    # Density data in kg/m^3
    densities = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Titanium": 4506,
        "Concrete": 2400,
        "Water": 1000
    }
    
    material = st.selectbox("Select Material", list(densities.keys()))
    
    if material:
        density_val = densities[material]
        st.metric(label=f"Density of {material}", value=f"{density_val} kg/m³")
        
        # Simple mass calculator
        st.write(f"---")
        st.write(f"**Quick Mass Calculator for {material}:**")
        volume = st.number_input("Enter Volume (m³)", min_value=0.0, value=1.0)
        mass = volume * density_val
        st.write(f"The total mass would be: **{mass:,} kg**")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("University Project - Mechanical Engineering")
