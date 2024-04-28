import streamlit as st
import random    

st.title('Helldivers 2 Equipment Randomizer')

st.subheader("""Use the checkboxes to select the equipment you would like randomized. Then click submit to see the loadout for your next deployment.
            FOR DEMOCRACY""")

primary = st.checkbox('Primary Weapons', key='pw')
pw_list = ['AR-23 Liberator', 'AR-23P Liberator Penetrator', 'AR-23C Liberator Concussive', 'R-63 Diligence', 'R-63CS Diligence Counter-Sniper', 'BR-14 Adjudicator', 'SMG-37 Defender', 'MP-98 Knight', 'SG-8 Punisher', 'SG-8S Slugger', 'SG-225 Breaker', 'SG-225SP Breaker SPRAY & PRAY', 'SG-225IE Breaker Incendiary', 'JAR-5 Dominator', 'R-36 Eruptor', 'ARC-12 Blitzer', 'SG-8P Punisher Plasma', 'LAS-5 Scythe', 'LAS-16 Sickle', 'Plas-1 Scorcher']
secondary = st.checkbox('Secondary Weapons', key='sw')
sw_list = ['P-2 Peacemaker', 'P-19 Redeemer', 'P-19 Redeemer', 'LAS-7 Dagger', 'GP-31 Grenade Pistol']
explosive = st.checkbox('Explosives', key='ex')
ex_list = ['G-12 High Explosive', 'G-6 Frag', 'G-10 Incendiary', 'G-16 Impact', 'G-123 Thermite']
armor_weight = st.checkbox('Armor Weights', key='aw')
aw_list = ['Light', 'Medium', 'Heavy']
armor_passive = st.checkbox('Armor Passives', key='ap')
ap_list = ['Democracy Protects', 'Engineering Kit', 'Extra padding', 'Fortified', 'Med Kit', 'Servo-Assisted', 'Scout']
strat_weapon = st.checkbox('Weapon Stratagems', key='stw')
stw_list = ['EAT-17', 'GR-8 Recoilless Rifle', 'FAF-14 Spear', 'LAS-99, Quasar Cannon', 'GL-21 Grenade Launcher', 'RS-422 Railgun', 'M-105 Stalwart', 'MG-43 Machine Gun', 'MG-206 Heavy Machine Gun', 'APW-1 Anti-Material Rifle', 'AC-8 Autocannon', 'LAS-98 Laser Cannon', 'ARC-3 Arc Thrower', 'FLAM-40 Flamethrower', ]
strat_backpack = st.checkbox('Backpack Stratagem', key='stbp')
stbp_list=['AX/AR-23 Guard Dog', 'AX/LAS-5 Guard Dog Rover', 'LIFT-850 Jump Pack', 'B-1 Supply Pack', 'SH-20 Ballistic Shield Backpack', 'SH-32 Shield Generator Pack']
stratagem = st.checkbox('Stratagems', key='sg')
sg_list = ['EXO-45 Patriot Exosuit', 'E/MG-101 HMG Emplacement', 'FX-12 Shield Generator Relay', 'A/ARC-3 Tesla Tower', 'MD-6 Anti-Personnel Minefield', 'MD-I4 Incendiary Mines', 'A/MG-43 Machine Gun Sentry', 'A/G-16 Gatling Sentry', 'A/M-12 Mortar Sentry', 'A/AC-8 Autocannon Sentry', 'A/MLS-4X Rocket Sentry', 'A/M-23 EMS Mortar Sentry', 'Orbital Gatling Barrage', 'Orbital Airburst Strike', 'Orbital 120MM HE Barrage', 'Orbital 380MM HE Barrage', 'Orbital Walking Barrag', 'Orbital Laser', 'Orbital Railcannon Strike', 'Orbital Precision Strike', 'Orbital Gas Strike', 'Orbital EMS Strike', 'Orbital Smoke Strike', 'Eagle Strafing Run', 'Eagle Airstrike', 'Eagle Cluster Bomb', 'Eagle Napalm Airstrike', 'Eagle Smoke Strike', 'Eagle 110MM Rocket Pods', 'Eagle 500kg Bomb']
booster = st.checkbox('Booster', key='bs')
bs_list = ['Hellpod Space Optimization', 'Vitality Enhancement', 'UAV Recon Booster', 'Stamina Enhancement', 'Muscle Enhancement', 'Increased Reinforcement Budget', 'Flexible Reinforcement Budget', 'Localization Confusion Booster', 'Expert Extraction Pilot Booster']

strat_cntr = 0

# randomizing items
if primary:
    pw_output = random.choice(pw_list)
    
if secondary:
    sw_output = random.choice(sw_list)
    
if explosive:
    ex_output = random.choice(ex_list)
    
if armor_weight:
    aw_output = random.choice(aw_list)

if armor_passive:
    ap_output = random.choice(ap_list)
    
if booster:
    bs_output = random.choice(bs_list)
    
if strat_weapon:
    stw_output = random.choice(stw_list)
    strat_cntr = strat_cntr + 1
    
if strat_backpack:
    stbp_output = random.choice(stbp_list)
    strat_cntr = strat_cntr + 1
    
if stratagem:
    n = 4 - strat_cntr
    sg_rand = random.choices(sg_list, k=n)
    sg_output = """
    
                """.join(sg_rand)

# Displaying randomized items
if st.button('Submit'):
    if primary:
        # st.write('## Primary Weapon:') 
        # st.write(pw_output)
        st.write(f"""
                ## Primary weapon:
                {pw_output}
                """)
        st.divider()
    if secondary:
        st.write(f"""
                 ## Seconary Weapon: 
                 {sw_output}
                 """)
        st.divider()
    if explosive:
        st.write(f"""
                 ## Explosive: 
                 {ex_output}
                 """)
        st.divider()
    if armor_weight:
        st.write(f"""
                 ## Armor Weight: 
                 {aw_output}
                 """)
        st.divider()
    if armor_passive:
        st.write(f"""
                 ## Armor Passive: 
                 {ap_output}
                 """)
        st.divider()
    if booster:
        st.write(f"""
                 ## Booster: 
                 {bs_output}
                 """)
        st.divider()
    if strat_weapon:
        st.write(f"""
                 ## Stratagem Weapon: 
                 {stw_output}
                 """)
        st.divider()
    if strat_backpack:
        st.write(f"""
                 ## Stratagem Backpack: 
                 {stbp_output}
                 """)
        st.divider()
    if stratagem:
        st.write(f"""
                 ## Stratagems: 
                 {sg_output}
                 """)
        st.divider()