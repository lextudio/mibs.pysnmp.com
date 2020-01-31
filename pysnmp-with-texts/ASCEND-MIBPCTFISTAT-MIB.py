#
# PySNMP MIB module ASCEND-MIBPCTFISTAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBPCTFISTAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, MibIdentifier, Integer32, NotificationType, Unsigned32, ObjectIdentity, Gauge32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "MibIdentifier", "Integer32", "NotificationType", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibpctfiLineStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 19))
mibpctfiLineStatusTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 19, 1), )
if mibBuilder.loadTexts: mibpctfiLineStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibpctfiLineStatusTable.setDescription('A list of mibpctfiLineStatus profile entries.')
mibpctfiLineStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1), ).setIndexNames((0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-Shelf-o"), (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-Slot-o"), (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-Item-o"))
if mibBuilder.loadTexts: mibpctfiLineStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibpctfiLineStatusEntry.setDescription('A mibpctfiLineStatus entry containing objects that maps to the parameters of mibpctfiLineStatus profile.')
pctfiLineStatus_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 1), Integer32()).setLabel("pctfiLineStatus-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pctfiLineStatus_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_Shelf_o.setDescription('')
pctfiLineStatus_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 2), Integer32()).setLabel("pctfiLineStatus-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pctfiLineStatus_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_Slot_o.setDescription('')
pctfiLineStatus_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 3), Integer32()).setLabel("pctfiLineStatus-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pctfiLineStatus_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_Item_o.setDescription('')
pctfiLineStatus_PhysicalAddress_Shelf = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("anyShelf", 1), ("shelf1", 2), ("shelf2", 3), ("shelf3", 4), ("shelf4", 5), ("shelf5", 6), ("shelf6", 7), ("shelf7", 8), ("shelf8", 9), ("shelf9", 10)))).setLabel("pctfiLineStatus-PhysicalAddress-Shelf").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_PhysicalAddress_Shelf.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_PhysicalAddress_Shelf.setDescription('The number of the shelf that the addressed physical device resides on.')
pctfiLineStatus_PhysicalAddress_Slot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 55, 56, 57, 58, 49, 50, 42, 53, 54, 45, 46, 51, 59))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot8", 9), ("slot9", 10), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17), ("slot17", 18), ("slot18", 19), ("slot19", 20), ("slot20", 21), ("slot21", 22), ("slot22", 23), ("slot23", 24), ("slot24", 25), ("slot25", 26), ("slot26", 27), ("slot27", 28), ("slot28", 29), ("slot29", 30), ("slot30", 31), ("slot31", 32), ("slot32", 33), ("slot33", 34), ("slot34", 35), ("slot35", 36), ("slot36", 37), ("slot37", 38), ("slot38", 39), ("slot39", 40), ("slot40", 41), ("aLim", 55), ("bLim", 56), ("cLim", 57), ("dLim", 58), ("leftController", 49), ("rightController", 50), ("controller", 42), ("firstControlModule", 53), ("secondControlModule", 54), ("trunkModule1", 45), ("trunkModule2", 46), ("controlModule", 51), ("slotPrimary", 59)))).setLabel("pctfiLineStatus-PhysicalAddress-Slot").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_PhysicalAddress_Slot.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_PhysicalAddress_Slot.setDescription('The number of the slot that the addressed physical device resides on.')
pctfiLineStatus_PhysicalAddress_ItemNumber = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 6), Integer32()).setLabel("pctfiLineStatus-PhysicalAddress-ItemNumber").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_PhysicalAddress_ItemNumber.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_PhysicalAddress_ItemNumber.setDescription('A number that specifies an addressable entity within the context of shelf and slot.')
pctfiLineStatus_Link0Status = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("available", 2), ("unavailable", 3)))).setLabel("pctfiLineStatus-Link0Status").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_Link0Status.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_Link0Status.setDescription('The Status of the PCTFI link.')
pctfiLineStatus_Link1Status = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("available", 2), ("unavailable", 3)))).setLabel("pctfiLineStatus-Link1Status").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_Link1Status.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_Link1Status.setDescription('The Status of the PCTFI link.')
pctfiLineStatus_SideSelect = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("side0", 1), ("side1", 2)))).setLabel("pctfiLineStatus-SideSelect").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_SideSelect.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_SideSelect.setDescription('The selected side of the PCTFI link.')
pctfiLineStatus_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("pctfiLineStatus-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_Action_o.setDescription('')
mibpctfiLineStatus_VirtualDs1LineStatusTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 19, 2), ).setLabel("mibpctfiLineStatus-VirtualDs1LineStatusTable")
if mibBuilder.loadTexts: mibpctfiLineStatus_VirtualDs1LineStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibpctfiLineStatus_VirtualDs1LineStatusTable.setDescription('A list of mibpctfiLineStatus__virtual_ds1_line_status profile entries.')
mibpctfiLineStatus_VirtualDs1LineStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1), ).setLabel("mibpctfiLineStatus-VirtualDs1LineStatusEntry").setIndexNames((0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Shelf-o"), (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Slot-o"), (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Item-o"), (0, "ASCEND-MIBPCTFISTAT-MIB", "pctfiLineStatus-VirtualDs1LineStatus-Index-o"))
if mibBuilder.loadTexts: mibpctfiLineStatus_VirtualDs1LineStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibpctfiLineStatus_VirtualDs1LineStatusEntry.setDescription('A mibpctfiLineStatus__virtual_ds1_line_status entry containing objects that maps to the parameters of mibpctfiLineStatus__virtual_ds1_line_status profile.')
pctfiLineStatus_VirtualDs1LineStatus_Shelf_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 1), Integer32()).setLabel("pctfiLineStatus-VirtualDs1LineStatus-Shelf-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Shelf_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Shelf_o.setDescription('')
pctfiLineStatus_VirtualDs1LineStatus_Slot_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 2), Integer32()).setLabel("pctfiLineStatus-VirtualDs1LineStatus-Slot-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Slot_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Slot_o.setDescription('')
pctfiLineStatus_VirtualDs1LineStatus_Item_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 3), Integer32()).setLabel("pctfiLineStatus-VirtualDs1LineStatus-Item-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Item_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Item_o.setDescription('')
pctfiLineStatus_VirtualDs1LineStatus_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 4), Integer32()).setLabel("pctfiLineStatus-VirtualDs1LineStatus-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_Index_o.setDescription('')
pctfiLineStatus_VirtualDs1LineStatus_TrunkState = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unused", 1), ("nonOperational", 2), ("operational", 3), ("unequipped", 4)))).setLabel("pctfiLineStatus-VirtualDs1LineStatus-TrunkState").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_TrunkState.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_TrunkState.setDescription('The state of the PCTFI link tributary trunk according to F2 and F3.')
pctfiLineStatus_VirtualDs1LineStatus_F4BitState = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 19, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nonCas", 1), ("cas", 2)))).setLabel("pctfiLineStatus-VirtualDs1LineStatus-F4BitState").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_F4BitState.setStatus('mandatory')
if mibBuilder.loadTexts: pctfiLineStatus_VirtualDs1LineStatus_F4BitState.setDescription('The state of the PCTFI link tributary F4 bit.')
mibBuilder.exportSymbols("ASCEND-MIBPCTFISTAT-MIB", pctfiLineStatus_Link0Status=pctfiLineStatus_Link0Status, pctfiLineStatus_PhysicalAddress_Slot=pctfiLineStatus_PhysicalAddress_Slot, pctfiLineStatus_VirtualDs1LineStatus_F4BitState=pctfiLineStatus_VirtualDs1LineStatus_F4BitState, pctfiLineStatus_VirtualDs1LineStatus_Index_o=pctfiLineStatus_VirtualDs1LineStatus_Index_o, mibpctfiLineStatusEntry=mibpctfiLineStatusEntry, pctfiLineStatus_Slot_o=pctfiLineStatus_Slot_o, pctfiLineStatus_PhysicalAddress_Shelf=pctfiLineStatus_PhysicalAddress_Shelf, pctfiLineStatus_VirtualDs1LineStatus_Shelf_o=pctfiLineStatus_VirtualDs1LineStatus_Shelf_o, pctfiLineStatus_VirtualDs1LineStatus_TrunkState=pctfiLineStatus_VirtualDs1LineStatus_TrunkState, mibpctfiLineStatus=mibpctfiLineStatus, pctfiLineStatus_Shelf_o=pctfiLineStatus_Shelf_o, pctfiLineStatus_SideSelect=pctfiLineStatus_SideSelect, mibpctfiLineStatusTable=mibpctfiLineStatusTable, pctfiLineStatus_Action_o=pctfiLineStatus_Action_o, pctfiLineStatus_PhysicalAddress_ItemNumber=pctfiLineStatus_PhysicalAddress_ItemNumber, pctfiLineStatus_VirtualDs1LineStatus_Item_o=pctfiLineStatus_VirtualDs1LineStatus_Item_o, pctfiLineStatus_Item_o=pctfiLineStatus_Item_o, mibpctfiLineStatus_VirtualDs1LineStatusEntry=mibpctfiLineStatus_VirtualDs1LineStatusEntry, pctfiLineStatus_Link1Status=pctfiLineStatus_Link1Status, mibpctfiLineStatus_VirtualDs1LineStatusTable=mibpctfiLineStatus_VirtualDs1LineStatusTable, DisplayString=DisplayString, pctfiLineStatus_VirtualDs1LineStatus_Slot_o=pctfiLineStatus_VirtualDs1LineStatus_Slot_o)