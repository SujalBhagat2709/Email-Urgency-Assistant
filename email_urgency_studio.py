"""
Email Urgency Studio
--------------------
Main interface for Email Urgency Assistant.
"""

from email_urgency_assistant import EmailUrgencyAssistant


class EmailUrgencyStudio:

    def __init__(self):

        self.assistant = EmailUrgencyAssistant()

    # ----------------------------------
    # Analyze Email
    # ----------------------------------
    def analyze_email(self):

        print(
            "\n========== ANALYZE EMAIL ==========\n"
        )

        sender = input(
            "Sender: "
        ).strip()

        subject = input(
            "Subject: "
        ).strip()

        body = input(
            "Email Body: "
        ).strip()

        email = self.assistant.analyze_email(

            sender,
            subject,
            body

        )

        print(
            "\nEmail analyzed successfully."
        )

        self.assistant.display_email(
            email
        )

    # ----------------------------------
    # Priority Emails
    # ----------------------------------
    def priority_emails(self):

        self.assistant.display_priority()

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        self.assistant.display_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("          EMAIL URGENCY ASSISTANT")
            print("=" * 60)

            print("1. Analyze Email")
            print("2. View Priority Emails")
            print("3. View Summary")
            print("4. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.analyze_email()

            elif choice == "2":

                self.priority_emails()

            elif choice == "3":

                self.summary()

            elif choice == "4":

                print(
                    "\nThank you for using Email Urgency Assistant."
                )

                break

            else:

                print(
                    "\nInvalid choice."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = EmailUrgencyStudio()

    studio.menu()