package com.nachofg.prediccionpalabras

import android.os.Bundle
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import com.android.volley.Request
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.Volley
import org.json.JSONObject

class MainActivity : AppCompatActivity() {

    private lateinit var entrada: EditText
    private lateinit var botonPredecir: Button
    private lateinit var predicciones: TextView
    private lateinit var progressBar: ProgressBar

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        entrada = findViewById(R.id.entrada)
        botonPredecir = findViewById(R.id.botonPredecir)
        predicciones = findViewById(R.id.predicciones)
        progressBar = findViewById(R.id.progressBar)

        botonPredecir.setOnClickListener {
            val palabra = entrada.text.toString().trim()
            if (palabra.isNotEmpty()) {
                predecirPalabras(palabra)
            } else {
                predicciones.text = "Por favor, escribe una palabra."
            }
        }
    }

    private fun predecirPalabras(palabra: String) {
        val url = "http://10.0.2.2:8080/GitHub/Segundo/accesodatos/Greenyellow/backend.php"
        val queue = Volley.newRequestQueue(this)

        // Crear JSON de manera correcta
        val jsonObject = JSONObject()
        jsonObject.put("accion", "predecir")
        jsonObject.put("previas", palabra)

        // Mostrar la barra de carga y deshabilitar el botón
        progressBar.visibility = View.VISIBLE
        botonPredecir.isEnabled = false

        val jsonRequest = JsonObjectRequest(
            Request.Method.POST, url, jsonObject,
            { response ->
                progressBar.visibility = View.GONE
                botonPredecir.isEnabled = true

                val palabrasPredichas = response.optJSONArray("predicciones")
                if (palabrasPredichas != null && palabrasPredichas.length() > 0) {
                    predicciones.text = "Predicciones: " + (0 until palabrasPredichas.length()).joinToString(", ") { i ->
                        palabrasPredichas.getString(i)
                    }
                } else {
                    predicciones.text = "No se encontraron predicciones."
                }
            },
            { error ->
                progressBar.visibility = View.GONE
                botonPredecir.isEnabled = true
                predicciones.text = "Error al obtener predicciones. Verifica tu conexión a Internet."
                error.printStackTrace()
            }
        )

        queue.add(jsonRequest)
    }
}
