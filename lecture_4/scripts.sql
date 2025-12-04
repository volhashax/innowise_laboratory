-- Create tables

-- Table 1: students
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
        CHECK (birth_year >= 1900)
);

-- Table 2: grades
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade BETWEEN 1 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Indexes

CREATE INDEX IF NOT EXISTS idx_grades_student_id
    ON grades(student_id);

CREATE INDEX IF NOT EXISTS idx_grades_subject
    ON grades(subject);

-- Insert Sample Data

-- Students
INSERT INTO students (full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- Grades
INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

-- Queries

-- Find all grades for a specific student (Alice Johnson)
SELECT
    s.id,
    s.full_name,
    s.birth_year,
    GROUP_CONCAT(gd.subject_grade, ', ') AS grades
FROM students s
LEFT JOIN (
    SELECT DISTINCT student_id, subject || ': ' || grade AS subject_grade
    FROM grades
) gd ON s.id = gd.student_id
WHERE s.full_name = 'Alice Johnson'
GROUP BY s.id, s.full_name, s.birth_year
ORDER BY s.id;

-- Calculate the average grade per student
SELECT
    s.id,
    s.full_name,
    AVG(g.grade) AS average_grade
FROM students s
LEFT JOIN (
    SELECT DISTINCT student_id, subject, grade
    FROM grades
    WHERE grade IS NOT NULL
) g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC;

-- All students born after 2004
SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year;

-- All subjects and their average grades
SELECT subject, AVG(grade) AS average_grade
FROM (
    SELECT DISTINCT student_id, subject, grade
    FROM grades
    WHERE grade IS NOT NULL
) AS unique_grades
GROUP BY subject
ORDER BY average_grade DESC;

-- Top 3 students with the highest average grades
SELECT s.id, s.full_name, AVG(g.grade) AS average_grade
FROM students s
JOIN (
    SELECT DISTINCT student_id, subject, grade
    FROM grades
    WHERE grade IS NOT NULL
) g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

-- All students who have scored below 80 in any subject
SELECT DISTINCT s.id, s.full_name, s.birth_year
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade IS NOT NULL AND g.grade < 80
ORDER BY s.id;