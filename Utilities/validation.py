import json
import jsonschema

def get_schema(schema_path: str) -> json:
    """T
    his function loads the schema for a Strafer configuration json.
    """
    try:
      with open(schema_path, 'r') as file:
          schema = json.load(file)
      return schema
  
    except OSError:
        # DEBUG
        print(f"Cannot open configuration file schema at {schema_path}")
        raise SystemExit

def validate_json(json_path: json, module: str) -> bool:
    """ 
    validates a json according to the module that is currently being configured
    """
    if module == "strafer":
        schema = get_schema('strafer_schema.json')
    else:
        # TBD  
        pass

    try:
        validation_result = jsonschema.validate(json_path, schema)

        if validation_result is None:
            return True

    except jsonschema.exceptions.SchemaError:
        # DEBUG
        print("There is an error with the schema")
        
    except jsonschema.exceptions.ValidationError as e:
        # DEBUG
        print(e)
        print(e.absolute_path)
        print(e.absolute_schema_path)
