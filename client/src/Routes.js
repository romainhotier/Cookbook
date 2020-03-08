class Routes {
  /**
   * @param {string} fragment
   * @param {string} base
   * @param {Boolean|Number} param
   *
   * @return {string}
   */
  static build(fragment, base, param) {
    if (false === param) {
      return fragment
    }

    if ('/' !== base.slice(-1)) {
      base = base + '/'
    }
    if (param !== undefined) {
      const regex = new RegExp(':(.+)(?=/|$)')
      fragment = (regex.test(fragment)) ? fragment.replace(regex, param) : fragment + param
    }

    return base + fragment
  }

  /**
   * @return {string}
   */
  static base() {
    return '/'
  }
}

export default Routes
