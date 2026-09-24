class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours=None, rest_day=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_day = rest_day
        self.email = email

    @classmethod
    def get_hours(cls, employee_instance):
        if employee_instance.hours is not None:
            return employee_instance.hours
        else:
            return (7 - employee_instance.rest_day) * 8

    @classmethod
    def get_email(cls, employee_instance):
        if employee_instance.email is not None:
            return employee_instance.email
        else:
            return f"{employee_instance.name}@email.com"

    @classmethod
    def set_hourly_payment(cls, new_rate):
        cls.hourly_payment = new_rate

    def salary(self):
        actual_hours = EmployeeSalary.get_hours(self)
        payment_rate = self.hourly_payment
        return actual_hours * payment_rate
