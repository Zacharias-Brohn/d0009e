%% Uppgift 5
% Beräkna
%
% $$ \lim_{x \to 0} \frac{\sin(2 \pi x)}{\sin(3 \pi x)} $$
%
% Eftersom vi ska beräkna gränsvärdet för $x \to 0$ så sätter jag små x-värden
x = linspace(-0.1, 0.1, 1000);
y = sin(2 * pi * x) ./ sin(3 * pi * x);
figure;
plot(x, y);
xlabel('x');
ylabel('y');
grid on;
axis([-0.1 0.1, -0.2 1]);
%%
% Om vi nu tittar närmare runt $x = 0$ så kan vi hitta gränsvärdet
figure;
plot(x, y, "Marker", "o", "MarkerSize", 3);
xlabel('x');
ylabel('y');
grid on;
axis([-0.005 0.005, 0.665 0.668]);
%%
% Vi ser här att
%
% $$ \lim_{x \to 0} \frac{\sin(2 \pi x)}{\sin(3 \pi x)} \approx 0.67
% \approx \frac{2}{3}. $$

