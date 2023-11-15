# API KEY: 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

import openai
import json
from format import output_2_pdf

openai.api_key = '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'

# ------------------------------------------------------------------------------------------------

# Get the Job and Resume as text

job_info = open("input/job.txt").read()

if(not job_info): 
  print("ERROR with input file: job.txt")
  exit(1)

resume = open('input/resume.txt').read()

if(not resume): 
  print("ERROR with input file: resume.txt")
  exit(1)

# ------------------------------------------------------------------------------------------------
# SETUP THE API CALL

# 1 - Set the context for the assistant (what is the duty/behavior?)

system_context = "You write in the first-person perspective of a student/proffesional with the skills/experiences listed in the resume below. You are designed to output to JSON, total length should roughly fit a page."

system_context += "\n" + resume

# 2 - Create the User Message for Assistant to reply to

user_message = """
  Based on the Job Info further down, create a detailed JSON response following this exact format: 
    {
      "intro": "Short intro. Mention the company, role and why your excited to apply",
      "qualifications": "'I meet the Basic Qualifcations:' quickly list that/how you meet them with specifics", 
      "requirements": [{
        "requirement #" : "How you meet this requirement (give examples and proof)", 
      }]
    }
"""

user_message += "Job Info:\n" + job_info


# ------------------------------------------------------------------------------------------------
# DO THE API CALL

def api_call() -> dict: 

  messages = [
    {"role": "system", "content": system_context},
    {"role": "user", "content": user_message}
  ]

  chat = openai.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type": "json_object"}, 
    messages = messages
  )

  # Check the finish reason 

  finish_reason = chat.choices[0].finish_reason
  reply = ""

  if(finish_reason == "stop"): 
    reply = chat.choices[0].message.content
    # Check # tokens
    usage = chat.usage
    total_tokens = usage.total_tokens
    print('\n Total Tokenns = ', total_tokens)
    # calculate cost 
    rate = 0.0001
    cost = rate * (total_tokens / 1000)
    print('\n Cost = ', cost)
  else: 
    print('ERROR with API call. finish_reason = ', finish_reason)
    exit(1)

  output: dict = json.loads(reply)
  print('\n', output, '\n')

# output = api_call()

output: dict = {'intro': 'I am excited to apply for the Software Developer position at FDM. The opportunity to undergo industry-specific training and continue my career journey as an FDM consultant while working for globally recognized clients aligns with my career goals and aspirations. I am enthusiastic about the prospect of utilizing my coding and creative thinking skills to impact the development and delivery of technological solutions for businesses, as well as to solve problems and improve efficiency for large software development projects.', 'qualifications': 'I meet the Basic Qualifications: Eligible to work in Canada, pursuing an Honours degree in Computer Science at the University of Waterloo, and able to commit to working for FDM for a minimum of two years following the training period.', 'requirements': [{'requirement 1': 'I possess a natural aptitude for technology and have a strong desire to expand my technical skill set. For instance, during my internship at Environics Analytics, I developed an automated pipeline with Alteryx and Deep-L API to parse and translate data product documents to French, resulting in significant savings for the company. This demonstrates my ability to leverage technology to solve complex problems and expand my technical skill set.'}, {'requirement 2': 'I have extensive exposure to multiple programming languages, including Python, C++, and C. I also have experience with JavaScript and TypeScript. For example, I developed a user-friendly app using Python/QT to extract client usage data from databases at Environics Analytics, showcasing my proficiency in multiple programming languages.'}, {'requirement 3': 'I am familiar with both Microsoft and Linux operating systems, having worked extensively with them during my academic and professional projects. This includes utilizing SQL databases and SQL Server in my internship at Environics Analytics, further demonstrating my exposure to operating systems and databases.'}, {'requirement 4': 'I have a solid understanding of databases and SQL, which is evident from my experience enhancing databases to monitor client usage of products and APIs, ultimately formulating an optimized product pricing strategy during my internship. Additionally, I created a dynamic and user-friendly Database Interface App using Python and SQL, showcasing my proficiency in databases and SQL.'}]}

output_2_pdf(output["intro"], output["qualifications"], output["requirements"])