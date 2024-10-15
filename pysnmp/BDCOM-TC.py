# SNMP MIB module (BDCOM-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:36 2024
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

(bdcomModules,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdcomModules")

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

bdcomTextualConventions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 12, 1)
)
bdcomTextualConventions.setRevisions(
        ("2003-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BDCOMNetworkProtocol(Integer32, TextualConvention):
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
              20,
              21,
              22,
              23,
              24,
              25,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("apollo", 12),
          ("appletalk", 7),
          ("atmIlmi", 17),
          ("bpxIgx", 23),
          ("bstun", 18),
          ("cdm", 21),
          ("chaos", 4),
          ("clns", 8),
          ("clnsPfx", 24),
          ("cons", 11),
          ("decnet", 2),
          ("http", 25),
          ("ip", 1),
          ("ipv6", 20),
          ("lat", 9),
          ("nbf", 22),
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



class BDCOMNetworkAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"


class Unsigned64(Counter64, TextualConvention):
    status = "current"


class InterfaceIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SAPType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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



class CountryCodeITU(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EntPhysicalIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class BDCOMRowOperStatus(Integer32, TextualConvention):
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



class BDCOMPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class BDCOMIpProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class BDCOMLocationClass(Integer32, TextualConvention):
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
        *(("channel", 7),
          ("chassis", 1),
          ("port", 5),
          ("shelf", 2),
          ("slot", 3),
          ("subChannel", 8),
          ("subPort", 6),
          ("subSlot", 4))
    )



class BDCOMLocationSpecifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class BDCOMInetAddressMask(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



class BDCOMAbsZeroBasedCounter32(Gauge32, TextualConvention):
    status = "current"


class BDCOMSnapShotAbsCounter32(Unsigned32, TextualConvention):
    status = "current"


class BDCOMAlarmSeverity(Integer32, TextualConvention):
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("info", 7),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class PerfHighIntervalCount(Counter64, TextualConvention):
    status = "current"


class ConfigIterator(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class BulkConfigResult(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ListIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ListIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TimeIntervalSec(Unsigned32, TextualConvention):
    status = "current"


class TimeIntervalMin(Unsigned32, TextualConvention):
    status = "current"


class BDCOMMilliSeconds(Unsigned32, TextualConvention):
    status = "current"


class MicroSeconds(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-TC",
    **{"BDCOMNetworkProtocol": BDCOMNetworkProtocol,
       "BDCOMNetworkAddress": BDCOMNetworkAddress,
       "Unsigned64": Unsigned64,
       "InterfaceIndexOrZero": InterfaceIndexOrZero,
       "SAPType": SAPType,
       "CountryCode": CountryCode,
       "CountryCodeITU": CountryCodeITU,
       "EntPhysicalIndexOrZero": EntPhysicalIndexOrZero,
       "BDCOMRowOperStatus": BDCOMRowOperStatus,
       "BDCOMPort": BDCOMPort,
       "BDCOMIpProtocol": BDCOMIpProtocol,
       "BDCOMLocationClass": BDCOMLocationClass,
       "BDCOMLocationSpecifier": BDCOMLocationSpecifier,
       "BDCOMInetAddressMask": BDCOMInetAddressMask,
       "BDCOMAbsZeroBasedCounter32": BDCOMAbsZeroBasedCounter32,
       "BDCOMSnapShotAbsCounter32": BDCOMSnapShotAbsCounter32,
       "BDCOMAlarmSeverity": BDCOMAlarmSeverity,
       "PerfHighIntervalCount": PerfHighIntervalCount,
       "ConfigIterator": ConfigIterator,
       "BulkConfigResult": BulkConfigResult,
       "ListIndex": ListIndex,
       "ListIndexOrZero": ListIndexOrZero,
       "TimeIntervalSec": TimeIntervalSec,
       "TimeIntervalMin": TimeIntervalMin,
       "BDCOMMilliSeconds": BDCOMMilliSeconds,
       "MicroSeconds": MicroSeconds,
       "bdcomTextualConventions": bdcomTextualConventions}
)
