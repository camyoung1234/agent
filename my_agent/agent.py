import os
import getpass
from google.adk.agents import LlmAgent

# Make sure GOOGLE_GENAI_USE_VERTEXAI is false to use the free tier / standard Gemini API
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "FALSE"

# Check if GOOGLE_API_KEY is already set, if not, ask securely
if "GOOGLE_API_KEY" not in os.environ:
    if "GEMINI_API_KEY" in os.environ:
        os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]
    else:
        # Prompt securely for API key if we don't have it
        try:
            api_key = getpass.getpass("Please enter your Gemini API Key: ")
            os.environ["GOOGLE_API_KEY"] = api_key
        except Exception:
            pass # Gracefully handle EOFError in non-interactive environments

# Create the root agent as expected by adk
root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="my_agent",
    instruction="You are a fast and helpful Gemini assistant."
)
