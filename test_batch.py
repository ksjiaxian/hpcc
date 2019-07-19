import random
with open('test_batch_output.txt', 'w', newline="\n", encoding='utf-8') as txt_file:
    txt_file.write('heyo ' + str(int(random.random() * 100)))
    