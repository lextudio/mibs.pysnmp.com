# SNMP MIB module (TPT-HIGH-AVAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-HIGH-AVAIL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:56 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(EnabledOrNot,) = mibBuilder.importSymbols(
    "TPT-PORT-CONFIG-MIB",
    "EnabledOrNot")

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_high_avail_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6)
)
tpt_high_avail_objs.setRevisions(
        ("2016-09-08 18:54",
         "2016-05-25 18:54")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FaultState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fallback", 1),
          ("normal", 0))
    )



class FaultCause(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("hard-disk-disable", 11),
          ("hardware-breakpoint", 3),
          ("initialization-failure", 12),
          ("internal-link-failure", 13),
          ("low-health-score", 20),
          ("multiple-fan-failures", 14),
          ("none", 0),
          ("oam-fault", 10),
          ("out-of-memory", 2),
          ("packet-egress-integrity", 15),
          ("process-error", 19),
          ("software-watchdog-timeout", 9),
          ("spike-reboot-or-halt", 18),
          ("stack-master", 16),
          ("suspended-task", 1),
          ("threshold-failure", 8),
          ("tse-failure", 4),
          ("user-fallback", 7),
          ("user-reset", 6),
          ("waiting-on-stack", 17),
          ("watchdog-timeout", 5))
    )



class ConnectionState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("not-connected", 0),
          ("unresponsive", 1))
    )



class PerfProtPhase(Integer32, TextualConvention):
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
        *(("continuing", 2),
          ("entering", 1),
          ("exiting", 3))
    )



class ZphaState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ips-bypass", 1),
          ("normal", 0))
    )



class ZphaAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("normal", 1),
          ("unknown", 0))
    )



class ZphaMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multi", 3),
          ("single", 2),
          ("unknown", 0))
    )



class ZphaPresent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HighAvailTimeStamp_Type = Unsigned32
_HighAvailTimeStamp_Object = MibScalar
highAvailTimeStamp = _HighAvailTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 1),
    _HighAvailTimeStamp_Type()
)
highAvailTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailTimeStamp.setStatus("current")
_HighAvailFaultState_Type = FaultState
_HighAvailFaultState_Object = MibScalar
highAvailFaultState = _HighAvailFaultState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 2),
    _HighAvailFaultState_Type()
)
highAvailFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailFaultState.setStatus("current")
_HighAvailFaultCause_Type = FaultCause
_HighAvailFaultCause_Object = MibScalar
highAvailFaultCause = _HighAvailFaultCause_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 3),
    _HighAvailFaultCause_Type()
)
highAvailFaultCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailFaultCause.setStatus("current")
_HighAvailThresholdEnabled_Type = EnabledOrNot
_HighAvailThresholdEnabled_Object = MibScalar
highAvailThresholdEnabled = _HighAvailThresholdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 4),
    _HighAvailThresholdEnabled_Type()
)
highAvailThresholdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailThresholdEnabled.setStatus("current")
_HighAvailThresholdPercent_Type = Integer32
_HighAvailThresholdPercent_Object = MibScalar
highAvailThresholdPercent = _HighAvailThresholdPercent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 5),
    _HighAvailThresholdPercent_Type()
)
highAvailThresholdPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailThresholdPercent.setStatus("current")
_HighAvailEnabled_Type = EnabledOrNot
_HighAvailEnabled_Object = MibScalar
highAvailEnabled = _HighAvailEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 6),
    _HighAvailEnabled_Type()
)
highAvailEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailEnabled.setStatus("current")
_HighAvailTransparentState_Type = ConnectionState
_HighAvailTransparentState_Object = MibScalar
highAvailTransparentState = _HighAvailTransparentState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 7),
    _HighAvailTransparentState_Type()
)
highAvailTransparentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailTransparentState.setStatus("current")
_HighAvailTransparentEnabled_Type = EnabledOrNot
_HighAvailTransparentEnabled_Object = MibScalar
highAvailTransparentEnabled = _HighAvailTransparentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 8),
    _HighAvailTransparentEnabled_Type()
)
highAvailTransparentEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailTransparentEnabled.setStatus("current")


class _HighAvailTransparentPartner_Type(OctetString):
    """Custom type highAvailTransparentPartner based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HighAvailTransparentPartner_Type.__name__ = "OctetString"
_HighAvailTransparentPartner_Object = MibScalar
highAvailTransparentPartner = _HighAvailTransparentPartner_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 9),
    _HighAvailTransparentPartner_Type()
)
highAvailTransparentPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailTransparentPartner.setStatus("current")
_HighAvailZeroPowerState_Type = ZphaState
_HighAvailZeroPowerState_Object = MibScalar
highAvailZeroPowerState = _HighAvailZeroPowerState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 10),
    _HighAvailZeroPowerState_Type()
)
highAvailZeroPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailZeroPowerState.setStatus("current")
_HighAvailZeroPowerQuantity_Type = Unsigned32
_HighAvailZeroPowerQuantity_Object = MibScalar
highAvailZeroPowerQuantity = _HighAvailZeroPowerQuantity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 11),
    _HighAvailZeroPowerQuantity_Type()
)
highAvailZeroPowerQuantity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailZeroPowerQuantity.setStatus("current")
_HighAvailZeroPowerTable_Object = MibTable
highAvailZeroPowerTable = _HighAvailZeroPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12)
)
if mibBuilder.loadTexts:
    highAvailZeroPowerTable.setStatus("current")
_HighAvailZeroPowerEntry_Object = MibTableRow
highAvailZeroPowerEntry = _HighAvailZeroPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1)
)
highAvailZeroPowerEntry.setIndexNames(
    (0, "TPT-HIGH-AVAIL-MIB", "highAvailZeroPowerIndex"),
)
if mibBuilder.loadTexts:
    highAvailZeroPowerEntry.setStatus("current")
_HighAvailZeroPowerIndex_Type = Unsigned32
_HighAvailZeroPowerIndex_Object = MibTableColumn
highAvailZeroPowerIndex = _HighAvailZeroPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 1),
    _HighAvailZeroPowerIndex_Type()
)
highAvailZeroPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    highAvailZeroPowerIndex.setStatus("current")


class _HighAvailZeroPowerSegment_Type(OctetString):
    """Custom type highAvailZeroPowerSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HighAvailZeroPowerSegment_Type.__name__ = "OctetString"
_HighAvailZeroPowerSegment_Object = MibTableColumn
highAvailZeroPowerSegment = _HighAvailZeroPowerSegment_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 2),
    _HighAvailZeroPowerSegment_Type()
)
highAvailZeroPowerSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailZeroPowerSegment.setStatus("current")
_HighAvailZeroPowerActive_Type = ZphaState
_HighAvailZeroPowerActive_Object = MibTableColumn
highAvailZeroPowerActive = _HighAvailZeroPowerActive_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 3),
    _HighAvailZeroPowerActive_Type()
)
highAvailZeroPowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailZeroPowerActive.setStatus("current")
_HighAvailZeroPowerAction_Type = ZphaAction
_HighAvailZeroPowerAction_Object = MibTableColumn
highAvailZeroPowerAction = _HighAvailZeroPowerAction_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 4),
    _HighAvailZeroPowerAction_Type()
)
highAvailZeroPowerAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailZeroPowerAction.setStatus("current")
_HighAvailZeroPowerMode_Type = ZphaMode
_HighAvailZeroPowerMode_Object = MibTableColumn
highAvailZeroPowerMode = _HighAvailZeroPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 12, 1, 5),
    _HighAvailZeroPowerMode_Type()
)
highAvailZeroPowerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailZeroPowerMode.setStatus("current")
_HighAvailZeroPowerPresence_Type = ZphaPresent
_HighAvailZeroPowerPresence_Object = MibScalar
highAvailZeroPowerPresence = _HighAvailZeroPowerPresence_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 6, 13),
    _HighAvailZeroPowerPresence_Type()
)
highAvailZeroPowerPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highAvailZeroPowerPresence.setStatus("current")


class _TptIhaNotifyDeviceID_Type(OctetString):
    """Custom type tptIhaNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptIhaNotifyDeviceID_Type.__name__ = "OctetString"
_TptIhaNotifyDeviceID_Object = MibScalar
tptIhaNotifyDeviceID = _TptIhaNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 81),
    _TptIhaNotifyDeviceID_Type()
)
tptIhaNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptIhaNotifyDeviceID.setStatus("current")
_TptIhaNotifyTimeStamp_Type = Unsigned32
_TptIhaNotifyTimeStamp_Object = MibScalar
tptIhaNotifyTimeStamp = _TptIhaNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 82),
    _TptIhaNotifyTimeStamp_Type()
)
tptIhaNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptIhaNotifyTimeStamp.setStatus("current")
_TptIhaNotifyFaultState_Type = FaultState
_TptIhaNotifyFaultState_Object = MibScalar
tptIhaNotifyFaultState = _TptIhaNotifyFaultState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 83),
    _TptIhaNotifyFaultState_Type()
)
tptIhaNotifyFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptIhaNotifyFaultState.setStatus("current")
_TptIhaNotifyFaultCause_Type = FaultCause
_TptIhaNotifyFaultCause_Object = MibScalar
tptIhaNotifyFaultCause = _TptIhaNotifyFaultCause_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 84),
    _TptIhaNotifyFaultCause_Type()
)
tptIhaNotifyFaultCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptIhaNotifyFaultCause.setStatus("current")


class _TptTrhaNotifyDeviceID_Type(OctetString):
    """Custom type tptTrhaNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptTrhaNotifyDeviceID_Type.__name__ = "OctetString"
_TptTrhaNotifyDeviceID_Object = MibScalar
tptTrhaNotifyDeviceID = _TptTrhaNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 86),
    _TptTrhaNotifyDeviceID_Type()
)
tptTrhaNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTrhaNotifyDeviceID.setStatus("current")
_TptTrhaNotifyTimeStamp_Type = Unsigned32
_TptTrhaNotifyTimeStamp_Object = MibScalar
tptTrhaNotifyTimeStamp = _TptTrhaNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 87),
    _TptTrhaNotifyTimeStamp_Type()
)
tptTrhaNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTrhaNotifyTimeStamp.setStatus("current")
_TptTrhaNotifyNewState_Type = ConnectionState
_TptTrhaNotifyNewState_Object = MibScalar
tptTrhaNotifyNewState = _TptTrhaNotifyNewState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 88),
    _TptTrhaNotifyNewState_Type()
)
tptTrhaNotifyNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTrhaNotifyNewState.setStatus("current")


class _TptPerfProtNotifyDeviceID_Type(OctetString):
    """Custom type tptPerfProtNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptPerfProtNotifyDeviceID_Type.__name__ = "OctetString"
_TptPerfProtNotifyDeviceID_Object = MibScalar
tptPerfProtNotifyDeviceID = _TptPerfProtNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 141),
    _TptPerfProtNotifyDeviceID_Type()
)
tptPerfProtNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPerfProtNotifyDeviceID.setStatus("current")
_TptPerfProtNotifyTimeStamp_Type = Unsigned32
_TptPerfProtNotifyTimeStamp_Object = MibScalar
tptPerfProtNotifyTimeStamp = _TptPerfProtNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 142),
    _TptPerfProtNotifyTimeStamp_Type()
)
tptPerfProtNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPerfProtNotifyTimeStamp.setStatus("current")
_TptPerfProtNotifyPhase_Type = PerfProtPhase
_TptPerfProtNotifyPhase_Object = MibScalar
tptPerfProtNotifyPhase = _TptPerfProtNotifyPhase_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 143),
    _TptPerfProtNotifyPhase_Type()
)
tptPerfProtNotifyPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPerfProtNotifyPhase.setStatus("current")
_TptPerfProtNotifyPacketLoss_Type = Unsigned32
_TptPerfProtNotifyPacketLoss_Object = MibScalar
tptPerfProtNotifyPacketLoss = _TptPerfProtNotifyPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 144),
    _TptPerfProtNotifyPacketLoss_Type()
)
tptPerfProtNotifyPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPerfProtNotifyPacketLoss.setStatus("current")
_TptPerfProtNotifyLossThreshold_Type = Unsigned32
_TptPerfProtNotifyLossThreshold_Object = MibScalar
tptPerfProtNotifyLossThreshold = _TptPerfProtNotifyLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 145),
    _TptPerfProtNotifyLossThreshold_Type()
)
tptPerfProtNotifyLossThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPerfProtNotifyLossThreshold.setStatus("current")
_TptPerfProtNotifyDuration_Type = Unsigned32
_TptPerfProtNotifyDuration_Object = MibScalar
tptPerfProtNotifyDuration = _TptPerfProtNotifyDuration_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 146),
    _TptPerfProtNotifyDuration_Type()
)
tptPerfProtNotifyDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPerfProtNotifyDuration.setStatus("current")
_TptPerfProtNotifyMissedAlerts_Type = Counter64
_TptPerfProtNotifyMissedAlerts_Object = MibScalar
tptPerfProtNotifyMissedAlerts = _TptPerfProtNotifyMissedAlerts_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 147),
    _TptPerfProtNotifyMissedAlerts_Type()
)
tptPerfProtNotifyMissedAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptPerfProtNotifyMissedAlerts.setStatus("current")


class _TptZphaNotifyDeviceID_Type(OctetString):
    """Custom type tptZphaNotifyDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptZphaNotifyDeviceID_Type.__name__ = "OctetString"
_TptZphaNotifyDeviceID_Object = MibScalar
tptZphaNotifyDeviceID = _TptZphaNotifyDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 161),
    _TptZphaNotifyDeviceID_Type()
)
tptZphaNotifyDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptZphaNotifyDeviceID.setStatus("current")
_TptZphaNotifyTimeStamp_Type = Unsigned32
_TptZphaNotifyTimeStamp_Object = MibScalar
tptZphaNotifyTimeStamp = _TptZphaNotifyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 162),
    _TptZphaNotifyTimeStamp_Type()
)
tptZphaNotifyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptZphaNotifyTimeStamp.setStatus("current")


class _TptZphaNotifySegmentName_Type(OctetString):
    """Custom type tptZphaNotifySegmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TptZphaNotifySegmentName_Type.__name__ = "OctetString"
_TptZphaNotifySegmentName_Object = MibScalar
tptZphaNotifySegmentName = _TptZphaNotifySegmentName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 163),
    _TptZphaNotifySegmentName_Type()
)
tptZphaNotifySegmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptZphaNotifySegmentName.setStatus("current")
_TptZphaNotifyNewState_Type = ZphaState
_TptZphaNotifyNewState_Object = MibScalar
tptZphaNotifyNewState = _TptZphaNotifyNewState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 164),
    _TptZphaNotifyNewState_Type()
)
tptZphaNotifyNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptZphaNotifyNewState.setStatus("current")

# Managed Objects groups


# Notification objects

tptIhaNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 15)
)
tptIhaNotify.setObjects(
      *(("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyDeviceID"),
        ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyTimeStamp"),
        ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyFaultState"),
        ("TPT-HIGH-AVAIL-MIB", "tptIhaNotifyFaultCause"))
)
if mibBuilder.loadTexts:
    tptIhaNotify.setStatus(
        "current"
    )

tptTrhaNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 18)
)
tptTrhaNotify.setObjects(
      *(("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyDeviceID"),
        ("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyTimeStamp"),
        ("TPT-HIGH-AVAIL-MIB", "tptTrhaNotifyNewState"))
)
if mibBuilder.loadTexts:
    tptTrhaNotify.setStatus(
        "current"
    )

tptPerfProtNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 21)
)
tptPerfProtNotify.setObjects(
      *(("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyDeviceID"),
        ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyTimeStamp"),
        ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyPhase"),
        ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyPacketLoss"),
        ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyLossThreshold"),
        ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyDuration"),
        ("TPT-HIGH-AVAIL-MIB", "tptPerfProtNotifyMissedAlerts"))
)
if mibBuilder.loadTexts:
    tptPerfProtNotify.setStatus(
        "current"
    )

tptZphaNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 24)
)
tptZphaNotify.setObjects(
      *(("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyDeviceID"),
        ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyTimeStamp"),
        ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifySegmentName"),
        ("TPT-HIGH-AVAIL-MIB", "tptZphaNotifyNewState"))
)
if mibBuilder.loadTexts:
    tptZphaNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-HIGH-AVAIL-MIB",
    **{"FaultState": FaultState,
       "FaultCause": FaultCause,
       "ConnectionState": ConnectionState,
       "PerfProtPhase": PerfProtPhase,
       "ZphaState": ZphaState,
       "ZphaAction": ZphaAction,
       "ZphaMode": ZphaMode,
       "ZphaPresent": ZphaPresent,
       "tpt-high-avail-objs": tpt_high_avail_objs,
       "highAvailTimeStamp": highAvailTimeStamp,
       "highAvailFaultState": highAvailFaultState,
       "highAvailFaultCause": highAvailFaultCause,
       "highAvailThresholdEnabled": highAvailThresholdEnabled,
       "highAvailThresholdPercent": highAvailThresholdPercent,
       "highAvailEnabled": highAvailEnabled,
       "highAvailTransparentState": highAvailTransparentState,
       "highAvailTransparentEnabled": highAvailTransparentEnabled,
       "highAvailTransparentPartner": highAvailTransparentPartner,
       "highAvailZeroPowerState": highAvailZeroPowerState,
       "highAvailZeroPowerQuantity": highAvailZeroPowerQuantity,
       "highAvailZeroPowerTable": highAvailZeroPowerTable,
       "highAvailZeroPowerEntry": highAvailZeroPowerEntry,
       "highAvailZeroPowerIndex": highAvailZeroPowerIndex,
       "highAvailZeroPowerSegment": highAvailZeroPowerSegment,
       "highAvailZeroPowerActive": highAvailZeroPowerActive,
       "highAvailZeroPowerAction": highAvailZeroPowerAction,
       "highAvailZeroPowerMode": highAvailZeroPowerMode,
       "highAvailZeroPowerPresence": highAvailZeroPowerPresence,
       "tptIhaNotify": tptIhaNotify,
       "tptTrhaNotify": tptTrhaNotify,
       "tptPerfProtNotify": tptPerfProtNotify,
       "tptZphaNotify": tptZphaNotify,
       "tptIhaNotifyDeviceID": tptIhaNotifyDeviceID,
       "tptIhaNotifyTimeStamp": tptIhaNotifyTimeStamp,
       "tptIhaNotifyFaultState": tptIhaNotifyFaultState,
       "tptIhaNotifyFaultCause": tptIhaNotifyFaultCause,
       "tptTrhaNotifyDeviceID": tptTrhaNotifyDeviceID,
       "tptTrhaNotifyTimeStamp": tptTrhaNotifyTimeStamp,
       "tptTrhaNotifyNewState": tptTrhaNotifyNewState,
       "tptPerfProtNotifyDeviceID": tptPerfProtNotifyDeviceID,
       "tptPerfProtNotifyTimeStamp": tptPerfProtNotifyTimeStamp,
       "tptPerfProtNotifyPhase": tptPerfProtNotifyPhase,
       "tptPerfProtNotifyPacketLoss": tptPerfProtNotifyPacketLoss,
       "tptPerfProtNotifyLossThreshold": tptPerfProtNotifyLossThreshold,
       "tptPerfProtNotifyDuration": tptPerfProtNotifyDuration,
       "tptPerfProtNotifyMissedAlerts": tptPerfProtNotifyMissedAlerts,
       "tptZphaNotifyDeviceID": tptZphaNotifyDeviceID,
       "tptZphaNotifyTimeStamp": tptZphaNotifyTimeStamp,
       "tptZphaNotifySegmentName": tptZphaNotifySegmentName,
       "tptZphaNotifyNewState": tptZphaNotifyNewState}
)
