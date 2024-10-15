# SNMP MIB module (APS-MIB-JUNI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APS-MIB-JUNI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:57 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniSonetApsExperiment,) = mibBuilder.importSymbols(
    "Juniper-Experiment",
    "juniSonetApsExperiment")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

junidApsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1)
)
junidApsMIB.setRevisions(
        ("2001-05-24 23:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JunidApsK1K2(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class JunidApsSwitchCommand(Integer32, TextualConvention):
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



class JunidApsControlCommand(Integer32, TextualConvention):
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

_JunidApsMIBObjects_ObjectIdentity = ObjectIdentity
junidApsMIBObjects = _JunidApsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1)
)
_JunidApsConfig_ObjectIdentity = ObjectIdentity
junidApsConfig = _JunidApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1)
)
_JunidApsConfigGroups_Type = Gauge32
_JunidApsConfigGroups_Object = MibScalar
junidApsConfigGroups = _JunidApsConfigGroups_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 1),
    _JunidApsConfigGroups_Type()
)
junidApsConfigGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsConfigGroups.setStatus("current")
_JunidApsConfigTable_Object = MibTable
junidApsConfigTable = _JunidApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    junidApsConfigTable.setStatus("current")
_JunidApsConfigEntry_Object = MibTableRow
junidApsConfigEntry = _JunidApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1)
)
junidApsConfigEntry.setIndexNames(
    (1, "APS-MIB-JUNI", "junidApsConfigName"),
)
if mibBuilder.loadTexts:
    junidApsConfigEntry.setStatus("current")


class _JunidApsConfigName_Type(SnmpAdminString):
    """Custom type junidApsConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JunidApsConfigName_Type.__name__ = "SnmpAdminString"
_JunidApsConfigName_Object = MibTableColumn
junidApsConfigName = _JunidApsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 1),
    _JunidApsConfigName_Type()
)
junidApsConfigName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidApsConfigName.setStatus("current")
_JunidApsConfigRowStatus_Type = RowStatus
_JunidApsConfigRowStatus_Object = MibTableColumn
junidApsConfigRowStatus = _JunidApsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 2),
    _JunidApsConfigRowStatus_Type()
)
junidApsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigRowStatus.setStatus("current")


class _JunidApsConfigMode_Type(Integer32):
    """Custom type junidApsConfigMode based on Integer32"""
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


_JunidApsConfigMode_Type.__name__ = "Integer32"
_JunidApsConfigMode_Object = MibTableColumn
junidApsConfigMode = _JunidApsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 3),
    _JunidApsConfigMode_Type()
)
junidApsConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigMode.setStatus("current")


class _JunidApsConfigRevert_Type(Integer32):
    """Custom type junidApsConfigRevert based on Integer32"""
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


_JunidApsConfigRevert_Type.__name__ = "Integer32"
_JunidApsConfigRevert_Object = MibTableColumn
junidApsConfigRevert = _JunidApsConfigRevert_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 4),
    _JunidApsConfigRevert_Type()
)
junidApsConfigRevert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigRevert.setStatus("current")


class _JunidApsConfigDirection_Type(Integer32):
    """Custom type junidApsConfigDirection based on Integer32"""
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


_JunidApsConfigDirection_Type.__name__ = "Integer32"
_JunidApsConfigDirection_Object = MibTableColumn
junidApsConfigDirection = _JunidApsConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 5),
    _JunidApsConfigDirection_Type()
)
junidApsConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigDirection.setStatus("current")


class _JunidApsConfigExtraTraffic_Type(Integer32):
    """Custom type junidApsConfigExtraTraffic based on Integer32"""
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


_JunidApsConfigExtraTraffic_Type.__name__ = "Integer32"
_JunidApsConfigExtraTraffic_Object = MibTableColumn
junidApsConfigExtraTraffic = _JunidApsConfigExtraTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 6),
    _JunidApsConfigExtraTraffic_Type()
)
junidApsConfigExtraTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigExtraTraffic.setStatus("current")


class _JunidApsConfigSdBerThreshold_Type(Integer32):
    """Custom type junidApsConfigSdBerThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_JunidApsConfigSdBerThreshold_Type.__name__ = "Integer32"
_JunidApsConfigSdBerThreshold_Object = MibTableColumn
junidApsConfigSdBerThreshold = _JunidApsConfigSdBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 7),
    _JunidApsConfigSdBerThreshold_Type()
)
junidApsConfigSdBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigSdBerThreshold.setStatus("current")


class _JunidApsConfigSfBerThreshold_Type(Integer32):
    """Custom type junidApsConfigSfBerThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_JunidApsConfigSfBerThreshold_Type.__name__ = "Integer32"
_JunidApsConfigSfBerThreshold_Object = MibTableColumn
junidApsConfigSfBerThreshold = _JunidApsConfigSfBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 8),
    _JunidApsConfigSfBerThreshold_Type()
)
junidApsConfigSfBerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigSfBerThreshold.setStatus("current")


class _JunidApsConfigWaitToRestore_Type(Integer32):
    """Custom type junidApsConfigWaitToRestore based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_JunidApsConfigWaitToRestore_Type.__name__ = "Integer32"
_JunidApsConfigWaitToRestore_Object = MibTableColumn
junidApsConfigWaitToRestore = _JunidApsConfigWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 9),
    _JunidApsConfigWaitToRestore_Type()
)
junidApsConfigWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsConfigWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    junidApsConfigWaitToRestore.setUnits("seconds")
_JunidApsConfigCreationTime_Type = TimeStamp
_JunidApsConfigCreationTime_Object = MibTableColumn
junidApsConfigCreationTime = _JunidApsConfigCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 1, 2, 1, 10),
    _JunidApsConfigCreationTime_Type()
)
junidApsConfigCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsConfigCreationTime.setStatus("current")
_JunidApsStatusTable_Object = MibTable
junidApsStatusTable = _JunidApsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    junidApsStatusTable.setStatus("current")
_JunidApsStatusEntry_Object = MibTableRow
junidApsStatusEntry = _JunidApsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1)
)
junidApsStatusEntry.setIndexNames(
    (1, "APS-MIB-JUNI", "junidApsConfigName"),
)
if mibBuilder.loadTexts:
    junidApsStatusEntry.setStatus("current")
_JunidApsStatusK1K2Rcv_Type = JunidApsK1K2
_JunidApsStatusK1K2Rcv_Object = MibTableColumn
junidApsStatusK1K2Rcv = _JunidApsStatusK1K2Rcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 1),
    _JunidApsStatusK1K2Rcv_Type()
)
junidApsStatusK1K2Rcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusK1K2Rcv.setStatus("current")
_JunidApsStatusK1K2Trans_Type = JunidApsK1K2
_JunidApsStatusK1K2Trans_Object = MibTableColumn
junidApsStatusK1K2Trans = _JunidApsStatusK1K2Trans_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 2),
    _JunidApsStatusK1K2Trans_Type()
)
junidApsStatusK1K2Trans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusK1K2Trans.setStatus("current")


class _JunidApsStatusCurrent_Type(Bits):
    """Custom type junidApsStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("channelMismatch", 1),
          ("extraTraffic", 4),
          ("feplf", 3),
          ("modeMismatch", 0),
          ("psbf", 2))
    )

_JunidApsStatusCurrent_Type.__name__ = "Bits"
_JunidApsStatusCurrent_Object = MibTableColumn
junidApsStatusCurrent = _JunidApsStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 3),
    _JunidApsStatusCurrent_Type()
)
junidApsStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusCurrent.setStatus("current")
_JunidApsStatusModeMismatches_Type = Counter32
_JunidApsStatusModeMismatches_Object = MibTableColumn
junidApsStatusModeMismatches = _JunidApsStatusModeMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 4),
    _JunidApsStatusModeMismatches_Type()
)
junidApsStatusModeMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusModeMismatches.setStatus("current")
_JunidApsStatusChannelMismatches_Type = Counter32
_JunidApsStatusChannelMismatches_Object = MibTableColumn
junidApsStatusChannelMismatches = _JunidApsStatusChannelMismatches_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 5),
    _JunidApsStatusChannelMismatches_Type()
)
junidApsStatusChannelMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusChannelMismatches.setStatus("current")
_JunidApsStatusPSBFs_Type = Counter32
_JunidApsStatusPSBFs_Object = MibTableColumn
junidApsStatusPSBFs = _JunidApsStatusPSBFs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 6),
    _JunidApsStatusPSBFs_Type()
)
junidApsStatusPSBFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusPSBFs.setStatus("current")
_JunidApsStatusFEPLFs_Type = Counter32
_JunidApsStatusFEPLFs_Object = MibTableColumn
junidApsStatusFEPLFs = _JunidApsStatusFEPLFs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 7),
    _JunidApsStatusFEPLFs_Type()
)
junidApsStatusFEPLFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusFEPLFs.setStatus("current")
_JunidApsStatusSwitchedChannel_Type = Integer32
_JunidApsStatusSwitchedChannel_Object = MibTableColumn
junidApsStatusSwitchedChannel = _JunidApsStatusSwitchedChannel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 2, 1, 8),
    _JunidApsStatusSwitchedChannel_Type()
)
junidApsStatusSwitchedChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsStatusSwitchedChannel.setStatus("current")
_JunidApsMap_ObjectIdentity = ObjectIdentity
junidApsMap = _JunidApsMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 3)
)
_JunidApsChanLTEs_Type = Gauge32
_JunidApsChanLTEs_Object = MibScalar
junidApsChanLTEs = _JunidApsChanLTEs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 3, 1),
    _JunidApsChanLTEs_Type()
)
junidApsChanLTEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsChanLTEs.setStatus("current")
_JunidApsMapTable_Object = MibTable
junidApsMapTable = _JunidApsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    junidApsMapTable.setStatus("current")
_JunidApsMapEntry_Object = MibTableRow
junidApsMapEntry = _JunidApsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 3, 2, 1)
)
junidApsMapEntry.setIndexNames(
    (0, "APS-MIB-JUNI", "junidApsMapIfIndex"),
)
if mibBuilder.loadTexts:
    junidApsMapEntry.setStatus("current")
_JunidApsMapIfIndex_Type = InterfaceIndex
_JunidApsMapIfIndex_Object = MibTableColumn
junidApsMapIfIndex = _JunidApsMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 3, 2, 1, 1),
    _JunidApsMapIfIndex_Type()
)
junidApsMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidApsMapIfIndex.setStatus("current")


class _JunidApsMapGroupName_Type(SnmpAdminString):
    """Custom type junidApsMapGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JunidApsMapGroupName_Type.__name__ = "SnmpAdminString"
_JunidApsMapGroupName_Object = MibTableColumn
junidApsMapGroupName = _JunidApsMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 3, 2, 1, 2),
    _JunidApsMapGroupName_Type()
)
junidApsMapGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsMapGroupName.setStatus("current")


class _JunidApsMapChanNumber_Type(Integer32):
    """Custom type junidApsMapChanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 14),
    )


_JunidApsMapChanNumber_Type.__name__ = "Integer32"
_JunidApsMapChanNumber_Object = MibTableColumn
junidApsMapChanNumber = _JunidApsMapChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 3, 2, 1, 3),
    _JunidApsMapChanNumber_Type()
)
junidApsMapChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsMapChanNumber.setStatus("current")
_JunidApsChanConfigTable_Object = MibTable
junidApsChanConfigTable = _JunidApsChanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    junidApsChanConfigTable.setStatus("current")
_JunidApsChanConfigEntry_Object = MibTableRow
junidApsChanConfigEntry = _JunidApsChanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 4, 1)
)
junidApsChanConfigEntry.setIndexNames(
    (0, "APS-MIB-JUNI", "junidApsChanConfigGroupName"),
    (0, "APS-MIB-JUNI", "junidApsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    junidApsChanConfigEntry.setStatus("current")


class _JunidApsChanConfigGroupName_Type(SnmpAdminString):
    """Custom type junidApsChanConfigGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JunidApsChanConfigGroupName_Type.__name__ = "SnmpAdminString"
_JunidApsChanConfigGroupName_Object = MibTableColumn
junidApsChanConfigGroupName = _JunidApsChanConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 4, 1, 1),
    _JunidApsChanConfigGroupName_Type()
)
junidApsChanConfigGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidApsChanConfigGroupName.setStatus("current")


class _JunidApsChanConfigNumber_Type(Integer32):
    """Custom type junidApsChanConfigNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_JunidApsChanConfigNumber_Type.__name__ = "Integer32"
_JunidApsChanConfigNumber_Object = MibTableColumn
junidApsChanConfigNumber = _JunidApsChanConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 4, 1, 2),
    _JunidApsChanConfigNumber_Type()
)
junidApsChanConfigNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    junidApsChanConfigNumber.setStatus("current")
_JunidApsChanConfigRowStatus_Type = RowStatus
_JunidApsChanConfigRowStatus_Object = MibTableColumn
junidApsChanConfigRowStatus = _JunidApsChanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 4, 1, 3),
    _JunidApsChanConfigRowStatus_Type()
)
junidApsChanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsChanConfigRowStatus.setStatus("current")
_JunidApsChanConfigIfIndex_Type = InterfaceIndex
_JunidApsChanConfigIfIndex_Object = MibTableColumn
junidApsChanConfigIfIndex = _JunidApsChanConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 4, 1, 4),
    _JunidApsChanConfigIfIndex_Type()
)
junidApsChanConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsChanConfigIfIndex.setStatus("current")


class _JunidApsChanConfigPriority_Type(Integer32):
    """Custom type junidApsChanConfigPriority based on Integer32"""
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


_JunidApsChanConfigPriority_Type.__name__ = "Integer32"
_JunidApsChanConfigPriority_Object = MibTableColumn
junidApsChanConfigPriority = _JunidApsChanConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 4, 1, 5),
    _JunidApsChanConfigPriority_Type()
)
junidApsChanConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    junidApsChanConfigPriority.setStatus("current")
_JunidApsCommandTable_Object = MibTable
junidApsCommandTable = _JunidApsCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    junidApsCommandTable.setStatus("current")
_JunidApsCommandEntry_Object = MibTableRow
junidApsCommandEntry = _JunidApsCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 5, 1)
)
junidApsCommandEntry.setIndexNames(
    (0, "APS-MIB-JUNI", "junidApsChanConfigGroupName"),
    (0, "APS-MIB-JUNI", "junidApsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    junidApsCommandEntry.setStatus("current")
_JunidApsCommandSwitch_Type = JunidApsSwitchCommand
_JunidApsCommandSwitch_Object = MibTableColumn
junidApsCommandSwitch = _JunidApsCommandSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 5, 1, 1),
    _JunidApsCommandSwitch_Type()
)
junidApsCommandSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    junidApsCommandSwitch.setStatus("current")
_JunidApsCommandControl_Type = JunidApsControlCommand
_JunidApsCommandControl_Object = MibTableColumn
junidApsCommandControl = _JunidApsCommandControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 5, 1, 2),
    _JunidApsCommandControl_Type()
)
junidApsCommandControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    junidApsCommandControl.setStatus("current")
_JunidApsChanStatusTable_Object = MibTable
junidApsChanStatusTable = _JunidApsChanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    junidApsChanStatusTable.setStatus("current")
_JunidApsChanStatusEntry_Object = MibTableRow
junidApsChanStatusEntry = _JunidApsChanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6, 1)
)
junidApsChanStatusEntry.setIndexNames(
    (0, "APS-MIB-JUNI", "junidApsChanConfigGroupName"),
    (0, "APS-MIB-JUNI", "junidApsChanConfigNumber"),
)
if mibBuilder.loadTexts:
    junidApsChanStatusEntry.setStatus("current")


class _JunidApsChanStatusCurrent_Type(Bits):
    """Custom type junidApsChanStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sd", 1),
          ("sf", 2),
          ("switched", 3))
    )

_JunidApsChanStatusCurrent_Type.__name__ = "Bits"
_JunidApsChanStatusCurrent_Object = MibTableColumn
junidApsChanStatusCurrent = _JunidApsChanStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6, 1, 1),
    _JunidApsChanStatusCurrent_Type()
)
junidApsChanStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsChanStatusCurrent.setStatus("current")
_JunidApsChanStatusSignalDegrades_Type = Counter32
_JunidApsChanStatusSignalDegrades_Object = MibTableColumn
junidApsChanStatusSignalDegrades = _JunidApsChanStatusSignalDegrades_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6, 1, 2),
    _JunidApsChanStatusSignalDegrades_Type()
)
junidApsChanStatusSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsChanStatusSignalDegrades.setStatus("current")
_JunidApsChanStatusSignalFailures_Type = Counter32
_JunidApsChanStatusSignalFailures_Object = MibTableColumn
junidApsChanStatusSignalFailures = _JunidApsChanStatusSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6, 1, 3),
    _JunidApsChanStatusSignalFailures_Type()
)
junidApsChanStatusSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsChanStatusSignalFailures.setStatus("current")
_JunidApsChanStatusSwitchovers_Type = Counter32
_JunidApsChanStatusSwitchovers_Object = MibTableColumn
junidApsChanStatusSwitchovers = _JunidApsChanStatusSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6, 1, 4),
    _JunidApsChanStatusSwitchovers_Type()
)
junidApsChanStatusSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsChanStatusSwitchovers.setStatus("current")
_JunidApsChanStatusLastSwitchover_Type = TimeStamp
_JunidApsChanStatusLastSwitchover_Object = MibTableColumn
junidApsChanStatusLastSwitchover = _JunidApsChanStatusLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6, 1, 5),
    _JunidApsChanStatusLastSwitchover_Type()
)
junidApsChanStatusLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsChanStatusLastSwitchover.setStatus("current")
_JunidApsChanStatusSwitchoverSeconds_Type = Counter32
_JunidApsChanStatusSwitchoverSeconds_Object = MibTableColumn
junidApsChanStatusSwitchoverSeconds = _JunidApsChanStatusSwitchoverSeconds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 1, 6, 1, 6),
    _JunidApsChanStatusSwitchoverSeconds_Type()
)
junidApsChanStatusSwitchoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    junidApsChanStatusSwitchoverSeconds.setStatus("current")
_JunidApsMIBNotifications_ObjectIdentity = ObjectIdentity
junidApsMIBNotifications = _JunidApsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 2)
)
_JunidApsNotificationsPrefix_ObjectIdentity = ObjectIdentity
junidApsNotificationsPrefix = _JunidApsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 2, 0)
)
_JunidApsMIBConformance_ObjectIdentity = ObjectIdentity
junidApsMIBConformance = _JunidApsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3)
)
_JunidApsGroups_ObjectIdentity = ObjectIdentity
junidApsGroups = _JunidApsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1)
)
_JunidApsCompliances_ObjectIdentity = ObjectIdentity
junidApsCompliances = _JunidApsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 2)
)

# Managed Objects groups

junidApsConfigGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 1)
)
junidApsConfigGeneral.setObjects(
      *(("APS-MIB-JUNI", "junidApsConfigMode"),
        ("APS-MIB-JUNI", "junidApsConfigRevert"),
        ("APS-MIB-JUNI", "junidApsConfigDirection"),
        ("APS-MIB-JUNI", "junidApsConfigExtraTraffic"),
        ("APS-MIB-JUNI", "junidApsConfigSdBerThreshold"),
        ("APS-MIB-JUNI", "junidApsConfigSfBerThreshold"),
        ("APS-MIB-JUNI", "junidApsConfigCreationTime"),
        ("APS-MIB-JUNI", "junidApsConfigRowStatus"))
)
if mibBuilder.loadTexts:
    junidApsConfigGeneral.setStatus("current")

junidApsConfigWtr = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 2)
)
junidApsConfigWtr.setObjects(
    ("APS-MIB-JUNI", "junidApsConfigWaitToRestore")
)
if mibBuilder.loadTexts:
    junidApsConfigWtr.setStatus("current")

junidApsCommandOnePlusOne = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 3)
)
junidApsCommandOnePlusOne.setObjects(
    ("APS-MIB-JUNI", "junidApsCommandSwitch")
)
if mibBuilder.loadTexts:
    junidApsCommandOnePlusOne.setStatus("current")

junidApsCommandOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 4)
)
junidApsCommandOneToN.setObjects(
      *(("APS-MIB-JUNI", "junidApsCommandSwitch"),
        ("APS-MIB-JUNI", "junidApsCommandControl"))
)
if mibBuilder.loadTexts:
    junidApsCommandOneToN.setStatus("current")

junidApsStatusGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 5)
)
junidApsStatusGeneral.setObjects(
      *(("APS-MIB-JUNI", "junidApsStatusK1K2Rcv"),
        ("APS-MIB-JUNI", "junidApsStatusK1K2Trans"),
        ("APS-MIB-JUNI", "junidApsStatusCurrent"),
        ("APS-MIB-JUNI", "junidApsStatusModeMismatches"),
        ("APS-MIB-JUNI", "junidApsStatusChannelMismatches"),
        ("APS-MIB-JUNI", "junidApsStatusPSBFs"),
        ("APS-MIB-JUNI", "junidApsStatusFEPLFs"),
        ("APS-MIB-JUNI", "junidApsStatusSwitchedChannel"))
)
if mibBuilder.loadTexts:
    junidApsStatusGeneral.setStatus("current")

junidApsChanGeneral = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 6)
)
junidApsChanGeneral.setObjects(
      *(("APS-MIB-JUNI", "junidApsChanConfigIfIndex"),
        ("APS-MIB-JUNI", "junidApsChanConfigRowStatus"),
        ("APS-MIB-JUNI", "junidApsChanStatusCurrent"),
        ("APS-MIB-JUNI", "junidApsChanStatusSignalDegrades"),
        ("APS-MIB-JUNI", "junidApsChanStatusSignalFailures"),
        ("APS-MIB-JUNI", "junidApsChanStatusSwitchovers"),
        ("APS-MIB-JUNI", "junidApsChanStatusLastSwitchover"),
        ("APS-MIB-JUNI", "junidApsChanStatusSwitchoverSeconds"))
)
if mibBuilder.loadTexts:
    junidApsChanGeneral.setStatus("current")

junidApsChanOneToN = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 7)
)
junidApsChanOneToN.setObjects(
    ("APS-MIB-JUNI", "junidApsChanConfigPriority")
)
if mibBuilder.loadTexts:
    junidApsChanOneToN.setStatus("current")

junidApsTotalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 8)
)
junidApsTotalsGroup.setObjects(
      *(("APS-MIB-JUNI", "junidApsConfigGroups"),
        ("APS-MIB-JUNI", "junidApsChanLTEs"))
)
if mibBuilder.loadTexts:
    junidApsTotalsGroup.setStatus("current")

junidApsMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 9)
)
junidApsMapGroup.setObjects(
      *(("APS-MIB-JUNI", "junidApsMapGroupName"),
        ("APS-MIB-JUNI", "junidApsMapChanNumber"))
)
if mibBuilder.loadTexts:
    junidApsMapGroup.setStatus("current")


# Notification objects

junidApsEventSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 2, 0, 1)
)
junidApsEventSwitchover.setObjects(
      *(("APS-MIB-JUNI", "junidApsChanStatusSwitchovers"),
        ("APS-MIB-JUNI", "junidApsChanStatusCurrent"))
)
if mibBuilder.loadTexts:
    junidApsEventSwitchover.setStatus(
        "current"
    )

junidApsEventModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 2, 0, 2)
)
junidApsEventModeMismatch.setObjects(
      *(("APS-MIB-JUNI", "junidApsStatusModeMismatches"),
        ("APS-MIB-JUNI", "junidApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    junidApsEventModeMismatch.setStatus(
        "current"
    )

junidApsEventChannelMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 2, 0, 3)
)
junidApsEventChannelMismatch.setObjects(
      *(("APS-MIB-JUNI", "junidApsStatusChannelMismatches"),
        ("APS-MIB-JUNI", "junidApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    junidApsEventChannelMismatch.setStatus(
        "current"
    )

junidApsEventPSBF = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 2, 0, 4)
)
junidApsEventPSBF.setObjects(
      *(("APS-MIB-JUNI", "junidApsStatusPSBFs"),
        ("APS-MIB-JUNI", "junidApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    junidApsEventPSBF.setStatus(
        "current"
    )

junidApsEventFEPLF = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 2, 0, 5)
)
junidApsEventFEPLF.setObjects(
      *(("APS-MIB-JUNI", "junidApsStatusFEPLFs"),
        ("APS-MIB-JUNI", "junidApsStatusCurrent"))
)
if mibBuilder.loadTexts:
    junidApsEventFEPLF.setStatus(
        "current"
    )


# Notifications groups

junidApsEventOptional = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 1, 10)
)
junidApsEventOptional.setObjects(
      *(("APS-MIB-JUNI", "junidApsEventSwitchover"),
        ("APS-MIB-JUNI", "junidApsEventModeMismatch"),
        ("APS-MIB-JUNI", "junidApsEventChannelMismatch"),
        ("APS-MIB-JUNI", "junidApsEventPSBF"),
        ("APS-MIB-JUNI", "junidApsEventFEPLF"))
)
if mibBuilder.loadTexts:
    junidApsEventOptional.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

junidApsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 3, 2, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    junidApsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APS-MIB-JUNI",
    **{"JunidApsK1K2": JunidApsK1K2,
       "JunidApsSwitchCommand": JunidApsSwitchCommand,
       "JunidApsControlCommand": JunidApsControlCommand,
       "junidApsMIB": junidApsMIB,
       "junidApsMIBObjects": junidApsMIBObjects,
       "junidApsConfig": junidApsConfig,
       "junidApsConfigGroups": junidApsConfigGroups,
       "junidApsConfigTable": junidApsConfigTable,
       "junidApsConfigEntry": junidApsConfigEntry,
       "junidApsConfigName": junidApsConfigName,
       "junidApsConfigRowStatus": junidApsConfigRowStatus,
       "junidApsConfigMode": junidApsConfigMode,
       "junidApsConfigRevert": junidApsConfigRevert,
       "junidApsConfigDirection": junidApsConfigDirection,
       "junidApsConfigExtraTraffic": junidApsConfigExtraTraffic,
       "junidApsConfigSdBerThreshold": junidApsConfigSdBerThreshold,
       "junidApsConfigSfBerThreshold": junidApsConfigSfBerThreshold,
       "junidApsConfigWaitToRestore": junidApsConfigWaitToRestore,
       "junidApsConfigCreationTime": junidApsConfigCreationTime,
       "junidApsStatusTable": junidApsStatusTable,
       "junidApsStatusEntry": junidApsStatusEntry,
       "junidApsStatusK1K2Rcv": junidApsStatusK1K2Rcv,
       "junidApsStatusK1K2Trans": junidApsStatusK1K2Trans,
       "junidApsStatusCurrent": junidApsStatusCurrent,
       "junidApsStatusModeMismatches": junidApsStatusModeMismatches,
       "junidApsStatusChannelMismatches": junidApsStatusChannelMismatches,
       "junidApsStatusPSBFs": junidApsStatusPSBFs,
       "junidApsStatusFEPLFs": junidApsStatusFEPLFs,
       "junidApsStatusSwitchedChannel": junidApsStatusSwitchedChannel,
       "junidApsMap": junidApsMap,
       "junidApsChanLTEs": junidApsChanLTEs,
       "junidApsMapTable": junidApsMapTable,
       "junidApsMapEntry": junidApsMapEntry,
       "junidApsMapIfIndex": junidApsMapIfIndex,
       "junidApsMapGroupName": junidApsMapGroupName,
       "junidApsMapChanNumber": junidApsMapChanNumber,
       "junidApsChanConfigTable": junidApsChanConfigTable,
       "junidApsChanConfigEntry": junidApsChanConfigEntry,
       "junidApsChanConfigGroupName": junidApsChanConfigGroupName,
       "junidApsChanConfigNumber": junidApsChanConfigNumber,
       "junidApsChanConfigRowStatus": junidApsChanConfigRowStatus,
       "junidApsChanConfigIfIndex": junidApsChanConfigIfIndex,
       "junidApsChanConfigPriority": junidApsChanConfigPriority,
       "junidApsCommandTable": junidApsCommandTable,
       "junidApsCommandEntry": junidApsCommandEntry,
       "junidApsCommandSwitch": junidApsCommandSwitch,
       "junidApsCommandControl": junidApsCommandControl,
       "junidApsChanStatusTable": junidApsChanStatusTable,
       "junidApsChanStatusEntry": junidApsChanStatusEntry,
       "junidApsChanStatusCurrent": junidApsChanStatusCurrent,
       "junidApsChanStatusSignalDegrades": junidApsChanStatusSignalDegrades,
       "junidApsChanStatusSignalFailures": junidApsChanStatusSignalFailures,
       "junidApsChanStatusSwitchovers": junidApsChanStatusSwitchovers,
       "junidApsChanStatusLastSwitchover": junidApsChanStatusLastSwitchover,
       "junidApsChanStatusSwitchoverSeconds": junidApsChanStatusSwitchoverSeconds,
       "junidApsMIBNotifications": junidApsMIBNotifications,
       "junidApsNotificationsPrefix": junidApsNotificationsPrefix,
       "junidApsEventSwitchover": junidApsEventSwitchover,
       "junidApsEventModeMismatch": junidApsEventModeMismatch,
       "junidApsEventChannelMismatch": junidApsEventChannelMismatch,
       "junidApsEventPSBF": junidApsEventPSBF,
       "junidApsEventFEPLF": junidApsEventFEPLF,
       "junidApsMIBConformance": junidApsMIBConformance,
       "junidApsGroups": junidApsGroups,
       "junidApsConfigGeneral": junidApsConfigGeneral,
       "junidApsConfigWtr": junidApsConfigWtr,
       "junidApsCommandOnePlusOne": junidApsCommandOnePlusOne,
       "junidApsCommandOneToN": junidApsCommandOneToN,
       "junidApsStatusGeneral": junidApsStatusGeneral,
       "junidApsChanGeneral": junidApsChanGeneral,
       "junidApsChanOneToN": junidApsChanOneToN,
       "junidApsTotalsGroup": junidApsTotalsGroup,
       "junidApsMapGroup": junidApsMapGroup,
       "junidApsEventOptional": junidApsEventOptional,
       "junidApsCompliances": junidApsCompliances,
       "junidApsCompliance": junidApsCompliance}
)
