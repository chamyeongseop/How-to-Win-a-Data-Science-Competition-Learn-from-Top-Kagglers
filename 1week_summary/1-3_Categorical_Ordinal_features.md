# Categorical and Ordinal features.

## Ordinal features
- Categorical 의미 + 순서(Ranking) 의미가 합한 형태
  - 최종 학력, 등급

- Tree based model과 Non-tree based model에서 각각의 Feature(Categorical, Ordinal)들을 다루는 방법이 모두 다르다.

## Label Encoding
- 각각의 Categorical Value별로 코드 값을 부여해준다.
- 'sklearn.preprocessing.LabelEncoder'
  - 알파벳 순서 또는 정렬된 순서대로 인코딩을 진행한다.
  - [S, C, Q] -> [2, 1, 3]
- Pandas.factorize.
  - sklearn보다 속도가 빠르며, 순서를 고려하지 않고, 인코딩을 진행한다.
  - [S, C, Q] -> [1, 2, 3]

## Frequence Encoding
- 빈도 수를 기반으로 인코딩을 한다.
- Linear, Tree based model에 모두 효과적이다.
- 빈도 수가 Target과 연관 관계가 있다면 유용하게 사용될 수 있다.
- 빈도수가 비슷한 Feature에서는 효과가 거의 없다.

## One-hot encoding
- Linear 모델에 효과적이지만, Tree 모델에서는 상대적으로 효율이 떨어진다.
- 메모리 이슈로 인해, Feature가 많을 경우에는 효율이 많이 떨어지며, 학습이 어렵고, 속도가 현저히 떨어진다.
- 2가지 이상의 Categorical Feature들을 결합하여 사용할 경우, 효과적이다.(KNN, Linear)
