# SNMP MIB module (ELTEX-MES-DOT1X) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-DOT1X
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:37 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

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

eltMesDot1x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95)
)
eltMesDot1x.setRevisions(
        ("2015-08-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Eltdot1xRadiusAttrNASPortFormatType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("human", 2))
    )



class Eltdot1xMacAuthFormatUsernameLettercase(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowercase", 1),
          ("uppercase", 2))
    )



class Eltdot1xMacAuthFormatUsernameSeparator(Integer32, TextualConvention):
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
        *(("colon", 2),
          ("dash", 1),
          ("dot", 3),
          ("none", 0))
    )



class Eltdot1xMacAuthFormatUsernameGroupsize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              12)
        )
    )
    namedValues = NamedValues(
        *(("byte", 2),
          ("nibble", 1),
          ("none", 12),
          ("word", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesDot1xRadiusAttr_ObjectIdentity = ObjectIdentity
eltMesDot1xRadiusAttr = _EltMesDot1xRadiusAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 1)
)


class _Eltdot1xRadiusAttrNASPortFormat_Type(Eltdot1xRadiusAttrNASPortFormatType):
    """Custom type eltdot1xRadiusAttrNASPortFormat based on Eltdot1xRadiusAttrNASPortFormatType"""
    defaultValue = 1


_Eltdot1xRadiusAttrNASPortFormat_Object = MibScalar
eltdot1xRadiusAttrNASPortFormat = _Eltdot1xRadiusAttrNASPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 1, 1),
    _Eltdot1xRadiusAttrNASPortFormat_Type()
)
eltdot1xRadiusAttrNASPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1xRadiusAttrNASPortFormat.setStatus("current")
_EltMesDot1xMacAuth_ObjectIdentity = ObjectIdentity
eltMesDot1xMacAuth = _EltMesDot1xMacAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2)
)
_EltMesDot1xMacAuthFormat_ObjectIdentity = ObjectIdentity
eltMesDot1xMacAuthFormat = _EltMesDot1xMacAuthFormat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1)
)
_Eltdot1xMacAuthFormatUsernameLettercase_Type = Eltdot1xMacAuthFormatUsernameLettercase
_Eltdot1xMacAuthFormatUsernameLettercase_Object = MibScalar
eltdot1xMacAuthFormatUsernameLettercase = _Eltdot1xMacAuthFormatUsernameLettercase_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 1),
    _Eltdot1xMacAuthFormatUsernameLettercase_Type()
)
eltdot1xMacAuthFormatUsernameLettercase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1xMacAuthFormatUsernameLettercase.setStatus("current")
_Eltdot1xMacAuthFormatUsernameSeparator_Type = Eltdot1xMacAuthFormatUsernameSeparator
_Eltdot1xMacAuthFormatUsernameSeparator_Object = MibScalar
eltdot1xMacAuthFormatUsernameSeparator = _Eltdot1xMacAuthFormatUsernameSeparator_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 2),
    _Eltdot1xMacAuthFormatUsernameSeparator_Type()
)
eltdot1xMacAuthFormatUsernameSeparator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1xMacAuthFormatUsernameSeparator.setStatus("current")
_Eltdot1xMacAuthFormatUsernameGroupsize_Type = Eltdot1xMacAuthFormatUsernameGroupsize
_Eltdot1xMacAuthFormatUsernameGroupsize_Object = MibScalar
eltdot1xMacAuthFormatUsernameGroupsize = _Eltdot1xMacAuthFormatUsernameGroupsize_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 3),
    _Eltdot1xMacAuthFormatUsernameGroupsize_Type()
)
eltdot1xMacAuthFormatUsernameGroupsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1xMacAuthFormatUsernameGroupsize.setStatus("current")


class _Eltdot1xMacAuthFormatUserPassword_Type(DisplayString):
    """Custom type eltdot1xMacAuthFormatUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Eltdot1xMacAuthFormatUserPassword_Type.__name__ = "DisplayString"
_Eltdot1xMacAuthFormatUserPassword_Object = MibScalar
eltdot1xMacAuthFormatUserPassword = _Eltdot1xMacAuthFormatUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 95, 2, 1, 4),
    _Eltdot1xMacAuthFormatUserPassword_Type()
)
eltdot1xMacAuthFormatUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1xMacAuthFormatUserPassword.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-DOT1X",
    **{"Eltdot1xRadiusAttrNASPortFormatType": Eltdot1xRadiusAttrNASPortFormatType,
       "Eltdot1xMacAuthFormatUsernameLettercase": Eltdot1xMacAuthFormatUsernameLettercase,
       "Eltdot1xMacAuthFormatUsernameSeparator": Eltdot1xMacAuthFormatUsernameSeparator,
       "Eltdot1xMacAuthFormatUsernameGroupsize": Eltdot1xMacAuthFormatUsernameGroupsize,
       "eltMesDot1x": eltMesDot1x,
       "eltMesDot1xRadiusAttr": eltMesDot1xRadiusAttr,
       "eltdot1xRadiusAttrNASPortFormat": eltdot1xRadiusAttrNASPortFormat,
       "eltMesDot1xMacAuth": eltMesDot1xMacAuth,
       "eltMesDot1xMacAuthFormat": eltMesDot1xMacAuthFormat,
       "eltdot1xMacAuthFormatUsernameLettercase": eltdot1xMacAuthFormatUsernameLettercase,
       "eltdot1xMacAuthFormatUsernameSeparator": eltdot1xMacAuthFormatUsernameSeparator,
       "eltdot1xMacAuthFormatUsernameGroupsize": eltdot1xMacAuthFormatUsernameGroupsize,
       "eltdot1xMacAuthFormatUserPassword": eltdot1xMacAuthFormatUserPassword}
)
