# CSE6250-Project
This repo contains the work done by Devin Warner and Justin Suen for the final project in CSE 6250 at Georgia Tech in Spring 2025. The purpose of this project was to attempt to reproduce the results of the 4SDrug paper published in as part of ACM SIGKDD in 2022 (see https://github.com/Melinda315/4SDrug).

The .pkl files "ddi_A_final", "ehr_adj_final", "voc_final" and "records_final" were copied from the SafeDrug repository (https://github.com/ycq091044/SafeDrug) as mentioned in the 4SDrug paper. These files are used in "data_preprocessing.py" to create training, testing, and evaluation datasets to by used by 4SDrug.

The Colab Notebook runs the 4SDrug model which is stored on a mounted Google Drive along with the datasets mentioned previously. When testing the model we changed the parameters alpha and beta in the final code block.
