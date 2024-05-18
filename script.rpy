# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color= "#45b6be")

transform middle:
    xalign 0.5
    yalign 0.6


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music refract loop fadein 0.5 volume 0.15

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "btw, what do u wanna be?"

    menu:
        "What do you want to be?"

        "A genius":
            t "A genius?"

            t "I see..."

            t "By choice... right?"
            jump a_genius
    
        "A leader":
            t "So you wish to lead?"

            t "To command others?"

            t "But respect is required for a leader,"
            jump a_leader

    # This ends the game.

    return
