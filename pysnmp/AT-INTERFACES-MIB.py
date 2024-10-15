# SNMP MIB module (AT-INTERFACES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-INTERFACES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:19 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(atRouter,
 traps) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "atRouter",
    "traps")

(InterfaceIndexOrZero,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifName")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

arInterfaces = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5)
)
arInterfaces.setRevisions(
        ("2006-06-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IgmpTraps_ObjectIdentity = ObjectIdentity
igmpTraps = _IgmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    igmpTraps.setStatus("current")
_ArBoardMaxIndex_Type = Integer32
_ArBoardMaxIndex_Object = MibScalar
arBoardMaxIndex = _ArBoardMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 1),
    _ArBoardMaxIndex_Type()
)
arBoardMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardMaxIndex.setStatus("current")
_ArBoardTable_Object = MibTable
arBoardTable = _ArBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2)
)
if mibBuilder.loadTexts:
    arBoardTable.setStatus("current")
_ArBoardEntry_Object = MibTableRow
arBoardEntry = _ArBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1)
)
arBoardEntry.setIndexNames(
    (0, "AT-INTERFACES-MIB", "arBoardIndex"),
)
if mibBuilder.loadTexts:
    arBoardEntry.setStatus("current")
_ArBoardIndex_Type = Integer32
_ArBoardIndex_Object = MibTableColumn
arBoardIndex = _ArBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 1),
    _ArBoardIndex_Type()
)
arBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardIndex.setStatus("current")
_ArBoardId_Type = ObjectIdentifier
_ArBoardId_Object = MibTableColumn
arBoardId = _ArBoardId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 2),
    _ArBoardId_Type()
)
arBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardId.setStatus("current")
_ArBoardName_Type = DisplayString
_ArBoardName_Object = MibTableColumn
arBoardName = _ArBoardName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 3),
    _ArBoardName_Type()
)
arBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardName.setStatus("current")
_ArBoardRevision_Type = DisplayString
_ArBoardRevision_Object = MibTableColumn
arBoardRevision = _ArBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 4),
    _ArBoardRevision_Type()
)
arBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardRevision.setStatus("current")
_ArBoardSerialNumber_Type = DisplayString
_ArBoardSerialNumber_Object = MibTableColumn
arBoardSerialNumber = _ArBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 5),
    _ArBoardSerialNumber_Type()
)
arBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardSerialNumber.setStatus("current")
_ArBoardTotalSlots_Type = Integer32
_ArBoardTotalSlots_Object = MibTableColumn
arBoardTotalSlots = _ArBoardTotalSlots_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 6),
    _ArBoardTotalSlots_Type()
)
arBoardTotalSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardTotalSlots.setStatus("current")
_ArBoardTotalPositions_Type = Integer32
_ArBoardTotalPositions_Object = MibTableColumn
arBoardTotalPositions = _ArBoardTotalPositions_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 2, 1, 7),
    _ArBoardTotalPositions_Type()
)
arBoardTotalPositions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arBoardTotalPositions.setStatus("current")
_ArSlotTable_Object = MibTable
arSlotTable = _ArSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3)
)
if mibBuilder.loadTexts:
    arSlotTable.setStatus("current")
_ArSlotEntry_Object = MibTableRow
arSlotEntry = _ArSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1)
)
arSlotEntry.setIndexNames(
    (0, "AT-INTERFACES-MIB", "arSlotBoardIndex"),
    (0, "AT-INTERFACES-MIB", "arSlotSlotIndex"),
)
if mibBuilder.loadTexts:
    arSlotEntry.setStatus("current")
_ArSlotBoardIndex_Type = Integer32
_ArSlotBoardIndex_Object = MibTableColumn
arSlotBoardIndex = _ArSlotBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 1),
    _ArSlotBoardIndex_Type()
)
arSlotBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotBoardIndex.setStatus("current")
_ArSlotSlotIndex_Type = Integer32
_ArSlotSlotIndex_Object = MibTableColumn
arSlotSlotIndex = _ArSlotSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 2),
    _ArSlotSlotIndex_Type()
)
arSlotSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotSlotIndex.setStatus("current")
_ArSlotHeldBoardIndex_Type = Integer32
_ArSlotHeldBoardIndex_Object = MibTableColumn
arSlotHeldBoardIndex = _ArSlotHeldBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 3),
    _ArSlotHeldBoardIndex_Type()
)
arSlotHeldBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotHeldBoardIndex.setStatus("current")
_ArSlotDescription_Type = DisplayString
_ArSlotDescription_Object = MibTableColumn
arSlotDescription = _ArSlotDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 3, 1, 4),
    _ArSlotDescription_Type()
)
arSlotDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arSlotDescription.setStatus("current")
_ArInterfaceTable_Object = MibTable
arInterfaceTable = _ArInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4)
)
if mibBuilder.loadTexts:
    arInterfaceTable.setStatus("current")
_ArInterfaceEntry_Object = MibTableRow
arInterfaceEntry = _ArInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1)
)
arInterfaceEntry.setIndexNames(
    (0, "AT-INTERFACES-MIB", "arInterfaceBoardIndex"),
    (0, "AT-INTERFACES-MIB", "arInterfacePosition"),
)
if mibBuilder.loadTexts:
    arInterfaceEntry.setStatus("current")
_ArInterfaceBoardIndex_Type = Integer32
_ArInterfaceBoardIndex_Object = MibTableColumn
arInterfaceBoardIndex = _ArInterfaceBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 1),
    _ArInterfaceBoardIndex_Type()
)
arInterfaceBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceBoardIndex.setStatus("current")
_ArInterfacePosition_Type = Integer32
_ArInterfacePosition_Object = MibTableColumn
arInterfacePosition = _ArInterfacePosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 2),
    _ArInterfacePosition_Type()
)
arInterfacePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfacePosition.setStatus("current")
_ArInterfaceIfIndex_Type = InterfaceIndexOrZero
_ArInterfaceIfIndex_Object = MibTableColumn
arInterfaceIfIndex = _ArInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 3),
    _ArInterfaceIfIndex_Type()
)
arInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceIfIndex.setStatus("current")
_ArInterfaceName_Type = DisplayString
_ArInterfaceName_Object = MibTableColumn
arInterfaceName = _ArInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 4),
    _ArInterfaceName_Type()
)
arInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceName.setStatus("current")
_ArInterfaceFullName_Type = DisplayString
_ArInterfaceFullName_Object = MibTableColumn
arInterfaceFullName = _ArInterfaceFullName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 4, 1, 5),
    _ArInterfaceFullName_Type()
)
arInterfaceFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arInterfaceFullName.setStatus("current")
_ArIfXTable_Object = MibTable
arIfXTable = _ArIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5)
)
if mibBuilder.loadTexts:
    arIfXTable.setStatus("current")
_ArIfXEntry_Object = MibTableRow
arIfXEntry = _ArIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1)
)
arIfXEntry.setIndexNames(
    (0, "AT-INTERFACES-MIB", "arIfXIndex"),
)
if mibBuilder.loadTexts:
    arIfXEntry.setStatus("current")
_ArIfXIndex_Type = Integer32
_ArIfXIndex_Object = MibTableColumn
arIfXIndex = _ArIfXIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 1),
    _ArIfXIndex_Type()
)
arIfXIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXIndex.setStatus("current")
_ArIfXAverageInputBitsSecond_Type = Integer32
_ArIfXAverageInputBitsSecond_Object = MibTableColumn
arIfXAverageInputBitsSecond = _ArIfXAverageInputBitsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 2),
    _ArIfXAverageInputBitsSecond_Type()
)
arIfXAverageInputBitsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageInputBitsSecond.setStatus("current")
_ArIfXAverageInputPacketsSecond_Type = Integer32
_ArIfXAverageInputPacketsSecond_Object = MibTableColumn
arIfXAverageInputPacketsSecond = _ArIfXAverageInputPacketsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 3),
    _ArIfXAverageInputPacketsSecond_Type()
)
arIfXAverageInputPacketsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageInputPacketsSecond.setStatus("current")
_ArIfXAverageOutputBitsSecond_Type = Integer32
_ArIfXAverageOutputBitsSecond_Object = MibTableColumn
arIfXAverageOutputBitsSecond = _ArIfXAverageOutputBitsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 4),
    _ArIfXAverageOutputBitsSecond_Type()
)
arIfXAverageOutputBitsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageOutputBitsSecond.setStatus("current")
_ArIfXAverageOutputPacketsSecond_Type = Integer32
_ArIfXAverageOutputPacketsSecond_Object = MibTableColumn
arIfXAverageOutputPacketsSecond = _ArIfXAverageOutputPacketsSecond_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5, 5, 1, 5),
    _ArIfXAverageOutputPacketsSecond_Type()
)
arIfXAverageOutputPacketsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arIfXAverageOutputPacketsSecond.setStatus("current")

# Managed Objects groups


# Notification objects

igmpGeneralQueryNotReceivedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2, 1, 1)
)
igmpGeneralQueryNotReceivedEvent.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    igmpGeneralQueryNotReceivedEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-INTERFACES-MIB",
    **{"igmpTraps": igmpTraps,
       "igmpGeneralQueryNotReceivedEvent": igmpGeneralQueryNotReceivedEvent,
       "arInterfaces": arInterfaces,
       "arBoardMaxIndex": arBoardMaxIndex,
       "arBoardTable": arBoardTable,
       "arBoardEntry": arBoardEntry,
       "arBoardIndex": arBoardIndex,
       "arBoardId": arBoardId,
       "arBoardName": arBoardName,
       "arBoardRevision": arBoardRevision,
       "arBoardSerialNumber": arBoardSerialNumber,
       "arBoardTotalSlots": arBoardTotalSlots,
       "arBoardTotalPositions": arBoardTotalPositions,
       "arSlotTable": arSlotTable,
       "arSlotEntry": arSlotEntry,
       "arSlotBoardIndex": arSlotBoardIndex,
       "arSlotSlotIndex": arSlotSlotIndex,
       "arSlotHeldBoardIndex": arSlotHeldBoardIndex,
       "arSlotDescription": arSlotDescription,
       "arInterfaceTable": arInterfaceTable,
       "arInterfaceEntry": arInterfaceEntry,
       "arInterfaceBoardIndex": arInterfaceBoardIndex,
       "arInterfacePosition": arInterfacePosition,
       "arInterfaceIfIndex": arInterfaceIfIndex,
       "arInterfaceName": arInterfaceName,
       "arInterfaceFullName": arInterfaceFullName,
       "arIfXTable": arIfXTable,
       "arIfXEntry": arIfXEntry,
       "arIfXIndex": arIfXIndex,
       "arIfXAverageInputBitsSecond": arIfXAverageInputBitsSecond,
       "arIfXAverageInputPacketsSecond": arIfXAverageInputPacketsSecond,
       "arIfXAverageOutputBitsSecond": arIfXAverageOutputBitsSecond,
       "arIfXAverageOutputPacketsSecond": arIfXAverageOutputPacketsSecond}
)
