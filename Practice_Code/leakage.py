# Final Project

# Load dataset
items = pd.read_csv('../intput/items.csv')
shops = pd.read_csv('../input/shops.csv')
cats = pd.read_csv('../input/sales_train.csv')

# set index to id to avoid dropping it later
test = pd.read_csv('../input/test.csv')

train = sales.join(items, on ='item_id', rsuffix='_').join(shops, on='shop_id', rsuffix='_').join(cats, on='item_category_id', rsuffix='_').drop(['item_id', 'shop_id', 'item_category_id'], axis=1)

# axis의 이해
# axis = 0의 값을 rowf(행)를 기준으로 계산 및 함수를 적용한다. (x축)
# axis = 1은 값을 column(열)을 기즌으로 계산 및 함수를 적용한다. (y축)
# axis = 2는 값을 Z축 기준으로 계산 및 함수를 적용한다.
