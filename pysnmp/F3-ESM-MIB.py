# SNMP MIB module (F3-ESM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F3-ESM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:31 2024
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

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
 TextualConvention,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "VariablePointer")


# MODULE-IDENTITY

f3ESMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23)
)
f3ESMMIB.setRevisions(
        ("2012-10-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F3EsmConfigObjects_ObjectIdentity = ObjectIdentity
f3EsmConfigObjects = _F3EsmConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1)
)
_EsmConfigTable_Object = MibTable
esmConfigTable = _EsmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 1)
)
if mibBuilder.loadTexts:
    esmConfigTable.setStatus("current")
_EsmConfigEntry_Object = MibTableRow
esmConfigEntry = _EsmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 1, 1)
)
esmConfigEntry.setIndexNames(
    (0, "F3-ESM-MIB", "esmConfigIndex"),
)
if mibBuilder.loadTexts:
    esmConfigEntry.setStatus("current")
_EsmConfigIndex_Type = Unsigned32
_EsmConfigIndex_Object = MibTableColumn
esmConfigIndex = _EsmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 1, 1, 1),
    _EsmConfigIndex_Type()
)
esmConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esmConfigIndex.setStatus("current")
_EsmConfigAssociatedEntity_Type = VariablePointer
_EsmConfigAssociatedEntity_Object = MibTableColumn
esmConfigAssociatedEntity = _EsmConfigAssociatedEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 1, 1, 2),
    _EsmConfigAssociatedEntity_Type()
)
esmConfigAssociatedEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmConfigAssociatedEntity.setStatus("current")
_EsmConfigStorageType_Type = StorageType
_EsmConfigStorageType_Object = MibTableColumn
esmConfigStorageType = _EsmConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 1, 1, 3),
    _EsmConfigStorageType_Type()
)
esmConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmConfigStorageType.setStatus("current")
_EsmConfigRowStatus_Type = RowStatus
_EsmConfigRowStatus_Object = MibTableColumn
esmConfigRowStatus = _EsmConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 1, 1, 4),
    _EsmConfigRowStatus_Type()
)
esmConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmConfigRowStatus.setStatus("current")
_EsmNameValuePairTable_Object = MibTable
esmNameValuePairTable = _EsmNameValuePairTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 2)
)
if mibBuilder.loadTexts:
    esmNameValuePairTable.setStatus("current")
_EsmNameValuePairEntry_Object = MibTableRow
esmNameValuePairEntry = _EsmNameValuePairEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 2, 1)
)
esmNameValuePairEntry.setIndexNames(
    (0, "F3-ESM-MIB", "esmConfigIndex"),
    (0, "F3-ESM-MIB", "esmNameValuePairName"),
)
if mibBuilder.loadTexts:
    esmNameValuePairEntry.setStatus("current")


class _EsmNameValuePairName_Type(DisplayString):
    """Custom type esmNameValuePairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EsmNameValuePairName_Type.__name__ = "DisplayString"
_EsmNameValuePairName_Object = MibTableColumn
esmNameValuePairName = _EsmNameValuePairName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 2, 1, 1),
    _EsmNameValuePairName_Type()
)
esmNameValuePairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    esmNameValuePairName.setStatus("current")


class _EsmNameValuePairValue_Type(DisplayString):
    """Custom type esmNameValuePairValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EsmNameValuePairValue_Type.__name__ = "DisplayString"
_EsmNameValuePairValue_Object = MibTableColumn
esmNameValuePairValue = _EsmNameValuePairValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 2, 1, 2),
    _EsmNameValuePairValue_Type()
)
esmNameValuePairValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmNameValuePairValue.setStatus("current")


class _EsmNameValuePairStorageType_Type(StorageType):
    """Custom type esmNameValuePairStorageType based on StorageType"""


_EsmNameValuePairStorageType_Object = MibTableColumn
esmNameValuePairStorageType = _EsmNameValuePairStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 2, 1, 3),
    _EsmNameValuePairStorageType_Type()
)
esmNameValuePairStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmNameValuePairStorageType.setStatus("current")
_EsmNameValuePairRowStatus_Type = RowStatus
_EsmNameValuePairRowStatus_Object = MibTableColumn
esmNameValuePairRowStatus = _EsmNameValuePairRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 1, 2, 1, 4),
    _EsmNameValuePairRowStatus_Type()
)
esmNameValuePairRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    esmNameValuePairRowStatus.setStatus("current")
_F3EsmConformance_ObjectIdentity = ObjectIdentity
f3EsmConformance = _F3EsmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 2)
)
_F3EsmCompliances_ObjectIdentity = ObjectIdentity
f3EsmCompliances = _F3EsmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 2, 1)
)
_F3EsmGroups_ObjectIdentity = ObjectIdentity
f3EsmGroups = _F3EsmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 2, 2)
)

# Managed Objects groups

esmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 2, 2, 1)
)
esmConfigGroup.setObjects(
      *(("F3-ESM-MIB", "esmConfigAssociatedEntity"),
        ("F3-ESM-MIB", "esmConfigStorageType"),
        ("F3-ESM-MIB", "esmConfigRowStatus"))
)
if mibBuilder.loadTexts:
    esmConfigGroup.setStatus("current")

esmNameValuePairGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 2, 2, 2)
)
esmNameValuePairGroup.setObjects(
      *(("F3-ESM-MIB", "esmNameValuePairValue"),
        ("F3-ESM-MIB", "esmNameValuePairStorageType"),
        ("F3-ESM-MIB", "esmNameValuePairRowStatus"))
)
if mibBuilder.loadTexts:
    esmNameValuePairGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3EsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 23, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f3EsmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-ESM-MIB",
    **{"f3ESMMIB": f3ESMMIB,
       "f3EsmConfigObjects": f3EsmConfigObjects,
       "esmConfigTable": esmConfigTable,
       "esmConfigEntry": esmConfigEntry,
       "esmConfigIndex": esmConfigIndex,
       "esmConfigAssociatedEntity": esmConfigAssociatedEntity,
       "esmConfigStorageType": esmConfigStorageType,
       "esmConfigRowStatus": esmConfigRowStatus,
       "esmNameValuePairTable": esmNameValuePairTable,
       "esmNameValuePairEntry": esmNameValuePairEntry,
       "esmNameValuePairName": esmNameValuePairName,
       "esmNameValuePairValue": esmNameValuePairValue,
       "esmNameValuePairStorageType": esmNameValuePairStorageType,
       "esmNameValuePairRowStatus": esmNameValuePairRowStatus,
       "f3EsmConformance": f3EsmConformance,
       "f3EsmCompliances": f3EsmCompliances,
       "f3EsmCompliance": f3EsmCompliance,
       "f3EsmGroups": f3EsmGroups,
       "esmConfigGroup": esmConfigGroup,
       "esmNameValuePairGroup": esmNameValuePairGroup}
)
