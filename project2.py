
# Function to count words in the input text
def count_words(text):
    # Splitting by default whitespace to extract words
    words = text.split()
    return len(words)

# Display welcome screen
print("\n" + "=" * 50)  
print("🔤 Welcome to the Word Counter Program!")
print("📌 Enter any sentence or paragraph below, and I'll count the words for you.")
print("=" * 50)

# Ask user for input
text = input("\n✏️  Please type your sentence/paragraph:\n\n👉 ")

# Trim whitespace and validate input
if not text.strip():
    print("\n⚠️  Oops! You didn't type anything. Please run the program again.")
else:
    # Count and display the result
    word_count = count_words(text)
    print("\n📊 Total Words Found:", word_count)
    print("\n🎉 Thank you for using the Word Counter! 🚀")

print("\n" + "=" * 50)
