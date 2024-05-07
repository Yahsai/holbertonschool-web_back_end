export default function createReportObject(employeesList) {
    const allEmployees = {};
    const departments = [];
  
    for (const [department, employees] of Object.entries(employeesList)) {
      allEmployees[department] = employees;
      departments.push(department);
    }
  
    const getNumberOfDepartments = () => departments.length;
  
    return {
      allEmployees,
      getNumberOfDepartments,
    };
  }
