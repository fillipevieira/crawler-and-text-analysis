import datetime


class RabinKarp(object):

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
            q = 101
            d = 256
            matched_indexes = self.compare(text=text, pattern=word, d=d, q=q)
            if matched_indexes:
                matched_indexes_amount += 1

            print("[RABIN KARP ALGORITHM] Word: {} | Matched indexes: {}".format(word, ",".join(matched_indexes)))

        end = datetime.datetime.now()

        words_amount = len(words)
        result = matched_indexes_amount / words_amount
        percent = result * 100

        print("\n------------------------- Results ---------------------------")
        print("Duration: {}".format(end - start))
        print("Words amount: {}".format(str(words_amount)))
        print("Matched indexes amount: {}".format(str(matched_indexes_amount)))
        print("Similarity percentage: %.2f" % percent)

    def compare(self, text, pattern, d, q):
        n = len(text)
        m = len(pattern)
        h = pow(d, m-1) % q
        p = 0
        t = 0
        result = []

        for i in range(m):
            p = (d*p+ord(pattern[i])) % q
            t = (d*t+ord(text[i])) % q

        for s in range(n-m+1):
            if p == t:
                match = True
                for i in range(m):
                    if pattern[i] != text[s+i]:
                        match = False
                        break

                if match:
                    result = result + [str(s)]

            if s < n-m:
                t = (t-h*ord(text[s])) % q
                t = (t*d+ord(text[s+m])) % q
                t = (t+q) % q

        return result


# if __name__ == "__main__":
#
#     pattern = "../../../preprocessed_files/liveboot/normalized-text.txt"
#     base_text = "../../../preprocessed_files/police/noise-free-text.txt"
#
#     with open(pattern, "r") as file:
#         words = [word.replace("\n", "") for word in file.readlines()]
#         words = list(set(words))
#
#     with open(base_text, "r") as file:
#         text = file.read().lower()
#
#     start = datetime.datetime.now()
#     matched_indexes_amount = 0
#     for word in words:
#         q = 101
#         d = 256
#         matched_indexes = rabin_karp(text=text, pattern=word, d=d, q=q)
#         if matched_indexes:
#             matched_indexes_amount += 1
#
#         print("[RABIN KARP ALGORITHM] Word: {} | Matched indexes: {}".format(word, ",".join(matched_indexes)))
#
#     end = datetime.datetime.now()
#
#     words_amount = len(words)
#     result = matched_indexes_amount / words_amount
#     percent = result * 100
#
#     print("\n------------------------- Results ---------------------------")
#     print("Duration: {}".format(end-start))
#     print("Words amount: {}".format(str(words_amount)))
#     print("Matched indexes amount: {}".format(str(matched_indexes_amount)))
#     print("Similarity percentage: %.2f" % percent)
