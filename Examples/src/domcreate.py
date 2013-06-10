from xml.dom.minidom import Document

doc = Document()

employees = doc.createElement('employees')
doc.appendChild(employees)

employeeRecord = doc.createElement('person')
employeeRecord.attributes['ssn'] = '111223333'
employeeRecord.attributes['empid'] = '12345'
employees.appendChild(employeeRecord)

firstName = doc.createElement('first')
firstNameText = doc.createTextNode('Jane')
firstName.appendChild(firstNameText)
employeeRecord.appendChild(firstName)

lastName = doc.createElement('last')
lastNameText = doc.createTextNode('Doe')
lastName.appendChild(lastNameText)
employeeRecord.appendChild(lastName)

print doc.toprettyxml(indent = '     ', encoding = 'UTF-8')


