# GUI for Trajectory Benchmarking with Indoor GPS

* Command to view data received from modem
    ```
    python src/MarvelmindRobotics/src/example_matplotlib.py 
    python src/MarvelmindRobotics/src/example.py
    ```
* Command for installing Qt5 Designer
    ```
    sudo apt-get install qttools5-dev-tools
    sudo apt-get install qttools5-dev
    ```
* Converting ".ui" to ".py" with PyQt5
    * Command usage : 
        ```
        pyuic5 -x [Qt_Design_FILENAME].ui -o [Python_FILENAME].py
        ```
    * Command : 
        ```
        pyuic5 -x src/GUI_Window.ui -o src/GUI_Window.py
        ```