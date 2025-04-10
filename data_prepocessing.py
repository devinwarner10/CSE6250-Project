import dill
import os
import numpy as np

# EHR Records
records_path = os.path.join('datasets', 'MIMIC3' + '/records_final.pkl')

records = dill.load(open(records_path, 'rb')) # Patients:Visits:(Diag,Proc,Drug)

print("Patient Records:",len(records)) # 6350 

# Remove Patient Dimension
records = [v for r in records for v in r]

print("Visits:",len(records)) # 15032 

# Data Summary Statistics
symptom_set = set()
symptom_counts = []
drug_set = set()
drug_counts = []

# max_symp = 0
# max_proc = 0
# max_drug = 0

for visit in records:
    # Number of Symptoms
    symptom_set = symptom_set | set(visit[0])
    symptom_counts.append(len(visit[0]))
    # if max(visit[0]) > max_symp:
    #     max_symp = max(visit[0])

    # Number of Procedures
    # if max(visit[1]) > max_proc:
    #     max_proc = max(visit[1])

    # Number of Drugs
    drug_set = drug_set | set(visit[2])
    drug_counts.append(len(visit[2]))
    # if max(visit[2]) > max_drug:
    #     max_drug = max(visit[2])

    

print(f"Num of Symptoms: {len(symptom_set)}") # 1958
print(f"Avg Num of Symp: {sum(symptom_counts)/len(symptom_counts)}") # 13.63
print(f"Num of Drugs: {len(drug_set)}") # 112
print(f"Avg Num of Drugs: {sum(drug_counts)/len(drug_counts)}") # 19.57

# print(f"Max Symp: {max_symp}")
# print(f"Max Proc: {max_proc}")
# print(f"Max Drug: {max_drug}")

# Split Data
# Training, Testing, Validation 4:1:1
# Train (10020), Test (2506), Validation (2506)
train = records[:10020]
test = records[10020:12526]
val = records[12526:]

print("Training:",len(train)) # 10020
print("Testing:",len(test)) # 2506
print("Validation:",len(val)) # 2506

# dill.dump(train,open("datasets/MIMIC3/data_train.pkl", "wb"))
# dill.dump(test,open("datasets/MIMIC3/data_test.pkl", "wb"))
# dill.dump(val,open("datasets/MIMIC3/data_eval.pkl", "wb"))

# main_4sdrug.py as is takes 32 minutes to run on Google Colab T4 GPU

# DDI Interactions
ddi_path = os.path.join('datasets', 'MIMIC3' + '/ddi_A_final.pkl')
ddi = dill.load(open(ddi_path, 'rb')) # 

print(f"DDI:{np.sum(ddi)}")
print(ddi)

# # Vocabulary
# voc_path = os.path.join('datasets', 'MIMIC3' + '/voc_final.pkl')
# voc = dill.load(open(voc_path, 'rb')) # 

# print(f"VOC:{voc['diag_voc']}") # diag_voc, med_voc, pro_voc