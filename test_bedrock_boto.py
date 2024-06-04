import boto3 # dolphins native to the Amazon River --> provides access to AWS tools
import json  # standard text-based format for representing structured data

# Bedrock runtime object: an application specific object that 
#                       contains both state and behavior that provides an application specific function
# 'bedrock-runtime' is an endpoint to send API request to
bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-west-2')

prompt = "What is RAG in AI?"

# kwargs = Key Word Arguments
kwargs = {
    "modelId": "meta.llama3-8b-instruct-v1:0",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    })
}

response = bedrock_runtime.invoke_model(**kwargs)
body = json.loads(response['body'].read())
generated_text = body['generation']
print(generated_text)