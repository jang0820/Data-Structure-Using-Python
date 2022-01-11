s = input().split()
st = []
for i in range(len(s)):
    if s[i] == '+':
        x = st.pop(-1)
        y = st.pop(-1)
        st.append(y+x)
    elif s[i] == '-':
        x = st.pop(-1)
        y = st.pop(-1)
        st.append(y-x)
    elif s[i] == '*':
        x = st.pop(-1)
        y = st.pop(-1)
        st.append(y*x)
    elif s[i] == '/':
        x = st.pop(-1)
        y = st.pop(-1)
        st.append(y/x)
    else:
        st.append(int(s[i]))
print(st[0])
