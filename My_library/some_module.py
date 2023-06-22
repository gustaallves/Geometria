import matplotlib.pyplot as plt

    
class Ponto():
    """Coordenadas do Ponto"""
    def __init__(self, cordX, cordY):
        
        self.cordX = cordX
        self.cordY = cordY
        
    def point(self):
        """Devolve as coordenadas do Ponto"""
        cord= 'As coordenadas do ponto são: ' '(' +str(self.cordX) + ',' + str(self.cordY) + ')'
        return cord.title() 
        
class Reta():
    """Coordenadas de uma Reta"""
    def __init__(self, x1, y1, x2, y2):     
        
        self.pontoA = Ponto(x1, y1)
        self.pontoB = Ponto(x2, y2)
        
        """Parâmetros para inserir a Reta no Gráfico""" 
        x= [self.pontoA.cordX, self.pontoB.cordX]
        y= [self.pontoA.cordY, self.pontoB.cordY]
        
        ax = plt.axes()
        plt.scatter(x, y, color = 'red')
        plt.plot(x, y, label = 'Reta')
        plt.plot([-5,10], [0,0], color='black')
        plt.plot([0,0], [-8,8], color='black')
        
        """Anotações e orientação"""
        plt.legend(loc = (0.1, 0.3))
        plt.xlabel('eixo X')
        plt.ylabel('eixo Y')
        plt.title('Plano Cartesiano') 
        
        ax.grid(True)
    
    def cord_reta(self):
        """Devolve as coordenadas da Reta"""
        cord_reta= 'As coordenadas da Reta sâo: ' '(' +  str(self.pontoA.cordX) + ',' + str(self.pontoB.cordX) + ')' + ' e ' + '(' + str(self.pontoA.cordY) + ',' + str(self.pontoB.cordY) + ')'
        return cord_reta.title()
    
    def dist_reta(self):
        """Calcula a distância entre dois pontos para ser a reta"""
        
        distancia= ((self.pontoB.cordX - self.pontoA.cordX)**2 + (self.pontoB.cordY - self.pontoA.cordY)**2)**0.5
        print(f"Reta = {distancia:.2f}")       
            
class Triangulo():
    """Coordenadas de um Triângulo"""
    def __init__(self,  Tx1, Ty1, Tx2, Ty2, Tx3, Ty3):
        
        self.TpontoA = Ponto(Tx1, Ty1)
        self.TpontoB = Ponto(Tx2, Ty2)
        self.TpontoC = Ponto(Tx3, Ty3)
        
        x= [self.TpontoA.cordX, self.TpontoB.cordX, self.TpontoC.cordX, self.TpontoA.cordX, self.TpontoC.cordX]
        y= [self.TpontoA.cordY, self.TpontoB.cordY, self.TpontoC.cordY, self.TpontoA.cordY, self.TpontoC.cordY]
       
        plt.scatter(x, y, color = 'red')
        plt.plot(x, y, label = 'Triângulo')        
        plt.legend(loc = (0.1, 0.3))
                
    def cord_triangulo(self):
        """Devolve as coordenadas do Triângulo"""
        cord_triangulo= 'As coordenadas do Triângulo são:  A=' '(' +  str(self.TpontoA.cordX) + ',' + str(self.TpontoA.cordY) + ')' + '; B=' + '(' + str(self.TpontoB.cordX) + ',' + str(self.TpontoB.cordY) + ')' ' e C=' + '(' + str(self.TpontoC.cordX) + ',' + str(self.TpontoC.cordY) + ')'
        return cord_triangulo.title()
        
    def dist_reta(self):
        """Calcula a distância da reta A = (x1,y1) e (x2,y2)"""        
        distanciaA = ((self.TpontoB.cordX - self.TpontoA.cordX)**2 + (self.TpontoB.cordY - self.TpontoA.cordY)**2)**0.5
        print(f"Reta A = {distanciaA:.2f}")
    
        """Calcula a distância da reta B = (x2,y2) e (x3,y3)"""        
        distanciaB = ((self.TpontoC.cordX - self.TpontoB.cordX)**2 + (self.TpontoC.cordY - self.TpontoB.cordY)**2)**0.5
        print(f"Reta B = {distanciaB:.2f}")
    
        """Calcula a distância da retat C = (x3,y3) e (x1,y1)"""        
        distanciaC = ((self.TpontoC.cordX - self.TpontoA.cordX)**2 + (self.TpontoC.cordY - self.TpontoA.cordY)**2)**0.5
        print(f"Reta C = {distanciaC:.2f}")
        
        """Soma reta A, B e C"""        
        perimetro = distanciaA + distanciaB + distanciaC
        print(f"Perímetro = {perimetro:.2f}")
        
        """Calcular a área do Triângulo com a fórmula de Heron"""
        semi_perimetro= perimetro/2
        area = (semi_perimetro * (semi_perimetro - distanciaA) * (semi_perimetro - distanciaB) * (semi_perimetro - distanciaC))**0.5
        print(f"Area = {area:.2f}")
        
class Quadrilatero():
    """Coordenadas de um Quadrilátero"""
    def __init__(self, Qx1, Qy1, Qx2, Qy2, Qx3, Qy3, Qx4, Qy4):
            
        self.QpontoA = Ponto(Qx1, Qy1)
        self.QpontoB = Ponto(Qx2, Qy2)
        self.QpontoC = Ponto(Qx3, Qy3)
        self.QpontoD = Ponto(Qx4, Qy4)
        
        x= [self.QpontoA.cordX, self.QpontoB.cordX, self.QpontoC.cordX, self.QpontoD.cordX, self.QpontoA.cordX, self.QpontoD.cordX]
        y= [self.QpontoA.cordY, self.QpontoB.cordY, self.QpontoC.cordY, self.QpontoD.cordY, self.QpontoA.cordY, self.QpontoD.cordY]
        
        plt.plot(x, y, label = 'Quadrilátero')
        plt.scatter(x, y, color = 'red')
        
        plt.legend(loc = (0.6, 0.1))
        
    def cord_quadrilatero(self):
        """Devolve as coordenadas do Quadrilátero"""
        cord_quadrilatero= 'As coordenadas do Quadrilátero são:  A=' '(' +  str(self.QpontoA.cordX) + ',' + str(self.QpontoA.cordY) + ')' + '; B=' + '(' + str(self.QpontoB.cordX) + ',' + str(self.QpontoB.cordY) + ')' ';  C=' + '(' + str(self.QpontoC.cordX) + ',' + str(self.QpontoC.cordY) + ')' ' E ' + 'D=(' + str(self.QpontoD.cordX) + ',' + str(self.QpontoD.cordY) + ')'
        return cord_quadrilatero.title()
        
    def dist_retas(self):
        """Calcula a distância da reta A = (x1,y1) e (x2,y2)"""        
        distanciaA = ((self.QpontoB.cordX - self.QpontoA.cordX)**2 + (self.QpontoB.cordY - self.QpontoA.cordY)**2)**0.5
        print(f"Reta A = {distanciaA:.2f}")
    
        """Calcula a distância da reta B = (x2,y2) e (x3,y3)"""        
        distanciaB = ((self.QpontoC.cordX - self.QpontoB.cordX)**2 + (self.QpontoC.cordY - self.QpontoB.cordY)**2)**0.5
        print(f"Reta B = {distanciaB:.2f}")
    
        """Calcula a distância da retat C = (x3,y3) e (x4,y4)"""        
        distanciaC = ((self.QpontoD.cordX - self.QpontoC.cordX)**2 + (self.QpontoD.cordY - self.QpontoC.cordY)**2)**0.5
        print(f"Reta C = {distanciaC:.2f}")
        
        """Calcula a distância da retat C = (x4,y4) e (x1,y1)"""        
        distanciaD = ((self.QpontoA.cordX - self.QpontoD.cordX)**2 + (self.QpontoA.cordY - self.QpontoD.cordY)**2)**0.5
        print(f"Reta D = {distanciaD:.2f}")
        
        """Soma reta A, B, C e D"""        
        perimetro = distanciaA + distanciaB + distanciaC + distanciaD
        print(f"Perímetro = {perimetro:.2f}")
            
            
        
        

