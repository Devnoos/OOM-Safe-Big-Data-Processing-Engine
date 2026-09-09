import random
def create_massive_csv(filename,rows=1000000):
    print(f"Generating {rows} rows in {filename}.... please wait.")
    # Headers
    columns = ["Transaction_ID", "User_ID", "Amount", "Status"]

    with open(filename,'w',encoding='utf-8') as file:
        file.write(",".join(columns)+"\n")  # write header 
        for i in range(1,rows+1):
            user_id = random.randint(100,9999)
            if random.random() < 0.01: #Generate 1% Fraud
                amount = round(random.uniform(5000,20000),2)
                status = "FAILED"
            else:
                amount = round(random.uniform(100,1000),2) #normal trasaction
                status = "SUCCESS"
            line = f"TXN{i},{user_id},{amount},{status}\n"
            file.write(line)
    print("Massive CSV generated")

if __name__ =="__main__":
    create_massive_csv("massive_data.csv")
    



    