# SNMP MIB module (APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:56 2024
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
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

apsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49)
)
apsMIB.setRevisions(
        ("2003-02-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApsK1K2(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class ApsSwitchCommand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("exercise", 8),
          ("forcedSwitchProtectToWork", 5),
          ("forcedSwitchWorkToProtect", 4),
          ("lockoutOfProtection", 3),
          ("manualSwitchProtectToWork", 7),
          ("manualSwitchWorkToProtect", 6),
          ("noCmd", 1))
    )



class ApsControlCommand(Integer32, TextualConvention):
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
        *(("clearLockoutWorkingChannel", 3),
          ("lockoutWorkingChannel", 2),
          ("noCmd", 1))
    )



# MIB Managed Objects in the order of their OIDs

_ApsMIBObjects_ObjectIdentity = ObjectIdentity
apsMIBObjects = _ApsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 1)
)
_ApsConfig_ObjectIdentity = ObjectIdentity
apsConfig = _ApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1)
)
_ApsConfigGroups_Type = Gauge32
_ApsConfigGroups_Object = MibScalar
apsConfigGroups = _ApsConfigGroups_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 1),
    _ApsConfigGroups_Type()
)
apsConfigGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsConfigGroups.setStatus("current")
_ApsConfigTable_Object = MibTable
apsConfigTable = _ApsConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2)
)
if mibBuilder.loadTexts:
    apsConfigTable.setStatus("current")
_ApsConfigEntry_Object = MibTableRow
apsConfigEntry = _ApsConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1)
)
apsConfigEntry.setIndexNames(
    (1, "APS-MIB", "apsConfigName"),
)
if mibBuilder.loadTexts:
    apsConfigEntry.setStatus("current")


class _ApsConfigName_Type(SnmpAdminString):
    """Custom type apsConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApsConfigName_Type.__name__ = "SnmpAdminString"
_ApsConfigName_Object = MibTableColumn
apsConfigName = _ApsConfigName_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 1),
    _ApsConfigName_Type()
)
apsConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsConfigName.setStatus("current")
_ApsConfigRowStatus_Type = RowStatus
_ApsConfigRowStatus_Object = MibTableColumn
apsConfigRowStatus = _ApsConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 2),
    _ApsConfigRowStatus_Type()
)
apsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigRowStatus.setStatus("current")


class _ApsConfigMode_Type(Integer32):
    """Custom type apsConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 1),
          ("onePlusOneCompatible", 3),
          ("onePlusOneOptimized", 4),
          ("oneToN", 2))
    )


_ApsConfigMode_Type.__name__ = "Integer32"
_ApsConfigMode_Object = MibTableColumn
apsConfigMode = _ApsConfigMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 3),
    _ApsConfigMode_Type()
)
apsConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigMode.setStatus("current")


class _ApsConfigRevert_Type(Integer32):
    """Custom type apsConfigRevert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_ApsConfigRevert_Type.__name__ = "Integer32"
_ApsConfigRevert_Object = MibTableColumn
apsConfigRevert = _ApsConfigRevert_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 4),
    _ApsConfigRevert_Type()
)
apsConfigRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigRevert.setStatus("current")


class _ApsConfigDirection_Type(Integer32):
    """Custom type apsConfigDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_ApsConfigDirection_Type.__name__ = "Integer32"
_ApsConfigDirection_Object = MibTableColumn
apsConfigDirection = _ApsConfigDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 5),
    _ApsConfigDirection_Type()
)
apsConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigDirection.setStatus("current")


class _ApsConfigExtraTraffic_Type(Integer32):
    """Custom type apsConfigExtraTraffic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApsConfigExtraTraffic_Type.__name__ = "Integer32"
_ApsConfigExtraTraffic_Object = MibTableColumn
apsConfigExtraTraffic = _ApsConfigExtraTraffic_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 6),
    _ApsConfigExtraTraffic_Type()
)
apsConfigExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigExtraTraffic.setStatus("current")


class _ApsConfigSdBerThreshold_Type(Integer32):
    """Custom type apsConfigSdBerThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_ApsConfigSdBerThreshold_Type.__name__ = "Integer32"
_ApsConfigSdBerThreshold_Object = MibTableColumn
apsConfigSdBerThreshold = _ApsConfigSdBerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 7),
    _ApsConfigSdBerThreshold_Type()
)
apsConfigSdBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigSdBerThreshold.setStatus("current")


class _ApsConfigSfBerThreshold_Type(Integer32):
    """Custom type apsConfigSfBerThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_ApsConfigSfBerThreshold_Type.__name__ = "Integer32"
_ApsConfigSfBerThreshold_Object = MibTableColumn
apsConfigSfBerThreshold = _ApsConfigSfBerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 8),
    _ApsConfigSfBerThreshold_Type()
)
apsConfigSfBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigSfBerThreshold.setStatus("current")


class _ApsConfigWaitToRestore_Type(Integer32):
    """Custom type apsConfigWaitToRestore based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_ApsConfigWaitToRestore_Type.__name__ = "Integer32"
_ApsConfigWaitToRestore_Object = MibTableColumn
apsConfigWaitToRestore = _ApsConfigWaitToRestore_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 9),
    _ApsConfigWaitToRestore_Type()
)
apsConfigWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    apsConfigWaitToRestore.setUnits("seconds")
_ApsConfigCreationTime_Type = TimeStamp
_ApsConfigCreationTime_Object = MibTableColumn
apsConfigCreationTime = _ApsConfigCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 10),
    _ApsConfigCreationTime_Type()
)
apsConfigCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsConfigCreationTime.setStatus("current")


class _ApsConfigStorageType_Type(StorageType):
    """Custom type apsConfigStorageType based on StorageType"""


_ApsConfigStorageType_Object = MibTableColumn
apsConfigStorageType = _ApsConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 1, 2, 1, 11),
    _ApsConfigStorageType_Type()
)
apsConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsConfigStorageType.setStatus("current")
_ApsStatusTable_Object = MibTable
apsStatusTable = _ApsStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2)
)
if mibBuilder.loadTexts:
    apsStatusTable.setStatus("current")
_ApsStatusEntry_Object = MibTableRow
apsStatusEntry = _ApsStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apsStatusEntry.setStatus("current")
_ApsStatusK1K2Rcv_Type = ApsK1K2
_ApsStatusK1K2Rcv_Object = MibTableColumn
apsStatusK1K2Rcv = _ApsStatusK1K2Rcv_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 1),
    _ApsStatusK1K2Rcv_Type()
)
apsStatusK1K2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusK1K2Rcv.setStatus("current")
_ApsStatusK1K2Trans_Type = ApsK1K2
_ApsStatusK1K2Trans_Object = MibTableColumn
apsStatusK1K2Trans = _ApsStatusK1K2Trans_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 2),
    _ApsStatusK1K2Trans_Type()
)
apsStatusK1K2Trans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusK1K2Trans.setStatus("current")


class _ApsStatusCurrent_Type(Bits):
    """Custom type apsStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("channelMismatch", 1),
          ("extraTraffic", 4),
          ("feplf", 3),
          ("modeMismatch", 0),
          ("psbf", 2))
    )

_ApsStatusCurrent_Type.__name__ = "Bits"
_ApsStatusCurrent_Object = MibTableColumn
apsStatusCurrent = _ApsStatusCurrent_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 3),
    _ApsStatusCurrent_Type()
)
apsStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusCurrent.setStatus("current")
_ApsStatusModeMismatches_Type = Counter32
_ApsStatusModeMismatches_Object = MibTableColumn
apsStatusModeMismatches = _ApsStatusModeMismatches_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 4),
    _ApsStatusModeMismatches_Type()
)
apsStatusModeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusModeMismatches.setStatus("current")
_ApsStatusChannelMismatches_Type = Counter32
_ApsStatusChannelMismatches_Object = MibTableColumn
apsStatusChannelMismatches = _ApsStatusChannelMismatches_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 5),
    _ApsStatusChannelMismatches_Type()
)
apsStatusChannelMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusChannelMismatches.setStatus("current")
_ApsStatusPSBFs_Type = Counter32
_ApsStatusPSBFs_Object = MibTableColumn
apsStatusPSBFs = _ApsStatusPSBFs_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 6),
    _ApsStatusPSBFs_Type()
)
apsStatusPSBFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusPSBFs.setStatus("current")
_ApsStatusFEPLFs_Type = Counter32
_ApsStatusFEPLFs_Object = MibTableColumn
apsStatusFEPLFs = _ApsStatusFEPLFs_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 7),
    _ApsStatusFEPLFs_Type()
)
apsStatusFEPLFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusFEPLFs.setStatus("current")
_ApsStatusSwitchedChannel_Type = Integer32
_ApsStatusSwitchedChannel_Object = MibTableColumn
apsStatusSwitchedChannel = _ApsStatusSwitchedChannel_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 8),
    _ApsStatusSwitchedChannel_Type()
)
apsStatusSwitchedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusSwitchedChannel.setStatus("current")
_ApsStatusDiscontinuityTime_Type = TimeStamp
_ApsStatusDiscontinuityTime_Object = MibTableColumn
apsStatusDiscontinuityTime = _ApsStatusDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 2, 1, 9),
    _ApsStatusDiscontinuityTime_Type()
)
apsStatusDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStatusDiscontinuityTime.setStatus("current")
_ApsMap_ObjectIdentity = ObjectIdentity
apsMap = _ApsMap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 3)
)
_ApsChanLTEs_Type = Gauge32
_ApsChanLTEs_Object = MibScalar
apsChanLTEs = _ApsChanLTEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 1),
    _ApsChanLTEs_Type()
)
apsChanLTEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanLTEs.setStatus("current")
_ApsMapTable_Object = MibTable
apsMapTable = _ApsMapTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2)
)
if mibBuilder.loadTexts:
    apsMapTable.setStatus("current")
_ApsMapEntry_Object = MibTableRow
apsMapEntry = _ApsMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2, 1)
)
apsMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apsMapEntry.setStatus("current")


class _ApsMapGroupName_Type(SnmpAdminString):
    """Custom type apsMapGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApsMapGroupName_Type.__name__ = "SnmpAdminString"
_ApsMapGroupName_Object = MibTableColumn
apsMapGroupName = _ApsMapGroupName_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2, 1, 2),
    _ApsMapGroupName_Type()
)
apsMapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsMapGroupName.setStatus("current")


class _ApsMapChanNumber_Type(Integer32):
    """Custom type apsMapChanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 14),
    )


_ApsMapChanNumber_Type.__name__ = "Integer32"
_ApsMapChanNumber_Object = MibTableColumn
apsMapChanNumber = _ApsMapChanNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 3, 2, 1, 3),
    _ApsMapChanNumber_Type()
)
apsMapChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsMapChanNumber.setStatus("current")
_ApsChanConfigTable_Object = MibTable
apsChanConfigTable = _ApsChanConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4)
)
if mibBuilder.loadTexts:
    apsChanConfigTable.setStatus("current")
_ApsChanConfigEntry_Object = MibTableRow
apsChanConfigEntry = _ApsChanConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1)
)
apsChanConfigEntry.setIndexNames(
    (0, "APS-MIB", "apsChanConfigGroupName"),
    (0, "APS-MIB", "apsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    apsChanConfigEntry.setStatus("current")


class _ApsChanConfigGroupName_Type(SnmpAdminString):
    """Custom type apsChanConfigGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ApsChanConfigGroupName_Type.__name__ = "SnmpAdminString"
_ApsChanConfigGroupName_Object = MibTableColumn
apsChanConfigGroupName = _ApsChanConfigGroupName_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 1),
    _ApsChanConfigGroupName_Type()
)
apsChanConfigGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsChanConfigGroupName.setStatus("current")


class _ApsChanConfigNumber_Type(Integer32):
    """Custom type apsChanConfigNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ApsChanConfigNumber_Type.__name__ = "Integer32"
_ApsChanConfigNumber_Object = MibTableColumn
apsChanConfigNumber = _ApsChanConfigNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 2),
    _ApsChanConfigNumber_Type()
)
apsChanConfigNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsChanConfigNumber.setStatus("current")
_ApsChanConfigRowStatus_Type = RowStatus
_ApsChanConfigRowStatus_Object = MibTableColumn
apsChanConfigRowStatus = _ApsChanConfigRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 3),
    _ApsChanConfigRowStatus_Type()
)
apsChanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsChanConfigRowStatus.setStatus("current")
_ApsChanConfigIfIndex_Type = InterfaceIndex
_ApsChanConfigIfIndex_Object = MibTableColumn
apsChanConfigIfIndex = _ApsChanConfigIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 4),
    _ApsChanConfigIfIndex_Type()
)
apsChanConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsChanConfigIfIndex.setStatus("current")


class _ApsChanConfigPriority_Type(Integer32):
    """Custom type apsChanConfigPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_ApsChanConfigPriority_Type.__name__ = "Integer32"
_ApsChanConfigPriority_Object = MibTableColumn
apsChanConfigPriority = _ApsChanConfigPriority_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 5),
    _ApsChanConfigPriority_Type()
)
apsChanConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsChanConfigPriority.setStatus("current")


class _ApsChanConfigStorageType_Type(StorageType):
    """Custom type apsChanConfigStorageType based on StorageType"""


_ApsChanConfigStorageType_Object = MibTableColumn
apsChanConfigStorageType = _ApsChanConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 4, 1, 6),
    _ApsChanConfigStorageType_Type()
)
apsChanConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apsChanConfigStorageType.setStatus("current")
_ApsCommandTable_Object = MibTable
apsCommandTable = _ApsCommandTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 5)
)
if mibBuilder.loadTexts:
    apsCommandTable.setStatus("current")
_ApsCommandEntry_Object = MibTableRow
apsCommandEntry = _ApsCommandEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 5, 1)
)
apsCommandEntry.setIndexNames(
    (0, "APS-MIB", "apsChanConfigGroupName"),
    (0, "APS-MIB", "apsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    apsCommandEntry.setStatus("current")
_ApsCommandSwitch_Type = ApsSwitchCommand
_ApsCommandSwitch_Object = MibTableColumn
apsCommandSwitch = _ApsCommandSwitch_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 5, 1, 1),
    _ApsCommandSwitch_Type()
)
apsCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCommandSwitch.setStatus("current")
_ApsCommandControl_Type = ApsControlCommand
_ApsCommandControl_Object = MibTableColumn
apsCommandControl = _ApsCommandControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 5, 1, 2),
    _ApsCommandControl_Type()
)
apsCommandControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCommandControl.setStatus("current")
_ApsChanStatusTable_Object = MibTable
apsChanStatusTable = _ApsChanStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6)
)
if mibBuilder.loadTexts:
    apsChanStatusTable.setStatus("current")
_ApsChanStatusEntry_Object = MibTableRow
apsChanStatusEntry = _ApsChanStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1)
)
if mibBuilder.loadTexts:
    apsChanStatusEntry.setStatus("current")


class _ApsChanStatusCurrent_Type(Bits):
    """Custom type apsChanStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3),
          ("wtr", 4))
    )

_ApsChanStatusCurrent_Type.__name__ = "Bits"
_ApsChanStatusCurrent_Object = MibTableColumn
apsChanStatusCurrent = _ApsChanStatusCurrent_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 1),
    _ApsChanStatusCurrent_Type()
)
apsChanStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusCurrent.setStatus("current")
_ApsChanStatusSignalDegrades_Type = Counter32
_ApsChanStatusSignalDegrades_Object = MibTableColumn
apsChanStatusSignalDegrades = _ApsChanStatusSignalDegrades_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 2),
    _ApsChanStatusSignalDegrades_Type()
)
apsChanStatusSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusSignalDegrades.setStatus("current")
_ApsChanStatusSignalFailures_Type = Counter32
_ApsChanStatusSignalFailures_Object = MibTableColumn
apsChanStatusSignalFailures = _ApsChanStatusSignalFailures_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 3),
    _ApsChanStatusSignalFailures_Type()
)
apsChanStatusSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusSignalFailures.setStatus("current")
_ApsChanStatusSwitchovers_Type = Counter32
_ApsChanStatusSwitchovers_Object = MibTableColumn
apsChanStatusSwitchovers = _ApsChanStatusSwitchovers_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 4),
    _ApsChanStatusSwitchovers_Type()
)
apsChanStatusSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusSwitchovers.setStatus("current")
_ApsChanStatusLastSwitchover_Type = TimeStamp
_ApsChanStatusLastSwitchover_Object = MibTableColumn
apsChanStatusLastSwitchover = _ApsChanStatusLastSwitchover_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 5),
    _ApsChanStatusLastSwitchover_Type()
)
apsChanStatusLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusLastSwitchover.setStatus("current")
_ApsChanStatusSwitchoverSeconds_Type = Counter32
_ApsChanStatusSwitchoverSeconds_Object = MibTableColumn
apsChanStatusSwitchoverSeconds = _ApsChanStatusSwitchoverSeconds_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 6),
    _ApsChanStatusSwitchoverSeconds_Type()
)
apsChanStatusSwitchoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusSwitchoverSeconds.setStatus("current")
_ApsChanStatusDiscontinuityTime_Type = TimeStamp
_ApsChanStatusDiscontinuityTime_Object = MibTableColumn
apsChanStatusDiscontinuityTime = _ApsChanStatusDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 6, 1, 7),
    _ApsChanStatusDiscontinuityTime_Type()
)
apsChanStatusDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsChanStatusDiscontinuityTime.setStatus("current")


class _ApsNotificationEnable_Type(Bits):
    """Custom type apsNotificationEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("channelMismatch", 2),
          ("feplf", 4),
          ("modeMismatch", 1),
          ("psbf", 3),
          ("switchover", 0))
    )

_ApsNotificationEnable_Type.__name__ = "Bits"
_ApsNotificationEnable_Object = MibScalar
apsNotificationEnable = _ApsNotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 49, 1, 7),
    _ApsNotificationEnable_Type()
)
apsNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsNotificationEnable.setStatus("current")
_ApsMIBNotifications_ObjectIdentity = ObjectIdentity
apsMIBNotifications = _ApsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 2)
)
_ApsNotificationsPrefix_ObjectIdentity = ObjectIdentity
apsNotificationsPrefix = _ApsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 2, 0)
)
_ApsMIBConformance_ObjectIdentity = ObjectIdentity
apsMIBConformance = _ApsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 3)
)
_ApsGroups_ObjectIdentity = ObjectIdentity
apsGroups = _ApsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1)
)
_ApsCompliances_ObjectIdentity = ObjectIdentity
apsCompliances = _ApsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 2)
)
apsConfigEntry.registerAugmentions(
    ("APS-MIB",
     "apsStatusEntry")
)
apsStatusEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsChanConfigEntry.registerAugmentions(
    ("APS-MIB",
     "apsChanStatusEntry")
)
apsChanStatusEntry.setIndexNames(*apsChanConfigEntry.getIndexNames())

# Managed Objects groups

apsConfigGeneral = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 1)
)
apsConfigGeneral.setObjects(
      *(("APS-MIB", "apsConfigMode"),
        ("APS-MIB", "apsConfigRevert"),
        ("APS-MIB", "apsConfigDirection"),
        ("APS-MIB", "apsConfigExtraTraffic"),
        ("APS-MIB", "apsConfigSdBerThreshold"),
        ("APS-MIB", "apsConfigSfBerThreshold"),
        ("APS-MIB", "apsConfigCreationTime"),
        ("APS-MIB", "apsConfigRowStatus"),
        ("APS-MIB", "apsConfigStorageType"),
        ("APS-MIB", "apsNotificationEnable"))
)
if mibBuilder.loadTexts:
    apsConfigGeneral.setStatus("current")

apsConfigWtr = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 2)
)
apsConfigWtr.setObjects(
    ("APS-MIB", "apsConfigWaitToRestore")
)
if mibBuilder.loadTexts:
    apsConfigWtr.setStatus("current")

apsCommandOnePlusOne = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 3)
)
apsCommandOnePlusOne.setObjects(
    ("APS-MIB", "apsCommandSwitch")
)
if mibBuilder.loadTexts:
    apsCommandOnePlusOne.setStatus("current")

apsCommandOneToN = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 4)
)
apsCommandOneToN.setObjects(
      *(("APS-MIB", "apsCommandSwitch"),
        ("APS-MIB", "apsCommandControl"))
)
if mibBuilder.loadTexts:
    apsCommandOneToN.setStatus("current")

apsStatusGeneral = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 5)
)
apsStatusGeneral.setObjects(
      *(("APS-MIB", "apsStatusK1K2Rcv"),
        ("APS-MIB", "apsStatusK1K2Trans"),
        ("APS-MIB", "apsStatusCurrent"),
        ("APS-MIB", "apsStatusModeMismatches"),
        ("APS-MIB", "apsStatusChannelMismatches"),
        ("APS-MIB", "apsStatusPSBFs"),
        ("APS-MIB", "apsStatusFEPLFs"),
        ("APS-MIB", "apsStatusSwitchedChannel"),
        ("APS-MIB", "apsStatusDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    apsStatusGeneral.setStatus("current")

apsChanGeneral = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 6)
)
apsChanGeneral.setObjects(
      *(("APS-MIB", "apsChanConfigIfIndex"),
        ("APS-MIB", "apsChanConfigRowStatus"),
        ("APS-MIB", "apsChanConfigStorageType"),
        ("APS-MIB", "apsChanStatusCurrent"),
        ("APS-MIB", "apsChanStatusSignalDegrades"),
        ("APS-MIB", "apsChanStatusSignalFailures"),
        ("APS-MIB", "apsChanStatusSwitchovers"),
        ("APS-MIB", "apsChanStatusLastSwitchover"),
        ("APS-MIB", "apsChanStatusSwitchoverSeconds"),
        ("APS-MIB", "apsChanStatusDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    apsChanGeneral.setStatus("current")

apsChanOneToN = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 7)
)
apsChanOneToN.setObjects(
    ("APS-MIB", "apsChanConfigPriority")
)
if mibBuilder.loadTexts:
    apsChanOneToN.setStatus("current")

apsTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 8)
)
apsTotalsGroup.setObjects(
      *(("APS-MIB", "apsConfigGroups"),
        ("APS-MIB", "apsChanLTEs"))
)
if mibBuilder.loadTexts:
    apsTotalsGroup.setStatus("current")

apsMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 9)
)
apsMapGroup.setObjects(
      *(("APS-MIB", "apsMapGroupName"),
        ("APS-MIB", "apsMapChanNumber"))
)
if mibBuilder.loadTexts:
    apsMapGroup.setStatus("current")


# Notification objects

apsEventSwitchover = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 1)
)
apsEventSwitchover.setObjects(
      *(("APS-MIB", "apsChanStatusSwitchovers"),
        ("APS-MIB", "apsChanStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsEventSwitchover.setStatus(
        "current"
    )

apsEventModeMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 2)
)
apsEventModeMismatch.setObjects(
      *(("APS-MIB", "apsStatusModeMismatches"),
        ("APS-MIB", "apsStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsEventModeMismatch.setStatus(
        "current"
    )

apsEventChannelMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 3)
)
apsEventChannelMismatch.setObjects(
      *(("APS-MIB", "apsStatusChannelMismatches"),
        ("APS-MIB", "apsStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsEventChannelMismatch.setStatus(
        "current"
    )

apsEventPSBF = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 4)
)
apsEventPSBF.setObjects(
      *(("APS-MIB", "apsStatusPSBFs"),
        ("APS-MIB", "apsStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsEventPSBF.setStatus(
        "current"
    )

apsEventFEPLF = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 49, 2, 0, 5)
)
apsEventFEPLF.setObjects(
      *(("APS-MIB", "apsStatusFEPLFs"),
        ("APS-MIB", "apsStatusCurrent"))
)
if mibBuilder.loadTexts:
    apsEventFEPLF.setStatus(
        "current"
    )


# Notifications groups

apsEventGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 1, 10)
)
apsEventGroup.setObjects(
      *(("APS-MIB", "apsEventSwitchover"),
        ("APS-MIB", "apsEventModeMismatch"),
        ("APS-MIB", "apsEventChannelMismatch"),
        ("APS-MIB", "apsEventPSBF"),
        ("APS-MIB", "apsEventFEPLF"))
)
if mibBuilder.loadTexts:
    apsEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

apsFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 2, 1)
)
if mibBuilder.loadTexts:
    apsFullCompliance.setStatus(
        "current"
    )

apsReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 49, 3, 2, 2)
)
if mibBuilder.loadTexts:
    apsReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APS-MIB",
    **{"ApsK1K2": ApsK1K2,
       "ApsSwitchCommand": ApsSwitchCommand,
       "ApsControlCommand": ApsControlCommand,
       "apsMIB": apsMIB,
       "apsMIBObjects": apsMIBObjects,
       "apsConfig": apsConfig,
       "apsConfigGroups": apsConfigGroups,
       "apsConfigTable": apsConfigTable,
       "apsConfigEntry": apsConfigEntry,
       "apsConfigName": apsConfigName,
       "apsConfigRowStatus": apsConfigRowStatus,
       "apsConfigMode": apsConfigMode,
       "apsConfigRevert": apsConfigRevert,
       "apsConfigDirection": apsConfigDirection,
       "apsConfigExtraTraffic": apsConfigExtraTraffic,
       "apsConfigSdBerThreshold": apsConfigSdBerThreshold,
       "apsConfigSfBerThreshold": apsConfigSfBerThreshold,
       "apsConfigWaitToRestore": apsConfigWaitToRestore,
       "apsConfigCreationTime": apsConfigCreationTime,
       "apsConfigStorageType": apsConfigStorageType,
       "apsStatusTable": apsStatusTable,
       "apsStatusEntry": apsStatusEntry,
       "apsStatusK1K2Rcv": apsStatusK1K2Rcv,
       "apsStatusK1K2Trans": apsStatusK1K2Trans,
       "apsStatusCurrent": apsStatusCurrent,
       "apsStatusModeMismatches": apsStatusModeMismatches,
       "apsStatusChannelMismatches": apsStatusChannelMismatches,
       "apsStatusPSBFs": apsStatusPSBFs,
       "apsStatusFEPLFs": apsStatusFEPLFs,
       "apsStatusSwitchedChannel": apsStatusSwitchedChannel,
       "apsStatusDiscontinuityTime": apsStatusDiscontinuityTime,
       "apsMap": apsMap,
       "apsChanLTEs": apsChanLTEs,
       "apsMapTable": apsMapTable,
       "apsMapEntry": apsMapEntry,
       "apsMapGroupName": apsMapGroupName,
       "apsMapChanNumber": apsMapChanNumber,
       "apsChanConfigTable": apsChanConfigTable,
       "apsChanConfigEntry": apsChanConfigEntry,
       "apsChanConfigGroupName": apsChanConfigGroupName,
       "apsChanConfigNumber": apsChanConfigNumber,
       "apsChanConfigRowStatus": apsChanConfigRowStatus,
       "apsChanConfigIfIndex": apsChanConfigIfIndex,
       "apsChanConfigPriority": apsChanConfigPriority,
       "apsChanConfigStorageType": apsChanConfigStorageType,
       "apsCommandTable": apsCommandTable,
       "apsCommandEntry": apsCommandEntry,
       "apsCommandSwitch": apsCommandSwitch,
       "apsCommandControl": apsCommandControl,
       "apsChanStatusTable": apsChanStatusTable,
       "apsChanStatusEntry": apsChanStatusEntry,
       "apsChanStatusCurrent": apsChanStatusCurrent,
       "apsChanStatusSignalDegrades": apsChanStatusSignalDegrades,
       "apsChanStatusSignalFailures": apsChanStatusSignalFailures,
       "apsChanStatusSwitchovers": apsChanStatusSwitchovers,
       "apsChanStatusLastSwitchover": apsChanStatusLastSwitchover,
       "apsChanStatusSwitchoverSeconds": apsChanStatusSwitchoverSeconds,
       "apsChanStatusDiscontinuityTime": apsChanStatusDiscontinuityTime,
       "apsNotificationEnable": apsNotificationEnable,
       "apsMIBNotifications": apsMIBNotifications,
       "apsNotificationsPrefix": apsNotificationsPrefix,
       "apsEventSwitchover": apsEventSwitchover,
       "apsEventModeMismatch": apsEventModeMismatch,
       "apsEventChannelMismatch": apsEventChannelMismatch,
       "apsEventPSBF": apsEventPSBF,
       "apsEventFEPLF": apsEventFEPLF,
       "apsMIBConformance": apsMIBConformance,
       "apsGroups": apsGroups,
       "apsConfigGeneral": apsConfigGeneral,
       "apsConfigWtr": apsConfigWtr,
       "apsCommandOnePlusOne": apsCommandOnePlusOne,
       "apsCommandOneToN": apsCommandOneToN,
       "apsStatusGeneral": apsStatusGeneral,
       "apsChanGeneral": apsChanGeneral,
       "apsChanOneToN": apsChanOneToN,
       "apsTotalsGroup": apsTotalsGroup,
       "apsMapGroup": apsMapGroup,
       "apsEventGroup": apsEventGroup,
       "apsCompliances": apsCompliances,
       "apsFullCompliance": apsFullCompliance,
       "apsReadOnlyCompliance": apsReadOnlyCompliance}
)
