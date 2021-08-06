# GUI for Trajectory Benchmarking with Indoor GPS

* Step 1:
    Run the following command to give rights for your user to access serial port by adding current user to dialout group.

    ```
    sudo adduser $USER dialout
    ```

* Step 2:
    Clone the Repository along with the Marvelmind submodule.
    ```
    git clone https://github.com/Kabilan-T/GUI_for_Trajectory_Benchmarking_with_Indoor_GPS.git
    ```
    ```
    cd GUI_for_Trajectory_Benchmarking_with_Indoor_GPS
    ```
    ```
    git submodule init
    ```
    ```
    git submodule update
    ```

* Step 3:
    Initialize the virtual environment
    * Install pip (if not available)
    ```
    apt-get update && install python3-pip
    ```
    * Install pipenv (if not available)
    ```
    python3.6 -m pip install install pipenv
    ```
    * Initializing pipenv environment
    ```
    pipenv install
    ```
    * Activate environment
    ```
    pipenv shell
    ```
    * Deactivate from environment
    ```
    exit
    ```
* Step 4
    Create the exe file (Suitable for the current Operating System)
    ```
    pyinstaller --onefile src/main.py
    ```
    Note: environment can be deactivated now
* Step 5
    * Make the exe file as executable
    ```
    sudo chmod +x dist/main
    ```
    * Run the exe file
    ```
    ./dist/main
    ```
    Note : The exe file can be copied and runned in any PC with same OS version but make sure the file is executable