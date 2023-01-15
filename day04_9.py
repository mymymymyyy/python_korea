# 세트 set = {}
# 중복이 안됨
# 중복된 값을 추가하려하면 무시
s = set({})
s2 = {'a','c','e'}

# 추가 add
s.add('a')
s.add('b')
s.add('a')
s.add('c')
s.add('d')

# 뺴기 remove
s.remove('d')

print(s)
print(s2)

# set(중복x)
# 교집함 (set 중 일치하는 값만)
s_kyo = s & s2
print(s_kyo)

# 합집함
s_sum = s | s2
print(s_sum)

# 차집함 (s에만 있고 s2 에는 없는 것)
s_sub = s - s2
print(s_sub)