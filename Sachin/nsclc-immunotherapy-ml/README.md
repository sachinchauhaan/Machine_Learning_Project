NSCLC immunotherapy helper for metastatic NSCLC.

Problem: use basic clinical markers to predict durable clinical benefit (1) versus no durable benefit (0) and guide immunotherapy choices.
Dataset: place a data.csv file in the project root with columns age, sex, smoking_status, pd_l1, tmb, kras_mutated, egfr_mutated, benefit. Missing rows are dropped and categorical fields are encoded manually.
Training: run python ml/preprocess.py then python ml/train_model.py to build processed data and fit both logistic regression and random forest, saving the random forest as ml/model.pkl.
Model use: start the API with python backend/app.py, open frontend/index.html, fill the short form, and submit to see the predicted probability and text recommendation.
