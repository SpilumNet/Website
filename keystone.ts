import { config, list } from '@keystone-6/core'
import { allowAll } from '@keystone-6/core/access'
import { password, relationship, select, text, timestamp } from '@keystone-6/core/fields'
import { document } from '@keystone-6/fields-document'
import { withAuth, session } from './auth'

const lists = {
    User: list({
        access: allowAll,
        fields: {
            name: text({ validation: { isRequired: true } }),
            email: text({ validation: { isRequired: true }, isIndexed: 'unique' }),
            posts: relationship({ ref: 'Post.author', many: true }),
            password: password({ validation: { isRequired: true }},)
        },
    }),
    Post: list({
        access: allowAll,
        fields: {
            title: text(),
            publishedAt: timestamp(),
            status: select({
                options: [
                    { label: 'Published', value: 'published' },
                    { label: 'Draft', value: 'draft' },
                ],
                defaultValue: 'draft',
                ui: { displayMode: 'segmented-control' },
            }),
            author: relationship({
                ref: 'User.posts',
                ui: {
                    displayMode: 'cards',
                    cardFields: ['name', 'email'],
                    inlineEdit: { fields: ['name', 'email'] },
                    linkToItem: true,
                    inlineCreate: { fields: ['name', 'email'] },
                },
                many: true,
            }),
            content: document({
                formatting: true,
                links: true,
                dividers: true,
                layouts: [
                    [1, 1],
                    [1, 1, 1],
                    [2, 1],
                    [1, 2],
                    [1, 2, 1],
                ],
            }),
        },
    }),
}

export default config(
    withAuth({
        db: {
            provider: 'sqlite',
            url: 'file:./keystone.db',
        },
        lists,
        session,
        ui: {
            isAccessAllowed: (context) => !!context.session?.data,
        },
    }),
)