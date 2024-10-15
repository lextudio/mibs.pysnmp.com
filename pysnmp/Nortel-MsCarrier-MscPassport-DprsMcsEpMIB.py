# SNMP MIB module (Nortel-MsCarrier-MscPassport-DprsMcsEpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-DprsMcsEpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:16 2024
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
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 FixedPoint2,
 HexString,
 Link,
 NonReplicated,
 PassportCounter64,
 Unsigned64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "FixedPoint2",
    "HexString",
    "Link",
    "NonReplicated",
    "PassportCounter64",
    "Unsigned64")

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

_MscMcsMgrDprsMcsEpG_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpG = _MscMcsMgrDprsMcsEpG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2)
)
_MscMcsMgrDprsMcsEpGRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGRowStatusTable = _MscMcsMgrDprsMcsEpGRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGRowStatusEntry = _MscMcsMgrDprsMcsEpGRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 1, 1)
)
mscMcsMgrDprsMcsEpGRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGRowStatus = _MscMcsMgrDprsMcsEpGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGRowStatus_Type()
)
mscMcsMgrDprsMcsEpGRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGComponentName = _MscMcsMgrDprsMcsEpGComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGComponentName_Type()
)
mscMcsMgrDprsMcsEpGComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGStorageType = _MscMcsMgrDprsMcsEpGStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGStorageType_Type()
)
mscMcsMgrDprsMcsEpGStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGStorageType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MscMcsMgrDprsMcsEpGIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGIndex = _MscMcsMgrDprsMcsEpGIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGIndex_Type()
)
mscMcsMgrDprsMcsEpGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddr_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGAddr = _MscMcsMgrDprsMcsEpGAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2)
)
_MscMcsMgrDprsMcsEpGAddrRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGAddrRowStatusTable = _MscMcsMgrDprsMcsEpGAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddrRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGAddrRowStatusEntry = _MscMcsMgrDprsMcsEpGAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 1, 1)
)
mscMcsMgrDprsMcsEpGAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddrRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGAddrRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGAddrRowStatus = _MscMcsMgrDprsMcsEpGAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGAddrRowStatus_Type()
)
mscMcsMgrDprsMcsEpGAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddrComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGAddrComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGAddrComponentName = _MscMcsMgrDprsMcsEpGAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGAddrComponentName_Type()
)
mscMcsMgrDprsMcsEpGAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddrStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGAddrStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGAddrStorageType = _MscMcsMgrDprsMcsEpGAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGAddrStorageType_Type()
)
mscMcsMgrDprsMcsEpGAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrStorageType.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddrIndex_Type = NonReplicated
_MscMcsMgrDprsMcsEpGAddrIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGAddrIndex = _MscMcsMgrDprsMcsEpGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGAddrIndex_Type()
)
mscMcsMgrDprsMcsEpGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddrProvTable_Object = MibTable
mscMcsMgrDprsMcsEpGAddrProvTable = _MscMcsMgrDprsMcsEpGAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrProvTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAddrProvEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGAddrProvEntry = _MscMcsMgrDprsMcsEpGAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 10, 1)
)
mscMcsMgrDprsMcsEpGAddrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrProvEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGAddrRemoteAddress_Type(AsciiString):
    """Custom type mscMcsMgrDprsMcsEpGAddrRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_MscMcsMgrDprsMcsEpGAddrRemoteAddress_Type.__name__ = "AsciiString"
_MscMcsMgrDprsMcsEpGAddrRemoteAddress_Object = MibTableColumn
mscMcsMgrDprsMcsEpGAddrRemoteAddress = _MscMcsMgrDprsMcsEpGAddrRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGAddrRemoteAddress_Type()
)
mscMcsMgrDprsMcsEpGAddrRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrRemoteAddress.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGAddrCommentText_Type(AsciiString):
    """Custom type mscMcsMgrDprsMcsEpGAddrCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_MscMcsMgrDprsMcsEpGAddrCommentText_Type.__name__ = "AsciiString"
_MscMcsMgrDprsMcsEpGAddrCommentText_Object = MibTableColumn
mscMcsMgrDprsMcsEpGAddrCommentText = _MscMcsMgrDprsMcsEpGAddrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 2, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGAddrCommentText_Type()
)
mscMcsMgrDprsMcsEpGAddrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAddrCommentText.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEp_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGEp = _MscMcsMgrDprsMcsEpGEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3)
)
_MscMcsMgrDprsMcsEpGEpRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpRowStatusTable = _MscMcsMgrDprsMcsEpGEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpRowStatusEntry = _MscMcsMgrDprsMcsEpGEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 1, 1)
)
mscMcsMgrDprsMcsEpGEpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGEpRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpRowStatus = _MscMcsMgrDprsMcsEpGEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGEpRowStatus_Type()
)
mscMcsMgrDprsMcsEpGEpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGEpComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpComponentName = _MscMcsMgrDprsMcsEpGEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGEpComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGEpStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpStorageType = _MscMcsMgrDprsMcsEpGEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGEpStorageType_Type()
)
mscMcsMgrDprsMcsEpGEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpStorageType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MscMcsMgrDprsMcsEpGEpIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpIndex = _MscMcsMgrDprsMcsEpGEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGEpIndex_Type()
)
mscMcsMgrDprsMcsEpGEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpD_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGEpEpD = _MscMcsMgrDprsMcsEpGEpEpD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2)
)
_MscMcsMgrDprsMcsEpGEpEpDRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpEpDRowStatusTable = _MscMcsMgrDprsMcsEpGEpEpDRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpEpDRowStatusEntry = _MscMcsMgrDprsMcsEpGEpEpDRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 1, 1)
)
mscMcsMgrDprsMcsEpGEpEpDRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpEpDIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGEpEpDRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDRowStatus = _MscMcsMgrDprsMcsEpGEpEpDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGEpEpDRowStatus_Type()
)
mscMcsMgrDprsMcsEpGEpEpDRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGEpEpDComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDComponentName = _MscMcsMgrDprsMcsEpGEpEpDComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGEpEpDComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpEpDComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGEpEpDStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDStorageType = _MscMcsMgrDprsMcsEpGEpEpDStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGEpEpDStorageType_Type()
)
mscMcsMgrDprsMcsEpGEpEpDStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDStorageType.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDIndex_Type = NonReplicated
_MscMcsMgrDprsMcsEpGEpEpDIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDIndex = _MscMcsMgrDprsMcsEpGEpEpDIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGEpEpDIndex_Type()
)
mscMcsMgrDprsMcsEpGEpEpDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDProvTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpEpDProvTable = _MscMcsMgrDprsMcsEpGEpEpDProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDProvTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDProvEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpEpDProvEntry = _MscMcsMgrDprsMcsEpGEpEpDProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1)
)
mscMcsMgrDprsMcsEpGEpEpDProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpEpDIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDProvEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpEpDBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpEpDBandwidth based on Unsigned32"""
    defaultValue = 512000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56000, 155000000),
    )


_MscMcsMgrDprsMcsEpGEpEpDBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpEpDBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDBandwidth = _MscMcsMgrDprsMcsEpGEpEpDBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGEpEpDBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpEpDBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDBandwidth.setStatus("obsolete")


class _MscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority = _MscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Type()
)
mscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmOnly", 1),
          ("porsOnly", 3))
    )


_MscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference = _MscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 3),
    _MscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Type()
)
mscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDProfile_Type = Link
_MscMcsMgrDprsMcsEpGEpEpDProfile_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDProfile = _MscMcsMgrDprsMcsEpGEpEpDProfile_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 4),
    _MscMcsMgrDprsMcsEpGEpEpDProfile_Type()
)
mscMcsMgrDprsMcsEpGEpEpDProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDProfile.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpEpDPorsManualPath_Type = Link
_MscMcsMgrDprsMcsEpGEpEpDPorsManualPath_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDPorsManualPath = _MscMcsMgrDprsMcsEpGEpEpDPorsManualPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 5),
    _MscMcsMgrDprsMcsEpGEpEpDPorsManualPath_Type()
)
mscMcsMgrDprsMcsEpGEpEpDPorsManualPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDPorsManualPath.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Type(OctetString):
    """Custom type mscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities based on OctetString"""
    defaultHexValue = "8000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Type.__name__ = "OctetString"
_MscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities = _MscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 6),
    _MscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Type()
)
mscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpEpDForwardBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpEpDForwardBandwidth based on Unsigned32"""
    defaultValue = 512000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56000, 155000000),
    )


_MscMcsMgrDprsMcsEpGEpEpDForwardBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpEpDForwardBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDForwardBandwidth = _MscMcsMgrDprsMcsEpGEpEpDForwardBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 7),
    _MscMcsMgrDprsMcsEpGEpEpDForwardBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpEpDForwardBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDForwardBandwidth.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpEpDReverseBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpEpDReverseBandwidth based on Unsigned32"""
    defaultValue = 155000002

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56000, 155000000),
        ValueRangeConstraint(155000002, 155000002),
    )


_MscMcsMgrDprsMcsEpGEpEpDReverseBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpEpDReverseBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpEpDReverseBandwidth = _MscMcsMgrDprsMcsEpGEpEpDReverseBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 2, 10, 1, 8),
    _MscMcsMgrDprsMcsEpGEpEpDReverseBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpEpDReverseBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpEpDReverseBandwidth.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmCon_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGEpAtmCon = _MscMcsMgrDprsMcsEpGEpAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3)
)
_MscMcsMgrDprsMcsEpGEpAtmConRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpAtmConRowStatusTable = _MscMcsMgrDprsMcsEpGEpAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpAtmConRowStatusEntry = _MscMcsMgrDprsMcsEpGEpAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 1, 1)
)
mscMcsMgrDprsMcsEpGEpAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGEpAtmConRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAtmConRowStatus = _MscMcsMgrDprsMcsEpGEpAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGEpAtmConRowStatus_Type()
)
mscMcsMgrDprsMcsEpGEpAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGEpAtmConComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAtmConComponentName = _MscMcsMgrDprsMcsEpGEpAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGEpAtmConComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGEpAtmConStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAtmConStorageType = _MscMcsMgrDprsMcsEpGEpAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGEpAtmConStorageType_Type()
)
mscMcsMgrDprsMcsEpGEpAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConStorageType.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConIndex_Type = NonReplicated
_MscMcsMgrDprsMcsEpGEpAtmConIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAtmConIndex = _MscMcsMgrDprsMcsEpGEpAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGEpAtmConIndex_Type()
)
mscMcsMgrDprsMcsEpGEpAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConOperTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpAtmConOperTable = _MscMcsMgrDprsMcsEpGEpAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConOperTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConOperEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpAtmConOperEntry = _MscMcsMgrDprsMcsEpGEpAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 10, 1)
)
mscMcsMgrDprsMcsEpGEpAtmConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConOperEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpAtmConNextHop_Type = RowPointer
_MscMcsMgrDprsMcsEpGEpAtmConNextHop_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAtmConNextHop = _MscMcsMgrDprsMcsEpGEpAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 3, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGEpAtmConNextHop_Type()
)
mscMcsMgrDprsMcsEpGEpAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAtmConNextHop.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCo_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGEpLCo = _MscMcsMgrDprsMcsEpGEpLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4)
)
_MscMcsMgrDprsMcsEpGEpLCoRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpLCoRowStatusTable = _MscMcsMgrDprsMcsEpGEpLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpLCoRowStatusEntry = _MscMcsMgrDprsMcsEpGEpLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 1, 1)
)
mscMcsMgrDprsMcsEpGEpLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpLCoIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGEpLCoRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRowStatus = _MscMcsMgrDprsMcsEpGEpLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGEpLCoRowStatus_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGEpLCoComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoComponentName = _MscMcsMgrDprsMcsEpGEpLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGEpLCoComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGEpLCoStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoStorageType = _MscMcsMgrDprsMcsEpGEpLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGEpLCoStorageType_Type()
)
mscMcsMgrDprsMcsEpGEpLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoStorageType.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoIndex_Type = NonReplicated
_MscMcsMgrDprsMcsEpGEpLCoIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoIndex = _MscMcsMgrDprsMcsEpGEpLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGEpLCoIndex_Type()
)
mscMcsMgrDprsMcsEpGEpLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoPathDataTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpLCoPathDataTable = _MscMcsMgrDprsMcsEpGEpLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathDataTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoPathDataEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpLCoPathDataEntry = _MscMcsMgrDprsMcsEpGEpLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1)
)
mscMcsMgrDprsMcsEpGEpLCoPathDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpLCoIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathDataEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoState_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoState based on Integer32"""
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
        *(("connecting", 2),
          ("pathDown", 0),
          ("pathDownRetrying", 4),
          ("pathUp", 3),
          ("selectingRoute", 1))
    )


_MscMcsMgrDprsMcsEpGEpLCoState_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoState_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoState = _MscMcsMgrDprsMcsEpGEpLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGEpLCoState_Type()
)
mscMcsMgrDprsMcsEpGEpLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoState.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_MscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName = _MscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName_Type()
)
mscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoEnd_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 0))
    )


_MscMcsMgrDprsMcsEpGEpLCoEnd_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoEnd_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoEnd = _MscMcsMgrDprsMcsEpGEpLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 3),
    _MscMcsMgrDprsMcsEpGEpLCoEnd_Type()
)
mscMcsMgrDprsMcsEpGEpLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoEnd.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoCostMetric_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscMcsMgrDprsMcsEpGEpLCoCostMetric_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoCostMetric_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoCostMetric = _MscMcsMgrDprsMcsEpGEpLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 4),
    _MscMcsMgrDprsMcsEpGEpLCoCostMetric_Type()
)
mscMcsMgrDprsMcsEpGEpLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoCostMetric.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoDelayMetric_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscMcsMgrDprsMcsEpGEpLCoDelayMetric_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoDelayMetric_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoDelayMetric = _MscMcsMgrDprsMcsEpGEpLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 5),
    _MscMcsMgrDprsMcsEpGEpLCoDelayMetric_Type()
)
mscMcsMgrDprsMcsEpGEpLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoDelayMetric.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_MscMcsMgrDprsMcsEpGEpLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoRoundTripDelay_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRoundTripDelay = _MscMcsMgrDprsMcsEpGEpLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 6),
    _MscMcsMgrDprsMcsEpGEpLCoRoundTripDelay_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRoundTripDelay.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoSetupPriority_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscMcsMgrDprsMcsEpGEpLCoSetupPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoSetupPriority_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoSetupPriority = _MscMcsMgrDprsMcsEpGEpLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 7),
    _MscMcsMgrDprsMcsEpGEpLCoSetupPriority_Type()
)
mscMcsMgrDprsMcsEpGEpLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoSetupPriority.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoHoldingPriority_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscMcsMgrDprsMcsEpGEpLCoHoldingPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoHoldingPriority_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoHoldingPriority = _MscMcsMgrDprsMcsEpGEpLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 8),
    _MscMcsMgrDprsMcsEpGEpLCoHoldingPriority_Type()
)
mscMcsMgrDprsMcsEpGEpLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoHoldingPriority.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_MscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth = _MscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 9),
    _MscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_MscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth = _MscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 10),
    _MscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType based on Integer32"""
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
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_MscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType = _MscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 11),
    _MscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes = _MscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 12),
    _MscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscMcsMgrDprsMcsEpGEpLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoRequiredSecurity_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRequiredSecurity = _MscMcsMgrDprsMcsEpGEpLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 13),
    _MscMcsMgrDprsMcsEpGEpLCoRequiredSecurity_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRequiredSecurity.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter = _MscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 14),
    _MscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoEmissionPriority_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscMcsMgrDprsMcsEpGEpLCoEmissionPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoEmissionPriority_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoEmissionPriority = _MscMcsMgrDprsMcsEpGEpLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 15),
    _MscMcsMgrDprsMcsEpGEpLCoEmissionPriority_Type()
)
mscMcsMgrDprsMcsEpGEpLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoEmissionPriority.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoDiscardPriority_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscMcsMgrDprsMcsEpGEpLCoDiscardPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoDiscardPriority_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoDiscardPriority = _MscMcsMgrDprsMcsEpGEpLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 16),
    _MscMcsMgrDprsMcsEpGEpLCoDiscardPriority_Type()
)
mscMcsMgrDprsMcsEpGEpLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoDiscardPriority.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoPathType_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("manual", 1),
          ("normal", 0))
    )


_MscMcsMgrDprsMcsEpGEpLCoPathType_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoPathType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPathType = _MscMcsMgrDprsMcsEpGEpLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 17),
    _MscMcsMgrDprsMcsEpGEpLCoPathType_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoRetryCount_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscMcsMgrDprsMcsEpGEpLCoRetryCount_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoRetryCount_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoRetryCount = _MscMcsMgrDprsMcsEpGEpLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 18),
    _MscMcsMgrDprsMcsEpGEpLCoRetryCount_Type()
)
mscMcsMgrDprsMcsEpGEpLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoRetryCount.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoPathFailureCount_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscMcsMgrDprsMcsEpGEpLCoPathFailureCount_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLCoPathFailureCount_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPathFailureCount = _MscMcsMgrDprsMcsEpGEpLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 19),
    _MscMcsMgrDprsMcsEpGEpLCoPathFailureCount_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathFailureCount.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute based on Integer32"""
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
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("anError", 12),
          ("attributeProfileProblem", 13),
          ("attributesNotMet", 11),
          ("destinationNameTooLong", 1),
          ("destinationNotSpecified", 2),
          ("incorrectDestination", 4),
          ("incorrectDestinationEndPoint", 5),
          ("manualPathIndexProblem", 14),
          ("none", 0),
          ("routeCostTooMuch", 9),
          ("routesDelayTooLong", 10),
          ("sameNode", 8),
          ("unknownDestination", 7),
          ("unknownDestinationName", 3),
          ("unknownSource", 6))
    )


_MscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute = _MscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 20),
    _MscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute_Type()
)
mscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoLastTearDownReason_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoLastTearDownReason based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("accessCardFailure", 20),
          ("bumped", 19),
          ("callLoopedBack", 13),
          ("farEndBusy", 12),
          ("farEndNotFound", 10),
          ("farEndNotReady", 15),
          ("insufficientRxLcOrBandwidth", 3),
          ("insufficientTxLcOrBandwidth", 2),
          ("lostLcnClash", 7),
          ("networkCongestion", 8),
          ("none", 0),
          ("normalShutDown", 1),
          ("operatorForced", 6),
          ("optimized", 21),
          ("overrideRemoteName", 22),
          ("reconnectFromFarEnd", 18),
          ("remoteNameMismatch", 16),
          ("serviceTypeMismatch", 17),
          ("trunkCardFailure", 5),
          ("trunkFailure", 4),
          ("trunkNotFound", 9),
          ("trunkOrFarEndDidNotSupportMode", 23),
          ("unknownReason", 14),
          ("wrongModuleReached", 11))
    )


_MscMcsMgrDprsMcsEpGEpLCoLastTearDownReason_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoLastTearDownReason_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoLastTearDownReason = _MscMcsMgrDprsMcsEpGEpLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 21),
    _MscMcsMgrDprsMcsEpGEpLCoLastTearDownReason_Type()
)
mscMcsMgrDprsMcsEpGEpLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoLastTearDownReason.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoPathFailureAction_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoPathFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_MscMcsMgrDprsMcsEpGEpLCoPathFailureAction_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoPathFailureAction_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPathFailureAction = _MscMcsMgrDprsMcsEpGEpLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 22),
    _MscMcsMgrDprsMcsEpGEpLCoPathFailureAction_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathFailureAction.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoBumpPreference_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoBumpPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_MscMcsMgrDprsMcsEpGEpLCoBumpPreference_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoBumpPreference_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoBumpPreference = _MscMcsMgrDprsMcsEpGEpLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 23),
    _MscMcsMgrDprsMcsEpGEpLCoBumpPreference_Type()
)
mscMcsMgrDprsMcsEpGEpLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoBumpPreference.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoOptimization_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoOptimization based on Integer32"""
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


_MscMcsMgrDprsMcsEpGEpLCoOptimization_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpLCoOptimization_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoOptimization = _MscMcsMgrDprsMcsEpGEpLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 24),
    _MscMcsMgrDprsMcsEpGEpLCoOptimization_Type()
)
mscMcsMgrDprsMcsEpGEpLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoOptimization.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscMcsMgrDprsMcsEpGEpLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_MscMcsMgrDprsMcsEpGEpLCoPathUpDateTime_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPathUpDateTime = _MscMcsMgrDprsMcsEpGEpLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 10, 1, 25),
    _MscMcsMgrDprsMcsEpGEpLCoPathUpDateTime_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathUpDateTime.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoStatsTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpLCoStatsTable = _MscMcsMgrDprsMcsEpGEpLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 11)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoStatsTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoStatsEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpLCoStatsEntry = _MscMcsMgrDprsMcsEpGEpLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 11, 1)
)
mscMcsMgrDprsMcsEpGEpLCoStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpLCoIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoStatsEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoPktsToNetwork_Type = PassportCounter64
_MscMcsMgrDprsMcsEpGEpLCoPktsToNetwork_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPktsToNetwork = _MscMcsMgrDprsMcsEpGEpLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 11, 1, 1),
    _MscMcsMgrDprsMcsEpGEpLCoPktsToNetwork_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPktsToNetwork.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoBytesToNetwork_Type = PassportCounter64
_MscMcsMgrDprsMcsEpGEpLCoBytesToNetwork_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoBytesToNetwork = _MscMcsMgrDprsMcsEpGEpLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 11, 1, 2),
    _MscMcsMgrDprsMcsEpGEpLCoBytesToNetwork_Type()
)
mscMcsMgrDprsMcsEpGEpLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoBytesToNetwork.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork_Type = PassportCounter64
_MscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork = _MscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 11, 1, 3),
    _MscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork_Type = PassportCounter64
_MscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork = _MscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 11, 1, 4),
    _MscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork_Type()
)
mscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoPathTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpLCoPathTable = _MscMcsMgrDprsMcsEpGEpLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 264)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpLCoPathEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpLCoPathEntry = _MscMcsMgrDprsMcsEpGEpLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 264, 1)
)
mscMcsMgrDprsMcsEpGEpLCoPathEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpLCoIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpLCoPathValue"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLCoPathValue_Type(AsciiString):
    """Custom type mscMcsMgrDprsMcsEpGEpLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscMcsMgrDprsMcsEpGEpLCoPathValue_Type.__name__ = "AsciiString"
_MscMcsMgrDprsMcsEpGEpLCoPathValue_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLCoPathValue = _MscMcsMgrDprsMcsEpGEpLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 4, 264, 1, 1),
    _MscMcsMgrDprsMcsEpGEpLCoPathValue_Type()
)
mscMcsMgrDprsMcsEpGEpLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLCoPathValue.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCac_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGEpCac = _MscMcsMgrDprsMcsEpGEpCac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5)
)
_MscMcsMgrDprsMcsEpGEpCacRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacRowStatusTable = _MscMcsMgrDprsMcsEpGEpCacRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacRowStatusEntry = _MscMcsMgrDprsMcsEpGEpCacRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 1, 1)
)
mscMcsMgrDprsMcsEpGEpCacRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGEpCacRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacRowStatus = _MscMcsMgrDprsMcsEpGEpCacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacRowStatus_Type()
)
mscMcsMgrDprsMcsEpGEpCacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGEpCacComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacComponentName = _MscMcsMgrDprsMcsEpGEpCacComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpCacComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGEpCacStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacStorageType = _MscMcsMgrDprsMcsEpGEpCacStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGEpCacStorageType_Type()
)
mscMcsMgrDprsMcsEpGEpCacStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacStorageType.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacIndex_Type = NonReplicated
_MscMcsMgrDprsMcsEpGEpCacIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacIndex = _MscMcsMgrDprsMcsEpGEpCacIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGEpCacIndex_Type()
)
mscMcsMgrDprsMcsEpGEpCacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacd_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGEpCacCacd = _MscMcsMgrDprsMcsEpGEpCacCacd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2)
)
_MscMcsMgrDprsMcsEpGEpCacCacdRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacCacdRowStatusTable = _MscMcsMgrDprsMcsEpGEpCacCacdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacCacdRowStatusEntry = _MscMcsMgrDprsMcsEpGEpCacCacdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 1, 1)
)
mscMcsMgrDprsMcsEpGEpCacCacdRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacCacdIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGEpCacCacdRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdRowStatus = _MscMcsMgrDprsMcsEpGEpCacCacdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacCacdRowStatus_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGEpCacCacdComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdComponentName = _MscMcsMgrDprsMcsEpGEpCacCacdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacCacdComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGEpCacCacdStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdStorageType = _MscMcsMgrDprsMcsEpGEpCacCacdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGEpCacCacdStorageType_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdStorageType.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdIndex_Type = NonReplicated
_MscMcsMgrDprsMcsEpGEpCacCacdIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdIndex = _MscMcsMgrDprsMcsEpGEpCacCacdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGEpCacCacdIndex_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdFrwdTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacCacdFrwdTable = _MscMcsMgrDprsMcsEpGEpCacCacdFrwdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdFrwdTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdFrwdEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacCacdFrwdEntry = _MscMcsMgrDprsMcsEpGEpCacCacdFrwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 10, 1)
)
mscMcsMgrDprsMcsEpGEpCacCacdFrwdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacCacdIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdFrwdEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enforced", 0),
          ("monitored", 1))
    )


_MscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy = _MscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdForwardCacType_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdForwardCacType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cir", 1),
          ("eir", 0))
    )


_MscMcsMgrDprsMcsEpGEpCacCacdForwardCacType_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacdForwardCacType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdForwardCacType = _MscMcsMgrDprsMcsEpGEpCacCacdForwardCacType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacCacdForwardCacType_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdForwardCacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdForwardCacType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor_Type(FixedPoint2):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor based on FixedPoint2"""
    defaultValue = 100

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor_Type.__name__ = "FixedPoint2"
_MscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor = _MscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 10, 1, 3),
    _MscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw based on Unsigned32"""
    defaultValue = 155000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
        ValueRangeConstraint(155000001, 155000001),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw = _MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 10, 1, 4),
    _MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw based on Unsigned32"""
    defaultValue = 155000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
        ValueRangeConstraint(155000001, 155000001),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw = _MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 10, 1, 5),
    _MscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdRvrsTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacCacdRvrsTable = _MscMcsMgrDprsMcsEpGEpCacCacdRvrsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 11)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRvrsTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdRvrsEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacCacdRvrsEntry = _MscMcsMgrDprsMcsEpGEpCacCacdRvrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 11, 1)
)
mscMcsMgrDprsMcsEpGEpCacCacdRvrsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacCacdIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRvrsEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy based on Integer32"""
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
        *(("enforced", 0),
          ("monitored", 1),
          ("sameAsForward", 2))
    )


_MscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy = _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 11, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacType_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdReverseCacType based on Integer32"""
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
        *(("cir", 1),
          ("eir", 0),
          ("sameAsForward", 2))
    )


_MscMcsMgrDprsMcsEpGEpCacCacdReverseCacType_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacdReverseCacType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdReverseCacType = _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 11, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacType_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdReverseCacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdReverseCacType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub_Type(FixedPoint2):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub based on FixedPoint2"""
    defaultValue = 10100

    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
        ValueRangeConstraint(10100, 10100),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub_Type.__name__ = "FixedPoint2"
_MscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub = _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 11, 1, 3),
    _MscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw based on Unsigned32"""
    defaultValue = 155000002

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
        ValueRangeConstraint(155000001, 155000001),
        ValueRangeConstraint(155000002, 155000002),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw = _MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 11, 1, 4),
    _MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw based on Unsigned32"""
    defaultValue = 155000002

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
        ValueRangeConstraint(155000001, 155000001),
        ValueRangeConstraint(155000002, 155000002),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw = _MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 11, 1, 5),
    _MscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshTable = _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 800)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshEntry = _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 800, 1)
)
mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacCacdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("major", 1),
          ("minor", 0))
    )


_MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex = _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 800, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue = _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 800, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshTable = _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 801)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshEntry = _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 801, 1)
)
mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacCacdIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("major", 1),
          ("minor", 0))
    )


_MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex = _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 801, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue = _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 2, 801, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacOperTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacOperTable = _MscMcsMgrDprsMcsEpGEpCacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacOperTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacOperEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacOperEntry = _MscMcsMgrDprsMcsEpGEpCacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1)
)
mscMcsMgrDprsMcsEpGEpCacOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacOperEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth_Type(Unsigned64):
    """Custom type mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth_Type.__name__ = "Unsigned64"
_MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth = _MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable_Type(Unsigned64):
    """Custom type mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable_Type.__name__ = "Unsigned64"
_MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable = _MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable_Type()
)
mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_MscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive = _MscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 3),
    _MscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive_Type()
)
mscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacPolicy_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enforced", 0),
          ("monitored", 1))
    )


_MscMcsMgrDprsMcsEpGEpCacCacPolicy_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacPolicy_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacPolicy = _MscMcsMgrDprsMcsEpGEpCacCacPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 4),
    _MscMcsMgrDprsMcsEpGEpCacCacPolicy_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacPolicy.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacCacType_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacCacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cir", 1),
          ("eir", 0))
    )


_MscMcsMgrDprsMcsEpGEpCacCacType_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacCacType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacCacType = _MscMcsMgrDprsMcsEpGEpCacCacType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 5),
    _MscMcsMgrDprsMcsEpGEpCacCacType_Type()
)
mscMcsMgrDprsMcsEpGEpCacCacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacCacType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
        ValueRangeConstraint(155000001, 155000001),
    )


_MscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth = _MscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 6),
    _MscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
        ValueRangeConstraint(155000001, 155000001),
    )


_MscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth = _MscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 7),
    _MscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures_Type = Counter32
_MscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures = _MscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 8),
    _MscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures_Type()
)
mscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci_Type = RowPointer
_MscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci = _MscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 9),
    _MscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci_Type()
)
mscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacLastFailedReason_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacLastFailedReason based on Integer32"""
    defaultValue = 0

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
        *(("epCacUnavailable", 4),
          ("maxConsExceeded", 5),
          ("maxPvcExceeded", 3),
          ("maxSvcExceeded", 2),
          ("noBandwidthAvailable", 1),
          ("none", 0))
    )


_MscMcsMgrDprsMcsEpGEpCacLastFailedReason_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacLastFailedReason_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacLastFailedReason = _MscMcsMgrDprsMcsEpGEpCacLastFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 10),
    _MscMcsMgrDprsMcsEpGEpCacLastFailedReason_Type()
)
mscMcsMgrDprsMcsEpGEpCacLastFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacLastFailedReason.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor_Type(FixedPoint2):
    """Custom type mscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor based on FixedPoint2"""
    subtypeSpec = FixedPoint2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor_Type.__name__ = "FixedPoint2"
_MscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor = _MscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 10, 1, 11),
    _MscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor_Type()
)
mscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacAlarmThresholdTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpCacAlarmThresholdTable = _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 802)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacAlarmThresholdTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCacAlarmThresholdEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpCacAlarmThresholdEntry = _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 802, 1)
)
mscMcsMgrDprsMcsEpGEpCacAlarmThresholdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacAlarmThresholdEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("major", 1),
          ("minor", 0))
    )


_MscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex = _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 802, 1, 1),
    _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex_Type()
)
mscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue = _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 5, 802, 1, 2),
    _MscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue_Type()
)
mscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpCon_ObjectIdentity = ObjectIdentity
mscMcsMgrDprsMcsEpGEpCon = _MscMcsMgrDprsMcsEpGEpCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6)
)
_MscMcsMgrDprsMcsEpGEpConRowStatusTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpConRowStatusTable = _MscMcsMgrDprsMcsEpGEpConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConRowStatusTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpConRowStatusEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpConRowStatusEntry = _MscMcsMgrDprsMcsEpGEpConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 1, 1)
)
mscMcsMgrDprsMcsEpGEpConRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpConIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConRowStatusEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpConRowStatus_Type = RowStatus
_MscMcsMgrDprsMcsEpGEpConRowStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpConRowStatus = _MscMcsMgrDprsMcsEpGEpConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 1, 1, 1),
    _MscMcsMgrDprsMcsEpGEpConRowStatus_Type()
)
mscMcsMgrDprsMcsEpGEpConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConRowStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpConComponentName_Type = DisplayString
_MscMcsMgrDprsMcsEpGEpConComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpConComponentName = _MscMcsMgrDprsMcsEpGEpConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 1, 1, 2),
    _MscMcsMgrDprsMcsEpGEpConComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConComponentName.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpConStorageType_Type = StorageType
_MscMcsMgrDprsMcsEpGEpConStorageType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpConStorageType = _MscMcsMgrDprsMcsEpGEpConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 1, 1, 4),
    _MscMcsMgrDprsMcsEpGEpConStorageType_Type()
)
mscMcsMgrDprsMcsEpGEpConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConStorageType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpConIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpConIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_MscMcsMgrDprsMcsEpGEpConIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpConIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpConIndex = _MscMcsMgrDprsMcsEpGEpConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 1, 1, 10),
    _MscMcsMgrDprsMcsEpGEpConIndex_Type()
)
mscMcsMgrDprsMcsEpGEpConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpConOperTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpConOperTable = _MscMcsMgrDprsMcsEpGEpConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConOperTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpConOperEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpConOperEntry = _MscMcsMgrDprsMcsEpGEpConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 10, 1)
)
mscMcsMgrDprsMcsEpGEpConOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpConIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConOperEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpConFrameRelayDlci_Type = RowPointer
_MscMcsMgrDprsMcsEpGEpConFrameRelayDlci_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpConFrameRelayDlci = _MscMcsMgrDprsMcsEpGEpConFrameRelayDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGEpConFrameRelayDlci_Type()
)
mscMcsMgrDprsMcsEpGEpConFrameRelayDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConFrameRelayDlci.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpConReservedBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpConReservedBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_MscMcsMgrDprsMcsEpGEpConReservedBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpConReservedBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpConReservedBandwidth = _MscMcsMgrDprsMcsEpGEpConReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 6, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGEpConReservedBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpConReservedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConReservedBandwidth.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpStateTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpStateTable = _MscMcsMgrDprsMcsEpGEpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpStateTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpStateEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpStateEntry = _MscMcsMgrDprsMcsEpGEpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1)
)
mscMcsMgrDprsMcsEpGEpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpStateEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpAdminState_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpAdminState based on Integer32"""
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


_MscMcsMgrDprsMcsEpGEpAdminState_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpAdminState_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAdminState = _MscMcsMgrDprsMcsEpGEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGEpAdminState_Type()
)
mscMcsMgrDprsMcsEpGEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAdminState.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpOperationalState_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpOperationalState based on Integer32"""
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


_MscMcsMgrDprsMcsEpGEpOperationalState_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpOperationalState_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpOperationalState = _MscMcsMgrDprsMcsEpGEpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGEpOperationalState_Type()
)
mscMcsMgrDprsMcsEpGEpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpOperationalState.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpUsageState_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpUsageState based on Integer32"""
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


_MscMcsMgrDprsMcsEpGEpUsageState_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpUsageState_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpUsageState = _MscMcsMgrDprsMcsEpGEpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 3),
    _MscMcsMgrDprsMcsEpGEpUsageState_Type()
)
mscMcsMgrDprsMcsEpGEpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpUsageState.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpAvailabilityStatus_Type(OctetString):
    """Custom type mscMcsMgrDprsMcsEpGEpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMcsMgrDprsMcsEpGEpAvailabilityStatus_Type.__name__ = "OctetString"
_MscMcsMgrDprsMcsEpGEpAvailabilityStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAvailabilityStatus = _MscMcsMgrDprsMcsEpGEpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 4),
    _MscMcsMgrDprsMcsEpGEpAvailabilityStatus_Type()
)
mscMcsMgrDprsMcsEpGEpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAvailabilityStatus.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpProceduralStatus_Type(OctetString):
    """Custom type mscMcsMgrDprsMcsEpGEpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrDprsMcsEpGEpProceduralStatus_Type.__name__ = "OctetString"
_MscMcsMgrDprsMcsEpGEpProceduralStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpProceduralStatus = _MscMcsMgrDprsMcsEpGEpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 5),
    _MscMcsMgrDprsMcsEpGEpProceduralStatus_Type()
)
mscMcsMgrDprsMcsEpGEpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpProceduralStatus.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpControlStatus_Type(OctetString):
    """Custom type mscMcsMgrDprsMcsEpGEpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrDprsMcsEpGEpControlStatus_Type.__name__ = "OctetString"
_MscMcsMgrDprsMcsEpGEpControlStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpControlStatus = _MscMcsMgrDprsMcsEpGEpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 6),
    _MscMcsMgrDprsMcsEpGEpControlStatus_Type()
)
mscMcsMgrDprsMcsEpGEpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpControlStatus.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpAlarmStatus_Type(OctetString):
    """Custom type mscMcsMgrDprsMcsEpGEpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscMcsMgrDprsMcsEpGEpAlarmStatus_Type.__name__ = "OctetString"
_MscMcsMgrDprsMcsEpGEpAlarmStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpAlarmStatus = _MscMcsMgrDprsMcsEpGEpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 7),
    _MscMcsMgrDprsMcsEpGEpAlarmStatus_Type()
)
mscMcsMgrDprsMcsEpGEpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpAlarmStatus.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpStandbyStatus_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpStandbyStatus based on Integer32"""
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


_MscMcsMgrDprsMcsEpGEpStandbyStatus_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpStandbyStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpStandbyStatus = _MscMcsMgrDprsMcsEpGEpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 8),
    _MscMcsMgrDprsMcsEpGEpStandbyStatus_Type()
)
mscMcsMgrDprsMcsEpGEpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpStandbyStatus.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpUnknownStatus_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpUnknownStatus based on Integer32"""
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


_MscMcsMgrDprsMcsEpGEpUnknownStatus_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpUnknownStatus_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpUnknownStatus = _MscMcsMgrDprsMcsEpGEpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 10, 1, 9),
    _MscMcsMgrDprsMcsEpGEpUnknownStatus_Type()
)
mscMcsMgrDprsMcsEpGEpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpUnknownStatus.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpOperTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpOperTable = _MscMcsMgrDprsMcsEpGEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpOperTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpOperEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpOperEntry = _MscMcsMgrDprsMcsEpGEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1)
)
mscMcsMgrDprsMcsEpGEpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpOperEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause = _MscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 3),
    _MscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Type()
)
mscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpType_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("originating", 0),
          ("terminating", 1))
    )


_MscMcsMgrDprsMcsEpGEpType_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpType_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpType = _MscMcsMgrDprsMcsEpGEpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 4),
    _MscMcsMgrDprsMcsEpGEpType_Type()
)
mscMcsMgrDprsMcsEpGEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpType.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpSupportedTransferPriorities_Type(OctetString):
    """Custom type mscMcsMgrDprsMcsEpGEpSupportedTransferPriorities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscMcsMgrDprsMcsEpGEpSupportedTransferPriorities_Type.__name__ = "OctetString"
_MscMcsMgrDprsMcsEpGEpSupportedTransferPriorities_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpSupportedTransferPriorities = _MscMcsMgrDprsMcsEpGEpSupportedTransferPriorities_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 5),
    _MscMcsMgrDprsMcsEpGEpSupportedTransferPriorities_Type()
)
mscMcsMgrDprsMcsEpGEpSupportedTransferPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpSupportedTransferPriorities.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpConnectionTransferPriority_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscMcsMgrDprsMcsEpGEpConnectionTransferPriority_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpConnectionTransferPriority_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpConnectionTransferPriority = _MscMcsMgrDprsMcsEpGEpConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 6),
    _MscMcsMgrDprsMcsEpGEpConnectionTransferPriority_Type()
)
mscMcsMgrDprsMcsEpGEpConnectionTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpConnectionTransferPriority.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpServiceCategory_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpServiceCategory based on Integer32"""
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


_MscMcsMgrDprsMcsEpGEpServiceCategory_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpServiceCategory_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpServiceCategory = _MscMcsMgrDprsMcsEpGEpServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 7),
    _MscMcsMgrDprsMcsEpGEpServiceCategory_Type()
)
mscMcsMgrDprsMcsEpGEpServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpServiceCategory.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_MscMcsMgrDprsMcsEpGEpBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpBandwidth = _MscMcsMgrDprsMcsEpGEpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 8),
    _MscMcsMgrDprsMcsEpGEpBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpBandwidth.setStatus("obsolete")


class _MscMcsMgrDprsMcsEpGEpRemoteComponentName_Type(AsciiString):
    """Custom type mscMcsMgrDprsMcsEpGEpRemoteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_MscMcsMgrDprsMcsEpGEpRemoteComponentName_Type.__name__ = "AsciiString"
_MscMcsMgrDprsMcsEpGEpRemoteComponentName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpRemoteComponentName = _MscMcsMgrDprsMcsEpGEpRemoteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 9),
    _MscMcsMgrDprsMcsEpGEpRemoteComponentName_Type()
)
mscMcsMgrDprsMcsEpGEpRemoteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpRemoteComponentName.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpRemoteRoutingId_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpRemoteRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_MscMcsMgrDprsMcsEpGEpRemoteRoutingId_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpRemoteRoutingId_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpRemoteRoutingId = _MscMcsMgrDprsMcsEpGEpRemoteRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 10),
    _MscMcsMgrDprsMcsEpGEpRemoteRoutingId_Type()
)
mscMcsMgrDprsMcsEpGEpRemoteRoutingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpRemoteRoutingId.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpRemoteModuleId_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpRemoteModuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1909),
    )


_MscMcsMgrDprsMcsEpGEpRemoteModuleId_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpRemoteModuleId_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpRemoteModuleId = _MscMcsMgrDprsMcsEpGEpRemoteModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 11),
    _MscMcsMgrDprsMcsEpGEpRemoteModuleId_Type()
)
mscMcsMgrDprsMcsEpGEpRemoteModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpRemoteModuleId.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpLastTrConnDiagCode_Type(HexString):
    """Custom type mscMcsMgrDprsMcsEpGEpLastTrConnDiagCode based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MscMcsMgrDprsMcsEpGEpLastTrConnDiagCode_Type.__name__ = "HexString"
_MscMcsMgrDprsMcsEpGEpLastTrConnDiagCode_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpLastTrConnDiagCode = _MscMcsMgrDprsMcsEpGEpLastTrConnDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 12),
    _MscMcsMgrDprsMcsEpGEpLastTrConnDiagCode_Type()
)
mscMcsMgrDprsMcsEpGEpLastTrConnDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpLastTrConnDiagCode.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpForwardBandwith_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpForwardBandwith based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_MscMcsMgrDprsMcsEpGEpForwardBandwith_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpForwardBandwith_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpForwardBandwith = _MscMcsMgrDprsMcsEpGEpForwardBandwith_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 13),
    _MscMcsMgrDprsMcsEpGEpForwardBandwith_Type()
)
mscMcsMgrDprsMcsEpGEpForwardBandwith.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpForwardBandwith.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpReverseBandwidth_Type(Unsigned32):
    """Custom type mscMcsMgrDprsMcsEpGEpReverseBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_MscMcsMgrDprsMcsEpGEpReverseBandwidth_Type.__name__ = "Unsigned32"
_MscMcsMgrDprsMcsEpGEpReverseBandwidth_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpReverseBandwidth = _MscMcsMgrDprsMcsEpGEpReverseBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 11, 1, 14),
    _MscMcsMgrDprsMcsEpGEpReverseBandwidth_Type()
)
mscMcsMgrDprsMcsEpGEpReverseBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpReverseBandwidth.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpStatsTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpStatsTable = _MscMcsMgrDprsMcsEpGEpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 12)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpStatsTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpStatsEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpStatsEntry = _MscMcsMgrDprsMcsEpGEpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 12, 1)
)
mscMcsMgrDprsMcsEpGEpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpStatsEntry.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpSetupAttempts_Type = Counter32
_MscMcsMgrDprsMcsEpGEpSetupAttempts_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpSetupAttempts = _MscMcsMgrDprsMcsEpGEpSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 12, 1, 1),
    _MscMcsMgrDprsMcsEpGEpSetupAttempts_Type()
)
mscMcsMgrDprsMcsEpGEpSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpSetupAttempts.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Type = Counter32
_MscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs = _MscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 12, 1, 2),
    _MscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Type()
)
mscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpPktFromMcsTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpPktFromMcsTable = _MscMcsMgrDprsMcsEpGEpPktFromMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 402)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktFromMcsTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpPktFromMcsEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpPktFromMcsEntry = _MscMcsMgrDprsMcsEpGEpPktFromMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 402, 1)
)
mscMcsMgrDprsMcsEpGEpPktFromMcsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpPktFromMcsIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktFromMcsEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpPktFromMcsIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpPktFromMcsIndex based on Integer32"""
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
        *(("discardPriority0", 0),
          ("discardPriority1", 1),
          ("discardPriority2", 2),
          ("discardPriority3", 3))
    )


_MscMcsMgrDprsMcsEpGEpPktFromMcsIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpPktFromMcsIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpPktFromMcsIndex = _MscMcsMgrDprsMcsEpGEpPktFromMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 402, 1, 1),
    _MscMcsMgrDprsMcsEpGEpPktFromMcsIndex_Type()
)
mscMcsMgrDprsMcsEpGEpPktFromMcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktFromMcsIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpPktFromMcsValue_Type = PassportCounter64
_MscMcsMgrDprsMcsEpGEpPktFromMcsValue_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpPktFromMcsValue = _MscMcsMgrDprsMcsEpGEpPktFromMcsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 402, 1, 2),
    _MscMcsMgrDprsMcsEpGEpPktFromMcsValue_Type()
)
mscMcsMgrDprsMcsEpGEpPktFromMcsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktFromMcsValue.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpOctetsFromMcsTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpOctetsFromMcsTable = _MscMcsMgrDprsMcsEpGEpOctetsFromMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 403)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpOctetsFromMcsTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpOctetsFromMcsEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpOctetsFromMcsEntry = _MscMcsMgrDprsMcsEpGEpOctetsFromMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 403, 1)
)
mscMcsMgrDprsMcsEpGEpOctetsFromMcsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpOctetsFromMcsEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex based on Integer32"""
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
        *(("discardPriority0", 0),
          ("discardPriority1", 1),
          ("discardPriority2", 2),
          ("discardPriority3", 3))
    )


_MscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex = _MscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 403, 1, 1),
    _MscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex_Type()
)
mscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpOctetsFromMcsValue_Type = PassportCounter64
_MscMcsMgrDprsMcsEpGEpOctetsFromMcsValue_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpOctetsFromMcsValue = _MscMcsMgrDprsMcsEpGEpOctetsFromMcsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 403, 1, 2),
    _MscMcsMgrDprsMcsEpGEpOctetsFromMcsValue_Type()
)
mscMcsMgrDprsMcsEpGEpOctetsFromMcsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpOctetsFromMcsValue.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable_Object = MibTable
mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable = _MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 404)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry = _MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 404, 1)
)
mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Type(Integer32):
    """Custom type mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex based on Integer32"""
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
        *(("discardPriority0", 0),
          ("discardPriority1", 1),
          ("discardPriority2", 2),
          ("discardPriority3", 3))
    )


_MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Type.__name__ = "Integer32"
_MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex = _MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 404, 1, 1),
    _MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Type()
)
mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Type = Counter32
_MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Object = MibTableColumn
mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue = _MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 3, 404, 1, 2),
    _MscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Type()
)
mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGOperTable_Object = MibTable
mscMcsMgrDprsMcsEpGOperTable = _MscMcsMgrDprsMcsEpGOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 10)
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGOperTable.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGOperEntry_Object = MibTableRow
mscMcsMgrDprsMcsEpGOperEntry = _MscMcsMgrDprsMcsEpGOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 10, 1)
)
mscMcsMgrDprsMcsEpGOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-McsMgrMIB", "mscMcsMgrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB", "mscMcsMgrDprsMcsEpGIndex"),
)
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGOperEntry.setStatus("mandatory")


class _MscMcsMgrDprsMcsEpGRemoteAddress_Type(AsciiString):
    """Custom type mscMcsMgrDprsMcsEpGRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_MscMcsMgrDprsMcsEpGRemoteAddress_Type.__name__ = "AsciiString"
_MscMcsMgrDprsMcsEpGRemoteAddress_Object = MibTableColumn
mscMcsMgrDprsMcsEpGRemoteAddress = _MscMcsMgrDprsMcsEpGRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 10, 1, 1),
    _MscMcsMgrDprsMcsEpGRemoteAddress_Type()
)
mscMcsMgrDprsMcsEpGRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGRemoteAddress.setStatus("mandatory")
_MscMcsMgrDprsMcsEpGAssociatedEpGroupName_Type = RowPointer
_MscMcsMgrDprsMcsEpGAssociatedEpGroupName_Object = MibTableColumn
mscMcsMgrDprsMcsEpGAssociatedEpGroupName = _MscMcsMgrDprsMcsEpGAssociatedEpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 122, 2, 10, 1, 2),
    _MscMcsMgrDprsMcsEpGAssociatedEpGroupName_Type()
)
mscMcsMgrDprsMcsEpGAssociatedEpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscMcsMgrDprsMcsEpGAssociatedEpGroupName.setStatus("mandatory")
_DprsMcsEpMIB_ObjectIdentity = ObjectIdentity
dprsMcsEpMIB = _DprsMcsEpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125)
)
_DprsMcsEpGroup_ObjectIdentity = ObjectIdentity
dprsMcsEpGroup = _DprsMcsEpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 1)
)
_DprsMcsEpGroupCA_ObjectIdentity = ObjectIdentity
dprsMcsEpGroupCA = _DprsMcsEpGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 1, 1)
)
_DprsMcsEpGroupCA02_ObjectIdentity = ObjectIdentity
dprsMcsEpGroupCA02 = _DprsMcsEpGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 1, 1, 3)
)
_DprsMcsEpGroupCA02A_ObjectIdentity = ObjectIdentity
dprsMcsEpGroupCA02A = _DprsMcsEpGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 1, 1, 3, 2)
)
_DprsMcsEpCapabilities_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilities = _DprsMcsEpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 3)
)
_DprsMcsEpCapabilitiesCA_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilitiesCA = _DprsMcsEpCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 3, 1)
)
_DprsMcsEpCapabilitiesCA02_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilitiesCA02 = _DprsMcsEpCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 3, 1, 3)
)
_DprsMcsEpCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilitiesCA02A = _DprsMcsEpCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 125, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-DprsMcsEpMIB",
    **{"mscMcsMgrDprsMcsEpG": mscMcsMgrDprsMcsEpG,
       "mscMcsMgrDprsMcsEpGRowStatusTable": mscMcsMgrDprsMcsEpGRowStatusTable,
       "mscMcsMgrDprsMcsEpGRowStatusEntry": mscMcsMgrDprsMcsEpGRowStatusEntry,
       "mscMcsMgrDprsMcsEpGRowStatus": mscMcsMgrDprsMcsEpGRowStatus,
       "mscMcsMgrDprsMcsEpGComponentName": mscMcsMgrDprsMcsEpGComponentName,
       "mscMcsMgrDprsMcsEpGStorageType": mscMcsMgrDprsMcsEpGStorageType,
       "mscMcsMgrDprsMcsEpGIndex": mscMcsMgrDprsMcsEpGIndex,
       "mscMcsMgrDprsMcsEpGAddr": mscMcsMgrDprsMcsEpGAddr,
       "mscMcsMgrDprsMcsEpGAddrRowStatusTable": mscMcsMgrDprsMcsEpGAddrRowStatusTable,
       "mscMcsMgrDprsMcsEpGAddrRowStatusEntry": mscMcsMgrDprsMcsEpGAddrRowStatusEntry,
       "mscMcsMgrDprsMcsEpGAddrRowStatus": mscMcsMgrDprsMcsEpGAddrRowStatus,
       "mscMcsMgrDprsMcsEpGAddrComponentName": mscMcsMgrDprsMcsEpGAddrComponentName,
       "mscMcsMgrDprsMcsEpGAddrStorageType": mscMcsMgrDprsMcsEpGAddrStorageType,
       "mscMcsMgrDprsMcsEpGAddrIndex": mscMcsMgrDprsMcsEpGAddrIndex,
       "mscMcsMgrDprsMcsEpGAddrProvTable": mscMcsMgrDprsMcsEpGAddrProvTable,
       "mscMcsMgrDprsMcsEpGAddrProvEntry": mscMcsMgrDprsMcsEpGAddrProvEntry,
       "mscMcsMgrDprsMcsEpGAddrRemoteAddress": mscMcsMgrDprsMcsEpGAddrRemoteAddress,
       "mscMcsMgrDprsMcsEpGAddrCommentText": mscMcsMgrDprsMcsEpGAddrCommentText,
       "mscMcsMgrDprsMcsEpGEp": mscMcsMgrDprsMcsEpGEp,
       "mscMcsMgrDprsMcsEpGEpRowStatusTable": mscMcsMgrDprsMcsEpGEpRowStatusTable,
       "mscMcsMgrDprsMcsEpGEpRowStatusEntry": mscMcsMgrDprsMcsEpGEpRowStatusEntry,
       "mscMcsMgrDprsMcsEpGEpRowStatus": mscMcsMgrDprsMcsEpGEpRowStatus,
       "mscMcsMgrDprsMcsEpGEpComponentName": mscMcsMgrDprsMcsEpGEpComponentName,
       "mscMcsMgrDprsMcsEpGEpStorageType": mscMcsMgrDprsMcsEpGEpStorageType,
       "mscMcsMgrDprsMcsEpGEpIndex": mscMcsMgrDprsMcsEpGEpIndex,
       "mscMcsMgrDprsMcsEpGEpEpD": mscMcsMgrDprsMcsEpGEpEpD,
       "mscMcsMgrDprsMcsEpGEpEpDRowStatusTable": mscMcsMgrDprsMcsEpGEpEpDRowStatusTable,
       "mscMcsMgrDprsMcsEpGEpEpDRowStatusEntry": mscMcsMgrDprsMcsEpGEpEpDRowStatusEntry,
       "mscMcsMgrDprsMcsEpGEpEpDRowStatus": mscMcsMgrDprsMcsEpGEpEpDRowStatus,
       "mscMcsMgrDprsMcsEpGEpEpDComponentName": mscMcsMgrDprsMcsEpGEpEpDComponentName,
       "mscMcsMgrDprsMcsEpGEpEpDStorageType": mscMcsMgrDprsMcsEpGEpEpDStorageType,
       "mscMcsMgrDprsMcsEpGEpEpDIndex": mscMcsMgrDprsMcsEpGEpEpDIndex,
       "mscMcsMgrDprsMcsEpGEpEpDProvTable": mscMcsMgrDprsMcsEpGEpEpDProvTable,
       "mscMcsMgrDprsMcsEpGEpEpDProvEntry": mscMcsMgrDprsMcsEpGEpEpDProvEntry,
       "mscMcsMgrDprsMcsEpGEpEpDBandwidth": mscMcsMgrDprsMcsEpGEpEpDBandwidth,
       "mscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority": mscMcsMgrDprsMcsEpGEpEpDConnectionTransferPriority,
       "mscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference": mscMcsMgrDprsMcsEpGEpEpDTransportConnectionPreference,
       "mscMcsMgrDprsMcsEpGEpEpDProfile": mscMcsMgrDprsMcsEpGEpEpDProfile,
       "mscMcsMgrDprsMcsEpGEpEpDPorsManualPath": mscMcsMgrDprsMcsEpGEpEpDPorsManualPath,
       "mscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities": mscMcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities,
       "mscMcsMgrDprsMcsEpGEpEpDForwardBandwidth": mscMcsMgrDprsMcsEpGEpEpDForwardBandwidth,
       "mscMcsMgrDprsMcsEpGEpEpDReverseBandwidth": mscMcsMgrDprsMcsEpGEpEpDReverseBandwidth,
       "mscMcsMgrDprsMcsEpGEpAtmCon": mscMcsMgrDprsMcsEpGEpAtmCon,
       "mscMcsMgrDprsMcsEpGEpAtmConRowStatusTable": mscMcsMgrDprsMcsEpGEpAtmConRowStatusTable,
       "mscMcsMgrDprsMcsEpGEpAtmConRowStatusEntry": mscMcsMgrDprsMcsEpGEpAtmConRowStatusEntry,
       "mscMcsMgrDprsMcsEpGEpAtmConRowStatus": mscMcsMgrDprsMcsEpGEpAtmConRowStatus,
       "mscMcsMgrDprsMcsEpGEpAtmConComponentName": mscMcsMgrDprsMcsEpGEpAtmConComponentName,
       "mscMcsMgrDprsMcsEpGEpAtmConStorageType": mscMcsMgrDprsMcsEpGEpAtmConStorageType,
       "mscMcsMgrDprsMcsEpGEpAtmConIndex": mscMcsMgrDprsMcsEpGEpAtmConIndex,
       "mscMcsMgrDprsMcsEpGEpAtmConOperTable": mscMcsMgrDprsMcsEpGEpAtmConOperTable,
       "mscMcsMgrDprsMcsEpGEpAtmConOperEntry": mscMcsMgrDprsMcsEpGEpAtmConOperEntry,
       "mscMcsMgrDprsMcsEpGEpAtmConNextHop": mscMcsMgrDprsMcsEpGEpAtmConNextHop,
       "mscMcsMgrDprsMcsEpGEpLCo": mscMcsMgrDprsMcsEpGEpLCo,
       "mscMcsMgrDprsMcsEpGEpLCoRowStatusTable": mscMcsMgrDprsMcsEpGEpLCoRowStatusTable,
       "mscMcsMgrDprsMcsEpGEpLCoRowStatusEntry": mscMcsMgrDprsMcsEpGEpLCoRowStatusEntry,
       "mscMcsMgrDprsMcsEpGEpLCoRowStatus": mscMcsMgrDprsMcsEpGEpLCoRowStatus,
       "mscMcsMgrDprsMcsEpGEpLCoComponentName": mscMcsMgrDprsMcsEpGEpLCoComponentName,
       "mscMcsMgrDprsMcsEpGEpLCoStorageType": mscMcsMgrDprsMcsEpGEpLCoStorageType,
       "mscMcsMgrDprsMcsEpGEpLCoIndex": mscMcsMgrDprsMcsEpGEpLCoIndex,
       "mscMcsMgrDprsMcsEpGEpLCoPathDataTable": mscMcsMgrDprsMcsEpGEpLCoPathDataTable,
       "mscMcsMgrDprsMcsEpGEpLCoPathDataEntry": mscMcsMgrDprsMcsEpGEpLCoPathDataEntry,
       "mscMcsMgrDprsMcsEpGEpLCoState": mscMcsMgrDprsMcsEpGEpLCoState,
       "mscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName": mscMcsMgrDprsMcsEpGEpLCoOverrideRemoteName,
       "mscMcsMgrDprsMcsEpGEpLCoEnd": mscMcsMgrDprsMcsEpGEpLCoEnd,
       "mscMcsMgrDprsMcsEpGEpLCoCostMetric": mscMcsMgrDprsMcsEpGEpLCoCostMetric,
       "mscMcsMgrDprsMcsEpGEpLCoDelayMetric": mscMcsMgrDprsMcsEpGEpLCoDelayMetric,
       "mscMcsMgrDprsMcsEpGEpLCoRoundTripDelay": mscMcsMgrDprsMcsEpGEpLCoRoundTripDelay,
       "mscMcsMgrDprsMcsEpGEpLCoSetupPriority": mscMcsMgrDprsMcsEpGEpLCoSetupPriority,
       "mscMcsMgrDprsMcsEpGEpLCoHoldingPriority": mscMcsMgrDprsMcsEpGEpLCoHoldingPriority,
       "mscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth": mscMcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth,
       "mscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth": mscMcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth,
       "mscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType": mscMcsMgrDprsMcsEpGEpLCoRequiredTrafficType,
       "mscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes": mscMcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes,
       "mscMcsMgrDprsMcsEpGEpLCoRequiredSecurity": mscMcsMgrDprsMcsEpGEpLCoRequiredSecurity,
       "mscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter": mscMcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter,
       "mscMcsMgrDprsMcsEpGEpLCoEmissionPriority": mscMcsMgrDprsMcsEpGEpLCoEmissionPriority,
       "mscMcsMgrDprsMcsEpGEpLCoDiscardPriority": mscMcsMgrDprsMcsEpGEpLCoDiscardPriority,
       "mscMcsMgrDprsMcsEpGEpLCoPathType": mscMcsMgrDprsMcsEpGEpLCoPathType,
       "mscMcsMgrDprsMcsEpGEpLCoRetryCount": mscMcsMgrDprsMcsEpGEpLCoRetryCount,
       "mscMcsMgrDprsMcsEpGEpLCoPathFailureCount": mscMcsMgrDprsMcsEpGEpLCoPathFailureCount,
       "mscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute": mscMcsMgrDprsMcsEpGEpLCoReasonForNoRoute,
       "mscMcsMgrDprsMcsEpGEpLCoLastTearDownReason": mscMcsMgrDprsMcsEpGEpLCoLastTearDownReason,
       "mscMcsMgrDprsMcsEpGEpLCoPathFailureAction": mscMcsMgrDprsMcsEpGEpLCoPathFailureAction,
       "mscMcsMgrDprsMcsEpGEpLCoBumpPreference": mscMcsMgrDprsMcsEpGEpLCoBumpPreference,
       "mscMcsMgrDprsMcsEpGEpLCoOptimization": mscMcsMgrDprsMcsEpGEpLCoOptimization,
       "mscMcsMgrDprsMcsEpGEpLCoPathUpDateTime": mscMcsMgrDprsMcsEpGEpLCoPathUpDateTime,
       "mscMcsMgrDprsMcsEpGEpLCoStatsTable": mscMcsMgrDprsMcsEpGEpLCoStatsTable,
       "mscMcsMgrDprsMcsEpGEpLCoStatsEntry": mscMcsMgrDprsMcsEpGEpLCoStatsEntry,
       "mscMcsMgrDprsMcsEpGEpLCoPktsToNetwork": mscMcsMgrDprsMcsEpGEpLCoPktsToNetwork,
       "mscMcsMgrDprsMcsEpGEpLCoBytesToNetwork": mscMcsMgrDprsMcsEpGEpLCoBytesToNetwork,
       "mscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork": mscMcsMgrDprsMcsEpGEpLCoPktsFromNetwork,
       "mscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork": mscMcsMgrDprsMcsEpGEpLCoBytesFromNetwork,
       "mscMcsMgrDprsMcsEpGEpLCoPathTable": mscMcsMgrDprsMcsEpGEpLCoPathTable,
       "mscMcsMgrDprsMcsEpGEpLCoPathEntry": mscMcsMgrDprsMcsEpGEpLCoPathEntry,
       "mscMcsMgrDprsMcsEpGEpLCoPathValue": mscMcsMgrDprsMcsEpGEpLCoPathValue,
       "mscMcsMgrDprsMcsEpGEpCac": mscMcsMgrDprsMcsEpGEpCac,
       "mscMcsMgrDprsMcsEpGEpCacRowStatusTable": mscMcsMgrDprsMcsEpGEpCacRowStatusTable,
       "mscMcsMgrDprsMcsEpGEpCacRowStatusEntry": mscMcsMgrDprsMcsEpGEpCacRowStatusEntry,
       "mscMcsMgrDprsMcsEpGEpCacRowStatus": mscMcsMgrDprsMcsEpGEpCacRowStatus,
       "mscMcsMgrDprsMcsEpGEpCacComponentName": mscMcsMgrDprsMcsEpGEpCacComponentName,
       "mscMcsMgrDprsMcsEpGEpCacStorageType": mscMcsMgrDprsMcsEpGEpCacStorageType,
       "mscMcsMgrDprsMcsEpGEpCacIndex": mscMcsMgrDprsMcsEpGEpCacIndex,
       "mscMcsMgrDprsMcsEpGEpCacCacd": mscMcsMgrDprsMcsEpGEpCacCacd,
       "mscMcsMgrDprsMcsEpGEpCacCacdRowStatusTable": mscMcsMgrDprsMcsEpGEpCacCacdRowStatusTable,
       "mscMcsMgrDprsMcsEpGEpCacCacdRowStatusEntry": mscMcsMgrDprsMcsEpGEpCacCacdRowStatusEntry,
       "mscMcsMgrDprsMcsEpGEpCacCacdRowStatus": mscMcsMgrDprsMcsEpGEpCacCacdRowStatus,
       "mscMcsMgrDprsMcsEpGEpCacCacdComponentName": mscMcsMgrDprsMcsEpGEpCacCacdComponentName,
       "mscMcsMgrDprsMcsEpGEpCacCacdStorageType": mscMcsMgrDprsMcsEpGEpCacCacdStorageType,
       "mscMcsMgrDprsMcsEpGEpCacCacdIndex": mscMcsMgrDprsMcsEpGEpCacCacdIndex,
       "mscMcsMgrDprsMcsEpGEpCacCacdFrwdTable": mscMcsMgrDprsMcsEpGEpCacCacdFrwdTable,
       "mscMcsMgrDprsMcsEpGEpCacCacdFrwdEntry": mscMcsMgrDprsMcsEpGEpCacCacdFrwdEntry,
       "mscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy": mscMcsMgrDprsMcsEpGEpCacCacdForwardCacPolicy,
       "mscMcsMgrDprsMcsEpGEpCacCacdForwardCacType": mscMcsMgrDprsMcsEpGEpCacCacdForwardCacType,
       "mscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor": mscMcsMgrDprsMcsEpGEpCacCacdForwardOversubFactor,
       "mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw": mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumSvcBw,
       "mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw": mscMcsMgrDprsMcsEpGEpCacCacdForwardMaximumPvcBw,
       "mscMcsMgrDprsMcsEpGEpCacCacdRvrsTable": mscMcsMgrDprsMcsEpGEpCacCacdRvrsTable,
       "mscMcsMgrDprsMcsEpGEpCacCacdRvrsEntry": mscMcsMgrDprsMcsEpGEpCacCacdRvrsEntry,
       "mscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy": mscMcsMgrDprsMcsEpGEpCacCacdReverseCacPolicy,
       "mscMcsMgrDprsMcsEpGEpCacCacdReverseCacType": mscMcsMgrDprsMcsEpGEpCacCacdReverseCacType,
       "mscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub": mscMcsMgrDprsMcsEpGEpCacCacdReverseCacOverSub,
       "mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw": mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxSvcBw,
       "mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw": mscMcsMgrDprsMcsEpGEpCacCacdReverseMaxPvcBw,
       "mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshTable": mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshTable,
       "mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshEntry": mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshEntry,
       "mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex": mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshIndex,
       "mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue": mscMcsMgrDprsMcsEpGEpCacCacdFAlarmThreshValue,
       "mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshTable": mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshTable,
       "mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshEntry": mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshEntry,
       "mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex": mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshIndex,
       "mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue": mscMcsMgrDprsMcsEpGEpCacCacdRAlarmThreshValue,
       "mscMcsMgrDprsMcsEpGEpCacOperTable": mscMcsMgrDprsMcsEpGEpCacOperTable,
       "mscMcsMgrDprsMcsEpGEpCacOperEntry": mscMcsMgrDprsMcsEpGEpCacOperEntry,
       "mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth": mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidth,
       "mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable": mscMcsMgrDprsMcsEpGEpCacEffectiveBandwidthAvailable,
       "mscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive": mscMcsMgrDprsMcsEpGEpCacNumberOfCallsActive,
       "mscMcsMgrDprsMcsEpGEpCacCacPolicy": mscMcsMgrDprsMcsEpGEpCacCacPolicy,
       "mscMcsMgrDprsMcsEpGEpCacCacType": mscMcsMgrDprsMcsEpGEpCacCacType,
       "mscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth": mscMcsMgrDprsMcsEpGEpCacMaximumSvcBandwidth,
       "mscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth": mscMcsMgrDprsMcsEpGEpCacMaximumPvcBandwidth,
       "mscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures": mscMcsMgrDprsMcsEpGEpCacNumberOfCacFailures,
       "mscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci": mscMcsMgrDprsMcsEpGEpCacLastFailedFrDlci,
       "mscMcsMgrDprsMcsEpGEpCacLastFailedReason": mscMcsMgrDprsMcsEpGEpCacLastFailedReason,
       "mscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor": mscMcsMgrDprsMcsEpGEpCacOverSubscriptionFactor,
       "mscMcsMgrDprsMcsEpGEpCacAlarmThresholdTable": mscMcsMgrDprsMcsEpGEpCacAlarmThresholdTable,
       "mscMcsMgrDprsMcsEpGEpCacAlarmThresholdEntry": mscMcsMgrDprsMcsEpGEpCacAlarmThresholdEntry,
       "mscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex": mscMcsMgrDprsMcsEpGEpCacAlarmThresholdIndex,
       "mscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue": mscMcsMgrDprsMcsEpGEpCacAlarmThresholdValue,
       "mscMcsMgrDprsMcsEpGEpCon": mscMcsMgrDprsMcsEpGEpCon,
       "mscMcsMgrDprsMcsEpGEpConRowStatusTable": mscMcsMgrDprsMcsEpGEpConRowStatusTable,
       "mscMcsMgrDprsMcsEpGEpConRowStatusEntry": mscMcsMgrDprsMcsEpGEpConRowStatusEntry,
       "mscMcsMgrDprsMcsEpGEpConRowStatus": mscMcsMgrDprsMcsEpGEpConRowStatus,
       "mscMcsMgrDprsMcsEpGEpConComponentName": mscMcsMgrDprsMcsEpGEpConComponentName,
       "mscMcsMgrDprsMcsEpGEpConStorageType": mscMcsMgrDprsMcsEpGEpConStorageType,
       "mscMcsMgrDprsMcsEpGEpConIndex": mscMcsMgrDprsMcsEpGEpConIndex,
       "mscMcsMgrDprsMcsEpGEpConOperTable": mscMcsMgrDprsMcsEpGEpConOperTable,
       "mscMcsMgrDprsMcsEpGEpConOperEntry": mscMcsMgrDprsMcsEpGEpConOperEntry,
       "mscMcsMgrDprsMcsEpGEpConFrameRelayDlci": mscMcsMgrDprsMcsEpGEpConFrameRelayDlci,
       "mscMcsMgrDprsMcsEpGEpConReservedBandwidth": mscMcsMgrDprsMcsEpGEpConReservedBandwidth,
       "mscMcsMgrDprsMcsEpGEpStateTable": mscMcsMgrDprsMcsEpGEpStateTable,
       "mscMcsMgrDprsMcsEpGEpStateEntry": mscMcsMgrDprsMcsEpGEpStateEntry,
       "mscMcsMgrDprsMcsEpGEpAdminState": mscMcsMgrDprsMcsEpGEpAdminState,
       "mscMcsMgrDprsMcsEpGEpOperationalState": mscMcsMgrDprsMcsEpGEpOperationalState,
       "mscMcsMgrDprsMcsEpGEpUsageState": mscMcsMgrDprsMcsEpGEpUsageState,
       "mscMcsMgrDprsMcsEpGEpAvailabilityStatus": mscMcsMgrDprsMcsEpGEpAvailabilityStatus,
       "mscMcsMgrDprsMcsEpGEpProceduralStatus": mscMcsMgrDprsMcsEpGEpProceduralStatus,
       "mscMcsMgrDprsMcsEpGEpControlStatus": mscMcsMgrDprsMcsEpGEpControlStatus,
       "mscMcsMgrDprsMcsEpGEpAlarmStatus": mscMcsMgrDprsMcsEpGEpAlarmStatus,
       "mscMcsMgrDprsMcsEpGEpStandbyStatus": mscMcsMgrDprsMcsEpGEpStandbyStatus,
       "mscMcsMgrDprsMcsEpGEpUnknownStatus": mscMcsMgrDprsMcsEpGEpUnknownStatus,
       "mscMcsMgrDprsMcsEpGEpOperTable": mscMcsMgrDprsMcsEpGEpOperTable,
       "mscMcsMgrDprsMcsEpGEpOperEntry": mscMcsMgrDprsMcsEpGEpOperEntry,
       "mscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause": mscMcsMgrDprsMcsEpGEpLastTransportConnectionClearCause,
       "mscMcsMgrDprsMcsEpGEpType": mscMcsMgrDprsMcsEpGEpType,
       "mscMcsMgrDprsMcsEpGEpSupportedTransferPriorities": mscMcsMgrDprsMcsEpGEpSupportedTransferPriorities,
       "mscMcsMgrDprsMcsEpGEpConnectionTransferPriority": mscMcsMgrDprsMcsEpGEpConnectionTransferPriority,
       "mscMcsMgrDprsMcsEpGEpServiceCategory": mscMcsMgrDprsMcsEpGEpServiceCategory,
       "mscMcsMgrDprsMcsEpGEpBandwidth": mscMcsMgrDprsMcsEpGEpBandwidth,
       "mscMcsMgrDprsMcsEpGEpRemoteComponentName": mscMcsMgrDprsMcsEpGEpRemoteComponentName,
       "mscMcsMgrDprsMcsEpGEpRemoteRoutingId": mscMcsMgrDprsMcsEpGEpRemoteRoutingId,
       "mscMcsMgrDprsMcsEpGEpRemoteModuleId": mscMcsMgrDprsMcsEpGEpRemoteModuleId,
       "mscMcsMgrDprsMcsEpGEpLastTrConnDiagCode": mscMcsMgrDprsMcsEpGEpLastTrConnDiagCode,
       "mscMcsMgrDprsMcsEpGEpForwardBandwith": mscMcsMgrDprsMcsEpGEpForwardBandwith,
       "mscMcsMgrDprsMcsEpGEpReverseBandwidth": mscMcsMgrDprsMcsEpGEpReverseBandwidth,
       "mscMcsMgrDprsMcsEpGEpStatsTable": mscMcsMgrDprsMcsEpGEpStatsTable,
       "mscMcsMgrDprsMcsEpGEpStatsEntry": mscMcsMgrDprsMcsEpGEpStatsEntry,
       "mscMcsMgrDprsMcsEpGEpSetupAttempts": mscMcsMgrDprsMcsEpGEpSetupAttempts,
       "mscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs": mscMcsMgrDprsMcsEpGEpPktDiscErroredFromMcs,
       "mscMcsMgrDprsMcsEpGEpPktFromMcsTable": mscMcsMgrDprsMcsEpGEpPktFromMcsTable,
       "mscMcsMgrDprsMcsEpGEpPktFromMcsEntry": mscMcsMgrDprsMcsEpGEpPktFromMcsEntry,
       "mscMcsMgrDprsMcsEpGEpPktFromMcsIndex": mscMcsMgrDprsMcsEpGEpPktFromMcsIndex,
       "mscMcsMgrDprsMcsEpGEpPktFromMcsValue": mscMcsMgrDprsMcsEpGEpPktFromMcsValue,
       "mscMcsMgrDprsMcsEpGEpOctetsFromMcsTable": mscMcsMgrDprsMcsEpGEpOctetsFromMcsTable,
       "mscMcsMgrDprsMcsEpGEpOctetsFromMcsEntry": mscMcsMgrDprsMcsEpGEpOctetsFromMcsEntry,
       "mscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex": mscMcsMgrDprsMcsEpGEpOctetsFromMcsIndex,
       "mscMcsMgrDprsMcsEpGEpOctetsFromMcsValue": mscMcsMgrDprsMcsEpGEpOctetsFromMcsValue,
       "mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable": mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable,
       "mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry": mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry,
       "mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex": mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex,
       "mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue": mscMcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue,
       "mscMcsMgrDprsMcsEpGOperTable": mscMcsMgrDprsMcsEpGOperTable,
       "mscMcsMgrDprsMcsEpGOperEntry": mscMcsMgrDprsMcsEpGOperEntry,
       "mscMcsMgrDprsMcsEpGRemoteAddress": mscMcsMgrDprsMcsEpGRemoteAddress,
       "mscMcsMgrDprsMcsEpGAssociatedEpGroupName": mscMcsMgrDprsMcsEpGAssociatedEpGroupName,
       "dprsMcsEpMIB": dprsMcsEpMIB,
       "dprsMcsEpGroup": dprsMcsEpGroup,
       "dprsMcsEpGroupCA": dprsMcsEpGroupCA,
       "dprsMcsEpGroupCA02": dprsMcsEpGroupCA02,
       "dprsMcsEpGroupCA02A": dprsMcsEpGroupCA02A,
       "dprsMcsEpCapabilities": dprsMcsEpCapabilities,
       "dprsMcsEpCapabilitiesCA": dprsMcsEpCapabilitiesCA,
       "dprsMcsEpCapabilitiesCA02": dprsMcsEpCapabilitiesCA02,
       "dprsMcsEpCapabilitiesCA02A": dprsMcsEpCapabilitiesCA02A}
)
