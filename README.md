ProcessVoiceRecordings.py
This Python script is a Microsoft demo used to process voice recordings. It fetches a specific file from Azure Data Lake Gen2, analyzes the document content, calculates the total number of tokens, and uses OpenAI to analyze the conversation. The results are then uploaded back to Azure Data Lake.

⚠️ Disclaimer
This script is a demonstration and not ready for production use. It requires further testing and User Acceptance Testing (UAT). Customers should use this as a demo and not in a production environment without proper testing and validation.

Dependencies
The script uses the following Python libraries:

asyncio
Gen2Services
DocumentAnalysis
Tools
OpenAIKernel
json
dotenv
os
Environment Variables
The script requires the following environment variable:

CONNECTION_STRING: The connection string for Azure Data Lake.
How to Run
The script is asynchronous and uses the asyncio library to run the main function. To run the script, use the following command:

Functions
use_gen2_services(): This function gets the URL of the file from Azure Data Lake Gen2.
main(): This is the main function that orchestrates the process of fetching the file, analyzing the content, and uploading the results back to Azure Data Lake.
Output
The script prints a message "Results uploaded to Azure Data Lake" to the console once the results are successfully uploaded to Azure Data Lake. The results are stored in the "customercalls/CallAnalytics" folder in Azure Data Lake.

Last update April 2024

CRTEATE THIS IN YOUR .env FILE
OPENAI_API_KEY=""
OPENAI_ORG_ID=""
AZURE_OPENAI_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=" "
AZURE_OPENAI_API_KEY=""
DOCUMENT_ENDPOINT=""
DOCUMENT_KEY=""
CONNECTION_STRING=""