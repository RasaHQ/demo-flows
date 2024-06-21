# Rasa CALM Demo

This demo showcases a chatbot built with Rasa's LLM-native approach: [CALM](https://rasa.com/docs/rasa-pro/calm). 

> [!CAUTION]
> Please note that the demo bot is an evolving platform. The flows currently 
> implemented in the demo bot are designed to showcase different features and 
> capabilities of the CALM bot. The functionality of each flow may vary, reflecting 
> CALM's current stage of development.

## Terms of Use

This project is released under the Rasa's [Early Release Software Access Terms](https://rasa.com/early-release-software-terms/). 

## Demo Bot

The demo bot's business logic is implemented as a set of [flows](https://rasa.com/docs/rasa-pro/concepts/flows), [rules](https://rasa.com/docs/rasa/rules), and [stories](https://rasa.com/docs/rasa/stories), 
which are organized into three main skill groups: Contacts, Transactions, 
and Others/Misc.

The skill groups `Contacts` and `Transactions` are implemented using CALM, e.g. are defined in flows.
The skill group `Others/Misc` is implemented via the [nlu-based approach](https://rasa.com/docs/rasa/training-data-format).
[Coexistence](https://rasa.com/docs/rasa-pro/building-assistants/coexistence) allows you to run a single assistant that uses both the Conversational AI with Language Models (CALM) 
approach and an NLU-based system in parallel.

Each flow consists of a `yaml` file and a [domain definition](https://rasa.com/docs/rasa-pro/concepts/domain), 
which includes [actions](https://rasa.com/docs/rasa-pro/concepts/domain#actions), 
[slots](https://rasa.com/docs/rasa-pro/concepts/domain#slots), and 
[bot ressponses](https://rasa.com/docs/rasa-pro/concepts/domain#responses). 

The table below shows all the skills implemented in the bot:

<table border="1">
   <tr>
   <th>Skill Group</th>
   <th>Flow Name</th>
   <th>Description</th>
   <th>Link to flow</th>
   <th>Link to domain</th>
   </tr>

   <!-- Contacts -->

   <tr>
      <td rowspan="3">Contacts</td>
      <td>Add new contact</td>
      <td>Adds a new contact to the user's list.</td>
      <td><a href="data/flows/add_contact.yml">Link</a></td>
      <td><a href="domain/flows/add_contact.yml">Link</a></td>
   </tr>
   
   <tr>
      <td>Remove contact</td>
      <td>Removes selected contact from the user's list.</td>
      <td><a href="data/flows/remove_contact.yml">Link</a></td>
      <td><a href="domain/flows/remove_contact.yml">Link</a></td>
   </tr>

   <tr>
      <td>List contacts</td>
      <td>List all of user's saved contacts.</td>
      <td><a href="data/flows/list_contacts.yml">Link</a></td>
      <td><a href="domain/flows/list_contacts.yml">Link</a></td>
   </tr>


   <!-- Transactions -->

   <tr>
      <td rowspan="7">Transactions</td>
      <td>Check account balance</td>
      <td>Allows users to check their current account balance.</td>
      <td><a href="data/flows/check_balance.yml">Link</a></td>
      <td><a href="domain/flows/check_balance.yml">Link</a></td>
   </tr>

   <tr>
      <td>Transfer money</td>
      <td>Facilitates the transfer of funds to user's contacts.</td>
      <td><a href="data/flows/transfer_money.yml">Link</a></td>
      <td><a href="domain/flows/transfer_money.yml">Link</a></td>
   </tr>

   <tr>
      <td>Setup recurrent payment</td>
      <td>Sets up recurring payments which can either be a direct debit or a standing order.</td>
      <td><a href="data/flows/setup_recurrent_payment.yml">Link</a></td>
      <td><a href="domain/flows/setup_recurrent_payment.yml">Link</a></td>
   </tr>

   <tr>
      <td>List transactions</td>
      <td>List the last user's transactions.</td>
      <td><a href="data/flows/transaction_search.yml">Link</a></td>
      <td><a href="domain/flows/transaction_search.yml">Link</a></td>
   </tr>
   
   <tr>
      <td>Replace card</td>
      <td>Replace the user's card.</td>
      <td><a href="data/flows/replace_card.yml">Link</a></td>
      <td><a href="domain/flows/replace_card.yml">Link</a></td>
   </tr>

   <tr>
      <td>Replace eligible card</td>
      <td>Replace the user's card that meets specific eligibility criteria. This is a <a href="https://rasa.com/docs/rasa-pro/concepts/flows#link">flow link</a> exclusively accessed by <a href="data/flows/replace_card.yml">replace_card</a> flow</td>
      <td><a href="data/flows/replace_eligible_card.yml">Link</a></td>
      <td>N/A</td>
   </tr>

   <tr>
      <td>Verify account</td>
      <td>Verify an account for higher transfer limits.</td>
      <td><a href="data/flows/verify_account.yml">Link</a></td>
      <td><a href="domain/flows/verify_account.yml">Link</a></td>
   </tr>
  
</table>


<table border="1">
   <tr>
   <th>Skill Group</th>
   <th>Description</th>
   <th>Link to story, rules, nlu data</th>
   <th>Link to domain</th>
   </tr>
   
   <!-- Others / Misc -->
   
   <tr>
      <td rowspan="5">Others / Misc</td>
      <td>Book Restaurant</td>
      <td>Make a reservation at a restaurant.</td>
      <td><a href="data/nlu-based">Link</a></td>
      <td><a href="domain/nlu-based/restaurant.yml">Link</a></td>
   </tr>

   <tr>
      <td>Health Advice</td>
      <td>Detects an out-of-scope topic: health advice.</td>
      <td><a href="data/nlu-based">Link</a></td>
      <td><a href="domain/nlu-based/health_advice.yml">Link</a></td>
   </tr>

   <tr>
      <td>Hotel search</td>
      <td>Search for a hotel and show hotel rating.</td>
      <td><a href="data/nlu-based">Link</a></td>
      <td><a href="domain/nlu-based/hotel_search.yml">Link</a></td>
   </tr>
  
</table>

Rasa ships with a default behavior in CALM for every [conversation repair case](https://rasa.com/docs/rasa-pro/concepts/conversation-repair/#conversation-repair-cases)
which is handled through a [default pattern flow](https://rasa.com/docs/rasa-pro/concepts/conversation-repair/#conversation-repair-cases). 
In addition to its core functionality, the demo bot also includes an examples of 
pattern overriding in [`data/flows/patterns.yml`](data/flows/patterns.yml).

## Running the project

This section guides you through the steps to get your Rasa bot up and running. 
We've provided simple `make` commands for a quick setup, as well as the underlying 
Rasa commands for a deeper understanding. Follow these steps to set up the 
environment, train your bot, launch the action server, start interactive sessions, 
and run end-to-end tests.

### Installation

> [!IMPORTANT]
> To build, run, and explore the bot's features, you need Rasa Pro license. You also 
> need access to the `rasa-plus` Python package, which requires authentication with 
> our artifact repository. For detailed instructions on the authentication process,
> please refer our documentation [here](https://rasa.com/docs/rasa-pro/installation/python/installation).

> [!NOTE]
> If you want to use a different version of `rasa` or `rasa-plus`, you can 
> change the versions in the [pyproject.toml](./pyproject.toml) file.

Prerequisites:
- rasa pro license
- being authenticated with our artifact registry
- [poetry](https://python-poetry.org/docs/#installation) (1.8.2), e.g. using 
  `poetry self update`
- python (3.10.12), e.g. using [pyenv](https://github.com/pyenv/pyenv) 
  `pyenv install 3.10.12`
- set up and running [Duckling](https://github.com/facebook/duckling) server;
The easiest option is to spin up a docker container using `docker run -p 8000:8000 rasa/duckling`.
Alternatively, you can use the `make run-duckling` command locally.
This runs automatically only when you use the `make run` command, before it launches the Inspector app.

After you cloned the repository and are authenticated, follow the installation steps:

1. Locate to the cloned repo:
   ```
   cd rasa-calm-demo
   ```
2. Set the python environment with `pyenv` or any other tool that gets you the right 
   python version
   ```
   pyenv local 3.10.12
   ```
3. Install the dependencies with `poetry`
   ```
   poetry install
   ```
4. Create an environment file `.env` in the root of the project with the following 
   content:
   ```bash
   RASA_PRO_LICENSE=<your rasa pro license key>
   OPENAI_API_KEY=<your openai api key>
   RASA_DUCKLING_HTTP_URL=<url to the duckling server>
   ```

### Training the bot

To train a model use `make` command for simplicity:
```commandline
make train
```
which is a shortcut for:
```commandline
rasa train -c config.yml -d domain --data data
```

The trained model is stored in `models` directory located in the project root.

### Starting the assistant

Before interacting with your assistant, start the action server to enable the 
assistant to perform custom actions located in the `actions` directory. Start the 
action server with the `make` command:
```commandline
make actions
```
which is a shortcut for:
```commandline
rasa run actions
```

Once the action server is started, you have two options to interact with your trained
assistant:
1. **CLI-based interaction** using rasa shell:
```commandline
rasa shell
```
2. **GUI-based interaction** using rasa inspector:
```commandline
rasa inspect
```

### Running e2e test

The demo bot comes with a set of e2e tests, categorized into two primary groups: 
**failing**, and **passing**. These tests are organized not per individual flow but 
according to CALM functionalities.

> [!NOTE]
> The passing and failing statuses are relative to the performance of the GPT-4, 
> which is enabled by default. The use of different models may yield varying results. 

You have the flexibility to run either all tests, only the passing tests, only the 
failing tests, or a single specific test.

------

To run **all the tests** you can use the `make` command:
```commandline
make test
```
or
```commandline
run rasa test e2e e2e_tests
```

------

To run **passing/failing/flaky** tests you can use the `make` command:
```commandline
make test-passing
```
```commandline
make test-failing
```
```commandline
make test-flaky
```
or
```commandline
run rasa test e2e e2e_tests/passing
```
```commandline
run rasa test e2e e2e_tests/failing
```
```commandline
run rasa test e2e e2e_tests/flaky
```

------

To run a **single test** with `make` command, you need to provide the path to a 
target test in an environment variable `target`:
```commandline
export target=e2e_tests/path/to/a/target/test.yml
```
and then run:
```commandline
make test-one
```
or
```commandline
rasa test e2e e2e/tests/path/to/a/target/test.yml
```
