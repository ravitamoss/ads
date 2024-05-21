
"""
Code was used to generate dataset of ads from generative AI (gemini-1.5-pro-latest)
"""
import time
import google.generativeai as genai

genai.configure(api_key="AIzaSyBJflTSmXMpQ5w2i3-HdthCTl-0D0QisCQ")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config)

convo = model.start_chat(history=[
])

msg = '''
Generate a dataset of magazine advertisements targeting women or men.
You are free to select the topic, product, service, or whatever your want.

Reply as follows:

1. Target audience: [Men / Women] (requirement: choose one, randomly)
2. General Domain: []
3. Product or Service: [ ] 
4. Aggressiveness level: [from 1 to 5]
5. Advertisement text - headline: [ ] (in double quotes)
6. Advertisement text - body: [ ] (in double quotes)
7. Visual Style and Tone: [ ] (requirement: one word) 
8: Image: [An image of the advertisement without humans]

Reply in a CSV format with 5-10 rows, each row contains all of the above.
'''

with open("gemini_ads.txt", "a") as f:
    try:
        while True:
            convo.send_message(msg)
            res = convo.last.text
            print(res)
            f.write(res + '\n')  # Ensure new data starts on a new line
            time.sleep(20)  # Wait before sending the next request
    except Exception as e:
        print("An error occurred:", e)


