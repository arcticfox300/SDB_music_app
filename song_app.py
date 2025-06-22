class Song:
    def __init__(self, title, artist, genre, duration):
        self.__title = title
        self.__artist = artist
        self.__genre = genre
        self.__duration = duration

    def title(self):
        return self.__title

    def artist(self):
        return self.__artist

    def genre(self):
        return self.__genre

    def duration(self):
        return self.__duration

def print_commands():
    print("1. Add song")
    print("2. Delete song")
    print("3. Average durations song")
    print("4. Print all song")
    print("5. Most popular genre")
    print("6. Exit")


def read_song():
    title = input("title: ")
    artist = input("artist: ")
    genre = input("genre: ")
    duration = input("duration: ")

    return Song(title, artist, genre, duration)

def add_new_song(song, play_list):
    play_list.append(song)

def delete_song(song, play_list):
    position = -1
    for index in range(len(play_list)):
        track_title = play_list[index].title()
        if (track_title == song):
            position = index

    if position != -1:
        del play_list[position]
    else:
        print("track not found")

def print_all_songs(play_list):
    for index in range(len(play_list)):
        track = play_list[index]
        print(f"title: {track.title()}, artist: {track.artist()}, genre: {track.genre()}, duration: {track.duration()}")


def avrage_duration(play_list):
    sum = 0
    count = 0

    for index in range(len(play_list)):
        track = play_list[index]
        count += 1
        sum += int(track.duration())

    return sum / count


def most_popular_genre(play_list):
    genres = {}
    for index in range(len(play_list)):
        genre = play_list[index].genre()
        if genre not in genres:
            genres[genre] = 1
        else:
            genres[genre] += 1

    maxx = 0
    most_frequent = ""
    for genre in genres:
        if genres[genre] > maxx:
            maxx = genres[genre]
            most_frequent = genre

    return most_frequent

def run():
    play_list = []

    while True:
        print_commands()
        current_command  = input("Choose action ")
        try:
            command  = int(current_command )
            if command == 1:
                new_song = read_song()
                add_new_song(new_song, play_list)
            if command == 2:
                to_delete = input("choose song: ")
                delete_song(to_delete, play_list)
            if command == 3:
                print(avrage_duration(play_list))
            if command == 4:
                print_all_songs(play_list)
            if command == 5:
                print(most_popular_genre(play_list))
            if command == 6:
                break
        except ValueError as ve:
            print(f"{current_command } is not a valid command. Try again")

run()

