from calcs import call_triangle, call_circle, call_square, call_cylinder

#bem vindo
def call_welcome ():
    print (" SEJA BEM VINDOS (AS)")
#MENU completo
def call_cod_menu ():
    menu_initial = True #menu inicial
    while menu_initial == True:
        print (""" \n Escolha a opção desejada através do menu abaixo: \n MENU
            1 - Calcular a Área do Triangulo 
            2 - Calcular a Área do Circulo
            3 - Calcular a Área do Retangulo
            4 - Calcular o Volume do Cilindro
            5 - Sair
            """)
        option_desired = int(input("Indique a opção desejada: ")) #opção desejada
        value_of_pi = 3.14

        match option_desired: #opções, variaveis e respectivos calculos
            case 1: #triangulo
                call_triangle ()
                menu_initial = call_return_menu ()
            case 2: #circulo
                call_circle (value_of_pi)
                menu_initial = call_return_menu ()
            case 3: #retangulo
                call_square ()
                menu_initial = call_return_menu ()
            case 4: #cilindro
                call_cylinder (value_of_pi)
                menu_initial = call_return_menu ()
            case 5:
                print ("Obrigada por utilizar o programa.")
                menu_initial = False
            case _ :
                print("Opção não encontrada. Tente de novo.")
#voltar ao menu
def call_return_menu ():
    return_menu = input("\nDeseja retornar ao Menu? (SIM|NAO): ").upper() #retorna o menu
    if return_menu == 'NAO':
        print ("Obrigada por utilizar o programa.")
        return False
    else :
        return True
