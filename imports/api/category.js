// import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';

export const category = new Mongo.Collection('Cates');
export const bigCategory = new Mongo.Collection('Bigs');
