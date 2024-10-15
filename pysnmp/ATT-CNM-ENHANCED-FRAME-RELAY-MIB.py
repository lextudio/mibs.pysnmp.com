# SNMP MIB module (ATT-CNM-ENHANCED-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATT-CNM-ENHANCED-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:17 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_products_ObjectIdentity = ObjectIdentity
att_products = _Att_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1)
)
_Att_cnmAgent_ObjectIdentity = ObjectIdentity
att_cnmAgent = _Att_cnmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 9)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_cnm_ObjectIdentity = ObjectIdentity
att_cnm = _Att_cnm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15)
)
_Att_cnm_efr_ObjectIdentity = ObjectIdentity
att_cnm_efr = _Att_cnm_efr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8)
)
_AttCNMefrConfigTable_Object = MibTable
attCNMefrConfigTable = _AttCNMefrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1)
)
if mibBuilder.loadTexts:
    attCNMefrConfigTable.setStatus("mandatory")
_AttCNMefrConfigEntry_Object = MibTableRow
attCNMefrConfigEntry = _AttCNMefrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1)
)
attCNMefrConfigEntry.setIndexNames(
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMefrConfigEntry.setStatus("mandatory")
_AttCNMefrConfigIndex_Type = Integer32
_AttCNMefrConfigIndex_Object = MibTableColumn
attCNMefrConfigIndex = _AttCNMefrConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 1),
    _AttCNMefrConfigIndex_Type()
)
attCNMefrConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrConfigIndex.setStatus("mandatory")


class _AttCNMefrMgmtType_Type(Integer32):
    """Custom type attCNMefrMgmtType based on Integer32"""
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
        *(("ansi", 3),
          ("auto-set", 1),
          ("ccitt", 4),
          ("lmi", 2),
          ("none", 5))
    )


_AttCNMefrMgmtType_Type.__name__ = "Integer32"
_AttCNMefrMgmtType_Object = MibTableColumn
attCNMefrMgmtType = _AttCNMefrMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 2),
    _AttCNMefrMgmtType_Type()
)
attCNMefrMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMgmtType.setStatus("mandatory")


class _AttCNMefrPollDirection_Type(Integer32):
    """Custom type attCNMefrPollDirection based on Integer32"""
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
          ("receive", 1),
          ("send", 2))
    )


_AttCNMefrPollDirection_Type.__name__ = "Integer32"
_AttCNMefrPollDirection_Object = MibTableColumn
attCNMefrPollDirection = _AttCNMefrPollDirection_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 3),
    _AttCNMefrPollDirection_Type()
)
attCNMefrPollDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPollDirection.setStatus("mandatory")
_AttCNMefrFullStatusPoll_Type = Integer32
_AttCNMefrFullStatusPoll_Object = MibTableColumn
attCNMefrFullStatusPoll = _AttCNMefrFullStatusPoll_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 4),
    _AttCNMefrFullStatusPoll_Type()
)
attCNMefrFullStatusPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrFullStatusPoll.setStatus("mandatory")
_AttCNMefrErrorThreshold_Type = Integer32
_AttCNMefrErrorThreshold_Object = MibTableColumn
attCNMefrErrorThreshold = _AttCNMefrErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 5),
    _AttCNMefrErrorThreshold_Type()
)
attCNMefrErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrErrorThreshold.setStatus("mandatory")
_AttCNMefrMonitoredEvents_Type = Integer32
_AttCNMefrMonitoredEvents_Object = MibTableColumn
attCNMefrMonitoredEvents = _AttCNMefrMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 6),
    _AttCNMefrMonitoredEvents_Type()
)
attCNMefrMonitoredEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMonitoredEvents.setStatus("mandatory")
_AttCNMefrIntegrityTimer_Type = Integer32
_AttCNMefrIntegrityTimer_Object = MibTableColumn
attCNMefrIntegrityTimer = _AttCNMefrIntegrityTimer_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 7),
    _AttCNMefrIntegrityTimer_Type()
)
attCNMefrIntegrityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrIntegrityTimer.setStatus("mandatory")
_AttCNMefrPollVerifyTimer_Type = Integer32
_AttCNMefrPollVerifyTimer_Object = MibTableColumn
attCNMefrPollVerifyTimer = _AttCNMefrPollVerifyTimer_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 8),
    _AttCNMefrPollVerifyTimer_Type()
)
attCNMefrPollVerifyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPollVerifyTimer.setStatus("mandatory")


class _AttCNMefrLMIFlowControl_Type(Integer32):
    """Custom type attCNMefrLMIFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lmiFlowControlOff", 2),
          ("lmiFlowControlOn", 1))
    )


_AttCNMefrLMIFlowControl_Type.__name__ = "Integer32"
_AttCNMefrLMIFlowControl_Object = MibTableColumn
attCNMefrLMIFlowControl = _AttCNMefrLMIFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 9),
    _AttCNMefrLMIFlowControl_Type()
)
attCNMefrLMIFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrLMIFlowControl.setStatus("mandatory")
_AttCNMefrSupportedPVCs_Type = Integer32
_AttCNMefrSupportedPVCs_Object = MibTableColumn
attCNMefrSupportedPVCs = _AttCNMefrSupportedPVCs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 10),
    _AttCNMefrSupportedPVCs_Type()
)
attCNMefrSupportedPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrSupportedPVCs.setStatus("mandatory")
_AttCNMefrMeasMaxIntervals_Type = Integer32
_AttCNMefrMeasMaxIntervals_Object = MibTableColumn
attCNMefrMeasMaxIntervals = _AttCNMefrMeasMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 11),
    _AttCNMefrMeasMaxIntervals_Type()
)
attCNMefrMeasMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMeasMaxIntervals.setStatus("mandatory")
_AttCNMefrMeasIntervalLen_Type = Integer32
_AttCNMefrMeasIntervalLen_Object = MibTableColumn
attCNMefrMeasIntervalLen = _AttCNMefrMeasIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 1, 1, 12),
    _AttCNMefrMeasIntervalLen_Type()
)
attCNMefrMeasIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMeasIntervalLen.setStatus("mandatory")
_AttCNMefrMeasTable_Object = MibTable
attCNMefrMeasTable = _AttCNMefrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2)
)
if mibBuilder.loadTexts:
    attCNMefrMeasTable.setStatus("mandatory")
_AttCNMefrMeasEntry_Object = MibTableRow
attCNMefrMeasEntry = _AttCNMefrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1)
)
attCNMefrMeasEntry.setIndexNames(
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrMeasIndex"),
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrMeasInterval"),
)
if mibBuilder.loadTexts:
    attCNMefrMeasEntry.setStatus("mandatory")
_AttCNMefrMeasIndex_Type = Integer32
_AttCNMefrMeasIndex_Object = MibTableColumn
attCNMefrMeasIndex = _AttCNMefrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 1),
    _AttCNMefrMeasIndex_Type()
)
attCNMefrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMeasIndex.setStatus("mandatory")
_AttCNMefrMeasInterval_Type = Integer32
_AttCNMefrMeasInterval_Object = MibTableColumn
attCNMefrMeasInterval = _AttCNMefrMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 2),
    _AttCNMefrMeasInterval_Type()
)
attCNMefrMeasInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMeasInterval.setStatus("mandatory")
_AttCNMefrMeasTimeStamp_Type = Integer32
_AttCNMefrMeasTimeStamp_Object = MibTableColumn
attCNMefrMeasTimeStamp = _AttCNMefrMeasTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 3),
    _AttCNMefrMeasTimeStamp_Type()
)
attCNMefrMeasTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMeasTimeStamp.setStatus("mandatory")


class _AttCNMefrMeasLocalTime_Type(DisplayString):
    """Custom type attCNMefrMeasLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMefrMeasLocalTime_Type.__name__ = "DisplayString"
_AttCNMefrMeasLocalTime_Object = MibTableColumn
attCNMefrMeasLocalTime = _AttCNMefrMeasLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 4),
    _AttCNMefrMeasLocalTime_Type()
)
attCNMefrMeasLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMeasLocalTime.setStatus("mandatory")
_AttCNMefrReceivedOctets_Type = Gauge32
_AttCNMefrReceivedOctets_Object = MibTableColumn
attCNMefrReceivedOctets = _AttCNMefrReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 5),
    _AttCNMefrReceivedOctets_Type()
)
attCNMefrReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrReceivedOctets.setStatus("mandatory")
_AttCNMefrSentOctets_Type = Gauge32
_AttCNMefrSentOctets_Object = MibTableColumn
attCNMefrSentOctets = _AttCNMefrSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 6),
    _AttCNMefrSentOctets_Type()
)
attCNMefrSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrSentOctets.setStatus("mandatory")
_AttCNMefrReceivedFrames_Type = Gauge32
_AttCNMefrReceivedFrames_Object = MibTableColumn
attCNMefrReceivedFrames = _AttCNMefrReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 7),
    _AttCNMefrReceivedFrames_Type()
)
attCNMefrReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrReceivedFrames.setStatus("mandatory")
_AttCNMefrSentFrames_Type = Gauge32
_AttCNMefrSentFrames_Object = MibTableColumn
attCNMefrSentFrames = _AttCNMefrSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 8),
    _AttCNMefrSentFrames_Type()
)
attCNMefrSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrSentFrames.setStatus("mandatory")
_AttCNMefrBadFrames_Type = Gauge32
_AttCNMefrBadFrames_Object = MibTableColumn
attCNMefrBadFrames = _AttCNMefrBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 9),
    _AttCNMefrBadFrames_Type()
)
attCNMefrBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrBadFrames.setStatus("mandatory")
_AttCNMefrReceiverOverruns_Type = Gauge32
_AttCNMefrReceiverOverruns_Object = MibTableColumn
attCNMefrReceiverOverruns = _AttCNMefrReceiverOverruns_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 10),
    _AttCNMefrReceiverOverruns_Type()
)
attCNMefrReceiverOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrReceiverOverruns.setStatus("mandatory")
_AttCNMefrIngressUtil_Type = Gauge32
_AttCNMefrIngressUtil_Object = MibTableColumn
attCNMefrIngressUtil = _AttCNMefrIngressUtil_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 11),
    _AttCNMefrIngressUtil_Type()
)
attCNMefrIngressUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrIngressUtil.setStatus("mandatory")
_AttCNMefrEgressUtil_Type = Gauge32
_AttCNMefrEgressUtil_Object = MibTableColumn
attCNMefrEgressUtil = _AttCNMefrEgressUtil_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 2, 1, 12),
    _AttCNMefrEgressUtil_Type()
)
attCNMefrEgressUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrEgressUtil.setStatus("mandatory")
_AttCNMefrPVCConfigTable_Object = MibTable
attCNMefrPVCConfigTable = _AttCNMefrPVCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3)
)
if mibBuilder.loadTexts:
    attCNMefrPVCConfigTable.setStatus("mandatory")
_AttCNMefrPVCConfigEntry_Object = MibTableRow
attCNMefrPVCConfigEntry = _AttCNMefrPVCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1)
)
attCNMefrPVCConfigEntry.setIndexNames(
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrPVCConfigIfIndex"),
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrPVCConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMefrPVCConfigEntry.setStatus("mandatory")
_AttCNMefrPVCConfigIfIndex_Type = Integer32
_AttCNMefrPVCConfigIfIndex_Object = MibTableColumn
attCNMefrPVCConfigIfIndex = _AttCNMefrPVCConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 1),
    _AttCNMefrPVCConfigIfIndex_Type()
)
attCNMefrPVCConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCConfigIfIndex.setStatus("mandatory")
_AttCNMefrPVCConfigIndex_Type = Integer32
_AttCNMefrPVCConfigIndex_Object = MibTableColumn
attCNMefrPVCConfigIndex = _AttCNMefrPVCConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 2),
    _AttCNMefrPVCConfigIndex_Type()
)
attCNMefrPVCConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCConfigIndex.setStatus("mandatory")


class _AttCNMefrPVCServiceType_Type(Integer32):
    """Custom type attCNMefrPVCServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_AttCNMefrPVCServiceType_Type.__name__ = "Integer32"
_AttCNMefrPVCServiceType_Object = MibTableColumn
attCNMefrPVCServiceType = _AttCNMefrPVCServiceType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 3),
    _AttCNMefrPVCServiceType_Type()
)
attCNMefrPVCServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCServiceType.setStatus("mandatory")
_AttCNMefrLocalCIR_Type = Integer32
_AttCNMefrLocalCIR_Object = MibTableColumn
attCNMefrLocalCIR = _AttCNMefrLocalCIR_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 4),
    _AttCNMefrLocalCIR_Type()
)
attCNMefrLocalCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrLocalCIR.setStatus("mandatory")
_AttCNMefrLocalCommittedBurst_Type = Integer32
_AttCNMefrLocalCommittedBurst_Object = MibTableColumn
attCNMefrLocalCommittedBurst = _AttCNMefrLocalCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 5),
    _AttCNMefrLocalCommittedBurst_Type()
)
attCNMefrLocalCommittedBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrLocalCommittedBurst.setStatus("mandatory")
_AttCNMefrLocalExcessBurst_Type = Integer32
_AttCNMefrLocalExcessBurst_Object = MibTableColumn
attCNMefrLocalExcessBurst = _AttCNMefrLocalExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 6),
    _AttCNMefrLocalExcessBurst_Type()
)
attCNMefrLocalExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrLocalExcessBurst.setStatus("mandatory")
_AttCNMefrRemoteCIR_Type = Integer32
_AttCNMefrRemoteCIR_Object = MibTableColumn
attCNMefrRemoteCIR = _AttCNMefrRemoteCIR_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 7),
    _AttCNMefrRemoteCIR_Type()
)
attCNMefrRemoteCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrRemoteCIR.setStatus("mandatory")
_AttCNMefrRemoteCommittedBurst_Type = Integer32
_AttCNMefrRemoteCommittedBurst_Object = MibTableColumn
attCNMefrRemoteCommittedBurst = _AttCNMefrRemoteCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 8),
    _AttCNMefrRemoteCommittedBurst_Type()
)
attCNMefrRemoteCommittedBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrRemoteCommittedBurst.setStatus("mandatory")
_AttCNMefrRemoteExcessBurst_Type = Integer32
_AttCNMefrRemoteExcessBurst_Object = MibTableColumn
attCNMefrRemoteExcessBurst = _AttCNMefrRemoteExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 9),
    _AttCNMefrRemoteExcessBurst_Type()
)
attCNMefrRemoteExcessBurst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrRemoteExcessBurst.setStatus("mandatory")
_AttCNMefrMulticastGroup1_Type = Integer32
_AttCNMefrMulticastGroup1_Object = MibTableColumn
attCNMefrMulticastGroup1 = _AttCNMefrMulticastGroup1_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 10),
    _AttCNMefrMulticastGroup1_Type()
)
attCNMefrMulticastGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMulticastGroup1.setStatus("mandatory")
_AttCNMefrMulticastGroup2_Type = Integer32
_AttCNMefrMulticastGroup2_Object = MibTableColumn
attCNMefrMulticastGroup2 = _AttCNMefrMulticastGroup2_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 11),
    _AttCNMefrMulticastGroup2_Type()
)
attCNMefrMulticastGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMulticastGroup2.setStatus("mandatory")
_AttCNMefrMulticastGroup3_Type = Integer32
_AttCNMefrMulticastGroup3_Object = MibTableColumn
attCNMefrMulticastGroup3 = _AttCNMefrMulticastGroup3_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 12),
    _AttCNMefrMulticastGroup3_Type()
)
attCNMefrMulticastGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMulticastGroup3.setStatus("mandatory")
_AttCNMefrMulticastGroup4_Type = Integer32
_AttCNMefrMulticastGroup4_Object = MibTableColumn
attCNMefrMulticastGroup4 = _AttCNMefrMulticastGroup4_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 13),
    _AttCNMefrMulticastGroup4_Type()
)
attCNMefrMulticastGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrMulticastGroup4.setStatus("mandatory")
_AttCNMefrPVCMeasMaxIntervals_Type = Integer32
_AttCNMefrPVCMeasMaxIntervals_Object = MibTableColumn
attCNMefrPVCMeasMaxIntervals = _AttCNMefrPVCMeasMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 14),
    _AttCNMefrPVCMeasMaxIntervals_Type()
)
attCNMefrPVCMeasMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCMeasMaxIntervals.setStatus("mandatory")
_AttCNMefrPVCMeasIntervalLen_Type = Integer32
_AttCNMefrPVCMeasIntervalLen_Object = MibTableColumn
attCNMefrPVCMeasIntervalLen = _AttCNMefrPVCMeasIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 3, 1, 15),
    _AttCNMefrPVCMeasIntervalLen_Type()
)
attCNMefrPVCMeasIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCMeasIntervalLen.setStatus("mandatory")
_AttCNMefrPVCMeasTable_Object = MibTable
attCNMefrPVCMeasTable = _AttCNMefrPVCMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4)
)
if mibBuilder.loadTexts:
    attCNMefrPVCMeasTable.setStatus("mandatory")
_AttCNMefrPVCMeasEntry_Object = MibTableRow
attCNMefrPVCMeasEntry = _AttCNMefrPVCMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1)
)
attCNMefrPVCMeasEntry.setIndexNames(
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrPVCMeasIfIndex"),
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrPVCMeasIndex"),
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrPVCMeasInterval"),
)
if mibBuilder.loadTexts:
    attCNMefrPVCMeasEntry.setStatus("mandatory")
_AttCNMefrPVCMeasIfIndex_Type = Integer32
_AttCNMefrPVCMeasIfIndex_Object = MibTableColumn
attCNMefrPVCMeasIfIndex = _AttCNMefrPVCMeasIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 1),
    _AttCNMefrPVCMeasIfIndex_Type()
)
attCNMefrPVCMeasIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCMeasIfIndex.setStatus("mandatory")
_AttCNMefrPVCMeasIndex_Type = Integer32
_AttCNMefrPVCMeasIndex_Object = MibTableColumn
attCNMefrPVCMeasIndex = _AttCNMefrPVCMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 2),
    _AttCNMefrPVCMeasIndex_Type()
)
attCNMefrPVCMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCMeasIndex.setStatus("mandatory")
_AttCNMefrPVCMeasInterval_Type = Integer32
_AttCNMefrPVCMeasInterval_Object = MibTableColumn
attCNMefrPVCMeasInterval = _AttCNMefrPVCMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 3),
    _AttCNMefrPVCMeasInterval_Type()
)
attCNMefrPVCMeasInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCMeasInterval.setStatus("mandatory")
_AttCNMefrPVCMeasTimeStamp_Type = Integer32
_AttCNMefrPVCMeasTimeStamp_Object = MibTableColumn
attCNMefrPVCMeasTimeStamp = _AttCNMefrPVCMeasTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 4),
    _AttCNMefrPVCMeasTimeStamp_Type()
)
attCNMefrPVCMeasTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCMeasTimeStamp.setStatus("mandatory")


class _AttCNMefrPVCMeasLocalTime_Type(DisplayString):
    """Custom type attCNMefrPVCMeasLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMefrPVCMeasLocalTime_Type.__name__ = "DisplayString"
_AttCNMefrPVCMeasLocalTime_Object = MibTableColumn
attCNMefrPVCMeasLocalTime = _AttCNMefrPVCMeasLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 5),
    _AttCNMefrPVCMeasLocalTime_Type()
)
attCNMefrPVCMeasLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCMeasLocalTime.setStatus("mandatory")
_AttCNMefrPVCReceivedFrames_Type = Gauge32
_AttCNMefrPVCReceivedFrames_Object = MibTableColumn
attCNMefrPVCReceivedFrames = _AttCNMefrPVCReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 6),
    _AttCNMefrPVCReceivedFrames_Type()
)
attCNMefrPVCReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCReceivedFrames.setStatus("mandatory")
_AttCNMefrPVCSentFrames_Type = Gauge32
_AttCNMefrPVCSentFrames_Object = MibTableColumn
attCNMefrPVCSentFrames = _AttCNMefrPVCSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 7),
    _AttCNMefrPVCSentFrames_Type()
)
attCNMefrPVCSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCSentFrames.setStatus("mandatory")
_AttCNMefrDiscardEligibilityFrames_Type = Gauge32
_AttCNMefrDiscardEligibilityFrames_Object = MibTableColumn
attCNMefrDiscardEligibilityFrames = _AttCNMefrDiscardEligibilityFrames_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 8),
    _AttCNMefrDiscardEligibilityFrames_Type()
)
attCNMefrDiscardEligibilityFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrDiscardEligibilityFrames.setStatus("mandatory")
_AttCNMefrBurstSizeExceeded_Type = Gauge32
_AttCNMefrBurstSizeExceeded_Object = MibTableColumn
attCNMefrBurstSizeExceeded = _AttCNMefrBurstSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 9),
    _AttCNMefrBurstSizeExceeded_Type()
)
attCNMefrBurstSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrBurstSizeExceeded.setStatus("mandatory")
_AttCNMefrCongestionAtIngress_Type = Gauge32
_AttCNMefrCongestionAtIngress_Object = MibTableColumn
attCNMefrCongestionAtIngress = _AttCNMefrCongestionAtIngress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 10),
    _AttCNMefrCongestionAtIngress_Type()
)
attCNMefrCongestionAtIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrCongestionAtIngress.setStatus("mandatory")
_AttCNMefrCongestionAtEgress_Type = Gauge32
_AttCNMefrCongestionAtEgress_Object = MibTableColumn
attCNMefrCongestionAtEgress = _AttCNMefrCongestionAtEgress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 4, 1, 11),
    _AttCNMefrCongestionAtEgress_Type()
)
attCNMefrCongestionAtEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrCongestionAtEgress.setStatus("mandatory")
_AttCNMefrPVCStatusTable_Object = MibTable
attCNMefrPVCStatusTable = _AttCNMefrPVCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 5)
)
if mibBuilder.loadTexts:
    attCNMefrPVCStatusTable.setStatus("mandatory")
_AttCNMefrPVCStatusEntry_Object = MibTableRow
attCNMefrPVCStatusEntry = _AttCNMefrPVCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 5, 1)
)
attCNMefrPVCStatusEntry.setIndexNames(
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrPVCStatusIfIndex"),
    (0, "ATT-CNM-ENHANCED-FRAME-RELAY-MIB", "attCNMefrPVCStatusIndex"),
)
if mibBuilder.loadTexts:
    attCNMefrPVCStatusEntry.setStatus("mandatory")
_AttCNMefrPVCStatusIfIndex_Type = Integer32
_AttCNMefrPVCStatusIfIndex_Object = MibTableColumn
attCNMefrPVCStatusIfIndex = _AttCNMefrPVCStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 5, 1, 1),
    _AttCNMefrPVCStatusIfIndex_Type()
)
attCNMefrPVCStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCStatusIfIndex.setStatus("mandatory")
_AttCNMefrPVCStatusIndex_Type = Integer32
_AttCNMefrPVCStatusIndex_Object = MibTableColumn
attCNMefrPVCStatusIndex = _AttCNMefrPVCStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 5, 1, 2),
    _AttCNMefrPVCStatusIndex_Type()
)
attCNMefrPVCStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCStatusIndex.setStatus("mandatory")


class _AttCNMefrPVCAdminStatus_Type(Integer32):
    """Custom type attCNMefrPVCAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_AttCNMefrPVCAdminStatus_Type.__name__ = "Integer32"
_AttCNMefrPVCAdminStatus_Object = MibTableColumn
attCNMefrPVCAdminStatus = _AttCNMefrPVCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 5, 1, 3),
    _AttCNMefrPVCAdminStatus_Type()
)
attCNMefrPVCAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCAdminStatus.setStatus("mandatory")


class _AttCNMefrPVCOperStatus_Type(Integer32):
    """Custom type attCNMefrPVCOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_AttCNMefrPVCOperStatus_Type.__name__ = "Integer32"
_AttCNMefrPVCOperStatus_Object = MibTableColumn
attCNMefrPVCOperStatus = _AttCNMefrPVCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 8, 5, 1, 4),
    _AttCNMefrPVCOperStatus_Type()
)
attCNMefrPVCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMefrPVCOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATT-CNM-ENHANCED-FRAME-RELAY-MIB",
    **{"att-2": att_2,
       "att-products": att_products,
       "att-cnmAgent": att_cnmAgent,
       "att-mgmt": att_mgmt,
       "att-cnm": att_cnm,
       "att-cnm-efr": att_cnm_efr,
       "attCNMefrConfigTable": attCNMefrConfigTable,
       "attCNMefrConfigEntry": attCNMefrConfigEntry,
       "attCNMefrConfigIndex": attCNMefrConfigIndex,
       "attCNMefrMgmtType": attCNMefrMgmtType,
       "attCNMefrPollDirection": attCNMefrPollDirection,
       "attCNMefrFullStatusPoll": attCNMefrFullStatusPoll,
       "attCNMefrErrorThreshold": attCNMefrErrorThreshold,
       "attCNMefrMonitoredEvents": attCNMefrMonitoredEvents,
       "attCNMefrIntegrityTimer": attCNMefrIntegrityTimer,
       "attCNMefrPollVerifyTimer": attCNMefrPollVerifyTimer,
       "attCNMefrLMIFlowControl": attCNMefrLMIFlowControl,
       "attCNMefrSupportedPVCs": attCNMefrSupportedPVCs,
       "attCNMefrMeasMaxIntervals": attCNMefrMeasMaxIntervals,
       "attCNMefrMeasIntervalLen": attCNMefrMeasIntervalLen,
       "attCNMefrMeasTable": attCNMefrMeasTable,
       "attCNMefrMeasEntry": attCNMefrMeasEntry,
       "attCNMefrMeasIndex": attCNMefrMeasIndex,
       "attCNMefrMeasInterval": attCNMefrMeasInterval,
       "attCNMefrMeasTimeStamp": attCNMefrMeasTimeStamp,
       "attCNMefrMeasLocalTime": attCNMefrMeasLocalTime,
       "attCNMefrReceivedOctets": attCNMefrReceivedOctets,
       "attCNMefrSentOctets": attCNMefrSentOctets,
       "attCNMefrReceivedFrames": attCNMefrReceivedFrames,
       "attCNMefrSentFrames": attCNMefrSentFrames,
       "attCNMefrBadFrames": attCNMefrBadFrames,
       "attCNMefrReceiverOverruns": attCNMefrReceiverOverruns,
       "attCNMefrIngressUtil": attCNMefrIngressUtil,
       "attCNMefrEgressUtil": attCNMefrEgressUtil,
       "attCNMefrPVCConfigTable": attCNMefrPVCConfigTable,
       "attCNMefrPVCConfigEntry": attCNMefrPVCConfigEntry,
       "attCNMefrPVCConfigIfIndex": attCNMefrPVCConfigIfIndex,
       "attCNMefrPVCConfigIndex": attCNMefrPVCConfigIndex,
       "attCNMefrPVCServiceType": attCNMefrPVCServiceType,
       "attCNMefrLocalCIR": attCNMefrLocalCIR,
       "attCNMefrLocalCommittedBurst": attCNMefrLocalCommittedBurst,
       "attCNMefrLocalExcessBurst": attCNMefrLocalExcessBurst,
       "attCNMefrRemoteCIR": attCNMefrRemoteCIR,
       "attCNMefrRemoteCommittedBurst": attCNMefrRemoteCommittedBurst,
       "attCNMefrRemoteExcessBurst": attCNMefrRemoteExcessBurst,
       "attCNMefrMulticastGroup1": attCNMefrMulticastGroup1,
       "attCNMefrMulticastGroup2": attCNMefrMulticastGroup2,
       "attCNMefrMulticastGroup3": attCNMefrMulticastGroup3,
       "attCNMefrMulticastGroup4": attCNMefrMulticastGroup4,
       "attCNMefrPVCMeasMaxIntervals": attCNMefrPVCMeasMaxIntervals,
       "attCNMefrPVCMeasIntervalLen": attCNMefrPVCMeasIntervalLen,
       "attCNMefrPVCMeasTable": attCNMefrPVCMeasTable,
       "attCNMefrPVCMeasEntry": attCNMefrPVCMeasEntry,
       "attCNMefrPVCMeasIfIndex": attCNMefrPVCMeasIfIndex,
       "attCNMefrPVCMeasIndex": attCNMefrPVCMeasIndex,
       "attCNMefrPVCMeasInterval": attCNMefrPVCMeasInterval,
       "attCNMefrPVCMeasTimeStamp": attCNMefrPVCMeasTimeStamp,
       "attCNMefrPVCMeasLocalTime": attCNMefrPVCMeasLocalTime,
       "attCNMefrPVCReceivedFrames": attCNMefrPVCReceivedFrames,
       "attCNMefrPVCSentFrames": attCNMefrPVCSentFrames,
       "attCNMefrDiscardEligibilityFrames": attCNMefrDiscardEligibilityFrames,
       "attCNMefrBurstSizeExceeded": attCNMefrBurstSizeExceeded,
       "attCNMefrCongestionAtIngress": attCNMefrCongestionAtIngress,
       "attCNMefrCongestionAtEgress": attCNMefrCongestionAtEgress,
       "attCNMefrPVCStatusTable": attCNMefrPVCStatusTable,
       "attCNMefrPVCStatusEntry": attCNMefrPVCStatusEntry,
       "attCNMefrPVCStatusIfIndex": attCNMefrPVCStatusIfIndex,
       "attCNMefrPVCStatusIndex": attCNMefrPVCStatusIndex,
       "attCNMefrPVCAdminStatus": attCNMefrPVCAdminStatus,
       "attCNMefrPVCOperStatus": attCNMefrPVCOperStatus}
)
