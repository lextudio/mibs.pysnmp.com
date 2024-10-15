# SNMP MIB module (SWITCH-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWITCH-INFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:15 2024
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

(switchVendor,) = mibBuilder.importSymbols(
    "TELESYN-ATI-TC",
    "switchVendor")


# MODULE-IDENTITY

switchVendorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1)
)
switchVendorMib.setRevisions(
        ("1997-05-16 22:00",
         "1996-11-05 22:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VendorInfo_ObjectIdentity = ObjectIdentity
vendorInfo = _VendorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1)
)


class _VendorName_Type(DisplayString):
    """Custom type vendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VendorName_Type.__name__ = "DisplayString"
_VendorName_Object = MibScalar
vendorName = _VendorName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 1),
    _VendorName_Type()
)
vendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorName.setStatus("current")


class _VendorProductName_Type(DisplayString):
    """Custom type vendorProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VendorProductName_Type.__name__ = "DisplayString"
_VendorProductName_Object = MibScalar
vendorProductName = _VendorProductName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 2),
    _VendorProductName_Type()
)
vendorProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorProductName.setStatus("current")


class _VendorModelName_Type(DisplayString):
    """Custom type vendorModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VendorModelName_Type.__name__ = "DisplayString"
_VendorModelName_Object = MibScalar
vendorModelName = _VendorModelName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 3),
    _VendorModelName_Type()
)
vendorModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorModelName.setStatus("current")


class _VendorModelId_Type(DisplayString):
    """Custom type vendorModelId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VendorModelId_Type.__name__ = "DisplayString"
_VendorModelId_Object = MibScalar
vendorModelId = _VendorModelId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 4),
    _VendorModelId_Type()
)
vendorModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorModelId.setStatus("current")


class _VendorCopyright_Type(DisplayString):
    """Custom type vendorCopyright based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VendorCopyright_Type.__name__ = "DisplayString"
_VendorCopyright_Object = MibScalar
vendorCopyright = _VendorCopyright_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 5),
    _VendorCopyright_Type()
)
vendorCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorCopyright.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-INFO-MIB",
    **{"switchVendorMib": switchVendorMib,
       "vendorInfo": vendorInfo,
       "vendorName": vendorName,
       "vendorProductName": vendorProductName,
       "vendorModelName": vendorModelName,
       "vendorModelId": vendorModelId,
       "vendorCopyright": vendorCopyright}
)
