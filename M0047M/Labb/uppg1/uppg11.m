%% Uppgift 11
% Plotta funktionen och hitta konstanta värdet i intervallet $[-a, -1]$ där $a >
% 0$ är tillräckligt stort
%
% $$ f(x) = tan^{-1}(\frac{x - 1}{x + 1}) - tan^{-1}(x) $$
x = linspace(-100000, -1, 100000);
f = @(x) atan((x - 1) ./ (x + 1)) - atan(x);

figure;
plot(x, f(x));
xlabel('x');
ylabel('y');
grid on;
%%
% Funktionen verkar ge sådant konstant värde
%
% $$ f(x) \approx 2,356 \approx \frac{3\pi}{4} $$
%
% Det kan bekräftas genom att räkna ut gränsvärdet
%
% $$ \lim_{x \to -\infty} f(x) = \lim_{x \to -\infty} \left( \tan^{-1}(\frac{x 
% - 1}{x + 1}) - \tan^{-1}(x) \right) $$
%
% vi räknar var för sig
%
% $$ \lim_{x \to -\infty} \tan^{-1}(\frac{x - 1}{x + 1}) =
% \lim_{x \to -\infty} \tan^{-1}(1 - \frac{2}{x + 1}) = \tan^{-1}(1) $$
%
% och
%
% $$ \lim_{x \to -\infty} \tan^{-1}(x) = -\frac{\pi}{2} $$
%
% slutligen
%
% $$ \lim_{x \to -\infty} f(x) = \tan^{-1}(1) - (-\frac{\pi}{2}) = \frac{3\pi}{4} 
% $$
% 
% Alltså är det konstanta värdet $\frac{3\pi}{4}$.
