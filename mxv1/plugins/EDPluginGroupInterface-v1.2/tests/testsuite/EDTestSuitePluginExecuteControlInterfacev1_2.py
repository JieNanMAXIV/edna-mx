#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author:       Marie-Francoise Incardona (incardon@esrf.fr)
#
#    Contributing author:    Olof Svensson (svensson@esrf.fr)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

from EDTestSuite                                  import EDTestSuite

class EDTestSuitePluginExecuteControlInterfacev1_2(EDTestSuite):


    def process(self):
        self.addTestCaseFromName("EDTestCasePluginExecuteControlInterfacev1_2")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlInterfacev1_2_withXMLInput")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlInterfacev1_2_blc6")
        self.addTestCaseFromName("EDTestCasePluginExecuteControlInterfacev1_2_NtermA46")
#        self.addTestCaseFromName("EDTestCasePluginExecuteControlInterfacev1_2_303")

if __name__ == '__main__':

    edTestSuitePluginExecuteControlInterfacev1_2 = EDTestSuitePluginExecuteControlInterfacev1_2("EDTestSuitePluginExecuteControlInterfacev1_2")
    edTestSuitePluginExecuteControlInterfacev1_2.execute()

