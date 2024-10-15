# SNMP MIB module (WWP-VOICE-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-VOICE-GATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:27 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpVoiceGatewayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43)
)
wwpVoiceGatewayMIB.setRevisions(
        ("2002-11-18 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpVoiceGatewayMIBObjects_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayMIBObjects = _WwpVoiceGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1)
)
_WwpVoiceGateway_ObjectIdentity = ObjectIdentity
wwpVoiceGateway = _WwpVoiceGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1)
)
_WwpVoiceGatewayMGCP_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayMGCP = _WwpVoiceGatewayMGCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1)
)
_WwpVoiceGatewayEndPointTable_Object = MibTable
wwpVoiceGatewayEndPointTable = _WwpVoiceGatewayEndPointTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpVoiceGatewayEndPointTable.setStatus("current")
_WwpVoiceGatewayEndPointEntry_Object = MibTableRow
wwpVoiceGatewayEndPointEntry = _WwpVoiceGatewayEndPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 1, 1)
)
wwpVoiceGatewayEndPointEntry.setIndexNames(
    (0, "WWP-VOICE-GATEWAY-MIB", "wwpVoiceGatewayEndPointId"),
)
if mibBuilder.loadTexts:
    wwpVoiceGatewayEndPointEntry.setStatus("current")


class _WwpVoiceGatewayEndPointId_Type(Integer32):
    """Custom type wwpVoiceGatewayEndPointId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpVoiceGatewayEndPointId_Type.__name__ = "Integer32"
_WwpVoiceGatewayEndPointId_Object = MibTableColumn
wwpVoiceGatewayEndPointId = _WwpVoiceGatewayEndPointId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 1, 1, 1),
    _WwpVoiceGatewayEndPointId_Type()
)
wwpVoiceGatewayEndPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayEndPointId.setStatus("current")
_WwpVoiceGatewayEndpoint_Type = DisplayString
_WwpVoiceGatewayEndpoint_Object = MibTableColumn
wwpVoiceGatewayEndpoint = _WwpVoiceGatewayEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 1, 1, 2),
    _WwpVoiceGatewayEndpoint_Type()
)
wwpVoiceGatewayEndpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayEndpoint.setStatus("current")
_WwpVoiceGatewayCallAgentAddr_Type = DisplayString
_WwpVoiceGatewayCallAgentAddr_Object = MibScalar
wwpVoiceGatewayCallAgentAddr = _WwpVoiceGatewayCallAgentAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 2),
    _WwpVoiceGatewayCallAgentAddr_Type()
)
wwpVoiceGatewayCallAgentAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayCallAgentAddr.setStatus("current")


class _WwpVoiceGatewayCallAgentUDPPort_Type(Integer32):
    """Custom type wwpVoiceGatewayCallAgentUDPPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_WwpVoiceGatewayCallAgentUDPPort_Type.__name__ = "Integer32"
_WwpVoiceGatewayCallAgentUDPPort_Object = MibScalar
wwpVoiceGatewayCallAgentUDPPort = _WwpVoiceGatewayCallAgentUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 3),
    _WwpVoiceGatewayCallAgentUDPPort_Type()
)
wwpVoiceGatewayCallAgentUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayCallAgentUDPPort.setStatus("current")


class _WwpVoiceGatewayCallAgentProtocol_Type(Integer32):
    """Custom type wwpVoiceGatewayCallAgentProtocol based on Integer32"""
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
        *(("mgcp1Ncs1NoPackages", 3),
          ("ncs1", 1),
          ("rfc2705", 2))
    )


_WwpVoiceGatewayCallAgentProtocol_Type.__name__ = "Integer32"
_WwpVoiceGatewayCallAgentProtocol_Object = MibScalar
wwpVoiceGatewayCallAgentProtocol = _WwpVoiceGatewayCallAgentProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 4),
    _WwpVoiceGatewayCallAgentProtocol_Type()
)
wwpVoiceGatewayCallAgentProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayCallAgentProtocol.setStatus("current")


class _WwpVoiceGatewaySupportMessagePiggybacking_Type(TruthValue):
    """Custom type wwpVoiceGatewaySupportMessagePiggybacking based on TruthValue"""


_WwpVoiceGatewaySupportMessagePiggybacking_Object = MibScalar
wwpVoiceGatewaySupportMessagePiggybacking = _WwpVoiceGatewaySupportMessagePiggybacking_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 5),
    _WwpVoiceGatewaySupportMessagePiggybacking_Type()
)
wwpVoiceGatewaySupportMessagePiggybacking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySupportMessagePiggybacking.setStatus("current")


class _WwpVoiceGatewayRsipKeepAliveEnable_Type(TruthValue):
    """Custom type wwpVoiceGatewayRsipKeepAliveEnable based on TruthValue"""


_WwpVoiceGatewayRsipKeepAliveEnable_Object = MibScalar
wwpVoiceGatewayRsipKeepAliveEnable = _WwpVoiceGatewayRsipKeepAliveEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 6),
    _WwpVoiceGatewayRsipKeepAliveEnable_Type()
)
wwpVoiceGatewayRsipKeepAliveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayRsipKeepAliveEnable.setStatus("current")


class _WwpVoiceGatewayRsipKeepAliveInterval_Type(Integer32):
    """Custom type wwpVoiceGatewayRsipKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_WwpVoiceGatewayRsipKeepAliveInterval_Type.__name__ = "Integer32"
_WwpVoiceGatewayRsipKeepAliveInterval_Object = MibScalar
wwpVoiceGatewayRsipKeepAliveInterval = _WwpVoiceGatewayRsipKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 1, 7),
    _WwpVoiceGatewayRsipKeepAliveInterval_Type()
)
wwpVoiceGatewayRsipKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayRsipKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceGatewayRsipKeepAliveInterval.setUnits("seconds")
_WwpVoiceGatewayCountry_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayCountry = _WwpVoiceGatewayCountry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 2)
)


class _WwpVoiceGatewayCountryCodes_Type(Integer32):
    """Custom type wwpVoiceGatewayCountryCodes based on Integer32"""
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
        *(("dubai", 2),
          ("holland", 3),
          ("newZealand", 4),
          ("sweden", 6),
          ("uk", 5),
          ("usa", 1))
    )


_WwpVoiceGatewayCountryCodes_Type.__name__ = "Integer32"
_WwpVoiceGatewayCountryCodes_Object = MibScalar
wwpVoiceGatewayCountryCodes = _WwpVoiceGatewayCountryCodes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 2, 1),
    _WwpVoiceGatewayCountryCodes_Type()
)
wwpVoiceGatewayCountryCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayCountryCodes.setStatus("current")
_WwpVoiceGatewayCodec_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayCodec = _WwpVoiceGatewayCodec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 3)
)


class _WwpVoiceGatewayComplexCodec_Type(Integer32):
    """Custom type wwpVoiceGatewayComplexCodec based on Integer32"""
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
        *(("g711", 2),
          ("g723", 3),
          ("g726", 4),
          ("g729", 5),
          ("none", 1))
    )


_WwpVoiceGatewayComplexCodec_Type.__name__ = "Integer32"
_WwpVoiceGatewayComplexCodec_Object = MibScalar
wwpVoiceGatewayComplexCodec = _WwpVoiceGatewayComplexCodec_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 3, 1),
    _WwpVoiceGatewayComplexCodec_Type()
)
wwpVoiceGatewayComplexCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayComplexCodec.setStatus("current")


class _WwpVoiceGatewaySilenceSuppression_Type(Integer32):
    """Custom type wwpVoiceGatewaySilenceSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpVoiceGatewaySilenceSuppression_Type.__name__ = "Integer32"
_WwpVoiceGatewaySilenceSuppression_Object = MibScalar
wwpVoiceGatewaySilenceSuppression = _WwpVoiceGatewaySilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 3, 2),
    _WwpVoiceGatewaySilenceSuppression_Type()
)
wwpVoiceGatewaySilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySilenceSuppression.setStatus("current")


class _WwpVoiceGatewayEchoCancellation_Type(Integer32):
    """Custom type wwpVoiceGatewayEchoCancellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpVoiceGatewayEchoCancellation_Type.__name__ = "Integer32"
_WwpVoiceGatewayEchoCancellation_Object = MibScalar
wwpVoiceGatewayEchoCancellation = _WwpVoiceGatewayEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 3, 3),
    _WwpVoiceGatewayEchoCancellation_Type()
)
wwpVoiceGatewayEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayEchoCancellation.setStatus("current")
_WwpVoiceGatewayPacketizationMinPeriod_Type = Integer32
_WwpVoiceGatewayPacketizationMinPeriod_Object = MibScalar
wwpVoiceGatewayPacketizationMinPeriod = _WwpVoiceGatewayPacketizationMinPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 3, 4),
    _WwpVoiceGatewayPacketizationMinPeriod_Type()
)
wwpVoiceGatewayPacketizationMinPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPacketizationMinPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPacketizationMinPeriod.setUnits("milliseconds")
_WwpVoiceGatewayPacketizationMaxPeriod_Type = Integer32
_WwpVoiceGatewayPacketizationMaxPeriod_Object = MibScalar
wwpVoiceGatewayPacketizationMaxPeriod = _WwpVoiceGatewayPacketizationMaxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 3, 5),
    _WwpVoiceGatewayPacketizationMaxPeriod_Type()
)
wwpVoiceGatewayPacketizationMaxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPacketizationMaxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPacketizationMaxPeriod.setUnits("milliseconds")
_WwpVoiceGatewayAudio_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayAudio = _WwpVoiceGatewayAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 4)
)


class _WwpVoiceGatewayPayloadType_Type(Integer32):
    """Custom type wwpVoiceGatewayPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(94, 127),
    )


_WwpVoiceGatewayPayloadType_Type.__name__ = "Integer32"
_WwpVoiceGatewayPayloadType_Object = MibScalar
wwpVoiceGatewayPayloadType = _WwpVoiceGatewayPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 4, 1),
    _WwpVoiceGatewayPayloadType_Type()
)
wwpVoiceGatewayPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPayloadType.setStatus("current")
_WwpVoiceGatewaySendEventsViaRFC2833_Type = TruthValue
_WwpVoiceGatewaySendEventsViaRFC2833_Object = MibScalar
wwpVoiceGatewaySendEventsViaRFC2833 = _WwpVoiceGatewaySendEventsViaRFC2833_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 4, 2),
    _WwpVoiceGatewaySendEventsViaRFC2833_Type()
)
wwpVoiceGatewaySendEventsViaRFC2833.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySendEventsViaRFC2833.setStatus("current")
_WwpVoiceGatewayDropVoicePktsDuringEvents_Type = TruthValue
_WwpVoiceGatewayDropVoicePktsDuringEvents_Object = MibScalar
wwpVoiceGatewayDropVoicePktsDuringEvents = _WwpVoiceGatewayDropVoicePktsDuringEvents_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 4, 3),
    _WwpVoiceGatewayDropVoicePktsDuringEvents_Type()
)
wwpVoiceGatewayDropVoicePktsDuringEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayDropVoicePktsDuringEvents.setStatus("current")
_WwpVoiceGatewaySquelchInbandDtmfAudio_Type = TruthValue
_WwpVoiceGatewaySquelchInbandDtmfAudio_Object = MibScalar
wwpVoiceGatewaySquelchInbandDtmfAudio = _WwpVoiceGatewaySquelchInbandDtmfAudio_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 4, 4),
    _WwpVoiceGatewaySquelchInbandDtmfAudio_Type()
)
wwpVoiceGatewaySquelchInbandDtmfAudio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySquelchInbandDtmfAudio.setStatus("current")
_WwpVoiceGatewayStats_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayStats = _WwpVoiceGatewayStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5)
)
_WwpVoiceGatewayPktsTx_Type = Counter32
_WwpVoiceGatewayPktsTx_Object = MibScalar
wwpVoiceGatewayPktsTx = _WwpVoiceGatewayPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 1),
    _WwpVoiceGatewayPktsTx_Type()
)
wwpVoiceGatewayPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPktsTx.setStatus("current")
_WwpVoiceGatewayOctetsTx_Type = Counter32
_WwpVoiceGatewayOctetsTx_Object = MibScalar
wwpVoiceGatewayOctetsTx = _WwpVoiceGatewayOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 2),
    _WwpVoiceGatewayOctetsTx_Type()
)
wwpVoiceGatewayOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayOctetsTx.setStatus("current")
_WwpVoiceGatewayPktsRx_Type = Counter32
_WwpVoiceGatewayPktsRx_Object = MibScalar
wwpVoiceGatewayPktsRx = _WwpVoiceGatewayPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 3),
    _WwpVoiceGatewayPktsRx_Type()
)
wwpVoiceGatewayPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPktsRx.setStatus("current")
_WwpVoiceGatewayOctetsRx_Type = Counter32
_WwpVoiceGatewayOctetsRx_Object = MibScalar
wwpVoiceGatewayOctetsRx = _WwpVoiceGatewayOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 4),
    _WwpVoiceGatewayOctetsRx_Type()
)
wwpVoiceGatewayOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayOctetsRx.setStatus("current")
_WwpVoiceGatewayPktsLost_Type = Counter32
_WwpVoiceGatewayPktsLost_Object = MibScalar
wwpVoiceGatewayPktsLost = _WwpVoiceGatewayPktsLost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 5),
    _WwpVoiceGatewayPktsLost_Type()
)
wwpVoiceGatewayPktsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayPktsLost.setStatus("current")
_WwpVoiceGatewayIntervalJitter_Type = Integer32
_WwpVoiceGatewayIntervalJitter_Object = MibScalar
wwpVoiceGatewayIntervalJitter = _WwpVoiceGatewayIntervalJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 6),
    _WwpVoiceGatewayIntervalJitter_Type()
)
wwpVoiceGatewayIntervalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayIntervalJitter.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceGatewayIntervalJitter.setUnits("milliseconds")
_WwpVoiceGatewayLatency_Type = Integer32
_WwpVoiceGatewayLatency_Object = MibScalar
wwpVoiceGatewayLatency = _WwpVoiceGatewayLatency_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 7),
    _WwpVoiceGatewayLatency_Type()
)
wwpVoiceGatewayLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayLatency.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceGatewayLatency.setUnits("milliseconds")


class _WwpVoiceGatewayResetStatCounters_Type(Integer32):
    """Custom type wwpVoiceGatewayResetStatCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_WwpVoiceGatewayResetStatCounters_Type.__name__ = "Integer32"
_WwpVoiceGatewayResetStatCounters_Object = MibScalar
wwpVoiceGatewayResetStatCounters = _WwpVoiceGatewayResetStatCounters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 5, 8),
    _WwpVoiceGatewayResetStatCounters_Type()
)
wwpVoiceGatewayResetStatCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayResetStatCounters.setStatus("current")
_WwpVoiceReset_ObjectIdentity = ObjectIdentity
wwpVoiceReset = _WwpVoiceReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 6)
)


class _WwpVoiceGatewayNumResets_Type(Unsigned32):
    """Custom type wwpVoiceGatewayNumResets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpVoiceGatewayNumResets_Type.__name__ = "Unsigned32"
_WwpVoiceGatewayNumResets_Object = MibScalar
wwpVoiceGatewayNumResets = _WwpVoiceGatewayNumResets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 6, 1),
    _WwpVoiceGatewayNumResets_Type()
)
wwpVoiceGatewayNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayNumResets.setStatus("current")


class _WwpVoiceGatewayReset_Type(Integer32):
    """Custom type wwpVoiceGatewayReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1),
          ("resetDefault", 2))
    )


_WwpVoiceGatewayReset_Type.__name__ = "Integer32"
_WwpVoiceGatewayReset_Object = MibScalar
wwpVoiceGatewayReset = _WwpVoiceGatewayReset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 6, 2),
    _WwpVoiceGatewayReset_Type()
)
wwpVoiceGatewayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayReset.setStatus("current")
_WwpVoiceSec_ObjectIdentity = ObjectIdentity
wwpVoiceSec = _WwpVoiceSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 7)
)


class _WwpVoiceAccess_Type(Integer32):
    """Custom type wwpVoiceAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_WwpVoiceAccess_Type.__name__ = "Integer32"
_WwpVoiceAccess_Object = MibScalar
wwpVoiceAccess = _WwpVoiceAccess_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 7, 1),
    _WwpVoiceAccess_Type()
)
wwpVoiceAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceAccess.setStatus("current")


class _WwpMgmtAccess_Type(Integer32):
    """Custom type wwpMgmtAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_WwpMgmtAccess_Type.__name__ = "Integer32"
_WwpMgmtAccess_Object = MibScalar
wwpMgmtAccess = _WwpMgmtAccess_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 7, 2),
    _WwpMgmtAccess_Type()
)
wwpMgmtAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpMgmtAccess.setStatus("current")
_WwpVoiceGatewayConfigCallAgent_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigCallAgent = _WwpVoiceGatewayConfigCallAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 8)
)


class _WwpVoiceCallAgentOtaModes_Type(Integer32):
    """Custom type wwpVoiceCallAgentOtaModes based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifOtaRecv", 1),
          ("sendOta", 2))
    )


_WwpVoiceCallAgentOtaModes_Type.__name__ = "Integer32"
_WwpVoiceCallAgentOtaModes_Object = MibScalar
wwpVoiceCallAgentOtaModes = _WwpVoiceCallAgentOtaModes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 8, 1),
    _WwpVoiceCallAgentOtaModes_Type()
)
wwpVoiceCallAgentOtaModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceCallAgentOtaModes.setStatus("current")


class _WwpVoiceCallAgentEgressEvent_Type(Integer32):
    """Custom type wwpVoiceCallAgentEgressEvent based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendIngressEgressNotif", 1),
          ("sendIngressNotif", 2))
    )


_WwpVoiceCallAgentEgressEvent_Type.__name__ = "Integer32"
_WwpVoiceCallAgentEgressEvent_Object = MibScalar
wwpVoiceCallAgentEgressEvent = _WwpVoiceCallAgentEgressEvent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 8, 2),
    _WwpVoiceCallAgentEgressEvent_Type()
)
wwpVoiceCallAgentEgressEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceCallAgentEgressEvent.setStatus("current")
_WwpVoiceGatewayConfigPots_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigPots = _WwpVoiceGatewayConfigPots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 9)
)


class _WwpVoiceCallAgentPotsLine_Type(Integer32):
    """Custom type wwpVoiceCallAgentPotsLine based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable1PotLine", 1),
          ("enable2PotLine", 2))
    )


_WwpVoiceCallAgentPotsLine_Type.__name__ = "Integer32"
_WwpVoiceCallAgentPotsLine_Object = MibScalar
wwpVoiceCallAgentPotsLine = _WwpVoiceCallAgentPotsLine_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 9, 1),
    _WwpVoiceCallAgentPotsLine_Type()
)
wwpVoiceCallAgentPotsLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceCallAgentPotsLine.setStatus("current")
_WwpVoiceGatewayConfigFax_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigFax = _WwpVoiceGatewayConfigFax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 10)
)


class _WwpVoiceAutonomousFaxState_Type(Integer32):
    """Custom type wwpVoiceAutonomousFaxState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpVoiceAutonomousFaxState_Type.__name__ = "Integer32"
_WwpVoiceAutonomousFaxState_Object = MibScalar
wwpVoiceAutonomousFaxState = _WwpVoiceAutonomousFaxState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 10, 1),
    _WwpVoiceAutonomousFaxState_Type()
)
wwpVoiceAutonomousFaxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceAutonomousFaxState.setStatus("current")
_WwpVoiceGatewayConfigEndPoint_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigEndPoint = _WwpVoiceGatewayConfigEndPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 11)
)


class _WwpVoiceEndPointName_Type(Integer32):
    """Custom type wwpVoiceEndPointName based on Integer32"""
    defaultValue = 2

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
        *(("fqdn", 5),
          ("hostName", 4),
          ("ip", 2),
          ("mac", 3),
          ("unknown", 1))
    )


_WwpVoiceEndPointName_Type.__name__ = "Integer32"
_WwpVoiceEndPointName_Object = MibScalar
wwpVoiceEndPointName = _WwpVoiceEndPointName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 11, 1),
    _WwpVoiceEndPointName_Type()
)
wwpVoiceEndPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceEndPointName.setStatus("current")
_WwpVoiceGatewayConfigNotifEntityCache_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigNotifEntityCache = _WwpVoiceGatewayConfigNotifEntityCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 12)
)


class _WwpVoiceNotifEntCache_Type(Integer32):
    """Custom type wwpVoiceNotifEntCache based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WwpVoiceNotifEntCache_Type.__name__ = "Integer32"
_WwpVoiceNotifEntCache_Object = MibScalar
wwpVoiceNotifEntCache = _WwpVoiceNotifEntCache_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 12, 1),
    _WwpVoiceNotifEntCache_Type()
)
wwpVoiceNotifEntCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceNotifEntCache.setStatus("current")
_WwpVoiceGatewayConfigJitterBuffer_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigJitterBuffer = _WwpVoiceGatewayConfigJitterBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 13)
)


class _WwpVoiceJitterOptionState_Type(Integer32):
    """Custom type wwpVoiceJitterOptionState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpVoiceJitterOptionState_Type.__name__ = "Integer32"
_WwpVoiceJitterOptionState_Object = MibScalar
wwpVoiceJitterOptionState = _WwpVoiceJitterOptionState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 13, 1),
    _WwpVoiceJitterOptionState_Type()
)
wwpVoiceJitterOptionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceJitterOptionState.setStatus("current")
_WwpVoiceGatewayConfigJitterBufferMinPeriod_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigJitterBufferMinPeriod = _WwpVoiceGatewayConfigJitterBufferMinPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 14)
)
_WwpVoiceJitterBufferMinPeriod_Type = Integer32
_WwpVoiceJitterBufferMinPeriod_Object = MibScalar
wwpVoiceJitterBufferMinPeriod = _WwpVoiceJitterBufferMinPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 14, 1),
    _WwpVoiceJitterBufferMinPeriod_Type()
)
wwpVoiceJitterBufferMinPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceJitterBufferMinPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceJitterBufferMinPeriod.setUnits("milliseconds")
_WwpVoiceGatewayConfigJitterBufferMaxPeriod_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigJitterBufferMaxPeriod = _WwpVoiceGatewayConfigJitterBufferMaxPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 15)
)
_WwpVoiceJitterBufferMaxPeriod_Type = Integer32
_WwpVoiceJitterBufferMaxPeriod_Object = MibScalar
wwpVoiceJitterBufferMaxPeriod = _WwpVoiceJitterBufferMaxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 15, 1),
    _WwpVoiceJitterBufferMaxPeriod_Type()
)
wwpVoiceJitterBufferMaxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceJitterBufferMaxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceJitterBufferMaxPeriod.setUnits("milliseconds")
_WwpVoiceGatewayConfigJitterBufferTargetPeriod_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigJitterBufferTargetPeriod = _WwpVoiceGatewayConfigJitterBufferTargetPeriod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 16)
)
_WwpVoiceJitterBufferTargetPeriod_Type = Integer32
_WwpVoiceJitterBufferTargetPeriod_Object = MibScalar
wwpVoiceJitterBufferTargetPeriod = _WwpVoiceJitterBufferTargetPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 16, 1),
    _WwpVoiceJitterBufferTargetPeriod_Type()
)
wwpVoiceJitterBufferTargetPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceJitterBufferTargetPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceJitterBufferTargetPeriod.setUnits("milliseconds")
_WwpVoiceGatewayConfigCodecOverride_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigCodecOverride = _WwpVoiceGatewayConfigCodecOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 17)
)


class _WwpVoiceGatewayCodecOverride_Type(Integer32):
    """Custom type wwpVoiceGatewayCodecOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711PCMA", 2),
          ("g711PCMU", 1))
    )


_WwpVoiceGatewayCodecOverride_Type.__name__ = "Integer32"
_WwpVoiceGatewayCodecOverride_Object = MibScalar
wwpVoiceGatewayCodecOverride = _WwpVoiceGatewayCodecOverride_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 17, 1),
    _WwpVoiceGatewayCodecOverride_Type()
)
wwpVoiceGatewayCodecOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayCodecOverride.setStatus("current")
_WwpVoiceGatewayConfigTestServerConnection_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigTestServerConnection = _WwpVoiceGatewayConfigTestServerConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 18)
)


class _WwpVoiceGatewayTestServerConnection_Type(Integer32):
    """Custom type wwpVoiceGatewayTestServerConnection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_WwpVoiceGatewayTestServerConnection_Type.__name__ = "Integer32"
_WwpVoiceGatewayTestServerConnection_Object = MibScalar
wwpVoiceGatewayTestServerConnection = _WwpVoiceGatewayTestServerConnection_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 18, 1),
    _WwpVoiceGatewayTestServerConnection_Type()
)
wwpVoiceGatewayTestServerConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayTestServerConnection.setStatus("current")
_WwpVoiceGatewayConfigLastServerResponseTime_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigLastServerResponseTime = _WwpVoiceGatewayConfigLastServerResponseTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 19)
)


class _WwpVoiceGatewayLastServerResponseTime_Type(OctetString):
    """Custom type wwpVoiceGatewayLastServerResponseTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpVoiceGatewayLastServerResponseTime_Type.__name__ = "OctetString"
_WwpVoiceGatewayLastServerResponseTime_Object = MibScalar
wwpVoiceGatewayLastServerResponseTime = _WwpVoiceGatewayLastServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 19, 1),
    _WwpVoiceGatewayLastServerResponseTime_Type()
)
wwpVoiceGatewayLastServerResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewayLastServerResponseTime.setStatus("current")
_WwpVoiceGatewaySIP_ObjectIdentity = ObjectIdentity
wwpVoiceGatewaySIP = _WwpVoiceGatewaySIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20)
)


class _WwpVoiceGatewaySipSessionTimeoutPeriod_Type(Integer32):
    """Custom type wwpVoiceGatewaySipSessionTimeoutPeriod based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WwpVoiceGatewaySipSessionTimeoutPeriod_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipSessionTimeoutPeriod_Object = MibScalar
wwpVoiceGatewaySipSessionTimeoutPeriod = _WwpVoiceGatewaySipSessionTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 1),
    _WwpVoiceGatewaySipSessionTimeoutPeriod_Type()
)
wwpVoiceGatewaySipSessionTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipSessionTimeoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipSessionTimeoutPeriod.setUnits("seconds")


class _WwpVoiceGatewaySipRegisterTimeoutPeriod_Type(Integer32):
    """Custom type wwpVoiceGatewaySipRegisterTimeoutPeriod based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WwpVoiceGatewaySipRegisterTimeoutPeriod_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipRegisterTimeoutPeriod_Object = MibScalar
wwpVoiceGatewaySipRegisterTimeoutPeriod = _WwpVoiceGatewaySipRegisterTimeoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 2),
    _WwpVoiceGatewaySipRegisterTimeoutPeriod_Type()
)
wwpVoiceGatewaySipRegisterTimeoutPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipRegisterTimeoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipRegisterTimeoutPeriod.setUnits("seconds")


class _WwpVoiceGatewaySipForceQuotesState_Type(Integer32):
    """Custom type wwpVoiceGatewaySipForceQuotesState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WwpVoiceGatewaySipForceQuotesState_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipForceQuotesState_Object = MibScalar
wwpVoiceGatewaySipForceQuotesState = _WwpVoiceGatewaySipForceQuotesState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 3),
    _WwpVoiceGatewaySipForceQuotesState_Type()
)
wwpVoiceGatewaySipForceQuotesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipForceQuotesState.setStatus("current")
_WwpVoiceGatewaySipPhoneLineTable_Object = MibTable
wwpVoiceGatewaySipPhoneLineTable = _WwpVoiceGatewaySipPhoneLineTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4)
)
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipPhoneLineTable.setStatus("current")
_WwpVoiceGatewaySipPhoneLineEntry_Object = MibTableRow
wwpVoiceGatewaySipPhoneLineEntry = _WwpVoiceGatewaySipPhoneLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4, 1)
)
wwpVoiceGatewaySipPhoneLineEntry.setIndexNames(
    (0, "WWP-VOICE-GATEWAY-MIB", "wwpVoiceGatewaySipLineId"),
)
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipPhoneLineEntry.setStatus("current")


class _WwpVoiceGatewaySipLineId_Type(Integer32):
    """Custom type wwpVoiceGatewaySipLineId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpVoiceGatewaySipLineId_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipLineId_Object = MibTableColumn
wwpVoiceGatewaySipLineId = _WwpVoiceGatewaySipLineId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4, 1, 1),
    _WwpVoiceGatewaySipLineId_Type()
)
wwpVoiceGatewaySipLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipLineId.setStatus("current")


class _WwpVoiceGatewaySipPhoneNumber_Type(OctetString):
    """Custom type wwpVoiceGatewaySipPhoneNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpVoiceGatewaySipPhoneNumber_Type.__name__ = "OctetString"
_WwpVoiceGatewaySipPhoneNumber_Object = MibTableColumn
wwpVoiceGatewaySipPhoneNumber = _WwpVoiceGatewaySipPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4, 1, 2),
    _WwpVoiceGatewaySipPhoneNumber_Type()
)
wwpVoiceGatewaySipPhoneNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipPhoneNumber.setStatus("current")


class _WwpVoiceGatewaySipUserName_Type(OctetString):
    """Custom type wwpVoiceGatewaySipUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpVoiceGatewaySipUserName_Type.__name__ = "OctetString"
_WwpVoiceGatewaySipUserName_Object = MibTableColumn
wwpVoiceGatewaySipUserName = _WwpVoiceGatewaySipUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4, 1, 3),
    _WwpVoiceGatewaySipUserName_Type()
)
wwpVoiceGatewaySipUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipUserName.setStatus("current")


class _WwpVoiceGatewaySipUserDisplayName_Type(OctetString):
    """Custom type wwpVoiceGatewaySipUserDisplayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpVoiceGatewaySipUserDisplayName_Type.__name__ = "OctetString"
_WwpVoiceGatewaySipUserDisplayName_Object = MibTableColumn
wwpVoiceGatewaySipUserDisplayName = _WwpVoiceGatewaySipUserDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4, 1, 4),
    _WwpVoiceGatewaySipUserDisplayName_Type()
)
wwpVoiceGatewaySipUserDisplayName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipUserDisplayName.setStatus("current")


class _WwpVoiceGatewaySipUserPassword_Type(OctetString):
    """Custom type wwpVoiceGatewaySipUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpVoiceGatewaySipUserPassword_Type.__name__ = "OctetString"
_WwpVoiceGatewaySipUserPassword_Object = MibTableColumn
wwpVoiceGatewaySipUserPassword = _WwpVoiceGatewaySipUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4, 1, 5),
    _WwpVoiceGatewaySipUserPassword_Type()
)
wwpVoiceGatewaySipUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipUserPassword.setStatus("current")


class _WwpVoiceGatewaySipDialPlan_Type(OctetString):
    """Custom type wwpVoiceGatewaySipDialPlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_WwpVoiceGatewaySipDialPlan_Type.__name__ = "OctetString"
_WwpVoiceGatewaySipDialPlan_Object = MibTableColumn
wwpVoiceGatewaySipDialPlan = _WwpVoiceGatewaySipDialPlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 4, 1, 6),
    _WwpVoiceGatewaySipDialPlan_Type()
)
wwpVoiceGatewaySipDialPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipDialPlan.setStatus("current")
_WwpVoiceGatewaySipPhoneLineTimerTable_Object = MibTable
wwpVoiceGatewaySipPhoneLineTimerTable = _WwpVoiceGatewaySipPhoneLineTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 5)
)
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipPhoneLineTimerTable.setStatus("current")
_WwpVoiceGatewaySipPhoneLineTimerEntry_Object = MibTableRow
wwpVoiceGatewaySipPhoneLineTimerEntry = _WwpVoiceGatewaySipPhoneLineTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 5, 1)
)
wwpVoiceGatewaySipPhoneLineTimerEntry.setIndexNames(
    (0, "WWP-VOICE-GATEWAY-MIB", "wwpVoiceGatewaySipTimerLineId"),
)
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipPhoneLineTimerEntry.setStatus("current")


class _WwpVoiceGatewaySipTimerLineId_Type(Integer32):
    """Custom type wwpVoiceGatewaySipTimerLineId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpVoiceGatewaySipTimerLineId_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipTimerLineId_Object = MibTableColumn
wwpVoiceGatewaySipTimerLineId = _WwpVoiceGatewaySipTimerLineId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 5, 1, 1),
    _WwpVoiceGatewaySipTimerLineId_Type()
)
wwpVoiceGatewaySipTimerLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipTimerLineId.setStatus("current")


class _WwpVoiceGatewaySipDialTimerLong_Type(Integer32):
    """Custom type wwpVoiceGatewaySipDialTimerLong based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WwpVoiceGatewaySipDialTimerLong_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipDialTimerLong_Object = MibTableColumn
wwpVoiceGatewaySipDialTimerLong = _WwpVoiceGatewaySipDialTimerLong_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 5, 1, 2),
    _WwpVoiceGatewaySipDialTimerLong_Type()
)
wwpVoiceGatewaySipDialTimerLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipDialTimerLong.setStatus("current")
_WwpVoiceGatewaySIPServers_ObjectIdentity = ObjectIdentity
wwpVoiceGatewaySIPServers = _WwpVoiceGatewaySIPServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6)
)
_WwpVoiceGatewaySIPProxyServers_ObjectIdentity = ObjectIdentity
wwpVoiceGatewaySIPProxyServers = _WwpVoiceGatewaySIPProxyServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 1)
)
_WwpVoiceGatewaySipProxyAddr_Type = DisplayString
_WwpVoiceGatewaySipProxyAddr_Object = MibScalar
wwpVoiceGatewaySipProxyAddr = _WwpVoiceGatewaySipProxyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 1, 1),
    _WwpVoiceGatewaySipProxyAddr_Type()
)
wwpVoiceGatewaySipProxyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipProxyAddr.setStatus("current")


class _WwpVoiceGatewaySipProxyPort_Type(Integer32):
    """Custom type wwpVoiceGatewaySipProxyPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_WwpVoiceGatewaySipProxyPort_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipProxyPort_Object = MibScalar
wwpVoiceGatewaySipProxyPort = _WwpVoiceGatewaySipProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 1, 2),
    _WwpVoiceGatewaySipProxyPort_Type()
)
wwpVoiceGatewaySipProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipProxyPort.setStatus("current")
_WwpVoiceGatewaySIPRegistrarServers_ObjectIdentity = ObjectIdentity
wwpVoiceGatewaySIPRegistrarServers = _WwpVoiceGatewaySIPRegistrarServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 2)
)
_WwpVoiceGatewaySipRegistrarAddr_Type = DisplayString
_WwpVoiceGatewaySipRegistrarAddr_Object = MibScalar
wwpVoiceGatewaySipRegistrarAddr = _WwpVoiceGatewaySipRegistrarAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 2, 1),
    _WwpVoiceGatewaySipRegistrarAddr_Type()
)
wwpVoiceGatewaySipRegistrarAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipRegistrarAddr.setStatus("current")


class _WwpVoiceGatewaySipRegistrarPort_Type(Integer32):
    """Custom type wwpVoiceGatewaySipRegistrarPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_WwpVoiceGatewaySipRegistrarPort_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipRegistrarPort_Object = MibScalar
wwpVoiceGatewaySipRegistrarPort = _WwpVoiceGatewaySipRegistrarPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 2, 2),
    _WwpVoiceGatewaySipRegistrarPort_Type()
)
wwpVoiceGatewaySipRegistrarPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipRegistrarPort.setStatus("current")
_WwpVoiceGatewaySIPLogServers_ObjectIdentity = ObjectIdentity
wwpVoiceGatewaySIPLogServers = _WwpVoiceGatewaySIPLogServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 3)
)
_WwpVoiceGatewaySipSyslogAddr_Type = DisplayString
_WwpVoiceGatewaySipSyslogAddr_Object = MibScalar
wwpVoiceGatewaySipSyslogAddr = _WwpVoiceGatewaySipSyslogAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 3, 1),
    _WwpVoiceGatewaySipSyslogAddr_Type()
)
wwpVoiceGatewaySipSyslogAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipSyslogAddr.setStatus("current")


class _WwpVoiceGatewaySipSyslogPort_Type(Integer32):
    """Custom type wwpVoiceGatewaySipSyslogPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpVoiceGatewaySipSyslogPort_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipSyslogPort_Object = MibScalar
wwpVoiceGatewaySipSyslogPort = _WwpVoiceGatewaySipSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 3, 2),
    _WwpVoiceGatewaySipSyslogPort_Type()
)
wwpVoiceGatewaySipSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipSyslogPort.setStatus("current")


class _WwpVoiceGatewaySipSyslogLogLevel_Type(Integer32):
    """Custom type wwpVoiceGatewaySipSyslogLogLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WwpVoiceGatewaySipSyslogLogLevel_Type.__name__ = "Integer32"
_WwpVoiceGatewaySipSyslogLogLevel_Object = MibScalar
wwpVoiceGatewaySipSyslogLogLevel = _WwpVoiceGatewaySipSyslogLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 6, 3, 3),
    _WwpVoiceGatewaySipSyslogLogLevel_Type()
)
wwpVoiceGatewaySipSyslogLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySipSyslogLogLevel.setStatus("current")


class _WwpVoiceGatewaySIPPreferredCodec_Type(Integer32):
    """Custom type wwpVoiceGatewaySIPPreferredCodec based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711", 1),
          ("g729", 2))
    )


_WwpVoiceGatewaySIPPreferredCodec_Type.__name__ = "Integer32"
_WwpVoiceGatewaySIPPreferredCodec_Object = MibScalar
wwpVoiceGatewaySIPPreferredCodec = _WwpVoiceGatewaySIPPreferredCodec_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 7),
    _WwpVoiceGatewaySIPPreferredCodec_Type()
)
wwpVoiceGatewaySIPPreferredCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySIPPreferredCodec.setStatus("current")


class _WwpVoiceGatewaySIPDtmfEventHandling_Type(Integer32):
    """Custom type wwpVoiceGatewaySIPDtmfEventHandling based on Integer32"""
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
        *(("audio", 1),
          ("info", 2),
          ("rfc2833", 3))
    )


_WwpVoiceGatewaySIPDtmfEventHandling_Type.__name__ = "Integer32"
_WwpVoiceGatewaySIPDtmfEventHandling_Object = MibScalar
wwpVoiceGatewaySIPDtmfEventHandling = _WwpVoiceGatewaySIPDtmfEventHandling_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 8),
    _WwpVoiceGatewaySIPDtmfEventHandling_Type()
)
wwpVoiceGatewaySIPDtmfEventHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewaySIPDtmfEventHandling.setStatus("current")
_WwpVoiceGatewaySIPCallFeatures_ObjectIdentity = ObjectIdentity
wwpVoiceGatewaySIPCallFeatures = _WwpVoiceGatewaySIPCallFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 9)
)


class _WwpVoiceGatewayHookFlashEnable_Type(TruthValue):
    """Custom type wwpVoiceGatewayHookFlashEnable based on TruthValue"""


_WwpVoiceGatewayHookFlashEnable_Object = MibScalar
wwpVoiceGatewayHookFlashEnable = _WwpVoiceGatewayHookFlashEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 20, 9, 1),
    _WwpVoiceGatewayHookFlashEnable_Type()
)
wwpVoiceGatewayHookFlashEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayHookFlashEnable.setStatus("current")
_WwpVoiceGatewayConfigProtocolType_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigProtocolType = _WwpVoiceGatewayConfigProtocolType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 21)
)


class _WwpVoiceGatewayProtocolType_Type(Integer32):
    """Custom type wwpVoiceGatewayProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgcp", 1),
          ("sip", 2))
    )


_WwpVoiceGatewayProtocolType_Type.__name__ = "Integer32"
_WwpVoiceGatewayProtocolType_Object = MibScalar
wwpVoiceGatewayProtocolType = _WwpVoiceGatewayProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 21, 1),
    _WwpVoiceGatewayProtocolType_Type()
)
wwpVoiceGatewayProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayProtocolType.setStatus("current")
_WwpVoiceGatewayConfigProtocolEnable_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayConfigProtocolEnable = _WwpVoiceGatewayConfigProtocolEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 22)
)


class _WwpVoiceGatewayProtocolEnable_Type(TruthValue):
    """Custom type wwpVoiceGatewayProtocolEnable based on TruthValue"""


_WwpVoiceGatewayProtocolEnable_Object = MibScalar
wwpVoiceGatewayProtocolEnable = _WwpVoiceGatewayProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 1, 1, 22, 1),
    _WwpVoiceGatewayProtocolEnable_Type()
)
wwpVoiceGatewayProtocolEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpVoiceGatewayProtocolEnable.setStatus("current")
_WwpVoiceGatewayMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayMIBNotificationPrefix = _WwpVoiceGatewayMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 2)
)
_WwpVoiceGatewayMIBNotifications_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayMIBNotifications = _WwpVoiceGatewayMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 2, 0)
)
_WwpVoiceGatewayMIBConformance_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayMIBConformance = _WwpVoiceGatewayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 3)
)
_WwpVoiceGatewayMIBCompliances_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayMIBCompliances = _WwpVoiceGatewayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 3, 1)
)
_WwpVoiceGatewayMIBGroups_ObjectIdentity = ObjectIdentity
wwpVoiceGatewayMIBGroups = _WwpVoiceGatewayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 43, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-VOICE-GATEWAY-MIB",
    **{"wwpVoiceGatewayMIB": wwpVoiceGatewayMIB,
       "wwpVoiceGatewayMIBObjects": wwpVoiceGatewayMIBObjects,
       "wwpVoiceGateway": wwpVoiceGateway,
       "wwpVoiceGatewayMGCP": wwpVoiceGatewayMGCP,
       "wwpVoiceGatewayEndPointTable": wwpVoiceGatewayEndPointTable,
       "wwpVoiceGatewayEndPointEntry": wwpVoiceGatewayEndPointEntry,
       "wwpVoiceGatewayEndPointId": wwpVoiceGatewayEndPointId,
       "wwpVoiceGatewayEndpoint": wwpVoiceGatewayEndpoint,
       "wwpVoiceGatewayCallAgentAddr": wwpVoiceGatewayCallAgentAddr,
       "wwpVoiceGatewayCallAgentUDPPort": wwpVoiceGatewayCallAgentUDPPort,
       "wwpVoiceGatewayCallAgentProtocol": wwpVoiceGatewayCallAgentProtocol,
       "wwpVoiceGatewaySupportMessagePiggybacking": wwpVoiceGatewaySupportMessagePiggybacking,
       "wwpVoiceGatewayRsipKeepAliveEnable": wwpVoiceGatewayRsipKeepAliveEnable,
       "wwpVoiceGatewayRsipKeepAliveInterval": wwpVoiceGatewayRsipKeepAliveInterval,
       "wwpVoiceGatewayCountry": wwpVoiceGatewayCountry,
       "wwpVoiceGatewayCountryCodes": wwpVoiceGatewayCountryCodes,
       "wwpVoiceGatewayCodec": wwpVoiceGatewayCodec,
       "wwpVoiceGatewayComplexCodec": wwpVoiceGatewayComplexCodec,
       "wwpVoiceGatewaySilenceSuppression": wwpVoiceGatewaySilenceSuppression,
       "wwpVoiceGatewayEchoCancellation": wwpVoiceGatewayEchoCancellation,
       "wwpVoiceGatewayPacketizationMinPeriod": wwpVoiceGatewayPacketizationMinPeriod,
       "wwpVoiceGatewayPacketizationMaxPeriod": wwpVoiceGatewayPacketizationMaxPeriod,
       "wwpVoiceGatewayAudio": wwpVoiceGatewayAudio,
       "wwpVoiceGatewayPayloadType": wwpVoiceGatewayPayloadType,
       "wwpVoiceGatewaySendEventsViaRFC2833": wwpVoiceGatewaySendEventsViaRFC2833,
       "wwpVoiceGatewayDropVoicePktsDuringEvents": wwpVoiceGatewayDropVoicePktsDuringEvents,
       "wwpVoiceGatewaySquelchInbandDtmfAudio": wwpVoiceGatewaySquelchInbandDtmfAudio,
       "wwpVoiceGatewayStats": wwpVoiceGatewayStats,
       "wwpVoiceGatewayPktsTx": wwpVoiceGatewayPktsTx,
       "wwpVoiceGatewayOctetsTx": wwpVoiceGatewayOctetsTx,
       "wwpVoiceGatewayPktsRx": wwpVoiceGatewayPktsRx,
       "wwpVoiceGatewayOctetsRx": wwpVoiceGatewayOctetsRx,
       "wwpVoiceGatewayPktsLost": wwpVoiceGatewayPktsLost,
       "wwpVoiceGatewayIntervalJitter": wwpVoiceGatewayIntervalJitter,
       "wwpVoiceGatewayLatency": wwpVoiceGatewayLatency,
       "wwpVoiceGatewayResetStatCounters": wwpVoiceGatewayResetStatCounters,
       "wwpVoiceReset": wwpVoiceReset,
       "wwpVoiceGatewayNumResets": wwpVoiceGatewayNumResets,
       "wwpVoiceGatewayReset": wwpVoiceGatewayReset,
       "wwpVoiceSec": wwpVoiceSec,
       "wwpVoiceAccess": wwpVoiceAccess,
       "wwpMgmtAccess": wwpMgmtAccess,
       "wwpVoiceGatewayConfigCallAgent": wwpVoiceGatewayConfigCallAgent,
       "wwpVoiceCallAgentOtaModes": wwpVoiceCallAgentOtaModes,
       "wwpVoiceCallAgentEgressEvent": wwpVoiceCallAgentEgressEvent,
       "wwpVoiceGatewayConfigPots": wwpVoiceGatewayConfigPots,
       "wwpVoiceCallAgentPotsLine": wwpVoiceCallAgentPotsLine,
       "wwpVoiceGatewayConfigFax": wwpVoiceGatewayConfigFax,
       "wwpVoiceAutonomousFaxState": wwpVoiceAutonomousFaxState,
       "wwpVoiceGatewayConfigEndPoint": wwpVoiceGatewayConfigEndPoint,
       "wwpVoiceEndPointName": wwpVoiceEndPointName,
       "wwpVoiceGatewayConfigNotifEntityCache": wwpVoiceGatewayConfigNotifEntityCache,
       "wwpVoiceNotifEntCache": wwpVoiceNotifEntCache,
       "wwpVoiceGatewayConfigJitterBuffer": wwpVoiceGatewayConfigJitterBuffer,
       "wwpVoiceJitterOptionState": wwpVoiceJitterOptionState,
       "wwpVoiceGatewayConfigJitterBufferMinPeriod": wwpVoiceGatewayConfigJitterBufferMinPeriod,
       "wwpVoiceJitterBufferMinPeriod": wwpVoiceJitterBufferMinPeriod,
       "wwpVoiceGatewayConfigJitterBufferMaxPeriod": wwpVoiceGatewayConfigJitterBufferMaxPeriod,
       "wwpVoiceJitterBufferMaxPeriod": wwpVoiceJitterBufferMaxPeriod,
       "wwpVoiceGatewayConfigJitterBufferTargetPeriod": wwpVoiceGatewayConfigJitterBufferTargetPeriod,
       "wwpVoiceJitterBufferTargetPeriod": wwpVoiceJitterBufferTargetPeriod,
       "wwpVoiceGatewayConfigCodecOverride": wwpVoiceGatewayConfigCodecOverride,
       "wwpVoiceGatewayCodecOverride": wwpVoiceGatewayCodecOverride,
       "wwpVoiceGatewayConfigTestServerConnection": wwpVoiceGatewayConfigTestServerConnection,
       "wwpVoiceGatewayTestServerConnection": wwpVoiceGatewayTestServerConnection,
       "wwpVoiceGatewayConfigLastServerResponseTime": wwpVoiceGatewayConfigLastServerResponseTime,
       "wwpVoiceGatewayLastServerResponseTime": wwpVoiceGatewayLastServerResponseTime,
       "wwpVoiceGatewaySIP": wwpVoiceGatewaySIP,
       "wwpVoiceGatewaySipSessionTimeoutPeriod": wwpVoiceGatewaySipSessionTimeoutPeriod,
       "wwpVoiceGatewaySipRegisterTimeoutPeriod": wwpVoiceGatewaySipRegisterTimeoutPeriod,
       "wwpVoiceGatewaySipForceQuotesState": wwpVoiceGatewaySipForceQuotesState,
       "wwpVoiceGatewaySipPhoneLineTable": wwpVoiceGatewaySipPhoneLineTable,
       "wwpVoiceGatewaySipPhoneLineEntry": wwpVoiceGatewaySipPhoneLineEntry,
       "wwpVoiceGatewaySipLineId": wwpVoiceGatewaySipLineId,
       "wwpVoiceGatewaySipPhoneNumber": wwpVoiceGatewaySipPhoneNumber,
       "wwpVoiceGatewaySipUserName": wwpVoiceGatewaySipUserName,
       "wwpVoiceGatewaySipUserDisplayName": wwpVoiceGatewaySipUserDisplayName,
       "wwpVoiceGatewaySipUserPassword": wwpVoiceGatewaySipUserPassword,
       "wwpVoiceGatewaySipDialPlan": wwpVoiceGatewaySipDialPlan,
       "wwpVoiceGatewaySipPhoneLineTimerTable": wwpVoiceGatewaySipPhoneLineTimerTable,
       "wwpVoiceGatewaySipPhoneLineTimerEntry": wwpVoiceGatewaySipPhoneLineTimerEntry,
       "wwpVoiceGatewaySipTimerLineId": wwpVoiceGatewaySipTimerLineId,
       "wwpVoiceGatewaySipDialTimerLong": wwpVoiceGatewaySipDialTimerLong,
       "wwpVoiceGatewaySIPServers": wwpVoiceGatewaySIPServers,
       "wwpVoiceGatewaySIPProxyServers": wwpVoiceGatewaySIPProxyServers,
       "wwpVoiceGatewaySipProxyAddr": wwpVoiceGatewaySipProxyAddr,
       "wwpVoiceGatewaySipProxyPort": wwpVoiceGatewaySipProxyPort,
       "wwpVoiceGatewaySIPRegistrarServers": wwpVoiceGatewaySIPRegistrarServers,
       "wwpVoiceGatewaySipRegistrarAddr": wwpVoiceGatewaySipRegistrarAddr,
       "wwpVoiceGatewaySipRegistrarPort": wwpVoiceGatewaySipRegistrarPort,
       "wwpVoiceGatewaySIPLogServers": wwpVoiceGatewaySIPLogServers,
       "wwpVoiceGatewaySipSyslogAddr": wwpVoiceGatewaySipSyslogAddr,
       "wwpVoiceGatewaySipSyslogPort": wwpVoiceGatewaySipSyslogPort,
       "wwpVoiceGatewaySipSyslogLogLevel": wwpVoiceGatewaySipSyslogLogLevel,
       "wwpVoiceGatewaySIPPreferredCodec": wwpVoiceGatewaySIPPreferredCodec,
       "wwpVoiceGatewaySIPDtmfEventHandling": wwpVoiceGatewaySIPDtmfEventHandling,
       "wwpVoiceGatewaySIPCallFeatures": wwpVoiceGatewaySIPCallFeatures,
       "wwpVoiceGatewayHookFlashEnable": wwpVoiceGatewayHookFlashEnable,
       "wwpVoiceGatewayConfigProtocolType": wwpVoiceGatewayConfigProtocolType,
       "wwpVoiceGatewayProtocolType": wwpVoiceGatewayProtocolType,
       "wwpVoiceGatewayConfigProtocolEnable": wwpVoiceGatewayConfigProtocolEnable,
       "wwpVoiceGatewayProtocolEnable": wwpVoiceGatewayProtocolEnable,
       "wwpVoiceGatewayMIBNotificationPrefix": wwpVoiceGatewayMIBNotificationPrefix,
       "wwpVoiceGatewayMIBNotifications": wwpVoiceGatewayMIBNotifications,
       "wwpVoiceGatewayMIBConformance": wwpVoiceGatewayMIBConformance,
       "wwpVoiceGatewayMIBCompliances": wwpVoiceGatewayMIBCompliances,
       "wwpVoiceGatewayMIBGroups": wwpVoiceGatewayMIBGroups}
)
