# code auto-generated by the cuba-generate.py script.
import tables


class Data(tables.IsDescription):

    name = tables.StringCol(pos=0, itemsize=20)
    direction = tables.Float64Col(pos=1, shape=3)
    status = tables.Int32Col(pos=2)
    label = tables.Int32Col(pos=3)
    material_id = tables.Int32Col(pos=4)
    chemical_specie = tables.StringCol(pos=5, itemsize=20)
    material_type = tables.Int32Col(pos=6)
    shape_center = tables.Float64Col(pos=7, shape=3)
    shape_length_uc = tables.Float64Col(pos=8, shape=3)
    shape_length = tables.Float64Col(pos=9, shape=3)
    shape_radius = tables.Float64Col(pos=10, shape=3)
    shape_side = tables.Float64Col(pos=11, shape=3)
    crystal_storage = tables.StringCol(pos=12, itemsize=20)
    name_uc = tables.StringCol(pos=13, itemsize=20)
    lattice_vectors = tables.Float64Col(pos=14, shape=(3, 3))
    symmetry_lattice_vectors = tables.Int32Col(pos=15)
    occupancy = tables.Float64Col(pos=16)
    bond_label = tables.StringCol(pos=17, itemsize=20)
    bond_type = tables.Int32Col(pos=18)
    velocity = tables.Float64Col(pos=19, shape=3)
    acceleration = tables.Float64Col(pos=20, shape=3)
    number_of_points = tables.Int32Col(pos=21)
    radius = tables.Float64Col(pos=22)
    size = tables.Float64Col(pos=23)
    mass = tables.Float64Col(pos=24)
    volume = tables.Float64Col(pos=25)
    angular_velocity = tables.Float64Col(pos=26, shape=3)
    angular_acceleration = tables.Float64Col(pos=27, shape=3)
    simulation_domain_dimensions = tables.Float64Col(pos=28, shape=3)
    simulation_domain_origin = tables.Float64Col(pos=29, shape=3)
    dynamic_viscosity = tables.Float64Col(pos=30)
    kinematic_viscosity = tables.Float64Col(pos=31)
    diffusion_coefficient = tables.Float64Col(pos=32)
    probability_coefficient = tables.Float64Col(pos=33)
    friction_coefficient = tables.Float64Col(pos=34)
    scaling_coefficient = tables.Float64Col(pos=35)
    equation_of_state_coefficient = tables.Float64Col(pos=36)
    contanct_angle = tables.Float64Col(pos=37)
    amphiphilicity = tables.Float64Col(pos=38)
    phase_interaction_strength = tables.Float64Col(pos=39)
    hamaker_constant = tables.Float64Col(pos=40)
    zeta_potential = tables.Float64Col(pos=41)
    ion_valence_effect = tables.Float64Col(pos=42)
    debye_length = tables.Float64Col(pos=43)
    smoothing_length = tables.Float64Col(pos=44)
    lattice_spacing = tables.Float64Col(pos=45)
    time_step = tables.Float64Col(pos=46)
    number_of_time_steps = tables.Float64Col(pos=47)
    force = tables.Float64Col(pos=48, shape=3)
    torque = tables.Float64Col(pos=49, shape=3)
    density = tables.Float64Col(pos=50)
    concentration = tables.Float64Col(pos=51)
    pressure = tables.Float64Col(pos=52)
    temperature = tables.Float64Col(pos=53)
    distribution = tables.Float64Col(pos=54)
    order_parameter = tables.Float64Col(pos=55)
    original_position = tables.Float64Col(pos=56, shape=3)
    delta_displacement = tables.Float64Col(pos=57, shape=3)
    external_applied_force = tables.Float64Col(pos=58, shape=3)
    euler_angles = tables.Float64Col(pos=59, shape=3)
    sphericity = tables.Float64Col(pos=60)
    young_modulus = tables.Float64Col(pos=61)
    poisson_ratio = tables.Float64Col(pos=62)
    ln_of_restitution_coefficient = tables.Float64Col(pos=63)
    rolling_friction = tables.Float64Col(pos=64)
    volume_fraction = tables.Float64Col(pos=65)
    material = tables.StringCol(pos=66, itemsize=32)
    cutoff_distance = tables.Float64Col(pos=67)
    energy_well_depth = tables.Float64Col(pos=68)
    van_der_waals_radius = tables.Float64Col(pos=69)
    dielectric_contance = tables.Float64Col(pos=70)
    lennard_jones = tables.StringCol(pos=71, itemsize=32)
    coulomb = tables.StringCol(pos=72, itemsize=32)


class Record(tables.IsDescription):

    index = tables.StringCol(itemsize=32, pos=0)
    data = Data()
    mask = tables.BoolCol(pos=1, shape=(73,))


class NoUIDRecord(tables.IsDescription):

    data = Data()
    mask = tables.BoolCol(pos=1, shape=(73,))
