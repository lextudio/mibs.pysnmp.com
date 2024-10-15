# SNMP MIB module (IEEE8021-DEVID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-DEVID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:18 2024
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

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021DevIDMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17)
)
ieee8021DevIDMIB.setRevisions(
        ("2018-07-15 19:04",
         "2009-06-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DevIDFingerprint(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )



class DevIDErrorStatus(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 2),
          ("none", 1))
    )



class DevIDAlgorithmIdentifier(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idecPublicKey", 2),
          ("rsaEncryption", 1))
    )



# MIB Managed Objects in the order of their OIDs

_DevIDMIBNotifications_ObjectIdentity = ObjectIdentity
devIDMIBNotifications = _DevIDMIBNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 0)
)
_DevIDMIBObjects_ObjectIdentity = ObjectIdentity
devIDMIBObjects = _DevIDMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 1)
)
_DevIDGlobalMIBObjects_ObjectIdentity = ObjectIdentity
devIDGlobalMIBObjects = _DevIDGlobalMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 1)
)
_DevIDMgmtMIBObjects_ObjectIdentity = ObjectIdentity
devIDMgmtMIBObjects = _DevIDMgmtMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2)
)
_DevIDPublicKeyCount_Type = Unsigned32
_DevIDPublicKeyCount_Object = MibScalar
devIDPublicKeyCount = _DevIDPublicKeyCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 1),
    _DevIDPublicKeyCount_Type()
)
devIDPublicKeyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDPublicKeyCount.setStatus("obsolete")
_DevIDPublicKeyTable_Object = MibTable
devIDPublicKeyTable = _DevIDPublicKeyTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    devIDPublicKeyTable.setStatus("obsolete")
_DevIDPublicKeyEntry_Object = MibTableRow
devIDPublicKeyEntry = _DevIDPublicKeyEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1)
)
devIDPublicKeyEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    devIDPublicKeyEntry.setStatus("obsolete")


class _DevIDPublicKeyIndex_Type(Unsigned32):
    """Custom type devIDPublicKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DevIDPublicKeyIndex_Type.__name__ = "Unsigned32"
_DevIDPublicKeyIndex_Object = MibTableColumn
devIDPublicKeyIndex = _DevIDPublicKeyIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 1),
    _DevIDPublicKeyIndex_Type()
)
devIDPublicKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    devIDPublicKeyIndex.setStatus("obsolete")
_DevIDPublicKeyEnabled_Type = TruthValue
_DevIDPublicKeyEnabled_Object = MibTableColumn
devIDPublicKeyEnabled = _DevIDPublicKeyEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 2),
    _DevIDPublicKeyEnabled_Type()
)
devIDPublicKeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devIDPublicKeyEnabled.setStatus("obsolete")
_DevIDPublicKeyAlgorithm_Type = DevIDAlgorithmIdentifier
_DevIDPublicKeyAlgorithm_Object = MibTableColumn
devIDPublicKeyAlgorithm = _DevIDPublicKeyAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 3),
    _DevIDPublicKeyAlgorithm_Type()
)
devIDPublicKeyAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDPublicKeyAlgorithm.setStatus("obsolete")
_DevIDPublicKeyPubkeySHA1Hash_Type = SnmpAdminString
_DevIDPublicKeyPubkeySHA1Hash_Object = MibTableColumn
devIDPublicKeyPubkeySHA1Hash = _DevIDPublicKeyPubkeySHA1Hash_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 4),
    _DevIDPublicKeyPubkeySHA1Hash_Type()
)
devIDPublicKeyPubkeySHA1Hash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDPublicKeyPubkeySHA1Hash.setStatus("obsolete")


class _DevIDPublicKeyErrStatus_Type(DevIDErrorStatus):
    """Custom type devIDPublicKeyErrStatus based on DevIDErrorStatus"""


_DevIDPublicKeyErrStatus_Object = MibTableColumn
devIDPublicKeyErrStatus = _DevIDPublicKeyErrStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 5),
    _DevIDPublicKeyErrStatus_Type()
)
devIDPublicKeyErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDPublicKeyErrStatus.setStatus("obsolete")
_DevIDCredentialCount_Type = Unsigned32
_DevIDCredentialCount_Object = MibScalar
devIDCredentialCount = _DevIDCredentialCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 3),
    _DevIDCredentialCount_Type()
)
devIDCredentialCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialCount.setStatus("obsolete")
_DevIDCredentialTable_Object = MibTable
devIDCredentialTable = _DevIDCredentialTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4)
)
if mibBuilder.loadTexts:
    devIDCredentialTable.setStatus("obsolete")
_DevIDCredentialEntry_Object = MibTableRow
devIDCredentialEntry = _DevIDCredentialEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1)
)
devIDCredentialEntry.setIndexNames(
    (0, "IEEE8021-DEVID-MIB", "devIDCredentialIndex"),
)
if mibBuilder.loadTexts:
    devIDCredentialEntry.setStatus("obsolete")


class _DevIDCredentialIndex_Type(Unsigned32):
    """Custom type devIDCredentialIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DevIDCredentialIndex_Type.__name__ = "Unsigned32"
_DevIDCredentialIndex_Object = MibTableColumn
devIDCredentialIndex = _DevIDCredentialIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 1),
    _DevIDCredentialIndex_Type()
)
devIDCredentialIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    devIDCredentialIndex.setStatus("obsolete")
_DevIDCredentialEnabled_Type = TruthValue
_DevIDCredentialEnabled_Object = MibTableColumn
devIDCredentialEnabled = _DevIDCredentialEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 2),
    _DevIDCredentialEnabled_Type()
)
devIDCredentialEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devIDCredentialEnabled.setStatus("obsolete")
_DevIDCredentialSHA1Hash_Type = SnmpAdminString
_DevIDCredentialSHA1Hash_Object = MibTableColumn
devIDCredentialSHA1Hash = _DevIDCredentialSHA1Hash_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 3),
    _DevIDCredentialSHA1Hash_Type()
)
devIDCredentialSHA1Hash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialSHA1Hash.setStatus("obsolete")


class _DevIDCredentialSerialNumber_Type(SnmpAdminString):
    """Custom type devIDCredentialSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DevIDCredentialSerialNumber_Type.__name__ = "SnmpAdminString"
_DevIDCredentialSerialNumber_Object = MibTableColumn
devIDCredentialSerialNumber = _DevIDCredentialSerialNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 4),
    _DevIDCredentialSerialNumber_Type()
)
devIDCredentialSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialSerialNumber.setStatus("obsolete")
_DevIDCredentialIssuer_Type = SnmpAdminString
_DevIDCredentialIssuer_Object = MibTableColumn
devIDCredentialIssuer = _DevIDCredentialIssuer_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 5),
    _DevIDCredentialIssuer_Type()
)
devIDCredentialIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialIssuer.setStatus("obsolete")
_DevIDCredentialSubject_Type = SnmpAdminString
_DevIDCredentialSubject_Object = MibTableColumn
devIDCredentialSubject = _DevIDCredentialSubject_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 6),
    _DevIDCredentialSubject_Type()
)
devIDCredentialSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialSubject.setStatus("obsolete")
_DevIDCredentialSubjectAltName_Type = SnmpAdminString
_DevIDCredentialSubjectAltName_Object = MibTableColumn
devIDCredentialSubjectAltName = _DevIDCredentialSubjectAltName_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 7),
    _DevIDCredentialSubjectAltName_Type()
)
devIDCredentialSubjectAltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialSubjectAltName.setStatus("obsolete")
_DevIDCredentialEntityIndex_Type = PhysicalIndex
_DevIDCredentialEntityIndex_Object = MibTableColumn
devIDCredentialEntityIndex = _DevIDCredentialEntityIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 8),
    _DevIDCredentialEntityIndex_Type()
)
devIDCredentialEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialEntityIndex.setStatus("obsolete")
_DevIDCredentialPubkeyIndex_Type = Unsigned32
_DevIDCredentialPubkeyIndex_Object = MibTableColumn
devIDCredentialPubkeyIndex = _DevIDCredentialPubkeyIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 9),
    _DevIDCredentialPubkeyIndex_Type()
)
devIDCredentialPubkeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialPubkeyIndex.setStatus("obsolete")


class _DevIDCredentialErrStatus_Type(DevIDErrorStatus):
    """Custom type devIDCredentialErrStatus based on DevIDErrorStatus"""


_DevIDCredentialErrStatus_Object = MibTableColumn
devIDCredentialErrStatus = _DevIDCredentialErrStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 10),
    _DevIDCredentialErrStatus_Type()
)
devIDCredentialErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCredentialErrStatus.setStatus("obsolete")
_DevIDStatisticsTable_Object = MibTable
devIDStatisticsTable = _DevIDStatisticsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5)
)
if mibBuilder.loadTexts:
    devIDStatisticsTable.setStatus("current")
_DevIDStatisticsEntry_Object = MibTableRow
devIDStatisticsEntry = _DevIDStatisticsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1)
)
devIDStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    devIDStatisticsEntry.setStatus("current")
_DevIDStatisticKeyGenerationCount_Type = Counter32
_DevIDStatisticKeyGenerationCount_Object = MibTableColumn
devIDStatisticKeyGenerationCount = _DevIDStatisticKeyGenerationCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 1),
    _DevIDStatisticKeyGenerationCount_Type()
)
devIDStatisticKeyGenerationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticKeyGenerationCount.setStatus("current")
_DevIDStatisticKeyInsertionCount_Type = Counter32
_DevIDStatisticKeyInsertionCount_Object = MibTableColumn
devIDStatisticKeyInsertionCount = _DevIDStatisticKeyInsertionCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 2),
    _DevIDStatisticKeyInsertionCount_Type()
)
devIDStatisticKeyInsertionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticKeyInsertionCount.setStatus("current")
_DevIDStatisticKeyDeletionCount_Type = Counter32
_DevIDStatisticKeyDeletionCount_Object = MibTableColumn
devIDStatisticKeyDeletionCount = _DevIDStatisticKeyDeletionCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 3),
    _DevIDStatisticKeyDeletionCount_Type()
)
devIDStatisticKeyDeletionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticKeyDeletionCount.setStatus("current")
_DevIDStatisticCSRGenerationCount_Type = Counter32
_DevIDStatisticCSRGenerationCount_Object = MibTableColumn
devIDStatisticCSRGenerationCount = _DevIDStatisticCSRGenerationCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 4),
    _DevIDStatisticCSRGenerationCount_Type()
)
devIDStatisticCSRGenerationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticCSRGenerationCount.setStatus("deprecated")
_DevIDStatisticCredentialInsertionCount_Type = Counter32
_DevIDStatisticCredentialInsertionCount_Object = MibTableColumn
devIDStatisticCredentialInsertionCount = _DevIDStatisticCredentialInsertionCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 5),
    _DevIDStatisticCredentialInsertionCount_Type()
)
devIDStatisticCredentialInsertionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticCredentialInsertionCount.setStatus("obsolete")
_DevIDStatisticCredentialDeletionCount_Type = Counter32
_DevIDStatisticCredentialDeletionCount_Object = MibTableColumn
devIDStatisticCredentialDeletionCount = _DevIDStatisticCredentialDeletionCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 6),
    _DevIDStatisticCredentialDeletionCount_Type()
)
devIDStatisticCredentialDeletionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticCredentialDeletionCount.setStatus("obsolete")
_DevIDStatisticCertInsertionCount_Type = Counter32
_DevIDStatisticCertInsertionCount_Object = MibTableColumn
devIDStatisticCertInsertionCount = _DevIDStatisticCertInsertionCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 7),
    _DevIDStatisticCertInsertionCount_Type()
)
devIDStatisticCertInsertionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticCertInsertionCount.setStatus("current")
_DevIDStatisticCertDeletionCount_Type = Counter32
_DevIDStatisticCertDeletionCount_Object = MibTableColumn
devIDStatisticCertDeletionCount = _DevIDStatisticCertDeletionCount_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 8),
    _DevIDStatisticCertDeletionCount_Type()
)
devIDStatisticCertDeletionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDStatisticCertDeletionCount.setStatus("current")
_DevIDModuleTable_Object = MibTable
devIDModuleTable = _DevIDModuleTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6)
)
if mibBuilder.loadTexts:
    devIDModuleTable.setStatus("current")
_DevIDModuleEntry_Object = MibTableRow
devIDModuleEntry = _DevIDModuleEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1)
)
devIDModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    devIDModuleEntry.setStatus("current")
_DevIDModuleSupportsLDevIDs_Type = TruthValue
_DevIDModuleSupportsLDevIDs_Object = MibTableColumn
devIDModuleSupportsLDevIDs = _DevIDModuleSupportsLDevIDs_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1, 1),
    _DevIDModuleSupportsLDevIDs_Type()
)
devIDModuleSupportsLDevIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDModuleSupportsLDevIDs.setStatus("current")
_DevIDModuleGeneratesLDevIDKeys_Type = TruthValue
_DevIDModuleGeneratesLDevIDKeys_Object = MibTableColumn
devIDModuleGeneratesLDevIDKeys = _DevIDModuleGeneratesLDevIDKeys_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1, 2),
    _DevIDModuleGeneratesLDevIDKeys_Type()
)
devIDModuleGeneratesLDevIDKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDModuleGeneratesLDevIDKeys.setStatus("current")
_DevIDModuleInsertsLDevIDKeys_Type = TruthValue
_DevIDModuleInsertsLDevIDKeys_Object = MibTableColumn
devIDModuleInsertsLDevIDKeys = _DevIDModuleInsertsLDevIDKeys_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1, 3),
    _DevIDModuleInsertsLDevIDKeys_Type()
)
devIDModuleInsertsLDevIDKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDModuleInsertsLDevIDKeys.setStatus("current")
_DevIDCertTable_Object = MibTable
devIDCertTable = _DevIDCertTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7)
)
if mibBuilder.loadTexts:
    devIDCertTable.setStatus("current")
_DevIDCertEntry_Object = MibTableRow
devIDCertEntry = _DevIDCertEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1)
)
devIDCertEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "IEEE8021-DEVID-MIB", "devIDCertFingerprint"),
)
if mibBuilder.loadTexts:
    devIDCertEntry.setStatus("current")
_DevIDCertFingerprint_Type = DevIDFingerprint
_DevIDCertFingerprint_Object = MibTableColumn
devIDCertFingerprint = _DevIDCertFingerprint_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 1),
    _DevIDCertFingerprint_Type()
)
devIDCertFingerprint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    devIDCertFingerprint.setStatus("current")
_DevIDCertPublicKeyInfoFprint_Type = DevIDFingerprint
_DevIDCertPublicKeyInfoFprint_Object = MibTableColumn
devIDCertPublicKeyInfoFprint = _DevIDCertPublicKeyInfoFprint_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 2),
    _DevIDCertPublicKeyInfoFprint_Type()
)
devIDCertPublicKeyInfoFprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCertPublicKeyInfoFprint.setStatus("current")
_DevIDCertIDevID_Type = TruthValue
_DevIDCertIDevID_Object = MibTableColumn
devIDCertIDevID = _DevIDCertIDevID_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 3),
    _DevIDCertIDevID_Type()
)
devIDCertIDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCertIDevID.setStatus("current")
_DevIDCertKeyEnabled_Type = TruthValue
_DevIDCertKeyEnabled_Object = MibTableColumn
devIDCertKeyEnabled = _DevIDCertKeyEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 4),
    _DevIDCertKeyEnabled_Type()
)
devIDCertKeyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCertKeyEnabled.setStatus("current")
_DevIDCertEnabled_Type = TruthValue
_DevIDCertEnabled_Object = MibTableColumn
devIDCertEnabled = _DevIDCertEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 5),
    _DevIDCertEnabled_Type()
)
devIDCertEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCertEnabled.setStatus("current")
_DevIDCert_Type = OctetString
_DevIDCert_Object = MibTableColumn
devIDCert = _DevIDCert_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 6),
    _DevIDCert_Type()
)
devIDCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDCert.setStatus("current")
_DevIDChainTable_Object = MibTable
devIDChainTable = _DevIDChainTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8)
)
if mibBuilder.loadTexts:
    devIDChainTable.setStatus("current")
_DevIDChainEntry_Object = MibTableRow
devIDChainEntry = _DevIDChainEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1)
)
devIDChainEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "IEEE8021-DEVID-MIB", "devIDCertFingerprint"),
    (0, "IEEE8021-DEVID-MIB", "devIDChainCertIndex"),
)
if mibBuilder.loadTexts:
    devIDChainEntry.setStatus("current")
_DevIDChainCertIndex_Type = Unsigned32
_DevIDChainCertIndex_Object = MibTableColumn
devIDChainCertIndex = _DevIDChainCertIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1, 1),
    _DevIDChainCertIndex_Type()
)
devIDChainCertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    devIDChainCertIndex.setStatus("current")
_DevIDChainCertFingerprint_Type = DevIDFingerprint
_DevIDChainCertFingerprint_Object = MibTableColumn
devIDChainCertFingerprint = _DevIDChainCertFingerprint_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1, 2),
    _DevIDChainCertFingerprint_Type()
)
devIDChainCertFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDChainCertFingerprint.setStatus("current")
_DevIDChainCert_Type = OctetString
_DevIDChainCert_Object = MibTableColumn
devIDChainCert = _DevIDChainCert_Object(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1, 3),
    _DevIDChainCert_Type()
)
devIDChainCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devIDChainCert.setStatus("current")
_DevIDStatsMIBObjects_ObjectIdentity = ObjectIdentity
devIDStatsMIBObjects = _DevIDStatsMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 1, 3)
)
_DevIDMIBConformance_ObjectIdentity = ObjectIdentity
devIDMIBConformance = _DevIDMIBConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 2)
)
_DevIDMIBCompliances_ObjectIdentity = ObjectIdentity
devIDMIBCompliances = _DevIDMIBCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 1)
)
_DevIDMIBGroups_ObjectIdentity = ObjectIdentity
devIDMIBGroups = _DevIDMIBGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 2)
)

# Managed Objects groups

devIDMIBObjectGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 1)
)
devIDMIBObjectGroup.setObjects(
      *(("IEEE8021-DEVID-MIB", "devIDPublicKeyCount"),
        ("IEEE8021-DEVID-MIB", "devIDPublicKeyEnabled"),
        ("IEEE8021-DEVID-MIB", "devIDPublicKeyAlgorithm"),
        ("IEEE8021-DEVID-MIB", "devIDPublicKeyPubkeySHA1Hash"),
        ("IEEE8021-DEVID-MIB", "devIDPublicKeyErrStatus"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialCount"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialEnabled"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialSHA1Hash"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialSerialNumber"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialIssuer"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialSubject"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialSubjectAltName"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialEntityIndex"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialPubkeyIndex"),
        ("IEEE8021-DEVID-MIB", "devIDCredentialErrStatus"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticKeyGenerationCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticKeyInsertionCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticKeyDeletionCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticCSRGenerationCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticCredentialInsertionCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticCredentialDeletionCount"))
)
if mibBuilder.loadTexts:
    devIDMIBObjectGroup.setStatus("obsolete")

devIDMIBModuleGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 2)
)
devIDMIBModuleGroup.setObjects(
      *(("IEEE8021-DEVID-MIB", "devIDModuleSupportsLDevIDs"),
        ("IEEE8021-DEVID-MIB", "devIDModuleGeneratesLDevIDKeys"),
        ("IEEE8021-DEVID-MIB", "devIDModuleInsertsLDevIDKeys"))
)
if mibBuilder.loadTexts:
    devIDMIBModuleGroup.setStatus("current")

devIDMIBCertificateGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 3)
)
devIDMIBCertificateGroup.setObjects(
      *(("IEEE8021-DEVID-MIB", "devIDCertPublicKeyInfoFprint"),
        ("IEEE8021-DEVID-MIB", "devIDCertIDevID"),
        ("IEEE8021-DEVID-MIB", "devIDCertKeyEnabled"),
        ("IEEE8021-DEVID-MIB", "devIDCertEnabled"),
        ("IEEE8021-DEVID-MIB", "devIDCert"),
        ("IEEE8021-DEVID-MIB", "devIDChainCertFingerprint"),
        ("IEEE8021-DEVID-MIB", "devIDChainCert"))
)
if mibBuilder.loadTexts:
    devIDMIBCertificateGroup.setStatus("current")

devIDMIBAuditGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 4)
)
devIDMIBAuditGroup.setObjects(
      *(("IEEE8021-DEVID-MIB", "devIDStatisticKeyGenerationCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticKeyInsertionCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticKeyDeletionCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticCertInsertionCount"),
        ("IEEE8021-DEVID-MIB", "devIDStatisticCertDeletionCount"))
)
if mibBuilder.loadTexts:
    devIDMIBAuditGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

devIDMIBModuleCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    devIDMIBModuleCompliance.setStatus(
        "obsolete"
    )

devIDMIBModuleCompliance2 = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 17, 2, 1, 2)
)
if mibBuilder.loadTexts:
    devIDMIBModuleCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-DEVID-MIB",
    **{"DevIDFingerprint": DevIDFingerprint,
       "DevIDErrorStatus": DevIDErrorStatus,
       "DevIDAlgorithmIdentifier": DevIDAlgorithmIdentifier,
       "ieee8021DevIDMIB": ieee8021DevIDMIB,
       "devIDMIBNotifications": devIDMIBNotifications,
       "devIDMIBObjects": devIDMIBObjects,
       "devIDGlobalMIBObjects": devIDGlobalMIBObjects,
       "devIDMgmtMIBObjects": devIDMgmtMIBObjects,
       "devIDPublicKeyCount": devIDPublicKeyCount,
       "devIDPublicKeyTable": devIDPublicKeyTable,
       "devIDPublicKeyEntry": devIDPublicKeyEntry,
       "devIDPublicKeyIndex": devIDPublicKeyIndex,
       "devIDPublicKeyEnabled": devIDPublicKeyEnabled,
       "devIDPublicKeyAlgorithm": devIDPublicKeyAlgorithm,
       "devIDPublicKeyPubkeySHA1Hash": devIDPublicKeyPubkeySHA1Hash,
       "devIDPublicKeyErrStatus": devIDPublicKeyErrStatus,
       "devIDCredentialCount": devIDCredentialCount,
       "devIDCredentialTable": devIDCredentialTable,
       "devIDCredentialEntry": devIDCredentialEntry,
       "devIDCredentialIndex": devIDCredentialIndex,
       "devIDCredentialEnabled": devIDCredentialEnabled,
       "devIDCredentialSHA1Hash": devIDCredentialSHA1Hash,
       "devIDCredentialSerialNumber": devIDCredentialSerialNumber,
       "devIDCredentialIssuer": devIDCredentialIssuer,
       "devIDCredentialSubject": devIDCredentialSubject,
       "devIDCredentialSubjectAltName": devIDCredentialSubjectAltName,
       "devIDCredentialEntityIndex": devIDCredentialEntityIndex,
       "devIDCredentialPubkeyIndex": devIDCredentialPubkeyIndex,
       "devIDCredentialErrStatus": devIDCredentialErrStatus,
       "devIDStatisticsTable": devIDStatisticsTable,
       "devIDStatisticsEntry": devIDStatisticsEntry,
       "devIDStatisticKeyGenerationCount": devIDStatisticKeyGenerationCount,
       "devIDStatisticKeyInsertionCount": devIDStatisticKeyInsertionCount,
       "devIDStatisticKeyDeletionCount": devIDStatisticKeyDeletionCount,
       "devIDStatisticCSRGenerationCount": devIDStatisticCSRGenerationCount,
       "devIDStatisticCredentialInsertionCount": devIDStatisticCredentialInsertionCount,
       "devIDStatisticCredentialDeletionCount": devIDStatisticCredentialDeletionCount,
       "devIDStatisticCertInsertionCount": devIDStatisticCertInsertionCount,
       "devIDStatisticCertDeletionCount": devIDStatisticCertDeletionCount,
       "devIDModuleTable": devIDModuleTable,
       "devIDModuleEntry": devIDModuleEntry,
       "devIDModuleSupportsLDevIDs": devIDModuleSupportsLDevIDs,
       "devIDModuleGeneratesLDevIDKeys": devIDModuleGeneratesLDevIDKeys,
       "devIDModuleInsertsLDevIDKeys": devIDModuleInsertsLDevIDKeys,
       "devIDCertTable": devIDCertTable,
       "devIDCertEntry": devIDCertEntry,
       "devIDCertFingerprint": devIDCertFingerprint,
       "devIDCertPublicKeyInfoFprint": devIDCertPublicKeyInfoFprint,
       "devIDCertIDevID": devIDCertIDevID,
       "devIDCertKeyEnabled": devIDCertKeyEnabled,
       "devIDCertEnabled": devIDCertEnabled,
       "devIDCert": devIDCert,
       "devIDChainTable": devIDChainTable,
       "devIDChainEntry": devIDChainEntry,
       "devIDChainCertIndex": devIDChainCertIndex,
       "devIDChainCertFingerprint": devIDChainCertFingerprint,
       "devIDChainCert": devIDChainCert,
       "devIDStatsMIBObjects": devIDStatsMIBObjects,
       "devIDMIBConformance": devIDMIBConformance,
       "devIDMIBCompliances": devIDMIBCompliances,
       "devIDMIBModuleCompliance": devIDMIBModuleCompliance,
       "devIDMIBModuleCompliance2": devIDMIBModuleCompliance2,
       "devIDMIBGroups": devIDMIBGroups,
       "devIDMIBObjectGroup": devIDMIBObjectGroup,
       "devIDMIBModuleGroup": devIDMIBModuleGroup,
       "devIDMIBCertificateGroup": devIDMIBCertificateGroup,
       "devIDMIBAuditGroup": devIDMIBAuditGroup}
)
