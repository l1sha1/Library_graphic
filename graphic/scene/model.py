class Scene:
    def __init__(self, shapes=None):
        path = input("Введите путь до сценария ")
        new_file = open(path, 'r')
        scene = new_file.read()
        scene = scene.replace("\n", " ")
        scene_new = scene.split(' ')
        self.__shapes = [scene_new[2]] or []
        self.num_fig = scene_new[1]
        if scene_new[2] == "circle":
            self.x = int(scene_new[3])
            self.y = int(scene_new[4])
            self.radius = int(scene_new[5])
            self.color = (int(scene_new[6]), int(scene_new[7]), int(scene_new[7]))

    def add(self, new_shape):
        self.__shapes.append(new_shape)

    def draw(self):
        for shape in self.__shapes:
            shape.draw()
            
            
            
            
            
            


            
