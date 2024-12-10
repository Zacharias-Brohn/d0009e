# Set up the variables
lambda_betong = 1.7  # W/(m·K)
lambda_mineralull = 0.055  # W/(m·K)
d_betong = 0.386  # m
d_mineralull = 0.143  # m
A = 30.9  # m²
T_ute = 10.13  # °C
T_inne = 20.68  # °C

# Heat flow must be equal through both layers
# q = -λ₁A(T₂-T₁)/d₁ = -λ₂A(T₃-T₂)/d₂

# Solve for T₂
T2 = (T_ute * lambda_betong * d_mineralull + T_inne * lambda_mineralull * d_betong) / (lambda_betong * d_mineralull + lambda_mineralull * d_betong)

print(f"Temperature at interface: {T2:.2f}°C")