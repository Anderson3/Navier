# Navier
Software de cálculo de peças de concreto armado, baseado na NBR 6118/14. Desenvolvido com Python 3.7 + PyQt5.

## Pequena Descrição
O Navier é um programa desenvolvido em Python com finalidade de produzir dados de dimensionamento de peças de Concreto Armado. Essa aplicação com finalidade para Desktops permite calcular Vigas, Pilares, Lajes e Sapatas analisando as peças de manaira isolada. Cada elemento estrutural é tratado no programa como um módulo de cálculo interno. O Navier se baseia nas condições normativas brasileiras de Concreto Armado, principalmente respaldadas através da ABNT NBR 6118/14. 

## Funcionalidades
O Navier permite cálcular como elementos:
<ul>
  <li>Vigas
    <ul>
      <li>Cálculo de armaduras longitudinais em vigas com seção retangular, para situações com armadura simples e dupla. Cálculo de armaduras transversais, para ambos os modelos de cálculo dispostos na NBR 6118/14.</li>
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
