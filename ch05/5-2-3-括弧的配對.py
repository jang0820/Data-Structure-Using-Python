s = input()
st = []
pair = 0
for i in range(len(s)):
    if s[i] == '{':
        st.append('{')
    if s[i] == '}':
        if len(st) > 0:
            st.pop(-1)
            pair = pair + 1
        else:
          pair = -1
          break
if  len(st) == 0 and pair >= 0:
    print("共有", pair, "對的大括號")
else:
    print("配對失敗")
