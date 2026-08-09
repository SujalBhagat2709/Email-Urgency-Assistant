"""
Email Urgency Assistant
-----------------------
File : email_urgency_assistant.py

Purpose
-------
Analyzes email text and estimates how urgent the
email is using simple NLP-style keyword scoring.

Features
--------
✔ Analyze Email
✔ Urgency Score
✔ Urgency Level
✔ Email Category
✔ Reason Detection
✔ Priority Sorting
✔ Email Summary
"""


class EmailUrgencyAssistant:

    def __init__(self):

        self.emails = []

        self.urgent_words = {

            "urgent": 5,
            "asap": 5,
            "immediately": 5,
            "emergency": 6,
            "critical": 5,
            "deadline": 4,
            "today": 3,
            "important": 3,
            "priority": 3,
            "action required": 4,
            "response required": 4,
            "final notice": 5

        }

        self.categories = {

            "meeting": [
                "meeting",
                "call",
                "schedule"
            ],

            "payment": [
                "payment",
                "invoice",
                "bill",
                "due"
            ],

            "work": [
                "project",
                "task",
                "report",
                "deadline"
            ],

            "support": [
                "issue",
                "problem",
                "error",
                "help"
            ]

        }

    # ----------------------------------
    # Calculate Urgency Score
    # ----------------------------------
    def calculate_score(self,
                        text):

        text = text.lower()

        score = 0

        for word, weight in self.urgent_words.items():

            if word in text:

                score += weight

        return min(score, 10)

    # ----------------------------------
    # Determine Urgency
    # ----------------------------------
    def urgency_level(self,
                      score):

        if score >= 8:

            return "Critical"

        elif score >= 5:

            return "High"

        elif score >= 2:

            return "Medium"

        return "Low"

    # ----------------------------------
    # Detect Category
    # ----------------------------------
    def detect_category(self,
                        text):

        text = text.lower()

        for category, keywords in self.categories.items():

            for keyword in keywords:

                if keyword in text:

                    return category.title()

        return "General"

    # ----------------------------------
    # Detect Reasons
    # ----------------------------------
    def detect_reasons(self,
                       text):

        text = text.lower()

        reasons = []

        for word in self.urgent_words:

            if word in text:

                reasons.append(word)

        return reasons

    # ----------------------------------
    # Analyze Email
    # ----------------------------------
    def analyze_email(self,
                      sender,
                      subject,
                      body):

        combined_text = (
            subject + " " + body
        )

        score = self.calculate_score(
            combined_text
        )

        email = {

            "Sender": sender,

            "Subject": subject,

            "Category":
                self.detect_category(
                    combined_text
                ),

            "Urgency Score":
                score,

            "Urgency":
                self.urgency_level(
                    score
                ),

            "Reasons":
                self.detect_reasons(
                    combined_text
                )

        }

        self.emails.append(email)

        return email

    # ----------------------------------
    # Sort by Priority
    # ----------------------------------
    def priority_emails(self):

        return sorted(

            self.emails,

            key=lambda email:
            email["Urgency Score"],

            reverse=True

        )

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        critical = 0
        high = 0
        medium = 0
        low = 0

        for email in self.emails:

            level = email["Urgency"]

            if level == "Critical":

                critical += 1

            elif level == "High":

                high += 1

            elif level == "Medium":

                medium += 1

            else:

                low += 1

        return {

            "Total Emails":
                len(self.emails),

            "Critical":
                critical,

            "High":
                high,

            "Medium":
                medium,

            "Low":
                low

        }

    # ----------------------------------
    # Display Email
    # ----------------------------------
    def display_email(self,
                      email):

        print(
            "\n========== EMAIL ANALYSIS ==========\n"
        )

        for key, value in email.items():

            print(
                f"{key:<18}: {value}"
            )

    # ----------------------------------
    # Display Priority List
    # ----------------------------------
    def display_priority(self):

        emails = self.priority_emails()

        if not emails:

            print(
                "\nNo emails analyzed."
            )

            return

        print(
            "\n========== PRIORITY EMAILS ==========\n"
        )

        for index, email in enumerate(

                emails,

                start=1):

            print(
                f"{index}. "
                f"{email['Subject']} "
                f"→ {email['Urgency']}"
            )

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print(
            "\n========== SUMMARY ==========\n"
        )

        for key, value in report.items():

            print(
                f"{key:<18}: {value}"
            )


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    assistant = EmailUrgencyAssistant()

    while True:

        print("\n1. Analyze Email")
        print("2. View Priority Emails")
        print("3. View Summary")
        print("4. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":

            sender = input(
                "Sender: "
            )

            subject = input(
                "Subject: "
            )

            body = input(
                "Email Body: "
            )

            email = assistant.analyze_email(

                sender,
                subject,
                body

            )

            assistant.display_email(
                email
            )

        elif choice == "2":

            assistant.display_priority()

        elif choice == "3":

            assistant.display_summary()

        elif choice == "4":

            print(
                "\nThank you for using Email Urgency Assistant."
            )

            break

        else:

            print(
                "\nInvalid choice."
            )