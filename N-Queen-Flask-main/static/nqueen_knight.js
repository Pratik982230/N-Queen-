let steps = [];
let currentStep = 0;
let simulationInterval;

function startSimulation() {
    const n = document.getElementById("n-input").value;
    const problem = document.getElementById("problem-select").value;

    fetch("/solve", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ n: n, problem: problem }),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response Data:", data);  // Debugging log for data
        steps = data.steps;

        if (steps.length === 0) {
            alert("No solution found!");
            return;
        }

        currentStep = 0;
        displayBoard(steps[currentStep], n, problem);

        simulationInterval = setInterval(() => {
            if (currentStep < steps.length - 1) {
                currentStep++;
                displayBoard(steps[currentStep], n, problem);
            } else {
                clearInterval(simulationInterval);
            }
        }, 1000);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function displayBoard(board, n, problem) {
    const chessboard = document.getElementById("chessboard");
    chessboard.innerHTML = "";

    for (let i = 0; i < n; i++) {
        let rowDiv = document.createElement("div");
        rowDiv.className = "row";

        for (let j = 0; j < n; j++) {
            let cellDiv = document.createElement("div");
            cellDiv.className = "cell " + ((i + j) % 2 === 0 ? "white" : "black");

            if (board[i][j] >= 0) {
                let pieceImg = document.createElement("img");
                if (problem === "queen" && board[i][j] === 1) {
                    pieceImg.src = "/static/queen.png";  // Direct path to queen image
                } else if (problem === "knight_tour" && board[i][j] >= 0) {
                    pieceImg.src = "/static/knight.png";  // Direct path to knight image
                }
                
                pieceImg.className = "piece";
                cellDiv.appendChild(pieceImg);
            }

            rowDiv.appendChild(cellDiv);
        }
        chessboard.appendChild(rowDiv);
    }
}
