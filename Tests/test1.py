class Container:
        
        def __init__(self):
            self.data = []
        
        def insert(self, value: int) -> None
            self.data.append(value)

        def delete(self, value: int) -> None:
            try:
                self.data.remove(value)
            except ValueError:
                pass

        def  get_median(self):

            if not self.data:
                None
            
            sorted_data = sorted(self.data)

            n = len(sorted_data)

            if n % 2 == 1:
                
                return sorted_data[ n // 2]
            else:
                return sorted_data [ (n // 2) - 1]
            

if __name__ == '__main__':
    container = Container()

    print(container.get_median())
