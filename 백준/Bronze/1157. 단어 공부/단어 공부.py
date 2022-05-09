string = input().upper()
cnt = {}

for i in string:
  if i in cnt :
    cnt[i] += 1
  else :
    cnt[i] = 1

val = []
cnt_max = max(cnt.values())
for j, k in cnt.items():
  if k == cnt_max:
    val.append(j)

if len(val) > 1:
  print("?")
else :
  print("".join(val))