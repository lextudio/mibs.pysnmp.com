# SNMP MIB module (ELTEX-FXS72) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-FXS72
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:09 2024
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

(elHardware,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "elHardware")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fxs72 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9)
)
fxs72.setRevisions(
        ("2009-10-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SSwStatusConv(Integer32, TextualConvention):
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
        *(("connected", 1),
          ("disconnected", 2),
          ("undefined", 0))
    )



class VoltageMode(Integer32, TextualConvention):
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
        *(("high", 1),
          ("low", 3),
          ("normal", 2))
    )



class FXSFanState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class BoolValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class DevTypeString(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              33,
              50)
        )
    )
    namedValues = NamedValues(
        *(("fxs72", 16),
          ("tau32m", 50),
          ("tau36", 33),
          ("tau72", 17))
    )



class FxsPortState(Integer32, TextualConvention):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 12),
          ("busy", 7),
          ("calling", 3),
          ("conference3way", 14),
          ("dial", 2),
          ("disabled", 255),
          ("dvo", 10),
          ("fxoHangdown", 16),
          ("fxoHangup", 17),
          ("hangdown", 0),
          ("hangup", 1),
          ("hold", 8),
          ("holdDial", 9),
          ("preCalling", 13),
          ("ringback", 4),
          ("ringing", 5),
          ("talking", 6),
          ("test", 11),
          ("void", 15))
    )



class PortMegacoState(Integer32, TextualConvention):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("absent", 17),
          ("blocked", 13),
          ("busy", 7),
          ("calling", 3),
          ("dial", 2),
          ("disabled", 16),
          ("hangdown", 0),
          ("hangup", 1),
          ("hold", 8),
          ("holdDial", 9),
          ("holdDvo", 10),
          ("noActualData", 255),
          ("notInited", 15),
          ("ready", 14),
          ("ringback", 4),
          ("ringing", 5),
          ("talking", 6),
          ("transfer", 11),
          ("unattended", 12))
    )



class PortMegacoJitter(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dissipatedPower", 3),
          ("leakageCurrent", 1),
          ("ok", 0),
          ("overheating", 2))
    )



class SipConnectState(Integer32, TextualConvention):
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
        *(("failed", 2),
          ("off", 0),
          ("ok", 1))
    )



class FxsDialPlanType(Integer32, TextualConvention):
    status = "current"
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
        *(("h323DirectIP", 3),
          ("h323GateKeeper", 1),
          ("pickupGroup", 6),
          ("sipDirectIP", 4),
          ("sipProxy", 2),
          ("siptDirectIP", 5))
    )



class FxsAON(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aonRus", 1),
          ("dtmf", 2),
          ("fskBell202", 3),
          ("fskV23", 4),
          ("off", 0))
    )



class FxsGroupSerialType(Integer32, TextualConvention):
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
        *(("cyclic", 2),
          ("group", 0),
          ("serial", 1))
    )



class FxoGroupType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fxoAround", 4),
          ("fxoFirstFree", 3))
    )



class FxsGroupBusyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clearOnBusy", 0),
          ("waitFirstFree", 1))
    )



class FxsGroupSerialEnableType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )



class FxsTaxophoneType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kHz12", 3),
          ("kHz16", 2),
          ("off", 0),
          ("polarity", 1))
    )



class FxsDialPlanNatureType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("international", 3),
          ("national", 2),
          ("subscriber", 1),
          ("unknown", 0))
    )



class FxsProcessFlashType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("attendedCT", 1),
          ("localCT", 4),
          ("noDetectFlash", 3),
          ("transmitFlash", 0),
          ("unattendedCT", 2))
    )



class TauDialProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h323", 2),
          ("sip", 1))
    )



class ProxyMode(Integer32, TextualConvention):
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
        *(("homing", 2),
          ("off", 0),
          ("parking", 1))
    )



class OptionsHomeServerTest(Integer32, TextualConvention):
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
        *(("invite", 0),
          ("options", 1),
          ("register", 2))
    )



class AuthenticationType(Integer32, TextualConvention):
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
        *(("global", 1),
          ("off", 0),
          ("userDefined", 2))
    )



class CwRingbackRingbackAtCallwaiting(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ring180Ringing", 0),
          ("ring182Queued", 1))
    )



class RemoteRingback(Integer32, TextualConvention):
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
        *(("dontSendRingbackInRTP", 0),
          ("ringbackWith180Ringing", 1),
          ("ringbackWith183Progress", 2))
    )



class DTMFMIMEType(Integer32, TextualConvention):
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
        *(("applicationDtmf", 1),
          ("applicationDtmfRelay", 0),
          ("audioTelephoneEvent", 2))
    )



class HookFlashMIMEType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("applicationBroadsoft", 2),
          ("applicationHookFlash", 1),
          ("applicationSscc", 3),
          ("asDTMF", 0))
    )



class TypeTransport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcpOnly", 3),
          ("tcpPrefferedOrUdp", 1),
          ("udpOnly", 2),
          ("udpPrefferedOrTcp", 0))
    )



class Type100rel(Integer32, TextualConvention):
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
        *(("off", 2),
          ("required", 1),
          ("supported", 0))
    )



class OutboundType(Integer32, TextualConvention):
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
        *(("off", 0),
          ("on", 1),
          ("withBusyTone", 2))
    )



class FxoDialingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )



class FxsToneParametrs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TauDtmfTransferType(Integer32, TextualConvention):
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
        *(("inband", 0),
          ("info", 2),
          ("rfc2833", 1))
    )



class TauFlashTransferType(Integer32, TextualConvention):
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
        *(("disabled", 0),
          ("info", 2),
          ("rfc2833", 1))
    )



class TauFaxDirectionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("callee", 2),
          ("caller", 1),
          ("none", 3))
    )



class TauFaxTransferType(Integer32, TextualConvention):
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
        *(("g711a", 0),
          ("g711u", 1),
          ("t38", 2))
    )



class TauFaxTransferSlaveType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711a", 0),
          ("g711u", 1),
          ("none", 3),
          ("t38", 2))
    )



class TauModemTransferType(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("g711aNse", 5),
          ("g711aRfc3108", 2),
          ("g711aVbd", 0),
          ("g711uNse", 6),
          ("g711uRfc3108", 3),
          ("g711uVbd", 1),
          ("off", 4))
    )



class TauVoiceModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("fixed", 0))
    )



class TauvoiceDeletionModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hard", 0),
          ("soft", 1))
    )



class TauTrapVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )



class TauMegacoTrapVersion(Integer32, TextualConvention):
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
        *(("inform", 0),
          ("trapV1", 1),
          ("trapV2", 2))
    )



class TauUserViewType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )



class FxoGroupBusyType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clearOnBusy", 0),
          ("waitFirstFree", 1))
    )



class FxsNetworkAutoupdateSourceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("dhcpVlan1", 1),
          ("dhcpVlan2", 2),
          ("dhcpVlan3", 3),
          ("noDhcp", 4))
    )



class SipLogLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("criticalErrors", 1),
          ("everything", 9),
          ("fatalErrors", 0),
          ("mediaProtocol", 7),
          ("nonCriticalErrors", 2),
          ("none", -1),
          ("signalProtocol", 5),
          ("verbose1", 4),
          ("verbose2", 6),
          ("verobse3", 8),
          ("warnings", 3))
    )



class H323LogLevel(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("debugA", 4),
          ("debugB", 5),
          ("debugC", 6),
          ("errors", 1),
          ("info", 3),
          ("none", 0),
          ("warnings", 2))
    )



class VapiLibLogLevel(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("allInfo", 6),
          ("api", 1),
          ("apiPacket", 2),
          ("none", 0),
          ("vapiGtlInfo", 4),
          ("vapiInfo", 3),
          ("vapiUt", 5))
    )



class VapiAppLogLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("debug", 2),
          ("info", 1),
          ("none", 5),
          ("packet", 3),
          ("warnings", 4))
    )



class FxsPortTestStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("completed", 2),
          ("disabled", 255),
          ("idle", 0),
          ("requested", 1))
    )



class FxsPortTestFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("capacitanceNotMeasured", 4),
          ("leakageCurrent", 2),
          ("ok", 0),
          ("overheat", 1),
          ("resistanceNotMeasured", 3),
          ("testFailure", 255),
          ("testingUnavailable", 5),
          ("unknown", -1))
    )



class KeepAliveMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clrf", 3),
          ("notify", 2),
          ("off", 0),
          ("options", 1))
    )



class ConferenceMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )



class GroupRegistrationState(Integer32, TextualConvention):
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
        *(("failed", 2),
          ("off", 0),
          ("ok", 1))
    )



class FirewallProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("icmp", 3),
          ("tcp", 2),
          ("udp", 1))
    )



class TypeOfMessageICMP(Integer32, TextualConvention):
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("addressMaskReply", 36),
          ("addressMaskRequest", 35),
          ("any", 0),
          ("communicationProhibited", 15),
          ("destinationUnreachable", 2),
          ("echoReply", 1),
          ("echoRequest", 24),
          ("fragmentationNeeded", 7),
          ("hostPrecedenceViolation", 16),
          ("hostProhibited", 12),
          ("hostRedirect", 21),
          ("hostUnknown", 10),
          ("hostUnreachable", 4),
          ("ipHeaderBad", 31),
          ("networkProhibited", 11),
          ("networkRedirect", 20),
          ("networkUnknown", 9),
          ("networkUnreachable", 3),
          ("parameterProblem", 30),
          ("portUnreachable", 6),
          ("precedenceCutoff", 17),
          ("protocolUnreachable", 5),
          ("redirect", 19),
          ("requiredOptionMissing", 32),
          ("routerAdvertisement", 25),
          ("routerSolicitation", 26),
          ("sourceQuench", 18),
          ("sourceRouteFailed", 8),
          ("timeExceeded", 27),
          ("timestampReply", 34),
          ("timestampRequest", 33),
          ("tosHostRedirect", 23),
          ("tosHostUnreachable", 14),
          ("tosNetworkRedirect", 22),
          ("tosNetworkUnreachable", 13),
          ("ttlZeroDuringReassembly", 29),
          ("ttlZeroDuringTransit", 28))
    )



class FirewallTarget(Integer32, TextualConvention):
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
        *(("accept", 1),
          ("drop", 0),
          ("reject", 2))
    )



class ReversalPolarityAction(Integer32, TextualConvention):
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
        *(("answer", 2),
          ("ignore", 0),
          ("release", 1))
    )



class CallLimitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("proxyGk", 0))
    )



class PowerMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extendedRange", 1),
          ("normal", 0))
    )



class DRSubscriberProfilesType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class PstnActivityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answerAtPstnReversalPolarityDetection", 2),
          ("off", 0),
          ("pstnAnswerDetection", 3),
          ("releaseAtPstnReversalPolarityDetection", 1))
    )



class IMSMode(Integer32, TextualConvention):
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
        *(("explicit", 2),
          ("implicit", 1),
          ("off", 0))
    )



class AutoupdateProtocolType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("http", 2),
          ("https", 3),
          ("tftp", 0))
    )



class SipProfileChangeoverType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("changeoverOnFailureOfInviteOrRegisterRequest", 0),
          ("changeoverOnFailureOfRegisterRequest", 1))
    )



class DevPowerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )



# MIB Managed Objects in the order of their OIDs



class _FxsDevName_Type(DisplayString):
    """Custom type fxsDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FxsDevName_Type.__name__ = "DisplayString"
_FxsDevName_Object = MibScalar
fxsDevName = _FxsDevName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 1),
    _FxsDevName_Type()
)
fxsDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsDevName.setStatus("current")
_FxsDevType_Type = DevTypeString
_FxsDevType_Object = MibScalar
fxsDevType = _FxsDevType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 2),
    _FxsDevType_Type()
)
fxsDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsDevType.setStatus("current")


class _FxsDevCfgBuild_Type(DisplayString):
    """Custom type fxsDevCfgBuild based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FxsDevCfgBuild_Type.__name__ = "DisplayString"
_FxsDevCfgBuild_Object = MibScalar
fxsDevCfgBuild = _FxsDevCfgBuild_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 3),
    _FxsDevCfgBuild_Type()
)
fxsDevCfgBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsDevCfgBuild.setStatus("current")
_FxsFreeSpace_Type = DisplayString
_FxsFreeSpace_Object = MibScalar
fxsFreeSpace = _FxsFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 4),
    _FxsFreeSpace_Type()
)
fxsFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsFreeSpace.setStatus("current")
_FxsFreeRam_Type = DisplayString
_FxsFreeRam_Object = MibScalar
fxsFreeRam = _FxsFreeRam_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 5),
    _FxsFreeRam_Type()
)
fxsFreeRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsFreeRam.setStatus("current")
_FxsSSwStatus_Type = SSwStatusConv
_FxsSSwStatus_Object = MibScalar
fxsSSwStatus = _FxsSSwStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 6),
    _FxsSSwStatus_Type()
)
fxsSSwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsSSwStatus.setStatus("current")
_FxsSSwStatusTime_Type = TimeTicks
_FxsSSwStatusTime_Object = MibScalar
fxsSSwStatusTime = _FxsSSwStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 7),
    _FxsSSwStatusTime_Type()
)
fxsSSwStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsSSwStatusTime.setStatus("current")
_FxsCpuUsage_Type = DisplayString
_FxsCpuUsage_Object = MibScalar
fxsCpuUsage = _FxsCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 8),
    _FxsCpuUsage_Type()
)
fxsCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsCpuUsage.setStatus("current")
_FxsMonitoring_ObjectIdentity = ObjectIdentity
fxsMonitoring = _FxsMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10)
)
_FxsMonitoringVMode_Type = VoltageMode
_FxsMonitoringVMode_Object = MibScalar
fxsMonitoringVMode = _FxsMonitoringVMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 1),
    _FxsMonitoringVMode_Type()
)
fxsMonitoringVMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringVMode.setStatus("current")
_FxsMonitoringVBat_Type = Integer32
_FxsMonitoringVBat_Object = MibScalar
fxsMonitoringVBat = _FxsMonitoringVBat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 2),
    _FxsMonitoringVBat_Type()
)
fxsMonitoringVBat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringVBat.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringVBat.setUnits("V")
_FxsMonitoringVRing1_Type = Integer32
_FxsMonitoringVRing1_Object = MibScalar
fxsMonitoringVRing1 = _FxsMonitoringVRing1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 3),
    _FxsMonitoringVRing1_Type()
)
fxsMonitoringVRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringVRing1.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringVRing1.setUnits("V")
_FxsMonitoringVRing2_Type = Integer32
_FxsMonitoringVRing2_Object = MibScalar
fxsMonitoringVRing2 = _FxsMonitoringVRing2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 4),
    _FxsMonitoringVRing2_Type()
)
fxsMonitoringVRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringVRing2.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringVRing2.setUnits("V")
_FxsMonitoringTemp1_Type = Integer32
_FxsMonitoringTemp1_Object = MibScalar
fxsMonitoringTemp1 = _FxsMonitoringTemp1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 5),
    _FxsMonitoringTemp1_Type()
)
fxsMonitoringTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringTemp1.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringTemp1.setUnits("ÃÂ°C")
_FxsMonitoringTemp2_Type = Integer32
_FxsMonitoringTemp2_Object = MibScalar
fxsMonitoringTemp2 = _FxsMonitoringTemp2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 6),
    _FxsMonitoringTemp2_Type()
)
fxsMonitoringTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringTemp2.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringTemp2.setUnits("ÃÂ°C")
_FxsMonitoringTemp3_Type = Integer32
_FxsMonitoringTemp3_Object = MibScalar
fxsMonitoringTemp3 = _FxsMonitoringTemp3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 7),
    _FxsMonitoringTemp3_Type()
)
fxsMonitoringTemp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringTemp3.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringTemp3.setUnits("ÃÂ°C")
_FxsMonitoringTemp4_Type = Integer32
_FxsMonitoringTemp4_Object = MibScalar
fxsMonitoringTemp4 = _FxsMonitoringTemp4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 8),
    _FxsMonitoringTemp4_Type()
)
fxsMonitoringTemp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringTemp4.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringTemp4.setUnits("ÃÂ°C")
_FxsMonitoringFanState_Type = FXSFanState
_FxsMonitoringFanState_Object = MibScalar
fxsMonitoringFanState = _FxsMonitoringFanState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 9),
    _FxsMonitoringFanState_Type()
)
fxsMonitoringFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringFanState.setStatus("current")
_FxsMonitoringFan1Rotate_Type = BoolValue
_FxsMonitoringFan1Rotate_Object = MibScalar
fxsMonitoringFan1Rotate = _FxsMonitoringFan1Rotate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 10),
    _FxsMonitoringFan1Rotate_Type()
)
fxsMonitoringFan1Rotate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringFan1Rotate.setStatus("current")
_FxsMonitoringFan2Rotate_Type = BoolValue
_FxsMonitoringFan2Rotate_Object = MibScalar
fxsMonitoringFan2Rotate = _FxsMonitoringFan2Rotate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 11),
    _FxsMonitoringFan2Rotate_Type()
)
fxsMonitoringFan2Rotate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringFan2Rotate.setStatus("current")
_FxsMonitoringSubCooling_Type = Integer32
_FxsMonitoringSubCooling_Object = MibScalar
fxsMonitoringSubCooling = _FxsMonitoringSubCooling_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 12),
    _FxsMonitoringSubCooling_Type()
)
fxsMonitoringSubCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringSubCooling.setStatus("current")
_FxsMonitoringVinput_Type = Integer32
_FxsMonitoringVinput_Object = MibScalar
fxsMonitoringVinput = _FxsMonitoringVinput_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 13),
    _FxsMonitoringVinput_Type()
)
fxsMonitoringVinput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringVinput.setStatus("current")
if mibBuilder.loadTexts:
    fxsMonitoringVinput.setUnits("V")
_FxsMonitoringDevicePower_Type = DevPowerType
_FxsMonitoringDevicePower_Object = MibScalar
fxsMonitoringDevicePower = _FxsMonitoringDevicePower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 10, 14),
    _FxsMonitoringDevicePower_Type()
)
fxsMonitoringDevicePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsMonitoringDevicePower.setStatus("current")
_FxsPortsMIBBoundary_Type = Integer32
_FxsPortsMIBBoundary_Object = MibScalar
fxsPortsMIBBoundary = _FxsPortsMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 11),
    _FxsPortsMIBBoundary_Type()
)
fxsPortsMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortsMIBBoundary.setStatus("current")
_FxsPorts_ObjectIdentity = ObjectIdentity
fxsPorts = _FxsPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12)
)
_FxsPortsMonitoringTable_Object = MibTable
fxsPortsMonitoringTable = _FxsPortsMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1)
)
if mibBuilder.loadTexts:
    fxsPortsMonitoringTable.setStatus("current")
_FxsPortsMonitoringEntry_Object = MibTableRow
fxsPortsMonitoringEntry = _FxsPortsMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1)
)
fxsPortsMonitoringEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxsPortNumber"),
)
if mibBuilder.loadTexts:
    fxsPortsMonitoringEntry.setStatus("current")


class _FxsPortNumber_Type(Integer32):
    """Custom type fxsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_FxsPortNumber_Type.__name__ = "Integer32"
_FxsPortNumber_Object = MibTableColumn
fxsPortNumber = _FxsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 1),
    _FxsPortNumber_Type()
)
fxsPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxsPortNumber.setStatus("current")
_FxsPortPhoneNumber_Type = DisplayString
_FxsPortPhoneNumber_Object = MibTableColumn
fxsPortPhoneNumber = _FxsPortPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 2),
    _FxsPortPhoneNumber_Type()
)
fxsPortPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortPhoneNumber.setStatus("current")
_FxsPortState_Type = FxsPortState
_FxsPortState_Object = MibTableColumn
fxsPortState = _FxsPortState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 3),
    _FxsPortState_Type()
)
fxsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortState.setStatus("current")
_FxsPortUserName_Type = DisplayString
_FxsPortUserName_Object = MibTableColumn
fxsPortUserName = _FxsPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 4),
    _FxsPortUserName_Type()
)
fxsPortUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortUserName.setStatus("current")
_FxsPortTalkingNum_Type = DisplayString
_FxsPortTalkingNum_Object = MibTableColumn
fxsPortTalkingNum = _FxsPortTalkingNum_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 5),
    _FxsPortTalkingNum_Type()
)
fxsPortTalkingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortTalkingNum.setStatus("current")
_FxsPortTalkingStartTime_Type = DisplayString
_FxsPortTalkingStartTime_Object = MibTableColumn
fxsPortTalkingStartTime = _FxsPortTalkingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 6),
    _FxsPortTalkingStartTime_Type()
)
fxsPortTalkingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortTalkingStartTime.setStatus("current")
_FxsPortSipConnected_Type = DisplayString
_FxsPortSipConnected_Object = MibTableColumn
fxsPortSipConnected = _FxsPortSipConnected_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 7),
    _FxsPortSipConnected_Type()
)
fxsPortSipConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortSipConnected.setStatus("current")
_FxsPortH323Connected_Type = DisplayString
_FxsPortH323Connected_Object = MibTableColumn
fxsPortH323Connected = _FxsPortH323Connected_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 8),
    _FxsPortH323Connected_Type()
)
fxsPortH323Connected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortH323Connected.setStatus("current")
_FxsPortSipConnecteNext_Type = DisplayString
_FxsPortSipConnecteNext_Object = MibTableColumn
fxsPortSipConnecteNext = _FxsPortSipConnecteNext_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 9),
    _FxsPortSipConnecteNext_Type()
)
fxsPortSipConnecteNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortSipConnecteNext.setStatus("current")
_FxsPortSipConnecteState_Type = SipConnectState
_FxsPortSipConnecteState_Object = MibTableColumn
fxsPortSipConnecteState = _FxsPortSipConnecteState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 10),
    _FxsPortSipConnecteState_Type()
)
fxsPortSipConnecteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortSipConnecteState.setStatus("current")
_FxsPortSipConnectHost_Type = DisplayString
_FxsPortSipConnectHost_Object = MibTableColumn
fxsPortSipConnectHost = _FxsPortSipConnectHost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 1, 1, 11),
    _FxsPortSipConnectHost_Type()
)
fxsPortSipConnectHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortSipConnectHost.setStatus("current")
_FxsPortsConfigTable_Object = MibTable
fxsPortsConfigTable = _FxsPortsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2)
)
if mibBuilder.loadTexts:
    fxsPortsConfigTable.setStatus("current")
_FxsPortsConfigEntry_Object = MibTableRow
fxsPortsConfigEntry = _FxsPortsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1)
)
fxsPortsConfigEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxsPortNumber"),
)
if mibBuilder.loadTexts:
    fxsPortsConfigEntry.setStatus("current")
_FxsPortConfigPhone_Type = DisplayString
_FxsPortConfigPhone_Object = MibTableColumn
fxsPortConfigPhone = _FxsPortConfigPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 1),
    _FxsPortConfigPhone_Type()
)
fxsPortConfigPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPhone.setStatus("current")
_FxsPortConfigUserName_Type = DisplayString
_FxsPortConfigUserName_Object = MibTableColumn
fxsPortConfigUserName = _FxsPortConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 2),
    _FxsPortConfigUserName_Type()
)
fxsPortConfigUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigUserName.setStatus("current")
_FxsPortConfigAuthName_Type = DisplayString
_FxsPortConfigAuthName_Object = MibTableColumn
fxsPortConfigAuthName = _FxsPortConfigAuthName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 3),
    _FxsPortConfigAuthName_Type()
)
fxsPortConfigAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigAuthName.setStatus("current")
_FxsPortConfigAuthPass_Type = DisplayString
_FxsPortConfigAuthPass_Object = MibTableColumn
fxsPortConfigAuthPass = _FxsPortConfigAuthPass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 4),
    _FxsPortConfigAuthPass_Type()
)
fxsPortConfigAuthPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigAuthPass.setStatus("current")
_FxsPortConfigCustom_Type = TruthValue
_FxsPortConfigCustom_Object = MibTableColumn
fxsPortConfigCustom = _FxsPortConfigCustom_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 5),
    _FxsPortConfigCustom_Type()
)
fxsPortConfigCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCustom.setStatus("current")
_FxsPortConfigPlaymoh_Type = TruthValue
_FxsPortConfigPlaymoh_Object = MibTableColumn
fxsPortConfigPlaymoh = _FxsPortConfigPlaymoh_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 6),
    _FxsPortConfigPlaymoh_Type()
)
fxsPortConfigPlaymoh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPlaymoh.setStatus("current")
_FxsPortConfigAON_Type = FxsAON
_FxsPortConfigAON_Object = MibTableColumn
fxsPortConfigAON = _FxsPortConfigAON_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 7),
    _FxsPortConfigAON_Type()
)
fxsPortConfigAON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigAON.setStatus("current")
_FxsPortConfigAONHideDate_Type = TruthValue
_FxsPortConfigAONHideDate_Object = MibTableColumn
fxsPortConfigAONHideDate = _FxsPortConfigAONHideDate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 8),
    _FxsPortConfigAONHideDate_Type()
)
fxsPortConfigAONHideDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigAONHideDate.setStatus("current")
_FxsPortConfigAONHideName_Type = TruthValue
_FxsPortConfigAONHideName_Object = MibTableColumn
fxsPortConfigAONHideName = _FxsPortConfigAONHideName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 9),
    _FxsPortConfigAONHideName_Type()
)
fxsPortConfigAONHideName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigAONHideName.setStatus("current")
_FxsPortConfigTaxophone_Type = FxsTaxophoneType
_FxsPortConfigTaxophone_Object = MibTableColumn
fxsPortConfigTaxophone = _FxsPortConfigTaxophone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 10),
    _FxsPortConfigTaxophone_Type()
)
fxsPortConfigTaxophone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigTaxophone.setStatus("current")
_FxsPortConfigMinFlashtime_Type = Integer32
_FxsPortConfigMinFlashtime_Object = MibTableColumn
fxsPortConfigMinFlashtime = _FxsPortConfigMinFlashtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 11),
    _FxsPortConfigMinFlashtime_Type()
)
fxsPortConfigMinFlashtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigMinFlashtime.setStatus("current")
_FxsPortConfigMaxFlashtime_Type = Integer32
_FxsPortConfigMaxFlashtime_Object = MibTableColumn
fxsPortConfigMaxFlashtime = _FxsPortConfigMaxFlashtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 12),
    _FxsPortConfigMaxFlashtime_Type()
)
fxsPortConfigMaxFlashtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigMaxFlashtime.setStatus("current")
_FxsPortConfigGainr_Type = Integer32
_FxsPortConfigGainr_Object = MibTableColumn
fxsPortConfigGainr = _FxsPortConfigGainr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 13),
    _FxsPortConfigGainr_Type()
)
fxsPortConfigGainr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigGainr.setStatus("current")
_FxsPortConfigGaint_Type = Integer32
_FxsPortConfigGaint_Object = MibTableColumn
fxsPortConfigGaint = _FxsPortConfigGaint_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 14),
    _FxsPortConfigGaint_Type()
)
fxsPortConfigGaint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigGaint.setStatus("current")
_FxsPortConfigCategory_Type = Integer32
_FxsPortConfigCategory_Object = MibTableColumn
fxsPortConfigCategory = _FxsPortConfigCategory_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 15),
    _FxsPortConfigCategory_Type()
)
fxsPortConfigCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCategory.setStatus("current")
_FxsPortConfigCallTransfer_Type = FxsProcessFlashType
_FxsPortConfigCallTransfer_Object = MibTableColumn
fxsPortConfigCallTransfer = _FxsPortConfigCallTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 16),
    _FxsPortConfigCallTransfer_Type()
)
fxsPortConfigCallTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCallTransfer.setStatus("current")
_FxsPortConfigCallWaiting_Type = TruthValue
_FxsPortConfigCallWaiting_Object = MibTableColumn
fxsPortConfigCallWaiting = _FxsPortConfigCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 17),
    _FxsPortConfigCallWaiting_Type()
)
fxsPortConfigCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCallWaiting.setStatus("current")
_FxsPortConfigHotLine_Type = TruthValue
_FxsPortConfigHotLine_Object = MibTableColumn
fxsPortConfigHotLine = _FxsPortConfigHotLine_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 18),
    _FxsPortConfigHotLine_Type()
)
fxsPortConfigHotLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigHotLine.setStatus("current")
_FxsPortConfigHotNumber_Type = DisplayString
_FxsPortConfigHotNumber_Object = MibTableColumn
fxsPortConfigHotNumber = _FxsPortConfigHotNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 19),
    _FxsPortConfigHotNumber_Type()
)
fxsPortConfigHotNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigHotNumber.setStatus("current")
_FxsPortConfigHotTimeout_Type = Integer32
_FxsPortConfigHotTimeout_Object = MibTableColumn
fxsPortConfigHotTimeout = _FxsPortConfigHotTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 20),
    _FxsPortConfigHotTimeout_Type()
)
fxsPortConfigHotTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigHotTimeout.setStatus("current")
_FxsPortConfigDisabled_Type = TruthValue
_FxsPortConfigDisabled_Object = MibTableColumn
fxsPortConfigDisabled = _FxsPortConfigDisabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 21),
    _FxsPortConfigDisabled_Type()
)
fxsPortConfigDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDisabled.setStatus("current")
_FxsPortConfigCtBusy_Type = TruthValue
_FxsPortConfigCtBusy_Object = MibTableColumn
fxsPortConfigCtBusy = _FxsPortConfigCtBusy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 22),
    _FxsPortConfigCtBusy_Type()
)
fxsPortConfigCtBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCtBusy.setStatus("current")
_FxsPortConfigCtUnconditional_Type = TruthValue
_FxsPortConfigCtUnconditional_Object = MibTableColumn
fxsPortConfigCtUnconditional = _FxsPortConfigCtUnconditional_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 23),
    _FxsPortConfigCtUnconditional_Type()
)
fxsPortConfigCtUnconditional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCtUnconditional.setStatus("current")
_FxsPortConfigCtNoanswer_Type = TruthValue
_FxsPortConfigCtNoanswer_Object = MibTableColumn
fxsPortConfigCtNoanswer = _FxsPortConfigCtNoanswer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 24),
    _FxsPortConfigCtNoanswer_Type()
)
fxsPortConfigCtNoanswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCtNoanswer.setStatus("current")
_FxsPortConfigCtNumber_Type = DisplayString
_FxsPortConfigCtNumber_Object = MibTableColumn
fxsPortConfigCtNumber = _FxsPortConfigCtNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 25),
    _FxsPortConfigCtNumber_Type()
)
fxsPortConfigCtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCtNumber.setStatus("obsolete")
_FxsPortConfigCtTimeout_Type = Integer32
_FxsPortConfigCtTimeout_Object = MibTableColumn
fxsPortConfigCtTimeout = _FxsPortConfigCtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 26),
    _FxsPortConfigCtTimeout_Type()
)
fxsPortConfigCtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCtTimeout.setStatus("current")
_FxsPortConfigClir_Type = TruthValue
_FxsPortConfigClir_Object = MibTableColumn
fxsPortConfigClir = _FxsPortConfigClir_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 27),
    _FxsPortConfigClir_Type()
)
fxsPortConfigClir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigClir.setStatus("current")
_FxsPortConfigStopDial_Type = TruthValue
_FxsPortConfigStopDial_Object = MibTableColumn
fxsPortConfigStopDial = _FxsPortConfigStopDial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 28),
    _FxsPortConfigStopDial_Type()
)
fxsPortConfigStopDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigStopDial.setStatus("current")
_FxsPortConfigAltNumber_Type = DisplayString
_FxsPortConfigAltNumber_Object = MibTableColumn
fxsPortConfigAltNumber = _FxsPortConfigAltNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 29),
    _FxsPortConfigAltNumber_Type()
)
fxsPortConfigAltNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigAltNumber.setStatus("current")
_FxsPortConfigUseAltNumber_Type = TruthValue
_FxsPortConfigUseAltNumber_Object = MibTableColumn
fxsPortConfigUseAltNumber = _FxsPortConfigUseAltNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 30),
    _FxsPortConfigUseAltNumber_Type()
)
fxsPortConfigUseAltNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigUseAltNumber.setStatus("current")
_FxsPortConfigPickUp_Type = DisplayString
_FxsPortConfigPickUp_Object = MibTableColumn
fxsPortConfigPickUp = _FxsPortConfigPickUp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 31),
    _FxsPortConfigPickUp_Type()
)
fxsPortConfigPickUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPickUp.setStatus("current")
_FxsPortConfigSipPort_Type = Integer32
_FxsPortConfigSipPort_Object = MibTableColumn
fxsPortConfigSipPort = _FxsPortConfigSipPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 32),
    _FxsPortConfigSipPort_Type()
)
fxsPortConfigSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigSipPort.setStatus("current")
_FxsPortConfigCfgPriOverCw_Type = TruthValue
_FxsPortConfigCfgPriOverCw_Object = MibTableColumn
fxsPortConfigCfgPriOverCw = _FxsPortConfigCfgPriOverCw_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 33),
    _FxsPortConfigCfgPriOverCw_Type()
)
fxsPortConfigCfgPriOverCw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCfgPriOverCw.setStatus("current")
_FxsPortConfigRowStatus_Type = RowStatus
_FxsPortConfigRowStatus_Object = MibTableColumn
fxsPortConfigRowStatus = _FxsPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 34),
    _FxsPortConfigRowStatus_Type()
)
fxsPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsPortConfigRowStatus.setStatus("current")
_FxsPortConfigDvoCwEn_Type = TruthValue
_FxsPortConfigDvoCwEn_Object = MibTableColumn
fxsPortConfigDvoCwEn = _FxsPortConfigDvoCwEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 35),
    _FxsPortConfigDvoCwEn_Type()
)
fxsPortConfigDvoCwEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoCwEn.setStatus("current")
_FxsPortConfigDvoCtAttendedEn_Type = TruthValue
_FxsPortConfigDvoCtAttendedEn_Object = MibTableColumn
fxsPortConfigDvoCtAttendedEn = _FxsPortConfigDvoCtAttendedEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 36),
    _FxsPortConfigDvoCtAttendedEn_Type()
)
fxsPortConfigDvoCtAttendedEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoCtAttendedEn.setStatus("current")
_FxsPortConfigDvoCtUnattendedEn_Type = TruthValue
_FxsPortConfigDvoCtUnattendedEn_Object = MibTableColumn
fxsPortConfigDvoCtUnattendedEn = _FxsPortConfigDvoCtUnattendedEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 37),
    _FxsPortConfigDvoCtUnattendedEn_Type()
)
fxsPortConfigDvoCtUnattendedEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoCtUnattendedEn.setStatus("current")
_FxsPortConfigDvoUnconditionalEn_Type = TruthValue
_FxsPortConfigDvoUnconditionalEn_Object = MibTableColumn
fxsPortConfigDvoUnconditionalEn = _FxsPortConfigDvoUnconditionalEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 38),
    _FxsPortConfigDvoUnconditionalEn_Type()
)
fxsPortConfigDvoUnconditionalEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoUnconditionalEn.setStatus("current")
_FxsPortConfigDvoCfBusyEn_Type = TruthValue
_FxsPortConfigDvoCfBusyEn_Object = MibTableColumn
fxsPortConfigDvoCfBusyEn = _FxsPortConfigDvoCfBusyEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 39),
    _FxsPortConfigDvoCfBusyEn_Type()
)
fxsPortConfigDvoCfBusyEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoCfBusyEn.setStatus("current")
_FxsPortConfigDvoCfAnswerEn_Type = TruthValue
_FxsPortConfigDvoCfAnswerEn_Object = MibTableColumn
fxsPortConfigDvoCfAnswerEn = _FxsPortConfigDvoCfAnswerEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 40),
    _FxsPortConfigDvoCfAnswerEn_Type()
)
fxsPortConfigDvoCfAnswerEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoCfAnswerEn.setStatus("current")
_FxsPortConfigDvoCfServiceEn_Type = TruthValue
_FxsPortConfigDvoCfServiceEn_Object = MibTableColumn
fxsPortConfigDvoCfServiceEn = _FxsPortConfigDvoCfServiceEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 41),
    _FxsPortConfigDvoCfServiceEn_Type()
)
fxsPortConfigDvoCfServiceEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoCfServiceEn.setStatus("current")
_FxsPortConfigDvoDoDisturbEn_Type = TruthValue
_FxsPortConfigDvoDoDisturbEn_Object = MibTableColumn
fxsPortConfigDvoDoDisturbEn = _FxsPortConfigDvoDoDisturbEn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 42),
    _FxsPortConfigDvoDoDisturbEn_Type()
)
fxsPortConfigDvoDoDisturbEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDvoDoDisturbEn.setStatus("current")
_FxsPortConfigCtOutofservice_Type = TruthValue
_FxsPortConfigCtOutofservice_Object = MibTableColumn
fxsPortConfigCtOutofservice = _FxsPortConfigCtOutofservice_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 43),
    _FxsPortConfigCtOutofservice_Type()
)
fxsPortConfigCtOutofservice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCtOutofservice.setStatus("current")
_FxsPortConfigCfuNumber_Type = DisplayString
_FxsPortConfigCfuNumber_Object = MibTableColumn
fxsPortConfigCfuNumber = _FxsPortConfigCfuNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 44),
    _FxsPortConfigCfuNumber_Type()
)
fxsPortConfigCfuNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCfuNumber.setStatus("current")
_FxsPortConfigCfbNumber_Type = DisplayString
_FxsPortConfigCfbNumber_Object = MibTableColumn
fxsPortConfigCfbNumber = _FxsPortConfigCfbNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 45),
    _FxsPortConfigCfbNumber_Type()
)
fxsPortConfigCfbNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCfbNumber.setStatus("current")
_FxsPortConfigCfnrNumber_Type = DisplayString
_FxsPortConfigCfnrNumber_Object = MibTableColumn
fxsPortConfigCfnrNumber = _FxsPortConfigCfnrNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 46),
    _FxsPortConfigCfnrNumber_Type()
)
fxsPortConfigCfnrNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCfnrNumber.setStatus("current")
_FxsPortConfigCfoosNumber_Type = DisplayString
_FxsPortConfigCfoosNumber_Object = MibTableColumn
fxsPortConfigCfoosNumber = _FxsPortConfigCfoosNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 47),
    _FxsPortConfigCfoosNumber_Type()
)
fxsPortConfigCfoosNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCfoosNumber.setStatus("current")
_FxsPortConfigDnd_Type = TruthValue
_FxsPortConfigDnd_Object = MibTableColumn
fxsPortConfigDnd = _FxsPortConfigDnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 48),
    _FxsPortConfigDnd_Type()
)
fxsPortConfigDnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDnd.setStatus("current")
_FxsPortConfigFxoFlashTime_Type = Integer32
_FxsPortConfigFxoFlashTime_Object = MibTableColumn
fxsPortConfigFxoFlashTime = _FxsPortConfigFxoFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 49),
    _FxsPortConfigFxoFlashTime_Type()
)
fxsPortConfigFxoFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigFxoFlashTime.setStatus("current")
_FxsPortConfigFxoDelTdm_Type = Integer32
_FxsPortConfigFxoDelTdm_Object = MibTableColumn
fxsPortConfigFxoDelTdm = _FxsPortConfigFxoDelTdm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 50),
    _FxsPortConfigFxoDelTdm_Type()
)
fxsPortConfigFxoDelTdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigFxoDelTdm.setStatus("current")
_FxsPortConfigFxoRingtdm_Type = Integer32
_FxsPortConfigFxoRingtdm_Object = MibTableColumn
fxsPortConfigFxoRingtdm = _FxsPortConfigFxoRingtdm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 51),
    _FxsPortConfigFxoRingtdm_Type()
)
fxsPortConfigFxoRingtdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigFxoRingtdm.setStatus("current")
_FxsPortConfigPstnNumberprefix_Type = DisplayString
_FxsPortConfigPstnNumberprefix_Object = MibTableColumn
fxsPortConfigPstnNumberprefix = _FxsPortConfigPstnNumberprefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 52),
    _FxsPortConfigPstnNumberprefix_Type()
)
fxsPortConfigPstnNumberprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPstnNumberprefix.setStatus("current")
_FxsPortConfigPstnNameprefix_Type = DisplayString
_FxsPortConfigPstnNameprefix_Object = MibTableColumn
fxsPortConfigPstnNameprefix = _FxsPortConfigPstnNameprefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 53),
    _FxsPortConfigPstnNameprefix_Type()
)
fxsPortConfigPstnNameprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPstnNameprefix.setStatus("current")
_FxsPortConfigUsePstnCid_Type = TruthValue
_FxsPortConfigUsePstnCid_Object = MibTableColumn
fxsPortConfigUsePstnCid = _FxsPortConfigUsePstnCid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 54),
    _FxsPortConfigUsePstnCid_Type()
)
fxsPortConfigUsePstnCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigUsePstnCid.setStatus("current")
_FxsPortConfigtdmhotline_Type = TruthValue
_FxsPortConfigtdmhotline_Object = MibTableColumn
fxsPortConfigtdmhotline = _FxsPortConfigtdmhotline_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 55),
    _FxsPortConfigtdmhotline_Type()
)
fxsPortConfigtdmhotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigtdmhotline.setStatus("current")
_FxsPortConfigtdmhottimeout_Type = Integer32
_FxsPortConfigtdmhottimeout_Object = MibTableColumn
fxsPortConfigtdmhottimeout = _FxsPortConfigtdmhottimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 56),
    _FxsPortConfigtdmhottimeout_Type()
)
fxsPortConfigtdmhottimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigtdmhottimeout.setStatus("current")
_FxsPortConfigtdmhotnumber_Type = DisplayString
_FxsPortConfigtdmhotnumber_Object = MibTableColumn
fxsPortConfigtdmhotnumber = _FxsPortConfigtdmhotnumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 57),
    _FxsPortConfigtdmhotnumber_Type()
)
fxsPortConfigtdmhotnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigtdmhotnumber.setStatus("current")
_FxsPortConfigEnableCpc_Type = TruthValue
_FxsPortConfigEnableCpc_Object = MibTableColumn
fxsPortConfigEnableCpc = _FxsPortConfigEnableCpc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 58),
    _FxsPortConfigEnableCpc_Type()
)
fxsPortConfigEnableCpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigEnableCpc.setStatus("current")
_FxsPortConfigCpcTime_Type = Integer32
_FxsPortConfigCpcTime_Object = MibTableColumn
fxsPortConfigCpcTime = _FxsPortConfigCpcTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 59),
    _FxsPortConfigCpcTime_Type()
)
fxsPortConfigCpcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCpcTime.setStatus("current")
_FxsPortConfigDontDetectDT_Type = TruthValue
_FxsPortConfigDontDetectDT_Object = MibTableColumn
fxsPortConfigDontDetectDT = _FxsPortConfigDontDetectDT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 60),
    _FxsPortConfigDontDetectDT_Type()
)
fxsPortConfigDontDetectDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDontDetectDT.setStatus("current")
_FxsPortConfigDelayDialingTimeout_Type = Integer32
_FxsPortConfigDelayDialingTimeout_Object = MibTableColumn
fxsPortConfigDelayDialingTimeout = _FxsPortConfigDelayDialingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 61),
    _FxsPortConfigDelayDialingTimeout_Type()
)
fxsPortConfigDelayDialingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDelayDialingTimeout.setStatus("current")
_FxsPortType_Type = DisplayString
_FxsPortType_Object = MibTableColumn
fxsPortType = _FxsPortType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 62),
    _FxsPortType_Type()
)
fxsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsPortType.setStatus("current")
_FxsPortConfigDialing_Type = FxoDialingType
_FxsPortConfigDialing_Object = MibTableColumn
fxsPortConfigDialing = _FxsPortConfigDialing_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 63),
    _FxsPortConfigDialing_Type()
)
fxsPortConfigDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDialing.setStatus("current")
_FxsPortConfigTransmitNumber_Type = TruthValue
_FxsPortConfigTransmitNumber_Object = MibTableColumn
fxsPortConfigTransmitNumber = _FxsPortConfigTransmitNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 64),
    _FxsPortConfigTransmitNumber_Type()
)
fxsPortConfigTransmitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigTransmitNumber.setStatus("current")
_FxsPortConfigDontTransmitPrefix_Type = TruthValue
_FxsPortConfigDontTransmitPrefix_Object = MibTableColumn
fxsPortConfigDontTransmitPrefix = _FxsPortConfigDontTransmitPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 65),
    _FxsPortConfigDontTransmitPrefix_Type()
)
fxsPortConfigDontTransmitPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDontTransmitPrefix.setStatus("current")
_FxsPortConfigPortProfileID_Type = Integer32
_FxsPortConfigPortProfileID_Object = MibTableColumn
fxsPortConfigPortProfileID = _FxsPortConfigPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 66),
    _FxsPortConfigPortProfileID_Type()
)
fxsPortConfigPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPortProfileID.setStatus("current")
_FxsPortConfigSipProfileID_Type = Integer32
_FxsPortConfigSipProfileID_Object = MibTableColumn
fxsPortConfigSipProfileID = _FxsPortConfigSipProfileID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 67),
    _FxsPortConfigSipProfileID_Type()
)
fxsPortConfigSipProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigSipProfileID.setStatus("current")
_FxsPortConfigDialToneDetectionParameters_Type = FxsToneParametrs
_FxsPortConfigDialToneDetectionParameters_Object = MibTableColumn
fxsPortConfigDialToneDetectionParameters = _FxsPortConfigDialToneDetectionParameters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 68),
    _FxsPortConfigDialToneDetectionParameters_Type()
)
fxsPortConfigDialToneDetectionParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDialToneDetectionParameters.setStatus("current")
_FxsPortConfigRingBackToneDetectionParameters_Type = FxsToneParametrs
_FxsPortConfigRingBackToneDetectionParameters_Object = MibTableColumn
fxsPortConfigRingBackToneDetectionParameters = _FxsPortConfigRingBackToneDetectionParameters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 69),
    _FxsPortConfigRingBackToneDetectionParameters_Type()
)
fxsPortConfigRingBackToneDetectionParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigRingBackToneDetectionParameters.setStatus("current")
_FxsPortConfigBusyToneDetectionParameters_Type = FxsToneParametrs
_FxsPortConfigBusyToneDetectionParameters_Object = MibTableColumn
fxsPortConfigBusyToneDetectionParameters = _FxsPortConfigBusyToneDetectionParameters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 70),
    _FxsPortConfigBusyToneDetectionParameters_Type()
)
fxsPortConfigBusyToneDetectionParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigBusyToneDetectionParameters.setStatus("current")
_FxsPortConfigDtDetectTime_Type = Integer32
_FxsPortConfigDtDetectTime_Object = MibTableColumn
fxsPortConfigDtDetectTime = _FxsPortConfigDtDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 71),
    _FxsPortConfigDtDetectTime_Type()
)
fxsPortConfigDtDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDtDetectTime.setStatus("current")
_FxsPortConfigDecadePulseTime_Type = Integer32
_FxsPortConfigDecadePulseTime_Object = MibTableColumn
fxsPortConfigDecadePulseTime = _FxsPortConfigDecadePulseTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 72),
    _FxsPortConfigDecadePulseTime_Type()
)
fxsPortConfigDecadePulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDecadePulseTime.setStatus("current")
_FxsPortConfigDecadePauseTime_Type = Integer32
_FxsPortConfigDecadePauseTime_Object = MibTableColumn
fxsPortConfigDecadePauseTime = _FxsPortConfigDecadePauseTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 73),
    _FxsPortConfigDecadePauseTime_Type()
)
fxsPortConfigDecadePauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDecadePauseTime.setStatus("current")
_FxsPortConfigNoOffhookAtRinging_Type = TruthValue
_FxsPortConfigNoOffhookAtRinging_Object = MibTableColumn
fxsPortConfigNoOffhookAtRinging = _FxsPortConfigNoOffhookAtRinging_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 74),
    _FxsPortConfigNoOffhookAtRinging_Type()
)
fxsPortConfigNoOffhookAtRinging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigNoOffhookAtRinging.setStatus("current")
_FxsPortConfigFxoCallBusy_Type = TruthValue
_FxsPortConfigFxoCallBusy_Object = MibTableColumn
fxsPortConfigFxoCallBusy = _FxsPortConfigFxoCallBusy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 75),
    _FxsPortConfigFxoCallBusy_Type()
)
fxsPortConfigFxoCallBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigFxoCallBusy.setStatus("current")


class _FxsPortConfigCpcRus_Type(Integer32):
    """Custom type fxsPortConfigCpcRus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FxsPortConfigCpcRus_Type.__name__ = "Integer32"
_FxsPortConfigCpcRus_Object = MibTableColumn
fxsPortConfigCpcRus = _FxsPortConfigCpcRus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 76),
    _FxsPortConfigCpcRus_Type()
)
fxsPortConfigCpcRus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCpcRus.setStatus("current")
_FxsPortConfigReversalPolarityAction_Type = ReversalPolarityAction
_FxsPortConfigReversalPolarityAction_Object = MibTableColumn
fxsPortConfigReversalPolarityAction = _FxsPortConfigReversalPolarityAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 77),
    _FxsPortConfigReversalPolarityAction_Type()
)
fxsPortConfigReversalPolarityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigReversalPolarityAction.setStatus("obsolete")
_FxsPortConfigPstnActivity_Type = PstnActivityType
_FxsPortConfigPstnActivity_Object = MibTableColumn
fxsPortConfigPstnActivity = _FxsPortConfigPstnActivity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 78),
    _FxsPortConfigPstnActivity_Type()
)
fxsPortConfigPstnActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPstnActivity.setStatus("current")


class _FxsPortConfigPstnRbDetectTimeout_Type(Integer32):
    """Custom type fxsPortConfigPstnRbDetectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FxsPortConfigPstnRbDetectTimeout_Type.__name__ = "Integer32"
_FxsPortConfigPstnRbDetectTimeout_Object = MibTableColumn
fxsPortConfigPstnRbDetectTimeout = _FxsPortConfigPstnRbDetectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 79),
    _FxsPortConfigPstnRbDetectTimeout_Type()
)
fxsPortConfigPstnRbDetectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigPstnRbDetectTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fxsPortConfigPstnRbDetectTimeout.setUnits("sec")
_FxsPortConfigDetectFxoLinePresence_Type = TruthValue
_FxsPortConfigDetectFxoLinePresence_Object = MibTableColumn
fxsPortConfigDetectFxoLinePresence = _FxsPortConfigDetectFxoLinePresence_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 80),
    _FxsPortConfigDetectFxoLinePresence_Type()
)
fxsPortConfigDetectFxoLinePresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigDetectFxoLinePresence.setStatus("current")
_FxsPortConfigBlockFxoLineInOutgoingDirection_Type = TruthValue
_FxsPortConfigBlockFxoLineInOutgoingDirection_Object = MibTableColumn
fxsPortConfigBlockFxoLineInOutgoingDirection = _FxsPortConfigBlockFxoLineInOutgoingDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 81),
    _FxsPortConfigBlockFxoLineInOutgoingDirection_Type()
)
fxsPortConfigBlockFxoLineInOutgoingDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigBlockFxoLineInOutgoingDirection.setStatus("current")
_FxsPortConfigFxoMinLevelDetect_Type = Integer32
_FxsPortConfigFxoMinLevelDetect_Object = MibTableColumn
fxsPortConfigFxoMinLevelDetect = _FxsPortConfigFxoMinLevelDetect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 82),
    _FxsPortConfigFxoMinLevelDetect_Type()
)
fxsPortConfigFxoMinLevelDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigFxoMinLevelDetect.setStatus("current")
_FxsPortConfigUseAltNumberAsContact_Type = TruthValue
_FxsPortConfigUseAltNumberAsContact_Object = MibTableColumn
fxsPortConfigUseAltNumberAsContact = _FxsPortConfigUseAltNumberAsContact_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 83),
    _FxsPortConfigUseAltNumberAsContact_Type()
)
fxsPortConfigUseAltNumberAsContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigUseAltNumberAsContact.setStatus("current")
_FxsPortConfigModifier_Type = Integer32
_FxsPortConfigModifier_Object = MibTableColumn
fxsPortConfigModifier = _FxsPortConfigModifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 84),
    _FxsPortConfigModifier_Type()
)
fxsPortConfigModifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigModifier.setStatus("current")
_FxsPortConfigMwiDialtone_Type = TruthValue
_FxsPortConfigMwiDialtone_Object = MibTableColumn
fxsPortConfigMwiDialtone = _FxsPortConfigMwiDialtone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 2, 1, 85),
    _FxsPortConfigMwiDialtone_Type()
)
fxsPortConfigMwiDialtone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigMwiDialtone.setStatus("current")
_FxsPortsConfigCommon_ObjectIdentity = ObjectIdentity
fxsPortsConfigCommon = _FxsPortsConfigCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3)
)
_FxsPortConfigCommonPlaymoh_Type = TruthValue
_FxsPortConfigCommonPlaymoh_Object = MibScalar
fxsPortConfigCommonPlaymoh = _FxsPortConfigCommonPlaymoh_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 1),
    _FxsPortConfigCommonPlaymoh_Type()
)
fxsPortConfigCommonPlaymoh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonPlaymoh.setStatus("obsolete")
_FxsPortConfigCommonAON_Type = FxsAON
_FxsPortConfigCommonAON_Object = MibScalar
fxsPortConfigCommonAON = _FxsPortConfigCommonAON_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 2),
    _FxsPortConfigCommonAON_Type()
)
fxsPortConfigCommonAON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonAON.setStatus("obsolete")
_FxsPortConfigCommonAONHideDate_Type = TruthValue
_FxsPortConfigCommonAONHideDate_Object = MibScalar
fxsPortConfigCommonAONHideDate = _FxsPortConfigCommonAONHideDate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 3),
    _FxsPortConfigCommonAONHideDate_Type()
)
fxsPortConfigCommonAONHideDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonAONHideDate.setStatus("obsolete")
_FxsPortConfigCommonAONHideName_Type = TruthValue
_FxsPortConfigCommonAONHideName_Object = MibScalar
fxsPortConfigCommonAONHideName = _FxsPortConfigCommonAONHideName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 4),
    _FxsPortConfigCommonAONHideName_Type()
)
fxsPortConfigCommonAONHideName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonAONHideName.setStatus("obsolete")
_FxsPortConfigCommonTaxophone_Type = FxsTaxophoneType
_FxsPortConfigCommonTaxophone_Object = MibScalar
fxsPortConfigCommonTaxophone = _FxsPortConfigCommonTaxophone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 5),
    _FxsPortConfigCommonTaxophone_Type()
)
fxsPortConfigCommonTaxophone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonTaxophone.setStatus("obsolete")
_FxsPortConfigCommonMinFlashtime_Type = Integer32
_FxsPortConfigCommonMinFlashtime_Object = MibScalar
fxsPortConfigCommonMinFlashtime = _FxsPortConfigCommonMinFlashtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 6),
    _FxsPortConfigCommonMinFlashtime_Type()
)
fxsPortConfigCommonMinFlashtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonMinFlashtime.setStatus("obsolete")
_FxsPortConfigCommonMaxFlashtime_Type = Integer32
_FxsPortConfigCommonMaxFlashtime_Object = MibScalar
fxsPortConfigCommonMaxFlashtime = _FxsPortConfigCommonMaxFlashtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 7),
    _FxsPortConfigCommonMaxFlashtime_Type()
)
fxsPortConfigCommonMaxFlashtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonMaxFlashtime.setStatus("obsolete")
_FxsPortConfigCommonGainr_Type = Integer32
_FxsPortConfigCommonGainr_Object = MibScalar
fxsPortConfigCommonGainr = _FxsPortConfigCommonGainr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 8),
    _FxsPortConfigCommonGainr_Type()
)
fxsPortConfigCommonGainr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonGainr.setStatus("obsolete")
_FxsPortConfigCommonGaint_Type = Integer32
_FxsPortConfigCommonGaint_Object = MibScalar
fxsPortConfigCommonGaint = _FxsPortConfigCommonGaint_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 9),
    _FxsPortConfigCommonGaint_Type()
)
fxsPortConfigCommonGaint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonGaint.setStatus("obsolete")
_FxsPortConfigCommonCategory_Type = Integer32
_FxsPortConfigCommonCategory_Object = MibScalar
fxsPortConfigCommonCategory = _FxsPortConfigCommonCategory_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 10),
    _FxsPortConfigCommonCategory_Type()
)
fxsPortConfigCommonCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonCategory.setStatus("obsolete")
_FxsPortConfigCommonCallTransfer_Type = FxsProcessFlashType
_FxsPortConfigCommonCallTransfer_Object = MibScalar
fxsPortConfigCommonCallTransfer = _FxsPortConfigCommonCallTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 11),
    _FxsPortConfigCommonCallTransfer_Type()
)
fxsPortConfigCommonCallTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonCallTransfer.setStatus("obsolete")
_FxsPortConfigCommonCallWaiting_Type = TruthValue
_FxsPortConfigCommonCallWaiting_Object = MibScalar
fxsPortConfigCommonCallWaiting = _FxsPortConfigCommonCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 12),
    _FxsPortConfigCommonCallWaiting_Type()
)
fxsPortConfigCommonCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonCallWaiting.setStatus("obsolete")
_FxsPortConfigCommonCfgPriOverCw_Type = TruthValue
_FxsPortConfigCommonCfgPriOverCw_Object = MibScalar
fxsPortConfigCommonCfgPriOverCw = _FxsPortConfigCommonCfgPriOverCw_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 13),
    _FxsPortConfigCommonCfgPriOverCw_Type()
)
fxsPortConfigCommonCfgPriOverCw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonCfgPriOverCw.setStatus("obsolete")
_FxsPortConfigCommonFxoFlashTime_Type = Integer32
_FxsPortConfigCommonFxoFlashTime_Object = MibScalar
fxsPortConfigCommonFxoFlashTime = _FxsPortConfigCommonFxoFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 14),
    _FxsPortConfigCommonFxoFlashTime_Type()
)
fxsPortConfigCommonFxoFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonFxoFlashTime.setStatus("obsolete")
_FxsPortConfigCommonFxoDelTdm_Type = Integer32
_FxsPortConfigCommonFxoDelTdm_Object = MibScalar
fxsPortConfigCommonFxoDelTdm = _FxsPortConfigCommonFxoDelTdm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 15),
    _FxsPortConfigCommonFxoDelTdm_Type()
)
fxsPortConfigCommonFxoDelTdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonFxoDelTdm.setStatus("obsolete")
_FxsPortConfigCommonFxoRingtdm_Type = Integer32
_FxsPortConfigCommonFxoRingtdm_Object = MibScalar
fxsPortConfigCommonFxoRingtdm = _FxsPortConfigCommonFxoRingtdm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 16),
    _FxsPortConfigCommonFxoRingtdm_Type()
)
fxsPortConfigCommonFxoRingtdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonFxoRingtdm.setStatus("obsolete")
_FxsPortConfigCommonPstnNumberprefix_Type = DisplayString
_FxsPortConfigCommonPstnNumberprefix_Object = MibScalar
fxsPortConfigCommonPstnNumberprefix = _FxsPortConfigCommonPstnNumberprefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 17),
    _FxsPortConfigCommonPstnNumberprefix_Type()
)
fxsPortConfigCommonPstnNumberprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonPstnNumberprefix.setStatus("obsolete")
_FxsPortConfigCommonPstnNameprefix_Type = DisplayString
_FxsPortConfigCommonPstnNameprefix_Object = MibScalar
fxsPortConfigCommonPstnNameprefix = _FxsPortConfigCommonPstnNameprefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 18),
    _FxsPortConfigCommonPstnNameprefix_Type()
)
fxsPortConfigCommonPstnNameprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonPstnNameprefix.setStatus("obsolete")
_FxsPortConfigCommonUsePstnCid_Type = TruthValue
_FxsPortConfigCommonUsePstnCid_Object = MibScalar
fxsPortConfigCommonUsePstnCid = _FxsPortConfigCommonUsePstnCid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 19),
    _FxsPortConfigCommonUsePstnCid_Type()
)
fxsPortConfigCommonUsePstnCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonUsePstnCid.setStatus("obsolete")
_FxsPortConfigCommonEnableCpc_Type = TruthValue
_FxsPortConfigCommonEnableCpc_Object = MibScalar
fxsPortConfigCommonEnableCpc = _FxsPortConfigCommonEnableCpc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 20),
    _FxsPortConfigCommonEnableCpc_Type()
)
fxsPortConfigCommonEnableCpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonEnableCpc.setStatus("obsolete")
_FxsPortConfigCommonCpcTime_Type = TruthValue
_FxsPortConfigCommonCpcTime_Object = MibScalar
fxsPortConfigCommonCpcTime = _FxsPortConfigCommonCpcTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 21),
    _FxsPortConfigCommonCpcTime_Type()
)
fxsPortConfigCommonCpcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonCpcTime.setStatus("obsolete")
_FxsPortConfigCommonDontDetectDT_Type = TruthValue
_FxsPortConfigCommonDontDetectDT_Object = MibScalar
fxsPortConfigCommonDontDetectDT = _FxsPortConfigCommonDontDetectDT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 22),
    _FxsPortConfigCommonDontDetectDT_Type()
)
fxsPortConfigCommonDontDetectDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonDontDetectDT.setStatus("obsolete")
_FxsPortConfigCommonDelayDialingTimeout_Type = Integer32
_FxsPortConfigCommonDelayDialingTimeout_Object = MibScalar
fxsPortConfigCommonDelayDialingTimeout = _FxsPortConfigCommonDelayDialingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 23),
    _FxsPortConfigCommonDelayDialingTimeout_Type()
)
fxsPortConfigCommonDelayDialingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonDelayDialingTimeout.setStatus("obsolete")
_FxsPortConfigCommonDialing_Type = FxoDialingType
_FxsPortConfigCommonDialing_Object = MibScalar
fxsPortConfigCommonDialing = _FxsPortConfigCommonDialing_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 24),
    _FxsPortConfigCommonDialing_Type()
)
fxsPortConfigCommonDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonDialing.setStatus("obsolete")
_FxsPortConfigCommonTransmitNumber_Type = TruthValue
_FxsPortConfigCommonTransmitNumber_Object = MibScalar
fxsPortConfigCommonTransmitNumber = _FxsPortConfigCommonTransmitNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 25),
    _FxsPortConfigCommonTransmitNumber_Type()
)
fxsPortConfigCommonTransmitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonTransmitNumber.setStatus("obsolete")
_FxsPortConfigCommonDontTransmitPrefix_Type = TruthValue
_FxsPortConfigCommonDontTransmitPrefix_Object = MibScalar
fxsPortConfigCommonDontTransmitPrefix = _FxsPortConfigCommonDontTransmitPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 3, 26),
    _FxsPortConfigCommonDontTransmitPrefix_Type()
)
fxsPortConfigCommonDontTransmitPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsPortConfigCommonDontTransmitPrefix.setStatus("obsolete")
_MegacoPortsMonitoringTable_Object = MibTable
megacoPortsMonitoringTable = _MegacoPortsMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4)
)
if mibBuilder.loadTexts:
    megacoPortsMonitoringTable.setStatus("current")
_MegacoPortsMonitoringEntry_Object = MibTableRow
megacoPortsMonitoringEntry = _MegacoPortsMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1)
)
megacoPortsMonitoringEntry.setIndexNames(
    (0, "ELTEX-FXS72", "megacoPortNumber"),
)
if mibBuilder.loadTexts:
    megacoPortsMonitoringEntry.setStatus("current")


class _MegacoPortNumber_Type(Integer32):
    """Custom type megacoPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 72),
    )


_MegacoPortNumber_Type.__name__ = "Integer32"
_MegacoPortNumber_Object = MibTableColumn
megacoPortNumber = _MegacoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 1),
    _MegacoPortNumber_Type()
)
megacoPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    megacoPortNumber.setStatus("current")
_MegacoPortTerminationID_Type = DisplayString
_MegacoPortTerminationID_Object = MibTableColumn
megacoPortTerminationID = _MegacoPortTerminationID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 2),
    _MegacoPortTerminationID_Type()
)
megacoPortTerminationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoPortTerminationID.setStatus("current")
_MegacoPortComments_Type = DisplayString
_MegacoPortComments_Object = MibTableColumn
megacoPortComments = _MegacoPortComments_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 3),
    _MegacoPortComments_Type()
)
megacoPortComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoPortComments.setStatus("current")
_MegacoPortState_Type = PortMegacoState
_MegacoPortState_Object = MibTableColumn
megacoPortState = _MegacoPortState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 4),
    _MegacoPortState_Type()
)
megacoPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoPortState.setStatus("current")
_MegacoPortStateStartTime_Type = DisplayString
_MegacoPortStateStartTime_Object = MibTableColumn
megacoPortStateStartTime = _MegacoPortStateStartTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 5),
    _MegacoPortStateStartTime_Type()
)
megacoPortStateStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoPortStateStartTime.setStatus("current")
_MegacoPortStateDuration_Type = DisplayString
_MegacoPortStateDuration_Object = MibTableColumn
megacoPortStateDuration = _MegacoPortStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 6),
    _MegacoPortStateDuration_Type()
)
megacoPortStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoPortStateDuration.setStatus("current")
_MegacoPortJitter_Type = PortMegacoJitter
_MegacoPortJitter_Object = MibTableColumn
megacoPortJitter = _MegacoPortJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 7),
    _MegacoPortJitter_Type()
)
megacoPortJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoPortJitter.setStatus("current")
_MegacoPortTelNo_Type = DisplayString
_MegacoPortTelNo_Object = MibTableColumn
megacoPortTelNo = _MegacoPortTelNo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 12, 4, 1, 8),
    _MegacoPortTelNo_Type()
)
megacoPortTelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    megacoPortTelNo.setStatus("current")
_FxsDialMIBBoundary_Type = Integer32
_FxsDialMIBBoundary_Object = MibScalar
fxsDialMIBBoundary = _FxsDialMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 13),
    _FxsDialMIBBoundary_Type()
)
fxsDialMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsDialMIBBoundary.setStatus("current")
_FxsDial_ObjectIdentity = ObjectIdentity
fxsDial = _FxsDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14)
)
_FxsDialPlanTable_Object = MibTable
fxsDialPlanTable = _FxsDialPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1)
)
if mibBuilder.loadTexts:
    fxsDialPlanTable.setStatus("obsolete")
_FxsDialPlanEntry_Object = MibTableRow
fxsDialPlanEntry = _FxsDialPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1)
)
fxsDialPlanEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxsDialPlanNumber"),
)
if mibBuilder.loadTexts:
    fxsDialPlanEntry.setStatus("obsolete")
_FxsDialPlanHost_Type = DisplayString
_FxsDialPlanHost_Object = MibTableColumn
fxsDialPlanHost = _FxsDialPlanHost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 1),
    _FxsDialPlanHost_Type()
)
fxsDialPlanHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanHost.setStatus("obsolete")
_FxsDialPlanDigits_Type = DisplayString
_FxsDialPlanDigits_Object = MibTableColumn
fxsDialPlanDigits = _FxsDialPlanDigits_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 2),
    _FxsDialPlanDigits_Type()
)
fxsDialPlanDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanDigits.setStatus("obsolete")
_FxsDialPlanTimeout_Type = Integer32
_FxsDialPlanTimeout_Object = MibTableColumn
fxsDialPlanTimeout = _FxsDialPlanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 3),
    _FxsDialPlanTimeout_Type()
)
fxsDialPlanTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanTimeout.setStatus("obsolete")
_FxsDialPlanMinDigits_Type = Integer32
_FxsDialPlanMinDigits_Object = MibTableColumn
fxsDialPlanMinDigits = _FxsDialPlanMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 4),
    _FxsDialPlanMinDigits_Type()
)
fxsDialPlanMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanMinDigits.setStatus("obsolete")
_FxsDialPlanType_Type = FxsDialPlanType
_FxsDialPlanType_Object = MibTableColumn
fxsDialPlanType = _FxsDialPlanType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 5),
    _FxsDialPlanType_Type()
)
fxsDialPlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanType.setStatus("obsolete")
_FxsDialPlanAccessMask_Type = DisplayString
_FxsDialPlanAccessMask_Object = MibTableColumn
fxsDialPlanAccessMask = _FxsDialPlanAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 6),
    _FxsDialPlanAccessMask_Type()
)
fxsDialPlanAccessMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanAccessMask.setStatus("obsolete")
_FxsDialPlanDialtone_Type = TruthValue
_FxsDialPlanDialtone_Object = MibTableColumn
fxsDialPlanDialtone = _FxsDialPlanDialtone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 7),
    _FxsDialPlanDialtone_Type()
)
fxsDialPlanDialtone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanDialtone.setStatus("obsolete")
_FxsDialPlanModifier_Type = DisplayString
_FxsDialPlanModifier_Object = MibTableColumn
fxsDialPlanModifier = _FxsDialPlanModifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 8),
    _FxsDialPlanModifier_Type()
)
fxsDialPlanModifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanModifier.setStatus("obsolete")
_FxsDialPlanNature_Type = FxsDialPlanNatureType
_FxsDialPlanNature_Object = MibTableColumn
fxsDialPlanNature = _FxsDialPlanNature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 9),
    _FxsDialPlanNature_Type()
)
fxsDialPlanNature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanNature.setStatus("obsolete")
_FxsDialPlanDelnum_Type = Integer32
_FxsDialPlanDelnum_Object = MibTableColumn
fxsDialPlanDelnum = _FxsDialPlanDelnum_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 10),
    _FxsDialPlanDelnum_Type()
)
fxsDialPlanDelnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanDelnum.setStatus("obsolete")
_FxsDialPlanPtime_Type = Integer32
_FxsDialPlanPtime_Object = MibTableColumn
fxsDialPlanPtime = _FxsDialPlanPtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 11),
    _FxsDialPlanPtime_Type()
)
fxsDialPlanPtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialPlanPtime.setStatus("obsolete")
_FxsDialRowStatus_Type = RowStatus
_FxsDialRowStatus_Object = MibTableColumn
fxsDialRowStatus = _FxsDialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 12),
    _FxsDialRowStatus_Type()
)
fxsDialRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsDialRowStatus.setStatus("obsolete")


class _FxsDialPlanNumber_Type(Integer32):
    """Custom type fxsDialPlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_FxsDialPlanNumber_Type.__name__ = "Integer32"
_FxsDialPlanNumber_Object = MibTableColumn
fxsDialPlanNumber = _FxsDialPlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 1, 1, 13),
    _FxsDialPlanNumber_Type()
)
fxsDialPlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxsDialPlanNumber.setStatus("obsolete")
_FxsDialPlanNext_Type = Integer32
_FxsDialPlanNext_Object = MibScalar
fxsDialPlanNext = _FxsDialPlanNext_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 2),
    _FxsDialPlanNext_Type()
)
fxsDialPlanNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsDialPlanNext.setStatus("obsolete")
_TauDialPlansRegExp_ObjectIdentity = ObjectIdentity
tauDialPlansRegExp = _TauDialPlansRegExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 3)
)
_TauDialRegularOn_Type = TruthValue
_TauDialRegularOn_Object = MibScalar
tauDialRegularOn = _TauDialRegularOn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 3, 1),
    _TauDialRegularOn_Type()
)
tauDialRegularOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauDialRegularOn.setStatus("obsolete")
_TauDialRegularProtocol_Type = TauDialProtocolType
_TauDialRegularProtocol_Object = MibScalar
tauDialRegularProtocol = _TauDialRegularProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 3, 2),
    _TauDialRegularProtocol_Type()
)
tauDialRegularProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauDialRegularProtocol.setStatus("obsolete")
_TauDialRegularText_Type = OctetString
_TauDialRegularText_Object = MibScalar
tauDialRegularText = _TauDialRegularText_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 14, 3, 3),
    _TauDialRegularText_Type()
)
tauDialRegularText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauDialRegularText.setStatus("obsolete")
_FxsConfigSave_Type = Integer32
_FxsConfigSave_Object = MibScalar
fxsConfigSave = _FxsConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 15),
    _FxsConfigSave_Type()
)
fxsConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsConfigSave.setStatus("current")
_FxsConfigApply_Type = Integer32
_FxsConfigApply_Object = MibScalar
fxsConfigApply = _FxsConfigApply_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 16),
    _FxsConfigApply_Type()
)
fxsConfigApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsConfigApply.setStatus("obsolete")
_FxsSerialGroupsMIBBoundary_Type = Integer32
_FxsSerialGroupsMIBBoundary_Object = MibScalar
fxsSerialGroupsMIBBoundary = _FxsSerialGroupsMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 17),
    _FxsSerialGroupsMIBBoundary_Type()
)
fxsSerialGroupsMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsSerialGroupsMIBBoundary.setStatus("current")
_FxsSerialGroups_ObjectIdentity = ObjectIdentity
fxsSerialGroups = _FxsSerialGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18)
)
_FxsSerialGroupsTable_Object = MibTable
fxsSerialGroupsTable = _FxsSerialGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1)
)
if mibBuilder.loadTexts:
    fxsSerialGroupsTable.setStatus("current")
_FxsSerialGroupsEntry_Object = MibTableRow
fxsSerialGroupsEntry = _FxsSerialGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1)
)
fxsSerialGroupsEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxsDialPlanNumber"),
)
if mibBuilder.loadTexts:
    fxsSerialGroupsEntry.setStatus("current")
_FxsSerialGroupsPhone_Type = DisplayString
_FxsSerialGroupsPhone_Object = MibTableColumn
fxsSerialGroupsPhone = _FxsSerialGroupsPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 1),
    _FxsSerialGroupsPhone_Type()
)
fxsSerialGroupsPhone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsPhone.setStatus("current")
_FxsSerialGroupsEnabled_Type = FxsGroupSerialEnableType
_FxsSerialGroupsEnabled_Object = MibTableColumn
fxsSerialGroupsEnabled = _FxsSerialGroupsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 2),
    _FxsSerialGroupsEnabled_Type()
)
fxsSerialGroupsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsEnabled.setStatus("current")
_FxsSerialGroupsSerialType_Type = FxsGroupSerialType
_FxsSerialGroupsSerialType_Object = MibTableColumn
fxsSerialGroupsSerialType = _FxsSerialGroupsSerialType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 3),
    _FxsSerialGroupsSerialType_Type()
)
fxsSerialGroupsSerialType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsSerialType.setStatus("current")
_FxsSerialGroupsBusyType_Type = FxsGroupBusyType
_FxsSerialGroupsBusyType_Object = MibTableColumn
fxsSerialGroupsBusyType = _FxsSerialGroupsBusyType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 4),
    _FxsSerialGroupsBusyType_Type()
)
fxsSerialGroupsBusyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsBusyType.setStatus("current")
_FxsSerialGroupsTimeout_Type = Integer32
_FxsSerialGroupsTimeout_Object = MibTableColumn
fxsSerialGroupsTimeout = _FxsSerialGroupsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 5),
    _FxsSerialGroupsTimeout_Type()
)
fxsSerialGroupsTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsTimeout.setStatus("current")
_FxsSerialGroupsSipPort_Type = Integer32
_FxsSerialGroupsSipPort_Object = MibTableColumn
fxsSerialGroupsSipPort = _FxsSerialGroupsSipPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 6),
    _FxsSerialGroupsSipPort_Type()
)
fxsSerialGroupsSipPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsSipPort.setStatus("current")
_FxsSerialGroupsAuthName_Type = DisplayString
_FxsSerialGroupsAuthName_Object = MibTableColumn
fxsSerialGroupsAuthName = _FxsSerialGroupsAuthName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 7),
    _FxsSerialGroupsAuthName_Type()
)
fxsSerialGroupsAuthName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsAuthName.setStatus("current")
_FxsSerialGroupsAuthPass_Type = DisplayString
_FxsSerialGroupsAuthPass_Object = MibTableColumn
fxsSerialGroupsAuthPass = _FxsSerialGroupsAuthPass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 8),
    _FxsSerialGroupsAuthPass_Type()
)
fxsSerialGroupsAuthPass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsAuthPass.setStatus("current")
_FxsSerialGroupsPorts_Type = DisplayString
_FxsSerialGroupsPorts_Object = MibTableColumn
fxsSerialGroupsPorts = _FxsSerialGroupsPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 9),
    _FxsSerialGroupsPorts_Type()
)
fxsSerialGroupsPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsPorts.setStatus("current")
_FxsSerialGroupsSipProfile_Type = Integer32
_FxsSerialGroupsSipProfile_Object = MibTableColumn
fxsSerialGroupsSipProfile = _FxsSerialGroupsSipProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 10),
    _FxsSerialGroupsSipProfile_Type()
)
fxsSerialGroupsSipProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsSipProfile.setStatus("current")
_FxsSerialGroupsRowStatus_Type = RowStatus
_FxsSerialGroupsRowStatus_Object = MibTableColumn
fxsSerialGroupsRowStatus = _FxsSerialGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 1, 1, 11),
    _FxsSerialGroupsRowStatus_Type()
)
fxsSerialGroupsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxsSerialGroupsRowStatus.setStatus("current")
_FxsSerialGroupsNextEmpty_Type = Integer32
_FxsSerialGroupsNextEmpty_Object = MibScalar
fxsSerialGroupsNextEmpty = _FxsSerialGroupsNextEmpty_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 18, 2),
    _FxsSerialGroupsNextEmpty_Type()
)
fxsSerialGroupsNextEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxsSerialGroupsNextEmpty.setStatus("current")
_FxsReboot_Type = Integer32
_FxsReboot_Object = MibScalar
fxsReboot = _FxsReboot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 19),
    _FxsReboot_Type()
)
fxsReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsReboot.setStatus("current")
_TauVoipDvo_ObjectIdentity = ObjectIdentity
tauVoipDvo = _TauVoipDvo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20)
)
_TauVoipDvoCallwaiting_Type = DisplayString
_TauVoipDvoCallwaiting_Object = MibScalar
tauVoipDvoCallwaiting = _TauVoipDvoCallwaiting_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 1),
    _TauVoipDvoCallwaiting_Type()
)
tauVoipDvoCallwaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoCallwaiting.setStatus("current")
_TauVoipDvoCtAttended_Type = DisplayString
_TauVoipDvoCtAttended_Object = MibScalar
tauVoipDvoCtAttended = _TauVoipDvoCtAttended_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 2),
    _TauVoipDvoCtAttended_Type()
)
tauVoipDvoCtAttended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoCtAttended.setStatus("current")
_TauVoipDvoCtUnattended_Type = DisplayString
_TauVoipDvoCtUnattended_Object = MibScalar
tauVoipDvoCtUnattended = _TauVoipDvoCtUnattended_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 3),
    _TauVoipDvoCtUnattended_Type()
)
tauVoipDvoCtUnattended.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoCtUnattended.setStatus("current")
_TauVoipDvoCfUnconditional_Type = DisplayString
_TauVoipDvoCfUnconditional_Object = MibScalar
tauVoipDvoCfUnconditional = _TauVoipDvoCfUnconditional_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 4),
    _TauVoipDvoCfUnconditional_Type()
)
tauVoipDvoCfUnconditional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoCfUnconditional.setStatus("current")
_TauVoipDvoCfBusy_Type = DisplayString
_TauVoipDvoCfBusy_Object = MibScalar
tauVoipDvoCfBusy = _TauVoipDvoCfBusy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 5),
    _TauVoipDvoCfBusy_Type()
)
tauVoipDvoCfBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoCfBusy.setStatus("current")
_TauVoipDvoCfNoanswer_Type = DisplayString
_TauVoipDvoCfNoanswer_Object = MibScalar
tauVoipDvoCfNoanswer = _TauVoipDvoCfNoanswer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 6),
    _TauVoipDvoCfNoanswer_Type()
)
tauVoipDvoCfNoanswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoCfNoanswer.setStatus("current")
_TauVoipDvoCfService_Type = DisplayString
_TauVoipDvoCfService_Object = MibScalar
tauVoipDvoCfService = _TauVoipDvoCfService_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 7),
    _TauVoipDvoCfService_Type()
)
tauVoipDvoCfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoCfService.setStatus("current")
_TauVoipDvoDoDisturb_Type = DisplayString
_TauVoipDvoDoDisturb_Object = MibScalar
tauVoipDvoDoDisturb = _TauVoipDvoDoDisturb_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 20, 8),
    _TauVoipDvoDoDisturb_Type()
)
tauVoipDvoDoDisturb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauVoipDvoDoDisturb.setStatus("current")
_TauSipConfig_ObjectIdentity = ObjectIdentity
tauSipConfig = _TauSipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21)
)
_SipEnablesip_Type = TruthValue
_SipEnablesip_Object = MibScalar
sipEnablesip = _SipEnablesip_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 1),
    _SipEnablesip_Type()
)
sipEnablesip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipEnablesip.setStatus("obsolete")
_SipObtimeout_Type = Integer32
_SipObtimeout_Object = MibScalar
sipObtimeout = _SipObtimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 2),
    _SipObtimeout_Type()
)
sipObtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipObtimeout.setStatus("obsolete")
_SipMode_Type = ProxyMode
_SipMode_Object = MibScalar
sipMode = _SipMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 3),
    _SipMode_Type()
)
sipMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMode.setStatus("obsolete")
_SipOptions_Type = OptionsHomeServerTest
_SipOptions_Object = MibScalar
sipOptions = _SipOptions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 4),
    _SipOptions_Type()
)
sipOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipOptions.setStatus("obsolete")
_SipKeepalivet_Type = Integer32
_SipKeepalivet_Object = MibScalar
sipKeepalivet = _SipKeepalivet_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 5),
    _SipKeepalivet_Type()
)
sipKeepalivet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipKeepalivet.setStatus("obsolete")
_SipDomainToReg_Type = TruthValue
_SipDomainToReg_Object = MibScalar
sipDomainToReg = _SipDomainToReg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 6),
    _SipDomainToReg_Type()
)
sipDomainToReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDomainToReg.setStatus("obsolete")
_SipDomain_Type = DisplayString
_SipDomain_Object = MibScalar
sipDomain = _SipDomain_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 7),
    _SipDomain_Type()
)
sipDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDomain.setStatus("obsolete")
_SipRegisterRetryInterval_Type = Integer32
_SipRegisterRetryInterval_Object = MibScalar
sipRegisterRetryInterval = _SipRegisterRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 8),
    _SipRegisterRetryInterval_Type()
)
sipRegisterRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegisterRetryInterval.setStatus("obsolete")
_SipOutbound_Type = OutboundType
_SipOutbound_Object = MibScalar
sipOutbound = _SipOutbound_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 9),
    _SipOutbound_Type()
)
sipOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipOutbound.setStatus("obsolete")
_SipInboundProxy_Type = TruthValue
_SipInboundProxy_Object = MibScalar
sipInboundProxy = _SipInboundProxy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 10),
    _SipInboundProxy_Type()
)
sipInboundProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInboundProxy.setStatus("obsolete")
_SipExpires_Type = Integer32
_SipExpires_Object = MibScalar
sipExpires = _SipExpires_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 11),
    _SipExpires_Type()
)
sipExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipExpires.setStatus("obsolete")
_SipAuthentication_Type = AuthenticationType
_SipAuthentication_Object = MibScalar
sipAuthentication = _SipAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 12),
    _SipAuthentication_Type()
)
sipAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipAuthentication.setStatus("obsolete")
_SipUsername_Type = DisplayString
_SipUsername_Object = MibScalar
sipUsername = _SipUsername_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 13),
    _SipUsername_Type()
)
sipUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUsername.setStatus("obsolete")
_SipPassword_Type = DisplayString
_SipPassword_Object = MibScalar
sipPassword = _SipPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 14),
    _SipPassword_Type()
)
sipPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPassword.setStatus("obsolete")
_SipProxy0_Type = DisplayString
_SipProxy0_Object = MibScalar
sipProxy0 = _SipProxy0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 15),
    _SipProxy0_Type()
)
sipProxy0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxy0.setStatus("obsolete")
_SipRegrar0_Type = DisplayString
_SipRegrar0_Object = MibScalar
sipRegrar0 = _SipRegrar0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 16),
    _SipRegrar0_Type()
)
sipRegrar0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegrar0.setStatus("obsolete")
_SipRegistration0_Type = TruthValue
_SipRegistration0_Object = MibScalar
sipRegistration0 = _SipRegistration0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 17),
    _SipRegistration0_Type()
)
sipRegistration0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistration0.setStatus("obsolete")
_SipProxy1_Type = DisplayString
_SipProxy1_Object = MibScalar
sipProxy1 = _SipProxy1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 18),
    _SipProxy1_Type()
)
sipProxy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxy1.setStatus("obsolete")
_SipRegrar1_Type = DisplayString
_SipRegrar1_Object = MibScalar
sipRegrar1 = _SipRegrar1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 19),
    _SipRegrar1_Type()
)
sipRegrar1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegrar1.setStatus("obsolete")
_SipProxy2_Type = DisplayString
_SipProxy2_Object = MibScalar
sipProxy2 = _SipProxy2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 20),
    _SipProxy2_Type()
)
sipProxy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxy2.setStatus("obsolete")
_SipRegrar2_Type = DisplayString
_SipRegrar2_Object = MibScalar
sipRegrar2 = _SipRegrar2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 21),
    _SipRegrar2_Type()
)
sipRegrar2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegrar2.setStatus("obsolete")
_SipProxy3_Type = DisplayString
_SipProxy3_Object = MibScalar
sipProxy3 = _SipProxy3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 22),
    _SipProxy3_Type()
)
sipProxy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxy3.setStatus("obsolete")
_SipRegrar3_Type = DisplayString
_SipRegrar3_Object = MibScalar
sipRegrar3 = _SipRegrar3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 23),
    _SipRegrar3_Type()
)
sipRegrar3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegrar3.setStatus("obsolete")
_SipProxy4_Type = DisplayString
_SipProxy4_Object = MibScalar
sipProxy4 = _SipProxy4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 24),
    _SipProxy4_Type()
)
sipProxy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProxy4.setStatus("obsolete")
_SipRegrar4_Type = DisplayString
_SipRegrar4_Object = MibScalar
sipRegrar4 = _SipRegrar4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 25),
    _SipRegrar4_Type()
)
sipRegrar4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegrar4.setStatus("obsolete")
_SipDtmfmime_Type = DTMFMIMEType
_SipDtmfmime_Object = MibScalar
sipDtmfmime = _SipDtmfmime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 26),
    _SipDtmfmime_Type()
)
sipDtmfmime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipDtmfmime.setStatus("obsolete")
_SipHfmime_Type = HookFlashMIMEType
_SipHfmime_Object = MibScalar
sipHfmime = _SipHfmime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 27),
    _SipHfmime_Type()
)
sipHfmime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipHfmime.setStatus("obsolete")
_SipCtWithReplaces_Type = TruthValue
_SipCtWithReplaces_Object = MibScalar
sipCtWithReplaces = _SipCtWithReplaces_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 28),
    _SipCtWithReplaces_Type()
)
sipCtWithReplaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCtWithReplaces.setStatus("obsolete")
_SipShortmode_Type = TruthValue
_SipShortmode_Object = MibScalar
sipShortmode = _SipShortmode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 29),
    _SipShortmode_Type()
)
sipShortmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipShortmode.setStatus("obsolete")
_SipTransport_Type = TypeTransport
_SipTransport_Object = MibScalar
sipTransport = _SipTransport_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 30),
    _SipTransport_Type()
)
sipTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipTransport.setStatus("obsolete")
_SipSipMtu_Type = Integer32
_SipSipMtu_Object = MibScalar
sipSipMtu = _SipSipMtu_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 31),
    _SipSipMtu_Type()
)
sipSipMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipSipMtu.setStatus("obsolete")
_Sip100Rel_Type = Type100rel
_Sip100Rel_Object = MibScalar
sip100Rel = _Sip100Rel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 32),
    _Sip100Rel_Type()
)
sip100Rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sip100Rel.setStatus("obsolete")
_SipUserPhone_Type = TruthValue
_SipUserPhone_Object = MibScalar
sipUserPhone = _SipUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 33),
    _SipUserPhone_Type()
)
sipUserPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUserPhone.setStatus("obsolete")
_SipUriEscapeHash_Type = TruthValue
_SipUriEscapeHash_Object = MibScalar
sipUriEscapeHash = _SipUriEscapeHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 34),
    _SipUriEscapeHash_Type()
)
sipUriEscapeHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipUriEscapeHash.setStatus("obsolete")
_SipInviteTotalT_Type = Integer32
_SipInviteTotalT_Object = MibScalar
sipInviteTotalT = _SipInviteTotalT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 35),
    _SipInviteTotalT_Type()
)
sipInviteTotalT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInviteTotalT.setStatus("obsolete")
_SipInviteInitT_Type = Integer32
_SipInviteInitT_Object = MibScalar
sipInviteInitT = _SipInviteInitT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 36),
    _SipInviteInitT_Type()
)
sipInviteInitT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipInviteInitT.setStatus("obsolete")
_SipCwRingback_Type = CwRingbackRingbackAtCallwaiting
_SipCwRingback_Object = MibScalar
sipCwRingback = _SipCwRingback_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 37),
    _SipCwRingback_Type()
)
sipCwRingback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCwRingback.setStatus("obsolete")
_SipRingbackSdp_Type = RemoteRingback
_SipRingbackSdp_Object = MibScalar
sipRingbackSdp = _SipRingbackSdp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 38),
    _SipRingbackSdp_Type()
)
sipRingbackSdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRingbackSdp.setStatus("obsolete")
_SipRingback_Type = TruthValue
_SipRingback_Object = MibScalar
sipRingback = _SipRingback_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 39),
    _SipRingback_Type()
)
sipRingback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRingback.setStatus("obsolete")
_SipRegistration1_Type = TruthValue
_SipRegistration1_Object = MibScalar
sipRegistration1 = _SipRegistration1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 40),
    _SipRegistration1_Type()
)
sipRegistration1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistration1.setStatus("obsolete")
_SipRegistration2_Type = TruthValue
_SipRegistration2_Object = MibScalar
sipRegistration2 = _SipRegistration2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 41),
    _SipRegistration2_Type()
)
sipRegistration2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistration2.setStatus("obsolete")
_SipRegistration3_Type = TruthValue
_SipRegistration3_Object = MibScalar
sipRegistration3 = _SipRegistration3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 42),
    _SipRegistration3_Type()
)
sipRegistration3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistration3.setStatus("obsolete")
_SipRegistration4_Type = TruthValue
_SipRegistration4_Object = MibScalar
sipRegistration4 = _SipRegistration4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 43),
    _SipRegistration4_Type()
)
sipRegistration4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipRegistration4.setStatus("obsolete")
_SipPRTPstat_Type = TruthValue
_SipPRTPstat_Object = MibScalar
sipPRTPstat = _SipPRTPstat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 21, 44),
    _SipPRTPstat_Type()
)
sipPRTPstat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPRTPstat.setStatus("obsolete")
_FxsStatTable_Object = MibTable
fxsStatTable = _FxsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23)
)
if mibBuilder.loadTexts:
    fxsStatTable.setStatus("current")
_FxsStatEntry_Object = MibTableRow
fxsStatEntry = _FxsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1)
)
fxsStatEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxsPortNumber"),
)
if mibBuilder.loadTexts:
    fxsStatEntry.setStatus("current")
_TermID_Type = Integer32
_TermID_Object = MibTableColumn
termID = _TermID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 1),
    _TermID_Type()
)
termID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termID.setStatus("current")
_CurrentState_Type = FxsPortState
_CurrentState_Object = MibTableColumn
currentState = _CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 2),
    _CurrentState_Type()
)
currentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentState.setStatus("current")
_TotalCallCount_Type = Integer32
_TotalCallCount_Object = MibTableColumn
totalCallCount = _TotalCallCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 3),
    _TotalCallCount_Type()
)
totalCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalCallCount.setStatus("current")
_LastCallPhone_Type = DisplayString
_LastCallPhone_Object = MibTableColumn
lastCallPhone = _LastCallPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 4),
    _LastCallPhone_Type()
)
lastCallPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCallPhone.setStatus("current")
_PeakJitter_Type = Integer32
_PeakJitter_Object = MibTableColumn
peakJitter = _PeakJitter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 5),
    _PeakJitter_Type()
)
peakJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakJitter.setStatus("current")
_LostPackets_Type = Integer32
_LostPackets_Object = MibTableColumn
lostPackets = _LostPackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 6),
    _LostPackets_Type()
)
lostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lostPackets.setStatus("current")
_NumTxPack_Type = Integer32
_NumTxPack_Object = MibTableColumn
numTxPack = _NumTxPack_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 7),
    _NumTxPack_Type()
)
numTxPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numTxPack.setStatus("current")
_NumTxOct_Type = Integer32
_NumTxOct_Object = MibTableColumn
numTxOct = _NumTxOct_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 8),
    _NumTxOct_Type()
)
numTxOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numTxOct.setStatus("current")
_NumRxPack_Type = Integer32
_NumRxPack_Object = MibTableColumn
numRxPack = _NumRxPack_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 9),
    _NumRxPack_Type()
)
numRxPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numRxPack.setStatus("current")
_NumRxOct_Type = Integer32
_NumRxOct_Object = MibTableColumn
numRxOct = _NumRxOct_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 23, 1, 10),
    _NumRxOct_Type()
)
numRxOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numRxOct.setStatus("current")
_FxsUpdateFw_Type = DisplayString
_FxsUpdateFw_Object = MibScalar
fxsUpdateFw = _FxsUpdateFw_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 25),
    _FxsUpdateFw_Type()
)
fxsUpdateFw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsUpdateFw.setStatus("current")
_FxsProfiles_ObjectIdentity = ObjectIdentity
fxsProfiles = _FxsProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30)
)
_ProfilesSip_ObjectIdentity = ObjectIdentity
profilesSip = _ProfilesSip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1)
)
_ProfilesSipCommon_ObjectIdentity = ObjectIdentity
profilesSipCommon = _ProfilesSipCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1)
)
_SipCommonEnablesip_Type = TruthValue
_SipCommonEnablesip_Object = MibScalar
sipCommonEnablesip = _SipCommonEnablesip_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 1),
    _SipCommonEnablesip_Type()
)
sipCommonEnablesip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonEnablesip.setStatus("current")
_SipCommonShortmode_Type = TruthValue
_SipCommonShortmode_Object = MibScalar
sipCommonShortmode = _SipCommonShortmode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 2),
    _SipCommonShortmode_Type()
)
sipCommonShortmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonShortmode.setStatus("current")
_SipCommonTransport_Type = TypeTransport
_SipCommonTransport_Object = MibScalar
sipCommonTransport = _SipCommonTransport_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 3),
    _SipCommonTransport_Type()
)
sipCommonTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonTransport.setStatus("current")


class _SipCommonSipMtu_Type(Integer32):
    """Custom type sipCommonSipMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1300, 1450),
    )


_SipCommonSipMtu_Type.__name__ = "Integer32"
_SipCommonSipMtu_Object = MibScalar
sipCommonSipMtu = _SipCommonSipMtu_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 4),
    _SipCommonSipMtu_Type()
)
sipCommonSipMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonSipMtu.setStatus("current")


class _SipCommonInviteTotalT_Type(Integer32):
    """Custom type sipCommonInviteTotalT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 39000),
    )


_SipCommonInviteTotalT_Type.__name__ = "Integer32"
_SipCommonInviteTotalT_Object = MibScalar
sipCommonInviteTotalT = _SipCommonInviteTotalT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 5),
    _SipCommonInviteTotalT_Type()
)
sipCommonInviteTotalT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonInviteTotalT.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonInviteTotalT.setUnits("ms")


class _SipCommonInviteInitT_Type(Integer32):
    """Custom type sipCommonInviteInitT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_SipCommonInviteInitT_Type.__name__ = "Integer32"
_SipCommonInviteInitT_Object = MibScalar
sipCommonInviteInitT = _SipCommonInviteInitT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 6),
    _SipCommonInviteInitT_Type()
)
sipCommonInviteInitT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonInviteInitT.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonInviteInitT.setUnits("ms")


class _SipCommonPortRegistrationDelay_Type(Integer32):
    """Custom type sipCommonPortRegistrationDelay based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_SipCommonPortRegistrationDelay_Type.__name__ = "Integer32"
_SipCommonPortRegistrationDelay_Object = MibScalar
sipCommonPortRegistrationDelay = _SipCommonPortRegistrationDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 7),
    _SipCommonPortRegistrationDelay_Type()
)
sipCommonPortRegistrationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCommonPortRegistrationDelay.setStatus("current")
if mibBuilder.loadTexts:
    sipCommonPortRegistrationDelay.setUnits("ms")
_StunEnable_Type = TruthValue
_StunEnable_Object = MibScalar
stunEnable = _StunEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 8),
    _StunEnable_Type()
)
stunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunEnable.setStatus("current")
_StunServer_Type = DisplayString
_StunServer_Object = MibScalar
stunServer = _StunServer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 9),
    _StunServer_Type()
)
stunServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunServer.setStatus("current")


class _StunInterval_Type(Integer32):
    """Custom type stunInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1800),
    )


_StunInterval_Type.__name__ = "Integer32"
_StunInterval_Object = MibScalar
stunInterval = _StunInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 10),
    _StunInterval_Type()
)
stunInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stunInterval.setStatus("current")
_SipPublicIp_Type = DisplayString
_SipPublicIp_Object = MibScalar
sipPublicIp = _SipPublicIp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 1, 11),
    _SipPublicIp_Type()
)
sipPublicIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipPublicIp.setStatus("current")
_ProfilesSipMIBBoundary_Type = Integer32
_ProfilesSipMIBBoundary_Object = MibScalar
profilesSipMIBBoundary = _ProfilesSipMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 2),
    _ProfilesSipMIBBoundary_Type()
)
profilesSipMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profilesSipMIBBoundary.setStatus("current")
_ProfilesSipTable_Object = MibTable
profilesSipTable = _ProfilesSipTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3)
)
if mibBuilder.loadTexts:
    profilesSipTable.setStatus("current")
_ProfilesSipEntry_Object = MibTableRow
profilesSipEntry = _ProfilesSipEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1)
)
profilesSipEntry.setIndexNames(
    (0, "ELTEX-FXS72", "profileNumber"),
)
if mibBuilder.loadTexts:
    profilesSipEntry.setStatus("current")


class _ProfileNumber_Type(Integer32):
    """Custom type profileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ProfileNumber_Type.__name__ = "Integer32"
_ProfileNumber_Object = MibTableColumn
profileNumber = _ProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 1),
    _ProfileNumber_Type()
)
profileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profileNumber.setStatus("current")
_SipProfileObtimeout_Type = Integer32
_SipProfileObtimeout_Object = MibTableColumn
sipProfileObtimeout = _SipProfileObtimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 2),
    _SipProfileObtimeout_Type()
)
sipProfileObtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileObtimeout.setStatus("current")
_SipProfileMode_Type = ProxyMode
_SipProfileMode_Object = MibTableColumn
sipProfileMode = _SipProfileMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 3),
    _SipProfileMode_Type()
)
sipProfileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileMode.setStatus("current")
_SipProfileOptions_Type = OptionsHomeServerTest
_SipProfileOptions_Object = MibTableColumn
sipProfileOptions = _SipProfileOptions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 4),
    _SipProfileOptions_Type()
)
sipProfileOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileOptions.setStatus("current")
_SipProfileKeepalivet_Type = Integer32
_SipProfileKeepalivet_Object = MibTableColumn
sipProfileKeepalivet = _SipProfileKeepalivet_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 5),
    _SipProfileKeepalivet_Type()
)
sipProfileKeepalivet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileKeepalivet.setStatus("current")
_SipProfileDomainToReg_Type = TruthValue
_SipProfileDomainToReg_Object = MibTableColumn
sipProfileDomainToReg = _SipProfileDomainToReg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 6),
    _SipProfileDomainToReg_Type()
)
sipProfileDomainToReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileDomainToReg.setStatus("current")


class _SipProfileDomain_Type(DisplayString):
    """Custom type sipProfileDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileDomain_Type.__name__ = "DisplayString"
_SipProfileDomain_Object = MibTableColumn
sipProfileDomain = _SipProfileDomain_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 7),
    _SipProfileDomain_Type()
)
sipProfileDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileDomain.setStatus("current")
_SipProfileRegisterRetryInterval_Type = Integer32
_SipProfileRegisterRetryInterval_Object = MibTableColumn
sipProfileRegisterRetryInterval = _SipProfileRegisterRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 8),
    _SipProfileRegisterRetryInterval_Type()
)
sipProfileRegisterRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegisterRetryInterval.setStatus("current")
_SipProfileOutbound_Type = OutboundType
_SipProfileOutbound_Object = MibTableColumn
sipProfileOutbound = _SipProfileOutbound_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 9),
    _SipProfileOutbound_Type()
)
sipProfileOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileOutbound.setStatus("current")
_SipProfileInboundProxy_Type = TruthValue
_SipProfileInboundProxy_Object = MibTableColumn
sipProfileInboundProxy = _SipProfileInboundProxy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 10),
    _SipProfileInboundProxy_Type()
)
sipProfileInboundProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileInboundProxy.setStatus("current")
_SipProfileExpires_Type = Integer32
_SipProfileExpires_Object = MibTableColumn
sipProfileExpires = _SipProfileExpires_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 11),
    _SipProfileExpires_Type()
)
sipProfileExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileExpires.setStatus("current")
_SipProfileAuthentication_Type = AuthenticationType
_SipProfileAuthentication_Object = MibTableColumn
sipProfileAuthentication = _SipProfileAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 12),
    _SipProfileAuthentication_Type()
)
sipProfileAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileAuthentication.setStatus("current")
_SipProfileUsername_Type = DisplayString
_SipProfileUsername_Object = MibTableColumn
sipProfileUsername = _SipProfileUsername_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 13),
    _SipProfileUsername_Type()
)
sipProfileUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileUsername.setStatus("current")
_SipProfilePassword_Type = DisplayString
_SipProfilePassword_Object = MibTableColumn
sipProfilePassword = _SipProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 14),
    _SipProfilePassword_Type()
)
sipProfilePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfilePassword.setStatus("current")


class _SipProfileProxy0_Type(DisplayString):
    """Custom type sipProfileProxy0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileProxy0_Type.__name__ = "DisplayString"
_SipProfileProxy0_Object = MibTableColumn
sipProfileProxy0 = _SipProfileProxy0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 15),
    _SipProfileProxy0_Type()
)
sipProfileProxy0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileProxy0.setStatus("current")


class _SipProfileRegrar0_Type(DisplayString):
    """Custom type sipProfileRegrar0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileRegrar0_Type.__name__ = "DisplayString"
_SipProfileRegrar0_Object = MibTableColumn
sipProfileRegrar0 = _SipProfileRegrar0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 16),
    _SipProfileRegrar0_Type()
)
sipProfileRegrar0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegrar0.setStatus("current")
_SipProfileRegistration0_Type = TruthValue
_SipProfileRegistration0_Object = MibTableColumn
sipProfileRegistration0 = _SipProfileRegistration0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 17),
    _SipProfileRegistration0_Type()
)
sipProfileRegistration0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegistration0.setStatus("current")


class _SipProfileProxy1_Type(DisplayString):
    """Custom type sipProfileProxy1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileProxy1_Type.__name__ = "DisplayString"
_SipProfileProxy1_Object = MibTableColumn
sipProfileProxy1 = _SipProfileProxy1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 18),
    _SipProfileProxy1_Type()
)
sipProfileProxy1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileProxy1.setStatus("current")


class _SipProfileRegrar1_Type(DisplayString):
    """Custom type sipProfileRegrar1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileRegrar1_Type.__name__ = "DisplayString"
_SipProfileRegrar1_Object = MibTableColumn
sipProfileRegrar1 = _SipProfileRegrar1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 19),
    _SipProfileRegrar1_Type()
)
sipProfileRegrar1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegrar1.setStatus("current")


class _SipProfileProxy2_Type(DisplayString):
    """Custom type sipProfileProxy2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileProxy2_Type.__name__ = "DisplayString"
_SipProfileProxy2_Object = MibTableColumn
sipProfileProxy2 = _SipProfileProxy2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 20),
    _SipProfileProxy2_Type()
)
sipProfileProxy2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileProxy2.setStatus("current")


class _SipProfileRegrar2_Type(DisplayString):
    """Custom type sipProfileRegrar2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileRegrar2_Type.__name__ = "DisplayString"
_SipProfileRegrar2_Object = MibTableColumn
sipProfileRegrar2 = _SipProfileRegrar2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 21),
    _SipProfileRegrar2_Type()
)
sipProfileRegrar2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegrar2.setStatus("current")


class _SipProfileProxy3_Type(DisplayString):
    """Custom type sipProfileProxy3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileProxy3_Type.__name__ = "DisplayString"
_SipProfileProxy3_Object = MibTableColumn
sipProfileProxy3 = _SipProfileProxy3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 22),
    _SipProfileProxy3_Type()
)
sipProfileProxy3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileProxy3.setStatus("current")


class _SipProfileRegrar3_Type(DisplayString):
    """Custom type sipProfileRegrar3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileRegrar3_Type.__name__ = "DisplayString"
_SipProfileRegrar3_Object = MibTableColumn
sipProfileRegrar3 = _SipProfileRegrar3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 23),
    _SipProfileRegrar3_Type()
)
sipProfileRegrar3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegrar3.setStatus("current")


class _SipProfileProxy4_Type(DisplayString):
    """Custom type sipProfileProxy4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileProxy4_Type.__name__ = "DisplayString"
_SipProfileProxy4_Object = MibTableColumn
sipProfileProxy4 = _SipProfileProxy4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 24),
    _SipProfileProxy4_Type()
)
sipProfileProxy4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileProxy4.setStatus("current")


class _SipProfileRegrar4_Type(DisplayString):
    """Custom type sipProfileRegrar4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SipProfileRegrar4_Type.__name__ = "DisplayString"
_SipProfileRegrar4_Object = MibTableColumn
sipProfileRegrar4 = _SipProfileRegrar4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 25),
    _SipProfileRegrar4_Type()
)
sipProfileRegrar4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegrar4.setStatus("current")
_SipProfileDtmfmime_Type = DTMFMIMEType
_SipProfileDtmfmime_Object = MibTableColumn
sipProfileDtmfmime = _SipProfileDtmfmime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 26),
    _SipProfileDtmfmime_Type()
)
sipProfileDtmfmime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileDtmfmime.setStatus("current")
_SipProfileHfmime_Type = HookFlashMIMEType
_SipProfileHfmime_Object = MibTableColumn
sipProfileHfmime = _SipProfileHfmime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 27),
    _SipProfileHfmime_Type()
)
sipProfileHfmime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileHfmime.setStatus("current")
_SipProfileCtWithReplaces_Type = TruthValue
_SipProfileCtWithReplaces_Object = MibTableColumn
sipProfileCtWithReplaces = _SipProfileCtWithReplaces_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 28),
    _SipProfileCtWithReplaces_Type()
)
sipProfileCtWithReplaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileCtWithReplaces.setStatus("current")
_SipProfile100Rel_Type = Type100rel
_SipProfile100Rel_Object = MibTableColumn
sipProfile100Rel = _SipProfile100Rel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 32),
    _SipProfile100Rel_Type()
)
sipProfile100Rel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfile100Rel.setStatus("current")
_SipProfileUserPhone_Type = TruthValue
_SipProfileUserPhone_Object = MibTableColumn
sipProfileUserPhone = _SipProfileUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 33),
    _SipProfileUserPhone_Type()
)
sipProfileUserPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileUserPhone.setStatus("current")
_SipProfileUriEscapeHash_Type = TruthValue
_SipProfileUriEscapeHash_Object = MibTableColumn
sipProfileUriEscapeHash = _SipProfileUriEscapeHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 34),
    _SipProfileUriEscapeHash_Type()
)
sipProfileUriEscapeHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileUriEscapeHash.setStatus("current")
_SipProfileCwRingback_Type = CwRingbackRingbackAtCallwaiting
_SipProfileCwRingback_Object = MibTableColumn
sipProfileCwRingback = _SipProfileCwRingback_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 37),
    _SipProfileCwRingback_Type()
)
sipProfileCwRingback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileCwRingback.setStatus("current")
_SipProfileRingbackSdp_Type = RemoteRingback
_SipProfileRingbackSdp_Object = MibTableColumn
sipProfileRingbackSdp = _SipProfileRingbackSdp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 38),
    _SipProfileRingbackSdp_Type()
)
sipProfileRingbackSdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRingbackSdp.setStatus("current")
_SipProfileRingback_Type = TruthValue
_SipProfileRingback_Object = MibTableColumn
sipProfileRingback = _SipProfileRingback_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 39),
    _SipProfileRingback_Type()
)
sipProfileRingback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRingback.setStatus("current")
_SipProfileRegistration1_Type = TruthValue
_SipProfileRegistration1_Object = MibTableColumn
sipProfileRegistration1 = _SipProfileRegistration1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 40),
    _SipProfileRegistration1_Type()
)
sipProfileRegistration1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegistration1.setStatus("current")
_SipProfileRegistration2_Type = TruthValue
_SipProfileRegistration2_Object = MibTableColumn
sipProfileRegistration2 = _SipProfileRegistration2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 41),
    _SipProfileRegistration2_Type()
)
sipProfileRegistration2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegistration2.setStatus("current")
_SipProfileRegistration3_Type = TruthValue
_SipProfileRegistration3_Object = MibTableColumn
sipProfileRegistration3 = _SipProfileRegistration3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 42),
    _SipProfileRegistration3_Type()
)
sipProfileRegistration3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegistration3.setStatus("current")
_SipProfileRegistration4_Type = TruthValue
_SipProfileRegistration4_Object = MibTableColumn
sipProfileRegistration4 = _SipProfileRegistration4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 43),
    _SipProfileRegistration4_Type()
)
sipProfileRegistration4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRegistration4.setStatus("current")
_SipProfilePRTPstat_Type = TruthValue
_SipProfilePRTPstat_Object = MibTableColumn
sipProfilePRTPstat = _SipProfilePRTPstat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 44),
    _SipProfilePRTPstat_Type()
)
sipProfilePRTPstat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfilePRTPstat.setStatus("current")
_SipProfileRowStatus_Type = RowStatus
_SipProfileRowStatus_Object = MibTableColumn
sipProfileRowStatus = _SipProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 45),
    _SipProfileRowStatus_Type()
)
sipProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sipProfileRowStatus.setStatus("current")
_SipProfileEnableTimer_Type = TruthValue
_SipProfileEnableTimer_Object = MibTableColumn
sipProfileEnableTimer = _SipProfileEnableTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 46),
    _SipProfileEnableTimer_Type()
)
sipProfileEnableTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileEnableTimer.setStatus("current")
_SipProfileMinSE_Type = Integer32
_SipProfileMinSE_Object = MibTableColumn
sipProfileMinSE = _SipProfileMinSE_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 47),
    _SipProfileMinSE_Type()
)
sipProfileMinSE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileMinSE.setStatus("current")
_SipProfileSessionExpires_Type = Integer32
_SipProfileSessionExpires_Object = MibTableColumn
sipProfileSessionExpires = _SipProfileSessionExpires_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 48),
    _SipProfileSessionExpires_Type()
)
sipProfileSessionExpires.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileSessionExpires.setStatus("current")
_SipProfileRemoveInactiveMedia_Type = TruthValue
_SipProfileRemoveInactiveMedia_Object = MibTableColumn
sipProfileRemoveInactiveMedia = _SipProfileRemoveInactiveMedia_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 49),
    _SipProfileRemoveInactiveMedia_Type()
)
sipProfileRemoveInactiveMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileRemoveInactiveMedia.setStatus("current")
_SipProfileKeepAliveInterval_Type = Integer32
_SipProfileKeepAliveInterval_Object = MibTableColumn
sipProfileKeepAliveInterval = _SipProfileKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 50),
    _SipProfileKeepAliveInterval_Type()
)
sipProfileKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileKeepAliveInterval.setStatus("current")
_SipProfileKeepAliveMode_Type = KeepAliveMode
_SipProfileKeepAliveMode_Object = MibTableColumn
sipProfileKeepAliveMode = _SipProfileKeepAliveMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 51),
    _SipProfileKeepAliveMode_Type()
)
sipProfileKeepAliveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileKeepAliveMode.setStatus("current")
_SipProfileConferenceMode_Type = ConferenceMode
_SipProfileConferenceMode_Object = MibTableColumn
sipProfileConferenceMode = _SipProfileConferenceMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 52),
    _SipProfileConferenceMode_Type()
)
sipProfileConferenceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileConferenceMode.setStatus("current")
_SipProfileConferenceServer_Type = DisplayString
_SipProfileConferenceServer_Object = MibTableColumn
sipProfileConferenceServer = _SipProfileConferenceServer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 53),
    _SipProfileConferenceServer_Type()
)
sipProfileConferenceServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileConferenceServer.setStatus("current")
_SipProfileEnableIMS_Type = IMSMode
_SipProfileEnableIMS_Object = MibTableColumn
sipProfileEnableIMS = _SipProfileEnableIMS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 54),
    _SipProfileEnableIMS_Type()
)
sipProfileEnableIMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileEnableIMS.setStatus("current")
_SipProfileXCAPNameForThreePartyConference_Type = DisplayString
_SipProfileXCAPNameForThreePartyConference_Object = MibTableColumn
sipProfileXCAPNameForThreePartyConference = _SipProfileXCAPNameForThreePartyConference_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 55),
    _SipProfileXCAPNameForThreePartyConference_Type()
)
sipProfileXCAPNameForThreePartyConference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileXCAPNameForThreePartyConference.setStatus("current")
_SipProfileXCAPNameForHotline_Type = DisplayString
_SipProfileXCAPNameForHotline_Object = MibTableColumn
sipProfileXCAPNameForHotline = _SipProfileXCAPNameForHotline_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 56),
    _SipProfileXCAPNameForHotline_Type()
)
sipProfileXCAPNameForHotline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileXCAPNameForHotline.setStatus("current")
_SipProfileXCAPNameForCallWaiting_Type = DisplayString
_SipProfileXCAPNameForCallWaiting_Object = MibTableColumn
sipProfileXCAPNameForCallWaiting = _SipProfileXCAPNameForCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 57),
    _SipProfileXCAPNameForCallWaiting_Type()
)
sipProfileXCAPNameForCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileXCAPNameForCallWaiting.setStatus("current")
_SipProfileXCAPNameForCallHold_Type = DisplayString
_SipProfileXCAPNameForCallHold_Object = MibTableColumn
sipProfileXCAPNameForCallHold = _SipProfileXCAPNameForCallHold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 58),
    _SipProfileXCAPNameForCallHold_Type()
)
sipProfileXCAPNameForCallHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileXCAPNameForCallHold.setStatus("current")
_SipProfileXCAPNameForExplicitCallTransfer_Type = DisplayString
_SipProfileXCAPNameForExplicitCallTransfer_Object = MibTableColumn
sipProfileXCAPNameForExplicitCallTransfer = _SipProfileXCAPNameForExplicitCallTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 59),
    _SipProfileXCAPNameForExplicitCallTransfer_Type()
)
sipProfileXCAPNameForExplicitCallTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileXCAPNameForExplicitCallTransfer.setStatus("current")
_SipProfileUseAlertInfo_Type = TruthValue
_SipProfileUseAlertInfo_Object = MibTableColumn
sipProfileUseAlertInfo = _SipProfileUseAlertInfo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 60),
    _SipProfileUseAlertInfo_Type()
)
sipProfileUseAlertInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileUseAlertInfo.setStatus("current")
_SipProfileFullRuriCompliance_Type = TruthValue
_SipProfileFullRuriCompliance_Object = MibTableColumn
sipProfileFullRuriCompliance = _SipProfileFullRuriCompliance_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 61),
    _SipProfileFullRuriCompliance_Type()
)
sipProfileFullRuriCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileFullRuriCompliance.setStatus("current")
_SipProfileChangeover_Type = SipProfileChangeoverType
_SipProfileChangeover_Object = MibTableColumn
sipProfileChangeover = _SipProfileChangeover_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 3, 1, 62),
    _SipProfileChangeover_Type()
)
sipProfileChangeover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipProfileChangeover.setStatus("current")
_ProfilesSipAlertInfoMIBBoundary_Type = Integer32
_ProfilesSipAlertInfoMIBBoundary_Object = MibScalar
profilesSipAlertInfoMIBBoundary = _ProfilesSipAlertInfoMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 4),
    _ProfilesSipAlertInfoMIBBoundary_Type()
)
profilesSipAlertInfoMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profilesSipAlertInfoMIBBoundary.setStatus("current")
_ProfilesSipAlertInfoTable_Object = MibTable
profilesSipAlertInfoTable = _ProfilesSipAlertInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 5)
)
if mibBuilder.loadTexts:
    profilesSipAlertInfoTable.setStatus("current")
_ProfilesSipAlertInfoEntry_Object = MibTableRow
profilesSipAlertInfoEntry = _ProfilesSipAlertInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 5, 1)
)
profilesSipAlertInfoEntry.setIndexNames(
    (0, "ELTEX-FXS72", "profileNumber"),
    (0, "ELTEX-FXS72", "cadenceNumber"),
)
if mibBuilder.loadTexts:
    profilesSipAlertInfoEntry.setStatus("current")


class _CadenceNumber_Type(Integer32):
    """Custom type cadenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CadenceNumber_Type.__name__ = "Integer32"
_CadenceNumber_Object = MibTableColumn
cadenceNumber = _CadenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 5, 1, 1),
    _CadenceNumber_Type()
)
cadenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadenceNumber.setStatus("current")
_CadenceName_Type = DisplayString
_CadenceName_Object = MibTableColumn
cadenceName = _CadenceName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 5, 1, 2),
    _CadenceName_Type()
)
cadenceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadenceName.setStatus("current")
_CadenceRingRule_Type = DisplayString
_CadenceRingRule_Object = MibTableColumn
cadenceRingRule = _CadenceRingRule_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 5, 1, 3),
    _CadenceRingRule_Type()
)
cadenceRingRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadenceRingRule.setStatus("current")
_CadenceRowStatus_Type = RowStatus
_CadenceRowStatus_Object = MibTableColumn
cadenceRowStatus = _CadenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 1, 5, 1, 4),
    _CadenceRowStatus_Type()
)
cadenceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadenceRowStatus.setStatus("current")
_ProfilesPortsMIBBoundary_Type = Integer32
_ProfilesPortsMIBBoundary_Object = MibScalar
profilesPortsMIBBoundary = _ProfilesPortsMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 2),
    _ProfilesPortsMIBBoundary_Type()
)
profilesPortsMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profilesPortsMIBBoundary.setStatus("current")
_ProfilesPorts_ObjectIdentity = ObjectIdentity
profilesPorts = _ProfilesPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3)
)
_ProfilesPortsTable_Object = MibTable
profilesPortsTable = _ProfilesPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1)
)
if mibBuilder.loadTexts:
    profilesPortsTable.setStatus("current")
_ProfilesPortsEntry_Object = MibTableRow
profilesPortsEntry = _ProfilesPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1)
)
profilesPortsEntry.setIndexNames(
    (0, "ELTEX-FXS72", "profileNumber"),
)
if mibBuilder.loadTexts:
    profilesPortsEntry.setStatus("current")
_ProfilePortsPlaymoh_Type = TruthValue
_ProfilePortsPlaymoh_Object = MibTableColumn
profilePortsPlaymoh = _ProfilePortsPlaymoh_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 1),
    _ProfilePortsPlaymoh_Type()
)
profilePortsPlaymoh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsPlaymoh.setStatus("current")
_ProfilePortsAON_Type = FxsAON
_ProfilePortsAON_Object = MibTableColumn
profilePortsAON = _ProfilePortsAON_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 2),
    _ProfilePortsAON_Type()
)
profilePortsAON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsAON.setStatus("current")
_ProfilePortsAONHideDate_Type = TruthValue
_ProfilePortsAONHideDate_Object = MibTableColumn
profilePortsAONHideDate = _ProfilePortsAONHideDate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 3),
    _ProfilePortsAONHideDate_Type()
)
profilePortsAONHideDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsAONHideDate.setStatus("current")
_ProfilePortsAONHideName_Type = TruthValue
_ProfilePortsAONHideName_Object = MibTableColumn
profilePortsAONHideName = _ProfilePortsAONHideName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 4),
    _ProfilePortsAONHideName_Type()
)
profilePortsAONHideName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsAONHideName.setStatus("current")
_ProfilePortsTaxophone_Type = FxsTaxophoneType
_ProfilePortsTaxophone_Object = MibTableColumn
profilePortsTaxophone = _ProfilePortsTaxophone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 5),
    _ProfilePortsTaxophone_Type()
)
profilePortsTaxophone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsTaxophone.setStatus("current")
_ProfilePortsMinFlashtime_Type = Integer32
_ProfilePortsMinFlashtime_Object = MibTableColumn
profilePortsMinFlashtime = _ProfilePortsMinFlashtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 6),
    _ProfilePortsMinFlashtime_Type()
)
profilePortsMinFlashtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsMinFlashtime.setStatus("current")
_ProfilePortsMaxFlashtime_Type = Integer32
_ProfilePortsMaxFlashtime_Object = MibTableColumn
profilePortsMaxFlashtime = _ProfilePortsMaxFlashtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 7),
    _ProfilePortsMaxFlashtime_Type()
)
profilePortsMaxFlashtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsMaxFlashtime.setStatus("current")
_ProfilePortsGainr_Type = Integer32
_ProfilePortsGainr_Object = MibTableColumn
profilePortsGainr = _ProfilePortsGainr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 8),
    _ProfilePortsGainr_Type()
)
profilePortsGainr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsGainr.setStatus("current")
_ProfilePortsGaint_Type = Integer32
_ProfilePortsGaint_Object = MibTableColumn
profilePortsGaint = _ProfilePortsGaint_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 9),
    _ProfilePortsGaint_Type()
)
profilePortsGaint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsGaint.setStatus("current")
_ProfilePortsCategory_Type = Integer32
_ProfilePortsCategory_Object = MibTableColumn
profilePortsCategory = _ProfilePortsCategory_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 10),
    _ProfilePortsCategory_Type()
)
profilePortsCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsCategory.setStatus("current")
_ProfilePortsCallTransfer_Type = FxsProcessFlashType
_ProfilePortsCallTransfer_Object = MibTableColumn
profilePortsCallTransfer = _ProfilePortsCallTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 11),
    _ProfilePortsCallTransfer_Type()
)
profilePortsCallTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsCallTransfer.setStatus("obsolete")
_ProfilePortsCallWaiting_Type = TruthValue
_ProfilePortsCallWaiting_Object = MibTableColumn
profilePortsCallWaiting = _ProfilePortsCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 12),
    _ProfilePortsCallWaiting_Type()
)
profilePortsCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsCallWaiting.setStatus("obsolete")
_ProfilePortsCfgPriOverCw_Type = TruthValue
_ProfilePortsCfgPriOverCw_Object = MibTableColumn
profilePortsCfgPriOverCw = _ProfilePortsCfgPriOverCw_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 13),
    _ProfilePortsCfgPriOverCw_Type()
)
profilePortsCfgPriOverCw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsCfgPriOverCw.setStatus("current")
_ProfilePortsFxoFlashTime_Type = Integer32
_ProfilePortsFxoFlashTime_Object = MibTableColumn
profilePortsFxoFlashTime = _ProfilePortsFxoFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 14),
    _ProfilePortsFxoFlashTime_Type()
)
profilePortsFxoFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsFxoFlashTime.setStatus("current")
_ProfilePortsFxoDelTdm_Type = Integer32
_ProfilePortsFxoDelTdm_Object = MibTableColumn
profilePortsFxoDelTdm = _ProfilePortsFxoDelTdm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 15),
    _ProfilePortsFxoDelTdm_Type()
)
profilePortsFxoDelTdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsFxoDelTdm.setStatus("current")
_ProfilePortsFxoRingtdm_Type = Integer32
_ProfilePortsFxoRingtdm_Object = MibTableColumn
profilePortsFxoRingtdm = _ProfilePortsFxoRingtdm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 16),
    _ProfilePortsFxoRingtdm_Type()
)
profilePortsFxoRingtdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsFxoRingtdm.setStatus("current")
_ProfilePortsPstnNumberprefix_Type = DisplayString
_ProfilePortsPstnNumberprefix_Object = MibTableColumn
profilePortsPstnNumberprefix = _ProfilePortsPstnNumberprefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 17),
    _ProfilePortsPstnNumberprefix_Type()
)
profilePortsPstnNumberprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsPstnNumberprefix.setStatus("current")
_ProfilePortsPstnNameprefix_Type = DisplayString
_ProfilePortsPstnNameprefix_Object = MibTableColumn
profilePortsPstnNameprefix = _ProfilePortsPstnNameprefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 18),
    _ProfilePortsPstnNameprefix_Type()
)
profilePortsPstnNameprefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsPstnNameprefix.setStatus("current")
_ProfilePortsUsePstnCid_Type = TruthValue
_ProfilePortsUsePstnCid_Object = MibTableColumn
profilePortsUsePstnCid = _ProfilePortsUsePstnCid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 19),
    _ProfilePortsUsePstnCid_Type()
)
profilePortsUsePstnCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsUsePstnCid.setStatus("current")
_ProfilePortsEnableCpc_Type = TruthValue
_ProfilePortsEnableCpc_Object = MibTableColumn
profilePortsEnableCpc = _ProfilePortsEnableCpc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 20),
    _ProfilePortsEnableCpc_Type()
)
profilePortsEnableCpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsEnableCpc.setStatus("current")
_ProfilePortsCpcTime_Type = TruthValue
_ProfilePortsCpcTime_Object = MibTableColumn
profilePortsCpcTime = _ProfilePortsCpcTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 21),
    _ProfilePortsCpcTime_Type()
)
profilePortsCpcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsCpcTime.setStatus("current")
_ProfilePortsDontDetectDT_Type = TruthValue
_ProfilePortsDontDetectDT_Object = MibTableColumn
profilePortsDontDetectDT = _ProfilePortsDontDetectDT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 22),
    _ProfilePortsDontDetectDT_Type()
)
profilePortsDontDetectDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDontDetectDT.setStatus("current")
_ProfilePortsDelayDialingTimeout_Type = Integer32
_ProfilePortsDelayDialingTimeout_Object = MibTableColumn
profilePortsDelayDialingTimeout = _ProfilePortsDelayDialingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 23),
    _ProfilePortsDelayDialingTimeout_Type()
)
profilePortsDelayDialingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDelayDialingTimeout.setStatus("current")
_ProfilePortsDialing_Type = FxoDialingType
_ProfilePortsDialing_Object = MibTableColumn
profilePortsDialing = _ProfilePortsDialing_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 24),
    _ProfilePortsDialing_Type()
)
profilePortsDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDialing.setStatus("current")
_ProfilePortsTransmitNumber_Type = TruthValue
_ProfilePortsTransmitNumber_Object = MibTableColumn
profilePortsTransmitNumber = _ProfilePortsTransmitNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 25),
    _ProfilePortsTransmitNumber_Type()
)
profilePortsTransmitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsTransmitNumber.setStatus("current")
_ProfilePortsDontTransmitPrefix_Type = TruthValue
_ProfilePortsDontTransmitPrefix_Object = MibTableColumn
profilePortsDontTransmitPrefix = _ProfilePortsDontTransmitPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 26),
    _ProfilePortsDontTransmitPrefix_Type()
)
profilePortsDontTransmitPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDontTransmitPrefix.setStatus("current")
_ProfilePortsRowStatus_Type = RowStatus
_ProfilePortsRowStatus_Object = MibTableColumn
profilePortsRowStatus = _ProfilePortsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 27),
    _ProfilePortsRowStatus_Type()
)
profilePortsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profilePortsRowStatus.setStatus("current")
_ProfilePortsDialToneDetectionParameters_Type = FxsToneParametrs
_ProfilePortsDialToneDetectionParameters_Object = MibTableColumn
profilePortsDialToneDetectionParameters = _ProfilePortsDialToneDetectionParameters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 28),
    _ProfilePortsDialToneDetectionParameters_Type()
)
profilePortsDialToneDetectionParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDialToneDetectionParameters.setStatus("current")
_ProfilePortsRingBackToneDetectionParameters_Type = FxsToneParametrs
_ProfilePortsRingBackToneDetectionParameters_Object = MibTableColumn
profilePortsRingBackToneDetectionParameters = _ProfilePortsRingBackToneDetectionParameters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 29),
    _ProfilePortsRingBackToneDetectionParameters_Type()
)
profilePortsRingBackToneDetectionParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsRingBackToneDetectionParameters.setStatus("current")
_ProfilePortsBusyToneDetectionParameters_Type = FxsToneParametrs
_ProfilePortsBusyToneDetectionParameters_Object = MibTableColumn
profilePortsBusyToneDetectionParameters = _ProfilePortsBusyToneDetectionParameters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 30),
    _ProfilePortsBusyToneDetectionParameters_Type()
)
profilePortsBusyToneDetectionParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsBusyToneDetectionParameters.setStatus("current")
_ProfilePortsDtDetectTime_Type = Integer32
_ProfilePortsDtDetectTime_Object = MibTableColumn
profilePortsDtDetectTime = _ProfilePortsDtDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 31),
    _ProfilePortsDtDetectTime_Type()
)
profilePortsDtDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDtDetectTime.setStatus("current")
_ProfilePortsDecadePulseTime_Type = Integer32
_ProfilePortsDecadePulseTime_Object = MibTableColumn
profilePortsDecadePulseTime = _ProfilePortsDecadePulseTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 32),
    _ProfilePortsDecadePulseTime_Type()
)
profilePortsDecadePulseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDecadePulseTime.setStatus("current")
_ProfilePortsDecadePauseTime_Type = Integer32
_ProfilePortsDecadePauseTime_Object = MibTableColumn
profilePortsDecadePauseTime = _ProfilePortsDecadePauseTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 33),
    _ProfilePortsDecadePauseTime_Type()
)
profilePortsDecadePauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDecadePauseTime.setStatus("current")
_ProfilePortsFxoCallBusy_Type = TruthValue
_ProfilePortsFxoCallBusy_Object = MibTableColumn
profilePortsFxoCallBusy = _ProfilePortsFxoCallBusy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 34),
    _ProfilePortsFxoCallBusy_Type()
)
profilePortsFxoCallBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsFxoCallBusy.setStatus("current")
_ProfilePortsCpcRus_Type = Integer32
_ProfilePortsCpcRus_Object = MibTableColumn
profilePortsCpcRus = _ProfilePortsCpcRus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 35),
    _ProfilePortsCpcRus_Type()
)
profilePortsCpcRus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsCpcRus.setStatus("current")
_ProfilePortsReversalPolarityAction_Type = ReversalPolarityAction
_ProfilePortsReversalPolarityAction_Object = MibTableColumn
profilePortsReversalPolarityAction = _ProfilePortsReversalPolarityAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 36),
    _ProfilePortsReversalPolarityAction_Type()
)
profilePortsReversalPolarityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsReversalPolarityAction.setStatus("obsolete")
_ProfilePortsPstnActivity_Type = PstnActivityType
_ProfilePortsPstnActivity_Object = MibTableColumn
profilePortsPstnActivity = _ProfilePortsPstnActivity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 37),
    _ProfilePortsPstnActivity_Type()
)
profilePortsPstnActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsPstnActivity.setStatus("current")


class _ProfilePortsPstnRbDetectTimeout_Type(Integer32):
    """Custom type profilePortsPstnRbDetectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ProfilePortsPstnRbDetectTimeout_Type.__name__ = "Integer32"
_ProfilePortsPstnRbDetectTimeout_Object = MibTableColumn
profilePortsPstnRbDetectTimeout = _ProfilePortsPstnRbDetectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 38),
    _ProfilePortsPstnRbDetectTimeout_Type()
)
profilePortsPstnRbDetectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsPstnRbDetectTimeout.setStatus("current")
if mibBuilder.loadTexts:
    profilePortsPstnRbDetectTimeout.setUnits("sec")
_ProfilePortsDetectFxoLinePresence_Type = TruthValue
_ProfilePortsDetectFxoLinePresence_Object = MibTableColumn
profilePortsDetectFxoLinePresence = _ProfilePortsDetectFxoLinePresence_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 39),
    _ProfilePortsDetectFxoLinePresence_Type()
)
profilePortsDetectFxoLinePresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsDetectFxoLinePresence.setStatus("current")
_ProfilePortsBlockFxoLineInOutgoingDirection_Type = TruthValue
_ProfilePortsBlockFxoLineInOutgoingDirection_Object = MibTableColumn
profilePortsBlockFxoLineInOutgoingDirection = _ProfilePortsBlockFxoLineInOutgoingDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 40),
    _ProfilePortsBlockFxoLineInOutgoingDirection_Type()
)
profilePortsBlockFxoLineInOutgoingDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsBlockFxoLineInOutgoingDirection.setStatus("current")
_ProfilePortsStopDial_Type = TruthValue
_ProfilePortsStopDial_Object = MibTableColumn
profilePortsStopDial = _ProfilePortsStopDial_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 41),
    _ProfilePortsStopDial_Type()
)
profilePortsStopDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsStopDial.setStatus("current")
_ProfilePortsFxoMinLevelDetect_Type = Integer32
_ProfilePortsFxoMinLevelDetect_Object = MibTableColumn
profilePortsFxoMinLevelDetect = _ProfilePortsFxoMinLevelDetect_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 42),
    _ProfilePortsFxoMinLevelDetect_Type()
)
profilePortsFxoMinLevelDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsFxoMinLevelDetect.setStatus("current")
_ProfilePortsModifier_Type = Integer32
_ProfilePortsModifier_Object = MibTableColumn
profilePortsModifier = _ProfilePortsModifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 3, 1, 1, 43),
    _ProfilePortsModifier_Type()
)
profilePortsModifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profilePortsModifier.setStatus("current")
_ProfilesDialPlansMIBBoundary_Type = Integer32
_ProfilesDialPlansMIBBoundary_Object = MibScalar
profilesDialPlansMIBBoundary = _ProfilesDialPlansMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 4),
    _ProfilesDialPlansMIBBoundary_Type()
)
profilesDialPlansMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profilesDialPlansMIBBoundary.setStatus("current")
_ProfilesDialPlans_ObjectIdentity = ObjectIdentity
profilesDialPlans = _ProfilesDialPlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5)
)
_ProfilesDialPlansTable_Object = MibTable
profilesDialPlansTable = _ProfilesDialPlansTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1)
)
if mibBuilder.loadTexts:
    profilesDialPlansTable.setStatus("current")
_ProfilesDialPlansEntry_Object = MibTableRow
profilesDialPlansEntry = _ProfilesDialPlansEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1)
)
profilesDialPlansEntry.setIndexNames(
    (0, "ELTEX-FXS72", "profileNumber"),
    (0, "ELTEX-FXS72", "profileDialPlanNumber"),
)
if mibBuilder.loadTexts:
    profilesDialPlansEntry.setStatus("current")
_ProfileDialPlanHost_Type = DisplayString
_ProfileDialPlanHost_Object = MibTableColumn
profileDialPlanHost = _ProfileDialPlanHost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 1),
    _ProfileDialPlanHost_Type()
)
profileDialPlanHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanHost.setStatus("current")
_ProfileDialPlanDigits_Type = DisplayString
_ProfileDialPlanDigits_Object = MibTableColumn
profileDialPlanDigits = _ProfileDialPlanDigits_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 2),
    _ProfileDialPlanDigits_Type()
)
profileDialPlanDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanDigits.setStatus("current")
_ProfileDialPlanTimeout_Type = Integer32
_ProfileDialPlanTimeout_Object = MibTableColumn
profileDialPlanTimeout = _ProfileDialPlanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 3),
    _ProfileDialPlanTimeout_Type()
)
profileDialPlanTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanTimeout.setStatus("current")
_ProfileDialPlanMinDigits_Type = Integer32
_ProfileDialPlanMinDigits_Object = MibTableColumn
profileDialPlanMinDigits = _ProfileDialPlanMinDigits_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 4),
    _ProfileDialPlanMinDigits_Type()
)
profileDialPlanMinDigits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanMinDigits.setStatus("current")
_ProfileDialPlanType_Type = FxsDialPlanType
_ProfileDialPlanType_Object = MibTableColumn
profileDialPlanType = _ProfileDialPlanType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 5),
    _ProfileDialPlanType_Type()
)
profileDialPlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanType.setStatus("current")
_ProfileDialPlanAccessMask_Type = DisplayString
_ProfileDialPlanAccessMask_Object = MibTableColumn
profileDialPlanAccessMask = _ProfileDialPlanAccessMask_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 6),
    _ProfileDialPlanAccessMask_Type()
)
profileDialPlanAccessMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanAccessMask.setStatus("current")
_ProfileDialPlanDialtone_Type = TruthValue
_ProfileDialPlanDialtone_Object = MibTableColumn
profileDialPlanDialtone = _ProfileDialPlanDialtone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 7),
    _ProfileDialPlanDialtone_Type()
)
profileDialPlanDialtone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanDialtone.setStatus("current")
_ProfileDialPlanModifier_Type = DisplayString
_ProfileDialPlanModifier_Object = MibTableColumn
profileDialPlanModifier = _ProfileDialPlanModifier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 8),
    _ProfileDialPlanModifier_Type()
)
profileDialPlanModifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanModifier.setStatus("current")
_ProfileDialPlanNature_Type = FxsDialPlanNatureType
_ProfileDialPlanNature_Object = MibTableColumn
profileDialPlanNature = _ProfileDialPlanNature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 9),
    _ProfileDialPlanNature_Type()
)
profileDialPlanNature.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanNature.setStatus("current")
_ProfileDialPlanDelnum_Type = Integer32
_ProfileDialPlanDelnum_Object = MibTableColumn
profileDialPlanDelnum = _ProfileDialPlanDelnum_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 10),
    _ProfileDialPlanDelnum_Type()
)
profileDialPlanDelnum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanDelnum.setStatus("current")
_ProfileDialPlanPtime_Type = Integer32
_ProfileDialPlanPtime_Object = MibTableColumn
profileDialPlanPtime = _ProfileDialPlanPtime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 11),
    _ProfileDialPlanPtime_Type()
)
profileDialPlanPtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialPlanPtime.setStatus("current")
_ProfileDialRowStatus_Type = RowStatus
_ProfileDialRowStatus_Object = MibTableColumn
profileDialRowStatus = _ProfileDialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 12),
    _ProfileDialRowStatus_Type()
)
profileDialRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileDialRowStatus.setStatus("current")


class _ProfileDialPlanNumber_Type(Integer32):
    """Custom type profileDialPlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ProfileDialPlanNumber_Type.__name__ = "Integer32"
_ProfileDialPlanNumber_Object = MibTableColumn
profileDialPlanNumber = _ProfileDialPlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 1, 1, 13),
    _ProfileDialPlanNumber_Type()
)
profileDialPlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    profileDialPlanNumber.setStatus("current")
_ProfilesRegExpDPTableMIBBoundary_Type = Integer32
_ProfilesRegExpDPTableMIBBoundary_Object = MibScalar
profilesRegExpDPTableMIBBoundary = _ProfilesRegExpDPTableMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 2),
    _ProfilesRegExpDPTableMIBBoundary_Type()
)
profilesRegExpDPTableMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    profilesRegExpDPTableMIBBoundary.setStatus("current")
_ProfilesRegExpDPTable_Object = MibTable
profilesRegExpDPTable = _ProfilesRegExpDPTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 3)
)
if mibBuilder.loadTexts:
    profilesRegExpDPTable.setStatus("current")
_ProfilesRegExpDPEntry_Object = MibTableRow
profilesRegExpDPEntry = _ProfilesRegExpDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 3, 1)
)
profilesRegExpDPEntry.setIndexNames(
    (0, "ELTEX-FXS72", "profileNumber"),
)
if mibBuilder.loadTexts:
    profilesRegExpDPEntry.setStatus("current")
_ProfileRegExpDialOn_Type = TruthValue
_ProfileRegExpDialOn_Object = MibTableColumn
profileRegExpDialOn = _ProfileRegExpDialOn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 3, 1, 1),
    _ProfileRegExpDialOn_Type()
)
profileRegExpDialOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileRegExpDialOn.setStatus("current")
_ProfileRegExpDialProtocol_Type = TauDialProtocolType
_ProfileRegExpDialProtocol_Object = MibTableColumn
profileRegExpDialProtocol = _ProfileRegExpDialProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 3, 1, 2),
    _ProfileRegExpDialProtocol_Type()
)
profileRegExpDialProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileRegExpDialProtocol.setStatus("current")
_ProfileRegExpDialText_Type = OctetString
_ProfileRegExpDialText_Object = MibTableColumn
profileRegExpDialText = _ProfileRegExpDialText_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 3, 1, 3),
    _ProfileRegExpDialText_Type()
)
profileRegExpDialText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    profileRegExpDialText.setStatus("current")
_ProfileRegExpDialRowStatus_Type = RowStatus
_ProfileRegExpDialRowStatus_Object = MibTableColumn
profileRegExpDialRowStatus = _ProfileRegExpDialRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 5, 3, 1, 4),
    _ProfileRegExpDialRowStatus_Type()
)
profileRegExpDialRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profileRegExpDialRowStatus.setStatus("current")
_ProfilesCodecs_ObjectIdentity = ObjectIdentity
profilesCodecs = _ProfilesCodecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7)
)
_ProfilesCodecsTable_Object = MibTable
profilesCodecsTable = _ProfilesCodecsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1)
)
if mibBuilder.loadTexts:
    profilesCodecsTable.setStatus("current")
_ProfilesCodecsEntry_Object = MibTableRow
profilesCodecsEntry = _ProfilesCodecsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1)
)
profilesCodecsEntry.setIndexNames(
    (0, "ELTEX-FXS72", "profileNumber"),
)
if mibBuilder.loadTexts:
    profilesCodecsEntry.setStatus("current")
_UseG711A_Type = Integer32
_UseG711A_Object = MibTableColumn
useG711A = _UseG711A_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 1),
    _UseG711A_Type()
)
useG711A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useG711A.setStatus("current")
_UseG711U_Type = Integer32
_UseG711U_Object = MibTableColumn
useG711U = _UseG711U_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 2),
    _UseG711U_Type()
)
useG711U.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useG711U.setStatus("current")
_UseG726to32_Type = Integer32
_UseG726to32_Object = MibTableColumn
useG726to32 = _UseG726to32_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 3),
    _UseG726to32_Type()
)
useG726to32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useG726to32.setStatus("current")
_UseG723_Type = Integer32
_UseG723_Object = MibTableColumn
useG723 = _UseG723_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 4),
    _UseG723_Type()
)
useG723.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useG723.setStatus("current")
_UseG729B_Type = Integer32
_UseG729B_Object = MibTableColumn
useG729B = _UseG729B_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 6),
    _UseG729B_Type()
)
useG729B.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useG729B.setStatus("current")
_UseG729A_Type = Integer32
_UseG729A_Object = MibTableColumn
useG729A = _UseG729A_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 7),
    _UseG729A_Type()
)
useG729A.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useG729A.setStatus("current")
_G711Ptime_Type = Integer32
_G711Ptime_Object = MibTableColumn
g711Ptime = _G711Ptime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 8),
    _G711Ptime_Type()
)
g711Ptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g711Ptime.setStatus("current")
_G729Ptime_Type = Integer32
_G729Ptime_Object = MibTableColumn
g729Ptime = _G729Ptime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 9),
    _G729Ptime_Type()
)
g729Ptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g729Ptime.setStatus("current")
_G723Ptime_Type = Integer32
_G723Ptime_Object = MibTableColumn
g723Ptime = _G723Ptime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 10),
    _G723Ptime_Type()
)
g723Ptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g723Ptime.setStatus("current")
_G726to32Ptime_Type = Integer32
_G726to32Ptime_Object = MibTableColumn
g726to32Ptime = _G726to32Ptime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 11),
    _G726to32Ptime_Type()
)
g726to32Ptime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g726to32Ptime.setStatus("current")
_G726to32PT_Type = Integer32
_G726to32PT_Object = MibTableColumn
g726to32PT = _G726to32PT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 12),
    _G726to32PT_Type()
)
g726to32PT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g726to32PT.setStatus("current")
_DtmfTransfer_Type = TauDtmfTransferType
_DtmfTransfer_Object = MibTableColumn
dtmfTransfer = _DtmfTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 13),
    _DtmfTransfer_Type()
)
dtmfTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dtmfTransfer.setStatus("current")
_FlashTransfer_Type = TauFlashTransferType
_FlashTransfer_Object = MibTableColumn
flashTransfer = _FlashTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 14),
    _FlashTransfer_Type()
)
flashTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashTransfer.setStatus("current")
_FaxDetectDirection_Type = TauFaxDirectionType
_FaxDetectDirection_Object = MibTableColumn
faxDetectDirection = _FaxDetectDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 15),
    _FaxDetectDirection_Type()
)
faxDetectDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxDetectDirection.setStatus("current")
_FaxTransferCodec_Type = TauFaxTransferType
_FaxTransferCodec_Object = MibTableColumn
faxTransferCodec = _FaxTransferCodec_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 16),
    _FaxTransferCodec_Type()
)
faxTransferCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faxTransferCodec.setStatus("current")
_SlaveFaxTransferCodec_Type = TauFaxTransferSlaveType
_SlaveFaxTransferCodec_Object = MibTableColumn
slaveFaxTransferCodec = _SlaveFaxTransferCodec_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 17),
    _SlaveFaxTransferCodec_Type()
)
slaveFaxTransferCodec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveFaxTransferCodec.setStatus("current")
_ModemTransfer_Type = TauModemTransferType
_ModemTransfer_Object = MibTableColumn
modemTransfer = _ModemTransfer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 18),
    _ModemTransfer_Type()
)
modemTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTransfer.setStatus("current")
_Rfc2833PT_Type = Integer32
_Rfc2833PT_Object = MibTableColumn
rfc2833PT = _Rfc2833PT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 19),
    _Rfc2833PT_Type()
)
rfc2833PT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfc2833PT.setStatus("current")
_SilenceSuppression_Type = TruthValue
_SilenceSuppression_Object = MibTableColumn
silenceSuppression = _SilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 20),
    _SilenceSuppression_Type()
)
silenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    silenceSuppression.setStatus("current")
_EchoCanceller_Type = TruthValue
_EchoCanceller_Object = MibTableColumn
echoCanceller = _EchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 21),
    _EchoCanceller_Type()
)
echoCanceller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    echoCanceller.setStatus("current")
_NlpDisable_Type = TruthValue
_NlpDisable_Object = MibTableColumn
nlpDisable = _NlpDisable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 22),
    _NlpDisable_Type()
)
nlpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlpDisable.setStatus("current")
_ComfortNoise_Type = TruthValue
_ComfortNoise_Object = MibTableColumn
comfortNoise = _ComfortNoise_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 23),
    _ComfortNoise_Type()
)
comfortNoise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comfortNoise.setStatus("current")
_RtcpTimer_Type = Integer32
_RtcpTimer_Object = MibTableColumn
rtcpTimer = _RtcpTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 24),
    _RtcpTimer_Type()
)
rtcpTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcpTimer.setStatus("current")
_RtcpControlPeriod_Type = Integer32
_RtcpControlPeriod_Object = MibTableColumn
rtcpControlPeriod = _RtcpControlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 25),
    _RtcpControlPeriod_Type()
)
rtcpControlPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcpControlPeriod.setStatus("current")
_CiscoNsePT_Type = Integer32
_CiscoNsePT_Object = MibTableColumn
ciscoNsePT = _CiscoNsePT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 26),
    _CiscoNsePT_Type()
)
ciscoNsePT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoNsePT.setStatus("current")
_T38MaxDatagramSize_Type = Integer32
_T38MaxDatagramSize_Object = MibTableColumn
t38MaxDatagramSize = _T38MaxDatagramSize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 27),
    _T38MaxDatagramSize_Type()
)
t38MaxDatagramSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38MaxDatagramSize.setStatus("current")
_T38Bitrate_Type = Integer32
_T38Bitrate_Object = MibTableColumn
t38Bitrate = _T38Bitrate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 28),
    _T38Bitrate_Type()
)
t38Bitrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38Bitrate.setStatus("current")
_ModemFaxDelay_Type = Integer32
_ModemFaxDelay_Object = MibTableColumn
modemFaxDelay = _ModemFaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 29),
    _ModemFaxDelay_Type()
)
modemFaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemFaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    modemFaxDelay.setUnits("ms")
_VoiceMode_Type = TauVoiceModeType
_VoiceMode_Object = MibTableColumn
voiceMode = _VoiceMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 30),
    _VoiceMode_Type()
)
voiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceMode.setStatus("current")
_VoiceDelayMin_Type = Integer32
_VoiceDelayMin_Object = MibTableColumn
voiceDelayMin = _VoiceDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 31),
    _VoiceDelayMin_Type()
)
voiceDelayMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    voiceDelayMin.setUnits("ms")
_VoiceDelayMax_Type = Integer32
_VoiceDelayMax_Object = MibTableColumn
voiceDelayMax = _VoiceDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 32),
    _VoiceDelayMax_Type()
)
voiceDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    voiceDelayMax.setUnits("ms")
_VoiceDeletionThreshold_Type = Integer32
_VoiceDeletionThreshold_Object = MibTableColumn
voiceDeletionThreshold = _VoiceDeletionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 33),
    _VoiceDeletionThreshold_Type()
)
voiceDeletionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceDeletionThreshold.setStatus("current")
if mibBuilder.loadTexts:
    voiceDeletionThreshold.setUnits("ms")
_VoiceDeletionMode_Type = TauvoiceDeletionModeType
_VoiceDeletionMode_Object = MibTableColumn
voiceDeletionMode = _VoiceDeletionMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 34),
    _VoiceDeletionMode_Type()
)
voiceDeletionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceDeletionMode.setStatus("current")
_ProfilesCodecsRowStatus_Type = RowStatus
_ProfilesCodecsRowStatus_Object = MibTableColumn
profilesCodecsRowStatus = _ProfilesCodecsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 35),
    _ProfilesCodecsRowStatus_Type()
)
profilesCodecsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    profilesCodecsRowStatus.setStatus("current")
_RtcpXR_Type = TruthValue
_RtcpXR_Object = MibTableColumn
rtcpXR = _RtcpXR_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 36),
    _RtcpXR_Type()
)
rtcpXR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtcpXR.setStatus("current")
_Rfc3264PtCommon_Type = TruthValue
_Rfc3264PtCommon_Object = MibTableColumn
rfc3264PtCommon = _Rfc3264PtCommon_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 30, 7, 1, 1, 37),
    _Rfc3264PtCommon_Type()
)
rfc3264PtCommon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfc3264PtCommon.setStatus("current")
_TauSnmpConfiguration_ObjectIdentity = ObjectIdentity
tauSnmpConfiguration = _TauSnmpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31)
)
_TauTrapSink_Type = OctetString
_TauTrapSink_Object = MibScalar
tauTrapSink = _TauTrapSink_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 1),
    _TauTrapSink_Type()
)
tauTrapSink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauTrapSink.setStatus("current")
_TauTrapType_Type = TauTrapVersion
_TauTrapType_Object = MibScalar
tauTrapType = _TauTrapType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 2),
    _TauTrapType_Type()
)
tauTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauTrapType.setStatus("current")
_TauSysName_Type = OctetString
_TauSysName_Object = MibScalar
tauSysName = _TauSysName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 3),
    _TauSysName_Type()
)
tauSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauSysName.setStatus("current")
_TauSysContact_Type = OctetString
_TauSysContact_Object = MibScalar
tauSysContact = _TauSysContact_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 4),
    _TauSysContact_Type()
)
tauSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauSysContact.setStatus("current")
_TauSysLocation_Type = OctetString
_TauSysLocation_Object = MibScalar
tauSysLocation = _TauSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 5),
    _TauSysLocation_Type()
)
tauSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauSysLocation.setStatus("current")
_TauRoCommunity_Type = OctetString
_TauRoCommunity_Object = MibScalar
tauRoCommunity = _TauRoCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 6),
    _TauRoCommunity_Type()
)
tauRoCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauRoCommunity.setStatus("current")
_TauRwCommunity_Type = OctetString
_TauRwCommunity_Object = MibScalar
tauRwCommunity = _TauRwCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 7),
    _TauRwCommunity_Type()
)
tauRwCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauRwCommunity.setStatus("current")
_TauTrapCommunity_Type = OctetString
_TauTrapCommunity_Object = MibScalar
tauTrapCommunity = _TauTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 8),
    _TauTrapCommunity_Type()
)
tauTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauTrapCommunity.setStatus("current")
_TauUserV3Name_Type = OctetString
_TauUserV3Name_Object = MibScalar
tauUserV3Name = _TauUserV3Name_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 9),
    _TauUserV3Name_Type()
)
tauUserV3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauUserV3Name.setStatus("current")
_TauUserV3Password_Type = OctetString
_TauUserV3Password_Object = MibScalar
tauUserV3Password = _TauUserV3Password_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 10),
    _TauUserV3Password_Type()
)
tauUserV3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauUserV3Password.setStatus("current")
_TauViewV3Type_Type = TauUserViewType
_TauViewV3Type_Object = MibScalar
tauViewV3Type = _TauViewV3Type_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 11),
    _TauViewV3Type_Type()
)
tauViewV3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauViewV3Type.setStatus("current")
_TauRestartSnmp_Type = TruthValue
_TauRestartSnmp_Object = MibScalar
tauRestartSnmp = _TauRestartSnmp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 31, 12),
    _TauRestartSnmp_Type()
)
tauRestartSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauRestartSnmp.setStatus("current")
_TauMegacoTrapsTable_Object = MibTable
tauMegacoTrapsTable = _TauMegacoTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32)
)
if mibBuilder.loadTexts:
    tauMegacoTrapsTable.setStatus("current")
_TauMegacoTrapsEntry_Object = MibTableRow
tauMegacoTrapsEntry = _TauMegacoTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32, 1)
)
tauMegacoTrapsEntry.setIndexNames(
    (0, "ELTEX-FXS72", "tauMegacoTrapId"),
)
if mibBuilder.loadTexts:
    tauMegacoTrapsEntry.setStatus("current")


class _TauMegacoTrapId_Type(Integer32):
    """Custom type tauMegacoTrapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TauMegacoTrapId_Type.__name__ = "Integer32"
_TauMegacoTrapId_Object = MibTableColumn
tauMegacoTrapId = _TauMegacoTrapId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32, 1, 1),
    _TauMegacoTrapId_Type()
)
tauMegacoTrapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tauMegacoTrapId.setStatus("current")
_TauMegacoTrapType_Type = TauMegacoTrapVersion
_TauMegacoTrapType_Object = MibTableColumn
tauMegacoTrapType = _TauMegacoTrapType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32, 1, 2),
    _TauMegacoTrapType_Type()
)
tauMegacoTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauMegacoTrapType.setStatus("current")
_TauMegacoTrapHost_Type = DisplayString
_TauMegacoTrapHost_Object = MibTableColumn
tauMegacoTrapHost = _TauMegacoTrapHost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32, 1, 3),
    _TauMegacoTrapHost_Type()
)
tauMegacoTrapHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauMegacoTrapHost.setStatus("current")
_TauMegacoTrapCommunity_Type = DisplayString
_TauMegacoTrapCommunity_Object = MibTableColumn
tauMegacoTrapCommunity = _TauMegacoTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32, 1, 4),
    _TauMegacoTrapCommunity_Type()
)
tauMegacoTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauMegacoTrapCommunity.setStatus("current")
_TauMegacoTrapPort_Type = Integer32
_TauMegacoTrapPort_Object = MibTableColumn
tauMegacoTrapPort = _TauMegacoTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32, 1, 5),
    _TauMegacoTrapPort_Type()
)
tauMegacoTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tauMegacoTrapPort.setStatus("current")
_TauMegacoTrapRowStatus_Type = RowStatus
_TauMegacoTrapRowStatus_Object = MibTableColumn
tauMegacoTrapRowStatus = _TauMegacoTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 32, 1, 6),
    _TauMegacoTrapRowStatus_Type()
)
tauMegacoTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tauMegacoTrapRowStatus.setStatus("current")
_FxoSerialGroups_ObjectIdentity = ObjectIdentity
fxoSerialGroups = _FxoSerialGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34)
)
_FxoSerialGroupsTable_Object = MibTable
fxoSerialGroupsTable = _FxoSerialGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1)
)
if mibBuilder.loadTexts:
    fxoSerialGroupsTable.setStatus("current")
_FxoSerialGroupsEntry_Object = MibTableRow
fxoSerialGroupsEntry = _FxoSerialGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1)
)
fxoSerialGroupsEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxsDialPlanNumber"),
)
if mibBuilder.loadTexts:
    fxoSerialGroupsEntry.setStatus("current")
_FxoSerialGroupsPhone_Type = DisplayString
_FxoSerialGroupsPhone_Object = MibTableColumn
fxoSerialGroupsPhone = _FxoSerialGroupsPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 1),
    _FxoSerialGroupsPhone_Type()
)
fxoSerialGroupsPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsPhone.setStatus("current")
_FxoSerialGroupsEnabled_Type = FxsGroupSerialEnableType
_FxoSerialGroupsEnabled_Object = MibTableColumn
fxoSerialGroupsEnabled = _FxoSerialGroupsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 2),
    _FxoSerialGroupsEnabled_Type()
)
fxoSerialGroupsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsEnabled.setStatus("current")
_FxoSerialGroupsBusyType_Type = FxoGroupBusyType
_FxoSerialGroupsBusyType_Object = MibTableColumn
fxoSerialGroupsBusyType = _FxoSerialGroupsBusyType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 3),
    _FxoSerialGroupsBusyType_Type()
)
fxoSerialGroupsBusyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsBusyType.setStatus("current")
_FxoSerialGroupsSipPort_Type = Integer32
_FxoSerialGroupsSipPort_Object = MibTableColumn
fxoSerialGroupsSipPort = _FxoSerialGroupsSipPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 4),
    _FxoSerialGroupsSipPort_Type()
)
fxoSerialGroupsSipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsSipPort.setStatus("current")
_FxoSerialGroupsAuthName_Type = DisplayString
_FxoSerialGroupsAuthName_Object = MibTableColumn
fxoSerialGroupsAuthName = _FxoSerialGroupsAuthName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 5),
    _FxoSerialGroupsAuthName_Type()
)
fxoSerialGroupsAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsAuthName.setStatus("current")
_FxoSerialGroupsAuthPass_Type = DisplayString
_FxoSerialGroupsAuthPass_Object = MibTableColumn
fxoSerialGroupsAuthPass = _FxoSerialGroupsAuthPass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 6),
    _FxoSerialGroupsAuthPass_Type()
)
fxoSerialGroupsAuthPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsAuthPass.setStatus("current")
_FxoSerialGroupsPorts_Type = DisplayString
_FxoSerialGroupsPorts_Object = MibTableColumn
fxoSerialGroupsPorts = _FxoSerialGroupsPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 7),
    _FxoSerialGroupsPorts_Type()
)
fxoSerialGroupsPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsPorts.setStatus("current")
_FxoSerialGroupsSipProfile_Type = Integer32
_FxoSerialGroupsSipProfile_Object = MibTableColumn
fxoSerialGroupsSipProfile = _FxoSerialGroupsSipProfile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 8),
    _FxoSerialGroupsSipProfile_Type()
)
fxoSerialGroupsSipProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsSipProfile.setStatus("current")
_FxoSerialGroupsTransmitNumber_Type = TruthValue
_FxoSerialGroupsTransmitNumber_Object = MibTableColumn
fxoSerialGroupsTransmitNumber = _FxoSerialGroupsTransmitNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 9),
    _FxoSerialGroupsTransmitNumber_Type()
)
fxoSerialGroupsTransmitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsTransmitNumber.setStatus("current")
_FxoSerialGroupsDontTransmitPrefix_Type = TruthValue
_FxoSerialGroupsDontTransmitPrefix_Object = MibTableColumn
fxoSerialGroupsDontTransmitPrefix = _FxoSerialGroupsDontTransmitPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 10),
    _FxoSerialGroupsDontTransmitPrefix_Type()
)
fxoSerialGroupsDontTransmitPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsDontTransmitPrefix.setStatus("current")
_FxoSerialGroupsRowStatus_Type = RowStatus
_FxoSerialGroupsRowStatus_Object = MibTableColumn
fxoSerialGroupsRowStatus = _FxoSerialGroupsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 11),
    _FxoSerialGroupsRowStatus_Type()
)
fxoSerialGroupsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fxoSerialGroupsRowStatus.setStatus("current")
_FxoSerialGroupsSend503OnBusy_Type = TruthValue
_FxoSerialGroupsSend503OnBusy_Object = MibTableColumn
fxoSerialGroupsSend503OnBusy = _FxoSerialGroupsSend503OnBusy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 12),
    _FxoSerialGroupsSend503OnBusy_Type()
)
fxoSerialGroupsSend503OnBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsSend503OnBusy.setStatus("current")
_FxoSerialGroupsType_Type = FxoGroupType
_FxoSerialGroupsType_Object = MibTableColumn
fxoSerialGroupsType = _FxoSerialGroupsType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 34, 1, 1, 13),
    _FxoSerialGroupsType_Type()
)
fxoSerialGroupsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxoSerialGroupsType.setStatus("current")
_FxsNetwork_ObjectIdentity = ObjectIdentity
fxsNetwork = _FxsNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35)
)
_FxsAutoupdateSettings_ObjectIdentity = ObjectIdentity
fxsAutoupdateSettings = _FxsAutoupdateSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1)
)
_FxsEnableAutoupdate_Type = TruthValue
_FxsEnableAutoupdate_Object = MibScalar
fxsEnableAutoupdate = _FxsEnableAutoupdate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 1),
    _FxsEnableAutoupdate_Type()
)
fxsEnableAutoupdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsEnableAutoupdate.setStatus("current")
_FxsSource_Type = FxsNetworkAutoupdateSourceType
_FxsSource_Object = MibScalar
fxsSource = _FxsSource_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 2),
    _FxsSource_Type()
)
fxsSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsSource.setStatus("current")


class _FxsTFTPServer_Type(DisplayString):
    """Custom type fxsTFTPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FxsTFTPServer_Type.__name__ = "DisplayString"
_FxsTFTPServer_Object = MibScalar
fxsTFTPServer = _FxsTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 3),
    _FxsTFTPServer_Type()
)
fxsTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsTFTPServer.setStatus("current")


class _FxsConfigurationFile_Type(DisplayString):
    """Custom type fxsConfigurationFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FxsConfigurationFile_Type.__name__ = "DisplayString"
_FxsConfigurationFile_Object = MibScalar
fxsConfigurationFile = _FxsConfigurationFile_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 4),
    _FxsConfigurationFile_Type()
)
fxsConfigurationFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsConfigurationFile.setStatus("current")


class _FxsFirmwareVersion_Type(DisplayString):
    """Custom type fxsFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_FxsFirmwareVersion_Type.__name__ = "DisplayString"
_FxsFirmwareVersion_Object = MibScalar
fxsFirmwareVersion = _FxsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 5),
    _FxsFirmwareVersion_Type()
)
fxsFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsFirmwareVersion.setStatus("current")


class _FxsConfigurationUpdateInterval_Type(Integer32):
    """Custom type fxsConfigurationUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 65535),
    )


_FxsConfigurationUpdateInterval_Type.__name__ = "Integer32"
_FxsConfigurationUpdateInterval_Object = MibScalar
fxsConfigurationUpdateInterval = _FxsConfigurationUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 6),
    _FxsConfigurationUpdateInterval_Type()
)
fxsConfigurationUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsConfigurationUpdateInterval.setStatus("current")


class _FxsFirmwareUpdateInterval_Type(Integer32):
    """Custom type fxsFirmwareUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 65535),
    )


_FxsFirmwareUpdateInterval_Type.__name__ = "Integer32"
_FxsFirmwareUpdateInterval_Object = MibScalar
fxsFirmwareUpdateInterval = _FxsFirmwareUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 7),
    _FxsFirmwareUpdateInterval_Type()
)
fxsFirmwareUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsFirmwareUpdateInterval.setStatus("current")
_AutoupdateProtocol_Type = AutoupdateProtocolType
_AutoupdateProtocol_Object = MibScalar
autoupdateProtocol = _AutoupdateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 8),
    _AutoupdateProtocol_Type()
)
autoupdateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoupdateProtocol.setStatus("current")
_AutoupdateAuth_Type = TruthValue
_AutoupdateAuth_Object = MibScalar
autoupdateAuth = _AutoupdateAuth_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 9),
    _AutoupdateAuth_Type()
)
autoupdateAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoupdateAuth.setStatus("current")


class _AutoupdateUser_Type(DisplayString):
    """Custom type autoupdateUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AutoupdateUser_Type.__name__ = "DisplayString"
_AutoupdateUser_Object = MibScalar
autoupdateUser = _AutoupdateUser_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 10),
    _AutoupdateUser_Type()
)
autoupdateUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoupdateUser.setStatus("current")


class _AutoupdatePassword_Type(DisplayString):
    """Custom type autoupdatePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AutoupdatePassword_Type.__name__ = "DisplayString"
_AutoupdatePassword_Object = MibScalar
autoupdatePassword = _AutoupdatePassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 35, 1, 11),
    _AutoupdatePassword_Type()
)
autoupdatePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoupdatePassword.setStatus("current")
_FxsVoipGeneral_ObjectIdentity = ObjectIdentity
fxsVoipGeneral = _FxsVoipGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37)
)
_FansForceEnable_Type = TruthValue
_FansForceEnable_Object = MibScalar
fansForceEnable = _FansForceEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 1),
    _FansForceEnable_Type()
)
fansForceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fansForceEnable.setStatus("current")


class _FansThresholdTemperature_Type(Integer32):
    """Custom type fansThresholdTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 55),
    )


_FansThresholdTemperature_Type.__name__ = "Integer32"
_FansThresholdTemperature_Object = MibScalar
fansThresholdTemperature = _FansThresholdTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 2),
    _FansThresholdTemperature_Type()
)
fansThresholdTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fansThresholdTemperature.setStatus("current")


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 3),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_StartTimer_Type = Integer32
_StartTimer_Object = MibScalar
startTimer = _StartTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 4),
    _StartTimer_Type()
)
startTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startTimer.setStatus("current")
_DurationTimer_Type = Integer32
_DurationTimer_Object = MibScalar
durationTimer = _DurationTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 5),
    _DurationTimer_Type()
)
durationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    durationTimer.setStatus("current")
_WaitAnswerTimer_Type = Integer32
_WaitAnswerTimer_Object = MibScalar
waitAnswerTimer = _WaitAnswerTimer_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 6),
    _WaitAnswerTimer_Type()
)
waitAnswerTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waitAnswerTimer.setStatus("current")
_PowerMode_Type = PowerMode
_PowerMode_Object = MibScalar
powerMode = _PowerMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 7),
    _PowerMode_Type()
)
powerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerMode.setStatus("current")
_SiptUsePrefix_Type = TruthValue
_SiptUsePrefix_Object = MibScalar
siptUsePrefix = _SiptUsePrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 8),
    _SiptUsePrefix_Type()
)
siptUsePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siptUsePrefix.setStatus("current")
_SiptPrefix_Type = DisplayString
_SiptPrefix_Object = MibScalar
siptPrefix = _SiptPrefix_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 37, 9),
    _SiptPrefix_Type()
)
siptPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siptPrefix.setStatus("current")
_FxsSyslog_ObjectIdentity = ObjectIdentity
fxsSyslog = _FxsSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38)
)
_RunSyslog_Type = TruthValue
_RunSyslog_Object = MibScalar
runSyslog = _RunSyslog_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 1),
    _RunSyslog_Type()
)
runSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runSyslog.setStatus("current")
_SyslogAddr_Type = DisplayString
_SyslogAddr_Object = MibScalar
syslogAddr = _SyslogAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 2),
    _SyslogAddr_Type()
)
syslogAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogAddr.setStatus("current")
_SyslogPort_Type = Integer32
_SyslogPort_Object = MibScalar
syslogPort = _SyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 3),
    _SyslogPort_Type()
)
syslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogPort.setStatus("current")
_AppErr_Type = TruthValue
_AppErr_Object = MibScalar
appErr = _AppErr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 4),
    _AppErr_Type()
)
appErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appErr.setStatus("current")
_AppWarn_Type = TruthValue
_AppWarn_Object = MibScalar
appWarn = _AppWarn_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 5),
    _AppWarn_Type()
)
appWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appWarn.setStatus("current")
_AppInfo_Type = TruthValue
_AppInfo_Object = MibScalar
appInfo = _AppInfo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 6),
    _AppInfo_Type()
)
appInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appInfo.setStatus("current")
_AppDbg_Type = TruthValue
_AppDbg_Object = MibScalar
appDbg = _AppDbg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 7),
    _AppDbg_Type()
)
appDbg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appDbg.setStatus("current")
_SipLevel_Type = SipLogLevel
_SipLevel_Object = MibScalar
sipLevel = _SipLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 8),
    _SipLevel_Type()
)
sipLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipLevel.setStatus("current")
_H323Level_Type = H323LogLevel
_H323Level_Object = MibScalar
h323Level = _H323Level_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 9),
    _H323Level_Type()
)
h323Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h323Level.setStatus("current")
_VapiEnabled_Type = TruthValue
_VapiEnabled_Object = MibScalar
vapiEnabled = _VapiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 10),
    _VapiEnabled_Type()
)
vapiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapiEnabled.setStatus("current")
_VapiLibLevel_Type = VapiLibLogLevel
_VapiLibLevel_Object = MibScalar
vapiLibLevel = _VapiLibLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 11),
    _VapiLibLevel_Type()
)
vapiLibLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapiLibLevel.setStatus("current")
_VapiAppLevel_Type = VapiAppLogLevel
_VapiAppLevel_Object = MibScalar
vapiAppLevel = _VapiAppLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 12),
    _VapiAppLevel_Type()
)
vapiAppLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vapiAppLevel.setStatus("current")
_AppAlarm_Type = TruthValue
_AppAlarm_Object = MibScalar
appAlarm = _AppAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 38, 13),
    _AppAlarm_Type()
)
appAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appAlarm.setStatus("current")
_TestPortsTable_Object = MibTable
testPortsTable = _TestPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39)
)
if mibBuilder.loadTexts:
    testPortsTable.setStatus("current")
_TestPortsTableEntry_Object = MibTableRow
testPortsTableEntry = _TestPortsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1)
)
testPortsTableEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxsPortNumber"),
)
if mibBuilder.loadTexts:
    testPortsTableEntry.setStatus("current")
_PortTestTestStatus_Type = FxsPortTestStatus
_PortTestTestStatus_Object = MibTableColumn
portTestTestStatus = _PortTestTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 1),
    _PortTestTestStatus_Type()
)
portTestTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestTestStatus.setStatus("current")
_PortTestTestStartTime_Type = Unsigned32
_PortTestTestStartTime_Object = MibTableColumn
portTestTestStartTime = _PortTestTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 2),
    _PortTestTestStartTime_Type()
)
portTestTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestTestStartTime.setStatus("current")
_PortTestLastTestStartTime_Type = Unsigned32
_PortTestLastTestStartTime_Object = MibTableColumn
portTestLastTestStartTime = _PortTestLastTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 3),
    _PortTestLastTestStartTime_Type()
)
portTestLastTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestLastTestStartTime.setStatus("current")
_PortTestLastTestEndTime_Type = Unsigned32
_PortTestLastTestEndTime_Object = MibTableColumn
portTestLastTestEndTime = _PortTestLastTestEndTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 4),
    _PortTestLastTestEndTime_Type()
)
portTestLastTestEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestLastTestEndTime.setStatus("current")
_PortTestResultFlag_Type = FxsPortTestFlag
_PortTestResultFlag_Object = MibTableColumn
portTestResultFlag = _PortTestResultFlag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 5),
    _PortTestResultFlag_Type()
)
portTestResultFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestResultFlag.setStatus("current")
_PortTestRingU_Type = DisplayString
_PortTestRingU_Object = MibTableColumn
portTestRingU = _PortTestRingU_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 6),
    _PortTestRingU_Type()
)
portTestRingU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestRingU.setStatus("current")
if mibBuilder.loadTexts:
    portTestRingU.setUnits("V")
_PortTestTipU_Type = DisplayString
_PortTestTipU_Object = MibTableColumn
portTestTipU = _PortTestTipU_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 7),
    _PortTestTipU_Type()
)
portTestTipU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestTipU.setStatus("current")
if mibBuilder.loadTexts:
    portTestTipU.setUnits("V")
_PortTestShortVbat_Type = DisplayString
_PortTestShortVbat_Object = MibTableColumn
portTestShortVbat = _PortTestShortVbat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 8),
    _PortTestShortVbat_Type()
)
portTestShortVbat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestShortVbat.setStatus("current")
if mibBuilder.loadTexts:
    portTestShortVbat.setUnits("V")
_PortTestResistTr_Type = DisplayString
_PortTestResistTr_Object = MibTableColumn
portTestResistTr = _PortTestResistTr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 9),
    _PortTestResistTr_Type()
)
portTestResistTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestResistTr.setStatus("current")
if mibBuilder.loadTexts:
    portTestResistTr.setUnits("kOhm")
_PortTestResistTg_Type = DisplayString
_PortTestResistTg_Object = MibTableColumn
portTestResistTg = _PortTestResistTg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 10),
    _PortTestResistTg_Type()
)
portTestResistTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestResistTg.setStatus("current")
if mibBuilder.loadTexts:
    portTestResistTg.setUnits("kOhm")
_PortTestResistRg_Type = DisplayString
_PortTestResistRg_Object = MibTableColumn
portTestResistRg = _PortTestResistRg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 11),
    _PortTestResistRg_Type()
)
portTestResistRg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestResistRg.setStatus("current")
if mibBuilder.loadTexts:
    portTestResistRg.setUnits("kOhm")
_PortTestCapacityTr_Type = DisplayString
_PortTestCapacityTr_Object = MibTableColumn
portTestCapacityTr = _PortTestCapacityTr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 12),
    _PortTestCapacityTr_Type()
)
portTestCapacityTr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestCapacityTr.setStatus("current")
if mibBuilder.loadTexts:
    portTestCapacityTr.setUnits("uF")
_PortTestCapacityTg_Type = DisplayString
_PortTestCapacityTg_Object = MibTableColumn
portTestCapacityTg = _PortTestCapacityTg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 13),
    _PortTestCapacityTg_Type()
)
portTestCapacityTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestCapacityTg.setStatus("current")
if mibBuilder.loadTexts:
    portTestCapacityTg.setUnits("uF")
_PortTestCapacityRg_Type = DisplayString
_PortTestCapacityRg_Object = MibTableColumn
portTestCapacityRg = _PortTestCapacityRg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 14),
    _PortTestCapacityRg_Type()
)
portTestCapacityRg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTestCapacityRg.setStatus("current")
if mibBuilder.loadTexts:
    portTestCapacityRg.setUnits("uF")
_PortTestRunTest_Type = Integer32
_PortTestRunTest_Object = MibTableColumn
portTestRunTest = _PortTestRunTest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 39, 1, 15),
    _PortTestRunTest_Type()
)
portTestRunTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTestRunTest.setStatus("current")
_MonitorSerialGroupsMIBBoundary_Type = Integer32
_MonitorSerialGroupsMIBBoundary_Object = MibScalar
monitorSerialGroupsMIBBoundary = _MonitorSerialGroupsMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 40),
    _MonitorSerialGroupsMIBBoundary_Type()
)
monitorSerialGroupsMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorSerialGroupsMIBBoundary.setStatus("current")
_MonitorSerialGroupsTable_Object = MibTable
monitorSerialGroupsTable = _MonitorSerialGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41)
)
if mibBuilder.loadTexts:
    monitorSerialGroupsTable.setStatus("current")
_MonitorSerialGroupsEntry_Object = MibTableRow
monitorSerialGroupsEntry = _MonitorSerialGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1)
)
monitorSerialGroupsEntry.setIndexNames(
    (0, "ELTEX-FXS72", "serialGroupNumber"),
)
if mibBuilder.loadTexts:
    monitorSerialGroupsEntry.setStatus("current")
_SerialGroupNumber_Type = Unsigned32
_SerialGroupNumber_Object = MibTableColumn
serialGroupNumber = _SerialGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1, 1),
    _SerialGroupNumber_Type()
)
serialGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serialGroupNumber.setStatus("current")
_SerialGroupPhone_Type = DisplayString
_SerialGroupPhone_Object = MibTableColumn
serialGroupPhone = _SerialGroupPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1, 2),
    _SerialGroupPhone_Type()
)
serialGroupPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialGroupPhone.setStatus("current")
_SerialGroupRegistrationState_Type = GroupRegistrationState
_SerialGroupRegistrationState_Object = MibTableColumn
serialGroupRegistrationState = _SerialGroupRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1, 3),
    _SerialGroupRegistrationState_Type()
)
serialGroupRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialGroupRegistrationState.setStatus("current")
_SerialGroupRegistrationHost_Type = DisplayString
_SerialGroupRegistrationHost_Object = MibTableColumn
serialGroupRegistrationHost = _SerialGroupRegistrationHost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1, 4),
    _SerialGroupRegistrationHost_Type()
)
serialGroupRegistrationHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialGroupRegistrationHost.setStatus("current")
_SerialGroupLastRegistrationAt_Type = DisplayString
_SerialGroupLastRegistrationAt_Object = MibTableColumn
serialGroupLastRegistrationAt = _SerialGroupLastRegistrationAt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1, 5),
    _SerialGroupLastRegistrationAt_Type()
)
serialGroupLastRegistrationAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialGroupLastRegistrationAt.setStatus("current")
_SerialGroupNextRegistrationAfter_Type = DisplayString
_SerialGroupNextRegistrationAfter_Object = MibTableColumn
serialGroupNextRegistrationAfter = _SerialGroupNextRegistrationAfter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1, 6),
    _SerialGroupNextRegistrationAfter_Type()
)
serialGroupNextRegistrationAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialGroupNextRegistrationAfter.setStatus("current")
_SerialGroupH323GK_Type = DisplayString
_SerialGroupH323GK_Object = MibTableColumn
serialGroupH323GK = _SerialGroupH323GK_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 41, 1, 7),
    _SerialGroupH323GK_Type()
)
serialGroupH323GK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialGroupH323GK.setStatus("current")
_MonitorFxoGroupsTable_Object = MibTable
monitorFxoGroupsTable = _MonitorFxoGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42)
)
if mibBuilder.loadTexts:
    monitorFxoGroupsTable.setStatus("current")
_MonitorFxoGroupsEntry_Object = MibTableRow
monitorFxoGroupsEntry = _MonitorFxoGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1)
)
monitorFxoGroupsEntry.setIndexNames(
    (0, "ELTEX-FXS72", "fxoGroupNumber"),
)
if mibBuilder.loadTexts:
    monitorFxoGroupsEntry.setStatus("current")
_FxoGroupNumber_Type = Unsigned32
_FxoGroupNumber_Object = MibTableColumn
fxoGroupNumber = _FxoGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1, 1),
    _FxoGroupNumber_Type()
)
fxoGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fxoGroupNumber.setStatus("current")
_FxoGroupPhone_Type = DisplayString
_FxoGroupPhone_Object = MibTableColumn
fxoGroupPhone = _FxoGroupPhone_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1, 2),
    _FxoGroupPhone_Type()
)
fxoGroupPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoGroupPhone.setStatus("current")
_FxoGroupRegistrationState_Type = GroupRegistrationState
_FxoGroupRegistrationState_Object = MibTableColumn
fxoGroupRegistrationState = _FxoGroupRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1, 3),
    _FxoGroupRegistrationState_Type()
)
fxoGroupRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoGroupRegistrationState.setStatus("current")
_FxoGroupRegistrationHost_Type = DisplayString
_FxoGroupRegistrationHost_Object = MibTableColumn
fxoGroupRegistrationHost = _FxoGroupRegistrationHost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1, 4),
    _FxoGroupRegistrationHost_Type()
)
fxoGroupRegistrationHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoGroupRegistrationHost.setStatus("current")
_FxoGroupLastRegistrationAt_Type = DisplayString
_FxoGroupLastRegistrationAt_Object = MibTableColumn
fxoGroupLastRegistrationAt = _FxoGroupLastRegistrationAt_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1, 5),
    _FxoGroupLastRegistrationAt_Type()
)
fxoGroupLastRegistrationAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoGroupLastRegistrationAt.setStatus("current")
_FxoGroupNextRegistrationAfter_Type = DisplayString
_FxoGroupNextRegistrationAfter_Object = MibTableColumn
fxoGroupNextRegistrationAfter = _FxoGroupNextRegistrationAfter_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1, 6),
    _FxoGroupNextRegistrationAfter_Type()
)
fxoGroupNextRegistrationAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoGroupNextRegistrationAfter.setStatus("current")
_FxoGroupH323GK_Type = DisplayString
_FxoGroupH323GK_Object = MibTableColumn
fxoGroupH323GK = _FxoGroupH323GK_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 42, 1, 7),
    _FxoGroupH323GK_Type()
)
fxoGroupH323GK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fxoGroupH323GK.setStatus("current")
_FirewallTableMIBBoundary_Type = Integer32
_FirewallTableMIBBoundary_Object = MibScalar
firewallTableMIBBoundary = _FirewallTableMIBBoundary_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 43),
    _FirewallTableMIBBoundary_Type()
)
firewallTableMIBBoundary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallTableMIBBoundary.setStatus("current")
_FirewallConfig_ObjectIdentity = ObjectIdentity
firewallConfig = _FirewallConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44)
)
_FirewallTable_Object = MibTable
firewallTable = _FirewallTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1)
)
if mibBuilder.loadTexts:
    firewallTable.setStatus("current")
_FirewallEntry_Object = MibTableRow
firewallEntry = _FirewallEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1)
)
firewallEntry.setIndexNames(
    (0, "ELTEX-FXS72", "ruleNumber"),
)
if mibBuilder.loadTexts:
    firewallEntry.setStatus("current")
_RuleNumber_Type = Unsigned32
_RuleNumber_Object = MibTableColumn
ruleNumber = _RuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 1),
    _RuleNumber_Type()
)
ruleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruleNumber.setStatus("current")
_StartingSourceIpAddress_Type = DisplayString
_StartingSourceIpAddress_Object = MibTableColumn
startingSourceIpAddress = _StartingSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 2),
    _StartingSourceIpAddress_Type()
)
startingSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startingSourceIpAddress.setStatus("current")
_NumberOfSourceIpAddresses_Type = Unsigned32
_NumberOfSourceIpAddresses_Object = MibTableColumn
numberOfSourceIpAddresses = _NumberOfSourceIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 3),
    _NumberOfSourceIpAddresses_Type()
)
numberOfSourceIpAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfSourceIpAddresses.setStatus("current")
_AllSourceIpAddresses_Type = TruthValue
_AllSourceIpAddresses_Object = MibTableColumn
allSourceIpAddresses = _AllSourceIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 4),
    _AllSourceIpAddresses_Type()
)
allSourceIpAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allSourceIpAddresses.setStatus("current")
_Ruleprotocol_Type = FirewallProtocol
_Ruleprotocol_Object = MibTableColumn
ruleprotocol = _Ruleprotocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 5),
    _Ruleprotocol_Type()
)
ruleprotocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleprotocol.setStatus("current")
_TypeOfMessageICMP_Type = TypeOfMessageICMP
_TypeOfMessageICMP_Object = MibTableColumn
typeOfMessageICMP = _TypeOfMessageICMP_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 6),
    _TypeOfMessageICMP_Type()
)
typeOfMessageICMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    typeOfMessageICMP.setStatus("current")
_StartingSourcePort_Type = Unsigned32
_StartingSourcePort_Object = MibTableColumn
startingSourcePort = _StartingSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 7),
    _StartingSourcePort_Type()
)
startingSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startingSourcePort.setStatus("current")
_NumberOfSourcePorts_Type = Unsigned32
_NumberOfSourcePorts_Object = MibTableColumn
numberOfSourcePorts = _NumberOfSourcePorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 8),
    _NumberOfSourcePorts_Type()
)
numberOfSourcePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfSourcePorts.setStatus("current")
_AllSourcePorts_Type = TruthValue
_AllSourcePorts_Object = MibTableColumn
allSourcePorts = _AllSourcePorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 9),
    _AllSourcePorts_Type()
)
allSourcePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allSourcePorts.setStatus("current")
_StartingDestinationPort_Type = Unsigned32
_StartingDestinationPort_Object = MibTableColumn
startingDestinationPort = _StartingDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 10),
    _StartingDestinationPort_Type()
)
startingDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startingDestinationPort.setStatus("current")
_NumberOfDestinationPorts_Type = Unsigned32
_NumberOfDestinationPorts_Object = MibTableColumn
numberOfDestinationPorts = _NumberOfDestinationPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 11),
    _NumberOfDestinationPorts_Type()
)
numberOfDestinationPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberOfDestinationPorts.setStatus("current")
_AllDestinationPorts_Type = TruthValue
_AllDestinationPorts_Object = MibTableColumn
allDestinationPorts = _AllDestinationPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 12),
    _AllDestinationPorts_Type()
)
allDestinationPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allDestinationPorts.setStatus("current")
_RuleTarget_Type = FirewallTarget
_RuleTarget_Object = MibTableColumn
ruleTarget = _RuleTarget_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 13),
    _RuleTarget_Type()
)
ruleTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleTarget.setStatus("current")
_RuleMoveTo_Type = Unsigned32
_RuleMoveTo_Object = MibTableColumn
ruleMoveTo = _RuleMoveTo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 14),
    _RuleMoveTo_Type()
)
ruleMoveTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleMoveTo.setStatus("current")
_RuleRowStatus_Type = RowStatus
_RuleRowStatus_Object = MibTableColumn
ruleRowStatus = _RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 1, 1, 15),
    _RuleRowStatus_Type()
)
ruleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruleRowStatus.setStatus("current")
_FirewallApply_Type = Integer32
_FirewallApply_Object = MibScalar
firewallApply = _FirewallApply_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 2),
    _FirewallApply_Type()
)
firewallApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallApply.setStatus("current")
_FirewallConfirm_Type = Integer32
_FirewallConfirm_Object = MibScalar
firewallConfirm = _FirewallConfirm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 44, 3),
    _FirewallConfirm_Type()
)
firewallConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallConfirm.setStatus("current")
_ConfigTcpIp_ObjectIdentity = ObjectIdentity
configTcpIp = _ConfigTcpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45)
)


class _RtpSipMin_Type(Integer32):
    """Custom type rtpSipMin based on Integer32"""
    defaultValue = 23000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65500),
    )


_RtpSipMin_Type.__name__ = "Integer32"
_RtpSipMin_Object = MibScalar
rtpSipMin = _RtpSipMin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45, 1),
    _RtpSipMin_Type()
)
rtpSipMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtpSipMin.setStatus("current")


class _RtpSipMax_Type(Integer32):
    """Custom type rtpSipMax based on Integer32"""
    defaultValue = 23896

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65500),
    )


_RtpSipMax_Type.__name__ = "Integer32"
_RtpSipMax_Object = MibScalar
rtpSipMax = _RtpSipMax_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45, 2),
    _RtpSipMax_Type()
)
rtpSipMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtpSipMax.setStatus("current")


class _InterceptPortMin_Type(Integer32):
    """Custom type interceptPortMin based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65500),
    )


_InterceptPortMin_Type.__name__ = "Integer32"
_InterceptPortMin_Object = MibScalar
interceptPortMin = _InterceptPortMin_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45, 3),
    _InterceptPortMin_Type()
)
interceptPortMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interceptPortMin.setStatus("current")


class _InterceptPortMax_Type(Integer32):
    """Custom type interceptPortMax based on Integer32"""
    defaultValue = 50100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65500),
    )


_InterceptPortMax_Type.__name__ = "Integer32"
_InterceptPortMax_Object = MibScalar
interceptPortMax = _InterceptPortMax_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45, 4),
    _InterceptPortMax_Type()
)
interceptPortMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interceptPortMax.setStatus("current")


class _DiffservForSip_Type(Integer32):
    """Custom type diffservForSip based on Integer32"""
    defaultValue = 104

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiffservForSip_Type.__name__ = "Integer32"
_DiffservForSip_Object = MibScalar
diffservForSip = _DiffservForSip_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45, 5),
    _DiffservForSip_Type()
)
diffservForSip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservForSip.setStatus("current")


class _DiffservForRtp_Type(Integer32):
    """Custom type diffservForRtp based on Integer32"""
    defaultValue = 184

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiffservForRtp_Type.__name__ = "Integer32"
_DiffservForRtp_Object = MibScalar
diffservForRtp = _DiffservForRtp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45, 6),
    _DiffservForRtp_Type()
)
diffservForRtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffservForRtp.setStatus("current")


class _VerifyRemoteMediaAddress_Type(TruthValue):
    """Custom type verifyRemoteMediaAddress based on TruthValue"""


_VerifyRemoteMediaAddress_Object = MibScalar
verifyRemoteMediaAddress = _VerifyRemoteMediaAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 45, 7),
    _VerifyRemoteMediaAddress_Type()
)
verifyRemoteMediaAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verifyRemoteMediaAddress.setStatus("current")
_CallLimitTable_Object = MibTable
callLimitTable = _CallLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 46)
)
if mibBuilder.loadTexts:
    callLimitTable.setStatus("current")
_CallLimitEntry_Object = MibTableRow
callLimitEntry = _CallLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 46, 1)
)
callLimitEntry.setIndexNames(
    (0, "ELTEX-FXS72", "clIndex"),
)
if mibBuilder.loadTexts:
    callLimitEntry.setStatus("current")


class _ClIndex_Type(Integer32):
    """Custom type clIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ClIndex_Type.__name__ = "Integer32"
_ClIndex_Object = MibTableColumn
clIndex = _ClIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 46, 1, 1),
    _ClIndex_Type()
)
clIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clIndex.setStatus("current")
_ClType_Type = CallLimitType
_ClType_Object = MibTableColumn
clType = _ClType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 46, 1, 2),
    _ClType_Type()
)
clType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clType.setStatus("current")
_ClHostOfNeighbourGateway_Type = DisplayString
_ClHostOfNeighbourGateway_Object = MibTableColumn
clHostOfNeighbourGateway = _ClHostOfNeighbourGateway_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 46, 1, 3),
    _ClHostOfNeighbourGateway_Type()
)
clHostOfNeighbourGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clHostOfNeighbourGateway.setStatus("current")
_ClSimultaneousCallsCount_Type = Integer32
_ClSimultaneousCallsCount_Object = MibTableColumn
clSimultaneousCallsCount = _ClSimultaneousCallsCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 46, 1, 4),
    _ClSimultaneousCallsCount_Type()
)
clSimultaneousCallsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clSimultaneousCallsCount.setStatus("current")
_ClRowStatus_Type = RowStatus
_ClRowStatus_Object = MibTableColumn
clRowStatus = _ClRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 46, 1, 5),
    _ClRowStatus_Type()
)
clRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clRowStatus.setStatus("current")
_DistinctiveRingTable_Object = MibTable
distinctiveRingTable = _DistinctiveRingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47)
)
if mibBuilder.loadTexts:
    distinctiveRingTable.setStatus("current")
_DistinctiveRingEntry_Object = MibTableRow
distinctiveRingEntry = _DistinctiveRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47, 1)
)
distinctiveRingEntry.setIndexNames(
    (0, "ELTEX-FXS72", "drId"),
)
if mibBuilder.loadTexts:
    distinctiveRingEntry.setStatus("current")


class _DrId_Type(Integer32):
    """Custom type drId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DrId_Type.__name__ = "Integer32"
_DrId_Object = MibTableColumn
drId = _DrId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47, 1, 1),
    _DrId_Type()
)
drId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    drId.setStatus("current")
_DrRule_Type = DisplayString
_DrRule_Object = MibTableColumn
drRule = _DrRule_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47, 1, 2),
    _DrRule_Type()
)
drRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drRule.setStatus("current")


class _DrRing_Type(Integer32):
    """Custom type drRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_DrRing_Type.__name__ = "Integer32"
_DrRing_Object = MibTableColumn
drRing = _DrRing_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47, 1, 3),
    _DrRing_Type()
)
drRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drRing.setStatus("current")


class _DrPause_Type(Integer32):
    """Custom type drPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_DrPause_Type.__name__ = "Integer32"
_DrPause_Object = MibTableColumn
drPause = _DrPause_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47, 1, 4),
    _DrPause_Type()
)
drPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drPause.setStatus("current")
_DrSubscriberProfiles_Type = DRSubscriberProfilesType
_DrSubscriberProfiles_Object = MibTableColumn
drSubscriberProfiles = _DrSubscriberProfiles_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47, 1, 5),
    _DrSubscriberProfiles_Type()
)
drSubscriberProfiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drSubscriberProfiles.setStatus("current")
_DrRowStatus_Type = RowStatus
_DrRowStatus_Object = MibTableColumn
drRowStatus = _DrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 47, 1, 6),
    _DrRowStatus_Type()
)
drRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    drRowStatus.setStatus("current")
_ModifiersTable_Object = MibTable
modifiersTable = _ModifiersTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48)
)
if mibBuilder.loadTexts:
    modifiersTable.setStatus("current")
_ModifiersEntry_Object = MibTableRow
modifiersEntry = _ModifiersEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48, 1)
)
modifiersEntry.setIndexNames(
    (0, "ELTEX-FXS72", "modifierNumber"),
    (0, "ELTEX-FXS72", "modifierRule"),
)
if mibBuilder.loadTexts:
    modifiersEntry.setStatus("current")


class _ModifierNumber_Type(Integer32):
    """Custom type modifierNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModifierNumber_Type.__name__ = "Integer32"
_ModifierNumber_Object = MibTableColumn
modifierNumber = _ModifierNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48, 1, 1),
    _ModifierNumber_Type()
)
modifierNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modifierNumber.setStatus("current")


class _ModifierRule_Type(Integer32):
    """Custom type modifierRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ModifierRule_Type.__name__ = "Integer32"
_ModifierRule_Object = MibTableColumn
modifierRule = _ModifierRule_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48, 1, 2),
    _ModifierRule_Type()
)
modifierRule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modifierRule.setStatus("current")
_ModifierDialedNumberRegexpRule_Type = DisplayString
_ModifierDialedNumberRegexpRule_Object = MibTableColumn
modifierDialedNumberRegexpRule = _ModifierDialedNumberRegexpRule_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48, 1, 3),
    _ModifierDialedNumberRegexpRule_Type()
)
modifierDialedNumberRegexpRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modifierDialedNumberRegexpRule.setStatus("current")
_ModifierDialedNumberModification_Type = DisplayString
_ModifierDialedNumberModification_Object = MibTableColumn
modifierDialedNumberModification = _ModifierDialedNumberModification_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48, 1, 4),
    _ModifierDialedNumberModification_Type()
)
modifierDialedNumberModification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modifierDialedNumberModification.setStatus("current")
_ModifierCallingNumberModification_Type = DisplayString
_ModifierCallingNumberModification_Object = MibTableColumn
modifierCallingNumberModification = _ModifierCallingNumberModification_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48, 1, 5),
    _ModifierCallingNumberModification_Type()
)
modifierCallingNumberModification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modifierCallingNumberModification.setStatus("current")
_ModifierRowStatus_Type = RowStatus
_ModifierRowStatus_Object = MibTableColumn
modifierRowStatus = _ModifierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 48, 1, 6),
    _ModifierRowStatus_Type()
)
modifierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modifierRowStatus.setStatus("current")
_TauSubtypes_ObjectIdentity = ObjectIdentity
tauSubtypes = _TauSubtypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90)
)
_Tau72sip_ObjectIdentity = ObjectIdentity
tau72sip = _Tau72sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 1)
)
_Tau36sip_ObjectIdentity = ObjectIdentity
tau36sip = _Tau36sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 2)
)
_Tau32Msip_ObjectIdentity = ObjectIdentity
tau32Msip = _Tau32Msip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 3)
)
_Tau72megaco_ObjectIdentity = ObjectIdentity
tau72megaco = _Tau72megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 4)
)
_Tau72v30sip_ObjectIdentity = ObjectIdentity
tau72v30sip = _Tau72v30sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 5)
)
_Tau36v30sip_ObjectIdentity = ObjectIdentity
tau36v30sip = _Tau36v30sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 6)
)
_Fxs72sip_ObjectIdentity = ObjectIdentity
fxs72sip = _Fxs72sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 7)
)
_Tau36megaco_ObjectIdentity = ObjectIdentity
tau36megaco = _Tau36megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 8)
)
_Tau72v30megaco_ObjectIdentity = ObjectIdentity
tau72v30megaco = _Tau72v30megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 9)
)
_Tau36v30megaco_ObjectIdentity = ObjectIdentity
tau36v30megaco = _Tau36v30megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 10)
)
_Fxs72megaco_ObjectIdentity = ObjectIdentity
fxs72megaco = _Fxs72megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 11)
)
_Fxs72v21_ObjectIdentity = ObjectIdentity
fxs72v21 = _Fxs72v21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 12)
)
_Tau72v40sip_ObjectIdentity = ObjectIdentity
tau72v40sip = _Tau72v40sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 13)
)
_Tau36v40sip_ObjectIdentity = ObjectIdentity
tau36v40sip = _Tau36v40sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 14)
)
_Tau72v40megaco_ObjectIdentity = ObjectIdentity
tau72v40megaco = _Tau72v40megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 15)
)
_Tau36v40megaco_ObjectIdentity = ObjectIdentity
tau36v40megaco = _Tau36v40megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 16)
)
_Tau32MrevBsip_ObjectIdentity = ObjectIdentity
tau32MrevBsip = _Tau32MrevBsip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 17)
)
_Tau32Mmegaco_ObjectIdentity = ObjectIdentity
tau32Mmegaco = _Tau32Mmegaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 18)
)
_Tau32MrevBmegaco_ObjectIdentity = ObjectIdentity
tau32MrevBmegaco = _Tau32MrevBmegaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 19)
)
_Tau16sip_ObjectIdentity = ObjectIdentity
tau16sip = _Tau16sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 20)
)
_Tau24sip_ObjectIdentity = ObjectIdentity
tau24sip = _Tau24sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 21)
)
_Tau16megaco_ObjectIdentity = ObjectIdentity
tau16megaco = _Tau16megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 22)
)
_Tau24megaco_ObjectIdentity = ObjectIdentity
tau24megaco = _Tau24megaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 90, 23)
)

# Managed Objects groups

fxsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 9, 200)
)
fxsGroup.setObjects(
      *(("ELTEX-FXS72", "fxsDevName"),
        ("ELTEX-FXS72", "fxsDevType"),
        ("ELTEX-FXS72", "fxsDevCfgBuild"),
        ("ELTEX-FXS72", "fxsFreeSpace"),
        ("ELTEX-FXS72", "fxsFreeRam"),
        ("ELTEX-FXS72", "fxsSSwStatus"),
        ("ELTEX-FXS72", "fxsSSwStatusTime"),
        ("ELTEX-FXS72", "fxsCpuUsage"),
        ("ELTEX-FXS72", "fxsMonitoringVMode"),
        ("ELTEX-FXS72", "fxsMonitoringVBat"),
        ("ELTEX-FXS72", "fxsMonitoringVRing1"),
        ("ELTEX-FXS72", "fxsMonitoringVRing2"),
        ("ELTEX-FXS72", "fxsMonitoringTemp1"),
        ("ELTEX-FXS72", "fxsMonitoringTemp2"),
        ("ELTEX-FXS72", "fxsMonitoringTemp3"),
        ("ELTEX-FXS72", "fxsMonitoringTemp4"),
        ("ELTEX-FXS72", "fxsMonitoringFanState"),
        ("ELTEX-FXS72", "fxsMonitoringFan1Rotate"),
        ("ELTEX-FXS72", "fxsMonitoringFan2Rotate"),
        ("ELTEX-FXS72", "fxsMonitoringSubCooling"),
        ("ELTEX-FXS72", "fxsMonitoringVinput"),
        ("ELTEX-FXS72", "fxsMonitoringDevicePower"),
        ("ELTEX-FXS72", "fxsPortsMIBBoundary"),
        ("ELTEX-FXS72", "fxsPortPhoneNumber"),
        ("ELTEX-FXS72", "fxsPortState"),
        ("ELTEX-FXS72", "fxsPortUserName"),
        ("ELTEX-FXS72", "fxsPortTalkingNum"),
        ("ELTEX-FXS72", "fxsPortTalkingStartTime"),
        ("ELTEX-FXS72", "fxsPortSipConnected"),
        ("ELTEX-FXS72", "fxsPortH323Connected"),
        ("ELTEX-FXS72", "fxsPortSipConnecteNext"),
        ("ELTEX-FXS72", "fxsPortSipConnecteState"),
        ("ELTEX-FXS72", "fxsPortSipConnectHost"),
        ("ELTEX-FXS72", "fxsPortConfigPhone"),
        ("ELTEX-FXS72", "fxsPortConfigUserName"),
        ("ELTEX-FXS72", "fxsPortConfigAuthName"),
        ("ELTEX-FXS72", "fxsPortConfigAuthPass"),
        ("ELTEX-FXS72", "fxsPortConfigCustom"),
        ("ELTEX-FXS72", "fxsPortConfigPlaymoh"),
        ("ELTEX-FXS72", "fxsPortConfigAON"),
        ("ELTEX-FXS72", "fxsPortConfigAONHideDate"),
        ("ELTEX-FXS72", "fxsPortConfigAONHideName"),
        ("ELTEX-FXS72", "fxsPortConfigTaxophone"),
        ("ELTEX-FXS72", "fxsPortConfigMinFlashtime"),
        ("ELTEX-FXS72", "fxsPortConfigMaxFlashtime"),
        ("ELTEX-FXS72", "fxsPortConfigGainr"),
        ("ELTEX-FXS72", "fxsPortConfigGaint"),
        ("ELTEX-FXS72", "fxsPortConfigCategory"),
        ("ELTEX-FXS72", "fxsPortConfigCallTransfer"),
        ("ELTEX-FXS72", "fxsPortConfigCallWaiting"),
        ("ELTEX-FXS72", "fxsPortConfigHotLine"),
        ("ELTEX-FXS72", "fxsPortConfigHotNumber"),
        ("ELTEX-FXS72", "fxsPortConfigHotTimeout"),
        ("ELTEX-FXS72", "fxsPortConfigDisabled"),
        ("ELTEX-FXS72", "fxsPortConfigCtBusy"),
        ("ELTEX-FXS72", "fxsPortConfigCtUnconditional"),
        ("ELTEX-FXS72", "fxsPortConfigCtNoanswer"),
        ("ELTEX-FXS72", "fxsPortConfigCtTimeout"),
        ("ELTEX-FXS72", "fxsPortConfigClir"),
        ("ELTEX-FXS72", "fxsPortConfigStopDial"),
        ("ELTEX-FXS72", "fxsPortConfigAltNumber"),
        ("ELTEX-FXS72", "fxsPortConfigUseAltNumber"),
        ("ELTEX-FXS72", "fxsPortConfigPickUp"),
        ("ELTEX-FXS72", "fxsPortConfigSipPort"),
        ("ELTEX-FXS72", "fxsPortConfigCfgPriOverCw"),
        ("ELTEX-FXS72", "fxsPortConfigRowStatus"),
        ("ELTEX-FXS72", "fxsPortConfigDvoCwEn"),
        ("ELTEX-FXS72", "fxsPortConfigDvoCtAttendedEn"),
        ("ELTEX-FXS72", "fxsPortConfigDvoCtUnattendedEn"),
        ("ELTEX-FXS72", "fxsPortConfigDvoUnconditionalEn"),
        ("ELTEX-FXS72", "fxsPortConfigDvoCfBusyEn"),
        ("ELTEX-FXS72", "fxsPortConfigDvoCfAnswerEn"),
        ("ELTEX-FXS72", "fxsPortConfigDvoCfServiceEn"),
        ("ELTEX-FXS72", "fxsPortConfigDvoDoDisturbEn"),
        ("ELTEX-FXS72", "fxsPortConfigCtOutofservice"),
        ("ELTEX-FXS72", "fxsPortConfigCfuNumber"),
        ("ELTEX-FXS72", "fxsPortConfigCfbNumber"),
        ("ELTEX-FXS72", "fxsPortConfigCfnrNumber"),
        ("ELTEX-FXS72", "fxsPortConfigCfoosNumber"),
        ("ELTEX-FXS72", "fxsPortConfigDnd"),
        ("ELTEX-FXS72", "fxsPortConfigCtNumber"),
        ("ELTEX-FXS72", "fxsPortConfigEnableCpc"),
        ("ELTEX-FXS72", "fxsPortConfigCpcTime"),
        ("ELTEX-FXS72", "fxsPortConfigFxoFlashTime"),
        ("ELTEX-FXS72", "fxsPortConfigFxoDelTdm"),
        ("ELTEX-FXS72", "fxsPortConfigFxoRingtdm"),
        ("ELTEX-FXS72", "fxsPortConfigPstnNumberprefix"),
        ("ELTEX-FXS72", "fxsPortConfigPstnNameprefix"),
        ("ELTEX-FXS72", "fxsPortConfigUsePstnCid"),
        ("ELTEX-FXS72", "fxsPortConfigtdmhotline"),
        ("ELTEX-FXS72", "fxsPortConfigtdmhottimeout"),
        ("ELTEX-FXS72", "fxsPortConfigtdmhotnumber"),
        ("ELTEX-FXS72", "fxsPortConfigDontDetectDT"),
        ("ELTEX-FXS72", "fxsPortConfigDelayDialingTimeout"),
        ("ELTEX-FXS72", "fxsPortType"),
        ("ELTEX-FXS72", "fxsPortConfigDialing"),
        ("ELTEX-FXS72", "fxsPortConfigTransmitNumber"),
        ("ELTEX-FXS72", "fxsPortConfigDontTransmitPrefix"),
        ("ELTEX-FXS72", "fxsPortConfigPortProfileID"),
        ("ELTEX-FXS72", "fxsPortConfigSipProfileID"),
        ("ELTEX-FXS72", "fxsPortConfigDialToneDetectionParameters"),
        ("ELTEX-FXS72", "fxsPortConfigRingBackToneDetectionParameters"),
        ("ELTEX-FXS72", "fxsPortConfigBusyToneDetectionParameters"),
        ("ELTEX-FXS72", "fxsPortConfigDtDetectTime"),
        ("ELTEX-FXS72", "fxsPortConfigDecadePulseTime"),
        ("ELTEX-FXS72", "fxsPortConfigDecadePauseTime"),
        ("ELTEX-FXS72", "fxsPortConfigNoOffhookAtRinging"),
        ("ELTEX-FXS72", "fxsPortConfigFxoCallBusy"),
        ("ELTEX-FXS72", "fxsPortConfigCpcRus"),
        ("ELTEX-FXS72", "fxsPortConfigReversalPolarityAction"),
        ("ELTEX-FXS72", "fxsPortConfigPstnActivity"),
        ("ELTEX-FXS72", "fxsPortConfigPstnRbDetectTimeout"),
        ("ELTEX-FXS72", "fxsPortConfigDetectFxoLinePresence"),
        ("ELTEX-FXS72", "fxsPortConfigBlockFxoLineInOutgoingDirection"),
        ("ELTEX-FXS72", "fxsPortConfigFxoMinLevelDetect"),
        ("ELTEX-FXS72", "fxsPortConfigUseAltNumberAsContact"),
        ("ELTEX-FXS72", "fxsPortConfigModifier"),
        ("ELTEX-FXS72", "fxsPortConfigMwiDialtone"),
        ("ELTEX-FXS72", "fxsPortConfigCommonPlaymoh"),
        ("ELTEX-FXS72", "fxsPortConfigCommonAON"),
        ("ELTEX-FXS72", "fxsPortConfigCommonAONHideDate"),
        ("ELTEX-FXS72", "fxsPortConfigCommonAONHideName"),
        ("ELTEX-FXS72", "fxsPortConfigCommonTaxophone"),
        ("ELTEX-FXS72", "fxsPortConfigCommonMinFlashtime"),
        ("ELTEX-FXS72", "fxsPortConfigCommonMaxFlashtime"),
        ("ELTEX-FXS72", "fxsPortConfigCommonGainr"),
        ("ELTEX-FXS72", "fxsPortConfigCommonGaint"),
        ("ELTEX-FXS72", "fxsPortConfigCommonCategory"),
        ("ELTEX-FXS72", "fxsPortConfigCommonCallTransfer"),
        ("ELTEX-FXS72", "fxsPortConfigCommonCallWaiting"),
        ("ELTEX-FXS72", "fxsPortConfigCommonCfgPriOverCw"),
        ("ELTEX-FXS72", "fxsPortConfigCommonFxoFlashTime"),
        ("ELTEX-FXS72", "fxsPortConfigCommonFxoDelTdm"),
        ("ELTEX-FXS72", "fxsPortConfigCommonFxoRingtdm"),
        ("ELTEX-FXS72", "fxsPortConfigCommonPstnNumberprefix"),
        ("ELTEX-FXS72", "fxsPortConfigCommonPstnNameprefix"),
        ("ELTEX-FXS72", "fxsPortConfigCommonUsePstnCid"),
        ("ELTEX-FXS72", "fxsPortConfigCommonEnableCpc"),
        ("ELTEX-FXS72", "fxsPortConfigCommonCpcTime"),
        ("ELTEX-FXS72", "fxsPortConfigCommonDontDetectDT"),
        ("ELTEX-FXS72", "fxsPortConfigCommonDelayDialingTimeout"),
        ("ELTEX-FXS72", "fxsPortConfigCommonDialing"),
        ("ELTEX-FXS72", "fxsPortConfigCommonTransmitNumber"),
        ("ELTEX-FXS72", "fxsPortConfigCommonDontTransmitPrefix"),
        ("ELTEX-FXS72", "fxsDialMIBBoundary"),
        ("ELTEX-FXS72", "fxsDialPlanHost"),
        ("ELTEX-FXS72", "fxsDialPlanDigits"),
        ("ELTEX-FXS72", "fxsDialPlanTimeout"),
        ("ELTEX-FXS72", "fxsDialPlanMinDigits"),
        ("ELTEX-FXS72", "fxsDialPlanType"),
        ("ELTEX-FXS72", "fxsDialPlanAccessMask"),
        ("ELTEX-FXS72", "fxsDialPlanDialtone"),
        ("ELTEX-FXS72", "fxsDialPlanModifier"),
        ("ELTEX-FXS72", "fxsDialPlanNature"),
        ("ELTEX-FXS72", "fxsDialPlanDelnum"),
        ("ELTEX-FXS72", "fxsDialPlanPtime"),
        ("ELTEX-FXS72", "fxsDialRowStatus"),
        ("ELTEX-FXS72", "fxsDialPlanNext"),
        ("ELTEX-FXS72", "tauDialRegularOn"),
        ("ELTEX-FXS72", "tauDialRegularProtocol"),
        ("ELTEX-FXS72", "tauDialRegularText"),
        ("ELTEX-FXS72", "fxsConfigSave"),
        ("ELTEX-FXS72", "fxsConfigApply"),
        ("ELTEX-FXS72", "fxsSerialGroupsMIBBoundary"),
        ("ELTEX-FXS72", "fxsSerialGroupsPhone"),
        ("ELTEX-FXS72", "fxsSerialGroupsEnabled"),
        ("ELTEX-FXS72", "fxsSerialGroupsSerialType"),
        ("ELTEX-FXS72", "fxsSerialGroupsBusyType"),
        ("ELTEX-FXS72", "fxsSerialGroupsTimeout"),
        ("ELTEX-FXS72", "fxsSerialGroupsSipPort"),
        ("ELTEX-FXS72", "fxsSerialGroupsAuthName"),
        ("ELTEX-FXS72", "fxsSerialGroupsAuthPass"),
        ("ELTEX-FXS72", "fxsSerialGroupsPorts"),
        ("ELTEX-FXS72", "fxsSerialGroupsRowStatus"),
        ("ELTEX-FXS72", "fxsSerialGroupsSipProfile"),
        ("ELTEX-FXS72", "fxsSerialGroupsNextEmpty"),
        ("ELTEX-FXS72", "fxsReboot"),
        ("ELTEX-FXS72", "tauVoipDvoCallwaiting"),
        ("ELTEX-FXS72", "tauVoipDvoCtAttended"),
        ("ELTEX-FXS72", "tauVoipDvoCtUnattended"),
        ("ELTEX-FXS72", "tauVoipDvoCfUnconditional"),
        ("ELTEX-FXS72", "tauVoipDvoCfBusy"),
        ("ELTEX-FXS72", "tauVoipDvoCfNoanswer"),
        ("ELTEX-FXS72", "tauVoipDvoCfService"),
        ("ELTEX-FXS72", "tauVoipDvoDoDisturb"),
        ("ELTEX-FXS72", "sipEnablesip"),
        ("ELTEX-FXS72", "sipObtimeout"),
        ("ELTEX-FXS72", "sipMode"),
        ("ELTEX-FXS72", "sipOptions"),
        ("ELTEX-FXS72", "sipKeepalivet"),
        ("ELTEX-FXS72", "sipDomainToReg"),
        ("ELTEX-FXS72", "sipDomain"),
        ("ELTEX-FXS72", "sipRegisterRetryInterval"),
        ("ELTEX-FXS72", "sipOutbound"),
        ("ELTEX-FXS72", "sipInboundProxy"),
        ("ELTEX-FXS72", "sipExpires"),
        ("ELTEX-FXS72", "sipAuthentication"),
        ("ELTEX-FXS72", "sipUsername"),
        ("ELTEX-FXS72", "sipPassword"),
        ("ELTEX-FXS72", "sipProxy0"),
        ("ELTEX-FXS72", "sipRegrar0"),
        ("ELTEX-FXS72", "sipRegistration0"),
        ("ELTEX-FXS72", "sipProxy1"),
        ("ELTEX-FXS72", "sipRegrar1"),
        ("ELTEX-FXS72", "sipProxy2"),
        ("ELTEX-FXS72", "sipRegrar2"),
        ("ELTEX-FXS72", "sipProxy3"),
        ("ELTEX-FXS72", "sipRegrar3"),
        ("ELTEX-FXS72", "sipProxy4"),
        ("ELTEX-FXS72", "sipRegrar4"),
        ("ELTEX-FXS72", "sipDtmfmime"),
        ("ELTEX-FXS72", "sipHfmime"),
        ("ELTEX-FXS72", "sipCtWithReplaces"),
        ("ELTEX-FXS72", "sipShortmode"),
        ("ELTEX-FXS72", "sipTransport"),
        ("ELTEX-FXS72", "sipSipMtu"),
        ("ELTEX-FXS72", "sip100Rel"),
        ("ELTEX-FXS72", "sipUserPhone"),
        ("ELTEX-FXS72", "sipUriEscapeHash"),
        ("ELTEX-FXS72", "sipInviteTotalT"),
        ("ELTEX-FXS72", "sipInviteInitT"),
        ("ELTEX-FXS72", "sipCwRingback"),
        ("ELTEX-FXS72", "sipRingbackSdp"),
        ("ELTEX-FXS72", "sipRingback"),
        ("ELTEX-FXS72", "sipRegistration1"),
        ("ELTEX-FXS72", "sipRegistration2"),
        ("ELTEX-FXS72", "sipRegistration3"),
        ("ELTEX-FXS72", "sipRegistration4"),
        ("ELTEX-FXS72", "sipPRTPstat"),
        ("ELTEX-FXS72", "termID"),
        ("ELTEX-FXS72", "currentState"),
        ("ELTEX-FXS72", "totalCallCount"),
        ("ELTEX-FXS72", "lastCallPhone"),
        ("ELTEX-FXS72", "peakJitter"),
        ("ELTEX-FXS72", "lostPackets"),
        ("ELTEX-FXS72", "numTxPack"),
        ("ELTEX-FXS72", "numTxOct"),
        ("ELTEX-FXS72", "numRxPack"),
        ("ELTEX-FXS72", "numRxOct"),
        ("ELTEX-FXS72", "fxsUpdateFw"),
        ("ELTEX-FXS72", "sipCommonEnablesip"),
        ("ELTEX-FXS72", "sipCommonShortmode"),
        ("ELTEX-FXS72", "sipCommonTransport"),
        ("ELTEX-FXS72", "sipCommonSipMtu"),
        ("ELTEX-FXS72", "sipCommonInviteTotalT"),
        ("ELTEX-FXS72", "sipCommonInviteInitT"),
        ("ELTEX-FXS72", "sipCommonPortRegistrationDelay"),
        ("ELTEX-FXS72", "profilesSipMIBBoundary"),
        ("ELTEX-FXS72", "profileNumber"),
        ("ELTEX-FXS72", "sipProfileObtimeout"),
        ("ELTEX-FXS72", "sipProfileMode"),
        ("ELTEX-FXS72", "sipProfileOptions"),
        ("ELTEX-FXS72", "sipProfileKeepalivet"),
        ("ELTEX-FXS72", "sipProfileDomainToReg"),
        ("ELTEX-FXS72", "sipProfileRegisterRetryInterval"),
        ("ELTEX-FXS72", "sipProfileOutbound"),
        ("ELTEX-FXS72", "sipProfileInboundProxy"),
        ("ELTEX-FXS72", "sipProfileExpires"),
        ("ELTEX-FXS72", "sipProfileAuthentication"),
        ("ELTEX-FXS72", "sipProfileUsername"),
        ("ELTEX-FXS72", "sipProfilePassword"),
        ("ELTEX-FXS72", "sipProfileProxy0"),
        ("ELTEX-FXS72", "sipProfileRegrar0"),
        ("ELTEX-FXS72", "sipProfileRegistration0"),
        ("ELTEX-FXS72", "sipProfileProxy1"),
        ("ELTEX-FXS72", "sipProfileRegrar1"),
        ("ELTEX-FXS72", "sipProfileProxy2"),
        ("ELTEX-FXS72", "sipProfileRegrar2"),
        ("ELTEX-FXS72", "sipProfileProxy3"),
        ("ELTEX-FXS72", "sipProfileRegrar3"),
        ("ELTEX-FXS72", "sipProfileProxy4"),
        ("ELTEX-FXS72", "sipProfileRegrar4"),
        ("ELTEX-FXS72", "sipProfileDtmfmime"),
        ("ELTEX-FXS72", "sipProfileHfmime"),
        ("ELTEX-FXS72", "sipProfileCtWithReplaces"),
        ("ELTEX-FXS72", "sipProfile100Rel"),
        ("ELTEX-FXS72", "sipProfileUserPhone"),
        ("ELTEX-FXS72", "sipProfileUriEscapeHash"),
        ("ELTEX-FXS72", "sipProfileCwRingback"),
        ("ELTEX-FXS72", "sipProfileRingbackSdp"),
        ("ELTEX-FXS72", "sipProfileRingback"),
        ("ELTEX-FXS72", "sipProfileRegistration1"),
        ("ELTEX-FXS72", "sipProfileRegistration2"),
        ("ELTEX-FXS72", "sipProfileRegistration3"),
        ("ELTEX-FXS72", "sipProfileRegistration4"),
        ("ELTEX-FXS72", "sipProfilePRTPstat"),
        ("ELTEX-FXS72", "sipProfileRowStatus"),
        ("ELTEX-FXS72", "sipProfileDomain"),
        ("ELTEX-FXS72", "sipProfileEnableTimer"),
        ("ELTEX-FXS72", "sipProfileMinSE"),
        ("ELTEX-FXS72", "sipProfileSessionExpires"),
        ("ELTEX-FXS72", "sipProfileRemoveInactiveMedia"),
        ("ELTEX-FXS72", "sipProfileKeepAliveInterval"),
        ("ELTEX-FXS72", "sipProfileKeepAliveMode"),
        ("ELTEX-FXS72", "sipProfileConferenceMode"),
        ("ELTEX-FXS72", "sipProfileConferenceServer"),
        ("ELTEX-FXS72", "sipProfileEnableIMS"),
        ("ELTEX-FXS72", "sipProfileXCAPNameForThreePartyConference"),
        ("ELTEX-FXS72", "sipProfileXCAPNameForHotline"),
        ("ELTEX-FXS72", "sipProfileXCAPNameForCallWaiting"),
        ("ELTEX-FXS72", "sipProfileXCAPNameForCallHold"),
        ("ELTEX-FXS72", "sipProfileXCAPNameForExplicitCallTransfer"),
        ("ELTEX-FXS72", "sipProfileUseAlertInfo"),
        ("ELTEX-FXS72", "sipProfileFullRuriCompliance"),
        ("ELTEX-FXS72", "sipProfileChangeover"),
        ("ELTEX-FXS72", "profilesPortsMIBBoundary"),
        ("ELTEX-FXS72", "profilePortsPlaymoh"),
        ("ELTEX-FXS72", "profilePortsAON"),
        ("ELTEX-FXS72", "profilePortsAONHideDate"),
        ("ELTEX-FXS72", "profilePortsAONHideName"),
        ("ELTEX-FXS72", "profilePortsTaxophone"),
        ("ELTEX-FXS72", "profilePortsMinFlashtime"),
        ("ELTEX-FXS72", "profilePortsMaxFlashtime"),
        ("ELTEX-FXS72", "profilePortsGainr"),
        ("ELTEX-FXS72", "profilePortsGaint"),
        ("ELTEX-FXS72", "profilePortsCategory"),
        ("ELTEX-FXS72", "profilePortsCallTransfer"),
        ("ELTEX-FXS72", "profilePortsCallWaiting"),
        ("ELTEX-FXS72", "profilePortsCfgPriOverCw"),
        ("ELTEX-FXS72", "profilePortsFxoFlashTime"),
        ("ELTEX-FXS72", "profilePortsFxoDelTdm"),
        ("ELTEX-FXS72", "profilePortsFxoRingtdm"),
        ("ELTEX-FXS72", "profilePortsPstnNumberprefix"),
        ("ELTEX-FXS72", "profilePortsPstnNameprefix"),
        ("ELTEX-FXS72", "profilePortsUsePstnCid"),
        ("ELTEX-FXS72", "profilePortsEnableCpc"),
        ("ELTEX-FXS72", "profilePortsCpcTime"),
        ("ELTEX-FXS72", "profilePortsDontDetectDT"),
        ("ELTEX-FXS72", "profilePortsDelayDialingTimeout"),
        ("ELTEX-FXS72", "profilePortsDialing"),
        ("ELTEX-FXS72", "profilePortsTransmitNumber"),
        ("ELTEX-FXS72", "profilePortsDontTransmitPrefix"),
        ("ELTEX-FXS72", "profilePortsRowStatus"),
        ("ELTEX-FXS72", "profilePortsDialToneDetectionParameters"),
        ("ELTEX-FXS72", "profilePortsRingBackToneDetectionParameters"),
        ("ELTEX-FXS72", "profilePortsBusyToneDetectionParameters"),
        ("ELTEX-FXS72", "profilePortsDtDetectTime"),
        ("ELTEX-FXS72", "profilePortsDecadePulseTime"),
        ("ELTEX-FXS72", "profilePortsDecadePauseTime"),
        ("ELTEX-FXS72", "profilePortsFxoCallBusy"),
        ("ELTEX-FXS72", "profilePortsCpcRus"),
        ("ELTEX-FXS72", "profilePortsReversalPolarityAction"),
        ("ELTEX-FXS72", "profilePortsPstnActivity"),
        ("ELTEX-FXS72", "profilePortsPstnRbDetectTimeout"),
        ("ELTEX-FXS72", "profilePortsDetectFxoLinePresence"),
        ("ELTEX-FXS72", "profilePortsBlockFxoLineInOutgoingDirection"),
        ("ELTEX-FXS72", "profilePortsStopDial"),
        ("ELTEX-FXS72", "profilePortsFxoMinLevelDetect"),
        ("ELTEX-FXS72", "profilePortsModifier"),
        ("ELTEX-FXS72", "profilesDialPlansMIBBoundary"),
        ("ELTEX-FXS72", "profileDialPlanHost"),
        ("ELTEX-FXS72", "profileDialPlanDigits"),
        ("ELTEX-FXS72", "profileDialPlanTimeout"),
        ("ELTEX-FXS72", "profileDialPlanMinDigits"),
        ("ELTEX-FXS72", "profileDialPlanType"),
        ("ELTEX-FXS72", "profileDialPlanAccessMask"),
        ("ELTEX-FXS72", "profileDialPlanDialtone"),
        ("ELTEX-FXS72", "profileDialPlanModifier"),
        ("ELTEX-FXS72", "profileDialPlanNature"),
        ("ELTEX-FXS72", "profileDialPlanDelnum"),
        ("ELTEX-FXS72", "profileDialPlanPtime"),
        ("ELTEX-FXS72", "profileDialRowStatus"),
        ("ELTEX-FXS72", "profilesRegExpDPTableMIBBoundary"),
        ("ELTEX-FXS72", "profileRegExpDialOn"),
        ("ELTEX-FXS72", "profileRegExpDialProtocol"),
        ("ELTEX-FXS72", "profileRegExpDialText"),
        ("ELTEX-FXS72", "profileRegExpDialRowStatus"),
        ("ELTEX-FXS72", "useG711A"),
        ("ELTEX-FXS72", "useG711U"),
        ("ELTEX-FXS72", "useG726to32"),
        ("ELTEX-FXS72", "useG723"),
        ("ELTEX-FXS72", "useG729B"),
        ("ELTEX-FXS72", "useG729A"),
        ("ELTEX-FXS72", "g711Ptime"),
        ("ELTEX-FXS72", "g729Ptime"),
        ("ELTEX-FXS72", "g723Ptime"),
        ("ELTEX-FXS72", "g726to32Ptime"),
        ("ELTEX-FXS72", "g726to32PT"),
        ("ELTEX-FXS72", "dtmfTransfer"),
        ("ELTEX-FXS72", "flashTransfer"),
        ("ELTEX-FXS72", "faxDetectDirection"),
        ("ELTEX-FXS72", "faxTransferCodec"),
        ("ELTEX-FXS72", "slaveFaxTransferCodec"),
        ("ELTEX-FXS72", "modemTransfer"),
        ("ELTEX-FXS72", "rfc2833PT"),
        ("ELTEX-FXS72", "silenceSuppression"),
        ("ELTEX-FXS72", "echoCanceller"),
        ("ELTEX-FXS72", "nlpDisable"),
        ("ELTEX-FXS72", "comfortNoise"),
        ("ELTEX-FXS72", "rtcpTimer"),
        ("ELTEX-FXS72", "rtcpControlPeriod"),
        ("ELTEX-FXS72", "ciscoNsePT"),
        ("ELTEX-FXS72", "t38MaxDatagramSize"),
        ("ELTEX-FXS72", "t38Bitrate"),
        ("ELTEX-FXS72", "modemFaxDelay"),
        ("ELTEX-FXS72", "voiceMode"),
        ("ELTEX-FXS72", "voiceDelayMin"),
        ("ELTEX-FXS72", "voiceDelayMax"),
        ("ELTEX-FXS72", "voiceDeletionThreshold"),
        ("ELTEX-FXS72", "voiceDeletionMode"),
        ("ELTEX-FXS72", "profilesCodecsRowStatus"),
        ("ELTEX-FXS72", "rtcpXR"),
        ("ELTEX-FXS72", "rfc3264PtCommon"),
        ("ELTEX-FXS72", "tauTrapSink"),
        ("ELTEX-FXS72", "tauTrapType"),
        ("ELTEX-FXS72", "tauSysName"),
        ("ELTEX-FXS72", "tauSysContact"),
        ("ELTEX-FXS72", "tauSysLocation"),
        ("ELTEX-FXS72", "tauRoCommunity"),
        ("ELTEX-FXS72", "tauRwCommunity"),
        ("ELTEX-FXS72", "tauTrapCommunity"),
        ("ELTEX-FXS72", "tauUserV3Name"),
        ("ELTEX-FXS72", "tauUserV3Password"),
        ("ELTEX-FXS72", "tauViewV3Type"),
        ("ELTEX-FXS72", "tauRestartSnmp"),
        ("ELTEX-FXS72", "tauMegacoTrapType"),
        ("ELTEX-FXS72", "tauMegacoTrapHost"),
        ("ELTEX-FXS72", "tauMegacoTrapCommunity"),
        ("ELTEX-FXS72", "tauMegacoTrapPort"),
        ("ELTEX-FXS72", "tauMegacoTrapRowStatus"),
        ("ELTEX-FXS72", "fxoSerialGroupsPhone"),
        ("ELTEX-FXS72", "fxoSerialGroupsEnabled"),
        ("ELTEX-FXS72", "fxoSerialGroupsBusyType"),
        ("ELTEX-FXS72", "fxoSerialGroupsSipPort"),
        ("ELTEX-FXS72", "fxoSerialGroupsAuthName"),
        ("ELTEX-FXS72", "fxoSerialGroupsAuthPass"),
        ("ELTEX-FXS72", "fxoSerialGroupsPorts"),
        ("ELTEX-FXS72", "fxoSerialGroupsSipProfile"),
        ("ELTEX-FXS72", "fxoSerialGroupsTransmitNumber"),
        ("ELTEX-FXS72", "fxoSerialGroupsDontTransmitPrefix"),
        ("ELTEX-FXS72", "fxoSerialGroupsRowStatus"),
        ("ELTEX-FXS72", "fxoSerialGroupsSend503OnBusy"),
        ("ELTEX-FXS72", "fxoSerialGroupsType"),
        ("ELTEX-FXS72", "fxsEnableAutoupdate"),
        ("ELTEX-FXS72", "fxsSource"),
        ("ELTEX-FXS72", "fxsTFTPServer"),
        ("ELTEX-FXS72", "fxsConfigurationFile"),
        ("ELTEX-FXS72", "fxsFirmwareVersion"),
        ("ELTEX-FXS72", "fxsConfigurationUpdateInterval"),
        ("ELTEX-FXS72", "fxsFirmwareUpdateInterval"),
        ("ELTEX-FXS72", "autoupdateProtocol"),
        ("ELTEX-FXS72", "autoupdateAuth"),
        ("ELTEX-FXS72", "autoupdateUser"),
        ("ELTEX-FXS72", "autoupdatePassword"),
        ("ELTEX-FXS72", "fansForceEnable"),
        ("ELTEX-FXS72", "fansThresholdTemperature"),
        ("ELTEX-FXS72", "runSyslog"),
        ("ELTEX-FXS72", "syslogAddr"),
        ("ELTEX-FXS72", "syslogPort"),
        ("ELTEX-FXS72", "appAlarm"),
        ("ELTEX-FXS72", "appErr"),
        ("ELTEX-FXS72", "appWarn"),
        ("ELTEX-FXS72", "appInfo"),
        ("ELTEX-FXS72", "appDbg"),
        ("ELTEX-FXS72", "sipLevel"),
        ("ELTEX-FXS72", "h323Level"),
        ("ELTEX-FXS72", "vapiEnabled"),
        ("ELTEX-FXS72", "vapiLibLevel"),
        ("ELTEX-FXS72", "vapiAppLevel"),
        ("ELTEX-FXS72", "portTestTestStatus"),
        ("ELTEX-FXS72", "portTestTestStartTime"),
        ("ELTEX-FXS72", "portTestLastTestStartTime"),
        ("ELTEX-FXS72", "portTestLastTestEndTime"),
        ("ELTEX-FXS72", "portTestResultFlag"),
        ("ELTEX-FXS72", "portTestRingU"),
        ("ELTEX-FXS72", "portTestTipU"),
        ("ELTEX-FXS72", "portTestShortVbat"),
        ("ELTEX-FXS72", "portTestResistTr"),
        ("ELTEX-FXS72", "portTestResistTg"),
        ("ELTEX-FXS72", "portTestResistRg"),
        ("ELTEX-FXS72", "portTestCapacityTr"),
        ("ELTEX-FXS72", "portTestCapacityTg"),
        ("ELTEX-FXS72", "portTestCapacityRg"),
        ("ELTEX-FXS72", "portTestRunTest"),
        ("ELTEX-FXS72", "monitorSerialGroupsMIBBoundary"),
        ("ELTEX-FXS72", "serialGroupPhone"),
        ("ELTEX-FXS72", "serialGroupRegistrationState"),
        ("ELTEX-FXS72", "serialGroupRegistrationHost"),
        ("ELTEX-FXS72", "serialGroupLastRegistrationAt"),
        ("ELTEX-FXS72", "serialGroupNextRegistrationAfter"),
        ("ELTEX-FXS72", "serialGroupH323GK"),
        ("ELTEX-FXS72", "fxoGroupPhone"),
        ("ELTEX-FXS72", "fxoGroupRegistrationState"),
        ("ELTEX-FXS72", "fxoGroupRegistrationHost"),
        ("ELTEX-FXS72", "fxoGroupLastRegistrationAt"),
        ("ELTEX-FXS72", "fxoGroupNextRegistrationAfter"),
        ("ELTEX-FXS72", "fxoGroupH323GK"),
        ("ELTEX-FXS72", "firewallTableMIBBoundary"),
        ("ELTEX-FXS72", "startingSourceIpAddress"),
        ("ELTEX-FXS72", "numberOfSourceIpAddresses"),
        ("ELTEX-FXS72", "allSourceIpAddresses"),
        ("ELTEX-FXS72", "ruleprotocol"),
        ("ELTEX-FXS72", "typeOfMessageICMP"),
        ("ELTEX-FXS72", "startingSourcePort"),
        ("ELTEX-FXS72", "numberOfSourcePorts"),
        ("ELTEX-FXS72", "allSourcePorts"),
        ("ELTEX-FXS72", "startingDestinationPort"),
        ("ELTEX-FXS72", "numberOfDestinationPorts"),
        ("ELTEX-FXS72", "allDestinationPorts"),
        ("ELTEX-FXS72", "ruleTarget"),
        ("ELTEX-FXS72", "ruleMoveTo"),
        ("ELTEX-FXS72", "ruleRowStatus"),
        ("ELTEX-FXS72", "firewallApply"),
        ("ELTEX-FXS72", "firewallConfirm"),
        ("ELTEX-FXS72", "megacoPortTerminationID"),
        ("ELTEX-FXS72", "megacoPortState"),
        ("ELTEX-FXS72", "megacoPortComments"),
        ("ELTEX-FXS72", "megacoPortStateStartTime"),
        ("ELTEX-FXS72", "megacoPortStateDuration"),
        ("ELTEX-FXS72", "megacoPortJitter"),
        ("ELTEX-FXS72", "megacoPortTelNo"),
        ("ELTEX-FXS72", "deviceName"),
        ("ELTEX-FXS72", "startTimer"),
        ("ELTEX-FXS72", "durationTimer"),
        ("ELTEX-FXS72", "waitAnswerTimer"),
        ("ELTEX-FXS72", "powerMode"),
        ("ELTEX-FXS72", "siptUsePrefix"),
        ("ELTEX-FXS72", "siptPrefix"),
        ("ELTEX-FXS72", "rtpSipMin"),
        ("ELTEX-FXS72", "rtpSipMax"),
        ("ELTEX-FXS72", "interceptPortMin"),
        ("ELTEX-FXS72", "interceptPortMax"),
        ("ELTEX-FXS72", "diffservForSip"),
        ("ELTEX-FXS72", "diffservForRtp"),
        ("ELTEX-FXS72", "verifyRemoteMediaAddress"),
        ("ELTEX-FXS72", "clType"),
        ("ELTEX-FXS72", "clHostOfNeighbourGateway"),
        ("ELTEX-FXS72", "clSimultaneousCallsCount"),
        ("ELTEX-FXS72", "clRowStatus"),
        ("ELTEX-FXS72", "drRule"),
        ("ELTEX-FXS72", "drRing"),
        ("ELTEX-FXS72", "drPause"),
        ("ELTEX-FXS72", "drSubscriberProfiles"),
        ("ELTEX-FXS72", "drRowStatus"),
        ("ELTEX-FXS72", "profilesSipAlertInfoMIBBoundary"),
        ("ELTEX-FXS72", "cadenceName"),
        ("ELTEX-FXS72", "cadenceRingRule"),
        ("ELTEX-FXS72", "cadenceRowStatus"),
        ("ELTEX-FXS72", "stunEnable"),
        ("ELTEX-FXS72", "stunServer"),
        ("ELTEX-FXS72", "stunInterval"),
        ("ELTEX-FXS72", "sipPublicIp"),
        ("ELTEX-FXS72", "modifierDialedNumberRegexpRule"),
        ("ELTEX-FXS72", "modifierDialedNumberModification"),
        ("ELTEX-FXS72", "modifierCallingNumberModification"),
        ("ELTEX-FXS72", "modifierRowStatus"))
)
if mibBuilder.loadTexts:
    fxsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-FXS72",
    **{"SSwStatusConv": SSwStatusConv,
       "VoltageMode": VoltageMode,
       "FXSFanState": FXSFanState,
       "BoolValue": BoolValue,
       "DevTypeString": DevTypeString,
       "FxsPortState": FxsPortState,
       "PortMegacoState": PortMegacoState,
       "PortMegacoJitter": PortMegacoJitter,
       "SipConnectState": SipConnectState,
       "FxsDialPlanType": FxsDialPlanType,
       "FxsAON": FxsAON,
       "FxsGroupSerialType": FxsGroupSerialType,
       "FxoGroupType": FxoGroupType,
       "FxsGroupBusyType": FxsGroupBusyType,
       "FxsGroupSerialEnableType": FxsGroupSerialEnableType,
       "FxsTaxophoneType": FxsTaxophoneType,
       "FxsDialPlanNatureType": FxsDialPlanNatureType,
       "FxsProcessFlashType": FxsProcessFlashType,
       "TauDialProtocolType": TauDialProtocolType,
       "ProxyMode": ProxyMode,
       "OptionsHomeServerTest": OptionsHomeServerTest,
       "AuthenticationType": AuthenticationType,
       "CwRingbackRingbackAtCallwaiting": CwRingbackRingbackAtCallwaiting,
       "RemoteRingback": RemoteRingback,
       "DTMFMIMEType": DTMFMIMEType,
       "HookFlashMIMEType": HookFlashMIMEType,
       "TypeTransport": TypeTransport,
       "Type100rel": Type100rel,
       "OutboundType": OutboundType,
       "FxoDialingType": FxoDialingType,
       "FxsToneParametrs": FxsToneParametrs,
       "TauDtmfTransferType": TauDtmfTransferType,
       "TauFlashTransferType": TauFlashTransferType,
       "TauFaxDirectionType": TauFaxDirectionType,
       "TauFaxTransferType": TauFaxTransferType,
       "TauFaxTransferSlaveType": TauFaxTransferSlaveType,
       "TauModemTransferType": TauModemTransferType,
       "TauVoiceModeType": TauVoiceModeType,
       "TauvoiceDeletionModeType": TauvoiceDeletionModeType,
       "TauTrapVersion": TauTrapVersion,
       "TauMegacoTrapVersion": TauMegacoTrapVersion,
       "TauUserViewType": TauUserViewType,
       "FxoGroupBusyType": FxoGroupBusyType,
       "FxsNetworkAutoupdateSourceType": FxsNetworkAutoupdateSourceType,
       "SipLogLevel": SipLogLevel,
       "H323LogLevel": H323LogLevel,
       "VapiLibLogLevel": VapiLibLogLevel,
       "VapiAppLogLevel": VapiAppLogLevel,
       "FxsPortTestStatus": FxsPortTestStatus,
       "FxsPortTestFlag": FxsPortTestFlag,
       "KeepAliveMode": KeepAliveMode,
       "ConferenceMode": ConferenceMode,
       "GroupRegistrationState": GroupRegistrationState,
       "FirewallProtocol": FirewallProtocol,
       "TypeOfMessageICMP": TypeOfMessageICMP,
       "FirewallTarget": FirewallTarget,
       "ReversalPolarityAction": ReversalPolarityAction,
       "CallLimitType": CallLimitType,
       "PowerMode": PowerMode,
       "DRSubscriberProfilesType": DRSubscriberProfilesType,
       "PstnActivityType": PstnActivityType,
       "IMSMode": IMSMode,
       "AutoupdateProtocolType": AutoupdateProtocolType,
       "SipProfileChangeoverType": SipProfileChangeoverType,
       "DevPowerType": DevPowerType,
       "fxs72": fxs72,
       "fxsDevName": fxsDevName,
       "fxsDevType": fxsDevType,
       "fxsDevCfgBuild": fxsDevCfgBuild,
       "fxsFreeSpace": fxsFreeSpace,
       "fxsFreeRam": fxsFreeRam,
       "fxsSSwStatus": fxsSSwStatus,
       "fxsSSwStatusTime": fxsSSwStatusTime,
       "fxsCpuUsage": fxsCpuUsage,
       "fxsMonitoring": fxsMonitoring,
       "fxsMonitoringVMode": fxsMonitoringVMode,
       "fxsMonitoringVBat": fxsMonitoringVBat,
       "fxsMonitoringVRing1": fxsMonitoringVRing1,
       "fxsMonitoringVRing2": fxsMonitoringVRing2,
       "fxsMonitoringTemp1": fxsMonitoringTemp1,
       "fxsMonitoringTemp2": fxsMonitoringTemp2,
       "fxsMonitoringTemp3": fxsMonitoringTemp3,
       "fxsMonitoringTemp4": fxsMonitoringTemp4,
       "fxsMonitoringFanState": fxsMonitoringFanState,
       "fxsMonitoringFan1Rotate": fxsMonitoringFan1Rotate,
       "fxsMonitoringFan2Rotate": fxsMonitoringFan2Rotate,
       "fxsMonitoringSubCooling": fxsMonitoringSubCooling,
       "fxsMonitoringVinput": fxsMonitoringVinput,
       "fxsMonitoringDevicePower": fxsMonitoringDevicePower,
       "fxsPortsMIBBoundary": fxsPortsMIBBoundary,
       "fxsPorts": fxsPorts,
       "fxsPortsMonitoringTable": fxsPortsMonitoringTable,
       "fxsPortsMonitoringEntry": fxsPortsMonitoringEntry,
       "fxsPortNumber": fxsPortNumber,
       "fxsPortPhoneNumber": fxsPortPhoneNumber,
       "fxsPortState": fxsPortState,
       "fxsPortUserName": fxsPortUserName,
       "fxsPortTalkingNum": fxsPortTalkingNum,
       "fxsPortTalkingStartTime": fxsPortTalkingStartTime,
       "fxsPortSipConnected": fxsPortSipConnected,
       "fxsPortH323Connected": fxsPortH323Connected,
       "fxsPortSipConnecteNext": fxsPortSipConnecteNext,
       "fxsPortSipConnecteState": fxsPortSipConnecteState,
       "fxsPortSipConnectHost": fxsPortSipConnectHost,
       "fxsPortsConfigTable": fxsPortsConfigTable,
       "fxsPortsConfigEntry": fxsPortsConfigEntry,
       "fxsPortConfigPhone": fxsPortConfigPhone,
       "fxsPortConfigUserName": fxsPortConfigUserName,
       "fxsPortConfigAuthName": fxsPortConfigAuthName,
       "fxsPortConfigAuthPass": fxsPortConfigAuthPass,
       "fxsPortConfigCustom": fxsPortConfigCustom,
       "fxsPortConfigPlaymoh": fxsPortConfigPlaymoh,
       "fxsPortConfigAON": fxsPortConfigAON,
       "fxsPortConfigAONHideDate": fxsPortConfigAONHideDate,
       "fxsPortConfigAONHideName": fxsPortConfigAONHideName,
       "fxsPortConfigTaxophone": fxsPortConfigTaxophone,
       "fxsPortConfigMinFlashtime": fxsPortConfigMinFlashtime,
       "fxsPortConfigMaxFlashtime": fxsPortConfigMaxFlashtime,
       "fxsPortConfigGainr": fxsPortConfigGainr,
       "fxsPortConfigGaint": fxsPortConfigGaint,
       "fxsPortConfigCategory": fxsPortConfigCategory,
       "fxsPortConfigCallTransfer": fxsPortConfigCallTransfer,
       "fxsPortConfigCallWaiting": fxsPortConfigCallWaiting,
       "fxsPortConfigHotLine": fxsPortConfigHotLine,
       "fxsPortConfigHotNumber": fxsPortConfigHotNumber,
       "fxsPortConfigHotTimeout": fxsPortConfigHotTimeout,
       "fxsPortConfigDisabled": fxsPortConfigDisabled,
       "fxsPortConfigCtBusy": fxsPortConfigCtBusy,
       "fxsPortConfigCtUnconditional": fxsPortConfigCtUnconditional,
       "fxsPortConfigCtNoanswer": fxsPortConfigCtNoanswer,
       "fxsPortConfigCtNumber": fxsPortConfigCtNumber,
       "fxsPortConfigCtTimeout": fxsPortConfigCtTimeout,
       "fxsPortConfigClir": fxsPortConfigClir,
       "fxsPortConfigStopDial": fxsPortConfigStopDial,
       "fxsPortConfigAltNumber": fxsPortConfigAltNumber,
       "fxsPortConfigUseAltNumber": fxsPortConfigUseAltNumber,
       "fxsPortConfigPickUp": fxsPortConfigPickUp,
       "fxsPortConfigSipPort": fxsPortConfigSipPort,
       "fxsPortConfigCfgPriOverCw": fxsPortConfigCfgPriOverCw,
       "fxsPortConfigRowStatus": fxsPortConfigRowStatus,
       "fxsPortConfigDvoCwEn": fxsPortConfigDvoCwEn,
       "fxsPortConfigDvoCtAttendedEn": fxsPortConfigDvoCtAttendedEn,
       "fxsPortConfigDvoCtUnattendedEn": fxsPortConfigDvoCtUnattendedEn,
       "fxsPortConfigDvoUnconditionalEn": fxsPortConfigDvoUnconditionalEn,
       "fxsPortConfigDvoCfBusyEn": fxsPortConfigDvoCfBusyEn,
       "fxsPortConfigDvoCfAnswerEn": fxsPortConfigDvoCfAnswerEn,
       "fxsPortConfigDvoCfServiceEn": fxsPortConfigDvoCfServiceEn,
       "fxsPortConfigDvoDoDisturbEn": fxsPortConfigDvoDoDisturbEn,
       "fxsPortConfigCtOutofservice": fxsPortConfigCtOutofservice,
       "fxsPortConfigCfuNumber": fxsPortConfigCfuNumber,
       "fxsPortConfigCfbNumber": fxsPortConfigCfbNumber,
       "fxsPortConfigCfnrNumber": fxsPortConfigCfnrNumber,
       "fxsPortConfigCfoosNumber": fxsPortConfigCfoosNumber,
       "fxsPortConfigDnd": fxsPortConfigDnd,
       "fxsPortConfigFxoFlashTime": fxsPortConfigFxoFlashTime,
       "fxsPortConfigFxoDelTdm": fxsPortConfigFxoDelTdm,
       "fxsPortConfigFxoRingtdm": fxsPortConfigFxoRingtdm,
       "fxsPortConfigPstnNumberprefix": fxsPortConfigPstnNumberprefix,
       "fxsPortConfigPstnNameprefix": fxsPortConfigPstnNameprefix,
       "fxsPortConfigUsePstnCid": fxsPortConfigUsePstnCid,
       "fxsPortConfigtdmhotline": fxsPortConfigtdmhotline,
       "fxsPortConfigtdmhottimeout": fxsPortConfigtdmhottimeout,
       "fxsPortConfigtdmhotnumber": fxsPortConfigtdmhotnumber,
       "fxsPortConfigEnableCpc": fxsPortConfigEnableCpc,
       "fxsPortConfigCpcTime": fxsPortConfigCpcTime,
       "fxsPortConfigDontDetectDT": fxsPortConfigDontDetectDT,
       "fxsPortConfigDelayDialingTimeout": fxsPortConfigDelayDialingTimeout,
       "fxsPortType": fxsPortType,
       "fxsPortConfigDialing": fxsPortConfigDialing,
       "fxsPortConfigTransmitNumber": fxsPortConfigTransmitNumber,
       "fxsPortConfigDontTransmitPrefix": fxsPortConfigDontTransmitPrefix,
       "fxsPortConfigPortProfileID": fxsPortConfigPortProfileID,
       "fxsPortConfigSipProfileID": fxsPortConfigSipProfileID,
       "fxsPortConfigDialToneDetectionParameters": fxsPortConfigDialToneDetectionParameters,
       "fxsPortConfigRingBackToneDetectionParameters": fxsPortConfigRingBackToneDetectionParameters,
       "fxsPortConfigBusyToneDetectionParameters": fxsPortConfigBusyToneDetectionParameters,
       "fxsPortConfigDtDetectTime": fxsPortConfigDtDetectTime,
       "fxsPortConfigDecadePulseTime": fxsPortConfigDecadePulseTime,
       "fxsPortConfigDecadePauseTime": fxsPortConfigDecadePauseTime,
       "fxsPortConfigNoOffhookAtRinging": fxsPortConfigNoOffhookAtRinging,
       "fxsPortConfigFxoCallBusy": fxsPortConfigFxoCallBusy,
       "fxsPortConfigCpcRus": fxsPortConfigCpcRus,
       "fxsPortConfigReversalPolarityAction": fxsPortConfigReversalPolarityAction,
       "fxsPortConfigPstnActivity": fxsPortConfigPstnActivity,
       "fxsPortConfigPstnRbDetectTimeout": fxsPortConfigPstnRbDetectTimeout,
       "fxsPortConfigDetectFxoLinePresence": fxsPortConfigDetectFxoLinePresence,
       "fxsPortConfigBlockFxoLineInOutgoingDirection": fxsPortConfigBlockFxoLineInOutgoingDirection,
       "fxsPortConfigFxoMinLevelDetect": fxsPortConfigFxoMinLevelDetect,
       "fxsPortConfigUseAltNumberAsContact": fxsPortConfigUseAltNumberAsContact,
       "fxsPortConfigModifier": fxsPortConfigModifier,
       "fxsPortConfigMwiDialtone": fxsPortConfigMwiDialtone,
       "fxsPortsConfigCommon": fxsPortsConfigCommon,
       "fxsPortConfigCommonPlaymoh": fxsPortConfigCommonPlaymoh,
       "fxsPortConfigCommonAON": fxsPortConfigCommonAON,
       "fxsPortConfigCommonAONHideDate": fxsPortConfigCommonAONHideDate,
       "fxsPortConfigCommonAONHideName": fxsPortConfigCommonAONHideName,
       "fxsPortConfigCommonTaxophone": fxsPortConfigCommonTaxophone,
       "fxsPortConfigCommonMinFlashtime": fxsPortConfigCommonMinFlashtime,
       "fxsPortConfigCommonMaxFlashtime": fxsPortConfigCommonMaxFlashtime,
       "fxsPortConfigCommonGainr": fxsPortConfigCommonGainr,
       "fxsPortConfigCommonGaint": fxsPortConfigCommonGaint,
       "fxsPortConfigCommonCategory": fxsPortConfigCommonCategory,
       "fxsPortConfigCommonCallTransfer": fxsPortConfigCommonCallTransfer,
       "fxsPortConfigCommonCallWaiting": fxsPortConfigCommonCallWaiting,
       "fxsPortConfigCommonCfgPriOverCw": fxsPortConfigCommonCfgPriOverCw,
       "fxsPortConfigCommonFxoFlashTime": fxsPortConfigCommonFxoFlashTime,
       "fxsPortConfigCommonFxoDelTdm": fxsPortConfigCommonFxoDelTdm,
       "fxsPortConfigCommonFxoRingtdm": fxsPortConfigCommonFxoRingtdm,
       "fxsPortConfigCommonPstnNumberprefix": fxsPortConfigCommonPstnNumberprefix,
       "fxsPortConfigCommonPstnNameprefix": fxsPortConfigCommonPstnNameprefix,
       "fxsPortConfigCommonUsePstnCid": fxsPortConfigCommonUsePstnCid,
       "fxsPortConfigCommonEnableCpc": fxsPortConfigCommonEnableCpc,
       "fxsPortConfigCommonCpcTime": fxsPortConfigCommonCpcTime,
       "fxsPortConfigCommonDontDetectDT": fxsPortConfigCommonDontDetectDT,
       "fxsPortConfigCommonDelayDialingTimeout": fxsPortConfigCommonDelayDialingTimeout,
       "fxsPortConfigCommonDialing": fxsPortConfigCommonDialing,
       "fxsPortConfigCommonTransmitNumber": fxsPortConfigCommonTransmitNumber,
       "fxsPortConfigCommonDontTransmitPrefix": fxsPortConfigCommonDontTransmitPrefix,
       "megacoPortsMonitoringTable": megacoPortsMonitoringTable,
       "megacoPortsMonitoringEntry": megacoPortsMonitoringEntry,
       "megacoPortNumber": megacoPortNumber,
       "megacoPortTerminationID": megacoPortTerminationID,
       "megacoPortComments": megacoPortComments,
       "megacoPortState": megacoPortState,
       "megacoPortStateStartTime": megacoPortStateStartTime,
       "megacoPortStateDuration": megacoPortStateDuration,
       "megacoPortJitter": megacoPortJitter,
       "megacoPortTelNo": megacoPortTelNo,
       "fxsDialMIBBoundary": fxsDialMIBBoundary,
       "fxsDial": fxsDial,
       "fxsDialPlanTable": fxsDialPlanTable,
       "fxsDialPlanEntry": fxsDialPlanEntry,
       "fxsDialPlanHost": fxsDialPlanHost,
       "fxsDialPlanDigits": fxsDialPlanDigits,
       "fxsDialPlanTimeout": fxsDialPlanTimeout,
       "fxsDialPlanMinDigits": fxsDialPlanMinDigits,
       "fxsDialPlanType": fxsDialPlanType,
       "fxsDialPlanAccessMask": fxsDialPlanAccessMask,
       "fxsDialPlanDialtone": fxsDialPlanDialtone,
       "fxsDialPlanModifier": fxsDialPlanModifier,
       "fxsDialPlanNature": fxsDialPlanNature,
       "fxsDialPlanDelnum": fxsDialPlanDelnum,
       "fxsDialPlanPtime": fxsDialPlanPtime,
       "fxsDialRowStatus": fxsDialRowStatus,
       "fxsDialPlanNumber": fxsDialPlanNumber,
       "fxsDialPlanNext": fxsDialPlanNext,
       "tauDialPlansRegExp": tauDialPlansRegExp,
       "tauDialRegularOn": tauDialRegularOn,
       "tauDialRegularProtocol": tauDialRegularProtocol,
       "tauDialRegularText": tauDialRegularText,
       "fxsConfigSave": fxsConfigSave,
       "fxsConfigApply": fxsConfigApply,
       "fxsSerialGroupsMIBBoundary": fxsSerialGroupsMIBBoundary,
       "fxsSerialGroups": fxsSerialGroups,
       "fxsSerialGroupsTable": fxsSerialGroupsTable,
       "fxsSerialGroupsEntry": fxsSerialGroupsEntry,
       "fxsSerialGroupsPhone": fxsSerialGroupsPhone,
       "fxsSerialGroupsEnabled": fxsSerialGroupsEnabled,
       "fxsSerialGroupsSerialType": fxsSerialGroupsSerialType,
       "fxsSerialGroupsBusyType": fxsSerialGroupsBusyType,
       "fxsSerialGroupsTimeout": fxsSerialGroupsTimeout,
       "fxsSerialGroupsSipPort": fxsSerialGroupsSipPort,
       "fxsSerialGroupsAuthName": fxsSerialGroupsAuthName,
       "fxsSerialGroupsAuthPass": fxsSerialGroupsAuthPass,
       "fxsSerialGroupsPorts": fxsSerialGroupsPorts,
       "fxsSerialGroupsSipProfile": fxsSerialGroupsSipProfile,
       "fxsSerialGroupsRowStatus": fxsSerialGroupsRowStatus,
       "fxsSerialGroupsNextEmpty": fxsSerialGroupsNextEmpty,
       "fxsReboot": fxsReboot,
       "tauVoipDvo": tauVoipDvo,
       "tauVoipDvoCallwaiting": tauVoipDvoCallwaiting,
       "tauVoipDvoCtAttended": tauVoipDvoCtAttended,
       "tauVoipDvoCtUnattended": tauVoipDvoCtUnattended,
       "tauVoipDvoCfUnconditional": tauVoipDvoCfUnconditional,
       "tauVoipDvoCfBusy": tauVoipDvoCfBusy,
       "tauVoipDvoCfNoanswer": tauVoipDvoCfNoanswer,
       "tauVoipDvoCfService": tauVoipDvoCfService,
       "tauVoipDvoDoDisturb": tauVoipDvoDoDisturb,
       "tauSipConfig": tauSipConfig,
       "sipEnablesip": sipEnablesip,
       "sipObtimeout": sipObtimeout,
       "sipMode": sipMode,
       "sipOptions": sipOptions,
       "sipKeepalivet": sipKeepalivet,
       "sipDomainToReg": sipDomainToReg,
       "sipDomain": sipDomain,
       "sipRegisterRetryInterval": sipRegisterRetryInterval,
       "sipOutbound": sipOutbound,
       "sipInboundProxy": sipInboundProxy,
       "sipExpires": sipExpires,
       "sipAuthentication": sipAuthentication,
       "sipUsername": sipUsername,
       "sipPassword": sipPassword,
       "sipProxy0": sipProxy0,
       "sipRegrar0": sipRegrar0,
       "sipRegistration0": sipRegistration0,
       "sipProxy1": sipProxy1,
       "sipRegrar1": sipRegrar1,
       "sipProxy2": sipProxy2,
       "sipRegrar2": sipRegrar2,
       "sipProxy3": sipProxy3,
       "sipRegrar3": sipRegrar3,
       "sipProxy4": sipProxy4,
       "sipRegrar4": sipRegrar4,
       "sipDtmfmime": sipDtmfmime,
       "sipHfmime": sipHfmime,
       "sipCtWithReplaces": sipCtWithReplaces,
       "sipShortmode": sipShortmode,
       "sipTransport": sipTransport,
       "sipSipMtu": sipSipMtu,
       "sip100Rel": sip100Rel,
       "sipUserPhone": sipUserPhone,
       "sipUriEscapeHash": sipUriEscapeHash,
       "sipInviteTotalT": sipInviteTotalT,
       "sipInviteInitT": sipInviteInitT,
       "sipCwRingback": sipCwRingback,
       "sipRingbackSdp": sipRingbackSdp,
       "sipRingback": sipRingback,
       "sipRegistration1": sipRegistration1,
       "sipRegistration2": sipRegistration2,
       "sipRegistration3": sipRegistration3,
       "sipRegistration4": sipRegistration4,
       "sipPRTPstat": sipPRTPstat,
       "fxsStatTable": fxsStatTable,
       "fxsStatEntry": fxsStatEntry,
       "termID": termID,
       "currentState": currentState,
       "totalCallCount": totalCallCount,
       "lastCallPhone": lastCallPhone,
       "peakJitter": peakJitter,
       "lostPackets": lostPackets,
       "numTxPack": numTxPack,
       "numTxOct": numTxOct,
       "numRxPack": numRxPack,
       "numRxOct": numRxOct,
       "fxsUpdateFw": fxsUpdateFw,
       "fxsProfiles": fxsProfiles,
       "profilesSip": profilesSip,
       "profilesSipCommon": profilesSipCommon,
       "sipCommonEnablesip": sipCommonEnablesip,
       "sipCommonShortmode": sipCommonShortmode,
       "sipCommonTransport": sipCommonTransport,
       "sipCommonSipMtu": sipCommonSipMtu,
       "sipCommonInviteTotalT": sipCommonInviteTotalT,
       "sipCommonInviteInitT": sipCommonInviteInitT,
       "sipCommonPortRegistrationDelay": sipCommonPortRegistrationDelay,
       "stunEnable": stunEnable,
       "stunServer": stunServer,
       "stunInterval": stunInterval,
       "sipPublicIp": sipPublicIp,
       "profilesSipMIBBoundary": profilesSipMIBBoundary,
       "profilesSipTable": profilesSipTable,
       "profilesSipEntry": profilesSipEntry,
       "profileNumber": profileNumber,
       "sipProfileObtimeout": sipProfileObtimeout,
       "sipProfileMode": sipProfileMode,
       "sipProfileOptions": sipProfileOptions,
       "sipProfileKeepalivet": sipProfileKeepalivet,
       "sipProfileDomainToReg": sipProfileDomainToReg,
       "sipProfileDomain": sipProfileDomain,
       "sipProfileRegisterRetryInterval": sipProfileRegisterRetryInterval,
       "sipProfileOutbound": sipProfileOutbound,
       "sipProfileInboundProxy": sipProfileInboundProxy,
       "sipProfileExpires": sipProfileExpires,
       "sipProfileAuthentication": sipProfileAuthentication,
       "sipProfileUsername": sipProfileUsername,
       "sipProfilePassword": sipProfilePassword,
       "sipProfileProxy0": sipProfileProxy0,
       "sipProfileRegrar0": sipProfileRegrar0,
       "sipProfileRegistration0": sipProfileRegistration0,
       "sipProfileProxy1": sipProfileProxy1,
       "sipProfileRegrar1": sipProfileRegrar1,
       "sipProfileProxy2": sipProfileProxy2,
       "sipProfileRegrar2": sipProfileRegrar2,
       "sipProfileProxy3": sipProfileProxy3,
       "sipProfileRegrar3": sipProfileRegrar3,
       "sipProfileProxy4": sipProfileProxy4,
       "sipProfileRegrar4": sipProfileRegrar4,
       "sipProfileDtmfmime": sipProfileDtmfmime,
       "sipProfileHfmime": sipProfileHfmime,
       "sipProfileCtWithReplaces": sipProfileCtWithReplaces,
       "sipProfile100Rel": sipProfile100Rel,
       "sipProfileUserPhone": sipProfileUserPhone,
       "sipProfileUriEscapeHash": sipProfileUriEscapeHash,
       "sipProfileCwRingback": sipProfileCwRingback,
       "sipProfileRingbackSdp": sipProfileRingbackSdp,
       "sipProfileRingback": sipProfileRingback,
       "sipProfileRegistration1": sipProfileRegistration1,
       "sipProfileRegistration2": sipProfileRegistration2,
       "sipProfileRegistration3": sipProfileRegistration3,
       "sipProfileRegistration4": sipProfileRegistration4,
       "sipProfilePRTPstat": sipProfilePRTPstat,
       "sipProfileRowStatus": sipProfileRowStatus,
       "sipProfileEnableTimer": sipProfileEnableTimer,
       "sipProfileMinSE": sipProfileMinSE,
       "sipProfileSessionExpires": sipProfileSessionExpires,
       "sipProfileRemoveInactiveMedia": sipProfileRemoveInactiveMedia,
       "sipProfileKeepAliveInterval": sipProfileKeepAliveInterval,
       "sipProfileKeepAliveMode": sipProfileKeepAliveMode,
       "sipProfileConferenceMode": sipProfileConferenceMode,
       "sipProfileConferenceServer": sipProfileConferenceServer,
       "sipProfileEnableIMS": sipProfileEnableIMS,
       "sipProfileXCAPNameForThreePartyConference": sipProfileXCAPNameForThreePartyConference,
       "sipProfileXCAPNameForHotline": sipProfileXCAPNameForHotline,
       "sipProfileXCAPNameForCallWaiting": sipProfileXCAPNameForCallWaiting,
       "sipProfileXCAPNameForCallHold": sipProfileXCAPNameForCallHold,
       "sipProfileXCAPNameForExplicitCallTransfer": sipProfileXCAPNameForExplicitCallTransfer,
       "sipProfileUseAlertInfo": sipProfileUseAlertInfo,
       "sipProfileFullRuriCompliance": sipProfileFullRuriCompliance,
       "sipProfileChangeover": sipProfileChangeover,
       "profilesSipAlertInfoMIBBoundary": profilesSipAlertInfoMIBBoundary,
       "profilesSipAlertInfoTable": profilesSipAlertInfoTable,
       "profilesSipAlertInfoEntry": profilesSipAlertInfoEntry,
       "cadenceNumber": cadenceNumber,
       "cadenceName": cadenceName,
       "cadenceRingRule": cadenceRingRule,
       "cadenceRowStatus": cadenceRowStatus,
       "profilesPortsMIBBoundary": profilesPortsMIBBoundary,
       "profilesPorts": profilesPorts,
       "profilesPortsTable": profilesPortsTable,
       "profilesPortsEntry": profilesPortsEntry,
       "profilePortsPlaymoh": profilePortsPlaymoh,
       "profilePortsAON": profilePortsAON,
       "profilePortsAONHideDate": profilePortsAONHideDate,
       "profilePortsAONHideName": profilePortsAONHideName,
       "profilePortsTaxophone": profilePortsTaxophone,
       "profilePortsMinFlashtime": profilePortsMinFlashtime,
       "profilePortsMaxFlashtime": profilePortsMaxFlashtime,
       "profilePortsGainr": profilePortsGainr,
       "profilePortsGaint": profilePortsGaint,
       "profilePortsCategory": profilePortsCategory,
       "profilePortsCallTransfer": profilePortsCallTransfer,
       "profilePortsCallWaiting": profilePortsCallWaiting,
       "profilePortsCfgPriOverCw": profilePortsCfgPriOverCw,
       "profilePortsFxoFlashTime": profilePortsFxoFlashTime,
       "profilePortsFxoDelTdm": profilePortsFxoDelTdm,
       "profilePortsFxoRingtdm": profilePortsFxoRingtdm,
       "profilePortsPstnNumberprefix": profilePortsPstnNumberprefix,
       "profilePortsPstnNameprefix": profilePortsPstnNameprefix,
       "profilePortsUsePstnCid": profilePortsUsePstnCid,
       "profilePortsEnableCpc": profilePortsEnableCpc,
       "profilePortsCpcTime": profilePortsCpcTime,
       "profilePortsDontDetectDT": profilePortsDontDetectDT,
       "profilePortsDelayDialingTimeout": profilePortsDelayDialingTimeout,
       "profilePortsDialing": profilePortsDialing,
       "profilePortsTransmitNumber": profilePortsTransmitNumber,
       "profilePortsDontTransmitPrefix": profilePortsDontTransmitPrefix,
       "profilePortsRowStatus": profilePortsRowStatus,
       "profilePortsDialToneDetectionParameters": profilePortsDialToneDetectionParameters,
       "profilePortsRingBackToneDetectionParameters": profilePortsRingBackToneDetectionParameters,
       "profilePortsBusyToneDetectionParameters": profilePortsBusyToneDetectionParameters,
       "profilePortsDtDetectTime": profilePortsDtDetectTime,
       "profilePortsDecadePulseTime": profilePortsDecadePulseTime,
       "profilePortsDecadePauseTime": profilePortsDecadePauseTime,
       "profilePortsFxoCallBusy": profilePortsFxoCallBusy,
       "profilePortsCpcRus": profilePortsCpcRus,
       "profilePortsReversalPolarityAction": profilePortsReversalPolarityAction,
       "profilePortsPstnActivity": profilePortsPstnActivity,
       "profilePortsPstnRbDetectTimeout": profilePortsPstnRbDetectTimeout,
       "profilePortsDetectFxoLinePresence": profilePortsDetectFxoLinePresence,
       "profilePortsBlockFxoLineInOutgoingDirection": profilePortsBlockFxoLineInOutgoingDirection,
       "profilePortsStopDial": profilePortsStopDial,
       "profilePortsFxoMinLevelDetect": profilePortsFxoMinLevelDetect,
       "profilePortsModifier": profilePortsModifier,
       "profilesDialPlansMIBBoundary": profilesDialPlansMIBBoundary,
       "profilesDialPlans": profilesDialPlans,
       "profilesDialPlansTable": profilesDialPlansTable,
       "profilesDialPlansEntry": profilesDialPlansEntry,
       "profileDialPlanHost": profileDialPlanHost,
       "profileDialPlanDigits": profileDialPlanDigits,
       "profileDialPlanTimeout": profileDialPlanTimeout,
       "profileDialPlanMinDigits": profileDialPlanMinDigits,
       "profileDialPlanType": profileDialPlanType,
       "profileDialPlanAccessMask": profileDialPlanAccessMask,
       "profileDialPlanDialtone": profileDialPlanDialtone,
       "profileDialPlanModifier": profileDialPlanModifier,
       "profileDialPlanNature": profileDialPlanNature,
       "profileDialPlanDelnum": profileDialPlanDelnum,
       "profileDialPlanPtime": profileDialPlanPtime,
       "profileDialRowStatus": profileDialRowStatus,
       "profileDialPlanNumber": profileDialPlanNumber,
       "profilesRegExpDPTableMIBBoundary": profilesRegExpDPTableMIBBoundary,
       "profilesRegExpDPTable": profilesRegExpDPTable,
       "profilesRegExpDPEntry": profilesRegExpDPEntry,
       "profileRegExpDialOn": profileRegExpDialOn,
       "profileRegExpDialProtocol": profileRegExpDialProtocol,
       "profileRegExpDialText": profileRegExpDialText,
       "profileRegExpDialRowStatus": profileRegExpDialRowStatus,
       "profilesCodecs": profilesCodecs,
       "profilesCodecsTable": profilesCodecsTable,
       "profilesCodecsEntry": profilesCodecsEntry,
       "useG711A": useG711A,
       "useG711U": useG711U,
       "useG726to32": useG726to32,
       "useG723": useG723,
       "useG729B": useG729B,
       "useG729A": useG729A,
       "g711Ptime": g711Ptime,
       "g729Ptime": g729Ptime,
       "g723Ptime": g723Ptime,
       "g726to32Ptime": g726to32Ptime,
       "g726to32PT": g726to32PT,
       "dtmfTransfer": dtmfTransfer,
       "flashTransfer": flashTransfer,
       "faxDetectDirection": faxDetectDirection,
       "faxTransferCodec": faxTransferCodec,
       "slaveFaxTransferCodec": slaveFaxTransferCodec,
       "modemTransfer": modemTransfer,
       "rfc2833PT": rfc2833PT,
       "silenceSuppression": silenceSuppression,
       "echoCanceller": echoCanceller,
       "nlpDisable": nlpDisable,
       "comfortNoise": comfortNoise,
       "rtcpTimer": rtcpTimer,
       "rtcpControlPeriod": rtcpControlPeriod,
       "ciscoNsePT": ciscoNsePT,
       "t38MaxDatagramSize": t38MaxDatagramSize,
       "t38Bitrate": t38Bitrate,
       "modemFaxDelay": modemFaxDelay,
       "voiceMode": voiceMode,
       "voiceDelayMin": voiceDelayMin,
       "voiceDelayMax": voiceDelayMax,
       "voiceDeletionThreshold": voiceDeletionThreshold,
       "voiceDeletionMode": voiceDeletionMode,
       "profilesCodecsRowStatus": profilesCodecsRowStatus,
       "rtcpXR": rtcpXR,
       "rfc3264PtCommon": rfc3264PtCommon,
       "tauSnmpConfiguration": tauSnmpConfiguration,
       "tauTrapSink": tauTrapSink,
       "tauTrapType": tauTrapType,
       "tauSysName": tauSysName,
       "tauSysContact": tauSysContact,
       "tauSysLocation": tauSysLocation,
       "tauRoCommunity": tauRoCommunity,
       "tauRwCommunity": tauRwCommunity,
       "tauTrapCommunity": tauTrapCommunity,
       "tauUserV3Name": tauUserV3Name,
       "tauUserV3Password": tauUserV3Password,
       "tauViewV3Type": tauViewV3Type,
       "tauRestartSnmp": tauRestartSnmp,
       "tauMegacoTrapsTable": tauMegacoTrapsTable,
       "tauMegacoTrapsEntry": tauMegacoTrapsEntry,
       "tauMegacoTrapId": tauMegacoTrapId,
       "tauMegacoTrapType": tauMegacoTrapType,
       "tauMegacoTrapHost": tauMegacoTrapHost,
       "tauMegacoTrapCommunity": tauMegacoTrapCommunity,
       "tauMegacoTrapPort": tauMegacoTrapPort,
       "tauMegacoTrapRowStatus": tauMegacoTrapRowStatus,
       "fxoSerialGroups": fxoSerialGroups,
       "fxoSerialGroupsTable": fxoSerialGroupsTable,
       "fxoSerialGroupsEntry": fxoSerialGroupsEntry,
       "fxoSerialGroupsPhone": fxoSerialGroupsPhone,
       "fxoSerialGroupsEnabled": fxoSerialGroupsEnabled,
       "fxoSerialGroupsBusyType": fxoSerialGroupsBusyType,
       "fxoSerialGroupsSipPort": fxoSerialGroupsSipPort,
       "fxoSerialGroupsAuthName": fxoSerialGroupsAuthName,
       "fxoSerialGroupsAuthPass": fxoSerialGroupsAuthPass,
       "fxoSerialGroupsPorts": fxoSerialGroupsPorts,
       "fxoSerialGroupsSipProfile": fxoSerialGroupsSipProfile,
       "fxoSerialGroupsTransmitNumber": fxoSerialGroupsTransmitNumber,
       "fxoSerialGroupsDontTransmitPrefix": fxoSerialGroupsDontTransmitPrefix,
       "fxoSerialGroupsRowStatus": fxoSerialGroupsRowStatus,
       "fxoSerialGroupsSend503OnBusy": fxoSerialGroupsSend503OnBusy,
       "fxoSerialGroupsType": fxoSerialGroupsType,
       "fxsNetwork": fxsNetwork,
       "fxsAutoupdateSettings": fxsAutoupdateSettings,
       "fxsEnableAutoupdate": fxsEnableAutoupdate,
       "fxsSource": fxsSource,
       "fxsTFTPServer": fxsTFTPServer,
       "fxsConfigurationFile": fxsConfigurationFile,
       "fxsFirmwareVersion": fxsFirmwareVersion,
       "fxsConfigurationUpdateInterval": fxsConfigurationUpdateInterval,
       "fxsFirmwareUpdateInterval": fxsFirmwareUpdateInterval,
       "autoupdateProtocol": autoupdateProtocol,
       "autoupdateAuth": autoupdateAuth,
       "autoupdateUser": autoupdateUser,
       "autoupdatePassword": autoupdatePassword,
       "fxsVoipGeneral": fxsVoipGeneral,
       "fansForceEnable": fansForceEnable,
       "fansThresholdTemperature": fansThresholdTemperature,
       "deviceName": deviceName,
       "startTimer": startTimer,
       "durationTimer": durationTimer,
       "waitAnswerTimer": waitAnswerTimer,
       "powerMode": powerMode,
       "siptUsePrefix": siptUsePrefix,
       "siptPrefix": siptPrefix,
       "fxsSyslog": fxsSyslog,
       "runSyslog": runSyslog,
       "syslogAddr": syslogAddr,
       "syslogPort": syslogPort,
       "appErr": appErr,
       "appWarn": appWarn,
       "appInfo": appInfo,
       "appDbg": appDbg,
       "sipLevel": sipLevel,
       "h323Level": h323Level,
       "vapiEnabled": vapiEnabled,
       "vapiLibLevel": vapiLibLevel,
       "vapiAppLevel": vapiAppLevel,
       "appAlarm": appAlarm,
       "testPortsTable": testPortsTable,
       "testPortsTableEntry": testPortsTableEntry,
       "portTestTestStatus": portTestTestStatus,
       "portTestTestStartTime": portTestTestStartTime,
       "portTestLastTestStartTime": portTestLastTestStartTime,
       "portTestLastTestEndTime": portTestLastTestEndTime,
       "portTestResultFlag": portTestResultFlag,
       "portTestRingU": portTestRingU,
       "portTestTipU": portTestTipU,
       "portTestShortVbat": portTestShortVbat,
       "portTestResistTr": portTestResistTr,
       "portTestResistTg": portTestResistTg,
       "portTestResistRg": portTestResistRg,
       "portTestCapacityTr": portTestCapacityTr,
       "portTestCapacityTg": portTestCapacityTg,
       "portTestCapacityRg": portTestCapacityRg,
       "portTestRunTest": portTestRunTest,
       "monitorSerialGroupsMIBBoundary": monitorSerialGroupsMIBBoundary,
       "monitorSerialGroupsTable": monitorSerialGroupsTable,
       "monitorSerialGroupsEntry": monitorSerialGroupsEntry,
       "serialGroupNumber": serialGroupNumber,
       "serialGroupPhone": serialGroupPhone,
       "serialGroupRegistrationState": serialGroupRegistrationState,
       "serialGroupRegistrationHost": serialGroupRegistrationHost,
       "serialGroupLastRegistrationAt": serialGroupLastRegistrationAt,
       "serialGroupNextRegistrationAfter": serialGroupNextRegistrationAfter,
       "serialGroupH323GK": serialGroupH323GK,
       "monitorFxoGroupsTable": monitorFxoGroupsTable,
       "monitorFxoGroupsEntry": monitorFxoGroupsEntry,
       "fxoGroupNumber": fxoGroupNumber,
       "fxoGroupPhone": fxoGroupPhone,
       "fxoGroupRegistrationState": fxoGroupRegistrationState,
       "fxoGroupRegistrationHost": fxoGroupRegistrationHost,
       "fxoGroupLastRegistrationAt": fxoGroupLastRegistrationAt,
       "fxoGroupNextRegistrationAfter": fxoGroupNextRegistrationAfter,
       "fxoGroupH323GK": fxoGroupH323GK,
       "firewallTableMIBBoundary": firewallTableMIBBoundary,
       "firewallConfig": firewallConfig,
       "firewallTable": firewallTable,
       "firewallEntry": firewallEntry,
       "ruleNumber": ruleNumber,
       "startingSourceIpAddress": startingSourceIpAddress,
       "numberOfSourceIpAddresses": numberOfSourceIpAddresses,
       "allSourceIpAddresses": allSourceIpAddresses,
       "ruleprotocol": ruleprotocol,
       "typeOfMessageICMP": typeOfMessageICMP,
       "startingSourcePort": startingSourcePort,
       "numberOfSourcePorts": numberOfSourcePorts,
       "allSourcePorts": allSourcePorts,
       "startingDestinationPort": startingDestinationPort,
       "numberOfDestinationPorts": numberOfDestinationPorts,
       "allDestinationPorts": allDestinationPorts,
       "ruleTarget": ruleTarget,
       "ruleMoveTo": ruleMoveTo,
       "ruleRowStatus": ruleRowStatus,
       "firewallApply": firewallApply,
       "firewallConfirm": firewallConfirm,
       "configTcpIp": configTcpIp,
       "rtpSipMin": rtpSipMin,
       "rtpSipMax": rtpSipMax,
       "interceptPortMin": interceptPortMin,
       "interceptPortMax": interceptPortMax,
       "diffservForSip": diffservForSip,
       "diffservForRtp": diffservForRtp,
       "verifyRemoteMediaAddress": verifyRemoteMediaAddress,
       "callLimitTable": callLimitTable,
       "callLimitEntry": callLimitEntry,
       "clIndex": clIndex,
       "clType": clType,
       "clHostOfNeighbourGateway": clHostOfNeighbourGateway,
       "clSimultaneousCallsCount": clSimultaneousCallsCount,
       "clRowStatus": clRowStatus,
       "distinctiveRingTable": distinctiveRingTable,
       "distinctiveRingEntry": distinctiveRingEntry,
       "drId": drId,
       "drRule": drRule,
       "drRing": drRing,
       "drPause": drPause,
       "drSubscriberProfiles": drSubscriberProfiles,
       "drRowStatus": drRowStatus,
       "modifiersTable": modifiersTable,
       "modifiersEntry": modifiersEntry,
       "modifierNumber": modifierNumber,
       "modifierRule": modifierRule,
       "modifierDialedNumberRegexpRule": modifierDialedNumberRegexpRule,
       "modifierDialedNumberModification": modifierDialedNumberModification,
       "modifierCallingNumberModification": modifierCallingNumberModification,
       "modifierRowStatus": modifierRowStatus,
       "tauSubtypes": tauSubtypes,
       "tau72sip": tau72sip,
       "tau36sip": tau36sip,
       "tau32Msip": tau32Msip,
       "tau72megaco": tau72megaco,
       "tau72v30sip": tau72v30sip,
       "tau36v30sip": tau36v30sip,
       "fxs72sip": fxs72sip,
       "tau36megaco": tau36megaco,
       "tau72v30megaco": tau72v30megaco,
       "tau36v30megaco": tau36v30megaco,
       "fxs72megaco": fxs72megaco,
       "fxs72v21": fxs72v21,
       "tau72v40sip": tau72v40sip,
       "tau36v40sip": tau36v40sip,
       "tau72v40megaco": tau72v40megaco,
       "tau36v40megaco": tau36v40megaco,
       "tau32MrevBsip": tau32MrevBsip,
       "tau32Mmegaco": tau32Mmegaco,
       "tau32MrevBmegaco": tau32MrevBmegaco,
       "tau16sip": tau16sip,
       "tau24sip": tau24sip,
       "tau16megaco": tau16megaco,
       "tau24megaco": tau24megaco,
       "fxsGroup": fxsGroup}
)
