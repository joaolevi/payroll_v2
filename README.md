# Projeto de Software 2020.1 part II
## Professor Baldoino Fonseca dos Santos

## Código inicial -> src/main.py

### Code Smells

1. Long Method:
  1.1 The size of the parameter list
	1.2 You are getting several values from an object and
	passing these values as parameters in a method call
	1.3 You have a group of parameters that
	naturally go together - Data Clumps
	1.4 A method is trying to do too much
	1.5 The amount of switch statement for dispatching
	and handling request
	1.6 The amount of switch statement to gather data from
	numerous classes with different interfaces
	1.7 The amount of switch statement to gather data from
	numerous classes with different interfaces
	
2. Large Class:
	Fields and methods

3. Shotgun Surgery:
	When every time you make a kind of change, you have to make a lot of
	Little changes to a lot of different classes

4. Feature Envy:
	A method that seems more interested in a class
	other than the one it actually is in.

5. Lazy Class:
	A class that is not doing enough to pay for itself.

6. Message Chains:
	Example: object.getE().getD().getC().getB().getA().getValue();

*7. Indecent Exposure:
	Methods or classes that ought not to be visible to clients are
	publicly visible to them
	
## Code Smells
#### 1. Bad Smell: Large Class
No projeto não-refatorado foi criada uma classe [Company][1] que contemplava todas as possíveis funções solicitadas no projeto, desde a função 1 a 9. Dessa forma, a classe assumiu um tamanho muito extenso que fugia dos padrões de código, tanto na quantidade de atributos quanto na quantidade de métodos.

Da mesma forma a classe [Employee][10] estava responsável por 12 atributos e diversas funções.
##### 1. Solution:
A classe Company foi dividida em outras 3 classes que assumiram seus respectivos papeis diminuindo a responsabilidade colocada em cima da antiga classe.

A organização do pacote ficou:

-- Company/[Departaments][2]/"classes"
As funções referentes ao setor de RH de uma empresa, como: Add employee, remove employee, change employee details, foram colocadas na nova classe [HumanResourcers][3]. As funções concernentes a um setor financeiro de uma empresa foram então colocadas na classe [Finances][4], ou seja, funções de pagamento, registro de vendas, dados financeiros dos empregados e etc. Por último, foram colocadas as funções da área administrativa de uma empresa como as funções em relação as agendas de pagamento na classe [Administration][5].

A classe [[11]][Employee] Employee no novo código passou a ter apenas 4 atributos e mais 3 atributos só que agora herdados da classe mãe (BankData - dados bancários). Os demais atributos ficaram sendo de responsabilidade das classes Departaments de mantê-los registrados.

#### 2. Bad Smell: Long Method
###### 2.2 Quando um método tenta fazer muita coisa:
Na classe Company do primeiro código, existiam funções como pay_employees e payday_employee_method que cumpriam seu papel porém, para elaborar um resultado ela precisava fazer várias verificações de condições pois não existiam funções que faziam isso por ela.

##### 2.2 Solution:
A solução para diminuir a quantidade de atribuições de uma função, foi a criação de uma pasta de classes "Ferramentas de Registro" onde cada classe da pasta DEPARTAMENTS teria uma classe que conteplasse funções de suporte, ou seja, que teriam o uso repetitivo nas demais funções. Assim como, também, como o próprio nome já diz, ter o registro dos dados concernente de cada departamento da compania.

O caminho, por tanto, ficou:
-- Company/[RegisterTools][6]/"classes"

Dessa forma, a classe Finances necessitava de uma ferramenta que tivesse o registro dos dados financeiros dos empregados e funções que acessassem e devolvessem tais dados. A classe criada foi [EmployeesPayCheck][7].
Enquanto que a classe HumanResourcers precisava de uma classe para ter o registro de dados pessoais dos empregados e funções de acesso a tais dados.
A classe criada foi [EmployeesRegister][8].

Essas ferramentas só estavam acessíveis as classes responsáveis por elas, no caso:

Finances -> EmployeesPayCheck
HumanResourcers -> EmployeesRegister

Não era possível acessar através de outra classe: Finances -x> EmployeesRegister.

##### 2.3. Quantidade de IF's muito grande:
Como o python não contempla a função "switch", foi-se necessário criar funções que tivessem diversos casos de if-else para verificar as condições e elaborar as saídas.
Mas ainda assim 



[1]: https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/Company/Company.py "Company"
[2]: https://github.com/joaolevi/payroll_v2/tree/main/src/Company/Departments "Departaments"
[3]: https://github.com/joaolevi/payroll_v2/blob/main/src/Company/Departments/HumanResourcers.py "HumanResourcers"
[4]: https://github.com/joaolevi/payroll_v2/blob/main/src/Company/Departments/Finances.py "Finances"
[5]: https://github.com/joaolevi/payroll_v2/blob/main/src/Company/Departments/Administration.py "Administration"
[6]: https://github.com/joaolevi/payroll_v2/tree/main/src/Company/RegisterTools "RegisterTools"
[7]: https://github.com/joaolevi/payroll_v2/blob/main/src/Company/RegisterTools/EmployeesPayCheck.py "EmployeesPayCheck"
[8]: https://github.com/joaolevi/payroll_v2/blob/main/src/Company/RegisterTools/EmployeesRegister.py "EmployeesRegister"
[10]: https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/Employees/Employee.py "Employee"
[Employee]: https://github.com/joaolevi/payroll_v2/blob/main/src/Employees/Employee.py "Employee"
