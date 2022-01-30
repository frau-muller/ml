first_string = 'В еиоен'
second_string = 'ывлклпы'
final_string = ''
for i in range(len(first_string)):
    final_string = final_string + first_string[i]
    final_string = final_string + second_string[i]
# ваш код здесь

print(final_string)