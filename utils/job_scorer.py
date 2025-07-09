
def calculate_job_readiness(ats_df, audit_dict):
    base_score = ats_df["ATS Score"].mean()

    # Safely get the readability_score with a default value of 0 if the key is missing
    readability_score = audit_dict.get("readability_score", 0)
    
    # Compute a bonus score from readability (capped at 10)
    readability_bonus = min(10, readability_score / 10)

    return round(base_score + readability_bonus, 2)
