def mixing_protien(init_state, num_mutations):
    idx_by_protien = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3
    }
    protien_by_idx = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D'
    }
    state = [idx_by_protien[c] for c in init_state]
    for _ in range(num_mutations):
        curr_state = []
        for i in range(len(state)):
            if i < len(state) - 1:
                curr_state.append(state[i] ^ state[i+1])
            else:
                curr_state.append(state[i] ^ state[0])
        state = curr_state



mixing_protien('AAAAD', 15)
