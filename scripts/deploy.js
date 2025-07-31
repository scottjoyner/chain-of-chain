const hre = require("hardhat");

async function main() {
  const ThoughtChain = await hre.ethers.getContractFactory("ThoughtChainV2");
  const thoughtChain = await ThoughtChain.deploy();

  await thoughtChain.deployed();

  console.log("ThoughtChainV2 deployed to:", thoughtChain.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
