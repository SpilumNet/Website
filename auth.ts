import { createAuth } from '@keystone-6/auth'
import { statelessSessions } from '@keystone-6/core/session';

const { withAuth } = createAuth({
    listKey: 'User',
    identityField: 'email',
    sessionData: 'name',
    secretField: 'password',
    initFirstItem: {
        fields: ['name', 'email', 'password'],
    },
})

let sessionSecret = '----------SECRET-HERE-----------'
let sessionMaxAge = 60 * 60 * 24

const session = statelessSessions({
    maxAge: sessionMaxAge,
    secret: sessionSecret,
})

export { withAuth, session }