import streamlit as st
from utils import generate_metadata_with_retry

def main():
    st.title("Story Channel Metadata & SEO Optimizer")

    niches = [
        "True Crime Stories",
        "Paranormal Encounters",
        "Survival Stories",
        "Celebrity Scandals",
        "Revenge & Payback Stories",
        "Relationship Breakups",
        "Workplace Horror Stories",
        "Family Feuds & Drama",
        "Unsolved Mysteries",
        "Alien Abduction & UFO Sightings",
        # Add more niches as needed
    ]

    niche = st.selectbox("Select Story Niche", niches)
    keywords = st.text_area("Enter story keywords or short topic summary", height=100)

    if st.button("Generate Metadata"):
        if keywords.strip() == "":
            st.error("Please enter keywords or story summary.")
        else:
            with st.spinner("Generating..."):
                try:
                    result = generate_metadata_with_retry(niche, keywords)
                    st.subheader("Generated Metadata")
                    st.code(result)
                except Exception as e:
                    st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
