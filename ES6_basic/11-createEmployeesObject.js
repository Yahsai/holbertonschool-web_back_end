export default function createEmployeesObject(departmentName, employees) {
    if (typeof departmentName !== 'string' || !Array.isArray(employees)) {
      throw new Error('Invalid arguments');
    }
    return {
      [departmentName]: employees
    };
  }
  