
# Ejercicio 5 - Árbol de superhéroes y villanos del MCU

class Nodo:
    def __init__(self, nombre, heroe):
        self.nombre = nombre
        self.heroe = heroe  # True si es héroe, False si es villano
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    # Insertar un personaje en el árbol
    def insertar(self, nombre, heroe):
        nuevo = Nodo(nombre, heroe)

        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar(self.raiz, nuevo)

    def _insertar(self, actual, nuevo):
        # Los nombres menores van a la izquierda
        if nuevo.nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar(actual.izquierda, nuevo)

        # Los nombres mayores van a la derecha
        elif nuevo.nombre > actual.nombre:
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar(actual.derecha, nuevo)
    # Inciso B: listar los villanos en orden alfabético
    def listar_villanos(self):
        self._listar_villanos(self.raiz)

    def _listar_villanos(self, nodo):
        if nodo is not None:
            # Primero recorremos el subárbol izquierdo
            self._listar_villanos(nodo.izquierda)

            # Mostramos solamente los villanos
            if nodo.heroe == False:
                print(nodo.nombre)

            # Finalmente recorremos el subárbol derecho
            self._listar_villanos(nodo.derecha)

    # Inciso C: mostrar los superhéroes que empiezan con C
    def heroes_con_c(self):
        self._heroes_con_c(self.raiz)

    def _heroes_con_c(self, nodo):
        if nodo is not None:
            # Recorremos el subárbol izquierdo
            self._heroes_con_c(nodo.izquierda)

            # Verificamos si es héroe y empieza con C
            if nodo.heroe == True and nodo.nombre.startswith("C"):
                print(nodo.nombre)

            # Recorremos el subárbol derecho
            self._heroes_con_c(nodo.derecha)

    # Inciso D: contar cuántos superhéroes hay en el árbol
    def contar_heroes(self):
        return self._contar_heroes(self.raiz)

    def _contar_heroes(self, nodo):
        # Si el nodo está vacío, no sumamos nada
        if nodo is None:
            return 0

        # Contamos los héroes del subárbol izquierdo
        izquierda = self._contar_heroes(nodo.izquierda)

        # Contamos los héroes del subárbol derecho
        derecha = self._contar_heroes(nodo.derecha)

        # Si el personaje actual es héroe, sumamos 1
        if nodo.heroe == True:
            return izquierda + derecha + 1

        # Si es villano, no lo contamos
        return izquierda + derecha

        # Inciso E: buscar personajes por proximidad
    def buscar_proximidad(self, texto):
        return self._buscar_proximidad(self.raiz, texto)

    def _buscar_proximidad(self, nodo, texto):
        if nodo is None:
            return None

        # Buscar si el texto coincide con una parte del nombre
        if texto.lower() in nodo.nombre.lower():
            return nodo

        # Buscar en el subárbol izquierdo
        encontrado = self._buscar_proximidad(nodo.izquierda, texto)

        if encontrado is not None:
            return encontrado

        # Buscar en el subárbol derecho
        return self._buscar_proximidad(nodo.derecha, texto)

    # Eliminar un personaje del árbol
    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        if nodo is None:
            return None

        if nombre < nodo.nombre:
            nodo.izquierda = self._eliminar(nodo.izquierda, nombre)

        elif nombre > nodo.nombre:
            nodo.derecha = self._eliminar(nodo.derecha, nombre)

        else:
            # Si no tiene hijo izquierdo, devolver el derecho
            if nodo.izquierda is None:
                return nodo.derecha

            # Si no tiene hijo derecho, devolver el izquierdo
            if nodo.derecha is None:
                return nodo.izquierda

            # Si tiene dos hijos, buscar el menor del subárbol derecho
            sucesor = nodo.derecha

            while sucesor.izquierda is not None:
                sucesor = sucesor.izquierda

            # Reemplazar los datos del nodo
            nodo.nombre = sucesor.nombre
            nodo.heroe = sucesor.heroe

            # Eliminar el sucesor de su posición original
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.nombre)

        return nodo

    # Corregir el nombre de un personaje
    def corregir_nombre(self, texto, nombre_correcto):
        personaje = self.buscar_proximidad(texto)

        if personaje is not None:
            nombre_anterior = personaje.nombre
            es_heroe = personaje.heroe

            # Eliminar el nombre incorrecto
            self.eliminar(nombre_anterior)

            # Insertar el nombre correcto
            self.insertar(nombre_correcto, es_heroe)

            print(f"Nombre corregido: {nombre_anterior} -> {nombre_correcto}")
        else:
            print("No se encontró el personaje")

    # Inciso F: listar los superhéroes en orden descendente
    def heroes_descendente(self):
        self._heroes_descendente(self.raiz)

    def _heroes_descendente(self, nodo):
        if nodo is not None:
            # Primero recorremos el subárbol derecho
            self._heroes_descendente(nodo.derecha)

            # Mostramos solamente los superhéroes
            if nodo.heroe == True:
                print(nodo.nombre)

            # Finalmente recorremos el subárbol izquierdo
            self._heroes_descendente(nodo.izquierda)

    # Inciso G: separar héroes y villanos en dos árboles
    def generar_bosque(self):
        arbol_heroes = Arbol()
        arbol_villanos = Arbol()

        # Recorrer el árbol original y separar los personajes
        self._separar_personajes(self.raiz, arbol_heroes, arbol_villanos)

        return arbol_heroes, arbol_villanos

    def _separar_personajes(self, nodo, arbol_heroes, arbol_villanos):
        if nodo is not None:
            # Si es héroe, se inserta en el árbol de héroes
            if nodo.heroe == True:
                arbol_heroes.insertar(nodo.nombre, True)
            else:
                # Si es villano, se inserta en el árbol de villanos
                arbol_villanos.insertar(nodo.nombre, False)

            # Recorrer los hijos del nodo
            self._separar_personajes(nodo.izquierda, arbol_heroes, arbol_villanos)
            self._separar_personajes(nodo.derecha, arbol_heroes, arbol_villanos)

    # Contar todos los nodos de un árbol
    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0

        # Contar el nodo actual y sus dos subárboles
        return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)

    # Mostrar todos los personajes en orden alfabético
    def listar_inorden(self):
        self._listar_inorden(self.raiz)

    def _listar_inorden(self, nodo):
        if nodo is not None:
            # Izquierda, raíz, derecha
            self._listar_inorden(nodo.izquierda)
            print(nodo.nombre)
            self._listar_inorden(nodo.derecha)

# Crear el árbol
arbol = Arbol()

# Cargar personajes
arbol.insertar("Iron Man", True)
arbol.insertar("Thanos", False)
arbol.insertar("Captain America", True)
arbol.insertar("Loki", False)
arbol.insertar("Captain Marvel", True)
arbol.insertar("Ultron", False)
arbol.insertar("Doctor Strang", True)
arbol.insertar("Hulk", True)

print("Personajes cargados correctamente")

# Mostrar los villanos ordenados alfabéticamente
print("\nVillanos ordenados alfabéticamente:")
arbol.listar_villanos()

# Mostrar los superhéroes que empiezan con C
print("\nSuperhéroes que empiezan con C:")
arbol.heroes_con_c()

# Inciso D: mostrar la cantidad de superhéroes
print("\nCantidad de superhéroes:")
print(arbol.contar_heroes())

# Inciso E: buscar y corregir el nombre de Doctor Strange
print("\nCorrección del nombre de Doctor Strange:")
arbol.corregir_nombre("Doctor Str", "Doctor Strange")

# Inciso F: mostrar superhéroes en orden descendente
print("\nSuperhéroes ordenados de manera descendente:")
arbol.heroes_descendente()

# Inciso G: generar un bosque de héroes y villanos
arbol_heroes, arbol_villanos = arbol.generar_bosque()

# Inciso G.I: contar los nodos de cada árbol
print("\nCantidad de nodos del árbol de héroes:")
print(arbol_heroes.contar_nodos())

print("\nCantidad de nodos del árbol de villanos:")
print(arbol_villanos.contar_nodos())

# Inciso G.II: listar ambos árboles alfabéticamente
print("\nÁrbol de héroes ordenado alfabéticamente:")
arbol_heroes.listar_inorden()

print("\nÁrbol de villanos ordenado alfabéticamente:")
arbol_villanos.listar_inorden()