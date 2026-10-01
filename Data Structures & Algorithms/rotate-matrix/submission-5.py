class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layers = n // 2

        for i in range(layers):
            for j in range(i,n-i-1):
                top_left = matrix[i][j]
                print(top_left)
                top_right = matrix[j][n-1-i]
                print(top_right)
                bot_right = matrix[n-1-i][n-1-j]
        
                print(bot_right)
                print("bot right")
                print(n-1-i, n-1-j)
                bot_left = matrix[n-1-j][i]
                print(bot_left)
                print(n-1-j,i)
                print("NEXT")

                matrix[i][j] = bot_left
                matrix[j][n-1-i] = top_left
                matrix[n-1-i][n-1-j] =top_right
                matrix[n-1-j][i] =bot_right

                #matrix
            print("------------")