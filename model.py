from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

def load_model():
    """Loads the quantized model and tokenizer."""
    model_id = "google/gemma-2b-it"

    # Configure 4-bit quantization to save memory
    quantization_config = BitsAndBytesConfig(load_in_4bit=True)

    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
    
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=quantization_config,
        device_map="auto",  # Automatically places layers on GPU/CPU
        torch_dtype=torch.bfloat16
    )
    # Returns only model and tokenizer
    return model, tokenizer

def get_response(prompt, model, tokenizer, max_length=150):
    """Generates a response from the model given a prompt."""
    
    # 1. Format the prompt for the chat model
    chat = [{"role": "user", "content": prompt}]
    
    formatted_prompt = tokenizer.apply_chat_template(
        chat,
        tokenize=False,
        add_generation_prompt=True
    )
    
    # 2. Tokenize the input and move to the correct device
    device = model.device 
    
    inputs = tokenizer(
        formatted_prompt, 
        return_tensors="pt"
    ).to(device)

    # 3. Generate output
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_length,
        do_sample=True,
        temperature=0.7,
        pad_token_id=tokenizer.eos_token_id
    )

    # 4. Decode and return the output
    try:
        # Slicing the tensor to get only the generated tokens
        prompt_len = inputs["input_ids"].shape[-1]
        generated_tokens = outputs[0][prompt_len:]
        response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
    except Exception:
        # Fallback to text parsing
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split("assistant")[-1].strip()
        
    return response.strip()