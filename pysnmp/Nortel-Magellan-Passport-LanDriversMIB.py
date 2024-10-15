# SNMP MIB module (Nortel-Magellan-Passport-LanDriversMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-LanDriversMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:05 2024
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

(lp,
 lpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-LogicalProcessorMIB",
    "lp",
    "lpIndex")

(Counter32,
 DisplayString,
 FddiMACLongAddressType,
 FddiTimeMilli,
 FddiTimeNano,
 Gauge32,
 Integer32,
 InterfaceIndex,
 MacAddress,
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "FddiMACLongAddressType",
    "FddiTimeMilli",
    "FddiTimeNano",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "MacAddress",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "Link",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_LpEnet_ObjectIdentity = ObjectIdentity
lpEnet = _LpEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3)
)
_LpEnetRowStatusTable_Object = MibTable
lpEnetRowStatusTable = _LpEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    lpEnetRowStatusTable.setStatus("mandatory")
_LpEnetRowStatusEntry_Object = MibTableRow
lpEnetRowStatusEntry = _LpEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 1, 1)
)
lpEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetRowStatusEntry.setStatus("mandatory")
_LpEnetRowStatus_Type = RowStatus
_LpEnetRowStatus_Object = MibTableColumn
lpEnetRowStatus = _LpEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 1, 1, 1),
    _LpEnetRowStatus_Type()
)
lpEnetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetRowStatus.setStatus("mandatory")
_LpEnetComponentName_Type = DisplayString
_LpEnetComponentName_Object = MibTableColumn
lpEnetComponentName = _LpEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 1, 1, 2),
    _LpEnetComponentName_Type()
)
lpEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetComponentName.setStatus("mandatory")
_LpEnetStorageType_Type = StorageType
_LpEnetStorageType_Object = MibTableColumn
lpEnetStorageType = _LpEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 1, 1, 4),
    _LpEnetStorageType_Type()
)
lpEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetStorageType.setStatus("mandatory")


class _LpEnetIndex_Type(Integer32):
    """Custom type lpEnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_LpEnetIndex_Type.__name__ = "Integer32"
_LpEnetIndex_Object = MibTableColumn
lpEnetIndex = _LpEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 1, 1, 10),
    _LpEnetIndex_Type()
)
lpEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetIndex.setStatus("mandatory")
_LpEnetLt_ObjectIdentity = ObjectIdentity
lpEnetLt = _LpEnetLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2)
)
_LpEnetLtRowStatusTable_Object = MibTable
lpEnetLtRowStatusTable = _LpEnetLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtRowStatusTable.setStatus("mandatory")
_LpEnetLtRowStatusEntry_Object = MibTableRow
lpEnetLtRowStatusEntry = _LpEnetLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 1, 1)
)
lpEnetLtRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtRowStatusEntry.setStatus("mandatory")
_LpEnetLtRowStatus_Type = RowStatus
_LpEnetLtRowStatus_Object = MibTableColumn
lpEnetLtRowStatus = _LpEnetLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 1, 1, 1),
    _LpEnetLtRowStatus_Type()
)
lpEnetLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtRowStatus.setStatus("mandatory")
_LpEnetLtComponentName_Type = DisplayString
_LpEnetLtComponentName_Object = MibTableColumn
lpEnetLtComponentName = _LpEnetLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 1, 1, 2),
    _LpEnetLtComponentName_Type()
)
lpEnetLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtComponentName.setStatus("mandatory")
_LpEnetLtStorageType_Type = StorageType
_LpEnetLtStorageType_Object = MibTableColumn
lpEnetLtStorageType = _LpEnetLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 1, 1, 4),
    _LpEnetLtStorageType_Type()
)
lpEnetLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtStorageType.setStatus("mandatory")
_LpEnetLtIndex_Type = NonReplicated
_LpEnetLtIndex_Object = MibTableColumn
lpEnetLtIndex = _LpEnetLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 1, 1, 10),
    _LpEnetLtIndex_Type()
)
lpEnetLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtIndex.setStatus("mandatory")
_LpEnetLtFrmCmp_ObjectIdentity = ObjectIdentity
lpEnetLtFrmCmp = _LpEnetLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2)
)
_LpEnetLtFrmCmpRowStatusTable_Object = MibTable
lpEnetLtFrmCmpRowStatusTable = _LpEnetLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpRowStatusTable.setStatus("mandatory")
_LpEnetLtFrmCmpRowStatusEntry_Object = MibTableRow
lpEnetLtFrmCmpRowStatusEntry = _LpEnetLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 1, 1)
)
lpEnetLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpRowStatusEntry.setStatus("mandatory")
_LpEnetLtFrmCmpRowStatus_Type = RowStatus
_LpEnetLtFrmCmpRowStatus_Object = MibTableColumn
lpEnetLtFrmCmpRowStatus = _LpEnetLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 1, 1, 1),
    _LpEnetLtFrmCmpRowStatus_Type()
)
lpEnetLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpRowStatus.setStatus("mandatory")
_LpEnetLtFrmCmpComponentName_Type = DisplayString
_LpEnetLtFrmCmpComponentName_Object = MibTableColumn
lpEnetLtFrmCmpComponentName = _LpEnetLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 1, 1, 2),
    _LpEnetLtFrmCmpComponentName_Type()
)
lpEnetLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpComponentName.setStatus("mandatory")
_LpEnetLtFrmCmpStorageType_Type = StorageType
_LpEnetLtFrmCmpStorageType_Object = MibTableColumn
lpEnetLtFrmCmpStorageType = _LpEnetLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 1, 1, 4),
    _LpEnetLtFrmCmpStorageType_Type()
)
lpEnetLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpStorageType.setStatus("mandatory")
_LpEnetLtFrmCmpIndex_Type = NonReplicated
_LpEnetLtFrmCmpIndex_Object = MibTableColumn
lpEnetLtFrmCmpIndex = _LpEnetLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 1, 1, 10),
    _LpEnetLtFrmCmpIndex_Type()
)
lpEnetLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpIndex.setStatus("mandatory")
_LpEnetLtFrmCmpTopTable_Object = MibTable
lpEnetLtFrmCmpTopTable = _LpEnetLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpTopTable.setStatus("mandatory")
_LpEnetLtFrmCmpTopEntry_Object = MibTableRow
lpEnetLtFrmCmpTopEntry = _LpEnetLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 10, 1)
)
lpEnetLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpTopEntry.setStatus("mandatory")


class _LpEnetLtFrmCmpTData_Type(AsciiString):
    """Custom type lpEnetLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFrmCmpTData_Type.__name__ = "AsciiString"
_LpEnetLtFrmCmpTData_Object = MibTableColumn
lpEnetLtFrmCmpTData = _LpEnetLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 2, 10, 1, 1),
    _LpEnetLtFrmCmpTData_Type()
)
lpEnetLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFrmCmpTData.setStatus("mandatory")
_LpEnetLtFrmCpy_ObjectIdentity = ObjectIdentity
lpEnetLtFrmCpy = _LpEnetLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3)
)
_LpEnetLtFrmCpyRowStatusTable_Object = MibTable
lpEnetLtFrmCpyRowStatusTable = _LpEnetLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyRowStatusTable.setStatus("mandatory")
_LpEnetLtFrmCpyRowStatusEntry_Object = MibTableRow
lpEnetLtFrmCpyRowStatusEntry = _LpEnetLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 1, 1)
)
lpEnetLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyRowStatusEntry.setStatus("mandatory")
_LpEnetLtFrmCpyRowStatus_Type = RowStatus
_LpEnetLtFrmCpyRowStatus_Object = MibTableColumn
lpEnetLtFrmCpyRowStatus = _LpEnetLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 1, 1, 1),
    _LpEnetLtFrmCpyRowStatus_Type()
)
lpEnetLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyRowStatus.setStatus("mandatory")
_LpEnetLtFrmCpyComponentName_Type = DisplayString
_LpEnetLtFrmCpyComponentName_Object = MibTableColumn
lpEnetLtFrmCpyComponentName = _LpEnetLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 1, 1, 2),
    _LpEnetLtFrmCpyComponentName_Type()
)
lpEnetLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyComponentName.setStatus("mandatory")
_LpEnetLtFrmCpyStorageType_Type = StorageType
_LpEnetLtFrmCpyStorageType_Object = MibTableColumn
lpEnetLtFrmCpyStorageType = _LpEnetLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 1, 1, 4),
    _LpEnetLtFrmCpyStorageType_Type()
)
lpEnetLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyStorageType.setStatus("mandatory")
_LpEnetLtFrmCpyIndex_Type = NonReplicated
_LpEnetLtFrmCpyIndex_Object = MibTableColumn
lpEnetLtFrmCpyIndex = _LpEnetLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 1, 1, 10),
    _LpEnetLtFrmCpyIndex_Type()
)
lpEnetLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyIndex.setStatus("mandatory")
_LpEnetLtFrmCpyTopTable_Object = MibTable
lpEnetLtFrmCpyTopTable = _LpEnetLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyTopTable.setStatus("mandatory")
_LpEnetLtFrmCpyTopEntry_Object = MibTableRow
lpEnetLtFrmCpyTopEntry = _LpEnetLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 10, 1)
)
lpEnetLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyTopEntry.setStatus("mandatory")


class _LpEnetLtFrmCpyTData_Type(AsciiString):
    """Custom type lpEnetLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFrmCpyTData_Type.__name__ = "AsciiString"
_LpEnetLtFrmCpyTData_Object = MibTableColumn
lpEnetLtFrmCpyTData = _LpEnetLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 3, 10, 1, 1),
    _LpEnetLtFrmCpyTData_Type()
)
lpEnetLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFrmCpyTData.setStatus("mandatory")
_LpEnetLtPrtCfg_ObjectIdentity = ObjectIdentity
lpEnetLtPrtCfg = _LpEnetLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4)
)
_LpEnetLtPrtCfgRowStatusTable_Object = MibTable
lpEnetLtPrtCfgRowStatusTable = _LpEnetLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgRowStatusTable.setStatus("mandatory")
_LpEnetLtPrtCfgRowStatusEntry_Object = MibTableRow
lpEnetLtPrtCfgRowStatusEntry = _LpEnetLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 1, 1)
)
lpEnetLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgRowStatusEntry.setStatus("mandatory")
_LpEnetLtPrtCfgRowStatus_Type = RowStatus
_LpEnetLtPrtCfgRowStatus_Object = MibTableColumn
lpEnetLtPrtCfgRowStatus = _LpEnetLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 1, 1, 1),
    _LpEnetLtPrtCfgRowStatus_Type()
)
lpEnetLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgRowStatus.setStatus("mandatory")
_LpEnetLtPrtCfgComponentName_Type = DisplayString
_LpEnetLtPrtCfgComponentName_Object = MibTableColumn
lpEnetLtPrtCfgComponentName = _LpEnetLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 1, 1, 2),
    _LpEnetLtPrtCfgComponentName_Type()
)
lpEnetLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgComponentName.setStatus("mandatory")
_LpEnetLtPrtCfgStorageType_Type = StorageType
_LpEnetLtPrtCfgStorageType_Object = MibTableColumn
lpEnetLtPrtCfgStorageType = _LpEnetLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 1, 1, 4),
    _LpEnetLtPrtCfgStorageType_Type()
)
lpEnetLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgStorageType.setStatus("mandatory")
_LpEnetLtPrtCfgIndex_Type = NonReplicated
_LpEnetLtPrtCfgIndex_Object = MibTableColumn
lpEnetLtPrtCfgIndex = _LpEnetLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 1, 1, 10),
    _LpEnetLtPrtCfgIndex_Type()
)
lpEnetLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgIndex.setStatus("mandatory")
_LpEnetLtPrtCfgTopTable_Object = MibTable
lpEnetLtPrtCfgTopTable = _LpEnetLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgTopTable.setStatus("mandatory")
_LpEnetLtPrtCfgTopEntry_Object = MibTableRow
lpEnetLtPrtCfgTopEntry = _LpEnetLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 10, 1)
)
lpEnetLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgTopEntry.setStatus("mandatory")


class _LpEnetLtPrtCfgTData_Type(AsciiString):
    """Custom type lpEnetLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtPrtCfgTData_Type.__name__ = "AsciiString"
_LpEnetLtPrtCfgTData_Object = MibTableColumn
lpEnetLtPrtCfgTData = _LpEnetLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 4, 10, 1, 1),
    _LpEnetLtPrtCfgTData_Type()
)
lpEnetLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtPrtCfgTData.setStatus("mandatory")
_LpEnetLtFb_ObjectIdentity = ObjectIdentity
lpEnetLtFb = _LpEnetLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5)
)
_LpEnetLtFbRowStatusTable_Object = MibTable
lpEnetLtFbRowStatusTable = _LpEnetLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbRowStatusTable.setStatus("mandatory")
_LpEnetLtFbRowStatusEntry_Object = MibTableRow
lpEnetLtFbRowStatusEntry = _LpEnetLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 1, 1)
)
lpEnetLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbRowStatus_Type = RowStatus
_LpEnetLtFbRowStatus_Object = MibTableColumn
lpEnetLtFbRowStatus = _LpEnetLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 1, 1, 1),
    _LpEnetLtFbRowStatus_Type()
)
lpEnetLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbRowStatus.setStatus("mandatory")
_LpEnetLtFbComponentName_Type = DisplayString
_LpEnetLtFbComponentName_Object = MibTableColumn
lpEnetLtFbComponentName = _LpEnetLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 1, 1, 2),
    _LpEnetLtFbComponentName_Type()
)
lpEnetLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbComponentName.setStatus("mandatory")
_LpEnetLtFbStorageType_Type = StorageType
_LpEnetLtFbStorageType_Object = MibTableColumn
lpEnetLtFbStorageType = _LpEnetLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 1, 1, 4),
    _LpEnetLtFbStorageType_Type()
)
lpEnetLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbStorageType.setStatus("mandatory")
_LpEnetLtFbIndex_Type = NonReplicated
_LpEnetLtFbIndex_Object = MibTableColumn
lpEnetLtFbIndex = _LpEnetLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 1, 1, 10),
    _LpEnetLtFbIndex_Type()
)
lpEnetLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbIndex.setStatus("mandatory")
_LpEnetLtFbTxInfo_ObjectIdentity = ObjectIdentity
lpEnetLtFbTxInfo = _LpEnetLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2)
)
_LpEnetLtFbTxInfoRowStatusTable_Object = MibTable
lpEnetLtFbTxInfoRowStatusTable = _LpEnetLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoRowStatusTable.setStatus("mandatory")
_LpEnetLtFbTxInfoRowStatusEntry_Object = MibTableRow
lpEnetLtFbTxInfoRowStatusEntry = _LpEnetLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 1, 1)
)
lpEnetLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbTxInfoRowStatus_Type = RowStatus
_LpEnetLtFbTxInfoRowStatus_Object = MibTableColumn
lpEnetLtFbTxInfoRowStatus = _LpEnetLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 1, 1, 1),
    _LpEnetLtFbTxInfoRowStatus_Type()
)
lpEnetLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoRowStatus.setStatus("mandatory")
_LpEnetLtFbTxInfoComponentName_Type = DisplayString
_LpEnetLtFbTxInfoComponentName_Object = MibTableColumn
lpEnetLtFbTxInfoComponentName = _LpEnetLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 1, 1, 2),
    _LpEnetLtFbTxInfoComponentName_Type()
)
lpEnetLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoComponentName.setStatus("mandatory")
_LpEnetLtFbTxInfoStorageType_Type = StorageType
_LpEnetLtFbTxInfoStorageType_Object = MibTableColumn
lpEnetLtFbTxInfoStorageType = _LpEnetLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 1, 1, 4),
    _LpEnetLtFbTxInfoStorageType_Type()
)
lpEnetLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoStorageType.setStatus("mandatory")
_LpEnetLtFbTxInfoIndex_Type = NonReplicated
_LpEnetLtFbTxInfoIndex_Object = MibTableColumn
lpEnetLtFbTxInfoIndex = _LpEnetLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 1, 1, 10),
    _LpEnetLtFbTxInfoIndex_Type()
)
lpEnetLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoIndex.setStatus("mandatory")
_LpEnetLtFbTxInfoTopTable_Object = MibTable
lpEnetLtFbTxInfoTopTable = _LpEnetLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoTopTable.setStatus("mandatory")
_LpEnetLtFbTxInfoTopEntry_Object = MibTableRow
lpEnetLtFbTxInfoTopEntry = _LpEnetLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 10, 1)
)
lpEnetLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoTopEntry.setStatus("mandatory")


class _LpEnetLtFbTxInfoTData_Type(AsciiString):
    """Custom type lpEnetLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbTxInfoTData_Type.__name__ = "AsciiString"
_LpEnetLtFbTxInfoTData_Object = MibTableColumn
lpEnetLtFbTxInfoTData = _LpEnetLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 2, 10, 1, 1),
    _LpEnetLtFbTxInfoTData_Type()
)
lpEnetLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbTxInfoTData.setStatus("mandatory")
_LpEnetLtFbFddiMac_ObjectIdentity = ObjectIdentity
lpEnetLtFbFddiMac = _LpEnetLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3)
)
_LpEnetLtFbFddiMacRowStatusTable_Object = MibTable
lpEnetLtFbFddiMacRowStatusTable = _LpEnetLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacRowStatusTable.setStatus("mandatory")
_LpEnetLtFbFddiMacRowStatusEntry_Object = MibTableRow
lpEnetLtFbFddiMacRowStatusEntry = _LpEnetLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 1, 1)
)
lpEnetLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbFddiMacRowStatus_Type = RowStatus
_LpEnetLtFbFddiMacRowStatus_Object = MibTableColumn
lpEnetLtFbFddiMacRowStatus = _LpEnetLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 1, 1, 1),
    _LpEnetLtFbFddiMacRowStatus_Type()
)
lpEnetLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacRowStatus.setStatus("mandatory")
_LpEnetLtFbFddiMacComponentName_Type = DisplayString
_LpEnetLtFbFddiMacComponentName_Object = MibTableColumn
lpEnetLtFbFddiMacComponentName = _LpEnetLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 1, 1, 2),
    _LpEnetLtFbFddiMacComponentName_Type()
)
lpEnetLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacComponentName.setStatus("mandatory")
_LpEnetLtFbFddiMacStorageType_Type = StorageType
_LpEnetLtFbFddiMacStorageType_Object = MibTableColumn
lpEnetLtFbFddiMacStorageType = _LpEnetLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 1, 1, 4),
    _LpEnetLtFbFddiMacStorageType_Type()
)
lpEnetLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacStorageType.setStatus("mandatory")
_LpEnetLtFbFddiMacIndex_Type = NonReplicated
_LpEnetLtFbFddiMacIndex_Object = MibTableColumn
lpEnetLtFbFddiMacIndex = _LpEnetLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 1, 1, 10),
    _LpEnetLtFbFddiMacIndex_Type()
)
lpEnetLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacIndex.setStatus("mandatory")
_LpEnetLtFbFddiMacTopTable_Object = MibTable
lpEnetLtFbFddiMacTopTable = _LpEnetLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacTopTable.setStatus("mandatory")
_LpEnetLtFbFddiMacTopEntry_Object = MibTableRow
lpEnetLtFbFddiMacTopEntry = _LpEnetLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 10, 1)
)
lpEnetLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacTopEntry.setStatus("mandatory")


class _LpEnetLtFbFddiMacTData_Type(AsciiString):
    """Custom type lpEnetLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbFddiMacTData_Type.__name__ = "AsciiString"
_LpEnetLtFbFddiMacTData_Object = MibTableColumn
lpEnetLtFbFddiMacTData = _LpEnetLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 3, 10, 1, 1),
    _LpEnetLtFbFddiMacTData_Type()
)
lpEnetLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbFddiMacTData.setStatus("mandatory")
_LpEnetLtFbMacEnet_ObjectIdentity = ObjectIdentity
lpEnetLtFbMacEnet = _LpEnetLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4)
)
_LpEnetLtFbMacEnetRowStatusTable_Object = MibTable
lpEnetLtFbMacEnetRowStatusTable = _LpEnetLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetRowStatusTable.setStatus("mandatory")
_LpEnetLtFbMacEnetRowStatusEntry_Object = MibTableRow
lpEnetLtFbMacEnetRowStatusEntry = _LpEnetLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 1, 1)
)
lpEnetLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbMacEnetRowStatus_Type = RowStatus
_LpEnetLtFbMacEnetRowStatus_Object = MibTableColumn
lpEnetLtFbMacEnetRowStatus = _LpEnetLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 1, 1, 1),
    _LpEnetLtFbMacEnetRowStatus_Type()
)
lpEnetLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetRowStatus.setStatus("mandatory")
_LpEnetLtFbMacEnetComponentName_Type = DisplayString
_LpEnetLtFbMacEnetComponentName_Object = MibTableColumn
lpEnetLtFbMacEnetComponentName = _LpEnetLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 1, 1, 2),
    _LpEnetLtFbMacEnetComponentName_Type()
)
lpEnetLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetComponentName.setStatus("mandatory")
_LpEnetLtFbMacEnetStorageType_Type = StorageType
_LpEnetLtFbMacEnetStorageType_Object = MibTableColumn
lpEnetLtFbMacEnetStorageType = _LpEnetLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 1, 1, 4),
    _LpEnetLtFbMacEnetStorageType_Type()
)
lpEnetLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetStorageType.setStatus("mandatory")
_LpEnetLtFbMacEnetIndex_Type = NonReplicated
_LpEnetLtFbMacEnetIndex_Object = MibTableColumn
lpEnetLtFbMacEnetIndex = _LpEnetLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 1, 1, 10),
    _LpEnetLtFbMacEnetIndex_Type()
)
lpEnetLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetIndex.setStatus("mandatory")
_LpEnetLtFbMacEnetTopTable_Object = MibTable
lpEnetLtFbMacEnetTopTable = _LpEnetLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetTopTable.setStatus("mandatory")
_LpEnetLtFbMacEnetTopEntry_Object = MibTableRow
lpEnetLtFbMacEnetTopEntry = _LpEnetLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 10, 1)
)
lpEnetLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetTopEntry.setStatus("mandatory")


class _LpEnetLtFbMacEnetTData_Type(AsciiString):
    """Custom type lpEnetLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbMacEnetTData_Type.__name__ = "AsciiString"
_LpEnetLtFbMacEnetTData_Object = MibTableColumn
lpEnetLtFbMacEnetTData = _LpEnetLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 4, 10, 1, 1),
    _LpEnetLtFbMacEnetTData_Type()
)
lpEnetLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbMacEnetTData.setStatus("mandatory")
_LpEnetLtFbMacTr_ObjectIdentity = ObjectIdentity
lpEnetLtFbMacTr = _LpEnetLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5)
)
_LpEnetLtFbMacTrRowStatusTable_Object = MibTable
lpEnetLtFbMacTrRowStatusTable = _LpEnetLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrRowStatusTable.setStatus("mandatory")
_LpEnetLtFbMacTrRowStatusEntry_Object = MibTableRow
lpEnetLtFbMacTrRowStatusEntry = _LpEnetLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 1, 1)
)
lpEnetLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbMacTrRowStatus_Type = RowStatus
_LpEnetLtFbMacTrRowStatus_Object = MibTableColumn
lpEnetLtFbMacTrRowStatus = _LpEnetLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 1, 1, 1),
    _LpEnetLtFbMacTrRowStatus_Type()
)
lpEnetLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrRowStatus.setStatus("mandatory")
_LpEnetLtFbMacTrComponentName_Type = DisplayString
_LpEnetLtFbMacTrComponentName_Object = MibTableColumn
lpEnetLtFbMacTrComponentName = _LpEnetLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 1, 1, 2),
    _LpEnetLtFbMacTrComponentName_Type()
)
lpEnetLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrComponentName.setStatus("mandatory")
_LpEnetLtFbMacTrStorageType_Type = StorageType
_LpEnetLtFbMacTrStorageType_Object = MibTableColumn
lpEnetLtFbMacTrStorageType = _LpEnetLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 1, 1, 4),
    _LpEnetLtFbMacTrStorageType_Type()
)
lpEnetLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrStorageType.setStatus("mandatory")
_LpEnetLtFbMacTrIndex_Type = NonReplicated
_LpEnetLtFbMacTrIndex_Object = MibTableColumn
lpEnetLtFbMacTrIndex = _LpEnetLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 1, 1, 10),
    _LpEnetLtFbMacTrIndex_Type()
)
lpEnetLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrIndex.setStatus("mandatory")
_LpEnetLtFbMacTrTopTable_Object = MibTable
lpEnetLtFbMacTrTopTable = _LpEnetLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrTopTable.setStatus("mandatory")
_LpEnetLtFbMacTrTopEntry_Object = MibTableRow
lpEnetLtFbMacTrTopEntry = _LpEnetLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 10, 1)
)
lpEnetLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrTopEntry.setStatus("mandatory")


class _LpEnetLtFbMacTrTData_Type(AsciiString):
    """Custom type lpEnetLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbMacTrTData_Type.__name__ = "AsciiString"
_LpEnetLtFbMacTrTData_Object = MibTableColumn
lpEnetLtFbMacTrTData = _LpEnetLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 5, 10, 1, 1),
    _LpEnetLtFbMacTrTData_Type()
)
lpEnetLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbMacTrTData.setStatus("mandatory")
_LpEnetLtFbData_ObjectIdentity = ObjectIdentity
lpEnetLtFbData = _LpEnetLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6)
)
_LpEnetLtFbDataRowStatusTable_Object = MibTable
lpEnetLtFbDataRowStatusTable = _LpEnetLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbDataRowStatusTable.setStatus("mandatory")
_LpEnetLtFbDataRowStatusEntry_Object = MibTableRow
lpEnetLtFbDataRowStatusEntry = _LpEnetLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 1, 1)
)
lpEnetLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbDataRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbDataRowStatus_Type = RowStatus
_LpEnetLtFbDataRowStatus_Object = MibTableColumn
lpEnetLtFbDataRowStatus = _LpEnetLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 1, 1, 1),
    _LpEnetLtFbDataRowStatus_Type()
)
lpEnetLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbDataRowStatus.setStatus("mandatory")
_LpEnetLtFbDataComponentName_Type = DisplayString
_LpEnetLtFbDataComponentName_Object = MibTableColumn
lpEnetLtFbDataComponentName = _LpEnetLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 1, 1, 2),
    _LpEnetLtFbDataComponentName_Type()
)
lpEnetLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbDataComponentName.setStatus("mandatory")
_LpEnetLtFbDataStorageType_Type = StorageType
_LpEnetLtFbDataStorageType_Object = MibTableColumn
lpEnetLtFbDataStorageType = _LpEnetLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 1, 1, 4),
    _LpEnetLtFbDataStorageType_Type()
)
lpEnetLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbDataStorageType.setStatus("mandatory")
_LpEnetLtFbDataIndex_Type = NonReplicated
_LpEnetLtFbDataIndex_Object = MibTableColumn
lpEnetLtFbDataIndex = _LpEnetLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 1, 1, 10),
    _LpEnetLtFbDataIndex_Type()
)
lpEnetLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbDataIndex.setStatus("mandatory")
_LpEnetLtFbDataTopTable_Object = MibTable
lpEnetLtFbDataTopTable = _LpEnetLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbDataTopTable.setStatus("mandatory")
_LpEnetLtFbDataTopEntry_Object = MibTableRow
lpEnetLtFbDataTopEntry = _LpEnetLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 10, 1)
)
lpEnetLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbDataTopEntry.setStatus("mandatory")


class _LpEnetLtFbDataTData_Type(AsciiString):
    """Custom type lpEnetLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbDataTData_Type.__name__ = "AsciiString"
_LpEnetLtFbDataTData_Object = MibTableColumn
lpEnetLtFbDataTData = _LpEnetLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 6, 10, 1, 1),
    _LpEnetLtFbDataTData_Type()
)
lpEnetLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbDataTData.setStatus("mandatory")
_LpEnetLtFbIpH_ObjectIdentity = ObjectIdentity
lpEnetLtFbIpH = _LpEnetLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7)
)
_LpEnetLtFbIpHRowStatusTable_Object = MibTable
lpEnetLtFbIpHRowStatusTable = _LpEnetLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpHRowStatusTable.setStatus("mandatory")
_LpEnetLtFbIpHRowStatusEntry_Object = MibTableRow
lpEnetLtFbIpHRowStatusEntry = _LpEnetLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 1, 1)
)
lpEnetLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpHRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbIpHRowStatus_Type = RowStatus
_LpEnetLtFbIpHRowStatus_Object = MibTableColumn
lpEnetLtFbIpHRowStatus = _LpEnetLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 1, 1, 1),
    _LpEnetLtFbIpHRowStatus_Type()
)
lpEnetLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbIpHRowStatus.setStatus("mandatory")
_LpEnetLtFbIpHComponentName_Type = DisplayString
_LpEnetLtFbIpHComponentName_Object = MibTableColumn
lpEnetLtFbIpHComponentName = _LpEnetLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 1, 1, 2),
    _LpEnetLtFbIpHComponentName_Type()
)
lpEnetLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbIpHComponentName.setStatus("mandatory")
_LpEnetLtFbIpHStorageType_Type = StorageType
_LpEnetLtFbIpHStorageType_Object = MibTableColumn
lpEnetLtFbIpHStorageType = _LpEnetLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 1, 1, 4),
    _LpEnetLtFbIpHStorageType_Type()
)
lpEnetLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbIpHStorageType.setStatus("mandatory")
_LpEnetLtFbIpHIndex_Type = NonReplicated
_LpEnetLtFbIpHIndex_Object = MibTableColumn
lpEnetLtFbIpHIndex = _LpEnetLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 1, 1, 10),
    _LpEnetLtFbIpHIndex_Type()
)
lpEnetLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbIpHIndex.setStatus("mandatory")
_LpEnetLtFbIpHTopTable_Object = MibTable
lpEnetLtFbIpHTopTable = _LpEnetLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpHTopTable.setStatus("mandatory")
_LpEnetLtFbIpHTopEntry_Object = MibTableRow
lpEnetLtFbIpHTopEntry = _LpEnetLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 10, 1)
)
lpEnetLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpHTopEntry.setStatus("mandatory")


class _LpEnetLtFbIpHTData_Type(AsciiString):
    """Custom type lpEnetLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbIpHTData_Type.__name__ = "AsciiString"
_LpEnetLtFbIpHTData_Object = MibTableColumn
lpEnetLtFbIpHTData = _LpEnetLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 7, 10, 1, 1),
    _LpEnetLtFbIpHTData_Type()
)
lpEnetLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbIpHTData.setStatus("mandatory")
_LpEnetLtFbLlch_ObjectIdentity = ObjectIdentity
lpEnetLtFbLlch = _LpEnetLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8)
)
_LpEnetLtFbLlchRowStatusTable_Object = MibTable
lpEnetLtFbLlchRowStatusTable = _LpEnetLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbLlchRowStatusTable.setStatus("mandatory")
_LpEnetLtFbLlchRowStatusEntry_Object = MibTableRow
lpEnetLtFbLlchRowStatusEntry = _LpEnetLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 1, 1)
)
lpEnetLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbLlchRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbLlchRowStatus_Type = RowStatus
_LpEnetLtFbLlchRowStatus_Object = MibTableColumn
lpEnetLtFbLlchRowStatus = _LpEnetLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 1, 1, 1),
    _LpEnetLtFbLlchRowStatus_Type()
)
lpEnetLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbLlchRowStatus.setStatus("mandatory")
_LpEnetLtFbLlchComponentName_Type = DisplayString
_LpEnetLtFbLlchComponentName_Object = MibTableColumn
lpEnetLtFbLlchComponentName = _LpEnetLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 1, 1, 2),
    _LpEnetLtFbLlchComponentName_Type()
)
lpEnetLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbLlchComponentName.setStatus("mandatory")
_LpEnetLtFbLlchStorageType_Type = StorageType
_LpEnetLtFbLlchStorageType_Object = MibTableColumn
lpEnetLtFbLlchStorageType = _LpEnetLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 1, 1, 4),
    _LpEnetLtFbLlchStorageType_Type()
)
lpEnetLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbLlchStorageType.setStatus("mandatory")
_LpEnetLtFbLlchIndex_Type = NonReplicated
_LpEnetLtFbLlchIndex_Object = MibTableColumn
lpEnetLtFbLlchIndex = _LpEnetLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 1, 1, 10),
    _LpEnetLtFbLlchIndex_Type()
)
lpEnetLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbLlchIndex.setStatus("mandatory")
_LpEnetLtFbLlchTopTable_Object = MibTable
lpEnetLtFbLlchTopTable = _LpEnetLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbLlchTopTable.setStatus("mandatory")
_LpEnetLtFbLlchTopEntry_Object = MibTableRow
lpEnetLtFbLlchTopEntry = _LpEnetLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 10, 1)
)
lpEnetLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbLlchTopEntry.setStatus("mandatory")


class _LpEnetLtFbLlchTData_Type(AsciiString):
    """Custom type lpEnetLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbLlchTData_Type.__name__ = "AsciiString"
_LpEnetLtFbLlchTData_Object = MibTableColumn
lpEnetLtFbLlchTData = _LpEnetLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 8, 10, 1, 1),
    _LpEnetLtFbLlchTData_Type()
)
lpEnetLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbLlchTData.setStatus("mandatory")
_LpEnetLtFbAppleH_ObjectIdentity = ObjectIdentity
lpEnetLtFbAppleH = _LpEnetLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9)
)
_LpEnetLtFbAppleHRowStatusTable_Object = MibTable
lpEnetLtFbAppleHRowStatusTable = _LpEnetLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHRowStatusTable.setStatus("mandatory")
_LpEnetLtFbAppleHRowStatusEntry_Object = MibTableRow
lpEnetLtFbAppleHRowStatusEntry = _LpEnetLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 1, 1)
)
lpEnetLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbAppleHRowStatus_Type = RowStatus
_LpEnetLtFbAppleHRowStatus_Object = MibTableColumn
lpEnetLtFbAppleHRowStatus = _LpEnetLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 1, 1, 1),
    _LpEnetLtFbAppleHRowStatus_Type()
)
lpEnetLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHRowStatus.setStatus("mandatory")
_LpEnetLtFbAppleHComponentName_Type = DisplayString
_LpEnetLtFbAppleHComponentName_Object = MibTableColumn
lpEnetLtFbAppleHComponentName = _LpEnetLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 1, 1, 2),
    _LpEnetLtFbAppleHComponentName_Type()
)
lpEnetLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHComponentName.setStatus("mandatory")
_LpEnetLtFbAppleHStorageType_Type = StorageType
_LpEnetLtFbAppleHStorageType_Object = MibTableColumn
lpEnetLtFbAppleHStorageType = _LpEnetLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 1, 1, 4),
    _LpEnetLtFbAppleHStorageType_Type()
)
lpEnetLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHStorageType.setStatus("mandatory")
_LpEnetLtFbAppleHIndex_Type = NonReplicated
_LpEnetLtFbAppleHIndex_Object = MibTableColumn
lpEnetLtFbAppleHIndex = _LpEnetLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 1, 1, 10),
    _LpEnetLtFbAppleHIndex_Type()
)
lpEnetLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHIndex.setStatus("mandatory")
_LpEnetLtFbAppleHTopTable_Object = MibTable
lpEnetLtFbAppleHTopTable = _LpEnetLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHTopTable.setStatus("mandatory")
_LpEnetLtFbAppleHTopEntry_Object = MibTableRow
lpEnetLtFbAppleHTopEntry = _LpEnetLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 10, 1)
)
lpEnetLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHTopEntry.setStatus("mandatory")


class _LpEnetLtFbAppleHTData_Type(AsciiString):
    """Custom type lpEnetLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbAppleHTData_Type.__name__ = "AsciiString"
_LpEnetLtFbAppleHTData_Object = MibTableColumn
lpEnetLtFbAppleHTData = _LpEnetLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 9, 10, 1, 1),
    _LpEnetLtFbAppleHTData_Type()
)
lpEnetLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbAppleHTData.setStatus("mandatory")
_LpEnetLtFbIpxH_ObjectIdentity = ObjectIdentity
lpEnetLtFbIpxH = _LpEnetLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10)
)
_LpEnetLtFbIpxHRowStatusTable_Object = MibTable
lpEnetLtFbIpxHRowStatusTable = _LpEnetLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHRowStatusTable.setStatus("mandatory")
_LpEnetLtFbIpxHRowStatusEntry_Object = MibTableRow
lpEnetLtFbIpxHRowStatusEntry = _LpEnetLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 1, 1)
)
lpEnetLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHRowStatusEntry.setStatus("mandatory")
_LpEnetLtFbIpxHRowStatus_Type = RowStatus
_LpEnetLtFbIpxHRowStatus_Object = MibTableColumn
lpEnetLtFbIpxHRowStatus = _LpEnetLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 1, 1, 1),
    _LpEnetLtFbIpxHRowStatus_Type()
)
lpEnetLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHRowStatus.setStatus("mandatory")
_LpEnetLtFbIpxHComponentName_Type = DisplayString
_LpEnetLtFbIpxHComponentName_Object = MibTableColumn
lpEnetLtFbIpxHComponentName = _LpEnetLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 1, 1, 2),
    _LpEnetLtFbIpxHComponentName_Type()
)
lpEnetLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHComponentName.setStatus("mandatory")
_LpEnetLtFbIpxHStorageType_Type = StorageType
_LpEnetLtFbIpxHStorageType_Object = MibTableColumn
lpEnetLtFbIpxHStorageType = _LpEnetLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 1, 1, 4),
    _LpEnetLtFbIpxHStorageType_Type()
)
lpEnetLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHStorageType.setStatus("mandatory")
_LpEnetLtFbIpxHIndex_Type = NonReplicated
_LpEnetLtFbIpxHIndex_Object = MibTableColumn
lpEnetLtFbIpxHIndex = _LpEnetLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 1, 1, 10),
    _LpEnetLtFbIpxHIndex_Type()
)
lpEnetLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHIndex.setStatus("mandatory")
_LpEnetLtFbIpxHTopTable_Object = MibTable
lpEnetLtFbIpxHTopTable = _LpEnetLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHTopTable.setStatus("mandatory")
_LpEnetLtFbIpxHTopEntry_Object = MibTableRow
lpEnetLtFbIpxHTopEntry = _LpEnetLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 10, 1)
)
lpEnetLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHTopEntry.setStatus("mandatory")


class _LpEnetLtFbIpxHTData_Type(AsciiString):
    """Custom type lpEnetLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbIpxHTData_Type.__name__ = "AsciiString"
_LpEnetLtFbIpxHTData_Object = MibTableColumn
lpEnetLtFbIpxHTData = _LpEnetLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 10, 10, 1, 1),
    _LpEnetLtFbIpxHTData_Type()
)
lpEnetLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbIpxHTData.setStatus("mandatory")
_LpEnetLtFbTopTable_Object = MibTable
lpEnetLtFbTopTable = _LpEnetLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 20)
)
if mibBuilder.loadTexts:
    lpEnetLtFbTopTable.setStatus("mandatory")
_LpEnetLtFbTopEntry_Object = MibTableRow
lpEnetLtFbTopEntry = _LpEnetLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 20, 1)
)
lpEnetLtFbTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtFbTopEntry.setStatus("mandatory")


class _LpEnetLtFbTData_Type(AsciiString):
    """Custom type lpEnetLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtFbTData_Type.__name__ = "AsciiString"
_LpEnetLtFbTData_Object = MibTableColumn
lpEnetLtFbTData = _LpEnetLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 5, 20, 1, 1),
    _LpEnetLtFbTData_Type()
)
lpEnetLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtFbTData.setStatus("mandatory")
_LpEnetLtCntl_ObjectIdentity = ObjectIdentity
lpEnetLtCntl = _LpEnetLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6)
)
_LpEnetLtCntlRowStatusTable_Object = MibTable
lpEnetLtCntlRowStatusTable = _LpEnetLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    lpEnetLtCntlRowStatusTable.setStatus("mandatory")
_LpEnetLtCntlRowStatusEntry_Object = MibTableRow
lpEnetLtCntlRowStatusEntry = _LpEnetLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 1, 1)
)
lpEnetLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtCntlRowStatusEntry.setStatus("mandatory")
_LpEnetLtCntlRowStatus_Type = RowStatus
_LpEnetLtCntlRowStatus_Object = MibTableColumn
lpEnetLtCntlRowStatus = _LpEnetLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 1, 1, 1),
    _LpEnetLtCntlRowStatus_Type()
)
lpEnetLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtCntlRowStatus.setStatus("mandatory")
_LpEnetLtCntlComponentName_Type = DisplayString
_LpEnetLtCntlComponentName_Object = MibTableColumn
lpEnetLtCntlComponentName = _LpEnetLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 1, 1, 2),
    _LpEnetLtCntlComponentName_Type()
)
lpEnetLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtCntlComponentName.setStatus("mandatory")
_LpEnetLtCntlStorageType_Type = StorageType
_LpEnetLtCntlStorageType_Object = MibTableColumn
lpEnetLtCntlStorageType = _LpEnetLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 1, 1, 4),
    _LpEnetLtCntlStorageType_Type()
)
lpEnetLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLtCntlStorageType.setStatus("mandatory")
_LpEnetLtCntlIndex_Type = NonReplicated
_LpEnetLtCntlIndex_Object = MibTableColumn
lpEnetLtCntlIndex = _LpEnetLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 1, 1, 10),
    _LpEnetLtCntlIndex_Type()
)
lpEnetLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetLtCntlIndex.setStatus("mandatory")
_LpEnetLtCntlTopTable_Object = MibTable
lpEnetLtCntlTopTable = _LpEnetLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 10)
)
if mibBuilder.loadTexts:
    lpEnetLtCntlTopTable.setStatus("mandatory")
_LpEnetLtCntlTopEntry_Object = MibTableRow
lpEnetLtCntlTopEntry = _LpEnetLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 10, 1)
)
lpEnetLtCntlTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtCntlTopEntry.setStatus("mandatory")


class _LpEnetLtCntlTData_Type(AsciiString):
    """Custom type lpEnetLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtCntlTData_Type.__name__ = "AsciiString"
_LpEnetLtCntlTData_Object = MibTableColumn
lpEnetLtCntlTData = _LpEnetLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 6, 10, 1, 1),
    _LpEnetLtCntlTData_Type()
)
lpEnetLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtCntlTData.setStatus("mandatory")
_LpEnetLtTopTable_Object = MibTable
lpEnetLtTopTable = _LpEnetLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 20)
)
if mibBuilder.loadTexts:
    lpEnetLtTopTable.setStatus("mandatory")
_LpEnetLtTopEntry_Object = MibTableRow
lpEnetLtTopEntry = _LpEnetLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 20, 1)
)
lpEnetLtTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetLtIndex"),
)
if mibBuilder.loadTexts:
    lpEnetLtTopEntry.setStatus("mandatory")


class _LpEnetLtTData_Type(AsciiString):
    """Custom type lpEnetLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEnetLtTData_Type.__name__ = "AsciiString"
_LpEnetLtTData_Object = MibTableColumn
lpEnetLtTData = _LpEnetLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 2, 20, 1, 1),
    _LpEnetLtTData_Type()
)
lpEnetLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetLtTData.setStatus("mandatory")
_LpEnetTest_ObjectIdentity = ObjectIdentity
lpEnetTest = _LpEnetTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5)
)
_LpEnetTestRowStatusTable_Object = MibTable
lpEnetTestRowStatusTable = _LpEnetTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 1)
)
if mibBuilder.loadTexts:
    lpEnetTestRowStatusTable.setStatus("mandatory")
_LpEnetTestRowStatusEntry_Object = MibTableRow
lpEnetTestRowStatusEntry = _LpEnetTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 1, 1)
)
lpEnetTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetTestIndex"),
)
if mibBuilder.loadTexts:
    lpEnetTestRowStatusEntry.setStatus("mandatory")
_LpEnetTestRowStatus_Type = RowStatus
_LpEnetTestRowStatus_Object = MibTableColumn
lpEnetTestRowStatus = _LpEnetTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 1, 1, 1),
    _LpEnetTestRowStatus_Type()
)
lpEnetTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestRowStatus.setStatus("mandatory")
_LpEnetTestComponentName_Type = DisplayString
_LpEnetTestComponentName_Object = MibTableColumn
lpEnetTestComponentName = _LpEnetTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 1, 1, 2),
    _LpEnetTestComponentName_Type()
)
lpEnetTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestComponentName.setStatus("mandatory")
_LpEnetTestStorageType_Type = StorageType
_LpEnetTestStorageType_Object = MibTableColumn
lpEnetTestStorageType = _LpEnetTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 1, 1, 4),
    _LpEnetTestStorageType_Type()
)
lpEnetTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestStorageType.setStatus("mandatory")
_LpEnetTestIndex_Type = NonReplicated
_LpEnetTestIndex_Object = MibTableColumn
lpEnetTestIndex = _LpEnetTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 1, 1, 10),
    _LpEnetTestIndex_Type()
)
lpEnetTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEnetTestIndex.setStatus("mandatory")
_LpEnetTestPTOTable_Object = MibTable
lpEnetTestPTOTable = _LpEnetTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 10)
)
if mibBuilder.loadTexts:
    lpEnetTestPTOTable.setStatus("mandatory")
_LpEnetTestPTOEntry_Object = MibTableRow
lpEnetTestPTOEntry = _LpEnetTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 10, 1)
)
lpEnetTestPTOEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetTestIndex"),
)
if mibBuilder.loadTexts:
    lpEnetTestPTOEntry.setStatus("mandatory")


class _LpEnetTestType_Type(Integer32):
    """Custom type lpEnetTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              257,
              258,
              259,
              260,
              263,
              264,
              265,
              266,
              267,
              268)
        )
    )
    namedValues = NamedValues(
        *(("extThruA", 265),
          ("extThruB", 266),
          ("extWrapA", 263),
          ("extWrapAB", 267),
          ("extWrapB", 264),
          ("extWrapBA", 268),
          ("normal", 1),
          ("onCard", 0),
          ("thruA", 259),
          ("thruB", 260),
          ("wrapA", 257),
          ("wrapB", 258))
    )


_LpEnetTestType_Type.__name__ = "Integer32"
_LpEnetTestType_Object = MibTableColumn
lpEnetTestType = _LpEnetTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 10, 1, 1),
    _LpEnetTestType_Type()
)
lpEnetTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetTestType.setStatus("mandatory")


class _LpEnetTestFrmSize_Type(Unsigned32):
    """Custom type lpEnetTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpEnetTestFrmSize_Type.__name__ = "Unsigned32"
_LpEnetTestFrmSize_Object = MibTableColumn
lpEnetTestFrmSize = _LpEnetTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 10, 1, 2),
    _LpEnetTestFrmSize_Type()
)
lpEnetTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetTestFrmSize.setStatus("mandatory")


class _LpEnetTestDuration_Type(Unsigned32):
    """Custom type lpEnetTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpEnetTestDuration_Type.__name__ = "Unsigned32"
_LpEnetTestDuration_Object = MibTableColumn
lpEnetTestDuration = _LpEnetTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 10, 1, 3),
    _LpEnetTestDuration_Type()
)
lpEnetTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetTestDuration.setStatus("mandatory")
_LpEnetTestResultsTable_Object = MibTable
lpEnetTestResultsTable = _LpEnetTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11)
)
if mibBuilder.loadTexts:
    lpEnetTestResultsTable.setStatus("mandatory")
_LpEnetTestResultsEntry_Object = MibTableRow
lpEnetTestResultsEntry = _LpEnetTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1)
)
lpEnetTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetTestIndex"),
)
if mibBuilder.loadTexts:
    lpEnetTestResultsEntry.setStatus("mandatory")
_LpEnetTestElapsedTime_Type = Counter32
_LpEnetTestElapsedTime_Object = MibTableColumn
lpEnetTestElapsedTime = _LpEnetTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 4),
    _LpEnetTestElapsedTime_Type()
)
lpEnetTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestElapsedTime.setStatus("mandatory")


class _LpEnetTestTimeRemaining_Type(Unsigned32):
    """Custom type lpEnetTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpEnetTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpEnetTestTimeRemaining_Object = MibTableColumn
lpEnetTestTimeRemaining = _LpEnetTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 5),
    _LpEnetTestTimeRemaining_Type()
)
lpEnetTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestTimeRemaining.setStatus("mandatory")


class _LpEnetTestCauseOfTermination_Type(Integer32):
    """Custom type lpEnetTestCauseOfTermination based on Integer32"""
    defaultValue = 3

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
        *(("neverStarted", 3),
          ("stoppedByOperator", 1),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_LpEnetTestCauseOfTermination_Type.__name__ = "Integer32"
_LpEnetTestCauseOfTermination_Object = MibTableColumn
lpEnetTestCauseOfTermination = _LpEnetTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 6),
    _LpEnetTestCauseOfTermination_Type()
)
lpEnetTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestCauseOfTermination.setStatus("mandatory")
_LpEnetTestFrmTx_Type = PassportCounter64
_LpEnetTestFrmTx_Object = MibTableColumn
lpEnetTestFrmTx = _LpEnetTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 7),
    _LpEnetTestFrmTx_Type()
)
lpEnetTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestFrmTx.setStatus("mandatory")
_LpEnetTestBitsTx_Type = PassportCounter64
_LpEnetTestBitsTx_Object = MibTableColumn
lpEnetTestBitsTx = _LpEnetTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 8),
    _LpEnetTestBitsTx_Type()
)
lpEnetTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestBitsTx.setStatus("mandatory")
_LpEnetTestFrmRx_Type = PassportCounter64
_LpEnetTestFrmRx_Object = MibTableColumn
lpEnetTestFrmRx = _LpEnetTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 9),
    _LpEnetTestFrmRx_Type()
)
lpEnetTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestFrmRx.setStatus("mandatory")
_LpEnetTestBitsRx_Type = PassportCounter64
_LpEnetTestBitsRx_Object = MibTableColumn
lpEnetTestBitsRx = _LpEnetTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 10),
    _LpEnetTestBitsRx_Type()
)
lpEnetTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestBitsRx.setStatus("mandatory")
_LpEnetTestErroredFrmRx_Type = PassportCounter64
_LpEnetTestErroredFrmRx_Object = MibTableColumn
lpEnetTestErroredFrmRx = _LpEnetTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 5, 11, 1, 11),
    _LpEnetTestErroredFrmRx_Type()
)
lpEnetTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetTestErroredFrmRx.setStatus("mandatory")
_LpEnetCidDataTable_Object = MibTable
lpEnetCidDataTable = _LpEnetCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 10)
)
if mibBuilder.loadTexts:
    lpEnetCidDataTable.setStatus("mandatory")
_LpEnetCidDataEntry_Object = MibTableRow
lpEnetCidDataEntry = _LpEnetCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 10, 1)
)
lpEnetCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetCidDataEntry.setStatus("mandatory")


class _LpEnetCustomerIdentifier_Type(Unsigned32):
    """Custom type lpEnetCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpEnetCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpEnetCustomerIdentifier_Object = MibTableColumn
lpEnetCustomerIdentifier = _LpEnetCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 10, 1, 1),
    _LpEnetCustomerIdentifier_Type()
)
lpEnetCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetCustomerIdentifier.setStatus("mandatory")
_LpEnetIfEntryTable_Object = MibTable
lpEnetIfEntryTable = _LpEnetIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 11)
)
if mibBuilder.loadTexts:
    lpEnetIfEntryTable.setStatus("mandatory")
_LpEnetIfEntryEntry_Object = MibTableRow
lpEnetIfEntryEntry = _LpEnetIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 11, 1)
)
lpEnetIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetIfEntryEntry.setStatus("mandatory")


class _LpEnetIfAdminStatus_Type(Integer32):
    """Custom type lpEnetIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpEnetIfAdminStatus_Type.__name__ = "Integer32"
_LpEnetIfAdminStatus_Object = MibTableColumn
lpEnetIfAdminStatus = _LpEnetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 11, 1, 1),
    _LpEnetIfAdminStatus_Type()
)
lpEnetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetIfAdminStatus.setStatus("mandatory")


class _LpEnetIfIndex_Type(InterfaceIndex):
    """Custom type lpEnetIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpEnetIfIndex_Type.__name__ = "InterfaceIndex"
_LpEnetIfIndex_Object = MibTableColumn
lpEnetIfIndex = _LpEnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 11, 1, 2),
    _LpEnetIfIndex_Type()
)
lpEnetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetIfIndex.setStatus("mandatory")
_LpEnetProvTable_Object = MibTable
lpEnetProvTable = _LpEnetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 12)
)
if mibBuilder.loadTexts:
    lpEnetProvTable.setStatus("mandatory")
_LpEnetProvEntry_Object = MibTableRow
lpEnetProvEntry = _LpEnetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 12, 1)
)
lpEnetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetProvEntry.setStatus("mandatory")


class _LpEnetHeartbeatPacket_Type(Integer32):
    """Custom type lpEnetHeartbeatPacket based on Integer32"""
    defaultValue = 1

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


_LpEnetHeartbeatPacket_Type.__name__ = "Integer32"
_LpEnetHeartbeatPacket_Object = MibTableColumn
lpEnetHeartbeatPacket = _LpEnetHeartbeatPacket_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 12, 1, 1),
    _LpEnetHeartbeatPacket_Type()
)
lpEnetHeartbeatPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetHeartbeatPacket.setStatus("mandatory")
_LpEnetApplicationFramerName_Type = Link
_LpEnetApplicationFramerName_Object = MibTableColumn
lpEnetApplicationFramerName = _LpEnetApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 12, 1, 2),
    _LpEnetApplicationFramerName_Type()
)
lpEnetApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetApplicationFramerName.setStatus("mandatory")
_LpEnetAdminInfoTable_Object = MibTable
lpEnetAdminInfoTable = _LpEnetAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 13)
)
if mibBuilder.loadTexts:
    lpEnetAdminInfoTable.setStatus("mandatory")
_LpEnetAdminInfoEntry_Object = MibTableRow
lpEnetAdminInfoEntry = _LpEnetAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 13, 1)
)
lpEnetAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetAdminInfoEntry.setStatus("mandatory")


class _LpEnetVendor_Type(AsciiString):
    """Custom type lpEnetVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpEnetVendor_Type.__name__ = "AsciiString"
_LpEnetVendor_Object = MibTableColumn
lpEnetVendor = _LpEnetVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 13, 1, 1),
    _LpEnetVendor_Type()
)
lpEnetVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetVendor.setStatus("mandatory")


class _LpEnetCommentText_Type(AsciiString):
    """Custom type lpEnetCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpEnetCommentText_Type.__name__ = "AsciiString"
_LpEnetCommentText_Object = MibTableColumn
lpEnetCommentText = _LpEnetCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 13, 1, 2),
    _LpEnetCommentText_Type()
)
lpEnetCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEnetCommentText.setStatus("mandatory")
_LpEnetStateTable_Object = MibTable
lpEnetStateTable = _LpEnetStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 15)
)
if mibBuilder.loadTexts:
    lpEnetStateTable.setStatus("mandatory")
_LpEnetStateEntry_Object = MibTableRow
lpEnetStateEntry = _LpEnetStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 15, 1)
)
lpEnetStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetStateEntry.setStatus("mandatory")


class _LpEnetAdminState_Type(Integer32):
    """Custom type lpEnetAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_LpEnetAdminState_Type.__name__ = "Integer32"
_LpEnetAdminState_Object = MibTableColumn
lpEnetAdminState = _LpEnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 15, 1, 1),
    _LpEnetAdminState_Type()
)
lpEnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetAdminState.setStatus("mandatory")


class _LpEnetOperationalState_Type(Integer32):
    """Custom type lpEnetOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LpEnetOperationalState_Type.__name__ = "Integer32"
_LpEnetOperationalState_Object = MibTableColumn
lpEnetOperationalState = _LpEnetOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 15, 1, 2),
    _LpEnetOperationalState_Type()
)
lpEnetOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetOperationalState.setStatus("mandatory")


class _LpEnetUsageState_Type(Integer32):
    """Custom type lpEnetUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_LpEnetUsageState_Type.__name__ = "Integer32"
_LpEnetUsageState_Object = MibTableColumn
lpEnetUsageState = _LpEnetUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 15, 1, 3),
    _LpEnetUsageState_Type()
)
lpEnetUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetUsageState.setStatus("mandatory")
_LpEnetOperStatusTable_Object = MibTable
lpEnetOperStatusTable = _LpEnetOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 16)
)
if mibBuilder.loadTexts:
    lpEnetOperStatusTable.setStatus("mandatory")
_LpEnetOperStatusEntry_Object = MibTableRow
lpEnetOperStatusEntry = _LpEnetOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 16, 1)
)
lpEnetOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetOperStatusEntry.setStatus("mandatory")


class _LpEnetSnmpOperStatus_Type(Integer32):
    """Custom type lpEnetSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpEnetSnmpOperStatus_Type.__name__ = "Integer32"
_LpEnetSnmpOperStatus_Object = MibTableColumn
lpEnetSnmpOperStatus = _LpEnetSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 16, 1, 1),
    _LpEnetSnmpOperStatus_Type()
)
lpEnetSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetSnmpOperStatus.setStatus("mandatory")
_LpEnetOperTable_Object = MibTable
lpEnetOperTable = _LpEnetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 17)
)
if mibBuilder.loadTexts:
    lpEnetOperTable.setStatus("mandatory")
_LpEnetOperEntry_Object = MibTableRow
lpEnetOperEntry = _LpEnetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 17, 1)
)
lpEnetOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetOperEntry.setStatus("mandatory")


class _LpEnetMacAddress_Type(MacAddress):
    """Custom type lpEnetMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpEnetMacAddress_Type.__name__ = "MacAddress"
_LpEnetMacAddress_Object = MibTableColumn
lpEnetMacAddress = _LpEnetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 17, 1, 1),
    _LpEnetMacAddress_Type()
)
lpEnetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetMacAddress.setStatus("mandatory")
_LpEnetStatsTable_Object = MibTable
lpEnetStatsTable = _LpEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18)
)
if mibBuilder.loadTexts:
    lpEnetStatsTable.setStatus("mandatory")
_LpEnetStatsEntry_Object = MibTableRow
lpEnetStatsEntry = _LpEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1)
)
lpEnetStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEnetStatsEntry.setStatus("mandatory")
_LpEnetAlignmentErrors_Type = Counter32
_LpEnetAlignmentErrors_Object = MibTableColumn
lpEnetAlignmentErrors = _LpEnetAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 2),
    _LpEnetAlignmentErrors_Type()
)
lpEnetAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetAlignmentErrors.setStatus("mandatory")
_LpEnetFcsErrors_Type = Counter32
_LpEnetFcsErrors_Object = MibTableColumn
lpEnetFcsErrors = _LpEnetFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 3),
    _LpEnetFcsErrors_Type()
)
lpEnetFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetFcsErrors.setStatus("mandatory")
_LpEnetSingleCollisionFrames_Type = Counter32
_LpEnetSingleCollisionFrames_Object = MibTableColumn
lpEnetSingleCollisionFrames = _LpEnetSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 4),
    _LpEnetSingleCollisionFrames_Type()
)
lpEnetSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetSingleCollisionFrames.setStatus("mandatory")
_LpEnetMultipleCollisionFrames_Type = Counter32
_LpEnetMultipleCollisionFrames_Object = MibTableColumn
lpEnetMultipleCollisionFrames = _LpEnetMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 5),
    _LpEnetMultipleCollisionFrames_Type()
)
lpEnetMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetMultipleCollisionFrames.setStatus("mandatory")
_LpEnetSqeTestErrors_Type = Counter32
_LpEnetSqeTestErrors_Object = MibTableColumn
lpEnetSqeTestErrors = _LpEnetSqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 6),
    _LpEnetSqeTestErrors_Type()
)
lpEnetSqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetSqeTestErrors.setStatus("mandatory")
_LpEnetDeferredTransmissions_Type = Counter32
_LpEnetDeferredTransmissions_Object = MibTableColumn
lpEnetDeferredTransmissions = _LpEnetDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 7),
    _LpEnetDeferredTransmissions_Type()
)
lpEnetDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetDeferredTransmissions.setStatus("mandatory")
_LpEnetLateCollisions_Type = Counter32
_LpEnetLateCollisions_Object = MibTableColumn
lpEnetLateCollisions = _LpEnetLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 8),
    _LpEnetLateCollisions_Type()
)
lpEnetLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetLateCollisions.setStatus("mandatory")
_LpEnetExcessiveCollisions_Type = Counter32
_LpEnetExcessiveCollisions_Object = MibTableColumn
lpEnetExcessiveCollisions = _LpEnetExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 9),
    _LpEnetExcessiveCollisions_Type()
)
lpEnetExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetExcessiveCollisions.setStatus("mandatory")
_LpEnetMacTransmitErrors_Type = Counter32
_LpEnetMacTransmitErrors_Object = MibTableColumn
lpEnetMacTransmitErrors = _LpEnetMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 10),
    _LpEnetMacTransmitErrors_Type()
)
lpEnetMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetMacTransmitErrors.setStatus("mandatory")
_LpEnetCarrierSenseErrors_Type = Counter32
_LpEnetCarrierSenseErrors_Object = MibTableColumn
lpEnetCarrierSenseErrors = _LpEnetCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 11),
    _LpEnetCarrierSenseErrors_Type()
)
lpEnetCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetCarrierSenseErrors.setStatus("mandatory")
_LpEnetFrameTooLongs_Type = Counter32
_LpEnetFrameTooLongs_Object = MibTableColumn
lpEnetFrameTooLongs = _LpEnetFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 12),
    _LpEnetFrameTooLongs_Type()
)
lpEnetFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetFrameTooLongs.setStatus("mandatory")
_LpEnetMacReceiveErrors_Type = Counter32
_LpEnetMacReceiveErrors_Object = MibTableColumn
lpEnetMacReceiveErrors = _LpEnetMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 3, 18, 1, 13),
    _LpEnetMacReceiveErrors_Type()
)
lpEnetMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEnetMacReceiveErrors.setStatus("mandatory")
_LpFi_ObjectIdentity = ObjectIdentity
lpFi = _LpFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4)
)
_LpFiRowStatusTable_Object = MibTable
lpFiRowStatusTable = _LpFiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 1)
)
if mibBuilder.loadTexts:
    lpFiRowStatusTable.setStatus("mandatory")
_LpFiRowStatusEntry_Object = MibTableRow
lpFiRowStatusEntry = _LpFiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 1, 1)
)
lpFiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiRowStatusEntry.setStatus("mandatory")
_LpFiRowStatus_Type = RowStatus
_LpFiRowStatus_Object = MibTableColumn
lpFiRowStatus = _LpFiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 1, 1, 1),
    _LpFiRowStatus_Type()
)
lpFiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiRowStatus.setStatus("mandatory")
_LpFiComponentName_Type = DisplayString
_LpFiComponentName_Object = MibTableColumn
lpFiComponentName = _LpFiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 1, 1, 2),
    _LpFiComponentName_Type()
)
lpFiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiComponentName.setStatus("mandatory")
_LpFiStorageType_Type = StorageType
_LpFiStorageType_Object = MibTableColumn
lpFiStorageType = _LpFiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 1, 1, 4),
    _LpFiStorageType_Type()
)
lpFiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiStorageType.setStatus("mandatory")


class _LpFiIndex_Type(Integer32):
    """Custom type lpFiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LpFiIndex_Type.__name__ = "Integer32"
_LpFiIndex_Object = MibTableColumn
lpFiIndex = _LpFiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 1, 1, 10),
    _LpFiIndex_Type()
)
lpFiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiIndex.setStatus("mandatory")
_LpFiLt_ObjectIdentity = ObjectIdentity
lpFiLt = _LpFiLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2)
)
_LpFiLtRowStatusTable_Object = MibTable
lpFiLtRowStatusTable = _LpFiLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lpFiLtRowStatusTable.setStatus("mandatory")
_LpFiLtRowStatusEntry_Object = MibTableRow
lpFiLtRowStatusEntry = _LpFiLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 1, 1)
)
lpFiLtRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtRowStatusEntry.setStatus("mandatory")
_LpFiLtRowStatus_Type = RowStatus
_LpFiLtRowStatus_Object = MibTableColumn
lpFiLtRowStatus = _LpFiLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 1, 1, 1),
    _LpFiLtRowStatus_Type()
)
lpFiLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtRowStatus.setStatus("mandatory")
_LpFiLtComponentName_Type = DisplayString
_LpFiLtComponentName_Object = MibTableColumn
lpFiLtComponentName = _LpFiLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 1, 1, 2),
    _LpFiLtComponentName_Type()
)
lpFiLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtComponentName.setStatus("mandatory")
_LpFiLtStorageType_Type = StorageType
_LpFiLtStorageType_Object = MibTableColumn
lpFiLtStorageType = _LpFiLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 1, 1, 4),
    _LpFiLtStorageType_Type()
)
lpFiLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtStorageType.setStatus("mandatory")
_LpFiLtIndex_Type = NonReplicated
_LpFiLtIndex_Object = MibTableColumn
lpFiLtIndex = _LpFiLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 1, 1, 10),
    _LpFiLtIndex_Type()
)
lpFiLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtIndex.setStatus("mandatory")
_LpFiLtFrmCmp_ObjectIdentity = ObjectIdentity
lpFiLtFrmCmp = _LpFiLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2)
)
_LpFiLtFrmCmpRowStatusTable_Object = MibTable
lpFiLtFrmCmpRowStatusTable = _LpFiLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFrmCmpRowStatusTable.setStatus("mandatory")
_LpFiLtFrmCmpRowStatusEntry_Object = MibTableRow
lpFiLtFrmCmpRowStatusEntry = _LpFiLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 1, 1)
)
lpFiLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFrmCmpRowStatusEntry.setStatus("mandatory")
_LpFiLtFrmCmpRowStatus_Type = RowStatus
_LpFiLtFrmCmpRowStatus_Object = MibTableColumn
lpFiLtFrmCmpRowStatus = _LpFiLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 1, 1, 1),
    _LpFiLtFrmCmpRowStatus_Type()
)
lpFiLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFrmCmpRowStatus.setStatus("mandatory")
_LpFiLtFrmCmpComponentName_Type = DisplayString
_LpFiLtFrmCmpComponentName_Object = MibTableColumn
lpFiLtFrmCmpComponentName = _LpFiLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 1, 1, 2),
    _LpFiLtFrmCmpComponentName_Type()
)
lpFiLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFrmCmpComponentName.setStatus("mandatory")
_LpFiLtFrmCmpStorageType_Type = StorageType
_LpFiLtFrmCmpStorageType_Object = MibTableColumn
lpFiLtFrmCmpStorageType = _LpFiLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 1, 1, 4),
    _LpFiLtFrmCmpStorageType_Type()
)
lpFiLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFrmCmpStorageType.setStatus("mandatory")
_LpFiLtFrmCmpIndex_Type = NonReplicated
_LpFiLtFrmCmpIndex_Object = MibTableColumn
lpFiLtFrmCmpIndex = _LpFiLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 1, 1, 10),
    _LpFiLtFrmCmpIndex_Type()
)
lpFiLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFrmCmpIndex.setStatus("mandatory")
_LpFiLtFrmCmpTopTable_Object = MibTable
lpFiLtFrmCmpTopTable = _LpFiLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFrmCmpTopTable.setStatus("mandatory")
_LpFiLtFrmCmpTopEntry_Object = MibTableRow
lpFiLtFrmCmpTopEntry = _LpFiLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 10, 1)
)
lpFiLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFrmCmpTopEntry.setStatus("mandatory")


class _LpFiLtFrmCmpTData_Type(AsciiString):
    """Custom type lpFiLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFrmCmpTData_Type.__name__ = "AsciiString"
_LpFiLtFrmCmpTData_Object = MibTableColumn
lpFiLtFrmCmpTData = _LpFiLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 2, 10, 1, 1),
    _LpFiLtFrmCmpTData_Type()
)
lpFiLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFrmCmpTData.setStatus("mandatory")
_LpFiLtFrmCpy_ObjectIdentity = ObjectIdentity
lpFiLtFrmCpy = _LpFiLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3)
)
_LpFiLtFrmCpyRowStatusTable_Object = MibTable
lpFiLtFrmCpyRowStatusTable = _LpFiLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFrmCpyRowStatusTable.setStatus("mandatory")
_LpFiLtFrmCpyRowStatusEntry_Object = MibTableRow
lpFiLtFrmCpyRowStatusEntry = _LpFiLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 1, 1)
)
lpFiLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFrmCpyRowStatusEntry.setStatus("mandatory")
_LpFiLtFrmCpyRowStatus_Type = RowStatus
_LpFiLtFrmCpyRowStatus_Object = MibTableColumn
lpFiLtFrmCpyRowStatus = _LpFiLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 1, 1, 1),
    _LpFiLtFrmCpyRowStatus_Type()
)
lpFiLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFrmCpyRowStatus.setStatus("mandatory")
_LpFiLtFrmCpyComponentName_Type = DisplayString
_LpFiLtFrmCpyComponentName_Object = MibTableColumn
lpFiLtFrmCpyComponentName = _LpFiLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 1, 1, 2),
    _LpFiLtFrmCpyComponentName_Type()
)
lpFiLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFrmCpyComponentName.setStatus("mandatory")
_LpFiLtFrmCpyStorageType_Type = StorageType
_LpFiLtFrmCpyStorageType_Object = MibTableColumn
lpFiLtFrmCpyStorageType = _LpFiLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 1, 1, 4),
    _LpFiLtFrmCpyStorageType_Type()
)
lpFiLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFrmCpyStorageType.setStatus("mandatory")
_LpFiLtFrmCpyIndex_Type = NonReplicated
_LpFiLtFrmCpyIndex_Object = MibTableColumn
lpFiLtFrmCpyIndex = _LpFiLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 1, 1, 10),
    _LpFiLtFrmCpyIndex_Type()
)
lpFiLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFrmCpyIndex.setStatus("mandatory")
_LpFiLtFrmCpyTopTable_Object = MibTable
lpFiLtFrmCpyTopTable = _LpFiLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFrmCpyTopTable.setStatus("mandatory")
_LpFiLtFrmCpyTopEntry_Object = MibTableRow
lpFiLtFrmCpyTopEntry = _LpFiLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 10, 1)
)
lpFiLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFrmCpyTopEntry.setStatus("mandatory")


class _LpFiLtFrmCpyTData_Type(AsciiString):
    """Custom type lpFiLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFrmCpyTData_Type.__name__ = "AsciiString"
_LpFiLtFrmCpyTData_Object = MibTableColumn
lpFiLtFrmCpyTData = _LpFiLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 3, 10, 1, 1),
    _LpFiLtFrmCpyTData_Type()
)
lpFiLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFrmCpyTData.setStatus("mandatory")
_LpFiLtPrtCfg_ObjectIdentity = ObjectIdentity
lpFiLtPrtCfg = _LpFiLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4)
)
_LpFiLtPrtCfgRowStatusTable_Object = MibTable
lpFiLtPrtCfgRowStatusTable = _LpFiLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpFiLtPrtCfgRowStatusTable.setStatus("mandatory")
_LpFiLtPrtCfgRowStatusEntry_Object = MibTableRow
lpFiLtPrtCfgRowStatusEntry = _LpFiLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 1, 1)
)
lpFiLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtPrtCfgRowStatusEntry.setStatus("mandatory")
_LpFiLtPrtCfgRowStatus_Type = RowStatus
_LpFiLtPrtCfgRowStatus_Object = MibTableColumn
lpFiLtPrtCfgRowStatus = _LpFiLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 1, 1, 1),
    _LpFiLtPrtCfgRowStatus_Type()
)
lpFiLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtPrtCfgRowStatus.setStatus("mandatory")
_LpFiLtPrtCfgComponentName_Type = DisplayString
_LpFiLtPrtCfgComponentName_Object = MibTableColumn
lpFiLtPrtCfgComponentName = _LpFiLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 1, 1, 2),
    _LpFiLtPrtCfgComponentName_Type()
)
lpFiLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtPrtCfgComponentName.setStatus("mandatory")
_LpFiLtPrtCfgStorageType_Type = StorageType
_LpFiLtPrtCfgStorageType_Object = MibTableColumn
lpFiLtPrtCfgStorageType = _LpFiLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 1, 1, 4),
    _LpFiLtPrtCfgStorageType_Type()
)
lpFiLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtPrtCfgStorageType.setStatus("mandatory")
_LpFiLtPrtCfgIndex_Type = NonReplicated
_LpFiLtPrtCfgIndex_Object = MibTableColumn
lpFiLtPrtCfgIndex = _LpFiLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 1, 1, 10),
    _LpFiLtPrtCfgIndex_Type()
)
lpFiLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtPrtCfgIndex.setStatus("mandatory")
_LpFiLtPrtCfgTopTable_Object = MibTable
lpFiLtPrtCfgTopTable = _LpFiLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpFiLtPrtCfgTopTable.setStatus("mandatory")
_LpFiLtPrtCfgTopEntry_Object = MibTableRow
lpFiLtPrtCfgTopEntry = _LpFiLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 10, 1)
)
lpFiLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtPrtCfgTopEntry.setStatus("mandatory")


class _LpFiLtPrtCfgTData_Type(AsciiString):
    """Custom type lpFiLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtPrtCfgTData_Type.__name__ = "AsciiString"
_LpFiLtPrtCfgTData_Object = MibTableColumn
lpFiLtPrtCfgTData = _LpFiLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 4, 10, 1, 1),
    _LpFiLtPrtCfgTData_Type()
)
lpFiLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtPrtCfgTData.setStatus("mandatory")
_LpFiLtFb_ObjectIdentity = ObjectIdentity
lpFiLtFb = _LpFiLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5)
)
_LpFiLtFbRowStatusTable_Object = MibTable
lpFiLtFbRowStatusTable = _LpFiLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbRowStatusTable.setStatus("mandatory")
_LpFiLtFbRowStatusEntry_Object = MibTableRow
lpFiLtFbRowStatusEntry = _LpFiLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 1, 1)
)
lpFiLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbRowStatusEntry.setStatus("mandatory")
_LpFiLtFbRowStatus_Type = RowStatus
_LpFiLtFbRowStatus_Object = MibTableColumn
lpFiLtFbRowStatus = _LpFiLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 1, 1, 1),
    _LpFiLtFbRowStatus_Type()
)
lpFiLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbRowStatus.setStatus("mandatory")
_LpFiLtFbComponentName_Type = DisplayString
_LpFiLtFbComponentName_Object = MibTableColumn
lpFiLtFbComponentName = _LpFiLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 1, 1, 2),
    _LpFiLtFbComponentName_Type()
)
lpFiLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbComponentName.setStatus("mandatory")
_LpFiLtFbStorageType_Type = StorageType
_LpFiLtFbStorageType_Object = MibTableColumn
lpFiLtFbStorageType = _LpFiLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 1, 1, 4),
    _LpFiLtFbStorageType_Type()
)
lpFiLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbStorageType.setStatus("mandatory")
_LpFiLtFbIndex_Type = NonReplicated
_LpFiLtFbIndex_Object = MibTableColumn
lpFiLtFbIndex = _LpFiLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 1, 1, 10),
    _LpFiLtFbIndex_Type()
)
lpFiLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbIndex.setStatus("mandatory")
_LpFiLtFbTxInfo_ObjectIdentity = ObjectIdentity
lpFiLtFbTxInfo = _LpFiLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2)
)
_LpFiLtFbTxInfoRowStatusTable_Object = MibTable
lpFiLtFbTxInfoRowStatusTable = _LpFiLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoRowStatusTable.setStatus("mandatory")
_LpFiLtFbTxInfoRowStatusEntry_Object = MibTableRow
lpFiLtFbTxInfoRowStatusEntry = _LpFiLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 1, 1)
)
lpFiLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_LpFiLtFbTxInfoRowStatus_Type = RowStatus
_LpFiLtFbTxInfoRowStatus_Object = MibTableColumn
lpFiLtFbTxInfoRowStatus = _LpFiLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 1, 1, 1),
    _LpFiLtFbTxInfoRowStatus_Type()
)
lpFiLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoRowStatus.setStatus("mandatory")
_LpFiLtFbTxInfoComponentName_Type = DisplayString
_LpFiLtFbTxInfoComponentName_Object = MibTableColumn
lpFiLtFbTxInfoComponentName = _LpFiLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 1, 1, 2),
    _LpFiLtFbTxInfoComponentName_Type()
)
lpFiLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoComponentName.setStatus("mandatory")
_LpFiLtFbTxInfoStorageType_Type = StorageType
_LpFiLtFbTxInfoStorageType_Object = MibTableColumn
lpFiLtFbTxInfoStorageType = _LpFiLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 1, 1, 4),
    _LpFiLtFbTxInfoStorageType_Type()
)
lpFiLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoStorageType.setStatus("mandatory")
_LpFiLtFbTxInfoIndex_Type = NonReplicated
_LpFiLtFbTxInfoIndex_Object = MibTableColumn
lpFiLtFbTxInfoIndex = _LpFiLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 1, 1, 10),
    _LpFiLtFbTxInfoIndex_Type()
)
lpFiLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoIndex.setStatus("mandatory")
_LpFiLtFbTxInfoTopTable_Object = MibTable
lpFiLtFbTxInfoTopTable = _LpFiLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoTopTable.setStatus("mandatory")
_LpFiLtFbTxInfoTopEntry_Object = MibTableRow
lpFiLtFbTxInfoTopEntry = _LpFiLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 10, 1)
)
lpFiLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoTopEntry.setStatus("mandatory")


class _LpFiLtFbTxInfoTData_Type(AsciiString):
    """Custom type lpFiLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbTxInfoTData_Type.__name__ = "AsciiString"
_LpFiLtFbTxInfoTData_Object = MibTableColumn
lpFiLtFbTxInfoTData = _LpFiLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 2, 10, 1, 1),
    _LpFiLtFbTxInfoTData_Type()
)
lpFiLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbTxInfoTData.setStatus("mandatory")
_LpFiLtFbFddiMac_ObjectIdentity = ObjectIdentity
lpFiLtFbFddiMac = _LpFiLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3)
)
_LpFiLtFbFddiMacRowStatusTable_Object = MibTable
lpFiLtFbFddiMacRowStatusTable = _LpFiLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacRowStatusTable.setStatus("mandatory")
_LpFiLtFbFddiMacRowStatusEntry_Object = MibTableRow
lpFiLtFbFddiMacRowStatusEntry = _LpFiLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 1, 1)
)
lpFiLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_LpFiLtFbFddiMacRowStatus_Type = RowStatus
_LpFiLtFbFddiMacRowStatus_Object = MibTableColumn
lpFiLtFbFddiMacRowStatus = _LpFiLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 1, 1, 1),
    _LpFiLtFbFddiMacRowStatus_Type()
)
lpFiLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacRowStatus.setStatus("mandatory")
_LpFiLtFbFddiMacComponentName_Type = DisplayString
_LpFiLtFbFddiMacComponentName_Object = MibTableColumn
lpFiLtFbFddiMacComponentName = _LpFiLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 1, 1, 2),
    _LpFiLtFbFddiMacComponentName_Type()
)
lpFiLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacComponentName.setStatus("mandatory")
_LpFiLtFbFddiMacStorageType_Type = StorageType
_LpFiLtFbFddiMacStorageType_Object = MibTableColumn
lpFiLtFbFddiMacStorageType = _LpFiLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 1, 1, 4),
    _LpFiLtFbFddiMacStorageType_Type()
)
lpFiLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacStorageType.setStatus("mandatory")
_LpFiLtFbFddiMacIndex_Type = NonReplicated
_LpFiLtFbFddiMacIndex_Object = MibTableColumn
lpFiLtFbFddiMacIndex = _LpFiLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 1, 1, 10),
    _LpFiLtFbFddiMacIndex_Type()
)
lpFiLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacIndex.setStatus("mandatory")
_LpFiLtFbFddiMacTopTable_Object = MibTable
lpFiLtFbFddiMacTopTable = _LpFiLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacTopTable.setStatus("mandatory")
_LpFiLtFbFddiMacTopEntry_Object = MibTableRow
lpFiLtFbFddiMacTopEntry = _LpFiLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 10, 1)
)
lpFiLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacTopEntry.setStatus("mandatory")


class _LpFiLtFbFddiMacTData_Type(AsciiString):
    """Custom type lpFiLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbFddiMacTData_Type.__name__ = "AsciiString"
_LpFiLtFbFddiMacTData_Object = MibTableColumn
lpFiLtFbFddiMacTData = _LpFiLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 3, 10, 1, 1),
    _LpFiLtFbFddiMacTData_Type()
)
lpFiLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbFddiMacTData.setStatus("mandatory")
_LpFiLtFbMacEnet_ObjectIdentity = ObjectIdentity
lpFiLtFbMacEnet = _LpFiLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4)
)
_LpFiLtFbMacEnetRowStatusTable_Object = MibTable
lpFiLtFbMacEnetRowStatusTable = _LpFiLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetRowStatusTable.setStatus("mandatory")
_LpFiLtFbMacEnetRowStatusEntry_Object = MibTableRow
lpFiLtFbMacEnetRowStatusEntry = _LpFiLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 1, 1)
)
lpFiLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_LpFiLtFbMacEnetRowStatus_Type = RowStatus
_LpFiLtFbMacEnetRowStatus_Object = MibTableColumn
lpFiLtFbMacEnetRowStatus = _LpFiLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 1, 1, 1),
    _LpFiLtFbMacEnetRowStatus_Type()
)
lpFiLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetRowStatus.setStatus("mandatory")
_LpFiLtFbMacEnetComponentName_Type = DisplayString
_LpFiLtFbMacEnetComponentName_Object = MibTableColumn
lpFiLtFbMacEnetComponentName = _LpFiLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 1, 1, 2),
    _LpFiLtFbMacEnetComponentName_Type()
)
lpFiLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetComponentName.setStatus("mandatory")
_LpFiLtFbMacEnetStorageType_Type = StorageType
_LpFiLtFbMacEnetStorageType_Object = MibTableColumn
lpFiLtFbMacEnetStorageType = _LpFiLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 1, 1, 4),
    _LpFiLtFbMacEnetStorageType_Type()
)
lpFiLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetStorageType.setStatus("mandatory")
_LpFiLtFbMacEnetIndex_Type = NonReplicated
_LpFiLtFbMacEnetIndex_Object = MibTableColumn
lpFiLtFbMacEnetIndex = _LpFiLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 1, 1, 10),
    _LpFiLtFbMacEnetIndex_Type()
)
lpFiLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetIndex.setStatus("mandatory")
_LpFiLtFbMacEnetTopTable_Object = MibTable
lpFiLtFbMacEnetTopTable = _LpFiLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetTopTable.setStatus("mandatory")
_LpFiLtFbMacEnetTopEntry_Object = MibTableRow
lpFiLtFbMacEnetTopEntry = _LpFiLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 10, 1)
)
lpFiLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetTopEntry.setStatus("mandatory")


class _LpFiLtFbMacEnetTData_Type(AsciiString):
    """Custom type lpFiLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbMacEnetTData_Type.__name__ = "AsciiString"
_LpFiLtFbMacEnetTData_Object = MibTableColumn
lpFiLtFbMacEnetTData = _LpFiLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 4, 10, 1, 1),
    _LpFiLtFbMacEnetTData_Type()
)
lpFiLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbMacEnetTData.setStatus("mandatory")
_LpFiLtFbMacTr_ObjectIdentity = ObjectIdentity
lpFiLtFbMacTr = _LpFiLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5)
)
_LpFiLtFbMacTrRowStatusTable_Object = MibTable
lpFiLtFbMacTrRowStatusTable = _LpFiLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbMacTrRowStatusTable.setStatus("mandatory")
_LpFiLtFbMacTrRowStatusEntry_Object = MibTableRow
lpFiLtFbMacTrRowStatusEntry = _LpFiLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 1, 1)
)
lpFiLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbMacTrRowStatusEntry.setStatus("mandatory")
_LpFiLtFbMacTrRowStatus_Type = RowStatus
_LpFiLtFbMacTrRowStatus_Object = MibTableColumn
lpFiLtFbMacTrRowStatus = _LpFiLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 1, 1, 1),
    _LpFiLtFbMacTrRowStatus_Type()
)
lpFiLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbMacTrRowStatus.setStatus("mandatory")
_LpFiLtFbMacTrComponentName_Type = DisplayString
_LpFiLtFbMacTrComponentName_Object = MibTableColumn
lpFiLtFbMacTrComponentName = _LpFiLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 1, 1, 2),
    _LpFiLtFbMacTrComponentName_Type()
)
lpFiLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbMacTrComponentName.setStatus("mandatory")
_LpFiLtFbMacTrStorageType_Type = StorageType
_LpFiLtFbMacTrStorageType_Object = MibTableColumn
lpFiLtFbMacTrStorageType = _LpFiLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 1, 1, 4),
    _LpFiLtFbMacTrStorageType_Type()
)
lpFiLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbMacTrStorageType.setStatus("mandatory")
_LpFiLtFbMacTrIndex_Type = NonReplicated
_LpFiLtFbMacTrIndex_Object = MibTableColumn
lpFiLtFbMacTrIndex = _LpFiLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 1, 1, 10),
    _LpFiLtFbMacTrIndex_Type()
)
lpFiLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbMacTrIndex.setStatus("mandatory")
_LpFiLtFbMacTrTopTable_Object = MibTable
lpFiLtFbMacTrTopTable = _LpFiLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbMacTrTopTable.setStatus("mandatory")
_LpFiLtFbMacTrTopEntry_Object = MibTableRow
lpFiLtFbMacTrTopEntry = _LpFiLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 10, 1)
)
lpFiLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbMacTrTopEntry.setStatus("mandatory")


class _LpFiLtFbMacTrTData_Type(AsciiString):
    """Custom type lpFiLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbMacTrTData_Type.__name__ = "AsciiString"
_LpFiLtFbMacTrTData_Object = MibTableColumn
lpFiLtFbMacTrTData = _LpFiLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 5, 10, 1, 1),
    _LpFiLtFbMacTrTData_Type()
)
lpFiLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbMacTrTData.setStatus("mandatory")
_LpFiLtFbData_ObjectIdentity = ObjectIdentity
lpFiLtFbData = _LpFiLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6)
)
_LpFiLtFbDataRowStatusTable_Object = MibTable
lpFiLtFbDataRowStatusTable = _LpFiLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbDataRowStatusTable.setStatus("mandatory")
_LpFiLtFbDataRowStatusEntry_Object = MibTableRow
lpFiLtFbDataRowStatusEntry = _LpFiLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 1, 1)
)
lpFiLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbDataRowStatusEntry.setStatus("mandatory")
_LpFiLtFbDataRowStatus_Type = RowStatus
_LpFiLtFbDataRowStatus_Object = MibTableColumn
lpFiLtFbDataRowStatus = _LpFiLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 1, 1, 1),
    _LpFiLtFbDataRowStatus_Type()
)
lpFiLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbDataRowStatus.setStatus("mandatory")
_LpFiLtFbDataComponentName_Type = DisplayString
_LpFiLtFbDataComponentName_Object = MibTableColumn
lpFiLtFbDataComponentName = _LpFiLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 1, 1, 2),
    _LpFiLtFbDataComponentName_Type()
)
lpFiLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbDataComponentName.setStatus("mandatory")
_LpFiLtFbDataStorageType_Type = StorageType
_LpFiLtFbDataStorageType_Object = MibTableColumn
lpFiLtFbDataStorageType = _LpFiLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 1, 1, 4),
    _LpFiLtFbDataStorageType_Type()
)
lpFiLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbDataStorageType.setStatus("mandatory")
_LpFiLtFbDataIndex_Type = NonReplicated
_LpFiLtFbDataIndex_Object = MibTableColumn
lpFiLtFbDataIndex = _LpFiLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 1, 1, 10),
    _LpFiLtFbDataIndex_Type()
)
lpFiLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbDataIndex.setStatus("mandatory")
_LpFiLtFbDataTopTable_Object = MibTable
lpFiLtFbDataTopTable = _LpFiLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbDataTopTable.setStatus("mandatory")
_LpFiLtFbDataTopEntry_Object = MibTableRow
lpFiLtFbDataTopEntry = _LpFiLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 10, 1)
)
lpFiLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbDataTopEntry.setStatus("mandatory")


class _LpFiLtFbDataTData_Type(AsciiString):
    """Custom type lpFiLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbDataTData_Type.__name__ = "AsciiString"
_LpFiLtFbDataTData_Object = MibTableColumn
lpFiLtFbDataTData = _LpFiLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 6, 10, 1, 1),
    _LpFiLtFbDataTData_Type()
)
lpFiLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbDataTData.setStatus("mandatory")
_LpFiLtFbIpH_ObjectIdentity = ObjectIdentity
lpFiLtFbIpH = _LpFiLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7)
)
_LpFiLtFbIpHRowStatusTable_Object = MibTable
lpFiLtFbIpHRowStatusTable = _LpFiLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbIpHRowStatusTable.setStatus("mandatory")
_LpFiLtFbIpHRowStatusEntry_Object = MibTableRow
lpFiLtFbIpHRowStatusEntry = _LpFiLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 1, 1)
)
lpFiLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbIpHRowStatusEntry.setStatus("mandatory")
_LpFiLtFbIpHRowStatus_Type = RowStatus
_LpFiLtFbIpHRowStatus_Object = MibTableColumn
lpFiLtFbIpHRowStatus = _LpFiLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 1, 1, 1),
    _LpFiLtFbIpHRowStatus_Type()
)
lpFiLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbIpHRowStatus.setStatus("mandatory")
_LpFiLtFbIpHComponentName_Type = DisplayString
_LpFiLtFbIpHComponentName_Object = MibTableColumn
lpFiLtFbIpHComponentName = _LpFiLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 1, 1, 2),
    _LpFiLtFbIpHComponentName_Type()
)
lpFiLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbIpHComponentName.setStatus("mandatory")
_LpFiLtFbIpHStorageType_Type = StorageType
_LpFiLtFbIpHStorageType_Object = MibTableColumn
lpFiLtFbIpHStorageType = _LpFiLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 1, 1, 4),
    _LpFiLtFbIpHStorageType_Type()
)
lpFiLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbIpHStorageType.setStatus("mandatory")
_LpFiLtFbIpHIndex_Type = NonReplicated
_LpFiLtFbIpHIndex_Object = MibTableColumn
lpFiLtFbIpHIndex = _LpFiLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 1, 1, 10),
    _LpFiLtFbIpHIndex_Type()
)
lpFiLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbIpHIndex.setStatus("mandatory")
_LpFiLtFbIpHTopTable_Object = MibTable
lpFiLtFbIpHTopTable = _LpFiLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbIpHTopTable.setStatus("mandatory")
_LpFiLtFbIpHTopEntry_Object = MibTableRow
lpFiLtFbIpHTopEntry = _LpFiLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 10, 1)
)
lpFiLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbIpHTopEntry.setStatus("mandatory")


class _LpFiLtFbIpHTData_Type(AsciiString):
    """Custom type lpFiLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbIpHTData_Type.__name__ = "AsciiString"
_LpFiLtFbIpHTData_Object = MibTableColumn
lpFiLtFbIpHTData = _LpFiLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 7, 10, 1, 1),
    _LpFiLtFbIpHTData_Type()
)
lpFiLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbIpHTData.setStatus("mandatory")
_LpFiLtFbLlch_ObjectIdentity = ObjectIdentity
lpFiLtFbLlch = _LpFiLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8)
)
_LpFiLtFbLlchRowStatusTable_Object = MibTable
lpFiLtFbLlchRowStatusTable = _LpFiLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbLlchRowStatusTable.setStatus("mandatory")
_LpFiLtFbLlchRowStatusEntry_Object = MibTableRow
lpFiLtFbLlchRowStatusEntry = _LpFiLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 1, 1)
)
lpFiLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbLlchRowStatusEntry.setStatus("mandatory")
_LpFiLtFbLlchRowStatus_Type = RowStatus
_LpFiLtFbLlchRowStatus_Object = MibTableColumn
lpFiLtFbLlchRowStatus = _LpFiLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 1, 1, 1),
    _LpFiLtFbLlchRowStatus_Type()
)
lpFiLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbLlchRowStatus.setStatus("mandatory")
_LpFiLtFbLlchComponentName_Type = DisplayString
_LpFiLtFbLlchComponentName_Object = MibTableColumn
lpFiLtFbLlchComponentName = _LpFiLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 1, 1, 2),
    _LpFiLtFbLlchComponentName_Type()
)
lpFiLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbLlchComponentName.setStatus("mandatory")
_LpFiLtFbLlchStorageType_Type = StorageType
_LpFiLtFbLlchStorageType_Object = MibTableColumn
lpFiLtFbLlchStorageType = _LpFiLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 1, 1, 4),
    _LpFiLtFbLlchStorageType_Type()
)
lpFiLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbLlchStorageType.setStatus("mandatory")
_LpFiLtFbLlchIndex_Type = NonReplicated
_LpFiLtFbLlchIndex_Object = MibTableColumn
lpFiLtFbLlchIndex = _LpFiLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 1, 1, 10),
    _LpFiLtFbLlchIndex_Type()
)
lpFiLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbLlchIndex.setStatus("mandatory")
_LpFiLtFbLlchTopTable_Object = MibTable
lpFiLtFbLlchTopTable = _LpFiLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbLlchTopTable.setStatus("mandatory")
_LpFiLtFbLlchTopEntry_Object = MibTableRow
lpFiLtFbLlchTopEntry = _LpFiLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 10, 1)
)
lpFiLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbLlchTopEntry.setStatus("mandatory")


class _LpFiLtFbLlchTData_Type(AsciiString):
    """Custom type lpFiLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbLlchTData_Type.__name__ = "AsciiString"
_LpFiLtFbLlchTData_Object = MibTableColumn
lpFiLtFbLlchTData = _LpFiLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 8, 10, 1, 1),
    _LpFiLtFbLlchTData_Type()
)
lpFiLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbLlchTData.setStatus("mandatory")
_LpFiLtFbAppleH_ObjectIdentity = ObjectIdentity
lpFiLtFbAppleH = _LpFiLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9)
)
_LpFiLtFbAppleHRowStatusTable_Object = MibTable
lpFiLtFbAppleHRowStatusTable = _LpFiLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbAppleHRowStatusTable.setStatus("mandatory")
_LpFiLtFbAppleHRowStatusEntry_Object = MibTableRow
lpFiLtFbAppleHRowStatusEntry = _LpFiLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 1, 1)
)
lpFiLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbAppleHRowStatusEntry.setStatus("mandatory")
_LpFiLtFbAppleHRowStatus_Type = RowStatus
_LpFiLtFbAppleHRowStatus_Object = MibTableColumn
lpFiLtFbAppleHRowStatus = _LpFiLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 1, 1, 1),
    _LpFiLtFbAppleHRowStatus_Type()
)
lpFiLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbAppleHRowStatus.setStatus("mandatory")
_LpFiLtFbAppleHComponentName_Type = DisplayString
_LpFiLtFbAppleHComponentName_Object = MibTableColumn
lpFiLtFbAppleHComponentName = _LpFiLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 1, 1, 2),
    _LpFiLtFbAppleHComponentName_Type()
)
lpFiLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbAppleHComponentName.setStatus("mandatory")
_LpFiLtFbAppleHStorageType_Type = StorageType
_LpFiLtFbAppleHStorageType_Object = MibTableColumn
lpFiLtFbAppleHStorageType = _LpFiLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 1, 1, 4),
    _LpFiLtFbAppleHStorageType_Type()
)
lpFiLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbAppleHStorageType.setStatus("mandatory")
_LpFiLtFbAppleHIndex_Type = NonReplicated
_LpFiLtFbAppleHIndex_Object = MibTableColumn
lpFiLtFbAppleHIndex = _LpFiLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 1, 1, 10),
    _LpFiLtFbAppleHIndex_Type()
)
lpFiLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbAppleHIndex.setStatus("mandatory")
_LpFiLtFbAppleHTopTable_Object = MibTable
lpFiLtFbAppleHTopTable = _LpFiLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbAppleHTopTable.setStatus("mandatory")
_LpFiLtFbAppleHTopEntry_Object = MibTableRow
lpFiLtFbAppleHTopEntry = _LpFiLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 10, 1)
)
lpFiLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbAppleHTopEntry.setStatus("mandatory")


class _LpFiLtFbAppleHTData_Type(AsciiString):
    """Custom type lpFiLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbAppleHTData_Type.__name__ = "AsciiString"
_LpFiLtFbAppleHTData_Object = MibTableColumn
lpFiLtFbAppleHTData = _LpFiLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 9, 10, 1, 1),
    _LpFiLtFbAppleHTData_Type()
)
lpFiLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbAppleHTData.setStatus("mandatory")
_LpFiLtFbIpxH_ObjectIdentity = ObjectIdentity
lpFiLtFbIpxH = _LpFiLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10)
)
_LpFiLtFbIpxHRowStatusTable_Object = MibTable
lpFiLtFbIpxHRowStatusTable = _LpFiLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    lpFiLtFbIpxHRowStatusTable.setStatus("mandatory")
_LpFiLtFbIpxHRowStatusEntry_Object = MibTableRow
lpFiLtFbIpxHRowStatusEntry = _LpFiLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 1, 1)
)
lpFiLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbIpxHRowStatusEntry.setStatus("mandatory")
_LpFiLtFbIpxHRowStatus_Type = RowStatus
_LpFiLtFbIpxHRowStatus_Object = MibTableColumn
lpFiLtFbIpxHRowStatus = _LpFiLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 1, 1, 1),
    _LpFiLtFbIpxHRowStatus_Type()
)
lpFiLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbIpxHRowStatus.setStatus("mandatory")
_LpFiLtFbIpxHComponentName_Type = DisplayString
_LpFiLtFbIpxHComponentName_Object = MibTableColumn
lpFiLtFbIpxHComponentName = _LpFiLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 1, 1, 2),
    _LpFiLtFbIpxHComponentName_Type()
)
lpFiLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbIpxHComponentName.setStatus("mandatory")
_LpFiLtFbIpxHStorageType_Type = StorageType
_LpFiLtFbIpxHStorageType_Object = MibTableColumn
lpFiLtFbIpxHStorageType = _LpFiLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 1, 1, 4),
    _LpFiLtFbIpxHStorageType_Type()
)
lpFiLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtFbIpxHStorageType.setStatus("mandatory")
_LpFiLtFbIpxHIndex_Type = NonReplicated
_LpFiLtFbIpxHIndex_Object = MibTableColumn
lpFiLtFbIpxHIndex = _LpFiLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 1, 1, 10),
    _LpFiLtFbIpxHIndex_Type()
)
lpFiLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtFbIpxHIndex.setStatus("mandatory")
_LpFiLtFbIpxHTopTable_Object = MibTable
lpFiLtFbIpxHTopTable = _LpFiLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    lpFiLtFbIpxHTopTable.setStatus("mandatory")
_LpFiLtFbIpxHTopEntry_Object = MibTableRow
lpFiLtFbIpxHTopEntry = _LpFiLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 10, 1)
)
lpFiLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbIpxHTopEntry.setStatus("mandatory")


class _LpFiLtFbIpxHTData_Type(AsciiString):
    """Custom type lpFiLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbIpxHTData_Type.__name__ = "AsciiString"
_LpFiLtFbIpxHTData_Object = MibTableColumn
lpFiLtFbIpxHTData = _LpFiLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 10, 10, 1, 1),
    _LpFiLtFbIpxHTData_Type()
)
lpFiLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbIpxHTData.setStatus("mandatory")
_LpFiLtFbTopTable_Object = MibTable
lpFiLtFbTopTable = _LpFiLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 20)
)
if mibBuilder.loadTexts:
    lpFiLtFbTopTable.setStatus("mandatory")
_LpFiLtFbTopEntry_Object = MibTableRow
lpFiLtFbTopEntry = _LpFiLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 20, 1)
)
lpFiLtFbTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtFbTopEntry.setStatus("mandatory")


class _LpFiLtFbTData_Type(AsciiString):
    """Custom type lpFiLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtFbTData_Type.__name__ = "AsciiString"
_LpFiLtFbTData_Object = MibTableColumn
lpFiLtFbTData = _LpFiLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 5, 20, 1, 1),
    _LpFiLtFbTData_Type()
)
lpFiLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtFbTData.setStatus("mandatory")
_LpFiLtCntl_ObjectIdentity = ObjectIdentity
lpFiLtCntl = _LpFiLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6)
)
_LpFiLtCntlRowStatusTable_Object = MibTable
lpFiLtCntlRowStatusTable = _LpFiLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    lpFiLtCntlRowStatusTable.setStatus("mandatory")
_LpFiLtCntlRowStatusEntry_Object = MibTableRow
lpFiLtCntlRowStatusEntry = _LpFiLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 1, 1)
)
lpFiLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtCntlRowStatusEntry.setStatus("mandatory")
_LpFiLtCntlRowStatus_Type = RowStatus
_LpFiLtCntlRowStatus_Object = MibTableColumn
lpFiLtCntlRowStatus = _LpFiLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 1, 1, 1),
    _LpFiLtCntlRowStatus_Type()
)
lpFiLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtCntlRowStatus.setStatus("mandatory")
_LpFiLtCntlComponentName_Type = DisplayString
_LpFiLtCntlComponentName_Object = MibTableColumn
lpFiLtCntlComponentName = _LpFiLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 1, 1, 2),
    _LpFiLtCntlComponentName_Type()
)
lpFiLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtCntlComponentName.setStatus("mandatory")
_LpFiLtCntlStorageType_Type = StorageType
_LpFiLtCntlStorageType_Object = MibTableColumn
lpFiLtCntlStorageType = _LpFiLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 1, 1, 4),
    _LpFiLtCntlStorageType_Type()
)
lpFiLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLtCntlStorageType.setStatus("mandatory")
_LpFiLtCntlIndex_Type = NonReplicated
_LpFiLtCntlIndex_Object = MibTableColumn
lpFiLtCntlIndex = _LpFiLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 1, 1, 10),
    _LpFiLtCntlIndex_Type()
)
lpFiLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiLtCntlIndex.setStatus("mandatory")
_LpFiLtCntlTopTable_Object = MibTable
lpFiLtCntlTopTable = _LpFiLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 10)
)
if mibBuilder.loadTexts:
    lpFiLtCntlTopTable.setStatus("mandatory")
_LpFiLtCntlTopEntry_Object = MibTableRow
lpFiLtCntlTopEntry = _LpFiLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 10, 1)
)
lpFiLtCntlTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtCntlTopEntry.setStatus("mandatory")


class _LpFiLtCntlTData_Type(AsciiString):
    """Custom type lpFiLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtCntlTData_Type.__name__ = "AsciiString"
_LpFiLtCntlTData_Object = MibTableColumn
lpFiLtCntlTData = _LpFiLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 6, 10, 1, 1),
    _LpFiLtCntlTData_Type()
)
lpFiLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtCntlTData.setStatus("mandatory")
_LpFiLtTopTable_Object = MibTable
lpFiLtTopTable = _LpFiLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 20)
)
if mibBuilder.loadTexts:
    lpFiLtTopTable.setStatus("mandatory")
_LpFiLtTopEntry_Object = MibTableRow
lpFiLtTopEntry = _LpFiLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 20, 1)
)
lpFiLtTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiLtIndex"),
)
if mibBuilder.loadTexts:
    lpFiLtTopEntry.setStatus("mandatory")


class _LpFiLtTData_Type(AsciiString):
    """Custom type lpFiLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpFiLtTData_Type.__name__ = "AsciiString"
_LpFiLtTData_Object = MibTableColumn
lpFiLtTData = _LpFiLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 2, 20, 1, 1),
    _LpFiLtTData_Type()
)
lpFiLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiLtTData.setStatus("mandatory")
_LpFiPhy_ObjectIdentity = ObjectIdentity
lpFiPhy = _LpFiPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3)
)
_LpFiPhyRowStatusTable_Object = MibTable
lpFiPhyRowStatusTable = _LpFiPhyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lpFiPhyRowStatusTable.setStatus("mandatory")
_LpFiPhyRowStatusEntry_Object = MibTableRow
lpFiPhyRowStatusEntry = _LpFiPhyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 1, 1)
)
lpFiPhyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiPhyFddiPhyTypeIndex"),
)
if mibBuilder.loadTexts:
    lpFiPhyRowStatusEntry.setStatus("mandatory")
_LpFiPhyRowStatus_Type = RowStatus
_LpFiPhyRowStatus_Object = MibTableColumn
lpFiPhyRowStatus = _LpFiPhyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 1, 1, 1),
    _LpFiPhyRowStatus_Type()
)
lpFiPhyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiPhyRowStatus.setStatus("mandatory")
_LpFiPhyComponentName_Type = DisplayString
_LpFiPhyComponentName_Object = MibTableColumn
lpFiPhyComponentName = _LpFiPhyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 1, 1, 2),
    _LpFiPhyComponentName_Type()
)
lpFiPhyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyComponentName.setStatus("mandatory")
_LpFiPhyStorageType_Type = StorageType
_LpFiPhyStorageType_Object = MibTableColumn
lpFiPhyStorageType = _LpFiPhyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 1, 1, 4),
    _LpFiPhyStorageType_Type()
)
lpFiPhyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyStorageType.setStatus("mandatory")


class _LpFiPhyFddiPhyTypeIndex_Type(Integer32):
    """Custom type lpFiPhyFddiPhyTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1))
    )


_LpFiPhyFddiPhyTypeIndex_Type.__name__ = "Integer32"
_LpFiPhyFddiPhyTypeIndex_Object = MibTableColumn
lpFiPhyFddiPhyTypeIndex = _LpFiPhyFddiPhyTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 1, 1, 10),
    _LpFiPhyFddiPhyTypeIndex_Type()
)
lpFiPhyFddiPhyTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiPhyFddiPhyTypeIndex.setStatus("mandatory")
_LpFiPhyProvTable_Object = MibTable
lpFiPhyProvTable = _LpFiPhyProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 10)
)
if mibBuilder.loadTexts:
    lpFiPhyProvTable.setStatus("mandatory")
_LpFiPhyProvEntry_Object = MibTableRow
lpFiPhyProvEntry = _LpFiPhyProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 10, 1)
)
lpFiPhyProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiPhyFddiPhyTypeIndex"),
)
if mibBuilder.loadTexts:
    lpFiPhyProvEntry.setStatus("mandatory")


class _LpFiPhyLerCutoff_Type(Unsigned32):
    """Custom type lpFiPhyLerCutoff based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_LpFiPhyLerCutoff_Type.__name__ = "Unsigned32"
_LpFiPhyLerCutoff_Object = MibTableColumn
lpFiPhyLerCutoff = _LpFiPhyLerCutoff_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 10, 1, 1),
    _LpFiPhyLerCutoff_Type()
)
lpFiPhyLerCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiPhyLerCutoff.setStatus("mandatory")


class _LpFiPhyLerAlarm_Type(Unsigned32):
    """Custom type lpFiPhyLerAlarm based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_LpFiPhyLerAlarm_Type.__name__ = "Unsigned32"
_LpFiPhyLerAlarm_Object = MibTableColumn
lpFiPhyLerAlarm = _LpFiPhyLerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 10, 1, 2),
    _LpFiPhyLerAlarm_Type()
)
lpFiPhyLerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiPhyLerAlarm.setStatus("mandatory")


class _LpFiPhyLinkErrorMonitor_Type(Integer32):
    """Custom type lpFiPhyLinkErrorMonitor based on Integer32"""
    defaultValue = 1

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


_LpFiPhyLinkErrorMonitor_Type.__name__ = "Integer32"
_LpFiPhyLinkErrorMonitor_Object = MibTableColumn
lpFiPhyLinkErrorMonitor = _LpFiPhyLinkErrorMonitor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 10, 1, 3),
    _LpFiPhyLinkErrorMonitor_Type()
)
lpFiPhyLinkErrorMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiPhyLinkErrorMonitor.setStatus("mandatory")
_LpFiPhyOperTable_Object = MibTable
lpFiPhyOperTable = _LpFiPhyOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11)
)
if mibBuilder.loadTexts:
    lpFiPhyOperTable.setStatus("mandatory")
_LpFiPhyOperEntry_Object = MibTableRow
lpFiPhyOperEntry = _LpFiPhyOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1)
)
lpFiPhyOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiPhyFddiPhyTypeIndex"),
)
if mibBuilder.loadTexts:
    lpFiPhyOperEntry.setStatus("mandatory")


class _LpFiPhyNeighborType_Type(Integer32):
    """Custom type lpFiPhyNeighborType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("none", 5),
          ("s", 3))
    )


_LpFiPhyNeighborType_Type.__name__ = "Integer32"
_LpFiPhyNeighborType_Object = MibTableColumn
lpFiPhyNeighborType = _LpFiPhyNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 4),
    _LpFiPhyNeighborType_Type()
)
lpFiPhyNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyNeighborType.setStatus("mandatory")
_LpFiPhyLctFailCounts_Type = Counter32
_LpFiPhyLctFailCounts_Object = MibTableColumn
lpFiPhyLctFailCounts = _LpFiPhyLctFailCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 13),
    _LpFiPhyLctFailCounts_Type()
)
lpFiPhyLctFailCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyLctFailCounts.setStatus("mandatory")


class _LpFiPhyLerEstimate_Type(Unsigned32):
    """Custom type lpFiPhyLerEstimate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_LpFiPhyLerEstimate_Type.__name__ = "Unsigned32"
_LpFiPhyLerEstimate_Object = MibTableColumn
lpFiPhyLerEstimate = _LpFiPhyLerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 14),
    _LpFiPhyLerEstimate_Type()
)
lpFiPhyLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyLerEstimate.setStatus("mandatory")
_LpFiPhyLemRejectCounts_Type = Counter32
_LpFiPhyLemRejectCounts_Object = MibTableColumn
lpFiPhyLemRejectCounts = _LpFiPhyLemRejectCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 15),
    _LpFiPhyLemRejectCounts_Type()
)
lpFiPhyLemRejectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyLemRejectCounts.setStatus("mandatory")
_LpFiPhyLemCounts_Type = Counter32
_LpFiPhyLemCounts_Object = MibTableColumn
lpFiPhyLemCounts = _LpFiPhyLemCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 16),
    _LpFiPhyLemCounts_Type()
)
lpFiPhyLemCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyLemCounts.setStatus("mandatory")


class _LpFiPhyPcmState_Type(Integer32):
    """Custom type lpFiPhyPcmState based on Integer32"""
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
        *(("active", 9),
          ("break", 2),
          ("connect", 4),
          ("join", 7),
          ("maint", 10),
          ("next", 5),
          ("off", 1),
          ("signal", 6),
          ("trace", 3),
          ("verify", 8))
    )


_LpFiPhyPcmState_Type.__name__ = "Integer32"
_LpFiPhyPcmState_Object = MibTableColumn
lpFiPhyPcmState = _LpFiPhyPcmState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 18),
    _LpFiPhyPcmState_Type()
)
lpFiPhyPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyPcmState.setStatus("mandatory")


class _LpFiPhyLerFlag_Type(Integer32):
    """Custom type lpFiPhyLerFlag based on Integer32"""
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


_LpFiPhyLerFlag_Type.__name__ = "Integer32"
_LpFiPhyLerFlag_Object = MibTableColumn
lpFiPhyLerFlag = _LpFiPhyLerFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 20),
    _LpFiPhyLerFlag_Type()
)
lpFiPhyLerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhyLerFlag.setStatus("mandatory")


class _LpFiPhySignalState_Type(Integer32):
    """Custom type lpFiPhySignalState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("accept", 3),
          ("escape", 0),
          ("lctLengthH", 5),
          ("lctLengthL", 4),
          ("lctResult", 7),
          ("macAvail", 6),
          ("macLoop", 8),
          ("macOnPhy", 9),
          ("phyTypeH", 2),
          ("phyTypeL", 1),
          ("signalingDone", 10))
    )


_LpFiPhySignalState_Type.__name__ = "Integer32"
_LpFiPhySignalState_Object = MibTableColumn
lpFiPhySignalState = _LpFiPhySignalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 23),
    _LpFiPhySignalState_Type()
)
lpFiPhySignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhySignalState.setStatus("mandatory")


class _LpFiPhySignalBitsRcvd_Type(OctetString):
    """Custom type lpFiPhySignalBitsRcvd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpFiPhySignalBitsRcvd_Type.__name__ = "OctetString"
_LpFiPhySignalBitsRcvd_Object = MibTableColumn
lpFiPhySignalBitsRcvd = _LpFiPhySignalBitsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 24),
    _LpFiPhySignalBitsRcvd_Type()
)
lpFiPhySignalBitsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhySignalBitsRcvd.setStatus("mandatory")


class _LpFiPhySignalBitsTxmt_Type(OctetString):
    """Custom type lpFiPhySignalBitsTxmt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpFiPhySignalBitsTxmt_Type.__name__ = "OctetString"
_LpFiPhySignalBitsTxmt_Object = MibTableColumn
lpFiPhySignalBitsTxmt = _LpFiPhySignalBitsTxmt_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 3, 11, 1, 25),
    _LpFiPhySignalBitsTxmt_Type()
)
lpFiPhySignalBitsTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiPhySignalBitsTxmt.setStatus("mandatory")
_LpFiTest_ObjectIdentity = ObjectIdentity
lpFiTest = _LpFiTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5)
)
_LpFiTestRowStatusTable_Object = MibTable
lpFiTestRowStatusTable = _LpFiTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 1)
)
if mibBuilder.loadTexts:
    lpFiTestRowStatusTable.setStatus("mandatory")
_LpFiTestRowStatusEntry_Object = MibTableRow
lpFiTestRowStatusEntry = _LpFiTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 1, 1)
)
lpFiTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiTestIndex"),
)
if mibBuilder.loadTexts:
    lpFiTestRowStatusEntry.setStatus("mandatory")
_LpFiTestRowStatus_Type = RowStatus
_LpFiTestRowStatus_Object = MibTableColumn
lpFiTestRowStatus = _LpFiTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 1, 1, 1),
    _LpFiTestRowStatus_Type()
)
lpFiTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestRowStatus.setStatus("mandatory")
_LpFiTestComponentName_Type = DisplayString
_LpFiTestComponentName_Object = MibTableColumn
lpFiTestComponentName = _LpFiTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 1, 1, 2),
    _LpFiTestComponentName_Type()
)
lpFiTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestComponentName.setStatus("mandatory")
_LpFiTestStorageType_Type = StorageType
_LpFiTestStorageType_Object = MibTableColumn
lpFiTestStorageType = _LpFiTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 1, 1, 4),
    _LpFiTestStorageType_Type()
)
lpFiTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestStorageType.setStatus("mandatory")
_LpFiTestIndex_Type = NonReplicated
_LpFiTestIndex_Object = MibTableColumn
lpFiTestIndex = _LpFiTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 1, 1, 10),
    _LpFiTestIndex_Type()
)
lpFiTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpFiTestIndex.setStatus("mandatory")
_LpFiTestPTOTable_Object = MibTable
lpFiTestPTOTable = _LpFiTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 10)
)
if mibBuilder.loadTexts:
    lpFiTestPTOTable.setStatus("mandatory")
_LpFiTestPTOEntry_Object = MibTableRow
lpFiTestPTOEntry = _LpFiTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 10, 1)
)
lpFiTestPTOEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiTestIndex"),
)
if mibBuilder.loadTexts:
    lpFiTestPTOEntry.setStatus("mandatory")


class _LpFiTestType_Type(Integer32):
    """Custom type lpFiTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              257,
              258,
              259,
              260,
              263,
              264,
              265,
              266,
              267,
              268)
        )
    )
    namedValues = NamedValues(
        *(("extThruA", 265),
          ("extThruB", 266),
          ("extWrapA", 263),
          ("extWrapAB", 267),
          ("extWrapB", 264),
          ("extWrapBA", 268),
          ("normal", 1),
          ("onCard", 0),
          ("thruA", 259),
          ("thruB", 260),
          ("wrapA", 257),
          ("wrapB", 258))
    )


_LpFiTestType_Type.__name__ = "Integer32"
_LpFiTestType_Object = MibTableColumn
lpFiTestType = _LpFiTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 10, 1, 1),
    _LpFiTestType_Type()
)
lpFiTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiTestType.setStatus("mandatory")


class _LpFiTestFrmSize_Type(Unsigned32):
    """Custom type lpFiTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpFiTestFrmSize_Type.__name__ = "Unsigned32"
_LpFiTestFrmSize_Object = MibTableColumn
lpFiTestFrmSize = _LpFiTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 10, 1, 2),
    _LpFiTestFrmSize_Type()
)
lpFiTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiTestFrmSize.setStatus("mandatory")


class _LpFiTestDuration_Type(Unsigned32):
    """Custom type lpFiTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpFiTestDuration_Type.__name__ = "Unsigned32"
_LpFiTestDuration_Object = MibTableColumn
lpFiTestDuration = _LpFiTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 10, 1, 3),
    _LpFiTestDuration_Type()
)
lpFiTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiTestDuration.setStatus("mandatory")
_LpFiTestResultsTable_Object = MibTable
lpFiTestResultsTable = _LpFiTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11)
)
if mibBuilder.loadTexts:
    lpFiTestResultsTable.setStatus("mandatory")
_LpFiTestResultsEntry_Object = MibTableRow
lpFiTestResultsEntry = _LpFiTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1)
)
lpFiTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiTestIndex"),
)
if mibBuilder.loadTexts:
    lpFiTestResultsEntry.setStatus("mandatory")
_LpFiTestElapsedTime_Type = Counter32
_LpFiTestElapsedTime_Object = MibTableColumn
lpFiTestElapsedTime = _LpFiTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 4),
    _LpFiTestElapsedTime_Type()
)
lpFiTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestElapsedTime.setStatus("mandatory")


class _LpFiTestTimeRemaining_Type(Unsigned32):
    """Custom type lpFiTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpFiTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpFiTestTimeRemaining_Object = MibTableColumn
lpFiTestTimeRemaining = _LpFiTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 5),
    _LpFiTestTimeRemaining_Type()
)
lpFiTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestTimeRemaining.setStatus("mandatory")


class _LpFiTestCauseOfTermination_Type(Integer32):
    """Custom type lpFiTestCauseOfTermination based on Integer32"""
    defaultValue = 3

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
        *(("neverStarted", 3),
          ("stoppedByOperator", 1),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_LpFiTestCauseOfTermination_Type.__name__ = "Integer32"
_LpFiTestCauseOfTermination_Object = MibTableColumn
lpFiTestCauseOfTermination = _LpFiTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 6),
    _LpFiTestCauseOfTermination_Type()
)
lpFiTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestCauseOfTermination.setStatus("mandatory")
_LpFiTestFrmTx_Type = PassportCounter64
_LpFiTestFrmTx_Object = MibTableColumn
lpFiTestFrmTx = _LpFiTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 7),
    _LpFiTestFrmTx_Type()
)
lpFiTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestFrmTx.setStatus("mandatory")
_LpFiTestBitsTx_Type = PassportCounter64
_LpFiTestBitsTx_Object = MibTableColumn
lpFiTestBitsTx = _LpFiTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 8),
    _LpFiTestBitsTx_Type()
)
lpFiTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestBitsTx.setStatus("mandatory")
_LpFiTestFrmRx_Type = PassportCounter64
_LpFiTestFrmRx_Object = MibTableColumn
lpFiTestFrmRx = _LpFiTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 9),
    _LpFiTestFrmRx_Type()
)
lpFiTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestFrmRx.setStatus("mandatory")
_LpFiTestBitsRx_Type = PassportCounter64
_LpFiTestBitsRx_Object = MibTableColumn
lpFiTestBitsRx = _LpFiTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 10),
    _LpFiTestBitsRx_Type()
)
lpFiTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestBitsRx.setStatus("mandatory")
_LpFiTestErroredFrmRx_Type = PassportCounter64
_LpFiTestErroredFrmRx_Object = MibTableColumn
lpFiTestErroredFrmRx = _LpFiTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 5, 11, 1, 11),
    _LpFiTestErroredFrmRx_Type()
)
lpFiTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTestErroredFrmRx.setStatus("mandatory")
_LpFiCidDataTable_Object = MibTable
lpFiCidDataTable = _LpFiCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 10)
)
if mibBuilder.loadTexts:
    lpFiCidDataTable.setStatus("mandatory")
_LpFiCidDataEntry_Object = MibTableRow
lpFiCidDataEntry = _LpFiCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 10, 1)
)
lpFiCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiCidDataEntry.setStatus("mandatory")


class _LpFiCustomerIdentifier_Type(Unsigned32):
    """Custom type lpFiCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpFiCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpFiCustomerIdentifier_Object = MibTableColumn
lpFiCustomerIdentifier = _LpFiCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 10, 1, 1),
    _LpFiCustomerIdentifier_Type()
)
lpFiCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiCustomerIdentifier.setStatus("mandatory")
_LpFiIfEntryTable_Object = MibTable
lpFiIfEntryTable = _LpFiIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 11)
)
if mibBuilder.loadTexts:
    lpFiIfEntryTable.setStatus("mandatory")
_LpFiIfEntryEntry_Object = MibTableRow
lpFiIfEntryEntry = _LpFiIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 11, 1)
)
lpFiIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiIfEntryEntry.setStatus("mandatory")


class _LpFiIfAdminStatus_Type(Integer32):
    """Custom type lpFiIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpFiIfAdminStatus_Type.__name__ = "Integer32"
_LpFiIfAdminStatus_Object = MibTableColumn
lpFiIfAdminStatus = _LpFiIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 11, 1, 1),
    _LpFiIfAdminStatus_Type()
)
lpFiIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiIfAdminStatus.setStatus("mandatory")


class _LpFiIfIndex_Type(InterfaceIndex):
    """Custom type lpFiIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpFiIfIndex_Type.__name__ = "InterfaceIndex"
_LpFiIfIndex_Object = MibTableColumn
lpFiIfIndex = _LpFiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 11, 1, 2),
    _LpFiIfIndex_Type()
)
lpFiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiIfIndex.setStatus("mandatory")
_LpFiSmtProvTable_Object = MibTable
lpFiSmtProvTable = _LpFiSmtProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12)
)
if mibBuilder.loadTexts:
    lpFiSmtProvTable.setStatus("mandatory")
_LpFiSmtProvEntry_Object = MibTableRow
lpFiSmtProvEntry = _LpFiSmtProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1)
)
lpFiSmtProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiSmtProvEntry.setStatus("mandatory")


class _LpFiUserData_Type(AsciiString):
    """Custom type lpFiUserData based on AsciiString"""
    defaultHexValue = "46444449"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LpFiUserData_Type.__name__ = "AsciiString"
_LpFiUserData_Object = MibTableColumn
lpFiUserData = _LpFiUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 1),
    _LpFiUserData_Type()
)
lpFiUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiUserData.setStatus("mandatory")


class _LpFiAcceptAa_Type(Integer32):
    """Custom type lpFiAcceptAa based on Integer32"""
    defaultValue = 2

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


_LpFiAcceptAa_Type.__name__ = "Integer32"
_LpFiAcceptAa_Object = MibTableColumn
lpFiAcceptAa = _LpFiAcceptAa_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 2),
    _LpFiAcceptAa_Type()
)
lpFiAcceptAa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiAcceptAa.setStatus("mandatory")


class _LpFiAcceptBb_Type(Integer32):
    """Custom type lpFiAcceptBb based on Integer32"""
    defaultValue = 2

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


_LpFiAcceptBb_Type.__name__ = "Integer32"
_LpFiAcceptBb_Object = MibTableColumn
lpFiAcceptBb = _LpFiAcceptBb_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 3),
    _LpFiAcceptBb_Type()
)
lpFiAcceptBb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiAcceptBb.setStatus("mandatory")


class _LpFiAcceptAs_Type(Integer32):
    """Custom type lpFiAcceptAs based on Integer32"""
    defaultValue = 2

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


_LpFiAcceptAs_Type.__name__ = "Integer32"
_LpFiAcceptAs_Object = MibTableColumn
lpFiAcceptAs = _LpFiAcceptAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 4),
    _LpFiAcceptAs_Type()
)
lpFiAcceptAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiAcceptAs.setStatus("mandatory")


class _LpFiAcceptBs_Type(Integer32):
    """Custom type lpFiAcceptBs based on Integer32"""
    defaultValue = 2

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


_LpFiAcceptBs_Type.__name__ = "Integer32"
_LpFiAcceptBs_Object = MibTableColumn
lpFiAcceptBs = _LpFiAcceptBs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 5),
    _LpFiAcceptBs_Type()
)
lpFiAcceptBs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiAcceptBs.setStatus("mandatory")


class _LpFiAcceptAm_Type(Integer32):
    """Custom type lpFiAcceptAm based on Integer32"""
    defaultValue = 1

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


_LpFiAcceptAm_Type.__name__ = "Integer32"
_LpFiAcceptAm_Object = MibTableColumn
lpFiAcceptAm = _LpFiAcceptAm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 6),
    _LpFiAcceptAm_Type()
)
lpFiAcceptAm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiAcceptAm.setStatus("mandatory")


class _LpFiAcceptBm_Type(Integer32):
    """Custom type lpFiAcceptBm based on Integer32"""
    defaultValue = 1

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


_LpFiAcceptBm_Type.__name__ = "Integer32"
_LpFiAcceptBm_Object = MibTableColumn
lpFiAcceptBm = _LpFiAcceptBm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 7),
    _LpFiAcceptBm_Type()
)
lpFiAcceptBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiAcceptBm.setStatus("mandatory")


class _LpFiUseThruBa_Type(Integer32):
    """Custom type lpFiUseThruBa based on Integer32"""
    defaultValue = 2

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


_LpFiUseThruBa_Type.__name__ = "Integer32"
_LpFiUseThruBa_Object = MibTableColumn
lpFiUseThruBa = _LpFiUseThruBa_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 8),
    _LpFiUseThruBa_Type()
)
lpFiUseThruBa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiUseThruBa.setStatus("mandatory")


class _LpFiNeighborNotifyInterval_Type(Unsigned32):
    """Custom type lpFiNeighborNotifyInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_LpFiNeighborNotifyInterval_Type.__name__ = "Unsigned32"
_LpFiNeighborNotifyInterval_Object = MibTableColumn
lpFiNeighborNotifyInterval = _LpFiNeighborNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 10),
    _LpFiNeighborNotifyInterval_Type()
)
lpFiNeighborNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiNeighborNotifyInterval.setStatus("mandatory")


class _LpFiStatusReportPolicy_Type(Integer32):
    """Custom type lpFiStatusReportPolicy based on Integer32"""
    defaultValue = 1

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


_LpFiStatusReportPolicy_Type.__name__ = "Integer32"
_LpFiStatusReportPolicy_Object = MibTableColumn
lpFiStatusReportPolicy = _LpFiStatusReportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 11),
    _LpFiStatusReportPolicy_Type()
)
lpFiStatusReportPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiStatusReportPolicy.setStatus("mandatory")


class _LpFiTraceMaxExpirationTimer_Type(FddiTimeMilli):
    """Custom type lpFiTraceMaxExpirationTimer based on FddiTimeMilli"""
    defaultValue = 7000

    subtypeSpec = FddiTimeMilli.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_LpFiTraceMaxExpirationTimer_Type.__name__ = "FddiTimeMilli"
_LpFiTraceMaxExpirationTimer_Object = MibTableColumn
lpFiTraceMaxExpirationTimer = _LpFiTraceMaxExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 12),
    _LpFiTraceMaxExpirationTimer_Type()
)
lpFiTraceMaxExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiTraceMaxExpirationTimer.setStatus("mandatory")
_LpFiApplicationFramerName_Type = Link
_LpFiApplicationFramerName_Object = MibTableColumn
lpFiApplicationFramerName = _LpFiApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 12, 1, 13),
    _LpFiApplicationFramerName_Type()
)
lpFiApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiApplicationFramerName.setStatus("mandatory")
_LpFiMacProvTable_Object = MibTable
lpFiMacProvTable = _LpFiMacProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 13)
)
if mibBuilder.loadTexts:
    lpFiMacProvTable.setStatus("mandatory")
_LpFiMacProvEntry_Object = MibTableRow
lpFiMacProvEntry = _LpFiMacProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 13, 1)
)
lpFiMacProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiMacProvEntry.setStatus("mandatory")


class _LpFiTokenRequestTimer_Type(FddiTimeNano):
    """Custom type lpFiTokenRequestTimer based on FddiTimeNano"""
    defaultValue = 165290000

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20480, 1340000000),
    )


_LpFiTokenRequestTimer_Type.__name__ = "FddiTimeNano"
_LpFiTokenRequestTimer_Object = MibTableColumn
lpFiTokenRequestTimer = _LpFiTokenRequestTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 13, 1, 1),
    _LpFiTokenRequestTimer_Type()
)
lpFiTokenRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiTokenRequestTimer.setStatus("mandatory")


class _LpFiTokenMaxTimer_Type(FddiTimeNano):
    """Custom type lpFiTokenMaxTimer based on FddiTimeNano"""
    defaultValue = 167770000

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40960, 1342200000),
    )


_LpFiTokenMaxTimer_Type.__name__ = "FddiTimeNano"
_LpFiTokenMaxTimer_Object = MibTableColumn
lpFiTokenMaxTimer = _LpFiTokenMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 13, 1, 2),
    _LpFiTokenMaxTimer_Type()
)
lpFiTokenMaxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiTokenMaxTimer.setStatus("mandatory")


class _LpFiValidTransmissionTimer_Type(FddiTimeNano):
    """Custom type lpFiValidTransmissionTimer based on FddiTimeNano"""
    defaultValue = 2621400

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40960, 1342200000),
    )


_LpFiValidTransmissionTimer_Type.__name__ = "FddiTimeNano"
_LpFiValidTransmissionTimer_Object = MibTableColumn
lpFiValidTransmissionTimer = _LpFiValidTransmissionTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 13, 1, 3),
    _LpFiValidTransmissionTimer_Type()
)
lpFiValidTransmissionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiValidTransmissionTimer.setStatus("mandatory")
_LpFiAdminInfoTable_Object = MibTable
lpFiAdminInfoTable = _LpFiAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 14)
)
if mibBuilder.loadTexts:
    lpFiAdminInfoTable.setStatus("mandatory")
_LpFiAdminInfoEntry_Object = MibTableRow
lpFiAdminInfoEntry = _LpFiAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 14, 1)
)
lpFiAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiAdminInfoEntry.setStatus("mandatory")


class _LpFiVendor_Type(AsciiString):
    """Custom type lpFiVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpFiVendor_Type.__name__ = "AsciiString"
_LpFiVendor_Object = MibTableColumn
lpFiVendor = _LpFiVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 14, 1, 1),
    _LpFiVendor_Type()
)
lpFiVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiVendor.setStatus("mandatory")


class _LpFiCommentText_Type(AsciiString):
    """Custom type lpFiCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpFiCommentText_Type.__name__ = "AsciiString"
_LpFiCommentText_Object = MibTableColumn
lpFiCommentText = _LpFiCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 14, 1, 2),
    _LpFiCommentText_Type()
)
lpFiCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpFiCommentText.setStatus("mandatory")
_LpFiStateTable_Object = MibTable
lpFiStateTable = _LpFiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 16)
)
if mibBuilder.loadTexts:
    lpFiStateTable.setStatus("mandatory")
_LpFiStateEntry_Object = MibTableRow
lpFiStateEntry = _LpFiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 16, 1)
)
lpFiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiStateEntry.setStatus("mandatory")


class _LpFiAdminState_Type(Integer32):
    """Custom type lpFiAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_LpFiAdminState_Type.__name__ = "Integer32"
_LpFiAdminState_Object = MibTableColumn
lpFiAdminState = _LpFiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 16, 1, 1),
    _LpFiAdminState_Type()
)
lpFiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiAdminState.setStatus("mandatory")


class _LpFiOperationalState_Type(Integer32):
    """Custom type lpFiOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LpFiOperationalState_Type.__name__ = "Integer32"
_LpFiOperationalState_Object = MibTableColumn
lpFiOperationalState = _LpFiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 16, 1, 2),
    _LpFiOperationalState_Type()
)
lpFiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiOperationalState.setStatus("mandatory")


class _LpFiUsageState_Type(Integer32):
    """Custom type lpFiUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_LpFiUsageState_Type.__name__ = "Integer32"
_LpFiUsageState_Object = MibTableColumn
lpFiUsageState = _LpFiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 16, 1, 3),
    _LpFiUsageState_Type()
)
lpFiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiUsageState.setStatus("mandatory")
_LpFiOperStatusTable_Object = MibTable
lpFiOperStatusTable = _LpFiOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 17)
)
if mibBuilder.loadTexts:
    lpFiOperStatusTable.setStatus("mandatory")
_LpFiOperStatusEntry_Object = MibTableRow
lpFiOperStatusEntry = _LpFiOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 17, 1)
)
lpFiOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiOperStatusEntry.setStatus("mandatory")


class _LpFiSnmpOperStatus_Type(Integer32):
    """Custom type lpFiSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpFiSnmpOperStatus_Type.__name__ = "Integer32"
_LpFiSnmpOperStatus_Object = MibTableColumn
lpFiSnmpOperStatus = _LpFiSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 17, 1, 1),
    _LpFiSnmpOperStatus_Type()
)
lpFiSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiSnmpOperStatus.setStatus("mandatory")
_LpFiSmtOperTable_Object = MibTable
lpFiSmtOperTable = _LpFiSmtOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 18)
)
if mibBuilder.loadTexts:
    lpFiSmtOperTable.setStatus("mandatory")
_LpFiSmtOperEntry_Object = MibTableRow
lpFiSmtOperEntry = _LpFiSmtOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 18, 1)
)
lpFiSmtOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiSmtOperEntry.setStatus("mandatory")


class _LpFiVersion_Type(AsciiString):
    """Custom type lpFiVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LpFiVersion_Type.__name__ = "AsciiString"
_LpFiVersion_Object = MibTableColumn
lpFiVersion = _LpFiVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 18, 1, 1),
    _LpFiVersion_Type()
)
lpFiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiVersion.setStatus("mandatory")


class _LpFiBypassPresent_Type(Integer32):
    """Custom type lpFiBypassPresent based on Integer32"""
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


_LpFiBypassPresent_Type.__name__ = "Integer32"
_LpFiBypassPresent_Object = MibTableColumn
lpFiBypassPresent = _LpFiBypassPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 18, 1, 14),
    _LpFiBypassPresent_Type()
)
lpFiBypassPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiBypassPresent.setStatus("mandatory")


class _LpFiEcmState_Type(Integer32):
    """Custom type lpFiEcmState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("check", 7),
          ("deinsert", 8),
          ("in", 2),
          ("insert", 6),
          ("leave", 4),
          ("out", 1),
          ("pathTest", 5),
          ("trace", 3))
    )


_LpFiEcmState_Type.__name__ = "Integer32"
_LpFiEcmState_Object = MibTableColumn
lpFiEcmState = _LpFiEcmState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 18, 1, 15),
    _LpFiEcmState_Type()
)
lpFiEcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiEcmState.setStatus("mandatory")


class _LpFiCfState_Type(Integer32):
    """Custom type lpFiCfState based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("cWrapA", 10),
          ("cWrapB", 11),
          ("cWrapS", 12),
          ("isolated", 1),
          ("localA", 2),
          ("localAB", 4),
          ("localB", 3),
          ("localS", 5),
          ("thru", 13),
          ("wrapA", 6),
          ("wrapAB", 8),
          ("wrapB", 7),
          ("wrapS", 9))
    )


_LpFiCfState_Type.__name__ = "Integer32"
_LpFiCfState_Object = MibTableColumn
lpFiCfState = _LpFiCfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 18, 1, 16),
    _LpFiCfState_Type()
)
lpFiCfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiCfState.setStatus("mandatory")
_LpFiMacOperTable_Object = MibTable
lpFiMacOperTable = _LpFiMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19)
)
if mibBuilder.loadTexts:
    lpFiMacOperTable.setStatus("mandatory")
_LpFiMacOperEntry_Object = MibTableRow
lpFiMacOperEntry = _LpFiMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1)
)
lpFiMacOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiMacOperEntry.setStatus("mandatory")


class _LpFiRingLatency_Type(Gauge32):
    """Custom type lpFiRingLatency based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 1342000000),
    )


_LpFiRingLatency_Type.__name__ = "Gauge32"
_LpFiRingLatency_Object = MibTableColumn
lpFiRingLatency = _LpFiRingLatency_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 1),
    _LpFiRingLatency_Type()
)
lpFiRingLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiRingLatency.setStatus("mandatory")


class _LpFiMacAddress_Type(FddiMACLongAddressType):
    """Custom type lpFiMacAddress based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiMacAddress_Type.__name__ = "FddiMACLongAddressType"
_LpFiMacAddress_Object = MibTableColumn
lpFiMacAddress = _LpFiMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 10),
    _LpFiMacAddress_Type()
)
lpFiMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiMacAddress.setStatus("mandatory")


class _LpFiUpstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type lpFiUpstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiUpstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_LpFiUpstreamNeighbor_Object = MibTableColumn
lpFiUpstreamNeighbor = _LpFiUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 11),
    _LpFiUpstreamNeighbor_Type()
)
lpFiUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiUpstreamNeighbor.setStatus("mandatory")


class _LpFiDownstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type lpFiDownstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiDownstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_LpFiDownstreamNeighbor_Object = MibTableColumn
lpFiDownstreamNeighbor = _LpFiDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 12),
    _LpFiDownstreamNeighbor_Type()
)
lpFiDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiDownstreamNeighbor.setStatus("mandatory")


class _LpFiOldUpstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type lpFiOldUpstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiOldUpstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_LpFiOldUpstreamNeighbor_Object = MibTableColumn
lpFiOldUpstreamNeighbor = _LpFiOldUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 13),
    _LpFiOldUpstreamNeighbor_Type()
)
lpFiOldUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiOldUpstreamNeighbor.setStatus("mandatory")


class _LpFiOldDownstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type lpFiOldDownstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiOldDownstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_LpFiOldDownstreamNeighbor_Object = MibTableColumn
lpFiOldDownstreamNeighbor = _LpFiOldDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 14),
    _LpFiOldDownstreamNeighbor_Type()
)
lpFiOldDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiOldDownstreamNeighbor.setStatus("mandatory")


class _LpFiDupAddressTest_Type(Integer32):
    """Custom type lpFiDupAddressTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("notDone", 1),
          ("pass", 2))
    )


_LpFiDupAddressTest_Type.__name__ = "Integer32"
_LpFiDupAddressTest_Object = MibTableColumn
lpFiDupAddressTest = _LpFiDupAddressTest_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 15),
    _LpFiDupAddressTest_Type()
)
lpFiDupAddressTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiDupAddressTest.setStatus("mandatory")


class _LpFiTokenNegotiatedTimer_Type(FddiTimeNano):
    """Custom type lpFiTokenNegotiatedTimer based on FddiTimeNano"""
    defaultValue = 167772000

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 1340000000),
    )


_LpFiTokenNegotiatedTimer_Type.__name__ = "FddiTimeNano"
_LpFiTokenNegotiatedTimer_Object = MibTableColumn
lpFiTokenNegotiatedTimer = _LpFiTokenNegotiatedTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 18),
    _LpFiTokenNegotiatedTimer_Type()
)
lpFiTokenNegotiatedTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTokenNegotiatedTimer.setStatus("mandatory")
_LpFiFrameCounts_Type = Counter32
_LpFiFrameCounts_Object = MibTableColumn
lpFiFrameCounts = _LpFiFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 19),
    _LpFiFrameCounts_Type()
)
lpFiFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiFrameCounts.setStatus("mandatory")
_LpFiCopiedCounts_Type = Counter32
_LpFiCopiedCounts_Object = MibTableColumn
lpFiCopiedCounts = _LpFiCopiedCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 20),
    _LpFiCopiedCounts_Type()
)
lpFiCopiedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiCopiedCounts.setStatus("mandatory")
_LpFiTransmitCounts_Type = Counter32
_LpFiTransmitCounts_Object = MibTableColumn
lpFiTransmitCounts = _LpFiTransmitCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 21),
    _LpFiTransmitCounts_Type()
)
lpFiTransmitCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTransmitCounts.setStatus("mandatory")
_LpFiErrorCounts_Type = Counter32
_LpFiErrorCounts_Object = MibTableColumn
lpFiErrorCounts = _LpFiErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 22),
    _LpFiErrorCounts_Type()
)
lpFiErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiErrorCounts.setStatus("mandatory")
_LpFiLostCounts_Type = Counter32
_LpFiLostCounts_Object = MibTableColumn
lpFiLostCounts = _LpFiLostCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 23),
    _LpFiLostCounts_Type()
)
lpFiLostCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLostCounts.setStatus("mandatory")


class _LpFiRmtState_Type(Integer32):
    """Custom type lpFiRmtState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("detect", 4),
          ("directed", 7),
          ("isolated", 1),
          ("nonOp", 2),
          ("nonOpDup", 5),
          ("ringOp", 3),
          ("ringOpDup", 6),
          ("trace", 8))
    )


_LpFiRmtState_Type.__name__ = "Integer32"
_LpFiRmtState_Object = MibTableColumn
lpFiRmtState = _LpFiRmtState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 25),
    _LpFiRmtState_Type()
)
lpFiRmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiRmtState.setStatus("mandatory")


class _LpFiFrameErrorFlag_Type(Integer32):
    """Custom type lpFiFrameErrorFlag based on Integer32"""
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


_LpFiFrameErrorFlag_Type.__name__ = "Integer32"
_LpFiFrameErrorFlag_Object = MibTableColumn
lpFiFrameErrorFlag = _LpFiFrameErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 19, 1, 28),
    _LpFiFrameErrorFlag_Type()
)
lpFiFrameErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiFrameErrorFlag.setStatus("mandatory")
_LpFiMacCOperTable_Object = MibTable
lpFiMacCOperTable = _LpFiMacCOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 20)
)
if mibBuilder.loadTexts:
    lpFiMacCOperTable.setStatus("mandatory")
_LpFiMacCOperEntry_Object = MibTableRow
lpFiMacCOperEntry = _LpFiMacCOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 20, 1)
)
lpFiMacCOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiMacCOperEntry.setStatus("mandatory")
_LpFiTokenCounts_Type = Counter32
_LpFiTokenCounts_Object = MibTableColumn
lpFiTokenCounts = _LpFiTokenCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 20, 1, 1),
    _LpFiTokenCounts_Type()
)
lpFiTokenCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTokenCounts.setStatus("mandatory")
_LpFiTvxExpiredCounts_Type = Counter32
_LpFiTvxExpiredCounts_Object = MibTableColumn
lpFiTvxExpiredCounts = _LpFiTvxExpiredCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 20, 1, 2),
    _LpFiTvxExpiredCounts_Type()
)
lpFiTvxExpiredCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiTvxExpiredCounts.setStatus("mandatory")
_LpFiNotCopiedCounts_Type = Counter32
_LpFiNotCopiedCounts_Object = MibTableColumn
lpFiNotCopiedCounts = _LpFiNotCopiedCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 20, 1, 3),
    _LpFiNotCopiedCounts_Type()
)
lpFiNotCopiedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiNotCopiedCounts.setStatus("mandatory")
_LpFiLateCounts_Type = Counter32
_LpFiLateCounts_Object = MibTableColumn
lpFiLateCounts = _LpFiLateCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 20, 1, 4),
    _LpFiLateCounts_Type()
)
lpFiLateCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiLateCounts.setStatus("mandatory")
_LpFiRingOpCounts_Type = Counter32
_LpFiRingOpCounts_Object = MibTableColumn
lpFiRingOpCounts = _LpFiRingOpCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 20, 1, 5),
    _LpFiRingOpCounts_Type()
)
lpFiRingOpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiRingOpCounts.setStatus("mandatory")
_LpFiNcMacOperTable_Object = MibTable
lpFiNcMacOperTable = _LpFiNcMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 26)
)
if mibBuilder.loadTexts:
    lpFiNcMacOperTable.setStatus("mandatory")
_LpFiNcMacOperEntry_Object = MibTableRow
lpFiNcMacOperEntry = _LpFiNcMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 26, 1)
)
lpFiNcMacOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpFiIndex"),
)
if mibBuilder.loadTexts:
    lpFiNcMacOperEntry.setStatus("mandatory")


class _LpFiNcMacAddress_Type(MacAddress):
    """Custom type lpFiNcMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiNcMacAddress_Type.__name__ = "MacAddress"
_LpFiNcMacAddress_Object = MibTableColumn
lpFiNcMacAddress = _LpFiNcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 26, 1, 1),
    _LpFiNcMacAddress_Type()
)
lpFiNcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiNcMacAddress.setStatus("mandatory")


class _LpFiNcUpstreamNeighbor_Type(MacAddress):
    """Custom type lpFiNcUpstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiNcUpstreamNeighbor_Type.__name__ = "MacAddress"
_LpFiNcUpstreamNeighbor_Object = MibTableColumn
lpFiNcUpstreamNeighbor = _LpFiNcUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 26, 1, 2),
    _LpFiNcUpstreamNeighbor_Type()
)
lpFiNcUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiNcUpstreamNeighbor.setStatus("mandatory")


class _LpFiNcDownstreamNeighbor_Type(MacAddress):
    """Custom type lpFiNcDownstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiNcDownstreamNeighbor_Type.__name__ = "MacAddress"
_LpFiNcDownstreamNeighbor_Object = MibTableColumn
lpFiNcDownstreamNeighbor = _LpFiNcDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 26, 1, 3),
    _LpFiNcDownstreamNeighbor_Type()
)
lpFiNcDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiNcDownstreamNeighbor.setStatus("mandatory")


class _LpFiNcOldUpstreamNeighbor_Type(MacAddress):
    """Custom type lpFiNcOldUpstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiNcOldUpstreamNeighbor_Type.__name__ = "MacAddress"
_LpFiNcOldUpstreamNeighbor_Object = MibTableColumn
lpFiNcOldUpstreamNeighbor = _LpFiNcOldUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 26, 1, 4),
    _LpFiNcOldUpstreamNeighbor_Type()
)
lpFiNcOldUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiNcOldUpstreamNeighbor.setStatus("mandatory")


class _LpFiNcOldDownstreamNeighbor_Type(MacAddress):
    """Custom type lpFiNcOldDownstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpFiNcOldDownstreamNeighbor_Type.__name__ = "MacAddress"
_LpFiNcOldDownstreamNeighbor_Object = MibTableColumn
lpFiNcOldDownstreamNeighbor = _LpFiNcOldDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 4, 26, 1, 5),
    _LpFiNcOldDownstreamNeighbor_Type()
)
lpFiNcOldDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpFiNcOldDownstreamNeighbor.setStatus("mandatory")
_LpTr_ObjectIdentity = ObjectIdentity
lpTr = _LpTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13)
)
_LpTrRowStatusTable_Object = MibTable
lpTrRowStatusTable = _LpTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 1)
)
if mibBuilder.loadTexts:
    lpTrRowStatusTable.setStatus("mandatory")
_LpTrRowStatusEntry_Object = MibTableRow
lpTrRowStatusEntry = _LpTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 1, 1)
)
lpTrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrRowStatusEntry.setStatus("mandatory")
_LpTrRowStatus_Type = RowStatus
_LpTrRowStatus_Object = MibTableColumn
lpTrRowStatus = _LpTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 1, 1, 1),
    _LpTrRowStatus_Type()
)
lpTrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrRowStatus.setStatus("mandatory")
_LpTrComponentName_Type = DisplayString
_LpTrComponentName_Object = MibTableColumn
lpTrComponentName = _LpTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 1, 1, 2),
    _LpTrComponentName_Type()
)
lpTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrComponentName.setStatus("mandatory")
_LpTrStorageType_Type = StorageType
_LpTrStorageType_Object = MibTableColumn
lpTrStorageType = _LpTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 1, 1, 4),
    _LpTrStorageType_Type()
)
lpTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrStorageType.setStatus("mandatory")


class _LpTrIndex_Type(Integer32):
    """Custom type lpTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_LpTrIndex_Type.__name__ = "Integer32"
_LpTrIndex_Object = MibTableColumn
lpTrIndex = _LpTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 1, 1, 10),
    _LpTrIndex_Type()
)
lpTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrIndex.setStatus("mandatory")
_LpTrLt_ObjectIdentity = ObjectIdentity
lpTrLt = _LpTrLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2)
)
_LpTrLtRowStatusTable_Object = MibTable
lpTrLtRowStatusTable = _LpTrLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 1)
)
if mibBuilder.loadTexts:
    lpTrLtRowStatusTable.setStatus("mandatory")
_LpTrLtRowStatusEntry_Object = MibTableRow
lpTrLtRowStatusEntry = _LpTrLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 1, 1)
)
lpTrLtRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtRowStatusEntry.setStatus("mandatory")
_LpTrLtRowStatus_Type = RowStatus
_LpTrLtRowStatus_Object = MibTableColumn
lpTrLtRowStatus = _LpTrLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 1, 1, 1),
    _LpTrLtRowStatus_Type()
)
lpTrLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtRowStatus.setStatus("mandatory")
_LpTrLtComponentName_Type = DisplayString
_LpTrLtComponentName_Object = MibTableColumn
lpTrLtComponentName = _LpTrLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 1, 1, 2),
    _LpTrLtComponentName_Type()
)
lpTrLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtComponentName.setStatus("mandatory")
_LpTrLtStorageType_Type = StorageType
_LpTrLtStorageType_Object = MibTableColumn
lpTrLtStorageType = _LpTrLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 1, 1, 4),
    _LpTrLtStorageType_Type()
)
lpTrLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtStorageType.setStatus("mandatory")
_LpTrLtIndex_Type = NonReplicated
_LpTrLtIndex_Object = MibTableColumn
lpTrLtIndex = _LpTrLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 1, 1, 10),
    _LpTrLtIndex_Type()
)
lpTrLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtIndex.setStatus("mandatory")
_LpTrLtFrmCmp_ObjectIdentity = ObjectIdentity
lpTrLtFrmCmp = _LpTrLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2)
)
_LpTrLtFrmCmpRowStatusTable_Object = MibTable
lpTrLtFrmCmpRowStatusTable = _LpTrLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFrmCmpRowStatusTable.setStatus("mandatory")
_LpTrLtFrmCmpRowStatusEntry_Object = MibTableRow
lpTrLtFrmCmpRowStatusEntry = _LpTrLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 1, 1)
)
lpTrLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFrmCmpRowStatusEntry.setStatus("mandatory")
_LpTrLtFrmCmpRowStatus_Type = RowStatus
_LpTrLtFrmCmpRowStatus_Object = MibTableColumn
lpTrLtFrmCmpRowStatus = _LpTrLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 1, 1, 1),
    _LpTrLtFrmCmpRowStatus_Type()
)
lpTrLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFrmCmpRowStatus.setStatus("mandatory")
_LpTrLtFrmCmpComponentName_Type = DisplayString
_LpTrLtFrmCmpComponentName_Object = MibTableColumn
lpTrLtFrmCmpComponentName = _LpTrLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 1, 1, 2),
    _LpTrLtFrmCmpComponentName_Type()
)
lpTrLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFrmCmpComponentName.setStatus("mandatory")
_LpTrLtFrmCmpStorageType_Type = StorageType
_LpTrLtFrmCmpStorageType_Object = MibTableColumn
lpTrLtFrmCmpStorageType = _LpTrLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 1, 1, 4),
    _LpTrLtFrmCmpStorageType_Type()
)
lpTrLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFrmCmpStorageType.setStatus("mandatory")
_LpTrLtFrmCmpIndex_Type = NonReplicated
_LpTrLtFrmCmpIndex_Object = MibTableColumn
lpTrLtFrmCmpIndex = _LpTrLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 1, 1, 10),
    _LpTrLtFrmCmpIndex_Type()
)
lpTrLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFrmCmpIndex.setStatus("mandatory")
_LpTrLtFrmCmpTopTable_Object = MibTable
lpTrLtFrmCmpTopTable = _LpTrLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFrmCmpTopTable.setStatus("mandatory")
_LpTrLtFrmCmpTopEntry_Object = MibTableRow
lpTrLtFrmCmpTopEntry = _LpTrLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 10, 1)
)
lpTrLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFrmCmpTopEntry.setStatus("mandatory")


class _LpTrLtFrmCmpTData_Type(AsciiString):
    """Custom type lpTrLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFrmCmpTData_Type.__name__ = "AsciiString"
_LpTrLtFrmCmpTData_Object = MibTableColumn
lpTrLtFrmCmpTData = _LpTrLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 2, 10, 1, 1),
    _LpTrLtFrmCmpTData_Type()
)
lpTrLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFrmCmpTData.setStatus("mandatory")
_LpTrLtFrmCpy_ObjectIdentity = ObjectIdentity
lpTrLtFrmCpy = _LpTrLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3)
)
_LpTrLtFrmCpyRowStatusTable_Object = MibTable
lpTrLtFrmCpyRowStatusTable = _LpTrLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFrmCpyRowStatusTable.setStatus("mandatory")
_LpTrLtFrmCpyRowStatusEntry_Object = MibTableRow
lpTrLtFrmCpyRowStatusEntry = _LpTrLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 1, 1)
)
lpTrLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFrmCpyRowStatusEntry.setStatus("mandatory")
_LpTrLtFrmCpyRowStatus_Type = RowStatus
_LpTrLtFrmCpyRowStatus_Object = MibTableColumn
lpTrLtFrmCpyRowStatus = _LpTrLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 1, 1, 1),
    _LpTrLtFrmCpyRowStatus_Type()
)
lpTrLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFrmCpyRowStatus.setStatus("mandatory")
_LpTrLtFrmCpyComponentName_Type = DisplayString
_LpTrLtFrmCpyComponentName_Object = MibTableColumn
lpTrLtFrmCpyComponentName = _LpTrLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 1, 1, 2),
    _LpTrLtFrmCpyComponentName_Type()
)
lpTrLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFrmCpyComponentName.setStatus("mandatory")
_LpTrLtFrmCpyStorageType_Type = StorageType
_LpTrLtFrmCpyStorageType_Object = MibTableColumn
lpTrLtFrmCpyStorageType = _LpTrLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 1, 1, 4),
    _LpTrLtFrmCpyStorageType_Type()
)
lpTrLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFrmCpyStorageType.setStatus("mandatory")
_LpTrLtFrmCpyIndex_Type = NonReplicated
_LpTrLtFrmCpyIndex_Object = MibTableColumn
lpTrLtFrmCpyIndex = _LpTrLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 1, 1, 10),
    _LpTrLtFrmCpyIndex_Type()
)
lpTrLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFrmCpyIndex.setStatus("mandatory")
_LpTrLtFrmCpyTopTable_Object = MibTable
lpTrLtFrmCpyTopTable = _LpTrLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFrmCpyTopTable.setStatus("mandatory")
_LpTrLtFrmCpyTopEntry_Object = MibTableRow
lpTrLtFrmCpyTopEntry = _LpTrLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 10, 1)
)
lpTrLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFrmCpyTopEntry.setStatus("mandatory")


class _LpTrLtFrmCpyTData_Type(AsciiString):
    """Custom type lpTrLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFrmCpyTData_Type.__name__ = "AsciiString"
_LpTrLtFrmCpyTData_Object = MibTableColumn
lpTrLtFrmCpyTData = _LpTrLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 3, 10, 1, 1),
    _LpTrLtFrmCpyTData_Type()
)
lpTrLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFrmCpyTData.setStatus("mandatory")
_LpTrLtPrtCfg_ObjectIdentity = ObjectIdentity
lpTrLtPrtCfg = _LpTrLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4)
)
_LpTrLtPrtCfgRowStatusTable_Object = MibTable
lpTrLtPrtCfgRowStatusTable = _LpTrLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpTrLtPrtCfgRowStatusTable.setStatus("mandatory")
_LpTrLtPrtCfgRowStatusEntry_Object = MibTableRow
lpTrLtPrtCfgRowStatusEntry = _LpTrLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 1, 1)
)
lpTrLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtPrtCfgRowStatusEntry.setStatus("mandatory")
_LpTrLtPrtCfgRowStatus_Type = RowStatus
_LpTrLtPrtCfgRowStatus_Object = MibTableColumn
lpTrLtPrtCfgRowStatus = _LpTrLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 1, 1, 1),
    _LpTrLtPrtCfgRowStatus_Type()
)
lpTrLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtPrtCfgRowStatus.setStatus("mandatory")
_LpTrLtPrtCfgComponentName_Type = DisplayString
_LpTrLtPrtCfgComponentName_Object = MibTableColumn
lpTrLtPrtCfgComponentName = _LpTrLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 1, 1, 2),
    _LpTrLtPrtCfgComponentName_Type()
)
lpTrLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtPrtCfgComponentName.setStatus("mandatory")
_LpTrLtPrtCfgStorageType_Type = StorageType
_LpTrLtPrtCfgStorageType_Object = MibTableColumn
lpTrLtPrtCfgStorageType = _LpTrLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 1, 1, 4),
    _LpTrLtPrtCfgStorageType_Type()
)
lpTrLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtPrtCfgStorageType.setStatus("mandatory")
_LpTrLtPrtCfgIndex_Type = NonReplicated
_LpTrLtPrtCfgIndex_Object = MibTableColumn
lpTrLtPrtCfgIndex = _LpTrLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 1, 1, 10),
    _LpTrLtPrtCfgIndex_Type()
)
lpTrLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtPrtCfgIndex.setStatus("mandatory")
_LpTrLtPrtCfgTopTable_Object = MibTable
lpTrLtPrtCfgTopTable = _LpTrLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpTrLtPrtCfgTopTable.setStatus("mandatory")
_LpTrLtPrtCfgTopEntry_Object = MibTableRow
lpTrLtPrtCfgTopEntry = _LpTrLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 10, 1)
)
lpTrLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtPrtCfgTopEntry.setStatus("mandatory")


class _LpTrLtPrtCfgTData_Type(AsciiString):
    """Custom type lpTrLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtPrtCfgTData_Type.__name__ = "AsciiString"
_LpTrLtPrtCfgTData_Object = MibTableColumn
lpTrLtPrtCfgTData = _LpTrLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 4, 10, 1, 1),
    _LpTrLtPrtCfgTData_Type()
)
lpTrLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtPrtCfgTData.setStatus("mandatory")
_LpTrLtFb_ObjectIdentity = ObjectIdentity
lpTrLtFb = _LpTrLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5)
)
_LpTrLtFbRowStatusTable_Object = MibTable
lpTrLtFbRowStatusTable = _LpTrLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbRowStatusTable.setStatus("mandatory")
_LpTrLtFbRowStatusEntry_Object = MibTableRow
lpTrLtFbRowStatusEntry = _LpTrLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 1, 1)
)
lpTrLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbRowStatusEntry.setStatus("mandatory")
_LpTrLtFbRowStatus_Type = RowStatus
_LpTrLtFbRowStatus_Object = MibTableColumn
lpTrLtFbRowStatus = _LpTrLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 1, 1, 1),
    _LpTrLtFbRowStatus_Type()
)
lpTrLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbRowStatus.setStatus("mandatory")
_LpTrLtFbComponentName_Type = DisplayString
_LpTrLtFbComponentName_Object = MibTableColumn
lpTrLtFbComponentName = _LpTrLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 1, 1, 2),
    _LpTrLtFbComponentName_Type()
)
lpTrLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbComponentName.setStatus("mandatory")
_LpTrLtFbStorageType_Type = StorageType
_LpTrLtFbStorageType_Object = MibTableColumn
lpTrLtFbStorageType = _LpTrLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 1, 1, 4),
    _LpTrLtFbStorageType_Type()
)
lpTrLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbStorageType.setStatus("mandatory")
_LpTrLtFbIndex_Type = NonReplicated
_LpTrLtFbIndex_Object = MibTableColumn
lpTrLtFbIndex = _LpTrLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 1, 1, 10),
    _LpTrLtFbIndex_Type()
)
lpTrLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbIndex.setStatus("mandatory")
_LpTrLtFbTxInfo_ObjectIdentity = ObjectIdentity
lpTrLtFbTxInfo = _LpTrLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2)
)
_LpTrLtFbTxInfoRowStatusTable_Object = MibTable
lpTrLtFbTxInfoRowStatusTable = _LpTrLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoRowStatusTable.setStatus("mandatory")
_LpTrLtFbTxInfoRowStatusEntry_Object = MibTableRow
lpTrLtFbTxInfoRowStatusEntry = _LpTrLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 1, 1)
)
lpTrLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_LpTrLtFbTxInfoRowStatus_Type = RowStatus
_LpTrLtFbTxInfoRowStatus_Object = MibTableColumn
lpTrLtFbTxInfoRowStatus = _LpTrLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 1, 1, 1),
    _LpTrLtFbTxInfoRowStatus_Type()
)
lpTrLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoRowStatus.setStatus("mandatory")
_LpTrLtFbTxInfoComponentName_Type = DisplayString
_LpTrLtFbTxInfoComponentName_Object = MibTableColumn
lpTrLtFbTxInfoComponentName = _LpTrLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 1, 1, 2),
    _LpTrLtFbTxInfoComponentName_Type()
)
lpTrLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoComponentName.setStatus("mandatory")
_LpTrLtFbTxInfoStorageType_Type = StorageType
_LpTrLtFbTxInfoStorageType_Object = MibTableColumn
lpTrLtFbTxInfoStorageType = _LpTrLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 1, 1, 4),
    _LpTrLtFbTxInfoStorageType_Type()
)
lpTrLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoStorageType.setStatus("mandatory")
_LpTrLtFbTxInfoIndex_Type = NonReplicated
_LpTrLtFbTxInfoIndex_Object = MibTableColumn
lpTrLtFbTxInfoIndex = _LpTrLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 1, 1, 10),
    _LpTrLtFbTxInfoIndex_Type()
)
lpTrLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoIndex.setStatus("mandatory")
_LpTrLtFbTxInfoTopTable_Object = MibTable
lpTrLtFbTxInfoTopTable = _LpTrLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoTopTable.setStatus("mandatory")
_LpTrLtFbTxInfoTopEntry_Object = MibTableRow
lpTrLtFbTxInfoTopEntry = _LpTrLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 10, 1)
)
lpTrLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoTopEntry.setStatus("mandatory")


class _LpTrLtFbTxInfoTData_Type(AsciiString):
    """Custom type lpTrLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbTxInfoTData_Type.__name__ = "AsciiString"
_LpTrLtFbTxInfoTData_Object = MibTableColumn
lpTrLtFbTxInfoTData = _LpTrLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 2, 10, 1, 1),
    _LpTrLtFbTxInfoTData_Type()
)
lpTrLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbTxInfoTData.setStatus("mandatory")
_LpTrLtFbFddiMac_ObjectIdentity = ObjectIdentity
lpTrLtFbFddiMac = _LpTrLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3)
)
_LpTrLtFbFddiMacRowStatusTable_Object = MibTable
lpTrLtFbFddiMacRowStatusTable = _LpTrLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacRowStatusTable.setStatus("mandatory")
_LpTrLtFbFddiMacRowStatusEntry_Object = MibTableRow
lpTrLtFbFddiMacRowStatusEntry = _LpTrLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 1, 1)
)
lpTrLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_LpTrLtFbFddiMacRowStatus_Type = RowStatus
_LpTrLtFbFddiMacRowStatus_Object = MibTableColumn
lpTrLtFbFddiMacRowStatus = _LpTrLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 1, 1, 1),
    _LpTrLtFbFddiMacRowStatus_Type()
)
lpTrLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacRowStatus.setStatus("mandatory")
_LpTrLtFbFddiMacComponentName_Type = DisplayString
_LpTrLtFbFddiMacComponentName_Object = MibTableColumn
lpTrLtFbFddiMacComponentName = _LpTrLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 1, 1, 2),
    _LpTrLtFbFddiMacComponentName_Type()
)
lpTrLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacComponentName.setStatus("mandatory")
_LpTrLtFbFddiMacStorageType_Type = StorageType
_LpTrLtFbFddiMacStorageType_Object = MibTableColumn
lpTrLtFbFddiMacStorageType = _LpTrLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 1, 1, 4),
    _LpTrLtFbFddiMacStorageType_Type()
)
lpTrLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacStorageType.setStatus("mandatory")
_LpTrLtFbFddiMacIndex_Type = NonReplicated
_LpTrLtFbFddiMacIndex_Object = MibTableColumn
lpTrLtFbFddiMacIndex = _LpTrLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 1, 1, 10),
    _LpTrLtFbFddiMacIndex_Type()
)
lpTrLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacIndex.setStatus("mandatory")
_LpTrLtFbFddiMacTopTable_Object = MibTable
lpTrLtFbFddiMacTopTable = _LpTrLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacTopTable.setStatus("mandatory")
_LpTrLtFbFddiMacTopEntry_Object = MibTableRow
lpTrLtFbFddiMacTopEntry = _LpTrLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 10, 1)
)
lpTrLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacTopEntry.setStatus("mandatory")


class _LpTrLtFbFddiMacTData_Type(AsciiString):
    """Custom type lpTrLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbFddiMacTData_Type.__name__ = "AsciiString"
_LpTrLtFbFddiMacTData_Object = MibTableColumn
lpTrLtFbFddiMacTData = _LpTrLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 3, 10, 1, 1),
    _LpTrLtFbFddiMacTData_Type()
)
lpTrLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbFddiMacTData.setStatus("mandatory")
_LpTrLtFbMacEnet_ObjectIdentity = ObjectIdentity
lpTrLtFbMacEnet = _LpTrLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4)
)
_LpTrLtFbMacEnetRowStatusTable_Object = MibTable
lpTrLtFbMacEnetRowStatusTable = _LpTrLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetRowStatusTable.setStatus("mandatory")
_LpTrLtFbMacEnetRowStatusEntry_Object = MibTableRow
lpTrLtFbMacEnetRowStatusEntry = _LpTrLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 1, 1)
)
lpTrLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_LpTrLtFbMacEnetRowStatus_Type = RowStatus
_LpTrLtFbMacEnetRowStatus_Object = MibTableColumn
lpTrLtFbMacEnetRowStatus = _LpTrLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 1, 1, 1),
    _LpTrLtFbMacEnetRowStatus_Type()
)
lpTrLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetRowStatus.setStatus("mandatory")
_LpTrLtFbMacEnetComponentName_Type = DisplayString
_LpTrLtFbMacEnetComponentName_Object = MibTableColumn
lpTrLtFbMacEnetComponentName = _LpTrLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 1, 1, 2),
    _LpTrLtFbMacEnetComponentName_Type()
)
lpTrLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetComponentName.setStatus("mandatory")
_LpTrLtFbMacEnetStorageType_Type = StorageType
_LpTrLtFbMacEnetStorageType_Object = MibTableColumn
lpTrLtFbMacEnetStorageType = _LpTrLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 1, 1, 4),
    _LpTrLtFbMacEnetStorageType_Type()
)
lpTrLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetStorageType.setStatus("mandatory")
_LpTrLtFbMacEnetIndex_Type = NonReplicated
_LpTrLtFbMacEnetIndex_Object = MibTableColumn
lpTrLtFbMacEnetIndex = _LpTrLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 1, 1, 10),
    _LpTrLtFbMacEnetIndex_Type()
)
lpTrLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetIndex.setStatus("mandatory")
_LpTrLtFbMacEnetTopTable_Object = MibTable
lpTrLtFbMacEnetTopTable = _LpTrLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetTopTable.setStatus("mandatory")
_LpTrLtFbMacEnetTopEntry_Object = MibTableRow
lpTrLtFbMacEnetTopEntry = _LpTrLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 10, 1)
)
lpTrLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetTopEntry.setStatus("mandatory")


class _LpTrLtFbMacEnetTData_Type(AsciiString):
    """Custom type lpTrLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbMacEnetTData_Type.__name__ = "AsciiString"
_LpTrLtFbMacEnetTData_Object = MibTableColumn
lpTrLtFbMacEnetTData = _LpTrLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 4, 10, 1, 1),
    _LpTrLtFbMacEnetTData_Type()
)
lpTrLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbMacEnetTData.setStatus("mandatory")
_LpTrLtFbMacTr_ObjectIdentity = ObjectIdentity
lpTrLtFbMacTr = _LpTrLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5)
)
_LpTrLtFbMacTrRowStatusTable_Object = MibTable
lpTrLtFbMacTrRowStatusTable = _LpTrLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbMacTrRowStatusTable.setStatus("mandatory")
_LpTrLtFbMacTrRowStatusEntry_Object = MibTableRow
lpTrLtFbMacTrRowStatusEntry = _LpTrLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 1, 1)
)
lpTrLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbMacTrRowStatusEntry.setStatus("mandatory")
_LpTrLtFbMacTrRowStatus_Type = RowStatus
_LpTrLtFbMacTrRowStatus_Object = MibTableColumn
lpTrLtFbMacTrRowStatus = _LpTrLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 1, 1, 1),
    _LpTrLtFbMacTrRowStatus_Type()
)
lpTrLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbMacTrRowStatus.setStatus("mandatory")
_LpTrLtFbMacTrComponentName_Type = DisplayString
_LpTrLtFbMacTrComponentName_Object = MibTableColumn
lpTrLtFbMacTrComponentName = _LpTrLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 1, 1, 2),
    _LpTrLtFbMacTrComponentName_Type()
)
lpTrLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbMacTrComponentName.setStatus("mandatory")
_LpTrLtFbMacTrStorageType_Type = StorageType
_LpTrLtFbMacTrStorageType_Object = MibTableColumn
lpTrLtFbMacTrStorageType = _LpTrLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 1, 1, 4),
    _LpTrLtFbMacTrStorageType_Type()
)
lpTrLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbMacTrStorageType.setStatus("mandatory")
_LpTrLtFbMacTrIndex_Type = NonReplicated
_LpTrLtFbMacTrIndex_Object = MibTableColumn
lpTrLtFbMacTrIndex = _LpTrLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 1, 1, 10),
    _LpTrLtFbMacTrIndex_Type()
)
lpTrLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbMacTrIndex.setStatus("mandatory")
_LpTrLtFbMacTrTopTable_Object = MibTable
lpTrLtFbMacTrTopTable = _LpTrLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbMacTrTopTable.setStatus("mandatory")
_LpTrLtFbMacTrTopEntry_Object = MibTableRow
lpTrLtFbMacTrTopEntry = _LpTrLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 10, 1)
)
lpTrLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbMacTrTopEntry.setStatus("mandatory")


class _LpTrLtFbMacTrTData_Type(AsciiString):
    """Custom type lpTrLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbMacTrTData_Type.__name__ = "AsciiString"
_LpTrLtFbMacTrTData_Object = MibTableColumn
lpTrLtFbMacTrTData = _LpTrLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 5, 10, 1, 1),
    _LpTrLtFbMacTrTData_Type()
)
lpTrLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbMacTrTData.setStatus("mandatory")
_LpTrLtFbData_ObjectIdentity = ObjectIdentity
lpTrLtFbData = _LpTrLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6)
)
_LpTrLtFbDataRowStatusTable_Object = MibTable
lpTrLtFbDataRowStatusTable = _LpTrLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbDataRowStatusTable.setStatus("mandatory")
_LpTrLtFbDataRowStatusEntry_Object = MibTableRow
lpTrLtFbDataRowStatusEntry = _LpTrLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 1, 1)
)
lpTrLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbDataRowStatusEntry.setStatus("mandatory")
_LpTrLtFbDataRowStatus_Type = RowStatus
_LpTrLtFbDataRowStatus_Object = MibTableColumn
lpTrLtFbDataRowStatus = _LpTrLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 1, 1, 1),
    _LpTrLtFbDataRowStatus_Type()
)
lpTrLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbDataRowStatus.setStatus("mandatory")
_LpTrLtFbDataComponentName_Type = DisplayString
_LpTrLtFbDataComponentName_Object = MibTableColumn
lpTrLtFbDataComponentName = _LpTrLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 1, 1, 2),
    _LpTrLtFbDataComponentName_Type()
)
lpTrLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbDataComponentName.setStatus("mandatory")
_LpTrLtFbDataStorageType_Type = StorageType
_LpTrLtFbDataStorageType_Object = MibTableColumn
lpTrLtFbDataStorageType = _LpTrLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 1, 1, 4),
    _LpTrLtFbDataStorageType_Type()
)
lpTrLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbDataStorageType.setStatus("mandatory")
_LpTrLtFbDataIndex_Type = NonReplicated
_LpTrLtFbDataIndex_Object = MibTableColumn
lpTrLtFbDataIndex = _LpTrLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 1, 1, 10),
    _LpTrLtFbDataIndex_Type()
)
lpTrLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbDataIndex.setStatus("mandatory")
_LpTrLtFbDataTopTable_Object = MibTable
lpTrLtFbDataTopTable = _LpTrLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbDataTopTable.setStatus("mandatory")
_LpTrLtFbDataTopEntry_Object = MibTableRow
lpTrLtFbDataTopEntry = _LpTrLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 10, 1)
)
lpTrLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbDataTopEntry.setStatus("mandatory")


class _LpTrLtFbDataTData_Type(AsciiString):
    """Custom type lpTrLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbDataTData_Type.__name__ = "AsciiString"
_LpTrLtFbDataTData_Object = MibTableColumn
lpTrLtFbDataTData = _LpTrLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 6, 10, 1, 1),
    _LpTrLtFbDataTData_Type()
)
lpTrLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbDataTData.setStatus("mandatory")
_LpTrLtFbIpH_ObjectIdentity = ObjectIdentity
lpTrLtFbIpH = _LpTrLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7)
)
_LpTrLtFbIpHRowStatusTable_Object = MibTable
lpTrLtFbIpHRowStatusTable = _LpTrLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbIpHRowStatusTable.setStatus("mandatory")
_LpTrLtFbIpHRowStatusEntry_Object = MibTableRow
lpTrLtFbIpHRowStatusEntry = _LpTrLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 1, 1)
)
lpTrLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbIpHRowStatusEntry.setStatus("mandatory")
_LpTrLtFbIpHRowStatus_Type = RowStatus
_LpTrLtFbIpHRowStatus_Object = MibTableColumn
lpTrLtFbIpHRowStatus = _LpTrLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 1, 1, 1),
    _LpTrLtFbIpHRowStatus_Type()
)
lpTrLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbIpHRowStatus.setStatus("mandatory")
_LpTrLtFbIpHComponentName_Type = DisplayString
_LpTrLtFbIpHComponentName_Object = MibTableColumn
lpTrLtFbIpHComponentName = _LpTrLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 1, 1, 2),
    _LpTrLtFbIpHComponentName_Type()
)
lpTrLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbIpHComponentName.setStatus("mandatory")
_LpTrLtFbIpHStorageType_Type = StorageType
_LpTrLtFbIpHStorageType_Object = MibTableColumn
lpTrLtFbIpHStorageType = _LpTrLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 1, 1, 4),
    _LpTrLtFbIpHStorageType_Type()
)
lpTrLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbIpHStorageType.setStatus("mandatory")
_LpTrLtFbIpHIndex_Type = NonReplicated
_LpTrLtFbIpHIndex_Object = MibTableColumn
lpTrLtFbIpHIndex = _LpTrLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 1, 1, 10),
    _LpTrLtFbIpHIndex_Type()
)
lpTrLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbIpHIndex.setStatus("mandatory")
_LpTrLtFbIpHTopTable_Object = MibTable
lpTrLtFbIpHTopTable = _LpTrLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbIpHTopTable.setStatus("mandatory")
_LpTrLtFbIpHTopEntry_Object = MibTableRow
lpTrLtFbIpHTopEntry = _LpTrLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 10, 1)
)
lpTrLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbIpHTopEntry.setStatus("mandatory")


class _LpTrLtFbIpHTData_Type(AsciiString):
    """Custom type lpTrLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbIpHTData_Type.__name__ = "AsciiString"
_LpTrLtFbIpHTData_Object = MibTableColumn
lpTrLtFbIpHTData = _LpTrLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 7, 10, 1, 1),
    _LpTrLtFbIpHTData_Type()
)
lpTrLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbIpHTData.setStatus("mandatory")
_LpTrLtFbLlch_ObjectIdentity = ObjectIdentity
lpTrLtFbLlch = _LpTrLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8)
)
_LpTrLtFbLlchRowStatusTable_Object = MibTable
lpTrLtFbLlchRowStatusTable = _LpTrLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbLlchRowStatusTable.setStatus("mandatory")
_LpTrLtFbLlchRowStatusEntry_Object = MibTableRow
lpTrLtFbLlchRowStatusEntry = _LpTrLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 1, 1)
)
lpTrLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbLlchRowStatusEntry.setStatus("mandatory")
_LpTrLtFbLlchRowStatus_Type = RowStatus
_LpTrLtFbLlchRowStatus_Object = MibTableColumn
lpTrLtFbLlchRowStatus = _LpTrLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 1, 1, 1),
    _LpTrLtFbLlchRowStatus_Type()
)
lpTrLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbLlchRowStatus.setStatus("mandatory")
_LpTrLtFbLlchComponentName_Type = DisplayString
_LpTrLtFbLlchComponentName_Object = MibTableColumn
lpTrLtFbLlchComponentName = _LpTrLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 1, 1, 2),
    _LpTrLtFbLlchComponentName_Type()
)
lpTrLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbLlchComponentName.setStatus("mandatory")
_LpTrLtFbLlchStorageType_Type = StorageType
_LpTrLtFbLlchStorageType_Object = MibTableColumn
lpTrLtFbLlchStorageType = _LpTrLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 1, 1, 4),
    _LpTrLtFbLlchStorageType_Type()
)
lpTrLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbLlchStorageType.setStatus("mandatory")
_LpTrLtFbLlchIndex_Type = NonReplicated
_LpTrLtFbLlchIndex_Object = MibTableColumn
lpTrLtFbLlchIndex = _LpTrLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 1, 1, 10),
    _LpTrLtFbLlchIndex_Type()
)
lpTrLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbLlchIndex.setStatus("mandatory")
_LpTrLtFbLlchTopTable_Object = MibTable
lpTrLtFbLlchTopTable = _LpTrLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbLlchTopTable.setStatus("mandatory")
_LpTrLtFbLlchTopEntry_Object = MibTableRow
lpTrLtFbLlchTopEntry = _LpTrLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 10, 1)
)
lpTrLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbLlchTopEntry.setStatus("mandatory")


class _LpTrLtFbLlchTData_Type(AsciiString):
    """Custom type lpTrLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbLlchTData_Type.__name__ = "AsciiString"
_LpTrLtFbLlchTData_Object = MibTableColumn
lpTrLtFbLlchTData = _LpTrLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 8, 10, 1, 1),
    _LpTrLtFbLlchTData_Type()
)
lpTrLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbLlchTData.setStatus("mandatory")
_LpTrLtFbAppleH_ObjectIdentity = ObjectIdentity
lpTrLtFbAppleH = _LpTrLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9)
)
_LpTrLtFbAppleHRowStatusTable_Object = MibTable
lpTrLtFbAppleHRowStatusTable = _LpTrLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbAppleHRowStatusTable.setStatus("mandatory")
_LpTrLtFbAppleHRowStatusEntry_Object = MibTableRow
lpTrLtFbAppleHRowStatusEntry = _LpTrLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 1, 1)
)
lpTrLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbAppleHRowStatusEntry.setStatus("mandatory")
_LpTrLtFbAppleHRowStatus_Type = RowStatus
_LpTrLtFbAppleHRowStatus_Object = MibTableColumn
lpTrLtFbAppleHRowStatus = _LpTrLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 1, 1, 1),
    _LpTrLtFbAppleHRowStatus_Type()
)
lpTrLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbAppleHRowStatus.setStatus("mandatory")
_LpTrLtFbAppleHComponentName_Type = DisplayString
_LpTrLtFbAppleHComponentName_Object = MibTableColumn
lpTrLtFbAppleHComponentName = _LpTrLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 1, 1, 2),
    _LpTrLtFbAppleHComponentName_Type()
)
lpTrLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbAppleHComponentName.setStatus("mandatory")
_LpTrLtFbAppleHStorageType_Type = StorageType
_LpTrLtFbAppleHStorageType_Object = MibTableColumn
lpTrLtFbAppleHStorageType = _LpTrLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 1, 1, 4),
    _LpTrLtFbAppleHStorageType_Type()
)
lpTrLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbAppleHStorageType.setStatus("mandatory")
_LpTrLtFbAppleHIndex_Type = NonReplicated
_LpTrLtFbAppleHIndex_Object = MibTableColumn
lpTrLtFbAppleHIndex = _LpTrLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 1, 1, 10),
    _LpTrLtFbAppleHIndex_Type()
)
lpTrLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbAppleHIndex.setStatus("mandatory")
_LpTrLtFbAppleHTopTable_Object = MibTable
lpTrLtFbAppleHTopTable = _LpTrLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbAppleHTopTable.setStatus("mandatory")
_LpTrLtFbAppleHTopEntry_Object = MibTableRow
lpTrLtFbAppleHTopEntry = _LpTrLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 10, 1)
)
lpTrLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbAppleHTopEntry.setStatus("mandatory")


class _LpTrLtFbAppleHTData_Type(AsciiString):
    """Custom type lpTrLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbAppleHTData_Type.__name__ = "AsciiString"
_LpTrLtFbAppleHTData_Object = MibTableColumn
lpTrLtFbAppleHTData = _LpTrLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 9, 10, 1, 1),
    _LpTrLtFbAppleHTData_Type()
)
lpTrLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbAppleHTData.setStatus("mandatory")
_LpTrLtFbIpxH_ObjectIdentity = ObjectIdentity
lpTrLtFbIpxH = _LpTrLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10)
)
_LpTrLtFbIpxHRowStatusTable_Object = MibTable
lpTrLtFbIpxHRowStatusTable = _LpTrLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    lpTrLtFbIpxHRowStatusTable.setStatus("mandatory")
_LpTrLtFbIpxHRowStatusEntry_Object = MibTableRow
lpTrLtFbIpxHRowStatusEntry = _LpTrLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 1, 1)
)
lpTrLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbIpxHRowStatusEntry.setStatus("mandatory")
_LpTrLtFbIpxHRowStatus_Type = RowStatus
_LpTrLtFbIpxHRowStatus_Object = MibTableColumn
lpTrLtFbIpxHRowStatus = _LpTrLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 1, 1, 1),
    _LpTrLtFbIpxHRowStatus_Type()
)
lpTrLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbIpxHRowStatus.setStatus("mandatory")
_LpTrLtFbIpxHComponentName_Type = DisplayString
_LpTrLtFbIpxHComponentName_Object = MibTableColumn
lpTrLtFbIpxHComponentName = _LpTrLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 1, 1, 2),
    _LpTrLtFbIpxHComponentName_Type()
)
lpTrLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbIpxHComponentName.setStatus("mandatory")
_LpTrLtFbIpxHStorageType_Type = StorageType
_LpTrLtFbIpxHStorageType_Object = MibTableColumn
lpTrLtFbIpxHStorageType = _LpTrLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 1, 1, 4),
    _LpTrLtFbIpxHStorageType_Type()
)
lpTrLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtFbIpxHStorageType.setStatus("mandatory")
_LpTrLtFbIpxHIndex_Type = NonReplicated
_LpTrLtFbIpxHIndex_Object = MibTableColumn
lpTrLtFbIpxHIndex = _LpTrLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 1, 1, 10),
    _LpTrLtFbIpxHIndex_Type()
)
lpTrLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtFbIpxHIndex.setStatus("mandatory")
_LpTrLtFbIpxHTopTable_Object = MibTable
lpTrLtFbIpxHTopTable = _LpTrLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    lpTrLtFbIpxHTopTable.setStatus("mandatory")
_LpTrLtFbIpxHTopEntry_Object = MibTableRow
lpTrLtFbIpxHTopEntry = _LpTrLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 10, 1)
)
lpTrLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbIpxHTopEntry.setStatus("mandatory")


class _LpTrLtFbIpxHTData_Type(AsciiString):
    """Custom type lpTrLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbIpxHTData_Type.__name__ = "AsciiString"
_LpTrLtFbIpxHTData_Object = MibTableColumn
lpTrLtFbIpxHTData = _LpTrLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 10, 10, 1, 1),
    _LpTrLtFbIpxHTData_Type()
)
lpTrLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbIpxHTData.setStatus("mandatory")
_LpTrLtFbTopTable_Object = MibTable
lpTrLtFbTopTable = _LpTrLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 20)
)
if mibBuilder.loadTexts:
    lpTrLtFbTopTable.setStatus("mandatory")
_LpTrLtFbTopEntry_Object = MibTableRow
lpTrLtFbTopEntry = _LpTrLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 20, 1)
)
lpTrLtFbTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtFbTopEntry.setStatus("mandatory")


class _LpTrLtFbTData_Type(AsciiString):
    """Custom type lpTrLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtFbTData_Type.__name__ = "AsciiString"
_LpTrLtFbTData_Object = MibTableColumn
lpTrLtFbTData = _LpTrLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 5, 20, 1, 1),
    _LpTrLtFbTData_Type()
)
lpTrLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtFbTData.setStatus("mandatory")
_LpTrLtCntl_ObjectIdentity = ObjectIdentity
lpTrLtCntl = _LpTrLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6)
)
_LpTrLtCntlRowStatusTable_Object = MibTable
lpTrLtCntlRowStatusTable = _LpTrLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 1)
)
if mibBuilder.loadTexts:
    lpTrLtCntlRowStatusTable.setStatus("mandatory")
_LpTrLtCntlRowStatusEntry_Object = MibTableRow
lpTrLtCntlRowStatusEntry = _LpTrLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 1, 1)
)
lpTrLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtCntlRowStatusEntry.setStatus("mandatory")
_LpTrLtCntlRowStatus_Type = RowStatus
_LpTrLtCntlRowStatus_Object = MibTableColumn
lpTrLtCntlRowStatus = _LpTrLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 1, 1, 1),
    _LpTrLtCntlRowStatus_Type()
)
lpTrLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtCntlRowStatus.setStatus("mandatory")
_LpTrLtCntlComponentName_Type = DisplayString
_LpTrLtCntlComponentName_Object = MibTableColumn
lpTrLtCntlComponentName = _LpTrLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 1, 1, 2),
    _LpTrLtCntlComponentName_Type()
)
lpTrLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtCntlComponentName.setStatus("mandatory")
_LpTrLtCntlStorageType_Type = StorageType
_LpTrLtCntlStorageType_Object = MibTableColumn
lpTrLtCntlStorageType = _LpTrLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 1, 1, 4),
    _LpTrLtCntlStorageType_Type()
)
lpTrLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLtCntlStorageType.setStatus("mandatory")
_LpTrLtCntlIndex_Type = NonReplicated
_LpTrLtCntlIndex_Object = MibTableColumn
lpTrLtCntlIndex = _LpTrLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 1, 1, 10),
    _LpTrLtCntlIndex_Type()
)
lpTrLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrLtCntlIndex.setStatus("mandatory")
_LpTrLtCntlTopTable_Object = MibTable
lpTrLtCntlTopTable = _LpTrLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 10)
)
if mibBuilder.loadTexts:
    lpTrLtCntlTopTable.setStatus("mandatory")
_LpTrLtCntlTopEntry_Object = MibTableRow
lpTrLtCntlTopEntry = _LpTrLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 10, 1)
)
lpTrLtCntlTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtCntlTopEntry.setStatus("mandatory")


class _LpTrLtCntlTData_Type(AsciiString):
    """Custom type lpTrLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtCntlTData_Type.__name__ = "AsciiString"
_LpTrLtCntlTData_Object = MibTableColumn
lpTrLtCntlTData = _LpTrLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 6, 10, 1, 1),
    _LpTrLtCntlTData_Type()
)
lpTrLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtCntlTData.setStatus("mandatory")
_LpTrLtTopTable_Object = MibTable
lpTrLtTopTable = _LpTrLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 20)
)
if mibBuilder.loadTexts:
    lpTrLtTopTable.setStatus("mandatory")
_LpTrLtTopEntry_Object = MibTableRow
lpTrLtTopEntry = _LpTrLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 20, 1)
)
lpTrLtTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrLtIndex"),
)
if mibBuilder.loadTexts:
    lpTrLtTopEntry.setStatus("mandatory")


class _LpTrLtTData_Type(AsciiString):
    """Custom type lpTrLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpTrLtTData_Type.__name__ = "AsciiString"
_LpTrLtTData_Object = MibTableColumn
lpTrLtTData = _LpTrLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 2, 20, 1, 1),
    _LpTrLtTData_Type()
)
lpTrLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrLtTData.setStatus("mandatory")
_LpTrTest_ObjectIdentity = ObjectIdentity
lpTrTest = _LpTrTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5)
)
_LpTrTestRowStatusTable_Object = MibTable
lpTrTestRowStatusTable = _LpTrTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 1)
)
if mibBuilder.loadTexts:
    lpTrTestRowStatusTable.setStatus("mandatory")
_LpTrTestRowStatusEntry_Object = MibTableRow
lpTrTestRowStatusEntry = _LpTrTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 1, 1)
)
lpTrTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrTestIndex"),
)
if mibBuilder.loadTexts:
    lpTrTestRowStatusEntry.setStatus("mandatory")
_LpTrTestRowStatus_Type = RowStatus
_LpTrTestRowStatus_Object = MibTableColumn
lpTrTestRowStatus = _LpTrTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 1, 1, 1),
    _LpTrTestRowStatus_Type()
)
lpTrTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestRowStatus.setStatus("mandatory")
_LpTrTestComponentName_Type = DisplayString
_LpTrTestComponentName_Object = MibTableColumn
lpTrTestComponentName = _LpTrTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 1, 1, 2),
    _LpTrTestComponentName_Type()
)
lpTrTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestComponentName.setStatus("mandatory")
_LpTrTestStorageType_Type = StorageType
_LpTrTestStorageType_Object = MibTableColumn
lpTrTestStorageType = _LpTrTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 1, 1, 4),
    _LpTrTestStorageType_Type()
)
lpTrTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestStorageType.setStatus("mandatory")
_LpTrTestIndex_Type = NonReplicated
_LpTrTestIndex_Object = MibTableColumn
lpTrTestIndex = _LpTrTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 1, 1, 10),
    _LpTrTestIndex_Type()
)
lpTrTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpTrTestIndex.setStatus("mandatory")
_LpTrTestPTOTable_Object = MibTable
lpTrTestPTOTable = _LpTrTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 10)
)
if mibBuilder.loadTexts:
    lpTrTestPTOTable.setStatus("mandatory")
_LpTrTestPTOEntry_Object = MibTableRow
lpTrTestPTOEntry = _LpTrTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 10, 1)
)
lpTrTestPTOEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrTestIndex"),
)
if mibBuilder.loadTexts:
    lpTrTestPTOEntry.setStatus("mandatory")


class _LpTrTestType_Type(Integer32):
    """Custom type lpTrTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              257,
              258,
              259,
              260,
              263,
              264,
              265,
              266,
              267,
              268)
        )
    )
    namedValues = NamedValues(
        *(("extThruA", 265),
          ("extThruB", 266),
          ("extWrapA", 263),
          ("extWrapAB", 267),
          ("extWrapB", 264),
          ("extWrapBA", 268),
          ("normal", 1),
          ("onCard", 0),
          ("thruA", 259),
          ("thruB", 260),
          ("wrapA", 257),
          ("wrapB", 258))
    )


_LpTrTestType_Type.__name__ = "Integer32"
_LpTrTestType_Object = MibTableColumn
lpTrTestType = _LpTrTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 10, 1, 1),
    _LpTrTestType_Type()
)
lpTrTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrTestType.setStatus("mandatory")


class _LpTrTestFrmSize_Type(Unsigned32):
    """Custom type lpTrTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpTrTestFrmSize_Type.__name__ = "Unsigned32"
_LpTrTestFrmSize_Object = MibTableColumn
lpTrTestFrmSize = _LpTrTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 10, 1, 2),
    _LpTrTestFrmSize_Type()
)
lpTrTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrTestFrmSize.setStatus("mandatory")


class _LpTrTestDuration_Type(Unsigned32):
    """Custom type lpTrTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpTrTestDuration_Type.__name__ = "Unsigned32"
_LpTrTestDuration_Object = MibTableColumn
lpTrTestDuration = _LpTrTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 10, 1, 3),
    _LpTrTestDuration_Type()
)
lpTrTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrTestDuration.setStatus("mandatory")
_LpTrTestResultsTable_Object = MibTable
lpTrTestResultsTable = _LpTrTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11)
)
if mibBuilder.loadTexts:
    lpTrTestResultsTable.setStatus("mandatory")
_LpTrTestResultsEntry_Object = MibTableRow
lpTrTestResultsEntry = _LpTrTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1)
)
lpTrTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrTestIndex"),
)
if mibBuilder.loadTexts:
    lpTrTestResultsEntry.setStatus("mandatory")
_LpTrTestElapsedTime_Type = Counter32
_LpTrTestElapsedTime_Object = MibTableColumn
lpTrTestElapsedTime = _LpTrTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 4),
    _LpTrTestElapsedTime_Type()
)
lpTrTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestElapsedTime.setStatus("mandatory")


class _LpTrTestTimeRemaining_Type(Unsigned32):
    """Custom type lpTrTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpTrTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpTrTestTimeRemaining_Object = MibTableColumn
lpTrTestTimeRemaining = _LpTrTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 5),
    _LpTrTestTimeRemaining_Type()
)
lpTrTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestTimeRemaining.setStatus("mandatory")


class _LpTrTestCauseOfTermination_Type(Integer32):
    """Custom type lpTrTestCauseOfTermination based on Integer32"""
    defaultValue = 3

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
        *(("neverStarted", 3),
          ("stoppedByOperator", 1),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_LpTrTestCauseOfTermination_Type.__name__ = "Integer32"
_LpTrTestCauseOfTermination_Object = MibTableColumn
lpTrTestCauseOfTermination = _LpTrTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 6),
    _LpTrTestCauseOfTermination_Type()
)
lpTrTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestCauseOfTermination.setStatus("mandatory")
_LpTrTestFrmTx_Type = PassportCounter64
_LpTrTestFrmTx_Object = MibTableColumn
lpTrTestFrmTx = _LpTrTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 7),
    _LpTrTestFrmTx_Type()
)
lpTrTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestFrmTx.setStatus("mandatory")
_LpTrTestBitsTx_Type = PassportCounter64
_LpTrTestBitsTx_Object = MibTableColumn
lpTrTestBitsTx = _LpTrTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 8),
    _LpTrTestBitsTx_Type()
)
lpTrTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestBitsTx.setStatus("mandatory")
_LpTrTestFrmRx_Type = PassportCounter64
_LpTrTestFrmRx_Object = MibTableColumn
lpTrTestFrmRx = _LpTrTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 9),
    _LpTrTestFrmRx_Type()
)
lpTrTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestFrmRx.setStatus("mandatory")
_LpTrTestBitsRx_Type = PassportCounter64
_LpTrTestBitsRx_Object = MibTableColumn
lpTrTestBitsRx = _LpTrTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 10),
    _LpTrTestBitsRx_Type()
)
lpTrTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestBitsRx.setStatus("mandatory")
_LpTrTestErroredFrmRx_Type = PassportCounter64
_LpTrTestErroredFrmRx_Object = MibTableColumn
lpTrTestErroredFrmRx = _LpTrTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 5, 11, 1, 11),
    _LpTrTestErroredFrmRx_Type()
)
lpTrTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTestErroredFrmRx.setStatus("mandatory")
_LpTrCidDataTable_Object = MibTable
lpTrCidDataTable = _LpTrCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 10)
)
if mibBuilder.loadTexts:
    lpTrCidDataTable.setStatus("mandatory")
_LpTrCidDataEntry_Object = MibTableRow
lpTrCidDataEntry = _LpTrCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 10, 1)
)
lpTrCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrCidDataEntry.setStatus("mandatory")


class _LpTrCustomerIdentifier_Type(Unsigned32):
    """Custom type lpTrCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpTrCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpTrCustomerIdentifier_Object = MibTableColumn
lpTrCustomerIdentifier = _LpTrCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 10, 1, 1),
    _LpTrCustomerIdentifier_Type()
)
lpTrCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrCustomerIdentifier.setStatus("mandatory")
_LpTrIfEntryTable_Object = MibTable
lpTrIfEntryTable = _LpTrIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 11)
)
if mibBuilder.loadTexts:
    lpTrIfEntryTable.setStatus("mandatory")
_LpTrIfEntryEntry_Object = MibTableRow
lpTrIfEntryEntry = _LpTrIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 11, 1)
)
lpTrIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrIfEntryEntry.setStatus("mandatory")


class _LpTrIfAdminStatus_Type(Integer32):
    """Custom type lpTrIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpTrIfAdminStatus_Type.__name__ = "Integer32"
_LpTrIfAdminStatus_Object = MibTableColumn
lpTrIfAdminStatus = _LpTrIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 11, 1, 1),
    _LpTrIfAdminStatus_Type()
)
lpTrIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrIfAdminStatus.setStatus("mandatory")


class _LpTrIfIndex_Type(InterfaceIndex):
    """Custom type lpTrIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpTrIfIndex_Type.__name__ = "InterfaceIndex"
_LpTrIfIndex_Object = MibTableColumn
lpTrIfIndex = _LpTrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 11, 1, 2),
    _LpTrIfIndex_Type()
)
lpTrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrIfIndex.setStatus("mandatory")
_LpTrProvTable_Object = MibTable
lpTrProvTable = _LpTrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12)
)
if mibBuilder.loadTexts:
    lpTrProvTable.setStatus("mandatory")
_LpTrProvEntry_Object = MibTableRow
lpTrProvEntry = _LpTrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1)
)
lpTrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrProvEntry.setStatus("mandatory")


class _LpTrRingSpeed_Type(Integer32):
    """Custom type lpTrRingSpeed based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 3),
          ("sixteenMegabit", 4))
    )


_LpTrRingSpeed_Type.__name__ = "Integer32"
_LpTrRingSpeed_Object = MibTableColumn
lpTrRingSpeed = _LpTrRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1, 1),
    _LpTrRingSpeed_Type()
)
lpTrRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrRingSpeed.setStatus("mandatory")


class _LpTrMonitorParticipate_Type(Integer32):
    """Custom type lpTrMonitorParticipate based on Integer32"""
    defaultValue = 2

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


_LpTrMonitorParticipate_Type.__name__ = "Integer32"
_LpTrMonitorParticipate_Object = MibTableColumn
lpTrMonitorParticipate = _LpTrMonitorParticipate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1, 2),
    _LpTrMonitorParticipate_Type()
)
lpTrMonitorParticipate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrMonitorParticipate.setStatus("mandatory")


class _LpTrFunctionalAddress_Type(MacAddress):
    """Custom type lpTrFunctionalAddress based on MacAddress"""
    defaultHexValue = "0300feff8f01"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpTrFunctionalAddress_Type.__name__ = "MacAddress"
_LpTrFunctionalAddress_Object = MibTableColumn
lpTrFunctionalAddress = _LpTrFunctionalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1, 3),
    _LpTrFunctionalAddress_Type()
)
lpTrFunctionalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrFunctionalAddress.setStatus("mandatory")


class _LpTrNodeAddress_Type(MacAddress):
    """Custom type lpTrNodeAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpTrNodeAddress_Type.__name__ = "MacAddress"
_LpTrNodeAddress_Object = MibTableColumn
lpTrNodeAddress = _LpTrNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1, 4),
    _LpTrNodeAddress_Type()
)
lpTrNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrNodeAddress.setStatus("mandatory")


class _LpTrGroupAddress_Type(MacAddress):
    """Custom type lpTrGroupAddress based on MacAddress"""
    defaultHexValue = "030001000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpTrGroupAddress_Type.__name__ = "MacAddress"
_LpTrGroupAddress_Object = MibTableColumn
lpTrGroupAddress = _LpTrGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1, 5),
    _LpTrGroupAddress_Type()
)
lpTrGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrGroupAddress.setStatus("mandatory")


class _LpTrProductId_Type(AsciiString):
    """Custom type lpTrProductId based on AsciiString"""
    defaultHexValue = "4c414e20546f6b656e2052696e67"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_LpTrProductId_Type.__name__ = "AsciiString"
_LpTrProductId_Object = MibTableColumn
lpTrProductId = _LpTrProductId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1, 6),
    _LpTrProductId_Type()
)
lpTrProductId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrProductId.setStatus("mandatory")
_LpTrApplicationFramerName_Type = Link
_LpTrApplicationFramerName_Object = MibTableColumn
lpTrApplicationFramerName = _LpTrApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 12, 1, 7),
    _LpTrApplicationFramerName_Type()
)
lpTrApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrApplicationFramerName.setStatus("mandatory")
_LpTrAdminInfoTable_Object = MibTable
lpTrAdminInfoTable = _LpTrAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 13)
)
if mibBuilder.loadTexts:
    lpTrAdminInfoTable.setStatus("mandatory")
_LpTrAdminInfoEntry_Object = MibTableRow
lpTrAdminInfoEntry = _LpTrAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 13, 1)
)
lpTrAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrAdminInfoEntry.setStatus("mandatory")


class _LpTrVendor_Type(AsciiString):
    """Custom type lpTrVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpTrVendor_Type.__name__ = "AsciiString"
_LpTrVendor_Object = MibTableColumn
lpTrVendor = _LpTrVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 13, 1, 1),
    _LpTrVendor_Type()
)
lpTrVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrVendor.setStatus("mandatory")


class _LpTrCommentText_Type(AsciiString):
    """Custom type lpTrCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpTrCommentText_Type.__name__ = "AsciiString"
_LpTrCommentText_Object = MibTableColumn
lpTrCommentText = _LpTrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 13, 1, 2),
    _LpTrCommentText_Type()
)
lpTrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpTrCommentText.setStatus("mandatory")
_LpTrStateTable_Object = MibTable
lpTrStateTable = _LpTrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 15)
)
if mibBuilder.loadTexts:
    lpTrStateTable.setStatus("mandatory")
_LpTrStateEntry_Object = MibTableRow
lpTrStateEntry = _LpTrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 15, 1)
)
lpTrStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrStateEntry.setStatus("mandatory")


class _LpTrAdminState_Type(Integer32):
    """Custom type lpTrAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_LpTrAdminState_Type.__name__ = "Integer32"
_LpTrAdminState_Object = MibTableColumn
lpTrAdminState = _LpTrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 15, 1, 1),
    _LpTrAdminState_Type()
)
lpTrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrAdminState.setStatus("mandatory")


class _LpTrOperationalState_Type(Integer32):
    """Custom type lpTrOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LpTrOperationalState_Type.__name__ = "Integer32"
_LpTrOperationalState_Object = MibTableColumn
lpTrOperationalState = _LpTrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 15, 1, 2),
    _LpTrOperationalState_Type()
)
lpTrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrOperationalState.setStatus("mandatory")


class _LpTrUsageState_Type(Integer32):
    """Custom type lpTrUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_LpTrUsageState_Type.__name__ = "Integer32"
_LpTrUsageState_Object = MibTableColumn
lpTrUsageState = _LpTrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 15, 1, 3),
    _LpTrUsageState_Type()
)
lpTrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrUsageState.setStatus("mandatory")
_LpTrOperStatusTable_Object = MibTable
lpTrOperStatusTable = _LpTrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 16)
)
if mibBuilder.loadTexts:
    lpTrOperStatusTable.setStatus("mandatory")
_LpTrOperStatusEntry_Object = MibTableRow
lpTrOperStatusEntry = _LpTrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 16, 1)
)
lpTrOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrOperStatusEntry.setStatus("mandatory")


class _LpTrSnmpOperStatus_Type(Integer32):
    """Custom type lpTrSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpTrSnmpOperStatus_Type.__name__ = "Integer32"
_LpTrSnmpOperStatus_Object = MibTableColumn
lpTrSnmpOperStatus = _LpTrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 16, 1, 1),
    _LpTrSnmpOperStatus_Type()
)
lpTrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrSnmpOperStatus.setStatus("mandatory")
_LpTrOperTable_Object = MibTable
lpTrOperTable = _LpTrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17)
)
if mibBuilder.loadTexts:
    lpTrOperTable.setStatus("mandatory")
_LpTrOperEntry_Object = MibTableRow
lpTrOperEntry = _LpTrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1)
)
lpTrOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrOperEntry.setStatus("mandatory")


class _LpTrMacAddress_Type(MacAddress):
    """Custom type lpTrMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpTrMacAddress_Type.__name__ = "MacAddress"
_LpTrMacAddress_Object = MibTableColumn
lpTrMacAddress = _LpTrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1, 2),
    _LpTrMacAddress_Type()
)
lpTrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrMacAddress.setStatus("mandatory")


class _LpTrRingState_Type(Integer32):
    """Custom type lpTrRingState based on Integer32"""
    defaultValue = 6

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
        *(("closed", 2),
          ("closing", 4),
          ("openFailure", 5),
          ("opened", 1),
          ("opening", 3),
          ("ringFailure", 6))
    )


_LpTrRingState_Type.__name__ = "Integer32"
_LpTrRingState_Object = MibTableColumn
lpTrRingState = _LpTrRingState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1, 4),
    _LpTrRingState_Type()
)
lpTrRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrRingState.setStatus("mandatory")


class _LpTrRingStatus_Type(OctetString):
    """Custom type lpTrRingStatus based on OctetString"""
    defaultHexValue = "000040"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LpTrRingStatus_Type.__name__ = "OctetString"
_LpTrRingStatus_Object = MibTableColumn
lpTrRingStatus = _LpTrRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1, 5),
    _LpTrRingStatus_Type()
)
lpTrRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrRingStatus.setStatus("mandatory")


class _LpTrRingOpenStatus_Type(Integer32):
    """Custom type lpTrRingOpenStatus based on Integer32"""
    defaultValue = 1

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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("badParam", 2),
          ("beaconing", 7),
          ("duplicateMac", 8),
          ("insertionTimeout", 5),
          ("lobeFailed", 3),
          ("noOpen", 1),
          ("open", 11),
          ("removeReceived", 10),
          ("requestFailed", 9),
          ("ringFailed", 6),
          ("signalLoss", 4))
    )


_LpTrRingOpenStatus_Type.__name__ = "Integer32"
_LpTrRingOpenStatus_Object = MibTableColumn
lpTrRingOpenStatus = _LpTrRingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1, 6),
    _LpTrRingOpenStatus_Type()
)
lpTrRingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrRingOpenStatus.setStatus("mandatory")


class _LpTrUpStream_Type(MacAddress):
    """Custom type lpTrUpStream based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpTrUpStream_Type.__name__ = "MacAddress"
_LpTrUpStream_Object = MibTableColumn
lpTrUpStream = _LpTrUpStream_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1, 7),
    _LpTrUpStream_Type()
)
lpTrUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrUpStream.setStatus("mandatory")


class _LpTrChipSet_Type(Integer32):
    """Custom type lpTrChipSet based on Integer32"""
    defaultValue = 3

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
        *(("ibm16", 1),
          ("titms380", 2),
          ("titms380c16", 3),
          ("titms380c26", 4))
    )


_LpTrChipSet_Type.__name__ = "Integer32"
_LpTrChipSet_Object = MibTableColumn
lpTrChipSet = _LpTrChipSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1, 9),
    _LpTrChipSet_Type()
)
lpTrChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrChipSet.setStatus("mandatory")


class _LpTrLastTimeBeaconSent_Type(EnterpriseDateAndTime):
    """Custom type lpTrLastTimeBeaconSent based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_LpTrLastTimeBeaconSent_Type.__name__ = "EnterpriseDateAndTime"
_LpTrLastTimeBeaconSent_Object = MibTableColumn
lpTrLastTimeBeaconSent = _LpTrLastTimeBeaconSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 17, 1, 10),
    _LpTrLastTimeBeaconSent_Type()
)
lpTrLastTimeBeaconSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLastTimeBeaconSent.setStatus("mandatory")
_LpTrStatsTable_Object = MibTable
lpTrStatsTable = _LpTrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18)
)
if mibBuilder.loadTexts:
    lpTrStatsTable.setStatus("mandatory")
_LpTrStatsEntry_Object = MibTableRow
lpTrStatsEntry = _LpTrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1)
)
lpTrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrStatsEntry.setStatus("mandatory")
_LpTrLineErrors_Type = Counter32
_LpTrLineErrors_Object = MibTableColumn
lpTrLineErrors = _LpTrLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 2),
    _LpTrLineErrors_Type()
)
lpTrLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLineErrors.setStatus("mandatory")
_LpTrBurstErrors_Type = Counter32
_LpTrBurstErrors_Object = MibTableColumn
lpTrBurstErrors = _LpTrBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 3),
    _LpTrBurstErrors_Type()
)
lpTrBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrBurstErrors.setStatus("mandatory")
_LpTrAcErrors_Type = Counter32
_LpTrAcErrors_Object = MibTableColumn
lpTrAcErrors = _LpTrAcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 4),
    _LpTrAcErrors_Type()
)
lpTrAcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrAcErrors.setStatus("mandatory")
_LpTrAbortTransErrors_Type = Counter32
_LpTrAbortTransErrors_Object = MibTableColumn
lpTrAbortTransErrors = _LpTrAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 5),
    _LpTrAbortTransErrors_Type()
)
lpTrAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrAbortTransErrors.setStatus("mandatory")
_LpTrInternalErrors_Type = Counter32
_LpTrInternalErrors_Object = MibTableColumn
lpTrInternalErrors = _LpTrInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 6),
    _LpTrInternalErrors_Type()
)
lpTrInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrInternalErrors.setStatus("mandatory")
_LpTrLostFrameErrors_Type = Counter32
_LpTrLostFrameErrors_Object = MibTableColumn
lpTrLostFrameErrors = _LpTrLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 7),
    _LpTrLostFrameErrors_Type()
)
lpTrLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLostFrameErrors.setStatus("mandatory")
_LpTrReceiveCongestions_Type = Counter32
_LpTrReceiveCongestions_Object = MibTableColumn
lpTrReceiveCongestions = _LpTrReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 8),
    _LpTrReceiveCongestions_Type()
)
lpTrReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrReceiveCongestions.setStatus("mandatory")
_LpTrFrameCopiedErrors_Type = Counter32
_LpTrFrameCopiedErrors_Object = MibTableColumn
lpTrFrameCopiedErrors = _LpTrFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 9),
    _LpTrFrameCopiedErrors_Type()
)
lpTrFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrFrameCopiedErrors.setStatus("mandatory")
_LpTrTokenErrors_Type = Counter32
_LpTrTokenErrors_Object = MibTableColumn
lpTrTokenErrors = _LpTrTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 10),
    _LpTrTokenErrors_Type()
)
lpTrTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTokenErrors.setStatus("mandatory")
_LpTrSoftErrors_Type = Counter32
_LpTrSoftErrors_Object = MibTableColumn
lpTrSoftErrors = _LpTrSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 11),
    _LpTrSoftErrors_Type()
)
lpTrSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrSoftErrors.setStatus("mandatory")
_LpTrHardErrors_Type = Counter32
_LpTrHardErrors_Object = MibTableColumn
lpTrHardErrors = _LpTrHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 12),
    _LpTrHardErrors_Type()
)
lpTrHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrHardErrors.setStatus("mandatory")
_LpTrSignalLoss_Type = Counter32
_LpTrSignalLoss_Object = MibTableColumn
lpTrSignalLoss = _LpTrSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 13),
    _LpTrSignalLoss_Type()
)
lpTrSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrSignalLoss.setStatus("mandatory")
_LpTrTransmitBeacons_Type = Counter32
_LpTrTransmitBeacons_Object = MibTableColumn
lpTrTransmitBeacons = _LpTrTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 14),
    _LpTrTransmitBeacons_Type()
)
lpTrTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrTransmitBeacons.setStatus("mandatory")
_LpTrRingRecoverys_Type = Counter32
_LpTrRingRecoverys_Object = MibTableColumn
lpTrRingRecoverys = _LpTrRingRecoverys_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 15),
    _LpTrRingRecoverys_Type()
)
lpTrRingRecoverys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrRingRecoverys.setStatus("mandatory")
_LpTrLobeWires_Type = Counter32
_LpTrLobeWires_Object = MibTableColumn
lpTrLobeWires = _LpTrLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 16),
    _LpTrLobeWires_Type()
)
lpTrLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrLobeWires.setStatus("mandatory")
_LpTrRemoveRings_Type = Counter32
_LpTrRemoveRings_Object = MibTableColumn
lpTrRemoveRings = _LpTrRemoveRings_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 17),
    _LpTrRemoveRings_Type()
)
lpTrRemoveRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrRemoveRings.setStatus("mandatory")
_LpTrSingleStation_Type = Counter32
_LpTrSingleStation_Object = MibTableColumn
lpTrSingleStation = _LpTrSingleStation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 18),
    _LpTrSingleStation_Type()
)
lpTrSingleStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrSingleStation.setStatus("mandatory")
_LpTrFreqErrors_Type = Counter32
_LpTrFreqErrors_Object = MibTableColumn
lpTrFreqErrors = _LpTrFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 18, 1, 19),
    _LpTrFreqErrors_Type()
)
lpTrFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrFreqErrors.setStatus("mandatory")
_LpTrNcMacOperTable_Object = MibTable
lpTrNcMacOperTable = _LpTrNcMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 20)
)
if mibBuilder.loadTexts:
    lpTrNcMacOperTable.setStatus("mandatory")
_LpTrNcMacOperEntry_Object = MibTableRow
lpTrNcMacOperEntry = _LpTrNcMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 20, 1)
)
lpTrNcMacOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpTrIndex"),
)
if mibBuilder.loadTexts:
    lpTrNcMacOperEntry.setStatus("mandatory")


class _LpTrNcMacAddress_Type(MacAddress):
    """Custom type lpTrNcMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpTrNcMacAddress_Type.__name__ = "MacAddress"
_LpTrNcMacAddress_Object = MibTableColumn
lpTrNcMacAddress = _LpTrNcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 20, 1, 1),
    _LpTrNcMacAddress_Type()
)
lpTrNcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrNcMacAddress.setStatus("mandatory")


class _LpTrNcUpStream_Type(MacAddress):
    """Custom type lpTrNcUpStream based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpTrNcUpStream_Type.__name__ = "MacAddress"
_LpTrNcUpStream_Object = MibTableColumn
lpTrNcUpStream = _LpTrNcUpStream_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 13, 20, 1, 2),
    _LpTrNcUpStream_Type()
)
lpTrNcUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTrNcUpStream.setStatus("mandatory")
_LpIlsFwdr_ObjectIdentity = ObjectIdentity
lpIlsFwdr = _LpIlsFwdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21)
)
_LpIlsFwdrRowStatusTable_Object = MibTable
lpIlsFwdrRowStatusTable = _LpIlsFwdrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrRowStatusTable.setStatus("mandatory")
_LpIlsFwdrRowStatusEntry_Object = MibTableRow
lpIlsFwdrRowStatusEntry = _LpIlsFwdrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 1, 1)
)
lpIlsFwdrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrRowStatus_Type = RowStatus
_LpIlsFwdrRowStatus_Object = MibTableColumn
lpIlsFwdrRowStatus = _LpIlsFwdrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 1, 1, 1),
    _LpIlsFwdrRowStatus_Type()
)
lpIlsFwdrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrRowStatus.setStatus("mandatory")
_LpIlsFwdrComponentName_Type = DisplayString
_LpIlsFwdrComponentName_Object = MibTableColumn
lpIlsFwdrComponentName = _LpIlsFwdrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 1, 1, 2),
    _LpIlsFwdrComponentName_Type()
)
lpIlsFwdrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrComponentName.setStatus("mandatory")
_LpIlsFwdrStorageType_Type = StorageType
_LpIlsFwdrStorageType_Object = MibTableColumn
lpIlsFwdrStorageType = _LpIlsFwdrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 1, 1, 4),
    _LpIlsFwdrStorageType_Type()
)
lpIlsFwdrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrStorageType.setStatus("mandatory")


class _LpIlsFwdrIndex_Type(Integer32):
    """Custom type lpIlsFwdrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LpIlsFwdrIndex_Type.__name__ = "Integer32"
_LpIlsFwdrIndex_Object = MibTableColumn
lpIlsFwdrIndex = _LpIlsFwdrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 1, 1, 10),
    _LpIlsFwdrIndex_Type()
)
lpIlsFwdrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrIndex.setStatus("mandatory")
_LpIlsFwdrLt_ObjectIdentity = ObjectIdentity
lpIlsFwdrLt = _LpIlsFwdrLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2)
)
_LpIlsFwdrLtRowStatusTable_Object = MibTable
lpIlsFwdrLtRowStatusTable = _LpIlsFwdrLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtRowStatusEntry = _LpIlsFwdrLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 1, 1)
)
lpIlsFwdrLtRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtRowStatus_Type = RowStatus
_LpIlsFwdrLtRowStatus_Object = MibTableColumn
lpIlsFwdrLtRowStatus = _LpIlsFwdrLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 1, 1, 1),
    _LpIlsFwdrLtRowStatus_Type()
)
lpIlsFwdrLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtRowStatus.setStatus("mandatory")
_LpIlsFwdrLtComponentName_Type = DisplayString
_LpIlsFwdrLtComponentName_Object = MibTableColumn
lpIlsFwdrLtComponentName = _LpIlsFwdrLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 1, 1, 2),
    _LpIlsFwdrLtComponentName_Type()
)
lpIlsFwdrLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtComponentName.setStatus("mandatory")
_LpIlsFwdrLtStorageType_Type = StorageType
_LpIlsFwdrLtStorageType_Object = MibTableColumn
lpIlsFwdrLtStorageType = _LpIlsFwdrLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 1, 1, 4),
    _LpIlsFwdrLtStorageType_Type()
)
lpIlsFwdrLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtStorageType.setStatus("mandatory")
_LpIlsFwdrLtIndex_Type = NonReplicated
_LpIlsFwdrLtIndex_Object = MibTableColumn
lpIlsFwdrLtIndex = _LpIlsFwdrLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 1, 1, 10),
    _LpIlsFwdrLtIndex_Type()
)
lpIlsFwdrLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtIndex.setStatus("mandatory")
_LpIlsFwdrLtFrmCmp_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFrmCmp = _LpIlsFwdrLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2)
)
_LpIlsFwdrLtFrmCmpRowStatusTable_Object = MibTable
lpIlsFwdrLtFrmCmpRowStatusTable = _LpIlsFwdrLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFrmCmpRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFrmCmpRowStatusEntry = _LpIlsFwdrLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 1, 1)
)
lpIlsFwdrLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFrmCmpRowStatus_Type = RowStatus
_LpIlsFwdrLtFrmCmpRowStatus_Object = MibTableColumn
lpIlsFwdrLtFrmCmpRowStatus = _LpIlsFwdrLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 1, 1, 1),
    _LpIlsFwdrLtFrmCmpRowStatus_Type()
)
lpIlsFwdrLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFrmCmpComponentName_Type = DisplayString
_LpIlsFwdrLtFrmCmpComponentName_Object = MibTableColumn
lpIlsFwdrLtFrmCmpComponentName = _LpIlsFwdrLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 1, 1, 2),
    _LpIlsFwdrLtFrmCmpComponentName_Type()
)
lpIlsFwdrLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpComponentName.setStatus("mandatory")
_LpIlsFwdrLtFrmCmpStorageType_Type = StorageType
_LpIlsFwdrLtFrmCmpStorageType_Object = MibTableColumn
lpIlsFwdrLtFrmCmpStorageType = _LpIlsFwdrLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 1, 1, 4),
    _LpIlsFwdrLtFrmCmpStorageType_Type()
)
lpIlsFwdrLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpStorageType.setStatus("mandatory")
_LpIlsFwdrLtFrmCmpIndex_Type = NonReplicated
_LpIlsFwdrLtFrmCmpIndex_Object = MibTableColumn
lpIlsFwdrLtFrmCmpIndex = _LpIlsFwdrLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 1, 1, 10),
    _LpIlsFwdrLtFrmCmpIndex_Type()
)
lpIlsFwdrLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpIndex.setStatus("mandatory")
_LpIlsFwdrLtFrmCmpTopTable_Object = MibTable
lpIlsFwdrLtFrmCmpTopTable = _LpIlsFwdrLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpTopTable.setStatus("mandatory")
_LpIlsFwdrLtFrmCmpTopEntry_Object = MibTableRow
lpIlsFwdrLtFrmCmpTopEntry = _LpIlsFwdrLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 10, 1)
)
lpIlsFwdrLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFrmCmpTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFrmCmpTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFrmCmpTData_Object = MibTableColumn
lpIlsFwdrLtFrmCmpTData = _LpIlsFwdrLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 2, 10, 1, 1),
    _LpIlsFwdrLtFrmCmpTData_Type()
)
lpIlsFwdrLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCmpTData.setStatus("mandatory")
_LpIlsFwdrLtFrmCpy_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFrmCpy = _LpIlsFwdrLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3)
)
_LpIlsFwdrLtFrmCpyRowStatusTable_Object = MibTable
lpIlsFwdrLtFrmCpyRowStatusTable = _LpIlsFwdrLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFrmCpyRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFrmCpyRowStatusEntry = _LpIlsFwdrLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 1, 1)
)
lpIlsFwdrLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFrmCpyRowStatus_Type = RowStatus
_LpIlsFwdrLtFrmCpyRowStatus_Object = MibTableColumn
lpIlsFwdrLtFrmCpyRowStatus = _LpIlsFwdrLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 1, 1, 1),
    _LpIlsFwdrLtFrmCpyRowStatus_Type()
)
lpIlsFwdrLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFrmCpyComponentName_Type = DisplayString
_LpIlsFwdrLtFrmCpyComponentName_Object = MibTableColumn
lpIlsFwdrLtFrmCpyComponentName = _LpIlsFwdrLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 1, 1, 2),
    _LpIlsFwdrLtFrmCpyComponentName_Type()
)
lpIlsFwdrLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyComponentName.setStatus("mandatory")
_LpIlsFwdrLtFrmCpyStorageType_Type = StorageType
_LpIlsFwdrLtFrmCpyStorageType_Object = MibTableColumn
lpIlsFwdrLtFrmCpyStorageType = _LpIlsFwdrLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 1, 1, 4),
    _LpIlsFwdrLtFrmCpyStorageType_Type()
)
lpIlsFwdrLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyStorageType.setStatus("mandatory")
_LpIlsFwdrLtFrmCpyIndex_Type = NonReplicated
_LpIlsFwdrLtFrmCpyIndex_Object = MibTableColumn
lpIlsFwdrLtFrmCpyIndex = _LpIlsFwdrLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 1, 1, 10),
    _LpIlsFwdrLtFrmCpyIndex_Type()
)
lpIlsFwdrLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyIndex.setStatus("mandatory")
_LpIlsFwdrLtFrmCpyTopTable_Object = MibTable
lpIlsFwdrLtFrmCpyTopTable = _LpIlsFwdrLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyTopTable.setStatus("mandatory")
_LpIlsFwdrLtFrmCpyTopEntry_Object = MibTableRow
lpIlsFwdrLtFrmCpyTopEntry = _LpIlsFwdrLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 10, 1)
)
lpIlsFwdrLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFrmCpyTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFrmCpyTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFrmCpyTData_Object = MibTableColumn
lpIlsFwdrLtFrmCpyTData = _LpIlsFwdrLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 3, 10, 1, 1),
    _LpIlsFwdrLtFrmCpyTData_Type()
)
lpIlsFwdrLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFrmCpyTData.setStatus("mandatory")
_LpIlsFwdrLtPrtCfg_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtPrtCfg = _LpIlsFwdrLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4)
)
_LpIlsFwdrLtPrtCfgRowStatusTable_Object = MibTable
lpIlsFwdrLtPrtCfgRowStatusTable = _LpIlsFwdrLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtPrtCfgRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtPrtCfgRowStatusEntry = _LpIlsFwdrLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 1, 1)
)
lpIlsFwdrLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtPrtCfgRowStatus_Type = RowStatus
_LpIlsFwdrLtPrtCfgRowStatus_Object = MibTableColumn
lpIlsFwdrLtPrtCfgRowStatus = _LpIlsFwdrLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 1, 1, 1),
    _LpIlsFwdrLtPrtCfgRowStatus_Type()
)
lpIlsFwdrLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgRowStatus.setStatus("mandatory")
_LpIlsFwdrLtPrtCfgComponentName_Type = DisplayString
_LpIlsFwdrLtPrtCfgComponentName_Object = MibTableColumn
lpIlsFwdrLtPrtCfgComponentName = _LpIlsFwdrLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 1, 1, 2),
    _LpIlsFwdrLtPrtCfgComponentName_Type()
)
lpIlsFwdrLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgComponentName.setStatus("mandatory")
_LpIlsFwdrLtPrtCfgStorageType_Type = StorageType
_LpIlsFwdrLtPrtCfgStorageType_Object = MibTableColumn
lpIlsFwdrLtPrtCfgStorageType = _LpIlsFwdrLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 1, 1, 4),
    _LpIlsFwdrLtPrtCfgStorageType_Type()
)
lpIlsFwdrLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgStorageType.setStatus("mandatory")
_LpIlsFwdrLtPrtCfgIndex_Type = NonReplicated
_LpIlsFwdrLtPrtCfgIndex_Object = MibTableColumn
lpIlsFwdrLtPrtCfgIndex = _LpIlsFwdrLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 1, 1, 10),
    _LpIlsFwdrLtPrtCfgIndex_Type()
)
lpIlsFwdrLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgIndex.setStatus("mandatory")
_LpIlsFwdrLtPrtCfgTopTable_Object = MibTable
lpIlsFwdrLtPrtCfgTopTable = _LpIlsFwdrLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgTopTable.setStatus("mandatory")
_LpIlsFwdrLtPrtCfgTopEntry_Object = MibTableRow
lpIlsFwdrLtPrtCfgTopEntry = _LpIlsFwdrLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 10, 1)
)
lpIlsFwdrLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtPrtCfgTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtPrtCfgTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtPrtCfgTData_Object = MibTableColumn
lpIlsFwdrLtPrtCfgTData = _LpIlsFwdrLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 4, 10, 1, 1),
    _LpIlsFwdrLtPrtCfgTData_Type()
)
lpIlsFwdrLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtPrtCfgTData.setStatus("mandatory")
_LpIlsFwdrLtFb_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFb = _LpIlsFwdrLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5)
)
_LpIlsFwdrLtFbRowStatusTable_Object = MibTable
lpIlsFwdrLtFbRowStatusTable = _LpIlsFwdrLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbRowStatusEntry = _LpIlsFwdrLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 1, 1)
)
lpIlsFwdrLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbRowStatus_Type = RowStatus
_LpIlsFwdrLtFbRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbRowStatus = _LpIlsFwdrLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 1, 1, 1),
    _LpIlsFwdrLtFbRowStatus_Type()
)
lpIlsFwdrLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbComponentName_Type = DisplayString
_LpIlsFwdrLtFbComponentName_Object = MibTableColumn
lpIlsFwdrLtFbComponentName = _LpIlsFwdrLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 1, 1, 2),
    _LpIlsFwdrLtFbComponentName_Type()
)
lpIlsFwdrLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbStorageType_Type = StorageType
_LpIlsFwdrLtFbStorageType_Object = MibTableColumn
lpIlsFwdrLtFbStorageType = _LpIlsFwdrLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 1, 1, 4),
    _LpIlsFwdrLtFbStorageType_Type()
)
lpIlsFwdrLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbIndex_Type = NonReplicated
_LpIlsFwdrLtFbIndex_Object = MibTableColumn
lpIlsFwdrLtFbIndex = _LpIlsFwdrLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 1, 1, 10),
    _LpIlsFwdrLtFbIndex_Type()
)
lpIlsFwdrLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIndex.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfo_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbTxInfo = _LpIlsFwdrLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2)
)
_LpIlsFwdrLtFbTxInfoRowStatusTable_Object = MibTable
lpIlsFwdrLtFbTxInfoRowStatusTable = _LpIlsFwdrLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfoRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbTxInfoRowStatusEntry = _LpIlsFwdrLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 1, 1)
)
lpIlsFwdrLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfoRowStatus_Type = RowStatus
_LpIlsFwdrLtFbTxInfoRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbTxInfoRowStatus = _LpIlsFwdrLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 1, 1, 1),
    _LpIlsFwdrLtFbTxInfoRowStatus_Type()
)
lpIlsFwdrLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfoComponentName_Type = DisplayString
_LpIlsFwdrLtFbTxInfoComponentName_Object = MibTableColumn
lpIlsFwdrLtFbTxInfoComponentName = _LpIlsFwdrLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 1, 1, 2),
    _LpIlsFwdrLtFbTxInfoComponentName_Type()
)
lpIlsFwdrLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfoStorageType_Type = StorageType
_LpIlsFwdrLtFbTxInfoStorageType_Object = MibTableColumn
lpIlsFwdrLtFbTxInfoStorageType = _LpIlsFwdrLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 1, 1, 4),
    _LpIlsFwdrLtFbTxInfoStorageType_Type()
)
lpIlsFwdrLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfoIndex_Type = NonReplicated
_LpIlsFwdrLtFbTxInfoIndex_Object = MibTableColumn
lpIlsFwdrLtFbTxInfoIndex = _LpIlsFwdrLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 1, 1, 10),
    _LpIlsFwdrLtFbTxInfoIndex_Type()
)
lpIlsFwdrLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoIndex.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfoTopTable_Object = MibTable
lpIlsFwdrLtFbTxInfoTopTable = _LpIlsFwdrLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbTxInfoTopEntry_Object = MibTableRow
lpIlsFwdrLtFbTxInfoTopEntry = _LpIlsFwdrLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 10, 1)
)
lpIlsFwdrLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbTxInfoTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbTxInfoTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbTxInfoTData_Object = MibTableColumn
lpIlsFwdrLtFbTxInfoTData = _LpIlsFwdrLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 2, 10, 1, 1),
    _LpIlsFwdrLtFbTxInfoTData_Type()
)
lpIlsFwdrLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTxInfoTData.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMac_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbFddiMac = _LpIlsFwdrLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3)
)
_LpIlsFwdrLtFbFddiMacRowStatusTable_Object = MibTable
lpIlsFwdrLtFbFddiMacRowStatusTable = _LpIlsFwdrLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMacRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbFddiMacRowStatusEntry = _LpIlsFwdrLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 1, 1)
)
lpIlsFwdrLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMacRowStatus_Type = RowStatus
_LpIlsFwdrLtFbFddiMacRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbFddiMacRowStatus = _LpIlsFwdrLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 1, 1, 1),
    _LpIlsFwdrLtFbFddiMacRowStatus_Type()
)
lpIlsFwdrLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMacComponentName_Type = DisplayString
_LpIlsFwdrLtFbFddiMacComponentName_Object = MibTableColumn
lpIlsFwdrLtFbFddiMacComponentName = _LpIlsFwdrLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 1, 1, 2),
    _LpIlsFwdrLtFbFddiMacComponentName_Type()
)
lpIlsFwdrLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMacStorageType_Type = StorageType
_LpIlsFwdrLtFbFddiMacStorageType_Object = MibTableColumn
lpIlsFwdrLtFbFddiMacStorageType = _LpIlsFwdrLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 1, 1, 4),
    _LpIlsFwdrLtFbFddiMacStorageType_Type()
)
lpIlsFwdrLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMacIndex_Type = NonReplicated
_LpIlsFwdrLtFbFddiMacIndex_Object = MibTableColumn
lpIlsFwdrLtFbFddiMacIndex = _LpIlsFwdrLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 1, 1, 10),
    _LpIlsFwdrLtFbFddiMacIndex_Type()
)
lpIlsFwdrLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacIndex.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMacTopTable_Object = MibTable
lpIlsFwdrLtFbFddiMacTopTable = _LpIlsFwdrLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbFddiMacTopEntry_Object = MibTableRow
lpIlsFwdrLtFbFddiMacTopEntry = _LpIlsFwdrLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 10, 1)
)
lpIlsFwdrLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbFddiMacTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbFddiMacTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbFddiMacTData_Object = MibTableColumn
lpIlsFwdrLtFbFddiMacTData = _LpIlsFwdrLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 3, 10, 1, 1),
    _LpIlsFwdrLtFbFddiMacTData_Type()
)
lpIlsFwdrLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbFddiMacTData.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnet_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbMacEnet = _LpIlsFwdrLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4)
)
_LpIlsFwdrLtFbMacEnetRowStatusTable_Object = MibTable
lpIlsFwdrLtFbMacEnetRowStatusTable = _LpIlsFwdrLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnetRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbMacEnetRowStatusEntry = _LpIlsFwdrLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 1, 1)
)
lpIlsFwdrLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnetRowStatus_Type = RowStatus
_LpIlsFwdrLtFbMacEnetRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbMacEnetRowStatus = _LpIlsFwdrLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 1, 1, 1),
    _LpIlsFwdrLtFbMacEnetRowStatus_Type()
)
lpIlsFwdrLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnetComponentName_Type = DisplayString
_LpIlsFwdrLtFbMacEnetComponentName_Object = MibTableColumn
lpIlsFwdrLtFbMacEnetComponentName = _LpIlsFwdrLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 1, 1, 2),
    _LpIlsFwdrLtFbMacEnetComponentName_Type()
)
lpIlsFwdrLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnetStorageType_Type = StorageType
_LpIlsFwdrLtFbMacEnetStorageType_Object = MibTableColumn
lpIlsFwdrLtFbMacEnetStorageType = _LpIlsFwdrLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 1, 1, 4),
    _LpIlsFwdrLtFbMacEnetStorageType_Type()
)
lpIlsFwdrLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnetIndex_Type = NonReplicated
_LpIlsFwdrLtFbMacEnetIndex_Object = MibTableColumn
lpIlsFwdrLtFbMacEnetIndex = _LpIlsFwdrLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 1, 1, 10),
    _LpIlsFwdrLtFbMacEnetIndex_Type()
)
lpIlsFwdrLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetIndex.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnetTopTable_Object = MibTable
lpIlsFwdrLtFbMacEnetTopTable = _LpIlsFwdrLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbMacEnetTopEntry_Object = MibTableRow
lpIlsFwdrLtFbMacEnetTopEntry = _LpIlsFwdrLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 10, 1)
)
lpIlsFwdrLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbMacEnetTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbMacEnetTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbMacEnetTData_Object = MibTableColumn
lpIlsFwdrLtFbMacEnetTData = _LpIlsFwdrLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 4, 10, 1, 1),
    _LpIlsFwdrLtFbMacEnetTData_Type()
)
lpIlsFwdrLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacEnetTData.setStatus("mandatory")
_LpIlsFwdrLtFbMacTr_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbMacTr = _LpIlsFwdrLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5)
)
_LpIlsFwdrLtFbMacTrRowStatusTable_Object = MibTable
lpIlsFwdrLtFbMacTrRowStatusTable = _LpIlsFwdrLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbMacTrRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbMacTrRowStatusEntry = _LpIlsFwdrLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 1, 1)
)
lpIlsFwdrLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbMacTrRowStatus_Type = RowStatus
_LpIlsFwdrLtFbMacTrRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbMacTrRowStatus = _LpIlsFwdrLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 1, 1, 1),
    _LpIlsFwdrLtFbMacTrRowStatus_Type()
)
lpIlsFwdrLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbMacTrComponentName_Type = DisplayString
_LpIlsFwdrLtFbMacTrComponentName_Object = MibTableColumn
lpIlsFwdrLtFbMacTrComponentName = _LpIlsFwdrLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 1, 1, 2),
    _LpIlsFwdrLtFbMacTrComponentName_Type()
)
lpIlsFwdrLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbMacTrStorageType_Type = StorageType
_LpIlsFwdrLtFbMacTrStorageType_Object = MibTableColumn
lpIlsFwdrLtFbMacTrStorageType = _LpIlsFwdrLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 1, 1, 4),
    _LpIlsFwdrLtFbMacTrStorageType_Type()
)
lpIlsFwdrLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbMacTrIndex_Type = NonReplicated
_LpIlsFwdrLtFbMacTrIndex_Object = MibTableColumn
lpIlsFwdrLtFbMacTrIndex = _LpIlsFwdrLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 1, 1, 10),
    _LpIlsFwdrLtFbMacTrIndex_Type()
)
lpIlsFwdrLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrIndex.setStatus("mandatory")
_LpIlsFwdrLtFbMacTrTopTable_Object = MibTable
lpIlsFwdrLtFbMacTrTopTable = _LpIlsFwdrLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbMacTrTopEntry_Object = MibTableRow
lpIlsFwdrLtFbMacTrTopEntry = _LpIlsFwdrLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 10, 1)
)
lpIlsFwdrLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbMacTrTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbMacTrTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbMacTrTData_Object = MibTableColumn
lpIlsFwdrLtFbMacTrTData = _LpIlsFwdrLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 5, 10, 1, 1),
    _LpIlsFwdrLtFbMacTrTData_Type()
)
lpIlsFwdrLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbMacTrTData.setStatus("mandatory")
_LpIlsFwdrLtFbData_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbData = _LpIlsFwdrLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6)
)
_LpIlsFwdrLtFbDataRowStatusTable_Object = MibTable
lpIlsFwdrLtFbDataRowStatusTable = _LpIlsFwdrLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbDataRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbDataRowStatusEntry = _LpIlsFwdrLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 1, 1)
)
lpIlsFwdrLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbDataRowStatus_Type = RowStatus
_LpIlsFwdrLtFbDataRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbDataRowStatus = _LpIlsFwdrLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 1, 1, 1),
    _LpIlsFwdrLtFbDataRowStatus_Type()
)
lpIlsFwdrLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbDataComponentName_Type = DisplayString
_LpIlsFwdrLtFbDataComponentName_Object = MibTableColumn
lpIlsFwdrLtFbDataComponentName = _LpIlsFwdrLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 1, 1, 2),
    _LpIlsFwdrLtFbDataComponentName_Type()
)
lpIlsFwdrLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbDataStorageType_Type = StorageType
_LpIlsFwdrLtFbDataStorageType_Object = MibTableColumn
lpIlsFwdrLtFbDataStorageType = _LpIlsFwdrLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 1, 1, 4),
    _LpIlsFwdrLtFbDataStorageType_Type()
)
lpIlsFwdrLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbDataIndex_Type = NonReplicated
_LpIlsFwdrLtFbDataIndex_Object = MibTableColumn
lpIlsFwdrLtFbDataIndex = _LpIlsFwdrLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 1, 1, 10),
    _LpIlsFwdrLtFbDataIndex_Type()
)
lpIlsFwdrLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataIndex.setStatus("mandatory")
_LpIlsFwdrLtFbDataTopTable_Object = MibTable
lpIlsFwdrLtFbDataTopTable = _LpIlsFwdrLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbDataTopEntry_Object = MibTableRow
lpIlsFwdrLtFbDataTopEntry = _LpIlsFwdrLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 10, 1)
)
lpIlsFwdrLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbDataTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbDataTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbDataTData_Object = MibTableColumn
lpIlsFwdrLtFbDataTData = _LpIlsFwdrLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 6, 10, 1, 1),
    _LpIlsFwdrLtFbDataTData_Type()
)
lpIlsFwdrLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbDataTData.setStatus("mandatory")
_LpIlsFwdrLtFbIpH_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbIpH = _LpIlsFwdrLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7)
)
_LpIlsFwdrLtFbIpHRowStatusTable_Object = MibTable
lpIlsFwdrLtFbIpHRowStatusTable = _LpIlsFwdrLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbIpHRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbIpHRowStatusEntry = _LpIlsFwdrLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 1, 1)
)
lpIlsFwdrLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbIpHRowStatus_Type = RowStatus
_LpIlsFwdrLtFbIpHRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbIpHRowStatus = _LpIlsFwdrLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 1, 1, 1),
    _LpIlsFwdrLtFbIpHRowStatus_Type()
)
lpIlsFwdrLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbIpHComponentName_Type = DisplayString
_LpIlsFwdrLtFbIpHComponentName_Object = MibTableColumn
lpIlsFwdrLtFbIpHComponentName = _LpIlsFwdrLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 1, 1, 2),
    _LpIlsFwdrLtFbIpHComponentName_Type()
)
lpIlsFwdrLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbIpHStorageType_Type = StorageType
_LpIlsFwdrLtFbIpHStorageType_Object = MibTableColumn
lpIlsFwdrLtFbIpHStorageType = _LpIlsFwdrLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 1, 1, 4),
    _LpIlsFwdrLtFbIpHStorageType_Type()
)
lpIlsFwdrLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbIpHIndex_Type = NonReplicated
_LpIlsFwdrLtFbIpHIndex_Object = MibTableColumn
lpIlsFwdrLtFbIpHIndex = _LpIlsFwdrLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 1, 1, 10),
    _LpIlsFwdrLtFbIpHIndex_Type()
)
lpIlsFwdrLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHIndex.setStatus("mandatory")
_LpIlsFwdrLtFbIpHTopTable_Object = MibTable
lpIlsFwdrLtFbIpHTopTable = _LpIlsFwdrLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbIpHTopEntry_Object = MibTableRow
lpIlsFwdrLtFbIpHTopEntry = _LpIlsFwdrLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 10, 1)
)
lpIlsFwdrLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbIpHTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbIpHTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbIpHTData_Object = MibTableColumn
lpIlsFwdrLtFbIpHTData = _LpIlsFwdrLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 7, 10, 1, 1),
    _LpIlsFwdrLtFbIpHTData_Type()
)
lpIlsFwdrLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpHTData.setStatus("mandatory")
_LpIlsFwdrLtFbLlch_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbLlch = _LpIlsFwdrLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8)
)
_LpIlsFwdrLtFbLlchRowStatusTable_Object = MibTable
lpIlsFwdrLtFbLlchRowStatusTable = _LpIlsFwdrLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbLlchRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbLlchRowStatusEntry = _LpIlsFwdrLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 1, 1)
)
lpIlsFwdrLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbLlchRowStatus_Type = RowStatus
_LpIlsFwdrLtFbLlchRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbLlchRowStatus = _LpIlsFwdrLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 1, 1, 1),
    _LpIlsFwdrLtFbLlchRowStatus_Type()
)
lpIlsFwdrLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbLlchComponentName_Type = DisplayString
_LpIlsFwdrLtFbLlchComponentName_Object = MibTableColumn
lpIlsFwdrLtFbLlchComponentName = _LpIlsFwdrLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 1, 1, 2),
    _LpIlsFwdrLtFbLlchComponentName_Type()
)
lpIlsFwdrLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbLlchStorageType_Type = StorageType
_LpIlsFwdrLtFbLlchStorageType_Object = MibTableColumn
lpIlsFwdrLtFbLlchStorageType = _LpIlsFwdrLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 1, 1, 4),
    _LpIlsFwdrLtFbLlchStorageType_Type()
)
lpIlsFwdrLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbLlchIndex_Type = NonReplicated
_LpIlsFwdrLtFbLlchIndex_Object = MibTableColumn
lpIlsFwdrLtFbLlchIndex = _LpIlsFwdrLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 1, 1, 10),
    _LpIlsFwdrLtFbLlchIndex_Type()
)
lpIlsFwdrLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchIndex.setStatus("mandatory")
_LpIlsFwdrLtFbLlchTopTable_Object = MibTable
lpIlsFwdrLtFbLlchTopTable = _LpIlsFwdrLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbLlchTopEntry_Object = MibTableRow
lpIlsFwdrLtFbLlchTopEntry = _LpIlsFwdrLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 10, 1)
)
lpIlsFwdrLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbLlchTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbLlchTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbLlchTData_Object = MibTableColumn
lpIlsFwdrLtFbLlchTData = _LpIlsFwdrLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 8, 10, 1, 1),
    _LpIlsFwdrLtFbLlchTData_Type()
)
lpIlsFwdrLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbLlchTData.setStatus("mandatory")
_LpIlsFwdrLtFbAppleH_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbAppleH = _LpIlsFwdrLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9)
)
_LpIlsFwdrLtFbAppleHRowStatusTable_Object = MibTable
lpIlsFwdrLtFbAppleHRowStatusTable = _LpIlsFwdrLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbAppleHRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbAppleHRowStatusEntry = _LpIlsFwdrLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 1, 1)
)
lpIlsFwdrLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbAppleHRowStatus_Type = RowStatus
_LpIlsFwdrLtFbAppleHRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbAppleHRowStatus = _LpIlsFwdrLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 1, 1, 1),
    _LpIlsFwdrLtFbAppleHRowStatus_Type()
)
lpIlsFwdrLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbAppleHComponentName_Type = DisplayString
_LpIlsFwdrLtFbAppleHComponentName_Object = MibTableColumn
lpIlsFwdrLtFbAppleHComponentName = _LpIlsFwdrLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 1, 1, 2),
    _LpIlsFwdrLtFbAppleHComponentName_Type()
)
lpIlsFwdrLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbAppleHStorageType_Type = StorageType
_LpIlsFwdrLtFbAppleHStorageType_Object = MibTableColumn
lpIlsFwdrLtFbAppleHStorageType = _LpIlsFwdrLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 1, 1, 4),
    _LpIlsFwdrLtFbAppleHStorageType_Type()
)
lpIlsFwdrLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbAppleHIndex_Type = NonReplicated
_LpIlsFwdrLtFbAppleHIndex_Object = MibTableColumn
lpIlsFwdrLtFbAppleHIndex = _LpIlsFwdrLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 1, 1, 10),
    _LpIlsFwdrLtFbAppleHIndex_Type()
)
lpIlsFwdrLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHIndex.setStatus("mandatory")
_LpIlsFwdrLtFbAppleHTopTable_Object = MibTable
lpIlsFwdrLtFbAppleHTopTable = _LpIlsFwdrLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbAppleHTopEntry_Object = MibTableRow
lpIlsFwdrLtFbAppleHTopEntry = _LpIlsFwdrLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 10, 1)
)
lpIlsFwdrLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbAppleHTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbAppleHTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbAppleHTData_Object = MibTableColumn
lpIlsFwdrLtFbAppleHTData = _LpIlsFwdrLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 9, 10, 1, 1),
    _LpIlsFwdrLtFbAppleHTData_Type()
)
lpIlsFwdrLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbAppleHTData.setStatus("mandatory")
_LpIlsFwdrLtFbIpxH_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtFbIpxH = _LpIlsFwdrLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10)
)
_LpIlsFwdrLtFbIpxHRowStatusTable_Object = MibTable
lpIlsFwdrLtFbIpxHRowStatusTable = _LpIlsFwdrLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtFbIpxHRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtFbIpxHRowStatusEntry = _LpIlsFwdrLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 1, 1)
)
lpIlsFwdrLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtFbIpxHRowStatus_Type = RowStatus
_LpIlsFwdrLtFbIpxHRowStatus_Object = MibTableColumn
lpIlsFwdrLtFbIpxHRowStatus = _LpIlsFwdrLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 1, 1, 1),
    _LpIlsFwdrLtFbIpxHRowStatus_Type()
)
lpIlsFwdrLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHRowStatus.setStatus("mandatory")
_LpIlsFwdrLtFbIpxHComponentName_Type = DisplayString
_LpIlsFwdrLtFbIpxHComponentName_Object = MibTableColumn
lpIlsFwdrLtFbIpxHComponentName = _LpIlsFwdrLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 1, 1, 2),
    _LpIlsFwdrLtFbIpxHComponentName_Type()
)
lpIlsFwdrLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHComponentName.setStatus("mandatory")
_LpIlsFwdrLtFbIpxHStorageType_Type = StorageType
_LpIlsFwdrLtFbIpxHStorageType_Object = MibTableColumn
lpIlsFwdrLtFbIpxHStorageType = _LpIlsFwdrLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 1, 1, 4),
    _LpIlsFwdrLtFbIpxHStorageType_Type()
)
lpIlsFwdrLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHStorageType.setStatus("mandatory")
_LpIlsFwdrLtFbIpxHIndex_Type = NonReplicated
_LpIlsFwdrLtFbIpxHIndex_Object = MibTableColumn
lpIlsFwdrLtFbIpxHIndex = _LpIlsFwdrLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 1, 1, 10),
    _LpIlsFwdrLtFbIpxHIndex_Type()
)
lpIlsFwdrLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHIndex.setStatus("mandatory")
_LpIlsFwdrLtFbIpxHTopTable_Object = MibTable
lpIlsFwdrLtFbIpxHTopTable = _LpIlsFwdrLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbIpxHTopEntry_Object = MibTableRow
lpIlsFwdrLtFbIpxHTopEntry = _LpIlsFwdrLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 10, 1)
)
lpIlsFwdrLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbIpxHTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbIpxHTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbIpxHTData_Object = MibTableColumn
lpIlsFwdrLtFbIpxHTData = _LpIlsFwdrLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 10, 10, 1, 1),
    _LpIlsFwdrLtFbIpxHTData_Type()
)
lpIlsFwdrLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbIpxHTData.setStatus("mandatory")
_LpIlsFwdrLtFbTopTable_Object = MibTable
lpIlsFwdrLtFbTopTable = _LpIlsFwdrLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 20)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTopTable.setStatus("mandatory")
_LpIlsFwdrLtFbTopEntry_Object = MibTableRow
lpIlsFwdrLtFbTopEntry = _LpIlsFwdrLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 20, 1)
)
lpIlsFwdrLtFbTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtFbIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtFbTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtFbTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtFbTData_Object = MibTableColumn
lpIlsFwdrLtFbTData = _LpIlsFwdrLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 5, 20, 1, 1),
    _LpIlsFwdrLtFbTData_Type()
)
lpIlsFwdrLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtFbTData.setStatus("mandatory")
_LpIlsFwdrLtCntl_ObjectIdentity = ObjectIdentity
lpIlsFwdrLtCntl = _LpIlsFwdrLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6)
)
_LpIlsFwdrLtCntlRowStatusTable_Object = MibTable
lpIlsFwdrLtCntlRowStatusTable = _LpIlsFwdrLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlRowStatusTable.setStatus("mandatory")
_LpIlsFwdrLtCntlRowStatusEntry_Object = MibTableRow
lpIlsFwdrLtCntlRowStatusEntry = _LpIlsFwdrLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 1, 1)
)
lpIlsFwdrLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrLtCntlRowStatus_Type = RowStatus
_LpIlsFwdrLtCntlRowStatus_Object = MibTableColumn
lpIlsFwdrLtCntlRowStatus = _LpIlsFwdrLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 1, 1, 1),
    _LpIlsFwdrLtCntlRowStatus_Type()
)
lpIlsFwdrLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlRowStatus.setStatus("mandatory")
_LpIlsFwdrLtCntlComponentName_Type = DisplayString
_LpIlsFwdrLtCntlComponentName_Object = MibTableColumn
lpIlsFwdrLtCntlComponentName = _LpIlsFwdrLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 1, 1, 2),
    _LpIlsFwdrLtCntlComponentName_Type()
)
lpIlsFwdrLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlComponentName.setStatus("mandatory")
_LpIlsFwdrLtCntlStorageType_Type = StorageType
_LpIlsFwdrLtCntlStorageType_Object = MibTableColumn
lpIlsFwdrLtCntlStorageType = _LpIlsFwdrLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 1, 1, 4),
    _LpIlsFwdrLtCntlStorageType_Type()
)
lpIlsFwdrLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlStorageType.setStatus("mandatory")
_LpIlsFwdrLtCntlIndex_Type = NonReplicated
_LpIlsFwdrLtCntlIndex_Object = MibTableColumn
lpIlsFwdrLtCntlIndex = _LpIlsFwdrLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 1, 1, 10),
    _LpIlsFwdrLtCntlIndex_Type()
)
lpIlsFwdrLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlIndex.setStatus("mandatory")
_LpIlsFwdrLtCntlTopTable_Object = MibTable
lpIlsFwdrLtCntlTopTable = _LpIlsFwdrLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlTopTable.setStatus("mandatory")
_LpIlsFwdrLtCntlTopEntry_Object = MibTableRow
lpIlsFwdrLtCntlTopEntry = _LpIlsFwdrLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 10, 1)
)
lpIlsFwdrLtCntlTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtCntlTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtCntlTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtCntlTData_Object = MibTableColumn
lpIlsFwdrLtCntlTData = _LpIlsFwdrLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 6, 10, 1, 1),
    _LpIlsFwdrLtCntlTData_Type()
)
lpIlsFwdrLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtCntlTData.setStatus("mandatory")
_LpIlsFwdrLtTopTable_Object = MibTable
lpIlsFwdrLtTopTable = _LpIlsFwdrLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 20)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtTopTable.setStatus("mandatory")
_LpIlsFwdrLtTopEntry_Object = MibTableRow
lpIlsFwdrLtTopEntry = _LpIlsFwdrLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 20, 1)
)
lpIlsFwdrLtTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLtIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLtTopEntry.setStatus("mandatory")


class _LpIlsFwdrLtTData_Type(AsciiString):
    """Custom type lpIlsFwdrLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpIlsFwdrLtTData_Type.__name__ = "AsciiString"
_LpIlsFwdrLtTData_Object = MibTableColumn
lpIlsFwdrLtTData = _LpIlsFwdrLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 2, 20, 1, 1),
    _LpIlsFwdrLtTData_Type()
)
lpIlsFwdrLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrLtTData.setStatus("mandatory")
_LpIlsFwdrTest_ObjectIdentity = ObjectIdentity
lpIlsFwdrTest = _LpIlsFwdrTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5)
)
_LpIlsFwdrTestRowStatusTable_Object = MibTable
lpIlsFwdrTestRowStatusTable = _LpIlsFwdrTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 1)
)
if mibBuilder.loadTexts:
    lpIlsFwdrTestRowStatusTable.setStatus("mandatory")
_LpIlsFwdrTestRowStatusEntry_Object = MibTableRow
lpIlsFwdrTestRowStatusEntry = _LpIlsFwdrTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 1, 1)
)
lpIlsFwdrTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrTestIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrTestRowStatusEntry.setStatus("mandatory")
_LpIlsFwdrTestRowStatus_Type = RowStatus
_LpIlsFwdrTestRowStatus_Object = MibTableColumn
lpIlsFwdrTestRowStatus = _LpIlsFwdrTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 1, 1, 1),
    _LpIlsFwdrTestRowStatus_Type()
)
lpIlsFwdrTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestRowStatus.setStatus("mandatory")
_LpIlsFwdrTestComponentName_Type = DisplayString
_LpIlsFwdrTestComponentName_Object = MibTableColumn
lpIlsFwdrTestComponentName = _LpIlsFwdrTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 1, 1, 2),
    _LpIlsFwdrTestComponentName_Type()
)
lpIlsFwdrTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestComponentName.setStatus("mandatory")
_LpIlsFwdrTestStorageType_Type = StorageType
_LpIlsFwdrTestStorageType_Object = MibTableColumn
lpIlsFwdrTestStorageType = _LpIlsFwdrTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 1, 1, 4),
    _LpIlsFwdrTestStorageType_Type()
)
lpIlsFwdrTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestStorageType.setStatus("mandatory")
_LpIlsFwdrTestIndex_Type = NonReplicated
_LpIlsFwdrTestIndex_Object = MibTableColumn
lpIlsFwdrTestIndex = _LpIlsFwdrTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 1, 1, 10),
    _LpIlsFwdrTestIndex_Type()
)
lpIlsFwdrTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIlsFwdrTestIndex.setStatus("mandatory")
_LpIlsFwdrTestPTOTable_Object = MibTable
lpIlsFwdrTestPTOTable = _LpIlsFwdrTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 10)
)
if mibBuilder.loadTexts:
    lpIlsFwdrTestPTOTable.setStatus("mandatory")
_LpIlsFwdrTestPTOEntry_Object = MibTableRow
lpIlsFwdrTestPTOEntry = _LpIlsFwdrTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 10, 1)
)
lpIlsFwdrTestPTOEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrTestIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrTestPTOEntry.setStatus("mandatory")


class _LpIlsFwdrTestType_Type(Integer32):
    """Custom type lpIlsFwdrTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              257,
              258,
              259,
              260,
              263,
              264,
              265,
              266,
              267,
              268)
        )
    )
    namedValues = NamedValues(
        *(("extThruA", 265),
          ("extThruB", 266),
          ("extWrapA", 263),
          ("extWrapAB", 267),
          ("extWrapB", 264),
          ("extWrapBA", 268),
          ("normal", 1),
          ("onCard", 0),
          ("thruA", 259),
          ("thruB", 260),
          ("wrapA", 257),
          ("wrapB", 258))
    )


_LpIlsFwdrTestType_Type.__name__ = "Integer32"
_LpIlsFwdrTestType_Object = MibTableColumn
lpIlsFwdrTestType = _LpIlsFwdrTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 10, 1, 1),
    _LpIlsFwdrTestType_Type()
)
lpIlsFwdrTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrTestType.setStatus("mandatory")


class _LpIlsFwdrTestFrmSize_Type(Unsigned32):
    """Custom type lpIlsFwdrTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpIlsFwdrTestFrmSize_Type.__name__ = "Unsigned32"
_LpIlsFwdrTestFrmSize_Object = MibTableColumn
lpIlsFwdrTestFrmSize = _LpIlsFwdrTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 10, 1, 2),
    _LpIlsFwdrTestFrmSize_Type()
)
lpIlsFwdrTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrTestFrmSize.setStatus("mandatory")


class _LpIlsFwdrTestDuration_Type(Unsigned32):
    """Custom type lpIlsFwdrTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpIlsFwdrTestDuration_Type.__name__ = "Unsigned32"
_LpIlsFwdrTestDuration_Object = MibTableColumn
lpIlsFwdrTestDuration = _LpIlsFwdrTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 10, 1, 3),
    _LpIlsFwdrTestDuration_Type()
)
lpIlsFwdrTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrTestDuration.setStatus("mandatory")
_LpIlsFwdrTestResultsTable_Object = MibTable
lpIlsFwdrTestResultsTable = _LpIlsFwdrTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11)
)
if mibBuilder.loadTexts:
    lpIlsFwdrTestResultsTable.setStatus("mandatory")
_LpIlsFwdrTestResultsEntry_Object = MibTableRow
lpIlsFwdrTestResultsEntry = _LpIlsFwdrTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1)
)
lpIlsFwdrTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrTestIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrTestResultsEntry.setStatus("mandatory")
_LpIlsFwdrTestElapsedTime_Type = Counter32
_LpIlsFwdrTestElapsedTime_Object = MibTableColumn
lpIlsFwdrTestElapsedTime = _LpIlsFwdrTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 4),
    _LpIlsFwdrTestElapsedTime_Type()
)
lpIlsFwdrTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestElapsedTime.setStatus("mandatory")


class _LpIlsFwdrTestTimeRemaining_Type(Unsigned32):
    """Custom type lpIlsFwdrTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpIlsFwdrTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpIlsFwdrTestTimeRemaining_Object = MibTableColumn
lpIlsFwdrTestTimeRemaining = _LpIlsFwdrTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 5),
    _LpIlsFwdrTestTimeRemaining_Type()
)
lpIlsFwdrTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestTimeRemaining.setStatus("mandatory")


class _LpIlsFwdrTestCauseOfTermination_Type(Integer32):
    """Custom type lpIlsFwdrTestCauseOfTermination based on Integer32"""
    defaultValue = 3

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
        *(("neverStarted", 3),
          ("stoppedByOperator", 1),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_LpIlsFwdrTestCauseOfTermination_Type.__name__ = "Integer32"
_LpIlsFwdrTestCauseOfTermination_Object = MibTableColumn
lpIlsFwdrTestCauseOfTermination = _LpIlsFwdrTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 6),
    _LpIlsFwdrTestCauseOfTermination_Type()
)
lpIlsFwdrTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestCauseOfTermination.setStatus("mandatory")
_LpIlsFwdrTestFrmTx_Type = PassportCounter64
_LpIlsFwdrTestFrmTx_Object = MibTableColumn
lpIlsFwdrTestFrmTx = _LpIlsFwdrTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 7),
    _LpIlsFwdrTestFrmTx_Type()
)
lpIlsFwdrTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestFrmTx.setStatus("mandatory")
_LpIlsFwdrTestBitsTx_Type = PassportCounter64
_LpIlsFwdrTestBitsTx_Object = MibTableColumn
lpIlsFwdrTestBitsTx = _LpIlsFwdrTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 8),
    _LpIlsFwdrTestBitsTx_Type()
)
lpIlsFwdrTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestBitsTx.setStatus("mandatory")
_LpIlsFwdrTestFrmRx_Type = PassportCounter64
_LpIlsFwdrTestFrmRx_Object = MibTableColumn
lpIlsFwdrTestFrmRx = _LpIlsFwdrTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 9),
    _LpIlsFwdrTestFrmRx_Type()
)
lpIlsFwdrTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestFrmRx.setStatus("mandatory")
_LpIlsFwdrTestBitsRx_Type = PassportCounter64
_LpIlsFwdrTestBitsRx_Object = MibTableColumn
lpIlsFwdrTestBitsRx = _LpIlsFwdrTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 10),
    _LpIlsFwdrTestBitsRx_Type()
)
lpIlsFwdrTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestBitsRx.setStatus("mandatory")
_LpIlsFwdrTestErroredFrmRx_Type = PassportCounter64
_LpIlsFwdrTestErroredFrmRx_Object = MibTableColumn
lpIlsFwdrTestErroredFrmRx = _LpIlsFwdrTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 5, 11, 1, 11),
    _LpIlsFwdrTestErroredFrmRx_Type()
)
lpIlsFwdrTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrTestErroredFrmRx.setStatus("mandatory")
_LpIlsFwdrIfEntryTable_Object = MibTable
lpIlsFwdrIfEntryTable = _LpIlsFwdrIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 11)
)
if mibBuilder.loadTexts:
    lpIlsFwdrIfEntryTable.setStatus("mandatory")
_LpIlsFwdrIfEntryEntry_Object = MibTableRow
lpIlsFwdrIfEntryEntry = _LpIlsFwdrIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 11, 1)
)
lpIlsFwdrIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrIfEntryEntry.setStatus("mandatory")


class _LpIlsFwdrIfAdminStatus_Type(Integer32):
    """Custom type lpIlsFwdrIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpIlsFwdrIfAdminStatus_Type.__name__ = "Integer32"
_LpIlsFwdrIfAdminStatus_Object = MibTableColumn
lpIlsFwdrIfAdminStatus = _LpIlsFwdrIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 11, 1, 1),
    _LpIlsFwdrIfAdminStatus_Type()
)
lpIlsFwdrIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpIlsFwdrIfAdminStatus.setStatus("mandatory")


class _LpIlsFwdrIfIndex_Type(InterfaceIndex):
    """Custom type lpIlsFwdrIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpIlsFwdrIfIndex_Type.__name__ = "InterfaceIndex"
_LpIlsFwdrIfIndex_Object = MibTableColumn
lpIlsFwdrIfIndex = _LpIlsFwdrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 11, 1, 2),
    _LpIlsFwdrIfIndex_Type()
)
lpIlsFwdrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrIfIndex.setStatus("mandatory")
_LpIlsFwdrStateTable_Object = MibTable
lpIlsFwdrStateTable = _LpIlsFwdrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 12)
)
if mibBuilder.loadTexts:
    lpIlsFwdrStateTable.setStatus("mandatory")
_LpIlsFwdrStateEntry_Object = MibTableRow
lpIlsFwdrStateEntry = _LpIlsFwdrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 12, 1)
)
lpIlsFwdrStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrStateEntry.setStatus("mandatory")


class _LpIlsFwdrAdminState_Type(Integer32):
    """Custom type lpIlsFwdrAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_LpIlsFwdrAdminState_Type.__name__ = "Integer32"
_LpIlsFwdrAdminState_Object = MibTableColumn
lpIlsFwdrAdminState = _LpIlsFwdrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 12, 1, 1),
    _LpIlsFwdrAdminState_Type()
)
lpIlsFwdrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrAdminState.setStatus("mandatory")


class _LpIlsFwdrOperationalState_Type(Integer32):
    """Custom type lpIlsFwdrOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LpIlsFwdrOperationalState_Type.__name__ = "Integer32"
_LpIlsFwdrOperationalState_Object = MibTableColumn
lpIlsFwdrOperationalState = _LpIlsFwdrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 12, 1, 2),
    _LpIlsFwdrOperationalState_Type()
)
lpIlsFwdrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrOperationalState.setStatus("mandatory")


class _LpIlsFwdrUsageState_Type(Integer32):
    """Custom type lpIlsFwdrUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_LpIlsFwdrUsageState_Type.__name__ = "Integer32"
_LpIlsFwdrUsageState_Object = MibTableColumn
lpIlsFwdrUsageState = _LpIlsFwdrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 12, 1, 3),
    _LpIlsFwdrUsageState_Type()
)
lpIlsFwdrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrUsageState.setStatus("mandatory")
_LpIlsFwdrOperStatusTable_Object = MibTable
lpIlsFwdrOperStatusTable = _LpIlsFwdrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 13)
)
if mibBuilder.loadTexts:
    lpIlsFwdrOperStatusTable.setStatus("mandatory")
_LpIlsFwdrOperStatusEntry_Object = MibTableRow
lpIlsFwdrOperStatusEntry = _LpIlsFwdrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 13, 1)
)
lpIlsFwdrOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrOperStatusEntry.setStatus("mandatory")


class _LpIlsFwdrSnmpOperStatus_Type(Integer32):
    """Custom type lpIlsFwdrSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpIlsFwdrSnmpOperStatus_Type.__name__ = "Integer32"
_LpIlsFwdrSnmpOperStatus_Object = MibTableColumn
lpIlsFwdrSnmpOperStatus = _LpIlsFwdrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 13, 1, 1),
    _LpIlsFwdrSnmpOperStatus_Type()
)
lpIlsFwdrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrSnmpOperStatus.setStatus("mandatory")
_LpIlsFwdrStatsTable_Object = MibTable
lpIlsFwdrStatsTable = _LpIlsFwdrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 14)
)
if mibBuilder.loadTexts:
    lpIlsFwdrStatsTable.setStatus("mandatory")
_LpIlsFwdrStatsEntry_Object = MibTableRow
lpIlsFwdrStatsEntry = _LpIlsFwdrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 14, 1)
)
lpIlsFwdrStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrStatsEntry.setStatus("mandatory")
_LpIlsFwdrFramesReceived_Type = PassportCounter64
_LpIlsFwdrFramesReceived_Object = MibTableColumn
lpIlsFwdrFramesReceived = _LpIlsFwdrFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 14, 1, 1),
    _LpIlsFwdrFramesReceived_Type()
)
lpIlsFwdrFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrFramesReceived.setStatus("mandatory")
_LpIlsFwdrProcessedCount_Type = PassportCounter64
_LpIlsFwdrProcessedCount_Object = MibTableColumn
lpIlsFwdrProcessedCount = _LpIlsFwdrProcessedCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 14, 1, 2),
    _LpIlsFwdrProcessedCount_Type()
)
lpIlsFwdrProcessedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrProcessedCount.setStatus("mandatory")
_LpIlsFwdrErrorCount_Type = PassportCounter64
_LpIlsFwdrErrorCount_Object = MibTableColumn
lpIlsFwdrErrorCount = _LpIlsFwdrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 14, 1, 3),
    _LpIlsFwdrErrorCount_Type()
)
lpIlsFwdrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrErrorCount.setStatus("mandatory")
_LpIlsFwdrFramesDiscarded_Type = PassportCounter64
_LpIlsFwdrFramesDiscarded_Object = MibTableColumn
lpIlsFwdrFramesDiscarded = _LpIlsFwdrFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 14, 1, 4),
    _LpIlsFwdrFramesDiscarded_Type()
)
lpIlsFwdrFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrFramesDiscarded.setStatus("mandatory")
_LpIlsFwdrLinkToTrafficSourceTable_Object = MibTable
lpIlsFwdrLinkToTrafficSourceTable = _LpIlsFwdrLinkToTrafficSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 312)
)
if mibBuilder.loadTexts:
    lpIlsFwdrLinkToTrafficSourceTable.setStatus("mandatory")
_LpIlsFwdrLinkToTrafficSourceEntry_Object = MibTableRow
lpIlsFwdrLinkToTrafficSourceEntry = _LpIlsFwdrLinkToTrafficSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 312, 1)
)
lpIlsFwdrLinkToTrafficSourceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpIlsFwdrLinkToTrafficSourceValue"),
)
if mibBuilder.loadTexts:
    lpIlsFwdrLinkToTrafficSourceEntry.setStatus("mandatory")
_LpIlsFwdrLinkToTrafficSourceValue_Type = Link
_LpIlsFwdrLinkToTrafficSourceValue_Object = MibTableColumn
lpIlsFwdrLinkToTrafficSourceValue = _LpIlsFwdrLinkToTrafficSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 21, 312, 1, 1),
    _LpIlsFwdrLinkToTrafficSourceValue_Type()
)
lpIlsFwdrLinkToTrafficSourceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpIlsFwdrLinkToTrafficSourceValue.setStatus("mandatory")
_LpEth100_ObjectIdentity = ObjectIdentity
lpEth100 = _LpEth100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25)
)
_LpEth100RowStatusTable_Object = MibTable
lpEth100RowStatusTable = _LpEth100RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 1)
)
if mibBuilder.loadTexts:
    lpEth100RowStatusTable.setStatus("mandatory")
_LpEth100RowStatusEntry_Object = MibTableRow
lpEth100RowStatusEntry = _LpEth100RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 1, 1)
)
lpEth100RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100RowStatusEntry.setStatus("mandatory")
_LpEth100RowStatus_Type = RowStatus
_LpEth100RowStatus_Object = MibTableColumn
lpEth100RowStatus = _LpEth100RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 1, 1, 1),
    _LpEth100RowStatus_Type()
)
lpEth100RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100RowStatus.setStatus("mandatory")
_LpEth100ComponentName_Type = DisplayString
_LpEth100ComponentName_Object = MibTableColumn
lpEth100ComponentName = _LpEth100ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 1, 1, 2),
    _LpEth100ComponentName_Type()
)
lpEth100ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100ComponentName.setStatus("mandatory")
_LpEth100StorageType_Type = StorageType
_LpEth100StorageType_Object = MibTableColumn
lpEth100StorageType = _LpEth100StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 1, 1, 4),
    _LpEth100StorageType_Type()
)
lpEth100StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100StorageType.setStatus("mandatory")


class _LpEth100Index_Type(Integer32):
    """Custom type lpEth100Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpEth100Index_Type.__name__ = "Integer32"
_LpEth100Index_Object = MibTableColumn
lpEth100Index = _LpEth100Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 1, 1, 10),
    _LpEth100Index_Type()
)
lpEth100Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100Index.setStatus("mandatory")
_LpEth100Lt_ObjectIdentity = ObjectIdentity
lpEth100Lt = _LpEth100Lt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2)
)
_LpEth100LtRowStatusTable_Object = MibTable
lpEth100LtRowStatusTable = _LpEth100LtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtRowStatusTable.setStatus("mandatory")
_LpEth100LtRowStatusEntry_Object = MibTableRow
lpEth100LtRowStatusEntry = _LpEth100LtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 1, 1)
)
lpEth100LtRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtRowStatusEntry.setStatus("mandatory")
_LpEth100LtRowStatus_Type = RowStatus
_LpEth100LtRowStatus_Object = MibTableColumn
lpEth100LtRowStatus = _LpEth100LtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 1, 1, 1),
    _LpEth100LtRowStatus_Type()
)
lpEth100LtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtRowStatus.setStatus("mandatory")
_LpEth100LtComponentName_Type = DisplayString
_LpEth100LtComponentName_Object = MibTableColumn
lpEth100LtComponentName = _LpEth100LtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 1, 1, 2),
    _LpEth100LtComponentName_Type()
)
lpEth100LtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtComponentName.setStatus("mandatory")
_LpEth100LtStorageType_Type = StorageType
_LpEth100LtStorageType_Object = MibTableColumn
lpEth100LtStorageType = _LpEth100LtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 1, 1, 4),
    _LpEth100LtStorageType_Type()
)
lpEth100LtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtStorageType.setStatus("mandatory")
_LpEth100LtIndex_Type = NonReplicated
_LpEth100LtIndex_Object = MibTableColumn
lpEth100LtIndex = _LpEth100LtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 1, 1, 10),
    _LpEth100LtIndex_Type()
)
lpEth100LtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtIndex.setStatus("mandatory")
_LpEth100LtFrmCmp_ObjectIdentity = ObjectIdentity
lpEth100LtFrmCmp = _LpEth100LtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2)
)
_LpEth100LtFrmCmpRowStatusTable_Object = MibTable
lpEth100LtFrmCmpRowStatusTable = _LpEth100LtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpRowStatusTable.setStatus("mandatory")
_LpEth100LtFrmCmpRowStatusEntry_Object = MibTableRow
lpEth100LtFrmCmpRowStatusEntry = _LpEth100LtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 1, 1)
)
lpEth100LtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpRowStatusEntry.setStatus("mandatory")
_LpEth100LtFrmCmpRowStatus_Type = RowStatus
_LpEth100LtFrmCmpRowStatus_Object = MibTableColumn
lpEth100LtFrmCmpRowStatus = _LpEth100LtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 1, 1, 1),
    _LpEth100LtFrmCmpRowStatus_Type()
)
lpEth100LtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpRowStatus.setStatus("mandatory")
_LpEth100LtFrmCmpComponentName_Type = DisplayString
_LpEth100LtFrmCmpComponentName_Object = MibTableColumn
lpEth100LtFrmCmpComponentName = _LpEth100LtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 1, 1, 2),
    _LpEth100LtFrmCmpComponentName_Type()
)
lpEth100LtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpComponentName.setStatus("mandatory")
_LpEth100LtFrmCmpStorageType_Type = StorageType
_LpEth100LtFrmCmpStorageType_Object = MibTableColumn
lpEth100LtFrmCmpStorageType = _LpEth100LtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 1, 1, 4),
    _LpEth100LtFrmCmpStorageType_Type()
)
lpEth100LtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpStorageType.setStatus("mandatory")
_LpEth100LtFrmCmpIndex_Type = NonReplicated
_LpEth100LtFrmCmpIndex_Object = MibTableColumn
lpEth100LtFrmCmpIndex = _LpEth100LtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 1, 1, 10),
    _LpEth100LtFrmCmpIndex_Type()
)
lpEth100LtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpIndex.setStatus("mandatory")
_LpEth100LtFrmCmpTopTable_Object = MibTable
lpEth100LtFrmCmpTopTable = _LpEth100LtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpTopTable.setStatus("mandatory")
_LpEth100LtFrmCmpTopEntry_Object = MibTableRow
lpEth100LtFrmCmpTopEntry = _LpEth100LtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 10, 1)
)
lpEth100LtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpTopEntry.setStatus("mandatory")


class _LpEth100LtFrmCmpTData_Type(AsciiString):
    """Custom type lpEth100LtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFrmCmpTData_Type.__name__ = "AsciiString"
_LpEth100LtFrmCmpTData_Object = MibTableColumn
lpEth100LtFrmCmpTData = _LpEth100LtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 2, 10, 1, 1),
    _LpEth100LtFrmCmpTData_Type()
)
lpEth100LtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFrmCmpTData.setStatus("mandatory")
_LpEth100LtFrmCpy_ObjectIdentity = ObjectIdentity
lpEth100LtFrmCpy = _LpEth100LtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3)
)
_LpEth100LtFrmCpyRowStatusTable_Object = MibTable
lpEth100LtFrmCpyRowStatusTable = _LpEth100LtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyRowStatusTable.setStatus("mandatory")
_LpEth100LtFrmCpyRowStatusEntry_Object = MibTableRow
lpEth100LtFrmCpyRowStatusEntry = _LpEth100LtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 1, 1)
)
lpEth100LtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyRowStatusEntry.setStatus("mandatory")
_LpEth100LtFrmCpyRowStatus_Type = RowStatus
_LpEth100LtFrmCpyRowStatus_Object = MibTableColumn
lpEth100LtFrmCpyRowStatus = _LpEth100LtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 1, 1, 1),
    _LpEth100LtFrmCpyRowStatus_Type()
)
lpEth100LtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyRowStatus.setStatus("mandatory")
_LpEth100LtFrmCpyComponentName_Type = DisplayString
_LpEth100LtFrmCpyComponentName_Object = MibTableColumn
lpEth100LtFrmCpyComponentName = _LpEth100LtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 1, 1, 2),
    _LpEth100LtFrmCpyComponentName_Type()
)
lpEth100LtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyComponentName.setStatus("mandatory")
_LpEth100LtFrmCpyStorageType_Type = StorageType
_LpEth100LtFrmCpyStorageType_Object = MibTableColumn
lpEth100LtFrmCpyStorageType = _LpEth100LtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 1, 1, 4),
    _LpEth100LtFrmCpyStorageType_Type()
)
lpEth100LtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyStorageType.setStatus("mandatory")
_LpEth100LtFrmCpyIndex_Type = NonReplicated
_LpEth100LtFrmCpyIndex_Object = MibTableColumn
lpEth100LtFrmCpyIndex = _LpEth100LtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 1, 1, 10),
    _LpEth100LtFrmCpyIndex_Type()
)
lpEth100LtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyIndex.setStatus("mandatory")
_LpEth100LtFrmCpyTopTable_Object = MibTable
lpEth100LtFrmCpyTopTable = _LpEth100LtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyTopTable.setStatus("mandatory")
_LpEth100LtFrmCpyTopEntry_Object = MibTableRow
lpEth100LtFrmCpyTopEntry = _LpEth100LtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 10, 1)
)
lpEth100LtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyTopEntry.setStatus("mandatory")


class _LpEth100LtFrmCpyTData_Type(AsciiString):
    """Custom type lpEth100LtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFrmCpyTData_Type.__name__ = "AsciiString"
_LpEth100LtFrmCpyTData_Object = MibTableColumn
lpEth100LtFrmCpyTData = _LpEth100LtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 3, 10, 1, 1),
    _LpEth100LtFrmCpyTData_Type()
)
lpEth100LtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFrmCpyTData.setStatus("mandatory")
_LpEth100LtPrtCfg_ObjectIdentity = ObjectIdentity
lpEth100LtPrtCfg = _LpEth100LtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4)
)
_LpEth100LtPrtCfgRowStatusTable_Object = MibTable
lpEth100LtPrtCfgRowStatusTable = _LpEth100LtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgRowStatusTable.setStatus("mandatory")
_LpEth100LtPrtCfgRowStatusEntry_Object = MibTableRow
lpEth100LtPrtCfgRowStatusEntry = _LpEth100LtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 1, 1)
)
lpEth100LtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgRowStatusEntry.setStatus("mandatory")
_LpEth100LtPrtCfgRowStatus_Type = RowStatus
_LpEth100LtPrtCfgRowStatus_Object = MibTableColumn
lpEth100LtPrtCfgRowStatus = _LpEth100LtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 1, 1, 1),
    _LpEth100LtPrtCfgRowStatus_Type()
)
lpEth100LtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgRowStatus.setStatus("mandatory")
_LpEth100LtPrtCfgComponentName_Type = DisplayString
_LpEth100LtPrtCfgComponentName_Object = MibTableColumn
lpEth100LtPrtCfgComponentName = _LpEth100LtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 1, 1, 2),
    _LpEth100LtPrtCfgComponentName_Type()
)
lpEth100LtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgComponentName.setStatus("mandatory")
_LpEth100LtPrtCfgStorageType_Type = StorageType
_LpEth100LtPrtCfgStorageType_Object = MibTableColumn
lpEth100LtPrtCfgStorageType = _LpEth100LtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 1, 1, 4),
    _LpEth100LtPrtCfgStorageType_Type()
)
lpEth100LtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgStorageType.setStatus("mandatory")
_LpEth100LtPrtCfgIndex_Type = NonReplicated
_LpEth100LtPrtCfgIndex_Object = MibTableColumn
lpEth100LtPrtCfgIndex = _LpEth100LtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 1, 1, 10),
    _LpEth100LtPrtCfgIndex_Type()
)
lpEth100LtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgIndex.setStatus("mandatory")
_LpEth100LtPrtCfgTopTable_Object = MibTable
lpEth100LtPrtCfgTopTable = _LpEth100LtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgTopTable.setStatus("mandatory")
_LpEth100LtPrtCfgTopEntry_Object = MibTableRow
lpEth100LtPrtCfgTopEntry = _LpEth100LtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 10, 1)
)
lpEth100LtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgTopEntry.setStatus("mandatory")


class _LpEth100LtPrtCfgTData_Type(AsciiString):
    """Custom type lpEth100LtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtPrtCfgTData_Type.__name__ = "AsciiString"
_LpEth100LtPrtCfgTData_Object = MibTableColumn
lpEth100LtPrtCfgTData = _LpEth100LtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 4, 10, 1, 1),
    _LpEth100LtPrtCfgTData_Type()
)
lpEth100LtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtPrtCfgTData.setStatus("mandatory")
_LpEth100LtFb_ObjectIdentity = ObjectIdentity
lpEth100LtFb = _LpEth100LtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5)
)
_LpEth100LtFbRowStatusTable_Object = MibTable
lpEth100LtFbRowStatusTable = _LpEth100LtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbRowStatusTable.setStatus("mandatory")
_LpEth100LtFbRowStatusEntry_Object = MibTableRow
lpEth100LtFbRowStatusEntry = _LpEth100LtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 1, 1)
)
lpEth100LtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbRowStatus_Type = RowStatus
_LpEth100LtFbRowStatus_Object = MibTableColumn
lpEth100LtFbRowStatus = _LpEth100LtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 1, 1, 1),
    _LpEth100LtFbRowStatus_Type()
)
lpEth100LtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbRowStatus.setStatus("mandatory")
_LpEth100LtFbComponentName_Type = DisplayString
_LpEth100LtFbComponentName_Object = MibTableColumn
lpEth100LtFbComponentName = _LpEth100LtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 1, 1, 2),
    _LpEth100LtFbComponentName_Type()
)
lpEth100LtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbComponentName.setStatus("mandatory")
_LpEth100LtFbStorageType_Type = StorageType
_LpEth100LtFbStorageType_Object = MibTableColumn
lpEth100LtFbStorageType = _LpEth100LtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 1, 1, 4),
    _LpEth100LtFbStorageType_Type()
)
lpEth100LtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbStorageType.setStatus("mandatory")
_LpEth100LtFbIndex_Type = NonReplicated
_LpEth100LtFbIndex_Object = MibTableColumn
lpEth100LtFbIndex = _LpEth100LtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 1, 1, 10),
    _LpEth100LtFbIndex_Type()
)
lpEth100LtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbIndex.setStatus("mandatory")
_LpEth100LtFbTxInfo_ObjectIdentity = ObjectIdentity
lpEth100LtFbTxInfo = _LpEth100LtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2)
)
_LpEth100LtFbTxInfoRowStatusTable_Object = MibTable
lpEth100LtFbTxInfoRowStatusTable = _LpEth100LtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoRowStatusTable.setStatus("mandatory")
_LpEth100LtFbTxInfoRowStatusEntry_Object = MibTableRow
lpEth100LtFbTxInfoRowStatusEntry = _LpEth100LtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 1, 1)
)
lpEth100LtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbTxInfoRowStatus_Type = RowStatus
_LpEth100LtFbTxInfoRowStatus_Object = MibTableColumn
lpEth100LtFbTxInfoRowStatus = _LpEth100LtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 1, 1, 1),
    _LpEth100LtFbTxInfoRowStatus_Type()
)
lpEth100LtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoRowStatus.setStatus("mandatory")
_LpEth100LtFbTxInfoComponentName_Type = DisplayString
_LpEth100LtFbTxInfoComponentName_Object = MibTableColumn
lpEth100LtFbTxInfoComponentName = _LpEth100LtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 1, 1, 2),
    _LpEth100LtFbTxInfoComponentName_Type()
)
lpEth100LtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoComponentName.setStatus("mandatory")
_LpEth100LtFbTxInfoStorageType_Type = StorageType
_LpEth100LtFbTxInfoStorageType_Object = MibTableColumn
lpEth100LtFbTxInfoStorageType = _LpEth100LtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 1, 1, 4),
    _LpEth100LtFbTxInfoStorageType_Type()
)
lpEth100LtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoStorageType.setStatus("mandatory")
_LpEth100LtFbTxInfoIndex_Type = NonReplicated
_LpEth100LtFbTxInfoIndex_Object = MibTableColumn
lpEth100LtFbTxInfoIndex = _LpEth100LtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 1, 1, 10),
    _LpEth100LtFbTxInfoIndex_Type()
)
lpEth100LtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoIndex.setStatus("mandatory")
_LpEth100LtFbTxInfoTopTable_Object = MibTable
lpEth100LtFbTxInfoTopTable = _LpEth100LtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoTopTable.setStatus("mandatory")
_LpEth100LtFbTxInfoTopEntry_Object = MibTableRow
lpEth100LtFbTxInfoTopEntry = _LpEth100LtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 10, 1)
)
lpEth100LtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoTopEntry.setStatus("mandatory")


class _LpEth100LtFbTxInfoTData_Type(AsciiString):
    """Custom type lpEth100LtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbTxInfoTData_Type.__name__ = "AsciiString"
_LpEth100LtFbTxInfoTData_Object = MibTableColumn
lpEth100LtFbTxInfoTData = _LpEth100LtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 2, 10, 1, 1),
    _LpEth100LtFbTxInfoTData_Type()
)
lpEth100LtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbTxInfoTData.setStatus("mandatory")
_LpEth100LtFbFddiMac_ObjectIdentity = ObjectIdentity
lpEth100LtFbFddiMac = _LpEth100LtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3)
)
_LpEth100LtFbFddiMacRowStatusTable_Object = MibTable
lpEth100LtFbFddiMacRowStatusTable = _LpEth100LtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacRowStatusTable.setStatus("mandatory")
_LpEth100LtFbFddiMacRowStatusEntry_Object = MibTableRow
lpEth100LtFbFddiMacRowStatusEntry = _LpEth100LtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 1, 1)
)
lpEth100LtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbFddiMacRowStatus_Type = RowStatus
_LpEth100LtFbFddiMacRowStatus_Object = MibTableColumn
lpEth100LtFbFddiMacRowStatus = _LpEth100LtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 1, 1, 1),
    _LpEth100LtFbFddiMacRowStatus_Type()
)
lpEth100LtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacRowStatus.setStatus("mandatory")
_LpEth100LtFbFddiMacComponentName_Type = DisplayString
_LpEth100LtFbFddiMacComponentName_Object = MibTableColumn
lpEth100LtFbFddiMacComponentName = _LpEth100LtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 1, 1, 2),
    _LpEth100LtFbFddiMacComponentName_Type()
)
lpEth100LtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacComponentName.setStatus("mandatory")
_LpEth100LtFbFddiMacStorageType_Type = StorageType
_LpEth100LtFbFddiMacStorageType_Object = MibTableColumn
lpEth100LtFbFddiMacStorageType = _LpEth100LtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 1, 1, 4),
    _LpEth100LtFbFddiMacStorageType_Type()
)
lpEth100LtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacStorageType.setStatus("mandatory")
_LpEth100LtFbFddiMacIndex_Type = NonReplicated
_LpEth100LtFbFddiMacIndex_Object = MibTableColumn
lpEth100LtFbFddiMacIndex = _LpEth100LtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 1, 1, 10),
    _LpEth100LtFbFddiMacIndex_Type()
)
lpEth100LtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacIndex.setStatus("mandatory")
_LpEth100LtFbFddiMacTopTable_Object = MibTable
lpEth100LtFbFddiMacTopTable = _LpEth100LtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacTopTable.setStatus("mandatory")
_LpEth100LtFbFddiMacTopEntry_Object = MibTableRow
lpEth100LtFbFddiMacTopEntry = _LpEth100LtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 10, 1)
)
lpEth100LtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacTopEntry.setStatus("mandatory")


class _LpEth100LtFbFddiMacTData_Type(AsciiString):
    """Custom type lpEth100LtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbFddiMacTData_Type.__name__ = "AsciiString"
_LpEth100LtFbFddiMacTData_Object = MibTableColumn
lpEth100LtFbFddiMacTData = _LpEth100LtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 3, 10, 1, 1),
    _LpEth100LtFbFddiMacTData_Type()
)
lpEth100LtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbFddiMacTData.setStatus("mandatory")
_LpEth100LtFbMacEnet_ObjectIdentity = ObjectIdentity
lpEth100LtFbMacEnet = _LpEth100LtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4)
)
_LpEth100LtFbMacEnetRowStatusTable_Object = MibTable
lpEth100LtFbMacEnetRowStatusTable = _LpEth100LtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetRowStatusTable.setStatus("mandatory")
_LpEth100LtFbMacEnetRowStatusEntry_Object = MibTableRow
lpEth100LtFbMacEnetRowStatusEntry = _LpEth100LtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 1, 1)
)
lpEth100LtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbMacEnetRowStatus_Type = RowStatus
_LpEth100LtFbMacEnetRowStatus_Object = MibTableColumn
lpEth100LtFbMacEnetRowStatus = _LpEth100LtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 1, 1, 1),
    _LpEth100LtFbMacEnetRowStatus_Type()
)
lpEth100LtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetRowStatus.setStatus("mandatory")
_LpEth100LtFbMacEnetComponentName_Type = DisplayString
_LpEth100LtFbMacEnetComponentName_Object = MibTableColumn
lpEth100LtFbMacEnetComponentName = _LpEth100LtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 1, 1, 2),
    _LpEth100LtFbMacEnetComponentName_Type()
)
lpEth100LtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetComponentName.setStatus("mandatory")
_LpEth100LtFbMacEnetStorageType_Type = StorageType
_LpEth100LtFbMacEnetStorageType_Object = MibTableColumn
lpEth100LtFbMacEnetStorageType = _LpEth100LtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 1, 1, 4),
    _LpEth100LtFbMacEnetStorageType_Type()
)
lpEth100LtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetStorageType.setStatus("mandatory")
_LpEth100LtFbMacEnetIndex_Type = NonReplicated
_LpEth100LtFbMacEnetIndex_Object = MibTableColumn
lpEth100LtFbMacEnetIndex = _LpEth100LtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 1, 1, 10),
    _LpEth100LtFbMacEnetIndex_Type()
)
lpEth100LtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetIndex.setStatus("mandatory")
_LpEth100LtFbMacEnetTopTable_Object = MibTable
lpEth100LtFbMacEnetTopTable = _LpEth100LtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetTopTable.setStatus("mandatory")
_LpEth100LtFbMacEnetTopEntry_Object = MibTableRow
lpEth100LtFbMacEnetTopEntry = _LpEth100LtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 10, 1)
)
lpEth100LtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetTopEntry.setStatus("mandatory")


class _LpEth100LtFbMacEnetTData_Type(AsciiString):
    """Custom type lpEth100LtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbMacEnetTData_Type.__name__ = "AsciiString"
_LpEth100LtFbMacEnetTData_Object = MibTableColumn
lpEth100LtFbMacEnetTData = _LpEth100LtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 4, 10, 1, 1),
    _LpEth100LtFbMacEnetTData_Type()
)
lpEth100LtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbMacEnetTData.setStatus("mandatory")
_LpEth100LtFbMacTr_ObjectIdentity = ObjectIdentity
lpEth100LtFbMacTr = _LpEth100LtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5)
)
_LpEth100LtFbMacTrRowStatusTable_Object = MibTable
lpEth100LtFbMacTrRowStatusTable = _LpEth100LtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrRowStatusTable.setStatus("mandatory")
_LpEth100LtFbMacTrRowStatusEntry_Object = MibTableRow
lpEth100LtFbMacTrRowStatusEntry = _LpEth100LtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 1, 1)
)
lpEth100LtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbMacTrRowStatus_Type = RowStatus
_LpEth100LtFbMacTrRowStatus_Object = MibTableColumn
lpEth100LtFbMacTrRowStatus = _LpEth100LtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 1, 1, 1),
    _LpEth100LtFbMacTrRowStatus_Type()
)
lpEth100LtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrRowStatus.setStatus("mandatory")
_LpEth100LtFbMacTrComponentName_Type = DisplayString
_LpEth100LtFbMacTrComponentName_Object = MibTableColumn
lpEth100LtFbMacTrComponentName = _LpEth100LtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 1, 1, 2),
    _LpEth100LtFbMacTrComponentName_Type()
)
lpEth100LtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrComponentName.setStatus("mandatory")
_LpEth100LtFbMacTrStorageType_Type = StorageType
_LpEth100LtFbMacTrStorageType_Object = MibTableColumn
lpEth100LtFbMacTrStorageType = _LpEth100LtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 1, 1, 4),
    _LpEth100LtFbMacTrStorageType_Type()
)
lpEth100LtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrStorageType.setStatus("mandatory")
_LpEth100LtFbMacTrIndex_Type = NonReplicated
_LpEth100LtFbMacTrIndex_Object = MibTableColumn
lpEth100LtFbMacTrIndex = _LpEth100LtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 1, 1, 10),
    _LpEth100LtFbMacTrIndex_Type()
)
lpEth100LtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrIndex.setStatus("mandatory")
_LpEth100LtFbMacTrTopTable_Object = MibTable
lpEth100LtFbMacTrTopTable = _LpEth100LtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrTopTable.setStatus("mandatory")
_LpEth100LtFbMacTrTopEntry_Object = MibTableRow
lpEth100LtFbMacTrTopEntry = _LpEth100LtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 10, 1)
)
lpEth100LtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrTopEntry.setStatus("mandatory")


class _LpEth100LtFbMacTrTData_Type(AsciiString):
    """Custom type lpEth100LtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbMacTrTData_Type.__name__ = "AsciiString"
_LpEth100LtFbMacTrTData_Object = MibTableColumn
lpEth100LtFbMacTrTData = _LpEth100LtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 5, 10, 1, 1),
    _LpEth100LtFbMacTrTData_Type()
)
lpEth100LtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbMacTrTData.setStatus("mandatory")
_LpEth100LtFbData_ObjectIdentity = ObjectIdentity
lpEth100LtFbData = _LpEth100LtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6)
)
_LpEth100LtFbDataRowStatusTable_Object = MibTable
lpEth100LtFbDataRowStatusTable = _LpEth100LtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbDataRowStatusTable.setStatus("mandatory")
_LpEth100LtFbDataRowStatusEntry_Object = MibTableRow
lpEth100LtFbDataRowStatusEntry = _LpEth100LtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 1, 1)
)
lpEth100LtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbDataRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbDataRowStatus_Type = RowStatus
_LpEth100LtFbDataRowStatus_Object = MibTableColumn
lpEth100LtFbDataRowStatus = _LpEth100LtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 1, 1, 1),
    _LpEth100LtFbDataRowStatus_Type()
)
lpEth100LtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbDataRowStatus.setStatus("mandatory")
_LpEth100LtFbDataComponentName_Type = DisplayString
_LpEth100LtFbDataComponentName_Object = MibTableColumn
lpEth100LtFbDataComponentName = _LpEth100LtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 1, 1, 2),
    _LpEth100LtFbDataComponentName_Type()
)
lpEth100LtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbDataComponentName.setStatus("mandatory")
_LpEth100LtFbDataStorageType_Type = StorageType
_LpEth100LtFbDataStorageType_Object = MibTableColumn
lpEth100LtFbDataStorageType = _LpEth100LtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 1, 1, 4),
    _LpEth100LtFbDataStorageType_Type()
)
lpEth100LtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbDataStorageType.setStatus("mandatory")
_LpEth100LtFbDataIndex_Type = NonReplicated
_LpEth100LtFbDataIndex_Object = MibTableColumn
lpEth100LtFbDataIndex = _LpEth100LtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 1, 1, 10),
    _LpEth100LtFbDataIndex_Type()
)
lpEth100LtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbDataIndex.setStatus("mandatory")
_LpEth100LtFbDataTopTable_Object = MibTable
lpEth100LtFbDataTopTable = _LpEth100LtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbDataTopTable.setStatus("mandatory")
_LpEth100LtFbDataTopEntry_Object = MibTableRow
lpEth100LtFbDataTopEntry = _LpEth100LtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 10, 1)
)
lpEth100LtFbDataTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbDataIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbDataTopEntry.setStatus("mandatory")


class _LpEth100LtFbDataTData_Type(AsciiString):
    """Custom type lpEth100LtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbDataTData_Type.__name__ = "AsciiString"
_LpEth100LtFbDataTData_Object = MibTableColumn
lpEth100LtFbDataTData = _LpEth100LtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 6, 10, 1, 1),
    _LpEth100LtFbDataTData_Type()
)
lpEth100LtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbDataTData.setStatus("mandatory")
_LpEth100LtFbIpH_ObjectIdentity = ObjectIdentity
lpEth100LtFbIpH = _LpEth100LtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7)
)
_LpEth100LtFbIpHRowStatusTable_Object = MibTable
lpEth100LtFbIpHRowStatusTable = _LpEth100LtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpHRowStatusTable.setStatus("mandatory")
_LpEth100LtFbIpHRowStatusEntry_Object = MibTableRow
lpEth100LtFbIpHRowStatusEntry = _LpEth100LtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 1, 1)
)
lpEth100LtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpHRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbIpHRowStatus_Type = RowStatus
_LpEth100LtFbIpHRowStatus_Object = MibTableColumn
lpEth100LtFbIpHRowStatus = _LpEth100LtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 1, 1, 1),
    _LpEth100LtFbIpHRowStatus_Type()
)
lpEth100LtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbIpHRowStatus.setStatus("mandatory")
_LpEth100LtFbIpHComponentName_Type = DisplayString
_LpEth100LtFbIpHComponentName_Object = MibTableColumn
lpEth100LtFbIpHComponentName = _LpEth100LtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 1, 1, 2),
    _LpEth100LtFbIpHComponentName_Type()
)
lpEth100LtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbIpHComponentName.setStatus("mandatory")
_LpEth100LtFbIpHStorageType_Type = StorageType
_LpEth100LtFbIpHStorageType_Object = MibTableColumn
lpEth100LtFbIpHStorageType = _LpEth100LtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 1, 1, 4),
    _LpEth100LtFbIpHStorageType_Type()
)
lpEth100LtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbIpHStorageType.setStatus("mandatory")
_LpEth100LtFbIpHIndex_Type = NonReplicated
_LpEth100LtFbIpHIndex_Object = MibTableColumn
lpEth100LtFbIpHIndex = _LpEth100LtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 1, 1, 10),
    _LpEth100LtFbIpHIndex_Type()
)
lpEth100LtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbIpHIndex.setStatus("mandatory")
_LpEth100LtFbIpHTopTable_Object = MibTable
lpEth100LtFbIpHTopTable = _LpEth100LtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpHTopTable.setStatus("mandatory")
_LpEth100LtFbIpHTopEntry_Object = MibTableRow
lpEth100LtFbIpHTopEntry = _LpEth100LtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 10, 1)
)
lpEth100LtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpHTopEntry.setStatus("mandatory")


class _LpEth100LtFbIpHTData_Type(AsciiString):
    """Custom type lpEth100LtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbIpHTData_Type.__name__ = "AsciiString"
_LpEth100LtFbIpHTData_Object = MibTableColumn
lpEth100LtFbIpHTData = _LpEth100LtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 7, 10, 1, 1),
    _LpEth100LtFbIpHTData_Type()
)
lpEth100LtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbIpHTData.setStatus("mandatory")
_LpEth100LtFbLlch_ObjectIdentity = ObjectIdentity
lpEth100LtFbLlch = _LpEth100LtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8)
)
_LpEth100LtFbLlchRowStatusTable_Object = MibTable
lpEth100LtFbLlchRowStatusTable = _LpEth100LtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbLlchRowStatusTable.setStatus("mandatory")
_LpEth100LtFbLlchRowStatusEntry_Object = MibTableRow
lpEth100LtFbLlchRowStatusEntry = _LpEth100LtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 1, 1)
)
lpEth100LtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbLlchRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbLlchRowStatus_Type = RowStatus
_LpEth100LtFbLlchRowStatus_Object = MibTableColumn
lpEth100LtFbLlchRowStatus = _LpEth100LtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 1, 1, 1),
    _LpEth100LtFbLlchRowStatus_Type()
)
lpEth100LtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbLlchRowStatus.setStatus("mandatory")
_LpEth100LtFbLlchComponentName_Type = DisplayString
_LpEth100LtFbLlchComponentName_Object = MibTableColumn
lpEth100LtFbLlchComponentName = _LpEth100LtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 1, 1, 2),
    _LpEth100LtFbLlchComponentName_Type()
)
lpEth100LtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbLlchComponentName.setStatus("mandatory")
_LpEth100LtFbLlchStorageType_Type = StorageType
_LpEth100LtFbLlchStorageType_Object = MibTableColumn
lpEth100LtFbLlchStorageType = _LpEth100LtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 1, 1, 4),
    _LpEth100LtFbLlchStorageType_Type()
)
lpEth100LtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbLlchStorageType.setStatus("mandatory")
_LpEth100LtFbLlchIndex_Type = NonReplicated
_LpEth100LtFbLlchIndex_Object = MibTableColumn
lpEth100LtFbLlchIndex = _LpEth100LtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 1, 1, 10),
    _LpEth100LtFbLlchIndex_Type()
)
lpEth100LtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbLlchIndex.setStatus("mandatory")
_LpEth100LtFbLlchTopTable_Object = MibTable
lpEth100LtFbLlchTopTable = _LpEth100LtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbLlchTopTable.setStatus("mandatory")
_LpEth100LtFbLlchTopEntry_Object = MibTableRow
lpEth100LtFbLlchTopEntry = _LpEth100LtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 10, 1)
)
lpEth100LtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbLlchTopEntry.setStatus("mandatory")


class _LpEth100LtFbLlchTData_Type(AsciiString):
    """Custom type lpEth100LtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbLlchTData_Type.__name__ = "AsciiString"
_LpEth100LtFbLlchTData_Object = MibTableColumn
lpEth100LtFbLlchTData = _LpEth100LtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 8, 10, 1, 1),
    _LpEth100LtFbLlchTData_Type()
)
lpEth100LtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbLlchTData.setStatus("mandatory")
_LpEth100LtFbAppleH_ObjectIdentity = ObjectIdentity
lpEth100LtFbAppleH = _LpEth100LtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9)
)
_LpEth100LtFbAppleHRowStatusTable_Object = MibTable
lpEth100LtFbAppleHRowStatusTable = _LpEth100LtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHRowStatusTable.setStatus("mandatory")
_LpEth100LtFbAppleHRowStatusEntry_Object = MibTableRow
lpEth100LtFbAppleHRowStatusEntry = _LpEth100LtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 1, 1)
)
lpEth100LtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbAppleHRowStatus_Type = RowStatus
_LpEth100LtFbAppleHRowStatus_Object = MibTableColumn
lpEth100LtFbAppleHRowStatus = _LpEth100LtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 1, 1, 1),
    _LpEth100LtFbAppleHRowStatus_Type()
)
lpEth100LtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHRowStatus.setStatus("mandatory")
_LpEth100LtFbAppleHComponentName_Type = DisplayString
_LpEth100LtFbAppleHComponentName_Object = MibTableColumn
lpEth100LtFbAppleHComponentName = _LpEth100LtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 1, 1, 2),
    _LpEth100LtFbAppleHComponentName_Type()
)
lpEth100LtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHComponentName.setStatus("mandatory")
_LpEth100LtFbAppleHStorageType_Type = StorageType
_LpEth100LtFbAppleHStorageType_Object = MibTableColumn
lpEth100LtFbAppleHStorageType = _LpEth100LtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 1, 1, 4),
    _LpEth100LtFbAppleHStorageType_Type()
)
lpEth100LtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHStorageType.setStatus("mandatory")
_LpEth100LtFbAppleHIndex_Type = NonReplicated
_LpEth100LtFbAppleHIndex_Object = MibTableColumn
lpEth100LtFbAppleHIndex = _LpEth100LtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 1, 1, 10),
    _LpEth100LtFbAppleHIndex_Type()
)
lpEth100LtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHIndex.setStatus("mandatory")
_LpEth100LtFbAppleHTopTable_Object = MibTable
lpEth100LtFbAppleHTopTable = _LpEth100LtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHTopTable.setStatus("mandatory")
_LpEth100LtFbAppleHTopEntry_Object = MibTableRow
lpEth100LtFbAppleHTopEntry = _LpEth100LtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 10, 1)
)
lpEth100LtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHTopEntry.setStatus("mandatory")


class _LpEth100LtFbAppleHTData_Type(AsciiString):
    """Custom type lpEth100LtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbAppleHTData_Type.__name__ = "AsciiString"
_LpEth100LtFbAppleHTData_Object = MibTableColumn
lpEth100LtFbAppleHTData = _LpEth100LtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 9, 10, 1, 1),
    _LpEth100LtFbAppleHTData_Type()
)
lpEth100LtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbAppleHTData.setStatus("mandatory")
_LpEth100LtFbIpxH_ObjectIdentity = ObjectIdentity
lpEth100LtFbIpxH = _LpEth100LtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10)
)
_LpEth100LtFbIpxHRowStatusTable_Object = MibTable
lpEth100LtFbIpxHRowStatusTable = _LpEth100LtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHRowStatusTable.setStatus("mandatory")
_LpEth100LtFbIpxHRowStatusEntry_Object = MibTableRow
lpEth100LtFbIpxHRowStatusEntry = _LpEth100LtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 1, 1)
)
lpEth100LtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHRowStatusEntry.setStatus("mandatory")
_LpEth100LtFbIpxHRowStatus_Type = RowStatus
_LpEth100LtFbIpxHRowStatus_Object = MibTableColumn
lpEth100LtFbIpxHRowStatus = _LpEth100LtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 1, 1, 1),
    _LpEth100LtFbIpxHRowStatus_Type()
)
lpEth100LtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHRowStatus.setStatus("mandatory")
_LpEth100LtFbIpxHComponentName_Type = DisplayString
_LpEth100LtFbIpxHComponentName_Object = MibTableColumn
lpEth100LtFbIpxHComponentName = _LpEth100LtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 1, 1, 2),
    _LpEth100LtFbIpxHComponentName_Type()
)
lpEth100LtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHComponentName.setStatus("mandatory")
_LpEth100LtFbIpxHStorageType_Type = StorageType
_LpEth100LtFbIpxHStorageType_Object = MibTableColumn
lpEth100LtFbIpxHStorageType = _LpEth100LtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 1, 1, 4),
    _LpEth100LtFbIpxHStorageType_Type()
)
lpEth100LtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHStorageType.setStatus("mandatory")
_LpEth100LtFbIpxHIndex_Type = NonReplicated
_LpEth100LtFbIpxHIndex_Object = MibTableColumn
lpEth100LtFbIpxHIndex = _LpEth100LtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 1, 1, 10),
    _LpEth100LtFbIpxHIndex_Type()
)
lpEth100LtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHIndex.setStatus("mandatory")
_LpEth100LtFbIpxHTopTable_Object = MibTable
lpEth100LtFbIpxHTopTable = _LpEth100LtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHTopTable.setStatus("mandatory")
_LpEth100LtFbIpxHTopEntry_Object = MibTableRow
lpEth100LtFbIpxHTopEntry = _LpEth100LtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 10, 1)
)
lpEth100LtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHTopEntry.setStatus("mandatory")


class _LpEth100LtFbIpxHTData_Type(AsciiString):
    """Custom type lpEth100LtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbIpxHTData_Type.__name__ = "AsciiString"
_LpEth100LtFbIpxHTData_Object = MibTableColumn
lpEth100LtFbIpxHTData = _LpEth100LtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 10, 10, 1, 1),
    _LpEth100LtFbIpxHTData_Type()
)
lpEth100LtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbIpxHTData.setStatus("mandatory")
_LpEth100LtFbTopTable_Object = MibTable
lpEth100LtFbTopTable = _LpEth100LtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 20)
)
if mibBuilder.loadTexts:
    lpEth100LtFbTopTable.setStatus("mandatory")
_LpEth100LtFbTopEntry_Object = MibTableRow
lpEth100LtFbTopEntry = _LpEth100LtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 20, 1)
)
lpEth100LtFbTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtFbIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtFbTopEntry.setStatus("mandatory")


class _LpEth100LtFbTData_Type(AsciiString):
    """Custom type lpEth100LtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtFbTData_Type.__name__ = "AsciiString"
_LpEth100LtFbTData_Object = MibTableColumn
lpEth100LtFbTData = _LpEth100LtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 5, 20, 1, 1),
    _LpEth100LtFbTData_Type()
)
lpEth100LtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtFbTData.setStatus("mandatory")
_LpEth100LtCntl_ObjectIdentity = ObjectIdentity
lpEth100LtCntl = _LpEth100LtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6)
)
_LpEth100LtCntlRowStatusTable_Object = MibTable
lpEth100LtCntlRowStatusTable = _LpEth100LtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 1)
)
if mibBuilder.loadTexts:
    lpEth100LtCntlRowStatusTable.setStatus("mandatory")
_LpEth100LtCntlRowStatusEntry_Object = MibTableRow
lpEth100LtCntlRowStatusEntry = _LpEth100LtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 1, 1)
)
lpEth100LtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtCntlRowStatusEntry.setStatus("mandatory")
_LpEth100LtCntlRowStatus_Type = RowStatus
_LpEth100LtCntlRowStatus_Object = MibTableColumn
lpEth100LtCntlRowStatus = _LpEth100LtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 1, 1, 1),
    _LpEth100LtCntlRowStatus_Type()
)
lpEth100LtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtCntlRowStatus.setStatus("mandatory")
_LpEth100LtCntlComponentName_Type = DisplayString
_LpEth100LtCntlComponentName_Object = MibTableColumn
lpEth100LtCntlComponentName = _LpEth100LtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 1, 1, 2),
    _LpEth100LtCntlComponentName_Type()
)
lpEth100LtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtCntlComponentName.setStatus("mandatory")
_LpEth100LtCntlStorageType_Type = StorageType
_LpEth100LtCntlStorageType_Object = MibTableColumn
lpEth100LtCntlStorageType = _LpEth100LtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 1, 1, 4),
    _LpEth100LtCntlStorageType_Type()
)
lpEth100LtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LtCntlStorageType.setStatus("mandatory")
_LpEth100LtCntlIndex_Type = NonReplicated
_LpEth100LtCntlIndex_Object = MibTableColumn
lpEth100LtCntlIndex = _LpEth100LtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 1, 1, 10),
    _LpEth100LtCntlIndex_Type()
)
lpEth100LtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100LtCntlIndex.setStatus("mandatory")
_LpEth100LtCntlTopTable_Object = MibTable
lpEth100LtCntlTopTable = _LpEth100LtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 10)
)
if mibBuilder.loadTexts:
    lpEth100LtCntlTopTable.setStatus("mandatory")
_LpEth100LtCntlTopEntry_Object = MibTableRow
lpEth100LtCntlTopEntry = _LpEth100LtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 10, 1)
)
lpEth100LtCntlTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtCntlIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtCntlTopEntry.setStatus("mandatory")


class _LpEth100LtCntlTData_Type(AsciiString):
    """Custom type lpEth100LtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtCntlTData_Type.__name__ = "AsciiString"
_LpEth100LtCntlTData_Object = MibTableColumn
lpEth100LtCntlTData = _LpEth100LtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 6, 10, 1, 1),
    _LpEth100LtCntlTData_Type()
)
lpEth100LtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtCntlTData.setStatus("mandatory")
_LpEth100LtTopTable_Object = MibTable
lpEth100LtTopTable = _LpEth100LtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 20)
)
if mibBuilder.loadTexts:
    lpEth100LtTopTable.setStatus("mandatory")
_LpEth100LtTopEntry_Object = MibTableRow
lpEth100LtTopEntry = _LpEth100LtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 20, 1)
)
lpEth100LtTopEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100LtIndex"),
)
if mibBuilder.loadTexts:
    lpEth100LtTopEntry.setStatus("mandatory")


class _LpEth100LtTData_Type(AsciiString):
    """Custom type lpEth100LtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpEth100LtTData_Type.__name__ = "AsciiString"
_LpEth100LtTData_Object = MibTableColumn
lpEth100LtTData = _LpEth100LtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 2, 20, 1, 1),
    _LpEth100LtTData_Type()
)
lpEth100LtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LtTData.setStatus("mandatory")
_LpEth100Test_ObjectIdentity = ObjectIdentity
lpEth100Test = _LpEth100Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3)
)
_LpEth100TestRowStatusTable_Object = MibTable
lpEth100TestRowStatusTable = _LpEth100TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 1)
)
if mibBuilder.loadTexts:
    lpEth100TestRowStatusTable.setStatus("mandatory")
_LpEth100TestRowStatusEntry_Object = MibTableRow
lpEth100TestRowStatusEntry = _LpEth100TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 1, 1)
)
lpEth100TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100TestIndex"),
)
if mibBuilder.loadTexts:
    lpEth100TestRowStatusEntry.setStatus("mandatory")
_LpEth100TestRowStatus_Type = RowStatus
_LpEth100TestRowStatus_Object = MibTableColumn
lpEth100TestRowStatus = _LpEth100TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 1, 1, 1),
    _LpEth100TestRowStatus_Type()
)
lpEth100TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestRowStatus.setStatus("mandatory")
_LpEth100TestComponentName_Type = DisplayString
_LpEth100TestComponentName_Object = MibTableColumn
lpEth100TestComponentName = _LpEth100TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 1, 1, 2),
    _LpEth100TestComponentName_Type()
)
lpEth100TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestComponentName.setStatus("mandatory")
_LpEth100TestStorageType_Type = StorageType
_LpEth100TestStorageType_Object = MibTableColumn
lpEth100TestStorageType = _LpEth100TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 1, 1, 4),
    _LpEth100TestStorageType_Type()
)
lpEth100TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestStorageType.setStatus("mandatory")
_LpEth100TestIndex_Type = NonReplicated
_LpEth100TestIndex_Object = MibTableColumn
lpEth100TestIndex = _LpEth100TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 1, 1, 10),
    _LpEth100TestIndex_Type()
)
lpEth100TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEth100TestIndex.setStatus("mandatory")
_LpEth100TestPTOTable_Object = MibTable
lpEth100TestPTOTable = _LpEth100TestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 10)
)
if mibBuilder.loadTexts:
    lpEth100TestPTOTable.setStatus("mandatory")
_LpEth100TestPTOEntry_Object = MibTableRow
lpEth100TestPTOEntry = _LpEth100TestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 10, 1)
)
lpEth100TestPTOEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100TestIndex"),
)
if mibBuilder.loadTexts:
    lpEth100TestPTOEntry.setStatus("mandatory")


class _LpEth100TestType_Type(Integer32):
    """Custom type lpEth100TestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              257,
              258,
              259,
              260,
              263,
              264,
              265,
              266,
              267,
              268)
        )
    )
    namedValues = NamedValues(
        *(("extThruA", 265),
          ("extThruB", 266),
          ("extWrapA", 263),
          ("extWrapAB", 267),
          ("extWrapB", 264),
          ("extWrapBA", 268),
          ("normal", 1),
          ("onCard", 0),
          ("thruA", 259),
          ("thruB", 260),
          ("wrapA", 257),
          ("wrapB", 258))
    )


_LpEth100TestType_Type.__name__ = "Integer32"
_LpEth100TestType_Object = MibTableColumn
lpEth100TestType = _LpEth100TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 10, 1, 1),
    _LpEth100TestType_Type()
)
lpEth100TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100TestType.setStatus("mandatory")


class _LpEth100TestFrmSize_Type(Unsigned32):
    """Custom type lpEth100TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpEth100TestFrmSize_Type.__name__ = "Unsigned32"
_LpEth100TestFrmSize_Object = MibTableColumn
lpEth100TestFrmSize = _LpEth100TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 10, 1, 2),
    _LpEth100TestFrmSize_Type()
)
lpEth100TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100TestFrmSize.setStatus("mandatory")


class _LpEth100TestDuration_Type(Unsigned32):
    """Custom type lpEth100TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpEth100TestDuration_Type.__name__ = "Unsigned32"
_LpEth100TestDuration_Object = MibTableColumn
lpEth100TestDuration = _LpEth100TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 10, 1, 3),
    _LpEth100TestDuration_Type()
)
lpEth100TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100TestDuration.setStatus("mandatory")
_LpEth100TestResultsTable_Object = MibTable
lpEth100TestResultsTable = _LpEth100TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11)
)
if mibBuilder.loadTexts:
    lpEth100TestResultsTable.setStatus("mandatory")
_LpEth100TestResultsEntry_Object = MibTableRow
lpEth100TestResultsEntry = _LpEth100TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1)
)
lpEth100TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100TestIndex"),
)
if mibBuilder.loadTexts:
    lpEth100TestResultsEntry.setStatus("mandatory")
_LpEth100TestElapsedTime_Type = Counter32
_LpEth100TestElapsedTime_Object = MibTableColumn
lpEth100TestElapsedTime = _LpEth100TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 4),
    _LpEth100TestElapsedTime_Type()
)
lpEth100TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestElapsedTime.setStatus("mandatory")


class _LpEth100TestTimeRemaining_Type(Unsigned32):
    """Custom type lpEth100TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpEth100TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpEth100TestTimeRemaining_Object = MibTableColumn
lpEth100TestTimeRemaining = _LpEth100TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 5),
    _LpEth100TestTimeRemaining_Type()
)
lpEth100TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestTimeRemaining.setStatus("mandatory")


class _LpEth100TestCauseOfTermination_Type(Integer32):
    """Custom type lpEth100TestCauseOfTermination based on Integer32"""
    defaultValue = 3

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
        *(("neverStarted", 3),
          ("stoppedByOperator", 1),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_LpEth100TestCauseOfTermination_Type.__name__ = "Integer32"
_LpEth100TestCauseOfTermination_Object = MibTableColumn
lpEth100TestCauseOfTermination = _LpEth100TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 6),
    _LpEth100TestCauseOfTermination_Type()
)
lpEth100TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestCauseOfTermination.setStatus("mandatory")
_LpEth100TestFrmTx_Type = PassportCounter64
_LpEth100TestFrmTx_Object = MibTableColumn
lpEth100TestFrmTx = _LpEth100TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 7),
    _LpEth100TestFrmTx_Type()
)
lpEth100TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestFrmTx.setStatus("mandatory")
_LpEth100TestBitsTx_Type = PassportCounter64
_LpEth100TestBitsTx_Object = MibTableColumn
lpEth100TestBitsTx = _LpEth100TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 8),
    _LpEth100TestBitsTx_Type()
)
lpEth100TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestBitsTx.setStatus("mandatory")
_LpEth100TestFrmRx_Type = PassportCounter64
_LpEth100TestFrmRx_Object = MibTableColumn
lpEth100TestFrmRx = _LpEth100TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 9),
    _LpEth100TestFrmRx_Type()
)
lpEth100TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestFrmRx.setStatus("mandatory")
_LpEth100TestBitsRx_Type = PassportCounter64
_LpEth100TestBitsRx_Object = MibTableColumn
lpEth100TestBitsRx = _LpEth100TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 10),
    _LpEth100TestBitsRx_Type()
)
lpEth100TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestBitsRx.setStatus("mandatory")
_LpEth100TestErroredFrmRx_Type = PassportCounter64
_LpEth100TestErroredFrmRx_Object = MibTableColumn
lpEth100TestErroredFrmRx = _LpEth100TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 3, 11, 1, 11),
    _LpEth100TestErroredFrmRx_Type()
)
lpEth100TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100TestErroredFrmRx.setStatus("mandatory")
_LpEth100CidDataTable_Object = MibTable
lpEth100CidDataTable = _LpEth100CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 10)
)
if mibBuilder.loadTexts:
    lpEth100CidDataTable.setStatus("mandatory")
_LpEth100CidDataEntry_Object = MibTableRow
lpEth100CidDataEntry = _LpEth100CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 10, 1)
)
lpEth100CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100CidDataEntry.setStatus("mandatory")


class _LpEth100CustomerIdentifier_Type(Unsigned32):
    """Custom type lpEth100CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpEth100CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpEth100CustomerIdentifier_Object = MibTableColumn
lpEth100CustomerIdentifier = _LpEth100CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 10, 1, 1),
    _LpEth100CustomerIdentifier_Type()
)
lpEth100CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100CustomerIdentifier.setStatus("mandatory")
_LpEth100IfEntryTable_Object = MibTable
lpEth100IfEntryTable = _LpEth100IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 11)
)
if mibBuilder.loadTexts:
    lpEth100IfEntryTable.setStatus("mandatory")
_LpEth100IfEntryEntry_Object = MibTableRow
lpEth100IfEntryEntry = _LpEth100IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 11, 1)
)
lpEth100IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100IfEntryEntry.setStatus("mandatory")


class _LpEth100IfAdminStatus_Type(Integer32):
    """Custom type lpEth100IfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpEth100IfAdminStatus_Type.__name__ = "Integer32"
_LpEth100IfAdminStatus_Object = MibTableColumn
lpEth100IfAdminStatus = _LpEth100IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 11, 1, 1),
    _LpEth100IfAdminStatus_Type()
)
lpEth100IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100IfAdminStatus.setStatus("mandatory")


class _LpEth100IfIndex_Type(InterfaceIndex):
    """Custom type lpEth100IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpEth100IfIndex_Type.__name__ = "InterfaceIndex"
_LpEth100IfIndex_Object = MibTableColumn
lpEth100IfIndex = _LpEth100IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 11, 1, 2),
    _LpEth100IfIndex_Type()
)
lpEth100IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100IfIndex.setStatus("mandatory")
_LpEth100ProvTable_Object = MibTable
lpEth100ProvTable = _LpEth100ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 12)
)
if mibBuilder.loadTexts:
    lpEth100ProvTable.setStatus("mandatory")
_LpEth100ProvEntry_Object = MibTableRow
lpEth100ProvEntry = _LpEth100ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 12, 1)
)
lpEth100ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100ProvEntry.setStatus("mandatory")


class _LpEth100DuplexMode_Type(Integer32):
    """Custom type lpEth100DuplexMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_LpEth100DuplexMode_Type.__name__ = "Integer32"
_LpEth100DuplexMode_Object = MibTableColumn
lpEth100DuplexMode = _LpEth100DuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 12, 1, 1),
    _LpEth100DuplexMode_Type()
)
lpEth100DuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100DuplexMode.setStatus("mandatory")


class _LpEth100LineSpeed_Type(Unsigned32):
    """Custom type lpEth100LineSpeed based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_LpEth100LineSpeed_Type.__name__ = "Unsigned32"
_LpEth100LineSpeed_Object = MibTableColumn
lpEth100LineSpeed = _LpEth100LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 12, 1, 2),
    _LpEth100LineSpeed_Type()
)
lpEth100LineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100LineSpeed.setStatus("mandatory")


class _LpEth100AutoNegotiation_Type(Integer32):
    """Custom type lpEth100AutoNegotiation based on Integer32"""
    defaultValue = 1

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


_LpEth100AutoNegotiation_Type.__name__ = "Integer32"
_LpEth100AutoNegotiation_Object = MibTableColumn
lpEth100AutoNegotiation = _LpEth100AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 12, 1, 3),
    _LpEth100AutoNegotiation_Type()
)
lpEth100AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100AutoNegotiation.setStatus("mandatory")
_LpEth100ApplicationFramerName_Type = Link
_LpEth100ApplicationFramerName_Object = MibTableColumn
lpEth100ApplicationFramerName = _LpEth100ApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 12, 1, 4),
    _LpEth100ApplicationFramerName_Type()
)
lpEth100ApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100ApplicationFramerName.setStatus("mandatory")
_LpEth100AdminInfoTable_Object = MibTable
lpEth100AdminInfoTable = _LpEth100AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 13)
)
if mibBuilder.loadTexts:
    lpEth100AdminInfoTable.setStatus("mandatory")
_LpEth100AdminInfoEntry_Object = MibTableRow
lpEth100AdminInfoEntry = _LpEth100AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 13, 1)
)
lpEth100AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100AdminInfoEntry.setStatus("mandatory")


class _LpEth100Vendor_Type(AsciiString):
    """Custom type lpEth100Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpEth100Vendor_Type.__name__ = "AsciiString"
_LpEth100Vendor_Object = MibTableColumn
lpEth100Vendor = _LpEth100Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 13, 1, 1),
    _LpEth100Vendor_Type()
)
lpEth100Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100Vendor.setStatus("mandatory")


class _LpEth100CommentText_Type(AsciiString):
    """Custom type lpEth100CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpEth100CommentText_Type.__name__ = "AsciiString"
_LpEth100CommentText_Object = MibTableColumn
lpEth100CommentText = _LpEth100CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 13, 1, 2),
    _LpEth100CommentText_Type()
)
lpEth100CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEth100CommentText.setStatus("mandatory")
_LpEth100StateTable_Object = MibTable
lpEth100StateTable = _LpEth100StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 15)
)
if mibBuilder.loadTexts:
    lpEth100StateTable.setStatus("mandatory")
_LpEth100StateEntry_Object = MibTableRow
lpEth100StateEntry = _LpEth100StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 15, 1)
)
lpEth100StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100StateEntry.setStatus("mandatory")


class _LpEth100AdminState_Type(Integer32):
    """Custom type lpEth100AdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_LpEth100AdminState_Type.__name__ = "Integer32"
_LpEth100AdminState_Object = MibTableColumn
lpEth100AdminState = _LpEth100AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 15, 1, 1),
    _LpEth100AdminState_Type()
)
lpEth100AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100AdminState.setStatus("mandatory")


class _LpEth100OperationalState_Type(Integer32):
    """Custom type lpEth100OperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LpEth100OperationalState_Type.__name__ = "Integer32"
_LpEth100OperationalState_Object = MibTableColumn
lpEth100OperationalState = _LpEth100OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 15, 1, 2),
    _LpEth100OperationalState_Type()
)
lpEth100OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100OperationalState.setStatus("mandatory")


class _LpEth100UsageState_Type(Integer32):
    """Custom type lpEth100UsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_LpEth100UsageState_Type.__name__ = "Integer32"
_LpEth100UsageState_Object = MibTableColumn
lpEth100UsageState = _LpEth100UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 15, 1, 3),
    _LpEth100UsageState_Type()
)
lpEth100UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100UsageState.setStatus("mandatory")
_LpEth100OperStatusTable_Object = MibTable
lpEth100OperStatusTable = _LpEth100OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 16)
)
if mibBuilder.loadTexts:
    lpEth100OperStatusTable.setStatus("mandatory")
_LpEth100OperStatusEntry_Object = MibTableRow
lpEth100OperStatusEntry = _LpEth100OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 16, 1)
)
lpEth100OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100OperStatusEntry.setStatus("mandatory")


class _LpEth100SnmpOperStatus_Type(Integer32):
    """Custom type lpEth100SnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpEth100SnmpOperStatus_Type.__name__ = "Integer32"
_LpEth100SnmpOperStatus_Object = MibTableColumn
lpEth100SnmpOperStatus = _LpEth100SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 16, 1, 1),
    _LpEth100SnmpOperStatus_Type()
)
lpEth100SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100SnmpOperStatus.setStatus("mandatory")
_LpEth100OperTable_Object = MibTable
lpEth100OperTable = _LpEth100OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 17)
)
if mibBuilder.loadTexts:
    lpEth100OperTable.setStatus("mandatory")
_LpEth100OperEntry_Object = MibTableRow
lpEth100OperEntry = _LpEth100OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 17, 1)
)
lpEth100OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100OperEntry.setStatus("mandatory")


class _LpEth100MacAddress_Type(MacAddress):
    """Custom type lpEth100MacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpEth100MacAddress_Type.__name__ = "MacAddress"
_LpEth100MacAddress_Object = MibTableColumn
lpEth100MacAddress = _LpEth100MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 17, 1, 1),
    _LpEth100MacAddress_Type()
)
lpEth100MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100MacAddress.setStatus("mandatory")


class _LpEth100AutoNegStatus_Type(Integer32):
    """Custom type lpEth100AutoNegStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("failed", 2),
          ("succeeded", 1))
    )


_LpEth100AutoNegStatus_Type.__name__ = "Integer32"
_LpEth100AutoNegStatus_Object = MibTableColumn
lpEth100AutoNegStatus = _LpEth100AutoNegStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 17, 1, 4),
    _LpEth100AutoNegStatus_Type()
)
lpEth100AutoNegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100AutoNegStatus.setStatus("mandatory")


class _LpEth100ActualLineSpeed_Type(Unsigned32):
    """Custom type lpEth100ActualLineSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_LpEth100ActualLineSpeed_Type.__name__ = "Unsigned32"
_LpEth100ActualLineSpeed_Object = MibTableColumn
lpEth100ActualLineSpeed = _LpEth100ActualLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 17, 1, 5),
    _LpEth100ActualLineSpeed_Type()
)
lpEth100ActualLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100ActualLineSpeed.setStatus("mandatory")


class _LpEth100ActualDuplexMode_Type(Integer32):
    """Custom type lpEth100ActualDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1))
    )


_LpEth100ActualDuplexMode_Type.__name__ = "Integer32"
_LpEth100ActualDuplexMode_Object = MibTableColumn
lpEth100ActualDuplexMode = _LpEth100ActualDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 17, 1, 6),
    _LpEth100ActualDuplexMode_Type()
)
lpEth100ActualDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100ActualDuplexMode.setStatus("mandatory")
_LpEth100Eth100StatsTable_Object = MibTable
lpEth100Eth100StatsTable = _LpEth100Eth100StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18)
)
if mibBuilder.loadTexts:
    lpEth100Eth100StatsTable.setStatus("mandatory")
_LpEth100Eth100StatsEntry_Object = MibTableRow
lpEth100Eth100StatsEntry = _LpEth100Eth100StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1)
)
lpEth100Eth100StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100Eth100StatsEntry.setStatus("mandatory")
_LpEth100FramesTransmittedOk_Type = Counter32
_LpEth100FramesTransmittedOk_Object = MibTableColumn
lpEth100FramesTransmittedOk = _LpEth100FramesTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1, 1),
    _LpEth100FramesTransmittedOk_Type()
)
lpEth100FramesTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100FramesTransmittedOk.setStatus("mandatory")
_LpEth100FramesReceivedOk_Type = Counter32
_LpEth100FramesReceivedOk_Object = MibTableColumn
lpEth100FramesReceivedOk = _LpEth100FramesReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1, 2),
    _LpEth100FramesReceivedOk_Type()
)
lpEth100FramesReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100FramesReceivedOk.setStatus("mandatory")
_LpEth100OctetsTransmittedOk_Type = Counter32
_LpEth100OctetsTransmittedOk_Object = MibTableColumn
lpEth100OctetsTransmittedOk = _LpEth100OctetsTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1, 3),
    _LpEth100OctetsTransmittedOk_Type()
)
lpEth100OctetsTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100OctetsTransmittedOk.setStatus("mandatory")
_LpEth100OctetsReceivedOk_Type = Counter32
_LpEth100OctetsReceivedOk_Object = MibTableColumn
lpEth100OctetsReceivedOk = _LpEth100OctetsReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1, 4),
    _LpEth100OctetsReceivedOk_Type()
)
lpEth100OctetsReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100OctetsReceivedOk.setStatus("mandatory")
_LpEth100UndersizeFrames_Type = Counter32
_LpEth100UndersizeFrames_Object = MibTableColumn
lpEth100UndersizeFrames = _LpEth100UndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1, 5),
    _LpEth100UndersizeFrames_Type()
)
lpEth100UndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100UndersizeFrames.setStatus("mandatory")
_LpEth100ReceivedOctetsIntoRouterBr_Type = Counter32
_LpEth100ReceivedOctetsIntoRouterBr_Object = MibTableColumn
lpEth100ReceivedOctetsIntoRouterBr = _LpEth100ReceivedOctetsIntoRouterBr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1, 6),
    _LpEth100ReceivedOctetsIntoRouterBr_Type()
)
lpEth100ReceivedOctetsIntoRouterBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100ReceivedOctetsIntoRouterBr.setStatus("mandatory")
_LpEth100ReceivedFramesIntoRouterBr_Type = Counter32
_LpEth100ReceivedFramesIntoRouterBr_Object = MibTableColumn
lpEth100ReceivedFramesIntoRouterBr = _LpEth100ReceivedFramesIntoRouterBr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 18, 1, 7),
    _LpEth100ReceivedFramesIntoRouterBr_Type()
)
lpEth100ReceivedFramesIntoRouterBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100ReceivedFramesIntoRouterBr.setStatus("mandatory")
_LpEth100StatsTable_Object = MibTable
lpEth100StatsTable = _LpEth100StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19)
)
if mibBuilder.loadTexts:
    lpEth100StatsTable.setStatus("mandatory")
_LpEth100StatsEntry_Object = MibTableRow
lpEth100StatsEntry = _LpEth100StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1)
)
lpEth100StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "lpEth100Index"),
)
if mibBuilder.loadTexts:
    lpEth100StatsEntry.setStatus("mandatory")
_LpEth100AlignmentErrors_Type = Counter32
_LpEth100AlignmentErrors_Object = MibTableColumn
lpEth100AlignmentErrors = _LpEth100AlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 2),
    _LpEth100AlignmentErrors_Type()
)
lpEth100AlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100AlignmentErrors.setStatus("mandatory")
_LpEth100FcsErrors_Type = Counter32
_LpEth100FcsErrors_Object = MibTableColumn
lpEth100FcsErrors = _LpEth100FcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 3),
    _LpEth100FcsErrors_Type()
)
lpEth100FcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100FcsErrors.setStatus("mandatory")
_LpEth100SingleCollisionFrames_Type = Counter32
_LpEth100SingleCollisionFrames_Object = MibTableColumn
lpEth100SingleCollisionFrames = _LpEth100SingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 4),
    _LpEth100SingleCollisionFrames_Type()
)
lpEth100SingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100SingleCollisionFrames.setStatus("mandatory")
_LpEth100MultipleCollisionFrames_Type = Counter32
_LpEth100MultipleCollisionFrames_Object = MibTableColumn
lpEth100MultipleCollisionFrames = _LpEth100MultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 5),
    _LpEth100MultipleCollisionFrames_Type()
)
lpEth100MultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100MultipleCollisionFrames.setStatus("mandatory")
_LpEth100SqeTestErrors_Type = Counter32
_LpEth100SqeTestErrors_Object = MibTableColumn
lpEth100SqeTestErrors = _LpEth100SqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 6),
    _LpEth100SqeTestErrors_Type()
)
lpEth100SqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100SqeTestErrors.setStatus("mandatory")
_LpEth100DeferredTransmissions_Type = Counter32
_LpEth100DeferredTransmissions_Object = MibTableColumn
lpEth100DeferredTransmissions = _LpEth100DeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 7),
    _LpEth100DeferredTransmissions_Type()
)
lpEth100DeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100DeferredTransmissions.setStatus("mandatory")
_LpEth100LateCollisions_Type = Counter32
_LpEth100LateCollisions_Object = MibTableColumn
lpEth100LateCollisions = _LpEth100LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 8),
    _LpEth100LateCollisions_Type()
)
lpEth100LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100LateCollisions.setStatus("mandatory")
_LpEth100ExcessiveCollisions_Type = Counter32
_LpEth100ExcessiveCollisions_Object = MibTableColumn
lpEth100ExcessiveCollisions = _LpEth100ExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 9),
    _LpEth100ExcessiveCollisions_Type()
)
lpEth100ExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100ExcessiveCollisions.setStatus("mandatory")
_LpEth100MacTransmitErrors_Type = Counter32
_LpEth100MacTransmitErrors_Object = MibTableColumn
lpEth100MacTransmitErrors = _LpEth100MacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 10),
    _LpEth100MacTransmitErrors_Type()
)
lpEth100MacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100MacTransmitErrors.setStatus("mandatory")
_LpEth100CarrierSenseErrors_Type = Counter32
_LpEth100CarrierSenseErrors_Object = MibTableColumn
lpEth100CarrierSenseErrors = _LpEth100CarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 11),
    _LpEth100CarrierSenseErrors_Type()
)
lpEth100CarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100CarrierSenseErrors.setStatus("mandatory")
_LpEth100FrameTooLongs_Type = Counter32
_LpEth100FrameTooLongs_Object = MibTableColumn
lpEth100FrameTooLongs = _LpEth100FrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 12),
    _LpEth100FrameTooLongs_Type()
)
lpEth100FrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100FrameTooLongs.setStatus("mandatory")
_LpEth100MacReceiveErrors_Type = Counter32
_LpEth100MacReceiveErrors_Object = MibTableColumn
lpEth100MacReceiveErrors = _LpEth100MacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 25, 19, 1, 13),
    _LpEth100MacReceiveErrors_Type()
)
lpEth100MacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEth100MacReceiveErrors.setStatus("mandatory")
_La_ObjectIdentity = ObjectIdentity
la = _La_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105)
)
_LaRowStatusTable_Object = MibTable
laRowStatusTable = _LaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 1)
)
if mibBuilder.loadTexts:
    laRowStatusTable.setStatus("mandatory")
_LaRowStatusEntry_Object = MibTableRow
laRowStatusEntry = _LaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 1, 1)
)
laRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laRowStatusEntry.setStatus("mandatory")
_LaRowStatus_Type = RowStatus
_LaRowStatus_Object = MibTableColumn
laRowStatus = _LaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 1, 1, 1),
    _LaRowStatus_Type()
)
laRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laRowStatus.setStatus("mandatory")
_LaComponentName_Type = DisplayString
_LaComponentName_Object = MibTableColumn
laComponentName = _LaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 1, 1, 2),
    _LaComponentName_Type()
)
laComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laComponentName.setStatus("mandatory")
_LaStorageType_Type = StorageType
_LaStorageType_Object = MibTableColumn
laStorageType = _LaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 1, 1, 4),
    _LaStorageType_Type()
)
laStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laStorageType.setStatus("mandatory")


class _LaIndex_Type(Integer32):
    """Custom type laIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LaIndex_Type.__name__ = "Integer32"
_LaIndex_Object = MibTableColumn
laIndex = _LaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 1, 1, 10),
    _LaIndex_Type()
)
laIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    laIndex.setStatus("mandatory")
_LaFramer_ObjectIdentity = ObjectIdentity
laFramer = _LaFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2)
)
_LaFramerRowStatusTable_Object = MibTable
laFramerRowStatusTable = _LaFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 1)
)
if mibBuilder.loadTexts:
    laFramerRowStatusTable.setStatus("mandatory")
_LaFramerRowStatusEntry_Object = MibTableRow
laFramerRowStatusEntry = _LaFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 1, 1)
)
laFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laFramerIndex"),
)
if mibBuilder.loadTexts:
    laFramerRowStatusEntry.setStatus("mandatory")
_LaFramerRowStatus_Type = RowStatus
_LaFramerRowStatus_Object = MibTableColumn
laFramerRowStatus = _LaFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 1, 1, 1),
    _LaFramerRowStatus_Type()
)
laFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laFramerRowStatus.setStatus("mandatory")
_LaFramerComponentName_Type = DisplayString
_LaFramerComponentName_Object = MibTableColumn
laFramerComponentName = _LaFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 1, 1, 2),
    _LaFramerComponentName_Type()
)
laFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laFramerComponentName.setStatus("mandatory")
_LaFramerStorageType_Type = StorageType
_LaFramerStorageType_Object = MibTableColumn
laFramerStorageType = _LaFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 1, 1, 4),
    _LaFramerStorageType_Type()
)
laFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laFramerStorageType.setStatus("mandatory")
_LaFramerIndex_Type = NonReplicated
_LaFramerIndex_Object = MibTableColumn
laFramerIndex = _LaFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 1, 1, 10),
    _LaFramerIndex_Type()
)
laFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    laFramerIndex.setStatus("mandatory")
_LaFramerProvTable_Object = MibTable
laFramerProvTable = _LaFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 10)
)
if mibBuilder.loadTexts:
    laFramerProvTable.setStatus("mandatory")
_LaFramerProvEntry_Object = MibTableRow
laFramerProvEntry = _LaFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 10, 1)
)
laFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laFramerIndex"),
)
if mibBuilder.loadTexts:
    laFramerProvEntry.setStatus("mandatory")
_LaFramerInterfaceName_Type = Link
_LaFramerInterfaceName_Object = MibTableColumn
laFramerInterfaceName = _LaFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 10, 1, 1),
    _LaFramerInterfaceName_Type()
)
laFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laFramerInterfaceName.setStatus("obsolete")
_LaFramerInterfaceNamesTable_Object = MibTable
laFramerInterfaceNamesTable = _LaFramerInterfaceNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 431)
)
if mibBuilder.loadTexts:
    laFramerInterfaceNamesTable.setStatus("mandatory")
_LaFramerInterfaceNamesEntry_Object = MibTableRow
laFramerInterfaceNamesEntry = _LaFramerInterfaceNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 431, 1)
)
laFramerInterfaceNamesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laFramerIndex"),
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laFramerInterfaceNamesValue"),
)
if mibBuilder.loadTexts:
    laFramerInterfaceNamesEntry.setStatus("mandatory")
_LaFramerInterfaceNamesValue_Type = Link
_LaFramerInterfaceNamesValue_Object = MibTableColumn
laFramerInterfaceNamesValue = _LaFramerInterfaceNamesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 431, 1, 1),
    _LaFramerInterfaceNamesValue_Type()
)
laFramerInterfaceNamesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laFramerInterfaceNamesValue.setStatus("mandatory")
_LaFramerInterfaceNamesRowStatus_Type = RowStatus
_LaFramerInterfaceNamesRowStatus_Object = MibTableColumn
laFramerInterfaceNamesRowStatus = _LaFramerInterfaceNamesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 2, 431, 1, 2),
    _LaFramerInterfaceNamesRowStatus_Type()
)
laFramerInterfaceNamesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    laFramerInterfaceNamesRowStatus.setStatus("mandatory")
_LaCidDataTable_Object = MibTable
laCidDataTable = _LaCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 10)
)
if mibBuilder.loadTexts:
    laCidDataTable.setStatus("mandatory")
_LaCidDataEntry_Object = MibTableRow
laCidDataEntry = _LaCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 10, 1)
)
laCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laCidDataEntry.setStatus("mandatory")


class _LaCustomerIdentifier_Type(Unsigned32):
    """Custom type laCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LaCustomerIdentifier_Type.__name__ = "Unsigned32"
_LaCustomerIdentifier_Object = MibTableColumn
laCustomerIdentifier = _LaCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 10, 1, 1),
    _LaCustomerIdentifier_Type()
)
laCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laCustomerIdentifier.setStatus("mandatory")
_LaMediaProvTable_Object = MibTable
laMediaProvTable = _LaMediaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 11)
)
if mibBuilder.loadTexts:
    laMediaProvTable.setStatus("mandatory")
_LaMediaProvEntry_Object = MibTableRow
laMediaProvEntry = _LaMediaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 11, 1)
)
laMediaProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laMediaProvEntry.setStatus("mandatory")
_LaLinkToProtocolPort_Type = Link
_LaLinkToProtocolPort_Object = MibTableColumn
laLinkToProtocolPort = _LaLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 11, 1, 1),
    _LaLinkToProtocolPort_Type()
)
laLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laLinkToProtocolPort.setStatus("mandatory")
_LaIfEntryTable_Object = MibTable
laIfEntryTable = _LaIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 12)
)
if mibBuilder.loadTexts:
    laIfEntryTable.setStatus("mandatory")
_LaIfEntryEntry_Object = MibTableRow
laIfEntryEntry = _LaIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 12, 1)
)
laIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laIfEntryEntry.setStatus("mandatory")


class _LaIfAdminStatus_Type(Integer32):
    """Custom type laIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LaIfAdminStatus_Type.__name__ = "Integer32"
_LaIfAdminStatus_Object = MibTableColumn
laIfAdminStatus = _LaIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 12, 1, 1),
    _LaIfAdminStatus_Type()
)
laIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laIfAdminStatus.setStatus("mandatory")


class _LaIfIndex_Type(InterfaceIndex):
    """Custom type laIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LaIfIndex_Type.__name__ = "InterfaceIndex"
_LaIfIndex_Object = MibTableColumn
laIfIndex = _LaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 12, 1, 2),
    _LaIfIndex_Type()
)
laIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laIfIndex.setStatus("mandatory")
_LaStateTable_Object = MibTable
laStateTable = _LaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 13)
)
if mibBuilder.loadTexts:
    laStateTable.setStatus("mandatory")
_LaStateEntry_Object = MibTableRow
laStateEntry = _LaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 13, 1)
)
laStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laStateEntry.setStatus("mandatory")


class _LaAdminState_Type(Integer32):
    """Custom type laAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_LaAdminState_Type.__name__ = "Integer32"
_LaAdminState_Object = MibTableColumn
laAdminState = _LaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 13, 1, 1),
    _LaAdminState_Type()
)
laAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laAdminState.setStatus("mandatory")


class _LaOperationalState_Type(Integer32):
    """Custom type laOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LaOperationalState_Type.__name__ = "Integer32"
_LaOperationalState_Object = MibTableColumn
laOperationalState = _LaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 13, 1, 2),
    _LaOperationalState_Type()
)
laOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laOperationalState.setStatus("mandatory")


class _LaUsageState_Type(Integer32):
    """Custom type laUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_LaUsageState_Type.__name__ = "Integer32"
_LaUsageState_Object = MibTableColumn
laUsageState = _LaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 13, 1, 3),
    _LaUsageState_Type()
)
laUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laUsageState.setStatus("mandatory")
_LaOperStatusTable_Object = MibTable
laOperStatusTable = _LaOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 14)
)
if mibBuilder.loadTexts:
    laOperStatusTable.setStatus("mandatory")
_LaOperStatusEntry_Object = MibTableRow
laOperStatusEntry = _LaOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 14, 1)
)
laOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LanDriversMIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laOperStatusEntry.setStatus("mandatory")


class _LaSnmpOperStatus_Type(Integer32):
    """Custom type laSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LaSnmpOperStatus_Type.__name__ = "Integer32"
_LaSnmpOperStatus_Object = MibTableColumn
laSnmpOperStatus = _LaSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 105, 14, 1, 1),
    _LaSnmpOperStatus_Type()
)
laSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laSnmpOperStatus.setStatus("mandatory")
_LanDriversMIB_ObjectIdentity = ObjectIdentity
lanDriversMIB = _LanDriversMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30)
)
_LanDriversGroup_ObjectIdentity = ObjectIdentity
lanDriversGroup = _LanDriversGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 1)
)
_LanDriversGroupBE_ObjectIdentity = ObjectIdentity
lanDriversGroupBE = _LanDriversGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 1, 5)
)
_LanDriversGroupBE01_ObjectIdentity = ObjectIdentity
lanDriversGroupBE01 = _LanDriversGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 1, 5, 2)
)
_LanDriversGroupBE01A_ObjectIdentity = ObjectIdentity
lanDriversGroupBE01A = _LanDriversGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 1, 5, 2, 2)
)
_LanDriversCapabilities_ObjectIdentity = ObjectIdentity
lanDriversCapabilities = _LanDriversCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 3)
)
_LanDriversCapabilitiesBE_ObjectIdentity = ObjectIdentity
lanDriversCapabilitiesBE = _LanDriversCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 3, 5)
)
_LanDriversCapabilitiesBE01_ObjectIdentity = ObjectIdentity
lanDriversCapabilitiesBE01 = _LanDriversCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 3, 5, 2)
)
_LanDriversCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
lanDriversCapabilitiesBE01A = _LanDriversCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 30, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-LanDriversMIB",
    **{"lpEnet": lpEnet,
       "lpEnetRowStatusTable": lpEnetRowStatusTable,
       "lpEnetRowStatusEntry": lpEnetRowStatusEntry,
       "lpEnetRowStatus": lpEnetRowStatus,
       "lpEnetComponentName": lpEnetComponentName,
       "lpEnetStorageType": lpEnetStorageType,
       "lpEnetIndex": lpEnetIndex,
       "lpEnetLt": lpEnetLt,
       "lpEnetLtRowStatusTable": lpEnetLtRowStatusTable,
       "lpEnetLtRowStatusEntry": lpEnetLtRowStatusEntry,
       "lpEnetLtRowStatus": lpEnetLtRowStatus,
       "lpEnetLtComponentName": lpEnetLtComponentName,
       "lpEnetLtStorageType": lpEnetLtStorageType,
       "lpEnetLtIndex": lpEnetLtIndex,
       "lpEnetLtFrmCmp": lpEnetLtFrmCmp,
       "lpEnetLtFrmCmpRowStatusTable": lpEnetLtFrmCmpRowStatusTable,
       "lpEnetLtFrmCmpRowStatusEntry": lpEnetLtFrmCmpRowStatusEntry,
       "lpEnetLtFrmCmpRowStatus": lpEnetLtFrmCmpRowStatus,
       "lpEnetLtFrmCmpComponentName": lpEnetLtFrmCmpComponentName,
       "lpEnetLtFrmCmpStorageType": lpEnetLtFrmCmpStorageType,
       "lpEnetLtFrmCmpIndex": lpEnetLtFrmCmpIndex,
       "lpEnetLtFrmCmpTopTable": lpEnetLtFrmCmpTopTable,
       "lpEnetLtFrmCmpTopEntry": lpEnetLtFrmCmpTopEntry,
       "lpEnetLtFrmCmpTData": lpEnetLtFrmCmpTData,
       "lpEnetLtFrmCpy": lpEnetLtFrmCpy,
       "lpEnetLtFrmCpyRowStatusTable": lpEnetLtFrmCpyRowStatusTable,
       "lpEnetLtFrmCpyRowStatusEntry": lpEnetLtFrmCpyRowStatusEntry,
       "lpEnetLtFrmCpyRowStatus": lpEnetLtFrmCpyRowStatus,
       "lpEnetLtFrmCpyComponentName": lpEnetLtFrmCpyComponentName,
       "lpEnetLtFrmCpyStorageType": lpEnetLtFrmCpyStorageType,
       "lpEnetLtFrmCpyIndex": lpEnetLtFrmCpyIndex,
       "lpEnetLtFrmCpyTopTable": lpEnetLtFrmCpyTopTable,
       "lpEnetLtFrmCpyTopEntry": lpEnetLtFrmCpyTopEntry,
       "lpEnetLtFrmCpyTData": lpEnetLtFrmCpyTData,
       "lpEnetLtPrtCfg": lpEnetLtPrtCfg,
       "lpEnetLtPrtCfgRowStatusTable": lpEnetLtPrtCfgRowStatusTable,
       "lpEnetLtPrtCfgRowStatusEntry": lpEnetLtPrtCfgRowStatusEntry,
       "lpEnetLtPrtCfgRowStatus": lpEnetLtPrtCfgRowStatus,
       "lpEnetLtPrtCfgComponentName": lpEnetLtPrtCfgComponentName,
       "lpEnetLtPrtCfgStorageType": lpEnetLtPrtCfgStorageType,
       "lpEnetLtPrtCfgIndex": lpEnetLtPrtCfgIndex,
       "lpEnetLtPrtCfgTopTable": lpEnetLtPrtCfgTopTable,
       "lpEnetLtPrtCfgTopEntry": lpEnetLtPrtCfgTopEntry,
       "lpEnetLtPrtCfgTData": lpEnetLtPrtCfgTData,
       "lpEnetLtFb": lpEnetLtFb,
       "lpEnetLtFbRowStatusTable": lpEnetLtFbRowStatusTable,
       "lpEnetLtFbRowStatusEntry": lpEnetLtFbRowStatusEntry,
       "lpEnetLtFbRowStatus": lpEnetLtFbRowStatus,
       "lpEnetLtFbComponentName": lpEnetLtFbComponentName,
       "lpEnetLtFbStorageType": lpEnetLtFbStorageType,
       "lpEnetLtFbIndex": lpEnetLtFbIndex,
       "lpEnetLtFbTxInfo": lpEnetLtFbTxInfo,
       "lpEnetLtFbTxInfoRowStatusTable": lpEnetLtFbTxInfoRowStatusTable,
       "lpEnetLtFbTxInfoRowStatusEntry": lpEnetLtFbTxInfoRowStatusEntry,
       "lpEnetLtFbTxInfoRowStatus": lpEnetLtFbTxInfoRowStatus,
       "lpEnetLtFbTxInfoComponentName": lpEnetLtFbTxInfoComponentName,
       "lpEnetLtFbTxInfoStorageType": lpEnetLtFbTxInfoStorageType,
       "lpEnetLtFbTxInfoIndex": lpEnetLtFbTxInfoIndex,
       "lpEnetLtFbTxInfoTopTable": lpEnetLtFbTxInfoTopTable,
       "lpEnetLtFbTxInfoTopEntry": lpEnetLtFbTxInfoTopEntry,
       "lpEnetLtFbTxInfoTData": lpEnetLtFbTxInfoTData,
       "lpEnetLtFbFddiMac": lpEnetLtFbFddiMac,
       "lpEnetLtFbFddiMacRowStatusTable": lpEnetLtFbFddiMacRowStatusTable,
       "lpEnetLtFbFddiMacRowStatusEntry": lpEnetLtFbFddiMacRowStatusEntry,
       "lpEnetLtFbFddiMacRowStatus": lpEnetLtFbFddiMacRowStatus,
       "lpEnetLtFbFddiMacComponentName": lpEnetLtFbFddiMacComponentName,
       "lpEnetLtFbFddiMacStorageType": lpEnetLtFbFddiMacStorageType,
       "lpEnetLtFbFddiMacIndex": lpEnetLtFbFddiMacIndex,
       "lpEnetLtFbFddiMacTopTable": lpEnetLtFbFddiMacTopTable,
       "lpEnetLtFbFddiMacTopEntry": lpEnetLtFbFddiMacTopEntry,
       "lpEnetLtFbFddiMacTData": lpEnetLtFbFddiMacTData,
       "lpEnetLtFbMacEnet": lpEnetLtFbMacEnet,
       "lpEnetLtFbMacEnetRowStatusTable": lpEnetLtFbMacEnetRowStatusTable,
       "lpEnetLtFbMacEnetRowStatusEntry": lpEnetLtFbMacEnetRowStatusEntry,
       "lpEnetLtFbMacEnetRowStatus": lpEnetLtFbMacEnetRowStatus,
       "lpEnetLtFbMacEnetComponentName": lpEnetLtFbMacEnetComponentName,
       "lpEnetLtFbMacEnetStorageType": lpEnetLtFbMacEnetStorageType,
       "lpEnetLtFbMacEnetIndex": lpEnetLtFbMacEnetIndex,
       "lpEnetLtFbMacEnetTopTable": lpEnetLtFbMacEnetTopTable,
       "lpEnetLtFbMacEnetTopEntry": lpEnetLtFbMacEnetTopEntry,
       "lpEnetLtFbMacEnetTData": lpEnetLtFbMacEnetTData,
       "lpEnetLtFbMacTr": lpEnetLtFbMacTr,
       "lpEnetLtFbMacTrRowStatusTable": lpEnetLtFbMacTrRowStatusTable,
       "lpEnetLtFbMacTrRowStatusEntry": lpEnetLtFbMacTrRowStatusEntry,
       "lpEnetLtFbMacTrRowStatus": lpEnetLtFbMacTrRowStatus,
       "lpEnetLtFbMacTrComponentName": lpEnetLtFbMacTrComponentName,
       "lpEnetLtFbMacTrStorageType": lpEnetLtFbMacTrStorageType,
       "lpEnetLtFbMacTrIndex": lpEnetLtFbMacTrIndex,
       "lpEnetLtFbMacTrTopTable": lpEnetLtFbMacTrTopTable,
       "lpEnetLtFbMacTrTopEntry": lpEnetLtFbMacTrTopEntry,
       "lpEnetLtFbMacTrTData": lpEnetLtFbMacTrTData,
       "lpEnetLtFbData": lpEnetLtFbData,
       "lpEnetLtFbDataRowStatusTable": lpEnetLtFbDataRowStatusTable,
       "lpEnetLtFbDataRowStatusEntry": lpEnetLtFbDataRowStatusEntry,
       "lpEnetLtFbDataRowStatus": lpEnetLtFbDataRowStatus,
       "lpEnetLtFbDataComponentName": lpEnetLtFbDataComponentName,
       "lpEnetLtFbDataStorageType": lpEnetLtFbDataStorageType,
       "lpEnetLtFbDataIndex": lpEnetLtFbDataIndex,
       "lpEnetLtFbDataTopTable": lpEnetLtFbDataTopTable,
       "lpEnetLtFbDataTopEntry": lpEnetLtFbDataTopEntry,
       "lpEnetLtFbDataTData": lpEnetLtFbDataTData,
       "lpEnetLtFbIpH": lpEnetLtFbIpH,
       "lpEnetLtFbIpHRowStatusTable": lpEnetLtFbIpHRowStatusTable,
       "lpEnetLtFbIpHRowStatusEntry": lpEnetLtFbIpHRowStatusEntry,
       "lpEnetLtFbIpHRowStatus": lpEnetLtFbIpHRowStatus,
       "lpEnetLtFbIpHComponentName": lpEnetLtFbIpHComponentName,
       "lpEnetLtFbIpHStorageType": lpEnetLtFbIpHStorageType,
       "lpEnetLtFbIpHIndex": lpEnetLtFbIpHIndex,
       "lpEnetLtFbIpHTopTable": lpEnetLtFbIpHTopTable,
       "lpEnetLtFbIpHTopEntry": lpEnetLtFbIpHTopEntry,
       "lpEnetLtFbIpHTData": lpEnetLtFbIpHTData,
       "lpEnetLtFbLlch": lpEnetLtFbLlch,
       "lpEnetLtFbLlchRowStatusTable": lpEnetLtFbLlchRowStatusTable,
       "lpEnetLtFbLlchRowStatusEntry": lpEnetLtFbLlchRowStatusEntry,
       "lpEnetLtFbLlchRowStatus": lpEnetLtFbLlchRowStatus,
       "lpEnetLtFbLlchComponentName": lpEnetLtFbLlchComponentName,
       "lpEnetLtFbLlchStorageType": lpEnetLtFbLlchStorageType,
       "lpEnetLtFbLlchIndex": lpEnetLtFbLlchIndex,
       "lpEnetLtFbLlchTopTable": lpEnetLtFbLlchTopTable,
       "lpEnetLtFbLlchTopEntry": lpEnetLtFbLlchTopEntry,
       "lpEnetLtFbLlchTData": lpEnetLtFbLlchTData,
       "lpEnetLtFbAppleH": lpEnetLtFbAppleH,
       "lpEnetLtFbAppleHRowStatusTable": lpEnetLtFbAppleHRowStatusTable,
       "lpEnetLtFbAppleHRowStatusEntry": lpEnetLtFbAppleHRowStatusEntry,
       "lpEnetLtFbAppleHRowStatus": lpEnetLtFbAppleHRowStatus,
       "lpEnetLtFbAppleHComponentName": lpEnetLtFbAppleHComponentName,
       "lpEnetLtFbAppleHStorageType": lpEnetLtFbAppleHStorageType,
       "lpEnetLtFbAppleHIndex": lpEnetLtFbAppleHIndex,
       "lpEnetLtFbAppleHTopTable": lpEnetLtFbAppleHTopTable,
       "lpEnetLtFbAppleHTopEntry": lpEnetLtFbAppleHTopEntry,
       "lpEnetLtFbAppleHTData": lpEnetLtFbAppleHTData,
       "lpEnetLtFbIpxH": lpEnetLtFbIpxH,
       "lpEnetLtFbIpxHRowStatusTable": lpEnetLtFbIpxHRowStatusTable,
       "lpEnetLtFbIpxHRowStatusEntry": lpEnetLtFbIpxHRowStatusEntry,
       "lpEnetLtFbIpxHRowStatus": lpEnetLtFbIpxHRowStatus,
       "lpEnetLtFbIpxHComponentName": lpEnetLtFbIpxHComponentName,
       "lpEnetLtFbIpxHStorageType": lpEnetLtFbIpxHStorageType,
       "lpEnetLtFbIpxHIndex": lpEnetLtFbIpxHIndex,
       "lpEnetLtFbIpxHTopTable": lpEnetLtFbIpxHTopTable,
       "lpEnetLtFbIpxHTopEntry": lpEnetLtFbIpxHTopEntry,
       "lpEnetLtFbIpxHTData": lpEnetLtFbIpxHTData,
       "lpEnetLtFbTopTable": lpEnetLtFbTopTable,
       "lpEnetLtFbTopEntry": lpEnetLtFbTopEntry,
       "lpEnetLtFbTData": lpEnetLtFbTData,
       "lpEnetLtCntl": lpEnetLtCntl,
       "lpEnetLtCntlRowStatusTable": lpEnetLtCntlRowStatusTable,
       "lpEnetLtCntlRowStatusEntry": lpEnetLtCntlRowStatusEntry,
       "lpEnetLtCntlRowStatus": lpEnetLtCntlRowStatus,
       "lpEnetLtCntlComponentName": lpEnetLtCntlComponentName,
       "lpEnetLtCntlStorageType": lpEnetLtCntlStorageType,
       "lpEnetLtCntlIndex": lpEnetLtCntlIndex,
       "lpEnetLtCntlTopTable": lpEnetLtCntlTopTable,
       "lpEnetLtCntlTopEntry": lpEnetLtCntlTopEntry,
       "lpEnetLtCntlTData": lpEnetLtCntlTData,
       "lpEnetLtTopTable": lpEnetLtTopTable,
       "lpEnetLtTopEntry": lpEnetLtTopEntry,
       "lpEnetLtTData": lpEnetLtTData,
       "lpEnetTest": lpEnetTest,
       "lpEnetTestRowStatusTable": lpEnetTestRowStatusTable,
       "lpEnetTestRowStatusEntry": lpEnetTestRowStatusEntry,
       "lpEnetTestRowStatus": lpEnetTestRowStatus,
       "lpEnetTestComponentName": lpEnetTestComponentName,
       "lpEnetTestStorageType": lpEnetTestStorageType,
       "lpEnetTestIndex": lpEnetTestIndex,
       "lpEnetTestPTOTable": lpEnetTestPTOTable,
       "lpEnetTestPTOEntry": lpEnetTestPTOEntry,
       "lpEnetTestType": lpEnetTestType,
       "lpEnetTestFrmSize": lpEnetTestFrmSize,
       "lpEnetTestDuration": lpEnetTestDuration,
       "lpEnetTestResultsTable": lpEnetTestResultsTable,
       "lpEnetTestResultsEntry": lpEnetTestResultsEntry,
       "lpEnetTestElapsedTime": lpEnetTestElapsedTime,
       "lpEnetTestTimeRemaining": lpEnetTestTimeRemaining,
       "lpEnetTestCauseOfTermination": lpEnetTestCauseOfTermination,
       "lpEnetTestFrmTx": lpEnetTestFrmTx,
       "lpEnetTestBitsTx": lpEnetTestBitsTx,
       "lpEnetTestFrmRx": lpEnetTestFrmRx,
       "lpEnetTestBitsRx": lpEnetTestBitsRx,
       "lpEnetTestErroredFrmRx": lpEnetTestErroredFrmRx,
       "lpEnetCidDataTable": lpEnetCidDataTable,
       "lpEnetCidDataEntry": lpEnetCidDataEntry,
       "lpEnetCustomerIdentifier": lpEnetCustomerIdentifier,
       "lpEnetIfEntryTable": lpEnetIfEntryTable,
       "lpEnetIfEntryEntry": lpEnetIfEntryEntry,
       "lpEnetIfAdminStatus": lpEnetIfAdminStatus,
       "lpEnetIfIndex": lpEnetIfIndex,
       "lpEnetProvTable": lpEnetProvTable,
       "lpEnetProvEntry": lpEnetProvEntry,
       "lpEnetHeartbeatPacket": lpEnetHeartbeatPacket,
       "lpEnetApplicationFramerName": lpEnetApplicationFramerName,
       "lpEnetAdminInfoTable": lpEnetAdminInfoTable,
       "lpEnetAdminInfoEntry": lpEnetAdminInfoEntry,
       "lpEnetVendor": lpEnetVendor,
       "lpEnetCommentText": lpEnetCommentText,
       "lpEnetStateTable": lpEnetStateTable,
       "lpEnetStateEntry": lpEnetStateEntry,
       "lpEnetAdminState": lpEnetAdminState,
       "lpEnetOperationalState": lpEnetOperationalState,
       "lpEnetUsageState": lpEnetUsageState,
       "lpEnetOperStatusTable": lpEnetOperStatusTable,
       "lpEnetOperStatusEntry": lpEnetOperStatusEntry,
       "lpEnetSnmpOperStatus": lpEnetSnmpOperStatus,
       "lpEnetOperTable": lpEnetOperTable,
       "lpEnetOperEntry": lpEnetOperEntry,
       "lpEnetMacAddress": lpEnetMacAddress,
       "lpEnetStatsTable": lpEnetStatsTable,
       "lpEnetStatsEntry": lpEnetStatsEntry,
       "lpEnetAlignmentErrors": lpEnetAlignmentErrors,
       "lpEnetFcsErrors": lpEnetFcsErrors,
       "lpEnetSingleCollisionFrames": lpEnetSingleCollisionFrames,
       "lpEnetMultipleCollisionFrames": lpEnetMultipleCollisionFrames,
       "lpEnetSqeTestErrors": lpEnetSqeTestErrors,
       "lpEnetDeferredTransmissions": lpEnetDeferredTransmissions,
       "lpEnetLateCollisions": lpEnetLateCollisions,
       "lpEnetExcessiveCollisions": lpEnetExcessiveCollisions,
       "lpEnetMacTransmitErrors": lpEnetMacTransmitErrors,
       "lpEnetCarrierSenseErrors": lpEnetCarrierSenseErrors,
       "lpEnetFrameTooLongs": lpEnetFrameTooLongs,
       "lpEnetMacReceiveErrors": lpEnetMacReceiveErrors,
       "lpFi": lpFi,
       "lpFiRowStatusTable": lpFiRowStatusTable,
       "lpFiRowStatusEntry": lpFiRowStatusEntry,
       "lpFiRowStatus": lpFiRowStatus,
       "lpFiComponentName": lpFiComponentName,
       "lpFiStorageType": lpFiStorageType,
       "lpFiIndex": lpFiIndex,
       "lpFiLt": lpFiLt,
       "lpFiLtRowStatusTable": lpFiLtRowStatusTable,
       "lpFiLtRowStatusEntry": lpFiLtRowStatusEntry,
       "lpFiLtRowStatus": lpFiLtRowStatus,
       "lpFiLtComponentName": lpFiLtComponentName,
       "lpFiLtStorageType": lpFiLtStorageType,
       "lpFiLtIndex": lpFiLtIndex,
       "lpFiLtFrmCmp": lpFiLtFrmCmp,
       "lpFiLtFrmCmpRowStatusTable": lpFiLtFrmCmpRowStatusTable,
       "lpFiLtFrmCmpRowStatusEntry": lpFiLtFrmCmpRowStatusEntry,
       "lpFiLtFrmCmpRowStatus": lpFiLtFrmCmpRowStatus,
       "lpFiLtFrmCmpComponentName": lpFiLtFrmCmpComponentName,
       "lpFiLtFrmCmpStorageType": lpFiLtFrmCmpStorageType,
       "lpFiLtFrmCmpIndex": lpFiLtFrmCmpIndex,
       "lpFiLtFrmCmpTopTable": lpFiLtFrmCmpTopTable,
       "lpFiLtFrmCmpTopEntry": lpFiLtFrmCmpTopEntry,
       "lpFiLtFrmCmpTData": lpFiLtFrmCmpTData,
       "lpFiLtFrmCpy": lpFiLtFrmCpy,
       "lpFiLtFrmCpyRowStatusTable": lpFiLtFrmCpyRowStatusTable,
       "lpFiLtFrmCpyRowStatusEntry": lpFiLtFrmCpyRowStatusEntry,
       "lpFiLtFrmCpyRowStatus": lpFiLtFrmCpyRowStatus,
       "lpFiLtFrmCpyComponentName": lpFiLtFrmCpyComponentName,
       "lpFiLtFrmCpyStorageType": lpFiLtFrmCpyStorageType,
       "lpFiLtFrmCpyIndex": lpFiLtFrmCpyIndex,
       "lpFiLtFrmCpyTopTable": lpFiLtFrmCpyTopTable,
       "lpFiLtFrmCpyTopEntry": lpFiLtFrmCpyTopEntry,
       "lpFiLtFrmCpyTData": lpFiLtFrmCpyTData,
       "lpFiLtPrtCfg": lpFiLtPrtCfg,
       "lpFiLtPrtCfgRowStatusTable": lpFiLtPrtCfgRowStatusTable,
       "lpFiLtPrtCfgRowStatusEntry": lpFiLtPrtCfgRowStatusEntry,
       "lpFiLtPrtCfgRowStatus": lpFiLtPrtCfgRowStatus,
       "lpFiLtPrtCfgComponentName": lpFiLtPrtCfgComponentName,
       "lpFiLtPrtCfgStorageType": lpFiLtPrtCfgStorageType,
       "lpFiLtPrtCfgIndex": lpFiLtPrtCfgIndex,
       "lpFiLtPrtCfgTopTable": lpFiLtPrtCfgTopTable,
       "lpFiLtPrtCfgTopEntry": lpFiLtPrtCfgTopEntry,
       "lpFiLtPrtCfgTData": lpFiLtPrtCfgTData,
       "lpFiLtFb": lpFiLtFb,
       "lpFiLtFbRowStatusTable": lpFiLtFbRowStatusTable,
       "lpFiLtFbRowStatusEntry": lpFiLtFbRowStatusEntry,
       "lpFiLtFbRowStatus": lpFiLtFbRowStatus,
       "lpFiLtFbComponentName": lpFiLtFbComponentName,
       "lpFiLtFbStorageType": lpFiLtFbStorageType,
       "lpFiLtFbIndex": lpFiLtFbIndex,
       "lpFiLtFbTxInfo": lpFiLtFbTxInfo,
       "lpFiLtFbTxInfoRowStatusTable": lpFiLtFbTxInfoRowStatusTable,
       "lpFiLtFbTxInfoRowStatusEntry": lpFiLtFbTxInfoRowStatusEntry,
       "lpFiLtFbTxInfoRowStatus": lpFiLtFbTxInfoRowStatus,
       "lpFiLtFbTxInfoComponentName": lpFiLtFbTxInfoComponentName,
       "lpFiLtFbTxInfoStorageType": lpFiLtFbTxInfoStorageType,
       "lpFiLtFbTxInfoIndex": lpFiLtFbTxInfoIndex,
       "lpFiLtFbTxInfoTopTable": lpFiLtFbTxInfoTopTable,
       "lpFiLtFbTxInfoTopEntry": lpFiLtFbTxInfoTopEntry,
       "lpFiLtFbTxInfoTData": lpFiLtFbTxInfoTData,
       "lpFiLtFbFddiMac": lpFiLtFbFddiMac,
       "lpFiLtFbFddiMacRowStatusTable": lpFiLtFbFddiMacRowStatusTable,
       "lpFiLtFbFddiMacRowStatusEntry": lpFiLtFbFddiMacRowStatusEntry,
       "lpFiLtFbFddiMacRowStatus": lpFiLtFbFddiMacRowStatus,
       "lpFiLtFbFddiMacComponentName": lpFiLtFbFddiMacComponentName,
       "lpFiLtFbFddiMacStorageType": lpFiLtFbFddiMacStorageType,
       "lpFiLtFbFddiMacIndex": lpFiLtFbFddiMacIndex,
       "lpFiLtFbFddiMacTopTable": lpFiLtFbFddiMacTopTable,
       "lpFiLtFbFddiMacTopEntry": lpFiLtFbFddiMacTopEntry,
       "lpFiLtFbFddiMacTData": lpFiLtFbFddiMacTData,
       "lpFiLtFbMacEnet": lpFiLtFbMacEnet,
       "lpFiLtFbMacEnetRowStatusTable": lpFiLtFbMacEnetRowStatusTable,
       "lpFiLtFbMacEnetRowStatusEntry": lpFiLtFbMacEnetRowStatusEntry,
       "lpFiLtFbMacEnetRowStatus": lpFiLtFbMacEnetRowStatus,
       "lpFiLtFbMacEnetComponentName": lpFiLtFbMacEnetComponentName,
       "lpFiLtFbMacEnetStorageType": lpFiLtFbMacEnetStorageType,
       "lpFiLtFbMacEnetIndex": lpFiLtFbMacEnetIndex,
       "lpFiLtFbMacEnetTopTable": lpFiLtFbMacEnetTopTable,
       "lpFiLtFbMacEnetTopEntry": lpFiLtFbMacEnetTopEntry,
       "lpFiLtFbMacEnetTData": lpFiLtFbMacEnetTData,
       "lpFiLtFbMacTr": lpFiLtFbMacTr,
       "lpFiLtFbMacTrRowStatusTable": lpFiLtFbMacTrRowStatusTable,
       "lpFiLtFbMacTrRowStatusEntry": lpFiLtFbMacTrRowStatusEntry,
       "lpFiLtFbMacTrRowStatus": lpFiLtFbMacTrRowStatus,
       "lpFiLtFbMacTrComponentName": lpFiLtFbMacTrComponentName,
       "lpFiLtFbMacTrStorageType": lpFiLtFbMacTrStorageType,
       "lpFiLtFbMacTrIndex": lpFiLtFbMacTrIndex,
       "lpFiLtFbMacTrTopTable": lpFiLtFbMacTrTopTable,
       "lpFiLtFbMacTrTopEntry": lpFiLtFbMacTrTopEntry,
       "lpFiLtFbMacTrTData": lpFiLtFbMacTrTData,
       "lpFiLtFbData": lpFiLtFbData,
       "lpFiLtFbDataRowStatusTable": lpFiLtFbDataRowStatusTable,
       "lpFiLtFbDataRowStatusEntry": lpFiLtFbDataRowStatusEntry,
       "lpFiLtFbDataRowStatus": lpFiLtFbDataRowStatus,
       "lpFiLtFbDataComponentName": lpFiLtFbDataComponentName,
       "lpFiLtFbDataStorageType": lpFiLtFbDataStorageType,
       "lpFiLtFbDataIndex": lpFiLtFbDataIndex,
       "lpFiLtFbDataTopTable": lpFiLtFbDataTopTable,
       "lpFiLtFbDataTopEntry": lpFiLtFbDataTopEntry,
       "lpFiLtFbDataTData": lpFiLtFbDataTData,
       "lpFiLtFbIpH": lpFiLtFbIpH,
       "lpFiLtFbIpHRowStatusTable": lpFiLtFbIpHRowStatusTable,
       "lpFiLtFbIpHRowStatusEntry": lpFiLtFbIpHRowStatusEntry,
       "lpFiLtFbIpHRowStatus": lpFiLtFbIpHRowStatus,
       "lpFiLtFbIpHComponentName": lpFiLtFbIpHComponentName,
       "lpFiLtFbIpHStorageType": lpFiLtFbIpHStorageType,
       "lpFiLtFbIpHIndex": lpFiLtFbIpHIndex,
       "lpFiLtFbIpHTopTable": lpFiLtFbIpHTopTable,
       "lpFiLtFbIpHTopEntry": lpFiLtFbIpHTopEntry,
       "lpFiLtFbIpHTData": lpFiLtFbIpHTData,
       "lpFiLtFbLlch": lpFiLtFbLlch,
       "lpFiLtFbLlchRowStatusTable": lpFiLtFbLlchRowStatusTable,
       "lpFiLtFbLlchRowStatusEntry": lpFiLtFbLlchRowStatusEntry,
       "lpFiLtFbLlchRowStatus": lpFiLtFbLlchRowStatus,
       "lpFiLtFbLlchComponentName": lpFiLtFbLlchComponentName,
       "lpFiLtFbLlchStorageType": lpFiLtFbLlchStorageType,
       "lpFiLtFbLlchIndex": lpFiLtFbLlchIndex,
       "lpFiLtFbLlchTopTable": lpFiLtFbLlchTopTable,
       "lpFiLtFbLlchTopEntry": lpFiLtFbLlchTopEntry,
       "lpFiLtFbLlchTData": lpFiLtFbLlchTData,
       "lpFiLtFbAppleH": lpFiLtFbAppleH,
       "lpFiLtFbAppleHRowStatusTable": lpFiLtFbAppleHRowStatusTable,
       "lpFiLtFbAppleHRowStatusEntry": lpFiLtFbAppleHRowStatusEntry,
       "lpFiLtFbAppleHRowStatus": lpFiLtFbAppleHRowStatus,
       "lpFiLtFbAppleHComponentName": lpFiLtFbAppleHComponentName,
       "lpFiLtFbAppleHStorageType": lpFiLtFbAppleHStorageType,
       "lpFiLtFbAppleHIndex": lpFiLtFbAppleHIndex,
       "lpFiLtFbAppleHTopTable": lpFiLtFbAppleHTopTable,
       "lpFiLtFbAppleHTopEntry": lpFiLtFbAppleHTopEntry,
       "lpFiLtFbAppleHTData": lpFiLtFbAppleHTData,
       "lpFiLtFbIpxH": lpFiLtFbIpxH,
       "lpFiLtFbIpxHRowStatusTable": lpFiLtFbIpxHRowStatusTable,
       "lpFiLtFbIpxHRowStatusEntry": lpFiLtFbIpxHRowStatusEntry,
       "lpFiLtFbIpxHRowStatus": lpFiLtFbIpxHRowStatus,
       "lpFiLtFbIpxHComponentName": lpFiLtFbIpxHComponentName,
       "lpFiLtFbIpxHStorageType": lpFiLtFbIpxHStorageType,
       "lpFiLtFbIpxHIndex": lpFiLtFbIpxHIndex,
       "lpFiLtFbIpxHTopTable": lpFiLtFbIpxHTopTable,
       "lpFiLtFbIpxHTopEntry": lpFiLtFbIpxHTopEntry,
       "lpFiLtFbIpxHTData": lpFiLtFbIpxHTData,
       "lpFiLtFbTopTable": lpFiLtFbTopTable,
       "lpFiLtFbTopEntry": lpFiLtFbTopEntry,
       "lpFiLtFbTData": lpFiLtFbTData,
       "lpFiLtCntl": lpFiLtCntl,
       "lpFiLtCntlRowStatusTable": lpFiLtCntlRowStatusTable,
       "lpFiLtCntlRowStatusEntry": lpFiLtCntlRowStatusEntry,
       "lpFiLtCntlRowStatus": lpFiLtCntlRowStatus,
       "lpFiLtCntlComponentName": lpFiLtCntlComponentName,
       "lpFiLtCntlStorageType": lpFiLtCntlStorageType,
       "lpFiLtCntlIndex": lpFiLtCntlIndex,
       "lpFiLtCntlTopTable": lpFiLtCntlTopTable,
       "lpFiLtCntlTopEntry": lpFiLtCntlTopEntry,
       "lpFiLtCntlTData": lpFiLtCntlTData,
       "lpFiLtTopTable": lpFiLtTopTable,
       "lpFiLtTopEntry": lpFiLtTopEntry,
       "lpFiLtTData": lpFiLtTData,
       "lpFiPhy": lpFiPhy,
       "lpFiPhyRowStatusTable": lpFiPhyRowStatusTable,
       "lpFiPhyRowStatusEntry": lpFiPhyRowStatusEntry,
       "lpFiPhyRowStatus": lpFiPhyRowStatus,
       "lpFiPhyComponentName": lpFiPhyComponentName,
       "lpFiPhyStorageType": lpFiPhyStorageType,
       "lpFiPhyFddiPhyTypeIndex": lpFiPhyFddiPhyTypeIndex,
       "lpFiPhyProvTable": lpFiPhyProvTable,
       "lpFiPhyProvEntry": lpFiPhyProvEntry,
       "lpFiPhyLerCutoff": lpFiPhyLerCutoff,
       "lpFiPhyLerAlarm": lpFiPhyLerAlarm,
       "lpFiPhyLinkErrorMonitor": lpFiPhyLinkErrorMonitor,
       "lpFiPhyOperTable": lpFiPhyOperTable,
       "lpFiPhyOperEntry": lpFiPhyOperEntry,
       "lpFiPhyNeighborType": lpFiPhyNeighborType,
       "lpFiPhyLctFailCounts": lpFiPhyLctFailCounts,
       "lpFiPhyLerEstimate": lpFiPhyLerEstimate,
       "lpFiPhyLemRejectCounts": lpFiPhyLemRejectCounts,
       "lpFiPhyLemCounts": lpFiPhyLemCounts,
       "lpFiPhyPcmState": lpFiPhyPcmState,
       "lpFiPhyLerFlag": lpFiPhyLerFlag,
       "lpFiPhySignalState": lpFiPhySignalState,
       "lpFiPhySignalBitsRcvd": lpFiPhySignalBitsRcvd,
       "lpFiPhySignalBitsTxmt": lpFiPhySignalBitsTxmt,
       "lpFiTest": lpFiTest,
       "lpFiTestRowStatusTable": lpFiTestRowStatusTable,
       "lpFiTestRowStatusEntry": lpFiTestRowStatusEntry,
       "lpFiTestRowStatus": lpFiTestRowStatus,
       "lpFiTestComponentName": lpFiTestComponentName,
       "lpFiTestStorageType": lpFiTestStorageType,
       "lpFiTestIndex": lpFiTestIndex,
       "lpFiTestPTOTable": lpFiTestPTOTable,
       "lpFiTestPTOEntry": lpFiTestPTOEntry,
       "lpFiTestType": lpFiTestType,
       "lpFiTestFrmSize": lpFiTestFrmSize,
       "lpFiTestDuration": lpFiTestDuration,
       "lpFiTestResultsTable": lpFiTestResultsTable,
       "lpFiTestResultsEntry": lpFiTestResultsEntry,
       "lpFiTestElapsedTime": lpFiTestElapsedTime,
       "lpFiTestTimeRemaining": lpFiTestTimeRemaining,
       "lpFiTestCauseOfTermination": lpFiTestCauseOfTermination,
       "lpFiTestFrmTx": lpFiTestFrmTx,
       "lpFiTestBitsTx": lpFiTestBitsTx,
       "lpFiTestFrmRx": lpFiTestFrmRx,
       "lpFiTestBitsRx": lpFiTestBitsRx,
       "lpFiTestErroredFrmRx": lpFiTestErroredFrmRx,
       "lpFiCidDataTable": lpFiCidDataTable,
       "lpFiCidDataEntry": lpFiCidDataEntry,
       "lpFiCustomerIdentifier": lpFiCustomerIdentifier,
       "lpFiIfEntryTable": lpFiIfEntryTable,
       "lpFiIfEntryEntry": lpFiIfEntryEntry,
       "lpFiIfAdminStatus": lpFiIfAdminStatus,
       "lpFiIfIndex": lpFiIfIndex,
       "lpFiSmtProvTable": lpFiSmtProvTable,
       "lpFiSmtProvEntry": lpFiSmtProvEntry,
       "lpFiUserData": lpFiUserData,
       "lpFiAcceptAa": lpFiAcceptAa,
       "lpFiAcceptBb": lpFiAcceptBb,
       "lpFiAcceptAs": lpFiAcceptAs,
       "lpFiAcceptBs": lpFiAcceptBs,
       "lpFiAcceptAm": lpFiAcceptAm,
       "lpFiAcceptBm": lpFiAcceptBm,
       "lpFiUseThruBa": lpFiUseThruBa,
       "lpFiNeighborNotifyInterval": lpFiNeighborNotifyInterval,
       "lpFiStatusReportPolicy": lpFiStatusReportPolicy,
       "lpFiTraceMaxExpirationTimer": lpFiTraceMaxExpirationTimer,
       "lpFiApplicationFramerName": lpFiApplicationFramerName,
       "lpFiMacProvTable": lpFiMacProvTable,
       "lpFiMacProvEntry": lpFiMacProvEntry,
       "lpFiTokenRequestTimer": lpFiTokenRequestTimer,
       "lpFiTokenMaxTimer": lpFiTokenMaxTimer,
       "lpFiValidTransmissionTimer": lpFiValidTransmissionTimer,
       "lpFiAdminInfoTable": lpFiAdminInfoTable,
       "lpFiAdminInfoEntry": lpFiAdminInfoEntry,
       "lpFiVendor": lpFiVendor,
       "lpFiCommentText": lpFiCommentText,
       "lpFiStateTable": lpFiStateTable,
       "lpFiStateEntry": lpFiStateEntry,
       "lpFiAdminState": lpFiAdminState,
       "lpFiOperationalState": lpFiOperationalState,
       "lpFiUsageState": lpFiUsageState,
       "lpFiOperStatusTable": lpFiOperStatusTable,
       "lpFiOperStatusEntry": lpFiOperStatusEntry,
       "lpFiSnmpOperStatus": lpFiSnmpOperStatus,
       "lpFiSmtOperTable": lpFiSmtOperTable,
       "lpFiSmtOperEntry": lpFiSmtOperEntry,
       "lpFiVersion": lpFiVersion,
       "lpFiBypassPresent": lpFiBypassPresent,
       "lpFiEcmState": lpFiEcmState,
       "lpFiCfState": lpFiCfState,
       "lpFiMacOperTable": lpFiMacOperTable,
       "lpFiMacOperEntry": lpFiMacOperEntry,
       "lpFiRingLatency": lpFiRingLatency,
       "lpFiMacAddress": lpFiMacAddress,
       "lpFiUpstreamNeighbor": lpFiUpstreamNeighbor,
       "lpFiDownstreamNeighbor": lpFiDownstreamNeighbor,
       "lpFiOldUpstreamNeighbor": lpFiOldUpstreamNeighbor,
       "lpFiOldDownstreamNeighbor": lpFiOldDownstreamNeighbor,
       "lpFiDupAddressTest": lpFiDupAddressTest,
       "lpFiTokenNegotiatedTimer": lpFiTokenNegotiatedTimer,
       "lpFiFrameCounts": lpFiFrameCounts,
       "lpFiCopiedCounts": lpFiCopiedCounts,
       "lpFiTransmitCounts": lpFiTransmitCounts,
       "lpFiErrorCounts": lpFiErrorCounts,
       "lpFiLostCounts": lpFiLostCounts,
       "lpFiRmtState": lpFiRmtState,
       "lpFiFrameErrorFlag": lpFiFrameErrorFlag,
       "lpFiMacCOperTable": lpFiMacCOperTable,
       "lpFiMacCOperEntry": lpFiMacCOperEntry,
       "lpFiTokenCounts": lpFiTokenCounts,
       "lpFiTvxExpiredCounts": lpFiTvxExpiredCounts,
       "lpFiNotCopiedCounts": lpFiNotCopiedCounts,
       "lpFiLateCounts": lpFiLateCounts,
       "lpFiRingOpCounts": lpFiRingOpCounts,
       "lpFiNcMacOperTable": lpFiNcMacOperTable,
       "lpFiNcMacOperEntry": lpFiNcMacOperEntry,
       "lpFiNcMacAddress": lpFiNcMacAddress,
       "lpFiNcUpstreamNeighbor": lpFiNcUpstreamNeighbor,
       "lpFiNcDownstreamNeighbor": lpFiNcDownstreamNeighbor,
       "lpFiNcOldUpstreamNeighbor": lpFiNcOldUpstreamNeighbor,
       "lpFiNcOldDownstreamNeighbor": lpFiNcOldDownstreamNeighbor,
       "lpTr": lpTr,
       "lpTrRowStatusTable": lpTrRowStatusTable,
       "lpTrRowStatusEntry": lpTrRowStatusEntry,
       "lpTrRowStatus": lpTrRowStatus,
       "lpTrComponentName": lpTrComponentName,
       "lpTrStorageType": lpTrStorageType,
       "lpTrIndex": lpTrIndex,
       "lpTrLt": lpTrLt,
       "lpTrLtRowStatusTable": lpTrLtRowStatusTable,
       "lpTrLtRowStatusEntry": lpTrLtRowStatusEntry,
       "lpTrLtRowStatus": lpTrLtRowStatus,
       "lpTrLtComponentName": lpTrLtComponentName,
       "lpTrLtStorageType": lpTrLtStorageType,
       "lpTrLtIndex": lpTrLtIndex,
       "lpTrLtFrmCmp": lpTrLtFrmCmp,
       "lpTrLtFrmCmpRowStatusTable": lpTrLtFrmCmpRowStatusTable,
       "lpTrLtFrmCmpRowStatusEntry": lpTrLtFrmCmpRowStatusEntry,
       "lpTrLtFrmCmpRowStatus": lpTrLtFrmCmpRowStatus,
       "lpTrLtFrmCmpComponentName": lpTrLtFrmCmpComponentName,
       "lpTrLtFrmCmpStorageType": lpTrLtFrmCmpStorageType,
       "lpTrLtFrmCmpIndex": lpTrLtFrmCmpIndex,
       "lpTrLtFrmCmpTopTable": lpTrLtFrmCmpTopTable,
       "lpTrLtFrmCmpTopEntry": lpTrLtFrmCmpTopEntry,
       "lpTrLtFrmCmpTData": lpTrLtFrmCmpTData,
       "lpTrLtFrmCpy": lpTrLtFrmCpy,
       "lpTrLtFrmCpyRowStatusTable": lpTrLtFrmCpyRowStatusTable,
       "lpTrLtFrmCpyRowStatusEntry": lpTrLtFrmCpyRowStatusEntry,
       "lpTrLtFrmCpyRowStatus": lpTrLtFrmCpyRowStatus,
       "lpTrLtFrmCpyComponentName": lpTrLtFrmCpyComponentName,
       "lpTrLtFrmCpyStorageType": lpTrLtFrmCpyStorageType,
       "lpTrLtFrmCpyIndex": lpTrLtFrmCpyIndex,
       "lpTrLtFrmCpyTopTable": lpTrLtFrmCpyTopTable,
       "lpTrLtFrmCpyTopEntry": lpTrLtFrmCpyTopEntry,
       "lpTrLtFrmCpyTData": lpTrLtFrmCpyTData,
       "lpTrLtPrtCfg": lpTrLtPrtCfg,
       "lpTrLtPrtCfgRowStatusTable": lpTrLtPrtCfgRowStatusTable,
       "lpTrLtPrtCfgRowStatusEntry": lpTrLtPrtCfgRowStatusEntry,
       "lpTrLtPrtCfgRowStatus": lpTrLtPrtCfgRowStatus,
       "lpTrLtPrtCfgComponentName": lpTrLtPrtCfgComponentName,
       "lpTrLtPrtCfgStorageType": lpTrLtPrtCfgStorageType,
       "lpTrLtPrtCfgIndex": lpTrLtPrtCfgIndex,
       "lpTrLtPrtCfgTopTable": lpTrLtPrtCfgTopTable,
       "lpTrLtPrtCfgTopEntry": lpTrLtPrtCfgTopEntry,
       "lpTrLtPrtCfgTData": lpTrLtPrtCfgTData,
       "lpTrLtFb": lpTrLtFb,
       "lpTrLtFbRowStatusTable": lpTrLtFbRowStatusTable,
       "lpTrLtFbRowStatusEntry": lpTrLtFbRowStatusEntry,
       "lpTrLtFbRowStatus": lpTrLtFbRowStatus,
       "lpTrLtFbComponentName": lpTrLtFbComponentName,
       "lpTrLtFbStorageType": lpTrLtFbStorageType,
       "lpTrLtFbIndex": lpTrLtFbIndex,
       "lpTrLtFbTxInfo": lpTrLtFbTxInfo,
       "lpTrLtFbTxInfoRowStatusTable": lpTrLtFbTxInfoRowStatusTable,
       "lpTrLtFbTxInfoRowStatusEntry": lpTrLtFbTxInfoRowStatusEntry,
       "lpTrLtFbTxInfoRowStatus": lpTrLtFbTxInfoRowStatus,
       "lpTrLtFbTxInfoComponentName": lpTrLtFbTxInfoComponentName,
       "lpTrLtFbTxInfoStorageType": lpTrLtFbTxInfoStorageType,
       "lpTrLtFbTxInfoIndex": lpTrLtFbTxInfoIndex,
       "lpTrLtFbTxInfoTopTable": lpTrLtFbTxInfoTopTable,
       "lpTrLtFbTxInfoTopEntry": lpTrLtFbTxInfoTopEntry,
       "lpTrLtFbTxInfoTData": lpTrLtFbTxInfoTData,
       "lpTrLtFbFddiMac": lpTrLtFbFddiMac,
       "lpTrLtFbFddiMacRowStatusTable": lpTrLtFbFddiMacRowStatusTable,
       "lpTrLtFbFddiMacRowStatusEntry": lpTrLtFbFddiMacRowStatusEntry,
       "lpTrLtFbFddiMacRowStatus": lpTrLtFbFddiMacRowStatus,
       "lpTrLtFbFddiMacComponentName": lpTrLtFbFddiMacComponentName,
       "lpTrLtFbFddiMacStorageType": lpTrLtFbFddiMacStorageType,
       "lpTrLtFbFddiMacIndex": lpTrLtFbFddiMacIndex,
       "lpTrLtFbFddiMacTopTable": lpTrLtFbFddiMacTopTable,
       "lpTrLtFbFddiMacTopEntry": lpTrLtFbFddiMacTopEntry,
       "lpTrLtFbFddiMacTData": lpTrLtFbFddiMacTData,
       "lpTrLtFbMacEnet": lpTrLtFbMacEnet,
       "lpTrLtFbMacEnetRowStatusTable": lpTrLtFbMacEnetRowStatusTable,
       "lpTrLtFbMacEnetRowStatusEntry": lpTrLtFbMacEnetRowStatusEntry,
       "lpTrLtFbMacEnetRowStatus": lpTrLtFbMacEnetRowStatus,
       "lpTrLtFbMacEnetComponentName": lpTrLtFbMacEnetComponentName,
       "lpTrLtFbMacEnetStorageType": lpTrLtFbMacEnetStorageType,
       "lpTrLtFbMacEnetIndex": lpTrLtFbMacEnetIndex,
       "lpTrLtFbMacEnetTopTable": lpTrLtFbMacEnetTopTable,
       "lpTrLtFbMacEnetTopEntry": lpTrLtFbMacEnetTopEntry,
       "lpTrLtFbMacEnetTData": lpTrLtFbMacEnetTData,
       "lpTrLtFbMacTr": lpTrLtFbMacTr,
       "lpTrLtFbMacTrRowStatusTable": lpTrLtFbMacTrRowStatusTable,
       "lpTrLtFbMacTrRowStatusEntry": lpTrLtFbMacTrRowStatusEntry,
       "lpTrLtFbMacTrRowStatus": lpTrLtFbMacTrRowStatus,
       "lpTrLtFbMacTrComponentName": lpTrLtFbMacTrComponentName,
       "lpTrLtFbMacTrStorageType": lpTrLtFbMacTrStorageType,
       "lpTrLtFbMacTrIndex": lpTrLtFbMacTrIndex,
       "lpTrLtFbMacTrTopTable": lpTrLtFbMacTrTopTable,
       "lpTrLtFbMacTrTopEntry": lpTrLtFbMacTrTopEntry,
       "lpTrLtFbMacTrTData": lpTrLtFbMacTrTData,
       "lpTrLtFbData": lpTrLtFbData,
       "lpTrLtFbDataRowStatusTable": lpTrLtFbDataRowStatusTable,
       "lpTrLtFbDataRowStatusEntry": lpTrLtFbDataRowStatusEntry,
       "lpTrLtFbDataRowStatus": lpTrLtFbDataRowStatus,
       "lpTrLtFbDataComponentName": lpTrLtFbDataComponentName,
       "lpTrLtFbDataStorageType": lpTrLtFbDataStorageType,
       "lpTrLtFbDataIndex": lpTrLtFbDataIndex,
       "lpTrLtFbDataTopTable": lpTrLtFbDataTopTable,
       "lpTrLtFbDataTopEntry": lpTrLtFbDataTopEntry,
       "lpTrLtFbDataTData": lpTrLtFbDataTData,
       "lpTrLtFbIpH": lpTrLtFbIpH,
       "lpTrLtFbIpHRowStatusTable": lpTrLtFbIpHRowStatusTable,
       "lpTrLtFbIpHRowStatusEntry": lpTrLtFbIpHRowStatusEntry,
       "lpTrLtFbIpHRowStatus": lpTrLtFbIpHRowStatus,
       "lpTrLtFbIpHComponentName": lpTrLtFbIpHComponentName,
       "lpTrLtFbIpHStorageType": lpTrLtFbIpHStorageType,
       "lpTrLtFbIpHIndex": lpTrLtFbIpHIndex,
       "lpTrLtFbIpHTopTable": lpTrLtFbIpHTopTable,
       "lpTrLtFbIpHTopEntry": lpTrLtFbIpHTopEntry,
       "lpTrLtFbIpHTData": lpTrLtFbIpHTData,
       "lpTrLtFbLlch": lpTrLtFbLlch,
       "lpTrLtFbLlchRowStatusTable": lpTrLtFbLlchRowStatusTable,
       "lpTrLtFbLlchRowStatusEntry": lpTrLtFbLlchRowStatusEntry,
       "lpTrLtFbLlchRowStatus": lpTrLtFbLlchRowStatus,
       "lpTrLtFbLlchComponentName": lpTrLtFbLlchComponentName,
       "lpTrLtFbLlchStorageType": lpTrLtFbLlchStorageType,
       "lpTrLtFbLlchIndex": lpTrLtFbLlchIndex,
       "lpTrLtFbLlchTopTable": lpTrLtFbLlchTopTable,
       "lpTrLtFbLlchTopEntry": lpTrLtFbLlchTopEntry,
       "lpTrLtFbLlchTData": lpTrLtFbLlchTData,
       "lpTrLtFbAppleH": lpTrLtFbAppleH,
       "lpTrLtFbAppleHRowStatusTable": lpTrLtFbAppleHRowStatusTable,
       "lpTrLtFbAppleHRowStatusEntry": lpTrLtFbAppleHRowStatusEntry,
       "lpTrLtFbAppleHRowStatus": lpTrLtFbAppleHRowStatus,
       "lpTrLtFbAppleHComponentName": lpTrLtFbAppleHComponentName,
       "lpTrLtFbAppleHStorageType": lpTrLtFbAppleHStorageType,
       "lpTrLtFbAppleHIndex": lpTrLtFbAppleHIndex,
       "lpTrLtFbAppleHTopTable": lpTrLtFbAppleHTopTable,
       "lpTrLtFbAppleHTopEntry": lpTrLtFbAppleHTopEntry,
       "lpTrLtFbAppleHTData": lpTrLtFbAppleHTData,
       "lpTrLtFbIpxH": lpTrLtFbIpxH,
       "lpTrLtFbIpxHRowStatusTable": lpTrLtFbIpxHRowStatusTable,
       "lpTrLtFbIpxHRowStatusEntry": lpTrLtFbIpxHRowStatusEntry,
       "lpTrLtFbIpxHRowStatus": lpTrLtFbIpxHRowStatus,
       "lpTrLtFbIpxHComponentName": lpTrLtFbIpxHComponentName,
       "lpTrLtFbIpxHStorageType": lpTrLtFbIpxHStorageType,
       "lpTrLtFbIpxHIndex": lpTrLtFbIpxHIndex,
       "lpTrLtFbIpxHTopTable": lpTrLtFbIpxHTopTable,
       "lpTrLtFbIpxHTopEntry": lpTrLtFbIpxHTopEntry,
       "lpTrLtFbIpxHTData": lpTrLtFbIpxHTData,
       "lpTrLtFbTopTable": lpTrLtFbTopTable,
       "lpTrLtFbTopEntry": lpTrLtFbTopEntry,
       "lpTrLtFbTData": lpTrLtFbTData,
       "lpTrLtCntl": lpTrLtCntl,
       "lpTrLtCntlRowStatusTable": lpTrLtCntlRowStatusTable,
       "lpTrLtCntlRowStatusEntry": lpTrLtCntlRowStatusEntry,
       "lpTrLtCntlRowStatus": lpTrLtCntlRowStatus,
       "lpTrLtCntlComponentName": lpTrLtCntlComponentName,
       "lpTrLtCntlStorageType": lpTrLtCntlStorageType,
       "lpTrLtCntlIndex": lpTrLtCntlIndex,
       "lpTrLtCntlTopTable": lpTrLtCntlTopTable,
       "lpTrLtCntlTopEntry": lpTrLtCntlTopEntry,
       "lpTrLtCntlTData": lpTrLtCntlTData,
       "lpTrLtTopTable": lpTrLtTopTable,
       "lpTrLtTopEntry": lpTrLtTopEntry,
       "lpTrLtTData": lpTrLtTData,
       "lpTrTest": lpTrTest,
       "lpTrTestRowStatusTable": lpTrTestRowStatusTable,
       "lpTrTestRowStatusEntry": lpTrTestRowStatusEntry,
       "lpTrTestRowStatus": lpTrTestRowStatus,
       "lpTrTestComponentName": lpTrTestComponentName,
       "lpTrTestStorageType": lpTrTestStorageType,
       "lpTrTestIndex": lpTrTestIndex,
       "lpTrTestPTOTable": lpTrTestPTOTable,
       "lpTrTestPTOEntry": lpTrTestPTOEntry,
       "lpTrTestType": lpTrTestType,
       "lpTrTestFrmSize": lpTrTestFrmSize,
       "lpTrTestDuration": lpTrTestDuration,
       "lpTrTestResultsTable": lpTrTestResultsTable,
       "lpTrTestResultsEntry": lpTrTestResultsEntry,
       "lpTrTestElapsedTime": lpTrTestElapsedTime,
       "lpTrTestTimeRemaining": lpTrTestTimeRemaining,
       "lpTrTestCauseOfTermination": lpTrTestCauseOfTermination,
       "lpTrTestFrmTx": lpTrTestFrmTx,
       "lpTrTestBitsTx": lpTrTestBitsTx,
       "lpTrTestFrmRx": lpTrTestFrmRx,
       "lpTrTestBitsRx": lpTrTestBitsRx,
       "lpTrTestErroredFrmRx": lpTrTestErroredFrmRx,
       "lpTrCidDataTable": lpTrCidDataTable,
       "lpTrCidDataEntry": lpTrCidDataEntry,
       "lpTrCustomerIdentifier": lpTrCustomerIdentifier,
       "lpTrIfEntryTable": lpTrIfEntryTable,
       "lpTrIfEntryEntry": lpTrIfEntryEntry,
       "lpTrIfAdminStatus": lpTrIfAdminStatus,
       "lpTrIfIndex": lpTrIfIndex,
       "lpTrProvTable": lpTrProvTable,
       "lpTrProvEntry": lpTrProvEntry,
       "lpTrRingSpeed": lpTrRingSpeed,
       "lpTrMonitorParticipate": lpTrMonitorParticipate,
       "lpTrFunctionalAddress": lpTrFunctionalAddress,
       "lpTrNodeAddress": lpTrNodeAddress,
       "lpTrGroupAddress": lpTrGroupAddress,
       "lpTrProductId": lpTrProductId,
       "lpTrApplicationFramerName": lpTrApplicationFramerName,
       "lpTrAdminInfoTable": lpTrAdminInfoTable,
       "lpTrAdminInfoEntry": lpTrAdminInfoEntry,
       "lpTrVendor": lpTrVendor,
       "lpTrCommentText": lpTrCommentText,
       "lpTrStateTable": lpTrStateTable,
       "lpTrStateEntry": lpTrStateEntry,
       "lpTrAdminState": lpTrAdminState,
       "lpTrOperationalState": lpTrOperationalState,
       "lpTrUsageState": lpTrUsageState,
       "lpTrOperStatusTable": lpTrOperStatusTable,
       "lpTrOperStatusEntry": lpTrOperStatusEntry,
       "lpTrSnmpOperStatus": lpTrSnmpOperStatus,
       "lpTrOperTable": lpTrOperTable,
       "lpTrOperEntry": lpTrOperEntry,
       "lpTrMacAddress": lpTrMacAddress,
       "lpTrRingState": lpTrRingState,
       "lpTrRingStatus": lpTrRingStatus,
       "lpTrRingOpenStatus": lpTrRingOpenStatus,
       "lpTrUpStream": lpTrUpStream,
       "lpTrChipSet": lpTrChipSet,
       "lpTrLastTimeBeaconSent": lpTrLastTimeBeaconSent,
       "lpTrStatsTable": lpTrStatsTable,
       "lpTrStatsEntry": lpTrStatsEntry,
       "lpTrLineErrors": lpTrLineErrors,
       "lpTrBurstErrors": lpTrBurstErrors,
       "lpTrAcErrors": lpTrAcErrors,
       "lpTrAbortTransErrors": lpTrAbortTransErrors,
       "lpTrInternalErrors": lpTrInternalErrors,
       "lpTrLostFrameErrors": lpTrLostFrameErrors,
       "lpTrReceiveCongestions": lpTrReceiveCongestions,
       "lpTrFrameCopiedErrors": lpTrFrameCopiedErrors,
       "lpTrTokenErrors": lpTrTokenErrors,
       "lpTrSoftErrors": lpTrSoftErrors,
       "lpTrHardErrors": lpTrHardErrors,
       "lpTrSignalLoss": lpTrSignalLoss,
       "lpTrTransmitBeacons": lpTrTransmitBeacons,
       "lpTrRingRecoverys": lpTrRingRecoverys,
       "lpTrLobeWires": lpTrLobeWires,
       "lpTrRemoveRings": lpTrRemoveRings,
       "lpTrSingleStation": lpTrSingleStation,
       "lpTrFreqErrors": lpTrFreqErrors,
       "lpTrNcMacOperTable": lpTrNcMacOperTable,
       "lpTrNcMacOperEntry": lpTrNcMacOperEntry,
       "lpTrNcMacAddress": lpTrNcMacAddress,
       "lpTrNcUpStream": lpTrNcUpStream,
       "lpIlsFwdr": lpIlsFwdr,
       "lpIlsFwdrRowStatusTable": lpIlsFwdrRowStatusTable,
       "lpIlsFwdrRowStatusEntry": lpIlsFwdrRowStatusEntry,
       "lpIlsFwdrRowStatus": lpIlsFwdrRowStatus,
       "lpIlsFwdrComponentName": lpIlsFwdrComponentName,
       "lpIlsFwdrStorageType": lpIlsFwdrStorageType,
       "lpIlsFwdrIndex": lpIlsFwdrIndex,
       "lpIlsFwdrLt": lpIlsFwdrLt,
       "lpIlsFwdrLtRowStatusTable": lpIlsFwdrLtRowStatusTable,
       "lpIlsFwdrLtRowStatusEntry": lpIlsFwdrLtRowStatusEntry,
       "lpIlsFwdrLtRowStatus": lpIlsFwdrLtRowStatus,
       "lpIlsFwdrLtComponentName": lpIlsFwdrLtComponentName,
       "lpIlsFwdrLtStorageType": lpIlsFwdrLtStorageType,
       "lpIlsFwdrLtIndex": lpIlsFwdrLtIndex,
       "lpIlsFwdrLtFrmCmp": lpIlsFwdrLtFrmCmp,
       "lpIlsFwdrLtFrmCmpRowStatusTable": lpIlsFwdrLtFrmCmpRowStatusTable,
       "lpIlsFwdrLtFrmCmpRowStatusEntry": lpIlsFwdrLtFrmCmpRowStatusEntry,
       "lpIlsFwdrLtFrmCmpRowStatus": lpIlsFwdrLtFrmCmpRowStatus,
       "lpIlsFwdrLtFrmCmpComponentName": lpIlsFwdrLtFrmCmpComponentName,
       "lpIlsFwdrLtFrmCmpStorageType": lpIlsFwdrLtFrmCmpStorageType,
       "lpIlsFwdrLtFrmCmpIndex": lpIlsFwdrLtFrmCmpIndex,
       "lpIlsFwdrLtFrmCmpTopTable": lpIlsFwdrLtFrmCmpTopTable,
       "lpIlsFwdrLtFrmCmpTopEntry": lpIlsFwdrLtFrmCmpTopEntry,
       "lpIlsFwdrLtFrmCmpTData": lpIlsFwdrLtFrmCmpTData,
       "lpIlsFwdrLtFrmCpy": lpIlsFwdrLtFrmCpy,
       "lpIlsFwdrLtFrmCpyRowStatusTable": lpIlsFwdrLtFrmCpyRowStatusTable,
       "lpIlsFwdrLtFrmCpyRowStatusEntry": lpIlsFwdrLtFrmCpyRowStatusEntry,
       "lpIlsFwdrLtFrmCpyRowStatus": lpIlsFwdrLtFrmCpyRowStatus,
       "lpIlsFwdrLtFrmCpyComponentName": lpIlsFwdrLtFrmCpyComponentName,
       "lpIlsFwdrLtFrmCpyStorageType": lpIlsFwdrLtFrmCpyStorageType,
       "lpIlsFwdrLtFrmCpyIndex": lpIlsFwdrLtFrmCpyIndex,
       "lpIlsFwdrLtFrmCpyTopTable": lpIlsFwdrLtFrmCpyTopTable,
       "lpIlsFwdrLtFrmCpyTopEntry": lpIlsFwdrLtFrmCpyTopEntry,
       "lpIlsFwdrLtFrmCpyTData": lpIlsFwdrLtFrmCpyTData,
       "lpIlsFwdrLtPrtCfg": lpIlsFwdrLtPrtCfg,
       "lpIlsFwdrLtPrtCfgRowStatusTable": lpIlsFwdrLtPrtCfgRowStatusTable,
       "lpIlsFwdrLtPrtCfgRowStatusEntry": lpIlsFwdrLtPrtCfgRowStatusEntry,
       "lpIlsFwdrLtPrtCfgRowStatus": lpIlsFwdrLtPrtCfgRowStatus,
       "lpIlsFwdrLtPrtCfgComponentName": lpIlsFwdrLtPrtCfgComponentName,
       "lpIlsFwdrLtPrtCfgStorageType": lpIlsFwdrLtPrtCfgStorageType,
       "lpIlsFwdrLtPrtCfgIndex": lpIlsFwdrLtPrtCfgIndex,
       "lpIlsFwdrLtPrtCfgTopTable": lpIlsFwdrLtPrtCfgTopTable,
       "lpIlsFwdrLtPrtCfgTopEntry": lpIlsFwdrLtPrtCfgTopEntry,
       "lpIlsFwdrLtPrtCfgTData": lpIlsFwdrLtPrtCfgTData,
       "lpIlsFwdrLtFb": lpIlsFwdrLtFb,
       "lpIlsFwdrLtFbRowStatusTable": lpIlsFwdrLtFbRowStatusTable,
       "lpIlsFwdrLtFbRowStatusEntry": lpIlsFwdrLtFbRowStatusEntry,
       "lpIlsFwdrLtFbRowStatus": lpIlsFwdrLtFbRowStatus,
       "lpIlsFwdrLtFbComponentName": lpIlsFwdrLtFbComponentName,
       "lpIlsFwdrLtFbStorageType": lpIlsFwdrLtFbStorageType,
       "lpIlsFwdrLtFbIndex": lpIlsFwdrLtFbIndex,
       "lpIlsFwdrLtFbTxInfo": lpIlsFwdrLtFbTxInfo,
       "lpIlsFwdrLtFbTxInfoRowStatusTable": lpIlsFwdrLtFbTxInfoRowStatusTable,
       "lpIlsFwdrLtFbTxInfoRowStatusEntry": lpIlsFwdrLtFbTxInfoRowStatusEntry,
       "lpIlsFwdrLtFbTxInfoRowStatus": lpIlsFwdrLtFbTxInfoRowStatus,
       "lpIlsFwdrLtFbTxInfoComponentName": lpIlsFwdrLtFbTxInfoComponentName,
       "lpIlsFwdrLtFbTxInfoStorageType": lpIlsFwdrLtFbTxInfoStorageType,
       "lpIlsFwdrLtFbTxInfoIndex": lpIlsFwdrLtFbTxInfoIndex,
       "lpIlsFwdrLtFbTxInfoTopTable": lpIlsFwdrLtFbTxInfoTopTable,
       "lpIlsFwdrLtFbTxInfoTopEntry": lpIlsFwdrLtFbTxInfoTopEntry,
       "lpIlsFwdrLtFbTxInfoTData": lpIlsFwdrLtFbTxInfoTData,
       "lpIlsFwdrLtFbFddiMac": lpIlsFwdrLtFbFddiMac,
       "lpIlsFwdrLtFbFddiMacRowStatusTable": lpIlsFwdrLtFbFddiMacRowStatusTable,
       "lpIlsFwdrLtFbFddiMacRowStatusEntry": lpIlsFwdrLtFbFddiMacRowStatusEntry,
       "lpIlsFwdrLtFbFddiMacRowStatus": lpIlsFwdrLtFbFddiMacRowStatus,
       "lpIlsFwdrLtFbFddiMacComponentName": lpIlsFwdrLtFbFddiMacComponentName,
       "lpIlsFwdrLtFbFddiMacStorageType": lpIlsFwdrLtFbFddiMacStorageType,
       "lpIlsFwdrLtFbFddiMacIndex": lpIlsFwdrLtFbFddiMacIndex,
       "lpIlsFwdrLtFbFddiMacTopTable": lpIlsFwdrLtFbFddiMacTopTable,
       "lpIlsFwdrLtFbFddiMacTopEntry": lpIlsFwdrLtFbFddiMacTopEntry,
       "lpIlsFwdrLtFbFddiMacTData": lpIlsFwdrLtFbFddiMacTData,
       "lpIlsFwdrLtFbMacEnet": lpIlsFwdrLtFbMacEnet,
       "lpIlsFwdrLtFbMacEnetRowStatusTable": lpIlsFwdrLtFbMacEnetRowStatusTable,
       "lpIlsFwdrLtFbMacEnetRowStatusEntry": lpIlsFwdrLtFbMacEnetRowStatusEntry,
       "lpIlsFwdrLtFbMacEnetRowStatus": lpIlsFwdrLtFbMacEnetRowStatus,
       "lpIlsFwdrLtFbMacEnetComponentName": lpIlsFwdrLtFbMacEnetComponentName,
       "lpIlsFwdrLtFbMacEnetStorageType": lpIlsFwdrLtFbMacEnetStorageType,
       "lpIlsFwdrLtFbMacEnetIndex": lpIlsFwdrLtFbMacEnetIndex,
       "lpIlsFwdrLtFbMacEnetTopTable": lpIlsFwdrLtFbMacEnetTopTable,
       "lpIlsFwdrLtFbMacEnetTopEntry": lpIlsFwdrLtFbMacEnetTopEntry,
       "lpIlsFwdrLtFbMacEnetTData": lpIlsFwdrLtFbMacEnetTData,
       "lpIlsFwdrLtFbMacTr": lpIlsFwdrLtFbMacTr,
       "lpIlsFwdrLtFbMacTrRowStatusTable": lpIlsFwdrLtFbMacTrRowStatusTable,
       "lpIlsFwdrLtFbMacTrRowStatusEntry": lpIlsFwdrLtFbMacTrRowStatusEntry,
       "lpIlsFwdrLtFbMacTrRowStatus": lpIlsFwdrLtFbMacTrRowStatus,
       "lpIlsFwdrLtFbMacTrComponentName": lpIlsFwdrLtFbMacTrComponentName,
       "lpIlsFwdrLtFbMacTrStorageType": lpIlsFwdrLtFbMacTrStorageType,
       "lpIlsFwdrLtFbMacTrIndex": lpIlsFwdrLtFbMacTrIndex,
       "lpIlsFwdrLtFbMacTrTopTable": lpIlsFwdrLtFbMacTrTopTable,
       "lpIlsFwdrLtFbMacTrTopEntry": lpIlsFwdrLtFbMacTrTopEntry,
       "lpIlsFwdrLtFbMacTrTData": lpIlsFwdrLtFbMacTrTData,
       "lpIlsFwdrLtFbData": lpIlsFwdrLtFbData,
       "lpIlsFwdrLtFbDataRowStatusTable": lpIlsFwdrLtFbDataRowStatusTable,
       "lpIlsFwdrLtFbDataRowStatusEntry": lpIlsFwdrLtFbDataRowStatusEntry,
       "lpIlsFwdrLtFbDataRowStatus": lpIlsFwdrLtFbDataRowStatus,
       "lpIlsFwdrLtFbDataComponentName": lpIlsFwdrLtFbDataComponentName,
       "lpIlsFwdrLtFbDataStorageType": lpIlsFwdrLtFbDataStorageType,
       "lpIlsFwdrLtFbDataIndex": lpIlsFwdrLtFbDataIndex,
       "lpIlsFwdrLtFbDataTopTable": lpIlsFwdrLtFbDataTopTable,
       "lpIlsFwdrLtFbDataTopEntry": lpIlsFwdrLtFbDataTopEntry,
       "lpIlsFwdrLtFbDataTData": lpIlsFwdrLtFbDataTData,
       "lpIlsFwdrLtFbIpH": lpIlsFwdrLtFbIpH,
       "lpIlsFwdrLtFbIpHRowStatusTable": lpIlsFwdrLtFbIpHRowStatusTable,
       "lpIlsFwdrLtFbIpHRowStatusEntry": lpIlsFwdrLtFbIpHRowStatusEntry,
       "lpIlsFwdrLtFbIpHRowStatus": lpIlsFwdrLtFbIpHRowStatus,
       "lpIlsFwdrLtFbIpHComponentName": lpIlsFwdrLtFbIpHComponentName,
       "lpIlsFwdrLtFbIpHStorageType": lpIlsFwdrLtFbIpHStorageType,
       "lpIlsFwdrLtFbIpHIndex": lpIlsFwdrLtFbIpHIndex,
       "lpIlsFwdrLtFbIpHTopTable": lpIlsFwdrLtFbIpHTopTable,
       "lpIlsFwdrLtFbIpHTopEntry": lpIlsFwdrLtFbIpHTopEntry,
       "lpIlsFwdrLtFbIpHTData": lpIlsFwdrLtFbIpHTData,
       "lpIlsFwdrLtFbLlch": lpIlsFwdrLtFbLlch,
       "lpIlsFwdrLtFbLlchRowStatusTable": lpIlsFwdrLtFbLlchRowStatusTable,
       "lpIlsFwdrLtFbLlchRowStatusEntry": lpIlsFwdrLtFbLlchRowStatusEntry,
       "lpIlsFwdrLtFbLlchRowStatus": lpIlsFwdrLtFbLlchRowStatus,
       "lpIlsFwdrLtFbLlchComponentName": lpIlsFwdrLtFbLlchComponentName,
       "lpIlsFwdrLtFbLlchStorageType": lpIlsFwdrLtFbLlchStorageType,
       "lpIlsFwdrLtFbLlchIndex": lpIlsFwdrLtFbLlchIndex,
       "lpIlsFwdrLtFbLlchTopTable": lpIlsFwdrLtFbLlchTopTable,
       "lpIlsFwdrLtFbLlchTopEntry": lpIlsFwdrLtFbLlchTopEntry,
       "lpIlsFwdrLtFbLlchTData": lpIlsFwdrLtFbLlchTData,
       "lpIlsFwdrLtFbAppleH": lpIlsFwdrLtFbAppleH,
       "lpIlsFwdrLtFbAppleHRowStatusTable": lpIlsFwdrLtFbAppleHRowStatusTable,
       "lpIlsFwdrLtFbAppleHRowStatusEntry": lpIlsFwdrLtFbAppleHRowStatusEntry,
       "lpIlsFwdrLtFbAppleHRowStatus": lpIlsFwdrLtFbAppleHRowStatus,
       "lpIlsFwdrLtFbAppleHComponentName": lpIlsFwdrLtFbAppleHComponentName,
       "lpIlsFwdrLtFbAppleHStorageType": lpIlsFwdrLtFbAppleHStorageType,
       "lpIlsFwdrLtFbAppleHIndex": lpIlsFwdrLtFbAppleHIndex,
       "lpIlsFwdrLtFbAppleHTopTable": lpIlsFwdrLtFbAppleHTopTable,
       "lpIlsFwdrLtFbAppleHTopEntry": lpIlsFwdrLtFbAppleHTopEntry,
       "lpIlsFwdrLtFbAppleHTData": lpIlsFwdrLtFbAppleHTData,
       "lpIlsFwdrLtFbIpxH": lpIlsFwdrLtFbIpxH,
       "lpIlsFwdrLtFbIpxHRowStatusTable": lpIlsFwdrLtFbIpxHRowStatusTable,
       "lpIlsFwdrLtFbIpxHRowStatusEntry": lpIlsFwdrLtFbIpxHRowStatusEntry,
       "lpIlsFwdrLtFbIpxHRowStatus": lpIlsFwdrLtFbIpxHRowStatus,
       "lpIlsFwdrLtFbIpxHComponentName": lpIlsFwdrLtFbIpxHComponentName,
       "lpIlsFwdrLtFbIpxHStorageType": lpIlsFwdrLtFbIpxHStorageType,
       "lpIlsFwdrLtFbIpxHIndex": lpIlsFwdrLtFbIpxHIndex,
       "lpIlsFwdrLtFbIpxHTopTable": lpIlsFwdrLtFbIpxHTopTable,
       "lpIlsFwdrLtFbIpxHTopEntry": lpIlsFwdrLtFbIpxHTopEntry,
       "lpIlsFwdrLtFbIpxHTData": lpIlsFwdrLtFbIpxHTData,
       "lpIlsFwdrLtFbTopTable": lpIlsFwdrLtFbTopTable,
       "lpIlsFwdrLtFbTopEntry": lpIlsFwdrLtFbTopEntry,
       "lpIlsFwdrLtFbTData": lpIlsFwdrLtFbTData,
       "lpIlsFwdrLtCntl": lpIlsFwdrLtCntl,
       "lpIlsFwdrLtCntlRowStatusTable": lpIlsFwdrLtCntlRowStatusTable,
       "lpIlsFwdrLtCntlRowStatusEntry": lpIlsFwdrLtCntlRowStatusEntry,
       "lpIlsFwdrLtCntlRowStatus": lpIlsFwdrLtCntlRowStatus,
       "lpIlsFwdrLtCntlComponentName": lpIlsFwdrLtCntlComponentName,
       "lpIlsFwdrLtCntlStorageType": lpIlsFwdrLtCntlStorageType,
       "lpIlsFwdrLtCntlIndex": lpIlsFwdrLtCntlIndex,
       "lpIlsFwdrLtCntlTopTable": lpIlsFwdrLtCntlTopTable,
       "lpIlsFwdrLtCntlTopEntry": lpIlsFwdrLtCntlTopEntry,
       "lpIlsFwdrLtCntlTData": lpIlsFwdrLtCntlTData,
       "lpIlsFwdrLtTopTable": lpIlsFwdrLtTopTable,
       "lpIlsFwdrLtTopEntry": lpIlsFwdrLtTopEntry,
       "lpIlsFwdrLtTData": lpIlsFwdrLtTData,
       "lpIlsFwdrTest": lpIlsFwdrTest,
       "lpIlsFwdrTestRowStatusTable": lpIlsFwdrTestRowStatusTable,
       "lpIlsFwdrTestRowStatusEntry": lpIlsFwdrTestRowStatusEntry,
       "lpIlsFwdrTestRowStatus": lpIlsFwdrTestRowStatus,
       "lpIlsFwdrTestComponentName": lpIlsFwdrTestComponentName,
       "lpIlsFwdrTestStorageType": lpIlsFwdrTestStorageType,
       "lpIlsFwdrTestIndex": lpIlsFwdrTestIndex,
       "lpIlsFwdrTestPTOTable": lpIlsFwdrTestPTOTable,
       "lpIlsFwdrTestPTOEntry": lpIlsFwdrTestPTOEntry,
       "lpIlsFwdrTestType": lpIlsFwdrTestType,
       "lpIlsFwdrTestFrmSize": lpIlsFwdrTestFrmSize,
       "lpIlsFwdrTestDuration": lpIlsFwdrTestDuration,
       "lpIlsFwdrTestResultsTable": lpIlsFwdrTestResultsTable,
       "lpIlsFwdrTestResultsEntry": lpIlsFwdrTestResultsEntry,
       "lpIlsFwdrTestElapsedTime": lpIlsFwdrTestElapsedTime,
       "lpIlsFwdrTestTimeRemaining": lpIlsFwdrTestTimeRemaining,
       "lpIlsFwdrTestCauseOfTermination": lpIlsFwdrTestCauseOfTermination,
       "lpIlsFwdrTestFrmTx": lpIlsFwdrTestFrmTx,
       "lpIlsFwdrTestBitsTx": lpIlsFwdrTestBitsTx,
       "lpIlsFwdrTestFrmRx": lpIlsFwdrTestFrmRx,
       "lpIlsFwdrTestBitsRx": lpIlsFwdrTestBitsRx,
       "lpIlsFwdrTestErroredFrmRx": lpIlsFwdrTestErroredFrmRx,
       "lpIlsFwdrIfEntryTable": lpIlsFwdrIfEntryTable,
       "lpIlsFwdrIfEntryEntry": lpIlsFwdrIfEntryEntry,
       "lpIlsFwdrIfAdminStatus": lpIlsFwdrIfAdminStatus,
       "lpIlsFwdrIfIndex": lpIlsFwdrIfIndex,
       "lpIlsFwdrStateTable": lpIlsFwdrStateTable,
       "lpIlsFwdrStateEntry": lpIlsFwdrStateEntry,
       "lpIlsFwdrAdminState": lpIlsFwdrAdminState,
       "lpIlsFwdrOperationalState": lpIlsFwdrOperationalState,
       "lpIlsFwdrUsageState": lpIlsFwdrUsageState,
       "lpIlsFwdrOperStatusTable": lpIlsFwdrOperStatusTable,
       "lpIlsFwdrOperStatusEntry": lpIlsFwdrOperStatusEntry,
       "lpIlsFwdrSnmpOperStatus": lpIlsFwdrSnmpOperStatus,
       "lpIlsFwdrStatsTable": lpIlsFwdrStatsTable,
       "lpIlsFwdrStatsEntry": lpIlsFwdrStatsEntry,
       "lpIlsFwdrFramesReceived": lpIlsFwdrFramesReceived,
       "lpIlsFwdrProcessedCount": lpIlsFwdrProcessedCount,
       "lpIlsFwdrErrorCount": lpIlsFwdrErrorCount,
       "lpIlsFwdrFramesDiscarded": lpIlsFwdrFramesDiscarded,
       "lpIlsFwdrLinkToTrafficSourceTable": lpIlsFwdrLinkToTrafficSourceTable,
       "lpIlsFwdrLinkToTrafficSourceEntry": lpIlsFwdrLinkToTrafficSourceEntry,
       "lpIlsFwdrLinkToTrafficSourceValue": lpIlsFwdrLinkToTrafficSourceValue,
       "lpEth100": lpEth100,
       "lpEth100RowStatusTable": lpEth100RowStatusTable,
       "lpEth100RowStatusEntry": lpEth100RowStatusEntry,
       "lpEth100RowStatus": lpEth100RowStatus,
       "lpEth100ComponentName": lpEth100ComponentName,
       "lpEth100StorageType": lpEth100StorageType,
       "lpEth100Index": lpEth100Index,
       "lpEth100Lt": lpEth100Lt,
       "lpEth100LtRowStatusTable": lpEth100LtRowStatusTable,
       "lpEth100LtRowStatusEntry": lpEth100LtRowStatusEntry,
       "lpEth100LtRowStatus": lpEth100LtRowStatus,
       "lpEth100LtComponentName": lpEth100LtComponentName,
       "lpEth100LtStorageType": lpEth100LtStorageType,
       "lpEth100LtIndex": lpEth100LtIndex,
       "lpEth100LtFrmCmp": lpEth100LtFrmCmp,
       "lpEth100LtFrmCmpRowStatusTable": lpEth100LtFrmCmpRowStatusTable,
       "lpEth100LtFrmCmpRowStatusEntry": lpEth100LtFrmCmpRowStatusEntry,
       "lpEth100LtFrmCmpRowStatus": lpEth100LtFrmCmpRowStatus,
       "lpEth100LtFrmCmpComponentName": lpEth100LtFrmCmpComponentName,
       "lpEth100LtFrmCmpStorageType": lpEth100LtFrmCmpStorageType,
       "lpEth100LtFrmCmpIndex": lpEth100LtFrmCmpIndex,
       "lpEth100LtFrmCmpTopTable": lpEth100LtFrmCmpTopTable,
       "lpEth100LtFrmCmpTopEntry": lpEth100LtFrmCmpTopEntry,
       "lpEth100LtFrmCmpTData": lpEth100LtFrmCmpTData,
       "lpEth100LtFrmCpy": lpEth100LtFrmCpy,
       "lpEth100LtFrmCpyRowStatusTable": lpEth100LtFrmCpyRowStatusTable,
       "lpEth100LtFrmCpyRowStatusEntry": lpEth100LtFrmCpyRowStatusEntry,
       "lpEth100LtFrmCpyRowStatus": lpEth100LtFrmCpyRowStatus,
       "lpEth100LtFrmCpyComponentName": lpEth100LtFrmCpyComponentName,
       "lpEth100LtFrmCpyStorageType": lpEth100LtFrmCpyStorageType,
       "lpEth100LtFrmCpyIndex": lpEth100LtFrmCpyIndex,
       "lpEth100LtFrmCpyTopTable": lpEth100LtFrmCpyTopTable,
       "lpEth100LtFrmCpyTopEntry": lpEth100LtFrmCpyTopEntry,
       "lpEth100LtFrmCpyTData": lpEth100LtFrmCpyTData,
       "lpEth100LtPrtCfg": lpEth100LtPrtCfg,
       "lpEth100LtPrtCfgRowStatusTable": lpEth100LtPrtCfgRowStatusTable,
       "lpEth100LtPrtCfgRowStatusEntry": lpEth100LtPrtCfgRowStatusEntry,
       "lpEth100LtPrtCfgRowStatus": lpEth100LtPrtCfgRowStatus,
       "lpEth100LtPrtCfgComponentName": lpEth100LtPrtCfgComponentName,
       "lpEth100LtPrtCfgStorageType": lpEth100LtPrtCfgStorageType,
       "lpEth100LtPrtCfgIndex": lpEth100LtPrtCfgIndex,
       "lpEth100LtPrtCfgTopTable": lpEth100LtPrtCfgTopTable,
       "lpEth100LtPrtCfgTopEntry": lpEth100LtPrtCfgTopEntry,
       "lpEth100LtPrtCfgTData": lpEth100LtPrtCfgTData,
       "lpEth100LtFb": lpEth100LtFb,
       "lpEth100LtFbRowStatusTable": lpEth100LtFbRowStatusTable,
       "lpEth100LtFbRowStatusEntry": lpEth100LtFbRowStatusEntry,
       "lpEth100LtFbRowStatus": lpEth100LtFbRowStatus,
       "lpEth100LtFbComponentName": lpEth100LtFbComponentName,
       "lpEth100LtFbStorageType": lpEth100LtFbStorageType,
       "lpEth100LtFbIndex": lpEth100LtFbIndex,
       "lpEth100LtFbTxInfo": lpEth100LtFbTxInfo,
       "lpEth100LtFbTxInfoRowStatusTable": lpEth100LtFbTxInfoRowStatusTable,
       "lpEth100LtFbTxInfoRowStatusEntry": lpEth100LtFbTxInfoRowStatusEntry,
       "lpEth100LtFbTxInfoRowStatus": lpEth100LtFbTxInfoRowStatus,
       "lpEth100LtFbTxInfoComponentName": lpEth100LtFbTxInfoComponentName,
       "lpEth100LtFbTxInfoStorageType": lpEth100LtFbTxInfoStorageType,
       "lpEth100LtFbTxInfoIndex": lpEth100LtFbTxInfoIndex,
       "lpEth100LtFbTxInfoTopTable": lpEth100LtFbTxInfoTopTable,
       "lpEth100LtFbTxInfoTopEntry": lpEth100LtFbTxInfoTopEntry,
       "lpEth100LtFbTxInfoTData": lpEth100LtFbTxInfoTData,
       "lpEth100LtFbFddiMac": lpEth100LtFbFddiMac,
       "lpEth100LtFbFddiMacRowStatusTable": lpEth100LtFbFddiMacRowStatusTable,
       "lpEth100LtFbFddiMacRowStatusEntry": lpEth100LtFbFddiMacRowStatusEntry,
       "lpEth100LtFbFddiMacRowStatus": lpEth100LtFbFddiMacRowStatus,
       "lpEth100LtFbFddiMacComponentName": lpEth100LtFbFddiMacComponentName,
       "lpEth100LtFbFddiMacStorageType": lpEth100LtFbFddiMacStorageType,
       "lpEth100LtFbFddiMacIndex": lpEth100LtFbFddiMacIndex,
       "lpEth100LtFbFddiMacTopTable": lpEth100LtFbFddiMacTopTable,
       "lpEth100LtFbFddiMacTopEntry": lpEth100LtFbFddiMacTopEntry,
       "lpEth100LtFbFddiMacTData": lpEth100LtFbFddiMacTData,
       "lpEth100LtFbMacEnet": lpEth100LtFbMacEnet,
       "lpEth100LtFbMacEnetRowStatusTable": lpEth100LtFbMacEnetRowStatusTable,
       "lpEth100LtFbMacEnetRowStatusEntry": lpEth100LtFbMacEnetRowStatusEntry,
       "lpEth100LtFbMacEnetRowStatus": lpEth100LtFbMacEnetRowStatus,
       "lpEth100LtFbMacEnetComponentName": lpEth100LtFbMacEnetComponentName,
       "lpEth100LtFbMacEnetStorageType": lpEth100LtFbMacEnetStorageType,
       "lpEth100LtFbMacEnetIndex": lpEth100LtFbMacEnetIndex,
       "lpEth100LtFbMacEnetTopTable": lpEth100LtFbMacEnetTopTable,
       "lpEth100LtFbMacEnetTopEntry": lpEth100LtFbMacEnetTopEntry,
       "lpEth100LtFbMacEnetTData": lpEth100LtFbMacEnetTData,
       "lpEth100LtFbMacTr": lpEth100LtFbMacTr,
       "lpEth100LtFbMacTrRowStatusTable": lpEth100LtFbMacTrRowStatusTable,
       "lpEth100LtFbMacTrRowStatusEntry": lpEth100LtFbMacTrRowStatusEntry,
       "lpEth100LtFbMacTrRowStatus": lpEth100LtFbMacTrRowStatus,
       "lpEth100LtFbMacTrComponentName": lpEth100LtFbMacTrComponentName,
       "lpEth100LtFbMacTrStorageType": lpEth100LtFbMacTrStorageType,
       "lpEth100LtFbMacTrIndex": lpEth100LtFbMacTrIndex,
       "lpEth100LtFbMacTrTopTable": lpEth100LtFbMacTrTopTable,
       "lpEth100LtFbMacTrTopEntry": lpEth100LtFbMacTrTopEntry,
       "lpEth100LtFbMacTrTData": lpEth100LtFbMacTrTData,
       "lpEth100LtFbData": lpEth100LtFbData,
       "lpEth100LtFbDataRowStatusTable": lpEth100LtFbDataRowStatusTable,
       "lpEth100LtFbDataRowStatusEntry": lpEth100LtFbDataRowStatusEntry,
       "lpEth100LtFbDataRowStatus": lpEth100LtFbDataRowStatus,
       "lpEth100LtFbDataComponentName": lpEth100LtFbDataComponentName,
       "lpEth100LtFbDataStorageType": lpEth100LtFbDataStorageType,
       "lpEth100LtFbDataIndex": lpEth100LtFbDataIndex,
       "lpEth100LtFbDataTopTable": lpEth100LtFbDataTopTable,
       "lpEth100LtFbDataTopEntry": lpEth100LtFbDataTopEntry,
       "lpEth100LtFbDataTData": lpEth100LtFbDataTData,
       "lpEth100LtFbIpH": lpEth100LtFbIpH,
       "lpEth100LtFbIpHRowStatusTable": lpEth100LtFbIpHRowStatusTable,
       "lpEth100LtFbIpHRowStatusEntry": lpEth100LtFbIpHRowStatusEntry,
       "lpEth100LtFbIpHRowStatus": lpEth100LtFbIpHRowStatus,
       "lpEth100LtFbIpHComponentName": lpEth100LtFbIpHComponentName,
       "lpEth100LtFbIpHStorageType": lpEth100LtFbIpHStorageType,
       "lpEth100LtFbIpHIndex": lpEth100LtFbIpHIndex,
       "lpEth100LtFbIpHTopTable": lpEth100LtFbIpHTopTable,
       "lpEth100LtFbIpHTopEntry": lpEth100LtFbIpHTopEntry,
       "lpEth100LtFbIpHTData": lpEth100LtFbIpHTData,
       "lpEth100LtFbLlch": lpEth100LtFbLlch,
       "lpEth100LtFbLlchRowStatusTable": lpEth100LtFbLlchRowStatusTable,
       "lpEth100LtFbLlchRowStatusEntry": lpEth100LtFbLlchRowStatusEntry,
       "lpEth100LtFbLlchRowStatus": lpEth100LtFbLlchRowStatus,
       "lpEth100LtFbLlchComponentName": lpEth100LtFbLlchComponentName,
       "lpEth100LtFbLlchStorageType": lpEth100LtFbLlchStorageType,
       "lpEth100LtFbLlchIndex": lpEth100LtFbLlchIndex,
       "lpEth100LtFbLlchTopTable": lpEth100LtFbLlchTopTable,
       "lpEth100LtFbLlchTopEntry": lpEth100LtFbLlchTopEntry,
       "lpEth100LtFbLlchTData": lpEth100LtFbLlchTData,
       "lpEth100LtFbAppleH": lpEth100LtFbAppleH,
       "lpEth100LtFbAppleHRowStatusTable": lpEth100LtFbAppleHRowStatusTable,
       "lpEth100LtFbAppleHRowStatusEntry": lpEth100LtFbAppleHRowStatusEntry,
       "lpEth100LtFbAppleHRowStatus": lpEth100LtFbAppleHRowStatus,
       "lpEth100LtFbAppleHComponentName": lpEth100LtFbAppleHComponentName,
       "lpEth100LtFbAppleHStorageType": lpEth100LtFbAppleHStorageType,
       "lpEth100LtFbAppleHIndex": lpEth100LtFbAppleHIndex,
       "lpEth100LtFbAppleHTopTable": lpEth100LtFbAppleHTopTable,
       "lpEth100LtFbAppleHTopEntry": lpEth100LtFbAppleHTopEntry,
       "lpEth100LtFbAppleHTData": lpEth100LtFbAppleHTData,
       "lpEth100LtFbIpxH": lpEth100LtFbIpxH,
       "lpEth100LtFbIpxHRowStatusTable": lpEth100LtFbIpxHRowStatusTable,
       "lpEth100LtFbIpxHRowStatusEntry": lpEth100LtFbIpxHRowStatusEntry,
       "lpEth100LtFbIpxHRowStatus": lpEth100LtFbIpxHRowStatus,
       "lpEth100LtFbIpxHComponentName": lpEth100LtFbIpxHComponentName,
       "lpEth100LtFbIpxHStorageType": lpEth100LtFbIpxHStorageType,
       "lpEth100LtFbIpxHIndex": lpEth100LtFbIpxHIndex,
       "lpEth100LtFbIpxHTopTable": lpEth100LtFbIpxHTopTable,
       "lpEth100LtFbIpxHTopEntry": lpEth100LtFbIpxHTopEntry,
       "lpEth100LtFbIpxHTData": lpEth100LtFbIpxHTData,
       "lpEth100LtFbTopTable": lpEth100LtFbTopTable,
       "lpEth100LtFbTopEntry": lpEth100LtFbTopEntry,
       "lpEth100LtFbTData": lpEth100LtFbTData,
       "lpEth100LtCntl": lpEth100LtCntl,
       "lpEth100LtCntlRowStatusTable": lpEth100LtCntlRowStatusTable,
       "lpEth100LtCntlRowStatusEntry": lpEth100LtCntlRowStatusEntry,
       "lpEth100LtCntlRowStatus": lpEth100LtCntlRowStatus,
       "lpEth100LtCntlComponentName": lpEth100LtCntlComponentName,
       "lpEth100LtCntlStorageType": lpEth100LtCntlStorageType,
       "lpEth100LtCntlIndex": lpEth100LtCntlIndex,
       "lpEth100LtCntlTopTable": lpEth100LtCntlTopTable,
       "lpEth100LtCntlTopEntry": lpEth100LtCntlTopEntry,
       "lpEth100LtCntlTData": lpEth100LtCntlTData,
       "lpEth100LtTopTable": lpEth100LtTopTable,
       "lpEth100LtTopEntry": lpEth100LtTopEntry,
       "lpEth100LtTData": lpEth100LtTData,
       "lpEth100Test": lpEth100Test,
       "lpEth100TestRowStatusTable": lpEth100TestRowStatusTable,
       "lpEth100TestRowStatusEntry": lpEth100TestRowStatusEntry,
       "lpEth100TestRowStatus": lpEth100TestRowStatus,
       "lpEth100TestComponentName": lpEth100TestComponentName,
       "lpEth100TestStorageType": lpEth100TestStorageType,
       "lpEth100TestIndex": lpEth100TestIndex,
       "lpEth100TestPTOTable": lpEth100TestPTOTable,
       "lpEth100TestPTOEntry": lpEth100TestPTOEntry,
       "lpEth100TestType": lpEth100TestType,
       "lpEth100TestFrmSize": lpEth100TestFrmSize,
       "lpEth100TestDuration": lpEth100TestDuration,
       "lpEth100TestResultsTable": lpEth100TestResultsTable,
       "lpEth100TestResultsEntry": lpEth100TestResultsEntry,
       "lpEth100TestElapsedTime": lpEth100TestElapsedTime,
       "lpEth100TestTimeRemaining": lpEth100TestTimeRemaining,
       "lpEth100TestCauseOfTermination": lpEth100TestCauseOfTermination,
       "lpEth100TestFrmTx": lpEth100TestFrmTx,
       "lpEth100TestBitsTx": lpEth100TestBitsTx,
       "lpEth100TestFrmRx": lpEth100TestFrmRx,
       "lpEth100TestBitsRx": lpEth100TestBitsRx,
       "lpEth100TestErroredFrmRx": lpEth100TestErroredFrmRx,
       "lpEth100CidDataTable": lpEth100CidDataTable,
       "lpEth100CidDataEntry": lpEth100CidDataEntry,
       "lpEth100CustomerIdentifier": lpEth100CustomerIdentifier,
       "lpEth100IfEntryTable": lpEth100IfEntryTable,
       "lpEth100IfEntryEntry": lpEth100IfEntryEntry,
       "lpEth100IfAdminStatus": lpEth100IfAdminStatus,
       "lpEth100IfIndex": lpEth100IfIndex,
       "lpEth100ProvTable": lpEth100ProvTable,
       "lpEth100ProvEntry": lpEth100ProvEntry,
       "lpEth100DuplexMode": lpEth100DuplexMode,
       "lpEth100LineSpeed": lpEth100LineSpeed,
       "lpEth100AutoNegotiation": lpEth100AutoNegotiation,
       "lpEth100ApplicationFramerName": lpEth100ApplicationFramerName,
       "lpEth100AdminInfoTable": lpEth100AdminInfoTable,
       "lpEth100AdminInfoEntry": lpEth100AdminInfoEntry,
       "lpEth100Vendor": lpEth100Vendor,
       "lpEth100CommentText": lpEth100CommentText,
       "lpEth100StateTable": lpEth100StateTable,
       "lpEth100StateEntry": lpEth100StateEntry,
       "lpEth100AdminState": lpEth100AdminState,
       "lpEth100OperationalState": lpEth100OperationalState,
       "lpEth100UsageState": lpEth100UsageState,
       "lpEth100OperStatusTable": lpEth100OperStatusTable,
       "lpEth100OperStatusEntry": lpEth100OperStatusEntry,
       "lpEth100SnmpOperStatus": lpEth100SnmpOperStatus,
       "lpEth100OperTable": lpEth100OperTable,
       "lpEth100OperEntry": lpEth100OperEntry,
       "lpEth100MacAddress": lpEth100MacAddress,
       "lpEth100AutoNegStatus": lpEth100AutoNegStatus,
       "lpEth100ActualLineSpeed": lpEth100ActualLineSpeed,
       "lpEth100ActualDuplexMode": lpEth100ActualDuplexMode,
       "lpEth100Eth100StatsTable": lpEth100Eth100StatsTable,
       "lpEth100Eth100StatsEntry": lpEth100Eth100StatsEntry,
       "lpEth100FramesTransmittedOk": lpEth100FramesTransmittedOk,
       "lpEth100FramesReceivedOk": lpEth100FramesReceivedOk,
       "lpEth100OctetsTransmittedOk": lpEth100OctetsTransmittedOk,
       "lpEth100OctetsReceivedOk": lpEth100OctetsReceivedOk,
       "lpEth100UndersizeFrames": lpEth100UndersizeFrames,
       "lpEth100ReceivedOctetsIntoRouterBr": lpEth100ReceivedOctetsIntoRouterBr,
       "lpEth100ReceivedFramesIntoRouterBr": lpEth100ReceivedFramesIntoRouterBr,
       "lpEth100StatsTable": lpEth100StatsTable,
       "lpEth100StatsEntry": lpEth100StatsEntry,
       "lpEth100AlignmentErrors": lpEth100AlignmentErrors,
       "lpEth100FcsErrors": lpEth100FcsErrors,
       "lpEth100SingleCollisionFrames": lpEth100SingleCollisionFrames,
       "lpEth100MultipleCollisionFrames": lpEth100MultipleCollisionFrames,
       "lpEth100SqeTestErrors": lpEth100SqeTestErrors,
       "lpEth100DeferredTransmissions": lpEth100DeferredTransmissions,
       "lpEth100LateCollisions": lpEth100LateCollisions,
       "lpEth100ExcessiveCollisions": lpEth100ExcessiveCollisions,
       "lpEth100MacTransmitErrors": lpEth100MacTransmitErrors,
       "lpEth100CarrierSenseErrors": lpEth100CarrierSenseErrors,
       "lpEth100FrameTooLongs": lpEth100FrameTooLongs,
       "lpEth100MacReceiveErrors": lpEth100MacReceiveErrors,
       "la": la,
       "laRowStatusTable": laRowStatusTable,
       "laRowStatusEntry": laRowStatusEntry,
       "laRowStatus": laRowStatus,
       "laComponentName": laComponentName,
       "laStorageType": laStorageType,
       "laIndex": laIndex,
       "laFramer": laFramer,
       "laFramerRowStatusTable": laFramerRowStatusTable,
       "laFramerRowStatusEntry": laFramerRowStatusEntry,
       "laFramerRowStatus": laFramerRowStatus,
       "laFramerComponentName": laFramerComponentName,
       "laFramerStorageType": laFramerStorageType,
       "laFramerIndex": laFramerIndex,
       "laFramerProvTable": laFramerProvTable,
       "laFramerProvEntry": laFramerProvEntry,
       "laFramerInterfaceName": laFramerInterfaceName,
       "laFramerInterfaceNamesTable": laFramerInterfaceNamesTable,
       "laFramerInterfaceNamesEntry": laFramerInterfaceNamesEntry,
       "laFramerInterfaceNamesValue": laFramerInterfaceNamesValue,
       "laFramerInterfaceNamesRowStatus": laFramerInterfaceNamesRowStatus,
       "laCidDataTable": laCidDataTable,
       "laCidDataEntry": laCidDataEntry,
       "laCustomerIdentifier": laCustomerIdentifier,
       "laMediaProvTable": laMediaProvTable,
       "laMediaProvEntry": laMediaProvEntry,
       "laLinkToProtocolPort": laLinkToProtocolPort,
       "laIfEntryTable": laIfEntryTable,
       "laIfEntryEntry": laIfEntryEntry,
       "laIfAdminStatus": laIfAdminStatus,
       "laIfIndex": laIfIndex,
       "laStateTable": laStateTable,
       "laStateEntry": laStateEntry,
       "laAdminState": laAdminState,
       "laOperationalState": laOperationalState,
       "laUsageState": laUsageState,
       "laOperStatusTable": laOperStatusTable,
       "laOperStatusEntry": laOperStatusEntry,
       "laSnmpOperStatus": laSnmpOperStatus,
       "lanDriversMIB": lanDriversMIB,
       "lanDriversGroup": lanDriversGroup,
       "lanDriversGroupBE": lanDriversGroupBE,
       "lanDriversGroupBE01": lanDriversGroupBE01,
       "lanDriversGroupBE01A": lanDriversGroupBE01A,
       "lanDriversCapabilities": lanDriversCapabilities,
       "lanDriversCapabilitiesBE": lanDriversCapabilitiesBE,
       "lanDriversCapabilitiesBE01": lanDriversCapabilitiesBE01,
       "lanDriversCapabilitiesBE01A": lanDriversCapabilitiesBE01A}
)
