@staticmethod
def best_switch():
    switch = None
    pokemon = Game.current_pokemon
    opponent = Game.opponent.pokemon
    potential_switches = []
    best_switches = []
    for switch in Game.Opponent_Party:
        if not isinstance(switch, int):
            if switch.current_health > 0:
                potential_switches.append(switch)
    for potential in potential_switches:
        for immune in potential.type.immune_list:
            for no_effect in pokemon.type.no_effect_list:
                if no_effect == immune:
                    best_switches.append(potential)
                    best_switches[0] = potential
                    break
        for resist in potential.type.resist_list:
            for strength in pokemon.type.not_effective_list:
                if strength == resist:
                    best_switches.append(potential)
                    best_switches[0] = potential
                else:
                    if pokemon.type2 != None and potential.type2 != None:
                        for resist2 in potential.type2.resist_list:
                            for strength2 in pokemon.type2.not_effective_list:
                                if strength == resist2 or strength2 == resist:
                                    best_switches.append(potential)
        for weakness in potential.type.weakness_list:
            if pokemon.type.name == weakness:
                potential_switches.remove(potential)
                continue
            if pokemon.type2 != None:
                if pokemon.type2.name == weakness:
                    potential_switches.remove(potential)
        best_switches.append(potential)


    super_effective_list = set(pokemon.type.super_effective_list)
    not_effective_list = set(pokemon.type.not_effective_list)
    no_effect_list = set(pokemon.type.no_effect_list)
    switches = set(potential_switches)
    if len(best_switches) > 1:
        for best in best_switches:
            for immune in best.type.immune_list:
                if immune in no_effect_list:
                    best_switches[0] = best
                    break
            for resist in best.type.resist_list:
                if resist in not_effective_list:
                    best_switches[0] = best
                    break
            if best not in switches:
                best_switches.remove(best)
                continue
            for weakness in best.type.weakness_list:
                if weakness in super_effective_list:
                    best_switches.remove(best)
            #best_switches.remove(best)

        #switch = Game.Opponent_Party.index(best_switches[0])
    if len(best_switches) < 1:
        if len(potential_switches) > 0:
            switch = Game.Opponent_Party.index(potential_switches[0])
    else:
        print best_switches
        switch = Game.Opponent_Party.index(best_switches[0])
    return switch

# #2
switch = 0
pokemon = Game.current_pokemon
opponent = Game.opponent.pokemon
potential_switches = []

for switch in Game.Opponent_Party:
    if not isinstance(switch, int):
        if switch.current_health > 0:
            potential_switches.append(switch)
super_effective_list = set(pokemon.type.super_effective_list)
not_effective_list = set(pokemon.type.not_effective_list)
no_effect_list = set(pokemon.type.no_effect_list)
#switches = set(potential_switches)
if len(potential_switches):
    best_switches = []
    best = None
    while best == None:
        switches = set(best_switches)
        for best in potential_switches:
            for no_effect in pokemon.type.no_effect_list:
                for immune in opponent.type.immune_list:
                    if no_effect == immune and best not in switches:
                        best_switches.append(best)
                        break
            for super_effective in pokemon.type.super_effective_list:
                for weakness in best.type.weakness_list:
                    if super_effective == weakness and best in switches:
                        best_switches.remove(best)
            for not_effective in pokemon.type.super_effective_list:
                for resist in best.type.weakness_list:
                    if not_effective == resist and best not in switches:
                        best_switches.append(best)
                        break
        if len(best_switches) > 1:
            for switch in best_switches:
                for no_effect in pokemon.type.no_effect_list:
                    for immune in opponent.type.immune_list:
                        if no_effect == immune:
                            best = switch
                            break
                for not_effective in pokemon.type.super_effective_list:
                    for resist in best.type.weakness_list:
                        if not_effective == resist:
                            best = switch
                            break
                for super_effective in pokemon.type.super_effective_list:
                    for weakness in best.type.weakness_list:
                        if super_effective == weakness and best in switches:
                            best_switches.remove(switch)
            best = best_switches[0]
#print best_switches
if best_switches:
    switch = Game.Opponent_Party.index(best_switches[0])
return switch
