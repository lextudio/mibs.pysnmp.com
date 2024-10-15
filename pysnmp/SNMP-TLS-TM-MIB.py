# SNMP MIB module (SNMP-TLS-TM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-TLS-TM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:05 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(snmpTargetAddrName,
 snmpTargetParamsName) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrName",
    "snmpTargetParamsName")

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
 iso,
 mib_2,
 snmpDomains) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpDomains")

(AutonomousType,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

snmpTlstmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 198)
)
snmpTlstmMIB.setRevisions(
        ("2011-07-19 00:00",
         "2010-05-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpTLSAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class SnmpTLSFingerprint(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SnmpTlstmNotifications_ObjectIdentity = ObjectIdentity
snmpTlstmNotifications = _SnmpTlstmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 0)
)
_SnmpTlstmIdentities_ObjectIdentity = ObjectIdentity
snmpTlstmIdentities = _SnmpTlstmIdentities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1)
)
_SnmpTlstmCertToTSNMIdentities_ObjectIdentity = ObjectIdentity
snmpTlstmCertToTSNMIdentities = _SnmpTlstmCertToTSNMIdentities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1, 1)
)
_SnmpTlstmCertSpecified_ObjectIdentity = ObjectIdentity
snmpTlstmCertSpecified = _SnmpTlstmCertSpecified_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snmpTlstmCertSpecified.setStatus("current")
_SnmpTlstmCertSANRFC822Name_ObjectIdentity = ObjectIdentity
snmpTlstmCertSANRFC822Name = _SnmpTlstmCertSANRFC822Name_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1, 1, 2)
)
if mibBuilder.loadTexts:
    snmpTlstmCertSANRFC822Name.setStatus("current")
_SnmpTlstmCertSANDNSName_ObjectIdentity = ObjectIdentity
snmpTlstmCertSANDNSName = _SnmpTlstmCertSANDNSName_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1, 1, 3)
)
if mibBuilder.loadTexts:
    snmpTlstmCertSANDNSName.setStatus("current")
_SnmpTlstmCertSANIpAddress_ObjectIdentity = ObjectIdentity
snmpTlstmCertSANIpAddress = _SnmpTlstmCertSANIpAddress_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1, 1, 4)
)
if mibBuilder.loadTexts:
    snmpTlstmCertSANIpAddress.setStatus("current")
_SnmpTlstmCertSANAny_ObjectIdentity = ObjectIdentity
snmpTlstmCertSANAny = _SnmpTlstmCertSANAny_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1, 1, 5)
)
if mibBuilder.loadTexts:
    snmpTlstmCertSANAny.setStatus("current")
_SnmpTlstmCertCommonName_ObjectIdentity = ObjectIdentity
snmpTlstmCertCommonName = _SnmpTlstmCertCommonName_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 1, 1, 6)
)
if mibBuilder.loadTexts:
    snmpTlstmCertCommonName.setStatus("current")
_SnmpTlstmObjects_ObjectIdentity = ObjectIdentity
snmpTlstmObjects = _SnmpTlstmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 2)
)
_SnmpTlstmSession_ObjectIdentity = ObjectIdentity
snmpTlstmSession = _SnmpTlstmSession_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 2, 1)
)
_SnmpTlstmSessionOpens_Type = Counter32
_SnmpTlstmSessionOpens_Object = MibScalar
snmpTlstmSessionOpens = _SnmpTlstmSessionOpens_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 1),
    _SnmpTlstmSessionOpens_Type()
)
snmpTlstmSessionOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionOpens.setStatus("current")
_SnmpTlstmSessionClientCloses_Type = Counter32
_SnmpTlstmSessionClientCloses_Object = MibScalar
snmpTlstmSessionClientCloses = _SnmpTlstmSessionClientCloses_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 2),
    _SnmpTlstmSessionClientCloses_Type()
)
snmpTlstmSessionClientCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionClientCloses.setStatus("current")
_SnmpTlstmSessionOpenErrors_Type = Counter32
_SnmpTlstmSessionOpenErrors_Object = MibScalar
snmpTlstmSessionOpenErrors = _SnmpTlstmSessionOpenErrors_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 3),
    _SnmpTlstmSessionOpenErrors_Type()
)
snmpTlstmSessionOpenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionOpenErrors.setStatus("current")
_SnmpTlstmSessionAccepts_Type = Counter32
_SnmpTlstmSessionAccepts_Object = MibScalar
snmpTlstmSessionAccepts = _SnmpTlstmSessionAccepts_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 4),
    _SnmpTlstmSessionAccepts_Type()
)
snmpTlstmSessionAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionAccepts.setStatus("current")
_SnmpTlstmSessionServerCloses_Type = Counter32
_SnmpTlstmSessionServerCloses_Object = MibScalar
snmpTlstmSessionServerCloses = _SnmpTlstmSessionServerCloses_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 5),
    _SnmpTlstmSessionServerCloses_Type()
)
snmpTlstmSessionServerCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionServerCloses.setStatus("current")
_SnmpTlstmSessionNoSessions_Type = Counter32
_SnmpTlstmSessionNoSessions_Object = MibScalar
snmpTlstmSessionNoSessions = _SnmpTlstmSessionNoSessions_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 6),
    _SnmpTlstmSessionNoSessions_Type()
)
snmpTlstmSessionNoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionNoSessions.setStatus("current")
_SnmpTlstmSessionInvalidClientCertificates_Type = Counter32
_SnmpTlstmSessionInvalidClientCertificates_Object = MibScalar
snmpTlstmSessionInvalidClientCertificates = _SnmpTlstmSessionInvalidClientCertificates_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 7),
    _SnmpTlstmSessionInvalidClientCertificates_Type()
)
snmpTlstmSessionInvalidClientCertificates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionInvalidClientCertificates.setStatus("current")
_SnmpTlstmSessionUnknownServerCertificate_Type = Counter32
_SnmpTlstmSessionUnknownServerCertificate_Object = MibScalar
snmpTlstmSessionUnknownServerCertificate = _SnmpTlstmSessionUnknownServerCertificate_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 8),
    _SnmpTlstmSessionUnknownServerCertificate_Type()
)
snmpTlstmSessionUnknownServerCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionUnknownServerCertificate.setStatus("current")
_SnmpTlstmSessionInvalidServerCertificates_Type = Counter32
_SnmpTlstmSessionInvalidServerCertificates_Object = MibScalar
snmpTlstmSessionInvalidServerCertificates = _SnmpTlstmSessionInvalidServerCertificates_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 9),
    _SnmpTlstmSessionInvalidServerCertificates_Type()
)
snmpTlstmSessionInvalidServerCertificates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionInvalidServerCertificates.setStatus("current")
_SnmpTlstmSessionInvalidCaches_Type = Counter32
_SnmpTlstmSessionInvalidCaches_Object = MibScalar
snmpTlstmSessionInvalidCaches = _SnmpTlstmSessionInvalidCaches_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 1, 10),
    _SnmpTlstmSessionInvalidCaches_Type()
)
snmpTlstmSessionInvalidCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmSessionInvalidCaches.setStatus("current")
_SnmpTlstmConfig_ObjectIdentity = ObjectIdentity
snmpTlstmConfig = _SnmpTlstmConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 2, 2)
)
_SnmpTlstmCertificateMapping_ObjectIdentity = ObjectIdentity
snmpTlstmCertificateMapping = _SnmpTlstmCertificateMapping_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1)
)
_SnmpTlstmCertToTSNCount_Type = Gauge32
_SnmpTlstmCertToTSNCount_Object = MibScalar
snmpTlstmCertToTSNCount = _SnmpTlstmCertToTSNCount_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 1),
    _SnmpTlstmCertToTSNCount_Type()
)
snmpTlstmCertToTSNCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNCount.setStatus("current")
_SnmpTlstmCertToTSNTableLastChanged_Type = TimeStamp
_SnmpTlstmCertToTSNTableLastChanged_Object = MibScalar
snmpTlstmCertToTSNTableLastChanged = _SnmpTlstmCertToTSNTableLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 2),
    _SnmpTlstmCertToTSNTableLastChanged_Type()
)
snmpTlstmCertToTSNTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNTableLastChanged.setStatus("current")
_SnmpTlstmCertToTSNTable_Object = MibTable
snmpTlstmCertToTSNTable = _SnmpTlstmCertToTSNTable_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNTable.setStatus("current")
_SnmpTlstmCertToTSNEntry_Object = MibTableRow
snmpTlstmCertToTSNEntry = _SnmpTlstmCertToTSNEntry_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3, 1)
)
snmpTlstmCertToTSNEntry.setIndexNames(
    (0, "SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNID"),
)
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNEntry.setStatus("current")


class _SnmpTlstmCertToTSNID_Type(Unsigned32):
    """Custom type snmpTlstmCertToTSNID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SnmpTlstmCertToTSNID_Type.__name__ = "Unsigned32"
_SnmpTlstmCertToTSNID_Object = MibTableColumn
snmpTlstmCertToTSNID = _SnmpTlstmCertToTSNID_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3, 1, 1),
    _SnmpTlstmCertToTSNID_Type()
)
snmpTlstmCertToTSNID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNID.setStatus("current")


class _SnmpTlstmCertToTSNFingerprint_Type(SnmpTLSFingerprint):
    """Custom type snmpTlstmCertToTSNFingerprint based on SnmpTLSFingerprint"""
    subtypeSpec = SnmpTLSFingerprint.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SnmpTlstmCertToTSNFingerprint_Type.__name__ = "SnmpTLSFingerprint"
_SnmpTlstmCertToTSNFingerprint_Object = MibTableColumn
snmpTlstmCertToTSNFingerprint = _SnmpTlstmCertToTSNFingerprint_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3, 1, 2),
    _SnmpTlstmCertToTSNFingerprint_Type()
)
snmpTlstmCertToTSNFingerprint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNFingerprint.setStatus("current")


class _SnmpTlstmCertToTSNMapType_Type(AutonomousType):
    """Custom type snmpTlstmCertToTSNMapType based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 2, 1, 198, 1, 1, 1)


_SnmpTlstmCertToTSNMapType_Object = MibTableColumn
snmpTlstmCertToTSNMapType = _SnmpTlstmCertToTSNMapType_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3, 1, 3),
    _SnmpTlstmCertToTSNMapType_Type()
)
snmpTlstmCertToTSNMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNMapType.setStatus("current")


class _SnmpTlstmCertToTSNData_Type(OctetString):
    """Custom type snmpTlstmCertToTSNData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SnmpTlstmCertToTSNData_Type.__name__ = "OctetString"
_SnmpTlstmCertToTSNData_Object = MibTableColumn
snmpTlstmCertToTSNData = _SnmpTlstmCertToTSNData_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3, 1, 4),
    _SnmpTlstmCertToTSNData_Type()
)
snmpTlstmCertToTSNData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNData.setStatus("current")


class _SnmpTlstmCertToTSNStorageType_Type(StorageType):
    """Custom type snmpTlstmCertToTSNStorageType based on StorageType"""


_SnmpTlstmCertToTSNStorageType_Object = MibTableColumn
snmpTlstmCertToTSNStorageType = _SnmpTlstmCertToTSNStorageType_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3, 1, 5),
    _SnmpTlstmCertToTSNStorageType_Type()
)
snmpTlstmCertToTSNStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNStorageType.setStatus("current")
_SnmpTlstmCertToTSNRowStatus_Type = RowStatus
_SnmpTlstmCertToTSNRowStatus_Object = MibTableColumn
snmpTlstmCertToTSNRowStatus = _SnmpTlstmCertToTSNRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 3, 1, 6),
    _SnmpTlstmCertToTSNRowStatus_Type()
)
snmpTlstmCertToTSNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmCertToTSNRowStatus.setStatus("current")
_SnmpTlstmParamsCount_Type = Gauge32
_SnmpTlstmParamsCount_Object = MibScalar
snmpTlstmParamsCount = _SnmpTlstmParamsCount_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 4),
    _SnmpTlstmParamsCount_Type()
)
snmpTlstmParamsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmParamsCount.setStatus("current")
_SnmpTlstmParamsTableLastChanged_Type = TimeStamp
_SnmpTlstmParamsTableLastChanged_Object = MibScalar
snmpTlstmParamsTableLastChanged = _SnmpTlstmParamsTableLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 5),
    _SnmpTlstmParamsTableLastChanged_Type()
)
snmpTlstmParamsTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmParamsTableLastChanged.setStatus("current")
_SnmpTlstmParamsTable_Object = MibTable
snmpTlstmParamsTable = _SnmpTlstmParamsTable_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    snmpTlstmParamsTable.setStatus("current")
_SnmpTlstmParamsEntry_Object = MibTableRow
snmpTlstmParamsEntry = _SnmpTlstmParamsEntry_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 6, 1)
)
snmpTlstmParamsEntry.setIndexNames(
    (1, "SNMP-TARGET-MIB", "snmpTargetParamsName"),
)
if mibBuilder.loadTexts:
    snmpTlstmParamsEntry.setStatus("current")
_SnmpTlstmParamsClientFingerprint_Type = SnmpTLSFingerprint
_SnmpTlstmParamsClientFingerprint_Object = MibTableColumn
snmpTlstmParamsClientFingerprint = _SnmpTlstmParamsClientFingerprint_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 6, 1, 1),
    _SnmpTlstmParamsClientFingerprint_Type()
)
snmpTlstmParamsClientFingerprint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmParamsClientFingerprint.setStatus("current")


class _SnmpTlstmParamsStorageType_Type(StorageType):
    """Custom type snmpTlstmParamsStorageType based on StorageType"""


_SnmpTlstmParamsStorageType_Object = MibTableColumn
snmpTlstmParamsStorageType = _SnmpTlstmParamsStorageType_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 6, 1, 2),
    _SnmpTlstmParamsStorageType_Type()
)
snmpTlstmParamsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmParamsStorageType.setStatus("current")
_SnmpTlstmParamsRowStatus_Type = RowStatus
_SnmpTlstmParamsRowStatus_Object = MibTableColumn
snmpTlstmParamsRowStatus = _SnmpTlstmParamsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 6, 1, 3),
    _SnmpTlstmParamsRowStatus_Type()
)
snmpTlstmParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmParamsRowStatus.setStatus("current")
_SnmpTlstmAddrCount_Type = Gauge32
_SnmpTlstmAddrCount_Object = MibScalar
snmpTlstmAddrCount = _SnmpTlstmAddrCount_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 7),
    _SnmpTlstmAddrCount_Type()
)
snmpTlstmAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmAddrCount.setStatus("current")
_SnmpTlstmAddrTableLastChanged_Type = TimeStamp
_SnmpTlstmAddrTableLastChanged_Object = MibScalar
snmpTlstmAddrTableLastChanged = _SnmpTlstmAddrTableLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 8),
    _SnmpTlstmAddrTableLastChanged_Type()
)
snmpTlstmAddrTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTlstmAddrTableLastChanged.setStatus("current")
_SnmpTlstmAddrTable_Object = MibTable
snmpTlstmAddrTable = _SnmpTlstmAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    snmpTlstmAddrTable.setStatus("current")
_SnmpTlstmAddrEntry_Object = MibTableRow
snmpTlstmAddrEntry = _SnmpTlstmAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 9, 1)
)
snmpTlstmAddrEntry.setIndexNames(
    (1, "SNMP-TARGET-MIB", "snmpTargetAddrName"),
)
if mibBuilder.loadTexts:
    snmpTlstmAddrEntry.setStatus("current")
_SnmpTlstmAddrServerFingerprint_Type = SnmpTLSFingerprint
_SnmpTlstmAddrServerFingerprint_Object = MibTableColumn
snmpTlstmAddrServerFingerprint = _SnmpTlstmAddrServerFingerprint_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 9, 1, 1),
    _SnmpTlstmAddrServerFingerprint_Type()
)
snmpTlstmAddrServerFingerprint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmAddrServerFingerprint.setStatus("current")
_SnmpTlstmAddrServerIdentity_Type = SnmpAdminString
_SnmpTlstmAddrServerIdentity_Object = MibTableColumn
snmpTlstmAddrServerIdentity = _SnmpTlstmAddrServerIdentity_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 9, 1, 2),
    _SnmpTlstmAddrServerIdentity_Type()
)
snmpTlstmAddrServerIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmAddrServerIdentity.setStatus("current")


class _SnmpTlstmAddrStorageType_Type(StorageType):
    """Custom type snmpTlstmAddrStorageType based on StorageType"""


_SnmpTlstmAddrStorageType_Object = MibTableColumn
snmpTlstmAddrStorageType = _SnmpTlstmAddrStorageType_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 9, 1, 3),
    _SnmpTlstmAddrStorageType_Type()
)
snmpTlstmAddrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmAddrStorageType.setStatus("current")
_SnmpTlstmAddrRowStatus_Type = RowStatus
_SnmpTlstmAddrRowStatus_Object = MibTableColumn
snmpTlstmAddrRowStatus = _SnmpTlstmAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 198, 2, 2, 1, 9, 1, 4),
    _SnmpTlstmAddrRowStatus_Type()
)
snmpTlstmAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTlstmAddrRowStatus.setStatus("current")
_SnmpTlstmConformance_ObjectIdentity = ObjectIdentity
snmpTlstmConformance = _SnmpTlstmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 3)
)
_SnmpTlstmCompliances_ObjectIdentity = ObjectIdentity
snmpTlstmCompliances = _SnmpTlstmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 3, 1)
)
_SnmpTlstmGroups_ObjectIdentity = ObjectIdentity
snmpTlstmGroups = _SnmpTlstmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 198, 3, 2)
)
_SnmpTLSTCPDomain_ObjectIdentity = ObjectIdentity
snmpTLSTCPDomain = _SnmpTLSTCPDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 8)
)
if mibBuilder.loadTexts:
    snmpTLSTCPDomain.setStatus("current")
_SnmpDTLSUDPDomain_ObjectIdentity = ObjectIdentity
snmpDTLSUDPDomain = _SnmpDTLSUDPDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 9)
)
if mibBuilder.loadTexts:
    snmpDTLSUDPDomain.setStatus("current")

# Managed Objects groups

snmpTlstmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 198, 3, 2, 1)
)
snmpTlstmStatsGroup.setObjects(
      *(("SNMP-TLS-TM-MIB", "snmpTlstmSessionOpens"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionClientCloses"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionOpenErrors"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionAccepts"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionServerCloses"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionNoSessions"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionInvalidClientCertificates"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionUnknownServerCertificate"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionInvalidServerCertificates"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionInvalidCaches"))
)
if mibBuilder.loadTexts:
    snmpTlstmStatsGroup.setStatus("current")

snmpTlstmIncomingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 198, 3, 2, 2)
)
snmpTlstmIncomingGroup.setObjects(
      *(("SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNCount"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNTableLastChanged"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNFingerprint"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNMapType"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNData"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNStorageType"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmCertToTSNRowStatus"))
)
if mibBuilder.loadTexts:
    snmpTlstmIncomingGroup.setStatus("current")

snmpTlstmOutgoingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 198, 3, 2, 3)
)
snmpTlstmOutgoingGroup.setObjects(
      *(("SNMP-TLS-TM-MIB", "snmpTlstmParamsCount"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmParamsTableLastChanged"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmParamsClientFingerprint"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmParamsStorageType"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmParamsRowStatus"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmAddrCount"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmAddrTableLastChanged"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmAddrServerFingerprint"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmAddrServerIdentity"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmAddrStorageType"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmAddrRowStatus"))
)
if mibBuilder.loadTexts:
    snmpTlstmOutgoingGroup.setStatus("current")


# Notification objects

snmpTlstmServerCertificateUnknown = NotificationType(
    (1, 3, 6, 1, 2, 1, 198, 0, 1)
)
snmpTlstmServerCertificateUnknown.setObjects(
    ("SNMP-TLS-TM-MIB", "snmpTlstmSessionUnknownServerCertificate")
)
if mibBuilder.loadTexts:
    snmpTlstmServerCertificateUnknown.setStatus(
        "current"
    )

snmpTlstmServerInvalidCertificate = NotificationType(
    (1, 3, 6, 1, 2, 1, 198, 0, 2)
)
snmpTlstmServerInvalidCertificate.setObjects(
      *(("SNMP-TLS-TM-MIB", "snmpTlstmAddrServerFingerprint"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmSessionInvalidServerCertificates"))
)
if mibBuilder.loadTexts:
    snmpTlstmServerInvalidCertificate.setStatus(
        "current"
    )


# Notifications groups

snmpTlstmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 198, 3, 2, 4)
)
snmpTlstmNotificationGroup.setObjects(
      *(("SNMP-TLS-TM-MIB", "snmpTlstmServerCertificateUnknown"),
        ("SNMP-TLS-TM-MIB", "snmpTlstmServerInvalidCertificate"))
)
if mibBuilder.loadTexts:
    snmpTlstmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

snmpTlstmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 198, 3, 1, 1)
)
if mibBuilder.loadTexts:
    snmpTlstmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-TLS-TM-MIB",
    **{"SnmpTLSAddress": SnmpTLSAddress,
       "SnmpTLSFingerprint": SnmpTLSFingerprint,
       "snmpTlstmMIB": snmpTlstmMIB,
       "snmpTlstmNotifications": snmpTlstmNotifications,
       "snmpTlstmServerCertificateUnknown": snmpTlstmServerCertificateUnknown,
       "snmpTlstmServerInvalidCertificate": snmpTlstmServerInvalidCertificate,
       "snmpTlstmIdentities": snmpTlstmIdentities,
       "snmpTlstmCertToTSNMIdentities": snmpTlstmCertToTSNMIdentities,
       "snmpTlstmCertSpecified": snmpTlstmCertSpecified,
       "snmpTlstmCertSANRFC822Name": snmpTlstmCertSANRFC822Name,
       "snmpTlstmCertSANDNSName": snmpTlstmCertSANDNSName,
       "snmpTlstmCertSANIpAddress": snmpTlstmCertSANIpAddress,
       "snmpTlstmCertSANAny": snmpTlstmCertSANAny,
       "snmpTlstmCertCommonName": snmpTlstmCertCommonName,
       "snmpTlstmObjects": snmpTlstmObjects,
       "snmpTlstmSession": snmpTlstmSession,
       "snmpTlstmSessionOpens": snmpTlstmSessionOpens,
       "snmpTlstmSessionClientCloses": snmpTlstmSessionClientCloses,
       "snmpTlstmSessionOpenErrors": snmpTlstmSessionOpenErrors,
       "snmpTlstmSessionAccepts": snmpTlstmSessionAccepts,
       "snmpTlstmSessionServerCloses": snmpTlstmSessionServerCloses,
       "snmpTlstmSessionNoSessions": snmpTlstmSessionNoSessions,
       "snmpTlstmSessionInvalidClientCertificates": snmpTlstmSessionInvalidClientCertificates,
       "snmpTlstmSessionUnknownServerCertificate": snmpTlstmSessionUnknownServerCertificate,
       "snmpTlstmSessionInvalidServerCertificates": snmpTlstmSessionInvalidServerCertificates,
       "snmpTlstmSessionInvalidCaches": snmpTlstmSessionInvalidCaches,
       "snmpTlstmConfig": snmpTlstmConfig,
       "snmpTlstmCertificateMapping": snmpTlstmCertificateMapping,
       "snmpTlstmCertToTSNCount": snmpTlstmCertToTSNCount,
       "snmpTlstmCertToTSNTableLastChanged": snmpTlstmCertToTSNTableLastChanged,
       "snmpTlstmCertToTSNTable": snmpTlstmCertToTSNTable,
       "snmpTlstmCertToTSNEntry": snmpTlstmCertToTSNEntry,
       "snmpTlstmCertToTSNID": snmpTlstmCertToTSNID,
       "snmpTlstmCertToTSNFingerprint": snmpTlstmCertToTSNFingerprint,
       "snmpTlstmCertToTSNMapType": snmpTlstmCertToTSNMapType,
       "snmpTlstmCertToTSNData": snmpTlstmCertToTSNData,
       "snmpTlstmCertToTSNStorageType": snmpTlstmCertToTSNStorageType,
       "snmpTlstmCertToTSNRowStatus": snmpTlstmCertToTSNRowStatus,
       "snmpTlstmParamsCount": snmpTlstmParamsCount,
       "snmpTlstmParamsTableLastChanged": snmpTlstmParamsTableLastChanged,
       "snmpTlstmParamsTable": snmpTlstmParamsTable,
       "snmpTlstmParamsEntry": snmpTlstmParamsEntry,
       "snmpTlstmParamsClientFingerprint": snmpTlstmParamsClientFingerprint,
       "snmpTlstmParamsStorageType": snmpTlstmParamsStorageType,
       "snmpTlstmParamsRowStatus": snmpTlstmParamsRowStatus,
       "snmpTlstmAddrCount": snmpTlstmAddrCount,
       "snmpTlstmAddrTableLastChanged": snmpTlstmAddrTableLastChanged,
       "snmpTlstmAddrTable": snmpTlstmAddrTable,
       "snmpTlstmAddrEntry": snmpTlstmAddrEntry,
       "snmpTlstmAddrServerFingerprint": snmpTlstmAddrServerFingerprint,
       "snmpTlstmAddrServerIdentity": snmpTlstmAddrServerIdentity,
       "snmpTlstmAddrStorageType": snmpTlstmAddrStorageType,
       "snmpTlstmAddrRowStatus": snmpTlstmAddrRowStatus,
       "snmpTlstmConformance": snmpTlstmConformance,
       "snmpTlstmCompliances": snmpTlstmCompliances,
       "snmpTlstmCompliance": snmpTlstmCompliance,
       "snmpTlstmGroups": snmpTlstmGroups,
       "snmpTlstmStatsGroup": snmpTlstmStatsGroup,
       "snmpTlstmIncomingGroup": snmpTlstmIncomingGroup,
       "snmpTlstmOutgoingGroup": snmpTlstmOutgoingGroup,
       "snmpTlstmNotificationGroup": snmpTlstmNotificationGroup,
       "snmpTLSTCPDomain": snmpTLSTCPDomain,
       "snmpDTLSUDPDomain": snmpDTLSUDPDomain}
)
