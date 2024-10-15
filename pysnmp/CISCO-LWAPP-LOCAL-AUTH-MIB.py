# SNMP MIB module (CISCO-LWAPP-LOCAL-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-LOCAL-AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:39 2024
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

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappLocalAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619)
)
ciscoLwappLocalAuthMIB.setRevisions(
        ("2010-02-09 00:00",
         "2009-11-24 00:00",
         "2007-03-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappLocalAuthMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappLocalAuthMIBNotifs = _CiscoLwappLocalAuthMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 0)
)
_CiscoLwappLocalAuthMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappLocalAuthMIBObjects = _CiscoLwappLocalAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1)
)
_CllaConfig_ObjectIdentity = ObjectIdentity
cllaConfig = _CllaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1)
)
_CllaLocalAuth_ObjectIdentity = ObjectIdentity
cllaLocalAuth = _CllaLocalAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1)
)
_CllaActiveTimeout_Type = Unsigned32
_CllaActiveTimeout_Object = MibScalar
cllaActiveTimeout = _CllaActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 1),
    _CllaActiveTimeout_Type()
)
cllaActiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cllaActiveTimeout.setUnits("seconds")
_CllaEapIdentityReqTimeout_Type = Unsigned32
_CllaEapIdentityReqTimeout_Object = MibScalar
cllaEapIdentityReqTimeout = _CllaEapIdentityReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 2),
    _CllaEapIdentityReqTimeout_Type()
)
cllaEapIdentityReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapIdentityReqTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cllaEapIdentityReqTimeout.setUnits("seconds")
_CllaEapIdentityReqMaxRetries_Type = Unsigned32
_CllaEapIdentityReqMaxRetries_Object = MibScalar
cllaEapIdentityReqMaxRetries = _CllaEapIdentityReqMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 3),
    _CllaEapIdentityReqMaxRetries_Type()
)
cllaEapIdentityReqMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapIdentityReqMaxRetries.setStatus("current")


class _CllaEapDynamicWepKeyIndex_Type(Unsigned32):
    """Custom type cllaEapDynamicWepKeyIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CllaEapDynamicWepKeyIndex_Type.__name__ = "Unsigned32"
_CllaEapDynamicWepKeyIndex_Object = MibScalar
cllaEapDynamicWepKeyIndex = _CllaEapDynamicWepKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 4),
    _CllaEapDynamicWepKeyIndex_Type()
)
cllaEapDynamicWepKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapDynamicWepKeyIndex.setStatus("current")
_CllaEapReqTimeout_Type = Unsigned32
_CllaEapReqTimeout_Object = MibScalar
cllaEapReqTimeout = _CllaEapReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 5),
    _CllaEapReqTimeout_Type()
)
cllaEapReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapReqTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cllaEapReqTimeout.setUnits("seconds")
_CllaEapReqMaxRetries_Type = Unsigned32
_CllaEapReqMaxRetries_Object = MibScalar
cllaEapReqMaxRetries = _CllaEapReqMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 6),
    _CllaEapReqMaxRetries_Type()
)
cllaEapReqMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapReqMaxRetries.setStatus("current")


class _CllaEapMaxLoginIgnIdResp_Type(TruthValue):
    """Custom type cllaEapMaxLoginIgnIdResp based on TruthValue"""


_CllaEapMaxLoginIgnIdResp_Object = MibScalar
cllaEapMaxLoginIgnIdResp = _CllaEapMaxLoginIgnIdResp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 7),
    _CllaEapMaxLoginIgnIdResp_Type()
)
cllaEapMaxLoginIgnIdResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapMaxLoginIgnIdResp.setStatus("current")


class _CllaEapKeyTimeout_Type(Unsigned32):
    """Custom type cllaEapKeyTimeout based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 5000),
    )


_CllaEapKeyTimeout_Type.__name__ = "Unsigned32"
_CllaEapKeyTimeout_Object = MibScalar
cllaEapKeyTimeout = _CllaEapKeyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 8),
    _CllaEapKeyTimeout_Type()
)
cllaEapKeyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapKeyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cllaEapKeyTimeout.setUnits("milliseconds")


class _CllaEapKeyMaxRetries_Type(Unsigned32):
    """Custom type cllaEapKeyMaxRetries based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CllaEapKeyMaxRetries_Type.__name__ = "Unsigned32"
_CllaEapKeyMaxRetries_Object = MibScalar
cllaEapKeyMaxRetries = _CllaEapKeyMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 1, 9),
    _CllaEapKeyMaxRetries_Type()
)
cllaEapKeyMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapKeyMaxRetries.setStatus("current")
_CllaEapProfileTable_Object = MibTable
cllaEapProfileTable = _CllaEapProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cllaEapProfileTable.setStatus("current")
_CllaEapProfileEntry_Object = MibTableRow
cllaEapProfileEntry = _CllaEapProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1)
)
cllaEapProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileName"),
)
if mibBuilder.loadTexts:
    cllaEapProfileEntry.setStatus("current")


class _CllaEapProfileName_Type(DisplayString):
    """Custom type cllaEapProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CllaEapProfileName_Type.__name__ = "DisplayString"
_CllaEapProfileName_Object = MibTableColumn
cllaEapProfileName = _CllaEapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 1),
    _CllaEapProfileName_Type()
)
cllaEapProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cllaEapProfileName.setStatus("current")


class _CllaEapProfileMethods_Type(Bits):
    """Custom type cllaEapProfileMethods based on Bits"""
    namedValues = NamedValues(
        *(("eapFast", 2),
          ("leap", 1),
          ("none", 0),
          ("peap", 4),
          ("tls", 3))
    )

_CllaEapProfileMethods_Type.__name__ = "Bits"
_CllaEapProfileMethods_Object = MibTableColumn
cllaEapProfileMethods = _CllaEapProfileMethods_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 2),
    _CllaEapProfileMethods_Type()
)
cllaEapProfileMethods.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileMethods.setStatus("current")


class _CllaEapProfileCertIssuer_Type(Integer32):
    """Custom type cllaEapProfileCertIssuer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cisco", 1),
          ("vendor", 2))
    )


_CllaEapProfileCertIssuer_Type.__name__ = "Integer32"
_CllaEapProfileCertIssuer_Object = MibTableColumn
cllaEapProfileCertIssuer = _CllaEapProfileCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 3),
    _CllaEapProfileCertIssuer_Type()
)
cllaEapProfileCertIssuer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileCertIssuer.setStatus("current")


class _CllaEapProfileCaCertificationCheck_Type(TruthValue):
    """Custom type cllaEapProfileCaCertificationCheck based on TruthValue"""


_CllaEapProfileCaCertificationCheck_Object = MibTableColumn
cllaEapProfileCaCertificationCheck = _CllaEapProfileCaCertificationCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 4),
    _CllaEapProfileCaCertificationCheck_Type()
)
cllaEapProfileCaCertificationCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileCaCertificationCheck.setStatus("current")


class _CllaEapProfileCnCertificationIdVerify_Type(TruthValue):
    """Custom type cllaEapProfileCnCertificationIdVerify based on TruthValue"""


_CllaEapProfileCnCertificationIdVerify_Object = MibTableColumn
cllaEapProfileCnCertificationIdVerify = _CllaEapProfileCnCertificationIdVerify_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 5),
    _CllaEapProfileCnCertificationIdVerify_Type()
)
cllaEapProfileCnCertificationIdVerify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileCnCertificationIdVerify.setStatus("current")


class _CllaEapProfileDateValidityEnabled_Type(TruthValue):
    """Custom type cllaEapProfileDateValidityEnabled based on TruthValue"""


_CllaEapProfileDateValidityEnabled_Object = MibTableColumn
cllaEapProfileDateValidityEnabled = _CllaEapProfileDateValidityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 6),
    _CllaEapProfileDateValidityEnabled_Type()
)
cllaEapProfileDateValidityEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileDateValidityEnabled.setStatus("current")


class _CllaEapProfileLocalCertificateRequired_Type(TruthValue):
    """Custom type cllaEapProfileLocalCertificateRequired based on TruthValue"""


_CllaEapProfileLocalCertificateRequired_Object = MibTableColumn
cllaEapProfileLocalCertificateRequired = _CllaEapProfileLocalCertificateRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 7),
    _CllaEapProfileLocalCertificateRequired_Type()
)
cllaEapProfileLocalCertificateRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileLocalCertificateRequired.setStatus("current")


class _CllaEapProfileClientCertificateRequired_Type(TruthValue):
    """Custom type cllaEapProfileClientCertificateRequired based on TruthValue"""


_CllaEapProfileClientCertificateRequired_Object = MibTableColumn
cllaEapProfileClientCertificateRequired = _CllaEapProfileClientCertificateRequired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 8),
    _CllaEapProfileClientCertificateRequired_Type()
)
cllaEapProfileClientCertificateRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileClientCertificateRequired.setStatus("current")
_CllaEapProfileRowStatus_Type = RowStatus
_CllaEapProfileRowStatus_Object = MibTableColumn
cllaEapProfileRowStatus = _CllaEapProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 2, 1, 9),
    _CllaEapProfileRowStatus_Type()
)
cllaEapProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cllaEapProfileRowStatus.setStatus("current")
_CllaWlanProfileTable_Object = MibTable
cllaWlanProfileTable = _CllaWlanProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cllaWlanProfileTable.setStatus("current")
_CllaWlanProfileEntry_Object = MibTableRow
cllaWlanProfileEntry = _CllaWlanProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 3, 1)
)
cllaWlanProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cllaWlanProfileEntry.setStatus("current")


class _CllaWlanProfileName_Type(DisplayString):
    """Custom type cllaWlanProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CllaWlanProfileName_Type.__name__ = "DisplayString"
_CllaWlanProfileName_Object = MibTableColumn
cllaWlanProfileName = _CllaWlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 3, 1, 1),
    _CllaWlanProfileName_Type()
)
cllaWlanProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaWlanProfileName.setStatus("current")
_CllaWlanProfileState_Type = TruthValue
_CllaWlanProfileState_Object = MibTableColumn
cllaWlanProfileState = _CllaWlanProfileState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 3, 1, 2),
    _CllaWlanProfileState_Type()
)
cllaWlanProfileState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaWlanProfileState.setStatus("current")
_CllaUserPriorityTable_Object = MibTable
cllaUserPriorityTable = _CllaUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cllaUserPriorityTable.setStatus("current")
_CllaUserPriorityEntry_Object = MibTableRow
cllaUserPriorityEntry = _CllaUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 4, 1)
)
cllaUserPriorityEntry.setIndexNames(
    (0, "CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaUserCredential"),
)
if mibBuilder.loadTexts:
    cllaUserPriorityEntry.setStatus("current")


class _CllaUserCredential_Type(Integer32):
    """Custom type cllaUserCredential based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ldap", 2),
          ("local", 1))
    )


_CllaUserCredential_Type.__name__ = "Integer32"
_CllaUserCredential_Object = MibTableColumn
cllaUserCredential = _CllaUserCredential_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 4, 1, 1),
    _CllaUserCredential_Type()
)
cllaUserCredential.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cllaUserCredential.setStatus("current")


class _CllaUserPriorityNumber_Type(Integer32):
    """Custom type cllaUserPriorityNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CllaUserPriorityNumber_Type.__name__ = "Integer32"
_CllaUserPriorityNumber_Object = MibTableColumn
cllaUserPriorityNumber = _CllaUserPriorityNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 4, 1, 2),
    _CllaUserPriorityNumber_Type()
)
cllaUserPriorityNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaUserPriorityNumber.setStatus("current")
_CllaEapParams_ObjectIdentity = ObjectIdentity
cllaEapParams = _CllaEapParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 5)
)


class _CllaEapMethodPacTtl_Type(Unsigned32):
    """Custom type cllaEapMethodPacTtl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CllaEapMethodPacTtl_Type.__name__ = "Unsigned32"
_CllaEapMethodPacTtl_Object = MibScalar
cllaEapMethodPacTtl = _CllaEapMethodPacTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 5, 1),
    _CllaEapMethodPacTtl_Type()
)
cllaEapMethodPacTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapMethodPacTtl.setStatus("current")
if mibBuilder.loadTexts:
    cllaEapMethodPacTtl.setUnits("days")


class _CllaEapAnonymousProvEnabled_Type(TruthValue):
    """Custom type cllaEapAnonymousProvEnabled based on TruthValue"""


_CllaEapAnonymousProvEnabled_Object = MibScalar
cllaEapAnonymousProvEnabled = _CllaEapAnonymousProvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 5, 2),
    _CllaEapAnonymousProvEnabled_Type()
)
cllaEapAnonymousProvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapAnonymousProvEnabled.setStatus("current")


class _CllaEapAuthorityId_Type(OctetString):
    """Custom type cllaEapAuthorityId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CllaEapAuthorityId_Type.__name__ = "OctetString"
_CllaEapAuthorityId_Object = MibScalar
cllaEapAuthorityId = _CllaEapAuthorityId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 5, 3),
    _CllaEapAuthorityId_Type()
)
cllaEapAuthorityId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapAuthorityId.setStatus("current")


class _CllaEapAuthorityInfo_Type(OctetString):
    """Custom type cllaEapAuthorityInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CllaEapAuthorityInfo_Type.__name__ = "OctetString"
_CllaEapAuthorityInfo_Object = MibScalar
cllaEapAuthorityInfo = _CllaEapAuthorityInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 5, 4),
    _CllaEapAuthorityInfo_Type()
)
cllaEapAuthorityInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapAuthorityInfo.setStatus("current")


class _CllaEapServerKey_Type(OctetString):
    """Custom type cllaEapServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CllaEapServerKey_Type.__name__ = "OctetString"
_CllaEapServerKey_Object = MibScalar
cllaEapServerKey = _CllaEapServerKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 5, 5),
    _CllaEapServerKey_Type()
)
cllaEapServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cllaEapServerKey.setStatus("current")


class _CllaEapAuthorityIdLength_Type(Unsigned32):
    """Custom type cllaEapAuthorityIdLength based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CllaEapAuthorityIdLength_Type.__name__ = "Unsigned32"
_CllaEapAuthorityIdLength_Object = MibScalar
cllaEapAuthorityIdLength = _CllaEapAuthorityIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 1, 1, 5, 6),
    _CllaEapAuthorityIdLength_Type()
)
cllaEapAuthorityIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cllaEapAuthorityIdLength.setStatus("current")
_CiscoLwappLocalAuthMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappLocalAuthMIBConform = _CiscoLwappLocalAuthMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 2)
)
_CiscoLwappLocalAuthMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappLocalAuthMIBCompliances = _CiscoLwappLocalAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 2, 1)
)
_CiscoLwappLocalAuthMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappLocalAuthMIBGroups = _CiscoLwappLocalAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 2, 2)
)

# Managed Objects groups

ciscoLwappLocalAuthMIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 2, 2, 1)
)
ciscoLwappLocalAuthMIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaActiveTimeout"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileMethods"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileCertIssuer"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileCaCertificationCheck"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileCnCertificationIdVerify"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileDateValidityEnabled"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileLocalCertificateRequired"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileClientCertificateRequired"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileRowStatus"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaWlanProfileName"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaWlanProfileState"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaUserPriorityNumber"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapMethodPacTtl"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAnonymousProvEnabled"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAuthorityId"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAuthorityInfo"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapServerKey"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAuthorityIdLength"))
)
if mibBuilder.loadTexts:
    ciscoLwappLocalAuthMIBConfigGroup.setStatus("deprecated")

ciscoLwappLocalAuthMIBConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 2, 2, 2)
)
ciscoLwappLocalAuthMIBConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaActiveTimeout"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapIdentityReqTimeout"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapIdentityReqMaxRetries"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapDynamicWepKeyIndex"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapReqTimeout"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapReqMaxRetries"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileMethods"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileCertIssuer"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileCaCertificationCheck"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileCnCertificationIdVerify"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileDateValidityEnabled"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileLocalCertificateRequired"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileClientCertificateRequired"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapProfileRowStatus"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaWlanProfileName"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaWlanProfileState"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaUserPriorityNumber"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapMethodPacTtl"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAnonymousProvEnabled"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAuthorityId"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAuthorityInfo"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapServerKey"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapAuthorityIdLength"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapMaxLoginIgnIdResp"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapKeyTimeout"),
        ("CISCO-LWAPP-LOCAL-AUTH-MIB", "cllaEapKeyMaxRetries"))
)
if mibBuilder.loadTexts:
    ciscoLwappLocalAuthMIBConfigGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappLocalAuthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappLocalAuthMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappLocalAuthMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 619, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappLocalAuthMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-LOCAL-AUTH-MIB",
    **{"ciscoLwappLocalAuthMIB": ciscoLwappLocalAuthMIB,
       "ciscoLwappLocalAuthMIBNotifs": ciscoLwappLocalAuthMIBNotifs,
       "ciscoLwappLocalAuthMIBObjects": ciscoLwappLocalAuthMIBObjects,
       "cllaConfig": cllaConfig,
       "cllaLocalAuth": cllaLocalAuth,
       "cllaActiveTimeout": cllaActiveTimeout,
       "cllaEapIdentityReqTimeout": cllaEapIdentityReqTimeout,
       "cllaEapIdentityReqMaxRetries": cllaEapIdentityReqMaxRetries,
       "cllaEapDynamicWepKeyIndex": cllaEapDynamicWepKeyIndex,
       "cllaEapReqTimeout": cllaEapReqTimeout,
       "cllaEapReqMaxRetries": cllaEapReqMaxRetries,
       "cllaEapMaxLoginIgnIdResp": cllaEapMaxLoginIgnIdResp,
       "cllaEapKeyTimeout": cllaEapKeyTimeout,
       "cllaEapKeyMaxRetries": cllaEapKeyMaxRetries,
       "cllaEapProfileTable": cllaEapProfileTable,
       "cllaEapProfileEntry": cllaEapProfileEntry,
       "cllaEapProfileName": cllaEapProfileName,
       "cllaEapProfileMethods": cllaEapProfileMethods,
       "cllaEapProfileCertIssuer": cllaEapProfileCertIssuer,
       "cllaEapProfileCaCertificationCheck": cllaEapProfileCaCertificationCheck,
       "cllaEapProfileCnCertificationIdVerify": cllaEapProfileCnCertificationIdVerify,
       "cllaEapProfileDateValidityEnabled": cllaEapProfileDateValidityEnabled,
       "cllaEapProfileLocalCertificateRequired": cllaEapProfileLocalCertificateRequired,
       "cllaEapProfileClientCertificateRequired": cllaEapProfileClientCertificateRequired,
       "cllaEapProfileRowStatus": cllaEapProfileRowStatus,
       "cllaWlanProfileTable": cllaWlanProfileTable,
       "cllaWlanProfileEntry": cllaWlanProfileEntry,
       "cllaWlanProfileName": cllaWlanProfileName,
       "cllaWlanProfileState": cllaWlanProfileState,
       "cllaUserPriorityTable": cllaUserPriorityTable,
       "cllaUserPriorityEntry": cllaUserPriorityEntry,
       "cllaUserCredential": cllaUserCredential,
       "cllaUserPriorityNumber": cllaUserPriorityNumber,
       "cllaEapParams": cllaEapParams,
       "cllaEapMethodPacTtl": cllaEapMethodPacTtl,
       "cllaEapAnonymousProvEnabled": cllaEapAnonymousProvEnabled,
       "cllaEapAuthorityId": cllaEapAuthorityId,
       "cllaEapAuthorityInfo": cllaEapAuthorityInfo,
       "cllaEapServerKey": cllaEapServerKey,
       "cllaEapAuthorityIdLength": cllaEapAuthorityIdLength,
       "ciscoLwappLocalAuthMIBConform": ciscoLwappLocalAuthMIBConform,
       "ciscoLwappLocalAuthMIBCompliances": ciscoLwappLocalAuthMIBCompliances,
       "ciscoLwappLocalAuthMIBCompliance": ciscoLwappLocalAuthMIBCompliance,
       "ciscoLwappLocalAuthMIBComplianceRev1": ciscoLwappLocalAuthMIBComplianceRev1,
       "ciscoLwappLocalAuthMIBGroups": ciscoLwappLocalAuthMIBGroups,
       "ciscoLwappLocalAuthMIBConfigGroup": ciscoLwappLocalAuthMIBConfigGroup,
       "ciscoLwappLocalAuthMIBConfigGroupSup1": ciscoLwappLocalAuthMIBConfigGroupSup1}
)
