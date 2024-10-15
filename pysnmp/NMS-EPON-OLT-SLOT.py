# SNMP MIB module (NMS-EPON-OLT-SLOT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-OLT-SLOT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:46 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOltSlot_ObjectIdentity = ObjectIdentity
nmsEponOltSlot = _NmsEponOltSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 21)
)
_NmsEponOltSlotTable_Object = MibTable
nmsEponOltSlotTable = _NmsEponOltSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1)
)
if mibBuilder.loadTexts:
    nmsEponOltSlotTable.setStatus("mandatory")
_NmsEponOltSlotEntry_Object = MibTableRow
nmsEponOltSlotEntry = _NmsEponOltSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1)
)
nmsEponOltSlotEntry.setIndexNames(
    (0, "NMS-EPON-OLT-SLOT", "oltSlotIndex"),
)
if mibBuilder.loadTexts:
    nmsEponOltSlotEntry.setStatus("mandatory")
_OltSlotIndex_Type = Integer32
_OltSlotIndex_Object = MibTableColumn
oltSlotIndex = _OltSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 1),
    _OltSlotIndex_Type()
)
oltSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltSlotIndex.setStatus("mandatory")
_OltSlotHelloInterval_Type = Integer32
_OltSlotHelloInterval_Object = MibTableColumn
oltSlotHelloInterval = _OltSlotHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 2),
    _OltSlotHelloInterval_Type()
)
oltSlotHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltSlotHelloInterval.setStatus("mandatory")
_OltSlotDeadInterval_Type = Integer32
_OltSlotDeadInterval_Object = MibTableColumn
oltSlotDeadInterval = _OltSlotDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 3),
    _OltSlotDeadInterval_Type()
)
oltSlotDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltSlotDeadInterval.setStatus("mandatory")
_OltSlotChipsRegisteredNumber_Type = Integer32
_OltSlotChipsRegisteredNumber_Object = MibTableColumn
oltSlotChipsRegisteredNumber = _OltSlotChipsRegisteredNumber_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 21, 1, 1, 4),
    _OltSlotChipsRegisteredNumber_Type()
)
oltSlotChipsRegisteredNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltSlotChipsRegisteredNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-OLT-SLOT",
    **{"nmsEponOltSlot": nmsEponOltSlot,
       "nmsEponOltSlotTable": nmsEponOltSlotTable,
       "nmsEponOltSlotEntry": nmsEponOltSlotEntry,
       "oltSlotIndex": oltSlotIndex,
       "oltSlotHelloInterval": oltSlotHelloInterval,
       "oltSlotDeadInterval": oltSlotDeadInterval,
       "oltSlotChipsRegisteredNumber": oltSlotChipsRegisteredNumber}
)
