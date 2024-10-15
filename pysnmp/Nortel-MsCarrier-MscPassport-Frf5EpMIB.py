# SNMP MIB module (Nortel-MsCarrier-MscPassport-Frf5EpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-Frf5EpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:32 2024
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

(mscMcsMgr,
 mscMcsMgrIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-McsMgrMIB",
    "mscMcsMgr",
    "mscMcsMgrIndex")

(Counter32,
 DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 HexString,
 IntegerSequence,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "HexString",
    "IntegerSequence",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
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

_MscMcsMgrFrf5EpG_ObjectIdentity = ObjectIdentity
mscMcsMgrFrf5EpG = _MscMcsMgrFrf5EpG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14)
)
_MscMcsMgrFrf5EpGRowStatusTable_Object = MibTable
mscMcsMgrFrf5EpGRowStatusTable = _MscMcsMgrFrf5EpGRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGRowStatusTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGRowStatusEntry_Object = MibTableRow
mscMcsMgrFrf5EpGRowStatusEntry = _MscMcsMgrFrf5EpGRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 1, 1)
)
mscMcsMgrFrf5EpGRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGRowStatusEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGRowStatus = _MscMcsMgrFrf5EpGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 1, 1, 1),
    _MscMcsMgrFrf5EpGRowStatus_Type()
)
mscMcsMgrFrf5EpGRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGComponentName_Type = DisplayString
_MscMcsMgrFrf5EpGComponentName_Object = MibTableColumn
mscMcsMgrFrf5EpGComponentName = _MscMcsMgrFrf5EpGComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 1, 1, 2),
    _MscMcsMgrFrf5EpGComponentName_Type()
)
mscMcsMgrFrf5EpGComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGComponentName.setStatus("mandatory")
_MscMcsMgrFrf5EpGStorageType_Type = StorageType
_MscMcsMgrFrf5EpGStorageType_Object = MibTableColumn
mscMcsMgrFrf5EpGStorageType = _MscMcsMgrFrf5EpGStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 1, 1, 4),
    _MscMcsMgrFrf5EpGStorageType_Type()
)
mscMcsMgrFrf5EpGStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGStorageType.setStatus("mandatory")


class _MscMcsMgrFrf5EpGIndex_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MscMcsMgrFrf5EpGIndex_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGIndex_Object = MibTableColumn
mscMcsMgrFrf5EpGIndex = _MscMcsMgrFrf5EpGIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 1, 1, 10),
    _MscMcsMgrFrf5EpGIndex_Type()
)
mscMcsMgrFrf5EpGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGIndex.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddr_ObjectIdentity = ObjectIdentity
mscMcsMgrFrf5EpGAddr = _MscMcsMgrFrf5EpGAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2)
)
_MscMcsMgrFrf5EpGAddrRowStatusTable_Object = MibTable
mscMcsMgrFrf5EpGAddrRowStatusTable = _MscMcsMgrFrf5EpGAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrRowStatusTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrRowStatusEntry_Object = MibTableRow
mscMcsMgrFrf5EpGAddrRowStatusEntry = _MscMcsMgrFrf5EpGAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 1, 1)
)
mscMcsMgrFrf5EpGAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrRowStatusEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGAddrRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrRowStatus = _MscMcsMgrFrf5EpGAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 1, 1, 1),
    _MscMcsMgrFrf5EpGAddrRowStatus_Type()
)
mscMcsMgrFrf5EpGAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrComponentName_Type = DisplayString
_MscMcsMgrFrf5EpGAddrComponentName_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrComponentName = _MscMcsMgrFrf5EpGAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 1, 1, 2),
    _MscMcsMgrFrf5EpGAddrComponentName_Type()
)
mscMcsMgrFrf5EpGAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrComponentName.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrStorageType_Type = StorageType
_MscMcsMgrFrf5EpGAddrStorageType_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrStorageType = _MscMcsMgrFrf5EpGAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 1, 1, 4),
    _MscMcsMgrFrf5EpGAddrStorageType_Type()
)
mscMcsMgrFrf5EpGAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrStorageType.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrIndex_Type = NonReplicated
_MscMcsMgrFrf5EpGAddrIndex_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrIndex = _MscMcsMgrFrf5EpGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 1, 1, 10),
    _MscMcsMgrFrf5EpGAddrIndex_Type()
)
mscMcsMgrFrf5EpGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrIndex.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrProvTable_Object = MibTable
mscMcsMgrFrf5EpGAddrProvTable = _MscMcsMgrFrf5EpGAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrProvTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrProvEntry_Object = MibTableRow
mscMcsMgrFrf5EpGAddrProvEntry = _MscMcsMgrFrf5EpGAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 10, 1)
)
mscMcsMgrFrf5EpGAddrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrProvEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGAddrRemoteAddress_Type(AsciiString):
    """Custom type mscMcsMgrFrf5EpGAddrRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_MscMcsMgrFrf5EpGAddrRemoteAddress_Type.__name__ = "AsciiString"
_MscMcsMgrFrf5EpGAddrRemoteAddress_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrRemoteAddress = _MscMcsMgrFrf5EpGAddrRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 10, 1, 1),
    _MscMcsMgrFrf5EpGAddrRemoteAddress_Type()
)
mscMcsMgrFrf5EpGAddrRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrRemoteAddress.setStatus("mandatory")


class _MscMcsMgrFrf5EpGAddrCommentText_Type(AsciiString):
    """Custom type mscMcsMgrFrf5EpGAddrCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_MscMcsMgrFrf5EpGAddrCommentText_Type.__name__ = "AsciiString"
_MscMcsMgrFrf5EpGAddrCommentText_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrCommentText = _MscMcsMgrFrf5EpGAddrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 10, 1, 2),
    _MscMcsMgrFrf5EpGAddrCommentText_Type()
)
mscMcsMgrFrf5EpGAddrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrCommentText.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrAddrPreTable_Object = MibTable
mscMcsMgrFrf5EpGAddrAddrPreTable = _MscMcsMgrFrf5EpGAddrAddrPreTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 362)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrAddrPreTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrAddrPreEntry_Object = MibTableRow
mscMcsMgrFrf5EpGAddrAddrPreEntry = _MscMcsMgrFrf5EpGAddrAddrPreEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 362, 1)
)
mscMcsMgrFrf5EpGAddrAddrPreEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGAddrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGAddrAddrPreValue"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrAddrPreEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGAddrAddrPreValue_Type(AsciiString):
    """Custom type mscMcsMgrFrf5EpGAddrAddrPreValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_MscMcsMgrFrf5EpGAddrAddrPreValue_Type.__name__ = "AsciiString"
_MscMcsMgrFrf5EpGAddrAddrPreValue_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrAddrPreValue = _MscMcsMgrFrf5EpGAddrAddrPreValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 362, 1, 1),
    _MscMcsMgrFrf5EpGAddrAddrPreValue_Type()
)
mscMcsMgrFrf5EpGAddrAddrPreValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrAddrPreValue.setStatus("mandatory")
_MscMcsMgrFrf5EpGAddrAddrPreRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGAddrAddrPreRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGAddrAddrPreRowStatus = _MscMcsMgrFrf5EpGAddrAddrPreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 2, 362, 1, 2),
    _MscMcsMgrFrf5EpGAddrAddrPreRowStatus_Type()
)
mscMcsMgrFrf5EpGAddrAddrPreRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGAddrAddrPreRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEp_ObjectIdentity = ObjectIdentity
mscMcsMgrFrf5EpGEp = _MscMcsMgrFrf5EpGEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3)
)
_MscMcsMgrFrf5EpGEpRowStatusTable_Object = MibTable
mscMcsMgrFrf5EpGEpRowStatusTable = _MscMcsMgrFrf5EpGEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpRowStatusTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpRowStatusEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpRowStatusEntry = _MscMcsMgrFrf5EpGEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 1, 1)
)
mscMcsMgrFrf5EpGEpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpRowStatusEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGEpRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpRowStatus = _MscMcsMgrFrf5EpGEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 1, 1, 1),
    _MscMcsMgrFrf5EpGEpRowStatus_Type()
)
mscMcsMgrFrf5EpGEpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpComponentName_Type = DisplayString
_MscMcsMgrFrf5EpGEpComponentName_Object = MibTableColumn
mscMcsMgrFrf5EpGEpComponentName = _MscMcsMgrFrf5EpGEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 1, 1, 2),
    _MscMcsMgrFrf5EpGEpComponentName_Type()
)
mscMcsMgrFrf5EpGEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpComponentName.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpStorageType_Type = StorageType
_MscMcsMgrFrf5EpGEpStorageType_Object = MibTableColumn
mscMcsMgrFrf5EpGEpStorageType = _MscMcsMgrFrf5EpGEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 1, 1, 4),
    _MscMcsMgrFrf5EpGEpStorageType_Type()
)
mscMcsMgrFrf5EpGEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpStorageType.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpIndex_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscMcsMgrFrf5EpGEpIndex_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpIndex_Object = MibTableColumn
mscMcsMgrFrf5EpGEpIndex = _MscMcsMgrFrf5EpGEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 1, 1, 10),
    _MscMcsMgrFrf5EpGEpIndex_Type()
)
mscMcsMgrFrf5EpGEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpIndex.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmi_ObjectIdentity = ObjectIdentity
mscMcsMgrFrf5EpGEpLmi = _MscMcsMgrFrf5EpGEpLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2)
)
_MscMcsMgrFrf5EpGEpLmiRowStatusTable_Object = MibTable
mscMcsMgrFrf5EpGEpLmiRowStatusTable = _MscMcsMgrFrf5EpGEpLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiRowStatusTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiRowStatusEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpLmiRowStatusEntry = _MscMcsMgrFrf5EpGEpLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 1, 1)
)
mscMcsMgrFrf5EpGEpLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiRowStatusEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGEpLmiRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiRowStatus = _MscMcsMgrFrf5EpGEpLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 1, 1, 1),
    _MscMcsMgrFrf5EpGEpLmiRowStatus_Type()
)
mscMcsMgrFrf5EpGEpLmiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiComponentName_Type = DisplayString
_MscMcsMgrFrf5EpGEpLmiComponentName_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiComponentName = _MscMcsMgrFrf5EpGEpLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 1, 1, 2),
    _MscMcsMgrFrf5EpGEpLmiComponentName_Type()
)
mscMcsMgrFrf5EpGEpLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiComponentName.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiStorageType_Type = StorageType
_MscMcsMgrFrf5EpGEpLmiStorageType_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiStorageType = _MscMcsMgrFrf5EpGEpLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 1, 1, 4),
    _MscMcsMgrFrf5EpGEpLmiStorageType_Type()
)
mscMcsMgrFrf5EpGEpLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiStorageType.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiIndex_Type = NonReplicated
_MscMcsMgrFrf5EpGEpLmiIndex_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiIndex = _MscMcsMgrFrf5EpGEpLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 1, 1, 10),
    _MscMcsMgrFrf5EpGEpLmiIndex_Type()
)
mscMcsMgrFrf5EpGEpLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiIndex.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiParmsTable_Object = MibTable
mscMcsMgrFrf5EpGEpLmiParmsTable = _MscMcsMgrFrf5EpGEpLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiParmsTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiParmsEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpLmiParmsEntry = _MscMcsMgrFrf5EpGEpLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10, 1)
)
mscMcsMgrFrf5EpGEpLmiParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiParmsEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiProcedures_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpLmiProcedures based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("ccitt", 3),
          ("none", 0))
    )


_MscMcsMgrFrf5EpGEpLmiProcedures_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpLmiProcedures_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiProcedures = _MscMcsMgrFrf5EpGEpLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10, 1, 1),
    _MscMcsMgrFrf5EpGEpLmiProcedures_Type()
)
mscMcsMgrFrf5EpGEpLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiProcedures.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiAsyncStatusReport_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpLmiAsyncStatusReport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MscMcsMgrFrf5EpGEpLmiAsyncStatusReport_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpLmiAsyncStatusReport_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiAsyncStatusReport = _MscMcsMgrFrf5EpGEpLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10, 1, 2),
    _MscMcsMgrFrf5EpGEpLmiAsyncStatusReport_Type()
)
mscMcsMgrFrf5EpGEpLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiAsyncStatusReport.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscMcsMgrFrf5EpGEpLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpLmiErrorEventThreshold_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiErrorEventThreshold = _MscMcsMgrFrf5EpGEpLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10, 1, 3),
    _MscMcsMgrFrf5EpGEpLmiErrorEventThreshold_Type()
)
mscMcsMgrFrf5EpGEpLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiErrorEventThreshold.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiEventCount_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscMcsMgrFrf5EpGEpLmiEventCount_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpLmiEventCount_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiEventCount = _MscMcsMgrFrf5EpGEpLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10, 1, 4),
    _MscMcsMgrFrf5EpGEpLmiEventCount_Type()
)
mscMcsMgrFrf5EpGEpLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiEventCount.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiCheckPointTimer_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpLmiCheckPointTimer based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_MscMcsMgrFrf5EpGEpLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpLmiCheckPointTimer_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiCheckPointTimer = _MscMcsMgrFrf5EpGEpLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10, 1, 5),
    _MscMcsMgrFrf5EpGEpLmiCheckPointTimer_Type()
)
mscMcsMgrFrf5EpGEpLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiCheckPointTimer.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiSide_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpLmiSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("network", 0),
          ("user", 1))
    )


_MscMcsMgrFrf5EpGEpLmiSide_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpLmiSide_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiSide = _MscMcsMgrFrf5EpGEpLmiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 10, 1, 8),
    _MscMcsMgrFrf5EpGEpLmiSide_Type()
)
mscMcsMgrFrf5EpGEpLmiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiSide.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiNniParmsTable_Object = MibTable
mscMcsMgrFrf5EpGEpLmiNniParmsTable = _MscMcsMgrFrf5EpGEpLmiNniParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiNniParmsTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiNniParmsEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpLmiNniParmsEntry = _MscMcsMgrFrf5EpGEpLmiNniParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 11, 1)
)
mscMcsMgrFrf5EpGEpLmiNniParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiNniParmsEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles = _MscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 11, 1, 1),
    _MscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles_Type()
)
mscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpLmiLinkVerificationTimer based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_MscMcsMgrFrf5EpGEpLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpLmiLinkVerificationTimer_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiLinkVerificationTimer = _MscMcsMgrFrf5EpGEpLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 11, 1, 2),
    _MscMcsMgrFrf5EpGEpLmiLinkVerificationTimer_Type()
)
mscMcsMgrFrf5EpGEpLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiLinkVerificationTimer.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiStateTable_Object = MibTable
mscMcsMgrFrf5EpGEpLmiStateTable = _MscMcsMgrFrf5EpGEpLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 12)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiStateTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiStateEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpLmiStateEntry = _MscMcsMgrFrf5EpGEpLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 12, 1)
)
mscMcsMgrFrf5EpGEpLmiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiStateEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiAdminState_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpLmiAdminState based on Integer32"""
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


_MscMcsMgrFrf5EpGEpLmiAdminState_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpLmiAdminState_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiAdminState = _MscMcsMgrFrf5EpGEpLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 12, 1, 1),
    _MscMcsMgrFrf5EpGEpLmiAdminState_Type()
)
mscMcsMgrFrf5EpGEpLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiAdminState.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiOperationalState_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpLmiOperationalState based on Integer32"""
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


_MscMcsMgrFrf5EpGEpLmiOperationalState_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpLmiOperationalState_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiOperationalState = _MscMcsMgrFrf5EpGEpLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 12, 1, 2),
    _MscMcsMgrFrf5EpGEpLmiOperationalState_Type()
)
mscMcsMgrFrf5EpGEpLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiOperationalState.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiUsageState_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpLmiUsageState based on Integer32"""
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


_MscMcsMgrFrf5EpGEpLmiUsageState_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpLmiUsageState_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiUsageState = _MscMcsMgrFrf5EpGEpLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 12, 1, 3),
    _MscMcsMgrFrf5EpGEpLmiUsageState_Type()
)
mscMcsMgrFrf5EpGEpLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiUsageState.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiPsiTable_Object = MibTable
mscMcsMgrFrf5EpGEpLmiPsiTable = _MscMcsMgrFrf5EpGEpLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 13)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiPsiTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiPsiEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpLmiPsiEntry = _MscMcsMgrFrf5EpGEpLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 13, 1)
)
mscMcsMgrFrf5EpGEpLmiPsiEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiPsiEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiProtocolStatus_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpLmiProtocolStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("errorCondition", 0),
          ("normalCondition", 1))
    )


_MscMcsMgrFrf5EpGEpLmiProtocolStatus_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpLmiProtocolStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiProtocolStatus = _MscMcsMgrFrf5EpGEpLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 13, 1, 1),
    _MscMcsMgrFrf5EpGEpLmiProtocolStatus_Type()
)
mscMcsMgrFrf5EpGEpLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiProtocolStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiStatsTable_Object = MibTable
mscMcsMgrFrf5EpGEpLmiStatsTable = _MscMcsMgrFrf5EpGEpLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiStatsTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiStatsEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpLmiStatsEntry = _MscMcsMgrFrf5EpGEpLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1)
)
mscMcsMgrFrf5EpGEpLmiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiStatsEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface = _MscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 1),
    _MscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Type()
)
mscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiFullStatusToInterface_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiFullStatusToInterface_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiFullStatusToInterface = _MscMcsMgrFrf5EpGEpLmiFullStatusToInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 2),
    _MscMcsMgrFrf5EpGEpLmiFullStatusToInterface_Type()
)
mscMcsMgrFrf5EpGEpLmiFullStatusToInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiFullStatusToInterface.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface = _MscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 3),
    _MscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Type()
)
mscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface = _MscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 4),
    _MscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Type()
)
mscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type mscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_MscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory = _MscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 5),
    _MscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory_Type()
)
mscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLmiUserSideEventHistory_Type(AsciiString):
    """Custom type mscMcsMgrFrf5EpGEpLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscMcsMgrFrf5EpGEpLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_MscMcsMgrFrf5EpGEpLmiUserSideEventHistory_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiUserSideEventHistory = _MscMcsMgrFrf5EpGEpLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 6),
    _MscMcsMgrFrf5EpGEpLmiUserSideEventHistory_Type()
)
mscMcsMgrFrf5EpGEpLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiUserSideEventHistory.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiProtocolErrors_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiProtocolErrors_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiProtocolErrors = _MscMcsMgrFrf5EpGEpLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 7),
    _MscMcsMgrFrf5EpGEpLmiProtocolErrors_Type()
)
mscMcsMgrFrf5EpGEpLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiProtocolErrors.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiUnexpectedIes_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiUnexpectedIes_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiUnexpectedIes = _MscMcsMgrFrf5EpGEpLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 8),
    _MscMcsMgrFrf5EpGEpLmiUnexpectedIes_Type()
)
mscMcsMgrFrf5EpGEpLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiUnexpectedIes.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiSequenceErrors_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiSequenceErrors_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiSequenceErrors = _MscMcsMgrFrf5EpGEpLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 9),
    _MscMcsMgrFrf5EpGEpLmiSequenceErrors_Type()
)
mscMcsMgrFrf5EpGEpLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiSequenceErrors.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiStatusSequenceErrors_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiStatusSequenceErrors_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiStatusSequenceErrors = _MscMcsMgrFrf5EpGEpLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 10),
    _MscMcsMgrFrf5EpGEpLmiStatusSequenceErrors_Type()
)
mscMcsMgrFrf5EpGEpLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiStatusSequenceErrors.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiUnexpectedReports_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiUnexpectedReports_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiUnexpectedReports = _MscMcsMgrFrf5EpGEpLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 11),
    _MscMcsMgrFrf5EpGEpLmiUnexpectedReports_Type()
)
mscMcsMgrFrf5EpGEpLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiUnexpectedReports.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts = _MscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 12),
    _MscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts_Type()
)
mscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiNoStatusReportCount_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiNoStatusReportCount_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiNoStatusReportCount = _MscMcsMgrFrf5EpGEpLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 13),
    _MscMcsMgrFrf5EpGEpLmiNoStatusReportCount_Type()
)
mscMcsMgrFrf5EpGEpLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiNoStatusReportCount.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf = _MscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 14),
    _MscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Type()
)
mscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf_Type = Counter32
_MscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf = _MscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 2, 14, 1, 15),
    _MscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf_Type()
)
mscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpd_ObjectIdentity = ObjectIdentity
mscMcsMgrFrf5EpGEpEpd = _MscMcsMgrFrf5EpGEpEpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3)
)
_MscMcsMgrFrf5EpGEpEpdRowStatusTable_Object = MibTable
mscMcsMgrFrf5EpGEpEpdRowStatusTable = _MscMcsMgrFrf5EpGEpEpdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdRowStatusTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdRowStatusEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpEpdRowStatusEntry = _MscMcsMgrFrf5EpGEpEpdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 1, 1)
)
mscMcsMgrFrf5EpGEpEpdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpEpdIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdRowStatusEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGEpEpdRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdRowStatus = _MscMcsMgrFrf5EpGEpEpdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 1, 1, 1),
    _MscMcsMgrFrf5EpGEpEpdRowStatus_Type()
)
mscMcsMgrFrf5EpGEpEpdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdComponentName_Type = DisplayString
_MscMcsMgrFrf5EpGEpEpdComponentName_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdComponentName = _MscMcsMgrFrf5EpGEpEpdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 1, 1, 2),
    _MscMcsMgrFrf5EpGEpEpdComponentName_Type()
)
mscMcsMgrFrf5EpGEpEpdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdComponentName.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdStorageType_Type = StorageType
_MscMcsMgrFrf5EpGEpEpdStorageType_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdStorageType = _MscMcsMgrFrf5EpGEpEpdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 1, 1, 4),
    _MscMcsMgrFrf5EpGEpEpdStorageType_Type()
)
mscMcsMgrFrf5EpGEpEpdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdStorageType.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdIndex_Type = NonReplicated
_MscMcsMgrFrf5EpGEpEpdIndex_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdIndex = _MscMcsMgrFrf5EpGEpEpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 1, 1, 10),
    _MscMcsMgrFrf5EpGEpEpdIndex_Type()
)
mscMcsMgrFrf5EpGEpEpdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdIndex.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdProvTable_Object = MibTable
mscMcsMgrFrf5EpGEpEpdProvTable = _MscMcsMgrFrf5EpGEpEpdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdProvTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdProvEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpEpdProvEntry = _MscMcsMgrFrf5EpGEpEpdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1)
)
mscMcsMgrFrf5EpGEpEpdProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpEpdIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdProvEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Type(IntegerSequence):
    """Custom type mscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_MscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Type.__name__ = "IntegerSequence"
_MscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier = _MscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 3),
    _MscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Type()
)
mscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdConnectionTransferPriority_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpEpdConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscMcsMgrFrf5EpGEpEpdConnectionTransferPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpEpdConnectionTransferPriority_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdConnectionTransferPriority = _MscMcsMgrFrf5EpGEpEpdConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 4),
    _MscMcsMgrFrf5EpGEpEpdConnectionTransferPriority_Type()
)
mscMcsMgrFrf5EpGEpEpdConnectionTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdConnectionTransferPriority.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdCommittedInformationRate_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpEpdCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscMcsMgrFrf5EpGEpEpdCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpEpdCommittedInformationRate_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdCommittedInformationRate = _MscMcsMgrFrf5EpGEpEpdCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 5),
    _MscMcsMgrFrf5EpGEpEpdCommittedInformationRate_Type()
)
mscMcsMgrFrf5EpGEpEpdCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdCommittedInformationRate.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdExcessInformationRate_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpEpdExcessInformationRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscMcsMgrFrf5EpGEpEpdExcessInformationRate_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpEpdExcessInformationRate_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdExcessInformationRate = _MscMcsMgrFrf5EpGEpEpdExcessInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 6),
    _MscMcsMgrFrf5EpGEpEpdExcessInformationRate_Type()
)
mscMcsMgrFrf5EpGEpEpdExcessInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdExcessInformationRate.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdCommittedBurstSize_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpEpdCommittedBurstSize based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscMcsMgrFrf5EpGEpEpdCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpEpdCommittedBurstSize_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdCommittedBurstSize = _MscMcsMgrFrf5EpGEpEpdCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 7),
    _MscMcsMgrFrf5EpGEpEpdCommittedBurstSize_Type()
)
mscMcsMgrFrf5EpGEpEpdCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdCommittedBurstSize.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdType_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpEpdType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_MscMcsMgrFrf5EpGEpEpdType_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpEpdType_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdType = _MscMcsMgrFrf5EpGEpEpdType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 8),
    _MscMcsMgrFrf5EpGEpEpdType_Type()
)
mscMcsMgrFrf5EpGEpEpdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdType.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdAccessRate_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpEpdAccessRate based on Unsigned32"""
    defaultValue = 1536000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscMcsMgrFrf5EpGEpEpdAccessRate_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpEpdAccessRate_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdAccessRate = _MscMcsMgrFrf5EpGEpEpdAccessRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 9),
    _MscMcsMgrFrf5EpGEpEpdAccessRate_Type()
)
mscMcsMgrFrf5EpGEpEpdAccessRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdAccessRate.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdExcessBurstSize_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpEpdExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscMcsMgrFrf5EpGEpEpdExcessBurstSize_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpEpdExcessBurstSize_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdExcessBurstSize = _MscMcsMgrFrf5EpGEpEpdExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 10, 1, 10),
    _MscMcsMgrFrf5EpGEpEpdExcessBurstSize_Type()
)
mscMcsMgrFrf5EpGEpEpdExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdExcessBurstSize.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdCidDataTable_Object = MibTable
mscMcsMgrFrf5EpGEpEpdCidDataTable = _MscMcsMgrFrf5EpGEpEpdCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 11)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdCidDataTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpEpdCidDataEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpEpdCidDataEntry = _MscMcsMgrFrf5EpGEpEpdCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 11, 1)
)
mscMcsMgrFrf5EpGEpEpdCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpEpdIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdCidDataEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpEpdCustomerIdentifier_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpEpdCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscMcsMgrFrf5EpGEpEpdCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpEpdCustomerIdentifier_Object = MibTableColumn
mscMcsMgrFrf5EpGEpEpdCustomerIdentifier = _MscMcsMgrFrf5EpGEpEpdCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 3, 11, 1, 1),
    _MscMcsMgrFrf5EpGEpEpdCustomerIdentifier_Type()
)
mscMcsMgrFrf5EpGEpEpdCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpEpdCustomerIdentifier.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpDlci_ObjectIdentity = ObjectIdentity
mscMcsMgrFrf5EpGEpDlci = _MscMcsMgrFrf5EpGEpDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4)
)
_MscMcsMgrFrf5EpGEpDlciRowStatusTable_Object = MibTable
mscMcsMgrFrf5EpGEpDlciRowStatusTable = _MscMcsMgrFrf5EpGEpDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciRowStatusTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpDlciRowStatusEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpDlciRowStatusEntry = _MscMcsMgrFrf5EpGEpDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 1, 1)
)
mscMcsMgrFrf5EpGEpDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciRowStatusEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpDlciRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGEpDlciRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciRowStatus = _MscMcsMgrFrf5EpGEpDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 1, 1, 1),
    _MscMcsMgrFrf5EpGEpDlciRowStatus_Type()
)
mscMcsMgrFrf5EpGEpDlciRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpDlciComponentName_Type = DisplayString
_MscMcsMgrFrf5EpGEpDlciComponentName_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciComponentName = _MscMcsMgrFrf5EpGEpDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 1, 1, 2),
    _MscMcsMgrFrf5EpGEpDlciComponentName_Type()
)
mscMcsMgrFrf5EpGEpDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciComponentName.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpDlciStorageType_Type = StorageType
_MscMcsMgrFrf5EpGEpDlciStorageType_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciStorageType = _MscMcsMgrFrf5EpGEpDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 1, 1, 4),
    _MscMcsMgrFrf5EpGEpDlciStorageType_Type()
)
mscMcsMgrFrf5EpGEpDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciStorageType.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpDlciIndex_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
        ValueRangeConstraint(1022, 1022),
    )


_MscMcsMgrFrf5EpGEpDlciIndex_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpDlciIndex_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciIndex = _MscMcsMgrFrf5EpGEpDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 1, 1, 10),
    _MscMcsMgrFrf5EpGEpDlciIndex_Type()
)
mscMcsMgrFrf5EpGEpDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciIndex.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpDlciOperTable_Object = MibTable
mscMcsMgrFrf5EpGEpDlciOperTable = _MscMcsMgrFrf5EpGEpDlciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciOperTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpDlciOperEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpDlciOperEntry = _MscMcsMgrFrf5EpGEpDlciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 10, 1)
)
mscMcsMgrFrf5EpGEpDlciOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpDlciIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciOperEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpDlciABitStatusToIf_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpDlciABitStatusToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_MscMcsMgrFrf5EpGEpDlciABitStatusToIf_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpDlciABitStatusToIf_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciABitStatusToIf = _MscMcsMgrFrf5EpGEpDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 10, 1, 1),
    _MscMcsMgrFrf5EpGEpDlciABitStatusToIf_Type()
)
mscMcsMgrFrf5EpGEpDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciABitStatusToIf.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpDlciABitReasonToIf_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpDlciABitReasonToIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("notApplicable", 0),
          ("pvcDown", 6),
          ("remoteLinkDown", 5),
          ("remoteLmiError", 3),
          ("remoteUserSignaled", 1))
    )


_MscMcsMgrFrf5EpGEpDlciABitReasonToIf_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpDlciABitReasonToIf_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciABitReasonToIf = _MscMcsMgrFrf5EpGEpDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 10, 1, 2),
    _MscMcsMgrFrf5EpGEpDlciABitReasonToIf_Type()
)
mscMcsMgrFrf5EpGEpDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciABitReasonToIf.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpDlciABitStatusFromIf_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpDlciABitStatusFromIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_MscMcsMgrFrf5EpGEpDlciABitStatusFromIf_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpDlciABitStatusFromIf_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciABitStatusFromIf = _MscMcsMgrFrf5EpGEpDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 10, 1, 3),
    _MscMcsMgrFrf5EpGEpDlciABitStatusFromIf_Type()
)
mscMcsMgrFrf5EpGEpDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciABitStatusFromIf.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpDlciABitReasonFromIf_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpDlciABitReasonFromIf based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localLinkDown", 4),
          ("localLmiError", 2),
          ("missingFromLmiReport", 7),
          ("notApplicable", 0),
          ("remoteUserSignalled", 1))
    )


_MscMcsMgrFrf5EpGEpDlciABitReasonFromIf_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpDlciABitReasonFromIf_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciABitReasonFromIf = _MscMcsMgrFrf5EpGEpDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 10, 1, 4),
    _MscMcsMgrFrf5EpGEpDlciABitReasonFromIf_Type()
)
mscMcsMgrFrf5EpGEpDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciABitReasonFromIf.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpDlciAccessConnectionComponent_Type(AsciiString):
    """Custom type mscMcsMgrFrf5EpGEpDlciAccessConnectionComponent based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_MscMcsMgrFrf5EpGEpDlciAccessConnectionComponent_Type.__name__ = "AsciiString"
_MscMcsMgrFrf5EpGEpDlciAccessConnectionComponent_Object = MibTableColumn
mscMcsMgrFrf5EpGEpDlciAccessConnectionComponent = _MscMcsMgrFrf5EpGEpDlciAccessConnectionComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 4, 10, 1, 5),
    _MscMcsMgrFrf5EpGEpDlciAccessConnectionComponent_Type()
)
mscMcsMgrFrf5EpGEpDlciAccessConnectionComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpDlciAccessConnectionComponent.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmCon_ObjectIdentity = ObjectIdentity
mscMcsMgrFrf5EpGEpAtmCon = _MscMcsMgrFrf5EpGEpAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5)
)
_MscMcsMgrFrf5EpGEpAtmConRowStatusTable_Object = MibTable
mscMcsMgrFrf5EpGEpAtmConRowStatusTable = _MscMcsMgrFrf5EpGEpAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConRowStatusTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConRowStatusEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpAtmConRowStatusEntry = _MscMcsMgrFrf5EpGEpAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 1, 1)
)
mscMcsMgrFrf5EpGEpAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConRowStatusEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConRowStatus_Type = RowStatus
_MscMcsMgrFrf5EpGEpAtmConRowStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAtmConRowStatus = _MscMcsMgrFrf5EpGEpAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 1, 1, 1),
    _MscMcsMgrFrf5EpGEpAtmConRowStatus_Type()
)
mscMcsMgrFrf5EpGEpAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConRowStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConComponentName_Type = DisplayString
_MscMcsMgrFrf5EpGEpAtmConComponentName_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAtmConComponentName = _MscMcsMgrFrf5EpGEpAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 1, 1, 2),
    _MscMcsMgrFrf5EpGEpAtmConComponentName_Type()
)
mscMcsMgrFrf5EpGEpAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConComponentName.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConStorageType_Type = StorageType
_MscMcsMgrFrf5EpGEpAtmConStorageType_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAtmConStorageType = _MscMcsMgrFrf5EpGEpAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 1, 1, 4),
    _MscMcsMgrFrf5EpGEpAtmConStorageType_Type()
)
mscMcsMgrFrf5EpGEpAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConStorageType.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConIndex_Type = NonReplicated
_MscMcsMgrFrf5EpGEpAtmConIndex_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAtmConIndex = _MscMcsMgrFrf5EpGEpAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 1, 1, 10),
    _MscMcsMgrFrf5EpGEpAtmConIndex_Type()
)
mscMcsMgrFrf5EpGEpAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConIndex.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConOperTable_Object = MibTable
mscMcsMgrFrf5EpGEpAtmConOperTable = _MscMcsMgrFrf5EpGEpAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConOperTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConOperEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpAtmConOperEntry = _MscMcsMgrFrf5EpGEpAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 10, 1)
)
mscMcsMgrFrf5EpGEpAtmConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConOperEntry.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpAtmConNextHop_Type = RowPointer
_MscMcsMgrFrf5EpGEpAtmConNextHop_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAtmConNextHop = _MscMcsMgrFrf5EpGEpAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 5, 10, 1, 1),
    _MscMcsMgrFrf5EpGEpAtmConNextHop_Type()
)
mscMcsMgrFrf5EpGEpAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAtmConNextHop.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpStateTable_Object = MibTable
mscMcsMgrFrf5EpGEpStateTable = _MscMcsMgrFrf5EpGEpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpStateTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpStateEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpStateEntry = _MscMcsMgrFrf5EpGEpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1)
)
mscMcsMgrFrf5EpGEpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpStateEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpAdminState_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpAdminState based on Integer32"""
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


_MscMcsMgrFrf5EpGEpAdminState_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpAdminState_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAdminState = _MscMcsMgrFrf5EpGEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 1),
    _MscMcsMgrFrf5EpGEpAdminState_Type()
)
mscMcsMgrFrf5EpGEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAdminState.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpOperationalState_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpOperationalState based on Integer32"""
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


_MscMcsMgrFrf5EpGEpOperationalState_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpOperationalState_Object = MibTableColumn
mscMcsMgrFrf5EpGEpOperationalState = _MscMcsMgrFrf5EpGEpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 2),
    _MscMcsMgrFrf5EpGEpOperationalState_Type()
)
mscMcsMgrFrf5EpGEpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpOperationalState.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpUsageState_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpUsageState based on Integer32"""
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


_MscMcsMgrFrf5EpGEpUsageState_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpUsageState_Object = MibTableColumn
mscMcsMgrFrf5EpGEpUsageState = _MscMcsMgrFrf5EpGEpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 3),
    _MscMcsMgrFrf5EpGEpUsageState_Type()
)
mscMcsMgrFrf5EpGEpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpUsageState.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpAvailabilityStatus_Type(OctetString):
    """Custom type mscMcsMgrFrf5EpGEpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMcsMgrFrf5EpGEpAvailabilityStatus_Type.__name__ = "OctetString"
_MscMcsMgrFrf5EpGEpAvailabilityStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAvailabilityStatus = _MscMcsMgrFrf5EpGEpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 4),
    _MscMcsMgrFrf5EpGEpAvailabilityStatus_Type()
)
mscMcsMgrFrf5EpGEpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAvailabilityStatus.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpProceduralStatus_Type(OctetString):
    """Custom type mscMcsMgrFrf5EpGEpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrFrf5EpGEpProceduralStatus_Type.__name__ = "OctetString"
_MscMcsMgrFrf5EpGEpProceduralStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpProceduralStatus = _MscMcsMgrFrf5EpGEpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 5),
    _MscMcsMgrFrf5EpGEpProceduralStatus_Type()
)
mscMcsMgrFrf5EpGEpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpProceduralStatus.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpControlStatus_Type(OctetString):
    """Custom type mscMcsMgrFrf5EpGEpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrFrf5EpGEpControlStatus_Type.__name__ = "OctetString"
_MscMcsMgrFrf5EpGEpControlStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpControlStatus = _MscMcsMgrFrf5EpGEpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 6),
    _MscMcsMgrFrf5EpGEpControlStatus_Type()
)
mscMcsMgrFrf5EpGEpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpControlStatus.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpAlarmStatus_Type(OctetString):
    """Custom type mscMcsMgrFrf5EpGEpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrFrf5EpGEpAlarmStatus_Type.__name__ = "OctetString"
_MscMcsMgrFrf5EpGEpAlarmStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAlarmStatus = _MscMcsMgrFrf5EpGEpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 7),
    _MscMcsMgrFrf5EpGEpAlarmStatus_Type()
)
mscMcsMgrFrf5EpGEpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAlarmStatus.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpStandbyStatus_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_MscMcsMgrFrf5EpGEpStandbyStatus_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpStandbyStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpStandbyStatus = _MscMcsMgrFrf5EpGEpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 8),
    _MscMcsMgrFrf5EpGEpStandbyStatus_Type()
)
mscMcsMgrFrf5EpGEpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpStandbyStatus.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpUnknownStatus_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MscMcsMgrFrf5EpGEpUnknownStatus_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpUnknownStatus_Object = MibTableColumn
mscMcsMgrFrf5EpGEpUnknownStatus = _MscMcsMgrFrf5EpGEpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 10, 1, 9),
    _MscMcsMgrFrf5EpGEpUnknownStatus_Type()
)
mscMcsMgrFrf5EpGEpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpUnknownStatus.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpOperTable_Object = MibTable
mscMcsMgrFrf5EpGEpOperTable = _MscMcsMgrFrf5EpGEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11)
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpOperTable.setStatus("mandatory")
_MscMcsMgrFrf5EpGEpOperEntry_Object = MibTableRow
mscMcsMgrFrf5EpGEpOperEntry = _MscMcsMgrFrf5EpGEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1)
)
mscMcsMgrFrf5EpGEpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-Frf5EpMIB", "mscMcsMgrFrf5EpGEpIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpOperEntry.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLastVccClearCause_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpLastVccClearCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMcsMgrFrf5EpGEpLastVccClearCause_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpLastVccClearCause_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLastVccClearCause = _MscMcsMgrFrf5EpGEpLastVccClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 4),
    _MscMcsMgrFrf5EpGEpLastVccClearCause_Type()
)
mscMcsMgrFrf5EpGEpLastVccClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLastVccClearCause.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpConnectionTransferPriority_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscMcsMgrFrf5EpGEpConnectionTransferPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpConnectionTransferPriority_Object = MibTableColumn
mscMcsMgrFrf5EpGEpConnectionTransferPriority = _MscMcsMgrFrf5EpGEpConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 5),
    _MscMcsMgrFrf5EpGEpConnectionTransferPriority_Type()
)
mscMcsMgrFrf5EpGEpConnectionTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpConnectionTransferPriority.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpServiceCategory_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpServiceCategory based on Integer32"""
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
        *(("cbr", 1),
          ("nrtVbr", 3),
          ("rtVbr", 2),
          ("ubr", 0))
    )


_MscMcsMgrFrf5EpGEpServiceCategory_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpServiceCategory_Object = MibTableColumn
mscMcsMgrFrf5EpGEpServiceCategory = _MscMcsMgrFrf5EpGEpServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 6),
    _MscMcsMgrFrf5EpGEpServiceCategory_Type()
)
mscMcsMgrFrf5EpGEpServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpServiceCategory.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpPeakCellRate01_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpPeakCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMcsMgrFrf5EpGEpPeakCellRate01_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpPeakCellRate01_Object = MibTableColumn
mscMcsMgrFrf5EpGEpPeakCellRate01 = _MscMcsMgrFrf5EpGEpPeakCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 8),
    _MscMcsMgrFrf5EpGEpPeakCellRate01_Type()
)
mscMcsMgrFrf5EpGEpPeakCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpPeakCellRate01.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpSustainedCellRate0_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpSustainedCellRate0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMcsMgrFrf5EpGEpSustainedCellRate0_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpSustainedCellRate0_Object = MibTableColumn
mscMcsMgrFrf5EpGEpSustainedCellRate0 = _MscMcsMgrFrf5EpGEpSustainedCellRate0_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 9),
    _MscMcsMgrFrf5EpGEpSustainedCellRate0_Type()
)
mscMcsMgrFrf5EpGEpSustainedCellRate0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpSustainedCellRate0.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpSustainedCellRate01_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpSustainedCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMcsMgrFrf5EpGEpSustainedCellRate01_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpSustainedCellRate01_Object = MibTableColumn
mscMcsMgrFrf5EpGEpSustainedCellRate01 = _MscMcsMgrFrf5EpGEpSustainedCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 10),
    _MscMcsMgrFrf5EpGEpSustainedCellRate01_Type()
)
mscMcsMgrFrf5EpGEpSustainedCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpSustainedCellRate01.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpMaximumBurstSize0_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpMaximumBurstSize0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMcsMgrFrf5EpGEpMaximumBurstSize0_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpMaximumBurstSize0_Object = MibTableColumn
mscMcsMgrFrf5EpGEpMaximumBurstSize0 = _MscMcsMgrFrf5EpGEpMaximumBurstSize0_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 11),
    _MscMcsMgrFrf5EpGEpMaximumBurstSize0_Type()
)
mscMcsMgrFrf5EpGEpMaximumBurstSize0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpMaximumBurstSize0.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpMaximumBurstSize01_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpMaximumBurstSize01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMcsMgrFrf5EpGEpMaximumBurstSize01_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpMaximumBurstSize01_Object = MibTableColumn
mscMcsMgrFrf5EpGEpMaximumBurstSize01 = _MscMcsMgrFrf5EpGEpMaximumBurstSize01_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 12),
    _MscMcsMgrFrf5EpGEpMaximumBurstSize01_Type()
)
mscMcsMgrFrf5EpGEpMaximumBurstSize01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpMaximumBurstSize01.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpAvgFrameSize_Type(Unsigned32):
    """Custom type mscMcsMgrFrf5EpGEpAvgFrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscMcsMgrFrf5EpGEpAvgFrameSize_Type.__name__ = "Unsigned32"
_MscMcsMgrFrf5EpGEpAvgFrameSize_Object = MibTableColumn
mscMcsMgrFrf5EpGEpAvgFrameSize = _MscMcsMgrFrf5EpGEpAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 13),
    _MscMcsMgrFrf5EpGEpAvgFrameSize_Type()
)
mscMcsMgrFrf5EpGEpAvgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpAvgFrameSize.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpTrafficParmConversionPolicy_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpTrafficParmConversionPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6))
    )


_MscMcsMgrFrf5EpGEpTrafficParmConversionPolicy_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpTrafficParmConversionPolicy_Object = MibTableColumn
mscMcsMgrFrf5EpGEpTrafficParmConversionPolicy = _MscMcsMgrFrf5EpGEpTrafficParmConversionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 14),
    _MscMcsMgrFrf5EpGEpTrafficParmConversionPolicy_Type()
)
mscMcsMgrFrf5EpGEpTrafficParmConversionPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpTrafficParmConversionPolicy.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpType_Type(Integer32):
    """Custom type mscMcsMgrFrf5EpGEpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("slave", 1))
    )


_MscMcsMgrFrf5EpGEpType_Type.__name__ = "Integer32"
_MscMcsMgrFrf5EpGEpType_Object = MibTableColumn
mscMcsMgrFrf5EpGEpType = _MscMcsMgrFrf5EpGEpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 15),
    _MscMcsMgrFrf5EpGEpType_Type()
)
mscMcsMgrFrf5EpGEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpType.setStatus("mandatory")


class _MscMcsMgrFrf5EpGEpLastVccCauseDiag_Type(HexString):
    """Custom type mscMcsMgrFrf5EpGEpLastVccCauseDiag based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MscMcsMgrFrf5EpGEpLastVccCauseDiag_Type.__name__ = "HexString"
_MscMcsMgrFrf5EpGEpLastVccCauseDiag_Object = MibTableColumn
mscMcsMgrFrf5EpGEpLastVccCauseDiag = _MscMcsMgrFrf5EpGEpLastVccCauseDiag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 14, 3, 11, 1, 20),
    _MscMcsMgrFrf5EpGEpLastVccCauseDiag_Type()
)
mscMcsMgrFrf5EpGEpLastVccCauseDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrFrf5EpGEpLastVccCauseDiag.setStatus("mandatory")
_Frf5EpMIB_ObjectIdentity = ObjectIdentity
frf5EpMIB = _Frf5EpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121)
)
_Frf5EpGroup_ObjectIdentity = ObjectIdentity
frf5EpGroup = _Frf5EpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 1)
)
_Frf5EpGroupCA_ObjectIdentity = ObjectIdentity
frf5EpGroupCA = _Frf5EpGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 1, 1)
)
_Frf5EpGroupCA02_ObjectIdentity = ObjectIdentity
frf5EpGroupCA02 = _Frf5EpGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 1, 1, 3)
)
_Frf5EpGroupCA02A_ObjectIdentity = ObjectIdentity
frf5EpGroupCA02A = _Frf5EpGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 1, 1, 3, 2)
)
_Frf5EpCapabilities_ObjectIdentity = ObjectIdentity
frf5EpCapabilities = _Frf5EpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 3)
)
_Frf5EpCapabilitiesCA_ObjectIdentity = ObjectIdentity
frf5EpCapabilitiesCA = _Frf5EpCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 3, 1)
)
_Frf5EpCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frf5EpCapabilitiesCA02 = _Frf5EpCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 3, 1, 3)
)
_Frf5EpCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frf5EpCapabilitiesCA02A = _Frf5EpCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 121, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-Frf5EpMIB",
    **{"mscMcsMgrFrf5EpG": mscMcsMgrFrf5EpG,
       "mscMcsMgrFrf5EpGRowStatusTable": mscMcsMgrFrf5EpGRowStatusTable,
       "mscMcsMgrFrf5EpGRowStatusEntry": mscMcsMgrFrf5EpGRowStatusEntry,
       "mscMcsMgrFrf5EpGRowStatus": mscMcsMgrFrf5EpGRowStatus,
       "mscMcsMgrFrf5EpGComponentName": mscMcsMgrFrf5EpGComponentName,
       "mscMcsMgrFrf5EpGStorageType": mscMcsMgrFrf5EpGStorageType,
       "mscMcsMgrFrf5EpGIndex": mscMcsMgrFrf5EpGIndex,
       "mscMcsMgrFrf5EpGAddr": mscMcsMgrFrf5EpGAddr,
       "mscMcsMgrFrf5EpGAddrRowStatusTable": mscMcsMgrFrf5EpGAddrRowStatusTable,
       "mscMcsMgrFrf5EpGAddrRowStatusEntry": mscMcsMgrFrf5EpGAddrRowStatusEntry,
       "mscMcsMgrFrf5EpGAddrRowStatus": mscMcsMgrFrf5EpGAddrRowStatus,
       "mscMcsMgrFrf5EpGAddrComponentName": mscMcsMgrFrf5EpGAddrComponentName,
       "mscMcsMgrFrf5EpGAddrStorageType": mscMcsMgrFrf5EpGAddrStorageType,
       "mscMcsMgrFrf5EpGAddrIndex": mscMcsMgrFrf5EpGAddrIndex,
       "mscMcsMgrFrf5EpGAddrProvTable": mscMcsMgrFrf5EpGAddrProvTable,
       "mscMcsMgrFrf5EpGAddrProvEntry": mscMcsMgrFrf5EpGAddrProvEntry,
       "mscMcsMgrFrf5EpGAddrRemoteAddress": mscMcsMgrFrf5EpGAddrRemoteAddress,
       "mscMcsMgrFrf5EpGAddrCommentText": mscMcsMgrFrf5EpGAddrCommentText,
       "mscMcsMgrFrf5EpGAddrAddrPreTable": mscMcsMgrFrf5EpGAddrAddrPreTable,
       "mscMcsMgrFrf5EpGAddrAddrPreEntry": mscMcsMgrFrf5EpGAddrAddrPreEntry,
       "mscMcsMgrFrf5EpGAddrAddrPreValue": mscMcsMgrFrf5EpGAddrAddrPreValue,
       "mscMcsMgrFrf5EpGAddrAddrPreRowStatus": mscMcsMgrFrf5EpGAddrAddrPreRowStatus,
       "mscMcsMgrFrf5EpGEp": mscMcsMgrFrf5EpGEp,
       "mscMcsMgrFrf5EpGEpRowStatusTable": mscMcsMgrFrf5EpGEpRowStatusTable,
       "mscMcsMgrFrf5EpGEpRowStatusEntry": mscMcsMgrFrf5EpGEpRowStatusEntry,
       "mscMcsMgrFrf5EpGEpRowStatus": mscMcsMgrFrf5EpGEpRowStatus,
       "mscMcsMgrFrf5EpGEpComponentName": mscMcsMgrFrf5EpGEpComponentName,
       "mscMcsMgrFrf5EpGEpStorageType": mscMcsMgrFrf5EpGEpStorageType,
       "mscMcsMgrFrf5EpGEpIndex": mscMcsMgrFrf5EpGEpIndex,
       "mscMcsMgrFrf5EpGEpLmi": mscMcsMgrFrf5EpGEpLmi,
       "mscMcsMgrFrf5EpGEpLmiRowStatusTable": mscMcsMgrFrf5EpGEpLmiRowStatusTable,
       "mscMcsMgrFrf5EpGEpLmiRowStatusEntry": mscMcsMgrFrf5EpGEpLmiRowStatusEntry,
       "mscMcsMgrFrf5EpGEpLmiRowStatus": mscMcsMgrFrf5EpGEpLmiRowStatus,
       "mscMcsMgrFrf5EpGEpLmiComponentName": mscMcsMgrFrf5EpGEpLmiComponentName,
       "mscMcsMgrFrf5EpGEpLmiStorageType": mscMcsMgrFrf5EpGEpLmiStorageType,
       "mscMcsMgrFrf5EpGEpLmiIndex": mscMcsMgrFrf5EpGEpLmiIndex,
       "mscMcsMgrFrf5EpGEpLmiParmsTable": mscMcsMgrFrf5EpGEpLmiParmsTable,
       "mscMcsMgrFrf5EpGEpLmiParmsEntry": mscMcsMgrFrf5EpGEpLmiParmsEntry,
       "mscMcsMgrFrf5EpGEpLmiProcedures": mscMcsMgrFrf5EpGEpLmiProcedures,
       "mscMcsMgrFrf5EpGEpLmiAsyncStatusReport": mscMcsMgrFrf5EpGEpLmiAsyncStatusReport,
       "mscMcsMgrFrf5EpGEpLmiErrorEventThreshold": mscMcsMgrFrf5EpGEpLmiErrorEventThreshold,
       "mscMcsMgrFrf5EpGEpLmiEventCount": mscMcsMgrFrf5EpGEpLmiEventCount,
       "mscMcsMgrFrf5EpGEpLmiCheckPointTimer": mscMcsMgrFrf5EpGEpLmiCheckPointTimer,
       "mscMcsMgrFrf5EpGEpLmiSide": mscMcsMgrFrf5EpGEpLmiSide,
       "mscMcsMgrFrf5EpGEpLmiNniParmsTable": mscMcsMgrFrf5EpGEpLmiNniParmsTable,
       "mscMcsMgrFrf5EpGEpLmiNniParmsEntry": mscMcsMgrFrf5EpGEpLmiNniParmsEntry,
       "mscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles": mscMcsMgrFrf5EpGEpLmiFullStatusPollingCycles,
       "mscMcsMgrFrf5EpGEpLmiLinkVerificationTimer": mscMcsMgrFrf5EpGEpLmiLinkVerificationTimer,
       "mscMcsMgrFrf5EpGEpLmiStateTable": mscMcsMgrFrf5EpGEpLmiStateTable,
       "mscMcsMgrFrf5EpGEpLmiStateEntry": mscMcsMgrFrf5EpGEpLmiStateEntry,
       "mscMcsMgrFrf5EpGEpLmiAdminState": mscMcsMgrFrf5EpGEpLmiAdminState,
       "mscMcsMgrFrf5EpGEpLmiOperationalState": mscMcsMgrFrf5EpGEpLmiOperationalState,
       "mscMcsMgrFrf5EpGEpLmiUsageState": mscMcsMgrFrf5EpGEpLmiUsageState,
       "mscMcsMgrFrf5EpGEpLmiPsiTable": mscMcsMgrFrf5EpGEpLmiPsiTable,
       "mscMcsMgrFrf5EpGEpLmiPsiEntry": mscMcsMgrFrf5EpGEpLmiPsiEntry,
       "mscMcsMgrFrf5EpGEpLmiProtocolStatus": mscMcsMgrFrf5EpGEpLmiProtocolStatus,
       "mscMcsMgrFrf5EpGEpLmiStatsTable": mscMcsMgrFrf5EpGEpLmiStatsTable,
       "mscMcsMgrFrf5EpGEpLmiStatsEntry": mscMcsMgrFrf5EpGEpLmiStatsEntry,
       "mscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface": mscMcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface,
       "mscMcsMgrFrf5EpGEpLmiFullStatusToInterface": mscMcsMgrFrf5EpGEpLmiFullStatusToInterface,
       "mscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface": mscMcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface,
       "mscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface": mscMcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface,
       "mscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory": mscMcsMgrFrf5EpGEpLmiNetworkSideEventHistory,
       "mscMcsMgrFrf5EpGEpLmiUserSideEventHistory": mscMcsMgrFrf5EpGEpLmiUserSideEventHistory,
       "mscMcsMgrFrf5EpGEpLmiProtocolErrors": mscMcsMgrFrf5EpGEpLmiProtocolErrors,
       "mscMcsMgrFrf5EpGEpLmiUnexpectedIes": mscMcsMgrFrf5EpGEpLmiUnexpectedIes,
       "mscMcsMgrFrf5EpGEpLmiSequenceErrors": mscMcsMgrFrf5EpGEpLmiSequenceErrors,
       "mscMcsMgrFrf5EpGEpLmiStatusSequenceErrors": mscMcsMgrFrf5EpGEpLmiStatusSequenceErrors,
       "mscMcsMgrFrf5EpGEpLmiUnexpectedReports": mscMcsMgrFrf5EpGEpLmiUnexpectedReports,
       "mscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts": mscMcsMgrFrf5EpGEpLmiPollingVerifTimeouts,
       "mscMcsMgrFrf5EpGEpLmiNoStatusReportCount": mscMcsMgrFrf5EpGEpLmiNoStatusReportCount,
       "mscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf": mscMcsMgrFrf5EpGEpLmiKeepAliveEnqToIf,
       "mscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf": mscMcsMgrFrf5EpGEpLmiFullStatusEnqToIf,
       "mscMcsMgrFrf5EpGEpEpd": mscMcsMgrFrf5EpGEpEpd,
       "mscMcsMgrFrf5EpGEpEpdRowStatusTable": mscMcsMgrFrf5EpGEpEpdRowStatusTable,
       "mscMcsMgrFrf5EpGEpEpdRowStatusEntry": mscMcsMgrFrf5EpGEpEpdRowStatusEntry,
       "mscMcsMgrFrf5EpGEpEpdRowStatus": mscMcsMgrFrf5EpGEpEpdRowStatus,
       "mscMcsMgrFrf5EpGEpEpdComponentName": mscMcsMgrFrf5EpGEpEpdComponentName,
       "mscMcsMgrFrf5EpGEpEpdStorageType": mscMcsMgrFrf5EpGEpEpdStorageType,
       "mscMcsMgrFrf5EpGEpEpdIndex": mscMcsMgrFrf5EpGEpEpdIndex,
       "mscMcsMgrFrf5EpGEpEpdProvTable": mscMcsMgrFrf5EpGEpEpdProvTable,
       "mscMcsMgrFrf5EpGEpEpdProvEntry": mscMcsMgrFrf5EpGEpEpdProvEntry,
       "mscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier": mscMcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier,
       "mscMcsMgrFrf5EpGEpEpdConnectionTransferPriority": mscMcsMgrFrf5EpGEpEpdConnectionTransferPriority,
       "mscMcsMgrFrf5EpGEpEpdCommittedInformationRate": mscMcsMgrFrf5EpGEpEpdCommittedInformationRate,
       "mscMcsMgrFrf5EpGEpEpdExcessInformationRate": mscMcsMgrFrf5EpGEpEpdExcessInformationRate,
       "mscMcsMgrFrf5EpGEpEpdCommittedBurstSize": mscMcsMgrFrf5EpGEpEpdCommittedBurstSize,
       "mscMcsMgrFrf5EpGEpEpdType": mscMcsMgrFrf5EpGEpEpdType,
       "mscMcsMgrFrf5EpGEpEpdAccessRate": mscMcsMgrFrf5EpGEpEpdAccessRate,
       "mscMcsMgrFrf5EpGEpEpdExcessBurstSize": mscMcsMgrFrf5EpGEpEpdExcessBurstSize,
       "mscMcsMgrFrf5EpGEpEpdCidDataTable": mscMcsMgrFrf5EpGEpEpdCidDataTable,
       "mscMcsMgrFrf5EpGEpEpdCidDataEntry": mscMcsMgrFrf5EpGEpEpdCidDataEntry,
       "mscMcsMgrFrf5EpGEpEpdCustomerIdentifier": mscMcsMgrFrf5EpGEpEpdCustomerIdentifier,
       "mscMcsMgrFrf5EpGEpDlci": mscMcsMgrFrf5EpGEpDlci,
       "mscMcsMgrFrf5EpGEpDlciRowStatusTable": mscMcsMgrFrf5EpGEpDlciRowStatusTable,
       "mscMcsMgrFrf5EpGEpDlciRowStatusEntry": mscMcsMgrFrf5EpGEpDlciRowStatusEntry,
       "mscMcsMgrFrf5EpGEpDlciRowStatus": mscMcsMgrFrf5EpGEpDlciRowStatus,
       "mscMcsMgrFrf5EpGEpDlciComponentName": mscMcsMgrFrf5EpGEpDlciComponentName,
       "mscMcsMgrFrf5EpGEpDlciStorageType": mscMcsMgrFrf5EpGEpDlciStorageType,
       "mscMcsMgrFrf5EpGEpDlciIndex": mscMcsMgrFrf5EpGEpDlciIndex,
       "mscMcsMgrFrf5EpGEpDlciOperTable": mscMcsMgrFrf5EpGEpDlciOperTable,
       "mscMcsMgrFrf5EpGEpDlciOperEntry": mscMcsMgrFrf5EpGEpDlciOperEntry,
       "mscMcsMgrFrf5EpGEpDlciABitStatusToIf": mscMcsMgrFrf5EpGEpDlciABitStatusToIf,
       "mscMcsMgrFrf5EpGEpDlciABitReasonToIf": mscMcsMgrFrf5EpGEpDlciABitReasonToIf,
       "mscMcsMgrFrf5EpGEpDlciABitStatusFromIf": mscMcsMgrFrf5EpGEpDlciABitStatusFromIf,
       "mscMcsMgrFrf5EpGEpDlciABitReasonFromIf": mscMcsMgrFrf5EpGEpDlciABitReasonFromIf,
       "mscMcsMgrFrf5EpGEpDlciAccessConnectionComponent": mscMcsMgrFrf5EpGEpDlciAccessConnectionComponent,
       "mscMcsMgrFrf5EpGEpAtmCon": mscMcsMgrFrf5EpGEpAtmCon,
       "mscMcsMgrFrf5EpGEpAtmConRowStatusTable": mscMcsMgrFrf5EpGEpAtmConRowStatusTable,
       "mscMcsMgrFrf5EpGEpAtmConRowStatusEntry": mscMcsMgrFrf5EpGEpAtmConRowStatusEntry,
       "mscMcsMgrFrf5EpGEpAtmConRowStatus": mscMcsMgrFrf5EpGEpAtmConRowStatus,
       "mscMcsMgrFrf5EpGEpAtmConComponentName": mscMcsMgrFrf5EpGEpAtmConComponentName,
       "mscMcsMgrFrf5EpGEpAtmConStorageType": mscMcsMgrFrf5EpGEpAtmConStorageType,
       "mscMcsMgrFrf5EpGEpAtmConIndex": mscMcsMgrFrf5EpGEpAtmConIndex,
       "mscMcsMgrFrf5EpGEpAtmConOperTable": mscMcsMgrFrf5EpGEpAtmConOperTable,
       "mscMcsMgrFrf5EpGEpAtmConOperEntry": mscMcsMgrFrf5EpGEpAtmConOperEntry,
       "mscMcsMgrFrf5EpGEpAtmConNextHop": mscMcsMgrFrf5EpGEpAtmConNextHop,
       "mscMcsMgrFrf5EpGEpStateTable": mscMcsMgrFrf5EpGEpStateTable,
       "mscMcsMgrFrf5EpGEpStateEntry": mscMcsMgrFrf5EpGEpStateEntry,
       "mscMcsMgrFrf5EpGEpAdminState": mscMcsMgrFrf5EpGEpAdminState,
       "mscMcsMgrFrf5EpGEpOperationalState": mscMcsMgrFrf5EpGEpOperationalState,
       "mscMcsMgrFrf5EpGEpUsageState": mscMcsMgrFrf5EpGEpUsageState,
       "mscMcsMgrFrf5EpGEpAvailabilityStatus": mscMcsMgrFrf5EpGEpAvailabilityStatus,
       "mscMcsMgrFrf5EpGEpProceduralStatus": mscMcsMgrFrf5EpGEpProceduralStatus,
       "mscMcsMgrFrf5EpGEpControlStatus": mscMcsMgrFrf5EpGEpControlStatus,
       "mscMcsMgrFrf5EpGEpAlarmStatus": mscMcsMgrFrf5EpGEpAlarmStatus,
       "mscMcsMgrFrf5EpGEpStandbyStatus": mscMcsMgrFrf5EpGEpStandbyStatus,
       "mscMcsMgrFrf5EpGEpUnknownStatus": mscMcsMgrFrf5EpGEpUnknownStatus,
       "mscMcsMgrFrf5EpGEpOperTable": mscMcsMgrFrf5EpGEpOperTable,
       "mscMcsMgrFrf5EpGEpOperEntry": mscMcsMgrFrf5EpGEpOperEntry,
       "mscMcsMgrFrf5EpGEpLastVccClearCause": mscMcsMgrFrf5EpGEpLastVccClearCause,
       "mscMcsMgrFrf5EpGEpConnectionTransferPriority": mscMcsMgrFrf5EpGEpConnectionTransferPriority,
       "mscMcsMgrFrf5EpGEpServiceCategory": mscMcsMgrFrf5EpGEpServiceCategory,
       "mscMcsMgrFrf5EpGEpPeakCellRate01": mscMcsMgrFrf5EpGEpPeakCellRate01,
       "mscMcsMgrFrf5EpGEpSustainedCellRate0": mscMcsMgrFrf5EpGEpSustainedCellRate0,
       "mscMcsMgrFrf5EpGEpSustainedCellRate01": mscMcsMgrFrf5EpGEpSustainedCellRate01,
       "mscMcsMgrFrf5EpGEpMaximumBurstSize0": mscMcsMgrFrf5EpGEpMaximumBurstSize0,
       "mscMcsMgrFrf5EpGEpMaximumBurstSize01": mscMcsMgrFrf5EpGEpMaximumBurstSize01,
       "mscMcsMgrFrf5EpGEpAvgFrameSize": mscMcsMgrFrf5EpGEpAvgFrameSize,
       "mscMcsMgrFrf5EpGEpTrafficParmConversionPolicy": mscMcsMgrFrf5EpGEpTrafficParmConversionPolicy,
       "mscMcsMgrFrf5EpGEpType": mscMcsMgrFrf5EpGEpType,
       "mscMcsMgrFrf5EpGEpLastVccCauseDiag": mscMcsMgrFrf5EpGEpLastVccCauseDiag,
       "frf5EpMIB": frf5EpMIB,
       "frf5EpGroup": frf5EpGroup,
       "frf5EpGroupCA": frf5EpGroupCA,
       "frf5EpGroupCA02": frf5EpGroupCA02,
       "frf5EpGroupCA02A": frf5EpGroupCA02A,
       "frf5EpCapabilities": frf5EpCapabilities,
       "frf5EpCapabilitiesCA": frf5EpCapabilitiesCA,
       "frf5EpCapabilitiesCA02": frf5EpCapabilitiesCA02,
       "frf5EpCapabilitiesCA02A": frf5EpCapabilitiesCA02A}
)
