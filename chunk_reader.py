# this module objective is to create a memory-safe reader function that can handle files of any size, loading only one line at a time into RAM.

def read_massive_csv(file_path):
    with open(file_path,'r',encoding='utf-8') as file:

        header=next(file).strip()
        print(f"[DEBUG] HEADER Detected : {header}")
        for line in file:
            yield line.strip()
