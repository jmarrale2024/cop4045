# Homework 2
import csv
import os
# Helper functions required by the question

def read_top_rated(filename: str) -> set: # Returns the set of (title, year) for every movie in top rated file
    try:
        movies = set()
        with open(filename, 'r', encoding='utf-8', newline='') as file: # Rank,Title,Year,IMDB Rating
            reader = csv.reader(file)
            next(reader) # Skip the header
            for row in reader:
                title, year = row[1], row[2]
                movies.add((title, year))
        return movies
    except Exception as e:
        print(f"Function failure, read_top_rated: {e}")
        raise

def read_box_office(filename: str) -> dict: # Returns a dict mapping (title, year) to box office for top grossing movies
    try:
        box_office = {}
        with open(filename, 'r', encoding='utf-8', newline='') as file: # Rank,Title,Year,USA Box Office
            reader = csv.reader(file)
            next(reader) # Skip the header
            for row in reader:
                title, year, money = row[1], row[2], int(row[3])
                box_office[(title, year)] = money
        return box_office
    except Exception as e:
        print(f"Function failure, read_box_office: {e}")
        raise

def read_casts(filename: str) -> list: # Returns a list of (title, year, director, actors) from the casts file
    try:
        casts = []
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            reader = csv.reader(file)
            for row in reader: # no header to skip for this file
                title, year, director = row[0], row[1], row[2]
                actors = []
                for actor in row[3:]:
                    if actor != "":
                        actors.append(actor)
                casts.append((title, year, director, actors))
        return casts
    except Exception as e:
        print(f"Function failure, read_read_casts: {e}")
        raise

def print_ranking(title: str , ranking: list) -> none: # prints a numbered list of the rankings
    print(title)
    rank = 1
    for item, value in ranking:
        print(f"{rank}.  {item}: {value}")
        rank += 1

# Question 4a:
def display_top_collaborations(rated_file: str , casts_file: str) -> none: # prints director,actor pairs ranked by the number of top rated movies together
    top_rated = read_top_rated(rated_file) # Returns the set of (title, year) for every movie in top rated file
    counts = {}
    for title, year, director, actors in read_casts(casts_file): # Returns a list of (title, year, director, actors) from the casts file
        if (title, year) not in top_rated:
            continue
        for actor in actors:
            pair = (director, actor)
            counts[pair] = counts.get(pair, 0) + 1 # increase amount of movies together

    ranking = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    print_ranking("Top director-actor collaborations:", ranking) # limit to top ten for screenshot [:10] but removed for final code

# Question 4b:
def display_top_actors(grossing_file: str , casts_file: str) -> none: # prints actors ranked by total box office earnings of their top grossing movies
    box_office = read_box_office(grossing_file) # Returns a dict mapping (title, year) to box office for top grossing movies
    totals = {}
    for title, year, director, actors in read_casts(casts_file): # Returns a list of (title, year, director, actors) from the casts file
        if (title, year) not in box_office:
            continue
        for actor in actors:
            totals[actor] = totals.get(actor, 0) + box_office[(title, year)] # adds earnings from every movie

    ranking = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    print_ranking("Top actors by total box office earnings", ranking) # limit to top ten for screenshot [:10] but removed for final code


def main():

    folder = os.path.dirname(__file__)
    rated = os.path.join(folder, "imdb-top-rated.csv")
    grossing = os.path.join(folder, "imdb-top-grossing.csv")
    casts = os.path.join(folder, "imdb-top-casts.csv")

    # question 1a test:
    display_top_collaborations(rated, casts)
    print("")

    # question 1b test:
    display_top_actors(grossing, casts)
    print("Jacob Marrale , 23779685")


if __name__ == "__main__":
    main()