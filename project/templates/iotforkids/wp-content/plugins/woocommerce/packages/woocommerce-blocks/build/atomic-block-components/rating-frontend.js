(window.webpackWcBlocksJsonp=window.webpackWcBlocksJsonp||[]).push([[7],{336:function(t,e){},347:function(t,e,a){"use strict";a.r(e);var c=a(5),n=a.n(c),r=(a(9),a(1)),o=a(3),s=a.n(o),u=a(107),i=a(252),l=(a(336),function(t){var e=parseFloat(t.average_rating);return Number.isFinite(e)&&e>0?e:0});e.default=Object(i.withProductDataContext)((function(t){var e=t.className,a=Object(u.useInnerBlockLayoutContext)().parentClassName,c=Object(u.useProductDataContext)().product,o=l(c);if(!o)return null;var i={width:o/5*100+"%"},p=Object(r.sprintf)(
/* translators: %f is referring to the average rating value */
Object(r.__)("Rated %f out of 5",'woocommerce'),o);return React.createElement("div",{className:s()(e,"wc-block-components-product-rating",n()({},"".concat(a,"__product-rating"),a))},React.createElement("div",{className:s()("wc-block-components-product-rating__stars","".concat(a,"__product-rating__stars")),role:"img","aria-label":p},React.createElement("span",{style:i},p)))}))}}]);