# Research Paper Classifier Using OpenAI API

## Overview
This tool helps researchers and educators automatically process, analyze, and categorize research papers using OpenAI's powerful AI models. While the current example focuses on wheat-related papers, you can easily adapt it for any research field by modifying the classification categories.

## Why Use This Tool?
- Save time by automating paper classification
- Create organized course databases
- Get AI-generated summaries of research papers
- Easily categorize large volumes of academic papers
- Perfect for departments and research groups managing many papers

## Prerequisites

### 1. Python Installation
1. Download Python from [python.org](https://python.org)
   - Choose version 3.8 or newer
   - During installation on Windows, check "Add Python to PATH"
   - For Mac/Linux users, Python is usually pre-installed

### 2. OpenAI API Key
1. Create an account at [OpenAI's website](https://openai.com)
2. Navigate to API section
3. Generate an API key
4. Store it safely - never share this key publicly

### 3. Required Python Packages
Open your terminal/command prompt and run:
```bash
pip install openai python-dotenv PyPDF2 tiktoken
```

## Project Structure
```
your-project/
│
├── papers/
│   ├── pdfs/         # Place your PDF papers here
│   ├── txts/         # Converted text files go here
│   ├── api_results/  # Classification results appear here
│   └── token_counts.txt
│
├── process_pdfs.py
├── token_counter.py
├── api_call.py
└── .env              # Store your API key here
```

## Step-by-Step Setup Guide

### 1. Setting Up Your Environment
1. Create a new folder for your project
2. Create a file named `.env` in this folder
3. Add your API key to the `.env` file:
```
OPENAI_API_KEY=your-api-key-goes-here
```

### 2. Organizing Your Papers
1. Create a folder named `papers`
2. Inside `papers`, create three subfolders:
   - `pdfs` (put your PDF papers here)
   - `txts` (converted text will go here)
   - `api_results` (classification results will appear here)

### 3. Customizing the Categories
In `api_call.py`, find and modify the classification categories:
```python
"""
Classify the following research paper into one of these classes:
1. category_one
2. category_two
3. category_three
# Add or modify categories as needed
"""
```

## Using the Tool

### Step 1: Convert PDFs to Text
```bash
python process_pdfs.py
```

This step:
- Reads all PDFs from `papers/pdfs`
- Converts them to text
- Saves them in `papers/txts`

### Step 2: Count Tokens
```bash
python token_counter.py
```

This step:
- Counts tokens in each text file
- Ensures papers fit within API limits
- Creates `token_counts.txt`

### Step 3: Classify Papers
```bash
python api_call.py
```

This step:
- Processes each text file
- Sends content to OpenAI API
- Saves results in `papers/api_results`

## Understanding the Results

### Result Format
Each result file contains:

#### Class
The category assigned to the paper

#### Summary
A one-paragraph summary of the paper's main goals and methods

### Example Result
```
Class: machine_learning_applications

Summary: This paper presents a novel approach to using deep learning 
for analyzing research data. The study implements a neural network 
architecture that achieves 95% accuracy in classification tasks...
```

## Customization Tips

### Modifying Categories
In `api_call.py`, update the classification prompt:
```python
"""
Classify the following research paper into one of these classes:
1. your_category_1
2. your_category_2
3. your_category_3
"""
```

### Adjusting Summary Style
Modify the prompt to focus on:
- Technical details
- Methodology
- Results
- Field-specific aspects

## Troubleshooting

### Common Issues and Solutions

#### ModuleNotFoundError
```bash
pip install [missing-module-name]
```

#### API Key Error
- Check `.env` file location
- Verify API key correctness
- Confirm API key is active

#### PDF Processing Errors
- Ensure PDFs aren't password-protected
- Verify PDF readability
- Try manual text conversion for problematic files

#### Token Limit Exceeded
- Normal for long papers
- Automatic truncation occurs
- Focus on key sections if needed

## Cost Considerations

### OpenAI API Pricing
- Charges based on token usage
- Monitor usage in OpenAI dashboard
- Approximate cost: $0.01-0.02 per paper

### Cost Optimization
- Process papers in batches
- Monitor token usage
- Use smaller models when possible

## Contributions

### Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## Version History
- v1.0.0 - Initial release

## Acknowledgments
- OpenAI for API access
