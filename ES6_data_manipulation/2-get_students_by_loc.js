export default function getStudentsByLocation(obj, city = '') {
    return obj.filter((student) => student.location === city);
  }