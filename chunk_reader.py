
def read_massive_csv(file_path):
    with open(file_path,'r',encoding='utf-8') as file:

        header=next(file).strip()
        print(f"[DEBUG] HEADER Detected : {header}")
        for line in file:
            yield line.strip()
