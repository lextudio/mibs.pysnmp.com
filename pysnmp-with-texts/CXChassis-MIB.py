#
# PySNMP MIB module CXChassis-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXChassis-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
cxChassis, cxRegChasCX1000 = mibBuilder.importSymbols("CXProduct-SMI", "cxChassis", "cxRegChasCX1000")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Gauge32, MibIdentifier, Counter32, ModuleIdentity, IpAddress, Unsigned32, Integer32, Counter64, NotificationType, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Gauge32", "MibIdentifier", "Counter32", "ModuleIdentity", "IpAddress", "Unsigned32", "Integer32", "Counter64", "NotificationType", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cxChasTrapCard = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxChasTrapCard.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasTrapCard.setDescription('Control (enable or disable) the two traps; cxChasCardDownTrap and cxChasCardUpTrap. Options: disabled (1): The traps are disabled. enabled (2): The traps are enabled. Default Value: (1) ')
cxFileTargetSlot = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxFileTargetSlot.setStatus('mandatory')
if mibBuilder.loadTexts: cxFileTargetSlot.setDescription('Sets the CX1000 slot to which a file transfer from a remote IP station will take place. The setting 0 indicates the NME slot (the slot in which the agent resides).')
cxChasSubSysTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5), )
if mibBuilder.loadTexts: cxChasSubSysTable.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysTable.setDescription('The subsystem description table.')
cxChasSubSysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1), ).setIndexNames((0, "CXChassis-MIB", "cxChasSubSysSlotNb"))
if mibBuilder.loadTexts: cxChasSubSysEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysEntry.setDescription('Information about the subsystem present in the chassis. ')
cxChasSubSysSlotNb = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysSlotNb.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysSlotNb.setDescription('The destination cpu card slot number.')
cxChasSubSysDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysDesc.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysDesc.setDescription("A textual description of the system. This value should include the full name and version identification of the system's hardware type, software operating-system, and networking software. This description must contain only printable ASCII characters. Range of Values: 0 to 255 ")
cxChasSubSysObjectID = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysObjectID.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysObjectID.setDescription('An administratively-assigned object ID for this managed sub system. This object is defined in the cxRegistration branch and is used to identify the subsystem.')
cxChasSubSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysName.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysName.setDescription('An administratively-assigned name for this managed node. This name is used to identify the subsystem (cpu card) for system routing.')
cxChasSubSysServices = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysServices.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysServices.setDescription('A value which indicates the set of services that this system primarily offers. The value is a sum. This sum initially takes the value zero, then, for each Selector, S, in the range from 1 through MAXSELECTOR implemented at this node, a value of 2 raised to the S is added to the sum. A Subsystem which implements Frame Relay switch functionality only would have a value of: - 2^(SEL-FR-FIRST-PROT) + 2^(SEL-BOP-FIRST-PROT) = 2^7 + 2^11 = XXX A Subsystem which implement FRAD functionality would have a value of: - 2^(SEL-FRAD-FIRST-PROT) + 2^(SEL-FR-FIRST-PROT) + 2^(SEL-BOP-FIRST-PROT)')
cxChasSubSysVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysVersion.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysVersion.setDescription('The version of the subsystem.')
cxChasSubSysOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noresponse", 1), ("responding", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxChasSubSysOperState.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysOperState.setDescription('The operating state of the subsystem. Options: noresponse (1): The subsystem is not responding. responding (2): The subsystem is responding. ')
cxChasSubSysConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("writetoflash", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxChasSubSysConfig.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysConfig.setDescription('The action for the configuration of the subsystem. The saved configuraton will be used in the next warm start. Options: writetoflash (1): The configuration will be written to flash memory. ')
cxChasSubSysRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("warmstart-with-save", 1), ("coldstart", 2), ("warmstart-without-save", 3)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxChasSubSysRestart.setStatus('mandatory')
if mibBuilder.loadTexts: cxChasSubSysRestart.setDescription('The action to restart the subsystem. Options: warmstart-with-save (1): Warm start (with save). coldstart (2): Coldstart. warmstart-without-save (3): Warm start (without save).')
cxChasCardUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1) + (0,10)).setObjects(("CXChassis-MIB", "cxChasSubSysSlotNb"))
if mibBuilder.loadTexts: cxChasCardUpTrap.setDescription('The enterprise specifc trap indicates the card in the slot is up ')
cxChasCardDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 7, 1, 1) + (0,11)).setObjects(("CXChassis-MIB", "cxChasSubSysSlotNb"))
if mibBuilder.loadTexts: cxChasCardDownTrap.setDescription('The enterprise specific trap indicates the card in the slot is down ')
chassisMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 4, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMibLevel.setStatus('mandatory')
if mibBuilder.loadTexts: chassisMibLevel.setDescription('Used to determine current MIB module release supported by the agent. Object is in decimal.')
mibBuilder.exportSymbols("CXChassis-MIB", cxChasSubSysObjectID=cxChasSubSysObjectID, cxChasSubSysSlotNb=cxChasSubSysSlotNb, cxFileTargetSlot=cxFileTargetSlot, cxChasCardDownTrap=cxChasCardDownTrap, chassisMibLevel=chassisMibLevel, cxChasSubSysServices=cxChasSubSysServices, cxChasSubSysEntry=cxChasSubSysEntry, cxChasSubSysRestart=cxChasSubSysRestart, cxChasSubSysName=cxChasSubSysName, cxChasTrapCard=cxChasTrapCard, cxChasSubSysVersion=cxChasSubSysVersion, cxChasSubSysOperState=cxChasSubSysOperState, cxChasCardUpTrap=cxChasCardUpTrap, cxChasSubSysTable=cxChasSubSysTable, cxChasSubSysConfig=cxChasSubSysConfig, cxChasSubSysDesc=cxChasSubSysDesc)
