class EmployeeSalary:
    def __init__(self, name, hours=None, rest_day=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_day = rest_day
        self.email = email

    hourly_payment = 400

    def get_hours(self, hours, rest_day):
        if hours is not None:
            return hours
        else:
            return (7 - rest_days) * 8


    def get_email(self):
        if self.email is not None:
            return self.email
        else:
            return f"{self.name}@email.com"

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        actual_hours = self.get_hours()
        return actual_hours * self.hourly_payment



