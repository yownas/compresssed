# compresssed
Compress-sed. Compress text in a way that it can be uncompressed with sed.

I have no idea who would want to use anything like this. It is a tool that reads stdin and tries to convert the input to a sed-script that hopefully is shorter.


    # a="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!"
    # echo $a | ./compresssed.py 
    We will use there chars to compress:
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    Shrank: 35 bytes
    s/^.* #//;s/0/AAAAAAAAAA/g; #000000AH!


    # b="s/^.* #//;s/0/AAAAAAAAAA/g; #000000AH!"
    # echo $b
    s/^.* #//;s/0/AAAAAAAAAA/g; #000000AH!
    # echo $b | sed "$b"
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!
    # echo $a
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!

It will probably have problems with input that has comments (#) and newlines in them.
