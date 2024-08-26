# Triller Account Gen

A Python script for generating Triller accounts automatically using CAPTCHA solving and disposable email services.

## Features

- **Automated CAPTCHA Solving:** Integrates with the [Ez-Captcha](https://ez-captcha.com) API to solve ReCAPTCHA challenges automatically.
- **Disposable Email Generation:** Uses the Mail API to create disposable email addresses for Triller account registration.
- **Multithreaded Account Creation:** Supports running multiple threads to create accounts in parallel.

## Prerequisites

- Python 3.6+
- Necessary Python packages (`faker`, `requests`, etc.)
- A valid [Ez-Captcha](https://ez-captcha.com) API key
- Access to a Mail API service that provides disposable email addresses
- Basic understanding of Python and threading

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/triller-account-generator.git
   cd triller-account-generator
   ```

2. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the script:**

   Create a `config.json` file in the root directory with the following structure:

   ```json
   {
       "captcha_key": "YOUR_EZ_CAPTCHA_API_KEY",
       "proxy": "YOUR_PROXY_SERVER"
   }
   ```

   Replace `"YOUR_EZ_CAPTCHA_API_KEY"` with your actual Ez-Captcha API key and `"YOUR_PROXY_SERVER"` with your proxy server if needed.

4. **Create the output directory:**

   ```bash
   mkdir output
   ```

## Usage

1. **Run the script:**

   ```bash
   python triller_account_generator.py
   ```

2. **Enter the number of threads** when prompted. Each thread will attempt to create accounts in parallel.

## Code Structure

- `load_config()`: Loads configuration settings from `config.json`.
- `get_timestamp()`: Generates a timestamp for logging.
- `get_captcha()`: Requests and solves a ReCAPTCHA challenge.
- `create_mail()`: Generates a disposable email address.
- `create_acc(mail, captcha)`: Creates a Triller account using the provided email and CAPTCHA solution.
- `worker()`: Runs the account creation process continuously.
- `start(num_threads)`: Starts multiple threads for parallel account creation.

## Notes

- Ensure that you have the necessary permissions and legal rights to use this script for your purposes.
- This script uses proxies and disposable emails, which might be flagged by the target service if overused.
- This script is provided for educational purposes. Misuse of the script can lead to legal consequences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. The author is not responsible for any misuse or legal issues arising from the use of this script.
