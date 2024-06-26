# Development

For local development, you should have `yarn` installed. It's possible that you may not have `node` installed yet, in which case it's recommended to do so with [nvm](https://github.com/nvm-sh/nvm).

### `nvm install node`
after `nvm` is installed. As of writing, you can use `v20.8.0`.

### `npm install --global yarn`
to install `yarn` which we'll use to manage dependencies.

### `yarn` or `yarn install`
to install the dependencies.

> If you're on a mac, you cannot bind mount `node_modules` from your host machine to the docker container due to differing architectures. This is already setup on the docker compose file.
> This means that adding dependencies means you'll have to rebuild the ui image for those to be reflected on the running container.

<details>
<summary><strong>CARTO for React</strong></summary>

Welcome to CARTO for React! The best way to develop Location Intelligence Apps using CARTO Cloud Native platform + deck.gl. It will provide you a well designed structure following the best practices for modern frontend development and an integrated toolchain for testing, building and deploying your application.

To get further information about CARTO for React visit our [documentation](https://docs.carto.com/react).

This application has been kickstarted using the CARTO for React basic TypeScript template for CARTO 3.

## Available Scripts

In the project directory, you will find some scripts ready to run. Here you have the command using the Yarn package manager, which we recommend, but you can also run them with npm:

### `yarn start`

Runs the app in the development mode.

Open [http://localhost:5173/](http://localhost:5173/) to view it in the browser.

The page will reload if you make edits.

You will also see any lint errors in the console.

### `yarn build`

Builds the app for production to the `build` folder.

It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.

Your app is ready to be deployed!

See the section about [deployment](https://create-react-app.dev/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (Webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Vite documentation](https://vitejs.dev/guide/#getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
</details>


# Proxy Passing
We proxy pass `/api` and `/cors-anywhere` requests to their corresponding services. This is configured differently on dev and production.

For dev, this is configured on [vite.config.ts](./vite.config.ts) under `server.proxy`. See https://vitejs.dev/config/server-options#server-proxy for more info.

For production, this is configured on [nginx.conf](./nginx.conf) under their `location` directives. See https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass for more info.