import urllib3
from environs import env
from requests import Session

from src.utils import get_sem_code, get_user_id, get_user_pass, is_ci


def get_webkiosk_origin(intra: bool):
    if intra:
        print("Using intranet...")
        return "https://webkioskintra.thapar.edu:8443"
    return "https://webkiosk.thapar.edu"


def get_html():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    origin = get_webkiosk_origin(env.bool("USE_WEBKIOSK_INTRA", False))
    login_url = f"{origin}/CommonFiles/UserAction.jsp"
    cgpa_url = f"{origin}/StudentFiles/Exam/StudCGPAReport.jsp"
    grades_url = f"{origin}/StudentFiles/Exam/StudentEventGradesView.jsp?x=&exam={get_sem_code()}&Subject=ALL"

    payload = {
        "txtuType": "Member Type",
        "UserType": "S",
        "txtCode": "Enrollment No",
        "MemberCode": get_user_id(),
        "txtPin": "Password/Pin",
        "Password": get_user_pass(),
        "BTNSubmit": "Submit",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "Referer": f"{origin}/index.jsp",
        "Origin": f"{origin}",
    }

    session = Session()
    session.verify = False

    try:
        # print("Visiting homepage...")
        # session.get(f"{origin}/index.jsp", headers=headers, verify=False)

        print("Attempting login...")
        response = session.post(login_url, data=payload, headers=headers, verify=False)
        print(f"Login Status: {response.status_code}")
        # print(response.text)

        print("Fetching CGPA Report...")
        cgpa_response = session.get(cgpa_url, headers=headers, verify=False)
        if not is_ci():
            with open("./cgpa.html", "w") as f:
                f.write(cgpa_response.text)
        print(f"CGPA Status: {cgpa_response.status_code}")

        print("Fetching Grades Report...")
        grade_response = session.get(grades_url, headers=headers, verify=False)
        if not is_ci():
            with open("./grades.html", "w") as f:
                f.write(grade_response.text)
        print(f"Grades Status: {cgpa_response.status_code}")

        if "CGPA" in cgpa_response.text or "Earned Credit" in cgpa_response.text:
            print("SUCCESS! Found Grade Data.")
            # print(cgpa_response.text)
            return cgpa_response.text
        else:
            print("Failed. Could not find cpga table in response.")
            # print(cgpa_response.text)
            return cgpa_response.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
