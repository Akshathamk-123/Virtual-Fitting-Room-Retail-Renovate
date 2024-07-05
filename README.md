# Virtual Fitting Room - Retail Renovate

Virtual Fitting Room is a web application that allows users to try on different shirts virtually using pose estimation and real-time video processing. The application is built using Flask, OpenCV, and cvzone, providing an interactive and immersive experience.

## Features

- Real-time pose estimation and shirt overlay
- Selection of different shirt sizes
- Admin interface for managing shirt resources
- Easy navigation and user-friendly interface

## Requirements

- Python 3.x
- Flask
- OpenCV
- cvzone

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/virtual-fitting-room.git
cd virtual-fitting-room
```

2. Install the required libraries:

```bash
pip install flask opencv-python-headless cvzone
```

3. Prepare the resources:

- Create the following directory structure inside the `Resources` folder:
  ```bash
  Resources/
    Shirts/
      small/
      medium/
      large/
      XL/
      XXL/
  ```
- Place the corresponding shirt images in the respective folders.
- Add a button image (`button.png`) inside the `Resources` folder.

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Navigate through the different pages and try on shirts virtually.

### Routes

- `/` - Home page
- `/admin` - Admin interface for managing shirts
- `/aboutus` - About Us page
- `/form` - Form to select shirt size
- `/delete` - Form to delete a specific shirt
- `/confirmation` - Confirmation page for shirt deletion
- `/cam` - Virtual fitting room interface
- `/video` - Stream video with pose estimation and shirt overlay

## Flask Application Structure

- `app.py` - Main Flask application file
- `templates/` - HTML templates for the web pages
- `Resources/` - Directory containing shirt images and button image

## Code Overview

### `app.py`

- **Imports**: Imports necessary libraries and modules.
- **Global Variables**: Initializes global variables for video capture, pose detection, and shirt resources.
- **Routes**:
  - `home`: Renders the home page.
  - `admin`: Renders the admin page.
  - `aboutus`: Renders the about us page.
  - `form`: Handles the shirt size selection form.
  - `delete`: Handles the shirt deletion form.
  - `confirmation`: Renders the confirmation page for shirt deletion.
  - `index`: Renders the virtual fitting room page.
  - `video`: Streams video with pose estimation and shirt overlay.
- **Functions**:
  - `generate_frames`: Captures video frames, detects poses, overlays shirts, and handles shirt selection logic.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
- [cvzone](https://github.com/cvzone/cvzone)

---

## Certificate of Participation
![image](https://github.com/Akshathamk-123/Virtual-Fitting-Room-Retail-Renovate/assets/92522733/e52b8844-ede5-4ce6-a5f6-ac454f2738a6)
