#!venv/bin/python3
import jinja2
from jinja2 import Template
from jinja2 import PackageLoader

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

experiences = [
    {
        "title": "Software Engineering Intern",
        "organization": "Quantum Corp",
        "date": "May 2019 - Present",
        "description": """Worked on Quantum Managed Services, a service which allows Quantum to co-manage on-premise appliances from remote.
Contracted by ProUnlimited."""
    }
]

projects = [
    {
        "title": "Ludum Dare (Game Jam): Life is Currency",
        "date": "April 2019",
        "description": """Used Two.js to make a Tower Defense browser game in a team with one other where the only way to make currency is to lose health."""
    },
    {
        "title": "Hack Merced: On My Way",
        "date": "March 2019",
        "description": """Used ReactJS to make an alternative graduation requirement planner with the aim of being faster and more user friendly."""
    },
    {
        "title": "Google foobar",
        "date": "2018",
        "description": """Completed all levels (1 - 5) of the Google foobar coding challenge twice and had been reached out by Google on both occasions."""
    },
    {
        "title": "SPARK Final Project",
        "date": "2018",
        "description": """Contributed data analysis code to interpreted oscilloscope data to find the speed of light in Python."""
    }
]

skillsets = [
    {
        "name": "Programming Languages",
        "skills": ["Java", "C/C\\verb!++!", "Python", "GoLang", "Kotlin", "php"]
    },
    {
        "name": "Web Development",
        "skills": ["React", "Laravel", "Javascript", "Google Analytics", "Two.js", "HTML", "CSS"]
    },
    {
        "name": "Other",
        "skills": ["AWS", "Linux", "\LaTeX", "docker", "computer networking", "Android Studio"]
    }
]

for skillset in skillsets:
    skillset["skills"] = ", ".join(skillset["skills"])

math_coursework = ["Probability and Statistics", "Linear Algebra & Differential Equations", "Multivariable Calculus"]
cs_coursework = ["Data Structures", "Discrete Mathematics", "Circuit Theory"]
phys_coursework = ["Special Relativity", "Thermal Physics"]

coursework = ", ".join(cs_coursework)

major_gpa = {
    "name": "Major GPA",
    "value": 3.9
}

gpa = {
    "name": "GPA",
    "value": 3.8
}


with open('Resume.tex', 'w+') as f:
    f.write(resume_template.render(
        config=config,
        experiences=experiences,
        projects=projects,
        skillsets=skillsets,
        gpa=major_gpa,
        coursework=coursework
    ))
