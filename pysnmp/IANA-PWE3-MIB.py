# SNMP MIB module (IANA-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IANA-PWE3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:02 2024
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

ianaPwe3MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 174)
)
ianaPwe3MIB.setRevisions(
        ("2009-06-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAPwTypeTC(Integer32, TextualConvention):
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
              32767)
        )
    )
    namedValues = NamedValues(
        *(("atmAal5PduVcc", 14),
          ("atmAal5SduVcc", 2),
          ("atmCell1to1Vcc", 12),
          ("atmCell1to1Vpc", 13),
          ("atmCellNto1Vcc", 9),
          ("atmCellNto1Vpc", 10),
          ("atmTransparent", 3),
          ("basicCesPsn", 21),
          ("basicTdmIp", 22),
          ("cem", 8),
          ("cep", 16),
          ("e1Satop", 17),
          ("e3Satop", 19),
          ("ethernet", 5),
          ("ethernetTagged", 4),
          ("frDlci", 25),
          ("frameRelayDlciMartiniMode", 1),
          ("frameRelayPortMode", 15),
          ("hdlc", 6),
          ("ipLayer2Transport", 11),
          ("other", 0),
          ("ppp", 7),
          ("t1Satop", 18),
          ("t3Satop", 20),
          ("tdmCasCesPsn", 23),
          ("tdmCasTdmIp", 24),
          ("wildcard", 32767))
    )



class IANAPwPsnTypeTC(Integer32, TextualConvention):
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
        *(("l2tp", 2),
          ("mpls", 1),
          ("mplsOverGre", 5),
          ("mplsOverIp", 4),
          ("other", 6),
          ("udpOverIp", 3))
    )



class IANAPwCapabilities(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANA-PWE3-MIB",
    **{"IANAPwTypeTC": IANAPwTypeTC,
       "IANAPwPsnTypeTC": IANAPwPsnTypeTC,
       "IANAPwCapabilities": IANAPwCapabilities,
       "ianaPwe3MIB": ianaPwe3MIB}
)
