from huggingface_hub import InferenceClient


def model(APIKEY):
    
    return InferenceClient(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        token=APIKEY
    )