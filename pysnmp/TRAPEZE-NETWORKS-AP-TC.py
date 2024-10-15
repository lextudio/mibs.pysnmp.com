# SNMP MIB module (TRAPEZE-NETWORKS-AP-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-AP-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:25 2024
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

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzApTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 3)
)
trpzApTc.setRevisions(
        ("2011-10-05 02:32",
         "2011-01-28 02:20",
         "2011-01-28 02:10",
         "2010-11-30 02:01",
         "2010-11-29 01:31",
         "2009-07-21 01:03",
         "2008-12-02 01:01",
         "2008-11-27 01:00",
         "2008-11-26 00:51",
         "2008-10-06 00:50",
         "2008-05-07 00:41",
         "2008-02-14 00:32",
         "2007-12-03 00:30",
         "2007-07-06 00:23",
         "2007-07-05 00:22",
         "2006-07-10 00:15",
         "2006-03-30 00:14")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzAccessType(Integer32, TextualConvention):
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
        *(("ap", 1),
          ("dap", 2),
          ("wired", 3))
    )



class TrpzApAttachType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directAttach", 1),
          ("networkAttach", 2))
    )



class TrpzApPortOrDapNum(Unsigned32, TextualConvention):
    status = "obsolete"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class TrpzApNum(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )



class TrpzApState(Integer32, TextualConvention):
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
              10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("bootStarted", 3),
          ("cleared", 1),
          ("configuring", 6),
          ("connOutage", 20),
          ("connectFailed", 5),
          ("imageDownloaded", 4),
          ("init", 2),
          ("operational", 7),
          ("redundant", 10))
    )



class TrpzApTransition(Integer32, TextualConvention):
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
              10,
              11,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("bootSuccess", 4),
          ("clear", 1),
          ("connLost", 20),
          ("connOutageExtendedTimeout", 22),
          ("connRestored", 21),
          ("connectFail", 6),
          ("reset", 3),
          ("setBackupConn", 10),
          ("startConfiguring", 5),
          ("startHandoverReconfiguring", 11),
          ("timeout", 2))
    )



class TrpzApFailDetail(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              11,
              12,
              91,
              92,
              99)
        )
    )
    namedValues = NamedValues(
        *(("adminRequest", 92),
          ("failUnknown", 99),
          ("fingerprintMismatch", 4),
          ("fingerprintRequired", 3),
          ("normalTransition", 91),
          ("portLinkDown", 12),
          ("portLinkUp", 11),
          ("secureHandshakeFailure", 2))
    )



class TrpzApConnectSecurityType(Integer32, TextualConvention):
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
        *(("auto", 3),
          ("insecure", 2),
          ("secure", 1))
    )



class TrpzApServiceAvailability(Integer32, TextualConvention):
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
        *(("degradedService", 3),
          ("fullService", 1),
          ("noService", 2))
    )



class TrpzApBias(Integer32, TextualConvention):
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
          ("low", 2),
          ("sticky", 3))
    )



class TrpzApSerialNum(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TrpzApFingerprint(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )



class TrpzRadioNum(Integer32, TextualConvention):
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
        *(("not-applicable", 3),
          ("radio-1", 1),
          ("radio-2", 2))
    )



class TrpzApRadioIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class TrpzApRadioIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class TrpzPowerLevel(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class TrpzRadioPowerChangeType(Integer32, TextualConvention):
    status = "current"
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
        *(("clients-optimal-performance-reached", 3),
          ("def-power-threshold-exceed", 4),
          ("dup-pkts-threshold-exceed", 1),
          ("retransmit-threshold-exceed", 2))
    )



class TrpzChannelChangeType(Integer32, TextualConvention):
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
        *(("crc-errors-offset", 7),
          ("noise", 4),
          ("noise-offset", 3),
          ("phy-error-offset", 6),
          ("radar-detected", 8),
          ("rexmit-pkt-offset", 2),
          ("util-index", 1),
          ("utilization", 5))
    )



class TrpzChannelNum(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



class TrpzRadioEnable(Integer32, TextualConvention):
    status = "obsolete"
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



class TrpzRadioMode(Integer32, TextualConvention):
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
        *(("disabled", 2),
          ("enabled", 1),
          ("sentry", 3))
    )



class TrpzRadioConfigState(Integer32, TextualConvention):
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
        *(("configFail", 2),
          ("configInit", 1),
          ("configOk", 3))
    )



class TrpzRadioRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 540),
    )



class TrpzRadioRateEx(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
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
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("rate1", 2),
          ("rate11", 7),
          ("rate12", 8),
          ("rate18", 9),
          ("rate2", 3),
          ("rate24", 10),
          ("rate36", 11),
          ("rate48", 12),
          ("rate5-5", 4),
          ("rate54", 13),
          ("rate6", 5),
          ("rate9", 6),
          ("rateMCS0", 20),
          ("rateMCS1", 21),
          ("rateMCS10", 30),
          ("rateMCS11", 31),
          ("rateMCS12", 32),
          ("rateMCS13", 33),
          ("rateMCS14", 34),
          ("rateMCS15", 35),
          ("rateMCS16", 36),
          ("rateMCS17", 37),
          ("rateMCS18", 38),
          ("rateMCS19", 39),
          ("rateMCS2", 22),
          ("rateMCS20", 40),
          ("rateMCS21", 41),
          ("rateMCS22", 42),
          ("rateMCS23", 43),
          ("rateMCS3", 23),
          ("rateMCS4", 24),
          ("rateMCS5", 25),
          ("rateMCS6", 26),
          ("rateMCS7", 27),
          ("rateMCS8", 28),
          ("rateMCS9", 29),
          ("rateUnknown", 1))
    )



class TrpzRadioType(Integer32, TextualConvention):
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
        *(("typeA", 2),
          ("typeB", 3),
          ("typeG", 4),
          ("typeNA", 5),
          ("typeNG", 6),
          ("typeUnknown", 1))
    )



class TrpzRssi(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )



class TrpzApWasOperational(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonOper", 2),
          ("oper", 1))
    )



class TrpzRadioChannelWidth(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelWidth20MHz", 1),
          ("channelWidth40MHz", 2))
    )



class TrpzRadioMimoState(Integer32, TextualConvention):
    status = "current"
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
        *(("mimo1x1", 2),
          ("mimo2x3", 3),
          ("mimo3x3", 4),
          ("mimoOther", 1))
    )



class TrpzApPowerMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("high", 2))
    )



class TrpzApLedMode(Integer32, TextualConvention):
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
        *(("auto", 1),
          ("off", 3),
          ("static", 2))
    )



class TrpzRadioAntennaLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoors", 1),
          ("outdoors", 2))
    )



class TrpzCryptoType(Integer32, TextualConvention):
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
        *(("aesCcmp", 7),
          ("clear", 2),
          ("other", 1),
          ("sms4", 8),
          ("tkip", 6),
          ("wep", 3),
          ("wep104", 5),
          ("wep40", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    **{"TrpzAccessType": TrpzAccessType,
       "TrpzApAttachType": TrpzApAttachType,
       "TrpzApPortOrDapNum": TrpzApPortOrDapNum,
       "TrpzApNum": TrpzApNum,
       "TrpzApState": TrpzApState,
       "TrpzApTransition": TrpzApTransition,
       "TrpzApFailDetail": TrpzApFailDetail,
       "TrpzApConnectSecurityType": TrpzApConnectSecurityType,
       "TrpzApServiceAvailability": TrpzApServiceAvailability,
       "TrpzApBias": TrpzApBias,
       "TrpzApSerialNum": TrpzApSerialNum,
       "TrpzApFingerprint": TrpzApFingerprint,
       "TrpzRadioNum": TrpzRadioNum,
       "TrpzApRadioIndex": TrpzApRadioIndex,
       "TrpzApRadioIndexOrZero": TrpzApRadioIndexOrZero,
       "TrpzPowerLevel": TrpzPowerLevel,
       "TrpzRadioPowerChangeType": TrpzRadioPowerChangeType,
       "TrpzChannelChangeType": TrpzChannelChangeType,
       "TrpzChannelNum": TrpzChannelNum,
       "TrpzRadioEnable": TrpzRadioEnable,
       "TrpzRadioMode": TrpzRadioMode,
       "TrpzRadioConfigState": TrpzRadioConfigState,
       "TrpzRadioRate": TrpzRadioRate,
       "TrpzRadioRateEx": TrpzRadioRateEx,
       "TrpzRadioType": TrpzRadioType,
       "TrpzRssi": TrpzRssi,
       "TrpzApWasOperational": TrpzApWasOperational,
       "TrpzRadioChannelWidth": TrpzRadioChannelWidth,
       "TrpzRadioMimoState": TrpzRadioMimoState,
       "TrpzApPowerMode": TrpzApPowerMode,
       "TrpzApLedMode": TrpzApLedMode,
       "TrpzRadioAntennaLocation": TrpzRadioAntennaLocation,
       "TrpzCryptoType": TrpzCryptoType,
       "trpzApTc": trpzApTc}
)
