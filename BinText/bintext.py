from conversion.convert import bitxt, txtbi
from Arts.arts import art
import os

def clear():   
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def main():
    try:
        clear()

        print(art["mainpage"])
        options = input("Option (1 or 2): ")

        while options not in {'1', '2', 'r'} or not options:
            options = input("Enter valid option (1 or 2): ")

        if options == 'r':
            main()

        elif options == '1':
            def opt1():
                clear()
                print(art["b2t"])
                
                def check(bi):
                    if bi == 'r': return True

                    for i in bi:
                        if i not in {'0', '1', ' '} or not bi:
                            return False
                        
                    return True

                while True:
                    uinput = input("Enter the binary code: ").lower()


                    if ' ' not in uinput:
                        uinput = ' '.join(uinput[i:i+8] for i in range(0, len(uinput), 8))

                    if check(uinput):
                        break

                if uinput == 'r':
                    main()
                
                uinput = uinput.split(' ')
                print(bitxt(uinput))


                again = input("Again (y/N  'ctrl + c' to quit)? ").lower()

                while again not in {'y', 'n', 'r'} or not again:
                    again = input("Again (y/N  'ctrl + c' to quit)? ").lower()

                if again == 'y':
                    clear()
                    opt1()
                
                elif again in {'n', 'r'}:
                    main()
            
            opt1()

        elif options == '2':
            def opt2():
                clear()
                print(art["t2b"])

                txt = input("Enter your text: ")

                while not txt:
                    txt = input("Enter your text: ")

                if txt == 'r':
                    confirmation = input("Do you want to return (y/N)? ").lower()

                    while confirmation not in ('y', 'n') or not confirmation:
                        confirmation = input("Do you want to return (y/N)? ").lower()

                    if confirmation == 'y':
                        main()

                    elif confirmation == 'n':
                        txt = "r"

                print(txtbi(txt))

                again = input("Again (y/N  'ctrl + c' to quit)? ").lower()

                while again not in {'y', 'n', 'r'} or not again:
                    again = input("Again (y/N  'ctrl + c' to quit)? ").lower()

                if again == 'y':
                    clear()
                    opt2()
                
                elif again in {'n', 'r'}:
                    main()
                
            opt2()

    except KeyboardInterrupt:
        clear()
        return
    
    except Exception as e:
        print(f"Program has been inturrupted! Error: {e}")
        return


if __name__ == '__main__':
    main()