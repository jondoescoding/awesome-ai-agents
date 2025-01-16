const LendingContract = artifacts.require("LendingContract");

module.exports = function (deployer) {
  deployer.deploy(LendingContract);
};