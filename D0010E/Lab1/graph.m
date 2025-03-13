data = load('raise.txt');
function count = recRaiseHalfCount(k)
    if k == 0
        count = 1;
    else
        count = 2^(floor(log2(k)) + 2) - 1;
    end
end
% Extract the columns
k = data(:, 1);
Nhalf = data(:, 2);
None = data(:, 3);
test = arrayfun(@recRaiseHalfCount, k);
% Plot Nhalf(k)
figure;
plot(k, Nhalf, 'b', 'DisplayName', 'Nhalf(k)');
xlabel('k');
ylabel('Number of Recursive Calls');
title('Nhalf(k) vs k');
legend;
grid on;

% Plot Nhalf(k)
figure;
plot(k, test, 'b', 'DisplayName', 'test(k)');
xlabel('k');
ylabel('Number of Recursive Calls');
title('Nhalf(k) vs k');
legend;
grid on;

% Plot None(k)
figure;
plot(k, None, 'r', 'DisplayName', 'None(k)');
xlabel('k');
ylabel('Number of Recursive Calls');
title('None(k) vs k');
legend;
grid on;
