%% Uppgift 13
% Lös
%
% $$ \sin(x) = 1 - x $$
x = linspace(-5, 5, 1000);
f = @(x) sin(x) - 1 + x;
f1 = @(x) sin(x);
f2 = @(x) 1 - x;

figure;
plot(x, f1(x));
hold on;
plot(x, f2(x));
xlabel('x');
ylabel('y');
grid on;
hold off;
%%
% Grafen tyder på att det finns en rot runt $x = 0.5$. Vi använder gissningar 
% $x_1 = 0$ och $x_2 = 1$.
f_prime = @(x) cos(x) + 1;
x_1 = 0;
x_2 = 1;
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
% Därmed får vi svaret att roten ligger vid
%
% $$ x \approx 0.5109734294 $$
