# SNMP MIB module (CISCO-DMN-DSG-PRODUCTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-PRODUCTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:29 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoDSGProd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21)
)
ciscoDSGProd.setRevisions(
        ("2010-08-24 07:00",
         "2009-12-20 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProdInfo_ObjectIdentity = ObjectIdentity
prodInfo = _ProdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1)
)


class _ProdHostName_Type(DisplayString):
    """Custom type prodHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ProdHostName_Type.__name__ = "DisplayString"
_ProdHostName_Object = MibScalar
prodHostName = _ProdHostName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 1),
    _ProdHostName_Type()
)
prodHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prodHostName.setStatus("current")


class _ProdTrackingId_Type(DisplayString):
    """Custom type prodTrackingId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ProdTrackingId_Type.__name__ = "DisplayString"
_ProdTrackingId_Object = MibScalar
prodTrackingId = _ProdTrackingId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 2),
    _ProdTrackingId_Type()
)
prodTrackingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodTrackingId.setStatus("current")


class _ProdModelNo_Type(DisplayString):
    """Custom type prodModelNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_ProdModelNo_Type.__name__ = "DisplayString"
_ProdModelNo_Object = MibScalar
prodModelNo = _ProdModelNo_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 3),
    _ProdModelNo_Type()
)
prodModelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodModelNo.setStatus("current")


class _ProdModelName_Type(DisplayString):
    """Custom type prodModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_ProdModelName_Type.__name__ = "DisplayString"
_ProdModelName_Object = MibScalar
prodModelName = _ProdModelName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 4),
    _ProdModelName_Type()
)
prodModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodModelName.setStatus("current")


class _ProdCatalogNo_Type(DisplayString):
    """Custom type prodCatalogNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_ProdCatalogNo_Type.__name__ = "DisplayString"
_ProdCatalogNo_Object = MibScalar
prodCatalogNo = _ProdCatalogNo_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 5),
    _ProdCatalogNo_Type()
)
prodCatalogNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodCatalogNo.setStatus("current")


class _ProdCustomerCode_Type(DisplayString):
    """Custom type prodCustomerCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_ProdCustomerCode_Type.__name__ = "DisplayString"
_ProdCustomerCode_Object = MibScalar
prodCustomerCode = _ProdCustomerCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 6),
    _ProdCustomerCode_Type()
)
prodCustomerCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodCustomerCode.setStatus("current")


class _ProdLimitVer_Type(DisplayString):
    """Custom type prodLimitVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_ProdLimitVer_Type.__name__ = "DisplayString"
_ProdLimitVer_Object = MibScalar
prodLimitVer = _ProdLimitVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 7),
    _ProdLimitVer_Type()
)
prodLimitVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodLimitVer.setStatus("current")


class _ProdFPGADesignation_Type(Integer32):
    """Custom type prodFPGADesignation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ProdFPGADesignation_Type.__name__ = "Integer32"
_ProdFPGADesignation_Object = MibScalar
prodFPGADesignation = _ProdFPGADesignation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 21, 1, 8),
    _ProdFPGADesignation_Type()
)
prodFPGADesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodFPGADesignation.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-PRODUCTION-MIB",
    **{"ciscoDSGProd": ciscoDSGProd,
       "prodInfo": prodInfo,
       "prodHostName": prodHostName,
       "prodTrackingId": prodTrackingId,
       "prodModelNo": prodModelNo,
       "prodModelName": prodModelName,
       "prodCatalogNo": prodCatalogNo,
       "prodCustomerCode": prodCustomerCode,
       "prodLimitVer": prodLimitVer,
       "prodFPGADesignation": prodFPGADesignation}
)
