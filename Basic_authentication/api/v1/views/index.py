from flask import Blueprint, jsonify

# Creamos el Blueprint para app_views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Devuelve el estado de la API.
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    Devuelve estadísticas básicas de la API (ejemplo: número de usuarios).
    """
    # Si tienes modelos, puedes contar cuántos objetos hay y devolver ese número
    from models.user import User
    stats = {
        "users": User.count()  # Asegúrate de tener un método count en el modelo User
    }
    return jsonify(stats)
