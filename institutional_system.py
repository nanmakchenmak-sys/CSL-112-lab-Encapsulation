# Name: Mark Nanmak Chenmak
# Matric Number: FUEP/2025/CSE/0196
# Course: CSL 112
# File: institutional_system.py

from abc import ABC, abstractmethod

# Abstract Base Class
class User(ABC):
    def __init__(self, user_id, full_name, email):
        self._user_id = user_id
        self._full_name = full_name
        self._email = email

    def __str__(self):
        return f"ID: {self._user_id}, Name: {self._full_name}, Email: {self._email}"

    @abstractmethod
    def calculate_monthly_payout(self):
        pass


# StudentUser Class
class StudentUser(User):
    def __init__(self, user_id, full_name, email, stipend_rate, courses_enrolled):
        super().__init__(user_id, full_name, email)
        self.__stipend_rate = stipend_rate
        self.__courses_enrolled = courses_enrolled

    def calculate_monthly_payout(self):
        return self.__stipend_rate * 0.98


# LecturerUser Class
class LecturerUser(User):
    def __init__(self, user_id, full_name, email, base_salary, overtime_hours, hourly_rate):
        super().__init__(user_id, full_name, email)
        self.__base_salary = base_salary
        self.__overtime_hours = overtime_hours
        self.__hourly_rate = hourly_rate

    def calculate_monthly_payout(self):
        return self.__base_salary + (self.__overtime_hours * self.__hourly_rate)


# ResearchAssistant Class
class ResearchAssistant(StudentUser):
    def __init__(self, user_id, full_name, email, stipend_rate, courses_enrolled, research_grant_allowance):
        super().__init__(user_id, full_name, email, stipend_rate, courses_enrolled)
        self.__research_grant_allowance = research_grant_allowance

    def calculate_monthly_payout(self):
        return super().calculate_monthly_payout() + self.__research_grant_allowance