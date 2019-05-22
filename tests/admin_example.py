from locust import HttpLocust, task, TaskSet


class UserBehavior(TaskSet):

    @task(1)
    def admin_index(self):
        self.client.get("/admin")

    @task(2)
    def list(self):
        self.client.get("/admin/example/demos")

    @task(1)
    def create_get(self):
        self.client.get("/admin/example/demos/create")

    @task(1)
    def create_post(self):
        self.client.post(
            "/admin/example/demos/create",
            data={"name": "Locust", "description": "Description"}
        )

    @task(1)
    def update_get(self):
        self.client.get("/admin/example/demos/1/update")

    @task(1)
    def update_post(self):
        self.client.post(
            "/admin/example/demos/1/update",
            data={"name": "Record 1", "description": "Description"}
        )


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
