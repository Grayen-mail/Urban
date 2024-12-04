"""Дополнительное практическое задание по модулю"""


from time import sleep


class User:
    """ Класс User """
    def __init__(self, nickname: str, password: str, age: int) -> None:
        """В экземпляре храним имя, хеш пароля и возраст"""
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self) -> str:
        """ Представление класса в виде строки с именем пользователя"""
        return self.nickname

    def __eq__(self, other) -> bool:
        """ Проверяем только объекты класса и строковое представление"""
        if isinstance(other, User):
            return self.nickname == other.nickname
        elif isinstance(other, str):
            return self.nickname == other
        else:
            return False


class Video:
    """ Класс Video """
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False) -> None:
        """ В экземпляре сохраняем заголовок, продолжительность,
        текущую позицию, признак ограничения по возрасту 18"""
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        """ Представление класса в виде строки с названием видео"""
        return self.title

    def __eq__(self, other):
        """ Проверяем только объекты класса и строковое представление"""
        if isinstance(other, Video):
            return self.title == other.title
        elif isinstance(other, str):
            return self.title == other
        else:
            return False


class UrTube:
    """ Класс UrTube """ 
    
    def __init__(self, ) -> None:
        """ В экземпляре хранит список видео, список зарегистрированных
        пользователей и текущего пользователя"""
        self.videos: list[Video] = []
        self.users: list[User] = []
        self.current_user: User | None = None

    def log_in(self, nickname: str, password: str) -> bool:
        """ Вход по имени и паролю"""
        if nickname in self.users:
            user = self.users[self.users.index(nickname)]
            if user.password == hash(password):
                self.current_user = user
                # print(f'Вошел пользователь с именем {nickname}')
                return True
            else:
                # print('Пароль пользователя указан неверно')
                return False
        else:
            # print('Пользователь не зарегистрирован')
            return False

    def register(self, nickname: str, password: str, age: int) -> bool:
        """ Регистрация нового пользователя с логином, паролем и возрастом.
            Длина имени 3 и более знаков, пароля - 8 и более знаков.
            При успешной регистрации автоматический вход.
            Если регистрация не удалась или пользователь существует,
            текущий пользователь не изменяется"""
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
            return False
        else:
            if len(nickname) < 3:
                # print('Имя пользователя должно быть длиной 3 и более знаков')
                return False
            elif len(password) < 8:
                # print('Пароль должен быть длиной 8 и более знаков')
                return False
            else:
                self.users.append(User(nickname, password, age))
                if self.log_in(nickname, password):
                    return True
                else:
                    return False

    def log_out(self):
        """ Выход текущего пользователя"""
        self.current_user = None

    def add(self, *video_tuple: Video) -> None:
        """ Добавляем видео, если название больше 3 знаков
        и продолжительность больше 0"""
        for video in video_tuple:
            if (video not in self. videos and
                    len(video.title) > 3 and video.duration > 0):
                self.videos.append(video)

    def get_videos(self, search_string: str) -> list[Video]:
        """ Поиск видео по частичному названию без учёта регистра,
            возвращает список найденных видео"""
        ret_value = []
        for video in self.videos:
            if search_string.lower() in video.title.lower():
                ret_value.append(video)
        return ret_value

    def watch_video(self, video_name: str) -> None:
        """ Просмотр видео, название которого полностью соответствует запросу
            Пользователь должен войти в UrTube"""
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if video_name in self.videos:
            list_index = self.videos.index(video_name)
            if self.videos[list_index].adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                for i in range(1, self.videos[list_index].duration + 1):
                    self.videos[list_index].time_now = i
                    print(i, end=' ')
                    sleep(0.1)
                print('Конец видео')
        else:
            #  print('Видео не существует')
            pass


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
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
    # print (ur.videos)
    # v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # ur.add(v1, v2)
    # print(ur.videos)
