# Universitaet Leipzig (WS20/21)
# Modul: WISSENSCHAFTLICHES PROGRAMMIEREN IN R
# Autor: Max Beining

library('plot.matrix') # Plot-Matrix
rm(list = ls()) # Clear all Variables

#==========================================================
#--------------------------------------
# SETTINGS
# World, Number of cells and generations
n_world = 50
cells = 800
generations = 50

#--------------------------------------
#==========================================================

######### START CODE #########
check_cell_state = function(n, m) {
  counter = 0
  # Check all neighbors of current cell
  for (i in -1:1) {
    for (j in -1:1) {
      # Try() for index out of range (Argument length = 0, be silent)
      try({
        if (world[n+i, m+j] == 1){
          counter = counter + 1
        }
      }, silent = TRUE)
    }
  }
  
  counter = counter - world[n, m] # minus self-state
  # Conditions for GoL
  # 1) Cell dies in next Gen. Under-Population
  if (counter < 2){
    return (0)
  }
  # 2) Cell stay alive in next Gen. Love
  else if ((counter == 2 | counter == 3) & world[n,m] == 1 ) {
    return (1)
  }
  # 2) Cell dies in next Gen. Over-Population
  else if (counter > 3) {
    return (0)
  }
  # 3) New living Cell is born
  else if (counter == 3 && world[n,m] == 0) {
    return (1)
  }
  # 4) Dead stays dead
  else {
    return (0)
  }
}

world <<- matrix(data = 0, nrow = n_world, ncol = n_world)
# Create Cells with random location
loc = sample(1:(n_world*n_world), cells, replace=FALSE)
for (i in loc) {
  world[i] = 1 # Matrix can be interpreted as a list with n*n entries
}

plot(world, col = c('white', 'blue'),
     main = paste("Generation 0", "\t", "Living Cells: ", cells),
     border = "grey", key = NULL, col.axis="white", col.lab = "white")

#------------------------------------------------
#------------------------------------------------
# Game of Life will begin

for (tick in 1:generations){

  start_time = Sys.time()

  # Cell Locations and states, empty lists, living cell counter
  row_seq = c()
  col_seq = c()
  states = c()
  living_cells = 0

  # Loop over all Cells in World
  for (mat_row in 1:n_world){
    for (mat_col in 1:n_world){
      # Check current and next State
      current_state = world[mat_row, mat_col]
      next_state = check_cell_state(mat_row, mat_col)
      # State update ?
      if (next_state != current_state) {
        states = c(states, next_state)
        row_seq = c(row_seq, mat_row)
        col_seq = c(col_seq, mat_col)
        }

      if (next_state == 1) {
        living_cells = living_cells + 1
        }

    }
  }

  # Update all Cell-States if they changes, iterate over (row,col) lists
  for (c in 1:length(states)) {
    world[row_seq[c], col_seq[c]] = states[c]
  }

  end_time = Sys.time()

  cat("Process ", tick, "\t","|", "Time: ", end_time - start_time, "\n")

  title = paste("Generation ", tick, "\t", "Living Cells: ", living_cells)
  plot(world, col = c('white', 'blue'), main = title, cex = 0.8,
       border = "grey", key = NULL, col.axis="white", col.lab = "white")

  # Break Condition if living cells = 0
  if (living_cells == 0) {
    print("All Cells are Dead!"); break }

  Sys.sleep(0.5)
}

