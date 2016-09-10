import React, { Component, PropTypes } from 'react';
import { Meteor } from 'meteor/meteor';
import { createContainer } from 'meteor/react-meteor-data';
import { category } from '../api/category.js';
import Category from './Category.jsx';

class CategoryApp extends Component {
  renderData() {
    return this.props.cate.map((e) => (
      // <Category id={this.props.cate._id} cate={this.props.cate} />
      <Category key={e._id} cate={e} />
    ));
  }

  render() {
    return (
      <div className='categories-content'>
        {this.renderData()}
      </div>);
  }
}

CategoryApp.propTypes = {
  cate: PropTypes.array.isRequired,
};

export default createContainer(() => {
  Meteor.subscribe('allCategories');
  // generate an array with categories and subCategories information
  const bigCateWithDup = category.find({}).fetch().map((e) => e.Category);
  const bigCate = [];
  bigCateWithDup.forEach((item) => {
    if (bigCate.indexOf(item) < 0) {
      bigCate.push(item);
    }
  });
  const allCategories = [];
  bigCate.forEach((e, i) => {
    const sub = category.find({ Category: e }).fetch();
    allCategories.push(
      {
        cate: e,
        subCate: sub.map((l) => l.SubCategory),
        _id: i,
      }
    );
  });
  window.hihi = allCategories;
  return {
    cate: allCategories,
  };
}, CategoryApp);
