# Question
<img width="1003" alt="Screenshot 2025-02-24 at 2 08 37 PM" src="https://github.com/user-attachments/assets/fd4a69f6-c77f-4cc1-a6a3-091907663575" />


# Code 
```.py
class WordCounter:
    def __init__(self, text):
        self.text = text.lower()  
        self.word_count = {}

    def count_words(self):
        words = self.text.replace(".", "").replace(",", "").split()  # Remove punctuation and split words
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1  # Increment count if word exists
            else:
                self.word_count[word] = 1  # Initialize count if word is new

    def display_counts(self):
        for word in sorted(self.word_count):  # Sort words alphabetically
            print(f"{word} : {self.word_count[word]}")


text = "This is a sample text. It contains some words that will be counted."
word_counter = WordCounter(text)
word_counter.count_words()
word_counter.display_counts()


```
## Evidence

<img width="1422" alt="Screenshot 2025-02-24 at 8 32 49 PM" src="https://github.com/user-attachments/assets/4c6c855f-6e8f-4cbc-af38-3811c
  
  ## UML Diagram

 
![Screenshot 2025-02-24 at 8 36 07 PM](https://github.com/user-attachments/assets/1b00236c-f72d-41a3-8f2c-db1c119dba8a)
