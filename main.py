from flask import Flask, render_template
from utils import *

app = Flask(__name__)

@app.route('/')
def main_page():
    all_candidates = load_candidates('candidates.json')
    return render_template('list.html', candidates=all_candidates)

@app.route('/candidate/<x>')
def page_candidates(x):
    pasport_candidate = get_candidate(int(x))
    return render_template('single.html', pasport_candidate=pasport_candidate)

@app.route('/search/<candidate_name>')
def searching_name(candidate_name):
    length = len(get_candidates_by_name(candidate_name))
    list_candidates = get_candidates_by_name(candidate_name)
    return render_template('candidate_name.html', list_candidates=list_candidates, length=length)

@app.route('/skill/<skill_name>')
def searching_skill(skill_name):
    candidates_with_skills = len(get_candidates_by_skill(skill_name))
    return render_template('candidate_skill.html', pasport_candidate=get_candidates_by_skill(skill_name), candidates_with_skills=candidates_with_skills, skill_name=skill_name)

app.run()