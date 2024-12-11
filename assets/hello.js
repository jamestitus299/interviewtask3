// import React from 'react';

// // const element = <Runner code={code} scope={scope} onRendered={handleRendered} />

// export function Hello({code}) {
//   return (
//     <div>
//         <h1>James</h1>
//       <Runner code={code} />
//     </div>
//   )
// }

import React, { ReactNode, isValidElement, createElement } from 'react';

const ContentRenderer = ({ 
  content,
  wrapperClassName = "p-4" 
}: {
  content: ReactNode | string | (() => ReactNode);
  wrapperClassName?: string;
}) => {
  const renderContent = () => {
    // If content is a function, call it
    if (typeof content === 'function') {
      return content();
    }
    
    // If content is a valid React element, render it directly
    if (isValidElement(content)) {
      return content;
    }
    
    // If content is a string, check if it's HTML
    if (typeof content === 'string') {
      if (content.trim().startsWith('<')) {
        // For HTML strings, create a div and set innerHTML
        return (
          <div 
            dangerouslySetInnerHTML={{ __html: content }}
            className="content-html"
          />
        );
      }
      // For plain strings, render as text
      return <span className="content-text">{content}</span>;
    }
    
    // Return null for unsupported content types
    return null;
  };

  return (
    <div className={wrapperClassName}>
      {renderContent()}
    </div>
  );
};

// Example usage component to demonstrate different ways to use ContentRenderer
export function Example() {
  // HTML string
  const htmlContent = '<h1>Hello World</h1><p>This is <strong>HTML</strong> content</p>';
  
  // React element
  const reactElement = (
    <div className="bg-blue-100 p-4 rounded">
      <h2>React Element</h2>
      <p>This is a React element</p>
    </div>
  );
  
  // Function that returns React element
  const renderFunction = () => (
    <div className="bg-green-100 p-4 rounded">
      <h3>Render Function</h3>
      <p>This content comes from a function</p>
    </div>
  );

  return (
    <div className="space-y-4">
      <ContentRenderer content={htmlContent} />
      <ContentRenderer content={reactElement} />
      <ContentRenderer content={renderFunction} />
      <ContentRenderer content="Plain text content" />
    </div>
  );
};

// export default Example;