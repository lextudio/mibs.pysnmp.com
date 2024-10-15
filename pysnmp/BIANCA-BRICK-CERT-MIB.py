# SNMP MIB module (BIANCA-BRICK-CERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-CERT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:23 2024
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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Ipsec_ObjectIdentity = ObjectIdentity
ipsec = _Ipsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26)
)
_Cert_ObjectIdentity = ObjectIdentity
cert = _Cert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33)
)
_CertGlobals_ObjectIdentity = ObjectIdentity
certGlobals = _CertGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1)
)
_CertGlobHttpProxy_Type = DisplayString
_CertGlobHttpProxy_Object = MibScalar
certGlobHttpProxy = _CertGlobHttpProxy_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 1),
    _CertGlobHttpProxy_Type()
)
certGlobHttpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobHttpProxy.setStatus("mandatory")
_CertGlobSocksServer_Type = DisplayString
_CertGlobSocksServer_Object = MibScalar
certGlobSocksServer = _CertGlobSocksServer_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 2),
    _CertGlobSocksServer_Type()
)
certGlobSocksServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobSocksServer.setStatus("mandatory")
_CertGlobMaxCacheEntries_Type = Integer32
_CertGlobMaxCacheEntries_Object = MibScalar
certGlobMaxCacheEntries = _CertGlobMaxCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 3),
    _CertGlobMaxCacheEntries_Type()
)
certGlobMaxCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobMaxCacheEntries.setStatus("mandatory")
_CertGlobMaxPathLength_Type = Integer32
_CertGlobMaxPathLength_Object = MibScalar
certGlobMaxPathLength = _CertGlobMaxPathLength_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 4),
    _CertGlobMaxPathLength_Type()
)
certGlobMaxPathLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobMaxPathLength.setStatus("mandatory")
_CertGlobMaxRestarts_Type = Integer32
_CertGlobMaxRestarts_Object = MibScalar
certGlobMaxRestarts = _CertGlobMaxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 5),
    _CertGlobMaxRestarts_Type()
)
certGlobMaxRestarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobMaxRestarts.setStatus("mandatory")
_CertGlobMaxCertValidity_Type = Integer32
_CertGlobMaxCertValidity_Object = MibScalar
certGlobMaxCertValidity = _CertGlobMaxCertValidity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 6),
    _CertGlobMaxCertValidity_Type()
)
certGlobMaxCertValidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobMaxCertValidity.setStatus("mandatory")
_CertGlobMaxCrlValidity_Type = Integer32
_CertGlobMaxCrlValidity_Object = MibScalar
certGlobMaxCrlValidity = _CertGlobMaxCrlValidity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 7),
    _CertGlobMaxCrlValidity_Type()
)
certGlobMaxCrlValidity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobMaxCrlValidity.setStatus("mandatory")
_CertGlobNegCachePeriod_Type = Integer32
_CertGlobNegCachePeriod_Object = MibScalar
certGlobNegCachePeriod = _CertGlobNegCachePeriod_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 1, 8),
    _CertGlobNegCachePeriod_Type()
)
certGlobNegCachePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certGlobNegCachePeriod.setStatus("mandatory")
_CertServerTable_Object = MibTable
certServerTable = _CertServerTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 2)
)
if mibBuilder.loadTexts:
    certServerTable.setStatus("mandatory")
_CertServerEntry_Object = MibTableRow
certServerEntry = _CertServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 2, 1)
)
certServerEntry.setIndexNames(
    (0, "BIANCA-BRICK-CERT-MIB", "certServerPreference"),
)
if mibBuilder.loadTexts:
    certServerEntry.setStatus("mandatory")
_CertServerName_Type = DisplayString
_CertServerName_Object = MibTableColumn
certServerName = _CertServerName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 2, 1, 1),
    _CertServerName_Type()
)
certServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certServerName.setStatus("mandatory")
_CertServerUrl_Type = DisplayString
_CertServerUrl_Object = MibTableColumn
certServerUrl = _CertServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 2, 1, 2),
    _CertServerUrl_Type()
)
certServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certServerUrl.setStatus("mandatory")
_CertServerPreference_Type = Integer32
_CertServerPreference_Object = MibTableColumn
certServerPreference = _CertServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 2, 1, 3),
    _CertServerPreference_Type()
)
certServerPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certServerPreference.setStatus("mandatory")


class _CertServerType_Type(Integer32):
    """Custom type certServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("server", 2))
    )


_CertServerType_Type.__name__ = "Integer32"
_CertServerType_Object = MibTableColumn
certServerType = _CertServerType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 2, 1, 4),
    _CertServerType_Type()
)
certServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certServerType.setStatus("mandatory")
_CertTable_Object = MibTable
certTable = _CertTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3)
)
if mibBuilder.loadTexts:
    certTable.setStatus("mandatory")
_CertEntry_Object = MibTableRow
certEntry = _CertEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1)
)
certEntry.setIndexNames(
    (0, "BIANCA-BRICK-CERT-MIB", "certIndex"),
)
if mibBuilder.loadTexts:
    certEntry.setStatus("mandatory")
_CertIndex_Type = Integer32
_CertIndex_Object = MibTableColumn
certIndex = _CertIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 1),
    _CertIndex_Type()
)
certIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certIndex.setStatus("mandatory")
_CertDescription_Type = DisplayString
_CertDescription_Object = MibTableColumn
certDescription = _CertDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 2),
    _CertDescription_Type()
)
certDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certDescription.setStatus("mandatory")


class _CertIsCA_Type(Integer32):
    """Custom type certIsCA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CertIsCA_Type.__name__ = "Integer32"
_CertIsCA_Object = MibTableColumn
certIsCA = _CertIsCA_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 3),
    _CertIsCA_Type()
)
certIsCA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certIsCA.setStatus("mandatory")


class _CertForceTrusted_Type(Integer32):
    """Custom type certForceTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CertForceTrusted_Type.__name__ = "Integer32"
_CertForceTrusted_Object = MibTableColumn
certForceTrusted = _CertForceTrusted_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 4),
    _CertForceTrusted_Type()
)
certForceTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certForceTrusted.setStatus("mandatory")


class _CertNoCrls_Type(Integer32):
    """Custom type certNoCrls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_CertNoCrls_Type.__name__ = "Integer32"
_CertNoCrls_Object = MibTableColumn
certNoCrls = _CertNoCrls_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 5),
    _CertNoCrls_Type()
)
certNoCrls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certNoCrls.setStatus("mandatory")
_CertSerialNumber_Type = DisplayString
_CertSerialNumber_Object = MibTableColumn
certSerialNumber = _CertSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 6),
    _CertSerialNumber_Type()
)
certSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSerialNumber.setStatus("mandatory")
_CertSubjectName_Type = DisplayString
_CertSubjectName_Object = MibTableColumn
certSubjectName = _CertSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 7),
    _CertSubjectName_Type()
)
certSubjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSubjectName.setStatus("mandatory")
_CertSubjectAltNames_Type = DisplayString
_CertSubjectAltNames_Object = MibTableColumn
certSubjectAltNames = _CertSubjectAltNames_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 8),
    _CertSubjectAltNames_Type()
)
certSubjectAltNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSubjectAltNames.setStatus("mandatory")
_CertIssuerName_Type = DisplayString
_CertIssuerName_Object = MibTableColumn
certIssuerName = _CertIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 9),
    _CertIssuerName_Type()
)
certIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certIssuerName.setStatus("mandatory")
_CertIssuerAltNames_Type = DisplayString
_CertIssuerAltNames_Object = MibTableColumn
certIssuerAltNames = _CertIssuerAltNames_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 10),
    _CertIssuerAltNames_Type()
)
certIssuerAltNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certIssuerAltNames.setStatus("mandatory")
_CertValidity_Type = DisplayString
_CertValidity_Object = MibTableColumn
certValidity = _CertValidity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 11),
    _CertValidity_Type()
)
certValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certValidity.setStatus("mandatory")
_CertPubKeyInfo_Type = DisplayString
_CertPubKeyInfo_Object = MibTableColumn
certPubKeyInfo = _CertPubKeyInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 12),
    _CertPubKeyInfo_Type()
)
certPubKeyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certPubKeyInfo.setStatus("mandatory")
_CertKeyId_Type = OctetString
_CertKeyId_Object = MibTableColumn
certKeyId = _CertKeyId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 13),
    _CertKeyId_Type()
)
certKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certKeyId.setStatus("mandatory")
_CertPrivateKey_Type = Integer32
_CertPrivateKey_Object = MibTableColumn
certPrivateKey = _CertPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 14),
    _CertPrivateKey_Type()
)
certPrivateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certPrivateKey.setStatus("mandatory")
_CertMD5Fingerprint_Type = OctetString
_CertMD5Fingerprint_Object = MibTableColumn
certMD5Fingerprint = _CertMD5Fingerprint_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 24),
    _CertMD5Fingerprint_Type()
)
certMD5Fingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certMD5Fingerprint.setStatus("mandatory")
_CertSHA1Fingerprint_Type = OctetString
_CertSHA1Fingerprint_Object = MibTableColumn
certSHA1Fingerprint = _CertSHA1Fingerprint_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 3, 1, 25),
    _CertSHA1Fingerprint_Type()
)
certSHA1Fingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSHA1Fingerprint.setStatus("mandatory")
_CertRevListTable_Object = MibTable
certRevListTable = _CertRevListTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6)
)
if mibBuilder.loadTexts:
    certRevListTable.setStatus("mandatory")
_CertRevListEntry_Object = MibTableRow
certRevListEntry = _CertRevListEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1)
)
certRevListEntry.setIndexNames(
    (0, "BIANCA-BRICK-CERT-MIB", "certRevListIndex"),
)
if mibBuilder.loadTexts:
    certRevListEntry.setStatus("mandatory")
_CertRevListIndex_Type = Integer32
_CertRevListIndex_Object = MibTableColumn
certRevListIndex = _CertRevListIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1, 1),
    _CertRevListIndex_Type()
)
certRevListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certRevListIndex.setStatus("mandatory")
_CertRevListDescription_Type = DisplayString
_CertRevListDescription_Object = MibTableColumn
certRevListDescription = _CertRevListDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1, 2),
    _CertRevListDescription_Type()
)
certRevListDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certRevListDescription.setStatus("mandatory")
_CertRevListIssuerName_Type = DisplayString
_CertRevListIssuerName_Object = MibTableColumn
certRevListIssuerName = _CertRevListIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1, 3),
    _CertRevListIssuerName_Type()
)
certRevListIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certRevListIssuerName.setStatus("mandatory")
_CertRevListIssuerAltNames_Type = DisplayString
_CertRevListIssuerAltNames_Object = MibTableColumn
certRevListIssuerAltNames = _CertRevListIssuerAltNames_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1, 4),
    _CertRevListIssuerAltNames_Type()
)
certRevListIssuerAltNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certRevListIssuerAltNames.setStatus("mandatory")
_CertRevListSerialNumber_Type = DisplayString
_CertRevListSerialNumber_Object = MibTableColumn
certRevListSerialNumber = _CertRevListSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1, 5),
    _CertRevListSerialNumber_Type()
)
certRevListSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certRevListSerialNumber.setStatus("mandatory")
_CertRevListValidity_Type = DisplayString
_CertRevListValidity_Object = MibTableColumn
certRevListValidity = _CertRevListValidity_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1, 6),
    _CertRevListValidity_Type()
)
certRevListValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certRevListValidity.setStatus("mandatory")
_CertRevListNumCerts_Type = Integer32
_CertRevListNumCerts_Object = MibTableColumn
certRevListNumCerts = _CertRevListNumCerts_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 26, 33, 6, 1, 7),
    _CertRevListNumCerts_Type()
)
certRevListNumCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certRevListNumCerts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-CERT-MIB",
    **{"DisplayString": DisplayString,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "ipsec": ipsec,
       "cert": cert,
       "certGlobals": certGlobals,
       "certGlobHttpProxy": certGlobHttpProxy,
       "certGlobSocksServer": certGlobSocksServer,
       "certGlobMaxCacheEntries": certGlobMaxCacheEntries,
       "certGlobMaxPathLength": certGlobMaxPathLength,
       "certGlobMaxRestarts": certGlobMaxRestarts,
       "certGlobMaxCertValidity": certGlobMaxCertValidity,
       "certGlobMaxCrlValidity": certGlobMaxCrlValidity,
       "certGlobNegCachePeriod": certGlobNegCachePeriod,
       "certServerTable": certServerTable,
       "certServerEntry": certServerEntry,
       "certServerName": certServerName,
       "certServerUrl": certServerUrl,
       "certServerPreference": certServerPreference,
       "certServerType": certServerType,
       "certTable": certTable,
       "certEntry": certEntry,
       "certIndex": certIndex,
       "certDescription": certDescription,
       "certIsCA": certIsCA,
       "certForceTrusted": certForceTrusted,
       "certNoCrls": certNoCrls,
       "certSerialNumber": certSerialNumber,
       "certSubjectName": certSubjectName,
       "certSubjectAltNames": certSubjectAltNames,
       "certIssuerName": certIssuerName,
       "certIssuerAltNames": certIssuerAltNames,
       "certValidity": certValidity,
       "certPubKeyInfo": certPubKeyInfo,
       "certKeyId": certKeyId,
       "certPrivateKey": certPrivateKey,
       "certMD5Fingerprint": certMD5Fingerprint,
       "certSHA1Fingerprint": certSHA1Fingerprint,
       "certRevListTable": certRevListTable,
       "certRevListEntry": certRevListEntry,
       "certRevListIndex": certRevListIndex,
       "certRevListDescription": certRevListDescription,
       "certRevListIssuerName": certRevListIssuerName,
       "certRevListIssuerAltNames": certRevListIssuerAltNames,
       "certRevListSerialNumber": certRevListSerialNumber,
       "certRevListValidity": certRevListValidity,
       "certRevListNumCerts": certRevListNumCerts}
)
