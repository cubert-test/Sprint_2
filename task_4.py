class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours=None, rest_day=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_day = rest_day
        self.email = email

    def get_hours(self):
        if self.hours is not None:
            return self.hours
        else:
            return (7 - self.rest_day) * 8

    def get_email(self):
        if self.email is not None:
            return self.email
        else:
            return f"{self.name}@email.com"

    @classmethod
    def set_hourly_payment(cls, new_rate):
        cls.hourly_payment = new_rate

    def salary(self):
        actual_hours = self.get_hours()
        payment_rate = self.hourly_payment
        return actual_hours * payment_rate