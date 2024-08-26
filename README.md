# Triller Account Gen

A Python script for generating Triller accounts automatically using CAPTCHA solving and disposable email services.

## Features

- **Automated CAPTCHA Solving:** Integrates with the [Ez-Captcha](https://dashboard.ez-captcha.com/#/register?inviteCode=QTaxJrpKMIJ) API to solve ReCAPTCHA challenges automatically.
- **Disposable Email Generation:** Uses the Mail API to create disposable email addresses for Triller account registration.
- **Multithreaded Account Creation:** Supports running multiple threads to create accounts in parallel.

## Prerequisites

- Python 3.6+
- Necessary Python packages (`faker`, `requests`, etc.)
- A valid [Ez-Captcha](https://dashboard.ez-captcha.com/#/register?inviteCode=QTaxJrpKMIJ) API key
- Basic understanding of Python and threading
- Brain Cells :)

## Setup

1. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure the script:**

   ```json
      {
          "captcha_key": "YOUR_EZ_CAPTCHA_API_KEY",
          "proxy": "USER:PASS@IP:PORT"
      }
   ```

   Replace `"YOUR_EZ_CAPTCHA_API_KEY"` with your actual Ez-Captcha API key and `"USER:PASS@IP:PORT"` with your proxy server if needed.

## Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **Enter the number of threads** when prompted. Each thread will attempt to create accounts in parallel.


# Disclaimer
This tool is created for educational purposes and ethical use only. Any misuse of this tool for malicious purposes is not condoned. The developers of this tool are not responsible for any illegal or unethical activities carried out using this tool.

[![Star History Chart](https://api.star-history.com/svg?repos=JOY6IX9INE/Triller-Account-Gen&type=Date)](https://star-history.t9t.io/#JOY6IX9INE/Triller-Account-Gen&Date)

