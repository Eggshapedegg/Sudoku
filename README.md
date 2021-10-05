# Sudoku
Sudoku puzzle solver
![Image of Yaktocat](https://github.com/Eggshapedegg/Sudoku/blob/main/sudoku.png)

This project (made in Python and Pygame) consist in 2 files, and I created it in order to study
the backtracking algorithm.

-Sudoku_base.py is a command-line version, where an incomplete Sudoku puzzle (where the empty slots are represented by zeroes),
is outputted together with the solved one, thanks to the backtracking algorithm.
In short, the algorithm tries to find the first available and valid number in a slot, after checking the column, row and square
it is in, and if no value is valid it means that somewhere previously there is a mistake, so the algorithm "backtracks" to a
previous slot and tries to solve the issue.
This continue until the puzzle is fully solved.

-Sudoku_advanced.py overcome the problem of the previous version, which is the lack of visual for the user.
In this version (made with pygame) we have sudoku puzzle that we can complete by ourselves by clicking a cell and inputting
a value (or a note). A mistake will be marked with a red X at the bottom.
In case we want to see a visualization of how the algorithm solves the puzzle, we can press spacebar, and the process will start,
with green cells (meaning a value setted) and red ones, meaning values that are being analyzed by the algorithm.

------------------------------------------------------------------------------------------------------------------------------

数独はPythonで作って、２バージョンがあります。Backtrackingアルゴリズムの勉強の為で作りました（それと、数独が好きですから）。

-Sudoku_base.pyはcommand lineバージョンで、完成していないパズルからアルゴリズムはコンプリートして、プリントします。
簡単に説明すると、アルゴリズムはパズルのスロットを見て、列とスクエアを確認して、最も適当な数字を入れます。
もし数字を入る可能性がなかったら、前にミスがあってアルゴリズムは前のスロットをもう一度確認します。
パズルが完成までアルゴリズムが続けます。

-Sudoku_advances.pyは他のバージョンに違ってGUIを使っています。すると、ユーザーが自分でパズルを完成も出来るし、spacebarを押すとアルゴリズムは
どんな感じで動いていることも出来ます。
