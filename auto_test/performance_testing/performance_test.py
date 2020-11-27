from locust import HttpLocust,TaskSet,task

class UserAction(TaskSet):

    @task
    def login(self):
        body = {'username':'admin','password':'admin123'}
        res = self.client.post("/JavaPrj_6/login.do",data=body)
        print(res)

# def WebSiteUser(self):

class WebSiteUser(HttpLocust):
    task_set = UserAction
    host = "http://127.0.0.1:8080"
    min_wait = 1000
    max_wait = 2000


