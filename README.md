# Navier
Software de cálculo de peças de concreto armado, baseado na NBR 6118/14. Desenvolvido com Python 3.7 + PyQt5.
![image](https://user-images.githubusercontent.com/17939997/70842933-d2987580-1e08-11ea-824c-51b98e1c73d8.png)

## Pequena Descrição
O Navier é um programa desenvolvido em Python com finalidade de produzir dados de dimensionamento de peças de Concreto Armado. Essa aplicação com finalidade para Desktops permite calcular Vigas, Pilares, Lajes e Sapatas analisando as peças de manaira isolada. Cada elemento estrutural é tratado no programa como um módulo de cálculo interno. O Navier se baseia nas condições normativas brasileiras de Concreto Armado, principalmente respaldadas através da ABNT NBR 6118/14. 

![image](https://user-images.githubusercontent.com/17939997/70842953-1e4b1f00-1e09-11ea-8194-6169fc5c0a14.png)
## Funcionalidades
O Navier permite cálcular como elementos:
<ul>
  <li>Vigas
    <ul>
      <li>Cálculo de armaduras longitudinais em vigas com seção retangular, para situações com armadura simples e dupla. Cálculo de armaduras transversais, para ambos os modelos de cálculo dispostos na NBR 6118/14.</li>
      </li>
    </ul>
  </li>
  <li>Pilares
    <ul>
      <li>Cálculo de pilares intermediários, de extremidade e de canto. Geração de Envoltória de momentos para seção retangular e dimensionamento de área de aço com auxílio de ábacos específicos para flexão.</li>
    </ul>
  </li>
  <li>Lajes
   <ul>
      <li>Cálculo de lajes bidirecionais (tipo cruz) e unidirecionais, definição de coeficientes de cálculo através do Método de Marcus e momentos centrais e de bordas. Definição de armaduras para os tipos de lajes e cálculos de áreas de aço.</li>
    </ul>
  </li>
  <li>Sapatas
   <ul>
      <li>Cálculo de sapatas de concreto armado isoladas e do tipo excêntricas. O Navier apresenta funções para geração de dimensões automáticas que garantem margem econômica e também permite calcular sapatas a partir de dimensões pré-definidas.</li>
    </ul>
  </li>
</ul>

## Imagens
![image](https://user-images.githubusercontent.com/17939997/70843053-9534e780-1e0a-11ea-8eb4-6caa118e6193.png)
![image](https://user-images.githubusercontent.com/17939997/70843057-abdb3e80-1e0a-11ea-8ce6-886ad7d0dc9d.png)
![image](https://user-images.githubusercontent.com/17939997/70843063-c2819580-1e0a-11ea-8450-c92c5fbc874b.png)
![image](https://user-images.githubusercontent.com/17939997/70843068-d62cfc00-1e0a-11ea-8cdf-ebe09f7e85a9.png)


## Nomenclatura
O nome Navier foi dado como homenagem ao engenheiro "Claude Louis Marie Henri Navier", que fora sorteado entre outros grande nomes da engenharia no mundo.
