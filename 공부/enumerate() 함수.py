modulation = input("Key를 입력해주세요 \n(변조가 있으면 , Key를 입력해주세여) : ").split(",")

keys = {}
for i in range(1, len(modulation)):
    keys[f'key{i}'] = modulation[i].strip()

# 동적으로 생성된 키를 출력
for key_name, key_value in keys.items():
    print(f'{key_name} = {key_value}')
    
keys["key1"]
