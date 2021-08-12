'use strict';

module.exports = function(electronApp, menuState) {
  return [{
    label: 'Toggle Klotz Detection',
    accelerator: 'CommandOrControl+k',
    enabled: function() {
      return true;
    },
    action: function() {
      electronApp.emit('menu:action', 'toggle-klotz-detection');
    }
  }];
};
