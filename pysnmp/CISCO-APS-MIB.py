# SNMP MIB module (CISCO-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:41 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cApsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71)
)
cApsMIB.setRevisions(
        ("2001-12-26 12:00",
         "2001-04-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CApsK1K2(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class CApsSwitchCommand(Integer32, TextualConvention):
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



class CApsControlCommand(Integer32, TextualConvention):
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

_CApsMIBObjects_ObjectIdentity = ObjectIdentity
cApsMIBObjects = _CApsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1)
)
_CApsConfig_ObjectIdentity = ObjectIdentity
cApsConfig = _CApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1)
)
_CApsConfigGroups_Type = Gauge32
_CApsConfigGroups_Object = MibScalar
cApsConfigGroups = _CApsConfigGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 1),
    _CApsConfigGroups_Type()
)
cApsConfigGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsConfigGroups.setStatus("current")
_CApsConfigTable_Object = MibTable
cApsConfigTable = _CApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cApsConfigTable.setStatus("current")
_CApsConfigEntry_Object = MibTableRow
cApsConfigEntry = _CApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1)
)
cApsConfigEntry.setIndexNames(
    (1, "CISCO-APS-MIB", "cApsConfigName"),
)
if mibBuilder.loadTexts:
    cApsConfigEntry.setStatus("current")


class _CApsConfigName_Type(SnmpAdminString):
    """Custom type cApsConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CApsConfigName_Type.__name__ = "SnmpAdminString"
_CApsConfigName_Object = MibTableColumn
cApsConfigName = _CApsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 1),
    _CApsConfigName_Type()
)
cApsConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cApsConfigName.setStatus("current")
_CApsConfigRowStatus_Type = RowStatus
_CApsConfigRowStatus_Object = MibTableColumn
cApsConfigRowStatus = _CApsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 2),
    _CApsConfigRowStatus_Type()
)
cApsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigRowStatus.setStatus("current")


class _CApsConfigMode_Type(Integer32):
    """Custom type cApsConfigMode based on Integer32"""
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


_CApsConfigMode_Type.__name__ = "Integer32"
_CApsConfigMode_Object = MibTableColumn
cApsConfigMode = _CApsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 3),
    _CApsConfigMode_Type()
)
cApsConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigMode.setStatus("current")


class _CApsConfigRevert_Type(Integer32):
    """Custom type cApsConfigRevert based on Integer32"""
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


_CApsConfigRevert_Type.__name__ = "Integer32"
_CApsConfigRevert_Object = MibTableColumn
cApsConfigRevert = _CApsConfigRevert_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 4),
    _CApsConfigRevert_Type()
)
cApsConfigRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigRevert.setStatus("current")


class _CApsConfigDirection_Type(Integer32):
    """Custom type cApsConfigDirection based on Integer32"""
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


_CApsConfigDirection_Type.__name__ = "Integer32"
_CApsConfigDirection_Object = MibTableColumn
cApsConfigDirection = _CApsConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 5),
    _CApsConfigDirection_Type()
)
cApsConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigDirection.setStatus("current")


class _CApsConfigExtraTraffic_Type(Integer32):
    """Custom type cApsConfigExtraTraffic based on Integer32"""
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


_CApsConfigExtraTraffic_Type.__name__ = "Integer32"
_CApsConfigExtraTraffic_Object = MibTableColumn
cApsConfigExtraTraffic = _CApsConfigExtraTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 6),
    _CApsConfigExtraTraffic_Type()
)
cApsConfigExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigExtraTraffic.setStatus("current")


class _CApsConfigSdBerThreshold_Type(Integer32):
    """Custom type cApsConfigSdBerThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_CApsConfigSdBerThreshold_Type.__name__ = "Integer32"
_CApsConfigSdBerThreshold_Object = MibTableColumn
cApsConfigSdBerThreshold = _CApsConfigSdBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 7),
    _CApsConfigSdBerThreshold_Type()
)
cApsConfigSdBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigSdBerThreshold.setStatus("current")


class _CApsConfigSfBerThreshold_Type(Integer32):
    """Custom type cApsConfigSfBerThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_CApsConfigSfBerThreshold_Type.__name__ = "Integer32"
_CApsConfigSfBerThreshold_Object = MibTableColumn
cApsConfigSfBerThreshold = _CApsConfigSfBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 8),
    _CApsConfigSfBerThreshold_Type()
)
cApsConfigSfBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigSfBerThreshold.setStatus("current")


class _CApsConfigWaitToRestore_Type(Integer32):
    """Custom type cApsConfigWaitToRestore based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_CApsConfigWaitToRestore_Type.__name__ = "Integer32"
_CApsConfigWaitToRestore_Object = MibTableColumn
cApsConfigWaitToRestore = _CApsConfigWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 9),
    _CApsConfigWaitToRestore_Type()
)
cApsConfigWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsConfigWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    cApsConfigWaitToRestore.setUnits("seconds")
_CApsConfigCreationTime_Type = TimeStamp
_CApsConfigCreationTime_Object = MibTableColumn
cApsConfigCreationTime = _CApsConfigCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 1, 2, 1, 10),
    _CApsConfigCreationTime_Type()
)
cApsConfigCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsConfigCreationTime.setStatus("current")
_CApsStatusTable_Object = MibTable
cApsStatusTable = _CApsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2)
)
if mibBuilder.loadTexts:
    cApsStatusTable.setStatus("current")
_CApsStatusEntry_Object = MibTableRow
cApsStatusEntry = _CApsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1)
)
cApsStatusEntry.setIndexNames(
    (1, "CISCO-APS-MIB", "cApsConfigName"),
)
if mibBuilder.loadTexts:
    cApsStatusEntry.setStatus("current")
_CApsStatusK1K2Rcv_Type = CApsK1K2
_CApsStatusK1K2Rcv_Object = MibTableColumn
cApsStatusK1K2Rcv = _CApsStatusK1K2Rcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 1),
    _CApsStatusK1K2Rcv_Type()
)
cApsStatusK1K2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusK1K2Rcv.setStatus("current")
_CApsStatusK1K2Trans_Type = CApsK1K2
_CApsStatusK1K2Trans_Object = MibTableColumn
cApsStatusK1K2Trans = _CApsStatusK1K2Trans_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 2),
    _CApsStatusK1K2Trans_Type()
)
cApsStatusK1K2Trans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusK1K2Trans.setStatus("current")


class _CApsStatusCurrent_Type(Bits):
    """Custom type cApsStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("channelMismatch", 1),
          ("extraTraffic", 4),
          ("feplf", 3),
          ("modeMismatch", 0),
          ("psbf", 2))
    )

_CApsStatusCurrent_Type.__name__ = "Bits"
_CApsStatusCurrent_Object = MibTableColumn
cApsStatusCurrent = _CApsStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 3),
    _CApsStatusCurrent_Type()
)
cApsStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusCurrent.setStatus("current")
_CApsStatusModeMismatches_Type = Counter32
_CApsStatusModeMismatches_Object = MibTableColumn
cApsStatusModeMismatches = _CApsStatusModeMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 4),
    _CApsStatusModeMismatches_Type()
)
cApsStatusModeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusModeMismatches.setStatus("current")
_CApsStatusChannelMismatches_Type = Counter32
_CApsStatusChannelMismatches_Object = MibTableColumn
cApsStatusChannelMismatches = _CApsStatusChannelMismatches_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 5),
    _CApsStatusChannelMismatches_Type()
)
cApsStatusChannelMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusChannelMismatches.setStatus("current")
_CApsStatusPSBFs_Type = Counter32
_CApsStatusPSBFs_Object = MibTableColumn
cApsStatusPSBFs = _CApsStatusPSBFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 6),
    _CApsStatusPSBFs_Type()
)
cApsStatusPSBFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusPSBFs.setStatus("current")
_CApsStatusFEPLFs_Type = Counter32
_CApsStatusFEPLFs_Object = MibTableColumn
cApsStatusFEPLFs = _CApsStatusFEPLFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 7),
    _CApsStatusFEPLFs_Type()
)
cApsStatusFEPLFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusFEPLFs.setStatus("current")
_CApsStatusSwitchedChannel_Type = Integer32
_CApsStatusSwitchedChannel_Object = MibTableColumn
cApsStatusSwitchedChannel = _CApsStatusSwitchedChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 2, 1, 8),
    _CApsStatusSwitchedChannel_Type()
)
cApsStatusSwitchedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsStatusSwitchedChannel.setStatus("current")
_CApsMap_ObjectIdentity = ObjectIdentity
cApsMap = _CApsMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3)
)
_CApsChanLTEs_Type = Gauge32
_CApsChanLTEs_Object = MibScalar
cApsChanLTEs = _CApsChanLTEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 1),
    _CApsChanLTEs_Type()
)
cApsChanLTEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanLTEs.setStatus("current")
_CApsMapTable_Object = MibTable
cApsMapTable = _CApsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cApsMapTable.setStatus("current")
_CApsMapEntry_Object = MibTableRow
cApsMapEntry = _CApsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1)
)
cApsMapEntry.setIndexNames(
    (0, "CISCO-APS-MIB", "cApsMapIfIndex"),
)
if mibBuilder.loadTexts:
    cApsMapEntry.setStatus("current")
_CApsMapIfIndex_Type = InterfaceIndex
_CApsMapIfIndex_Object = MibTableColumn
cApsMapIfIndex = _CApsMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1, 1),
    _CApsMapIfIndex_Type()
)
cApsMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cApsMapIfIndex.setStatus("current")


class _CApsMapGroupName_Type(SnmpAdminString):
    """Custom type cApsMapGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CApsMapGroupName_Type.__name__ = "SnmpAdminString"
_CApsMapGroupName_Object = MibTableColumn
cApsMapGroupName = _CApsMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1, 2),
    _CApsMapGroupName_Type()
)
cApsMapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsMapGroupName.setStatus("current")


class _CApsMapChanNumber_Type(Integer32):
    """Custom type cApsMapChanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 14),
    )


_CApsMapChanNumber_Type.__name__ = "Integer32"
_CApsMapChanNumber_Object = MibTableColumn
cApsMapChanNumber = _CApsMapChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 3, 2, 1, 3),
    _CApsMapChanNumber_Type()
)
cApsMapChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsMapChanNumber.setStatus("current")
_CApsChanConfigTable_Object = MibTable
cApsChanConfigTable = _CApsChanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4)
)
if mibBuilder.loadTexts:
    cApsChanConfigTable.setStatus("current")
_CApsChanConfigEntry_Object = MibTableRow
cApsChanConfigEntry = _CApsChanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1)
)
cApsChanConfigEntry.setIndexNames(
    (0, "CISCO-APS-MIB", "cApsChanConfigGroupName"),
    (0, "CISCO-APS-MIB", "cApsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    cApsChanConfigEntry.setStatus("current")


class _CApsChanConfigGroupName_Type(SnmpAdminString):
    """Custom type cApsChanConfigGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CApsChanConfigGroupName_Type.__name__ = "SnmpAdminString"
_CApsChanConfigGroupName_Object = MibTableColumn
cApsChanConfigGroupName = _CApsChanConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 1),
    _CApsChanConfigGroupName_Type()
)
cApsChanConfigGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cApsChanConfigGroupName.setStatus("current")


class _CApsChanConfigNumber_Type(Integer32):
    """Custom type cApsChanConfigNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CApsChanConfigNumber_Type.__name__ = "Integer32"
_CApsChanConfigNumber_Object = MibTableColumn
cApsChanConfigNumber = _CApsChanConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 2),
    _CApsChanConfigNumber_Type()
)
cApsChanConfigNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cApsChanConfigNumber.setStatus("current")
_CApsChanConfigRowStatus_Type = RowStatus
_CApsChanConfigRowStatus_Object = MibTableColumn
cApsChanConfigRowStatus = _CApsChanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 3),
    _CApsChanConfigRowStatus_Type()
)
cApsChanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsChanConfigRowStatus.setStatus("current")
_CApsChanConfigIfIndex_Type = InterfaceIndex
_CApsChanConfigIfIndex_Object = MibTableColumn
cApsChanConfigIfIndex = _CApsChanConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 4),
    _CApsChanConfigIfIndex_Type()
)
cApsChanConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsChanConfigIfIndex.setStatus("current")


class _CApsChanConfigPriority_Type(Integer32):
    """Custom type cApsChanConfigPriority based on Integer32"""
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


_CApsChanConfigPriority_Type.__name__ = "Integer32"
_CApsChanConfigPriority_Object = MibTableColumn
cApsChanConfigPriority = _CApsChanConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 4, 1, 5),
    _CApsChanConfigPriority_Type()
)
cApsChanConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cApsChanConfigPriority.setStatus("current")
_CApsCommandTable_Object = MibTable
cApsCommandTable = _CApsCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5)
)
if mibBuilder.loadTexts:
    cApsCommandTable.setStatus("current")
_CApsCommandEntry_Object = MibTableRow
cApsCommandEntry = _CApsCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5, 1)
)
cApsCommandEntry.setIndexNames(
    (0, "CISCO-APS-MIB", "cApsChanConfigGroupName"),
    (0, "CISCO-APS-MIB", "cApsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    cApsCommandEntry.setStatus("current")
_CApsCommandSwitch_Type = CApsSwitchCommand
_CApsCommandSwitch_Object = MibTableColumn
cApsCommandSwitch = _CApsCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5, 1, 1),
    _CApsCommandSwitch_Type()
)
cApsCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cApsCommandSwitch.setStatus("current")
_CApsCommandControl_Type = CApsControlCommand
_CApsCommandControl_Object = MibTableColumn
cApsCommandControl = _CApsCommandControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 5, 1, 2),
    _CApsCommandControl_Type()
)
cApsCommandControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cApsCommandControl.setStatus("current")
_CApsChanStatusTable_Object = MibTable
cApsChanStatusTable = _CApsChanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6)
)
if mibBuilder.loadTexts:
    cApsChanStatusTable.setStatus("current")
_CApsChanStatusEntry_Object = MibTableRow
cApsChanStatusEntry = _CApsChanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1)
)
cApsChanStatusEntry.setIndexNames(
    (0, "CISCO-APS-MIB", "cApsChanConfigGroupName"),
    (0, "CISCO-APS-MIB", "cApsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    cApsChanStatusEntry.setStatus("current")


class _CApsChanStatusCurrent_Type(Bits):
    """Custom type cApsChanStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3))
    )

_CApsChanStatusCurrent_Type.__name__ = "Bits"
_CApsChanStatusCurrent_Object = MibTableColumn
cApsChanStatusCurrent = _CApsChanStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 1),
    _CApsChanStatusCurrent_Type()
)
cApsChanStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanStatusCurrent.setStatus("current")
_CApsChanStatusSignalDegrades_Type = Counter32
_CApsChanStatusSignalDegrades_Object = MibTableColumn
cApsChanStatusSignalDegrades = _CApsChanStatusSignalDegrades_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 2),
    _CApsChanStatusSignalDegrades_Type()
)
cApsChanStatusSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanStatusSignalDegrades.setStatus("current")
_CApsChanStatusSignalFailures_Type = Counter32
_CApsChanStatusSignalFailures_Object = MibTableColumn
cApsChanStatusSignalFailures = _CApsChanStatusSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 3),
    _CApsChanStatusSignalFailures_Type()
)
cApsChanStatusSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanStatusSignalFailures.setStatus("current")
_CApsChanStatusSwitchovers_Type = Counter32
_CApsChanStatusSwitchovers_Object = MibTableColumn
cApsChanStatusSwitchovers = _CApsChanStatusSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 4),
    _CApsChanStatusSwitchovers_Type()
)
cApsChanStatusSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanStatusSwitchovers.setStatus("current")
_CApsChanStatusLastSwitchover_Type = TimeStamp
_CApsChanStatusLastSwitchover_Object = MibTableColumn
cApsChanStatusLastSwitchover = _CApsChanStatusLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 5),
    _CApsChanStatusLastSwitchover_Type()
)
cApsChanStatusLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanStatusLastSwitchover.setStatus("current")
_CApsChanStatusSwitchoverSeconds_Type = Counter32
_CApsChanStatusSwitchoverSeconds_Object = MibTableColumn
cApsChanStatusSwitchoverSeconds = _CApsChanStatusSwitchoverSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 1, 6, 1, 6),
    _CApsChanStatusSwitchoverSeconds_Type()
)
cApsChanStatusSwitchoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cApsChanStatusSwitchoverSeconds.setStatus("current")
_CApsMIBNotifications_ObjectIdentity = ObjectIdentity
cApsMIBNotifications = _CApsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 2)
)
_CApsNotificationsPrefix_ObjectIdentity = ObjectIdentity
cApsNotificationsPrefix = _CApsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0)
)
_CApsMIBConformance_ObjectIdentity = ObjectIdentity
cApsMIBConformance = _CApsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3)
)
_CApsGroups_ObjectIdentity = ObjectIdentity
cApsGroups = _CApsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1)
)
_CApsCompliances_ObjectIdentity = ObjectIdentity
cApsCompliances = _CApsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 2)
)

# Managed Objects groups

cApsConfigGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 1)
)
cApsConfigGeneral.setObjects(
      *(("CISCO-APS-MIB", "cApsConfigMode"),
        ("CISCO-APS-MIB", "cApsConfigRevert"),
        ("CISCO-APS-MIB", "cApsConfigDirection"),
        ("CISCO-APS-MIB", "cApsConfigExtraTraffic"),
        ("CISCO-APS-MIB", "cApsConfigSdBerThreshold"),
        ("CISCO-APS-MIB", "cApsConfigSfBerThreshold"),
        ("CISCO-APS-MIB", "cApsConfigCreationTime"),
        ("CISCO-APS-MIB", "cApsConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cApsConfigGeneral.setStatus("current")

cApsConfigWtr = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 2)
)
cApsConfigWtr.setObjects(
    ("CISCO-APS-MIB", "cApsConfigWaitToRestore")
)
if mibBuilder.loadTexts:
    cApsConfigWtr.setStatus("current")

cApsCommandOnePlusOne = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 3)
)
cApsCommandOnePlusOne.setObjects(
    ("CISCO-APS-MIB", "cApsCommandSwitch")
)
if mibBuilder.loadTexts:
    cApsCommandOnePlusOne.setStatus("current")

cApsCommandOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 4)
)
cApsCommandOneToN.setObjects(
      *(("CISCO-APS-MIB", "cApsCommandSwitch"),
        ("CISCO-APS-MIB", "cApsCommandControl"))
)
if mibBuilder.loadTexts:
    cApsCommandOneToN.setStatus("current")

cApsStatusGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 5)
)
cApsStatusGeneral.setObjects(
      *(("CISCO-APS-MIB", "cApsStatusK1K2Rcv"),
        ("CISCO-APS-MIB", "cApsStatusK1K2Trans"),
        ("CISCO-APS-MIB", "cApsStatusCurrent"),
        ("CISCO-APS-MIB", "cApsStatusModeMismatches"),
        ("CISCO-APS-MIB", "cApsStatusChannelMismatches"),
        ("CISCO-APS-MIB", "cApsStatusPSBFs"),
        ("CISCO-APS-MIB", "cApsStatusFEPLFs"),
        ("CISCO-APS-MIB", "cApsStatusSwitchedChannel"))
)
if mibBuilder.loadTexts:
    cApsStatusGeneral.setStatus("current")

cApsChanGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 6)
)
cApsChanGeneral.setObjects(
      *(("CISCO-APS-MIB", "cApsChanConfigIfIndex"),
        ("CISCO-APS-MIB", "cApsChanConfigRowStatus"),
        ("CISCO-APS-MIB", "cApsChanStatusCurrent"),
        ("CISCO-APS-MIB", "cApsChanStatusSignalDegrades"),
        ("CISCO-APS-MIB", "cApsChanStatusSignalFailures"),
        ("CISCO-APS-MIB", "cApsChanStatusSwitchovers"),
        ("CISCO-APS-MIB", "cApsChanStatusLastSwitchover"),
        ("CISCO-APS-MIB", "cApsChanStatusSwitchoverSeconds"))
)
if mibBuilder.loadTexts:
    cApsChanGeneral.setStatus("current")

cApsChanOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 7)
)
cApsChanOneToN.setObjects(
    ("CISCO-APS-MIB", "cApsChanConfigPriority")
)
if mibBuilder.loadTexts:
    cApsChanOneToN.setStatus("current")

cApsTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 8)
)
cApsTotalsGroup.setObjects(
      *(("CISCO-APS-MIB", "cApsConfigGroups"),
        ("CISCO-APS-MIB", "cApsChanLTEs"))
)
if mibBuilder.loadTexts:
    cApsTotalsGroup.setStatus("current")

cApsMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 9)
)
cApsMapGroup.setObjects(
      *(("CISCO-APS-MIB", "cApsMapGroupName"),
        ("CISCO-APS-MIB", "cApsMapChanNumber"))
)
if mibBuilder.loadTexts:
    cApsMapGroup.setStatus("current")


# Notification objects

cApsEventSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 1)
)
cApsEventSwitchover.setObjects(
      *(("CISCO-APS-MIB", "cApsChanStatusSwitchovers"),
        ("CISCO-APS-MIB", "cApsChanStatusCurrent"))
)
if mibBuilder.loadTexts:
    cApsEventSwitchover.setStatus(
        "current"
    )

cApsEventModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 2)
)
cApsEventModeMismatch.setObjects(
      *(("CISCO-APS-MIB", "cApsStatusModeMismatches"),
        ("CISCO-APS-MIB", "cApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    cApsEventModeMismatch.setStatus(
        "current"
    )

cApsEventChannelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 3)
)
cApsEventChannelMismatch.setObjects(
      *(("CISCO-APS-MIB", "cApsStatusChannelMismatches"),
        ("CISCO-APS-MIB", "cApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    cApsEventChannelMismatch.setStatus(
        "current"
    )

cApsEventPSBF = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 4)
)
cApsEventPSBF.setObjects(
      *(("CISCO-APS-MIB", "cApsStatusPSBFs"),
        ("CISCO-APS-MIB", "cApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    cApsEventPSBF.setStatus(
        "current"
    )

cApsEventFEPLF = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 2, 0, 5)
)
cApsEventFEPLF.setObjects(
      *(("CISCO-APS-MIB", "cApsStatusFEPLFs"),
        ("CISCO-APS-MIB", "cApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    cApsEventFEPLF.setStatus(
        "current"
    )


# Notifications groups

cApsEventOptional = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 1, 10)
)
cApsEventOptional.setObjects(
      *(("CISCO-APS-MIB", "cApsEventSwitchover"),
        ("CISCO-APS-MIB", "cApsEventModeMismatch"),
        ("CISCO-APS-MIB", "cApsEventChannelMismatch"),
        ("CISCO-APS-MIB", "cApsEventPSBF"),
        ("CISCO-APS-MIB", "cApsEventFEPLF"))
)
if mibBuilder.loadTexts:
    cApsEventOptional.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cApsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 71, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cApsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-APS-MIB",
    **{"CApsK1K2": CApsK1K2,
       "CApsSwitchCommand": CApsSwitchCommand,
       "CApsControlCommand": CApsControlCommand,
       "cApsMIB": cApsMIB,
       "cApsMIBObjects": cApsMIBObjects,
       "cApsConfig": cApsConfig,
       "cApsConfigGroups": cApsConfigGroups,
       "cApsConfigTable": cApsConfigTable,
       "cApsConfigEntry": cApsConfigEntry,
       "cApsConfigName": cApsConfigName,
       "cApsConfigRowStatus": cApsConfigRowStatus,
       "cApsConfigMode": cApsConfigMode,
       "cApsConfigRevert": cApsConfigRevert,
       "cApsConfigDirection": cApsConfigDirection,
       "cApsConfigExtraTraffic": cApsConfigExtraTraffic,
       "cApsConfigSdBerThreshold": cApsConfigSdBerThreshold,
       "cApsConfigSfBerThreshold": cApsConfigSfBerThreshold,
       "cApsConfigWaitToRestore": cApsConfigWaitToRestore,
       "cApsConfigCreationTime": cApsConfigCreationTime,
       "cApsStatusTable": cApsStatusTable,
       "cApsStatusEntry": cApsStatusEntry,
       "cApsStatusK1K2Rcv": cApsStatusK1K2Rcv,
       "cApsStatusK1K2Trans": cApsStatusK1K2Trans,
       "cApsStatusCurrent": cApsStatusCurrent,
       "cApsStatusModeMismatches": cApsStatusModeMismatches,
       "cApsStatusChannelMismatches": cApsStatusChannelMismatches,
       "cApsStatusPSBFs": cApsStatusPSBFs,
       "cApsStatusFEPLFs": cApsStatusFEPLFs,
       "cApsStatusSwitchedChannel": cApsStatusSwitchedChannel,
       "cApsMap": cApsMap,
       "cApsChanLTEs": cApsChanLTEs,
       "cApsMapTable": cApsMapTable,
       "cApsMapEntry": cApsMapEntry,
       "cApsMapIfIndex": cApsMapIfIndex,
       "cApsMapGroupName": cApsMapGroupName,
       "cApsMapChanNumber": cApsMapChanNumber,
       "cApsChanConfigTable": cApsChanConfigTable,
       "cApsChanConfigEntry": cApsChanConfigEntry,
       "cApsChanConfigGroupName": cApsChanConfigGroupName,
       "cApsChanConfigNumber": cApsChanConfigNumber,
       "cApsChanConfigRowStatus": cApsChanConfigRowStatus,
       "cApsChanConfigIfIndex": cApsChanConfigIfIndex,
       "cApsChanConfigPriority": cApsChanConfigPriority,
       "cApsCommandTable": cApsCommandTable,
       "cApsCommandEntry": cApsCommandEntry,
       "cApsCommandSwitch": cApsCommandSwitch,
       "cApsCommandControl": cApsCommandControl,
       "cApsChanStatusTable": cApsChanStatusTable,
       "cApsChanStatusEntry": cApsChanStatusEntry,
       "cApsChanStatusCurrent": cApsChanStatusCurrent,
       "cApsChanStatusSignalDegrades": cApsChanStatusSignalDegrades,
       "cApsChanStatusSignalFailures": cApsChanStatusSignalFailures,
       "cApsChanStatusSwitchovers": cApsChanStatusSwitchovers,
       "cApsChanStatusLastSwitchover": cApsChanStatusLastSwitchover,
       "cApsChanStatusSwitchoverSeconds": cApsChanStatusSwitchoverSeconds,
       "cApsMIBNotifications": cApsMIBNotifications,
       "cApsNotificationsPrefix": cApsNotificationsPrefix,
       "cApsEventSwitchover": cApsEventSwitchover,
       "cApsEventModeMismatch": cApsEventModeMismatch,
       "cApsEventChannelMismatch": cApsEventChannelMismatch,
       "cApsEventPSBF": cApsEventPSBF,
       "cApsEventFEPLF": cApsEventFEPLF,
       "cApsMIBConformance": cApsMIBConformance,
       "cApsGroups": cApsGroups,
       "cApsConfigGeneral": cApsConfigGeneral,
       "cApsConfigWtr": cApsConfigWtr,
       "cApsCommandOnePlusOne": cApsCommandOnePlusOne,
       "cApsCommandOneToN": cApsCommandOneToN,
       "cApsStatusGeneral": cApsStatusGeneral,
       "cApsChanGeneral": cApsChanGeneral,
       "cApsChanOneToN": cApsChanOneToN,
       "cApsTotalsGroup": cApsTotalsGroup,
       "cApsMapGroup": cApsMapGroup,
       "cApsEventOptional": cApsEventOptional,
       "cApsCompliances": cApsCompliances,
       "cApsCompliance": cApsCompliance}
)
