import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Smart Medical Bot", layout="centered")

# Title and description
st.title("🤖 Smart Medical Bot")
st.markdown("Please enter your symptoms, and the bot will provide an initial medical suggestion.")

# Text input from user
user_input = st.text_input("✍️ Describe your symptoms:")

# Button to trigger the response
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter your symptoms before submitting.")
    else:
        # API endpoint and headers
        url = "https://udify.app/chat/BXE7UHClh3Liaf7T"
        headers = {
            "Authorization": "Bearer app-MvMNfrvLnaD8mR9eKbP1Q4I1",
            "Content-Type": "application/json"
        }

        # Payload for the request
        payload = {
            "inputs": user_input,
            "response_mode": "blocking"
        }

        # Make the API request
        with st.spinner("⏳ Please wait..."):
            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()

                try:
                    result = response.json()
                    reply = result.get("answer") or result.get("response") or result.get("text") or "⚠️ No valid answer received."
                except ValueError:
                    reply = "⚠️ Response is not in JSON format:\n\n" + response.text

                st.success("🩺 Bot's Response:")
                st.write(reply)

            except requests.exceptions.HTTPError as e:
                st.error("🚫 HTTP Error:")
                st.code(f"{e}\n\n{response.text}")
            except requests.exceptions.RequestException as e:
                st.error("🚨 Request failed:")
                st.code(str(e))
