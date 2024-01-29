# Convert get to post request.
import json

# Step 1 class to handle get resp and convert it
class ParseData:

    def __init__(self, data):
        self.data = data

    # Step 2 convert get into post
    def format(self):
        # Mapping key to link get variable name to get value
        mapping_key = 0

        # Split our string into arrays by ? meaning there is an new array
        data_splited = self.data.split("?")

        # load an empty json object
        formatted_json = json.loads("{}")
        
        # Loop trough arrayas
        for i in data_splited:
            # Increase mapping_key to make an new json array
            mapping_key += 1

            # Make get object into other objects to acces the variable data and variable name
            get_attribute = i.split("=")

            # Loop trough the object
            for i in get_attribute:
                
                # Make sure there isnt empty data
                if i:
                    # Add data to our json object by key and value
                    formatted_json[get_attribute[0]] = i
        
        # Return our json object
        return formatted_json

                      
# Step 3 Run Class'
if __name__ == "__main__":
    GetToPost = ParseData("?item1=thisisitem1?second=12")
    # Step 4 Print the response      
    print(GetToPost.format())
