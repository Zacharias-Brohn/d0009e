import math

# Constants
stefan_boltzmann = 5.6705e-8  # W/(m²·K⁴)
emissivity_al = 0.11        # Oxidized aluminum at 40°C
area = 0.204                # m²
time = 95.8                 # s
mass_n2 = 0.78          # kg
c_n2 = 1170                # J/(kg·K)

# Temperatures
T_container = 117.15  # K
T_boiling_n2 = 77.15 # K
T_initial = 76.15    # K

# Radiative heat transfer
Q_rad = emissivity_al * stefan_boltzmann * area * time * (T_container**4 - T_boiling_n2**4)

# Energy needed to heat N2 to boiling point
Q_heating = mass_n2 * c_n2 * (T_boiling_n2 - T_initial)

# Energy needed for vaporization
L_vap = 200  # J/kg
Q_available = Q_rad - Q_heating

# Mass of N2 vaporized
mass_vaporized = Q_available / L_vap

print(f"Mass of N2 vaporized: {mass_vaporized:.10f} g")