# Clash Royale Deck Maker

A Python application that finds competitive Clash Royale decks based on your card collection and minimum card level.

The application retrieves decks from top players in Path of Legend, compares them against your own cards and filters out any decks containing cards below your specified level. This helps you find competitive decks that you can actually use with your current collection.

## Features

- **Competitive decks:** Retrieves current decks used by top Path of Legend players.
- **Card collection analysis:** Fetches your card collection directly from the Clash Royale API.
- **Minimum level filtering:** Only displays decks where all 8 cards meet your specified minimum level.
- **Deck caching:** Stores retrieved decks locally in `cache.json` to avoid unnecessary API requests.
- **Cache synchronization:** Allows you to refresh the locally stored decks whenever you want.
- **Concurrent requests:** Uses `ThreadPoolExecutor` to retrieve player information concurrently, reducing waiting time.

## Requirements

- Python 3.10+
- A Clash Royale API token.
- The following Python packages:
  - `requests`
  - `python-dotenv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

2. Install the dependencies:

   ```bash
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the project root and add your Clash Royale API token:

   ```env
   TOKEN=your_api_token
   ```

   You can obtain an API token from the [Clash Royale Developer Portal](https://developer.clashroyale.com/).

## Usage

The application runs from the command line and requires two main arguments:

| Argument | Short | Description |
|---|---|---|
| `--level` | `-l` | Minimum required card level. |
| `--id` | | Your Clash Royale player tag. |
| `--test` | `-t` | Uses a predefined player tag for testing. |
| `--sync` | `-s` | Fetches new competitive decks and updates the local cache. |

### Examples

**Find decks using your player tag:**

```bash
python main.py --id "#YOURTAG" --level 14
```

**Use the predefined test account:**

```bash
python main.py --test --level 14
```

**Refresh the cached decks:**

```bash
python main.py --id "#YOURTAG" --level 14 --sync
```

**Use a different minimum card level:**

```bash
python main.py --test --level 12
```

## How It Works

1. **Player information:** Retrieves your card collection through the Clash Royale API.
2. **Competitive deck retrieval:** Fetches the global Path of Legend leaderboard and retrieves the current decks of its players.
3. **Deck processing:** Extracts card names from the retrieved decks and stores them locally.
4. **Caching:** Saves the decks in `cache.json` to avoid fetching them again on every execution.
5. **Level filtering:** Checks whether you own every card in each deck and whether all cards meet the minimum level requirement.
6. **Results:** Displays all decks that satisfy the specified requirements.

## Project Structure

```text
.
├── main.py          # Application entry point and CLI arguments
├── api.py           # Clash Royale API requests
├── utils.py         # Deck processing and filtering functions
├── .env             # API token (not included in Git)
├── cache.json       # Locally cached competitive decks
└── README.md
```

## Dependencies

| Package | Purpose |
|---|---|
| `requests` | HTTP requests to the Clash Royale API |
| `python-dotenv` | Loads API credentials from the `.env` file |
| `argparse` | Command-line argument parsing |
| `concurrent.futures` | Concurrent API requests |
| `json` | Local deck caching |
 
## Notes

- Card levels are normalized to account for different maximum levels across card types.
- A deck is only considered valid if you own all 8 cards and every card meets the minimum level.
- Cached decks are reused until `--sync` is specified.
- An active internet connection and a valid Clash Royale API token are required.

## Disclaimer

This project is an independent fan-made application and is not affiliated with, endorsed by, or sponsored by Supercell.

Clash Royale and its associated assets are trademarks of Supercell.

---

**Built with Python and the Clash Royale API.**
