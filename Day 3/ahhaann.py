import qrcode
print('''
                     _.---.(       ..--._)
     (_.'       `''-.'`      `'.
      /            /            \_)
   (_|    _,.-'""'-,-'""'-.,_   |
      \  /.--'           '--.\  /_)
    ,__\ ) (_(_(       )_)_) ) /__,
     \  (_, (  o)      (  o) /    /
     `--.-`  '-'   c    '-'  `-'-`
       (O\                   (O)
          '-.....__w__.....-'
          .-'             '-.
         /   , .--.  .--._   |
        /   / (    \/    )`\  |
       /   / \ \        /   \  |
       \  \   \ |      (    /  /
        `\ `.  \/       \  /\/
          `.//.'         '-; |
            |/             \/
            /               |
         ,_/ _,--,_  __,--,_ \_,
         `--' \    ``|    / '--'
               `.    |===/
                 >   |   |
                 /   |   |
                |    |   |
                |    Y  /
                \   /  /
                 | /| /
         jgs    / / / |
               /=/  |=/
               `"`  `"`
''')
print("Welcome to lapaki.com ")
url = 'https://suhailroushan.com'
print("sukham kalige chootu.")
crossroad= input ("do you prefer'small boobs' or 'big boobs'\n ").lower()
if crossroad == "big boobs" :
    print("you naughty! naughty!")
    forest= input("do you want 'aunty' or 'teen'\n" ).lower()
    if forest== "aunty" :
       print ("thats my boii")
       castle= input("how many nights '1 night' '2 nights' and '1 week package'.choose one\n").lower()
       if castle == "1 night" :
         print("lestada re niku. pay$5 ")
       elif castle =="2 nights":
         print("chii po raww .pay$10")
         qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
         qr.add_data(url)
         qr.make()
         img = qr.make_image(fill_color = 'red', back_color = 'yellow')
         img.save('suhail.jpg')


       elif castle =="1 week package":
           print("nuvvu mogoonivi.pay $100")
       else:
           print("pikinav tee")
    else :
       print("noob pro max")
else :
    print("noob")
