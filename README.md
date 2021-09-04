This is a collection of bot account names. NamelistMASTER contains all the names we recommend you ban in your channel

Sometimes people get on that list by accident, in that case they will be removed from the namelist and put into the False-positive list so you can unban them.

I've created a "How to" Video on the FileDifference and how to use the files you can view here: https://twitter.com/hackbolt_/status/1430649215785517057?s=20

### Text-based, Non-technical Instructions

1. Get a copy of this repository on your computer. To get a copy of the program and the lists, click on the Code button and click Download ZIP (or follow this [direct link to the archive](https://github.com/hackbolt/twitchbotsnbigots/archive/refs/heads/main.zip)). Code savvy folks can also choose to use Github and checkout the repository for easier updates in the future.
2. If you've downloaded the ZIP file, unzip it to its own folder. This can be done through any archive utility, including the one baked into Windows. 
  - To use the Windows ZIP utility, navigate to the ZIP file and open it. If you have no other programs to handle ZIP, it should open in the same window as if it were a folder. From here, click the `Extract Compressed Folder Tools` button in the top section of the folder window. This will expand a menu with an extract all button, click it now.
  - Follow the prompts here to extract the contents to a folder. It is recommended to put the contents in a new folder for easier cleanup and finding of the files. 
3. Once in the folder, you should see a couple of text (.txt) files. These are lists of known bots/hate raiders submitted by the community, and a small list of False-Positives that can be used to reverse bans on verified users that were falsely submitted. There will also be a folder called FileDifference which contains the program used to compare ban lists to reduce potential duplicate bans. If you have run this before, copy whatever was in your new_list.txt into the old_list.txt, and erase the contents of new_list.txt and save. This allows the script to give you a smaller set of names to ban, and thus take less time.
4. Open the namelistMASTER.txt and copy all of the text. This will be pasted into the new_list.txt file under the FileDifference folder.
5. Repeat the preceeding step for each of the patches of additional user lists (e.g. 8-31 adds.txt).
6. If you have used this ban list before, run the FileDifferences.exe (or see the [Mac/Linux instructions](#mac-linux-instructions) for this step). This will give you a list of users under !added_names.txt to use in CommanderRoot.
7. Once you have your list (either in !added_names.txt or new_list.txt if this is your first run), open a Web browser and go to the CommanderRoot website (currently https://twitch-tools.rootonline.de/) and open the Blocklist Manager. There will be a button if this is your first visit to this page to Login via Twitch. This allows the CommanderRoot site to add blocked users for you.
8. Using the blocklist manager, click the `Add new blocks` button and a new larger text area should appear. Paste your full list of bot users into this textarea and click `Apply filter`.
9. New text should now appear on the page indicating how many users are left to block from the list. This runs in your browser, so you will need to keep your page open (even if its just in the background) to continue adding the bots.

Mac/Linux Instructions
1. Open the FileDifferences folder in a Terminal window, and run `py ./Difference.py`
