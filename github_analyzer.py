import requests

class GitHubUser:
    def __init__(self, username):
        self.username = username
        self.user_data = self.fetch_user_data()

    def fetch_user_data(self):
        url = f'https://api.github.com/users/{{self.username}}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('User not found')

    def analyze_user(self):
        if not self.user_data:
            print("No user data available.")
            return
        print(f"User: {{self.user_data['login']}}")
        print(f"Public Repos: {{self.user_data['public_repos']}}")
        print(f"Followers: {{self.user_data['followers']}}")
        print(f"Following: {{self.user_data['following']}}")
        print(f"Bio: {{self.user_data.get('bio', 'No bio available')}}")
        
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    user = GitHubUser(username)
    user.analyze_user()