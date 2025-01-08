def find_max_skill():
    
    print("Masukkan jumlah pemain (N) dan tingkat kemahiran awal Juned (M), dipisahkan dengan spasi:")
    N, M = map(int, input().split())
    if not (1 <= N <= 100 and 1 <= M <= 100):
        print("Jumlah pemain (N) dan kemahiran awal (M) harus dalam rentang 1 <= N, M <= 100")
        return

    
    print(f"Masukkan tingkat kemahiran (A[i]) dari {N} pemain, dipisahkan dengan spasi:")
    A = list(map(int, input().split()))
    if len(A) != N or any(a < 1 or a > 1000 for a in A):
        print("Masukkan A[i] sebanyak N elemen dengan nilai 1 <= A[i] <= 1000")
        return

   
    print(f"Masukkan tambahan kemahiran (B[i]) dari {N} pemain, dipisahkan dengan spasi:")
    B = list(map(int, input().split()))
    if len(B) != N or any(b < 1 or b > 1000 for b in B):
        print("Masukkan B[i] sebanyak N elemen dengan nilai 1 <= B[i] <= 1000")
        return

    
    players = sorted(zip(A, B))  

    max_skill = M  
    for skill, bonus in players:
        if skill <= max_skill: 
            max_skill += bonus

  
    print("Tingkat kemahiran maksimum yang dapat dicapai Juned:", max_skill)


find_max_skill()
