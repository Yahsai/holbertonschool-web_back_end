function getListStudentIds(studentList) {
    if (!Array.isArray(studentList)) {
        return [];
    }
    return studentList.map(student => student.id);
}

// Example usage
const students = [
    { id: 1, name: 'Alice', age: 20 },
    { id: 2, name: 'Bob', age: 22 },
    { id: 3, name: 'Charlie', age: 23 }
];

console.log(getListStudentIds(students)); // Output: [1, 2, 3]

