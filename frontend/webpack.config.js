{
    module.rules = [
        {
            test: /\.pug$/,
            oneOf: [
                // this applies to pug imports inside JavaScript
                {
                    exclude: /\.vue$/,
                    use: ['raw-loader', 'pug-plain-loader']
                },
                // this applies to <template lang="pug"> in Vue components
                {
                    use: ['pug-plain-loader']
                }
            ]
        }
    ]
}