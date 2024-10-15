# SNMP MIB module (CIENA-WS-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-WS-SOFTWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:11 2024
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(StringMaxl128,
 StringMaxl256,
 StringMaxl32,
 StringMaxl64) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "StringMaxl128",
    "StringMaxl256",
    "StringMaxl32",
    "StringMaxl64")

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

cienaWsSoftwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14)
)
cienaWsSoftwareMIB.setRevisions(
        ("2016-11-03 00:00",
         "2016-06-14 00:00",
         "2015-09-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SoftwareOpState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("restartinprogress", 3),
          ("subsystemfailed", 4),
          ("systemloaderror", 5),
          ("unknown", 0),
          ("upgradeinprogress", 2))
    )



class SoftwareRtncode(Unsigned32, TextualConvention):
    status = "current"


class UpgradeOpState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("activationcomplete", 9),
          ("activationfailed", 10),
          ("activationinprogress", 8),
          ("cancelcomplete", 15),
          ("cancelfailed", 16),
          ("cancelinprogress", 14),
          ("commitcomplete", 12),
          ("commitfailed", 13),
          ("commitinprogress", 11),
          ("downloadcomplete", 3),
          ("downloadfailed", 4),
          ("downloadinprogress", 2),
          ("idle", 1),
          ("installationcomplete", 6),
          ("installationfailed", 7),
          ("installationinprogress", 5),
          ("manualcancel", 18),
          ("manualcommit", 17),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CienaWsSoftwareObjects_ObjectIdentity = ObjectIdentity
cienaWsSoftwareObjects = _CienaWsSoftwareObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 1)
)
_CienaWsSoftwareConformance_ObjectIdentity = ObjectIdentity
cienaWsSoftwareConformance = _CienaWsSoftwareConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2)
)
_CienaWsSoftwareGroups_ObjectIdentity = ObjectIdentity
cienaWsSoftwareGroups = _CienaWsSoftwareGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 1)
)
_CienaWsSoftwareCompliances_ObjectIdentity = ObjectIdentity
cienaWsSoftwareCompliances = _CienaWsSoftwareCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 2)
)
_CwsSoftwareStatusTable_Object = MibTable
cwsSoftwareStatusTable = _CwsSoftwareStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3)
)
if mibBuilder.loadTexts:
    cwsSoftwareStatusTable.setStatus("current")
_CwsSoftwareStatusEntry_Object = MibTableRow
cwsSoftwareStatusEntry = _CwsSoftwareStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1)
)
cwsSoftwareStatusEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSoftwareStatusEntry.setStatus("current")


class _CwsSoftwareStatusTableSnmpKey_Type(Integer32):
    """Custom type cwsSoftwareStatusTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareStatusTableSnmpKey_Type.__name__ = "Integer32"
_CwsSoftwareStatusTableSnmpKey_Object = MibTableColumn
cwsSoftwareStatusTableSnmpKey = _CwsSoftwareStatusTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 1),
    _CwsSoftwareStatusTableSnmpKey_Type()
)
cwsSoftwareStatusTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareStatusTableSnmpKey.setStatus("current")
_CwsSoftwareStatusSoftwareOperationalState_Type = SoftwareOpState
_CwsSoftwareStatusSoftwareOperationalState_Object = MibTableColumn
cwsSoftwareStatusSoftwareOperationalState = _CwsSoftwareStatusSoftwareOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 2),
    _CwsSoftwareStatusSoftwareOperationalState_Type()
)
cwsSoftwareStatusSoftwareOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareStatusSoftwareOperationalState.setStatus("current")
_CwsSoftwareStatusUpgradeOperationalState_Type = UpgradeOpState
_CwsSoftwareStatusUpgradeOperationalState_Object = MibTableColumn
cwsSoftwareStatusUpgradeOperationalState = _CwsSoftwareStatusUpgradeOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 3),
    _CwsSoftwareStatusUpgradeOperationalState_Type()
)
cwsSoftwareStatusUpgradeOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareStatusUpgradeOperationalState.setStatus("current")
_CwsSoftwareStatusCommittedVersion_Type = StringMaxl32
_CwsSoftwareStatusCommittedVersion_Object = MibTableColumn
cwsSoftwareStatusCommittedVersion = _CwsSoftwareStatusCommittedVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 4),
    _CwsSoftwareStatusCommittedVersion_Type()
)
cwsSoftwareStatusCommittedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareStatusCommittedVersion.setStatus("current")
_CwsSoftwareStatusActiveVersion_Type = StringMaxl32
_CwsSoftwareStatusActiveVersion_Object = MibTableColumn
cwsSoftwareStatusActiveVersion = _CwsSoftwareStatusActiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 5),
    _CwsSoftwareStatusActiveVersion_Type()
)
cwsSoftwareStatusActiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareStatusActiveVersion.setStatus("current")
_CwsSoftwareStatusUpgradeToVersion_Type = StringMaxl32
_CwsSoftwareStatusUpgradeToVersion_Object = MibTableColumn
cwsSoftwareStatusUpgradeToVersion = _CwsSoftwareStatusUpgradeToVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 6),
    _CwsSoftwareStatusUpgradeToVersion_Type()
)
cwsSoftwareStatusUpgradeToVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareStatusUpgradeToVersion.setStatus("current")
_CwsSoftwareStatusLastOperation_Type = StringMaxl128
_CwsSoftwareStatusLastOperation_Object = MibTableColumn
cwsSoftwareStatusLastOperation = _CwsSoftwareStatusLastOperation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 3, 1, 7),
    _CwsSoftwareStatusLastOperation_Type()
)
cwsSoftwareStatusLastOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareStatusLastOperation.setStatus("current")
_CwsSoftwareCheckStatusReportTable_Object = MibTable
cwsSoftwareCheckStatusReportTable = _CwsSoftwareCheckStatusReportTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4)
)
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportTable.setStatus("current")
_CwsSoftwareCheckStatusReportEntry_Object = MibTableRow
cwsSoftwareCheckStatusReportEntry = _CwsSoftwareCheckStatusReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1)
)
cwsSoftwareCheckStatusReportEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportEntry.setStatus("current")


class _CwsSoftwareCheckStatusReportTableSnmpKey_Type(Integer32):
    """Custom type cwsSoftwareCheckStatusReportTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareCheckStatusReportTableSnmpKey_Type.__name__ = "Integer32"
_CwsSoftwareCheckStatusReportTableSnmpKey_Object = MibTableColumn
cwsSoftwareCheckStatusReportTableSnmpKey = _CwsSoftwareCheckStatusReportTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 1),
    _CwsSoftwareCheckStatusReportTableSnmpKey_Type()
)
cwsSoftwareCheckStatusReportTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportTableSnmpKey.setStatus("current")
_CwsSoftwareCheckStatusReportActiveReleaseVersion_Type = StringMaxl32
_CwsSoftwareCheckStatusReportActiveReleaseVersion_Object = MibTableColumn
cwsSoftwareCheckStatusReportActiveReleaseVersion = _CwsSoftwareCheckStatusReportActiveReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 2),
    _CwsSoftwareCheckStatusReportActiveReleaseVersion_Type()
)
cwsSoftwareCheckStatusReportActiveReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportActiveReleaseVersion.setStatus("current")
_CwsSoftwareCheckStatusReportServerReleaseVersion_Type = StringMaxl32
_CwsSoftwareCheckStatusReportServerReleaseVersion_Object = MibTableColumn
cwsSoftwareCheckStatusReportServerReleaseVersion = _CwsSoftwareCheckStatusReportServerReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 3),
    _CwsSoftwareCheckStatusReportServerReleaseVersion_Type()
)
cwsSoftwareCheckStatusReportServerReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportServerReleaseVersion.setStatus("current")
_CwsSoftwareCheckStatusReportLocalReleaseVersion_Type = StringMaxl32
_CwsSoftwareCheckStatusReportLocalReleaseVersion_Object = MibTableColumn
cwsSoftwareCheckStatusReportLocalReleaseVersion = _CwsSoftwareCheckStatusReportLocalReleaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 4),
    _CwsSoftwareCheckStatusReportLocalReleaseVersion_Type()
)
cwsSoftwareCheckStatusReportLocalReleaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportLocalReleaseVersion.setStatus("current")
_CwsSoftwareCheckStatusReportServerHostname_Type = StringMaxl32
_CwsSoftwareCheckStatusReportServerHostname_Object = MibTableColumn
cwsSoftwareCheckStatusReportServerHostname = _CwsSoftwareCheckStatusReportServerHostname_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 5),
    _CwsSoftwareCheckStatusReportServerHostname_Type()
)
cwsSoftwareCheckStatusReportServerHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportServerHostname.setStatus("current")
_CwsSoftwareCheckStatusReportServerPath_Type = StringMaxl256
_CwsSoftwareCheckStatusReportServerPath_Object = MibTableColumn
cwsSoftwareCheckStatusReportServerPath = _CwsSoftwareCheckStatusReportServerPath_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 6),
    _CwsSoftwareCheckStatusReportServerPath_Type()
)
cwsSoftwareCheckStatusReportServerPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportServerPath.setStatus("current")
_CwsSoftwareCheckStatusReportTimestamp_Type = StringMaxl128
_CwsSoftwareCheckStatusReportTimestamp_Object = MibTableColumn
cwsSoftwareCheckStatusReportTimestamp = _CwsSoftwareCheckStatusReportTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 7),
    _CwsSoftwareCheckStatusReportTimestamp_Type()
)
cwsSoftwareCheckStatusReportTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportTimestamp.setStatus("current")
_CwsSoftwareCheckStatusReportCheckOperationalState_Type = SoftwareOpState
_CwsSoftwareCheckStatusReportCheckOperationalState_Object = MibTableColumn
cwsSoftwareCheckStatusReportCheckOperationalState = _CwsSoftwareCheckStatusReportCheckOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 8),
    _CwsSoftwareCheckStatusReportCheckOperationalState_Type()
)
cwsSoftwareCheckStatusReportCheckOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportCheckOperationalState.setStatus("current")
_CwsSoftwareCheckStatusReportCheckUpgradeState_Type = UpgradeOpState
_CwsSoftwareCheckStatusReportCheckUpgradeState_Object = MibTableColumn
cwsSoftwareCheckStatusReportCheckUpgradeState = _CwsSoftwareCheckStatusReportCheckUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 9),
    _CwsSoftwareCheckStatusReportCheckUpgradeState_Type()
)
cwsSoftwareCheckStatusReportCheckUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportCheckUpgradeState.setStatus("current")
_CwsSoftwareCheckStatusReportRequiredActivationType_Type = StringMaxl32
_CwsSoftwareCheckStatusReportRequiredActivationType_Object = MibTableColumn
cwsSoftwareCheckStatusReportRequiredActivationType = _CwsSoftwareCheckStatusReportRequiredActivationType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 10),
    _CwsSoftwareCheckStatusReportRequiredActivationType_Type()
)
cwsSoftwareCheckStatusReportRequiredActivationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportRequiredActivationType.setStatus("current")
_CwsSoftwareCheckStatusReportServiceInterruptionActivation_Type = TruthValue
_CwsSoftwareCheckStatusReportServiceInterruptionActivation_Object = MibTableColumn
cwsSoftwareCheckStatusReportServiceInterruptionActivation = _CwsSoftwareCheckStatusReportServiceInterruptionActivation_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 4, 1, 11),
    _CwsSoftwareCheckStatusReportServiceInterruptionActivation_Type()
)
cwsSoftwareCheckStatusReportServiceInterruptionActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareCheckStatusReportServiceInterruptionActivation.setStatus("current")
_CwsSoftwareUpgradeServerTable_Object = MibTable
cwsSoftwareUpgradeServerTable = _CwsSoftwareUpgradeServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5)
)
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerTable.setStatus("current")
_CwsSoftwareUpgradeServerEntry_Object = MibTableRow
cwsSoftwareUpgradeServerEntry = _CwsSoftwareUpgradeServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1)
)
cwsSoftwareUpgradeServerEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerEntry.setStatus("current")


class _CwsSoftwareUpgradeServerTableSnmpKey_Type(Integer32):
    """Custom type cwsSoftwareUpgradeServerTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareUpgradeServerTableSnmpKey_Type.__name__ = "Integer32"
_CwsSoftwareUpgradeServerTableSnmpKey_Object = MibTableColumn
cwsSoftwareUpgradeServerTableSnmpKey = _CwsSoftwareUpgradeServerTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 1),
    _CwsSoftwareUpgradeServerTableSnmpKey_Type()
)
cwsSoftwareUpgradeServerTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerTableSnmpKey.setStatus("current")
_CwsSoftwareUpgradeServerIndex_Type = Unsigned32
_CwsSoftwareUpgradeServerIndex_Object = MibTableColumn
cwsSoftwareUpgradeServerIndex = _CwsSoftwareUpgradeServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 2),
    _CwsSoftwareUpgradeServerIndex_Type()
)
cwsSoftwareUpgradeServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerIndex.setStatus("current")
_CwsSoftwareUpgradeServerServer_Type = StringMaxl64
_CwsSoftwareUpgradeServerServer_Object = MibTableColumn
cwsSoftwareUpgradeServerServer = _CwsSoftwareUpgradeServerServer_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 3),
    _CwsSoftwareUpgradeServerServer_Type()
)
cwsSoftwareUpgradeServerServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerServer.setStatus("current")


class _CwsSoftwareUpgradeServerMode_Type(Integer32):
    """Custom type cwsSoftwareUpgradeServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("scp", 3),
          ("sftp", 2),
          ("tftp", 0))
    )


_CwsSoftwareUpgradeServerMode_Type.__name__ = "Integer32"
_CwsSoftwareUpgradeServerMode_Object = MibTableColumn
cwsSoftwareUpgradeServerMode = _CwsSoftwareUpgradeServerMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 4),
    _CwsSoftwareUpgradeServerMode_Type()
)
cwsSoftwareUpgradeServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerMode.setStatus("current")


class _CwsSoftwareUpgradeServerRemotePath_Type(OctetString):
    """Custom type cwsSoftwareUpgradeServerRemotePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CwsSoftwareUpgradeServerRemotePath_Type.__name__ = "OctetString"
_CwsSoftwareUpgradeServerRemotePath_Object = MibTableColumn
cwsSoftwareUpgradeServerRemotePath = _CwsSoftwareUpgradeServerRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 5),
    _CwsSoftwareUpgradeServerRemotePath_Type()
)
cwsSoftwareUpgradeServerRemotePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerRemotePath.setStatus("current")
_CwsSoftwareUpgradeServerLoginId_Type = StringMaxl32
_CwsSoftwareUpgradeServerLoginId_Object = MibTableColumn
cwsSoftwareUpgradeServerLoginId = _CwsSoftwareUpgradeServerLoginId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 6),
    _CwsSoftwareUpgradeServerLoginId_Type()
)
cwsSoftwareUpgradeServerLoginId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerLoginId.setStatus("current")
_CwsSoftwareUpgradeServerPassword_Type = StringMaxl32
_CwsSoftwareUpgradeServerPassword_Object = MibTableColumn
cwsSoftwareUpgradeServerPassword = _CwsSoftwareUpgradeServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 5, 1, 7),
    _CwsSoftwareUpgradeServerPassword_Type()
)
cwsSoftwareUpgradeServerPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeServerPassword.setStatus("current")
_CwsSoftwareUpgradeLogListTable_Object = MibTable
cwsSoftwareUpgradeLogListTable = _CwsSoftwareUpgradeLogListTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6)
)
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeLogListTable.setStatus("current")
_CwsSoftwareUpgradeLogListEntry_Object = MibTableRow
cwsSoftwareUpgradeLogListEntry = _CwsSoftwareUpgradeLogListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1)
)
cwsSoftwareUpgradeLogListEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeLogListLogIndex"),
)
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeLogListEntry.setStatus("current")


class _CwsSoftwareUpgradeLogListLogIndex_Type(Integer32):
    """Custom type cwsSoftwareUpgradeLogListLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareUpgradeLogListLogIndex_Type.__name__ = "Integer32"
_CwsSoftwareUpgradeLogListLogIndex_Object = MibTableColumn
cwsSoftwareUpgradeLogListLogIndex = _CwsSoftwareUpgradeLogListLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1, 1),
    _CwsSoftwareUpgradeLogListLogIndex_Type()
)
cwsSoftwareUpgradeLogListLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeLogListLogIndex.setStatus("current")
_CwsSoftwareUpgradeLogListDateAndTime_Type = StringMaxl64
_CwsSoftwareUpgradeLogListDateAndTime_Object = MibTableColumn
cwsSoftwareUpgradeLogListDateAndTime = _CwsSoftwareUpgradeLogListDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1, 2),
    _CwsSoftwareUpgradeLogListDateAndTime_Type()
)
cwsSoftwareUpgradeLogListDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeLogListDateAndTime.setStatus("current")
_CwsSoftwareUpgradeLogListText_Type = StringMaxl256
_CwsSoftwareUpgradeLogListText_Object = MibTableColumn
cwsSoftwareUpgradeLogListText = _CwsSoftwareUpgradeLogListText_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 6, 1, 3),
    _CwsSoftwareUpgradeLogListText_Type()
)
cwsSoftwareUpgradeLogListText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareUpgradeLogListText.setStatus("current")
_CwsSoftwareActiveSoftwareTable_Object = MibTable
cwsSoftwareActiveSoftwareTable = _CwsSoftwareActiveSoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7)
)
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareTable.setStatus("current")
_CwsSoftwareActiveSoftwareEntry_Object = MibTableRow
cwsSoftwareActiveSoftwareEntry = _CwsSoftwareActiveSoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1)
)
cwsSoftwareActiveSoftwareEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareEntry.setStatus("current")


class _CwsSoftwareActiveSoftwareTableSnmpKey_Type(Integer32):
    """Custom type cwsSoftwareActiveSoftwareTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareActiveSoftwareTableSnmpKey_Type.__name__ = "Integer32"
_CwsSoftwareActiveSoftwareTableSnmpKey_Object = MibTableColumn
cwsSoftwareActiveSoftwareTableSnmpKey = _CwsSoftwareActiveSoftwareTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 1),
    _CwsSoftwareActiveSoftwareTableSnmpKey_Type()
)
cwsSoftwareActiveSoftwareTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareTableSnmpKey.setStatus("current")
_CwsSoftwareActiveSoftwareVersion_Type = StringMaxl32
_CwsSoftwareActiveSoftwareVersion_Object = MibTableColumn
cwsSoftwareActiveSoftwareVersion = _CwsSoftwareActiveSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 2),
    _CwsSoftwareActiveSoftwareVersion_Type()
)
cwsSoftwareActiveSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareVersion.setStatus("current")
_CwsSoftwareActiveSoftwareBuildNumber_Type = StringMaxl32
_CwsSoftwareActiveSoftwareBuildNumber_Object = MibTableColumn
cwsSoftwareActiveSoftwareBuildNumber = _CwsSoftwareActiveSoftwareBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 3),
    _CwsSoftwareActiveSoftwareBuildNumber_Type()
)
cwsSoftwareActiveSoftwareBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareBuildNumber.setStatus("current")
_CwsSoftwareActiveSoftwareBuildDate_Type = StringMaxl32
_CwsSoftwareActiveSoftwareBuildDate_Object = MibTableColumn
cwsSoftwareActiveSoftwareBuildDate = _CwsSoftwareActiveSoftwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 4),
    _CwsSoftwareActiveSoftwareBuildDate_Type()
)
cwsSoftwareActiveSoftwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareBuildDate.setStatus("current")
_CwsSoftwareActiveSoftwareCatalogName_Type = StringMaxl64
_CwsSoftwareActiveSoftwareCatalogName_Object = MibTableColumn
cwsSoftwareActiveSoftwareCatalogName = _CwsSoftwareActiveSoftwareCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 5),
    _CwsSoftwareActiveSoftwareCatalogName_Type()
)
cwsSoftwareActiveSoftwareCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareCatalogName.setStatus("current")
_CwsSoftwareActiveSoftwareNumberOfComponents_Type = Unsigned32
_CwsSoftwareActiveSoftwareNumberOfComponents_Object = MibTableColumn
cwsSoftwareActiveSoftwareNumberOfComponents = _CwsSoftwareActiveSoftwareNumberOfComponents_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 7, 1, 6),
    _CwsSoftwareActiveSoftwareNumberOfComponents_Type()
)
cwsSoftwareActiveSoftwareNumberOfComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActiveSoftwareNumberOfComponents.setStatus("current")
_CwsSoftwareActivecomponentsTable_Object = MibTable
cwsSoftwareActivecomponentsTable = _CwsSoftwareActivecomponentsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8)
)
if mibBuilder.loadTexts:
    cwsSoftwareActivecomponentsTable.setStatus("current")
_CwsSoftwareActivecomponentsEntry_Object = MibTableRow
cwsSoftwareActivecomponentsEntry = _CwsSoftwareActivecomponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1)
)
cwsSoftwareActivecomponentsEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsComponentIndex"),
)
if mibBuilder.loadTexts:
    cwsSoftwareActivecomponentsEntry.setStatus("current")


class _CwsSoftwareActivecomponentsComponentIndex_Type(Integer32):
    """Custom type cwsSoftwareActivecomponentsComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareActivecomponentsComponentIndex_Type.__name__ = "Integer32"
_CwsSoftwareActivecomponentsComponentIndex_Object = MibTableColumn
cwsSoftwareActivecomponentsComponentIndex = _CwsSoftwareActivecomponentsComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 1),
    _CwsSoftwareActivecomponentsComponentIndex_Type()
)
cwsSoftwareActivecomponentsComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareActivecomponentsComponentIndex.setStatus("current")
_CwsSoftwareActivecomponentsName_Type = StringMaxl32
_CwsSoftwareActivecomponentsName_Object = MibTableColumn
cwsSoftwareActivecomponentsName = _CwsSoftwareActivecomponentsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 2),
    _CwsSoftwareActivecomponentsName_Type()
)
cwsSoftwareActivecomponentsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActivecomponentsName.setStatus("current")
_CwsSoftwareActivecomponentsVersion_Type = StringMaxl32
_CwsSoftwareActivecomponentsVersion_Object = MibTableColumn
cwsSoftwareActivecomponentsVersion = _CwsSoftwareActivecomponentsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 3),
    _CwsSoftwareActivecomponentsVersion_Type()
)
cwsSoftwareActivecomponentsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActivecomponentsVersion.setStatus("current")
_CwsSoftwareActivecomponentsBuildNumber_Type = StringMaxl32
_CwsSoftwareActivecomponentsBuildNumber_Object = MibTableColumn
cwsSoftwareActivecomponentsBuildNumber = _CwsSoftwareActivecomponentsBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 4),
    _CwsSoftwareActivecomponentsBuildNumber_Type()
)
cwsSoftwareActivecomponentsBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActivecomponentsBuildNumber.setStatus("current")


class _CwsSoftwareActivecomponentsStatus_Type(Integer32):
    """Custom type cwsSoftwareActivecomponentsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("failed", 2),
          ("pending", 3),
          ("restarting", 4),
          ("unknown", 0))
    )


_CwsSoftwareActivecomponentsStatus_Type.__name__ = "Integer32"
_CwsSoftwareActivecomponentsStatus_Object = MibTableColumn
cwsSoftwareActivecomponentsStatus = _CwsSoftwareActivecomponentsStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 8, 1, 5),
    _CwsSoftwareActivecomponentsStatus_Type()
)
cwsSoftwareActivecomponentsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareActivecomponentsStatus.setStatus("current")
_CwsSoftwareBootPartitionListTable_Object = MibTable
cwsSoftwareBootPartitionListTable = _CwsSoftwareBootPartitionListTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9)
)
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListTable.setStatus("current")
_CwsSoftwareBootPartitionListEntry_Object = MibTableRow
cwsSoftwareBootPartitionListEntry = _CwsSoftwareBootPartitionListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1)
)
cwsSoftwareBootPartitionListEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListIndex"),
)
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListEntry.setStatus("current")


class _CwsSoftwareBootPartitionListIndex_Type(Integer32):
    """Custom type cwsSoftwareBootPartitionListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareBootPartitionListIndex_Type.__name__ = "Integer32"
_CwsSoftwareBootPartitionListIndex_Object = MibTableColumn
cwsSoftwareBootPartitionListIndex = _CwsSoftwareBootPartitionListIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 1),
    _CwsSoftwareBootPartitionListIndex_Type()
)
cwsSoftwareBootPartitionListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListIndex.setStatus("current")


class _CwsSoftwareBootPartitionListName_Type(Integer32):
    """Custom type cwsSoftwareBootPartitionListName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backupbl", 7),
          ("bootloader0", 2),
          ("bootloader1", 4),
          ("firmware0", 5),
          ("firmware1", 6),
          ("kernel0", 1),
          ("kernel1", 3),
          ("unknown", 0))
    )


_CwsSoftwareBootPartitionListName_Type.__name__ = "Integer32"
_CwsSoftwareBootPartitionListName_Object = MibTableColumn
cwsSoftwareBootPartitionListName = _CwsSoftwareBootPartitionListName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 2),
    _CwsSoftwareBootPartitionListName_Type()
)
cwsSoftwareBootPartitionListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListName.setStatus("current")
_CwsSoftwareBootPartitionListVersion_Type = StringMaxl32
_CwsSoftwareBootPartitionListVersion_Object = MibTableColumn
cwsSoftwareBootPartitionListVersion = _CwsSoftwareBootPartitionListVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 3),
    _CwsSoftwareBootPartitionListVersion_Type()
)
cwsSoftwareBootPartitionListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListVersion.setStatus("current")
_CwsSoftwareBootPartitionListDate_Type = StringMaxl32
_CwsSoftwareBootPartitionListDate_Object = MibTableColumn
cwsSoftwareBootPartitionListDate = _CwsSoftwareBootPartitionListDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 4),
    _CwsSoftwareBootPartitionListDate_Type()
)
cwsSoftwareBootPartitionListDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListDate.setStatus("current")


class _CwsSoftwareBootPartitionListState_Type(Integer32):
    """Custom type cwsSoftwareBootPartitionListState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notapplicable", 3),
          ("standby", 2),
          ("unknown", 0))
    )


_CwsSoftwareBootPartitionListState_Type.__name__ = "Integer32"
_CwsSoftwareBootPartitionListState_Object = MibTableColumn
cwsSoftwareBootPartitionListState = _CwsSoftwareBootPartitionListState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 5),
    _CwsSoftwareBootPartitionListState_Type()
)
cwsSoftwareBootPartitionListState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListState.setStatus("current")


class _CwsSoftwareBootPartitionListIntegrityCheck_Type(Integer32):
    """Custom type cwsSoftwareBootPartitionListIntegrityCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("pass", 1),
          ("unknown", 0))
    )


_CwsSoftwareBootPartitionListIntegrityCheck_Type.__name__ = "Integer32"
_CwsSoftwareBootPartitionListIntegrityCheck_Object = MibTableColumn
cwsSoftwareBootPartitionListIntegrityCheck = _CwsSoftwareBootPartitionListIntegrityCheck_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 9, 1, 6),
    _CwsSoftwareBootPartitionListIntegrityCheck_Type()
)
cwsSoftwareBootPartitionListIntegrityCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareBootPartitionListIntegrityCheck.setStatus("current")
_CwsSoftwareVersionsTable_Object = MibTable
cwsSoftwareVersionsTable = _CwsSoftwareVersionsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10)
)
if mibBuilder.loadTexts:
    cwsSoftwareVersionsTable.setStatus("current")
_CwsSoftwareVersionsEntry_Object = MibTableRow
cwsSoftwareVersionsEntry = _CwsSoftwareVersionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1)
)
cwsSoftwareVersionsEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsIndex"),
)
if mibBuilder.loadTexts:
    cwsSoftwareVersionsEntry.setStatus("current")


class _CwsSoftwareVersionsIndex_Type(Integer32):
    """Custom type cwsSoftwareVersionsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareVersionsIndex_Type.__name__ = "Integer32"
_CwsSoftwareVersionsIndex_Object = MibTableColumn
cwsSoftwareVersionsIndex = _CwsSoftwareVersionsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 1),
    _CwsSoftwareVersionsIndex_Type()
)
cwsSoftwareVersionsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareVersionsIndex.setStatus("current")
_CwsSoftwareVersionsVersion_Type = StringMaxl32
_CwsSoftwareVersionsVersion_Object = MibTableColumn
cwsSoftwareVersionsVersion = _CwsSoftwareVersionsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 2),
    _CwsSoftwareVersionsVersion_Type()
)
cwsSoftwareVersionsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareVersionsVersion.setStatus("current")
_CwsSoftwareVersionsBuildNumber_Type = StringMaxl32
_CwsSoftwareVersionsBuildNumber_Object = MibTableColumn
cwsSoftwareVersionsBuildNumber = _CwsSoftwareVersionsBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 3),
    _CwsSoftwareVersionsBuildNumber_Type()
)
cwsSoftwareVersionsBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareVersionsBuildNumber.setStatus("current")
_CwsSoftwareVersionsBuildTag_Type = StringMaxl32
_CwsSoftwareVersionsBuildTag_Object = MibTableColumn
cwsSoftwareVersionsBuildTag = _CwsSoftwareVersionsBuildTag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 4),
    _CwsSoftwareVersionsBuildTag_Type()
)
cwsSoftwareVersionsBuildTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareVersionsBuildTag.setStatus("current")
_CwsSoftwareVersionsBuildDate_Type = StringMaxl32
_CwsSoftwareVersionsBuildDate_Object = MibTableColumn
cwsSoftwareVersionsBuildDate = _CwsSoftwareVersionsBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 5),
    _CwsSoftwareVersionsBuildDate_Type()
)
cwsSoftwareVersionsBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareVersionsBuildDate.setStatus("current")
_CwsSoftwareVersionsSize_Type = Unsigned32
_CwsSoftwareVersionsSize_Object = MibTableColumn
cwsSoftwareVersionsSize = _CwsSoftwareVersionsSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 6),
    _CwsSoftwareVersionsSize_Type()
)
cwsSoftwareVersionsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareVersionsSize.setStatus("current")
_CwsSoftwareVersionsNumberOfComponents_Type = Unsigned32
_CwsSoftwareVersionsNumberOfComponents_Object = MibTableColumn
cwsSoftwareVersionsNumberOfComponents = _CwsSoftwareVersionsNumberOfComponents_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 10, 1, 7),
    _CwsSoftwareVersionsNumberOfComponents_Type()
)
cwsSoftwareVersionsNumberOfComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareVersionsNumberOfComponents.setStatus("current")
_CwsSoftwareInstalledcomponentsTable_Object = MibTable
cwsSoftwareInstalledcomponentsTable = _CwsSoftwareInstalledcomponentsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11)
)
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsTable.setStatus("current")
_CwsSoftwareInstalledcomponentsEntry_Object = MibTableRow
cwsSoftwareInstalledcomponentsEntry = _CwsSoftwareInstalledcomponentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1)
)
cwsSoftwareInstalledcomponentsEntry.setIndexNames(
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsIndex"),
    (0, "CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsComponentIndex"),
)
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsEntry.setStatus("current")


class _CwsSoftwareInstalledcomponentsComponentIndex_Type(Integer32):
    """Custom type cwsSoftwareInstalledcomponentsComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsSoftwareInstalledcomponentsComponentIndex_Type.__name__ = "Integer32"
_CwsSoftwareInstalledcomponentsComponentIndex_Object = MibTableColumn
cwsSoftwareInstalledcomponentsComponentIndex = _CwsSoftwareInstalledcomponentsComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 1),
    _CwsSoftwareInstalledcomponentsComponentIndex_Type()
)
cwsSoftwareInstalledcomponentsComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsComponentIndex.setStatus("current")
_CwsSoftwareInstalledcomponentsName_Type = StringMaxl32
_CwsSoftwareInstalledcomponentsName_Object = MibTableColumn
cwsSoftwareInstalledcomponentsName = _CwsSoftwareInstalledcomponentsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 2),
    _CwsSoftwareInstalledcomponentsName_Type()
)
cwsSoftwareInstalledcomponentsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsName.setStatus("current")
_CwsSoftwareInstalledcomponentsVersion_Type = StringMaxl32
_CwsSoftwareInstalledcomponentsVersion_Object = MibTableColumn
cwsSoftwareInstalledcomponentsVersion = _CwsSoftwareInstalledcomponentsVersion_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 3),
    _CwsSoftwareInstalledcomponentsVersion_Type()
)
cwsSoftwareInstalledcomponentsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsVersion.setStatus("current")
_CwsSoftwareInstalledcomponentsBuildNumber_Type = StringMaxl32
_CwsSoftwareInstalledcomponentsBuildNumber_Object = MibTableColumn
cwsSoftwareInstalledcomponentsBuildNumber = _CwsSoftwareInstalledcomponentsBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 4),
    _CwsSoftwareInstalledcomponentsBuildNumber_Type()
)
cwsSoftwareInstalledcomponentsBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsBuildNumber.setStatus("current")
_CwsSoftwareInstalledcomponentsBuildTag_Type = StringMaxl32
_CwsSoftwareInstalledcomponentsBuildTag_Object = MibTableColumn
cwsSoftwareInstalledcomponentsBuildTag = _CwsSoftwareInstalledcomponentsBuildTag_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 5),
    _CwsSoftwareInstalledcomponentsBuildTag_Type()
)
cwsSoftwareInstalledcomponentsBuildTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsBuildTag.setStatus("current")
_CwsSoftwareInstalledcomponentsBuildTimestamp_Type = StringMaxl32
_CwsSoftwareInstalledcomponentsBuildTimestamp_Object = MibTableColumn
cwsSoftwareInstalledcomponentsBuildTimestamp = _CwsSoftwareInstalledcomponentsBuildTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 6),
    _CwsSoftwareInstalledcomponentsBuildTimestamp_Type()
)
cwsSoftwareInstalledcomponentsBuildTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsBuildTimestamp.setStatus("current")
_CwsSoftwareInstalledcomponentsBuildSize_Type = Unsigned32
_CwsSoftwareInstalledcomponentsBuildSize_Object = MibTableColumn
cwsSoftwareInstalledcomponentsBuildSize = _CwsSoftwareInstalledcomponentsBuildSize_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 11, 1, 7),
    _CwsSoftwareInstalledcomponentsBuildSize_Type()
)
cwsSoftwareInstalledcomponentsBuildSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsSoftwareInstalledcomponentsBuildSize.setStatus("current")

# Managed Objects groups

cienaWsSoftwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 1, 1)
)
cienaWsSoftwareGroup.setObjects(
      *(("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusSoftwareOperationalState"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusUpgradeOperationalState"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusCommittedVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusActiveVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusUpgradeToVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareStatusLastOperation"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportActiveReleaseVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServerReleaseVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportLocalReleaseVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServerHostname"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServerPath"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportTimestamp"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportCheckOperationalState"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportCheckUpgradeState"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportRequiredActivationType"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareCheckStatusReportServiceInterruptionActivation"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerIndex"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerServer"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerMode"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerRemotePath"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerLoginId"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeServerPassword"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeLogListDateAndTime"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareUpgradeLogListText"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareBuildNumber"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareBuildDate"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareCatalogName"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActiveSoftwareNumberOfComponents"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsName"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsBuildNumber"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareActivecomponentsStatus"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListName"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListDate"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListState"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareBootPartitionListIntegrityCheck"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsBuildNumber"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsBuildTag"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsBuildDate"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsSize"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareVersionsNumberOfComponents"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsName"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsVersion"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildNumber"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildTag"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildTimestamp"),
        ("CIENA-WS-SOFTWARE-MIB", "cwsSoftwareInstalledcomponentsBuildSize"))
)
if mibBuilder.loadTexts:
    cienaWsSoftwareGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsSoftwareCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cienaWsSoftwareCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-SOFTWARE-MIB",
    **{"SoftwareOpState": SoftwareOpState,
       "SoftwareRtncode": SoftwareRtncode,
       "UpgradeOpState": UpgradeOpState,
       "cienaWsSoftwareMIB": cienaWsSoftwareMIB,
       "cienaWsSoftwareObjects": cienaWsSoftwareObjects,
       "cienaWsSoftwareConformance": cienaWsSoftwareConformance,
       "cienaWsSoftwareGroups": cienaWsSoftwareGroups,
       "cienaWsSoftwareGroup": cienaWsSoftwareGroup,
       "cienaWsSoftwareCompliances": cienaWsSoftwareCompliances,
       "cienaWsSoftwareCompliance": cienaWsSoftwareCompliance,
       "cwsSoftwareStatusTable": cwsSoftwareStatusTable,
       "cwsSoftwareStatusEntry": cwsSoftwareStatusEntry,
       "cwsSoftwareStatusTableSnmpKey": cwsSoftwareStatusTableSnmpKey,
       "cwsSoftwareStatusSoftwareOperationalState": cwsSoftwareStatusSoftwareOperationalState,
       "cwsSoftwareStatusUpgradeOperationalState": cwsSoftwareStatusUpgradeOperationalState,
       "cwsSoftwareStatusCommittedVersion": cwsSoftwareStatusCommittedVersion,
       "cwsSoftwareStatusActiveVersion": cwsSoftwareStatusActiveVersion,
       "cwsSoftwareStatusUpgradeToVersion": cwsSoftwareStatusUpgradeToVersion,
       "cwsSoftwareStatusLastOperation": cwsSoftwareStatusLastOperation,
       "cwsSoftwareCheckStatusReportTable": cwsSoftwareCheckStatusReportTable,
       "cwsSoftwareCheckStatusReportEntry": cwsSoftwareCheckStatusReportEntry,
       "cwsSoftwareCheckStatusReportTableSnmpKey": cwsSoftwareCheckStatusReportTableSnmpKey,
       "cwsSoftwareCheckStatusReportActiveReleaseVersion": cwsSoftwareCheckStatusReportActiveReleaseVersion,
       "cwsSoftwareCheckStatusReportServerReleaseVersion": cwsSoftwareCheckStatusReportServerReleaseVersion,
       "cwsSoftwareCheckStatusReportLocalReleaseVersion": cwsSoftwareCheckStatusReportLocalReleaseVersion,
       "cwsSoftwareCheckStatusReportServerHostname": cwsSoftwareCheckStatusReportServerHostname,
       "cwsSoftwareCheckStatusReportServerPath": cwsSoftwareCheckStatusReportServerPath,
       "cwsSoftwareCheckStatusReportTimestamp": cwsSoftwareCheckStatusReportTimestamp,
       "cwsSoftwareCheckStatusReportCheckOperationalState": cwsSoftwareCheckStatusReportCheckOperationalState,
       "cwsSoftwareCheckStatusReportCheckUpgradeState": cwsSoftwareCheckStatusReportCheckUpgradeState,
       "cwsSoftwareCheckStatusReportRequiredActivationType": cwsSoftwareCheckStatusReportRequiredActivationType,
       "cwsSoftwareCheckStatusReportServiceInterruptionActivation": cwsSoftwareCheckStatusReportServiceInterruptionActivation,
       "cwsSoftwareUpgradeServerTable": cwsSoftwareUpgradeServerTable,
       "cwsSoftwareUpgradeServerEntry": cwsSoftwareUpgradeServerEntry,
       "cwsSoftwareUpgradeServerTableSnmpKey": cwsSoftwareUpgradeServerTableSnmpKey,
       "cwsSoftwareUpgradeServerIndex": cwsSoftwareUpgradeServerIndex,
       "cwsSoftwareUpgradeServerServer": cwsSoftwareUpgradeServerServer,
       "cwsSoftwareUpgradeServerMode": cwsSoftwareUpgradeServerMode,
       "cwsSoftwareUpgradeServerRemotePath": cwsSoftwareUpgradeServerRemotePath,
       "cwsSoftwareUpgradeServerLoginId": cwsSoftwareUpgradeServerLoginId,
       "cwsSoftwareUpgradeServerPassword": cwsSoftwareUpgradeServerPassword,
       "cwsSoftwareUpgradeLogListTable": cwsSoftwareUpgradeLogListTable,
       "cwsSoftwareUpgradeLogListEntry": cwsSoftwareUpgradeLogListEntry,
       "cwsSoftwareUpgradeLogListLogIndex": cwsSoftwareUpgradeLogListLogIndex,
       "cwsSoftwareUpgradeLogListDateAndTime": cwsSoftwareUpgradeLogListDateAndTime,
       "cwsSoftwareUpgradeLogListText": cwsSoftwareUpgradeLogListText,
       "cwsSoftwareActiveSoftwareTable": cwsSoftwareActiveSoftwareTable,
       "cwsSoftwareActiveSoftwareEntry": cwsSoftwareActiveSoftwareEntry,
       "cwsSoftwareActiveSoftwareTableSnmpKey": cwsSoftwareActiveSoftwareTableSnmpKey,
       "cwsSoftwareActiveSoftwareVersion": cwsSoftwareActiveSoftwareVersion,
       "cwsSoftwareActiveSoftwareBuildNumber": cwsSoftwareActiveSoftwareBuildNumber,
       "cwsSoftwareActiveSoftwareBuildDate": cwsSoftwareActiveSoftwareBuildDate,
       "cwsSoftwareActiveSoftwareCatalogName": cwsSoftwareActiveSoftwareCatalogName,
       "cwsSoftwareActiveSoftwareNumberOfComponents": cwsSoftwareActiveSoftwareNumberOfComponents,
       "cwsSoftwareActivecomponentsTable": cwsSoftwareActivecomponentsTable,
       "cwsSoftwareActivecomponentsEntry": cwsSoftwareActivecomponentsEntry,
       "cwsSoftwareActivecomponentsComponentIndex": cwsSoftwareActivecomponentsComponentIndex,
       "cwsSoftwareActivecomponentsName": cwsSoftwareActivecomponentsName,
       "cwsSoftwareActivecomponentsVersion": cwsSoftwareActivecomponentsVersion,
       "cwsSoftwareActivecomponentsBuildNumber": cwsSoftwareActivecomponentsBuildNumber,
       "cwsSoftwareActivecomponentsStatus": cwsSoftwareActivecomponentsStatus,
       "cwsSoftwareBootPartitionListTable": cwsSoftwareBootPartitionListTable,
       "cwsSoftwareBootPartitionListEntry": cwsSoftwareBootPartitionListEntry,
       "cwsSoftwareBootPartitionListIndex": cwsSoftwareBootPartitionListIndex,
       "cwsSoftwareBootPartitionListName": cwsSoftwareBootPartitionListName,
       "cwsSoftwareBootPartitionListVersion": cwsSoftwareBootPartitionListVersion,
       "cwsSoftwareBootPartitionListDate": cwsSoftwareBootPartitionListDate,
       "cwsSoftwareBootPartitionListState": cwsSoftwareBootPartitionListState,
       "cwsSoftwareBootPartitionListIntegrityCheck": cwsSoftwareBootPartitionListIntegrityCheck,
       "cwsSoftwareVersionsTable": cwsSoftwareVersionsTable,
       "cwsSoftwareVersionsEntry": cwsSoftwareVersionsEntry,
       "cwsSoftwareVersionsIndex": cwsSoftwareVersionsIndex,
       "cwsSoftwareVersionsVersion": cwsSoftwareVersionsVersion,
       "cwsSoftwareVersionsBuildNumber": cwsSoftwareVersionsBuildNumber,
       "cwsSoftwareVersionsBuildTag": cwsSoftwareVersionsBuildTag,
       "cwsSoftwareVersionsBuildDate": cwsSoftwareVersionsBuildDate,
       "cwsSoftwareVersionsSize": cwsSoftwareVersionsSize,
       "cwsSoftwareVersionsNumberOfComponents": cwsSoftwareVersionsNumberOfComponents,
       "cwsSoftwareInstalledcomponentsTable": cwsSoftwareInstalledcomponentsTable,
       "cwsSoftwareInstalledcomponentsEntry": cwsSoftwareInstalledcomponentsEntry,
       "cwsSoftwareInstalledcomponentsComponentIndex": cwsSoftwareInstalledcomponentsComponentIndex,
       "cwsSoftwareInstalledcomponentsName": cwsSoftwareInstalledcomponentsName,
       "cwsSoftwareInstalledcomponentsVersion": cwsSoftwareInstalledcomponentsVersion,
       "cwsSoftwareInstalledcomponentsBuildNumber": cwsSoftwareInstalledcomponentsBuildNumber,
       "cwsSoftwareInstalledcomponentsBuildTag": cwsSoftwareInstalledcomponentsBuildTag,
       "cwsSoftwareInstalledcomponentsBuildTimestamp": cwsSoftwareInstalledcomponentsBuildTimestamp,
       "cwsSoftwareInstalledcomponentsBuildSize": cwsSoftwareInstalledcomponentsBuildSize}
)
