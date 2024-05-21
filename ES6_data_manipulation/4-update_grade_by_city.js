function updateStudentGradeByCity(students, city, grade) {
    return students.map((student) => {
        const newGrade = grade.find((item) => item.studentId === student.id);
        if (newGrade) {
        return {
            ...student,
            grade: newGrade.grade,
        };
        }
        return student;
    });
}

export default updateStudentGradeByCity;