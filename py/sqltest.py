import pymysql


def findItem(idNum):
      sql = "select * from question where id = '\d' " % (idNum)
      return sql

Title = "Remove 9"
Title_slug = "remove-9"
Question_ID = 660
Difficulty_level = 3
Paid = "False"
description = """Start from integer 1, remove any integer that contains 9 such as 9, 19, 29... 
So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...
Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.
Example 1:
Input: 9
Output: 10
 Hint: n will not exceed 9 x 10^8."""


db = pymysql.connect("localhost","testuser","test123","leetcode")
cursor = db.cursor()
sql = "INSERT INTO question (id, title, paid, difficulty, description) VALUE('%d','%s','%s','%d','%s') " % \
      (Question_ID, Title, Paid, Difficulty_level, description)
print(cursor.execute("select * from question where id = 660 "))
db.commit()
db.close()