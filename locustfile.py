from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/", verify=False)
        self.client.get("/world", verify=False)
