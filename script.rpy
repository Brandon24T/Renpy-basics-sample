# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mary Anne Funk", color= "#45b6be")

transform middle:
    xalign 0.5
    yalign 0.6


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene space background
    play music refract loop fadein 0.5 volume 0.15

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mary happy at middle

    # These display lines of dialogue.

    "Mary" "Welcome to class"

    m "Let's see if you can press buttons!"

    menu:
        "will you click yes or no for me?"

        "yes":
            "Good it works!"
            jump it_works
        
        "no":
            "But.. u just clicked no..."
    
    return
        
    label it_works:
    m "let's get you back to the main menu for now."

    # This ends the game.

    return
