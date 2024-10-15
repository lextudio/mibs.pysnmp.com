# SNMP MIB module (CTRON-WEBVIEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-WEBVIEW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:56 2024
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

(ctApplication,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctApplication")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtWebView_ObjectIdentity = ObjectIdentity
ctWebView = _CtWebView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4)
)
_CtEwvConfiguration_ObjectIdentity = ObjectIdentity
ctEwvConfiguration = _CtEwvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1)
)
_CtEwvDocSupport_ObjectIdentity = ObjectIdentity
ctEwvDocSupport = _CtEwvDocSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1)
)


class _CtEwvDocSupportAdmin_Type(Integer32):
    """Custom type ctEwvDocSupportAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CtEwvDocSupportAdmin_Type.__name__ = "Integer32"
_CtEwvDocSupportAdmin_Object = MibScalar
ctEwvDocSupportAdmin = _CtEwvDocSupportAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 1),
    _CtEwvDocSupportAdmin_Type()
)
ctEwvDocSupportAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEwvDocSupportAdmin.setStatus("mandatory")
_CtEwvDocSupportLocation_Type = DisplayString
_CtEwvDocSupportLocation_Object = MibScalar
ctEwvDocSupportLocation = _CtEwvDocSupportLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 2),
    _CtEwvDocSupportLocation_Type()
)
ctEwvDocSupportLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEwvDocSupportLocation.setStatus("mandatory")


class _CtEwvDocSupportAdminUID_Type(Integer32):
    """Custom type ctEwvDocSupportAdminUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CtEwvDocSupportAdminUID_Type.__name__ = "Integer32"
_CtEwvDocSupportAdminUID_Object = MibScalar
ctEwvDocSupportAdminUID = _CtEwvDocSupportAdminUID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 3),
    _CtEwvDocSupportAdminUID_Type()
)
ctEwvDocSupportAdminUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEwvDocSupportAdminUID.setStatus("mandatory")
_CtEwvDocSupportUsername_Type = DisplayString
_CtEwvDocSupportUsername_Object = MibScalar
ctEwvDocSupportUsername = _CtEwvDocSupportUsername_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 4),
    _CtEwvDocSupportUsername_Type()
)
ctEwvDocSupportUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEwvDocSupportUsername.setStatus("mandatory")
_CtEwvDocSupportPassword_Type = DisplayString
_CtEwvDocSupportPassword_Object = MibScalar
ctEwvDocSupportPassword = _CtEwvDocSupportPassword_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 5),
    _CtEwvDocSupportPassword_Type()
)
ctEwvDocSupportPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEwvDocSupportPassword.setStatus("mandatory")
_CtEwvSystemParameters_ObjectIdentity = ObjectIdentity
ctEwvSystemParameters = _CtEwvSystemParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2)
)


class _CtEwvAuthScheme_Type(Integer32):
    """Custom type ctEwvAuthScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 2),
          ("digest", 3),
          ("none", 1))
    )


_CtEwvAuthScheme_Type.__name__ = "Integer32"
_CtEwvAuthScheme_Object = MibScalar
ctEwvAuthScheme = _CtEwvAuthScheme_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 1),
    _CtEwvAuthScheme_Type()
)
ctEwvAuthScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEwvAuthScheme.setStatus("mandatory")
_CtEwvAuthNonceValidCount_Type = Integer32
_CtEwvAuthNonceValidCount_Object = MibScalar
ctEwvAuthNonceValidCount = _CtEwvAuthNonceValidCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 2),
    _CtEwvAuthNonceValidCount_Type()
)
ctEwvAuthNonceValidCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctEwvAuthNonceValidCount.setStatus("mandatory")
_CtEwvStatus_ObjectIdentity = ObjectIdentity
ctEwvStatus = _CtEwvStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-WEBVIEW-MIB",
    **{"ctWebView": ctWebView,
       "ctEwvConfiguration": ctEwvConfiguration,
       "ctEwvDocSupport": ctEwvDocSupport,
       "ctEwvDocSupportAdmin": ctEwvDocSupportAdmin,
       "ctEwvDocSupportLocation": ctEwvDocSupportLocation,
       "ctEwvDocSupportAdminUID": ctEwvDocSupportAdminUID,
       "ctEwvDocSupportUsername": ctEwvDocSupportUsername,
       "ctEwvDocSupportPassword": ctEwvDocSupportPassword,
       "ctEwvSystemParameters": ctEwvSystemParameters,
       "ctEwvAuthScheme": ctEwvAuthScheme,
       "ctEwvAuthNonceValidCount": ctEwvAuthNonceValidCount,
       "ctEwvStatus": ctEwvStatus}
)
