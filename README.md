# LLM Outreach Email Practice

This project is a personal sandbox to explore how a Large Language Model (LLM)—such as ChatGPT—can generate **tailored outreach emails**. It incorporates:

1. **Website Content Scraping**: Extracting text from a company’s website to understand its focus or mission.  
2. **Resume Text Extraction**: Parsing a PDF resume to capture relevant skills and experiences.  
3. **Prompt Engineering**: Providing clear instructions to guide the LLM in crafting concise, targeted emails.

## Purpose

- **Practice Prompt Engineering**: Experiment with creating system and user prompts for an LLM.  
- **Understand LLM Use Cases**: See how an AI can leverage external data to generate context-aware communications.

## How It Works

1. **Scrape the Website**: Retrieve text from a target website.  
2. **Extract Resume Text**: Parse PDF resume data.  
3. **Build System & User Prompts**:  
   - **System Prompt**: Instructs the model on how to use the website data and resume details without directly quoting.  
   - **User Prompt**: Directs the model to craft an email that is professional, concise, and reflects the applicant’s unique background.  
4. **Generate the Email**: Use ChatGPT (or a similar LLM) to create a **150–200 word outreach message**, referencing the scraped content and resume.

## Files

- **`scraper.py`** – Functions to scrape plaintext from a website.  
- **`resume_scraper.py`** – Functions to extract text from a PDF resume.  
- **`main.py`** – Example script that puts everything together and interacts with ChatGPT.  

## Installation & Usage

### Install Dependencies  
Ensure you have **Python 3.9+** installed. Then, install required libraries:  

## Run the Project
Scrape website content using scraper.py.
Extract resume text using resume_scraper.py.
Construct prompts in main.py and generate the email.



#Note
Since this is a personal learning project, no code or output is intended for public use or distribution.
