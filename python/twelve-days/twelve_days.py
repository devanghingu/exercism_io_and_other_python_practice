
default_stmt="On the {0} day of Christmas my true love gave to me: {1}"
song=["a Partridge in a Pear Tree.","two Turtle Doves, ","three French Hens, ","four Calling Birds, "
,"five Gold Rings, ","six Geese-a-Laying, ","seven Swans-a-Swimming, ","eight Maids-a-Milking, "
,"nine Ladies Dancing, ","ten Lords-a-Leaping, ","eleven Pipers Piping, ","twelve Drummers Drumming, "]
days=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
daywithnum = dict(zip(range(1,13),days))

def join_song(num):
    final_song=song[num-1::-1]
    if(num > 1):
        final_song[-1]="and " + final_song[-1]
    return default_stmt.format(daywithnum[num],"".join(final_song))
    
def recite(start_verse, end_verse):
    return [join_song(i) for i in range(start_verse,end_verse+1)]
    #     mainsong+=join_song(i)        
    # return [mainsong]


expected = [recite(n, n) for n in range(1, 4)]
print(expected,"\n\n")
print(recite(3, 3))