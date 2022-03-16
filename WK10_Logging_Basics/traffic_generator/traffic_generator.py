from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)  # will make the simulated users wait between 5 and 9 seconds

    # @task is the key. For every running user, Locust creates a greenlet (micro-thread), that will call those methods.
    # @task(5) indicates the weight is 5.
    @task
    def error_page(self):
        self.client.get("/test1/")

    @task(20)
    def success_page(self):
        self.client.get("/test/")

    def on_start(self):
        pass
