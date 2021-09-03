%RETO
%Indicaciones iniciales 
clear; close all; clc; 

%Datos 
m = 0.4; 
N = 14; %Número de imanes 
p = 1.72e-8; %Resistividad del cobre 
B = 0.2; %Campo magnético en T
V = 0.014*0.025*0.007; 
h1 = 2; %Altura del cilindro transparente
h2 = 0.3;  %Altura del cilindro de cobre 
v0 = 0; %Velocidad inicial de la góndola (reposo) 
y0 = h1 + h2; %Posición inicial de la góndola
g = 9.81; %Aceleración debida a la gravedad

%Determinación de datos para caída libre

%vf2 =2*g*(y0-h2); %Obtener magnitud de velocidad final (velocidad en 0.3m)
t1 = sqrt((2*(h2-y0))/-g); %Obtener tiempo en el que llega a 0.3m
vf = -g*t1; 

%Función anónima caída libre 
F1 = @(t,v) [v(2), -g]; 
[tsol, vsol] = rungeKuntam(F1, 0, [y0, v0], t1, 100);
%disp(vsol);

F2 = @(t,v) [v(2), -(N*V*B^2*v(2))/(p*m) - g]; 
[tsol1, vsol1] = eulerEDONm(F2, t1+1e-30, [h2, vf], 1.3, 100);
disp(vsol1);
%tt = [tsol;tsol1];
%disp(tsol);
%disp(vsol1(1, :));
%Gráfica de posición en función del tiempo
figure
plot([tsol tsol1],[vsol(:,1);vsol1(:,1)]); 
%plot(tsol1,  vsol1(:,1)); %Grafica posición
%Grafica posición
hold on 
title('Posición vs Tiempo'); 
xlabel('Tiempo en s'); 
ylabel('Posición en m');  
hold off


figure
plot([tsol tsol1],[vsol(:,2);vsol1(:,2)]);  %Grafica velocidad
title('Velocidad vs Tiempo');
xlabel('Tiempo en s'); 
ylabel('Velocidad en m/s');  
hold off