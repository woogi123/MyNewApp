id_number = "901212-1234567"

front = id_number.split('-')[0]  # 앞 6자리: 생년월일
year = int(front[:2])
month = front[2:4]
day = front[4:6]

print(f"19{year}년 {month}월 {day}일")