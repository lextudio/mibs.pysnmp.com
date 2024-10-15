# SNMP MIB module (Nortel-Magellan-Passport-VcTesterMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VcTesterMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:32 2024
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

(DisplayString,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 HexString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
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

_Vct_ObjectIdentity = ObjectIdentity
vct = _Vct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130)
)
_VctRowStatusTable_Object = MibTable
vctRowStatusTable = _VctRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 1)
)
if mibBuilder.loadTexts:
    vctRowStatusTable.setStatus("mandatory")
_VctRowStatusEntry_Object = MibTableRow
vctRowStatusEntry = _VctRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 1, 1)
)
vctRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
)
if mibBuilder.loadTexts:
    vctRowStatusEntry.setStatus("mandatory")
_VctRowStatus_Type = RowStatus
_VctRowStatus_Object = MibTableColumn
vctRowStatus = _VctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 1, 1, 1),
    _VctRowStatus_Type()
)
vctRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctRowStatus.setStatus("mandatory")
_VctComponentName_Type = DisplayString
_VctComponentName_Object = MibTableColumn
vctComponentName = _VctComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 1, 1, 2),
    _VctComponentName_Type()
)
vctComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctComponentName.setStatus("mandatory")
_VctStorageType_Type = StorageType
_VctStorageType_Object = MibTableColumn
vctStorageType = _VctStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 1, 1, 4),
    _VctStorageType_Type()
)
vctStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctStorageType.setStatus("mandatory")


class _VctIndex_Type(Integer32):
    """Custom type vctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VctIndex_Type.__name__ = "Integer32"
_VctIndex_Object = MibTableColumn
vctIndex = _VctIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 1, 1, 10),
    _VctIndex_Type()
)
vctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctIndex.setStatus("mandatory")
_VctDna_ObjectIdentity = ObjectIdentity
vctDna = _VctDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2)
)
_VctDnaRowStatusTable_Object = MibTable
vctDnaRowStatusTable = _VctDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 1)
)
if mibBuilder.loadTexts:
    vctDnaRowStatusTable.setStatus("mandatory")
_VctDnaRowStatusEntry_Object = MibTableRow
vctDnaRowStatusEntry = _VctDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 1, 1)
)
vctDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
)
if mibBuilder.loadTexts:
    vctDnaRowStatusEntry.setStatus("mandatory")
_VctDnaRowStatus_Type = RowStatus
_VctDnaRowStatus_Object = MibTableColumn
vctDnaRowStatus = _VctDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 1, 1, 1),
    _VctDnaRowStatus_Type()
)
vctDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaRowStatus.setStatus("mandatory")
_VctDnaComponentName_Type = DisplayString
_VctDnaComponentName_Object = MibTableColumn
vctDnaComponentName = _VctDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 1, 1, 2),
    _VctDnaComponentName_Type()
)
vctDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaComponentName.setStatus("mandatory")
_VctDnaStorageType_Type = StorageType
_VctDnaStorageType_Object = MibTableColumn
vctDnaStorageType = _VctDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 1, 1, 4),
    _VctDnaStorageType_Type()
)
vctDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaStorageType.setStatus("mandatory")
_VctDnaIndex_Type = NonReplicated
_VctDnaIndex_Object = MibTableColumn
vctDnaIndex = _VctDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 1, 1, 10),
    _VctDnaIndex_Type()
)
vctDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDnaIndex.setStatus("mandatory")
_VctDnaCug_ObjectIdentity = ObjectIdentity
vctDnaCug = _VctDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2)
)
_VctDnaCugRowStatusTable_Object = MibTable
vctDnaCugRowStatusTable = _VctDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vctDnaCugRowStatusTable.setStatus("mandatory")
_VctDnaCugRowStatusEntry_Object = MibTableRow
vctDnaCugRowStatusEntry = _VctDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 1, 1)
)
vctDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaCugIndex"),
)
if mibBuilder.loadTexts:
    vctDnaCugRowStatusEntry.setStatus("mandatory")
_VctDnaCugRowStatus_Type = RowStatus
_VctDnaCugRowStatus_Object = MibTableColumn
vctDnaCugRowStatus = _VctDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 1, 1, 1),
    _VctDnaCugRowStatus_Type()
)
vctDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugRowStatus.setStatus("mandatory")
_VctDnaCugComponentName_Type = DisplayString
_VctDnaCugComponentName_Object = MibTableColumn
vctDnaCugComponentName = _VctDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 1, 1, 2),
    _VctDnaCugComponentName_Type()
)
vctDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaCugComponentName.setStatus("mandatory")
_VctDnaCugStorageType_Type = StorageType
_VctDnaCugStorageType_Object = MibTableColumn
vctDnaCugStorageType = _VctDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 1, 1, 4),
    _VctDnaCugStorageType_Type()
)
vctDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaCugStorageType.setStatus("mandatory")


class _VctDnaCugIndex_Type(Integer32):
    """Custom type vctDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctDnaCugIndex_Type.__name__ = "Integer32"
_VctDnaCugIndex_Object = MibTableColumn
vctDnaCugIndex = _VctDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 1, 1, 10),
    _VctDnaCugIndex_Type()
)
vctDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDnaCugIndex.setStatus("mandatory")
_VctDnaCugCugOptionsTable_Object = MibTable
vctDnaCugCugOptionsTable = _VctDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vctDnaCugCugOptionsTable.setStatus("mandatory")
_VctDnaCugCugOptionsEntry_Object = MibTableRow
vctDnaCugCugOptionsEntry = _VctDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1)
)
vctDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaCugIndex"),
)
if mibBuilder.loadTexts:
    vctDnaCugCugOptionsEntry.setStatus("mandatory")


class _VctDnaCugType_Type(Integer32):
    """Custom type vctDnaCugType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("international", 1),
          ("national", 0))
    )


_VctDnaCugType_Type.__name__ = "Integer32"
_VctDnaCugType_Object = MibTableColumn
vctDnaCugType = _VctDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1, 1),
    _VctDnaCugType_Type()
)
vctDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugType.setStatus("mandatory")


class _VctDnaCugDnic_Type(DigitString):
    """Custom type vctDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VctDnaCugDnic_Type.__name__ = "DigitString"
_VctDnaCugDnic_Object = MibTableColumn
vctDnaCugDnic = _VctDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1, 2),
    _VctDnaCugDnic_Type()
)
vctDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugDnic.setStatus("mandatory")


class _VctDnaCugInterlockCode_Type(Unsigned32):
    """Custom type vctDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VctDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_VctDnaCugInterlockCode_Object = MibTableColumn
vctDnaCugInterlockCode = _VctDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1, 3),
    _VctDnaCugInterlockCode_Type()
)
vctDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugInterlockCode.setStatus("mandatory")


class _VctDnaCugPreferential_Type(Integer32):
    """Custom type vctDnaCugPreferential based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaCugPreferential_Type.__name__ = "Integer32"
_VctDnaCugPreferential_Object = MibTableColumn
vctDnaCugPreferential = _VctDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1, 4),
    _VctDnaCugPreferential_Type()
)
vctDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugPreferential.setStatus("mandatory")


class _VctDnaCugOutCalls_Type(Integer32):
    """Custom type vctDnaCugOutCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaCugOutCalls_Type.__name__ = "Integer32"
_VctDnaCugOutCalls_Object = MibTableColumn
vctDnaCugOutCalls = _VctDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1, 5),
    _VctDnaCugOutCalls_Type()
)
vctDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugOutCalls.setStatus("mandatory")


class _VctDnaCugIncCalls_Type(Integer32):
    """Custom type vctDnaCugIncCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaCugIncCalls_Type.__name__ = "Integer32"
_VctDnaCugIncCalls_Object = MibTableColumn
vctDnaCugIncCalls = _VctDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1, 6),
    _VctDnaCugIncCalls_Type()
)
vctDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugIncCalls.setStatus("mandatory")


class _VctDnaCugPrivileged_Type(Integer32):
    """Custom type vctDnaCugPrivileged based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaCugPrivileged_Type.__name__ = "Integer32"
_VctDnaCugPrivileged_Object = MibTableColumn
vctDnaCugPrivileged = _VctDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 2, 10, 1, 7),
    _VctDnaCugPrivileged_Type()
)
vctDnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugPrivileged.setStatus("mandatory")
_VctDnaHgM_ObjectIdentity = ObjectIdentity
vctDnaHgM = _VctDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3)
)
_VctDnaHgMRowStatusTable_Object = MibTable
vctDnaHgMRowStatusTable = _VctDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vctDnaHgMRowStatusTable.setStatus("mandatory")
_VctDnaHgMRowStatusEntry_Object = MibTableRow
vctDnaHgMRowStatusEntry = _VctDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 1, 1)
)
vctDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    vctDnaHgMRowStatusEntry.setStatus("mandatory")
_VctDnaHgMRowStatus_Type = RowStatus
_VctDnaHgMRowStatus_Object = MibTableColumn
vctDnaHgMRowStatus = _VctDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 1, 1, 1),
    _VctDnaHgMRowStatus_Type()
)
vctDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaHgMRowStatus.setStatus("mandatory")
_VctDnaHgMComponentName_Type = DisplayString
_VctDnaHgMComponentName_Object = MibTableColumn
vctDnaHgMComponentName = _VctDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 1, 1, 2),
    _VctDnaHgMComponentName_Type()
)
vctDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaHgMComponentName.setStatus("mandatory")
_VctDnaHgMStorageType_Type = StorageType
_VctDnaHgMStorageType_Object = MibTableColumn
vctDnaHgMStorageType = _VctDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 1, 1, 4),
    _VctDnaHgMStorageType_Type()
)
vctDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaHgMStorageType.setStatus("mandatory")
_VctDnaHgMIndex_Type = NonReplicated
_VctDnaHgMIndex_Object = MibTableColumn
vctDnaHgMIndex = _VctDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 1, 1, 10),
    _VctDnaHgMIndex_Type()
)
vctDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDnaHgMIndex.setStatus("mandatory")
_VctDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
vctDnaHgMHgAddr = _VctDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2)
)
_VctDnaHgMHgAddrRowStatusTable_Object = MibTable
vctDnaHgMHgAddrRowStatusTable = _VctDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_VctDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
vctDnaHgMHgAddrRowStatusEntry = _VctDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 1, 1)
)
vctDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_VctDnaHgMHgAddrRowStatus_Type = RowStatus
_VctDnaHgMHgAddrRowStatus_Object = MibTableColumn
vctDnaHgMHgAddrRowStatus = _VctDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 1, 1, 1),
    _VctDnaHgMHgAddrRowStatus_Type()
)
vctDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrRowStatus.setStatus("mandatory")
_VctDnaHgMHgAddrComponentName_Type = DisplayString
_VctDnaHgMHgAddrComponentName_Object = MibTableColumn
vctDnaHgMHgAddrComponentName = _VctDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 1, 1, 2),
    _VctDnaHgMHgAddrComponentName_Type()
)
vctDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrComponentName.setStatus("mandatory")
_VctDnaHgMHgAddrStorageType_Type = StorageType
_VctDnaHgMHgAddrStorageType_Object = MibTableColumn
vctDnaHgMHgAddrStorageType = _VctDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 1, 1, 4),
    _VctDnaHgMHgAddrStorageType_Type()
)
vctDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrStorageType.setStatus("mandatory")


class _VctDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type vctDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_VctDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_VctDnaHgMHgAddrIndex_Object = MibTableColumn
vctDnaHgMHgAddrIndex = _VctDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 1, 1, 10),
    _VctDnaHgMHgAddrIndex_Type()
)
vctDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrIndex.setStatus("mandatory")
_VctDnaHgMHgAddrAddrTable_Object = MibTable
vctDnaHgMHgAddrAddrTable = _VctDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrAddrTable.setStatus("mandatory")
_VctDnaHgMHgAddrAddrEntry_Object = MibTableRow
vctDnaHgMHgAddrAddrEntry = _VctDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 10, 1)
)
vctDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _VctDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type vctDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_VctDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
vctDnaHgMHgAddrNumberingPlanIndicator = _VctDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 10, 1, 1),
    _VctDnaHgMHgAddrNumberingPlanIndicator_Type()
)
vctDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _VctDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type vctDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VctDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_VctDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
vctDnaHgMHgAddrDataNetworkAddress = _VctDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 2, 10, 1, 2),
    _VctDnaHgMHgAddrDataNetworkAddress_Type()
)
vctDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_VctDnaHgMIfTable_Object = MibTable
vctDnaHgMIfTable = _VctDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 10)
)
if mibBuilder.loadTexts:
    vctDnaHgMIfTable.setStatus("mandatory")
_VctDnaHgMIfEntry_Object = MibTableRow
vctDnaHgMIfEntry = _VctDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 10, 1)
)
vctDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    vctDnaHgMIfEntry.setStatus("mandatory")


class _VctDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type vctDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_VctDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
vctDnaHgMAvailabilityUpdateThreshold = _VctDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 10, 1, 1),
    _VctDnaHgMAvailabilityUpdateThreshold_Type()
)
vctDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_VctDnaHgMOpTable_Object = MibTable
vctDnaHgMOpTable = _VctDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 11)
)
if mibBuilder.loadTexts:
    vctDnaHgMOpTable.setStatus("mandatory")
_VctDnaHgMOpEntry_Object = MibTableRow
vctDnaHgMOpEntry = _VctDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 11, 1)
)
vctDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    vctDnaHgMOpEntry.setStatus("mandatory")


class _VctDnaHgMMaxAvailableChannels_Type(Unsigned32):
    """Custom type vctDnaHgMMaxAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctDnaHgMMaxAvailableChannels_Type.__name__ = "Unsigned32"
_VctDnaHgMMaxAvailableChannels_Object = MibTableColumn
vctDnaHgMMaxAvailableChannels = _VctDnaHgMMaxAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 11, 1, 1),
    _VctDnaHgMMaxAvailableChannels_Type()
)
vctDnaHgMMaxAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaHgMMaxAvailableChannels.setStatus("mandatory")


class _VctDnaHgMAvailableChannels_Type(Unsigned32):
    """Custom type vctDnaHgMAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctDnaHgMAvailableChannels_Type.__name__ = "Unsigned32"
_VctDnaHgMAvailableChannels_Object = MibTableColumn
vctDnaHgMAvailableChannels = _VctDnaHgMAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 11, 1, 2),
    _VctDnaHgMAvailableChannels_Type()
)
vctDnaHgMAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaHgMAvailableChannels.setStatus("mandatory")


class _VctDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type vctDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4096, 4096),
    )


_VctDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_VctDnaHgMAvailabilityDelta_Object = MibTableColumn
vctDnaHgMAvailabilityDelta = _VctDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 3, 11, 1, 3),
    _VctDnaHgMAvailabilityDelta_Type()
)
vctDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDnaHgMAvailabilityDelta.setStatus("mandatory")
_VctDnaAddressTable_Object = MibTable
vctDnaAddressTable = _VctDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 10)
)
if mibBuilder.loadTexts:
    vctDnaAddressTable.setStatus("mandatory")
_VctDnaAddressEntry_Object = MibTableRow
vctDnaAddressEntry = _VctDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 10, 1)
)
vctDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
)
if mibBuilder.loadTexts:
    vctDnaAddressEntry.setStatus("mandatory")


class _VctDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type vctDnaNumberingPlanIndicator based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_VctDnaNumberingPlanIndicator_Object = MibTableColumn
vctDnaNumberingPlanIndicator = _VctDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 10, 1, 1),
    _VctDnaNumberingPlanIndicator_Type()
)
vctDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaNumberingPlanIndicator.setStatus("mandatory")


class _VctDnaDataNetworkAddress_Type(DigitString):
    """Custom type vctDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VctDnaDataNetworkAddress_Type.__name__ = "DigitString"
_VctDnaDataNetworkAddress_Object = MibTableColumn
vctDnaDataNetworkAddress = _VctDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 10, 1, 2),
    _VctDnaDataNetworkAddress_Type()
)
vctDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDataNetworkAddress.setStatus("mandatory")
_VctDnaOutgoingOptionsTable_Object = MibTable
vctDnaOutgoingOptionsTable = _VctDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11)
)
if mibBuilder.loadTexts:
    vctDnaOutgoingOptionsTable.setStatus("mandatory")
_VctDnaOutgoingOptionsEntry_Object = MibTableRow
vctDnaOutgoingOptionsEntry = _VctDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1)
)
vctDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
)
if mibBuilder.loadTexts:
    vctDnaOutgoingOptionsEntry.setStatus("mandatory")


class _VctDnaOutCalls_Type(Integer32):
    """Custom type vctDnaOutCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutCalls_Type.__name__ = "Integer32"
_VctDnaOutCalls_Object = MibTableColumn
vctDnaOutCalls = _VctDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 1),
    _VctDnaOutCalls_Type()
)
vctDnaOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutCalls.setStatus("mandatory")


class _VctDnaOutNormalCharge_Type(Integer32):
    """Custom type vctDnaOutNormalCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutNormalCharge_Type.__name__ = "Integer32"
_VctDnaOutNormalCharge_Object = MibTableColumn
vctDnaOutNormalCharge = _VctDnaOutNormalCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 2),
    _VctDnaOutNormalCharge_Type()
)
vctDnaOutNormalCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutNormalCharge.setStatus("mandatory")


class _VctDnaOutReverseCharge_Type(Integer32):
    """Custom type vctDnaOutReverseCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutReverseCharge_Type.__name__ = "Integer32"
_VctDnaOutReverseCharge_Object = MibTableColumn
vctDnaOutReverseCharge = _VctDnaOutReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 3),
    _VctDnaOutReverseCharge_Type()
)
vctDnaOutReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutReverseCharge.setStatus("mandatory")


class _VctDnaOutForceReverseCharge_Type(Integer32):
    """Custom type vctDnaOutForceReverseCharge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaOutForceReverseCharge_Type.__name__ = "Integer32"
_VctDnaOutForceReverseCharge_Object = MibTableColumn
vctDnaOutForceReverseCharge = _VctDnaOutForceReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 4),
    _VctDnaOutForceReverseCharge_Type()
)
vctDnaOutForceReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutForceReverseCharge.setStatus("mandatory")


class _VctDnaOutNormalPriority_Type(Integer32):
    """Custom type vctDnaOutNormalPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutNormalPriority_Type.__name__ = "Integer32"
_VctDnaOutNormalPriority_Object = MibTableColumn
vctDnaOutNormalPriority = _VctDnaOutNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 5),
    _VctDnaOutNormalPriority_Type()
)
vctDnaOutNormalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutNormalPriority.setStatus("mandatory")


class _VctDnaOutHighPriority_Type(Integer32):
    """Custom type vctDnaOutHighPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutHighPriority_Type.__name__ = "Integer32"
_VctDnaOutHighPriority_Object = MibTableColumn
vctDnaOutHighPriority = _VctDnaOutHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 6),
    _VctDnaOutHighPriority_Type()
)
vctDnaOutHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutHighPriority.setStatus("mandatory")


class _VctDnaOutDefaultPriority_Type(Integer32):
    """Custom type vctDnaOutDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_VctDnaOutDefaultPriority_Type.__name__ = "Integer32"
_VctDnaOutDefaultPriority_Object = MibTableColumn
vctDnaOutDefaultPriority = _VctDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 7),
    _VctDnaOutDefaultPriority_Type()
)
vctDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutDefaultPriority.setStatus("mandatory")


class _VctDnaOutIntl_Type(Integer32):
    """Custom type vctDnaOutIntl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutIntl_Type.__name__ = "Integer32"
_VctDnaOutIntl_Object = MibTableColumn
vctDnaOutIntl = _VctDnaOutIntl_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 8),
    _VctDnaOutIntl_Type()
)
vctDnaOutIntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutIntl.setStatus("mandatory")


class _VctDnaOutFsRestrictedResponse_Type(Integer32):
    """Custom type vctDnaOutFsRestrictedResponse based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutFsRestrictedResponse_Type.__name__ = "Integer32"
_VctDnaOutFsRestrictedResponse_Object = MibTableColumn
vctDnaOutFsRestrictedResponse = _VctDnaOutFsRestrictedResponse_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 9),
    _VctDnaOutFsRestrictedResponse_Type()
)
vctDnaOutFsRestrictedResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutFsRestrictedResponse.setStatus("mandatory")


class _VctDnaOutFsUnrestrictedResponse_Type(Integer32):
    """Custom type vctDnaOutFsUnrestrictedResponse based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutFsUnrestrictedResponse_Type.__name__ = "Integer32"
_VctDnaOutFsUnrestrictedResponse_Object = MibTableColumn
vctDnaOutFsUnrestrictedResponse = _VctDnaOutFsUnrestrictedResponse_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 10),
    _VctDnaOutFsUnrestrictedResponse_Type()
)
vctDnaOutFsUnrestrictedResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutFsUnrestrictedResponse.setStatus("mandatory")


class _VctDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type vctDnaOutDefaultPathSensitivity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("throughput", 0))
    )


_VctDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_VctDnaOutDefaultPathSensitivity_Object = MibTableColumn
vctDnaOutDefaultPathSensitivity = _VctDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 11),
    _VctDnaOutDefaultPathSensitivity_Type()
)
vctDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _VctDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type vctDnaOutPathSensitivityOverRide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_VctDnaOutPathSensitivityOverRide_Object = MibTableColumn
vctDnaOutPathSensitivityOverRide = _VctDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 12),
    _VctDnaOutPathSensitivityOverRide_Type()
)
vctDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _VctDnaOutPathSensitivitySignal_Type(Integer32):
    """Custom type vctDnaOutPathSensitivitySignal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutPathSensitivitySignal_Type.__name__ = "Integer32"
_VctDnaOutPathSensitivitySignal_Object = MibTableColumn
vctDnaOutPathSensitivitySignal = _VctDnaOutPathSensitivitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 13),
    _VctDnaOutPathSensitivitySignal_Type()
)
vctDnaOutPathSensitivitySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutPathSensitivitySignal.setStatus("mandatory")


class _VctDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type vctDnaOutDefaultPathReliability based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_VctDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_VctDnaOutDefaultPathReliability_Object = MibTableColumn
vctDnaOutDefaultPathReliability = _VctDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 14),
    _VctDnaOutDefaultPathReliability_Type()
)
vctDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutDefaultPathReliability.setStatus("mandatory")


class _VctDnaOutPathReliabilityOverRide_Type(Integer32):
    """Custom type vctDnaOutPathReliabilityOverRide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaOutPathReliabilityOverRide_Type.__name__ = "Integer32"
_VctDnaOutPathReliabilityOverRide_Object = MibTableColumn
vctDnaOutPathReliabilityOverRide = _VctDnaOutPathReliabilityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 15),
    _VctDnaOutPathReliabilityOverRide_Type()
)
vctDnaOutPathReliabilityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutPathReliabilityOverRide.setStatus("mandatory")


class _VctDnaOutPathReliabilitySignal_Type(Integer32):
    """Custom type vctDnaOutPathReliabilitySignal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutPathReliabilitySignal_Type.__name__ = "Integer32"
_VctDnaOutPathReliabilitySignal_Object = MibTableColumn
vctDnaOutPathReliabilitySignal = _VctDnaOutPathReliabilitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 16),
    _VctDnaOutPathReliabilitySignal_Type()
)
vctDnaOutPathReliabilitySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutPathReliabilitySignal.setStatus("mandatory")


class _VctDnaOutAccess_Type(Integer32):
    """Custom type vctDnaOutAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaOutAccess_Type.__name__ = "Integer32"
_VctDnaOutAccess_Object = MibTableColumn
vctDnaOutAccess = _VctDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 17),
    _VctDnaOutAccess_Type()
)
vctDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaOutAccess.setStatus("mandatory")


class _VctDnaDefaultTransferPriority_Type(Integer32):
    """Custom type vctDnaDefaultTransferPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_VctDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_VctDnaDefaultTransferPriority_Object = MibTableColumn
vctDnaDefaultTransferPriority = _VctDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 18),
    _VctDnaDefaultTransferPriority_Type()
)
vctDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDefaultTransferPriority.setStatus("mandatory")


class _VctDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type vctDnaTransferPriorityOverRide based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_VctDnaTransferPriorityOverRide_Object = MibTableColumn
vctDnaTransferPriorityOverRide = _VctDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 11, 1, 19),
    _VctDnaTransferPriorityOverRide_Type()
)
vctDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaTransferPriorityOverRide.setStatus("mandatory")
_VctDnaIncomingOptionsTable_Object = MibTable
vctDnaIncomingOptionsTable = _VctDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12)
)
if mibBuilder.loadTexts:
    vctDnaIncomingOptionsTable.setStatus("mandatory")
_VctDnaIncomingOptionsEntry_Object = MibTableRow
vctDnaIncomingOptionsEntry = _VctDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1)
)
vctDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
)
if mibBuilder.loadTexts:
    vctDnaIncomingOptionsEntry.setStatus("mandatory")


class _VctDnaIncCalls_Type(Integer32):
    """Custom type vctDnaIncCalls based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncCalls_Type.__name__ = "Integer32"
_VctDnaIncCalls_Object = MibTableColumn
vctDnaIncCalls = _VctDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 1),
    _VctDnaIncCalls_Type()
)
vctDnaIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncCalls.setStatus("mandatory")


class _VctDnaIncHighPriorityReverseCharge_Type(Integer32):
    """Custom type vctDnaIncHighPriorityReverseCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncHighPriorityReverseCharge_Type.__name__ = "Integer32"
_VctDnaIncHighPriorityReverseCharge_Object = MibTableColumn
vctDnaIncHighPriorityReverseCharge = _VctDnaIncHighPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 2),
    _VctDnaIncHighPriorityReverseCharge_Type()
)
vctDnaIncHighPriorityReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncHighPriorityReverseCharge.setStatus("mandatory")


class _VctDnaIncNormalPriorityReverseCharge_Type(Integer32):
    """Custom type vctDnaIncNormalPriorityReverseCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncNormalPriorityReverseCharge_Type.__name__ = "Integer32"
_VctDnaIncNormalPriorityReverseCharge_Object = MibTableColumn
vctDnaIncNormalPriorityReverseCharge = _VctDnaIncNormalPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 3),
    _VctDnaIncNormalPriorityReverseCharge_Type()
)
vctDnaIncNormalPriorityReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncNormalPriorityReverseCharge.setStatus("mandatory")


class _VctDnaIncIntlNormalCharge_Type(Integer32):
    """Custom type vctDnaIncIntlNormalCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncIntlNormalCharge_Type.__name__ = "Integer32"
_VctDnaIncIntlNormalCharge_Object = MibTableColumn
vctDnaIncIntlNormalCharge = _VctDnaIncIntlNormalCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 4),
    _VctDnaIncIntlNormalCharge_Type()
)
vctDnaIncIntlNormalCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncIntlNormalCharge.setStatus("mandatory")


class _VctDnaIncIntlReverseCharge_Type(Integer32):
    """Custom type vctDnaIncIntlReverseCharge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncIntlReverseCharge_Type.__name__ = "Integer32"
_VctDnaIncIntlReverseCharge_Object = MibTableColumn
vctDnaIncIntlReverseCharge = _VctDnaIncIntlReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 5),
    _VctDnaIncIntlReverseCharge_Type()
)
vctDnaIncIntlReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncIntlReverseCharge.setStatus("mandatory")


class _VctDnaIncFastSelect_Type(Integer32):
    """Custom type vctDnaIncFastSelect based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncFastSelect_Type.__name__ = "Integer32"
_VctDnaIncFastSelect_Object = MibTableColumn
vctDnaIncFastSelect = _VctDnaIncFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 6),
    _VctDnaIncFastSelect_Type()
)
vctDnaIncFastSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncFastSelect.setStatus("mandatory")


class _VctDnaIncSameService_Type(Integer32):
    """Custom type vctDnaIncSameService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncSameService_Type.__name__ = "Integer32"
_VctDnaIncSameService_Object = MibTableColumn
vctDnaIncSameService = _VctDnaIncSameService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 7),
    _VctDnaIncSameService_Type()
)
vctDnaIncSameService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncSameService.setStatus("mandatory")


class _VctDnaIncChargeTransfer_Type(Integer32):
    """Custom type vctDnaIncChargeTransfer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaIncChargeTransfer_Type.__name__ = "Integer32"
_VctDnaIncChargeTransfer_Object = MibTableColumn
vctDnaIncChargeTransfer = _VctDnaIncChargeTransfer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 8),
    _VctDnaIncChargeTransfer_Type()
)
vctDnaIncChargeTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncChargeTransfer.setStatus("mandatory")


class _VctDnaIncAccess_Type(Integer32):
    """Custom type vctDnaIncAccess based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaIncAccess_Type.__name__ = "Integer32"
_VctDnaIncAccess_Object = MibTableColumn
vctDnaIncAccess = _VctDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 12, 1, 9),
    _VctDnaIncAccess_Type()
)
vctDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaIncAccess.setStatus("mandatory")
_VctDnaCallOptionsTable_Object = MibTable
vctDnaCallOptionsTable = _VctDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13)
)
if mibBuilder.loadTexts:
    vctDnaCallOptionsTable.setStatus("mandatory")
_VctDnaCallOptionsEntry_Object = MibTableRow
vctDnaCallOptionsEntry = _VctDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1)
)
vctDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDnaIndex"),
)
if mibBuilder.loadTexts:
    vctDnaCallOptionsEntry.setStatus("mandatory")


class _VctDnaServiceCategory_Type(Integer32):
    """Custom type vctDnaServiceCategory based on Integer32"""
    defaultValue = 30

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
              13,
              14,
              15,
              16,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("api3201", 20),
          ("bsi", 13),
          ("dsp3270", 7),
          ("enhancedIti", 2),
          ("frameRelay", 30),
          ("gasServer", 26),
          ("gsp", 0),
          ("gvcIf", 32),
          ("hdsp3270", 16),
          ("hostIti", 14),
          ("iam", 8),
          ("ici", 6),
          ("ipiVc", 31),
          ("iti", 11),
          ("mlhi", 9),
          ("mlti", 4),
          ("ncs", 3),
          ("offnetNui", 25),
          ("redirectionServ", 23),
          ("sdlc", 21),
          ("sm", 5),
          ("snaMultiHost", 22),
          ("term3270", 10),
          ("trSnaTpad", 24),
          ("vapAgent", 29),
          ("vapServer", 28),
          ("x25", 1),
          ("x75", 15))
    )


_VctDnaServiceCategory_Type.__name__ = "Integer32"
_VctDnaServiceCategory_Object = MibTableColumn
vctDnaServiceCategory = _VctDnaServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 1),
    _VctDnaServiceCategory_Type()
)
vctDnaServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaServiceCategory.setStatus("mandatory")


class _VctDnaPacketSizes_Type(OctetString):
    """Custom type vctDnaPacketSizes based on OctetString"""
    defaultHexValue = "1c00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VctDnaPacketSizes_Type.__name__ = "OctetString"
_VctDnaPacketSizes_Object = MibTableColumn
vctDnaPacketSizes = _VctDnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 2),
    _VctDnaPacketSizes_Type()
)
vctDnaPacketSizes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaPacketSizes.setStatus("mandatory")


class _VctDnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type vctDnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6))
    )


_VctDnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_VctDnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
vctDnaDefaultRecvFrmNetworkPacketSize = _VctDnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 3),
    _VctDnaDefaultRecvFrmNetworkPacketSize_Type()
)
vctDnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _VctDnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type vctDnaDefaultSendToNetworkPacketSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6))
    )


_VctDnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_VctDnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
vctDnaDefaultSendToNetworkPacketSize = _VctDnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 4),
    _VctDnaDefaultSendToNetworkPacketSize_Type()
)
vctDnaDefaultSendToNetworkPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _VctDnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type vctDnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 15),
    )


_VctDnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_VctDnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
vctDnaDefaultRecvFrmNetworkThruputClass = _VctDnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 5),
    _VctDnaDefaultRecvFrmNetworkThruputClass_Type()
)
vctDnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _VctDnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type vctDnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VctDnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_VctDnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
vctDnaDefaultSendToNetworkThruputClass = _VctDnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 6),
    _VctDnaDefaultSendToNetworkThruputClass_Type()
)
vctDnaDefaultSendToNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _VctDnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type vctDnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VctDnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_VctDnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
vctDnaDefaultRecvFrmNetworkWindowSize = _VctDnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 7),
    _VctDnaDefaultRecvFrmNetworkWindowSize_Type()
)
vctDnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _VctDnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type vctDnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VctDnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_VctDnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
vctDnaDefaultSendToNetworkWindowSize = _VctDnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 8),
    _VctDnaDefaultSendToNetworkWindowSize_Type()
)
vctDnaDefaultSendToNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _VctDnaPacketSizeNegotiation_Type(Integer32):
    """Custom type vctDnaPacketSizeNegotiation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 0),
          ("local", 1))
    )


_VctDnaPacketSizeNegotiation_Type.__name__ = "Integer32"
_VctDnaPacketSizeNegotiation_Object = MibTableColumn
vctDnaPacketSizeNegotiation = _VctDnaPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 9),
    _VctDnaPacketSizeNegotiation_Type()
)
vctDnaPacketSizeNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaPacketSizeNegotiation.setStatus("mandatory")


class _VctDnaCugFormat_Type(Integer32):
    """Custom type vctDnaCugFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("basic", 0),
          ("extended", 1))
    )


_VctDnaCugFormat_Type.__name__ = "Integer32"
_VctDnaCugFormat_Object = MibTableColumn
vctDnaCugFormat = _VctDnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 10),
    _VctDnaCugFormat_Type()
)
vctDnaCugFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCugFormat.setStatus("mandatory")


class _VctDnaCug0AsNonCugCall_Type(Integer32):
    """Custom type vctDnaCug0AsNonCugCall based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 0))
    )


_VctDnaCug0AsNonCugCall_Type.__name__ = "Integer32"
_VctDnaCug0AsNonCugCall_Object = MibTableColumn
vctDnaCug0AsNonCugCall = _VctDnaCug0AsNonCugCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 11),
    _VctDnaCug0AsNonCugCall_Type()
)
vctDnaCug0AsNonCugCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaCug0AsNonCugCall.setStatus("mandatory")


class _VctDnaSignalPreferentialCugToLink_Type(Integer32):
    """Custom type vctDnaSignalPreferentialCugToLink based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaSignalPreferentialCugToLink_Type.__name__ = "Integer32"
_VctDnaSignalPreferentialCugToLink_Object = MibTableColumn
vctDnaSignalPreferentialCugToLink = _VctDnaSignalPreferentialCugToLink_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 12),
    _VctDnaSignalPreferentialCugToLink_Type()
)
vctDnaSignalPreferentialCugToLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaSignalPreferentialCugToLink.setStatus("mandatory")


class _VctDnaSignalIntlAddressToLink_Type(Integer32):
    """Custom type vctDnaSignalIntlAddressToLink based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaSignalIntlAddressToLink_Type.__name__ = "Integer32"
_VctDnaSignalIntlAddressToLink_Object = MibTableColumn
vctDnaSignalIntlAddressToLink = _VctDnaSignalIntlAddressToLink_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 13),
    _VctDnaSignalIntlAddressToLink_Type()
)
vctDnaSignalIntlAddressToLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaSignalIntlAddressToLink.setStatus("mandatory")


class _VctDnaFastSelectCallsOnly_Type(Integer32):
    """Custom type vctDnaFastSelectCallsOnly based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaFastSelectCallsOnly_Type.__name__ = "Integer32"
_VctDnaFastSelectCallsOnly_Object = MibTableColumn
vctDnaFastSelectCallsOnly = _VctDnaFastSelectCallsOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 14),
    _VctDnaFastSelectCallsOnly_Type()
)
vctDnaFastSelectCallsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaFastSelectCallsOnly.setStatus("mandatory")


class _VctDnaPreselectRpoa_Type(Integer32):
    """Custom type vctDnaPreselectRpoa based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaPreselectRpoa_Type.__name__ = "Integer32"
_VctDnaPreselectRpoa_Object = MibTableColumn
vctDnaPreselectRpoa = _VctDnaPreselectRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 15),
    _VctDnaPreselectRpoa_Type()
)
vctDnaPreselectRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaPreselectRpoa.setStatus("mandatory")


class _VctDnaAccountClass_Type(Unsigned32):
    """Custom type vctDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctDnaAccountClass_Type.__name__ = "Unsigned32"
_VctDnaAccountClass_Object = MibTableColumn
vctDnaAccountClass = _VctDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 16),
    _VctDnaAccountClass_Type()
)
vctDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaAccountClass.setStatus("mandatory")


class _VctDnaAccountCollection_Type(OctetString):
    """Custom type vctDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VctDnaAccountCollection_Type.__name__ = "OctetString"
_VctDnaAccountCollection_Object = MibTableColumn
vctDnaAccountCollection = _VctDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 17),
    _VctDnaAccountCollection_Type()
)
vctDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaAccountCollection.setStatus("mandatory")


class _VctDnaServiceExchange_Type(Unsigned32):
    """Custom type vctDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctDnaServiceExchange_Type.__name__ = "Unsigned32"
_VctDnaServiceExchange_Object = MibTableColumn
vctDnaServiceExchange = _VctDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 18),
    _VctDnaServiceExchange_Type()
)
vctDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaServiceExchange.setStatus("mandatory")


class _VctDnaEgressAccounting_Type(Integer32):
    """Custom type vctDnaEgressAccounting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDnaEgressAccounting_Type.__name__ = "Integer32"
_VctDnaEgressAccounting_Object = MibTableColumn
vctDnaEgressAccounting = _VctDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 19),
    _VctDnaEgressAccounting_Type()
)
vctDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaEgressAccounting.setStatus("mandatory")


class _VctDnaRpoa_Type(DigitString):
    """Custom type vctDnaRpoa based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VctDnaRpoa_Type.__name__ = "DigitString"
_VctDnaRpoa_Object = MibTableColumn
vctDnaRpoa = _VctDnaRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 20),
    _VctDnaRpoa_Type()
)
vctDnaRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaRpoa.setStatus("mandatory")


class _VctDnaDataPath_Type(Integer32):
    """Custom type vctDnaDataPath based on Integer32"""
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
        *(("dprsMcsFirst", 2),
          ("dprsMcsOnly", 1),
          ("dprsOnly", 0))
    )


_VctDnaDataPath_Type.__name__ = "Integer32"
_VctDnaDataPath_Object = MibTableColumn
vctDnaDataPath = _VctDnaDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 2, 13, 1, 21),
    _VctDnaDataPath_Type()
)
vctDnaDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDnaDataPath.setStatus("mandatory")
_VctDc_ObjectIdentity = ObjectIdentity
vctDc = _VctDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3)
)
_VctDcRowStatusTable_Object = MibTable
vctDcRowStatusTable = _VctDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 1)
)
if mibBuilder.loadTexts:
    vctDcRowStatusTable.setStatus("mandatory")
_VctDcRowStatusEntry_Object = MibTableRow
vctDcRowStatusEntry = _VctDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 1, 1)
)
vctDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcIndex"),
)
if mibBuilder.loadTexts:
    vctDcRowStatusEntry.setStatus("mandatory")
_VctDcRowStatus_Type = RowStatus
_VctDcRowStatus_Object = MibTableColumn
vctDcRowStatus = _VctDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 1, 1, 1),
    _VctDcRowStatus_Type()
)
vctDcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcRowStatus.setStatus("mandatory")
_VctDcComponentName_Type = DisplayString
_VctDcComponentName_Object = MibTableColumn
vctDcComponentName = _VctDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 1, 1, 2),
    _VctDcComponentName_Type()
)
vctDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDcComponentName.setStatus("mandatory")
_VctDcStorageType_Type = StorageType
_VctDcStorageType_Object = MibTableColumn
vctDcStorageType = _VctDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 1, 1, 4),
    _VctDcStorageType_Type()
)
vctDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctDcStorageType.setStatus("mandatory")


class _VctDcIndex_Type(Integer32):
    """Custom type vctDcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VctDcIndex_Type.__name__ = "Integer32"
_VctDcIndex_Object = MibTableColumn
vctDcIndex = _VctDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 1, 1, 10),
    _VctDcIndex_Type()
)
vctDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDcIndex.setStatus("mandatory")
_VctDcOptionsTable_Object = MibTable
vctDcOptionsTable = _VctDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10)
)
if mibBuilder.loadTexts:
    vctDcOptionsTable.setStatus("mandatory")
_VctDcOptionsEntry_Object = MibTableRow
vctDcOptionsEntry = _VctDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1)
)
vctDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcIndex"),
)
if mibBuilder.loadTexts:
    vctDcOptionsEntry.setStatus("mandatory")


class _VctDcLocalNpi_Type(Integer32):
    """Custom type vctDcLocalNpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctDcLocalNpi_Type.__name__ = "Integer32"
_VctDcLocalNpi_Object = MibTableColumn
vctDcLocalNpi = _VctDcLocalNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 1),
    _VctDcLocalNpi_Type()
)
vctDcLocalNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcLocalNpi.setStatus("mandatory")


class _VctDcLocalDna_Type(DigitString):
    """Custom type vctDcLocalDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VctDcLocalDna_Type.__name__ = "DigitString"
_VctDcLocalDna_Object = MibTableColumn
vctDcLocalDna = _VctDcLocalDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 2),
    _VctDcLocalDna_Type()
)
vctDcLocalDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcLocalDna.setStatus("mandatory")


class _VctDcRemoteNpi_Type(Integer32):
    """Custom type vctDcRemoteNpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctDcRemoteNpi_Type.__name__ = "Integer32"
_VctDcRemoteNpi_Object = MibTableColumn
vctDcRemoteNpi = _VctDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 3),
    _VctDcRemoteNpi_Type()
)
vctDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcRemoteNpi.setStatus("mandatory")


class _VctDcRemoteDna_Type(DigitString):
    """Custom type vctDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VctDcRemoteDna_Type.__name__ = "DigitString"
_VctDcRemoteDna_Object = MibTableColumn
vctDcRemoteDna = _VctDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 4),
    _VctDcRemoteDna_Type()
)
vctDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcRemoteDna.setStatus("mandatory")


class _VctDcRemoteLcn_Type(Unsigned32):
    """Custom type vctDcRemoteLcn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VctDcRemoteLcn_Type.__name__ = "Unsigned32"
_VctDcRemoteLcn_Object = MibTableColumn
vctDcRemoteLcn = _VctDcRemoteLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 5),
    _VctDcRemoteLcn_Type()
)
vctDcRemoteLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcRemoteLcn.setStatus("mandatory")


class _VctDcType_Type(Integer32):
    """Custom type vctDcType based on Integer32"""
    defaultValue = 0

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
        *(("permanentBackupSlave", 3),
          ("permanentMaster", 1),
          ("permanentSlave", 2),
          ("permanentSlaveWithBackup", 4),
          ("switched", 0))
    )


_VctDcType_Type.__name__ = "Integer32"
_VctDcType_Object = MibTableColumn
vctDcType = _VctDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 6),
    _VctDcType_Type()
)
vctDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcType.setStatus("mandatory")


class _VctDcSvcAutoCallRetry_Type(Integer32):
    """Custom type vctDcSvcAutoCallRetry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctDcSvcAutoCallRetry_Type.__name__ = "Integer32"
_VctDcSvcAutoCallRetry_Object = MibTableColumn
vctDcSvcAutoCallRetry = _VctDcSvcAutoCallRetry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 7),
    _VctDcSvcAutoCallRetry_Type()
)
vctDcSvcAutoCallRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcSvcAutoCallRetry.setStatus("mandatory")


class _VctDcUserData_Type(HexString):
    """Custom type vctDcUserData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VctDcUserData_Type.__name__ = "HexString"
_VctDcUserData_Object = MibTableColumn
vctDcUserData = _VctDcUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 8),
    _VctDcUserData_Type()
)
vctDcUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcUserData.setStatus("mandatory")


class _VctDcDiscardPriority_Type(Integer32):
    """Custom type vctDcDiscardPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0),
          ("useDnaDefPriority", 3))
    )


_VctDcDiscardPriority_Type.__name__ = "Integer32"
_VctDcDiscardPriority_Object = MibTableColumn
vctDcDiscardPriority = _VctDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 10),
    _VctDcDiscardPriority_Type()
)
vctDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcDiscardPriority.setStatus("mandatory")


class _VctDcDataPath_Type(Integer32):
    """Custom type vctDcDataPath based on Integer32"""
    defaultValue = 0

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
        *(("dprsMcsFirst", 2),
          ("dprsMcsOnly", 1),
          ("dprsOnly", 0),
          ("useDnaValue", 3))
    )


_VctDcDataPath_Type.__name__ = "Integer32"
_VctDcDataPath_Object = MibTableColumn
vctDcDataPath = _VctDcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 11),
    _VctDcDataPath_Type()
)
vctDcDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcDataPath.setStatus("mandatory")


class _VctDcCugIndex_Type(Unsigned32):
    """Custom type vctDcCugIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctDcCugIndex_Type.__name__ = "Unsigned32"
_VctDcCugIndex_Object = MibTableColumn
vctDcCugIndex = _VctDcCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 13),
    _VctDcCugIndex_Type()
)
vctDcCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcCugIndex.setStatus("mandatory")


class _VctDcCugType_Type(Integer32):
    """Custom type vctDcCugType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cug", 3),
          ("cugOa", 9),
          ("doNotSignal", 0))
    )


_VctDcCugType_Type.__name__ = "Integer32"
_VctDcCugType_Object = MibTableColumn
vctDcCugType = _VctDcCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 10, 1, 14),
    _VctDcCugType_Type()
)
vctDcCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcCugType.setStatus("mandatory")
_VctDcCfaTable_Object = MibTable
vctDcCfaTable = _VctDcCfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 267)
)
if mibBuilder.loadTexts:
    vctDcCfaTable.setStatus("mandatory")
_VctDcCfaEntry_Object = MibTableRow
vctDcCfaEntry = _VctDcCfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 267, 1)
)
vctDcCfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcCfaIndex"),
)
if mibBuilder.loadTexts:
    vctDcCfaEntry.setStatus("mandatory")


class _VctDcCfaIndex_Type(Integer32):
    """Custom type vctDcCfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(9, 9),
        ValueRangeConstraint(66, 66),
        ValueRangeConstraint(67, 67),
        ValueRangeConstraint(68, 68),
        ValueRangeConstraint(71, 71),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(73, 73),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(198, 198),
    )


_VctDcCfaIndex_Type.__name__ = "Integer32"
_VctDcCfaIndex_Object = MibTableColumn
vctDcCfaIndex = _VctDcCfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 267, 1, 1),
    _VctDcCfaIndex_Type()
)
vctDcCfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDcCfaIndex.setStatus("mandatory")


class _VctDcCfaValue_Type(HexString):
    """Custom type vctDcCfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VctDcCfaValue_Type.__name__ = "HexString"
_VctDcCfaValue_Object = MibTableColumn
vctDcCfaValue = _VctDcCfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 267, 1, 2),
    _VctDcCfaValue_Type()
)
vctDcCfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcCfaValue.setStatus("mandatory")
_VctDcCfaRowStatus_Type = RowStatus
_VctDcCfaRowStatus_Object = MibTableColumn
vctDcCfaRowStatus = _VctDcCfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 267, 1, 3),
    _VctDcCfaRowStatus_Type()
)
vctDcCfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vctDcCfaRowStatus.setStatus("mandatory")
_VctDcDfaTable_Object = MibTable
vctDcDfaTable = _VctDcDfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 268)
)
if mibBuilder.loadTexts:
    vctDcDfaTable.setStatus("mandatory")
_VctDcDfaEntry_Object = MibTableRow
vctDcDfaEntry = _VctDcDfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 268, 1)
)
vctDcDfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcDfaIndex"),
)
if mibBuilder.loadTexts:
    vctDcDfaEntry.setStatus("mandatory")


class _VctDcDfaIndex_Type(Integer32):
    """Custom type vctDcDfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(11, 11),
        ValueRangeConstraint(201, 201),
        ValueRangeConstraint(202, 202),
        ValueRangeConstraint(203, 203),
        ValueRangeConstraint(210, 210),
        ValueRangeConstraint(211, 211),
    )


_VctDcDfaIndex_Type.__name__ = "Integer32"
_VctDcDfaIndex_Object = MibTableColumn
vctDcDfaIndex = _VctDcDfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 268, 1, 1),
    _VctDcDfaIndex_Type()
)
vctDcDfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDcDfaIndex.setStatus("mandatory")


class _VctDcDfaValue_Type(HexString):
    """Custom type vctDcDfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VctDcDfaValue_Type.__name__ = "HexString"
_VctDcDfaValue_Object = MibTableColumn
vctDcDfaValue = _VctDcDfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 268, 1, 2),
    _VctDcDfaValue_Type()
)
vctDcDfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcDfaValue.setStatus("mandatory")
_VctDcDfaRowStatus_Type = RowStatus
_VctDcDfaRowStatus_Object = MibTableColumn
vctDcDfaRowStatus = _VctDcDfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 268, 1, 3),
    _VctDcDfaRowStatus_Type()
)
vctDcDfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vctDcDfaRowStatus.setStatus("mandatory")
_VctDcNfaTable_Object = MibTable
vctDcNfaTable = _VctDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 269)
)
if mibBuilder.loadTexts:
    vctDcNfaTable.setStatus("obsolete")
_VctDcNfaEntry_Object = MibTableRow
vctDcNfaEntry = _VctDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 269, 1)
)
vctDcNfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcNfaIndex"),
)
if mibBuilder.loadTexts:
    vctDcNfaEntry.setStatus("obsolete")


class _VctDcNfaIndex_Type(Integer32):
    """Custom type vctDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(127, 127),
        ValueRangeConstraint(212, 212),
    )


_VctDcNfaIndex_Type.__name__ = "Integer32"
_VctDcNfaIndex_Object = MibTableColumn
vctDcNfaIndex = _VctDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 269, 1, 1),
    _VctDcNfaIndex_Type()
)
vctDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDcNfaIndex.setStatus("obsolete")


class _VctDcNfaValue_Type(HexString):
    """Custom type vctDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VctDcNfaValue_Type.__name__ = "HexString"
_VctDcNfaValue_Object = MibTableColumn
vctDcNfaValue = _VctDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 269, 1, 2),
    _VctDcNfaValue_Type()
)
vctDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcNfaValue.setStatus("obsolete")
_VctDcNfaRowStatus_Type = RowStatus
_VctDcNfaRowStatus_Object = MibTableColumn
vctDcNfaRowStatus = _VctDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 269, 1, 3),
    _VctDcNfaRowStatus_Type()
)
vctDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vctDcNfaRowStatus.setStatus("obsolete")
_VctDcIfaTable_Object = MibTable
vctDcIfaTable = _VctDcIfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 270)
)
if mibBuilder.loadTexts:
    vctDcIfaTable.setStatus("mandatory")
_VctDcIfaEntry_Object = MibTableRow
vctDcIfaEntry = _VctDcIfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 270, 1)
)
vctDcIfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctDcIfaIndex"),
)
if mibBuilder.loadTexts:
    vctDcIfaEntry.setStatus("mandatory")


class _VctDcIfaIndex_Type(Integer32):
    """Custom type vctDcIfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VctDcIfaIndex_Type.__name__ = "Integer32"
_VctDcIfaIndex_Object = MibTableColumn
vctDcIfaIndex = _VctDcIfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 270, 1, 1),
    _VctDcIfaIndex_Type()
)
vctDcIfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctDcIfaIndex.setStatus("mandatory")


class _VctDcIfaValue_Type(HexString):
    """Custom type vctDcIfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VctDcIfaValue_Type.__name__ = "HexString"
_VctDcIfaValue_Object = MibTableColumn
vctDcIfaValue = _VctDcIfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 270, 1, 2),
    _VctDcIfaValue_Type()
)
vctDcIfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDcIfaValue.setStatus("mandatory")
_VctDcIfaRowStatus_Type = RowStatus
_VctDcIfaRowStatus_Object = MibTableColumn
vctDcIfaRowStatus = _VctDcIfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 3, 270, 1, 3),
    _VctDcIfaRowStatus_Type()
)
vctDcIfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vctDcIfaRowStatus.setStatus("mandatory")
_VctVc_ObjectIdentity = ObjectIdentity
vctVc = _VctVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4)
)
_VctVcRowStatusTable_Object = MibTable
vctVcRowStatusTable = _VctVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 1)
)
if mibBuilder.loadTexts:
    vctVcRowStatusTable.setStatus("mandatory")
_VctVcRowStatusEntry_Object = MibTableRow
vctVcRowStatusEntry = _VctVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 1, 1)
)
vctVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcIndex"),
)
if mibBuilder.loadTexts:
    vctVcRowStatusEntry.setStatus("mandatory")
_VctVcRowStatus_Type = RowStatus
_VctVcRowStatus_Object = MibTableColumn
vctVcRowStatus = _VctVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 1, 1, 1),
    _VctVcRowStatus_Type()
)
vctVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcRowStatus.setStatus("mandatory")
_VctVcComponentName_Type = DisplayString
_VctVcComponentName_Object = MibTableColumn
vctVcComponentName = _VctVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 1, 1, 2),
    _VctVcComponentName_Type()
)
vctVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcComponentName.setStatus("mandatory")
_VctVcStorageType_Type = StorageType
_VctVcStorageType_Object = MibTableColumn
vctVcStorageType = _VctVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 1, 1, 4),
    _VctVcStorageType_Type()
)
vctVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcStorageType.setStatus("mandatory")
_VctVcIndex_Type = NonReplicated
_VctVcIndex_Object = MibTableColumn
vctVcIndex = _VctVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 1, 1, 10),
    _VctVcIndex_Type()
)
vctVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctVcIndex.setStatus("mandatory")
_VctVcCadTable_Object = MibTable
vctVcCadTable = _VctVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10)
)
if mibBuilder.loadTexts:
    vctVcCadTable.setStatus("mandatory")
_VctVcCadEntry_Object = MibTableRow
vctVcCadEntry = _VctVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1)
)
vctVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcIndex"),
)
if mibBuilder.loadTexts:
    vctVcCadEntry.setStatus("mandatory")


class _VctVcType_Type(Integer32):
    """Custom type vctVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 0))
    )


_VctVcType_Type.__name__ = "Integer32"
_VctVcType_Object = MibTableColumn
vctVcType = _VctVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 1),
    _VctVcType_Type()
)
vctVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcType.setStatus("mandatory")


class _VctVcState_Type(Integer32):
    """Custom type vctVcState based on Integer32"""
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
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_VctVcState_Type.__name__ = "Integer32"
_VctVcState_Object = MibTableColumn
vctVcState = _VctVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 2),
    _VctVcState_Type()
)
vctVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcState.setStatus("mandatory")


class _VctVcPreviousState_Type(Integer32):
    """Custom type vctVcPreviousState based on Integer32"""
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
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_VctVcPreviousState_Type.__name__ = "Integer32"
_VctVcPreviousState_Object = MibTableColumn
vctVcPreviousState = _VctVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 3),
    _VctVcPreviousState_Type()
)
vctVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPreviousState.setStatus("mandatory")


class _VctVcDiagnosticCode_Type(Unsigned32):
    """Custom type vctVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctVcDiagnosticCode_Type.__name__ = "Unsigned32"
_VctVcDiagnosticCode_Object = MibTableColumn
vctVcDiagnosticCode = _VctVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 4),
    _VctVcDiagnosticCode_Type()
)
vctVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcDiagnosticCode.setStatus("mandatory")


class _VctVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type vctVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_VctVcPreviousDiagnosticCode_Object = MibTableColumn
vctVcPreviousDiagnosticCode = _VctVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 5),
    _VctVcPreviousDiagnosticCode_Type()
)
vctVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPreviousDiagnosticCode.setStatus("mandatory")


class _VctVcCalledNpi_Type(Integer32):
    """Custom type vctVcCalledNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctVcCalledNpi_Type.__name__ = "Integer32"
_VctVcCalledNpi_Object = MibTableColumn
vctVcCalledNpi = _VctVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 6),
    _VctVcCalledNpi_Type()
)
vctVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcCalledNpi.setStatus("mandatory")


class _VctVcCalledDna_Type(DigitString):
    """Custom type vctVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VctVcCalledDna_Type.__name__ = "DigitString"
_VctVcCalledDna_Object = MibTableColumn
vctVcCalledDna = _VctVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 7),
    _VctVcCalledDna_Type()
)
vctVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcCalledDna.setStatus("mandatory")


class _VctVcCalledLcn_Type(Unsigned32):
    """Custom type vctVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VctVcCalledLcn_Type.__name__ = "Unsigned32"
_VctVcCalledLcn_Object = MibTableColumn
vctVcCalledLcn = _VctVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 8),
    _VctVcCalledLcn_Type()
)
vctVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcCalledLcn.setStatus("mandatory")


class _VctVcCallingNpi_Type(Integer32):
    """Custom type vctVcCallingNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctVcCallingNpi_Type.__name__ = "Integer32"
_VctVcCallingNpi_Object = MibTableColumn
vctVcCallingNpi = _VctVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 9),
    _VctVcCallingNpi_Type()
)
vctVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcCallingNpi.setStatus("mandatory")


class _VctVcCallingDna_Type(DigitString):
    """Custom type vctVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VctVcCallingDna_Type.__name__ = "DigitString"
_VctVcCallingDna_Object = MibTableColumn
vctVcCallingDna = _VctVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 10),
    _VctVcCallingDna_Type()
)
vctVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcCallingDna.setStatus("mandatory")


class _VctVcCallingLcn_Type(Unsigned32):
    """Custom type vctVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VctVcCallingLcn_Type.__name__ = "Unsigned32"
_VctVcCallingLcn_Object = MibTableColumn
vctVcCallingLcn = _VctVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 11),
    _VctVcCallingLcn_Type()
)
vctVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcCallingLcn.setStatus("mandatory")


class _VctVcAccountingEnabled_Type(Integer32):
    """Custom type vctVcAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_VctVcAccountingEnabled_Type.__name__ = "Integer32"
_VctVcAccountingEnabled_Object = MibTableColumn
vctVcAccountingEnabled = _VctVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 12),
    _VctVcAccountingEnabled_Type()
)
vctVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcAccountingEnabled.setStatus("mandatory")


class _VctVcFastSelectCall_Type(Integer32):
    """Custom type vctVcFastSelectCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctVcFastSelectCall_Type.__name__ = "Integer32"
_VctVcFastSelectCall_Object = MibTableColumn
vctVcFastSelectCall = _VctVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 13),
    _VctVcFastSelectCall_Type()
)
vctVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcFastSelectCall.setStatus("mandatory")


class _VctVcLocalRxPktSize_Type(Integer32):
    """Custom type vctVcLocalRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_VctVcLocalRxPktSize_Type.__name__ = "Integer32"
_VctVcLocalRxPktSize_Object = MibTableColumn
vctVcLocalRxPktSize = _VctVcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 14),
    _VctVcLocalRxPktSize_Type()
)
vctVcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcLocalRxPktSize.setStatus("mandatory")


class _VctVcLocalTxPktSize_Type(Integer32):
    """Custom type vctVcLocalTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_VctVcLocalTxPktSize_Type.__name__ = "Integer32"
_VctVcLocalTxPktSize_Object = MibTableColumn
vctVcLocalTxPktSize = _VctVcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 15),
    _VctVcLocalTxPktSize_Type()
)
vctVcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcLocalTxPktSize.setStatus("mandatory")


class _VctVcLocalTxWindowSize_Type(Unsigned32):
    """Custom type vctVcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VctVcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_VctVcLocalTxWindowSize_Object = MibTableColumn
vctVcLocalTxWindowSize = _VctVcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 16),
    _VctVcLocalTxWindowSize_Type()
)
vctVcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcLocalTxWindowSize.setStatus("mandatory")


class _VctVcLocalRxWindowSize_Type(Unsigned32):
    """Custom type vctVcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VctVcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_VctVcLocalRxWindowSize_Object = MibTableColumn
vctVcLocalRxWindowSize = _VctVcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 17),
    _VctVcLocalRxWindowSize_Type()
)
vctVcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcLocalRxWindowSize.setStatus("mandatory")


class _VctVcPathReliability_Type(Integer32):
    """Custom type vctVcPathReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_VctVcPathReliability_Type.__name__ = "Integer32"
_VctVcPathReliability_Object = MibTableColumn
vctVcPathReliability = _VctVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 19),
    _VctVcPathReliability_Type()
)
vctVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPathReliability.setStatus("mandatory")


class _VctVcAccountingEnd_Type(Integer32):
    """Custom type vctVcAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_VctVcAccountingEnd_Type.__name__ = "Integer32"
_VctVcAccountingEnd_Object = MibTableColumn
vctVcAccountingEnd = _VctVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 20),
    _VctVcAccountingEnd_Type()
)
vctVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcAccountingEnd.setStatus("mandatory")


class _VctVcPriority_Type(Integer32):
    """Custom type vctVcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_VctVcPriority_Type.__name__ = "Integer32"
_VctVcPriority_Object = MibTableColumn
vctVcPriority = _VctVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 21),
    _VctVcPriority_Type()
)
vctVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPriority.setStatus("mandatory")


class _VctVcSegmentSize_Type(Unsigned32):
    """Custom type vctVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctVcSegmentSize_Type.__name__ = "Unsigned32"
_VctVcSegmentSize_Object = MibTableColumn
vctVcSegmentSize = _VctVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 22),
    _VctVcSegmentSize_Type()
)
vctVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSegmentSize.setStatus("mandatory")


class _VctVcSubnetTxPktSize_Type(Integer32):
    """Custom type vctVcSubnetTxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_VctVcSubnetTxPktSize_Type.__name__ = "Integer32"
_VctVcSubnetTxPktSize_Object = MibTableColumn
vctVcSubnetTxPktSize = _VctVcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 23),
    _VctVcSubnetTxPktSize_Type()
)
vctVcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSubnetTxPktSize.setStatus("mandatory")


class _VctVcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type vctVcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctVcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_VctVcSubnetTxWindowSize_Object = MibTableColumn
vctVcSubnetTxWindowSize = _VctVcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 24),
    _VctVcSubnetTxWindowSize_Type()
)
vctVcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSubnetTxWindowSize.setStatus("mandatory")


class _VctVcSubnetRxPktSize_Type(Integer32):
    """Custom type vctVcSubnetRxPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("n1024", 10),
          ("n128", 7),
          ("n16", 4),
          ("n2048", 11),
          ("n256", 8),
          ("n32", 5),
          ("n4096", 12),
          ("n512", 9),
          ("n64", 6),
          ("unknown", 0))
    )


_VctVcSubnetRxPktSize_Type.__name__ = "Integer32"
_VctVcSubnetRxPktSize_Object = MibTableColumn
vctVcSubnetRxPktSize = _VctVcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 25),
    _VctVcSubnetRxPktSize_Type()
)
vctVcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSubnetRxPktSize.setStatus("mandatory")


class _VctVcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type vctVcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctVcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_VctVcSubnetRxWindowSize_Object = MibTableColumn
vctVcSubnetRxWindowSize = _VctVcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 26),
    _VctVcSubnetRxWindowSize_Type()
)
vctVcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSubnetRxWindowSize.setStatus("mandatory")


class _VctVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type vctVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_VctVcMaxSubnetPktSize_Object = MibTableColumn
vctVcMaxSubnetPktSize = _VctVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 27),
    _VctVcMaxSubnetPktSize_Type()
)
vctVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcMaxSubnetPktSize.setStatus("mandatory")


class _VctVcTransferPriorityToNetwork_Type(Integer32):
    """Custom type vctVcTransferPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_VctVcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_VctVcTransferPriorityToNetwork_Object = MibTableColumn
vctVcTransferPriorityToNetwork = _VctVcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 28),
    _VctVcTransferPriorityToNetwork_Type()
)
vctVcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcTransferPriorityToNetwork.setStatus("mandatory")


class _VctVcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type vctVcTransferPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0))
    )


_VctVcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_VctVcTransferPriorityFromNetwork_Object = MibTableColumn
vctVcTransferPriorityFromNetwork = _VctVcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 10, 1, 29),
    _VctVcTransferPriorityFromNetwork_Type()
)
vctVcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcTransferPriorityFromNetwork.setStatus("mandatory")
_VctVcIntdTable_Object = MibTable
vctVcIntdTable = _VctVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 11)
)
if mibBuilder.loadTexts:
    vctVcIntdTable.setStatus("mandatory")
_VctVcIntdEntry_Object = MibTableRow
vctVcIntdEntry = _VctVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 11, 1)
)
vctVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcIndex"),
)
if mibBuilder.loadTexts:
    vctVcIntdEntry.setStatus("mandatory")


class _VctVcCallReferenceNumber_Type(Hex):
    """Custom type vctVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcCallReferenceNumber_Type.__name__ = "Hex"
_VctVcCallReferenceNumber_Object = MibTableColumn
vctVcCallReferenceNumber = _VctVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 11, 1, 1),
    _VctVcCallReferenceNumber_Type()
)
vctVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcCallReferenceNumber.setStatus("mandatory")


class _VctVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type vctVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_VctVcElapsedTimeTillNow_Object = MibTableColumn
vctVcElapsedTimeTillNow = _VctVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 11, 1, 2),
    _VctVcElapsedTimeTillNow_Type()
)
vctVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcElapsedTimeTillNow.setStatus("mandatory")


class _VctVcSegmentsRx_Type(Unsigned32):
    """Custom type vctVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcSegmentsRx_Type.__name__ = "Unsigned32"
_VctVcSegmentsRx_Object = MibTableColumn
vctVcSegmentsRx = _VctVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 11, 1, 3),
    _VctVcSegmentsRx_Type()
)
vctVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSegmentsRx.setStatus("mandatory")


class _VctVcSegmentsSent_Type(Unsigned32):
    """Custom type vctVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcSegmentsSent_Type.__name__ = "Unsigned32"
_VctVcSegmentsSent_Object = MibTableColumn
vctVcSegmentsSent = _VctVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 11, 1, 4),
    _VctVcSegmentsSent_Type()
)
vctVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSegmentsSent.setStatus("mandatory")


class _VctVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type vctVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_VctVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_VctVcStartTime_Object = MibTableColumn
vctVcStartTime = _VctVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 11, 1, 5),
    _VctVcStartTime_Type()
)
vctVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcStartTime.setStatus("mandatory")
_VctVcStatsTable_Object = MibTable
vctVcStatsTable = _VctVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12)
)
if mibBuilder.loadTexts:
    vctVcStatsTable.setStatus("mandatory")
_VctVcStatsEntry_Object = MibTableRow
vctVcStatsEntry = _VctVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1)
)
vctVcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcIndex"),
)
if mibBuilder.loadTexts:
    vctVcStatsEntry.setStatus("mandatory")


class _VctVcAckStackingTimeouts_Type(Unsigned32):
    """Custom type vctVcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_VctVcAckStackingTimeouts_Object = MibTableColumn
vctVcAckStackingTimeouts = _VctVcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 1),
    _VctVcAckStackingTimeouts_Type()
)
vctVcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcAckStackingTimeouts.setStatus("mandatory")


class _VctVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type vctVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_VctVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
vctVcOutOfRangeFrmFromSubnet = _VctVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 2),
    _VctVcOutOfRangeFrmFromSubnet_Type()
)
vctVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _VctVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type vctVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_VctVcDuplicatesFromSubnet_Object = MibTableColumn
vctVcDuplicatesFromSubnet = _VctVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 3),
    _VctVcDuplicatesFromSubnet_Type()
)
vctVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcDuplicatesFromSubnet.setStatus("mandatory")


class _VctVcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type vctVcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_VctVcFrmRetryTimeouts_Object = MibTableColumn
vctVcFrmRetryTimeouts = _VctVcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 4),
    _VctVcFrmRetryTimeouts_Type()
)
vctVcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcFrmRetryTimeouts.setStatus("mandatory")


class _VctVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type vctVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_VctVcPeakRetryQueueSize_Object = MibTableColumn
vctVcPeakRetryQueueSize = _VctVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 5),
    _VctVcPeakRetryQueueSize_Type()
)
vctVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPeakRetryQueueSize.setStatus("mandatory")


class _VctVcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type vctVcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_VctVcPeakOoSeqQueueSize_Object = MibTableColumn
vctVcPeakOoSeqQueueSize = _VctVcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 6),
    _VctVcPeakOoSeqQueueSize_Type()
)
vctVcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPeakOoSeqQueueSize.setStatus("mandatory")


class _VctVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type vctVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_VctVcPeakOoSeqFrmForwarded_Object = MibTableColumn
vctVcPeakOoSeqFrmForwarded = _VctVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 7),
    _VctVcPeakOoSeqFrmForwarded_Type()
)
vctVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _VctVcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type vctVcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_VctVcPeakStackedAcksRx_Object = MibTableColumn
vctVcPeakStackedAcksRx = _VctVcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 8),
    _VctVcPeakStackedAcksRx_Type()
)
vctVcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcPeakStackedAcksRx.setStatus("mandatory")


class _VctVcSubnetRecoveries_Type(Unsigned32):
    """Custom type vctVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_VctVcSubnetRecoveries_Object = MibTableColumn
vctVcSubnetRecoveries = _VctVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 9),
    _VctVcSubnetRecoveries_Type()
)
vctVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcSubnetRecoveries.setStatus("mandatory")


class _VctVcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type vctVcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_VctVcWindowClosuresToSubnet_Object = MibTableColumn
vctVcWindowClosuresToSubnet = _VctVcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 10),
    _VctVcWindowClosuresToSubnet_Type()
)
vctVcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcWindowClosuresToSubnet.setStatus("mandatory")


class _VctVcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type vctVcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_VctVcWindowClosuresFromSubnet_Object = MibTableColumn
vctVcWindowClosuresFromSubnet = _VctVcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 11),
    _VctVcWindowClosuresFromSubnet_Type()
)
vctVcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcWindowClosuresFromSubnet.setStatus("mandatory")


class _VctVcWrTriggers_Type(Unsigned32):
    """Custom type vctVcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcWrTriggers_Type.__name__ = "Unsigned32"
_VctVcWrTriggers_Object = MibTableColumn
vctVcWrTriggers = _VctVcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 4, 12, 1, 12),
    _VctVcWrTriggers_Type()
)
vctVcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcWrTriggers.setStatus("mandatory")
_VctVcfr_ObjectIdentity = ObjectIdentity
vctVcfr = _VctVcfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5)
)
_VctVcfrRowStatusTable_Object = MibTable
vctVcfrRowStatusTable = _VctVcfrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 1)
)
if mibBuilder.loadTexts:
    vctVcfrRowStatusTable.setStatus("mandatory")
_VctVcfrRowStatusEntry_Object = MibTableRow
vctVcfrRowStatusEntry = _VctVcfrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 1, 1)
)
vctVcfrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcfrIndex"),
)
if mibBuilder.loadTexts:
    vctVcfrRowStatusEntry.setStatus("mandatory")
_VctVcfrRowStatus_Type = RowStatus
_VctVcfrRowStatus_Object = MibTableColumn
vctVcfrRowStatus = _VctVcfrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 1, 1, 1),
    _VctVcfrRowStatus_Type()
)
vctVcfrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrRowStatus.setStatus("mandatory")
_VctVcfrComponentName_Type = DisplayString
_VctVcfrComponentName_Object = MibTableColumn
vctVcfrComponentName = _VctVcfrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 1, 1, 2),
    _VctVcfrComponentName_Type()
)
vctVcfrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrComponentName.setStatus("mandatory")
_VctVcfrStorageType_Type = StorageType
_VctVcfrStorageType_Object = MibTableColumn
vctVcfrStorageType = _VctVcfrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 1, 1, 4),
    _VctVcfrStorageType_Type()
)
vctVcfrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrStorageType.setStatus("mandatory")
_VctVcfrIndex_Type = NonReplicated
_VctVcfrIndex_Object = MibTableColumn
vctVcfrIndex = _VctVcfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 1, 1, 10),
    _VctVcfrIndex_Type()
)
vctVcfrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctVcfrIndex.setStatus("mandatory")
_VctVcfrCadTable_Object = MibTable
vctVcfrCadTable = _VctVcfrCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10)
)
if mibBuilder.loadTexts:
    vctVcfrCadTable.setStatus("mandatory")
_VctVcfrCadEntry_Object = MibTableRow
vctVcfrCadEntry = _VctVcfrCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1)
)
vctVcfrCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcfrIndex"),
)
if mibBuilder.loadTexts:
    vctVcfrCadEntry.setStatus("mandatory")


class _VctVcfrType_Type(Integer32):
    """Custom type vctVcfrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("spvc", 2),
          ("svc", 0))
    )


_VctVcfrType_Type.__name__ = "Integer32"
_VctVcfrType_Object = MibTableColumn
vctVcfrType = _VctVcfrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 1),
    _VctVcfrType_Type()
)
vctVcfrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrType.setStatus("mandatory")


class _VctVcfrState_Type(Integer32):
    """Custom type vctVcfrState based on Integer32"""
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
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_VctVcfrState_Type.__name__ = "Integer32"
_VctVcfrState_Object = MibTableColumn
vctVcfrState = _VctVcfrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 2),
    _VctVcfrState_Type()
)
vctVcfrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrState.setStatus("mandatory")


class _VctVcfrPreviousState_Type(Integer32):
    """Custom type vctVcfrPreviousState based on Integer32"""
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
        *(("creating", 0),
          ("dataTransferP4", 4),
          ("dceClearIndicationP7", 7),
          ("dceWaitingP3", 3),
          ("dteClearRequestP6", 6),
          ("dteWaitingP2", 2),
          ("readyP1", 1),
          ("termination", 8),
          ("unsupportedP5", 5))
    )


_VctVcfrPreviousState_Type.__name__ = "Integer32"
_VctVcfrPreviousState_Object = MibTableColumn
vctVcfrPreviousState = _VctVcfrPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 3),
    _VctVcfrPreviousState_Type()
)
vctVcfrPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPreviousState.setStatus("mandatory")


class _VctVcfrDiagnosticCode_Type(Unsigned32):
    """Custom type vctVcfrDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctVcfrDiagnosticCode_Type.__name__ = "Unsigned32"
_VctVcfrDiagnosticCode_Object = MibTableColumn
vctVcfrDiagnosticCode = _VctVcfrDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 4),
    _VctVcfrDiagnosticCode_Type()
)
vctVcfrDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrDiagnosticCode.setStatus("mandatory")


class _VctVcfrPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type vctVcfrPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctVcfrPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_VctVcfrPreviousDiagnosticCode_Object = MibTableColumn
vctVcfrPreviousDiagnosticCode = _VctVcfrPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 5),
    _VctVcfrPreviousDiagnosticCode_Type()
)
vctVcfrPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPreviousDiagnosticCode.setStatus("mandatory")


class _VctVcfrCalledNpi_Type(Integer32):
    """Custom type vctVcfrCalledNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctVcfrCalledNpi_Type.__name__ = "Integer32"
_VctVcfrCalledNpi_Object = MibTableColumn
vctVcfrCalledNpi = _VctVcfrCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 6),
    _VctVcfrCalledNpi_Type()
)
vctVcfrCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCalledNpi.setStatus("mandatory")


class _VctVcfrCalledDna_Type(DigitString):
    """Custom type vctVcfrCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VctVcfrCalledDna_Type.__name__ = "DigitString"
_VctVcfrCalledDna_Object = MibTableColumn
vctVcfrCalledDna = _VctVcfrCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 7),
    _VctVcfrCalledDna_Type()
)
vctVcfrCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCalledDna.setStatus("mandatory")


class _VctVcfrCalledLcn_Type(Unsigned32):
    """Custom type vctVcfrCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VctVcfrCalledLcn_Type.__name__ = "Unsigned32"
_VctVcfrCalledLcn_Object = MibTableColumn
vctVcfrCalledLcn = _VctVcfrCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 8),
    _VctVcfrCalledLcn_Type()
)
vctVcfrCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCalledLcn.setStatus("mandatory")


class _VctVcfrCallingNpi_Type(Integer32):
    """Custom type vctVcfrCallingNpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e164", 1),
          ("x121", 0))
    )


_VctVcfrCallingNpi_Type.__name__ = "Integer32"
_VctVcfrCallingNpi_Object = MibTableColumn
vctVcfrCallingNpi = _VctVcfrCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 9),
    _VctVcfrCallingNpi_Type()
)
vctVcfrCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCallingNpi.setStatus("mandatory")


class _VctVcfrCallingDna_Type(DigitString):
    """Custom type vctVcfrCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_VctVcfrCallingDna_Type.__name__ = "DigitString"
_VctVcfrCallingDna_Object = MibTableColumn
vctVcfrCallingDna = _VctVcfrCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 10),
    _VctVcfrCallingDna_Type()
)
vctVcfrCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCallingDna.setStatus("mandatory")


class _VctVcfrCallingLcn_Type(Unsigned32):
    """Custom type vctVcfrCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VctVcfrCallingLcn_Type.__name__ = "Unsigned32"
_VctVcfrCallingLcn_Object = MibTableColumn
vctVcfrCallingLcn = _VctVcfrCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 11),
    _VctVcfrCallingLcn_Type()
)
vctVcfrCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCallingLcn.setStatus("mandatory")


class _VctVcfrAccountingEnabled_Type(Integer32):
    """Custom type vctVcfrAccountingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_VctVcfrAccountingEnabled_Type.__name__ = "Integer32"
_VctVcfrAccountingEnabled_Object = MibTableColumn
vctVcfrAccountingEnabled = _VctVcfrAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 12),
    _VctVcfrAccountingEnabled_Type()
)
vctVcfrAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrAccountingEnabled.setStatus("mandatory")


class _VctVcfrFastSelectCall_Type(Integer32):
    """Custom type vctVcfrFastSelectCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_VctVcfrFastSelectCall_Type.__name__ = "Integer32"
_VctVcfrFastSelectCall_Object = MibTableColumn
vctVcfrFastSelectCall = _VctVcfrFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 13),
    _VctVcfrFastSelectCall_Type()
)
vctVcfrFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrFastSelectCall.setStatus("mandatory")


class _VctVcfrPathReliability_Type(Integer32):
    """Custom type vctVcfrPathReliability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("normal", 1))
    )


_VctVcfrPathReliability_Type.__name__ = "Integer32"
_VctVcfrPathReliability_Object = MibTableColumn
vctVcfrPathReliability = _VctVcfrPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 19),
    _VctVcfrPathReliability_Type()
)
vctVcfrPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPathReliability.setStatus("mandatory")


class _VctVcfrAccountingEnd_Type(Integer32):
    """Custom type vctVcfrAccountingEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("calledEnd", 1),
          ("callingEnd", 0))
    )


_VctVcfrAccountingEnd_Type.__name__ = "Integer32"
_VctVcfrAccountingEnd_Object = MibTableColumn
vctVcfrAccountingEnd = _VctVcfrAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 20),
    _VctVcfrAccountingEnd_Type()
)
vctVcfrAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrAccountingEnd.setStatus("mandatory")


class _VctVcfrPriority_Type(Integer32):
    """Custom type vctVcfrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("normal", 0))
    )


_VctVcfrPriority_Type.__name__ = "Integer32"
_VctVcfrPriority_Object = MibTableColumn
vctVcfrPriority = _VctVcfrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 21),
    _VctVcfrPriority_Type()
)
vctVcfrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPriority.setStatus("mandatory")


class _VctVcfrSegmentSize_Type(Unsigned32):
    """Custom type vctVcfrSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctVcfrSegmentSize_Type.__name__ = "Unsigned32"
_VctVcfrSegmentSize_Object = MibTableColumn
vctVcfrSegmentSize = _VctVcfrSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 22),
    _VctVcfrSegmentSize_Type()
)
vctVcfrSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrSegmentSize.setStatus("mandatory")


class _VctVcfrMaxSubnetPktSize_Type(Unsigned32):
    """Custom type vctVcfrMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VctVcfrMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_VctVcfrMaxSubnetPktSize_Object = MibTableColumn
vctVcfrMaxSubnetPktSize = _VctVcfrMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 27),
    _VctVcfrMaxSubnetPktSize_Type()
)
vctVcfrMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrMaxSubnetPktSize.setStatus("mandatory")


class _VctVcfrRcosToNetwork_Type(Integer32):
    """Custom type vctVcfrRcosToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_VctVcfrRcosToNetwork_Type.__name__ = "Integer32"
_VctVcfrRcosToNetwork_Object = MibTableColumn
vctVcfrRcosToNetwork = _VctVcfrRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 28),
    _VctVcfrRcosToNetwork_Type()
)
vctVcfrRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrRcosToNetwork.setStatus("mandatory")


class _VctVcfrRcosFromNetwork_Type(Integer32):
    """Custom type vctVcfrRcosFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delay", 1),
          ("multimedia", 2),
          ("throughput", 0))
    )


_VctVcfrRcosFromNetwork_Type.__name__ = "Integer32"
_VctVcfrRcosFromNetwork_Object = MibTableColumn
vctVcfrRcosFromNetwork = _VctVcfrRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 29),
    _VctVcfrRcosFromNetwork_Type()
)
vctVcfrRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrRcosFromNetwork.setStatus("mandatory")


class _VctVcfrEmissionPriorityToNetwork_Type(Integer32):
    """Custom type vctVcfrEmissionPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_VctVcfrEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_VctVcfrEmissionPriorityToNetwork_Object = MibTableColumn
vctVcfrEmissionPriorityToNetwork = _VctVcfrEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 30),
    _VctVcfrEmissionPriorityToNetwork_Type()
)
vctVcfrEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrEmissionPriorityToNetwork.setStatus("mandatory")


class _VctVcfrEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type vctVcfrEmissionPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("interrupting", 2),
          ("normal", 0))
    )


_VctVcfrEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_VctVcfrEmissionPriorityFromNetwork_Object = MibTableColumn
vctVcfrEmissionPriorityFromNetwork = _VctVcfrEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 31),
    _VctVcfrEmissionPriorityFromNetwork_Type()
)
vctVcfrEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrEmissionPriorityFromNetwork.setStatus("mandatory")


class _VctVcfrDataPath_Type(AsciiString):
    """Custom type vctVcfrDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VctVcfrDataPath_Type.__name__ = "AsciiString"
_VctVcfrDataPath_Object = MibTableColumn
vctVcfrDataPath = _VctVcfrDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 10, 1, 32),
    _VctVcfrDataPath_Type()
)
vctVcfrDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrDataPath.setStatus("mandatory")
_VctVcfrIntdTable_Object = MibTable
vctVcfrIntdTable = _VctVcfrIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 11)
)
if mibBuilder.loadTexts:
    vctVcfrIntdTable.setStatus("mandatory")
_VctVcfrIntdEntry_Object = MibTableRow
vctVcfrIntdEntry = _VctVcfrIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 11, 1)
)
vctVcfrIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcfrIndex"),
)
if mibBuilder.loadTexts:
    vctVcfrIntdEntry.setStatus("mandatory")


class _VctVcfrCallReferenceNumber_Type(Hex):
    """Custom type vctVcfrCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcfrCallReferenceNumber_Type.__name__ = "Hex"
_VctVcfrCallReferenceNumber_Object = MibTableColumn
vctVcfrCallReferenceNumber = _VctVcfrCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 11, 1, 1),
    _VctVcfrCallReferenceNumber_Type()
)
vctVcfrCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCallReferenceNumber.setStatus("mandatory")


class _VctVcfrElapsedTimeTillNow_Type(Unsigned32):
    """Custom type vctVcfrElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcfrElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_VctVcfrElapsedTimeTillNow_Object = MibTableColumn
vctVcfrElapsedTimeTillNow = _VctVcfrElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 11, 1, 2),
    _VctVcfrElapsedTimeTillNow_Type()
)
vctVcfrElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrElapsedTimeTillNow.setStatus("mandatory")


class _VctVcfrSegmentsRx_Type(Unsigned32):
    """Custom type vctVcfrSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcfrSegmentsRx_Type.__name__ = "Unsigned32"
_VctVcfrSegmentsRx_Object = MibTableColumn
vctVcfrSegmentsRx = _VctVcfrSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 11, 1, 3),
    _VctVcfrSegmentsRx_Type()
)
vctVcfrSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrSegmentsRx.setStatus("mandatory")


class _VctVcfrSegmentsSent_Type(Unsigned32):
    """Custom type vctVcfrSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VctVcfrSegmentsSent_Type.__name__ = "Unsigned32"
_VctVcfrSegmentsSent_Object = MibTableColumn
vctVcfrSegmentsSent = _VctVcfrSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 11, 1, 4),
    _VctVcfrSegmentsSent_Type()
)
vctVcfrSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrSegmentsSent.setStatus("mandatory")


class _VctVcfrStartTime_Type(EnterpriseDateAndTime):
    """Custom type vctVcfrStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_VctVcfrStartTime_Type.__name__ = "EnterpriseDateAndTime"
_VctVcfrStartTime_Object = MibTableColumn
vctVcfrStartTime = _VctVcfrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 11, 1, 5),
    _VctVcfrStartTime_Type()
)
vctVcfrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrStartTime.setStatus("mandatory")
_VctVcfrFrdTable_Object = MibTable
vctVcfrFrdTable = _VctVcfrFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12)
)
if mibBuilder.loadTexts:
    vctVcfrFrdTable.setStatus("mandatory")
_VctVcfrFrdEntry_Object = MibTableRow
vctVcfrFrdEntry = _VctVcfrFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1)
)
vctVcfrFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcfrIndex"),
)
if mibBuilder.loadTexts:
    vctVcfrFrdEntry.setStatus("mandatory")


class _VctVcfrFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type vctVcfrFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_VctVcfrFrmCongestedToSubnet_Object = MibTableColumn
vctVcfrFrmCongestedToSubnet = _VctVcfrFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 2),
    _VctVcfrFrmCongestedToSubnet_Type()
)
vctVcfrFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrFrmCongestedToSubnet.setStatus("mandatory")


class _VctVcfrCannotForwardToSubnet_Type(Unsigned32):
    """Custom type vctVcfrCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_VctVcfrCannotForwardToSubnet_Object = MibTableColumn
vctVcfrCannotForwardToSubnet = _VctVcfrCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 3),
    _VctVcfrCannotForwardToSubnet_Type()
)
vctVcfrCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCannotForwardToSubnet.setStatus("mandatory")


class _VctVcfrNotDataXferToSubnet_Type(Unsigned32):
    """Custom type vctVcfrNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_VctVcfrNotDataXferToSubnet_Object = MibTableColumn
vctVcfrNotDataXferToSubnet = _VctVcfrNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 4),
    _VctVcfrNotDataXferToSubnet_Type()
)
vctVcfrNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrNotDataXferToSubnet.setStatus("mandatory")


class _VctVcfrOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type vctVcfrOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_VctVcfrOutOfRangeFrmFromSubnet_Object = MibTableColumn
vctVcfrOutOfRangeFrmFromSubnet = _VctVcfrOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 5),
    _VctVcfrOutOfRangeFrmFromSubnet_Type()
)
vctVcfrOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _VctVcfrCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type vctVcfrCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_VctVcfrCombErrorsFromSubnet_Object = MibTableColumn
vctVcfrCombErrorsFromSubnet = _VctVcfrCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 6),
    _VctVcfrCombErrorsFromSubnet_Type()
)
vctVcfrCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrCombErrorsFromSubnet.setStatus("mandatory")


class _VctVcfrDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type vctVcfrDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_VctVcfrDuplicatesFromSubnet_Object = MibTableColumn
vctVcfrDuplicatesFromSubnet = _VctVcfrDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 7),
    _VctVcfrDuplicatesFromSubnet_Type()
)
vctVcfrDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrDuplicatesFromSubnet.setStatus("mandatory")


class _VctVcfrNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type vctVcfrNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_VctVcfrNotDataXferFromSubnet_Object = MibTableColumn
vctVcfrNotDataXferFromSubnet = _VctVcfrNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 8),
    _VctVcfrNotDataXferFromSubnet_Type()
)
vctVcfrNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrNotDataXferFromSubnet.setStatus("mandatory")


class _VctVcfrFrmLossTimeouts_Type(Unsigned32):
    """Custom type vctVcfrFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrFrmLossTimeouts_Type.__name__ = "Unsigned32"
_VctVcfrFrmLossTimeouts_Object = MibTableColumn
vctVcfrFrmLossTimeouts = _VctVcfrFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 9),
    _VctVcfrFrmLossTimeouts_Type()
)
vctVcfrFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrFrmLossTimeouts.setStatus("mandatory")


class _VctVcfrOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type vctVcfrOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_VctVcfrOoSeqByteCntExceeded_Object = MibTableColumn
vctVcfrOoSeqByteCntExceeded = _VctVcfrOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 10),
    _VctVcfrOoSeqByteCntExceeded_Type()
)
vctVcfrOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrOoSeqByteCntExceeded.setStatus("mandatory")


class _VctVcfrPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type vctVcfrPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_VctVcfrPeakOoSeqPktCount_Object = MibTableColumn
vctVcfrPeakOoSeqPktCount = _VctVcfrPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 11),
    _VctVcfrPeakOoSeqPktCount_Type()
)
vctVcfrPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPeakOoSeqPktCount.setStatus("mandatory")


class _VctVcfrPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type vctVcfrPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_VctVcfrPeakOoSeqFrmForwarded_Object = MibTableColumn
vctVcfrPeakOoSeqFrmForwarded = _VctVcfrPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 12),
    _VctVcfrPeakOoSeqFrmForwarded_Type()
)
vctVcfrPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPeakOoSeqFrmForwarded.setStatus("mandatory")


class _VctVcfrSendSequenceNumber_Type(Unsigned32):
    """Custom type vctVcfrSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrSendSequenceNumber_Type.__name__ = "Unsigned32"
_VctVcfrSendSequenceNumber_Object = MibTableColumn
vctVcfrSendSequenceNumber = _VctVcfrSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 13),
    _VctVcfrSendSequenceNumber_Type()
)
vctVcfrSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrSendSequenceNumber.setStatus("mandatory")


class _VctVcfrPktRetryTimeouts_Type(Unsigned32):
    """Custom type vctVcfrPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrPktRetryTimeouts_Type.__name__ = "Unsigned32"
_VctVcfrPktRetryTimeouts_Object = MibTableColumn
vctVcfrPktRetryTimeouts = _VctVcfrPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 15),
    _VctVcfrPktRetryTimeouts_Type()
)
vctVcfrPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPktRetryTimeouts.setStatus("mandatory")


class _VctVcfrPeakRetryQueueSize_Type(Unsigned32):
    """Custom type vctVcfrPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_VctVcfrPeakRetryQueueSize_Object = MibTableColumn
vctVcfrPeakRetryQueueSize = _VctVcfrPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 16),
    _VctVcfrPeakRetryQueueSize_Type()
)
vctVcfrPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPeakRetryQueueSize.setStatus("mandatory")


class _VctVcfrSubnetRecoveries_Type(Unsigned32):
    """Custom type vctVcfrSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VctVcfrSubnetRecoveries_Type.__name__ = "Unsigned32"
_VctVcfrSubnetRecoveries_Object = MibTableColumn
vctVcfrSubnetRecoveries = _VctVcfrSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 17),
    _VctVcfrSubnetRecoveries_Type()
)
vctVcfrSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrSubnetRecoveries.setStatus("mandatory")


class _VctVcfrOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type vctVcfrOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VctVcfrOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_VctVcfrOoSeqPktCntExceeded_Object = MibTableColumn
vctVcfrOoSeqPktCntExceeded = _VctVcfrOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 19),
    _VctVcfrOoSeqPktCntExceeded_Type()
)
vctVcfrOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrOoSeqPktCntExceeded.setStatus("mandatory")


class _VctVcfrPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type vctVcfrPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_VctVcfrPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_VctVcfrPeakOoSeqByteCount_Object = MibTableColumn
vctVcfrPeakOoSeqByteCount = _VctVcfrPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 12, 1, 20),
    _VctVcfrPeakOoSeqByteCount_Type()
)
vctVcfrPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrPeakOoSeqByteCount.setStatus("mandatory")
_VctVcfrDmepTable_Object = MibTable
vctVcfrDmepTable = _VctVcfrDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 417)
)
if mibBuilder.loadTexts:
    vctVcfrDmepTable.setStatus("mandatory")
_VctVcfrDmepEntry_Object = MibTableRow
vctVcfrDmepEntry = _VctVcfrDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 417, 1)
)
vctVcfrDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcfrIndex"),
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctVcfrDmepValue"),
)
if mibBuilder.loadTexts:
    vctVcfrDmepEntry.setStatus("mandatory")
_VctVcfrDmepValue_Type = RowPointer
_VctVcfrDmepValue_Object = MibTableColumn
vctVcfrDmepValue = _VctVcfrDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 5, 417, 1, 1),
    _VctVcfrDmepValue_Type()
)
vctVcfrDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctVcfrDmepValue.setStatus("mandatory")
_VctProvTable_Object = MibTable
vctProvTable = _VctProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 10)
)
if mibBuilder.loadTexts:
    vctProvTable.setStatus("mandatory")
_VctProvEntry_Object = MibTableRow
vctProvEntry = _VctProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 10, 1)
)
vctProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VcTesterMIB", "vctIndex"),
)
if mibBuilder.loadTexts:
    vctProvEntry.setStatus("mandatory")
_VctLogicalProcessor_Type = Link
_VctLogicalProcessor_Object = MibTableColumn
vctLogicalProcessor = _VctLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 10, 1, 1),
    _VctLogicalProcessor_Type()
)
vctLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctLogicalProcessor.setStatus("mandatory")


class _VctVcName_Type(Integer32):
    """Custom type vctVcName based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fvc", 2),
          ("gvc", 1))
    )


_VctVcName_Type.__name__ = "Integer32"
_VctVcName_Object = MibTableColumn
vctVcName = _VctVcName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 5130, 10, 1, 2),
    _VctVcName_Type()
)
vctVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctVcName.setStatus("mandatory")
_VcTesterMIB_ObjectIdentity = ObjectIdentity
vcTesterMIB = _VcTesterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34)
)
_VcTesterGroup_ObjectIdentity = ObjectIdentity
vcTesterGroup = _VcTesterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 1)
)
_VcTesterGroupBE_ObjectIdentity = ObjectIdentity
vcTesterGroupBE = _VcTesterGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 1, 5)
)
_VcTesterGroupBE01_ObjectIdentity = ObjectIdentity
vcTesterGroupBE01 = _VcTesterGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 1, 5, 2)
)
_VcTesterGroupBE01A_ObjectIdentity = ObjectIdentity
vcTesterGroupBE01A = _VcTesterGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 1, 5, 2, 2)
)
_VcTesterCapabilities_ObjectIdentity = ObjectIdentity
vcTesterCapabilities = _VcTesterCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 3)
)
_VcTesterCapabilitiesBE_ObjectIdentity = ObjectIdentity
vcTesterCapabilitiesBE = _VcTesterCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 3, 5)
)
_VcTesterCapabilitiesBE01_ObjectIdentity = ObjectIdentity
vcTesterCapabilitiesBE01 = _VcTesterCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 3, 5, 2)
)
_VcTesterCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
vcTesterCapabilitiesBE01A = _VcTesterCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 34, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VcTesterMIB",
    **{"vct": vct,
       "vctRowStatusTable": vctRowStatusTable,
       "vctRowStatusEntry": vctRowStatusEntry,
       "vctRowStatus": vctRowStatus,
       "vctComponentName": vctComponentName,
       "vctStorageType": vctStorageType,
       "vctIndex": vctIndex,
       "vctDna": vctDna,
       "vctDnaRowStatusTable": vctDnaRowStatusTable,
       "vctDnaRowStatusEntry": vctDnaRowStatusEntry,
       "vctDnaRowStatus": vctDnaRowStatus,
       "vctDnaComponentName": vctDnaComponentName,
       "vctDnaStorageType": vctDnaStorageType,
       "vctDnaIndex": vctDnaIndex,
       "vctDnaCug": vctDnaCug,
       "vctDnaCugRowStatusTable": vctDnaCugRowStatusTable,
       "vctDnaCugRowStatusEntry": vctDnaCugRowStatusEntry,
       "vctDnaCugRowStatus": vctDnaCugRowStatus,
       "vctDnaCugComponentName": vctDnaCugComponentName,
       "vctDnaCugStorageType": vctDnaCugStorageType,
       "vctDnaCugIndex": vctDnaCugIndex,
       "vctDnaCugCugOptionsTable": vctDnaCugCugOptionsTable,
       "vctDnaCugCugOptionsEntry": vctDnaCugCugOptionsEntry,
       "vctDnaCugType": vctDnaCugType,
       "vctDnaCugDnic": vctDnaCugDnic,
       "vctDnaCugInterlockCode": vctDnaCugInterlockCode,
       "vctDnaCugPreferential": vctDnaCugPreferential,
       "vctDnaCugOutCalls": vctDnaCugOutCalls,
       "vctDnaCugIncCalls": vctDnaCugIncCalls,
       "vctDnaCugPrivileged": vctDnaCugPrivileged,
       "vctDnaHgM": vctDnaHgM,
       "vctDnaHgMRowStatusTable": vctDnaHgMRowStatusTable,
       "vctDnaHgMRowStatusEntry": vctDnaHgMRowStatusEntry,
       "vctDnaHgMRowStatus": vctDnaHgMRowStatus,
       "vctDnaHgMComponentName": vctDnaHgMComponentName,
       "vctDnaHgMStorageType": vctDnaHgMStorageType,
       "vctDnaHgMIndex": vctDnaHgMIndex,
       "vctDnaHgMHgAddr": vctDnaHgMHgAddr,
       "vctDnaHgMHgAddrRowStatusTable": vctDnaHgMHgAddrRowStatusTable,
       "vctDnaHgMHgAddrRowStatusEntry": vctDnaHgMHgAddrRowStatusEntry,
       "vctDnaHgMHgAddrRowStatus": vctDnaHgMHgAddrRowStatus,
       "vctDnaHgMHgAddrComponentName": vctDnaHgMHgAddrComponentName,
       "vctDnaHgMHgAddrStorageType": vctDnaHgMHgAddrStorageType,
       "vctDnaHgMHgAddrIndex": vctDnaHgMHgAddrIndex,
       "vctDnaHgMHgAddrAddrTable": vctDnaHgMHgAddrAddrTable,
       "vctDnaHgMHgAddrAddrEntry": vctDnaHgMHgAddrAddrEntry,
       "vctDnaHgMHgAddrNumberingPlanIndicator": vctDnaHgMHgAddrNumberingPlanIndicator,
       "vctDnaHgMHgAddrDataNetworkAddress": vctDnaHgMHgAddrDataNetworkAddress,
       "vctDnaHgMIfTable": vctDnaHgMIfTable,
       "vctDnaHgMIfEntry": vctDnaHgMIfEntry,
       "vctDnaHgMAvailabilityUpdateThreshold": vctDnaHgMAvailabilityUpdateThreshold,
       "vctDnaHgMOpTable": vctDnaHgMOpTable,
       "vctDnaHgMOpEntry": vctDnaHgMOpEntry,
       "vctDnaHgMMaxAvailableChannels": vctDnaHgMMaxAvailableChannels,
       "vctDnaHgMAvailableChannels": vctDnaHgMAvailableChannels,
       "vctDnaHgMAvailabilityDelta": vctDnaHgMAvailabilityDelta,
       "vctDnaAddressTable": vctDnaAddressTable,
       "vctDnaAddressEntry": vctDnaAddressEntry,
       "vctDnaNumberingPlanIndicator": vctDnaNumberingPlanIndicator,
       "vctDnaDataNetworkAddress": vctDnaDataNetworkAddress,
       "vctDnaOutgoingOptionsTable": vctDnaOutgoingOptionsTable,
       "vctDnaOutgoingOptionsEntry": vctDnaOutgoingOptionsEntry,
       "vctDnaOutCalls": vctDnaOutCalls,
       "vctDnaOutNormalCharge": vctDnaOutNormalCharge,
       "vctDnaOutReverseCharge": vctDnaOutReverseCharge,
       "vctDnaOutForceReverseCharge": vctDnaOutForceReverseCharge,
       "vctDnaOutNormalPriority": vctDnaOutNormalPriority,
       "vctDnaOutHighPriority": vctDnaOutHighPriority,
       "vctDnaOutDefaultPriority": vctDnaOutDefaultPriority,
       "vctDnaOutIntl": vctDnaOutIntl,
       "vctDnaOutFsRestrictedResponse": vctDnaOutFsRestrictedResponse,
       "vctDnaOutFsUnrestrictedResponse": vctDnaOutFsUnrestrictedResponse,
       "vctDnaOutDefaultPathSensitivity": vctDnaOutDefaultPathSensitivity,
       "vctDnaOutPathSensitivityOverRide": vctDnaOutPathSensitivityOverRide,
       "vctDnaOutPathSensitivitySignal": vctDnaOutPathSensitivitySignal,
       "vctDnaOutDefaultPathReliability": vctDnaOutDefaultPathReliability,
       "vctDnaOutPathReliabilityOverRide": vctDnaOutPathReliabilityOverRide,
       "vctDnaOutPathReliabilitySignal": vctDnaOutPathReliabilitySignal,
       "vctDnaOutAccess": vctDnaOutAccess,
       "vctDnaDefaultTransferPriority": vctDnaDefaultTransferPriority,
       "vctDnaTransferPriorityOverRide": vctDnaTransferPriorityOverRide,
       "vctDnaIncomingOptionsTable": vctDnaIncomingOptionsTable,
       "vctDnaIncomingOptionsEntry": vctDnaIncomingOptionsEntry,
       "vctDnaIncCalls": vctDnaIncCalls,
       "vctDnaIncHighPriorityReverseCharge": vctDnaIncHighPriorityReverseCharge,
       "vctDnaIncNormalPriorityReverseCharge": vctDnaIncNormalPriorityReverseCharge,
       "vctDnaIncIntlNormalCharge": vctDnaIncIntlNormalCharge,
       "vctDnaIncIntlReverseCharge": vctDnaIncIntlReverseCharge,
       "vctDnaIncFastSelect": vctDnaIncFastSelect,
       "vctDnaIncSameService": vctDnaIncSameService,
       "vctDnaIncChargeTransfer": vctDnaIncChargeTransfer,
       "vctDnaIncAccess": vctDnaIncAccess,
       "vctDnaCallOptionsTable": vctDnaCallOptionsTable,
       "vctDnaCallOptionsEntry": vctDnaCallOptionsEntry,
       "vctDnaServiceCategory": vctDnaServiceCategory,
       "vctDnaPacketSizes": vctDnaPacketSizes,
       "vctDnaDefaultRecvFrmNetworkPacketSize": vctDnaDefaultRecvFrmNetworkPacketSize,
       "vctDnaDefaultSendToNetworkPacketSize": vctDnaDefaultSendToNetworkPacketSize,
       "vctDnaDefaultRecvFrmNetworkThruputClass": vctDnaDefaultRecvFrmNetworkThruputClass,
       "vctDnaDefaultSendToNetworkThruputClass": vctDnaDefaultSendToNetworkThruputClass,
       "vctDnaDefaultRecvFrmNetworkWindowSize": vctDnaDefaultRecvFrmNetworkWindowSize,
       "vctDnaDefaultSendToNetworkWindowSize": vctDnaDefaultSendToNetworkWindowSize,
       "vctDnaPacketSizeNegotiation": vctDnaPacketSizeNegotiation,
       "vctDnaCugFormat": vctDnaCugFormat,
       "vctDnaCug0AsNonCugCall": vctDnaCug0AsNonCugCall,
       "vctDnaSignalPreferentialCugToLink": vctDnaSignalPreferentialCugToLink,
       "vctDnaSignalIntlAddressToLink": vctDnaSignalIntlAddressToLink,
       "vctDnaFastSelectCallsOnly": vctDnaFastSelectCallsOnly,
       "vctDnaPreselectRpoa": vctDnaPreselectRpoa,
       "vctDnaAccountClass": vctDnaAccountClass,
       "vctDnaAccountCollection": vctDnaAccountCollection,
       "vctDnaServiceExchange": vctDnaServiceExchange,
       "vctDnaEgressAccounting": vctDnaEgressAccounting,
       "vctDnaRpoa": vctDnaRpoa,
       "vctDnaDataPath": vctDnaDataPath,
       "vctDc": vctDc,
       "vctDcRowStatusTable": vctDcRowStatusTable,
       "vctDcRowStatusEntry": vctDcRowStatusEntry,
       "vctDcRowStatus": vctDcRowStatus,
       "vctDcComponentName": vctDcComponentName,
       "vctDcStorageType": vctDcStorageType,
       "vctDcIndex": vctDcIndex,
       "vctDcOptionsTable": vctDcOptionsTable,
       "vctDcOptionsEntry": vctDcOptionsEntry,
       "vctDcLocalNpi": vctDcLocalNpi,
       "vctDcLocalDna": vctDcLocalDna,
       "vctDcRemoteNpi": vctDcRemoteNpi,
       "vctDcRemoteDna": vctDcRemoteDna,
       "vctDcRemoteLcn": vctDcRemoteLcn,
       "vctDcType": vctDcType,
       "vctDcSvcAutoCallRetry": vctDcSvcAutoCallRetry,
       "vctDcUserData": vctDcUserData,
       "vctDcDiscardPriority": vctDcDiscardPriority,
       "vctDcDataPath": vctDcDataPath,
       "vctDcCugIndex": vctDcCugIndex,
       "vctDcCugType": vctDcCugType,
       "vctDcCfaTable": vctDcCfaTable,
       "vctDcCfaEntry": vctDcCfaEntry,
       "vctDcCfaIndex": vctDcCfaIndex,
       "vctDcCfaValue": vctDcCfaValue,
       "vctDcCfaRowStatus": vctDcCfaRowStatus,
       "vctDcDfaTable": vctDcDfaTable,
       "vctDcDfaEntry": vctDcDfaEntry,
       "vctDcDfaIndex": vctDcDfaIndex,
       "vctDcDfaValue": vctDcDfaValue,
       "vctDcDfaRowStatus": vctDcDfaRowStatus,
       "vctDcNfaTable": vctDcNfaTable,
       "vctDcNfaEntry": vctDcNfaEntry,
       "vctDcNfaIndex": vctDcNfaIndex,
       "vctDcNfaValue": vctDcNfaValue,
       "vctDcNfaRowStatus": vctDcNfaRowStatus,
       "vctDcIfaTable": vctDcIfaTable,
       "vctDcIfaEntry": vctDcIfaEntry,
       "vctDcIfaIndex": vctDcIfaIndex,
       "vctDcIfaValue": vctDcIfaValue,
       "vctDcIfaRowStatus": vctDcIfaRowStatus,
       "vctVc": vctVc,
       "vctVcRowStatusTable": vctVcRowStatusTable,
       "vctVcRowStatusEntry": vctVcRowStatusEntry,
       "vctVcRowStatus": vctVcRowStatus,
       "vctVcComponentName": vctVcComponentName,
       "vctVcStorageType": vctVcStorageType,
       "vctVcIndex": vctVcIndex,
       "vctVcCadTable": vctVcCadTable,
       "vctVcCadEntry": vctVcCadEntry,
       "vctVcType": vctVcType,
       "vctVcState": vctVcState,
       "vctVcPreviousState": vctVcPreviousState,
       "vctVcDiagnosticCode": vctVcDiagnosticCode,
       "vctVcPreviousDiagnosticCode": vctVcPreviousDiagnosticCode,
       "vctVcCalledNpi": vctVcCalledNpi,
       "vctVcCalledDna": vctVcCalledDna,
       "vctVcCalledLcn": vctVcCalledLcn,
       "vctVcCallingNpi": vctVcCallingNpi,
       "vctVcCallingDna": vctVcCallingDna,
       "vctVcCallingLcn": vctVcCallingLcn,
       "vctVcAccountingEnabled": vctVcAccountingEnabled,
       "vctVcFastSelectCall": vctVcFastSelectCall,
       "vctVcLocalRxPktSize": vctVcLocalRxPktSize,
       "vctVcLocalTxPktSize": vctVcLocalTxPktSize,
       "vctVcLocalTxWindowSize": vctVcLocalTxWindowSize,
       "vctVcLocalRxWindowSize": vctVcLocalRxWindowSize,
       "vctVcPathReliability": vctVcPathReliability,
       "vctVcAccountingEnd": vctVcAccountingEnd,
       "vctVcPriority": vctVcPriority,
       "vctVcSegmentSize": vctVcSegmentSize,
       "vctVcSubnetTxPktSize": vctVcSubnetTxPktSize,
       "vctVcSubnetTxWindowSize": vctVcSubnetTxWindowSize,
       "vctVcSubnetRxPktSize": vctVcSubnetRxPktSize,
       "vctVcSubnetRxWindowSize": vctVcSubnetRxWindowSize,
       "vctVcMaxSubnetPktSize": vctVcMaxSubnetPktSize,
       "vctVcTransferPriorityToNetwork": vctVcTransferPriorityToNetwork,
       "vctVcTransferPriorityFromNetwork": vctVcTransferPriorityFromNetwork,
       "vctVcIntdTable": vctVcIntdTable,
       "vctVcIntdEntry": vctVcIntdEntry,
       "vctVcCallReferenceNumber": vctVcCallReferenceNumber,
       "vctVcElapsedTimeTillNow": vctVcElapsedTimeTillNow,
       "vctVcSegmentsRx": vctVcSegmentsRx,
       "vctVcSegmentsSent": vctVcSegmentsSent,
       "vctVcStartTime": vctVcStartTime,
       "vctVcStatsTable": vctVcStatsTable,
       "vctVcStatsEntry": vctVcStatsEntry,
       "vctVcAckStackingTimeouts": vctVcAckStackingTimeouts,
       "vctVcOutOfRangeFrmFromSubnet": vctVcOutOfRangeFrmFromSubnet,
       "vctVcDuplicatesFromSubnet": vctVcDuplicatesFromSubnet,
       "vctVcFrmRetryTimeouts": vctVcFrmRetryTimeouts,
       "vctVcPeakRetryQueueSize": vctVcPeakRetryQueueSize,
       "vctVcPeakOoSeqQueueSize": vctVcPeakOoSeqQueueSize,
       "vctVcPeakOoSeqFrmForwarded": vctVcPeakOoSeqFrmForwarded,
       "vctVcPeakStackedAcksRx": vctVcPeakStackedAcksRx,
       "vctVcSubnetRecoveries": vctVcSubnetRecoveries,
       "vctVcWindowClosuresToSubnet": vctVcWindowClosuresToSubnet,
       "vctVcWindowClosuresFromSubnet": vctVcWindowClosuresFromSubnet,
       "vctVcWrTriggers": vctVcWrTriggers,
       "vctVcfr": vctVcfr,
       "vctVcfrRowStatusTable": vctVcfrRowStatusTable,
       "vctVcfrRowStatusEntry": vctVcfrRowStatusEntry,
       "vctVcfrRowStatus": vctVcfrRowStatus,
       "vctVcfrComponentName": vctVcfrComponentName,
       "vctVcfrStorageType": vctVcfrStorageType,
       "vctVcfrIndex": vctVcfrIndex,
       "vctVcfrCadTable": vctVcfrCadTable,
       "vctVcfrCadEntry": vctVcfrCadEntry,
       "vctVcfrType": vctVcfrType,
       "vctVcfrState": vctVcfrState,
       "vctVcfrPreviousState": vctVcfrPreviousState,
       "vctVcfrDiagnosticCode": vctVcfrDiagnosticCode,
       "vctVcfrPreviousDiagnosticCode": vctVcfrPreviousDiagnosticCode,
       "vctVcfrCalledNpi": vctVcfrCalledNpi,
       "vctVcfrCalledDna": vctVcfrCalledDna,
       "vctVcfrCalledLcn": vctVcfrCalledLcn,
       "vctVcfrCallingNpi": vctVcfrCallingNpi,
       "vctVcfrCallingDna": vctVcfrCallingDna,
       "vctVcfrCallingLcn": vctVcfrCallingLcn,
       "vctVcfrAccountingEnabled": vctVcfrAccountingEnabled,
       "vctVcfrFastSelectCall": vctVcfrFastSelectCall,
       "vctVcfrPathReliability": vctVcfrPathReliability,
       "vctVcfrAccountingEnd": vctVcfrAccountingEnd,
       "vctVcfrPriority": vctVcfrPriority,
       "vctVcfrSegmentSize": vctVcfrSegmentSize,
       "vctVcfrMaxSubnetPktSize": vctVcfrMaxSubnetPktSize,
       "vctVcfrRcosToNetwork": vctVcfrRcosToNetwork,
       "vctVcfrRcosFromNetwork": vctVcfrRcosFromNetwork,
       "vctVcfrEmissionPriorityToNetwork": vctVcfrEmissionPriorityToNetwork,
       "vctVcfrEmissionPriorityFromNetwork": vctVcfrEmissionPriorityFromNetwork,
       "vctVcfrDataPath": vctVcfrDataPath,
       "vctVcfrIntdTable": vctVcfrIntdTable,
       "vctVcfrIntdEntry": vctVcfrIntdEntry,
       "vctVcfrCallReferenceNumber": vctVcfrCallReferenceNumber,
       "vctVcfrElapsedTimeTillNow": vctVcfrElapsedTimeTillNow,
       "vctVcfrSegmentsRx": vctVcfrSegmentsRx,
       "vctVcfrSegmentsSent": vctVcfrSegmentsSent,
       "vctVcfrStartTime": vctVcfrStartTime,
       "vctVcfrFrdTable": vctVcfrFrdTable,
       "vctVcfrFrdEntry": vctVcfrFrdEntry,
       "vctVcfrFrmCongestedToSubnet": vctVcfrFrmCongestedToSubnet,
       "vctVcfrCannotForwardToSubnet": vctVcfrCannotForwardToSubnet,
       "vctVcfrNotDataXferToSubnet": vctVcfrNotDataXferToSubnet,
       "vctVcfrOutOfRangeFrmFromSubnet": vctVcfrOutOfRangeFrmFromSubnet,
       "vctVcfrCombErrorsFromSubnet": vctVcfrCombErrorsFromSubnet,
       "vctVcfrDuplicatesFromSubnet": vctVcfrDuplicatesFromSubnet,
       "vctVcfrNotDataXferFromSubnet": vctVcfrNotDataXferFromSubnet,
       "vctVcfrFrmLossTimeouts": vctVcfrFrmLossTimeouts,
       "vctVcfrOoSeqByteCntExceeded": vctVcfrOoSeqByteCntExceeded,
       "vctVcfrPeakOoSeqPktCount": vctVcfrPeakOoSeqPktCount,
       "vctVcfrPeakOoSeqFrmForwarded": vctVcfrPeakOoSeqFrmForwarded,
       "vctVcfrSendSequenceNumber": vctVcfrSendSequenceNumber,
       "vctVcfrPktRetryTimeouts": vctVcfrPktRetryTimeouts,
       "vctVcfrPeakRetryQueueSize": vctVcfrPeakRetryQueueSize,
       "vctVcfrSubnetRecoveries": vctVcfrSubnetRecoveries,
       "vctVcfrOoSeqPktCntExceeded": vctVcfrOoSeqPktCntExceeded,
       "vctVcfrPeakOoSeqByteCount": vctVcfrPeakOoSeqByteCount,
       "vctVcfrDmepTable": vctVcfrDmepTable,
       "vctVcfrDmepEntry": vctVcfrDmepEntry,
       "vctVcfrDmepValue": vctVcfrDmepValue,
       "vctProvTable": vctProvTable,
       "vctProvEntry": vctProvEntry,
       "vctLogicalProcessor": vctLogicalProcessor,
       "vctVcName": vctVcName,
       "vcTesterMIB": vcTesterMIB,
       "vcTesterGroup": vcTesterGroup,
       "vcTesterGroupBE": vcTesterGroupBE,
       "vcTesterGroupBE01": vcTesterGroupBE01,
       "vcTesterGroupBE01A": vcTesterGroupBE01A,
       "vcTesterCapabilities": vcTesterCapabilities,
       "vcTesterCapabilitiesBE": vcTesterCapabilitiesBE,
       "vcTesterCapabilitiesBE01": vcTesterCapabilitiesBE01,
       "vcTesterCapabilitiesBE01A": vcTesterCapabilitiesBE01A}
)
