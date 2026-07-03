import requests
from config.config import RESEND_BASE_URL, SEND_EMAIL_URL, RESEND_TO, RESEND_FROM, RESEND_API_KEY, TIMEOUT
from utils.logger import write_log
from datetime import datetime
from pathlib import Path
import base64

def send_reports():
    """Send the reports to the team via email"""
    url = RESEND_BASE_URL + SEND_EMAIL_URL

    folder_path = Path("reports")
    reports = folder_path.glob("*.csv")

    attachments = []
    report_list = ""

    for report in reports:
        # add report name to HTML
        report_list += f"<li>{report.stem}</li>"

        # read report file
        with open(report, "rb") as f:
            encoded_file = base64.b64encode(f.read()).decode("utf-8")

        # prepare attachments for Resend:
        attachments.append(
            {
                "filename": report.name,
                "content": encoded_file,
            }
        )

    today = datetime.now().strftime("%Y-%m-%d")
    subject = f"GitHub Analytics Report - {today}"
    html = f"""
    <h2>Good Morning Team,</h2>

    <p>Please find today's GitHub Analytics reports attached.</p>

    <p>Report Date: <strong>{today}</strong></p>

    <ul>
        {report_list}
    </ul>

    <p>Regards,<br>
    GitHub ETL Pipeline</p>
    """

    payload = {
        "from": RESEND_FROM,
        "to": [RESEND_TO],
        "subject": subject,
        "html": html,
        "attachments": attachments,
    }

    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)
        if response.ok:
            write_log("github", "info", "Email sent successfully.")
        else:
            write_log("github", "error", f"Email sending failed ({response.status_code}): {response.text}")

        return response
    except Exception as e:
        write_log("github", "error", f"Failed to send email: {e}")
        return None