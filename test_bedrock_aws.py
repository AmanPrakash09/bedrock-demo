from langchain_aws import BedrockLLM

# Initialize the Bedrock LLM
# no more niche API request formats, set model_id and you're good to go!
llm = BedrockLLM(
    model_id="meta.llama3-8b-instruct-v1:0"
)

# Invoke the llm
response = llm.invoke("What is RAG in AI?")
print(response)