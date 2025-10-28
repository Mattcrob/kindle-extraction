# Kindle Extraction Project - AI Assistant Instructions

## Project Overview
This project is designed to extract and process highlighted text from Kindle books, primarily for language learning purposes. The main functionality involves parsing the "My Clippings.txt" file that Kindle devices generate.

## Key Components

### Data Source
- Input: `My Clippings.txt` file from Kindle devices
- Location: Must be in the root directory
- Encoding: UTF-8
- Format: Text entries separated by "=========="

### Core Processing (`harry_potter.py`)
- Main script for processing Kindle highlights
- Uses pandas for data manipulation
- Key operations:
  - File reading with UTF-8 encoding
  - Highlight extraction using "==========" as delimiter
  - Basic statistics calculation (number of highlights)

## Development Setup
1. Virtual Environment:
   ```powershell
   python -m venv venv
   venv\scripts\activate
   ```
2. Dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Dependencies
Key packages (see `requirements.txt`):
- pandas (2.3.3)
- numpy (2.3.4)
- python-dateutil
- pytz
- tzdata

## Project Conventions
- Python scripts use UTF-8 encoding for file operations
- Virtual environment (`venv`) is used for dependency management
- Package versions are strictly pinned in requirements.txt

## Development Guidelines
1. Maintain compatibility with Windows file systems
2. Keep explicit encoding specifications (UTF-8) for file operations
3. Use pandas for data manipulation tasks
4. Follow the existing pattern of basic statistics reporting