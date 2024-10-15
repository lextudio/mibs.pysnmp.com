# SNMP MIB module (SSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:48 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swSSLMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSSLMgmt_ObjectIdentity = ObjectIdentity
swSSLMgmt = _SwSSLMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 1)
)


class _SwSSLStatusAdmin_Type(Integer32):
    """Custom type swSSLStatusAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwSSLStatusAdmin_Type.__name__ = "Integer32"
_SwSSLStatusAdmin_Object = MibScalar
swSSLStatusAdmin = _SwSSLStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 1, 1),
    _SwSSLStatusAdmin_Type()
)
swSSLStatusAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSLStatusAdmin.setStatus("current")


class _SwSSLCipherSuites_Type(Bits):
    """Custom type swSSLCipherSuites based on Bits"""
    namedValues = NamedValues(
        *(("dhe-dss-with-3des-ede-cbc-sha", 2),
          ("rsa-export-with-rc4-40-md5", 3),
          ("rsa-with-3des-ede-cbc-sha", 1),
          ("rsa-with-rc4-128-MD5", 0))
    )

_SwSSLCipherSuites_Type.__name__ = "Bits"
_SwSSLCipherSuites_Object = MibScalar
swSSLCipherSuites = _SwSSLCipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 1, 2),
    _SwSSLCipherSuites_Type()
)
swSSLCipherSuites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSLCipherSuites.setStatus("current")


class _SwSSLCacheTimeout_Type(Unsigned32):
    """Custom type swSSLCacheTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_SwSSLCacheTimeout_Type.__name__ = "Unsigned32"
_SwSSLCacheTimeout_Object = MibScalar
swSSLCacheTimeout = _SwSSLCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 1, 3),
    _SwSSLCacheTimeout_Type()
)
swSSLCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSLCacheTimeout.setStatus("current")
_SwSSLCertificateFile_ObjectIdentity = ObjectIdentity
swSSLCertificateFile = _SwSSLCertificateFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 2)
)
_SwSSLCertificateFileIPAddr_Type = IpAddress
_SwSSLCertificateFileIPAddr_Object = MibScalar
swSSLCertificateFileIPAddr = _SwSSLCertificateFileIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 1),
    _SwSSLCertificateFileIPAddr_Type()
)
swSSLCertificateFileIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSLCertificateFileIPAddr.setStatus("current")


class _SwSSLCertificateFilePath_Type(DisplayString):
    """Custom type swSSLCertificateFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSSLCertificateFilePath_Type.__name__ = "DisplayString"
_SwSSLCertificateFilePath_Object = MibScalar
swSSLCertificateFilePath = _SwSSLCertificateFilePath_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 2),
    _SwSSLCertificateFilePath_Type()
)
swSSLCertificateFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSLCertificateFilePath.setStatus("current")


class _SwSSLCertificateKeyFilePath_Type(DisplayString):
    """Custom type swSSLCertificateKeyFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwSSLCertificateKeyFilePath_Type.__name__ = "DisplayString"
_SwSSLCertificateKeyFilePath_Object = MibScalar
swSSLCertificateKeyFilePath = _SwSSLCertificateKeyFilePath_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 3),
    _SwSSLCertificateKeyFilePath_Type()
)
swSSLCertificateKeyFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSLCertificateKeyFilePath.setStatus("current")


class _SwSSLCertificateFileCtrl_Type(Integer32):
    """Custom type swSSLCertificateFileCtrl based on Integer32"""
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
        *(("delete", 4),
          ("inactive", 2),
          ("other", 1),
          ("start", 3))
    )


_SwSSLCertificateFileCtrl_Type.__name__ = "Integer32"
_SwSSLCertificateFileCtrl_Object = MibScalar
swSSLCertificateFileCtrl = _SwSSLCertificateFileCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 4),
    _SwSSLCertificateFileCtrl_Type()
)
swSSLCertificateFileCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSSLCertificateFileCtrl.setStatus("current")


class _SwSSLCertificateFileShowSatus_Type(Integer32):
    """Custom type swSSLCertificateFileShowSatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsa", 3),
          ("none", 1),
          ("rsa", 2))
    )


_SwSSLCertificateFileShowSatus_Type.__name__ = "Integer32"
_SwSSLCertificateFileShowSatus_Object = MibScalar
swSSLCertificateFileShowSatus = _SwSSLCertificateFileShowSatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 7, 2, 5),
    _SwSSLCertificateFileShowSatus_Type()
)
swSSLCertificateFileShowSatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSSLCertificateFileShowSatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SSL-MIB",
    **{"swSSLMIB": swSSLMIB,
       "swSSLMgmt": swSSLMgmt,
       "swSSLStatusAdmin": swSSLStatusAdmin,
       "swSSLCipherSuites": swSSLCipherSuites,
       "swSSLCacheTimeout": swSSLCacheTimeout,
       "swSSLCertificateFile": swSSLCertificateFile,
       "swSSLCertificateFileIPAddr": swSSLCertificateFileIPAddr,
       "swSSLCertificateFilePath": swSSLCertificateFilePath,
       "swSSLCertificateKeyFilePath": swSSLCertificateKeyFilePath,
       "swSSLCertificateFileCtrl": swSSLCertificateFileCtrl,
       "swSSLCertificateFileShowSatus": swSSLCertificateFileShowSatus}
)
