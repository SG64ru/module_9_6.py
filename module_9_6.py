def all_variants(text):
    l_str = len(text)
    for i in range(l_str):
        for j in range(i + 1, l_str + 1):
            yield  text[i:j]

a = all_variants("abc")
for i in a:
    print(i)




