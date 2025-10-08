{
  description = "A Django application.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ poetry2nix.overlay ];
        };
        pythonEnv = pkgs.poetry2nix.mkPoetryEnv {
          projectDir = ./.;
        };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            pythonEnv
            pkgs.just
          ];
        };
      });
}