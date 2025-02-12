class MatrixOperations:
    
    @staticmethod
    def is_valid_matrix(matrix):
        if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("The input must be a list of lists.")
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise ValueError("All rows must have the same number of columns.")
        return True

    @staticmethod
    def transpose_matrix(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    @staticmethod
    def row_sums(matrix):
        return [sum(row) for row in matrix]

    @staticmethod
    def column_products(matrix):
        transposed = MatrixOperations.transpose_matrix(matrix)
        products = []
        for column in transposed:
            product = 1
            for element in column:
                product *= element
            products.append(product)
        return products

    @staticmethod
    def spiral_traversal(matrix):
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                result.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result

    @staticmethod
    def rotate_matrix(matrix, degrees):
        if degrees == 90:
            return [list(reversed(col)) for col in zip(*matrix)]
        elif degrees == 180:
            return [row[::-1] for row in matrix[::-1]]
        else:
            raise ValueError("Only 90 and 180 degrees are supported.")

# example matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

try:
    if MatrixOperations.is_valid_matrix(matrix):
        print("Matrix is valid.")
        
# to transpose the matrix
        transposed = MatrixOperations.transpose_matrix(matrix)
        print("Transpose of the matrix:")
        for row in transposed:
            print(row)
        
# in order to sums rows
        print("Sum of each row:", MatrixOperations.row_sums(matrix))
        
# to do the Column products
        print("Product of each column:", MatrixOperations.column_products(matrix))
        
# to do the spiral traversal
        print("Matrix spiral traversal:", MatrixOperations.spiral_traversal(matrix))
        
# in order to rotate 90 degrees
        rotated_90 = MatrixOperations.rotate_matrix(matrix, 90)
        print("Matrix rotated 90 degrees clockwise:")
        for row in rotated_90:
            print(row)
        
# in  order to rotate 180 degrees
        rotated_180 = MatrixOperations.rotate_matrix(matrix, 180)
        print("Matrix rotated 180 degrees:")
        for row in rotated_180:
            print(row)
except ValueError as e:
    print(f"Error: {e}")
