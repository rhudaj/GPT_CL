'''
    Header Info
    "Dear Hiring manager," + [GPT].Intro
    [GPT].BasicQualifications
    For every Requirement 
    "i." + "Requirement i" + [GPT].Requirements[i]
'''

import fpdf
pdf = fpdf.FPDF()
pdf.add_page() #create new page
font_size = 10
line_height = .6 * font_size
pdf.set_font(family="Arial", size=10) # font

def new_line(content: str = ""):
    pdf.multi_cell(w=0, h=line_height, txt=content)

# GET/CREATE OUTPUT DATA

import datetime

header = [
    datetime.date.today().strftime("%B %d, %Y"),
    "Roman Hudaj", 
    "Toronto, On", 
    "647-502-0512", 
    "rhudaj@uwaterloo.ca"
]


def output_2_pdf(intro: str, qualification: str, requirements: dict[dict]): 
    # HEADER
        for item in header: new_line(item)
    # GREETING
        new_line()
        new_line("Dear Hiring Manager, ")
    
    # INTRO
        new_line()
        new_line(str(intro))
    
    # QUALIFICATIONS
        new_line()
        new_line(str(qualification))

    # REQUIREMENTS
        new_line()
        for item in requirements:
            key = list(item.keys())[0]
            value = item[key]
            new_line(key)
            new_line(value)
            new_line()


    # FINAL OUTPUT
        pdf.output("output/test.pdf")