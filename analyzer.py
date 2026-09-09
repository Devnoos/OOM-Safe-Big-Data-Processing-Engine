# this file objective -> Ye tumhare project ka "Brain" hai. Ek Data Analyst ka kaam sirf data padhna nahi, usme se insights (patterns) nikalna hota hai. Hum check karenge ki in 10 lakh transactions mein total kitna paisa process hua, aur kitne frauds the.

import gc
from chunk_reader import read_massive_csv

def analyze_fraud_data(file_path):
    total_transactions = 0
    total_revenue = 0
    fraud_count = 0
    for line in read_massive_csv(file_path):
        data = line.split(',')
        total_transactions+=1
        amount= float(data[2])
        if  amount>=5000:
            fraud_count+=1
        else:
            total_revenue += amount
        if total_transactions % 100000 == 0:
            print(f"[SYSTEM] Processed {total_transactions} rows... GC running.")
            gc.collect()

    print(f"Total Trasactions : {total_transactions} , Total Revenue : {total_revenue} , Fraud_count : {fraud_count}")

print("--Final Analytics Reports--")
print(analyze_fraud_data("massive_data.csv"))