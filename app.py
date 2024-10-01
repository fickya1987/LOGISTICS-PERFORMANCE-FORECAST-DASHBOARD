import streamlit as st

# Set the title of your Streamlit app
st.title('CREST CONTAINERS LOGISTICS PERFORMANCE & FORECAST DASHBOARD')

# Provide a description for your dashboard
st.write("""
This Streamlit app embeds a Power BI dashboard. You can interact with the dashboard directly from this page.
""")

# Add the Power BI embed URL (replace with your actual embed link)
powerbi_embed_url = "https://app.powerbi.com/reportEmbed?reportId=bc64dd41-c344-4503-a2e5-16987b680e86&autoAuth=true&ctid=fe8ccb52-ca53-49de-a5b4-50faf33a9cc2"

# Embed the Power BI dashboard using an iframe
st.components.v1.iframe(src=powerbi_embed_url, width=1000, height=600)
