class Player:
    def __init__(self):
        self.player_name = "person"
        self.emotions = []
        
        # to keep track at which task the player is
        # increment after each combat
        # should prob be int?
        self.current_project = 1
        self.current_task = 0
        # saves info about which task from which project is done
        # {project_id: {task_id:status, ...}...}
        self.tasks_state = {1: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
                            2: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, 
                            3: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}}
    

    def get_finished_projects(self):
        # loops over tasks_state and decides which projects are finished
        # the id of the finished projects get returned

        finished_projects = []
        for project, tasks in self.tasks_state.items():
            if all(status == 1 for task, status in tasks.items()):
                finished_projects.append(project)
        return finished_projects


    def add_emotion(self, emotion: object):
        self.emotions.append(emotion)
