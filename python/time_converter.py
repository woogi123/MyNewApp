time = 12345

h = time // 3600
m = (time % 3600) // 60
s = time % 60

print(f"12345초는 {h}시간 {m}분 {s}초입니다.")