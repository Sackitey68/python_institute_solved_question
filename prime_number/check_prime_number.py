def is_prime(num):

        divisor = 2

            while divisor < num:
                        if num % divisor == 0:
                                        return False
                                            divisor = divisor + 1
                                                    
                                                        return True
                                                                
                                                                

                                                    for i in range(1, 20):
                                                            if is_prime(i + 1):
                                                                            print(i + 1, end=" ")
                                                                            print()

