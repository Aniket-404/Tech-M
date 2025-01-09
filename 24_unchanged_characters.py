def unchanged_characters(s):
    reversed_s = s[::-1]
    unchanged = []
    for i in range(len(s)):
        if s[i] == reversed_s[i]:
            unchanged.append(s[i])
    print("".join(unchanged))

input_string="hello"
unchanged_characters(input_string)