# SNMP MIB module (VPLS-GENERIC-DRAFT-01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPLS-GENERIC-DRAFT-01-MIB
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(VPNIdOrZero,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNIdOrZero")


# MODULE-IDENTITY

jnxVplsGenericDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8)
)
jnxVplsGenericDraft01MIB.setRevisions(
        ("2011-03-26 12:00",
         "2006-08-30 12:00",
         "2006-06-04 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwIndexType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class JnxVplsBgpRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class JnxVplsBgpRouteTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class JnxVplsBgpRouteTargetType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("export", 2),
          ("import", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JnxVplsNotifications_ObjectIdentity = ObjectIdentity
jnxVplsNotifications = _JnxVplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 0)
)
_JnxVplsObjects_ObjectIdentity = ObjectIdentity
jnxVplsObjects = _JnxVplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1)
)
_JnxVplsConfigIndexNext_Type = Unsigned32
_JnxVplsConfigIndexNext_Object = MibScalar
jnxVplsConfigIndexNext = _JnxVplsConfigIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 1),
    _JnxVplsConfigIndexNext_Type()
)
jnxVplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigIndexNext.setStatus("current")
_JnxVplsConfigTable_Object = MibTable
jnxVplsConfigTable = _JnxVplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2)
)
if mibBuilder.loadTexts:
    jnxVplsConfigTable.setStatus("current")
_JnxVplsConfigEntry_Object = MibTableRow
jnxVplsConfigEntry = _JnxVplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1)
)
jnxVplsConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsConfigEntry.setStatus("current")


class _JnxVplsConfigIndex_Type(Unsigned32):
    """Custom type jnxVplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxVplsConfigIndex_Type.__name__ = "Unsigned32"
_JnxVplsConfigIndex_Object = MibTableColumn
jnxVplsConfigIndex = _JnxVplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 1),
    _JnxVplsConfigIndex_Type()
)
jnxVplsConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigIndex.setStatus("current")
_JnxVplsConfigName_Type = SnmpAdminString
_JnxVplsConfigName_Object = MibTableColumn
jnxVplsConfigName = _JnxVplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 2),
    _JnxVplsConfigName_Type()
)
jnxVplsConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigName.setStatus("current")
_JnxVplsConfigDescr_Type = SnmpAdminString
_JnxVplsConfigDescr_Object = MibTableColumn
jnxVplsConfigDescr = _JnxVplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 3),
    _JnxVplsConfigDescr_Type()
)
jnxVplsConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigDescr.setStatus("current")


class _JnxVplsConfigAdminStatus_Type(Integer32):
    """Custom type jnxVplsConfigAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_JnxVplsConfigAdminStatus_Type.__name__ = "Integer32"
_JnxVplsConfigAdminStatus_Object = MibTableColumn
jnxVplsConfigAdminStatus = _JnxVplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 4),
    _JnxVplsConfigAdminStatus_Type()
)
jnxVplsConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigAdminStatus.setStatus("current")


class _JnxVplsConfigMacLearning_Type(TruthValue):
    """Custom type jnxVplsConfigMacLearning based on TruthValue"""


_JnxVplsConfigMacLearning_Object = MibTableColumn
jnxVplsConfigMacLearning = _JnxVplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 6),
    _JnxVplsConfigMacLearning_Type()
)
jnxVplsConfigMacLearning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigMacLearning.setStatus("current")


class _JnxVplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type jnxVplsConfigDiscardUnknownDest based on TruthValue"""


_JnxVplsConfigDiscardUnknownDest_Object = MibTableColumn
jnxVplsConfigDiscardUnknownDest = _JnxVplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 7),
    _JnxVplsConfigDiscardUnknownDest_Type()
)
jnxVplsConfigDiscardUnknownDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigDiscardUnknownDest.setStatus("current")


class _JnxVplsConfigMacAging_Type(TruthValue):
    """Custom type jnxVplsConfigMacAging based on TruthValue"""


_JnxVplsConfigMacAging_Object = MibTableColumn
jnxVplsConfigMacAging = _JnxVplsConfigMacAging_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 8),
    _JnxVplsConfigMacAging_Type()
)
jnxVplsConfigMacAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigMacAging.setStatus("current")


class _JnxVplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type jnxVplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxVplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_JnxVplsConfigFwdFullHighWatermark_Object = MibTableColumn
jnxVplsConfigFwdFullHighWatermark = _JnxVplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 10),
    _JnxVplsConfigFwdFullHighWatermark_Type()
)
jnxVplsConfigFwdFullHighWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    jnxVplsConfigFwdFullHighWatermark.setUnits("percentage")


class _JnxVplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type jnxVplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxVplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_JnxVplsConfigFwdFullLowWatermark_Object = MibTableColumn
jnxVplsConfigFwdFullLowWatermark = _JnxVplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 11),
    _JnxVplsConfigFwdFullLowWatermark_Type()
)
jnxVplsConfigFwdFullLowWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    jnxVplsConfigFwdFullLowWatermark.setUnits("percentage")
_JnxVplsConfigRowStatus_Type = RowStatus
_JnxVplsConfigRowStatus_Object = MibTableColumn
jnxVplsConfigRowStatus = _JnxVplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 12),
    _JnxVplsConfigRowStatus_Type()
)
jnxVplsConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigRowStatus.setStatus("current")


class _JnxVplsConfigMtu_Type(Unsigned32):
    """Custom type jnxVplsConfigMtu based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_JnxVplsConfigMtu_Type.__name__ = "Unsigned32"
_JnxVplsConfigMtu_Object = MibTableColumn
jnxVplsConfigMtu = _JnxVplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 13),
    _JnxVplsConfigMtu_Type()
)
jnxVplsConfigMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigMtu.setStatus("current")
_JnxVplsConfigVpnId_Type = VPNIdOrZero
_JnxVplsConfigVpnId_Object = MibTableColumn
jnxVplsConfigVpnId = _JnxVplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 14),
    _JnxVplsConfigVpnId_Type()
)
jnxVplsConfigVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigVpnId.setStatus("current")


class _JnxVplsConfigServiceType_Type(Integer32):
    """Custom type jnxVplsConfigServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("vlan", 1))
    )


_JnxVplsConfigServiceType_Type.__name__ = "Integer32"
_JnxVplsConfigServiceType_Object = MibTableColumn
jnxVplsConfigServiceType = _JnxVplsConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 15),
    _JnxVplsConfigServiceType_Type()
)
jnxVplsConfigServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigServiceType.setStatus("current")


class _JnxVplsConfigStorageType_Type(StorageType):
    """Custom type jnxVplsConfigStorageType based on StorageType"""


_JnxVplsConfigStorageType_Object = MibTableColumn
jnxVplsConfigStorageType = _JnxVplsConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 2, 1, 16),
    _JnxVplsConfigStorageType_Type()
)
jnxVplsConfigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsConfigStorageType.setStatus("current")
_JnxVplsStatusTable_Object = MibTable
jnxVplsStatusTable = _JnxVplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3)
)
if mibBuilder.loadTexts:
    jnxVplsStatusTable.setStatus("current")
_JnxVplsStatusEntry_Object = MibTableRow
jnxVplsStatusEntry = _JnxVplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3, 1)
)
jnxVplsStatusEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsStatusEntry.setStatus("current")


class _JnxVplsStatusOperStatus_Type(Integer32):
    """Custom type jnxVplsStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 0),
          ("up", 1))
    )


_JnxVplsStatusOperStatus_Type.__name__ = "Integer32"
_JnxVplsStatusOperStatus_Object = MibTableColumn
jnxVplsStatusOperStatus = _JnxVplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3, 1, 1),
    _JnxVplsStatusOperStatus_Type()
)
jnxVplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsStatusOperStatus.setStatus("current")
_JnxVplsStatusPeerCount_Type = Counter32
_JnxVplsStatusPeerCount_Object = MibTableColumn
jnxVplsStatusPeerCount = _JnxVplsStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 3, 1, 2),
    _JnxVplsStatusPeerCount_Type()
)
jnxVplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsStatusPeerCount.setStatus("current")
_JnxVplsPwBindTable_Object = MibTable
jnxVplsPwBindTable = _JnxVplsPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4)
)
if mibBuilder.loadTexts:
    jnxVplsPwBindTable.setStatus("current")
_JnxVplsPwBindEntry_Object = MibTableRow
jnxVplsPwBindEntry = _JnxVplsPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1)
)
jnxVplsPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsPwBindEntry.setStatus("current")


class _JnxVplsPwBindConfigType_Type(Integer32):
    """Custom type jnxVplsPwBindConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autodiscovery", 2),
          ("manual", 1))
    )


_JnxVplsPwBindConfigType_Type.__name__ = "Integer32"
_JnxVplsPwBindConfigType_Object = MibTableColumn
jnxVplsPwBindConfigType = _JnxVplsPwBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 1),
    _JnxVplsPwBindConfigType_Type()
)
jnxVplsPwBindConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsPwBindConfigType.setStatus("current")


class _JnxVplsPwBindType_Type(Integer32):
    """Custom type jnxVplsPwBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mesh", 1),
          ("spoke", 2))
    )


_JnxVplsPwBindType_Type.__name__ = "Integer32"
_JnxVplsPwBindType_Object = MibTableColumn
jnxVplsPwBindType = _JnxVplsPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 2),
    _JnxVplsPwBindType_Type()
)
jnxVplsPwBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsPwBindType.setStatus("current")
_JnxVplsPwBindRowStatus_Type = RowStatus
_JnxVplsPwBindRowStatus_Object = MibTableColumn
jnxVplsPwBindRowStatus = _JnxVplsPwBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 3),
    _JnxVplsPwBindRowStatus_Type()
)
jnxVplsPwBindRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsPwBindRowStatus.setStatus("current")


class _JnxVplsPwBindStorageType_Type(StorageType):
    """Custom type jnxVplsPwBindStorageType based on StorageType"""


_JnxVplsPwBindStorageType_Object = MibTableColumn
jnxVplsPwBindStorageType = _JnxVplsPwBindStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 4),
    _JnxVplsPwBindStorageType_Type()
)
jnxVplsPwBindStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsPwBindStorageType.setStatus("current")
_JnxVplsPwBindIndex_Type = PwIndexType
_JnxVplsPwBindIndex_Object = MibTableColumn
jnxVplsPwBindIndex = _JnxVplsPwBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 4, 1, 5),
    _JnxVplsPwBindIndex_Type()
)
jnxVplsPwBindIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsPwBindIndex.setStatus("current")
_JnxVplsBgpADConfigTable_Object = MibTable
jnxVplsBgpADConfigTable = _JnxVplsBgpADConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5)
)
if mibBuilder.loadTexts:
    jnxVplsBgpADConfigTable.setStatus("current")
_JnxVplsBgpADConfigEntry_Object = MibTableRow
jnxVplsBgpADConfigEntry = _JnxVplsBgpADConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1)
)
jnxVplsBgpADConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsBgpADConfigEntry.setStatus("current")
_JnxVplsBgpADConfigRouteDistinguisher_Type = JnxVplsBgpRouteDistinguisher
_JnxVplsBgpADConfigRouteDistinguisher_Object = MibTableColumn
jnxVplsBgpADConfigRouteDistinguisher = _JnxVplsBgpADConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 1),
    _JnxVplsBgpADConfigRouteDistinguisher_Type()
)
jnxVplsBgpADConfigRouteDistinguisher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpADConfigRouteDistinguisher.setStatus("current")


class _JnxVplsBgpADConfigPrefix_Type(Unsigned32):
    """Custom type jnxVplsBgpADConfigPrefix based on Unsigned32"""
    defaultValue = 0


_JnxVplsBgpADConfigPrefix_Object = MibTableColumn
jnxVplsBgpADConfigPrefix = _JnxVplsBgpADConfigPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 2),
    _JnxVplsBgpADConfigPrefix_Type()
)
jnxVplsBgpADConfigPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpADConfigPrefix.setStatus("current")
_JnxVplsBgpADConfigVplsId_Type = JnxVplsBgpRouteDistinguisher
_JnxVplsBgpADConfigVplsId_Object = MibTableColumn
jnxVplsBgpADConfigVplsId = _JnxVplsBgpADConfigVplsId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 3),
    _JnxVplsBgpADConfigVplsId_Type()
)
jnxVplsBgpADConfigVplsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpADConfigVplsId.setStatus("current")
_JnxVplsBgpADConfigRowStatus_Type = RowStatus
_JnxVplsBgpADConfigRowStatus_Object = MibTableColumn
jnxVplsBgpADConfigRowStatus = _JnxVplsBgpADConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 5, 1, 4),
    _JnxVplsBgpADConfigRowStatus_Type()
)
jnxVplsBgpADConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpADConfigRowStatus.setStatus("current")
_JnxVplsBgpRteTargetTable_Object = MibTable
jnxVplsBgpRteTargetTable = _JnxVplsBgpRteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6)
)
if mibBuilder.loadTexts:
    jnxVplsBgpRteTargetTable.setStatus("current")
_JnxVplsBgpRteTargetEntry_Object = MibTableRow
jnxVplsBgpRteTargetEntry = _JnxVplsBgpRteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1)
)
jnxVplsBgpRteTargetEntry.setIndexNames(
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigIndex"),
    (0, "VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsBgpRteTargetIndex"),
)
if mibBuilder.loadTexts:
    jnxVplsBgpRteTargetEntry.setStatus("current")
_JnxVplsBgpRteTargetIndex_Type = Unsigned32
_JnxVplsBgpRteTargetIndex_Object = MibTableColumn
jnxVplsBgpRteTargetIndex = _JnxVplsBgpRteTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 1),
    _JnxVplsBgpRteTargetIndex_Type()
)
jnxVplsBgpRteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVplsBgpRteTargetIndex.setStatus("current")
_JnxVplsBgpRteTargetRTType_Type = JnxVplsBgpRouteTargetType
_JnxVplsBgpRteTargetRTType_Object = MibTableColumn
jnxVplsBgpRteTargetRTType = _JnxVplsBgpRteTargetRTType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 2),
    _JnxVplsBgpRteTargetRTType_Type()
)
jnxVplsBgpRteTargetRTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpRteTargetRTType.setStatus("current")
_JnxVplsBgpRteTargetRT_Type = JnxVplsBgpRouteTarget
_JnxVplsBgpRteTargetRT_Object = MibTableColumn
jnxVplsBgpRteTargetRT = _JnxVplsBgpRteTargetRT_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 3),
    _JnxVplsBgpRteTargetRT_Type()
)
jnxVplsBgpRteTargetRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpRteTargetRT.setStatus("current")
_JnxVplsBgpRteTargetRTRowStatus_Type = RowStatus
_JnxVplsBgpRteTargetRTRowStatus_Object = MibTableColumn
jnxVplsBgpRteTargetRTRowStatus = _JnxVplsBgpRteTargetRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 6, 1, 4),
    _JnxVplsBgpRteTargetRTRowStatus_Type()
)
jnxVplsBgpRteTargetRTRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVplsBgpRteTargetRTRowStatus.setStatus("current")


class _JnxVplsStatusNotifEnable_Type(TruthValue):
    """Custom type jnxVplsStatusNotifEnable based on TruthValue"""


_JnxVplsStatusNotifEnable_Object = MibScalar
jnxVplsStatusNotifEnable = _JnxVplsStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 7),
    _JnxVplsStatusNotifEnable_Type()
)
jnxVplsStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxVplsStatusNotifEnable.setStatus("current")


class _JnxVplsNotificationMaxRate_Type(Unsigned32):
    """Custom type jnxVplsNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_JnxVplsNotificationMaxRate_Object = MibScalar
jnxVplsNotificationMaxRate = _JnxVplsNotificationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 1, 8),
    _JnxVplsNotificationMaxRate_Type()
)
jnxVplsNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxVplsNotificationMaxRate.setStatus("current")
_JnxVplsConformance_ObjectIdentity = ObjectIdentity
jnxVplsConformance = _JnxVplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 2)
)

# Managed Objects groups


# Notification objects

jnxVplsStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 0, 1)
)
jnxVplsStatusChanged.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigVpnId"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigAdminStatus"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsStatusOperStatus"))
)
if mibBuilder.loadTexts:
    jnxVplsStatusChanged.setStatus(
        "current"
    )

jnxVplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 0, 2)
)
jnxVplsFwdFullAlarmRaised.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigVpnId"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    jnxVplsFwdFullAlarmRaised.setStatus(
        "current"
    )

jnxVplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 8, 0, 3)
)
jnxVplsFwdFullAlarmCleared.setObjects(
      *(("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigVpnId"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-DRAFT-01-MIB", "jnxVplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    jnxVplsFwdFullAlarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPLS-GENERIC-DRAFT-01-MIB",
    **{"PwIndexType": PwIndexType,
       "JnxVplsBgpRouteDistinguisher": JnxVplsBgpRouteDistinguisher,
       "JnxVplsBgpRouteTarget": JnxVplsBgpRouteTarget,
       "JnxVplsBgpRouteTargetType": JnxVplsBgpRouteTargetType,
       "jnxVplsGenericDraft01MIB": jnxVplsGenericDraft01MIB,
       "jnxVplsNotifications": jnxVplsNotifications,
       "jnxVplsStatusChanged": jnxVplsStatusChanged,
       "jnxVplsFwdFullAlarmRaised": jnxVplsFwdFullAlarmRaised,
       "jnxVplsFwdFullAlarmCleared": jnxVplsFwdFullAlarmCleared,
       "jnxVplsObjects": jnxVplsObjects,
       "jnxVplsConfigIndexNext": jnxVplsConfigIndexNext,
       "jnxVplsConfigTable": jnxVplsConfigTable,
       "jnxVplsConfigEntry": jnxVplsConfigEntry,
       "jnxVplsConfigIndex": jnxVplsConfigIndex,
       "jnxVplsConfigName": jnxVplsConfigName,
       "jnxVplsConfigDescr": jnxVplsConfigDescr,
       "jnxVplsConfigAdminStatus": jnxVplsConfigAdminStatus,
       "jnxVplsConfigMacLearning": jnxVplsConfigMacLearning,
       "jnxVplsConfigDiscardUnknownDest": jnxVplsConfigDiscardUnknownDest,
       "jnxVplsConfigMacAging": jnxVplsConfigMacAging,
       "jnxVplsConfigFwdFullHighWatermark": jnxVplsConfigFwdFullHighWatermark,
       "jnxVplsConfigFwdFullLowWatermark": jnxVplsConfigFwdFullLowWatermark,
       "jnxVplsConfigRowStatus": jnxVplsConfigRowStatus,
       "jnxVplsConfigMtu": jnxVplsConfigMtu,
       "jnxVplsConfigVpnId": jnxVplsConfigVpnId,
       "jnxVplsConfigServiceType": jnxVplsConfigServiceType,
       "jnxVplsConfigStorageType": jnxVplsConfigStorageType,
       "jnxVplsStatusTable": jnxVplsStatusTable,
       "jnxVplsStatusEntry": jnxVplsStatusEntry,
       "jnxVplsStatusOperStatus": jnxVplsStatusOperStatus,
       "jnxVplsStatusPeerCount": jnxVplsStatusPeerCount,
       "jnxVplsPwBindTable": jnxVplsPwBindTable,
       "jnxVplsPwBindEntry": jnxVplsPwBindEntry,
       "jnxVplsPwBindConfigType": jnxVplsPwBindConfigType,
       "jnxVplsPwBindType": jnxVplsPwBindType,
       "jnxVplsPwBindRowStatus": jnxVplsPwBindRowStatus,
       "jnxVplsPwBindStorageType": jnxVplsPwBindStorageType,
       "jnxVplsPwBindIndex": jnxVplsPwBindIndex,
       "jnxVplsBgpADConfigTable": jnxVplsBgpADConfigTable,
       "jnxVplsBgpADConfigEntry": jnxVplsBgpADConfigEntry,
       "jnxVplsBgpADConfigRouteDistinguisher": jnxVplsBgpADConfigRouteDistinguisher,
       "jnxVplsBgpADConfigPrefix": jnxVplsBgpADConfigPrefix,
       "jnxVplsBgpADConfigVplsId": jnxVplsBgpADConfigVplsId,
       "jnxVplsBgpADConfigRowStatus": jnxVplsBgpADConfigRowStatus,
       "jnxVplsBgpRteTargetTable": jnxVplsBgpRteTargetTable,
       "jnxVplsBgpRteTargetEntry": jnxVplsBgpRteTargetEntry,
       "jnxVplsBgpRteTargetIndex": jnxVplsBgpRteTargetIndex,
       "jnxVplsBgpRteTargetRTType": jnxVplsBgpRteTargetRTType,
       "jnxVplsBgpRteTargetRT": jnxVplsBgpRteTargetRT,
       "jnxVplsBgpRteTargetRTRowStatus": jnxVplsBgpRteTargetRTRowStatus,
       "jnxVplsStatusNotifEnable": jnxVplsStatusNotifEnable,
       "jnxVplsNotificationMaxRate": jnxVplsNotificationMaxRate,
       "jnxVplsConformance": jnxVplsConformance}
)
