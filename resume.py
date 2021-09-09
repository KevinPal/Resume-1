#!venv/bin/python3
import os
import json

import jinja2

ME_PATH = "./me.json"

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

config = {
    "short_skills": True
}

experiences = me['career']['experience']

projects = me['career']['projects']

skillsets = me['career']['skillsets']

for skillset in skillsets: # comma separating skills from skillsets
    skillset["skills"] = ", ".join(skillset["skills"])

coursework = " --- ".join([x for x in list(me['academics']['relevant_coursework']['cs'])])
user = me['user']

with open('Resume.tex', 'w+') as f:
    f.write(resume_template.render(
        config=config,
        experiences=experiences,
        projects=projects,
        skillsets=skillsets,
        coursework=coursework,
        **me
    ))
