export default function getStudentIdsSum(obj) {
    const idArr = obj.map((student) => student.id);
    return idArr.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  }
