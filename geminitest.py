import google.generativeai as genai

genai.configure(api_key="AIzaSyA4vOzZ6CFLvYdaMcEiIPSYuSgi3-6xTxs")  # Ensure your API key is correct

# Fetch and print the available models
models = genai.list_models()

for model in models:
    print(model.name)  # Prints available model names
