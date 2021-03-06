import React, { Component, PropTypes } from 'react';
import { observer } from 'mobx-react';


@observer
class AddToCart extends Component {
  static propTypes = {
    product: PropTypes.object,
    store: PropTypes.object,
  }

  render() {
    const { product } = this.props;
    if (product.activeCartitem) {
      return <div className="bg-green c-white pa-8px tc br2 br--bottom pointer flex justify-center items-center min-h-50px">
        <div onClick={product.removeFromCart}
          className="btn btn-small btn-white rounded w-30px h-30px pa-0px bra-30px justify-center fs-120r">
          <i className="ion-android-remove"></i>
        </div>
        <span className="count fs-120r pl-10px pr-10px">{product.activeCartitem.count}</span>
        <div onClick={product.addToCart}
          className="btn btn-small btn-white rounded w-30px h-30px pa-0px bra-30px justify-center fs-120r">
          <i className="ion-android-add"></i>
        </div>
      </div>;
    }
    return <div className="bg-green c-white pa-8px tc br2 br--bottom pointer min-h-50px flex justify-center items-center" onClick={product.addToCart}>
      <span className="ion-bag fs-120r mr-10px" />
      <span>Добавить в корзину</span>
    </div>;
  }
}


@observer
class Property extends Component {

  static propTypes = {
    propObject: PropTypes.object,
    product: PropTypes.object,
  }

  setActiveProperty = () => {
    const { propObject, product } = this.props;
    product.setActiveProperty(propObject.id);
  }

  render() {
    const { propObject } = this.props;

    return <button
      className={`property btn btn-small rounded ${propObject.isActive ? 'active' : ''} ${propObject.inUse ? 'btn-green' : 'btn-white'} mr-7px mt-5px`}
      onClick={this.setActiveProperty}>
      {propObject.value} {propObject.type.unit}
    </button>;

  }
}


@observer
class Product extends Component {

  static propTypes = {
    product: PropTypes.object,
    store: PropTypes.object,
  }

  render() {
    const { product, store } = this.props;
    return <div className="product-container">
      <div className="ba bd-mild-gray2 pa-10px tc br2 br--top">
        <img src={ product.images[0].croppedImage } alt="" className="max-h-150px" />
        <p className="fs-190r mb-0px">{product.activeProperty ? product.activeProperty.price : product.price}р.</p>
        <a href={ product.absoluteUrl } className="product-name c-brown">{ product.name }</a>

          {product.properties &&
            <div className="pb-24px pt-19px">
              <div className="flex justify-center flex-wrap">
                {product.properties.map((propObject, index) =>
                  <Property
                    propObject={propObject}
                    product={product}
                    key={index} /> )}
              </div>
            </div>
          }

      </div>
      <AddToCart product={product} store={store}/>
    </div>;
  }
}

export default Product;
