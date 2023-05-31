from locust import HttpUser, task

class ServerLoadTest(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/", verify=False)
        self.client.get("/admin", verify=False)
