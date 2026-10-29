# Ejercicio 23 - Árbol de criaturas mitológicas

class Nodo:
    def __init__(self, nombre, derrotada_por=None):
        # Datos de cada criatura
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.descripcion = None
        self.capturada = None

        # Hijos del nodo
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    # Insertar una criatura en el árbol
    def insertar(self, nombre, derrotada_por=None):
        nuevo = Nodo(nombre, derrotada_por)

        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar(self.raiz, nuevo)

    def _insertar(self, actual, nuevo):
        # Si el nombre es menor, va a la izquierda
        if nuevo.nombre < actual.nombre:
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar(actual.izquierda, nuevo)

        # Si el nombre es mayor, va a la derecha
        elif nuevo.nombre > actual.nombre:
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar(actual.derecha, nuevo)

    # Inciso A: listar las criaturas y quién las derrotó en inorden
    def listar_inorden(self):
        self._listar_inorden(self.raiz)

    def _listar_inorden(self, nodo):
        if nodo is not None:
            # Primero recorremos el subárbol izquierdo
            self._listar_inorden(nodo.izquierda)

            # Mostramos la criatura y quién la derrotó
            if nodo.derrotada_por is not None:
                print(f"{nodo.nombre} - Derrotada por: {nodo.derrotada_por}")
            else:
                print(f"{nodo.nombre} - No fue derrotada")

            # Finalmente recorremos el subárbol derecho
            self._listar_inorden(nodo.derecha)

    # Inciso B: buscar una criatura por su nombre
    def buscar(self, nombre):
        actual = self.raiz

        while actual is not None:
            if nombre == actual.nombre:
                return actual
            elif nombre < actual.nombre:
                actual = actual.izquierda
            else:
                actual = actual.derecha

        return None

    # Agregar una descripción a una criatura
    def agregar_descripcion(self, nombre, descripcion):
        criatura = self.buscar(nombre)

        if criatura is not None:
            criatura.descripcion = descripcion
            print(f"Descripción agregada a {nombre}")
        else:
            print(f"No se encontró la criatura {nombre}")

    # Inciso C: mostrar toda la información de una criatura
    def mostrar_criatura(self, nombre):
        criatura = self.buscar(nombre)

        if criatura is not None:
            print(f"Nombre: {criatura.nombre}")
            print(f"Derrotada por: {criatura.derrotada_por}")
            print(f"Descripción: {criatura.descripcion}")
            print(f"Capturada por: {criatura.capturada}")
        else:
            print(f"No se encontró la criatura {nombre}")

    # Inciso D: obtener los 3 héroes o dioses con más victorias
    def top_3_heroes(self):
        victorias = {}

        # Recorrer el árbol y contar las criaturas derrotadas
        self._contar_victorias(self.raiz, victorias)

        # Ordenar por cantidad de victorias, de mayor a menor
        ranking = sorted(
            victorias.items(),
            key=lambda elemento: (-elemento[1], elemento[0])
        )

        # Mostrar los primeros 3
        for heroe, cantidad in ranking[:3]:
            print(f"{heroe}: {cantidad} criaturas derrotadas")

    def _contar_victorias(self, nodo, victorias):
        if nodo is not None:
            # Si la criatura fue derrotada, contamos una victoria
            if nodo.derrotada_por is not None:
                heroe = nodo.derrotada_por

                if heroe not in victorias:
                    victorias[heroe] = 0

                victorias[heroe] += 1

            # Recorrer los dos subárboles
            self._contar_victorias(nodo.izquierda, victorias)
            self._contar_victorias(nodo.derecha, victorias)

    # Inciso E: listar las criaturas derrotadas por Heracles
    def criaturas_de_heracles(self):
        self._criaturas_de_heracles(self.raiz)

    def _criaturas_de_heracles(self, nodo):
        if nodo is not None:
            # Recorremos el subárbol izquierdo
            self._criaturas_de_heracles(nodo.izquierda)

            # Mostramos las criaturas derrotadas por Heracles
            if nodo.derrotada_por == "Heracles":
                print(nodo.nombre)

            # Recorremos el subárbol derecho
            self._criaturas_de_heracles(nodo.derecha)

    # Inciso F: listar las criaturas que no fueron derrotadas
    def criaturas_no_derrotadas(self):
        self._criaturas_no_derrotadas(self.raiz)

    def _criaturas_no_derrotadas(self, nodo):
        if nodo is not None:
            # Recorrer el subárbol izquierdo
            self._criaturas_no_derrotadas(nodo.izquierda)

            # Mostrar solamente las criaturas no derrotadas
            if nodo.derrotada_por is None:
                print(nodo.nombre)

            # Recorrer el subárbol derecho
            self._criaturas_no_derrotadas(nodo.derecha)

    # Inciso G: registrar quién capturó a una criatura
    def capturar_criatura(self, nombre, heroe):
        # Buscar la criatura por su nombre
        criatura = self.buscar(nombre)

        if criatura is not None:
            # Guardar el nombre del héroe que la capturó
            criatura.capturada = heroe
            print(f"{nombre} fue capturada por {heroe}")
        else:
            print(f"No se encontró la criatura {nombre}")

    # Inciso I: buscar criaturas por coincidencia
    def buscar_coincidencia(self, texto):
        print(f"\nResultados de la búsqueda '{texto}':")
        self._buscar_coincidencia(self.raiz, texto)

    def _buscar_coincidencia(self, nodo, texto):
        if nodo is not None:
            # Recorrer el subárbol izquierdo
            self._buscar_coincidencia(nodo.izquierda, texto)

            # Comprobar si el texto aparece dentro del nombre
            if texto.lower() in nodo.nombre.lower():
                print(nodo.nombre)

            # Recorrer el subárbol derecho
            self._buscar_coincidencia(nodo.derecha, texto)

    # Inciso J: eliminar una criatura del árbol
    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        # Si no encontramos la criatura
        if nodo is None:
            return None

        # Buscar la criatura por su nombre
        if nombre < nodo.nombre:
            nodo.izquierda = self._eliminar(nodo.izquierda, nombre)

        elif nombre > nodo.nombre:
            nodo.derecha = self._eliminar(nodo.derecha, nombre)

        else:
            # Caso 1: el nodo no tiene hijo izquierdo
            if nodo.izquierda is None:
                return nodo.derecha

            # Caso 2: el nodo no tiene hijo derecho
            if nodo.derecha is None:
                return nodo.izquierda

            # Caso 3: el nodo tiene dos hijos
            # Buscamos el menor nodo del subárbol derecho
            sucesor = nodo.derecha

            while sucesor.izquierda is not None:
                sucesor = sucesor.izquierda

            # Copiamos todos los datos del sucesor
            nodo.nombre = sucesor.nombre
            nodo.derrotada_por = sucesor.derrotada_por
            nodo.descripcion = sucesor.descripcion
            nodo.capturada = sucesor.capturada

            # Eliminamos el sucesor de su posición original
            nodo.derecha = self._eliminar(nodo.derecha, sucesor.nombre)

        return nodo

    # Inciso K: modificar quién derrotó a una criatura
    def modificar_derrota(self, nombre, heroe, descripcion):
        # Buscar la criatura en el árbol
        criatura = self.buscar(nombre)

        if criatura is not None:
            # Actualizar el héroe que la derrotó
            criatura.derrotada_por = heroe

            # Agregar información sobre la derrota
            criatura.descripcion = descripcion

            print(f"Información de {nombre} actualizada correctamente")
        else:
            print(f"No se encontró la criatura {nombre}")

    # Inciso L: cambiar el nombre de una criatura
    def cambiar_nombre(self, nombre_anterior, nombre_nuevo):
        # Buscar la criatura que queremos modificar
        criatura = self.buscar(nombre_anterior)

        if criatura is not None:
            # Guardar sus datos antes de eliminarla
            derrotada_por = criatura.derrotada_por
            descripcion = criatura.descripcion
            capturada = criatura.capturada

            # Eliminar el nodo con el nombre anterior
            self.eliminar(nombre_anterior)

            # Insertar la criatura con el nombre nuevo
            self.insertar(nombre_nuevo, derrotada_por)

            # Recuperar el nodo recién insertado
            nueva_criatura = self.buscar(nombre_nuevo)

            # Restaurar sus demás datos
            nueva_criatura.descripcion = descripcion
            nueva_criatura.capturada = capturada

            print(f"Nombre modificado: {nombre_anterior} -> {nombre_nuevo}")
        else:
            print(f"No se encontró la criatura {nombre_anterior}")

    # Inciso M: mostrar las criaturas por nivel
    def listar_por_nivel(self):
        if self.raiz is None:
            print("El árbol está vacío")
            return

        # Creamos una cola con la raíz del árbol
        cola = [self.raiz]

        # Mientras haya nodos en la cola
        while len(cola) > 0:
            # Sacamos el primer nodo de la cola
            nodo = cola.pop(0)

            # Mostramos el nombre de la criatura
            print(nodo.nombre)

            # Agregamos sus hijos a la cola
            if nodo.izquierda is not None:
                cola.append(nodo.izquierda)

            if nodo.derecha is not None:
                cola.append(nodo.derecha)

    # Inciso N: listar las criaturas capturadas por Heracles
    def capturadas_por_heracles(self):
        self._capturadas_por_heracles(self.raiz)

    def _capturadas_por_heracles(self, nodo):
        if nodo is not None:
            # Recorrer el subárbol izquierdo
            self._capturadas_por_heracles(nodo.izquierda)

            # Mostrar las criaturas capturadas por Heracles
            if nodo.capturada == "Heracles":
                print(nodo.nombre)

            # Recorrer el subárbol derecho
            self._capturadas_por_heracles(nodo.derecha)

# Crear el árbol de criaturas
arbol = Arbol()

# Cargar todas las criaturas de la tabla del libro
# Si no aparece un héroe o dios, significa que no fue derrotada

arbol.insertar("Ceto")
arbol.insertar("Cerda de Cromión", "Teseo")
arbol.insertar("Tifón", "Zeus")
arbol.insertar("Ortro", "Heracles")
arbol.insertar("Equidna", "Argos Panoptes")
arbol.insertar("Toro de Creta", "Teseo")
arbol.insertar("Dino")
arbol.insertar("Jabalí de Calidón", "Atalanta")
arbol.insertar("Pefredo")
arbol.insertar("Carcinos")
arbol.insertar("Enio")
arbol.insertar("Gerión", "Heracles")
arbol.insertar("Escila")
arbol.insertar("Cloto")
arbol.insertar("Caribdis")
arbol.insertar("Láquesis")
arbol.insertar("Euríale")
arbol.insertar("Átropos")
arbol.insertar("Esteno")
arbol.insertar("Minotauro de Creta", "Teseo")
arbol.insertar("Medusa", "Perseo")
arbol.insertar("Harpías")
arbol.insertar("Ladón", "Heracles")
arbol.insertar("Argos Panoptes", "Hermes")
arbol.insertar("Águila del Cáucaso")
arbol.insertar("Aves del Estínfalo")
arbol.insertar("Quimera", "Belerofonte")
arbol.insertar("Talos", "Medea")
arbol.insertar("Hidra de Lerna", "Heracles")
arbol.insertar("Sirenas")
arbol.insertar("León de Nemea", "Heracles")
arbol.insertar("Pitón", "Apolo")
arbol.insertar("Esfinge", "Edipo")
arbol.insertar("Cierva de Cerinea")
arbol.insertar("Dragón de la Cólquida")
arbol.insertar("Basilisco")
arbol.insertar("Cerbero")
arbol.insertar("Jabalí de Erimanto")

print("Criaturas cargadas correctamente")

# Inciso A: mostrar las criaturas en orden alfabético
print("\nCriaturas ordenadas alfabéticamente:")
arbol.listar_inorden()

# Inciso B: agregar descripciones a las criaturas
print("\nAgregar descripciones:")

arbol.agregar_descripcion(
    "Medusa",
    "Criatura con serpientes en lugar de cabello que petrificaba con la mirada."
)

arbol.agregar_descripcion(
    "Talos",
    "Gigante de bronce que protegía la isla de Creta."
)

arbol.agregar_descripcion(
    "Cerbero",
    "Perro de tres cabezas que custodiaba la entrada al inframundo."
)

# Inciso C: mostrar toda la información de Talos
print("\nInformación de Talos:")
arbol.mostrar_criatura("Talos")

# Inciso D: mostrar los 3 héroes o dioses con más victorias
print("\nLos 3 héroes o dioses que derrotaron más criaturas:")
arbol.top_3_heroes()

# Inciso E: mostrar las criaturas derrotadas por Heracles
print("\nCriaturas derrotadas por Heracles:")
arbol.criaturas_de_heracles()

# Inciso F: mostrar las criaturas que no fueron derrotadas
print("\nCriaturas que no fueron derrotadas:")
arbol.criaturas_no_derrotadas()

# Incisos G y H: registrar las criaturas capturadas por Heracles
print("\nCriaturas capturadas por Heracles:")

arbol.capturar_criatura("Cerbero", "Heracles")
arbol.capturar_criatura("Toro de Creta", "Heracles")
arbol.capturar_criatura("Cierva de Cerinea", "Heracles")
arbol.capturar_criatura("Jabalí de Erimanto", "Heracles")

# Inciso I: buscar criaturas por coincidencia
arbol.buscar_coincidencia("de Creta")
arbol.buscar_coincidencia("Jabalí")

# Inciso J: eliminar a Basilisco y Sirenas
print("\nEliminación de criaturas:")

arbol.eliminar("Basilisco")
arbol.eliminar("Sirenas")

# Comprobar que fueron eliminadas
if arbol.buscar("Basilisco") is None:
    print("Basilisco eliminado correctamente")

if arbol.buscar("Sirenas") is None:
    print("Sirenas eliminadas correctamente")

# Inciso K: modificar las Aves del Estínfalo
print("\nModificación de las Aves del Estínfalo:")

arbol.modificar_derrota(
    "Aves del Estínfalo",
    "Heracles",
    "Heracles derrotó a varias de estas criaturas."
)

# Mostrar los datos actualizados
arbol.mostrar_criatura("Aves del Estínfalo")

# Inciso L: cambiar Ladón por Dragón Ladón
print("\nModificación del nombre de Ladón:")

arbol.cambiar_nombre("Ladón", "Dragón Ladón")

# Mostrar la información con el nuevo nombre
arbol.mostrar_criatura("Dragón Ladón")

# Inciso M: mostrar las criaturas por nivel
print("\nCriaturas listadas por nivel:")
arbol.listar_por_nivel()

# Inciso N: mostrar las criaturas capturadas por Heracles
print("\nCriaturas capturadas por Heracles:")
arbol.capturadas_por_heracles()

