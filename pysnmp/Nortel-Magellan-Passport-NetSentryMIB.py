# SNMP MIB module (Nortel-Magellan-Passport-NetSentryMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-NetSentryMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:13 2024
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

(Counter32,
 DisplayString,
 Integer32,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType")

(AsciiString,
 AsciiStringIndex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vr,
 vrIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vr",
    "vrIndex")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VrNs_ObjectIdentity = ObjectIdentity
vrNs = _VrNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4)
)
_VrNsRowStatusTable_Object = MibTable
vrNsRowStatusTable = _VrNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 1)
)
if mibBuilder.loadTexts:
    vrNsRowStatusTable.setStatus("mandatory")
_VrNsRowStatusEntry_Object = MibTableRow
vrNsRowStatusEntry = _VrNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 1, 1)
)
vrNsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
)
if mibBuilder.loadTexts:
    vrNsRowStatusEntry.setStatus("mandatory")
_VrNsRowStatus_Type = RowStatus
_VrNsRowStatus_Object = MibTableColumn
vrNsRowStatus = _VrNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 1, 1, 1),
    _VrNsRowStatus_Type()
)
vrNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsRowStatus.setStatus("mandatory")
_VrNsComponentName_Type = DisplayString
_VrNsComponentName_Object = MibTableColumn
vrNsComponentName = _VrNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 1, 1, 2),
    _VrNsComponentName_Type()
)
vrNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsComponentName.setStatus("mandatory")
_VrNsStorageType_Type = StorageType
_VrNsStorageType_Object = MibTableColumn
vrNsStorageType = _VrNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 1, 1, 4),
    _VrNsStorageType_Type()
)
vrNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsStorageType.setStatus("mandatory")
_VrNsIndex_Type = NonReplicated
_VrNsIndex_Object = MibTableColumn
vrNsIndex = _VrNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 1, 1, 10),
    _VrNsIndex_Type()
)
vrNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsIndex.setStatus("mandatory")
_VrNsFile_ObjectIdentity = ObjectIdentity
vrNsFile = _VrNsFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2)
)
_VrNsFileRowStatusTable_Object = MibTable
vrNsFileRowStatusTable = _VrNsFileRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vrNsFileRowStatusTable.setStatus("mandatory")
_VrNsFileRowStatusEntry_Object = MibTableRow
vrNsFileRowStatusEntry = _VrNsFileRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 1, 1)
)
vrNsFileRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsFileIndex"),
)
if mibBuilder.loadTexts:
    vrNsFileRowStatusEntry.setStatus("mandatory")
_VrNsFileRowStatus_Type = RowStatus
_VrNsFileRowStatus_Object = MibTableColumn
vrNsFileRowStatus = _VrNsFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 1, 1, 1),
    _VrNsFileRowStatus_Type()
)
vrNsFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsFileRowStatus.setStatus("mandatory")
_VrNsFileComponentName_Type = DisplayString
_VrNsFileComponentName_Object = MibTableColumn
vrNsFileComponentName = _VrNsFileComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 1, 1, 2),
    _VrNsFileComponentName_Type()
)
vrNsFileComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFileComponentName.setStatus("mandatory")
_VrNsFileStorageType_Type = StorageType
_VrNsFileStorageType_Object = MibTableColumn
vrNsFileStorageType = _VrNsFileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 1, 1, 4),
    _VrNsFileStorageType_Type()
)
vrNsFileStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFileStorageType.setStatus("mandatory")


class _VrNsFileIndex_Type(AsciiStringIndex):
    """Custom type vrNsFileIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VrNsFileIndex_Type.__name__ = "AsciiStringIndex"
_VrNsFileIndex_Object = MibTableColumn
vrNsFileIndex = _VrNsFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 1, 1, 10),
    _VrNsFileIndex_Type()
)
vrNsFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsFileIndex.setStatus("mandatory")
_VrNsFileOperTable_Object = MibTable
vrNsFileOperTable = _VrNsFileOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 10)
)
if mibBuilder.loadTexts:
    vrNsFileOperTable.setStatus("mandatory")
_VrNsFileOperEntry_Object = MibTableRow
vrNsFileOperEntry = _VrNsFileOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 10, 1)
)
vrNsFileOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsFileIndex"),
)
if mibBuilder.loadTexts:
    vrNsFileOperEntry.setStatus("mandatory")


class _VrNsFileCompilerErrorMsg_Type(AsciiString):
    """Custom type vrNsFileCompilerErrorMsg based on AsciiString"""
    defaultHexValue = "4e6f204572726f72"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_VrNsFileCompilerErrorMsg_Type.__name__ = "AsciiString"
_VrNsFileCompilerErrorMsg_Object = MibTableColumn
vrNsFileCompilerErrorMsg = _VrNsFileCompilerErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 2, 10, 1, 1),
    _VrNsFileCompilerErrorMsg_Type()
)
vrNsFileCompilerErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFileCompilerErrorMsg.setStatus("mandatory")
_VrNsEngine_ObjectIdentity = ObjectIdentity
vrNsEngine = _VrNsEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 3)
)
_VrNsEngineRowStatusTable_Object = MibTable
vrNsEngineRowStatusTable = _VrNsEngineRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 3, 1)
)
if mibBuilder.loadTexts:
    vrNsEngineRowStatusTable.setStatus("mandatory")
_VrNsEngineRowStatusEntry_Object = MibTableRow
vrNsEngineRowStatusEntry = _VrNsEngineRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 3, 1, 1)
)
vrNsEngineRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsEngineIndex"),
)
if mibBuilder.loadTexts:
    vrNsEngineRowStatusEntry.setStatus("mandatory")
_VrNsEngineRowStatus_Type = RowStatus
_VrNsEngineRowStatus_Object = MibTableColumn
vrNsEngineRowStatus = _VrNsEngineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 3, 1, 1, 1),
    _VrNsEngineRowStatus_Type()
)
vrNsEngineRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsEngineRowStatus.setStatus("mandatory")
_VrNsEngineComponentName_Type = DisplayString
_VrNsEngineComponentName_Object = MibTableColumn
vrNsEngineComponentName = _VrNsEngineComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 3, 1, 1, 2),
    _VrNsEngineComponentName_Type()
)
vrNsEngineComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsEngineComponentName.setStatus("mandatory")
_VrNsEngineStorageType_Type = StorageType
_VrNsEngineStorageType_Object = MibTableColumn
vrNsEngineStorageType = _VrNsEngineStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 3, 1, 1, 4),
    _VrNsEngineStorageType_Type()
)
vrNsEngineStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsEngineStorageType.setStatus("mandatory")


class _VrNsEngineIndex_Type(Integer32):
    """Custom type vrNsEngineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VrNsEngineIndex_Type.__name__ = "Integer32"
_VrNsEngineIndex_Object = MibTableColumn
vrNsEngineIndex = _VrNsEngineIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 3, 1, 1, 10),
    _VrNsEngineIndex_Type()
)
vrNsEngineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsEngineIndex.setStatus("mandatory")
_VrNsIPStats_ObjectIdentity = ObjectIdentity
vrNsIPStats = _VrNsIPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4)
)
_VrNsIPStatsRowStatusTable_Object = MibTable
vrNsIPStatsRowStatusTable = _VrNsIPStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 1)
)
if mibBuilder.loadTexts:
    vrNsIPStatsRowStatusTable.setStatus("mandatory")
_VrNsIPStatsRowStatusEntry_Object = MibTableRow
vrNsIPStatsRowStatusEntry = _VrNsIPStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 1, 1)
)
vrNsIPStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPStatsIndex"),
)
if mibBuilder.loadTexts:
    vrNsIPStatsRowStatusEntry.setStatus("mandatory")
_VrNsIPStatsRowStatus_Type = RowStatus
_VrNsIPStatsRowStatus_Object = MibTableColumn
vrNsIPStatsRowStatus = _VrNsIPStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 1, 1, 1),
    _VrNsIPStatsRowStatus_Type()
)
vrNsIPStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsIPStatsRowStatus.setStatus("mandatory")
_VrNsIPStatsComponentName_Type = DisplayString
_VrNsIPStatsComponentName_Object = MibTableColumn
vrNsIPStatsComponentName = _VrNsIPStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 1, 1, 2),
    _VrNsIPStatsComponentName_Type()
)
vrNsIPStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsComponentName.setStatus("mandatory")
_VrNsIPStatsStorageType_Type = StorageType
_VrNsIPStatsStorageType_Object = MibTableColumn
vrNsIPStatsStorageType = _VrNsIPStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 1, 1, 4),
    _VrNsIPStatsStorageType_Type()
)
vrNsIPStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsStorageType.setStatus("mandatory")
_VrNsIPStatsIndex_Type = NonReplicated
_VrNsIPStatsIndex_Object = MibTableColumn
vrNsIPStatsIndex = _VrNsIPStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 1, 1, 10),
    _VrNsIPStatsIndex_Type()
)
vrNsIPStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsIPStatsIndex.setStatus("mandatory")
_VrNsIPStatsAddrStat_ObjectIdentity = ObjectIdentity
vrNsIPStatsAddrStat = _VrNsIPStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2)
)
_VrNsIPStatsAddrStatRowStatusTable_Object = MibTable
vrNsIPStatsAddrStatRowStatusTable = _VrNsIPStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatRowStatusTable.setStatus("mandatory")
_VrNsIPStatsAddrStatRowStatusEntry_Object = MibTableRow
vrNsIPStatsAddrStatRowStatusEntry = _VrNsIPStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 1, 1)
)
vrNsIPStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatRowStatusEntry.setStatus("mandatory")
_VrNsIPStatsAddrStatRowStatus_Type = RowStatus
_VrNsIPStatsAddrStatRowStatus_Object = MibTableColumn
vrNsIPStatsAddrStatRowStatus = _VrNsIPStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 1, 1, 1),
    _VrNsIPStatsAddrStatRowStatus_Type()
)
vrNsIPStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatRowStatus.setStatus("mandatory")
_VrNsIPStatsAddrStatComponentName_Type = DisplayString
_VrNsIPStatsAddrStatComponentName_Object = MibTableColumn
vrNsIPStatsAddrStatComponentName = _VrNsIPStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 1, 1, 2),
    _VrNsIPStatsAddrStatComponentName_Type()
)
vrNsIPStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatComponentName.setStatus("mandatory")
_VrNsIPStatsAddrStatStorageType_Type = StorageType
_VrNsIPStatsAddrStatStorageType_Object = MibTableColumn
vrNsIPStatsAddrStatStorageType = _VrNsIPStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 1, 1, 4),
    _VrNsIPStatsAddrStatStorageType_Type()
)
vrNsIPStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatStorageType.setStatus("mandatory")


class _VrNsIPStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsIPStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsIPStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsIPStatsAddrStatSourceAddressIndex_Object = MibTableColumn
vrNsIPStatsAddrStatSourceAddressIndex = _VrNsIPStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 1, 1, 10),
    _VrNsIPStatsAddrStatSourceAddressIndex_Type()
)
vrNsIPStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _VrNsIPStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsIPStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsIPStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsIPStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
vrNsIPStatsAddrStatDestinationAddressIndex = _VrNsIPStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 1, 1, 11),
    _VrNsIPStatsAddrStatDestinationAddressIndex_Type()
)
vrNsIPStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_VrNsIPStatsAddrStatStatsTable_Object = MibTable
vrNsIPStatsAddrStatStatsTable = _VrNsIPStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 10)
)
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatStatsTable.setStatus("mandatory")
_VrNsIPStatsAddrStatStatsEntry_Object = MibTableRow
vrNsIPStatsAddrStatStatsEntry = _VrNsIPStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 10, 1)
)
vrNsIPStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatStatsEntry.setStatus("mandatory")
_VrNsIPStatsAddrStatPacketCount_Type = Counter32
_VrNsIPStatsAddrStatPacketCount_Object = MibTableColumn
vrNsIPStatsAddrStatPacketCount = _VrNsIPStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 10, 1, 1),
    _VrNsIPStatsAddrStatPacketCount_Type()
)
vrNsIPStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatPacketCount.setStatus("mandatory")
_VrNsIPStatsAddrStatByteCount_Type = Counter32
_VrNsIPStatsAddrStatByteCount_Object = MibTableColumn
vrNsIPStatsAddrStatByteCount = _VrNsIPStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 10, 1, 2),
    _VrNsIPStatsAddrStatByteCount_Type()
)
vrNsIPStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatByteCount.setStatus("mandatory")
_VrNsIPStatsAddrStatCounter1_Type = Counter32
_VrNsIPStatsAddrStatCounter1_Object = MibTableColumn
vrNsIPStatsAddrStatCounter1 = _VrNsIPStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 10, 1, 3),
    _VrNsIPStatsAddrStatCounter1_Type()
)
vrNsIPStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatCounter1.setStatus("mandatory")
_VrNsIPStatsAddrStatCounter2_Type = Counter32
_VrNsIPStatsAddrStatCounter2_Object = MibTableColumn
vrNsIPStatsAddrStatCounter2 = _VrNsIPStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 4, 2, 10, 1, 4),
    _VrNsIPStatsAddrStatCounter2_Type()
)
vrNsIPStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPStatsAddrStatCounter2.setStatus("mandatory")
_VrNsIPXStats_ObjectIdentity = ObjectIdentity
vrNsIPXStats = _VrNsIPXStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5)
)
_VrNsIPXStatsRowStatusTable_Object = MibTable
vrNsIPXStatsRowStatusTable = _VrNsIPXStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 1)
)
if mibBuilder.loadTexts:
    vrNsIPXStatsRowStatusTable.setStatus("mandatory")
_VrNsIPXStatsRowStatusEntry_Object = MibTableRow
vrNsIPXStatsRowStatusEntry = _VrNsIPXStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 1, 1)
)
vrNsIPXStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPXStatsIndex"),
)
if mibBuilder.loadTexts:
    vrNsIPXStatsRowStatusEntry.setStatus("mandatory")
_VrNsIPXStatsRowStatus_Type = RowStatus
_VrNsIPXStatsRowStatus_Object = MibTableColumn
vrNsIPXStatsRowStatus = _VrNsIPXStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 1, 1, 1),
    _VrNsIPXStatsRowStatus_Type()
)
vrNsIPXStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsIPXStatsRowStatus.setStatus("mandatory")
_VrNsIPXStatsComponentName_Type = DisplayString
_VrNsIPXStatsComponentName_Object = MibTableColumn
vrNsIPXStatsComponentName = _VrNsIPXStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 1, 1, 2),
    _VrNsIPXStatsComponentName_Type()
)
vrNsIPXStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsComponentName.setStatus("mandatory")
_VrNsIPXStatsStorageType_Type = StorageType
_VrNsIPXStatsStorageType_Object = MibTableColumn
vrNsIPXStatsStorageType = _VrNsIPXStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 1, 1, 4),
    _VrNsIPXStatsStorageType_Type()
)
vrNsIPXStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsStorageType.setStatus("mandatory")
_VrNsIPXStatsIndex_Type = NonReplicated
_VrNsIPXStatsIndex_Object = MibTableColumn
vrNsIPXStatsIndex = _VrNsIPXStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 1, 1, 10),
    _VrNsIPXStatsIndex_Type()
)
vrNsIPXStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsIPXStatsIndex.setStatus("mandatory")
_VrNsIPXStatsAddrStat_ObjectIdentity = ObjectIdentity
vrNsIPXStatsAddrStat = _VrNsIPXStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2)
)
_VrNsIPXStatsAddrStatRowStatusTable_Object = MibTable
vrNsIPXStatsAddrStatRowStatusTable = _VrNsIPXStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatRowStatusTable.setStatus("mandatory")
_VrNsIPXStatsAddrStatRowStatusEntry_Object = MibTableRow
vrNsIPXStatsAddrStatRowStatusEntry = _VrNsIPXStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 1, 1)
)
vrNsIPXStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPXStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPXStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPXStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatRowStatusEntry.setStatus("mandatory")
_VrNsIPXStatsAddrStatRowStatus_Type = RowStatus
_VrNsIPXStatsAddrStatRowStatus_Object = MibTableColumn
vrNsIPXStatsAddrStatRowStatus = _VrNsIPXStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 1, 1, 1),
    _VrNsIPXStatsAddrStatRowStatus_Type()
)
vrNsIPXStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatRowStatus.setStatus("mandatory")
_VrNsIPXStatsAddrStatComponentName_Type = DisplayString
_VrNsIPXStatsAddrStatComponentName_Object = MibTableColumn
vrNsIPXStatsAddrStatComponentName = _VrNsIPXStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 1, 1, 2),
    _VrNsIPXStatsAddrStatComponentName_Type()
)
vrNsIPXStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatComponentName.setStatus("mandatory")
_VrNsIPXStatsAddrStatStorageType_Type = StorageType
_VrNsIPXStatsAddrStatStorageType_Object = MibTableColumn
vrNsIPXStatsAddrStatStorageType = _VrNsIPXStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 1, 1, 4),
    _VrNsIPXStatsAddrStatStorageType_Type()
)
vrNsIPXStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatStorageType.setStatus("mandatory")


class _VrNsIPXStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsIPXStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsIPXStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsIPXStatsAddrStatSourceAddressIndex_Object = MibTableColumn
vrNsIPXStatsAddrStatSourceAddressIndex = _VrNsIPXStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 1, 1, 10),
    _VrNsIPXStatsAddrStatSourceAddressIndex_Type()
)
vrNsIPXStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _VrNsIPXStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsIPXStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsIPXStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsIPXStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
vrNsIPXStatsAddrStatDestinationAddressIndex = _VrNsIPXStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 1, 1, 11),
    _VrNsIPXStatsAddrStatDestinationAddressIndex_Type()
)
vrNsIPXStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_VrNsIPXStatsAddrStatStatsTable_Object = MibTable
vrNsIPXStatsAddrStatStatsTable = _VrNsIPXStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 10)
)
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatStatsTable.setStatus("mandatory")
_VrNsIPXStatsAddrStatStatsEntry_Object = MibTableRow
vrNsIPXStatsAddrStatStatsEntry = _VrNsIPXStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 10, 1)
)
vrNsIPXStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPXStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPXStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIPXStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatStatsEntry.setStatus("mandatory")
_VrNsIPXStatsAddrStatPacketCount_Type = Counter32
_VrNsIPXStatsAddrStatPacketCount_Object = MibTableColumn
vrNsIPXStatsAddrStatPacketCount = _VrNsIPXStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 10, 1, 1),
    _VrNsIPXStatsAddrStatPacketCount_Type()
)
vrNsIPXStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatPacketCount.setStatus("mandatory")
_VrNsIPXStatsAddrStatByteCount_Type = Counter32
_VrNsIPXStatsAddrStatByteCount_Object = MibTableColumn
vrNsIPXStatsAddrStatByteCount = _VrNsIPXStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 10, 1, 2),
    _VrNsIPXStatsAddrStatByteCount_Type()
)
vrNsIPXStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatByteCount.setStatus("mandatory")
_VrNsIPXStatsAddrStatCounter1_Type = Counter32
_VrNsIPXStatsAddrStatCounter1_Object = MibTableColumn
vrNsIPXStatsAddrStatCounter1 = _VrNsIPXStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 10, 1, 3),
    _VrNsIPXStatsAddrStatCounter1_Type()
)
vrNsIPXStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatCounter1.setStatus("mandatory")
_VrNsIPXStatsAddrStatCounter2_Type = Counter32
_VrNsIPXStatsAddrStatCounter2_Object = MibTableColumn
vrNsIPXStatsAddrStatCounter2 = _VrNsIPXStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 5, 2, 10, 1, 4),
    _VrNsIPXStatsAddrStatCounter2_Type()
)
vrNsIPXStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsIPXStatsAddrStatCounter2.setStatus("mandatory")
_VrNsATStats_ObjectIdentity = ObjectIdentity
vrNsATStats = _VrNsATStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6)
)
_VrNsATStatsRowStatusTable_Object = MibTable
vrNsATStatsRowStatusTable = _VrNsATStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 1)
)
if mibBuilder.loadTexts:
    vrNsATStatsRowStatusTable.setStatus("mandatory")
_VrNsATStatsRowStatusEntry_Object = MibTableRow
vrNsATStatsRowStatusEntry = _VrNsATStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 1, 1)
)
vrNsATStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsATStatsIndex"),
)
if mibBuilder.loadTexts:
    vrNsATStatsRowStatusEntry.setStatus("mandatory")
_VrNsATStatsRowStatus_Type = RowStatus
_VrNsATStatsRowStatus_Object = MibTableColumn
vrNsATStatsRowStatus = _VrNsATStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 1, 1, 1),
    _VrNsATStatsRowStatus_Type()
)
vrNsATStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsATStatsRowStatus.setStatus("mandatory")
_VrNsATStatsComponentName_Type = DisplayString
_VrNsATStatsComponentName_Object = MibTableColumn
vrNsATStatsComponentName = _VrNsATStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 1, 1, 2),
    _VrNsATStatsComponentName_Type()
)
vrNsATStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsComponentName.setStatus("mandatory")
_VrNsATStatsStorageType_Type = StorageType
_VrNsATStatsStorageType_Object = MibTableColumn
vrNsATStatsStorageType = _VrNsATStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 1, 1, 4),
    _VrNsATStatsStorageType_Type()
)
vrNsATStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsStorageType.setStatus("mandatory")
_VrNsATStatsIndex_Type = NonReplicated
_VrNsATStatsIndex_Object = MibTableColumn
vrNsATStatsIndex = _VrNsATStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 1, 1, 10),
    _VrNsATStatsIndex_Type()
)
vrNsATStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsATStatsIndex.setStatus("mandatory")
_VrNsATStatsAddrStat_ObjectIdentity = ObjectIdentity
vrNsATStatsAddrStat = _VrNsATStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2)
)
_VrNsATStatsAddrStatRowStatusTable_Object = MibTable
vrNsATStatsAddrStatRowStatusTable = _VrNsATStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatRowStatusTable.setStatus("mandatory")
_VrNsATStatsAddrStatRowStatusEntry_Object = MibTableRow
vrNsATStatsAddrStatRowStatusEntry = _VrNsATStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 1, 1)
)
vrNsATStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsATStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsATStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsATStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatRowStatusEntry.setStatus("mandatory")
_VrNsATStatsAddrStatRowStatus_Type = RowStatus
_VrNsATStatsAddrStatRowStatus_Object = MibTableColumn
vrNsATStatsAddrStatRowStatus = _VrNsATStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 1, 1, 1),
    _VrNsATStatsAddrStatRowStatus_Type()
)
vrNsATStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatRowStatus.setStatus("mandatory")
_VrNsATStatsAddrStatComponentName_Type = DisplayString
_VrNsATStatsAddrStatComponentName_Object = MibTableColumn
vrNsATStatsAddrStatComponentName = _VrNsATStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 1, 1, 2),
    _VrNsATStatsAddrStatComponentName_Type()
)
vrNsATStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatComponentName.setStatus("mandatory")
_VrNsATStatsAddrStatStorageType_Type = StorageType
_VrNsATStatsAddrStatStorageType_Object = MibTableColumn
vrNsATStatsAddrStatStorageType = _VrNsATStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 1, 1, 4),
    _VrNsATStatsAddrStatStorageType_Type()
)
vrNsATStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatStorageType.setStatus("mandatory")


class _VrNsATStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsATStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsATStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsATStatsAddrStatSourceAddressIndex_Object = MibTableColumn
vrNsATStatsAddrStatSourceAddressIndex = _VrNsATStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 1, 1, 10),
    _VrNsATStatsAddrStatSourceAddressIndex_Type()
)
vrNsATStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _VrNsATStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsATStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsATStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsATStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
vrNsATStatsAddrStatDestinationAddressIndex = _VrNsATStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 1, 1, 11),
    _VrNsATStatsAddrStatDestinationAddressIndex_Type()
)
vrNsATStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_VrNsATStatsAddrStatStatsTable_Object = MibTable
vrNsATStatsAddrStatStatsTable = _VrNsATStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 10)
)
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatStatsTable.setStatus("mandatory")
_VrNsATStatsAddrStatStatsEntry_Object = MibTableRow
vrNsATStatsAddrStatStatsEntry = _VrNsATStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 10, 1)
)
vrNsATStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsATStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsATStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsATStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatStatsEntry.setStatus("mandatory")
_VrNsATStatsAddrStatPacketCount_Type = Counter32
_VrNsATStatsAddrStatPacketCount_Object = MibTableColumn
vrNsATStatsAddrStatPacketCount = _VrNsATStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 10, 1, 1),
    _VrNsATStatsAddrStatPacketCount_Type()
)
vrNsATStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatPacketCount.setStatus("mandatory")
_VrNsATStatsAddrStatByteCount_Type = Counter32
_VrNsATStatsAddrStatByteCount_Object = MibTableColumn
vrNsATStatsAddrStatByteCount = _VrNsATStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 10, 1, 2),
    _VrNsATStatsAddrStatByteCount_Type()
)
vrNsATStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatByteCount.setStatus("mandatory")
_VrNsATStatsAddrStatCounter1_Type = Counter32
_VrNsATStatsAddrStatCounter1_Object = MibTableColumn
vrNsATStatsAddrStatCounter1 = _VrNsATStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 10, 1, 3),
    _VrNsATStatsAddrStatCounter1_Type()
)
vrNsATStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatCounter1.setStatus("mandatory")
_VrNsATStatsAddrStatCounter2_Type = Counter32
_VrNsATStatsAddrStatCounter2_Object = MibTableColumn
vrNsATStatsAddrStatCounter2 = _VrNsATStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 6, 2, 10, 1, 4),
    _VrNsATStatsAddrStatCounter2_Type()
)
vrNsATStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsATStatsAddrStatCounter2.setStatus("mandatory")
_VrNsDNStats_ObjectIdentity = ObjectIdentity
vrNsDNStats = _VrNsDNStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7)
)
_VrNsDNStatsRowStatusTable_Object = MibTable
vrNsDNStatsRowStatusTable = _VrNsDNStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 1)
)
if mibBuilder.loadTexts:
    vrNsDNStatsRowStatusTable.setStatus("mandatory")
_VrNsDNStatsRowStatusEntry_Object = MibTableRow
vrNsDNStatsRowStatusEntry = _VrNsDNStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 1, 1)
)
vrNsDNStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsDNStatsIndex"),
)
if mibBuilder.loadTexts:
    vrNsDNStatsRowStatusEntry.setStatus("mandatory")
_VrNsDNStatsRowStatus_Type = RowStatus
_VrNsDNStatsRowStatus_Object = MibTableColumn
vrNsDNStatsRowStatus = _VrNsDNStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 1, 1, 1),
    _VrNsDNStatsRowStatus_Type()
)
vrNsDNStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsDNStatsRowStatus.setStatus("mandatory")
_VrNsDNStatsComponentName_Type = DisplayString
_VrNsDNStatsComponentName_Object = MibTableColumn
vrNsDNStatsComponentName = _VrNsDNStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 1, 1, 2),
    _VrNsDNStatsComponentName_Type()
)
vrNsDNStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsComponentName.setStatus("mandatory")
_VrNsDNStatsStorageType_Type = StorageType
_VrNsDNStatsStorageType_Object = MibTableColumn
vrNsDNStatsStorageType = _VrNsDNStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 1, 1, 4),
    _VrNsDNStatsStorageType_Type()
)
vrNsDNStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsStorageType.setStatus("mandatory")
_VrNsDNStatsIndex_Type = NonReplicated
_VrNsDNStatsIndex_Object = MibTableColumn
vrNsDNStatsIndex = _VrNsDNStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 1, 1, 10),
    _VrNsDNStatsIndex_Type()
)
vrNsDNStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsDNStatsIndex.setStatus("mandatory")
_VrNsDNStatsAddrStat_ObjectIdentity = ObjectIdentity
vrNsDNStatsAddrStat = _VrNsDNStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2)
)
_VrNsDNStatsAddrStatRowStatusTable_Object = MibTable
vrNsDNStatsAddrStatRowStatusTable = _VrNsDNStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatRowStatusTable.setStatus("mandatory")
_VrNsDNStatsAddrStatRowStatusEntry_Object = MibTableRow
vrNsDNStatsAddrStatRowStatusEntry = _VrNsDNStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 1, 1)
)
vrNsDNStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsDNStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsDNStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsDNStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatRowStatusEntry.setStatus("mandatory")
_VrNsDNStatsAddrStatRowStatus_Type = RowStatus
_VrNsDNStatsAddrStatRowStatus_Object = MibTableColumn
vrNsDNStatsAddrStatRowStatus = _VrNsDNStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 1, 1, 1),
    _VrNsDNStatsAddrStatRowStatus_Type()
)
vrNsDNStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatRowStatus.setStatus("mandatory")
_VrNsDNStatsAddrStatComponentName_Type = DisplayString
_VrNsDNStatsAddrStatComponentName_Object = MibTableColumn
vrNsDNStatsAddrStatComponentName = _VrNsDNStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 1, 1, 2),
    _VrNsDNStatsAddrStatComponentName_Type()
)
vrNsDNStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatComponentName.setStatus("mandatory")
_VrNsDNStatsAddrStatStorageType_Type = StorageType
_VrNsDNStatsAddrStatStorageType_Object = MibTableColumn
vrNsDNStatsAddrStatStorageType = _VrNsDNStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 1, 1, 4),
    _VrNsDNStatsAddrStatStorageType_Type()
)
vrNsDNStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatStorageType.setStatus("mandatory")


class _VrNsDNStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsDNStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsDNStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsDNStatsAddrStatSourceAddressIndex_Object = MibTableColumn
vrNsDNStatsAddrStatSourceAddressIndex = _VrNsDNStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 1, 1, 10),
    _VrNsDNStatsAddrStatSourceAddressIndex_Type()
)
vrNsDNStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _VrNsDNStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsDNStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsDNStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsDNStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
vrNsDNStatsAddrStatDestinationAddressIndex = _VrNsDNStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 1, 1, 11),
    _VrNsDNStatsAddrStatDestinationAddressIndex_Type()
)
vrNsDNStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_VrNsDNStatsAddrStatStatsTable_Object = MibTable
vrNsDNStatsAddrStatStatsTable = _VrNsDNStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 10)
)
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatStatsTable.setStatus("mandatory")
_VrNsDNStatsAddrStatStatsEntry_Object = MibTableRow
vrNsDNStatsAddrStatStatsEntry = _VrNsDNStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 10, 1)
)
vrNsDNStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsDNStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsDNStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsDNStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatStatsEntry.setStatus("mandatory")
_VrNsDNStatsAddrStatPacketCount_Type = Counter32
_VrNsDNStatsAddrStatPacketCount_Object = MibTableColumn
vrNsDNStatsAddrStatPacketCount = _VrNsDNStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 10, 1, 1),
    _VrNsDNStatsAddrStatPacketCount_Type()
)
vrNsDNStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatPacketCount.setStatus("mandatory")
_VrNsDNStatsAddrStatByteCount_Type = Counter32
_VrNsDNStatsAddrStatByteCount_Object = MibTableColumn
vrNsDNStatsAddrStatByteCount = _VrNsDNStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 10, 1, 2),
    _VrNsDNStatsAddrStatByteCount_Type()
)
vrNsDNStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatByteCount.setStatus("mandatory")
_VrNsDNStatsAddrStatCounter1_Type = Counter32
_VrNsDNStatsAddrStatCounter1_Object = MibTableColumn
vrNsDNStatsAddrStatCounter1 = _VrNsDNStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 10, 1, 3),
    _VrNsDNStatsAddrStatCounter1_Type()
)
vrNsDNStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatCounter1.setStatus("mandatory")
_VrNsDNStatsAddrStatCounter2_Type = Counter32
_VrNsDNStatsAddrStatCounter2_Object = MibTableColumn
vrNsDNStatsAddrStatCounter2 = _VrNsDNStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 7, 2, 10, 1, 4),
    _VrNsDNStatsAddrStatCounter2_Type()
)
vrNsDNStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDNStatsAddrStatCounter2.setStatus("mandatory")
_VrNsBrStats_ObjectIdentity = ObjectIdentity
vrNsBrStats = _VrNsBrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8)
)
_VrNsBrStatsRowStatusTable_Object = MibTable
vrNsBrStatsRowStatusTable = _VrNsBrStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 1)
)
if mibBuilder.loadTexts:
    vrNsBrStatsRowStatusTable.setStatus("mandatory")
_VrNsBrStatsRowStatusEntry_Object = MibTableRow
vrNsBrStatsRowStatusEntry = _VrNsBrStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 1, 1)
)
vrNsBrStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsBrStatsIndex"),
)
if mibBuilder.loadTexts:
    vrNsBrStatsRowStatusEntry.setStatus("mandatory")
_VrNsBrStatsRowStatus_Type = RowStatus
_VrNsBrStatsRowStatus_Object = MibTableColumn
vrNsBrStatsRowStatus = _VrNsBrStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 1, 1, 1),
    _VrNsBrStatsRowStatus_Type()
)
vrNsBrStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsBrStatsRowStatus.setStatus("mandatory")
_VrNsBrStatsComponentName_Type = DisplayString
_VrNsBrStatsComponentName_Object = MibTableColumn
vrNsBrStatsComponentName = _VrNsBrStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 1, 1, 2),
    _VrNsBrStatsComponentName_Type()
)
vrNsBrStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsComponentName.setStatus("mandatory")
_VrNsBrStatsStorageType_Type = StorageType
_VrNsBrStatsStorageType_Object = MibTableColumn
vrNsBrStatsStorageType = _VrNsBrStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 1, 1, 4),
    _VrNsBrStatsStorageType_Type()
)
vrNsBrStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsStorageType.setStatus("mandatory")
_VrNsBrStatsIndex_Type = NonReplicated
_VrNsBrStatsIndex_Object = MibTableColumn
vrNsBrStatsIndex = _VrNsBrStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 1, 1, 10),
    _VrNsBrStatsIndex_Type()
)
vrNsBrStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsBrStatsIndex.setStatus("mandatory")
_VrNsBrStatsAddrStat_ObjectIdentity = ObjectIdentity
vrNsBrStatsAddrStat = _VrNsBrStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2)
)
_VrNsBrStatsAddrStatRowStatusTable_Object = MibTable
vrNsBrStatsAddrStatRowStatusTable = _VrNsBrStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatRowStatusTable.setStatus("mandatory")
_VrNsBrStatsAddrStatRowStatusEntry_Object = MibTableRow
vrNsBrStatsAddrStatRowStatusEntry = _VrNsBrStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 1, 1)
)
vrNsBrStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsBrStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsBrStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsBrStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatRowStatusEntry.setStatus("mandatory")
_VrNsBrStatsAddrStatRowStatus_Type = RowStatus
_VrNsBrStatsAddrStatRowStatus_Object = MibTableColumn
vrNsBrStatsAddrStatRowStatus = _VrNsBrStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 1, 1, 1),
    _VrNsBrStatsAddrStatRowStatus_Type()
)
vrNsBrStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatRowStatus.setStatus("mandatory")
_VrNsBrStatsAddrStatComponentName_Type = DisplayString
_VrNsBrStatsAddrStatComponentName_Object = MibTableColumn
vrNsBrStatsAddrStatComponentName = _VrNsBrStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 1, 1, 2),
    _VrNsBrStatsAddrStatComponentName_Type()
)
vrNsBrStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatComponentName.setStatus("mandatory")
_VrNsBrStatsAddrStatStorageType_Type = StorageType
_VrNsBrStatsAddrStatStorageType_Object = MibTableColumn
vrNsBrStatsAddrStatStorageType = _VrNsBrStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 1, 1, 4),
    _VrNsBrStatsAddrStatStorageType_Type()
)
vrNsBrStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatStorageType.setStatus("mandatory")


class _VrNsBrStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsBrStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsBrStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsBrStatsAddrStatSourceAddressIndex_Object = MibTableColumn
vrNsBrStatsAddrStatSourceAddressIndex = _VrNsBrStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 1, 1, 10),
    _VrNsBrStatsAddrStatSourceAddressIndex_Type()
)
vrNsBrStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _VrNsBrStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type vrNsBrStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsBrStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_VrNsBrStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
vrNsBrStatsAddrStatDestinationAddressIndex = _VrNsBrStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 1, 1, 11),
    _VrNsBrStatsAddrStatDestinationAddressIndex_Type()
)
vrNsBrStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_VrNsBrStatsAddrStatStatsTable_Object = MibTable
vrNsBrStatsAddrStatStatsTable = _VrNsBrStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 10)
)
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatStatsTable.setStatus("mandatory")
_VrNsBrStatsAddrStatStatsEntry_Object = MibTableRow
vrNsBrStatsAddrStatStatsEntry = _VrNsBrStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 10, 1)
)
vrNsBrStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsBrStatsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsBrStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsBrStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatStatsEntry.setStatus("mandatory")
_VrNsBrStatsAddrStatPacketCount_Type = Counter32
_VrNsBrStatsAddrStatPacketCount_Object = MibTableColumn
vrNsBrStatsAddrStatPacketCount = _VrNsBrStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 10, 1, 1),
    _VrNsBrStatsAddrStatPacketCount_Type()
)
vrNsBrStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatPacketCount.setStatus("mandatory")
_VrNsBrStatsAddrStatByteCount_Type = Counter32
_VrNsBrStatsAddrStatByteCount_Object = MibTableColumn
vrNsBrStatsAddrStatByteCount = _VrNsBrStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 10, 1, 2),
    _VrNsBrStatsAddrStatByteCount_Type()
)
vrNsBrStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatByteCount.setStatus("mandatory")
_VrNsBrStatsAddrStatCounter1_Type = Counter32
_VrNsBrStatsAddrStatCounter1_Object = MibTableColumn
vrNsBrStatsAddrStatCounter1 = _VrNsBrStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 10, 1, 3),
    _VrNsBrStatsAddrStatCounter1_Type()
)
vrNsBrStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatCounter1.setStatus("mandatory")
_VrNsBrStatsAddrStatCounter2_Type = Counter32
_VrNsBrStatsAddrStatCounter2_Object = MibTableColumn
vrNsBrStatsAddrStatCounter2 = _VrNsBrStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 8, 2, 10, 1, 4),
    _VrNsBrStatsAddrStatCounter2_Type()
)
vrNsBrStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsBrStatsAddrStatCounter2.setStatus("mandatory")
_VrNsFilter_ObjectIdentity = ObjectIdentity
vrNsFilter = _VrNsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9)
)
_VrNsFilterRowStatusTable_Object = MibTable
vrNsFilterRowStatusTable = _VrNsFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 1)
)
if mibBuilder.loadTexts:
    vrNsFilterRowStatusTable.setStatus("mandatory")
_VrNsFilterRowStatusEntry_Object = MibTableRow
vrNsFilterRowStatusEntry = _VrNsFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 1, 1)
)
vrNsFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsFilterNameIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsFilterKindIndex"),
)
if mibBuilder.loadTexts:
    vrNsFilterRowStatusEntry.setStatus("mandatory")
_VrNsFilterRowStatus_Type = RowStatus
_VrNsFilterRowStatus_Object = MibTableColumn
vrNsFilterRowStatus = _VrNsFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 1, 1, 1),
    _VrNsFilterRowStatus_Type()
)
vrNsFilterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterRowStatus.setStatus("mandatory")
_VrNsFilterComponentName_Type = DisplayString
_VrNsFilterComponentName_Object = MibTableColumn
vrNsFilterComponentName = _VrNsFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 1, 1, 2),
    _VrNsFilterComponentName_Type()
)
vrNsFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterComponentName.setStatus("mandatory")
_VrNsFilterStorageType_Type = StorageType
_VrNsFilterStorageType_Object = MibTableColumn
vrNsFilterStorageType = _VrNsFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 1, 1, 4),
    _VrNsFilterStorageType_Type()
)
vrNsFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterStorageType.setStatus("mandatory")


class _VrNsFilterNameIndex_Type(AsciiStringIndex):
    """Custom type vrNsFilterNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VrNsFilterNameIndex_Type.__name__ = "AsciiStringIndex"
_VrNsFilterNameIndex_Object = MibTableColumn
vrNsFilterNameIndex = _VrNsFilterNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 1, 1, 10),
    _VrNsFilterNameIndex_Type()
)
vrNsFilterNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsFilterNameIndex.setStatus("mandatory")


class _VrNsFilterKindIndex_Type(Integer32):
    """Custom type vrNsFilterKindIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("accreditTable", 6),
          ("aeso", 5),
          ("aesoData", 3),
          ("compartment", 2),
          ("filter", 0),
          ("metaFilter", 8),
          ("nleso", 4),
          ("pafSet", 1),
          ("setData", 7))
    )


_VrNsFilterKindIndex_Type.__name__ = "Integer32"
_VrNsFilterKindIndex_Object = MibTableColumn
vrNsFilterKindIndex = _VrNsFilterKindIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 1, 1, 11),
    _VrNsFilterKindIndex_Type()
)
vrNsFilterKindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrNsFilterKindIndex.setStatus("mandatory")
_VrNsFilterStatsTable_Object = MibTable
vrNsFilterStatsTable = _VrNsFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10)
)
if mibBuilder.loadTexts:
    vrNsFilterStatsTable.setStatus("mandatory")
_VrNsFilterStatsEntry_Object = MibTableRow
vrNsFilterStatsEntry = _VrNsFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1)
)
vrNsFilterStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsFilterNameIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsFilterKindIndex"),
)
if mibBuilder.loadTexts:
    vrNsFilterStatsEntry.setStatus("mandatory")
_VrNsFilterPacketsSucceeded_Type = Counter32
_VrNsFilterPacketsSucceeded_Object = MibTableColumn
vrNsFilterPacketsSucceeded = _VrNsFilterPacketsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 1),
    _VrNsFilterPacketsSucceeded_Type()
)
vrNsFilterPacketsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterPacketsSucceeded.setStatus("mandatory")
_VrNsFilterBytesSucceeded_Type = Counter32
_VrNsFilterBytesSucceeded_Object = MibTableColumn
vrNsFilterBytesSucceeded = _VrNsFilterBytesSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 2),
    _VrNsFilterBytesSucceeded_Type()
)
vrNsFilterBytesSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterBytesSucceeded.setStatus("mandatory")
_VrNsFilterPacketsFailed_Type = Counter32
_VrNsFilterPacketsFailed_Object = MibTableColumn
vrNsFilterPacketsFailed = _VrNsFilterPacketsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 3),
    _VrNsFilterPacketsFailed_Type()
)
vrNsFilterPacketsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterPacketsFailed.setStatus("mandatory")
_VrNsFilterBytesFailed_Type = Counter32
_VrNsFilterBytesFailed_Object = MibTableColumn
vrNsFilterBytesFailed = _VrNsFilterBytesFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 4),
    _VrNsFilterBytesFailed_Type()
)
vrNsFilterBytesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterBytesFailed.setStatus("mandatory")
_VrNsFilterPacketsBreaked_Type = Counter32
_VrNsFilterPacketsBreaked_Object = MibTableColumn
vrNsFilterPacketsBreaked = _VrNsFilterPacketsBreaked_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 5),
    _VrNsFilterPacketsBreaked_Type()
)
vrNsFilterPacketsBreaked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterPacketsBreaked.setStatus("mandatory")
_VrNsFilterBytesBreaked_Type = Counter32
_VrNsFilterBytesBreaked_Object = MibTableColumn
vrNsFilterBytesBreaked = _VrNsFilterBytesBreaked_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 6),
    _VrNsFilterBytesBreaked_Type()
)
vrNsFilterBytesBreaked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterBytesBreaked.setStatus("mandatory")
_VrNsFilterPacketsContinued_Type = Counter32
_VrNsFilterPacketsContinued_Object = MibTableColumn
vrNsFilterPacketsContinued = _VrNsFilterPacketsContinued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 7),
    _VrNsFilterPacketsContinued_Type()
)
vrNsFilterPacketsContinued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterPacketsContinued.setStatus("mandatory")
_VrNsFilterBytesContinued_Type = Counter32
_VrNsFilterBytesContinued_Object = MibTableColumn
vrNsFilterBytesContinued = _VrNsFilterBytesContinued_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 9, 10, 1, 8),
    _VrNsFilterBytesContinued_Type()
)
vrNsFilterBytesContinued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsFilterBytesContinued.setStatus("mandatory")
_VrNsProvTable_Object = MibTable
vrNsProvTable = _VrNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 100)
)
if mibBuilder.loadTexts:
    vrNsProvTable.setStatus("mandatory")
_VrNsProvEntry_Object = MibTableRow
vrNsProvEntry = _VrNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 100, 1)
)
vrNsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
)
if mibBuilder.loadTexts:
    vrNsProvEntry.setStatus("mandatory")


class _VrNsDropConditions_Type(OctetString):
    """Custom type vrNsDropConditions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VrNsDropConditions_Type.__name__ = "OctetString"
_VrNsDropConditions_Object = MibTableColumn
vrNsDropConditions = _VrNsDropConditions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 100, 1, 1),
    _VrNsDropConditions_Type()
)
vrNsDropConditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrNsDropConditions.setStatus("mandatory")
_VrNsStatsTable_Object = MibTable
vrNsStatsTable = _VrNsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101)
)
if mibBuilder.loadTexts:
    vrNsStatsTable.setStatus("mandatory")
_VrNsStatsEntry_Object = MibTableRow
vrNsStatsEntry = _VrNsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1)
)
vrNsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-NetSentryMIB", "vrNsIndex"),
)
if mibBuilder.loadTexts:
    vrNsStatsEntry.setStatus("mandatory")
_VrNsPacketsProcessed_Type = Counter32
_VrNsPacketsProcessed_Object = MibTableColumn
vrNsPacketsProcessed = _VrNsPacketsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 1),
    _VrNsPacketsProcessed_Type()
)
vrNsPacketsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsPacketsProcessed.setStatus("mandatory")
_VrNsPacketsFailed_Type = Counter32
_VrNsPacketsFailed_Object = MibTableColumn
vrNsPacketsFailed = _VrNsPacketsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 2),
    _VrNsPacketsFailed_Type()
)
vrNsPacketsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsPacketsFailed.setStatus("mandatory")
_VrNsStatsNoMem_Type = Counter32
_VrNsStatsNoMem_Object = MibTableColumn
vrNsStatsNoMem = _VrNsStatsNoMem_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 3),
    _VrNsStatsNoMem_Type()
)
vrNsStatsNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsStatsNoMem.setStatus("mandatory")
_VrNsHsaOkayFailed_Type = Counter32
_VrNsHsaOkayFailed_Object = MibTableColumn
vrNsHsaOkayFailed = _VrNsHsaOkayFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 4),
    _VrNsHsaOkayFailed_Type()
)
vrNsHsaOkayFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsHsaOkayFailed.setStatus("mandatory")
_VrNsDepthExceeded_Type = Counter32
_VrNsDepthExceeded_Object = MibTableColumn
vrNsDepthExceeded = _VrNsDepthExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 5),
    _VrNsDepthExceeded_Type()
)
vrNsDepthExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDepthExceeded.setStatus("mandatory")
_VrNsDroppedStatsNoMem_Type = Counter32
_VrNsDroppedStatsNoMem_Object = MibTableColumn
vrNsDroppedStatsNoMem = _VrNsDroppedStatsNoMem_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 6),
    _VrNsDroppedStatsNoMem_Type()
)
vrNsDroppedStatsNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDroppedStatsNoMem.setStatus("mandatory")
_VrNsDroppedCantCloneTo_Type = Counter32
_VrNsDroppedCantCloneTo_Object = MibTableColumn
vrNsDroppedCantCloneTo = _VrNsDroppedCantCloneTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 7),
    _VrNsDroppedCantCloneTo_Type()
)
vrNsDroppedCantCloneTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDroppedCantCloneTo.setStatus("mandatory")
_VrNsDroppedCantLogTo_Type = Counter32
_VrNsDroppedCantLogTo_Object = MibTableColumn
vrNsDroppedCantLogTo = _VrNsDroppedCantLogTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 8),
    _VrNsDroppedCantLogTo_Type()
)
vrNsDroppedCantLogTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDroppedCantLogTo.setStatus("mandatory")
_VrNsDroppedCantCopyTo_Type = Counter32
_VrNsDroppedCantCopyTo_Object = MibTableColumn
vrNsDroppedCantCopyTo = _VrNsDroppedCantCopyTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 9),
    _VrNsDroppedCantCopyTo_Type()
)
vrNsDroppedCantCopyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDroppedCantCopyTo.setStatus("mandatory")
_VrNsDroppedNullFilter_Type = Counter32
_VrNsDroppedNullFilter_Object = MibTableColumn
vrNsDroppedNullFilter = _VrNsDroppedNullFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 4, 101, 1, 10),
    _VrNsDroppedNullFilter_Type()
)
vrNsDroppedNullFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrNsDroppedNullFilter.setStatus("mandatory")
_NetSentryMIB_ObjectIdentity = ObjectIdentity
netSentryMIB = _NetSentryMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31)
)
_NetSentryGroup_ObjectIdentity = ObjectIdentity
netSentryGroup = _NetSentryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 1)
)
_NetSentryGroupBD_ObjectIdentity = ObjectIdentity
netSentryGroupBD = _NetSentryGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 1, 4)
)
_NetSentryGroupBD00_ObjectIdentity = ObjectIdentity
netSentryGroupBD00 = _NetSentryGroupBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 1, 4, 1)
)
_NetSentryGroupBD00A_ObjectIdentity = ObjectIdentity
netSentryGroupBD00A = _NetSentryGroupBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 1, 4, 1, 2)
)
_NetSentryCapabilities_ObjectIdentity = ObjectIdentity
netSentryCapabilities = _NetSentryCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 3)
)
_NetSentryCapabilitiesBD_ObjectIdentity = ObjectIdentity
netSentryCapabilitiesBD = _NetSentryCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 3, 4)
)
_NetSentryCapabilitiesBD00_ObjectIdentity = ObjectIdentity
netSentryCapabilitiesBD00 = _NetSentryCapabilitiesBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 3, 4, 1)
)
_NetSentryCapabilitiesBD00A_ObjectIdentity = ObjectIdentity
netSentryCapabilitiesBD00A = _NetSentryCapabilitiesBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 31, 3, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-NetSentryMIB",
    **{"vrNs": vrNs,
       "vrNsRowStatusTable": vrNsRowStatusTable,
       "vrNsRowStatusEntry": vrNsRowStatusEntry,
       "vrNsRowStatus": vrNsRowStatus,
       "vrNsComponentName": vrNsComponentName,
       "vrNsStorageType": vrNsStorageType,
       "vrNsIndex": vrNsIndex,
       "vrNsFile": vrNsFile,
       "vrNsFileRowStatusTable": vrNsFileRowStatusTable,
       "vrNsFileRowStatusEntry": vrNsFileRowStatusEntry,
       "vrNsFileRowStatus": vrNsFileRowStatus,
       "vrNsFileComponentName": vrNsFileComponentName,
       "vrNsFileStorageType": vrNsFileStorageType,
       "vrNsFileIndex": vrNsFileIndex,
       "vrNsFileOperTable": vrNsFileOperTable,
       "vrNsFileOperEntry": vrNsFileOperEntry,
       "vrNsFileCompilerErrorMsg": vrNsFileCompilerErrorMsg,
       "vrNsEngine": vrNsEngine,
       "vrNsEngineRowStatusTable": vrNsEngineRowStatusTable,
       "vrNsEngineRowStatusEntry": vrNsEngineRowStatusEntry,
       "vrNsEngineRowStatus": vrNsEngineRowStatus,
       "vrNsEngineComponentName": vrNsEngineComponentName,
       "vrNsEngineStorageType": vrNsEngineStorageType,
       "vrNsEngineIndex": vrNsEngineIndex,
       "vrNsIPStats": vrNsIPStats,
       "vrNsIPStatsRowStatusTable": vrNsIPStatsRowStatusTable,
       "vrNsIPStatsRowStatusEntry": vrNsIPStatsRowStatusEntry,
       "vrNsIPStatsRowStatus": vrNsIPStatsRowStatus,
       "vrNsIPStatsComponentName": vrNsIPStatsComponentName,
       "vrNsIPStatsStorageType": vrNsIPStatsStorageType,
       "vrNsIPStatsIndex": vrNsIPStatsIndex,
       "vrNsIPStatsAddrStat": vrNsIPStatsAddrStat,
       "vrNsIPStatsAddrStatRowStatusTable": vrNsIPStatsAddrStatRowStatusTable,
       "vrNsIPStatsAddrStatRowStatusEntry": vrNsIPStatsAddrStatRowStatusEntry,
       "vrNsIPStatsAddrStatRowStatus": vrNsIPStatsAddrStatRowStatus,
       "vrNsIPStatsAddrStatComponentName": vrNsIPStatsAddrStatComponentName,
       "vrNsIPStatsAddrStatStorageType": vrNsIPStatsAddrStatStorageType,
       "vrNsIPStatsAddrStatSourceAddressIndex": vrNsIPStatsAddrStatSourceAddressIndex,
       "vrNsIPStatsAddrStatDestinationAddressIndex": vrNsIPStatsAddrStatDestinationAddressIndex,
       "vrNsIPStatsAddrStatStatsTable": vrNsIPStatsAddrStatStatsTable,
       "vrNsIPStatsAddrStatStatsEntry": vrNsIPStatsAddrStatStatsEntry,
       "vrNsIPStatsAddrStatPacketCount": vrNsIPStatsAddrStatPacketCount,
       "vrNsIPStatsAddrStatByteCount": vrNsIPStatsAddrStatByteCount,
       "vrNsIPStatsAddrStatCounter1": vrNsIPStatsAddrStatCounter1,
       "vrNsIPStatsAddrStatCounter2": vrNsIPStatsAddrStatCounter2,
       "vrNsIPXStats": vrNsIPXStats,
       "vrNsIPXStatsRowStatusTable": vrNsIPXStatsRowStatusTable,
       "vrNsIPXStatsRowStatusEntry": vrNsIPXStatsRowStatusEntry,
       "vrNsIPXStatsRowStatus": vrNsIPXStatsRowStatus,
       "vrNsIPXStatsComponentName": vrNsIPXStatsComponentName,
       "vrNsIPXStatsStorageType": vrNsIPXStatsStorageType,
       "vrNsIPXStatsIndex": vrNsIPXStatsIndex,
       "vrNsIPXStatsAddrStat": vrNsIPXStatsAddrStat,
       "vrNsIPXStatsAddrStatRowStatusTable": vrNsIPXStatsAddrStatRowStatusTable,
       "vrNsIPXStatsAddrStatRowStatusEntry": vrNsIPXStatsAddrStatRowStatusEntry,
       "vrNsIPXStatsAddrStatRowStatus": vrNsIPXStatsAddrStatRowStatus,
       "vrNsIPXStatsAddrStatComponentName": vrNsIPXStatsAddrStatComponentName,
       "vrNsIPXStatsAddrStatStorageType": vrNsIPXStatsAddrStatStorageType,
       "vrNsIPXStatsAddrStatSourceAddressIndex": vrNsIPXStatsAddrStatSourceAddressIndex,
       "vrNsIPXStatsAddrStatDestinationAddressIndex": vrNsIPXStatsAddrStatDestinationAddressIndex,
       "vrNsIPXStatsAddrStatStatsTable": vrNsIPXStatsAddrStatStatsTable,
       "vrNsIPXStatsAddrStatStatsEntry": vrNsIPXStatsAddrStatStatsEntry,
       "vrNsIPXStatsAddrStatPacketCount": vrNsIPXStatsAddrStatPacketCount,
       "vrNsIPXStatsAddrStatByteCount": vrNsIPXStatsAddrStatByteCount,
       "vrNsIPXStatsAddrStatCounter1": vrNsIPXStatsAddrStatCounter1,
       "vrNsIPXStatsAddrStatCounter2": vrNsIPXStatsAddrStatCounter2,
       "vrNsATStats": vrNsATStats,
       "vrNsATStatsRowStatusTable": vrNsATStatsRowStatusTable,
       "vrNsATStatsRowStatusEntry": vrNsATStatsRowStatusEntry,
       "vrNsATStatsRowStatus": vrNsATStatsRowStatus,
       "vrNsATStatsComponentName": vrNsATStatsComponentName,
       "vrNsATStatsStorageType": vrNsATStatsStorageType,
       "vrNsATStatsIndex": vrNsATStatsIndex,
       "vrNsATStatsAddrStat": vrNsATStatsAddrStat,
       "vrNsATStatsAddrStatRowStatusTable": vrNsATStatsAddrStatRowStatusTable,
       "vrNsATStatsAddrStatRowStatusEntry": vrNsATStatsAddrStatRowStatusEntry,
       "vrNsATStatsAddrStatRowStatus": vrNsATStatsAddrStatRowStatus,
       "vrNsATStatsAddrStatComponentName": vrNsATStatsAddrStatComponentName,
       "vrNsATStatsAddrStatStorageType": vrNsATStatsAddrStatStorageType,
       "vrNsATStatsAddrStatSourceAddressIndex": vrNsATStatsAddrStatSourceAddressIndex,
       "vrNsATStatsAddrStatDestinationAddressIndex": vrNsATStatsAddrStatDestinationAddressIndex,
       "vrNsATStatsAddrStatStatsTable": vrNsATStatsAddrStatStatsTable,
       "vrNsATStatsAddrStatStatsEntry": vrNsATStatsAddrStatStatsEntry,
       "vrNsATStatsAddrStatPacketCount": vrNsATStatsAddrStatPacketCount,
       "vrNsATStatsAddrStatByteCount": vrNsATStatsAddrStatByteCount,
       "vrNsATStatsAddrStatCounter1": vrNsATStatsAddrStatCounter1,
       "vrNsATStatsAddrStatCounter2": vrNsATStatsAddrStatCounter2,
       "vrNsDNStats": vrNsDNStats,
       "vrNsDNStatsRowStatusTable": vrNsDNStatsRowStatusTable,
       "vrNsDNStatsRowStatusEntry": vrNsDNStatsRowStatusEntry,
       "vrNsDNStatsRowStatus": vrNsDNStatsRowStatus,
       "vrNsDNStatsComponentName": vrNsDNStatsComponentName,
       "vrNsDNStatsStorageType": vrNsDNStatsStorageType,
       "vrNsDNStatsIndex": vrNsDNStatsIndex,
       "vrNsDNStatsAddrStat": vrNsDNStatsAddrStat,
       "vrNsDNStatsAddrStatRowStatusTable": vrNsDNStatsAddrStatRowStatusTable,
       "vrNsDNStatsAddrStatRowStatusEntry": vrNsDNStatsAddrStatRowStatusEntry,
       "vrNsDNStatsAddrStatRowStatus": vrNsDNStatsAddrStatRowStatus,
       "vrNsDNStatsAddrStatComponentName": vrNsDNStatsAddrStatComponentName,
       "vrNsDNStatsAddrStatStorageType": vrNsDNStatsAddrStatStorageType,
       "vrNsDNStatsAddrStatSourceAddressIndex": vrNsDNStatsAddrStatSourceAddressIndex,
       "vrNsDNStatsAddrStatDestinationAddressIndex": vrNsDNStatsAddrStatDestinationAddressIndex,
       "vrNsDNStatsAddrStatStatsTable": vrNsDNStatsAddrStatStatsTable,
       "vrNsDNStatsAddrStatStatsEntry": vrNsDNStatsAddrStatStatsEntry,
       "vrNsDNStatsAddrStatPacketCount": vrNsDNStatsAddrStatPacketCount,
       "vrNsDNStatsAddrStatByteCount": vrNsDNStatsAddrStatByteCount,
       "vrNsDNStatsAddrStatCounter1": vrNsDNStatsAddrStatCounter1,
       "vrNsDNStatsAddrStatCounter2": vrNsDNStatsAddrStatCounter2,
       "vrNsBrStats": vrNsBrStats,
       "vrNsBrStatsRowStatusTable": vrNsBrStatsRowStatusTable,
       "vrNsBrStatsRowStatusEntry": vrNsBrStatsRowStatusEntry,
       "vrNsBrStatsRowStatus": vrNsBrStatsRowStatus,
       "vrNsBrStatsComponentName": vrNsBrStatsComponentName,
       "vrNsBrStatsStorageType": vrNsBrStatsStorageType,
       "vrNsBrStatsIndex": vrNsBrStatsIndex,
       "vrNsBrStatsAddrStat": vrNsBrStatsAddrStat,
       "vrNsBrStatsAddrStatRowStatusTable": vrNsBrStatsAddrStatRowStatusTable,
       "vrNsBrStatsAddrStatRowStatusEntry": vrNsBrStatsAddrStatRowStatusEntry,
       "vrNsBrStatsAddrStatRowStatus": vrNsBrStatsAddrStatRowStatus,
       "vrNsBrStatsAddrStatComponentName": vrNsBrStatsAddrStatComponentName,
       "vrNsBrStatsAddrStatStorageType": vrNsBrStatsAddrStatStorageType,
       "vrNsBrStatsAddrStatSourceAddressIndex": vrNsBrStatsAddrStatSourceAddressIndex,
       "vrNsBrStatsAddrStatDestinationAddressIndex": vrNsBrStatsAddrStatDestinationAddressIndex,
       "vrNsBrStatsAddrStatStatsTable": vrNsBrStatsAddrStatStatsTable,
       "vrNsBrStatsAddrStatStatsEntry": vrNsBrStatsAddrStatStatsEntry,
       "vrNsBrStatsAddrStatPacketCount": vrNsBrStatsAddrStatPacketCount,
       "vrNsBrStatsAddrStatByteCount": vrNsBrStatsAddrStatByteCount,
       "vrNsBrStatsAddrStatCounter1": vrNsBrStatsAddrStatCounter1,
       "vrNsBrStatsAddrStatCounter2": vrNsBrStatsAddrStatCounter2,
       "vrNsFilter": vrNsFilter,
       "vrNsFilterRowStatusTable": vrNsFilterRowStatusTable,
       "vrNsFilterRowStatusEntry": vrNsFilterRowStatusEntry,
       "vrNsFilterRowStatus": vrNsFilterRowStatus,
       "vrNsFilterComponentName": vrNsFilterComponentName,
       "vrNsFilterStorageType": vrNsFilterStorageType,
       "vrNsFilterNameIndex": vrNsFilterNameIndex,
       "vrNsFilterKindIndex": vrNsFilterKindIndex,
       "vrNsFilterStatsTable": vrNsFilterStatsTable,
       "vrNsFilterStatsEntry": vrNsFilterStatsEntry,
       "vrNsFilterPacketsSucceeded": vrNsFilterPacketsSucceeded,
       "vrNsFilterBytesSucceeded": vrNsFilterBytesSucceeded,
       "vrNsFilterPacketsFailed": vrNsFilterPacketsFailed,
       "vrNsFilterBytesFailed": vrNsFilterBytesFailed,
       "vrNsFilterPacketsBreaked": vrNsFilterPacketsBreaked,
       "vrNsFilterBytesBreaked": vrNsFilterBytesBreaked,
       "vrNsFilterPacketsContinued": vrNsFilterPacketsContinued,
       "vrNsFilterBytesContinued": vrNsFilterBytesContinued,
       "vrNsProvTable": vrNsProvTable,
       "vrNsProvEntry": vrNsProvEntry,
       "vrNsDropConditions": vrNsDropConditions,
       "vrNsStatsTable": vrNsStatsTable,
       "vrNsStatsEntry": vrNsStatsEntry,
       "vrNsPacketsProcessed": vrNsPacketsProcessed,
       "vrNsPacketsFailed": vrNsPacketsFailed,
       "vrNsStatsNoMem": vrNsStatsNoMem,
       "vrNsHsaOkayFailed": vrNsHsaOkayFailed,
       "vrNsDepthExceeded": vrNsDepthExceeded,
       "vrNsDroppedStatsNoMem": vrNsDroppedStatsNoMem,
       "vrNsDroppedCantCloneTo": vrNsDroppedCantCloneTo,
       "vrNsDroppedCantLogTo": vrNsDroppedCantLogTo,
       "vrNsDroppedCantCopyTo": vrNsDroppedCantCopyTo,
       "vrNsDroppedNullFilter": vrNsDroppedNullFilter,
       "netSentryMIB": netSentryMIB,
       "netSentryGroup": netSentryGroup,
       "netSentryGroupBD": netSentryGroupBD,
       "netSentryGroupBD00": netSentryGroupBD00,
       "netSentryGroupBD00A": netSentryGroupBD00A,
       "netSentryCapabilities": netSentryCapabilities,
       "netSentryCapabilitiesBD": netSentryCapabilitiesBD,
       "netSentryCapabilitiesBD00": netSentryCapabilitiesBD00,
       "netSentryCapabilitiesBD00A": netSentryCapabilitiesBD00A}
)
