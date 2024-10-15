# SNMP MIB module (VPLS-BGP-DRAFT-01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPLS-BGP-DRAFT-01-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:06 2024
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

(jnxExperiment,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxExperiment")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")

(jnxVplsConfigIndex,
 jnxVplsPwBindIndex) = mibBuilder.importSymbols(
    "VPLS-GENERIC-DRAFT-01-MIB",
    "jnxVplsConfigIndex",
    "jnxVplsPwBindIndex")


# MODULE-IDENTITY

jnxVplsBgpDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10)
)
jnxVplsBgpDraft01MIB.setRevisions(
        ("2006-12-06 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxVplsBgpObjects_ObjectIdentity = ObjectIdentity
jnxVplsBgpObjects = _JnxVplsBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1)
)
_JnxVplsBgpConfigTable_Object = MibTable
jnxVplsBgpConfigTable = _JnxVplsBgpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 1)
)
if mibBuilder.loadTexts:
    jnxVplsBgpConfigTable.setStatus("current")
_JnxVplsBgpConfigEntry_Object = MibTableRow
jnxVplsBgpConfigEntry = _JnxVplsBgpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 1, 1)
)
jnxVplsBgpConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsBgpConfigEntry.setStatus("current")


class _JnxVplsBgpConfigVERangeSize_Type(Unsigned32):
    """Custom type jnxVplsBgpConfigVERangeSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxVplsBgpConfigVERangeSize_Type.__name__ = "Unsigned32"
_JnxVplsBgpConfigVERangeSize_Object = MibTableColumn
jnxVplsBgpConfigVERangeSize = _JnxVplsBgpConfigVERangeSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 1, 1, 1),
    _JnxVplsBgpConfigVERangeSize_Type()
)
jnxVplsBgpConfigVERangeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpConfigVERangeSize.setStatus("current")
_JnxVplsBgpVETable_Object = MibTable
jnxVplsBgpVETable = _JnxVplsBgpVETable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2)
)
if mibBuilder.loadTexts:
    jnxVplsBgpVETable.setStatus("current")
_JnxVplsBgpVEEntry_Object = MibTableRow
jnxVplsBgpVEEntry = _JnxVplsBgpVEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1)
)
jnxVplsBgpVEEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
    (0, "VPLS-BGP-DRAFT-01-MIB", "jnxVplsBgpVEId"),
)
if mibBuilder.loadTexts:
    jnxVplsBgpVEEntry.setStatus("current")


class _JnxVplsBgpVEId_Type(Unsigned32):
    """Custom type jnxVplsBgpVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxVplsBgpVEId_Type.__name__ = "Unsigned32"
_JnxVplsBgpVEId_Object = MibTableColumn
jnxVplsBgpVEId = _JnxVplsBgpVEId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 1),
    _JnxVplsBgpVEId_Type()
)
jnxVplsBgpVEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVplsBgpVEId.setStatus("current")
_JnxVplsBgpVEName_Type = SnmpAdminString
_JnxVplsBgpVEName_Object = MibTableColumn
jnxVplsBgpVEName = _JnxVplsBgpVEName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 2),
    _JnxVplsBgpVEName_Type()
)
jnxVplsBgpVEName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpVEName.setStatus("current")


class _JnxVplsBgpVEPreference_Type(Unsigned32):
    """Custom type jnxVplsBgpVEPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxVplsBgpVEPreference_Type.__name__ = "Unsigned32"
_JnxVplsBgpVEPreference_Object = MibTableColumn
jnxVplsBgpVEPreference = _JnxVplsBgpVEPreference_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 3),
    _JnxVplsBgpVEPreference_Type()
)
jnxVplsBgpVEPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpVEPreference.setStatus("current")
_JnxVplsBgpVERowStatus_Type = RowStatus
_JnxVplsBgpVERowStatus_Object = MibTableColumn
jnxVplsBgpVERowStatus = _JnxVplsBgpVERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 5),
    _JnxVplsBgpVERowStatus_Type()
)
jnxVplsBgpVERowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpVERowStatus.setStatus("current")


class _JnxVplsBgpVEStorageType_Type(StorageType):
    """Custom type jnxVplsBgpVEStorageType based on StorageType"""


_JnxVplsBgpVEStorageType_Object = MibTableColumn
jnxVplsBgpVEStorageType = _JnxVplsBgpVEStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 2, 1, 6),
    _JnxVplsBgpVEStorageType_Type()
)
jnxVplsBgpVEStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpVEStorageType.setStatus("current")
_JnxVplsBgpPwBindTable_Object = MibTable
jnxVplsBgpPwBindTable = _JnxVplsBgpPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3)
)
if mibBuilder.loadTexts:
    jnxVplsBgpPwBindTable.setStatus("current")
_JnxVplsBgpPwBindEntry_Object = MibTableRow
jnxVplsBgpPwBindEntry = _JnxVplsBgpPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3, 1)
)
jnxVplsBgpPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsBgpPwBindEntry.setStatus("current")


class _JnxVplsBgpPwBindLocalVEId_Type(Unsigned32):
    """Custom type jnxVplsBgpPwBindLocalVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxVplsBgpPwBindLocalVEId_Type.__name__ = "Unsigned32"
_JnxVplsBgpPwBindLocalVEId_Object = MibTableColumn
jnxVplsBgpPwBindLocalVEId = _JnxVplsBgpPwBindLocalVEId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3, 1, 1),
    _JnxVplsBgpPwBindLocalVEId_Type()
)
jnxVplsBgpPwBindLocalVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpPwBindLocalVEId.setStatus("current")


class _JnxVplsBgpPwBindRemoteVEId_Type(Unsigned32):
    """Custom type jnxVplsBgpPwBindRemoteVEId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxVplsBgpPwBindRemoteVEId_Type.__name__ = "Unsigned32"
_JnxVplsBgpPwBindRemoteVEId_Object = MibTableColumn
jnxVplsBgpPwBindRemoteVEId = _JnxVplsBgpPwBindRemoteVEId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 1, 3, 1, 2),
    _JnxVplsBgpPwBindRemoteVEId_Type()
)
jnxVplsBgpPwBindRemoteVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpPwBindRemoteVEId.setStatus("current")
_JnxVplsBgpConformance_ObjectIdentity = ObjectIdentity
jnxVplsBgpConformance = _JnxVplsBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 10, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPLS-BGP-DRAFT-01-MIB",
    **{"jnxVplsBgpDraft01MIB": jnxVplsBgpDraft01MIB,
       "jnxVplsBgpObjects": jnxVplsBgpObjects,
       "jnxVplsBgpConfigTable": jnxVplsBgpConfigTable,
       "jnxVplsBgpConfigEntry": jnxVplsBgpConfigEntry,
       "jnxVplsBgpConfigVERangeSize": jnxVplsBgpConfigVERangeSize,
       "jnxVplsBgpVETable": jnxVplsBgpVETable,
       "jnxVplsBgpVEEntry": jnxVplsBgpVEEntry,
       "jnxVplsBgpVEId": jnxVplsBgpVEId,
       "jnxVplsBgpVEName": jnxVplsBgpVEName,
       "jnxVplsBgpVEPreference": jnxVplsBgpVEPreference,
       "jnxVplsBgpVERowStatus": jnxVplsBgpVERowStatus,
       "jnxVplsBgpVEStorageType": jnxVplsBgpVEStorageType,
       "jnxVplsBgpPwBindTable": jnxVplsBgpPwBindTable,
       "jnxVplsBgpPwBindEntry": jnxVplsBgpPwBindEntry,
       "jnxVplsBgpPwBindLocalVEId": jnxVplsBgpPwBindLocalVEId,
       "jnxVplsBgpPwBindRemoteVEId": jnxVplsBgpPwBindRemoteVEId,
       "jnxVplsBgpConformance": jnxVplsBgpConformance}
)
