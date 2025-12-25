def spa_chatbot():
    print("🤖 Welcome to Serenity Spa Booking Chatbot!")
    print("Please answer a few questions to book your appointment.\n")

    # Question 1
    name = input("1. What is your full name? ")

    # Question 2
    phone = input("2. What is your phone number? ")

    # Question 3
    email = input("3. What is your email address? ")

    # Question 4
    service = input("4. Which spa service would you like? (Massage / Facial / Hair Spa / Body Treatment) ")

    # Question 5
    date = input("5. Preferred appointment date (DD-MM-YYYY): ")

    # Question 6
    time = input("6. Preferred time slot (Morning / Afternoon / Evening): ")

    # Question 7
    therapist = input("7. Do you prefer a male or female therapist? ")

    # Question 8
    requests = input("8. Any special requests or notes? (If none, type 'No') ")

    # Booking summary
    print("\n📋 Booking Summary")
    print("----------------------------")
    print(f"Name: {name}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")
    print(f"Service: {service}")
    print(f"Date: {date}")
    print(f"Time: {time}")
    print(f"Therapist Preference: {therapist}")
    print(f"Special Requests: {requests}")
    print("----------------------------")
    print("✅ Your spa appointment request has been recorded!")
    print("Our team will contact you shortly for confirmation. Thank you 😊")

# Run the chatbot
spa_chatbot()