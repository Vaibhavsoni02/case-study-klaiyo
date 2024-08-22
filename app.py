import streamlit as st
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract content from the HTML code
def extract_content(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    data = []

    # Extract all the articles
    articles = soup.find_all('article')

    for article in articles:
        # Extract the header content
        header = article.find('h3', class_='variants__TypographyBase-sc-g6bgyl-1 dpqvHS styles__StyledHeaderContent-sc-cms744-1 bzocry')
        header_text = header.text if header else 'N/A'

        # Extract the body content
        body = article.find('div', class_='variants__TypographyBase-sc-g6bgyl-1 iiZygX styles__StyledBodyContent-sc-cms744-4 gkAJRZ')
        body_text = body.text if body else 'N/A'

        # Extract the href link
        link = article.find('a', class_='button-module--light--22f31 button-module--button--3cbf6 button-module--tertiary--57c95')
        href = link['href'] if link else 'N/A'

        data.append({
            'Header': header_text,
            'Body': body_text,
            'Link': href
        })

    return data

# Streamlit app
st.title("HTML Content Extractor")

# Input field for raw HTML code
html_code = st.text_area("Paste your raw HTML code here:")

if st.button("Extract"):
    if html_code:
        # Extract content
        extracted_content = extract_content(html_code)
        
        if extracted_content:
            # Convert to DataFrame
            df_content = pd.DataFrame(extracted_content)
            st.write("Extracted Data:")
            st.dataframe(df_content)
        else:
            st.write("No content found in the provided HTML.")
    else:
        st.write("Please paste some HTML code.")
