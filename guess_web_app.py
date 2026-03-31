import streamlit as st

st.set_page_config(page_title="GlowCare | Skincare Website", page_icon="✨", layout="wide")

st.markdown(
    """
    <style>
    .hero {
        background: linear-gradient(135deg, #ffe8f1 0%, #f5fbff 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1rem;
    }
    .card {
        background: #ffffff;
        border: 1px solid #f0e5ec;
        border-radius: 16px;
        padding: 1rem;
        height: 100%;
    }
    .muted {
        color: #6f6f6f;
        font-size: 0.95rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class='hero'>
        <h1>✨ GlowCare Skincare Studio</h1>
        <p class='muted'>Healthy skin starts with a simple routine and products matched to your skin type.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

menu = st.radio(
    "Go to section:",
    ["Home", "Products", "Skin Routine Builder", "Testimonials", "Contact"],
    horizontal=True,
)

if menu == "Home":
    st.subheader("Welcome to your skincare destination")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🌿 Clean Ingredients")
        st.write("Dermatologist-reviewed formulas with no harsh fragrance.")
    with col2:
        st.markdown("### 💧 Hydration First")
        st.write("Barrier-supporting products for dry, combination, and oily skin.")
    with col3:
        st.markdown("### ☀️ Daily SPF")
        st.write("Lightweight sun protection for everyday use.")

    st.info("Tip: Use the **Skin Routine Builder** tab to get a personalized routine setup.")

elif menu == "Products":
    st.subheader("Featured Product Line")
    products = [
        {
            "name": "Gentle Gel Cleanser",
            "for": "All skin types",
            "price": "$18",
            "details": "Removes dirt and sunscreen without stripping moisture.",
        },
        {
            "name": "Vitamin C Glow Serum",
            "for": "Dull skin",
            "price": "$29",
            "details": "Brightens tone and helps fade dark spots over time.",
        },
        {
            "name": "Ceramide Repair Cream",
            "for": "Dry / sensitive",
            "price": "$26",
            "details": "Strengthens skin barrier and locks in hydration.",
        },
        {
            "name": "Daily SPF 50 Fluid",
            "for": "All skin types",
            "price": "$22",
            "details": "No white cast, lightweight, and makeup-friendly.",
        },
    ]

    cols = st.columns(2)
    for idx, product in enumerate(products):
        with cols[idx % 2]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown(f"#### {product['name']}")
            st.write(f"**Best for:** {product['for']}")
            st.write(f"**Price:** {product['price']}")
            st.write(product["details"])
            st.button(f"Add {product['name']} to cart", key=f"add_{idx}")
            st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Skin Routine Builder":
    st.subheader("Build your full skincare setup")
    st.write("Tell us your skin profile and we will suggest a complete daily routine.")

    skin_type = st.selectbox("Your skin type", ["Dry", "Oily", "Combination", "Sensitive", "Normal"])
    concern = st.multiselect(
        "Main skin concerns",
        ["Acne", "Dark spots", "Redness", "Dryness", "Fine lines", "Uneven texture"],
    )
    experience = st.radio("Skincare experience", ["Beginner", "Intermediate", "Advanced"], horizontal=True)

    if st.button("Generate Routine"):
        st.success("Your personalized routine is ready!")

        st.markdown("### 🌞 Morning")
        st.write("1. Gentle Gel Cleanser")
        st.write("2. Vitamin C Glow Serum")
        st.write("3. Ceramide Repair Cream")
        st.write("4. Daily SPF 50 Fluid")

        st.markdown("### 🌙 Night")
        st.write("1. Gentle Gel Cleanser")
        if "Acne" in concern:
            st.write("2. Salicylic BHA Treatment (2-3 nights/week)")
        else:
            st.write("2. Hydrating Serum")
        st.write("3. Ceramide Repair Cream")

        if experience == "Advanced":
            st.info("Advanced option: Add a retinol serum 2 nights per week.")

        st.caption(f"Suggested routine for **{skin_type} skin** with concerns: {', '.join(concern) if concern else 'General maintenance'}.")

elif menu == "Testimonials":
    st.subheader("Client Results")
    st.markdown("- ⭐⭐⭐⭐⭐ *'My skin texture improved in 4 weeks!'* — Mia")
    st.markdown("- ⭐⭐⭐⭐⭐ *'Simple routine, big glow difference.'* — Daniel")
    st.markdown("- ⭐⭐⭐⭐⭐ *'Finally found SPF that doesn't feel greasy.'* — Priya")

else:
    st.subheader("Contact & Setup")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        goal = st.text_area("What do you want help with?")
        submitted = st.form_submit_button("Submit Setup Request")

    if submitted:
        if name and email:
            st.success(f"Thanks {name}! Our skincare team will contact you at {email}.")
        else:
            st.error("Please enter at least your name and email.")

st.write("---")
st.write("👨‍💻 Demo skincare website built with Streamlit")
