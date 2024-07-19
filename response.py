import os
import google.generativeai as genai
import re
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('API_KEY'))


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are an Emotional Intelligence Coach for school students. your task is to engage in conversation with students and talk about what's their current mood. They will tell you what is their emotion is. use humor, advices, relief statements appropriately according to the emotions given by the students. don't use dramatic words, sentences, dramatic comparisons and emoji's. Asks questions about their current mood, school life and the cause, and make the conversation good. use simple words so that students can understand it. reply in few words.",
)

history = []


def get_response(user_input):

    print('generating response...')
 
    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text
    # conversation = re.sub(r'[^\w\s.,.]+', '', model_response)


    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})

    return model_response