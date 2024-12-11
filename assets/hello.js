import React from 'react';
import { Runner } from 'react-runner'

// const element = <Runner code={code} scope={scope} onRendered={handleRendered} />

export function Hello({code}) {
  return (
    <div>
        <h1>James</h1>
      <Runner code={code} />
    </div>
  )
}