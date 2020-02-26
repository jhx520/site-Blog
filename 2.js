
  class ChangeBackground {
    constructor() {
      this.init();
    };
    init() {
      this.addStyle(`
        html, body {
          background-color: #000 !important;
        }
        * {
          color: #CCD1D9 !important;
          box-shadow: none !important;
        }
        *:after, *:before {
          border-color: #1e1e1e !important;
          color: #CCD1D9 !important;
          box-shadow: none !important;
          background-color: transparent !important;
        }
        a, a > *{
          color: #409B9B !important;
        }
        [data-change-border-color][data-change-border-color-important] {
          border-color: #1e1e1e !important;
        }
        [data-change-background-color][data-change-background-color-important] {
          background-color: #000 !important;
        }
      `);
      this.selectAllNodes(node => {
        if (node.nodeType !== 1) {
          return;
        };
        const style = window.getComputedStyle(node, null);
        const whiteList = ['rgba(0, 0, 0, 0)', 'transparent'];
        const backgroundColor = style.getPropertyValue('background-color');
        const borderColor = style.getPropertyValue('border-color');
        if (whiteList.indexOf(backgroundColor) < 0) {
          if (this.isWhiteToBlack(backgroundColor)) {
            node.dataset.changeBackgroundColor = '';
            node.dataset.changeBackgroundColorImportant = '';
          } else {
            delete node.dataset.changeBackgroundColor;
            delete node.dataset.changeBackgroundColorImportant;
          };
        };
        if (whiteList.indexOf(borderColor) < 0) {
          if (this.isWhiteToBlack(borderColor)) {
            node.dataset.changeBorderColor = '';
            node.dataset.changeBorderColorImportant = '';
          } else {
            delete node.dataset.changeBorderColor;
            delete node.dataset.changeBorderColorImportant;
          };
        };
        if (borderColor.indexOf('rgb(255, 255, 255)') >= 0) {
          delete node.dataset.changeBorderColor;
          delete node.dataset.changeBorderColorImportant;
          node.style.borderColor = 'transparent';
        };
      });
    };
    addStyle(style = '') {
      const styleElm = document.createElement('style');
      styleElm.innerHTML = style;
      document.head.appendChild(styleElm);
    };
    /* 是否为灰白黑 */
    isWhiteToBlack(colorStr = '') {
      let hasWhiteToBlack = false;
      const colorArr = colorStr.match(/rgb.+?\)/g);
      if (!colorArr || colorArr.length === 0) {
        return true;
      };
      colorArr.forEach(color => {
        const reg = /rgb[a]*?\(([0-9]+),.*?([0-9]+),.*?([0-9]+).*?\)/g;
        const result = reg.exec(color);
        const red = result[1];
        const green = result[2];
        const blue = result[3];
        const deviation = 20;
        const max = Math.max(red, green, blue);
        const min = Math.min(red, green, blue);
        if (max - min <= deviation) {
          hasWhiteToBlack = true;
        };
      });
      return hasWhiteToBlack;
    };
    selectAllNodes(callback = () => { }) {
      const allNodes = document.querySelectorAll('*');
      Array.from(allNodes, node => {
        callback(node);
      });
      this.observe({
        targetNode: document.documentElement,
        config: {
          attributes: false
        },
        callback(mutations, observer) {
          const allNodes = document.querySelectorAll('*');
          Array.from(allNodes, node => {
            callback(node);
          });
        }
      });
    };
    observe({ targetNode, config = {}, callback = () => { } }) {
      if (!targetNode) {
        return;
      };

      config = Object.assign({
        attributes: true,
        childList: true,
        subtree: true
      }, config);

      const observer = new MutationObserver(callback);
      observer.observe(targetNode, config);
    };
  };
  new ChangeBackground();
})();