var isCompatible=function(){if(navigator.appVersion.indexOf('MSIE')!==-1&&parseFloat(navigator.appVersion.split('MSIE')[1])<6){return false;}return true;};var startUp=function(){mw.config=new mw.Map(true);mw.loader.addSource({"local":{"loadScript":"/wiki/load.php","apiScript":"/wiki/api.php"}});mw.loader.register([["site","1399948175",[],"site"],["noscript","1399948175",[],"noscript"],["startup","1468510197",[],"startup"],["user","1399948175",[],"user"],["user.groups","1399948175",[],"user"],["user.options","1468510197",[],"private"],["user.cssprefs","1468510197",["mediawiki.user"],"private"],["user.tokens","1399948175",[],"private"],["filepage","1399948175",[]],["skins.chick","1399948175",[]],["skins.cologneblue","1399948175",[]],["skins.modern","1399948175",[]],["skins.monobook","1399948175",[]],["skins.nostalgia","1399948175",[]],["skins.simple","1399948175",[]],["skins.standard","1399948175",[]],["skins.vector","1399948175",[]],["jquery","1399948175",[]],["jquery.appear",
"1399948175",[]],["jquery.arrowSteps","1399948175",[]],["jquery.async","1399948175",[]],["jquery.autoEllipsis","1399948175",["jquery.highlightText"]],["jquery.byteLength","1399948175",[]],["jquery.byteLimit","1399948175",["jquery.byteLength"]],["jquery.checkboxShiftClick","1399948175",[]],["jquery.client","1399948175",[]],["jquery.collapsibleTabs","1399948175",[]],["jquery.color","1399948175",["jquery.colorUtil"]],["jquery.colorUtil","1399948175",[]],["jquery.cookie","1399948175",[]],["jquery.delayedBind","1399948175",[]],["jquery.expandableField","1399948175",["jquery.delayedBind"]],["jquery.farbtastic","1399948175",["jquery.colorUtil"]],["jquery.footHovzer","1399948175",[]],["jquery.form","1399948175",[]],["jquery.getAttrs","1399948175",[]],["jquery.highlightText","1399948175",[]],["jquery.hoverIntent","1399948175",[]],["jquery.json","1399948175",[]],["jquery.localize","1399948175",[]],["jquery.makeCollapsible","1460510328",[]],["jquery.messageBox","1399948175",[]],["jquery.mockjax",
"1399948175",[]],["jquery.mw-jump","1399948175",[]],["jquery.mwExtension","1399948175",[]],["jquery.placeholder","1399948175",[]],["jquery.qunit","1399948175",[]],["jquery.qunit.completenessTest","1399948175",["jquery.qunit"]],["jquery.spinner","1399948175",[]],["jquery.suggestions","1399948175",["jquery.autoEllipsis"]],["jquery.tabIndex","1399948175",[]],["jquery.tablesorter","1460513323",[]],["jquery.textSelection","1399948175",[]],["jquery.validate","1399948175",[]],["jquery.xmldom","1399948175",[]],["jquery.tipsy","1399948175",[]],["jquery.ui.core","1399948175",["jquery"],"jquery.ui"],["jquery.ui.widget","1399948175",[],"jquery.ui"],["jquery.ui.mouse","1399948175",["jquery.ui.widget"],"jquery.ui"],["jquery.ui.position","1399948175",[],"jquery.ui"],["jquery.ui.draggable","1399948175",["jquery.ui.core","jquery.ui.mouse","jquery.ui.widget"],"jquery.ui"],["jquery.ui.droppable","1399948175",["jquery.ui.core","jquery.ui.mouse","jquery.ui.widget","jquery.ui.draggable"],"jquery.ui"],[
"jquery.ui.resizable","1399948175",["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.selectable","1399948175",["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.sortable","1399948175",["jquery.ui.core","jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.accordion","1399948175",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.ui.autocomplete","1399948175",["jquery.ui.core","jquery.ui.widget","jquery.ui.position"],"jquery.ui"],["jquery.ui.button","1399948175",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.ui.datepicker","1399948175",["jquery.ui.core"],"jquery.ui"],["jquery.ui.dialog","1399948175",["jquery.ui.core","jquery.ui.widget","jquery.ui.button","jquery.ui.draggable","jquery.ui.mouse","jquery.ui.position","jquery.ui.resizable"],"jquery.ui"],["jquery.ui.progressbar","1399948175",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.ui.slider","1399948175",["jquery.ui.core",
"jquery.ui.widget","jquery.ui.mouse"],"jquery.ui"],["jquery.ui.tabs","1399948175",["jquery.ui.core","jquery.ui.widget"],"jquery.ui"],["jquery.effects.core","1399948175",["jquery"],"jquery.ui"],["jquery.effects.blind","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.bounce","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.clip","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.drop","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.explode","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.fade","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.fold","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.highlight","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.pulsate","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.scale","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.shake","1399948175",["jquery.effects.core"],
"jquery.ui"],["jquery.effects.slide","1399948175",["jquery.effects.core"],"jquery.ui"],["jquery.effects.transfer","1399948175",["jquery.effects.core"],"jquery.ui"],["mediawiki","1399948175",[]],["mediawiki.api","1399948175",["mediawiki.util"]],["mediawiki.api.category","1399948175",["mediawiki.api","mediawiki.Title"]],["mediawiki.api.edit","1399948175",["mediawiki.api","mediawiki.Title"]],["mediawiki.api.parse","1399948175",["mediawiki.api"]],["mediawiki.api.titleblacklist","1399948175",["mediawiki.api","mediawiki.Title"]],["mediawiki.api.watch","1399948175",["mediawiki.api","mediawiki.user"]],["mediawiki.debug","1399948175",["jquery.footHovzer"]],["mediawiki.debug.init","1399948175",["mediawiki.debug"]],["mediawiki.feedback","1399948175",["mediawiki.api.edit","mediawiki.Title","mediawiki.jqueryMsg","jquery.ui.dialog"]],["mediawiki.htmlform","1399948175",[]],["mediawiki.Title","1399948175",["mediawiki.util"]],["mediawiki.Uri","1399948175",[]],["mediawiki.user","1399948175",[
"jquery.cookie"]],["mediawiki.util","1460510156",["jquery.client","jquery.cookie","jquery.messageBox","jquery.mwExtension"]],["mediawiki.action.edit","1399948175",["jquery.textSelection","jquery.byteLimit"]],["mediawiki.action.history","1399948175",["jquery.ui.button"],"mediawiki.action.history"],["mediawiki.action.history.diff","1399948175",[],"mediawiki.action.history"],["mediawiki.action.view.dblClickEdit","1399948175",["mediawiki.util"]],["mediawiki.action.view.metadata","1460512503",[]],["mediawiki.action.view.rightClickEdit","1399948175",[]],["mediawiki.action.watch.ajax","1460511687",["mediawiki.api.watch","mediawiki.util"]],["mediawiki.language","1399948175",[]],["mediawiki.jqueryMsg","1399948175",["mediawiki.language","mediawiki.util"]],["mediawiki.libs.jpegmeta","1399948175",[]],["mediawiki.page.ready","1399948175",["jquery.checkboxShiftClick","jquery.makeCollapsible","jquery.placeholder","jquery.mw-jump","mediawiki.util"]],["mediawiki.page.startup","1399948175",[
"jquery.client","mediawiki.util"]],["mediawiki.special","1399948175",[]],["mediawiki.special.block","1399948175",["mediawiki.util"]],["mediawiki.special.changeemail","1399948175",["mediawiki.util"]],["mediawiki.special.changeslist","1399948175",["jquery.makeCollapsible"]],["mediawiki.special.movePage","1399948175",["jquery.byteLimit"]],["mediawiki.special.preferences","1399948175",[]],["mediawiki.special.recentchanges","1399948175",["mediawiki.special"]],["mediawiki.special.search","1399948175",[]],["mediawiki.special.undelete","1399948175",[]],["mediawiki.special.upload","1460514457",["mediawiki.libs.jpegmeta","mediawiki.util"]],["mediawiki.special.javaScriptTest","1399948175",["jquery.qunit"]],["mediawiki.tests.qunit.testrunner","1399948175",["jquery.qunit","jquery.qunit.completenessTest","mediawiki.page.startup","mediawiki.page.ready"]],["mediawiki.legacy.ajax","1399948175",["mediawiki.util","mediawiki.legacy.wikibits"]],["mediawiki.legacy.commonPrint","1399948175",[]],[
"mediawiki.legacy.config","1399948175",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.IEFixes","1399948175",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.mwsuggest","1399948175",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.preview","1399948175",["mediawiki.legacy.wikibits"]],["mediawiki.legacy.protect","1399948175",["mediawiki.legacy.wikibits","jquery.byteLimit"]],["mediawiki.legacy.shared","1399948175",[]],["mediawiki.legacy.oldshared","1399948175",[]],["mediawiki.legacy.upload","1399948175",["mediawiki.legacy.wikibits","mediawiki.util"]],["mediawiki.legacy.wikibits","1399948175",["mediawiki.util"]],["mediawiki.legacy.wikiprintable","1399948175",[]]]);mw.config.set({"wgLoadScript":"/wiki/load.php","debug":false,"skin":"vector","stylepath":"/wiki/skins","wgUrlProtocols":"http\\:\\/\\/|https\\:\\/\\/|ftp\\:\\/\\/|irc\\:\\/\\/|ircs\\:\\/\\/|gopher\\:\\/\\/|telnet\\:\\/\\/|nntp\\:\\/\\/|worldwind\\:\\/\\/|mailto\\:|news\\:|svn\\:\\/\\/|git\\:\\/\\/|mms\\:\\/\\/|\\/\\/",
"wgArticlePath":"/wiki/index.php?title=$1","wgScriptPath":"/wiki","wgScriptExtension":".php","wgScript":"/wiki/index.php","wgVariantArticlePath":false,"wgActionPaths":{},"wgServer":"http://www.elecrow.com","wgUserLanguage":"en","wgContentLanguage":"en","wgVersion":"1.19.1","wgEnableAPI":true,"wgEnableWriteAPI":true,"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgMainPageTitle":"Main Page","wgFormattedNamespaces":{"-2":"Media","-1":"Special","0":"","1":"Talk","2":"User","3":"User talk","4":"Elecrow","5":"Elecrow talk","6":"File","7":"File talk","8":"MediaWiki","9":"MediaWiki talk","10":"Template","11":"Template talk","12":"Help","13":"Help talk","14":"Category","15":"Category talk"},"wgNamespaceIds":{"media":-2,"special":-1,"":0,"talk":1,"user":2,"user_talk":3,"elecrow":4,
"elecrow_talk":5,"file":6,"file_talk":7,"mediawiki":8,"mediawiki_talk":9,"template":10,"template_talk":11,"help":12,"help_talk":13,"category":14,"category_talk":15,"image":6,"image_talk":7,"project":4,"project_talk":5},"wgSiteName":"Elecrow","wgFileExtensions":["png","gif","jpg","jpeg","zip","pdf","txt","ino"],"wgDBname":"elecro5_CrowWiki","wgFileCanRotate":true,"wgAvailableSkins":{"modern":"Modern","standard":"Standard","simple":"Simple","monobook":"MonoBook","chick":"Chick","vector":"Vector","nostalgia":"Nostalgia","myskin":"MySkin","cologneblue":"CologneBlue"},"wgExtensionAssetsPath":"/wiki/extensions","wgCookiePrefix":"elecro5_CrowWiki","wgResourceLoaderMaxQueryLength":-1,"wgCaseSensitiveNamespaces":[]});};if(isCompatible()){document.write("\x3cscript src=\"/wiki/load.php?debug=false\x26amp;lang=en\x26amp;modules=jquery%2Cmediawiki\x26amp;only=scripts\x26amp;skin=vector\x26amp;version=20120614T062240Z\"\x3e\x3c/script\x3e");}delete isCompatible;;

/* cache key: elecro5_CrowWiki:resourceloader:filter:minify-js:7:21983c5625a0d929bc959cc9f646320e */
