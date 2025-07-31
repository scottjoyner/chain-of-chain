require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  defaultNetwork: "localhost",
  networks: {
    localhost: {
      url: "http://127.0.0.1:8545"
    },
    sepolia: {
      url: "https://sepolia.infura.io/v3/YOUR_INFURA_KEY",
      accounts: ["0xYOUR_PRIVATE_KEY"]
    }
  }
};
