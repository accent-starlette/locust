from locust import HttpLocust, task, TaskSet


class UserBehavior(TaskSet):

    def on_start(self):
        self.client.post(
            "/auth/login", {
                "email": "admin@example.com",
                "password": "password"
            }
        )

    def on_stop(self):
        self.client.get("/auth/logout")

    @task(1)
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
