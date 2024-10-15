# SNMP MIB module (Nortel-MsCarrier-MscPassport-LanDriversMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-LanDriversMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:44 2024
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

(mscLp,
 mscLpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB",
    "mscLp",
    "mscLpIndex")

(Counter32,
 DisplayString,
 FddiMACLongAddressType,
 FddiTimeMilli,
 FddiTimeNano,
 Gauge32,
 Integer32,
 InterfaceIndex,
 MacAddress,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "FddiMACLongAddressType",
    "FddiTimeMilli",
    "FddiTimeNano",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "Link",
    "NonReplicated",
    "PassportCounter64")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscLpEnet_ObjectIdentity = ObjectIdentity
mscLpEnet = _MscLpEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3)
)
_MscLpEnetRowStatusTable_Object = MibTable
mscLpEnetRowStatusTable = _MscLpEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetRowStatusTable.setStatus("mandatory")
_MscLpEnetRowStatusEntry_Object = MibTableRow
mscLpEnetRowStatusEntry = _MscLpEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 1, 1)
)
mscLpEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetRowStatusEntry.setStatus("mandatory")
_MscLpEnetRowStatus_Type = RowStatus
_MscLpEnetRowStatus_Object = MibTableColumn
mscLpEnetRowStatus = _MscLpEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 1, 1, 1),
    _MscLpEnetRowStatus_Type()
)
mscLpEnetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetRowStatus.setStatus("mandatory")
_MscLpEnetComponentName_Type = DisplayString
_MscLpEnetComponentName_Object = MibTableColumn
mscLpEnetComponentName = _MscLpEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 1, 1, 2),
    _MscLpEnetComponentName_Type()
)
mscLpEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetComponentName.setStatus("mandatory")
_MscLpEnetStorageType_Type = StorageType
_MscLpEnetStorageType_Object = MibTableColumn
mscLpEnetStorageType = _MscLpEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 1, 1, 4),
    _MscLpEnetStorageType_Type()
)
mscLpEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetStorageType.setStatus("mandatory")


class _MscLpEnetIndex_Type(Integer32):
    """Custom type mscLpEnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MscLpEnetIndex_Type.__name__ = "Integer32"
_MscLpEnetIndex_Object = MibTableColumn
mscLpEnetIndex = _MscLpEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 1, 1, 10),
    _MscLpEnetIndex_Type()
)
mscLpEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetIndex.setStatus("mandatory")
_MscLpEnetLt_ObjectIdentity = ObjectIdentity
mscLpEnetLt = _MscLpEnetLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2)
)
_MscLpEnetLtRowStatusTable_Object = MibTable
mscLpEnetLtRowStatusTable = _MscLpEnetLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtRowStatusTable.setStatus("mandatory")
_MscLpEnetLtRowStatusEntry_Object = MibTableRow
mscLpEnetLtRowStatusEntry = _MscLpEnetLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 1, 1)
)
mscLpEnetLtRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtRowStatus_Type = RowStatus
_MscLpEnetLtRowStatus_Object = MibTableColumn
mscLpEnetLtRowStatus = _MscLpEnetLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 1, 1, 1),
    _MscLpEnetLtRowStatus_Type()
)
mscLpEnetLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtRowStatus.setStatus("mandatory")
_MscLpEnetLtComponentName_Type = DisplayString
_MscLpEnetLtComponentName_Object = MibTableColumn
mscLpEnetLtComponentName = _MscLpEnetLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 1, 1, 2),
    _MscLpEnetLtComponentName_Type()
)
mscLpEnetLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtComponentName.setStatus("mandatory")
_MscLpEnetLtStorageType_Type = StorageType
_MscLpEnetLtStorageType_Object = MibTableColumn
mscLpEnetLtStorageType = _MscLpEnetLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 1, 1, 4),
    _MscLpEnetLtStorageType_Type()
)
mscLpEnetLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtStorageType.setStatus("mandatory")
_MscLpEnetLtIndex_Type = NonReplicated
_MscLpEnetLtIndex_Object = MibTableColumn
mscLpEnetLtIndex = _MscLpEnetLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 1, 1, 10),
    _MscLpEnetLtIndex_Type()
)
mscLpEnetLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtIndex.setStatus("mandatory")
_MscLpEnetLtFrmCmp_ObjectIdentity = ObjectIdentity
mscLpEnetLtFrmCmp = _MscLpEnetLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2)
)
_MscLpEnetLtFrmCmpRowStatusTable_Object = MibTable
mscLpEnetLtFrmCmpRowStatusTable = _MscLpEnetLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFrmCmpRowStatusEntry_Object = MibTableRow
mscLpEnetLtFrmCmpRowStatusEntry = _MscLpEnetLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 1, 1)
)
mscLpEnetLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFrmCmpRowStatus_Type = RowStatus
_MscLpEnetLtFrmCmpRowStatus_Object = MibTableColumn
mscLpEnetLtFrmCmpRowStatus = _MscLpEnetLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 1, 1, 1),
    _MscLpEnetLtFrmCmpRowStatus_Type()
)
mscLpEnetLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpRowStatus.setStatus("mandatory")
_MscLpEnetLtFrmCmpComponentName_Type = DisplayString
_MscLpEnetLtFrmCmpComponentName_Object = MibTableColumn
mscLpEnetLtFrmCmpComponentName = _MscLpEnetLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 1, 1, 2),
    _MscLpEnetLtFrmCmpComponentName_Type()
)
mscLpEnetLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpComponentName.setStatus("mandatory")
_MscLpEnetLtFrmCmpStorageType_Type = StorageType
_MscLpEnetLtFrmCmpStorageType_Object = MibTableColumn
mscLpEnetLtFrmCmpStorageType = _MscLpEnetLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 1, 1, 4),
    _MscLpEnetLtFrmCmpStorageType_Type()
)
mscLpEnetLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpStorageType.setStatus("mandatory")
_MscLpEnetLtFrmCmpIndex_Type = NonReplicated
_MscLpEnetLtFrmCmpIndex_Object = MibTableColumn
mscLpEnetLtFrmCmpIndex = _MscLpEnetLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 1, 1, 10),
    _MscLpEnetLtFrmCmpIndex_Type()
)
mscLpEnetLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpIndex.setStatus("mandatory")
_MscLpEnetLtFrmCmpTopTable_Object = MibTable
mscLpEnetLtFrmCmpTopTable = _MscLpEnetLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpTopTable.setStatus("mandatory")
_MscLpEnetLtFrmCmpTopEntry_Object = MibTableRow
mscLpEnetLtFrmCmpTopEntry = _MscLpEnetLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 10, 1)
)
mscLpEnetLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpTopEntry.setStatus("mandatory")


class _MscLpEnetLtFrmCmpTData_Type(AsciiString):
    """Custom type mscLpEnetLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFrmCmpTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFrmCmpTData_Object = MibTableColumn
mscLpEnetLtFrmCmpTData = _MscLpEnetLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 2, 10, 1, 1),
    _MscLpEnetLtFrmCmpTData_Type()
)
mscLpEnetLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCmpTData.setStatus("mandatory")
_MscLpEnetLtFrmCpy_ObjectIdentity = ObjectIdentity
mscLpEnetLtFrmCpy = _MscLpEnetLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3)
)
_MscLpEnetLtFrmCpyRowStatusTable_Object = MibTable
mscLpEnetLtFrmCpyRowStatusTable = _MscLpEnetLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFrmCpyRowStatusEntry_Object = MibTableRow
mscLpEnetLtFrmCpyRowStatusEntry = _MscLpEnetLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 1, 1)
)
mscLpEnetLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFrmCpyRowStatus_Type = RowStatus
_MscLpEnetLtFrmCpyRowStatus_Object = MibTableColumn
mscLpEnetLtFrmCpyRowStatus = _MscLpEnetLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 1, 1, 1),
    _MscLpEnetLtFrmCpyRowStatus_Type()
)
mscLpEnetLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyRowStatus.setStatus("mandatory")
_MscLpEnetLtFrmCpyComponentName_Type = DisplayString
_MscLpEnetLtFrmCpyComponentName_Object = MibTableColumn
mscLpEnetLtFrmCpyComponentName = _MscLpEnetLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 1, 1, 2),
    _MscLpEnetLtFrmCpyComponentName_Type()
)
mscLpEnetLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyComponentName.setStatus("mandatory")
_MscLpEnetLtFrmCpyStorageType_Type = StorageType
_MscLpEnetLtFrmCpyStorageType_Object = MibTableColumn
mscLpEnetLtFrmCpyStorageType = _MscLpEnetLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 1, 1, 4),
    _MscLpEnetLtFrmCpyStorageType_Type()
)
mscLpEnetLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyStorageType.setStatus("mandatory")
_MscLpEnetLtFrmCpyIndex_Type = NonReplicated
_MscLpEnetLtFrmCpyIndex_Object = MibTableColumn
mscLpEnetLtFrmCpyIndex = _MscLpEnetLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 1, 1, 10),
    _MscLpEnetLtFrmCpyIndex_Type()
)
mscLpEnetLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyIndex.setStatus("mandatory")
_MscLpEnetLtFrmCpyTopTable_Object = MibTable
mscLpEnetLtFrmCpyTopTable = _MscLpEnetLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyTopTable.setStatus("mandatory")
_MscLpEnetLtFrmCpyTopEntry_Object = MibTableRow
mscLpEnetLtFrmCpyTopEntry = _MscLpEnetLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 10, 1)
)
mscLpEnetLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyTopEntry.setStatus("mandatory")


class _MscLpEnetLtFrmCpyTData_Type(AsciiString):
    """Custom type mscLpEnetLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFrmCpyTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFrmCpyTData_Object = MibTableColumn
mscLpEnetLtFrmCpyTData = _MscLpEnetLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 3, 10, 1, 1),
    _MscLpEnetLtFrmCpyTData_Type()
)
mscLpEnetLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFrmCpyTData.setStatus("mandatory")
_MscLpEnetLtPrtCfg_ObjectIdentity = ObjectIdentity
mscLpEnetLtPrtCfg = _MscLpEnetLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4)
)
_MscLpEnetLtPrtCfgRowStatusTable_Object = MibTable
mscLpEnetLtPrtCfgRowStatusTable = _MscLpEnetLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgRowStatusTable.setStatus("mandatory")
_MscLpEnetLtPrtCfgRowStatusEntry_Object = MibTableRow
mscLpEnetLtPrtCfgRowStatusEntry = _MscLpEnetLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 1, 1)
)
mscLpEnetLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtPrtCfgRowStatus_Type = RowStatus
_MscLpEnetLtPrtCfgRowStatus_Object = MibTableColumn
mscLpEnetLtPrtCfgRowStatus = _MscLpEnetLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 1, 1, 1),
    _MscLpEnetLtPrtCfgRowStatus_Type()
)
mscLpEnetLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgRowStatus.setStatus("mandatory")
_MscLpEnetLtPrtCfgComponentName_Type = DisplayString
_MscLpEnetLtPrtCfgComponentName_Object = MibTableColumn
mscLpEnetLtPrtCfgComponentName = _MscLpEnetLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 1, 1, 2),
    _MscLpEnetLtPrtCfgComponentName_Type()
)
mscLpEnetLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgComponentName.setStatus("mandatory")
_MscLpEnetLtPrtCfgStorageType_Type = StorageType
_MscLpEnetLtPrtCfgStorageType_Object = MibTableColumn
mscLpEnetLtPrtCfgStorageType = _MscLpEnetLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 1, 1, 4),
    _MscLpEnetLtPrtCfgStorageType_Type()
)
mscLpEnetLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgStorageType.setStatus("mandatory")
_MscLpEnetLtPrtCfgIndex_Type = NonReplicated
_MscLpEnetLtPrtCfgIndex_Object = MibTableColumn
mscLpEnetLtPrtCfgIndex = _MscLpEnetLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 1, 1, 10),
    _MscLpEnetLtPrtCfgIndex_Type()
)
mscLpEnetLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgIndex.setStatus("mandatory")
_MscLpEnetLtPrtCfgTopTable_Object = MibTable
mscLpEnetLtPrtCfgTopTable = _MscLpEnetLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgTopTable.setStatus("mandatory")
_MscLpEnetLtPrtCfgTopEntry_Object = MibTableRow
mscLpEnetLtPrtCfgTopEntry = _MscLpEnetLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 10, 1)
)
mscLpEnetLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgTopEntry.setStatus("mandatory")


class _MscLpEnetLtPrtCfgTData_Type(AsciiString):
    """Custom type mscLpEnetLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtPrtCfgTData_Type.__name__ = "AsciiString"
_MscLpEnetLtPrtCfgTData_Object = MibTableColumn
mscLpEnetLtPrtCfgTData = _MscLpEnetLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 4, 10, 1, 1),
    _MscLpEnetLtPrtCfgTData_Type()
)
mscLpEnetLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtPrtCfgTData.setStatus("mandatory")
_MscLpEnetLtFb_ObjectIdentity = ObjectIdentity
mscLpEnetLtFb = _MscLpEnetLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5)
)
_MscLpEnetLtFbRowStatusTable_Object = MibTable
mscLpEnetLtFbRowStatusTable = _MscLpEnetLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbRowStatusEntry = _MscLpEnetLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 1, 1)
)
mscLpEnetLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbRowStatus_Type = RowStatus
_MscLpEnetLtFbRowStatus_Object = MibTableColumn
mscLpEnetLtFbRowStatus = _MscLpEnetLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 1, 1, 1),
    _MscLpEnetLtFbRowStatus_Type()
)
mscLpEnetLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbRowStatus.setStatus("mandatory")
_MscLpEnetLtFbComponentName_Type = DisplayString
_MscLpEnetLtFbComponentName_Object = MibTableColumn
mscLpEnetLtFbComponentName = _MscLpEnetLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 1, 1, 2),
    _MscLpEnetLtFbComponentName_Type()
)
mscLpEnetLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbComponentName.setStatus("mandatory")
_MscLpEnetLtFbStorageType_Type = StorageType
_MscLpEnetLtFbStorageType_Object = MibTableColumn
mscLpEnetLtFbStorageType = _MscLpEnetLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 1, 1, 4),
    _MscLpEnetLtFbStorageType_Type()
)
mscLpEnetLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbStorageType.setStatus("mandatory")
_MscLpEnetLtFbIndex_Type = NonReplicated
_MscLpEnetLtFbIndex_Object = MibTableColumn
mscLpEnetLtFbIndex = _MscLpEnetLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 1, 1, 10),
    _MscLpEnetLtFbIndex_Type()
)
mscLpEnetLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIndex.setStatus("mandatory")
_MscLpEnetLtFbTxInfo_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbTxInfo = _MscLpEnetLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2)
)
_MscLpEnetLtFbTxInfoRowStatusTable_Object = MibTable
mscLpEnetLtFbTxInfoRowStatusTable = _MscLpEnetLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbTxInfoRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbTxInfoRowStatusEntry = _MscLpEnetLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 1, 1)
)
mscLpEnetLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbTxInfoRowStatus_Type = RowStatus
_MscLpEnetLtFbTxInfoRowStatus_Object = MibTableColumn
mscLpEnetLtFbTxInfoRowStatus = _MscLpEnetLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 1, 1, 1),
    _MscLpEnetLtFbTxInfoRowStatus_Type()
)
mscLpEnetLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoRowStatus.setStatus("mandatory")
_MscLpEnetLtFbTxInfoComponentName_Type = DisplayString
_MscLpEnetLtFbTxInfoComponentName_Object = MibTableColumn
mscLpEnetLtFbTxInfoComponentName = _MscLpEnetLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 1, 1, 2),
    _MscLpEnetLtFbTxInfoComponentName_Type()
)
mscLpEnetLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoComponentName.setStatus("mandatory")
_MscLpEnetLtFbTxInfoStorageType_Type = StorageType
_MscLpEnetLtFbTxInfoStorageType_Object = MibTableColumn
mscLpEnetLtFbTxInfoStorageType = _MscLpEnetLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 1, 1, 4),
    _MscLpEnetLtFbTxInfoStorageType_Type()
)
mscLpEnetLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoStorageType.setStatus("mandatory")
_MscLpEnetLtFbTxInfoIndex_Type = NonReplicated
_MscLpEnetLtFbTxInfoIndex_Object = MibTableColumn
mscLpEnetLtFbTxInfoIndex = _MscLpEnetLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 1, 1, 10),
    _MscLpEnetLtFbTxInfoIndex_Type()
)
mscLpEnetLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoIndex.setStatus("mandatory")
_MscLpEnetLtFbTxInfoTopTable_Object = MibTable
mscLpEnetLtFbTxInfoTopTable = _MscLpEnetLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoTopTable.setStatus("mandatory")
_MscLpEnetLtFbTxInfoTopEntry_Object = MibTableRow
mscLpEnetLtFbTxInfoTopEntry = _MscLpEnetLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 10, 1)
)
mscLpEnetLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbTxInfoTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbTxInfoTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbTxInfoTData_Object = MibTableColumn
mscLpEnetLtFbTxInfoTData = _MscLpEnetLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 2, 10, 1, 1),
    _MscLpEnetLtFbTxInfoTData_Type()
)
mscLpEnetLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbTxInfoTData.setStatus("mandatory")
_MscLpEnetLtFbFddiMac_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbFddiMac = _MscLpEnetLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3)
)
_MscLpEnetLtFbFddiMacRowStatusTable_Object = MibTable
mscLpEnetLtFbFddiMacRowStatusTable = _MscLpEnetLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbFddiMacRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbFddiMacRowStatusEntry = _MscLpEnetLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 1, 1)
)
mscLpEnetLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbFddiMacRowStatus_Type = RowStatus
_MscLpEnetLtFbFddiMacRowStatus_Object = MibTableColumn
mscLpEnetLtFbFddiMacRowStatus = _MscLpEnetLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 1, 1, 1),
    _MscLpEnetLtFbFddiMacRowStatus_Type()
)
mscLpEnetLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacRowStatus.setStatus("mandatory")
_MscLpEnetLtFbFddiMacComponentName_Type = DisplayString
_MscLpEnetLtFbFddiMacComponentName_Object = MibTableColumn
mscLpEnetLtFbFddiMacComponentName = _MscLpEnetLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 1, 1, 2),
    _MscLpEnetLtFbFddiMacComponentName_Type()
)
mscLpEnetLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacComponentName.setStatus("mandatory")
_MscLpEnetLtFbFddiMacStorageType_Type = StorageType
_MscLpEnetLtFbFddiMacStorageType_Object = MibTableColumn
mscLpEnetLtFbFddiMacStorageType = _MscLpEnetLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 1, 1, 4),
    _MscLpEnetLtFbFddiMacStorageType_Type()
)
mscLpEnetLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacStorageType.setStatus("mandatory")
_MscLpEnetLtFbFddiMacIndex_Type = NonReplicated
_MscLpEnetLtFbFddiMacIndex_Object = MibTableColumn
mscLpEnetLtFbFddiMacIndex = _MscLpEnetLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 1, 1, 10),
    _MscLpEnetLtFbFddiMacIndex_Type()
)
mscLpEnetLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacIndex.setStatus("mandatory")
_MscLpEnetLtFbFddiMacTopTable_Object = MibTable
mscLpEnetLtFbFddiMacTopTable = _MscLpEnetLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacTopTable.setStatus("mandatory")
_MscLpEnetLtFbFddiMacTopEntry_Object = MibTableRow
mscLpEnetLtFbFddiMacTopEntry = _MscLpEnetLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 10, 1)
)
mscLpEnetLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbFddiMacTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbFddiMacTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbFddiMacTData_Object = MibTableColumn
mscLpEnetLtFbFddiMacTData = _MscLpEnetLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 3, 10, 1, 1),
    _MscLpEnetLtFbFddiMacTData_Type()
)
mscLpEnetLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbFddiMacTData.setStatus("mandatory")
_MscLpEnetLtFbMacEnet_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbMacEnet = _MscLpEnetLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4)
)
_MscLpEnetLtFbMacEnetRowStatusTable_Object = MibTable
mscLpEnetLtFbMacEnetRowStatusTable = _MscLpEnetLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbMacEnetRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbMacEnetRowStatusEntry = _MscLpEnetLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 1, 1)
)
mscLpEnetLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbMacEnetRowStatus_Type = RowStatus
_MscLpEnetLtFbMacEnetRowStatus_Object = MibTableColumn
mscLpEnetLtFbMacEnetRowStatus = _MscLpEnetLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 1, 1, 1),
    _MscLpEnetLtFbMacEnetRowStatus_Type()
)
mscLpEnetLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetRowStatus.setStatus("mandatory")
_MscLpEnetLtFbMacEnetComponentName_Type = DisplayString
_MscLpEnetLtFbMacEnetComponentName_Object = MibTableColumn
mscLpEnetLtFbMacEnetComponentName = _MscLpEnetLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 1, 1, 2),
    _MscLpEnetLtFbMacEnetComponentName_Type()
)
mscLpEnetLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetComponentName.setStatus("mandatory")
_MscLpEnetLtFbMacEnetStorageType_Type = StorageType
_MscLpEnetLtFbMacEnetStorageType_Object = MibTableColumn
mscLpEnetLtFbMacEnetStorageType = _MscLpEnetLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 1, 1, 4),
    _MscLpEnetLtFbMacEnetStorageType_Type()
)
mscLpEnetLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetStorageType.setStatus("mandatory")
_MscLpEnetLtFbMacEnetIndex_Type = NonReplicated
_MscLpEnetLtFbMacEnetIndex_Object = MibTableColumn
mscLpEnetLtFbMacEnetIndex = _MscLpEnetLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 1, 1, 10),
    _MscLpEnetLtFbMacEnetIndex_Type()
)
mscLpEnetLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetIndex.setStatus("mandatory")
_MscLpEnetLtFbMacEnetTopTable_Object = MibTable
mscLpEnetLtFbMacEnetTopTable = _MscLpEnetLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetTopTable.setStatus("mandatory")
_MscLpEnetLtFbMacEnetTopEntry_Object = MibTableRow
mscLpEnetLtFbMacEnetTopEntry = _MscLpEnetLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 10, 1)
)
mscLpEnetLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbMacEnetTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbMacEnetTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbMacEnetTData_Object = MibTableColumn
mscLpEnetLtFbMacEnetTData = _MscLpEnetLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 4, 10, 1, 1),
    _MscLpEnetLtFbMacEnetTData_Type()
)
mscLpEnetLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacEnetTData.setStatus("mandatory")
_MscLpEnetLtFbMacTr_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbMacTr = _MscLpEnetLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5)
)
_MscLpEnetLtFbMacTrRowStatusTable_Object = MibTable
mscLpEnetLtFbMacTrRowStatusTable = _MscLpEnetLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbMacTrRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbMacTrRowStatusEntry = _MscLpEnetLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 1, 1)
)
mscLpEnetLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbMacTrRowStatus_Type = RowStatus
_MscLpEnetLtFbMacTrRowStatus_Object = MibTableColumn
mscLpEnetLtFbMacTrRowStatus = _MscLpEnetLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 1, 1, 1),
    _MscLpEnetLtFbMacTrRowStatus_Type()
)
mscLpEnetLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrRowStatus.setStatus("mandatory")
_MscLpEnetLtFbMacTrComponentName_Type = DisplayString
_MscLpEnetLtFbMacTrComponentName_Object = MibTableColumn
mscLpEnetLtFbMacTrComponentName = _MscLpEnetLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 1, 1, 2),
    _MscLpEnetLtFbMacTrComponentName_Type()
)
mscLpEnetLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrComponentName.setStatus("mandatory")
_MscLpEnetLtFbMacTrStorageType_Type = StorageType
_MscLpEnetLtFbMacTrStorageType_Object = MibTableColumn
mscLpEnetLtFbMacTrStorageType = _MscLpEnetLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 1, 1, 4),
    _MscLpEnetLtFbMacTrStorageType_Type()
)
mscLpEnetLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrStorageType.setStatus("mandatory")
_MscLpEnetLtFbMacTrIndex_Type = NonReplicated
_MscLpEnetLtFbMacTrIndex_Object = MibTableColumn
mscLpEnetLtFbMacTrIndex = _MscLpEnetLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 1, 1, 10),
    _MscLpEnetLtFbMacTrIndex_Type()
)
mscLpEnetLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrIndex.setStatus("mandatory")
_MscLpEnetLtFbMacTrTopTable_Object = MibTable
mscLpEnetLtFbMacTrTopTable = _MscLpEnetLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrTopTable.setStatus("mandatory")
_MscLpEnetLtFbMacTrTopEntry_Object = MibTableRow
mscLpEnetLtFbMacTrTopEntry = _MscLpEnetLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 10, 1)
)
mscLpEnetLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbMacTrTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbMacTrTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbMacTrTData_Object = MibTableColumn
mscLpEnetLtFbMacTrTData = _MscLpEnetLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 5, 10, 1, 1),
    _MscLpEnetLtFbMacTrTData_Type()
)
mscLpEnetLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbMacTrTData.setStatus("mandatory")
_MscLpEnetLtFbData_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbData = _MscLpEnetLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6)
)
_MscLpEnetLtFbDataRowStatusTable_Object = MibTable
mscLpEnetLtFbDataRowStatusTable = _MscLpEnetLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbDataRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbDataRowStatusEntry = _MscLpEnetLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 1, 1)
)
mscLpEnetLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbDataRowStatus_Type = RowStatus
_MscLpEnetLtFbDataRowStatus_Object = MibTableColumn
mscLpEnetLtFbDataRowStatus = _MscLpEnetLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 1, 1, 1),
    _MscLpEnetLtFbDataRowStatus_Type()
)
mscLpEnetLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataRowStatus.setStatus("mandatory")
_MscLpEnetLtFbDataComponentName_Type = DisplayString
_MscLpEnetLtFbDataComponentName_Object = MibTableColumn
mscLpEnetLtFbDataComponentName = _MscLpEnetLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 1, 1, 2),
    _MscLpEnetLtFbDataComponentName_Type()
)
mscLpEnetLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataComponentName.setStatus("mandatory")
_MscLpEnetLtFbDataStorageType_Type = StorageType
_MscLpEnetLtFbDataStorageType_Object = MibTableColumn
mscLpEnetLtFbDataStorageType = _MscLpEnetLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 1, 1, 4),
    _MscLpEnetLtFbDataStorageType_Type()
)
mscLpEnetLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataStorageType.setStatus("mandatory")
_MscLpEnetLtFbDataIndex_Type = NonReplicated
_MscLpEnetLtFbDataIndex_Object = MibTableColumn
mscLpEnetLtFbDataIndex = _MscLpEnetLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 1, 1, 10),
    _MscLpEnetLtFbDataIndex_Type()
)
mscLpEnetLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataIndex.setStatus("mandatory")
_MscLpEnetLtFbDataTopTable_Object = MibTable
mscLpEnetLtFbDataTopTable = _MscLpEnetLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataTopTable.setStatus("mandatory")
_MscLpEnetLtFbDataTopEntry_Object = MibTableRow
mscLpEnetLtFbDataTopEntry = _MscLpEnetLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 10, 1)
)
mscLpEnetLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbDataTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbDataTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbDataTData_Object = MibTableColumn
mscLpEnetLtFbDataTData = _MscLpEnetLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 6, 10, 1, 1),
    _MscLpEnetLtFbDataTData_Type()
)
mscLpEnetLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbDataTData.setStatus("mandatory")
_MscLpEnetLtFbIpH_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbIpH = _MscLpEnetLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7)
)
_MscLpEnetLtFbIpHRowStatusTable_Object = MibTable
mscLpEnetLtFbIpHRowStatusTable = _MscLpEnetLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbIpHRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbIpHRowStatusEntry = _MscLpEnetLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 1, 1)
)
mscLpEnetLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbIpHRowStatus_Type = RowStatus
_MscLpEnetLtFbIpHRowStatus_Object = MibTableColumn
mscLpEnetLtFbIpHRowStatus = _MscLpEnetLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 1, 1, 1),
    _MscLpEnetLtFbIpHRowStatus_Type()
)
mscLpEnetLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHRowStatus.setStatus("mandatory")
_MscLpEnetLtFbIpHComponentName_Type = DisplayString
_MscLpEnetLtFbIpHComponentName_Object = MibTableColumn
mscLpEnetLtFbIpHComponentName = _MscLpEnetLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 1, 1, 2),
    _MscLpEnetLtFbIpHComponentName_Type()
)
mscLpEnetLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHComponentName.setStatus("mandatory")
_MscLpEnetLtFbIpHStorageType_Type = StorageType
_MscLpEnetLtFbIpHStorageType_Object = MibTableColumn
mscLpEnetLtFbIpHStorageType = _MscLpEnetLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 1, 1, 4),
    _MscLpEnetLtFbIpHStorageType_Type()
)
mscLpEnetLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHStorageType.setStatus("mandatory")
_MscLpEnetLtFbIpHIndex_Type = NonReplicated
_MscLpEnetLtFbIpHIndex_Object = MibTableColumn
mscLpEnetLtFbIpHIndex = _MscLpEnetLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 1, 1, 10),
    _MscLpEnetLtFbIpHIndex_Type()
)
mscLpEnetLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHIndex.setStatus("mandatory")
_MscLpEnetLtFbIpHTopTable_Object = MibTable
mscLpEnetLtFbIpHTopTable = _MscLpEnetLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHTopTable.setStatus("mandatory")
_MscLpEnetLtFbIpHTopEntry_Object = MibTableRow
mscLpEnetLtFbIpHTopEntry = _MscLpEnetLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 10, 1)
)
mscLpEnetLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbIpHTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbIpHTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbIpHTData_Object = MibTableColumn
mscLpEnetLtFbIpHTData = _MscLpEnetLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 7, 10, 1, 1),
    _MscLpEnetLtFbIpHTData_Type()
)
mscLpEnetLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpHTData.setStatus("mandatory")
_MscLpEnetLtFbLlch_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbLlch = _MscLpEnetLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8)
)
_MscLpEnetLtFbLlchRowStatusTable_Object = MibTable
mscLpEnetLtFbLlchRowStatusTable = _MscLpEnetLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbLlchRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbLlchRowStatusEntry = _MscLpEnetLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 1, 1)
)
mscLpEnetLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbLlchRowStatus_Type = RowStatus
_MscLpEnetLtFbLlchRowStatus_Object = MibTableColumn
mscLpEnetLtFbLlchRowStatus = _MscLpEnetLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 1, 1, 1),
    _MscLpEnetLtFbLlchRowStatus_Type()
)
mscLpEnetLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchRowStatus.setStatus("mandatory")
_MscLpEnetLtFbLlchComponentName_Type = DisplayString
_MscLpEnetLtFbLlchComponentName_Object = MibTableColumn
mscLpEnetLtFbLlchComponentName = _MscLpEnetLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 1, 1, 2),
    _MscLpEnetLtFbLlchComponentName_Type()
)
mscLpEnetLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchComponentName.setStatus("mandatory")
_MscLpEnetLtFbLlchStorageType_Type = StorageType
_MscLpEnetLtFbLlchStorageType_Object = MibTableColumn
mscLpEnetLtFbLlchStorageType = _MscLpEnetLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 1, 1, 4),
    _MscLpEnetLtFbLlchStorageType_Type()
)
mscLpEnetLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchStorageType.setStatus("mandatory")
_MscLpEnetLtFbLlchIndex_Type = NonReplicated
_MscLpEnetLtFbLlchIndex_Object = MibTableColumn
mscLpEnetLtFbLlchIndex = _MscLpEnetLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 1, 1, 10),
    _MscLpEnetLtFbLlchIndex_Type()
)
mscLpEnetLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchIndex.setStatus("mandatory")
_MscLpEnetLtFbLlchTopTable_Object = MibTable
mscLpEnetLtFbLlchTopTable = _MscLpEnetLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchTopTable.setStatus("mandatory")
_MscLpEnetLtFbLlchTopEntry_Object = MibTableRow
mscLpEnetLtFbLlchTopEntry = _MscLpEnetLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 10, 1)
)
mscLpEnetLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbLlchTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbLlchTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbLlchTData_Object = MibTableColumn
mscLpEnetLtFbLlchTData = _MscLpEnetLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 8, 10, 1, 1),
    _MscLpEnetLtFbLlchTData_Type()
)
mscLpEnetLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbLlchTData.setStatus("mandatory")
_MscLpEnetLtFbAppleH_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbAppleH = _MscLpEnetLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9)
)
_MscLpEnetLtFbAppleHRowStatusTable_Object = MibTable
mscLpEnetLtFbAppleHRowStatusTable = _MscLpEnetLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbAppleHRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbAppleHRowStatusEntry = _MscLpEnetLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 1, 1)
)
mscLpEnetLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbAppleHRowStatus_Type = RowStatus
_MscLpEnetLtFbAppleHRowStatus_Object = MibTableColumn
mscLpEnetLtFbAppleHRowStatus = _MscLpEnetLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 1, 1, 1),
    _MscLpEnetLtFbAppleHRowStatus_Type()
)
mscLpEnetLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHRowStatus.setStatus("mandatory")
_MscLpEnetLtFbAppleHComponentName_Type = DisplayString
_MscLpEnetLtFbAppleHComponentName_Object = MibTableColumn
mscLpEnetLtFbAppleHComponentName = _MscLpEnetLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 1, 1, 2),
    _MscLpEnetLtFbAppleHComponentName_Type()
)
mscLpEnetLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHComponentName.setStatus("mandatory")
_MscLpEnetLtFbAppleHStorageType_Type = StorageType
_MscLpEnetLtFbAppleHStorageType_Object = MibTableColumn
mscLpEnetLtFbAppleHStorageType = _MscLpEnetLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 1, 1, 4),
    _MscLpEnetLtFbAppleHStorageType_Type()
)
mscLpEnetLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHStorageType.setStatus("mandatory")
_MscLpEnetLtFbAppleHIndex_Type = NonReplicated
_MscLpEnetLtFbAppleHIndex_Object = MibTableColumn
mscLpEnetLtFbAppleHIndex = _MscLpEnetLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 1, 1, 10),
    _MscLpEnetLtFbAppleHIndex_Type()
)
mscLpEnetLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHIndex.setStatus("mandatory")
_MscLpEnetLtFbAppleHTopTable_Object = MibTable
mscLpEnetLtFbAppleHTopTable = _MscLpEnetLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHTopTable.setStatus("mandatory")
_MscLpEnetLtFbAppleHTopEntry_Object = MibTableRow
mscLpEnetLtFbAppleHTopEntry = _MscLpEnetLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 10, 1)
)
mscLpEnetLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbAppleHTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbAppleHTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbAppleHTData_Object = MibTableColumn
mscLpEnetLtFbAppleHTData = _MscLpEnetLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 9, 10, 1, 1),
    _MscLpEnetLtFbAppleHTData_Type()
)
mscLpEnetLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbAppleHTData.setStatus("mandatory")
_MscLpEnetLtFbIpxH_ObjectIdentity = ObjectIdentity
mscLpEnetLtFbIpxH = _MscLpEnetLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10)
)
_MscLpEnetLtFbIpxHRowStatusTable_Object = MibTable
mscLpEnetLtFbIpxHRowStatusTable = _MscLpEnetLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHRowStatusTable.setStatus("mandatory")
_MscLpEnetLtFbIpxHRowStatusEntry_Object = MibTableRow
mscLpEnetLtFbIpxHRowStatusEntry = _MscLpEnetLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 1, 1)
)
mscLpEnetLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtFbIpxHRowStatus_Type = RowStatus
_MscLpEnetLtFbIpxHRowStatus_Object = MibTableColumn
mscLpEnetLtFbIpxHRowStatus = _MscLpEnetLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 1, 1, 1),
    _MscLpEnetLtFbIpxHRowStatus_Type()
)
mscLpEnetLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHRowStatus.setStatus("mandatory")
_MscLpEnetLtFbIpxHComponentName_Type = DisplayString
_MscLpEnetLtFbIpxHComponentName_Object = MibTableColumn
mscLpEnetLtFbIpxHComponentName = _MscLpEnetLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 1, 1, 2),
    _MscLpEnetLtFbIpxHComponentName_Type()
)
mscLpEnetLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHComponentName.setStatus("mandatory")
_MscLpEnetLtFbIpxHStorageType_Type = StorageType
_MscLpEnetLtFbIpxHStorageType_Object = MibTableColumn
mscLpEnetLtFbIpxHStorageType = _MscLpEnetLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 1, 1, 4),
    _MscLpEnetLtFbIpxHStorageType_Type()
)
mscLpEnetLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHStorageType.setStatus("mandatory")
_MscLpEnetLtFbIpxHIndex_Type = NonReplicated
_MscLpEnetLtFbIpxHIndex_Object = MibTableColumn
mscLpEnetLtFbIpxHIndex = _MscLpEnetLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 1, 1, 10),
    _MscLpEnetLtFbIpxHIndex_Type()
)
mscLpEnetLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHIndex.setStatus("mandatory")
_MscLpEnetLtFbIpxHTopTable_Object = MibTable
mscLpEnetLtFbIpxHTopTable = _MscLpEnetLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHTopTable.setStatus("mandatory")
_MscLpEnetLtFbIpxHTopEntry_Object = MibTableRow
mscLpEnetLtFbIpxHTopEntry = _MscLpEnetLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 10, 1)
)
mscLpEnetLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbIpxHTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbIpxHTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbIpxHTData_Object = MibTableColumn
mscLpEnetLtFbIpxHTData = _MscLpEnetLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 10, 10, 1, 1),
    _MscLpEnetLtFbIpxHTData_Type()
)
mscLpEnetLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbIpxHTData.setStatus("mandatory")
_MscLpEnetLtFbTopTable_Object = MibTable
mscLpEnetLtFbTopTable = _MscLpEnetLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 20)
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbTopTable.setStatus("mandatory")
_MscLpEnetLtFbTopEntry_Object = MibTableRow
mscLpEnetLtFbTopEntry = _MscLpEnetLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 20, 1)
)
mscLpEnetLtFbTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtFbTopEntry.setStatus("mandatory")


class _MscLpEnetLtFbTData_Type(AsciiString):
    """Custom type mscLpEnetLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtFbTData_Type.__name__ = "AsciiString"
_MscLpEnetLtFbTData_Object = MibTableColumn
mscLpEnetLtFbTData = _MscLpEnetLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 5, 20, 1, 1),
    _MscLpEnetLtFbTData_Type()
)
mscLpEnetLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtFbTData.setStatus("mandatory")
_MscLpEnetLtCntl_ObjectIdentity = ObjectIdentity
mscLpEnetLtCntl = _MscLpEnetLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6)
)
_MscLpEnetLtCntlRowStatusTable_Object = MibTable
mscLpEnetLtCntlRowStatusTable = _MscLpEnetLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetLtCntlRowStatusTable.setStatus("mandatory")
_MscLpEnetLtCntlRowStatusEntry_Object = MibTableRow
mscLpEnetLtCntlRowStatusEntry = _MscLpEnetLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 1, 1)
)
mscLpEnetLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtCntlRowStatusEntry.setStatus("mandatory")
_MscLpEnetLtCntlRowStatus_Type = RowStatus
_MscLpEnetLtCntlRowStatus_Object = MibTableColumn
mscLpEnetLtCntlRowStatus = _MscLpEnetLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 1, 1, 1),
    _MscLpEnetLtCntlRowStatus_Type()
)
mscLpEnetLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtCntlRowStatus.setStatus("mandatory")
_MscLpEnetLtCntlComponentName_Type = DisplayString
_MscLpEnetLtCntlComponentName_Object = MibTableColumn
mscLpEnetLtCntlComponentName = _MscLpEnetLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 1, 1, 2),
    _MscLpEnetLtCntlComponentName_Type()
)
mscLpEnetLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtCntlComponentName.setStatus("mandatory")
_MscLpEnetLtCntlStorageType_Type = StorageType
_MscLpEnetLtCntlStorageType_Object = MibTableColumn
mscLpEnetLtCntlStorageType = _MscLpEnetLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 1, 1, 4),
    _MscLpEnetLtCntlStorageType_Type()
)
mscLpEnetLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLtCntlStorageType.setStatus("mandatory")
_MscLpEnetLtCntlIndex_Type = NonReplicated
_MscLpEnetLtCntlIndex_Object = MibTableColumn
mscLpEnetLtCntlIndex = _MscLpEnetLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 1, 1, 10),
    _MscLpEnetLtCntlIndex_Type()
)
mscLpEnetLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetLtCntlIndex.setStatus("mandatory")
_MscLpEnetLtCntlTopTable_Object = MibTable
mscLpEnetLtCntlTopTable = _MscLpEnetLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetLtCntlTopTable.setStatus("mandatory")
_MscLpEnetLtCntlTopEntry_Object = MibTableRow
mscLpEnetLtCntlTopEntry = _MscLpEnetLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 10, 1)
)
mscLpEnetLtCntlTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtCntlTopEntry.setStatus("mandatory")


class _MscLpEnetLtCntlTData_Type(AsciiString):
    """Custom type mscLpEnetLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtCntlTData_Type.__name__ = "AsciiString"
_MscLpEnetLtCntlTData_Object = MibTableColumn
mscLpEnetLtCntlTData = _MscLpEnetLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 6, 10, 1, 1),
    _MscLpEnetLtCntlTData_Type()
)
mscLpEnetLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtCntlTData.setStatus("mandatory")
_MscLpEnetLtTopTable_Object = MibTable
mscLpEnetLtTopTable = _MscLpEnetLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 20)
)
if mibBuilder.loadTexts:
    mscLpEnetLtTopTable.setStatus("mandatory")
_MscLpEnetLtTopEntry_Object = MibTableRow
mscLpEnetLtTopEntry = _MscLpEnetLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 20, 1)
)
mscLpEnetLtTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetLtTopEntry.setStatus("mandatory")


class _MscLpEnetLtTData_Type(AsciiString):
    """Custom type mscLpEnetLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEnetLtTData_Type.__name__ = "AsciiString"
_MscLpEnetLtTData_Object = MibTableColumn
mscLpEnetLtTData = _MscLpEnetLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 2, 20, 1, 1),
    _MscLpEnetLtTData_Type()
)
mscLpEnetLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetLtTData.setStatus("mandatory")
_MscLpEnetTest_ObjectIdentity = ObjectIdentity
mscLpEnetTest = _MscLpEnetTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5)
)
_MscLpEnetTestRowStatusTable_Object = MibTable
mscLpEnetTestRowStatusTable = _MscLpEnetTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpEnetTestRowStatusTable.setStatus("mandatory")
_MscLpEnetTestRowStatusEntry_Object = MibTableRow
mscLpEnetTestRowStatusEntry = _MscLpEnetTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 1, 1)
)
mscLpEnetTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetTestRowStatusEntry.setStatus("mandatory")
_MscLpEnetTestRowStatus_Type = RowStatus
_MscLpEnetTestRowStatus_Object = MibTableColumn
mscLpEnetTestRowStatus = _MscLpEnetTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 1, 1, 1),
    _MscLpEnetTestRowStatus_Type()
)
mscLpEnetTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestRowStatus.setStatus("mandatory")
_MscLpEnetTestComponentName_Type = DisplayString
_MscLpEnetTestComponentName_Object = MibTableColumn
mscLpEnetTestComponentName = _MscLpEnetTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 1, 1, 2),
    _MscLpEnetTestComponentName_Type()
)
mscLpEnetTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestComponentName.setStatus("mandatory")
_MscLpEnetTestStorageType_Type = StorageType
_MscLpEnetTestStorageType_Object = MibTableColumn
mscLpEnetTestStorageType = _MscLpEnetTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 1, 1, 4),
    _MscLpEnetTestStorageType_Type()
)
mscLpEnetTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestStorageType.setStatus("mandatory")
_MscLpEnetTestIndex_Type = NonReplicated
_MscLpEnetTestIndex_Object = MibTableColumn
mscLpEnetTestIndex = _MscLpEnetTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 1, 1, 10),
    _MscLpEnetTestIndex_Type()
)
mscLpEnetTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEnetTestIndex.setStatus("mandatory")
_MscLpEnetTestPTOTable_Object = MibTable
mscLpEnetTestPTOTable = _MscLpEnetTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetTestPTOTable.setStatus("mandatory")
_MscLpEnetTestPTOEntry_Object = MibTableRow
mscLpEnetTestPTOEntry = _MscLpEnetTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 10, 1)
)
mscLpEnetTestPTOEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetTestPTOEntry.setStatus("mandatory")


class _MscLpEnetTestType_Type(Integer32):
    """Custom type mscLpEnetTestType based on Integer32"""
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


_MscLpEnetTestType_Type.__name__ = "Integer32"
_MscLpEnetTestType_Object = MibTableColumn
mscLpEnetTestType = _MscLpEnetTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 10, 1, 1),
    _MscLpEnetTestType_Type()
)
mscLpEnetTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetTestType.setStatus("mandatory")


class _MscLpEnetTestFrmSize_Type(Unsigned32):
    """Custom type mscLpEnetTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscLpEnetTestFrmSize_Type.__name__ = "Unsigned32"
_MscLpEnetTestFrmSize_Object = MibTableColumn
mscLpEnetTestFrmSize = _MscLpEnetTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 10, 1, 2),
    _MscLpEnetTestFrmSize_Type()
)
mscLpEnetTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetTestFrmSize.setStatus("mandatory")


class _MscLpEnetTestDuration_Type(Unsigned32):
    """Custom type mscLpEnetTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscLpEnetTestDuration_Type.__name__ = "Unsigned32"
_MscLpEnetTestDuration_Object = MibTableColumn
mscLpEnetTestDuration = _MscLpEnetTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 10, 1, 3),
    _MscLpEnetTestDuration_Type()
)
mscLpEnetTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetTestDuration.setStatus("mandatory")
_MscLpEnetTestResultsTable_Object = MibTable
mscLpEnetTestResultsTable = _MscLpEnetTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11)
)
if mibBuilder.loadTexts:
    mscLpEnetTestResultsTable.setStatus("mandatory")
_MscLpEnetTestResultsEntry_Object = MibTableRow
mscLpEnetTestResultsEntry = _MscLpEnetTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1)
)
mscLpEnetTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetTestResultsEntry.setStatus("mandatory")
_MscLpEnetTestElapsedTime_Type = Counter32
_MscLpEnetTestElapsedTime_Object = MibTableColumn
mscLpEnetTestElapsedTime = _MscLpEnetTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 4),
    _MscLpEnetTestElapsedTime_Type()
)
mscLpEnetTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestElapsedTime.setStatus("mandatory")


class _MscLpEnetTestTimeRemaining_Type(Unsigned32):
    """Custom type mscLpEnetTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpEnetTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscLpEnetTestTimeRemaining_Object = MibTableColumn
mscLpEnetTestTimeRemaining = _MscLpEnetTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 5),
    _MscLpEnetTestTimeRemaining_Type()
)
mscLpEnetTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestTimeRemaining.setStatus("mandatory")


class _MscLpEnetTestCauseOfTermination_Type(Integer32):
    """Custom type mscLpEnetTestCauseOfTermination based on Integer32"""
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


_MscLpEnetTestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpEnetTestCauseOfTermination_Object = MibTableColumn
mscLpEnetTestCauseOfTermination = _MscLpEnetTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 6),
    _MscLpEnetTestCauseOfTermination_Type()
)
mscLpEnetTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestCauseOfTermination.setStatus("mandatory")
_MscLpEnetTestFrmTx_Type = PassportCounter64
_MscLpEnetTestFrmTx_Object = MibTableColumn
mscLpEnetTestFrmTx = _MscLpEnetTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 7),
    _MscLpEnetTestFrmTx_Type()
)
mscLpEnetTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestFrmTx.setStatus("mandatory")
_MscLpEnetTestBitsTx_Type = PassportCounter64
_MscLpEnetTestBitsTx_Object = MibTableColumn
mscLpEnetTestBitsTx = _MscLpEnetTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 8),
    _MscLpEnetTestBitsTx_Type()
)
mscLpEnetTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestBitsTx.setStatus("mandatory")
_MscLpEnetTestFrmRx_Type = PassportCounter64
_MscLpEnetTestFrmRx_Object = MibTableColumn
mscLpEnetTestFrmRx = _MscLpEnetTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 9),
    _MscLpEnetTestFrmRx_Type()
)
mscLpEnetTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestFrmRx.setStatus("mandatory")
_MscLpEnetTestBitsRx_Type = PassportCounter64
_MscLpEnetTestBitsRx_Object = MibTableColumn
mscLpEnetTestBitsRx = _MscLpEnetTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 10),
    _MscLpEnetTestBitsRx_Type()
)
mscLpEnetTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestBitsRx.setStatus("mandatory")
_MscLpEnetTestErroredFrmRx_Type = PassportCounter64
_MscLpEnetTestErroredFrmRx_Object = MibTableColumn
mscLpEnetTestErroredFrmRx = _MscLpEnetTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 5, 11, 1, 11),
    _MscLpEnetTestErroredFrmRx_Type()
)
mscLpEnetTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetTestErroredFrmRx.setStatus("mandatory")
_MscLpEnetCidDataTable_Object = MibTable
mscLpEnetCidDataTable = _MscLpEnetCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEnetCidDataTable.setStatus("mandatory")
_MscLpEnetCidDataEntry_Object = MibTableRow
mscLpEnetCidDataEntry = _MscLpEnetCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 10, 1)
)
mscLpEnetCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetCidDataEntry.setStatus("mandatory")


class _MscLpEnetCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLpEnetCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLpEnetCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLpEnetCustomerIdentifier_Object = MibTableColumn
mscLpEnetCustomerIdentifier = _MscLpEnetCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 10, 1, 1),
    _MscLpEnetCustomerIdentifier_Type()
)
mscLpEnetCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetCustomerIdentifier.setStatus("mandatory")
_MscLpEnetIfEntryTable_Object = MibTable
mscLpEnetIfEntryTable = _MscLpEnetIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 11)
)
if mibBuilder.loadTexts:
    mscLpEnetIfEntryTable.setStatus("mandatory")
_MscLpEnetIfEntryEntry_Object = MibTableRow
mscLpEnetIfEntryEntry = _MscLpEnetIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 11, 1)
)
mscLpEnetIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetIfEntryEntry.setStatus("mandatory")


class _MscLpEnetIfAdminStatus_Type(Integer32):
    """Custom type mscLpEnetIfAdminStatus based on Integer32"""
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


_MscLpEnetIfAdminStatus_Type.__name__ = "Integer32"
_MscLpEnetIfAdminStatus_Object = MibTableColumn
mscLpEnetIfAdminStatus = _MscLpEnetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 11, 1, 1),
    _MscLpEnetIfAdminStatus_Type()
)
mscLpEnetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetIfAdminStatus.setStatus("mandatory")


class _MscLpEnetIfIndex_Type(InterfaceIndex):
    """Custom type mscLpEnetIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLpEnetIfIndex_Type.__name__ = "InterfaceIndex"
_MscLpEnetIfIndex_Object = MibTableColumn
mscLpEnetIfIndex = _MscLpEnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 11, 1, 2),
    _MscLpEnetIfIndex_Type()
)
mscLpEnetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetIfIndex.setStatus("mandatory")
_MscLpEnetProvTable_Object = MibTable
mscLpEnetProvTable = _MscLpEnetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 12)
)
if mibBuilder.loadTexts:
    mscLpEnetProvTable.setStatus("mandatory")
_MscLpEnetProvEntry_Object = MibTableRow
mscLpEnetProvEntry = _MscLpEnetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 12, 1)
)
mscLpEnetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetProvEntry.setStatus("mandatory")


class _MscLpEnetHeartbeatPacket_Type(Integer32):
    """Custom type mscLpEnetHeartbeatPacket based on Integer32"""
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


_MscLpEnetHeartbeatPacket_Type.__name__ = "Integer32"
_MscLpEnetHeartbeatPacket_Object = MibTableColumn
mscLpEnetHeartbeatPacket = _MscLpEnetHeartbeatPacket_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 12, 1, 1),
    _MscLpEnetHeartbeatPacket_Type()
)
mscLpEnetHeartbeatPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetHeartbeatPacket.setStatus("mandatory")
_MscLpEnetApplicationFramerName_Type = Link
_MscLpEnetApplicationFramerName_Object = MibTableColumn
mscLpEnetApplicationFramerName = _MscLpEnetApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 12, 1, 2),
    _MscLpEnetApplicationFramerName_Type()
)
mscLpEnetApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetApplicationFramerName.setStatus("mandatory")
_MscLpEnetAdminInfoTable_Object = MibTable
mscLpEnetAdminInfoTable = _MscLpEnetAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 13)
)
if mibBuilder.loadTexts:
    mscLpEnetAdminInfoTable.setStatus("mandatory")
_MscLpEnetAdminInfoEntry_Object = MibTableRow
mscLpEnetAdminInfoEntry = _MscLpEnetAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 13, 1)
)
mscLpEnetAdminInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetAdminInfoEntry.setStatus("mandatory")


class _MscLpEnetVendor_Type(AsciiString):
    """Custom type mscLpEnetVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLpEnetVendor_Type.__name__ = "AsciiString"
_MscLpEnetVendor_Object = MibTableColumn
mscLpEnetVendor = _MscLpEnetVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 13, 1, 1),
    _MscLpEnetVendor_Type()
)
mscLpEnetVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetVendor.setStatus("mandatory")


class _MscLpEnetCommentText_Type(AsciiString):
    """Custom type mscLpEnetCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_MscLpEnetCommentText_Type.__name__ = "AsciiString"
_MscLpEnetCommentText_Object = MibTableColumn
mscLpEnetCommentText = _MscLpEnetCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 13, 1, 2),
    _MscLpEnetCommentText_Type()
)
mscLpEnetCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEnetCommentText.setStatus("mandatory")
_MscLpEnetStateTable_Object = MibTable
mscLpEnetStateTable = _MscLpEnetStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 15)
)
if mibBuilder.loadTexts:
    mscLpEnetStateTable.setStatus("mandatory")
_MscLpEnetStateEntry_Object = MibTableRow
mscLpEnetStateEntry = _MscLpEnetStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 15, 1)
)
mscLpEnetStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetStateEntry.setStatus("mandatory")


class _MscLpEnetAdminState_Type(Integer32):
    """Custom type mscLpEnetAdminState based on Integer32"""
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


_MscLpEnetAdminState_Type.__name__ = "Integer32"
_MscLpEnetAdminState_Object = MibTableColumn
mscLpEnetAdminState = _MscLpEnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 15, 1, 1),
    _MscLpEnetAdminState_Type()
)
mscLpEnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetAdminState.setStatus("mandatory")


class _MscLpEnetOperationalState_Type(Integer32):
    """Custom type mscLpEnetOperationalState based on Integer32"""
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


_MscLpEnetOperationalState_Type.__name__ = "Integer32"
_MscLpEnetOperationalState_Object = MibTableColumn
mscLpEnetOperationalState = _MscLpEnetOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 15, 1, 2),
    _MscLpEnetOperationalState_Type()
)
mscLpEnetOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetOperationalState.setStatus("mandatory")


class _MscLpEnetUsageState_Type(Integer32):
    """Custom type mscLpEnetUsageState based on Integer32"""
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


_MscLpEnetUsageState_Type.__name__ = "Integer32"
_MscLpEnetUsageState_Object = MibTableColumn
mscLpEnetUsageState = _MscLpEnetUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 15, 1, 3),
    _MscLpEnetUsageState_Type()
)
mscLpEnetUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetUsageState.setStatus("mandatory")
_MscLpEnetOperStatusTable_Object = MibTable
mscLpEnetOperStatusTable = _MscLpEnetOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 16)
)
if mibBuilder.loadTexts:
    mscLpEnetOperStatusTable.setStatus("mandatory")
_MscLpEnetOperStatusEntry_Object = MibTableRow
mscLpEnetOperStatusEntry = _MscLpEnetOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 16, 1)
)
mscLpEnetOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetOperStatusEntry.setStatus("mandatory")


class _MscLpEnetSnmpOperStatus_Type(Integer32):
    """Custom type mscLpEnetSnmpOperStatus based on Integer32"""
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


_MscLpEnetSnmpOperStatus_Type.__name__ = "Integer32"
_MscLpEnetSnmpOperStatus_Object = MibTableColumn
mscLpEnetSnmpOperStatus = _MscLpEnetSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 16, 1, 1),
    _MscLpEnetSnmpOperStatus_Type()
)
mscLpEnetSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetSnmpOperStatus.setStatus("mandatory")
_MscLpEnetOperTable_Object = MibTable
mscLpEnetOperTable = _MscLpEnetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 17)
)
if mibBuilder.loadTexts:
    mscLpEnetOperTable.setStatus("mandatory")
_MscLpEnetOperEntry_Object = MibTableRow
mscLpEnetOperEntry = _MscLpEnetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 17, 1)
)
mscLpEnetOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetOperEntry.setStatus("mandatory")


class _MscLpEnetMacAddress_Type(MacAddress):
    """Custom type mscLpEnetMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpEnetMacAddress_Type.__name__ = "MacAddress"
_MscLpEnetMacAddress_Object = MibTableColumn
mscLpEnetMacAddress = _MscLpEnetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 17, 1, 1),
    _MscLpEnetMacAddress_Type()
)
mscLpEnetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetMacAddress.setStatus("mandatory")
_MscLpEnetStatsTable_Object = MibTable
mscLpEnetStatsTable = _MscLpEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18)
)
if mibBuilder.loadTexts:
    mscLpEnetStatsTable.setStatus("mandatory")
_MscLpEnetStatsEntry_Object = MibTableRow
mscLpEnetStatsEntry = _MscLpEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1)
)
mscLpEnetStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEnetStatsEntry.setStatus("mandatory")
_MscLpEnetAlignmentErrors_Type = Counter32
_MscLpEnetAlignmentErrors_Object = MibTableColumn
mscLpEnetAlignmentErrors = _MscLpEnetAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 2),
    _MscLpEnetAlignmentErrors_Type()
)
mscLpEnetAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetAlignmentErrors.setStatus("mandatory")
_MscLpEnetFcsErrors_Type = Counter32
_MscLpEnetFcsErrors_Object = MibTableColumn
mscLpEnetFcsErrors = _MscLpEnetFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 3),
    _MscLpEnetFcsErrors_Type()
)
mscLpEnetFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetFcsErrors.setStatus("mandatory")
_MscLpEnetSingleCollisionFrames_Type = Counter32
_MscLpEnetSingleCollisionFrames_Object = MibTableColumn
mscLpEnetSingleCollisionFrames = _MscLpEnetSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 4),
    _MscLpEnetSingleCollisionFrames_Type()
)
mscLpEnetSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetSingleCollisionFrames.setStatus("mandatory")
_MscLpEnetMultipleCollisionFrames_Type = Counter32
_MscLpEnetMultipleCollisionFrames_Object = MibTableColumn
mscLpEnetMultipleCollisionFrames = _MscLpEnetMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 5),
    _MscLpEnetMultipleCollisionFrames_Type()
)
mscLpEnetMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetMultipleCollisionFrames.setStatus("mandatory")
_MscLpEnetSqeTestErrors_Type = Counter32
_MscLpEnetSqeTestErrors_Object = MibTableColumn
mscLpEnetSqeTestErrors = _MscLpEnetSqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 6),
    _MscLpEnetSqeTestErrors_Type()
)
mscLpEnetSqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetSqeTestErrors.setStatus("mandatory")
_MscLpEnetDeferredTransmissions_Type = Counter32
_MscLpEnetDeferredTransmissions_Object = MibTableColumn
mscLpEnetDeferredTransmissions = _MscLpEnetDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 7),
    _MscLpEnetDeferredTransmissions_Type()
)
mscLpEnetDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetDeferredTransmissions.setStatus("mandatory")
_MscLpEnetLateCollisions_Type = Counter32
_MscLpEnetLateCollisions_Object = MibTableColumn
mscLpEnetLateCollisions = _MscLpEnetLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 8),
    _MscLpEnetLateCollisions_Type()
)
mscLpEnetLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetLateCollisions.setStatus("mandatory")
_MscLpEnetExcessiveCollisions_Type = Counter32
_MscLpEnetExcessiveCollisions_Object = MibTableColumn
mscLpEnetExcessiveCollisions = _MscLpEnetExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 9),
    _MscLpEnetExcessiveCollisions_Type()
)
mscLpEnetExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetExcessiveCollisions.setStatus("mandatory")
_MscLpEnetMacTransmitErrors_Type = Counter32
_MscLpEnetMacTransmitErrors_Object = MibTableColumn
mscLpEnetMacTransmitErrors = _MscLpEnetMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 10),
    _MscLpEnetMacTransmitErrors_Type()
)
mscLpEnetMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetMacTransmitErrors.setStatus("mandatory")
_MscLpEnetCarrierSenseErrors_Type = Counter32
_MscLpEnetCarrierSenseErrors_Object = MibTableColumn
mscLpEnetCarrierSenseErrors = _MscLpEnetCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 11),
    _MscLpEnetCarrierSenseErrors_Type()
)
mscLpEnetCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetCarrierSenseErrors.setStatus("mandatory")
_MscLpEnetFrameTooLongs_Type = Counter32
_MscLpEnetFrameTooLongs_Object = MibTableColumn
mscLpEnetFrameTooLongs = _MscLpEnetFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 12),
    _MscLpEnetFrameTooLongs_Type()
)
mscLpEnetFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetFrameTooLongs.setStatus("mandatory")
_MscLpEnetMacReceiveErrors_Type = Counter32
_MscLpEnetMacReceiveErrors_Object = MibTableColumn
mscLpEnetMacReceiveErrors = _MscLpEnetMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 3, 18, 1, 13),
    _MscLpEnetMacReceiveErrors_Type()
)
mscLpEnetMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEnetMacReceiveErrors.setStatus("mandatory")
_MscLpFi_ObjectIdentity = ObjectIdentity
mscLpFi = _MscLpFi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4)
)
_MscLpFiRowStatusTable_Object = MibTable
mscLpFiRowStatusTable = _MscLpFiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpFiRowStatusTable.setStatus("mandatory")
_MscLpFiRowStatusEntry_Object = MibTableRow
mscLpFiRowStatusEntry = _MscLpFiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 1, 1)
)
mscLpFiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiRowStatusEntry.setStatus("mandatory")
_MscLpFiRowStatus_Type = RowStatus
_MscLpFiRowStatus_Object = MibTableColumn
mscLpFiRowStatus = _MscLpFiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 1, 1, 1),
    _MscLpFiRowStatus_Type()
)
mscLpFiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiRowStatus.setStatus("mandatory")
_MscLpFiComponentName_Type = DisplayString
_MscLpFiComponentName_Object = MibTableColumn
mscLpFiComponentName = _MscLpFiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 1, 1, 2),
    _MscLpFiComponentName_Type()
)
mscLpFiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiComponentName.setStatus("mandatory")
_MscLpFiStorageType_Type = StorageType
_MscLpFiStorageType_Object = MibTableColumn
mscLpFiStorageType = _MscLpFiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 1, 1, 4),
    _MscLpFiStorageType_Type()
)
mscLpFiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiStorageType.setStatus("mandatory")


class _MscLpFiIndex_Type(Integer32):
    """Custom type mscLpFiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscLpFiIndex_Type.__name__ = "Integer32"
_MscLpFiIndex_Object = MibTableColumn
mscLpFiIndex = _MscLpFiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 1, 1, 10),
    _MscLpFiIndex_Type()
)
mscLpFiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiIndex.setStatus("mandatory")
_MscLpFiLt_ObjectIdentity = ObjectIdentity
mscLpFiLt = _MscLpFiLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2)
)
_MscLpFiLtRowStatusTable_Object = MibTable
mscLpFiLtRowStatusTable = _MscLpFiLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtRowStatusTable.setStatus("mandatory")
_MscLpFiLtRowStatusEntry_Object = MibTableRow
mscLpFiLtRowStatusEntry = _MscLpFiLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 1, 1)
)
mscLpFiLtRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtRowStatusEntry.setStatus("mandatory")
_MscLpFiLtRowStatus_Type = RowStatus
_MscLpFiLtRowStatus_Object = MibTableColumn
mscLpFiLtRowStatus = _MscLpFiLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 1, 1, 1),
    _MscLpFiLtRowStatus_Type()
)
mscLpFiLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtRowStatus.setStatus("mandatory")
_MscLpFiLtComponentName_Type = DisplayString
_MscLpFiLtComponentName_Object = MibTableColumn
mscLpFiLtComponentName = _MscLpFiLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 1, 1, 2),
    _MscLpFiLtComponentName_Type()
)
mscLpFiLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtComponentName.setStatus("mandatory")
_MscLpFiLtStorageType_Type = StorageType
_MscLpFiLtStorageType_Object = MibTableColumn
mscLpFiLtStorageType = _MscLpFiLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 1, 1, 4),
    _MscLpFiLtStorageType_Type()
)
mscLpFiLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtStorageType.setStatus("mandatory")
_MscLpFiLtIndex_Type = NonReplicated
_MscLpFiLtIndex_Object = MibTableColumn
mscLpFiLtIndex = _MscLpFiLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 1, 1, 10),
    _MscLpFiLtIndex_Type()
)
mscLpFiLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtIndex.setStatus("mandatory")
_MscLpFiLtFrmCmp_ObjectIdentity = ObjectIdentity
mscLpFiLtFrmCmp = _MscLpFiLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2)
)
_MscLpFiLtFrmCmpRowStatusTable_Object = MibTable
mscLpFiLtFrmCmpRowStatusTable = _MscLpFiLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpRowStatusTable.setStatus("mandatory")
_MscLpFiLtFrmCmpRowStatusEntry_Object = MibTableRow
mscLpFiLtFrmCmpRowStatusEntry = _MscLpFiLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 1, 1)
)
mscLpFiLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFrmCmpRowStatus_Type = RowStatus
_MscLpFiLtFrmCmpRowStatus_Object = MibTableColumn
mscLpFiLtFrmCmpRowStatus = _MscLpFiLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 1, 1, 1),
    _MscLpFiLtFrmCmpRowStatus_Type()
)
mscLpFiLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpRowStatus.setStatus("mandatory")
_MscLpFiLtFrmCmpComponentName_Type = DisplayString
_MscLpFiLtFrmCmpComponentName_Object = MibTableColumn
mscLpFiLtFrmCmpComponentName = _MscLpFiLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 1, 1, 2),
    _MscLpFiLtFrmCmpComponentName_Type()
)
mscLpFiLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpComponentName.setStatus("mandatory")
_MscLpFiLtFrmCmpStorageType_Type = StorageType
_MscLpFiLtFrmCmpStorageType_Object = MibTableColumn
mscLpFiLtFrmCmpStorageType = _MscLpFiLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 1, 1, 4),
    _MscLpFiLtFrmCmpStorageType_Type()
)
mscLpFiLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpStorageType.setStatus("mandatory")
_MscLpFiLtFrmCmpIndex_Type = NonReplicated
_MscLpFiLtFrmCmpIndex_Object = MibTableColumn
mscLpFiLtFrmCmpIndex = _MscLpFiLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 1, 1, 10),
    _MscLpFiLtFrmCmpIndex_Type()
)
mscLpFiLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpIndex.setStatus("mandatory")
_MscLpFiLtFrmCmpTopTable_Object = MibTable
mscLpFiLtFrmCmpTopTable = _MscLpFiLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpTopTable.setStatus("mandatory")
_MscLpFiLtFrmCmpTopEntry_Object = MibTableRow
mscLpFiLtFrmCmpTopEntry = _MscLpFiLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 10, 1)
)
mscLpFiLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpTopEntry.setStatus("mandatory")


class _MscLpFiLtFrmCmpTData_Type(AsciiString):
    """Custom type mscLpFiLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFrmCmpTData_Type.__name__ = "AsciiString"
_MscLpFiLtFrmCmpTData_Object = MibTableColumn
mscLpFiLtFrmCmpTData = _MscLpFiLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 2, 10, 1, 1),
    _MscLpFiLtFrmCmpTData_Type()
)
mscLpFiLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCmpTData.setStatus("mandatory")
_MscLpFiLtFrmCpy_ObjectIdentity = ObjectIdentity
mscLpFiLtFrmCpy = _MscLpFiLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3)
)
_MscLpFiLtFrmCpyRowStatusTable_Object = MibTable
mscLpFiLtFrmCpyRowStatusTable = _MscLpFiLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyRowStatusTable.setStatus("mandatory")
_MscLpFiLtFrmCpyRowStatusEntry_Object = MibTableRow
mscLpFiLtFrmCpyRowStatusEntry = _MscLpFiLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 1, 1)
)
mscLpFiLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFrmCpyRowStatus_Type = RowStatus
_MscLpFiLtFrmCpyRowStatus_Object = MibTableColumn
mscLpFiLtFrmCpyRowStatus = _MscLpFiLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 1, 1, 1),
    _MscLpFiLtFrmCpyRowStatus_Type()
)
mscLpFiLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyRowStatus.setStatus("mandatory")
_MscLpFiLtFrmCpyComponentName_Type = DisplayString
_MscLpFiLtFrmCpyComponentName_Object = MibTableColumn
mscLpFiLtFrmCpyComponentName = _MscLpFiLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 1, 1, 2),
    _MscLpFiLtFrmCpyComponentName_Type()
)
mscLpFiLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyComponentName.setStatus("mandatory")
_MscLpFiLtFrmCpyStorageType_Type = StorageType
_MscLpFiLtFrmCpyStorageType_Object = MibTableColumn
mscLpFiLtFrmCpyStorageType = _MscLpFiLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 1, 1, 4),
    _MscLpFiLtFrmCpyStorageType_Type()
)
mscLpFiLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyStorageType.setStatus("mandatory")
_MscLpFiLtFrmCpyIndex_Type = NonReplicated
_MscLpFiLtFrmCpyIndex_Object = MibTableColumn
mscLpFiLtFrmCpyIndex = _MscLpFiLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 1, 1, 10),
    _MscLpFiLtFrmCpyIndex_Type()
)
mscLpFiLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyIndex.setStatus("mandatory")
_MscLpFiLtFrmCpyTopTable_Object = MibTable
mscLpFiLtFrmCpyTopTable = _MscLpFiLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyTopTable.setStatus("mandatory")
_MscLpFiLtFrmCpyTopEntry_Object = MibTableRow
mscLpFiLtFrmCpyTopEntry = _MscLpFiLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 10, 1)
)
mscLpFiLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyTopEntry.setStatus("mandatory")


class _MscLpFiLtFrmCpyTData_Type(AsciiString):
    """Custom type mscLpFiLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFrmCpyTData_Type.__name__ = "AsciiString"
_MscLpFiLtFrmCpyTData_Object = MibTableColumn
mscLpFiLtFrmCpyTData = _MscLpFiLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 3, 10, 1, 1),
    _MscLpFiLtFrmCpyTData_Type()
)
mscLpFiLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFrmCpyTData.setStatus("mandatory")
_MscLpFiLtPrtCfg_ObjectIdentity = ObjectIdentity
mscLpFiLtPrtCfg = _MscLpFiLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4)
)
_MscLpFiLtPrtCfgRowStatusTable_Object = MibTable
mscLpFiLtPrtCfgRowStatusTable = _MscLpFiLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgRowStatusTable.setStatus("mandatory")
_MscLpFiLtPrtCfgRowStatusEntry_Object = MibTableRow
mscLpFiLtPrtCfgRowStatusEntry = _MscLpFiLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 1, 1)
)
mscLpFiLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgRowStatusEntry.setStatus("mandatory")
_MscLpFiLtPrtCfgRowStatus_Type = RowStatus
_MscLpFiLtPrtCfgRowStatus_Object = MibTableColumn
mscLpFiLtPrtCfgRowStatus = _MscLpFiLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 1, 1, 1),
    _MscLpFiLtPrtCfgRowStatus_Type()
)
mscLpFiLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgRowStatus.setStatus("mandatory")
_MscLpFiLtPrtCfgComponentName_Type = DisplayString
_MscLpFiLtPrtCfgComponentName_Object = MibTableColumn
mscLpFiLtPrtCfgComponentName = _MscLpFiLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 1, 1, 2),
    _MscLpFiLtPrtCfgComponentName_Type()
)
mscLpFiLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgComponentName.setStatus("mandatory")
_MscLpFiLtPrtCfgStorageType_Type = StorageType
_MscLpFiLtPrtCfgStorageType_Object = MibTableColumn
mscLpFiLtPrtCfgStorageType = _MscLpFiLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 1, 1, 4),
    _MscLpFiLtPrtCfgStorageType_Type()
)
mscLpFiLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgStorageType.setStatus("mandatory")
_MscLpFiLtPrtCfgIndex_Type = NonReplicated
_MscLpFiLtPrtCfgIndex_Object = MibTableColumn
mscLpFiLtPrtCfgIndex = _MscLpFiLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 1, 1, 10),
    _MscLpFiLtPrtCfgIndex_Type()
)
mscLpFiLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgIndex.setStatus("mandatory")
_MscLpFiLtPrtCfgTopTable_Object = MibTable
mscLpFiLtPrtCfgTopTable = _MscLpFiLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgTopTable.setStatus("mandatory")
_MscLpFiLtPrtCfgTopEntry_Object = MibTableRow
mscLpFiLtPrtCfgTopEntry = _MscLpFiLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 10, 1)
)
mscLpFiLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgTopEntry.setStatus("mandatory")


class _MscLpFiLtPrtCfgTData_Type(AsciiString):
    """Custom type mscLpFiLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtPrtCfgTData_Type.__name__ = "AsciiString"
_MscLpFiLtPrtCfgTData_Object = MibTableColumn
mscLpFiLtPrtCfgTData = _MscLpFiLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 4, 10, 1, 1),
    _MscLpFiLtPrtCfgTData_Type()
)
mscLpFiLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtPrtCfgTData.setStatus("mandatory")
_MscLpFiLtFb_ObjectIdentity = ObjectIdentity
mscLpFiLtFb = _MscLpFiLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5)
)
_MscLpFiLtFbRowStatusTable_Object = MibTable
mscLpFiLtFbRowStatusTable = _MscLpFiLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbRowStatusEntry_Object = MibTableRow
mscLpFiLtFbRowStatusEntry = _MscLpFiLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 1, 1)
)
mscLpFiLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbRowStatus_Type = RowStatus
_MscLpFiLtFbRowStatus_Object = MibTableColumn
mscLpFiLtFbRowStatus = _MscLpFiLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 1, 1, 1),
    _MscLpFiLtFbRowStatus_Type()
)
mscLpFiLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbRowStatus.setStatus("mandatory")
_MscLpFiLtFbComponentName_Type = DisplayString
_MscLpFiLtFbComponentName_Object = MibTableColumn
mscLpFiLtFbComponentName = _MscLpFiLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 1, 1, 2),
    _MscLpFiLtFbComponentName_Type()
)
mscLpFiLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbComponentName.setStatus("mandatory")
_MscLpFiLtFbStorageType_Type = StorageType
_MscLpFiLtFbStorageType_Object = MibTableColumn
mscLpFiLtFbStorageType = _MscLpFiLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 1, 1, 4),
    _MscLpFiLtFbStorageType_Type()
)
mscLpFiLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbStorageType.setStatus("mandatory")
_MscLpFiLtFbIndex_Type = NonReplicated
_MscLpFiLtFbIndex_Object = MibTableColumn
mscLpFiLtFbIndex = _MscLpFiLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 1, 1, 10),
    _MscLpFiLtFbIndex_Type()
)
mscLpFiLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbIndex.setStatus("mandatory")
_MscLpFiLtFbTxInfo_ObjectIdentity = ObjectIdentity
mscLpFiLtFbTxInfo = _MscLpFiLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2)
)
_MscLpFiLtFbTxInfoRowStatusTable_Object = MibTable
mscLpFiLtFbTxInfoRowStatusTable = _MscLpFiLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbTxInfoRowStatusEntry_Object = MibTableRow
mscLpFiLtFbTxInfoRowStatusEntry = _MscLpFiLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 1, 1)
)
mscLpFiLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbTxInfoRowStatus_Type = RowStatus
_MscLpFiLtFbTxInfoRowStatus_Object = MibTableColumn
mscLpFiLtFbTxInfoRowStatus = _MscLpFiLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 1, 1, 1),
    _MscLpFiLtFbTxInfoRowStatus_Type()
)
mscLpFiLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoRowStatus.setStatus("mandatory")
_MscLpFiLtFbTxInfoComponentName_Type = DisplayString
_MscLpFiLtFbTxInfoComponentName_Object = MibTableColumn
mscLpFiLtFbTxInfoComponentName = _MscLpFiLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 1, 1, 2),
    _MscLpFiLtFbTxInfoComponentName_Type()
)
mscLpFiLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoComponentName.setStatus("mandatory")
_MscLpFiLtFbTxInfoStorageType_Type = StorageType
_MscLpFiLtFbTxInfoStorageType_Object = MibTableColumn
mscLpFiLtFbTxInfoStorageType = _MscLpFiLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 1, 1, 4),
    _MscLpFiLtFbTxInfoStorageType_Type()
)
mscLpFiLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoStorageType.setStatus("mandatory")
_MscLpFiLtFbTxInfoIndex_Type = NonReplicated
_MscLpFiLtFbTxInfoIndex_Object = MibTableColumn
mscLpFiLtFbTxInfoIndex = _MscLpFiLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 1, 1, 10),
    _MscLpFiLtFbTxInfoIndex_Type()
)
mscLpFiLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoIndex.setStatus("mandatory")
_MscLpFiLtFbTxInfoTopTable_Object = MibTable
mscLpFiLtFbTxInfoTopTable = _MscLpFiLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoTopTable.setStatus("mandatory")
_MscLpFiLtFbTxInfoTopEntry_Object = MibTableRow
mscLpFiLtFbTxInfoTopEntry = _MscLpFiLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 10, 1)
)
mscLpFiLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoTopEntry.setStatus("mandatory")


class _MscLpFiLtFbTxInfoTData_Type(AsciiString):
    """Custom type mscLpFiLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbTxInfoTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbTxInfoTData_Object = MibTableColumn
mscLpFiLtFbTxInfoTData = _MscLpFiLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 2, 10, 1, 1),
    _MscLpFiLtFbTxInfoTData_Type()
)
mscLpFiLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbTxInfoTData.setStatus("mandatory")
_MscLpFiLtFbFddiMac_ObjectIdentity = ObjectIdentity
mscLpFiLtFbFddiMac = _MscLpFiLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3)
)
_MscLpFiLtFbFddiMacRowStatusTable_Object = MibTable
mscLpFiLtFbFddiMacRowStatusTable = _MscLpFiLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbFddiMacRowStatusEntry_Object = MibTableRow
mscLpFiLtFbFddiMacRowStatusEntry = _MscLpFiLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 1, 1)
)
mscLpFiLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbFddiMacRowStatus_Type = RowStatus
_MscLpFiLtFbFddiMacRowStatus_Object = MibTableColumn
mscLpFiLtFbFddiMacRowStatus = _MscLpFiLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 1, 1, 1),
    _MscLpFiLtFbFddiMacRowStatus_Type()
)
mscLpFiLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacRowStatus.setStatus("mandatory")
_MscLpFiLtFbFddiMacComponentName_Type = DisplayString
_MscLpFiLtFbFddiMacComponentName_Object = MibTableColumn
mscLpFiLtFbFddiMacComponentName = _MscLpFiLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 1, 1, 2),
    _MscLpFiLtFbFddiMacComponentName_Type()
)
mscLpFiLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacComponentName.setStatus("mandatory")
_MscLpFiLtFbFddiMacStorageType_Type = StorageType
_MscLpFiLtFbFddiMacStorageType_Object = MibTableColumn
mscLpFiLtFbFddiMacStorageType = _MscLpFiLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 1, 1, 4),
    _MscLpFiLtFbFddiMacStorageType_Type()
)
mscLpFiLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacStorageType.setStatus("mandatory")
_MscLpFiLtFbFddiMacIndex_Type = NonReplicated
_MscLpFiLtFbFddiMacIndex_Object = MibTableColumn
mscLpFiLtFbFddiMacIndex = _MscLpFiLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 1, 1, 10),
    _MscLpFiLtFbFddiMacIndex_Type()
)
mscLpFiLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacIndex.setStatus("mandatory")
_MscLpFiLtFbFddiMacTopTable_Object = MibTable
mscLpFiLtFbFddiMacTopTable = _MscLpFiLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacTopTable.setStatus("mandatory")
_MscLpFiLtFbFddiMacTopEntry_Object = MibTableRow
mscLpFiLtFbFddiMacTopEntry = _MscLpFiLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 10, 1)
)
mscLpFiLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacTopEntry.setStatus("mandatory")


class _MscLpFiLtFbFddiMacTData_Type(AsciiString):
    """Custom type mscLpFiLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbFddiMacTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbFddiMacTData_Object = MibTableColumn
mscLpFiLtFbFddiMacTData = _MscLpFiLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 3, 10, 1, 1),
    _MscLpFiLtFbFddiMacTData_Type()
)
mscLpFiLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbFddiMacTData.setStatus("mandatory")
_MscLpFiLtFbMacEnet_ObjectIdentity = ObjectIdentity
mscLpFiLtFbMacEnet = _MscLpFiLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4)
)
_MscLpFiLtFbMacEnetRowStatusTable_Object = MibTable
mscLpFiLtFbMacEnetRowStatusTable = _MscLpFiLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbMacEnetRowStatusEntry_Object = MibTableRow
mscLpFiLtFbMacEnetRowStatusEntry = _MscLpFiLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 1, 1)
)
mscLpFiLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbMacEnetRowStatus_Type = RowStatus
_MscLpFiLtFbMacEnetRowStatus_Object = MibTableColumn
mscLpFiLtFbMacEnetRowStatus = _MscLpFiLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 1, 1, 1),
    _MscLpFiLtFbMacEnetRowStatus_Type()
)
mscLpFiLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetRowStatus.setStatus("mandatory")
_MscLpFiLtFbMacEnetComponentName_Type = DisplayString
_MscLpFiLtFbMacEnetComponentName_Object = MibTableColumn
mscLpFiLtFbMacEnetComponentName = _MscLpFiLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 1, 1, 2),
    _MscLpFiLtFbMacEnetComponentName_Type()
)
mscLpFiLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetComponentName.setStatus("mandatory")
_MscLpFiLtFbMacEnetStorageType_Type = StorageType
_MscLpFiLtFbMacEnetStorageType_Object = MibTableColumn
mscLpFiLtFbMacEnetStorageType = _MscLpFiLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 1, 1, 4),
    _MscLpFiLtFbMacEnetStorageType_Type()
)
mscLpFiLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetStorageType.setStatus("mandatory")
_MscLpFiLtFbMacEnetIndex_Type = NonReplicated
_MscLpFiLtFbMacEnetIndex_Object = MibTableColumn
mscLpFiLtFbMacEnetIndex = _MscLpFiLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 1, 1, 10),
    _MscLpFiLtFbMacEnetIndex_Type()
)
mscLpFiLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetIndex.setStatus("mandatory")
_MscLpFiLtFbMacEnetTopTable_Object = MibTable
mscLpFiLtFbMacEnetTopTable = _MscLpFiLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetTopTable.setStatus("mandatory")
_MscLpFiLtFbMacEnetTopEntry_Object = MibTableRow
mscLpFiLtFbMacEnetTopEntry = _MscLpFiLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 10, 1)
)
mscLpFiLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetTopEntry.setStatus("mandatory")


class _MscLpFiLtFbMacEnetTData_Type(AsciiString):
    """Custom type mscLpFiLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbMacEnetTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbMacEnetTData_Object = MibTableColumn
mscLpFiLtFbMacEnetTData = _MscLpFiLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 4, 10, 1, 1),
    _MscLpFiLtFbMacEnetTData_Type()
)
mscLpFiLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacEnetTData.setStatus("mandatory")
_MscLpFiLtFbMacTr_ObjectIdentity = ObjectIdentity
mscLpFiLtFbMacTr = _MscLpFiLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5)
)
_MscLpFiLtFbMacTrRowStatusTable_Object = MibTable
mscLpFiLtFbMacTrRowStatusTable = _MscLpFiLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbMacTrRowStatusEntry_Object = MibTableRow
mscLpFiLtFbMacTrRowStatusEntry = _MscLpFiLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 1, 1)
)
mscLpFiLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbMacTrRowStatus_Type = RowStatus
_MscLpFiLtFbMacTrRowStatus_Object = MibTableColumn
mscLpFiLtFbMacTrRowStatus = _MscLpFiLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 1, 1, 1),
    _MscLpFiLtFbMacTrRowStatus_Type()
)
mscLpFiLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrRowStatus.setStatus("mandatory")
_MscLpFiLtFbMacTrComponentName_Type = DisplayString
_MscLpFiLtFbMacTrComponentName_Object = MibTableColumn
mscLpFiLtFbMacTrComponentName = _MscLpFiLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 1, 1, 2),
    _MscLpFiLtFbMacTrComponentName_Type()
)
mscLpFiLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrComponentName.setStatus("mandatory")
_MscLpFiLtFbMacTrStorageType_Type = StorageType
_MscLpFiLtFbMacTrStorageType_Object = MibTableColumn
mscLpFiLtFbMacTrStorageType = _MscLpFiLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 1, 1, 4),
    _MscLpFiLtFbMacTrStorageType_Type()
)
mscLpFiLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrStorageType.setStatus("mandatory")
_MscLpFiLtFbMacTrIndex_Type = NonReplicated
_MscLpFiLtFbMacTrIndex_Object = MibTableColumn
mscLpFiLtFbMacTrIndex = _MscLpFiLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 1, 1, 10),
    _MscLpFiLtFbMacTrIndex_Type()
)
mscLpFiLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrIndex.setStatus("mandatory")
_MscLpFiLtFbMacTrTopTable_Object = MibTable
mscLpFiLtFbMacTrTopTable = _MscLpFiLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrTopTable.setStatus("mandatory")
_MscLpFiLtFbMacTrTopEntry_Object = MibTableRow
mscLpFiLtFbMacTrTopEntry = _MscLpFiLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 10, 1)
)
mscLpFiLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrTopEntry.setStatus("mandatory")


class _MscLpFiLtFbMacTrTData_Type(AsciiString):
    """Custom type mscLpFiLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbMacTrTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbMacTrTData_Object = MibTableColumn
mscLpFiLtFbMacTrTData = _MscLpFiLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 5, 10, 1, 1),
    _MscLpFiLtFbMacTrTData_Type()
)
mscLpFiLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbMacTrTData.setStatus("mandatory")
_MscLpFiLtFbData_ObjectIdentity = ObjectIdentity
mscLpFiLtFbData = _MscLpFiLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6)
)
_MscLpFiLtFbDataRowStatusTable_Object = MibTable
mscLpFiLtFbDataRowStatusTable = _MscLpFiLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbDataRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbDataRowStatusEntry_Object = MibTableRow
mscLpFiLtFbDataRowStatusEntry = _MscLpFiLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 1, 1)
)
mscLpFiLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbDataRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbDataRowStatus_Type = RowStatus
_MscLpFiLtFbDataRowStatus_Object = MibTableColumn
mscLpFiLtFbDataRowStatus = _MscLpFiLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 1, 1, 1),
    _MscLpFiLtFbDataRowStatus_Type()
)
mscLpFiLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbDataRowStatus.setStatus("mandatory")
_MscLpFiLtFbDataComponentName_Type = DisplayString
_MscLpFiLtFbDataComponentName_Object = MibTableColumn
mscLpFiLtFbDataComponentName = _MscLpFiLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 1, 1, 2),
    _MscLpFiLtFbDataComponentName_Type()
)
mscLpFiLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbDataComponentName.setStatus("mandatory")
_MscLpFiLtFbDataStorageType_Type = StorageType
_MscLpFiLtFbDataStorageType_Object = MibTableColumn
mscLpFiLtFbDataStorageType = _MscLpFiLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 1, 1, 4),
    _MscLpFiLtFbDataStorageType_Type()
)
mscLpFiLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbDataStorageType.setStatus("mandatory")
_MscLpFiLtFbDataIndex_Type = NonReplicated
_MscLpFiLtFbDataIndex_Object = MibTableColumn
mscLpFiLtFbDataIndex = _MscLpFiLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 1, 1, 10),
    _MscLpFiLtFbDataIndex_Type()
)
mscLpFiLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbDataIndex.setStatus("mandatory")
_MscLpFiLtFbDataTopTable_Object = MibTable
mscLpFiLtFbDataTopTable = _MscLpFiLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbDataTopTable.setStatus("mandatory")
_MscLpFiLtFbDataTopEntry_Object = MibTableRow
mscLpFiLtFbDataTopEntry = _MscLpFiLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 10, 1)
)
mscLpFiLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbDataTopEntry.setStatus("mandatory")


class _MscLpFiLtFbDataTData_Type(AsciiString):
    """Custom type mscLpFiLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbDataTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbDataTData_Object = MibTableColumn
mscLpFiLtFbDataTData = _MscLpFiLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 6, 10, 1, 1),
    _MscLpFiLtFbDataTData_Type()
)
mscLpFiLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbDataTData.setStatus("mandatory")
_MscLpFiLtFbIpH_ObjectIdentity = ObjectIdentity
mscLpFiLtFbIpH = _MscLpFiLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7)
)
_MscLpFiLtFbIpHRowStatusTable_Object = MibTable
mscLpFiLtFbIpHRowStatusTable = _MscLpFiLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbIpHRowStatusEntry_Object = MibTableRow
mscLpFiLtFbIpHRowStatusEntry = _MscLpFiLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 1, 1)
)
mscLpFiLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbIpHRowStatus_Type = RowStatus
_MscLpFiLtFbIpHRowStatus_Object = MibTableColumn
mscLpFiLtFbIpHRowStatus = _MscLpFiLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 1, 1, 1),
    _MscLpFiLtFbIpHRowStatus_Type()
)
mscLpFiLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHRowStatus.setStatus("mandatory")
_MscLpFiLtFbIpHComponentName_Type = DisplayString
_MscLpFiLtFbIpHComponentName_Object = MibTableColumn
mscLpFiLtFbIpHComponentName = _MscLpFiLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 1, 1, 2),
    _MscLpFiLtFbIpHComponentName_Type()
)
mscLpFiLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHComponentName.setStatus("mandatory")
_MscLpFiLtFbIpHStorageType_Type = StorageType
_MscLpFiLtFbIpHStorageType_Object = MibTableColumn
mscLpFiLtFbIpHStorageType = _MscLpFiLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 1, 1, 4),
    _MscLpFiLtFbIpHStorageType_Type()
)
mscLpFiLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHStorageType.setStatus("mandatory")
_MscLpFiLtFbIpHIndex_Type = NonReplicated
_MscLpFiLtFbIpHIndex_Object = MibTableColumn
mscLpFiLtFbIpHIndex = _MscLpFiLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 1, 1, 10),
    _MscLpFiLtFbIpHIndex_Type()
)
mscLpFiLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHIndex.setStatus("mandatory")
_MscLpFiLtFbIpHTopTable_Object = MibTable
mscLpFiLtFbIpHTopTable = _MscLpFiLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHTopTable.setStatus("mandatory")
_MscLpFiLtFbIpHTopEntry_Object = MibTableRow
mscLpFiLtFbIpHTopEntry = _MscLpFiLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 10, 1)
)
mscLpFiLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHTopEntry.setStatus("mandatory")


class _MscLpFiLtFbIpHTData_Type(AsciiString):
    """Custom type mscLpFiLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbIpHTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbIpHTData_Object = MibTableColumn
mscLpFiLtFbIpHTData = _MscLpFiLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 7, 10, 1, 1),
    _MscLpFiLtFbIpHTData_Type()
)
mscLpFiLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpHTData.setStatus("mandatory")
_MscLpFiLtFbLlch_ObjectIdentity = ObjectIdentity
mscLpFiLtFbLlch = _MscLpFiLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8)
)
_MscLpFiLtFbLlchRowStatusTable_Object = MibTable
mscLpFiLtFbLlchRowStatusTable = _MscLpFiLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbLlchRowStatusEntry_Object = MibTableRow
mscLpFiLtFbLlchRowStatusEntry = _MscLpFiLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 1, 1)
)
mscLpFiLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbLlchRowStatus_Type = RowStatus
_MscLpFiLtFbLlchRowStatus_Object = MibTableColumn
mscLpFiLtFbLlchRowStatus = _MscLpFiLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 1, 1, 1),
    _MscLpFiLtFbLlchRowStatus_Type()
)
mscLpFiLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchRowStatus.setStatus("mandatory")
_MscLpFiLtFbLlchComponentName_Type = DisplayString
_MscLpFiLtFbLlchComponentName_Object = MibTableColumn
mscLpFiLtFbLlchComponentName = _MscLpFiLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 1, 1, 2),
    _MscLpFiLtFbLlchComponentName_Type()
)
mscLpFiLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchComponentName.setStatus("mandatory")
_MscLpFiLtFbLlchStorageType_Type = StorageType
_MscLpFiLtFbLlchStorageType_Object = MibTableColumn
mscLpFiLtFbLlchStorageType = _MscLpFiLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 1, 1, 4),
    _MscLpFiLtFbLlchStorageType_Type()
)
mscLpFiLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchStorageType.setStatus("mandatory")
_MscLpFiLtFbLlchIndex_Type = NonReplicated
_MscLpFiLtFbLlchIndex_Object = MibTableColumn
mscLpFiLtFbLlchIndex = _MscLpFiLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 1, 1, 10),
    _MscLpFiLtFbLlchIndex_Type()
)
mscLpFiLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchIndex.setStatus("mandatory")
_MscLpFiLtFbLlchTopTable_Object = MibTable
mscLpFiLtFbLlchTopTable = _MscLpFiLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchTopTable.setStatus("mandatory")
_MscLpFiLtFbLlchTopEntry_Object = MibTableRow
mscLpFiLtFbLlchTopEntry = _MscLpFiLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 10, 1)
)
mscLpFiLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchTopEntry.setStatus("mandatory")


class _MscLpFiLtFbLlchTData_Type(AsciiString):
    """Custom type mscLpFiLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbLlchTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbLlchTData_Object = MibTableColumn
mscLpFiLtFbLlchTData = _MscLpFiLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 8, 10, 1, 1),
    _MscLpFiLtFbLlchTData_Type()
)
mscLpFiLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbLlchTData.setStatus("mandatory")
_MscLpFiLtFbAppleH_ObjectIdentity = ObjectIdentity
mscLpFiLtFbAppleH = _MscLpFiLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9)
)
_MscLpFiLtFbAppleHRowStatusTable_Object = MibTable
mscLpFiLtFbAppleHRowStatusTable = _MscLpFiLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbAppleHRowStatusEntry_Object = MibTableRow
mscLpFiLtFbAppleHRowStatusEntry = _MscLpFiLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 1, 1)
)
mscLpFiLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbAppleHRowStatus_Type = RowStatus
_MscLpFiLtFbAppleHRowStatus_Object = MibTableColumn
mscLpFiLtFbAppleHRowStatus = _MscLpFiLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 1, 1, 1),
    _MscLpFiLtFbAppleHRowStatus_Type()
)
mscLpFiLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHRowStatus.setStatus("mandatory")
_MscLpFiLtFbAppleHComponentName_Type = DisplayString
_MscLpFiLtFbAppleHComponentName_Object = MibTableColumn
mscLpFiLtFbAppleHComponentName = _MscLpFiLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 1, 1, 2),
    _MscLpFiLtFbAppleHComponentName_Type()
)
mscLpFiLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHComponentName.setStatus("mandatory")
_MscLpFiLtFbAppleHStorageType_Type = StorageType
_MscLpFiLtFbAppleHStorageType_Object = MibTableColumn
mscLpFiLtFbAppleHStorageType = _MscLpFiLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 1, 1, 4),
    _MscLpFiLtFbAppleHStorageType_Type()
)
mscLpFiLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHStorageType.setStatus("mandatory")
_MscLpFiLtFbAppleHIndex_Type = NonReplicated
_MscLpFiLtFbAppleHIndex_Object = MibTableColumn
mscLpFiLtFbAppleHIndex = _MscLpFiLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 1, 1, 10),
    _MscLpFiLtFbAppleHIndex_Type()
)
mscLpFiLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHIndex.setStatus("mandatory")
_MscLpFiLtFbAppleHTopTable_Object = MibTable
mscLpFiLtFbAppleHTopTable = _MscLpFiLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHTopTable.setStatus("mandatory")
_MscLpFiLtFbAppleHTopEntry_Object = MibTableRow
mscLpFiLtFbAppleHTopEntry = _MscLpFiLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 10, 1)
)
mscLpFiLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHTopEntry.setStatus("mandatory")


class _MscLpFiLtFbAppleHTData_Type(AsciiString):
    """Custom type mscLpFiLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbAppleHTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbAppleHTData_Object = MibTableColumn
mscLpFiLtFbAppleHTData = _MscLpFiLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 9, 10, 1, 1),
    _MscLpFiLtFbAppleHTData_Type()
)
mscLpFiLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbAppleHTData.setStatus("mandatory")
_MscLpFiLtFbIpxH_ObjectIdentity = ObjectIdentity
mscLpFiLtFbIpxH = _MscLpFiLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10)
)
_MscLpFiLtFbIpxHRowStatusTable_Object = MibTable
mscLpFiLtFbIpxHRowStatusTable = _MscLpFiLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHRowStatusTable.setStatus("mandatory")
_MscLpFiLtFbIpxHRowStatusEntry_Object = MibTableRow
mscLpFiLtFbIpxHRowStatusEntry = _MscLpFiLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 1, 1)
)
mscLpFiLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHRowStatusEntry.setStatus("mandatory")
_MscLpFiLtFbIpxHRowStatus_Type = RowStatus
_MscLpFiLtFbIpxHRowStatus_Object = MibTableColumn
mscLpFiLtFbIpxHRowStatus = _MscLpFiLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 1, 1, 1),
    _MscLpFiLtFbIpxHRowStatus_Type()
)
mscLpFiLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHRowStatus.setStatus("mandatory")
_MscLpFiLtFbIpxHComponentName_Type = DisplayString
_MscLpFiLtFbIpxHComponentName_Object = MibTableColumn
mscLpFiLtFbIpxHComponentName = _MscLpFiLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 1, 1, 2),
    _MscLpFiLtFbIpxHComponentName_Type()
)
mscLpFiLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHComponentName.setStatus("mandatory")
_MscLpFiLtFbIpxHStorageType_Type = StorageType
_MscLpFiLtFbIpxHStorageType_Object = MibTableColumn
mscLpFiLtFbIpxHStorageType = _MscLpFiLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 1, 1, 4),
    _MscLpFiLtFbIpxHStorageType_Type()
)
mscLpFiLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHStorageType.setStatus("mandatory")
_MscLpFiLtFbIpxHIndex_Type = NonReplicated
_MscLpFiLtFbIpxHIndex_Object = MibTableColumn
mscLpFiLtFbIpxHIndex = _MscLpFiLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 1, 1, 10),
    _MscLpFiLtFbIpxHIndex_Type()
)
mscLpFiLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHIndex.setStatus("mandatory")
_MscLpFiLtFbIpxHTopTable_Object = MibTable
mscLpFiLtFbIpxHTopTable = _MscLpFiLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHTopTable.setStatus("mandatory")
_MscLpFiLtFbIpxHTopEntry_Object = MibTableRow
mscLpFiLtFbIpxHTopEntry = _MscLpFiLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 10, 1)
)
mscLpFiLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHTopEntry.setStatus("mandatory")


class _MscLpFiLtFbIpxHTData_Type(AsciiString):
    """Custom type mscLpFiLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbIpxHTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbIpxHTData_Object = MibTableColumn
mscLpFiLtFbIpxHTData = _MscLpFiLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 10, 10, 1, 1),
    _MscLpFiLtFbIpxHTData_Type()
)
mscLpFiLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbIpxHTData.setStatus("mandatory")
_MscLpFiLtFbTopTable_Object = MibTable
mscLpFiLtFbTopTable = _MscLpFiLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 20)
)
if mibBuilder.loadTexts:
    mscLpFiLtFbTopTable.setStatus("mandatory")
_MscLpFiLtFbTopEntry_Object = MibTableRow
mscLpFiLtFbTopEntry = _MscLpFiLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 20, 1)
)
mscLpFiLtFbTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtFbTopEntry.setStatus("mandatory")


class _MscLpFiLtFbTData_Type(AsciiString):
    """Custom type mscLpFiLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtFbTData_Type.__name__ = "AsciiString"
_MscLpFiLtFbTData_Object = MibTableColumn
mscLpFiLtFbTData = _MscLpFiLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 5, 20, 1, 1),
    _MscLpFiLtFbTData_Type()
)
mscLpFiLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtFbTData.setStatus("mandatory")
_MscLpFiLtCntl_ObjectIdentity = ObjectIdentity
mscLpFiLtCntl = _MscLpFiLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6)
)
_MscLpFiLtCntlRowStatusTable_Object = MibTable
mscLpFiLtCntlRowStatusTable = _MscLpFiLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpFiLtCntlRowStatusTable.setStatus("mandatory")
_MscLpFiLtCntlRowStatusEntry_Object = MibTableRow
mscLpFiLtCntlRowStatusEntry = _MscLpFiLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 1, 1)
)
mscLpFiLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtCntlRowStatusEntry.setStatus("mandatory")
_MscLpFiLtCntlRowStatus_Type = RowStatus
_MscLpFiLtCntlRowStatus_Object = MibTableColumn
mscLpFiLtCntlRowStatus = _MscLpFiLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 1, 1, 1),
    _MscLpFiLtCntlRowStatus_Type()
)
mscLpFiLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtCntlRowStatus.setStatus("mandatory")
_MscLpFiLtCntlComponentName_Type = DisplayString
_MscLpFiLtCntlComponentName_Object = MibTableColumn
mscLpFiLtCntlComponentName = _MscLpFiLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 1, 1, 2),
    _MscLpFiLtCntlComponentName_Type()
)
mscLpFiLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtCntlComponentName.setStatus("mandatory")
_MscLpFiLtCntlStorageType_Type = StorageType
_MscLpFiLtCntlStorageType_Object = MibTableColumn
mscLpFiLtCntlStorageType = _MscLpFiLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 1, 1, 4),
    _MscLpFiLtCntlStorageType_Type()
)
mscLpFiLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLtCntlStorageType.setStatus("mandatory")
_MscLpFiLtCntlIndex_Type = NonReplicated
_MscLpFiLtCntlIndex_Object = MibTableColumn
mscLpFiLtCntlIndex = _MscLpFiLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 1, 1, 10),
    _MscLpFiLtCntlIndex_Type()
)
mscLpFiLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiLtCntlIndex.setStatus("mandatory")
_MscLpFiLtCntlTopTable_Object = MibTable
mscLpFiLtCntlTopTable = _MscLpFiLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpFiLtCntlTopTable.setStatus("mandatory")
_MscLpFiLtCntlTopEntry_Object = MibTableRow
mscLpFiLtCntlTopEntry = _MscLpFiLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 10, 1)
)
mscLpFiLtCntlTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtCntlTopEntry.setStatus("mandatory")


class _MscLpFiLtCntlTData_Type(AsciiString):
    """Custom type mscLpFiLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtCntlTData_Type.__name__ = "AsciiString"
_MscLpFiLtCntlTData_Object = MibTableColumn
mscLpFiLtCntlTData = _MscLpFiLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 6, 10, 1, 1),
    _MscLpFiLtCntlTData_Type()
)
mscLpFiLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtCntlTData.setStatus("mandatory")
_MscLpFiLtTopTable_Object = MibTable
mscLpFiLtTopTable = _MscLpFiLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 20)
)
if mibBuilder.loadTexts:
    mscLpFiLtTopTable.setStatus("mandatory")
_MscLpFiLtTopEntry_Object = MibTableRow
mscLpFiLtTopEntry = _MscLpFiLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 20, 1)
)
mscLpFiLtTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiLtTopEntry.setStatus("mandatory")


class _MscLpFiLtTData_Type(AsciiString):
    """Custom type mscLpFiLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpFiLtTData_Type.__name__ = "AsciiString"
_MscLpFiLtTData_Object = MibTableColumn
mscLpFiLtTData = _MscLpFiLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 2, 20, 1, 1),
    _MscLpFiLtTData_Type()
)
mscLpFiLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiLtTData.setStatus("mandatory")
_MscLpFiPhy_ObjectIdentity = ObjectIdentity
mscLpFiPhy = _MscLpFiPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3)
)
_MscLpFiPhyRowStatusTable_Object = MibTable
mscLpFiPhyRowStatusTable = _MscLpFiPhyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpFiPhyRowStatusTable.setStatus("mandatory")
_MscLpFiPhyRowStatusEntry_Object = MibTableRow
mscLpFiPhyRowStatusEntry = _MscLpFiPhyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 1, 1)
)
mscLpFiPhyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiPhyFddiPhyTypeIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiPhyRowStatusEntry.setStatus("mandatory")
_MscLpFiPhyRowStatus_Type = RowStatus
_MscLpFiPhyRowStatus_Object = MibTableColumn
mscLpFiPhyRowStatus = _MscLpFiPhyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 1, 1, 1),
    _MscLpFiPhyRowStatus_Type()
)
mscLpFiPhyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiPhyRowStatus.setStatus("mandatory")
_MscLpFiPhyComponentName_Type = DisplayString
_MscLpFiPhyComponentName_Object = MibTableColumn
mscLpFiPhyComponentName = _MscLpFiPhyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 1, 1, 2),
    _MscLpFiPhyComponentName_Type()
)
mscLpFiPhyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyComponentName.setStatus("mandatory")
_MscLpFiPhyStorageType_Type = StorageType
_MscLpFiPhyStorageType_Object = MibTableColumn
mscLpFiPhyStorageType = _MscLpFiPhyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 1, 1, 4),
    _MscLpFiPhyStorageType_Type()
)
mscLpFiPhyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyStorageType.setStatus("mandatory")


class _MscLpFiPhyFddiPhyTypeIndex_Type(Integer32):
    """Custom type mscLpFiPhyFddiPhyTypeIndex based on Integer32"""
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


_MscLpFiPhyFddiPhyTypeIndex_Type.__name__ = "Integer32"
_MscLpFiPhyFddiPhyTypeIndex_Object = MibTableColumn
mscLpFiPhyFddiPhyTypeIndex = _MscLpFiPhyFddiPhyTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 1, 1, 10),
    _MscLpFiPhyFddiPhyTypeIndex_Type()
)
mscLpFiPhyFddiPhyTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiPhyFddiPhyTypeIndex.setStatus("mandatory")
_MscLpFiPhyProvTable_Object = MibTable
mscLpFiPhyProvTable = _MscLpFiPhyProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpFiPhyProvTable.setStatus("mandatory")
_MscLpFiPhyProvEntry_Object = MibTableRow
mscLpFiPhyProvEntry = _MscLpFiPhyProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 10, 1)
)
mscLpFiPhyProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiPhyFddiPhyTypeIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiPhyProvEntry.setStatus("mandatory")


class _MscLpFiPhyLerCutoff_Type(Unsigned32):
    """Custom type mscLpFiPhyLerCutoff based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_MscLpFiPhyLerCutoff_Type.__name__ = "Unsigned32"
_MscLpFiPhyLerCutoff_Object = MibTableColumn
mscLpFiPhyLerCutoff = _MscLpFiPhyLerCutoff_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 10, 1, 1),
    _MscLpFiPhyLerCutoff_Type()
)
mscLpFiPhyLerCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiPhyLerCutoff.setStatus("mandatory")


class _MscLpFiPhyLerAlarm_Type(Unsigned32):
    """Custom type mscLpFiPhyLerAlarm based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_MscLpFiPhyLerAlarm_Type.__name__ = "Unsigned32"
_MscLpFiPhyLerAlarm_Object = MibTableColumn
mscLpFiPhyLerAlarm = _MscLpFiPhyLerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 10, 1, 2),
    _MscLpFiPhyLerAlarm_Type()
)
mscLpFiPhyLerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiPhyLerAlarm.setStatus("mandatory")


class _MscLpFiPhyLinkErrorMonitor_Type(Integer32):
    """Custom type mscLpFiPhyLinkErrorMonitor based on Integer32"""
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


_MscLpFiPhyLinkErrorMonitor_Type.__name__ = "Integer32"
_MscLpFiPhyLinkErrorMonitor_Object = MibTableColumn
mscLpFiPhyLinkErrorMonitor = _MscLpFiPhyLinkErrorMonitor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 10, 1, 3),
    _MscLpFiPhyLinkErrorMonitor_Type()
)
mscLpFiPhyLinkErrorMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiPhyLinkErrorMonitor.setStatus("mandatory")
_MscLpFiPhyOperTable_Object = MibTable
mscLpFiPhyOperTable = _MscLpFiPhyOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11)
)
if mibBuilder.loadTexts:
    mscLpFiPhyOperTable.setStatus("mandatory")
_MscLpFiPhyOperEntry_Object = MibTableRow
mscLpFiPhyOperEntry = _MscLpFiPhyOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1)
)
mscLpFiPhyOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiPhyFddiPhyTypeIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiPhyOperEntry.setStatus("mandatory")


class _MscLpFiPhyNeighborType_Type(Integer32):
    """Custom type mscLpFiPhyNeighborType based on Integer32"""
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


_MscLpFiPhyNeighborType_Type.__name__ = "Integer32"
_MscLpFiPhyNeighborType_Object = MibTableColumn
mscLpFiPhyNeighborType = _MscLpFiPhyNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 4),
    _MscLpFiPhyNeighborType_Type()
)
mscLpFiPhyNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyNeighborType.setStatus("mandatory")
_MscLpFiPhyLctFailCounts_Type = Counter32
_MscLpFiPhyLctFailCounts_Object = MibTableColumn
mscLpFiPhyLctFailCounts = _MscLpFiPhyLctFailCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 13),
    _MscLpFiPhyLctFailCounts_Type()
)
mscLpFiPhyLctFailCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyLctFailCounts.setStatus("mandatory")


class _MscLpFiPhyLerEstimate_Type(Unsigned32):
    """Custom type mscLpFiPhyLerEstimate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_MscLpFiPhyLerEstimate_Type.__name__ = "Unsigned32"
_MscLpFiPhyLerEstimate_Object = MibTableColumn
mscLpFiPhyLerEstimate = _MscLpFiPhyLerEstimate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 14),
    _MscLpFiPhyLerEstimate_Type()
)
mscLpFiPhyLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyLerEstimate.setStatus("mandatory")
_MscLpFiPhyLemRejectCounts_Type = Counter32
_MscLpFiPhyLemRejectCounts_Object = MibTableColumn
mscLpFiPhyLemRejectCounts = _MscLpFiPhyLemRejectCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 15),
    _MscLpFiPhyLemRejectCounts_Type()
)
mscLpFiPhyLemRejectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyLemRejectCounts.setStatus("mandatory")
_MscLpFiPhyLemCounts_Type = Counter32
_MscLpFiPhyLemCounts_Object = MibTableColumn
mscLpFiPhyLemCounts = _MscLpFiPhyLemCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 16),
    _MscLpFiPhyLemCounts_Type()
)
mscLpFiPhyLemCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyLemCounts.setStatus("mandatory")


class _MscLpFiPhyPcmState_Type(Integer32):
    """Custom type mscLpFiPhyPcmState based on Integer32"""
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


_MscLpFiPhyPcmState_Type.__name__ = "Integer32"
_MscLpFiPhyPcmState_Object = MibTableColumn
mscLpFiPhyPcmState = _MscLpFiPhyPcmState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 18),
    _MscLpFiPhyPcmState_Type()
)
mscLpFiPhyPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyPcmState.setStatus("mandatory")


class _MscLpFiPhyLerFlag_Type(Integer32):
    """Custom type mscLpFiPhyLerFlag based on Integer32"""
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


_MscLpFiPhyLerFlag_Type.__name__ = "Integer32"
_MscLpFiPhyLerFlag_Object = MibTableColumn
mscLpFiPhyLerFlag = _MscLpFiPhyLerFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 20),
    _MscLpFiPhyLerFlag_Type()
)
mscLpFiPhyLerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhyLerFlag.setStatus("mandatory")


class _MscLpFiPhySignalState_Type(Integer32):
    """Custom type mscLpFiPhySignalState based on Integer32"""
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


_MscLpFiPhySignalState_Type.__name__ = "Integer32"
_MscLpFiPhySignalState_Object = MibTableColumn
mscLpFiPhySignalState = _MscLpFiPhySignalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 23),
    _MscLpFiPhySignalState_Type()
)
mscLpFiPhySignalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhySignalState.setStatus("mandatory")


class _MscLpFiPhySignalBitsRcvd_Type(OctetString):
    """Custom type mscLpFiPhySignalBitsRcvd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpFiPhySignalBitsRcvd_Type.__name__ = "OctetString"
_MscLpFiPhySignalBitsRcvd_Object = MibTableColumn
mscLpFiPhySignalBitsRcvd = _MscLpFiPhySignalBitsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 24),
    _MscLpFiPhySignalBitsRcvd_Type()
)
mscLpFiPhySignalBitsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhySignalBitsRcvd.setStatus("mandatory")


class _MscLpFiPhySignalBitsTxmt_Type(OctetString):
    """Custom type mscLpFiPhySignalBitsTxmt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpFiPhySignalBitsTxmt_Type.__name__ = "OctetString"
_MscLpFiPhySignalBitsTxmt_Object = MibTableColumn
mscLpFiPhySignalBitsTxmt = _MscLpFiPhySignalBitsTxmt_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 3, 11, 1, 25),
    _MscLpFiPhySignalBitsTxmt_Type()
)
mscLpFiPhySignalBitsTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiPhySignalBitsTxmt.setStatus("mandatory")
_MscLpFiTest_ObjectIdentity = ObjectIdentity
mscLpFiTest = _MscLpFiTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5)
)
_MscLpFiTestRowStatusTable_Object = MibTable
mscLpFiTestRowStatusTable = _MscLpFiTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpFiTestRowStatusTable.setStatus("mandatory")
_MscLpFiTestRowStatusEntry_Object = MibTableRow
mscLpFiTestRowStatusEntry = _MscLpFiTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 1, 1)
)
mscLpFiTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiTestRowStatusEntry.setStatus("mandatory")
_MscLpFiTestRowStatus_Type = RowStatus
_MscLpFiTestRowStatus_Object = MibTableColumn
mscLpFiTestRowStatus = _MscLpFiTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 1, 1, 1),
    _MscLpFiTestRowStatus_Type()
)
mscLpFiTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestRowStatus.setStatus("mandatory")
_MscLpFiTestComponentName_Type = DisplayString
_MscLpFiTestComponentName_Object = MibTableColumn
mscLpFiTestComponentName = _MscLpFiTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 1, 1, 2),
    _MscLpFiTestComponentName_Type()
)
mscLpFiTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestComponentName.setStatus("mandatory")
_MscLpFiTestStorageType_Type = StorageType
_MscLpFiTestStorageType_Object = MibTableColumn
mscLpFiTestStorageType = _MscLpFiTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 1, 1, 4),
    _MscLpFiTestStorageType_Type()
)
mscLpFiTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestStorageType.setStatus("mandatory")
_MscLpFiTestIndex_Type = NonReplicated
_MscLpFiTestIndex_Object = MibTableColumn
mscLpFiTestIndex = _MscLpFiTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 1, 1, 10),
    _MscLpFiTestIndex_Type()
)
mscLpFiTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpFiTestIndex.setStatus("mandatory")
_MscLpFiTestPTOTable_Object = MibTable
mscLpFiTestPTOTable = _MscLpFiTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpFiTestPTOTable.setStatus("mandatory")
_MscLpFiTestPTOEntry_Object = MibTableRow
mscLpFiTestPTOEntry = _MscLpFiTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 10, 1)
)
mscLpFiTestPTOEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiTestPTOEntry.setStatus("mandatory")


class _MscLpFiTestType_Type(Integer32):
    """Custom type mscLpFiTestType based on Integer32"""
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


_MscLpFiTestType_Type.__name__ = "Integer32"
_MscLpFiTestType_Object = MibTableColumn
mscLpFiTestType = _MscLpFiTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 10, 1, 1),
    _MscLpFiTestType_Type()
)
mscLpFiTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiTestType.setStatus("mandatory")


class _MscLpFiTestFrmSize_Type(Unsigned32):
    """Custom type mscLpFiTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscLpFiTestFrmSize_Type.__name__ = "Unsigned32"
_MscLpFiTestFrmSize_Object = MibTableColumn
mscLpFiTestFrmSize = _MscLpFiTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 10, 1, 2),
    _MscLpFiTestFrmSize_Type()
)
mscLpFiTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiTestFrmSize.setStatus("mandatory")


class _MscLpFiTestDuration_Type(Unsigned32):
    """Custom type mscLpFiTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscLpFiTestDuration_Type.__name__ = "Unsigned32"
_MscLpFiTestDuration_Object = MibTableColumn
mscLpFiTestDuration = _MscLpFiTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 10, 1, 3),
    _MscLpFiTestDuration_Type()
)
mscLpFiTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiTestDuration.setStatus("mandatory")
_MscLpFiTestResultsTable_Object = MibTable
mscLpFiTestResultsTable = _MscLpFiTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11)
)
if mibBuilder.loadTexts:
    mscLpFiTestResultsTable.setStatus("mandatory")
_MscLpFiTestResultsEntry_Object = MibTableRow
mscLpFiTestResultsEntry = _MscLpFiTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1)
)
mscLpFiTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiTestResultsEntry.setStatus("mandatory")
_MscLpFiTestElapsedTime_Type = Counter32
_MscLpFiTestElapsedTime_Object = MibTableColumn
mscLpFiTestElapsedTime = _MscLpFiTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 4),
    _MscLpFiTestElapsedTime_Type()
)
mscLpFiTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestElapsedTime.setStatus("mandatory")


class _MscLpFiTestTimeRemaining_Type(Unsigned32):
    """Custom type mscLpFiTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpFiTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscLpFiTestTimeRemaining_Object = MibTableColumn
mscLpFiTestTimeRemaining = _MscLpFiTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 5),
    _MscLpFiTestTimeRemaining_Type()
)
mscLpFiTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestTimeRemaining.setStatus("mandatory")


class _MscLpFiTestCauseOfTermination_Type(Integer32):
    """Custom type mscLpFiTestCauseOfTermination based on Integer32"""
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


_MscLpFiTestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpFiTestCauseOfTermination_Object = MibTableColumn
mscLpFiTestCauseOfTermination = _MscLpFiTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 6),
    _MscLpFiTestCauseOfTermination_Type()
)
mscLpFiTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestCauseOfTermination.setStatus("mandatory")
_MscLpFiTestFrmTx_Type = PassportCounter64
_MscLpFiTestFrmTx_Object = MibTableColumn
mscLpFiTestFrmTx = _MscLpFiTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 7),
    _MscLpFiTestFrmTx_Type()
)
mscLpFiTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestFrmTx.setStatus("mandatory")
_MscLpFiTestBitsTx_Type = PassportCounter64
_MscLpFiTestBitsTx_Object = MibTableColumn
mscLpFiTestBitsTx = _MscLpFiTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 8),
    _MscLpFiTestBitsTx_Type()
)
mscLpFiTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestBitsTx.setStatus("mandatory")
_MscLpFiTestFrmRx_Type = PassportCounter64
_MscLpFiTestFrmRx_Object = MibTableColumn
mscLpFiTestFrmRx = _MscLpFiTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 9),
    _MscLpFiTestFrmRx_Type()
)
mscLpFiTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestFrmRx.setStatus("mandatory")
_MscLpFiTestBitsRx_Type = PassportCounter64
_MscLpFiTestBitsRx_Object = MibTableColumn
mscLpFiTestBitsRx = _MscLpFiTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 10),
    _MscLpFiTestBitsRx_Type()
)
mscLpFiTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestBitsRx.setStatus("mandatory")
_MscLpFiTestErroredFrmRx_Type = PassportCounter64
_MscLpFiTestErroredFrmRx_Object = MibTableColumn
mscLpFiTestErroredFrmRx = _MscLpFiTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 5, 11, 1, 11),
    _MscLpFiTestErroredFrmRx_Type()
)
mscLpFiTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTestErroredFrmRx.setStatus("mandatory")
_MscLpFiCidDataTable_Object = MibTable
mscLpFiCidDataTable = _MscLpFiCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpFiCidDataTable.setStatus("mandatory")
_MscLpFiCidDataEntry_Object = MibTableRow
mscLpFiCidDataEntry = _MscLpFiCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 10, 1)
)
mscLpFiCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiCidDataEntry.setStatus("mandatory")


class _MscLpFiCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLpFiCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLpFiCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLpFiCustomerIdentifier_Object = MibTableColumn
mscLpFiCustomerIdentifier = _MscLpFiCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 10, 1, 1),
    _MscLpFiCustomerIdentifier_Type()
)
mscLpFiCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiCustomerIdentifier.setStatus("mandatory")
_MscLpFiIfEntryTable_Object = MibTable
mscLpFiIfEntryTable = _MscLpFiIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 11)
)
if mibBuilder.loadTexts:
    mscLpFiIfEntryTable.setStatus("mandatory")
_MscLpFiIfEntryEntry_Object = MibTableRow
mscLpFiIfEntryEntry = _MscLpFiIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 11, 1)
)
mscLpFiIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiIfEntryEntry.setStatus("mandatory")


class _MscLpFiIfAdminStatus_Type(Integer32):
    """Custom type mscLpFiIfAdminStatus based on Integer32"""
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


_MscLpFiIfAdminStatus_Type.__name__ = "Integer32"
_MscLpFiIfAdminStatus_Object = MibTableColumn
mscLpFiIfAdminStatus = _MscLpFiIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 11, 1, 1),
    _MscLpFiIfAdminStatus_Type()
)
mscLpFiIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiIfAdminStatus.setStatus("mandatory")


class _MscLpFiIfIndex_Type(InterfaceIndex):
    """Custom type mscLpFiIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLpFiIfIndex_Type.__name__ = "InterfaceIndex"
_MscLpFiIfIndex_Object = MibTableColumn
mscLpFiIfIndex = _MscLpFiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 11, 1, 2),
    _MscLpFiIfIndex_Type()
)
mscLpFiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiIfIndex.setStatus("mandatory")
_MscLpFiSmtProvTable_Object = MibTable
mscLpFiSmtProvTable = _MscLpFiSmtProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12)
)
if mibBuilder.loadTexts:
    mscLpFiSmtProvTable.setStatus("mandatory")
_MscLpFiSmtProvEntry_Object = MibTableRow
mscLpFiSmtProvEntry = _MscLpFiSmtProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1)
)
mscLpFiSmtProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiSmtProvEntry.setStatus("mandatory")


class _MscLpFiUserData_Type(AsciiString):
    """Custom type mscLpFiUserData based on AsciiString"""
    defaultHexValue = "46444449"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscLpFiUserData_Type.__name__ = "AsciiString"
_MscLpFiUserData_Object = MibTableColumn
mscLpFiUserData = _MscLpFiUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 1),
    _MscLpFiUserData_Type()
)
mscLpFiUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiUserData.setStatus("mandatory")


class _MscLpFiAcceptAa_Type(Integer32):
    """Custom type mscLpFiAcceptAa based on Integer32"""
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


_MscLpFiAcceptAa_Type.__name__ = "Integer32"
_MscLpFiAcceptAa_Object = MibTableColumn
mscLpFiAcceptAa = _MscLpFiAcceptAa_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 2),
    _MscLpFiAcceptAa_Type()
)
mscLpFiAcceptAa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiAcceptAa.setStatus("mandatory")


class _MscLpFiAcceptBb_Type(Integer32):
    """Custom type mscLpFiAcceptBb based on Integer32"""
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


_MscLpFiAcceptBb_Type.__name__ = "Integer32"
_MscLpFiAcceptBb_Object = MibTableColumn
mscLpFiAcceptBb = _MscLpFiAcceptBb_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 3),
    _MscLpFiAcceptBb_Type()
)
mscLpFiAcceptBb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiAcceptBb.setStatus("mandatory")


class _MscLpFiAcceptAs_Type(Integer32):
    """Custom type mscLpFiAcceptAs based on Integer32"""
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


_MscLpFiAcceptAs_Type.__name__ = "Integer32"
_MscLpFiAcceptAs_Object = MibTableColumn
mscLpFiAcceptAs = _MscLpFiAcceptAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 4),
    _MscLpFiAcceptAs_Type()
)
mscLpFiAcceptAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiAcceptAs.setStatus("mandatory")


class _MscLpFiAcceptBs_Type(Integer32):
    """Custom type mscLpFiAcceptBs based on Integer32"""
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


_MscLpFiAcceptBs_Type.__name__ = "Integer32"
_MscLpFiAcceptBs_Object = MibTableColumn
mscLpFiAcceptBs = _MscLpFiAcceptBs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 5),
    _MscLpFiAcceptBs_Type()
)
mscLpFiAcceptBs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiAcceptBs.setStatus("mandatory")


class _MscLpFiAcceptAm_Type(Integer32):
    """Custom type mscLpFiAcceptAm based on Integer32"""
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


_MscLpFiAcceptAm_Type.__name__ = "Integer32"
_MscLpFiAcceptAm_Object = MibTableColumn
mscLpFiAcceptAm = _MscLpFiAcceptAm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 6),
    _MscLpFiAcceptAm_Type()
)
mscLpFiAcceptAm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiAcceptAm.setStatus("mandatory")


class _MscLpFiAcceptBm_Type(Integer32):
    """Custom type mscLpFiAcceptBm based on Integer32"""
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


_MscLpFiAcceptBm_Type.__name__ = "Integer32"
_MscLpFiAcceptBm_Object = MibTableColumn
mscLpFiAcceptBm = _MscLpFiAcceptBm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 7),
    _MscLpFiAcceptBm_Type()
)
mscLpFiAcceptBm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiAcceptBm.setStatus("mandatory")


class _MscLpFiUseThruBa_Type(Integer32):
    """Custom type mscLpFiUseThruBa based on Integer32"""
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


_MscLpFiUseThruBa_Type.__name__ = "Integer32"
_MscLpFiUseThruBa_Object = MibTableColumn
mscLpFiUseThruBa = _MscLpFiUseThruBa_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 8),
    _MscLpFiUseThruBa_Type()
)
mscLpFiUseThruBa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiUseThruBa.setStatus("mandatory")


class _MscLpFiNeighborNotifyInterval_Type(Unsigned32):
    """Custom type mscLpFiNeighborNotifyInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_MscLpFiNeighborNotifyInterval_Type.__name__ = "Unsigned32"
_MscLpFiNeighborNotifyInterval_Object = MibTableColumn
mscLpFiNeighborNotifyInterval = _MscLpFiNeighborNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 10),
    _MscLpFiNeighborNotifyInterval_Type()
)
mscLpFiNeighborNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiNeighborNotifyInterval.setStatus("mandatory")


class _MscLpFiStatusReportPolicy_Type(Integer32):
    """Custom type mscLpFiStatusReportPolicy based on Integer32"""
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


_MscLpFiStatusReportPolicy_Type.__name__ = "Integer32"
_MscLpFiStatusReportPolicy_Object = MibTableColumn
mscLpFiStatusReportPolicy = _MscLpFiStatusReportPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 11),
    _MscLpFiStatusReportPolicy_Type()
)
mscLpFiStatusReportPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiStatusReportPolicy.setStatus("mandatory")


class _MscLpFiTraceMaxExpirationTimer_Type(FddiTimeMilli):
    """Custom type mscLpFiTraceMaxExpirationTimer based on FddiTimeMilli"""
    defaultValue = 7000

    subtypeSpec = FddiTimeMilli.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MscLpFiTraceMaxExpirationTimer_Type.__name__ = "FddiTimeMilli"
_MscLpFiTraceMaxExpirationTimer_Object = MibTableColumn
mscLpFiTraceMaxExpirationTimer = _MscLpFiTraceMaxExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 12),
    _MscLpFiTraceMaxExpirationTimer_Type()
)
mscLpFiTraceMaxExpirationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiTraceMaxExpirationTimer.setStatus("mandatory")
_MscLpFiApplicationFramerName_Type = Link
_MscLpFiApplicationFramerName_Object = MibTableColumn
mscLpFiApplicationFramerName = _MscLpFiApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 12, 1, 13),
    _MscLpFiApplicationFramerName_Type()
)
mscLpFiApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiApplicationFramerName.setStatus("mandatory")
_MscLpFiMacProvTable_Object = MibTable
mscLpFiMacProvTable = _MscLpFiMacProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 13)
)
if mibBuilder.loadTexts:
    mscLpFiMacProvTable.setStatus("mandatory")
_MscLpFiMacProvEntry_Object = MibTableRow
mscLpFiMacProvEntry = _MscLpFiMacProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 13, 1)
)
mscLpFiMacProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiMacProvEntry.setStatus("mandatory")


class _MscLpFiTokenRequestTimer_Type(FddiTimeNano):
    """Custom type mscLpFiTokenRequestTimer based on FddiTimeNano"""
    defaultValue = 165290000

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20480, 1340000000),
    )


_MscLpFiTokenRequestTimer_Type.__name__ = "FddiTimeNano"
_MscLpFiTokenRequestTimer_Object = MibTableColumn
mscLpFiTokenRequestTimer = _MscLpFiTokenRequestTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 13, 1, 1),
    _MscLpFiTokenRequestTimer_Type()
)
mscLpFiTokenRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiTokenRequestTimer.setStatus("mandatory")


class _MscLpFiTokenMaxTimer_Type(FddiTimeNano):
    """Custom type mscLpFiTokenMaxTimer based on FddiTimeNano"""
    defaultValue = 167770000

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40960, 1342200000),
    )


_MscLpFiTokenMaxTimer_Type.__name__ = "FddiTimeNano"
_MscLpFiTokenMaxTimer_Object = MibTableColumn
mscLpFiTokenMaxTimer = _MscLpFiTokenMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 13, 1, 2),
    _MscLpFiTokenMaxTimer_Type()
)
mscLpFiTokenMaxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiTokenMaxTimer.setStatus("mandatory")


class _MscLpFiValidTransmissionTimer_Type(FddiTimeNano):
    """Custom type mscLpFiValidTransmissionTimer based on FddiTimeNano"""
    defaultValue = 2621400

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40960, 1342200000),
    )


_MscLpFiValidTransmissionTimer_Type.__name__ = "FddiTimeNano"
_MscLpFiValidTransmissionTimer_Object = MibTableColumn
mscLpFiValidTransmissionTimer = _MscLpFiValidTransmissionTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 13, 1, 3),
    _MscLpFiValidTransmissionTimer_Type()
)
mscLpFiValidTransmissionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiValidTransmissionTimer.setStatus("mandatory")
_MscLpFiAdminInfoTable_Object = MibTable
mscLpFiAdminInfoTable = _MscLpFiAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 14)
)
if mibBuilder.loadTexts:
    mscLpFiAdminInfoTable.setStatus("mandatory")
_MscLpFiAdminInfoEntry_Object = MibTableRow
mscLpFiAdminInfoEntry = _MscLpFiAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 14, 1)
)
mscLpFiAdminInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiAdminInfoEntry.setStatus("mandatory")


class _MscLpFiVendor_Type(AsciiString):
    """Custom type mscLpFiVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLpFiVendor_Type.__name__ = "AsciiString"
_MscLpFiVendor_Object = MibTableColumn
mscLpFiVendor = _MscLpFiVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 14, 1, 1),
    _MscLpFiVendor_Type()
)
mscLpFiVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiVendor.setStatus("mandatory")


class _MscLpFiCommentText_Type(AsciiString):
    """Custom type mscLpFiCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_MscLpFiCommentText_Type.__name__ = "AsciiString"
_MscLpFiCommentText_Object = MibTableColumn
mscLpFiCommentText = _MscLpFiCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 14, 1, 2),
    _MscLpFiCommentText_Type()
)
mscLpFiCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpFiCommentText.setStatus("mandatory")
_MscLpFiStateTable_Object = MibTable
mscLpFiStateTable = _MscLpFiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 16)
)
if mibBuilder.loadTexts:
    mscLpFiStateTable.setStatus("mandatory")
_MscLpFiStateEntry_Object = MibTableRow
mscLpFiStateEntry = _MscLpFiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 16, 1)
)
mscLpFiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiStateEntry.setStatus("mandatory")


class _MscLpFiAdminState_Type(Integer32):
    """Custom type mscLpFiAdminState based on Integer32"""
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


_MscLpFiAdminState_Type.__name__ = "Integer32"
_MscLpFiAdminState_Object = MibTableColumn
mscLpFiAdminState = _MscLpFiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 16, 1, 1),
    _MscLpFiAdminState_Type()
)
mscLpFiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiAdminState.setStatus("mandatory")


class _MscLpFiOperationalState_Type(Integer32):
    """Custom type mscLpFiOperationalState based on Integer32"""
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


_MscLpFiOperationalState_Type.__name__ = "Integer32"
_MscLpFiOperationalState_Object = MibTableColumn
mscLpFiOperationalState = _MscLpFiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 16, 1, 2),
    _MscLpFiOperationalState_Type()
)
mscLpFiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiOperationalState.setStatus("mandatory")


class _MscLpFiUsageState_Type(Integer32):
    """Custom type mscLpFiUsageState based on Integer32"""
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


_MscLpFiUsageState_Type.__name__ = "Integer32"
_MscLpFiUsageState_Object = MibTableColumn
mscLpFiUsageState = _MscLpFiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 16, 1, 3),
    _MscLpFiUsageState_Type()
)
mscLpFiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiUsageState.setStatus("mandatory")
_MscLpFiOperStatusTable_Object = MibTable
mscLpFiOperStatusTable = _MscLpFiOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 17)
)
if mibBuilder.loadTexts:
    mscLpFiOperStatusTable.setStatus("mandatory")
_MscLpFiOperStatusEntry_Object = MibTableRow
mscLpFiOperStatusEntry = _MscLpFiOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 17, 1)
)
mscLpFiOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiOperStatusEntry.setStatus("mandatory")


class _MscLpFiSnmpOperStatus_Type(Integer32):
    """Custom type mscLpFiSnmpOperStatus based on Integer32"""
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


_MscLpFiSnmpOperStatus_Type.__name__ = "Integer32"
_MscLpFiSnmpOperStatus_Object = MibTableColumn
mscLpFiSnmpOperStatus = _MscLpFiSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 17, 1, 1),
    _MscLpFiSnmpOperStatus_Type()
)
mscLpFiSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiSnmpOperStatus.setStatus("mandatory")
_MscLpFiSmtOperTable_Object = MibTable
mscLpFiSmtOperTable = _MscLpFiSmtOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 18)
)
if mibBuilder.loadTexts:
    mscLpFiSmtOperTable.setStatus("mandatory")
_MscLpFiSmtOperEntry_Object = MibTableRow
mscLpFiSmtOperEntry = _MscLpFiSmtOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 18, 1)
)
mscLpFiSmtOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiSmtOperEntry.setStatus("mandatory")


class _MscLpFiVersion_Type(AsciiString):
    """Custom type mscLpFiVersion based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscLpFiVersion_Type.__name__ = "AsciiString"
_MscLpFiVersion_Object = MibTableColumn
mscLpFiVersion = _MscLpFiVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 18, 1, 1),
    _MscLpFiVersion_Type()
)
mscLpFiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiVersion.setStatus("mandatory")


class _MscLpFiBypassPresent_Type(Integer32):
    """Custom type mscLpFiBypassPresent based on Integer32"""
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


_MscLpFiBypassPresent_Type.__name__ = "Integer32"
_MscLpFiBypassPresent_Object = MibTableColumn
mscLpFiBypassPresent = _MscLpFiBypassPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 18, 1, 14),
    _MscLpFiBypassPresent_Type()
)
mscLpFiBypassPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiBypassPresent.setStatus("mandatory")


class _MscLpFiEcmState_Type(Integer32):
    """Custom type mscLpFiEcmState based on Integer32"""
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


_MscLpFiEcmState_Type.__name__ = "Integer32"
_MscLpFiEcmState_Object = MibTableColumn
mscLpFiEcmState = _MscLpFiEcmState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 18, 1, 15),
    _MscLpFiEcmState_Type()
)
mscLpFiEcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiEcmState.setStatus("mandatory")


class _MscLpFiCfState_Type(Integer32):
    """Custom type mscLpFiCfState based on Integer32"""
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


_MscLpFiCfState_Type.__name__ = "Integer32"
_MscLpFiCfState_Object = MibTableColumn
mscLpFiCfState = _MscLpFiCfState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 18, 1, 16),
    _MscLpFiCfState_Type()
)
mscLpFiCfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiCfState.setStatus("mandatory")
_MscLpFiMacOperTable_Object = MibTable
mscLpFiMacOperTable = _MscLpFiMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19)
)
if mibBuilder.loadTexts:
    mscLpFiMacOperTable.setStatus("mandatory")
_MscLpFiMacOperEntry_Object = MibTableRow
mscLpFiMacOperEntry = _MscLpFiMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1)
)
mscLpFiMacOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiMacOperEntry.setStatus("mandatory")


class _MscLpFiRingLatency_Type(Gauge32):
    """Custom type mscLpFiRingLatency based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 1342000000),
    )


_MscLpFiRingLatency_Type.__name__ = "Gauge32"
_MscLpFiRingLatency_Object = MibTableColumn
mscLpFiRingLatency = _MscLpFiRingLatency_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 1),
    _MscLpFiRingLatency_Type()
)
mscLpFiRingLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiRingLatency.setStatus("mandatory")


class _MscLpFiMacAddress_Type(FddiMACLongAddressType):
    """Custom type mscLpFiMacAddress based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiMacAddress_Type.__name__ = "FddiMACLongAddressType"
_MscLpFiMacAddress_Object = MibTableColumn
mscLpFiMacAddress = _MscLpFiMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 10),
    _MscLpFiMacAddress_Type()
)
mscLpFiMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiMacAddress.setStatus("mandatory")


class _MscLpFiUpstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type mscLpFiUpstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiUpstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_MscLpFiUpstreamNeighbor_Object = MibTableColumn
mscLpFiUpstreamNeighbor = _MscLpFiUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 11),
    _MscLpFiUpstreamNeighbor_Type()
)
mscLpFiUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiUpstreamNeighbor.setStatus("mandatory")


class _MscLpFiDownstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type mscLpFiDownstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiDownstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_MscLpFiDownstreamNeighbor_Object = MibTableColumn
mscLpFiDownstreamNeighbor = _MscLpFiDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 12),
    _MscLpFiDownstreamNeighbor_Type()
)
mscLpFiDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiDownstreamNeighbor.setStatus("mandatory")


class _MscLpFiOldUpstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type mscLpFiOldUpstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiOldUpstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_MscLpFiOldUpstreamNeighbor_Object = MibTableColumn
mscLpFiOldUpstreamNeighbor = _MscLpFiOldUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 13),
    _MscLpFiOldUpstreamNeighbor_Type()
)
mscLpFiOldUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiOldUpstreamNeighbor.setStatus("mandatory")


class _MscLpFiOldDownstreamNeighbor_Type(FddiMACLongAddressType):
    """Custom type mscLpFiOldDownstreamNeighbor based on FddiMACLongAddressType"""
    subtypeSpec = FddiMACLongAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiOldDownstreamNeighbor_Type.__name__ = "FddiMACLongAddressType"
_MscLpFiOldDownstreamNeighbor_Object = MibTableColumn
mscLpFiOldDownstreamNeighbor = _MscLpFiOldDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 14),
    _MscLpFiOldDownstreamNeighbor_Type()
)
mscLpFiOldDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiOldDownstreamNeighbor.setStatus("mandatory")


class _MscLpFiDupAddressTest_Type(Integer32):
    """Custom type mscLpFiDupAddressTest based on Integer32"""
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


_MscLpFiDupAddressTest_Type.__name__ = "Integer32"
_MscLpFiDupAddressTest_Object = MibTableColumn
mscLpFiDupAddressTest = _MscLpFiDupAddressTest_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 15),
    _MscLpFiDupAddressTest_Type()
)
mscLpFiDupAddressTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiDupAddressTest.setStatus("mandatory")


class _MscLpFiTokenNegotiatedTimer_Type(FddiTimeNano):
    """Custom type mscLpFiTokenNegotiatedTimer based on FddiTimeNano"""
    defaultValue = 167772000

    subtypeSpec = FddiTimeNano.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 1340000000),
    )


_MscLpFiTokenNegotiatedTimer_Type.__name__ = "FddiTimeNano"
_MscLpFiTokenNegotiatedTimer_Object = MibTableColumn
mscLpFiTokenNegotiatedTimer = _MscLpFiTokenNegotiatedTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 18),
    _MscLpFiTokenNegotiatedTimer_Type()
)
mscLpFiTokenNegotiatedTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTokenNegotiatedTimer.setStatus("mandatory")
_MscLpFiFrameCounts_Type = Counter32
_MscLpFiFrameCounts_Object = MibTableColumn
mscLpFiFrameCounts = _MscLpFiFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 19),
    _MscLpFiFrameCounts_Type()
)
mscLpFiFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiFrameCounts.setStatus("mandatory")
_MscLpFiCopiedCounts_Type = Counter32
_MscLpFiCopiedCounts_Object = MibTableColumn
mscLpFiCopiedCounts = _MscLpFiCopiedCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 20),
    _MscLpFiCopiedCounts_Type()
)
mscLpFiCopiedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiCopiedCounts.setStatus("mandatory")
_MscLpFiTransmitCounts_Type = Counter32
_MscLpFiTransmitCounts_Object = MibTableColumn
mscLpFiTransmitCounts = _MscLpFiTransmitCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 21),
    _MscLpFiTransmitCounts_Type()
)
mscLpFiTransmitCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTransmitCounts.setStatus("mandatory")
_MscLpFiErrorCounts_Type = Counter32
_MscLpFiErrorCounts_Object = MibTableColumn
mscLpFiErrorCounts = _MscLpFiErrorCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 22),
    _MscLpFiErrorCounts_Type()
)
mscLpFiErrorCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiErrorCounts.setStatus("mandatory")
_MscLpFiLostCounts_Type = Counter32
_MscLpFiLostCounts_Object = MibTableColumn
mscLpFiLostCounts = _MscLpFiLostCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 23),
    _MscLpFiLostCounts_Type()
)
mscLpFiLostCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLostCounts.setStatus("mandatory")


class _MscLpFiRmtState_Type(Integer32):
    """Custom type mscLpFiRmtState based on Integer32"""
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


_MscLpFiRmtState_Type.__name__ = "Integer32"
_MscLpFiRmtState_Object = MibTableColumn
mscLpFiRmtState = _MscLpFiRmtState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 25),
    _MscLpFiRmtState_Type()
)
mscLpFiRmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiRmtState.setStatus("mandatory")


class _MscLpFiFrameErrorFlag_Type(Integer32):
    """Custom type mscLpFiFrameErrorFlag based on Integer32"""
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


_MscLpFiFrameErrorFlag_Type.__name__ = "Integer32"
_MscLpFiFrameErrorFlag_Object = MibTableColumn
mscLpFiFrameErrorFlag = _MscLpFiFrameErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 19, 1, 28),
    _MscLpFiFrameErrorFlag_Type()
)
mscLpFiFrameErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiFrameErrorFlag.setStatus("mandatory")
_MscLpFiMacCOperTable_Object = MibTable
mscLpFiMacCOperTable = _MscLpFiMacCOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 20)
)
if mibBuilder.loadTexts:
    mscLpFiMacCOperTable.setStatus("mandatory")
_MscLpFiMacCOperEntry_Object = MibTableRow
mscLpFiMacCOperEntry = _MscLpFiMacCOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 20, 1)
)
mscLpFiMacCOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiMacCOperEntry.setStatus("mandatory")
_MscLpFiTokenCounts_Type = Counter32
_MscLpFiTokenCounts_Object = MibTableColumn
mscLpFiTokenCounts = _MscLpFiTokenCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 20, 1, 1),
    _MscLpFiTokenCounts_Type()
)
mscLpFiTokenCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTokenCounts.setStatus("mandatory")
_MscLpFiTvxExpiredCounts_Type = Counter32
_MscLpFiTvxExpiredCounts_Object = MibTableColumn
mscLpFiTvxExpiredCounts = _MscLpFiTvxExpiredCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 20, 1, 2),
    _MscLpFiTvxExpiredCounts_Type()
)
mscLpFiTvxExpiredCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiTvxExpiredCounts.setStatus("mandatory")
_MscLpFiNotCopiedCounts_Type = Counter32
_MscLpFiNotCopiedCounts_Object = MibTableColumn
mscLpFiNotCopiedCounts = _MscLpFiNotCopiedCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 20, 1, 3),
    _MscLpFiNotCopiedCounts_Type()
)
mscLpFiNotCopiedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiNotCopiedCounts.setStatus("mandatory")
_MscLpFiLateCounts_Type = Counter32
_MscLpFiLateCounts_Object = MibTableColumn
mscLpFiLateCounts = _MscLpFiLateCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 20, 1, 4),
    _MscLpFiLateCounts_Type()
)
mscLpFiLateCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiLateCounts.setStatus("mandatory")
_MscLpFiRingOpCounts_Type = Counter32
_MscLpFiRingOpCounts_Object = MibTableColumn
mscLpFiRingOpCounts = _MscLpFiRingOpCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 20, 1, 5),
    _MscLpFiRingOpCounts_Type()
)
mscLpFiRingOpCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiRingOpCounts.setStatus("mandatory")
_MscLpFiNcMacOperTable_Object = MibTable
mscLpFiNcMacOperTable = _MscLpFiNcMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 26)
)
if mibBuilder.loadTexts:
    mscLpFiNcMacOperTable.setStatus("mandatory")
_MscLpFiNcMacOperEntry_Object = MibTableRow
mscLpFiNcMacOperEntry = _MscLpFiNcMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 26, 1)
)
mscLpFiNcMacOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpFiIndex"),
)
if mibBuilder.loadTexts:
    mscLpFiNcMacOperEntry.setStatus("mandatory")


class _MscLpFiNcMacAddress_Type(MacAddress):
    """Custom type mscLpFiNcMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiNcMacAddress_Type.__name__ = "MacAddress"
_MscLpFiNcMacAddress_Object = MibTableColumn
mscLpFiNcMacAddress = _MscLpFiNcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 26, 1, 1),
    _MscLpFiNcMacAddress_Type()
)
mscLpFiNcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiNcMacAddress.setStatus("mandatory")


class _MscLpFiNcUpstreamNeighbor_Type(MacAddress):
    """Custom type mscLpFiNcUpstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiNcUpstreamNeighbor_Type.__name__ = "MacAddress"
_MscLpFiNcUpstreamNeighbor_Object = MibTableColumn
mscLpFiNcUpstreamNeighbor = _MscLpFiNcUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 26, 1, 2),
    _MscLpFiNcUpstreamNeighbor_Type()
)
mscLpFiNcUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiNcUpstreamNeighbor.setStatus("mandatory")


class _MscLpFiNcDownstreamNeighbor_Type(MacAddress):
    """Custom type mscLpFiNcDownstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiNcDownstreamNeighbor_Type.__name__ = "MacAddress"
_MscLpFiNcDownstreamNeighbor_Object = MibTableColumn
mscLpFiNcDownstreamNeighbor = _MscLpFiNcDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 26, 1, 3),
    _MscLpFiNcDownstreamNeighbor_Type()
)
mscLpFiNcDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiNcDownstreamNeighbor.setStatus("mandatory")


class _MscLpFiNcOldUpstreamNeighbor_Type(MacAddress):
    """Custom type mscLpFiNcOldUpstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiNcOldUpstreamNeighbor_Type.__name__ = "MacAddress"
_MscLpFiNcOldUpstreamNeighbor_Object = MibTableColumn
mscLpFiNcOldUpstreamNeighbor = _MscLpFiNcOldUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 26, 1, 4),
    _MscLpFiNcOldUpstreamNeighbor_Type()
)
mscLpFiNcOldUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiNcOldUpstreamNeighbor.setStatus("mandatory")


class _MscLpFiNcOldDownstreamNeighbor_Type(MacAddress):
    """Custom type mscLpFiNcOldDownstreamNeighbor based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpFiNcOldDownstreamNeighbor_Type.__name__ = "MacAddress"
_MscLpFiNcOldDownstreamNeighbor_Object = MibTableColumn
mscLpFiNcOldDownstreamNeighbor = _MscLpFiNcOldDownstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 4, 26, 1, 5),
    _MscLpFiNcOldDownstreamNeighbor_Type()
)
mscLpFiNcOldDownstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpFiNcOldDownstreamNeighbor.setStatus("mandatory")
_MscLpTr_ObjectIdentity = ObjectIdentity
mscLpTr = _MscLpTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13)
)
_MscLpTrRowStatusTable_Object = MibTable
mscLpTrRowStatusTable = _MscLpTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 1)
)
if mibBuilder.loadTexts:
    mscLpTrRowStatusTable.setStatus("mandatory")
_MscLpTrRowStatusEntry_Object = MibTableRow
mscLpTrRowStatusEntry = _MscLpTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 1, 1)
)
mscLpTrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrRowStatusEntry.setStatus("mandatory")
_MscLpTrRowStatus_Type = RowStatus
_MscLpTrRowStatus_Object = MibTableColumn
mscLpTrRowStatus = _MscLpTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 1, 1, 1),
    _MscLpTrRowStatus_Type()
)
mscLpTrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrRowStatus.setStatus("mandatory")
_MscLpTrComponentName_Type = DisplayString
_MscLpTrComponentName_Object = MibTableColumn
mscLpTrComponentName = _MscLpTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 1, 1, 2),
    _MscLpTrComponentName_Type()
)
mscLpTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrComponentName.setStatus("mandatory")
_MscLpTrStorageType_Type = StorageType
_MscLpTrStorageType_Object = MibTableColumn
mscLpTrStorageType = _MscLpTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 1, 1, 4),
    _MscLpTrStorageType_Type()
)
mscLpTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrStorageType.setStatus("mandatory")


class _MscLpTrIndex_Type(Integer32):
    """Custom type mscLpTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_MscLpTrIndex_Type.__name__ = "Integer32"
_MscLpTrIndex_Object = MibTableColumn
mscLpTrIndex = _MscLpTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 1, 1, 10),
    _MscLpTrIndex_Type()
)
mscLpTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrIndex.setStatus("mandatory")
_MscLpTrLt_ObjectIdentity = ObjectIdentity
mscLpTrLt = _MscLpTrLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2)
)
_MscLpTrLtRowStatusTable_Object = MibTable
mscLpTrLtRowStatusTable = _MscLpTrLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtRowStatusTable.setStatus("mandatory")
_MscLpTrLtRowStatusEntry_Object = MibTableRow
mscLpTrLtRowStatusEntry = _MscLpTrLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 1, 1)
)
mscLpTrLtRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtRowStatusEntry.setStatus("mandatory")
_MscLpTrLtRowStatus_Type = RowStatus
_MscLpTrLtRowStatus_Object = MibTableColumn
mscLpTrLtRowStatus = _MscLpTrLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 1, 1, 1),
    _MscLpTrLtRowStatus_Type()
)
mscLpTrLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtRowStatus.setStatus("mandatory")
_MscLpTrLtComponentName_Type = DisplayString
_MscLpTrLtComponentName_Object = MibTableColumn
mscLpTrLtComponentName = _MscLpTrLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 1, 1, 2),
    _MscLpTrLtComponentName_Type()
)
mscLpTrLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtComponentName.setStatus("mandatory")
_MscLpTrLtStorageType_Type = StorageType
_MscLpTrLtStorageType_Object = MibTableColumn
mscLpTrLtStorageType = _MscLpTrLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 1, 1, 4),
    _MscLpTrLtStorageType_Type()
)
mscLpTrLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtStorageType.setStatus("mandatory")
_MscLpTrLtIndex_Type = NonReplicated
_MscLpTrLtIndex_Object = MibTableColumn
mscLpTrLtIndex = _MscLpTrLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 1, 1, 10),
    _MscLpTrLtIndex_Type()
)
mscLpTrLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtIndex.setStatus("mandatory")
_MscLpTrLtFrmCmp_ObjectIdentity = ObjectIdentity
mscLpTrLtFrmCmp = _MscLpTrLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2)
)
_MscLpTrLtFrmCmpRowStatusTable_Object = MibTable
mscLpTrLtFrmCmpRowStatusTable = _MscLpTrLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpRowStatusTable.setStatus("mandatory")
_MscLpTrLtFrmCmpRowStatusEntry_Object = MibTableRow
mscLpTrLtFrmCmpRowStatusEntry = _MscLpTrLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 1, 1)
)
mscLpTrLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFrmCmpRowStatus_Type = RowStatus
_MscLpTrLtFrmCmpRowStatus_Object = MibTableColumn
mscLpTrLtFrmCmpRowStatus = _MscLpTrLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 1, 1, 1),
    _MscLpTrLtFrmCmpRowStatus_Type()
)
mscLpTrLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpRowStatus.setStatus("mandatory")
_MscLpTrLtFrmCmpComponentName_Type = DisplayString
_MscLpTrLtFrmCmpComponentName_Object = MibTableColumn
mscLpTrLtFrmCmpComponentName = _MscLpTrLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 1, 1, 2),
    _MscLpTrLtFrmCmpComponentName_Type()
)
mscLpTrLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpComponentName.setStatus("mandatory")
_MscLpTrLtFrmCmpStorageType_Type = StorageType
_MscLpTrLtFrmCmpStorageType_Object = MibTableColumn
mscLpTrLtFrmCmpStorageType = _MscLpTrLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 1, 1, 4),
    _MscLpTrLtFrmCmpStorageType_Type()
)
mscLpTrLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpStorageType.setStatus("mandatory")
_MscLpTrLtFrmCmpIndex_Type = NonReplicated
_MscLpTrLtFrmCmpIndex_Object = MibTableColumn
mscLpTrLtFrmCmpIndex = _MscLpTrLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 1, 1, 10),
    _MscLpTrLtFrmCmpIndex_Type()
)
mscLpTrLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpIndex.setStatus("mandatory")
_MscLpTrLtFrmCmpTopTable_Object = MibTable
mscLpTrLtFrmCmpTopTable = _MscLpTrLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpTopTable.setStatus("mandatory")
_MscLpTrLtFrmCmpTopEntry_Object = MibTableRow
mscLpTrLtFrmCmpTopEntry = _MscLpTrLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 10, 1)
)
mscLpTrLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpTopEntry.setStatus("mandatory")


class _MscLpTrLtFrmCmpTData_Type(AsciiString):
    """Custom type mscLpTrLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFrmCmpTData_Type.__name__ = "AsciiString"
_MscLpTrLtFrmCmpTData_Object = MibTableColumn
mscLpTrLtFrmCmpTData = _MscLpTrLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 2, 10, 1, 1),
    _MscLpTrLtFrmCmpTData_Type()
)
mscLpTrLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCmpTData.setStatus("mandatory")
_MscLpTrLtFrmCpy_ObjectIdentity = ObjectIdentity
mscLpTrLtFrmCpy = _MscLpTrLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3)
)
_MscLpTrLtFrmCpyRowStatusTable_Object = MibTable
mscLpTrLtFrmCpyRowStatusTable = _MscLpTrLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyRowStatusTable.setStatus("mandatory")
_MscLpTrLtFrmCpyRowStatusEntry_Object = MibTableRow
mscLpTrLtFrmCpyRowStatusEntry = _MscLpTrLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 1, 1)
)
mscLpTrLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFrmCpyRowStatus_Type = RowStatus
_MscLpTrLtFrmCpyRowStatus_Object = MibTableColumn
mscLpTrLtFrmCpyRowStatus = _MscLpTrLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 1, 1, 1),
    _MscLpTrLtFrmCpyRowStatus_Type()
)
mscLpTrLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyRowStatus.setStatus("mandatory")
_MscLpTrLtFrmCpyComponentName_Type = DisplayString
_MscLpTrLtFrmCpyComponentName_Object = MibTableColumn
mscLpTrLtFrmCpyComponentName = _MscLpTrLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 1, 1, 2),
    _MscLpTrLtFrmCpyComponentName_Type()
)
mscLpTrLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyComponentName.setStatus("mandatory")
_MscLpTrLtFrmCpyStorageType_Type = StorageType
_MscLpTrLtFrmCpyStorageType_Object = MibTableColumn
mscLpTrLtFrmCpyStorageType = _MscLpTrLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 1, 1, 4),
    _MscLpTrLtFrmCpyStorageType_Type()
)
mscLpTrLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyStorageType.setStatus("mandatory")
_MscLpTrLtFrmCpyIndex_Type = NonReplicated
_MscLpTrLtFrmCpyIndex_Object = MibTableColumn
mscLpTrLtFrmCpyIndex = _MscLpTrLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 1, 1, 10),
    _MscLpTrLtFrmCpyIndex_Type()
)
mscLpTrLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyIndex.setStatus("mandatory")
_MscLpTrLtFrmCpyTopTable_Object = MibTable
mscLpTrLtFrmCpyTopTable = _MscLpTrLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyTopTable.setStatus("mandatory")
_MscLpTrLtFrmCpyTopEntry_Object = MibTableRow
mscLpTrLtFrmCpyTopEntry = _MscLpTrLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 10, 1)
)
mscLpTrLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyTopEntry.setStatus("mandatory")


class _MscLpTrLtFrmCpyTData_Type(AsciiString):
    """Custom type mscLpTrLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFrmCpyTData_Type.__name__ = "AsciiString"
_MscLpTrLtFrmCpyTData_Object = MibTableColumn
mscLpTrLtFrmCpyTData = _MscLpTrLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 3, 10, 1, 1),
    _MscLpTrLtFrmCpyTData_Type()
)
mscLpTrLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFrmCpyTData.setStatus("mandatory")
_MscLpTrLtPrtCfg_ObjectIdentity = ObjectIdentity
mscLpTrLtPrtCfg = _MscLpTrLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4)
)
_MscLpTrLtPrtCfgRowStatusTable_Object = MibTable
mscLpTrLtPrtCfgRowStatusTable = _MscLpTrLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgRowStatusTable.setStatus("mandatory")
_MscLpTrLtPrtCfgRowStatusEntry_Object = MibTableRow
mscLpTrLtPrtCfgRowStatusEntry = _MscLpTrLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 1, 1)
)
mscLpTrLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgRowStatusEntry.setStatus("mandatory")
_MscLpTrLtPrtCfgRowStatus_Type = RowStatus
_MscLpTrLtPrtCfgRowStatus_Object = MibTableColumn
mscLpTrLtPrtCfgRowStatus = _MscLpTrLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 1, 1, 1),
    _MscLpTrLtPrtCfgRowStatus_Type()
)
mscLpTrLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgRowStatus.setStatus("mandatory")
_MscLpTrLtPrtCfgComponentName_Type = DisplayString
_MscLpTrLtPrtCfgComponentName_Object = MibTableColumn
mscLpTrLtPrtCfgComponentName = _MscLpTrLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 1, 1, 2),
    _MscLpTrLtPrtCfgComponentName_Type()
)
mscLpTrLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgComponentName.setStatus("mandatory")
_MscLpTrLtPrtCfgStorageType_Type = StorageType
_MscLpTrLtPrtCfgStorageType_Object = MibTableColumn
mscLpTrLtPrtCfgStorageType = _MscLpTrLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 1, 1, 4),
    _MscLpTrLtPrtCfgStorageType_Type()
)
mscLpTrLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgStorageType.setStatus("mandatory")
_MscLpTrLtPrtCfgIndex_Type = NonReplicated
_MscLpTrLtPrtCfgIndex_Object = MibTableColumn
mscLpTrLtPrtCfgIndex = _MscLpTrLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 1, 1, 10),
    _MscLpTrLtPrtCfgIndex_Type()
)
mscLpTrLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgIndex.setStatus("mandatory")
_MscLpTrLtPrtCfgTopTable_Object = MibTable
mscLpTrLtPrtCfgTopTable = _MscLpTrLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgTopTable.setStatus("mandatory")
_MscLpTrLtPrtCfgTopEntry_Object = MibTableRow
mscLpTrLtPrtCfgTopEntry = _MscLpTrLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 10, 1)
)
mscLpTrLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgTopEntry.setStatus("mandatory")


class _MscLpTrLtPrtCfgTData_Type(AsciiString):
    """Custom type mscLpTrLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtPrtCfgTData_Type.__name__ = "AsciiString"
_MscLpTrLtPrtCfgTData_Object = MibTableColumn
mscLpTrLtPrtCfgTData = _MscLpTrLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 4, 10, 1, 1),
    _MscLpTrLtPrtCfgTData_Type()
)
mscLpTrLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtPrtCfgTData.setStatus("mandatory")
_MscLpTrLtFb_ObjectIdentity = ObjectIdentity
mscLpTrLtFb = _MscLpTrLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5)
)
_MscLpTrLtFbRowStatusTable_Object = MibTable
mscLpTrLtFbRowStatusTable = _MscLpTrLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbRowStatusEntry_Object = MibTableRow
mscLpTrLtFbRowStatusEntry = _MscLpTrLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 1, 1)
)
mscLpTrLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbRowStatus_Type = RowStatus
_MscLpTrLtFbRowStatus_Object = MibTableColumn
mscLpTrLtFbRowStatus = _MscLpTrLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 1, 1, 1),
    _MscLpTrLtFbRowStatus_Type()
)
mscLpTrLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbRowStatus.setStatus("mandatory")
_MscLpTrLtFbComponentName_Type = DisplayString
_MscLpTrLtFbComponentName_Object = MibTableColumn
mscLpTrLtFbComponentName = _MscLpTrLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 1, 1, 2),
    _MscLpTrLtFbComponentName_Type()
)
mscLpTrLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbComponentName.setStatus("mandatory")
_MscLpTrLtFbStorageType_Type = StorageType
_MscLpTrLtFbStorageType_Object = MibTableColumn
mscLpTrLtFbStorageType = _MscLpTrLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 1, 1, 4),
    _MscLpTrLtFbStorageType_Type()
)
mscLpTrLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbStorageType.setStatus("mandatory")
_MscLpTrLtFbIndex_Type = NonReplicated
_MscLpTrLtFbIndex_Object = MibTableColumn
mscLpTrLtFbIndex = _MscLpTrLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 1, 1, 10),
    _MscLpTrLtFbIndex_Type()
)
mscLpTrLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbIndex.setStatus("mandatory")
_MscLpTrLtFbTxInfo_ObjectIdentity = ObjectIdentity
mscLpTrLtFbTxInfo = _MscLpTrLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2)
)
_MscLpTrLtFbTxInfoRowStatusTable_Object = MibTable
mscLpTrLtFbTxInfoRowStatusTable = _MscLpTrLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbTxInfoRowStatusEntry_Object = MibTableRow
mscLpTrLtFbTxInfoRowStatusEntry = _MscLpTrLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 1, 1)
)
mscLpTrLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbTxInfoRowStatus_Type = RowStatus
_MscLpTrLtFbTxInfoRowStatus_Object = MibTableColumn
mscLpTrLtFbTxInfoRowStatus = _MscLpTrLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 1, 1, 1),
    _MscLpTrLtFbTxInfoRowStatus_Type()
)
mscLpTrLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoRowStatus.setStatus("mandatory")
_MscLpTrLtFbTxInfoComponentName_Type = DisplayString
_MscLpTrLtFbTxInfoComponentName_Object = MibTableColumn
mscLpTrLtFbTxInfoComponentName = _MscLpTrLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 1, 1, 2),
    _MscLpTrLtFbTxInfoComponentName_Type()
)
mscLpTrLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoComponentName.setStatus("mandatory")
_MscLpTrLtFbTxInfoStorageType_Type = StorageType
_MscLpTrLtFbTxInfoStorageType_Object = MibTableColumn
mscLpTrLtFbTxInfoStorageType = _MscLpTrLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 1, 1, 4),
    _MscLpTrLtFbTxInfoStorageType_Type()
)
mscLpTrLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoStorageType.setStatus("mandatory")
_MscLpTrLtFbTxInfoIndex_Type = NonReplicated
_MscLpTrLtFbTxInfoIndex_Object = MibTableColumn
mscLpTrLtFbTxInfoIndex = _MscLpTrLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 1, 1, 10),
    _MscLpTrLtFbTxInfoIndex_Type()
)
mscLpTrLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoIndex.setStatus("mandatory")
_MscLpTrLtFbTxInfoTopTable_Object = MibTable
mscLpTrLtFbTxInfoTopTable = _MscLpTrLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoTopTable.setStatus("mandatory")
_MscLpTrLtFbTxInfoTopEntry_Object = MibTableRow
mscLpTrLtFbTxInfoTopEntry = _MscLpTrLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 10, 1)
)
mscLpTrLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoTopEntry.setStatus("mandatory")


class _MscLpTrLtFbTxInfoTData_Type(AsciiString):
    """Custom type mscLpTrLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbTxInfoTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbTxInfoTData_Object = MibTableColumn
mscLpTrLtFbTxInfoTData = _MscLpTrLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 2, 10, 1, 1),
    _MscLpTrLtFbTxInfoTData_Type()
)
mscLpTrLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbTxInfoTData.setStatus("mandatory")
_MscLpTrLtFbFddiMac_ObjectIdentity = ObjectIdentity
mscLpTrLtFbFddiMac = _MscLpTrLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3)
)
_MscLpTrLtFbFddiMacRowStatusTable_Object = MibTable
mscLpTrLtFbFddiMacRowStatusTable = _MscLpTrLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbFddiMacRowStatusEntry_Object = MibTableRow
mscLpTrLtFbFddiMacRowStatusEntry = _MscLpTrLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 1, 1)
)
mscLpTrLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbFddiMacRowStatus_Type = RowStatus
_MscLpTrLtFbFddiMacRowStatus_Object = MibTableColumn
mscLpTrLtFbFddiMacRowStatus = _MscLpTrLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 1, 1, 1),
    _MscLpTrLtFbFddiMacRowStatus_Type()
)
mscLpTrLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacRowStatus.setStatus("mandatory")
_MscLpTrLtFbFddiMacComponentName_Type = DisplayString
_MscLpTrLtFbFddiMacComponentName_Object = MibTableColumn
mscLpTrLtFbFddiMacComponentName = _MscLpTrLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 1, 1, 2),
    _MscLpTrLtFbFddiMacComponentName_Type()
)
mscLpTrLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacComponentName.setStatus("mandatory")
_MscLpTrLtFbFddiMacStorageType_Type = StorageType
_MscLpTrLtFbFddiMacStorageType_Object = MibTableColumn
mscLpTrLtFbFddiMacStorageType = _MscLpTrLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 1, 1, 4),
    _MscLpTrLtFbFddiMacStorageType_Type()
)
mscLpTrLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacStorageType.setStatus("mandatory")
_MscLpTrLtFbFddiMacIndex_Type = NonReplicated
_MscLpTrLtFbFddiMacIndex_Object = MibTableColumn
mscLpTrLtFbFddiMacIndex = _MscLpTrLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 1, 1, 10),
    _MscLpTrLtFbFddiMacIndex_Type()
)
mscLpTrLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacIndex.setStatus("mandatory")
_MscLpTrLtFbFddiMacTopTable_Object = MibTable
mscLpTrLtFbFddiMacTopTable = _MscLpTrLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacTopTable.setStatus("mandatory")
_MscLpTrLtFbFddiMacTopEntry_Object = MibTableRow
mscLpTrLtFbFddiMacTopEntry = _MscLpTrLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 10, 1)
)
mscLpTrLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacTopEntry.setStatus("mandatory")


class _MscLpTrLtFbFddiMacTData_Type(AsciiString):
    """Custom type mscLpTrLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbFddiMacTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbFddiMacTData_Object = MibTableColumn
mscLpTrLtFbFddiMacTData = _MscLpTrLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 3, 10, 1, 1),
    _MscLpTrLtFbFddiMacTData_Type()
)
mscLpTrLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbFddiMacTData.setStatus("mandatory")
_MscLpTrLtFbMacEnet_ObjectIdentity = ObjectIdentity
mscLpTrLtFbMacEnet = _MscLpTrLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4)
)
_MscLpTrLtFbMacEnetRowStatusTable_Object = MibTable
mscLpTrLtFbMacEnetRowStatusTable = _MscLpTrLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbMacEnetRowStatusEntry_Object = MibTableRow
mscLpTrLtFbMacEnetRowStatusEntry = _MscLpTrLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 1, 1)
)
mscLpTrLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbMacEnetRowStatus_Type = RowStatus
_MscLpTrLtFbMacEnetRowStatus_Object = MibTableColumn
mscLpTrLtFbMacEnetRowStatus = _MscLpTrLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 1, 1, 1),
    _MscLpTrLtFbMacEnetRowStatus_Type()
)
mscLpTrLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetRowStatus.setStatus("mandatory")
_MscLpTrLtFbMacEnetComponentName_Type = DisplayString
_MscLpTrLtFbMacEnetComponentName_Object = MibTableColumn
mscLpTrLtFbMacEnetComponentName = _MscLpTrLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 1, 1, 2),
    _MscLpTrLtFbMacEnetComponentName_Type()
)
mscLpTrLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetComponentName.setStatus("mandatory")
_MscLpTrLtFbMacEnetStorageType_Type = StorageType
_MscLpTrLtFbMacEnetStorageType_Object = MibTableColumn
mscLpTrLtFbMacEnetStorageType = _MscLpTrLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 1, 1, 4),
    _MscLpTrLtFbMacEnetStorageType_Type()
)
mscLpTrLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetStorageType.setStatus("mandatory")
_MscLpTrLtFbMacEnetIndex_Type = NonReplicated
_MscLpTrLtFbMacEnetIndex_Object = MibTableColumn
mscLpTrLtFbMacEnetIndex = _MscLpTrLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 1, 1, 10),
    _MscLpTrLtFbMacEnetIndex_Type()
)
mscLpTrLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetIndex.setStatus("mandatory")
_MscLpTrLtFbMacEnetTopTable_Object = MibTable
mscLpTrLtFbMacEnetTopTable = _MscLpTrLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetTopTable.setStatus("mandatory")
_MscLpTrLtFbMacEnetTopEntry_Object = MibTableRow
mscLpTrLtFbMacEnetTopEntry = _MscLpTrLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 10, 1)
)
mscLpTrLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetTopEntry.setStatus("mandatory")


class _MscLpTrLtFbMacEnetTData_Type(AsciiString):
    """Custom type mscLpTrLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbMacEnetTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbMacEnetTData_Object = MibTableColumn
mscLpTrLtFbMacEnetTData = _MscLpTrLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 4, 10, 1, 1),
    _MscLpTrLtFbMacEnetTData_Type()
)
mscLpTrLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacEnetTData.setStatus("mandatory")
_MscLpTrLtFbMacTr_ObjectIdentity = ObjectIdentity
mscLpTrLtFbMacTr = _MscLpTrLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5)
)
_MscLpTrLtFbMacTrRowStatusTable_Object = MibTable
mscLpTrLtFbMacTrRowStatusTable = _MscLpTrLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbMacTrRowStatusEntry_Object = MibTableRow
mscLpTrLtFbMacTrRowStatusEntry = _MscLpTrLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 1, 1)
)
mscLpTrLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbMacTrRowStatus_Type = RowStatus
_MscLpTrLtFbMacTrRowStatus_Object = MibTableColumn
mscLpTrLtFbMacTrRowStatus = _MscLpTrLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 1, 1, 1),
    _MscLpTrLtFbMacTrRowStatus_Type()
)
mscLpTrLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrRowStatus.setStatus("mandatory")
_MscLpTrLtFbMacTrComponentName_Type = DisplayString
_MscLpTrLtFbMacTrComponentName_Object = MibTableColumn
mscLpTrLtFbMacTrComponentName = _MscLpTrLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 1, 1, 2),
    _MscLpTrLtFbMacTrComponentName_Type()
)
mscLpTrLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrComponentName.setStatus("mandatory")
_MscLpTrLtFbMacTrStorageType_Type = StorageType
_MscLpTrLtFbMacTrStorageType_Object = MibTableColumn
mscLpTrLtFbMacTrStorageType = _MscLpTrLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 1, 1, 4),
    _MscLpTrLtFbMacTrStorageType_Type()
)
mscLpTrLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrStorageType.setStatus("mandatory")
_MscLpTrLtFbMacTrIndex_Type = NonReplicated
_MscLpTrLtFbMacTrIndex_Object = MibTableColumn
mscLpTrLtFbMacTrIndex = _MscLpTrLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 1, 1, 10),
    _MscLpTrLtFbMacTrIndex_Type()
)
mscLpTrLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrIndex.setStatus("mandatory")
_MscLpTrLtFbMacTrTopTable_Object = MibTable
mscLpTrLtFbMacTrTopTable = _MscLpTrLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrTopTable.setStatus("mandatory")
_MscLpTrLtFbMacTrTopEntry_Object = MibTableRow
mscLpTrLtFbMacTrTopEntry = _MscLpTrLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 10, 1)
)
mscLpTrLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrTopEntry.setStatus("mandatory")


class _MscLpTrLtFbMacTrTData_Type(AsciiString):
    """Custom type mscLpTrLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbMacTrTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbMacTrTData_Object = MibTableColumn
mscLpTrLtFbMacTrTData = _MscLpTrLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 5, 10, 1, 1),
    _MscLpTrLtFbMacTrTData_Type()
)
mscLpTrLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbMacTrTData.setStatus("mandatory")
_MscLpTrLtFbData_ObjectIdentity = ObjectIdentity
mscLpTrLtFbData = _MscLpTrLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6)
)
_MscLpTrLtFbDataRowStatusTable_Object = MibTable
mscLpTrLtFbDataRowStatusTable = _MscLpTrLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbDataRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbDataRowStatusEntry_Object = MibTableRow
mscLpTrLtFbDataRowStatusEntry = _MscLpTrLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 1, 1)
)
mscLpTrLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbDataRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbDataRowStatus_Type = RowStatus
_MscLpTrLtFbDataRowStatus_Object = MibTableColumn
mscLpTrLtFbDataRowStatus = _MscLpTrLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 1, 1, 1),
    _MscLpTrLtFbDataRowStatus_Type()
)
mscLpTrLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbDataRowStatus.setStatus("mandatory")
_MscLpTrLtFbDataComponentName_Type = DisplayString
_MscLpTrLtFbDataComponentName_Object = MibTableColumn
mscLpTrLtFbDataComponentName = _MscLpTrLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 1, 1, 2),
    _MscLpTrLtFbDataComponentName_Type()
)
mscLpTrLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbDataComponentName.setStatus("mandatory")
_MscLpTrLtFbDataStorageType_Type = StorageType
_MscLpTrLtFbDataStorageType_Object = MibTableColumn
mscLpTrLtFbDataStorageType = _MscLpTrLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 1, 1, 4),
    _MscLpTrLtFbDataStorageType_Type()
)
mscLpTrLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbDataStorageType.setStatus("mandatory")
_MscLpTrLtFbDataIndex_Type = NonReplicated
_MscLpTrLtFbDataIndex_Object = MibTableColumn
mscLpTrLtFbDataIndex = _MscLpTrLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 1, 1, 10),
    _MscLpTrLtFbDataIndex_Type()
)
mscLpTrLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbDataIndex.setStatus("mandatory")
_MscLpTrLtFbDataTopTable_Object = MibTable
mscLpTrLtFbDataTopTable = _MscLpTrLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbDataTopTable.setStatus("mandatory")
_MscLpTrLtFbDataTopEntry_Object = MibTableRow
mscLpTrLtFbDataTopEntry = _MscLpTrLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 10, 1)
)
mscLpTrLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbDataTopEntry.setStatus("mandatory")


class _MscLpTrLtFbDataTData_Type(AsciiString):
    """Custom type mscLpTrLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbDataTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbDataTData_Object = MibTableColumn
mscLpTrLtFbDataTData = _MscLpTrLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 6, 10, 1, 1),
    _MscLpTrLtFbDataTData_Type()
)
mscLpTrLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbDataTData.setStatus("mandatory")
_MscLpTrLtFbIpH_ObjectIdentity = ObjectIdentity
mscLpTrLtFbIpH = _MscLpTrLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7)
)
_MscLpTrLtFbIpHRowStatusTable_Object = MibTable
mscLpTrLtFbIpHRowStatusTable = _MscLpTrLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbIpHRowStatusEntry_Object = MibTableRow
mscLpTrLtFbIpHRowStatusEntry = _MscLpTrLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 1, 1)
)
mscLpTrLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbIpHRowStatus_Type = RowStatus
_MscLpTrLtFbIpHRowStatus_Object = MibTableColumn
mscLpTrLtFbIpHRowStatus = _MscLpTrLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 1, 1, 1),
    _MscLpTrLtFbIpHRowStatus_Type()
)
mscLpTrLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHRowStatus.setStatus("mandatory")
_MscLpTrLtFbIpHComponentName_Type = DisplayString
_MscLpTrLtFbIpHComponentName_Object = MibTableColumn
mscLpTrLtFbIpHComponentName = _MscLpTrLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 1, 1, 2),
    _MscLpTrLtFbIpHComponentName_Type()
)
mscLpTrLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHComponentName.setStatus("mandatory")
_MscLpTrLtFbIpHStorageType_Type = StorageType
_MscLpTrLtFbIpHStorageType_Object = MibTableColumn
mscLpTrLtFbIpHStorageType = _MscLpTrLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 1, 1, 4),
    _MscLpTrLtFbIpHStorageType_Type()
)
mscLpTrLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHStorageType.setStatus("mandatory")
_MscLpTrLtFbIpHIndex_Type = NonReplicated
_MscLpTrLtFbIpHIndex_Object = MibTableColumn
mscLpTrLtFbIpHIndex = _MscLpTrLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 1, 1, 10),
    _MscLpTrLtFbIpHIndex_Type()
)
mscLpTrLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHIndex.setStatus("mandatory")
_MscLpTrLtFbIpHTopTable_Object = MibTable
mscLpTrLtFbIpHTopTable = _MscLpTrLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHTopTable.setStatus("mandatory")
_MscLpTrLtFbIpHTopEntry_Object = MibTableRow
mscLpTrLtFbIpHTopEntry = _MscLpTrLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 10, 1)
)
mscLpTrLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHTopEntry.setStatus("mandatory")


class _MscLpTrLtFbIpHTData_Type(AsciiString):
    """Custom type mscLpTrLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbIpHTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbIpHTData_Object = MibTableColumn
mscLpTrLtFbIpHTData = _MscLpTrLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 7, 10, 1, 1),
    _MscLpTrLtFbIpHTData_Type()
)
mscLpTrLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpHTData.setStatus("mandatory")
_MscLpTrLtFbLlch_ObjectIdentity = ObjectIdentity
mscLpTrLtFbLlch = _MscLpTrLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8)
)
_MscLpTrLtFbLlchRowStatusTable_Object = MibTable
mscLpTrLtFbLlchRowStatusTable = _MscLpTrLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbLlchRowStatusEntry_Object = MibTableRow
mscLpTrLtFbLlchRowStatusEntry = _MscLpTrLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 1, 1)
)
mscLpTrLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbLlchRowStatus_Type = RowStatus
_MscLpTrLtFbLlchRowStatus_Object = MibTableColumn
mscLpTrLtFbLlchRowStatus = _MscLpTrLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 1, 1, 1),
    _MscLpTrLtFbLlchRowStatus_Type()
)
mscLpTrLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchRowStatus.setStatus("mandatory")
_MscLpTrLtFbLlchComponentName_Type = DisplayString
_MscLpTrLtFbLlchComponentName_Object = MibTableColumn
mscLpTrLtFbLlchComponentName = _MscLpTrLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 1, 1, 2),
    _MscLpTrLtFbLlchComponentName_Type()
)
mscLpTrLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchComponentName.setStatus("mandatory")
_MscLpTrLtFbLlchStorageType_Type = StorageType
_MscLpTrLtFbLlchStorageType_Object = MibTableColumn
mscLpTrLtFbLlchStorageType = _MscLpTrLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 1, 1, 4),
    _MscLpTrLtFbLlchStorageType_Type()
)
mscLpTrLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchStorageType.setStatus("mandatory")
_MscLpTrLtFbLlchIndex_Type = NonReplicated
_MscLpTrLtFbLlchIndex_Object = MibTableColumn
mscLpTrLtFbLlchIndex = _MscLpTrLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 1, 1, 10),
    _MscLpTrLtFbLlchIndex_Type()
)
mscLpTrLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchIndex.setStatus("mandatory")
_MscLpTrLtFbLlchTopTable_Object = MibTable
mscLpTrLtFbLlchTopTable = _MscLpTrLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchTopTable.setStatus("mandatory")
_MscLpTrLtFbLlchTopEntry_Object = MibTableRow
mscLpTrLtFbLlchTopEntry = _MscLpTrLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 10, 1)
)
mscLpTrLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchTopEntry.setStatus("mandatory")


class _MscLpTrLtFbLlchTData_Type(AsciiString):
    """Custom type mscLpTrLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbLlchTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbLlchTData_Object = MibTableColumn
mscLpTrLtFbLlchTData = _MscLpTrLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 8, 10, 1, 1),
    _MscLpTrLtFbLlchTData_Type()
)
mscLpTrLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbLlchTData.setStatus("mandatory")
_MscLpTrLtFbAppleH_ObjectIdentity = ObjectIdentity
mscLpTrLtFbAppleH = _MscLpTrLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9)
)
_MscLpTrLtFbAppleHRowStatusTable_Object = MibTable
mscLpTrLtFbAppleHRowStatusTable = _MscLpTrLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbAppleHRowStatusEntry_Object = MibTableRow
mscLpTrLtFbAppleHRowStatusEntry = _MscLpTrLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 1, 1)
)
mscLpTrLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbAppleHRowStatus_Type = RowStatus
_MscLpTrLtFbAppleHRowStatus_Object = MibTableColumn
mscLpTrLtFbAppleHRowStatus = _MscLpTrLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 1, 1, 1),
    _MscLpTrLtFbAppleHRowStatus_Type()
)
mscLpTrLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHRowStatus.setStatus("mandatory")
_MscLpTrLtFbAppleHComponentName_Type = DisplayString
_MscLpTrLtFbAppleHComponentName_Object = MibTableColumn
mscLpTrLtFbAppleHComponentName = _MscLpTrLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 1, 1, 2),
    _MscLpTrLtFbAppleHComponentName_Type()
)
mscLpTrLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHComponentName.setStatus("mandatory")
_MscLpTrLtFbAppleHStorageType_Type = StorageType
_MscLpTrLtFbAppleHStorageType_Object = MibTableColumn
mscLpTrLtFbAppleHStorageType = _MscLpTrLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 1, 1, 4),
    _MscLpTrLtFbAppleHStorageType_Type()
)
mscLpTrLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHStorageType.setStatus("mandatory")
_MscLpTrLtFbAppleHIndex_Type = NonReplicated
_MscLpTrLtFbAppleHIndex_Object = MibTableColumn
mscLpTrLtFbAppleHIndex = _MscLpTrLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 1, 1, 10),
    _MscLpTrLtFbAppleHIndex_Type()
)
mscLpTrLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHIndex.setStatus("mandatory")
_MscLpTrLtFbAppleHTopTable_Object = MibTable
mscLpTrLtFbAppleHTopTable = _MscLpTrLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHTopTable.setStatus("mandatory")
_MscLpTrLtFbAppleHTopEntry_Object = MibTableRow
mscLpTrLtFbAppleHTopEntry = _MscLpTrLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 10, 1)
)
mscLpTrLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHTopEntry.setStatus("mandatory")


class _MscLpTrLtFbAppleHTData_Type(AsciiString):
    """Custom type mscLpTrLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbAppleHTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbAppleHTData_Object = MibTableColumn
mscLpTrLtFbAppleHTData = _MscLpTrLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 9, 10, 1, 1),
    _MscLpTrLtFbAppleHTData_Type()
)
mscLpTrLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbAppleHTData.setStatus("mandatory")
_MscLpTrLtFbIpxH_ObjectIdentity = ObjectIdentity
mscLpTrLtFbIpxH = _MscLpTrLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10)
)
_MscLpTrLtFbIpxHRowStatusTable_Object = MibTable
mscLpTrLtFbIpxHRowStatusTable = _MscLpTrLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHRowStatusTable.setStatus("mandatory")
_MscLpTrLtFbIpxHRowStatusEntry_Object = MibTableRow
mscLpTrLtFbIpxHRowStatusEntry = _MscLpTrLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 1, 1)
)
mscLpTrLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHRowStatusEntry.setStatus("mandatory")
_MscLpTrLtFbIpxHRowStatus_Type = RowStatus
_MscLpTrLtFbIpxHRowStatus_Object = MibTableColumn
mscLpTrLtFbIpxHRowStatus = _MscLpTrLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 1, 1, 1),
    _MscLpTrLtFbIpxHRowStatus_Type()
)
mscLpTrLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHRowStatus.setStatus("mandatory")
_MscLpTrLtFbIpxHComponentName_Type = DisplayString
_MscLpTrLtFbIpxHComponentName_Object = MibTableColumn
mscLpTrLtFbIpxHComponentName = _MscLpTrLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 1, 1, 2),
    _MscLpTrLtFbIpxHComponentName_Type()
)
mscLpTrLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHComponentName.setStatus("mandatory")
_MscLpTrLtFbIpxHStorageType_Type = StorageType
_MscLpTrLtFbIpxHStorageType_Object = MibTableColumn
mscLpTrLtFbIpxHStorageType = _MscLpTrLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 1, 1, 4),
    _MscLpTrLtFbIpxHStorageType_Type()
)
mscLpTrLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHStorageType.setStatus("mandatory")
_MscLpTrLtFbIpxHIndex_Type = NonReplicated
_MscLpTrLtFbIpxHIndex_Object = MibTableColumn
mscLpTrLtFbIpxHIndex = _MscLpTrLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 1, 1, 10),
    _MscLpTrLtFbIpxHIndex_Type()
)
mscLpTrLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHIndex.setStatus("mandatory")
_MscLpTrLtFbIpxHTopTable_Object = MibTable
mscLpTrLtFbIpxHTopTable = _MscLpTrLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHTopTable.setStatus("mandatory")
_MscLpTrLtFbIpxHTopEntry_Object = MibTableRow
mscLpTrLtFbIpxHTopEntry = _MscLpTrLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 10, 1)
)
mscLpTrLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHTopEntry.setStatus("mandatory")


class _MscLpTrLtFbIpxHTData_Type(AsciiString):
    """Custom type mscLpTrLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbIpxHTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbIpxHTData_Object = MibTableColumn
mscLpTrLtFbIpxHTData = _MscLpTrLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 10, 10, 1, 1),
    _MscLpTrLtFbIpxHTData_Type()
)
mscLpTrLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbIpxHTData.setStatus("mandatory")
_MscLpTrLtFbTopTable_Object = MibTable
mscLpTrLtFbTopTable = _MscLpTrLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 20)
)
if mibBuilder.loadTexts:
    mscLpTrLtFbTopTable.setStatus("mandatory")
_MscLpTrLtFbTopEntry_Object = MibTableRow
mscLpTrLtFbTopEntry = _MscLpTrLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 20, 1)
)
mscLpTrLtFbTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtFbTopEntry.setStatus("mandatory")


class _MscLpTrLtFbTData_Type(AsciiString):
    """Custom type mscLpTrLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtFbTData_Type.__name__ = "AsciiString"
_MscLpTrLtFbTData_Object = MibTableColumn
mscLpTrLtFbTData = _MscLpTrLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 5, 20, 1, 1),
    _MscLpTrLtFbTData_Type()
)
mscLpTrLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtFbTData.setStatus("mandatory")
_MscLpTrLtCntl_ObjectIdentity = ObjectIdentity
mscLpTrLtCntl = _MscLpTrLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6)
)
_MscLpTrLtCntlRowStatusTable_Object = MibTable
mscLpTrLtCntlRowStatusTable = _MscLpTrLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpTrLtCntlRowStatusTable.setStatus("mandatory")
_MscLpTrLtCntlRowStatusEntry_Object = MibTableRow
mscLpTrLtCntlRowStatusEntry = _MscLpTrLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 1, 1)
)
mscLpTrLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtCntlRowStatusEntry.setStatus("mandatory")
_MscLpTrLtCntlRowStatus_Type = RowStatus
_MscLpTrLtCntlRowStatus_Object = MibTableColumn
mscLpTrLtCntlRowStatus = _MscLpTrLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 1, 1, 1),
    _MscLpTrLtCntlRowStatus_Type()
)
mscLpTrLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtCntlRowStatus.setStatus("mandatory")
_MscLpTrLtCntlComponentName_Type = DisplayString
_MscLpTrLtCntlComponentName_Object = MibTableColumn
mscLpTrLtCntlComponentName = _MscLpTrLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 1, 1, 2),
    _MscLpTrLtCntlComponentName_Type()
)
mscLpTrLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtCntlComponentName.setStatus("mandatory")
_MscLpTrLtCntlStorageType_Type = StorageType
_MscLpTrLtCntlStorageType_Object = MibTableColumn
mscLpTrLtCntlStorageType = _MscLpTrLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 1, 1, 4),
    _MscLpTrLtCntlStorageType_Type()
)
mscLpTrLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLtCntlStorageType.setStatus("mandatory")
_MscLpTrLtCntlIndex_Type = NonReplicated
_MscLpTrLtCntlIndex_Object = MibTableColumn
mscLpTrLtCntlIndex = _MscLpTrLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 1, 1, 10),
    _MscLpTrLtCntlIndex_Type()
)
mscLpTrLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrLtCntlIndex.setStatus("mandatory")
_MscLpTrLtCntlTopTable_Object = MibTable
mscLpTrLtCntlTopTable = _MscLpTrLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpTrLtCntlTopTable.setStatus("mandatory")
_MscLpTrLtCntlTopEntry_Object = MibTableRow
mscLpTrLtCntlTopEntry = _MscLpTrLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 10, 1)
)
mscLpTrLtCntlTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtCntlTopEntry.setStatus("mandatory")


class _MscLpTrLtCntlTData_Type(AsciiString):
    """Custom type mscLpTrLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtCntlTData_Type.__name__ = "AsciiString"
_MscLpTrLtCntlTData_Object = MibTableColumn
mscLpTrLtCntlTData = _MscLpTrLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 6, 10, 1, 1),
    _MscLpTrLtCntlTData_Type()
)
mscLpTrLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtCntlTData.setStatus("mandatory")
_MscLpTrLtTopTable_Object = MibTable
mscLpTrLtTopTable = _MscLpTrLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 20)
)
if mibBuilder.loadTexts:
    mscLpTrLtTopTable.setStatus("mandatory")
_MscLpTrLtTopEntry_Object = MibTableRow
mscLpTrLtTopEntry = _MscLpTrLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 20, 1)
)
mscLpTrLtTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrLtTopEntry.setStatus("mandatory")


class _MscLpTrLtTData_Type(AsciiString):
    """Custom type mscLpTrLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpTrLtTData_Type.__name__ = "AsciiString"
_MscLpTrLtTData_Object = MibTableColumn
mscLpTrLtTData = _MscLpTrLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 2, 20, 1, 1),
    _MscLpTrLtTData_Type()
)
mscLpTrLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrLtTData.setStatus("mandatory")
_MscLpTrTest_ObjectIdentity = ObjectIdentity
mscLpTrTest = _MscLpTrTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5)
)
_MscLpTrTestRowStatusTable_Object = MibTable
mscLpTrTestRowStatusTable = _MscLpTrTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpTrTestRowStatusTable.setStatus("mandatory")
_MscLpTrTestRowStatusEntry_Object = MibTableRow
mscLpTrTestRowStatusEntry = _MscLpTrTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 1, 1)
)
mscLpTrTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrTestRowStatusEntry.setStatus("mandatory")
_MscLpTrTestRowStatus_Type = RowStatus
_MscLpTrTestRowStatus_Object = MibTableColumn
mscLpTrTestRowStatus = _MscLpTrTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 1, 1, 1),
    _MscLpTrTestRowStatus_Type()
)
mscLpTrTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestRowStatus.setStatus("mandatory")
_MscLpTrTestComponentName_Type = DisplayString
_MscLpTrTestComponentName_Object = MibTableColumn
mscLpTrTestComponentName = _MscLpTrTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 1, 1, 2),
    _MscLpTrTestComponentName_Type()
)
mscLpTrTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestComponentName.setStatus("mandatory")
_MscLpTrTestStorageType_Type = StorageType
_MscLpTrTestStorageType_Object = MibTableColumn
mscLpTrTestStorageType = _MscLpTrTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 1, 1, 4),
    _MscLpTrTestStorageType_Type()
)
mscLpTrTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestStorageType.setStatus("mandatory")
_MscLpTrTestIndex_Type = NonReplicated
_MscLpTrTestIndex_Object = MibTableColumn
mscLpTrTestIndex = _MscLpTrTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 1, 1, 10),
    _MscLpTrTestIndex_Type()
)
mscLpTrTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpTrTestIndex.setStatus("mandatory")
_MscLpTrTestPTOTable_Object = MibTable
mscLpTrTestPTOTable = _MscLpTrTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpTrTestPTOTable.setStatus("mandatory")
_MscLpTrTestPTOEntry_Object = MibTableRow
mscLpTrTestPTOEntry = _MscLpTrTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 10, 1)
)
mscLpTrTestPTOEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrTestPTOEntry.setStatus("mandatory")


class _MscLpTrTestType_Type(Integer32):
    """Custom type mscLpTrTestType based on Integer32"""
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


_MscLpTrTestType_Type.__name__ = "Integer32"
_MscLpTrTestType_Object = MibTableColumn
mscLpTrTestType = _MscLpTrTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 10, 1, 1),
    _MscLpTrTestType_Type()
)
mscLpTrTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrTestType.setStatus("mandatory")


class _MscLpTrTestFrmSize_Type(Unsigned32):
    """Custom type mscLpTrTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscLpTrTestFrmSize_Type.__name__ = "Unsigned32"
_MscLpTrTestFrmSize_Object = MibTableColumn
mscLpTrTestFrmSize = _MscLpTrTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 10, 1, 2),
    _MscLpTrTestFrmSize_Type()
)
mscLpTrTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrTestFrmSize.setStatus("mandatory")


class _MscLpTrTestDuration_Type(Unsigned32):
    """Custom type mscLpTrTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscLpTrTestDuration_Type.__name__ = "Unsigned32"
_MscLpTrTestDuration_Object = MibTableColumn
mscLpTrTestDuration = _MscLpTrTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 10, 1, 3),
    _MscLpTrTestDuration_Type()
)
mscLpTrTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrTestDuration.setStatus("mandatory")
_MscLpTrTestResultsTable_Object = MibTable
mscLpTrTestResultsTable = _MscLpTrTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11)
)
if mibBuilder.loadTexts:
    mscLpTrTestResultsTable.setStatus("mandatory")
_MscLpTrTestResultsEntry_Object = MibTableRow
mscLpTrTestResultsEntry = _MscLpTrTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1)
)
mscLpTrTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrTestResultsEntry.setStatus("mandatory")
_MscLpTrTestElapsedTime_Type = Counter32
_MscLpTrTestElapsedTime_Object = MibTableColumn
mscLpTrTestElapsedTime = _MscLpTrTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 4),
    _MscLpTrTestElapsedTime_Type()
)
mscLpTrTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestElapsedTime.setStatus("mandatory")


class _MscLpTrTestTimeRemaining_Type(Unsigned32):
    """Custom type mscLpTrTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpTrTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscLpTrTestTimeRemaining_Object = MibTableColumn
mscLpTrTestTimeRemaining = _MscLpTrTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 5),
    _MscLpTrTestTimeRemaining_Type()
)
mscLpTrTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestTimeRemaining.setStatus("mandatory")


class _MscLpTrTestCauseOfTermination_Type(Integer32):
    """Custom type mscLpTrTestCauseOfTermination based on Integer32"""
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


_MscLpTrTestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpTrTestCauseOfTermination_Object = MibTableColumn
mscLpTrTestCauseOfTermination = _MscLpTrTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 6),
    _MscLpTrTestCauseOfTermination_Type()
)
mscLpTrTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestCauseOfTermination.setStatus("mandatory")
_MscLpTrTestFrmTx_Type = PassportCounter64
_MscLpTrTestFrmTx_Object = MibTableColumn
mscLpTrTestFrmTx = _MscLpTrTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 7),
    _MscLpTrTestFrmTx_Type()
)
mscLpTrTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestFrmTx.setStatus("mandatory")
_MscLpTrTestBitsTx_Type = PassportCounter64
_MscLpTrTestBitsTx_Object = MibTableColumn
mscLpTrTestBitsTx = _MscLpTrTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 8),
    _MscLpTrTestBitsTx_Type()
)
mscLpTrTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestBitsTx.setStatus("mandatory")
_MscLpTrTestFrmRx_Type = PassportCounter64
_MscLpTrTestFrmRx_Object = MibTableColumn
mscLpTrTestFrmRx = _MscLpTrTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 9),
    _MscLpTrTestFrmRx_Type()
)
mscLpTrTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestFrmRx.setStatus("mandatory")
_MscLpTrTestBitsRx_Type = PassportCounter64
_MscLpTrTestBitsRx_Object = MibTableColumn
mscLpTrTestBitsRx = _MscLpTrTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 10),
    _MscLpTrTestBitsRx_Type()
)
mscLpTrTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestBitsRx.setStatus("mandatory")
_MscLpTrTestErroredFrmRx_Type = PassportCounter64
_MscLpTrTestErroredFrmRx_Object = MibTableColumn
mscLpTrTestErroredFrmRx = _MscLpTrTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 5, 11, 1, 11),
    _MscLpTrTestErroredFrmRx_Type()
)
mscLpTrTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTestErroredFrmRx.setStatus("mandatory")
_MscLpTrCidDataTable_Object = MibTable
mscLpTrCidDataTable = _MscLpTrCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 10)
)
if mibBuilder.loadTexts:
    mscLpTrCidDataTable.setStatus("mandatory")
_MscLpTrCidDataEntry_Object = MibTableRow
mscLpTrCidDataEntry = _MscLpTrCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 10, 1)
)
mscLpTrCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrCidDataEntry.setStatus("mandatory")


class _MscLpTrCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLpTrCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLpTrCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLpTrCustomerIdentifier_Object = MibTableColumn
mscLpTrCustomerIdentifier = _MscLpTrCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 10, 1, 1),
    _MscLpTrCustomerIdentifier_Type()
)
mscLpTrCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrCustomerIdentifier.setStatus("mandatory")
_MscLpTrIfEntryTable_Object = MibTable
mscLpTrIfEntryTable = _MscLpTrIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 11)
)
if mibBuilder.loadTexts:
    mscLpTrIfEntryTable.setStatus("mandatory")
_MscLpTrIfEntryEntry_Object = MibTableRow
mscLpTrIfEntryEntry = _MscLpTrIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 11, 1)
)
mscLpTrIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrIfEntryEntry.setStatus("mandatory")


class _MscLpTrIfAdminStatus_Type(Integer32):
    """Custom type mscLpTrIfAdminStatus based on Integer32"""
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


_MscLpTrIfAdminStatus_Type.__name__ = "Integer32"
_MscLpTrIfAdminStatus_Object = MibTableColumn
mscLpTrIfAdminStatus = _MscLpTrIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 11, 1, 1),
    _MscLpTrIfAdminStatus_Type()
)
mscLpTrIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrIfAdminStatus.setStatus("mandatory")


class _MscLpTrIfIndex_Type(InterfaceIndex):
    """Custom type mscLpTrIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLpTrIfIndex_Type.__name__ = "InterfaceIndex"
_MscLpTrIfIndex_Object = MibTableColumn
mscLpTrIfIndex = _MscLpTrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 11, 1, 2),
    _MscLpTrIfIndex_Type()
)
mscLpTrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrIfIndex.setStatus("mandatory")
_MscLpTrProvTable_Object = MibTable
mscLpTrProvTable = _MscLpTrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12)
)
if mibBuilder.loadTexts:
    mscLpTrProvTable.setStatus("mandatory")
_MscLpTrProvEntry_Object = MibTableRow
mscLpTrProvEntry = _MscLpTrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1)
)
mscLpTrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrProvEntry.setStatus("mandatory")


class _MscLpTrRingSpeed_Type(Integer32):
    """Custom type mscLpTrRingSpeed based on Integer32"""
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


_MscLpTrRingSpeed_Type.__name__ = "Integer32"
_MscLpTrRingSpeed_Object = MibTableColumn
mscLpTrRingSpeed = _MscLpTrRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1, 1),
    _MscLpTrRingSpeed_Type()
)
mscLpTrRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrRingSpeed.setStatus("mandatory")


class _MscLpTrMonitorParticipate_Type(Integer32):
    """Custom type mscLpTrMonitorParticipate based on Integer32"""
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


_MscLpTrMonitorParticipate_Type.__name__ = "Integer32"
_MscLpTrMonitorParticipate_Object = MibTableColumn
mscLpTrMonitorParticipate = _MscLpTrMonitorParticipate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1, 2),
    _MscLpTrMonitorParticipate_Type()
)
mscLpTrMonitorParticipate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrMonitorParticipate.setStatus("mandatory")


class _MscLpTrFunctionalAddress_Type(MacAddress):
    """Custom type mscLpTrFunctionalAddress based on MacAddress"""
    defaultHexValue = "0300feff8f01"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpTrFunctionalAddress_Type.__name__ = "MacAddress"
_MscLpTrFunctionalAddress_Object = MibTableColumn
mscLpTrFunctionalAddress = _MscLpTrFunctionalAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1, 3),
    _MscLpTrFunctionalAddress_Type()
)
mscLpTrFunctionalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrFunctionalAddress.setStatus("mandatory")


class _MscLpTrNodeAddress_Type(MacAddress):
    """Custom type mscLpTrNodeAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpTrNodeAddress_Type.__name__ = "MacAddress"
_MscLpTrNodeAddress_Object = MibTableColumn
mscLpTrNodeAddress = _MscLpTrNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1, 4),
    _MscLpTrNodeAddress_Type()
)
mscLpTrNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrNodeAddress.setStatus("mandatory")


class _MscLpTrGroupAddress_Type(MacAddress):
    """Custom type mscLpTrGroupAddress based on MacAddress"""
    defaultHexValue = "030001000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpTrGroupAddress_Type.__name__ = "MacAddress"
_MscLpTrGroupAddress_Object = MibTableColumn
mscLpTrGroupAddress = _MscLpTrGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1, 5),
    _MscLpTrGroupAddress_Type()
)
mscLpTrGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrGroupAddress.setStatus("mandatory")


class _MscLpTrProductId_Type(AsciiString):
    """Custom type mscLpTrProductId based on AsciiString"""
    defaultHexValue = "4c414e20546f6b656e2052696e67"

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_MscLpTrProductId_Type.__name__ = "AsciiString"
_MscLpTrProductId_Object = MibTableColumn
mscLpTrProductId = _MscLpTrProductId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1, 6),
    _MscLpTrProductId_Type()
)
mscLpTrProductId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrProductId.setStatus("mandatory")
_MscLpTrApplicationFramerName_Type = Link
_MscLpTrApplicationFramerName_Object = MibTableColumn
mscLpTrApplicationFramerName = _MscLpTrApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 12, 1, 7),
    _MscLpTrApplicationFramerName_Type()
)
mscLpTrApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrApplicationFramerName.setStatus("mandatory")
_MscLpTrAdminInfoTable_Object = MibTable
mscLpTrAdminInfoTable = _MscLpTrAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 13)
)
if mibBuilder.loadTexts:
    mscLpTrAdminInfoTable.setStatus("mandatory")
_MscLpTrAdminInfoEntry_Object = MibTableRow
mscLpTrAdminInfoEntry = _MscLpTrAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 13, 1)
)
mscLpTrAdminInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrAdminInfoEntry.setStatus("mandatory")


class _MscLpTrVendor_Type(AsciiString):
    """Custom type mscLpTrVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLpTrVendor_Type.__name__ = "AsciiString"
_MscLpTrVendor_Object = MibTableColumn
mscLpTrVendor = _MscLpTrVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 13, 1, 1),
    _MscLpTrVendor_Type()
)
mscLpTrVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrVendor.setStatus("mandatory")


class _MscLpTrCommentText_Type(AsciiString):
    """Custom type mscLpTrCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_MscLpTrCommentText_Type.__name__ = "AsciiString"
_MscLpTrCommentText_Object = MibTableColumn
mscLpTrCommentText = _MscLpTrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 13, 1, 2),
    _MscLpTrCommentText_Type()
)
mscLpTrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpTrCommentText.setStatus("mandatory")
_MscLpTrStateTable_Object = MibTable
mscLpTrStateTable = _MscLpTrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 15)
)
if mibBuilder.loadTexts:
    mscLpTrStateTable.setStatus("mandatory")
_MscLpTrStateEntry_Object = MibTableRow
mscLpTrStateEntry = _MscLpTrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 15, 1)
)
mscLpTrStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrStateEntry.setStatus("mandatory")


class _MscLpTrAdminState_Type(Integer32):
    """Custom type mscLpTrAdminState based on Integer32"""
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


_MscLpTrAdminState_Type.__name__ = "Integer32"
_MscLpTrAdminState_Object = MibTableColumn
mscLpTrAdminState = _MscLpTrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 15, 1, 1),
    _MscLpTrAdminState_Type()
)
mscLpTrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrAdminState.setStatus("mandatory")


class _MscLpTrOperationalState_Type(Integer32):
    """Custom type mscLpTrOperationalState based on Integer32"""
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


_MscLpTrOperationalState_Type.__name__ = "Integer32"
_MscLpTrOperationalState_Object = MibTableColumn
mscLpTrOperationalState = _MscLpTrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 15, 1, 2),
    _MscLpTrOperationalState_Type()
)
mscLpTrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrOperationalState.setStatus("mandatory")


class _MscLpTrUsageState_Type(Integer32):
    """Custom type mscLpTrUsageState based on Integer32"""
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


_MscLpTrUsageState_Type.__name__ = "Integer32"
_MscLpTrUsageState_Object = MibTableColumn
mscLpTrUsageState = _MscLpTrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 15, 1, 3),
    _MscLpTrUsageState_Type()
)
mscLpTrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrUsageState.setStatus("mandatory")
_MscLpTrOperStatusTable_Object = MibTable
mscLpTrOperStatusTable = _MscLpTrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 16)
)
if mibBuilder.loadTexts:
    mscLpTrOperStatusTable.setStatus("mandatory")
_MscLpTrOperStatusEntry_Object = MibTableRow
mscLpTrOperStatusEntry = _MscLpTrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 16, 1)
)
mscLpTrOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrOperStatusEntry.setStatus("mandatory")


class _MscLpTrSnmpOperStatus_Type(Integer32):
    """Custom type mscLpTrSnmpOperStatus based on Integer32"""
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


_MscLpTrSnmpOperStatus_Type.__name__ = "Integer32"
_MscLpTrSnmpOperStatus_Object = MibTableColumn
mscLpTrSnmpOperStatus = _MscLpTrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 16, 1, 1),
    _MscLpTrSnmpOperStatus_Type()
)
mscLpTrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrSnmpOperStatus.setStatus("mandatory")
_MscLpTrOperTable_Object = MibTable
mscLpTrOperTable = _MscLpTrOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17)
)
if mibBuilder.loadTexts:
    mscLpTrOperTable.setStatus("mandatory")
_MscLpTrOperEntry_Object = MibTableRow
mscLpTrOperEntry = _MscLpTrOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1)
)
mscLpTrOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrOperEntry.setStatus("mandatory")


class _MscLpTrMacAddress_Type(MacAddress):
    """Custom type mscLpTrMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpTrMacAddress_Type.__name__ = "MacAddress"
_MscLpTrMacAddress_Object = MibTableColumn
mscLpTrMacAddress = _MscLpTrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1, 2),
    _MscLpTrMacAddress_Type()
)
mscLpTrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrMacAddress.setStatus("mandatory")


class _MscLpTrRingState_Type(Integer32):
    """Custom type mscLpTrRingState based on Integer32"""
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


_MscLpTrRingState_Type.__name__ = "Integer32"
_MscLpTrRingState_Object = MibTableColumn
mscLpTrRingState = _MscLpTrRingState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1, 4),
    _MscLpTrRingState_Type()
)
mscLpTrRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrRingState.setStatus("mandatory")


class _MscLpTrRingStatus_Type(OctetString):
    """Custom type mscLpTrRingStatus based on OctetString"""
    defaultHexValue = "000040"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_MscLpTrRingStatus_Type.__name__ = "OctetString"
_MscLpTrRingStatus_Object = MibTableColumn
mscLpTrRingStatus = _MscLpTrRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1, 5),
    _MscLpTrRingStatus_Type()
)
mscLpTrRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrRingStatus.setStatus("mandatory")


class _MscLpTrRingOpenStatus_Type(Integer32):
    """Custom type mscLpTrRingOpenStatus based on Integer32"""
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


_MscLpTrRingOpenStatus_Type.__name__ = "Integer32"
_MscLpTrRingOpenStatus_Object = MibTableColumn
mscLpTrRingOpenStatus = _MscLpTrRingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1, 6),
    _MscLpTrRingOpenStatus_Type()
)
mscLpTrRingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrRingOpenStatus.setStatus("mandatory")


class _MscLpTrUpStream_Type(MacAddress):
    """Custom type mscLpTrUpStream based on MacAddress"""
    defaultHexValue = "000000000000"

    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpTrUpStream_Type.__name__ = "MacAddress"
_MscLpTrUpStream_Object = MibTableColumn
mscLpTrUpStream = _MscLpTrUpStream_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1, 7),
    _MscLpTrUpStream_Type()
)
mscLpTrUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrUpStream.setStatus("mandatory")


class _MscLpTrChipSet_Type(Integer32):
    """Custom type mscLpTrChipSet based on Integer32"""
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


_MscLpTrChipSet_Type.__name__ = "Integer32"
_MscLpTrChipSet_Object = MibTableColumn
mscLpTrChipSet = _MscLpTrChipSet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1, 9),
    _MscLpTrChipSet_Type()
)
mscLpTrChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrChipSet.setStatus("mandatory")


class _MscLpTrLastTimeBeaconSent_Type(EnterpriseDateAndTime):
    """Custom type mscLpTrLastTimeBeaconSent based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscLpTrLastTimeBeaconSent_Type.__name__ = "EnterpriseDateAndTime"
_MscLpTrLastTimeBeaconSent_Object = MibTableColumn
mscLpTrLastTimeBeaconSent = _MscLpTrLastTimeBeaconSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 17, 1, 10),
    _MscLpTrLastTimeBeaconSent_Type()
)
mscLpTrLastTimeBeaconSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLastTimeBeaconSent.setStatus("mandatory")
_MscLpTrStatsTable_Object = MibTable
mscLpTrStatsTable = _MscLpTrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18)
)
if mibBuilder.loadTexts:
    mscLpTrStatsTable.setStatus("mandatory")
_MscLpTrStatsEntry_Object = MibTableRow
mscLpTrStatsEntry = _MscLpTrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1)
)
mscLpTrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrStatsEntry.setStatus("mandatory")
_MscLpTrLineErrors_Type = Counter32
_MscLpTrLineErrors_Object = MibTableColumn
mscLpTrLineErrors = _MscLpTrLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 2),
    _MscLpTrLineErrors_Type()
)
mscLpTrLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLineErrors.setStatus("mandatory")
_MscLpTrBurstErrors_Type = Counter32
_MscLpTrBurstErrors_Object = MibTableColumn
mscLpTrBurstErrors = _MscLpTrBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 3),
    _MscLpTrBurstErrors_Type()
)
mscLpTrBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrBurstErrors.setStatus("mandatory")
_MscLpTrAcErrors_Type = Counter32
_MscLpTrAcErrors_Object = MibTableColumn
mscLpTrAcErrors = _MscLpTrAcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 4),
    _MscLpTrAcErrors_Type()
)
mscLpTrAcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrAcErrors.setStatus("mandatory")
_MscLpTrAbortTransErrors_Type = Counter32
_MscLpTrAbortTransErrors_Object = MibTableColumn
mscLpTrAbortTransErrors = _MscLpTrAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 5),
    _MscLpTrAbortTransErrors_Type()
)
mscLpTrAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrAbortTransErrors.setStatus("mandatory")
_MscLpTrInternalErrors_Type = Counter32
_MscLpTrInternalErrors_Object = MibTableColumn
mscLpTrInternalErrors = _MscLpTrInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 6),
    _MscLpTrInternalErrors_Type()
)
mscLpTrInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrInternalErrors.setStatus("mandatory")
_MscLpTrLostFrameErrors_Type = Counter32
_MscLpTrLostFrameErrors_Object = MibTableColumn
mscLpTrLostFrameErrors = _MscLpTrLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 7),
    _MscLpTrLostFrameErrors_Type()
)
mscLpTrLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLostFrameErrors.setStatus("mandatory")
_MscLpTrReceiveCongestions_Type = Counter32
_MscLpTrReceiveCongestions_Object = MibTableColumn
mscLpTrReceiveCongestions = _MscLpTrReceiveCongestions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 8),
    _MscLpTrReceiveCongestions_Type()
)
mscLpTrReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrReceiveCongestions.setStatus("mandatory")
_MscLpTrFrameCopiedErrors_Type = Counter32
_MscLpTrFrameCopiedErrors_Object = MibTableColumn
mscLpTrFrameCopiedErrors = _MscLpTrFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 9),
    _MscLpTrFrameCopiedErrors_Type()
)
mscLpTrFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrFrameCopiedErrors.setStatus("mandatory")
_MscLpTrTokenErrors_Type = Counter32
_MscLpTrTokenErrors_Object = MibTableColumn
mscLpTrTokenErrors = _MscLpTrTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 10),
    _MscLpTrTokenErrors_Type()
)
mscLpTrTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTokenErrors.setStatus("mandatory")
_MscLpTrSoftErrors_Type = Counter32
_MscLpTrSoftErrors_Object = MibTableColumn
mscLpTrSoftErrors = _MscLpTrSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 11),
    _MscLpTrSoftErrors_Type()
)
mscLpTrSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrSoftErrors.setStatus("mandatory")
_MscLpTrHardErrors_Type = Counter32
_MscLpTrHardErrors_Object = MibTableColumn
mscLpTrHardErrors = _MscLpTrHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 12),
    _MscLpTrHardErrors_Type()
)
mscLpTrHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrHardErrors.setStatus("mandatory")
_MscLpTrSignalLoss_Type = Counter32
_MscLpTrSignalLoss_Object = MibTableColumn
mscLpTrSignalLoss = _MscLpTrSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 13),
    _MscLpTrSignalLoss_Type()
)
mscLpTrSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrSignalLoss.setStatus("mandatory")
_MscLpTrTransmitBeacons_Type = Counter32
_MscLpTrTransmitBeacons_Object = MibTableColumn
mscLpTrTransmitBeacons = _MscLpTrTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 14),
    _MscLpTrTransmitBeacons_Type()
)
mscLpTrTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrTransmitBeacons.setStatus("mandatory")
_MscLpTrRingRecoverys_Type = Counter32
_MscLpTrRingRecoverys_Object = MibTableColumn
mscLpTrRingRecoverys = _MscLpTrRingRecoverys_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 15),
    _MscLpTrRingRecoverys_Type()
)
mscLpTrRingRecoverys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrRingRecoverys.setStatus("mandatory")
_MscLpTrLobeWires_Type = Counter32
_MscLpTrLobeWires_Object = MibTableColumn
mscLpTrLobeWires = _MscLpTrLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 16),
    _MscLpTrLobeWires_Type()
)
mscLpTrLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrLobeWires.setStatus("mandatory")
_MscLpTrRemoveRings_Type = Counter32
_MscLpTrRemoveRings_Object = MibTableColumn
mscLpTrRemoveRings = _MscLpTrRemoveRings_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 17),
    _MscLpTrRemoveRings_Type()
)
mscLpTrRemoveRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrRemoveRings.setStatus("mandatory")
_MscLpTrSingleStation_Type = Counter32
_MscLpTrSingleStation_Object = MibTableColumn
mscLpTrSingleStation = _MscLpTrSingleStation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 18),
    _MscLpTrSingleStation_Type()
)
mscLpTrSingleStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrSingleStation.setStatus("mandatory")
_MscLpTrFreqErrors_Type = Counter32
_MscLpTrFreqErrors_Object = MibTableColumn
mscLpTrFreqErrors = _MscLpTrFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 18, 1, 19),
    _MscLpTrFreqErrors_Type()
)
mscLpTrFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrFreqErrors.setStatus("mandatory")
_MscLpTrNcMacOperTable_Object = MibTable
mscLpTrNcMacOperTable = _MscLpTrNcMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 20)
)
if mibBuilder.loadTexts:
    mscLpTrNcMacOperTable.setStatus("mandatory")
_MscLpTrNcMacOperEntry_Object = MibTableRow
mscLpTrNcMacOperEntry = _MscLpTrNcMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 20, 1)
)
mscLpTrNcMacOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpTrNcMacOperEntry.setStatus("mandatory")


class _MscLpTrNcMacAddress_Type(MacAddress):
    """Custom type mscLpTrNcMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpTrNcMacAddress_Type.__name__ = "MacAddress"
_MscLpTrNcMacAddress_Object = MibTableColumn
mscLpTrNcMacAddress = _MscLpTrNcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 20, 1, 1),
    _MscLpTrNcMacAddress_Type()
)
mscLpTrNcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrNcMacAddress.setStatus("mandatory")


class _MscLpTrNcUpStream_Type(MacAddress):
    """Custom type mscLpTrNcUpStream based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpTrNcUpStream_Type.__name__ = "MacAddress"
_MscLpTrNcUpStream_Object = MibTableColumn
mscLpTrNcUpStream = _MscLpTrNcUpStream_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 13, 20, 1, 2),
    _MscLpTrNcUpStream_Type()
)
mscLpTrNcUpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpTrNcUpStream.setStatus("mandatory")
_MscLpIlsFwdr_ObjectIdentity = ObjectIdentity
mscLpIlsFwdr = _MscLpIlsFwdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21)
)
_MscLpIlsFwdrRowStatusTable_Object = MibTable
mscLpIlsFwdrRowStatusTable = _MscLpIlsFwdrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrRowStatusEntry = _MscLpIlsFwdrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 1, 1)
)
mscLpIlsFwdrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrRowStatus_Type = RowStatus
_MscLpIlsFwdrRowStatus_Object = MibTableColumn
mscLpIlsFwdrRowStatus = _MscLpIlsFwdrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 1, 1, 1),
    _MscLpIlsFwdrRowStatus_Type()
)
mscLpIlsFwdrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrRowStatus.setStatus("mandatory")
_MscLpIlsFwdrComponentName_Type = DisplayString
_MscLpIlsFwdrComponentName_Object = MibTableColumn
mscLpIlsFwdrComponentName = _MscLpIlsFwdrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 1, 1, 2),
    _MscLpIlsFwdrComponentName_Type()
)
mscLpIlsFwdrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrComponentName.setStatus("mandatory")
_MscLpIlsFwdrStorageType_Type = StorageType
_MscLpIlsFwdrStorageType_Object = MibTableColumn
mscLpIlsFwdrStorageType = _MscLpIlsFwdrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 1, 1, 4),
    _MscLpIlsFwdrStorageType_Type()
)
mscLpIlsFwdrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrStorageType.setStatus("mandatory")


class _MscLpIlsFwdrIndex_Type(Integer32):
    """Custom type mscLpIlsFwdrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscLpIlsFwdrIndex_Type.__name__ = "Integer32"
_MscLpIlsFwdrIndex_Object = MibTableColumn
mscLpIlsFwdrIndex = _MscLpIlsFwdrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 1, 1, 10),
    _MscLpIlsFwdrIndex_Type()
)
mscLpIlsFwdrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrIndex.setStatus("mandatory")
_MscLpIlsFwdrLt_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLt = _MscLpIlsFwdrLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2)
)
_MscLpIlsFwdrLtRowStatusTable_Object = MibTable
mscLpIlsFwdrLtRowStatusTable = _MscLpIlsFwdrLtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtRowStatusEntry = _MscLpIlsFwdrLtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 1, 1)
)
mscLpIlsFwdrLtRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtRowStatus_Type = RowStatus
_MscLpIlsFwdrLtRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtRowStatus = _MscLpIlsFwdrLtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 1, 1, 1),
    _MscLpIlsFwdrLtRowStatus_Type()
)
mscLpIlsFwdrLtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtComponentName_Type = DisplayString
_MscLpIlsFwdrLtComponentName_Object = MibTableColumn
mscLpIlsFwdrLtComponentName = _MscLpIlsFwdrLtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 1, 1, 2),
    _MscLpIlsFwdrLtComponentName_Type()
)
mscLpIlsFwdrLtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtStorageType_Type = StorageType
_MscLpIlsFwdrLtStorageType_Object = MibTableColumn
mscLpIlsFwdrLtStorageType = _MscLpIlsFwdrLtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 1, 1, 4),
    _MscLpIlsFwdrLtStorageType_Type()
)
mscLpIlsFwdrLtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtIndex_Type = NonReplicated
_MscLpIlsFwdrLtIndex_Object = MibTableColumn
mscLpIlsFwdrLtIndex = _MscLpIlsFwdrLtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 1, 1, 10),
    _MscLpIlsFwdrLtIndex_Type()
)
mscLpIlsFwdrLtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmp_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFrmCmp = _MscLpIlsFwdrLtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2)
)
_MscLpIlsFwdrLtFrmCmpRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFrmCmpRowStatusTable = _MscLpIlsFwdrLtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmpRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFrmCmpRowStatusEntry = _MscLpIlsFwdrLtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 1, 1)
)
mscLpIlsFwdrLtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmpRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFrmCmpRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFrmCmpRowStatus = _MscLpIlsFwdrLtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 1, 1, 1),
    _MscLpIlsFwdrLtFrmCmpRowStatus_Type()
)
mscLpIlsFwdrLtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmpComponentName_Type = DisplayString
_MscLpIlsFwdrLtFrmCmpComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFrmCmpComponentName = _MscLpIlsFwdrLtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 1, 1, 2),
    _MscLpIlsFwdrLtFrmCmpComponentName_Type()
)
mscLpIlsFwdrLtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmpStorageType_Type = StorageType
_MscLpIlsFwdrLtFrmCmpStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFrmCmpStorageType = _MscLpIlsFwdrLtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 1, 1, 4),
    _MscLpIlsFwdrLtFrmCmpStorageType_Type()
)
mscLpIlsFwdrLtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmpIndex_Type = NonReplicated
_MscLpIlsFwdrLtFrmCmpIndex_Object = MibTableColumn
mscLpIlsFwdrLtFrmCmpIndex = _MscLpIlsFwdrLtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 1, 1, 10),
    _MscLpIlsFwdrLtFrmCmpIndex_Type()
)
mscLpIlsFwdrLtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmpTopTable_Object = MibTable
mscLpIlsFwdrLtFrmCmpTopTable = _MscLpIlsFwdrLtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCmpTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFrmCmpTopEntry = _MscLpIlsFwdrLtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 10, 1)
)
mscLpIlsFwdrLtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFrmCmpTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFrmCmpTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFrmCmpTData_Object = MibTableColumn
mscLpIlsFwdrLtFrmCmpTData = _MscLpIlsFwdrLtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 2, 10, 1, 1),
    _MscLpIlsFwdrLtFrmCmpTData_Type()
)
mscLpIlsFwdrLtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCmpTData.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpy_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFrmCpy = _MscLpIlsFwdrLtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3)
)
_MscLpIlsFwdrLtFrmCpyRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFrmCpyRowStatusTable = _MscLpIlsFwdrLtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpyRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFrmCpyRowStatusEntry = _MscLpIlsFwdrLtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 1, 1)
)
mscLpIlsFwdrLtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpyRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFrmCpyRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFrmCpyRowStatus = _MscLpIlsFwdrLtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 1, 1, 1),
    _MscLpIlsFwdrLtFrmCpyRowStatus_Type()
)
mscLpIlsFwdrLtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpyComponentName_Type = DisplayString
_MscLpIlsFwdrLtFrmCpyComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFrmCpyComponentName = _MscLpIlsFwdrLtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 1, 1, 2),
    _MscLpIlsFwdrLtFrmCpyComponentName_Type()
)
mscLpIlsFwdrLtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpyStorageType_Type = StorageType
_MscLpIlsFwdrLtFrmCpyStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFrmCpyStorageType = _MscLpIlsFwdrLtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 1, 1, 4),
    _MscLpIlsFwdrLtFrmCpyStorageType_Type()
)
mscLpIlsFwdrLtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpyIndex_Type = NonReplicated
_MscLpIlsFwdrLtFrmCpyIndex_Object = MibTableColumn
mscLpIlsFwdrLtFrmCpyIndex = _MscLpIlsFwdrLtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 1, 1, 10),
    _MscLpIlsFwdrLtFrmCpyIndex_Type()
)
mscLpIlsFwdrLtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpyTopTable_Object = MibTable
mscLpIlsFwdrLtFrmCpyTopTable = _MscLpIlsFwdrLtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFrmCpyTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFrmCpyTopEntry = _MscLpIlsFwdrLtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 10, 1)
)
mscLpIlsFwdrLtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFrmCpyTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFrmCpyTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFrmCpyTData_Object = MibTableColumn
mscLpIlsFwdrLtFrmCpyTData = _MscLpIlsFwdrLtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 3, 10, 1, 1),
    _MscLpIlsFwdrLtFrmCpyTData_Type()
)
mscLpIlsFwdrLtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFrmCpyTData.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfg_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtPrtCfg = _MscLpIlsFwdrLtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4)
)
_MscLpIlsFwdrLtPrtCfgRowStatusTable_Object = MibTable
mscLpIlsFwdrLtPrtCfgRowStatusTable = _MscLpIlsFwdrLtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfgRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtPrtCfgRowStatusEntry = _MscLpIlsFwdrLtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 1, 1)
)
mscLpIlsFwdrLtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfgRowStatus_Type = RowStatus
_MscLpIlsFwdrLtPrtCfgRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtPrtCfgRowStatus = _MscLpIlsFwdrLtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 1, 1, 1),
    _MscLpIlsFwdrLtPrtCfgRowStatus_Type()
)
mscLpIlsFwdrLtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfgComponentName_Type = DisplayString
_MscLpIlsFwdrLtPrtCfgComponentName_Object = MibTableColumn
mscLpIlsFwdrLtPrtCfgComponentName = _MscLpIlsFwdrLtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 1, 1, 2),
    _MscLpIlsFwdrLtPrtCfgComponentName_Type()
)
mscLpIlsFwdrLtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfgStorageType_Type = StorageType
_MscLpIlsFwdrLtPrtCfgStorageType_Object = MibTableColumn
mscLpIlsFwdrLtPrtCfgStorageType = _MscLpIlsFwdrLtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 1, 1, 4),
    _MscLpIlsFwdrLtPrtCfgStorageType_Type()
)
mscLpIlsFwdrLtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfgIndex_Type = NonReplicated
_MscLpIlsFwdrLtPrtCfgIndex_Object = MibTableColumn
mscLpIlsFwdrLtPrtCfgIndex = _MscLpIlsFwdrLtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 1, 1, 10),
    _MscLpIlsFwdrLtPrtCfgIndex_Type()
)
mscLpIlsFwdrLtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgIndex.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfgTopTable_Object = MibTable
mscLpIlsFwdrLtPrtCfgTopTable = _MscLpIlsFwdrLtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtPrtCfgTopEntry_Object = MibTableRow
mscLpIlsFwdrLtPrtCfgTopEntry = _MscLpIlsFwdrLtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 10, 1)
)
mscLpIlsFwdrLtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtPrtCfgTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtPrtCfgTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtPrtCfgTData_Object = MibTableColumn
mscLpIlsFwdrLtPrtCfgTData = _MscLpIlsFwdrLtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 4, 10, 1, 1),
    _MscLpIlsFwdrLtPrtCfgTData_Type()
)
mscLpIlsFwdrLtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtPrtCfgTData.setStatus("mandatory")
_MscLpIlsFwdrLtFb_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFb = _MscLpIlsFwdrLtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5)
)
_MscLpIlsFwdrLtFbRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbRowStatusTable = _MscLpIlsFwdrLtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbRowStatusEntry = _MscLpIlsFwdrLtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 1, 1)
)
mscLpIlsFwdrLtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbRowStatus = _MscLpIlsFwdrLtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 1, 1, 1),
    _MscLpIlsFwdrLtFbRowStatus_Type()
)
mscLpIlsFwdrLtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbComponentName = _MscLpIlsFwdrLtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 1, 1, 2),
    _MscLpIlsFwdrLtFbComponentName_Type()
)
mscLpIlsFwdrLtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbStorageType_Type = StorageType
_MscLpIlsFwdrLtFbStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbStorageType = _MscLpIlsFwdrLtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 1, 1, 4),
    _MscLpIlsFwdrLtFbStorageType_Type()
)
mscLpIlsFwdrLtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbIndex = _MscLpIlsFwdrLtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 1, 1, 10),
    _MscLpIlsFwdrLtFbIndex_Type()
)
mscLpIlsFwdrLtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfo_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbTxInfo = _MscLpIlsFwdrLtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2)
)
_MscLpIlsFwdrLtFbTxInfoRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbTxInfoRowStatusTable = _MscLpIlsFwdrLtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfoRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbTxInfoRowStatusEntry = _MscLpIlsFwdrLtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 1, 1)
)
mscLpIlsFwdrLtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfoRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbTxInfoRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbTxInfoRowStatus = _MscLpIlsFwdrLtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 1, 1, 1),
    _MscLpIlsFwdrLtFbTxInfoRowStatus_Type()
)
mscLpIlsFwdrLtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfoComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbTxInfoComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbTxInfoComponentName = _MscLpIlsFwdrLtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 1, 1, 2),
    _MscLpIlsFwdrLtFbTxInfoComponentName_Type()
)
mscLpIlsFwdrLtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfoStorageType_Type = StorageType
_MscLpIlsFwdrLtFbTxInfoStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbTxInfoStorageType = _MscLpIlsFwdrLtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 1, 1, 4),
    _MscLpIlsFwdrLtFbTxInfoStorageType_Type()
)
mscLpIlsFwdrLtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfoIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbTxInfoIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbTxInfoIndex = _MscLpIlsFwdrLtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 1, 1, 10),
    _MscLpIlsFwdrLtFbTxInfoIndex_Type()
)
mscLpIlsFwdrLtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfoTopTable_Object = MibTable
mscLpIlsFwdrLtFbTxInfoTopTable = _MscLpIlsFwdrLtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbTxInfoTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbTxInfoTopEntry = _MscLpIlsFwdrLtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 10, 1)
)
mscLpIlsFwdrLtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbTxInfoTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbTxInfoTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbTxInfoTData_Object = MibTableColumn
mscLpIlsFwdrLtFbTxInfoTData = _MscLpIlsFwdrLtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 2, 10, 1, 1),
    _MscLpIlsFwdrLtFbTxInfoTData_Type()
)
mscLpIlsFwdrLtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTxInfoTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMac_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbFddiMac = _MscLpIlsFwdrLtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3)
)
_MscLpIlsFwdrLtFbFddiMacRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbFddiMacRowStatusTable = _MscLpIlsFwdrLtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMacRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbFddiMacRowStatusEntry = _MscLpIlsFwdrLtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 1, 1)
)
mscLpIlsFwdrLtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMacRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbFddiMacRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbFddiMacRowStatus = _MscLpIlsFwdrLtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 1, 1, 1),
    _MscLpIlsFwdrLtFbFddiMacRowStatus_Type()
)
mscLpIlsFwdrLtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMacComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbFddiMacComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbFddiMacComponentName = _MscLpIlsFwdrLtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 1, 1, 2),
    _MscLpIlsFwdrLtFbFddiMacComponentName_Type()
)
mscLpIlsFwdrLtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMacStorageType_Type = StorageType
_MscLpIlsFwdrLtFbFddiMacStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbFddiMacStorageType = _MscLpIlsFwdrLtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 1, 1, 4),
    _MscLpIlsFwdrLtFbFddiMacStorageType_Type()
)
mscLpIlsFwdrLtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMacIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbFddiMacIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbFddiMacIndex = _MscLpIlsFwdrLtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 1, 1, 10),
    _MscLpIlsFwdrLtFbFddiMacIndex_Type()
)
mscLpIlsFwdrLtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMacTopTable_Object = MibTable
mscLpIlsFwdrLtFbFddiMacTopTable = _MscLpIlsFwdrLtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbFddiMacTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbFddiMacTopEntry = _MscLpIlsFwdrLtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 10, 1)
)
mscLpIlsFwdrLtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbFddiMacTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbFddiMacTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbFddiMacTData_Object = MibTableColumn
mscLpIlsFwdrLtFbFddiMacTData = _MscLpIlsFwdrLtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 3, 10, 1, 1),
    _MscLpIlsFwdrLtFbFddiMacTData_Type()
)
mscLpIlsFwdrLtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbFddiMacTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnet_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbMacEnet = _MscLpIlsFwdrLtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4)
)
_MscLpIlsFwdrLtFbMacEnetRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbMacEnetRowStatusTable = _MscLpIlsFwdrLtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnetRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbMacEnetRowStatusEntry = _MscLpIlsFwdrLtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 1, 1)
)
mscLpIlsFwdrLtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnetRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbMacEnetRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbMacEnetRowStatus = _MscLpIlsFwdrLtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 1, 1, 1),
    _MscLpIlsFwdrLtFbMacEnetRowStatus_Type()
)
mscLpIlsFwdrLtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnetComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbMacEnetComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbMacEnetComponentName = _MscLpIlsFwdrLtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 1, 1, 2),
    _MscLpIlsFwdrLtFbMacEnetComponentName_Type()
)
mscLpIlsFwdrLtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnetStorageType_Type = StorageType
_MscLpIlsFwdrLtFbMacEnetStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbMacEnetStorageType = _MscLpIlsFwdrLtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 1, 1, 4),
    _MscLpIlsFwdrLtFbMacEnetStorageType_Type()
)
mscLpIlsFwdrLtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnetIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbMacEnetIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbMacEnetIndex = _MscLpIlsFwdrLtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 1, 1, 10),
    _MscLpIlsFwdrLtFbMacEnetIndex_Type()
)
mscLpIlsFwdrLtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnetTopTable_Object = MibTable
mscLpIlsFwdrLtFbMacEnetTopTable = _MscLpIlsFwdrLtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacEnetTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbMacEnetTopEntry = _MscLpIlsFwdrLtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 10, 1)
)
mscLpIlsFwdrLtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbMacEnetTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbMacEnetTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbMacEnetTData_Object = MibTableColumn
mscLpIlsFwdrLtFbMacEnetTData = _MscLpIlsFwdrLtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 4, 10, 1, 1),
    _MscLpIlsFwdrLtFbMacEnetTData_Type()
)
mscLpIlsFwdrLtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacEnetTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTr_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbMacTr = _MscLpIlsFwdrLtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5)
)
_MscLpIlsFwdrLtFbMacTrRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbMacTrRowStatusTable = _MscLpIlsFwdrLtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTrRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbMacTrRowStatusEntry = _MscLpIlsFwdrLtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 1, 1)
)
mscLpIlsFwdrLtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTrRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbMacTrRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbMacTrRowStatus = _MscLpIlsFwdrLtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 1, 1, 1),
    _MscLpIlsFwdrLtFbMacTrRowStatus_Type()
)
mscLpIlsFwdrLtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTrComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbMacTrComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbMacTrComponentName = _MscLpIlsFwdrLtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 1, 1, 2),
    _MscLpIlsFwdrLtFbMacTrComponentName_Type()
)
mscLpIlsFwdrLtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTrStorageType_Type = StorageType
_MscLpIlsFwdrLtFbMacTrStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbMacTrStorageType = _MscLpIlsFwdrLtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 1, 1, 4),
    _MscLpIlsFwdrLtFbMacTrStorageType_Type()
)
mscLpIlsFwdrLtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTrIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbMacTrIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbMacTrIndex = _MscLpIlsFwdrLtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 1, 1, 10),
    _MscLpIlsFwdrLtFbMacTrIndex_Type()
)
mscLpIlsFwdrLtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTrTopTable_Object = MibTable
mscLpIlsFwdrLtFbMacTrTopTable = _MscLpIlsFwdrLtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbMacTrTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbMacTrTopEntry = _MscLpIlsFwdrLtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 10, 1)
)
mscLpIlsFwdrLtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbMacTrTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbMacTrTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbMacTrTData_Object = MibTableColumn
mscLpIlsFwdrLtFbMacTrTData = _MscLpIlsFwdrLtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 5, 10, 1, 1),
    _MscLpIlsFwdrLtFbMacTrTData_Type()
)
mscLpIlsFwdrLtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbMacTrTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbData_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbData = _MscLpIlsFwdrLtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6)
)
_MscLpIlsFwdrLtFbDataRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbDataRowStatusTable = _MscLpIlsFwdrLtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbDataRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbDataRowStatusEntry = _MscLpIlsFwdrLtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 1, 1)
)
mscLpIlsFwdrLtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbDataRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbDataRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbDataRowStatus = _MscLpIlsFwdrLtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 1, 1, 1),
    _MscLpIlsFwdrLtFbDataRowStatus_Type()
)
mscLpIlsFwdrLtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbDataComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbDataComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbDataComponentName = _MscLpIlsFwdrLtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 1, 1, 2),
    _MscLpIlsFwdrLtFbDataComponentName_Type()
)
mscLpIlsFwdrLtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbDataStorageType_Type = StorageType
_MscLpIlsFwdrLtFbDataStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbDataStorageType = _MscLpIlsFwdrLtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 1, 1, 4),
    _MscLpIlsFwdrLtFbDataStorageType_Type()
)
mscLpIlsFwdrLtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbDataIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbDataIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbDataIndex = _MscLpIlsFwdrLtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 1, 1, 10),
    _MscLpIlsFwdrLtFbDataIndex_Type()
)
mscLpIlsFwdrLtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbDataTopTable_Object = MibTable
mscLpIlsFwdrLtFbDataTopTable = _MscLpIlsFwdrLtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbDataTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbDataTopEntry = _MscLpIlsFwdrLtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 10, 1)
)
mscLpIlsFwdrLtFbDataTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbDataTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbDataTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbDataTData_Object = MibTableColumn
mscLpIlsFwdrLtFbDataTData = _MscLpIlsFwdrLtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 6, 10, 1, 1),
    _MscLpIlsFwdrLtFbDataTData_Type()
)
mscLpIlsFwdrLtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbDataTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpH_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbIpH = _MscLpIlsFwdrLtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7)
)
_MscLpIlsFwdrLtFbIpHRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbIpHRowStatusTable = _MscLpIlsFwdrLtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpHRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbIpHRowStatusEntry = _MscLpIlsFwdrLtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 1, 1)
)
mscLpIlsFwdrLtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpHRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbIpHRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbIpHRowStatus = _MscLpIlsFwdrLtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 1, 1, 1),
    _MscLpIlsFwdrLtFbIpHRowStatus_Type()
)
mscLpIlsFwdrLtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpHComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbIpHComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbIpHComponentName = _MscLpIlsFwdrLtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 1, 1, 2),
    _MscLpIlsFwdrLtFbIpHComponentName_Type()
)
mscLpIlsFwdrLtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpHStorageType_Type = StorageType
_MscLpIlsFwdrLtFbIpHStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbIpHStorageType = _MscLpIlsFwdrLtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 1, 1, 4),
    _MscLpIlsFwdrLtFbIpHStorageType_Type()
)
mscLpIlsFwdrLtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpHIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbIpHIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbIpHIndex = _MscLpIlsFwdrLtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 1, 1, 10),
    _MscLpIlsFwdrLtFbIpHIndex_Type()
)
mscLpIlsFwdrLtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpHTopTable_Object = MibTable
mscLpIlsFwdrLtFbIpHTopTable = _MscLpIlsFwdrLtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpHTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbIpHTopEntry = _MscLpIlsFwdrLtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 10, 1)
)
mscLpIlsFwdrLtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbIpHTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbIpHTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbIpHTData_Object = MibTableColumn
mscLpIlsFwdrLtFbIpHTData = _MscLpIlsFwdrLtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 7, 10, 1, 1),
    _MscLpIlsFwdrLtFbIpHTData_Type()
)
mscLpIlsFwdrLtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpHTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlch_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbLlch = _MscLpIlsFwdrLtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8)
)
_MscLpIlsFwdrLtFbLlchRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbLlchRowStatusTable = _MscLpIlsFwdrLtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlchRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbLlchRowStatusEntry = _MscLpIlsFwdrLtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 1, 1)
)
mscLpIlsFwdrLtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlchRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbLlchRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbLlchRowStatus = _MscLpIlsFwdrLtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 1, 1, 1),
    _MscLpIlsFwdrLtFbLlchRowStatus_Type()
)
mscLpIlsFwdrLtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlchComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbLlchComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbLlchComponentName = _MscLpIlsFwdrLtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 1, 1, 2),
    _MscLpIlsFwdrLtFbLlchComponentName_Type()
)
mscLpIlsFwdrLtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlchStorageType_Type = StorageType
_MscLpIlsFwdrLtFbLlchStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbLlchStorageType = _MscLpIlsFwdrLtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 1, 1, 4),
    _MscLpIlsFwdrLtFbLlchStorageType_Type()
)
mscLpIlsFwdrLtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlchIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbLlchIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbLlchIndex = _MscLpIlsFwdrLtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 1, 1, 10),
    _MscLpIlsFwdrLtFbLlchIndex_Type()
)
mscLpIlsFwdrLtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlchTopTable_Object = MibTable
mscLpIlsFwdrLtFbLlchTopTable = _MscLpIlsFwdrLtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbLlchTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbLlchTopEntry = _MscLpIlsFwdrLtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 10, 1)
)
mscLpIlsFwdrLtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbLlchTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbLlchTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbLlchTData_Object = MibTableColumn
mscLpIlsFwdrLtFbLlchTData = _MscLpIlsFwdrLtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 8, 10, 1, 1),
    _MscLpIlsFwdrLtFbLlchTData_Type()
)
mscLpIlsFwdrLtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbLlchTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleH_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbAppleH = _MscLpIlsFwdrLtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9)
)
_MscLpIlsFwdrLtFbAppleHRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbAppleHRowStatusTable = _MscLpIlsFwdrLtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleHRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbAppleHRowStatusEntry = _MscLpIlsFwdrLtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 1, 1)
)
mscLpIlsFwdrLtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleHRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbAppleHRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbAppleHRowStatus = _MscLpIlsFwdrLtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 1, 1, 1),
    _MscLpIlsFwdrLtFbAppleHRowStatus_Type()
)
mscLpIlsFwdrLtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleHComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbAppleHComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbAppleHComponentName = _MscLpIlsFwdrLtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 1, 1, 2),
    _MscLpIlsFwdrLtFbAppleHComponentName_Type()
)
mscLpIlsFwdrLtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleHStorageType_Type = StorageType
_MscLpIlsFwdrLtFbAppleHStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbAppleHStorageType = _MscLpIlsFwdrLtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 1, 1, 4),
    _MscLpIlsFwdrLtFbAppleHStorageType_Type()
)
mscLpIlsFwdrLtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleHIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbAppleHIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbAppleHIndex = _MscLpIlsFwdrLtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 1, 1, 10),
    _MscLpIlsFwdrLtFbAppleHIndex_Type()
)
mscLpIlsFwdrLtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleHTopTable_Object = MibTable
mscLpIlsFwdrLtFbAppleHTopTable = _MscLpIlsFwdrLtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbAppleHTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbAppleHTopEntry = _MscLpIlsFwdrLtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 10, 1)
)
mscLpIlsFwdrLtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbAppleHTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbAppleHTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbAppleHTData_Object = MibTableColumn
mscLpIlsFwdrLtFbAppleHTData = _MscLpIlsFwdrLtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 9, 10, 1, 1),
    _MscLpIlsFwdrLtFbAppleHTData_Type()
)
mscLpIlsFwdrLtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbAppleHTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxH_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtFbIpxH = _MscLpIlsFwdrLtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10)
)
_MscLpIlsFwdrLtFbIpxHRowStatusTable_Object = MibTable
mscLpIlsFwdrLtFbIpxHRowStatusTable = _MscLpIlsFwdrLtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxHRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtFbIpxHRowStatusEntry = _MscLpIlsFwdrLtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 1, 1)
)
mscLpIlsFwdrLtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxHRowStatus_Type = RowStatus
_MscLpIlsFwdrLtFbIpxHRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtFbIpxHRowStatus = _MscLpIlsFwdrLtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 1, 1, 1),
    _MscLpIlsFwdrLtFbIpxHRowStatus_Type()
)
mscLpIlsFwdrLtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxHComponentName_Type = DisplayString
_MscLpIlsFwdrLtFbIpxHComponentName_Object = MibTableColumn
mscLpIlsFwdrLtFbIpxHComponentName = _MscLpIlsFwdrLtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 1, 1, 2),
    _MscLpIlsFwdrLtFbIpxHComponentName_Type()
)
mscLpIlsFwdrLtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxHStorageType_Type = StorageType
_MscLpIlsFwdrLtFbIpxHStorageType_Object = MibTableColumn
mscLpIlsFwdrLtFbIpxHStorageType = _MscLpIlsFwdrLtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 1, 1, 4),
    _MscLpIlsFwdrLtFbIpxHStorageType_Type()
)
mscLpIlsFwdrLtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxHIndex_Type = NonReplicated
_MscLpIlsFwdrLtFbIpxHIndex_Object = MibTableColumn
mscLpIlsFwdrLtFbIpxHIndex = _MscLpIlsFwdrLtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 1, 1, 10),
    _MscLpIlsFwdrLtFbIpxHIndex_Type()
)
mscLpIlsFwdrLtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHIndex.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxHTopTable_Object = MibTable
mscLpIlsFwdrLtFbIpxHTopTable = _MscLpIlsFwdrLtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbIpxHTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbIpxHTopEntry = _MscLpIlsFwdrLtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 10, 1)
)
mscLpIlsFwdrLtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbIpxHTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbIpxHTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbIpxHTData_Object = MibTableColumn
mscLpIlsFwdrLtFbIpxHTData = _MscLpIlsFwdrLtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 10, 10, 1, 1),
    _MscLpIlsFwdrLtFbIpxHTData_Type()
)
mscLpIlsFwdrLtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbIpxHTData.setStatus("mandatory")
_MscLpIlsFwdrLtFbTopTable_Object = MibTable
mscLpIlsFwdrLtFbTopTable = _MscLpIlsFwdrLtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 20)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtFbTopEntry_Object = MibTableRow
mscLpIlsFwdrLtFbTopEntry = _MscLpIlsFwdrLtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 20, 1)
)
mscLpIlsFwdrLtFbTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtFbTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtFbTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtFbTData_Object = MibTableColumn
mscLpIlsFwdrLtFbTData = _MscLpIlsFwdrLtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 5, 20, 1, 1),
    _MscLpIlsFwdrLtFbTData_Type()
)
mscLpIlsFwdrLtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtFbTData.setStatus("mandatory")
_MscLpIlsFwdrLtCntl_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrLtCntl = _MscLpIlsFwdrLtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6)
)
_MscLpIlsFwdrLtCntlRowStatusTable_Object = MibTable
mscLpIlsFwdrLtCntlRowStatusTable = _MscLpIlsFwdrLtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrLtCntlRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrLtCntlRowStatusEntry = _MscLpIlsFwdrLtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 1, 1)
)
mscLpIlsFwdrLtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrLtCntlRowStatus_Type = RowStatus
_MscLpIlsFwdrLtCntlRowStatus_Object = MibTableColumn
mscLpIlsFwdrLtCntlRowStatus = _MscLpIlsFwdrLtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 1, 1, 1),
    _MscLpIlsFwdrLtCntlRowStatus_Type()
)
mscLpIlsFwdrLtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlRowStatus.setStatus("mandatory")
_MscLpIlsFwdrLtCntlComponentName_Type = DisplayString
_MscLpIlsFwdrLtCntlComponentName_Object = MibTableColumn
mscLpIlsFwdrLtCntlComponentName = _MscLpIlsFwdrLtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 1, 1, 2),
    _MscLpIlsFwdrLtCntlComponentName_Type()
)
mscLpIlsFwdrLtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlComponentName.setStatus("mandatory")
_MscLpIlsFwdrLtCntlStorageType_Type = StorageType
_MscLpIlsFwdrLtCntlStorageType_Object = MibTableColumn
mscLpIlsFwdrLtCntlStorageType = _MscLpIlsFwdrLtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 1, 1, 4),
    _MscLpIlsFwdrLtCntlStorageType_Type()
)
mscLpIlsFwdrLtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlStorageType.setStatus("mandatory")
_MscLpIlsFwdrLtCntlIndex_Type = NonReplicated
_MscLpIlsFwdrLtCntlIndex_Object = MibTableColumn
mscLpIlsFwdrLtCntlIndex = _MscLpIlsFwdrLtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 1, 1, 10),
    _MscLpIlsFwdrLtCntlIndex_Type()
)
mscLpIlsFwdrLtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlIndex.setStatus("mandatory")
_MscLpIlsFwdrLtCntlTopTable_Object = MibTable
mscLpIlsFwdrLtCntlTopTable = _MscLpIlsFwdrLtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtCntlTopEntry_Object = MibTableRow
mscLpIlsFwdrLtCntlTopEntry = _MscLpIlsFwdrLtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 10, 1)
)
mscLpIlsFwdrLtCntlTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtCntlTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtCntlTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtCntlTData_Object = MibTableColumn
mscLpIlsFwdrLtCntlTData = _MscLpIlsFwdrLtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 6, 10, 1, 1),
    _MscLpIlsFwdrLtCntlTData_Type()
)
mscLpIlsFwdrLtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtCntlTData.setStatus("mandatory")
_MscLpIlsFwdrLtTopTable_Object = MibTable
mscLpIlsFwdrLtTopTable = _MscLpIlsFwdrLtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 20)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtTopTable.setStatus("mandatory")
_MscLpIlsFwdrLtTopEntry_Object = MibTableRow
mscLpIlsFwdrLtTopEntry = _MscLpIlsFwdrLtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 20, 1)
)
mscLpIlsFwdrLtTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLtIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtTopEntry.setStatus("mandatory")


class _MscLpIlsFwdrLtTData_Type(AsciiString):
    """Custom type mscLpIlsFwdrLtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpIlsFwdrLtTData_Type.__name__ = "AsciiString"
_MscLpIlsFwdrLtTData_Object = MibTableColumn
mscLpIlsFwdrLtTData = _MscLpIlsFwdrLtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 2, 20, 1, 1),
    _MscLpIlsFwdrLtTData_Type()
)
mscLpIlsFwdrLtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLtTData.setStatus("mandatory")
_MscLpIlsFwdrTest_ObjectIdentity = ObjectIdentity
mscLpIlsFwdrTest = _MscLpIlsFwdrTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5)
)
_MscLpIlsFwdrTestRowStatusTable_Object = MibTable
mscLpIlsFwdrTestRowStatusTable = _MscLpIlsFwdrTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestRowStatusTable.setStatus("mandatory")
_MscLpIlsFwdrTestRowStatusEntry_Object = MibTableRow
mscLpIlsFwdrTestRowStatusEntry = _MscLpIlsFwdrTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 1, 1)
)
mscLpIlsFwdrTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestRowStatusEntry.setStatus("mandatory")
_MscLpIlsFwdrTestRowStatus_Type = RowStatus
_MscLpIlsFwdrTestRowStatus_Object = MibTableColumn
mscLpIlsFwdrTestRowStatus = _MscLpIlsFwdrTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 1, 1, 1),
    _MscLpIlsFwdrTestRowStatus_Type()
)
mscLpIlsFwdrTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestRowStatus.setStatus("mandatory")
_MscLpIlsFwdrTestComponentName_Type = DisplayString
_MscLpIlsFwdrTestComponentName_Object = MibTableColumn
mscLpIlsFwdrTestComponentName = _MscLpIlsFwdrTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 1, 1, 2),
    _MscLpIlsFwdrTestComponentName_Type()
)
mscLpIlsFwdrTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestComponentName.setStatus("mandatory")
_MscLpIlsFwdrTestStorageType_Type = StorageType
_MscLpIlsFwdrTestStorageType_Object = MibTableColumn
mscLpIlsFwdrTestStorageType = _MscLpIlsFwdrTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 1, 1, 4),
    _MscLpIlsFwdrTestStorageType_Type()
)
mscLpIlsFwdrTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestStorageType.setStatus("mandatory")
_MscLpIlsFwdrTestIndex_Type = NonReplicated
_MscLpIlsFwdrTestIndex_Object = MibTableColumn
mscLpIlsFwdrTestIndex = _MscLpIlsFwdrTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 1, 1, 10),
    _MscLpIlsFwdrTestIndex_Type()
)
mscLpIlsFwdrTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestIndex.setStatus("mandatory")
_MscLpIlsFwdrTestPTOTable_Object = MibTable
mscLpIlsFwdrTestPTOTable = _MscLpIlsFwdrTestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestPTOTable.setStatus("mandatory")
_MscLpIlsFwdrTestPTOEntry_Object = MibTableRow
mscLpIlsFwdrTestPTOEntry = _MscLpIlsFwdrTestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 10, 1)
)
mscLpIlsFwdrTestPTOEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestPTOEntry.setStatus("mandatory")


class _MscLpIlsFwdrTestType_Type(Integer32):
    """Custom type mscLpIlsFwdrTestType based on Integer32"""
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


_MscLpIlsFwdrTestType_Type.__name__ = "Integer32"
_MscLpIlsFwdrTestType_Object = MibTableColumn
mscLpIlsFwdrTestType = _MscLpIlsFwdrTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 10, 1, 1),
    _MscLpIlsFwdrTestType_Type()
)
mscLpIlsFwdrTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestType.setStatus("mandatory")


class _MscLpIlsFwdrTestFrmSize_Type(Unsigned32):
    """Custom type mscLpIlsFwdrTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscLpIlsFwdrTestFrmSize_Type.__name__ = "Unsigned32"
_MscLpIlsFwdrTestFrmSize_Object = MibTableColumn
mscLpIlsFwdrTestFrmSize = _MscLpIlsFwdrTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 10, 1, 2),
    _MscLpIlsFwdrTestFrmSize_Type()
)
mscLpIlsFwdrTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestFrmSize.setStatus("mandatory")


class _MscLpIlsFwdrTestDuration_Type(Unsigned32):
    """Custom type mscLpIlsFwdrTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscLpIlsFwdrTestDuration_Type.__name__ = "Unsigned32"
_MscLpIlsFwdrTestDuration_Object = MibTableColumn
mscLpIlsFwdrTestDuration = _MscLpIlsFwdrTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 10, 1, 3),
    _MscLpIlsFwdrTestDuration_Type()
)
mscLpIlsFwdrTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestDuration.setStatus("mandatory")
_MscLpIlsFwdrTestResultsTable_Object = MibTable
mscLpIlsFwdrTestResultsTable = _MscLpIlsFwdrTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestResultsTable.setStatus("mandatory")
_MscLpIlsFwdrTestResultsEntry_Object = MibTableRow
mscLpIlsFwdrTestResultsEntry = _MscLpIlsFwdrTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1)
)
mscLpIlsFwdrTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestResultsEntry.setStatus("mandatory")
_MscLpIlsFwdrTestElapsedTime_Type = Counter32
_MscLpIlsFwdrTestElapsedTime_Object = MibTableColumn
mscLpIlsFwdrTestElapsedTime = _MscLpIlsFwdrTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 4),
    _MscLpIlsFwdrTestElapsedTime_Type()
)
mscLpIlsFwdrTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestElapsedTime.setStatus("mandatory")


class _MscLpIlsFwdrTestTimeRemaining_Type(Unsigned32):
    """Custom type mscLpIlsFwdrTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpIlsFwdrTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscLpIlsFwdrTestTimeRemaining_Object = MibTableColumn
mscLpIlsFwdrTestTimeRemaining = _MscLpIlsFwdrTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 5),
    _MscLpIlsFwdrTestTimeRemaining_Type()
)
mscLpIlsFwdrTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestTimeRemaining.setStatus("mandatory")


class _MscLpIlsFwdrTestCauseOfTermination_Type(Integer32):
    """Custom type mscLpIlsFwdrTestCauseOfTermination based on Integer32"""
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


_MscLpIlsFwdrTestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpIlsFwdrTestCauseOfTermination_Object = MibTableColumn
mscLpIlsFwdrTestCauseOfTermination = _MscLpIlsFwdrTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 6),
    _MscLpIlsFwdrTestCauseOfTermination_Type()
)
mscLpIlsFwdrTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestCauseOfTermination.setStatus("mandatory")
_MscLpIlsFwdrTestFrmTx_Type = PassportCounter64
_MscLpIlsFwdrTestFrmTx_Object = MibTableColumn
mscLpIlsFwdrTestFrmTx = _MscLpIlsFwdrTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 7),
    _MscLpIlsFwdrTestFrmTx_Type()
)
mscLpIlsFwdrTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestFrmTx.setStatus("mandatory")
_MscLpIlsFwdrTestBitsTx_Type = PassportCounter64
_MscLpIlsFwdrTestBitsTx_Object = MibTableColumn
mscLpIlsFwdrTestBitsTx = _MscLpIlsFwdrTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 8),
    _MscLpIlsFwdrTestBitsTx_Type()
)
mscLpIlsFwdrTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestBitsTx.setStatus("mandatory")
_MscLpIlsFwdrTestFrmRx_Type = PassportCounter64
_MscLpIlsFwdrTestFrmRx_Object = MibTableColumn
mscLpIlsFwdrTestFrmRx = _MscLpIlsFwdrTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 9),
    _MscLpIlsFwdrTestFrmRx_Type()
)
mscLpIlsFwdrTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestFrmRx.setStatus("mandatory")
_MscLpIlsFwdrTestBitsRx_Type = PassportCounter64
_MscLpIlsFwdrTestBitsRx_Object = MibTableColumn
mscLpIlsFwdrTestBitsRx = _MscLpIlsFwdrTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 10),
    _MscLpIlsFwdrTestBitsRx_Type()
)
mscLpIlsFwdrTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestBitsRx.setStatus("mandatory")
_MscLpIlsFwdrTestErroredFrmRx_Type = PassportCounter64
_MscLpIlsFwdrTestErroredFrmRx_Object = MibTableColumn
mscLpIlsFwdrTestErroredFrmRx = _MscLpIlsFwdrTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 5, 11, 1, 11),
    _MscLpIlsFwdrTestErroredFrmRx_Type()
)
mscLpIlsFwdrTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrTestErroredFrmRx.setStatus("mandatory")
_MscLpIlsFwdrIfEntryTable_Object = MibTable
mscLpIlsFwdrIfEntryTable = _MscLpIlsFwdrIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 11)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrIfEntryTable.setStatus("mandatory")
_MscLpIlsFwdrIfEntryEntry_Object = MibTableRow
mscLpIlsFwdrIfEntryEntry = _MscLpIlsFwdrIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 11, 1)
)
mscLpIlsFwdrIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrIfEntryEntry.setStatus("mandatory")


class _MscLpIlsFwdrIfAdminStatus_Type(Integer32):
    """Custom type mscLpIlsFwdrIfAdminStatus based on Integer32"""
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


_MscLpIlsFwdrIfAdminStatus_Type.__name__ = "Integer32"
_MscLpIlsFwdrIfAdminStatus_Object = MibTableColumn
mscLpIlsFwdrIfAdminStatus = _MscLpIlsFwdrIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 11, 1, 1),
    _MscLpIlsFwdrIfAdminStatus_Type()
)
mscLpIlsFwdrIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpIlsFwdrIfAdminStatus.setStatus("mandatory")


class _MscLpIlsFwdrIfIndex_Type(InterfaceIndex):
    """Custom type mscLpIlsFwdrIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLpIlsFwdrIfIndex_Type.__name__ = "InterfaceIndex"
_MscLpIlsFwdrIfIndex_Object = MibTableColumn
mscLpIlsFwdrIfIndex = _MscLpIlsFwdrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 11, 1, 2),
    _MscLpIlsFwdrIfIndex_Type()
)
mscLpIlsFwdrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrIfIndex.setStatus("mandatory")
_MscLpIlsFwdrStateTable_Object = MibTable
mscLpIlsFwdrStateTable = _MscLpIlsFwdrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 12)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrStateTable.setStatus("mandatory")
_MscLpIlsFwdrStateEntry_Object = MibTableRow
mscLpIlsFwdrStateEntry = _MscLpIlsFwdrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 12, 1)
)
mscLpIlsFwdrStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrStateEntry.setStatus("mandatory")


class _MscLpIlsFwdrAdminState_Type(Integer32):
    """Custom type mscLpIlsFwdrAdminState based on Integer32"""
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


_MscLpIlsFwdrAdminState_Type.__name__ = "Integer32"
_MscLpIlsFwdrAdminState_Object = MibTableColumn
mscLpIlsFwdrAdminState = _MscLpIlsFwdrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 12, 1, 1),
    _MscLpIlsFwdrAdminState_Type()
)
mscLpIlsFwdrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrAdminState.setStatus("mandatory")


class _MscLpIlsFwdrOperationalState_Type(Integer32):
    """Custom type mscLpIlsFwdrOperationalState based on Integer32"""
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


_MscLpIlsFwdrOperationalState_Type.__name__ = "Integer32"
_MscLpIlsFwdrOperationalState_Object = MibTableColumn
mscLpIlsFwdrOperationalState = _MscLpIlsFwdrOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 12, 1, 2),
    _MscLpIlsFwdrOperationalState_Type()
)
mscLpIlsFwdrOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrOperationalState.setStatus("mandatory")


class _MscLpIlsFwdrUsageState_Type(Integer32):
    """Custom type mscLpIlsFwdrUsageState based on Integer32"""
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


_MscLpIlsFwdrUsageState_Type.__name__ = "Integer32"
_MscLpIlsFwdrUsageState_Object = MibTableColumn
mscLpIlsFwdrUsageState = _MscLpIlsFwdrUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 12, 1, 3),
    _MscLpIlsFwdrUsageState_Type()
)
mscLpIlsFwdrUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrUsageState.setStatus("mandatory")
_MscLpIlsFwdrOperStatusTable_Object = MibTable
mscLpIlsFwdrOperStatusTable = _MscLpIlsFwdrOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 13)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrOperStatusTable.setStatus("mandatory")
_MscLpIlsFwdrOperStatusEntry_Object = MibTableRow
mscLpIlsFwdrOperStatusEntry = _MscLpIlsFwdrOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 13, 1)
)
mscLpIlsFwdrOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrOperStatusEntry.setStatus("mandatory")


class _MscLpIlsFwdrSnmpOperStatus_Type(Integer32):
    """Custom type mscLpIlsFwdrSnmpOperStatus based on Integer32"""
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


_MscLpIlsFwdrSnmpOperStatus_Type.__name__ = "Integer32"
_MscLpIlsFwdrSnmpOperStatus_Object = MibTableColumn
mscLpIlsFwdrSnmpOperStatus = _MscLpIlsFwdrSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 13, 1, 1),
    _MscLpIlsFwdrSnmpOperStatus_Type()
)
mscLpIlsFwdrSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrSnmpOperStatus.setStatus("mandatory")
_MscLpIlsFwdrStatsTable_Object = MibTable
mscLpIlsFwdrStatsTable = _MscLpIlsFwdrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 14)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrStatsTable.setStatus("mandatory")
_MscLpIlsFwdrStatsEntry_Object = MibTableRow
mscLpIlsFwdrStatsEntry = _MscLpIlsFwdrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 14, 1)
)
mscLpIlsFwdrStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrStatsEntry.setStatus("mandatory")
_MscLpIlsFwdrFramesReceived_Type = PassportCounter64
_MscLpIlsFwdrFramesReceived_Object = MibTableColumn
mscLpIlsFwdrFramesReceived = _MscLpIlsFwdrFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 14, 1, 1),
    _MscLpIlsFwdrFramesReceived_Type()
)
mscLpIlsFwdrFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrFramesReceived.setStatus("mandatory")
_MscLpIlsFwdrProcessedCount_Type = PassportCounter64
_MscLpIlsFwdrProcessedCount_Object = MibTableColumn
mscLpIlsFwdrProcessedCount = _MscLpIlsFwdrProcessedCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 14, 1, 2),
    _MscLpIlsFwdrProcessedCount_Type()
)
mscLpIlsFwdrProcessedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrProcessedCount.setStatus("mandatory")
_MscLpIlsFwdrErrorCount_Type = PassportCounter64
_MscLpIlsFwdrErrorCount_Object = MibTableColumn
mscLpIlsFwdrErrorCount = _MscLpIlsFwdrErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 14, 1, 3),
    _MscLpIlsFwdrErrorCount_Type()
)
mscLpIlsFwdrErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrErrorCount.setStatus("mandatory")
_MscLpIlsFwdrFramesDiscarded_Type = PassportCounter64
_MscLpIlsFwdrFramesDiscarded_Object = MibTableColumn
mscLpIlsFwdrFramesDiscarded = _MscLpIlsFwdrFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 14, 1, 4),
    _MscLpIlsFwdrFramesDiscarded_Type()
)
mscLpIlsFwdrFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrFramesDiscarded.setStatus("mandatory")
_MscLpIlsFwdrLinkToTrafficSourceTable_Object = MibTable
mscLpIlsFwdrLinkToTrafficSourceTable = _MscLpIlsFwdrLinkToTrafficSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 312)
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLinkToTrafficSourceTable.setStatus("mandatory")
_MscLpIlsFwdrLinkToTrafficSourceEntry_Object = MibTableRow
mscLpIlsFwdrLinkToTrafficSourceEntry = _MscLpIlsFwdrLinkToTrafficSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 312, 1)
)
mscLpIlsFwdrLinkToTrafficSourceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpIlsFwdrLinkToTrafficSourceValue"),
)
if mibBuilder.loadTexts:
    mscLpIlsFwdrLinkToTrafficSourceEntry.setStatus("mandatory")
_MscLpIlsFwdrLinkToTrafficSourceValue_Type = Link
_MscLpIlsFwdrLinkToTrafficSourceValue_Object = MibTableColumn
mscLpIlsFwdrLinkToTrafficSourceValue = _MscLpIlsFwdrLinkToTrafficSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 21, 312, 1, 1),
    _MscLpIlsFwdrLinkToTrafficSourceValue_Type()
)
mscLpIlsFwdrLinkToTrafficSourceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpIlsFwdrLinkToTrafficSourceValue.setStatus("mandatory")
_MscLpEth100_ObjectIdentity = ObjectIdentity
mscLpEth100 = _MscLpEth100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25)
)
_MscLpEth100RowStatusTable_Object = MibTable
mscLpEth100RowStatusTable = _MscLpEth100RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100RowStatusTable.setStatus("mandatory")
_MscLpEth100RowStatusEntry_Object = MibTableRow
mscLpEth100RowStatusEntry = _MscLpEth100RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 1, 1)
)
mscLpEth100RowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100RowStatusEntry.setStatus("mandatory")
_MscLpEth100RowStatus_Type = RowStatus
_MscLpEth100RowStatus_Object = MibTableColumn
mscLpEth100RowStatus = _MscLpEth100RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 1, 1, 1),
    _MscLpEth100RowStatus_Type()
)
mscLpEth100RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100RowStatus.setStatus("mandatory")
_MscLpEth100ComponentName_Type = DisplayString
_MscLpEth100ComponentName_Object = MibTableColumn
mscLpEth100ComponentName = _MscLpEth100ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 1, 1, 2),
    _MscLpEth100ComponentName_Type()
)
mscLpEth100ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100ComponentName.setStatus("mandatory")
_MscLpEth100StorageType_Type = StorageType
_MscLpEth100StorageType_Object = MibTableColumn
mscLpEth100StorageType = _MscLpEth100StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 1, 1, 4),
    _MscLpEth100StorageType_Type()
)
mscLpEth100StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100StorageType.setStatus("mandatory")


class _MscLpEth100Index_Type(Integer32):
    """Custom type mscLpEth100Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscLpEth100Index_Type.__name__ = "Integer32"
_MscLpEth100Index_Object = MibTableColumn
mscLpEth100Index = _MscLpEth100Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 1, 1, 10),
    _MscLpEth100Index_Type()
)
mscLpEth100Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100Index.setStatus("mandatory")
_MscLpEth100Lt_ObjectIdentity = ObjectIdentity
mscLpEth100Lt = _MscLpEth100Lt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2)
)
_MscLpEth100LtRowStatusTable_Object = MibTable
mscLpEth100LtRowStatusTable = _MscLpEth100LtRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtRowStatusTable.setStatus("mandatory")
_MscLpEth100LtRowStatusEntry_Object = MibTableRow
mscLpEth100LtRowStatusEntry = _MscLpEth100LtRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 1, 1)
)
mscLpEth100LtRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtRowStatus_Type = RowStatus
_MscLpEth100LtRowStatus_Object = MibTableColumn
mscLpEth100LtRowStatus = _MscLpEth100LtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 1, 1, 1),
    _MscLpEth100LtRowStatus_Type()
)
mscLpEth100LtRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtRowStatus.setStatus("mandatory")
_MscLpEth100LtComponentName_Type = DisplayString
_MscLpEth100LtComponentName_Object = MibTableColumn
mscLpEth100LtComponentName = _MscLpEth100LtComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 1, 1, 2),
    _MscLpEth100LtComponentName_Type()
)
mscLpEth100LtComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtComponentName.setStatus("mandatory")
_MscLpEth100LtStorageType_Type = StorageType
_MscLpEth100LtStorageType_Object = MibTableColumn
mscLpEth100LtStorageType = _MscLpEth100LtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 1, 1, 4),
    _MscLpEth100LtStorageType_Type()
)
mscLpEth100LtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtStorageType.setStatus("mandatory")
_MscLpEth100LtIndex_Type = NonReplicated
_MscLpEth100LtIndex_Object = MibTableColumn
mscLpEth100LtIndex = _MscLpEth100LtIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 1, 1, 10),
    _MscLpEth100LtIndex_Type()
)
mscLpEth100LtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtIndex.setStatus("mandatory")
_MscLpEth100LtFrmCmp_ObjectIdentity = ObjectIdentity
mscLpEth100LtFrmCmp = _MscLpEth100LtFrmCmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2)
)
_MscLpEth100LtFrmCmpRowStatusTable_Object = MibTable
mscLpEth100LtFrmCmpRowStatusTable = _MscLpEth100LtFrmCmpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFrmCmpRowStatusEntry_Object = MibTableRow
mscLpEth100LtFrmCmpRowStatusEntry = _MscLpEth100LtFrmCmpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 1, 1)
)
mscLpEth100LtFrmCmpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFrmCmpRowStatus_Type = RowStatus
_MscLpEth100LtFrmCmpRowStatus_Object = MibTableColumn
mscLpEth100LtFrmCmpRowStatus = _MscLpEth100LtFrmCmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 1, 1, 1),
    _MscLpEth100LtFrmCmpRowStatus_Type()
)
mscLpEth100LtFrmCmpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpRowStatus.setStatus("mandatory")
_MscLpEth100LtFrmCmpComponentName_Type = DisplayString
_MscLpEth100LtFrmCmpComponentName_Object = MibTableColumn
mscLpEth100LtFrmCmpComponentName = _MscLpEth100LtFrmCmpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 1, 1, 2),
    _MscLpEth100LtFrmCmpComponentName_Type()
)
mscLpEth100LtFrmCmpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpComponentName.setStatus("mandatory")
_MscLpEth100LtFrmCmpStorageType_Type = StorageType
_MscLpEth100LtFrmCmpStorageType_Object = MibTableColumn
mscLpEth100LtFrmCmpStorageType = _MscLpEth100LtFrmCmpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 1, 1, 4),
    _MscLpEth100LtFrmCmpStorageType_Type()
)
mscLpEth100LtFrmCmpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpStorageType.setStatus("mandatory")
_MscLpEth100LtFrmCmpIndex_Type = NonReplicated
_MscLpEth100LtFrmCmpIndex_Object = MibTableColumn
mscLpEth100LtFrmCmpIndex = _MscLpEth100LtFrmCmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 1, 1, 10),
    _MscLpEth100LtFrmCmpIndex_Type()
)
mscLpEth100LtFrmCmpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpIndex.setStatus("mandatory")
_MscLpEth100LtFrmCmpTopTable_Object = MibTable
mscLpEth100LtFrmCmpTopTable = _MscLpEth100LtFrmCmpTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpTopTable.setStatus("mandatory")
_MscLpEth100LtFrmCmpTopEntry_Object = MibTableRow
mscLpEth100LtFrmCmpTopEntry = _MscLpEth100LtFrmCmpTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 10, 1)
)
mscLpEth100LtFrmCmpTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFrmCmpIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpTopEntry.setStatus("mandatory")


class _MscLpEth100LtFrmCmpTData_Type(AsciiString):
    """Custom type mscLpEth100LtFrmCmpTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFrmCmpTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFrmCmpTData_Object = MibTableColumn
mscLpEth100LtFrmCmpTData = _MscLpEth100LtFrmCmpTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 2, 10, 1, 1),
    _MscLpEth100LtFrmCmpTData_Type()
)
mscLpEth100LtFrmCmpTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCmpTData.setStatus("mandatory")
_MscLpEth100LtFrmCpy_ObjectIdentity = ObjectIdentity
mscLpEth100LtFrmCpy = _MscLpEth100LtFrmCpy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3)
)
_MscLpEth100LtFrmCpyRowStatusTable_Object = MibTable
mscLpEth100LtFrmCpyRowStatusTable = _MscLpEth100LtFrmCpyRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFrmCpyRowStatusEntry_Object = MibTableRow
mscLpEth100LtFrmCpyRowStatusEntry = _MscLpEth100LtFrmCpyRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 1, 1)
)
mscLpEth100LtFrmCpyRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFrmCpyRowStatus_Type = RowStatus
_MscLpEth100LtFrmCpyRowStatus_Object = MibTableColumn
mscLpEth100LtFrmCpyRowStatus = _MscLpEth100LtFrmCpyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 1, 1, 1),
    _MscLpEth100LtFrmCpyRowStatus_Type()
)
mscLpEth100LtFrmCpyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyRowStatus.setStatus("mandatory")
_MscLpEth100LtFrmCpyComponentName_Type = DisplayString
_MscLpEth100LtFrmCpyComponentName_Object = MibTableColumn
mscLpEth100LtFrmCpyComponentName = _MscLpEth100LtFrmCpyComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 1, 1, 2),
    _MscLpEth100LtFrmCpyComponentName_Type()
)
mscLpEth100LtFrmCpyComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyComponentName.setStatus("mandatory")
_MscLpEth100LtFrmCpyStorageType_Type = StorageType
_MscLpEth100LtFrmCpyStorageType_Object = MibTableColumn
mscLpEth100LtFrmCpyStorageType = _MscLpEth100LtFrmCpyStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 1, 1, 4),
    _MscLpEth100LtFrmCpyStorageType_Type()
)
mscLpEth100LtFrmCpyStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyStorageType.setStatus("mandatory")
_MscLpEth100LtFrmCpyIndex_Type = NonReplicated
_MscLpEth100LtFrmCpyIndex_Object = MibTableColumn
mscLpEth100LtFrmCpyIndex = _MscLpEth100LtFrmCpyIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 1, 1, 10),
    _MscLpEth100LtFrmCpyIndex_Type()
)
mscLpEth100LtFrmCpyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyIndex.setStatus("mandatory")
_MscLpEth100LtFrmCpyTopTable_Object = MibTable
mscLpEth100LtFrmCpyTopTable = _MscLpEth100LtFrmCpyTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyTopTable.setStatus("mandatory")
_MscLpEth100LtFrmCpyTopEntry_Object = MibTableRow
mscLpEth100LtFrmCpyTopEntry = _MscLpEth100LtFrmCpyTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 10, 1)
)
mscLpEth100LtFrmCpyTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFrmCpyIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyTopEntry.setStatus("mandatory")


class _MscLpEth100LtFrmCpyTData_Type(AsciiString):
    """Custom type mscLpEth100LtFrmCpyTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFrmCpyTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFrmCpyTData_Object = MibTableColumn
mscLpEth100LtFrmCpyTData = _MscLpEth100LtFrmCpyTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 3, 10, 1, 1),
    _MscLpEth100LtFrmCpyTData_Type()
)
mscLpEth100LtFrmCpyTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFrmCpyTData.setStatus("mandatory")
_MscLpEth100LtPrtCfg_ObjectIdentity = ObjectIdentity
mscLpEth100LtPrtCfg = _MscLpEth100LtPrtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4)
)
_MscLpEth100LtPrtCfgRowStatusTable_Object = MibTable
mscLpEth100LtPrtCfgRowStatusTable = _MscLpEth100LtPrtCfgRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgRowStatusTable.setStatus("mandatory")
_MscLpEth100LtPrtCfgRowStatusEntry_Object = MibTableRow
mscLpEth100LtPrtCfgRowStatusEntry = _MscLpEth100LtPrtCfgRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 1, 1)
)
mscLpEth100LtPrtCfgRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtPrtCfgRowStatus_Type = RowStatus
_MscLpEth100LtPrtCfgRowStatus_Object = MibTableColumn
mscLpEth100LtPrtCfgRowStatus = _MscLpEth100LtPrtCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 1, 1, 1),
    _MscLpEth100LtPrtCfgRowStatus_Type()
)
mscLpEth100LtPrtCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgRowStatus.setStatus("mandatory")
_MscLpEth100LtPrtCfgComponentName_Type = DisplayString
_MscLpEth100LtPrtCfgComponentName_Object = MibTableColumn
mscLpEth100LtPrtCfgComponentName = _MscLpEth100LtPrtCfgComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 1, 1, 2),
    _MscLpEth100LtPrtCfgComponentName_Type()
)
mscLpEth100LtPrtCfgComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgComponentName.setStatus("mandatory")
_MscLpEth100LtPrtCfgStorageType_Type = StorageType
_MscLpEth100LtPrtCfgStorageType_Object = MibTableColumn
mscLpEth100LtPrtCfgStorageType = _MscLpEth100LtPrtCfgStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 1, 1, 4),
    _MscLpEth100LtPrtCfgStorageType_Type()
)
mscLpEth100LtPrtCfgStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgStorageType.setStatus("mandatory")
_MscLpEth100LtPrtCfgIndex_Type = NonReplicated
_MscLpEth100LtPrtCfgIndex_Object = MibTableColumn
mscLpEth100LtPrtCfgIndex = _MscLpEth100LtPrtCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 1, 1, 10),
    _MscLpEth100LtPrtCfgIndex_Type()
)
mscLpEth100LtPrtCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgIndex.setStatus("mandatory")
_MscLpEth100LtPrtCfgTopTable_Object = MibTable
mscLpEth100LtPrtCfgTopTable = _MscLpEth100LtPrtCfgTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgTopTable.setStatus("mandatory")
_MscLpEth100LtPrtCfgTopEntry_Object = MibTableRow
mscLpEth100LtPrtCfgTopEntry = _MscLpEth100LtPrtCfgTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 10, 1)
)
mscLpEth100LtPrtCfgTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtPrtCfgIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgTopEntry.setStatus("mandatory")


class _MscLpEth100LtPrtCfgTData_Type(AsciiString):
    """Custom type mscLpEth100LtPrtCfgTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtPrtCfgTData_Type.__name__ = "AsciiString"
_MscLpEth100LtPrtCfgTData_Object = MibTableColumn
mscLpEth100LtPrtCfgTData = _MscLpEth100LtPrtCfgTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 4, 10, 1, 1),
    _MscLpEth100LtPrtCfgTData_Type()
)
mscLpEth100LtPrtCfgTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtPrtCfgTData.setStatus("mandatory")
_MscLpEth100LtFb_ObjectIdentity = ObjectIdentity
mscLpEth100LtFb = _MscLpEth100LtFb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5)
)
_MscLpEth100LtFbRowStatusTable_Object = MibTable
mscLpEth100LtFbRowStatusTable = _MscLpEth100LtFbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbRowStatusEntry = _MscLpEth100LtFbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 1, 1)
)
mscLpEth100LtFbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbRowStatus_Type = RowStatus
_MscLpEth100LtFbRowStatus_Object = MibTableColumn
mscLpEth100LtFbRowStatus = _MscLpEth100LtFbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 1, 1, 1),
    _MscLpEth100LtFbRowStatus_Type()
)
mscLpEth100LtFbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbRowStatus.setStatus("mandatory")
_MscLpEth100LtFbComponentName_Type = DisplayString
_MscLpEth100LtFbComponentName_Object = MibTableColumn
mscLpEth100LtFbComponentName = _MscLpEth100LtFbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 1, 1, 2),
    _MscLpEth100LtFbComponentName_Type()
)
mscLpEth100LtFbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbComponentName.setStatus("mandatory")
_MscLpEth100LtFbStorageType_Type = StorageType
_MscLpEth100LtFbStorageType_Object = MibTableColumn
mscLpEth100LtFbStorageType = _MscLpEth100LtFbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 1, 1, 4),
    _MscLpEth100LtFbStorageType_Type()
)
mscLpEth100LtFbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbStorageType.setStatus("mandatory")
_MscLpEth100LtFbIndex_Type = NonReplicated
_MscLpEth100LtFbIndex_Object = MibTableColumn
mscLpEth100LtFbIndex = _MscLpEth100LtFbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 1, 1, 10),
    _MscLpEth100LtFbIndex_Type()
)
mscLpEth100LtFbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIndex.setStatus("mandatory")
_MscLpEth100LtFbTxInfo_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbTxInfo = _MscLpEth100LtFbTxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2)
)
_MscLpEth100LtFbTxInfoRowStatusTable_Object = MibTable
mscLpEth100LtFbTxInfoRowStatusTable = _MscLpEth100LtFbTxInfoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbTxInfoRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbTxInfoRowStatusEntry = _MscLpEth100LtFbTxInfoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 1, 1)
)
mscLpEth100LtFbTxInfoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbTxInfoRowStatus_Type = RowStatus
_MscLpEth100LtFbTxInfoRowStatus_Object = MibTableColumn
mscLpEth100LtFbTxInfoRowStatus = _MscLpEth100LtFbTxInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 1, 1, 1),
    _MscLpEth100LtFbTxInfoRowStatus_Type()
)
mscLpEth100LtFbTxInfoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoRowStatus.setStatus("mandatory")
_MscLpEth100LtFbTxInfoComponentName_Type = DisplayString
_MscLpEth100LtFbTxInfoComponentName_Object = MibTableColumn
mscLpEth100LtFbTxInfoComponentName = _MscLpEth100LtFbTxInfoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 1, 1, 2),
    _MscLpEth100LtFbTxInfoComponentName_Type()
)
mscLpEth100LtFbTxInfoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoComponentName.setStatus("mandatory")
_MscLpEth100LtFbTxInfoStorageType_Type = StorageType
_MscLpEth100LtFbTxInfoStorageType_Object = MibTableColumn
mscLpEth100LtFbTxInfoStorageType = _MscLpEth100LtFbTxInfoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 1, 1, 4),
    _MscLpEth100LtFbTxInfoStorageType_Type()
)
mscLpEth100LtFbTxInfoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoStorageType.setStatus("mandatory")
_MscLpEth100LtFbTxInfoIndex_Type = NonReplicated
_MscLpEth100LtFbTxInfoIndex_Object = MibTableColumn
mscLpEth100LtFbTxInfoIndex = _MscLpEth100LtFbTxInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 1, 1, 10),
    _MscLpEth100LtFbTxInfoIndex_Type()
)
mscLpEth100LtFbTxInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoIndex.setStatus("mandatory")
_MscLpEth100LtFbTxInfoTopTable_Object = MibTable
mscLpEth100LtFbTxInfoTopTable = _MscLpEth100LtFbTxInfoTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoTopTable.setStatus("mandatory")
_MscLpEth100LtFbTxInfoTopEntry_Object = MibTableRow
mscLpEth100LtFbTxInfoTopEntry = _MscLpEth100LtFbTxInfoTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 10, 1)
)
mscLpEth100LtFbTxInfoTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbTxInfoIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbTxInfoTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbTxInfoTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbTxInfoTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbTxInfoTData_Object = MibTableColumn
mscLpEth100LtFbTxInfoTData = _MscLpEth100LtFbTxInfoTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 2, 10, 1, 1),
    _MscLpEth100LtFbTxInfoTData_Type()
)
mscLpEth100LtFbTxInfoTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbTxInfoTData.setStatus("mandatory")
_MscLpEth100LtFbFddiMac_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbFddiMac = _MscLpEth100LtFbFddiMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3)
)
_MscLpEth100LtFbFddiMacRowStatusTable_Object = MibTable
mscLpEth100LtFbFddiMacRowStatusTable = _MscLpEth100LtFbFddiMacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbFddiMacRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbFddiMacRowStatusEntry = _MscLpEth100LtFbFddiMacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 1, 1)
)
mscLpEth100LtFbFddiMacRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbFddiMacRowStatus_Type = RowStatus
_MscLpEth100LtFbFddiMacRowStatus_Object = MibTableColumn
mscLpEth100LtFbFddiMacRowStatus = _MscLpEth100LtFbFddiMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 1, 1, 1),
    _MscLpEth100LtFbFddiMacRowStatus_Type()
)
mscLpEth100LtFbFddiMacRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacRowStatus.setStatus("mandatory")
_MscLpEth100LtFbFddiMacComponentName_Type = DisplayString
_MscLpEth100LtFbFddiMacComponentName_Object = MibTableColumn
mscLpEth100LtFbFddiMacComponentName = _MscLpEth100LtFbFddiMacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 1, 1, 2),
    _MscLpEth100LtFbFddiMacComponentName_Type()
)
mscLpEth100LtFbFddiMacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacComponentName.setStatus("mandatory")
_MscLpEth100LtFbFddiMacStorageType_Type = StorageType
_MscLpEth100LtFbFddiMacStorageType_Object = MibTableColumn
mscLpEth100LtFbFddiMacStorageType = _MscLpEth100LtFbFddiMacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 1, 1, 4),
    _MscLpEth100LtFbFddiMacStorageType_Type()
)
mscLpEth100LtFbFddiMacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacStorageType.setStatus("mandatory")
_MscLpEth100LtFbFddiMacIndex_Type = NonReplicated
_MscLpEth100LtFbFddiMacIndex_Object = MibTableColumn
mscLpEth100LtFbFddiMacIndex = _MscLpEth100LtFbFddiMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 1, 1, 10),
    _MscLpEth100LtFbFddiMacIndex_Type()
)
mscLpEth100LtFbFddiMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacIndex.setStatus("mandatory")
_MscLpEth100LtFbFddiMacTopTable_Object = MibTable
mscLpEth100LtFbFddiMacTopTable = _MscLpEth100LtFbFddiMacTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacTopTable.setStatus("mandatory")
_MscLpEth100LtFbFddiMacTopEntry_Object = MibTableRow
mscLpEth100LtFbFddiMacTopEntry = _MscLpEth100LtFbFddiMacTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 10, 1)
)
mscLpEth100LtFbFddiMacTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbFddiMacIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbFddiMacTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbFddiMacTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbFddiMacTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbFddiMacTData_Object = MibTableColumn
mscLpEth100LtFbFddiMacTData = _MscLpEth100LtFbFddiMacTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 3, 10, 1, 1),
    _MscLpEth100LtFbFddiMacTData_Type()
)
mscLpEth100LtFbFddiMacTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbFddiMacTData.setStatus("mandatory")
_MscLpEth100LtFbMacEnet_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbMacEnet = _MscLpEth100LtFbMacEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4)
)
_MscLpEth100LtFbMacEnetRowStatusTable_Object = MibTable
mscLpEth100LtFbMacEnetRowStatusTable = _MscLpEth100LtFbMacEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbMacEnetRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbMacEnetRowStatusEntry = _MscLpEth100LtFbMacEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 1, 1)
)
mscLpEth100LtFbMacEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbMacEnetRowStatus_Type = RowStatus
_MscLpEth100LtFbMacEnetRowStatus_Object = MibTableColumn
mscLpEth100LtFbMacEnetRowStatus = _MscLpEth100LtFbMacEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 1, 1, 1),
    _MscLpEth100LtFbMacEnetRowStatus_Type()
)
mscLpEth100LtFbMacEnetRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetRowStatus.setStatus("mandatory")
_MscLpEth100LtFbMacEnetComponentName_Type = DisplayString
_MscLpEth100LtFbMacEnetComponentName_Object = MibTableColumn
mscLpEth100LtFbMacEnetComponentName = _MscLpEth100LtFbMacEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 1, 1, 2),
    _MscLpEth100LtFbMacEnetComponentName_Type()
)
mscLpEth100LtFbMacEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetComponentName.setStatus("mandatory")
_MscLpEth100LtFbMacEnetStorageType_Type = StorageType
_MscLpEth100LtFbMacEnetStorageType_Object = MibTableColumn
mscLpEth100LtFbMacEnetStorageType = _MscLpEth100LtFbMacEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 1, 1, 4),
    _MscLpEth100LtFbMacEnetStorageType_Type()
)
mscLpEth100LtFbMacEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetStorageType.setStatus("mandatory")
_MscLpEth100LtFbMacEnetIndex_Type = NonReplicated
_MscLpEth100LtFbMacEnetIndex_Object = MibTableColumn
mscLpEth100LtFbMacEnetIndex = _MscLpEth100LtFbMacEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 1, 1, 10),
    _MscLpEth100LtFbMacEnetIndex_Type()
)
mscLpEth100LtFbMacEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetIndex.setStatus("mandatory")
_MscLpEth100LtFbMacEnetTopTable_Object = MibTable
mscLpEth100LtFbMacEnetTopTable = _MscLpEth100LtFbMacEnetTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetTopTable.setStatus("mandatory")
_MscLpEth100LtFbMacEnetTopEntry_Object = MibTableRow
mscLpEth100LtFbMacEnetTopEntry = _MscLpEth100LtFbMacEnetTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 10, 1)
)
mscLpEth100LtFbMacEnetTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbMacEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbMacEnetTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbMacEnetTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbMacEnetTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbMacEnetTData_Object = MibTableColumn
mscLpEth100LtFbMacEnetTData = _MscLpEth100LtFbMacEnetTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 4, 10, 1, 1),
    _MscLpEth100LtFbMacEnetTData_Type()
)
mscLpEth100LtFbMacEnetTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacEnetTData.setStatus("mandatory")
_MscLpEth100LtFbMacTr_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbMacTr = _MscLpEth100LtFbMacTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5)
)
_MscLpEth100LtFbMacTrRowStatusTable_Object = MibTable
mscLpEth100LtFbMacTrRowStatusTable = _MscLpEth100LtFbMacTrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbMacTrRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbMacTrRowStatusEntry = _MscLpEth100LtFbMacTrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 1, 1)
)
mscLpEth100LtFbMacTrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbMacTrRowStatus_Type = RowStatus
_MscLpEth100LtFbMacTrRowStatus_Object = MibTableColumn
mscLpEth100LtFbMacTrRowStatus = _MscLpEth100LtFbMacTrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 1, 1, 1),
    _MscLpEth100LtFbMacTrRowStatus_Type()
)
mscLpEth100LtFbMacTrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrRowStatus.setStatus("mandatory")
_MscLpEth100LtFbMacTrComponentName_Type = DisplayString
_MscLpEth100LtFbMacTrComponentName_Object = MibTableColumn
mscLpEth100LtFbMacTrComponentName = _MscLpEth100LtFbMacTrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 1, 1, 2),
    _MscLpEth100LtFbMacTrComponentName_Type()
)
mscLpEth100LtFbMacTrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrComponentName.setStatus("mandatory")
_MscLpEth100LtFbMacTrStorageType_Type = StorageType
_MscLpEth100LtFbMacTrStorageType_Object = MibTableColumn
mscLpEth100LtFbMacTrStorageType = _MscLpEth100LtFbMacTrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 1, 1, 4),
    _MscLpEth100LtFbMacTrStorageType_Type()
)
mscLpEth100LtFbMacTrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrStorageType.setStatus("mandatory")
_MscLpEth100LtFbMacTrIndex_Type = NonReplicated
_MscLpEth100LtFbMacTrIndex_Object = MibTableColumn
mscLpEth100LtFbMacTrIndex = _MscLpEth100LtFbMacTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 1, 1, 10),
    _MscLpEth100LtFbMacTrIndex_Type()
)
mscLpEth100LtFbMacTrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrIndex.setStatus("mandatory")
_MscLpEth100LtFbMacTrTopTable_Object = MibTable
mscLpEth100LtFbMacTrTopTable = _MscLpEth100LtFbMacTrTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrTopTable.setStatus("mandatory")
_MscLpEth100LtFbMacTrTopEntry_Object = MibTableRow
mscLpEth100LtFbMacTrTopEntry = _MscLpEth100LtFbMacTrTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 10, 1)
)
mscLpEth100LtFbMacTrTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbMacTrIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbMacTrTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbMacTrTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbMacTrTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbMacTrTData_Object = MibTableColumn
mscLpEth100LtFbMacTrTData = _MscLpEth100LtFbMacTrTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 5, 10, 1, 1),
    _MscLpEth100LtFbMacTrTData_Type()
)
mscLpEth100LtFbMacTrTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbMacTrTData.setStatus("mandatory")
_MscLpEth100LtFbData_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbData = _MscLpEth100LtFbData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6)
)
_MscLpEth100LtFbDataRowStatusTable_Object = MibTable
mscLpEth100LtFbDataRowStatusTable = _MscLpEth100LtFbDataRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbDataRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbDataRowStatusEntry = _MscLpEth100LtFbDataRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 1, 1)
)
mscLpEth100LtFbDataRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbDataRowStatus_Type = RowStatus
_MscLpEth100LtFbDataRowStatus_Object = MibTableColumn
mscLpEth100LtFbDataRowStatus = _MscLpEth100LtFbDataRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 1, 1, 1),
    _MscLpEth100LtFbDataRowStatus_Type()
)
mscLpEth100LtFbDataRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataRowStatus.setStatus("mandatory")
_MscLpEth100LtFbDataComponentName_Type = DisplayString
_MscLpEth100LtFbDataComponentName_Object = MibTableColumn
mscLpEth100LtFbDataComponentName = _MscLpEth100LtFbDataComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 1, 1, 2),
    _MscLpEth100LtFbDataComponentName_Type()
)
mscLpEth100LtFbDataComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataComponentName.setStatus("mandatory")
_MscLpEth100LtFbDataStorageType_Type = StorageType
_MscLpEth100LtFbDataStorageType_Object = MibTableColumn
mscLpEth100LtFbDataStorageType = _MscLpEth100LtFbDataStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 1, 1, 4),
    _MscLpEth100LtFbDataStorageType_Type()
)
mscLpEth100LtFbDataStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataStorageType.setStatus("mandatory")
_MscLpEth100LtFbDataIndex_Type = NonReplicated
_MscLpEth100LtFbDataIndex_Object = MibTableColumn
mscLpEth100LtFbDataIndex = _MscLpEth100LtFbDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 1, 1, 10),
    _MscLpEth100LtFbDataIndex_Type()
)
mscLpEth100LtFbDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataIndex.setStatus("mandatory")
_MscLpEth100LtFbDataTopTable_Object = MibTable
mscLpEth100LtFbDataTopTable = _MscLpEth100LtFbDataTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataTopTable.setStatus("mandatory")
_MscLpEth100LtFbDataTopEntry_Object = MibTableRow
mscLpEth100LtFbDataTopEntry = _MscLpEth100LtFbDataTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 10, 1)
)
mscLpEth100LtFbDataTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbDataIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbDataTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbDataTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbDataTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbDataTData_Object = MibTableColumn
mscLpEth100LtFbDataTData = _MscLpEth100LtFbDataTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 6, 10, 1, 1),
    _MscLpEth100LtFbDataTData_Type()
)
mscLpEth100LtFbDataTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbDataTData.setStatus("mandatory")
_MscLpEth100LtFbIpH_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbIpH = _MscLpEth100LtFbIpH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7)
)
_MscLpEth100LtFbIpHRowStatusTable_Object = MibTable
mscLpEth100LtFbIpHRowStatusTable = _MscLpEth100LtFbIpHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbIpHRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbIpHRowStatusEntry = _MscLpEth100LtFbIpHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 1, 1)
)
mscLpEth100LtFbIpHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbIpHRowStatus_Type = RowStatus
_MscLpEth100LtFbIpHRowStatus_Object = MibTableColumn
mscLpEth100LtFbIpHRowStatus = _MscLpEth100LtFbIpHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 1, 1, 1),
    _MscLpEth100LtFbIpHRowStatus_Type()
)
mscLpEth100LtFbIpHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHRowStatus.setStatus("mandatory")
_MscLpEth100LtFbIpHComponentName_Type = DisplayString
_MscLpEth100LtFbIpHComponentName_Object = MibTableColumn
mscLpEth100LtFbIpHComponentName = _MscLpEth100LtFbIpHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 1, 1, 2),
    _MscLpEth100LtFbIpHComponentName_Type()
)
mscLpEth100LtFbIpHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHComponentName.setStatus("mandatory")
_MscLpEth100LtFbIpHStorageType_Type = StorageType
_MscLpEth100LtFbIpHStorageType_Object = MibTableColumn
mscLpEth100LtFbIpHStorageType = _MscLpEth100LtFbIpHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 1, 1, 4),
    _MscLpEth100LtFbIpHStorageType_Type()
)
mscLpEth100LtFbIpHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHStorageType.setStatus("mandatory")
_MscLpEth100LtFbIpHIndex_Type = NonReplicated
_MscLpEth100LtFbIpHIndex_Object = MibTableColumn
mscLpEth100LtFbIpHIndex = _MscLpEth100LtFbIpHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 1, 1, 10),
    _MscLpEth100LtFbIpHIndex_Type()
)
mscLpEth100LtFbIpHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHIndex.setStatus("mandatory")
_MscLpEth100LtFbIpHTopTable_Object = MibTable
mscLpEth100LtFbIpHTopTable = _MscLpEth100LtFbIpHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHTopTable.setStatus("mandatory")
_MscLpEth100LtFbIpHTopEntry_Object = MibTableRow
mscLpEth100LtFbIpHTopEntry = _MscLpEth100LtFbIpHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 10, 1)
)
mscLpEth100LtFbIpHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIpHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbIpHTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbIpHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbIpHTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbIpHTData_Object = MibTableColumn
mscLpEth100LtFbIpHTData = _MscLpEth100LtFbIpHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 7, 10, 1, 1),
    _MscLpEth100LtFbIpHTData_Type()
)
mscLpEth100LtFbIpHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpHTData.setStatus("mandatory")
_MscLpEth100LtFbLlch_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbLlch = _MscLpEth100LtFbLlch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8)
)
_MscLpEth100LtFbLlchRowStatusTable_Object = MibTable
mscLpEth100LtFbLlchRowStatusTable = _MscLpEth100LtFbLlchRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbLlchRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbLlchRowStatusEntry = _MscLpEth100LtFbLlchRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 1, 1)
)
mscLpEth100LtFbLlchRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbLlchRowStatus_Type = RowStatus
_MscLpEth100LtFbLlchRowStatus_Object = MibTableColumn
mscLpEth100LtFbLlchRowStatus = _MscLpEth100LtFbLlchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 1, 1, 1),
    _MscLpEth100LtFbLlchRowStatus_Type()
)
mscLpEth100LtFbLlchRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchRowStatus.setStatus("mandatory")
_MscLpEth100LtFbLlchComponentName_Type = DisplayString
_MscLpEth100LtFbLlchComponentName_Object = MibTableColumn
mscLpEth100LtFbLlchComponentName = _MscLpEth100LtFbLlchComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 1, 1, 2),
    _MscLpEth100LtFbLlchComponentName_Type()
)
mscLpEth100LtFbLlchComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchComponentName.setStatus("mandatory")
_MscLpEth100LtFbLlchStorageType_Type = StorageType
_MscLpEth100LtFbLlchStorageType_Object = MibTableColumn
mscLpEth100LtFbLlchStorageType = _MscLpEth100LtFbLlchStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 1, 1, 4),
    _MscLpEth100LtFbLlchStorageType_Type()
)
mscLpEth100LtFbLlchStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchStorageType.setStatus("mandatory")
_MscLpEth100LtFbLlchIndex_Type = NonReplicated
_MscLpEth100LtFbLlchIndex_Object = MibTableColumn
mscLpEth100LtFbLlchIndex = _MscLpEth100LtFbLlchIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 1, 1, 10),
    _MscLpEth100LtFbLlchIndex_Type()
)
mscLpEth100LtFbLlchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchIndex.setStatus("mandatory")
_MscLpEth100LtFbLlchTopTable_Object = MibTable
mscLpEth100LtFbLlchTopTable = _MscLpEth100LtFbLlchTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchTopTable.setStatus("mandatory")
_MscLpEth100LtFbLlchTopEntry_Object = MibTableRow
mscLpEth100LtFbLlchTopEntry = _MscLpEth100LtFbLlchTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 10, 1)
)
mscLpEth100LtFbLlchTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbLlchIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbLlchTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbLlchTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbLlchTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbLlchTData_Object = MibTableColumn
mscLpEth100LtFbLlchTData = _MscLpEth100LtFbLlchTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 8, 10, 1, 1),
    _MscLpEth100LtFbLlchTData_Type()
)
mscLpEth100LtFbLlchTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbLlchTData.setStatus("mandatory")
_MscLpEth100LtFbAppleH_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbAppleH = _MscLpEth100LtFbAppleH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9)
)
_MscLpEth100LtFbAppleHRowStatusTable_Object = MibTable
mscLpEth100LtFbAppleHRowStatusTable = _MscLpEth100LtFbAppleHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbAppleHRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbAppleHRowStatusEntry = _MscLpEth100LtFbAppleHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 1, 1)
)
mscLpEth100LtFbAppleHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbAppleHRowStatus_Type = RowStatus
_MscLpEth100LtFbAppleHRowStatus_Object = MibTableColumn
mscLpEth100LtFbAppleHRowStatus = _MscLpEth100LtFbAppleHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 1, 1, 1),
    _MscLpEth100LtFbAppleHRowStatus_Type()
)
mscLpEth100LtFbAppleHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHRowStatus.setStatus("mandatory")
_MscLpEth100LtFbAppleHComponentName_Type = DisplayString
_MscLpEth100LtFbAppleHComponentName_Object = MibTableColumn
mscLpEth100LtFbAppleHComponentName = _MscLpEth100LtFbAppleHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 1, 1, 2),
    _MscLpEth100LtFbAppleHComponentName_Type()
)
mscLpEth100LtFbAppleHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHComponentName.setStatus("mandatory")
_MscLpEth100LtFbAppleHStorageType_Type = StorageType
_MscLpEth100LtFbAppleHStorageType_Object = MibTableColumn
mscLpEth100LtFbAppleHStorageType = _MscLpEth100LtFbAppleHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 1, 1, 4),
    _MscLpEth100LtFbAppleHStorageType_Type()
)
mscLpEth100LtFbAppleHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHStorageType.setStatus("mandatory")
_MscLpEth100LtFbAppleHIndex_Type = NonReplicated
_MscLpEth100LtFbAppleHIndex_Object = MibTableColumn
mscLpEth100LtFbAppleHIndex = _MscLpEth100LtFbAppleHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 1, 1, 10),
    _MscLpEth100LtFbAppleHIndex_Type()
)
mscLpEth100LtFbAppleHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHIndex.setStatus("mandatory")
_MscLpEth100LtFbAppleHTopTable_Object = MibTable
mscLpEth100LtFbAppleHTopTable = _MscLpEth100LtFbAppleHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHTopTable.setStatus("mandatory")
_MscLpEth100LtFbAppleHTopEntry_Object = MibTableRow
mscLpEth100LtFbAppleHTopEntry = _MscLpEth100LtFbAppleHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 10, 1)
)
mscLpEth100LtFbAppleHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbAppleHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbAppleHTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbAppleHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbAppleHTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbAppleHTData_Object = MibTableColumn
mscLpEth100LtFbAppleHTData = _MscLpEth100LtFbAppleHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 9, 10, 1, 1),
    _MscLpEth100LtFbAppleHTData_Type()
)
mscLpEth100LtFbAppleHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbAppleHTData.setStatus("mandatory")
_MscLpEth100LtFbIpxH_ObjectIdentity = ObjectIdentity
mscLpEth100LtFbIpxH = _MscLpEth100LtFbIpxH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10)
)
_MscLpEth100LtFbIpxHRowStatusTable_Object = MibTable
mscLpEth100LtFbIpxHRowStatusTable = _MscLpEth100LtFbIpxHRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHRowStatusTable.setStatus("mandatory")
_MscLpEth100LtFbIpxHRowStatusEntry_Object = MibTableRow
mscLpEth100LtFbIpxHRowStatusEntry = _MscLpEth100LtFbIpxHRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 1, 1)
)
mscLpEth100LtFbIpxHRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtFbIpxHRowStatus_Type = RowStatus
_MscLpEth100LtFbIpxHRowStatus_Object = MibTableColumn
mscLpEth100LtFbIpxHRowStatus = _MscLpEth100LtFbIpxHRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 1, 1, 1),
    _MscLpEth100LtFbIpxHRowStatus_Type()
)
mscLpEth100LtFbIpxHRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHRowStatus.setStatus("mandatory")
_MscLpEth100LtFbIpxHComponentName_Type = DisplayString
_MscLpEth100LtFbIpxHComponentName_Object = MibTableColumn
mscLpEth100LtFbIpxHComponentName = _MscLpEth100LtFbIpxHComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 1, 1, 2),
    _MscLpEth100LtFbIpxHComponentName_Type()
)
mscLpEth100LtFbIpxHComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHComponentName.setStatus("mandatory")
_MscLpEth100LtFbIpxHStorageType_Type = StorageType
_MscLpEth100LtFbIpxHStorageType_Object = MibTableColumn
mscLpEth100LtFbIpxHStorageType = _MscLpEth100LtFbIpxHStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 1, 1, 4),
    _MscLpEth100LtFbIpxHStorageType_Type()
)
mscLpEth100LtFbIpxHStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHStorageType.setStatus("mandatory")
_MscLpEth100LtFbIpxHIndex_Type = NonReplicated
_MscLpEth100LtFbIpxHIndex_Object = MibTableColumn
mscLpEth100LtFbIpxHIndex = _MscLpEth100LtFbIpxHIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 1, 1, 10),
    _MscLpEth100LtFbIpxHIndex_Type()
)
mscLpEth100LtFbIpxHIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHIndex.setStatus("mandatory")
_MscLpEth100LtFbIpxHTopTable_Object = MibTable
mscLpEth100LtFbIpxHTopTable = _MscLpEth100LtFbIpxHTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHTopTable.setStatus("mandatory")
_MscLpEth100LtFbIpxHTopEntry_Object = MibTableRow
mscLpEth100LtFbIpxHTopEntry = _MscLpEth100LtFbIpxHTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 10, 1)
)
mscLpEth100LtFbIpxHTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIpxHIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbIpxHTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbIpxHTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbIpxHTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbIpxHTData_Object = MibTableColumn
mscLpEth100LtFbIpxHTData = _MscLpEth100LtFbIpxHTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 10, 10, 1, 1),
    _MscLpEth100LtFbIpxHTData_Type()
)
mscLpEth100LtFbIpxHTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbIpxHTData.setStatus("mandatory")
_MscLpEth100LtFbTopTable_Object = MibTable
mscLpEth100LtFbTopTable = _MscLpEth100LtFbTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 20)
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbTopTable.setStatus("mandatory")
_MscLpEth100LtFbTopEntry_Object = MibTableRow
mscLpEth100LtFbTopEntry = _MscLpEth100LtFbTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 20, 1)
)
mscLpEth100LtFbTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtFbIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtFbTopEntry.setStatus("mandatory")


class _MscLpEth100LtFbTData_Type(AsciiString):
    """Custom type mscLpEth100LtFbTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtFbTData_Type.__name__ = "AsciiString"
_MscLpEth100LtFbTData_Object = MibTableColumn
mscLpEth100LtFbTData = _MscLpEth100LtFbTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 5, 20, 1, 1),
    _MscLpEth100LtFbTData_Type()
)
mscLpEth100LtFbTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtFbTData.setStatus("mandatory")
_MscLpEth100LtCntl_ObjectIdentity = ObjectIdentity
mscLpEth100LtCntl = _MscLpEth100LtCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6)
)
_MscLpEth100LtCntlRowStatusTable_Object = MibTable
mscLpEth100LtCntlRowStatusTable = _MscLpEth100LtCntlRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100LtCntlRowStatusTable.setStatus("mandatory")
_MscLpEth100LtCntlRowStatusEntry_Object = MibTableRow
mscLpEth100LtCntlRowStatusEntry = _MscLpEth100LtCntlRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 1, 1)
)
mscLpEth100LtCntlRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtCntlRowStatusEntry.setStatus("mandatory")
_MscLpEth100LtCntlRowStatus_Type = RowStatus
_MscLpEth100LtCntlRowStatus_Object = MibTableColumn
mscLpEth100LtCntlRowStatus = _MscLpEth100LtCntlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 1, 1, 1),
    _MscLpEth100LtCntlRowStatus_Type()
)
mscLpEth100LtCntlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtCntlRowStatus.setStatus("mandatory")
_MscLpEth100LtCntlComponentName_Type = DisplayString
_MscLpEth100LtCntlComponentName_Object = MibTableColumn
mscLpEth100LtCntlComponentName = _MscLpEth100LtCntlComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 1, 1, 2),
    _MscLpEth100LtCntlComponentName_Type()
)
mscLpEth100LtCntlComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtCntlComponentName.setStatus("mandatory")
_MscLpEth100LtCntlStorageType_Type = StorageType
_MscLpEth100LtCntlStorageType_Object = MibTableColumn
mscLpEth100LtCntlStorageType = _MscLpEth100LtCntlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 1, 1, 4),
    _MscLpEth100LtCntlStorageType_Type()
)
mscLpEth100LtCntlStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LtCntlStorageType.setStatus("mandatory")
_MscLpEth100LtCntlIndex_Type = NonReplicated
_MscLpEth100LtCntlIndex_Object = MibTableColumn
mscLpEth100LtCntlIndex = _MscLpEth100LtCntlIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 1, 1, 10),
    _MscLpEth100LtCntlIndex_Type()
)
mscLpEth100LtCntlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100LtCntlIndex.setStatus("mandatory")
_MscLpEth100LtCntlTopTable_Object = MibTable
mscLpEth100LtCntlTopTable = _MscLpEth100LtCntlTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100LtCntlTopTable.setStatus("mandatory")
_MscLpEth100LtCntlTopEntry_Object = MibTableRow
mscLpEth100LtCntlTopEntry = _MscLpEth100LtCntlTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 10, 1)
)
mscLpEth100LtCntlTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtCntlIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtCntlTopEntry.setStatus("mandatory")


class _MscLpEth100LtCntlTData_Type(AsciiString):
    """Custom type mscLpEth100LtCntlTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtCntlTData_Type.__name__ = "AsciiString"
_MscLpEth100LtCntlTData_Object = MibTableColumn
mscLpEth100LtCntlTData = _MscLpEth100LtCntlTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 6, 10, 1, 1),
    _MscLpEth100LtCntlTData_Type()
)
mscLpEth100LtCntlTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtCntlTData.setStatus("mandatory")
_MscLpEth100LtTopTable_Object = MibTable
mscLpEth100LtTopTable = _MscLpEth100LtTopTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 20)
)
if mibBuilder.loadTexts:
    mscLpEth100LtTopTable.setStatus("mandatory")
_MscLpEth100LtTopEntry_Object = MibTableRow
mscLpEth100LtTopEntry = _MscLpEth100LtTopEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 20, 1)
)
mscLpEth100LtTopEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100LtIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100LtTopEntry.setStatus("mandatory")


class _MscLpEth100LtTData_Type(AsciiString):
    """Custom type mscLpEth100LtTData based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscLpEth100LtTData_Type.__name__ = "AsciiString"
_MscLpEth100LtTData_Object = MibTableColumn
mscLpEth100LtTData = _MscLpEth100LtTData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 2, 20, 1, 1),
    _MscLpEth100LtTData_Type()
)
mscLpEth100LtTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LtTData.setStatus("mandatory")
_MscLpEth100Test_ObjectIdentity = ObjectIdentity
mscLpEth100Test = _MscLpEth100Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3)
)
_MscLpEth100TestRowStatusTable_Object = MibTable
mscLpEth100TestRowStatusTable = _MscLpEth100TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpEth100TestRowStatusTable.setStatus("mandatory")
_MscLpEth100TestRowStatusEntry_Object = MibTableRow
mscLpEth100TestRowStatusEntry = _MscLpEth100TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 1, 1)
)
mscLpEth100TestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100TestIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100TestRowStatusEntry.setStatus("mandatory")
_MscLpEth100TestRowStatus_Type = RowStatus
_MscLpEth100TestRowStatus_Object = MibTableColumn
mscLpEth100TestRowStatus = _MscLpEth100TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 1, 1, 1),
    _MscLpEth100TestRowStatus_Type()
)
mscLpEth100TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestRowStatus.setStatus("mandatory")
_MscLpEth100TestComponentName_Type = DisplayString
_MscLpEth100TestComponentName_Object = MibTableColumn
mscLpEth100TestComponentName = _MscLpEth100TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 1, 1, 2),
    _MscLpEth100TestComponentName_Type()
)
mscLpEth100TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestComponentName.setStatus("mandatory")
_MscLpEth100TestStorageType_Type = StorageType
_MscLpEth100TestStorageType_Object = MibTableColumn
mscLpEth100TestStorageType = _MscLpEth100TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 1, 1, 4),
    _MscLpEth100TestStorageType_Type()
)
mscLpEth100TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestStorageType.setStatus("mandatory")
_MscLpEth100TestIndex_Type = NonReplicated
_MscLpEth100TestIndex_Object = MibTableColumn
mscLpEth100TestIndex = _MscLpEth100TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 1, 1, 10),
    _MscLpEth100TestIndex_Type()
)
mscLpEth100TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpEth100TestIndex.setStatus("mandatory")
_MscLpEth100TestPTOTable_Object = MibTable
mscLpEth100TestPTOTable = _MscLpEth100TestPTOTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100TestPTOTable.setStatus("mandatory")
_MscLpEth100TestPTOEntry_Object = MibTableRow
mscLpEth100TestPTOEntry = _MscLpEth100TestPTOEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 10, 1)
)
mscLpEth100TestPTOEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100TestIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100TestPTOEntry.setStatus("mandatory")


class _MscLpEth100TestType_Type(Integer32):
    """Custom type mscLpEth100TestType based on Integer32"""
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


_MscLpEth100TestType_Type.__name__ = "Integer32"
_MscLpEth100TestType_Object = MibTableColumn
mscLpEth100TestType = _MscLpEth100TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 10, 1, 1),
    _MscLpEth100TestType_Type()
)
mscLpEth100TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100TestType.setStatus("mandatory")


class _MscLpEth100TestFrmSize_Type(Unsigned32):
    """Custom type mscLpEth100TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscLpEth100TestFrmSize_Type.__name__ = "Unsigned32"
_MscLpEth100TestFrmSize_Object = MibTableColumn
mscLpEth100TestFrmSize = _MscLpEth100TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 10, 1, 2),
    _MscLpEth100TestFrmSize_Type()
)
mscLpEth100TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100TestFrmSize.setStatus("mandatory")


class _MscLpEth100TestDuration_Type(Unsigned32):
    """Custom type mscLpEth100TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscLpEth100TestDuration_Type.__name__ = "Unsigned32"
_MscLpEth100TestDuration_Object = MibTableColumn
mscLpEth100TestDuration = _MscLpEth100TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 10, 1, 3),
    _MscLpEth100TestDuration_Type()
)
mscLpEth100TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100TestDuration.setStatus("mandatory")
_MscLpEth100TestResultsTable_Object = MibTable
mscLpEth100TestResultsTable = _MscLpEth100TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11)
)
if mibBuilder.loadTexts:
    mscLpEth100TestResultsTable.setStatus("mandatory")
_MscLpEth100TestResultsEntry_Object = MibTableRow
mscLpEth100TestResultsEntry = _MscLpEth100TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1)
)
mscLpEth100TestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100TestIndex"),
)
if mibBuilder.loadTexts:
    mscLpEth100TestResultsEntry.setStatus("mandatory")
_MscLpEth100TestElapsedTime_Type = Counter32
_MscLpEth100TestElapsedTime_Object = MibTableColumn
mscLpEth100TestElapsedTime = _MscLpEth100TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 4),
    _MscLpEth100TestElapsedTime_Type()
)
mscLpEth100TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestElapsedTime.setStatus("mandatory")


class _MscLpEth100TestTimeRemaining_Type(Unsigned32):
    """Custom type mscLpEth100TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpEth100TestTimeRemaining_Type.__name__ = "Unsigned32"
_MscLpEth100TestTimeRemaining_Object = MibTableColumn
mscLpEth100TestTimeRemaining = _MscLpEth100TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 5),
    _MscLpEth100TestTimeRemaining_Type()
)
mscLpEth100TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestTimeRemaining.setStatus("mandatory")


class _MscLpEth100TestCauseOfTermination_Type(Integer32):
    """Custom type mscLpEth100TestCauseOfTermination based on Integer32"""
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


_MscLpEth100TestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpEth100TestCauseOfTermination_Object = MibTableColumn
mscLpEth100TestCauseOfTermination = _MscLpEth100TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 6),
    _MscLpEth100TestCauseOfTermination_Type()
)
mscLpEth100TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestCauseOfTermination.setStatus("mandatory")
_MscLpEth100TestFrmTx_Type = PassportCounter64
_MscLpEth100TestFrmTx_Object = MibTableColumn
mscLpEth100TestFrmTx = _MscLpEth100TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 7),
    _MscLpEth100TestFrmTx_Type()
)
mscLpEth100TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestFrmTx.setStatus("mandatory")
_MscLpEth100TestBitsTx_Type = PassportCounter64
_MscLpEth100TestBitsTx_Object = MibTableColumn
mscLpEth100TestBitsTx = _MscLpEth100TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 8),
    _MscLpEth100TestBitsTx_Type()
)
mscLpEth100TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestBitsTx.setStatus("mandatory")
_MscLpEth100TestFrmRx_Type = PassportCounter64
_MscLpEth100TestFrmRx_Object = MibTableColumn
mscLpEth100TestFrmRx = _MscLpEth100TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 9),
    _MscLpEth100TestFrmRx_Type()
)
mscLpEth100TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestFrmRx.setStatus("mandatory")
_MscLpEth100TestBitsRx_Type = PassportCounter64
_MscLpEth100TestBitsRx_Object = MibTableColumn
mscLpEth100TestBitsRx = _MscLpEth100TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 10),
    _MscLpEth100TestBitsRx_Type()
)
mscLpEth100TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestBitsRx.setStatus("mandatory")
_MscLpEth100TestErroredFrmRx_Type = PassportCounter64
_MscLpEth100TestErroredFrmRx_Object = MibTableColumn
mscLpEth100TestErroredFrmRx = _MscLpEth100TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 3, 11, 1, 11),
    _MscLpEth100TestErroredFrmRx_Type()
)
mscLpEth100TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100TestErroredFrmRx.setStatus("mandatory")
_MscLpEth100CidDataTable_Object = MibTable
mscLpEth100CidDataTable = _MscLpEth100CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 10)
)
if mibBuilder.loadTexts:
    mscLpEth100CidDataTable.setStatus("mandatory")
_MscLpEth100CidDataEntry_Object = MibTableRow
mscLpEth100CidDataEntry = _MscLpEth100CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 10, 1)
)
mscLpEth100CidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100CidDataEntry.setStatus("mandatory")


class _MscLpEth100CustomerIdentifier_Type(Unsigned32):
    """Custom type mscLpEth100CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLpEth100CustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLpEth100CustomerIdentifier_Object = MibTableColumn
mscLpEth100CustomerIdentifier = _MscLpEth100CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 10, 1, 1),
    _MscLpEth100CustomerIdentifier_Type()
)
mscLpEth100CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100CustomerIdentifier.setStatus("mandatory")
_MscLpEth100IfEntryTable_Object = MibTable
mscLpEth100IfEntryTable = _MscLpEth100IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 11)
)
if mibBuilder.loadTexts:
    mscLpEth100IfEntryTable.setStatus("mandatory")
_MscLpEth100IfEntryEntry_Object = MibTableRow
mscLpEth100IfEntryEntry = _MscLpEth100IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 11, 1)
)
mscLpEth100IfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100IfEntryEntry.setStatus("mandatory")


class _MscLpEth100IfAdminStatus_Type(Integer32):
    """Custom type mscLpEth100IfAdminStatus based on Integer32"""
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


_MscLpEth100IfAdminStatus_Type.__name__ = "Integer32"
_MscLpEth100IfAdminStatus_Object = MibTableColumn
mscLpEth100IfAdminStatus = _MscLpEth100IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 11, 1, 1),
    _MscLpEth100IfAdminStatus_Type()
)
mscLpEth100IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100IfAdminStatus.setStatus("mandatory")


class _MscLpEth100IfIndex_Type(InterfaceIndex):
    """Custom type mscLpEth100IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLpEth100IfIndex_Type.__name__ = "InterfaceIndex"
_MscLpEth100IfIndex_Object = MibTableColumn
mscLpEth100IfIndex = _MscLpEth100IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 11, 1, 2),
    _MscLpEth100IfIndex_Type()
)
mscLpEth100IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100IfIndex.setStatus("mandatory")
_MscLpEth100ProvTable_Object = MibTable
mscLpEth100ProvTable = _MscLpEth100ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 12)
)
if mibBuilder.loadTexts:
    mscLpEth100ProvTable.setStatus("mandatory")
_MscLpEth100ProvEntry_Object = MibTableRow
mscLpEth100ProvEntry = _MscLpEth100ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 12, 1)
)
mscLpEth100ProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100ProvEntry.setStatus("mandatory")


class _MscLpEth100DuplexMode_Type(Integer32):
    """Custom type mscLpEth100DuplexMode based on Integer32"""
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


_MscLpEth100DuplexMode_Type.__name__ = "Integer32"
_MscLpEth100DuplexMode_Object = MibTableColumn
mscLpEth100DuplexMode = _MscLpEth100DuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 12, 1, 1),
    _MscLpEth100DuplexMode_Type()
)
mscLpEth100DuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100DuplexMode.setStatus("mandatory")


class _MscLpEth100LineSpeed_Type(Unsigned32):
    """Custom type mscLpEth100LineSpeed based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_MscLpEth100LineSpeed_Type.__name__ = "Unsigned32"
_MscLpEth100LineSpeed_Object = MibTableColumn
mscLpEth100LineSpeed = _MscLpEth100LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 12, 1, 2),
    _MscLpEth100LineSpeed_Type()
)
mscLpEth100LineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100LineSpeed.setStatus("mandatory")


class _MscLpEth100AutoNegotiation_Type(Integer32):
    """Custom type mscLpEth100AutoNegotiation based on Integer32"""
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


_MscLpEth100AutoNegotiation_Type.__name__ = "Integer32"
_MscLpEth100AutoNegotiation_Object = MibTableColumn
mscLpEth100AutoNegotiation = _MscLpEth100AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 12, 1, 3),
    _MscLpEth100AutoNegotiation_Type()
)
mscLpEth100AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100AutoNegotiation.setStatus("mandatory")
_MscLpEth100ApplicationFramerName_Type = Link
_MscLpEth100ApplicationFramerName_Object = MibTableColumn
mscLpEth100ApplicationFramerName = _MscLpEth100ApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 12, 1, 4),
    _MscLpEth100ApplicationFramerName_Type()
)
mscLpEth100ApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100ApplicationFramerName.setStatus("mandatory")
_MscLpEth100AdminInfoTable_Object = MibTable
mscLpEth100AdminInfoTable = _MscLpEth100AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 13)
)
if mibBuilder.loadTexts:
    mscLpEth100AdminInfoTable.setStatus("mandatory")
_MscLpEth100AdminInfoEntry_Object = MibTableRow
mscLpEth100AdminInfoEntry = _MscLpEth100AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 13, 1)
)
mscLpEth100AdminInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100AdminInfoEntry.setStatus("mandatory")


class _MscLpEth100Vendor_Type(AsciiString):
    """Custom type mscLpEth100Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLpEth100Vendor_Type.__name__ = "AsciiString"
_MscLpEth100Vendor_Object = MibTableColumn
mscLpEth100Vendor = _MscLpEth100Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 13, 1, 1),
    _MscLpEth100Vendor_Type()
)
mscLpEth100Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100Vendor.setStatus("mandatory")


class _MscLpEth100CommentText_Type(AsciiString):
    """Custom type mscLpEth100CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_MscLpEth100CommentText_Type.__name__ = "AsciiString"
_MscLpEth100CommentText_Object = MibTableColumn
mscLpEth100CommentText = _MscLpEth100CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 13, 1, 2),
    _MscLpEth100CommentText_Type()
)
mscLpEth100CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpEth100CommentText.setStatus("mandatory")
_MscLpEth100StateTable_Object = MibTable
mscLpEth100StateTable = _MscLpEth100StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 15)
)
if mibBuilder.loadTexts:
    mscLpEth100StateTable.setStatus("mandatory")
_MscLpEth100StateEntry_Object = MibTableRow
mscLpEth100StateEntry = _MscLpEth100StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 15, 1)
)
mscLpEth100StateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100StateEntry.setStatus("mandatory")


class _MscLpEth100AdminState_Type(Integer32):
    """Custom type mscLpEth100AdminState based on Integer32"""
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


_MscLpEth100AdminState_Type.__name__ = "Integer32"
_MscLpEth100AdminState_Object = MibTableColumn
mscLpEth100AdminState = _MscLpEth100AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 15, 1, 1),
    _MscLpEth100AdminState_Type()
)
mscLpEth100AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100AdminState.setStatus("mandatory")


class _MscLpEth100OperationalState_Type(Integer32):
    """Custom type mscLpEth100OperationalState based on Integer32"""
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


_MscLpEth100OperationalState_Type.__name__ = "Integer32"
_MscLpEth100OperationalState_Object = MibTableColumn
mscLpEth100OperationalState = _MscLpEth100OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 15, 1, 2),
    _MscLpEth100OperationalState_Type()
)
mscLpEth100OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100OperationalState.setStatus("mandatory")


class _MscLpEth100UsageState_Type(Integer32):
    """Custom type mscLpEth100UsageState based on Integer32"""
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


_MscLpEth100UsageState_Type.__name__ = "Integer32"
_MscLpEth100UsageState_Object = MibTableColumn
mscLpEth100UsageState = _MscLpEth100UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 15, 1, 3),
    _MscLpEth100UsageState_Type()
)
mscLpEth100UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100UsageState.setStatus("mandatory")
_MscLpEth100OperStatusTable_Object = MibTable
mscLpEth100OperStatusTable = _MscLpEth100OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 16)
)
if mibBuilder.loadTexts:
    mscLpEth100OperStatusTable.setStatus("mandatory")
_MscLpEth100OperStatusEntry_Object = MibTableRow
mscLpEth100OperStatusEntry = _MscLpEth100OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 16, 1)
)
mscLpEth100OperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100OperStatusEntry.setStatus("mandatory")


class _MscLpEth100SnmpOperStatus_Type(Integer32):
    """Custom type mscLpEth100SnmpOperStatus based on Integer32"""
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


_MscLpEth100SnmpOperStatus_Type.__name__ = "Integer32"
_MscLpEth100SnmpOperStatus_Object = MibTableColumn
mscLpEth100SnmpOperStatus = _MscLpEth100SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 16, 1, 1),
    _MscLpEth100SnmpOperStatus_Type()
)
mscLpEth100SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100SnmpOperStatus.setStatus("mandatory")
_MscLpEth100OperTable_Object = MibTable
mscLpEth100OperTable = _MscLpEth100OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 17)
)
if mibBuilder.loadTexts:
    mscLpEth100OperTable.setStatus("mandatory")
_MscLpEth100OperEntry_Object = MibTableRow
mscLpEth100OperEntry = _MscLpEth100OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 17, 1)
)
mscLpEth100OperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100OperEntry.setStatus("mandatory")


class _MscLpEth100MacAddress_Type(MacAddress):
    """Custom type mscLpEth100MacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpEth100MacAddress_Type.__name__ = "MacAddress"
_MscLpEth100MacAddress_Object = MibTableColumn
mscLpEth100MacAddress = _MscLpEth100MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 17, 1, 1),
    _MscLpEth100MacAddress_Type()
)
mscLpEth100MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100MacAddress.setStatus("mandatory")


class _MscLpEth100AutoNegStatus_Type(Integer32):
    """Custom type mscLpEth100AutoNegStatus based on Integer32"""
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


_MscLpEth100AutoNegStatus_Type.__name__ = "Integer32"
_MscLpEth100AutoNegStatus_Object = MibTableColumn
mscLpEth100AutoNegStatus = _MscLpEth100AutoNegStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 17, 1, 4),
    _MscLpEth100AutoNegStatus_Type()
)
mscLpEth100AutoNegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100AutoNegStatus.setStatus("mandatory")


class _MscLpEth100ActualLineSpeed_Type(Unsigned32):
    """Custom type mscLpEth100ActualLineSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_MscLpEth100ActualLineSpeed_Type.__name__ = "Unsigned32"
_MscLpEth100ActualLineSpeed_Object = MibTableColumn
mscLpEth100ActualLineSpeed = _MscLpEth100ActualLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 17, 1, 5),
    _MscLpEth100ActualLineSpeed_Type()
)
mscLpEth100ActualLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100ActualLineSpeed.setStatus("mandatory")


class _MscLpEth100ActualDuplexMode_Type(Integer32):
    """Custom type mscLpEth100ActualDuplexMode based on Integer32"""
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


_MscLpEth100ActualDuplexMode_Type.__name__ = "Integer32"
_MscLpEth100ActualDuplexMode_Object = MibTableColumn
mscLpEth100ActualDuplexMode = _MscLpEth100ActualDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 17, 1, 6),
    _MscLpEth100ActualDuplexMode_Type()
)
mscLpEth100ActualDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100ActualDuplexMode.setStatus("mandatory")
_MscLpEth100Eth100StatsTable_Object = MibTable
mscLpEth100Eth100StatsTable = _MscLpEth100Eth100StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18)
)
if mibBuilder.loadTexts:
    mscLpEth100Eth100StatsTable.setStatus("mandatory")
_MscLpEth100Eth100StatsEntry_Object = MibTableRow
mscLpEth100Eth100StatsEntry = _MscLpEth100Eth100StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1)
)
mscLpEth100Eth100StatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100Eth100StatsEntry.setStatus("mandatory")
_MscLpEth100FramesTransmittedOk_Type = Counter32
_MscLpEth100FramesTransmittedOk_Object = MibTableColumn
mscLpEth100FramesTransmittedOk = _MscLpEth100FramesTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1, 1),
    _MscLpEth100FramesTransmittedOk_Type()
)
mscLpEth100FramesTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100FramesTransmittedOk.setStatus("mandatory")
_MscLpEth100FramesReceivedOk_Type = Counter32
_MscLpEth100FramesReceivedOk_Object = MibTableColumn
mscLpEth100FramesReceivedOk = _MscLpEth100FramesReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1, 2),
    _MscLpEth100FramesReceivedOk_Type()
)
mscLpEth100FramesReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100FramesReceivedOk.setStatus("mandatory")
_MscLpEth100OctetsTransmittedOk_Type = Counter32
_MscLpEth100OctetsTransmittedOk_Object = MibTableColumn
mscLpEth100OctetsTransmittedOk = _MscLpEth100OctetsTransmittedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1, 3),
    _MscLpEth100OctetsTransmittedOk_Type()
)
mscLpEth100OctetsTransmittedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100OctetsTransmittedOk.setStatus("mandatory")
_MscLpEth100OctetsReceivedOk_Type = Counter32
_MscLpEth100OctetsReceivedOk_Object = MibTableColumn
mscLpEth100OctetsReceivedOk = _MscLpEth100OctetsReceivedOk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1, 4),
    _MscLpEth100OctetsReceivedOk_Type()
)
mscLpEth100OctetsReceivedOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100OctetsReceivedOk.setStatus("mandatory")
_MscLpEth100UndersizeFrames_Type = Counter32
_MscLpEth100UndersizeFrames_Object = MibTableColumn
mscLpEth100UndersizeFrames = _MscLpEth100UndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1, 5),
    _MscLpEth100UndersizeFrames_Type()
)
mscLpEth100UndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100UndersizeFrames.setStatus("mandatory")
_MscLpEth100ReceivedOctetsIntoRouterBr_Type = Counter32
_MscLpEth100ReceivedOctetsIntoRouterBr_Object = MibTableColumn
mscLpEth100ReceivedOctetsIntoRouterBr = _MscLpEth100ReceivedOctetsIntoRouterBr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1, 6),
    _MscLpEth100ReceivedOctetsIntoRouterBr_Type()
)
mscLpEth100ReceivedOctetsIntoRouterBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100ReceivedOctetsIntoRouterBr.setStatus("mandatory")
_MscLpEth100ReceivedFramesIntoRouterBr_Type = Counter32
_MscLpEth100ReceivedFramesIntoRouterBr_Object = MibTableColumn
mscLpEth100ReceivedFramesIntoRouterBr = _MscLpEth100ReceivedFramesIntoRouterBr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 18, 1, 7),
    _MscLpEth100ReceivedFramesIntoRouterBr_Type()
)
mscLpEth100ReceivedFramesIntoRouterBr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100ReceivedFramesIntoRouterBr.setStatus("mandatory")
_MscLpEth100StatsTable_Object = MibTable
mscLpEth100StatsTable = _MscLpEth100StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19)
)
if mibBuilder.loadTexts:
    mscLpEth100StatsTable.setStatus("mandatory")
_MscLpEth100StatsEntry_Object = MibTableRow
mscLpEth100StatsEntry = _MscLpEth100StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1)
)
mscLpEth100StatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLpEth100Index"),
)
if mibBuilder.loadTexts:
    mscLpEth100StatsEntry.setStatus("mandatory")
_MscLpEth100AlignmentErrors_Type = Counter32
_MscLpEth100AlignmentErrors_Object = MibTableColumn
mscLpEth100AlignmentErrors = _MscLpEth100AlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 2),
    _MscLpEth100AlignmentErrors_Type()
)
mscLpEth100AlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100AlignmentErrors.setStatus("mandatory")
_MscLpEth100FcsErrors_Type = Counter32
_MscLpEth100FcsErrors_Object = MibTableColumn
mscLpEth100FcsErrors = _MscLpEth100FcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 3),
    _MscLpEth100FcsErrors_Type()
)
mscLpEth100FcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100FcsErrors.setStatus("mandatory")
_MscLpEth100SingleCollisionFrames_Type = Counter32
_MscLpEth100SingleCollisionFrames_Object = MibTableColumn
mscLpEth100SingleCollisionFrames = _MscLpEth100SingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 4),
    _MscLpEth100SingleCollisionFrames_Type()
)
mscLpEth100SingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100SingleCollisionFrames.setStatus("mandatory")
_MscLpEth100MultipleCollisionFrames_Type = Counter32
_MscLpEth100MultipleCollisionFrames_Object = MibTableColumn
mscLpEth100MultipleCollisionFrames = _MscLpEth100MultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 5),
    _MscLpEth100MultipleCollisionFrames_Type()
)
mscLpEth100MultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100MultipleCollisionFrames.setStatus("mandatory")
_MscLpEth100SqeTestErrors_Type = Counter32
_MscLpEth100SqeTestErrors_Object = MibTableColumn
mscLpEth100SqeTestErrors = _MscLpEth100SqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 6),
    _MscLpEth100SqeTestErrors_Type()
)
mscLpEth100SqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100SqeTestErrors.setStatus("mandatory")
_MscLpEth100DeferredTransmissions_Type = Counter32
_MscLpEth100DeferredTransmissions_Object = MibTableColumn
mscLpEth100DeferredTransmissions = _MscLpEth100DeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 7),
    _MscLpEth100DeferredTransmissions_Type()
)
mscLpEth100DeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100DeferredTransmissions.setStatus("mandatory")
_MscLpEth100LateCollisions_Type = Counter32
_MscLpEth100LateCollisions_Object = MibTableColumn
mscLpEth100LateCollisions = _MscLpEth100LateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 8),
    _MscLpEth100LateCollisions_Type()
)
mscLpEth100LateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100LateCollisions.setStatus("mandatory")
_MscLpEth100ExcessiveCollisions_Type = Counter32
_MscLpEth100ExcessiveCollisions_Object = MibTableColumn
mscLpEth100ExcessiveCollisions = _MscLpEth100ExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 9),
    _MscLpEth100ExcessiveCollisions_Type()
)
mscLpEth100ExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100ExcessiveCollisions.setStatus("mandatory")
_MscLpEth100MacTransmitErrors_Type = Counter32
_MscLpEth100MacTransmitErrors_Object = MibTableColumn
mscLpEth100MacTransmitErrors = _MscLpEth100MacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 10),
    _MscLpEth100MacTransmitErrors_Type()
)
mscLpEth100MacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100MacTransmitErrors.setStatus("mandatory")
_MscLpEth100CarrierSenseErrors_Type = Counter32
_MscLpEth100CarrierSenseErrors_Object = MibTableColumn
mscLpEth100CarrierSenseErrors = _MscLpEth100CarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 11),
    _MscLpEth100CarrierSenseErrors_Type()
)
mscLpEth100CarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100CarrierSenseErrors.setStatus("mandatory")
_MscLpEth100FrameTooLongs_Type = Counter32
_MscLpEth100FrameTooLongs_Object = MibTableColumn
mscLpEth100FrameTooLongs = _MscLpEth100FrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 12),
    _MscLpEth100FrameTooLongs_Type()
)
mscLpEth100FrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100FrameTooLongs.setStatus("mandatory")
_MscLpEth100MacReceiveErrors_Type = Counter32
_MscLpEth100MacReceiveErrors_Object = MibTableColumn
mscLpEth100MacReceiveErrors = _MscLpEth100MacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 25, 19, 1, 13),
    _MscLpEth100MacReceiveErrors_Type()
)
mscLpEth100MacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpEth100MacReceiveErrors.setStatus("mandatory")
_MscLa_ObjectIdentity = ObjectIdentity
mscLa = _MscLa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105)
)
_MscLaRowStatusTable_Object = MibTable
mscLaRowStatusTable = _MscLaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 1)
)
if mibBuilder.loadTexts:
    mscLaRowStatusTable.setStatus("mandatory")
_MscLaRowStatusEntry_Object = MibTableRow
mscLaRowStatusEntry = _MscLaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 1, 1)
)
mscLaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
)
if mibBuilder.loadTexts:
    mscLaRowStatusEntry.setStatus("mandatory")
_MscLaRowStatus_Type = RowStatus
_MscLaRowStatus_Object = MibTableColumn
mscLaRowStatus = _MscLaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 1, 1, 1),
    _MscLaRowStatus_Type()
)
mscLaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLaRowStatus.setStatus("mandatory")
_MscLaComponentName_Type = DisplayString
_MscLaComponentName_Object = MibTableColumn
mscLaComponentName = _MscLaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 1, 1, 2),
    _MscLaComponentName_Type()
)
mscLaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaComponentName.setStatus("mandatory")
_MscLaStorageType_Type = StorageType
_MscLaStorageType_Object = MibTableColumn
mscLaStorageType = _MscLaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 1, 1, 4),
    _MscLaStorageType_Type()
)
mscLaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaStorageType.setStatus("mandatory")


class _MscLaIndex_Type(Integer32):
    """Custom type mscLaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscLaIndex_Type.__name__ = "Integer32"
_MscLaIndex_Object = MibTableColumn
mscLaIndex = _MscLaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 1, 1, 10),
    _MscLaIndex_Type()
)
mscLaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLaIndex.setStatus("mandatory")
_MscLaFramer_ObjectIdentity = ObjectIdentity
mscLaFramer = _MscLaFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2)
)
_MscLaFramerRowStatusTable_Object = MibTable
mscLaFramerRowStatusTable = _MscLaFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 1)
)
if mibBuilder.loadTexts:
    mscLaFramerRowStatusTable.setStatus("mandatory")
_MscLaFramerRowStatusEntry_Object = MibTableRow
mscLaFramerRowStatusEntry = _MscLaFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 1, 1)
)
mscLaFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaFramerIndex"),
)
if mibBuilder.loadTexts:
    mscLaFramerRowStatusEntry.setStatus("mandatory")
_MscLaFramerRowStatus_Type = RowStatus
_MscLaFramerRowStatus_Object = MibTableColumn
mscLaFramerRowStatus = _MscLaFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 1, 1, 1),
    _MscLaFramerRowStatus_Type()
)
mscLaFramerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaFramerRowStatus.setStatus("mandatory")
_MscLaFramerComponentName_Type = DisplayString
_MscLaFramerComponentName_Object = MibTableColumn
mscLaFramerComponentName = _MscLaFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 1, 1, 2),
    _MscLaFramerComponentName_Type()
)
mscLaFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaFramerComponentName.setStatus("mandatory")
_MscLaFramerStorageType_Type = StorageType
_MscLaFramerStorageType_Object = MibTableColumn
mscLaFramerStorageType = _MscLaFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 1, 1, 4),
    _MscLaFramerStorageType_Type()
)
mscLaFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaFramerStorageType.setStatus("mandatory")
_MscLaFramerIndex_Type = NonReplicated
_MscLaFramerIndex_Object = MibTableColumn
mscLaFramerIndex = _MscLaFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 1, 1, 10),
    _MscLaFramerIndex_Type()
)
mscLaFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLaFramerIndex.setStatus("mandatory")
_MscLaFramerProvTable_Object = MibTable
mscLaFramerProvTable = _MscLaFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 10)
)
if mibBuilder.loadTexts:
    mscLaFramerProvTable.setStatus("mandatory")
_MscLaFramerProvEntry_Object = MibTableRow
mscLaFramerProvEntry = _MscLaFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 10, 1)
)
mscLaFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaFramerIndex"),
)
if mibBuilder.loadTexts:
    mscLaFramerProvEntry.setStatus("mandatory")
_MscLaFramerInterfaceName_Type = Link
_MscLaFramerInterfaceName_Object = MibTableColumn
mscLaFramerInterfaceName = _MscLaFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 10, 1, 1),
    _MscLaFramerInterfaceName_Type()
)
mscLaFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLaFramerInterfaceName.setStatus("obsolete")
_MscLaFramerInterfaceNamesTable_Object = MibTable
mscLaFramerInterfaceNamesTable = _MscLaFramerInterfaceNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 431)
)
if mibBuilder.loadTexts:
    mscLaFramerInterfaceNamesTable.setStatus("mandatory")
_MscLaFramerInterfaceNamesEntry_Object = MibTableRow
mscLaFramerInterfaceNamesEntry = _MscLaFramerInterfaceNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 431, 1)
)
mscLaFramerInterfaceNamesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaFramerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaFramerInterfaceNamesValue"),
)
if mibBuilder.loadTexts:
    mscLaFramerInterfaceNamesEntry.setStatus("mandatory")
_MscLaFramerInterfaceNamesValue_Type = Link
_MscLaFramerInterfaceNamesValue_Object = MibTableColumn
mscLaFramerInterfaceNamesValue = _MscLaFramerInterfaceNamesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 431, 1, 1),
    _MscLaFramerInterfaceNamesValue_Type()
)
mscLaFramerInterfaceNamesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLaFramerInterfaceNamesValue.setStatus("mandatory")
_MscLaFramerInterfaceNamesRowStatus_Type = RowStatus
_MscLaFramerInterfaceNamesRowStatus_Object = MibTableColumn
mscLaFramerInterfaceNamesRowStatus = _MscLaFramerInterfaceNamesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 2, 431, 1, 2),
    _MscLaFramerInterfaceNamesRowStatus_Type()
)
mscLaFramerInterfaceNamesRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscLaFramerInterfaceNamesRowStatus.setStatus("mandatory")
_MscLaCidDataTable_Object = MibTable
mscLaCidDataTable = _MscLaCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 10)
)
if mibBuilder.loadTexts:
    mscLaCidDataTable.setStatus("mandatory")
_MscLaCidDataEntry_Object = MibTableRow
mscLaCidDataEntry = _MscLaCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 10, 1)
)
mscLaCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
)
if mibBuilder.loadTexts:
    mscLaCidDataEntry.setStatus("mandatory")


class _MscLaCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLaCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLaCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLaCustomerIdentifier_Object = MibTableColumn
mscLaCustomerIdentifier = _MscLaCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 10, 1, 1),
    _MscLaCustomerIdentifier_Type()
)
mscLaCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLaCustomerIdentifier.setStatus("mandatory")
_MscLaMediaProvTable_Object = MibTable
mscLaMediaProvTable = _MscLaMediaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 11)
)
if mibBuilder.loadTexts:
    mscLaMediaProvTable.setStatus("mandatory")
_MscLaMediaProvEntry_Object = MibTableRow
mscLaMediaProvEntry = _MscLaMediaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 11, 1)
)
mscLaMediaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
)
if mibBuilder.loadTexts:
    mscLaMediaProvEntry.setStatus("mandatory")
_MscLaLinkToProtocolPort_Type = Link
_MscLaLinkToProtocolPort_Object = MibTableColumn
mscLaLinkToProtocolPort = _MscLaLinkToProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 11, 1, 1),
    _MscLaLinkToProtocolPort_Type()
)
mscLaLinkToProtocolPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLaLinkToProtocolPort.setStatus("mandatory")
_MscLaIfEntryTable_Object = MibTable
mscLaIfEntryTable = _MscLaIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 12)
)
if mibBuilder.loadTexts:
    mscLaIfEntryTable.setStatus("mandatory")
_MscLaIfEntryEntry_Object = MibTableRow
mscLaIfEntryEntry = _MscLaIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 12, 1)
)
mscLaIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
)
if mibBuilder.loadTexts:
    mscLaIfEntryEntry.setStatus("mandatory")


class _MscLaIfAdminStatus_Type(Integer32):
    """Custom type mscLaIfAdminStatus based on Integer32"""
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


_MscLaIfAdminStatus_Type.__name__ = "Integer32"
_MscLaIfAdminStatus_Object = MibTableColumn
mscLaIfAdminStatus = _MscLaIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 12, 1, 1),
    _MscLaIfAdminStatus_Type()
)
mscLaIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLaIfAdminStatus.setStatus("mandatory")


class _MscLaIfIndex_Type(InterfaceIndex):
    """Custom type mscLaIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLaIfIndex_Type.__name__ = "InterfaceIndex"
_MscLaIfIndex_Object = MibTableColumn
mscLaIfIndex = _MscLaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 12, 1, 2),
    _MscLaIfIndex_Type()
)
mscLaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaIfIndex.setStatus("mandatory")
_MscLaStateTable_Object = MibTable
mscLaStateTable = _MscLaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 13)
)
if mibBuilder.loadTexts:
    mscLaStateTable.setStatus("mandatory")
_MscLaStateEntry_Object = MibTableRow
mscLaStateEntry = _MscLaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 13, 1)
)
mscLaStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
)
if mibBuilder.loadTexts:
    mscLaStateEntry.setStatus("mandatory")


class _MscLaAdminState_Type(Integer32):
    """Custom type mscLaAdminState based on Integer32"""
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


_MscLaAdminState_Type.__name__ = "Integer32"
_MscLaAdminState_Object = MibTableColumn
mscLaAdminState = _MscLaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 13, 1, 1),
    _MscLaAdminState_Type()
)
mscLaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaAdminState.setStatus("mandatory")


class _MscLaOperationalState_Type(Integer32):
    """Custom type mscLaOperationalState based on Integer32"""
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


_MscLaOperationalState_Type.__name__ = "Integer32"
_MscLaOperationalState_Object = MibTableColumn
mscLaOperationalState = _MscLaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 13, 1, 2),
    _MscLaOperationalState_Type()
)
mscLaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaOperationalState.setStatus("mandatory")


class _MscLaUsageState_Type(Integer32):
    """Custom type mscLaUsageState based on Integer32"""
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


_MscLaUsageState_Type.__name__ = "Integer32"
_MscLaUsageState_Object = MibTableColumn
mscLaUsageState = _MscLaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 13, 1, 3),
    _MscLaUsageState_Type()
)
mscLaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaUsageState.setStatus("mandatory")
_MscLaOperStatusTable_Object = MibTable
mscLaOperStatusTable = _MscLaOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 14)
)
if mibBuilder.loadTexts:
    mscLaOperStatusTable.setStatus("mandatory")
_MscLaOperStatusEntry_Object = MibTableRow
mscLaOperStatusEntry = _MscLaOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 14, 1)
)
mscLaOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LanDriversMIB", "mscLaIndex"),
)
if mibBuilder.loadTexts:
    mscLaOperStatusEntry.setStatus("mandatory")


class _MscLaSnmpOperStatus_Type(Integer32):
    """Custom type mscLaSnmpOperStatus based on Integer32"""
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


_MscLaSnmpOperStatus_Type.__name__ = "Integer32"
_MscLaSnmpOperStatus_Object = MibTableColumn
mscLaSnmpOperStatus = _MscLaSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 105, 14, 1, 1),
    _MscLaSnmpOperStatus_Type()
)
mscLaSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLaSnmpOperStatus.setStatus("mandatory")
_LanDriversMIB_ObjectIdentity = ObjectIdentity
lanDriversMIB = _LanDriversMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30)
)
_LanDriversGroup_ObjectIdentity = ObjectIdentity
lanDriversGroup = _LanDriversGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 1)
)
_LanDriversGroupCA_ObjectIdentity = ObjectIdentity
lanDriversGroupCA = _LanDriversGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 1, 1)
)
_LanDriversGroupCA02_ObjectIdentity = ObjectIdentity
lanDriversGroupCA02 = _LanDriversGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 1, 1, 3)
)
_LanDriversGroupCA02A_ObjectIdentity = ObjectIdentity
lanDriversGroupCA02A = _LanDriversGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 1, 1, 3, 2)
)
_LanDriversCapabilities_ObjectIdentity = ObjectIdentity
lanDriversCapabilities = _LanDriversCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 3)
)
_LanDriversCapabilitiesCA_ObjectIdentity = ObjectIdentity
lanDriversCapabilitiesCA = _LanDriversCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 3, 1)
)
_LanDriversCapabilitiesCA02_ObjectIdentity = ObjectIdentity
lanDriversCapabilitiesCA02 = _LanDriversCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 3, 1, 3)
)
_LanDriversCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
lanDriversCapabilitiesCA02A = _LanDriversCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 30, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-LanDriversMIB",
    **{"mscLpEnet": mscLpEnet,
       "mscLpEnetRowStatusTable": mscLpEnetRowStatusTable,
       "mscLpEnetRowStatusEntry": mscLpEnetRowStatusEntry,
       "mscLpEnetRowStatus": mscLpEnetRowStatus,
       "mscLpEnetComponentName": mscLpEnetComponentName,
       "mscLpEnetStorageType": mscLpEnetStorageType,
       "mscLpEnetIndex": mscLpEnetIndex,
       "mscLpEnetLt": mscLpEnetLt,
       "mscLpEnetLtRowStatusTable": mscLpEnetLtRowStatusTable,
       "mscLpEnetLtRowStatusEntry": mscLpEnetLtRowStatusEntry,
       "mscLpEnetLtRowStatus": mscLpEnetLtRowStatus,
       "mscLpEnetLtComponentName": mscLpEnetLtComponentName,
       "mscLpEnetLtStorageType": mscLpEnetLtStorageType,
       "mscLpEnetLtIndex": mscLpEnetLtIndex,
       "mscLpEnetLtFrmCmp": mscLpEnetLtFrmCmp,
       "mscLpEnetLtFrmCmpRowStatusTable": mscLpEnetLtFrmCmpRowStatusTable,
       "mscLpEnetLtFrmCmpRowStatusEntry": mscLpEnetLtFrmCmpRowStatusEntry,
       "mscLpEnetLtFrmCmpRowStatus": mscLpEnetLtFrmCmpRowStatus,
       "mscLpEnetLtFrmCmpComponentName": mscLpEnetLtFrmCmpComponentName,
       "mscLpEnetLtFrmCmpStorageType": mscLpEnetLtFrmCmpStorageType,
       "mscLpEnetLtFrmCmpIndex": mscLpEnetLtFrmCmpIndex,
       "mscLpEnetLtFrmCmpTopTable": mscLpEnetLtFrmCmpTopTable,
       "mscLpEnetLtFrmCmpTopEntry": mscLpEnetLtFrmCmpTopEntry,
       "mscLpEnetLtFrmCmpTData": mscLpEnetLtFrmCmpTData,
       "mscLpEnetLtFrmCpy": mscLpEnetLtFrmCpy,
       "mscLpEnetLtFrmCpyRowStatusTable": mscLpEnetLtFrmCpyRowStatusTable,
       "mscLpEnetLtFrmCpyRowStatusEntry": mscLpEnetLtFrmCpyRowStatusEntry,
       "mscLpEnetLtFrmCpyRowStatus": mscLpEnetLtFrmCpyRowStatus,
       "mscLpEnetLtFrmCpyComponentName": mscLpEnetLtFrmCpyComponentName,
       "mscLpEnetLtFrmCpyStorageType": mscLpEnetLtFrmCpyStorageType,
       "mscLpEnetLtFrmCpyIndex": mscLpEnetLtFrmCpyIndex,
       "mscLpEnetLtFrmCpyTopTable": mscLpEnetLtFrmCpyTopTable,
       "mscLpEnetLtFrmCpyTopEntry": mscLpEnetLtFrmCpyTopEntry,
       "mscLpEnetLtFrmCpyTData": mscLpEnetLtFrmCpyTData,
       "mscLpEnetLtPrtCfg": mscLpEnetLtPrtCfg,
       "mscLpEnetLtPrtCfgRowStatusTable": mscLpEnetLtPrtCfgRowStatusTable,
       "mscLpEnetLtPrtCfgRowStatusEntry": mscLpEnetLtPrtCfgRowStatusEntry,
       "mscLpEnetLtPrtCfgRowStatus": mscLpEnetLtPrtCfgRowStatus,
       "mscLpEnetLtPrtCfgComponentName": mscLpEnetLtPrtCfgComponentName,
       "mscLpEnetLtPrtCfgStorageType": mscLpEnetLtPrtCfgStorageType,
       "mscLpEnetLtPrtCfgIndex": mscLpEnetLtPrtCfgIndex,
       "mscLpEnetLtPrtCfgTopTable": mscLpEnetLtPrtCfgTopTable,
       "mscLpEnetLtPrtCfgTopEntry": mscLpEnetLtPrtCfgTopEntry,
       "mscLpEnetLtPrtCfgTData": mscLpEnetLtPrtCfgTData,
       "mscLpEnetLtFb": mscLpEnetLtFb,
       "mscLpEnetLtFbRowStatusTable": mscLpEnetLtFbRowStatusTable,
       "mscLpEnetLtFbRowStatusEntry": mscLpEnetLtFbRowStatusEntry,
       "mscLpEnetLtFbRowStatus": mscLpEnetLtFbRowStatus,
       "mscLpEnetLtFbComponentName": mscLpEnetLtFbComponentName,
       "mscLpEnetLtFbStorageType": mscLpEnetLtFbStorageType,
       "mscLpEnetLtFbIndex": mscLpEnetLtFbIndex,
       "mscLpEnetLtFbTxInfo": mscLpEnetLtFbTxInfo,
       "mscLpEnetLtFbTxInfoRowStatusTable": mscLpEnetLtFbTxInfoRowStatusTable,
       "mscLpEnetLtFbTxInfoRowStatusEntry": mscLpEnetLtFbTxInfoRowStatusEntry,
       "mscLpEnetLtFbTxInfoRowStatus": mscLpEnetLtFbTxInfoRowStatus,
       "mscLpEnetLtFbTxInfoComponentName": mscLpEnetLtFbTxInfoComponentName,
       "mscLpEnetLtFbTxInfoStorageType": mscLpEnetLtFbTxInfoStorageType,
       "mscLpEnetLtFbTxInfoIndex": mscLpEnetLtFbTxInfoIndex,
       "mscLpEnetLtFbTxInfoTopTable": mscLpEnetLtFbTxInfoTopTable,
       "mscLpEnetLtFbTxInfoTopEntry": mscLpEnetLtFbTxInfoTopEntry,
       "mscLpEnetLtFbTxInfoTData": mscLpEnetLtFbTxInfoTData,
       "mscLpEnetLtFbFddiMac": mscLpEnetLtFbFddiMac,
       "mscLpEnetLtFbFddiMacRowStatusTable": mscLpEnetLtFbFddiMacRowStatusTable,
       "mscLpEnetLtFbFddiMacRowStatusEntry": mscLpEnetLtFbFddiMacRowStatusEntry,
       "mscLpEnetLtFbFddiMacRowStatus": mscLpEnetLtFbFddiMacRowStatus,
       "mscLpEnetLtFbFddiMacComponentName": mscLpEnetLtFbFddiMacComponentName,
       "mscLpEnetLtFbFddiMacStorageType": mscLpEnetLtFbFddiMacStorageType,
       "mscLpEnetLtFbFddiMacIndex": mscLpEnetLtFbFddiMacIndex,
       "mscLpEnetLtFbFddiMacTopTable": mscLpEnetLtFbFddiMacTopTable,
       "mscLpEnetLtFbFddiMacTopEntry": mscLpEnetLtFbFddiMacTopEntry,
       "mscLpEnetLtFbFddiMacTData": mscLpEnetLtFbFddiMacTData,
       "mscLpEnetLtFbMacEnet": mscLpEnetLtFbMacEnet,
       "mscLpEnetLtFbMacEnetRowStatusTable": mscLpEnetLtFbMacEnetRowStatusTable,
       "mscLpEnetLtFbMacEnetRowStatusEntry": mscLpEnetLtFbMacEnetRowStatusEntry,
       "mscLpEnetLtFbMacEnetRowStatus": mscLpEnetLtFbMacEnetRowStatus,
       "mscLpEnetLtFbMacEnetComponentName": mscLpEnetLtFbMacEnetComponentName,
       "mscLpEnetLtFbMacEnetStorageType": mscLpEnetLtFbMacEnetStorageType,
       "mscLpEnetLtFbMacEnetIndex": mscLpEnetLtFbMacEnetIndex,
       "mscLpEnetLtFbMacEnetTopTable": mscLpEnetLtFbMacEnetTopTable,
       "mscLpEnetLtFbMacEnetTopEntry": mscLpEnetLtFbMacEnetTopEntry,
       "mscLpEnetLtFbMacEnetTData": mscLpEnetLtFbMacEnetTData,
       "mscLpEnetLtFbMacTr": mscLpEnetLtFbMacTr,
       "mscLpEnetLtFbMacTrRowStatusTable": mscLpEnetLtFbMacTrRowStatusTable,
       "mscLpEnetLtFbMacTrRowStatusEntry": mscLpEnetLtFbMacTrRowStatusEntry,
       "mscLpEnetLtFbMacTrRowStatus": mscLpEnetLtFbMacTrRowStatus,
       "mscLpEnetLtFbMacTrComponentName": mscLpEnetLtFbMacTrComponentName,
       "mscLpEnetLtFbMacTrStorageType": mscLpEnetLtFbMacTrStorageType,
       "mscLpEnetLtFbMacTrIndex": mscLpEnetLtFbMacTrIndex,
       "mscLpEnetLtFbMacTrTopTable": mscLpEnetLtFbMacTrTopTable,
       "mscLpEnetLtFbMacTrTopEntry": mscLpEnetLtFbMacTrTopEntry,
       "mscLpEnetLtFbMacTrTData": mscLpEnetLtFbMacTrTData,
       "mscLpEnetLtFbData": mscLpEnetLtFbData,
       "mscLpEnetLtFbDataRowStatusTable": mscLpEnetLtFbDataRowStatusTable,
       "mscLpEnetLtFbDataRowStatusEntry": mscLpEnetLtFbDataRowStatusEntry,
       "mscLpEnetLtFbDataRowStatus": mscLpEnetLtFbDataRowStatus,
       "mscLpEnetLtFbDataComponentName": mscLpEnetLtFbDataComponentName,
       "mscLpEnetLtFbDataStorageType": mscLpEnetLtFbDataStorageType,
       "mscLpEnetLtFbDataIndex": mscLpEnetLtFbDataIndex,
       "mscLpEnetLtFbDataTopTable": mscLpEnetLtFbDataTopTable,
       "mscLpEnetLtFbDataTopEntry": mscLpEnetLtFbDataTopEntry,
       "mscLpEnetLtFbDataTData": mscLpEnetLtFbDataTData,
       "mscLpEnetLtFbIpH": mscLpEnetLtFbIpH,
       "mscLpEnetLtFbIpHRowStatusTable": mscLpEnetLtFbIpHRowStatusTable,
       "mscLpEnetLtFbIpHRowStatusEntry": mscLpEnetLtFbIpHRowStatusEntry,
       "mscLpEnetLtFbIpHRowStatus": mscLpEnetLtFbIpHRowStatus,
       "mscLpEnetLtFbIpHComponentName": mscLpEnetLtFbIpHComponentName,
       "mscLpEnetLtFbIpHStorageType": mscLpEnetLtFbIpHStorageType,
       "mscLpEnetLtFbIpHIndex": mscLpEnetLtFbIpHIndex,
       "mscLpEnetLtFbIpHTopTable": mscLpEnetLtFbIpHTopTable,
       "mscLpEnetLtFbIpHTopEntry": mscLpEnetLtFbIpHTopEntry,
       "mscLpEnetLtFbIpHTData": mscLpEnetLtFbIpHTData,
       "mscLpEnetLtFbLlch": mscLpEnetLtFbLlch,
       "mscLpEnetLtFbLlchRowStatusTable": mscLpEnetLtFbLlchRowStatusTable,
       "mscLpEnetLtFbLlchRowStatusEntry": mscLpEnetLtFbLlchRowStatusEntry,
       "mscLpEnetLtFbLlchRowStatus": mscLpEnetLtFbLlchRowStatus,
       "mscLpEnetLtFbLlchComponentName": mscLpEnetLtFbLlchComponentName,
       "mscLpEnetLtFbLlchStorageType": mscLpEnetLtFbLlchStorageType,
       "mscLpEnetLtFbLlchIndex": mscLpEnetLtFbLlchIndex,
       "mscLpEnetLtFbLlchTopTable": mscLpEnetLtFbLlchTopTable,
       "mscLpEnetLtFbLlchTopEntry": mscLpEnetLtFbLlchTopEntry,
       "mscLpEnetLtFbLlchTData": mscLpEnetLtFbLlchTData,
       "mscLpEnetLtFbAppleH": mscLpEnetLtFbAppleH,
       "mscLpEnetLtFbAppleHRowStatusTable": mscLpEnetLtFbAppleHRowStatusTable,
       "mscLpEnetLtFbAppleHRowStatusEntry": mscLpEnetLtFbAppleHRowStatusEntry,
       "mscLpEnetLtFbAppleHRowStatus": mscLpEnetLtFbAppleHRowStatus,
       "mscLpEnetLtFbAppleHComponentName": mscLpEnetLtFbAppleHComponentName,
       "mscLpEnetLtFbAppleHStorageType": mscLpEnetLtFbAppleHStorageType,
       "mscLpEnetLtFbAppleHIndex": mscLpEnetLtFbAppleHIndex,
       "mscLpEnetLtFbAppleHTopTable": mscLpEnetLtFbAppleHTopTable,
       "mscLpEnetLtFbAppleHTopEntry": mscLpEnetLtFbAppleHTopEntry,
       "mscLpEnetLtFbAppleHTData": mscLpEnetLtFbAppleHTData,
       "mscLpEnetLtFbIpxH": mscLpEnetLtFbIpxH,
       "mscLpEnetLtFbIpxHRowStatusTable": mscLpEnetLtFbIpxHRowStatusTable,
       "mscLpEnetLtFbIpxHRowStatusEntry": mscLpEnetLtFbIpxHRowStatusEntry,
       "mscLpEnetLtFbIpxHRowStatus": mscLpEnetLtFbIpxHRowStatus,
       "mscLpEnetLtFbIpxHComponentName": mscLpEnetLtFbIpxHComponentName,
       "mscLpEnetLtFbIpxHStorageType": mscLpEnetLtFbIpxHStorageType,
       "mscLpEnetLtFbIpxHIndex": mscLpEnetLtFbIpxHIndex,
       "mscLpEnetLtFbIpxHTopTable": mscLpEnetLtFbIpxHTopTable,
       "mscLpEnetLtFbIpxHTopEntry": mscLpEnetLtFbIpxHTopEntry,
       "mscLpEnetLtFbIpxHTData": mscLpEnetLtFbIpxHTData,
       "mscLpEnetLtFbTopTable": mscLpEnetLtFbTopTable,
       "mscLpEnetLtFbTopEntry": mscLpEnetLtFbTopEntry,
       "mscLpEnetLtFbTData": mscLpEnetLtFbTData,
       "mscLpEnetLtCntl": mscLpEnetLtCntl,
       "mscLpEnetLtCntlRowStatusTable": mscLpEnetLtCntlRowStatusTable,
       "mscLpEnetLtCntlRowStatusEntry": mscLpEnetLtCntlRowStatusEntry,
       "mscLpEnetLtCntlRowStatus": mscLpEnetLtCntlRowStatus,
       "mscLpEnetLtCntlComponentName": mscLpEnetLtCntlComponentName,
       "mscLpEnetLtCntlStorageType": mscLpEnetLtCntlStorageType,
       "mscLpEnetLtCntlIndex": mscLpEnetLtCntlIndex,
       "mscLpEnetLtCntlTopTable": mscLpEnetLtCntlTopTable,
       "mscLpEnetLtCntlTopEntry": mscLpEnetLtCntlTopEntry,
       "mscLpEnetLtCntlTData": mscLpEnetLtCntlTData,
       "mscLpEnetLtTopTable": mscLpEnetLtTopTable,
       "mscLpEnetLtTopEntry": mscLpEnetLtTopEntry,
       "mscLpEnetLtTData": mscLpEnetLtTData,
       "mscLpEnetTest": mscLpEnetTest,
       "mscLpEnetTestRowStatusTable": mscLpEnetTestRowStatusTable,
       "mscLpEnetTestRowStatusEntry": mscLpEnetTestRowStatusEntry,
       "mscLpEnetTestRowStatus": mscLpEnetTestRowStatus,
       "mscLpEnetTestComponentName": mscLpEnetTestComponentName,
       "mscLpEnetTestStorageType": mscLpEnetTestStorageType,
       "mscLpEnetTestIndex": mscLpEnetTestIndex,
       "mscLpEnetTestPTOTable": mscLpEnetTestPTOTable,
       "mscLpEnetTestPTOEntry": mscLpEnetTestPTOEntry,
       "mscLpEnetTestType": mscLpEnetTestType,
       "mscLpEnetTestFrmSize": mscLpEnetTestFrmSize,
       "mscLpEnetTestDuration": mscLpEnetTestDuration,
       "mscLpEnetTestResultsTable": mscLpEnetTestResultsTable,
       "mscLpEnetTestResultsEntry": mscLpEnetTestResultsEntry,
       "mscLpEnetTestElapsedTime": mscLpEnetTestElapsedTime,
       "mscLpEnetTestTimeRemaining": mscLpEnetTestTimeRemaining,
       "mscLpEnetTestCauseOfTermination": mscLpEnetTestCauseOfTermination,
       "mscLpEnetTestFrmTx": mscLpEnetTestFrmTx,
       "mscLpEnetTestBitsTx": mscLpEnetTestBitsTx,
       "mscLpEnetTestFrmRx": mscLpEnetTestFrmRx,
       "mscLpEnetTestBitsRx": mscLpEnetTestBitsRx,
       "mscLpEnetTestErroredFrmRx": mscLpEnetTestErroredFrmRx,
       "mscLpEnetCidDataTable": mscLpEnetCidDataTable,
       "mscLpEnetCidDataEntry": mscLpEnetCidDataEntry,
       "mscLpEnetCustomerIdentifier": mscLpEnetCustomerIdentifier,
       "mscLpEnetIfEntryTable": mscLpEnetIfEntryTable,
       "mscLpEnetIfEntryEntry": mscLpEnetIfEntryEntry,
       "mscLpEnetIfAdminStatus": mscLpEnetIfAdminStatus,
       "mscLpEnetIfIndex": mscLpEnetIfIndex,
       "mscLpEnetProvTable": mscLpEnetProvTable,
       "mscLpEnetProvEntry": mscLpEnetProvEntry,
       "mscLpEnetHeartbeatPacket": mscLpEnetHeartbeatPacket,
       "mscLpEnetApplicationFramerName": mscLpEnetApplicationFramerName,
       "mscLpEnetAdminInfoTable": mscLpEnetAdminInfoTable,
       "mscLpEnetAdminInfoEntry": mscLpEnetAdminInfoEntry,
       "mscLpEnetVendor": mscLpEnetVendor,
       "mscLpEnetCommentText": mscLpEnetCommentText,
       "mscLpEnetStateTable": mscLpEnetStateTable,
       "mscLpEnetStateEntry": mscLpEnetStateEntry,
       "mscLpEnetAdminState": mscLpEnetAdminState,
       "mscLpEnetOperationalState": mscLpEnetOperationalState,
       "mscLpEnetUsageState": mscLpEnetUsageState,
       "mscLpEnetOperStatusTable": mscLpEnetOperStatusTable,
       "mscLpEnetOperStatusEntry": mscLpEnetOperStatusEntry,
       "mscLpEnetSnmpOperStatus": mscLpEnetSnmpOperStatus,
       "mscLpEnetOperTable": mscLpEnetOperTable,
       "mscLpEnetOperEntry": mscLpEnetOperEntry,
       "mscLpEnetMacAddress": mscLpEnetMacAddress,
       "mscLpEnetStatsTable": mscLpEnetStatsTable,
       "mscLpEnetStatsEntry": mscLpEnetStatsEntry,
       "mscLpEnetAlignmentErrors": mscLpEnetAlignmentErrors,
       "mscLpEnetFcsErrors": mscLpEnetFcsErrors,
       "mscLpEnetSingleCollisionFrames": mscLpEnetSingleCollisionFrames,
       "mscLpEnetMultipleCollisionFrames": mscLpEnetMultipleCollisionFrames,
       "mscLpEnetSqeTestErrors": mscLpEnetSqeTestErrors,
       "mscLpEnetDeferredTransmissions": mscLpEnetDeferredTransmissions,
       "mscLpEnetLateCollisions": mscLpEnetLateCollisions,
       "mscLpEnetExcessiveCollisions": mscLpEnetExcessiveCollisions,
       "mscLpEnetMacTransmitErrors": mscLpEnetMacTransmitErrors,
       "mscLpEnetCarrierSenseErrors": mscLpEnetCarrierSenseErrors,
       "mscLpEnetFrameTooLongs": mscLpEnetFrameTooLongs,
       "mscLpEnetMacReceiveErrors": mscLpEnetMacReceiveErrors,
       "mscLpFi": mscLpFi,
       "mscLpFiRowStatusTable": mscLpFiRowStatusTable,
       "mscLpFiRowStatusEntry": mscLpFiRowStatusEntry,
       "mscLpFiRowStatus": mscLpFiRowStatus,
       "mscLpFiComponentName": mscLpFiComponentName,
       "mscLpFiStorageType": mscLpFiStorageType,
       "mscLpFiIndex": mscLpFiIndex,
       "mscLpFiLt": mscLpFiLt,
       "mscLpFiLtRowStatusTable": mscLpFiLtRowStatusTable,
       "mscLpFiLtRowStatusEntry": mscLpFiLtRowStatusEntry,
       "mscLpFiLtRowStatus": mscLpFiLtRowStatus,
       "mscLpFiLtComponentName": mscLpFiLtComponentName,
       "mscLpFiLtStorageType": mscLpFiLtStorageType,
       "mscLpFiLtIndex": mscLpFiLtIndex,
       "mscLpFiLtFrmCmp": mscLpFiLtFrmCmp,
       "mscLpFiLtFrmCmpRowStatusTable": mscLpFiLtFrmCmpRowStatusTable,
       "mscLpFiLtFrmCmpRowStatusEntry": mscLpFiLtFrmCmpRowStatusEntry,
       "mscLpFiLtFrmCmpRowStatus": mscLpFiLtFrmCmpRowStatus,
       "mscLpFiLtFrmCmpComponentName": mscLpFiLtFrmCmpComponentName,
       "mscLpFiLtFrmCmpStorageType": mscLpFiLtFrmCmpStorageType,
       "mscLpFiLtFrmCmpIndex": mscLpFiLtFrmCmpIndex,
       "mscLpFiLtFrmCmpTopTable": mscLpFiLtFrmCmpTopTable,
       "mscLpFiLtFrmCmpTopEntry": mscLpFiLtFrmCmpTopEntry,
       "mscLpFiLtFrmCmpTData": mscLpFiLtFrmCmpTData,
       "mscLpFiLtFrmCpy": mscLpFiLtFrmCpy,
       "mscLpFiLtFrmCpyRowStatusTable": mscLpFiLtFrmCpyRowStatusTable,
       "mscLpFiLtFrmCpyRowStatusEntry": mscLpFiLtFrmCpyRowStatusEntry,
       "mscLpFiLtFrmCpyRowStatus": mscLpFiLtFrmCpyRowStatus,
       "mscLpFiLtFrmCpyComponentName": mscLpFiLtFrmCpyComponentName,
       "mscLpFiLtFrmCpyStorageType": mscLpFiLtFrmCpyStorageType,
       "mscLpFiLtFrmCpyIndex": mscLpFiLtFrmCpyIndex,
       "mscLpFiLtFrmCpyTopTable": mscLpFiLtFrmCpyTopTable,
       "mscLpFiLtFrmCpyTopEntry": mscLpFiLtFrmCpyTopEntry,
       "mscLpFiLtFrmCpyTData": mscLpFiLtFrmCpyTData,
       "mscLpFiLtPrtCfg": mscLpFiLtPrtCfg,
       "mscLpFiLtPrtCfgRowStatusTable": mscLpFiLtPrtCfgRowStatusTable,
       "mscLpFiLtPrtCfgRowStatusEntry": mscLpFiLtPrtCfgRowStatusEntry,
       "mscLpFiLtPrtCfgRowStatus": mscLpFiLtPrtCfgRowStatus,
       "mscLpFiLtPrtCfgComponentName": mscLpFiLtPrtCfgComponentName,
       "mscLpFiLtPrtCfgStorageType": mscLpFiLtPrtCfgStorageType,
       "mscLpFiLtPrtCfgIndex": mscLpFiLtPrtCfgIndex,
       "mscLpFiLtPrtCfgTopTable": mscLpFiLtPrtCfgTopTable,
       "mscLpFiLtPrtCfgTopEntry": mscLpFiLtPrtCfgTopEntry,
       "mscLpFiLtPrtCfgTData": mscLpFiLtPrtCfgTData,
       "mscLpFiLtFb": mscLpFiLtFb,
       "mscLpFiLtFbRowStatusTable": mscLpFiLtFbRowStatusTable,
       "mscLpFiLtFbRowStatusEntry": mscLpFiLtFbRowStatusEntry,
       "mscLpFiLtFbRowStatus": mscLpFiLtFbRowStatus,
       "mscLpFiLtFbComponentName": mscLpFiLtFbComponentName,
       "mscLpFiLtFbStorageType": mscLpFiLtFbStorageType,
       "mscLpFiLtFbIndex": mscLpFiLtFbIndex,
       "mscLpFiLtFbTxInfo": mscLpFiLtFbTxInfo,
       "mscLpFiLtFbTxInfoRowStatusTable": mscLpFiLtFbTxInfoRowStatusTable,
       "mscLpFiLtFbTxInfoRowStatusEntry": mscLpFiLtFbTxInfoRowStatusEntry,
       "mscLpFiLtFbTxInfoRowStatus": mscLpFiLtFbTxInfoRowStatus,
       "mscLpFiLtFbTxInfoComponentName": mscLpFiLtFbTxInfoComponentName,
       "mscLpFiLtFbTxInfoStorageType": mscLpFiLtFbTxInfoStorageType,
       "mscLpFiLtFbTxInfoIndex": mscLpFiLtFbTxInfoIndex,
       "mscLpFiLtFbTxInfoTopTable": mscLpFiLtFbTxInfoTopTable,
       "mscLpFiLtFbTxInfoTopEntry": mscLpFiLtFbTxInfoTopEntry,
       "mscLpFiLtFbTxInfoTData": mscLpFiLtFbTxInfoTData,
       "mscLpFiLtFbFddiMac": mscLpFiLtFbFddiMac,
       "mscLpFiLtFbFddiMacRowStatusTable": mscLpFiLtFbFddiMacRowStatusTable,
       "mscLpFiLtFbFddiMacRowStatusEntry": mscLpFiLtFbFddiMacRowStatusEntry,
       "mscLpFiLtFbFddiMacRowStatus": mscLpFiLtFbFddiMacRowStatus,
       "mscLpFiLtFbFddiMacComponentName": mscLpFiLtFbFddiMacComponentName,
       "mscLpFiLtFbFddiMacStorageType": mscLpFiLtFbFddiMacStorageType,
       "mscLpFiLtFbFddiMacIndex": mscLpFiLtFbFddiMacIndex,
       "mscLpFiLtFbFddiMacTopTable": mscLpFiLtFbFddiMacTopTable,
       "mscLpFiLtFbFddiMacTopEntry": mscLpFiLtFbFddiMacTopEntry,
       "mscLpFiLtFbFddiMacTData": mscLpFiLtFbFddiMacTData,
       "mscLpFiLtFbMacEnet": mscLpFiLtFbMacEnet,
       "mscLpFiLtFbMacEnetRowStatusTable": mscLpFiLtFbMacEnetRowStatusTable,
       "mscLpFiLtFbMacEnetRowStatusEntry": mscLpFiLtFbMacEnetRowStatusEntry,
       "mscLpFiLtFbMacEnetRowStatus": mscLpFiLtFbMacEnetRowStatus,
       "mscLpFiLtFbMacEnetComponentName": mscLpFiLtFbMacEnetComponentName,
       "mscLpFiLtFbMacEnetStorageType": mscLpFiLtFbMacEnetStorageType,
       "mscLpFiLtFbMacEnetIndex": mscLpFiLtFbMacEnetIndex,
       "mscLpFiLtFbMacEnetTopTable": mscLpFiLtFbMacEnetTopTable,
       "mscLpFiLtFbMacEnetTopEntry": mscLpFiLtFbMacEnetTopEntry,
       "mscLpFiLtFbMacEnetTData": mscLpFiLtFbMacEnetTData,
       "mscLpFiLtFbMacTr": mscLpFiLtFbMacTr,
       "mscLpFiLtFbMacTrRowStatusTable": mscLpFiLtFbMacTrRowStatusTable,
       "mscLpFiLtFbMacTrRowStatusEntry": mscLpFiLtFbMacTrRowStatusEntry,
       "mscLpFiLtFbMacTrRowStatus": mscLpFiLtFbMacTrRowStatus,
       "mscLpFiLtFbMacTrComponentName": mscLpFiLtFbMacTrComponentName,
       "mscLpFiLtFbMacTrStorageType": mscLpFiLtFbMacTrStorageType,
       "mscLpFiLtFbMacTrIndex": mscLpFiLtFbMacTrIndex,
       "mscLpFiLtFbMacTrTopTable": mscLpFiLtFbMacTrTopTable,
       "mscLpFiLtFbMacTrTopEntry": mscLpFiLtFbMacTrTopEntry,
       "mscLpFiLtFbMacTrTData": mscLpFiLtFbMacTrTData,
       "mscLpFiLtFbData": mscLpFiLtFbData,
       "mscLpFiLtFbDataRowStatusTable": mscLpFiLtFbDataRowStatusTable,
       "mscLpFiLtFbDataRowStatusEntry": mscLpFiLtFbDataRowStatusEntry,
       "mscLpFiLtFbDataRowStatus": mscLpFiLtFbDataRowStatus,
       "mscLpFiLtFbDataComponentName": mscLpFiLtFbDataComponentName,
       "mscLpFiLtFbDataStorageType": mscLpFiLtFbDataStorageType,
       "mscLpFiLtFbDataIndex": mscLpFiLtFbDataIndex,
       "mscLpFiLtFbDataTopTable": mscLpFiLtFbDataTopTable,
       "mscLpFiLtFbDataTopEntry": mscLpFiLtFbDataTopEntry,
       "mscLpFiLtFbDataTData": mscLpFiLtFbDataTData,
       "mscLpFiLtFbIpH": mscLpFiLtFbIpH,
       "mscLpFiLtFbIpHRowStatusTable": mscLpFiLtFbIpHRowStatusTable,
       "mscLpFiLtFbIpHRowStatusEntry": mscLpFiLtFbIpHRowStatusEntry,
       "mscLpFiLtFbIpHRowStatus": mscLpFiLtFbIpHRowStatus,
       "mscLpFiLtFbIpHComponentName": mscLpFiLtFbIpHComponentName,
       "mscLpFiLtFbIpHStorageType": mscLpFiLtFbIpHStorageType,
       "mscLpFiLtFbIpHIndex": mscLpFiLtFbIpHIndex,
       "mscLpFiLtFbIpHTopTable": mscLpFiLtFbIpHTopTable,
       "mscLpFiLtFbIpHTopEntry": mscLpFiLtFbIpHTopEntry,
       "mscLpFiLtFbIpHTData": mscLpFiLtFbIpHTData,
       "mscLpFiLtFbLlch": mscLpFiLtFbLlch,
       "mscLpFiLtFbLlchRowStatusTable": mscLpFiLtFbLlchRowStatusTable,
       "mscLpFiLtFbLlchRowStatusEntry": mscLpFiLtFbLlchRowStatusEntry,
       "mscLpFiLtFbLlchRowStatus": mscLpFiLtFbLlchRowStatus,
       "mscLpFiLtFbLlchComponentName": mscLpFiLtFbLlchComponentName,
       "mscLpFiLtFbLlchStorageType": mscLpFiLtFbLlchStorageType,
       "mscLpFiLtFbLlchIndex": mscLpFiLtFbLlchIndex,
       "mscLpFiLtFbLlchTopTable": mscLpFiLtFbLlchTopTable,
       "mscLpFiLtFbLlchTopEntry": mscLpFiLtFbLlchTopEntry,
       "mscLpFiLtFbLlchTData": mscLpFiLtFbLlchTData,
       "mscLpFiLtFbAppleH": mscLpFiLtFbAppleH,
       "mscLpFiLtFbAppleHRowStatusTable": mscLpFiLtFbAppleHRowStatusTable,
       "mscLpFiLtFbAppleHRowStatusEntry": mscLpFiLtFbAppleHRowStatusEntry,
       "mscLpFiLtFbAppleHRowStatus": mscLpFiLtFbAppleHRowStatus,
       "mscLpFiLtFbAppleHComponentName": mscLpFiLtFbAppleHComponentName,
       "mscLpFiLtFbAppleHStorageType": mscLpFiLtFbAppleHStorageType,
       "mscLpFiLtFbAppleHIndex": mscLpFiLtFbAppleHIndex,
       "mscLpFiLtFbAppleHTopTable": mscLpFiLtFbAppleHTopTable,
       "mscLpFiLtFbAppleHTopEntry": mscLpFiLtFbAppleHTopEntry,
       "mscLpFiLtFbAppleHTData": mscLpFiLtFbAppleHTData,
       "mscLpFiLtFbIpxH": mscLpFiLtFbIpxH,
       "mscLpFiLtFbIpxHRowStatusTable": mscLpFiLtFbIpxHRowStatusTable,
       "mscLpFiLtFbIpxHRowStatusEntry": mscLpFiLtFbIpxHRowStatusEntry,
       "mscLpFiLtFbIpxHRowStatus": mscLpFiLtFbIpxHRowStatus,
       "mscLpFiLtFbIpxHComponentName": mscLpFiLtFbIpxHComponentName,
       "mscLpFiLtFbIpxHStorageType": mscLpFiLtFbIpxHStorageType,
       "mscLpFiLtFbIpxHIndex": mscLpFiLtFbIpxHIndex,
       "mscLpFiLtFbIpxHTopTable": mscLpFiLtFbIpxHTopTable,
       "mscLpFiLtFbIpxHTopEntry": mscLpFiLtFbIpxHTopEntry,
       "mscLpFiLtFbIpxHTData": mscLpFiLtFbIpxHTData,
       "mscLpFiLtFbTopTable": mscLpFiLtFbTopTable,
       "mscLpFiLtFbTopEntry": mscLpFiLtFbTopEntry,
       "mscLpFiLtFbTData": mscLpFiLtFbTData,
       "mscLpFiLtCntl": mscLpFiLtCntl,
       "mscLpFiLtCntlRowStatusTable": mscLpFiLtCntlRowStatusTable,
       "mscLpFiLtCntlRowStatusEntry": mscLpFiLtCntlRowStatusEntry,
       "mscLpFiLtCntlRowStatus": mscLpFiLtCntlRowStatus,
       "mscLpFiLtCntlComponentName": mscLpFiLtCntlComponentName,
       "mscLpFiLtCntlStorageType": mscLpFiLtCntlStorageType,
       "mscLpFiLtCntlIndex": mscLpFiLtCntlIndex,
       "mscLpFiLtCntlTopTable": mscLpFiLtCntlTopTable,
       "mscLpFiLtCntlTopEntry": mscLpFiLtCntlTopEntry,
       "mscLpFiLtCntlTData": mscLpFiLtCntlTData,
       "mscLpFiLtTopTable": mscLpFiLtTopTable,
       "mscLpFiLtTopEntry": mscLpFiLtTopEntry,
       "mscLpFiLtTData": mscLpFiLtTData,
       "mscLpFiPhy": mscLpFiPhy,
       "mscLpFiPhyRowStatusTable": mscLpFiPhyRowStatusTable,
       "mscLpFiPhyRowStatusEntry": mscLpFiPhyRowStatusEntry,
       "mscLpFiPhyRowStatus": mscLpFiPhyRowStatus,
       "mscLpFiPhyComponentName": mscLpFiPhyComponentName,
       "mscLpFiPhyStorageType": mscLpFiPhyStorageType,
       "mscLpFiPhyFddiPhyTypeIndex": mscLpFiPhyFddiPhyTypeIndex,
       "mscLpFiPhyProvTable": mscLpFiPhyProvTable,
       "mscLpFiPhyProvEntry": mscLpFiPhyProvEntry,
       "mscLpFiPhyLerCutoff": mscLpFiPhyLerCutoff,
       "mscLpFiPhyLerAlarm": mscLpFiPhyLerAlarm,
       "mscLpFiPhyLinkErrorMonitor": mscLpFiPhyLinkErrorMonitor,
       "mscLpFiPhyOperTable": mscLpFiPhyOperTable,
       "mscLpFiPhyOperEntry": mscLpFiPhyOperEntry,
       "mscLpFiPhyNeighborType": mscLpFiPhyNeighborType,
       "mscLpFiPhyLctFailCounts": mscLpFiPhyLctFailCounts,
       "mscLpFiPhyLerEstimate": mscLpFiPhyLerEstimate,
       "mscLpFiPhyLemRejectCounts": mscLpFiPhyLemRejectCounts,
       "mscLpFiPhyLemCounts": mscLpFiPhyLemCounts,
       "mscLpFiPhyPcmState": mscLpFiPhyPcmState,
       "mscLpFiPhyLerFlag": mscLpFiPhyLerFlag,
       "mscLpFiPhySignalState": mscLpFiPhySignalState,
       "mscLpFiPhySignalBitsRcvd": mscLpFiPhySignalBitsRcvd,
       "mscLpFiPhySignalBitsTxmt": mscLpFiPhySignalBitsTxmt,
       "mscLpFiTest": mscLpFiTest,
       "mscLpFiTestRowStatusTable": mscLpFiTestRowStatusTable,
       "mscLpFiTestRowStatusEntry": mscLpFiTestRowStatusEntry,
       "mscLpFiTestRowStatus": mscLpFiTestRowStatus,
       "mscLpFiTestComponentName": mscLpFiTestComponentName,
       "mscLpFiTestStorageType": mscLpFiTestStorageType,
       "mscLpFiTestIndex": mscLpFiTestIndex,
       "mscLpFiTestPTOTable": mscLpFiTestPTOTable,
       "mscLpFiTestPTOEntry": mscLpFiTestPTOEntry,
       "mscLpFiTestType": mscLpFiTestType,
       "mscLpFiTestFrmSize": mscLpFiTestFrmSize,
       "mscLpFiTestDuration": mscLpFiTestDuration,
       "mscLpFiTestResultsTable": mscLpFiTestResultsTable,
       "mscLpFiTestResultsEntry": mscLpFiTestResultsEntry,
       "mscLpFiTestElapsedTime": mscLpFiTestElapsedTime,
       "mscLpFiTestTimeRemaining": mscLpFiTestTimeRemaining,
       "mscLpFiTestCauseOfTermination": mscLpFiTestCauseOfTermination,
       "mscLpFiTestFrmTx": mscLpFiTestFrmTx,
       "mscLpFiTestBitsTx": mscLpFiTestBitsTx,
       "mscLpFiTestFrmRx": mscLpFiTestFrmRx,
       "mscLpFiTestBitsRx": mscLpFiTestBitsRx,
       "mscLpFiTestErroredFrmRx": mscLpFiTestErroredFrmRx,
       "mscLpFiCidDataTable": mscLpFiCidDataTable,
       "mscLpFiCidDataEntry": mscLpFiCidDataEntry,
       "mscLpFiCustomerIdentifier": mscLpFiCustomerIdentifier,
       "mscLpFiIfEntryTable": mscLpFiIfEntryTable,
       "mscLpFiIfEntryEntry": mscLpFiIfEntryEntry,
       "mscLpFiIfAdminStatus": mscLpFiIfAdminStatus,
       "mscLpFiIfIndex": mscLpFiIfIndex,
       "mscLpFiSmtProvTable": mscLpFiSmtProvTable,
       "mscLpFiSmtProvEntry": mscLpFiSmtProvEntry,
       "mscLpFiUserData": mscLpFiUserData,
       "mscLpFiAcceptAa": mscLpFiAcceptAa,
       "mscLpFiAcceptBb": mscLpFiAcceptBb,
       "mscLpFiAcceptAs": mscLpFiAcceptAs,
       "mscLpFiAcceptBs": mscLpFiAcceptBs,
       "mscLpFiAcceptAm": mscLpFiAcceptAm,
       "mscLpFiAcceptBm": mscLpFiAcceptBm,
       "mscLpFiUseThruBa": mscLpFiUseThruBa,
       "mscLpFiNeighborNotifyInterval": mscLpFiNeighborNotifyInterval,
       "mscLpFiStatusReportPolicy": mscLpFiStatusReportPolicy,
       "mscLpFiTraceMaxExpirationTimer": mscLpFiTraceMaxExpirationTimer,
       "mscLpFiApplicationFramerName": mscLpFiApplicationFramerName,
       "mscLpFiMacProvTable": mscLpFiMacProvTable,
       "mscLpFiMacProvEntry": mscLpFiMacProvEntry,
       "mscLpFiTokenRequestTimer": mscLpFiTokenRequestTimer,
       "mscLpFiTokenMaxTimer": mscLpFiTokenMaxTimer,
       "mscLpFiValidTransmissionTimer": mscLpFiValidTransmissionTimer,
       "mscLpFiAdminInfoTable": mscLpFiAdminInfoTable,
       "mscLpFiAdminInfoEntry": mscLpFiAdminInfoEntry,
       "mscLpFiVendor": mscLpFiVendor,
       "mscLpFiCommentText": mscLpFiCommentText,
       "mscLpFiStateTable": mscLpFiStateTable,
       "mscLpFiStateEntry": mscLpFiStateEntry,
       "mscLpFiAdminState": mscLpFiAdminState,
       "mscLpFiOperationalState": mscLpFiOperationalState,
       "mscLpFiUsageState": mscLpFiUsageState,
       "mscLpFiOperStatusTable": mscLpFiOperStatusTable,
       "mscLpFiOperStatusEntry": mscLpFiOperStatusEntry,
       "mscLpFiSnmpOperStatus": mscLpFiSnmpOperStatus,
       "mscLpFiSmtOperTable": mscLpFiSmtOperTable,
       "mscLpFiSmtOperEntry": mscLpFiSmtOperEntry,
       "mscLpFiVersion": mscLpFiVersion,
       "mscLpFiBypassPresent": mscLpFiBypassPresent,
       "mscLpFiEcmState": mscLpFiEcmState,
       "mscLpFiCfState": mscLpFiCfState,
       "mscLpFiMacOperTable": mscLpFiMacOperTable,
       "mscLpFiMacOperEntry": mscLpFiMacOperEntry,
       "mscLpFiRingLatency": mscLpFiRingLatency,
       "mscLpFiMacAddress": mscLpFiMacAddress,
       "mscLpFiUpstreamNeighbor": mscLpFiUpstreamNeighbor,
       "mscLpFiDownstreamNeighbor": mscLpFiDownstreamNeighbor,
       "mscLpFiOldUpstreamNeighbor": mscLpFiOldUpstreamNeighbor,
       "mscLpFiOldDownstreamNeighbor": mscLpFiOldDownstreamNeighbor,
       "mscLpFiDupAddressTest": mscLpFiDupAddressTest,
       "mscLpFiTokenNegotiatedTimer": mscLpFiTokenNegotiatedTimer,
       "mscLpFiFrameCounts": mscLpFiFrameCounts,
       "mscLpFiCopiedCounts": mscLpFiCopiedCounts,
       "mscLpFiTransmitCounts": mscLpFiTransmitCounts,
       "mscLpFiErrorCounts": mscLpFiErrorCounts,
       "mscLpFiLostCounts": mscLpFiLostCounts,
       "mscLpFiRmtState": mscLpFiRmtState,
       "mscLpFiFrameErrorFlag": mscLpFiFrameErrorFlag,
       "mscLpFiMacCOperTable": mscLpFiMacCOperTable,
       "mscLpFiMacCOperEntry": mscLpFiMacCOperEntry,
       "mscLpFiTokenCounts": mscLpFiTokenCounts,
       "mscLpFiTvxExpiredCounts": mscLpFiTvxExpiredCounts,
       "mscLpFiNotCopiedCounts": mscLpFiNotCopiedCounts,
       "mscLpFiLateCounts": mscLpFiLateCounts,
       "mscLpFiRingOpCounts": mscLpFiRingOpCounts,
       "mscLpFiNcMacOperTable": mscLpFiNcMacOperTable,
       "mscLpFiNcMacOperEntry": mscLpFiNcMacOperEntry,
       "mscLpFiNcMacAddress": mscLpFiNcMacAddress,
       "mscLpFiNcUpstreamNeighbor": mscLpFiNcUpstreamNeighbor,
       "mscLpFiNcDownstreamNeighbor": mscLpFiNcDownstreamNeighbor,
       "mscLpFiNcOldUpstreamNeighbor": mscLpFiNcOldUpstreamNeighbor,
       "mscLpFiNcOldDownstreamNeighbor": mscLpFiNcOldDownstreamNeighbor,
       "mscLpTr": mscLpTr,
       "mscLpTrRowStatusTable": mscLpTrRowStatusTable,
       "mscLpTrRowStatusEntry": mscLpTrRowStatusEntry,
       "mscLpTrRowStatus": mscLpTrRowStatus,
       "mscLpTrComponentName": mscLpTrComponentName,
       "mscLpTrStorageType": mscLpTrStorageType,
       "mscLpTrIndex": mscLpTrIndex,
       "mscLpTrLt": mscLpTrLt,
       "mscLpTrLtRowStatusTable": mscLpTrLtRowStatusTable,
       "mscLpTrLtRowStatusEntry": mscLpTrLtRowStatusEntry,
       "mscLpTrLtRowStatus": mscLpTrLtRowStatus,
       "mscLpTrLtComponentName": mscLpTrLtComponentName,
       "mscLpTrLtStorageType": mscLpTrLtStorageType,
       "mscLpTrLtIndex": mscLpTrLtIndex,
       "mscLpTrLtFrmCmp": mscLpTrLtFrmCmp,
       "mscLpTrLtFrmCmpRowStatusTable": mscLpTrLtFrmCmpRowStatusTable,
       "mscLpTrLtFrmCmpRowStatusEntry": mscLpTrLtFrmCmpRowStatusEntry,
       "mscLpTrLtFrmCmpRowStatus": mscLpTrLtFrmCmpRowStatus,
       "mscLpTrLtFrmCmpComponentName": mscLpTrLtFrmCmpComponentName,
       "mscLpTrLtFrmCmpStorageType": mscLpTrLtFrmCmpStorageType,
       "mscLpTrLtFrmCmpIndex": mscLpTrLtFrmCmpIndex,
       "mscLpTrLtFrmCmpTopTable": mscLpTrLtFrmCmpTopTable,
       "mscLpTrLtFrmCmpTopEntry": mscLpTrLtFrmCmpTopEntry,
       "mscLpTrLtFrmCmpTData": mscLpTrLtFrmCmpTData,
       "mscLpTrLtFrmCpy": mscLpTrLtFrmCpy,
       "mscLpTrLtFrmCpyRowStatusTable": mscLpTrLtFrmCpyRowStatusTable,
       "mscLpTrLtFrmCpyRowStatusEntry": mscLpTrLtFrmCpyRowStatusEntry,
       "mscLpTrLtFrmCpyRowStatus": mscLpTrLtFrmCpyRowStatus,
       "mscLpTrLtFrmCpyComponentName": mscLpTrLtFrmCpyComponentName,
       "mscLpTrLtFrmCpyStorageType": mscLpTrLtFrmCpyStorageType,
       "mscLpTrLtFrmCpyIndex": mscLpTrLtFrmCpyIndex,
       "mscLpTrLtFrmCpyTopTable": mscLpTrLtFrmCpyTopTable,
       "mscLpTrLtFrmCpyTopEntry": mscLpTrLtFrmCpyTopEntry,
       "mscLpTrLtFrmCpyTData": mscLpTrLtFrmCpyTData,
       "mscLpTrLtPrtCfg": mscLpTrLtPrtCfg,
       "mscLpTrLtPrtCfgRowStatusTable": mscLpTrLtPrtCfgRowStatusTable,
       "mscLpTrLtPrtCfgRowStatusEntry": mscLpTrLtPrtCfgRowStatusEntry,
       "mscLpTrLtPrtCfgRowStatus": mscLpTrLtPrtCfgRowStatus,
       "mscLpTrLtPrtCfgComponentName": mscLpTrLtPrtCfgComponentName,
       "mscLpTrLtPrtCfgStorageType": mscLpTrLtPrtCfgStorageType,
       "mscLpTrLtPrtCfgIndex": mscLpTrLtPrtCfgIndex,
       "mscLpTrLtPrtCfgTopTable": mscLpTrLtPrtCfgTopTable,
       "mscLpTrLtPrtCfgTopEntry": mscLpTrLtPrtCfgTopEntry,
       "mscLpTrLtPrtCfgTData": mscLpTrLtPrtCfgTData,
       "mscLpTrLtFb": mscLpTrLtFb,
       "mscLpTrLtFbRowStatusTable": mscLpTrLtFbRowStatusTable,
       "mscLpTrLtFbRowStatusEntry": mscLpTrLtFbRowStatusEntry,
       "mscLpTrLtFbRowStatus": mscLpTrLtFbRowStatus,
       "mscLpTrLtFbComponentName": mscLpTrLtFbComponentName,
       "mscLpTrLtFbStorageType": mscLpTrLtFbStorageType,
       "mscLpTrLtFbIndex": mscLpTrLtFbIndex,
       "mscLpTrLtFbTxInfo": mscLpTrLtFbTxInfo,
       "mscLpTrLtFbTxInfoRowStatusTable": mscLpTrLtFbTxInfoRowStatusTable,
       "mscLpTrLtFbTxInfoRowStatusEntry": mscLpTrLtFbTxInfoRowStatusEntry,
       "mscLpTrLtFbTxInfoRowStatus": mscLpTrLtFbTxInfoRowStatus,
       "mscLpTrLtFbTxInfoComponentName": mscLpTrLtFbTxInfoComponentName,
       "mscLpTrLtFbTxInfoStorageType": mscLpTrLtFbTxInfoStorageType,
       "mscLpTrLtFbTxInfoIndex": mscLpTrLtFbTxInfoIndex,
       "mscLpTrLtFbTxInfoTopTable": mscLpTrLtFbTxInfoTopTable,
       "mscLpTrLtFbTxInfoTopEntry": mscLpTrLtFbTxInfoTopEntry,
       "mscLpTrLtFbTxInfoTData": mscLpTrLtFbTxInfoTData,
       "mscLpTrLtFbFddiMac": mscLpTrLtFbFddiMac,
       "mscLpTrLtFbFddiMacRowStatusTable": mscLpTrLtFbFddiMacRowStatusTable,
       "mscLpTrLtFbFddiMacRowStatusEntry": mscLpTrLtFbFddiMacRowStatusEntry,
       "mscLpTrLtFbFddiMacRowStatus": mscLpTrLtFbFddiMacRowStatus,
       "mscLpTrLtFbFddiMacComponentName": mscLpTrLtFbFddiMacComponentName,
       "mscLpTrLtFbFddiMacStorageType": mscLpTrLtFbFddiMacStorageType,
       "mscLpTrLtFbFddiMacIndex": mscLpTrLtFbFddiMacIndex,
       "mscLpTrLtFbFddiMacTopTable": mscLpTrLtFbFddiMacTopTable,
       "mscLpTrLtFbFddiMacTopEntry": mscLpTrLtFbFddiMacTopEntry,
       "mscLpTrLtFbFddiMacTData": mscLpTrLtFbFddiMacTData,
       "mscLpTrLtFbMacEnet": mscLpTrLtFbMacEnet,
       "mscLpTrLtFbMacEnetRowStatusTable": mscLpTrLtFbMacEnetRowStatusTable,
       "mscLpTrLtFbMacEnetRowStatusEntry": mscLpTrLtFbMacEnetRowStatusEntry,
       "mscLpTrLtFbMacEnetRowStatus": mscLpTrLtFbMacEnetRowStatus,
       "mscLpTrLtFbMacEnetComponentName": mscLpTrLtFbMacEnetComponentName,
       "mscLpTrLtFbMacEnetStorageType": mscLpTrLtFbMacEnetStorageType,
       "mscLpTrLtFbMacEnetIndex": mscLpTrLtFbMacEnetIndex,
       "mscLpTrLtFbMacEnetTopTable": mscLpTrLtFbMacEnetTopTable,
       "mscLpTrLtFbMacEnetTopEntry": mscLpTrLtFbMacEnetTopEntry,
       "mscLpTrLtFbMacEnetTData": mscLpTrLtFbMacEnetTData,
       "mscLpTrLtFbMacTr": mscLpTrLtFbMacTr,
       "mscLpTrLtFbMacTrRowStatusTable": mscLpTrLtFbMacTrRowStatusTable,
       "mscLpTrLtFbMacTrRowStatusEntry": mscLpTrLtFbMacTrRowStatusEntry,
       "mscLpTrLtFbMacTrRowStatus": mscLpTrLtFbMacTrRowStatus,
       "mscLpTrLtFbMacTrComponentName": mscLpTrLtFbMacTrComponentName,
       "mscLpTrLtFbMacTrStorageType": mscLpTrLtFbMacTrStorageType,
       "mscLpTrLtFbMacTrIndex": mscLpTrLtFbMacTrIndex,
       "mscLpTrLtFbMacTrTopTable": mscLpTrLtFbMacTrTopTable,
       "mscLpTrLtFbMacTrTopEntry": mscLpTrLtFbMacTrTopEntry,
       "mscLpTrLtFbMacTrTData": mscLpTrLtFbMacTrTData,
       "mscLpTrLtFbData": mscLpTrLtFbData,
       "mscLpTrLtFbDataRowStatusTable": mscLpTrLtFbDataRowStatusTable,
       "mscLpTrLtFbDataRowStatusEntry": mscLpTrLtFbDataRowStatusEntry,
       "mscLpTrLtFbDataRowStatus": mscLpTrLtFbDataRowStatus,
       "mscLpTrLtFbDataComponentName": mscLpTrLtFbDataComponentName,
       "mscLpTrLtFbDataStorageType": mscLpTrLtFbDataStorageType,
       "mscLpTrLtFbDataIndex": mscLpTrLtFbDataIndex,
       "mscLpTrLtFbDataTopTable": mscLpTrLtFbDataTopTable,
       "mscLpTrLtFbDataTopEntry": mscLpTrLtFbDataTopEntry,
       "mscLpTrLtFbDataTData": mscLpTrLtFbDataTData,
       "mscLpTrLtFbIpH": mscLpTrLtFbIpH,
       "mscLpTrLtFbIpHRowStatusTable": mscLpTrLtFbIpHRowStatusTable,
       "mscLpTrLtFbIpHRowStatusEntry": mscLpTrLtFbIpHRowStatusEntry,
       "mscLpTrLtFbIpHRowStatus": mscLpTrLtFbIpHRowStatus,
       "mscLpTrLtFbIpHComponentName": mscLpTrLtFbIpHComponentName,
       "mscLpTrLtFbIpHStorageType": mscLpTrLtFbIpHStorageType,
       "mscLpTrLtFbIpHIndex": mscLpTrLtFbIpHIndex,
       "mscLpTrLtFbIpHTopTable": mscLpTrLtFbIpHTopTable,
       "mscLpTrLtFbIpHTopEntry": mscLpTrLtFbIpHTopEntry,
       "mscLpTrLtFbIpHTData": mscLpTrLtFbIpHTData,
       "mscLpTrLtFbLlch": mscLpTrLtFbLlch,
       "mscLpTrLtFbLlchRowStatusTable": mscLpTrLtFbLlchRowStatusTable,
       "mscLpTrLtFbLlchRowStatusEntry": mscLpTrLtFbLlchRowStatusEntry,
       "mscLpTrLtFbLlchRowStatus": mscLpTrLtFbLlchRowStatus,
       "mscLpTrLtFbLlchComponentName": mscLpTrLtFbLlchComponentName,
       "mscLpTrLtFbLlchStorageType": mscLpTrLtFbLlchStorageType,
       "mscLpTrLtFbLlchIndex": mscLpTrLtFbLlchIndex,
       "mscLpTrLtFbLlchTopTable": mscLpTrLtFbLlchTopTable,
       "mscLpTrLtFbLlchTopEntry": mscLpTrLtFbLlchTopEntry,
       "mscLpTrLtFbLlchTData": mscLpTrLtFbLlchTData,
       "mscLpTrLtFbAppleH": mscLpTrLtFbAppleH,
       "mscLpTrLtFbAppleHRowStatusTable": mscLpTrLtFbAppleHRowStatusTable,
       "mscLpTrLtFbAppleHRowStatusEntry": mscLpTrLtFbAppleHRowStatusEntry,
       "mscLpTrLtFbAppleHRowStatus": mscLpTrLtFbAppleHRowStatus,
       "mscLpTrLtFbAppleHComponentName": mscLpTrLtFbAppleHComponentName,
       "mscLpTrLtFbAppleHStorageType": mscLpTrLtFbAppleHStorageType,
       "mscLpTrLtFbAppleHIndex": mscLpTrLtFbAppleHIndex,
       "mscLpTrLtFbAppleHTopTable": mscLpTrLtFbAppleHTopTable,
       "mscLpTrLtFbAppleHTopEntry": mscLpTrLtFbAppleHTopEntry,
       "mscLpTrLtFbAppleHTData": mscLpTrLtFbAppleHTData,
       "mscLpTrLtFbIpxH": mscLpTrLtFbIpxH,
       "mscLpTrLtFbIpxHRowStatusTable": mscLpTrLtFbIpxHRowStatusTable,
       "mscLpTrLtFbIpxHRowStatusEntry": mscLpTrLtFbIpxHRowStatusEntry,
       "mscLpTrLtFbIpxHRowStatus": mscLpTrLtFbIpxHRowStatus,
       "mscLpTrLtFbIpxHComponentName": mscLpTrLtFbIpxHComponentName,
       "mscLpTrLtFbIpxHStorageType": mscLpTrLtFbIpxHStorageType,
       "mscLpTrLtFbIpxHIndex": mscLpTrLtFbIpxHIndex,
       "mscLpTrLtFbIpxHTopTable": mscLpTrLtFbIpxHTopTable,
       "mscLpTrLtFbIpxHTopEntry": mscLpTrLtFbIpxHTopEntry,
       "mscLpTrLtFbIpxHTData": mscLpTrLtFbIpxHTData,
       "mscLpTrLtFbTopTable": mscLpTrLtFbTopTable,
       "mscLpTrLtFbTopEntry": mscLpTrLtFbTopEntry,
       "mscLpTrLtFbTData": mscLpTrLtFbTData,
       "mscLpTrLtCntl": mscLpTrLtCntl,
       "mscLpTrLtCntlRowStatusTable": mscLpTrLtCntlRowStatusTable,
       "mscLpTrLtCntlRowStatusEntry": mscLpTrLtCntlRowStatusEntry,
       "mscLpTrLtCntlRowStatus": mscLpTrLtCntlRowStatus,
       "mscLpTrLtCntlComponentName": mscLpTrLtCntlComponentName,
       "mscLpTrLtCntlStorageType": mscLpTrLtCntlStorageType,
       "mscLpTrLtCntlIndex": mscLpTrLtCntlIndex,
       "mscLpTrLtCntlTopTable": mscLpTrLtCntlTopTable,
       "mscLpTrLtCntlTopEntry": mscLpTrLtCntlTopEntry,
       "mscLpTrLtCntlTData": mscLpTrLtCntlTData,
       "mscLpTrLtTopTable": mscLpTrLtTopTable,
       "mscLpTrLtTopEntry": mscLpTrLtTopEntry,
       "mscLpTrLtTData": mscLpTrLtTData,
       "mscLpTrTest": mscLpTrTest,
       "mscLpTrTestRowStatusTable": mscLpTrTestRowStatusTable,
       "mscLpTrTestRowStatusEntry": mscLpTrTestRowStatusEntry,
       "mscLpTrTestRowStatus": mscLpTrTestRowStatus,
       "mscLpTrTestComponentName": mscLpTrTestComponentName,
       "mscLpTrTestStorageType": mscLpTrTestStorageType,
       "mscLpTrTestIndex": mscLpTrTestIndex,
       "mscLpTrTestPTOTable": mscLpTrTestPTOTable,
       "mscLpTrTestPTOEntry": mscLpTrTestPTOEntry,
       "mscLpTrTestType": mscLpTrTestType,
       "mscLpTrTestFrmSize": mscLpTrTestFrmSize,
       "mscLpTrTestDuration": mscLpTrTestDuration,
       "mscLpTrTestResultsTable": mscLpTrTestResultsTable,
       "mscLpTrTestResultsEntry": mscLpTrTestResultsEntry,
       "mscLpTrTestElapsedTime": mscLpTrTestElapsedTime,
       "mscLpTrTestTimeRemaining": mscLpTrTestTimeRemaining,
       "mscLpTrTestCauseOfTermination": mscLpTrTestCauseOfTermination,
       "mscLpTrTestFrmTx": mscLpTrTestFrmTx,
       "mscLpTrTestBitsTx": mscLpTrTestBitsTx,
       "mscLpTrTestFrmRx": mscLpTrTestFrmRx,
       "mscLpTrTestBitsRx": mscLpTrTestBitsRx,
       "mscLpTrTestErroredFrmRx": mscLpTrTestErroredFrmRx,
       "mscLpTrCidDataTable": mscLpTrCidDataTable,
       "mscLpTrCidDataEntry": mscLpTrCidDataEntry,
       "mscLpTrCustomerIdentifier": mscLpTrCustomerIdentifier,
       "mscLpTrIfEntryTable": mscLpTrIfEntryTable,
       "mscLpTrIfEntryEntry": mscLpTrIfEntryEntry,
       "mscLpTrIfAdminStatus": mscLpTrIfAdminStatus,
       "mscLpTrIfIndex": mscLpTrIfIndex,
       "mscLpTrProvTable": mscLpTrProvTable,
       "mscLpTrProvEntry": mscLpTrProvEntry,
       "mscLpTrRingSpeed": mscLpTrRingSpeed,
       "mscLpTrMonitorParticipate": mscLpTrMonitorParticipate,
       "mscLpTrFunctionalAddress": mscLpTrFunctionalAddress,
       "mscLpTrNodeAddress": mscLpTrNodeAddress,
       "mscLpTrGroupAddress": mscLpTrGroupAddress,
       "mscLpTrProductId": mscLpTrProductId,
       "mscLpTrApplicationFramerName": mscLpTrApplicationFramerName,
       "mscLpTrAdminInfoTable": mscLpTrAdminInfoTable,
       "mscLpTrAdminInfoEntry": mscLpTrAdminInfoEntry,
       "mscLpTrVendor": mscLpTrVendor,
       "mscLpTrCommentText": mscLpTrCommentText,
       "mscLpTrStateTable": mscLpTrStateTable,
       "mscLpTrStateEntry": mscLpTrStateEntry,
       "mscLpTrAdminState": mscLpTrAdminState,
       "mscLpTrOperationalState": mscLpTrOperationalState,
       "mscLpTrUsageState": mscLpTrUsageState,
       "mscLpTrOperStatusTable": mscLpTrOperStatusTable,
       "mscLpTrOperStatusEntry": mscLpTrOperStatusEntry,
       "mscLpTrSnmpOperStatus": mscLpTrSnmpOperStatus,
       "mscLpTrOperTable": mscLpTrOperTable,
       "mscLpTrOperEntry": mscLpTrOperEntry,
       "mscLpTrMacAddress": mscLpTrMacAddress,
       "mscLpTrRingState": mscLpTrRingState,
       "mscLpTrRingStatus": mscLpTrRingStatus,
       "mscLpTrRingOpenStatus": mscLpTrRingOpenStatus,
       "mscLpTrUpStream": mscLpTrUpStream,
       "mscLpTrChipSet": mscLpTrChipSet,
       "mscLpTrLastTimeBeaconSent": mscLpTrLastTimeBeaconSent,
       "mscLpTrStatsTable": mscLpTrStatsTable,
       "mscLpTrStatsEntry": mscLpTrStatsEntry,
       "mscLpTrLineErrors": mscLpTrLineErrors,
       "mscLpTrBurstErrors": mscLpTrBurstErrors,
       "mscLpTrAcErrors": mscLpTrAcErrors,
       "mscLpTrAbortTransErrors": mscLpTrAbortTransErrors,
       "mscLpTrInternalErrors": mscLpTrInternalErrors,
       "mscLpTrLostFrameErrors": mscLpTrLostFrameErrors,
       "mscLpTrReceiveCongestions": mscLpTrReceiveCongestions,
       "mscLpTrFrameCopiedErrors": mscLpTrFrameCopiedErrors,
       "mscLpTrTokenErrors": mscLpTrTokenErrors,
       "mscLpTrSoftErrors": mscLpTrSoftErrors,
       "mscLpTrHardErrors": mscLpTrHardErrors,
       "mscLpTrSignalLoss": mscLpTrSignalLoss,
       "mscLpTrTransmitBeacons": mscLpTrTransmitBeacons,
       "mscLpTrRingRecoverys": mscLpTrRingRecoverys,
       "mscLpTrLobeWires": mscLpTrLobeWires,
       "mscLpTrRemoveRings": mscLpTrRemoveRings,
       "mscLpTrSingleStation": mscLpTrSingleStation,
       "mscLpTrFreqErrors": mscLpTrFreqErrors,
       "mscLpTrNcMacOperTable": mscLpTrNcMacOperTable,
       "mscLpTrNcMacOperEntry": mscLpTrNcMacOperEntry,
       "mscLpTrNcMacAddress": mscLpTrNcMacAddress,
       "mscLpTrNcUpStream": mscLpTrNcUpStream,
       "mscLpIlsFwdr": mscLpIlsFwdr,
       "mscLpIlsFwdrRowStatusTable": mscLpIlsFwdrRowStatusTable,
       "mscLpIlsFwdrRowStatusEntry": mscLpIlsFwdrRowStatusEntry,
       "mscLpIlsFwdrRowStatus": mscLpIlsFwdrRowStatus,
       "mscLpIlsFwdrComponentName": mscLpIlsFwdrComponentName,
       "mscLpIlsFwdrStorageType": mscLpIlsFwdrStorageType,
       "mscLpIlsFwdrIndex": mscLpIlsFwdrIndex,
       "mscLpIlsFwdrLt": mscLpIlsFwdrLt,
       "mscLpIlsFwdrLtRowStatusTable": mscLpIlsFwdrLtRowStatusTable,
       "mscLpIlsFwdrLtRowStatusEntry": mscLpIlsFwdrLtRowStatusEntry,
       "mscLpIlsFwdrLtRowStatus": mscLpIlsFwdrLtRowStatus,
       "mscLpIlsFwdrLtComponentName": mscLpIlsFwdrLtComponentName,
       "mscLpIlsFwdrLtStorageType": mscLpIlsFwdrLtStorageType,
       "mscLpIlsFwdrLtIndex": mscLpIlsFwdrLtIndex,
       "mscLpIlsFwdrLtFrmCmp": mscLpIlsFwdrLtFrmCmp,
       "mscLpIlsFwdrLtFrmCmpRowStatusTable": mscLpIlsFwdrLtFrmCmpRowStatusTable,
       "mscLpIlsFwdrLtFrmCmpRowStatusEntry": mscLpIlsFwdrLtFrmCmpRowStatusEntry,
       "mscLpIlsFwdrLtFrmCmpRowStatus": mscLpIlsFwdrLtFrmCmpRowStatus,
       "mscLpIlsFwdrLtFrmCmpComponentName": mscLpIlsFwdrLtFrmCmpComponentName,
       "mscLpIlsFwdrLtFrmCmpStorageType": mscLpIlsFwdrLtFrmCmpStorageType,
       "mscLpIlsFwdrLtFrmCmpIndex": mscLpIlsFwdrLtFrmCmpIndex,
       "mscLpIlsFwdrLtFrmCmpTopTable": mscLpIlsFwdrLtFrmCmpTopTable,
       "mscLpIlsFwdrLtFrmCmpTopEntry": mscLpIlsFwdrLtFrmCmpTopEntry,
       "mscLpIlsFwdrLtFrmCmpTData": mscLpIlsFwdrLtFrmCmpTData,
       "mscLpIlsFwdrLtFrmCpy": mscLpIlsFwdrLtFrmCpy,
       "mscLpIlsFwdrLtFrmCpyRowStatusTable": mscLpIlsFwdrLtFrmCpyRowStatusTable,
       "mscLpIlsFwdrLtFrmCpyRowStatusEntry": mscLpIlsFwdrLtFrmCpyRowStatusEntry,
       "mscLpIlsFwdrLtFrmCpyRowStatus": mscLpIlsFwdrLtFrmCpyRowStatus,
       "mscLpIlsFwdrLtFrmCpyComponentName": mscLpIlsFwdrLtFrmCpyComponentName,
       "mscLpIlsFwdrLtFrmCpyStorageType": mscLpIlsFwdrLtFrmCpyStorageType,
       "mscLpIlsFwdrLtFrmCpyIndex": mscLpIlsFwdrLtFrmCpyIndex,
       "mscLpIlsFwdrLtFrmCpyTopTable": mscLpIlsFwdrLtFrmCpyTopTable,
       "mscLpIlsFwdrLtFrmCpyTopEntry": mscLpIlsFwdrLtFrmCpyTopEntry,
       "mscLpIlsFwdrLtFrmCpyTData": mscLpIlsFwdrLtFrmCpyTData,
       "mscLpIlsFwdrLtPrtCfg": mscLpIlsFwdrLtPrtCfg,
       "mscLpIlsFwdrLtPrtCfgRowStatusTable": mscLpIlsFwdrLtPrtCfgRowStatusTable,
       "mscLpIlsFwdrLtPrtCfgRowStatusEntry": mscLpIlsFwdrLtPrtCfgRowStatusEntry,
       "mscLpIlsFwdrLtPrtCfgRowStatus": mscLpIlsFwdrLtPrtCfgRowStatus,
       "mscLpIlsFwdrLtPrtCfgComponentName": mscLpIlsFwdrLtPrtCfgComponentName,
       "mscLpIlsFwdrLtPrtCfgStorageType": mscLpIlsFwdrLtPrtCfgStorageType,
       "mscLpIlsFwdrLtPrtCfgIndex": mscLpIlsFwdrLtPrtCfgIndex,
       "mscLpIlsFwdrLtPrtCfgTopTable": mscLpIlsFwdrLtPrtCfgTopTable,
       "mscLpIlsFwdrLtPrtCfgTopEntry": mscLpIlsFwdrLtPrtCfgTopEntry,
       "mscLpIlsFwdrLtPrtCfgTData": mscLpIlsFwdrLtPrtCfgTData,
       "mscLpIlsFwdrLtFb": mscLpIlsFwdrLtFb,
       "mscLpIlsFwdrLtFbRowStatusTable": mscLpIlsFwdrLtFbRowStatusTable,
       "mscLpIlsFwdrLtFbRowStatusEntry": mscLpIlsFwdrLtFbRowStatusEntry,
       "mscLpIlsFwdrLtFbRowStatus": mscLpIlsFwdrLtFbRowStatus,
       "mscLpIlsFwdrLtFbComponentName": mscLpIlsFwdrLtFbComponentName,
       "mscLpIlsFwdrLtFbStorageType": mscLpIlsFwdrLtFbStorageType,
       "mscLpIlsFwdrLtFbIndex": mscLpIlsFwdrLtFbIndex,
       "mscLpIlsFwdrLtFbTxInfo": mscLpIlsFwdrLtFbTxInfo,
       "mscLpIlsFwdrLtFbTxInfoRowStatusTable": mscLpIlsFwdrLtFbTxInfoRowStatusTable,
       "mscLpIlsFwdrLtFbTxInfoRowStatusEntry": mscLpIlsFwdrLtFbTxInfoRowStatusEntry,
       "mscLpIlsFwdrLtFbTxInfoRowStatus": mscLpIlsFwdrLtFbTxInfoRowStatus,
       "mscLpIlsFwdrLtFbTxInfoComponentName": mscLpIlsFwdrLtFbTxInfoComponentName,
       "mscLpIlsFwdrLtFbTxInfoStorageType": mscLpIlsFwdrLtFbTxInfoStorageType,
       "mscLpIlsFwdrLtFbTxInfoIndex": mscLpIlsFwdrLtFbTxInfoIndex,
       "mscLpIlsFwdrLtFbTxInfoTopTable": mscLpIlsFwdrLtFbTxInfoTopTable,
       "mscLpIlsFwdrLtFbTxInfoTopEntry": mscLpIlsFwdrLtFbTxInfoTopEntry,
       "mscLpIlsFwdrLtFbTxInfoTData": mscLpIlsFwdrLtFbTxInfoTData,
       "mscLpIlsFwdrLtFbFddiMac": mscLpIlsFwdrLtFbFddiMac,
       "mscLpIlsFwdrLtFbFddiMacRowStatusTable": mscLpIlsFwdrLtFbFddiMacRowStatusTable,
       "mscLpIlsFwdrLtFbFddiMacRowStatusEntry": mscLpIlsFwdrLtFbFddiMacRowStatusEntry,
       "mscLpIlsFwdrLtFbFddiMacRowStatus": mscLpIlsFwdrLtFbFddiMacRowStatus,
       "mscLpIlsFwdrLtFbFddiMacComponentName": mscLpIlsFwdrLtFbFddiMacComponentName,
       "mscLpIlsFwdrLtFbFddiMacStorageType": mscLpIlsFwdrLtFbFddiMacStorageType,
       "mscLpIlsFwdrLtFbFddiMacIndex": mscLpIlsFwdrLtFbFddiMacIndex,
       "mscLpIlsFwdrLtFbFddiMacTopTable": mscLpIlsFwdrLtFbFddiMacTopTable,
       "mscLpIlsFwdrLtFbFddiMacTopEntry": mscLpIlsFwdrLtFbFddiMacTopEntry,
       "mscLpIlsFwdrLtFbFddiMacTData": mscLpIlsFwdrLtFbFddiMacTData,
       "mscLpIlsFwdrLtFbMacEnet": mscLpIlsFwdrLtFbMacEnet,
       "mscLpIlsFwdrLtFbMacEnetRowStatusTable": mscLpIlsFwdrLtFbMacEnetRowStatusTable,
       "mscLpIlsFwdrLtFbMacEnetRowStatusEntry": mscLpIlsFwdrLtFbMacEnetRowStatusEntry,
       "mscLpIlsFwdrLtFbMacEnetRowStatus": mscLpIlsFwdrLtFbMacEnetRowStatus,
       "mscLpIlsFwdrLtFbMacEnetComponentName": mscLpIlsFwdrLtFbMacEnetComponentName,
       "mscLpIlsFwdrLtFbMacEnetStorageType": mscLpIlsFwdrLtFbMacEnetStorageType,
       "mscLpIlsFwdrLtFbMacEnetIndex": mscLpIlsFwdrLtFbMacEnetIndex,
       "mscLpIlsFwdrLtFbMacEnetTopTable": mscLpIlsFwdrLtFbMacEnetTopTable,
       "mscLpIlsFwdrLtFbMacEnetTopEntry": mscLpIlsFwdrLtFbMacEnetTopEntry,
       "mscLpIlsFwdrLtFbMacEnetTData": mscLpIlsFwdrLtFbMacEnetTData,
       "mscLpIlsFwdrLtFbMacTr": mscLpIlsFwdrLtFbMacTr,
       "mscLpIlsFwdrLtFbMacTrRowStatusTable": mscLpIlsFwdrLtFbMacTrRowStatusTable,
       "mscLpIlsFwdrLtFbMacTrRowStatusEntry": mscLpIlsFwdrLtFbMacTrRowStatusEntry,
       "mscLpIlsFwdrLtFbMacTrRowStatus": mscLpIlsFwdrLtFbMacTrRowStatus,
       "mscLpIlsFwdrLtFbMacTrComponentName": mscLpIlsFwdrLtFbMacTrComponentName,
       "mscLpIlsFwdrLtFbMacTrStorageType": mscLpIlsFwdrLtFbMacTrStorageType,
       "mscLpIlsFwdrLtFbMacTrIndex": mscLpIlsFwdrLtFbMacTrIndex,
       "mscLpIlsFwdrLtFbMacTrTopTable": mscLpIlsFwdrLtFbMacTrTopTable,
       "mscLpIlsFwdrLtFbMacTrTopEntry": mscLpIlsFwdrLtFbMacTrTopEntry,
       "mscLpIlsFwdrLtFbMacTrTData": mscLpIlsFwdrLtFbMacTrTData,
       "mscLpIlsFwdrLtFbData": mscLpIlsFwdrLtFbData,
       "mscLpIlsFwdrLtFbDataRowStatusTable": mscLpIlsFwdrLtFbDataRowStatusTable,
       "mscLpIlsFwdrLtFbDataRowStatusEntry": mscLpIlsFwdrLtFbDataRowStatusEntry,
       "mscLpIlsFwdrLtFbDataRowStatus": mscLpIlsFwdrLtFbDataRowStatus,
       "mscLpIlsFwdrLtFbDataComponentName": mscLpIlsFwdrLtFbDataComponentName,
       "mscLpIlsFwdrLtFbDataStorageType": mscLpIlsFwdrLtFbDataStorageType,
       "mscLpIlsFwdrLtFbDataIndex": mscLpIlsFwdrLtFbDataIndex,
       "mscLpIlsFwdrLtFbDataTopTable": mscLpIlsFwdrLtFbDataTopTable,
       "mscLpIlsFwdrLtFbDataTopEntry": mscLpIlsFwdrLtFbDataTopEntry,
       "mscLpIlsFwdrLtFbDataTData": mscLpIlsFwdrLtFbDataTData,
       "mscLpIlsFwdrLtFbIpH": mscLpIlsFwdrLtFbIpH,
       "mscLpIlsFwdrLtFbIpHRowStatusTable": mscLpIlsFwdrLtFbIpHRowStatusTable,
       "mscLpIlsFwdrLtFbIpHRowStatusEntry": mscLpIlsFwdrLtFbIpHRowStatusEntry,
       "mscLpIlsFwdrLtFbIpHRowStatus": mscLpIlsFwdrLtFbIpHRowStatus,
       "mscLpIlsFwdrLtFbIpHComponentName": mscLpIlsFwdrLtFbIpHComponentName,
       "mscLpIlsFwdrLtFbIpHStorageType": mscLpIlsFwdrLtFbIpHStorageType,
       "mscLpIlsFwdrLtFbIpHIndex": mscLpIlsFwdrLtFbIpHIndex,
       "mscLpIlsFwdrLtFbIpHTopTable": mscLpIlsFwdrLtFbIpHTopTable,
       "mscLpIlsFwdrLtFbIpHTopEntry": mscLpIlsFwdrLtFbIpHTopEntry,
       "mscLpIlsFwdrLtFbIpHTData": mscLpIlsFwdrLtFbIpHTData,
       "mscLpIlsFwdrLtFbLlch": mscLpIlsFwdrLtFbLlch,
       "mscLpIlsFwdrLtFbLlchRowStatusTable": mscLpIlsFwdrLtFbLlchRowStatusTable,
       "mscLpIlsFwdrLtFbLlchRowStatusEntry": mscLpIlsFwdrLtFbLlchRowStatusEntry,
       "mscLpIlsFwdrLtFbLlchRowStatus": mscLpIlsFwdrLtFbLlchRowStatus,
       "mscLpIlsFwdrLtFbLlchComponentName": mscLpIlsFwdrLtFbLlchComponentName,
       "mscLpIlsFwdrLtFbLlchStorageType": mscLpIlsFwdrLtFbLlchStorageType,
       "mscLpIlsFwdrLtFbLlchIndex": mscLpIlsFwdrLtFbLlchIndex,
       "mscLpIlsFwdrLtFbLlchTopTable": mscLpIlsFwdrLtFbLlchTopTable,
       "mscLpIlsFwdrLtFbLlchTopEntry": mscLpIlsFwdrLtFbLlchTopEntry,
       "mscLpIlsFwdrLtFbLlchTData": mscLpIlsFwdrLtFbLlchTData,
       "mscLpIlsFwdrLtFbAppleH": mscLpIlsFwdrLtFbAppleH,
       "mscLpIlsFwdrLtFbAppleHRowStatusTable": mscLpIlsFwdrLtFbAppleHRowStatusTable,
       "mscLpIlsFwdrLtFbAppleHRowStatusEntry": mscLpIlsFwdrLtFbAppleHRowStatusEntry,
       "mscLpIlsFwdrLtFbAppleHRowStatus": mscLpIlsFwdrLtFbAppleHRowStatus,
       "mscLpIlsFwdrLtFbAppleHComponentName": mscLpIlsFwdrLtFbAppleHComponentName,
       "mscLpIlsFwdrLtFbAppleHStorageType": mscLpIlsFwdrLtFbAppleHStorageType,
       "mscLpIlsFwdrLtFbAppleHIndex": mscLpIlsFwdrLtFbAppleHIndex,
       "mscLpIlsFwdrLtFbAppleHTopTable": mscLpIlsFwdrLtFbAppleHTopTable,
       "mscLpIlsFwdrLtFbAppleHTopEntry": mscLpIlsFwdrLtFbAppleHTopEntry,
       "mscLpIlsFwdrLtFbAppleHTData": mscLpIlsFwdrLtFbAppleHTData,
       "mscLpIlsFwdrLtFbIpxH": mscLpIlsFwdrLtFbIpxH,
       "mscLpIlsFwdrLtFbIpxHRowStatusTable": mscLpIlsFwdrLtFbIpxHRowStatusTable,
       "mscLpIlsFwdrLtFbIpxHRowStatusEntry": mscLpIlsFwdrLtFbIpxHRowStatusEntry,
       "mscLpIlsFwdrLtFbIpxHRowStatus": mscLpIlsFwdrLtFbIpxHRowStatus,
       "mscLpIlsFwdrLtFbIpxHComponentName": mscLpIlsFwdrLtFbIpxHComponentName,
       "mscLpIlsFwdrLtFbIpxHStorageType": mscLpIlsFwdrLtFbIpxHStorageType,
       "mscLpIlsFwdrLtFbIpxHIndex": mscLpIlsFwdrLtFbIpxHIndex,
       "mscLpIlsFwdrLtFbIpxHTopTable": mscLpIlsFwdrLtFbIpxHTopTable,
       "mscLpIlsFwdrLtFbIpxHTopEntry": mscLpIlsFwdrLtFbIpxHTopEntry,
       "mscLpIlsFwdrLtFbIpxHTData": mscLpIlsFwdrLtFbIpxHTData,
       "mscLpIlsFwdrLtFbTopTable": mscLpIlsFwdrLtFbTopTable,
       "mscLpIlsFwdrLtFbTopEntry": mscLpIlsFwdrLtFbTopEntry,
       "mscLpIlsFwdrLtFbTData": mscLpIlsFwdrLtFbTData,
       "mscLpIlsFwdrLtCntl": mscLpIlsFwdrLtCntl,
       "mscLpIlsFwdrLtCntlRowStatusTable": mscLpIlsFwdrLtCntlRowStatusTable,
       "mscLpIlsFwdrLtCntlRowStatusEntry": mscLpIlsFwdrLtCntlRowStatusEntry,
       "mscLpIlsFwdrLtCntlRowStatus": mscLpIlsFwdrLtCntlRowStatus,
       "mscLpIlsFwdrLtCntlComponentName": mscLpIlsFwdrLtCntlComponentName,
       "mscLpIlsFwdrLtCntlStorageType": mscLpIlsFwdrLtCntlStorageType,
       "mscLpIlsFwdrLtCntlIndex": mscLpIlsFwdrLtCntlIndex,
       "mscLpIlsFwdrLtCntlTopTable": mscLpIlsFwdrLtCntlTopTable,
       "mscLpIlsFwdrLtCntlTopEntry": mscLpIlsFwdrLtCntlTopEntry,
       "mscLpIlsFwdrLtCntlTData": mscLpIlsFwdrLtCntlTData,
       "mscLpIlsFwdrLtTopTable": mscLpIlsFwdrLtTopTable,
       "mscLpIlsFwdrLtTopEntry": mscLpIlsFwdrLtTopEntry,
       "mscLpIlsFwdrLtTData": mscLpIlsFwdrLtTData,
       "mscLpIlsFwdrTest": mscLpIlsFwdrTest,
       "mscLpIlsFwdrTestRowStatusTable": mscLpIlsFwdrTestRowStatusTable,
       "mscLpIlsFwdrTestRowStatusEntry": mscLpIlsFwdrTestRowStatusEntry,
       "mscLpIlsFwdrTestRowStatus": mscLpIlsFwdrTestRowStatus,
       "mscLpIlsFwdrTestComponentName": mscLpIlsFwdrTestComponentName,
       "mscLpIlsFwdrTestStorageType": mscLpIlsFwdrTestStorageType,
       "mscLpIlsFwdrTestIndex": mscLpIlsFwdrTestIndex,
       "mscLpIlsFwdrTestPTOTable": mscLpIlsFwdrTestPTOTable,
       "mscLpIlsFwdrTestPTOEntry": mscLpIlsFwdrTestPTOEntry,
       "mscLpIlsFwdrTestType": mscLpIlsFwdrTestType,
       "mscLpIlsFwdrTestFrmSize": mscLpIlsFwdrTestFrmSize,
       "mscLpIlsFwdrTestDuration": mscLpIlsFwdrTestDuration,
       "mscLpIlsFwdrTestResultsTable": mscLpIlsFwdrTestResultsTable,
       "mscLpIlsFwdrTestResultsEntry": mscLpIlsFwdrTestResultsEntry,
       "mscLpIlsFwdrTestElapsedTime": mscLpIlsFwdrTestElapsedTime,
       "mscLpIlsFwdrTestTimeRemaining": mscLpIlsFwdrTestTimeRemaining,
       "mscLpIlsFwdrTestCauseOfTermination": mscLpIlsFwdrTestCauseOfTermination,
       "mscLpIlsFwdrTestFrmTx": mscLpIlsFwdrTestFrmTx,
       "mscLpIlsFwdrTestBitsTx": mscLpIlsFwdrTestBitsTx,
       "mscLpIlsFwdrTestFrmRx": mscLpIlsFwdrTestFrmRx,
       "mscLpIlsFwdrTestBitsRx": mscLpIlsFwdrTestBitsRx,
       "mscLpIlsFwdrTestErroredFrmRx": mscLpIlsFwdrTestErroredFrmRx,
       "mscLpIlsFwdrIfEntryTable": mscLpIlsFwdrIfEntryTable,
       "mscLpIlsFwdrIfEntryEntry": mscLpIlsFwdrIfEntryEntry,
       "mscLpIlsFwdrIfAdminStatus": mscLpIlsFwdrIfAdminStatus,
       "mscLpIlsFwdrIfIndex": mscLpIlsFwdrIfIndex,
       "mscLpIlsFwdrStateTable": mscLpIlsFwdrStateTable,
       "mscLpIlsFwdrStateEntry": mscLpIlsFwdrStateEntry,
       "mscLpIlsFwdrAdminState": mscLpIlsFwdrAdminState,
       "mscLpIlsFwdrOperationalState": mscLpIlsFwdrOperationalState,
       "mscLpIlsFwdrUsageState": mscLpIlsFwdrUsageState,
       "mscLpIlsFwdrOperStatusTable": mscLpIlsFwdrOperStatusTable,
       "mscLpIlsFwdrOperStatusEntry": mscLpIlsFwdrOperStatusEntry,
       "mscLpIlsFwdrSnmpOperStatus": mscLpIlsFwdrSnmpOperStatus,
       "mscLpIlsFwdrStatsTable": mscLpIlsFwdrStatsTable,
       "mscLpIlsFwdrStatsEntry": mscLpIlsFwdrStatsEntry,
       "mscLpIlsFwdrFramesReceived": mscLpIlsFwdrFramesReceived,
       "mscLpIlsFwdrProcessedCount": mscLpIlsFwdrProcessedCount,
       "mscLpIlsFwdrErrorCount": mscLpIlsFwdrErrorCount,
       "mscLpIlsFwdrFramesDiscarded": mscLpIlsFwdrFramesDiscarded,
       "mscLpIlsFwdrLinkToTrafficSourceTable": mscLpIlsFwdrLinkToTrafficSourceTable,
       "mscLpIlsFwdrLinkToTrafficSourceEntry": mscLpIlsFwdrLinkToTrafficSourceEntry,
       "mscLpIlsFwdrLinkToTrafficSourceValue": mscLpIlsFwdrLinkToTrafficSourceValue,
       "mscLpEth100": mscLpEth100,
       "mscLpEth100RowStatusTable": mscLpEth100RowStatusTable,
       "mscLpEth100RowStatusEntry": mscLpEth100RowStatusEntry,
       "mscLpEth100RowStatus": mscLpEth100RowStatus,
       "mscLpEth100ComponentName": mscLpEth100ComponentName,
       "mscLpEth100StorageType": mscLpEth100StorageType,
       "mscLpEth100Index": mscLpEth100Index,
       "mscLpEth100Lt": mscLpEth100Lt,
       "mscLpEth100LtRowStatusTable": mscLpEth100LtRowStatusTable,
       "mscLpEth100LtRowStatusEntry": mscLpEth100LtRowStatusEntry,
       "mscLpEth100LtRowStatus": mscLpEth100LtRowStatus,
       "mscLpEth100LtComponentName": mscLpEth100LtComponentName,
       "mscLpEth100LtStorageType": mscLpEth100LtStorageType,
       "mscLpEth100LtIndex": mscLpEth100LtIndex,
       "mscLpEth100LtFrmCmp": mscLpEth100LtFrmCmp,
       "mscLpEth100LtFrmCmpRowStatusTable": mscLpEth100LtFrmCmpRowStatusTable,
       "mscLpEth100LtFrmCmpRowStatusEntry": mscLpEth100LtFrmCmpRowStatusEntry,
       "mscLpEth100LtFrmCmpRowStatus": mscLpEth100LtFrmCmpRowStatus,
       "mscLpEth100LtFrmCmpComponentName": mscLpEth100LtFrmCmpComponentName,
       "mscLpEth100LtFrmCmpStorageType": mscLpEth100LtFrmCmpStorageType,
       "mscLpEth100LtFrmCmpIndex": mscLpEth100LtFrmCmpIndex,
       "mscLpEth100LtFrmCmpTopTable": mscLpEth100LtFrmCmpTopTable,
       "mscLpEth100LtFrmCmpTopEntry": mscLpEth100LtFrmCmpTopEntry,
       "mscLpEth100LtFrmCmpTData": mscLpEth100LtFrmCmpTData,
       "mscLpEth100LtFrmCpy": mscLpEth100LtFrmCpy,
       "mscLpEth100LtFrmCpyRowStatusTable": mscLpEth100LtFrmCpyRowStatusTable,
       "mscLpEth100LtFrmCpyRowStatusEntry": mscLpEth100LtFrmCpyRowStatusEntry,
       "mscLpEth100LtFrmCpyRowStatus": mscLpEth100LtFrmCpyRowStatus,
       "mscLpEth100LtFrmCpyComponentName": mscLpEth100LtFrmCpyComponentName,
       "mscLpEth100LtFrmCpyStorageType": mscLpEth100LtFrmCpyStorageType,
       "mscLpEth100LtFrmCpyIndex": mscLpEth100LtFrmCpyIndex,
       "mscLpEth100LtFrmCpyTopTable": mscLpEth100LtFrmCpyTopTable,
       "mscLpEth100LtFrmCpyTopEntry": mscLpEth100LtFrmCpyTopEntry,
       "mscLpEth100LtFrmCpyTData": mscLpEth100LtFrmCpyTData,
       "mscLpEth100LtPrtCfg": mscLpEth100LtPrtCfg,
       "mscLpEth100LtPrtCfgRowStatusTable": mscLpEth100LtPrtCfgRowStatusTable,
       "mscLpEth100LtPrtCfgRowStatusEntry": mscLpEth100LtPrtCfgRowStatusEntry,
       "mscLpEth100LtPrtCfgRowStatus": mscLpEth100LtPrtCfgRowStatus,
       "mscLpEth100LtPrtCfgComponentName": mscLpEth100LtPrtCfgComponentName,
       "mscLpEth100LtPrtCfgStorageType": mscLpEth100LtPrtCfgStorageType,
       "mscLpEth100LtPrtCfgIndex": mscLpEth100LtPrtCfgIndex,
       "mscLpEth100LtPrtCfgTopTable": mscLpEth100LtPrtCfgTopTable,
       "mscLpEth100LtPrtCfgTopEntry": mscLpEth100LtPrtCfgTopEntry,
       "mscLpEth100LtPrtCfgTData": mscLpEth100LtPrtCfgTData,
       "mscLpEth100LtFb": mscLpEth100LtFb,
       "mscLpEth100LtFbRowStatusTable": mscLpEth100LtFbRowStatusTable,
       "mscLpEth100LtFbRowStatusEntry": mscLpEth100LtFbRowStatusEntry,
       "mscLpEth100LtFbRowStatus": mscLpEth100LtFbRowStatus,
       "mscLpEth100LtFbComponentName": mscLpEth100LtFbComponentName,
       "mscLpEth100LtFbStorageType": mscLpEth100LtFbStorageType,
       "mscLpEth100LtFbIndex": mscLpEth100LtFbIndex,
       "mscLpEth100LtFbTxInfo": mscLpEth100LtFbTxInfo,
       "mscLpEth100LtFbTxInfoRowStatusTable": mscLpEth100LtFbTxInfoRowStatusTable,
       "mscLpEth100LtFbTxInfoRowStatusEntry": mscLpEth100LtFbTxInfoRowStatusEntry,
       "mscLpEth100LtFbTxInfoRowStatus": mscLpEth100LtFbTxInfoRowStatus,
       "mscLpEth100LtFbTxInfoComponentName": mscLpEth100LtFbTxInfoComponentName,
       "mscLpEth100LtFbTxInfoStorageType": mscLpEth100LtFbTxInfoStorageType,
       "mscLpEth100LtFbTxInfoIndex": mscLpEth100LtFbTxInfoIndex,
       "mscLpEth100LtFbTxInfoTopTable": mscLpEth100LtFbTxInfoTopTable,
       "mscLpEth100LtFbTxInfoTopEntry": mscLpEth100LtFbTxInfoTopEntry,
       "mscLpEth100LtFbTxInfoTData": mscLpEth100LtFbTxInfoTData,
       "mscLpEth100LtFbFddiMac": mscLpEth100LtFbFddiMac,
       "mscLpEth100LtFbFddiMacRowStatusTable": mscLpEth100LtFbFddiMacRowStatusTable,
       "mscLpEth100LtFbFddiMacRowStatusEntry": mscLpEth100LtFbFddiMacRowStatusEntry,
       "mscLpEth100LtFbFddiMacRowStatus": mscLpEth100LtFbFddiMacRowStatus,
       "mscLpEth100LtFbFddiMacComponentName": mscLpEth100LtFbFddiMacComponentName,
       "mscLpEth100LtFbFddiMacStorageType": mscLpEth100LtFbFddiMacStorageType,
       "mscLpEth100LtFbFddiMacIndex": mscLpEth100LtFbFddiMacIndex,
       "mscLpEth100LtFbFddiMacTopTable": mscLpEth100LtFbFddiMacTopTable,
       "mscLpEth100LtFbFddiMacTopEntry": mscLpEth100LtFbFddiMacTopEntry,
       "mscLpEth100LtFbFddiMacTData": mscLpEth100LtFbFddiMacTData,
       "mscLpEth100LtFbMacEnet": mscLpEth100LtFbMacEnet,
       "mscLpEth100LtFbMacEnetRowStatusTable": mscLpEth100LtFbMacEnetRowStatusTable,
       "mscLpEth100LtFbMacEnetRowStatusEntry": mscLpEth100LtFbMacEnetRowStatusEntry,
       "mscLpEth100LtFbMacEnetRowStatus": mscLpEth100LtFbMacEnetRowStatus,
       "mscLpEth100LtFbMacEnetComponentName": mscLpEth100LtFbMacEnetComponentName,
       "mscLpEth100LtFbMacEnetStorageType": mscLpEth100LtFbMacEnetStorageType,
       "mscLpEth100LtFbMacEnetIndex": mscLpEth100LtFbMacEnetIndex,
       "mscLpEth100LtFbMacEnetTopTable": mscLpEth100LtFbMacEnetTopTable,
       "mscLpEth100LtFbMacEnetTopEntry": mscLpEth100LtFbMacEnetTopEntry,
       "mscLpEth100LtFbMacEnetTData": mscLpEth100LtFbMacEnetTData,
       "mscLpEth100LtFbMacTr": mscLpEth100LtFbMacTr,
       "mscLpEth100LtFbMacTrRowStatusTable": mscLpEth100LtFbMacTrRowStatusTable,
       "mscLpEth100LtFbMacTrRowStatusEntry": mscLpEth100LtFbMacTrRowStatusEntry,
       "mscLpEth100LtFbMacTrRowStatus": mscLpEth100LtFbMacTrRowStatus,
       "mscLpEth100LtFbMacTrComponentName": mscLpEth100LtFbMacTrComponentName,
       "mscLpEth100LtFbMacTrStorageType": mscLpEth100LtFbMacTrStorageType,
       "mscLpEth100LtFbMacTrIndex": mscLpEth100LtFbMacTrIndex,
       "mscLpEth100LtFbMacTrTopTable": mscLpEth100LtFbMacTrTopTable,
       "mscLpEth100LtFbMacTrTopEntry": mscLpEth100LtFbMacTrTopEntry,
       "mscLpEth100LtFbMacTrTData": mscLpEth100LtFbMacTrTData,
       "mscLpEth100LtFbData": mscLpEth100LtFbData,
       "mscLpEth100LtFbDataRowStatusTable": mscLpEth100LtFbDataRowStatusTable,
       "mscLpEth100LtFbDataRowStatusEntry": mscLpEth100LtFbDataRowStatusEntry,
       "mscLpEth100LtFbDataRowStatus": mscLpEth100LtFbDataRowStatus,
       "mscLpEth100LtFbDataComponentName": mscLpEth100LtFbDataComponentName,
       "mscLpEth100LtFbDataStorageType": mscLpEth100LtFbDataStorageType,
       "mscLpEth100LtFbDataIndex": mscLpEth100LtFbDataIndex,
       "mscLpEth100LtFbDataTopTable": mscLpEth100LtFbDataTopTable,
       "mscLpEth100LtFbDataTopEntry": mscLpEth100LtFbDataTopEntry,
       "mscLpEth100LtFbDataTData": mscLpEth100LtFbDataTData,
       "mscLpEth100LtFbIpH": mscLpEth100LtFbIpH,
       "mscLpEth100LtFbIpHRowStatusTable": mscLpEth100LtFbIpHRowStatusTable,
       "mscLpEth100LtFbIpHRowStatusEntry": mscLpEth100LtFbIpHRowStatusEntry,
       "mscLpEth100LtFbIpHRowStatus": mscLpEth100LtFbIpHRowStatus,
       "mscLpEth100LtFbIpHComponentName": mscLpEth100LtFbIpHComponentName,
       "mscLpEth100LtFbIpHStorageType": mscLpEth100LtFbIpHStorageType,
       "mscLpEth100LtFbIpHIndex": mscLpEth100LtFbIpHIndex,
       "mscLpEth100LtFbIpHTopTable": mscLpEth100LtFbIpHTopTable,
       "mscLpEth100LtFbIpHTopEntry": mscLpEth100LtFbIpHTopEntry,
       "mscLpEth100LtFbIpHTData": mscLpEth100LtFbIpHTData,
       "mscLpEth100LtFbLlch": mscLpEth100LtFbLlch,
       "mscLpEth100LtFbLlchRowStatusTable": mscLpEth100LtFbLlchRowStatusTable,
       "mscLpEth100LtFbLlchRowStatusEntry": mscLpEth100LtFbLlchRowStatusEntry,
       "mscLpEth100LtFbLlchRowStatus": mscLpEth100LtFbLlchRowStatus,
       "mscLpEth100LtFbLlchComponentName": mscLpEth100LtFbLlchComponentName,
       "mscLpEth100LtFbLlchStorageType": mscLpEth100LtFbLlchStorageType,
       "mscLpEth100LtFbLlchIndex": mscLpEth100LtFbLlchIndex,
       "mscLpEth100LtFbLlchTopTable": mscLpEth100LtFbLlchTopTable,
       "mscLpEth100LtFbLlchTopEntry": mscLpEth100LtFbLlchTopEntry,
       "mscLpEth100LtFbLlchTData": mscLpEth100LtFbLlchTData,
       "mscLpEth100LtFbAppleH": mscLpEth100LtFbAppleH,
       "mscLpEth100LtFbAppleHRowStatusTable": mscLpEth100LtFbAppleHRowStatusTable,
       "mscLpEth100LtFbAppleHRowStatusEntry": mscLpEth100LtFbAppleHRowStatusEntry,
       "mscLpEth100LtFbAppleHRowStatus": mscLpEth100LtFbAppleHRowStatus,
       "mscLpEth100LtFbAppleHComponentName": mscLpEth100LtFbAppleHComponentName,
       "mscLpEth100LtFbAppleHStorageType": mscLpEth100LtFbAppleHStorageType,
       "mscLpEth100LtFbAppleHIndex": mscLpEth100LtFbAppleHIndex,
       "mscLpEth100LtFbAppleHTopTable": mscLpEth100LtFbAppleHTopTable,
       "mscLpEth100LtFbAppleHTopEntry": mscLpEth100LtFbAppleHTopEntry,
       "mscLpEth100LtFbAppleHTData": mscLpEth100LtFbAppleHTData,
       "mscLpEth100LtFbIpxH": mscLpEth100LtFbIpxH,
       "mscLpEth100LtFbIpxHRowStatusTable": mscLpEth100LtFbIpxHRowStatusTable,
       "mscLpEth100LtFbIpxHRowStatusEntry": mscLpEth100LtFbIpxHRowStatusEntry,
       "mscLpEth100LtFbIpxHRowStatus": mscLpEth100LtFbIpxHRowStatus,
       "mscLpEth100LtFbIpxHComponentName": mscLpEth100LtFbIpxHComponentName,
       "mscLpEth100LtFbIpxHStorageType": mscLpEth100LtFbIpxHStorageType,
       "mscLpEth100LtFbIpxHIndex": mscLpEth100LtFbIpxHIndex,
       "mscLpEth100LtFbIpxHTopTable": mscLpEth100LtFbIpxHTopTable,
       "mscLpEth100LtFbIpxHTopEntry": mscLpEth100LtFbIpxHTopEntry,
       "mscLpEth100LtFbIpxHTData": mscLpEth100LtFbIpxHTData,
       "mscLpEth100LtFbTopTable": mscLpEth100LtFbTopTable,
       "mscLpEth100LtFbTopEntry": mscLpEth100LtFbTopEntry,
       "mscLpEth100LtFbTData": mscLpEth100LtFbTData,
       "mscLpEth100LtCntl": mscLpEth100LtCntl,
       "mscLpEth100LtCntlRowStatusTable": mscLpEth100LtCntlRowStatusTable,
       "mscLpEth100LtCntlRowStatusEntry": mscLpEth100LtCntlRowStatusEntry,
       "mscLpEth100LtCntlRowStatus": mscLpEth100LtCntlRowStatus,
       "mscLpEth100LtCntlComponentName": mscLpEth100LtCntlComponentName,
       "mscLpEth100LtCntlStorageType": mscLpEth100LtCntlStorageType,
       "mscLpEth100LtCntlIndex": mscLpEth100LtCntlIndex,
       "mscLpEth100LtCntlTopTable": mscLpEth100LtCntlTopTable,
       "mscLpEth100LtCntlTopEntry": mscLpEth100LtCntlTopEntry,
       "mscLpEth100LtCntlTData": mscLpEth100LtCntlTData,
       "mscLpEth100LtTopTable": mscLpEth100LtTopTable,
       "mscLpEth100LtTopEntry": mscLpEth100LtTopEntry,
       "mscLpEth100LtTData": mscLpEth100LtTData,
       "mscLpEth100Test": mscLpEth100Test,
       "mscLpEth100TestRowStatusTable": mscLpEth100TestRowStatusTable,
       "mscLpEth100TestRowStatusEntry": mscLpEth100TestRowStatusEntry,
       "mscLpEth100TestRowStatus": mscLpEth100TestRowStatus,
       "mscLpEth100TestComponentName": mscLpEth100TestComponentName,
       "mscLpEth100TestStorageType": mscLpEth100TestStorageType,
       "mscLpEth100TestIndex": mscLpEth100TestIndex,
       "mscLpEth100TestPTOTable": mscLpEth100TestPTOTable,
       "mscLpEth100TestPTOEntry": mscLpEth100TestPTOEntry,
       "mscLpEth100TestType": mscLpEth100TestType,
       "mscLpEth100TestFrmSize": mscLpEth100TestFrmSize,
       "mscLpEth100TestDuration": mscLpEth100TestDuration,
       "mscLpEth100TestResultsTable": mscLpEth100TestResultsTable,
       "mscLpEth100TestResultsEntry": mscLpEth100TestResultsEntry,
       "mscLpEth100TestElapsedTime": mscLpEth100TestElapsedTime,
       "mscLpEth100TestTimeRemaining": mscLpEth100TestTimeRemaining,
       "mscLpEth100TestCauseOfTermination": mscLpEth100TestCauseOfTermination,
       "mscLpEth100TestFrmTx": mscLpEth100TestFrmTx,
       "mscLpEth100TestBitsTx": mscLpEth100TestBitsTx,
       "mscLpEth100TestFrmRx": mscLpEth100TestFrmRx,
       "mscLpEth100TestBitsRx": mscLpEth100TestBitsRx,
       "mscLpEth100TestErroredFrmRx": mscLpEth100TestErroredFrmRx,
       "mscLpEth100CidDataTable": mscLpEth100CidDataTable,
       "mscLpEth100CidDataEntry": mscLpEth100CidDataEntry,
       "mscLpEth100CustomerIdentifier": mscLpEth100CustomerIdentifier,
       "mscLpEth100IfEntryTable": mscLpEth100IfEntryTable,
       "mscLpEth100IfEntryEntry": mscLpEth100IfEntryEntry,
       "mscLpEth100IfAdminStatus": mscLpEth100IfAdminStatus,
       "mscLpEth100IfIndex": mscLpEth100IfIndex,
       "mscLpEth100ProvTable": mscLpEth100ProvTable,
       "mscLpEth100ProvEntry": mscLpEth100ProvEntry,
       "mscLpEth100DuplexMode": mscLpEth100DuplexMode,
       "mscLpEth100LineSpeed": mscLpEth100LineSpeed,
       "mscLpEth100AutoNegotiation": mscLpEth100AutoNegotiation,
       "mscLpEth100ApplicationFramerName": mscLpEth100ApplicationFramerName,
       "mscLpEth100AdminInfoTable": mscLpEth100AdminInfoTable,
       "mscLpEth100AdminInfoEntry": mscLpEth100AdminInfoEntry,
       "mscLpEth100Vendor": mscLpEth100Vendor,
       "mscLpEth100CommentText": mscLpEth100CommentText,
       "mscLpEth100StateTable": mscLpEth100StateTable,
       "mscLpEth100StateEntry": mscLpEth100StateEntry,
       "mscLpEth100AdminState": mscLpEth100AdminState,
       "mscLpEth100OperationalState": mscLpEth100OperationalState,
       "mscLpEth100UsageState": mscLpEth100UsageState,
       "mscLpEth100OperStatusTable": mscLpEth100OperStatusTable,
       "mscLpEth100OperStatusEntry": mscLpEth100OperStatusEntry,
       "mscLpEth100SnmpOperStatus": mscLpEth100SnmpOperStatus,
       "mscLpEth100OperTable": mscLpEth100OperTable,
       "mscLpEth100OperEntry": mscLpEth100OperEntry,
       "mscLpEth100MacAddress": mscLpEth100MacAddress,
       "mscLpEth100AutoNegStatus": mscLpEth100AutoNegStatus,
       "mscLpEth100ActualLineSpeed": mscLpEth100ActualLineSpeed,
       "mscLpEth100ActualDuplexMode": mscLpEth100ActualDuplexMode,
       "mscLpEth100Eth100StatsTable": mscLpEth100Eth100StatsTable,
       "mscLpEth100Eth100StatsEntry": mscLpEth100Eth100StatsEntry,
       "mscLpEth100FramesTransmittedOk": mscLpEth100FramesTransmittedOk,
       "mscLpEth100FramesReceivedOk": mscLpEth100FramesReceivedOk,
       "mscLpEth100OctetsTransmittedOk": mscLpEth100OctetsTransmittedOk,
       "mscLpEth100OctetsReceivedOk": mscLpEth100OctetsReceivedOk,
       "mscLpEth100UndersizeFrames": mscLpEth100UndersizeFrames,
       "mscLpEth100ReceivedOctetsIntoRouterBr": mscLpEth100ReceivedOctetsIntoRouterBr,
       "mscLpEth100ReceivedFramesIntoRouterBr": mscLpEth100ReceivedFramesIntoRouterBr,
       "mscLpEth100StatsTable": mscLpEth100StatsTable,
       "mscLpEth100StatsEntry": mscLpEth100StatsEntry,
       "mscLpEth100AlignmentErrors": mscLpEth100AlignmentErrors,
       "mscLpEth100FcsErrors": mscLpEth100FcsErrors,
       "mscLpEth100SingleCollisionFrames": mscLpEth100SingleCollisionFrames,
       "mscLpEth100MultipleCollisionFrames": mscLpEth100MultipleCollisionFrames,
       "mscLpEth100SqeTestErrors": mscLpEth100SqeTestErrors,
       "mscLpEth100DeferredTransmissions": mscLpEth100DeferredTransmissions,
       "mscLpEth100LateCollisions": mscLpEth100LateCollisions,
       "mscLpEth100ExcessiveCollisions": mscLpEth100ExcessiveCollisions,
       "mscLpEth100MacTransmitErrors": mscLpEth100MacTransmitErrors,
       "mscLpEth100CarrierSenseErrors": mscLpEth100CarrierSenseErrors,
       "mscLpEth100FrameTooLongs": mscLpEth100FrameTooLongs,
       "mscLpEth100MacReceiveErrors": mscLpEth100MacReceiveErrors,
       "mscLa": mscLa,
       "mscLaRowStatusTable": mscLaRowStatusTable,
       "mscLaRowStatusEntry": mscLaRowStatusEntry,
       "mscLaRowStatus": mscLaRowStatus,
       "mscLaComponentName": mscLaComponentName,
       "mscLaStorageType": mscLaStorageType,
       "mscLaIndex": mscLaIndex,
       "mscLaFramer": mscLaFramer,
       "mscLaFramerRowStatusTable": mscLaFramerRowStatusTable,
       "mscLaFramerRowStatusEntry": mscLaFramerRowStatusEntry,
       "mscLaFramerRowStatus": mscLaFramerRowStatus,
       "mscLaFramerComponentName": mscLaFramerComponentName,
       "mscLaFramerStorageType": mscLaFramerStorageType,
       "mscLaFramerIndex": mscLaFramerIndex,
       "mscLaFramerProvTable": mscLaFramerProvTable,
       "mscLaFramerProvEntry": mscLaFramerProvEntry,
       "mscLaFramerInterfaceName": mscLaFramerInterfaceName,
       "mscLaFramerInterfaceNamesTable": mscLaFramerInterfaceNamesTable,
       "mscLaFramerInterfaceNamesEntry": mscLaFramerInterfaceNamesEntry,
       "mscLaFramerInterfaceNamesValue": mscLaFramerInterfaceNamesValue,
       "mscLaFramerInterfaceNamesRowStatus": mscLaFramerInterfaceNamesRowStatus,
       "mscLaCidDataTable": mscLaCidDataTable,
       "mscLaCidDataEntry": mscLaCidDataEntry,
       "mscLaCustomerIdentifier": mscLaCustomerIdentifier,
       "mscLaMediaProvTable": mscLaMediaProvTable,
       "mscLaMediaProvEntry": mscLaMediaProvEntry,
       "mscLaLinkToProtocolPort": mscLaLinkToProtocolPort,
       "mscLaIfEntryTable": mscLaIfEntryTable,
       "mscLaIfEntryEntry": mscLaIfEntryEntry,
       "mscLaIfAdminStatus": mscLaIfAdminStatus,
       "mscLaIfIndex": mscLaIfIndex,
       "mscLaStateTable": mscLaStateTable,
       "mscLaStateEntry": mscLaStateEntry,
       "mscLaAdminState": mscLaAdminState,
       "mscLaOperationalState": mscLaOperationalState,
       "mscLaUsageState": mscLaUsageState,
       "mscLaOperStatusTable": mscLaOperStatusTable,
       "mscLaOperStatusEntry": mscLaOperStatusEntry,
       "mscLaSnmpOperStatus": mscLaSnmpOperStatus,
       "lanDriversMIB": lanDriversMIB,
       "lanDriversGroup": lanDriversGroup,
       "lanDriversGroupCA": lanDriversGroupCA,
       "lanDriversGroupCA02": lanDriversGroupCA02,
       "lanDriversGroupCA02A": lanDriversGroupCA02A,
       "lanDriversCapabilities": lanDriversCapabilities,
       "lanDriversCapabilitiesCA": lanDriversCapabilitiesCA,
       "lanDriversCapabilitiesCA02": lanDriversCapabilitiesCA02,
       "lanDriversCapabilitiesCA02A": lanDriversCapabilitiesCA02A}
)
