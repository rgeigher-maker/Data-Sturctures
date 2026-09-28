import string
import os


class MyHashSet:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def contains(self, key):
        index = self._hash(key)
        return key in self.buckets[index]


class MyHashMap:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return 0

    def get_all_items(self):
        items = []
        for bucket in self.buckets:
            items.extend(bucket)
        return items



def clean_text(filename):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return []

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text.split()


def main():
    print("CSC 2440 Final Project: Word Frequency & Spell Checker")

    dictionary = MyHashSet()
    for word in ["data", "structures", "python", "algorithm", "hashing", "college", "programming"]:
        dictionary.add(word)

    # 2. Setup Stop Words
    stop_words = {"the", "be", "to", "of", "and", "a", "in", "that", "have", "it"}

    # 3. Process the Text File
    words = clean_text('sample_text.txt')
    if not words: return

    freq_map = MyHashMap()
    misspelled = []

    for word in words:
        # Spell Checking
        if not dictionary.contains(word) and word not in stop_words:
            if word not in misspelled: misspelled.append(word)

        # Frequency Counting (ignoring stop words)
        if word not in stop_words:
            current_count = freq_map.get(word)
            freq_map.put(word, current_count + 1)

            # 4. Display Results
            print(f"--- ANALYSIS REPORT ---")
            print(f"Total Words Processed: {len(words)}")

            print("\nTop Word Frequencies:")
            # We sort at the very end for display
            sorted_freqs = sorted(freq_map.get_all_items(), key = lambda x: x[1], reverse = True)
            for word, count in sorted_freqs[:5]:
                print(f" {word:<15}: {count} times")

        print("\nPotential Misspellings (Not in Dictionary):")
        if misspelled:
            print(", ".join(misspelled[:10]) + "...")
        else:
            print("No misspellings found!")

    if __name__ == "__main__":
        main()