from locust import between, HttpLocust, task, TaskSet


class UserBehavior(TaskSet):

    def on_start(self):
        response = self.client.post(
            "/api/token", {
                "username": "admin@example.com",
                "password": "password"
            }
        )
        bearer = response.json()["access_token"]
        self.headers = {"Authorization": f"Bearer {bearer}"}

    @task(1)
    def users_me(self):
        self.client.get("/api/users/me", headers=self.headers)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 10)
