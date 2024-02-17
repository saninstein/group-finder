Exercise 1:
Given a list of strings, write a program that groups them based on their prefixes.
We want the group names to be as descriptive as possible.
For example, if I have foo_bar_abc, and foo_bar_xyz, the group name should be foo_bar.

Input: list of strings.
Output: json object where the key is the name of the group and the value is the list of elements within the group.

Example data: Attached file names.csv
(https://drive.google.com/file/d/1JsE9gQSJ4BKrH95htv2L5YV8cd9jEXk6/view?usp=sharing)

Please note:
→ We prefer this to be written in Python.
→ Use standard libraries as much as possible.
→ We don’t want the groups to be nested.
→ The names are not always delimited by underscore (it could be a different special character).


Exercise 2:
Design and create REST API endpoints that the front-end can call (bonus points if you use DRF)
and display the Ex 1 result in a list view with folders.
Allow the user to be able to create new folders and move each name into different folders.

We expect it would take about 3-5 hours to complete both of the exercises.

REST API should include validation and persistent storage.
You can decide what may be the best way to implement the application
(i.e. whether to run word grouping via API or CLI, how the storage structure should look like).
Through this exercise, we’re basically looking to understand your thought process, programming logic,
coding style, and communication (docs/comments).

If you have extra time, you can also make it easy for us to review - dockerize it, host it, etc., so
we can easily test out your application.

FAQ
1. What should be a prefix for `adhoc_charge_amt` and `adhoc_charge_amt_usd`?
Our suggestion is “adhoc_charge_amt”. But this part of the task is open-ended and we
accept anything that’s reasonable (we expect to hear some reasoning too!).
2. Is the prefix always terminated by a special character?
You can assume it is. Prefix won't be terminated by any alphanum character. For the
sake of the exercise, you can define a set of special characters that will be treated as
delimiters (or you can assume one, just make it easy to change what is defined as a
delimiter).
3. Does input data always contain a unique delimiter?
Yes. String like foo_bar.xyz will be treated as two words: foo and bar.xyz instead of 3
words: foo, bar, and xyz
4. Can the group be nested in another group?
No, we want a flat structure of groups with words inside them.
5. Can a word belong to more than one group?
No.
6. Should I create a REST API for “Allow the user to be able to create new folders
and move each name into different folders.”?
Yes.

Follow up questions
1. How do you productionize this application?
2. How do you optimize it to work at a much bigger scale processing millions of words per second?