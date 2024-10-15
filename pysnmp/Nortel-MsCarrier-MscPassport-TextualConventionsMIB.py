# SNMP MIB module (Nortel-MsCarrier-MscPassport-TextualConventionsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-TextualConventionsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:43 2024
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

(Integer32,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Integer32",
    "Unsigned32")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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


# Types definitions



class PassportCounter64(Counter32):
    """Custom type PassportCounter64 based on Counter32"""




class Hex(Unsigned32):
    """Custom type Hex based on Unsigned32"""




class Gauge64(OctetString):
    """Custom type Gauge64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Unsigned64(OctetString):
    """Custom type Unsigned64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class DigitString(OctetString):
    """Custom type DigitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )





class WildcardedDigitString(OctetString):
    """Custom type WildcardedDigitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )





class HexString(OctetString):
    """Custom type HexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )





class AsciiString(OctetString):
    """Custom type AsciiString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )





class ExtendedAsciiString(OctetString):
    """Custom type ExtendedAsciiString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )





class DashedHexString(OctetString):
    """Custom type DashedHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )





class EnterpriseDateAndTime(OctetString):
    """Custom type EnterpriseDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(19, 19),
    )





class Link(ObjectIdentifier):
    """Custom type Link based on ObjectIdentifier"""




class IntegerSequence(OctetString):
    """Custom type IntegerSequence based on OctetString"""




class FixedPoint1(Unsigned32):
    """Custom type FixedPoint1 based on Unsigned32"""




class FixedPoint2(Unsigned32):
    """Custom type FixedPoint2 based on Unsigned32"""




class FixedPoint3(Unsigned32):
    """Custom type FixedPoint3 based on Unsigned32"""




class FixedPoint4(Unsigned32):
    """Custom type FixedPoint4 based on Unsigned32"""




class FixedPoint5(Unsigned32):
    """Custom type FixedPoint5 based on Unsigned32"""




class FixedPoint6(Unsigned32):
    """Custom type FixedPoint6 based on Unsigned32"""




class FixedPoint7(Unsigned32):
    """Custom type FixedPoint7 based on Unsigned32"""




class FixedPoint8(Unsigned32):
    """Custom type FixedPoint8 based on Unsigned32"""




class FixedPoint9(Unsigned32):
    """Custom type FixedPoint9 based on Unsigned32"""




class AsciiStringIndex(OctetString):
    """Custom type AsciiStringIndex based on OctetString"""




class NonReplicated(Integer32):
    """Custom type NonReplicated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("present", 1)
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TextualConventionsMIB_ObjectIdentity = ObjectIdentity
textualConventionsMIB = _TextualConventionsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2)
)
_TextualConventionsGroup_ObjectIdentity = ObjectIdentity
textualConventionsGroup = _TextualConventionsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1)
)
_TextualConventionsGroupCA_ObjectIdentity = ObjectIdentity
textualConventionsGroupCA = _TextualConventionsGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1, 1)
)
_TextualConventionsGroupCA01_ObjectIdentity = ObjectIdentity
textualConventionsGroupCA01 = _TextualConventionsGroupCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1, 1, 2)
)
_TextualConventionsGroupCA01A_ObjectIdentity = ObjectIdentity
textualConventionsGroupCA01A = _TextualConventionsGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 1, 1, 2, 2)
)
_TextualConventionsCapabilities_ObjectIdentity = ObjectIdentity
textualConventionsCapabilities = _TextualConventionsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3)
)
_TextualConventionsCapabilitiesCA_ObjectIdentity = ObjectIdentity
textualConventionsCapabilitiesCA = _TextualConventionsCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3, 1)
)
_TextualConventionsCapabilitiesCA01_ObjectIdentity = ObjectIdentity
textualConventionsCapabilitiesCA01 = _TextualConventionsCapabilitiesCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3, 1, 2)
)
_TextualConventionsCapabilitiesCA01A_ObjectIdentity = ObjectIdentity
textualConventionsCapabilitiesCA01A = _TextualConventionsCapabilitiesCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 2, 3, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    **{"PassportCounter64": PassportCounter64,
       "Hex": Hex,
       "Gauge64": Gauge64,
       "Unsigned64": Unsigned64,
       "DigitString": DigitString,
       "WildcardedDigitString": WildcardedDigitString,
       "HexString": HexString,
       "AsciiString": AsciiString,
       "ExtendedAsciiString": ExtendedAsciiString,
       "DashedHexString": DashedHexString,
       "EnterpriseDateAndTime": EnterpriseDateAndTime,
       "Link": Link,
       "IntegerSequence": IntegerSequence,
       "FixedPoint1": FixedPoint1,
       "FixedPoint2": FixedPoint2,
       "FixedPoint3": FixedPoint3,
       "FixedPoint4": FixedPoint4,
       "FixedPoint5": FixedPoint5,
       "FixedPoint6": FixedPoint6,
       "FixedPoint7": FixedPoint7,
       "FixedPoint8": FixedPoint8,
       "FixedPoint9": FixedPoint9,
       "AsciiStringIndex": AsciiStringIndex,
       "NonReplicated": NonReplicated,
       "textualConventionsMIB": textualConventionsMIB,
       "textualConventionsGroup": textualConventionsGroup,
       "textualConventionsGroupCA": textualConventionsGroupCA,
       "textualConventionsGroupCA01": textualConventionsGroupCA01,
       "textualConventionsGroupCA01A": textualConventionsGroupCA01A,
       "textualConventionsCapabilities": textualConventionsCapabilities,
       "textualConventionsCapabilitiesCA": textualConventionsCapabilitiesCA,
       "textualConventionsCapabilitiesCA01": textualConventionsCapabilitiesCA01,
       "textualConventionsCapabilitiesCA01A": textualConventionsCapabilitiesCA01A}
)
