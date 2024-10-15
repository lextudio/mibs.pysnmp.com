# SNMP MIB module (CISCO-DSP-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DSP-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:10 2024
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

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDspMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86)
)
ciscoDspMgmtMIB.setRevisions(
        ("2011-02-17 00:00",
         "2009-04-09 00:00",
         "2007-09-03 00:05",
         "2007-06-25 00:00",
         "2007-06-20 00:00",
         "2006-04-14 00:00",
         "2005-11-02 00:00",
         "2005-08-17 00:00",
         "2005-08-04 00:00",
         "2005-06-20 00:00",
         "2005-05-18 00:00",
         "2005-04-18 00:00",
         "2004-10-21 00:00",
         "2003-10-10 00:00",
         "2003-08-20 00:00",
         "2003-08-14 00:00",
         "2000-08-14 00:00",
         "1998-10-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CdspMgmtNotifications_ObjectIdentity = ObjectIdentity
cdspMgmtNotifications = _CdspMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 0)
)
_CdspMgmtObjects_ObjectIdentity = ObjectIdentity
cdspMgmtObjects = _CdspMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1)
)
_CdspCardObjects_ObjectIdentity = ObjectIdentity
cdspCardObjects = _CdspCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1)
)
_CdspCardStatusTable_Object = MibTable
cdspCardStatusTable = _CdspCardStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdspCardStatusTable.setStatus("current")
_CdspCardStatusEntry_Object = MibTableRow
cdspCardStatusEntry = _CdspCardStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1)
)
cdspCardStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cdspCardStatusEntry.setStatus("current")
_CdspCardIndex_Type = Integer32
_CdspCardIndex_Object = MibTableColumn
cdspCardIndex = _CdspCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 1),
    _CdspCardIndex_Type()
)
cdspCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCardIndex.setStatus("current")


class _CdspCardState_Type(Integer32):
    """Custom type cdspCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("fatal", 4),
          ("normal", 1),
          ("offLine", 5),
          ("warning", 2))
    )


_CdspCardState_Type.__name__ = "Integer32"
_CdspCardState_Object = MibTableColumn
cdspCardState = _CdspCardState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 2),
    _CdspCardState_Type()
)
cdspCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCardState.setStatus("current")


class _CdspCardResourceUtilization_Type(Unsigned32):
    """Custom type cdspCardResourceUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdspCardResourceUtilization_Type.__name__ = "Unsigned32"
_CdspCardResourceUtilization_Object = MibTableColumn
cdspCardResourceUtilization = _CdspCardResourceUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 3),
    _CdspCardResourceUtilization_Type()
)
cdspCardResourceUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCardResourceUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cdspCardResourceUtilization.setUnits("percent")


class _CdspCardLastHiWaterUtilization_Type(Unsigned32):
    """Custom type cdspCardLastHiWaterUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdspCardLastHiWaterUtilization_Type.__name__ = "Unsigned32"
_CdspCardLastHiWaterUtilization_Object = MibTableColumn
cdspCardLastHiWaterUtilization = _CdspCardLastHiWaterUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 4),
    _CdspCardLastHiWaterUtilization_Type()
)
cdspCardLastHiWaterUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCardLastHiWaterUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cdspCardLastHiWaterUtilization.setUnits("percent")
_CdspCardLastResetTime_Type = TimeStamp
_CdspCardLastResetTime_Object = MibTableColumn
cdspCardLastResetTime = _CdspCardLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 5),
    _CdspCardLastResetTime_Type()
)
cdspCardLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCardLastResetTime.setStatus("current")
_CdspCardMaxChanPerDSP_Type = Unsigned32
_CdspCardMaxChanPerDSP_Object = MibTableColumn
cdspCardMaxChanPerDSP = _CdspCardMaxChanPerDSP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 6),
    _CdspCardMaxChanPerDSP_Type()
)
cdspCardMaxChanPerDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCardMaxChanPerDSP.setStatus("current")
if mibBuilder.loadTexts:
    cdspCardMaxChanPerDSP.setUnits("channels")


class _CdspTotalDsp_Type(Unsigned32):
    """Custom type cdspTotalDsp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CdspTotalDsp_Type.__name__ = "Unsigned32"
_CdspTotalDsp_Object = MibTableColumn
cdspTotalDsp = _CdspTotalDsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 7),
    _CdspTotalDsp_Type()
)
cdspTotalDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspTotalDsp.setStatus("current")


class _CdspFailedDsp_Type(Gauge32):
    """Custom type cdspFailedDsp based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CdspFailedDsp_Type.__name__ = "Gauge32"
_CdspFailedDsp_Object = MibTableColumn
cdspFailedDsp = _CdspFailedDsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 8),
    _CdspFailedDsp_Type()
)
cdspFailedDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspFailedDsp.setStatus("current")


class _CdspDspSwitchOverThreshold_Type(Unsigned32):
    """Custom type cdspDspSwitchOverThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_CdspDspSwitchOverThreshold_Type.__name__ = "Unsigned32"
_CdspDspSwitchOverThreshold_Object = MibTableColumn
cdspDspSwitchOverThreshold = _CdspDspSwitchOverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 9),
    _CdspDspSwitchOverThreshold_Type()
)
cdspDspSwitchOverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspDspSwitchOverThreshold.setStatus("current")


class _CdspCongestedDsp_Type(Gauge32):
    """Custom type cdspCongestedDsp based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CdspCongestedDsp_Type.__name__ = "Gauge32"
_CdspCongestedDsp_Object = MibTableColumn
cdspCongestedDsp = _CdspCongestedDsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 10),
    _CdspCongestedDsp_Type()
)
cdspCongestedDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCongestedDsp.setStatus("current")


class _CdspNormalDsp_Type(Gauge32):
    """Custom type cdspNormalDsp based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CdspNormalDsp_Type.__name__ = "Gauge32"
_CdspNormalDsp_Object = MibTableColumn
cdspNormalDsp = _CdspNormalDsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 11),
    _CdspNormalDsp_Type()
)
cdspNormalDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspNormalDsp.setStatus("current")


class _CdspNx64Dsp_Type(Unsigned32):
    """Custom type cdspNx64Dsp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_CdspNx64Dsp_Type.__name__ = "Unsigned32"
_CdspNx64Dsp_Object = MibTableColumn
cdspNx64Dsp = _CdspNx64Dsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 12),
    _CdspNx64Dsp_Type()
)
cdspNx64Dsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspNx64Dsp.setStatus("current")


class _CdspCodecTemplateSupported_Type(Integer32):
    """Custom type cdspCodecTemplateSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cable", 2),
          ("cdma3G", 4),
          ("fmc", 6),
          ("tgw", 1),
          ("tgw2", 5),
          ("umts3G", 3))
    )


_CdspCodecTemplateSupported_Type.__name__ = "Integer32"
_CdspCodecTemplateSupported_Object = MibTableColumn
cdspCodecTemplateSupported = _CdspCodecTemplateSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 13),
    _CdspCodecTemplateSupported_Type()
)
cdspCodecTemplateSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCodecTemplateSupported.setStatus("current")
_CdspCardVideoPoolUtilization_Type = Percent
_CdspCardVideoPoolUtilization_Object = MibTableColumn
cdspCardVideoPoolUtilization = _CdspCardVideoPoolUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 14),
    _CdspCardVideoPoolUtilization_Type()
)
cdspCardVideoPoolUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCardVideoPoolUtilization.setStatus("current")


class _CdspCardVideoPoolUtilizationThreshold_Type(Unsigned32):
    """Custom type cdspCardVideoPoolUtilizationThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CdspCardVideoPoolUtilizationThreshold_Type.__name__ = "Unsigned32"
_CdspCardVideoPoolUtilizationThreshold_Object = MibTableColumn
cdspCardVideoPoolUtilizationThreshold = _CdspCardVideoPoolUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 1, 1, 1, 15),
    _CdspCardVideoPoolUtilizationThreshold_Type()
)
cdspCardVideoPoolUtilizationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspCardVideoPoolUtilizationThreshold.setStatus("current")
_CdspObjects_ObjectIdentity = ObjectIdentity
cdspObjects = _CdspObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2)
)
_CdspStatusTable_Object = MibTable
cdspStatusTable = _CdspStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdspStatusTable.setStatus("current")
_CdspStatusEntry_Object = MibTableRow
cdspStatusEntry = _CdspStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1)
)
cdspStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cdspStatusEntry.setStatus("current")


class _CdspOperState_Type(Integer32):
    """Custom type cdspOperState based on Integer32"""
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
        *(("congested", 3),
          ("failed", 4),
          ("normal", 1),
          ("shutdown", 2))
    )


_CdspOperState_Type.__name__ = "Integer32"
_CdspOperState_Object = MibTableColumn
cdspOperState = _CdspOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 1),
    _CdspOperState_Type()
)
cdspOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspOperState.setStatus("current")
_CdspAlarms_Type = Counter32
_CdspAlarms_Object = MibTableColumn
cdspAlarms = _CdspAlarms_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 2),
    _CdspAlarms_Type()
)
cdspAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspAlarms.setStatus("current")


class _CdspLastAlarmCause_Type(Integer32):
    """Custom type cdspLastAlarmCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dspBufferError", 5),
          ("dspDownloadError", 6),
          ("dspFatalError", 3),
          ("dspMemoryError", 4),
          ("noAlarm", 2),
          ("other", 1))
    )


_CdspLastAlarmCause_Type.__name__ = "Integer32"
_CdspLastAlarmCause_Object = MibTableColumn
cdspLastAlarmCause = _CdspLastAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 3),
    _CdspLastAlarmCause_Type()
)
cdspLastAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspLastAlarmCause.setStatus("current")
_CdspLastAlarmCauseText_Type = DisplayString
_CdspLastAlarmCauseText_Object = MibTableColumn
cdspLastAlarmCauseText = _CdspLastAlarmCauseText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 4),
    _CdspLastAlarmCauseText_Type()
)
cdspLastAlarmCauseText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspLastAlarmCauseText.setStatus("current")
_CdspLastAlarmTime_Type = TimeStamp
_CdspLastAlarmTime_Object = MibTableColumn
cdspLastAlarmTime = _CdspLastAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 5),
    _CdspLastAlarmTime_Type()
)
cdspLastAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspLastAlarmTime.setStatus("current")
_CdspTotalChannels_Type = Unsigned32
_CdspTotalChannels_Object = MibTableColumn
cdspTotalChannels = _CdspTotalChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 6),
    _CdspTotalChannels_Type()
)
cdspTotalChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspTotalChannels.setStatus("current")
if mibBuilder.loadTexts:
    cdspTotalChannels.setUnits("channels")
_CdspInUseChannels_Type = Gauge32
_CdspInUseChannels_Object = MibTableColumn
cdspInUseChannels = _CdspInUseChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 7),
    _CdspInUseChannels_Type()
)
cdspInUseChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspInUseChannels.setStatus("current")
if mibBuilder.loadTexts:
    cdspInUseChannels.setUnits("channels")
_CdspActiveChannels_Type = Gauge32
_CdspActiveChannels_Object = MibTableColumn
cdspActiveChannels = _CdspActiveChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 8),
    _CdspActiveChannels_Type()
)
cdspActiveChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspActiveChannels.setStatus("current")
if mibBuilder.loadTexts:
    cdspActiveChannels.setUnits("channels")
_CdspSigBearerChannelSplit_Type = TruthValue
_CdspSigBearerChannelSplit_Object = MibTableColumn
cdspSigBearerChannelSplit = _CdspSigBearerChannelSplit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 9),
    _CdspSigBearerChannelSplit_Type()
)
cdspSigBearerChannelSplit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspSigBearerChannelSplit.setStatus("current")
_CdspNumCongestionOccurrence_Type = Counter32
_CdspNumCongestionOccurrence_Object = MibTableColumn
cdspNumCongestionOccurrence = _CdspNumCongestionOccurrence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 10),
    _CdspNumCongestionOccurrence_Type()
)
cdspNumCongestionOccurrence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspNumCongestionOccurrence.setStatus("current")


class _CdspDspNum_Type(Unsigned32):
    """Custom type cdspDspNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 252),
    )


_CdspDspNum_Type.__name__ = "Unsigned32"
_CdspDspNum_Object = MibTableColumn
cdspDspNum = _CdspDspNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 1, 1, 11),
    _CdspDspNum_Type()
)
cdspDspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspDspNum.setStatus("current")
_CdspStatusXTable_Object = MibTable
cdspStatusXTable = _CdspStatusXTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cdspStatusXTable.setStatus("current")
_CdspStatusXEntry_Object = MibTableRow
cdspStatusXEntry = _CdspStatusXEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cdspStatusXEntry.setStatus("current")
_CdspXNumberOfBearerCalls_Type = Gauge32
_CdspXNumberOfBearerCalls_Object = MibTableColumn
cdspXNumberOfBearerCalls = _CdspXNumberOfBearerCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 2, 1, 1),
    _CdspXNumberOfBearerCalls_Type()
)
cdspXNumberOfBearerCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspXNumberOfBearerCalls.setStatus("current")
if mibBuilder.loadTexts:
    cdspXNumberOfBearerCalls.setUnits("calls")
_CdspXNumberOfSigCalls_Type = Gauge32
_CdspXNumberOfSigCalls_Object = MibTableColumn
cdspXNumberOfSigCalls = _CdspXNumberOfSigCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 2, 1, 2),
    _CdspXNumberOfSigCalls_Type()
)
cdspXNumberOfSigCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspXNumberOfSigCalls.setStatus("current")
if mibBuilder.loadTexts:
    cdspXNumberOfSigCalls.setUnits("calls")
_CdspXAvailableBearerBandwidth_Type = Gauge32
_CdspXAvailableBearerBandwidth_Object = MibTableColumn
cdspXAvailableBearerBandwidth = _CdspXAvailableBearerBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 2, 1, 3),
    _CdspXAvailableBearerBandwidth_Type()
)
cdspXAvailableBearerBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspXAvailableBearerBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cdspXAvailableBearerBandwidth.setUnits("percent")
_CdspXAvailableSigBandwidth_Type = Gauge32
_CdspXAvailableSigBandwidth_Object = MibTableColumn
cdspXAvailableSigBandwidth = _CdspXAvailableSigBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 2, 2, 1, 4),
    _CdspXAvailableSigBandwidth_Type()
)
cdspXAvailableSigBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspXAvailableSigBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cdspXAvailableSigBandwidth.setUnits("percent")
_CdspMIBNotificationEnables_ObjectIdentity = ObjectIdentity
cdspMIBNotificationEnables = _CdspMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 3)
)


class _CdspMIBEnableCardStatusNotification_Type(TruthValue):
    """Custom type cdspMIBEnableCardStatusNotification based on TruthValue"""


_CdspMIBEnableCardStatusNotification_Object = MibScalar
cdspMIBEnableCardStatusNotification = _CdspMIBEnableCardStatusNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 3, 1),
    _CdspMIBEnableCardStatusNotification_Type()
)
cdspMIBEnableCardStatusNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspMIBEnableCardStatusNotification.setStatus("current")


class _CdspEnableOperStateNotification_Type(TruthValue):
    """Custom type cdspEnableOperStateNotification based on TruthValue"""


_CdspEnableOperStateNotification_Object = MibScalar
cdspEnableOperStateNotification = _CdspEnableOperStateNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 3, 2),
    _CdspEnableOperStateNotification_Type()
)
cdspEnableOperStateNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspEnableOperStateNotification.setStatus("current")
_CdspVideoUsageNotificationEnable_Type = TruthValue
_CdspVideoUsageNotificationEnable_Object = MibScalar
cdspVideoUsageNotificationEnable = _CdspVideoUsageNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 3, 3),
    _CdspVideoUsageNotificationEnable_Type()
)
cdspVideoUsageNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspVideoUsageNotificationEnable.setStatus("current")
_CdspVideoOutOfResourceNotificationEnable_Type = TruthValue
_CdspVideoOutOfResourceNotificationEnable_Object = MibScalar
cdspVideoOutOfResourceNotificationEnable = _CdspVideoOutOfResourceNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 3, 4),
    _CdspVideoOutOfResourceNotificationEnable_Type()
)
cdspVideoOutOfResourceNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspVideoOutOfResourceNotificationEnable.setStatus("current")
_CdspVoiceObjects_ObjectIdentity = ObjectIdentity
cdspVoiceObjects = _CdspVoiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4)
)
_CdspVoiceParamTable_Object = MibTable
cdspVoiceParamTable = _CdspVoiceParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdspVoiceParamTable.setStatus("current")
_CdspVoiceParamEntry_Object = MibTableRow
cdspVoiceParamEntry = _CdspVoiceParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1)
)
cdspVoiceParamEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cdspVoiceParamEntry.setStatus("current")


class _CdspRtpSidPayloadType_Type(Integer32):
    """Custom type cdspRtpSidPayloadType based on Integer32"""
    defaultValue = 13

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              19)
        )
    )
    namedValues = NamedValues(
        *(("decimal", 13),
          ("hexadecimal", 19))
    )


_CdspRtpSidPayloadType_Type.__name__ = "Integer32"
_CdspRtpSidPayloadType_Object = MibTableColumn
cdspRtpSidPayloadType = _CdspRtpSidPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 1),
    _CdspRtpSidPayloadType_Type()
)
cdspRtpSidPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtpSidPayloadType.setStatus("current")


class _CdspRtcpControl_Type(TruthValue):
    """Custom type cdspRtcpControl based on TruthValue"""


_CdspRtcpControl_Object = MibTableColumn
cdspRtcpControl = _CdspRtcpControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 2),
    _CdspRtcpControl_Type()
)
cdspRtcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpControl.setStatus("current")


class _CdspRtcpTransInterval_Type(Unsigned32):
    """Custom type cdspRtcpTransInterval based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 65535),
    )


_CdspRtcpTransInterval_Type.__name__ = "Unsigned32"
_CdspRtcpTransInterval_Object = MibTableColumn
cdspRtcpTransInterval = _CdspRtcpTransInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 3),
    _CdspRtcpTransInterval_Type()
)
cdspRtcpTransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpTransInterval.setStatus("current")
if mibBuilder.loadTexts:
    cdspRtcpTransInterval.setUnits("milliseconds")


class _CdspRtcpRecvMultiplier_Type(Unsigned32):
    """Custom type cdspRtcpRecvMultiplier based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CdspRtcpRecvMultiplier_Type.__name__ = "Unsigned32"
_CdspRtcpRecvMultiplier_Object = MibTableColumn
cdspRtcpRecvMultiplier = _CdspRtcpRecvMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 4),
    _CdspRtcpRecvMultiplier_Type()
)
cdspRtcpRecvMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpRecvMultiplier.setStatus("current")


class _CdspVadAdaptive_Type(TruthValue):
    """Custom type cdspVadAdaptive based on TruthValue"""


_CdspVadAdaptive_Object = MibTableColumn
cdspVadAdaptive = _CdspVadAdaptive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 5),
    _CdspVadAdaptive_Type()
)
cdspVadAdaptive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspVadAdaptive.setStatus("current")


class _CdspDtmfPowerLevel_Type(Integer32):
    """Custom type cdspDtmfPowerLevel based on Integer32"""
    defaultValue = -120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-250, 30),
    )


_CdspDtmfPowerLevel_Type.__name__ = "Integer32"
_CdspDtmfPowerLevel_Object = MibTableColumn
cdspDtmfPowerLevel = _CdspDtmfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 6),
    _CdspDtmfPowerLevel_Type()
)
cdspDtmfPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspDtmfPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    cdspDtmfPowerLevel.setUnits("0.1 dBm")


class _CdspDtmfPowerTwist_Type(Integer32):
    """Custom type cdspDtmfPowerTwist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_CdspDtmfPowerTwist_Type.__name__ = "Integer32"
_CdspDtmfPowerTwist_Object = MibTableColumn
cdspDtmfPowerTwist = _CdspDtmfPowerTwist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 7),
    _CdspDtmfPowerTwist_Type()
)
cdspDtmfPowerTwist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspDtmfPowerTwist.setStatus("current")
if mibBuilder.loadTexts:
    cdspDtmfPowerTwist.setUnits("0.1 dB")


class _CdspRtcpTimerControl_Type(Integer32):
    """Custom type cdspRtcpTimerControl based on Integer32"""
    defaultValue = 4

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
        *(("disabled", 1),
          ("startImmediately", 2),
          ("startRtcpPktRcvd", 4),
          ("startRtpOrRtcpPktRcvd", 3))
    )


_CdspRtcpTimerControl_Type.__name__ = "Integer32"
_CdspRtcpTimerControl_Object = MibTableColumn
cdspRtcpTimerControl = _CdspRtcpTimerControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 8),
    _CdspRtcpTimerControl_Type()
)
cdspRtcpTimerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpTimerControl.setStatus("current")


class _CdspVqmControl_Type(Integer32):
    """Custom type cdspVqmControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("rfc3611Vqm", 2),
          ("xnq", 3))
    )


_CdspVqmControl_Type.__name__ = "Integer32"
_CdspVqmControl_Object = MibTableColumn
cdspVqmControl = _CdspVqmControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 9),
    _CdspVqmControl_Type()
)
cdspVqmControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspVqmControl.setStatus("current")


class _CdspRtcpXrControl_Type(TruthValue):
    """Custom type cdspRtcpXrControl based on TruthValue"""


_CdspRtcpXrControl_Object = MibTableColumn
cdspRtcpXrControl = _CdspRtcpXrControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 10),
    _CdspRtcpXrControl_Type()
)
cdspRtcpXrControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpXrControl.setStatus("current")


class _CdspRtcpXrTransMultiplier_Type(Unsigned32):
    """Custom type cdspRtcpXrTransMultiplier based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CdspRtcpXrTransMultiplier_Type.__name__ = "Unsigned32"
_CdspRtcpXrTransMultiplier_Object = MibTableColumn
cdspRtcpXrTransMultiplier = _CdspRtcpXrTransMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 11),
    _CdspRtcpXrTransMultiplier_Type()
)
cdspRtcpXrTransMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpXrTransMultiplier.setStatus("current")


class _CdspRtcpXrGminDefault_Type(Unsigned32):
    """Custom type cdspRtcpXrGminDefault based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CdspRtcpXrGminDefault_Type.__name__ = "Unsigned32"
_CdspRtcpXrGminDefault_Object = MibTableColumn
cdspRtcpXrGminDefault = _CdspRtcpXrGminDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 12),
    _CdspRtcpXrGminDefault_Type()
)
cdspRtcpXrGminDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpXrGminDefault.setStatus("current")


class _CdspRtcpXrExtRfactor_Type(Unsigned32):
    """Custom type cdspRtcpXrExtRfactor based on Unsigned32"""
    defaultValue = 127

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CdspRtcpXrExtRfactor_Type.__name__ = "Unsigned32"
_CdspRtcpXrExtRfactor_Object = MibTableColumn
cdspRtcpXrExtRfactor = _CdspRtcpXrExtRfactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 13),
    _CdspRtcpXrExtRfactor_Type()
)
cdspRtcpXrExtRfactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspRtcpXrExtRfactor.setStatus("current")


class _CdspPktLossConcealment_Type(Integer32):
    """Custom type cdspPktLossConcealment based on Integer32"""
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
        *(("g711A1", 3),
          ("none", 1),
          ("simple", 2))
    )


_CdspPktLossConcealment_Type.__name__ = "Integer32"
_CdspPktLossConcealment_Object = MibTableColumn
cdspPktLossConcealment = _CdspPktLossConcealment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 14),
    _CdspPktLossConcealment_Type()
)
cdspPktLossConcealment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspPktLossConcealment.setStatus("current")


class _CdspVqmThreshSES_Type(Unsigned32):
    """Custom type cdspVqmThreshSES based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_CdspVqmThreshSES_Type.__name__ = "Unsigned32"
_CdspVqmThreshSES_Object = MibTableColumn
cdspVqmThreshSES = _CdspVqmThreshSES_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 15),
    _CdspVqmThreshSES_Type()
)
cdspVqmThreshSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspVqmThreshSES.setStatus("current")
if mibBuilder.loadTexts:
    cdspVqmThreshSES.setUnits("milliseconds")


class _CdspTransparentIpIp_Type(TruthValue):
    """Custom type cdspTransparentIpIp based on TruthValue"""


_CdspTransparentIpIp_Object = MibTableColumn
cdspTransparentIpIp = _CdspTransparentIpIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 16),
    _CdspTransparentIpIp_Type()
)
cdspTransparentIpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspTransparentIpIp.setStatus("deprecated")


class _CdspVoiceModeIpIp_Type(Integer32):
    """Custom type cdspVoiceModeIpIp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fastRoute", 2),
          ("normal", 1),
          ("transparent", 3))
    )


_CdspVoiceModeIpIp_Type.__name__ = "Integer32"
_CdspVoiceModeIpIp_Object = MibTableColumn
cdspVoiceModeIpIp = _CdspVoiceModeIpIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 4, 1, 1, 17),
    _CdspVoiceModeIpIp_Type()
)
cdspVoiceModeIpIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspVoiceModeIpIp.setStatus("current")
_CdspUtilObjects_ObjectIdentity = ObjectIdentity
cdspUtilObjects = _CdspUtilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 5)
)
_CdspUtilTable_Object = MibTable
cdspUtilTable = _CdspUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cdspUtilTable.setStatus("current")
_CdspUtilEntry_Object = MibTableRow
cdspUtilEntry = _CdspUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 5, 1, 1)
)
cdspUtilEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-DSP-MGMT-MIB", "cdspCodecPoolIndex"),
)
if mibBuilder.loadTexts:
    cdspUtilEntry.setStatus("current")


class _CdspCodecPoolIndex_Type(Unsigned32):
    """Custom type cdspCodecPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CdspCodecPoolIndex_Type.__name__ = "Unsigned32"
_CdspCodecPoolIndex_Object = MibTableColumn
cdspCodecPoolIndex = _CdspCodecPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 5, 1, 1, 1),
    _CdspCodecPoolIndex_Type()
)
cdspCodecPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdspCodecPoolIndex.setStatus("current")


class _CdspCurrentUtilCap_Type(Unsigned32):
    """Custom type cdspCurrentUtilCap based on Unsigned32"""
    defaultValue = 0


_CdspCurrentUtilCap_Object = MibTableColumn
cdspCurrentUtilCap = _CdspCurrentUtilCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 5, 1, 1, 2),
    _CdspCurrentUtilCap_Type()
)
cdspCurrentUtilCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCurrentUtilCap.setStatus("current")


class _CdspCurrentAvlbCap_Type(Unsigned32):
    """Custom type cdspCurrentAvlbCap based on Unsigned32"""
    defaultValue = 0


_CdspCurrentAvlbCap_Object = MibTableColumn
cdspCurrentAvlbCap = _CdspCurrentAvlbCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 5, 1, 1, 3),
    _CdspCurrentAvlbCap_Type()
)
cdspCurrentAvlbCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspCurrentAvlbCap.setStatus("current")
_CdspDspfarmObjects_ObjectIdentity = ObjectIdentity
cdspDspfarmObjects = _CdspDspfarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6)
)


class _CdspGlobMaxConfTranscodeSess_Type(Unsigned32):
    """Custom type cdspGlobMaxConfTranscodeSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspGlobMaxConfTranscodeSess_Type.__name__ = "Unsigned32"
_CdspGlobMaxConfTranscodeSess_Object = MibScalar
cdspGlobMaxConfTranscodeSess = _CdspGlobMaxConfTranscodeSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 1),
    _CdspGlobMaxConfTranscodeSess_Type()
)
cdspGlobMaxConfTranscodeSess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdspGlobMaxConfTranscodeSess.setStatus("current")


class _CdspGlobMaxAvailTranscodeSess_Type(Unsigned32):
    """Custom type cdspGlobMaxAvailTranscodeSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspGlobMaxAvailTranscodeSess_Type.__name__ = "Unsigned32"
_CdspGlobMaxAvailTranscodeSess_Object = MibScalar
cdspGlobMaxAvailTranscodeSess = _CdspGlobMaxAvailTranscodeSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 2),
    _CdspGlobMaxAvailTranscodeSess_Type()
)
cdspGlobMaxAvailTranscodeSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspGlobMaxAvailTranscodeSess.setStatus("current")
_CdspTranscodeProfileTable_Object = MibTable
cdspTranscodeProfileTable = _CdspTranscodeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cdspTranscodeProfileTable.setStatus("current")
_CdspTranscodeProfileEntry_Object = MibTableRow
cdspTranscodeProfileEntry = _CdspTranscodeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 3, 1)
)
cdspTranscodeProfileEntry.setIndexNames(
    (0, "CISCO-DSP-MGMT-MIB", "cdspTranscodeProfileId"),
)
if mibBuilder.loadTexts:
    cdspTranscodeProfileEntry.setStatus("current")


class _CdspTranscodeProfileId_Type(Unsigned32):
    """Custom type cdspTranscodeProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdspTranscodeProfileId_Type.__name__ = "Unsigned32"
_CdspTranscodeProfileId_Object = MibTableColumn
cdspTranscodeProfileId = _CdspTranscodeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 3, 1, 1),
    _CdspTranscodeProfileId_Type()
)
cdspTranscodeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdspTranscodeProfileId.setStatus("current")


class _CdspTranscodeProfileMaxConfSess_Type(Unsigned32):
    """Custom type cdspTranscodeProfileMaxConfSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspTranscodeProfileMaxConfSess_Type.__name__ = "Unsigned32"
_CdspTranscodeProfileMaxConfSess_Object = MibTableColumn
cdspTranscodeProfileMaxConfSess = _CdspTranscodeProfileMaxConfSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 3, 1, 2),
    _CdspTranscodeProfileMaxConfSess_Type()
)
cdspTranscodeProfileMaxConfSess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdspTranscodeProfileMaxConfSess.setStatus("current")


class _CdspTranscodeProfileMaxAvailSess_Type(Unsigned32):
    """Custom type cdspTranscodeProfileMaxAvailSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspTranscodeProfileMaxAvailSess_Type.__name__ = "Unsigned32"
_CdspTranscodeProfileMaxAvailSess_Object = MibTableColumn
cdspTranscodeProfileMaxAvailSess = _CdspTranscodeProfileMaxAvailSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 3, 1, 3),
    _CdspTranscodeProfileMaxAvailSess_Type()
)
cdspTranscodeProfileMaxAvailSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspTranscodeProfileMaxAvailSess.setStatus("current")
_CdspTranscodeProfileRowStatus_Type = RowStatus
_CdspTranscodeProfileRowStatus_Object = MibTableColumn
cdspTranscodeProfileRowStatus = _CdspTranscodeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 3, 1, 4),
    _CdspTranscodeProfileRowStatus_Type()
)
cdspTranscodeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdspTranscodeProfileRowStatus.setStatus("current")
_CdspMtpProfileTable_Object = MibTable
cdspMtpProfileTable = _CdspMtpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 4)
)
if mibBuilder.loadTexts:
    cdspMtpProfileTable.setStatus("current")
_CdspMtpProfileEntry_Object = MibTableRow
cdspMtpProfileEntry = _CdspMtpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 4, 1)
)
cdspMtpProfileEntry.setIndexNames(
    (0, "CISCO-DSP-MGMT-MIB", "cdspMtpProfileId"),
)
if mibBuilder.loadTexts:
    cdspMtpProfileEntry.setStatus("current")


class _CdspMtpProfileId_Type(Unsigned32):
    """Custom type cdspMtpProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CdspMtpProfileId_Type.__name__ = "Unsigned32"
_CdspMtpProfileId_Object = MibTableColumn
cdspMtpProfileId = _CdspMtpProfileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 4, 1, 1),
    _CdspMtpProfileId_Type()
)
cdspMtpProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdspMtpProfileId.setStatus("current")


class _CdspMtpProfileMaxConfSoftSess_Type(Unsigned32):
    """Custom type cdspMtpProfileMaxConfSoftSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspMtpProfileMaxConfSoftSess_Type.__name__ = "Unsigned32"
_CdspMtpProfileMaxConfSoftSess_Object = MibTableColumn
cdspMtpProfileMaxConfSoftSess = _CdspMtpProfileMaxConfSoftSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 4, 1, 2),
    _CdspMtpProfileMaxConfSoftSess_Type()
)
cdspMtpProfileMaxConfSoftSess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdspMtpProfileMaxConfSoftSess.setStatus("current")


class _CdspMtpProfileMaxConfHardSess_Type(Unsigned32):
    """Custom type cdspMtpProfileMaxConfHardSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspMtpProfileMaxConfHardSess_Type.__name__ = "Unsigned32"
_CdspMtpProfileMaxConfHardSess_Object = MibTableColumn
cdspMtpProfileMaxConfHardSess = _CdspMtpProfileMaxConfHardSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 4, 1, 3),
    _CdspMtpProfileMaxConfHardSess_Type()
)
cdspMtpProfileMaxConfHardSess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdspMtpProfileMaxConfHardSess.setStatus("current")


class _CdspMtpProfileMaxAvailHardSess_Type(Unsigned32):
    """Custom type cdspMtpProfileMaxAvailHardSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspMtpProfileMaxAvailHardSess_Type.__name__ = "Unsigned32"
_CdspMtpProfileMaxAvailHardSess_Object = MibTableColumn
cdspMtpProfileMaxAvailHardSess = _CdspMtpProfileMaxAvailHardSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 4, 1, 4),
    _CdspMtpProfileMaxAvailHardSess_Type()
)
cdspMtpProfileMaxAvailHardSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspMtpProfileMaxAvailHardSess.setStatus("current")
_CdspMtpProfileRowStatus_Type = RowStatus
_CdspMtpProfileRowStatus_Object = MibTableColumn
cdspMtpProfileRowStatus = _CdspMtpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 6, 4, 1, 5),
    _CdspMtpProfileRowStatus_Type()
)
cdspMtpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdspMtpProfileRowStatus.setStatus("current")
_CdspDspfarmUtilObjects_ObjectIdentity = ObjectIdentity
cdspDspfarmUtilObjects = _CdspDspfarmUtilObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 7)
)


class _CdspTotAvailTranscodeSess_Type(Unsigned32):
    """Custom type cdspTotAvailTranscodeSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspTotAvailTranscodeSess_Type.__name__ = "Unsigned32"
_CdspTotAvailTranscodeSess_Object = MibScalar
cdspTotAvailTranscodeSess = _CdspTotAvailTranscodeSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 7, 1),
    _CdspTotAvailTranscodeSess_Type()
)
cdspTotAvailTranscodeSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspTotAvailTranscodeSess.setStatus("current")


class _CdspTotUnusedTranscodeSess_Type(Unsigned32):
    """Custom type cdspTotUnusedTranscodeSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspTotUnusedTranscodeSess_Type.__name__ = "Unsigned32"
_CdspTotUnusedTranscodeSess_Object = MibScalar
cdspTotUnusedTranscodeSess = _CdspTotUnusedTranscodeSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 7, 2),
    _CdspTotUnusedTranscodeSess_Type()
)
cdspTotUnusedTranscodeSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspTotUnusedTranscodeSess.setStatus("current")


class _CdspTotAvailMtpSess_Type(Unsigned32):
    """Custom type cdspTotAvailMtpSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspTotAvailMtpSess_Type.__name__ = "Unsigned32"
_CdspTotAvailMtpSess_Object = MibScalar
cdspTotAvailMtpSess = _CdspTotAvailMtpSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 7, 3),
    _CdspTotAvailMtpSess_Type()
)
cdspTotAvailMtpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspTotAvailMtpSess.setStatus("current")


class _CdspTotUnusedMtpSess_Type(Unsigned32):
    """Custom type cdspTotUnusedMtpSess based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdspTotUnusedMtpSess_Type.__name__ = "Unsigned32"
_CdspTotUnusedMtpSess_Object = MibScalar
cdspTotUnusedMtpSess = _CdspTotUnusedMtpSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 1, 7, 4),
    _CdspTotUnusedMtpSess_Type()
)
cdspTotUnusedMtpSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdspTotUnusedMtpSess.setStatus("current")
_CdspMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cdspMIBNotificationPrefix = _CdspMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 2)
)
_CdspMIBNotifications_ObjectIdentity = ObjectIdentity
cdspMIBNotifications = _CdspMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 2, 0)
)
_CdspMgmtConformance_ObjectIdentity = ObjectIdentity
cdspMgmtConformance = _CdspMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3)
)
_CdspMgmtCompliances_ObjectIdentity = ObjectIdentity
cdspMgmtCompliances = _CdspMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1)
)
_CdspMgmtGroups_ObjectIdentity = ObjectIdentity
cdspMgmtGroups = _CdspMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2)
)
cdspStatusEntry.registerAugmentions(
    ("CISCO-DSP-MGMT-MIB",
     "cdspStatusXEntry")
)
cdspStatusXEntry.setIndexNames(*cdspStatusEntry.getIndexNames())

# Managed Objects groups

cdspMgmtGeneralInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 1)
)
cdspMgmtGeneralInfoGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspCardIndex"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardState"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardResourceUtilization"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardLastHiWaterUtilization"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardLastResetTime"),
        ("CISCO-DSP-MGMT-MIB", "cdspOperState"),
        ("CISCO-DSP-MGMT-MIB", "cdspAlarms"),
        ("CISCO-DSP-MGMT-MIB", "cdspLastAlarmCause"),
        ("CISCO-DSP-MGMT-MIB", "cdspLastAlarmCauseText"),
        ("CISCO-DSP-MGMT-MIB", "cdspLastAlarmTime"),
        ("CISCO-DSP-MGMT-MIB", "cdspMIBEnableCardStatusNotification"))
)
if mibBuilder.loadTexts:
    cdspMgmtGeneralInfoGroup.setStatus("deprecated")

cdspChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 2)
)
cdspChannelGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspCardMaxChanPerDSP"),
        ("CISCO-DSP-MGMT-MIB", "cdspTotalChannels"),
        ("CISCO-DSP-MGMT-MIB", "cdspInUseChannels"),
        ("CISCO-DSP-MGMT-MIB", "cdspActiveChannels"))
)
if mibBuilder.loadTexts:
    cdspChannelGroup.setStatus("current")

cdspMgmtExtGeneralInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 3)
)
cdspMgmtExtGeneralInfoGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspTotalDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspFailedDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspCongestedDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspNormalDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspDspSwitchOverThreshold"),
        ("CISCO-DSP-MGMT-MIB", "cdspNx64Dsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspDspNum"))
)
if mibBuilder.loadTexts:
    cdspMgmtExtGeneralInfoGroup.setStatus("deprecated")

cdspVoiceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 4)
)
cdspVoiceInfoGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspRtpSidPayloadType"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpControl"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpTransInterval"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpRecvMultiplier"),
        ("CISCO-DSP-MGMT-MIB", "cdspVadAdaptive"),
        ("CISCO-DSP-MGMT-MIB", "cdspDtmfPowerLevel"),
        ("CISCO-DSP-MGMT-MIB", "cdspDtmfPowerTwist"))
)
if mibBuilder.loadTexts:
    cdspVoiceInfoGroup.setStatus("deprecated")

cdspChannelExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 6)
)
cdspChannelExtGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspSigBearerChannelSplit"),
        ("CISCO-DSP-MGMT-MIB", "cdspNumCongestionOccurrence"),
        ("CISCO-DSP-MGMT-MIB", "cdspXNumberOfBearerCalls"),
        ("CISCO-DSP-MGMT-MIB", "cdspXNumberOfSigCalls"),
        ("CISCO-DSP-MGMT-MIB", "cdspXAvailableBearerBandwidth"),
        ("CISCO-DSP-MGMT-MIB", "cdspXAvailableSigBandwidth"))
)
if mibBuilder.loadTexts:
    cdspChannelExtGroup.setStatus("current")

cdspVoiceInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 7)
)
cdspVoiceInfoGroupRev1.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspRtpSidPayloadType"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpControl"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpTransInterval"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpRecvMultiplier"),
        ("CISCO-DSP-MGMT-MIB", "cdspVadAdaptive"),
        ("CISCO-DSP-MGMT-MIB", "cdspDtmfPowerLevel"),
        ("CISCO-DSP-MGMT-MIB", "cdspDtmfPowerTwist"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpTimerControl"))
)
if mibBuilder.loadTexts:
    cdspVoiceInfoGroupRev1.setStatus("deprecated")

cdspMgmtExtGeneralInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 8)
)
cdspMgmtExtGeneralInfoGroupRev1.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspTotalDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspFailedDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspCongestedDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspNormalDsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspDspSwitchOverThreshold"),
        ("CISCO-DSP-MGMT-MIB", "cdspNx64Dsp"),
        ("CISCO-DSP-MGMT-MIB", "cdspDspNum"),
        ("CISCO-DSP-MGMT-MIB", "cdspCodecTemplateSupported"))
)
if mibBuilder.loadTexts:
    cdspMgmtExtGeneralInfoGroupRev1.setStatus("current")

cdspMgmtGeneralInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 9)
)
cdspMgmtGeneralInfoGroupRev1.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspCardIndex"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardState"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardResourceUtilization"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardLastHiWaterUtilization"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardLastResetTime"),
        ("CISCO-DSP-MGMT-MIB", "cdspOperState"),
        ("CISCO-DSP-MGMT-MIB", "cdspAlarms"),
        ("CISCO-DSP-MGMT-MIB", "cdspLastAlarmCause"),
        ("CISCO-DSP-MGMT-MIB", "cdspLastAlarmCauseText"),
        ("CISCO-DSP-MGMT-MIB", "cdspLastAlarmTime"),
        ("CISCO-DSP-MGMT-MIB", "cdspMIBEnableCardStatusNotification"),
        ("CISCO-DSP-MGMT-MIB", "cdspEnableOperStateNotification"))
)
if mibBuilder.loadTexts:
    cdspMgmtGeneralInfoGroupRev1.setStatus("current")

cdspVQMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 11)
)
cdspVQMGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspVqmControl"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpXrControl"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpXrTransMultiplier"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpXrGminDefault"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpXrExtRfactor"),
        ("CISCO-DSP-MGMT-MIB", "cdspVqmThreshSES"))
)
if mibBuilder.loadTexts:
    cdspVQMGroup.setStatus("current")

cdspVoiceInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 12)
)
cdspVoiceInfoGroupRev2.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspRtpSidPayloadType"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpControl"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpTransInterval"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpRecvMultiplier"),
        ("CISCO-DSP-MGMT-MIB", "cdspVadAdaptive"),
        ("CISCO-DSP-MGMT-MIB", "cdspDtmfPowerLevel"),
        ("CISCO-DSP-MGMT-MIB", "cdspDtmfPowerTwist"),
        ("CISCO-DSP-MGMT-MIB", "cdspRtcpTimerControl"),
        ("CISCO-DSP-MGMT-MIB", "cdspPktLossConcealment"))
)
if mibBuilder.loadTexts:
    cdspVoiceInfoGroupRev2.setStatus("current")

cdspTransCodingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 13)
)
cdspTransCodingGroup.setObjects(
    ("CISCO-DSP-MGMT-MIB", "cdspTransparentIpIp")
)
if mibBuilder.loadTexts:
    cdspTransCodingGroup.setStatus("deprecated")

cdspTransCodingGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 14)
)
cdspTransCodingGroup1.setObjects(
    ("CISCO-DSP-MGMT-MIB", "cdspVoiceModeIpIp")
)
if mibBuilder.loadTexts:
    cdspTransCodingGroup1.setStatus("current")

cdspUtilInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 15)
)
cdspUtilInfoGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspCurrentUtilCap"),
        ("CISCO-DSP-MGMT-MIB", "cdspCurrentAvlbCap"))
)
if mibBuilder.loadTexts:
    cdspUtilInfoGroup.setStatus("current")

cdspDspfarmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 16)
)
cdspDspfarmInfoGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspGlobMaxConfTranscodeSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspGlobMaxAvailTranscodeSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspTranscodeProfileRowStatus"),
        ("CISCO-DSP-MGMT-MIB", "cdspTranscodeProfileMaxConfSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspTranscodeProfileMaxAvailSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspMtpProfileRowStatus"),
        ("CISCO-DSP-MGMT-MIB", "cdspMtpProfileMaxConfSoftSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspMtpProfileMaxConfHardSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspMtpProfileMaxAvailHardSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspTotAvailTranscodeSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspTotUnusedTranscodeSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspTotAvailMtpSess"),
        ("CISCO-DSP-MGMT-MIB", "cdspTotUnusedMtpSess"))
)
if mibBuilder.loadTexts:
    cdspDspfarmInfoGroup.setStatus("current")

cdspMgmtVideoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 18)
)
cdspMgmtVideoInfoGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspCardVideoPoolUtilization"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardVideoPoolUtilizationThreshold"),
        ("CISCO-DSP-MGMT-MIB", "cdspVideoUsageNotificationEnable"),
        ("CISCO-DSP-MGMT-MIB", "cdspVideoOutOfResourceNotificationEnable"))
)
if mibBuilder.loadTexts:
    cdspMgmtVideoInfoGroup.setStatus("current")


# Notification objects

cdspMIBCardStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 2, 0, 1)
)
cdspMIBCardStateNotification.setObjects(
    ("CISCO-DSP-MGMT-MIB", "cdspCardState")
)
if mibBuilder.loadTexts:
    cdspMIBCardStateNotification.setStatus(
        "current"
    )

cdspOperStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 2, 0, 2)
)
cdspOperStateNotification.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspOperState"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    cdspOperStateNotification.setStatus(
        "current"
    )

cdspVideoUsageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 2, 0, 3)
)
cdspVideoUsageNotification.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspCardVideoPoolUtilization"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardVideoPoolUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    cdspVideoUsageNotification.setStatus(
        "current"
    )

cdspVideoOutOfResourceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 2, 0, 4)
)
cdspVideoOutOfResourceNotification.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspCardVideoPoolUtilization"),
        ("CISCO-DSP-MGMT-MIB", "cdspCardVideoPoolUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    cdspVideoOutOfResourceNotification.setStatus(
        "current"
    )


# Notifications groups

cdspMgmtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 5)
)
cdspMgmtNotificationsGroup.setObjects(
    ("CISCO-DSP-MGMT-MIB", "cdspMIBCardStateNotification")
)
if mibBuilder.loadTexts:
    cdspMgmtNotificationsGroup.setStatus(
        "deprecated"
    )

cdspMgmtNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 10)
)
cdspMgmtNotificationsGroupRev1.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspMIBCardStateNotification"),
        ("CISCO-DSP-MGMT-MIB", "cdspOperStateNotification"))
)
if mibBuilder.loadTexts:
    cdspMgmtNotificationsGroupRev1.setStatus(
        "current"
    )

cdspMgmtVideoNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 2, 17)
)
cdspMgmtVideoNotificationsGroup.setObjects(
      *(("CISCO-DSP-MGMT-MIB", "cdspVideoUsageNotification"),
        ("CISCO-DSP-MGMT-MIB", "cdspVideoOutOfResourceNotification"))
)
if mibBuilder.loadTexts:
    cdspMgmtVideoNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cdspMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cdspMgmtCompliance.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev1.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev2.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev3.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev4.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev5.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev6.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev7.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev8.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev9.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev10.setStatus(
        "deprecated"
    )

cdspMgmtComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 86, 3, 1, 12)
)
if mibBuilder.loadTexts:
    cdspMgmtComplianceRev11.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DSP-MGMT-MIB",
    **{"ciscoDspMgmtMIB": ciscoDspMgmtMIB,
       "cdspMgmtNotifications": cdspMgmtNotifications,
       "cdspMgmtObjects": cdspMgmtObjects,
       "cdspCardObjects": cdspCardObjects,
       "cdspCardStatusTable": cdspCardStatusTable,
       "cdspCardStatusEntry": cdspCardStatusEntry,
       "cdspCardIndex": cdspCardIndex,
       "cdspCardState": cdspCardState,
       "cdspCardResourceUtilization": cdspCardResourceUtilization,
       "cdspCardLastHiWaterUtilization": cdspCardLastHiWaterUtilization,
       "cdspCardLastResetTime": cdspCardLastResetTime,
       "cdspCardMaxChanPerDSP": cdspCardMaxChanPerDSP,
       "cdspTotalDsp": cdspTotalDsp,
       "cdspFailedDsp": cdspFailedDsp,
       "cdspDspSwitchOverThreshold": cdspDspSwitchOverThreshold,
       "cdspCongestedDsp": cdspCongestedDsp,
       "cdspNormalDsp": cdspNormalDsp,
       "cdspNx64Dsp": cdspNx64Dsp,
       "cdspCodecTemplateSupported": cdspCodecTemplateSupported,
       "cdspCardVideoPoolUtilization": cdspCardVideoPoolUtilization,
       "cdspCardVideoPoolUtilizationThreshold": cdspCardVideoPoolUtilizationThreshold,
       "cdspObjects": cdspObjects,
       "cdspStatusTable": cdspStatusTable,
       "cdspStatusEntry": cdspStatusEntry,
       "cdspOperState": cdspOperState,
       "cdspAlarms": cdspAlarms,
       "cdspLastAlarmCause": cdspLastAlarmCause,
       "cdspLastAlarmCauseText": cdspLastAlarmCauseText,
       "cdspLastAlarmTime": cdspLastAlarmTime,
       "cdspTotalChannels": cdspTotalChannels,
       "cdspInUseChannels": cdspInUseChannels,
       "cdspActiveChannels": cdspActiveChannels,
       "cdspSigBearerChannelSplit": cdspSigBearerChannelSplit,
       "cdspNumCongestionOccurrence": cdspNumCongestionOccurrence,
       "cdspDspNum": cdspDspNum,
       "cdspStatusXTable": cdspStatusXTable,
       "cdspStatusXEntry": cdspStatusXEntry,
       "cdspXNumberOfBearerCalls": cdspXNumberOfBearerCalls,
       "cdspXNumberOfSigCalls": cdspXNumberOfSigCalls,
       "cdspXAvailableBearerBandwidth": cdspXAvailableBearerBandwidth,
       "cdspXAvailableSigBandwidth": cdspXAvailableSigBandwidth,
       "cdspMIBNotificationEnables": cdspMIBNotificationEnables,
       "cdspMIBEnableCardStatusNotification": cdspMIBEnableCardStatusNotification,
       "cdspEnableOperStateNotification": cdspEnableOperStateNotification,
       "cdspVideoUsageNotificationEnable": cdspVideoUsageNotificationEnable,
       "cdspVideoOutOfResourceNotificationEnable": cdspVideoOutOfResourceNotificationEnable,
       "cdspVoiceObjects": cdspVoiceObjects,
       "cdspVoiceParamTable": cdspVoiceParamTable,
       "cdspVoiceParamEntry": cdspVoiceParamEntry,
       "cdspRtpSidPayloadType": cdspRtpSidPayloadType,
       "cdspRtcpControl": cdspRtcpControl,
       "cdspRtcpTransInterval": cdspRtcpTransInterval,
       "cdspRtcpRecvMultiplier": cdspRtcpRecvMultiplier,
       "cdspVadAdaptive": cdspVadAdaptive,
       "cdspDtmfPowerLevel": cdspDtmfPowerLevel,
       "cdspDtmfPowerTwist": cdspDtmfPowerTwist,
       "cdspRtcpTimerControl": cdspRtcpTimerControl,
       "cdspVqmControl": cdspVqmControl,
       "cdspRtcpXrControl": cdspRtcpXrControl,
       "cdspRtcpXrTransMultiplier": cdspRtcpXrTransMultiplier,
       "cdspRtcpXrGminDefault": cdspRtcpXrGminDefault,
       "cdspRtcpXrExtRfactor": cdspRtcpXrExtRfactor,
       "cdspPktLossConcealment": cdspPktLossConcealment,
       "cdspVqmThreshSES": cdspVqmThreshSES,
       "cdspTransparentIpIp": cdspTransparentIpIp,
       "cdspVoiceModeIpIp": cdspVoiceModeIpIp,
       "cdspUtilObjects": cdspUtilObjects,
       "cdspUtilTable": cdspUtilTable,
       "cdspUtilEntry": cdspUtilEntry,
       "cdspCodecPoolIndex": cdspCodecPoolIndex,
       "cdspCurrentUtilCap": cdspCurrentUtilCap,
       "cdspCurrentAvlbCap": cdspCurrentAvlbCap,
       "cdspDspfarmObjects": cdspDspfarmObjects,
       "cdspGlobMaxConfTranscodeSess": cdspGlobMaxConfTranscodeSess,
       "cdspGlobMaxAvailTranscodeSess": cdspGlobMaxAvailTranscodeSess,
       "cdspTranscodeProfileTable": cdspTranscodeProfileTable,
       "cdspTranscodeProfileEntry": cdspTranscodeProfileEntry,
       "cdspTranscodeProfileId": cdspTranscodeProfileId,
       "cdspTranscodeProfileMaxConfSess": cdspTranscodeProfileMaxConfSess,
       "cdspTranscodeProfileMaxAvailSess": cdspTranscodeProfileMaxAvailSess,
       "cdspTranscodeProfileRowStatus": cdspTranscodeProfileRowStatus,
       "cdspMtpProfileTable": cdspMtpProfileTable,
       "cdspMtpProfileEntry": cdspMtpProfileEntry,
       "cdspMtpProfileId": cdspMtpProfileId,
       "cdspMtpProfileMaxConfSoftSess": cdspMtpProfileMaxConfSoftSess,
       "cdspMtpProfileMaxConfHardSess": cdspMtpProfileMaxConfHardSess,
       "cdspMtpProfileMaxAvailHardSess": cdspMtpProfileMaxAvailHardSess,
       "cdspMtpProfileRowStatus": cdspMtpProfileRowStatus,
       "cdspDspfarmUtilObjects": cdspDspfarmUtilObjects,
       "cdspTotAvailTranscodeSess": cdspTotAvailTranscodeSess,
       "cdspTotUnusedTranscodeSess": cdspTotUnusedTranscodeSess,
       "cdspTotAvailMtpSess": cdspTotAvailMtpSess,
       "cdspTotUnusedMtpSess": cdspTotUnusedMtpSess,
       "cdspMIBNotificationPrefix": cdspMIBNotificationPrefix,
       "cdspMIBNotifications": cdspMIBNotifications,
       "cdspMIBCardStateNotification": cdspMIBCardStateNotification,
       "cdspOperStateNotification": cdspOperStateNotification,
       "cdspVideoUsageNotification": cdspVideoUsageNotification,
       "cdspVideoOutOfResourceNotification": cdspVideoOutOfResourceNotification,
       "cdspMgmtConformance": cdspMgmtConformance,
       "cdspMgmtCompliances": cdspMgmtCompliances,
       "cdspMgmtCompliance": cdspMgmtCompliance,
       "cdspMgmtComplianceRev1": cdspMgmtComplianceRev1,
       "cdspMgmtComplianceRev2": cdspMgmtComplianceRev2,
       "cdspMgmtComplianceRev3": cdspMgmtComplianceRev3,
       "cdspMgmtComplianceRev4": cdspMgmtComplianceRev4,
       "cdspMgmtComplianceRev5": cdspMgmtComplianceRev5,
       "cdspMgmtComplianceRev6": cdspMgmtComplianceRev6,
       "cdspMgmtComplianceRev7": cdspMgmtComplianceRev7,
       "cdspMgmtComplianceRev8": cdspMgmtComplianceRev8,
       "cdspMgmtComplianceRev9": cdspMgmtComplianceRev9,
       "cdspMgmtComplianceRev10": cdspMgmtComplianceRev10,
       "cdspMgmtComplianceRev11": cdspMgmtComplianceRev11,
       "cdspMgmtGroups": cdspMgmtGroups,
       "cdspMgmtGeneralInfoGroup": cdspMgmtGeneralInfoGroup,
       "cdspChannelGroup": cdspChannelGroup,
       "cdspMgmtExtGeneralInfoGroup": cdspMgmtExtGeneralInfoGroup,
       "cdspVoiceInfoGroup": cdspVoiceInfoGroup,
       "cdspMgmtNotificationsGroup": cdspMgmtNotificationsGroup,
       "cdspChannelExtGroup": cdspChannelExtGroup,
       "cdspVoiceInfoGroupRev1": cdspVoiceInfoGroupRev1,
       "cdspMgmtExtGeneralInfoGroupRev1": cdspMgmtExtGeneralInfoGroupRev1,
       "cdspMgmtGeneralInfoGroupRev1": cdspMgmtGeneralInfoGroupRev1,
       "cdspMgmtNotificationsGroupRev1": cdspMgmtNotificationsGroupRev1,
       "cdspVQMGroup": cdspVQMGroup,
       "cdspVoiceInfoGroupRev2": cdspVoiceInfoGroupRev2,
       "cdspTransCodingGroup": cdspTransCodingGroup,
       "cdspTransCodingGroup1": cdspTransCodingGroup1,
       "cdspUtilInfoGroup": cdspUtilInfoGroup,
       "cdspDspfarmInfoGroup": cdspDspfarmInfoGroup,
       "cdspMgmtVideoNotificationsGroup": cdspMgmtVideoNotificationsGroup,
       "cdspMgmtVideoInfoGroup": cdspMgmtVideoInfoGroup}
)
