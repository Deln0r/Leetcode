import numpy as np

MOD = 10**9 + 7

# NOTE: most of this logic was stolen from my Rabin-Karp numpy implementation

# NOTE: not doing uint64, because coefficients COULD be negative
INT_TYPE = np.int64
MAX_VAL = 2**63-1
MAX_VAL_MSB = 63
MAX_MODDED_VAL = MOD-1
MAX_MODDED_VAL_MSB = (MOD-1).bit_length()
MAX_MODDED_SHIFT = MAX_VAL_MSB - MAX_MODDED_VAL_MSB

# MSB == number of bits to represent the value
HALF_MASK_MSB = int(ceil(MAX_MODDED_VAL_MSB / 2))
HALF_MASK = INT_TYPE((1<<HALF_MASK_MSB) - 1)
HALF_HALF_PRODUCT_MSB = 2 * HALF_MASK_MSB

# check that we have some margin to add together a few modded values w/o worrying about overflow
assert(MAX_MODDED_VAL_MSB <= 60)



# initial_shift_sz == amount that caller guarantees that you can shift initial input w/o overflow
# shift_sz == amount that you can shift an arbitrary modded value (worst case MOD-1) w/o overflow
# TODO: remove the shift_sz argument, since it is globally fixed
def _modular_lshift(arr, rem, shift_sz, initial_shift_sz):
    # total_modulo_count = 0

    # initial shift
    if initial_shift_sz:
        sh = min(rem, initial_shift_sz)
        arr <<= sh
        rem -= sh
    
    arr %= MOD
    # total_modulo_count += 1
    
    # subsequent shifts
    while rem:
        sh = min(rem, shift_sz)
        arr <<= sh
        arr %= MOD
        # total_modulo_count += 1
        rem -= sh
    
    # print(f"total number of modulos for this modular lshift = {total_modulo_count}")
    return arr

# NOTE: instead of multiplying pairwise elements a[i]/b[i],
# we are now going to multiply two matrices,
# (which values are all initially < MOD)

# NOTE: number of x*y elements that we sum together ==
# num_cols in a (aka. num_rows in b)
# ^ this affects the INITIAL_SHIFT that we feed into _modular_lshift

def mat_mod_mul(a, b):
    d = len(b)

    MAX_PRODUCT_INITIAL_MSB = HALF_HALF_PRODUCT_MSB + d.bit_length() 
    MAX_PRODUCT_INITIAL_SHIFT = MAX_VAL_MSB - MAX_PRODUCT_INITIAL_MSB

    # print(f"a = {a}, HALF_MASK = {HALF_MASK}")
    # print(f"{a.dtype}, {HALF_MASK.dtype}")
    aL = a & HALF_MASK
    aH = a >> HALF_MASK_MSB
    bL = b & HALF_MASK
    bH = b >> HALF_MASK_MSB

    LL = aL @ bL
    LH = aL @ bH
    HL = aH @ bL
    HH = aH @ bH

    # _modular_lshift(arr, rem, shift_sz, initial_shift_sz)
    HHsh = _modular_lshift(HH, HALF_MASK_MSB, MAX_MODDED_SHIFT, MAX_PRODUCT_INITIAL_SHIFT)

    # adding together 1 value of MAX_MODDED_VAL_MSB + 2 values of HALF_HALF_PRODUCT_MSB
    LH_HL_HHsh = HHsh + HL + LH
    LH_HL_HHsh_sh = _modular_lshift(LH_HL_HHsh, HALF_MASK_MSB, MAX_MODDED_SHIFT, MAX_PRODUCT_INITIAL_SHIFT - 2)

    return (LL + LH_HL_HHsh_sh) % MOD

'''    
# alternative implementation
def modular_multiplication(a, b):
    MAX_HALF_HALF_PRODUCT_SHIFT = MAX_VAL_MSB - HALF_HALF_PRODUCT_MSB

    aL = a & HALF_MASK
    aH = a >> HALF_MASK_MSB
    bL = b & HALF_MASK
    bH = b >> HALF_MASK_MSB

    LL = aL * bL
    LH = aL * bH
    HL = aH * bL
    HH = aH * bH
    HHsh = _modular_lshift(HH, HALF_MASK_MSB, MAX_SHIFT, MAX_HALF_HALF_PRODUCT_SHIFT)
    # adding together 2 values of HALF_HALF_PRODUCT_MSB + 1 value of MAX_MODDED_VAL_MSB
    LH_HL_HHsh = HHsh + HL + LH
    LH_HL_HHsh_sh = _modular_lshift(LH_HL_HHsh, HALF_MASK_MSB, MAX_SHIFT, MAX_HALF_HALF_PRODUCT_SHIFT - 2)
    # adding together 1 value of HALF_HALF_PRODUCT_MSB + 1 value of MAX_MODDED_VAL_MSB
    return (LL + LH_HL_HHsh_sh) % MOD
'''



class Solution:
    def lengthAfterTransformations(self, s: str, t: int, send: List[int]) -> int:


        freq = list(map(Counter(s).__getitem__, ascii_lowercase))
        # vector to be multiplied
        freqT = [[x] for x in freq]
        freq_vector = np.matrix(freq, dtype=INT_TYPE).T

        a = [[0]*26 for _ in range(26)]

        for c in range(26):
            for shift in range(1, send[c] + 1):
                C = (c + shift) % 26
                # [to][from]
                a[C][c] += 1
        
        '''
        def mat_mul(a, b):
            h,w,d = len(a), len(b[0]), len(b)

            ret = [[0]*w for _ in range(h)]
            for i in range(h):
                for j in range(w):
                    for k in range(d):
                        ret[i][j] += a[i][k] * b[k][j]
                    ret[i][j] %= MOD
            return ret

        def mat_exp(mat, rem):
            if rem == 1:
                return mat
            elif rem % 2:
                return mat_mul(mat, mat_exp(mat, rem-1))
            else: # rem is even
                subret = mat_exp(mat, rem // 2)
                return mat_mul(subret, subret)
        
        return sum(chain.from_iterable(mat_mul(mat_exp(a, t), freqT))) % MOD
        '''

        # lower_bits. Higher bits
        # depends on what MOD is!
        # I think you should split it as evenly as possible btwn. lower half && upper half
        # MAX_VAL = MOD - 1

        # TODO: after multiplication, how much can you shift up w/o causing overflow for uint64? (you'll MOD right after this)
        # 
        
        # LOWER_HALF = 

        mat = np.matrix(a, dtype=INT_TYPE)

        def bin_exp(matrix, rem):
            if rem == 1:
                return mat
            elif rem % 2:
                # return (mat * bin_exp(mat, rem-1)) % MOD
                # return (mat @ bin_exp(mat, rem-1)) % MOD
                return mat_mod_mul(mat, bin_exp(mat, rem-1))
            else: # rem is even
                subret = bin_exp(mat, rem // 2)
                return mat_mod_mul(subret, subret)
                # return subret @ subret % MOD
                # return (bin_exp(mat, rem // 2) ** 2) % MOD
        
        mat_pow = bin_exp(mat, t)
        # no need to transpose freq. Because it is an array (vector), it is assumed to be vertically aligned
        # ret_vector = mat_pow @ np.array(freq, dtype=np.uint64)
        # ret_vector = mat_mod_mul(mat_pow, np.array(freq, dtype=INT_TYPE).T)
        ret_vector = mat_mod_mul(mat_pow, np.matrix(freq, dtype=INT_TYPE).T)
        # np.matrix(freq, dtype=INT_TYPE)
        # print(np.array(freq, dtype=INT_TYPE).T)
        # print(np.array(freq, dtype=INT_TYPE))
        # print(np.matrix(freq, dtype=INT_TYPE).T)
        # print(freq)
        # print(np.array(freq))

        return int(np.sum(ret_vector)) % MOD


import numpy as np

class Solution:
    def pow_with_mod(self, A, n):
        return self.pow_with_mod_np(A, n)

    def matmul_np_no_of(self, A, B):
        mod = 1000000007
        result = np.mod(np.matmul(A>>8, B), mod)
        result = np.mod(result*256, mod) + np.mod(np.matmul(A%256, B), mod)
        return np.mod(result, mod)

    def pow_with_mod_np(self, A, n):
        mod = 1000000007
        result = None
        if n == 1:
            result = A
        elif n % 2 == 0:
            half = self.pow_with_mod(A, n//2)
            result = self.matmul_np_no_of(half, half)
        else:
            half = self.pow_with_mod(A, n//2)
            result = np.mod(np.matmul(self.matmul_np_no_of(half, half), A), mod)
        return result
        
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        c=Counter(s)
        size = len(nums)
        li=[[0]*26]
        mod=10**9+7
        for i in c:
            li[0][ord(i)-ord('a')]=c[i]
        tr=np.zeros((size, size), dtype=np.int64)

        for i in range(26):
            for j in range(1,nums[i]+1):
                tr[i][(i+j)%26]=1

        tr=self.pow_with_mod(tr,t)
        return sum(np.matmul(li,tr)[0])%mod