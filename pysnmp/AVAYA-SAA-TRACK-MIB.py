# SNMP MIB module (AVAYA-SAA-TRACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-SAA-TRACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:34 2024
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

(avGatewayMibs,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "avGatewayMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

avayaSaaTrackMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2)
)
avayaSaaTrackMib.setRevisions(
        ("2007-01-08 16:57",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvstrMIBObjects_ObjectIdentity = ObjectIdentity
avstrMIBObjects = _AvstrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1)
)
_AvstrRtrMIBObjects_ObjectIdentity = ObjectIdentity
avstrRtrMIBObjects = _AvstrRtrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1)
)
_AvstrRtrTable_Object = MibTable
avstrRtrTable = _AvstrRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    avstrRtrTable.setStatus("current")
_AvstrRtrEntry_Object = MibTableRow
avstrRtrEntry = _AvstrRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1)
)
avstrRtrEntry.setIndexNames(
    (0, "AVAYA-SAA-TRACK-MIB", "avstrRtrId"),
)
if mibBuilder.loadTexts:
    avstrRtrEntry.setStatus("current")
_AvstrRtrId_Type = Unsigned32
_AvstrRtrId_Object = MibTableColumn
avstrRtrId = _AvstrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 1),
    _AvstrRtrId_Type()
)
avstrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avstrRtrId.setStatus("current")


class _AvstrRtrType_Type(Integer32):
    """Custom type avstrRtrType based on Integer32"""
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
        *(("ipIcmpEcho", 2),
          ("none", 1),
          ("tcpConnect", 3))
    )


_AvstrRtrType_Type.__name__ = "Integer32"
_AvstrRtrType_Object = MibTableColumn
avstrRtrType = _AvstrRtrType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 2),
    _AvstrRtrType_Type()
)
avstrRtrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrType.setStatus("current")
_AvstrRtrDestIp_Type = IpAddress
_AvstrRtrDestIp_Object = MibTableColumn
avstrRtrDestIp = _AvstrRtrDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 3),
    _AvstrRtrDestIp_Type()
)
avstrRtrDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrDestIp.setStatus("current")


class _AvstrRtrDestPort_Type(Integer32):
    """Custom type avstrRtrDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvstrRtrDestPort_Type.__name__ = "Integer32"
_AvstrRtrDestPort_Object = MibTableColumn
avstrRtrDestPort = _AvstrRtrDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 4),
    _AvstrRtrDestPort_Type()
)
avstrRtrDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrDestPort.setStatus("current")


class _AvstrRtrFrequencyMs_Type(Unsigned32):
    """Custom type avstrRtrFrequencyMs based on Unsigned32"""
    defaultValue = 5000


_AvstrRtrFrequencyMs_Object = MibTableColumn
avstrRtrFrequencyMs = _AvstrRtrFrequencyMs_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 5),
    _AvstrRtrFrequencyMs_Type()
)
avstrRtrFrequencyMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrFrequencyMs.setStatus("current")


class _AvstrRtrWaitIntervalMs_Type(Unsigned32):
    """Custom type avstrRtrWaitIntervalMs based on Unsigned32"""
    defaultValue = 5000


_AvstrRtrWaitIntervalMs_Object = MibTableColumn
avstrRtrWaitIntervalMs = _AvstrRtrWaitIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 6),
    _AvstrRtrWaitIntervalMs_Type()
)
avstrRtrWaitIntervalMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrWaitIntervalMs.setStatus("current")


class _AvstrRtrFailRetries_Type(Unsigned32):
    """Custom type avstrRtrFailRetries based on Unsigned32"""
    defaultValue = 5


_AvstrRtrFailRetries_Object = MibTableColumn
avstrRtrFailRetries = _AvstrRtrFailRetries_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 7),
    _AvstrRtrFailRetries_Type()
)
avstrRtrFailRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrFailRetries.setStatus("current")


class _AvstrRtrSuccessRetries_Type(Unsigned32):
    """Custom type avstrRtrSuccessRetries based on Unsigned32"""
    defaultValue = 1


_AvstrRtrSuccessRetries_Object = MibTableColumn
avstrRtrSuccessRetries = _AvstrRtrSuccessRetries_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 8),
    _AvstrRtrSuccessRetries_Type()
)
avstrRtrSuccessRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrSuccessRetries.setStatus("current")


class _AvstrRtrProbeDscp_Type(Unsigned32):
    """Custom type avstrRtrProbeDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AvstrRtrProbeDscp_Type.__name__ = "Unsigned32"
_AvstrRtrProbeDscp_Object = MibTableColumn
avstrRtrProbeDscp = _AvstrRtrProbeDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 9),
    _AvstrRtrProbeDscp_Type()
)
avstrRtrProbeDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrProbeDscp.setStatus("current")


class _AvstrRtrProbeSrcIpAddr_Type(IpAddress):
    """Custom type avstrRtrProbeSrcIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AvstrRtrProbeSrcIpAddr_Object = MibTableColumn
avstrRtrProbeSrcIpAddr = _AvstrRtrProbeSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 10),
    _AvstrRtrProbeSrcIpAddr_Type()
)
avstrRtrProbeSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrProbeSrcIpAddr.setStatus("current")


class _AvstrRtrProbeNextHopIf_Type(InterfaceIndex):
    """Custom type avstrRtrProbeNextHopIf based on InterfaceIndex"""
    defaultValue = 0


_AvstrRtrProbeNextHopIf_Object = MibTableColumn
avstrRtrProbeNextHopIf = _AvstrRtrProbeNextHopIf_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 11),
    _AvstrRtrProbeNextHopIf_Type()
)
avstrRtrProbeNextHopIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrProbeNextHopIf.setStatus("current")


class _AvstrRtrProbeNextHopMac_Type(MacAddress):
    """Custom type avstrRtrProbeNextHopMac based on MacAddress"""
    defaultHexValue = "000000000000"


_AvstrRtrProbeNextHopMac_Object = MibTableColumn
avstrRtrProbeNextHopMac = _AvstrRtrProbeNextHopMac_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 12),
    _AvstrRtrProbeNextHopMac_Type()
)
avstrRtrProbeNextHopMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrProbeNextHopMac.setStatus("current")


class _AvstrRtrSchedule_Type(Integer32):
    """Custom type avstrRtrSchedule based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AvstrRtrSchedule_Type.__name__ = "Integer32"
_AvstrRtrSchedule_Object = MibTableColumn
avstrRtrSchedule = _AvstrRtrSchedule_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 13),
    _AvstrRtrSchedule_Type()
)
avstrRtrSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrSchedule.setStatus("current")


class _AvstrRtrOperState_Type(Integer32):
    """Custom type avstrRtrOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("inactive", 1),
          ("up", 2))
    )


_AvstrRtrOperState_Type.__name__ = "Integer32"
_AvstrRtrOperState_Object = MibTableColumn
avstrRtrOperState = _AvstrRtrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 14),
    _AvstrRtrOperState_Type()
)
avstrRtrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrRtrOperState.setStatus("current")
_AvstrRtrOperStateLastChange_Type = TimeTicks
_AvstrRtrOperStateLastChange_Object = MibTableColumn
avstrRtrOperStateLastChange = _AvstrRtrOperStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 15),
    _AvstrRtrOperStateLastChange_Type()
)
avstrRtrOperStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrRtrOperStateLastChange.setStatus("current")
_AvstrRtrRowStatus_Type = RowStatus
_AvstrRtrRowStatus_Object = MibTableColumn
avstrRtrRowStatus = _AvstrRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 16),
    _AvstrRtrRowStatus_Type()
)
avstrRtrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrRowStatus.setStatus("current")


class _AvstrRtrProbeNextHopIp_Type(IpAddress):
    """Custom type avstrRtrProbeNextHopIp based on IpAddress"""
    defaultHexValue = "00000000"


_AvstrRtrProbeNextHopIp_Object = MibTableColumn
avstrRtrProbeNextHopIp = _AvstrRtrProbeNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 17),
    _AvstrRtrProbeNextHopIp_Type()
)
avstrRtrProbeNextHopIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrProbeNextHopIp.setStatus("current")


class _AvstrRtrIfKpaliveBypass_Type(TruthValue):
    """Custom type avstrRtrIfKpaliveBypass based on TruthValue"""


_AvstrRtrIfKpaliveBypass_Object = MibTableColumn
avstrRtrIfKpaliveBypass = _AvstrRtrIfKpaliveBypass_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 18),
    _AvstrRtrIfKpaliveBypass_Type()
)
avstrRtrIfKpaliveBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrIfKpaliveBypass.setStatus("current")


class _AvstrRtrDestHostName_Type(DisplayString):
    """Custom type avstrRtrDestHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AvstrRtrDestHostName_Type.__name__ = "DisplayString"
_AvstrRtrDestHostName_Object = MibTableColumn
avstrRtrDestHostName = _AvstrRtrDestHostName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 19),
    _AvstrRtrDestHostName_Type()
)
avstrRtrDestHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrRtrDestHostName.setStatus("current")
_AvstrRtrResolvedIp_Type = IpAddress
_AvstrRtrResolvedIp_Object = MibTableColumn
avstrRtrResolvedIp = _AvstrRtrResolvedIp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 1, 1, 1, 20),
    _AvstrRtrResolvedIp_Type()
)
avstrRtrResolvedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrRtrResolvedIp.setStatus("current")
_AvstrTrackerMIBObjects_ObjectIdentity = ObjectIdentity
avstrTrackerMIBObjects = _AvstrTrackerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2)
)
_AvstrTrackerTable_Object = MibTable
avstrTrackerTable = _AvstrTrackerTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    avstrTrackerTable.setStatus("current")
_AvstrTrackerEntry_Object = MibTableRow
avstrTrackerEntry = _AvstrTrackerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1)
)
avstrTrackerEntry.setIndexNames(
    (0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerId"),
)
if mibBuilder.loadTexts:
    avstrTrackerEntry.setStatus("current")
_AvstrTrackerId_Type = Unsigned32
_AvstrTrackerId_Object = MibTableColumn
avstrTrackerId = _AvstrTrackerId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 1),
    _AvstrTrackerId_Type()
)
avstrTrackerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avstrTrackerId.setStatus("current")


class _AvstrTrackerDescription_Type(DisplayString):
    """Custom type avstrTrackerDescription based on DisplayString"""
    defaultHexValue = ""


_AvstrTrackerDescription_Object = MibTableColumn
avstrTrackerDescription = _AvstrTrackerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 2),
    _AvstrTrackerDescription_Type()
)
avstrTrackerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerDescription.setStatus("current")


class _AvstrTrackerType_Type(Integer32):
    """Custom type avstrTrackerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("list", 1),
          ("rtr", 2))
    )


_AvstrTrackerType_Type.__name__ = "Integer32"
_AvstrTrackerType_Object = MibTableColumn
avstrTrackerType = _AvstrTrackerType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 3),
    _AvstrTrackerType_Type()
)
avstrTrackerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerType.setStatus("current")
_AvstrTrackerRtrId_Type = Unsigned32
_AvstrTrackerRtrId_Object = MibTableColumn
avstrTrackerRtrId = _AvstrTrackerRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 4),
    _AvstrTrackerRtrId_Type()
)
avstrTrackerRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerRtrId.setStatus("current")


class _AvstrTrackerListType_Type(Integer32):
    """Custom type avstrTrackerListType based on Integer32"""
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
        *(("boolAnd", 1),
          ("boolOr", 2),
          ("threshCount", 3))
    )


_AvstrTrackerListType_Type.__name__ = "Integer32"
_AvstrTrackerListType_Object = MibTableColumn
avstrTrackerListType = _AvstrTrackerListType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 5),
    _AvstrTrackerListType_Type()
)
avstrTrackerListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerListType.setStatus("current")
_AvstrTrackerListThresholdUp_Type = Unsigned32
_AvstrTrackerListThresholdUp_Object = MibTableColumn
avstrTrackerListThresholdUp = _AvstrTrackerListThresholdUp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 6),
    _AvstrTrackerListThresholdUp_Type()
)
avstrTrackerListThresholdUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerListThresholdUp.setStatus("current")
_AvstrTrackerListThresholdDown_Type = Unsigned32
_AvstrTrackerListThresholdDown_Object = MibTableColumn
avstrTrackerListThresholdDown = _AvstrTrackerListThresholdDown_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 7),
    _AvstrTrackerListThresholdDown_Type()
)
avstrTrackerListThresholdDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerListThresholdDown.setStatus("current")


class _AvstrTrackerOperState_Type(Integer32):
    """Custom type avstrTrackerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("reserved", 1),
          ("up", 2))
    )


_AvstrTrackerOperState_Type.__name__ = "Integer32"
_AvstrTrackerOperState_Object = MibTableColumn
avstrTrackerOperState = _AvstrTrackerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 8),
    _AvstrTrackerOperState_Type()
)
avstrTrackerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrTrackerOperState.setStatus("current")
_AvstrTrackerOperStateLastChange_Type = TimeTicks
_AvstrTrackerOperStateLastChange_Object = MibTableColumn
avstrTrackerOperStateLastChange = _AvstrTrackerOperStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 9),
    _AvstrTrackerOperStateLastChange_Type()
)
avstrTrackerOperStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrTrackerOperStateLastChange.setStatus("current")
_AvstrTrackerRowStatus_Type = RowStatus
_AvstrTrackerRowStatus_Object = MibTableColumn
avstrTrackerRowStatus = _AvstrTrackerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 10),
    _AvstrTrackerRowStatus_Type()
)
avstrTrackerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerRowStatus.setStatus("current")


class _AvstrTrackerPermanentTrackState_Type(TruthValue):
    """Custom type avstrTrackerPermanentTrackState based on TruthValue"""


_AvstrTrackerPermanentTrackState_Object = MibTableColumn
avstrTrackerPermanentTrackState = _AvstrTrackerPermanentTrackState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 1, 1, 11),
    _AvstrTrackerPermanentTrackState_Type()
)
avstrTrackerPermanentTrackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerPermanentTrackState.setStatus("current")
_AvstrTrackerListObjsTable_Object = MibTable
avstrTrackerListObjsTable = _AvstrTrackerListObjsTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    avstrTrackerListObjsTable.setStatus("current")
_AvstrTrackerListObjsEntry_Object = MibTableRow
avstrTrackerListObjsEntry = _AvstrTrackerListObjsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1)
)
avstrTrackerListObjsEntry.setIndexNames(
    (0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsParentTrackId"),
    (0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsChildTrackId"),
)
if mibBuilder.loadTexts:
    avstrTrackerListObjsEntry.setStatus("current")
_AvstrTrackerListObjsParentTrackId_Type = Unsigned32
_AvstrTrackerListObjsParentTrackId_Object = MibTableColumn
avstrTrackerListObjsParentTrackId = _AvstrTrackerListObjsParentTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 1),
    _AvstrTrackerListObjsParentTrackId_Type()
)
avstrTrackerListObjsParentTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avstrTrackerListObjsParentTrackId.setStatus("current")
_AvstrTrackerListObjsChildTrackId_Type = Unsigned32
_AvstrTrackerListObjsChildTrackId_Object = MibTableColumn
avstrTrackerListObjsChildTrackId = _AvstrTrackerListObjsChildTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 2),
    _AvstrTrackerListObjsChildTrackId_Type()
)
avstrTrackerListObjsChildTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avstrTrackerListObjsChildTrackId.setStatus("current")
_AvstrTrackerListObjsRowStatus_Type = RowStatus
_AvstrTrackerListObjsRowStatus_Object = MibTableColumn
avstrTrackerListObjsRowStatus = _AvstrTrackerListObjsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 3),
    _AvstrTrackerListObjsRowStatus_Type()
)
avstrTrackerListObjsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerListObjsRowStatus.setStatus("current")


class _AvstrTrackerListObjsReverseState_Type(TruthValue):
    """Custom type avstrTrackerListObjsReverseState based on TruthValue"""


_AvstrTrackerListObjsReverseState_Object = MibTableColumn
avstrTrackerListObjsReverseState = _AvstrTrackerListObjsReverseState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 2, 1, 4),
    _AvstrTrackerListObjsReverseState_Type()
)
avstrTrackerListObjsReverseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avstrTrackerListObjsReverseState.setStatus("current")
_AvstrTrackerPtrsTable_Object = MibTable
avstrTrackerPtrsTable = _AvstrTrackerPtrsTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    avstrTrackerPtrsTable.setStatus("current")
_AvstrTrackerPtrsEntry_Object = MibTableRow
avstrTrackerPtrsEntry = _AvstrTrackerPtrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1)
)
avstrTrackerPtrsEntry.setIndexNames(
    (0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsTrackId"),
    (0, "AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsIndex"),
)
if mibBuilder.loadTexts:
    avstrTrackerPtrsEntry.setStatus("current")
_AvstrTrackerPtrsTrackId_Type = Unsigned32
_AvstrTrackerPtrsTrackId_Object = MibTableColumn
avstrTrackerPtrsTrackId = _AvstrTrackerPtrsTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 1),
    _AvstrTrackerPtrsTrackId_Type()
)
avstrTrackerPtrsTrackId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avstrTrackerPtrsTrackId.setStatus("current")
_AvstrTrackerPtrsIndex_Type = Unsigned32
_AvstrTrackerPtrsIndex_Object = MibTableColumn
avstrTrackerPtrsIndex = _AvstrTrackerPtrsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 2),
    _AvstrTrackerPtrsIndex_Type()
)
avstrTrackerPtrsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avstrTrackerPtrsIndex.setStatus("current")


class _AvstrTrackerPtrsDescription_Type(DisplayString):
    """Custom type avstrTrackerPtrsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AvstrTrackerPtrsDescription_Type.__name__ = "DisplayString"
_AvstrTrackerPtrsDescription_Object = MibTableColumn
avstrTrackerPtrsDescription = _AvstrTrackerPtrsDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 3),
    _AvstrTrackerPtrsDescription_Type()
)
avstrTrackerPtrsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrTrackerPtrsDescription.setStatus("current")


class _AvstrTrackerPtrsType_Type(Integer32):
    """Custom type avstrTrackerPtrsType based on Integer32"""
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
        *(("ifIndex", 3),
          ("ipPbrNhListEntry", 6),
          ("ipStaticRoute", 5),
          ("isakmpPeer", 4),
          ("none", 1),
          ("trackerList", 2))
    )


_AvstrTrackerPtrsType_Type.__name__ = "Integer32"
_AvstrTrackerPtrsType_Object = MibTableColumn
avstrTrackerPtrsType = _AvstrTrackerPtrsType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 4),
    _AvstrTrackerPtrsType_Type()
)
avstrTrackerPtrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrTrackerPtrsType.setStatus("current")
_AvstrTrackerPtrsValue_Type = OctetString
_AvstrTrackerPtrsValue_Object = MibTableColumn
avstrTrackerPtrsValue = _AvstrTrackerPtrsValue_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 1, 2, 3, 1, 5),
    _AvstrTrackerPtrsValue_Type()
)
avstrTrackerPtrsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avstrTrackerPtrsValue.setStatus("current")
_AvstrMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
avstrMIBNotificationPrefix = _AvstrMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 2)
)
_AvstrMIBNotifications_ObjectIdentity = ObjectIdentity
avstrMIBNotifications = _AvstrMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 2, 0)
)
_AvstrMIBConformance_ObjectIdentity = ObjectIdentity
avstrMIBConformance = _AvstrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3)
)
_AvstrMIBGroups_ObjectIdentity = ObjectIdentity
avstrMIBGroups = _AvstrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1)
)
_AvstrMIBCompliances_ObjectIdentity = ObjectIdentity
avstrMIBCompliances = _AvstrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 2)
)

# Managed Objects groups

avstrRtrConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 1)
)
avstrRtrConfigGroup.setObjects(
      *(("AVAYA-SAA-TRACK-MIB", "avstrRtrType"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrFrequencyMs"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrWaitIntervalMs"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrFailRetries"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrSuccessRetries"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeDscp"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeSrcIpAddr"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeNextHopIf"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeNextHopMac"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrSchedule"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrDestPort"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrIfKpaliveBypass"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrProbeNextHopIp"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrRowStatus"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrDestIp"))
)
if mibBuilder.loadTexts:
    avstrRtrConfigGroup.setStatus("current")

avstrRtrMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 2)
)
avstrRtrMonitoringGroup.setObjects(
      *(("AVAYA-SAA-TRACK-MIB", "avstrRtrOperState"),
        ("AVAYA-SAA-TRACK-MIB", "avstrRtrOperStateLastChange"))
)
if mibBuilder.loadTexts:
    avstrRtrMonitoringGroup.setStatus("current")

avstrTrackerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 3)
)
avstrTrackerConfigGroup.setObjects(
      *(("AVAYA-SAA-TRACK-MIB", "avstrTrackerType"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerRtrId"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListType"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerRowStatus"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsRowStatus"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListObjsReverseState"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListThresholdUp"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerDescription"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerListThresholdDown"))
)
if mibBuilder.loadTexts:
    avstrTrackerConfigGroup.setStatus("current")

avstrTrackerMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 1, 4)
)
avstrTrackerMonitoringGroup.setObjects(
      *(("AVAYA-SAA-TRACK-MIB", "avstrTrackerOperState"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerOperStateLastChange"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsDescription"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsType"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerPtrsValue"))
)
if mibBuilder.loadTexts:
    avstrTrackerMonitoringGroup.setStatus("current")


# Notification objects

avstrTrackerOperStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 2, 0, 1)
)
avstrTrackerOperStateChangeNotification.setObjects(
      *(("AVAYA-SAA-TRACK-MIB", "avstrTrackerOperState"),
        ("AVAYA-SAA-TRACK-MIB", "avstrTrackerDescription"))
)
if mibBuilder.loadTexts:
    avstrTrackerOperStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

avstrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    avstrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-SAA-TRACK-MIB",
    **{"avayaSaaTrackMib": avayaSaaTrackMib,
       "avstrMIBObjects": avstrMIBObjects,
       "avstrRtrMIBObjects": avstrRtrMIBObjects,
       "avstrRtrTable": avstrRtrTable,
       "avstrRtrEntry": avstrRtrEntry,
       "avstrRtrId": avstrRtrId,
       "avstrRtrType": avstrRtrType,
       "avstrRtrDestIp": avstrRtrDestIp,
       "avstrRtrDestPort": avstrRtrDestPort,
       "avstrRtrFrequencyMs": avstrRtrFrequencyMs,
       "avstrRtrWaitIntervalMs": avstrRtrWaitIntervalMs,
       "avstrRtrFailRetries": avstrRtrFailRetries,
       "avstrRtrSuccessRetries": avstrRtrSuccessRetries,
       "avstrRtrProbeDscp": avstrRtrProbeDscp,
       "avstrRtrProbeSrcIpAddr": avstrRtrProbeSrcIpAddr,
       "avstrRtrProbeNextHopIf": avstrRtrProbeNextHopIf,
       "avstrRtrProbeNextHopMac": avstrRtrProbeNextHopMac,
       "avstrRtrSchedule": avstrRtrSchedule,
       "avstrRtrOperState": avstrRtrOperState,
       "avstrRtrOperStateLastChange": avstrRtrOperStateLastChange,
       "avstrRtrRowStatus": avstrRtrRowStatus,
       "avstrRtrProbeNextHopIp": avstrRtrProbeNextHopIp,
       "avstrRtrIfKpaliveBypass": avstrRtrIfKpaliveBypass,
       "avstrRtrDestHostName": avstrRtrDestHostName,
       "avstrRtrResolvedIp": avstrRtrResolvedIp,
       "avstrTrackerMIBObjects": avstrTrackerMIBObjects,
       "avstrTrackerTable": avstrTrackerTable,
       "avstrTrackerEntry": avstrTrackerEntry,
       "avstrTrackerId": avstrTrackerId,
       "avstrTrackerDescription": avstrTrackerDescription,
       "avstrTrackerType": avstrTrackerType,
       "avstrTrackerRtrId": avstrTrackerRtrId,
       "avstrTrackerListType": avstrTrackerListType,
       "avstrTrackerListThresholdUp": avstrTrackerListThresholdUp,
       "avstrTrackerListThresholdDown": avstrTrackerListThresholdDown,
       "avstrTrackerOperState": avstrTrackerOperState,
       "avstrTrackerOperStateLastChange": avstrTrackerOperStateLastChange,
       "avstrTrackerRowStatus": avstrTrackerRowStatus,
       "avstrTrackerPermanentTrackState": avstrTrackerPermanentTrackState,
       "avstrTrackerListObjsTable": avstrTrackerListObjsTable,
       "avstrTrackerListObjsEntry": avstrTrackerListObjsEntry,
       "avstrTrackerListObjsParentTrackId": avstrTrackerListObjsParentTrackId,
       "avstrTrackerListObjsChildTrackId": avstrTrackerListObjsChildTrackId,
       "avstrTrackerListObjsRowStatus": avstrTrackerListObjsRowStatus,
       "avstrTrackerListObjsReverseState": avstrTrackerListObjsReverseState,
       "avstrTrackerPtrsTable": avstrTrackerPtrsTable,
       "avstrTrackerPtrsEntry": avstrTrackerPtrsEntry,
       "avstrTrackerPtrsTrackId": avstrTrackerPtrsTrackId,
       "avstrTrackerPtrsIndex": avstrTrackerPtrsIndex,
       "avstrTrackerPtrsDescription": avstrTrackerPtrsDescription,
       "avstrTrackerPtrsType": avstrTrackerPtrsType,
       "avstrTrackerPtrsValue": avstrTrackerPtrsValue,
       "avstrMIBNotificationPrefix": avstrMIBNotificationPrefix,
       "avstrMIBNotifications": avstrMIBNotifications,
       "avstrTrackerOperStateChangeNotification": avstrTrackerOperStateChangeNotification,
       "avstrMIBConformance": avstrMIBConformance,
       "avstrMIBGroups": avstrMIBGroups,
       "avstrRtrConfigGroup": avstrRtrConfigGroup,
       "avstrRtrMonitoringGroup": avstrRtrMonitoringGroup,
       "avstrTrackerConfigGroup": avstrTrackerConfigGroup,
       "avstrTrackerMonitoringGroup": avstrTrackerMonitoringGroup,
       "avstrMIBCompliances": avstrMIBCompliances,
       "avstrMIBCompliance": avstrMIBCompliance}
)
