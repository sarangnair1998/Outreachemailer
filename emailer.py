from openai import OpenAI
from dotenv import load_dotenv
import os
from scraper import get_plaintext_content
from resume_scraper import extract_text_from_pdf

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')


openai = OpenAI()


url = input("Enter the URL of the website you want to analyze: ")
content = get_plaintext_content(url)

home_dir = os.path.expanduser("~")  
pdf_path = os.path.join(home_dir, "Documents", "Resume for work", "Robotics Resume 2025.pdf")

resume_text = extract_text_from_pdf(pdf_path)


system_prompt = """
You are ChatGPT, an AI specialized in crafting concise, compelling,human-like outreach emails (150–200 words). You have access to:

- Company website content (scraped data), which provides insights into the company’s products, mission, and focus areas.
- The applicant’s resume (scraped from their PDF), detailing their expertise in robotics, automation, AI-driven systems, leadership, and technical project execution.

When generating an email, you must:

1. **Contextually Align with the Company (Without Directly Copying Website Text)**
   - Extract key ideas from the company website without directly reusing its phrasing.
   - Instead of quoting descriptions verbatim, rephrase and synthesize the company’s focus, emphasizing how it connects with the applicant’s skills and interests.

2. **Showcase the Applicant’s Strengths**
   - Highlight relevant expertise (robotics, AI, automation, leadership, product execution).
   - Connect these capabilities to the company’s industry challenges, goals, or product offerings.

3. **Maintain a Professional Yet Personable Tone**
   - Ensure the email is respectful, direct, and warm.
   - Avoid being too casual while keeping the message engaging and inviting.

4. **Be Action-Oriented**
   - Clearly propose a next step: internship, short-term project, or discussion.
   - End with an open invitation for follow-up.

5. **Stay Within 150–200 Words**
   - Ensure every email adheres strictly to this limit, keeping the message concise yet impactful.

Always ensure your output remains focused on the applicant’s fit, avoids direct wording from the company website, and encourages further conversation.
"""

user_prompt = f"""
Write a concise, 150–200 word outreach email to [Recipient Name] at [Company Name].
Use this information from the website:\n{content}\n
And these highlights from my resume:\n{resume_text}\n

Avoid reusing exact phrases from the website content (please paraphrase).
Maintain a personable(human-like) tone,avoid grandiose emotions or buzzwords,make it casual and impactful,propose next steps (e.g., internship,full-time role), 
and end by inviting further discussion. 
Remember to include my LinkedIn link (https://www.linkedin.com/in/sarangsnair/) and my resume attached.
"""

def messages_for():
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

response = openai.chat.completions.create(
        model = "gpt-4o",
        messages = messages_for()
    )

print(response.choices[0].message.content)