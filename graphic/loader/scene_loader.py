class FileLoadder:
    def load_scene(self):
        path = input("Введите путь до сценария ")
        new_file = open(path, 'r')
        scene = new_file.read()
        scene = scene.replace("\n", " ")
        scene_new = scene.split(' ')
        return scene_new

    def save_scene(self):
        pass
