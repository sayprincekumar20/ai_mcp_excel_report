import pandas as pd

def save_to_excel(data_dict: dict, filename: str):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for sheet, data in data_dict.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, index=False, sheet_name=sheet)
