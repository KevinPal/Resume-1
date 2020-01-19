#!venv/bin/python3
import os
import json

import jinja2

ME_PATH = "me/me.json"

def load_me():
    """
    Loads "me" information from ME_PATH
    """
    with open(ME_PATH, "r") as f:
        return json.loads(f.read())

me = load_me()

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.PackageLoader('resume', 'templates')
)

resume_template = latex_jinja_env.get_template('Resume.tex')

experiences = me['career']['experience']

projects = me['career']['projects']

skillsets = me['career']['skillsets']

for skillset in skillsets: # comma separating skills from skillsets
    skillset["skills"] = ", ".join(skillset["skills"])

coursework = ", ".join(me['academics']['relevant_coursework']['cs'])

major_gpa = me['academics']['major_gpa']
gpa = me['academics']['gpa']

short_skills = True

with open('Resume.tex', 'w+') as f:
    f.write(resume_template.render(
        experiences=experiences,
        projects=projects,
        skillsets=skillsets,
        gpa=major_gpa,
        short_skills=short_skills,
        coursework=coursework
    ))
