# SNMP MIB module (TRAPEZE-NETWORKS-RF-DETECT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-RF-DETECT-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:33 2024
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

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzRFDetectTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 11)
)
trpzRFDetectTc.setRevisions(
        ("2011-07-27 00:11",
         "2009-08-13 00:10",
         "2007-04-18 00:02",
         "2007-03-28 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzRFDetectClassificationReason(Integer32, TextualConvention):
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



class TrpzRFDetectClassification(Integer32, TextualConvention):
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
        *(("member", 3),
          ("neighbor", 4),
          ("not-classified", 2),
          ("other", 1),
          ("rogue", 6),
          ("suspect", 5),
          ("tag", 7))
    )



class TrpzRFDetectNetworkingMode(Integer32, TextualConvention):
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



class TrpzRFDetectDot11ModulationStandard(Integer32, TextualConvention):
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
        *(("dot11A", 3),
          ("dot11B", 4),
          ("dot11G", 5),
          ("dot11NA", 6),
          ("dot11NG", 7),
          ("dot11Other", 2),
          ("dot11Unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-RF-DETECT-TC",
    **{"TrpzRFDetectClassificationReason": TrpzRFDetectClassificationReason,
       "TrpzRFDetectClassification": TrpzRFDetectClassification,
       "TrpzRFDetectNetworkingMode": TrpzRFDetectNetworkingMode,
       "TrpzRFDetectDot11ModulationStandard": TrpzRFDetectDot11ModulationStandard,
       "trpzRFDetectTc": trpzRFDetectTc}
)
