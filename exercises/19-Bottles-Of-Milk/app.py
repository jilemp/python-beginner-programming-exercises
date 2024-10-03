# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(99,-1, -1):
        lyrics = ''
        if i == 2:
            lyrics += '2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.'
        elif i == 1:
            lyrics += '1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.'
        elif i == 0 :
            lyrics += 'No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.'
        else:
            lyrics += str(i) + ' bottles of milk on the wall, ' + str(i) + ' bottles of milk. Take one down and pass it around, ' + str(i-1) + ' bottles of milk on the wall.'
        print(lyrics)

number_of_bottles()