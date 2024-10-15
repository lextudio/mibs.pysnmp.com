# SNMP MIB module (NTWS-AP-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-AP-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:50 2024
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

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsApTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 3)
)
ntwsApTc.setRevisions(
        ("2009-07-21 01:03",
         "2008-12-02 01:01",
         "2008-11-27 01:00",
         "2008-11-26 00:51",
         "2008-10-06 00:50",
         "2008-05-07 00:41",
         "2008-02-14 00:32",
         "2007-12-03 00:30",
         "2007-09-25 00:24",
         "2007-07-06 00:23",
         "2007-07-05 00:22",
         "2006-07-10 00:15",
         "2006-03-30 00:14")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsAccessType(Integer32, TextualConvention):
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



class NtwsApAttachType(Integer32, TextualConvention):
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



class NtwsApPortOrDapNum(Unsigned32, TextualConvention):
    status = "obsolete"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class NtwsApNum(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )



class NtwsApState(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("bootStarted", 3),
          ("cleared", 1),
          ("configured", 7),
          ("configuring", 6),
          ("connectFailed", 5),
          ("imageDownloaded", 4),
          ("init", 2))
    )



class NtwsApTransition(Integer32, TextualConvention):
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
        *(("bootSuccess", 4),
          ("clear", 1),
          ("connectFail", 6),
          ("reset", 3),
          ("startConfiguring", 5),
          ("timeout", 2))
    )



class NtwsApFailDetail(Integer32, TextualConvention):
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("failUnknown", 99),
          ("fingerprintMismatch", 4),
          ("fingerprintRequired", 3),
          ("normalTransition", 91),
          ("portLinkDown", 12),
          ("portLinkUp", 11),
          ("secureHandshakeFailure", 2))
    )



class NtwsApConnectSecurityType(Integer32, TextualConvention):
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



class NtwsApServiceAvailability(Integer32, TextualConvention):
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



class NtwsApBias(Integer32, TextualConvention):
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



class NtwsApSerialNum(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class NtwsApFingerprint(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )



class NtwsRadioNum(Integer32, TextualConvention):
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



class NtwsApRadioIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NtwsApRadioIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class NtwsPowerLevel(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class NtwsRadioPowerChangeType(Integer32, TextualConvention):
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



class NtwsChannelChangeType(Integer32, TextualConvention):
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



class NtwsChannelNum(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



class NtwsRadioEnable(Integer32, TextualConvention):
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



class NtwsRadioMode(Integer32, TextualConvention):
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



class NtwsRadioConfigState(Integer32, TextualConvention):
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



class NtwsRadioRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 540),
    )



class NtwsRadioRateEx(Integer32, TextualConvention):
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
              35)
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
          ("rateMCS2", 22),
          ("rateMCS3", 23),
          ("rateMCS4", 24),
          ("rateMCS5", 25),
          ("rateMCS6", 26),
          ("rateMCS7", 27),
          ("rateMCS8", 28),
          ("rateMCS9", 29),
          ("rateUnknown", 1))
    )



class NtwsRadioType(Integer32, TextualConvention):
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



class NtwsRssi(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )



class NtwsApWasOperational(Integer32, TextualConvention):
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



class NtwsRadioChannelWidth(Integer32, TextualConvention):
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



class NtwsRadioMimoState(Integer32, TextualConvention):
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



class NtwsApPowerMode(Integer32, TextualConvention):
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



class NtwsApLedMode(Integer32, TextualConvention):
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



class NtwsRadioAntennaLocation(Integer32, TextualConvention):
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



class NtwsCryptoType(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("aesCcmp", 7),
          ("clear", 2),
          ("other", 1),
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
    "NTWS-AP-TC",
    **{"NtwsAccessType": NtwsAccessType,
       "NtwsApAttachType": NtwsApAttachType,
       "NtwsApPortOrDapNum": NtwsApPortOrDapNum,
       "NtwsApNum": NtwsApNum,
       "NtwsApState": NtwsApState,
       "NtwsApTransition": NtwsApTransition,
       "NtwsApFailDetail": NtwsApFailDetail,
       "NtwsApConnectSecurityType": NtwsApConnectSecurityType,
       "NtwsApServiceAvailability": NtwsApServiceAvailability,
       "NtwsApBias": NtwsApBias,
       "NtwsApSerialNum": NtwsApSerialNum,
       "NtwsApFingerprint": NtwsApFingerprint,
       "NtwsRadioNum": NtwsRadioNum,
       "NtwsApRadioIndex": NtwsApRadioIndex,
       "NtwsApRadioIndexOrZero": NtwsApRadioIndexOrZero,
       "NtwsPowerLevel": NtwsPowerLevel,
       "NtwsRadioPowerChangeType": NtwsRadioPowerChangeType,
       "NtwsChannelChangeType": NtwsChannelChangeType,
       "NtwsChannelNum": NtwsChannelNum,
       "NtwsRadioEnable": NtwsRadioEnable,
       "NtwsRadioMode": NtwsRadioMode,
       "NtwsRadioConfigState": NtwsRadioConfigState,
       "NtwsRadioRate": NtwsRadioRate,
       "NtwsRadioRateEx": NtwsRadioRateEx,
       "NtwsRadioType": NtwsRadioType,
       "NtwsRssi": NtwsRssi,
       "NtwsApWasOperational": NtwsApWasOperational,
       "NtwsRadioChannelWidth": NtwsRadioChannelWidth,
       "NtwsRadioMimoState": NtwsRadioMimoState,
       "NtwsApPowerMode": NtwsApPowerMode,
       "NtwsApLedMode": NtwsApLedMode,
       "NtwsRadioAntennaLocation": NtwsRadioAntennaLocation,
       "NtwsCryptoType": NtwsCryptoType,
       "ntwsApTc": ntwsApTc}
)
