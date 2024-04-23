//Evento
$("#add_cart").on("click", function () {
  const { flan_id, user_id, csrf_token } = $("#add_cart").data();

  const requestData = {
    user_id,
    flan_id,
  };

  fetch("/agregar_carrito/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrf_token,
    },
    body: JSON.stringify(requestData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        Swal.fire({
          title: "Flan agregado al carro!",
          icon: "success",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Ir al carrito",
          cancelButtonText: "Seguir viendo",
          backdrop: `
                    rgba(0,0,123,0.4)
                    url("../img/bandera.gif")
                    left top
                    no-repeat
                    `,
          showClass: {
            popup: `
                          animate__animated
                          animate__fadeInUp
                          animate__faster
                        `,
          },
          hideClass: {
            popup: `
                          animate__animated
                          animate__fadeOutDown
                          animate__faster
                        `,
          },
        }).then((result) => {
          if (result.isConfirmed) {
            const url = `/carrito/${data.carrito_uuid}`;
            window.location.href = url;
          }
        });
      } else {
        console.error(data.message); // Manejo de error
      }
    })
    .catch((error) => console.error("Error al agregar al carrito:", error)); // Manejo de errores
});


$("#generar_orden").on("click", function () {
  const { uuid, csrf_token } = $("#generar_orden").data();
  fetch("/carrito_change_status/" + uuid, {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrf_token,
        },
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            Swal.fire({
                position: "top",
                icon: "success",
                title: data.message,
                showConfirmButton: true,
            }).then((result) => {
                window.location.href = "/welcome";
            });
        } else {
            console.error(data.message); // Manejo de error
        }
    });
});

$('input[id^="form_"]').on("click", function () {
  const buttonId = $(this).attr("id");
  const itemId = buttonId.replace("form_", "");

  // Seleccionar el input correspondiente
  const input = $("#form_" + itemId);
  const precio = $("#precio_" + itemId).text().replace("Precio: ", "");

  // Obtener el valor actual y aumentarlo
  var currentValue = parseInt(input.val());
  if (currentValue <= 0) {
    input.val(1);
    $("#total_" + itemId).text("$" + String(precio));
  } else {
    $("#total_" + itemId).text("$" + String(currentValue * precio));
  }
});

function calcularTotal() {
  let total = 0; // Iniciar el total en 0

  // Recorrer todos los inputs con cantidades y precios asociados
  $('input[id^="form_"]').each(function () {
    let itemId = $(this).attr("id").replace("form_", ""); // Obtener el ID del item
    let cantidad = parseInt($(this).val()); // Obtener la cantidad
    cantidad = cantidad < 1 ? 1 : cantidad 
    let precio = parseFloat(
      $("#precio_" + itemId)
        .text()
        .replace("Precio: ", "")
    ); // Obtener el precio

    total += cantidad * precio; // Calcular el subtotal y añadirlo al total
  });

  // Actualizar el total en la etiqueta h5 al final de la lista
  $("#total_final").text("Total: $" + total); // Redondear a 2 decimales
}

// Asignar eventos para recalcular el total cuando se cambie la cantidad
$('input[id^="form_"]').on("change keyup", function () {
  calcularTotal(); // Llamar a la función para recalcular
});

// Calcular el total al cargar la página, por si ya hay valores existentes
calcularTotal();