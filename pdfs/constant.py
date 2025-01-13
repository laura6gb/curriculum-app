import pandas as pd

edu = [
    ["Ciencias de la Computación", "2023", "Universidad Nacional de Colombia", "4.5"],
    [
        "Análisis y Desarrollo de Software",
        "2023",
        "Servicio Nacional de Aprendizaje (SENA)",
        "5",
    ],
]

info = {
    "name": "Laura Galvis",
    "Brief": "Profesional en formación con experiencia en programación y desarrollo de software, especializada en Python, Java, MySQL, y desarrollo web. Busco aplicar mis conocimientos en un entorno colaborativo que me permita recibir retroalimentación constructiva para fortalecer mis habilidades. Cuento con un perfil integral, manejando herramientas ofimáticas y de diseño, además de tener habilidades como excelente redacción, ortografía, y un nivel intermedio-avanzado de inglés. Estoy comprometida con el aprendizaje constante y la mejora continua.",
    "Mobile": "313********",
    "Email": "laura66gb@gmail.com",
    "City": "Manizales, Caldas",
    "edu": pd.DataFrame(edu, columns=["Profesión", "Año", "Institución", "GPA"]),
    "skills": [
        "HTML",
        "CSS",
        "React",
        "Python",
        "Java",
        "SQL",
        "UML",
        "Documentación",
        "Ofimática",
        "Testing",
    ],
    "achievements": [
        "Distinción por “Puntaje sobresaliente en el Examen de Admisión”: Séptimo mejor puntaje Universidad Nacional de Colombia, Sede Manizales.",
        "Reconocimiento por Rendimiento Académico: Clasificada entre los 15 mejores estudiantes en el pregrado de Ciencias de la Computación.",
    ],
}

skill_col_size = 5
