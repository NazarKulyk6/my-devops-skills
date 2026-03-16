const request = require('supertest');
const app = require('./app');

afterAll((done) => {
  if (app.server) {
    app.server.close(done);
  } else {
    done();
  }
});

describe('GET /', () => {
  it('should return welcome message', async () => {
    const res = await request(app).get('/');
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toBe('Hello from Node.js DevOps App!');
  });
});

describe('GET /health', () => {
  it('should return health status', async () => {
    const res = await request(app).get('/health');
    expect(res.statusCode).toBe(200);
    expect(res.body.status).toBe('healthy');
  });
});
