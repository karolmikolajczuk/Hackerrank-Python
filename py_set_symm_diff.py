n_english = int(input())
english_newsl = set(map(int, input().split()))
n_french = int(input())
french_newsl = set(map(int, input().split()))
print(len(english_newsl ^ french_newsl))

