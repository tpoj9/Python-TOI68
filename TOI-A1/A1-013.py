C = input()
D = input()

if C == 'H' and D == '4567':
    print("safe unlocked")
elif C == 'H':
    print("safe locked - change digit")
elif D == '4567':
    print("safe locked - change char")
else:
    print("safe locked")