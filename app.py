import cohere
import streamlit as st

# --- Setup ---
st.set_page_config(page_title="AI Social Post Optimizer", page_icon="🤖")
st.title("🤖 AI-Powered Social Media Post Optimizer")
st.write("Get short, optimized captions based on your input content.")

# --- API Key ---
co = cohere.Client(st.secrets["COHERE_API_KEY"])

# --- User Input ---
user_input = st.text_area("Enter your content idea, product, or post:", height=150)

tone = st.selectbox("Choose tone:", ["Witty", "Inspirational", "Professional", "Funny", "Minimal"])
goal = st.radio("Goal:", ["Increase engagement", "Drive clicks", "Build trust", "Go viral"])

if st.button("Generate Caption"):
    with st.spinner("Thinking..."):

        prompt = f"""
You are a social media expert.

Generate 1 short, catchy, and optimized caption (under 30 words) for this content idea:
\"\"\"{user_input}\"\"\"

Tone: {tone}
Goal: {goal}
Platform: Instagram
Style: Hook + CTA (if appropriate)
Avoid hashtags.
        """

        try:
            response = co.chat(
                model="command-r",
                message=prompt,
                temperature=0.7
            )
            caption = response.text.strip()
            st.subheader("📢 Optimized Caption")
            st.success(caption)

        except Exception as e:
            st.error(f"❌ Error: {e}")
