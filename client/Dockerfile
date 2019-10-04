FROM node:12-alpine

ENV NODE_ENV=production
ENV HOME=/app

RUN chown -R node:node $HOME
USER node

ADD . $HOME
