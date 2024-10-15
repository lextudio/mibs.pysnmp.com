# SNMP MIB module (ZHNGPONLINK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNGPONLINK
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:59 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")


# MODULE-IDENTITY

zhnGPONLink = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43)
)
zhnGPONLink.setRevisions(
        ("2012-02-03 13:46",
         "2011-01-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class GPONLinkStatusValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class GPONEnabledDisabledStatusValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class GPONStateValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class GPONOnOffAlarmValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_ZhnGPONLinkObjects_ObjectIdentity = ObjectIdentity
zhnGPONLinkObjects = _ZhnGPONLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1)
)
_GponInterfaceNumberOfEntries_Type = Unsigned32
_GponInterfaceNumberOfEntries_Object = MibScalar
gponInterfaceNumberOfEntries = _GponInterfaceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 1),
    _GponInterfaceNumberOfEntries_Type()
)
gponInterfaceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponInterfaceNumberOfEntries.setStatus("current")
_GponLinkStatusTable_Object = MibTable
gponLinkStatusTable = _GponLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2)
)
if mibBuilder.loadTexts:
    gponLinkStatusTable.setStatus("current")
_GponLinkStatusEntry_Object = MibTableRow
gponLinkStatusEntry = _GponLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1)
)
gponLinkStatusEntry.setIndexNames(
    (0, "ZHNGPONLINK", "gponIfIndex"),
)
if mibBuilder.loadTexts:
    gponLinkStatusEntry.setStatus("current")
_GponIfIndex_Type = Unsigned32
_GponIfIndex_Object = MibTableColumn
gponIfIndex = _GponIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 1),
    _GponIfIndex_Type()
)
gponIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gponIfIndex.setStatus("current")
_GponOperStatus_Type = GPONLinkStatusValues
_GponOperStatus_Object = MibTableColumn
gponOperStatus = _GponOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 2),
    _GponOperStatus_Type()
)
gponOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOperStatus.setStatus("current")
_GponLinkUpTransitions_Type = Unsigned32
_GponLinkUpTransitions_Object = MibTableColumn
gponLinkUpTransitions = _GponLinkUpTransitions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 3),
    _GponLinkUpTransitions_Type()
)
gponLinkUpTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponLinkUpTransitions.setStatus("current")
_RfVideo_Type = GPONEnabledDisabledStatusValues
_RfVideo_Object = MibTableColumn
rfVideo = _RfVideo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 4),
    _RfVideo_Type()
)
rfVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfVideo.setStatus("current")
_GponOnuId_Type = Unsigned32
_GponOnuId_Object = MibTableColumn
gponOnuId = _GponOnuId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 5),
    _GponOnuId_Type()
)
gponOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponOnuId.setStatus("current")
_GponState_Type = GPONStateValues
_GponState_Object = MibTableColumn
gponState = _GponState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 6),
    _GponState_Type()
)
gponState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponState.setStatus("current")
_RxLevel_Type = OctetString
_RxLevel_Object = MibTableColumn
rxLevel = _RxLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 7),
    _RxLevel_Type()
)
rxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxLevel.setStatus("current")
_TxPower_Type = OctetString
_TxPower_Object = MibTableColumn
txPower = _TxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 8),
    _TxPower_Type()
)
txPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPower.setStatus("current")
_TxBiasCurrent_Type = OctetString
_TxBiasCurrent_Object = MibTableColumn
txBiasCurrent = _TxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 9),
    _TxBiasCurrent_Type()
)
txBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBiasCurrent.setStatus("current")
_GponTemperature_Type = OctetString
_GponTemperature_Object = MibTableColumn
gponTemperature = _GponTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 10),
    _GponTemperature_Type()
)
gponTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponTemperature.setStatus("current")
_GponVcc_Type = OctetString
_GponVcc_Object = MibTableColumn
gponVcc = _GponVcc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 2, 1, 11),
    _GponVcc_Type()
)
gponVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponVcc.setStatus("current")
_GponAlarmStatusTable_Object = MibTable
gponAlarmStatusTable = _GponAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3)
)
if mibBuilder.loadTexts:
    gponAlarmStatusTable.setStatus("current")
_GponAlarmStatusEntry_Object = MibTableRow
gponAlarmStatusEntry = _GponAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1)
)
gponAlarmStatusEntry.setIndexNames(
    (0, "ZHNGPONLINK", "gponIfIndex"),
)
if mibBuilder.loadTexts:
    gponAlarmStatusEntry.setStatus("current")
_GponAlarmAutoPowerControlFail_Type = GPONOnOffAlarmValues
_GponAlarmAutoPowerControlFail_Object = MibTableColumn
gponAlarmAutoPowerControlFail = _GponAlarmAutoPowerControlFail_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 1),
    _GponAlarmAutoPowerControlFail_Type()
)
gponAlarmAutoPowerControlFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmAutoPowerControlFail.setStatus("current")
_GponAlarmLOS_Type = GPONOnOffAlarmValues
_GponAlarmLOS_Object = MibTableColumn
gponAlarmLOS = _GponAlarmLOS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 2),
    _GponAlarmLOS_Type()
)
gponAlarmLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmLOS.setStatus("current")
_GponAlarmLOL_Type = GPONOnOffAlarmValues
_GponAlarmLOL_Object = MibTableColumn
gponAlarmLOL = _GponAlarmLOL_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 3),
    _GponAlarmLOL_Type()
)
gponAlarmLOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmLOL.setStatus("current")
_GponAlarmLOF_Type = GPONOnOffAlarmValues
_GponAlarmLOF_Object = MibTableColumn
gponAlarmLOF = _GponAlarmLOF_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 4),
    _GponAlarmLOF_Type()
)
gponAlarmLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmLOF.setStatus("current")
_GponAlarmLCDG_Type = GPONOnOffAlarmValues
_GponAlarmLCDG_Object = MibTableColumn
gponAlarmLCDG = _GponAlarmLCDG_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 5),
    _GponAlarmLCDG_Type()
)
gponAlarmLCDG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmLCDG.setStatus("current")
_GponAlarmFailedSignal_Type = GPONOnOffAlarmValues
_GponAlarmFailedSignal_Object = MibTableColumn
gponAlarmFailedSignal = _GponAlarmFailedSignal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 6),
    _GponAlarmFailedSignal_Type()
)
gponAlarmFailedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmFailedSignal.setStatus("current")
_GponAlarmDegradedSignal_Type = GPONOnOffAlarmValues
_GponAlarmDegradedSignal_Object = MibTableColumn
gponAlarmDegradedSignal = _GponAlarmDegradedSignal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 7),
    _GponAlarmDegradedSignal_Type()
)
gponAlarmDegradedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmDegradedSignal.setStatus("current")
_GponAlarmStartupFail_Type = GPONOnOffAlarmValues
_GponAlarmStartupFail_Object = MibTableColumn
gponAlarmStartupFail = _GponAlarmStartupFail_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 8),
    _GponAlarmStartupFail_Type()
)
gponAlarmStartupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmStartupFail.setStatus("current")
_GponAlarmMsgErrorMsg_Type = GPONOnOffAlarmValues
_GponAlarmMsgErrorMsg_Object = MibTableColumn
gponAlarmMsgErrorMsg = _GponAlarmMsgErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 9),
    _GponAlarmMsgErrorMsg_Type()
)
gponAlarmMsgErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmMsgErrorMsg.setStatus("current")
_GponAlarmDeactivateOnuId_Type = GPONOnOffAlarmValues
_GponAlarmDeactivateOnuId_Object = MibTableColumn
gponAlarmDeactivateOnuId = _GponAlarmDeactivateOnuId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 10),
    _GponAlarmDeactivateOnuId_Type()
)
gponAlarmDeactivateOnuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmDeactivateOnuId.setStatus("current")
_GponAlarmDisabledOnu_Type = GPONOnOffAlarmValues
_GponAlarmDisabledOnu_Object = MibTableColumn
gponAlarmDisabledOnu = _GponAlarmDisabledOnu_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 11),
    _GponAlarmDisabledOnu_Type()
)
gponAlarmDisabledOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmDisabledOnu.setStatus("current")
_GponAlarmPEE_Type = GPONOnOffAlarmValues
_GponAlarmPEE_Object = MibTableColumn
gponAlarmPEE = _GponAlarmPEE_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 3, 1, 12),
    _GponAlarmPEE_Type()
)
gponAlarmPEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gponAlarmPEE.setStatus("current")
_GponDataGemStatsTable_Object = MibTable
gponDataGemStatsTable = _GponDataGemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4)
)
if mibBuilder.loadTexts:
    gponDataGemStatsTable.setStatus("current")
_GponDataGemStatsEntry_Object = MibTableRow
gponDataGemStatsEntry = _GponDataGemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1)
)
gponDataGemStatsEntry.setIndexNames(
    (0, "ZHNGPONLINK", "gponIfIndex"),
)
if mibBuilder.loadTexts:
    gponDataGemStatsEntry.setStatus("current")
_DataGemPortRxBytes_Type = Unsigned32
_DataGemPortRxBytes_Object = MibTableColumn
dataGemPortRxBytes = _DataGemPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 1),
    _DataGemPortRxBytes_Type()
)
dataGemPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortRxBytes.setStatus("current")
_DataGemPortRxFragments_Type = Unsigned32
_DataGemPortRxFragments_Object = MibTableColumn
dataGemPortRxFragments = _DataGemPortRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 2),
    _DataGemPortRxFragments_Type()
)
dataGemPortRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortRxFragments.setStatus("current")
_DataGemPortRxFrames_Type = Unsigned32
_DataGemPortRxFrames_Object = MibTableColumn
dataGemPortRxFrames = _DataGemPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 3),
    _DataGemPortRxFrames_Type()
)
dataGemPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortRxFrames.setStatus("current")
_DataGemPortRxDroppedFrames_Type = Unsigned32
_DataGemPortRxDroppedFrames_Object = MibTableColumn
dataGemPortRxDroppedFrames = _DataGemPortRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 4),
    _DataGemPortRxDroppedFrames_Type()
)
dataGemPortRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortRxDroppedFrames.setStatus("current")
_DataGemPortTxBytes_Type = Unsigned32
_DataGemPortTxBytes_Object = MibTableColumn
dataGemPortTxBytes = _DataGemPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 5),
    _DataGemPortTxBytes_Type()
)
dataGemPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortTxBytes.setStatus("current")
_DataGemPortTxFragments_Type = Unsigned32
_DataGemPortTxFragments_Object = MibTableColumn
dataGemPortTxFragments = _DataGemPortTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 6),
    _DataGemPortTxFragments_Type()
)
dataGemPortTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortTxFragments.setStatus("current")
_DataGemPortTxFrames_Type = Unsigned32
_DataGemPortTxFrames_Object = MibTableColumn
dataGemPortTxFrames = _DataGemPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 7),
    _DataGemPortTxFrames_Type()
)
dataGemPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortTxFrames.setStatus("current")
_DataGemPortTxDroppedFrames_Type = Unsigned32
_DataGemPortTxDroppedFrames_Object = MibTableColumn
dataGemPortTxDroppedFrames = _DataGemPortTxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 8),
    _DataGemPortTxDroppedFrames_Type()
)
dataGemPortTxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortTxDroppedFrames.setStatus("current")
_DataGemPortAcceptedMulticastFrames_Type = Unsigned32
_DataGemPortAcceptedMulticastFrames_Object = MibTableColumn
dataGemPortAcceptedMulticastFrames = _DataGemPortAcceptedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 9),
    _DataGemPortAcceptedMulticastFrames_Type()
)
dataGemPortAcceptedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortAcceptedMulticastFrames.setStatus("current")
_DataGemPortDroppedMulticastFrames_Type = Unsigned32
_DataGemPortDroppedMulticastFrames_Object = MibTableColumn
dataGemPortDroppedMulticastFrames = _DataGemPortDroppedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 4, 1, 10),
    _DataGemPortDroppedMulticastFrames_Type()
)
dataGemPortDroppedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataGemPortDroppedMulticastFrames.setStatus("current")
_GponVideoGemStatsTable_Object = MibTable
gponVideoGemStatsTable = _GponVideoGemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5)
)
if mibBuilder.loadTexts:
    gponVideoGemStatsTable.setStatus("current")
_GponVideoGemStatsEntry_Object = MibTableRow
gponVideoGemStatsEntry = _GponVideoGemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1)
)
gponVideoGemStatsEntry.setIndexNames(
    (0, "ZHNGPONLINK", "gponIfIndex"),
)
if mibBuilder.loadTexts:
    gponVideoGemStatsEntry.setStatus("current")
_VideoGemPortRxBytes_Type = Unsigned32
_VideoGemPortRxBytes_Object = MibTableColumn
videoGemPortRxBytes = _VideoGemPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 1),
    _VideoGemPortRxBytes_Type()
)
videoGemPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortRxBytes.setStatus("current")
_VideoGemPortRxFragments_Type = Unsigned32
_VideoGemPortRxFragments_Object = MibTableColumn
videoGemPortRxFragments = _VideoGemPortRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 2),
    _VideoGemPortRxFragments_Type()
)
videoGemPortRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortRxFragments.setStatus("current")
_VideoGemPortRxFrames_Type = Unsigned32
_VideoGemPortRxFrames_Object = MibTableColumn
videoGemPortRxFrames = _VideoGemPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 3),
    _VideoGemPortRxFrames_Type()
)
videoGemPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortRxFrames.setStatus("current")
_VideoGemPortRxDroppedFrames_Type = Unsigned32
_VideoGemPortRxDroppedFrames_Object = MibTableColumn
videoGemPortRxDroppedFrames = _VideoGemPortRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 4),
    _VideoGemPortRxDroppedFrames_Type()
)
videoGemPortRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortRxDroppedFrames.setStatus("current")
_VideoGemPortTxBytes_Type = Unsigned32
_VideoGemPortTxBytes_Object = MibTableColumn
videoGemPortTxBytes = _VideoGemPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 5),
    _VideoGemPortTxBytes_Type()
)
videoGemPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortTxBytes.setStatus("current")
_VideoGemPortTxFragments_Type = Unsigned32
_VideoGemPortTxFragments_Object = MibTableColumn
videoGemPortTxFragments = _VideoGemPortTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 6),
    _VideoGemPortTxFragments_Type()
)
videoGemPortTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortTxFragments.setStatus("current")
_VideoGemPortTxFrames_Type = Unsigned32
_VideoGemPortTxFrames_Object = MibTableColumn
videoGemPortTxFrames = _VideoGemPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 7),
    _VideoGemPortTxFrames_Type()
)
videoGemPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortTxFrames.setStatus("current")
_VideoGemPortTxDroppedFrames_Type = Unsigned32
_VideoGemPortTxDroppedFrames_Object = MibTableColumn
videoGemPortTxDroppedFrames = _VideoGemPortTxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 8),
    _VideoGemPortTxDroppedFrames_Type()
)
videoGemPortTxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortTxDroppedFrames.setStatus("current")
_VideoGemPortAcceptedMulticastFrames_Type = Unsigned32
_VideoGemPortAcceptedMulticastFrames_Object = MibTableColumn
videoGemPortAcceptedMulticastFrames = _VideoGemPortAcceptedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 9),
    _VideoGemPortAcceptedMulticastFrames_Type()
)
videoGemPortAcceptedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortAcceptedMulticastFrames.setStatus("current")
_VideoGemPortDroppedMulticastFrames_Type = Unsigned32
_VideoGemPortDroppedMulticastFrames_Object = MibTableColumn
videoGemPortDroppedMulticastFrames = _VideoGemPortDroppedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 5, 1, 10),
    _VideoGemPortDroppedMulticastFrames_Type()
)
videoGemPortDroppedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGemPortDroppedMulticastFrames.setStatus("current")
_GponGtcStatsTable_Object = MibTable
gponGtcStatsTable = _GponGtcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6)
)
if mibBuilder.loadTexts:
    gponGtcStatsTable.setStatus("current")
_GponGtcStatsEntry_Object = MibTableRow
gponGtcStatsEntry = _GponGtcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1)
)
gponGtcStatsEntry.setIndexNames(
    (0, "ZHNGPONLINK", "gponIfIndex"),
)
if mibBuilder.loadTexts:
    gponGtcStatsEntry.setStatus("current")
_GtcBipErrors_Type = Unsigned32
_GtcBipErrors_Object = MibTableColumn
gtcBipErrors = _GtcBipErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 1),
    _GtcBipErrors_Type()
)
gtcBipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtcBipErrors.setStatus("current")
_GtcFecCorrectedCodewords_Type = Unsigned32
_GtcFecCorrectedCodewords_Object = MibTableColumn
gtcFecCorrectedCodewords = _GtcFecCorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 2),
    _GtcFecCorrectedCodewords_Type()
)
gtcFecCorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtcFecCorrectedCodewords.setStatus("current")
_GtcFecUncorrectableCodewords_Type = Unsigned32
_GtcFecUncorrectableCodewords_Object = MibTableColumn
gtcFecUncorrectableCodewords = _GtcFecUncorrectableCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 3),
    _GtcFecUncorrectableCodewords_Type()
)
gtcFecUncorrectableCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtcFecUncorrectableCodewords.setStatus("current")
_GtcTotalRxDsFecCodewords_Type = Unsigned32
_GtcTotalRxDsFecCodewords_Object = MibTableColumn
gtcTotalRxDsFecCodewords = _GtcTotalRxDsFecCodewords_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 4),
    _GtcTotalRxDsFecCodewords_Type()
)
gtcTotalRxDsFecCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtcTotalRxDsFecCodewords.setStatus("current")
_GtcFecCorrectionSeconds_Type = Unsigned32
_GtcFecCorrectionSeconds_Object = MibTableColumn
gtcFecCorrectionSeconds = _GtcFecCorrectionSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 5),
    _GtcFecCorrectionSeconds_Type()
)
gtcFecCorrectionSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtcFecCorrectionSeconds.setStatus("current")
_GtcCorrectedHecErrorsGemFrames_Type = Unsigned32
_GtcCorrectedHecErrorsGemFrames_Object = MibTableColumn
gtcCorrectedHecErrorsGemFrames = _GtcCorrectedHecErrorsGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 6),
    _GtcCorrectedHecErrorsGemFrames_Type()
)
gtcCorrectedHecErrorsGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtcCorrectedHecErrorsGemFrames.setStatus("current")
_GtcUncorrectableHecErrorsGemFrames_Type = Unsigned32
_GtcUncorrectableHecErrorsGemFrames_Object = MibTableColumn
gtcUncorrectableHecErrorsGemFrames = _GtcUncorrectableHecErrorsGemFrames_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 6, 1, 7),
    _GtcUncorrectableHecErrorsGemFrames_Type()
)
gtcUncorrectableHecErrorsGemFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gtcUncorrectableHecErrorsGemFrames.setStatus("current")
_GponPloamStatsTable_Object = MibTable
gponPloamStatsTable = _GponPloamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7)
)
if mibBuilder.loadTexts:
    gponPloamStatsTable.setStatus("current")
_GponPloamStatsEntry_Object = MibTableRow
gponPloamStatsEntry = _GponPloamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1)
)
gponPloamStatsEntry.setIndexNames(
    (0, "ZHNGPONLINK", "gponIfIndex"),
)
if mibBuilder.loadTexts:
    gponPloamStatsEntry.setStatus("current")
_MsgsCrcError_Type = Unsigned32
_MsgsCrcError_Object = MibTableColumn
msgsCrcError = _MsgsCrcError_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 1),
    _MsgsCrcError_Type()
)
msgsCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsCrcError.setStatus("current")
_MsgsRxTotal_Type = Unsigned32
_MsgsRxTotal_Object = MibTableColumn
msgsRxTotal = _MsgsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 2),
    _MsgsRxTotal_Type()
)
msgsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsRxTotal.setStatus("current")
_MsgsRxUnicast_Type = Unsigned32
_MsgsRxUnicast_Object = MibTableColumn
msgsRxUnicast = _MsgsRxUnicast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 3),
    _MsgsRxUnicast_Type()
)
msgsRxUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsRxUnicast.setStatus("current")
_MsgsRxBroadcast_Type = Unsigned32
_MsgsRxBroadcast_Object = MibTableColumn
msgsRxBroadcast = _MsgsRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 4),
    _MsgsRxBroadcast_Type()
)
msgsRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsRxBroadcast.setStatus("current")
_MsgsRxDiscarded_Type = Unsigned32
_MsgsRxDiscarded_Object = MibTableColumn
msgsRxDiscarded = _MsgsRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 5),
    _MsgsRxDiscarded_Type()
)
msgsRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsRxDiscarded.setStatus("current")
_MsgsRxNonStandard_Type = Unsigned32
_MsgsRxNonStandard_Object = MibTableColumn
msgsRxNonStandard = _MsgsRxNonStandard_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 6),
    _MsgsRxNonStandard_Type()
)
msgsRxNonStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsRxNonStandard.setStatus("current")
_MsgsTxTotal_Type = Unsigned32
_MsgsTxTotal_Object = MibTableColumn
msgsTxTotal = _MsgsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 7),
    _MsgsTxTotal_Type()
)
msgsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsTxTotal.setStatus("current")
_MsgsTxNonStandard_Type = Unsigned32
_MsgsTxNonStandard_Object = MibTableColumn
msgsTxNonStandard = _MsgsTxNonStandard_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 1, 7, 1, 8),
    _MsgsTxNonStandard_Type()
)
msgsTxNonStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgsTxNonStandard.setStatus("current")
_ZhnGPONLinkConformance_ObjectIdentity = ObjectIdentity
zhnGPONLinkConformance = _ZhnGPONLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2)
)
_ZhnGPONLinkGroups_ObjectIdentity = ObjectIdentity
zhnGPONLinkGroups = _ZhnGPONLinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1)
)
_ZhnGPONLinkCompliances_ObjectIdentity = ObjectIdentity
zhnGPONLinkCompliances = _ZhnGPONLinkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 2)
)

# Managed Objects groups

zhnGPONStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 1)
)
zhnGPONStatusGroup.setObjects(
      *(("ZHNGPONLINK", "gponInterfaceNumberOfEntries"),
        ("ZHNGPONLINK", "gponOperStatus"),
        ("ZHNGPONLINK", "gponLinkUpTransitions"),
        ("ZHNGPONLINK", "rfVideo"),
        ("ZHNGPONLINK", "gponOnuId"),
        ("ZHNGPONLINK", "gponState"),
        ("ZHNGPONLINK", "rxLevel"),
        ("ZHNGPONLINK", "txPower"),
        ("ZHNGPONLINK", "txBiasCurrent"),
        ("ZHNGPONLINK", "gponTemperature"),
        ("ZHNGPONLINK", "gponVcc"))
)
if mibBuilder.loadTexts:
    zhnGPONStatusGroup.setStatus("current")

zhnGPONAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 2)
)
zhnGPONAlarmGroup.setObjects(
      *(("ZHNGPONLINK", "gponAlarmAutoPowerControlFail"),
        ("ZHNGPONLINK", "gponAlarmLOS"),
        ("ZHNGPONLINK", "gponAlarmLOL"),
        ("ZHNGPONLINK", "gponAlarmLOF"),
        ("ZHNGPONLINK", "gponAlarmLCDG"),
        ("ZHNGPONLINK", "gponAlarmFailedSignal"),
        ("ZHNGPONLINK", "gponAlarmDegradedSignal"),
        ("ZHNGPONLINK", "gponAlarmStartupFail"),
        ("ZHNGPONLINK", "gponAlarmMsgErrorMsg"),
        ("ZHNGPONLINK", "gponAlarmDeactivateOnuId"),
        ("ZHNGPONLINK", "gponAlarmDisabledOnu"),
        ("ZHNGPONLINK", "gponAlarmPEE"))
)
if mibBuilder.loadTexts:
    zhnGPONAlarmGroup.setStatus("current")

zhnGPONDataGemStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 3)
)
zhnGPONDataGemStatsGroup.setObjects(
      *(("ZHNGPONLINK", "dataGemPortRxBytes"),
        ("ZHNGPONLINK", "dataGemPortRxFragments"),
        ("ZHNGPONLINK", "dataGemPortRxFrames"),
        ("ZHNGPONLINK", "dataGemPortRxDroppedFrames"),
        ("ZHNGPONLINK", "dataGemPortTxBytes"),
        ("ZHNGPONLINK", "dataGemPortTxFragments"),
        ("ZHNGPONLINK", "dataGemPortTxFrames"),
        ("ZHNGPONLINK", "dataGemPortTxDroppedFrames"),
        ("ZHNGPONLINK", "dataGemPortAcceptedMulticastFrames"),
        ("ZHNGPONLINK", "dataGemPortDroppedMulticastFrames"))
)
if mibBuilder.loadTexts:
    zhnGPONDataGemStatsGroup.setStatus("current")

zhnGPONVideoGemStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 4)
)
zhnGPONVideoGemStatsGroup.setObjects(
      *(("ZHNGPONLINK", "videoGemPortRxBytes"),
        ("ZHNGPONLINK", "videoGemPortRxFragments"),
        ("ZHNGPONLINK", "videoGemPortRxFrames"),
        ("ZHNGPONLINK", "videoGemPortRxDroppedFrames"),
        ("ZHNGPONLINK", "videoGemPortTxBytes"),
        ("ZHNGPONLINK", "videoGemPortTxFragments"),
        ("ZHNGPONLINK", "videoGemPortTxFrames"),
        ("ZHNGPONLINK", "videoGemPortTxDroppedFrames"),
        ("ZHNGPONLINK", "videoGemPortAcceptedMulticastFrames"),
        ("ZHNGPONLINK", "videoGemPortDroppedMulticastFrames"))
)
if mibBuilder.loadTexts:
    zhnGPONVideoGemStatsGroup.setStatus("current")

zhnGPONGtcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 5)
)
zhnGPONGtcStatsGroup.setObjects(
      *(("ZHNGPONLINK", "gtcBipErrors"),
        ("ZHNGPONLINK", "gtcFecCorrectedCodewords"),
        ("ZHNGPONLINK", "gtcFecUncorrectableCodewords"),
        ("ZHNGPONLINK", "gtcTotalRxDsFecCodewords"),
        ("ZHNGPONLINK", "gtcFecCorrectionSeconds"),
        ("ZHNGPONLINK", "gtcCorrectedHecErrorsGemFrames"),
        ("ZHNGPONLINK", "gtcUncorrectableHecErrorsGemFrames"))
)
if mibBuilder.loadTexts:
    zhnGPONGtcStatsGroup.setStatus("current")

zhnGPONPloamStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 1, 6)
)
zhnGPONPloamStatsGroup.setObjects(
      *(("ZHNGPONLINK", "msgsCrcError"),
        ("ZHNGPONLINK", "msgsRxTotal"),
        ("ZHNGPONLINK", "msgsRxUnicast"),
        ("ZHNGPONLINK", "msgsRxBroadcast"),
        ("ZHNGPONLINK", "msgsRxDiscarded"),
        ("ZHNGPONLINK", "msgsRxNonStandard"),
        ("ZHNGPONLINK", "msgsTxTotal"),
        ("ZHNGPONLINK", "msgsTxNonStandard"))
)
if mibBuilder.loadTexts:
    zhnGPONPloamStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnGPONLinkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 43, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnGPONLinkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNGPONLINK",
    **{"GPONLinkStatusValues": GPONLinkStatusValues,
       "GPONEnabledDisabledStatusValues": GPONEnabledDisabledStatusValues,
       "GPONStateValues": GPONStateValues,
       "GPONOnOffAlarmValues": GPONOnOffAlarmValues,
       "zhnGPONLink": zhnGPONLink,
       "zhnGPONLinkObjects": zhnGPONLinkObjects,
       "gponInterfaceNumberOfEntries": gponInterfaceNumberOfEntries,
       "gponLinkStatusTable": gponLinkStatusTable,
       "gponLinkStatusEntry": gponLinkStatusEntry,
       "gponIfIndex": gponIfIndex,
       "gponOperStatus": gponOperStatus,
       "gponLinkUpTransitions": gponLinkUpTransitions,
       "rfVideo": rfVideo,
       "gponOnuId": gponOnuId,
       "gponState": gponState,
       "rxLevel": rxLevel,
       "txPower": txPower,
       "txBiasCurrent": txBiasCurrent,
       "gponTemperature": gponTemperature,
       "gponVcc": gponVcc,
       "gponAlarmStatusTable": gponAlarmStatusTable,
       "gponAlarmStatusEntry": gponAlarmStatusEntry,
       "gponAlarmAutoPowerControlFail": gponAlarmAutoPowerControlFail,
       "gponAlarmLOS": gponAlarmLOS,
       "gponAlarmLOL": gponAlarmLOL,
       "gponAlarmLOF": gponAlarmLOF,
       "gponAlarmLCDG": gponAlarmLCDG,
       "gponAlarmFailedSignal": gponAlarmFailedSignal,
       "gponAlarmDegradedSignal": gponAlarmDegradedSignal,
       "gponAlarmStartupFail": gponAlarmStartupFail,
       "gponAlarmMsgErrorMsg": gponAlarmMsgErrorMsg,
       "gponAlarmDeactivateOnuId": gponAlarmDeactivateOnuId,
       "gponAlarmDisabledOnu": gponAlarmDisabledOnu,
       "gponAlarmPEE": gponAlarmPEE,
       "gponDataGemStatsTable": gponDataGemStatsTable,
       "gponDataGemStatsEntry": gponDataGemStatsEntry,
       "dataGemPortRxBytes": dataGemPortRxBytes,
       "dataGemPortRxFragments": dataGemPortRxFragments,
       "dataGemPortRxFrames": dataGemPortRxFrames,
       "dataGemPortRxDroppedFrames": dataGemPortRxDroppedFrames,
       "dataGemPortTxBytes": dataGemPortTxBytes,
       "dataGemPortTxFragments": dataGemPortTxFragments,
       "dataGemPortTxFrames": dataGemPortTxFrames,
       "dataGemPortTxDroppedFrames": dataGemPortTxDroppedFrames,
       "dataGemPortAcceptedMulticastFrames": dataGemPortAcceptedMulticastFrames,
       "dataGemPortDroppedMulticastFrames": dataGemPortDroppedMulticastFrames,
       "gponVideoGemStatsTable": gponVideoGemStatsTable,
       "gponVideoGemStatsEntry": gponVideoGemStatsEntry,
       "videoGemPortRxBytes": videoGemPortRxBytes,
       "videoGemPortRxFragments": videoGemPortRxFragments,
       "videoGemPortRxFrames": videoGemPortRxFrames,
       "videoGemPortRxDroppedFrames": videoGemPortRxDroppedFrames,
       "videoGemPortTxBytes": videoGemPortTxBytes,
       "videoGemPortTxFragments": videoGemPortTxFragments,
       "videoGemPortTxFrames": videoGemPortTxFrames,
       "videoGemPortTxDroppedFrames": videoGemPortTxDroppedFrames,
       "videoGemPortAcceptedMulticastFrames": videoGemPortAcceptedMulticastFrames,
       "videoGemPortDroppedMulticastFrames": videoGemPortDroppedMulticastFrames,
       "gponGtcStatsTable": gponGtcStatsTable,
       "gponGtcStatsEntry": gponGtcStatsEntry,
       "gtcBipErrors": gtcBipErrors,
       "gtcFecCorrectedCodewords": gtcFecCorrectedCodewords,
       "gtcFecUncorrectableCodewords": gtcFecUncorrectableCodewords,
       "gtcTotalRxDsFecCodewords": gtcTotalRxDsFecCodewords,
       "gtcFecCorrectionSeconds": gtcFecCorrectionSeconds,
       "gtcCorrectedHecErrorsGemFrames": gtcCorrectedHecErrorsGemFrames,
       "gtcUncorrectableHecErrorsGemFrames": gtcUncorrectableHecErrorsGemFrames,
       "gponPloamStatsTable": gponPloamStatsTable,
       "gponPloamStatsEntry": gponPloamStatsEntry,
       "msgsCrcError": msgsCrcError,
       "msgsRxTotal": msgsRxTotal,
       "msgsRxUnicast": msgsRxUnicast,
       "msgsRxBroadcast": msgsRxBroadcast,
       "msgsRxDiscarded": msgsRxDiscarded,
       "msgsRxNonStandard": msgsRxNonStandard,
       "msgsTxTotal": msgsTxTotal,
       "msgsTxNonStandard": msgsTxNonStandard,
       "zhnGPONLinkConformance": zhnGPONLinkConformance,
       "zhnGPONLinkGroups": zhnGPONLinkGroups,
       "zhnGPONStatusGroup": zhnGPONStatusGroup,
       "zhnGPONAlarmGroup": zhnGPONAlarmGroup,
       "zhnGPONDataGemStatsGroup": zhnGPONDataGemStatsGroup,
       "zhnGPONVideoGemStatsGroup": zhnGPONVideoGemStatsGroup,
       "zhnGPONGtcStatsGroup": zhnGPONGtcStatsGroup,
       "zhnGPONPloamStatsGroup": zhnGPONPloamStatsGroup,
       "zhnGPONLinkCompliances": zhnGPONLinkCompliances,
       "zhnGPONLinkCompliance": zhnGPONLinkCompliance}
)
