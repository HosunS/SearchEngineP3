(:Summary: Preferences for [[PmWiki/access keys]] and edit form:)
Preferences for [[PmWiki/access keys]] and edit form

This page can be used as template for (personal) preferences, or set as default site preference (see below).

->[@
  # Access keys - hold Alt (Windows IE), Shift + Alt (Firefox)
  # or Control (Mac) and tap the indicated key on your keyboard
  # to trigger the corresponding action.
#  'ak_view'          => '' ,         # view page
  'ak_edit'          => 'e',         # edit page
  'ak_history'       => 'h',         # page history
#  'ak_print'         => '',          # print view of page
  'ak_recentchanges' => 'c',         # Recent Changes
  'ak_save'          => 's',         # save page
  'ak_saveedit'      => 'u',         # save and keep editing
  'ak_savedraft'     => 'd',         # save as draft
  'ak_preview'       => 'p',         # preview page
  'ak_textedit'      => ','          # focus to edit textarea (at the end)
  'ak_em'            => 'i',         # emphasized text (italic)
  'ak_strong'        => 'b',         # strong text (bold)

#  'ak_attach'        => '',          # attach a file
#  'ak_backlinks'     => '',          # show backlinks
#  'ak_logout'        => '',          # log out

  # Editing components
  'e_rows' => '20',                  # rows in edit textarea
  'e_cols' => '70',                  # columns in edit textarea
  'Site.EditForm' => 'Site.EditForm' # location of EditForm
  @]

To create personal user (browser) preferences,
* make a copy of [[{$FullName}?action=source | this page]] somewhere, preferably as @@Profiles.''%green%insert_your_name_here%%''-Preferences@@
* edit that page with your new preferred settings,
* select [[{$FullName}?setprefs={$FullName} | Set Preferences of this Page]] on the page containing your newly created settings. 
-> This sets a preference cookie on your browser which tells PmWiki where to find your personal preference settings.

To revert to the PmWiki default preferences
* select [[{$Name}?setprefs=| Revert to PmWiki Default Preferences]] to unset the preference cookie

See also [[Cookbook:UserConfigurations]] about how to customise the edit form for personal use.


Note that by default, parsing of {$FullName} is disabled. To make it the default site preference, add
 XLPage('prefs', "Site.Preferences");
to a config file (e.g. local/config.php).

To disable user preferences entirely set $EnablePrefs = 0;