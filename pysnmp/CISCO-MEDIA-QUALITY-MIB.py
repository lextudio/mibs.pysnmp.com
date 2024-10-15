# SNMP MIB module (CISCO-MEDIA-QUALITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEDIA-QUALITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:21 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvcCallReferenceIdOrZero,
 CvcCoderTypeRate,
 CvcGUid) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcCallReferenceIdOrZero",
    "CvcCoderTypeRate",
    "CvcGUid")

(callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "callActiveIndex",
    "callActiveSetupTime")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMediaQualityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769)
)
ciscoMediaQualityMIB.setRevisions(
        ("2011-03-23 00:00",
         "2011-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMediaQualityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMediaQualityMIBNotifs = _CiscoMediaQualityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 0)
)
_CiscoMediaQualityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMediaQualityMIBObjects = _CiscoMediaQualityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1)
)
_CmqVoiceCallActive_ObjectIdentity = ObjectIdentity
cmqVoiceCallActive = _CmqVoiceCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1)
)
_CmqVoIPCallActiveTable_Object = MibTable
cmqVoIPCallActiveTable = _CmqVoIPCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTable.setStatus("current")
_CmqVoIPCallActiveEntry_Object = MibTableRow
cmqVoIPCallActiveEntry = _CmqVoIPCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1)
)
cmqVoIPCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cmqVoIPCallActiveEntry.setStatus("current")
_CmqVoIPCallActiveConnectionId_Type = CvcGUid
_CmqVoIPCallActiveConnectionId_Object = MibTableColumn
cmqVoIPCallActiveConnectionId = _CmqVoIPCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 1),
    _CmqVoIPCallActiveConnectionId_Type()
)
cmqVoIPCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveConnectionId.setStatus("current")
_CmqVoIPCallActiveCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqVoIPCallActiveCallReferenceId_Object = MibTableColumn
cmqVoIPCallActiveCallReferenceId = _CmqVoIPCallActiveCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 2),
    _CmqVoIPCallActiveCallReferenceId_Type()
)
cmqVoIPCallActiveCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveCallReferenceId.setStatus("current")
_CmqVoIPCallActiveRxCodecId_Type = CvcCoderTypeRate
_CmqVoIPCallActiveRxCodecId_Object = MibTableColumn
cmqVoIPCallActiveRxCodecId = _CmqVoIPCallActiveRxCodecId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 3),
    _CmqVoIPCallActiveRxCodecId_Type()
)
cmqVoIPCallActiveRxCodecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxCodecId.setStatus("current")
_CmqVoIPCallActiveRxSevConcealRatioPct_Type = Unsigned32
_CmqVoIPCallActiveRxSevConcealRatioPct_Object = MibTableColumn
cmqVoIPCallActiveRxSevConcealRatioPct = _CmqVoIPCallActiveRxSevConcealRatioPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 4),
    _CmqVoIPCallActiveRxSevConcealRatioPct_Type()
)
cmqVoIPCallActiveRxSevConcealRatioPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxSevConcealRatioPct.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxSevConcealRatioPct.setUnits("percent")
_CmqVoIPCallActiveRxCallConcealRatioPct_Type = Unsigned32
_CmqVoIPCallActiveRxCallConcealRatioPct_Object = MibTableColumn
cmqVoIPCallActiveRxCallConcealRatioPct = _CmqVoIPCallActiveRxCallConcealRatioPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 5),
    _CmqVoIPCallActiveRxCallConcealRatioPct_Type()
)
cmqVoIPCallActiveRxCallConcealRatioPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxCallConcealRatioPct.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxCallConcealRatioPct.setUnits("percent")
_CmqVoIPCallActiveRxPktLossRatioPct_Type = Unsigned32
_CmqVoIPCallActiveRxPktLossRatioPct_Object = MibTableColumn
cmqVoIPCallActiveRxPktLossRatioPct = _CmqVoIPCallActiveRxPktLossRatioPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 6),
    _CmqVoIPCallActiveRxPktLossRatioPct_Type()
)
cmqVoIPCallActiveRxPktLossRatioPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktLossRatioPct.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktLossRatioPct.setUnits("percent")
_CmqVoIPCallActiveRxRoundTripTime_Type = Unsigned32
_CmqVoIPCallActiveRxRoundTripTime_Object = MibTableColumn
cmqVoIPCallActiveRxRoundTripTime = _CmqVoIPCallActiveRxRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 7),
    _CmqVoIPCallActiveRxRoundTripTime_Type()
)
cmqVoIPCallActiveRxRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxRoundTripTime.setUnits("milliseconds")
_CmqVoIPCallActiveRxCallDur_Type = Unsigned32
_CmqVoIPCallActiveRxCallDur_Object = MibTableColumn
cmqVoIPCallActiveRxCallDur = _CmqVoIPCallActiveRxCallDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 8),
    _CmqVoIPCallActiveRxCallDur_Type()
)
cmqVoIPCallActiveRxCallDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxCallDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxCallDur.setUnits("milliseconds")
_CmqVoIPCallActiveRxVoiceDur_Type = Unsigned32
_CmqVoIPCallActiveRxVoiceDur_Object = MibTableColumn
cmqVoIPCallActiveRxVoiceDur = _CmqVoIPCallActiveRxVoiceDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 9),
    _CmqVoIPCallActiveRxVoiceDur_Type()
)
cmqVoIPCallActiveRxVoiceDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxVoiceDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxVoiceDur.setUnits("milliseconds")
_CmqVoIPCallActiveRxPktLossConcealDur_Type = Unsigned32
_CmqVoIPCallActiveRxPktLossConcealDur_Object = MibTableColumn
cmqVoIPCallActiveRxPktLossConcealDur = _CmqVoIPCallActiveRxPktLossConcealDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 10),
    _CmqVoIPCallActiveRxPktLossConcealDur_Type()
)
cmqVoIPCallActiveRxPktLossConcealDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktLossConcealDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktLossConcealDur.setUnits("milliseconds")
_CmqVoIPCallActiveRxPktCntExpected_Type = Counter32
_CmqVoIPCallActiveRxPktCntExpected_Object = MibTableColumn
cmqVoIPCallActiveRxPktCntExpected = _CmqVoIPCallActiveRxPktCntExpected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 11),
    _CmqVoIPCallActiveRxPktCntExpected_Type()
)
cmqVoIPCallActiveRxPktCntExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntExpected.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntExpected.setUnits("packets")
_CmqVoIPCallActiveRxPktCntNotArrived_Type = Counter32
_CmqVoIPCallActiveRxPktCntNotArrived_Object = MibTableColumn
cmqVoIPCallActiveRxPktCntNotArrived = _CmqVoIPCallActiveRxPktCntNotArrived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 12),
    _CmqVoIPCallActiveRxPktCntNotArrived_Type()
)
cmqVoIPCallActiveRxPktCntNotArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntNotArrived.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntNotArrived.setUnits("packets")
_CmqVoIPCallActiveRxPktCntComfortNoise_Type = Counter32
_CmqVoIPCallActiveRxPktCntComfortNoise_Object = MibTableColumn
cmqVoIPCallActiveRxPktCntComfortNoise = _CmqVoIPCallActiveRxPktCntComfortNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 13),
    _CmqVoIPCallActiveRxPktCntComfortNoise_Type()
)
cmqVoIPCallActiveRxPktCntComfortNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntComfortNoise.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntComfortNoise.setUnits("packets")
_CmqVoIPCallActiveRxPktCntUnusableLate_Type = Counter32
_CmqVoIPCallActiveRxPktCntUnusableLate_Object = MibTableColumn
cmqVoIPCallActiveRxPktCntUnusableLate = _CmqVoIPCallActiveRxPktCntUnusableLate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 14),
    _CmqVoIPCallActiveRxPktCntUnusableLate_Type()
)
cmqVoIPCallActiveRxPktCntUnusableLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntUnusableLate.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntUnusableLate.setUnits("packets")
_CmqVoIPCallActiveRxPktCntDiscarded_Type = Counter32
_CmqVoIPCallActiveRxPktCntDiscarded_Object = MibTableColumn
cmqVoIPCallActiveRxPktCntDiscarded = _CmqVoIPCallActiveRxPktCntDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 15),
    _CmqVoIPCallActiveRxPktCntDiscarded_Type()
)
cmqVoIPCallActiveRxPktCntDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntDiscarded.setUnits("packets")
_CmqVoIPCallActiveRxPktCntEffLoss_Type = Counter32
_CmqVoIPCallActiveRxPktCntEffLoss_Object = MibTableColumn
cmqVoIPCallActiveRxPktCntEffLoss = _CmqVoIPCallActiveRxPktCntEffLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 16),
    _CmqVoIPCallActiveRxPktCntEffLoss_Type()
)
cmqVoIPCallActiveRxPktCntEffLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntEffLoss.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPktCntEffLoss.setUnits("packets")
_CmqVoIPCallActiveRxUnimpairedSecOK_Type = Counter32
_CmqVoIPCallActiveRxUnimpairedSecOK_Object = MibTableColumn
cmqVoIPCallActiveRxUnimpairedSecOK = _CmqVoIPCallActiveRxUnimpairedSecOK_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 17),
    _CmqVoIPCallActiveRxUnimpairedSecOK_Type()
)
cmqVoIPCallActiveRxUnimpairedSecOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxUnimpairedSecOK.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxUnimpairedSecOK.setUnits("seconds")
_CmqVoIPCallActiveRxConcealSec_Type = Counter32
_CmqVoIPCallActiveRxConcealSec_Object = MibTableColumn
cmqVoIPCallActiveRxConcealSec = _CmqVoIPCallActiveRxConcealSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 18),
    _CmqVoIPCallActiveRxConcealSec_Type()
)
cmqVoIPCallActiveRxConcealSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxConcealSec.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxConcealSec.setUnits("seconds")
_CmqVoIPCallActiveRxSevConcealSec_Type = Counter32
_CmqVoIPCallActiveRxSevConcealSec_Object = MibTableColumn
cmqVoIPCallActiveRxSevConcealSec = _CmqVoIPCallActiveRxSevConcealSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 19),
    _CmqVoIPCallActiveRxSevConcealSec_Type()
)
cmqVoIPCallActiveRxSevConcealSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxSevConcealSec.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxSevConcealSec.setUnits("seconds")


class _CmqVoIPCallActiveRxJBufMode_Type(Integer32):
    """Custom type cmqVoIPCallActiveRxJBufMode based on Integer32"""
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
        *(("adaptive", 1),
          ("disabled", 4),
          ("fixed", 2),
          ("unknown", 3))
    )


_CmqVoIPCallActiveRxJBufMode_Type.__name__ = "Integer32"
_CmqVoIPCallActiveRxJBufMode_Object = MibTableColumn
cmqVoIPCallActiveRxJBufMode = _CmqVoIPCallActiveRxJBufMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 20),
    _CmqVoIPCallActiveRxJBufMode_Type()
)
cmqVoIPCallActiveRxJBufMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBufMode.setStatus("current")
_CmqVoIPCallActiveRxJBufNomDelay_Type = Unsigned32
_CmqVoIPCallActiveRxJBufNomDelay_Object = MibTableColumn
cmqVoIPCallActiveRxJBufNomDelay = _CmqVoIPCallActiveRxJBufNomDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 21),
    _CmqVoIPCallActiveRxJBufNomDelay_Type()
)
cmqVoIPCallActiveRxJBufNomDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBufNomDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBufNomDelay.setUnits("milliseconds")
_CmqVoIPCallActiveRxJBufDlyNow_Type = Unsigned32
_CmqVoIPCallActiveRxJBufDlyNow_Object = MibTableColumn
cmqVoIPCallActiveRxJBufDlyNow = _CmqVoIPCallActiveRxJBufDlyNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 22),
    _CmqVoIPCallActiveRxJBufDlyNow_Type()
)
cmqVoIPCallActiveRxJBufDlyNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBufDlyNow.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBufDlyNow.setUnits("milliseconds")
_CmqVoIPCallActiveRxJBufLowWater_Type = Unsigned32
_CmqVoIPCallActiveRxJBufLowWater_Object = MibTableColumn
cmqVoIPCallActiveRxJBufLowWater = _CmqVoIPCallActiveRxJBufLowWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 23),
    _CmqVoIPCallActiveRxJBufLowWater_Type()
)
cmqVoIPCallActiveRxJBufLowWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBufLowWater.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBufLowWater.setUnits("milliseconds")
_CmqVoIPCallActiveRxJBuffHiWater_Type = Unsigned32
_CmqVoIPCallActiveRxJBuffHiWater_Object = MibTableColumn
cmqVoIPCallActiveRxJBuffHiWater = _CmqVoIPCallActiveRxJBuffHiWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 24),
    _CmqVoIPCallActiveRxJBuffHiWater_Type()
)
cmqVoIPCallActiveRxJBuffHiWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBuffHiWater.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxJBuffHiWater.setUnits("milliseconds")
_CmqVoIPCallActive3550JShortTermAvg_Type = Unsigned32
_CmqVoIPCallActive3550JShortTermAvg_Object = MibTableColumn
cmqVoIPCallActive3550JShortTermAvg = _CmqVoIPCallActive3550JShortTermAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 25),
    _CmqVoIPCallActive3550JShortTermAvg_Type()
)
cmqVoIPCallActive3550JShortTermAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActive3550JShortTermAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActive3550JShortTermAvg.setUnits("milliseconds")
_CmqVoIPCallActive3550JCallAvg_Type = Unsigned32
_CmqVoIPCallActive3550JCallAvg_Object = MibTableColumn
cmqVoIPCallActive3550JCallAvg = _CmqVoIPCallActive3550JCallAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 26),
    _CmqVoIPCallActive3550JCallAvg_Type()
)
cmqVoIPCallActive3550JCallAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActive3550JCallAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActive3550JCallAvg.setUnits("milliseconds")
_CmqVoIPCallActiveRxSignalLvl_Type = Integer32
_CmqVoIPCallActiveRxSignalLvl_Object = MibTableColumn
cmqVoIPCallActiveRxSignalLvl = _CmqVoIPCallActiveRxSignalLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 27),
    _CmqVoIPCallActiveRxSignalLvl_Type()
)
cmqVoIPCallActiveRxSignalLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxSignalLvl.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxSignalLvl.setUnits("0.1 dB")
_CmqVoIPCallActiveRxPred107Rscore_Type = Unsigned32
_CmqVoIPCallActiveRxPred107Rscore_Object = MibTableColumn
cmqVoIPCallActiveRxPred107Rscore = _CmqVoIPCallActiveRxPred107Rscore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 28),
    _CmqVoIPCallActiveRxPred107Rscore_Type()
)
cmqVoIPCallActiveRxPred107Rscore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107Rscore.setStatus("current")
_CmqVoIPCallActiveRxPred107RMosListen_Type = Unsigned32
_CmqVoIPCallActiveRxPred107RMosListen_Object = MibTableColumn
cmqVoIPCallActiveRxPred107RMosListen = _CmqVoIPCallActiveRxPred107RMosListen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 29),
    _CmqVoIPCallActiveRxPred107RMosListen_Type()
)
cmqVoIPCallActiveRxPred107RMosListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107RMosListen.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107RMosListen.setUnits("percent")
_CmqVoIPCallActiveRxPred107RScoreConv_Type = Unsigned32
_CmqVoIPCallActiveRxPred107RScoreConv_Object = MibTableColumn
cmqVoIPCallActiveRxPred107RScoreConv = _CmqVoIPCallActiveRxPred107RScoreConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 30),
    _CmqVoIPCallActiveRxPred107RScoreConv_Type()
)
cmqVoIPCallActiveRxPred107RScoreConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107RScoreConv.setStatus("current")
_CmqVoIPCallActiveRxPred107RMosConv_Type = Unsigned32
_CmqVoIPCallActiveRxPred107RMosConv_Object = MibTableColumn
cmqVoIPCallActiveRxPred107RMosConv = _CmqVoIPCallActiveRxPred107RMosConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 31),
    _CmqVoIPCallActiveRxPred107RMosConv_Type()
)
cmqVoIPCallActiveRxPred107RMosConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107RMosConv.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107RMosConv.setUnits("percent")
_CmqVoIPCallActiveRxPred107CodecIeBase_Type = Unsigned32
_CmqVoIPCallActiveRxPred107CodecIeBase_Object = MibTableColumn
cmqVoIPCallActiveRxPred107CodecIeBase = _CmqVoIPCallActiveRxPred107CodecIeBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 32),
    _CmqVoIPCallActiveRxPred107CodecIeBase_Type()
)
cmqVoIPCallActiveRxPred107CodecIeBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107CodecIeBase.setStatus("current")
_CmqVoIPCallActiveRxPred107CodecBPL_Type = Unsigned32
_CmqVoIPCallActiveRxPred107CodecBPL_Object = MibTableColumn
cmqVoIPCallActiveRxPred107CodecBPL = _CmqVoIPCallActiveRxPred107CodecBPL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 33),
    _CmqVoIPCallActiveRxPred107CodecBPL_Type()
)
cmqVoIPCallActiveRxPred107CodecBPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107CodecBPL.setStatus("current")
_CmqVoIPCallActiveRxPred107DefaultR0_Type = Unsigned32
_CmqVoIPCallActiveRxPred107DefaultR0_Object = MibTableColumn
cmqVoIPCallActiveRxPred107DefaultR0 = _CmqVoIPCallActiveRxPred107DefaultR0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 34),
    _CmqVoIPCallActiveRxPred107DefaultR0_Type()
)
cmqVoIPCallActiveRxPred107DefaultR0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107DefaultR0.setStatus("current")
_CmqVoIPCallActiveRxPred107IeEff_Type = Unsigned32
_CmqVoIPCallActiveRxPred107IeEff_Object = MibTableColumn
cmqVoIPCallActiveRxPred107IeEff = _CmqVoIPCallActiveRxPred107IeEff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 35),
    _CmqVoIPCallActiveRxPred107IeEff_Type()
)
cmqVoIPCallActiveRxPred107IeEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107IeEff.setStatus("current")
_CmqVoIPCallActiveRxPred107Idd_Type = Unsigned32
_CmqVoIPCallActiveRxPred107Idd_Object = MibTableColumn
cmqVoIPCallActiveRxPred107Idd = _CmqVoIPCallActiveRxPred107Idd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 36),
    _CmqVoIPCallActiveRxPred107Idd_Type()
)
cmqVoIPCallActiveRxPred107Idd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPred107Idd.setStatus("current")
_CmqVoIPCallActiveRxPredMosLqoAvg_Type = Unsigned32
_CmqVoIPCallActiveRxPredMosLqoAvg_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoAvg = _CmqVoIPCallActiveRxPredMosLqoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 37),
    _CmqVoIPCallActiveRxPredMosLqoAvg_Type()
)
cmqVoIPCallActiveRxPredMosLqoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoAvg.setUnits("percent")
_CmqVoIPCallActiveRxPredMosLqoRecent_Type = Unsigned32
_CmqVoIPCallActiveRxPredMosLqoRecent_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoRecent = _CmqVoIPCallActiveRxPredMosLqoRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 38),
    _CmqVoIPCallActiveRxPredMosLqoRecent_Type()
)
cmqVoIPCallActiveRxPredMosLqoRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoRecent.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoRecent.setUnits("percent")
_CmqVoIPCallActiveRxPredMosLqoBaseline_Type = Unsigned32
_CmqVoIPCallActiveRxPredMosLqoBaseline_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoBaseline = _CmqVoIPCallActiveRxPredMosLqoBaseline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 39),
    _CmqVoIPCallActiveRxPredMosLqoBaseline_Type()
)
cmqVoIPCallActiveRxPredMosLqoBaseline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoBaseline.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoBaseline.setUnits("percent")
_CmqVoIPCallActiveRxPredMosLqoMin_Type = Unsigned32
_CmqVoIPCallActiveRxPredMosLqoMin_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoMin = _CmqVoIPCallActiveRxPredMosLqoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 40),
    _CmqVoIPCallActiveRxPredMosLqoMin_Type()
)
cmqVoIPCallActiveRxPredMosLqoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoMin.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoMin.setUnits("percent")
_CmqVoIPCallActiveRxPredMosLqoNumWin_Type = Unsigned32
_CmqVoIPCallActiveRxPredMosLqoNumWin_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoNumWin = _CmqVoIPCallActiveRxPredMosLqoNumWin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 41),
    _CmqVoIPCallActiveRxPredMosLqoNumWin_Type()
)
cmqVoIPCallActiveRxPredMosLqoNumWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoNumWin.setStatus("current")
_CmqVoIPCallActiveRxPredMosLqoBursts_Type = Unsigned32
_CmqVoIPCallActiveRxPredMosLqoBursts_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoBursts = _CmqVoIPCallActiveRxPredMosLqoBursts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 42),
    _CmqVoIPCallActiveRxPredMosLqoBursts_Type()
)
cmqVoIPCallActiveRxPredMosLqoBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoBursts.setStatus("current")
_CmqVoIPCallActiveRxPredMosLqoFrLoss_Type = Unsigned32
_CmqVoIPCallActiveRxPredMosLqoFrLoss_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoFrLoss = _CmqVoIPCallActiveRxPredMosLqoFrLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 43),
    _CmqVoIPCallActiveRxPredMosLqoFrLoss_Type()
)
cmqVoIPCallActiveRxPredMosLqoFrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoFrLoss.setStatus("current")


class _CmqVoIPCallActiveRxPredMosLqoVerID_Type(SnmpAdminString):
    """Custom type cmqVoIPCallActiveRxPredMosLqoVerID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmqVoIPCallActiveRxPredMosLqoVerID_Type.__name__ = "SnmpAdminString"
_CmqVoIPCallActiveRxPredMosLqoVerID_Object = MibTableColumn
cmqVoIPCallActiveRxPredMosLqoVerID = _CmqVoIPCallActiveRxPredMosLqoVerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 44),
    _CmqVoIPCallActiveRxPredMosLqoVerID_Type()
)
cmqVoIPCallActiveRxPredMosLqoVerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveRxPredMosLqoVerID.setStatus("current")
_CmqVoIPCallActiveTxCodecId_Type = CvcCoderTypeRate
_CmqVoIPCallActiveTxCodecId_Object = MibTableColumn
cmqVoIPCallActiveTxCodecId = _CmqVoIPCallActiveTxCodecId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 45),
    _CmqVoIPCallActiveTxCodecId_Type()
)
cmqVoIPCallActiveTxCodecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxCodecId.setStatus("current")
_CmqVoIPCallActiveTxVadEnabled_Type = TruthValue
_CmqVoIPCallActiveTxVadEnabled_Object = MibTableColumn
cmqVoIPCallActiveTxVadEnabled = _CmqVoIPCallActiveTxVadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 46),
    _CmqVoIPCallActiveTxVadEnabled_Type()
)
cmqVoIPCallActiveTxVadEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxVadEnabled.setStatus("current")
_CmqVoIPCallActiveTxTmrCallDur_Type = Unsigned32
_CmqVoIPCallActiveTxTmrCallDur_Object = MibTableColumn
cmqVoIPCallActiveTxTmrCallDur = _CmqVoIPCallActiveTxTmrCallDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 47),
    _CmqVoIPCallActiveTxTmrCallDur_Type()
)
cmqVoIPCallActiveTxTmrCallDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxTmrCallDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxTmrCallDur.setUnits("milliseconds")
_CmqVoIPCallActiveTxTmrActSpeechDur_Type = Unsigned32
_CmqVoIPCallActiveTxTmrActSpeechDur_Object = MibTableColumn
cmqVoIPCallActiveTxTmrActSpeechDur = _CmqVoIPCallActiveTxTmrActSpeechDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 48),
    _CmqVoIPCallActiveTxTmrActSpeechDur_Type()
)
cmqVoIPCallActiveTxTmrActSpeechDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxTmrActSpeechDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxTmrActSpeechDur.setUnits("milliseconds")
_CmqVoIPCallActiveTxSignalLvl_Type = Integer32
_CmqVoIPCallActiveTxSignalLvl_Object = MibTableColumn
cmqVoIPCallActiveTxSignalLvl = _CmqVoIPCallActiveTxSignalLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 49),
    _CmqVoIPCallActiveTxSignalLvl_Type()
)
cmqVoIPCallActiveTxSignalLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxSignalLvl.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxSignalLvl.setUnits("0.1 dB")
_CmqVoIPCallActiveTxNoiseFloor_Type = Integer32
_CmqVoIPCallActiveTxNoiseFloor_Object = MibTableColumn
cmqVoIPCallActiveTxNoiseFloor = _CmqVoIPCallActiveTxNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 1, 1, 50),
    _CmqVoIPCallActiveTxNoiseFloor_Type()
)
cmqVoIPCallActiveTxNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallActiveTxNoiseFloor.setStatus("current")
_CmqCommonCallActiveNRTable_Object = MibTable
cmqCommonCallActiveNRTable = _CmqCommonCallActiveNRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRTable.setStatus("current")
_CmqCommonCallActiveNREntry_Object = MibTableRow
cmqCommonCallActiveNREntry = _CmqCommonCallActiveNREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1)
)
cmqCommonCallActiveNREntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cmqCommonCallActiveNREntry.setStatus("current")
_CmqCommonCallActiveNRConnectionId_Type = CvcGUid
_CmqCommonCallActiveNRConnectionId_Object = MibTableColumn
cmqCommonCallActiveNRConnectionId = _CmqCommonCallActiveNRConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 1),
    _CmqCommonCallActiveNRConnectionId_Type()
)
cmqCommonCallActiveNRConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRConnectionId.setStatus("current")
_CmqCommonCallActiveNRCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqCommonCallActiveNRCallReferenceId_Object = MibTableColumn
cmqCommonCallActiveNRCallReferenceId = _CmqCommonCallActiveNRCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 2),
    _CmqCommonCallActiveNRCallReferenceId_Type()
)
cmqCommonCallActiveNRCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRCallReferenceId.setStatus("current")


class _CmqCommonCallActiveNRCallType_Type(Integer32):
    """Custom type cmqCommonCallActiveNRCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tdm", 1),
          ("voip", 2))
    )


_CmqCommonCallActiveNRCallType_Type.__name__ = "Integer32"
_CmqCommonCallActiveNRCallType_Object = MibTableColumn
cmqCommonCallActiveNRCallType = _CmqCommonCallActiveNRCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 3),
    _CmqCommonCallActiveNRCallType_Type()
)
cmqCommonCallActiveNRCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRCallType.setStatus("current")
_CmqCommonCallActiveNREnabledMic_Type = TruthValue
_CmqCommonCallActiveNREnabledMic_Object = MibTableColumn
cmqCommonCallActiveNREnabledMic = _CmqCommonCallActiveNREnabledMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 4),
    _CmqCommonCallActiveNREnabledMic_Type()
)
cmqCommonCallActiveNREnabledMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNREnabledMic.setStatus("current")
_CmqCommonCallActiveNREnabledEar_Type = TruthValue
_CmqCommonCallActiveNREnabledEar_Object = MibTableColumn
cmqCommonCallActiveNREnabledEar = _CmqCommonCallActiveNREnabledEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 5),
    _CmqCommonCallActiveNREnabledEar_Type()
)
cmqCommonCallActiveNREnabledEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNREnabledEar.setStatus("current")


class _CmqCommonCallActiveNRDirMic_Type(Integer32):
    """Custom type cmqCommonCallActiveNRDirMic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallActiveNRDirMic_Type.__name__ = "Integer32"
_CmqCommonCallActiveNRDirMic_Object = MibTableColumn
cmqCommonCallActiveNRDirMic = _CmqCommonCallActiveNRDirMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 6),
    _CmqCommonCallActiveNRDirMic_Type()
)
cmqCommonCallActiveNRDirMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRDirMic.setStatus("current")


class _CmqCommonCallActiveNRDirEar_Type(Integer32):
    """Custom type cmqCommonCallActiveNRDirEar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallActiveNRDirEar_Type.__name__ = "Integer32"
_CmqCommonCallActiveNRDirEar_Object = MibTableColumn
cmqCommonCallActiveNRDirEar = _CmqCommonCallActiveNRDirEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 7),
    _CmqCommonCallActiveNRDirEar_Type()
)
cmqCommonCallActiveNRDirEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRDirEar.setStatus("current")
_CmqCommonCallActiveNRLibVer_Type = Unsigned32
_CmqCommonCallActiveNRLibVer_Object = MibTableColumn
cmqCommonCallActiveNRLibVer = _CmqCommonCallActiveNRLibVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 8),
    _CmqCommonCallActiveNRLibVer_Type()
)
cmqCommonCallActiveNRLibVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRLibVer.setStatus("current")


class _CmqCommonCallActiveNRIntensity_Type(Integer32):
    """Custom type cmqCommonCallActiveNRIntensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_CmqCommonCallActiveNRIntensity_Type.__name__ = "Integer32"
_CmqCommonCallActiveNRIntensity_Object = MibTableColumn
cmqCommonCallActiveNRIntensity = _CmqCommonCallActiveNRIntensity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 9),
    _CmqCommonCallActiveNRIntensity_Type()
)
cmqCommonCallActiveNRIntensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNRIntensity.setStatus("current")
_CmqCommonCallActivePreNRNoiseFloorEstMic_Type = Integer32
_CmqCommonCallActivePreNRNoiseFloorEstMic_Object = MibTableColumn
cmqCommonCallActivePreNRNoiseFloorEstMic = _CmqCommonCallActivePreNRNoiseFloorEstMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 10),
    _CmqCommonCallActivePreNRNoiseFloorEstMic_Type()
)
cmqCommonCallActivePreNRNoiseFloorEstMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActivePreNRNoiseFloorEstMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActivePreNRNoiseFloorEstMic.setUnits("0.1 dB")
_CmqCommonCallActivePostNRNoiseFloorEstMic_Type = Integer32
_CmqCommonCallActivePostNRNoiseFloorEstMic_Object = MibTableColumn
cmqCommonCallActivePostNRNoiseFloorEstMic = _CmqCommonCallActivePostNRNoiseFloorEstMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 11),
    _CmqCommonCallActivePostNRNoiseFloorEstMic_Type()
)
cmqCommonCallActivePostNRNoiseFloorEstMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActivePostNRNoiseFloorEstMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActivePostNRNoiseFloorEstMic.setUnits("0.1 dB")
_CmqCommonCallActivePreNRNoiseFloorEstEar_Type = Integer32
_CmqCommonCallActivePreNRNoiseFloorEstEar_Object = MibTableColumn
cmqCommonCallActivePreNRNoiseFloorEstEar = _CmqCommonCallActivePreNRNoiseFloorEstEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 12),
    _CmqCommonCallActivePreNRNoiseFloorEstEar_Type()
)
cmqCommonCallActivePreNRNoiseFloorEstEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActivePreNRNoiseFloorEstEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActivePreNRNoiseFloorEstEar.setUnits("0.1 dB")
_CmqCommonCallActivePostNRNoiseFloorEstEar_Type = Integer32
_CmqCommonCallActivePostNRNoiseFloorEstEar_Object = MibTableColumn
cmqCommonCallActivePostNRNoiseFloorEstEar = _CmqCommonCallActivePostNRNoiseFloorEstEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 2, 1, 13),
    _CmqCommonCallActivePostNRNoiseFloorEstEar_Type()
)
cmqCommonCallActivePostNRNoiseFloorEstEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActivePostNRNoiseFloorEstEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActivePostNRNoiseFloorEstEar.setUnits("0.1 dB")
_CmqCommonCallActiveASPTable_Object = MibTable
cmqCommonCallActiveASPTable = _CmqCommonCallActiveASPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPTable.setStatus("current")
_CmqCommonCallActiveASPEntry_Object = MibTableRow
cmqCommonCallActiveASPEntry = _CmqCommonCallActiveASPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1)
)
cmqCommonCallActiveASPEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPEntry.setStatus("current")
_CmqCommonCallActiveASPConnectionId_Type = CvcGUid
_CmqCommonCallActiveASPConnectionId_Object = MibTableColumn
cmqCommonCallActiveASPConnectionId = _CmqCommonCallActiveASPConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 1),
    _CmqCommonCallActiveASPConnectionId_Type()
)
cmqCommonCallActiveASPConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPConnectionId.setStatus("current")
_CmqCommonCallActiveASPCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqCommonCallActiveASPCallReferenceId_Object = MibTableColumn
cmqCommonCallActiveASPCallReferenceId = _CmqCommonCallActiveASPCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 2),
    _CmqCommonCallActiveASPCallReferenceId_Type()
)
cmqCommonCallActiveASPCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPCallReferenceId.setStatus("current")


class _CmqCommonCallActiveASPCallType_Type(Integer32):
    """Custom type cmqCommonCallActiveASPCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tdm", 1),
          ("voip", 2))
    )


_CmqCommonCallActiveASPCallType_Type.__name__ = "Integer32"
_CmqCommonCallActiveASPCallType_Object = MibTableColumn
cmqCommonCallActiveASPCallType = _CmqCommonCallActiveASPCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 3),
    _CmqCommonCallActiveASPCallType_Type()
)
cmqCommonCallActiveASPCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPCallType.setStatus("current")
_CmqCommonCallActiveASPEnabledMic_Type = TruthValue
_CmqCommonCallActiveASPEnabledMic_Object = MibTableColumn
cmqCommonCallActiveASPEnabledMic = _CmqCommonCallActiveASPEnabledMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 4),
    _CmqCommonCallActiveASPEnabledMic_Type()
)
cmqCommonCallActiveASPEnabledMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPEnabledMic.setStatus("current")
_CmqCommonCallActiveASPEnabledEar_Type = TruthValue
_CmqCommonCallActiveASPEnabledEar_Object = MibTableColumn
cmqCommonCallActiveASPEnabledEar = _CmqCommonCallActiveASPEnabledEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 5),
    _CmqCommonCallActiveASPEnabledEar_Type()
)
cmqCommonCallActiveASPEnabledEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPEnabledEar.setStatus("current")


class _CmqCommonCallActiveASPDirMic_Type(Integer32):
    """Custom type cmqCommonCallActiveASPDirMic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallActiveASPDirMic_Type.__name__ = "Integer32"
_CmqCommonCallActiveASPDirMic_Object = MibTableColumn
cmqCommonCallActiveASPDirMic = _CmqCommonCallActiveASPDirMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 6),
    _CmqCommonCallActiveASPDirMic_Type()
)
cmqCommonCallActiveASPDirMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPDirMic.setStatus("current")


class _CmqCommonCallActiveASPDirEar_Type(Integer32):
    """Custom type cmqCommonCallActiveASPDirEar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallActiveASPDirEar_Type.__name__ = "Integer32"
_CmqCommonCallActiveASPDirEar_Object = MibTableColumn
cmqCommonCallActiveASPDirEar = _CmqCommonCallActiveASPDirEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 7),
    _CmqCommonCallActiveASPDirEar_Type()
)
cmqCommonCallActiveASPDirEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPDirEar.setStatus("current")


class _CmqCommonCallActiveASPMode_Type(Integer32):
    """Custom type cmqCommonCallActiveASPMode based on Integer32"""
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
        *(("auto", 1),
          ("expert", 4),
          ("fast", 3),
          ("slow", 2))
    )


_CmqCommonCallActiveASPMode_Type.__name__ = "Integer32"
_CmqCommonCallActiveASPMode_Object = MibTableColumn
cmqCommonCallActiveASPMode = _CmqCommonCallActiveASPMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 8),
    _CmqCommonCallActiveASPMode_Type()
)
cmqCommonCallActiveASPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPMode.setStatus("current")
_CmqCommonCallActiveASPVer_Type = Unsigned32
_CmqCommonCallActiveASPVer_Object = MibTableColumn
cmqCommonCallActiveASPVer = _CmqCommonCallActiveASPVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 9),
    _CmqCommonCallActiveASPVer_Type()
)
cmqCommonCallActiveASPVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveASPVer.setStatus("current")
_CmqCommonCallActiveNumSigASPTriggMic_Type = Unsigned32
_CmqCommonCallActiveNumSigASPTriggMic_Object = MibTableColumn
cmqCommonCallActiveNumSigASPTriggMic = _CmqCommonCallActiveNumSigASPTriggMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 10),
    _CmqCommonCallActiveNumSigASPTriggMic_Type()
)
cmqCommonCallActiveNumSigASPTriggMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNumSigASPTriggMic.setStatus("current")
_CmqCommonCallActiveDurSigASPTriggMic_Type = Unsigned32
_CmqCommonCallActiveDurSigASPTriggMic_Object = MibTableColumn
cmqCommonCallActiveDurSigASPTriggMic = _CmqCommonCallActiveDurSigASPTriggMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 11),
    _CmqCommonCallActiveDurSigASPTriggMic_Type()
)
cmqCommonCallActiveDurSigASPTriggMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveDurSigASPTriggMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveDurSigASPTriggMic.setUnits("milliseconds")
_CmqCommonCallActiveTotNumASPTriggMic_Type = Unsigned32
_CmqCommonCallActiveTotNumASPTriggMic_Object = MibTableColumn
cmqCommonCallActiveTotNumASPTriggMic = _CmqCommonCallActiveTotNumASPTriggMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 12),
    _CmqCommonCallActiveTotNumASPTriggMic_Type()
)
cmqCommonCallActiveTotNumASPTriggMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveTotNumASPTriggMic.setStatus("current")
_CmqCommonCallActiveTotASPDurMic_Type = Unsigned32
_CmqCommonCallActiveTotASPDurMic_Object = MibTableColumn
cmqCommonCallActiveTotASPDurMic = _CmqCommonCallActiveTotASPDurMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 13),
    _CmqCommonCallActiveTotASPDurMic_Type()
)
cmqCommonCallActiveTotASPDurMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveTotASPDurMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveTotASPDurMic.setUnits("milliseconds")
_CmqCommonCallActiveLoudestFreqEstForLongEpiMic_Type = Unsigned32
_CmqCommonCallActiveLoudestFreqEstForLongEpiMic_Object = MibTableColumn
cmqCommonCallActiveLoudestFreqEstForLongEpiMic = _CmqCommonCallActiveLoudestFreqEstForLongEpiMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 14),
    _CmqCommonCallActiveLoudestFreqEstForLongEpiMic_Type()
)
cmqCommonCallActiveLoudestFreqEstForLongEpiMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLoudestFreqEstForLongEpiMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLoudestFreqEstForLongEpiMic.setUnits("frequency")
_CmqCommonCallActiveLongestDurEpiMic_Type = Unsigned32
_CmqCommonCallActiveLongestDurEpiMic_Object = MibTableColumn
cmqCommonCallActiveLongestDurEpiMic = _CmqCommonCallActiveLongestDurEpiMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 15),
    _CmqCommonCallActiveLongestDurEpiMic_Type()
)
cmqCommonCallActiveLongestDurEpiMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLongestDurEpiMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLongestDurEpiMic.setUnits("milliseconds")
_CmqCommonCallActiveNumSigASPTriggEar_Type = Unsigned32
_CmqCommonCallActiveNumSigASPTriggEar_Object = MibTableColumn
cmqCommonCallActiveNumSigASPTriggEar = _CmqCommonCallActiveNumSigASPTriggEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 16),
    _CmqCommonCallActiveNumSigASPTriggEar_Type()
)
cmqCommonCallActiveNumSigASPTriggEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveNumSigASPTriggEar.setStatus("current")
_CmqCommonCallActiveDurSigASPTriggEar_Type = Unsigned32
_CmqCommonCallActiveDurSigASPTriggEar_Object = MibTableColumn
cmqCommonCallActiveDurSigASPTriggEar = _CmqCommonCallActiveDurSigASPTriggEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 17),
    _CmqCommonCallActiveDurSigASPTriggEar_Type()
)
cmqCommonCallActiveDurSigASPTriggEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveDurSigASPTriggEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveDurSigASPTriggEar.setUnits("milliseconds")
_CmqCommonCallActiveTotNumASPTriggEar_Type = Unsigned32
_CmqCommonCallActiveTotNumASPTriggEar_Object = MibTableColumn
cmqCommonCallActiveTotNumASPTriggEar = _CmqCommonCallActiveTotNumASPTriggEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 18),
    _CmqCommonCallActiveTotNumASPTriggEar_Type()
)
cmqCommonCallActiveTotNumASPTriggEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveTotNumASPTriggEar.setStatus("current")
_CmqCommonCallActiveTotASPDurEar_Type = Unsigned32
_CmqCommonCallActiveTotASPDurEar_Object = MibTableColumn
cmqCommonCallActiveTotASPDurEar = _CmqCommonCallActiveTotASPDurEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 19),
    _CmqCommonCallActiveTotASPDurEar_Type()
)
cmqCommonCallActiveTotASPDurEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveTotASPDurEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveTotASPDurEar.setUnits("milliseconds")
_CmqCommonCallActiveLoudestFreqEstForLongEpiEar_Type = Unsigned32
_CmqCommonCallActiveLoudestFreqEstForLongEpiEar_Object = MibTableColumn
cmqCommonCallActiveLoudestFreqEstForLongEpiEar = _CmqCommonCallActiveLoudestFreqEstForLongEpiEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 20),
    _CmqCommonCallActiveLoudestFreqEstForLongEpiEar_Type()
)
cmqCommonCallActiveLoudestFreqEstForLongEpiEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLoudestFreqEstForLongEpiEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLoudestFreqEstForLongEpiEar.setUnits("frequency")
_CmqCommonCallActiveLongestDurEpiEar_Type = Unsigned32
_CmqCommonCallActiveLongestDurEpiEar_Object = MibTableColumn
cmqCommonCallActiveLongestDurEpiEar = _CmqCommonCallActiveLongestDurEpiEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 1, 3, 1, 21),
    _CmqCommonCallActiveLongestDurEpiEar_Type()
)
cmqCommonCallActiveLongestDurEpiEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLongestDurEpiEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallActiveLongestDurEpiEar.setUnits("milliseconds")
_CmqVoiceCallHistory_ObjectIdentity = ObjectIdentity
cmqVoiceCallHistory = _CmqVoiceCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2)
)
_CmqVoIPCallHistoryTable_Object = MibTable
cmqVoIPCallHistoryTable = _CmqVoIPCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTable.setStatus("current")
_CmqVoIPCallHistoryEntry_Object = MibTableRow
cmqVoIPCallHistoryEntry = _CmqVoIPCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1)
)
cmqVoIPCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryEntry.setStatus("current")
_CmqVoIPCallHistoryConnectionId_Type = CvcGUid
_CmqVoIPCallHistoryConnectionId_Object = MibTableColumn
cmqVoIPCallHistoryConnectionId = _CmqVoIPCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 1),
    _CmqVoIPCallHistoryConnectionId_Type()
)
cmqVoIPCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryConnectionId.setStatus("current")
_CmqVoIPCallHistoryCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqVoIPCallHistoryCallReferenceId_Object = MibTableColumn
cmqVoIPCallHistoryCallReferenceId = _CmqVoIPCallHistoryCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 2),
    _CmqVoIPCallHistoryCallReferenceId_Type()
)
cmqVoIPCallHistoryCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryCallReferenceId.setStatus("current")
_CmqVoIPCallHistoryRxCodecId_Type = CvcCoderTypeRate
_CmqVoIPCallHistoryRxCodecId_Object = MibTableColumn
cmqVoIPCallHistoryRxCodecId = _CmqVoIPCallHistoryRxCodecId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 3),
    _CmqVoIPCallHistoryRxCodecId_Type()
)
cmqVoIPCallHistoryRxCodecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxCodecId.setStatus("current")
_CmqVoIPCallHistoryRxSevConcealRatioPct_Type = Unsigned32
_CmqVoIPCallHistoryRxSevConcealRatioPct_Object = MibTableColumn
cmqVoIPCallHistoryRxSevConcealRatioPct = _CmqVoIPCallHistoryRxSevConcealRatioPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 4),
    _CmqVoIPCallHistoryRxSevConcealRatioPct_Type()
)
cmqVoIPCallHistoryRxSevConcealRatioPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxSevConcealRatioPct.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxSevConcealRatioPct.setUnits("percent")
_CmqVoIPCallHistoryRxCallConcealRatioPct_Type = Unsigned32
_CmqVoIPCallHistoryRxCallConcealRatioPct_Object = MibTableColumn
cmqVoIPCallHistoryRxCallConcealRatioPct = _CmqVoIPCallHistoryRxCallConcealRatioPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 5),
    _CmqVoIPCallHistoryRxCallConcealRatioPct_Type()
)
cmqVoIPCallHistoryRxCallConcealRatioPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxCallConcealRatioPct.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxCallConcealRatioPct.setUnits("percent")
_CmqVoIPCallHistoryRxPktLossRatioPct_Type = Unsigned32
_CmqVoIPCallHistoryRxPktLossRatioPct_Object = MibTableColumn
cmqVoIPCallHistoryRxPktLossRatioPct = _CmqVoIPCallHistoryRxPktLossRatioPct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 6),
    _CmqVoIPCallHistoryRxPktLossRatioPct_Type()
)
cmqVoIPCallHistoryRxPktLossRatioPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktLossRatioPct.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktLossRatioPct.setUnits("percent")
_CmqVoIPCallHistoryRxRoundTripTime_Type = Unsigned32
_CmqVoIPCallHistoryRxRoundTripTime_Object = MibTableColumn
cmqVoIPCallHistoryRxRoundTripTime = _CmqVoIPCallHistoryRxRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 7),
    _CmqVoIPCallHistoryRxRoundTripTime_Type()
)
cmqVoIPCallHistoryRxRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxRoundTripTime.setUnits("milliseconds")
_CmqVoIPCallHistoryRxCallDur_Type = Unsigned32
_CmqVoIPCallHistoryRxCallDur_Object = MibTableColumn
cmqVoIPCallHistoryRxCallDur = _CmqVoIPCallHistoryRxCallDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 8),
    _CmqVoIPCallHistoryRxCallDur_Type()
)
cmqVoIPCallHistoryRxCallDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxCallDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxCallDur.setUnits("milliseconds")
_CmqVoIPCallHistoryRxVoiceDur_Type = Unsigned32
_CmqVoIPCallHistoryRxVoiceDur_Object = MibTableColumn
cmqVoIPCallHistoryRxVoiceDur = _CmqVoIPCallHistoryRxVoiceDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 9),
    _CmqVoIPCallHistoryRxVoiceDur_Type()
)
cmqVoIPCallHistoryRxVoiceDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxVoiceDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxVoiceDur.setUnits("milliseconds")
_CmqVoIPCallHistoryRxPktLossConcealDur_Type = Unsigned32
_CmqVoIPCallHistoryRxPktLossConcealDur_Object = MibTableColumn
cmqVoIPCallHistoryRxPktLossConcealDur = _CmqVoIPCallHistoryRxPktLossConcealDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 10),
    _CmqVoIPCallHistoryRxPktLossConcealDur_Type()
)
cmqVoIPCallHistoryRxPktLossConcealDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktLossConcealDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktLossConcealDur.setUnits("milliseconds")
_CmqVoIPCallHistoryRxPktCntExpected_Type = Counter32
_CmqVoIPCallHistoryRxPktCntExpected_Object = MibTableColumn
cmqVoIPCallHistoryRxPktCntExpected = _CmqVoIPCallHistoryRxPktCntExpected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 11),
    _CmqVoIPCallHistoryRxPktCntExpected_Type()
)
cmqVoIPCallHistoryRxPktCntExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntExpected.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntExpected.setUnits("packets")
_CmqVoIPCallHistoryRxPktCntNotArrived_Type = Counter32
_CmqVoIPCallHistoryRxPktCntNotArrived_Object = MibTableColumn
cmqVoIPCallHistoryRxPktCntNotArrived = _CmqVoIPCallHistoryRxPktCntNotArrived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 12),
    _CmqVoIPCallHistoryRxPktCntNotArrived_Type()
)
cmqVoIPCallHistoryRxPktCntNotArrived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntNotArrived.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntNotArrived.setUnits("packets")
_CmqVoIPCallHistoryRxPktCntComfortNoise_Type = Counter32
_CmqVoIPCallHistoryRxPktCntComfortNoise_Object = MibTableColumn
cmqVoIPCallHistoryRxPktCntComfortNoise = _CmqVoIPCallHistoryRxPktCntComfortNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 13),
    _CmqVoIPCallHistoryRxPktCntComfortNoise_Type()
)
cmqVoIPCallHistoryRxPktCntComfortNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntComfortNoise.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntComfortNoise.setUnits("packets")
_CmqVoIPCallHistoryRxPktCntUnusableLate_Type = Counter32
_CmqVoIPCallHistoryRxPktCntUnusableLate_Object = MibTableColumn
cmqVoIPCallHistoryRxPktCntUnusableLate = _CmqVoIPCallHistoryRxPktCntUnusableLate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 14),
    _CmqVoIPCallHistoryRxPktCntUnusableLate_Type()
)
cmqVoIPCallHistoryRxPktCntUnusableLate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntUnusableLate.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntUnusableLate.setUnits("packets")
_CmqVoIPCallHistoryRxPktCntDiscarded_Type = Counter32
_CmqVoIPCallHistoryRxPktCntDiscarded_Object = MibTableColumn
cmqVoIPCallHistoryRxPktCntDiscarded = _CmqVoIPCallHistoryRxPktCntDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 15),
    _CmqVoIPCallHistoryRxPktCntDiscarded_Type()
)
cmqVoIPCallHistoryRxPktCntDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntDiscarded.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntDiscarded.setUnits("packets")
_CmqVoIPCallHistoryRxPktCntEffLoss_Type = Counter32
_CmqVoIPCallHistoryRxPktCntEffLoss_Object = MibTableColumn
cmqVoIPCallHistoryRxPktCntEffLoss = _CmqVoIPCallHistoryRxPktCntEffLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 16),
    _CmqVoIPCallHistoryRxPktCntEffLoss_Type()
)
cmqVoIPCallHistoryRxPktCntEffLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntEffLoss.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPktCntEffLoss.setUnits("packets")
_CmqVoIPCallHistoryRxUnimpairedSecOK_Type = Counter32
_CmqVoIPCallHistoryRxUnimpairedSecOK_Object = MibTableColumn
cmqVoIPCallHistoryRxUnimpairedSecOK = _CmqVoIPCallHistoryRxUnimpairedSecOK_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 17),
    _CmqVoIPCallHistoryRxUnimpairedSecOK_Type()
)
cmqVoIPCallHistoryRxUnimpairedSecOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxUnimpairedSecOK.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxUnimpairedSecOK.setUnits("seconds")
_CmqVoIPCallHistoryRxConcealSec_Type = Counter32
_CmqVoIPCallHistoryRxConcealSec_Object = MibTableColumn
cmqVoIPCallHistoryRxConcealSec = _CmqVoIPCallHistoryRxConcealSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 18),
    _CmqVoIPCallHistoryRxConcealSec_Type()
)
cmqVoIPCallHistoryRxConcealSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxConcealSec.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxConcealSec.setUnits("seconds")
_CmqVoIPCallHistoryRxSevConcealSec_Type = Counter32
_CmqVoIPCallHistoryRxSevConcealSec_Object = MibTableColumn
cmqVoIPCallHistoryRxSevConcealSec = _CmqVoIPCallHistoryRxSevConcealSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 19),
    _CmqVoIPCallHistoryRxSevConcealSec_Type()
)
cmqVoIPCallHistoryRxSevConcealSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxSevConcealSec.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxSevConcealSec.setUnits("seconds")


class _CmqVoIPCallHistoryRxJBufMode_Type(Integer32):
    """Custom type cmqVoIPCallHistoryRxJBufMode based on Integer32"""
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
        *(("adaptive", 1),
          ("disabled", 4),
          ("fixed", 2),
          ("unknown", 3))
    )


_CmqVoIPCallHistoryRxJBufMode_Type.__name__ = "Integer32"
_CmqVoIPCallHistoryRxJBufMode_Object = MibTableColumn
cmqVoIPCallHistoryRxJBufMode = _CmqVoIPCallHistoryRxJBufMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 20),
    _CmqVoIPCallHistoryRxJBufMode_Type()
)
cmqVoIPCallHistoryRxJBufMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBufMode.setStatus("current")
_CmqVoIPCallHistoryRxJBufNomDelay_Type = Unsigned32
_CmqVoIPCallHistoryRxJBufNomDelay_Object = MibTableColumn
cmqVoIPCallHistoryRxJBufNomDelay = _CmqVoIPCallHistoryRxJBufNomDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 21),
    _CmqVoIPCallHistoryRxJBufNomDelay_Type()
)
cmqVoIPCallHistoryRxJBufNomDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBufNomDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBufNomDelay.setUnits("milliseconds")
_CmqVoIPCallHistoryRxJBufDlyNow_Type = Unsigned32
_CmqVoIPCallHistoryRxJBufDlyNow_Object = MibTableColumn
cmqVoIPCallHistoryRxJBufDlyNow = _CmqVoIPCallHistoryRxJBufDlyNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 22),
    _CmqVoIPCallHistoryRxJBufDlyNow_Type()
)
cmqVoIPCallHistoryRxJBufDlyNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBufDlyNow.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBufDlyNow.setUnits("milliseconds")
_CmqVoIPCallHistoryRxJBufLowWater_Type = Unsigned32
_CmqVoIPCallHistoryRxJBufLowWater_Object = MibTableColumn
cmqVoIPCallHistoryRxJBufLowWater = _CmqVoIPCallHistoryRxJBufLowWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 23),
    _CmqVoIPCallHistoryRxJBufLowWater_Type()
)
cmqVoIPCallHistoryRxJBufLowWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBufLowWater.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBufLowWater.setUnits("milliseconds")
_CmqVoIPCallHistoryRxJBuffHiWater_Type = Unsigned32
_CmqVoIPCallHistoryRxJBuffHiWater_Object = MibTableColumn
cmqVoIPCallHistoryRxJBuffHiWater = _CmqVoIPCallHistoryRxJBuffHiWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 24),
    _CmqVoIPCallHistoryRxJBuffHiWater_Type()
)
cmqVoIPCallHistoryRxJBuffHiWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBuffHiWater.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxJBuffHiWater.setUnits("milliseconds")
_CmqVoIPCallHistory3550JShortTermAvg_Type = Unsigned32
_CmqVoIPCallHistory3550JShortTermAvg_Object = MibTableColumn
cmqVoIPCallHistory3550JShortTermAvg = _CmqVoIPCallHistory3550JShortTermAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 25),
    _CmqVoIPCallHistory3550JShortTermAvg_Type()
)
cmqVoIPCallHistory3550JShortTermAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistory3550JShortTermAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistory3550JShortTermAvg.setUnits("milliseconds")
_CmqVoIPCallHistory3550JCallAvg_Type = Unsigned32
_CmqVoIPCallHistory3550JCallAvg_Object = MibTableColumn
cmqVoIPCallHistory3550JCallAvg = _CmqVoIPCallHistory3550JCallAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 26),
    _CmqVoIPCallHistory3550JCallAvg_Type()
)
cmqVoIPCallHistory3550JCallAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistory3550JCallAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistory3550JCallAvg.setUnits("milliseconds")
_CmqVoIPCallHistoryRxSignalLvl_Type = Integer32
_CmqVoIPCallHistoryRxSignalLvl_Object = MibTableColumn
cmqVoIPCallHistoryRxSignalLvl = _CmqVoIPCallHistoryRxSignalLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 27),
    _CmqVoIPCallHistoryRxSignalLvl_Type()
)
cmqVoIPCallHistoryRxSignalLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxSignalLvl.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxSignalLvl.setUnits("0.1 dB")
_CmqVoIPCallHistoryRxPred107Rscore_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107Rscore_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107Rscore = _CmqVoIPCallHistoryRxPred107Rscore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 28),
    _CmqVoIPCallHistoryRxPred107Rscore_Type()
)
cmqVoIPCallHistoryRxPred107Rscore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107Rscore.setStatus("current")
_CmqVoIPCallHistoryRxPred107RMosListen_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107RMosListen_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107RMosListen = _CmqVoIPCallHistoryRxPred107RMosListen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 29),
    _CmqVoIPCallHistoryRxPred107RMosListen_Type()
)
cmqVoIPCallHistoryRxPred107RMosListen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107RMosListen.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107RMosListen.setUnits("percent")
_CmqVoIPCallHistoryRxPred107RScoreConv_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107RScoreConv_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107RScoreConv = _CmqVoIPCallHistoryRxPred107RScoreConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 30),
    _CmqVoIPCallHistoryRxPred107RScoreConv_Type()
)
cmqVoIPCallHistoryRxPred107RScoreConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107RScoreConv.setStatus("current")
_CmqVoIPCallHistoryRxPred107RMosConv_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107RMosConv_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107RMosConv = _CmqVoIPCallHistoryRxPred107RMosConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 31),
    _CmqVoIPCallHistoryRxPred107RMosConv_Type()
)
cmqVoIPCallHistoryRxPred107RMosConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107RMosConv.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107RMosConv.setUnits("percent")
_CmqVoIPCallHistoryRxPred107CodecIeBase_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107CodecIeBase_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107CodecIeBase = _CmqVoIPCallHistoryRxPred107CodecIeBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 32),
    _CmqVoIPCallHistoryRxPred107CodecIeBase_Type()
)
cmqVoIPCallHistoryRxPred107CodecIeBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107CodecIeBase.setStatus("current")
_CmqVoIPCallHistoryRxPred107CodecBPL_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107CodecBPL_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107CodecBPL = _CmqVoIPCallHistoryRxPred107CodecBPL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 33),
    _CmqVoIPCallHistoryRxPred107CodecBPL_Type()
)
cmqVoIPCallHistoryRxPred107CodecBPL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107CodecBPL.setStatus("current")
_CmqVoIPCallHistoryRxPred107DefaultR0_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107DefaultR0_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107DefaultR0 = _CmqVoIPCallHistoryRxPred107DefaultR0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 34),
    _CmqVoIPCallHistoryRxPred107DefaultR0_Type()
)
cmqVoIPCallHistoryRxPred107DefaultR0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107DefaultR0.setStatus("current")
_CmqVoIPCallHistoryRxPred107IeEff_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107IeEff_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107IeEff = _CmqVoIPCallHistoryRxPred107IeEff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 35),
    _CmqVoIPCallHistoryRxPred107IeEff_Type()
)
cmqVoIPCallHistoryRxPred107IeEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107IeEff.setStatus("current")
_CmqVoIPCallHistoryRxPred107Idd_Type = Unsigned32
_CmqVoIPCallHistoryRxPred107Idd_Object = MibTableColumn
cmqVoIPCallHistoryRxPred107Idd = _CmqVoIPCallHistoryRxPred107Idd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 36),
    _CmqVoIPCallHistoryRxPred107Idd_Type()
)
cmqVoIPCallHistoryRxPred107Idd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPred107Idd.setStatus("current")
_CmqVoIPCallHistoryRxPredMosLqoAvg_Type = Unsigned32
_CmqVoIPCallHistoryRxPredMosLqoAvg_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoAvg = _CmqVoIPCallHistoryRxPredMosLqoAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 37),
    _CmqVoIPCallHistoryRxPredMosLqoAvg_Type()
)
cmqVoIPCallHistoryRxPredMosLqoAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoAvg.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoAvg.setUnits("percent")
_CmqVoIPCallHistoryRxPredMosLqoRecent_Type = Unsigned32
_CmqVoIPCallHistoryRxPredMosLqoRecent_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoRecent = _CmqVoIPCallHistoryRxPredMosLqoRecent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 38),
    _CmqVoIPCallHistoryRxPredMosLqoRecent_Type()
)
cmqVoIPCallHistoryRxPredMosLqoRecent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoRecent.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoRecent.setUnits("percent")
_CmqVoIPCallHistoryRxPredMosLqoBaseline_Type = Unsigned32
_CmqVoIPCallHistoryRxPredMosLqoBaseline_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoBaseline = _CmqVoIPCallHistoryRxPredMosLqoBaseline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 39),
    _CmqVoIPCallHistoryRxPredMosLqoBaseline_Type()
)
cmqVoIPCallHistoryRxPredMosLqoBaseline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoBaseline.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoBaseline.setUnits("percent")
_CmqVoIPCallHistoryRxPredMosLqoMin_Type = Unsigned32
_CmqVoIPCallHistoryRxPredMosLqoMin_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoMin = _CmqVoIPCallHistoryRxPredMosLqoMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 40),
    _CmqVoIPCallHistoryRxPredMosLqoMin_Type()
)
cmqVoIPCallHistoryRxPredMosLqoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoMin.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoMin.setUnits("percent")
_CmqVoIPCallHistoryRxPredMosLqoNumWin_Type = Unsigned32
_CmqVoIPCallHistoryRxPredMosLqoNumWin_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoNumWin = _CmqVoIPCallHistoryRxPredMosLqoNumWin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 41),
    _CmqVoIPCallHistoryRxPredMosLqoNumWin_Type()
)
cmqVoIPCallHistoryRxPredMosLqoNumWin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoNumWin.setStatus("current")
_CmqVoIPCallHistoryRxPredMosLqoBursts_Type = Unsigned32
_CmqVoIPCallHistoryRxPredMosLqoBursts_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoBursts = _CmqVoIPCallHistoryRxPredMosLqoBursts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 42),
    _CmqVoIPCallHistoryRxPredMosLqoBursts_Type()
)
cmqVoIPCallHistoryRxPredMosLqoBursts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoBursts.setStatus("current")
_CmqVoIPCallHistoryRxPredMosLqoFrLoss_Type = Unsigned32
_CmqVoIPCallHistoryRxPredMosLqoFrLoss_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoFrLoss = _CmqVoIPCallHistoryRxPredMosLqoFrLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 43),
    _CmqVoIPCallHistoryRxPredMosLqoFrLoss_Type()
)
cmqVoIPCallHistoryRxPredMosLqoFrLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoFrLoss.setStatus("current")


class _CmqVoIPCallHistoryRxPredMosLqoVerID_Type(SnmpAdminString):
    """Custom type cmqVoIPCallHistoryRxPredMosLqoVerID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmqVoIPCallHistoryRxPredMosLqoVerID_Type.__name__ = "SnmpAdminString"
_CmqVoIPCallHistoryRxPredMosLqoVerID_Object = MibTableColumn
cmqVoIPCallHistoryRxPredMosLqoVerID = _CmqVoIPCallHistoryRxPredMosLqoVerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 44),
    _CmqVoIPCallHistoryRxPredMosLqoVerID_Type()
)
cmqVoIPCallHistoryRxPredMosLqoVerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryRxPredMosLqoVerID.setStatus("current")
_CmqVoIPCallHistoryTxCodecId_Type = CvcCoderTypeRate
_CmqVoIPCallHistoryTxCodecId_Object = MibTableColumn
cmqVoIPCallHistoryTxCodecId = _CmqVoIPCallHistoryTxCodecId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 45),
    _CmqVoIPCallHistoryTxCodecId_Type()
)
cmqVoIPCallHistoryTxCodecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxCodecId.setStatus("current")
_CmqVoIPCallHistoryTxVadEnabled_Type = TruthValue
_CmqVoIPCallHistoryTxVadEnabled_Object = MibTableColumn
cmqVoIPCallHistoryTxVadEnabled = _CmqVoIPCallHistoryTxVadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 46),
    _CmqVoIPCallHistoryTxVadEnabled_Type()
)
cmqVoIPCallHistoryTxVadEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxVadEnabled.setStatus("current")
_CmqVoIPCallHistoryTxTmrCallDur_Type = Unsigned32
_CmqVoIPCallHistoryTxTmrCallDur_Object = MibTableColumn
cmqVoIPCallHistoryTxTmrCallDur = _CmqVoIPCallHistoryTxTmrCallDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 47),
    _CmqVoIPCallHistoryTxTmrCallDur_Type()
)
cmqVoIPCallHistoryTxTmrCallDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxTmrCallDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxTmrCallDur.setUnits("milliseconds")
_CmqVoIPCallHistoryTxTmrActSpeechDur_Type = Unsigned32
_CmqVoIPCallHistoryTxTmrActSpeechDur_Object = MibTableColumn
cmqVoIPCallHistoryTxTmrActSpeechDur = _CmqVoIPCallHistoryTxTmrActSpeechDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 48),
    _CmqVoIPCallHistoryTxTmrActSpeechDur_Type()
)
cmqVoIPCallHistoryTxTmrActSpeechDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxTmrActSpeechDur.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxTmrActSpeechDur.setUnits("milliseconds")
_CmqVoIPCallHistoryTxSignalLvl_Type = Integer32
_CmqVoIPCallHistoryTxSignalLvl_Object = MibTableColumn
cmqVoIPCallHistoryTxSignalLvl = _CmqVoIPCallHistoryTxSignalLvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 49),
    _CmqVoIPCallHistoryTxSignalLvl_Type()
)
cmqVoIPCallHistoryTxSignalLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxSignalLvl.setStatus("current")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxSignalLvl.setUnits("0.1 dB")
_CmqVoIPCallHistoryTxNoiseFloor_Type = Integer32
_CmqVoIPCallHistoryTxNoiseFloor_Object = MibTableColumn
cmqVoIPCallHistoryTxNoiseFloor = _CmqVoIPCallHistoryTxNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 1, 1, 50),
    _CmqVoIPCallHistoryTxNoiseFloor_Type()
)
cmqVoIPCallHistoryTxNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVoIPCallHistoryTxNoiseFloor.setStatus("current")
_CmqCommonCallHistoryNRTable_Object = MibTable
cmqCommonCallHistoryNRTable = _CmqCommonCallHistoryNRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRTable.setStatus("current")
_CmqCommonCallHistoryNREntry_Object = MibTableRow
cmqCommonCallHistoryNREntry = _CmqCommonCallHistoryNREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1)
)
cmqCommonCallHistoryNREntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNREntry.setStatus("current")
_CmqCommonCallHistoryNRConnectionId_Type = CvcGUid
_CmqCommonCallHistoryNRConnectionId_Object = MibTableColumn
cmqCommonCallHistoryNRConnectionId = _CmqCommonCallHistoryNRConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 1),
    _CmqCommonCallHistoryNRConnectionId_Type()
)
cmqCommonCallHistoryNRConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRConnectionId.setStatus("current")
_CmqCommonCallHistoryNRCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqCommonCallHistoryNRCallReferenceId_Object = MibTableColumn
cmqCommonCallHistoryNRCallReferenceId = _CmqCommonCallHistoryNRCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 2),
    _CmqCommonCallHistoryNRCallReferenceId_Type()
)
cmqCommonCallHistoryNRCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRCallReferenceId.setStatus("current")


class _CmqCommonCallHistoryNRCallType_Type(Integer32):
    """Custom type cmqCommonCallHistoryNRCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tdm", 1),
          ("voip", 2))
    )


_CmqCommonCallHistoryNRCallType_Type.__name__ = "Integer32"
_CmqCommonCallHistoryNRCallType_Object = MibTableColumn
cmqCommonCallHistoryNRCallType = _CmqCommonCallHistoryNRCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 3),
    _CmqCommonCallHistoryNRCallType_Type()
)
cmqCommonCallHistoryNRCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRCallType.setStatus("current")
_CmqCommonCallHistoryNREnabledMic_Type = TruthValue
_CmqCommonCallHistoryNREnabledMic_Object = MibTableColumn
cmqCommonCallHistoryNREnabledMic = _CmqCommonCallHistoryNREnabledMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 4),
    _CmqCommonCallHistoryNREnabledMic_Type()
)
cmqCommonCallHistoryNREnabledMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNREnabledMic.setStatus("current")
_CmqCommonCallHistoryNREnabledEar_Type = TruthValue
_CmqCommonCallHistoryNREnabledEar_Object = MibTableColumn
cmqCommonCallHistoryNREnabledEar = _CmqCommonCallHistoryNREnabledEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 5),
    _CmqCommonCallHistoryNREnabledEar_Type()
)
cmqCommonCallHistoryNREnabledEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNREnabledEar.setStatus("current")


class _CmqCommonCallHistoryNRDirMic_Type(Integer32):
    """Custom type cmqCommonCallHistoryNRDirMic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallHistoryNRDirMic_Type.__name__ = "Integer32"
_CmqCommonCallHistoryNRDirMic_Object = MibTableColumn
cmqCommonCallHistoryNRDirMic = _CmqCommonCallHistoryNRDirMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 6),
    _CmqCommonCallHistoryNRDirMic_Type()
)
cmqCommonCallHistoryNRDirMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRDirMic.setStatus("current")


class _CmqCommonCallHistoryNRDirEar_Type(Integer32):
    """Custom type cmqCommonCallHistoryNRDirEar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallHistoryNRDirEar_Type.__name__ = "Integer32"
_CmqCommonCallHistoryNRDirEar_Object = MibTableColumn
cmqCommonCallHistoryNRDirEar = _CmqCommonCallHistoryNRDirEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 7),
    _CmqCommonCallHistoryNRDirEar_Type()
)
cmqCommonCallHistoryNRDirEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRDirEar.setStatus("current")
_CmqCommonCallHistoryNRLibVer_Type = Unsigned32
_CmqCommonCallHistoryNRLibVer_Object = MibTableColumn
cmqCommonCallHistoryNRLibVer = _CmqCommonCallHistoryNRLibVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 8),
    _CmqCommonCallHistoryNRLibVer_Type()
)
cmqCommonCallHistoryNRLibVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRLibVer.setStatus("current")


class _CmqCommonCallHistoryNRIntensity_Type(Integer32):
    """Custom type cmqCommonCallHistoryNRIntensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_CmqCommonCallHistoryNRIntensity_Type.__name__ = "Integer32"
_CmqCommonCallHistoryNRIntensity_Object = MibTableColumn
cmqCommonCallHistoryNRIntensity = _CmqCommonCallHistoryNRIntensity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 9),
    _CmqCommonCallHistoryNRIntensity_Type()
)
cmqCommonCallHistoryNRIntensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNRIntensity.setStatus("current")
_CmqCommonCallHistoryPreNRNoiseFloorEstMic_Type = Integer32
_CmqCommonCallHistoryPreNRNoiseFloorEstMic_Object = MibTableColumn
cmqCommonCallHistoryPreNRNoiseFloorEstMic = _CmqCommonCallHistoryPreNRNoiseFloorEstMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 10),
    _CmqCommonCallHistoryPreNRNoiseFloorEstMic_Type()
)
cmqCommonCallHistoryPreNRNoiseFloorEstMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPreNRNoiseFloorEstMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPreNRNoiseFloorEstMic.setUnits("0.1 dB")
_CmqCommonCallHistoryPostNRNoiseFloorEstMic_Type = Integer32
_CmqCommonCallHistoryPostNRNoiseFloorEstMic_Object = MibTableColumn
cmqCommonCallHistoryPostNRNoiseFloorEstMic = _CmqCommonCallHistoryPostNRNoiseFloorEstMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 11),
    _CmqCommonCallHistoryPostNRNoiseFloorEstMic_Type()
)
cmqCommonCallHistoryPostNRNoiseFloorEstMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPostNRNoiseFloorEstMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPostNRNoiseFloorEstMic.setUnits("0.1 dB")
_CmqCommonCallHistoryPreNRNoiseFloorEstEar_Type = Integer32
_CmqCommonCallHistoryPreNRNoiseFloorEstEar_Object = MibTableColumn
cmqCommonCallHistoryPreNRNoiseFloorEstEar = _CmqCommonCallHistoryPreNRNoiseFloorEstEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 12),
    _CmqCommonCallHistoryPreNRNoiseFloorEstEar_Type()
)
cmqCommonCallHistoryPreNRNoiseFloorEstEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPreNRNoiseFloorEstEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPreNRNoiseFloorEstEar.setUnits("0.1 dB")
_CmqCommonCallHistoryPostNRNoiseFloorEstEar_Type = Integer32
_CmqCommonCallHistoryPostNRNoiseFloorEstEar_Object = MibTableColumn
cmqCommonCallHistoryPostNRNoiseFloorEstEar = _CmqCommonCallHistoryPostNRNoiseFloorEstEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 2, 1, 13),
    _CmqCommonCallHistoryPostNRNoiseFloorEstEar_Type()
)
cmqCommonCallHistoryPostNRNoiseFloorEstEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPostNRNoiseFloorEstEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryPostNRNoiseFloorEstEar.setUnits("0.1 dB")
_CmqCommonCallHistoryASPTable_Object = MibTable
cmqCommonCallHistoryASPTable = _CmqCommonCallHistoryASPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPTable.setStatus("current")
_CmqCommonCallHistoryASPEntry_Object = MibTableRow
cmqCommonCallHistoryASPEntry = _CmqCommonCallHistoryASPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1)
)
cmqCommonCallHistoryASPEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPEntry.setStatus("current")
_CmqCommonCallHistoryASPConnectionId_Type = CvcGUid
_CmqCommonCallHistoryASPConnectionId_Object = MibTableColumn
cmqCommonCallHistoryASPConnectionId = _CmqCommonCallHistoryASPConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 1),
    _CmqCommonCallHistoryASPConnectionId_Type()
)
cmqCommonCallHistoryASPConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPConnectionId.setStatus("current")
_CmqCommonCallHistoryASPCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqCommonCallHistoryASPCallReferenceId_Object = MibTableColumn
cmqCommonCallHistoryASPCallReferenceId = _CmqCommonCallHistoryASPCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 2),
    _CmqCommonCallHistoryASPCallReferenceId_Type()
)
cmqCommonCallHistoryASPCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPCallReferenceId.setStatus("current")


class _CmqCommonCallHistoryASPCallType_Type(Integer32):
    """Custom type cmqCommonCallHistoryASPCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tdm", 1),
          ("voip", 2))
    )


_CmqCommonCallHistoryASPCallType_Type.__name__ = "Integer32"
_CmqCommonCallHistoryASPCallType_Object = MibTableColumn
cmqCommonCallHistoryASPCallType = _CmqCommonCallHistoryASPCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 3),
    _CmqCommonCallHistoryASPCallType_Type()
)
cmqCommonCallHistoryASPCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPCallType.setStatus("current")


class _CmqCommonCallHistoryASPEnabledMic_Type(TruthValue):
    """Custom type cmqCommonCallHistoryASPEnabledMic based on TruthValue"""


_CmqCommonCallHistoryASPEnabledMic_Object = MibTableColumn
cmqCommonCallHistoryASPEnabledMic = _CmqCommonCallHistoryASPEnabledMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 4),
    _CmqCommonCallHistoryASPEnabledMic_Type()
)
cmqCommonCallHistoryASPEnabledMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPEnabledMic.setStatus("current")
_CmqCommonCallHistoryASPEnabledEar_Type = TruthValue
_CmqCommonCallHistoryASPEnabledEar_Object = MibTableColumn
cmqCommonCallHistoryASPEnabledEar = _CmqCommonCallHistoryASPEnabledEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 5),
    _CmqCommonCallHistoryASPEnabledEar_Type()
)
cmqCommonCallHistoryASPEnabledEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPEnabledEar.setStatus("current")


class _CmqCommonCallHistoryASPDirMic_Type(Integer32):
    """Custom type cmqCommonCallHistoryASPDirMic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallHistoryASPDirMic_Type.__name__ = "Integer32"
_CmqCommonCallHistoryASPDirMic_Object = MibTableColumn
cmqCommonCallHistoryASPDirMic = _CmqCommonCallHistoryASPDirMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 6),
    _CmqCommonCallHistoryASPDirMic_Type()
)
cmqCommonCallHistoryASPDirMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPDirMic.setStatus("current")


class _CmqCommonCallHistoryASPDirEar_Type(Integer32):
    """Custom type cmqCommonCallHistoryASPDirEar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lan", 3),
          ("tdm", 1),
          ("wan", 2))
    )


_CmqCommonCallHistoryASPDirEar_Type.__name__ = "Integer32"
_CmqCommonCallHistoryASPDirEar_Object = MibTableColumn
cmqCommonCallHistoryASPDirEar = _CmqCommonCallHistoryASPDirEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 7),
    _CmqCommonCallHistoryASPDirEar_Type()
)
cmqCommonCallHistoryASPDirEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPDirEar.setStatus("current")


class _CmqCommonCallHistoryASPMode_Type(Integer32):
    """Custom type cmqCommonCallHistoryASPMode based on Integer32"""
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
        *(("auto", 1),
          ("expert", 4),
          ("fast", 3),
          ("slow", 2))
    )


_CmqCommonCallHistoryASPMode_Type.__name__ = "Integer32"
_CmqCommonCallHistoryASPMode_Object = MibTableColumn
cmqCommonCallHistoryASPMode = _CmqCommonCallHistoryASPMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 8),
    _CmqCommonCallHistoryASPMode_Type()
)
cmqCommonCallHistoryASPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPMode.setStatus("current")
_CmqCommonCallHistoryASPVer_Type = Integer32
_CmqCommonCallHistoryASPVer_Object = MibTableColumn
cmqCommonCallHistoryASPVer = _CmqCommonCallHistoryASPVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 9),
    _CmqCommonCallHistoryASPVer_Type()
)
cmqCommonCallHistoryASPVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryASPVer.setStatus("current")
_CmqCommonCallHistoryNumSigASPTriggMic_Type = Unsigned32
_CmqCommonCallHistoryNumSigASPTriggMic_Object = MibTableColumn
cmqCommonCallHistoryNumSigASPTriggMic = _CmqCommonCallHistoryNumSigASPTriggMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 10),
    _CmqCommonCallHistoryNumSigASPTriggMic_Type()
)
cmqCommonCallHistoryNumSigASPTriggMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNumSigASPTriggMic.setStatus("current")
_CmqCommonCallHistoryDurSigASPTriggMic_Type = Unsigned32
_CmqCommonCallHistoryDurSigASPTriggMic_Object = MibTableColumn
cmqCommonCallHistoryDurSigASPTriggMic = _CmqCommonCallHistoryDurSigASPTriggMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 11),
    _CmqCommonCallHistoryDurSigASPTriggMic_Type()
)
cmqCommonCallHistoryDurSigASPTriggMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryDurSigASPTriggMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryDurSigASPTriggMic.setUnits("milliseconds")
_CmqCommonCallHistoryTotNumASPTriggMic_Type = Unsigned32
_CmqCommonCallHistoryTotNumASPTriggMic_Object = MibTableColumn
cmqCommonCallHistoryTotNumASPTriggMic = _CmqCommonCallHistoryTotNumASPTriggMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 12),
    _CmqCommonCallHistoryTotNumASPTriggMic_Type()
)
cmqCommonCallHistoryTotNumASPTriggMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryTotNumASPTriggMic.setStatus("current")
_CmqCommonCallHistoryTotASPDurMic_Type = Unsigned32
_CmqCommonCallHistoryTotASPDurMic_Object = MibTableColumn
cmqCommonCallHistoryTotASPDurMic = _CmqCommonCallHistoryTotASPDurMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 13),
    _CmqCommonCallHistoryTotASPDurMic_Type()
)
cmqCommonCallHistoryTotASPDurMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryTotASPDurMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryTotASPDurMic.setUnits("milliseconds")
_CmqCommonCallHistoryLoudestFreqEstForLongEpiMic_Type = Unsigned32
_CmqCommonCallHistoryLoudestFreqEstForLongEpiMic_Object = MibTableColumn
cmqCommonCallHistoryLoudestFreqEstForLongEpiMic = _CmqCommonCallHistoryLoudestFreqEstForLongEpiMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 14),
    _CmqCommonCallHistoryLoudestFreqEstForLongEpiMic_Type()
)
cmqCommonCallHistoryLoudestFreqEstForLongEpiMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLoudestFreqEstForLongEpiMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLoudestFreqEstForLongEpiMic.setUnits("frequency")
_CmqCommonCallHistoryLongestDurEpiMic_Type = Unsigned32
_CmqCommonCallHistoryLongestDurEpiMic_Object = MibTableColumn
cmqCommonCallHistoryLongestDurEpiMic = _CmqCommonCallHistoryLongestDurEpiMic_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 15),
    _CmqCommonCallHistoryLongestDurEpiMic_Type()
)
cmqCommonCallHistoryLongestDurEpiMic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLongestDurEpiMic.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLongestDurEpiMic.setUnits("milliseconds")
_CmqCommonCallHistoryNumSigASPTriggEar_Type = Unsigned32
_CmqCommonCallHistoryNumSigASPTriggEar_Object = MibTableColumn
cmqCommonCallHistoryNumSigASPTriggEar = _CmqCommonCallHistoryNumSigASPTriggEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 16),
    _CmqCommonCallHistoryNumSigASPTriggEar_Type()
)
cmqCommonCallHistoryNumSigASPTriggEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryNumSigASPTriggEar.setStatus("current")
_CmqCommonCallHistoryDurSigASPTriggEar_Type = Unsigned32
_CmqCommonCallHistoryDurSigASPTriggEar_Object = MibTableColumn
cmqCommonCallHistoryDurSigASPTriggEar = _CmqCommonCallHistoryDurSigASPTriggEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 17),
    _CmqCommonCallHistoryDurSigASPTriggEar_Type()
)
cmqCommonCallHistoryDurSigASPTriggEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryDurSigASPTriggEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryDurSigASPTriggEar.setUnits("milliseconds")
_CmqCommonCallHistoryTotNumASPTriggEar_Type = Unsigned32
_CmqCommonCallHistoryTotNumASPTriggEar_Object = MibTableColumn
cmqCommonCallHistoryTotNumASPTriggEar = _CmqCommonCallHistoryTotNumASPTriggEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 18),
    _CmqCommonCallHistoryTotNumASPTriggEar_Type()
)
cmqCommonCallHistoryTotNumASPTriggEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryTotNumASPTriggEar.setStatus("current")
_CmqCommonCallHistoryTotASPDurEar_Type = Unsigned32
_CmqCommonCallHistoryTotASPDurEar_Object = MibTableColumn
cmqCommonCallHistoryTotASPDurEar = _CmqCommonCallHistoryTotASPDurEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 19),
    _CmqCommonCallHistoryTotASPDurEar_Type()
)
cmqCommonCallHistoryTotASPDurEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryTotASPDurEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryTotASPDurEar.setUnits("milliseconds")
_CmqCommonCallHistoryLoudestFreqEstForLongEpiEar_Type = Unsigned32
_CmqCommonCallHistoryLoudestFreqEstForLongEpiEar_Object = MibTableColumn
cmqCommonCallHistoryLoudestFreqEstForLongEpiEar = _CmqCommonCallHistoryLoudestFreqEstForLongEpiEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 20),
    _CmqCommonCallHistoryLoudestFreqEstForLongEpiEar_Type()
)
cmqCommonCallHistoryLoudestFreqEstForLongEpiEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLoudestFreqEstForLongEpiEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLoudestFreqEstForLongEpiEar.setUnits("frequency")
_CmqCommonCallHistoryLongestDurEpiEar_Type = Unsigned32
_CmqCommonCallHistoryLongestDurEpiEar_Object = MibTableColumn
cmqCommonCallHistoryLongestDurEpiEar = _CmqCommonCallHistoryLongestDurEpiEar_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 2, 3, 1, 21),
    _CmqCommonCallHistoryLongestDurEpiEar_Type()
)
cmqCommonCallHistoryLongestDurEpiEar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLongestDurEpiEar.setStatus("current")
if mibBuilder.loadTexts:
    cmqCommonCallHistoryLongestDurEpiEar.setUnits("milliseconds")
_CmqVideoCallActive_ObjectIdentity = ObjectIdentity
cmqVideoCallActive = _CmqVideoCallActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3)
)
_CmqVideoCallActiveTable_Object = MibTable
cmqVideoCallActiveTable = _CmqVideoCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmqVideoCallActiveTable.setStatus("current")
_CmqVideoCallActiveEntry_Object = MibTableRow
cmqVideoCallActiveEntry = _CmqVideoCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1)
)
cmqVideoCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cmqVideoCallActiveEntry.setStatus("current")
_CmqVideoCallActiveConnectionId_Type = CvcGUid
_CmqVideoCallActiveConnectionId_Object = MibTableColumn
cmqVideoCallActiveConnectionId = _CmqVideoCallActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 1),
    _CmqVideoCallActiveConnectionId_Type()
)
cmqVideoCallActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveConnectionId.setStatus("current")
_CmqVideoCallActiveCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqVideoCallActiveCallReferenceId_Object = MibTableColumn
cmqVideoCallActiveCallReferenceId = _CmqVideoCallActiveCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 2),
    _CmqVideoCallActiveCallReferenceId_Type()
)
cmqVideoCallActiveCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveCallReferenceId.setStatus("current")


class _CmqVideoCallActiveRxMOSInstant_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxMOSInstant based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxMOSInstant_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxMOSInstant_Object = MibTableColumn
cmqVideoCallActiveRxMOSInstant = _CmqVideoCallActiveRxMOSInstant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 3),
    _CmqVideoCallActiveRxMOSInstant_Type()
)
cmqVideoCallActiveRxMOSInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxMOSInstant.setStatus("current")


class _CmqVideoCallActiveRxCompressDegradeInstant_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxCompressDegradeInstant based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxCompressDegradeInstant_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxCompressDegradeInstant_Object = MibTableColumn
cmqVideoCallActiveRxCompressDegradeInstant = _CmqVideoCallActiveRxCompressDegradeInstant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 4),
    _CmqVideoCallActiveRxCompressDegradeInstant_Type()
)
cmqVideoCallActiveRxCompressDegradeInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxCompressDegradeInstant.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxCompressDegradeInstant.setUnits("percent")


class _CmqVideoCallActiveRxNetworkDegradeInstant_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxNetworkDegradeInstant based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxNetworkDegradeInstant_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxNetworkDegradeInstant_Object = MibTableColumn
cmqVideoCallActiveRxNetworkDegradeInstant = _CmqVideoCallActiveRxNetworkDegradeInstant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 5),
    _CmqVideoCallActiveRxNetworkDegradeInstant_Type()
)
cmqVideoCallActiveRxNetworkDegradeInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxNetworkDegradeInstant.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxNetworkDegradeInstant.setUnits("percent")


class _CmqVideoCallActiveRxTransscodeDegradeInstant_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxTransscodeDegradeInstant based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxTransscodeDegradeInstant_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxTransscodeDegradeInstant_Object = MibTableColumn
cmqVideoCallActiveRxTransscodeDegradeInstant = _CmqVideoCallActiveRxTransscodeDegradeInstant_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 6),
    _CmqVideoCallActiveRxTransscodeDegradeInstant_Type()
)
cmqVideoCallActiveRxTransscodeDegradeInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxTransscodeDegradeInstant.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxTransscodeDegradeInstant.setUnits("percent")


class _CmqVideoCallActiveRxMOSAverage_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxMOSAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxMOSAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxMOSAverage_Object = MibTableColumn
cmqVideoCallActiveRxMOSAverage = _CmqVideoCallActiveRxMOSAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 7),
    _CmqVideoCallActiveRxMOSAverage_Type()
)
cmqVideoCallActiveRxMOSAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxMOSAverage.setStatus("current")


class _CmqVideoCallActiveRxCompressDegradeAverage_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxCompressDegradeAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxCompressDegradeAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxCompressDegradeAverage_Object = MibTableColumn
cmqVideoCallActiveRxCompressDegradeAverage = _CmqVideoCallActiveRxCompressDegradeAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 8),
    _CmqVideoCallActiveRxCompressDegradeAverage_Type()
)
cmqVideoCallActiveRxCompressDegradeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxCompressDegradeAverage.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxCompressDegradeAverage.setUnits("percent")


class _CmqVideoCallActiveRxNetworkDegradeAverage_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxNetworkDegradeAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxNetworkDegradeAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxNetworkDegradeAverage_Object = MibTableColumn
cmqVideoCallActiveRxNetworkDegradeAverage = _CmqVideoCallActiveRxNetworkDegradeAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 9),
    _CmqVideoCallActiveRxNetworkDegradeAverage_Type()
)
cmqVideoCallActiveRxNetworkDegradeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxNetworkDegradeAverage.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxNetworkDegradeAverage.setUnits("percent")


class _CmqVideoCallActiveRxTransscodeDegradeAverage_Type(Unsigned32):
    """Custom type cmqVideoCallActiveRxTransscodeDegradeAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallActiveRxTransscodeDegradeAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallActiveRxTransscodeDegradeAverage_Object = MibTableColumn
cmqVideoCallActiveRxTransscodeDegradeAverage = _CmqVideoCallActiveRxTransscodeDegradeAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 3, 1, 1, 10),
    _CmqVideoCallActiveRxTransscodeDegradeAverage_Type()
)
cmqVideoCallActiveRxTransscodeDegradeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxTransscodeDegradeAverage.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallActiveRxTransscodeDegradeAverage.setUnits("percent")
_CmqVideoCallHistory_ObjectIdentity = ObjectIdentity
cmqVideoCallHistory = _CmqVideoCallHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4)
)
_CmqVideoCallHistoryTable_Object = MibTable
cmqVideoCallHistoryTable = _CmqVideoCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cmqVideoCallHistoryTable.setStatus("current")
_CmqVideoCallHistoryEntry_Object = MibTableRow
cmqVideoCallHistoryEntry = _CmqVideoCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1, 1)
)
cmqVideoCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmqVideoCallHistoryEntry.setStatus("current")
_CmqVideoCallHistoryConnectionId_Type = CvcGUid
_CmqVideoCallHistoryConnectionId_Object = MibTableColumn
cmqVideoCallHistoryConnectionId = _CmqVideoCallHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1, 1, 1),
    _CmqVideoCallHistoryConnectionId_Type()
)
cmqVideoCallHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryConnectionId.setStatus("current")
_CmqVideoCallHistoryCallReferenceId_Type = CvcCallReferenceIdOrZero
_CmqVideoCallHistoryCallReferenceId_Object = MibTableColumn
cmqVideoCallHistoryCallReferenceId = _CmqVideoCallHistoryCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1, 1, 2),
    _CmqVideoCallHistoryCallReferenceId_Type()
)
cmqVideoCallHistoryCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryCallReferenceId.setStatus("current")


class _CmqVideoCallHistoryRxMOSAverage_Type(Unsigned32):
    """Custom type cmqVideoCallHistoryRxMOSAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallHistoryRxMOSAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallHistoryRxMOSAverage_Object = MibTableColumn
cmqVideoCallHistoryRxMOSAverage = _CmqVideoCallHistoryRxMOSAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1, 1, 3),
    _CmqVideoCallHistoryRxMOSAverage_Type()
)
cmqVideoCallHistoryRxMOSAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryRxMOSAverage.setStatus("current")


class _CmqVideoCallHistoryRxCompressDegradeAverage_Type(Unsigned32):
    """Custom type cmqVideoCallHistoryRxCompressDegradeAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallHistoryRxCompressDegradeAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallHistoryRxCompressDegradeAverage_Object = MibTableColumn
cmqVideoCallHistoryRxCompressDegradeAverage = _CmqVideoCallHistoryRxCompressDegradeAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1, 1, 4),
    _CmqVideoCallHistoryRxCompressDegradeAverage_Type()
)
cmqVideoCallHistoryRxCompressDegradeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryRxCompressDegradeAverage.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryRxCompressDegradeAverage.setUnits("percent")


class _CmqVideoCallHistoryRxNetworkDegradeAverage_Type(Unsigned32):
    """Custom type cmqVideoCallHistoryRxNetworkDegradeAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallHistoryRxNetworkDegradeAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallHistoryRxNetworkDegradeAverage_Object = MibTableColumn
cmqVideoCallHistoryRxNetworkDegradeAverage = _CmqVideoCallHistoryRxNetworkDegradeAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1, 1, 5),
    _CmqVideoCallHistoryRxNetworkDegradeAverage_Type()
)
cmqVideoCallHistoryRxNetworkDegradeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryRxNetworkDegradeAverage.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryRxNetworkDegradeAverage.setUnits("percent")


class _CmqVideoCallHistoryRxTransscodeDegradeAverage_Type(Unsigned32):
    """Custom type cmqVideoCallHistoryRxTransscodeDegradeAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CmqVideoCallHistoryRxTransscodeDegradeAverage_Type.__name__ = "Unsigned32"
_CmqVideoCallHistoryRxTransscodeDegradeAverage_Object = MibTableColumn
cmqVideoCallHistoryRxTransscodeDegradeAverage = _CmqVideoCallHistoryRxTransscodeDegradeAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 1, 4, 1, 1, 6),
    _CmqVideoCallHistoryRxTransscodeDegradeAverage_Type()
)
cmqVideoCallHistoryRxTransscodeDegradeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryRxTransscodeDegradeAverage.setStatus("current")
if mibBuilder.loadTexts:
    cmqVideoCallHistoryRxTransscodeDegradeAverage.setUnits("percent")
_CiscoMediaQualityMIBConform_ObjectIdentity = ObjectIdentity
ciscoMediaQualityMIBConform = _CiscoMediaQualityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2)
)
_CiscoMediaQualityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMediaQualityMIBCompliances = _CiscoMediaQualityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2, 1)
)
_CiscoMediaQualityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMediaQualityMIBGroups = _CiscoMediaQualityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2, 2)
)

# Managed Objects groups

cmqVoiceCallActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2, 2, 1)
)
cmqVoiceCallActiveGroup.setObjects(
      *(("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxSevConcealRatioPct"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxCallConcealRatioPct"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktLossRatioPct"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxRoundTripTime"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxCallDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxVoiceDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktLossConcealDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktCntExpected"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktCntNotArrived"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktCntComfortNoise"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktCntUnusableLate"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktCntDiscarded"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPktCntEffLoss"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxUnimpairedSecOK"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxConcealSec"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxSevConcealSec"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxJBufMode"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxJBufNomDelay"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxJBufDlyNow"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxJBufLowWater"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxJBuffHiWater"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActive3550JShortTermAvg"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActive3550JCallAvg"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxSignalLvl"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107Rscore"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107RMosListen"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107RScoreConv"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107RMosConv"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107CodecIeBase"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107CodecBPL"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107DefaultR0"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107IeEff"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPred107Idd"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoAvg"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoRecent"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoBaseline"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoMin"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoNumWin"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoBursts"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoFrLoss"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxPredMosLqoVerID"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveTxCodecId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveTxVadEnabled"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveTxTmrCallDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveTxTmrActSpeechDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveTxSignalLvl"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveTxNoiseFloor"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallActiveRxCodecId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNRConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNRCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNREnabledMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActivePreNRNoiseFloorEstMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActivePostNRNoiseFloorEstMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPEnabledMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNumSigASPTriggMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveTotNumASPTriggMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveTotASPDurMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveLongestDurEpiMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveLoudestFreqEstForLongEpiMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveDurSigASPTriggMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNREnabledEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNRDirEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNumSigASPTriggEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveTotNumASPTriggEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveTotASPDurEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveLongestDurEpiEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveLoudestFreqEstForLongEpiEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveDurSigASPTriggEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNRDirMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNRLibVer"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNRIntensity"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPDirMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPMode"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPVer"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveNRCallType"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPCallType"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActivePreNRNoiseFloorEstEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActivePostNRNoiseFloorEstEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPEnabledEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallActiveASPDirEar"))
)
if mibBuilder.loadTexts:
    cmqVoiceCallActiveGroup.setStatus("current")

cmqVoiceCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2, 2, 2)
)
cmqVoiceCallHistoryGroup.setObjects(
      *(("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxCodecId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxSevConcealRatioPct"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxCallConcealRatioPct"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktLossRatioPct"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxRoundTripTime"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxCallDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxVoiceDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktLossConcealDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktCntExpected"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktCntNotArrived"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktCntComfortNoise"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktCntUnusableLate"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktCntDiscarded"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPktCntEffLoss"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxUnimpairedSecOK"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxConcealSec"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxSevConcealSec"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxJBufMode"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxJBufNomDelay"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxJBufDlyNow"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxJBufLowWater"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxJBuffHiWater"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistory3550JShortTermAvg"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistory3550JCallAvg"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxSignalLvl"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107Rscore"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107RMosListen"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107RScoreConv"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107RMosConv"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107CodecIeBase"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107CodecBPL"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107DefaultR0"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107IeEff"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPred107Idd"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoAvg"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoRecent"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoBaseline"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoMin"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoNumWin"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoBursts"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoFrLoss"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryRxPredMosLqoVerID"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryTxCodecId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryTxVadEnabled"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryTxTmrCallDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryTxTmrActSpeechDur"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryTxSignalLvl"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryTxNoiseFloor"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVoIPCallHistoryCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNRConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNRCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNREnabledMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryPreNRNoiseFloorEstMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryPostNRNoiseFloorEstMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPEnabledMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNumSigASPTriggMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryDurSigASPTriggMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryTotNumASPTriggMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryTotASPDurMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryLongestDurEpiMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryLoudestFreqEstForLongEpiMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryPreNRNoiseFloorEstEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryPostNRNoiseFloorEstEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNumSigASPTriggEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryDurSigASPTriggEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryTotNumASPTriggEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryTotASPDurEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryLongestDurEpiEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryLoudestFreqEstForLongEpiEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNRDirMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNRLibVer"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNRIntensity"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPDirMic"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPMode"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPVer"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNRCallType"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPCallType"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNREnabledEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryNRDirEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPEnabledEar"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqCommonCallHistoryASPDirEar"))
)
if mibBuilder.loadTexts:
    cmqVoiceCallHistoryGroup.setStatus("current")

cmqVideoCallActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2, 2, 3)
)
cmqVideoCallActiveGroup.setObjects(
      *(("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxMOSInstant"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxMOSAverage"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxCompressDegradeInstant"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxNetworkDegradeInstant"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxTransscodeDegradeInstant"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxCompressDegradeAverage"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxNetworkDegradeAverage"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallActiveRxTransscodeDegradeAverage"))
)
if mibBuilder.loadTexts:
    cmqVideoCallActiveGroup.setStatus("current")

cmqVideoCallHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2, 2, 4)
)
cmqVideoCallHistoryGroup.setObjects(
      *(("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallHistoryConnectionId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallHistoryCallReferenceId"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallHistoryRxMOSAverage"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallHistoryRxCompressDegradeAverage"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallHistoryRxNetworkDegradeAverage"),
        ("CISCO-MEDIA-QUALITY-MIB", "cmqVideoCallHistoryRxTransscodeDegradeAverage"))
)
if mibBuilder.loadTexts:
    cmqVideoCallHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMediaQualityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 769, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMediaQualityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEDIA-QUALITY-MIB",
    **{"ciscoMediaQualityMIB": ciscoMediaQualityMIB,
       "ciscoMediaQualityMIBNotifs": ciscoMediaQualityMIBNotifs,
       "ciscoMediaQualityMIBObjects": ciscoMediaQualityMIBObjects,
       "cmqVoiceCallActive": cmqVoiceCallActive,
       "cmqVoIPCallActiveTable": cmqVoIPCallActiveTable,
       "cmqVoIPCallActiveEntry": cmqVoIPCallActiveEntry,
       "cmqVoIPCallActiveConnectionId": cmqVoIPCallActiveConnectionId,
       "cmqVoIPCallActiveCallReferenceId": cmqVoIPCallActiveCallReferenceId,
       "cmqVoIPCallActiveRxCodecId": cmqVoIPCallActiveRxCodecId,
       "cmqVoIPCallActiveRxSevConcealRatioPct": cmqVoIPCallActiveRxSevConcealRatioPct,
       "cmqVoIPCallActiveRxCallConcealRatioPct": cmqVoIPCallActiveRxCallConcealRatioPct,
       "cmqVoIPCallActiveRxPktLossRatioPct": cmqVoIPCallActiveRxPktLossRatioPct,
       "cmqVoIPCallActiveRxRoundTripTime": cmqVoIPCallActiveRxRoundTripTime,
       "cmqVoIPCallActiveRxCallDur": cmqVoIPCallActiveRxCallDur,
       "cmqVoIPCallActiveRxVoiceDur": cmqVoIPCallActiveRxVoiceDur,
       "cmqVoIPCallActiveRxPktLossConcealDur": cmqVoIPCallActiveRxPktLossConcealDur,
       "cmqVoIPCallActiveRxPktCntExpected": cmqVoIPCallActiveRxPktCntExpected,
       "cmqVoIPCallActiveRxPktCntNotArrived": cmqVoIPCallActiveRxPktCntNotArrived,
       "cmqVoIPCallActiveRxPktCntComfortNoise": cmqVoIPCallActiveRxPktCntComfortNoise,
       "cmqVoIPCallActiveRxPktCntUnusableLate": cmqVoIPCallActiveRxPktCntUnusableLate,
       "cmqVoIPCallActiveRxPktCntDiscarded": cmqVoIPCallActiveRxPktCntDiscarded,
       "cmqVoIPCallActiveRxPktCntEffLoss": cmqVoIPCallActiveRxPktCntEffLoss,
       "cmqVoIPCallActiveRxUnimpairedSecOK": cmqVoIPCallActiveRxUnimpairedSecOK,
       "cmqVoIPCallActiveRxConcealSec": cmqVoIPCallActiveRxConcealSec,
       "cmqVoIPCallActiveRxSevConcealSec": cmqVoIPCallActiveRxSevConcealSec,
       "cmqVoIPCallActiveRxJBufMode": cmqVoIPCallActiveRxJBufMode,
       "cmqVoIPCallActiveRxJBufNomDelay": cmqVoIPCallActiveRxJBufNomDelay,
       "cmqVoIPCallActiveRxJBufDlyNow": cmqVoIPCallActiveRxJBufDlyNow,
       "cmqVoIPCallActiveRxJBufLowWater": cmqVoIPCallActiveRxJBufLowWater,
       "cmqVoIPCallActiveRxJBuffHiWater": cmqVoIPCallActiveRxJBuffHiWater,
       "cmqVoIPCallActive3550JShortTermAvg": cmqVoIPCallActive3550JShortTermAvg,
       "cmqVoIPCallActive3550JCallAvg": cmqVoIPCallActive3550JCallAvg,
       "cmqVoIPCallActiveRxSignalLvl": cmqVoIPCallActiveRxSignalLvl,
       "cmqVoIPCallActiveRxPred107Rscore": cmqVoIPCallActiveRxPred107Rscore,
       "cmqVoIPCallActiveRxPred107RMosListen": cmqVoIPCallActiveRxPred107RMosListen,
       "cmqVoIPCallActiveRxPred107RScoreConv": cmqVoIPCallActiveRxPred107RScoreConv,
       "cmqVoIPCallActiveRxPred107RMosConv": cmqVoIPCallActiveRxPred107RMosConv,
       "cmqVoIPCallActiveRxPred107CodecIeBase": cmqVoIPCallActiveRxPred107CodecIeBase,
       "cmqVoIPCallActiveRxPred107CodecBPL": cmqVoIPCallActiveRxPred107CodecBPL,
       "cmqVoIPCallActiveRxPred107DefaultR0": cmqVoIPCallActiveRxPred107DefaultR0,
       "cmqVoIPCallActiveRxPred107IeEff": cmqVoIPCallActiveRxPred107IeEff,
       "cmqVoIPCallActiveRxPred107Idd": cmqVoIPCallActiveRxPred107Idd,
       "cmqVoIPCallActiveRxPredMosLqoAvg": cmqVoIPCallActiveRxPredMosLqoAvg,
       "cmqVoIPCallActiveRxPredMosLqoRecent": cmqVoIPCallActiveRxPredMosLqoRecent,
       "cmqVoIPCallActiveRxPredMosLqoBaseline": cmqVoIPCallActiveRxPredMosLqoBaseline,
       "cmqVoIPCallActiveRxPredMosLqoMin": cmqVoIPCallActiveRxPredMosLqoMin,
       "cmqVoIPCallActiveRxPredMosLqoNumWin": cmqVoIPCallActiveRxPredMosLqoNumWin,
       "cmqVoIPCallActiveRxPredMosLqoBursts": cmqVoIPCallActiveRxPredMosLqoBursts,
       "cmqVoIPCallActiveRxPredMosLqoFrLoss": cmqVoIPCallActiveRxPredMosLqoFrLoss,
       "cmqVoIPCallActiveRxPredMosLqoVerID": cmqVoIPCallActiveRxPredMosLqoVerID,
       "cmqVoIPCallActiveTxCodecId": cmqVoIPCallActiveTxCodecId,
       "cmqVoIPCallActiveTxVadEnabled": cmqVoIPCallActiveTxVadEnabled,
       "cmqVoIPCallActiveTxTmrCallDur": cmqVoIPCallActiveTxTmrCallDur,
       "cmqVoIPCallActiveTxTmrActSpeechDur": cmqVoIPCallActiveTxTmrActSpeechDur,
       "cmqVoIPCallActiveTxSignalLvl": cmqVoIPCallActiveTxSignalLvl,
       "cmqVoIPCallActiveTxNoiseFloor": cmqVoIPCallActiveTxNoiseFloor,
       "cmqCommonCallActiveNRTable": cmqCommonCallActiveNRTable,
       "cmqCommonCallActiveNREntry": cmqCommonCallActiveNREntry,
       "cmqCommonCallActiveNRConnectionId": cmqCommonCallActiveNRConnectionId,
       "cmqCommonCallActiveNRCallReferenceId": cmqCommonCallActiveNRCallReferenceId,
       "cmqCommonCallActiveNRCallType": cmqCommonCallActiveNRCallType,
       "cmqCommonCallActiveNREnabledMic": cmqCommonCallActiveNREnabledMic,
       "cmqCommonCallActiveNREnabledEar": cmqCommonCallActiveNREnabledEar,
       "cmqCommonCallActiveNRDirMic": cmqCommonCallActiveNRDirMic,
       "cmqCommonCallActiveNRDirEar": cmqCommonCallActiveNRDirEar,
       "cmqCommonCallActiveNRLibVer": cmqCommonCallActiveNRLibVer,
       "cmqCommonCallActiveNRIntensity": cmqCommonCallActiveNRIntensity,
       "cmqCommonCallActivePreNRNoiseFloorEstMic": cmqCommonCallActivePreNRNoiseFloorEstMic,
       "cmqCommonCallActivePostNRNoiseFloorEstMic": cmqCommonCallActivePostNRNoiseFloorEstMic,
       "cmqCommonCallActivePreNRNoiseFloorEstEar": cmqCommonCallActivePreNRNoiseFloorEstEar,
       "cmqCommonCallActivePostNRNoiseFloorEstEar": cmqCommonCallActivePostNRNoiseFloorEstEar,
       "cmqCommonCallActiveASPTable": cmqCommonCallActiveASPTable,
       "cmqCommonCallActiveASPEntry": cmqCommonCallActiveASPEntry,
       "cmqCommonCallActiveASPConnectionId": cmqCommonCallActiveASPConnectionId,
       "cmqCommonCallActiveASPCallReferenceId": cmqCommonCallActiveASPCallReferenceId,
       "cmqCommonCallActiveASPCallType": cmqCommonCallActiveASPCallType,
       "cmqCommonCallActiveASPEnabledMic": cmqCommonCallActiveASPEnabledMic,
       "cmqCommonCallActiveASPEnabledEar": cmqCommonCallActiveASPEnabledEar,
       "cmqCommonCallActiveASPDirMic": cmqCommonCallActiveASPDirMic,
       "cmqCommonCallActiveASPDirEar": cmqCommonCallActiveASPDirEar,
       "cmqCommonCallActiveASPMode": cmqCommonCallActiveASPMode,
       "cmqCommonCallActiveASPVer": cmqCommonCallActiveASPVer,
       "cmqCommonCallActiveNumSigASPTriggMic": cmqCommonCallActiveNumSigASPTriggMic,
       "cmqCommonCallActiveDurSigASPTriggMic": cmqCommonCallActiveDurSigASPTriggMic,
       "cmqCommonCallActiveTotNumASPTriggMic": cmqCommonCallActiveTotNumASPTriggMic,
       "cmqCommonCallActiveTotASPDurMic": cmqCommonCallActiveTotASPDurMic,
       "cmqCommonCallActiveLoudestFreqEstForLongEpiMic": cmqCommonCallActiveLoudestFreqEstForLongEpiMic,
       "cmqCommonCallActiveLongestDurEpiMic": cmqCommonCallActiveLongestDurEpiMic,
       "cmqCommonCallActiveNumSigASPTriggEar": cmqCommonCallActiveNumSigASPTriggEar,
       "cmqCommonCallActiveDurSigASPTriggEar": cmqCommonCallActiveDurSigASPTriggEar,
       "cmqCommonCallActiveTotNumASPTriggEar": cmqCommonCallActiveTotNumASPTriggEar,
       "cmqCommonCallActiveTotASPDurEar": cmqCommonCallActiveTotASPDurEar,
       "cmqCommonCallActiveLoudestFreqEstForLongEpiEar": cmqCommonCallActiveLoudestFreqEstForLongEpiEar,
       "cmqCommonCallActiveLongestDurEpiEar": cmqCommonCallActiveLongestDurEpiEar,
       "cmqVoiceCallHistory": cmqVoiceCallHistory,
       "cmqVoIPCallHistoryTable": cmqVoIPCallHistoryTable,
       "cmqVoIPCallHistoryEntry": cmqVoIPCallHistoryEntry,
       "cmqVoIPCallHistoryConnectionId": cmqVoIPCallHistoryConnectionId,
       "cmqVoIPCallHistoryCallReferenceId": cmqVoIPCallHistoryCallReferenceId,
       "cmqVoIPCallHistoryRxCodecId": cmqVoIPCallHistoryRxCodecId,
       "cmqVoIPCallHistoryRxSevConcealRatioPct": cmqVoIPCallHistoryRxSevConcealRatioPct,
       "cmqVoIPCallHistoryRxCallConcealRatioPct": cmqVoIPCallHistoryRxCallConcealRatioPct,
       "cmqVoIPCallHistoryRxPktLossRatioPct": cmqVoIPCallHistoryRxPktLossRatioPct,
       "cmqVoIPCallHistoryRxRoundTripTime": cmqVoIPCallHistoryRxRoundTripTime,
       "cmqVoIPCallHistoryRxCallDur": cmqVoIPCallHistoryRxCallDur,
       "cmqVoIPCallHistoryRxVoiceDur": cmqVoIPCallHistoryRxVoiceDur,
       "cmqVoIPCallHistoryRxPktLossConcealDur": cmqVoIPCallHistoryRxPktLossConcealDur,
       "cmqVoIPCallHistoryRxPktCntExpected": cmqVoIPCallHistoryRxPktCntExpected,
       "cmqVoIPCallHistoryRxPktCntNotArrived": cmqVoIPCallHistoryRxPktCntNotArrived,
       "cmqVoIPCallHistoryRxPktCntComfortNoise": cmqVoIPCallHistoryRxPktCntComfortNoise,
       "cmqVoIPCallHistoryRxPktCntUnusableLate": cmqVoIPCallHistoryRxPktCntUnusableLate,
       "cmqVoIPCallHistoryRxPktCntDiscarded": cmqVoIPCallHistoryRxPktCntDiscarded,
       "cmqVoIPCallHistoryRxPktCntEffLoss": cmqVoIPCallHistoryRxPktCntEffLoss,
       "cmqVoIPCallHistoryRxUnimpairedSecOK": cmqVoIPCallHistoryRxUnimpairedSecOK,
       "cmqVoIPCallHistoryRxConcealSec": cmqVoIPCallHistoryRxConcealSec,
       "cmqVoIPCallHistoryRxSevConcealSec": cmqVoIPCallHistoryRxSevConcealSec,
       "cmqVoIPCallHistoryRxJBufMode": cmqVoIPCallHistoryRxJBufMode,
       "cmqVoIPCallHistoryRxJBufNomDelay": cmqVoIPCallHistoryRxJBufNomDelay,
       "cmqVoIPCallHistoryRxJBufDlyNow": cmqVoIPCallHistoryRxJBufDlyNow,
       "cmqVoIPCallHistoryRxJBufLowWater": cmqVoIPCallHistoryRxJBufLowWater,
       "cmqVoIPCallHistoryRxJBuffHiWater": cmqVoIPCallHistoryRxJBuffHiWater,
       "cmqVoIPCallHistory3550JShortTermAvg": cmqVoIPCallHistory3550JShortTermAvg,
       "cmqVoIPCallHistory3550JCallAvg": cmqVoIPCallHistory3550JCallAvg,
       "cmqVoIPCallHistoryRxSignalLvl": cmqVoIPCallHistoryRxSignalLvl,
       "cmqVoIPCallHistoryRxPred107Rscore": cmqVoIPCallHistoryRxPred107Rscore,
       "cmqVoIPCallHistoryRxPred107RMosListen": cmqVoIPCallHistoryRxPred107RMosListen,
       "cmqVoIPCallHistoryRxPred107RScoreConv": cmqVoIPCallHistoryRxPred107RScoreConv,
       "cmqVoIPCallHistoryRxPred107RMosConv": cmqVoIPCallHistoryRxPred107RMosConv,
       "cmqVoIPCallHistoryRxPred107CodecIeBase": cmqVoIPCallHistoryRxPred107CodecIeBase,
       "cmqVoIPCallHistoryRxPred107CodecBPL": cmqVoIPCallHistoryRxPred107CodecBPL,
       "cmqVoIPCallHistoryRxPred107DefaultR0": cmqVoIPCallHistoryRxPred107DefaultR0,
       "cmqVoIPCallHistoryRxPred107IeEff": cmqVoIPCallHistoryRxPred107IeEff,
       "cmqVoIPCallHistoryRxPred107Idd": cmqVoIPCallHistoryRxPred107Idd,
       "cmqVoIPCallHistoryRxPredMosLqoAvg": cmqVoIPCallHistoryRxPredMosLqoAvg,
       "cmqVoIPCallHistoryRxPredMosLqoRecent": cmqVoIPCallHistoryRxPredMosLqoRecent,
       "cmqVoIPCallHistoryRxPredMosLqoBaseline": cmqVoIPCallHistoryRxPredMosLqoBaseline,
       "cmqVoIPCallHistoryRxPredMosLqoMin": cmqVoIPCallHistoryRxPredMosLqoMin,
       "cmqVoIPCallHistoryRxPredMosLqoNumWin": cmqVoIPCallHistoryRxPredMosLqoNumWin,
       "cmqVoIPCallHistoryRxPredMosLqoBursts": cmqVoIPCallHistoryRxPredMosLqoBursts,
       "cmqVoIPCallHistoryRxPredMosLqoFrLoss": cmqVoIPCallHistoryRxPredMosLqoFrLoss,
       "cmqVoIPCallHistoryRxPredMosLqoVerID": cmqVoIPCallHistoryRxPredMosLqoVerID,
       "cmqVoIPCallHistoryTxCodecId": cmqVoIPCallHistoryTxCodecId,
       "cmqVoIPCallHistoryTxVadEnabled": cmqVoIPCallHistoryTxVadEnabled,
       "cmqVoIPCallHistoryTxTmrCallDur": cmqVoIPCallHistoryTxTmrCallDur,
       "cmqVoIPCallHistoryTxTmrActSpeechDur": cmqVoIPCallHistoryTxTmrActSpeechDur,
       "cmqVoIPCallHistoryTxSignalLvl": cmqVoIPCallHistoryTxSignalLvl,
       "cmqVoIPCallHistoryTxNoiseFloor": cmqVoIPCallHistoryTxNoiseFloor,
       "cmqCommonCallHistoryNRTable": cmqCommonCallHistoryNRTable,
       "cmqCommonCallHistoryNREntry": cmqCommonCallHistoryNREntry,
       "cmqCommonCallHistoryNRConnectionId": cmqCommonCallHistoryNRConnectionId,
       "cmqCommonCallHistoryNRCallReferenceId": cmqCommonCallHistoryNRCallReferenceId,
       "cmqCommonCallHistoryNRCallType": cmqCommonCallHistoryNRCallType,
       "cmqCommonCallHistoryNREnabledMic": cmqCommonCallHistoryNREnabledMic,
       "cmqCommonCallHistoryNREnabledEar": cmqCommonCallHistoryNREnabledEar,
       "cmqCommonCallHistoryNRDirMic": cmqCommonCallHistoryNRDirMic,
       "cmqCommonCallHistoryNRDirEar": cmqCommonCallHistoryNRDirEar,
       "cmqCommonCallHistoryNRLibVer": cmqCommonCallHistoryNRLibVer,
       "cmqCommonCallHistoryNRIntensity": cmqCommonCallHistoryNRIntensity,
       "cmqCommonCallHistoryPreNRNoiseFloorEstMic": cmqCommonCallHistoryPreNRNoiseFloorEstMic,
       "cmqCommonCallHistoryPostNRNoiseFloorEstMic": cmqCommonCallHistoryPostNRNoiseFloorEstMic,
       "cmqCommonCallHistoryPreNRNoiseFloorEstEar": cmqCommonCallHistoryPreNRNoiseFloorEstEar,
       "cmqCommonCallHistoryPostNRNoiseFloorEstEar": cmqCommonCallHistoryPostNRNoiseFloorEstEar,
       "cmqCommonCallHistoryASPTable": cmqCommonCallHistoryASPTable,
       "cmqCommonCallHistoryASPEntry": cmqCommonCallHistoryASPEntry,
       "cmqCommonCallHistoryASPConnectionId": cmqCommonCallHistoryASPConnectionId,
       "cmqCommonCallHistoryASPCallReferenceId": cmqCommonCallHistoryASPCallReferenceId,
       "cmqCommonCallHistoryASPCallType": cmqCommonCallHistoryASPCallType,
       "cmqCommonCallHistoryASPEnabledMic": cmqCommonCallHistoryASPEnabledMic,
       "cmqCommonCallHistoryASPEnabledEar": cmqCommonCallHistoryASPEnabledEar,
       "cmqCommonCallHistoryASPDirMic": cmqCommonCallHistoryASPDirMic,
       "cmqCommonCallHistoryASPDirEar": cmqCommonCallHistoryASPDirEar,
       "cmqCommonCallHistoryASPMode": cmqCommonCallHistoryASPMode,
       "cmqCommonCallHistoryASPVer": cmqCommonCallHistoryASPVer,
       "cmqCommonCallHistoryNumSigASPTriggMic": cmqCommonCallHistoryNumSigASPTriggMic,
       "cmqCommonCallHistoryDurSigASPTriggMic": cmqCommonCallHistoryDurSigASPTriggMic,
       "cmqCommonCallHistoryTotNumASPTriggMic": cmqCommonCallHistoryTotNumASPTriggMic,
       "cmqCommonCallHistoryTotASPDurMic": cmqCommonCallHistoryTotASPDurMic,
       "cmqCommonCallHistoryLoudestFreqEstForLongEpiMic": cmqCommonCallHistoryLoudestFreqEstForLongEpiMic,
       "cmqCommonCallHistoryLongestDurEpiMic": cmqCommonCallHistoryLongestDurEpiMic,
       "cmqCommonCallHistoryNumSigASPTriggEar": cmqCommonCallHistoryNumSigASPTriggEar,
       "cmqCommonCallHistoryDurSigASPTriggEar": cmqCommonCallHistoryDurSigASPTriggEar,
       "cmqCommonCallHistoryTotNumASPTriggEar": cmqCommonCallHistoryTotNumASPTriggEar,
       "cmqCommonCallHistoryTotASPDurEar": cmqCommonCallHistoryTotASPDurEar,
       "cmqCommonCallHistoryLoudestFreqEstForLongEpiEar": cmqCommonCallHistoryLoudestFreqEstForLongEpiEar,
       "cmqCommonCallHistoryLongestDurEpiEar": cmqCommonCallHistoryLongestDurEpiEar,
       "cmqVideoCallActive": cmqVideoCallActive,
       "cmqVideoCallActiveTable": cmqVideoCallActiveTable,
       "cmqVideoCallActiveEntry": cmqVideoCallActiveEntry,
       "cmqVideoCallActiveConnectionId": cmqVideoCallActiveConnectionId,
       "cmqVideoCallActiveCallReferenceId": cmqVideoCallActiveCallReferenceId,
       "cmqVideoCallActiveRxMOSInstant": cmqVideoCallActiveRxMOSInstant,
       "cmqVideoCallActiveRxCompressDegradeInstant": cmqVideoCallActiveRxCompressDegradeInstant,
       "cmqVideoCallActiveRxNetworkDegradeInstant": cmqVideoCallActiveRxNetworkDegradeInstant,
       "cmqVideoCallActiveRxTransscodeDegradeInstant": cmqVideoCallActiveRxTransscodeDegradeInstant,
       "cmqVideoCallActiveRxMOSAverage": cmqVideoCallActiveRxMOSAverage,
       "cmqVideoCallActiveRxCompressDegradeAverage": cmqVideoCallActiveRxCompressDegradeAverage,
       "cmqVideoCallActiveRxNetworkDegradeAverage": cmqVideoCallActiveRxNetworkDegradeAverage,
       "cmqVideoCallActiveRxTransscodeDegradeAverage": cmqVideoCallActiveRxTransscodeDegradeAverage,
       "cmqVideoCallHistory": cmqVideoCallHistory,
       "cmqVideoCallHistoryTable": cmqVideoCallHistoryTable,
       "cmqVideoCallHistoryEntry": cmqVideoCallHistoryEntry,
       "cmqVideoCallHistoryConnectionId": cmqVideoCallHistoryConnectionId,
       "cmqVideoCallHistoryCallReferenceId": cmqVideoCallHistoryCallReferenceId,
       "cmqVideoCallHistoryRxMOSAverage": cmqVideoCallHistoryRxMOSAverage,
       "cmqVideoCallHistoryRxCompressDegradeAverage": cmqVideoCallHistoryRxCompressDegradeAverage,
       "cmqVideoCallHistoryRxNetworkDegradeAverage": cmqVideoCallHistoryRxNetworkDegradeAverage,
       "cmqVideoCallHistoryRxTransscodeDegradeAverage": cmqVideoCallHistoryRxTransscodeDegradeAverage,
       "ciscoMediaQualityMIBConform": ciscoMediaQualityMIBConform,
       "ciscoMediaQualityMIBCompliances": ciscoMediaQualityMIBCompliances,
       "ciscoMediaQualityMIBCompliance": ciscoMediaQualityMIBCompliance,
       "ciscoMediaQualityMIBGroups": ciscoMediaQualityMIBGroups,
       "cmqVoiceCallActiveGroup": cmqVoiceCallActiveGroup,
       "cmqVoiceCallHistoryGroup": cmqVoiceCallHistoryGroup,
       "cmqVideoCallActiveGroup": cmqVideoCallActiveGroup,
       "cmqVideoCallHistoryGroup": cmqVideoCallHistoryGroup}
)
