function y = calcul_gains2()



% Valeurs de qd2 � modifier
%val_qd2 = -pi/2;

% Calcul des constantes
g = 9.81;
l1 = 1.15;
l2 = 2.25;
lc1 = l1/2;
lc2 = l2/2;
m1 = 0.4;
m2 = 0.9;
I1 = 1/12 * m1 * l1^2;
I2 = 1/12 * m2 * l2^2;

% On d�clare les gains et les variables d'angles comme �tants des symboles de
% variables r�elles
syms q1 q2 qd1 qd2 dotq1 dotq2 ddotq1 ddotq2 kdd kd kp real

% Calcul des variables de position et de leurs premi�res d�riv�es par rapport au
% temps
x1 = lc1*cos(q1);
x2 = l1*cos(q1) + lc2*cos(q1 + q2);
dotx1 = -dotq1*lc1*sin(q1);
dotx2 = -dotq1*l1*sin(q1) - (dotq1 + dotq2)*lc2*sin(q1 + q2);
% Constantes
c = m1 + m2;
c1 = m1 * lc1^2 + m2 * l1^2 + I1;
c2 = m2 * lc2^2 + I2;
c3 = m2 * l1 * lc2;
c4 = m1 * lc1 + m2 * l1;
c5 = m2 * lc2;

% Calcul du moment angulaire et de ses 2 premi�res d�riv�es par rapport au
% temps
L = (c1 + c2 + 2*c3*cos(q2))*dotq1 + (c2 + c3*cos(q2))*dotq2; 
dotL = - g * ( m1*x1 + m2*x2 );
ddotL = - g * ( m1*dotx1 + m2*dotx2 );

% Valeurs du couple pour la configuration but
taud = m2*lc2*g*cos(qd1 + qd2);

% Formule de la loi de contr�le
tau = kdd*ddotL + kd*dotL  + kp*L + taud;

% Variables li�es au �quations du mouvement
d11 = m1*lc1^2 + m2*(l1^2 + lc2^2 + 2*l1*lc2*cos(q2)) + I1 + I2;
d22 = m2*lc2^2 + I2;
d12 = m2*(lc2^2 + l1*lc2*cos(q2)) + I2;
d21 = m2*(lc2^2 + l1*lc2*cos(q2)) + I2;

h1 = -m2*l1*lc2*sin(q2)*dotq2^2 - 2*m2*l1*lc2*sin(q2)*dotq2*dotq1;
h2 = m2*l1*lc2*sin(q2)*dotq1^2;
phi1 = (m1*lc1+m2*l1)*g*cos(q1)+m2*lc2*g*cos(q1+q2);
phi2 = m2*lc2*g*cos(q1+q2);

% Calcul de la fonction h

M = [[0 0 d11 d12]
    [0 0 d21 d22]
    [1 0 0 0]
    [0 1 0 0]];
N = [-h1-phi1 tau-h2-phi2 dotq1 dotq2]';
hx = M\N;

% Calcul de A
A = zeros(4);
A = sym(A);

x = [q1 q2 dotq1 dotq2];

for i = 1:4
    for j = 1:4
        A(i,j) = diff(hx(i), x(j));
    end
end

% On remplace par les valeurs de l'�tat but
A = subs( A, [q1 q2 dotq1 dotq2], [qd1 qd2 0 0] );

% R�cup�re une valeur pour qd2 qui est dans un fichier
% Servira quant on pourra tout lancer � partir de python
fid = fopen('Data/vals_qd.txt','r');
formatSpec = '%s';
str = fscanf(fid,formatSpec);
val = strsplit(str, 'qd2=');
val_qd2 = degtorad(str2double(val(2)));


% Calcul de qd1, de sorte que qd1 et qd2 forment une position d'�quilibre
f = c4*cos(qd1)+c5*cos(qd1+qd2);
f = subs(f, qd2, val_qd2);
val_qd1 = solve(f==0, qd1, 'Real', true);
if val_qd1(1) >= 0
    val_qd1 = val_qd1(1);
else 
    val_qd1 = val_qd1(2);
end

A = subs(A, [qd1 qd2], [val_qd1 val_qd2]);
A = vpa(A);

% Calcul du polyn�me caract�ristique
syms x
polynome = charpoly(A);
y = struct('qd1', radtodeg(vpa(val_qd1)));
%y = radtodeg(vpa(val_qd1));
end