user_input = input("4자리의 정수 입력: ")

# 각 자리수를 반복문으로 처리
for digit in user_input:
    total += int(digit)  # 각 자리수를 정수로 변환하여 합산

print(f"자리수의 합: {total}")
