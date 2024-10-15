# SNMP MIB module (Nortel-MsCarrier-MscPassport-NetSentryMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-NetSentryMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:53 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType")

(AsciiString,
 AsciiStringIndex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "AsciiStringIndex",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVr,
 mscVrIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVr",
    "mscVrIndex")

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

_MscVrNs_ObjectIdentity = ObjectIdentity
mscVrNs = _MscVrNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4)
)
_MscVrNsRowStatusTable_Object = MibTable
mscVrNsRowStatusTable = _MscVrNsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrNsRowStatusTable.setStatus("mandatory")
_MscVrNsRowStatusEntry_Object = MibTableRow
mscVrNsRowStatusEntry = _MscVrNsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 1, 1)
)
mscVrNsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsRowStatusEntry.setStatus("mandatory")
_MscVrNsRowStatus_Type = RowStatus
_MscVrNsRowStatus_Object = MibTableColumn
mscVrNsRowStatus = _MscVrNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 1, 1, 1),
    _MscVrNsRowStatus_Type()
)
mscVrNsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsRowStatus.setStatus("mandatory")
_MscVrNsComponentName_Type = DisplayString
_MscVrNsComponentName_Object = MibTableColumn
mscVrNsComponentName = _MscVrNsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 1, 1, 2),
    _MscVrNsComponentName_Type()
)
mscVrNsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsComponentName.setStatus("mandatory")
_MscVrNsStorageType_Type = StorageType
_MscVrNsStorageType_Object = MibTableColumn
mscVrNsStorageType = _MscVrNsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 1, 1, 4),
    _MscVrNsStorageType_Type()
)
mscVrNsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsStorageType.setStatus("mandatory")
_MscVrNsIndex_Type = NonReplicated
_MscVrNsIndex_Object = MibTableColumn
mscVrNsIndex = _MscVrNsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 1, 1, 10),
    _MscVrNsIndex_Type()
)
mscVrNsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsIndex.setStatus("mandatory")
_MscVrNsFile_ObjectIdentity = ObjectIdentity
mscVrNsFile = _MscVrNsFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2)
)
_MscVrNsFileRowStatusTable_Object = MibTable
mscVrNsFileRowStatusTable = _MscVrNsFileRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrNsFileRowStatusTable.setStatus("mandatory")
_MscVrNsFileRowStatusEntry_Object = MibTableRow
mscVrNsFileRowStatusEntry = _MscVrNsFileRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 1, 1)
)
mscVrNsFileRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsFileIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsFileRowStatusEntry.setStatus("mandatory")
_MscVrNsFileRowStatus_Type = RowStatus
_MscVrNsFileRowStatus_Object = MibTableColumn
mscVrNsFileRowStatus = _MscVrNsFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 1, 1, 1),
    _MscVrNsFileRowStatus_Type()
)
mscVrNsFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsFileRowStatus.setStatus("mandatory")
_MscVrNsFileComponentName_Type = DisplayString
_MscVrNsFileComponentName_Object = MibTableColumn
mscVrNsFileComponentName = _MscVrNsFileComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 1, 1, 2),
    _MscVrNsFileComponentName_Type()
)
mscVrNsFileComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFileComponentName.setStatus("mandatory")
_MscVrNsFileStorageType_Type = StorageType
_MscVrNsFileStorageType_Object = MibTableColumn
mscVrNsFileStorageType = _MscVrNsFileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 1, 1, 4),
    _MscVrNsFileStorageType_Type()
)
mscVrNsFileStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFileStorageType.setStatus("mandatory")


class _MscVrNsFileIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsFileIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MscVrNsFileIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsFileIndex_Object = MibTableColumn
mscVrNsFileIndex = _MscVrNsFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 1, 1, 10),
    _MscVrNsFileIndex_Type()
)
mscVrNsFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsFileIndex.setStatus("mandatory")
_MscVrNsFileOperTable_Object = MibTable
mscVrNsFileOperTable = _MscVrNsFileOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrNsFileOperTable.setStatus("mandatory")
_MscVrNsFileOperEntry_Object = MibTableRow
mscVrNsFileOperEntry = _MscVrNsFileOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 10, 1)
)
mscVrNsFileOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsFileIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsFileOperEntry.setStatus("mandatory")


class _MscVrNsFileCompilerErrorMsg_Type(AsciiString):
    """Custom type mscVrNsFileCompilerErrorMsg based on AsciiString"""
    defaultHexValue = "4e6f204572726f72"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MscVrNsFileCompilerErrorMsg_Type.__name__ = "AsciiString"
_MscVrNsFileCompilerErrorMsg_Object = MibTableColumn
mscVrNsFileCompilerErrorMsg = _MscVrNsFileCompilerErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 2, 10, 1, 1),
    _MscVrNsFileCompilerErrorMsg_Type()
)
mscVrNsFileCompilerErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFileCompilerErrorMsg.setStatus("mandatory")
_MscVrNsEngine_ObjectIdentity = ObjectIdentity
mscVrNsEngine = _MscVrNsEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 3)
)
_MscVrNsEngineRowStatusTable_Object = MibTable
mscVrNsEngineRowStatusTable = _MscVrNsEngineRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrNsEngineRowStatusTable.setStatus("mandatory")
_MscVrNsEngineRowStatusEntry_Object = MibTableRow
mscVrNsEngineRowStatusEntry = _MscVrNsEngineRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 3, 1, 1)
)
mscVrNsEngineRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsEngineIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsEngineRowStatusEntry.setStatus("mandatory")
_MscVrNsEngineRowStatus_Type = RowStatus
_MscVrNsEngineRowStatus_Object = MibTableColumn
mscVrNsEngineRowStatus = _MscVrNsEngineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 3, 1, 1, 1),
    _MscVrNsEngineRowStatus_Type()
)
mscVrNsEngineRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsEngineRowStatus.setStatus("mandatory")
_MscVrNsEngineComponentName_Type = DisplayString
_MscVrNsEngineComponentName_Object = MibTableColumn
mscVrNsEngineComponentName = _MscVrNsEngineComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 3, 1, 1, 2),
    _MscVrNsEngineComponentName_Type()
)
mscVrNsEngineComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsEngineComponentName.setStatus("mandatory")
_MscVrNsEngineStorageType_Type = StorageType
_MscVrNsEngineStorageType_Object = MibTableColumn
mscVrNsEngineStorageType = _MscVrNsEngineStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 3, 1, 1, 4),
    _MscVrNsEngineStorageType_Type()
)
mscVrNsEngineStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsEngineStorageType.setStatus("mandatory")


class _MscVrNsEngineIndex_Type(Integer32):
    """Custom type mscVrNsEngineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVrNsEngineIndex_Type.__name__ = "Integer32"
_MscVrNsEngineIndex_Object = MibTableColumn
mscVrNsEngineIndex = _MscVrNsEngineIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 3, 1, 1, 10),
    _MscVrNsEngineIndex_Type()
)
mscVrNsEngineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsEngineIndex.setStatus("mandatory")
_MscVrNsIPStats_ObjectIdentity = ObjectIdentity
mscVrNsIPStats = _MscVrNsIPStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4)
)
_MscVrNsIPStatsRowStatusTable_Object = MibTable
mscVrNsIPStatsRowStatusTable = _MscVrNsIPStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrNsIPStatsRowStatusTable.setStatus("mandatory")
_MscVrNsIPStatsRowStatusEntry_Object = MibTableRow
mscVrNsIPStatsRowStatusEntry = _MscVrNsIPStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 1, 1)
)
mscVrNsIPStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPStatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsIPStatsRowStatusEntry.setStatus("mandatory")
_MscVrNsIPStatsRowStatus_Type = RowStatus
_MscVrNsIPStatsRowStatus_Object = MibTableColumn
mscVrNsIPStatsRowStatus = _MscVrNsIPStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 1, 1, 1),
    _MscVrNsIPStatsRowStatus_Type()
)
mscVrNsIPStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsIPStatsRowStatus.setStatus("mandatory")
_MscVrNsIPStatsComponentName_Type = DisplayString
_MscVrNsIPStatsComponentName_Object = MibTableColumn
mscVrNsIPStatsComponentName = _MscVrNsIPStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 1, 1, 2),
    _MscVrNsIPStatsComponentName_Type()
)
mscVrNsIPStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsComponentName.setStatus("mandatory")
_MscVrNsIPStatsStorageType_Type = StorageType
_MscVrNsIPStatsStorageType_Object = MibTableColumn
mscVrNsIPStatsStorageType = _MscVrNsIPStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 1, 1, 4),
    _MscVrNsIPStatsStorageType_Type()
)
mscVrNsIPStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsStorageType.setStatus("mandatory")
_MscVrNsIPStatsIndex_Type = NonReplicated
_MscVrNsIPStatsIndex_Object = MibTableColumn
mscVrNsIPStatsIndex = _MscVrNsIPStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 1, 1, 10),
    _MscVrNsIPStatsIndex_Type()
)
mscVrNsIPStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsIPStatsIndex.setStatus("mandatory")
_MscVrNsIPStatsAddrStat_ObjectIdentity = ObjectIdentity
mscVrNsIPStatsAddrStat = _MscVrNsIPStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2)
)
_MscVrNsIPStatsAddrStatRowStatusTable_Object = MibTable
mscVrNsIPStatsAddrStatRowStatusTable = _MscVrNsIPStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatRowStatusTable.setStatus("mandatory")
_MscVrNsIPStatsAddrStatRowStatusEntry_Object = MibTableRow
mscVrNsIPStatsAddrStatRowStatusEntry = _MscVrNsIPStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 1, 1)
)
mscVrNsIPStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatRowStatusEntry.setStatus("mandatory")
_MscVrNsIPStatsAddrStatRowStatus_Type = RowStatus
_MscVrNsIPStatsAddrStatRowStatus_Object = MibTableColumn
mscVrNsIPStatsAddrStatRowStatus = _MscVrNsIPStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 1, 1, 1),
    _MscVrNsIPStatsAddrStatRowStatus_Type()
)
mscVrNsIPStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatRowStatus.setStatus("mandatory")
_MscVrNsIPStatsAddrStatComponentName_Type = DisplayString
_MscVrNsIPStatsAddrStatComponentName_Object = MibTableColumn
mscVrNsIPStatsAddrStatComponentName = _MscVrNsIPStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 1, 1, 2),
    _MscVrNsIPStatsAddrStatComponentName_Type()
)
mscVrNsIPStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatComponentName.setStatus("mandatory")
_MscVrNsIPStatsAddrStatStorageType_Type = StorageType
_MscVrNsIPStatsAddrStatStorageType_Object = MibTableColumn
mscVrNsIPStatsAddrStatStorageType = _MscVrNsIPStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 1, 1, 4),
    _MscVrNsIPStatsAddrStatStorageType_Type()
)
mscVrNsIPStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatStorageType.setStatus("mandatory")


class _MscVrNsIPStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsIPStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsIPStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsIPStatsAddrStatSourceAddressIndex_Object = MibTableColumn
mscVrNsIPStatsAddrStatSourceAddressIndex = _MscVrNsIPStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 1, 1, 10),
    _MscVrNsIPStatsAddrStatSourceAddressIndex_Type()
)
mscVrNsIPStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _MscVrNsIPStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsIPStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsIPStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsIPStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
mscVrNsIPStatsAddrStatDestinationAddressIndex = _MscVrNsIPStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 1, 1, 11),
    _MscVrNsIPStatsAddrStatDestinationAddressIndex_Type()
)
mscVrNsIPStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_MscVrNsIPStatsAddrStatStatsTable_Object = MibTable
mscVrNsIPStatsAddrStatStatsTable = _MscVrNsIPStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatStatsTable.setStatus("mandatory")
_MscVrNsIPStatsAddrStatStatsEntry_Object = MibTableRow
mscVrNsIPStatsAddrStatStatsEntry = _MscVrNsIPStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 10, 1)
)
mscVrNsIPStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatStatsEntry.setStatus("mandatory")
_MscVrNsIPStatsAddrStatPacketCount_Type = Counter32
_MscVrNsIPStatsAddrStatPacketCount_Object = MibTableColumn
mscVrNsIPStatsAddrStatPacketCount = _MscVrNsIPStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 10, 1, 1),
    _MscVrNsIPStatsAddrStatPacketCount_Type()
)
mscVrNsIPStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatPacketCount.setStatus("mandatory")
_MscVrNsIPStatsAddrStatByteCount_Type = Counter32
_MscVrNsIPStatsAddrStatByteCount_Object = MibTableColumn
mscVrNsIPStatsAddrStatByteCount = _MscVrNsIPStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 10, 1, 2),
    _MscVrNsIPStatsAddrStatByteCount_Type()
)
mscVrNsIPStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatByteCount.setStatus("mandatory")
_MscVrNsIPStatsAddrStatCounter1_Type = Counter32
_MscVrNsIPStatsAddrStatCounter1_Object = MibTableColumn
mscVrNsIPStatsAddrStatCounter1 = _MscVrNsIPStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 10, 1, 3),
    _MscVrNsIPStatsAddrStatCounter1_Type()
)
mscVrNsIPStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatCounter1.setStatus("mandatory")
_MscVrNsIPStatsAddrStatCounter2_Type = Counter32
_MscVrNsIPStatsAddrStatCounter2_Object = MibTableColumn
mscVrNsIPStatsAddrStatCounter2 = _MscVrNsIPStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 4, 2, 10, 1, 4),
    _MscVrNsIPStatsAddrStatCounter2_Type()
)
mscVrNsIPStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPStatsAddrStatCounter2.setStatus("mandatory")
_MscVrNsIPXStats_ObjectIdentity = ObjectIdentity
mscVrNsIPXStats = _MscVrNsIPXStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5)
)
_MscVrNsIPXStatsRowStatusTable_Object = MibTable
mscVrNsIPXStatsRowStatusTable = _MscVrNsIPXStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrNsIPXStatsRowStatusTable.setStatus("mandatory")
_MscVrNsIPXStatsRowStatusEntry_Object = MibTableRow
mscVrNsIPXStatsRowStatusEntry = _MscVrNsIPXStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 1, 1)
)
mscVrNsIPXStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPXStatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsIPXStatsRowStatusEntry.setStatus("mandatory")
_MscVrNsIPXStatsRowStatus_Type = RowStatus
_MscVrNsIPXStatsRowStatus_Object = MibTableColumn
mscVrNsIPXStatsRowStatus = _MscVrNsIPXStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 1, 1, 1),
    _MscVrNsIPXStatsRowStatus_Type()
)
mscVrNsIPXStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsRowStatus.setStatus("mandatory")
_MscVrNsIPXStatsComponentName_Type = DisplayString
_MscVrNsIPXStatsComponentName_Object = MibTableColumn
mscVrNsIPXStatsComponentName = _MscVrNsIPXStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 1, 1, 2),
    _MscVrNsIPXStatsComponentName_Type()
)
mscVrNsIPXStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsComponentName.setStatus("mandatory")
_MscVrNsIPXStatsStorageType_Type = StorageType
_MscVrNsIPXStatsStorageType_Object = MibTableColumn
mscVrNsIPXStatsStorageType = _MscVrNsIPXStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 1, 1, 4),
    _MscVrNsIPXStatsStorageType_Type()
)
mscVrNsIPXStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsStorageType.setStatus("mandatory")
_MscVrNsIPXStatsIndex_Type = NonReplicated
_MscVrNsIPXStatsIndex_Object = MibTableColumn
mscVrNsIPXStatsIndex = _MscVrNsIPXStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 1, 1, 10),
    _MscVrNsIPXStatsIndex_Type()
)
mscVrNsIPXStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsIndex.setStatus("mandatory")
_MscVrNsIPXStatsAddrStat_ObjectIdentity = ObjectIdentity
mscVrNsIPXStatsAddrStat = _MscVrNsIPXStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2)
)
_MscVrNsIPXStatsAddrStatRowStatusTable_Object = MibTable
mscVrNsIPXStatsAddrStatRowStatusTable = _MscVrNsIPXStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatRowStatusTable.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatRowStatusEntry_Object = MibTableRow
mscVrNsIPXStatsAddrStatRowStatusEntry = _MscVrNsIPXStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 1, 1)
)
mscVrNsIPXStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPXStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPXStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPXStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatRowStatusEntry.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatRowStatus_Type = RowStatus
_MscVrNsIPXStatsAddrStatRowStatus_Object = MibTableColumn
mscVrNsIPXStatsAddrStatRowStatus = _MscVrNsIPXStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 1, 1, 1),
    _MscVrNsIPXStatsAddrStatRowStatus_Type()
)
mscVrNsIPXStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatRowStatus.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatComponentName_Type = DisplayString
_MscVrNsIPXStatsAddrStatComponentName_Object = MibTableColumn
mscVrNsIPXStatsAddrStatComponentName = _MscVrNsIPXStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 1, 1, 2),
    _MscVrNsIPXStatsAddrStatComponentName_Type()
)
mscVrNsIPXStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatComponentName.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatStorageType_Type = StorageType
_MscVrNsIPXStatsAddrStatStorageType_Object = MibTableColumn
mscVrNsIPXStatsAddrStatStorageType = _MscVrNsIPXStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 1, 1, 4),
    _MscVrNsIPXStatsAddrStatStorageType_Type()
)
mscVrNsIPXStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatStorageType.setStatus("mandatory")


class _MscVrNsIPXStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsIPXStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsIPXStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsIPXStatsAddrStatSourceAddressIndex_Object = MibTableColumn
mscVrNsIPXStatsAddrStatSourceAddressIndex = _MscVrNsIPXStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 1, 1, 10),
    _MscVrNsIPXStatsAddrStatSourceAddressIndex_Type()
)
mscVrNsIPXStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _MscVrNsIPXStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsIPXStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsIPXStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsIPXStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
mscVrNsIPXStatsAddrStatDestinationAddressIndex = _MscVrNsIPXStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 1, 1, 11),
    _MscVrNsIPXStatsAddrStatDestinationAddressIndex_Type()
)
mscVrNsIPXStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatStatsTable_Object = MibTable
mscVrNsIPXStatsAddrStatStatsTable = _MscVrNsIPXStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatStatsTable.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatStatsEntry_Object = MibTableRow
mscVrNsIPXStatsAddrStatStatsEntry = _MscVrNsIPXStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 10, 1)
)
mscVrNsIPXStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPXStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPXStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIPXStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatStatsEntry.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatPacketCount_Type = Counter32
_MscVrNsIPXStatsAddrStatPacketCount_Object = MibTableColumn
mscVrNsIPXStatsAddrStatPacketCount = _MscVrNsIPXStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 10, 1, 1),
    _MscVrNsIPXStatsAddrStatPacketCount_Type()
)
mscVrNsIPXStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatPacketCount.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatByteCount_Type = Counter32
_MscVrNsIPXStatsAddrStatByteCount_Object = MibTableColumn
mscVrNsIPXStatsAddrStatByteCount = _MscVrNsIPXStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 10, 1, 2),
    _MscVrNsIPXStatsAddrStatByteCount_Type()
)
mscVrNsIPXStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatByteCount.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatCounter1_Type = Counter32
_MscVrNsIPXStatsAddrStatCounter1_Object = MibTableColumn
mscVrNsIPXStatsAddrStatCounter1 = _MscVrNsIPXStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 10, 1, 3),
    _MscVrNsIPXStatsAddrStatCounter1_Type()
)
mscVrNsIPXStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatCounter1.setStatus("mandatory")
_MscVrNsIPXStatsAddrStatCounter2_Type = Counter32
_MscVrNsIPXStatsAddrStatCounter2_Object = MibTableColumn
mscVrNsIPXStatsAddrStatCounter2 = _MscVrNsIPXStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 5, 2, 10, 1, 4),
    _MscVrNsIPXStatsAddrStatCounter2_Type()
)
mscVrNsIPXStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsIPXStatsAddrStatCounter2.setStatus("mandatory")
_MscVrNsATStats_ObjectIdentity = ObjectIdentity
mscVrNsATStats = _MscVrNsATStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6)
)
_MscVrNsATStatsRowStatusTable_Object = MibTable
mscVrNsATStatsRowStatusTable = _MscVrNsATStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrNsATStatsRowStatusTable.setStatus("mandatory")
_MscVrNsATStatsRowStatusEntry_Object = MibTableRow
mscVrNsATStatsRowStatusEntry = _MscVrNsATStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 1, 1)
)
mscVrNsATStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsATStatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsATStatsRowStatusEntry.setStatus("mandatory")
_MscVrNsATStatsRowStatus_Type = RowStatus
_MscVrNsATStatsRowStatus_Object = MibTableColumn
mscVrNsATStatsRowStatus = _MscVrNsATStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 1, 1, 1),
    _MscVrNsATStatsRowStatus_Type()
)
mscVrNsATStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsATStatsRowStatus.setStatus("mandatory")
_MscVrNsATStatsComponentName_Type = DisplayString
_MscVrNsATStatsComponentName_Object = MibTableColumn
mscVrNsATStatsComponentName = _MscVrNsATStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 1, 1, 2),
    _MscVrNsATStatsComponentName_Type()
)
mscVrNsATStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsComponentName.setStatus("mandatory")
_MscVrNsATStatsStorageType_Type = StorageType
_MscVrNsATStatsStorageType_Object = MibTableColumn
mscVrNsATStatsStorageType = _MscVrNsATStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 1, 1, 4),
    _MscVrNsATStatsStorageType_Type()
)
mscVrNsATStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsStorageType.setStatus("mandatory")
_MscVrNsATStatsIndex_Type = NonReplicated
_MscVrNsATStatsIndex_Object = MibTableColumn
mscVrNsATStatsIndex = _MscVrNsATStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 1, 1, 10),
    _MscVrNsATStatsIndex_Type()
)
mscVrNsATStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsATStatsIndex.setStatus("mandatory")
_MscVrNsATStatsAddrStat_ObjectIdentity = ObjectIdentity
mscVrNsATStatsAddrStat = _MscVrNsATStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2)
)
_MscVrNsATStatsAddrStatRowStatusTable_Object = MibTable
mscVrNsATStatsAddrStatRowStatusTable = _MscVrNsATStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatRowStatusTable.setStatus("mandatory")
_MscVrNsATStatsAddrStatRowStatusEntry_Object = MibTableRow
mscVrNsATStatsAddrStatRowStatusEntry = _MscVrNsATStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 1, 1)
)
mscVrNsATStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsATStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsATStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsATStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatRowStatusEntry.setStatus("mandatory")
_MscVrNsATStatsAddrStatRowStatus_Type = RowStatus
_MscVrNsATStatsAddrStatRowStatus_Object = MibTableColumn
mscVrNsATStatsAddrStatRowStatus = _MscVrNsATStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 1, 1, 1),
    _MscVrNsATStatsAddrStatRowStatus_Type()
)
mscVrNsATStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatRowStatus.setStatus("mandatory")
_MscVrNsATStatsAddrStatComponentName_Type = DisplayString
_MscVrNsATStatsAddrStatComponentName_Object = MibTableColumn
mscVrNsATStatsAddrStatComponentName = _MscVrNsATStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 1, 1, 2),
    _MscVrNsATStatsAddrStatComponentName_Type()
)
mscVrNsATStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatComponentName.setStatus("mandatory")
_MscVrNsATStatsAddrStatStorageType_Type = StorageType
_MscVrNsATStatsAddrStatStorageType_Object = MibTableColumn
mscVrNsATStatsAddrStatStorageType = _MscVrNsATStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 1, 1, 4),
    _MscVrNsATStatsAddrStatStorageType_Type()
)
mscVrNsATStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatStorageType.setStatus("mandatory")


class _MscVrNsATStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsATStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsATStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsATStatsAddrStatSourceAddressIndex_Object = MibTableColumn
mscVrNsATStatsAddrStatSourceAddressIndex = _MscVrNsATStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 1, 1, 10),
    _MscVrNsATStatsAddrStatSourceAddressIndex_Type()
)
mscVrNsATStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _MscVrNsATStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsATStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsATStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsATStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
mscVrNsATStatsAddrStatDestinationAddressIndex = _MscVrNsATStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 1, 1, 11),
    _MscVrNsATStatsAddrStatDestinationAddressIndex_Type()
)
mscVrNsATStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_MscVrNsATStatsAddrStatStatsTable_Object = MibTable
mscVrNsATStatsAddrStatStatsTable = _MscVrNsATStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatStatsTable.setStatus("mandatory")
_MscVrNsATStatsAddrStatStatsEntry_Object = MibTableRow
mscVrNsATStatsAddrStatStatsEntry = _MscVrNsATStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 10, 1)
)
mscVrNsATStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsATStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsATStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsATStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatStatsEntry.setStatus("mandatory")
_MscVrNsATStatsAddrStatPacketCount_Type = Counter32
_MscVrNsATStatsAddrStatPacketCount_Object = MibTableColumn
mscVrNsATStatsAddrStatPacketCount = _MscVrNsATStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 10, 1, 1),
    _MscVrNsATStatsAddrStatPacketCount_Type()
)
mscVrNsATStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatPacketCount.setStatus("mandatory")
_MscVrNsATStatsAddrStatByteCount_Type = Counter32
_MscVrNsATStatsAddrStatByteCount_Object = MibTableColumn
mscVrNsATStatsAddrStatByteCount = _MscVrNsATStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 10, 1, 2),
    _MscVrNsATStatsAddrStatByteCount_Type()
)
mscVrNsATStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatByteCount.setStatus("mandatory")
_MscVrNsATStatsAddrStatCounter1_Type = Counter32
_MscVrNsATStatsAddrStatCounter1_Object = MibTableColumn
mscVrNsATStatsAddrStatCounter1 = _MscVrNsATStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 10, 1, 3),
    _MscVrNsATStatsAddrStatCounter1_Type()
)
mscVrNsATStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatCounter1.setStatus("mandatory")
_MscVrNsATStatsAddrStatCounter2_Type = Counter32
_MscVrNsATStatsAddrStatCounter2_Object = MibTableColumn
mscVrNsATStatsAddrStatCounter2 = _MscVrNsATStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 6, 2, 10, 1, 4),
    _MscVrNsATStatsAddrStatCounter2_Type()
)
mscVrNsATStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsATStatsAddrStatCounter2.setStatus("mandatory")
_MscVrNsDNStats_ObjectIdentity = ObjectIdentity
mscVrNsDNStats = _MscVrNsDNStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7)
)
_MscVrNsDNStatsRowStatusTable_Object = MibTable
mscVrNsDNStatsRowStatusTable = _MscVrNsDNStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 1)
)
if mibBuilder.loadTexts:
    mscVrNsDNStatsRowStatusTable.setStatus("mandatory")
_MscVrNsDNStatsRowStatusEntry_Object = MibTableRow
mscVrNsDNStatsRowStatusEntry = _MscVrNsDNStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 1, 1)
)
mscVrNsDNStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsDNStatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsDNStatsRowStatusEntry.setStatus("mandatory")
_MscVrNsDNStatsRowStatus_Type = RowStatus
_MscVrNsDNStatsRowStatus_Object = MibTableColumn
mscVrNsDNStatsRowStatus = _MscVrNsDNStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 1, 1, 1),
    _MscVrNsDNStatsRowStatus_Type()
)
mscVrNsDNStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsDNStatsRowStatus.setStatus("mandatory")
_MscVrNsDNStatsComponentName_Type = DisplayString
_MscVrNsDNStatsComponentName_Object = MibTableColumn
mscVrNsDNStatsComponentName = _MscVrNsDNStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 1, 1, 2),
    _MscVrNsDNStatsComponentName_Type()
)
mscVrNsDNStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsComponentName.setStatus("mandatory")
_MscVrNsDNStatsStorageType_Type = StorageType
_MscVrNsDNStatsStorageType_Object = MibTableColumn
mscVrNsDNStatsStorageType = _MscVrNsDNStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 1, 1, 4),
    _MscVrNsDNStatsStorageType_Type()
)
mscVrNsDNStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsStorageType.setStatus("mandatory")
_MscVrNsDNStatsIndex_Type = NonReplicated
_MscVrNsDNStatsIndex_Object = MibTableColumn
mscVrNsDNStatsIndex = _MscVrNsDNStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 1, 1, 10),
    _MscVrNsDNStatsIndex_Type()
)
mscVrNsDNStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsDNStatsIndex.setStatus("mandatory")
_MscVrNsDNStatsAddrStat_ObjectIdentity = ObjectIdentity
mscVrNsDNStatsAddrStat = _MscVrNsDNStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2)
)
_MscVrNsDNStatsAddrStatRowStatusTable_Object = MibTable
mscVrNsDNStatsAddrStatRowStatusTable = _MscVrNsDNStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatRowStatusTable.setStatus("mandatory")
_MscVrNsDNStatsAddrStatRowStatusEntry_Object = MibTableRow
mscVrNsDNStatsAddrStatRowStatusEntry = _MscVrNsDNStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 1, 1)
)
mscVrNsDNStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsDNStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsDNStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsDNStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatRowStatusEntry.setStatus("mandatory")
_MscVrNsDNStatsAddrStatRowStatus_Type = RowStatus
_MscVrNsDNStatsAddrStatRowStatus_Object = MibTableColumn
mscVrNsDNStatsAddrStatRowStatus = _MscVrNsDNStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 1, 1, 1),
    _MscVrNsDNStatsAddrStatRowStatus_Type()
)
mscVrNsDNStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatRowStatus.setStatus("mandatory")
_MscVrNsDNStatsAddrStatComponentName_Type = DisplayString
_MscVrNsDNStatsAddrStatComponentName_Object = MibTableColumn
mscVrNsDNStatsAddrStatComponentName = _MscVrNsDNStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 1, 1, 2),
    _MscVrNsDNStatsAddrStatComponentName_Type()
)
mscVrNsDNStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatComponentName.setStatus("mandatory")
_MscVrNsDNStatsAddrStatStorageType_Type = StorageType
_MscVrNsDNStatsAddrStatStorageType_Object = MibTableColumn
mscVrNsDNStatsAddrStatStorageType = _MscVrNsDNStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 1, 1, 4),
    _MscVrNsDNStatsAddrStatStorageType_Type()
)
mscVrNsDNStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatStorageType.setStatus("mandatory")


class _MscVrNsDNStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsDNStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsDNStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsDNStatsAddrStatSourceAddressIndex_Object = MibTableColumn
mscVrNsDNStatsAddrStatSourceAddressIndex = _MscVrNsDNStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 1, 1, 10),
    _MscVrNsDNStatsAddrStatSourceAddressIndex_Type()
)
mscVrNsDNStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _MscVrNsDNStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsDNStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsDNStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsDNStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
mscVrNsDNStatsAddrStatDestinationAddressIndex = _MscVrNsDNStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 1, 1, 11),
    _MscVrNsDNStatsAddrStatDestinationAddressIndex_Type()
)
mscVrNsDNStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_MscVrNsDNStatsAddrStatStatsTable_Object = MibTable
mscVrNsDNStatsAddrStatStatsTable = _MscVrNsDNStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatStatsTable.setStatus("mandatory")
_MscVrNsDNStatsAddrStatStatsEntry_Object = MibTableRow
mscVrNsDNStatsAddrStatStatsEntry = _MscVrNsDNStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 10, 1)
)
mscVrNsDNStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsDNStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsDNStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsDNStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatStatsEntry.setStatus("mandatory")
_MscVrNsDNStatsAddrStatPacketCount_Type = Counter32
_MscVrNsDNStatsAddrStatPacketCount_Object = MibTableColumn
mscVrNsDNStatsAddrStatPacketCount = _MscVrNsDNStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 10, 1, 1),
    _MscVrNsDNStatsAddrStatPacketCount_Type()
)
mscVrNsDNStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatPacketCount.setStatus("mandatory")
_MscVrNsDNStatsAddrStatByteCount_Type = Counter32
_MscVrNsDNStatsAddrStatByteCount_Object = MibTableColumn
mscVrNsDNStatsAddrStatByteCount = _MscVrNsDNStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 10, 1, 2),
    _MscVrNsDNStatsAddrStatByteCount_Type()
)
mscVrNsDNStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatByteCount.setStatus("mandatory")
_MscVrNsDNStatsAddrStatCounter1_Type = Counter32
_MscVrNsDNStatsAddrStatCounter1_Object = MibTableColumn
mscVrNsDNStatsAddrStatCounter1 = _MscVrNsDNStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 10, 1, 3),
    _MscVrNsDNStatsAddrStatCounter1_Type()
)
mscVrNsDNStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatCounter1.setStatus("mandatory")
_MscVrNsDNStatsAddrStatCounter2_Type = Counter32
_MscVrNsDNStatsAddrStatCounter2_Object = MibTableColumn
mscVrNsDNStatsAddrStatCounter2 = _MscVrNsDNStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 7, 2, 10, 1, 4),
    _MscVrNsDNStatsAddrStatCounter2_Type()
)
mscVrNsDNStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDNStatsAddrStatCounter2.setStatus("mandatory")
_MscVrNsBrStats_ObjectIdentity = ObjectIdentity
mscVrNsBrStats = _MscVrNsBrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8)
)
_MscVrNsBrStatsRowStatusTable_Object = MibTable
mscVrNsBrStatsRowStatusTable = _MscVrNsBrStatsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 1)
)
if mibBuilder.loadTexts:
    mscVrNsBrStatsRowStatusTable.setStatus("mandatory")
_MscVrNsBrStatsRowStatusEntry_Object = MibTableRow
mscVrNsBrStatsRowStatusEntry = _MscVrNsBrStatsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 1, 1)
)
mscVrNsBrStatsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsBrStatsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsBrStatsRowStatusEntry.setStatus("mandatory")
_MscVrNsBrStatsRowStatus_Type = RowStatus
_MscVrNsBrStatsRowStatus_Object = MibTableColumn
mscVrNsBrStatsRowStatus = _MscVrNsBrStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 1, 1, 1),
    _MscVrNsBrStatsRowStatus_Type()
)
mscVrNsBrStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsBrStatsRowStatus.setStatus("mandatory")
_MscVrNsBrStatsComponentName_Type = DisplayString
_MscVrNsBrStatsComponentName_Object = MibTableColumn
mscVrNsBrStatsComponentName = _MscVrNsBrStatsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 1, 1, 2),
    _MscVrNsBrStatsComponentName_Type()
)
mscVrNsBrStatsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsComponentName.setStatus("mandatory")
_MscVrNsBrStatsStorageType_Type = StorageType
_MscVrNsBrStatsStorageType_Object = MibTableColumn
mscVrNsBrStatsStorageType = _MscVrNsBrStatsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 1, 1, 4),
    _MscVrNsBrStatsStorageType_Type()
)
mscVrNsBrStatsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsStorageType.setStatus("mandatory")
_MscVrNsBrStatsIndex_Type = NonReplicated
_MscVrNsBrStatsIndex_Object = MibTableColumn
mscVrNsBrStatsIndex = _MscVrNsBrStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 1, 1, 10),
    _MscVrNsBrStatsIndex_Type()
)
mscVrNsBrStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsBrStatsIndex.setStatus("mandatory")
_MscVrNsBrStatsAddrStat_ObjectIdentity = ObjectIdentity
mscVrNsBrStatsAddrStat = _MscVrNsBrStatsAddrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2)
)
_MscVrNsBrStatsAddrStatRowStatusTable_Object = MibTable
mscVrNsBrStatsAddrStatRowStatusTable = _MscVrNsBrStatsAddrStatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatRowStatusTable.setStatus("mandatory")
_MscVrNsBrStatsAddrStatRowStatusEntry_Object = MibTableRow
mscVrNsBrStatsAddrStatRowStatusEntry = _MscVrNsBrStatsAddrStatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 1, 1)
)
mscVrNsBrStatsAddrStatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsBrStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsBrStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsBrStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatRowStatusEntry.setStatus("mandatory")
_MscVrNsBrStatsAddrStatRowStatus_Type = RowStatus
_MscVrNsBrStatsAddrStatRowStatus_Object = MibTableColumn
mscVrNsBrStatsAddrStatRowStatus = _MscVrNsBrStatsAddrStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 1, 1, 1),
    _MscVrNsBrStatsAddrStatRowStatus_Type()
)
mscVrNsBrStatsAddrStatRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatRowStatus.setStatus("mandatory")
_MscVrNsBrStatsAddrStatComponentName_Type = DisplayString
_MscVrNsBrStatsAddrStatComponentName_Object = MibTableColumn
mscVrNsBrStatsAddrStatComponentName = _MscVrNsBrStatsAddrStatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 1, 1, 2),
    _MscVrNsBrStatsAddrStatComponentName_Type()
)
mscVrNsBrStatsAddrStatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatComponentName.setStatus("mandatory")
_MscVrNsBrStatsAddrStatStorageType_Type = StorageType
_MscVrNsBrStatsAddrStatStorageType_Object = MibTableColumn
mscVrNsBrStatsAddrStatStorageType = _MscVrNsBrStatsAddrStatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 1, 1, 4),
    _MscVrNsBrStatsAddrStatStorageType_Type()
)
mscVrNsBrStatsAddrStatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatStorageType.setStatus("mandatory")


class _MscVrNsBrStatsAddrStatSourceAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsBrStatsAddrStatSourceAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsBrStatsAddrStatSourceAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsBrStatsAddrStatSourceAddressIndex_Object = MibTableColumn
mscVrNsBrStatsAddrStatSourceAddressIndex = _MscVrNsBrStatsAddrStatSourceAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 1, 1, 10),
    _MscVrNsBrStatsAddrStatSourceAddressIndex_Type()
)
mscVrNsBrStatsAddrStatSourceAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatSourceAddressIndex.setStatus("mandatory")


class _MscVrNsBrStatsAddrStatDestinationAddressIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsBrStatsAddrStatDestinationAddressIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsBrStatsAddrStatDestinationAddressIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsBrStatsAddrStatDestinationAddressIndex_Object = MibTableColumn
mscVrNsBrStatsAddrStatDestinationAddressIndex = _MscVrNsBrStatsAddrStatDestinationAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 1, 1, 11),
    _MscVrNsBrStatsAddrStatDestinationAddressIndex_Type()
)
mscVrNsBrStatsAddrStatDestinationAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatDestinationAddressIndex.setStatus("mandatory")
_MscVrNsBrStatsAddrStatStatsTable_Object = MibTable
mscVrNsBrStatsAddrStatStatsTable = _MscVrNsBrStatsAddrStatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatStatsTable.setStatus("mandatory")
_MscVrNsBrStatsAddrStatStatsEntry_Object = MibTableRow
mscVrNsBrStatsAddrStatStatsEntry = _MscVrNsBrStatsAddrStatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 10, 1)
)
mscVrNsBrStatsAddrStatStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsBrStatsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsBrStatsAddrStatSourceAddressIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsBrStatsAddrStatDestinationAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatStatsEntry.setStatus("mandatory")
_MscVrNsBrStatsAddrStatPacketCount_Type = Counter32
_MscVrNsBrStatsAddrStatPacketCount_Object = MibTableColumn
mscVrNsBrStatsAddrStatPacketCount = _MscVrNsBrStatsAddrStatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 10, 1, 1),
    _MscVrNsBrStatsAddrStatPacketCount_Type()
)
mscVrNsBrStatsAddrStatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatPacketCount.setStatus("mandatory")
_MscVrNsBrStatsAddrStatByteCount_Type = Counter32
_MscVrNsBrStatsAddrStatByteCount_Object = MibTableColumn
mscVrNsBrStatsAddrStatByteCount = _MscVrNsBrStatsAddrStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 10, 1, 2),
    _MscVrNsBrStatsAddrStatByteCount_Type()
)
mscVrNsBrStatsAddrStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatByteCount.setStatus("mandatory")
_MscVrNsBrStatsAddrStatCounter1_Type = Counter32
_MscVrNsBrStatsAddrStatCounter1_Object = MibTableColumn
mscVrNsBrStatsAddrStatCounter1 = _MscVrNsBrStatsAddrStatCounter1_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 10, 1, 3),
    _MscVrNsBrStatsAddrStatCounter1_Type()
)
mscVrNsBrStatsAddrStatCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatCounter1.setStatus("mandatory")
_MscVrNsBrStatsAddrStatCounter2_Type = Counter32
_MscVrNsBrStatsAddrStatCounter2_Object = MibTableColumn
mscVrNsBrStatsAddrStatCounter2 = _MscVrNsBrStatsAddrStatCounter2_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 8, 2, 10, 1, 4),
    _MscVrNsBrStatsAddrStatCounter2_Type()
)
mscVrNsBrStatsAddrStatCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsBrStatsAddrStatCounter2.setStatus("mandatory")
_MscVrNsFilter_ObjectIdentity = ObjectIdentity
mscVrNsFilter = _MscVrNsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9)
)
_MscVrNsFilterRowStatusTable_Object = MibTable
mscVrNsFilterRowStatusTable = _MscVrNsFilterRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 1)
)
if mibBuilder.loadTexts:
    mscVrNsFilterRowStatusTable.setStatus("mandatory")
_MscVrNsFilterRowStatusEntry_Object = MibTableRow
mscVrNsFilterRowStatusEntry = _MscVrNsFilterRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 1, 1)
)
mscVrNsFilterRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsFilterNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsFilterKindIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsFilterRowStatusEntry.setStatus("mandatory")
_MscVrNsFilterRowStatus_Type = RowStatus
_MscVrNsFilterRowStatus_Object = MibTableColumn
mscVrNsFilterRowStatus = _MscVrNsFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 1, 1, 1),
    _MscVrNsFilterRowStatus_Type()
)
mscVrNsFilterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterRowStatus.setStatus("mandatory")
_MscVrNsFilterComponentName_Type = DisplayString
_MscVrNsFilterComponentName_Object = MibTableColumn
mscVrNsFilterComponentName = _MscVrNsFilterComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 1, 1, 2),
    _MscVrNsFilterComponentName_Type()
)
mscVrNsFilterComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterComponentName.setStatus("mandatory")
_MscVrNsFilterStorageType_Type = StorageType
_MscVrNsFilterStorageType_Object = MibTableColumn
mscVrNsFilterStorageType = _MscVrNsFilterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 1, 1, 4),
    _MscVrNsFilterStorageType_Type()
)
mscVrNsFilterStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterStorageType.setStatus("mandatory")


class _MscVrNsFilterNameIndex_Type(AsciiStringIndex):
    """Custom type mscVrNsFilterNameIndex based on AsciiStringIndex"""
    subtypeSpec = AsciiStringIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MscVrNsFilterNameIndex_Type.__name__ = "AsciiStringIndex"
_MscVrNsFilterNameIndex_Object = MibTableColumn
mscVrNsFilterNameIndex = _MscVrNsFilterNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 1, 1, 10),
    _MscVrNsFilterNameIndex_Type()
)
mscVrNsFilterNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsFilterNameIndex.setStatus("mandatory")


class _MscVrNsFilterKindIndex_Type(Integer32):
    """Custom type mscVrNsFilterKindIndex based on Integer32"""
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


_MscVrNsFilterKindIndex_Type.__name__ = "Integer32"
_MscVrNsFilterKindIndex_Object = MibTableColumn
mscVrNsFilterKindIndex = _MscVrNsFilterKindIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 1, 1, 11),
    _MscVrNsFilterKindIndex_Type()
)
mscVrNsFilterKindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrNsFilterKindIndex.setStatus("mandatory")
_MscVrNsFilterStatsTable_Object = MibTable
mscVrNsFilterStatsTable = _MscVrNsFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10)
)
if mibBuilder.loadTexts:
    mscVrNsFilterStatsTable.setStatus("mandatory")
_MscVrNsFilterStatsEntry_Object = MibTableRow
mscVrNsFilterStatsEntry = _MscVrNsFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1)
)
mscVrNsFilterStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsFilterNameIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsFilterKindIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsFilterStatsEntry.setStatus("mandatory")
_MscVrNsFilterPacketsSucceeded_Type = Counter32
_MscVrNsFilterPacketsSucceeded_Object = MibTableColumn
mscVrNsFilterPacketsSucceeded = _MscVrNsFilterPacketsSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 1),
    _MscVrNsFilterPacketsSucceeded_Type()
)
mscVrNsFilterPacketsSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterPacketsSucceeded.setStatus("mandatory")
_MscVrNsFilterBytesSucceeded_Type = Counter32
_MscVrNsFilterBytesSucceeded_Object = MibTableColumn
mscVrNsFilterBytesSucceeded = _MscVrNsFilterBytesSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 2),
    _MscVrNsFilterBytesSucceeded_Type()
)
mscVrNsFilterBytesSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterBytesSucceeded.setStatus("mandatory")
_MscVrNsFilterPacketsFailed_Type = Counter32
_MscVrNsFilterPacketsFailed_Object = MibTableColumn
mscVrNsFilterPacketsFailed = _MscVrNsFilterPacketsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 3),
    _MscVrNsFilterPacketsFailed_Type()
)
mscVrNsFilterPacketsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterPacketsFailed.setStatus("mandatory")
_MscVrNsFilterBytesFailed_Type = Counter32
_MscVrNsFilterBytesFailed_Object = MibTableColumn
mscVrNsFilterBytesFailed = _MscVrNsFilterBytesFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 4),
    _MscVrNsFilterBytesFailed_Type()
)
mscVrNsFilterBytesFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterBytesFailed.setStatus("mandatory")
_MscVrNsFilterPacketsBreaked_Type = Counter32
_MscVrNsFilterPacketsBreaked_Object = MibTableColumn
mscVrNsFilterPacketsBreaked = _MscVrNsFilterPacketsBreaked_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 5),
    _MscVrNsFilterPacketsBreaked_Type()
)
mscVrNsFilterPacketsBreaked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterPacketsBreaked.setStatus("mandatory")
_MscVrNsFilterBytesBreaked_Type = Counter32
_MscVrNsFilterBytesBreaked_Object = MibTableColumn
mscVrNsFilterBytesBreaked = _MscVrNsFilterBytesBreaked_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 6),
    _MscVrNsFilterBytesBreaked_Type()
)
mscVrNsFilterBytesBreaked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterBytesBreaked.setStatus("mandatory")
_MscVrNsFilterPacketsContinued_Type = Counter32
_MscVrNsFilterPacketsContinued_Object = MibTableColumn
mscVrNsFilterPacketsContinued = _MscVrNsFilterPacketsContinued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 7),
    _MscVrNsFilterPacketsContinued_Type()
)
mscVrNsFilterPacketsContinued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterPacketsContinued.setStatus("mandatory")
_MscVrNsFilterBytesContinued_Type = Counter32
_MscVrNsFilterBytesContinued_Object = MibTableColumn
mscVrNsFilterBytesContinued = _MscVrNsFilterBytesContinued_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 9, 10, 1, 8),
    _MscVrNsFilterBytesContinued_Type()
)
mscVrNsFilterBytesContinued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsFilterBytesContinued.setStatus("mandatory")
_MscVrNsProvTable_Object = MibTable
mscVrNsProvTable = _MscVrNsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 100)
)
if mibBuilder.loadTexts:
    mscVrNsProvTable.setStatus("mandatory")
_MscVrNsProvEntry_Object = MibTableRow
mscVrNsProvEntry = _MscVrNsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 100, 1)
)
mscVrNsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsProvEntry.setStatus("mandatory")


class _MscVrNsDropConditions_Type(OctetString):
    """Custom type mscVrNsDropConditions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVrNsDropConditions_Type.__name__ = "OctetString"
_MscVrNsDropConditions_Object = MibTableColumn
mscVrNsDropConditions = _MscVrNsDropConditions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 100, 1, 1),
    _MscVrNsDropConditions_Type()
)
mscVrNsDropConditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrNsDropConditions.setStatus("mandatory")
_MscVrNsStatsTable_Object = MibTable
mscVrNsStatsTable = _MscVrNsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101)
)
if mibBuilder.loadTexts:
    mscVrNsStatsTable.setStatus("mandatory")
_MscVrNsStatsEntry_Object = MibTableRow
mscVrNsStatsEntry = _MscVrNsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1)
)
mscVrNsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-NetSentryMIB", "mscVrNsIndex"),
)
if mibBuilder.loadTexts:
    mscVrNsStatsEntry.setStatus("mandatory")
_MscVrNsPacketsProcessed_Type = Counter32
_MscVrNsPacketsProcessed_Object = MibTableColumn
mscVrNsPacketsProcessed = _MscVrNsPacketsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 1),
    _MscVrNsPacketsProcessed_Type()
)
mscVrNsPacketsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsPacketsProcessed.setStatus("mandatory")
_MscVrNsPacketsFailed_Type = Counter32
_MscVrNsPacketsFailed_Object = MibTableColumn
mscVrNsPacketsFailed = _MscVrNsPacketsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 2),
    _MscVrNsPacketsFailed_Type()
)
mscVrNsPacketsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsPacketsFailed.setStatus("mandatory")
_MscVrNsStatsNoMem_Type = Counter32
_MscVrNsStatsNoMem_Object = MibTableColumn
mscVrNsStatsNoMem = _MscVrNsStatsNoMem_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 3),
    _MscVrNsStatsNoMem_Type()
)
mscVrNsStatsNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsStatsNoMem.setStatus("mandatory")
_MscVrNsHsaOkayFailed_Type = Counter32
_MscVrNsHsaOkayFailed_Object = MibTableColumn
mscVrNsHsaOkayFailed = _MscVrNsHsaOkayFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 4),
    _MscVrNsHsaOkayFailed_Type()
)
mscVrNsHsaOkayFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsHsaOkayFailed.setStatus("mandatory")
_MscVrNsDepthExceeded_Type = Counter32
_MscVrNsDepthExceeded_Object = MibTableColumn
mscVrNsDepthExceeded = _MscVrNsDepthExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 5),
    _MscVrNsDepthExceeded_Type()
)
mscVrNsDepthExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDepthExceeded.setStatus("mandatory")
_MscVrNsDroppedStatsNoMem_Type = Counter32
_MscVrNsDroppedStatsNoMem_Object = MibTableColumn
mscVrNsDroppedStatsNoMem = _MscVrNsDroppedStatsNoMem_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 6),
    _MscVrNsDroppedStatsNoMem_Type()
)
mscVrNsDroppedStatsNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDroppedStatsNoMem.setStatus("mandatory")
_MscVrNsDroppedCantCloneTo_Type = Counter32
_MscVrNsDroppedCantCloneTo_Object = MibTableColumn
mscVrNsDroppedCantCloneTo = _MscVrNsDroppedCantCloneTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 7),
    _MscVrNsDroppedCantCloneTo_Type()
)
mscVrNsDroppedCantCloneTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDroppedCantCloneTo.setStatus("mandatory")
_MscVrNsDroppedCantLogTo_Type = Counter32
_MscVrNsDroppedCantLogTo_Object = MibTableColumn
mscVrNsDroppedCantLogTo = _MscVrNsDroppedCantLogTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 8),
    _MscVrNsDroppedCantLogTo_Type()
)
mscVrNsDroppedCantLogTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDroppedCantLogTo.setStatus("mandatory")
_MscVrNsDroppedCantCopyTo_Type = Counter32
_MscVrNsDroppedCantCopyTo_Object = MibTableColumn
mscVrNsDroppedCantCopyTo = _MscVrNsDroppedCantCopyTo_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 9),
    _MscVrNsDroppedCantCopyTo_Type()
)
mscVrNsDroppedCantCopyTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDroppedCantCopyTo.setStatus("mandatory")
_MscVrNsDroppedNullFilter_Type = Counter32
_MscVrNsDroppedNullFilter_Object = MibTableColumn
mscVrNsDroppedNullFilter = _MscVrNsDroppedNullFilter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 4, 101, 1, 10),
    _MscVrNsDroppedNullFilter_Type()
)
mscVrNsDroppedNullFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrNsDroppedNullFilter.setStatus("mandatory")
_NetSentryMIB_ObjectIdentity = ObjectIdentity
netSentryMIB = _NetSentryMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31)
)
_NetSentryGroup_ObjectIdentity = ObjectIdentity
netSentryGroup = _NetSentryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 1)
)
_NetSentryGroupCA_ObjectIdentity = ObjectIdentity
netSentryGroupCA = _NetSentryGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 1, 1)
)
_NetSentryGroupCA02_ObjectIdentity = ObjectIdentity
netSentryGroupCA02 = _NetSentryGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 1, 1, 3)
)
_NetSentryGroupCA02A_ObjectIdentity = ObjectIdentity
netSentryGroupCA02A = _NetSentryGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 1, 1, 3, 2)
)
_NetSentryCapabilities_ObjectIdentity = ObjectIdentity
netSentryCapabilities = _NetSentryCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 3)
)
_NetSentryCapabilitiesCA_ObjectIdentity = ObjectIdentity
netSentryCapabilitiesCA = _NetSentryCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 3, 1)
)
_NetSentryCapabilitiesCA02_ObjectIdentity = ObjectIdentity
netSentryCapabilitiesCA02 = _NetSentryCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 3, 1, 3)
)
_NetSentryCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
netSentryCapabilitiesCA02A = _NetSentryCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 31, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-NetSentryMIB",
    **{"mscVrNs": mscVrNs,
       "mscVrNsRowStatusTable": mscVrNsRowStatusTable,
       "mscVrNsRowStatusEntry": mscVrNsRowStatusEntry,
       "mscVrNsRowStatus": mscVrNsRowStatus,
       "mscVrNsComponentName": mscVrNsComponentName,
       "mscVrNsStorageType": mscVrNsStorageType,
       "mscVrNsIndex": mscVrNsIndex,
       "mscVrNsFile": mscVrNsFile,
       "mscVrNsFileRowStatusTable": mscVrNsFileRowStatusTable,
       "mscVrNsFileRowStatusEntry": mscVrNsFileRowStatusEntry,
       "mscVrNsFileRowStatus": mscVrNsFileRowStatus,
       "mscVrNsFileComponentName": mscVrNsFileComponentName,
       "mscVrNsFileStorageType": mscVrNsFileStorageType,
       "mscVrNsFileIndex": mscVrNsFileIndex,
       "mscVrNsFileOperTable": mscVrNsFileOperTable,
       "mscVrNsFileOperEntry": mscVrNsFileOperEntry,
       "mscVrNsFileCompilerErrorMsg": mscVrNsFileCompilerErrorMsg,
       "mscVrNsEngine": mscVrNsEngine,
       "mscVrNsEngineRowStatusTable": mscVrNsEngineRowStatusTable,
       "mscVrNsEngineRowStatusEntry": mscVrNsEngineRowStatusEntry,
       "mscVrNsEngineRowStatus": mscVrNsEngineRowStatus,
       "mscVrNsEngineComponentName": mscVrNsEngineComponentName,
       "mscVrNsEngineStorageType": mscVrNsEngineStorageType,
       "mscVrNsEngineIndex": mscVrNsEngineIndex,
       "mscVrNsIPStats": mscVrNsIPStats,
       "mscVrNsIPStatsRowStatusTable": mscVrNsIPStatsRowStatusTable,
       "mscVrNsIPStatsRowStatusEntry": mscVrNsIPStatsRowStatusEntry,
       "mscVrNsIPStatsRowStatus": mscVrNsIPStatsRowStatus,
       "mscVrNsIPStatsComponentName": mscVrNsIPStatsComponentName,
       "mscVrNsIPStatsStorageType": mscVrNsIPStatsStorageType,
       "mscVrNsIPStatsIndex": mscVrNsIPStatsIndex,
       "mscVrNsIPStatsAddrStat": mscVrNsIPStatsAddrStat,
       "mscVrNsIPStatsAddrStatRowStatusTable": mscVrNsIPStatsAddrStatRowStatusTable,
       "mscVrNsIPStatsAddrStatRowStatusEntry": mscVrNsIPStatsAddrStatRowStatusEntry,
       "mscVrNsIPStatsAddrStatRowStatus": mscVrNsIPStatsAddrStatRowStatus,
       "mscVrNsIPStatsAddrStatComponentName": mscVrNsIPStatsAddrStatComponentName,
       "mscVrNsIPStatsAddrStatStorageType": mscVrNsIPStatsAddrStatStorageType,
       "mscVrNsIPStatsAddrStatSourceAddressIndex": mscVrNsIPStatsAddrStatSourceAddressIndex,
       "mscVrNsIPStatsAddrStatDestinationAddressIndex": mscVrNsIPStatsAddrStatDestinationAddressIndex,
       "mscVrNsIPStatsAddrStatStatsTable": mscVrNsIPStatsAddrStatStatsTable,
       "mscVrNsIPStatsAddrStatStatsEntry": mscVrNsIPStatsAddrStatStatsEntry,
       "mscVrNsIPStatsAddrStatPacketCount": mscVrNsIPStatsAddrStatPacketCount,
       "mscVrNsIPStatsAddrStatByteCount": mscVrNsIPStatsAddrStatByteCount,
       "mscVrNsIPStatsAddrStatCounter1": mscVrNsIPStatsAddrStatCounter1,
       "mscVrNsIPStatsAddrStatCounter2": mscVrNsIPStatsAddrStatCounter2,
       "mscVrNsIPXStats": mscVrNsIPXStats,
       "mscVrNsIPXStatsRowStatusTable": mscVrNsIPXStatsRowStatusTable,
       "mscVrNsIPXStatsRowStatusEntry": mscVrNsIPXStatsRowStatusEntry,
       "mscVrNsIPXStatsRowStatus": mscVrNsIPXStatsRowStatus,
       "mscVrNsIPXStatsComponentName": mscVrNsIPXStatsComponentName,
       "mscVrNsIPXStatsStorageType": mscVrNsIPXStatsStorageType,
       "mscVrNsIPXStatsIndex": mscVrNsIPXStatsIndex,
       "mscVrNsIPXStatsAddrStat": mscVrNsIPXStatsAddrStat,
       "mscVrNsIPXStatsAddrStatRowStatusTable": mscVrNsIPXStatsAddrStatRowStatusTable,
       "mscVrNsIPXStatsAddrStatRowStatusEntry": mscVrNsIPXStatsAddrStatRowStatusEntry,
       "mscVrNsIPXStatsAddrStatRowStatus": mscVrNsIPXStatsAddrStatRowStatus,
       "mscVrNsIPXStatsAddrStatComponentName": mscVrNsIPXStatsAddrStatComponentName,
       "mscVrNsIPXStatsAddrStatStorageType": mscVrNsIPXStatsAddrStatStorageType,
       "mscVrNsIPXStatsAddrStatSourceAddressIndex": mscVrNsIPXStatsAddrStatSourceAddressIndex,
       "mscVrNsIPXStatsAddrStatDestinationAddressIndex": mscVrNsIPXStatsAddrStatDestinationAddressIndex,
       "mscVrNsIPXStatsAddrStatStatsTable": mscVrNsIPXStatsAddrStatStatsTable,
       "mscVrNsIPXStatsAddrStatStatsEntry": mscVrNsIPXStatsAddrStatStatsEntry,
       "mscVrNsIPXStatsAddrStatPacketCount": mscVrNsIPXStatsAddrStatPacketCount,
       "mscVrNsIPXStatsAddrStatByteCount": mscVrNsIPXStatsAddrStatByteCount,
       "mscVrNsIPXStatsAddrStatCounter1": mscVrNsIPXStatsAddrStatCounter1,
       "mscVrNsIPXStatsAddrStatCounter2": mscVrNsIPXStatsAddrStatCounter2,
       "mscVrNsATStats": mscVrNsATStats,
       "mscVrNsATStatsRowStatusTable": mscVrNsATStatsRowStatusTable,
       "mscVrNsATStatsRowStatusEntry": mscVrNsATStatsRowStatusEntry,
       "mscVrNsATStatsRowStatus": mscVrNsATStatsRowStatus,
       "mscVrNsATStatsComponentName": mscVrNsATStatsComponentName,
       "mscVrNsATStatsStorageType": mscVrNsATStatsStorageType,
       "mscVrNsATStatsIndex": mscVrNsATStatsIndex,
       "mscVrNsATStatsAddrStat": mscVrNsATStatsAddrStat,
       "mscVrNsATStatsAddrStatRowStatusTable": mscVrNsATStatsAddrStatRowStatusTable,
       "mscVrNsATStatsAddrStatRowStatusEntry": mscVrNsATStatsAddrStatRowStatusEntry,
       "mscVrNsATStatsAddrStatRowStatus": mscVrNsATStatsAddrStatRowStatus,
       "mscVrNsATStatsAddrStatComponentName": mscVrNsATStatsAddrStatComponentName,
       "mscVrNsATStatsAddrStatStorageType": mscVrNsATStatsAddrStatStorageType,
       "mscVrNsATStatsAddrStatSourceAddressIndex": mscVrNsATStatsAddrStatSourceAddressIndex,
       "mscVrNsATStatsAddrStatDestinationAddressIndex": mscVrNsATStatsAddrStatDestinationAddressIndex,
       "mscVrNsATStatsAddrStatStatsTable": mscVrNsATStatsAddrStatStatsTable,
       "mscVrNsATStatsAddrStatStatsEntry": mscVrNsATStatsAddrStatStatsEntry,
       "mscVrNsATStatsAddrStatPacketCount": mscVrNsATStatsAddrStatPacketCount,
       "mscVrNsATStatsAddrStatByteCount": mscVrNsATStatsAddrStatByteCount,
       "mscVrNsATStatsAddrStatCounter1": mscVrNsATStatsAddrStatCounter1,
       "mscVrNsATStatsAddrStatCounter2": mscVrNsATStatsAddrStatCounter2,
       "mscVrNsDNStats": mscVrNsDNStats,
       "mscVrNsDNStatsRowStatusTable": mscVrNsDNStatsRowStatusTable,
       "mscVrNsDNStatsRowStatusEntry": mscVrNsDNStatsRowStatusEntry,
       "mscVrNsDNStatsRowStatus": mscVrNsDNStatsRowStatus,
       "mscVrNsDNStatsComponentName": mscVrNsDNStatsComponentName,
       "mscVrNsDNStatsStorageType": mscVrNsDNStatsStorageType,
       "mscVrNsDNStatsIndex": mscVrNsDNStatsIndex,
       "mscVrNsDNStatsAddrStat": mscVrNsDNStatsAddrStat,
       "mscVrNsDNStatsAddrStatRowStatusTable": mscVrNsDNStatsAddrStatRowStatusTable,
       "mscVrNsDNStatsAddrStatRowStatusEntry": mscVrNsDNStatsAddrStatRowStatusEntry,
       "mscVrNsDNStatsAddrStatRowStatus": mscVrNsDNStatsAddrStatRowStatus,
       "mscVrNsDNStatsAddrStatComponentName": mscVrNsDNStatsAddrStatComponentName,
       "mscVrNsDNStatsAddrStatStorageType": mscVrNsDNStatsAddrStatStorageType,
       "mscVrNsDNStatsAddrStatSourceAddressIndex": mscVrNsDNStatsAddrStatSourceAddressIndex,
       "mscVrNsDNStatsAddrStatDestinationAddressIndex": mscVrNsDNStatsAddrStatDestinationAddressIndex,
       "mscVrNsDNStatsAddrStatStatsTable": mscVrNsDNStatsAddrStatStatsTable,
       "mscVrNsDNStatsAddrStatStatsEntry": mscVrNsDNStatsAddrStatStatsEntry,
       "mscVrNsDNStatsAddrStatPacketCount": mscVrNsDNStatsAddrStatPacketCount,
       "mscVrNsDNStatsAddrStatByteCount": mscVrNsDNStatsAddrStatByteCount,
       "mscVrNsDNStatsAddrStatCounter1": mscVrNsDNStatsAddrStatCounter1,
       "mscVrNsDNStatsAddrStatCounter2": mscVrNsDNStatsAddrStatCounter2,
       "mscVrNsBrStats": mscVrNsBrStats,
       "mscVrNsBrStatsRowStatusTable": mscVrNsBrStatsRowStatusTable,
       "mscVrNsBrStatsRowStatusEntry": mscVrNsBrStatsRowStatusEntry,
       "mscVrNsBrStatsRowStatus": mscVrNsBrStatsRowStatus,
       "mscVrNsBrStatsComponentName": mscVrNsBrStatsComponentName,
       "mscVrNsBrStatsStorageType": mscVrNsBrStatsStorageType,
       "mscVrNsBrStatsIndex": mscVrNsBrStatsIndex,
       "mscVrNsBrStatsAddrStat": mscVrNsBrStatsAddrStat,
       "mscVrNsBrStatsAddrStatRowStatusTable": mscVrNsBrStatsAddrStatRowStatusTable,
       "mscVrNsBrStatsAddrStatRowStatusEntry": mscVrNsBrStatsAddrStatRowStatusEntry,
       "mscVrNsBrStatsAddrStatRowStatus": mscVrNsBrStatsAddrStatRowStatus,
       "mscVrNsBrStatsAddrStatComponentName": mscVrNsBrStatsAddrStatComponentName,
       "mscVrNsBrStatsAddrStatStorageType": mscVrNsBrStatsAddrStatStorageType,
       "mscVrNsBrStatsAddrStatSourceAddressIndex": mscVrNsBrStatsAddrStatSourceAddressIndex,
       "mscVrNsBrStatsAddrStatDestinationAddressIndex": mscVrNsBrStatsAddrStatDestinationAddressIndex,
       "mscVrNsBrStatsAddrStatStatsTable": mscVrNsBrStatsAddrStatStatsTable,
       "mscVrNsBrStatsAddrStatStatsEntry": mscVrNsBrStatsAddrStatStatsEntry,
       "mscVrNsBrStatsAddrStatPacketCount": mscVrNsBrStatsAddrStatPacketCount,
       "mscVrNsBrStatsAddrStatByteCount": mscVrNsBrStatsAddrStatByteCount,
       "mscVrNsBrStatsAddrStatCounter1": mscVrNsBrStatsAddrStatCounter1,
       "mscVrNsBrStatsAddrStatCounter2": mscVrNsBrStatsAddrStatCounter2,
       "mscVrNsFilter": mscVrNsFilter,
       "mscVrNsFilterRowStatusTable": mscVrNsFilterRowStatusTable,
       "mscVrNsFilterRowStatusEntry": mscVrNsFilterRowStatusEntry,
       "mscVrNsFilterRowStatus": mscVrNsFilterRowStatus,
       "mscVrNsFilterComponentName": mscVrNsFilterComponentName,
       "mscVrNsFilterStorageType": mscVrNsFilterStorageType,
       "mscVrNsFilterNameIndex": mscVrNsFilterNameIndex,
       "mscVrNsFilterKindIndex": mscVrNsFilterKindIndex,
       "mscVrNsFilterStatsTable": mscVrNsFilterStatsTable,
       "mscVrNsFilterStatsEntry": mscVrNsFilterStatsEntry,
       "mscVrNsFilterPacketsSucceeded": mscVrNsFilterPacketsSucceeded,
       "mscVrNsFilterBytesSucceeded": mscVrNsFilterBytesSucceeded,
       "mscVrNsFilterPacketsFailed": mscVrNsFilterPacketsFailed,
       "mscVrNsFilterBytesFailed": mscVrNsFilterBytesFailed,
       "mscVrNsFilterPacketsBreaked": mscVrNsFilterPacketsBreaked,
       "mscVrNsFilterBytesBreaked": mscVrNsFilterBytesBreaked,
       "mscVrNsFilterPacketsContinued": mscVrNsFilterPacketsContinued,
       "mscVrNsFilterBytesContinued": mscVrNsFilterBytesContinued,
       "mscVrNsProvTable": mscVrNsProvTable,
       "mscVrNsProvEntry": mscVrNsProvEntry,
       "mscVrNsDropConditions": mscVrNsDropConditions,
       "mscVrNsStatsTable": mscVrNsStatsTable,
       "mscVrNsStatsEntry": mscVrNsStatsEntry,
       "mscVrNsPacketsProcessed": mscVrNsPacketsProcessed,
       "mscVrNsPacketsFailed": mscVrNsPacketsFailed,
       "mscVrNsStatsNoMem": mscVrNsStatsNoMem,
       "mscVrNsHsaOkayFailed": mscVrNsHsaOkayFailed,
       "mscVrNsDepthExceeded": mscVrNsDepthExceeded,
       "mscVrNsDroppedStatsNoMem": mscVrNsDroppedStatsNoMem,
       "mscVrNsDroppedCantCloneTo": mscVrNsDroppedCantCloneTo,
       "mscVrNsDroppedCantLogTo": mscVrNsDroppedCantLogTo,
       "mscVrNsDroppedCantCopyTo": mscVrNsDroppedCantCopyTo,
       "mscVrNsDroppedNullFilter": mscVrNsDroppedNullFilter,
       "netSentryMIB": netSentryMIB,
       "netSentryGroup": netSentryGroup,
       "netSentryGroupCA": netSentryGroupCA,
       "netSentryGroupCA02": netSentryGroupCA02,
       "netSentryGroupCA02A": netSentryGroupCA02A,
       "netSentryCapabilities": netSentryCapabilities,
       "netSentryCapabilitiesCA": netSentryCapabilitiesCA,
       "netSentryCapabilitiesCA02": netSentryCapabilitiesCA02,
       "netSentryCapabilitiesCA02A": netSentryCapabilitiesCA02A}
)
