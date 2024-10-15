# SNMP MIB module (CISCOSB-rndApplications) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-rndApplications
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:20 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

rndApplications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35)
)
rndApplications.setRevisions(
        ("2004-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PingCompletionStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bad-reply-data", 9),
          ("host-unreachable", 4),
          ("incomplete", 10),
          ("net-unreachable", 3),
          ("ok", 1),
          ("protocol-unreachable", 5),
          ("reassembly-time-exceeded", 7),
          ("time-to-live-exceeded", 6),
          ("timeout", 2),
          ("unable-to-send", 8))
    )



# MIB Managed Objects in the order of their OIDs

_RndMidLevelManagement_ObjectIdentity = ObjectIdentity
rndMidLevelManagement = _RndMidLevelManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2)
)
_RndAlarmOptions_ObjectIdentity = ObjectIdentity
rndAlarmOptions = _RndAlarmOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 2)
)


class _RndAlarmEnabling_Type(Integer32):
    """Custom type rndAlarmEnabling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RndAlarmEnabling_Type.__name__ = "Integer32"
_RndAlarmEnabling_Object = MibScalar
rndAlarmEnabling = _RndAlarmEnabling_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 2, 1),
    _RndAlarmEnabling_Type()
)
rndAlarmEnabling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmEnabling.setStatus("current")
_RndAlarmInterval_Type = Integer32
_RndAlarmInterval_Object = MibScalar
rndAlarmInterval = _RndAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 2, 2),
    _RndAlarmInterval_Type()
)
rndAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmInterval.setStatus("current")
_RndMonitoredElementsTable_Object = MibTable
rndMonitoredElementsTable = _RndMonitoredElementsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3)
)
if mibBuilder.loadTexts:
    rndMonitoredElementsTable.setStatus("current")
_RndMonitoredElementEntry_Object = MibTableRow
rndMonitoredElementEntry = _RndMonitoredElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3, 1)
)
rndMonitoredElementEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rndMonitoredElementAddress"),
)
if mibBuilder.loadTexts:
    rndMonitoredElementEntry.setStatus("current")
_RndMonitoredElementAddress_Type = IpAddress
_RndMonitoredElementAddress_Object = MibTableColumn
rndMonitoredElementAddress = _RndMonitoredElementAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3, 1, 1),
    _RndMonitoredElementAddress_Type()
)
rndMonitoredElementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredElementAddress.setStatus("current")


class _RndMonitoredElementCommunity_Type(DisplayString):
    """Custom type rndMonitoredElementCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElementCommunity_Type.__name__ = "DisplayString"
_RndMonitoredElementCommunity_Object = MibTableColumn
rndMonitoredElementCommunity = _RndMonitoredElementCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3, 1, 2),
    _RndMonitoredElementCommunity_Type()
)
rndMonitoredElementCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementCommunity.setStatus("current")


class _RndMonitoredElementLabel_Type(DisplayString):
    """Custom type rndMonitoredElementLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElementLabel_Type.__name__ = "DisplayString"
_RndMonitoredElementLabel_Object = MibTableColumn
rndMonitoredElementLabel = _RndMonitoredElementLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3, 1, 3),
    _RndMonitoredElementLabel_Type()
)
rndMonitoredElementLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementLabel.setStatus("current")
_RndDefaultPollingInterval_Type = Integer32
_RndDefaultPollingInterval_Object = MibTableColumn
rndDefaultPollingInterval = _RndDefaultPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3, 1, 4),
    _RndDefaultPollingInterval_Type()
)
rndDefaultPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDefaultPollingInterval.setStatus("current")
_RndDefaultLogFile_Type = DisplayString
_RndDefaultLogFile_Object = MibTableColumn
rndDefaultLogFile = _RndDefaultLogFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3, 1, 5),
    _RndDefaultLogFile_Type()
)
rndDefaultLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDefaultLogFile.setStatus("current")
_RndMonitoredElementStatus_Type = RowStatus
_RndMonitoredElementStatus_Object = MibTableColumn
rndMonitoredElementStatus = _RndMonitoredElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 3, 1, 6),
    _RndMonitoredElementStatus_Type()
)
rndMonitoredElementStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredElementStatus.setStatus("current")
_RndMonitoringTable_Object = MibTable
rndMonitoringTable = _RndMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4)
)
if mibBuilder.loadTexts:
    rndMonitoringTable.setStatus("current")
_RndMonitoringEntry_Object = MibTableRow
rndMonitoringEntry = _RndMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1)
)
rndMonitoringEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rndMonitoredElement"),
    (1, "CISCOSB-rndApplications", "rndMonitoredObjectInstanceLabel"),
)
if mibBuilder.loadTexts:
    rndMonitoringEntry.setStatus("current")


class _RndMonitoredElement_Type(DisplayString):
    """Custom type rndMonitoredElement based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredElement_Type.__name__ = "DisplayString"
_RndMonitoredElement_Object = MibTableColumn
rndMonitoredElement = _RndMonitoredElement_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 1),
    _RndMonitoredElement_Type()
)
rndMonitoredElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredElement.setStatus("current")


class _RndMonitoredObjectInstanceLabel_Type(DisplayString):
    """Custom type rndMonitoredObjectInstanceLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndMonitoredObjectInstanceLabel_Type.__name__ = "DisplayString"
_RndMonitoredObjectInstanceLabel_Object = MibTableColumn
rndMonitoredObjectInstanceLabel = _RndMonitoredObjectInstanceLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 2),
    _RndMonitoredObjectInstanceLabel_Type()
)
rndMonitoredObjectInstanceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMonitoredObjectInstanceLabel.setStatus("current")


class _RndMonitoredObjectName_Type(DisplayString):
    """Custom type rndMonitoredObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RndMonitoredObjectName_Type.__name__ = "DisplayString"
_RndMonitoredObjectName_Object = MibTableColumn
rndMonitoredObjectName = _RndMonitoredObjectName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 3),
    _RndMonitoredObjectName_Type()
)
rndMonitoredObjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectName.setStatus("current")
_RndMonitoredObjectIdentifier_Type = ObjectIdentifier
_RndMonitoredObjectIdentifier_Object = MibTableColumn
rndMonitoredObjectIdentifier = _RndMonitoredObjectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 4),
    _RndMonitoredObjectIdentifier_Type()
)
rndMonitoredObjectIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectIdentifier.setStatus("current")
_RndMonitoredObjectInstance_Type = ObjectIdentifier
_RndMonitoredObjectInstance_Object = MibTableColumn
rndMonitoredObjectInstance = _RndMonitoredObjectInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 5),
    _RndMonitoredObjectInstance_Type()
)
rndMonitoredObjectInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectInstance.setStatus("current")


class _RndMonitoredObjectSyntax_Type(Integer32):
    """Custom type rndMonitoredObjectSyntax based on Integer32"""
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
        *(("integer", 1),
          ("ip-address", 3),
          ("object-identifier", 4),
          ("octet-string", 2))
    )


_RndMonitoredObjectSyntax_Type.__name__ = "Integer32"
_RndMonitoredObjectSyntax_Object = MibTableColumn
rndMonitoredObjectSyntax = _RndMonitoredObjectSyntax_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 6),
    _RndMonitoredObjectSyntax_Type()
)
rndMonitoredObjectSyntax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredObjectSyntax.setStatus("current")
_RndMonitoringInterval_Type = Integer32
_RndMonitoringInterval_Object = MibTableColumn
rndMonitoringInterval = _RndMonitoringInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 7),
    _RndMonitoringInterval_Type()
)
rndMonitoringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringInterval.setStatus("current")
_RndAlarmMaxTreshold_Type = Integer32
_RndAlarmMaxTreshold_Object = MibTableColumn
rndAlarmMaxTreshold = _RndAlarmMaxTreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 8),
    _RndAlarmMaxTreshold_Type()
)
rndAlarmMaxTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmMaxTreshold.setStatus("current")
_RndAlarmMinTreshold_Type = Integer32
_RndAlarmMinTreshold_Object = MibTableColumn
rndAlarmMinTreshold = _RndAlarmMinTreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 9),
    _RndAlarmMinTreshold_Type()
)
rndAlarmMinTreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndAlarmMinTreshold.setStatus("current")
_RndMonitoringLogfile_Type = DisplayString
_RndMonitoringLogfile_Object = MibTableColumn
rndMonitoringLogfile = _RndMonitoringLogfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 10),
    _RndMonitoringLogfile_Type()
)
rndMonitoringLogfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringLogfile.setStatus("current")
_RndMonitoringEntryStatus_Type = RowStatus
_RndMonitoringEntryStatus_Object = MibTableColumn
rndMonitoringEntryStatus = _RndMonitoringEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 11),
    _RndMonitoringEntryStatus_Type()
)
rndMonitoringEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoringEntryStatus.setStatus("current")
_RndMonitoredIntegerInstance_Type = Integer32
_RndMonitoredIntegerInstance_Object = MibTableColumn
rndMonitoredIntegerInstance = _RndMonitoredIntegerInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 4, 1, 12),
    _RndMonitoredIntegerInstance_Type()
)
rndMonitoredIntegerInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMonitoredIntegerInstance.setStatus("current")
_RndMibFilesTable_Object = MibTable
rndMibFilesTable = _RndMibFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 5)
)
if mibBuilder.loadTexts:
    rndMibFilesTable.setStatus("current")
_RndMibFileEntry_Object = MibTableRow
rndMibFileEntry = _RndMibFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 5, 1)
)
rndMibFileEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rndMibFileIndex"),
)
if mibBuilder.loadTexts:
    rndMibFileEntry.setStatus("current")
_RndMibFileIndex_Type = Integer32
_RndMibFileIndex_Object = MibTableColumn
rndMibFileIndex = _RndMibFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 5, 1, 1),
    _RndMibFileIndex_Type()
)
rndMibFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndMibFileIndex.setStatus("current")
_RndMibFilePath_Type = DisplayString
_RndMibFilePath_Object = MibTableColumn
rndMibFilePath = _RndMibFilePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 5, 1, 2),
    _RndMibFilePath_Type()
)
rndMibFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFilePath.setStatus("current")


class _RndMibFileRefresh_Type(Integer32):
    """Custom type rndMibFileRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_RndMibFileRefresh_Type.__name__ = "Integer32"
_RndMibFileRefresh_Object = MibTableColumn
rndMibFileRefresh = _RndMibFileRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 5, 1, 3),
    _RndMibFileRefresh_Type()
)
rndMibFileRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFileRefresh.setStatus("current")
_RndMibFileEntryStatus_Type = RowStatus
_RndMibFileEntryStatus_Object = MibTableColumn
rndMibFileEntryStatus = _RndMibFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 5, 1, 4),
    _RndMibFileEntryStatus_Type()
)
rndMibFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndMibFileEntryStatus.setStatus("current")
_RndHardwareConfiguration_Type = TruthValue
_RndHardwareConfiguration_Object = MibScalar
rndHardwareConfiguration = _RndHardwareConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 6),
    _RndHardwareConfiguration_Type()
)
rndHardwareConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndHardwareConfiguration.setStatus("current")


class _RndEraseSimulatedConfiguration_Type(Integer32):
    """Custom type rndEraseSimulatedConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eraseSimulatedConfiguration", 1),
          ("simulatedConfigurationErased", 3),
          ("simulatedConfigurationPresent", 2))
    )


_RndEraseSimulatedConfiguration_Type.__name__ = "Integer32"
_RndEraseSimulatedConfiguration_Object = MibScalar
rndEraseSimulatedConfiguration = _RndEraseSimulatedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 7),
    _RndEraseSimulatedConfiguration_Type()
)
rndEraseSimulatedConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndEraseSimulatedConfiguration.setStatus("current")
_RndDeleteValuesTable_Object = MibTable
rndDeleteValuesTable = _RndDeleteValuesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 8)
)
if mibBuilder.loadTexts:
    rndDeleteValuesTable.setStatus("current")
_RndDeleteValuesEntry_Object = MibTableRow
rndDeleteValuesEntry = _RndDeleteValuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 8, 1)
)
rndDeleteValuesEntry.setIndexNames(
    (1, "CISCOSB-rndApplications", "rndRowStatusVariableName"),
)
if mibBuilder.loadTexts:
    rndDeleteValuesEntry.setStatus("current")


class _RndRowStatusVariableName_Type(DisplayString):
    """Custom type rndRowStatusVariableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RndRowStatusVariableName_Type.__name__ = "DisplayString"
_RndRowStatusVariableName_Object = MibTableColumn
rndRowStatusVariableName = _RndRowStatusVariableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 8, 1, 1),
    _RndRowStatusVariableName_Type()
)
rndRowStatusVariableName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowStatusVariableName.setStatus("current")
_RndRowStatusObjectId_Type = ObjectIdentifier
_RndRowStatusObjectId_Object = MibTableColumn
rndRowStatusObjectId = _RndRowStatusObjectId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 8, 1, 2),
    _RndRowStatusObjectId_Type()
)
rndRowStatusObjectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowStatusObjectId.setStatus("current")
_RndRowDeleteValue_Type = Integer32
_RndRowDeleteValue_Object = MibTableColumn
rndRowDeleteValue = _RndRowDeleteValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 8, 1, 3),
    _RndRowDeleteValue_Type()
)
rndRowDeleteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndRowDeleteValue.setStatus("current")
_RndDeleteValueEntryStatus_Type = RowStatus
_RndDeleteValueEntryStatus_Object = MibTableColumn
rndDeleteValueEntryStatus = _RndDeleteValueEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 8, 1, 4),
    _RndDeleteValueEntryStatus_Type()
)
rndDeleteValueEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndDeleteValueEntryStatus.setStatus("current")
_SnmpTesting_ObjectIdentity = ObjectIdentity
snmpTesting = _SnmpTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9)
)
_RndSimulatedVariablesTable_Object = MibTable
rndSimulatedVariablesTable = _RndSimulatedVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 1)
)
if mibBuilder.loadTexts:
    rndSimulatedVariablesTable.setStatus("current")
_RndSimulatedVariablesEntry_Object = MibTableRow
rndSimulatedVariablesEntry = _RndSimulatedVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 1, 1)
)
rndSimulatedVariablesEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rndSimulatedVariableEntryIndex"),
)
if mibBuilder.loadTexts:
    rndSimulatedVariablesEntry.setStatus("current")
_RndSimulatedVariableEntryIndex_Type = Integer32
_RndSimulatedVariableEntryIndex_Object = MibTableColumn
rndSimulatedVariableEntryIndex = _RndSimulatedVariableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 1, 1, 1),
    _RndSimulatedVariableEntryIndex_Type()
)
rndSimulatedVariableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndSimulatedVariableEntryIndex.setStatus("current")
_RndSimulatedVariableObjectId_Type = ObjectIdentifier
_RndSimulatedVariableObjectId_Object = MibTableColumn
rndSimulatedVariableObjectId = _RndSimulatedVariableObjectId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 1, 1, 2),
    _RndSimulatedVariableObjectId_Type()
)
rndSimulatedVariableObjectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndSimulatedVariableObjectId.setStatus("current")
_RndNotSupportedField_Type = Integer32
_RndNotSupportedField_Object = MibTableColumn
rndNotSupportedField = _RndNotSupportedField_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 1, 1, 3),
    _RndNotSupportedField_Type()
)
rndNotSupportedField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndNotSupportedField.setStatus("current")
_RndSimulatedVariableEntryStatus_Type = RowStatus
_RndSimulatedVariableEntryStatus_Object = MibTableColumn
rndSimulatedVariableEntryStatus = _RndSimulatedVariableEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 1, 1, 4),
    _RndSimulatedVariableEntryStatus_Type()
)
rndSimulatedVariableEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndSimulatedVariableEntryStatus.setStatus("current")
_RndSnmpTestPassword_Type = Integer32
_RndSnmpTestPassword_Object = MibScalar
rndSnmpTestPassword = _RndSnmpTestPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 2),
    _RndSnmpTestPassword_Type()
)
rndSnmpTestPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndSnmpTestPassword.setStatus("current")


class _RndSnmpTests_Type(Integer32):
    """Custom type rndSnmpTests based on Integer32"""
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
        *(("noSimulation", 1),
          ("simulateAppGet", 3),
          ("simulateAppGetNext", 4),
          ("simulateSetFailure", 2))
    )


_RndSnmpTests_Type.__name__ = "Integer32"
_RndSnmpTests_Object = MibScalar
rndSnmpTests = _RndSnmpTests_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 3),
    _RndSnmpTests_Type()
)
rndSnmpTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndSnmpTests.setStatus("current")
_RndSimulateUndo_Type = Integer32
_RndSimulateUndo_Object = MibScalar
rndSimulateUndo = _RndSimulateUndo_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 4),
    _RndSimulateUndo_Type()
)
rndSimulateUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndSimulateUndo.setStatus("current")
_RlSnmpServTestRequest_Type = Integer32
_RlSnmpServTestRequest_Object = MibScalar
rlSnmpServTestRequest = _RlSnmpServTestRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 5),
    _RlSnmpServTestRequest_Type()
)
rlSnmpServTestRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnmpServTestRequest.setStatus("current")
_RlSnmpServTestResponse_Type = OctetString
_RlSnmpServTestResponse_Object = MibScalar
rlSnmpServTestResponse = _RlSnmpServTestResponse_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 6),
    _RlSnmpServTestResponse_Type()
)
rlSnmpServTestResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpServTestResponse.setStatus("current")


class _RlSnmpServCreateTestPool_Type(Integer32):
    """Custom type rlSnmpServCreateTestPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("no-create", 2))
    )


_RlSnmpServCreateTestPool_Type.__name__ = "Integer32"
_RlSnmpServCreateTestPool_Object = MibScalar
rlSnmpServCreateTestPool = _RlSnmpServCreateTestPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 7),
    _RlSnmpServCreateTestPool_Type()
)
rlSnmpServCreateTestPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnmpServCreateTestPool.setStatus("current")
_RlSnmpServITCbindClients_Type = ObjectIdentifier
_RlSnmpServITCbindClients_Object = MibScalar
rlSnmpServITCbindClients = _RlSnmpServITCbindClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 8),
    _RlSnmpServITCbindClients_Type()
)
rlSnmpServITCbindClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlSnmpServITCbindClients.setStatus("current")
_RlSnmpTestSimulatedVariables_ObjectIdentity = ObjectIdentity
rlSnmpTestSimulatedVariables = _RlSnmpTestSimulatedVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 9)
)
_RlTstBasicRateTable_Object = MibTable
rlTstBasicRateTable = _RlTstBasicRateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 10)
)
if mibBuilder.loadTexts:
    rlTstBasicRateTable.setStatus("current")
_RlTstBasicRateEntry_Object = MibTableRow
rlTstBasicRateEntry = _RlTstBasicRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 10, 1)
)
rlTstBasicRateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlTstBasicRateEntry.setStatus("current")


class _RlTstBasicRateIfType_Type(Integer32):
    """Custom type rlTstBasicRateIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("isdns", 75),
          ("isdnu", 76))
    )


_RlTstBasicRateIfType_Type.__name__ = "Integer32"
_RlTstBasicRateIfType_Object = MibTableColumn
rlTstBasicRateIfType = _RlTstBasicRateIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 10, 1, 1),
    _RlTstBasicRateIfType_Type()
)
rlTstBasicRateIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTstBasicRateIfType.setStatus("current")


class _RlTstBasicRateLineTopology_Type(Integer32):
    """Custom type rlTstBasicRateLineTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToMultipoint", 2),
          ("pointToPoint", 1))
    )


_RlTstBasicRateLineTopology_Type.__name__ = "Integer32"
_RlTstBasicRateLineTopology_Object = MibTableColumn
rlTstBasicRateLineTopology = _RlTstBasicRateLineTopology_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 10, 1, 2),
    _RlTstBasicRateLineTopology_Type()
)
rlTstBasicRateLineTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTstBasicRateLineTopology.setStatus("current")


class _RlTstBasicRateIfMode_Type(Integer32):
    """Custom type rlTstBasicRateIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nt", 2),
          ("te", 1))
    )


_RlTstBasicRateIfMode_Type.__name__ = "Integer32"
_RlTstBasicRateIfMode_Object = MibTableColumn
rlTstBasicRateIfMode = _RlTstBasicRateIfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 10, 1, 3),
    _RlTstBasicRateIfMode_Type()
)
rlTstBasicRateIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTstBasicRateIfMode.setStatus("current")


class _RlTstBasicRateSignalMode_Type(Integer32):
    """Custom type rlTstBasicRateSignalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RlTstBasicRateSignalMode_Type.__name__ = "Integer32"
_RlTstBasicRateSignalMode_Object = MibTableColumn
rlTstBasicRateSignalMode = _RlTstBasicRateSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 9, 10, 1, 4),
    _RlTstBasicRateSignalMode_Type()
)
rlTstBasicRateSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTstBasicRateSignalMode.setStatus("current")
_RlMibTree_ObjectIdentity = ObjectIdentity
rlMibTree = _RlMibTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10)
)
_RlMibTreeTable_Object = MibTable
rlMibTreeTable = _RlMibTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10, 1)
)
if mibBuilder.loadTexts:
    rlMibTreeTable.setStatus("current")
_RlMibTreeEntry_Object = MibTableRow
rlMibTreeEntry = _RlMibTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10, 1, 1)
)
rlMibTreeEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rlMibTreeFather"),
    (0, "CISCOSB-rndApplications", "rlMibTreeSonIndex"),
)
if mibBuilder.loadTexts:
    rlMibTreeEntry.setStatus("current")
_RlMibTreeFather_Type = DisplayString
_RlMibTreeFather_Object = MibTableColumn
rlMibTreeFather = _RlMibTreeFather_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10, 1, 1, 1),
    _RlMibTreeFather_Type()
)
rlMibTreeFather.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlMibTreeFather.setStatus("current")
_RlMibTreeSonIndex_Type = Integer32
_RlMibTreeSonIndex_Object = MibTableColumn
rlMibTreeSonIndex = _RlMibTreeSonIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10, 1, 1, 2),
    _RlMibTreeSonIndex_Type()
)
rlMibTreeSonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlMibTreeSonIndex.setStatus("current")
_RlMibTreeSon_Type = DisplayString
_RlMibTreeSon_Object = MibTableColumn
rlMibTreeSon = _RlMibTreeSon_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10, 1, 1, 3),
    _RlMibTreeSon_Type()
)
rlMibTreeSon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMibTreeSon.setStatus("current")
_RlMibTreeSonObjectId_Type = ObjectIdentifier
_RlMibTreeSonObjectId_Object = MibTableColumn
rlMibTreeSonObjectId = _RlMibTreeSonObjectId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10, 1, 1, 4),
    _RlMibTreeSonObjectId_Type()
)
rlMibTreeSonObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMibTreeSonObjectId.setStatus("current")
_RlMibTreeGrandFather_Type = DisplayString
_RlMibTreeGrandFather_Object = MibTableColumn
rlMibTreeGrandFather = _RlMibTreeGrandFather_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 10, 1, 1, 5),
    _RlMibTreeGrandFather_Type()
)
rlMibTreeGrandFather.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMibTreeGrandFather.setStatus("current")
_RlMibInstances_ObjectIdentity = ObjectIdentity
rlMibInstances = _RlMibInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 11)
)
_RlMibTableInstancesInfoTable_Object = MibTable
rlMibTableInstancesInfoTable = _RlMibTableInstancesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 11, 1)
)
if mibBuilder.loadTexts:
    rlMibTableInstancesInfoTable.setStatus("current")
_RlMibTableInstancesInfoEntry_Object = MibTableRow
rlMibTableInstancesInfoEntry = _RlMibTableInstancesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 11, 1, 1)
)
rlMibTableInstancesInfoEntry.setIndexNames(
    (1, "CISCOSB-rndApplications", "rlMibTableInstancesInfoTableName"),
)
if mibBuilder.loadTexts:
    rlMibTableInstancesInfoEntry.setStatus("current")


class _RlMibTableInstancesInfoTableName_Type(DisplayString):
    """Custom type rlMibTableInstancesInfoTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 160),
    )


_RlMibTableInstancesInfoTableName_Type.__name__ = "DisplayString"
_RlMibTableInstancesInfoTableName_Object = MibTableColumn
rlMibTableInstancesInfoTableName = _RlMibTableInstancesInfoTableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 11, 1, 1, 1),
    _RlMibTableInstancesInfoTableName_Type()
)
rlMibTableInstancesInfoTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlMibTableInstancesInfoTableName.setStatus("current")
_RlMibTableInstancesInfoNumOfInstances_Type = Integer32
_RlMibTableInstancesInfoNumOfInstances_Object = MibTableColumn
rlMibTableInstancesInfoNumOfInstances = _RlMibTableInstancesInfoNumOfInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 2, 11, 1, 1, 2),
    _RlMibTableInstancesInfoNumOfInstances_Type()
)
rlMibTableInstancesInfoNumOfInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMibTableInstancesInfoNumOfInstances.setStatus("current")
_RsPingMIB_ObjectIdentity = ObjectIdentity
rsPingMIB = _RsPingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4)
)
_RsPingTable_Object = MibTable
rsPingTable = _RsPingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1)
)
if mibBuilder.loadTexts:
    rsPingTable.setStatus("current")
_RsPingEntry_Object = MibTableRow
rsPingEntry = _RsPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1)
)
rsPingEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rsPingAddress"),
)
if mibBuilder.loadTexts:
    rsPingEntry.setStatus("current")
_RsPingAddress_Type = IpAddress
_RsPingAddress_Object = MibTableColumn
rsPingAddress = _RsPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 1),
    _RsPingAddress_Type()
)
rsPingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingAddress.setStatus("current")


class _RsPingPacketCount_Type(Integer32):
    """Custom type rsPingPacketCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsPingPacketCount_Type.__name__ = "Integer32"
_RsPingPacketCount_Object = MibTableColumn
rsPingPacketCount = _RsPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 2),
    _RsPingPacketCount_Type()
)
rsPingPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingPacketCount.setStatus("current")
_RsPingPacketSize_Type = Integer32
_RsPingPacketSize_Object = MibTableColumn
rsPingPacketSize = _RsPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 3),
    _RsPingPacketSize_Type()
)
rsPingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingPacketSize.setStatus("current")


class _RsPingPacketTimeout_Type(Integer32):
    """Custom type rsPingPacketTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_RsPingPacketTimeout_Type.__name__ = "Integer32"
_RsPingPacketTimeout_Object = MibTableColumn
rsPingPacketTimeout = _RsPingPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 4),
    _RsPingPacketTimeout_Type()
)
rsPingPacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingPacketTimeout.setStatus("current")


class _RsPingDelay_Type(Integer32):
    """Custom type rsPingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_RsPingDelay_Type.__name__ = "Integer32"
_RsPingDelay_Object = MibTableColumn
rsPingDelay = _RsPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 5),
    _RsPingDelay_Type()
)
rsPingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingDelay.setStatus("current")
_RsPingTrapOnCompletion_Type = TruthValue
_RsPingTrapOnCompletion_Object = MibTableColumn
rsPingTrapOnCompletion = _RsPingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 6),
    _RsPingTrapOnCompletion_Type()
)
rsPingTrapOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingTrapOnCompletion.setStatus("current")
_RsPingSentPackets_Type = Counter32
_RsPingSentPackets_Object = MibTableColumn
rsPingSentPackets = _RsPingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 7),
    _RsPingSentPackets_Type()
)
rsPingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingSentPackets.setStatus("current")
_RsPingReceivedPackets_Type = Counter32
_RsPingReceivedPackets_Object = MibTableColumn
rsPingReceivedPackets = _RsPingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 8),
    _RsPingReceivedPackets_Type()
)
rsPingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingReceivedPackets.setStatus("current")
_RsPingMinReturnTime_Type = Integer32
_RsPingMinReturnTime_Object = MibTableColumn
rsPingMinReturnTime = _RsPingMinReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 9),
    _RsPingMinReturnTime_Type()
)
rsPingMinReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingMinReturnTime.setStatus("current")
_RsPingAvgReturnTime_Type = Integer32
_RsPingAvgReturnTime_Object = MibTableColumn
rsPingAvgReturnTime = _RsPingAvgReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 10),
    _RsPingAvgReturnTime_Type()
)
rsPingAvgReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingAvgReturnTime.setStatus("current")
_RsPingMaxReturnTime_Type = Integer32
_RsPingMaxReturnTime_Object = MibTableColumn
rsPingMaxReturnTime = _RsPingMaxReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 11),
    _RsPingMaxReturnTime_Type()
)
rsPingMaxReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingMaxReturnTime.setStatus("current")
_RsPingCompletionStatus_Type = PingCompletionStatus
_RsPingCompletionStatus_Object = MibTableColumn
rsPingCompletionStatus = _RsPingCompletionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 12),
    _RsPingCompletionStatus_Type()
)
rsPingCompletionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingCompletionStatus.setStatus("current")


class _RsPingTimeStamp_Type(DisplayString):
    """Custom type rsPingTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_RsPingTimeStamp_Type.__name__ = "DisplayString"
_RsPingTimeStamp_Object = MibTableColumn
rsPingTimeStamp = _RsPingTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 13),
    _RsPingTimeStamp_Type()
)
rsPingTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingTimeStamp.setStatus("current")
_RsPingEntryStatus_Type = RowStatus
_RsPingEntryStatus_Object = MibTableColumn
rsPingEntryStatus = _RsPingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 1, 1, 14),
    _RsPingEntryStatus_Type()
)
rsPingEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingEntryStatus.setStatus("current")
_RsPingInetTable_Object = MibTable
rsPingInetTable = _RsPingInetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2)
)
if mibBuilder.loadTexts:
    rsPingInetTable.setStatus("current")
_RsPingInetEntry_Object = MibTableRow
rsPingInetEntry = _RsPingInetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1)
)
rsPingInetEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rsPingInetAddressType"),
    (0, "CISCOSB-rndApplications", "rsPingInetAddress"),
)
if mibBuilder.loadTexts:
    rsPingInetEntry.setStatus("current")
_RsPingInetAddressType_Type = InetAddressType
_RsPingInetAddressType_Object = MibTableColumn
rsPingInetAddressType = _RsPingInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 1),
    _RsPingInetAddressType_Type()
)
rsPingInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetAddressType.setStatus("current")
_RsPingInetAddress_Type = InetAddress
_RsPingInetAddress_Object = MibTableColumn
rsPingInetAddress = _RsPingInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 2),
    _RsPingInetAddress_Type()
)
rsPingInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetAddress.setStatus("current")


class _RsPingInetPacketCount_Type(Integer32):
    """Custom type rsPingInetPacketCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RsPingInetPacketCount_Type.__name__ = "Integer32"
_RsPingInetPacketCount_Object = MibTableColumn
rsPingInetPacketCount = _RsPingInetPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 3),
    _RsPingInetPacketCount_Type()
)
rsPingInetPacketCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetPacketCount.setStatus("current")
_RsPingInetPacketSize_Type = Integer32
_RsPingInetPacketSize_Object = MibTableColumn
rsPingInetPacketSize = _RsPingInetPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 4),
    _RsPingInetPacketSize_Type()
)
rsPingInetPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetPacketSize.setStatus("current")


class _RsPingInetPacketTimeout_Type(Integer32):
    """Custom type rsPingInetPacketTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_RsPingInetPacketTimeout_Type.__name__ = "Integer32"
_RsPingInetPacketTimeout_Object = MibTableColumn
rsPingInetPacketTimeout = _RsPingInetPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 5),
    _RsPingInetPacketTimeout_Type()
)
rsPingInetPacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetPacketTimeout.setStatus("current")


class _RsPingInetDelay_Type(Integer32):
    """Custom type rsPingInetDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_RsPingInetDelay_Type.__name__ = "Integer32"
_RsPingInetDelay_Object = MibTableColumn
rsPingInetDelay = _RsPingInetDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 6),
    _RsPingInetDelay_Type()
)
rsPingInetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetDelay.setStatus("current")
_RsPingInetTrapOnCompletion_Type = TruthValue
_RsPingInetTrapOnCompletion_Object = MibTableColumn
rsPingInetTrapOnCompletion = _RsPingInetTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 7),
    _RsPingInetTrapOnCompletion_Type()
)
rsPingInetTrapOnCompletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetTrapOnCompletion.setStatus("current")
_RsPingInetSentPackets_Type = Counter32
_RsPingInetSentPackets_Object = MibTableColumn
rsPingInetSentPackets = _RsPingInetSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 8),
    _RsPingInetSentPackets_Type()
)
rsPingInetSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingInetSentPackets.setStatus("current")
_RsPingInetReceivedPackets_Type = Counter32
_RsPingInetReceivedPackets_Object = MibTableColumn
rsPingInetReceivedPackets = _RsPingInetReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 9),
    _RsPingInetReceivedPackets_Type()
)
rsPingInetReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingInetReceivedPackets.setStatus("current")
_RsPingInetMinReturnTime_Type = Integer32
_RsPingInetMinReturnTime_Object = MibTableColumn
rsPingInetMinReturnTime = _RsPingInetMinReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 10),
    _RsPingInetMinReturnTime_Type()
)
rsPingInetMinReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingInetMinReturnTime.setStatus("current")
_RsPingInetAvgReturnTime_Type = Integer32
_RsPingInetAvgReturnTime_Object = MibTableColumn
rsPingInetAvgReturnTime = _RsPingInetAvgReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 11),
    _RsPingInetAvgReturnTime_Type()
)
rsPingInetAvgReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingInetAvgReturnTime.setStatus("current")
_RsPingInetMaxReturnTime_Type = Integer32
_RsPingInetMaxReturnTime_Object = MibTableColumn
rsPingInetMaxReturnTime = _RsPingInetMaxReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 12),
    _RsPingInetMaxReturnTime_Type()
)
rsPingInetMaxReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingInetMaxReturnTime.setStatus("current")
_RsPingInetCompletionStatus_Type = PingCompletionStatus
_RsPingInetCompletionStatus_Object = MibTableColumn
rsPingInetCompletionStatus = _RsPingInetCompletionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 13),
    _RsPingInetCompletionStatus_Type()
)
rsPingInetCompletionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingInetCompletionStatus.setStatus("current")


class _RsPingInetTimeStamp_Type(DisplayString):
    """Custom type rsPingInetTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_RsPingInetTimeStamp_Type.__name__ = "DisplayString"
_RsPingInetTimeStamp_Object = MibTableColumn
rsPingInetTimeStamp = _RsPingInetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 14),
    _RsPingInetTimeStamp_Type()
)
rsPingInetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPingInetTimeStamp.setStatus("current")
_RsPingInetEntryStatus_Type = RowStatus
_RsPingInetEntryStatus_Object = MibTableColumn
rsPingInetEntryStatus = _RsPingInetEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 15),
    _RsPingInetEntryStatus_Type()
)
rsPingInetEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetEntryStatus.setStatus("current")
_RsPingInetSourceAddr_Type = InetAddress
_RsPingInetSourceAddr_Object = MibTableColumn
rsPingInetSourceAddr = _RsPingInetSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 4, 2, 1, 16),
    _RsPingInetSourceAddr_Type()
)
rsPingInetSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPingInetSourceAddr.setStatus("current")
_RsPowerSupplyRedundacy_ObjectIdentity = ObjectIdentity
rsPowerSupplyRedundacy = _RsPowerSupplyRedundacy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 5)
)
_RsPowerSupplyRedundacyTable_Object = MibTable
rsPowerSupplyRedundacyTable = _RsPowerSupplyRedundacyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 5, 1)
)
if mibBuilder.loadTexts:
    rsPowerSupplyRedundacyTable.setStatus("current")
_RsPowerSupplyRedundacyEntry_Object = MibTableRow
rsPowerSupplyRedundacyEntry = _RsPowerSupplyRedundacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 5, 1, 1)
)
rsPowerSupplyRedundacyEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rsPowerSupplyRedundacyReNumber"),
)
if mibBuilder.loadTexts:
    rsPowerSupplyRedundacyEntry.setStatus("current")


class _RsPowerSupplyRedundacyReNumber_Type(Integer32):
    """Custom type rsPowerSupplyRedundacyReNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_RsPowerSupplyRedundacyReNumber_Type.__name__ = "Integer32"
_RsPowerSupplyRedundacyReNumber_Object = MibTableColumn
rsPowerSupplyRedundacyReNumber = _RsPowerSupplyRedundacyReNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 5, 1, 1, 1),
    _RsPowerSupplyRedundacyReNumber_Type()
)
rsPowerSupplyRedundacyReNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPowerSupplyRedundacyReNumber.setStatus("current")


class _RsPowerSupplyRedundacyStatus_Type(Integer32):
    """Custom type rsPowerSupplyRedundacyStatus based on Integer32"""
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
        *(("bothWorking", 3),
          ("existButNotWorking", 2),
          ("externalOnlyWorking", 5),
          ("internalOnlyWorking", 4),
          ("notExist", 1))
    )


_RsPowerSupplyRedundacyStatus_Type.__name__ = "Integer32"
_RsPowerSupplyRedundacyStatus_Object = MibTableColumn
rsPowerSupplyRedundacyStatus = _RsPowerSupplyRedundacyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 5, 1, 1, 2),
    _RsPowerSupplyRedundacyStatus_Type()
)
rsPowerSupplyRedundacyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPowerSupplyRedundacyStatus.setStatus("current")
_RsNvram_ObjectIdentity = ObjectIdentity
rsNvram = _RsNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 6)
)


class _RsEraseNvramAfterReset_Type(DisplayString):
    """Custom type rsEraseNvramAfterReset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsEraseNvramAfterReset_Type.__name__ = "DisplayString"
_RsEraseNvramAfterReset_Object = MibScalar
rsEraseNvramAfterReset = _RsEraseNvramAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 6, 1),
    _RsEraseNvramAfterReset_Type()
)
rsEraseNvramAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsEraseNvramAfterReset.setStatus("current")
_RsNvramApplTable_Object = MibTable
rsNvramApplTable = _RsNvramApplTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 6, 2)
)
if mibBuilder.loadTexts:
    rsNvramApplTable.setStatus("current")
_RsNvramApplEntry_Object = MibTableRow
rsNvramApplEntry = _RsNvramApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 6, 2, 1)
)
rsNvramApplEntry.setIndexNames(
    (0, "CISCOSB-rndApplications", "rsNvramApplIndex"),
)
if mibBuilder.loadTexts:
    rsNvramApplEntry.setStatus("current")
_RsNvramApplIndex_Type = Integer32
_RsNvramApplIndex_Object = MibTableColumn
rsNvramApplIndex = _RsNvramApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 6, 2, 1, 1),
    _RsNvramApplIndex_Type()
)
rsNvramApplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNvramApplIndex.setStatus("current")


class _RsNvramApplName_Type(DisplayString):
    """Custom type rsNvramApplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsNvramApplName_Type.__name__ = "DisplayString"
_RsNvramApplName_Object = MibTableColumn
rsNvramApplName = _RsNvramApplName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 35, 6, 2, 1, 2),
    _RsNvramApplName_Type()
)
rsNvramApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNvramApplName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-rndApplications",
    **{"PingCompletionStatus": PingCompletionStatus,
       "rndApplications": rndApplications,
       "rndMidLevelManagement": rndMidLevelManagement,
       "rndAlarmOptions": rndAlarmOptions,
       "rndAlarmEnabling": rndAlarmEnabling,
       "rndAlarmInterval": rndAlarmInterval,
       "rndMonitoredElementsTable": rndMonitoredElementsTable,
       "rndMonitoredElementEntry": rndMonitoredElementEntry,
       "rndMonitoredElementAddress": rndMonitoredElementAddress,
       "rndMonitoredElementCommunity": rndMonitoredElementCommunity,
       "rndMonitoredElementLabel": rndMonitoredElementLabel,
       "rndDefaultPollingInterval": rndDefaultPollingInterval,
       "rndDefaultLogFile": rndDefaultLogFile,
       "rndMonitoredElementStatus": rndMonitoredElementStatus,
       "rndMonitoringTable": rndMonitoringTable,
       "rndMonitoringEntry": rndMonitoringEntry,
       "rndMonitoredElement": rndMonitoredElement,
       "rndMonitoredObjectInstanceLabel": rndMonitoredObjectInstanceLabel,
       "rndMonitoredObjectName": rndMonitoredObjectName,
       "rndMonitoredObjectIdentifier": rndMonitoredObjectIdentifier,
       "rndMonitoredObjectInstance": rndMonitoredObjectInstance,
       "rndMonitoredObjectSyntax": rndMonitoredObjectSyntax,
       "rndMonitoringInterval": rndMonitoringInterval,
       "rndAlarmMaxTreshold": rndAlarmMaxTreshold,
       "rndAlarmMinTreshold": rndAlarmMinTreshold,
       "rndMonitoringLogfile": rndMonitoringLogfile,
       "rndMonitoringEntryStatus": rndMonitoringEntryStatus,
       "rndMonitoredIntegerInstance": rndMonitoredIntegerInstance,
       "rndMibFilesTable": rndMibFilesTable,
       "rndMibFileEntry": rndMibFileEntry,
       "rndMibFileIndex": rndMibFileIndex,
       "rndMibFilePath": rndMibFilePath,
       "rndMibFileRefresh": rndMibFileRefresh,
       "rndMibFileEntryStatus": rndMibFileEntryStatus,
       "rndHardwareConfiguration": rndHardwareConfiguration,
       "rndEraseSimulatedConfiguration": rndEraseSimulatedConfiguration,
       "rndDeleteValuesTable": rndDeleteValuesTable,
       "rndDeleteValuesEntry": rndDeleteValuesEntry,
       "rndRowStatusVariableName": rndRowStatusVariableName,
       "rndRowStatusObjectId": rndRowStatusObjectId,
       "rndRowDeleteValue": rndRowDeleteValue,
       "rndDeleteValueEntryStatus": rndDeleteValueEntryStatus,
       "snmpTesting": snmpTesting,
       "rndSimulatedVariablesTable": rndSimulatedVariablesTable,
       "rndSimulatedVariablesEntry": rndSimulatedVariablesEntry,
       "rndSimulatedVariableEntryIndex": rndSimulatedVariableEntryIndex,
       "rndSimulatedVariableObjectId": rndSimulatedVariableObjectId,
       "rndNotSupportedField": rndNotSupportedField,
       "rndSimulatedVariableEntryStatus": rndSimulatedVariableEntryStatus,
       "rndSnmpTestPassword": rndSnmpTestPassword,
       "rndSnmpTests": rndSnmpTests,
       "rndSimulateUndo": rndSimulateUndo,
       "rlSnmpServTestRequest": rlSnmpServTestRequest,
       "rlSnmpServTestResponse": rlSnmpServTestResponse,
       "rlSnmpServCreateTestPool": rlSnmpServCreateTestPool,
       "rlSnmpServITCbindClients": rlSnmpServITCbindClients,
       "rlSnmpTestSimulatedVariables": rlSnmpTestSimulatedVariables,
       "rlTstBasicRateTable": rlTstBasicRateTable,
       "rlTstBasicRateEntry": rlTstBasicRateEntry,
       "rlTstBasicRateIfType": rlTstBasicRateIfType,
       "rlTstBasicRateLineTopology": rlTstBasicRateLineTopology,
       "rlTstBasicRateIfMode": rlTstBasicRateIfMode,
       "rlTstBasicRateSignalMode": rlTstBasicRateSignalMode,
       "rlMibTree": rlMibTree,
       "rlMibTreeTable": rlMibTreeTable,
       "rlMibTreeEntry": rlMibTreeEntry,
       "rlMibTreeFather": rlMibTreeFather,
       "rlMibTreeSonIndex": rlMibTreeSonIndex,
       "rlMibTreeSon": rlMibTreeSon,
       "rlMibTreeSonObjectId": rlMibTreeSonObjectId,
       "rlMibTreeGrandFather": rlMibTreeGrandFather,
       "rlMibInstances": rlMibInstances,
       "rlMibTableInstancesInfoTable": rlMibTableInstancesInfoTable,
       "rlMibTableInstancesInfoEntry": rlMibTableInstancesInfoEntry,
       "rlMibTableInstancesInfoTableName": rlMibTableInstancesInfoTableName,
       "rlMibTableInstancesInfoNumOfInstances": rlMibTableInstancesInfoNumOfInstances,
       "rsPingMIB": rsPingMIB,
       "rsPingTable": rsPingTable,
       "rsPingEntry": rsPingEntry,
       "rsPingAddress": rsPingAddress,
       "rsPingPacketCount": rsPingPacketCount,
       "rsPingPacketSize": rsPingPacketSize,
       "rsPingPacketTimeout": rsPingPacketTimeout,
       "rsPingDelay": rsPingDelay,
       "rsPingTrapOnCompletion": rsPingTrapOnCompletion,
       "rsPingSentPackets": rsPingSentPackets,
       "rsPingReceivedPackets": rsPingReceivedPackets,
       "rsPingMinReturnTime": rsPingMinReturnTime,
       "rsPingAvgReturnTime": rsPingAvgReturnTime,
       "rsPingMaxReturnTime": rsPingMaxReturnTime,
       "rsPingCompletionStatus": rsPingCompletionStatus,
       "rsPingTimeStamp": rsPingTimeStamp,
       "rsPingEntryStatus": rsPingEntryStatus,
       "rsPingInetTable": rsPingInetTable,
       "rsPingInetEntry": rsPingInetEntry,
       "rsPingInetAddressType": rsPingInetAddressType,
       "rsPingInetAddress": rsPingInetAddress,
       "rsPingInetPacketCount": rsPingInetPacketCount,
       "rsPingInetPacketSize": rsPingInetPacketSize,
       "rsPingInetPacketTimeout": rsPingInetPacketTimeout,
       "rsPingInetDelay": rsPingInetDelay,
       "rsPingInetTrapOnCompletion": rsPingInetTrapOnCompletion,
       "rsPingInetSentPackets": rsPingInetSentPackets,
       "rsPingInetReceivedPackets": rsPingInetReceivedPackets,
       "rsPingInetMinReturnTime": rsPingInetMinReturnTime,
       "rsPingInetAvgReturnTime": rsPingInetAvgReturnTime,
       "rsPingInetMaxReturnTime": rsPingInetMaxReturnTime,
       "rsPingInetCompletionStatus": rsPingInetCompletionStatus,
       "rsPingInetTimeStamp": rsPingInetTimeStamp,
       "rsPingInetEntryStatus": rsPingInetEntryStatus,
       "rsPingInetSourceAddr": rsPingInetSourceAddr,
       "rsPowerSupplyRedundacy": rsPowerSupplyRedundacy,
       "rsPowerSupplyRedundacyTable": rsPowerSupplyRedundacyTable,
       "rsPowerSupplyRedundacyEntry": rsPowerSupplyRedundacyEntry,
       "rsPowerSupplyRedundacyReNumber": rsPowerSupplyRedundacyReNumber,
       "rsPowerSupplyRedundacyStatus": rsPowerSupplyRedundacyStatus,
       "rsNvram": rsNvram,
       "rsEraseNvramAfterReset": rsEraseNvramAfterReset,
       "rsNvramApplTable": rsNvramApplTable,
       "rsNvramApplEntry": rsNvramApplEntry,
       "rsNvramApplIndex": rsNvramApplIndex,
       "rsNvramApplName": rsNvramApplName}
)
