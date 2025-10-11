================
CODE SNIPPETS
================
### Gulp Integration Example

Source: https://github.com/fomantic/fomantic-ui/blob/develop/tasks/collections/README.md

Demonstrates how to import and initialize Fomantic UI's Gulp tasks, specifically the 'install' task, and then start the 'install' task.

```javascript
const gulp = require('gulp');
// modified to point to semantic folder
const install = require('tasks/collections/install');
gulp = install(gulp);

// tasks are now injected and ready to be used
gulp.start('install');
```

--------------------------------

### Fomantic UI Installation and Build Commands

Source: https://github.com/fomantic/fomantic-ui/blob/develop/src/README.md

Commands to install Fomantic UI dependencies and build the project using Gulp. Includes watching for file changes and building all files.

```bash
npm install

# Watch files
gulp watch

# Build all files
gulp build
```

--------------------------------

### Fomantic-UI Configuration Files Reference

Source: https://github.com/fomantic/fomantic-ui/blob/develop/src/README.md

This reference details the essential configuration files used in Fomantic-UI. These files are automatically generated during installation but require manual renaming if installing manually, and are crucial for managing themes and build tool integration.

```APIDOC
theme.config:
  usage: config file that stores each element's current theme for LESS
  initial_name: theme.config.example
site/:
  usage: folder storing all your site's variables and css overrides for each UI component
  initial_name: _site/
semantic.json:
  usage: stores folder paths for build tools and current installed version for updates. Only necessary when using build tools
  initial_name: semantic.json.example
```

--------------------------------

### Using Pre-Packaged Themes

Source: https://github.com/fomantic/fomantic-ui/blob/develop/src/README.md

Example of how to configure Fomantic UI to use a pre-packaged theme, such as the 'github' button theme, by modifying the theme.config file.

```less
@button: 'github';
```

--------------------------------

### Fomantic UI HTML Structure Example

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/homepage.html

Example HTML structure demonstrating Fomantic UI components like headers, menus, buttons, and content sections. Includes navigation elements and placeholders for images and text.

```html
<!-- Navigation and Header -->
<div class="ui fixed inverted menu">
  <div class="ui container">
    <a href="#" class="header item">
      <img class="logo" src="assets/images/logo.png">
      Fomantic UI
    </a>
    <a href="#" class="item">Home</a>
    <a href="#" class="item">Work</a>
    <a href="#" class="item">Company</a>
    <a href="#" class="item">Careers</a>
    <div class="right item">
      <a href="#" class="ui inverted button">Log in</a>
      <a href="#" class="ui inverted button">Sign Up</a>
    </div>
  </div>
</div>

<!-- Masthead Section -->
<div class="ui inverted vertical masthead segment">
  <div class="ui middle aligned stackable grid container">
    <div class="ui large text header item">
      Imagine-a-Company
    </div>
    <div class="ui large text header item">
      Do whatever you want when you want to.
    </div>
    <a class="ui huge primary button">
      Get Started
      <i class="right arrow icon"></i>
    </a>
  </div>
</div>

<!-- Content Sections -->
<div class="ui vertical stripe segment">
  <div class="ui text container">
    <h3>We Help Companies and Companions</h3>
    <p>We can give your company superpowers to do things that they never thought possible. Let us delight your customers and empower your needs...through pure data analytics.</p>
  </div>
</div>

<div class="ui vertical stripe quote segment">
  <div class="ui equal height stackable grid">
    <div class="center aligned four wide column">
      <h3>"What a Company"</h3>
      <p>That is what they all say about us</p>
      <div class="ui avatar image">
        <img src="assets/images/avatar/nan.jpg">
      </div>
      <br/>
      <strong>Nan</strong> Chief Fun Officer Acme Toys
    </div>
  </div>
</div>

<!-- Footer -->
<div class="ui inverted vertical footer segment">
  <div class="ui container">
    <div class="ui stackable inverted divided equal height grid">
      <div class="three wide column">
        <h4 class="ui inverted header">About</h4>
        <div class="ui inverted link list">
          <a href="#" class="item">Sitemap</a>
          <a href="#" class="item">Contact Us</a>
          <a href="#" class="item">Religious Ceremonies</a>
          <a href="#" class="item">Gazebo Plans</a>
        </div>
      </div>
      <div class="three wide column">
        <h4 class="ui inverted header">Services</h4>
        <div class="ui inverted link list">
          <a href="#" class="item">Banana Pre-Order</a>
          <a href="#" class="item">DNA FAQ</a>
          <a href="#" class="item">How To Access</a>
          <a href="#" class="item">Favorite X-Men</a>
        </div>
      </div>
      <div class="ten wide column">
        <h4 class="ui inverted header">Footer Header</h4>
        <p>Extra space for a call to action inside the footer that could help re-engage users.</p>
      </div>
    </div>
  </div>
</div>
```

--------------------------------

### Importing Gulp Tasks in Gulpfile

Source: https://github.com/fomantic/fomantic-ui/blob/develop/src/README.md

Example of how to import and use Fomantic UI's Gulp tasks within your own Gulpfile.

```javascript
const watch = require('path/to/semantic/tasks/watch');

gulp.task('watch ui', 'Watch Fomantic-UI', watch);
```

--------------------------------

### Install Fomantic-UI Nightly Build

Source: https://github.com/fomantic/fomantic-ui/blob/develop/README.md

Installs the nightly build of Fomantic-UI, which includes the latest features and bug fixes. Use this for early testing.

```bash
$ npm install fomantic-ui@nightly
```

--------------------------------

### Importing Fomantic UI LESS Files

Source: https://github.com/fomantic/fomantic-ui/blob/develop/src/README.md

Demonstrates how to import all Fomantic UI components or individual components into your LESS files. Requires setting up theme.config and site folder.

```less
/* Import all components */
@import 'src/semantic';

/* Import a specific component */
& { @import 'src/definitions/elements/button'; }
```

--------------------------------

### Setup Git Environment for Fomantic-UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/CONTRIBUTING.md

Steps to clone the Fomantic-UI repository, add the main repository as a remote, fetch its branches, and checkout a new branch based on the 'develop' branch.

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/Fomantic-UI.git
cd Fomantic-UI
git remote add fui https://github.com/fomantic/Fomantic-UI.git
git fetch fui
git checkout -b <BRANCH_NAME> fui/develop
```

--------------------------------

### Install Fomantic-UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/README.md

Installs the latest stable version of Fomantic-UI using npm. This is the recommended way to add Fomantic-UI to your project.

```bash
$ npm install fomantic-ui
```

--------------------------------

### Install Fomantic UI Packages

Source: https://github.com/fomantic/fomantic-ui/blob/develop/README.md

Provides installation commands for Fomantic UI via npm for CSS-only and LESS, and via gem for SASS. These commands are used to add the Fomantic UI library to your project.

```bash
npm install fomantic-ui-css
```

```bash
npm install fomantic-ui-less
```

```gem
gem 'fomantic-ui-sass'
```

--------------------------------

### Fomantic UI Sticky Example Styling

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/sticky.html

CSS styles for the Fomantic UI sticky example, defining the appearance of the body, main container, menu, overlay, and floated images to create a responsive and visually appealing layout.

```css
body { background-color: #fff; } .main.container { margin-top: 2em; } .main.menu { margin-top: 4em; border-radius: 0; border: none; box-shadow: none; transition: box-shadow 0.5s ease, padding 0.5s ease ; } .main.menu .item img.logo { margin-right: 1.5em; } .overlay { float: left; margin: 0em 3em 1em 0em; } .overlay .menu { position: relative; left: 0; transition: left 0.5s ease; } .main.menu.fixed { background-color: #fff; border: 1px solid #ddd; box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2); } .overlay.fixed .menu { left: 800px; } .text.container .left.floated.image { margin: 2em 2em 2em -4em; } .text.container .right.floated.image { margin: 2em -4em 2em 2em; } .ui.footer.segment { margin: 5em 0em 0em; padding: 5em 0em; }
```

--------------------------------

### Install Fomantic UI Component with Bower

Source: https://github.com/fomantic/fomantic-ui/blob/develop/tasks/config/admin/templates/README.md

Installs a specific Fomantic UI component using the Bower package manager. Ensure Bower is installed and configured in your project.

```bash
bower install fomantic-ui-{component}
```

--------------------------------

### Fomantic UI Responsive Width Adjustments

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Illustrates how to specify different column widths for different screen sizes in Fomantic UI grids, allowing for fine-grained control over responsive layouts.

```html
<div class="ui grid">
  <div class="ten wide column computer only">ten wide column computer only</div>
  <div class="six wide column computer only">six wide column computer only</div>
  <div class="sixteen wide column mobile only">sixteen wide column mobile only</div>
  <div class="computer only row">computer only row</div>
  <div class="mobile only column">mobile only column</div>
</div>
```

--------------------------------

### Fomantic UI Build Tasks

Source: https://github.com/fomantic/fomantic-ui/blob/develop/tasks/README.md

Lists the available command-line tasks for Fomantic UI. These include 'watch' for compiling changed files, 'build' for compiling all files, 'version' for outputting the version number, and 'install' for setting up paths.

```bash
gulp watch
gulp build
gulp version
gulp install
```

--------------------------------

### Import Specific Fomantic-UI LESS Component

Source: https://github.com/fomantic/fomantic-ui/blob/develop/src/README.md

To import an individual Fomantic-UI component, such as a button, use this LESS snippet. The component is scoped within '& {}' to ensure proper integration. Remember to add vendor prefixes during your build process.

```less
/* Import a specific component */
& { @import 'src/definitions/elements/button'; }
```

--------------------------------

### Responsive Table - Fomantic UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/responsive.html

Demonstrates a responsive table structure in Fomantic UI. This example shows how table columns can adapt or stack on smaller screens for better readability.

```html
<table class="ui celled stackable table">
  <thead>
    <tr>
      <th>Employee</th>
      <th>Correct Guesses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <h4 class="ui image header">
          <img src="assets/images/wireframe/square-image.png" class="ui small circular image">
          <div class="content">
            Lena
            <div class="sub header">Human Resources</div>
          </div>
        </h4>
      </td>
      <td>22</td>
    </tr>
    <tr>
      <td>
        <h4 class="ui image header">
          <img src="assets/images/wireframe/square-image.png" class="ui small circular image">
          <div class="content">
            Matthew
            <div class="sub header">Fabric Design</div>
          </div>
        </h4>
      </td>
      <td>15</td>
    </tr>
    <tr>
      <td>
        <h4 class="ui image header">
          <img src="assets/images/wireframe/square-image.png" class="ui small circular image">
          <div class="content">
            Lindsay
            <div class="sub header">Entertainment</div>
          </div>
        </h4>
      </td>
      <td>12</td>
    </tr>
    <tr>
      <td>
        <h4 class="ui image header">
          <img src="assets/images/wireframe/square-image.png" class="ui small circular image">
          <div class="content">
            Mark
            <div class="sub header">Executive</div>
          </div>
        </h4>
      </td>
      <td>11</td>
    </tr>
  </tbody>
</table>
```

--------------------------------

### Configure Fomantic-UI Pre-Packaged Theme in theme.config

Source: https://github.com/fomantic/fomantic-ui/blob/develop/src/README.md

This LESS snippet demonstrates how to apply a pre-packaged theme to a specific Fomantic-UI component, such as a button, by modifying the 'theme.config' file. Simply change the value to the desired theme name, like 'github'.

```less
@button: 'github';
```

--------------------------------

### Fomantic UI Responsive Doubling Columns

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Shows how to make columns in a Fomantic UI grid double in width at each device size jump, creating a responsive layout that adapts to different screen sizes.

```html
<div class="ui doubling grid">
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
</div>
```

--------------------------------

### Install Fomantic UI Component with NPM

Source: https://github.com/fomantic/fomantic-ui/blob/develop/tasks/config/admin/templates/README.md

Installs a specific Fomantic UI component using the NPM package manager. This is a common method for modern JavaScript projects.

```shell
npm install fomantic-ui-{component}
```

--------------------------------

### Fomantic UI Stackable Columns

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Demonstrates how to configure columns in a Fomantic UI grid to stack vertically on mobile devices, improving readability on smaller screens.

```html
<div class="ui stackable grid">
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
</div>
```

--------------------------------

### Responsive Menu and Item - Fomantic UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/responsive.html

Shows examples of a responsive menu and item components in Fomantic UI. The menu includes navigation links and a logo, while the item demonstrates content layout with images and text.

```html
<!-- Responsive Menu -->
<div class="ui menu">
  <img src="assets/images/logo.png" class="ui item image">
  <a class="item">Features</a>
  <a class="item">Testimonials</a>
  <div class="right menu">
    <a class="ui item">Sign-in</a>
  </div>
</div>

<!-- Responsive Item -->
<div class="ui items">
  <div class="item">
    <a class="ui tiny image">
      <img src="assets/images/wireframe/image.png">
    </a>
    <div class="content">
      <a class="header">Content Header</a>
      <div class="meta">
        <span>Date</span>
        <span>Category</span>
      </div>
      <div class="description">
        <p>A description which may flow for several lines and give context to the content.</p>
      </div>
      <div class="extra">
        <a class="ui label">Primary</a>
        <a class="ui label">Limited</a>
      </div>
    </div>
  </div>
  <div class="item">
    <a class="ui tiny image">
      <img src="assets/images/wireframe/square-image.png">
    </a>
    <div class="content">
      <a class="header">Username</a>
    </div>
  </div>
  <div class="item">
    <a class="ui tiny image">
      <img src="assets/images/wireframe/image.png">
    </a>
    <div class="content">
      <a class="header">Content Header</a>
      <div class="meta">
        <span>Date</span>
        <span>Category</span>
      </div>
      <div class="description">
        <p>A description which may flow for several lines and give context to the content.</p>
      </div>
      <div class="extra">
        <a class="ui label">Primary</a>
      </div>
    </div>
  </div>
</div>
```

--------------------------------

### Apache License 2.0 Boilerplate Notice

Source: https://github.com/fomantic/fomantic-ui/blob/develop/dist/themes/material/assets/fonts/LICENSE.txt

This notice provides the standard copyright and license information required when applying the Apache License, Version 2.0 to your work. It should be attached to your files, enclosed in the appropriate comment syntax for the file format, and customized with your identifying information.

```Text
Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

--------------------------------

### Fomantic UI Login Form with Validation

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/login.html

This snippet demonstrates how to set up a login form using Fomantic UI and its built-in form validation. It includes rules for email format and password length.

```javascript
$(document).ready(function() {
  $('.ui.form').form({
    fields: {
      email: {
        identifier: 'email',
        rules: [
          {
            type: 'empty',
            prompt: 'Please enter your e-mail'
          },
          {
            type: 'email',
            prompt: 'Please enter a valid e-mail'
          }
        ]
      },
      password: {
        identifier: 'password',
        rules: [
          {
            type: 'empty',
            prompt: 'Please enter your password'
          },
          {
            type: 'length[6]',
            prompt: 'Your password must be at least 6 characters'
          }
        ]
      }
    }
  });
});
```

```html
<div class="ui middle aligned center aligned grid">
  <div class="column">
    <h2 class="ui teal image header">
      <img src="assets/images/logo.png" class="ui image">
      <div class="content">
        Log-in to your account
      </div>
    </h2>
    <form class="ui large form">
      <div class="ui stacked segment">
        <div class="field">
          <div class="ui left icon input">
            <i class="user icon"></i>
            <input type="text" name="email" placeholder="E-mail address">
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="lock icon"></i>
            <input type="password" name="password" placeholder="Password">
          </div>
        </div>
        <div class="ui fluid large teal submit button">Login</div>
      </div>

      <div class="ui error message"></div>

    </form>

    <div class="ui message">
      New to us? <a href="#">Sign Up</a>
    </div>
  </div>
</div>
```

```css
body { background-color: #dadada; }
body > .grid { height: 100%; }
.image { margin-top: -100px; }
.column { max-width: 450px; }
```

--------------------------------

### Fomantic UI Grid CSS Styling

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Provides basic CSS styling for Fomantic UI grids, including styles for code elements, containers, headers, images, and grid pseudo-elements for visualization.

```css
/* Some basic formatting */
code {
  background-color: #e0e0e0;
  padding: 0.25em 0.3em;
  font-family: 'Lato';
  font-weight: bold;
}
.container {
  padding: 5em 0em;
}
.ui.dividing.header, .first {
  margin-top: 5em;
}
.ui.dividing.header:first-child {
  margin-top: 0em;
}
h1, h3 {
  margin-top: 10em;
}
img {
  display: block;
  max-width: 100%;
}
img + img {
  margin-top: 0.5em;
}
/* Shows content box (not negative margins) */
.grid {
  position: relative;
}
.grid:before {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background-color: #f0f0f0;
  content: '';
  width: calc(100% - 2rem);
  height: calc(100% - 2rem);
  box-shadow: 0px 0px 0px 1px #ddd inset;
}
.ui.divided.grid:before, .celled.grid:before {
  display: none;
}
.ui.aligned .column:after {
  display: none !important;
}
.grid .column:not(.row):not(.grid):after {
  background-color: rgba(86, 61, 124, .15);
  box-shadow: 0px 0px 0px 1px rgba(86, 61, 124, 0.2) inset;
  content: "";
  display: block;
  min-height: 50px;
}
@media only screen and (max-width: 768px) {
  .stackable.grid:before {
    width: 100%;
    left: 0em;
  }
}
```

--------------------------------

### Fomantic UI Equal Width Columns

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Explains how to create an 'equal width grid' in Fomantic UI, where column sizes are automatically adjusted to fit evenly within a single row.

```html
<div class="ui equal width grid">
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
  <div class="column">column</div>
</div>
```

--------------------------------

### Responsive Grid Variations - Fomantic UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/responsive.html

Demonstrates various responsive grid layouts in Fomantic UI, including stackable, divided, celled, and doubling variations. These examples show how grids adapt to different screen sizes and orientations.

```html
<!-- Stackable Grid -->
<div class="ui stackable grid">
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
</div>

<!-- Stackable Divided Grid -->
<div class="ui stackable divided grid">
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
</div>

<!-- Celled Stackable Grid -->
<div class="ui celled stackable grid">
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
  <div class="four wide column">
    <p>Content</p>
  </div>
</div>
```

--------------------------------

### Initialize Fomantic UI Components with jQuery

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/components/card.html

Initializes Fomantic UI interactive components upon document readiness using jQuery. It configures image dimmers on specific card elements to activate on hover and enables the rating component functionality across the page. This ensures dynamic UI elements are properly set up after the DOM is loaded.

```JavaScript
$(document) .ready(function() { $('.special.card .image').dimmer({ on: 'hover' }); $('.rating') .rating() ; $('.card .dimmer') .dimmer({ on: 'hover' }) ; }) ;
```

--------------------------------

### Install Fomantic UI Component with Meteor

Source: https://github.com/fomantic/fomantic-ui/blob/develop/tasks/config/admin/templates/README.md

Adds a specific Fomantic UI component to a Meteor project. This command integrates the component directly into your Meteor application.

```meteor
meteor add fomantic:ui-{component}
```

--------------------------------

### Fomantic UI Sticky Initialization and Behavior

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/components/sticky-context.html

Initializes the Fomantic UI sticky component with a specified context and handles button clicks to change the sticky element's size and the container's visibility. Includes JavaScript for dynamic class manipulation and sticky refresh.

```javascript
$(document).ready(function() {
  // sticky $('.ui.sticky').sticky({
  //   context: $('.page.container'),
  // });
  $('.sticky.field .button')
    .on('click', function() {
      if ($(this).hasClass('tall')) {
        $('.ui.sticky').addClass('tall').removeClass('short');
      } else {
        $('.ui.sticky').addClass('short').removeClass('tall');
      }
      $(this).addClass('primary').siblings().removeClass('primary');
      $('.ui.sticky').sticky('refresh');
    });
  $('.content.field .button')
    .on('click', function() {
      if ($(this).hasClass('tall')) {
        $('.page.container').addClass('tall').removeClass('short');
      } else {
        $('.page.container').addClass('short').removeClass('tall');
      }
      $(this).addClass('primary').siblings().removeClass('primary');
      $('.ui.sticky').sticky('refresh');
    });
});
```

--------------------------------

### Fomantic UI Sticky Menu and Lazy Load Images

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/sticky.html

JavaScript code to initialize Fomantic UI's sticky behavior for the main menu and overlay, and to enable lazy loading for images. It also sets up dropdown menus to appear on hover.

```javascript
$(document) .ready(function() { // fix main menu to page on passing $('.main.menu').visibility({ type: 'fixed' }); $('.overlay').visibility({ type: 'fixed', offset: 80 }); // lazy load images $('.image').visibility({ type: 'image', transition: 'vertical flip in', duration: 500 }); // show dropdown on hover $('.main.menu .ui.dropdown').dropdown({ on: 'hover' }); }) ;
```

--------------------------------

### Fomantic UI Grid Column Widths

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Demonstrates how to specify individual column widths within a Fomantic UI grid. Columns will automatically flow to the next row if the total width exceeds the grid's capacity.

```html
<div class="ui grid">
  <div class="four wide column">
    four wide column
  </div>
  <div class="eight wide column">
    eight wide column
  </div>
  <div class="four wide column">
    four wide column
  </div>
</div>
```

--------------------------------

### Fomantic UI Sticky Styling and Layout

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/components/sticky-context.html

Provides CSS rules for styling the Fomantic UI sticky elements, page containers, and related components. Includes styles for different states like 'tall' and 'short', and ensures proper layout and visibility.

```css
body {
  background-color: #fff;
}
.text.container {
  position: relative;
  margin-top: 3rem;
}
.rail .image {
  margin-bottom: 1rem;
}
.ui.sticky {
  padding: 1rem 0rem;
}
.masthead {
  background-color: #121212;
  padding: 4rem 0rem;
  color: rgba(255, 255, 255, 0.6);
  text-align: center;
}
.masthead p {
  font-size: 18px;
  max-width: 450px;
  margin: 0 auto 2rem;
}
.ui.sticky.short img {
  display: none;
}
.ui.sticky.short img:first-child {
  display: block;
}
.ui.sticky.short img:nth-child(2) {
  display: block;
}
.page.container {
  margin-bottom: 3rem;
}
.page.container.short p {
  display: none;
}
.page.container.short p:first-of-type {
  display: block;
}
```

--------------------------------

### Fomantic UI Visibility Callback Example

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/responsive.html

JavaScript code for handling Fomantic UI's visibility events, specifically for managing header visibility and scroll behavior on window resize. It includes logic to preserve element positions during resize.

```javascript
$(document).ready(function() {
  let $headers = $('body > h3'),
      $header = $headers.first(),
      ignoreScroll = false,
      timer ;

  // Preserve example in viewport when resizing browser
  $(window)
    .on('resize', function() {
      // ignore callbacks from scroll change
      clearTimeout(timer);
      $headers.visibility('disable callbacks');

      // preserve position
      $(document).scrollTop($header.offset().top);

      // allow callbacks in 500ms
      timer = setTimeout(function() {
        $headers.visibility('enable callbacks');
      }, 500);
    })
  ;

  $headers.visibility({
    // fire once each time passed
    once: false,
    // don't refresh position on resize
    checkOnRefresh: true,
    // lock to this element on resize
    onTopPassed: function() {
      $header = $(this);
    },
    onTopPassedReverse: function() {
      $header = $(this);
    }
  });
});
```

--------------------------------

### Fixed Menu Layout - Fomantic UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/fixed.html

This snippet shows the HTML structure and CSS styling for a fixed menu layout in Fomantic UI. It includes a header with a logo and navigation links, a main content area, and a footer.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Fixed Menu Example - Fomantic</title>
  <link rel="stylesheet" type="text/css" href="/dist/semantic.min.css">
  <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
  <script src="/dist/semantic.min.js"></script>
</head>
<body>

<div class="ui inverted fixed menu">
  <div class="ui container">
    <a href="#" class="header item">
      <img class="logo" src="assets/images/logo.png">
      Project Name
    </a>
    <a href="#" class="item">Home</a>
    <div class="ui simple dropdown item">
      Dropdown
      <i class="dropdown icon"></i>
      <div class="menu">
        <a class="item" href="#"><i class="edit icon"></i> Edit Profile</a>
        <a class="item" href="#"><i class="globe icon"></i> Choose Language</a>
        <a class="item" href="#"><i class="settings icon"></i> Account Settings</a>
      </div>
    </div>
    <a href="#" class="item">Link Item</a>
    <a href="#" class="item">Link Item</a>
  </div>
</div>

<div class="ui main text container">
  <h1 class="ui header">Fomantic UI Fixed Template</h1>
  <p>This is a basic fixed menu template using fixed size containers.</p>
  <p>A text container is used for the main container, which is useful for single column layouts</p>
  <img src="assets/images/wireframe/media-paragraph.png" alt="Wireframe 1">
  <img src="assets/images/wireframe/paragraph.png" alt="Wireframe 2">
  <img src="assets/images/wireframe/paragraph.png" alt="Wireframe 3">
  <img src="assets/images/wireframe/paragraph.png" alt="Wireframe 4">
  <img src="assets/images/wireframe/paragraph.png" alt="Wireframe 5">
  <img src="assets/images/wireframe/paragraph.png" alt="Wireframe 6">
  <img src="assets/images/wireframe/paragraph.png" alt="Wireframe 7">

  <h4 class="ui header">Group 1</h4>
  <a href="#" class="item">Link One</a>
  <a href="#" class="item">Link Two</a>
  <a href="#" class="item">Link Three</a>
  <a href="#" class="item">Link Four</a>

  <h4 class="ui header">Group 2</h4>
  <a href="#" class="item">Link One</a>
  <a href="#" class="item">Link Two</a>
  <a href="#" class="item">Link Three</a>
  <a href="#" class="item">Link Four</a>

  <h4 class="ui header">Group 3</h4>
  <a href="#" class="item">Link One</a>
  <a href="#" class="item">Link Two</a>
  <a href="#" class="item">Link Three</a>
  <a href="#" class="item">Link Four</a>
</div>

<div class="ui inverted vertical footer segment">
  <div class="ui container">
    <div class="ui stackable grid">
      <div class="three wide column">
        <h4 class="ui inverted header">Footer Header</h4>
        <p>Extra space for a call to action inside the footer that could help re-engage users.</p>
      </div>
      <div class="three wide column">
        <h4 class="ui inverted header">Group 1</h4>
        <a href="#" class="item">Link One</a>
        <a href="#" class="item">Link Two</a>
        <a href="#" class="item">Link Three</a>
        <a href="#" class="item">Link Four</a>
      </div>
      <div class="three wide column">
        <h4 class="ui inverted header">Group 2</h4>
        <a href="#" class="item">Link One</a>
        <a href="#" class="item">Link Two</a>
        <a href="#" class="item">Link Three</a>
        <a href="#" class="item">Link Four</a>
      </div>
      <div class="seven wide column">
        <h4 class="ui inverted header">Site Map</h4>
        <a href="#" class="item">Site Map</a>
        <a href="#" class="item">Contact Us</a>
        <a href="#" class="item">Terms and Conditions</a>
        <a href="#" class="item">Privacy Policy</a>
      </div>
    </div>
  </div>
</div>

</body>
</html>
```

--------------------------------

### Fomantic UI Fixed Menu Styling

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/fixed.html

This CSS snippet defines the styling for the fixed menu and layout elements in Fomantic UI. It sets background colors, margins, and positions for the menu and containers.

```css
body { background-color: #fff; }
.ui.menu .item img.logo { margin-right: 1.5em; }
.main.container { margin-top: 7em; }
.wireframe { margin-top: 2em; }
.ui.footer.segment { margin: 5em 0em 0em; padding: 5em 0em; }
```

--------------------------------

### Fomantic UI Vertical Alignment in Grid

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Demonstrates how to apply vertical alignment to content within a Fomantic UI grid, row, or column. This controls the vertical positioning of items within their container.

```html
<div class="ui grid">
  <div class="column">
    <img src="assets/images/wireframe/image.png" alt="Placeholder">
  </div>
  <div class="column">
    <img src="assets/images/wireframe/image.png" alt="Placeholder">
    <img src="assets/images/wireframe/image.png" alt="Placeholder">
  </div>
  <div class="column">
    <img src="assets/images/wireframe/image.png" alt="Placeholder">
  </div>
</div>
```

--------------------------------

### Fomantic UI Grid Row Clearing

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Shows how to manually specify new rows in a Fomantic UI grid by using row wrappers. This is useful for controlling the layout when columns don't fill a full row.

```html
<div class="ui grid">
  <div class="row">
    <div class="column">column</div>
    <div class="column">column</div>
    <div class="column">column</div>
    <div class="column">column</div>
    <div class="column">column</div>
    <div class="column">column</div>
  </div>
</div>
```

--------------------------------

### Fomantic UI Centered Grid Content

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Illustrates how to center content within a Fomantic UI grid using variations like 'ui centered grid', 'centered row', or 'centered column'. This is applied when a row doesn't occupy all sixteen grid columns.

```html
<div class="ui centered grid">
  <div class="column">
    Centered Column
  </div>
</div>
```

--------------------------------

### Fomantic UI Form Validation for Login Fields

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/login.html

Initializes Fomantic UI form validation for the email and password input fields. It includes rules to check for empty fields, validate email format, and enforce a minimum password length of 6 characters, providing user-friendly prompts for each rule violation.

```JavaScript
$(document)
  .ready(function() {
    $('.ui.form')
      .form({
        fields: {
          email: {
            identifier : 'email',
            rules: [
              { type : 'empty', prompt : 'Please enter your e-mail' },
              { type : 'email', prompt : 'Please enter a valid e-mail' }
            ]
          },
          password: {
            identifier : 'password',
            rules: [
              { type : 'empty', prompt : 'Please enter your password' },
              { type : 'length[6]', prompt : 'Your password must be at least 6 characters' }
            ]
          }
        }
      })
    ;
  })
;
```

--------------------------------

### Fomantic UI Text Alignment in Grid

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Shows how to align text within a Fomantic UI grid at the grid, row, or column level using alignment variations like 'right aligned', 'left aligned', or 'center aligned'.

```html
<div class="ui grid">
  <div class="right aligned column">right aligned column</div>
  <div class="left aligned column">left aligned column</div>
  <div class="center aligned row">
    <div class="column">center aligned row</div>
    <div class="column">center aligned row</div>
  </div>
</div>
```

--------------------------------

### Fomantic UI Floated Grid Content

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/grid.html

Demonstrates how to float content left or right within a Fomantic UI grid row. Due to flexbox, the 'left floated' item should appear first, and the 'right floated' item last.

```html
<div class="ui grid">
  <div class="left floated column">
    Left floated
  </div>
  <div class="right floated column">
    Right floated
  </div>
</div>
```

--------------------------------

### Fomantic UI Theming and Component Initialization

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/components/card.html

Demonstrates basic Fomantic UI theming with CSS and JavaScript initialization for interactive components like dimmers and ratings on document ready.

```javascript
$(document) .ready(function() {
  $('.special.card .image').dimmer({ on: 'hover' });
  $('.rating') .rating() ;
  $('.card .dimmer') .dimmer({ on: 'hover' }) ;
});
```

--------------------------------

### Responsive Steps - Fomantic UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/responsive.html

Demonstrates the responsive steps component in Fomantic UI, used for multi-step processes. The steps adapt their layout based on screen size.

```html
<div class="ui steps">
  <a class="step">
    <div class="title">Shipping</div>
    <div class="description">Choose your shipping options</div>
  </a>
  <a class="step">
    <div class="title">Billing</div>
    <div class="description">Enter billing information</div>
  </a>
  <a class="active step">
    <div class="title">Confirm Order</div>
    <div class="description">Review your order details</div>
  </a>
</div>
```

--------------------------------

### Create New Development Branch for Fomantic-UI

Source: https://github.com/fomantic/fomantic-ui/blob/develop/CONTRIBUTING.md

Illustrates the Git command to create and checkout a new branch based on the Fomantic-UI 'develop' branch, which is the required base for all pull requests.

```bash
$ git checkout -b <BRANCH_NAME> fui/develop
```

--------------------------------

### Fomantic UI JavaScript Initialization

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/homepage.html

Initializes Fomantic UI components, including sidebar and sticky menu behavior, upon document ready. It handles menu visibility based on scroll position.

```javascript
$(document) .ready(function() { // fix menu when passed $('.masthead') .visibility({ once: false, onBottomPassed: function() { $('.fixed.menu').transition('fade in'); }, onBottomPassedReverse: function() { $('.fixed.menu').transition('fade out'); } }) ; // create sidebar and attach to menu open $('.ui.sidebar') .sidebar('attach events', '.toc.item') ; }) ;
```

--------------------------------

### Initialize Fomantic UI Dropdowns

Source: https://github.com/fomantic/fomantic-ui/blob/develop/examples/bootstrap.html

This JavaScript snippet initializes Fomantic UI dropdowns on the page. It targets elements with the class 'ui.selection.dropdown' for standard dropdowns and '.ui.menu .ui.dropdown' for dropdowns within menus, applying a 'hover' activation for the latter. Ensure Fomantic UI CSS and JS are included before running this code.

```javascript
$(document) .ready(function() { $('.ui.selection.dropdown').dropdown(); $('.ui.menu .ui.dropdown').dropdown({ on: 'hover' }); }) ;
```

--------------------------------

### Fomantic UI v3.0 Library Implementations

Source: https://github.com/fomantic/fomantic-ui/blob/develop/ROADMAP.md

Details the proposed and planned library implementations for Fomantic UI v3.0, supporting various JavaScript frameworks and technologies.

```javascript
React
```

```javascript
Vue
```

```javascript
Angular
```

```javascript
Meteor
```

```javascript
Stencil
```

```javascript
Mithril
```

```javascript
Web Components (Shadow DOM)
```