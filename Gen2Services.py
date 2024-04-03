from azure.storage.filedatalake import DataLakeFileClient
from azure.storage.filedatalake import DataLakeFileClient, generate_file_sas
from azure.storage.filedatalake import FileSasPermissions
from datetime import datetime, timedelta


def upload_to_datalake(connectionstring, file_system_name, file_path, data):
    file = DataLakeFileClient.from_connection_string(connectionstring,
                                                     file_system_name=file_system_name, file_path=file_path)
    file.create_file()
    file.append_data(data, offset=0, length=len(data))
    file.flush_data(len(data))
    

def get_file_url(connectionstring, file_system_name, file_path):
    file = DataLakeFileClient.from_connection_string(connectionstring,
                                                     file_system_name=file_system_name, file_path=file_path)
   

    # Generate SAS token
    sas_token = generate_file_sas(
        account_name=file.account_name,
        file_system_name=file_system_name,
        file_name=file_path,
        directory_name="",      
        credential=file.credential.account_key,
        permission=FileSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)  # Token valid for 1 hour
    )

    # Construct the URL
    url = f"https://{file.account_name}.dfs.core.windows.net/{file.file_system_name}/{file_path}?{sas_token}"

    return url 