def extract_jd_text(jd_input):
    return [jd.strip() for jd in jd_input.split("###") if jd.strip()]