# SNMP MIB module (ACMEPACKET-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACMEPACKET-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:33 2024
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

(acmepacket,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacket")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 0)
)
apTextualConventions.setRevisions(
        ("2012-02-06 23:05",
         "2012-05-05 23:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ApHardwareModuleFamily(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              17,
              18,
              19,
              24,
              25,
              26,
              240,
              241,
              242)
        )
    )
    namedValues = NamedValues(
        *(("fanTray", 240),
          ("miu", 26),
          ("niu10g", 242),
          ("niuCopper", 24),
          ("niuFiber", 25),
          ("npu", 18),
          ("powerSupply", 241),
          ("spu", 17),
          ("tcu", 19),
          ("unknown", 0))
    )



class ApRedundancyState(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("activePending", 6),
          ("initial", 1),
          ("outOfService", 4),
          ("outOfServicePending", 8),
          ("recovery", 9),
          ("standby", 3),
          ("standbyPending", 7),
          ("unassigned", 5),
          ("unknown", 0))
    )



class ApPhyPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sfp", 1),
          ("unknown", 0))
    )



class ApPresence(Integer32, TextualConvention):
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
        *(("inserted", 1),
          ("removed", 2),
          ("unknown", 0))
    )



class ApTransportType(Integer32, TextualConvention):
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
        *(("sctp", 2),
          ("tcp", 1),
          ("unknown", 0))
    )



class ApServerStatus(Integer32, TextualConvention):
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
        *(("inservice", 0),
          ("lowerpriority", 1),
          ("oosunreachable", 2))
    )



class ApDiamResultCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1001,
              2001,
              2002,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3009,
              3010,
              4001,
              4002,
              4003,
              5001,
              5002,
              5003,
              5004,
              5005,
              5006,
              5007,
              5008,
              5009,
              5010,
              5011,
              5012,
              5013,
              5014,
              5015,
              5016,
              5017)
        )
    )
    namedValues = NamedValues(
        *(("diameterApplicationUnsupported", 3007),
          ("diameterAuthenticationRejected", 4001),
          ("diameterAuthoriszationRejected", 5003),
          ("diameterAvpNotAllowed", 5008),
          ("diameterAvpTooManyTimes", 5009),
          ("diameterAvpUnsupported", 5001),
          ("diameterCommandUnsupported", 3001),
          ("diameterContradictingAvps", 5007),
          ("diameterInvalidAvpBitCombo", 5016),
          ("diameterInvalidAvpBits", 3009),
          ("diameterInvalidAvpLength", 5014),
          ("diameterInvalidAvpValue", 5004),
          ("diameterInvalidBitInHeader", 5013),
          ("diameterInvalidHdrBits", 3008),
          ("diameterInvalidMessageLength", 5015),
          ("diameterLimitedSuccess", 2002),
          ("diameterLoopDetected", 3005),
          ("diameterMissingAvp", 5005),
          ("diameterMultiRoundAuth", 1001),
          ("diameterNoCommonApplication", 5010),
          ("diameterNoCommonSecurity", 5017),
          ("diameterOutOfSpace", 4002),
          ("diameterRealmNotServed", 3003),
          ("diameterRedirectIndicatoion", 3006),
          ("diameterResourcesExceeded", 5006),
          ("diameterSuccess", 2001),
          ("diameterTooBusy", 3004),
          ("diameterUnableToComply", 5012),
          ("diameterUnableToDeliver", 3002),
          ("diameterUnknownPeer", 3010),
          ("diameterUnknownSessionId", 5002),
          ("diameterUnsupportedVersion", 5011),
          ("electionLost", 4003))
    )



class ApPercentage(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACMEPACKET-TC",
    **{"ApHardwareModuleFamily": ApHardwareModuleFamily,
       "ApRedundancyState": ApRedundancyState,
       "ApPhyPortType": ApPhyPortType,
       "ApPresence": ApPresence,
       "ApTransportType": ApTransportType,
       "ApServerStatus": ApServerStatus,
       "ApDiamResultCode": ApDiamResultCode,
       "ApPercentage": ApPercentage,
       "apTextualConventions": apTextualConventions}
)
