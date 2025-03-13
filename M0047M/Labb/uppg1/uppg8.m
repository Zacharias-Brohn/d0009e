%% Uppgift 8
% Hitta kritiska punkter för funktionen
% $$ f(x) = x - sin(\frac{x}{x^2 + x + 1}) $$
x = linspace(-5, 5, 2000);
f = @(x) x - sin(x ./ (x.^2 + x + 1));

figure;
plot(x, f(x));
xlabel('x');
ylabel('y');
grid on;
axis([-1 0.6, -1 1]);
%%
% Här kan man se att det finns kritiska punkter runt $x = 0$ och $x \approx
% -0.518$.
% 
% För $x = 0$

figure;
plot(x, f(x));
hold on;
x1 = 0;
xlabel('x');
ylabel('y');
grid on;
plot(x1, f(x1), 'o', 'MarkerSize', 3);
axis([-0.1 0.1, -0.1 0.1]);
hold off;
%%
% För $x \approx -0.518$

figure;
plot(x, f(x));
hold on;
x2 = -0.518;
xlabel('x');
ylabel('y');
grid on;
plot(x2, f(x2), 'o', 'MarkerSize', 3);
axis([-0.6 -0.4, 0 0.20]);
hold off;
%%
% Alltså är svaret
%
% $$ x_{cp1} = 0 $$
%
% $$ x_{cp2} \approx -0.518 $$
