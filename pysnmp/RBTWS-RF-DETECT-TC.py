# SNMP MIB module (RBTWS-RF-DETECT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-RF-DETECT-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:35 2024
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

rbtwsRFDetectTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 11)
)
rbtwsRFDetectTc.setRevisions(
        ("2007-04-18 00:02",
         "2007-03-28 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsRFDetectClassificationReason(Integer32, TextualConvention):
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
        *(("ad-hoc", 8),
          ("ap-in-modo", 4),
          ("default-classification", 2),
          ("fail-fingerprint", 11),
          ("neighbor-list", 5),
          ("other", 1),
          ("pass-fingerprint", 10),
          ("rogue-list", 3),
          ("seen-in-network", 7),
          ("ssid-list", 9),
          ("ssid-masquerade", 6))
    )



class RbtwsRFDetectClassification(Integer32, TextualConvention):
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
        *(("member", 3),
          ("neighbor", 4),
          ("not-classified", 2),
          ("other", 1),
          ("rogue", 6),
          ("suspect", 5))
    )



class RbtwsRFDetectNetworkingMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ad-hoc", 1),
          ("infrastructure", 2))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-RF-DETECT-TC",
    **{"RbtwsRFDetectClassificationReason": RbtwsRFDetectClassificationReason,
       "RbtwsRFDetectClassification": RbtwsRFDetectClassification,
       "RbtwsRFDetectNetworkingMode": RbtwsRFDetectNetworkingMode,
       "rbtwsRFDetectTc": rbtwsRFDetectTc}
)
