%% Uppgift 14
% Vi har $x + (10 - x) = 10$. Om vi använder det tillsammans med förklaringen av
% problemet kan vi skriva funktionen som
%
% $$ f(x) = x^3 + (10 - x)^2 $$
% 
% Först plottar vi funktionen för att se ungefär var minimumvärdet ligger
x = linspace(0, 10, 1000);
f = @(x) x.^3 + (10 - x).^2;
plot(x, f(x));
xlabel('x');
ylabel('f(x)');
grid on;
%%
% Då ser det ut som att minimumvärdet ligger mellan $2 < x < 3$.
%
% Nu kan vi skriva kod för att räkna ut minimumvärdet samt summan

[x_min, f_min] = fminbnd(f, 0, 10);
disp(['Minimum value occurs at x = ', num2str(x_min)]);
disp(['Minimum value of f(x) = ', num2str(f_min)]);
%%
% Alltså får vi svaret att
%
% $$ x_{crit} \approx 2,2701 $$
%
% vilket ger
%
% $$ f(2,2701) \approx 71,45. $$
