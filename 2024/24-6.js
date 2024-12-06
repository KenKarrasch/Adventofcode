<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid Walk Simulation</title>
</head>
<body>
    <h1>Grid Walk Simulation</h1>
    <textarea id="gridInput" rows="10" cols="50" placeholder="Paste your grid here..."></textarea>
    <br>
    <button onclick="runSimulation()">Run Simulation</button>
    <pre id="output"></pre>

    <script>
  
        // Javascript ran much quicker
  
  
        function simulateWalk(grid) {
            const directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]; // Up, Right, Down, Left
            let dirIndex = 0;

            // Find the starting position
            let startPos = null;
            for (let i = 0; i < grid.length; i++) {
                for (let j = 0; j < grid[0].length; j++) {
                    if (grid[i][j] === '^') {
                        startPos = [i, j];
                        break;
                    }
                }
                if (startPos) break;
            }

            if (!startPos) return [0, grid]; // No starting position found

            let [x, y] = startPos;
            let steps = 0;
            const visited = new Set();

            while (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length) {
                const currentState = `${x},${y},${dirIndex}`;
                if (visited.has(currentState)) return [-1, null]; // Circular path detected
                visited.add(currentState);

                const [dx, dy] = directions[dirIndex];
                const newX = x + dx;
                const newY = y + dy;

                if (newX >= 0 && newX < grid.length && newY >= 0 && newY < grid[0].length) {
                    if (grid[newX][newY] === '#') {
                        dirIndex = (dirIndex + 1) % 4; // Turn right
                    } else {
                        x = newX;
                        y = newY;
                        steps++;
                    }
                } else {
                    break; // Off the map
                }
            }

            return [steps, -1];
        }

        function runSimulation() {
            const input = document.getElementById('gridInput').value;
            const grid = input.split('\n').map(line => line.split(''));
            const gr = grid.map(row => [...row]);
            const output = document.getElementById('output');

            output.textContent = `Grid size: ${grid.length} x ${grid[0].length}\n\n`;

            let infi = 0;
            const ln = 0;
	    let tly = 0

            for (let i = ln; i < ln + 130; i++) {
                for (let j = 0; j < grid.length; j++) {
                    const testGrid = gr.map(row => [...row]);
                    testGrid[j][i] = '#';
                    const [steps, _] = simulateWalk(testGrid);
                    if (steps === -1) {
                        infi++;
                    }
                }
                //output.textContent += `Line ${i}: ${infi} infinite paths\n`;
		tly = tly + infi;
                infi = 0;
		
            }
	    output.textContent += `${tly} infinite paths\n`;
        }
    </script>
</body>
</html>
