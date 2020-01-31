#
# PySNMP MIB module TIMETRA-SAS-GLOBAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-SAS-GLOBAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:21:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, IpAddress, Integer32, ModuleIdentity, ObjectIdentity, iso, Unsigned32, Counter64, MibIdentifier, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "IpAddress", "Integer32", "ModuleIdentity", "ObjectIdentity", "iso", "Unsigned32", "Counter64", "MibIdentifier", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tmnxBasedProducts, = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxBasedProducts")
timetraSASGlobalMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 1))
timetraSASGlobalMIBModule.setRevisions(('1908-01-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: timetraSASGlobalMIBModule.setRevisionsDescriptions(('Rev 1.0 09 Jan 2008 00:00 This is the 1.0 release of the TIMETRA-SAS-GLOBAL-MIB.',))
if mibBuilder.loadTexts: timetraSASGlobalMIBModule.setLastUpdated('0801090000Z')
if mibBuilder.loadTexts: timetraSASGlobalMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: timetraSASGlobalMIBModule.setContactInfo('Alcatel 7x50 Support Web: http://www.alcatel.com/comps/pages/carrier_support.jhtml')
if mibBuilder.loadTexts: timetraSASGlobalMIBModule.setDescription("This document is the SNMP MIB module for central registration of object identifiers defined under the Alcatel 'timetra' branch for the Alcatel 7210 SAS series SNMP MIBs. Copyright 2003-2013 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel's proprietary intellectual property. Alcatel retains all title and ownership in the Specification, including any revisions. Alcatel grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied `as is', and Alcatel makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
timetraServiceAccessSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2))
timetraSASRegistry = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1))
timetraSASModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1))
timetraSASMIBModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 3))
timetraSASCapabilityModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4))
timetraSASE7210CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 1))
timetraSASM7210CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 2))
timetraSASX7210CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 3))
timetraSASD7210CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 4))
timetraSAST7210CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 5))
timetraSASR7210CapModule = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 4, 6))
timetraSAS7210ServiceAccessSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2))
timetraSASModel7210SASEReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 1))
if mibBuilder.loadTexts: timetraSASModel7210SASEReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASEReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-E device.')
timetraSASModel7210SASM = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2))
timetraSASModel7210SASMReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2, 1))
if mibBuilder.loadTexts: timetraSASModel7210SASMReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASMReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-M device.')
timetraSASModel7210SASM24F2XPReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2, 2))
if mibBuilder.loadTexts: timetraSASModel7210SASM24F2XPReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASM24F2XPReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-M 24F 2XP device.')
timetraSASModel7210SASM24F2XPETRReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 2, 3))
if mibBuilder.loadTexts: timetraSASModel7210SASM24F2XPETRReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASM24F2XPETRReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-M 24F 2XP ETR device.')
timetraSASModel7210SASX = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 3))
timetraSASModel7210SASX24F2XPReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 3, 1))
if mibBuilder.loadTexts: timetraSASModel7210SASX24F2XPReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASX24F2XPReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-X device.')
timetraSASModel7210SASD = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 4))
timetraSASModel7210SASDReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 4, 1))
if mibBuilder.loadTexts: timetraSASModel7210SASDReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASDReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-D device.')
timetraSASModel7210SASDETRReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 4, 2))
if mibBuilder.loadTexts: timetraSASModel7210SASDETRReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASDETRReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-D ETR device.')
timetraSASModel7210SAST = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 5))
timetraSASModel7210SASTReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 5, 1))
if mibBuilder.loadTexts: timetraSASModel7210SASTReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASTReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-T device.')
timetraSASModel7210SASTETRReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 5, 2))
if mibBuilder.loadTexts: timetraSASModel7210SASTETRReg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASTETRReg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-T ETR device.')
timetraSASModel7210SASR = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 6))
timetraSASModel7210SASR6Reg = ObjectIdentity((1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 2, 6, 1))
if mibBuilder.loadTexts: timetraSASModel7210SASR6Reg.setStatus('current')
if mibBuilder.loadTexts: timetraSASModel7210SASR6Reg.setDescription('This objectID is to be used as the mib-2 sysObjID to identify the Alcatel-Lucent 7210 SAS-R six slot device.')
timetraSASMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2))
timetraSASConfs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1))
timetraSASObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2))
timetraSASNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3))
timetraSASProductCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3))
timetraSAS7210Capability = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1))
timetraSAS7210V1v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 1))
timetraSAS7210V1v1 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 2))
timetraSAS7210V2v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 3))
timetraSAS7210V3v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 4))
timetraSAS7210V4v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 5))
timetraSAS7210V5v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 6))
timetraSAS7210V6v0 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 6, 2, 3, 1, 7))
mibBuilder.exportSymbols("TIMETRA-SAS-GLOBAL-MIB", timetraSASModel7210SASX24F2XPReg=timetraSASModel7210SASX24F2XPReg, timetraSASProductCapability=timetraSASProductCapability, timetraSASModel7210SASDETRReg=timetraSASModel7210SASDETRReg, timetraSAS7210V4v0=timetraSAS7210V4v0, timetraServiceAccessSwitches=timetraServiceAccessSwitches, timetraSAS7210V6v0=timetraSAS7210V6v0, timetraSASModel7210SASTReg=timetraSASModel7210SASTReg, timetraSASRegistry=timetraSASRegistry, timetraSASMIB=timetraSASMIB, timetraSAS7210ServiceAccessSwitches=timetraSAS7210ServiceAccessSwitches, timetraSASModules=timetraSASModules, timetraSASModel7210SASM24F2XPETRReg=timetraSASModel7210SASM24F2XPETRReg, timetraSASModel7210SASDReg=timetraSASModel7210SASDReg, timetraSASModel7210SASR=timetraSASModel7210SASR, PYSNMP_MODULE_ID=timetraSASGlobalMIBModule, timetraSASObjs=timetraSASObjs, timetraSAST7210CapModule=timetraSAST7210CapModule, timetraSASM7210CapModule=timetraSASM7210CapModule, timetraSAS7210V1v1=timetraSAS7210V1v1, timetraSAS7210V3v0=timetraSAS7210V3v0, timetraSAS7210Capability=timetraSAS7210Capability, timetraSASModel7210SASX=timetraSASModel7210SASX, timetraSAS7210V5v0=timetraSAS7210V5v0, timetraSASModel7210SASR6Reg=timetraSASModel7210SASR6Reg, timetraSASGlobalMIBModule=timetraSASGlobalMIBModule, timetraSAS7210V2v0=timetraSAS7210V2v0, timetraSASModel7210SASD=timetraSASModel7210SASD, timetraSASModel7210SASM=timetraSASModel7210SASM, timetraSASX7210CapModule=timetraSASX7210CapModule, timetraSASModel7210SAST=timetraSASModel7210SAST, timetraSASD7210CapModule=timetraSASD7210CapModule, timetraSASMIBModules=timetraSASMIBModules, timetraSASCapabilityModule=timetraSASCapabilityModule, timetraSASE7210CapModule=timetraSASE7210CapModule, timetraSASModel7210SASMReg=timetraSASModel7210SASMReg, timetraSAS7210V1v0=timetraSAS7210V1v0, timetraSASNotifyPrefix=timetraSASNotifyPrefix, timetraSASConfs=timetraSASConfs, timetraSASModel7210SASEReg=timetraSASModel7210SASEReg, timetraSASR7210CapModule=timetraSASR7210CapModule, timetraSASModel7210SASM24F2XPReg=timetraSASModel7210SASM24F2XPReg, timetraSASModel7210SASTETRReg=timetraSASModel7210SASTETRReg)