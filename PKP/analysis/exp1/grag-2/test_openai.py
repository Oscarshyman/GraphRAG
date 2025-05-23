import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file in the current directory
# Ensure your .env file has GRAPHRAG_API_KEY=sk-proj-xxxxxx
load_dotenv()

api_key = os.getenv("GRAPHRAG_API_KEY")

if not api_key:
    print("Error: GRAPHRAG_API_KEY not found in .env file or environment variables.")
else:
    print(f"Using API Key: {api_key[:8]}...{api_key[-4:]}") # Print part of the key to confirm it's loaded
    client = openai.OpenAI(api_key=api_key)

    try:
        print("Attempting to call OpenAI API (models.list)...")
        response = client.models.list()
        # If the call succeeds, it will print a list of models.
        # We are just checking if we get *any* successful response.
        print("Successfully received response from OpenAI API.")
        print(f"Found {len(response.data)} models.")
        # print("First few models:")
        # for model in list(response.data)[:3]:
        #     print(f"- {model.id}")

    except openai.APIConnectionError as e:
        print(f"OpenAI APIConnectionError: {e}")
        print("This usually indicates a network problem (DNS, firewall, proxy).")
    except openai.RateLimitError as e:
        print(f"OpenAI RateLimitError: {e}")
    except openai.AuthenticationError as e:
        print(f"OpenAI AuthenticationError: {e}")
        print("Please check your API key and organization ID (if applicable).")
    except openai.APIStatusError as e:
        print(f"OpenAI APIStatusError: {e.status_code} - {e.response}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()