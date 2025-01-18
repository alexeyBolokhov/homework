# Задание "Свой YouTube":

class Video:
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode = False):
    #Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
    # adult_mode(ограничение по возрасту, bool (False по умолчанию))
        self.title = title  # атрибут заголовок
        self.duration = duration  # атрибут продолжительность
        self.time_now = time_now  # атрибут секунда остановки
        self.adult_mode = adult_mode  # атрибут ограничение по возрасту

    def __eq__(self, other): #магич метод ==
        return self.title == other.title

    def __contains__(self, item): #проверка принадлежности с помощью contains
        return item in self.title

class User:
    def __init__(self, nickname: str, password: int, age: int):
        #Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
        self.nickname = nickname  # атрибут имя пользователя
        self.password = hash(password)  # атрибут пароль
        self.age = age  # атрибут возраст
    def __str__(self):
        return self.nickname

class UrTube:
    def __init__(self):
    # Атриубты: users(список [] объектов User), videos(список [] объектов Video), current_user(текущий пользователь User None- пусто)
        self.users = []  # атрибут список объектов User
        self.videos = []  # атрибут список объектов Video
        self.current_user = None  # атрибут текущий пользователь User
    def log_in(self,nickname, password): # метод
        for i in self.users:
            if nickname in i and password in i: # ищем пользователя и пароль
                self.current_user = nickname # если найден меняем текущего на найденный
    def log_out(self): # метод для сброса текущего пользователя на None
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        #flag = True
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user


    ##################
    def add(self, *args):
        #принимает неограниченное кол-во объектов класса Video и все добавляет в videos
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def get_videos(self, text: str):
        list_movie = []
        for i in self.videos:
            if isinstance(i, Video):
                title = i.title
                if text.upper() in title.upper():
                    list_movie.append(title)
            else:
                continue
        return list_movie

    def watch_video(self, movie: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(x.duration):
                    print(i, end=' ')
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')
# проверяем
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
#print(ur.v)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
