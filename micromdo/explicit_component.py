import numpy as np


class Component(object):

    def __init__(self):
        self._input_vars = {}
        self._output_vars = {}

    def add_input(self, name, shape):
        self._input_vars[name] = {}
        self._input_vars[name]['shape'] = shape

    def add_output(self, name, shape):
        self._output_vars[name] = {}
        self._output_vars[name]['shape'] = shape

    def solve_linear(rhs_vec, sol_vec):
        pass

    def apply_linear(self, inputs, outputs, d_i, d_o, d_r, mode='fwd', sign='pos'):
        if sign == 'pos':
            if mode == 'fwd':
                for ip in inputs.keys():
                    for op in outputs.keys():
                        if ip in d_r:
                            d_r[op] += -self.jac[op, ip] * d_i[ip]
            else:  # rev
                pass
        else:  # neg
            if mode == 'fwd':
                for ip in inputs.keys():
                    for op in outputs.keys():
                        if ip in d_r:
                            d_r[op] += self.jac[op, ip] * d_i[ip]
            else:  # rev
                pass

    class ExplicitComponent(object):

        def compute(self, inputs, outputs):
            pass

        def compute_partials(self, inputs, partials):
            pass

        def solve_linear(self, rhs_vec, sol_vec):
            for op in self._output_vars:
                sol_vec[op][:] = rhs_vec[op][:]

        def linearize(self):
            pass


def X(inputs, outputs):
    outputs['x'][:] = [2,3,4]

def Y(inputs, outputs):
    outputs['y'][:] = 5 * inputs['x']

def Z(inputs, outputs):
    outputs['z'][:] = inputs['y']**2 + inputs['x']**3
