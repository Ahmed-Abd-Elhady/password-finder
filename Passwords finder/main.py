king = {
    "email": {
        "1": ["Google@gmail.com", "noneIndra?"],
        "2": ["Chrome1@gmail.com", "BSArkamNight2"],
    },
    "steam": {
        "1": ["Hello)(!@#)", "FXCA123a"],
    },
    "epicgames": {
        "1": ["Google@gmail.com", "Chrome123"],
    },
    "riot": {
        "1": ["Valorant?", "hello?>"],
    },
}
print(f"if you have any problem this bec : i can't find (your inputs) try again <3")
cffv = ", ".join(king)
whatcawant = str(
    input(f"do you want : {cffv} ?: ")
)
s = king[whatcawant]
c = " , ".join(s)
n = len(s)
print(f" ({n}) acounnts found!")
whatWant = input("what account number you want? : ")


for x in king:
    if whatcawant == str(x):
        print(
            f"Email/UserName : {king[x][whatWant][0]} , Password : {king[x][whatWant][1]}"
        )
