# SNMP MIB module (CISCO-GSLB-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GSLB-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:59 2024
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

ciscoGslbTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 583)
)
ciscoGslbTcMIB.setRevisions(
        ("2007-02-23 00:00",
         "2006-09-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoGslbNodeServices(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 3),
          ("standby", 2))
    )



class CiscoGslbPeerStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("offline", 2),
          ("online", 3))
    )



class CiscoGslbAnswerType(Integer32, TextualConvention):
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
        *(("cra", 4),
          ("ns", 3),
          ("other", 1),
          ("vip", 2))
    )



class CiscoGslbKeepaliveTargetType(Integer32, TextualConvention):
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
        *(("cra", 4),
          ("ns", 3),
          ("other", 1),
          ("shared", 5),
          ("vip", 2))
    )



class CiscoGslbKeepaliveMethod(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cra", 8),
          ("httphead", 5),
          ("icmp", 3),
          ("kalap", 6),
          ("none", 2),
          ("ns", 7),
          ("other", 1),
          ("scriptedKal", 9),
          ("tcp", 4))
    )



class CiscoGslbKeepaliveConfigState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suspend", 2))
    )



class CiscoGslbKeepaliveRate(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fast", 3),
          ("other", 1),
          ("standard", 2))
    )



class CiscoGslbTerminationMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("graceful", 3),
          ("other", 1),
          ("reset", 2))
    )



class CiscoGslbKeepaliveStatus(Integer32, TextualConvention):
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
        *(("init", 5),
          ("offline", 2),
          ("online", 3),
          ("other", 1),
          ("suspended", 4))
    )



class CiscoGslbAnswerStatus(Integer32, TextualConvention):
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
        *(("init", 5),
          ("offline", 2),
          ("online", 3),
          ("other", 1),
          ("suspended", 4))
    )



class CiscoGslbAnswerAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("suspended", 1))
    )



class CiscoGslbKalapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kalapByTag", 3),
          ("kalapByVip", 2),
          ("other", 1))
    )



class CiscoGslbBalanceMethod(Integer32, TextualConvention):
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
        *(("boomerang", 7),
          ("hashed", 6),
          ("leastLoaded", 5),
          ("orderedList", 2),
          ("other", 1),
          ("roundRobin", 3),
          ("weightedRR", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GSLB-TC-MIB",
    **{"CiscoGslbNodeServices": CiscoGslbNodeServices,
       "CiscoGslbPeerStatus": CiscoGslbPeerStatus,
       "CiscoGslbAnswerType": CiscoGslbAnswerType,
       "CiscoGslbKeepaliveTargetType": CiscoGslbKeepaliveTargetType,
       "CiscoGslbKeepaliveMethod": CiscoGslbKeepaliveMethod,
       "CiscoGslbKeepaliveConfigState": CiscoGslbKeepaliveConfigState,
       "CiscoGslbKeepaliveRate": CiscoGslbKeepaliveRate,
       "CiscoGslbTerminationMethod": CiscoGslbTerminationMethod,
       "CiscoGslbKeepaliveStatus": CiscoGslbKeepaliveStatus,
       "CiscoGslbAnswerStatus": CiscoGslbAnswerStatus,
       "CiscoGslbAnswerAdminState": CiscoGslbAnswerAdminState,
       "CiscoGslbKalapType": CiscoGslbKalapType,
       "CiscoGslbBalanceMethod": CiscoGslbBalanceMethod,
       "ciscoGslbTcMIB": ciscoGslbTcMIB}
)
