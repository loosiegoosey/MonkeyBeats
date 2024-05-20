# MonkeyBeats

## Overview
MonkeyBeats is a dynamic file organizer designed to efficiently manage and organize multimedia files on your system. This project offers tools for filtering, moving, and organizing files, along with removing empty directories and handling events.

## Features
- **Empty Directory Removal**: Automatically remove empty directories within a specified location.
- **Custom Event Handling**: Create and manage custom events.
- **File Filtering**: Filter files based on dynamic criteria.
- **File Moving**: Move files to specified locations with unique naming conventions.
- **Command Line Options**: Configure and control application behavior through command line arguments.
- **Console and GUI Interfaces**: Choose between a simple console interface or an intuitive graphical user interface.
- **Testing Framework**: Unit tests for ensuring code reliability and correctness.

## Installation Instructions
1. **Clone the repository:**
    ```sh
    git clone https://github.com/YourUsername/MonkeyBeats.git
    cd MonkeyBeats
    ```
2. **Install dependencies:**
    Make sure you have Python installed. You may also need the `PyQt4` library for the GUI interface:
    ```sh
    pip install PyQt4 eyeD3
    ```

## Usage Examples
### Organizing Files via Command Line:
1. **Basic usage:**
    ```sh
    python organize.py --rootDirectory=path/to/your/files
    ```
2. **Start in GUI mode:**
    ```sh
    python organize.py --startGuiMode=true
    ```

### Sample Python Code for Using File Mover:
```python
from fileMover import FileMover

files = ['file1.mp3', 'file2.mp3']
destination = 'path/to/destination'
mover = FileMover(files, destination)
mover.move()
```

## Code Summary
- **emptyDirectoryRemover.py**: Contains `EmptyDirectoryRemover` class to remove empty directories.
- **errors.py**: Defines a custom exception hierarchy for handling errors.
- **event.py**: Implements an event handling system to manage and trigger events.
- **fileFilters.py**: Contains `FileSource` for retrieving files and `FileFilter` for filtering files based on specific criteria.
- **fileMover.py**: Includes `FileMover` class for moving files to new locations while ensuring unique filenames.
- **options.py**: Manages command line options and configuration settings for the application.
- **organize.py**: The main script that ties together the components of the project and runs the file organization process.
- **organizer.py**: Handles metadata retrieval and utility functions for managing multimedia metadata.
- **tests/**: Contains unit tests for various modules to ensure code reliability.
- **views/**: Directory containing different user interfaces, including `ConsoleView` and `FormView`.

## Contributing Guidelines
1. **Fork the repository.**
2. **Create a new feature branch:**
    ```sh
    git checkout -b feature-branch
    ```
3. **Commit your changes:**
    ```sh
    git commit -am 'Add new feature'
    ```
4. **Push to the feature branch:**
    ```sh
    git push origin feature-branch
    ```
5. **Create a new Pull Request.**

## License
Licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.