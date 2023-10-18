# Machine-Learning
## machine-learning models
### linear Regression
### clustering
#### Hierarchical clustering
Hierarchical clustering: Cluster have a tree like structure or a parent child relationship 
- Agglomerative: Bottom up approach: Begin with each element as a separate cluster and merge them into successively larger cluster 
- Divisive: Top Down approach begin with the whole set and proceed to divide it successively smaller clusters. 
#### Partitional clustering 
- K-Means: Division of objects into clusters such that each object is in exactly one cluster, not several  
- Fuzzy C-Means: Division of objects into clusters such that each object can belong to multiple clusters.
### Distance Measure 
Distance Measure: distance measure will determine the similarity between two elements and it will influence the shape the clusters 
- Euclidean distance measure: is the ordinary straight line. It is the distance between two points in Euclidean space
- Squared Euclidean distance measure: matric uses the same equation as the Euclidean distance but does not take the square root.
- Manhattan distance measure: is the simple sum of the horizontal and vertical components or the distance between two points along axes at right angles.  
- Cosine distance measure: similarity measures the angle between the two vectors. 

- <img width="727" alt="截屏2023-10-14 18 13 57" src="https://github.com/Felicia1993/Machine-Learning/assets/22839284/05f18377-53ee-4da5-918b-5f7d3271def2">

### Decision Tree
Decision Tree is a tree shape diagram used to determine a course of action. Each branch of the tree represents a possible decision, occurrence or reaction. 
#### Problems decision tree can solve
- Classification: a classification tree will determine a set of logical if-then condition to classify problem. For example, discriminating between three types of flowers based on certain features. 

- Regression: Regression tree is used when the target variable is numerical or continues in nature. We fit a regression model to a target variable using each independent variables. Each splits is made based on the sum of squared error.
#### Advantages of Decision Tree 
- Simple to understand and interpret and visualize 

- Little effort required for data preparation 

- Can handle both numerical and categorical data 

Non linear parameters don't effect its performance 
#### Disadvantages of Decision Tree 
- Overfitting occurs when algorithm captures noise in the data 

- High variance: The model can get unstable due to small variation in data. 

- A highly complicated decision tree trends to have a low bias which makes it difficult for the model to work with new data.

### Random Forest
Advantage of Random Forest 
- No overfitting:
	- Use of multiple trees reduces the risks of overfitting
	- Training time is less
- High accuracy:
	- Runs efficiently on large databases
	- For large data, it produce highly accurate predictions  
  

- Estimate missing data: 
	- Random Forest can maintain accuracy when a large proportion of data is missing

Random Forest or random decision forest is a method that operates by constructing multiple Decision trees during training phase. The decision of the majority of the trees is chosen by the random forest as the final decision. 

#### Decision Tree 
Decision Tree is a tree shaped diagram used to determine a course of action. Each branch of the tree represents a possible decision, occurrence or reaction. 

##### Important Terms 
**Entropy**: Entropy is the measure of randomness or unpredictability in the dataset. 
**Information gain**: It is the measure of decrease in entropy after the dataset is split. 
**Leaf node**: carries the classification or the decision 
**Decision node**: has 2 or more branches 
**Root node**: The top most decision node is known as the root node.  


 
