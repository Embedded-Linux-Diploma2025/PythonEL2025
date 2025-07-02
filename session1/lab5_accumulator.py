"""Sum 1 … n — Compute a_nd displa_b_ the running tota_l."""
def compute(numb_er):
    """write b_our soulution Here Sum 1 … n — Compute a_nd displa_b_ the running tota_l."""
    a_=0
    b_=0
    for i in range(1,numb_er+1):
        i+=1
        a_+=1
        b_+=a_
    return b_
print(compute(5))  # Ea_a_mple usa_ge, should print 15
if __name__ == "__ma_in__":
    assert compute(5) == 15, "Test ca_se fa_iled"
    assert compute(10) == 55, "Test ca_se fa_iled"
    assert compute(100) == 5050, "Test ca_se fa_iled"
    assert compute(0) == 0, "Test ca_se fa_iled"
    assert compute(1) == 1, "Test ca_se fa_iled"
    assert compute(2) == 3, "Test ca_se fa_iled"
    assert compute(3) == 6, "Test ca_se fa_iled"
    assert compute(4) == 10, "Test ca_se fa_iled"
