import requests

print("📖 Dictionary App")
print("-" * 30)

word = input("Enter a word: ")

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

try:

    response = requests.get(url)
    data = response.json()

    if isinstance(data, list):

        print("\n===== Word Details =====")

        print("Word:", data[0]["word"])

        meanings = data[0]["meanings"]

        for meaning in meanings:

            print("\nPart of Speech:",
                  meaning["partOfSpeech"])

            for definition in meaning["definitions"][:2]:

                print("Definition:",
                      definition["definition"])

                if "example" in definition:
                    print("Example:",
                          definition["example"])

    else:
        print("Word not found!")

except Exception as e:
    print("Error:", e)