# compresssed
Compress-sed. Compress text in a way that it can be uncompressed with sed.

I have no idea who would want to use anything like this. It is a tool that reads stdin and tries to convert the input to a sed-script that hopefully is shorter.


    # a="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!"
    # echo -n $a | ./compresssed.py 
    We will use these chars as markers:
    0123456789abcdefghijklmnopqrstuvwxyzBCDEFGIJKLMNOPQRSTUVWXYZ
    Shrank: 62 bytes
    s/^.* #//;s/0/AAAAAAA/g; #0000000000000AAH!
    
    Original length: 95
    Final length: 43 (17)
    # b='s/^.* #//;s/0/AAAAAAA/g; #0000000000000AAH!'
    # echo $b | sed "$b"
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!


It will probably have problems with input that has comments (#) and newlines in them. *Shrug* Not my problem.
