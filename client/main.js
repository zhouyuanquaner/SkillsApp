import React from 'react';
import { Meteor } from 'meteor/meteor';
import { render } from 'react-dom';
import CategoryApp from '../imports/ui/CategoryApp.jsx';


Meteor.startup(() => {
  render(
    <CategoryApp/>, document.getElementById('categories')
    );
});
