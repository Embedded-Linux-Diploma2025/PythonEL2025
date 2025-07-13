"""Get the functions prototype from a header file and insert them in excel file."""
import os
import re
import pandas
PATTERN = r"^\s*([\w\s\*]+?)\s+(\w+)\s*\(([^;]*)\)\s*;"
current_dir = os.path.dirname(os.path.abspath(__file__))
header_file_path = os.path.join(current_dir, "functions.h")
list_of_func = []
ID:int = 1
with open(header_file_path, "r", encoding="utf-8") as file_descriptor:
    file_list = file_descriptor.readlines()
    for line in file_list:
        match = re.search(PATTERN, line)
        if match:
            return_type = match.group(1)
            function_name = match.group(2)
            parameters = match.group(3)
            list_of_func.append({"return_type": return_type,
                                 "function_name": function_name,
                                 "parameters": parameters,
                                 "ID": f"IDX00{ID}"})
            ID = ID + 1
data = pandas.DataFrame(list_of_func)
data.to_excel(os.path.join(current_dir, "functions.xlsx"), index=False)
