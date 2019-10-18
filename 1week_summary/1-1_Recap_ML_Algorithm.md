# Coursera Kaggle 강의 (Week 1. 요약)
## Competition mechanics

### Linear Model
- 대표적인 모델
  - Try to seperate objects with a plane which divides space into two parts.
  - SVM(Support Vector Machine), LR(Linear Regression)
  - SVM과 LR 모델은 서로 다른 loss 함수를 가지고 있음.
  - 특히 SVM은 Sparse high dimensional data에 좋은 성능을 가지고 있음.
  - 비선형 문제는 해결하지 못함.

### Tree-based Model
- Tree based models can combined together in a lot of ways.
- Tree based model are very powerful and can be a good default method for tabular data.
- Tree-based methods are hard to capture linear dependencies since it requires a lot of splits
- Decision Tree, Random Forest, GBDT, xgboost, LightGBM.
- 선형 문제로 쉽게 해결 되는 문제에 적용할 경우, 훨씬 복잡해질 수 있으며, 정확성도 떨어질 우려가 있다.

### K-NN (K-Nearest Neighbors)
- 결측값(Missing) Value를 채울 때, K-NN으로 가능
- Sklearn의 KNN 라이브러리가 성능이 괜찮음.
- Update와 Calculate 함수를 활용하여, Cluster(군집)내의 Mean 값과의 Distance에 따라서 label이 할당된다.

### Neural Network
- 정형 및 비정형 데이터에 모두 사용이 가능
- Black Box 방식으로 계산
- Tensorflow, Keras, MXNet, Pytorch(추천).

### Summary
- Linear model can be imagined as splitting space into two sub-spaces separated by a hyper planes(Decision Boundary).

- Tree based models split space into boxes and use constant predictions in every box.

- K-NN  are based on the assumption that close objects are likely to have same label.
  - its approaches heavily relies on how to measure closeness.

- NN are harder to interpret but they produce smooth non-linear decision boundary.

- 가장 강력한 방법은 Gradient Boosted Decision Tree와 NN
  - Dataset과 도메인이 모두 다르기 때문에, 치킨런 모델은 존재하지 않는다.
