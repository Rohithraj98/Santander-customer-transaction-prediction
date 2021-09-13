# Santander-customer-transaction-prediction
Santander bank is one of the leading banks in Europe and 16th largest bank institution in the world which has headquarters at Spain founded in 1857. Santander has provided a dataset of the customers which has features like ID_Code and var_0 to 200 depending on that features test data set has a target variable as 0’s and 1’s. similarly we have to train the dataset with the help of test dataset and find the target variable. By do this we can tell which customer will make a specific transaction in future, irrespective of the amount of money transacted. 


Machine learning Model:
Light GBM-
	Light GBM is a fast, distributed, high-performance gradient boosting framework based on decision tress algorithm, used for ranking, classification and many other machine leaning tasks. Since it is based on decision tress algorithms, it splits the tress leaf wise with best fit whereas other boosting algorithms split the tree depth wise pr level wise rather than leaf-wise. So, when growing on the same leaf in the light GBM, the leaf wise algorithm can reduce more loss than the level wise algorithm and hence results in much better accuracy which can be rarely be achieved by any of the existing boosting algorithm. Also, it is surprisingly very fast, hence the word ‘light’.
	
	
Results/Conclusion
	As the results we can say, by using lightGBM model we got accuracy of 98% which is best fit to the dataset.
