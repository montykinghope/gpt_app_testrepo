import azure.functions as func
import json
import os
from openai import OpenAI

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Extract the prompt from the HTTP request
        req_body = req.get_json()
        prompt = req_body.get('body')  # Assuming the prompt is passed in the 'body' key

        if not prompt:
            return func.HttpResponse(
                "Please pass a prompt in the request body",
                status_code=400
            )

        api_key = os.environ.get('openaikey')
        if not api_key:
            return func.HttpResponse(
                "API key is missing",
                status_code=500
            )

        # Initialize the OpenAI client with your API key
        client = OpenAI(api_key=api_key)

        # Make the GPT call with the provided prompt
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-3.5-turbo",
            temperature=0,
        )

        # Extract the reply content
        reply_content = chat_completion.choices[0].message.content

        # Return the GPT response
        return func.HttpResponse(json.dumps({"response": reply_content}), mimetype="application/json")
    except ValueError:
        return func.HttpResponse(
            "Invalid request body. Please send JSON with a 'body' key.",
            status_code=400
        )
    except Exception as e:
        return func.HttpResponse(f"Error processing request: {str(e)}", status_code=500)
