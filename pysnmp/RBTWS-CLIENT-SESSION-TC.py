# SNMP MIB module (RBTWS-CLIENT-SESSION-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-CLIENT-SESSION-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:33 2024
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

rbtwsClientSessionTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 10)
)
rbtwsClientSessionTc.setRevisions(
        ("2007-10-08 00:10",
         "2006-09-26 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsUserAccessType(Integer32, TextualConvention):
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
        *(("dot1x", 3),
          ("last-resort", 4),
          ("mac", 1),
          ("web", 2))
    )



class RbtwsClientSessionState(Integer32, TextualConvention):
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
        *(("active", 4),
          ("associated", 1),
          ("authorized", 3),
          ("authorizing", 2),
          ("clearing", 9),
          ("de-associated", 5),
          ("invalid", 10),
          ("roaming-away", 6),
          ("updated-to-roam", 7),
          ("web-authing", 11),
          ("wired", 8))
    )



class RbtwsClientDot1xState(Integer32, TextualConvention):
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
        *(("aborting", 7),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("held", 8),
          ("initialize", 1),
          ("wired", 6))
    )



class RbtwsClientAuthenProtocolType(Integer32, TextualConvention):
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
        *(("eap-tls", 2),
          ("eap-ttls", 3),
          ("leap", 6),
          ("md5", 4),
          ("none", 1),
          ("pass-through", 7),
          ("peap", 5))
    )



class RbtwsClientAccessMode(Integer32, TextualConvention):
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
        *(("ap", 2),
          ("other", 1),
          ("wired", 3))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-CLIENT-SESSION-TC",
    **{"RbtwsUserAccessType": RbtwsUserAccessType,
       "RbtwsClientSessionState": RbtwsClientSessionState,
       "RbtwsClientDot1xState": RbtwsClientDot1xState,
       "RbtwsClientAuthenProtocolType": RbtwsClientAuthenProtocolType,
       "RbtwsClientAccessMode": RbtwsClientAccessMode,
       "rbtwsClientSessionTc": rbtwsClientSessionTc}
)
