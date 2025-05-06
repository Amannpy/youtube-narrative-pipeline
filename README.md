# YouTube Narrative Analysis Pipeline

## Usage

1. **List topics:**  
   `python cli.py --list`

2. **Add a topic:**  
   `python cli.py --add`

3. **Run the full pipeline:**  
   `python main.py`

4. **View results:**  
   `streamlit run visualization/web_dashboard.py`

## Configuration

- Add or edit topics in `config/topics.yaml`
- Set filters in `config/filters.yaml`
- Specify channels in `config/channels.yaml`

## Customization

- Add more analysis modules in `analysis/`
- Extend visualization in `visualization/web_dashboard.py`

## Automation

- Configure GitHub Actions in `.github/workflows/pipeline.yaml`
