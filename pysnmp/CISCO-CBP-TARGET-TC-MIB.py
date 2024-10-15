# SNMP MIB module (CISCO-CBP-TARGET-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CBP-TARGET-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:05 2024
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

ciscoCbpTargetTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 511)
)
ciscoCbpTargetTCMIB.setRevisions(
        ("2006-03-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcbptTargetType(Integer32, TextualConvention):
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
        *(("aaaSession", 7),
          ("atmPvc", 2),
          ("entity", 4),
          ("frDlci", 3),
          ("fwZone", 5),
          ("fwZonePair", 6),
          ("genIf", 1))
    )



class CcbptTargetDirection(Integer32, TextualConvention):
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
        *(("inOut", 4),
          ("input", 2),
          ("output", 3),
          ("undirected", 1))
    )



class CcbptTargetId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CcbptTargetIdIf(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class CcbptTargetIdAtmPvc(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d:2d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class CcbptTargetIdFrDlci(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class CcbptTargetIdEntity(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class CcbptTargetIdNameString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CcbptTargetIdAaaSession(OctetString, TextualConvention):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class CcbptPolicySourceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCbQos", 1),
          ("ciscoCbpBase", 2))
    )



class CcbptPolicyIdentifier(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CcbptPolicyIdentifierOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CBP-TARGET-TC-MIB",
    **{"CcbptTargetType": CcbptTargetType,
       "CcbptTargetDirection": CcbptTargetDirection,
       "CcbptTargetId": CcbptTargetId,
       "CcbptTargetIdIf": CcbptTargetIdIf,
       "CcbptTargetIdAtmPvc": CcbptTargetIdAtmPvc,
       "CcbptTargetIdFrDlci": CcbptTargetIdFrDlci,
       "CcbptTargetIdEntity": CcbptTargetIdEntity,
       "CcbptTargetIdNameString": CcbptTargetIdNameString,
       "CcbptTargetIdAaaSession": CcbptTargetIdAaaSession,
       "CcbptPolicySourceType": CcbptPolicySourceType,
       "CcbptPolicyIdentifier": CcbptPolicyIdentifier,
       "CcbptPolicyIdentifierOrZero": CcbptPolicyIdentifierOrZero,
       "ciscoCbpTargetTCMIB": ciscoCbpTargetTCMIB}
)
