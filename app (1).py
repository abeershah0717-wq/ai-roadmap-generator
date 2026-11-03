
import streamlit as st
from groq import Groq

st.title("🎓 AI Learning Roadmap Generator")

st.write("Generate your personalized AI learning roadmap!")

# User inputs
field = st.text_input("What do you want to learn?")

level = st.selectbox(
    "Select your skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

duration = st.selectbox(
    "Learning duration",
    ["1 Month", "3 Months", "6 Months", "1 Year"]
)

hours = st.selectbox(
    "Daily study hours",
    ["1 Hour", "2 Hours", "3 Hours", "4 Hours"]
)

# Generate roadmap
if st.button("Generate Roadmap"):

    if field.strip() == "":
        st.warning("Please enter your learning field!")

    else:
        try:
            client = Groq(
                api_key=st.secrets["GROQ_API_KEY"]
            )

            prompt = f"""
            Create a simple and detailed learning roadmap.

            Field: {field}
            Skill Level: {level}
            Duration: {duration}
            Daily Study Time: {hours}

            Include:
            1. Topics to learn
            2. Weekly learning plan
            3. Practical exercises
            4. Projects
            5. Learning resources
            6. Final project

            Explain everything in simple language.
            """

            with st.spinner("Generating your roadmap..."):

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                roadmap = response.choices[0].message.content

            st.success("Your roadmap is ready!")
            st.markdown(roadmap)

            st.download_button(
                "Download Roadmap",
                roadmap,
                file_name="learning_roadmap.md"
            )

        except Exception as e:
            st.error(f"Error: {e}")
