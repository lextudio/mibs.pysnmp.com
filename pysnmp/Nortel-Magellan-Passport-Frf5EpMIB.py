# SNMP MIB module (Nortel-Magellan-Passport-Frf5EpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-Frf5EpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:51 2024
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

(mcsMgr,
 mcsMgrIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-McsMgrMIB",
    "mcsMgr",
    "mcsMgrIndex")

(Counter32,
 DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "HexString",
    "IntegerSequence",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
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

_McsMgrFrf5EpG_ObjectIdentity = ObjectIdentity
mcsMgrFrf5EpG = _McsMgrFrf5EpG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14)
)
_McsMgrFrf5EpGRowStatusTable_Object = MibTable
mcsMgrFrf5EpGRowStatusTable = _McsMgrFrf5EpGRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 1)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGRowStatusTable.setStatus("mandatory")
_McsMgrFrf5EpGRowStatusEntry_Object = MibTableRow
mcsMgrFrf5EpGRowStatusEntry = _McsMgrFrf5EpGRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 1, 1)
)
mcsMgrFrf5EpGRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGRowStatusEntry.setStatus("mandatory")
_McsMgrFrf5EpGRowStatus_Type = RowStatus
_McsMgrFrf5EpGRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGRowStatus = _McsMgrFrf5EpGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 1, 1, 1),
    _McsMgrFrf5EpGRowStatus_Type()
)
mcsMgrFrf5EpGRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGComponentName_Type = DisplayString
_McsMgrFrf5EpGComponentName_Object = MibTableColumn
mcsMgrFrf5EpGComponentName = _McsMgrFrf5EpGComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 1, 1, 2),
    _McsMgrFrf5EpGComponentName_Type()
)
mcsMgrFrf5EpGComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGComponentName.setStatus("mandatory")
_McsMgrFrf5EpGStorageType_Type = StorageType
_McsMgrFrf5EpGStorageType_Object = MibTableColumn
mcsMgrFrf5EpGStorageType = _McsMgrFrf5EpGStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 1, 1, 4),
    _McsMgrFrf5EpGStorageType_Type()
)
mcsMgrFrf5EpGStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGStorageType.setStatus("mandatory")


class _McsMgrFrf5EpGIndex_Type(Integer32):
    """Custom type mcsMgrFrf5EpGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_McsMgrFrf5EpGIndex_Type.__name__ = "Integer32"
_McsMgrFrf5EpGIndex_Object = MibTableColumn
mcsMgrFrf5EpGIndex = _McsMgrFrf5EpGIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 1, 1, 10),
    _McsMgrFrf5EpGIndex_Type()
)
mcsMgrFrf5EpGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGIndex.setStatus("mandatory")
_McsMgrFrf5EpGAddr_ObjectIdentity = ObjectIdentity
mcsMgrFrf5EpGAddr = _McsMgrFrf5EpGAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2)
)
_McsMgrFrf5EpGAddrRowStatusTable_Object = MibTable
mcsMgrFrf5EpGAddrRowStatusTable = _McsMgrFrf5EpGAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 1)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrRowStatusTable.setStatus("mandatory")
_McsMgrFrf5EpGAddrRowStatusEntry_Object = MibTableRow
mcsMgrFrf5EpGAddrRowStatusEntry = _McsMgrFrf5EpGAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 1, 1)
)
mcsMgrFrf5EpGAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrRowStatusEntry.setStatus("mandatory")
_McsMgrFrf5EpGAddrRowStatus_Type = RowStatus
_McsMgrFrf5EpGAddrRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGAddrRowStatus = _McsMgrFrf5EpGAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 1, 1, 1),
    _McsMgrFrf5EpGAddrRowStatus_Type()
)
mcsMgrFrf5EpGAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGAddrComponentName_Type = DisplayString
_McsMgrFrf5EpGAddrComponentName_Object = MibTableColumn
mcsMgrFrf5EpGAddrComponentName = _McsMgrFrf5EpGAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 1, 1, 2),
    _McsMgrFrf5EpGAddrComponentName_Type()
)
mcsMgrFrf5EpGAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrComponentName.setStatus("mandatory")
_McsMgrFrf5EpGAddrStorageType_Type = StorageType
_McsMgrFrf5EpGAddrStorageType_Object = MibTableColumn
mcsMgrFrf5EpGAddrStorageType = _McsMgrFrf5EpGAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 1, 1, 4),
    _McsMgrFrf5EpGAddrStorageType_Type()
)
mcsMgrFrf5EpGAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrStorageType.setStatus("mandatory")
_McsMgrFrf5EpGAddrIndex_Type = NonReplicated
_McsMgrFrf5EpGAddrIndex_Object = MibTableColumn
mcsMgrFrf5EpGAddrIndex = _McsMgrFrf5EpGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 1, 1, 10),
    _McsMgrFrf5EpGAddrIndex_Type()
)
mcsMgrFrf5EpGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrIndex.setStatus("mandatory")
_McsMgrFrf5EpGAddrProvTable_Object = MibTable
mcsMgrFrf5EpGAddrProvTable = _McsMgrFrf5EpGAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 10)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrProvTable.setStatus("mandatory")
_McsMgrFrf5EpGAddrProvEntry_Object = MibTableRow
mcsMgrFrf5EpGAddrProvEntry = _McsMgrFrf5EpGAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 10, 1)
)
mcsMgrFrf5EpGAddrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrProvEntry.setStatus("mandatory")


class _McsMgrFrf5EpGAddrRemoteAddress_Type(AsciiString):
    """Custom type mcsMgrFrf5EpGAddrRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_McsMgrFrf5EpGAddrRemoteAddress_Type.__name__ = "AsciiString"
_McsMgrFrf5EpGAddrRemoteAddress_Object = MibTableColumn
mcsMgrFrf5EpGAddrRemoteAddress = _McsMgrFrf5EpGAddrRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 10, 1, 1),
    _McsMgrFrf5EpGAddrRemoteAddress_Type()
)
mcsMgrFrf5EpGAddrRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrRemoteAddress.setStatus("mandatory")


class _McsMgrFrf5EpGAddrCommentText_Type(AsciiString):
    """Custom type mcsMgrFrf5EpGAddrCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 750),
    )


_McsMgrFrf5EpGAddrCommentText_Type.__name__ = "AsciiString"
_McsMgrFrf5EpGAddrCommentText_Object = MibTableColumn
mcsMgrFrf5EpGAddrCommentText = _McsMgrFrf5EpGAddrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 10, 1, 2),
    _McsMgrFrf5EpGAddrCommentText_Type()
)
mcsMgrFrf5EpGAddrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrCommentText.setStatus("mandatory")
_McsMgrFrf5EpGAddrAddrPreTable_Object = MibTable
mcsMgrFrf5EpGAddrAddrPreTable = _McsMgrFrf5EpGAddrAddrPreTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 362)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrAddrPreTable.setStatus("mandatory")
_McsMgrFrf5EpGAddrAddrPreEntry_Object = MibTableRow
mcsMgrFrf5EpGAddrAddrPreEntry = _McsMgrFrf5EpGAddrAddrPreEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 362, 1)
)
mcsMgrFrf5EpGAddrAddrPreEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGAddrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGAddrAddrPreValue"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrAddrPreEntry.setStatus("mandatory")


class _McsMgrFrf5EpGAddrAddrPreValue_Type(AsciiString):
    """Custom type mcsMgrFrf5EpGAddrAddrPreValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_McsMgrFrf5EpGAddrAddrPreValue_Type.__name__ = "AsciiString"
_McsMgrFrf5EpGAddrAddrPreValue_Object = MibTableColumn
mcsMgrFrf5EpGAddrAddrPreValue = _McsMgrFrf5EpGAddrAddrPreValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 362, 1, 1),
    _McsMgrFrf5EpGAddrAddrPreValue_Type()
)
mcsMgrFrf5EpGAddrAddrPreValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrAddrPreValue.setStatus("mandatory")
_McsMgrFrf5EpGAddrAddrPreRowStatus_Type = RowStatus
_McsMgrFrf5EpGAddrAddrPreRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGAddrAddrPreRowStatus = _McsMgrFrf5EpGAddrAddrPreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 2, 362, 1, 2),
    _McsMgrFrf5EpGAddrAddrPreRowStatus_Type()
)
mcsMgrFrf5EpGAddrAddrPreRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGAddrAddrPreRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGEp_ObjectIdentity = ObjectIdentity
mcsMgrFrf5EpGEp = _McsMgrFrf5EpGEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3)
)
_McsMgrFrf5EpGEpRowStatusTable_Object = MibTable
mcsMgrFrf5EpGEpRowStatusTable = _McsMgrFrf5EpGEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 1)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpRowStatusTable.setStatus("mandatory")
_McsMgrFrf5EpGEpRowStatusEntry_Object = MibTableRow
mcsMgrFrf5EpGEpRowStatusEntry = _McsMgrFrf5EpGEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 1, 1)
)
mcsMgrFrf5EpGEpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpRowStatusEntry.setStatus("mandatory")
_McsMgrFrf5EpGEpRowStatus_Type = RowStatus
_McsMgrFrf5EpGEpRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpRowStatus = _McsMgrFrf5EpGEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 1, 1, 1),
    _McsMgrFrf5EpGEpRowStatus_Type()
)
mcsMgrFrf5EpGEpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGEpComponentName_Type = DisplayString
_McsMgrFrf5EpGEpComponentName_Object = MibTableColumn
mcsMgrFrf5EpGEpComponentName = _McsMgrFrf5EpGEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 1, 1, 2),
    _McsMgrFrf5EpGEpComponentName_Type()
)
mcsMgrFrf5EpGEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpComponentName.setStatus("mandatory")
_McsMgrFrf5EpGEpStorageType_Type = StorageType
_McsMgrFrf5EpGEpStorageType_Object = MibTableColumn
mcsMgrFrf5EpGEpStorageType = _McsMgrFrf5EpGEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 1, 1, 4),
    _McsMgrFrf5EpGEpStorageType_Type()
)
mcsMgrFrf5EpGEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpStorageType.setStatus("mandatory")


class _McsMgrFrf5EpGEpIndex_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McsMgrFrf5EpGEpIndex_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpIndex_Object = MibTableColumn
mcsMgrFrf5EpGEpIndex = _McsMgrFrf5EpGEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 1, 1, 10),
    _McsMgrFrf5EpGEpIndex_Type()
)
mcsMgrFrf5EpGEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpIndex.setStatus("mandatory")
_McsMgrFrf5EpGEpLmi_ObjectIdentity = ObjectIdentity
mcsMgrFrf5EpGEpLmi = _McsMgrFrf5EpGEpLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2)
)
_McsMgrFrf5EpGEpLmiRowStatusTable_Object = MibTable
mcsMgrFrf5EpGEpLmiRowStatusTable = _McsMgrFrf5EpGEpLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiRowStatusTable.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiRowStatusEntry_Object = MibTableRow
mcsMgrFrf5EpGEpLmiRowStatusEntry = _McsMgrFrf5EpGEpLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 1, 1)
)
mcsMgrFrf5EpGEpLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiRowStatusEntry.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiRowStatus_Type = RowStatus
_McsMgrFrf5EpGEpLmiRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiRowStatus = _McsMgrFrf5EpGEpLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 1, 1, 1),
    _McsMgrFrf5EpGEpLmiRowStatus_Type()
)
mcsMgrFrf5EpGEpLmiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiComponentName_Type = DisplayString
_McsMgrFrf5EpGEpLmiComponentName_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiComponentName = _McsMgrFrf5EpGEpLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 1, 1, 2),
    _McsMgrFrf5EpGEpLmiComponentName_Type()
)
mcsMgrFrf5EpGEpLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiComponentName.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiStorageType_Type = StorageType
_McsMgrFrf5EpGEpLmiStorageType_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiStorageType = _McsMgrFrf5EpGEpLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 1, 1, 4),
    _McsMgrFrf5EpGEpLmiStorageType_Type()
)
mcsMgrFrf5EpGEpLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiStorageType.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiIndex_Type = NonReplicated
_McsMgrFrf5EpGEpLmiIndex_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiIndex = _McsMgrFrf5EpGEpLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 1, 1, 10),
    _McsMgrFrf5EpGEpLmiIndex_Type()
)
mcsMgrFrf5EpGEpLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiIndex.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiParmsTable_Object = MibTable
mcsMgrFrf5EpGEpLmiParmsTable = _McsMgrFrf5EpGEpLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiParmsTable.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiParmsEntry_Object = MibTableRow
mcsMgrFrf5EpGEpLmiParmsEntry = _McsMgrFrf5EpGEpLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10, 1)
)
mcsMgrFrf5EpGEpLmiParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiParmsEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiProcedures_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpLmiProcedures based on Integer32"""
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


_McsMgrFrf5EpGEpLmiProcedures_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpLmiProcedures_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiProcedures = _McsMgrFrf5EpGEpLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10, 1, 1),
    _McsMgrFrf5EpGEpLmiProcedures_Type()
)
mcsMgrFrf5EpGEpLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiProcedures.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiAsyncStatusReport_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpLmiAsyncStatusReport based on Integer32"""
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


_McsMgrFrf5EpGEpLmiAsyncStatusReport_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpLmiAsyncStatusReport_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiAsyncStatusReport = _McsMgrFrf5EpGEpLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10, 1, 2),
    _McsMgrFrf5EpGEpLmiAsyncStatusReport_Type()
)
mcsMgrFrf5EpGEpLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiAsyncStatusReport.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_McsMgrFrf5EpGEpLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpLmiErrorEventThreshold_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiErrorEventThreshold = _McsMgrFrf5EpGEpLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10, 1, 3),
    _McsMgrFrf5EpGEpLmiErrorEventThreshold_Type()
)
mcsMgrFrf5EpGEpLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiErrorEventThreshold.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiEventCount_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_McsMgrFrf5EpGEpLmiEventCount_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpLmiEventCount_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiEventCount = _McsMgrFrf5EpGEpLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10, 1, 4),
    _McsMgrFrf5EpGEpLmiEventCount_Type()
)
mcsMgrFrf5EpGEpLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiEventCount.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiCheckPointTimer_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpLmiCheckPointTimer based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_McsMgrFrf5EpGEpLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpLmiCheckPointTimer_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiCheckPointTimer = _McsMgrFrf5EpGEpLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10, 1, 5),
    _McsMgrFrf5EpGEpLmiCheckPointTimer_Type()
)
mcsMgrFrf5EpGEpLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiCheckPointTimer.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiSide_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpLmiSide based on Integer32"""
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


_McsMgrFrf5EpGEpLmiSide_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpLmiSide_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiSide = _McsMgrFrf5EpGEpLmiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 10, 1, 8),
    _McsMgrFrf5EpGEpLmiSide_Type()
)
mcsMgrFrf5EpGEpLmiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiSide.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiNniParmsTable_Object = MibTable
mcsMgrFrf5EpGEpLmiNniParmsTable = _McsMgrFrf5EpGEpLmiNniParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 11)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiNniParmsTable.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiNniParmsEntry_Object = MibTableRow
mcsMgrFrf5EpGEpLmiNniParmsEntry = _McsMgrFrf5EpGEpLmiNniParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 11, 1)
)
mcsMgrFrf5EpGEpLmiNniParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiNniParmsEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McsMgrFrf5EpGEpLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpLmiFullStatusPollingCycles_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiFullStatusPollingCycles = _McsMgrFrf5EpGEpLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 11, 1, 1),
    _McsMgrFrf5EpGEpLmiFullStatusPollingCycles_Type()
)
mcsMgrFrf5EpGEpLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiFullStatusPollingCycles.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpLmiLinkVerificationTimer based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_McsMgrFrf5EpGEpLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpLmiLinkVerificationTimer_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiLinkVerificationTimer = _McsMgrFrf5EpGEpLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 11, 1, 2),
    _McsMgrFrf5EpGEpLmiLinkVerificationTimer_Type()
)
mcsMgrFrf5EpGEpLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiLinkVerificationTimer.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiStateTable_Object = MibTable
mcsMgrFrf5EpGEpLmiStateTable = _McsMgrFrf5EpGEpLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 12)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiStateTable.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiStateEntry_Object = MibTableRow
mcsMgrFrf5EpGEpLmiStateEntry = _McsMgrFrf5EpGEpLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 12, 1)
)
mcsMgrFrf5EpGEpLmiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiStateEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiAdminState_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpLmiAdminState based on Integer32"""
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


_McsMgrFrf5EpGEpLmiAdminState_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpLmiAdminState_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiAdminState = _McsMgrFrf5EpGEpLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 12, 1, 1),
    _McsMgrFrf5EpGEpLmiAdminState_Type()
)
mcsMgrFrf5EpGEpLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiAdminState.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiOperationalState_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpLmiOperationalState based on Integer32"""
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


_McsMgrFrf5EpGEpLmiOperationalState_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpLmiOperationalState_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiOperationalState = _McsMgrFrf5EpGEpLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 12, 1, 2),
    _McsMgrFrf5EpGEpLmiOperationalState_Type()
)
mcsMgrFrf5EpGEpLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiOperationalState.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiUsageState_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpLmiUsageState based on Integer32"""
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


_McsMgrFrf5EpGEpLmiUsageState_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpLmiUsageState_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiUsageState = _McsMgrFrf5EpGEpLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 12, 1, 3),
    _McsMgrFrf5EpGEpLmiUsageState_Type()
)
mcsMgrFrf5EpGEpLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiUsageState.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiPsiTable_Object = MibTable
mcsMgrFrf5EpGEpLmiPsiTable = _McsMgrFrf5EpGEpLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 13)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiPsiTable.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiPsiEntry_Object = MibTableRow
mcsMgrFrf5EpGEpLmiPsiEntry = _McsMgrFrf5EpGEpLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 13, 1)
)
mcsMgrFrf5EpGEpLmiPsiEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiPsiEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiProtocolStatus_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpLmiProtocolStatus based on Integer32"""
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


_McsMgrFrf5EpGEpLmiProtocolStatus_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpLmiProtocolStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiProtocolStatus = _McsMgrFrf5EpGEpLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 13, 1, 1),
    _McsMgrFrf5EpGEpLmiProtocolStatus_Type()
)
mcsMgrFrf5EpGEpLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiProtocolStatus.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiStatsTable_Object = MibTable
mcsMgrFrf5EpGEpLmiStatsTable = _McsMgrFrf5EpGEpLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiStatsTable.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiStatsEntry_Object = MibTableRow
mcsMgrFrf5EpGEpLmiStatsEntry = _McsMgrFrf5EpGEpLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1)
)
mcsMgrFrf5EpGEpLmiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpLmiIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiStatsEntry.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Type = Counter32
_McsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface = _McsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 1),
    _McsMgrFrf5EpGEpLmiKeepAliveStatusToInterface_Type()
)
mcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiFullStatusToInterface_Type = Counter32
_McsMgrFrf5EpGEpLmiFullStatusToInterface_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiFullStatusToInterface = _McsMgrFrf5EpGEpLmiFullStatusToInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 2),
    _McsMgrFrf5EpGEpLmiFullStatusToInterface_Type()
)
mcsMgrFrf5EpGEpLmiFullStatusToInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiFullStatusToInterface.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Type = Counter32
_McsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface = _McsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 3),
    _McsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface_Type()
)
mcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Type = Counter32
_McsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface = _McsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 4),
    _McsMgrFrf5EpGEpLmiFullStatusEnqFromInterface_Type()
)
mcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type mcsMgrFrf5EpGEpLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_McsMgrFrf5EpGEpLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_McsMgrFrf5EpGEpLmiNetworkSideEventHistory_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiNetworkSideEventHistory = _McsMgrFrf5EpGEpLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 5),
    _McsMgrFrf5EpGEpLmiNetworkSideEventHistory_Type()
)
mcsMgrFrf5EpGEpLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiNetworkSideEventHistory.setStatus("mandatory")


class _McsMgrFrf5EpGEpLmiUserSideEventHistory_Type(AsciiString):
    """Custom type mcsMgrFrf5EpGEpLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_McsMgrFrf5EpGEpLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_McsMgrFrf5EpGEpLmiUserSideEventHistory_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiUserSideEventHistory = _McsMgrFrf5EpGEpLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 6),
    _McsMgrFrf5EpGEpLmiUserSideEventHistory_Type()
)
mcsMgrFrf5EpGEpLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiUserSideEventHistory.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiProtocolErrors_Type = Counter32
_McsMgrFrf5EpGEpLmiProtocolErrors_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiProtocolErrors = _McsMgrFrf5EpGEpLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 7),
    _McsMgrFrf5EpGEpLmiProtocolErrors_Type()
)
mcsMgrFrf5EpGEpLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiProtocolErrors.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiUnexpectedIes_Type = Counter32
_McsMgrFrf5EpGEpLmiUnexpectedIes_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiUnexpectedIes = _McsMgrFrf5EpGEpLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 8),
    _McsMgrFrf5EpGEpLmiUnexpectedIes_Type()
)
mcsMgrFrf5EpGEpLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiUnexpectedIes.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiSequenceErrors_Type = Counter32
_McsMgrFrf5EpGEpLmiSequenceErrors_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiSequenceErrors = _McsMgrFrf5EpGEpLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 9),
    _McsMgrFrf5EpGEpLmiSequenceErrors_Type()
)
mcsMgrFrf5EpGEpLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiSequenceErrors.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiStatusSequenceErrors_Type = Counter32
_McsMgrFrf5EpGEpLmiStatusSequenceErrors_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiStatusSequenceErrors = _McsMgrFrf5EpGEpLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 10),
    _McsMgrFrf5EpGEpLmiStatusSequenceErrors_Type()
)
mcsMgrFrf5EpGEpLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiStatusSequenceErrors.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiUnexpectedReports_Type = Counter32
_McsMgrFrf5EpGEpLmiUnexpectedReports_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiUnexpectedReports = _McsMgrFrf5EpGEpLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 11),
    _McsMgrFrf5EpGEpLmiUnexpectedReports_Type()
)
mcsMgrFrf5EpGEpLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiUnexpectedReports.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiPollingVerifTimeouts_Type = Counter32
_McsMgrFrf5EpGEpLmiPollingVerifTimeouts_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiPollingVerifTimeouts = _McsMgrFrf5EpGEpLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 12),
    _McsMgrFrf5EpGEpLmiPollingVerifTimeouts_Type()
)
mcsMgrFrf5EpGEpLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiPollingVerifTimeouts.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiNoStatusReportCount_Type = Counter32
_McsMgrFrf5EpGEpLmiNoStatusReportCount_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiNoStatusReportCount = _McsMgrFrf5EpGEpLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 13),
    _McsMgrFrf5EpGEpLmiNoStatusReportCount_Type()
)
mcsMgrFrf5EpGEpLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiNoStatusReportCount.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Type = Counter32
_McsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiKeepAliveEnqToIf = _McsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 14),
    _McsMgrFrf5EpGEpLmiKeepAliveEnqToIf_Type()
)
mcsMgrFrf5EpGEpLmiKeepAliveEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiKeepAliveEnqToIf.setStatus("mandatory")
_McsMgrFrf5EpGEpLmiFullStatusEnqToIf_Type = Counter32
_McsMgrFrf5EpGEpLmiFullStatusEnqToIf_Object = MibTableColumn
mcsMgrFrf5EpGEpLmiFullStatusEnqToIf = _McsMgrFrf5EpGEpLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 2, 14, 1, 15),
    _McsMgrFrf5EpGEpLmiFullStatusEnqToIf_Type()
)
mcsMgrFrf5EpGEpLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLmiFullStatusEnqToIf.setStatus("mandatory")
_McsMgrFrf5EpGEpEpd_ObjectIdentity = ObjectIdentity
mcsMgrFrf5EpGEpEpd = _McsMgrFrf5EpGEpEpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3)
)
_McsMgrFrf5EpGEpEpdRowStatusTable_Object = MibTable
mcsMgrFrf5EpGEpEpdRowStatusTable = _McsMgrFrf5EpGEpEpdRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdRowStatusTable.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdRowStatusEntry_Object = MibTableRow
mcsMgrFrf5EpGEpEpdRowStatusEntry = _McsMgrFrf5EpGEpEpdRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 1, 1)
)
mcsMgrFrf5EpGEpEpdRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpEpdIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdRowStatusEntry.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdRowStatus_Type = RowStatus
_McsMgrFrf5EpGEpEpdRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdRowStatus = _McsMgrFrf5EpGEpEpdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 1, 1, 1),
    _McsMgrFrf5EpGEpEpdRowStatus_Type()
)
mcsMgrFrf5EpGEpEpdRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdComponentName_Type = DisplayString
_McsMgrFrf5EpGEpEpdComponentName_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdComponentName = _McsMgrFrf5EpGEpEpdComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 1, 1, 2),
    _McsMgrFrf5EpGEpEpdComponentName_Type()
)
mcsMgrFrf5EpGEpEpdComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdComponentName.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdStorageType_Type = StorageType
_McsMgrFrf5EpGEpEpdStorageType_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdStorageType = _McsMgrFrf5EpGEpEpdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 1, 1, 4),
    _McsMgrFrf5EpGEpEpdStorageType_Type()
)
mcsMgrFrf5EpGEpEpdStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdStorageType.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdIndex_Type = NonReplicated
_McsMgrFrf5EpGEpEpdIndex_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdIndex = _McsMgrFrf5EpGEpEpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 1, 1, 10),
    _McsMgrFrf5EpGEpEpdIndex_Type()
)
mcsMgrFrf5EpGEpEpdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdIndex.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdProvTable_Object = MibTable
mcsMgrFrf5EpGEpEpdProvTable = _McsMgrFrf5EpGEpEpdProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdProvTable.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdProvEntry_Object = MibTableRow
mcsMgrFrf5EpGEpEpdProvEntry = _McsMgrFrf5EpGEpEpdProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1)
)
mcsMgrFrf5EpGEpEpdProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpEpdIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdProvEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Type(IntegerSequence):
    """Custom type mcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier based on IntegerSequence"""
    subtypeSpec = IntegerSequence.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 9),
    )


_McsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Type.__name__ = "IntegerSequence"
_McsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier = _McsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 3),
    _McsMgrFrf5EpGEpEpdRemoteConnectionIdentifier_Type()
)
mcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdConnectionTransferPriority_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpEpdConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McsMgrFrf5EpGEpEpdConnectionTransferPriority_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpEpdConnectionTransferPriority_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdConnectionTransferPriority = _McsMgrFrf5EpGEpEpdConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 4),
    _McsMgrFrf5EpGEpEpdConnectionTransferPriority_Type()
)
mcsMgrFrf5EpGEpEpdConnectionTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdConnectionTransferPriority.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdCommittedInformationRate_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpEpdCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_McsMgrFrf5EpGEpEpdCommittedInformationRate_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpEpdCommittedInformationRate_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdCommittedInformationRate = _McsMgrFrf5EpGEpEpdCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 5),
    _McsMgrFrf5EpGEpEpdCommittedInformationRate_Type()
)
mcsMgrFrf5EpGEpEpdCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdCommittedInformationRate.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdExcessInformationRate_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpEpdExcessInformationRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_McsMgrFrf5EpGEpEpdExcessInformationRate_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpEpdExcessInformationRate_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdExcessInformationRate = _McsMgrFrf5EpGEpEpdExcessInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 6),
    _McsMgrFrf5EpGEpEpdExcessInformationRate_Type()
)
mcsMgrFrf5EpGEpEpdExcessInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdExcessInformationRate.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdCommittedBurstSize_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpEpdCommittedBurstSize based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_McsMgrFrf5EpGEpEpdCommittedBurstSize_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpEpdCommittedBurstSize_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdCommittedBurstSize = _McsMgrFrf5EpGEpEpdCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 7),
    _McsMgrFrf5EpGEpEpdCommittedBurstSize_Type()
)
mcsMgrFrf5EpGEpEpdCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdCommittedBurstSize.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdType_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpEpdType based on Integer32"""
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


_McsMgrFrf5EpGEpEpdType_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpEpdType_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdType = _McsMgrFrf5EpGEpEpdType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 8),
    _McsMgrFrf5EpGEpEpdType_Type()
)
mcsMgrFrf5EpGEpEpdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdType.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdAccessRate_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpEpdAccessRate based on Unsigned32"""
    defaultValue = 1536000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_McsMgrFrf5EpGEpEpdAccessRate_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpEpdAccessRate_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdAccessRate = _McsMgrFrf5EpGEpEpdAccessRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 9),
    _McsMgrFrf5EpGEpEpdAccessRate_Type()
)
mcsMgrFrf5EpGEpEpdAccessRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdAccessRate.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdExcessBurstSize_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpEpdExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_McsMgrFrf5EpGEpEpdExcessBurstSize_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpEpdExcessBurstSize_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdExcessBurstSize = _McsMgrFrf5EpGEpEpdExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 10, 1, 10),
    _McsMgrFrf5EpGEpEpdExcessBurstSize_Type()
)
mcsMgrFrf5EpGEpEpdExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdExcessBurstSize.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdCidDataTable_Object = MibTable
mcsMgrFrf5EpGEpEpdCidDataTable = _McsMgrFrf5EpGEpEpdCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 11)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdCidDataTable.setStatus("mandatory")
_McsMgrFrf5EpGEpEpdCidDataEntry_Object = MibTableRow
mcsMgrFrf5EpGEpEpdCidDataEntry = _McsMgrFrf5EpGEpEpdCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 11, 1)
)
mcsMgrFrf5EpGEpEpdCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpEpdIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdCidDataEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpEpdCustomerIdentifier_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpEpdCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_McsMgrFrf5EpGEpEpdCustomerIdentifier_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpEpdCustomerIdentifier_Object = MibTableColumn
mcsMgrFrf5EpGEpEpdCustomerIdentifier = _McsMgrFrf5EpGEpEpdCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 3, 11, 1, 1),
    _McsMgrFrf5EpGEpEpdCustomerIdentifier_Type()
)
mcsMgrFrf5EpGEpEpdCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpEpdCustomerIdentifier.setStatus("mandatory")
_McsMgrFrf5EpGEpDlci_ObjectIdentity = ObjectIdentity
mcsMgrFrf5EpGEpDlci = _McsMgrFrf5EpGEpDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4)
)
_McsMgrFrf5EpGEpDlciRowStatusTable_Object = MibTable
mcsMgrFrf5EpGEpDlciRowStatusTable = _McsMgrFrf5EpGEpDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciRowStatusTable.setStatus("mandatory")
_McsMgrFrf5EpGEpDlciRowStatusEntry_Object = MibTableRow
mcsMgrFrf5EpGEpDlciRowStatusEntry = _McsMgrFrf5EpGEpDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 1, 1)
)
mcsMgrFrf5EpGEpDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpDlciIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciRowStatusEntry.setStatus("mandatory")
_McsMgrFrf5EpGEpDlciRowStatus_Type = RowStatus
_McsMgrFrf5EpGEpDlciRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciRowStatus = _McsMgrFrf5EpGEpDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 1, 1, 1),
    _McsMgrFrf5EpGEpDlciRowStatus_Type()
)
mcsMgrFrf5EpGEpDlciRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGEpDlciComponentName_Type = DisplayString
_McsMgrFrf5EpGEpDlciComponentName_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciComponentName = _McsMgrFrf5EpGEpDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 1, 1, 2),
    _McsMgrFrf5EpGEpDlciComponentName_Type()
)
mcsMgrFrf5EpGEpDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciComponentName.setStatus("mandatory")
_McsMgrFrf5EpGEpDlciStorageType_Type = StorageType
_McsMgrFrf5EpGEpDlciStorageType_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciStorageType = _McsMgrFrf5EpGEpDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 1, 1, 4),
    _McsMgrFrf5EpGEpDlciStorageType_Type()
)
mcsMgrFrf5EpGEpDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciStorageType.setStatus("mandatory")


class _McsMgrFrf5EpGEpDlciIndex_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
        ValueRangeConstraint(1022, 1022),
    )


_McsMgrFrf5EpGEpDlciIndex_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpDlciIndex_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciIndex = _McsMgrFrf5EpGEpDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 1, 1, 10),
    _McsMgrFrf5EpGEpDlciIndex_Type()
)
mcsMgrFrf5EpGEpDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciIndex.setStatus("mandatory")
_McsMgrFrf5EpGEpDlciOperTable_Object = MibTable
mcsMgrFrf5EpGEpDlciOperTable = _McsMgrFrf5EpGEpDlciOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciOperTable.setStatus("mandatory")
_McsMgrFrf5EpGEpDlciOperEntry_Object = MibTableRow
mcsMgrFrf5EpGEpDlciOperEntry = _McsMgrFrf5EpGEpDlciOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 10, 1)
)
mcsMgrFrf5EpGEpDlciOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpDlciIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciOperEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpDlciABitStatusToIf_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpDlciABitStatusToIf based on Integer32"""
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


_McsMgrFrf5EpGEpDlciABitStatusToIf_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpDlciABitStatusToIf_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciABitStatusToIf = _McsMgrFrf5EpGEpDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 10, 1, 1),
    _McsMgrFrf5EpGEpDlciABitStatusToIf_Type()
)
mcsMgrFrf5EpGEpDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciABitStatusToIf.setStatus("mandatory")


class _McsMgrFrf5EpGEpDlciABitReasonToIf_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpDlciABitReasonToIf based on Integer32"""
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


_McsMgrFrf5EpGEpDlciABitReasonToIf_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpDlciABitReasonToIf_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciABitReasonToIf = _McsMgrFrf5EpGEpDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 10, 1, 2),
    _McsMgrFrf5EpGEpDlciABitReasonToIf_Type()
)
mcsMgrFrf5EpGEpDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciABitReasonToIf.setStatus("mandatory")


class _McsMgrFrf5EpGEpDlciABitStatusFromIf_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpDlciABitStatusFromIf based on Integer32"""
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


_McsMgrFrf5EpGEpDlciABitStatusFromIf_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpDlciABitStatusFromIf_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciABitStatusFromIf = _McsMgrFrf5EpGEpDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 10, 1, 3),
    _McsMgrFrf5EpGEpDlciABitStatusFromIf_Type()
)
mcsMgrFrf5EpGEpDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciABitStatusFromIf.setStatus("mandatory")


class _McsMgrFrf5EpGEpDlciABitReasonFromIf_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpDlciABitReasonFromIf based on Integer32"""
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


_McsMgrFrf5EpGEpDlciABitReasonFromIf_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpDlciABitReasonFromIf_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciABitReasonFromIf = _McsMgrFrf5EpGEpDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 10, 1, 4),
    _McsMgrFrf5EpGEpDlciABitReasonFromIf_Type()
)
mcsMgrFrf5EpGEpDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciABitReasonFromIf.setStatus("mandatory")


class _McsMgrFrf5EpGEpDlciAccessConnectionComponent_Type(AsciiString):
    """Custom type mcsMgrFrf5EpGEpDlciAccessConnectionComponent based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_McsMgrFrf5EpGEpDlciAccessConnectionComponent_Type.__name__ = "AsciiString"
_McsMgrFrf5EpGEpDlciAccessConnectionComponent_Object = MibTableColumn
mcsMgrFrf5EpGEpDlciAccessConnectionComponent = _McsMgrFrf5EpGEpDlciAccessConnectionComponent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 4, 10, 1, 5),
    _McsMgrFrf5EpGEpDlciAccessConnectionComponent_Type()
)
mcsMgrFrf5EpGEpDlciAccessConnectionComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpDlciAccessConnectionComponent.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmCon_ObjectIdentity = ObjectIdentity
mcsMgrFrf5EpGEpAtmCon = _McsMgrFrf5EpGEpAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5)
)
_McsMgrFrf5EpGEpAtmConRowStatusTable_Object = MibTable
mcsMgrFrf5EpGEpAtmConRowStatusTable = _McsMgrFrf5EpGEpAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 1)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConRowStatusTable.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConRowStatusEntry_Object = MibTableRow
mcsMgrFrf5EpGEpAtmConRowStatusEntry = _McsMgrFrf5EpGEpAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 1, 1)
)
mcsMgrFrf5EpGEpAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConRowStatusEntry.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConRowStatus_Type = RowStatus
_McsMgrFrf5EpGEpAtmConRowStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpAtmConRowStatus = _McsMgrFrf5EpGEpAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 1, 1, 1),
    _McsMgrFrf5EpGEpAtmConRowStatus_Type()
)
mcsMgrFrf5EpGEpAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConRowStatus.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConComponentName_Type = DisplayString
_McsMgrFrf5EpGEpAtmConComponentName_Object = MibTableColumn
mcsMgrFrf5EpGEpAtmConComponentName = _McsMgrFrf5EpGEpAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 1, 1, 2),
    _McsMgrFrf5EpGEpAtmConComponentName_Type()
)
mcsMgrFrf5EpGEpAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConComponentName.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConStorageType_Type = StorageType
_McsMgrFrf5EpGEpAtmConStorageType_Object = MibTableColumn
mcsMgrFrf5EpGEpAtmConStorageType = _McsMgrFrf5EpGEpAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 1, 1, 4),
    _McsMgrFrf5EpGEpAtmConStorageType_Type()
)
mcsMgrFrf5EpGEpAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConStorageType.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConIndex_Type = NonReplicated
_McsMgrFrf5EpGEpAtmConIndex_Object = MibTableColumn
mcsMgrFrf5EpGEpAtmConIndex = _McsMgrFrf5EpGEpAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 1, 1, 10),
    _McsMgrFrf5EpGEpAtmConIndex_Type()
)
mcsMgrFrf5EpGEpAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConIndex.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConOperTable_Object = MibTable
mcsMgrFrf5EpGEpAtmConOperTable = _McsMgrFrf5EpGEpAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConOperTable.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConOperEntry_Object = MibTableRow
mcsMgrFrf5EpGEpAtmConOperEntry = _McsMgrFrf5EpGEpAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 10, 1)
)
mcsMgrFrf5EpGEpAtmConOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConOperEntry.setStatus("mandatory")
_McsMgrFrf5EpGEpAtmConNextHop_Type = RowPointer
_McsMgrFrf5EpGEpAtmConNextHop_Object = MibTableColumn
mcsMgrFrf5EpGEpAtmConNextHop = _McsMgrFrf5EpGEpAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 5, 10, 1, 1),
    _McsMgrFrf5EpGEpAtmConNextHop_Type()
)
mcsMgrFrf5EpGEpAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAtmConNextHop.setStatus("mandatory")
_McsMgrFrf5EpGEpStateTable_Object = MibTable
mcsMgrFrf5EpGEpStateTable = _McsMgrFrf5EpGEpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpStateTable.setStatus("mandatory")
_McsMgrFrf5EpGEpStateEntry_Object = MibTableRow
mcsMgrFrf5EpGEpStateEntry = _McsMgrFrf5EpGEpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1)
)
mcsMgrFrf5EpGEpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpStateEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpAdminState_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpAdminState based on Integer32"""
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


_McsMgrFrf5EpGEpAdminState_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpAdminState_Object = MibTableColumn
mcsMgrFrf5EpGEpAdminState = _McsMgrFrf5EpGEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 1),
    _McsMgrFrf5EpGEpAdminState_Type()
)
mcsMgrFrf5EpGEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAdminState.setStatus("mandatory")


class _McsMgrFrf5EpGEpOperationalState_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpOperationalState based on Integer32"""
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


_McsMgrFrf5EpGEpOperationalState_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpOperationalState_Object = MibTableColumn
mcsMgrFrf5EpGEpOperationalState = _McsMgrFrf5EpGEpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 2),
    _McsMgrFrf5EpGEpOperationalState_Type()
)
mcsMgrFrf5EpGEpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpOperationalState.setStatus("mandatory")


class _McsMgrFrf5EpGEpUsageState_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpUsageState based on Integer32"""
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


_McsMgrFrf5EpGEpUsageState_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpUsageState_Object = MibTableColumn
mcsMgrFrf5EpGEpUsageState = _McsMgrFrf5EpGEpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 3),
    _McsMgrFrf5EpGEpUsageState_Type()
)
mcsMgrFrf5EpGEpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpUsageState.setStatus("mandatory")


class _McsMgrFrf5EpGEpAvailabilityStatus_Type(OctetString):
    """Custom type mcsMgrFrf5EpGEpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_McsMgrFrf5EpGEpAvailabilityStatus_Type.__name__ = "OctetString"
_McsMgrFrf5EpGEpAvailabilityStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpAvailabilityStatus = _McsMgrFrf5EpGEpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 4),
    _McsMgrFrf5EpGEpAvailabilityStatus_Type()
)
mcsMgrFrf5EpGEpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAvailabilityStatus.setStatus("mandatory")


class _McsMgrFrf5EpGEpProceduralStatus_Type(OctetString):
    """Custom type mcsMgrFrf5EpGEpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrFrf5EpGEpProceduralStatus_Type.__name__ = "OctetString"
_McsMgrFrf5EpGEpProceduralStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpProceduralStatus = _McsMgrFrf5EpGEpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 5),
    _McsMgrFrf5EpGEpProceduralStatus_Type()
)
mcsMgrFrf5EpGEpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpProceduralStatus.setStatus("mandatory")


class _McsMgrFrf5EpGEpControlStatus_Type(OctetString):
    """Custom type mcsMgrFrf5EpGEpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrFrf5EpGEpControlStatus_Type.__name__ = "OctetString"
_McsMgrFrf5EpGEpControlStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpControlStatus = _McsMgrFrf5EpGEpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 6),
    _McsMgrFrf5EpGEpControlStatus_Type()
)
mcsMgrFrf5EpGEpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpControlStatus.setStatus("mandatory")


class _McsMgrFrf5EpGEpAlarmStatus_Type(OctetString):
    """Custom type mcsMgrFrf5EpGEpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrFrf5EpGEpAlarmStatus_Type.__name__ = "OctetString"
_McsMgrFrf5EpGEpAlarmStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpAlarmStatus = _McsMgrFrf5EpGEpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 7),
    _McsMgrFrf5EpGEpAlarmStatus_Type()
)
mcsMgrFrf5EpGEpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAlarmStatus.setStatus("mandatory")


class _McsMgrFrf5EpGEpStandbyStatus_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpStandbyStatus based on Integer32"""
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


_McsMgrFrf5EpGEpStandbyStatus_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpStandbyStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpStandbyStatus = _McsMgrFrf5EpGEpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 8),
    _McsMgrFrf5EpGEpStandbyStatus_Type()
)
mcsMgrFrf5EpGEpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpStandbyStatus.setStatus("mandatory")


class _McsMgrFrf5EpGEpUnknownStatus_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpUnknownStatus based on Integer32"""
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


_McsMgrFrf5EpGEpUnknownStatus_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpUnknownStatus_Object = MibTableColumn
mcsMgrFrf5EpGEpUnknownStatus = _McsMgrFrf5EpGEpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 10, 1, 9),
    _McsMgrFrf5EpGEpUnknownStatus_Type()
)
mcsMgrFrf5EpGEpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpUnknownStatus.setStatus("mandatory")
_McsMgrFrf5EpGEpOperTable_Object = MibTable
mcsMgrFrf5EpGEpOperTable = _McsMgrFrf5EpGEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11)
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpOperTable.setStatus("mandatory")
_McsMgrFrf5EpGEpOperEntry_Object = MibTableRow
mcsMgrFrf5EpGEpOperEntry = _McsMgrFrf5EpGEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1)
)
mcsMgrFrf5EpGEpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGIndex"),
    (0, "Nortel-Magellan-Passport-Frf5EpMIB", "mcsMgrFrf5EpGEpIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpOperEntry.setStatus("mandatory")


class _McsMgrFrf5EpGEpLastVccClearCause_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpLastVccClearCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McsMgrFrf5EpGEpLastVccClearCause_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpLastVccClearCause_Object = MibTableColumn
mcsMgrFrf5EpGEpLastVccClearCause = _McsMgrFrf5EpGEpLastVccClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 4),
    _McsMgrFrf5EpGEpLastVccClearCause_Type()
)
mcsMgrFrf5EpGEpLastVccClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLastVccClearCause.setStatus("mandatory")


class _McsMgrFrf5EpGEpConnectionTransferPriority_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McsMgrFrf5EpGEpConnectionTransferPriority_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpConnectionTransferPriority_Object = MibTableColumn
mcsMgrFrf5EpGEpConnectionTransferPriority = _McsMgrFrf5EpGEpConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 5),
    _McsMgrFrf5EpGEpConnectionTransferPriority_Type()
)
mcsMgrFrf5EpGEpConnectionTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpConnectionTransferPriority.setStatus("mandatory")


class _McsMgrFrf5EpGEpServiceCategory_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpServiceCategory based on Integer32"""
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


_McsMgrFrf5EpGEpServiceCategory_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpServiceCategory_Object = MibTableColumn
mcsMgrFrf5EpGEpServiceCategory = _McsMgrFrf5EpGEpServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 6),
    _McsMgrFrf5EpGEpServiceCategory_Type()
)
mcsMgrFrf5EpGEpServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpServiceCategory.setStatus("mandatory")


class _McsMgrFrf5EpGEpPeakCellRate01_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpPeakCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_McsMgrFrf5EpGEpPeakCellRate01_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpPeakCellRate01_Object = MibTableColumn
mcsMgrFrf5EpGEpPeakCellRate01 = _McsMgrFrf5EpGEpPeakCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 8),
    _McsMgrFrf5EpGEpPeakCellRate01_Type()
)
mcsMgrFrf5EpGEpPeakCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpPeakCellRate01.setStatus("mandatory")


class _McsMgrFrf5EpGEpSustainedCellRate0_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpSustainedCellRate0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_McsMgrFrf5EpGEpSustainedCellRate0_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpSustainedCellRate0_Object = MibTableColumn
mcsMgrFrf5EpGEpSustainedCellRate0 = _McsMgrFrf5EpGEpSustainedCellRate0_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 9),
    _McsMgrFrf5EpGEpSustainedCellRate0_Type()
)
mcsMgrFrf5EpGEpSustainedCellRate0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpSustainedCellRate0.setStatus("mandatory")


class _McsMgrFrf5EpGEpSustainedCellRate01_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpSustainedCellRate01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_McsMgrFrf5EpGEpSustainedCellRate01_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpSustainedCellRate01_Object = MibTableColumn
mcsMgrFrf5EpGEpSustainedCellRate01 = _McsMgrFrf5EpGEpSustainedCellRate01_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 10),
    _McsMgrFrf5EpGEpSustainedCellRate01_Type()
)
mcsMgrFrf5EpGEpSustainedCellRate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpSustainedCellRate01.setStatus("mandatory")


class _McsMgrFrf5EpGEpMaximumBurstSize0_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpMaximumBurstSize0 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_McsMgrFrf5EpGEpMaximumBurstSize0_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpMaximumBurstSize0_Object = MibTableColumn
mcsMgrFrf5EpGEpMaximumBurstSize0 = _McsMgrFrf5EpGEpMaximumBurstSize0_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 11),
    _McsMgrFrf5EpGEpMaximumBurstSize0_Type()
)
mcsMgrFrf5EpGEpMaximumBurstSize0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpMaximumBurstSize0.setStatus("mandatory")


class _McsMgrFrf5EpGEpMaximumBurstSize01_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpMaximumBurstSize01 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_McsMgrFrf5EpGEpMaximumBurstSize01_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpMaximumBurstSize01_Object = MibTableColumn
mcsMgrFrf5EpGEpMaximumBurstSize01 = _McsMgrFrf5EpGEpMaximumBurstSize01_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 12),
    _McsMgrFrf5EpGEpMaximumBurstSize01_Type()
)
mcsMgrFrf5EpGEpMaximumBurstSize01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpMaximumBurstSize01.setStatus("mandatory")


class _McsMgrFrf5EpGEpAvgFrameSize_Type(Unsigned32):
    """Custom type mcsMgrFrf5EpGEpAvgFrameSize based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_McsMgrFrf5EpGEpAvgFrameSize_Type.__name__ = "Unsigned32"
_McsMgrFrf5EpGEpAvgFrameSize_Object = MibTableColumn
mcsMgrFrf5EpGEpAvgFrameSize = _McsMgrFrf5EpGEpAvgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 13),
    _McsMgrFrf5EpGEpAvgFrameSize_Type()
)
mcsMgrFrf5EpGEpAvgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpAvgFrameSize.setStatus("mandatory")


class _McsMgrFrf5EpGEpTrafficParmConversionPolicy_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpTrafficParmConversionPolicy based on Integer32"""
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


_McsMgrFrf5EpGEpTrafficParmConversionPolicy_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpTrafficParmConversionPolicy_Object = MibTableColumn
mcsMgrFrf5EpGEpTrafficParmConversionPolicy = _McsMgrFrf5EpGEpTrafficParmConversionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 14),
    _McsMgrFrf5EpGEpTrafficParmConversionPolicy_Type()
)
mcsMgrFrf5EpGEpTrafficParmConversionPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpTrafficParmConversionPolicy.setStatus("mandatory")


class _McsMgrFrf5EpGEpType_Type(Integer32):
    """Custom type mcsMgrFrf5EpGEpType based on Integer32"""
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


_McsMgrFrf5EpGEpType_Type.__name__ = "Integer32"
_McsMgrFrf5EpGEpType_Object = MibTableColumn
mcsMgrFrf5EpGEpType = _McsMgrFrf5EpGEpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 15),
    _McsMgrFrf5EpGEpType_Type()
)
mcsMgrFrf5EpGEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpType.setStatus("mandatory")


class _McsMgrFrf5EpGEpLastVccCauseDiag_Type(HexString):
    """Custom type mcsMgrFrf5EpGEpLastVccCauseDiag based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_McsMgrFrf5EpGEpLastVccCauseDiag_Type.__name__ = "HexString"
_McsMgrFrf5EpGEpLastVccCauseDiag_Object = MibTableColumn
mcsMgrFrf5EpGEpLastVccCauseDiag = _McsMgrFrf5EpGEpLastVccCauseDiag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 14, 3, 11, 1, 20),
    _McsMgrFrf5EpGEpLastVccCauseDiag_Type()
)
mcsMgrFrf5EpGEpLastVccCauseDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrFrf5EpGEpLastVccCauseDiag.setStatus("mandatory")
_Frf5EpMIB_ObjectIdentity = ObjectIdentity
frf5EpMIB = _Frf5EpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121)
)
_Frf5EpGroup_ObjectIdentity = ObjectIdentity
frf5EpGroup = _Frf5EpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 1)
)
_Frf5EpGroupBD_ObjectIdentity = ObjectIdentity
frf5EpGroupBD = _Frf5EpGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 1, 4)
)
_Frf5EpGroupBD02_ObjectIdentity = ObjectIdentity
frf5EpGroupBD02 = _Frf5EpGroupBD02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 1, 4, 3)
)
_Frf5EpGroupBD02A_ObjectIdentity = ObjectIdentity
frf5EpGroupBD02A = _Frf5EpGroupBD02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 1, 4, 3, 2)
)
_Frf5EpCapabilities_ObjectIdentity = ObjectIdentity
frf5EpCapabilities = _Frf5EpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 3)
)
_Frf5EpCapabilitiesBD_ObjectIdentity = ObjectIdentity
frf5EpCapabilitiesBD = _Frf5EpCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 3, 4)
)
_Frf5EpCapabilitiesBD02_ObjectIdentity = ObjectIdentity
frf5EpCapabilitiesBD02 = _Frf5EpCapabilitiesBD02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 3, 4, 3)
)
_Frf5EpCapabilitiesBD02A_ObjectIdentity = ObjectIdentity
frf5EpCapabilitiesBD02A = _Frf5EpCapabilitiesBD02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 121, 3, 4, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-Frf5EpMIB",
    **{"mcsMgrFrf5EpG": mcsMgrFrf5EpG,
       "mcsMgrFrf5EpGRowStatusTable": mcsMgrFrf5EpGRowStatusTable,
       "mcsMgrFrf5EpGRowStatusEntry": mcsMgrFrf5EpGRowStatusEntry,
       "mcsMgrFrf5EpGRowStatus": mcsMgrFrf5EpGRowStatus,
       "mcsMgrFrf5EpGComponentName": mcsMgrFrf5EpGComponentName,
       "mcsMgrFrf5EpGStorageType": mcsMgrFrf5EpGStorageType,
       "mcsMgrFrf5EpGIndex": mcsMgrFrf5EpGIndex,
       "mcsMgrFrf5EpGAddr": mcsMgrFrf5EpGAddr,
       "mcsMgrFrf5EpGAddrRowStatusTable": mcsMgrFrf5EpGAddrRowStatusTable,
       "mcsMgrFrf5EpGAddrRowStatusEntry": mcsMgrFrf5EpGAddrRowStatusEntry,
       "mcsMgrFrf5EpGAddrRowStatus": mcsMgrFrf5EpGAddrRowStatus,
       "mcsMgrFrf5EpGAddrComponentName": mcsMgrFrf5EpGAddrComponentName,
       "mcsMgrFrf5EpGAddrStorageType": mcsMgrFrf5EpGAddrStorageType,
       "mcsMgrFrf5EpGAddrIndex": mcsMgrFrf5EpGAddrIndex,
       "mcsMgrFrf5EpGAddrProvTable": mcsMgrFrf5EpGAddrProvTable,
       "mcsMgrFrf5EpGAddrProvEntry": mcsMgrFrf5EpGAddrProvEntry,
       "mcsMgrFrf5EpGAddrRemoteAddress": mcsMgrFrf5EpGAddrRemoteAddress,
       "mcsMgrFrf5EpGAddrCommentText": mcsMgrFrf5EpGAddrCommentText,
       "mcsMgrFrf5EpGAddrAddrPreTable": mcsMgrFrf5EpGAddrAddrPreTable,
       "mcsMgrFrf5EpGAddrAddrPreEntry": mcsMgrFrf5EpGAddrAddrPreEntry,
       "mcsMgrFrf5EpGAddrAddrPreValue": mcsMgrFrf5EpGAddrAddrPreValue,
       "mcsMgrFrf5EpGAddrAddrPreRowStatus": mcsMgrFrf5EpGAddrAddrPreRowStatus,
       "mcsMgrFrf5EpGEp": mcsMgrFrf5EpGEp,
       "mcsMgrFrf5EpGEpRowStatusTable": mcsMgrFrf5EpGEpRowStatusTable,
       "mcsMgrFrf5EpGEpRowStatusEntry": mcsMgrFrf5EpGEpRowStatusEntry,
       "mcsMgrFrf5EpGEpRowStatus": mcsMgrFrf5EpGEpRowStatus,
       "mcsMgrFrf5EpGEpComponentName": mcsMgrFrf5EpGEpComponentName,
       "mcsMgrFrf5EpGEpStorageType": mcsMgrFrf5EpGEpStorageType,
       "mcsMgrFrf5EpGEpIndex": mcsMgrFrf5EpGEpIndex,
       "mcsMgrFrf5EpGEpLmi": mcsMgrFrf5EpGEpLmi,
       "mcsMgrFrf5EpGEpLmiRowStatusTable": mcsMgrFrf5EpGEpLmiRowStatusTable,
       "mcsMgrFrf5EpGEpLmiRowStatusEntry": mcsMgrFrf5EpGEpLmiRowStatusEntry,
       "mcsMgrFrf5EpGEpLmiRowStatus": mcsMgrFrf5EpGEpLmiRowStatus,
       "mcsMgrFrf5EpGEpLmiComponentName": mcsMgrFrf5EpGEpLmiComponentName,
       "mcsMgrFrf5EpGEpLmiStorageType": mcsMgrFrf5EpGEpLmiStorageType,
       "mcsMgrFrf5EpGEpLmiIndex": mcsMgrFrf5EpGEpLmiIndex,
       "mcsMgrFrf5EpGEpLmiParmsTable": mcsMgrFrf5EpGEpLmiParmsTable,
       "mcsMgrFrf5EpGEpLmiParmsEntry": mcsMgrFrf5EpGEpLmiParmsEntry,
       "mcsMgrFrf5EpGEpLmiProcedures": mcsMgrFrf5EpGEpLmiProcedures,
       "mcsMgrFrf5EpGEpLmiAsyncStatusReport": mcsMgrFrf5EpGEpLmiAsyncStatusReport,
       "mcsMgrFrf5EpGEpLmiErrorEventThreshold": mcsMgrFrf5EpGEpLmiErrorEventThreshold,
       "mcsMgrFrf5EpGEpLmiEventCount": mcsMgrFrf5EpGEpLmiEventCount,
       "mcsMgrFrf5EpGEpLmiCheckPointTimer": mcsMgrFrf5EpGEpLmiCheckPointTimer,
       "mcsMgrFrf5EpGEpLmiSide": mcsMgrFrf5EpGEpLmiSide,
       "mcsMgrFrf5EpGEpLmiNniParmsTable": mcsMgrFrf5EpGEpLmiNniParmsTable,
       "mcsMgrFrf5EpGEpLmiNniParmsEntry": mcsMgrFrf5EpGEpLmiNniParmsEntry,
       "mcsMgrFrf5EpGEpLmiFullStatusPollingCycles": mcsMgrFrf5EpGEpLmiFullStatusPollingCycles,
       "mcsMgrFrf5EpGEpLmiLinkVerificationTimer": mcsMgrFrf5EpGEpLmiLinkVerificationTimer,
       "mcsMgrFrf5EpGEpLmiStateTable": mcsMgrFrf5EpGEpLmiStateTable,
       "mcsMgrFrf5EpGEpLmiStateEntry": mcsMgrFrf5EpGEpLmiStateEntry,
       "mcsMgrFrf5EpGEpLmiAdminState": mcsMgrFrf5EpGEpLmiAdminState,
       "mcsMgrFrf5EpGEpLmiOperationalState": mcsMgrFrf5EpGEpLmiOperationalState,
       "mcsMgrFrf5EpGEpLmiUsageState": mcsMgrFrf5EpGEpLmiUsageState,
       "mcsMgrFrf5EpGEpLmiPsiTable": mcsMgrFrf5EpGEpLmiPsiTable,
       "mcsMgrFrf5EpGEpLmiPsiEntry": mcsMgrFrf5EpGEpLmiPsiEntry,
       "mcsMgrFrf5EpGEpLmiProtocolStatus": mcsMgrFrf5EpGEpLmiProtocolStatus,
       "mcsMgrFrf5EpGEpLmiStatsTable": mcsMgrFrf5EpGEpLmiStatsTable,
       "mcsMgrFrf5EpGEpLmiStatsEntry": mcsMgrFrf5EpGEpLmiStatsEntry,
       "mcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface": mcsMgrFrf5EpGEpLmiKeepAliveStatusToInterface,
       "mcsMgrFrf5EpGEpLmiFullStatusToInterface": mcsMgrFrf5EpGEpLmiFullStatusToInterface,
       "mcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface": mcsMgrFrf5EpGEpLmiKeepAliveStatusEnqFromInterface,
       "mcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface": mcsMgrFrf5EpGEpLmiFullStatusEnqFromInterface,
       "mcsMgrFrf5EpGEpLmiNetworkSideEventHistory": mcsMgrFrf5EpGEpLmiNetworkSideEventHistory,
       "mcsMgrFrf5EpGEpLmiUserSideEventHistory": mcsMgrFrf5EpGEpLmiUserSideEventHistory,
       "mcsMgrFrf5EpGEpLmiProtocolErrors": mcsMgrFrf5EpGEpLmiProtocolErrors,
       "mcsMgrFrf5EpGEpLmiUnexpectedIes": mcsMgrFrf5EpGEpLmiUnexpectedIes,
       "mcsMgrFrf5EpGEpLmiSequenceErrors": mcsMgrFrf5EpGEpLmiSequenceErrors,
       "mcsMgrFrf5EpGEpLmiStatusSequenceErrors": mcsMgrFrf5EpGEpLmiStatusSequenceErrors,
       "mcsMgrFrf5EpGEpLmiUnexpectedReports": mcsMgrFrf5EpGEpLmiUnexpectedReports,
       "mcsMgrFrf5EpGEpLmiPollingVerifTimeouts": mcsMgrFrf5EpGEpLmiPollingVerifTimeouts,
       "mcsMgrFrf5EpGEpLmiNoStatusReportCount": mcsMgrFrf5EpGEpLmiNoStatusReportCount,
       "mcsMgrFrf5EpGEpLmiKeepAliveEnqToIf": mcsMgrFrf5EpGEpLmiKeepAliveEnqToIf,
       "mcsMgrFrf5EpGEpLmiFullStatusEnqToIf": mcsMgrFrf5EpGEpLmiFullStatusEnqToIf,
       "mcsMgrFrf5EpGEpEpd": mcsMgrFrf5EpGEpEpd,
       "mcsMgrFrf5EpGEpEpdRowStatusTable": mcsMgrFrf5EpGEpEpdRowStatusTable,
       "mcsMgrFrf5EpGEpEpdRowStatusEntry": mcsMgrFrf5EpGEpEpdRowStatusEntry,
       "mcsMgrFrf5EpGEpEpdRowStatus": mcsMgrFrf5EpGEpEpdRowStatus,
       "mcsMgrFrf5EpGEpEpdComponentName": mcsMgrFrf5EpGEpEpdComponentName,
       "mcsMgrFrf5EpGEpEpdStorageType": mcsMgrFrf5EpGEpEpdStorageType,
       "mcsMgrFrf5EpGEpEpdIndex": mcsMgrFrf5EpGEpEpdIndex,
       "mcsMgrFrf5EpGEpEpdProvTable": mcsMgrFrf5EpGEpEpdProvTable,
       "mcsMgrFrf5EpGEpEpdProvEntry": mcsMgrFrf5EpGEpEpdProvEntry,
       "mcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier": mcsMgrFrf5EpGEpEpdRemoteConnectionIdentifier,
       "mcsMgrFrf5EpGEpEpdConnectionTransferPriority": mcsMgrFrf5EpGEpEpdConnectionTransferPriority,
       "mcsMgrFrf5EpGEpEpdCommittedInformationRate": mcsMgrFrf5EpGEpEpdCommittedInformationRate,
       "mcsMgrFrf5EpGEpEpdExcessInformationRate": mcsMgrFrf5EpGEpEpdExcessInformationRate,
       "mcsMgrFrf5EpGEpEpdCommittedBurstSize": mcsMgrFrf5EpGEpEpdCommittedBurstSize,
       "mcsMgrFrf5EpGEpEpdType": mcsMgrFrf5EpGEpEpdType,
       "mcsMgrFrf5EpGEpEpdAccessRate": mcsMgrFrf5EpGEpEpdAccessRate,
       "mcsMgrFrf5EpGEpEpdExcessBurstSize": mcsMgrFrf5EpGEpEpdExcessBurstSize,
       "mcsMgrFrf5EpGEpEpdCidDataTable": mcsMgrFrf5EpGEpEpdCidDataTable,
       "mcsMgrFrf5EpGEpEpdCidDataEntry": mcsMgrFrf5EpGEpEpdCidDataEntry,
       "mcsMgrFrf5EpGEpEpdCustomerIdentifier": mcsMgrFrf5EpGEpEpdCustomerIdentifier,
       "mcsMgrFrf5EpGEpDlci": mcsMgrFrf5EpGEpDlci,
       "mcsMgrFrf5EpGEpDlciRowStatusTable": mcsMgrFrf5EpGEpDlciRowStatusTable,
       "mcsMgrFrf5EpGEpDlciRowStatusEntry": mcsMgrFrf5EpGEpDlciRowStatusEntry,
       "mcsMgrFrf5EpGEpDlciRowStatus": mcsMgrFrf5EpGEpDlciRowStatus,
       "mcsMgrFrf5EpGEpDlciComponentName": mcsMgrFrf5EpGEpDlciComponentName,
       "mcsMgrFrf5EpGEpDlciStorageType": mcsMgrFrf5EpGEpDlciStorageType,
       "mcsMgrFrf5EpGEpDlciIndex": mcsMgrFrf5EpGEpDlciIndex,
       "mcsMgrFrf5EpGEpDlciOperTable": mcsMgrFrf5EpGEpDlciOperTable,
       "mcsMgrFrf5EpGEpDlciOperEntry": mcsMgrFrf5EpGEpDlciOperEntry,
       "mcsMgrFrf5EpGEpDlciABitStatusToIf": mcsMgrFrf5EpGEpDlciABitStatusToIf,
       "mcsMgrFrf5EpGEpDlciABitReasonToIf": mcsMgrFrf5EpGEpDlciABitReasonToIf,
       "mcsMgrFrf5EpGEpDlciABitStatusFromIf": mcsMgrFrf5EpGEpDlciABitStatusFromIf,
       "mcsMgrFrf5EpGEpDlciABitReasonFromIf": mcsMgrFrf5EpGEpDlciABitReasonFromIf,
       "mcsMgrFrf5EpGEpDlciAccessConnectionComponent": mcsMgrFrf5EpGEpDlciAccessConnectionComponent,
       "mcsMgrFrf5EpGEpAtmCon": mcsMgrFrf5EpGEpAtmCon,
       "mcsMgrFrf5EpGEpAtmConRowStatusTable": mcsMgrFrf5EpGEpAtmConRowStatusTable,
       "mcsMgrFrf5EpGEpAtmConRowStatusEntry": mcsMgrFrf5EpGEpAtmConRowStatusEntry,
       "mcsMgrFrf5EpGEpAtmConRowStatus": mcsMgrFrf5EpGEpAtmConRowStatus,
       "mcsMgrFrf5EpGEpAtmConComponentName": mcsMgrFrf5EpGEpAtmConComponentName,
       "mcsMgrFrf5EpGEpAtmConStorageType": mcsMgrFrf5EpGEpAtmConStorageType,
       "mcsMgrFrf5EpGEpAtmConIndex": mcsMgrFrf5EpGEpAtmConIndex,
       "mcsMgrFrf5EpGEpAtmConOperTable": mcsMgrFrf5EpGEpAtmConOperTable,
       "mcsMgrFrf5EpGEpAtmConOperEntry": mcsMgrFrf5EpGEpAtmConOperEntry,
       "mcsMgrFrf5EpGEpAtmConNextHop": mcsMgrFrf5EpGEpAtmConNextHop,
       "mcsMgrFrf5EpGEpStateTable": mcsMgrFrf5EpGEpStateTable,
       "mcsMgrFrf5EpGEpStateEntry": mcsMgrFrf5EpGEpStateEntry,
       "mcsMgrFrf5EpGEpAdminState": mcsMgrFrf5EpGEpAdminState,
       "mcsMgrFrf5EpGEpOperationalState": mcsMgrFrf5EpGEpOperationalState,
       "mcsMgrFrf5EpGEpUsageState": mcsMgrFrf5EpGEpUsageState,
       "mcsMgrFrf5EpGEpAvailabilityStatus": mcsMgrFrf5EpGEpAvailabilityStatus,
       "mcsMgrFrf5EpGEpProceduralStatus": mcsMgrFrf5EpGEpProceduralStatus,
       "mcsMgrFrf5EpGEpControlStatus": mcsMgrFrf5EpGEpControlStatus,
       "mcsMgrFrf5EpGEpAlarmStatus": mcsMgrFrf5EpGEpAlarmStatus,
       "mcsMgrFrf5EpGEpStandbyStatus": mcsMgrFrf5EpGEpStandbyStatus,
       "mcsMgrFrf5EpGEpUnknownStatus": mcsMgrFrf5EpGEpUnknownStatus,
       "mcsMgrFrf5EpGEpOperTable": mcsMgrFrf5EpGEpOperTable,
       "mcsMgrFrf5EpGEpOperEntry": mcsMgrFrf5EpGEpOperEntry,
       "mcsMgrFrf5EpGEpLastVccClearCause": mcsMgrFrf5EpGEpLastVccClearCause,
       "mcsMgrFrf5EpGEpConnectionTransferPriority": mcsMgrFrf5EpGEpConnectionTransferPriority,
       "mcsMgrFrf5EpGEpServiceCategory": mcsMgrFrf5EpGEpServiceCategory,
       "mcsMgrFrf5EpGEpPeakCellRate01": mcsMgrFrf5EpGEpPeakCellRate01,
       "mcsMgrFrf5EpGEpSustainedCellRate0": mcsMgrFrf5EpGEpSustainedCellRate0,
       "mcsMgrFrf5EpGEpSustainedCellRate01": mcsMgrFrf5EpGEpSustainedCellRate01,
       "mcsMgrFrf5EpGEpMaximumBurstSize0": mcsMgrFrf5EpGEpMaximumBurstSize0,
       "mcsMgrFrf5EpGEpMaximumBurstSize01": mcsMgrFrf5EpGEpMaximumBurstSize01,
       "mcsMgrFrf5EpGEpAvgFrameSize": mcsMgrFrf5EpGEpAvgFrameSize,
       "mcsMgrFrf5EpGEpTrafficParmConversionPolicy": mcsMgrFrf5EpGEpTrafficParmConversionPolicy,
       "mcsMgrFrf5EpGEpType": mcsMgrFrf5EpGEpType,
       "mcsMgrFrf5EpGEpLastVccCauseDiag": mcsMgrFrf5EpGEpLastVccCauseDiag,
       "frf5EpMIB": frf5EpMIB,
       "frf5EpGroup": frf5EpGroup,
       "frf5EpGroupBD": frf5EpGroupBD,
       "frf5EpGroupBD02": frf5EpGroupBD02,
       "frf5EpGroupBD02A": frf5EpGroupBD02A,
       "frf5EpCapabilities": frf5EpCapabilities,
       "frf5EpCapabilitiesBD": frf5EpCapabilitiesBD,
       "frf5EpCapabilitiesBD02": frf5EpCapabilitiesBD02,
       "frf5EpCapabilitiesBD02A": frf5EpCapabilitiesBD02A}
)
