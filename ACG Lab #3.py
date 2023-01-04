# 1) Set the users variable to be an empty list
users = []

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"

# 2) Add 'Kevin', 'Bob', and 'Alice' to the users list in that order without reassigning the variable.
users.append('Kevin')
users.append('Bob')
users.append('Alice')

assert users == ['Kevin', 'Bob', 'Alice'], f"Expected `users` to be ['Kevin', 'Bob', 'Alice'] but got: {repr(users)}"

# 3) Remove 'Bob' from the `users` list without reassigning the variable.
del users[1]

assert users == ['Kevin', 'Alice'], f"Expected `users` to be ['Kevin', 'Alice'] but got: {repr(users)}"

# 4) Reverse the users list and assign the result to `rev_users`
rev_users = list(reversed(users))

assert rev_users == ['Alice', 'Kevin'], f"Expected `rev_users` to be ['Alice', 'Kevin'] but got: {repr(rev_users)}"

# 5) Add the user 'Melody' to users where 'Bob' used to be.
users.insert(1, 'Melody')

assert users == ['Kevin', 'Melody', 'Alice'], f"Expected `users` to be ['Kevin', 'Melody', 'Alice'] but got: {repr(users)}"

# 6) Add the users 'Andy', 'Wanda', and 'Jim' to the users list using a single command
users += ['Andy', 'Wanda', 'Jim']

assert users == ['Kevin', 'Melody', 'Alice', 'Andy', 'Wanda', 'Jim'], f"Expected `users` to be ['Kevin', 'Melody', 'Alice', 'Andy', 'Wanda', 'Jim'] but got: {repr(users)}"

# 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`
center_users = users[2:4]

assert center_users == ['Alice', 'Andy'], f"Expected `users` to be ['Alice', 'Andy'] but got: {repr(center_users)}"