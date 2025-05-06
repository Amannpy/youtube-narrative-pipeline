import yaml
import argparse

def list_topics():
    with open('config/topics.yaml') as f:
        topics = yaml.safe_load(f)['topics']
        for idx, topic in enumerate(topics):
            print(f"{idx + 1}. {topic['name']}")


def add_topic():
    name = input("Topic name: ")
    terms = input("Search terms (comma-separated): ").split(',')
    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")
    with open('config/topics.yaml') as f:
        data = yaml.safe_load(f)
    data['topics'].append({
        'name': name,
        'search_terms': [term.strip() for term in terms],
        'date_range': {
            'start': start,
            'end': end
        }
    })
    with open('config/topics.yaml', 'w') as f:
        yaml.dump(data, f)
    print("Topic added successfully.")

def main():
    parser = argparse.ArgumentParser(description='YouTube Narrative Pipeline CLI')
    parser.add_argument('--list', action='store_true', help='List all topics')
    parser.add_argument('--add', action='store_true', help='Add a new topic')
    args = parser.parse_args()
    if args.list:
        list_topics()
    elif args.add:
        add_topic()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
# cli.py