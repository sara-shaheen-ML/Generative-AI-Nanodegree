'''
This script demonstrates how to use LiteLLM and OpenAI models to automatically generate Python unittest test cases based on natural-language instructions.
The script:
Loads an OpenAI API key (from environment or hardcoded fallback)
Defines a system prompt to set the model’s behavior
Defines a user prompt specifying the exact test requirements
Calls an LLM model (e.g., gpt-4o-mini) to generate unittest test code
Prints the generated test class to the console
It uses a simple function named double(x) as an example and produces tests for:
A positive number
Zero
A negative number
This file is intended as a learning example for:
Understanding system vs user prompts
Integrating LLMs with Python code
Generating automated unit tests
Practicing API usage outside of Vocareum/Udacity
TO USE THE SCRIPT: 
1. install LiteLLM
pip install litellm
2. set your environment API key or hard-code it
export OPENAI_API_KEY="sk-your-key"
3. RUN the script
python unittestGenerator.py

run the script
'''
import litellm
import os

# --- SET YOUR API KEY ---
# Use environment variable OR hardcode your key here
litellm.openai_key = os.getenv("OPENAI_API_KEY") or "sk-your-key-here"

# --- PROMPTS ---
SYSTEM_PROMPT = """
You are a helpful coding assistant that writes unit tests using the unittest framework.
Return only the code, no explanations.
"""

USER_PROMPT = """
Generate unittest test cases for a function called `double`
that returns the input number multiplied by 2.

Requirements:
- Create a class `TestDouble` that inherits from unittest.TestCase
- Include tests for:
    * a positive number (e.g., 5 → 10)
    * zero (0 → 0)
    * a negative number (e.g., -3 → -6)
- Do not include any imports or a main block.
"""

# --- LLM CALL ---
from litellm import completion

response = completion(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ],
)

print("Generated Test Code:\n")
print(response.choices[0].message.content)

