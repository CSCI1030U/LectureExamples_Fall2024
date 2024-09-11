kid_age = 11
if kid_age < 11:
    print('No way, sorry.  Keep it in the dock.')

kid_age = 7
if kid_age < 11:
    print('Yes, but keep the switch in the dock.')
else:
    print('Yes, and you can take with you if you want.')

# equivalent to (more prone to error, more work for me):
if kid_age < 11:
    print('Yes, but keep the switch in the dock.')
if kid_age >= 11:
    print('Yes, and you can take with you if you want.')

kid_age = 7
if kid_age < 8:
    print('No gaming PC for you.')
elif kid_age < 12:
    print('You need to be supervised.')
else:
    print('Go right ahead.')
