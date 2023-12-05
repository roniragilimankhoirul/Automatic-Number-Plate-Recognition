# Automatic-Number-Plate-Recognition

This project aims to perform vehicle license plate detection in images using Optical Character Recognition (OCR). The detection results are stored in a MySQL database, and there is also a viewing script to display images along with the associated text and IDs.

## Prerequisites

Before running the script, make sure you have:

- Python installed
- Required Python packages installed (`mysql-connector-python`, `matplotlib`, `numpy`, `opencv-python`, `easyocr`, `imutils`, `python-dotenv`)

```bash
pip install mysql-connector-python matplotlib numpy opencv-python easyocr imutils python-dotenv
```

## Usage

1. Clone the repository:

```
git clone https://github.com/roniragilimankhoirul/Automatic-Number-Plate-Recognition.git && cd Automatic-Number-Plate-Recognition
```

2. Create a virtual environment:

```
python -m venv myenv
```

3. Activate the virtual environments:

```
source myenv/bin/activate
```

4. Install Dependencies:

```
pip install -r requirements.txt
```

5. Set up your environment by creating a .env file with the following variables:

```
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

6. Run the image detection program:

```
python main.py path/to/your/image.jpg
```

7. Run the view images in database program:

```
python view_image.py [index]
```

- If no index is provided, all images will be displayed.
- If an index is provided, only the image at that index will be displayed.

## Language Versions

- [English Version (README.md)](README.md)
- [Indonesian Version (README_ID.md)](README_ID.md)
