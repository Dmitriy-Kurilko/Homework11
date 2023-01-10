import json


def load_candidates(path):
    with open(path, 'r') as candidates:
        return json.load(candidates)


def get_candidate(candidate_id):
    list_ = []
    for candidate in load_candidates('candidates.json'):
        if candidate['id'] == candidate_id:
            list_.append(candidate)
    return list_[0]


def get_candidates_by_name(candidate_name):
    list_ = []
    for candidate in load_candidates('candidates.json'):
        if candidate_name in candidate['name']:
            list_.append(candidate)
    return list_


def get_candidates_by_skill(skill_name):
    list_ = []
    for candidate in load_candidates('candidates.json'):
        if skill_name.lower() in candidate['skills'].lower():
            list_.append(candidate)
    return list_
