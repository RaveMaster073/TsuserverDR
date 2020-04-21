## TsuserverDR 3
### 180801 (3.0.1)
* Added /time12

### 180812 (3.1)
* Added /ddroll, /ddrollp for rolls with modifiers
* Added 'rp_getarea(s)' attributes to restrict /getarea(s)
* Added /toggle_rpgetarea(s) to change the above attribute
* Added /st for staff-only chat
* /g now includes OOC usernames as opposed to charname

### 180910 (3.2)
* Added reachable areas support with
  - /unilock
  - /bilock
  - /delete_areareachlock
  - /restore_areareachlock
* Added proper support for spectators (can talk OOC/use commands/change music&areas/use judge buttons now)
* Added support for IC locking with /iclock
* OOC usernames may no longer include the hostname or global message prefixe
* Fixed /kick crash on unrecognized parameters

### 190126 (3.3)
* Added AFK kicks
* Added user-initiated timers with
  - /timer start
  - /timer get
  - /timer cancel
* Area lists now only list reachable areas

### 190225 (3.4)
* Added inter-area OOC communication with /scream
* Added debugging tool /exec
* Added inter-area music setting with /rplay
* Renamed /ddroll -> /roll, /ddrollp -> /rollp

### 190323 (3.5)
* Added sneak support with /sneak and /reveal
* Added inter-area IC announcements with /globalic, /unglobalic
* Added server custom shownames with /shownames
* Added soundproof area attribute
* Expanded inter-area OOC communication with /knock

### 190519 (3.6)
* Added support for custom music lists with /music_list
* Added area list reloading with /area_list
* Added character restriction on a per-area basis with /char_restrict
* Added scream ranges on a per-area basis (deprecating soundproof attribute)
* Default server configuration now uses DRO standards

### 190602 (3.7)
* Added automatic passing messages with /autopass
* Added passage lock transientness with /transient
* Added showname moderation tools
  - /showname_freeze
  - /showname_history
  - /showname_list
  - /showname_nuke
  - /showname_set
* Enforced showname uniqueness per area
* Fixed /area_kick crash on unrecognized parameters
* Fixed /getareas listing an empty area if only people there are sneaking
* Players on server select no longer count in online playercount, nor in /getarea[s] and /area

### 190609 (3.8)
* Added movement handicaps with /handicap, /unhandicap
* Added area lights with /lights
* Added blood trails with
  - /bloodtrail
  - /bloodtrail_clean
  - /bloodtrail_list
  - /bloodtrail_set
* Added /toggle_shownames to disable receiving server shownames
* Allowed for more DRO client effects being used
* Fixed /autopass not sending messages from or for staff

### 190618 (first with date version system) (3.9)
* Added area descriptions with /look, /look_set
* Console now displays server opening/closing/reconnecting messages.
* Python errors now show additional debugging info on server log+client if error came as a result of command
* Renamed some commands
  - allow_iniswap -> /can_iniswap
  - delete_areareachlock -> /passage_clear
  - restore_areareachlock -> /passage_restore
  - toggle_areareachlock -> /can_passagelock
  - toggleglobal -> /toggle_global
  - toggle_rollp -> /can_rollp
  - toggle_rpgetarea -> /can_rpgetarea
  - toggle_rpgetareas -> /can_rpgetareas
* Reworked /area_kick so that it now allows area names as parameter
* Reworked /discord so that it now shows the server's Discord server invite link
* Fixed /autopass sending old character name in case of forced char switch on area change
* Fixed /bloodtrail_set not enforcing staff member rank
* Fixed /disemconsonant and /remove_h not working/crashing
* Fixed /follow allowing to follow yourself
* Fixed "Knock" client effect not being sent

### 190630 (3.10)
* Added support for user initiated day cycles with 
  - /clock
  - /clock_cancel
  - /clock_pause
  - /clock_unpause
* Added various moderation tools
  - /judgelog
  - /shoutlog
  - /version
  - /whereis
* Added 'has_lights' parameters to areas to allow/disallow using /lights
* Enforced different staff passwords on server configuration
* Shouts now show character used as opposed to OOC name
* Turning lights on reveals who is bleeding and not sneaking
* Fixed area lists allowing for empty parameters
* Fixed blood announcements sent to wrong areas occasionally
* Fixed /kick requiring no arguments
* Fixed music flood guard crash
* Fixed server ghosting on master server list on incorrect server closing
* Fixed pre2.2.5 clients being unable to join

### 190708 (3.11)
* Added various moderation/debugging tools
  - /lasterror
  - /multiclients
  - /whois
* Added area parameters to allow for non-staff use of custom backgrounds/music
* Added /toggle_allrolls so staff get roll notifications from other areas
* Day cycle notifications now send 'CL' packets to clients
* GMs can no longer /area_kick users from lobby areas
* Renamed timer commands
  - /timer start -> /timer
  - /timer get -> /timer_get
  - /timer cancel -> /timer_cancel
* Fixed a player not unfollowing a player who disconnects and then crashing on area change
* Fixed /roll crashing on too many arguments

### 190721 (3.12)
* Added global IC prefixes with /globalic_pre
* Added first person mode with /toggle_fp
* Banned players now receive 'You are banned from this server' notifications on attempting to join+Notifies mods of this attempt
* Global IC messages now send notifications on each use
* Made daily gmpasses optional
* Multiple players may now follow the same player
* Renamed some commands from /toggle to /can
* Fixed clients being able to join too quickly on server select and crashing

## TsuserverDR 4.0 (The Party Update)

### 190801 (4.0)
* Added party support so players move with one another automatically with
  - /party
  - /party_disband
  - /party_id
  - /party_invite
  - /party_join
  - /party_kick
  - /party_lead
  - /party_list
  - /party_members
  - /party_uninvite
  - /party_unlead
* Added HDID bans with /banhdid, /unbanhdid
* CMs now get IPIDs in /getarea(s), /showname_list and /whois, as well as HDID in /whois
* Iniswapped folders are now shown with /whois
* Fixed security issue with webAO
* TsuserverDR now uses semantic versioning.

### 190801b (4.0.1)
* Introduced CI testing on Travis

### 190802 (4.0.2-4.0.3)
* Fixed server player limit not being enforced

### 190805 (4.0.4)
* Fixed invalid characters crash with /area_list and /music_list

### 190806 (4.0.5)
* Fixed logging in to a second rank making you keep the first one

## TsuserverDR 4.1 (The Sense Block Update)

### 190819 (4.1)
* Added sense block support with
  - /blind
  - /deaf
  - /gag
* Added /bloodtrail_smear to smear blood trails in the area
  - If player is blind or area lights are out, /bloodtrail_clean effectively runs this instead
* Added /ping to check for lost connection
* Added /showname_area to list shownames just in the current area
* CMs now receive Call Mod notifications
* Renamed /mutepm -> /toggle_pm, /showname_list -> /showname_areas
* Started including additional marks to certain staff privileged RP notifications
* Minor changes to messages sent on area change
  - Staff now receive autopass messages if lights are off instead of regular lights off messages
  - Reworded messages sent if someone arrives/leaves while bleeding/lights off and sneaking
  - Players now receive special notification if there is blood in the area and lights are off
* Fixed global IC OOC notifications showing message went one area past the last area actually sent to
* Fixed IPIDs on rare occasions being non-trivially not unique
* Fixed /pm not sending complete character names to recipient
* Minor bugfixes with respect to bleeding
  - Blood cleaning notifications will no longer be sent with lights off
  - Blood will now automatically be spilled on the area as soon as /bloodtrail is executed, not only on area change
 
### 190820 (4.1.1)
* Added special marks to more staff privileged RP notifications
* Reworded global IC notification messages

### 190822 (4.1.2)
* Added more special marks to more staff privileged RP notifications
* Normal players now get who cleaned/smeared blood in area if they are not blind and the lights are on

### 190903 (4.1.3)
* Renamed repository to TsuserverDR
* Added more special marks to more staff only RP notifications
* Fixed /multiclients failing for GMs/CMs on non-staff targets while in RP mode

### 190904 (4.1.4)
* Gagged messages are now randomly generated 
* Staff get new messages when using /bloodtrail, with privilege marks added where needed

## TsuserverDR 4.2 (The DRO 2nd Anniversary Update/The Zone and Poison Update)

### 191031 (4.2)
* Added zones. Zones are groups of areas such that any privileged server notifications that come from a player action within the zone will be sent only to "watchers", who are people who watch the zone. They come with the following commands:
  - /zone
  - /zone_add
  - /zone_delete
  - /zone_global (alias /zg)
  - /zone_list
  - /zone_play
  - /zone_remove
  - /zone_unwatch
  - /zone_watch
* Zones will send notifications to all zone watchers for standard RP notifications as well as the following:
  - Players coming IN and OUT of the zone (with their shownames)
  - Players coming in a zone while having other clients open in the zone
  - Players in the zone disconnecting
  - Players in the zone changing character
  - Players in the zone changing showname
* Added poison through /poison. Poisoned targets will be inflicted an assortment of effects at the end of a timer (currently a selection of blindness, deafness and gagged). Targets can have their poison removed before it affects them by having /cure run on them
  - /cure will also remove effects if they have been already applied
* Improved password-less process of GM logins:
  - Added /make_gm so CMs and mods can log in other players as GMs
  - Added /gmself so GMs can log in all other clients they opened as GMs
* Custom shownames now appear if set in server notifications instead of character folders
* Improved /help
  - It can now take a command name and it will show a brief description and expected syntax, as well as the minimum required rank if the player is not authorized to use it
* Improved roll management mechanics
  - Added dice log commands to retrieve roll history through /dicelog (for one player) and /dicelog_area (for one area)
  - Roll options are now modifiable from server configurations
* Improved information sent to moderators on mod actions
  - /ban, /banhdid and /kick notifications are now sent to all mods and CMs in the server, as well as appropiate information on the targets.
* Reworded notifications for the following mechanics
  - Rolls failing
  - Enabling/disabling IC locks
  - Setting your own showname, or someone else's showname
  - Characters becoming restricted in an area
  - Revoking/restoring DJ permissions
* The following actions now send an IC message in conjunction with an OOC notification:
  - /knock (which has been restricted to non-lobby areas only)
  - /scream
* Private servers will now include the masterserver name when showing the server IP in the terminal
* Fixed clients with same HDID but different IPID not being recognized as multiclients. This fixes the following: 
  - Players getting a new IP can now kick ghosting clients under their old IP with /kickself
  - Staff can now recognize such situations with /whois or /multiclients
* Fixed /play and /rplay not looping music tracks that appear in the server music list
* Fixed daily GM passwords switching at 3 pm incorrectly, they now switch correctly and at midnight
* Fixed day cycles not canceling on area list reload
* Fixed single space messages sent by gagged players not blankposting but being converted to jumbled text
* Fixed GMs receiving IPID information through /multiclients
* Explicitly allowed Python 3.8 support for server owners

### 191031b (4.2.0-post1)
* Fixed uncaught ValueError if server files do not contain a valid README.md when attempting to generate help text for commands
* Fixed zones being able to obtain duplicate zone ID values

### 191109a (4.2.0-post2)
* Fixed /multiclients not considering same HDID users as multiclients
* Fixed /unban considering the unbanning of an already unbanned person as an invalid IPID
* Reorganized /ban and /unban text to include backticks surrounding argument
* Made /unban notify all other mods and CMs in the server whenever executed
* Fixed /narrate crashing on use
* Fixed changelog listing incorrect dates for 4.2.0 releases

### 191122a (4.2.0-post3)
* Fixed /zone_watch and /zone_delete raising an uncaught KeyError if an invalid zone name was passed as an argument
* Fixed rare issue with new AWS instances raising a certificate error when pinging api.ipify.org on server boot-up
* Made unrecoverable server errors expect an operator Enter input on console before finishing the program so that they can see the error message if they launched the server by double-clicking `start_server.py`
* Made error log files be created if the server crashes on bootup, which would normally happen if some files are missing or have some parsing errors
* Fixed master server connection not being closed automatically on server shutdown, which displayed ignored exception messages if running Python 3.8

### 191209a (4.2.1)
* Added deprecation warnings to the following commands
  - **allow_iniswap**: Same as /can_iniswap.
  - **delete_areareachlock**: Same as /passage_clear.
  - **mutepm**: Same as /toggle_pm.
  - **restore_areareachlock**: Same as /passage_restore.
  - **showname_list**: Same as /showname_areas.
  - **toggleglobal**: Same as /toggle_global.
  - **toggle_areareachlock**: Same as /can_passagelock.
  - **toggle_rollp**: Same as /can_rollp.
  - **toggle_rpgetarea**: Same as /can_rpgetarea.
  - **toggle_rpgetareas**: Same as /can_rpgetareas.
* Added /files and /files_set for custom file linking
* Added logging messages to the server logs when the server starts up, shuts down, or it crashes and the server can manage to save the log
* Server logs files are now separated by month. Logging information will go to the file associated with the month and year the server was last launched on (so if in one session the server was launched December 2019 and was shut down January 2020, all logs for that session would go in `logs/server-2019-12.log`). 
  - `logs/server.log` will now go unused, but server owners may keep this file for their archives.
* Improved cross-compatibility between multiple AO-like clients. For client-exclusive features, a best-effort-like approach will be taken to adapt to clients that do not have said features. 
* Improved /help message so that it suggests to use the extended syntax (/help "command name") to get help with a particular command
* Improved README.md instructions so that server installation steps are more clear
* Fixed minor typos in `config_sample/config.yaml`
* Fixed /area_kick'ing someone off a locked area under special circumstances allowing the target to rejoin the locked area
* Fixed /help not showing extended syntax (/help "command name") when running /help help
* Fixed /narrate messages being replaced for deafened players
* Fixed /poison effects kicking in being notified to all players in the server as opposed to zone watchers or staff members if target is in an area not in a zone

### 191224a (4.2.2)
* Added /whisper for IC private communications between players (meant to be used for RPs, as staff members can read the contents of the message)
* Added /guide for providing personalized guidance specific to a particular player
* Made /invite be a public command as opposed to GM+
* Added helpful commands-to-run-next suggestions for the following actions
  - Setting files.
  - Setting up global IC messages
  - Creating/being invited to a party.
  - Entering a zone you that a GM+ is not watching/leaving a zone a GM+ is watching.
  - Logging in in an area part of a zone.
  - Being in an area when a zone is created involving that area, or that area is added to a zone.
  - Being in an area that is removed from the player's zone.
* The following commands can now take character name, edited-to character, showname or OOC name as identifiers, provided the target is in the same area
  - /files
  - /guide
  - /invite
  - /party_invite
  - /party_kick
  - /party_uninvite
  - /pm
  - /uninvite
  - /whisper
* Fixed normal players being able to use /uninvite with IPID.

### 191231a (4.2.3)
* Added /toggle_allpasses to be able to receive autopass notifications from players that do not have autopass on
* Added optional argument to /coinflip to call coin flip results
* Added optional argument to /8ball to directly ask questions to the magic 8 ball
* Added optional argument to /getarea and /showname_area to obtain details from a particular area
* Added source and destination areas to zone entry/exit notification sent to watchers when a player enters/leaves a zone
* Added anti-bullet tag as an area parameter
* Allowed /whois to take HDID as an identifier (CM and mod only)
* Removed leftover ability of GMs to use commands with IPID
* Reworked responses of the magic 8 ball so it now chooses from a pool of 25 answers as opposed to 8
* Fixed documentation of /unban not listing it can unban by IP address
* Fixed GMs not receiving privileged staff notifications for autopass when players leave/enter an area whose lights are off or they enter/leave an area while sneaking
* Fixed unsupported webAO clients lingering for too long and taking server spots away
* Fixed wrong messages being sent when a client is bleeding and they are sneaking or the area lights are out

### 191231b (4.2.3-post1)
* Fixed non-numerical HDIDs not being recognized with /whois

### 200110a (4.2.3-post2)
* Fixed players in first person mode being unable to talk after a server-initiated IC message

### 200112a (4.2.3-post3)
* Aligned wording of music list loading outputs with the ones from area list loading outputs
* Fixed players/server being able to load music lists with invalid syntax. An informative error message will be returned to assist in fixing the music list

### 200112b (4.2.3-post4)
* Fixed players/server being able to load any YAML files with invalid YAML syntax. An informative error message will be returned to assist in fixing said file

### 200201a (4.2.3-post5)
* Fixed /showname_freeze and /showname_nuke causing errors when notifying other users

### 200320a (4.2.3-post6)
* Fixed /bg turning on lights in previously dark rooms.

### 200327a (4.2.3-post7)
* Fixed players/server being able to load music lists with non-numerical track lengths. An informative error message will be returned to assist in fixing the music list
* Fixed duplicate /look_set output messages being sent to other zone watchers in the same area
* Fixed typo in /passage_restore: 'statue'->'state'

### 200410a (4.2.3-post8)
* Fixed clients who do not/cannot update their music list crashing when they attempt to join an area that no longer exists.
* Readded description of /login to README.md

### (4.2.4)
* Added /cid to get your (or other's) client ID.
* Added /spectate to switch to spectator
* Added /time_est
* Added server configuration setting to disable ms2-prober connections being logged in server logs
* Added client version to /whois
* Warnings are now sent to players in once-locked rooms that were reloaded via /area_list
* /whisper messages from private rooms are no longer sent to staff members
* GMs may now /make_gm their multiclients, and their multiclients only
* Login/logout notifications are now sent to other staff members
* Staff login+passwords messages are now censored both in IC and OOC
* Added /zone_lights to turn the lights of every area in your zone on or off
* Added:
  - /sa (Alias for /showname_area)
  - /sas (Alias for /showname_areas)
  - /shout (Alias for /scream)
  - /unsneak (Alias for /reveal)
  - /yell (Alias for /scream)
* Added best effort support for Attorney Online 2.7