import sys


def intial_phonebook ():
    rows, columns = int(input("please enter intial number of contacts")), 5

    phone_book = []
    print(phone_book)
    for i in range (rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))

        print("NOTE: * indicates mandatory fields")

        print("....................................................................")
        temp = [] 
        for j in range(columns):

            if j == 0:
                if temp [j] ==' 'or temp[j]==' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
           
            if j == 1:
                        temp.append(int(input("enter number*:")))

            if j == 2:
                        temp.append(int(input("enter email addres*:")))

                        if temp [j] == ' 'or temp[j] == ' ':
                              temp[j] = None
                              

            if j == 3:
               temp.append(int(imput("enter your date of birth(dd/mm/yy)*:   ")))
            if temp[j] == '' or temp[j] == '':
              temp[j] 
                          
             if j == 4:
               temp.append(int(imput(" enter category(family/freinds/work others))*:   "))) 



        phon_book.append(temp)           
