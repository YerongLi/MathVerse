import json
import time
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM
ckpt_path = "/home/yerong2/models/internlm-xcomposer2-vl-7b"
tokenizer = AutoTokenizer.from_pretrained(ckpt_path, trust_remote_code=True)
# Set `torch_dtype=torch.float16` to load model in float16, otherwise it will be loaded as float32 and might cause OOM Error.
model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=torch.float16, trust_remote_code=True, device_map='auto')

model = model.eval()

# Load the data from the JSON file
with open('data/testmini.json', 'r') as file:
    data = json.load(file)

# Iterate through each dictionary in the list
for entry in tqdm(data):
    # Extract the relevant fields from each entry
    query_cot = entry["query_cot"]
    image_path = entry["image"]

    # Load the image
    image = 'data/images/blank.png'
    # Define the query for the model
    query = '<ImageHere>'+query_cot
    # Assuming 'model' and 'tokenizer' are already defined and loaded
    with torch.cuda.amp.autocast():
        response, _ = model.chat(tokenizer, query=query, image=image, history=[], do_sample=False)

    # Add the response to the entry
    entry["answer"] = response

# Save the updated data to a new JSON file
with open('data/testmini_text_ans.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Responses saved to data/testmini_test_ans.json")

