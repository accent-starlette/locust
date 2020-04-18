from locust import between, HttpLocust, task, TaskSet


class UserBehavior(TaskSet):

    def on_start(self):
        self.client.post(
            "/login", {
                "email": "admin@example.com",
                "password": "password"
            }
        )

    def on_stop(self):
        self.client.get("/logout")

    @task(1)
    def index(self):
        self.client.get("/")
    
    @task(1)
    def restricted(self):
        self.client.get("/restricted")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 10)
