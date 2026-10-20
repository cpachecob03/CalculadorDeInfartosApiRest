document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('imcForm');
    const resultadoContainer = document.getElementById('resultadoContainer');

    // Seleccionamos los inputs para poder escucharlos individualmente si lo deseas
    const inputNombre = document.getElementById('nombre');
    const inputPeso = document.getElementById('peso');
    const inputAltura = document.getElementById('altura');
    const inputEdad = document.getElementById('edad');

    // Opcional: Escuchar eventos de cambio/input en las cajas en tiempo real
    const inputs = [inputNombre, inputPeso, inputAltura, inputEdad];
    inputs.forEach(input => {
        input.addEventListener('input', (e) => {
            console.log(`Campo [${e.target.id}] modificado:`, e.target.value);
            // Aquí puedes añadir lógica en tiempo real si lo necesitas (ej. validaciones visuales)
        });
    });

    // Escuchar el evento de envío del formulario (al hacer clic en el botón)
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // Recoger los datos de las cajas ajustados al modelo de Pydantic
        const datos = {
            nombre: inputNombre.value,
            peso_persona: parseFloat(inputPeso.value),
            altura_persona: parseFloat(inputAltura.value),
            edad: parseInt(inputEdad.value)
        };

        try {
            // Petición POST al backend de FastAPI
            const response = await fetch('/api/calcular-imc', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datos)
            });

            if (!response.ok) {
                throw new Error('Error al conectar con el servidor');
            }

            const resultado = await response.json();

            // Rellenar los elementos del DOM con la respuesta del backend
            document.getElementById('resSolicitante').textContent = resultado.solicitante;
            document.getElementById('resImc').textContent = resultado.calculo_imc.toFixed(2);
            document.getElementById('resCategoria').textContent = resultado.categoria_peso;
            document.getElementById('resProbabilidad').textContent = resultado.probabilidad_infarto;
            document.getElementById('resRecomendacion').textContent = resultado.recomendacion;

            // Mostrar el contenedor de resultados
            resultadoContainer.classList.remove('hidden');

        } catch (error) {
            alert('Ocurrió un error al procesar el cálculo. Revisa la consola.');
            console.error(error);
        }
    });
});