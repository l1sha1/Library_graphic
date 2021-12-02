class FileLoadder:
    def load_scene(self):
        new_file = open(input("Введите путь до сценария "), 'r')
        scene = new_file.readlines()
        for j in range(len(scene)):
            for i in range(len(scene[j])):
                if scene[j][i] == ' ' and (scene[j][i + 1] == ' ' or scene[j][i + 1] == '/'):
                    scene[j] = scene[j][:i]
                    break
            for i in range(len(scene[j])):
                if scene[j][i] == "\n":
                    scene[j] = scene[j][:i]
                    break
        scene = ','.join(scene)
        scene = scene.replace(",", " ")
        scene_new = scene.split(' ')
        scene_new.insert(2, '')
        return scene_new

    def save_scene(self):
        pass
