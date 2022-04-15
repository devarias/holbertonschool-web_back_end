export default class Building {
  constructor(sqft) {
    const validation = typeof this.evacuationWarningMessage !== 'function';
    if (this.constructor !== Building && validation) {
      throw Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }

    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
