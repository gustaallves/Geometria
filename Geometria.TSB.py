from My_library.some_module import Ponto, Reta, Triangulo, Quadrilatero

def workspace():
    my_cord = Ponto(2, 2)
    print(f'\n{my_cord.point()}')
    
    my_cords = Reta(-4, 6, 0, 6)
    print(f'\n{my_cords.cord_reta()}')    
    my_cords.dist_reta()    
    
    my_Tcords = Triangulo(8, 0, 4, 2, 6, 6)
    print(f'\n{my_Tcords.cord_triangulo()}')    
    my_Tcords.dist_reta()
    
    my_Qcords = Quadrilatero(4, 0, 2, 4, -4, -2, 0, -6)
    print(f'\n{my_Qcords.cord_quadrilatero()}')
    my_Qcords.dist_retas()
    
    print("\nSuccessful exit.")
    
    
    
if __name__ == "__main__":
    
    workspace()

