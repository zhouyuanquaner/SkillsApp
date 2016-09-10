import { Meteor } from 'meteor/meteor';
import '../imports/api/category.js';
import { Mysql } from 'meteor/nodets:mysql';

Meteor.startup(() => {
  // connect to MySQL Database
  const connectionSettings = {
    host: 'localhost',
    port: 3306,
    user: 'root',
    database: 'SkillsApp',
  };
  const db = Mysql.connect(connectionSettings);
  // generate an array with categories and subCategories information
  const category = db.meteorCollection('SubCategories', 'Cates');
  Meteor.publish('allCategories', () => category.find({}));

  const bigCategory = db.meteorCollection('Categories', 'Bigs');
  Meteor.publish('bigCategories', () => bigCategory.find({}));
});
