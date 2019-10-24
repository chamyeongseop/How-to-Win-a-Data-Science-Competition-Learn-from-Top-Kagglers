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

# Time lag 설정

time_shift = [1,2,3,4,5,6]

for lag in time_shift:
    ft_name = ('item_cnt_shifted%s' % lag)
    train_monthly[ft_name] = train_monthly.sort_values('date_block_name').groupby(['shop_id', 'item_category_id', 'item_id'])['item_cnt'].shift(lag)

    # Fill the empty shifted features with 0
    train_monthly[ft_name].fillna(0, inplace = True)
