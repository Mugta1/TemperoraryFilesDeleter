

# Temp File Deleter

## Overview

The Temp File Deleter is a simple Python script designed to periodically delete temporary files from specified directories. This can help free up disk space and improve system performance. The script checks two directories by default: the system temporary files directory and the user-specific temporary files directory.

## Features

- Deletes files from specified temporary directories.
- Prompts the user every 48 hours to confirm whether to delete the files again.
- Handles exceptions gracefully if files cannot be deleted.

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/Mugta1/TemperoraryFilesDeleter.git
    cd TemperoraryFilesDeleter
    ```

2. **Run the Script:**

    ```sh
    python main.py
    ```

## How It Works

1. **Deleting Temporary Files:**
    The `deleter` function iterates through a list of directories and attempts to delete all files within them.

2. **Main Function:**
    The `main` function pauses execution for 48 hours (`172800` seconds). After this period, it prompts the user to confirm if they want to delete the files again. If the user responds with "yes", the `deleter` function is called again. Otherwise, the prompt is repeated.

## Notes

- Ensure you have the necessary permissions to delete files from the specified directories.
- Modify the directories in `tempfiledirectory` as needed for your specific use case.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

