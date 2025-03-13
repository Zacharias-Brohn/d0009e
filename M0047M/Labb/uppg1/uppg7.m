%% Uppgift 7
% Undersök om det finns punkter med horisontell tangens eller saknar tangens
% till funktionen
%
% $$ y = ({x^2 - 1)^{1/3} $$
x = linspace(-5, 5, 1000);
y = @(x) nthroot((x.^2 - 1), 3);

figure;
plot(x, y(x));
xlabel('x');
ylabel('y');
grid on;
axis equal;
%%
% Här ser vi att om det kan finnas en horisontell tangens runt $x = 0$, vi kan
% dubbelkolla.
% 
% $$ y'(0) = \frac{2x}{3(x^2 - 1)^{2/3}} $$
%
% Om vi sätter in $x = 0$ så får vi att $y' = 0$.
%
% Vi ser också att det kan finnas vertikal tangens runt $x = 1$ och $x = -1$. Så
% om vi sätter in de x-värdena
%
% $$ y'(-1) = \frac{2 \cdot (-1)}{3((-1)^2 - 1)^{2/3}} = \frac{-2}{3(1 - 1)^{2/3}} =
% \frac{-2}{3(0)^{2/3}} = -\infty $$
%
% $$ y'(1) = \frac{2 \cdot 1}{3(1^2 - 1)^{2/3}} = \frac{2}{3(1 - 1)^{2/3}} =
% \frac{-2}{3(0)^{2/3}} = \infty $$
