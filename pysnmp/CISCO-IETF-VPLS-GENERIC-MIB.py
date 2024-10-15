# SNMP MIB module (CISCO-IETF-VPLS-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-VPLS-GENERIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:04 2024
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

(CpwVcIndexType,) = mibBuilder.importSymbols(
    "CISCO-IETF-PW-TC-MIB",
    "CpwVcIndexType")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

cvplsGenericMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 138)
)
cvplsGenericMIB.setRevisions(
        ("2007-10-22 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CvplsNotifications_ObjectIdentity = ObjectIdentity
cvplsNotifications = _CvplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 0)
)
_CvplsObjects_ObjectIdentity = ObjectIdentity
cvplsObjects = _CvplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1)
)
_CvplsConfigIndexNext_Type = Unsigned32
_CvplsConfigIndexNext_Object = MibScalar
cvplsConfigIndexNext = _CvplsConfigIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 1),
    _CvplsConfigIndexNext_Type()
)
cvplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvplsConfigIndexNext.setStatus("current")
_CvplsConfigTable_Object = MibTable
cvplsConfigTable = _CvplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2)
)
if mibBuilder.loadTexts:
    cvplsConfigTable.setStatus("current")
_CvplsConfigEntry_Object = MibTableRow
cvplsConfigEntry = _CvplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1)
)
cvplsConfigEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    cvplsConfigEntry.setStatus("current")


class _CvplsConfigIndex_Type(Unsigned32):
    """Custom type cvplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvplsConfigIndex_Type.__name__ = "Unsigned32"
_CvplsConfigIndex_Object = MibTableColumn
cvplsConfigIndex = _CvplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 1),
    _CvplsConfigIndex_Type()
)
cvplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvplsConfigIndex.setStatus("current")
_CvplsConfigName_Type = SnmpAdminString
_CvplsConfigName_Object = MibTableColumn
cvplsConfigName = _CvplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 2),
    _CvplsConfigName_Type()
)
cvplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigName.setStatus("current")
_CvplsConfigDescr_Type = SnmpAdminString
_CvplsConfigDescr_Object = MibTableColumn
cvplsConfigDescr = _CvplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 3),
    _CvplsConfigDescr_Type()
)
cvplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigDescr.setStatus("current")


class _CvplsConfigAdminStatus_Type(Integer32):
    """Custom type cvplsConfigAdminStatus based on Integer32"""
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


_CvplsConfigAdminStatus_Type.__name__ = "Integer32"
_CvplsConfigAdminStatus_Object = MibTableColumn
cvplsConfigAdminStatus = _CvplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 4),
    _CvplsConfigAdminStatus_Type()
)
cvplsConfigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigAdminStatus.setStatus("current")


class _CvplsConfigMacLearning_Type(TruthValue):
    """Custom type cvplsConfigMacLearning based on TruthValue"""


_CvplsConfigMacLearning_Object = MibTableColumn
cvplsConfigMacLearning = _CvplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 6),
    _CvplsConfigMacLearning_Type()
)
cvplsConfigMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigMacLearning.setStatus("current")


class _CvplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type cvplsConfigDiscardUnknownDest based on TruthValue"""


_CvplsConfigDiscardUnknownDest_Object = MibTableColumn
cvplsConfigDiscardUnknownDest = _CvplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 7),
    _CvplsConfigDiscardUnknownDest_Type()
)
cvplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigDiscardUnknownDest.setStatus("current")


class _CvplsConfigMacAging_Type(TruthValue):
    """Custom type cvplsConfigMacAging based on TruthValue"""


_CvplsConfigMacAging_Object = MibTableColumn
cvplsConfigMacAging = _CvplsConfigMacAging_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 8),
    _CvplsConfigMacAging_Type()
)
cvplsConfigMacAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigMacAging.setStatus("current")


class _CvplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type cvplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CvplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_CvplsConfigFwdFullHighWatermark_Object = MibTableColumn
cvplsConfigFwdFullHighWatermark = _CvplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 10),
    _CvplsConfigFwdFullHighWatermark_Type()
)
cvplsConfigFwdFullHighWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cvplsConfigFwdFullHighWatermark.setUnits("percentage")


class _CvplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type cvplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CvplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_CvplsConfigFwdFullLowWatermark_Object = MibTableColumn
cvplsConfigFwdFullLowWatermark = _CvplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 11),
    _CvplsConfigFwdFullLowWatermark_Type()
)
cvplsConfigFwdFullLowWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cvplsConfigFwdFullLowWatermark.setUnits("percentage")
_CvplsConfigRowStatus_Type = RowStatus
_CvplsConfigRowStatus_Object = MibTableColumn
cvplsConfigRowStatus = _CvplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 12),
    _CvplsConfigRowStatus_Type()
)
cvplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigRowStatus.setStatus("current")


class _CvplsConfigMtu_Type(Unsigned32):
    """Custom type cvplsConfigMtu based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_CvplsConfigMtu_Type.__name__ = "Unsigned32"
_CvplsConfigMtu_Object = MibTableColumn
cvplsConfigMtu = _CvplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 13),
    _CvplsConfigMtu_Type()
)
cvplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigMtu.setStatus("current")
_CvplsConfigVpnId_Type = VPNIdOrZero
_CvplsConfigVpnId_Object = MibTableColumn
cvplsConfigVpnId = _CvplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 14),
    _CvplsConfigVpnId_Type()
)
cvplsConfigVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvplsConfigVpnId.setStatus("current")


class _CvplsConfigServiceType_Type(Integer32):
    """Custom type cvplsConfigServiceType based on Integer32"""
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


_CvplsConfigServiceType_Type.__name__ = "Integer32"
_CvplsConfigServiceType_Object = MibTableColumn
cvplsConfigServiceType = _CvplsConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 15),
    _CvplsConfigServiceType_Type()
)
cvplsConfigServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigServiceType.setStatus("current")


class _CvplsConfigStorageType_Type(StorageType):
    """Custom type cvplsConfigStorageType based on StorageType"""


_CvplsConfigStorageType_Object = MibTableColumn
cvplsConfigStorageType = _CvplsConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 2, 1, 16),
    _CvplsConfigStorageType_Type()
)
cvplsConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsConfigStorageType.setStatus("current")
_CvplsStatusTable_Object = MibTable
cvplsStatusTable = _CvplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 3)
)
if mibBuilder.loadTexts:
    cvplsStatusTable.setStatus("current")
_CvplsStatusEntry_Object = MibTableRow
cvplsStatusEntry = _CvplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 3, 1)
)
cvplsStatusEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    cvplsStatusEntry.setStatus("current")


class _CvplsStatusOperStatus_Type(Integer32):
    """Custom type cvplsStatusOperStatus based on Integer32"""
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


_CvplsStatusOperStatus_Type.__name__ = "Integer32"
_CvplsStatusOperStatus_Object = MibTableColumn
cvplsStatusOperStatus = _CvplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 3, 1, 1),
    _CvplsStatusOperStatus_Type()
)
cvplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvplsStatusOperStatus.setStatus("current")
_CvplsStatusPeerCount_Type = Counter32
_CvplsStatusPeerCount_Object = MibTableColumn
cvplsStatusPeerCount = _CvplsStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 3, 1, 2),
    _CvplsStatusPeerCount_Type()
)
cvplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvplsStatusPeerCount.setStatus("current")
_CvplsPwBindTable_Object = MibTable
cvplsPwBindTable = _CvplsPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 4)
)
if mibBuilder.loadTexts:
    cvplsPwBindTable.setStatus("current")
_CvplsPwBindEntry_Object = MibTableRow
cvplsPwBindEntry = _CvplsPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 4, 1)
)
cvplsPwBindEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    cvplsPwBindEntry.setStatus("current")
_CvplsPwBindIndex_Type = CpwVcIndexType
_CvplsPwBindIndex_Object = MibTableColumn
cvplsPwBindIndex = _CvplsPwBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 4, 1, 1),
    _CvplsPwBindIndex_Type()
)
cvplsPwBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvplsPwBindIndex.setStatus("current")


class _CvplsPwBindConfigType_Type(Integer32):
    """Custom type cvplsPwBindConfigType based on Integer32"""
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


_CvplsPwBindConfigType_Type.__name__ = "Integer32"
_CvplsPwBindConfigType_Object = MibTableColumn
cvplsPwBindConfigType = _CvplsPwBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 4, 1, 2),
    _CvplsPwBindConfigType_Type()
)
cvplsPwBindConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsPwBindConfigType.setStatus("current")


class _CvplsPwBindType_Type(Integer32):
    """Custom type cvplsPwBindType based on Integer32"""
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


_CvplsPwBindType_Type.__name__ = "Integer32"
_CvplsPwBindType_Object = MibTableColumn
cvplsPwBindType = _CvplsPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 4, 1, 3),
    _CvplsPwBindType_Type()
)
cvplsPwBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsPwBindType.setStatus("current")
_CvplsPwBindRowStatus_Type = RowStatus
_CvplsPwBindRowStatus_Object = MibTableColumn
cvplsPwBindRowStatus = _CvplsPwBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 4, 1, 4),
    _CvplsPwBindRowStatus_Type()
)
cvplsPwBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsPwBindRowStatus.setStatus("current")


class _CvplsPwBindStorageType_Type(StorageType):
    """Custom type cvplsPwBindStorageType based on StorageType"""


_CvplsPwBindStorageType_Object = MibTableColumn
cvplsPwBindStorageType = _CvplsPwBindStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 4, 1, 5),
    _CvplsPwBindStorageType_Type()
)
cvplsPwBindStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvplsPwBindStorageType.setStatus("current")


class _CvplsStatusNotifEnable_Type(TruthValue):
    """Custom type cvplsStatusNotifEnable based on TruthValue"""


_CvplsStatusNotifEnable_Object = MibScalar
cvplsStatusNotifEnable = _CvplsStatusNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 5),
    _CvplsStatusNotifEnable_Type()
)
cvplsStatusNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvplsStatusNotifEnable.setStatus("current")


class _CvplsNotificationMaxRate_Type(Unsigned32):
    """Custom type cvplsNotificationMaxRate based on Unsigned32"""
    defaultValue = 0


_CvplsNotificationMaxRate_Object = MibScalar
cvplsNotificationMaxRate = _CvplsNotificationMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 1, 6),
    _CvplsNotificationMaxRate_Type()
)
cvplsNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvplsNotificationMaxRate.setStatus("current")
_CvplsConformance_ObjectIdentity = ObjectIdentity
cvplsConformance = _CvplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2)
)
_CvplsCompliances_ObjectIdentity = ObjectIdentity
cvplsCompliances = _CvplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2, 1)
)
_CvplsGroups_ObjectIdentity = ObjectIdentity
cvplsGroups = _CvplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2, 2)
)

# Managed Objects groups

cvplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2, 2, 1)
)
cvplsGroup.setObjects(
      *(("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigName"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigDescr"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigAdminStatus"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigMacLearning"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigDiscardUnknownDest"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigMacAging"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigVpnId"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigFwdFullHighWatermark"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigFwdFullLowWatermark"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigRowStatus"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndexNext"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigMtu"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigServiceType"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigStorageType"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsStatusOperStatus"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsStatusPeerCount"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsStatusNotifEnable"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    cvplsGroup.setStatus("current")

cvplsPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2, 2, 2)
)
cvplsPwBindGroup.setObjects(
      *(("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindConfigType"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindType"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindRowStatus"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindStorageType"))
)
if mibBuilder.loadTexts:
    cvplsPwBindGroup.setStatus("current")


# Notification objects

cvplsStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 0, 1)
)
cvplsStatusChanged.setObjects(
      *(("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigVpnId"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigAdminStatus"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsStatusOperStatus"))
)
if mibBuilder.loadTexts:
    cvplsStatusChanged.setStatus(
        "current"
    )

cvplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 0, 2)
)
cvplsFwdFullAlarmRaised.setObjects(
      *(("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigVpnId"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigFwdFullHighWatermark"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    cvplsFwdFullAlarmRaised.setStatus(
        "current"
    )

cvplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 0, 3)
)
cvplsFwdFullAlarmCleared.setObjects(
      *(("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigVpnId"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigFwdFullHighWatermark"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    cvplsFwdFullAlarmCleared.setStatus(
        "current"
    )


# Notifications groups

cvplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2, 2, 3)
)
cvplsNotificationGroup.setObjects(
      *(("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsStatusChanged"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsFwdFullAlarmRaised"),
        ("CISCO-IETF-VPLS-GENERIC-MIB", "cvplsFwdFullAlarmCleared"))
)
if mibBuilder.loadTexts:
    cvplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cvplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvplsModuleFullCompliance.setStatus(
        "current"
    )

cvplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 138, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cvplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-VPLS-GENERIC-MIB",
    **{"cvplsGenericMIB": cvplsGenericMIB,
       "cvplsNotifications": cvplsNotifications,
       "cvplsStatusChanged": cvplsStatusChanged,
       "cvplsFwdFullAlarmRaised": cvplsFwdFullAlarmRaised,
       "cvplsFwdFullAlarmCleared": cvplsFwdFullAlarmCleared,
       "cvplsObjects": cvplsObjects,
       "cvplsConfigIndexNext": cvplsConfigIndexNext,
       "cvplsConfigTable": cvplsConfigTable,
       "cvplsConfigEntry": cvplsConfigEntry,
       "cvplsConfigIndex": cvplsConfigIndex,
       "cvplsConfigName": cvplsConfigName,
       "cvplsConfigDescr": cvplsConfigDescr,
       "cvplsConfigAdminStatus": cvplsConfigAdminStatus,
       "cvplsConfigMacLearning": cvplsConfigMacLearning,
       "cvplsConfigDiscardUnknownDest": cvplsConfigDiscardUnknownDest,
       "cvplsConfigMacAging": cvplsConfigMacAging,
       "cvplsConfigFwdFullHighWatermark": cvplsConfigFwdFullHighWatermark,
       "cvplsConfigFwdFullLowWatermark": cvplsConfigFwdFullLowWatermark,
       "cvplsConfigRowStatus": cvplsConfigRowStatus,
       "cvplsConfigMtu": cvplsConfigMtu,
       "cvplsConfigVpnId": cvplsConfigVpnId,
       "cvplsConfigServiceType": cvplsConfigServiceType,
       "cvplsConfigStorageType": cvplsConfigStorageType,
       "cvplsStatusTable": cvplsStatusTable,
       "cvplsStatusEntry": cvplsStatusEntry,
       "cvplsStatusOperStatus": cvplsStatusOperStatus,
       "cvplsStatusPeerCount": cvplsStatusPeerCount,
       "cvplsPwBindTable": cvplsPwBindTable,
       "cvplsPwBindEntry": cvplsPwBindEntry,
       "cvplsPwBindIndex": cvplsPwBindIndex,
       "cvplsPwBindConfigType": cvplsPwBindConfigType,
       "cvplsPwBindType": cvplsPwBindType,
       "cvplsPwBindRowStatus": cvplsPwBindRowStatus,
       "cvplsPwBindStorageType": cvplsPwBindStorageType,
       "cvplsStatusNotifEnable": cvplsStatusNotifEnable,
       "cvplsNotificationMaxRate": cvplsNotificationMaxRate,
       "cvplsConformance": cvplsConformance,
       "cvplsCompliances": cvplsCompliances,
       "cvplsModuleFullCompliance": cvplsModuleFullCompliance,
       "cvplsModuleReadOnlyCompliance": cvplsModuleReadOnlyCompliance,
       "cvplsGroups": cvplsGroups,
       "cvplsGroup": cvplsGroup,
       "cvplsPwBindGroup": cvplsPwBindGroup,
       "cvplsNotificationGroup": cvplsNotificationGroup}
)
