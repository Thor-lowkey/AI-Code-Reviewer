import streamlit as st
import requests

st.set_page_config(
    page_title="Code Review AI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.title("🛠️ Code Review AI")
st.caption("Automated structural analysis and senior-level optimization reports for engineering teams.")
st.markdown("---")

col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.subheader("Source Input")
    language = st.selectbox(
        "Programming Language", 
        ["Python", "C++", "Java", "JavaScript"]
    )
    user_code = st.text_area(
        "Paste Source Code", 
        height=450, 
        placeholder="Enter your source code configuration here...",
        key="code_input"
    )
    submit_button = st.button("Execute Code Review", use_container_width=True, type="primary")

with col2:
    st.subheader("Analysis & Metrics")
    
    if submit_button:
        if not user_code.strip():
            st.warning("Please provide a valid code snippet to analyze.")
        else:
            with st.spinner("Compiling structural analysis report..."):
                try:
                    payload = {"code": user_code}
                    # Sending request to FastAPI backend
                    response = requests.post("http://127.0.0.1:8000/review", json=payload)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.success("Analysis Complete")
                        st.markdown(f"## {language} Quality Report")
                        st.markdown("---")
                        # Using st.markdown to cleanly render bullet points and code blocks from Gemini
                        st.markdown(result["review"])
                    else:
                        st.error(f"Execution Error: Server returned status code {response.status_code}")
                        
                except Exception as e:
                    st.error("Unable to establish connection to the backend server architecture.")
    else:
        st.info("Submit your source code in the left panel to generate the engineering metrics.")