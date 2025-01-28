from Course import Course

class Queue_wait():
    def __init__(self, queue: list, course_of_queue, id: int):
        self._id = id  # מזהה ייחודי
        self._queue = queue  # שימוש במשתנה פנימי
        self._course_of_queue = course_of_queue  # קורס משויך לתור

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        if isinstance(new_id, int) and new_id > 0:
            self._id = new_id
        else:
            raise ValueError("ID must be a positive integer.")

    @property
    def queue(self):
        return self._queue

    @queue.setter
    def queue(self, queue):
        if isinstance(queue, list):
            self._queue = queue  # עדכון המשתנה הפנימי
        else:
            raise ValueError("Queue must be a list.")

    @property
    def course_of_queue(self):
        return self._course_of_queue

    @course_of_queue.setter
    def course_of_queue(self, course):
        if isinstance(course, Course):
            self._course_of_queue = course  # עדכון משתנה פנימי
        else:
            raise ValueError("Course must be an instance of Course class.")

    def __str__(self):
        return f'Queue [id : {self.id} , course : {self.course_of_queue.name} , number of student in list : {len(self.queue)} ]'
