#!/usr/bin/env python3
"""Defines course selection module.

Module defines CourseSelection class which can be used to create a course
selection object or deserialize/parse a course selection string into a
CourseSelection object.

CourseSelection object is composed of Department, Course Number, Semester and
Year.

Input:
Department is one or more alphabetic charecters.

Course number is a number.

Semester is one of F (Fall), W (Winter), S (Spring), Su (Summer).
If short form is used then it is converted to normalized form.

Year is either in the form of yyyy or yy.
If year is yy then it is prefixed with 20 for convert to yyyy format.
"""

import dataclasses
import enum
import logging
import re
import typing


class SemesterEnum(enum.Enum):
    """Enumerator for semesters."""
    WINTER = 'winter'
    SPRING = 'spring'
    SUMMER = 'summer'
    FALL = 'fall'


SEMESTER_LIST = list((SemesterEnum.FALL.value, SemesterEnum.WINTER.value,
                      SemesterEnum.SPRING.value, SemesterEnum.SUMMER.value))


SEMESTER_SHORT_FORM_MAP = {
    'w': SemesterEnum.WINTER.value,
    's': SemesterEnum.SPRING.value,
    'su': SemesterEnum.SUMMER.value,
    'f': SemesterEnum.FALL.value,
}
VALID_SEMESTERS = frozenset(tuple(SEMESTER_SHORT_FORM_MAP.keys()) +
                            tuple(SEMESTER_SHORT_FORM_MAP.values()))

DEPARTMENT_REGEX = '(?P<department>[a-z]+)'
COURSE_NUMBER_REGEX = '(?P<course_number>[\d]+)'
SEMESTER_REGEX = '(?P<semester>{regex})'.format(regex='|'.join(VALID_SEMESTERS))
YEAR_REGEX = '(?P<year>[\d]{4}|[\d]{2})'
DEPARTMENT_COURSE_REGEX = f'^{DEPARTMENT_REGEX}[-: ]?{COURSE_NUMBER_REGEX} '
SEMESTER_YEAR_REGEX = f' {SEMESTER_REGEX}[ ]?{YEAR_REGEX}'
YEAR_SEMESTER_REGEX = f' {YEAR_REGEX}[ ]?{SEMESTER_REGEX}'


class CourseSelectionParseError(Exception):
    """Error to be raised in case of course selection parsing issues."""
    pass


CourseSelectionType = typing.TypeVar(
    'CourseSelectionType', bound='CourseSelection')


@dataclasses.dataclass
class CourseSelection:
    """Defines a course selection data model.

    Atrributes:
      department: The department of the course.
      course_number: The course number.
      semester: The course semester.
      year: The course semester year.
    """
    department: str
    course_number: int
    semester: str
    year: int

    def __post_init__(self):
        """Post init data normalizaion."""
        self.normalize()

    def normalize(self):
        """Normalizes class atrributes.

        Raises:
          ValueError: If the atrributes are incorrect.
        """
        self.department = self.department.upper()
        self.course_number = int(self.course_number)

        semester = self.semester.lower()
        if semester not in VALID_SEMESTERS:
            raise ValueError(
                f'Invalid semester {self.semester} expected one of '
                '%s.' % (', '.join(VALID_SEMESTERS)))
        if semester in SEMESTER_SHORT_FORM_MAP:
            semester = SEMESTER_SHORT_FORM_MAP[semester]
        self.semester = semester.title()

        year = str(self.year)
        if len(year) != 4:
            if len(year) == 2:
                year = f'20{year}'
            else:
                raise ValueError(
                    f'year {self.year} must be either yyyy or yy format.')
        self.year = int(year)

    @classmethod
    def from_string(cls, string: str) -> CourseSelectionType:
        """Creates a course selection object parsing the string.

        Examples string formats:
        “CS111 2016 Fall”
        “CS-111 Fall 2016”
        “CS 111 F2016”

        Args:
          string: The string course selection.

        Returns:
          The deserialized course selection object.

        Raises:
          CourseSelectionParseError: If course selection parsing failed.
        """
        if not string:
            raise CourseSelectionParseError(
                'The course selection string was empty.')

        dept_course_parser = re.compile(DEPARTMENT_COURSE_REGEX, re.IGNORECASE)
        dept_course_match = dept_course_parser.search(string)
        if dept_course_match is None:
            logging.error(
                'String %s did not conform to course selection format.',
                string)
            raise CourseSelectionParseError(
                'Invalid course selection format.')

        semester_year_parser = re.compile(SEMESTER_YEAR_REGEX, re.IGNORECASE)
        semester_year_match = semester_year_parser.search(string)
        if semester_year_match is None:
            year_semester_parser = re.compile(
                YEAR_SEMESTER_REGEX, re.IGNORECASE)
            semester_year_match = year_semester_parser.search(string)
            if semester_year_match is None:
                logging.error(
                    'String %s did not conform to course selection format',
                    string)
                raise CourseSelectionParseError(
                    'Invalid course selection format.')

        department = dept_course_match.group('department')
        course_number = dept_course_match.group('course_number')
        semester = semester_year_match.group('semester')
        year = semester_year_match.group('year')
        return cls(department, course_number, semester, year)

    def __eq__(self, other):
        return (self.year == other.year and
                self.semester == other.year and
                self.department == other.department and
                self.course_number == other.course_number)

    def __lt__(self, other):
        return (self.year < other.year or
                SEMESTER_LIST.index(self.semester.lower()) < SEMESTER_LIST.index(other.semester.lower()) or
                self.department < other.department or
                self.course_number < other.course_number)


if __name__ == '__main__':
    course_names = (
        'CS888 S16', 'AC-888 S2016', 'CS 777 2016SU',
        'CS:666 16F', 'CS:555 2016 W', 'CS:444 W 2006', 'CS:333 16 fall',
        'CS:222 16 f', 'CS:111 2016 S', 'hh-88909 FalL 04'
    )
    all_c = []
    for name in course_names:
        course_selection = CourseSelection.from_string(name)
        all_c.append(course_selection)
    for c in sorted(all_c):
        print(c)
