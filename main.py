import streamlit as st
from core.engine import compute_typography_styles

st.set_page_config(
    page_title="OptiScale | Optical Accessibility",
    page_icon="👁️",
    layout="wide"
)

st.title("👁️ OptiScale: Prescriptive Visual Accessibility Engine")
st.caption("Translates refractive spectacle prescriptions (Sphere, Cylinder, Axis, Add) into real-time responsive digital typography.")

st.divider()

col_input, col_preview = st.columns([1, 1], gap="large")

with col_input:
    st.subheader("1. Spectacle Prescription (Rx)")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        sph = st.number_input("Sphere (SPH)", min_value=-15.0, max_value=+10.0, value=+1.50, step=0.25)
    with c2:
        cyl = st.number_input("Cylinder (CYL)", min_value=-8.0, max_value=0.0, value=-1.25, step=0.25)
    with c3:
        axis = st.number_input("Axis (°)", min_value=1, max_value=180, value=90, step=1)
        
    add_power = st.number_input("Near Reading Add (ADD)", min_value=0.0, max_value=+4.0, value=+2.00, step=0.25)
    
    result = compute_typography_styles(sph, cyl, axis, add_power)
    
    st.markdown("#### Clinical Optical Summary")
    st.metric("Spherical Equivalent (SE)", f"{result['spherical_equivalent']:+.2f} D")

with col_preview:
    st.subheader("2. Calibrated Eye Care Typography")
    
    theme = result["theme"]
    if theme == "ultra_high_contrast":
        bg = "#000000"
        txt = "#FFD700"
        bdr = "#FFD700"
    elif theme == "high_contrast":
        bg = "#0F172A"
        txt = "#F8FAFC"
        bdr = "#38BDF8"
    else:
        bg = "#F8FAFC"
        txt = "#0F172A"
        bdr = "#CBD5E1"

    preview_html = f""""""
st.markdown(preview_html, unsafe_allow_html=True)

st.markdown("#### Dynamic CSS Output")
st.code(
    f"font-size: {result['font_size_px']};\n"
    f"font-weight: {result['font_weight']};\n"
    f"line-height: {result['line_height']};\n"
    f"letter-spacing: {result['letter_spacing_px']};\n"
    f"theme: {result['theme']};",
    language="css"
)