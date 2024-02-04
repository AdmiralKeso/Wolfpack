#Global variable for grid
world_grid = [[]]
#Global variable for grid size
world_grid-size = 14
#Global variable for number of ships
ship_num = 3
#Global variable for game over
game_over = False
#Global variable for number of ships sunk
ship_destroyed = 0
#Global variable for ship position
ship_position = [[]]
#Global variable for alphabet
alphabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ

def grid_ship_placement(start-row, end-row, start-col, end-col):
    #This will check the column or row to see if there can be a ship placed
    global world_grid
    global ship_position

    if (
        start_row < 0
        or end_row >= world_grid
        or start_col < 0
        or end_col >= world_grid
    ):
        print("Please place ship inside boundary of the board.")

    checked = True
    for r in range(start-row, end-row):
        for c in range(start-col, end-col):
            if world_grid[r][c] != ".":
                checked = False
                break
    if checked:
        ship_position.append(start-row, end-row, start-col, end-col)
        for r in range(start-row, end-row):
            for c in range(start-col, end-col)
                world_grid[r][c] = "0"
    return checked