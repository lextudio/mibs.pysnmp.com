# SNMP MIB module (XEDIA-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:52 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 40)
)


# Types definitions



class Unsigned32(Gauge32):
    """Custom type Unsigned32 based on Gauge32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XifObjects_ObjectIdentity = ObjectIdentity
xifObjects = _XifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 40, 1)
)
_XifNextIndex_Type = Integer32
_XifNextIndex_Object = MibScalar
xifNextIndex = _XifNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 1),
    _XifNextIndex_Type()
)
xifNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xifNextIndex.setStatus("current")
_XifTable_Object = MibTable
xifTable = _XifTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2)
)
if mibBuilder.loadTexts:
    xifTable.setStatus("current")
_XifEntry_Object = MibTableRow
xifEntry = _XifEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2, 1)
)
xifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xifEntry.setStatus("current")
_XifRowStatus_Type = RowStatus
_XifRowStatus_Object = MibTableColumn
xifRowStatus = _XifRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 40, 1, 2, 1, 1),
    _XifRowStatus_Type()
)
xifRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xifRowStatus.setStatus("current")
_XifNotifications_ObjectIdentity = ObjectIdentity
xifNotifications = _XifNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 40, 2)
)
_XifConformance_ObjectIdentity = ObjectIdentity
xifConformance = _XifConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 40, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-IF-MIB",
    **{"Unsigned32": Unsigned32,
       "xediaIfMIB": xediaIfMIB,
       "xifObjects": xifObjects,
       "xifNextIndex": xifNextIndex,
       "xifTable": xifTable,
       "xifEntry": xifEntry,
       "xifRowStatus": xifRowStatus,
       "xifNotifications": xifNotifications,
       "xifConformance": xifConformance}
)
