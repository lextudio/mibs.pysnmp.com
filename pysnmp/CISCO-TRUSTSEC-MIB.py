# SNMP MIB module (CISCO-TRUSTSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TRUSTSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:49 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CtsAcsAuthorityIdentity,
 CtsCredentialRecordType,
 CtsGenerationId,
 CtsPasswordEncryptionType,
 CtsSecurityGroupTag) = mibBuilder.importSymbols(
    "CISCO-TRUSTSEC-TC-MIB",
    "CtsAcsAuthorityIdentity",
    "CtsCredentialRecordType",
    "CtsGenerationId",
    "CtsPasswordEncryptionType",
    "CtsSecurityGroupTag")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTrustSecMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730)
)
ciscoTrustSecMIB.setRevisions(
        ("2014-01-30 00:00",
         "2012-09-26 00:00",
         "2011-03-15 00:00",
         "2010-09-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTrustSecMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTrustSecMIBNotifs = _CiscoTrustSecMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 0)
)
_CiscoTrustSecMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTrustSecMIBObjects = _CiscoTrustSecMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1)
)
_CtsCacheObjects_ObjectIdentity = ObjectIdentity
ctsCacheObjects = _CtsCacheObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 1)
)
_CtsCacheEnabled_Type = TruthValue
_CtsCacheEnabled_Object = MibScalar
ctsCacheEnabled = _CtsCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 1, 1),
    _CtsCacheEnabled_Type()
)
ctsCacheEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCacheEnabled.setStatus("current")
_CtsCacheNvStorage_Type = SnmpAdminString
_CtsCacheNvStorage_Object = MibScalar
ctsCacheNvStorage = _CtsCacheNvStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 1, 2),
    _CtsCacheNvStorage_Type()
)
ctsCacheNvStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCacheNvStorage.setStatus("current")


class _CtsCacheClear_Type(Integer32):
    """Custom type ctsCacheClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("authzPolicies", 3),
          ("authzPoliciesPeer", 4),
          ("authzPoliciesSgt", 5),
          ("environmentData", 6),
          ("interfaceController", 7),
          ("none", 1))
    )


_CtsCacheClear_Type.__name__ = "Integer32"
_CtsCacheClear_Object = MibScalar
ctsCacheClear = _CtsCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 1, 3),
    _CtsCacheClear_Type()
)
ctsCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCacheClear.setStatus("current")
_CtsSgtObjects_ObjectIdentity = ObjectIdentity
ctsSgtObjects = _CtsSgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 2)
)
_CtsSecurityGroupTagId_Type = CtsSecurityGroupTag
_CtsSecurityGroupTagId_Object = MibScalar
ctsSecurityGroupTagId = _CtsSecurityGroupTagId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 2, 1),
    _CtsSecurityGroupTagId_Type()
)
ctsSecurityGroupTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSecurityGroupTagId.setStatus("current")


class _CtsSgtAssignmentMethod_Type(Integer32):
    """Custom type ctsSgtAssignmentMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 2),
          ("none", 1))
    )


_CtsSgtAssignmentMethod_Type.__name__ = "Integer32"
_CtsSgtAssignmentMethod_Object = MibScalar
ctsSgtAssignmentMethod = _CtsSgtAssignmentMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 2, 2),
    _CtsSgtAssignmentMethod_Type()
)
ctsSgtAssignmentMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSgtAssignmentMethod.setStatus("current")
_CtsCredentialObjects_ObjectIdentity = ObjectIdentity
ctsCredentialObjects = _CtsCredentialObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3)
)
_CtsDeviceId_Type = SnmpAdminString
_CtsDeviceId_Object = MibScalar
ctsDeviceId = _CtsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 1),
    _CtsDeviceId_Type()
)
ctsDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsDeviceId.setStatus("current")
_CtsDevicePasswordType_Type = CtsPasswordEncryptionType
_CtsDevicePasswordType_Object = MibScalar
ctsDevicePasswordType = _CtsDevicePasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 2),
    _CtsDevicePasswordType_Type()
)
ctsDevicePasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsDevicePasswordType.setStatus("current")
_CtsDevicePassword_Type = SnmpAdminString
_CtsDevicePassword_Object = MibScalar
ctsDevicePassword = _CtsDevicePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 3),
    _CtsDevicePassword_Type()
)
ctsDevicePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsDevicePassword.setStatus("current")


class _CtsKeystoreType_Type(Integer32):
    """Custom type ctsKeystoreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardwareKeystore", 1),
          ("softwareEmulation", 2))
    )


_CtsKeystoreType_Type.__name__ = "Integer32"
_CtsKeystoreType_Object = MibScalar
ctsKeystoreType = _CtsKeystoreType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 4),
    _CtsKeystoreType_Type()
)
ctsKeystoreType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreType.setStatus("current")
_CtsKeystoreFwVersion_Type = SnmpAdminString
_CtsKeystoreFwVersion_Object = MibScalar
ctsKeystoreFwVersion = _CtsKeystoreFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 5),
    _CtsKeystoreFwVersion_Type()
)
ctsKeystoreFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreFwVersion.setStatus("current")
_CtsKeystoreFwAlerts_Type = Counter32
_CtsKeystoreFwAlerts_Object = MibScalar
ctsKeystoreFwAlerts = _CtsKeystoreFwAlerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 6),
    _CtsKeystoreFwAlerts_Type()
)
ctsKeystoreFwAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreFwAlerts.setStatus("current")
_CtsKeystoreFwResets_Type = Counter32
_CtsKeystoreFwResets_Object = MibScalar
ctsKeystoreFwResets = _CtsKeystoreFwResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 7),
    _CtsKeystoreFwResets_Type()
)
ctsKeystoreFwResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreFwResets.setStatus("current")
_CtsKeystoreRxTimeouts_Type = Counter32
_CtsKeystoreRxTimeouts_Object = MibScalar
ctsKeystoreRxTimeouts = _CtsKeystoreRxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 8),
    _CtsKeystoreRxTimeouts_Type()
)
ctsKeystoreRxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreRxTimeouts.setStatus("current")
_CtsKeystoreRxBadChecksums_Type = Counter32
_CtsKeystoreRxBadChecksums_Object = MibScalar
ctsKeystoreRxBadChecksums = _CtsKeystoreRxBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 9),
    _CtsKeystoreRxBadChecksums_Type()
)
ctsKeystoreRxBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreRxBadChecksums.setStatus("current")
_CtsKeystoreRxBadFragmentLengths_Type = Counter32
_CtsKeystoreRxBadFragmentLengths_Object = MibScalar
ctsKeystoreRxBadFragmentLengths = _CtsKeystoreRxBadFragmentLengths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 10),
    _CtsKeystoreRxBadFragmentLengths_Type()
)
ctsKeystoreRxBadFragmentLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreRxBadFragmentLengths.setStatus("current")
_CtsKeystoreCorruptions_Type = Counter32
_CtsKeystoreCorruptions_Object = MibScalar
ctsKeystoreCorruptions = _CtsKeystoreCorruptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 11),
    _CtsKeystoreCorruptions_Type()
)
ctsKeystoreCorruptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystoreCorruptions.setStatus("current")
_CtsKeystorePasswordRecordTable_Object = MibTable
ctsKeystorePasswordRecordTable = _CtsKeystorePasswordRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 13)
)
if mibBuilder.loadTexts:
    ctsKeystorePasswordRecordTable.setStatus("current")
_CtsKeystorePasswordRecordEntry_Object = MibTableRow
ctsKeystorePasswordRecordEntry = _CtsKeystorePasswordRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 13, 1)
)
ctsKeystorePasswordRecordEntry.setIndexNames(
    (1, "CISCO-TRUSTSEC-MIB", "ctsKeystorePasswordRecordName"),
)
if mibBuilder.loadTexts:
    ctsKeystorePasswordRecordEntry.setStatus("current")


class _CtsKeystorePasswordRecordName_Type(SnmpAdminString):
    """Custom type ctsKeystorePasswordRecordName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsKeystorePasswordRecordName_Type.__name__ = "SnmpAdminString"
_CtsKeystorePasswordRecordName_Object = MibTableColumn
ctsKeystorePasswordRecordName = _CtsKeystorePasswordRecordName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 13, 1, 1),
    _CtsKeystorePasswordRecordName_Type()
)
ctsKeystorePasswordRecordName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsKeystorePasswordRecordName.setStatus("current")
_CtsKeystorePasswordRecordType_Type = CtsCredentialRecordType
_CtsKeystorePasswordRecordType_Object = MibTableColumn
ctsKeystorePasswordRecordType = _CtsKeystorePasswordRecordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 13, 1, 2),
    _CtsKeystorePasswordRecordType_Type()
)
ctsKeystorePasswordRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystorePasswordRecordType.setStatus("current")
_CtsKeystorePacRecordTable_Object = MibTable
ctsKeystorePacRecordTable = _CtsKeystorePacRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 14)
)
if mibBuilder.loadTexts:
    ctsKeystorePacRecordTable.setStatus("current")
_CtsKeystorePacRecordEntry_Object = MibTableRow
ctsKeystorePacRecordEntry = _CtsKeystorePacRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 14, 1)
)
ctsKeystorePacRecordEntry.setIndexNames(
    (1, "CISCO-TRUSTSEC-MIB", "ctsKeystorePacRecordName"),
)
if mibBuilder.loadTexts:
    ctsKeystorePacRecordEntry.setStatus("current")


class _CtsKeystorePacRecordName_Type(CtsAcsAuthorityIdentity):
    """Custom type ctsKeystorePacRecordName based on CtsAcsAuthorityIdentity"""
    subtypeSpec = CtsAcsAuthorityIdentity.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsKeystorePacRecordName_Type.__name__ = "CtsAcsAuthorityIdentity"
_CtsKeystorePacRecordName_Object = MibTableColumn
ctsKeystorePacRecordName = _CtsKeystorePacRecordName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 14, 1, 1),
    _CtsKeystorePacRecordName_Type()
)
ctsKeystorePacRecordName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsKeystorePacRecordName.setStatus("current")
_CtsKeystorePacRecordType_Type = CtsCredentialRecordType
_CtsKeystorePacRecordType_Object = MibTableColumn
ctsKeystorePacRecordType = _CtsKeystorePacRecordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 14, 1, 2),
    _CtsKeystorePacRecordType_Type()
)
ctsKeystorePacRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsKeystorePacRecordType.setStatus("current")
_CtsPacInfoTable_Object = MibTable
ctsPacInfoTable = _CtsPacInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15)
)
if mibBuilder.loadTexts:
    ctsPacInfoTable.setStatus("current")
_CtsPacInfoEntry_Object = MibTableRow
ctsPacInfoEntry = _CtsPacInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15, 1)
)
ctsPacInfoEntry.setIndexNames(
    (1, "CISCO-TRUSTSEC-MIB", "ctsPacAcsAuthId"),
)
if mibBuilder.loadTexts:
    ctsPacInfoEntry.setStatus("current")


class _CtsPacAcsAuthId_Type(CtsAcsAuthorityIdentity):
    """Custom type ctsPacAcsAuthId based on CtsAcsAuthorityIdentity"""
    subtypeSpec = CtsAcsAuthorityIdentity.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsPacAcsAuthId_Type.__name__ = "CtsAcsAuthorityIdentity"
_CtsPacAcsAuthId_Object = MibTableColumn
ctsPacAcsAuthId = _CtsPacAcsAuthId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15, 1, 1),
    _CtsPacAcsAuthId_Type()
)
ctsPacAcsAuthId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsPacAcsAuthId.setStatus("current")
_CtsPacAcsDescription_Type = SnmpAdminString
_CtsPacAcsDescription_Object = MibTableColumn
ctsPacAcsDescription = _CtsPacAcsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15, 1, 2),
    _CtsPacAcsDescription_Type()
)
ctsPacAcsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsPacAcsDescription.setStatus("current")


class _CtsPacType_Type(Integer32):
    """Custom type ctsPacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ciscoTrustSec", 6),
          ("machineAuthentication", 3),
          ("posture", 5),
          ("tunnel", 2),
          ("unknown", 1),
          ("userAuthorization", 4))
    )


_CtsPacType_Type.__name__ = "Integer32"
_CtsPacType_Object = MibTableColumn
ctsPacType = _CtsPacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15, 1, 3),
    _CtsPacType_Type()
)
ctsPacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsPacType.setStatus("current")
_CtsPacExpirationTime_Type = DateAndTime
_CtsPacExpirationTime_Object = MibTableColumn
ctsPacExpirationTime = _CtsPacExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15, 1, 4),
    _CtsPacExpirationTime_Type()
)
ctsPacExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsPacExpirationTime.setStatus("current")
_CtsPacTimeToRefresh_Type = Unsigned32
_CtsPacTimeToRefresh_Object = MibTableColumn
ctsPacTimeToRefresh = _CtsPacTimeToRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15, 1, 5),
    _CtsPacTimeToRefresh_Type()
)
ctsPacTimeToRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsPacTimeToRefresh.setStatus("current")
if mibBuilder.loadTexts:
    ctsPacTimeToRefresh.setUnits("seconds")
_CtsPacStatus_Type = RowStatus
_CtsPacStatus_Object = MibTableColumn
ctsPacStatus = _CtsPacStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 15, 1, 6),
    _CtsPacStatus_Type()
)
ctsPacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsPacStatus.setStatus("current")
_CtsCredentialsClearAll_Type = TruthValue
_CtsCredentialsClearAll_Object = MibScalar
ctsCredentialsClearAll = _CtsCredentialsClearAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 3, 16),
    _CtsCredentialsClearAll_Type()
)
ctsCredentialsClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCredentialsClearAll.setStatus("current")
_CtsEnvironmentDataObjects_ObjectIdentity = ObjectIdentity
ctsEnvironmentDataObjects = _CtsEnvironmentDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4)
)


class _CtsEnvDataLastDownloadStatus_Type(Integer32):
    """Custom type ctsEnvDataLastDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 7),
          ("failed", 3),
          ("incomplete", 5),
          ("inprogress", 4),
          ("other", 1),
          ("succeeded", 2),
          ("timedout", 6))
    )


_CtsEnvDataLastDownloadStatus_Type.__name__ = "Integer32"
_CtsEnvDataLastDownloadStatus_Object = MibScalar
ctsEnvDataLastDownloadStatus = _CtsEnvDataLastDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 1),
    _CtsEnvDataLastDownloadStatus_Type()
)
ctsEnvDataLastDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvDataLastDownloadStatus.setStatus("current")
_CtsEnvSecurityGroupTagId_Type = CtsSecurityGroupTag
_CtsEnvSecurityGroupTagId_Object = MibScalar
ctsEnvSecurityGroupTagId = _CtsEnvSecurityGroupTagId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 2),
    _CtsEnvSecurityGroupTagId_Type()
)
ctsEnvSecurityGroupTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupTagId.setStatus("current")
_CtsEnvSecurityGroupTagGenId_Type = CtsGenerationId
_CtsEnvSecurityGroupTagGenId_Object = MibScalar
ctsEnvSecurityGroupTagGenId = _CtsEnvSecurityGroupTagGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 3),
    _CtsEnvSecurityGroupTagGenId_Type()
)
ctsEnvSecurityGroupTagGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupTagGenId.setStatus("current")
_CtsEnvDataLastUpdate_Type = DateAndTime
_CtsEnvDataLastUpdate_Object = MibScalar
ctsEnvDataLastUpdate = _CtsEnvDataLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 4),
    _CtsEnvDataLastUpdate_Type()
)
ctsEnvDataLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvDataLastUpdate.setStatus("current")
_CtsEnvDataRefreshInterval_Type = Unsigned32
_CtsEnvDataRefreshInterval_Object = MibScalar
ctsEnvDataRefreshInterval = _CtsEnvDataRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 5),
    _CtsEnvDataRefreshInterval_Type()
)
ctsEnvDataRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvDataRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsEnvDataRefreshInterval.setUnits("seconds")
_CtsEnvDataTimeLeft_Type = Unsigned32
_CtsEnvDataTimeLeft_Object = MibScalar
ctsEnvDataTimeLeft = _CtsEnvDataTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 6),
    _CtsEnvDataTimeLeft_Type()
)
ctsEnvDataTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvDataTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    ctsEnvDataTimeLeft.setUnits("seconds")
_CtsEnvDataTimeToRefresh_Type = Unsigned32
_CtsEnvDataTimeToRefresh_Object = MibScalar
ctsEnvDataTimeToRefresh = _CtsEnvDataTimeToRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 7),
    _CtsEnvDataTimeToRefresh_Type()
)
ctsEnvDataTimeToRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvDataTimeToRefresh.setStatus("current")
if mibBuilder.loadTexts:
    ctsEnvDataTimeToRefresh.setUnits("seconds")


class _CtsEnvDataSource_Type(Integer32):
    """Custom type ctsEnvDataSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cached", 2),
          ("downloaded", 3),
          ("none", 1))
    )


_CtsEnvDataSource_Type.__name__ = "Integer32"
_CtsEnvDataSource_Object = MibScalar
ctsEnvDataSource = _CtsEnvDataSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 8),
    _CtsEnvDataSource_Type()
)
ctsEnvDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvDataSource.setStatus("current")


class _CtsEnvDataAction_Type(Integer32):
    """Custom type ctsEnvDataAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_CtsEnvDataAction_Type.__name__ = "Integer32"
_CtsEnvDataAction_Object = MibScalar
ctsEnvDataAction = _CtsEnvDataAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 9),
    _CtsEnvDataAction_Type()
)
ctsEnvDataAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsEnvDataAction.setStatus("current")
_CtsEnvSecurityGroupNameTable_Object = MibTable
ctsEnvSecurityGroupNameTable = _CtsEnvSecurityGroupNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 16)
)
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupNameTable.setStatus("current")
_CtsEnvSecurityGroupNameEntry_Object = MibTableRow
ctsEnvSecurityGroupNameEntry = _CtsEnvSecurityGroupNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 16, 1)
)
ctsEnvSecurityGroupNameEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-MIB", "ctsEnvSecurityGroupNameSgt"),
)
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupNameEntry.setStatus("current")


class _CtsEnvSecurityGroupNameSgt_Type(CtsSecurityGroupTag):
    """Custom type ctsEnvSecurityGroupNameSgt based on CtsSecurityGroupTag"""
    subtypeSpec = CtsSecurityGroupTag.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtsEnvSecurityGroupNameSgt_Type.__name__ = "CtsSecurityGroupTag"
_CtsEnvSecurityGroupNameSgt_Object = MibTableColumn
ctsEnvSecurityGroupNameSgt = _CtsEnvSecurityGroupNameSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 16, 1, 1),
    _CtsEnvSecurityGroupNameSgt_Type()
)
ctsEnvSecurityGroupNameSgt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupNameSgt.setStatus("current")
_CtsEnvSecurityGroupNameSgtGenId_Type = CtsGenerationId
_CtsEnvSecurityGroupNameSgtGenId_Object = MibTableColumn
ctsEnvSecurityGroupNameSgtGenId = _CtsEnvSecurityGroupNameSgtGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 16, 1, 2),
    _CtsEnvSecurityGroupNameSgtGenId_Type()
)
ctsEnvSecurityGroupNameSgtGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupNameSgtGenId.setStatus("current")


class _CtsEnvSecurityGroupNameSgtFlag_Type(Bits):
    """Custom type ctsEnvSecurityGroupNameSgtFlag based on Bits"""
    namedValues = NamedValues(
        *(("recognizedSgt", 0),
          ("unicastSgt", 1))
    )

_CtsEnvSecurityGroupNameSgtFlag_Type.__name__ = "Bits"
_CtsEnvSecurityGroupNameSgtFlag_Object = MibTableColumn
ctsEnvSecurityGroupNameSgtFlag = _CtsEnvSecurityGroupNameSgtFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 16, 1, 3),
    _CtsEnvSecurityGroupNameSgtFlag_Type()
)
ctsEnvSecurityGroupNameSgtFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupNameSgtFlag.setStatus("current")
_CtsEnvSecurityGroupName_Type = SnmpAdminString
_CtsEnvSecurityGroupName_Object = MibTableColumn
ctsEnvSecurityGroupName = _CtsEnvSecurityGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 4, 16, 1, 4),
    _CtsEnvSecurityGroupName_Type()
)
ctsEnvSecurityGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsEnvSecurityGroupName.setStatus("current")
_CtsNotifsControlObjects_ObjectIdentity = ObjectIdentity
ctsNotifsControlObjects = _CtsNotifsControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 5)
)
_CtsSwKeystoreFileErrNotifEnable_Type = TruthValue
_CtsSwKeystoreFileErrNotifEnable_Object = MibScalar
ctsSwKeystoreFileErrNotifEnable = _CtsSwKeystoreFileErrNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 5, 1),
    _CtsSwKeystoreFileErrNotifEnable_Type()
)
ctsSwKeystoreFileErrNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSwKeystoreFileErrNotifEnable.setStatus("current")
_CtsSwKeystoreSyncFailNotifEnable_Type = TruthValue
_CtsSwKeystoreSyncFailNotifEnable_Object = MibScalar
ctsSwKeystoreSyncFailNotifEnable = _CtsSwKeystoreSyncFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 5, 2),
    _CtsSwKeystoreSyncFailNotifEnable_Type()
)
ctsSwKeystoreSyncFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSwKeystoreSyncFailNotifEnable.setStatus("current")
_CtsAuthzCacheFileErrNotifEnable_Type = TruthValue
_CtsAuthzCacheFileErrNotifEnable_Object = MibScalar
ctsAuthzCacheFileErrNotifEnable = _CtsAuthzCacheFileErrNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 5, 3),
    _CtsAuthzCacheFileErrNotifEnable_Type()
)
ctsAuthzCacheFileErrNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsAuthzCacheFileErrNotifEnable.setStatus("current")
_CtsCacheFileAccessErrNotifEnable_Type = TruthValue
_CtsCacheFileAccessErrNotifEnable_Object = MibScalar
ctsCacheFileAccessErrNotifEnable = _CtsCacheFileAccessErrNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 5, 4),
    _CtsCacheFileAccessErrNotifEnable_Type()
)
ctsCacheFileAccessErrNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCacheFileAccessErrNotifEnable.setStatus("current")
_CtsSrcEntropyFailNotifEnable_Type = TruthValue
_CtsSrcEntropyFailNotifEnable_Object = MibScalar
ctsSrcEntropyFailNotifEnable = _CtsSrcEntropyFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 5, 5),
    _CtsSrcEntropyFailNotifEnable_Type()
)
ctsSrcEntropyFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSrcEntropyFailNotifEnable.setStatus("current")
_CtsSapRandomNumberFailNotifEnable_Type = TruthValue
_CtsSapRandomNumberFailNotifEnable_Object = MibScalar
ctsSapRandomNumberFailNotifEnable = _CtsSapRandomNumberFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 5, 6),
    _CtsSapRandomNumberFailNotifEnable_Type()
)
ctsSapRandomNumberFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSapRandomNumberFailNotifEnable.setStatus("current")
_CtsNotifsInfoObjects_ObjectIdentity = ObjectIdentity
ctsNotifsInfoObjects = _CtsNotifsInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 6)
)


class _CtsFileErrNotifReason_Type(Integer32):
    """Custom type ctsFileErrNotifReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("badHeader", 7),
          ("badMagic", 5),
          ("openFailedForRead", 3),
          ("openFailedForWrite", 1),
          ("readFailed", 4),
          ("unexpectedEof", 6),
          ("writeFailed", 2))
    )


_CtsFileErrNotifReason_Type.__name__ = "Integer32"
_CtsFileErrNotifReason_Object = MibScalar
ctsFileErrNotifReason = _CtsFileErrNotifReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 6, 1),
    _CtsFileErrNotifReason_Type()
)
ctsFileErrNotifReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsFileErrNotifReason.setStatus("current")


class _CtsSwKeystoreSyncFailNotifReason_Type(Integer32):
    """Custom type ctsSwKeystoreSyncFailNotifReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ipcConnectionFailure", 3),
          ("ipcPortCreationFailed", 1),
          ("ipcPortOpenFailed", 2),
          ("ipcSendFailure", 4),
          ("standbyIncompatible", 5),
          ("syncProcessCreationFailed", 6))
    )


_CtsSwKeystoreSyncFailNotifReason_Type.__name__ = "Integer32"
_CtsSwKeystoreSyncFailNotifReason_Object = MibScalar
ctsSwKeystoreSyncFailNotifReason = _CtsSwKeystoreSyncFailNotifReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 6, 2),
    _CtsSwKeystoreSyncFailNotifReason_Type()
)
ctsSwKeystoreSyncFailNotifReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsSwKeystoreSyncFailNotifReason.setStatus("current")
_CtsNotifMessageString_Type = SnmpAdminString
_CtsNotifMessageString_Object = MibScalar
ctsNotifMessageString = _CtsNotifMessageString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 6, 3),
    _CtsNotifMessageString_Type()
)
ctsNotifMessageString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsNotifMessageString.setStatus("current")
_CtsCriticalAuthObjects_ObjectIdentity = ObjectIdentity
ctsCriticalAuthObjects = _CtsCriticalAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 7)
)
_CtsCriticalAuthEnabled_Type = TruthValue
_CtsCriticalAuthEnabled_Object = MibScalar
ctsCriticalAuthEnabled = _CtsCriticalAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 7, 1),
    _CtsCriticalAuthEnabled_Type()
)
ctsCriticalAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCriticalAuthEnabled.setStatus("current")


class _CtsCriticalAuthFallback_Type(Integer32):
    """Custom type ctsCriticalAuthFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cache", 2),
          ("default", 1))
    )


_CtsCriticalAuthFallback_Type.__name__ = "Integer32"
_CtsCriticalAuthFallback_Object = MibScalar
ctsCriticalAuthFallback = _CtsCriticalAuthFallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 7, 2),
    _CtsCriticalAuthFallback_Type()
)
ctsCriticalAuthFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCriticalAuthFallback.setStatus("current")
_CtsCriticalAuthPeerSgt_Type = CtsSecurityGroupTag
_CtsCriticalAuthPeerSgt_Object = MibScalar
ctsCriticalAuthPeerSgt = _CtsCriticalAuthPeerSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 7, 3),
    _CtsCriticalAuthPeerSgt_Type()
)
ctsCriticalAuthPeerSgt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCriticalAuthPeerSgt.setStatus("current")
_CtsCriticalAuthPeerSgtTrust_Type = TruthValue
_CtsCriticalAuthPeerSgtTrust_Object = MibScalar
ctsCriticalAuthPeerSgtTrust = _CtsCriticalAuthPeerSgtTrust_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 7, 4),
    _CtsCriticalAuthPeerSgtTrust_Type()
)
ctsCriticalAuthPeerSgtTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCriticalAuthPeerSgtTrust.setStatus("current")


class _CtsCriticalAuthDefaultPmk_Type(OctetString):
    """Custom type ctsCriticalAuthDefaultPmk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_CtsCriticalAuthDefaultPmk_Type.__name__ = "OctetString"
_CtsCriticalAuthDefaultPmk_Object = MibScalar
ctsCriticalAuthDefaultPmk = _CtsCriticalAuthDefaultPmk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 7, 5),
    _CtsCriticalAuthDefaultPmk_Type()
)
ctsCriticalAuthDefaultPmk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsCriticalAuthDefaultPmk.setStatus("current")


class _CtsCriticalAuthViewDefaultPmk_Type(OctetString):
    """Custom type ctsCriticalAuthViewDefaultPmk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CtsCriticalAuthViewDefaultPmk_Type.__name__ = "OctetString"
_CtsCriticalAuthViewDefaultPmk_Object = MibScalar
ctsCriticalAuthViewDefaultPmk = _CtsCriticalAuthViewDefaultPmk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 1, 7, 6),
    _CtsCriticalAuthViewDefaultPmk_Type()
)
ctsCriticalAuthViewDefaultPmk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsCriticalAuthViewDefaultPmk.setStatus("current")
_CiscoTrustSecMIBConform_ObjectIdentity = ObjectIdentity
ciscoTrustSecMIBConform = _CiscoTrustSecMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2)
)
_CiscoTrustSecMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTrustSecMIBCompliances = _CiscoTrustSecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 1)
)
_CiscoTrustSecMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTrustSecMIBGroups = _CiscoTrustSecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2)
)

# Managed Objects groups

ciscoTrustSecCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 1)
)
ciscoTrustSecCacheGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsCacheEnabled"),
        ("CISCO-TRUSTSEC-MIB", "ctsCacheNvStorage"),
        ("CISCO-TRUSTSEC-MIB", "ctsCacheClear"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecCacheGroup.setStatus("current")

ciscoTrustSecSgtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 2)
)
ciscoTrustSecSgtGroup.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsSecurityGroupTagId")
)
if mibBuilder.loadTexts:
    ciscoTrustSecSgtGroup.setStatus("current")

ciscoTrustSecCredentialsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 3)
)
ciscoTrustSecCredentialsGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsDeviceId"),
        ("CISCO-TRUSTSEC-MIB", "ctsDevicePasswordType"),
        ("CISCO-TRUSTSEC-MIB", "ctsDevicePassword"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystoreType"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystorePasswordRecordType"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystorePacRecordType"),
        ("CISCO-TRUSTSEC-MIB", "ctsPacAcsDescription"),
        ("CISCO-TRUSTSEC-MIB", "ctsPacType"),
        ("CISCO-TRUSTSEC-MIB", "ctsPacExpirationTime"),
        ("CISCO-TRUSTSEC-MIB", "ctsPacTimeToRefresh"),
        ("CISCO-TRUSTSEC-MIB", "ctsPacStatus"),
        ("CISCO-TRUSTSEC-MIB", "ctsCredentialsClearAll"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecCredentialsGroup.setStatus("current")

ciscoTrustSecHwKeystoreInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 4)
)
ciscoTrustSecHwKeystoreInfoGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsKeystoreFwVersion"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystoreFwAlerts"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystoreFwResets"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystoreRxTimeouts"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystoreRxBadChecksums"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystoreRxBadFragmentLengths"),
        ("CISCO-TRUSTSEC-MIB", "ctsKeystoreCorruptions"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecHwKeystoreInfoGroup.setStatus("current")

ciscoTrustSecEnvDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 5)
)
ciscoTrustSecEnvDataGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsEnvDataLastDownloadStatus"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvSecurityGroupTagId"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvSecurityGroupTagGenId"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvDataLastUpdate"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvDataRefreshInterval"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvDataTimeLeft"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvDataTimeToRefresh"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvDataSource"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvDataAction"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecEnvDataGroup.setStatus("current")

ciscoTrustSecSgtAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 6)
)
ciscoTrustSecSgtAssignmentGroup.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsSgtAssignmentMethod")
)
if mibBuilder.loadTexts:
    ciscoTrustSecSgtAssignmentGroup.setStatus("current")

ciscoTrustSecEnvSecGroupNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 7)
)
ciscoTrustSecEnvSecGroupNameGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsEnvSecurityGroupNameSgtGenId"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvSecurityGroupNameSgtFlag"),
        ("CISCO-TRUSTSEC-MIB", "ctsEnvSecurityGroupName"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecEnvSecGroupNameGroup.setStatus("current")

ciscoTrustSecSwKeystoreNotifsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 8)
)
ciscoTrustSecSwKeystoreNotifsInfoGroup.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsSwKeystoreSyncFailNotifReason")
)
if mibBuilder.loadTexts:
    ciscoTrustSecSwKeystoreNotifsInfoGroup.setStatus("current")

ciscoTrustSecSwKeystoreNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 9)
)
ciscoTrustSecSwKeystoreNotifsControlGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsSwKeystoreFileErrNotifEnable"),
        ("CISCO-TRUSTSEC-MIB", "ctsSwKeystoreSyncFailNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecSwKeystoreNotifsControlGroup.setStatus("current")

ciscoTrustSecFileErrNotifsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 11)
)
ciscoTrustSecFileErrNotifsInfoGroup.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsFileErrNotifReason")
)
if mibBuilder.loadTexts:
    ciscoTrustSecFileErrNotifsInfoGroup.setStatus("current")

ciscoTrustSecNotifsMessageStringInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 12)
)
ciscoTrustSecNotifsMessageStringInfoGroup.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsNotifMessageString")
)
if mibBuilder.loadTexts:
    ciscoTrustSecNotifsMessageStringInfoGroup.setStatus("current")

ciscoTrustSecCacheFileNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 13)
)
ciscoTrustSecCacheFileNotifsControlGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsAuthzCacheFileErrNotifEnable"),
        ("CISCO-TRUSTSEC-MIB", "ctsCacheFileAccessErrNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecCacheFileNotifsControlGroup.setStatus("current")

ciscoTrustSecCtrDrbgNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 15)
)
ciscoTrustSecCtrDrbgNotifsControlGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsSrcEntropyFailNotifEnable"),
        ("CISCO-TRUSTSEC-MIB", "ctsSapRandomNumberFailNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecCtrDrbgNotifsControlGroup.setStatus("current")

ciscoTrustSecCrtclAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 17)
)
ciscoTrustSecCrtclAuthGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsCriticalAuthEnabled"),
        ("CISCO-TRUSTSEC-MIB", "ctsCriticalAuthFallback"),
        ("CISCO-TRUSTSEC-MIB", "ctsCriticalAuthPeerSgt"),
        ("CISCO-TRUSTSEC-MIB", "ctsCriticalAuthPeerSgtTrust"),
        ("CISCO-TRUSTSEC-MIB", "ctsCriticalAuthDefaultPmk"),
        ("CISCO-TRUSTSEC-MIB", "ctsCriticalAuthViewDefaultPmk"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecCrtclAuthGroup.setStatus("current")


# Notification objects

ctsSwKeystoreFileErrNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 0, 1)
)
ctsSwKeystoreFileErrNotif.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsFileErrNotifReason")
)
if mibBuilder.loadTexts:
    ctsSwKeystoreFileErrNotif.setStatus(
        "current"
    )

ctsSwKeystoreSyncFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 0, 2)
)
ctsSwKeystoreSyncFailNotif.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsSwKeystoreSyncFailNotifReason")
)
if mibBuilder.loadTexts:
    ctsSwKeystoreSyncFailNotif.setStatus(
        "current"
    )

ctsAuthzCacheFileErrNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 0, 3)
)
ctsAuthzCacheFileErrNotif.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsFileErrNotifReason"),
        ("CISCO-TRUSTSEC-MIB", "ctsNotifMessageString"))
)
if mibBuilder.loadTexts:
    ctsAuthzCacheFileErrNotif.setStatus(
        "current"
    )

ctsCacheFileAccessErrNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 0, 4)
)
ctsCacheFileAccessErrNotif.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsFileErrNotifReason"),
        ("CISCO-TRUSTSEC-MIB", "ctsNotifMessageString"))
)
if mibBuilder.loadTexts:
    ctsCacheFileAccessErrNotif.setStatus(
        "current"
    )

ctsSrcEntropyFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 0, 5)
)
if mibBuilder.loadTexts:
    ctsSrcEntropyFailNotif.setStatus(
        "current"
    )

ctsSapRandomNumberFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 0, 6)
)
ctsSapRandomNumberFailNotif.setObjects(
    ("CISCO-TRUSTSEC-MIB", "ctsNotifMessageString")
)
if mibBuilder.loadTexts:
    ctsSapRandomNumberFailNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoTrustSecSwKeystoreNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 10)
)
ciscoTrustSecSwKeystoreNotifsGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsSwKeystoreFileErrNotif"),
        ("CISCO-TRUSTSEC-MIB", "ctsSwKeystoreSyncFailNotif"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecSwKeystoreNotifsGroup.setStatus(
        "current"
    )

ciscoTrustSecCacheFileNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 14)
)
ciscoTrustSecCacheFileNotifsGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsAuthzCacheFileErrNotif"),
        ("CISCO-TRUSTSEC-MIB", "ctsCacheFileAccessErrNotif"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecCacheFileNotifsGroup.setStatus(
        "current"
    )

ciscoTrustSecCtrDrbgNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 2, 16)
)
ciscoTrustSecCtrDrbgNotifsGroup.setObjects(
      *(("CISCO-TRUSTSEC-MIB", "ctsSrcEntropyFailNotif"),
        ("CISCO-TRUSTSEC-MIB", "ctsSapRandomNumberFailNotif"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecCtrDrbgNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTrustSecMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBCompliance.setStatus(
        "deprecated"
    )

ciscoTrustSecMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoTrustSecMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoTrustSecMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 730, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoTrustSecMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TRUSTSEC-MIB",
    **{"ciscoTrustSecMIB": ciscoTrustSecMIB,
       "ciscoTrustSecMIBNotifs": ciscoTrustSecMIBNotifs,
       "ctsSwKeystoreFileErrNotif": ctsSwKeystoreFileErrNotif,
       "ctsSwKeystoreSyncFailNotif": ctsSwKeystoreSyncFailNotif,
       "ctsAuthzCacheFileErrNotif": ctsAuthzCacheFileErrNotif,
       "ctsCacheFileAccessErrNotif": ctsCacheFileAccessErrNotif,
       "ctsSrcEntropyFailNotif": ctsSrcEntropyFailNotif,
       "ctsSapRandomNumberFailNotif": ctsSapRandomNumberFailNotif,
       "ciscoTrustSecMIBObjects": ciscoTrustSecMIBObjects,
       "ctsCacheObjects": ctsCacheObjects,
       "ctsCacheEnabled": ctsCacheEnabled,
       "ctsCacheNvStorage": ctsCacheNvStorage,
       "ctsCacheClear": ctsCacheClear,
       "ctsSgtObjects": ctsSgtObjects,
       "ctsSecurityGroupTagId": ctsSecurityGroupTagId,
       "ctsSgtAssignmentMethod": ctsSgtAssignmentMethod,
       "ctsCredentialObjects": ctsCredentialObjects,
       "ctsDeviceId": ctsDeviceId,
       "ctsDevicePasswordType": ctsDevicePasswordType,
       "ctsDevicePassword": ctsDevicePassword,
       "ctsKeystoreType": ctsKeystoreType,
       "ctsKeystoreFwVersion": ctsKeystoreFwVersion,
       "ctsKeystoreFwAlerts": ctsKeystoreFwAlerts,
       "ctsKeystoreFwResets": ctsKeystoreFwResets,
       "ctsKeystoreRxTimeouts": ctsKeystoreRxTimeouts,
       "ctsKeystoreRxBadChecksums": ctsKeystoreRxBadChecksums,
       "ctsKeystoreRxBadFragmentLengths": ctsKeystoreRxBadFragmentLengths,
       "ctsKeystoreCorruptions": ctsKeystoreCorruptions,
       "ctsKeystorePasswordRecordTable": ctsKeystorePasswordRecordTable,
       "ctsKeystorePasswordRecordEntry": ctsKeystorePasswordRecordEntry,
       "ctsKeystorePasswordRecordName": ctsKeystorePasswordRecordName,
       "ctsKeystorePasswordRecordType": ctsKeystorePasswordRecordType,
       "ctsKeystorePacRecordTable": ctsKeystorePacRecordTable,
       "ctsKeystorePacRecordEntry": ctsKeystorePacRecordEntry,
       "ctsKeystorePacRecordName": ctsKeystorePacRecordName,
       "ctsKeystorePacRecordType": ctsKeystorePacRecordType,
       "ctsPacInfoTable": ctsPacInfoTable,
       "ctsPacInfoEntry": ctsPacInfoEntry,
       "ctsPacAcsAuthId": ctsPacAcsAuthId,
       "ctsPacAcsDescription": ctsPacAcsDescription,
       "ctsPacType": ctsPacType,
       "ctsPacExpirationTime": ctsPacExpirationTime,
       "ctsPacTimeToRefresh": ctsPacTimeToRefresh,
       "ctsPacStatus": ctsPacStatus,
       "ctsCredentialsClearAll": ctsCredentialsClearAll,
       "ctsEnvironmentDataObjects": ctsEnvironmentDataObjects,
       "ctsEnvDataLastDownloadStatus": ctsEnvDataLastDownloadStatus,
       "ctsEnvSecurityGroupTagId": ctsEnvSecurityGroupTagId,
       "ctsEnvSecurityGroupTagGenId": ctsEnvSecurityGroupTagGenId,
       "ctsEnvDataLastUpdate": ctsEnvDataLastUpdate,
       "ctsEnvDataRefreshInterval": ctsEnvDataRefreshInterval,
       "ctsEnvDataTimeLeft": ctsEnvDataTimeLeft,
       "ctsEnvDataTimeToRefresh": ctsEnvDataTimeToRefresh,
       "ctsEnvDataSource": ctsEnvDataSource,
       "ctsEnvDataAction": ctsEnvDataAction,
       "ctsEnvSecurityGroupNameTable": ctsEnvSecurityGroupNameTable,
       "ctsEnvSecurityGroupNameEntry": ctsEnvSecurityGroupNameEntry,
       "ctsEnvSecurityGroupNameSgt": ctsEnvSecurityGroupNameSgt,
       "ctsEnvSecurityGroupNameSgtGenId": ctsEnvSecurityGroupNameSgtGenId,
       "ctsEnvSecurityGroupNameSgtFlag": ctsEnvSecurityGroupNameSgtFlag,
       "ctsEnvSecurityGroupName": ctsEnvSecurityGroupName,
       "ctsNotifsControlObjects": ctsNotifsControlObjects,
       "ctsSwKeystoreFileErrNotifEnable": ctsSwKeystoreFileErrNotifEnable,
       "ctsSwKeystoreSyncFailNotifEnable": ctsSwKeystoreSyncFailNotifEnable,
       "ctsAuthzCacheFileErrNotifEnable": ctsAuthzCacheFileErrNotifEnable,
       "ctsCacheFileAccessErrNotifEnable": ctsCacheFileAccessErrNotifEnable,
       "ctsSrcEntropyFailNotifEnable": ctsSrcEntropyFailNotifEnable,
       "ctsSapRandomNumberFailNotifEnable": ctsSapRandomNumberFailNotifEnable,
       "ctsNotifsInfoObjects": ctsNotifsInfoObjects,
       "ctsFileErrNotifReason": ctsFileErrNotifReason,
       "ctsSwKeystoreSyncFailNotifReason": ctsSwKeystoreSyncFailNotifReason,
       "ctsNotifMessageString": ctsNotifMessageString,
       "ctsCriticalAuthObjects": ctsCriticalAuthObjects,
       "ctsCriticalAuthEnabled": ctsCriticalAuthEnabled,
       "ctsCriticalAuthFallback": ctsCriticalAuthFallback,
       "ctsCriticalAuthPeerSgt": ctsCriticalAuthPeerSgt,
       "ctsCriticalAuthPeerSgtTrust": ctsCriticalAuthPeerSgtTrust,
       "ctsCriticalAuthDefaultPmk": ctsCriticalAuthDefaultPmk,
       "ctsCriticalAuthViewDefaultPmk": ctsCriticalAuthViewDefaultPmk,
       "ciscoTrustSecMIBConform": ciscoTrustSecMIBConform,
       "ciscoTrustSecMIBCompliances": ciscoTrustSecMIBCompliances,
       "ciscoTrustSecMIBCompliance": ciscoTrustSecMIBCompliance,
       "ciscoTrustSecMIBCompliance2": ciscoTrustSecMIBCompliance2,
       "ciscoTrustSecMIBCompliance3": ciscoTrustSecMIBCompliance3,
       "ciscoTrustSecMIBCompliance4": ciscoTrustSecMIBCompliance4,
       "ciscoTrustSecMIBGroups": ciscoTrustSecMIBGroups,
       "ciscoTrustSecCacheGroup": ciscoTrustSecCacheGroup,
       "ciscoTrustSecSgtGroup": ciscoTrustSecSgtGroup,
       "ciscoTrustSecCredentialsGroup": ciscoTrustSecCredentialsGroup,
       "ciscoTrustSecHwKeystoreInfoGroup": ciscoTrustSecHwKeystoreInfoGroup,
       "ciscoTrustSecEnvDataGroup": ciscoTrustSecEnvDataGroup,
       "ciscoTrustSecSgtAssignmentGroup": ciscoTrustSecSgtAssignmentGroup,
       "ciscoTrustSecEnvSecGroupNameGroup": ciscoTrustSecEnvSecGroupNameGroup,
       "ciscoTrustSecSwKeystoreNotifsInfoGroup": ciscoTrustSecSwKeystoreNotifsInfoGroup,
       "ciscoTrustSecSwKeystoreNotifsControlGroup": ciscoTrustSecSwKeystoreNotifsControlGroup,
       "ciscoTrustSecSwKeystoreNotifsGroup": ciscoTrustSecSwKeystoreNotifsGroup,
       "ciscoTrustSecFileErrNotifsInfoGroup": ciscoTrustSecFileErrNotifsInfoGroup,
       "ciscoTrustSecNotifsMessageStringInfoGroup": ciscoTrustSecNotifsMessageStringInfoGroup,
       "ciscoTrustSecCacheFileNotifsControlGroup": ciscoTrustSecCacheFileNotifsControlGroup,
       "ciscoTrustSecCacheFileNotifsGroup": ciscoTrustSecCacheFileNotifsGroup,
       "ciscoTrustSecCtrDrbgNotifsControlGroup": ciscoTrustSecCtrDrbgNotifsControlGroup,
       "ciscoTrustSecCtrDrbgNotifsGroup": ciscoTrustSecCtrDrbgNotifsGroup,
       "ciscoTrustSecCrtclAuthGroup": ciscoTrustSecCrtclAuthGroup}
)
