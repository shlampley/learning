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