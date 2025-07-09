from utils.ats_matcher import calculate_ats_score
import pandas as pd

def score_multiple_jds(resume_text, jd_list):
    results = []
    for jd in jd_list:
        score = calculate_ats_score(resume_text, jd)
        results.append({"Job Description": jd[:40] + "...", "ATS Score": score})
    return pd.DataFrame(results)
