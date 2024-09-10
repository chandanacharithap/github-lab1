import json

def search_json(json_data, search_string):
    results = []

    def search_in_data(data, search_string, path=""):
        if isinstance(data, dict):  
            for key, value in data.items():
                new_path = f"{path}/{key}" if path else key
                if search_string.lower() in key.lower():
                    results.append(f"Found in key: {new_path}")
                search_in_data(value, search_string, new_path)
        elif isinstance(data, list):  
            for index, item in enumerate(data):
                new_path = f"{path}[{index}]"
                if isinstance(item, dict): 
                    search_in_data(item, search_string, new_path)
        else:  
            if search_string.lower() in str(data).lower():
                results.append(f"Found in value at: {path}")

    # Assuming json_data is a list of dictionaries
    search_in_data(json_data, search_string)
    
    return results
