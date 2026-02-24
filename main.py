data = {

  "Alan": {
    "task_name": "Model Training",
    "status": "Pending"
  },

  "John Doe": {
    "task_name": "Data Preprocessing",
    "status": "Pending"
  },

  "Basim": {
    "task_name": "Cloud Deployment",
    "status": "Pending"
  }

}

########################################


def add_employee(employee_name):

    data[employee_name] = {
      "task_name": "TBA",
      "status": "Pending"
    }

    return "New Employee Added!!"


def assign_task(employee_name, task_name):
    if employee_name not in data.keys():
        return "employee doesn't exists"

    data[employee_name] = {
        "task_name": task_name,
        "status": "Pending"
    }

    return "New Task Assigned!!"


def complete_task(employee_name, task_name=""):

    if employee_name not in data.keys():
        return "employee doesn't exists"

    data[employee_name]["status"] = "Completed"

    return "Task marked as Completed!"


def get_employee_tasks(employee_name):
    return data[employee_name]["task_name"]


def get_pending_tasks():
    incomp = dict({})
    for emp in data:
        if data[emp]["status"] == "Pending":
            incomp[emp] = data[emp]["task_name"]

    return incomp



