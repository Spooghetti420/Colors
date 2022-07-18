from colors import *

def main():
    printc("==Colors==", BOLD, WHITE)
    printc("Beautiful, pure white text", WHITE)
    printc("Red bold text", BOLD, RED)
    printc("Yellow bold text", BOLD, YELLOW)
    printc("Green bold text", BOLD, GREEN)
    printc("Blue bold text", BOLD, BLUE)
    printc("Underlined text", UNDERLINE)
    print("Unaffected remainder text")

    printc("Black text on white background", BLACK, WHITE_BG)
    print()
    printc(" "*10, RED_BG)
    printc(" Rainbow! ", BLACK, BOLD, YELLOW_BG)
    printc(" "*10, GREEN_BG)
    printc(" "*10, BLUE_BG)

if __name__ == "__main__":
    main()