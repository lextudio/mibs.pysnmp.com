# SNMP MIB module (ADSL-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADSL-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:55 2024
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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

adsltcmib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94, 2)
)
adsltcmib.setRevisions(
        ("1999-08-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdslLineCodingType(Integer32, TextualConvention):
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
        *(("cap", 3),
          ("dmt", 2),
          ("other", 1),
          ("qam", 4))
    )



class AdslPerfCurrDayCount(Gauge32, TextualConvention):
    status = "current"


class AdslPerfPrevDayCount(Gauge32, TextualConvention):
    status = "current"


class AdslPerfTimeElapsed(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AdslMIB_ObjectIdentity = ObjectIdentity
adslMIB = _AdslMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 94)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADSL-TC-MIB",
    **{"AdslLineCodingType": AdslLineCodingType,
       "AdslPerfCurrDayCount": AdslPerfCurrDayCount,
       "AdslPerfPrevDayCount": AdslPerfPrevDayCount,
       "AdslPerfTimeElapsed": AdslPerfTimeElapsed,
       "adslMIB": adslMIB,
       "adsltcmib": adsltcmib}
)
