# SNMP MIB module (DLINK-3100-EMBWEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-EMBWEB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:56 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlEmbWeb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66)
)
rlEmbWeb.setRevisions(
        ("2006-07-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlEmbWebProtocol(Integer32, TextualConvention):
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
        *(("default", 1),
          ("http", 2),
          ("https", 3))
    )



class RlEmbWebEnabled(Integer32, TextualConvention):
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
        *(("default", 1),
          ("false", 2),
          ("true", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlEmWebMibVersion_Type = Integer32
_RlEmWebMibVersion_Object = MibScalar
rlEmWebMibVersion = _RlEmWebMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 1),
    _RlEmWebMibVersion_Type()
)
rlEmWebMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEmWebMibVersion.setStatus("current")
_RlEmWebWebSite_Type = DisplayString
_RlEmWebWebSite_Object = MibScalar
rlEmWebWebSite = _RlEmWebWebSite_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 2),
    _RlEmWebWebSite_Type()
)
rlEmWebWebSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebWebSite.setStatus("current")
_RlEmWebSecurityTable_Object = MibTable
rlEmWebSecurityTable = _RlEmWebSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3)
)
if mibBuilder.loadTexts:
    rlEmWebSecurityTable.setStatus("current")
_RlEmWebSecurityEntry_Object = MibTableRow
rlEmWebSecurityEntry = _RlEmWebSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1)
)
rlEmWebSecurityEntry.setIndexNames(
    (0, "DLINK-3100-EMBWEB-MIB", "rlEmWebSecurityUserName"),
)
if mibBuilder.loadTexts:
    rlEmWebSecurityEntry.setStatus("current")


class _RlEmWebSecurityUserName_Type(DisplayString):
    """Custom type rlEmWebSecurityUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RlEmWebSecurityUserName_Type.__name__ = "DisplayString"
_RlEmWebSecurityUserName_Object = MibTableColumn
rlEmWebSecurityUserName = _RlEmWebSecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 1),
    _RlEmWebSecurityUserName_Type()
)
rlEmWebSecurityUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSecurityUserName.setStatus("current")


class _RlEmWebSecurityPassword_Type(DisplayString):
    """Custom type rlEmWebSecurityPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RlEmWebSecurityPassword_Type.__name__ = "DisplayString"
_RlEmWebSecurityPassword_Object = MibTableColumn
rlEmWebSecurityPassword = _RlEmWebSecurityPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 2),
    _RlEmWebSecurityPassword_Type()
)
rlEmWebSecurityPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSecurityPassword.setStatus("current")


class _RlEmWebSecurityAccess_Type(Integer32):
    """Custom type rlEmWebSecurityAccess based on Integer32"""
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
        *(("none", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("super", 4))
    )


_RlEmWebSecurityAccess_Type.__name__ = "Integer32"
_RlEmWebSecurityAccess_Object = MibTableColumn
rlEmWebSecurityAccess = _RlEmWebSecurityAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 3),
    _RlEmWebSecurityAccess_Type()
)
rlEmWebSecurityAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSecurityAccess.setStatus("current")
_RlEmWebSecurityIpAddr_Type = IpAddress
_RlEmWebSecurityIpAddr_Object = MibTableColumn
rlEmWebSecurityIpAddr = _RlEmWebSecurityIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 4),
    _RlEmWebSecurityIpAddr_Type()
)
rlEmWebSecurityIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSecurityIpAddr.setStatus("current")
_RlEmWebSecurityPort_Type = Integer32
_RlEmWebSecurityPort_Object = MibTableColumn
rlEmWebSecurityPort = _RlEmWebSecurityPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 5),
    _RlEmWebSecurityPort_Type()
)
rlEmWebSecurityPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSecurityPort.setStatus("current")


class _RlEmWebSecuritySnmpVersion_Type(Integer32):
    """Custom type rlEmWebSecuritySnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ver1", 1),
          ("ver2", 2),
          ("ver3", 3))
    )


_RlEmWebSecuritySnmpVersion_Type.__name__ = "Integer32"
_RlEmWebSecuritySnmpVersion_Object = MibTableColumn
rlEmWebSecuritySnmpVersion = _RlEmWebSecuritySnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 6),
    _RlEmWebSecuritySnmpVersion_Type()
)
rlEmWebSecuritySnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSecuritySnmpVersion.setStatus("current")
_RlEmWebSecurityStatus_Type = RowStatus
_RlEmWebSecurityStatus_Object = MibTableColumn
rlEmWebSecurityStatus = _RlEmWebSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 3, 1, 7),
    _RlEmWebSecurityStatus_Type()
)
rlEmWebSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSecurityStatus.setStatus("current")


class _RlEmWebCloseTimeout_Type(Integer32):
    """Custom type rlEmWebCloseTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlEmWebCloseTimeout_Type.__name__ = "Integer32"
_RlEmWebCloseTimeout_Object = MibScalar
rlEmWebCloseTimeout = _RlEmWebCloseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 5),
    _RlEmWebCloseTimeout_Type()
)
rlEmWebCloseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebCloseTimeout.setStatus("current")


class _RlEmWebReceiveTimeout_Type(Integer32):
    """Custom type rlEmWebReceiveTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlEmWebReceiveTimeout_Type.__name__ = "Integer32"
_RlEmWebReceiveTimeout_Object = MibScalar
rlEmWebReceiveTimeout = _RlEmWebReceiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 6),
    _RlEmWebReceiveTimeout_Type()
)
rlEmWebReceiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebReceiveTimeout.setStatus("current")


class _RlEmWebMaxIdleTimeout_Type(Integer32):
    """Custom type rlEmWebMaxIdleTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3932159),
    )


_RlEmWebMaxIdleTimeout_Type.__name__ = "Integer32"
_RlEmWebMaxIdleTimeout_Object = MibScalar
rlEmWebMaxIdleTimeout = _RlEmWebMaxIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 7),
    _RlEmWebMaxIdleTimeout_Type()
)
rlEmWebMaxIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebMaxIdleTimeout.setStatus("current")


class _RlEmWebSetEWSfilesStatus_Type(Integer32):
    """Custom type rlEmWebSetEWSfilesStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("opened", 1))
    )


_RlEmWebSetEWSfilesStatus_Type.__name__ = "Integer32"
_RlEmWebSetEWSfilesStatus_Object = MibScalar
rlEmWebSetEWSfilesStatus = _RlEmWebSetEWSfilesStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 8),
    _RlEmWebSetEWSfilesStatus_Type()
)
rlEmWebSetEWSfilesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebSetEWSfilesStatus.setStatus("current")
_RlEmbeddedWebApplied_Type = TruthValue
_RlEmbeddedWebApplied_Object = MibScalar
rlEmbeddedWebApplied = _RlEmbeddedWebApplied_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 9),
    _RlEmbeddedWebApplied_Type()
)
rlEmbeddedWebApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEmbeddedWebApplied.setStatus("current")


class _RlEmWebHttpPort_Type(Integer32):
    """Custom type rlEmWebHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlEmWebHttpPort_Type.__name__ = "Integer32"
_RlEmWebHttpPort_Object = MibScalar
rlEmWebHttpPort = _RlEmWebHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 10),
    _RlEmWebHttpPort_Type()
)
rlEmWebHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebHttpPort.setStatus("current")
_RlEmWebHttpEnable_Type = TruthValue
_RlEmWebHttpEnable_Object = MibScalar
rlEmWebHttpEnable = _RlEmWebHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 11),
    _RlEmWebHttpEnable_Type()
)
rlEmWebHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebHttpEnable.setStatus("current")


class _RlEmWebHttpsPort_Type(Integer32):
    """Custom type rlEmWebHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlEmWebHttpsPort_Type.__name__ = "Integer32"
_RlEmWebHttpsPort_Object = MibScalar
rlEmWebHttpsPort = _RlEmWebHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 12),
    _RlEmWebHttpsPort_Type()
)
rlEmWebHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebHttpsPort.setStatus("current")
_RlEmWebHttpsEnable_Type = TruthValue
_RlEmWebHttpsEnable_Object = MibScalar
rlEmWebHttpsEnable = _RlEmWebHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 13),
    _RlEmWebHttpsEnable_Type()
)
rlEmWebHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebHttpsEnable.setStatus("current")


class _RlEmWebCertificateCountryName_Type(DisplayString):
    """Custom type rlEmWebCertificateCountryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_RlEmWebCertificateCountryName_Type.__name__ = "DisplayString"
_RlEmWebCertificateCountryName_Object = MibScalar
rlEmWebCertificateCountryName = _RlEmWebCertificateCountryName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 14),
    _RlEmWebCertificateCountryName_Type()
)
rlEmWebCertificateCountryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebCertificateCountryName.setStatus("current")


class _RlEmWebCertificateStateOrProvinceName_Type(DisplayString):
    """Custom type rlEmWebCertificateStateOrProvinceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RlEmWebCertificateStateOrProvinceName_Type.__name__ = "DisplayString"
_RlEmWebCertificateStateOrProvinceName_Object = MibScalar
rlEmWebCertificateStateOrProvinceName = _RlEmWebCertificateStateOrProvinceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 15),
    _RlEmWebCertificateStateOrProvinceName_Type()
)
rlEmWebCertificateStateOrProvinceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebCertificateStateOrProvinceName.setStatus("current")


class _RlEmWebCertificateLocalityName_Type(DisplayString):
    """Custom type rlEmWebCertificateLocalityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlEmWebCertificateLocalityName_Type.__name__ = "DisplayString"
_RlEmWebCertificateLocalityName_Object = MibScalar
rlEmWebCertificateLocalityName = _RlEmWebCertificateLocalityName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 16),
    _RlEmWebCertificateLocalityName_Type()
)
rlEmWebCertificateLocalityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebCertificateLocalityName.setStatus("current")


class _RlEmWebCertificateOrganizationName_Type(DisplayString):
    """Custom type rlEmWebCertificateOrganizationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RlEmWebCertificateOrganizationName_Type.__name__ = "DisplayString"
_RlEmWebCertificateOrganizationName_Object = MibScalar
rlEmWebCertificateOrganizationName = _RlEmWebCertificateOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 17),
    _RlEmWebCertificateOrganizationName_Type()
)
rlEmWebCertificateOrganizationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebCertificateOrganizationName.setStatus("current")
_RlEmWebCertificateCommonName_Type = IpAddress
_RlEmWebCertificateCommonName_Object = MibScalar
rlEmWebCertificateCommonName = _RlEmWebCertificateCommonName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 19),
    _RlEmWebCertificateCommonName_Type()
)
rlEmWebCertificateCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebCertificateCommonName.setStatus("current")


class _RlEmWebCertificateRegenerate_Type(Integer32):
    """Custom type rlEmWebCertificateRegenerate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("regenerateCertificate", 1),
          ("regenerateRsaKeyAndCertificate", 2))
    )


_RlEmWebCertificateRegenerate_Type.__name__ = "Integer32"
_RlEmWebCertificateRegenerate_Object = MibScalar
rlEmWebCertificateRegenerate = _RlEmWebCertificateRegenerate_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 20),
    _RlEmWebCertificateRegenerate_Type()
)
rlEmWebCertificateRegenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebCertificateRegenerate.setStatus("current")


class _RlEmWebRsaKeyLength_Type(Integer32):
    """Custom type rlEmWebRsaKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_RlEmWebRsaKeyLength_Type.__name__ = "Integer32"
_RlEmWebRsaKeyLength_Object = MibScalar
rlEmWebRsaKeyLength = _RlEmWebRsaKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 21),
    _RlEmWebRsaKeyLength_Type()
)
rlEmWebRsaKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebRsaKeyLength.setStatus("current")
_RlEmWebDebug_Type = Integer32
_RlEmWebDebug_Object = MibScalar
rlEmWebDebug = _RlEmWebDebug_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 22),
    _RlEmWebDebug_Type()
)
rlEmWebDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebDebug.setStatus("current")
_RlEmWebURL_Type = DisplayString
_RlEmWebURL_Object = MibScalar
rlEmWebURL = _RlEmWebURL_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 23),
    _RlEmWebURL_Type()
)
rlEmWebURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEmWebURL.setStatus("current")
_RlEmWebDisplayNonPresentEntities_Type = TruthValue
_RlEmWebDisplayNonPresentEntities_Object = MibScalar
rlEmWebDisplayNonPresentEntities = _RlEmWebDisplayNonPresentEntities_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 24),
    _RlEmWebDisplayNonPresentEntities_Type()
)
rlEmWebDisplayNonPresentEntities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEmWebDisplayNonPresentEntities.setStatus("current")
_RlEmWebCertificateExists_Type = TruthValue
_RlEmWebCertificateExists_Object = MibScalar
rlEmWebCertificateExists = _RlEmWebCertificateExists_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 25),
    _RlEmWebCertificateExists_Type()
)
rlEmWebCertificateExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEmWebCertificateExists.setStatus("current")
_RlEmWebHttpsActiveCertificateId_Type = Integer32
_RlEmWebHttpsActiveCertificateId_Object = MibScalar
rlEmWebHttpsActiveCertificateId = _RlEmWebHttpsActiveCertificateId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 26),
    _RlEmWebHttpsActiveCertificateId_Type()
)
rlEmWebHttpsActiveCertificateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebHttpsActiveCertificateId.setStatus("current")


class _RlEmWebExtraPort_Type(Integer32):
    """Custom type rlEmWebExtraPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlEmWebExtraPort_Type.__name__ = "Integer32"
_RlEmWebExtraPort_Object = MibScalar
rlEmWebExtraPort = _RlEmWebExtraPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 27),
    _RlEmWebExtraPort_Type()
)
rlEmWebExtraPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebExtraPort.setStatus("current")


class _RlEmWebExtraPortType_Type(Integer32):
    """Custom type rlEmWebExtraPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("http", 0),
          ("https", 1))
    )


_RlEmWebExtraPortType_Type.__name__ = "Integer32"
_RlEmWebExtraPortType_Object = MibScalar
rlEmWebExtraPortType = _RlEmWebExtraPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 28),
    _RlEmWebExtraPortType_Type()
)
rlEmWebExtraPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebExtraPortType.setStatus("current")


class _RlEmWebMaxHttpsIdleTimeout_Type(Integer32):
    """Custom type rlEmWebMaxHttpsIdleTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3932159),
    )


_RlEmWebMaxHttpsIdleTimeout_Type.__name__ = "Integer32"
_RlEmWebMaxHttpsIdleTimeout_Object = MibScalar
rlEmWebMaxHttpsIdleTimeout = _RlEmWebMaxHttpsIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 29),
    _RlEmWebMaxHttpsIdleTimeout_Type()
)
rlEmWebMaxHttpsIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebMaxHttpsIdleTimeout.setStatus("current")
_RlEmWebServiceTable_Object = MibTable
rlEmWebServiceTable = _RlEmWebServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30)
)
if mibBuilder.loadTexts:
    rlEmWebServiceTable.setStatus("current")
_RlEmWebServiceEntry_Object = MibTableRow
rlEmWebServiceEntry = _RlEmWebServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1)
)
rlEmWebServiceEntry.setIndexNames(
    (0, "DLINK-3100-EMBWEB-MIB", "rlEmWebServiceId"),
)
if mibBuilder.loadTexts:
    rlEmWebServiceEntry.setStatus("current")
_RlEmWebServiceId_Type = Integer32
_RlEmWebServiceId_Object = MibTableColumn
rlEmWebServiceId = _RlEmWebServiceId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 1),
    _RlEmWebServiceId_Type()
)
rlEmWebServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlEmWebServiceId.setStatus("current")


class _RlEmWebServiceName_Type(DisplayString):
    """Custom type rlEmWebServiceName based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RlEmWebServiceName_Type.__name__ = "DisplayString"
_RlEmWebServiceName_Object = MibTableColumn
rlEmWebServiceName = _RlEmWebServiceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 2),
    _RlEmWebServiceName_Type()
)
rlEmWebServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEmWebServiceName.setStatus("current")


class _RlEmWebServiceEnable_Type(RlEmbWebEnabled):
    """Custom type rlEmWebServiceEnable based on RlEmbWebEnabled"""


_RlEmWebServiceEnable_Object = MibTableColumn
rlEmWebServiceEnable = _RlEmWebServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 3),
    _RlEmWebServiceEnable_Type()
)
rlEmWebServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebServiceEnable.setStatus("current")


class _RlEmWebServicePort_Type(Integer32):
    """Custom type rlEmWebServicePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlEmWebServicePort_Type.__name__ = "Integer32"
_RlEmWebServicePort_Object = MibTableColumn
rlEmWebServicePort = _RlEmWebServicePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 4),
    _RlEmWebServicePort_Type()
)
rlEmWebServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebServicePort.setStatus("current")


class _RlEmWebServiceMaxUsers_Type(Integer32):
    """Custom type rlEmWebServiceMaxUsers based on Integer32"""
    defaultValue = 0


_RlEmWebServiceMaxUsers_Object = MibTableColumn
rlEmWebServiceMaxUsers = _RlEmWebServiceMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 5),
    _RlEmWebServiceMaxUsers_Type()
)
rlEmWebServiceMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlEmWebServiceMaxUsers.setStatus("current")


class _RlEmWebServiceProtocol_Type(RlEmbWebProtocol):
    """Custom type rlEmWebServiceProtocol based on RlEmbWebProtocol"""


_RlEmWebServiceProtocol_Object = MibTableColumn
rlEmWebServiceProtocol = _RlEmWebServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 6),
    _RlEmWebServiceProtocol_Type()
)
rlEmWebServiceProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebServiceProtocol.setStatus("current")


class _RlEmWebServiceCertificateId_Type(Integer32):
    """Custom type rlEmWebServiceCertificateId based on Integer32"""
    defaultValue = 1000


_RlEmWebServiceCertificateId_Object = MibTableColumn
rlEmWebServiceCertificateId = _RlEmWebServiceCertificateId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 7),
    _RlEmWebServiceCertificateId_Type()
)
rlEmWebServiceCertificateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebServiceCertificateId.setStatus("current")


class _RlEmWebServiceMaxIdleTimeOut_Type(Integer32):
    """Custom type rlEmWebServiceMaxIdleTimeOut based on Integer32"""
    defaultValue = 3932160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3932160),
    )


_RlEmWebServiceMaxIdleTimeOut_Type.__name__ = "Integer32"
_RlEmWebServiceMaxIdleTimeOut_Object = MibTableColumn
rlEmWebServiceMaxIdleTimeOut = _RlEmWebServiceMaxIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 66, 30, 1, 8),
    _RlEmWebServiceMaxIdleTimeOut_Type()
)
rlEmWebServiceMaxIdleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlEmWebServiceMaxIdleTimeOut.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-EMBWEB-MIB",
    **{"RlEmbWebProtocol": RlEmbWebProtocol,
       "RlEmbWebEnabled": RlEmbWebEnabled,
       "rlEmbWeb": rlEmbWeb,
       "rlEmWebMibVersion": rlEmWebMibVersion,
       "rlEmWebWebSite": rlEmWebWebSite,
       "rlEmWebSecurityTable": rlEmWebSecurityTable,
       "rlEmWebSecurityEntry": rlEmWebSecurityEntry,
       "rlEmWebSecurityUserName": rlEmWebSecurityUserName,
       "rlEmWebSecurityPassword": rlEmWebSecurityPassword,
       "rlEmWebSecurityAccess": rlEmWebSecurityAccess,
       "rlEmWebSecurityIpAddr": rlEmWebSecurityIpAddr,
       "rlEmWebSecurityPort": rlEmWebSecurityPort,
       "rlEmWebSecuritySnmpVersion": rlEmWebSecuritySnmpVersion,
       "rlEmWebSecurityStatus": rlEmWebSecurityStatus,
       "rlEmWebCloseTimeout": rlEmWebCloseTimeout,
       "rlEmWebReceiveTimeout": rlEmWebReceiveTimeout,
       "rlEmWebMaxIdleTimeout": rlEmWebMaxIdleTimeout,
       "rlEmWebSetEWSfilesStatus": rlEmWebSetEWSfilesStatus,
       "rlEmbeddedWebApplied": rlEmbeddedWebApplied,
       "rlEmWebHttpPort": rlEmWebHttpPort,
       "rlEmWebHttpEnable": rlEmWebHttpEnable,
       "rlEmWebHttpsPort": rlEmWebHttpsPort,
       "rlEmWebHttpsEnable": rlEmWebHttpsEnable,
       "rlEmWebCertificateCountryName": rlEmWebCertificateCountryName,
       "rlEmWebCertificateStateOrProvinceName": rlEmWebCertificateStateOrProvinceName,
       "rlEmWebCertificateLocalityName": rlEmWebCertificateLocalityName,
       "rlEmWebCertificateOrganizationName": rlEmWebCertificateOrganizationName,
       "rlEmWebCertificateCommonName": rlEmWebCertificateCommonName,
       "rlEmWebCertificateRegenerate": rlEmWebCertificateRegenerate,
       "rlEmWebRsaKeyLength": rlEmWebRsaKeyLength,
       "rlEmWebDebug": rlEmWebDebug,
       "rlEmWebURL": rlEmWebURL,
       "rlEmWebDisplayNonPresentEntities": rlEmWebDisplayNonPresentEntities,
       "rlEmWebCertificateExists": rlEmWebCertificateExists,
       "rlEmWebHttpsActiveCertificateId": rlEmWebHttpsActiveCertificateId,
       "rlEmWebExtraPort": rlEmWebExtraPort,
       "rlEmWebExtraPortType": rlEmWebExtraPortType,
       "rlEmWebMaxHttpsIdleTimeout": rlEmWebMaxHttpsIdleTimeout,
       "rlEmWebServiceTable": rlEmWebServiceTable,
       "rlEmWebServiceEntry": rlEmWebServiceEntry,
       "rlEmWebServiceId": rlEmWebServiceId,
       "rlEmWebServiceName": rlEmWebServiceName,
       "rlEmWebServiceEnable": rlEmWebServiceEnable,
       "rlEmWebServicePort": rlEmWebServicePort,
       "rlEmWebServiceMaxUsers": rlEmWebServiceMaxUsers,
       "rlEmWebServiceProtocol": rlEmWebServiceProtocol,
       "rlEmWebServiceCertificateId": rlEmWebServiceCertificateId,
       "rlEmWebServiceMaxIdleTimeOut": rlEmWebServiceMaxIdleTimeOut}
)
