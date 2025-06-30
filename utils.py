import openai
import os

# Set your OpenAI API key here or use environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")  

def generate_metadata(niche: str, keywords: str) -> str:
    prompt = f"""
You are an expert YouTube strategist for faceless story channels.
Niche: "{niche}"
Story Keywords: "{keywords}"

Generate 5 clickable, emotional YouTube titles using popular story clickbait styles.
Then generate a compelling video description with an emotional hook, keywords, CTAs, and hashtags.

Output format:

Titles:
1.
2.
3.
4.
5.

Description:

Tags:

Hashtags:
"""
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=prompt,
        max_tokens=350,
        temperature=0.8,
        n=1
    )
    return response.choices[0].text.strip()
