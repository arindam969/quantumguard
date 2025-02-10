# QuantumGuard

QuantumGuard is a Python-based print management utility designed to streamline and organize printing tasks on Windows systems. By managing the queue and efficiently processing print jobs, QuantumGuard aims to reduce wait times and optimize the printing workflow.

## Features

- Automatically discovers and sets the default printer.
- Adds documents to a managed print queue.
- Processes print jobs in the order they are received.
- Supports concurrent job handling with thread safety.

## Requirements

- Windows OS
- Python 3.x
- PyWin32 library

## Installation

1. Ensure you have Python 3.x installed on your Windows machine.
2. Install the PyWin32 library by running:
   ```shell
   pip install pywin32
   ```

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing `quantum_guard.py`.
3. Run the script using Python:
   ```shell
   python quantum_guard.py
   ```
4. Add documents to the print queue by calling the `add_print_task` method with the document path as an argument.

## Example

```python
from quantum_guard import QuantumGuard

qg = QuantumGuard()
qg.add_print_task("example_document.txt")
```

This example demonstrates how to add a document to the print queue for processing.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Contact

For questions or support, please contact [your-email@example.com].