# SNMP MIB module (STN-IKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-IKE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:07 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(stnSystems,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnSystems")


# MODULE-IDENTITY

stnIKE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnIkeObjects_ObjectIdentity = ObjectIdentity
stnIkeObjects = _StnIkeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1)
)
_StnIkePreferences_ObjectIdentity = ObjectIdentity
stnIkePreferences = _StnIkePreferences_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1)
)
_StnIkePreferenceTable_Object = MibTable
stnIkePreferenceTable = _StnIkePreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnIkePreferenceTable.setStatus("current")
_StnIkePreferenceEntry_Object = MibTableRow
stnIkePreferenceEntry = _StnIkePreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1)
)
stnIkePreferenceEntry.setIndexNames(
    (0, "STN-IKE-MIB", "stnIkePrefPeerAddress"),
    (0, "STN-IKE-MIB", "stnIkePrefTransform"),
)
if mibBuilder.loadTexts:
    stnIkePreferenceEntry.setStatus("current")
_StnIkePrefPeerAddress_Type = IpAddress
_StnIkePrefPeerAddress_Object = MibTableColumn
stnIkePrefPeerAddress = _StnIkePrefPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 1),
    _StnIkePrefPeerAddress_Type()
)
stnIkePrefPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefPeerAddress.setStatus("current")
_StnIkePrefTransform_Type = Integer32
_StnIkePrefTransform_Object = MibTableColumn
stnIkePrefTransform = _StnIkePrefTransform_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 2),
    _StnIkePrefTransform_Type()
)
stnIkePrefTransform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefTransform.setStatus("current")


class _StnIkePrefPeerPort_Type(Integer32):
    """Custom type stnIkePrefPeerPort based on Integer32"""
    defaultValue = 500


_StnIkePrefPeerPort_Object = MibTableColumn
stnIkePrefPeerPort = _StnIkePrefPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 3),
    _StnIkePrefPeerPort_Type()
)
stnIkePrefPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefPeerPort.setStatus("current")


class _StnIkePrefHash_Type(Integer32):
    """Custom type stnIkePrefHash based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmac-md5", 1),
          ("hmac-sha", 2))
    )


_StnIkePrefHash_Type.__name__ = "Integer32"
_StnIkePrefHash_Object = MibTableColumn
stnIkePrefHash = _StnIkePrefHash_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 4),
    _StnIkePrefHash_Type()
)
stnIkePrefHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefHash.setStatus("current")


class _StnIkePrefEncryption_Type(Integer32):
    """Custom type stnIkePrefEncryption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blowfish-cbc", 3),
          ("des-cbc", 1),
          ("des3-cbc", 5),
          ("idea-cbc", 2),
          ("rc5-r16-b64-cbc", 4))
    )


_StnIkePrefEncryption_Type.__name__ = "Integer32"
_StnIkePrefEncryption_Object = MibTableColumn
stnIkePrefEncryption = _StnIkePrefEncryption_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 5),
    _StnIkePrefEncryption_Type()
)
stnIkePrefEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefEncryption.setStatus("current")


class _StnIkePrefAuthentication_Type(Integer32):
    """Custom type stnIkePrefAuthentication based on Integer32"""
    defaultValue = 1

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
        *(("dss-sig", 2),
          ("rsa-enc", 4),
          ("rsa-sig", 3),
          ("shared", 1))
    )


_StnIkePrefAuthentication_Type.__name__ = "Integer32"
_StnIkePrefAuthentication_Object = MibTableColumn
stnIkePrefAuthentication = _StnIkePrefAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 6),
    _StnIkePrefAuthentication_Type()
)
stnIkePrefAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefAuthentication.setStatus("current")


class _StnIkePrefDHGroup_Type(Integer32):
    """Custom type stnIkePrefDHGroup based on Integer32"""
    defaultValue = 1


_StnIkePrefDHGroup_Object = MibTableColumn
stnIkePrefDHGroup = _StnIkePrefDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 7),
    _StnIkePrefDHGroup_Type()
)
stnIkePrefDHGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefDHGroup.setStatus("current")


class _StnIkePrefMode_Type(Integer32):
    """Custom type stnIkePrefMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 4),
          ("main", 2))
    )


_StnIkePrefMode_Type.__name__ = "Integer32"
_StnIkePrefMode_Object = MibTableColumn
stnIkePrefMode = _StnIkePrefMode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 8),
    _StnIkePrefMode_Type()
)
stnIkePrefMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefMode.setStatus("current")
_StnIkePrefLifeTime_Type = TimeStamp
_StnIkePrefLifeTime_Object = MibTableColumn
stnIkePrefLifeTime = _StnIkePrefLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 9),
    _StnIkePrefLifeTime_Type()
)
stnIkePrefLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefLifeTime.setStatus("current")
_StnIkePrefLifeBytes_Type = Integer32
_StnIkePrefLifeBytes_Object = MibTableColumn
stnIkePrefLifeBytes = _StnIkePrefLifeBytes_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 10),
    _StnIkePrefLifeBytes_Type()
)
stnIkePrefLifeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefLifeBytes.setStatus("current")


class _StnIkePrefCertAlias_Type(OctetString):
    """Custom type stnIkePrefCertAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnIkePrefCertAlias_Type.__name__ = "OctetString"
_StnIkePrefCertAlias_Object = MibTableColumn
stnIkePrefCertAlias = _StnIkePrefCertAlias_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 11),
    _StnIkePrefCertAlias_Type()
)
stnIkePrefCertAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefCertAlias.setStatus("current")


class _StnIkePrefServiceName_Type(OctetString):
    """Custom type stnIkePrefServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnIkePrefServiceName_Type.__name__ = "OctetString"
_StnIkePrefServiceName_Object = MibTableColumn
stnIkePrefServiceName = _StnIkePrefServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 1, 1, 1, 12),
    _StnIkePrefServiceName_Type()
)
stnIkePrefServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkePrefServiceName.setStatus("current")
_StnIkeSharedSecrets_ObjectIdentity = ObjectIdentity
stnIkeSharedSecrets = _StnIkeSharedSecrets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2)
)
_StnIkeSharedSecretTable_Object = MibTable
stnIkeSharedSecretTable = _StnIkeSharedSecretTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stnIkeSharedSecretTable.setStatus("current")
_StnIkeSharedSecretEntry_Object = MibTableRow
stnIkeSharedSecretEntry = _StnIkeSharedSecretEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1, 1)
)
stnIkeSharedSecretEntry.setIndexNames(
    (0, "STN-IKE-MIB", "stnIkeSSPeerAddress"),
)
if mibBuilder.loadTexts:
    stnIkeSharedSecretEntry.setStatus("current")
_StnIkeSSPeerAddress_Type = IpAddress
_StnIkeSSPeerAddress_Object = MibTableColumn
stnIkeSSPeerAddress = _StnIkeSSPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1, 1, 1),
    _StnIkeSSPeerAddress_Type()
)
stnIkeSSPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkeSSPeerAddress.setStatus("current")


class _StnIkeSSSecret_Type(OctetString):
    """Custom type stnIkeSSSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnIkeSSSecret_Type.__name__ = "OctetString"
_StnIkeSSSecret_Object = MibTableColumn
stnIkeSSSecret = _StnIkeSSSecret_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 2, 1, 1, 2),
    _StnIkeSSSecret_Type()
)
stnIkeSSSecret.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnIkeSSSecret.setStatus("current")
_StnIkeCertificates_ObjectIdentity = ObjectIdentity
stnIkeCertificates = _StnIkeCertificates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3)
)
_StnIkeCertificateTable_Object = MibTable
stnIkeCertificateTable = _StnIkeCertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stnIkeCertificateTable.setStatus("current")
_StnIkeCertificateEntry_Object = MibTableRow
stnIkeCertificateEntry = _StnIkeCertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1)
)
stnIkeCertificateEntry.setIndexNames(
    (0, "STN-IKE-MIB", "stnIkeCertificateIndex"),
)
if mibBuilder.loadTexts:
    stnIkeCertificateEntry.setStatus("current")
_StnIkeCertificateIndex_Type = Integer32
_StnIkeCertificateIndex_Object = MibTableColumn
stnIkeCertificateIndex = _StnIkeCertificateIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 1),
    _StnIkeCertificateIndex_Type()
)
stnIkeCertificateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkeCertificateIndex.setStatus("current")


class _StnIkeCertificateType_Type(Integer32):
    """Custom type stnIkeCertificateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crl", 3),
          ("mine", 1),
          ("root", 2))
    )


_StnIkeCertificateType_Type.__name__ = "Integer32"
_StnIkeCertificateType_Object = MibTableColumn
stnIkeCertificateType = _StnIkeCertificateType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 2),
    _StnIkeCertificateType_Type()
)
stnIkeCertificateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkeCertificateType.setStatus("current")


class _StnIkeCertificateAlias_Type(OctetString):
    """Custom type stnIkeCertificateAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnIkeCertificateAlias_Type.__name__ = "OctetString"
_StnIkeCertificateAlias_Object = MibTableColumn
stnIkeCertificateAlias = _StnIkeCertificateAlias_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 3),
    _StnIkeCertificateAlias_Type()
)
stnIkeCertificateAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkeCertificateAlias.setStatus("current")


class _StnIkeCertificateDN_Type(OctetString):
    """Custom type stnIkeCertificateDN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnIkeCertificateDN_Type.__name__ = "OctetString"
_StnIkeCertificateDN_Object = MibTableColumn
stnIkeCertificateDN = _StnIkeCertificateDN_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 4),
    _StnIkeCertificateDN_Type()
)
stnIkeCertificateDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkeCertificateDN.setStatus("current")


class _StnIkeCertificateAltName_Type(OctetString):
    """Custom type stnIkeCertificateAltName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnIkeCertificateAltName_Type.__name__ = "OctetString"
_StnIkeCertificateAltName_Object = MibTableColumn
stnIkeCertificateAltName = _StnIkeCertificateAltName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 5),
    _StnIkeCertificateAltName_Type()
)
stnIkeCertificateAltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkeCertificateAltName.setStatus("current")


class _StnIkeCertificateIssuer_Type(OctetString):
    """Custom type stnIkeCertificateIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_StnIkeCertificateIssuer_Type.__name__ = "OctetString"
_StnIkeCertificateIssuer_Object = MibTableColumn
stnIkeCertificateIssuer = _StnIkeCertificateIssuer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 1, 3, 1, 1, 6),
    _StnIkeCertificateIssuer_Type()
)
stnIkeCertificateIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnIkeCertificateIssuer.setStatus("current")
_StnIkeMibConformance_ObjectIdentity = ObjectIdentity
stnIkeMibConformance = _StnIkeMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 8, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-IKE-MIB",
    **{"stnIKE": stnIKE,
       "stnIkeObjects": stnIkeObjects,
       "stnIkePreferences": stnIkePreferences,
       "stnIkePreferenceTable": stnIkePreferenceTable,
       "stnIkePreferenceEntry": stnIkePreferenceEntry,
       "stnIkePrefPeerAddress": stnIkePrefPeerAddress,
       "stnIkePrefTransform": stnIkePrefTransform,
       "stnIkePrefPeerPort": stnIkePrefPeerPort,
       "stnIkePrefHash": stnIkePrefHash,
       "stnIkePrefEncryption": stnIkePrefEncryption,
       "stnIkePrefAuthentication": stnIkePrefAuthentication,
       "stnIkePrefDHGroup": stnIkePrefDHGroup,
       "stnIkePrefMode": stnIkePrefMode,
       "stnIkePrefLifeTime": stnIkePrefLifeTime,
       "stnIkePrefLifeBytes": stnIkePrefLifeBytes,
       "stnIkePrefCertAlias": stnIkePrefCertAlias,
       "stnIkePrefServiceName": stnIkePrefServiceName,
       "stnIkeSharedSecrets": stnIkeSharedSecrets,
       "stnIkeSharedSecretTable": stnIkeSharedSecretTable,
       "stnIkeSharedSecretEntry": stnIkeSharedSecretEntry,
       "stnIkeSSPeerAddress": stnIkeSSPeerAddress,
       "stnIkeSSSecret": stnIkeSSSecret,
       "stnIkeCertificates": stnIkeCertificates,
       "stnIkeCertificateTable": stnIkeCertificateTable,
       "stnIkeCertificateEntry": stnIkeCertificateEntry,
       "stnIkeCertificateIndex": stnIkeCertificateIndex,
       "stnIkeCertificateType": stnIkeCertificateType,
       "stnIkeCertificateAlias": stnIkeCertificateAlias,
       "stnIkeCertificateDN": stnIkeCertificateDN,
       "stnIkeCertificateAltName": stnIkeCertificateAltName,
       "stnIkeCertificateIssuer": stnIkeCertificateIssuer,
       "stnIkeMibConformance": stnIkeMibConformance}
)
