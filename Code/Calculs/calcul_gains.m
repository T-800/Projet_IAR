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

% Calcul du moment angulaire et de ses 2 premi�res d�riv�es par rapport au
% temps
L = (m1*lc1^2j + m2*l1^2 + I1 + m2*lc2^2 + I2 + 2*m2*l1*lc2*cos(q2))*dotq1 + (m2*lc2^2 + I2 + m2*l1*lc2*cos(q2))*dotq2; 
dotL = -g * ( m1*x1 + m2*x2 );
ddotL = -g * ( m1*dotx1 + m2*dotx2 );

% A v�rifier si ce ne sont pas des qd
taud = m2*lc2*g*cos(q1 + q2);

% Formule de la loi de contr�le
tau = kdd*ddotL + kd*dotL  + kp*L + taud;

% Variables li�es au �quations du mouvement
d11 = m1*lc1^2 + m2*(l1^2 + lc2^2 + 2*l1*lc2*cos(q2)) + I1 + I2;
d22 = m2*lc2^2 + I2;
d12 = m2*(lc2^2 + l1*lc2*cos(q2)) + I2;
d21 = m2*(lc2^2+l1*lc2*cos(q2)) + I2;

h1 = -m2*l1*lc2*sin(q2)*dotq2^2 - 2*m2*l1*lc2*sin(q2)*dotq2*dotq1;
h2 = m2*l1*lc2*sin(q2)*dotq1^2;
phi1 = (m1*lc1+m2*l1)*g*cos(q1)+m2*lc2*g*cos(q1+q2);
phi2 = m2*lc2*g*cos(q1+q2);


% Calcul de la fonction h
M = zeros(4);
M = sym(M);
M(3,1) = 1;
M(4,2) = 1;
M(1,3) = d11;
M(1,4) = d12;
M(2,3) = d21;
M(2,4) = d22;

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

A = subs( A, [q1 q2 dotq1 dotq2], [90 0 0 0] );
%A = vpa(A);

%eig(A)

% Calcul du polyn�me caract�ristique
p = charpoly(A);
[lam1, lam2, lam3, lam4] = solve(p==0, x);
