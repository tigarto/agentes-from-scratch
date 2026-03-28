# Diario del Proyecto — Agentes de IA desde Cero

Bitácora de sesiones de trabajo. Registra qué se hizo, qué cambió en el contexto y dónde se dejó cada sesión.

---

## Sesión de trabajo 1 — 2026-03-28

### Contexto inicial
- Repo recién creado con un `README.md` vacío.
- Sin estructura de curso, sin código, sin dependencias.

### Lo que se hizo

1. **Creación del cronograma** (`CLAUDE.md`)
   - 15 sesiones, 3 módulos, metodología learning by doing.
   - Módulo 1: Fundamentos (S1–S5), Módulo 2: Construyendo Agentes (S6–S10), Módulo 3: Avanzado (S11–S15).

2. **Sesión 1 del curso completada** — ¿Qué es un Agente de IA?
   - Contenido: chatbot vs agente, 4 componentes, loop agéntico, pseudocódigo.
   - Diagramas Mermaid generados.
   - Test aplicado: **4.5/5** (punto débil: rol exacto de la memoria).
   - Archivo: `curso-agentes/sesion-01.md`

3. **Sesión 2 del curso iniciada** — Entorno de desarrollo
   - Contenido multi-proveedor: Claude, OpenAI, Gemini, DeepSeek, Groq.
   - Script de prueba: `codigo/sesion-02/test_conexion.py`
   - Archivo: `curso-agentes/sesion-02.md`

4. **Problemas encontrados con Gemini**

   | Intento | Error | Causa | Estado |
   |---|---|---|---|
   | Key de Google Cloud (2018) | 403 PERMISSION_DENIED | API no habilitada en el proyecto | Descartada |
   | Key de AI Studio | 429 RESOURCE_EXHAUSTED (`limit: 0`) | Free tier agotado o no disponible | Pendiente reset (7AM COL) |
   | Modelo `gemini-1.5-flash` | 404 NOT_FOUND | Modelo no disponible en v1beta con esa key | Descartado |

5. **Cambio de SDK de Gemini**
   - `google-generativeai` → **`google.genai`** (el anterior está deprecado).
   - Script y `sesion-02.md` actualizados.

6. **Infraestructura del repo**
   - `.gitignore` creado con `.env` excluido.
   - `curso-agentes/progreso.md` como tabla de seguimiento del curso.

### Estado al cerrar
- Sesión 1 del curso: ✅ completada
- Sesión 2 del curso: 🔄 en curso — falta ejecutar `test_conexion.py` con éxito
- Pendiente para la próxima sesión de trabajo:
  - [ ] Probar Gemini a las 7AM (reset cuota) **o** crear key en Groq
  - [ ] Marcar Sesión 2 como completada en `progreso.md`
  - [ ] Continuar con Sesión 3: primer agente real con LLM

### Commits de esta sesión
```
9f45b21 Add .gitignore and update progreso sesion-02
f2b02b8 Fix sesion-02: migrate Gemini SDK to google-genai, add 429 error note
773a40d Add sesion-02: entorno de desarrollo (multi-proveedor)
2126d88 Update progreso: sesion-01 completada (4.5/5)
82b6516 Add sesion-01 content and update CLAUDE.md with full course schedule
e9257bd Add CLAUDE.md: cronograma curso agentes IA
```

---

<!-- PLANTILLA PARA PRÓXIMAS SESIONES

## Sesión de trabajo N — YYYY-MM-DD

### Contexto al iniciar
(Copiar "Estado al cerrar" de la sesión anterior)

### Lo que se hizo
1. ...

### Problemas encontrados
| Problema | Causa | Solución |
|---|---|---|

### Estado al cerrar
- ...
- Pendiente:
  - [ ] ...

### Commits de esta sesión
```
hash mensaje
```
-->
