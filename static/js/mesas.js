var vacio = "None";
var disponible = "disponible";
var ocupado = "ocupado";
var no_disponible = "no disponible";
var clientes = document.querySelectorAll(".cliente");
var seña = document.querySelectorAll(".seña");
var reserva = document.querySelectorAll(".reserva");
var estado = document.querySelectorAll(".cartauwu");
var carta = document.querySelectorAll(".carta");
var vacios = document.getElementsByTagName("dato");
// 



Array.from(clientes).forEach(e => {
    if (e.textContent.includes(vacio)) {
        e.textContent = "";
    }
})

Array.from(seña).forEach(e => {
    if (e.textContent.includes(vacio)) {
        e.textContent = "";
        e.setAttribute('style', 'margin-bottom: 35%');
    }
})


Array.from(estado).forEach(e => {
    if (e.textContent.includes(no_disponible)) {
        e.classList.add('mesa-no-disponible');
    } else if (e.textContent.includes(disponible)) {
        e.classList.add('mesa-libre');
        e.querySelector('.iniciar_servicio').classList.remove('iniciar_servicio');
    } else if (e.textContent.includes(ocupado)) {
        e.classList.add('mesa-ocupada');
        e.querySelector('.ver').classList.remove('ver');
        e.querySelector('.terminar').classList.remove('terminar');
    }
})




Array.from(vacios).forEach(e => {
    if (e.textContent.includes("None")) {
        e.textContent = "-";
    }
})

function confirmar() {
    alert('¿Estás seguro de que deseas crear una nueva mesa?');
}

function cambiarEstado() {
    checkbox = document.getElementById("estado");
    valor = document.getElementById("estado_mesa");
    if (checkbox.checked) {
        checkbox.textContent = "Disponible";
        valor.value = "disponible";
        checkbox.checked = false;
    } else {
        checkbox.textContent = "Ocupado"
        valor.value = "ocupado";
        checkbox.checked = true;
    }
}

function verContrasenia() {
    var tipo = document.getElementById("pass");
    if (tipo.type == "password") {
        tipo.type = "text";
    } else {
        tipo.type = "password";
    }
}

function openCreationForm() {
    document.getElementById("crear_mesa").style.display = "block";
}

function closeCreationForm() {
    document.getElementById("crear_mesa").style.display = "none";
}

function getMesas() {
    var cantidad_mesas;
    var list = document.getElementsByClassName("card-title");
    for (var i = 1; i <= list.length; i++) {
        cantidad_mesas = i;
    }
    console.log(cantidad_mesas);
    document.getElementById("creacion_mesa").value = (cantidad_mesas + 1);
    document.getElementById("creacion_mesa").innerHTML = (cantidad_mesas + 1);
}

function openModifyForm() {
    document.getElementById("editar_mesa").style.display = "block";
}

function closeModifyForm() {
    document.getElementById("editar_mesa").style.display = "none";
}

function openDeleteForm() {
    document.getElementById("borrar_mesa").style.display = "block";
}

function closeDeleteForm() {
    document.getElementById("borrar_mesa").style.display = "none";
}

let selectElement = document.getElementById("loop");

// Itera desde 1 hasta 50 para crear las opciones
for (let i = 1; i <= 50; i++) {
    // Crea un nuevo elemento option
    let optionElement = document.createElement("option");
    
    // Asigna el valor y el texto de la opción
    optionElement.value = i;
    optionElement.text = i;

    // Agrega la opción al elemento select
    selectElement.add(optionElement);
}

function openEditForm(nombre, cantidad) {
    document.getElementById("editar_producto").style.display = "block";

    var form = document.getElementById('editForm');
    form.querySelector('#nombre_edit').value = nombre;
    var cantidadSelect = form.querySelector('#cantidad_edit');

    cantidad = parseInt(cantidad);

    for (var i = 1; i <= 20; i++) {
        var option = document.createElement("option");
        option.value = i;
        option.text = i;

        if (i === cantidad) {
            option.selected = true;
        }

        cantidadSelect.appendChild(option);
    }
    document.getElementById('editar_producto').style.display = 'block';
}

function closeEditForm() {
    // Oculta el popup cuando se cierra
    document.getElementById("editar_producto").style.display = "none";
}
 //Función para calcular la suma de los precios
 function calcularTotal() {
    var precios = document.querySelectorAll('#precio');
    var total = 0;
    precios.forEach(function (precio) {
        total += parseFloat(precio.textContent.replace('$', ''));
    });

    return total.toFixed(2); // Redondear a 2 decimales
}
 //Función para actualizar el contenido del elemento 'monto'
function actualizarTotal() {
    var monto = document.getElementById('monto');
    monto.textContent = 'Total: $' + calcularTotal();
}
actualizarTotal()

/* SEARCH
const searchInput = document.querySelector("[busqueda-datos]").style.display = "background-color: red"

let empleados = document.querySelectorAll("nombre")
searchInput.addEventListener("input", e => {
    const value = e.target.value.toLowerCase()
    empleados.forEach(empleado => {
        const visible =
            empleado.toLowerCase().includes(value)
        document.querySelector("[lista-datos]").style.display = "none";
        empleado.element.classList.toggle("hide", !visible)
    })
})

FORMATEAR MONEDA LOCAL 
onBlur="toFinalNumberFormat(this)"
function toFinalNumberFormat(controlToCheck) {
    var enteredNumber = '' + controlToCheck.value;
    enteredNumber = enteredNumber.replace(/[^0-9\.]+/g, '');
    controlToCheck.value = Number(enteredNumber).toLocaleString('es-AR', { style: 'currency', currency: 'ARS' });
}

*/