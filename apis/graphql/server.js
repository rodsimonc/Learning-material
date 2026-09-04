const { ApolloServer } = require("@apollo/server");
const { startStandaloneServer } = require("@apollo/server/standalone");

const typeDefs = `#graphql
  type Item { producto: String, cantidad: Int }
  type Pedido { fecha: String, items: [Item] }
  type Usuario { nombre: String, pedidos: [Pedido] }
  type Query { usuario(id: Int!): Usuario }
`;

const resolvers = {
  Query: {
    usuario: (_, { id }) => ({
      nombre: "Carlos",
      pedidos: [{ fecha: "2026-08-01", items: [{ producto: "Teclado", cantidad: 1 }] }],
    }),
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
startStandaloneServer(server, { listen: { port: 8004 } }).then(({ url }) =>
  console.log(`GraphQL en ${url}`)
);
