# SNMP MIB module (IANA-ADDRESS-FAMILY-NUMBERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANA-ADDRESS-FAMILY-NUMBERS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:19 2024
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

ianaAddressFamilyNumbers = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 72)
)
ianaAddressFamilyNumbers.setRevisions(
        ("2014-09-02 00:00",
         "2013-09-25 00:00",
         "2013-07-16 00:00",
         "2013-06-26 00:00",
         "2013-06-18 00:00",
         "2002-03-14 00:00",
         "2000-09-08 00:00",
         "2000-03-01 00:00",
         "2000-02-04 00:00",
         "1999-08-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AddressFamilyNumbers(Integer32, TextualConvention):
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
              26,
              27,
              28,
              16384,
              16385,
              16386,
              16387,
              16388,
              16389,
              16390,
              16391,
              16392,
              16393,
              16394,
              16395,
              16396,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("afi", 25),
          ("all802", 6),
          ("appleTalk", 12),
          ("asNumber", 18),
          ("banyanVines", 14),
          ("bbn1822", 5),
          ("bgpLs", 16388),
          ("decnetIV", 13),
          ("distinguishedName", 17),
          ("dns", 16),
          ("e163", 7),
          ("e164", 8),
          ("e164withNsap", 15),
          ("eigrpCommonServiceFamily", 16384),
          ("eigrpIpv4ServiceFamily", 16385),
          ("eigrpIpv6ServiceFamily", 16386),
          ("f69", 9),
          ("fibreChannelWWNN", 23),
          ("fibreChannelWWPN", 22),
          ("fortyeightBitMac", 16389),
          ("gwid", 24),
          ("hdlc", 4),
          ("ipV4", 1),
          ("ipV6", 2),
          ("ipv664", 16394),
          ("ipx", 11),
          ("lispCanonicalAddressFormat", 16387),
          ("mac24", 16392),
          ("mac40", 16393),
          ("mplsTpLspEndpointIdentifier", 27),
          ("mplsTpPseudowireEndpointIdentifier", 28),
          ("mplsTpSectionEndpointIdentifier", 26),
          ("nsap", 3),
          ("other", 0),
          ("oui", 16391),
          ("rBridgePortID", 16395),
          ("reserved", 65535),
          ("sixtyfourBitMac", 16390),
          ("trillNickname", 16396),
          ("x121", 10),
          ("xtpNativeModeXTP", 21),
          ("xtpOverIpv4", 19),
          ("xtpOverIpv6", 20))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    **{"AddressFamilyNumbers": AddressFamilyNumbers,
       "ianaAddressFamilyNumbers": ianaAddressFamilyNumbers}
)
