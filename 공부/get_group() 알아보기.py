import pandas as pd
# 그룹 안에 데이터를 확인하고 싶을때 groupby().get_group()을 이용합니다.
# Sample DataFrame
data = {'value': [10, 15, 20, 5, 30, 25]}
df = pd.DataFrame(data)

# Define the threshold to classify values as large or small
threshold = 20

# Group the data based on the threshold
grouped = df.groupby(df['value'] > threshold)

# Retrieve the groups
large_group = grouped.get_group(True)  # grouped 안에 참이 value 값이 20보다 큰 애들을 묶는다.
small_group = grouped.get_group(False) # grouped 안에 거짓인 value 값이 20보다 작은 애들을 묶는다.

print("Large Group:")
print(large_group)

print("\nSmall Group:")
print(small_group)
