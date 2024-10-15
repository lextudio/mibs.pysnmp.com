# SNMP MIB module (MULTI-MEDIA-REG-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MULTI-MEDIA-REG-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:05 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

multimediaRegMib = ModuleIdentity(
    (1, 3, 6, 1, 3, 323)
)
multimediaRegMib.setRevisions(
        ("1998-05-29 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MmUtf8String(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class MmE164String(OctetString, TextualConvention):
    status = "current"
    displayHint = "128a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmTAddressTag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipx", 3),
          ("netbios", 5),
          ("nsap", 4),
          ("other", 0))
    )



class MmGlobalIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "8d-9,3x,1d,2x:2x:2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class MmAliasTag(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("emailId", 5),
          ("h323Id", 2),
          ("other", 0),
          ("partyNumber", 6),
          ("transportId", 4),
          ("urlId", 3))
    )



class MmAliasAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "512a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )



class MmEndpointID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmGatekeeperID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class MmH225Crv(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_MmRtpRoot_ObjectIdentity = ObjectIdentity
mmRtpRoot = _MmRtpRoot_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 1)
)
if mibBuilder.loadTexts:
    mmRtpRoot.setStatus("current")
_MmH323Root_ObjectIdentity = ObjectIdentity
mmH323Root = _MmH323Root_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 2)
)
if mibBuilder.loadTexts:
    mmH323Root.setStatus("current")
_MmH320Root_ObjectIdentity = ObjectIdentity
mmH320Root = _MmH320Root_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 3)
)
if mibBuilder.loadTexts:
    mmH320Root.setStatus("current")
_MmH245Root_ObjectIdentity = ObjectIdentity
mmH245Root = _MmH245Root_ObjectIdentity(
    (1, 3, 6, 1, 3, 323, 4)
)
if mibBuilder.loadTexts:
    mmH245Root.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MULTI-MEDIA-REG-TC",
    **{"MmUtf8String": MmUtf8String,
       "MmE164String": MmE164String,
       "MmTAddressTag": MmTAddressTag,
       "MmGlobalIdentifier": MmGlobalIdentifier,
       "MmAliasTag": MmAliasTag,
       "MmAliasAddress": MmAliasAddress,
       "MmEndpointID": MmEndpointID,
       "MmGatekeeperID": MmGatekeeperID,
       "MmH225Crv": MmH225Crv,
       "multimediaRegMib": multimediaRegMib,
       "mmRtpRoot": mmRtpRoot,
       "mmH323Root": mmH323Root,
       "mmH320Root": mmH320Root,
       "mmH245Root": mmH245Root}
)
