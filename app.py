#  ========================================================
# Project : AI Interview Preparation System
# Technologies : Python, Streamlit, Machine Learning
# Copyright : Study Trigger
# =========================================================

import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import random 
import json

st.set_page_config(page_title="AI Interview Preparation System", layout="wide")

#read question.json file

with open("questions.json","r") as file:
    questions_bank=json.load(file)

    st.sidebar.title("AI Interview Preparation")
    menu = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "Student Profile",
            "Skill Assessment",
            "Dashboard",
            "AI Roadmap",
            "Interview Question",
            "Progress Tracker",
        ]
    )

    if 'scores'not in st.session_state:
        st.session_state.scores={}

        if 'student_name'not in st.session_state:
            st.session_state.student_name=""

            if 'role'not in st.session_state:
                st.session_state.role=""

                menu = st.sidebar.selectbox(
                    "Navigation",
                    ["Home","Practice","Progress Tracker"]
                )

            if menu =="Home":

                st.title("AI Interview Preparation System")        
            st.markdown("""
### Crack Technical Interviews with AI-Powered Analysis

Analyze your coding skills, detect weak areas,
generate interview questions, and build a smart roadmap.
""")

    col1, col2, col3 = st.columns(3)

    col1.metric("Students Practicing", "100+")
    col2.metric("Questions Available", "500+")
    col3.metric("Success Rate", "87%")

    st.divider()

    st.subheader("🎯 What This System Can Do")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📊 Skill Assessment")
        st.info("⚠️ Weak Topic Detection")
        st.info("🛣️ AI Learning Roadmap")

    with col2:
        st.info("💡 Interview Questions")
        st.info("📈 Progress Tracking")
        st.info("🤖 AI Readiness Prediction")

    st.divider()

    st.success("Start your preparation journey today")

    if menu=="Home":
        st.title("Home")

    elif menu =="Student Profile":
        st.title("Student Profile")
    name = st.text_input("Enter your name")

    role = st.selectbox(
        "Preferred Role",
        [
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Analyst",
            "ML Engineer"
        ]
    )

    branch = st.selectbox(
        "Branch",
        ["BCA", "BTech", "MCA", "BSc(IT)", "MSc(IT)"]
    )

    year = st.selectbox(
        "Year",
        ["1st Year", "2nd Year", "3rd Year", "Final Year"]
    )

    if st.button("Save Profile"):
        st.session_state.student_name = name
        st.session_state.role = role

        st.success("Profile Saved Successfully!")

    elif menu == "Skill Assessment":
        st.title("🧠 Skill Assessment")

    st.markdown("Rate yourself out of 100")

    arrays = st.slider("Arrays", 0, 100, 50)
    linked_list = st.slider("Linked List", 0, 100, 50)
    stack = st.slider("Stack", 0, 100, 50)
    queue = st.slider("Queue", 0, 100, 50)
    dbms = st.slider("DBMS", 0, 100, 50)
    os = st.slider("Operating System", 0, 100, 50)

    if st.button("Analyze Skills"):

        st.session_state.scores = {
            "Arrays": arrays,
            "Linked List": linked_list,
            "Stack": stack,
            "Queue": queue,
            "DBMS": dbms,
            "OS": os
        }

        st.success("Skill Analysis Completed")

    elif menu == "Dashboard":
        st.title("Dashboard Analytics")

    if not st.session_state.scores:
        st.warning("Please complete Skill Assesment first")
    else:
        scores = st.session_state.scores

        df = pd.DataFrame({
            "Topic": list(scores.keys()),
            "Score": list(scores.values())
        })

        col1, col2, col3 = st.columns(3)

        avg_score = sum(scores.values()) / len(scores)

        weak_topics = [k for k, v in scores.items() if v < 50]
        strong_topics = [k for k, v in scores.items() if v >= 75]

        col1.metric("Average Score", f"{avg_score:.2f}%")
        col2.metric("Weak Topics", len(weak_topics))
        col3.metric("Strong Topics", len(strong_topics))

        st.subheader("Topic Performance")

        fig, ax = plt.subplots(figsize=(5, 2.5))
        ax.bar(df['Topic'], df['Score'])
        plt.xticks(rotation = 20)
        st.pyplot(fig)

        st.subheader(" weak Topic Dectectiom")
        
        if weak_topics:
            for topic in weak_topics:
                st.error(f"Weak Topic:{topic}")
            else:
                st.success("No weak topics detected")

                st.subheader("Strong Topics")

                if strong_topics:
                    for topic in strong_topics :
                        st.success(f"Strong Topic: {topic}")


        elif menu == "AI Roadmap": 
            st.title("AI Learning Roadmap")

    if not st.session_state.scores:
        st.warning("Please complete Skill Assessment first")

    else:
        scores = st.session_state.scores

        weak_topics = [k for k, v in scores.items() if v < 50]

        if not weak_topics:
            st.success(
                "Excellent Performance! Keep practicing advanced problems."
            )

        else:
            for topic in weak_topics:

                st.subheader(f"📚 {topic} Roadmap")

                if topic == "Arrays":
                    st.write("Week 1 :- Array Basics")
                    st.write("Week 2 :- Sliding Window")
                    st.write("Week 3 :- Prefix Sum")
                    st.write("Week 4 :- LeetCode Problems")


                elif topic == "Linked List":
                    st.write("Week 1 :- Linked List Basics")
                    st.write("Week 2 :- Reverse Linked List")
                    st.write("Week 3 :- Fast & Slow Pointer")
                    st.write("Week 4 :- Interview Problems")


                elif topic == "Stack":
                    st.write("Week 1 :- Stack Basics")
                    st.write("Week 2 :- Monotonic Stack")
                    st.write("Week 3 :- Expression Evaluation")
                    st.write("Week 4 :- Advanced Problems")


                elif topic == "Queue":
                    st.write("Week 1 :- Queue Basics")
                    st.write("Week 2 :- Circular Queue")
                    st.write("Week 3 :- Priority Queue")
                    st.write("Week 4 :- Graph Applications")


                elif topic == "DBMS":
                    st.write("Week 1 :- SQL Basics")
                    st.write("Week 2 :- Joins")
                    st.write("Week 3 :- Normalization")
                    st.write("Week 4 :- Transactions & Indexing")


                elif topic == "OS":
                    st.write("Week 1 :- Process & Thread")
                    st.write("Week 2 :- Scheduling")
                    st.write("Week 3 :- Deadlock")
                    st.write("Week 3 :- Memory Management")

                elif menu == "Interview Questions":

                    st.title("Interview Question Generator")

    topic = st.selectbox(
        "Select Topic",
        list(questions_bank.keys())
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("Generate Questions"):

        questions = random.sample(
            questions_bank[topic],
            min(16, len(questions_bank[topic]))
        )

        st.subheader(f"{difficulty} Level Questions")

        for i, q in enumerate(questions, start=1):
            st.write(f"{i}. {q}")

    elif menu == "Progress Tracker":

        st.title(" Progress Tracker")

    if not st.session_state.scores:
        st.warning("Please complete Skill Assessment first")

    else:
        scores = st.session_state.scores
        progress_df = pd.DataFrame({
            'Topic': list(scores.keys()),
            'Current Score': list(scores.values()),
            'Target Score': [100] * len(scores)
        })

        st.dataframe(progress_df)

        st.subheader("Interview Readiness")
        avg_score = sum(scores.values()) / len(scores)

        X = [ [20], [35], [45], [55], [65], [75], [85], [95]]
        y = ['Low','Low','Medium','Medium','Good', 'Good','Excellent','Excellent' ]

        model = DecisionTreeClassifier()
        model.fit(X, y)
        prediction = model.predict([[avg_score]])

        st.success(f"Interview Readiness Level: {prediction[0]}")

        if prediction[0] == 'Low':
            st.error("You need strong preparation before placements")

        elif prediction[0] == 'Medium':
            st.warning("You are improving but still need practice")

        elif prediction[0] == 'Good':
            st.info("Good preparation level. Keep practicing")
        else:
            st.success("Excellent preparation level")
