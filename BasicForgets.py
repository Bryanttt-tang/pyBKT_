import sys
sys.path.append('../')
import numpy as np
from pyBKT.models import Model
np.seterr(divide='ignore', invalid='ignore')

if __name__ == '__main__':
    model = Model(seed = 0, num_fits = 10)
    model.fit(data_path = "data/comb_df_1_train.csv")
    print(model.params())
    preds_df = model.predict(data_path = 'comb_df_1_train.csv') # prediction on training set
    preds_df.to_csv('pred_df1.csv', index=False)
    print("Standard BKT:", model.evaluate(data_path = "data/course4_bkt_test.csv", metric="auc"))
    # model2 = Model(seed = 0, num_fits = 20)
    # model2.fit(data_path = "data/builder_train_preprocessed.csv", forgets=True)
    # print("BKT+Forgets:", model2.evaluate(data_path = "data/builder_test_preprocessed.csv", metric="auc"))
