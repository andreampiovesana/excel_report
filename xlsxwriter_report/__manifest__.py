###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'XLSX report',
    'version': '0.1',
    'category': 'Report',
    'description': '''  
        Better manage python xlsxwriter report
        ''',
    'summary': 'Excel, utility, report',
    'author': 'Micronaet S.r.l. - Nicola Riolini',
    'website': 'http://www.micronaet.it',
    'license': 'AGPL-3',
    'depends': [
        'base',
        ],
    'init_xml': [],
    'demo': [],
    'data': [
        #'data/config_data.xml',
        'security/ir.model.access.csv',
        
        'views/excel_report_view.xml',

        # Data: 
        'data/color_data.xml',
        'data/border_data.xml',
        'data/font_data.xml',
        'data/page_data.xml',

        'data/format_data.xml',
        'data/style_data.xml',
        ],
    'external_dependencies': {
        'python': ['xlsxwriter'],
        },
    'active': False,
    'installable': True,
    'auto_install': False,
    }
