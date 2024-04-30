def sort_on(dict):
  return dict["num"]

def create_report(words: int, char_dict: dict[str, int]):
  chars_list = []
  for item in char_dict:
    if item.isalpha():
      chars_list.append({"char": item, "num": char_dict[item]})

  chars_list.sort(reverse=True, key=sort_on)
  
  report = "--- Begin report of books/frankenstein.txt ---\n"
  report += f"{words} words found in the document\n"
  for item in chars_list:
    report += f"The \'{item["char"]}\' character was found {item["num"]} times\n"
  report += "--- End report ---"
  return report

def count_letters(text: str):
  chars = {}
  lower = text.lower()
  for c in lower:
    if c not in chars:
      chars[c] = 1
    else:
      chars[c] += 1

  return chars

def count_words(text: str):
  return len(text.split())

def get_book_text(path):
  with open(path) as f:
    return f.read()

def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  words = count_words(text)
  chars_dict = count_letters(text)
  report = create_report(words, chars_dict)
  print(report)
main()