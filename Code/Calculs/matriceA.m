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

c = m1 + m2;
c1 = m1 * lc1^2 + m2 * l1^2 + I1;
c2 = m2 * lc2^2 + I2;
c3 = m2 * l1 * lc2;
c4 = m1 * lc1 + m2 * l1;
c5 = m2 * lc2;


syms qd1 qd2 kdd kd kp real

a = c1 * c2 - (c3 * cos(qd2))^2;
gamma1 = c1 + c2 + 2 * c3 * cos(qd2);
gamma2 = - g * (c4 * sin (qd1) + c5 * sin (qd1 + qd2));


ddotq1_q1 = (gamma2/a) * (kd * (c2 + c3 * cos(qd2)) - c2);
ddotq1_q2 = (1 / a) * (- kd * g * (c2 + c3 * cos(qd2)) * c5 * sin(qd1 + qd2));
ddotq1_dotq1 = (1 / a) * (kdd * gamma2 - kp * gamma1) * (c2 + c3 * cos(qd2));
ddotq1_dotq2 = -(1 / a) * (kp * (c2 + c3 * cos(qd2))^2 + kdd * g * (c2 + c3 * cos(qd2)) * c5 * sin(qd1 + qd2));

ddotq2_q1 = (gamma2 / a) * (c2 + c3 * cos(qd2) - kd * gamma1);
ddotq2_q2 = (1 / a) * ( (kd * g * c5 * sin(qd1 + qd2)) * gamma1 - (c2 + c3 * cos(qd2)) * c5 * g * sin(qd1 + qd2));
ddotq2_dotq1 = (gamma1 / a) * (kp * gamma1 - kdd * gamma2);
ddotq2_dotq2 = (gamma1 / a) * (kp * (c2 + c3 * cos(qd2)) + kdd * g * c5 * sin(qd1+ qd2));

A = [[0 0 1 0]
    [0 0 0 1]
    [ddotq1_q1 ddotq1_q2 ddotq1_dotq1 ddotq1_dotq2]
    [ddotq2_q1 ddotq2_q2 ddotq2_dotq1 ddotq2_dotq2]];


A = subs(A, [qd1 qd2], [90 0]);
A = vpa(A);
% Est ce qu'on a le droit de garder uniquemment la partie réelle???
A = real(A);
%lambda = eig(A);

% Calcul du polynôme caractéristique

syms x
p = charpoly(A);
p(5);

%lam = solve(p==0, x);
%lam = vpa(lam)
