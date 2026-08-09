print("Welcome! to our movie theater.")
age = int(input("Enter your age here: "))
movie_ticket = 0

if age < 5:
    print("Free ticket for kids. Who come under 5.")
elif 5 <= age <= 18:
    movie_ticket = 100
    print(f"Price for teenagers {movie_ticket} rupees.")
elif 19 <= age <= 60:
    movie_ticket = 200
    print(f"Price for adults {movie_ticket} rupees.")
else:
    movie_ticket = 150
    print(f"Price for old pepole {movie_ticket} rupees")