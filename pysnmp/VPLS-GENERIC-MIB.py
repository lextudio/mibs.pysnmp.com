# SNMP MIB module (VPLS-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPLS-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:43 2024
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

(pwIndex,) = mibBuilder.importSymbols(
    "PW-STD-MIB",
    "pwIndex")

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

vplsGenericMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 274)
)
vplsGenericMIB.setRevisions(
        ("2014-05-19 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VplsBgpRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VplsBgpRouteTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VplsBgpRouteTargetType(Integer32, TextualConvention):
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

_VplsNotifications_ObjectIdentity = ObjectIdentity
vplsNotifications = _VplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 274, 0)
)
_VplsObjects_ObjectIdentity = ObjectIdentity
vplsObjects = _VplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 274, 1)
)
_VplsConfigIndexNext_Type = Unsigned32
_VplsConfigIndexNext_Object = MibScalar
vplsConfigIndexNext = _VplsConfigIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 1),
    _VplsConfigIndexNext_Type()
)
vplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsConfigIndexNext.setStatus("current")
_VplsConfigTable_Object = MibTable
vplsConfigTable = _VplsConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2)
)
if mibBuilder.loadTexts:
    vplsConfigTable.setStatus("current")
_VplsConfigEntry_Object = MibTableRow
vplsConfigEntry = _VplsConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1)
)
vplsConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsConfigEntry.setStatus("current")


class _VplsConfigIndex_Type(Unsigned32):
    """Custom type vplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VplsConfigIndex_Type.__name__ = "Unsigned32"
_VplsConfigIndex_Object = MibTableColumn
vplsConfigIndex = _VplsConfigIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 1),
    _VplsConfigIndex_Type()
)
vplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsConfigIndex.setStatus("current")
_VplsConfigName_Type = SnmpAdminString
_VplsConfigName_Object = MibTableColumn
vplsConfigName = _VplsConfigName_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 2),
    _VplsConfigName_Type()
)
vplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigName.setStatus("current")
_VplsConfigDescr_Type = SnmpAdminString
_VplsConfigDescr_Object = MibTableColumn
vplsConfigDescr = _VplsConfigDescr_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 3),
    _VplsConfigDescr_Type()
)
vplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDescr.setStatus("current")


class _VplsConfigAdminStatus_Type(Integer32):
    """Custom type vplsConfigAdminStatus based on Integer32"""
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


_VplsConfigAdminStatus_Type.__name__ = "Integer32"
_VplsConfigAdminStatus_Object = MibTableColumn
vplsConfigAdminStatus = _VplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 4),
    _VplsConfigAdminStatus_Type()
)
vplsConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigAdminStatus.setStatus("current")


class _VplsConfigMacLearning_Type(TruthValue):
    """Custom type vplsConfigMacLearning based on TruthValue"""


_VplsConfigMacLearning_Object = MibTableColumn
vplsConfigMacLearning = _VplsConfigMacLearning_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 6),
    _VplsConfigMacLearning_Type()
)
vplsConfigMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacLearning.setStatus("current")


class _VplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type vplsConfigDiscardUnknownDest based on TruthValue"""


_VplsConfigDiscardUnknownDest_Object = MibTableColumn
vplsConfigDiscardUnknownDest = _VplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 7),
    _VplsConfigDiscardUnknownDest_Type()
)
vplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigDiscardUnknownDest.setStatus("current")


class _VplsConfigMacAging_Type(TruthValue):
    """Custom type vplsConfigMacAging based on TruthValue"""


_VplsConfigMacAging_Object = MibTableColumn
vplsConfigMacAging = _VplsConfigMacAging_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 8),
    _VplsConfigMacAging_Type()
)
vplsConfigMacAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMacAging.setStatus("current")


class _VplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type vplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_VplsConfigFwdFullHighWatermark_Object = MibTableColumn
vplsConfigFwdFullHighWatermark = _VplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 10),
    _VplsConfigFwdFullHighWatermark_Type()
)
vplsConfigFwdFullHighWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigFwdFullHighWatermark.setUnits("percentage")


class _VplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type vplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_VplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_VplsConfigFwdFullLowWatermark_Object = MibTableColumn
vplsConfigFwdFullLowWatermark = _VplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 11),
    _VplsConfigFwdFullLowWatermark_Type()
)
vplsConfigFwdFullLowWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    vplsConfigFwdFullLowWatermark.setUnits("percentage")
_VplsConfigRowStatus_Type = RowStatus
_VplsConfigRowStatus_Object = MibTableColumn
vplsConfigRowStatus = _VplsConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 12),
    _VplsConfigRowStatus_Type()
)
vplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigRowStatus.setStatus("current")


class _VplsConfigMtu_Type(Unsigned32):
    """Custom type vplsConfigMtu based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9192),
    )


_VplsConfigMtu_Type.__name__ = "Unsigned32"
_VplsConfigMtu_Object = MibTableColumn
vplsConfigMtu = _VplsConfigMtu_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 13),
    _VplsConfigMtu_Type()
)
vplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigMtu.setStatus("current")
_VplsConfigVpnId_Type = VPNIdOrZero
_VplsConfigVpnId_Object = MibTableColumn
vplsConfigVpnId = _VplsConfigVpnId_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 14),
    _VplsConfigVpnId_Type()
)
vplsConfigVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigVpnId.setStatus("current")


class _VplsConfigStorageType_Type(StorageType):
    """Custom type vplsConfigStorageType based on StorageType"""


_VplsConfigStorageType_Object = MibTableColumn
vplsConfigStorageType = _VplsConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 15),
    _VplsConfigStorageType_Type()
)
vplsConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigStorageType.setStatus("current")


class _VplsConfigSignalingType_Type(Integer32):
    """Custom type vplsConfigSignalingType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("ldp", 1),
          ("none", 3))
    )


_VplsConfigSignalingType_Type.__name__ = "Integer32"
_VplsConfigSignalingType_Object = MibTableColumn
vplsConfigSignalingType = _VplsConfigSignalingType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 2, 1, 16),
    _VplsConfigSignalingType_Type()
)
vplsConfigSignalingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsConfigSignalingType.setStatus("current")
_VplsStatusTable_Object = MibTable
vplsStatusTable = _VplsStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 3)
)
if mibBuilder.loadTexts:
    vplsStatusTable.setStatus("current")
_VplsStatusEntry_Object = MibTableRow
vplsStatusEntry = _VplsStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vplsStatusEntry.setStatus("current")


class _VplsStatusOperStatus_Type(Integer32):
    """Custom type vplsStatusOperStatus based on Integer32"""
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


_VplsStatusOperStatus_Type.__name__ = "Integer32"
_VplsStatusOperStatus_Object = MibTableColumn
vplsStatusOperStatus = _VplsStatusOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 3, 1, 1),
    _VplsStatusOperStatus_Type()
)
vplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusOperStatus.setStatus("current")
_VplsStatusPeerCount_Type = Counter32
_VplsStatusPeerCount_Object = MibTableColumn
vplsStatusPeerCount = _VplsStatusPeerCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 3, 1, 2),
    _VplsStatusPeerCount_Type()
)
vplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vplsStatusPeerCount.setStatus("current")
_VplsPwBindTable_Object = MibTable
vplsPwBindTable = _VplsPwBindTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 4)
)
if mibBuilder.loadTexts:
    vplsPwBindTable.setStatus("current")
_VplsPwBindEntry_Object = MibTableRow
vplsPwBindEntry = _VplsPwBindEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1)
)
vplsPwBindEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "PW-STD-MIB", "pwIndex"),
)
if mibBuilder.loadTexts:
    vplsPwBindEntry.setStatus("current")


class _VplsPwBindConfigType_Type(Integer32):
    """Custom type vplsPwBindConfigType based on Integer32"""
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


_VplsPwBindConfigType_Type.__name__ = "Integer32"
_VplsPwBindConfigType_Object = MibTableColumn
vplsPwBindConfigType = _VplsPwBindConfigType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 1),
    _VplsPwBindConfigType_Type()
)
vplsPwBindConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindConfigType.setStatus("current")


class _VplsPwBindType_Type(Integer32):
    """Custom type vplsPwBindType based on Integer32"""
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


_VplsPwBindType_Type.__name__ = "Integer32"
_VplsPwBindType_Object = MibTableColumn
vplsPwBindType = _VplsPwBindType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 2),
    _VplsPwBindType_Type()
)
vplsPwBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindType.setStatus("current")
_VplsPwBindRowStatus_Type = RowStatus
_VplsPwBindRowStatus_Object = MibTableColumn
vplsPwBindRowStatus = _VplsPwBindRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 3),
    _VplsPwBindRowStatus_Type()
)
vplsPwBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindRowStatus.setStatus("current")


class _VplsPwBindStorageType_Type(StorageType):
    """Custom type vplsPwBindStorageType based on StorageType"""


_VplsPwBindStorageType_Object = MibTableColumn
vplsPwBindStorageType = _VplsPwBindStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 4, 1, 4),
    _VplsPwBindStorageType_Type()
)
vplsPwBindStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsPwBindStorageType.setStatus("current")
_VplsBgpADConfigTable_Object = MibTable
vplsBgpADConfigTable = _VplsBgpADConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 5)
)
if mibBuilder.loadTexts:
    vplsBgpADConfigTable.setStatus("current")
_VplsBgpADConfigEntry_Object = MibTableRow
vplsBgpADConfigEntry = _VplsBgpADConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1)
)
vplsBgpADConfigEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpADConfigEntry.setStatus("current")
_VplsBgpADConfigRouteDistinguisher_Type = VplsBgpRouteDistinguisher
_VplsBgpADConfigRouteDistinguisher_Object = MibTableColumn
vplsBgpADConfigRouteDistinguisher = _VplsBgpADConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 1),
    _VplsBgpADConfigRouteDistinguisher_Type()
)
vplsBgpADConfigRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigRouteDistinguisher.setStatus("current")


class _VplsBgpADConfigPrefix_Type(Unsigned32):
    """Custom type vplsBgpADConfigPrefix based on Unsigned32"""
    defaultValue = 0


_VplsBgpADConfigPrefix_Object = MibTableColumn
vplsBgpADConfigPrefix = _VplsBgpADConfigPrefix_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 2),
    _VplsBgpADConfigPrefix_Type()
)
vplsBgpADConfigPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigPrefix.setStatus("current")
_VplsBgpADConfigVplsId_Type = VplsBgpRouteDistinguisher
_VplsBgpADConfigVplsId_Object = MibTableColumn
vplsBgpADConfigVplsId = _VplsBgpADConfigVplsId_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 3),
    _VplsBgpADConfigVplsId_Type()
)
vplsBgpADConfigVplsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigVplsId.setStatus("current")
_VplsBgpADConfigRowStatus_Type = RowStatus
_VplsBgpADConfigRowStatus_Object = MibTableColumn
vplsBgpADConfigRowStatus = _VplsBgpADConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 4),
    _VplsBgpADConfigRowStatus_Type()
)
vplsBgpADConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigRowStatus.setStatus("current")


class _VplsBgpADConfigStorageType_Type(StorageType):
    """Custom type vplsBgpADConfigStorageType based on StorageType"""


_VplsBgpADConfigStorageType_Object = MibTableColumn
vplsBgpADConfigStorageType = _VplsBgpADConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 5, 1, 5),
    _VplsBgpADConfigStorageType_Type()
)
vplsBgpADConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpADConfigStorageType.setStatus("current")
_VplsBgpRteTargetTable_Object = MibTable
vplsBgpRteTargetTable = _VplsBgpRteTargetTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 6)
)
if mibBuilder.loadTexts:
    vplsBgpRteTargetTable.setStatus("current")
_VplsBgpRteTargetEntry_Object = MibTableRow
vplsBgpRteTargetEntry = _VplsBgpRteTargetEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1)
)
vplsBgpRteTargetEntry.setIndexNames(
    (0, "VPLS-GENERIC-MIB", "vplsConfigIndex"),
    (0, "VPLS-GENERIC-MIB", "vplsBgpRteTargetIndex"),
)
if mibBuilder.loadTexts:
    vplsBgpRteTargetEntry.setStatus("current")
_VplsBgpRteTargetIndex_Type = Unsigned32
_VplsBgpRteTargetIndex_Object = MibTableColumn
vplsBgpRteTargetIndex = _VplsBgpRteTargetIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 1),
    _VplsBgpRteTargetIndex_Type()
)
vplsBgpRteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vplsBgpRteTargetIndex.setStatus("current")
_VplsBgpRteTargetRTType_Type = VplsBgpRouteTargetType
_VplsBgpRteTargetRTType_Object = MibTableColumn
vplsBgpRteTargetRTType = _VplsBgpRteTargetRTType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 2),
    _VplsBgpRteTargetRTType_Type()
)
vplsBgpRteTargetRTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetRTType.setStatus("current")
_VplsBgpRteTargetRT_Type = VplsBgpRouteTarget
_VplsBgpRteTargetRT_Object = MibTableColumn
vplsBgpRteTargetRT = _VplsBgpRteTargetRT_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 3),
    _VplsBgpRteTargetRT_Type()
)
vplsBgpRteTargetRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetRT.setStatus("current")
_VplsBgpRteTargetRowStatus_Type = RowStatus
_VplsBgpRteTargetRowStatus_Object = MibTableColumn
vplsBgpRteTargetRowStatus = _VplsBgpRteTargetRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 4),
    _VplsBgpRteTargetRowStatus_Type()
)
vplsBgpRteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetRowStatus.setStatus("current")


class _VplsBgpRteTargetStorageType_Type(StorageType):
    """Custom type vplsBgpRteTargetStorageType based on StorageType"""


_VplsBgpRteTargetStorageType_Object = MibTableColumn
vplsBgpRteTargetStorageType = _VplsBgpRteTargetStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 6, 1, 5),
    _VplsBgpRteTargetStorageType_Type()
)
vplsBgpRteTargetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vplsBgpRteTargetStorageType.setStatus("current")


class _VplsStatusNotifEnable_Type(TruthValue):
    """Custom type vplsStatusNotifEnable based on TruthValue"""


_VplsStatusNotifEnable_Object = MibScalar
vplsStatusNotifEnable = _VplsStatusNotifEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 7),
    _VplsStatusNotifEnable_Type()
)
vplsStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsStatusNotifEnable.setStatus("current")


class _VplsNotificationMaxRate_Type(Unsigned32):
    """Custom type vplsNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_VplsNotificationMaxRate_Object = MibScalar
vplsNotificationMaxRate = _VplsNotificationMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 274, 1, 8),
    _VplsNotificationMaxRate_Type()
)
vplsNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vplsNotificationMaxRate.setStatus("current")
_VplsConformance_ObjectIdentity = ObjectIdentity
vplsConformance = _VplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 274, 2)
)
_VplsCompliances_ObjectIdentity = ObjectIdentity
vplsCompliances = _VplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 274, 2, 1)
)
_VplsGroups_ObjectIdentity = ObjectIdentity
vplsGroups = _VplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 274, 2, 2)
)
vplsConfigEntry.registerAugmentions(
    ("VPLS-GENERIC-MIB",
     "vplsStatusEntry")
)
vplsStatusEntry.setIndexNames(*vplsConfigEntry.getIndexNames())

# Managed Objects groups

vplsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 274, 2, 2, 1)
)
vplsGroup.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsConfigName"),
        ("VPLS-GENERIC-MIB", "vplsBgpADConfigRouteDistinguisher"),
        ("VPLS-GENERIC-MIB", "vplsBgpRteTargetRTType"),
        ("VPLS-GENERIC-MIB", "vplsBgpRteTargetRT"),
        ("VPLS-GENERIC-MIB", "vplsBgpRteTargetRowStatus"),
        ("VPLS-GENERIC-MIB", "vplsBgpRteTargetStorageType"),
        ("VPLS-GENERIC-MIB", "vplsBgpADConfigPrefix"),
        ("VPLS-GENERIC-MIB", "vplsBgpADConfigVplsId"),
        ("VPLS-GENERIC-MIB", "vplsBgpADConfigRowStatus"),
        ("VPLS-GENERIC-MIB", "vplsBgpADConfigStorageType"),
        ("VPLS-GENERIC-MIB", "vplsConfigDescr"),
        ("VPLS-GENERIC-MIB", "vplsConfigAdminStatus"),
        ("VPLS-GENERIC-MIB", "vplsConfigMacLearning"),
        ("VPLS-GENERIC-MIB", "vplsConfigDiscardUnknownDest"),
        ("VPLS-GENERIC-MIB", "vplsConfigMacAging"),
        ("VPLS-GENERIC-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"),
        ("VPLS-GENERIC-MIB", "vplsConfigRowStatus"),
        ("VPLS-GENERIC-MIB", "vplsConfigIndexNext"),
        ("VPLS-GENERIC-MIB", "vplsConfigMtu"),
        ("VPLS-GENERIC-MIB", "vplsConfigStorageType"),
        ("VPLS-GENERIC-MIB", "vplsConfigSignalingType"),
        ("VPLS-GENERIC-MIB", "vplsStatusOperStatus"),
        ("VPLS-GENERIC-MIB", "vplsStatusPeerCount"),
        ("VPLS-GENERIC-MIB", "vplsStatusNotifEnable"),
        ("VPLS-GENERIC-MIB", "vplsNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    vplsGroup.setStatus("current")

vplsPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 274, 2, 2, 2)
)
vplsPwBindGroup.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsPwBindConfigType"),
        ("VPLS-GENERIC-MIB", "vplsPwBindType"),
        ("VPLS-GENERIC-MIB", "vplsPwBindRowStatus"),
        ("VPLS-GENERIC-MIB", "vplsPwBindStorageType"))
)
if mibBuilder.loadTexts:
    vplsPwBindGroup.setStatus("current")


# Notification objects

vplsStatusChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 274, 0, 1)
)
vplsStatusChanged.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-MIB", "vplsConfigAdminStatus"),
        ("VPLS-GENERIC-MIB", "vplsStatusOperStatus"))
)
if mibBuilder.loadTexts:
    vplsStatusChanged.setStatus(
        "current"
    )

vplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 274, 0, 2)
)
vplsFwdFullAlarmRaised.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    vplsFwdFullAlarmRaised.setStatus(
        "current"
    )

vplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 274, 0, 3)
)
vplsFwdFullAlarmCleared.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsConfigVpnId"),
        ("VPLS-GENERIC-MIB", "vplsConfigFwdFullHighWatermark"),
        ("VPLS-GENERIC-MIB", "vplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    vplsFwdFullAlarmCleared.setStatus(
        "current"
    )


# Notifications groups

vplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 274, 2, 2, 3)
)
vplsNotificationGroup.setObjects(
      *(("VPLS-GENERIC-MIB", "vplsStatusChanged"),
        ("VPLS-GENERIC-MIB", "vplsFwdFullAlarmRaised"),
        ("VPLS-GENERIC-MIB", "vplsFwdFullAlarmCleared"))
)
if mibBuilder.loadTexts:
    vplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 274, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vplsModuleFullCompliance.setStatus(
        "current"
    )

vplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 274, 2, 1, 2)
)
if mibBuilder.loadTexts:
    vplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPLS-GENERIC-MIB",
    **{"VplsBgpRouteDistinguisher": VplsBgpRouteDistinguisher,
       "VplsBgpRouteTarget": VplsBgpRouteTarget,
       "VplsBgpRouteTargetType": VplsBgpRouteTargetType,
       "vplsGenericMIB": vplsGenericMIB,
       "vplsNotifications": vplsNotifications,
       "vplsStatusChanged": vplsStatusChanged,
       "vplsFwdFullAlarmRaised": vplsFwdFullAlarmRaised,
       "vplsFwdFullAlarmCleared": vplsFwdFullAlarmCleared,
       "vplsObjects": vplsObjects,
       "vplsConfigIndexNext": vplsConfigIndexNext,
       "vplsConfigTable": vplsConfigTable,
       "vplsConfigEntry": vplsConfigEntry,
       "vplsConfigIndex": vplsConfigIndex,
       "vplsConfigName": vplsConfigName,
       "vplsConfigDescr": vplsConfigDescr,
       "vplsConfigAdminStatus": vplsConfigAdminStatus,
       "vplsConfigMacLearning": vplsConfigMacLearning,
       "vplsConfigDiscardUnknownDest": vplsConfigDiscardUnknownDest,
       "vplsConfigMacAging": vplsConfigMacAging,
       "vplsConfigFwdFullHighWatermark": vplsConfigFwdFullHighWatermark,
       "vplsConfigFwdFullLowWatermark": vplsConfigFwdFullLowWatermark,
       "vplsConfigRowStatus": vplsConfigRowStatus,
       "vplsConfigMtu": vplsConfigMtu,
       "vplsConfigVpnId": vplsConfigVpnId,
       "vplsConfigStorageType": vplsConfigStorageType,
       "vplsConfigSignalingType": vplsConfigSignalingType,
       "vplsStatusTable": vplsStatusTable,
       "vplsStatusEntry": vplsStatusEntry,
       "vplsStatusOperStatus": vplsStatusOperStatus,
       "vplsStatusPeerCount": vplsStatusPeerCount,
       "vplsPwBindTable": vplsPwBindTable,
       "vplsPwBindEntry": vplsPwBindEntry,
       "vplsPwBindConfigType": vplsPwBindConfigType,
       "vplsPwBindType": vplsPwBindType,
       "vplsPwBindRowStatus": vplsPwBindRowStatus,
       "vplsPwBindStorageType": vplsPwBindStorageType,
       "vplsBgpADConfigTable": vplsBgpADConfigTable,
       "vplsBgpADConfigEntry": vplsBgpADConfigEntry,
       "vplsBgpADConfigRouteDistinguisher": vplsBgpADConfigRouteDistinguisher,
       "vplsBgpADConfigPrefix": vplsBgpADConfigPrefix,
       "vplsBgpADConfigVplsId": vplsBgpADConfigVplsId,
       "vplsBgpADConfigRowStatus": vplsBgpADConfigRowStatus,
       "vplsBgpADConfigStorageType": vplsBgpADConfigStorageType,
       "vplsBgpRteTargetTable": vplsBgpRteTargetTable,
       "vplsBgpRteTargetEntry": vplsBgpRteTargetEntry,
       "vplsBgpRteTargetIndex": vplsBgpRteTargetIndex,
       "vplsBgpRteTargetRTType": vplsBgpRteTargetRTType,
       "vplsBgpRteTargetRT": vplsBgpRteTargetRT,
       "vplsBgpRteTargetRowStatus": vplsBgpRteTargetRowStatus,
       "vplsBgpRteTargetStorageType": vplsBgpRteTargetStorageType,
       "vplsStatusNotifEnable": vplsStatusNotifEnable,
       "vplsNotificationMaxRate": vplsNotificationMaxRate,
       "vplsConformance": vplsConformance,
       "vplsCompliances": vplsCompliances,
       "vplsModuleFullCompliance": vplsModuleFullCompliance,
       "vplsModuleReadOnlyCompliance": vplsModuleReadOnlyCompliance,
       "vplsGroups": vplsGroups,
       "vplsGroup": vplsGroup,
       "vplsPwBindGroup": vplsPwBindGroup,
       "vplsNotificationGroup": vplsNotificationGroup}
)
