import React from 'react';
import { render } from '@testing-library/react';
import { shallow } from 'enzyme'
import Layout from './Layout.component';

describe('Layout.component', () => {
    it('should if Layout is present in the page', () => {
        const wrapper = shallow(<Layout />)
      
        expect(wrapper.find('.layout').length).toEqual(1)
      })
});
