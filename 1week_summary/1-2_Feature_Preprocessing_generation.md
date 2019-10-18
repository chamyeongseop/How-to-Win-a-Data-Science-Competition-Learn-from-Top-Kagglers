# Feature preprocessing and generation with respect to models
- Feature preprocessing
- Feature generation

## Numeric features
- Non-tree
  - Linear, K-NN 모델은 scaling에 따라 결과값이 변할 수 있다.(L2 Distance)
    - 특정 feature 값에 0의 값을 곱해버리면, 모델에서는 특정 feature 값을 무시해버린다.
    - 특정 feature 값에 큰 값을 곱해버리면, feature 내에서의 약간의 차이가 Prediction 성능에 큰 영향력을 미친다.
  - Feature Scaling의 종류
    - MinMax : Range가 규정된 겨웅에 사용하거나 Outlier가 없는 경우에 사용한다.
    - Standard : PCA를 적용할 때, 사용한다.
    - We use preprocessing to scale all features to one scale, so that their initial impact on the model will be roughly similar.

  - Outlier
    - Upper Bound와 Lower Bound를 설정하여 1 ~ 99% 범위 내에 있는 데이터만 사용한다.

  - Rank transformation
    - Outlier가 데이터에 많이 존재한다면, MinMax보다 좋은 성능을 나타날 수 있다.
    - 'scipy.stats.rankdata' 명령어를 통해 사용하며, Test를 할 때도 동일한 Rank value를 적용한다.
