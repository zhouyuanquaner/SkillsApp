import React, { Component, PropTypes } from 'react';


export default class Category extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isOpen: false,
    };
  }

  getSub() {
    return this.state.isOpen ?
    this.props.cate.subCate.map((e, i) =>
      <li key={i} className='list-group-item'>{e}</li>
    ) : '';
  }

  toggleStateOnClick() {
    this.setState({
      isOpen: !this.state.isOpen,
    });
  }

  render() {
    return (
      <div className={'categories-' + (this.state.isOpen ? 'open' : 'close')} key={this.props.cate._id}>
          <li className='list-group-item' key={this.props.cate._id}
            onClick={this.toggleStateOnClick.bind(this)}>
            {this.props.cate.cate}
          </li>
          {this.getSub()}
      </div>
    );
  }
}

Category.propTypes = {
  cate: PropTypes.object.isRequired,
};
