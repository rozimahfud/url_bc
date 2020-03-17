const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const window = (new JSDOM(``, { runScripts: "outside-only" })).window;
const document = (new JSDOM(``, { runScripts: "outside-only" })).window.document;
const navigator = (new JSDOM(``, { runScripts: "outside-only" })).window.navigator;

const top = (new JSDOM(``, { runScripts: "outside-only" })).window.top;
const self = (new JSDOM(``, { runScripts: "outside-only" })).window.self;
const screen = (new JSDOM(``, { runScripts: "outside-only" })).window.screen;
const parent = (new JSDOM(``, { runScripts: "outside-only" })).window.parent;
const length = (new JSDOM(``, { runScripts: "outside-only" })).window.length;
const frames = (new JSDOM(``, { runScripts: "outside-only" })).window.frames;
const origin = (new JSDOM(``, { runScripts: "outside-only" })).window.origin;
const history = (new JSDOM(``, { runScripts: "outside-only" })).window.history;
const toolbar = (new JSDOM(``, { runScripts: "outside-only" })).window.toolbar;
const menubar = (new JSDOM(``, { runScripts: "outside-only" })).window.menubar;
const external = (new JSDOM(``, { runScripts: "outside-only" })).window.external;
const location = (new JSDOM(``, { runScripts: "outside-only" })).window.location;
const statusbar = (new JSDOM(``, { runScripts: "outside-only" })).window.statusbar;
const scrollbars = (new JSDOM(``, { runScripts: "outside-only" })).window.scrollbars;
const performance = (new JSDOM(``, { runScripts: "outside-only" })).window.performance;
const personalbar = (new JSDOM(``, { runScripts: "outside-only" })).window.personalbar;
const locationbar = (new JSDOM(``, { runScripts: "outside-only" })).window.locationbar;
const localstorage = (new JSDOM(``, { runScripts: "outside-only" })).window.localstorage;
const frameElement = (new JSDOM(``, { runScripts: "outside-only" })).window.frameElement;
const customElements = (new JSDOM(``, { runScripts: "outside-only" })).window.customElements;

const $ = require("jquery")(window);
const jQuery = require("jquery")(window);
const jquery = require("jquery")(window);

function alert(name) {}
const Handlebars = require("handlebars");

exports.$ = $;
exports.top = top;
exports.self = self;
exports.alert = alert;
exports.window = window;
exports.screen = screen;
exports.parent = parent;
exports.length = length;
exports.jQuery = jQuery;
exports.jquery = jquery;
exports.frames = frames;
exports.origin = origin;
exports.history = history;
exports.toolbar = toolbar;
exports.menubar = menubar;
exports.document = document;
exports.external = external;
exports.location = location;
exports.navigator = navigator;
exports.statusbar = statusbar;
exports.Handlebars = Handlebars;
exports.scrollbars = scrollbars;
exports.performance = performance;
exports.personalbar = personalbar;
exports.locationbar = locationbar;
exports.localstorage = localstorage;
exports.frameElement = frameElement;
exports.customElements = customElements;