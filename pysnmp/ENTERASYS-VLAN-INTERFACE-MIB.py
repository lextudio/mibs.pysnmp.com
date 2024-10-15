# SNMP MIB module (ENTERASYS-VLAN-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-VLAN-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:43 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

etsysVlanInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22)
)
etsysVlanInterfaceMIB.setRevisions(
        ("2002-06-07 20:34",
         "2002-06-07 15:37",
         "2002-05-07 17:55")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysVlanInterface_ObjectIdentity = ObjectIdentity
etsysVlanInterface = _EtsysVlanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1)
)
_EtsysVlanInterfaceMaximumEntries_Type = Unsigned32
_EtsysVlanInterfaceMaximumEntries_Object = MibScalar
etsysVlanInterfaceMaximumEntries = _EtsysVlanInterfaceMaximumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 1),
    _EtsysVlanInterfaceMaximumEntries_Type()
)
etsysVlanInterfaceMaximumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVlanInterfaceMaximumEntries.setStatus("current")
_EtsysVlanInterfaceCurrentEntries_Type = Unsigned32
_EtsysVlanInterfaceCurrentEntries_Object = MibScalar
etsysVlanInterfaceCurrentEntries = _EtsysVlanInterfaceCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 2),
    _EtsysVlanInterfaceCurrentEntries_Type()
)
etsysVlanInterfaceCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVlanInterfaceCurrentEntries.setStatus("current")
_EtsysVlanInterfaceTable_Object = MibTable
etsysVlanInterfaceTable = _EtsysVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 3)
)
if mibBuilder.loadTexts:
    etsysVlanInterfaceTable.setStatus("current")
_EtsysVlanInterfaceEntry_Object = MibTableRow
etsysVlanInterfaceEntry = _EtsysVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 3, 1)
)
etsysVlanInterfaceEntry.setIndexNames(
    (0, "ENTERASYS-VLAN-INTERFACE-MIB", "etsysVlanInterfaceVlanID"),
)
if mibBuilder.loadTexts:
    etsysVlanInterfaceEntry.setStatus("current")
_EtsysVlanInterfaceVlanID_Type = VlanIndex
_EtsysVlanInterfaceVlanID_Object = MibTableColumn
etsysVlanInterfaceVlanID = _EtsysVlanInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 3, 1, 1),
    _EtsysVlanInterfaceVlanID_Type()
)
etsysVlanInterfaceVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysVlanInterfaceVlanID.setStatus("current")
_EtsysVlanInterfaceIfIndex_Type = InterfaceIndexOrZero
_EtsysVlanInterfaceIfIndex_Object = MibTableColumn
etsysVlanInterfaceIfIndex = _EtsysVlanInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 3, 1, 2),
    _EtsysVlanInterfaceIfIndex_Type()
)
etsysVlanInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVlanInterfaceIfIndex.setStatus("current")


class _EtsysVlanInterfaceStorageType_Type(StorageType):
    """Custom type etsysVlanInterfaceStorageType based on StorageType"""


_EtsysVlanInterfaceStorageType_Object = MibTableColumn
etsysVlanInterfaceStorageType = _EtsysVlanInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 3, 1, 3),
    _EtsysVlanInterfaceStorageType_Type()
)
etsysVlanInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVlanInterfaceStorageType.setStatus("current")
_EtsysVlanInterfaceRowStatus_Type = RowStatus
_EtsysVlanInterfaceRowStatus_Object = MibTableColumn
etsysVlanInterfaceRowStatus = _EtsysVlanInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 1, 3, 1, 4),
    _EtsysVlanInterfaceRowStatus_Type()
)
etsysVlanInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysVlanInterfaceRowStatus.setStatus("current")
_EtsysVlanInterfaceVlanLookup_ObjectIdentity = ObjectIdentity
etsysVlanInterfaceVlanLookup = _EtsysVlanInterfaceVlanLookup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 2)
)
_EtsysVlanInterfaceVlanLookupTable_Object = MibTable
etsysVlanInterfaceVlanLookupTable = _EtsysVlanInterfaceVlanLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 2, 1)
)
if mibBuilder.loadTexts:
    etsysVlanInterfaceVlanLookupTable.setStatus("current")
_EtsysVlanInterfaceVlanLookupEntry_Object = MibTableRow
etsysVlanInterfaceVlanLookupEntry = _EtsysVlanInterfaceVlanLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 2, 1, 1)
)
etsysVlanInterfaceVlanLookupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysVlanInterfaceVlanLookupEntry.setStatus("current")
_EtsysVlanInterfaceVlanIndex_Type = VlanIndex
_EtsysVlanInterfaceVlanIndex_Object = MibTableColumn
etsysVlanInterfaceVlanIndex = _EtsysVlanInterfaceVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 2, 1, 1, 1),
    _EtsysVlanInterfaceVlanIndex_Type()
)
etsysVlanInterfaceVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVlanInterfaceVlanIndex.setStatus("current")
_EtsysVlanInterfaceConformance_ObjectIdentity = ObjectIdentity
etsysVlanInterfaceConformance = _EtsysVlanInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 3)
)
_EtsysVlanInterfaceGroups_ObjectIdentity = ObjectIdentity
etsysVlanInterfaceGroups = _EtsysVlanInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 3, 1)
)
_EtsysVlanInterfaceCompliances_ObjectIdentity = ObjectIdentity
etsysVlanInterfaceCompliances = _EtsysVlanInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 3, 2)
)

# Managed Objects groups

etsysVlanInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 3, 1, 1)
)
etsysVlanInterfaceGroup.setObjects(
      *(("ENTERASYS-VLAN-INTERFACE-MIB", "etsysVlanInterfaceMaximumEntries"),
        ("ENTERASYS-VLAN-INTERFACE-MIB", "etsysVlanInterfaceCurrentEntries"),
        ("ENTERASYS-VLAN-INTERFACE-MIB", "etsysVlanInterfaceIfIndex"),
        ("ENTERASYS-VLAN-INTERFACE-MIB", "etsysVlanInterfaceStorageType"),
        ("ENTERASYS-VLAN-INTERFACE-MIB", "etsysVlanInterfaceRowStatus"),
        ("ENTERASYS-VLAN-INTERFACE-MIB", "etsysVlanInterfaceVlanIndex"))
)
if mibBuilder.loadTexts:
    etsysVlanInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysVlanInterfaceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 22, 3, 2, 1)
)
if mibBuilder.loadTexts:
    etsysVlanInterfaceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-VLAN-INTERFACE-MIB",
    **{"etsysVlanInterfaceMIB": etsysVlanInterfaceMIB,
       "etsysVlanInterface": etsysVlanInterface,
       "etsysVlanInterfaceMaximumEntries": etsysVlanInterfaceMaximumEntries,
       "etsysVlanInterfaceCurrentEntries": etsysVlanInterfaceCurrentEntries,
       "etsysVlanInterfaceTable": etsysVlanInterfaceTable,
       "etsysVlanInterfaceEntry": etsysVlanInterfaceEntry,
       "etsysVlanInterfaceVlanID": etsysVlanInterfaceVlanID,
       "etsysVlanInterfaceIfIndex": etsysVlanInterfaceIfIndex,
       "etsysVlanInterfaceStorageType": etsysVlanInterfaceStorageType,
       "etsysVlanInterfaceRowStatus": etsysVlanInterfaceRowStatus,
       "etsysVlanInterfaceVlanLookup": etsysVlanInterfaceVlanLookup,
       "etsysVlanInterfaceVlanLookupTable": etsysVlanInterfaceVlanLookupTable,
       "etsysVlanInterfaceVlanLookupEntry": etsysVlanInterfaceVlanLookupEntry,
       "etsysVlanInterfaceVlanIndex": etsysVlanInterfaceVlanIndex,
       "etsysVlanInterfaceConformance": etsysVlanInterfaceConformance,
       "etsysVlanInterfaceGroups": etsysVlanInterfaceGroups,
       "etsysVlanInterfaceGroup": etsysVlanInterfaceGroup,
       "etsysVlanInterfaceCompliances": etsysVlanInterfaceCompliances,
       "etsysVlanInterfaceCompliance": etsysVlanInterfaceCompliance}
)
