import streamlit as st

import random
from io import BytesIO
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="AI Lesson Plan Architect")

st.title("📚 AI Lesson Plan Architect")

subject = st.text_input("Enter Subject")

grade = st.selectbox(
    "Select Grade",
    ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5",
     "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10"]
)

topic = st.text_input("Enter Topic")

time_limit = st.selectbox(
    "Select Lesson Time Limit",
    ["30 Minutes", "40 Minutes", "60 Minutes"]
)

board = st.selectbox(
    "Select Syllabus Board",
    ["CBSE", "ICSE", "State Board"]
)

level = st.selectbox(
    "Select Information Level",
    ["Basic", "Intermediate", "Advanced"]
)

def mock_lesson_plan(subject, grade, topic):
    return f"""
Lesson Plan

Subject: {subject}
Grade: {grade}
Topic: {topic}

Time Limit: {time_limit}
Board: {board}
Information Level: {level}

Learning Objectives:
- Understand {topic} concepts

Teaching Content:
- Explain {topic} in structured classroom format.

Activity:
- Classroom discussion and practice.

Assessment:
- Short quiz questions.

Homework:
- Write 5 important points about {topic}.
"""

def create_pdf(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
        story.append(Spacer(1, 12))

    doc.build(story)

    buffer.seek(0)
    return buffer

if st.button("Generate Lesson Plan"):
    if subject and topic:
        plan = mock_lesson_plan(subject, grade, topic)

        st.subheader("Generated Lesson Plan")
        st.write(plan)

        pdf_buffer = create_pdf(plan)

        st.download_button(
            label="📄 Download Lesson Plan as PDF",
            data=pdf_buffer,
            file_name="lesson_plan.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Please fill subject and topic.")