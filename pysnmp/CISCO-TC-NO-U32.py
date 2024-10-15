# SNMP MIB module (CISCO-TC-NO-U32) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TC-NO-U32
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:31 2024
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

(ciscoModules,
 ciscoProducts) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoModules",
    "ciscoProducts")

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

ciscoTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 12, 1)
)
ciscoTextualConventions.setRevisions(
        ("1997-03-13 00:00",
         "1997-03-13 00:00",
         "1996-08-14 00:00",
         "1996-07-08 00:00",
         "1995-06-07 00:00",
         "1998-10-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoNetworkProtocol(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("apollo", 12),
          ("appletalk", 7),
          ("atmIlmi", 17),
          ("bstun", 18),
          ("chaos", 4),
          ("clns", 8),
          ("cons", 11),
          ("decnet", 2),
          ("ip", 1),
          ("lat", 9),
          ("novell", 14),
          ("pup", 3),
          ("qllc", 15),
          ("snapshot", 16),
          ("stun", 13),
          ("unknown", 65535),
          ("vines", 10),
          ("x121", 6),
          ("x25pvc", 19),
          ("xns", 5))
    )



class CiscoNetworkAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"


class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SAPType(Integer32, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )



class CountryCode(OctetString, TextualConvention):
    status = "current"
    displayHint = "2a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )



class EntPhysicalIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CiscoRowOperStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("activeDependencies", 2),
          ("inactiveDependency", 3),
          ("missingDependency", 4))
    )



class CiscoPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CiscoIpProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TC-NO-U32",
    **{"CiscoNetworkProtocol": CiscoNetworkProtocol,
       "CiscoNetworkAddress": CiscoNetworkAddress,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SAPType": SAPType,
       "CountryCode": CountryCode,
       "EntPhysicalIndexOrZero": EntPhysicalIndexOrZero,
       "CiscoRowOperStatus": CiscoRowOperStatus,
       "CiscoPort": CiscoPort,
       "CiscoIpProtocol": CiscoIpProtocol,
       "ciscoTextualConventions": ciscoTextualConventions}
)
