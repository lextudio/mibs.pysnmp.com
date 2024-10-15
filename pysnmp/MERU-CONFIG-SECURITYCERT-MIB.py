# SNMP MIB module (MERU-CONFIG-SECURITYCERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-SECURITYCERT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:07 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigSecurityCert = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwSslCertInput_ObjectIdentity = ObjectIdentity
mwSslCertInput = _MwSslCertInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2)
)


class _MwSslCertInputCertificateName_Type(DisplayString):
    """Custom type mwSslCertInputCertificateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MwSslCertInputCertificateName_Type.__name__ = "DisplayString"
_MwSslCertInputCertificateName_Object = MibScalar
mwSslCertInputCertificateName = _MwSslCertInputCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 1),
    _MwSslCertInputCertificateName_Type()
)
mwSslCertInputCertificateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwSslCertInputCertificateName.setStatus("current")


class _MwSslCertInputPfxPassword_Type(DisplayString):
    """Custom type mwSslCertInputPfxPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MwSslCertInputPfxPassword_Type.__name__ = "DisplayString"
_MwSslCertInputPfxPassword_Object = MibScalar
mwSslCertInputPfxPassword = _MwSslCertInputPfxPassword_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 2, 2),
    _MwSslCertInputPfxPassword_Type()
)
mwSslCertInputPfxPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwSslCertInputPfxPassword.setStatus("current")
_MwSslCert_ObjectIdentity = ObjectIdentity
mwSslCert = _MwSslCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3)
)


class _MwSslCertCertificateName_Type(DisplayString):
    """Custom type mwSslCertCertificateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MwSslCertCertificateName_Type.__name__ = "DisplayString"
_MwSslCertCertificateName_Object = MibScalar
mwSslCertCertificateName = _MwSslCertCertificateName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 1),
    _MwSslCertCertificateName_Type()
)
mwSslCertCertificateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSslCertCertificateName.setStatus("current")
_MwSslCertCertFormattedText_Type = DisplayString
_MwSslCertCertFormattedText_Object = MibScalar
mwSslCertCertFormattedText = _MwSslCertCertFormattedText_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 10, 3, 2),
    _MwSslCertCertFormattedText_Type()
)
mwSslCertCertFormattedText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSslCertCertFormattedText.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-SECURITYCERT-MIB",
    **{"mwConfigSecurityCert": mwConfigSecurityCert,
       "mwSslCertInput": mwSslCertInput,
       "mwSslCertInputCertificateName": mwSslCertInputCertificateName,
       "mwSslCertInputPfxPassword": mwSslCertInputPfxPassword,
       "mwSslCert": mwSslCert,
       "mwSslCertCertificateName": mwSslCertCertificateName,
       "mwSslCertCertFormattedText": mwSslCertCertFormattedText}
)
