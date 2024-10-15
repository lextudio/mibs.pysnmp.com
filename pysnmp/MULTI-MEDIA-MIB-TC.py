# SNMP MIB module (MULTI-MEDIA-MIB-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MULTI-MEDIA-MIB-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:36 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class MmUtf8String(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class MmE164String(OctetString, TextualConvention):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmTAddressTag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipx", 3),
          ("netbios", 5),
          ("nsap", 4),
          ("other", 0))
    )



class MmGlobalIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "8d-9,3x,1d,2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class MmAliasTag(Integer32, TextualConvention):
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
        *(("e164", 1),
          ("emailId", 5),
          ("h323Id", 2),
          ("other", 0),
          ("partyNumber", 6),
          ("transportId", 4),
          ("urlId", 3))
    )



class MmAliasAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "512a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )



class MmEndpointID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmGatekeeperID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmH225Crv(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class MmTerminalAudioCapability(Bits, TextualConvention):
    status = "current"


class MmTerminalDataCapability(Bits, TextualConvention):
    status = "current"


class MmTerminalVideoCapability(Bits, TextualConvention):
    status = "current"


class MmTerminalLineRateCapability(Bits, TextualConvention):
    status = "current"


class MmControlsCommands(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("abruptRestart", 2),
          ("abruptShutdown", 4),
          ("enterQuiescence", 6),
          ("exitQuiescence", 7),
          ("gracefulRestart", 3),
          ("gracefulShutdown", 5),
          ("other", 1),
          ("resetStatistics", 10),
          ("runDiagnostic", 11),
          ("startLog", 8),
          ("stopLog", 9))
    )



class MmErrorSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("critical", 2),
          ("indeterminate", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )



class MmErrorProbableCause(Integer32, TextualConvention):
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
              16,
              17,
              18,
              19,
              20,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("alarmOnIncomingConn", 17),
          ("alarmOnOutgoingConn", 18),
          ("alarmSignal", 5),
          ("callEstablishmentError", 16),
          ("commProtocolError", 4),
          ("componentFailure", 30),
          ("congestion", 32),
          ("lossOfConn", 3),
          ("lossOfIncomingConn", 19),
          ("lossOfOutgoingConn", 20),
          ("other", 1),
          ("performanceDegraded", 6),
          ("powerProblem", 33),
          ("processingError", 31),
          ("qoSDegraded", 2))
    )



class MmH323EndpointType(Integer32, TextualConvention):
    status = "current"


class MmCallType(Integer32, TextualConvention):
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
        *(("nToN", 4),
          ("nToOne", 3),
          ("oneToN", 2),
          ("pointToPoint", 1))
    )



# MIB Managed Objects in the order of their OIDs

_MmRoot_ObjectIdentity = ObjectIdentity
mmRoot = _MmRoot_ObjectIdentity(
    (0, 0, 8, 341, 1)
)
_MmH323Root_ObjectIdentity = ObjectIdentity
mmH323Root = _MmH323Root_ObjectIdentity(
    (0, 0, 8, 341, 1, 1)
)
if mibBuilder.loadTexts:
    mmH323Root.setStatus("current")
_MmH320Root_ObjectIdentity = ObjectIdentity
mmH320Root = _MmH320Root_ObjectIdentity(
    (0, 0, 8, 341, 1, 2)
)
if mibBuilder.loadTexts:
    mmH320Root.setStatus("current")
_MmH245Root_ObjectIdentity = ObjectIdentity
mmH245Root = _MmH245Root_ObjectIdentity(
    (0, 0, 8, 341, 1, 3)
)
if mibBuilder.loadTexts:
    mmH245Root.setStatus("current")
_MmH323GatewayRoot_ObjectIdentity = ObjectIdentity
mmH323GatewayRoot = _MmH323GatewayRoot_ObjectIdentity(
    (0, 0, 8, 341, 1, 4)
)
if mibBuilder.loadTexts:
    mmH323GatewayRoot.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MULTI-MEDIA-MIB-TC",
    **{"MmUtf8String": MmUtf8String,
       "MmE164String": MmE164String,
       "MmTAddressTag": MmTAddressTag,
       "MmGlobalIdentifier": MmGlobalIdentifier,
       "MmAliasTag": MmAliasTag,
       "MmAliasAddress": MmAliasAddress,
       "MmEndpointID": MmEndpointID,
       "MmGatekeeperID": MmGatekeeperID,
       "MmH225Crv": MmH225Crv,
       "MmTerminalAudioCapability": MmTerminalAudioCapability,
       "MmTerminalDataCapability": MmTerminalDataCapability,
       "MmTerminalVideoCapability": MmTerminalVideoCapability,
       "MmTerminalLineRateCapability": MmTerminalLineRateCapability,
       "MmControlsCommands": MmControlsCommands,
       "MmErrorSeverity": MmErrorSeverity,
       "MmErrorProbableCause": MmErrorProbableCause,
       "MmH323EndpointType": MmH323EndpointType,
       "MmCallType": MmCallType,
       "mmRoot": mmRoot,
       "mmH323Root": mmH323Root,
       "mmH320Root": mmH320Root,
       "mmH245Root": mmH245Root,
       "mmH323GatewayRoot": mmH323GatewayRoot}
)
