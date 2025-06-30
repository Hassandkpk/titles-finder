from openai import OpenAI
import streamlit as st

# Initialize OpenAI client
client = OpenAI()

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert YouTube strategist for faceless story channels."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=350,
    )
    return response.choices[0].message.content.strip()
