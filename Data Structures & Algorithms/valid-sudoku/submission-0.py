class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map, col_map = { i: set() for i in range(9) }, { i: set() for i in range(9) }
        block_map = { f'{i}{j}': set() for i in range(3) for j in range(3) }

        for row_index, row in enumerate(board):
            for col_index, ij_element in enumerate(row):
                if ij_element == '.':
                    continue
                if ij_element in row_map[row_index]:
                    return False
                if ij_element in col_map[col_index]:
                    return False
                block_number = f'{row_index // 3}{col_index // 3}'
                if ij_element in block_map[block_number]:
                    return False
                row_map[row_index].add(ij_element)
                col_map[col_index].add(ij_element)
                block_map[block_number].add(ij_element)
        return True