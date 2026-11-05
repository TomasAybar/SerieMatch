class MaxHeap:
    def __init__(self):
        self.heap = []

    def swapp(self, i, j):
        """Intercambia dos nodos en el heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def burbujeo_arriba(self, index):
        """Realiza el burbujeo hacia arriba para mantener la propiedad del MaxHeap."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.swapp(index, parent)
            self.burbujeo_arriba(parent)

    def burbujeo_abajo(self, index):
        """Realiza el burbujeo hacia abajo para mantener la propiedad del MaxHeap."""
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swapp(index, largest)
            self.burbujeo_abajo(largest)

    def insert(self, value):
        """Inserta un nuevo valor en el heap."""
        self.heap.append(value)
        self.burbujeo_arriba(len(self.heap) - 1)

    def extract_max(self):
        """Extrae y devuelve el máximo valor del heap."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.burbujeo_abajo(0)
        return root
