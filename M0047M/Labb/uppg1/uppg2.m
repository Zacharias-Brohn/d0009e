%% Uppgift 2
% Vilken linje/punkt är symmetrisk i funktionen
%
% $$ f(x) = \frac{2x^2 + 3x}{x^2 + 4x + 5} $$
x = linspace(-30, 30, 5000);
y = (2 * x.^2 + 3 * x) ./ (x.^2 + 4 * x + 5);

figure;
plot(x, y);
xlabel('x');
ylabel('y');
grid on
axis equal
%%
% då ser vi att symmetrin ligger här, vid
%
% $$ x = -2 $$
%
% $$ y = 2 $$
figure;
plot(x, y);
hold on
x_hl = -2;
y_hl = 2;
plot(x_hl, y_hl, 'ro', 'MarkerSize', 3, 'MarkerFaceColor', 'r');
grid on
axis([-6 2, -2 6]);
hold off
%%
% Symmetri kan bevisas för $(h,k)$ genom
%
% $$ f(2h - x) = 2k - f(x) $$
%
% så för våran funktion blir det
%
% $$ f(-4-x) = \frac{2(-4 - x)^2 + 3(-4 - x)}{(-4 - x)^2 + 4(-4 - x) + 5}
% $$
%
% utveckla täljaren
%
% $$ (-4 - x)^2 = 16 + 8x + x^2 $$
%
% $$ 2(16 + 8x + x^2) = 32 + 16x + 2x^2 $$
%
% $$ 3(-4 - x) = -12 - 3x $$
%
% $$ 32 + 16x + 2x^2 - 12 - 3x = 2x^2 + 13x + 20 $$
%
% sedan nämnaren
%
% $$ (16 + 8x + x^2) + (-16 - 4x) + 5 = x^2 + 4x + 5 $$
%
% då får vi tillslut att
%
% $$ f(-4 - x) = \frac{2x^2 + 13x + 20}{x^2 + 4x + 5} $$
%
% och nu för $4 - f(x)$
%
% $$ 4 - f(x) = 4 - \frac{2x^2 + 3x}{x^2 + 4x + 5} $$
%
% flyttar 4 in i bråket
%
% $$ \frac{4(x^2 + 4x + 5) - 2x^2 - 3x}{x^2 + 4x + 5} $$
%
% utvecklar täljaren
%
% $$ 4x^2 + 16x + 20 - 2x^2 - 3x = 2x^2 + 13x + 20 $$
%
% då får vi att
%
% $$ 4 - f(x) = \frac{2x^2 + 13x + 20}{x^2 + 4x + 5} $$
%
% vilket är samma som $f(-4 - x)$, vilket betyder att punkten är
% symmetrisk.
