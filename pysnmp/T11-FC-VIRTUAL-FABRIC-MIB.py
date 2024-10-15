# SNMP MIB module (T11-FC-VIRTUAL-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-VIRTUAL-FABRIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:39 2024
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

(FcNameIdOrZero,
 fcmInstanceIndex,
 fcmPortEntry,
 fcmSwitchEntry) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcNameIdOrZero",
    "fcmInstanceIndex",
    "fcmPortEntry",
    "fcmSwitchEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcVirtualFabricMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 147)
)
t11FcVirtualFabricMIB.setRevisions(
        ("2006-11-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11vfObjects_ObjectIdentity = ObjectIdentity
t11vfObjects = _T11vfObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 147, 1)
)
_T11vfCoreSwitchTable_Object = MibTable
t11vfCoreSwitchTable = _T11vfCoreSwitchTable_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 1)
)
if mibBuilder.loadTexts:
    t11vfCoreSwitchTable.setStatus("current")
_T11vfCoreSwitchEntry_Object = MibTableRow
t11vfCoreSwitchEntry = _T11vfCoreSwitchEntry_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 1, 1)
)
t11vfCoreSwitchEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchSwitchName"),
)
if mibBuilder.loadTexts:
    t11vfCoreSwitchEntry.setStatus("current")


class _T11vfCoreSwitchSwitchName_Type(FcNameIdOrZero):
    """Custom type t11vfCoreSwitchSwitchName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_T11vfCoreSwitchSwitchName_Type.__name__ = "FcNameIdOrZero"
_T11vfCoreSwitchSwitchName_Object = MibTableColumn
t11vfCoreSwitchSwitchName = _T11vfCoreSwitchSwitchName_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 1),
    _T11vfCoreSwitchSwitchName_Type()
)
t11vfCoreSwitchSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11vfCoreSwitchSwitchName.setStatus("current")


class _T11vfCoreSwitchMaxSupported_Type(Unsigned32):
    """Custom type t11vfCoreSwitchMaxSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_T11vfCoreSwitchMaxSupported_Type.__name__ = "Unsigned32"
_T11vfCoreSwitchMaxSupported_Object = MibTableColumn
t11vfCoreSwitchMaxSupported = _T11vfCoreSwitchMaxSupported_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 2),
    _T11vfCoreSwitchMaxSupported_Type()
)
t11vfCoreSwitchMaxSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11vfCoreSwitchMaxSupported.setStatus("current")


class _T11vfCoreSwitchStorageType_Type(StorageType):
    """Custom type t11vfCoreSwitchStorageType based on StorageType"""


_T11vfCoreSwitchStorageType_Object = MibTableColumn
t11vfCoreSwitchStorageType = _T11vfCoreSwitchStorageType_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 3),
    _T11vfCoreSwitchStorageType_Type()
)
t11vfCoreSwitchStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11vfCoreSwitchStorageType.setStatus("current")
_T11vfVirtualSwitchTable_Object = MibTable
t11vfVirtualSwitchTable = _T11vfVirtualSwitchTable_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 2)
)
if mibBuilder.loadTexts:
    t11vfVirtualSwitchTable.setStatus("current")
_T11vfVirtualSwitchEntry_Object = MibTableRow
t11vfVirtualSwitchEntry = _T11vfVirtualSwitchEntry_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11vfVirtualSwitchEntry.setStatus("current")
_T11vfVirtualSwitchVfId_Type = T11FabricIndex
_T11vfVirtualSwitchVfId_Object = MibTableColumn
t11vfVirtualSwitchVfId = _T11vfVirtualSwitchVfId_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 1),
    _T11vfVirtualSwitchVfId_Type()
)
t11vfVirtualSwitchVfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11vfVirtualSwitchVfId.setStatus("current")


class _T11vfVirtualSwitchCoreSwitchName_Type(FcNameIdOrZero):
    """Custom type t11vfVirtualSwitchCoreSwitchName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_T11vfVirtualSwitchCoreSwitchName_Type.__name__ = "FcNameIdOrZero"
_T11vfVirtualSwitchCoreSwitchName_Object = MibTableColumn
t11vfVirtualSwitchCoreSwitchName = _T11vfVirtualSwitchCoreSwitchName_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 2),
    _T11vfVirtualSwitchCoreSwitchName_Type()
)
t11vfVirtualSwitchCoreSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11vfVirtualSwitchCoreSwitchName.setStatus("current")
_T11vfVirtualSwitchRowStatus_Type = RowStatus
_T11vfVirtualSwitchRowStatus_Object = MibTableColumn
t11vfVirtualSwitchRowStatus = _T11vfVirtualSwitchRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 3),
    _T11vfVirtualSwitchRowStatus_Type()
)
t11vfVirtualSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11vfVirtualSwitchRowStatus.setStatus("current")


class _T11vfVirtualSwitchStorageType_Type(StorageType):
    """Custom type t11vfVirtualSwitchStorageType based on StorageType"""


_T11vfVirtualSwitchStorageType_Object = MibTableColumn
t11vfVirtualSwitchStorageType = _T11vfVirtualSwitchStorageType_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 4),
    _T11vfVirtualSwitchStorageType_Type()
)
t11vfVirtualSwitchStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11vfVirtualSwitchStorageType.setStatus("current")
_T11vfPortTable_Object = MibTable
t11vfPortTable = _T11vfPortTable_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 3)
)
if mibBuilder.loadTexts:
    t11vfPortTable.setStatus("current")
_T11vfPortEntry_Object = MibTableRow
t11vfPortEntry = _T11vfPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 3, 1)
)
if mibBuilder.loadTexts:
    t11vfPortEntry.setStatus("current")


class _T11vfPortVfId_Type(T11FabricIndex):
    """Custom type t11vfPortVfId based on T11FabricIndex"""
    defaultValue = 1


_T11vfPortVfId_Object = MibTableColumn
t11vfPortVfId = _T11vfPortVfId_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 1),
    _T11vfPortVfId_Type()
)
t11vfPortVfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11vfPortVfId.setStatus("current")


class _T11vfPortTaggingAdminStatus_Type(Integer32):
    """Custom type t11vfPortTaggingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("off", 1),
          ("on", 2))
    )


_T11vfPortTaggingAdminStatus_Type.__name__ = "Integer32"
_T11vfPortTaggingAdminStatus_Object = MibTableColumn
t11vfPortTaggingAdminStatus = _T11vfPortTaggingAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 2),
    _T11vfPortTaggingAdminStatus_Type()
)
t11vfPortTaggingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11vfPortTaggingAdminStatus.setStatus("current")


class _T11vfPortTaggingOperStatus_Type(Integer32):
    """Custom type t11vfPortTaggingOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_T11vfPortTaggingOperStatus_Type.__name__ = "Integer32"
_T11vfPortTaggingOperStatus_Object = MibTableColumn
t11vfPortTaggingOperStatus = _T11vfPortTaggingOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 3),
    _T11vfPortTaggingOperStatus_Type()
)
t11vfPortTaggingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11vfPortTaggingOperStatus.setStatus("current")


class _T11vfPortStorageType_Type(StorageType):
    """Custom type t11vfPortStorageType based on StorageType"""


_T11vfPortStorageType_Object = MibTableColumn
t11vfPortStorageType = _T11vfPortStorageType_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 4),
    _T11vfPortStorageType_Type()
)
t11vfPortStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11vfPortStorageType.setStatus("current")
_T11vfLocallyEnabledTable_Object = MibTable
t11vfLocallyEnabledTable = _T11vfLocallyEnabledTable_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 4)
)
if mibBuilder.loadTexts:
    t11vfLocallyEnabledTable.setStatus("current")
_T11vfLocallyEnabledEntry_Object = MibTableRow
t11vfLocallyEnabledEntry = _T11vfLocallyEnabledEntry_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 4, 1)
)
t11vfLocallyEnabledEntry.setIndexNames(
    (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledPortIfIndex"),
    (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledVfId"),
)
if mibBuilder.loadTexts:
    t11vfLocallyEnabledEntry.setStatus("current")
_T11vfLocallyEnabledPortIfIndex_Type = InterfaceIndex
_T11vfLocallyEnabledPortIfIndex_Object = MibTableColumn
t11vfLocallyEnabledPortIfIndex = _T11vfLocallyEnabledPortIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 1),
    _T11vfLocallyEnabledPortIfIndex_Type()
)
t11vfLocallyEnabledPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11vfLocallyEnabledPortIfIndex.setStatus("current")
_T11vfLocallyEnabledVfId_Type = T11FabricIndex
_T11vfLocallyEnabledVfId_Object = MibTableColumn
t11vfLocallyEnabledVfId = _T11vfLocallyEnabledVfId_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 2),
    _T11vfLocallyEnabledVfId_Type()
)
t11vfLocallyEnabledVfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11vfLocallyEnabledVfId.setStatus("current")


class _T11vfLocallyEnabledOperStatus_Type(Integer32):
    """Custom type t11vfLocallyEnabledOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_T11vfLocallyEnabledOperStatus_Type.__name__ = "Integer32"
_T11vfLocallyEnabledOperStatus_Object = MibTableColumn
t11vfLocallyEnabledOperStatus = _T11vfLocallyEnabledOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 3),
    _T11vfLocallyEnabledOperStatus_Type()
)
t11vfLocallyEnabledOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11vfLocallyEnabledOperStatus.setStatus("current")
_T11vfLocallyEnabledRowStatus_Type = RowStatus
_T11vfLocallyEnabledRowStatus_Object = MibTableColumn
t11vfLocallyEnabledRowStatus = _T11vfLocallyEnabledRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 4),
    _T11vfLocallyEnabledRowStatus_Type()
)
t11vfLocallyEnabledRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11vfLocallyEnabledRowStatus.setStatus("current")


class _T11vfLocallyEnabledStorageType_Type(StorageType):
    """Custom type t11vfLocallyEnabledStorageType based on StorageType"""


_T11vfLocallyEnabledStorageType_Object = MibTableColumn
t11vfLocallyEnabledStorageType = _T11vfLocallyEnabledStorageType_Object(
    (1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 5),
    _T11vfLocallyEnabledStorageType_Type()
)
t11vfLocallyEnabledStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11vfLocallyEnabledStorageType.setStatus("current")
_T11vfConformance_ObjectIdentity = ObjectIdentity
t11vfConformance = _T11vfConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 147, 2)
)
_T11vfMIBCompliances_ObjectIdentity = ObjectIdentity
t11vfMIBCompliances = _T11vfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 147, 2, 1)
)
_T11vfMIBGroups_ObjectIdentity = ObjectIdentity
t11vfMIBGroups = _T11vfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 147, 2, 2)
)
fcmSwitchEntry.registerAugmentions(
    ("T11-FC-VIRTUAL-FABRIC-MIB",
     "t11vfVirtualSwitchEntry")
)
t11vfVirtualSwitchEntry.setIndexNames(*fcmSwitchEntry.getIndexNames())
fcmPortEntry.registerAugmentions(
    ("T11-FC-VIRTUAL-FABRIC-MIB",
     "t11vfPortEntry")
)
t11vfPortEntry.setIndexNames(*fcmPortEntry.getIndexNames())

# Managed Objects groups

t11vfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 147, 2, 2, 1)
)
t11vfGeneralGroup.setObjects(
      *(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchMaxSupported"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchVfId"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchCoreSwitchName"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchRowStatus"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortVfId"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingAdminStatus"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledOperStatus"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingOperStatus"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledRowStatus"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchStorageType"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchStorageType"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortStorageType"),
        ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledStorageType"))
)
if mibBuilder.loadTexts:
    t11vfGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

t11vfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 147, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11vfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-VIRTUAL-FABRIC-MIB",
    **{"t11FcVirtualFabricMIB": t11FcVirtualFabricMIB,
       "t11vfObjects": t11vfObjects,
       "t11vfCoreSwitchTable": t11vfCoreSwitchTable,
       "t11vfCoreSwitchEntry": t11vfCoreSwitchEntry,
       "t11vfCoreSwitchSwitchName": t11vfCoreSwitchSwitchName,
       "t11vfCoreSwitchMaxSupported": t11vfCoreSwitchMaxSupported,
       "t11vfCoreSwitchStorageType": t11vfCoreSwitchStorageType,
       "t11vfVirtualSwitchTable": t11vfVirtualSwitchTable,
       "t11vfVirtualSwitchEntry": t11vfVirtualSwitchEntry,
       "t11vfVirtualSwitchVfId": t11vfVirtualSwitchVfId,
       "t11vfVirtualSwitchCoreSwitchName": t11vfVirtualSwitchCoreSwitchName,
       "t11vfVirtualSwitchRowStatus": t11vfVirtualSwitchRowStatus,
       "t11vfVirtualSwitchStorageType": t11vfVirtualSwitchStorageType,
       "t11vfPortTable": t11vfPortTable,
       "t11vfPortEntry": t11vfPortEntry,
       "t11vfPortVfId": t11vfPortVfId,
       "t11vfPortTaggingAdminStatus": t11vfPortTaggingAdminStatus,
       "t11vfPortTaggingOperStatus": t11vfPortTaggingOperStatus,
       "t11vfPortStorageType": t11vfPortStorageType,
       "t11vfLocallyEnabledTable": t11vfLocallyEnabledTable,
       "t11vfLocallyEnabledEntry": t11vfLocallyEnabledEntry,
       "t11vfLocallyEnabledPortIfIndex": t11vfLocallyEnabledPortIfIndex,
       "t11vfLocallyEnabledVfId": t11vfLocallyEnabledVfId,
       "t11vfLocallyEnabledOperStatus": t11vfLocallyEnabledOperStatus,
       "t11vfLocallyEnabledRowStatus": t11vfLocallyEnabledRowStatus,
       "t11vfLocallyEnabledStorageType": t11vfLocallyEnabledStorageType,
       "t11vfConformance": t11vfConformance,
       "t11vfMIBCompliances": t11vfMIBCompliances,
       "t11vfMIBCompliance": t11vfMIBCompliance,
       "t11vfMIBGroups": t11vfMIBGroups,
       "t11vfGeneralGroup": t11vfGeneralGroup}
)
