import numpy as np
from micromdo.explicit_component import ExplicitComponent


class XComp(ExplicitComponent):

    def __init__(self):
        super(XComp, self).__init__()
        self.add_output('x', shape=(3,))

    def compute(self, inputs, outputs):
        outputs['x'][:] = [2, 3, 4]

    def compute_partials(self, inputs, partials):
        partials['x', 'x'][:] = np.eye(3)

    def solve_linear(rhs_vec, sol_vec):
        sol_vec['x'][:] = rhs_vec['x']


class YComp(ExplicitComponent):

    def __init__(self):
        super(XComp, self).__init__()
        self.add_input('x', shape=(3,))
        self.add_output('y1', shape=(3,))
        self.add_output('y2', shape=(3,))

    def compute(self, inputs, outputs):
        outputs['y1'][:] = 5 * inputs['x']
        outputs['y2'][:] = 5 * inputs['x'] + 3

    def compute_partials(self, inputs, partials):
        partials['y1', 'x'][:] = 5 * np.eye(3)
        partials['y2', 'x'][:] = 5 * np.eye(3)


class ZComp(ExplicitComponent):

    def __init__(self):
        super(XComp, self).__init__()
        self.add_input('x', shape=(3,))
        self.add_input('y1', shape=(3,))
        self.add_input('y2', shape=(3,))
        self.add_output('z', shape=(3,))

    def compute(self, inputs, outputs):
        outputs['z'][:] = inputs['y1']**2 + inputs['x']**3 - inputs['y2']

    def compute_partials(self, inputs, partials):
        partials['z', 'x'][:] = 3 * inputs['x']**2
        partials['z', 'y1'][:] = 2 * inputs['y1']
        partials['z', 'y2'][:] = -1.0


def gs_forward_example():
    nn = 3
    
    data = np.empty(nn * 3)
    nl_vec = {}
    nl_vec['x'] = data[:3]
    nl_vec['y'] = data[3:6]
    nl_vec['z'] = data[6:9]
    
    data_o = np.empty(nn * 3)
    ln_o = {}
    ln_o['x'] = data_o[:3]
    ln_o['y'] = data_o[3:6]
    ln_o['z'] = data_o[6:9]
    
    data_r = np.empty(nn * 3)
    ln_r = {}
    ln_r['x'] = data_r[:3]
    ln_r['y'] = data_r[3:6]
    ln_r['z'] = data_r[6:9]
    
    print(50 * '#')
    print('# Nonlinear run')
    print(50 * '#')
    print('init:', data)
    print()

    X = XComp()
    Y = YComp()
    Z = ZComp()

    X.compute(nl_vec, nl_vec)
    print('after X:', data)
    print()

    Y.compute(nl_vec, nl_vec)
    print('after Y:', data)
    print()

    Z.compute(nl_vec, nl_vec)
    print('after Z:', data)
    print()

    print()
    print()

    exit(0)

    print(50 * '#')
    print('# Linear run')
    print(50 * '#')

    data_r[:] = 0
    data_o[:] = 0

    # ln_r['x'][:3] = 1.
    ln_r['x'][0] = 1.

    print('init rhs', data_r)
    print('.       ', data_o)

    print('X block')
    X_apply_linear(nl_vec, nl_vec, ln_o, ln_o, ln_r, mode='fwd', sign='neg')
    print('  X apply', data_r)
    X_solve_linear(ln_r, ln_o)
    print('  X solve', data_r)
    print('         ', data_o)

    print('Y block')
    Y_apply_linear(nl_vec, nl_vec, ln_o, ln_o, ln_r, mode='fwd', sign='neg')
    print('  Y apply', data_r)
    Y_solve_linear(ln_r, ln_o)
    print('  Y solve', data_r)
    print('         ', data_o)

    print('Z block')
    Z_apply_linear(nl_vec, nl_vec, ln_o, ln_o, ln_r, mode='fwd', sign='neg')
    print('  Z apply', data_r)
    Z_solve_linear(ln_r, ln_o)
    print('  Z solve', data_r)
    print('         ', data_o)


    print('CS check')
    data_r[:] = data
    print(data_r)
    data_r[0] += .000001
    print(data_r)

    # X(ln_r, ln_r)
    Y(ln_r, ln_r)
    Z(ln_r, ln_r)


    fd_check = (ln_r['z'] - nl_vec['z']) / .000001
    print('fd ', fd_check)


    # want dz/dx




if __name__ == '__main__':
    gs_forward_example()