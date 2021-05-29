# Projeto de Software 2020.1 part II
## Professor Baldoino Fonseca dos Santos

## Código inicial -> src/main.py

## Code Smells
#### 1. Large Class
No projeto não-refatorado foi criada uma classe [Company](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/Company/Company.py "Company") que contemplava todas as possíveis funções solicitadas no projeto, desde a função 1 a 9. Dessa forma, a classe assumiu um tamanho muito extenso que fugia dos padrões de código, tanto na quantidade de atributos quanto na quantidade de métodos.

Da mesma forma a classe [Employee](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/Employees/Employee.py "Employee") estava responsável por 12 atributos e diversas funções.
##### 1. Solution:
A classe Company foi dividida em outras 3 classes que assumiram seus respectivos papeis diminuindo a responsabilidade colocada em cima da antiga classe.

A organização do pacote ficou:

-- Company/[Departaments](https://github.com/joaolevi/payroll_v2/tree/main/src/Company/Departments "Departaments")/"classes"
As funções referentes ao setor de RH de uma empresa, como: Add employee, remove employee, change employee details, foram colocadas na nova classe [HumanResourcers](https://github.com/joaolevi/payroll_v2/blob/main/src/Company/Departments/HumanResourcers.py "HumanResourcers"). As funções concernentes a um setor financeiro de uma empresa foram então colocadas na classe [Finances](https://github.com/joaolevi/payroll_v2/blob/main/src/Company/Departments/Finances.py "Finances"), ou seja, funções de pagamento, registro de vendas, dados financeiros dos empregados e etc. Por último, foram colocadas as funções da área administrativa de uma empresa como as funções em relação as agendas de pagamento na classe [Administration](https://github.com/joaolevi/payroll_v2/blob/main/src/Company/Departments/Administration.py "Administration").

A classe [Employee](https://github.com/joaolevi/payroll_v2/blob/main/src/Employees/Employee.py "Employee") no novo código passou a ter apenas 4 atributos e mais 3 atributos só que agora herdados da classe mãe (BankData - dados bancários). Os demais atributos ficaram sendo de responsabilidade das classes Departaments de mantê-los registrados.

#### 2. Long Method
##### 2.2 Quando um método tenta fazer muita coisa:
Na classe Company do primeiro código, existiam funções como [pay_employees](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/3b9b5a048c55638f2e6d31de55720098e3be649c/src/Company/Company.py#L149 "pay_employees") e [payday_employee_method](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/3b9b5a048c55638f2e6d31de55720098e3be649c/src/Company/Company.py#L130 "payday_employee_method") que cumpriam seu papel porém, para elaborar um resultado ela precisava fazer várias verificações de condições pois não existiam funções que faziam isso por ela.

###### 2.2 Solution:
A solução para diminuir a quantidade de atribuições de uma função, foi a criação de uma pasta de classes "Ferramentas de Registro" onde cada classe da pasta DEPARTAMENTS teria uma classe que conteplasse funções de suporte, ou seja, que teriam o uso repetitivo nas demais funções. Assim também, como o próprio nome já diz, ter o registro dos dados concernentes de cada departamento da compania.

O caminho, por tanto, ficou:
-- Company/[RegisterTools](https://github.com/joaolevi/payroll_v2/tree/main/src/Company/RegisterTools "RegisterTools")/"classes"

Dessa forma, a classe Finances necessitava de uma ferramenta que tivesse o registro dos dados financeiros dos empregados e funções que acessassem e devolvessem tais dados. A classe criada foi [EmployeesPayCheck](https://github.com/joaolevi/payroll_v2/blob/main/src/Company/RegisterTools/EmployeesPayCheck.py "EmployeesPayCheck")
Enquanto que a classe HumanResourcers precisava de uma classe para ter o registro de dados pessoais dos empregados e funções de acesso a tais dados.
A classe criada foi [EmployeesRegister](https://github.com/joaolevi/payroll_v2/blob/main/src/Company/RegisterTools/EmployeesRegister.py "EmployeesRegister")

Essas ferramentas só estavam acessíveis as classes responsáveis por elas, no caso:

Finances -> EmployeesPayCheck
HumanResourcers -> EmployeesRegister

Não era possível acessar através de outra classe: Finances -x> EmployeesRegister.

##### 2.3. Quantidade de IF's muito grande:
Como o python não contempla a função "switch", foi-se necessário criar funções que tivessem diversos casos de if-else para verificar as condições e elaborar as saídas.
Ainda assim, várias funções continham uma quantidade enorme de condicionais. Como exemplo: [change_employee_details](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/3b9b5a048c55638f2e6d31de55720098e3be649c/src/Company/Company.py#L97 "change_employee_details") e a função de interação com o usuário construída no arquivo [main.py](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/main.py "main.py") do código não refatorado.

###### 2.3 Solution:
Como a classe [Employee](https://github.com/joaolevi/payroll_v2/blob/main/src/Employees/Employee.py "Employee") do projeto refatorado teve seus atributos reduzidos, consequentemente a função para alteração dos dados do empregado foram também reduzidas. ([change_employees_details](https://github.com/joaolevi/payroll_v2/blob/9f256a0ab0b0f8d977a186511b7e2dd5b7f85846/src/Company/RegisterTools/EmployeesRegister.py#L58 "change_employees_details")).
Em relação as funções de intereção com o usuário, foi criado um [subpacote](https://github.com/joaolevi/payroll_v2/tree/main/src/UI/DepartamentsUI "subpacote") com a interação necessária para cada classe. Por tanto, um menu ([FinancesUI](https://github.com/joaolevi/payroll_v2/blob/main/src/UI/DepartamentsUI/FinancesUI.py "FinancesUI"), [HumanResourcersUI](https://github.com/joaolevi/payroll_v2/blob/main/src/UI/DepartamentsUI/HumanResourcersUI.py "HumanResourcersUI"), [AdministrationUI](https://github.com/joaolevi/payroll_v2/blob/main/src/UI/DepartamentsUI/AdministrationUI.py "AdministrationUI")) para cada setor foi desenvolvido.
Além disso, uma classe com as funções mais utilizadas nas interações foi criada ([aqui](https://github.com/joaolevi/payroll_v2/blob/main/src/UI/MenuOfChoices.py "aqui")) para evitar a repetição de código.

Para unir os menus dos departamentos em um único menu sem que houvesse uma grande quantidade de código, foi criada uma classe "[menu principal](https://github.com/joaolevi/payroll_v2/blob/main/src/UI/MainMenu.py "menu principal")" e usada uma técnica de "routes" para passar os dados de uma "screen" (está entre áspas pois a interação foi feita no console, então não é bem uma screen) para outra e assim poder transitar no menu e fazer as operações sem bugs ou perda de dados.

#### 3. Lazy Class:
Algumas classes foram criadas no projeto 1 com o intuito de serem utilizadas como ferramentas e terminaram não sendo utilizadas ou se usadas, foram usadas poucas vezes.
Exemplo: [Tax class](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/Tax/Tax.py "Tax class") e [SindTax class](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/Tax/SindTax.py "SindTax class").

##### 3. Solution:
As classes citadas faziam parte de um sub pacote "Taxas". Como a implementação era muito pouca elas foram removidas.

#### 4 .Shotgun Surgery:
Como a classe [Employee](https://github.com/joaolevi/Projeto_de_software_2020.1/blob/main/src/Employees/Employee.py "Employee") continha vários atributos, qualquer modificação feita na classe ou em alguma função que a utilizasse exigia uma série de modificações. 

##### 4. Solution:
Como a classe Employee foi reduzida, mudanças na classe passaram a exigir menos modificações ou quase nenhuma nas demais classes e funções que a utilizavam.

#### 5. Data Class:
Classes com muitos atributos como a Employee, ou classes que continham apenas métodos getters e setters e não tinham outra função além disso.

##### 5. Solution:
A classe Employee foi reduzida ([aqui](https://github.com/joaolevi/payroll_v2/blob/main/src/Employees/Employee.py "aqui")). Apesar de conter praticamente os métodos get e set, ela foi necessária para a configuração da função [__repr__](https://github.com/joaolevi/payroll_v2/blob/bf688a4e41f6cc3f8aac60ec4d8f4cbf7966cc36/src/Employees/Employee.py#L25 "__repr__") que printa os dados no console, evitando que tivesse que se criar uma nova função nas outras classes de tipos de empregados ou em qualquer outra classe ou função que printasse esses dados na tela, assim como, qualquer modificação necessária na impressão dos dados era feita diretamente na classe Employee sem a necessidade de ser feita nas outras classes. As classes apenas com métodos getters e setters como as do subpacote [Tax](https://github.com/joaolevi/Projeto_de_software_2020.1/tree/main/src/Tax "Tax") foram removidas.
