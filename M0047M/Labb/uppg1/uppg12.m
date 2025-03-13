%% Uppgift 12
% Hitta rötterna till funktionen
%
% $$ x^4 - 8x^2 - x + 16 = 0 $$
% 
% inom [1, 3] med Newton-Raphsons metod
format long;
f = @(x) x.^4 - 8 * x.^2 - x + 16;
f_prime = @(x) 4 * x.^3 - 16 * x - 1;
x0_1 = 1;
x_1 = x0_1;
x0_2 = 3;
x_2 = x0_2;
tol = 1e-10;
while abs(f(x_1)) > tol
    x_1 = x_1 - (f(x_1) ./ f_prime(x_1));
end

while abs(f(x_2)) > tol
    x_2 = x_2 - (f(x_2) ./ f_prime(x_2));
end

fprintf('x = %.10f\n', x_1);
fprintf('x = %.10f\n', x_2);
%%
% alltså är de två rötter i intervallet [1, 3]
%
% $$ x_1 \approx 1.6480953656 $$
%
% $$ x_2 \approx 2.3523926477 $$
