"""
Flask Internship Application
A simple Flask application to demonstrate deployment capabilities.
"""

from flask import Flask, jsonify
import os

# Application Factory
def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Configuration
    app.config['DEBUG'] = os.environ.get('DEBUG', False)
    
    # Register routes
    register_routes(app)
    
    return app

def register_routes(app):
    """Register application routes."""
    
    @app.route('/')
    def home():
        """Home endpoint."""
        return jsonify({
            'status': 'success',
            'message': 'Welcome! My Flask Internship Project is Live.',
            'version': '1.0.0'
        })
    
    @app.route('/health')
    def health():
        """Health check endpoint."""
        return jsonify({'status': 'healthy'})

# Create application instance
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)