# Import necessary modules
import asyncio
import Gen2Services as g2s
import DocumentAnalysis as da
import Tools as tools
import OpenAIKernel as oai
import json
from dotenv import load_dotenv
import os
load_dotenv()

# Get the connection string
connection_string = os.getenv('CONNECTION_STRING')
# Define connection string for Azure Data Lake
 
# Define the file name
FileName = "8x8 Transcript Sale Call 3"

# Function to get the URL of the file from Azure Data Lake Gen2
async def use_gen2_services():     
    url = g2s.get_file_url(connection_string, "voicefiles",  FileName + ".pdf")
    return url

# Main function
async def main():
    # Get the file URL
    fileURL = await use_gen2_services()
    
    # Analyze the document content
    documentContent = da.analyze_read(fileURL)
    
    # Calculate the total number of tokens
    totalTokens = tools.num_tokens_from_string(documentContent, "cl100k_base") 
    documentContent = documentContent.replace("&", " and ")
    # Analyze the conversation using OpenAI
    Results = await oai.analyze_conversation(documentContent, totalTokens)
    
    # Convert the results to a string
    Content = (str(Results))  
    # Upload the results to Azure Data Lake
    g2s.upload_to_datalake(connection_string, "customercalls/CallAnalytics", FileName + ".txt", Content) 
    print("Results uploaded to Azure Data Lake")

# Run the main function
asyncio.run(main())