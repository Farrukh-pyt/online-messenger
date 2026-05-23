chat = []

print("=== Online Messenger ===")

while True:
    print("\n1. Send Message")
    print("2. View Chat")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        text = input("Message: ")

        chat.append(f"{name}: {text}")

        print("Message sent!")

    elif choice == "2":
        print("\n=== CHAT ===")

        if len(chat) == 0:
            print("No messages yet.")
        else:
            for msg in chat:
                print(msg)

    elif choice == "3":
        print("Closing messenger...")
        break

    else:
        print("Invalid option")
