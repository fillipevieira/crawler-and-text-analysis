import datetime


class BruteForce(object):

    def start(self, html_1, html_2):
        pattern = "preprocessed_files/" + html_1 + "/normalized-text.txt"
        base_text = "preprocessed_files/" + html_2 + "/noise-free-text.txt"

        with open(pattern, "r") as file:
            words = [word.replace("\n", "") for word in file.readlines()]
            words = list(set(words))

        with open(base_text, "r") as file:
            text = file.read().lower()

        start = datetime.datetime.now()
        matched_indexes_amount = 0
        for word in words:
            matched_indexes = self.compare(text=text, pattern=word)
            if matched_indexes:
                matched_indexes_amount += 1

            print("[BRUTE FORCE ALGORITHM] Word: {} | Matched indexes: {}".format(word, ",".join(matched_indexes)))

        end = datetime.datetime.now()

        words_amount = len(words)
        result = matched_indexes_amount / words_amount
        percent = result * 100

        print("\n------------------------- Results ---------------------------")
        print("Duration: {}".format(end - start))
        print("Words amount: {}".format(str(words_amount)))
        print("Matched indexes amount: {}".format(str(matched_indexes_amount)))
        print("Similarity percentage: %.2f" % percent)

    def compare(self, text, pattern):
        integers = list()
        n_text = len(text)
        n_pattern = len(pattern)
        for i in range(n_text - n_pattern):
            j = 0

            while j < n_pattern and text[i+j] == pattern[j]:
                j += 1

            if j == n_pattern:
                integers.append(str(i))

        return integers
