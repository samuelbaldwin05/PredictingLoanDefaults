  This project aims to predict bank loan defaults using a comprehensive kaggle dataset of
45,000 loan applicants, leveraging exploratory data analysis (EDA), feature engineering, and
machine learning. We employ Kernel Density Estimation (KDE) to quantitatively analyze feature
distributions, identifying key discriminators (e.g., credit_score, loan_int_rate) through KL
divergence and distribution overlap metrics. Additionally, PCA was used to explore the
possibility of reducing components.


  We compare multiple algorithms, including KNN, Random Forest, Logistic Regression,
and SVM, with Random Forest achieving the highest accuracy (93%). Feature importance
analysis reveals that income, loan-to-income ratio, and prior defaults are critical predictors.
Additionally, we detect potential biases (e.g., gender-based income disparities) and data quality
issues (e.g., unrealistic ages) using KDE-based outlier detection.


Read Predicting Bank Loan Approval.pdf (Paper) for further information.


Collaborated with Eduardo Ruiz
