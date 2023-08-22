import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Defining levels
levels = [
    """
############
#         *#
#         D#
#P         #
#         D#
#         *#
############
"""
]

def drawSokobanLevel(level):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.set_xlim(0, len(level[0]))
    ax.set_ylim(0, len(level))
    ax.axis('off')

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            if cell == '#':
                ax.add_patch(patches.Rectangle((x, len(level) - y - 1), 1, 1, color='black'))
            elif cell == 'P':
                ax.add_patch(patches.Circle((x + 0.5, len(level) - y - 0.5), radius=0.3, color='blue'))
            elif cell == 'D':
                ax.add_patch(patches.Rectangle((x, len(level) - y - 1), 1, 1, facecolor='yellow', edgecolor='black'))
            elif cell == '*':
                ax.add_patch(patches.Circle((x + 0.5, len(level) - y - 0.5), radius=0.3, color='brown')) # Changed color to brown for the box

    plt.show()

# Drawing the levels
for level in levels:
    drawSokobanLevel(level.strip().split('\n'))
