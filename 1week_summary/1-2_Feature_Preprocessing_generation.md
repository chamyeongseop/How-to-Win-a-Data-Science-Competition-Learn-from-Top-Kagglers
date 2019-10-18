# Feature preprocessing and generation with respect to models
- Feature preprocessing
- Feature generation

## Numeric features
- Non-tree
  - Linear, K-NN 모델은 scaling에 따라 결과값이 변할 수 있다.(L2 Distance)
    - 특정 feature 값에 0의 값을 곱해버리면, 모델에서는 특정 feature 값을 무시해버린다.
    - 특정 feature 값에 큰 값을 곱해버리면, feature 내에서의 약간의 차이가 Prediction 성능에 큰 영향력을 미친다.
  - Feature Scaling의 종류
    - MinMax
      - 범위가 규정된 경우에 사용하거나 Outlier가 없는 경우에 사용한다.
      - 'sklearn.preprocessing.MinMaxScaler'
      - X = (X X.min()) / (X.max() X.min())

    - Standard : PCA를 적용할 때, 사용되며, 평균은 0으로, 표준 편차는 1로 설정된다.
      - 'sklearn.preprocessing.StandardScaler'
      - X = (X X.mean()) / X.std()
      - We use preprocessing to scale all features to one scale, so that their initial impact on the model will be roughly similar.

  - Outlier
    - Upper Bound와 Lower Bound를 설정하여 1 ~ 99% 범위 내에 있는 데이터만 사용한다.
    - np.percentile을 이용하여, Outlier를 제거하는 것이 효과적이다.

  - Rank transformation
    - Outlier가 데이터에 많이 존재한다면, MinMax보다 좋은 성능을 나타날 수 있다.
    - Linear models, KNN, Neural nets에서 전처리 할 시간이 부족하다면 Rank Transformation이 효과적인 방안이 될 수 있다.
    - Sorting을 한 후, Indexing 기법을 활용하여, Labelling을 한다.
      [1000, 1, 10] -> [2,0,1]
    - 'scipy.stats.rankdata'

  - Log transformation
    - 'np.log(1+x)'
    - Raising to the power < 1
      - np.sqrt(x+2/3)

    - New feature generation
      - 데이터에 대한 지식이 필요하며, EDA(Explore Data Analysis)를 적극 활용한다.
      - 기존의 Feature들을 사칙연산을 활용하여, 새로운 Feature들을 생성한다.
        - 평당 가격, 월 수익, 대각선 거리 등등
