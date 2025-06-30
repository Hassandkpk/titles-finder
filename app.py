import streamlit as st
from utils import generate_metadata

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
                result = generate_metadata(niche, keywords)
                st.subheader("Generated Metadata")
                st.code(result)

if __name__ == "__main__":
    main()
