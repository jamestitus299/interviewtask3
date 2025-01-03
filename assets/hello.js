import React, {
  useState,
  useEffect,
  useContext,
  useReducer,
  useRef,
  useMemo,
  useCallback,
} from "react";
import {
  LiveProvider,
  LiveEditor,
  LiveError,
  LivePreview,
} from "react-live-runner";

export function Hello({ code }) {
  // const code = "<h1>James Titus</h1>";
  const scope = {
    React,
    useState,
    useEffect,
    useContext,
    useReducer,
    useRef,
    useMemo,
    useCallback,
  };
  // console.log(code);
  return (
    <div
      className="container rounded"
      style={{ height: "70vh", width: "55vw", overflow: "auto" }}
    >
      <LiveProvider code={code} scope={scope}>
        <div className="d-flex flex-column flex-lg-row h-100">
          <div
            className="rounded p-2 mb-3 mb-lg-0 me-lg-3"
            style={{ height: "70vh", width:"100%", flex: "1", overflow: "auto" }}
          >
            <LivePreview />
          </div>
          <div
            className="rounded p-2"
            style={{ height: "70vh", flex: "1", overflow: "auto" }}
          >
            <LiveEditor />
          </div>
        </div>
        <div className="text-danger mt-3">
          <LiveError />
        </div>
      </LiveProvider>
    </div>
  );
}
