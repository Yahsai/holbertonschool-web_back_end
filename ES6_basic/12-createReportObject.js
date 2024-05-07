export default function createReportObject(employeesList) {
    // Verificación de parámetros
    if (typeof employeesList !== 'object' || employeesList === null) {
      throw new Error('Invalid argument: employeesList must be an object');
    }
  
    return {
      allEmployees: {
        ...employeesList
      },
      // Devuelve el número de departamentos
      getNumberOfDepartments() {
        return Object.keys(this.allEmployees).length;
      }
    };
  }
  
