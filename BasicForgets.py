import sys
import wandb
import logging
import pickle
sys.path.append('../')
import numpy as np
from pyBKT.models import Model
np.seterr(divide='ignore', invalid='ignore')

if __name__ == '__main__':
    # wandb.init(
    # project="BKT",
    # name="trial-df1",)
    # Open a file for writing
    logging.basicConfig(filename='output_sem1.log', level=logging.INFO)
    logger = logging.getLogger()

    # Now, log messages to the file
    
    # steam_file = open('output_df1.txt', 'w')
    # # Save the current sys.stdout so you can restore it later
    # original_stdout = sys.stdout
    # # Redirect sys.stdout to the file
    # sys.stdout = steam_file
    model = Model(seed = 0, num_fits =10)
    model.fit(data_path = "data/course_sem1_bkt_train.csv")
    # model_file = "model_df1.pkl"
    # with open(model_file, "wb") as file:
    result="Standard BKT:"+str(model.evaluate(data_path = "data/course_sem1_bkt_test.csv", metric="auc"))
    print(result)
    logger.info(result)
    file_path = "sem1.txt"
    with open(file_path, "w") as file:
        file.write(result)
    # wandb.log({"Standard BKT:": result})
    # wandb.finish()
    # model2 = Model(seed = 0, num_fits = 20)
    # model2.fit(data_path = "data/builder_train_preprocessed.csv", forgets=True)
    # print("BKT+Forgets:", model2.evaluate(data_path = "data/builder_test_preprocessed.csv", metric="auc"))
