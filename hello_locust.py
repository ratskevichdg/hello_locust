from locust import HttpUser, TaskSet, task
 
class UserBehavior(TaskSet):
 
    @task
    def visit_website(self):
        self.client.get("/")
 
class WebsiteUser(HttpUser):
    # task_set = UserBehavior
    tasks = [UserBehavior]