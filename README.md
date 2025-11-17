🤖 AI Assignment 1B: Large Language Model Implementation & Analysis

📌 Project Overview

This repository contains the solution for AI Assignment 1B, focusing on practical, hands-on experience with a modern Large Language Model (LLM).

The objective of this project is to set up a development environment, implement a Python script to load and interact with a quantized open-weight model (specifically Google's Gemma-2B-it), and rigorously test its capabilities and limitations through qualitative analysis and unit testing.

Key Learning Outcomes:

Model Quantization and Efficient Inference (using bitsandbytes).

Hugging Face transformers library usage.

Prompt Engineering and chat templating.

Challenges of LLM deployment on consumer hardware.

🛠️ I. Setup and Installation Guide

Follow these steps to create a reproducible Python environment and install all necessary dependencies.

1. Prerequisites

Python: Version 3.8 or higher.

Tools: Git and a code editor (VS Code recommended).

Hardware: An NVIDIA GPU with at least 8GB VRAM is highly recommended for acceptable inference speed.

2. Get the Starter Code

Assuming you have already created your public repository (llm-project-[YourName]) from the provided template:

# Clone your repository (REPLACE WITH YOUR URL)
git clone [https://github.com/](https://github.com/)[YourUsername]/llm-project-[YourName].git

# Navigate into the project directory
cd llm-project-[YourName]


3. Setup the Python Virtual Environment (venv)

It is crucial to isolate project dependencies using a virtual environment.

# Create a virtual environment named 'venv'
python -m venv venv


Activate the environment:

Operating System

Command

Windows

venv\Scripts\activate

macOS/Linux

source venv/bin/activate

💡 Your terminal prompt should now show (venv).

4. Install Dependencies

Install all required libraries using the provided requirements.txt file.

# Upgrade pip first (optional)
pip install --upgrade pip

# Install the core libraries
pip install -r requirements.txt


5. Hugging Face Authentication

The google/gemma-2b-it model requires that you accept its license agreement and authenticate via a user token.

Create a free account on huggingface.co.

Visit the Gemma-2B-it model card and accept the license agreement.

Generate a new User Access Token with "read" privileges in your Hugging Face settings.

Run the following command in your activated terminal and paste your token when prompted:

huggingface-cli login


💻 II. Project Structure and Execution

Directory Structure

The project follows this required structure:

llm-project-[YourName]/
├── src/
│   └── model.py             # Your main implementation (load_model, get_response)
├── tests/
│   └── test_model.py          # Unit tests for core functions
├── demo.py                  # Simple script to run and test the model live
├── requirements.txt         # Dependency list
├── RESULTS.md               # Document for qualitative analysis and test results
└── README.md                # This file


Running the Model

1. Implementation: Complete the load_model() and get_response() functions in src/model.py.

2. Demo Interaction: Run demo.py from the root directory to test the model conversationally:

python demo.py


3. Unit Testing: Run your implemented unit tests to verify functionality:

python -m unittest discover tests


📹 III. Video Submission (Mandatory)

Per the assignment, three screen-recorded videos are mandatory. Please replace the placeholders below with the links to your uploaded videos.

Video File Name (Format)

Content Requirement

Link to Video

[Student Number]_[Project Title]_1-installation.mp4

Show cloning the repository, creating/activating venv, running pip install -r requirements.txt, and successful huggingface-cli login.

[INSERT VIDEO 1 LINK HERE]

[Student Number]_[Project Title]_2-implementation.mp4

Walk through the code in src/model.py. Run demo.py and interact with the model live (ask one factual, one creative, and one coding question).

[INSERT VIDEO 2 LINK HERE]

[Student Number]_[Project Title]_3-testing.mp4

Run unit tests (python -m unittest discover tests) and show they pass. Open RESULTS.md and demonstrate the live model output for each of the five qualitative analysis points.

[INSERT VIDEO 3 LINK HERE]

📤 IV. Submission Checklist

Before the due date, ensure the following items are present in your public GitHub repository:

Source Code: All Python files (.py files, including src/, tests/, and demo.py).

README.md: This detailed setup instruction file.

RESULTS.md: Completed qualitative analysis.

requirements.txt: Allows for a one-command install of dependencies.

VIDEOS: Links to the three required videos (in .mp4 format) posted clearly above in Section III.
