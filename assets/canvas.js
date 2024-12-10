import React from 'react';

const reactcanvas = ({ Component }) => {
  const isValidComponent = typeof Component === 'function';

  return (
    <div>
      {isValidComponent ? (
        <Component />
      ) : (
        <p>Invalid Component. Can not render Component.</p>
      )}
    </div>
  );
};

export default reactcanvas;