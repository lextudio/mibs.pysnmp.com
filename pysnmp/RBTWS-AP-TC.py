# SNMP MIB module (RBTWS-AP-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-AP-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:31 2024
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

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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

rbtwsApTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 3)
)
rbtwsApTc.setRevisions(
        ("2008-05-07 00:41",
         "2008-02-14 00:32",
         "2007-12-03 00:30",
         "2007-07-06 00:23",
         "2007-07-05 00:22",
         "2006-07-10 00:15",
         "2006-03-30 00:14")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsAccessType(Integer32, TextualConvention):
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



class RbtwsApAttachType(Integer32, TextualConvention):
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



class RbtwsApPortOrDapNum(Unsigned32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class RbtwsApNum(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )



class RbtwsApState(Integer32, TextualConvention):
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



class RbtwsApTransition(Integer32, TextualConvention):
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



class RbtwsApFailDetail(Integer32, TextualConvention):
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



class RbtwsApConnectSecurityType(Integer32, TextualConvention):
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



class RbtwsApServiceAvailability(Integer32, TextualConvention):
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



class RbtwsApBias(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )



class RbtwsApSerialNum(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class RbtwsApFingerprint(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )



class RbtwsRadioNum(Integer32, TextualConvention):
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



class RbtwsPowerLevel(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )



class RbtwsRadioPowerChangeType(Integer32, TextualConvention):
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



class RbtwsChannelChangeType(Integer32, TextualConvention):
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



class RbtwsChannelNum(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



class RbtwsRadioEnable(Integer32, TextualConvention):
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



class RbtwsRadioMode(Integer32, TextualConvention):
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



class RbtwsRadioConfigState(Integer32, TextualConvention):
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



class RbtwsRadioRate(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 540),
    )



class RbtwsRadioType(Integer32, TextualConvention):
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



class RbtwsRssi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )



class RbtwsApWasOperational(Integer32, TextualConvention):
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



class RbtwsRadioChannelWidth(Integer32, TextualConvention):
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



class RbtwsRadioMimoState(Integer32, TextualConvention):
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



class RbtwsCryptoType(Integer32, TextualConvention):
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
    "RBTWS-AP-TC",
    **{"RbtwsAccessType": RbtwsAccessType,
       "RbtwsApAttachType": RbtwsApAttachType,
       "RbtwsApPortOrDapNum": RbtwsApPortOrDapNum,
       "RbtwsApNum": RbtwsApNum,
       "RbtwsApState": RbtwsApState,
       "RbtwsApTransition": RbtwsApTransition,
       "RbtwsApFailDetail": RbtwsApFailDetail,
       "RbtwsApConnectSecurityType": RbtwsApConnectSecurityType,
       "RbtwsApServiceAvailability": RbtwsApServiceAvailability,
       "RbtwsApBias": RbtwsApBias,
       "RbtwsApSerialNum": RbtwsApSerialNum,
       "RbtwsApFingerprint": RbtwsApFingerprint,
       "RbtwsRadioNum": RbtwsRadioNum,
       "RbtwsPowerLevel": RbtwsPowerLevel,
       "RbtwsRadioPowerChangeType": RbtwsRadioPowerChangeType,
       "RbtwsChannelChangeType": RbtwsChannelChangeType,
       "RbtwsChannelNum": RbtwsChannelNum,
       "RbtwsRadioEnable": RbtwsRadioEnable,
       "RbtwsRadioMode": RbtwsRadioMode,
       "RbtwsRadioConfigState": RbtwsRadioConfigState,
       "RbtwsRadioRate": RbtwsRadioRate,
       "RbtwsRadioType": RbtwsRadioType,
       "RbtwsRssi": RbtwsRssi,
       "RbtwsApWasOperational": RbtwsApWasOperational,
       "RbtwsRadioChannelWidth": RbtwsRadioChannelWidth,
       "RbtwsRadioMimoState": RbtwsRadioMimoState,
       "RbtwsCryptoType": RbtwsCryptoType,
       "rbtwsApTc": rbtwsApTc}
)
