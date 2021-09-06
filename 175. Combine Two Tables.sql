select Person.FirstName,Person.Lastname,Address.City,Address.State from Person 
left join Address 
on person.PersonId = Address.PersonId
