import os
from dotenv import load_dotenv
load_dotenv()
groq_api = os.getenv('GROQ_API_KEY')
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from groq import Groq

model_name = "sentence-transformers/all-mpnet-base-v2"

embeddings = HuggingFaceEmbeddings(model_name=model_name)

CHROMA_PATH='chroma\policies'


def policy_details(policy_name):
    query_db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings,collection_name=policy_name)
    documents = query_db.get(include=['documents'])
    document_content=""
    for doc in documents['documents']:
        document_content+=doc+"\n"
    return document_content

def denial_details():
    path="chroma\denial"
    query_db = Chroma(persist_directory=path, embedding_function=embeddings,collection_name='denial')
    documents = query_db.get(include=['documents'])
    document_content=""
    for doc in documents['documents']:
        document_content+=doc+"\n"
    return document_content

def get_user_summary(name,age,policy,type,gender,claims,policy_start_date,premium,amt,expiry,contact):
    summary =f"""
                Name: {name}
                Age: {age}
                Gender: {gender}
                Policy Name: {policy}
                Policy Type: {type}
                Policy Enrolled Date: {policy_start_date}
                Policy Expiry: {expiry}
                Premium: {premium}
                Total Insurance Amount: {amt}
                Insurer Contact :{contact}
                History of claims made by the user:
                {claims}
            """
    print(summary)
    return summary


def denial_details():
    path="chroma\denial"
    query_db = Chroma(persist_directory=path, embedding_function=embeddings,collection_name='denial')
    documents = query_db.get(include=['documents'])
    document_content=""
    for doc in documents['documents']:
        document_content+=doc+"\n"
    return document_content

def policy_details(policy_name):
    query_db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings,collection_name=policy_name)
    documents = query_db.get(include=['documents'])
    document_content=""
    for doc in documents['documents']:
        document_content+=doc+"\n"
    return document_content
    


def format_output(llm_output):
    client = Groq(
        api_key=groq_api,
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are provided with content generated by llm. Your task is to format the output with html tags. Dont change the content!! only format by adding html tags like <h3>,<h4> ,<h5>,<p>",
            },
            {
                "role": "user",
                "content": "Dont mention contents liked 'I have added HTML tags to the existing content as requested', 'Here is the formatted output with HTML tags:' or similar content",
            },
            {
                "role": "user",
                "content": llm_output,
            },
        ],
        model="llama-3.1-70b-versatile",
    )
    output=chat_completion.choices[0].message.content
    return output


