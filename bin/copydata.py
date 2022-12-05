# import sqlite3
import json
import sqlite3

correct_word_file = open("./share/correct.json")
correct_word = json.load(correct_word_file)

valid_word_file = open("./share/valid.json")
valid_word = json.load(valid_word_file)


connection = sqlite3.connect('./var/wordleGame.db')
cursor = connection.cursor()


correct_str = 'insert into Correct_Words(correct_word) values '
for i in list(correct_word):
    correct_str += '("'+ i +'"),'
correct_str = correct_str[:-1] + ';'


valid_str = 'insert into Valid_Words(valid_word) values '
for i in list(valid_word):
    valid_str += '("'+ i +'"),'
valid_str = valid_str[:-1] + ';'

cursor.execute(correct_str)
cursor.execute(valid_str)


# Closing file
connection.commit()
correct_word_file.close()
valid_word_file.close()
