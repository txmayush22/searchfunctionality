search_google=input("Search:: ")

fruits=["apple","orange","banana"]
color=["red fruits blog","orange fruits blog","yellow fruits blog"]
trendingNews=["apples extinct","oranges infected","bananas production increased"]
shape=["round fruits","round fruits","moon shape fruits"]


if search_google=="apple":
    print("red fruits blog","apples extinct","round fruits")
elif search_google=="red fruits blog":
    print("apple","apples extinct","round fruits")
elif search_google=="apples extinct":
    print("apple","red fruits blog","round fruits")
elif search_google=="round fruits":
    print("apple","red fruits blog","apples extinct")


if search_google=="orange":
    print("orange fruits blog","oranges infected","round fruits")
elif search_google=="orange fruits blog":
    print("orange","oranges infected","round fruits")
elif search_google=="oranges infected":
    print("orange","orange fruits blog","round fruits")
elif search_google=="round fruits":
    print("orange","orange fruits blog","oranges infected")



if search_google=="banana":
    print("yellow fruits blog","bananas production increased","moon shaped fruits")
elif search_google=="yellow fruits blog":
    print("banana","bananas production increased","moon shaped fruits")
elif search_google=="bananas production increased":
    print("banana","yellow fruits blog","moon shaped fruits")
elif search_google=="moon shaped fruits":
    print("banana","yellow fruits blog","bananas production increased")


#####################################################################################################################3


fruits=["apple","orange","banana"]
if "apple" or "orange" or "banana"  in fruits:
    print("yes")
    print(fruits.index("orange"))







