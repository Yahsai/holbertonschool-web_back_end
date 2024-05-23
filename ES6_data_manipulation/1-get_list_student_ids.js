export default function getListStudentIds(arr) {
  return Array.isArray(arr) ? arr.map((el) => el.id) : [];
}
