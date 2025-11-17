from src.model import load_model, get_response 
 
model, tokenizer = load_model() 
 
while True: 
    user_input = input("You: ") 
    if user_input.lower() == 'quit': 
        break 
    response = get_response(user_input, model, tokenizer) 
    print(f"Model: {response}\n")