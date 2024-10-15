# SNMP MIB module (IANA-BFD-TC-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANA-BFD-TC-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:10 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ianaBfdTCStdMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 224)
)
ianaBfdTCStdMib.setRevisions(
        ("2014-08-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAbfdDiagTC(Integer32, TextualConvention):
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
        *(("administrativelyDown", 7),
          ("concatenatedPathDown", 6),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("forwardingPlaneReset", 4),
          ("misConnectivityDefect", 9),
          ("neighborSignaledSessionDown", 3),
          ("noDiagnostic", 0),
          ("pathDown", 5),
          ("reverseConcatenatedPathDown", 8))
    )



class IANAbfdSessTypeTC(Integer32, TextualConvention):
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
        *(("multiHopOutOfBandSignaling", 3),
          ("multiHopTotallyArbitraryPaths", 2),
          ("multiHopUnidirectionalLinks", 4),
          ("singleHop", 1))
    )



class IANAbfdSessOperModeTC(Integer32, TextualConvention):
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
        *(("asyncModeWEchoFunction", 1),
          ("asynchModeWOEchoFunction", 2),
          ("demandModeWEchoFunction", 3),
          ("demandModeWOEchoFunction", 4))
    )



class IANAbfdSessStateTC(Integer32, TextualConvention):
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
        *(("adminDown", 1),
          ("down", 2),
          ("failing", 5),
          ("init", 3),
          ("up", 4))
    )



class IANAbfdSessAuthenticationTypeTC(Integer32, TextualConvention):
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("keyedMD5", 2),
          ("keyedSHA1", 4),
          ("meticulousKeyedMD5", 3),
          ("meticulousKeyedSHA1", 5),
          ("noAuthentication", -1),
          ("reserved", 0),
          ("simplePassword", 1))
    )



class IANAbfdSessAuthenticationKeyTC(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 252),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-BFD-TC-STD-MIB",
    **{"IANAbfdDiagTC": IANAbfdDiagTC,
       "IANAbfdSessTypeTC": IANAbfdSessTypeTC,
       "IANAbfdSessOperModeTC": IANAbfdSessOperModeTC,
       "IANAbfdSessStateTC": IANAbfdSessStateTC,
       "IANAbfdSessAuthenticationTypeTC": IANAbfdSessAuthenticationTypeTC,
       "IANAbfdSessAuthenticationKeyTC": IANAbfdSessAuthenticationKeyTC,
       "ianaBfdTCStdMib": ianaBfdTCStdMib}
)
