# SNMP MIB module (Nortel-Magellan-Passport-DprsMcsEpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-DprsMcsEpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:40 2024
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
 Gauge32,
 Integer32,
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
    "HexString",
    "Link",
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

_McsMgrDprsMcsEpG_ObjectIdentity = ObjectIdentity
mcsMgrDprsMcsEpG = _McsMgrDprsMcsEpG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2)
)
_McsMgrDprsMcsEpGRowStatusTable_Object = MibTable
mcsMgrDprsMcsEpGRowStatusTable = _McsMgrDprsMcsEpGRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 1)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGRowStatusTable.setStatus("mandatory")
_McsMgrDprsMcsEpGRowStatusEntry_Object = MibTableRow
mcsMgrDprsMcsEpGRowStatusEntry = _McsMgrDprsMcsEpGRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 1, 1)
)
mcsMgrDprsMcsEpGRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGRowStatusEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGRowStatus_Type = RowStatus
_McsMgrDprsMcsEpGRowStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGRowStatus = _McsMgrDprsMcsEpGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 1, 1, 1),
    _McsMgrDprsMcsEpGRowStatus_Type()
)
mcsMgrDprsMcsEpGRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGRowStatus.setStatus("mandatory")
_McsMgrDprsMcsEpGComponentName_Type = DisplayString
_McsMgrDprsMcsEpGComponentName_Object = MibTableColumn
mcsMgrDprsMcsEpGComponentName = _McsMgrDprsMcsEpGComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 1, 1, 2),
    _McsMgrDprsMcsEpGComponentName_Type()
)
mcsMgrDprsMcsEpGComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGComponentName.setStatus("mandatory")
_McsMgrDprsMcsEpGStorageType_Type = StorageType
_McsMgrDprsMcsEpGStorageType_Object = MibTableColumn
mcsMgrDprsMcsEpGStorageType = _McsMgrDprsMcsEpGStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 1, 1, 4),
    _McsMgrDprsMcsEpGStorageType_Type()
)
mcsMgrDprsMcsEpGStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGStorageType.setStatus("mandatory")


class _McsMgrDprsMcsEpGIndex_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_McsMgrDprsMcsEpGIndex_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGIndex = _McsMgrDprsMcsEpGIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 1, 1, 10),
    _McsMgrDprsMcsEpGIndex_Type()
)
mcsMgrDprsMcsEpGIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGAddr_ObjectIdentity = ObjectIdentity
mcsMgrDprsMcsEpGAddr = _McsMgrDprsMcsEpGAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2)
)
_McsMgrDprsMcsEpGAddrRowStatusTable_Object = MibTable
mcsMgrDprsMcsEpGAddrRowStatusTable = _McsMgrDprsMcsEpGAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrRowStatusTable.setStatus("mandatory")
_McsMgrDprsMcsEpGAddrRowStatusEntry_Object = MibTableRow
mcsMgrDprsMcsEpGAddrRowStatusEntry = _McsMgrDprsMcsEpGAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 1, 1)
)
mcsMgrDprsMcsEpGAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrRowStatusEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGAddrRowStatus_Type = RowStatus
_McsMgrDprsMcsEpGAddrRowStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGAddrRowStatus = _McsMgrDprsMcsEpGAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 1, 1, 1),
    _McsMgrDprsMcsEpGAddrRowStatus_Type()
)
mcsMgrDprsMcsEpGAddrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrRowStatus.setStatus("mandatory")
_McsMgrDprsMcsEpGAddrComponentName_Type = DisplayString
_McsMgrDprsMcsEpGAddrComponentName_Object = MibTableColumn
mcsMgrDprsMcsEpGAddrComponentName = _McsMgrDprsMcsEpGAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 1, 1, 2),
    _McsMgrDprsMcsEpGAddrComponentName_Type()
)
mcsMgrDprsMcsEpGAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrComponentName.setStatus("mandatory")
_McsMgrDprsMcsEpGAddrStorageType_Type = StorageType
_McsMgrDprsMcsEpGAddrStorageType_Object = MibTableColumn
mcsMgrDprsMcsEpGAddrStorageType = _McsMgrDprsMcsEpGAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 1, 1, 4),
    _McsMgrDprsMcsEpGAddrStorageType_Type()
)
mcsMgrDprsMcsEpGAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrStorageType.setStatus("mandatory")
_McsMgrDprsMcsEpGAddrIndex_Type = NonReplicated
_McsMgrDprsMcsEpGAddrIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGAddrIndex = _McsMgrDprsMcsEpGAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 1, 1, 10),
    _McsMgrDprsMcsEpGAddrIndex_Type()
)
mcsMgrDprsMcsEpGAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGAddrProvTable_Object = MibTable
mcsMgrDprsMcsEpGAddrProvTable = _McsMgrDprsMcsEpGAddrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrProvTable.setStatus("mandatory")
_McsMgrDprsMcsEpGAddrProvEntry_Object = MibTableRow
mcsMgrDprsMcsEpGAddrProvEntry = _McsMgrDprsMcsEpGAddrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 10, 1)
)
mcsMgrDprsMcsEpGAddrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGAddrIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrProvEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGAddrRemoteAddress_Type(AsciiString):
    """Custom type mcsMgrDprsMcsEpGAddrRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_McsMgrDprsMcsEpGAddrRemoteAddress_Type.__name__ = "AsciiString"
_McsMgrDprsMcsEpGAddrRemoteAddress_Object = MibTableColumn
mcsMgrDprsMcsEpGAddrRemoteAddress = _McsMgrDprsMcsEpGAddrRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 10, 1, 1),
    _McsMgrDprsMcsEpGAddrRemoteAddress_Type()
)
mcsMgrDprsMcsEpGAddrRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrRemoteAddress.setStatus("mandatory")


class _McsMgrDprsMcsEpGAddrCommentText_Type(AsciiString):
    """Custom type mcsMgrDprsMcsEpGAddrCommentText based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_McsMgrDprsMcsEpGAddrCommentText_Type.__name__ = "AsciiString"
_McsMgrDprsMcsEpGAddrCommentText_Object = MibTableColumn
mcsMgrDprsMcsEpGAddrCommentText = _McsMgrDprsMcsEpGAddrCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 2, 10, 1, 2),
    _McsMgrDprsMcsEpGAddrCommentText_Type()
)
mcsMgrDprsMcsEpGAddrCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAddrCommentText.setStatus("mandatory")
_McsMgrDprsMcsEpGEp_ObjectIdentity = ObjectIdentity
mcsMgrDprsMcsEpGEp = _McsMgrDprsMcsEpGEp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3)
)
_McsMgrDprsMcsEpGEpRowStatusTable_Object = MibTable
mcsMgrDprsMcsEpGEpRowStatusTable = _McsMgrDprsMcsEpGEpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpRowStatusTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpRowStatusEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpRowStatusEntry = _McsMgrDprsMcsEpGEpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 1, 1)
)
mcsMgrDprsMcsEpGEpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpRowStatusEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGEpRowStatus_Type = RowStatus
_McsMgrDprsMcsEpGEpRowStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpRowStatus = _McsMgrDprsMcsEpGEpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 1, 1, 1),
    _McsMgrDprsMcsEpGEpRowStatus_Type()
)
mcsMgrDprsMcsEpGEpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpRowStatus.setStatus("mandatory")
_McsMgrDprsMcsEpGEpComponentName_Type = DisplayString
_McsMgrDprsMcsEpGEpComponentName_Object = MibTableColumn
mcsMgrDprsMcsEpGEpComponentName = _McsMgrDprsMcsEpGEpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 1, 1, 2),
    _McsMgrDprsMcsEpGEpComponentName_Type()
)
mcsMgrDprsMcsEpGEpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpComponentName.setStatus("mandatory")
_McsMgrDprsMcsEpGEpStorageType_Type = StorageType
_McsMgrDprsMcsEpGEpStorageType_Object = MibTableColumn
mcsMgrDprsMcsEpGEpStorageType = _McsMgrDprsMcsEpGEpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 1, 1, 4),
    _McsMgrDprsMcsEpGEpStorageType_Type()
)
mcsMgrDprsMcsEpGEpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpStorageType.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpIndex_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_McsMgrDprsMcsEpGEpIndex_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGEpIndex = _McsMgrDprsMcsEpGEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 1, 1, 10),
    _McsMgrDprsMcsEpGEpIndex_Type()
)
mcsMgrDprsMcsEpGEpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpD_ObjectIdentity = ObjectIdentity
mcsMgrDprsMcsEpGEpEpD = _McsMgrDprsMcsEpGEpEpD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2)
)
_McsMgrDprsMcsEpGEpEpDRowStatusTable_Object = MibTable
mcsMgrDprsMcsEpGEpEpDRowStatusTable = _McsMgrDprsMcsEpGEpEpDRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDRowStatusTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDRowStatusEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpEpDRowStatusEntry = _McsMgrDprsMcsEpGEpEpDRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 1, 1)
)
mcsMgrDprsMcsEpGEpEpDRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpEpDIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDRowStatusEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDRowStatus_Type = RowStatus
_McsMgrDprsMcsEpGEpEpDRowStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDRowStatus = _McsMgrDprsMcsEpGEpEpDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 1, 1, 1),
    _McsMgrDprsMcsEpGEpEpDRowStatus_Type()
)
mcsMgrDprsMcsEpGEpEpDRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDRowStatus.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDComponentName_Type = DisplayString
_McsMgrDprsMcsEpGEpEpDComponentName_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDComponentName = _McsMgrDprsMcsEpGEpEpDComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 1, 1, 2),
    _McsMgrDprsMcsEpGEpEpDComponentName_Type()
)
mcsMgrDprsMcsEpGEpEpDComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDComponentName.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDStorageType_Type = StorageType
_McsMgrDprsMcsEpGEpEpDStorageType_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDStorageType = _McsMgrDprsMcsEpGEpEpDStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 1, 1, 4),
    _McsMgrDprsMcsEpGEpEpDStorageType_Type()
)
mcsMgrDprsMcsEpGEpEpDStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDStorageType.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDIndex_Type = NonReplicated
_McsMgrDprsMcsEpGEpEpDIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDIndex = _McsMgrDprsMcsEpGEpEpDIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 1, 1, 10),
    _McsMgrDprsMcsEpGEpEpDIndex_Type()
)
mcsMgrDprsMcsEpGEpEpDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDProvTable_Object = MibTable
mcsMgrDprsMcsEpGEpEpDProvTable = _McsMgrDprsMcsEpGEpEpDProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDProvTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDProvEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpEpDProvEntry = _McsMgrDprsMcsEpGEpEpDProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10, 1)
)
mcsMgrDprsMcsEpGEpEpDProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpEpDIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDProvEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpEpDBandwidth_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpEpDBandwidth based on Unsigned32"""
    defaultValue = 512000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56000, 155000000),
    )


_McsMgrDprsMcsEpGEpEpDBandwidth_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpEpDBandwidth_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDBandwidth = _McsMgrDprsMcsEpGEpEpDBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10, 1, 1),
    _McsMgrDprsMcsEpGEpEpDBandwidth_Type()
)
mcsMgrDprsMcsEpGEpEpDBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDBandwidth.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpEpDConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDConnectionTransferPriority = _McsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10, 1, 2),
    _McsMgrDprsMcsEpGEpEpDConnectionTransferPriority_Type()
)
mcsMgrDprsMcsEpGEpEpDConnectionTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDConnectionTransferPriority.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpEpDTransportConnectionPreference based on Integer32"""
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


_McsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDTransportConnectionPreference = _McsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10, 1, 3),
    _McsMgrDprsMcsEpGEpEpDTransportConnectionPreference_Type()
)
mcsMgrDprsMcsEpGEpEpDTransportConnectionPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDTransportConnectionPreference.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDProfile_Type = Link
_McsMgrDprsMcsEpGEpEpDProfile_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDProfile = _McsMgrDprsMcsEpGEpEpDProfile_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10, 1, 4),
    _McsMgrDprsMcsEpGEpEpDProfile_Type()
)
mcsMgrDprsMcsEpGEpEpDProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDProfile.setStatus("mandatory")
_McsMgrDprsMcsEpGEpEpDPorsManualPath_Type = Link
_McsMgrDprsMcsEpGEpEpDPorsManualPath_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDPorsManualPath = _McsMgrDprsMcsEpGEpEpDPorsManualPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10, 1, 5),
    _McsMgrDprsMcsEpGEpEpDPorsManualPath_Type()
)
mcsMgrDprsMcsEpGEpEpDPorsManualPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDPorsManualPath.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Type(OctetString):
    """Custom type mcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities based on OctetString"""
    defaultHexValue = "8000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_McsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Type.__name__ = "OctetString"
_McsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Object = MibTableColumn
mcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities = _McsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 2, 10, 1, 6),
    _McsMgrDprsMcsEpGEpEpDSupportedTransferPriorities_Type()
)
mcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmCon_ObjectIdentity = ObjectIdentity
mcsMgrDprsMcsEpGEpAtmCon = _McsMgrDprsMcsEpGEpAtmCon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3)
)
_McsMgrDprsMcsEpGEpAtmConRowStatusTable_Object = MibTable
mcsMgrDprsMcsEpGEpAtmConRowStatusTable = _McsMgrDprsMcsEpGEpAtmConRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConRowStatusTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConRowStatusEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpAtmConRowStatusEntry = _McsMgrDprsMcsEpGEpAtmConRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 1, 1)
)
mcsMgrDprsMcsEpGEpAtmConRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConRowStatusEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConRowStatus_Type = RowStatus
_McsMgrDprsMcsEpGEpAtmConRowStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAtmConRowStatus = _McsMgrDprsMcsEpGEpAtmConRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 1, 1, 1),
    _McsMgrDprsMcsEpGEpAtmConRowStatus_Type()
)
mcsMgrDprsMcsEpGEpAtmConRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConRowStatus.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConComponentName_Type = DisplayString
_McsMgrDprsMcsEpGEpAtmConComponentName_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAtmConComponentName = _McsMgrDprsMcsEpGEpAtmConComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 1, 1, 2),
    _McsMgrDprsMcsEpGEpAtmConComponentName_Type()
)
mcsMgrDprsMcsEpGEpAtmConComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConComponentName.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConStorageType_Type = StorageType
_McsMgrDprsMcsEpGEpAtmConStorageType_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAtmConStorageType = _McsMgrDprsMcsEpGEpAtmConStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 1, 1, 4),
    _McsMgrDprsMcsEpGEpAtmConStorageType_Type()
)
mcsMgrDprsMcsEpGEpAtmConStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConStorageType.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConIndex_Type = NonReplicated
_McsMgrDprsMcsEpGEpAtmConIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAtmConIndex = _McsMgrDprsMcsEpGEpAtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 1, 1, 10),
    _McsMgrDprsMcsEpGEpAtmConIndex_Type()
)
mcsMgrDprsMcsEpGEpAtmConIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConOperTable_Object = MibTable
mcsMgrDprsMcsEpGEpAtmConOperTable = _McsMgrDprsMcsEpGEpAtmConOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 10)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConOperTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConOperEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpAtmConOperEntry = _McsMgrDprsMcsEpGEpAtmConOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 10, 1)
)
mcsMgrDprsMcsEpGEpAtmConOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpAtmConIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConOperEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGEpAtmConNextHop_Type = RowPointer
_McsMgrDprsMcsEpGEpAtmConNextHop_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAtmConNextHop = _McsMgrDprsMcsEpGEpAtmConNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 3, 10, 1, 1),
    _McsMgrDprsMcsEpGEpAtmConNextHop_Type()
)
mcsMgrDprsMcsEpGEpAtmConNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAtmConNextHop.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCo_ObjectIdentity = ObjectIdentity
mcsMgrDprsMcsEpGEpLCo = _McsMgrDprsMcsEpGEpLCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4)
)
_McsMgrDprsMcsEpGEpLCoRowStatusTable_Object = MibTable
mcsMgrDprsMcsEpGEpLCoRowStatusTable = _McsMgrDprsMcsEpGEpLCoRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRowStatusTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoRowStatusEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpLCoRowStatusEntry = _McsMgrDprsMcsEpGEpLCoRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 1, 1)
)
mcsMgrDprsMcsEpGEpLCoRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpLCoIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRowStatusEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoRowStatus_Type = RowStatus
_McsMgrDprsMcsEpGEpLCoRowStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRowStatus = _McsMgrDprsMcsEpGEpLCoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 1, 1, 1),
    _McsMgrDprsMcsEpGEpLCoRowStatus_Type()
)
mcsMgrDprsMcsEpGEpLCoRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRowStatus.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoComponentName_Type = DisplayString
_McsMgrDprsMcsEpGEpLCoComponentName_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoComponentName = _McsMgrDprsMcsEpGEpLCoComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 1, 1, 2),
    _McsMgrDprsMcsEpGEpLCoComponentName_Type()
)
mcsMgrDprsMcsEpGEpLCoComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoComponentName.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoStorageType_Type = StorageType
_McsMgrDprsMcsEpGEpLCoStorageType_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoStorageType = _McsMgrDprsMcsEpGEpLCoStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 1, 1, 4),
    _McsMgrDprsMcsEpGEpLCoStorageType_Type()
)
mcsMgrDprsMcsEpGEpLCoStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoStorageType.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoIndex_Type = NonReplicated
_McsMgrDprsMcsEpGEpLCoIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoIndex = _McsMgrDprsMcsEpGEpLCoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 1, 1, 10),
    _McsMgrDprsMcsEpGEpLCoIndex_Type()
)
mcsMgrDprsMcsEpGEpLCoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoPathDataTable_Object = MibTable
mcsMgrDprsMcsEpGEpLCoPathDataTable = _McsMgrDprsMcsEpGEpLCoPathDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathDataTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoPathDataEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpLCoPathDataEntry = _McsMgrDprsMcsEpGEpLCoPathDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1)
)
mcsMgrDprsMcsEpGEpLCoPathDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpLCoIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathDataEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoState_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoState based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoState_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoState_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoState = _McsMgrDprsMcsEpGEpLCoState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 1),
    _McsMgrDprsMcsEpGEpLCoState_Type()
)
mcsMgrDprsMcsEpGEpLCoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoState.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoOverrideRemoteName_Type(AsciiString):
    """Custom type mcsMgrDprsMcsEpGEpLCoOverrideRemoteName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_McsMgrDprsMcsEpGEpLCoOverrideRemoteName_Type.__name__ = "AsciiString"
_McsMgrDprsMcsEpGEpLCoOverrideRemoteName_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoOverrideRemoteName = _McsMgrDprsMcsEpGEpLCoOverrideRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 2),
    _McsMgrDprsMcsEpGEpLCoOverrideRemoteName_Type()
)
mcsMgrDprsMcsEpGEpLCoOverrideRemoteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoOverrideRemoteName.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoEnd_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoEnd based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoEnd_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoEnd_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoEnd = _McsMgrDprsMcsEpGEpLCoEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 3),
    _McsMgrDprsMcsEpGEpLCoEnd_Type()
)
mcsMgrDprsMcsEpGEpLCoEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoEnd.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoCostMetric_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoCostMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McsMgrDprsMcsEpGEpLCoCostMetric_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoCostMetric_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoCostMetric = _McsMgrDprsMcsEpGEpLCoCostMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 4),
    _McsMgrDprsMcsEpGEpLCoCostMetric_Type()
)
mcsMgrDprsMcsEpGEpLCoCostMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoCostMetric.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoDelayMetric_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoDelayMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_McsMgrDprsMcsEpGEpLCoDelayMetric_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoDelayMetric_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoDelayMetric = _McsMgrDprsMcsEpGEpLCoDelayMetric_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 5),
    _McsMgrDprsMcsEpGEpLCoDelayMetric_Type()
)
mcsMgrDprsMcsEpGEpLCoDelayMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoDelayMetric.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoRoundTripDelay_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoRoundTripDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_McsMgrDprsMcsEpGEpLCoRoundTripDelay_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoRoundTripDelay_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRoundTripDelay = _McsMgrDprsMcsEpGEpLCoRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 6),
    _McsMgrDprsMcsEpGEpLCoRoundTripDelay_Type()
)
mcsMgrDprsMcsEpGEpLCoRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRoundTripDelay.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoSetupPriority_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_McsMgrDprsMcsEpGEpLCoSetupPriority_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoSetupPriority_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoSetupPriority = _McsMgrDprsMcsEpGEpLCoSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 7),
    _McsMgrDprsMcsEpGEpLCoSetupPriority_Type()
)
mcsMgrDprsMcsEpGEpLCoSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoSetupPriority.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoHoldingPriority_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_McsMgrDprsMcsEpGEpLCoHoldingPriority_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoHoldingPriority_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoHoldingPriority = _McsMgrDprsMcsEpGEpLCoHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 8),
    _McsMgrDprsMcsEpGEpLCoHoldingPriority_Type()
)
mcsMgrDprsMcsEpGEpLCoHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoHoldingPriority.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Type(Gauge32):
    """Custom type mcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_McsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Type.__name__ = "Gauge32"
_McsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth = _McsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 9),
    _McsMgrDprsMcsEpGEpLCoRequiredTxBandwidth_Type()
)
mcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Type(Gauge32):
    """Custom type mcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_McsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Type.__name__ = "Gauge32"
_McsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth = _McsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 10),
    _McsMgrDprsMcsEpGEpLCoRequiredRxBandwidth_Type()
)
mcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoRequiredTrafficType_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoRequiredTrafficType based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoRequiredTrafficType_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoRequiredTrafficType_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRequiredTrafficType = _McsMgrDprsMcsEpGEpLCoRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 11),
    _McsMgrDprsMcsEpGEpLCoRequiredTrafficType_Type()
)
mcsMgrDprsMcsEpGEpLCoRequiredTrafficType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRequiredTrafficType.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Type(OctetString):
    """Custom type mcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Type.__name__ = "OctetString"
_McsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes = _McsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 12),
    _McsMgrDprsMcsEpGEpLCoPermittedTrunkTypes_Type()
)
mcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoRequiredSecurity_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoRequiredSecurity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_McsMgrDprsMcsEpGEpLCoRequiredSecurity_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoRequiredSecurity_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRequiredSecurity = _McsMgrDprsMcsEpGEpLCoRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 13),
    _McsMgrDprsMcsEpGEpLCoRequiredSecurity_Type()
)
mcsMgrDprsMcsEpGEpLCoRequiredSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRequiredSecurity.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_McsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter = _McsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 14),
    _McsMgrDprsMcsEpGEpLCoRequiredCustomerParameter_Type()
)
mcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoEmissionPriority_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoEmissionPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_McsMgrDprsMcsEpGEpLCoEmissionPriority_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoEmissionPriority_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoEmissionPriority = _McsMgrDprsMcsEpGEpLCoEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 15),
    _McsMgrDprsMcsEpGEpLCoEmissionPriority_Type()
)
mcsMgrDprsMcsEpGEpLCoEmissionPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoEmissionPriority.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoDiscardPriority_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoDiscardPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_McsMgrDprsMcsEpGEpLCoDiscardPriority_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoDiscardPriority_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoDiscardPriority = _McsMgrDprsMcsEpGEpLCoDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 16),
    _McsMgrDprsMcsEpGEpLCoDiscardPriority_Type()
)
mcsMgrDprsMcsEpGEpLCoDiscardPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoDiscardPriority.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoPathType_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoPathType based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoPathType_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoPathType_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPathType = _McsMgrDprsMcsEpGEpLCoPathType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 17),
    _McsMgrDprsMcsEpGEpLCoPathType_Type()
)
mcsMgrDprsMcsEpGEpLCoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathType.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoRetryCount_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoRetryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McsMgrDprsMcsEpGEpLCoRetryCount_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoRetryCount_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoRetryCount = _McsMgrDprsMcsEpGEpLCoRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 18),
    _McsMgrDprsMcsEpGEpLCoRetryCount_Type()
)
mcsMgrDprsMcsEpGEpLCoRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoRetryCount.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoPathFailureCount_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLCoPathFailureCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McsMgrDprsMcsEpGEpLCoPathFailureCount_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLCoPathFailureCount_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPathFailureCount = _McsMgrDprsMcsEpGEpLCoPathFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 19),
    _McsMgrDprsMcsEpGEpLCoPathFailureCount_Type()
)
mcsMgrDprsMcsEpGEpLCoPathFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathFailureCount.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoReasonForNoRoute_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoReasonForNoRoute based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoReasonForNoRoute_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoReasonForNoRoute_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoReasonForNoRoute = _McsMgrDprsMcsEpGEpLCoReasonForNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 20),
    _McsMgrDprsMcsEpGEpLCoReasonForNoRoute_Type()
)
mcsMgrDprsMcsEpGEpLCoReasonForNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoReasonForNoRoute.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoLastTearDownReason_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoLastTearDownReason based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoLastTearDownReason_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoLastTearDownReason_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoLastTearDownReason = _McsMgrDprsMcsEpGEpLCoLastTearDownReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 21),
    _McsMgrDprsMcsEpGEpLCoLastTearDownReason_Type()
)
mcsMgrDprsMcsEpGEpLCoLastTearDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoLastTearDownReason.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoPathFailureAction_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoPathFailureAction based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoPathFailureAction_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoPathFailureAction_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPathFailureAction = _McsMgrDprsMcsEpGEpLCoPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 22),
    _McsMgrDprsMcsEpGEpLCoPathFailureAction_Type()
)
mcsMgrDprsMcsEpGEpLCoPathFailureAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathFailureAction.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoBumpPreference_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoBumpPreference based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoBumpPreference_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoBumpPreference_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoBumpPreference = _McsMgrDprsMcsEpGEpLCoBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 23),
    _McsMgrDprsMcsEpGEpLCoBumpPreference_Type()
)
mcsMgrDprsMcsEpGEpLCoBumpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoBumpPreference.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoOptimization_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpLCoOptimization based on Integer32"""
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


_McsMgrDprsMcsEpGEpLCoOptimization_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpLCoOptimization_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoOptimization = _McsMgrDprsMcsEpGEpLCoOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 24),
    _McsMgrDprsMcsEpGEpLCoOptimization_Type()
)
mcsMgrDprsMcsEpGEpLCoOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoOptimization.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoPathUpDateTime_Type(EnterpriseDateAndTime):
    """Custom type mcsMgrDprsMcsEpGEpLCoPathUpDateTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_McsMgrDprsMcsEpGEpLCoPathUpDateTime_Type.__name__ = "EnterpriseDateAndTime"
_McsMgrDprsMcsEpGEpLCoPathUpDateTime_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPathUpDateTime = _McsMgrDprsMcsEpGEpLCoPathUpDateTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 10, 1, 25),
    _McsMgrDprsMcsEpGEpLCoPathUpDateTime_Type()
)
mcsMgrDprsMcsEpGEpLCoPathUpDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathUpDateTime.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoStatsTable_Object = MibTable
mcsMgrDprsMcsEpGEpLCoStatsTable = _McsMgrDprsMcsEpGEpLCoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 11)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoStatsTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoStatsEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpLCoStatsEntry = _McsMgrDprsMcsEpGEpLCoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 11, 1)
)
mcsMgrDprsMcsEpGEpLCoStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpLCoIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoStatsEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoPktsToNetwork_Type = PassportCounter64
_McsMgrDprsMcsEpGEpLCoPktsToNetwork_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPktsToNetwork = _McsMgrDprsMcsEpGEpLCoPktsToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 11, 1, 1),
    _McsMgrDprsMcsEpGEpLCoPktsToNetwork_Type()
)
mcsMgrDprsMcsEpGEpLCoPktsToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPktsToNetwork.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoBytesToNetwork_Type = PassportCounter64
_McsMgrDprsMcsEpGEpLCoBytesToNetwork_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoBytesToNetwork = _McsMgrDprsMcsEpGEpLCoBytesToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 11, 1, 2),
    _McsMgrDprsMcsEpGEpLCoBytesToNetwork_Type()
)
mcsMgrDprsMcsEpGEpLCoBytesToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoBytesToNetwork.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoPktsFromNetwork_Type = PassportCounter64
_McsMgrDprsMcsEpGEpLCoPktsFromNetwork_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPktsFromNetwork = _McsMgrDprsMcsEpGEpLCoPktsFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 11, 1, 3),
    _McsMgrDprsMcsEpGEpLCoPktsFromNetwork_Type()
)
mcsMgrDprsMcsEpGEpLCoPktsFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPktsFromNetwork.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoBytesFromNetwork_Type = PassportCounter64
_McsMgrDprsMcsEpGEpLCoBytesFromNetwork_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoBytesFromNetwork = _McsMgrDprsMcsEpGEpLCoBytesFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 11, 1, 4),
    _McsMgrDprsMcsEpGEpLCoBytesFromNetwork_Type()
)
mcsMgrDprsMcsEpGEpLCoBytesFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoBytesFromNetwork.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoPathTable_Object = MibTable
mcsMgrDprsMcsEpGEpLCoPathTable = _McsMgrDprsMcsEpGEpLCoPathTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 264)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpLCoPathEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpLCoPathEntry = _McsMgrDprsMcsEpGEpLCoPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 264, 1)
)
mcsMgrDprsMcsEpGEpLCoPathEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpLCoIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpLCoPathValue"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLCoPathValue_Type(AsciiString):
    """Custom type mcsMgrDprsMcsEpGEpLCoPathValue based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_McsMgrDprsMcsEpGEpLCoPathValue_Type.__name__ = "AsciiString"
_McsMgrDprsMcsEpGEpLCoPathValue_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLCoPathValue = _McsMgrDprsMcsEpGEpLCoPathValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 4, 264, 1, 1),
    _McsMgrDprsMcsEpGEpLCoPathValue_Type()
)
mcsMgrDprsMcsEpGEpLCoPathValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLCoPathValue.setStatus("mandatory")
_McsMgrDprsMcsEpGEpStateTable_Object = MibTable
mcsMgrDprsMcsEpGEpStateTable = _McsMgrDprsMcsEpGEpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpStateTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpStateEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpStateEntry = _McsMgrDprsMcsEpGEpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1)
)
mcsMgrDprsMcsEpGEpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpStateEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpAdminState_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpAdminState based on Integer32"""
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


_McsMgrDprsMcsEpGEpAdminState_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpAdminState_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAdminState = _McsMgrDprsMcsEpGEpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 1),
    _McsMgrDprsMcsEpGEpAdminState_Type()
)
mcsMgrDprsMcsEpGEpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAdminState.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpOperationalState_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpOperationalState based on Integer32"""
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


_McsMgrDprsMcsEpGEpOperationalState_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpOperationalState_Object = MibTableColumn
mcsMgrDprsMcsEpGEpOperationalState = _McsMgrDprsMcsEpGEpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 2),
    _McsMgrDprsMcsEpGEpOperationalState_Type()
)
mcsMgrDprsMcsEpGEpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpOperationalState.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpUsageState_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpUsageState based on Integer32"""
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


_McsMgrDprsMcsEpGEpUsageState_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpUsageState_Object = MibTableColumn
mcsMgrDprsMcsEpGEpUsageState = _McsMgrDprsMcsEpGEpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 3),
    _McsMgrDprsMcsEpGEpUsageState_Type()
)
mcsMgrDprsMcsEpGEpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpUsageState.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpAvailabilityStatus_Type(OctetString):
    """Custom type mcsMgrDprsMcsEpGEpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_McsMgrDprsMcsEpGEpAvailabilityStatus_Type.__name__ = "OctetString"
_McsMgrDprsMcsEpGEpAvailabilityStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAvailabilityStatus = _McsMgrDprsMcsEpGEpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 4),
    _McsMgrDprsMcsEpGEpAvailabilityStatus_Type()
)
mcsMgrDprsMcsEpGEpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAvailabilityStatus.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpProceduralStatus_Type(OctetString):
    """Custom type mcsMgrDprsMcsEpGEpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrDprsMcsEpGEpProceduralStatus_Type.__name__ = "OctetString"
_McsMgrDprsMcsEpGEpProceduralStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpProceduralStatus = _McsMgrDprsMcsEpGEpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 5),
    _McsMgrDprsMcsEpGEpProceduralStatus_Type()
)
mcsMgrDprsMcsEpGEpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpProceduralStatus.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpControlStatus_Type(OctetString):
    """Custom type mcsMgrDprsMcsEpGEpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrDprsMcsEpGEpControlStatus_Type.__name__ = "OctetString"
_McsMgrDprsMcsEpGEpControlStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpControlStatus = _McsMgrDprsMcsEpGEpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 6),
    _McsMgrDprsMcsEpGEpControlStatus_Type()
)
mcsMgrDprsMcsEpGEpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpControlStatus.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpAlarmStatus_Type(OctetString):
    """Custom type mcsMgrDprsMcsEpGEpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_McsMgrDprsMcsEpGEpAlarmStatus_Type.__name__ = "OctetString"
_McsMgrDprsMcsEpGEpAlarmStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpAlarmStatus = _McsMgrDprsMcsEpGEpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 7),
    _McsMgrDprsMcsEpGEpAlarmStatus_Type()
)
mcsMgrDprsMcsEpGEpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpAlarmStatus.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpStandbyStatus_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpStandbyStatus based on Integer32"""
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


_McsMgrDprsMcsEpGEpStandbyStatus_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpStandbyStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpStandbyStatus = _McsMgrDprsMcsEpGEpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 8),
    _McsMgrDprsMcsEpGEpStandbyStatus_Type()
)
mcsMgrDprsMcsEpGEpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpStandbyStatus.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpUnknownStatus_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpUnknownStatus based on Integer32"""
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


_McsMgrDprsMcsEpGEpUnknownStatus_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpUnknownStatus_Object = MibTableColumn
mcsMgrDprsMcsEpGEpUnknownStatus = _McsMgrDprsMcsEpGEpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 10, 1, 9),
    _McsMgrDprsMcsEpGEpUnknownStatus_Type()
)
mcsMgrDprsMcsEpGEpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpUnknownStatus.setStatus("mandatory")
_McsMgrDprsMcsEpGEpOperTable_Object = MibTable
mcsMgrDprsMcsEpGEpOperTable = _McsMgrDprsMcsEpGEpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpOperTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpOperEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpOperEntry = _McsMgrDprsMcsEpGEpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1)
)
mcsMgrDprsMcsEpGEpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpOperEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpLastTransportConnectionClearCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_McsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLastTransportConnectionClearCause = _McsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 3),
    _McsMgrDprsMcsEpGEpLastTransportConnectionClearCause_Type()
)
mcsMgrDprsMcsEpGEpLastTransportConnectionClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLastTransportConnectionClearCause.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpType_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpType based on Integer32"""
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


_McsMgrDprsMcsEpGEpType_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpType_Object = MibTableColumn
mcsMgrDprsMcsEpGEpType = _McsMgrDprsMcsEpGEpType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 4),
    _McsMgrDprsMcsEpGEpType_Type()
)
mcsMgrDprsMcsEpGEpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpType.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpSupportedTransferPriorities_Type(OctetString):
    """Custom type mcsMgrDprsMcsEpGEpSupportedTransferPriorities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_McsMgrDprsMcsEpGEpSupportedTransferPriorities_Type.__name__ = "OctetString"
_McsMgrDprsMcsEpGEpSupportedTransferPriorities_Object = MibTableColumn
mcsMgrDprsMcsEpGEpSupportedTransferPriorities = _McsMgrDprsMcsEpGEpSupportedTransferPriorities_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 5),
    _McsMgrDprsMcsEpGEpSupportedTransferPriorities_Type()
)
mcsMgrDprsMcsEpGEpSupportedTransferPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpSupportedTransferPriorities.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpConnectionTransferPriority_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpConnectionTransferPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McsMgrDprsMcsEpGEpConnectionTransferPriority_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpConnectionTransferPriority_Object = MibTableColumn
mcsMgrDprsMcsEpGEpConnectionTransferPriority = _McsMgrDprsMcsEpGEpConnectionTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 6),
    _McsMgrDprsMcsEpGEpConnectionTransferPriority_Type()
)
mcsMgrDprsMcsEpGEpConnectionTransferPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpConnectionTransferPriority.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpServiceCategory_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpServiceCategory based on Integer32"""
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


_McsMgrDprsMcsEpGEpServiceCategory_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpServiceCategory_Object = MibTableColumn
mcsMgrDprsMcsEpGEpServiceCategory = _McsMgrDprsMcsEpGEpServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 7),
    _McsMgrDprsMcsEpGEpServiceCategory_Type()
)
mcsMgrDprsMcsEpGEpServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpServiceCategory.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpBandwidth_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_McsMgrDprsMcsEpGEpBandwidth_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpBandwidth_Object = MibTableColumn
mcsMgrDprsMcsEpGEpBandwidth = _McsMgrDprsMcsEpGEpBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 8),
    _McsMgrDprsMcsEpGEpBandwidth_Type()
)
mcsMgrDprsMcsEpGEpBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpBandwidth.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpRemoteComponentName_Type(AsciiString):
    """Custom type mcsMgrDprsMcsEpGEpRemoteComponentName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_McsMgrDprsMcsEpGEpRemoteComponentName_Type.__name__ = "AsciiString"
_McsMgrDprsMcsEpGEpRemoteComponentName_Object = MibTableColumn
mcsMgrDprsMcsEpGEpRemoteComponentName = _McsMgrDprsMcsEpGEpRemoteComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 9),
    _McsMgrDprsMcsEpGEpRemoteComponentName_Type()
)
mcsMgrDprsMcsEpGEpRemoteComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpRemoteComponentName.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpRemoteRoutingId_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpRemoteRoutingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_McsMgrDprsMcsEpGEpRemoteRoutingId_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpRemoteRoutingId_Object = MibTableColumn
mcsMgrDprsMcsEpGEpRemoteRoutingId = _McsMgrDprsMcsEpGEpRemoteRoutingId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 10),
    _McsMgrDprsMcsEpGEpRemoteRoutingId_Type()
)
mcsMgrDprsMcsEpGEpRemoteRoutingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpRemoteRoutingId.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpRemoteModuleId_Type(Unsigned32):
    """Custom type mcsMgrDprsMcsEpGEpRemoteModuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1909),
    )


_McsMgrDprsMcsEpGEpRemoteModuleId_Type.__name__ = "Unsigned32"
_McsMgrDprsMcsEpGEpRemoteModuleId_Object = MibTableColumn
mcsMgrDprsMcsEpGEpRemoteModuleId = _McsMgrDprsMcsEpGEpRemoteModuleId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 11),
    _McsMgrDprsMcsEpGEpRemoteModuleId_Type()
)
mcsMgrDprsMcsEpGEpRemoteModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpRemoteModuleId.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpLastTrConnDiagCode_Type(HexString):
    """Custom type mcsMgrDprsMcsEpGEpLastTrConnDiagCode based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_McsMgrDprsMcsEpGEpLastTrConnDiagCode_Type.__name__ = "HexString"
_McsMgrDprsMcsEpGEpLastTrConnDiagCode_Object = MibTableColumn
mcsMgrDprsMcsEpGEpLastTrConnDiagCode = _McsMgrDprsMcsEpGEpLastTrConnDiagCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 11, 1, 12),
    _McsMgrDprsMcsEpGEpLastTrConnDiagCode_Type()
)
mcsMgrDprsMcsEpGEpLastTrConnDiagCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpLastTrConnDiagCode.setStatus("mandatory")
_McsMgrDprsMcsEpGEpStatsTable_Object = MibTable
mcsMgrDprsMcsEpGEpStatsTable = _McsMgrDprsMcsEpGEpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 12)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpStatsTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpStatsEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpStatsEntry = _McsMgrDprsMcsEpGEpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 12, 1)
)
mcsMgrDprsMcsEpGEpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpStatsEntry.setStatus("mandatory")
_McsMgrDprsMcsEpGEpSetupAttempts_Type = Counter32
_McsMgrDprsMcsEpGEpSetupAttempts_Object = MibTableColumn
mcsMgrDprsMcsEpGEpSetupAttempts = _McsMgrDprsMcsEpGEpSetupAttempts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 12, 1, 1),
    _McsMgrDprsMcsEpGEpSetupAttempts_Type()
)
mcsMgrDprsMcsEpGEpSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpSetupAttempts.setStatus("mandatory")
_McsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Type = Counter32
_McsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Object = MibTableColumn
mcsMgrDprsMcsEpGEpPktDiscErroredFromMcs = _McsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 12, 1, 2),
    _McsMgrDprsMcsEpGEpPktDiscErroredFromMcs_Type()
)
mcsMgrDprsMcsEpGEpPktDiscErroredFromMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktDiscErroredFromMcs.setStatus("mandatory")
_McsMgrDprsMcsEpGEpPktFromMcsTable_Object = MibTable
mcsMgrDprsMcsEpGEpPktFromMcsTable = _McsMgrDprsMcsEpGEpPktFromMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 402)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktFromMcsTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpPktFromMcsEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpPktFromMcsEntry = _McsMgrDprsMcsEpGEpPktFromMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 402, 1)
)
mcsMgrDprsMcsEpGEpPktFromMcsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpPktFromMcsIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktFromMcsEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpPktFromMcsIndex_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpPktFromMcsIndex based on Integer32"""
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


_McsMgrDprsMcsEpGEpPktFromMcsIndex_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpPktFromMcsIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGEpPktFromMcsIndex = _McsMgrDprsMcsEpGEpPktFromMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 402, 1, 1),
    _McsMgrDprsMcsEpGEpPktFromMcsIndex_Type()
)
mcsMgrDprsMcsEpGEpPktFromMcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktFromMcsIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGEpPktFromMcsValue_Type = PassportCounter64
_McsMgrDprsMcsEpGEpPktFromMcsValue_Object = MibTableColumn
mcsMgrDprsMcsEpGEpPktFromMcsValue = _McsMgrDprsMcsEpGEpPktFromMcsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 402, 1, 2),
    _McsMgrDprsMcsEpGEpPktFromMcsValue_Type()
)
mcsMgrDprsMcsEpGEpPktFromMcsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktFromMcsValue.setStatus("mandatory")
_McsMgrDprsMcsEpGEpOctetsFromMcsTable_Object = MibTable
mcsMgrDprsMcsEpGEpOctetsFromMcsTable = _McsMgrDprsMcsEpGEpOctetsFromMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 403)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpOctetsFromMcsTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpOctetsFromMcsEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpOctetsFromMcsEntry = _McsMgrDprsMcsEpGEpOctetsFromMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 403, 1)
)
mcsMgrDprsMcsEpGEpOctetsFromMcsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpOctetsFromMcsIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpOctetsFromMcsEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpOctetsFromMcsIndex_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpOctetsFromMcsIndex based on Integer32"""
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


_McsMgrDprsMcsEpGEpOctetsFromMcsIndex_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpOctetsFromMcsIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGEpOctetsFromMcsIndex = _McsMgrDprsMcsEpGEpOctetsFromMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 403, 1, 1),
    _McsMgrDprsMcsEpGEpOctetsFromMcsIndex_Type()
)
mcsMgrDprsMcsEpGEpOctetsFromMcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpOctetsFromMcsIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGEpOctetsFromMcsValue_Type = PassportCounter64
_McsMgrDprsMcsEpGEpOctetsFromMcsValue_Object = MibTableColumn
mcsMgrDprsMcsEpGEpOctetsFromMcsValue = _McsMgrDprsMcsEpGEpOctetsFromMcsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 403, 1, 2),
    _McsMgrDprsMcsEpGEpOctetsFromMcsValue_Type()
)
mcsMgrDprsMcsEpGEpOctetsFromMcsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpOctetsFromMcsValue.setStatus("mandatory")
_McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable_Object = MibTable
mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable = _McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 404)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable.setStatus("mandatory")
_McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry_Object = MibTableRow
mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry = _McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 404, 1)
)
mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Type(Integer32):
    """Custom type mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex based on Integer32"""
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


_McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Type.__name__ = "Integer32"
_McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Object = MibTableColumn
mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex = _McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 404, 1, 1),
    _McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex_Type()
)
mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex.setStatus("mandatory")
_McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Type = Counter32
_McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Object = MibTableColumn
mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue = _McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 3, 404, 1, 2),
    _McsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue_Type()
)
mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue.setStatus("mandatory")
_McsMgrDprsMcsEpGOperTable_Object = MibTable
mcsMgrDprsMcsEpGOperTable = _McsMgrDprsMcsEpGOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 10)
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGOperTable.setStatus("mandatory")
_McsMgrDprsMcsEpGOperEntry_Object = MibTableRow
mcsMgrDprsMcsEpGOperEntry = _McsMgrDprsMcsEpGOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 10, 1)
)
mcsMgrDprsMcsEpGOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-McsMgrMIB", "mcsMgrIndex"),
    (0, "Nortel-Magellan-Passport-DprsMcsEpMIB", "mcsMgrDprsMcsEpGIndex"),
)
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGOperEntry.setStatus("mandatory")


class _McsMgrDprsMcsEpGRemoteAddress_Type(AsciiString):
    """Custom type mcsMgrDprsMcsEpGRemoteAddress based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 44),
    )


_McsMgrDprsMcsEpGRemoteAddress_Type.__name__ = "AsciiString"
_McsMgrDprsMcsEpGRemoteAddress_Object = MibTableColumn
mcsMgrDprsMcsEpGRemoteAddress = _McsMgrDprsMcsEpGRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 10, 1, 1),
    _McsMgrDprsMcsEpGRemoteAddress_Type()
)
mcsMgrDprsMcsEpGRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGRemoteAddress.setStatus("mandatory")
_McsMgrDprsMcsEpGAssociatedEpGroupName_Type = RowPointer
_McsMgrDprsMcsEpGAssociatedEpGroupName_Object = MibTableColumn
mcsMgrDprsMcsEpGAssociatedEpGroupName = _McsMgrDprsMcsEpGAssociatedEpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 122, 2, 10, 1, 2),
    _McsMgrDprsMcsEpGAssociatedEpGroupName_Type()
)
mcsMgrDprsMcsEpGAssociatedEpGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcsMgrDprsMcsEpGAssociatedEpGroupName.setStatus("mandatory")
_DprsMcsEpMIB_ObjectIdentity = ObjectIdentity
dprsMcsEpMIB = _DprsMcsEpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125)
)
_DprsMcsEpGroup_ObjectIdentity = ObjectIdentity
dprsMcsEpGroup = _DprsMcsEpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 1)
)
_DprsMcsEpGroupBE_ObjectIdentity = ObjectIdentity
dprsMcsEpGroupBE = _DprsMcsEpGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 1, 5)
)
_DprsMcsEpGroupBE01_ObjectIdentity = ObjectIdentity
dprsMcsEpGroupBE01 = _DprsMcsEpGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 1, 5, 2)
)
_DprsMcsEpGroupBE01A_ObjectIdentity = ObjectIdentity
dprsMcsEpGroupBE01A = _DprsMcsEpGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 1, 5, 2, 2)
)
_DprsMcsEpCapabilities_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilities = _DprsMcsEpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 3)
)
_DprsMcsEpCapabilitiesBE_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilitiesBE = _DprsMcsEpCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 3, 5)
)
_DprsMcsEpCapabilitiesBE01_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilitiesBE01 = _DprsMcsEpCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 3, 5, 2)
)
_DprsMcsEpCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
dprsMcsEpCapabilitiesBE01A = _DprsMcsEpCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 125, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-DprsMcsEpMIB",
    **{"mcsMgrDprsMcsEpG": mcsMgrDprsMcsEpG,
       "mcsMgrDprsMcsEpGRowStatusTable": mcsMgrDprsMcsEpGRowStatusTable,
       "mcsMgrDprsMcsEpGRowStatusEntry": mcsMgrDprsMcsEpGRowStatusEntry,
       "mcsMgrDprsMcsEpGRowStatus": mcsMgrDprsMcsEpGRowStatus,
       "mcsMgrDprsMcsEpGComponentName": mcsMgrDprsMcsEpGComponentName,
       "mcsMgrDprsMcsEpGStorageType": mcsMgrDprsMcsEpGStorageType,
       "mcsMgrDprsMcsEpGIndex": mcsMgrDprsMcsEpGIndex,
       "mcsMgrDprsMcsEpGAddr": mcsMgrDprsMcsEpGAddr,
       "mcsMgrDprsMcsEpGAddrRowStatusTable": mcsMgrDprsMcsEpGAddrRowStatusTable,
       "mcsMgrDprsMcsEpGAddrRowStatusEntry": mcsMgrDprsMcsEpGAddrRowStatusEntry,
       "mcsMgrDprsMcsEpGAddrRowStatus": mcsMgrDprsMcsEpGAddrRowStatus,
       "mcsMgrDprsMcsEpGAddrComponentName": mcsMgrDprsMcsEpGAddrComponentName,
       "mcsMgrDprsMcsEpGAddrStorageType": mcsMgrDprsMcsEpGAddrStorageType,
       "mcsMgrDprsMcsEpGAddrIndex": mcsMgrDprsMcsEpGAddrIndex,
       "mcsMgrDprsMcsEpGAddrProvTable": mcsMgrDprsMcsEpGAddrProvTable,
       "mcsMgrDprsMcsEpGAddrProvEntry": mcsMgrDprsMcsEpGAddrProvEntry,
       "mcsMgrDprsMcsEpGAddrRemoteAddress": mcsMgrDprsMcsEpGAddrRemoteAddress,
       "mcsMgrDprsMcsEpGAddrCommentText": mcsMgrDprsMcsEpGAddrCommentText,
       "mcsMgrDprsMcsEpGEp": mcsMgrDprsMcsEpGEp,
       "mcsMgrDprsMcsEpGEpRowStatusTable": mcsMgrDprsMcsEpGEpRowStatusTable,
       "mcsMgrDprsMcsEpGEpRowStatusEntry": mcsMgrDprsMcsEpGEpRowStatusEntry,
       "mcsMgrDprsMcsEpGEpRowStatus": mcsMgrDprsMcsEpGEpRowStatus,
       "mcsMgrDprsMcsEpGEpComponentName": mcsMgrDprsMcsEpGEpComponentName,
       "mcsMgrDprsMcsEpGEpStorageType": mcsMgrDprsMcsEpGEpStorageType,
       "mcsMgrDprsMcsEpGEpIndex": mcsMgrDprsMcsEpGEpIndex,
       "mcsMgrDprsMcsEpGEpEpD": mcsMgrDprsMcsEpGEpEpD,
       "mcsMgrDprsMcsEpGEpEpDRowStatusTable": mcsMgrDprsMcsEpGEpEpDRowStatusTable,
       "mcsMgrDprsMcsEpGEpEpDRowStatusEntry": mcsMgrDprsMcsEpGEpEpDRowStatusEntry,
       "mcsMgrDprsMcsEpGEpEpDRowStatus": mcsMgrDprsMcsEpGEpEpDRowStatus,
       "mcsMgrDprsMcsEpGEpEpDComponentName": mcsMgrDprsMcsEpGEpEpDComponentName,
       "mcsMgrDprsMcsEpGEpEpDStorageType": mcsMgrDprsMcsEpGEpEpDStorageType,
       "mcsMgrDprsMcsEpGEpEpDIndex": mcsMgrDprsMcsEpGEpEpDIndex,
       "mcsMgrDprsMcsEpGEpEpDProvTable": mcsMgrDprsMcsEpGEpEpDProvTable,
       "mcsMgrDprsMcsEpGEpEpDProvEntry": mcsMgrDprsMcsEpGEpEpDProvEntry,
       "mcsMgrDprsMcsEpGEpEpDBandwidth": mcsMgrDprsMcsEpGEpEpDBandwidth,
       "mcsMgrDprsMcsEpGEpEpDConnectionTransferPriority": mcsMgrDprsMcsEpGEpEpDConnectionTransferPriority,
       "mcsMgrDprsMcsEpGEpEpDTransportConnectionPreference": mcsMgrDprsMcsEpGEpEpDTransportConnectionPreference,
       "mcsMgrDprsMcsEpGEpEpDProfile": mcsMgrDprsMcsEpGEpEpDProfile,
       "mcsMgrDprsMcsEpGEpEpDPorsManualPath": mcsMgrDprsMcsEpGEpEpDPorsManualPath,
       "mcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities": mcsMgrDprsMcsEpGEpEpDSupportedTransferPriorities,
       "mcsMgrDprsMcsEpGEpAtmCon": mcsMgrDprsMcsEpGEpAtmCon,
       "mcsMgrDprsMcsEpGEpAtmConRowStatusTable": mcsMgrDprsMcsEpGEpAtmConRowStatusTable,
       "mcsMgrDprsMcsEpGEpAtmConRowStatusEntry": mcsMgrDprsMcsEpGEpAtmConRowStatusEntry,
       "mcsMgrDprsMcsEpGEpAtmConRowStatus": mcsMgrDprsMcsEpGEpAtmConRowStatus,
       "mcsMgrDprsMcsEpGEpAtmConComponentName": mcsMgrDprsMcsEpGEpAtmConComponentName,
       "mcsMgrDprsMcsEpGEpAtmConStorageType": mcsMgrDprsMcsEpGEpAtmConStorageType,
       "mcsMgrDprsMcsEpGEpAtmConIndex": mcsMgrDprsMcsEpGEpAtmConIndex,
       "mcsMgrDprsMcsEpGEpAtmConOperTable": mcsMgrDprsMcsEpGEpAtmConOperTable,
       "mcsMgrDprsMcsEpGEpAtmConOperEntry": mcsMgrDprsMcsEpGEpAtmConOperEntry,
       "mcsMgrDprsMcsEpGEpAtmConNextHop": mcsMgrDprsMcsEpGEpAtmConNextHop,
       "mcsMgrDprsMcsEpGEpLCo": mcsMgrDprsMcsEpGEpLCo,
       "mcsMgrDprsMcsEpGEpLCoRowStatusTable": mcsMgrDprsMcsEpGEpLCoRowStatusTable,
       "mcsMgrDprsMcsEpGEpLCoRowStatusEntry": mcsMgrDprsMcsEpGEpLCoRowStatusEntry,
       "mcsMgrDprsMcsEpGEpLCoRowStatus": mcsMgrDprsMcsEpGEpLCoRowStatus,
       "mcsMgrDprsMcsEpGEpLCoComponentName": mcsMgrDprsMcsEpGEpLCoComponentName,
       "mcsMgrDprsMcsEpGEpLCoStorageType": mcsMgrDprsMcsEpGEpLCoStorageType,
       "mcsMgrDprsMcsEpGEpLCoIndex": mcsMgrDprsMcsEpGEpLCoIndex,
       "mcsMgrDprsMcsEpGEpLCoPathDataTable": mcsMgrDprsMcsEpGEpLCoPathDataTable,
       "mcsMgrDprsMcsEpGEpLCoPathDataEntry": mcsMgrDprsMcsEpGEpLCoPathDataEntry,
       "mcsMgrDprsMcsEpGEpLCoState": mcsMgrDprsMcsEpGEpLCoState,
       "mcsMgrDprsMcsEpGEpLCoOverrideRemoteName": mcsMgrDprsMcsEpGEpLCoOverrideRemoteName,
       "mcsMgrDprsMcsEpGEpLCoEnd": mcsMgrDprsMcsEpGEpLCoEnd,
       "mcsMgrDprsMcsEpGEpLCoCostMetric": mcsMgrDprsMcsEpGEpLCoCostMetric,
       "mcsMgrDprsMcsEpGEpLCoDelayMetric": mcsMgrDprsMcsEpGEpLCoDelayMetric,
       "mcsMgrDprsMcsEpGEpLCoRoundTripDelay": mcsMgrDprsMcsEpGEpLCoRoundTripDelay,
       "mcsMgrDprsMcsEpGEpLCoSetupPriority": mcsMgrDprsMcsEpGEpLCoSetupPriority,
       "mcsMgrDprsMcsEpGEpLCoHoldingPriority": mcsMgrDprsMcsEpGEpLCoHoldingPriority,
       "mcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth": mcsMgrDprsMcsEpGEpLCoRequiredTxBandwidth,
       "mcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth": mcsMgrDprsMcsEpGEpLCoRequiredRxBandwidth,
       "mcsMgrDprsMcsEpGEpLCoRequiredTrafficType": mcsMgrDprsMcsEpGEpLCoRequiredTrafficType,
       "mcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes": mcsMgrDprsMcsEpGEpLCoPermittedTrunkTypes,
       "mcsMgrDprsMcsEpGEpLCoRequiredSecurity": mcsMgrDprsMcsEpGEpLCoRequiredSecurity,
       "mcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter": mcsMgrDprsMcsEpGEpLCoRequiredCustomerParameter,
       "mcsMgrDprsMcsEpGEpLCoEmissionPriority": mcsMgrDprsMcsEpGEpLCoEmissionPriority,
       "mcsMgrDprsMcsEpGEpLCoDiscardPriority": mcsMgrDprsMcsEpGEpLCoDiscardPriority,
       "mcsMgrDprsMcsEpGEpLCoPathType": mcsMgrDprsMcsEpGEpLCoPathType,
       "mcsMgrDprsMcsEpGEpLCoRetryCount": mcsMgrDprsMcsEpGEpLCoRetryCount,
       "mcsMgrDprsMcsEpGEpLCoPathFailureCount": mcsMgrDprsMcsEpGEpLCoPathFailureCount,
       "mcsMgrDprsMcsEpGEpLCoReasonForNoRoute": mcsMgrDprsMcsEpGEpLCoReasonForNoRoute,
       "mcsMgrDprsMcsEpGEpLCoLastTearDownReason": mcsMgrDprsMcsEpGEpLCoLastTearDownReason,
       "mcsMgrDprsMcsEpGEpLCoPathFailureAction": mcsMgrDprsMcsEpGEpLCoPathFailureAction,
       "mcsMgrDprsMcsEpGEpLCoBumpPreference": mcsMgrDprsMcsEpGEpLCoBumpPreference,
       "mcsMgrDprsMcsEpGEpLCoOptimization": mcsMgrDprsMcsEpGEpLCoOptimization,
       "mcsMgrDprsMcsEpGEpLCoPathUpDateTime": mcsMgrDprsMcsEpGEpLCoPathUpDateTime,
       "mcsMgrDprsMcsEpGEpLCoStatsTable": mcsMgrDprsMcsEpGEpLCoStatsTable,
       "mcsMgrDprsMcsEpGEpLCoStatsEntry": mcsMgrDprsMcsEpGEpLCoStatsEntry,
       "mcsMgrDprsMcsEpGEpLCoPktsToNetwork": mcsMgrDprsMcsEpGEpLCoPktsToNetwork,
       "mcsMgrDprsMcsEpGEpLCoBytesToNetwork": mcsMgrDprsMcsEpGEpLCoBytesToNetwork,
       "mcsMgrDprsMcsEpGEpLCoPktsFromNetwork": mcsMgrDprsMcsEpGEpLCoPktsFromNetwork,
       "mcsMgrDprsMcsEpGEpLCoBytesFromNetwork": mcsMgrDprsMcsEpGEpLCoBytesFromNetwork,
       "mcsMgrDprsMcsEpGEpLCoPathTable": mcsMgrDprsMcsEpGEpLCoPathTable,
       "mcsMgrDprsMcsEpGEpLCoPathEntry": mcsMgrDprsMcsEpGEpLCoPathEntry,
       "mcsMgrDprsMcsEpGEpLCoPathValue": mcsMgrDprsMcsEpGEpLCoPathValue,
       "mcsMgrDprsMcsEpGEpStateTable": mcsMgrDprsMcsEpGEpStateTable,
       "mcsMgrDprsMcsEpGEpStateEntry": mcsMgrDprsMcsEpGEpStateEntry,
       "mcsMgrDprsMcsEpGEpAdminState": mcsMgrDprsMcsEpGEpAdminState,
       "mcsMgrDprsMcsEpGEpOperationalState": mcsMgrDprsMcsEpGEpOperationalState,
       "mcsMgrDprsMcsEpGEpUsageState": mcsMgrDprsMcsEpGEpUsageState,
       "mcsMgrDprsMcsEpGEpAvailabilityStatus": mcsMgrDprsMcsEpGEpAvailabilityStatus,
       "mcsMgrDprsMcsEpGEpProceduralStatus": mcsMgrDprsMcsEpGEpProceduralStatus,
       "mcsMgrDprsMcsEpGEpControlStatus": mcsMgrDprsMcsEpGEpControlStatus,
       "mcsMgrDprsMcsEpGEpAlarmStatus": mcsMgrDprsMcsEpGEpAlarmStatus,
       "mcsMgrDprsMcsEpGEpStandbyStatus": mcsMgrDprsMcsEpGEpStandbyStatus,
       "mcsMgrDprsMcsEpGEpUnknownStatus": mcsMgrDprsMcsEpGEpUnknownStatus,
       "mcsMgrDprsMcsEpGEpOperTable": mcsMgrDprsMcsEpGEpOperTable,
       "mcsMgrDprsMcsEpGEpOperEntry": mcsMgrDprsMcsEpGEpOperEntry,
       "mcsMgrDprsMcsEpGEpLastTransportConnectionClearCause": mcsMgrDprsMcsEpGEpLastTransportConnectionClearCause,
       "mcsMgrDprsMcsEpGEpType": mcsMgrDprsMcsEpGEpType,
       "mcsMgrDprsMcsEpGEpSupportedTransferPriorities": mcsMgrDprsMcsEpGEpSupportedTransferPriorities,
       "mcsMgrDprsMcsEpGEpConnectionTransferPriority": mcsMgrDprsMcsEpGEpConnectionTransferPriority,
       "mcsMgrDprsMcsEpGEpServiceCategory": mcsMgrDprsMcsEpGEpServiceCategory,
       "mcsMgrDprsMcsEpGEpBandwidth": mcsMgrDprsMcsEpGEpBandwidth,
       "mcsMgrDprsMcsEpGEpRemoteComponentName": mcsMgrDprsMcsEpGEpRemoteComponentName,
       "mcsMgrDprsMcsEpGEpRemoteRoutingId": mcsMgrDprsMcsEpGEpRemoteRoutingId,
       "mcsMgrDprsMcsEpGEpRemoteModuleId": mcsMgrDprsMcsEpGEpRemoteModuleId,
       "mcsMgrDprsMcsEpGEpLastTrConnDiagCode": mcsMgrDprsMcsEpGEpLastTrConnDiagCode,
       "mcsMgrDprsMcsEpGEpStatsTable": mcsMgrDprsMcsEpGEpStatsTable,
       "mcsMgrDprsMcsEpGEpStatsEntry": mcsMgrDprsMcsEpGEpStatsEntry,
       "mcsMgrDprsMcsEpGEpSetupAttempts": mcsMgrDprsMcsEpGEpSetupAttempts,
       "mcsMgrDprsMcsEpGEpPktDiscErroredFromMcs": mcsMgrDprsMcsEpGEpPktDiscErroredFromMcs,
       "mcsMgrDprsMcsEpGEpPktFromMcsTable": mcsMgrDprsMcsEpGEpPktFromMcsTable,
       "mcsMgrDprsMcsEpGEpPktFromMcsEntry": mcsMgrDprsMcsEpGEpPktFromMcsEntry,
       "mcsMgrDprsMcsEpGEpPktFromMcsIndex": mcsMgrDprsMcsEpGEpPktFromMcsIndex,
       "mcsMgrDprsMcsEpGEpPktFromMcsValue": mcsMgrDprsMcsEpGEpPktFromMcsValue,
       "mcsMgrDprsMcsEpGEpOctetsFromMcsTable": mcsMgrDprsMcsEpGEpOctetsFromMcsTable,
       "mcsMgrDprsMcsEpGEpOctetsFromMcsEntry": mcsMgrDprsMcsEpGEpOctetsFromMcsEntry,
       "mcsMgrDprsMcsEpGEpOctetsFromMcsIndex": mcsMgrDprsMcsEpGEpOctetsFromMcsIndex,
       "mcsMgrDprsMcsEpGEpOctetsFromMcsValue": mcsMgrDprsMcsEpGEpOctetsFromMcsValue,
       "mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable": mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsTable,
       "mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry": mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsEntry,
       "mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex": mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsIndex,
       "mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue": mcsMgrDprsMcsEpGEpPktDiscCongestedFromMcsValue,
       "mcsMgrDprsMcsEpGOperTable": mcsMgrDprsMcsEpGOperTable,
       "mcsMgrDprsMcsEpGOperEntry": mcsMgrDprsMcsEpGOperEntry,
       "mcsMgrDprsMcsEpGRemoteAddress": mcsMgrDprsMcsEpGRemoteAddress,
       "mcsMgrDprsMcsEpGAssociatedEpGroupName": mcsMgrDprsMcsEpGAssociatedEpGroupName,
       "dprsMcsEpMIB": dprsMcsEpMIB,
       "dprsMcsEpGroup": dprsMcsEpGroup,
       "dprsMcsEpGroupBE": dprsMcsEpGroupBE,
       "dprsMcsEpGroupBE01": dprsMcsEpGroupBE01,
       "dprsMcsEpGroupBE01A": dprsMcsEpGroupBE01A,
       "dprsMcsEpCapabilities": dprsMcsEpCapabilities,
       "dprsMcsEpCapabilitiesBE": dprsMcsEpCapabilitiesBE,
       "dprsMcsEpCapabilitiesBE01": dprsMcsEpCapabilitiesBE01,
       "dprsMcsEpCapabilitiesBE01A": dprsMcsEpCapabilitiesBE01A}
)
