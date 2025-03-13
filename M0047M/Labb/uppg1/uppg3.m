%% Uppgift 3
% Beräkna $a_k$ tills den verkar konvergera, samt gränsvärde.
%
% $$ a_k = ( \frac{k - 3}{k} )^k $$
%
% Jag bestämde mig för att skriva ett skript som beräknar $a_k$ mellan $[1,
    % 100].$
% 
k_values = 1:100;
a = zeros(size(k_values));

for i = 1:length(k_values)
    k = k_values(i);
    a(i) = exp(k * log((k - 3) / k));
end

figure;
plot(k_values, a, 'bo', 'MarkerSize', 4);
hold on;
xlabel('k');
ylabel('a_k');
grid on;
axis([0 100, 0 0.05]);
hold off;
%%
% Vi ser att $a_k$ konvergerar runt $a_n \approx 0.047$.
%
% Detta går att bevisa algebraiskt
%
% $$ \frac{k - 3}{k} = 1 - \frac{3}{k} $$
%
% Så vi söker alltså
%
% $$ \lim_{k \to \infty} (1 - \frac{3}{k})^k $$
%
% Nu ser den bekant ut, eftersom
%
% $$ e = \lim_{n \to \infty} (1 + \frac{1}{n})^n $$
%
% så vi kan skriva om vår ekvation som
%
% $$ \lim_{k \to \infty} (1 - \frac{3}{k})^k = \lim_{k \to \infty} (1 +
% \frac{(-3)}{k})^k = e^{-3} $$
% 
% och
%
% $$ e^{-3} \approx 0.0498. $$
