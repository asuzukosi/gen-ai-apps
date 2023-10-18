import yaml

def get_info_from_config(query, file_path="config.yaml"):
    """
    Retreive specific information from the config file
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            for key in data:
                if key == query:
                    return data[key]
            print("Query not found in config file")
    except Exception as e:
        print("Failed to load config file formt eh specified path: %s" % file_path)
        
    