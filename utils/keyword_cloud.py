from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io

def generate_missing_keywords_cloud(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())

    missing_keywords = jd_words - resume_words
    missing_text = " ".join(missing_keywords)

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(missing_text)

    # Save to bytes
    img_bytes = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    return img_bytes
