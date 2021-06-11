let Game = {
    isGameWon: false,
    currentTurn: 'O',
    valid_values: ["X", "O"],
    ResetGame: () => {
        cells.forEach(cell => {
            cell.innerHTML = '';
        });
        Game.currentTurn = 'O';
        Game.isGameWon = false;
    },
    SwitchTurn: () => {
        if (!Game.isGameWon) {
            Game.currentTurn = (Game.currentTurn === 'O') ? Game.currentTurn = 'X' : Game.currentTurn = 'O';
        }
    },
    CheckIfWon: () => {
        //Chech horizontal 
        if (Game.checkRows() || Game.checkColumns() || checkDiagonals()) {
            alert(`${Game.currentTurn} won the game`);
            Game.isGameWon = true;
        }
    },
    OnClickCell: (cell) => {
        if ((!Game.isGameWon) && (!Game.valid_values.includes(cell.innerHTML))) {
            console.log("Checking if the listener is working. ")
            cell.innerHTML = Game.currentTurn;
            console.log(cell.innerHtml);
            Game.CheckIfWon();
            Game.SwitchTurn();
        }
    },
    checkRows: () => {
        for (let i = 0; i < 3; i++) {

            let cell1 = getCell(i, 0).innerHTML;
            let cell2 = getCell(i, 1).innerHTML;
            let cell3 = getCell(i, 2).innerHTML;
            if (checkIfAllEqual([cell1, cell2, cell3])) {
                return true;
            }
        }
    },

    checkColumns: () => {
        for (let i = 0; i < 3; i++) {

            let cell1 = getCell(0, i).innerHTML;
            let cell2 = getCell(1, i).innerHTML;
            let cell3 = getCell(2, i).innerHTML;
            console.log(cell3.innerHTML + " " + cell3.innerHTML + " " + cell3.innerHTML + " " + Game.currentTurn + "\n");
            if (checkIfAllEqual([cell1, cell2, cell3])) {

                console.log("winning on Vertical")
                return true;
            }
        }
    },
};

function checkDiagonals() {
    //get diagonal
    //grab every 4th cellstarting t the first cell
    //check if they are all equal
    let diagonals = [];
    let won = false;
    for (let i = 0; i < 9; i++) {
        if (i % 4 == 0) {
            diagonals.push(cells[i].innerHTML)
                //console.log("Checking diagonals" + " " + i + " " + diagonals[i % 3])

        }
    }
    if (diagonals.every(val => val === diagonals[0] && val != '')) {
        console.log("game won on diagonal" + diagonals.length);
        return true;
    }
    let opDiagonals = [];
    //get opposite diagonals, get every other cell starting at the third cell and ending on the 7th
    //check if they are all equal
    for (let i = 2; i <= 6; i++) {
        if (i % 2 == 0) {
            opDiagonals.push(cells[i].innerHTML) //cells[i]
                // console.log("Checking opposite diagonals" + " " + i + " " + opDiagonals[i % 3])
        }
    }

    if (opDiagonals.every(val => val === opDiagonals[0] && val != '')) {
        console.log("game won on opposite diagonal");
        return true;
    }
    return false;
}