# SNMP MIB module (CISCO-LWAPP-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:09 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoLwappTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 514)
)
ciscoLwappTextualConventions.setRevisions(
        ("2011-09-13 00:00",
         "2007-10-30 00:00",
         "2007-02-05 00:00",
         "2006-10-31 00:00",
         "2006-04-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CLApIfType(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 2),
          ("dot11abgn", 4),
          ("dot11ac", 5),
          ("dot11b", 6),
          ("dot11bg", 1),
          ("dot11g", 7),
          ("dot11n24", 8),
          ("dot11n5", 9),
          ("unknown", 10),
          ("uwb", 3))
    )



class CLDot11Channel(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
        ValueRangeConstraint(169, 169),
        ValueRangeConstraint(173, 173),
    )



class CLDot11ClientStatus(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aaaPending", 2),
          ("associated", 4),
          ("authenticated", 3),
          ("disassociated", 6),
          ("excluded", 9),
          ("idle", 1),
          ("powersave", 5),
          ("probing", 8),
          ("tobedeleted", 7))
    )



class CLEventFrames(Bits, TextualConvention):
    status = "current"


class CLMfpEventType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16,
              17,
              19,
              20,
              21,
              22,
              23,
              24,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("bcastActionFrameRcvd", 34),
          ("bcastDeauthenticationFrameRcvd", 33),
          ("bcastDisassociationFrameRcvd", 32),
          ("ccmpDecryptError", 17),
          ("ccmpInvalidReplayCtr", 19),
          ("ccmpNoEncryptError", 16),
          ("invalidMic", 1),
          ("invalidSeq", 2),
          ("noMic", 3),
          ("tkipInvalidIcv", 21),
          ("tkipInvalidMhdrIe", 23),
          ("tkipInvalidMic", 22),
          ("tkipInvalidReplayCtr", 24),
          ("tkipNoEncryptError", 20),
          ("unexpectedMic", 4))
    )



class CLMfpEventSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientMfp", 2),
          ("infrastructureMfp", 1))
    )



class CLMfpVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mfpv1", 1),
          ("mfpv2", 2))
    )



class CLTimeBaseStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cTimeBaseInSync", 1),
          ("cTimeBaseNotInSync", 2))
    )



class CLSecEncryptType(Bits, TextualConvention):
    status = "current"


class CLSecKeyFormat(Integer32, TextualConvention):
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
        *(("ascii", 3),
          ("default", 1),
          ("hex", 2))
    )



class CLDot11RfParamMode(Integer32, TextualConvention):
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
          ("custom", 2),
          ("default", 1))
    )



class CLTsmDot11CurrentPackets(Gauge32, TextualConvention):
    status = "current"


class CLCdpAdvtVersionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cdpv1", 1),
          ("cdpv2", 2))
    )



class CLDot11ChannelBandwidth(Integer32, TextualConvention):
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
        *(("aboveforty", 4),
          ("belowforty", 5),
          ("five", 1),
          ("ten", 2),
          ("twenty", 3))
    )



class CLDot11Band(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("band2dot4", 1),
          ("band5", 2))
    )



class CLApAssocFailureReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("unknown", 1))
    )



class CLWebAuthType(Integer32, TextualConvention):
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
        *(("external", 3),
          ("internalCustom", 2),
          ("internalDefault", 1))
    )



class CLClientPowerSaveMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )



class CLApEthernetIfStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class CLApDot11RadioSubband(Integer32, TextualConvention):
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
        *(("all", 1),
          ("sub49", 2),
          ("sub52", 3),
          ("sub54", 4),
          ("sub58", 5))
    )



class CLApDot11RadioRole(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("access", 4),
          ("downlink", 3),
          ("downlinkaccess", 6),
          ("shutdown", 0),
          ("unknown", 8),
          ("updownlink", 1),
          ("updownlinkaccess", 7),
          ("uplink", 2),
          ("uplinkaccess", 5))
    )



class CcxServiceVersion(Integer32, TextualConvention):
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
        *(("none", 1),
          ("version1", 2),
          ("version2", 3))
    )



class CLApMode(Integer32, TextualConvention):
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
        *(("bridge", 5),
          ("local", 0),
          ("monitor", 1),
          ("remote", 2),
          ("roguedetector", 3),
          ("seConnect", 6),
          ("sniffer", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-TC-MIB",
    **{"CLApIfType": CLApIfType,
       "CLDot11Channel": CLDot11Channel,
       "CLDot11ClientStatus": CLDot11ClientStatus,
       "CLEventFrames": CLEventFrames,
       "CLMfpEventType": CLMfpEventType,
       "CLMfpEventSource": CLMfpEventSource,
       "CLMfpVersion": CLMfpVersion,
       "CLTimeBaseStatus": CLTimeBaseStatus,
       "CLSecEncryptType": CLSecEncryptType,
       "CLSecKeyFormat": CLSecKeyFormat,
       "CLDot11RfParamMode": CLDot11RfParamMode,
       "CLTsmDot11CurrentPackets": CLTsmDot11CurrentPackets,
       "CLCdpAdvtVersionType": CLCdpAdvtVersionType,
       "CLDot11ChannelBandwidth": CLDot11ChannelBandwidth,
       "CLDot11Band": CLDot11Band,
       "CLApAssocFailureReason": CLApAssocFailureReason,
       "CLWebAuthType": CLWebAuthType,
       "CLClientPowerSaveMode": CLClientPowerSaveMode,
       "CLApEthernetIfStatus": CLApEthernetIfStatus,
       "CLApDot11RadioSubband": CLApDot11RadioSubband,
       "CLApDot11RadioRole": CLApDot11RadioRole,
       "CcxServiceVersion": CcxServiceVersion,
       "CLApMode": CLApMode,
       "ciscoLwappTextualConventions": ciscoLwappTextualConventions}
)
