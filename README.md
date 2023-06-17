# youtube-auto-subscribe
Auto Subscribe in Youtube Personal Account.

## Description
Auto Subscribe in Youtube Personal Account. It is an automated tool that allows you to seamlessly subscribe in Youtube Personal Account. This application utilizes Python with Selenium to automate to subscribe to a list of a channels.

## Prerequisites

Before using this tool, ensure that you have the following:

- Python installed on your system.
- Selenium library installed.
- webdriver_manager library installed.
- Chrome
- Run your Chrome in your right path like this, example:
C:\Program Files (x86)\Google\Chrome\Application>chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\xampp\htdocs\youtube-auto-subscribe\localhost"

## Installation
   
1. Clone the repository:

   ```bash
   git clone https://github.com/eselejuanito/youtube-auto-subscribe.git
   ```

2. Navigate to the project directory:

   ```bash
   cd youtube-auto-subscribe
   ```

3. Create an virtual enviroment 

   ```bash
   python -m venv env
   ```
   
   Then acvivate it.
   
   ```bash
   env\Scripts\activate
   ```
   
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Run get-channels.js in your Chrome to get a list of your channels you would like to subscribe to.
6. Run Chrome in your right path like this, example:

   ```bash
   C:\Program Files (x86)\Google\Chrome\Application>chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\xampp\htdocs\youtube-auto-subscribe\localhost"
   ```
     
7. Login to your Youtube Personal Account manually to then run the tool. 
8. Run python main.py
   ```bash
   python main.py
   ```

## Usage

1. Get the list of channels you would like to subscribe to with get-channels.js.
2. Run the tool:

   ```bash
   python main.py
   ```

## Contribution

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Contact

For any questions, suggestions, or feedback, please feel free to contact me at [eselejuanito](https://linktr.ee/eselejuanito).

For help me 💰:
paypal.me/eselejuanito
