#
# PySNMP MIB module Wellfleet-LNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-LNM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, ModuleIdentity, TimeTicks, mgmt, iso, Opaque, NotificationType, NotificationType, Unsigned32, mib_2, enterprises, Integer32, MibIdentifier, ObjectIdentity, Bits, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "ModuleIdentity", "TimeTicks", "mgmt", "iso", "Opaque", "NotificationType", "NotificationType", "Unsigned32", "mib-2", "enterprises", "Integer32", "MibIdentifier", "ObjectIdentity", "Bits", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfLanManagerGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfLanManagerGroup")
wfLnm = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1))
wfLnmDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmDelete.setDescription('Create/Delete parameter. Default is created. Users perform an SNMP SET operation on this object in order to create/delete the LNM Servers subsystem.')
wfLnmDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmDisable.setDescription('Enable/Disable parameter. Default is enabled. Users perform an SNMP SET operation on this object in order to enable/disable the LNM Servers subsystem.')
wfLnmState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmState.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmState.setDescription('The current state of the LNM Servers subsystem.')
wfLnmLnmSetsDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmLnmSetsDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmLnmSetsDisable.setDescription('Allow or disallow Lan Manager to SET MIB values')
wfLnmInternalLanId = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInternalLanId.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInternalLanId.setDescription('The internal LAN id matches exactly wfBrSrBaseInternalLanId in the source routing mib. It is written here, but not displayed.')
wfLnmBridgeId = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmBridgeId.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmBridgeId.setDescription('The bridge id matches exactly wfBrSrBaseBridgeId in the source routing mib. It is written here, but not displayed.')
wfLnmInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2), )
if mibBuilder.loadTexts: wfLnmInterfaceTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceTable.setDescription('table of instances')
wfLnmInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1), ).setIndexNames((0, "Wellfleet-LNM-MIB", "wfLnmInterfaceMacCircuit"))
if mibBuilder.loadTexts: wfLnmInterfaceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceEntry.setDescription('An entry in the LNM table')
wfLnmInterfaceDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceDelete.setDescription('A flag to allow an entire row to be deleted')
wfLnmInterfaceDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceDisable.setDescription('- Enable/Disable parameter. Default is enabled. - Users perform an SNMP SET operation on this - object in order to enable/disable an interface.')
wfLnmInterfaceCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceCircuit.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceCircuit.setDescription('circuit number for LLC2 - filled in by Site Man')
wfLnmInterfaceMacCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceMacCircuit.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceMacCircuit.setDescription('circuit number for MAC')
wfLnmInterfaceRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceRemoteMac.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceRemoteMac.setDescription('Site Man will suggest a value, but the user can override.')
wfLnmInterfaceLrmDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceLrmDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceLrmDisable.setDescription('LRM server can be turned on/off')
wfLnmInterfaceLrmState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLrmState.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceLrmState.setDescription('There is only a state - enabling LNM Servers automatically enables LRM')
wfLnmInterfaceLbsState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLbsState.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceLbsState.setDescription('There is no corresponding enable for LBS')
wfLnmInterfaceRemDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceRemDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceRemDisable.setDescription('REM server can be turned on/off')
wfLnmInterfaceRemState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRemState.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceRemState.setDescription('REM state parameter - can be active or not')
wfLnmInterfaceRpsDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceRpsDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceRpsDisable.setDescription('RPS server can be turned on/off')
wfLnmInterfaceRpsState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRpsState.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceRpsState.setDescription('RPS state - actively forwarding to LAN Manager, or only collecting stats')
wfLnmInterfaceCrsDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceCrsDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceCrsDisable.setDescription('CRS server can be turned on/off')
wfLnmInterfaceCrsState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceCrsState.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceCrsState.setDescription('CRS state - actively forwarding to LAN Manager, or only collecting stats')
wfLnmInterfaceCtrlMgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceCtrlMgrPswd.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceCtrlMgrPswd.setDescription('Controlling LAN Manager Password; default = all 0s')
wfLnmInterfaceOb1MgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceOb1MgrPswd.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceOb1MgrPswd.setDescription('Observing LAN Manager Password; default = all 0s')
wfLnmInterfaceOb2MgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 17), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceOb2MgrPswd.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceOb2MgrPswd.setDescription('Observing LAN Manager Password; default = all 0s')
wfLnmInterfaceOb3MgrPswd = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 18), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceOb3MgrPswd.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceOb3MgrPswd.setDescription('Observing LAN Manager Password; default = all 0s')
wfLnmInterfaceCtrlMgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceCtrlMgrMac.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceCtrlMgrMac.setDescription('Controlling LAN Manager Location; default = all 0s')
wfLnmInterfaceOb1MgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 20), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceOb1MgrMac.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceOb1MgrMac.setDescription('Observing LAN Manager Location; default = all 0s')
wfLnmInterfaceOb2MgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceOb2MgrMac.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceOb2MgrMac.setDescription('Observing LAN Manager Location; default = all 0s')
wfLnmInterfaceOb3MgrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 22), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceOb3MgrMac.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceOb3MgrMac.setDescription('Observing LAN Manager Location; default = all 0s')
wfLnmInterfaceWghtTrshld = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 256)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfLnmInterfaceWghtTrshld.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceWghtTrshld.setDescription('Error rate threshold - defaults to 128')
wfLnmInterfaceLrmCngstnErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLrmCngstnErrs.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceLrmCngstnErrs.setDescription('Measure the number of packets LRM drops')
wfLnmInterfaceLrmRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLrmRxErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceLrmRxErrors.setDescription("Measure the number of packets LRM can't parse")
wfLnmInterfaceRemRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRemRxErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceRemRxErrors.setDescription("Measure the number of packets REM can't parse")
wfLnmInterfaceRpsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceRpsRxErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceRpsRxErrors.setDescription("Measure the number of packets RPS can't parse")
wfLnmInterfaceCrsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceCrsRxErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceCrsRxErrors.setDescription("Measure the number of packets CRS can't parse")
wfLnmInterfaceLbsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 12, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfLnmInterfaceLbsRxErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfLnmInterfaceLbsRxErrors.setDescription("Measure the number of packets LBS can't parse")
mibBuilder.exportSymbols("Wellfleet-LNM-MIB", wfLnmInterfaceTable=wfLnmInterfaceTable, wfLnmInterfaceRpsDisable=wfLnmInterfaceRpsDisable, wfLnmInterfaceRpsRxErrors=wfLnmInterfaceRpsRxErrors, wfLnmDisable=wfLnmDisable, wfLnmInterfaceOb2MgrMac=wfLnmInterfaceOb2MgrMac, wfLnmInterfaceMacCircuit=wfLnmInterfaceMacCircuit, wfLnmInterfaceCircuit=wfLnmInterfaceCircuit, wfLnmInterfaceOb2MgrPswd=wfLnmInterfaceOb2MgrPswd, wfLnmInterfaceLrmState=wfLnmInterfaceLrmState, wfLnmInterfaceCtrlMgrMac=wfLnmInterfaceCtrlMgrMac, wfLnmInterfaceLbsState=wfLnmInterfaceLbsState, wfLnmInterfaceCrsDisable=wfLnmInterfaceCrsDisable, wfLnmInterfaceCrsRxErrors=wfLnmInterfaceCrsRxErrors, wfLnmInterfaceCrsState=wfLnmInterfaceCrsState, wfLnmLnmSetsDisable=wfLnmLnmSetsDisable, wfLnmInterfaceOb3MgrMac=wfLnmInterfaceOb3MgrMac, wfLnmInternalLanId=wfLnmInternalLanId, wfLnm=wfLnm, wfLnmInterfaceRemoteMac=wfLnmInterfaceRemoteMac, wfLnmInterfaceRemState=wfLnmInterfaceRemState, wfLnmInterfaceLrmRxErrors=wfLnmInterfaceLrmRxErrors, wfLnmInterfaceLbsRxErrors=wfLnmInterfaceLbsRxErrors, wfLnmInterfaceOb3MgrPswd=wfLnmInterfaceOb3MgrPswd, wfLnmState=wfLnmState, wfLnmInterfaceRemDisable=wfLnmInterfaceRemDisable, wfLnmDelete=wfLnmDelete, wfLnmInterfaceDelete=wfLnmInterfaceDelete, wfLnmInterfaceDisable=wfLnmInterfaceDisable, wfLnmInterfaceOb1MgrMac=wfLnmInterfaceOb1MgrMac, wfLnmInterfaceOb1MgrPswd=wfLnmInterfaceOb1MgrPswd, wfLnmInterfaceWghtTrshld=wfLnmInterfaceWghtTrshld, wfLnmInterfaceEntry=wfLnmInterfaceEntry, wfLnmInterfaceRpsState=wfLnmInterfaceRpsState, wfLnmInterfaceCtrlMgrPswd=wfLnmInterfaceCtrlMgrPswd, wfLnmInterfaceRemRxErrors=wfLnmInterfaceRemRxErrors, wfLnmBridgeId=wfLnmBridgeId, wfLnmInterfaceLrmCngstnErrs=wfLnmInterfaceLrmCngstnErrs, wfLnmInterfaceLrmDisable=wfLnmInterfaceLrmDisable)