# GUI for Trajectory Benchmarking with Indoor GPS

* Command to view data received from modem
    ```
    python src/main/python/MarvelmindRobotics/src/example_matplotlib.py 
    python src/main/python/MarvelmindRobotics/src/example.py
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
        pyuic5 -x src/Qt_design/GUI_Window.ui -o src/main/python/scripts/GUI_Window.py
        ```
* Packaging PyQt5 apps with fbs
    * Starting an app (only when starting a new project)
        ```
        fbs startproject
        ```
    * Running the app
        ```
        fbs run
        ```
    * Freezing the app
        ```
        fbs freeze
        ```
    * Creating the Installer
        ```
        fbs installer
        ```
        The resulting package will be created under the "target/folder". the package file will be named "AppName.deb".