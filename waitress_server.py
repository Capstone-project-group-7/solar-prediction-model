from waitress import serve
import main1
serve(main1.app, host='0.0.0.0', port=8080)