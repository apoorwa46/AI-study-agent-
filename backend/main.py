from agents.planner import PlannerAgent
from agents.content_agent import ContentAgent
from agents.quiz_agent import QuizAgent
from agents.feedback_agent import FeedbackAgent
from tools.pdf_loader import read_pdf

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use FREE Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Initialize agents
planner = PlannerAgent()
content_agent = ContentAgent(model)
quiz_agent = QuizAgent(model)
feedback_agent = FeedbackAgent()

# Create study plan
plan = planner.create_plan("Study Operating Systems")

# Read PDF
pdf_text = read_pdf("data/uploads/sample.pdf")

# Generate summary
summary = content_agent.summarize(pdf_text)

# Generate quiz
quiz = quiz_agent.generate_quiz(summary)

# Output
print("\n📌 STUDY PLAN:")
for step in plan:
    print("-", step)

print("\n📘 SUMMARY:\n", summary)
print("\n📝 QUIZ:\n", quiz)
