# SNMP MIB module (CISCO-IPSLA-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSLA-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:56 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoIpSlaTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 624)
)
ciscoIpSlaTCMIB.setRevisions(
        ("2007-03-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpSlaOperType(Integer32, TextualConvention):
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
        *(("icmpEcho", 1),
          ("icmpJitter", 5),
          ("tcpConnect", 3),
          ("udpEcho", 2),
          ("udpJitter", 4))
    )



class IpSlaCodecType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("g711alaw", 2),
          ("g711ulaw", 1),
          ("g729a", 3),
          ("notApplicable", 0))
    )



class IpSlaReactVar(Integer32, TextualConvention):
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("connectionLoss", 8),
          ("icpif", 11),
          ("jitterAvg", 10),
          ("jitterDSAvg", 3),
          ("jitterSDAvg", 2),
          ("latencyDSAvg", 22),
          ("latencySDAvg", 23),
          ("maxOfLatencyDS", 20),
          ("maxOfLatencySD", 21),
          ("maxOfNegativeDS", 18),
          ("maxOfNegativeSD", 16),
          ("maxOfPositiveDS", 17),
          ("maxOfPositiveSD", 15),
          ("mos", 6),
          ("packetLateArrival", 13),
          ("packetLoss", 24),
          ("packetLossDS", 5),
          ("packetLossSD", 4),
          ("packetMIA", 12),
          ("packetOutOfSequence", 14),
          ("rtt", 1),
          ("successivePacketLoss", 19),
          ("timeout", 7),
          ("verifyError", 9))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSLA-TC-MIB",
    **{"IpSlaOperType": IpSlaOperType,
       "IpSlaCodecType": IpSlaCodecType,
       "IpSlaReactVar": IpSlaReactVar,
       "ciscoIpSlaTCMIB": ciscoIpSlaTCMIB}
)
