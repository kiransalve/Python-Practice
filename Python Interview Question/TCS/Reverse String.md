# Write a program to reverse a string using a for loop (don’t use slicing).
word = "TCS"
rev = ""
for w in str(word):
    rev = w + rev
rev

Explanation :

| Step | char  | reversed_string (before) | Operation (`char + reversed_string`) | reversed_string (after) |
| ---- | ----- | ------------------------ | ------------------------------------ | ----------------------- |
| 1    | `'h'` | `""`                     | `'h' + ""`                           | `'h'`                   |
| 2    | `'e'` | `'h'`                    | `'e' + "h"`                          | `'eh'`                  |
| 3    | `'l'` | `'eh'`                   | `'l' + "eh"`                         | `'leh'`                 |
| 4    | `'l'` | `'leh'`                  | `'l' + "leh"`                        | `'lleh'`                |
| 5    | `'o'` | `'lleh'`                 | `'o' + "lleh"`                       | `'olleh'`               |
