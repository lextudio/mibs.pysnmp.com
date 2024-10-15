# SNMP MIB module (Nortel-MsCarrier-MscPassport-VcTesterMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VcTesterMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:13 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated")

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

_MscVct_ObjectIdentity = ObjectIdentity
mscVct = _MscVct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130)
)
_MscVctRowStatusTable_Object = MibTable
mscVctRowStatusTable = _MscVctRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 1)
)
if mibBuilder.loadTexts:
    mscVctRowStatusTable.setStatus("mandatory")
_MscVctRowStatusEntry_Object = MibTableRow
mscVctRowStatusEntry = _MscVctRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 1, 1)
)
mscVctRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
)
if mibBuilder.loadTexts:
    mscVctRowStatusEntry.setStatus("mandatory")
_MscVctRowStatus_Type = RowStatus
_MscVctRowStatus_Object = MibTableColumn
mscVctRowStatus = _MscVctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 1, 1, 1),
    _MscVctRowStatus_Type()
)
mscVctRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctRowStatus.setStatus("mandatory")
_MscVctComponentName_Type = DisplayString
_MscVctComponentName_Object = MibTableColumn
mscVctComponentName = _MscVctComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 1, 1, 2),
    _MscVctComponentName_Type()
)
mscVctComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctComponentName.setStatus("mandatory")
_MscVctStorageType_Type = StorageType
_MscVctStorageType_Object = MibTableColumn
mscVctStorageType = _MscVctStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 1, 1, 4),
    _MscVctStorageType_Type()
)
mscVctStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctStorageType.setStatus("mandatory")


class _MscVctIndex_Type(Integer32):
    """Custom type mscVctIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVctIndex_Type.__name__ = "Integer32"
_MscVctIndex_Object = MibTableColumn
mscVctIndex = _MscVctIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 1, 1, 10),
    _MscVctIndex_Type()
)
mscVctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctIndex.setStatus("mandatory")
_MscVctDna_ObjectIdentity = ObjectIdentity
mscVctDna = _MscVctDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2)
)
_MscVctDnaRowStatusTable_Object = MibTable
mscVctDnaRowStatusTable = _MscVctDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 1)
)
if mibBuilder.loadTexts:
    mscVctDnaRowStatusTable.setStatus("mandatory")
_MscVctDnaRowStatusEntry_Object = MibTableRow
mscVctDnaRowStatusEntry = _MscVctDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 1, 1)
)
mscVctDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaRowStatusEntry.setStatus("mandatory")
_MscVctDnaRowStatus_Type = RowStatus
_MscVctDnaRowStatus_Object = MibTableColumn
mscVctDnaRowStatus = _MscVctDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 1, 1, 1),
    _MscVctDnaRowStatus_Type()
)
mscVctDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaRowStatus.setStatus("mandatory")
_MscVctDnaComponentName_Type = DisplayString
_MscVctDnaComponentName_Object = MibTableColumn
mscVctDnaComponentName = _MscVctDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 1, 1, 2),
    _MscVctDnaComponentName_Type()
)
mscVctDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaComponentName.setStatus("mandatory")
_MscVctDnaStorageType_Type = StorageType
_MscVctDnaStorageType_Object = MibTableColumn
mscVctDnaStorageType = _MscVctDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 1, 1, 4),
    _MscVctDnaStorageType_Type()
)
mscVctDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaStorageType.setStatus("mandatory")
_MscVctDnaIndex_Type = NonReplicated
_MscVctDnaIndex_Object = MibTableColumn
mscVctDnaIndex = _MscVctDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 1, 1, 10),
    _MscVctDnaIndex_Type()
)
mscVctDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDnaIndex.setStatus("mandatory")
_MscVctDnaCug_ObjectIdentity = ObjectIdentity
mscVctDnaCug = _MscVctDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2)
)
_MscVctDnaCugRowStatusTable_Object = MibTable
mscVctDnaCugRowStatusTable = _MscVctDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVctDnaCugRowStatusTable.setStatus("mandatory")
_MscVctDnaCugRowStatusEntry_Object = MibTableRow
mscVctDnaCugRowStatusEntry = _MscVctDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 1, 1)
)
mscVctDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaCugRowStatusEntry.setStatus("mandatory")
_MscVctDnaCugRowStatus_Type = RowStatus
_MscVctDnaCugRowStatus_Object = MibTableColumn
mscVctDnaCugRowStatus = _MscVctDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 1, 1, 1),
    _MscVctDnaCugRowStatus_Type()
)
mscVctDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugRowStatus.setStatus("mandatory")
_MscVctDnaCugComponentName_Type = DisplayString
_MscVctDnaCugComponentName_Object = MibTableColumn
mscVctDnaCugComponentName = _MscVctDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 1, 1, 2),
    _MscVctDnaCugComponentName_Type()
)
mscVctDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaCugComponentName.setStatus("mandatory")
_MscVctDnaCugStorageType_Type = StorageType
_MscVctDnaCugStorageType_Object = MibTableColumn
mscVctDnaCugStorageType = _MscVctDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 1, 1, 4),
    _MscVctDnaCugStorageType_Type()
)
mscVctDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaCugStorageType.setStatus("mandatory")


class _MscVctDnaCugIndex_Type(Integer32):
    """Custom type mscVctDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctDnaCugIndex_Type.__name__ = "Integer32"
_MscVctDnaCugIndex_Object = MibTableColumn
mscVctDnaCugIndex = _MscVctDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 1, 1, 10),
    _MscVctDnaCugIndex_Type()
)
mscVctDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDnaCugIndex.setStatus("mandatory")
_MscVctDnaCugCugOptionsTable_Object = MibTable
mscVctDnaCugCugOptionsTable = _MscVctDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVctDnaCugCugOptionsTable.setStatus("mandatory")
_MscVctDnaCugCugOptionsEntry_Object = MibTableRow
mscVctDnaCugCugOptionsEntry = _MscVctDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1)
)
mscVctDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaCugCugOptionsEntry.setStatus("mandatory")


class _MscVctDnaCugType_Type(Integer32):
    """Custom type mscVctDnaCugType based on Integer32"""
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


_MscVctDnaCugType_Type.__name__ = "Integer32"
_MscVctDnaCugType_Object = MibTableColumn
mscVctDnaCugType = _MscVctDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1, 1),
    _MscVctDnaCugType_Type()
)
mscVctDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugType.setStatus("mandatory")


class _MscVctDnaCugDnic_Type(DigitString):
    """Custom type mscVctDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscVctDnaCugDnic_Type.__name__ = "DigitString"
_MscVctDnaCugDnic_Object = MibTableColumn
mscVctDnaCugDnic = _MscVctDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1, 2),
    _MscVctDnaCugDnic_Type()
)
mscVctDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugDnic.setStatus("mandatory")


class _MscVctDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscVctDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVctDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscVctDnaCugInterlockCode_Object = MibTableColumn
mscVctDnaCugInterlockCode = _MscVctDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1, 3),
    _MscVctDnaCugInterlockCode_Type()
)
mscVctDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugInterlockCode.setStatus("mandatory")


class _MscVctDnaCugPreferential_Type(Integer32):
    """Custom type mscVctDnaCugPreferential based on Integer32"""
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


_MscVctDnaCugPreferential_Type.__name__ = "Integer32"
_MscVctDnaCugPreferential_Object = MibTableColumn
mscVctDnaCugPreferential = _MscVctDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1, 4),
    _MscVctDnaCugPreferential_Type()
)
mscVctDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugPreferential.setStatus("mandatory")


class _MscVctDnaCugOutCalls_Type(Integer32):
    """Custom type mscVctDnaCugOutCalls based on Integer32"""
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


_MscVctDnaCugOutCalls_Type.__name__ = "Integer32"
_MscVctDnaCugOutCalls_Object = MibTableColumn
mscVctDnaCugOutCalls = _MscVctDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1, 5),
    _MscVctDnaCugOutCalls_Type()
)
mscVctDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugOutCalls.setStatus("mandatory")


class _MscVctDnaCugIncCalls_Type(Integer32):
    """Custom type mscVctDnaCugIncCalls based on Integer32"""
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


_MscVctDnaCugIncCalls_Type.__name__ = "Integer32"
_MscVctDnaCugIncCalls_Object = MibTableColumn
mscVctDnaCugIncCalls = _MscVctDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1, 6),
    _MscVctDnaCugIncCalls_Type()
)
mscVctDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugIncCalls.setStatus("mandatory")


class _MscVctDnaCugPrivileged_Type(Integer32):
    """Custom type mscVctDnaCugPrivileged based on Integer32"""
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


_MscVctDnaCugPrivileged_Type.__name__ = "Integer32"
_MscVctDnaCugPrivileged_Object = MibTableColumn
mscVctDnaCugPrivileged = _MscVctDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 2, 10, 1, 7),
    _MscVctDnaCugPrivileged_Type()
)
mscVctDnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugPrivileged.setStatus("mandatory")
_MscVctDnaHgM_ObjectIdentity = ObjectIdentity
mscVctDnaHgM = _MscVctDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3)
)
_MscVctDnaHgMRowStatusTable_Object = MibTable
mscVctDnaHgMRowStatusTable = _MscVctDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscVctDnaHgMRowStatusTable.setStatus("mandatory")
_MscVctDnaHgMRowStatusEntry_Object = MibTableRow
mscVctDnaHgMRowStatusEntry = _MscVctDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 1, 1)
)
mscVctDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaHgMRowStatusEntry.setStatus("mandatory")
_MscVctDnaHgMRowStatus_Type = RowStatus
_MscVctDnaHgMRowStatus_Object = MibTableColumn
mscVctDnaHgMRowStatus = _MscVctDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 1, 1, 1),
    _MscVctDnaHgMRowStatus_Type()
)
mscVctDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaHgMRowStatus.setStatus("mandatory")
_MscVctDnaHgMComponentName_Type = DisplayString
_MscVctDnaHgMComponentName_Object = MibTableColumn
mscVctDnaHgMComponentName = _MscVctDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 1, 1, 2),
    _MscVctDnaHgMComponentName_Type()
)
mscVctDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaHgMComponentName.setStatus("mandatory")
_MscVctDnaHgMStorageType_Type = StorageType
_MscVctDnaHgMStorageType_Object = MibTableColumn
mscVctDnaHgMStorageType = _MscVctDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 1, 1, 4),
    _MscVctDnaHgMStorageType_Type()
)
mscVctDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaHgMStorageType.setStatus("mandatory")
_MscVctDnaHgMIndex_Type = NonReplicated
_MscVctDnaHgMIndex_Object = MibTableColumn
mscVctDnaHgMIndex = _MscVctDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 1, 1, 10),
    _MscVctDnaHgMIndex_Type()
)
mscVctDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDnaHgMIndex.setStatus("mandatory")
_MscVctDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
mscVctDnaHgMHgAddr = _MscVctDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2)
)
_MscVctDnaHgMHgAddrRowStatusTable_Object = MibTable
mscVctDnaHgMHgAddrRowStatusTable = _MscVctDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_MscVctDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
mscVctDnaHgMHgAddrRowStatusEntry = _MscVctDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 1, 1)
)
mscVctDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_MscVctDnaHgMHgAddrRowStatus_Type = RowStatus
_MscVctDnaHgMHgAddrRowStatus_Object = MibTableColumn
mscVctDnaHgMHgAddrRowStatus = _MscVctDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 1, 1, 1),
    _MscVctDnaHgMHgAddrRowStatus_Type()
)
mscVctDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrRowStatus.setStatus("mandatory")
_MscVctDnaHgMHgAddrComponentName_Type = DisplayString
_MscVctDnaHgMHgAddrComponentName_Object = MibTableColumn
mscVctDnaHgMHgAddrComponentName = _MscVctDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 1, 1, 2),
    _MscVctDnaHgMHgAddrComponentName_Type()
)
mscVctDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrComponentName.setStatus("mandatory")
_MscVctDnaHgMHgAddrStorageType_Type = StorageType
_MscVctDnaHgMHgAddrStorageType_Object = MibTableColumn
mscVctDnaHgMHgAddrStorageType = _MscVctDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 1, 1, 4),
    _MscVctDnaHgMHgAddrStorageType_Type()
)
mscVctDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrStorageType.setStatus("mandatory")


class _MscVctDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type mscVctDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscVctDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_MscVctDnaHgMHgAddrIndex_Object = MibTableColumn
mscVctDnaHgMHgAddrIndex = _MscVctDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 1, 1, 10),
    _MscVctDnaHgMHgAddrIndex_Type()
)
mscVctDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrIndex.setStatus("mandatory")
_MscVctDnaHgMHgAddrAddrTable_Object = MibTable
mscVctDnaHgMHgAddrAddrTable = _MscVctDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrAddrTable.setStatus("mandatory")
_MscVctDnaHgMHgAddrAddrEntry_Object = MibTableRow
mscVctDnaHgMHgAddrAddrEntry = _MscVctDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 10, 1)
)
mscVctDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _MscVctDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type mscVctDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
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


_MscVctDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscVctDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
mscVctDnaHgMHgAddrNumberingPlanIndicator = _MscVctDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 10, 1, 1),
    _MscVctDnaHgMHgAddrNumberingPlanIndicator_Type()
)
mscVctDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _MscVctDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type mscVctDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscVctDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_MscVctDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
mscVctDnaHgMHgAddrDataNetworkAddress = _MscVctDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 2, 10, 1, 2),
    _MscVctDnaHgMHgAddrDataNetworkAddress_Type()
)
mscVctDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_MscVctDnaHgMIfTable_Object = MibTable
mscVctDnaHgMIfTable = _MscVctDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscVctDnaHgMIfTable.setStatus("mandatory")
_MscVctDnaHgMIfEntry_Object = MibTableRow
mscVctDnaHgMIfEntry = _MscVctDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 10, 1)
)
mscVctDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaHgMIfEntry.setStatus("mandatory")


class _MscVctDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type mscVctDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_MscVctDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
mscVctDnaHgMAvailabilityUpdateThreshold = _MscVctDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 10, 1, 1),
    _MscVctDnaHgMAvailabilityUpdateThreshold_Type()
)
mscVctDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_MscVctDnaHgMOpTable_Object = MibTable
mscVctDnaHgMOpTable = _MscVctDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscVctDnaHgMOpTable.setStatus("mandatory")
_MscVctDnaHgMOpEntry_Object = MibTableRow
mscVctDnaHgMOpEntry = _MscVctDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 11, 1)
)
mscVctDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaHgMOpEntry.setStatus("mandatory")


class _MscVctDnaHgMMaxAvailableChannels_Type(Unsigned32):
    """Custom type mscVctDnaHgMMaxAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctDnaHgMMaxAvailableChannels_Type.__name__ = "Unsigned32"
_MscVctDnaHgMMaxAvailableChannels_Object = MibTableColumn
mscVctDnaHgMMaxAvailableChannels = _MscVctDnaHgMMaxAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 11, 1, 1),
    _MscVctDnaHgMMaxAvailableChannels_Type()
)
mscVctDnaHgMMaxAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaHgMMaxAvailableChannels.setStatus("mandatory")


class _MscVctDnaHgMAvailableChannels_Type(Unsigned32):
    """Custom type mscVctDnaHgMAvailableChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctDnaHgMAvailableChannels_Type.__name__ = "Unsigned32"
_MscVctDnaHgMAvailableChannels_Object = MibTableColumn
mscVctDnaHgMAvailableChannels = _MscVctDnaHgMAvailableChannels_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 11, 1, 2),
    _MscVctDnaHgMAvailableChannels_Type()
)
mscVctDnaHgMAvailableChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaHgMAvailableChannels.setStatus("mandatory")


class _MscVctDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type mscVctDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4096, 4096),
    )


_MscVctDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_MscVctDnaHgMAvailabilityDelta_Object = MibTableColumn
mscVctDnaHgMAvailabilityDelta = _MscVctDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 3, 11, 1, 3),
    _MscVctDnaHgMAvailabilityDelta_Type()
)
mscVctDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDnaHgMAvailabilityDelta.setStatus("mandatory")
_MscVctDnaAddressTable_Object = MibTable
mscVctDnaAddressTable = _MscVctDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 10)
)
if mibBuilder.loadTexts:
    mscVctDnaAddressTable.setStatus("mandatory")
_MscVctDnaAddressEntry_Object = MibTableRow
mscVctDnaAddressEntry = _MscVctDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 10, 1)
)
mscVctDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaAddressEntry.setStatus("mandatory")


class _MscVctDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscVctDnaNumberingPlanIndicator based on Integer32"""
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


_MscVctDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscVctDnaNumberingPlanIndicator_Object = MibTableColumn
mscVctDnaNumberingPlanIndicator = _MscVctDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 10, 1, 1),
    _MscVctDnaNumberingPlanIndicator_Type()
)
mscVctDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscVctDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscVctDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscVctDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscVctDnaDataNetworkAddress_Object = MibTableColumn
mscVctDnaDataNetworkAddress = _MscVctDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 10, 1, 2),
    _MscVctDnaDataNetworkAddress_Type()
)
mscVctDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDataNetworkAddress.setStatus("mandatory")
_MscVctDnaOutgoingOptionsTable_Object = MibTable
mscVctDnaOutgoingOptionsTable = _MscVctDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11)
)
if mibBuilder.loadTexts:
    mscVctDnaOutgoingOptionsTable.setStatus("mandatory")
_MscVctDnaOutgoingOptionsEntry_Object = MibTableRow
mscVctDnaOutgoingOptionsEntry = _MscVctDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1)
)
mscVctDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscVctDnaOutCalls_Type(Integer32):
    """Custom type mscVctDnaOutCalls based on Integer32"""
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


_MscVctDnaOutCalls_Type.__name__ = "Integer32"
_MscVctDnaOutCalls_Object = MibTableColumn
mscVctDnaOutCalls = _MscVctDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 1),
    _MscVctDnaOutCalls_Type()
)
mscVctDnaOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutCalls.setStatus("mandatory")


class _MscVctDnaOutNormalCharge_Type(Integer32):
    """Custom type mscVctDnaOutNormalCharge based on Integer32"""
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


_MscVctDnaOutNormalCharge_Type.__name__ = "Integer32"
_MscVctDnaOutNormalCharge_Object = MibTableColumn
mscVctDnaOutNormalCharge = _MscVctDnaOutNormalCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 2),
    _MscVctDnaOutNormalCharge_Type()
)
mscVctDnaOutNormalCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutNormalCharge.setStatus("mandatory")


class _MscVctDnaOutReverseCharge_Type(Integer32):
    """Custom type mscVctDnaOutReverseCharge based on Integer32"""
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


_MscVctDnaOutReverseCharge_Type.__name__ = "Integer32"
_MscVctDnaOutReverseCharge_Object = MibTableColumn
mscVctDnaOutReverseCharge = _MscVctDnaOutReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 3),
    _MscVctDnaOutReverseCharge_Type()
)
mscVctDnaOutReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutReverseCharge.setStatus("mandatory")


class _MscVctDnaOutForceReverseCharge_Type(Integer32):
    """Custom type mscVctDnaOutForceReverseCharge based on Integer32"""
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


_MscVctDnaOutForceReverseCharge_Type.__name__ = "Integer32"
_MscVctDnaOutForceReverseCharge_Object = MibTableColumn
mscVctDnaOutForceReverseCharge = _MscVctDnaOutForceReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 4),
    _MscVctDnaOutForceReverseCharge_Type()
)
mscVctDnaOutForceReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutForceReverseCharge.setStatus("mandatory")


class _MscVctDnaOutNormalPriority_Type(Integer32):
    """Custom type mscVctDnaOutNormalPriority based on Integer32"""
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


_MscVctDnaOutNormalPriority_Type.__name__ = "Integer32"
_MscVctDnaOutNormalPriority_Object = MibTableColumn
mscVctDnaOutNormalPriority = _MscVctDnaOutNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 5),
    _MscVctDnaOutNormalPriority_Type()
)
mscVctDnaOutNormalPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutNormalPriority.setStatus("mandatory")


class _MscVctDnaOutHighPriority_Type(Integer32):
    """Custom type mscVctDnaOutHighPriority based on Integer32"""
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


_MscVctDnaOutHighPriority_Type.__name__ = "Integer32"
_MscVctDnaOutHighPriority_Object = MibTableColumn
mscVctDnaOutHighPriority = _MscVctDnaOutHighPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 6),
    _MscVctDnaOutHighPriority_Type()
)
mscVctDnaOutHighPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutHighPriority.setStatus("mandatory")


class _MscVctDnaOutDefaultPriority_Type(Integer32):
    """Custom type mscVctDnaOutDefaultPriority based on Integer32"""
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


_MscVctDnaOutDefaultPriority_Type.__name__ = "Integer32"
_MscVctDnaOutDefaultPriority_Object = MibTableColumn
mscVctDnaOutDefaultPriority = _MscVctDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 7),
    _MscVctDnaOutDefaultPriority_Type()
)
mscVctDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutDefaultPriority.setStatus("mandatory")


class _MscVctDnaOutIntl_Type(Integer32):
    """Custom type mscVctDnaOutIntl based on Integer32"""
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


_MscVctDnaOutIntl_Type.__name__ = "Integer32"
_MscVctDnaOutIntl_Object = MibTableColumn
mscVctDnaOutIntl = _MscVctDnaOutIntl_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 8),
    _MscVctDnaOutIntl_Type()
)
mscVctDnaOutIntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutIntl.setStatus("mandatory")


class _MscVctDnaOutFsRestrictedResponse_Type(Integer32):
    """Custom type mscVctDnaOutFsRestrictedResponse based on Integer32"""
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


_MscVctDnaOutFsRestrictedResponse_Type.__name__ = "Integer32"
_MscVctDnaOutFsRestrictedResponse_Object = MibTableColumn
mscVctDnaOutFsRestrictedResponse = _MscVctDnaOutFsRestrictedResponse_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 9),
    _MscVctDnaOutFsRestrictedResponse_Type()
)
mscVctDnaOutFsRestrictedResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutFsRestrictedResponse.setStatus("mandatory")


class _MscVctDnaOutFsUnrestrictedResponse_Type(Integer32):
    """Custom type mscVctDnaOutFsUnrestrictedResponse based on Integer32"""
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


_MscVctDnaOutFsUnrestrictedResponse_Type.__name__ = "Integer32"
_MscVctDnaOutFsUnrestrictedResponse_Object = MibTableColumn
mscVctDnaOutFsUnrestrictedResponse = _MscVctDnaOutFsUnrestrictedResponse_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 10),
    _MscVctDnaOutFsUnrestrictedResponse_Type()
)
mscVctDnaOutFsUnrestrictedResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutFsUnrestrictedResponse.setStatus("mandatory")


class _MscVctDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type mscVctDnaOutDefaultPathSensitivity based on Integer32"""
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


_MscVctDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_MscVctDnaOutDefaultPathSensitivity_Object = MibTableColumn
mscVctDnaOutDefaultPathSensitivity = _MscVctDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 11),
    _MscVctDnaOutDefaultPathSensitivity_Type()
)
mscVctDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _MscVctDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type mscVctDnaOutPathSensitivityOverRide based on Integer32"""
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


_MscVctDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_MscVctDnaOutPathSensitivityOverRide_Object = MibTableColumn
mscVctDnaOutPathSensitivityOverRide = _MscVctDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 12),
    _MscVctDnaOutPathSensitivityOverRide_Type()
)
mscVctDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _MscVctDnaOutPathSensitivitySignal_Type(Integer32):
    """Custom type mscVctDnaOutPathSensitivitySignal based on Integer32"""
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


_MscVctDnaOutPathSensitivitySignal_Type.__name__ = "Integer32"
_MscVctDnaOutPathSensitivitySignal_Object = MibTableColumn
mscVctDnaOutPathSensitivitySignal = _MscVctDnaOutPathSensitivitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 13),
    _MscVctDnaOutPathSensitivitySignal_Type()
)
mscVctDnaOutPathSensitivitySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutPathSensitivitySignal.setStatus("mandatory")


class _MscVctDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type mscVctDnaOutDefaultPathReliability based on Integer32"""
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


_MscVctDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_MscVctDnaOutDefaultPathReliability_Object = MibTableColumn
mscVctDnaOutDefaultPathReliability = _MscVctDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 14),
    _MscVctDnaOutDefaultPathReliability_Type()
)
mscVctDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutDefaultPathReliability.setStatus("mandatory")


class _MscVctDnaOutPathReliabilityOverRide_Type(Integer32):
    """Custom type mscVctDnaOutPathReliabilityOverRide based on Integer32"""
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


_MscVctDnaOutPathReliabilityOverRide_Type.__name__ = "Integer32"
_MscVctDnaOutPathReliabilityOverRide_Object = MibTableColumn
mscVctDnaOutPathReliabilityOverRide = _MscVctDnaOutPathReliabilityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 15),
    _MscVctDnaOutPathReliabilityOverRide_Type()
)
mscVctDnaOutPathReliabilityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutPathReliabilityOverRide.setStatus("mandatory")


class _MscVctDnaOutPathReliabilitySignal_Type(Integer32):
    """Custom type mscVctDnaOutPathReliabilitySignal based on Integer32"""
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


_MscVctDnaOutPathReliabilitySignal_Type.__name__ = "Integer32"
_MscVctDnaOutPathReliabilitySignal_Object = MibTableColumn
mscVctDnaOutPathReliabilitySignal = _MscVctDnaOutPathReliabilitySignal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 16),
    _MscVctDnaOutPathReliabilitySignal_Type()
)
mscVctDnaOutPathReliabilitySignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutPathReliabilitySignal.setStatus("mandatory")


class _MscVctDnaOutAccess_Type(Integer32):
    """Custom type mscVctDnaOutAccess based on Integer32"""
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


_MscVctDnaOutAccess_Type.__name__ = "Integer32"
_MscVctDnaOutAccess_Object = MibTableColumn
mscVctDnaOutAccess = _MscVctDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 17),
    _MscVctDnaOutAccess_Type()
)
mscVctDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaOutAccess.setStatus("mandatory")


class _MscVctDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mscVctDnaDefaultTransferPriority based on Integer32"""
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


_MscVctDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MscVctDnaDefaultTransferPriority_Object = MibTableColumn
mscVctDnaDefaultTransferPriority = _MscVctDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 18),
    _MscVctDnaDefaultTransferPriority_Type()
)
mscVctDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDefaultTransferPriority.setStatus("mandatory")


class _MscVctDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type mscVctDnaTransferPriorityOverRide based on Integer32"""
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


_MscVctDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_MscVctDnaTransferPriorityOverRide_Object = MibTableColumn
mscVctDnaTransferPriorityOverRide = _MscVctDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 11, 1, 19),
    _MscVctDnaTransferPriorityOverRide_Type()
)
mscVctDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaTransferPriorityOverRide.setStatus("mandatory")
_MscVctDnaIncomingOptionsTable_Object = MibTable
mscVctDnaIncomingOptionsTable = _MscVctDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12)
)
if mibBuilder.loadTexts:
    mscVctDnaIncomingOptionsTable.setStatus("mandatory")
_MscVctDnaIncomingOptionsEntry_Object = MibTableRow
mscVctDnaIncomingOptionsEntry = _MscVctDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1)
)
mscVctDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscVctDnaIncCalls_Type(Integer32):
    """Custom type mscVctDnaIncCalls based on Integer32"""
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


_MscVctDnaIncCalls_Type.__name__ = "Integer32"
_MscVctDnaIncCalls_Object = MibTableColumn
mscVctDnaIncCalls = _MscVctDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 1),
    _MscVctDnaIncCalls_Type()
)
mscVctDnaIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncCalls.setStatus("mandatory")


class _MscVctDnaIncHighPriorityReverseCharge_Type(Integer32):
    """Custom type mscVctDnaIncHighPriorityReverseCharge based on Integer32"""
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


_MscVctDnaIncHighPriorityReverseCharge_Type.__name__ = "Integer32"
_MscVctDnaIncHighPriorityReverseCharge_Object = MibTableColumn
mscVctDnaIncHighPriorityReverseCharge = _MscVctDnaIncHighPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 2),
    _MscVctDnaIncHighPriorityReverseCharge_Type()
)
mscVctDnaIncHighPriorityReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncHighPriorityReverseCharge.setStatus("mandatory")


class _MscVctDnaIncNormalPriorityReverseCharge_Type(Integer32):
    """Custom type mscVctDnaIncNormalPriorityReverseCharge based on Integer32"""
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


_MscVctDnaIncNormalPriorityReverseCharge_Type.__name__ = "Integer32"
_MscVctDnaIncNormalPriorityReverseCharge_Object = MibTableColumn
mscVctDnaIncNormalPriorityReverseCharge = _MscVctDnaIncNormalPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 3),
    _MscVctDnaIncNormalPriorityReverseCharge_Type()
)
mscVctDnaIncNormalPriorityReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncNormalPriorityReverseCharge.setStatus("mandatory")


class _MscVctDnaIncIntlNormalCharge_Type(Integer32):
    """Custom type mscVctDnaIncIntlNormalCharge based on Integer32"""
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


_MscVctDnaIncIntlNormalCharge_Type.__name__ = "Integer32"
_MscVctDnaIncIntlNormalCharge_Object = MibTableColumn
mscVctDnaIncIntlNormalCharge = _MscVctDnaIncIntlNormalCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 4),
    _MscVctDnaIncIntlNormalCharge_Type()
)
mscVctDnaIncIntlNormalCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncIntlNormalCharge.setStatus("mandatory")


class _MscVctDnaIncIntlReverseCharge_Type(Integer32):
    """Custom type mscVctDnaIncIntlReverseCharge based on Integer32"""
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


_MscVctDnaIncIntlReverseCharge_Type.__name__ = "Integer32"
_MscVctDnaIncIntlReverseCharge_Object = MibTableColumn
mscVctDnaIncIntlReverseCharge = _MscVctDnaIncIntlReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 5),
    _MscVctDnaIncIntlReverseCharge_Type()
)
mscVctDnaIncIntlReverseCharge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncIntlReverseCharge.setStatus("mandatory")


class _MscVctDnaIncFastSelect_Type(Integer32):
    """Custom type mscVctDnaIncFastSelect based on Integer32"""
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


_MscVctDnaIncFastSelect_Type.__name__ = "Integer32"
_MscVctDnaIncFastSelect_Object = MibTableColumn
mscVctDnaIncFastSelect = _MscVctDnaIncFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 6),
    _MscVctDnaIncFastSelect_Type()
)
mscVctDnaIncFastSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncFastSelect.setStatus("mandatory")


class _MscVctDnaIncSameService_Type(Integer32):
    """Custom type mscVctDnaIncSameService based on Integer32"""
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


_MscVctDnaIncSameService_Type.__name__ = "Integer32"
_MscVctDnaIncSameService_Object = MibTableColumn
mscVctDnaIncSameService = _MscVctDnaIncSameService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 7),
    _MscVctDnaIncSameService_Type()
)
mscVctDnaIncSameService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncSameService.setStatus("mandatory")


class _MscVctDnaIncChargeTransfer_Type(Integer32):
    """Custom type mscVctDnaIncChargeTransfer based on Integer32"""
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


_MscVctDnaIncChargeTransfer_Type.__name__ = "Integer32"
_MscVctDnaIncChargeTransfer_Object = MibTableColumn
mscVctDnaIncChargeTransfer = _MscVctDnaIncChargeTransfer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 8),
    _MscVctDnaIncChargeTransfer_Type()
)
mscVctDnaIncChargeTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncChargeTransfer.setStatus("mandatory")


class _MscVctDnaIncAccess_Type(Integer32):
    """Custom type mscVctDnaIncAccess based on Integer32"""
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


_MscVctDnaIncAccess_Type.__name__ = "Integer32"
_MscVctDnaIncAccess_Object = MibTableColumn
mscVctDnaIncAccess = _MscVctDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 12, 1, 9),
    _MscVctDnaIncAccess_Type()
)
mscVctDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaIncAccess.setStatus("mandatory")
_MscVctDnaCallOptionsTable_Object = MibTable
mscVctDnaCallOptionsTable = _MscVctDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13)
)
if mibBuilder.loadTexts:
    mscVctDnaCallOptionsTable.setStatus("mandatory")
_MscVctDnaCallOptionsEntry_Object = MibTableRow
mscVctDnaCallOptionsEntry = _MscVctDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1)
)
mscVctDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDnaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDnaCallOptionsEntry.setStatus("mandatory")


class _MscVctDnaServiceCategory_Type(Integer32):
    """Custom type mscVctDnaServiceCategory based on Integer32"""
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


_MscVctDnaServiceCategory_Type.__name__ = "Integer32"
_MscVctDnaServiceCategory_Object = MibTableColumn
mscVctDnaServiceCategory = _MscVctDnaServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 1),
    _MscVctDnaServiceCategory_Type()
)
mscVctDnaServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaServiceCategory.setStatus("mandatory")


class _MscVctDnaPacketSizes_Type(OctetString):
    """Custom type mscVctDnaPacketSizes based on OctetString"""
    defaultHexValue = "1c00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVctDnaPacketSizes_Type.__name__ = "OctetString"
_MscVctDnaPacketSizes_Object = MibTableColumn
mscVctDnaPacketSizes = _MscVctDnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 2),
    _MscVctDnaPacketSizes_Type()
)
mscVctDnaPacketSizes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaPacketSizes.setStatus("mandatory")


class _MscVctDnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type mscVctDnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
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


_MscVctDnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_MscVctDnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
mscVctDnaDefaultRecvFrmNetworkPacketSize = _MscVctDnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 3),
    _MscVctDnaDefaultRecvFrmNetworkPacketSize_Type()
)
mscVctDnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _MscVctDnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type mscVctDnaDefaultSendToNetworkPacketSize based on Integer32"""
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


_MscVctDnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_MscVctDnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
mscVctDnaDefaultSendToNetworkPacketSize = _MscVctDnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 4),
    _MscVctDnaDefaultSendToNetworkPacketSize_Type()
)
mscVctDnaDefaultSendToNetworkPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _MscVctDnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type mscVctDnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 15),
    )


_MscVctDnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscVctDnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
mscVctDnaDefaultRecvFrmNetworkThruputClass = _MscVctDnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 5),
    _MscVctDnaDefaultRecvFrmNetworkThruputClass_Type()
)
mscVctDnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _MscVctDnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type mscVctDnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscVctDnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscVctDnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
mscVctDnaDefaultSendToNetworkThruputClass = _MscVctDnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 6),
    _MscVctDnaDefaultSendToNetworkThruputClass_Type()
)
mscVctDnaDefaultSendToNetworkThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _MscVctDnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type mscVctDnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVctDnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscVctDnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
mscVctDnaDefaultRecvFrmNetworkWindowSize = _MscVctDnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 7),
    _MscVctDnaDefaultRecvFrmNetworkWindowSize_Type()
)
mscVctDnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _MscVctDnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type mscVctDnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscVctDnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscVctDnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
mscVctDnaDefaultSendToNetworkWindowSize = _MscVctDnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 8),
    _MscVctDnaDefaultSendToNetworkWindowSize_Type()
)
mscVctDnaDefaultSendToNetworkWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _MscVctDnaPacketSizeNegotiation_Type(Integer32):
    """Custom type mscVctDnaPacketSizeNegotiation based on Integer32"""
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


_MscVctDnaPacketSizeNegotiation_Type.__name__ = "Integer32"
_MscVctDnaPacketSizeNegotiation_Object = MibTableColumn
mscVctDnaPacketSizeNegotiation = _MscVctDnaPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 9),
    _MscVctDnaPacketSizeNegotiation_Type()
)
mscVctDnaPacketSizeNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaPacketSizeNegotiation.setStatus("mandatory")


class _MscVctDnaCugFormat_Type(Integer32):
    """Custom type mscVctDnaCugFormat based on Integer32"""
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


_MscVctDnaCugFormat_Type.__name__ = "Integer32"
_MscVctDnaCugFormat_Object = MibTableColumn
mscVctDnaCugFormat = _MscVctDnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 10),
    _MscVctDnaCugFormat_Type()
)
mscVctDnaCugFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCugFormat.setStatus("mandatory")


class _MscVctDnaCug0AsNonCugCall_Type(Integer32):
    """Custom type mscVctDnaCug0AsNonCugCall based on Integer32"""
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


_MscVctDnaCug0AsNonCugCall_Type.__name__ = "Integer32"
_MscVctDnaCug0AsNonCugCall_Object = MibTableColumn
mscVctDnaCug0AsNonCugCall = _MscVctDnaCug0AsNonCugCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 11),
    _MscVctDnaCug0AsNonCugCall_Type()
)
mscVctDnaCug0AsNonCugCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaCug0AsNonCugCall.setStatus("mandatory")


class _MscVctDnaSignalPreferentialCugToLink_Type(Integer32):
    """Custom type mscVctDnaSignalPreferentialCugToLink based on Integer32"""
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


_MscVctDnaSignalPreferentialCugToLink_Type.__name__ = "Integer32"
_MscVctDnaSignalPreferentialCugToLink_Object = MibTableColumn
mscVctDnaSignalPreferentialCugToLink = _MscVctDnaSignalPreferentialCugToLink_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 12),
    _MscVctDnaSignalPreferentialCugToLink_Type()
)
mscVctDnaSignalPreferentialCugToLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaSignalPreferentialCugToLink.setStatus("mandatory")


class _MscVctDnaSignalIntlAddressToLink_Type(Integer32):
    """Custom type mscVctDnaSignalIntlAddressToLink based on Integer32"""
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


_MscVctDnaSignalIntlAddressToLink_Type.__name__ = "Integer32"
_MscVctDnaSignalIntlAddressToLink_Object = MibTableColumn
mscVctDnaSignalIntlAddressToLink = _MscVctDnaSignalIntlAddressToLink_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 13),
    _MscVctDnaSignalIntlAddressToLink_Type()
)
mscVctDnaSignalIntlAddressToLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaSignalIntlAddressToLink.setStatus("mandatory")


class _MscVctDnaFastSelectCallsOnly_Type(Integer32):
    """Custom type mscVctDnaFastSelectCallsOnly based on Integer32"""
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


_MscVctDnaFastSelectCallsOnly_Type.__name__ = "Integer32"
_MscVctDnaFastSelectCallsOnly_Object = MibTableColumn
mscVctDnaFastSelectCallsOnly = _MscVctDnaFastSelectCallsOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 14),
    _MscVctDnaFastSelectCallsOnly_Type()
)
mscVctDnaFastSelectCallsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaFastSelectCallsOnly.setStatus("mandatory")


class _MscVctDnaPreselectRpoa_Type(Integer32):
    """Custom type mscVctDnaPreselectRpoa based on Integer32"""
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


_MscVctDnaPreselectRpoa_Type.__name__ = "Integer32"
_MscVctDnaPreselectRpoa_Object = MibTableColumn
mscVctDnaPreselectRpoa = _MscVctDnaPreselectRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 15),
    _MscVctDnaPreselectRpoa_Type()
)
mscVctDnaPreselectRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaPreselectRpoa.setStatus("mandatory")


class _MscVctDnaAccountClass_Type(Unsigned32):
    """Custom type mscVctDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctDnaAccountClass_Type.__name__ = "Unsigned32"
_MscVctDnaAccountClass_Object = MibTableColumn
mscVctDnaAccountClass = _MscVctDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 16),
    _MscVctDnaAccountClass_Type()
)
mscVctDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaAccountClass.setStatus("mandatory")


class _MscVctDnaAccountCollection_Type(OctetString):
    """Custom type mscVctDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVctDnaAccountCollection_Type.__name__ = "OctetString"
_MscVctDnaAccountCollection_Object = MibTableColumn
mscVctDnaAccountCollection = _MscVctDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 17),
    _MscVctDnaAccountCollection_Type()
)
mscVctDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaAccountCollection.setStatus("mandatory")


class _MscVctDnaServiceExchange_Type(Unsigned32):
    """Custom type mscVctDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctDnaServiceExchange_Type.__name__ = "Unsigned32"
_MscVctDnaServiceExchange_Object = MibTableColumn
mscVctDnaServiceExchange = _MscVctDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 18),
    _MscVctDnaServiceExchange_Type()
)
mscVctDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaServiceExchange.setStatus("mandatory")


class _MscVctDnaEgressAccounting_Type(Integer32):
    """Custom type mscVctDnaEgressAccounting based on Integer32"""
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


_MscVctDnaEgressAccounting_Type.__name__ = "Integer32"
_MscVctDnaEgressAccounting_Object = MibTableColumn
mscVctDnaEgressAccounting = _MscVctDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 19),
    _MscVctDnaEgressAccounting_Type()
)
mscVctDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaEgressAccounting.setStatus("mandatory")


class _MscVctDnaRpoa_Type(DigitString):
    """Custom type mscVctDnaRpoa based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscVctDnaRpoa_Type.__name__ = "DigitString"
_MscVctDnaRpoa_Object = MibTableColumn
mscVctDnaRpoa = _MscVctDnaRpoa_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 20),
    _MscVctDnaRpoa_Type()
)
mscVctDnaRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaRpoa.setStatus("mandatory")


class _MscVctDnaDataPath_Type(Integer32):
    """Custom type mscVctDnaDataPath based on Integer32"""
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


_MscVctDnaDataPath_Type.__name__ = "Integer32"
_MscVctDnaDataPath_Object = MibTableColumn
mscVctDnaDataPath = _MscVctDnaDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 2, 13, 1, 21),
    _MscVctDnaDataPath_Type()
)
mscVctDnaDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDnaDataPath.setStatus("mandatory")
_MscVctDc_ObjectIdentity = ObjectIdentity
mscVctDc = _MscVctDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3)
)
_MscVctDcRowStatusTable_Object = MibTable
mscVctDcRowStatusTable = _MscVctDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 1)
)
if mibBuilder.loadTexts:
    mscVctDcRowStatusTable.setStatus("mandatory")
_MscVctDcRowStatusEntry_Object = MibTableRow
mscVctDcRowStatusEntry = _MscVctDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 1, 1)
)
mscVctDcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcIndex"),
)
if mibBuilder.loadTexts:
    mscVctDcRowStatusEntry.setStatus("mandatory")
_MscVctDcRowStatus_Type = RowStatus
_MscVctDcRowStatus_Object = MibTableColumn
mscVctDcRowStatus = _MscVctDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 1, 1, 1),
    _MscVctDcRowStatus_Type()
)
mscVctDcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcRowStatus.setStatus("mandatory")
_MscVctDcComponentName_Type = DisplayString
_MscVctDcComponentName_Object = MibTableColumn
mscVctDcComponentName = _MscVctDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 1, 1, 2),
    _MscVctDcComponentName_Type()
)
mscVctDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDcComponentName.setStatus("mandatory")
_MscVctDcStorageType_Type = StorageType
_MscVctDcStorageType_Object = MibTableColumn
mscVctDcStorageType = _MscVctDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 1, 1, 4),
    _MscVctDcStorageType_Type()
)
mscVctDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctDcStorageType.setStatus("mandatory")


class _MscVctDcIndex_Type(Integer32):
    """Custom type mscVctDcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscVctDcIndex_Type.__name__ = "Integer32"
_MscVctDcIndex_Object = MibTableColumn
mscVctDcIndex = _MscVctDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 1, 1, 10),
    _MscVctDcIndex_Type()
)
mscVctDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDcIndex.setStatus("mandatory")
_MscVctDcOptionsTable_Object = MibTable
mscVctDcOptionsTable = _MscVctDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10)
)
if mibBuilder.loadTexts:
    mscVctDcOptionsTable.setStatus("mandatory")
_MscVctDcOptionsEntry_Object = MibTableRow
mscVctDcOptionsEntry = _MscVctDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1)
)
mscVctDcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcIndex"),
)
if mibBuilder.loadTexts:
    mscVctDcOptionsEntry.setStatus("mandatory")


class _MscVctDcLocalNpi_Type(Integer32):
    """Custom type mscVctDcLocalNpi based on Integer32"""
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


_MscVctDcLocalNpi_Type.__name__ = "Integer32"
_MscVctDcLocalNpi_Object = MibTableColumn
mscVctDcLocalNpi = _MscVctDcLocalNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 1),
    _MscVctDcLocalNpi_Type()
)
mscVctDcLocalNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcLocalNpi.setStatus("mandatory")


class _MscVctDcLocalDna_Type(DigitString):
    """Custom type mscVctDcLocalDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscVctDcLocalDna_Type.__name__ = "DigitString"
_MscVctDcLocalDna_Object = MibTableColumn
mscVctDcLocalDna = _MscVctDcLocalDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 2),
    _MscVctDcLocalDna_Type()
)
mscVctDcLocalDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcLocalDna.setStatus("mandatory")


class _MscVctDcRemoteNpi_Type(Integer32):
    """Custom type mscVctDcRemoteNpi based on Integer32"""
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


_MscVctDcRemoteNpi_Type.__name__ = "Integer32"
_MscVctDcRemoteNpi_Object = MibTableColumn
mscVctDcRemoteNpi = _MscVctDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 3),
    _MscVctDcRemoteNpi_Type()
)
mscVctDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcRemoteNpi.setStatus("mandatory")


class _MscVctDcRemoteDna_Type(DigitString):
    """Custom type mscVctDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscVctDcRemoteDna_Type.__name__ = "DigitString"
_MscVctDcRemoteDna_Object = MibTableColumn
mscVctDcRemoteDna = _MscVctDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 4),
    _MscVctDcRemoteDna_Type()
)
mscVctDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcRemoteDna.setStatus("mandatory")


class _MscVctDcRemoteLcn_Type(Unsigned32):
    """Custom type mscVctDcRemoteLcn based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVctDcRemoteLcn_Type.__name__ = "Unsigned32"
_MscVctDcRemoteLcn_Object = MibTableColumn
mscVctDcRemoteLcn = _MscVctDcRemoteLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 5),
    _MscVctDcRemoteLcn_Type()
)
mscVctDcRemoteLcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcRemoteLcn.setStatus("mandatory")


class _MscVctDcType_Type(Integer32):
    """Custom type mscVctDcType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("permanentBackupSlave", 3),
          ("permanentMaster", 1),
          ("permanentSlave", 2),
          ("permanentSlaveWithBackup", 4),
          ("spvcBackupSlave", 7),
          ("spvcMaster", 5),
          ("spvcSlave", 6),
          ("spvcSlaveWithBackup", 8),
          ("switched", 0))
    )


_MscVctDcType_Type.__name__ = "Integer32"
_MscVctDcType_Object = MibTableColumn
mscVctDcType = _MscVctDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 6),
    _MscVctDcType_Type()
)
mscVctDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcType.setStatus("mandatory")


class _MscVctDcSvcAutoCallRetry_Type(Integer32):
    """Custom type mscVctDcSvcAutoCallRetry based on Integer32"""
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


_MscVctDcSvcAutoCallRetry_Type.__name__ = "Integer32"
_MscVctDcSvcAutoCallRetry_Object = MibTableColumn
mscVctDcSvcAutoCallRetry = _MscVctDcSvcAutoCallRetry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 7),
    _MscVctDcSvcAutoCallRetry_Type()
)
mscVctDcSvcAutoCallRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcSvcAutoCallRetry.setStatus("mandatory")


class _MscVctDcUserData_Type(HexString):
    """Custom type mscVctDcUserData based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscVctDcUserData_Type.__name__ = "HexString"
_MscVctDcUserData_Object = MibTableColumn
mscVctDcUserData = _MscVctDcUserData_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 8),
    _MscVctDcUserData_Type()
)
mscVctDcUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcUserData.setStatus("mandatory")


class _MscVctDcDiscardPriority_Type(Integer32):
    """Custom type mscVctDcDiscardPriority based on Integer32"""
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


_MscVctDcDiscardPriority_Type.__name__ = "Integer32"
_MscVctDcDiscardPriority_Object = MibTableColumn
mscVctDcDiscardPriority = _MscVctDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 10),
    _MscVctDcDiscardPriority_Type()
)
mscVctDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcDiscardPriority.setStatus("mandatory")


class _MscVctDcDataPath_Type(Integer32):
    """Custom type mscVctDcDataPath based on Integer32"""
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


_MscVctDcDataPath_Type.__name__ = "Integer32"
_MscVctDcDataPath_Object = MibTableColumn
mscVctDcDataPath = _MscVctDcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 11),
    _MscVctDcDataPath_Type()
)
mscVctDcDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcDataPath.setStatus("mandatory")


class _MscVctDcCugIndex_Type(Unsigned32):
    """Custom type mscVctDcCugIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctDcCugIndex_Type.__name__ = "Unsigned32"
_MscVctDcCugIndex_Object = MibTableColumn
mscVctDcCugIndex = _MscVctDcCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 13),
    _MscVctDcCugIndex_Type()
)
mscVctDcCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcCugIndex.setStatus("mandatory")


class _MscVctDcCugType_Type(Integer32):
    """Custom type mscVctDcCugType based on Integer32"""
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


_MscVctDcCugType_Type.__name__ = "Integer32"
_MscVctDcCugType_Object = MibTableColumn
mscVctDcCugType = _MscVctDcCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 10, 1, 14),
    _MscVctDcCugType_Type()
)
mscVctDcCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcCugType.setStatus("mandatory")
_MscVctDcCfaTable_Object = MibTable
mscVctDcCfaTable = _MscVctDcCfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 267)
)
if mibBuilder.loadTexts:
    mscVctDcCfaTable.setStatus("mandatory")
_MscVctDcCfaEntry_Object = MibTableRow
mscVctDcCfaEntry = _MscVctDcCfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 267, 1)
)
mscVctDcCfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcCfaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDcCfaEntry.setStatus("mandatory")


class _MscVctDcCfaIndex_Type(Integer32):
    """Custom type mscVctDcCfaIndex based on Integer32"""
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


_MscVctDcCfaIndex_Type.__name__ = "Integer32"
_MscVctDcCfaIndex_Object = MibTableColumn
mscVctDcCfaIndex = _MscVctDcCfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 267, 1, 1),
    _MscVctDcCfaIndex_Type()
)
mscVctDcCfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDcCfaIndex.setStatus("mandatory")


class _MscVctDcCfaValue_Type(HexString):
    """Custom type mscVctDcCfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscVctDcCfaValue_Type.__name__ = "HexString"
_MscVctDcCfaValue_Object = MibTableColumn
mscVctDcCfaValue = _MscVctDcCfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 267, 1, 2),
    _MscVctDcCfaValue_Type()
)
mscVctDcCfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcCfaValue.setStatus("mandatory")
_MscVctDcCfaRowStatus_Type = RowStatus
_MscVctDcCfaRowStatus_Object = MibTableColumn
mscVctDcCfaRowStatus = _MscVctDcCfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 267, 1, 3),
    _MscVctDcCfaRowStatus_Type()
)
mscVctDcCfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVctDcCfaRowStatus.setStatus("mandatory")
_MscVctDcDfaTable_Object = MibTable
mscVctDcDfaTable = _MscVctDcDfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 268)
)
if mibBuilder.loadTexts:
    mscVctDcDfaTable.setStatus("mandatory")
_MscVctDcDfaEntry_Object = MibTableRow
mscVctDcDfaEntry = _MscVctDcDfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 268, 1)
)
mscVctDcDfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcDfaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDcDfaEntry.setStatus("mandatory")


class _MscVctDcDfaIndex_Type(Integer32):
    """Custom type mscVctDcDfaIndex based on Integer32"""
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


_MscVctDcDfaIndex_Type.__name__ = "Integer32"
_MscVctDcDfaIndex_Object = MibTableColumn
mscVctDcDfaIndex = _MscVctDcDfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 268, 1, 1),
    _MscVctDcDfaIndex_Type()
)
mscVctDcDfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDcDfaIndex.setStatus("mandatory")


class _MscVctDcDfaValue_Type(HexString):
    """Custom type mscVctDcDfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscVctDcDfaValue_Type.__name__ = "HexString"
_MscVctDcDfaValue_Object = MibTableColumn
mscVctDcDfaValue = _MscVctDcDfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 268, 1, 2),
    _MscVctDcDfaValue_Type()
)
mscVctDcDfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcDfaValue.setStatus("mandatory")
_MscVctDcDfaRowStatus_Type = RowStatus
_MscVctDcDfaRowStatus_Object = MibTableColumn
mscVctDcDfaRowStatus = _MscVctDcDfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 268, 1, 3),
    _MscVctDcDfaRowStatus_Type()
)
mscVctDcDfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVctDcDfaRowStatus.setStatus("mandatory")
_MscVctDcNfaTable_Object = MibTable
mscVctDcNfaTable = _MscVctDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 269)
)
if mibBuilder.loadTexts:
    mscVctDcNfaTable.setStatus("obsolete")
_MscVctDcNfaEntry_Object = MibTableRow
mscVctDcNfaEntry = _MscVctDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 269, 1)
)
mscVctDcNfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcNfaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDcNfaEntry.setStatus("obsolete")


class _MscVctDcNfaIndex_Type(Integer32):
    """Custom type mscVctDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(127, 127),
        ValueRangeConstraint(212, 212),
    )


_MscVctDcNfaIndex_Type.__name__ = "Integer32"
_MscVctDcNfaIndex_Object = MibTableColumn
mscVctDcNfaIndex = _MscVctDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 269, 1, 1),
    _MscVctDcNfaIndex_Type()
)
mscVctDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDcNfaIndex.setStatus("obsolete")


class _MscVctDcNfaValue_Type(HexString):
    """Custom type mscVctDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscVctDcNfaValue_Type.__name__ = "HexString"
_MscVctDcNfaValue_Object = MibTableColumn
mscVctDcNfaValue = _MscVctDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 269, 1, 2),
    _MscVctDcNfaValue_Type()
)
mscVctDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcNfaValue.setStatus("obsolete")
_MscVctDcNfaRowStatus_Type = RowStatus
_MscVctDcNfaRowStatus_Object = MibTableColumn
mscVctDcNfaRowStatus = _MscVctDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 269, 1, 3),
    _MscVctDcNfaRowStatus_Type()
)
mscVctDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVctDcNfaRowStatus.setStatus("obsolete")
_MscVctDcIfaTable_Object = MibTable
mscVctDcIfaTable = _MscVctDcIfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 270)
)
if mibBuilder.loadTexts:
    mscVctDcIfaTable.setStatus("mandatory")
_MscVctDcIfaEntry_Object = MibTableRow
mscVctDcIfaEntry = _MscVctDcIfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 270, 1)
)
mscVctDcIfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctDcIfaIndex"),
)
if mibBuilder.loadTexts:
    mscVctDcIfaEntry.setStatus("mandatory")


class _MscVctDcIfaIndex_Type(Integer32):
    """Custom type mscVctDcIfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscVctDcIfaIndex_Type.__name__ = "Integer32"
_MscVctDcIfaIndex_Object = MibTableColumn
mscVctDcIfaIndex = _MscVctDcIfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 270, 1, 1),
    _MscVctDcIfaIndex_Type()
)
mscVctDcIfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctDcIfaIndex.setStatus("mandatory")


class _MscVctDcIfaValue_Type(HexString):
    """Custom type mscVctDcIfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscVctDcIfaValue_Type.__name__ = "HexString"
_MscVctDcIfaValue_Object = MibTableColumn
mscVctDcIfaValue = _MscVctDcIfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 270, 1, 2),
    _MscVctDcIfaValue_Type()
)
mscVctDcIfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctDcIfaValue.setStatus("mandatory")
_MscVctDcIfaRowStatus_Type = RowStatus
_MscVctDcIfaRowStatus_Object = MibTableColumn
mscVctDcIfaRowStatus = _MscVctDcIfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 3, 270, 1, 3),
    _MscVctDcIfaRowStatus_Type()
)
mscVctDcIfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscVctDcIfaRowStatus.setStatus("mandatory")
_MscVctVc_ObjectIdentity = ObjectIdentity
mscVctVc = _MscVctVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4)
)
_MscVctVcRowStatusTable_Object = MibTable
mscVctVcRowStatusTable = _MscVctVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 1)
)
if mibBuilder.loadTexts:
    mscVctVcRowStatusTable.setStatus("mandatory")
_MscVctVcRowStatusEntry_Object = MibTableRow
mscVctVcRowStatusEntry = _MscVctVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 1, 1)
)
mscVctVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcRowStatusEntry.setStatus("mandatory")
_MscVctVcRowStatus_Type = RowStatus
_MscVctVcRowStatus_Object = MibTableColumn
mscVctVcRowStatus = _MscVctVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 1, 1, 1),
    _MscVctVcRowStatus_Type()
)
mscVctVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcRowStatus.setStatus("mandatory")
_MscVctVcComponentName_Type = DisplayString
_MscVctVcComponentName_Object = MibTableColumn
mscVctVcComponentName = _MscVctVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 1, 1, 2),
    _MscVctVcComponentName_Type()
)
mscVctVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcComponentName.setStatus("mandatory")
_MscVctVcStorageType_Type = StorageType
_MscVctVcStorageType_Object = MibTableColumn
mscVctVcStorageType = _MscVctVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 1, 1, 4),
    _MscVctVcStorageType_Type()
)
mscVctVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcStorageType.setStatus("mandatory")
_MscVctVcIndex_Type = NonReplicated
_MscVctVcIndex_Object = MibTableColumn
mscVctVcIndex = _MscVctVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 1, 1, 10),
    _MscVctVcIndex_Type()
)
mscVctVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctVcIndex.setStatus("mandatory")
_MscVctVcCadTable_Object = MibTable
mscVctVcCadTable = _MscVctVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10)
)
if mibBuilder.loadTexts:
    mscVctVcCadTable.setStatus("mandatory")
_MscVctVcCadEntry_Object = MibTableRow
mscVctVcCadEntry = _MscVctVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1)
)
mscVctVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcCadEntry.setStatus("mandatory")


class _MscVctVcType_Type(Integer32):
    """Custom type mscVctVcType based on Integer32"""
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


_MscVctVcType_Type.__name__ = "Integer32"
_MscVctVcType_Object = MibTableColumn
mscVctVcType = _MscVctVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 1),
    _MscVctVcType_Type()
)
mscVctVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcType.setStatus("mandatory")


class _MscVctVcState_Type(Integer32):
    """Custom type mscVctVcState based on Integer32"""
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


_MscVctVcState_Type.__name__ = "Integer32"
_MscVctVcState_Object = MibTableColumn
mscVctVcState = _MscVctVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 2),
    _MscVctVcState_Type()
)
mscVctVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcState.setStatus("mandatory")


class _MscVctVcPreviousState_Type(Integer32):
    """Custom type mscVctVcPreviousState based on Integer32"""
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


_MscVctVcPreviousState_Type.__name__ = "Integer32"
_MscVctVcPreviousState_Object = MibTableColumn
mscVctVcPreviousState = _MscVctVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 3),
    _MscVctVcPreviousState_Type()
)
mscVctVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPreviousState.setStatus("mandatory")


class _MscVctVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscVctVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscVctVcDiagnosticCode_Object = MibTableColumn
mscVctVcDiagnosticCode = _MscVctVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 4),
    _MscVctVcDiagnosticCode_Type()
)
mscVctVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcDiagnosticCode.setStatus("mandatory")


class _MscVctVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscVctVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscVctVcPreviousDiagnosticCode_Object = MibTableColumn
mscVctVcPreviousDiagnosticCode = _MscVctVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 5),
    _MscVctVcPreviousDiagnosticCode_Type()
)
mscVctVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscVctVcCalledNpi_Type(Integer32):
    """Custom type mscVctVcCalledNpi based on Integer32"""
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


_MscVctVcCalledNpi_Type.__name__ = "Integer32"
_MscVctVcCalledNpi_Object = MibTableColumn
mscVctVcCalledNpi = _MscVctVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 6),
    _MscVctVcCalledNpi_Type()
)
mscVctVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCalledNpi.setStatus("mandatory")


class _MscVctVcCalledDna_Type(DigitString):
    """Custom type mscVctVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscVctVcCalledDna_Type.__name__ = "DigitString"
_MscVctVcCalledDna_Object = MibTableColumn
mscVctVcCalledDna = _MscVctVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 7),
    _MscVctVcCalledDna_Type()
)
mscVctVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCalledDna.setStatus("mandatory")


class _MscVctVcCalledLcn_Type(Unsigned32):
    """Custom type mscVctVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVctVcCalledLcn_Type.__name__ = "Unsigned32"
_MscVctVcCalledLcn_Object = MibTableColumn
mscVctVcCalledLcn = _MscVctVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 8),
    _MscVctVcCalledLcn_Type()
)
mscVctVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCalledLcn.setStatus("mandatory")


class _MscVctVcCallingNpi_Type(Integer32):
    """Custom type mscVctVcCallingNpi based on Integer32"""
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


_MscVctVcCallingNpi_Type.__name__ = "Integer32"
_MscVctVcCallingNpi_Object = MibTableColumn
mscVctVcCallingNpi = _MscVctVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 9),
    _MscVctVcCallingNpi_Type()
)
mscVctVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCallingNpi.setStatus("mandatory")


class _MscVctVcCallingDna_Type(DigitString):
    """Custom type mscVctVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscVctVcCallingDna_Type.__name__ = "DigitString"
_MscVctVcCallingDna_Object = MibTableColumn
mscVctVcCallingDna = _MscVctVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 10),
    _MscVctVcCallingDna_Type()
)
mscVctVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCallingDna.setStatus("mandatory")


class _MscVctVcCallingLcn_Type(Unsigned32):
    """Custom type mscVctVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVctVcCallingLcn_Type.__name__ = "Unsigned32"
_MscVctVcCallingLcn_Object = MibTableColumn
mscVctVcCallingLcn = _MscVctVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 11),
    _MscVctVcCallingLcn_Type()
)
mscVctVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCallingLcn.setStatus("mandatory")


class _MscVctVcAccountingEnabled_Type(Integer32):
    """Custom type mscVctVcAccountingEnabled based on Integer32"""
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


_MscVctVcAccountingEnabled_Type.__name__ = "Integer32"
_MscVctVcAccountingEnabled_Object = MibTableColumn
mscVctVcAccountingEnabled = _MscVctVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 12),
    _MscVctVcAccountingEnabled_Type()
)
mscVctVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcAccountingEnabled.setStatus("mandatory")


class _MscVctVcFastSelectCall_Type(Integer32):
    """Custom type mscVctVcFastSelectCall based on Integer32"""
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


_MscVctVcFastSelectCall_Type.__name__ = "Integer32"
_MscVctVcFastSelectCall_Object = MibTableColumn
mscVctVcFastSelectCall = _MscVctVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 13),
    _MscVctVcFastSelectCall_Type()
)
mscVctVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcFastSelectCall.setStatus("mandatory")


class _MscVctVcLocalRxPktSize_Type(Integer32):
    """Custom type mscVctVcLocalRxPktSize based on Integer32"""
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


_MscVctVcLocalRxPktSize_Type.__name__ = "Integer32"
_MscVctVcLocalRxPktSize_Object = MibTableColumn
mscVctVcLocalRxPktSize = _MscVctVcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 14),
    _MscVctVcLocalRxPktSize_Type()
)
mscVctVcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcLocalRxPktSize.setStatus("mandatory")


class _MscVctVcLocalTxPktSize_Type(Integer32):
    """Custom type mscVctVcLocalTxPktSize based on Integer32"""
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


_MscVctVcLocalTxPktSize_Type.__name__ = "Integer32"
_MscVctVcLocalTxPktSize_Object = MibTableColumn
mscVctVcLocalTxPktSize = _MscVctVcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 15),
    _MscVctVcLocalTxPktSize_Type()
)
mscVctVcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcLocalTxPktSize.setStatus("mandatory")


class _MscVctVcLocalTxWindowSize_Type(Unsigned32):
    """Custom type mscVctVcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscVctVcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_MscVctVcLocalTxWindowSize_Object = MibTableColumn
mscVctVcLocalTxWindowSize = _MscVctVcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 16),
    _MscVctVcLocalTxWindowSize_Type()
)
mscVctVcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcLocalTxWindowSize.setStatus("mandatory")


class _MscVctVcLocalRxWindowSize_Type(Unsigned32):
    """Custom type mscVctVcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscVctVcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_MscVctVcLocalRxWindowSize_Object = MibTableColumn
mscVctVcLocalRxWindowSize = _MscVctVcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 17),
    _MscVctVcLocalRxWindowSize_Type()
)
mscVctVcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcLocalRxWindowSize.setStatus("mandatory")


class _MscVctVcPathReliability_Type(Integer32):
    """Custom type mscVctVcPathReliability based on Integer32"""
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


_MscVctVcPathReliability_Type.__name__ = "Integer32"
_MscVctVcPathReliability_Object = MibTableColumn
mscVctVcPathReliability = _MscVctVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 19),
    _MscVctVcPathReliability_Type()
)
mscVctVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPathReliability.setStatus("mandatory")


class _MscVctVcAccountingEnd_Type(Integer32):
    """Custom type mscVctVcAccountingEnd based on Integer32"""
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


_MscVctVcAccountingEnd_Type.__name__ = "Integer32"
_MscVctVcAccountingEnd_Object = MibTableColumn
mscVctVcAccountingEnd = _MscVctVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 20),
    _MscVctVcAccountingEnd_Type()
)
mscVctVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcAccountingEnd.setStatus("mandatory")


class _MscVctVcPriority_Type(Integer32):
    """Custom type mscVctVcPriority based on Integer32"""
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


_MscVctVcPriority_Type.__name__ = "Integer32"
_MscVctVcPriority_Object = MibTableColumn
mscVctVcPriority = _MscVctVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 21),
    _MscVctVcPriority_Type()
)
mscVctVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPriority.setStatus("mandatory")


class _MscVctVcSegmentSize_Type(Unsigned32):
    """Custom type mscVctVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctVcSegmentSize_Type.__name__ = "Unsigned32"
_MscVctVcSegmentSize_Object = MibTableColumn
mscVctVcSegmentSize = _MscVctVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 22),
    _MscVctVcSegmentSize_Type()
)
mscVctVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSegmentSize.setStatus("mandatory")


class _MscVctVcSubnetTxPktSize_Type(Integer32):
    """Custom type mscVctVcSubnetTxPktSize based on Integer32"""
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


_MscVctVcSubnetTxPktSize_Type.__name__ = "Integer32"
_MscVctVcSubnetTxPktSize_Object = MibTableColumn
mscVctVcSubnetTxPktSize = _MscVctVcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 23),
    _MscVctVcSubnetTxPktSize_Type()
)
mscVctVcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSubnetTxPktSize.setStatus("mandatory")


class _MscVctVcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type mscVctVcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctVcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_MscVctVcSubnetTxWindowSize_Object = MibTableColumn
mscVctVcSubnetTxWindowSize = _MscVctVcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 24),
    _MscVctVcSubnetTxWindowSize_Type()
)
mscVctVcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSubnetTxWindowSize.setStatus("mandatory")


class _MscVctVcSubnetRxPktSize_Type(Integer32):
    """Custom type mscVctVcSubnetRxPktSize based on Integer32"""
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


_MscVctVcSubnetRxPktSize_Type.__name__ = "Integer32"
_MscVctVcSubnetRxPktSize_Object = MibTableColumn
mscVctVcSubnetRxPktSize = _MscVctVcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 25),
    _MscVctVcSubnetRxPktSize_Type()
)
mscVctVcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSubnetRxPktSize.setStatus("mandatory")


class _MscVctVcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type mscVctVcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctVcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_MscVctVcSubnetRxWindowSize_Object = MibTableColumn
mscVctVcSubnetRxWindowSize = _MscVctVcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 26),
    _MscVctVcSubnetRxWindowSize_Type()
)
mscVctVcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSubnetRxWindowSize.setStatus("mandatory")


class _MscVctVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscVctVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscVctVcMaxSubnetPktSize_Object = MibTableColumn
mscVctVcMaxSubnetPktSize = _MscVctVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 27),
    _MscVctVcMaxSubnetPktSize_Type()
)
mscVctVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcMaxSubnetPktSize.setStatus("mandatory")


class _MscVctVcTransferPriorityToNetwork_Type(Integer32):
    """Custom type mscVctVcTransferPriorityToNetwork based on Integer32"""
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


_MscVctVcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MscVctVcTransferPriorityToNetwork_Object = MibTableColumn
mscVctVcTransferPriorityToNetwork = _MscVctVcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 28),
    _MscVctVcTransferPriorityToNetwork_Type()
)
mscVctVcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcTransferPriorityToNetwork.setStatus("mandatory")


class _MscVctVcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mscVctVcTransferPriorityFromNetwork based on Integer32"""
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


_MscVctVcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MscVctVcTransferPriorityFromNetwork_Object = MibTableColumn
mscVctVcTransferPriorityFromNetwork = _MscVctVcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 10, 1, 29),
    _MscVctVcTransferPriorityFromNetwork_Type()
)
mscVctVcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcTransferPriorityFromNetwork.setStatus("mandatory")
_MscVctVcIntdTable_Object = MibTable
mscVctVcIntdTable = _MscVctVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11)
)
if mibBuilder.loadTexts:
    mscVctVcIntdTable.setStatus("mandatory")
_MscVctVcIntdEntry_Object = MibTableRow
mscVctVcIntdEntry = _MscVctVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11, 1)
)
mscVctVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcIntdEntry.setStatus("mandatory")


class _MscVctVcCallReferenceNumber_Type(Hex):
    """Custom type mscVctVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcCallReferenceNumber_Type.__name__ = "Hex"
_MscVctVcCallReferenceNumber_Object = MibTableColumn
mscVctVcCallReferenceNumber = _MscVctVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11, 1, 1),
    _MscVctVcCallReferenceNumber_Type()
)
mscVctVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCallReferenceNumber.setStatus("obsolete")


class _MscVctVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscVctVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscVctVcElapsedTimeTillNow_Object = MibTableColumn
mscVctVcElapsedTimeTillNow = _MscVctVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11, 1, 2),
    _MscVctVcElapsedTimeTillNow_Type()
)
mscVctVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcElapsedTimeTillNow.setStatus("mandatory")


class _MscVctVcSegmentsRx_Type(Unsigned32):
    """Custom type mscVctVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscVctVcSegmentsRx_Object = MibTableColumn
mscVctVcSegmentsRx = _MscVctVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11, 1, 3),
    _MscVctVcSegmentsRx_Type()
)
mscVctVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSegmentsRx.setStatus("mandatory")


class _MscVctVcSegmentsSent_Type(Unsigned32):
    """Custom type mscVctVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscVctVcSegmentsSent_Object = MibTableColumn
mscVctVcSegmentsSent = _MscVctVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11, 1, 4),
    _MscVctVcSegmentsSent_Type()
)
mscVctVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSegmentsSent.setStatus("mandatory")


class _MscVctVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscVctVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscVctVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscVctVcStartTime_Object = MibTableColumn
mscVctVcStartTime = _MscVctVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11, 1, 5),
    _MscVctVcStartTime_Type()
)
mscVctVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcStartTime.setStatus("mandatory")


class _MscVctVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscVctVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVctVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscVctVcCallReferenceNumberDecimal_Object = MibTableColumn
mscVctVcCallReferenceNumberDecimal = _MscVctVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 11, 1, 7),
    _MscVctVcCallReferenceNumberDecimal_Type()
)
mscVctVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscVctVcStatsTable_Object = MibTable
mscVctVcStatsTable = _MscVctVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12)
)
if mibBuilder.loadTexts:
    mscVctVcStatsTable.setStatus("mandatory")
_MscVctVcStatsEntry_Object = MibTableRow
mscVctVcStatsEntry = _MscVctVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1)
)
mscVctVcStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcStatsEntry.setStatus("mandatory")


class _MscVctVcAckStackingTimeouts_Type(Unsigned32):
    """Custom type mscVctVcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_MscVctVcAckStackingTimeouts_Object = MibTableColumn
mscVctVcAckStackingTimeouts = _MscVctVcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 1),
    _MscVctVcAckStackingTimeouts_Type()
)
mscVctVcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcAckStackingTimeouts.setStatus("mandatory")


class _MscVctVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscVctVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscVctVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscVctVcOutOfRangeFrmFromSubnet = _MscVctVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 2),
    _MscVctVcOutOfRangeFrmFromSubnet_Type()
)
mscVctVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscVctVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscVctVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscVctVcDuplicatesFromSubnet_Object = MibTableColumn
mscVctVcDuplicatesFromSubnet = _MscVctVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 3),
    _MscVctVcDuplicatesFromSubnet_Type()
)
mscVctVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscVctVcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type mscVctVcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_MscVctVcFrmRetryTimeouts_Object = MibTableColumn
mscVctVcFrmRetryTimeouts = _MscVctVcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 4),
    _MscVctVcFrmRetryTimeouts_Type()
)
mscVctVcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcFrmRetryTimeouts.setStatus("mandatory")


class _MscVctVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscVctVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscVctVcPeakRetryQueueSize_Object = MibTableColumn
mscVctVcPeakRetryQueueSize = _MscVctVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 5),
    _MscVctVcPeakRetryQueueSize_Type()
)
mscVctVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPeakRetryQueueSize.setStatus("mandatory")


class _MscVctVcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type mscVctVcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_MscVctVcPeakOoSeqQueueSize_Object = MibTableColumn
mscVctVcPeakOoSeqQueueSize = _MscVctVcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 6),
    _MscVctVcPeakOoSeqQueueSize_Type()
)
mscVctVcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPeakOoSeqQueueSize.setStatus("mandatory")


class _MscVctVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscVctVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscVctVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscVctVcPeakOoSeqFrmForwarded = _MscVctVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 7),
    _MscVctVcPeakOoSeqFrmForwarded_Type()
)
mscVctVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscVctVcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type mscVctVcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_MscVctVcPeakStackedAcksRx_Object = MibTableColumn
mscVctVcPeakStackedAcksRx = _MscVctVcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 8),
    _MscVctVcPeakStackedAcksRx_Type()
)
mscVctVcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcPeakStackedAcksRx.setStatus("mandatory")


class _MscVctVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscVctVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscVctVcSubnetRecoveries_Object = MibTableColumn
mscVctVcSubnetRecoveries = _MscVctVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 9),
    _MscVctVcSubnetRecoveries_Type()
)
mscVctVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcSubnetRecoveries.setStatus("mandatory")


class _MscVctVcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type mscVctVcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_MscVctVcWindowClosuresToSubnet_Object = MibTableColumn
mscVctVcWindowClosuresToSubnet = _MscVctVcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 10),
    _MscVctVcWindowClosuresToSubnet_Type()
)
mscVctVcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcWindowClosuresToSubnet.setStatus("mandatory")


class _MscVctVcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type mscVctVcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_MscVctVcWindowClosuresFromSubnet_Object = MibTableColumn
mscVctVcWindowClosuresFromSubnet = _MscVctVcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 11),
    _MscVctVcWindowClosuresFromSubnet_Type()
)
mscVctVcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcWindowClosuresFromSubnet.setStatus("mandatory")


class _MscVctVcWrTriggers_Type(Unsigned32):
    """Custom type mscVctVcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcWrTriggers_Type.__name__ = "Unsigned32"
_MscVctVcWrTriggers_Object = MibTableColumn
mscVctVcWrTriggers = _MscVctVcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 4, 12, 1, 12),
    _MscVctVcWrTriggers_Type()
)
mscVctVcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcWrTriggers.setStatus("mandatory")
_MscVctVcfr_ObjectIdentity = ObjectIdentity
mscVctVcfr = _MscVctVcfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5)
)
_MscVctVcfrRowStatusTable_Object = MibTable
mscVctVcfrRowStatusTable = _MscVctVcfrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 1)
)
if mibBuilder.loadTexts:
    mscVctVcfrRowStatusTable.setStatus("mandatory")
_MscVctVcfrRowStatusEntry_Object = MibTableRow
mscVctVcfrRowStatusEntry = _MscVctVcfrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 1, 1)
)
mscVctVcfrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcfrIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcfrRowStatusEntry.setStatus("mandatory")
_MscVctVcfrRowStatus_Type = RowStatus
_MscVctVcfrRowStatus_Object = MibTableColumn
mscVctVcfrRowStatus = _MscVctVcfrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 1, 1, 1),
    _MscVctVcfrRowStatus_Type()
)
mscVctVcfrRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrRowStatus.setStatus("mandatory")
_MscVctVcfrComponentName_Type = DisplayString
_MscVctVcfrComponentName_Object = MibTableColumn
mscVctVcfrComponentName = _MscVctVcfrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 1, 1, 2),
    _MscVctVcfrComponentName_Type()
)
mscVctVcfrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrComponentName.setStatus("mandatory")
_MscVctVcfrStorageType_Type = StorageType
_MscVctVcfrStorageType_Object = MibTableColumn
mscVctVcfrStorageType = _MscVctVcfrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 1, 1, 4),
    _MscVctVcfrStorageType_Type()
)
mscVctVcfrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrStorageType.setStatus("mandatory")
_MscVctVcfrIndex_Type = NonReplicated
_MscVctVcfrIndex_Object = MibTableColumn
mscVctVcfrIndex = _MscVctVcfrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 1, 1, 10),
    _MscVctVcfrIndex_Type()
)
mscVctVcfrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVctVcfrIndex.setStatus("mandatory")
_MscVctVcfrCadTable_Object = MibTable
mscVctVcfrCadTable = _MscVctVcfrCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10)
)
if mibBuilder.loadTexts:
    mscVctVcfrCadTable.setStatus("mandatory")
_MscVctVcfrCadEntry_Object = MibTableRow
mscVctVcfrCadEntry = _MscVctVcfrCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1)
)
mscVctVcfrCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcfrIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcfrCadEntry.setStatus("mandatory")


class _MscVctVcfrType_Type(Integer32):
    """Custom type mscVctVcfrType based on Integer32"""
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
        *(("frf10spvc", 3),
          ("pvc", 1),
          ("spvc", 2),
          ("svc", 0))
    )


_MscVctVcfrType_Type.__name__ = "Integer32"
_MscVctVcfrType_Object = MibTableColumn
mscVctVcfrType = _MscVctVcfrType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 1),
    _MscVctVcfrType_Type()
)
mscVctVcfrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrType.setStatus("mandatory")


class _MscVctVcfrState_Type(Integer32):
    """Custom type mscVctVcfrState based on Integer32"""
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


_MscVctVcfrState_Type.__name__ = "Integer32"
_MscVctVcfrState_Object = MibTableColumn
mscVctVcfrState = _MscVctVcfrState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 2),
    _MscVctVcfrState_Type()
)
mscVctVcfrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrState.setStatus("mandatory")


class _MscVctVcfrPreviousState_Type(Integer32):
    """Custom type mscVctVcfrPreviousState based on Integer32"""
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


_MscVctVcfrPreviousState_Type.__name__ = "Integer32"
_MscVctVcfrPreviousState_Object = MibTableColumn
mscVctVcfrPreviousState = _MscVctVcfrPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 3),
    _MscVctVcfrPreviousState_Type()
)
mscVctVcfrPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPreviousState.setStatus("mandatory")


class _MscVctVcfrDiagnosticCode_Type(Unsigned32):
    """Custom type mscVctVcfrDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctVcfrDiagnosticCode_Type.__name__ = "Unsigned32"
_MscVctVcfrDiagnosticCode_Object = MibTableColumn
mscVctVcfrDiagnosticCode = _MscVctVcfrDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 4),
    _MscVctVcfrDiagnosticCode_Type()
)
mscVctVcfrDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrDiagnosticCode.setStatus("mandatory")


class _MscVctVcfrPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscVctVcfrPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctVcfrPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscVctVcfrPreviousDiagnosticCode_Object = MibTableColumn
mscVctVcfrPreviousDiagnosticCode = _MscVctVcfrPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 5),
    _MscVctVcfrPreviousDiagnosticCode_Type()
)
mscVctVcfrPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPreviousDiagnosticCode.setStatus("mandatory")


class _MscVctVcfrCalledNpi_Type(Integer32):
    """Custom type mscVctVcfrCalledNpi based on Integer32"""
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


_MscVctVcfrCalledNpi_Type.__name__ = "Integer32"
_MscVctVcfrCalledNpi_Object = MibTableColumn
mscVctVcfrCalledNpi = _MscVctVcfrCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 6),
    _MscVctVcfrCalledNpi_Type()
)
mscVctVcfrCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCalledNpi.setStatus("mandatory")


class _MscVctVcfrCalledDna_Type(DigitString):
    """Custom type mscVctVcfrCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscVctVcfrCalledDna_Type.__name__ = "DigitString"
_MscVctVcfrCalledDna_Object = MibTableColumn
mscVctVcfrCalledDna = _MscVctVcfrCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 7),
    _MscVctVcfrCalledDna_Type()
)
mscVctVcfrCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCalledDna.setStatus("mandatory")


class _MscVctVcfrCalledLcn_Type(Unsigned32):
    """Custom type mscVctVcfrCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVctVcfrCalledLcn_Type.__name__ = "Unsigned32"
_MscVctVcfrCalledLcn_Object = MibTableColumn
mscVctVcfrCalledLcn = _MscVctVcfrCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 8),
    _MscVctVcfrCalledLcn_Type()
)
mscVctVcfrCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCalledLcn.setStatus("mandatory")


class _MscVctVcfrCallingNpi_Type(Integer32):
    """Custom type mscVctVcfrCallingNpi based on Integer32"""
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


_MscVctVcfrCallingNpi_Type.__name__ = "Integer32"
_MscVctVcfrCallingNpi_Object = MibTableColumn
mscVctVcfrCallingNpi = _MscVctVcfrCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 9),
    _MscVctVcfrCallingNpi_Type()
)
mscVctVcfrCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCallingNpi.setStatus("mandatory")


class _MscVctVcfrCallingDna_Type(DigitString):
    """Custom type mscVctVcfrCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscVctVcfrCallingDna_Type.__name__ = "DigitString"
_MscVctVcfrCallingDna_Object = MibTableColumn
mscVctVcfrCallingDna = _MscVctVcfrCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 10),
    _MscVctVcfrCallingDna_Type()
)
mscVctVcfrCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCallingDna.setStatus("mandatory")


class _MscVctVcfrCallingLcn_Type(Unsigned32):
    """Custom type mscVctVcfrCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVctVcfrCallingLcn_Type.__name__ = "Unsigned32"
_MscVctVcfrCallingLcn_Object = MibTableColumn
mscVctVcfrCallingLcn = _MscVctVcfrCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 11),
    _MscVctVcfrCallingLcn_Type()
)
mscVctVcfrCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCallingLcn.setStatus("mandatory")


class _MscVctVcfrAccountingEnabled_Type(Integer32):
    """Custom type mscVctVcfrAccountingEnabled based on Integer32"""
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


_MscVctVcfrAccountingEnabled_Type.__name__ = "Integer32"
_MscVctVcfrAccountingEnabled_Object = MibTableColumn
mscVctVcfrAccountingEnabled = _MscVctVcfrAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 12),
    _MscVctVcfrAccountingEnabled_Type()
)
mscVctVcfrAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrAccountingEnabled.setStatus("mandatory")


class _MscVctVcfrFastSelectCall_Type(Integer32):
    """Custom type mscVctVcfrFastSelectCall based on Integer32"""
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


_MscVctVcfrFastSelectCall_Type.__name__ = "Integer32"
_MscVctVcfrFastSelectCall_Object = MibTableColumn
mscVctVcfrFastSelectCall = _MscVctVcfrFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 13),
    _MscVctVcfrFastSelectCall_Type()
)
mscVctVcfrFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrFastSelectCall.setStatus("mandatory")


class _MscVctVcfrPathReliability_Type(Integer32):
    """Custom type mscVctVcfrPathReliability based on Integer32"""
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


_MscVctVcfrPathReliability_Type.__name__ = "Integer32"
_MscVctVcfrPathReliability_Object = MibTableColumn
mscVctVcfrPathReliability = _MscVctVcfrPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 19),
    _MscVctVcfrPathReliability_Type()
)
mscVctVcfrPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPathReliability.setStatus("mandatory")


class _MscVctVcfrAccountingEnd_Type(Integer32):
    """Custom type mscVctVcfrAccountingEnd based on Integer32"""
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


_MscVctVcfrAccountingEnd_Type.__name__ = "Integer32"
_MscVctVcfrAccountingEnd_Object = MibTableColumn
mscVctVcfrAccountingEnd = _MscVctVcfrAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 20),
    _MscVctVcfrAccountingEnd_Type()
)
mscVctVcfrAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrAccountingEnd.setStatus("mandatory")


class _MscVctVcfrPriority_Type(Integer32):
    """Custom type mscVctVcfrPriority based on Integer32"""
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


_MscVctVcfrPriority_Type.__name__ = "Integer32"
_MscVctVcfrPriority_Object = MibTableColumn
mscVctVcfrPriority = _MscVctVcfrPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 21),
    _MscVctVcfrPriority_Type()
)
mscVctVcfrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPriority.setStatus("mandatory")


class _MscVctVcfrSegmentSize_Type(Unsigned32):
    """Custom type mscVctVcfrSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctVcfrSegmentSize_Type.__name__ = "Unsigned32"
_MscVctVcfrSegmentSize_Object = MibTableColumn
mscVctVcfrSegmentSize = _MscVctVcfrSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 22),
    _MscVctVcfrSegmentSize_Type()
)
mscVctVcfrSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrSegmentSize.setStatus("mandatory")


class _MscVctVcfrMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscVctVcfrMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscVctVcfrMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscVctVcfrMaxSubnetPktSize_Object = MibTableColumn
mscVctVcfrMaxSubnetPktSize = _MscVctVcfrMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 27),
    _MscVctVcfrMaxSubnetPktSize_Type()
)
mscVctVcfrMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrMaxSubnetPktSize.setStatus("mandatory")


class _MscVctVcfrRcosToNetwork_Type(Integer32):
    """Custom type mscVctVcfrRcosToNetwork based on Integer32"""
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


_MscVctVcfrRcosToNetwork_Type.__name__ = "Integer32"
_MscVctVcfrRcosToNetwork_Object = MibTableColumn
mscVctVcfrRcosToNetwork = _MscVctVcfrRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 28),
    _MscVctVcfrRcosToNetwork_Type()
)
mscVctVcfrRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrRcosToNetwork.setStatus("mandatory")


class _MscVctVcfrRcosFromNetwork_Type(Integer32):
    """Custom type mscVctVcfrRcosFromNetwork based on Integer32"""
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


_MscVctVcfrRcosFromNetwork_Type.__name__ = "Integer32"
_MscVctVcfrRcosFromNetwork_Object = MibTableColumn
mscVctVcfrRcosFromNetwork = _MscVctVcfrRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 29),
    _MscVctVcfrRcosFromNetwork_Type()
)
mscVctVcfrRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrRcosFromNetwork.setStatus("mandatory")


class _MscVctVcfrEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscVctVcfrEmissionPriorityToNetwork based on Integer32"""
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


_MscVctVcfrEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscVctVcfrEmissionPriorityToNetwork_Object = MibTableColumn
mscVctVcfrEmissionPriorityToNetwork = _MscVctVcfrEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 30),
    _MscVctVcfrEmissionPriorityToNetwork_Type()
)
mscVctVcfrEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrEmissionPriorityToNetwork.setStatus("mandatory")


class _MscVctVcfrEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscVctVcfrEmissionPriorityFromNetwork based on Integer32"""
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


_MscVctVcfrEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscVctVcfrEmissionPriorityFromNetwork_Object = MibTableColumn
mscVctVcfrEmissionPriorityFromNetwork = _MscVctVcfrEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 31),
    _MscVctVcfrEmissionPriorityFromNetwork_Type()
)
mscVctVcfrEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscVctVcfrDataPath_Type(AsciiString):
    """Custom type mscVctVcfrDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscVctVcfrDataPath_Type.__name__ = "AsciiString"
_MscVctVcfrDataPath_Object = MibTableColumn
mscVctVcfrDataPath = _MscVctVcfrDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 10, 1, 32),
    _MscVctVcfrDataPath_Type()
)
mscVctVcfrDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrDataPath.setStatus("mandatory")
_MscVctVcfrIntdTable_Object = MibTable
mscVctVcfrIntdTable = _MscVctVcfrIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11)
)
if mibBuilder.loadTexts:
    mscVctVcfrIntdTable.setStatus("mandatory")
_MscVctVcfrIntdEntry_Object = MibTableRow
mscVctVcfrIntdEntry = _MscVctVcfrIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11, 1)
)
mscVctVcfrIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcfrIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcfrIntdEntry.setStatus("mandatory")


class _MscVctVcfrCallReferenceNumber_Type(Hex):
    """Custom type mscVctVcfrCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcfrCallReferenceNumber_Type.__name__ = "Hex"
_MscVctVcfrCallReferenceNumber_Object = MibTableColumn
mscVctVcfrCallReferenceNumber = _MscVctVcfrCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11, 1, 1),
    _MscVctVcfrCallReferenceNumber_Type()
)
mscVctVcfrCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCallReferenceNumber.setStatus("obsolete")


class _MscVctVcfrElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscVctVcfrElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcfrElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscVctVcfrElapsedTimeTillNow_Object = MibTableColumn
mscVctVcfrElapsedTimeTillNow = _MscVctVcfrElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11, 1, 2),
    _MscVctVcfrElapsedTimeTillNow_Type()
)
mscVctVcfrElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrElapsedTimeTillNow.setStatus("mandatory")


class _MscVctVcfrSegmentsRx_Type(Unsigned32):
    """Custom type mscVctVcfrSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcfrSegmentsRx_Type.__name__ = "Unsigned32"
_MscVctVcfrSegmentsRx_Object = MibTableColumn
mscVctVcfrSegmentsRx = _MscVctVcfrSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11, 1, 3),
    _MscVctVcfrSegmentsRx_Type()
)
mscVctVcfrSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrSegmentsRx.setStatus("mandatory")


class _MscVctVcfrSegmentsSent_Type(Unsigned32):
    """Custom type mscVctVcfrSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscVctVcfrSegmentsSent_Type.__name__ = "Unsigned32"
_MscVctVcfrSegmentsSent_Object = MibTableColumn
mscVctVcfrSegmentsSent = _MscVctVcfrSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11, 1, 4),
    _MscVctVcfrSegmentsSent_Type()
)
mscVctVcfrSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrSegmentsSent.setStatus("mandatory")


class _MscVctVcfrStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscVctVcfrStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscVctVcfrStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscVctVcfrStartTime_Object = MibTableColumn
mscVctVcfrStartTime = _MscVctVcfrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11, 1, 5),
    _MscVctVcfrStartTime_Type()
)
mscVctVcfrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrStartTime.setStatus("mandatory")


class _MscVctVcfrCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscVctVcfrCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVctVcfrCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscVctVcfrCallReferenceNumberDecimal_Object = MibTableColumn
mscVctVcfrCallReferenceNumberDecimal = _MscVctVcfrCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 11, 1, 7),
    _MscVctVcfrCallReferenceNumberDecimal_Type()
)
mscVctVcfrCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCallReferenceNumberDecimal.setStatus("mandatory")
_MscVctVcfrFrdTable_Object = MibTable
mscVctVcfrFrdTable = _MscVctVcfrFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12)
)
if mibBuilder.loadTexts:
    mscVctVcfrFrdTable.setStatus("mandatory")
_MscVctVcfrFrdEntry_Object = MibTableRow
mscVctVcfrFrdEntry = _MscVctVcfrFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1)
)
mscVctVcfrFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcfrIndex"),
)
if mibBuilder.loadTexts:
    mscVctVcfrFrdEntry.setStatus("mandatory")


class _MscVctVcfrFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscVctVcfrFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscVctVcfrFrmCongestedToSubnet_Object = MibTableColumn
mscVctVcfrFrmCongestedToSubnet = _MscVctVcfrFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 2),
    _MscVctVcfrFrmCongestedToSubnet_Type()
)
mscVctVcfrFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrFrmCongestedToSubnet.setStatus("mandatory")


class _MscVctVcfrCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscVctVcfrCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscVctVcfrCannotForwardToSubnet_Object = MibTableColumn
mscVctVcfrCannotForwardToSubnet = _MscVctVcfrCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 3),
    _MscVctVcfrCannotForwardToSubnet_Type()
)
mscVctVcfrCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCannotForwardToSubnet.setStatus("mandatory")


class _MscVctVcfrNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscVctVcfrNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscVctVcfrNotDataXferToSubnet_Object = MibTableColumn
mscVctVcfrNotDataXferToSubnet = _MscVctVcfrNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 4),
    _MscVctVcfrNotDataXferToSubnet_Type()
)
mscVctVcfrNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrNotDataXferToSubnet.setStatus("mandatory")


class _MscVctVcfrOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscVctVcfrOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscVctVcfrOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscVctVcfrOutOfRangeFrmFromSubnet = _MscVctVcfrOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 5),
    _MscVctVcfrOutOfRangeFrmFromSubnet_Type()
)
mscVctVcfrOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscVctVcfrCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscVctVcfrCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscVctVcfrCombErrorsFromSubnet_Object = MibTableColumn
mscVctVcfrCombErrorsFromSubnet = _MscVctVcfrCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 6),
    _MscVctVcfrCombErrorsFromSubnet_Type()
)
mscVctVcfrCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrCombErrorsFromSubnet.setStatus("mandatory")


class _MscVctVcfrDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscVctVcfrDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscVctVcfrDuplicatesFromSubnet_Object = MibTableColumn
mscVctVcfrDuplicatesFromSubnet = _MscVctVcfrDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 7),
    _MscVctVcfrDuplicatesFromSubnet_Type()
)
mscVctVcfrDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrDuplicatesFromSubnet.setStatus("mandatory")


class _MscVctVcfrNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscVctVcfrNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscVctVcfrNotDataXferFromSubnet_Object = MibTableColumn
mscVctVcfrNotDataXferFromSubnet = _MscVctVcfrNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 8),
    _MscVctVcfrNotDataXferFromSubnet_Type()
)
mscVctVcfrNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrNotDataXferFromSubnet.setStatus("mandatory")


class _MscVctVcfrFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscVctVcfrFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscVctVcfrFrmLossTimeouts_Object = MibTableColumn
mscVctVcfrFrmLossTimeouts = _MscVctVcfrFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 9),
    _MscVctVcfrFrmLossTimeouts_Type()
)
mscVctVcfrFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrFrmLossTimeouts.setStatus("mandatory")


class _MscVctVcfrOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscVctVcfrOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscVctVcfrOoSeqByteCntExceeded_Object = MibTableColumn
mscVctVcfrOoSeqByteCntExceeded = _MscVctVcfrOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 10),
    _MscVctVcfrOoSeqByteCntExceeded_Type()
)
mscVctVcfrOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrOoSeqByteCntExceeded.setStatus("mandatory")


class _MscVctVcfrPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscVctVcfrPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscVctVcfrPeakOoSeqPktCount_Object = MibTableColumn
mscVctVcfrPeakOoSeqPktCount = _MscVctVcfrPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 11),
    _MscVctVcfrPeakOoSeqPktCount_Type()
)
mscVctVcfrPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPeakOoSeqPktCount.setStatus("mandatory")


class _MscVctVcfrPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscVctVcfrPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscVctVcfrPeakOoSeqFrmForwarded_Object = MibTableColumn
mscVctVcfrPeakOoSeqFrmForwarded = _MscVctVcfrPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 12),
    _MscVctVcfrPeakOoSeqFrmForwarded_Type()
)
mscVctVcfrPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscVctVcfrSendSequenceNumber_Type(Unsigned32):
    """Custom type mscVctVcfrSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscVctVcfrSendSequenceNumber_Object = MibTableColumn
mscVctVcfrSendSequenceNumber = _MscVctVcfrSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 13),
    _MscVctVcfrSendSequenceNumber_Type()
)
mscVctVcfrSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrSendSequenceNumber.setStatus("mandatory")


class _MscVctVcfrPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscVctVcfrPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscVctVcfrPktRetryTimeouts_Object = MibTableColumn
mscVctVcfrPktRetryTimeouts = _MscVctVcfrPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 15),
    _MscVctVcfrPktRetryTimeouts_Type()
)
mscVctVcfrPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPktRetryTimeouts.setStatus("mandatory")


class _MscVctVcfrPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscVctVcfrPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscVctVcfrPeakRetryQueueSize_Object = MibTableColumn
mscVctVcfrPeakRetryQueueSize = _MscVctVcfrPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 16),
    _MscVctVcfrPeakRetryQueueSize_Type()
)
mscVctVcfrPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPeakRetryQueueSize.setStatus("mandatory")


class _MscVctVcfrSubnetRecoveries_Type(Unsigned32):
    """Custom type mscVctVcfrSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscVctVcfrSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscVctVcfrSubnetRecoveries_Object = MibTableColumn
mscVctVcfrSubnetRecoveries = _MscVctVcfrSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 17),
    _MscVctVcfrSubnetRecoveries_Type()
)
mscVctVcfrSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrSubnetRecoveries.setStatus("mandatory")


class _MscVctVcfrOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscVctVcfrOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVctVcfrOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscVctVcfrOoSeqPktCntExceeded_Object = MibTableColumn
mscVctVcfrOoSeqPktCntExceeded = _MscVctVcfrOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 19),
    _MscVctVcfrOoSeqPktCntExceeded_Type()
)
mscVctVcfrOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrOoSeqPktCntExceeded.setStatus("mandatory")


class _MscVctVcfrPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscVctVcfrPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscVctVcfrPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscVctVcfrPeakOoSeqByteCount_Object = MibTableColumn
mscVctVcfrPeakOoSeqByteCount = _MscVctVcfrPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 12, 1, 20),
    _MscVctVcfrPeakOoSeqByteCount_Type()
)
mscVctVcfrPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrPeakOoSeqByteCount.setStatus("mandatory")
_MscVctVcfrDmepTable_Object = MibTable
mscVctVcfrDmepTable = _MscVctVcfrDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 417)
)
if mibBuilder.loadTexts:
    mscVctVcfrDmepTable.setStatus("mandatory")
_MscVctVcfrDmepEntry_Object = MibTableRow
mscVctVcfrDmepEntry = _MscVctVcfrDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 417, 1)
)
mscVctVcfrDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcfrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctVcfrDmepValue"),
)
if mibBuilder.loadTexts:
    mscVctVcfrDmepEntry.setStatus("mandatory")
_MscVctVcfrDmepValue_Type = RowPointer
_MscVctVcfrDmepValue_Object = MibTableColumn
mscVctVcfrDmepValue = _MscVctVcfrDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 5, 417, 1, 1),
    _MscVctVcfrDmepValue_Type()
)
mscVctVcfrDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVctVcfrDmepValue.setStatus("mandatory")
_MscVctProvTable_Object = MibTable
mscVctProvTable = _MscVctProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 10)
)
if mibBuilder.loadTexts:
    mscVctProvTable.setStatus("mandatory")
_MscVctProvEntry_Object = MibTableRow
mscVctProvEntry = _MscVctProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 10, 1)
)
mscVctProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VcTesterMIB", "mscVctIndex"),
)
if mibBuilder.loadTexts:
    mscVctProvEntry.setStatus("mandatory")
_MscVctLogicalProcessor_Type = Link
_MscVctLogicalProcessor_Object = MibTableColumn
mscVctLogicalProcessor = _MscVctLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 10, 1, 1),
    _MscVctLogicalProcessor_Type()
)
mscVctLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctLogicalProcessor.setStatus("mandatory")


class _MscVctVcName_Type(Integer32):
    """Custom type mscVctVcName based on Integer32"""
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


_MscVctVcName_Type.__name__ = "Integer32"
_MscVctVcName_Object = MibTableColumn
mscVctVcName = _MscVctVcName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 5130, 10, 1, 2),
    _MscVctVcName_Type()
)
mscVctVcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVctVcName.setStatus("mandatory")
_VcTesterMIB_ObjectIdentity = ObjectIdentity
vcTesterMIB = _VcTesterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34)
)
_VcTesterGroup_ObjectIdentity = ObjectIdentity
vcTesterGroup = _VcTesterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 1)
)
_VcTesterGroupCA_ObjectIdentity = ObjectIdentity
vcTesterGroupCA = _VcTesterGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 1, 1)
)
_VcTesterGroupCA02_ObjectIdentity = ObjectIdentity
vcTesterGroupCA02 = _VcTesterGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 1, 1, 3)
)
_VcTesterGroupCA02A_ObjectIdentity = ObjectIdentity
vcTesterGroupCA02A = _VcTesterGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 1, 1, 3, 2)
)
_VcTesterCapabilities_ObjectIdentity = ObjectIdentity
vcTesterCapabilities = _VcTesterCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 3)
)
_VcTesterCapabilitiesCA_ObjectIdentity = ObjectIdentity
vcTesterCapabilitiesCA = _VcTesterCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 3, 1)
)
_VcTesterCapabilitiesCA02_ObjectIdentity = ObjectIdentity
vcTesterCapabilitiesCA02 = _VcTesterCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 3, 1, 3)
)
_VcTesterCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
vcTesterCapabilitiesCA02A = _VcTesterCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 34, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VcTesterMIB",
    **{"mscVct": mscVct,
       "mscVctRowStatusTable": mscVctRowStatusTable,
       "mscVctRowStatusEntry": mscVctRowStatusEntry,
       "mscVctRowStatus": mscVctRowStatus,
       "mscVctComponentName": mscVctComponentName,
       "mscVctStorageType": mscVctStorageType,
       "mscVctIndex": mscVctIndex,
       "mscVctDna": mscVctDna,
       "mscVctDnaRowStatusTable": mscVctDnaRowStatusTable,
       "mscVctDnaRowStatusEntry": mscVctDnaRowStatusEntry,
       "mscVctDnaRowStatus": mscVctDnaRowStatus,
       "mscVctDnaComponentName": mscVctDnaComponentName,
       "mscVctDnaStorageType": mscVctDnaStorageType,
       "mscVctDnaIndex": mscVctDnaIndex,
       "mscVctDnaCug": mscVctDnaCug,
       "mscVctDnaCugRowStatusTable": mscVctDnaCugRowStatusTable,
       "mscVctDnaCugRowStatusEntry": mscVctDnaCugRowStatusEntry,
       "mscVctDnaCugRowStatus": mscVctDnaCugRowStatus,
       "mscVctDnaCugComponentName": mscVctDnaCugComponentName,
       "mscVctDnaCugStorageType": mscVctDnaCugStorageType,
       "mscVctDnaCugIndex": mscVctDnaCugIndex,
       "mscVctDnaCugCugOptionsTable": mscVctDnaCugCugOptionsTable,
       "mscVctDnaCugCugOptionsEntry": mscVctDnaCugCugOptionsEntry,
       "mscVctDnaCugType": mscVctDnaCugType,
       "mscVctDnaCugDnic": mscVctDnaCugDnic,
       "mscVctDnaCugInterlockCode": mscVctDnaCugInterlockCode,
       "mscVctDnaCugPreferential": mscVctDnaCugPreferential,
       "mscVctDnaCugOutCalls": mscVctDnaCugOutCalls,
       "mscVctDnaCugIncCalls": mscVctDnaCugIncCalls,
       "mscVctDnaCugPrivileged": mscVctDnaCugPrivileged,
       "mscVctDnaHgM": mscVctDnaHgM,
       "mscVctDnaHgMRowStatusTable": mscVctDnaHgMRowStatusTable,
       "mscVctDnaHgMRowStatusEntry": mscVctDnaHgMRowStatusEntry,
       "mscVctDnaHgMRowStatus": mscVctDnaHgMRowStatus,
       "mscVctDnaHgMComponentName": mscVctDnaHgMComponentName,
       "mscVctDnaHgMStorageType": mscVctDnaHgMStorageType,
       "mscVctDnaHgMIndex": mscVctDnaHgMIndex,
       "mscVctDnaHgMHgAddr": mscVctDnaHgMHgAddr,
       "mscVctDnaHgMHgAddrRowStatusTable": mscVctDnaHgMHgAddrRowStatusTable,
       "mscVctDnaHgMHgAddrRowStatusEntry": mscVctDnaHgMHgAddrRowStatusEntry,
       "mscVctDnaHgMHgAddrRowStatus": mscVctDnaHgMHgAddrRowStatus,
       "mscVctDnaHgMHgAddrComponentName": mscVctDnaHgMHgAddrComponentName,
       "mscVctDnaHgMHgAddrStorageType": mscVctDnaHgMHgAddrStorageType,
       "mscVctDnaHgMHgAddrIndex": mscVctDnaHgMHgAddrIndex,
       "mscVctDnaHgMHgAddrAddrTable": mscVctDnaHgMHgAddrAddrTable,
       "mscVctDnaHgMHgAddrAddrEntry": mscVctDnaHgMHgAddrAddrEntry,
       "mscVctDnaHgMHgAddrNumberingPlanIndicator": mscVctDnaHgMHgAddrNumberingPlanIndicator,
       "mscVctDnaHgMHgAddrDataNetworkAddress": mscVctDnaHgMHgAddrDataNetworkAddress,
       "mscVctDnaHgMIfTable": mscVctDnaHgMIfTable,
       "mscVctDnaHgMIfEntry": mscVctDnaHgMIfEntry,
       "mscVctDnaHgMAvailabilityUpdateThreshold": mscVctDnaHgMAvailabilityUpdateThreshold,
       "mscVctDnaHgMOpTable": mscVctDnaHgMOpTable,
       "mscVctDnaHgMOpEntry": mscVctDnaHgMOpEntry,
       "mscVctDnaHgMMaxAvailableChannels": mscVctDnaHgMMaxAvailableChannels,
       "mscVctDnaHgMAvailableChannels": mscVctDnaHgMAvailableChannels,
       "mscVctDnaHgMAvailabilityDelta": mscVctDnaHgMAvailabilityDelta,
       "mscVctDnaAddressTable": mscVctDnaAddressTable,
       "mscVctDnaAddressEntry": mscVctDnaAddressEntry,
       "mscVctDnaNumberingPlanIndicator": mscVctDnaNumberingPlanIndicator,
       "mscVctDnaDataNetworkAddress": mscVctDnaDataNetworkAddress,
       "mscVctDnaOutgoingOptionsTable": mscVctDnaOutgoingOptionsTable,
       "mscVctDnaOutgoingOptionsEntry": mscVctDnaOutgoingOptionsEntry,
       "mscVctDnaOutCalls": mscVctDnaOutCalls,
       "mscVctDnaOutNormalCharge": mscVctDnaOutNormalCharge,
       "mscVctDnaOutReverseCharge": mscVctDnaOutReverseCharge,
       "mscVctDnaOutForceReverseCharge": mscVctDnaOutForceReverseCharge,
       "mscVctDnaOutNormalPriority": mscVctDnaOutNormalPriority,
       "mscVctDnaOutHighPriority": mscVctDnaOutHighPriority,
       "mscVctDnaOutDefaultPriority": mscVctDnaOutDefaultPriority,
       "mscVctDnaOutIntl": mscVctDnaOutIntl,
       "mscVctDnaOutFsRestrictedResponse": mscVctDnaOutFsRestrictedResponse,
       "mscVctDnaOutFsUnrestrictedResponse": mscVctDnaOutFsUnrestrictedResponse,
       "mscVctDnaOutDefaultPathSensitivity": mscVctDnaOutDefaultPathSensitivity,
       "mscVctDnaOutPathSensitivityOverRide": mscVctDnaOutPathSensitivityOverRide,
       "mscVctDnaOutPathSensitivitySignal": mscVctDnaOutPathSensitivitySignal,
       "mscVctDnaOutDefaultPathReliability": mscVctDnaOutDefaultPathReliability,
       "mscVctDnaOutPathReliabilityOverRide": mscVctDnaOutPathReliabilityOverRide,
       "mscVctDnaOutPathReliabilitySignal": mscVctDnaOutPathReliabilitySignal,
       "mscVctDnaOutAccess": mscVctDnaOutAccess,
       "mscVctDnaDefaultTransferPriority": mscVctDnaDefaultTransferPriority,
       "mscVctDnaTransferPriorityOverRide": mscVctDnaTransferPriorityOverRide,
       "mscVctDnaIncomingOptionsTable": mscVctDnaIncomingOptionsTable,
       "mscVctDnaIncomingOptionsEntry": mscVctDnaIncomingOptionsEntry,
       "mscVctDnaIncCalls": mscVctDnaIncCalls,
       "mscVctDnaIncHighPriorityReverseCharge": mscVctDnaIncHighPriorityReverseCharge,
       "mscVctDnaIncNormalPriorityReverseCharge": mscVctDnaIncNormalPriorityReverseCharge,
       "mscVctDnaIncIntlNormalCharge": mscVctDnaIncIntlNormalCharge,
       "mscVctDnaIncIntlReverseCharge": mscVctDnaIncIntlReverseCharge,
       "mscVctDnaIncFastSelect": mscVctDnaIncFastSelect,
       "mscVctDnaIncSameService": mscVctDnaIncSameService,
       "mscVctDnaIncChargeTransfer": mscVctDnaIncChargeTransfer,
       "mscVctDnaIncAccess": mscVctDnaIncAccess,
       "mscVctDnaCallOptionsTable": mscVctDnaCallOptionsTable,
       "mscVctDnaCallOptionsEntry": mscVctDnaCallOptionsEntry,
       "mscVctDnaServiceCategory": mscVctDnaServiceCategory,
       "mscVctDnaPacketSizes": mscVctDnaPacketSizes,
       "mscVctDnaDefaultRecvFrmNetworkPacketSize": mscVctDnaDefaultRecvFrmNetworkPacketSize,
       "mscVctDnaDefaultSendToNetworkPacketSize": mscVctDnaDefaultSendToNetworkPacketSize,
       "mscVctDnaDefaultRecvFrmNetworkThruputClass": mscVctDnaDefaultRecvFrmNetworkThruputClass,
       "mscVctDnaDefaultSendToNetworkThruputClass": mscVctDnaDefaultSendToNetworkThruputClass,
       "mscVctDnaDefaultRecvFrmNetworkWindowSize": mscVctDnaDefaultRecvFrmNetworkWindowSize,
       "mscVctDnaDefaultSendToNetworkWindowSize": mscVctDnaDefaultSendToNetworkWindowSize,
       "mscVctDnaPacketSizeNegotiation": mscVctDnaPacketSizeNegotiation,
       "mscVctDnaCugFormat": mscVctDnaCugFormat,
       "mscVctDnaCug0AsNonCugCall": mscVctDnaCug0AsNonCugCall,
       "mscVctDnaSignalPreferentialCugToLink": mscVctDnaSignalPreferentialCugToLink,
       "mscVctDnaSignalIntlAddressToLink": mscVctDnaSignalIntlAddressToLink,
       "mscVctDnaFastSelectCallsOnly": mscVctDnaFastSelectCallsOnly,
       "mscVctDnaPreselectRpoa": mscVctDnaPreselectRpoa,
       "mscVctDnaAccountClass": mscVctDnaAccountClass,
       "mscVctDnaAccountCollection": mscVctDnaAccountCollection,
       "mscVctDnaServiceExchange": mscVctDnaServiceExchange,
       "mscVctDnaEgressAccounting": mscVctDnaEgressAccounting,
       "mscVctDnaRpoa": mscVctDnaRpoa,
       "mscVctDnaDataPath": mscVctDnaDataPath,
       "mscVctDc": mscVctDc,
       "mscVctDcRowStatusTable": mscVctDcRowStatusTable,
       "mscVctDcRowStatusEntry": mscVctDcRowStatusEntry,
       "mscVctDcRowStatus": mscVctDcRowStatus,
       "mscVctDcComponentName": mscVctDcComponentName,
       "mscVctDcStorageType": mscVctDcStorageType,
       "mscVctDcIndex": mscVctDcIndex,
       "mscVctDcOptionsTable": mscVctDcOptionsTable,
       "mscVctDcOptionsEntry": mscVctDcOptionsEntry,
       "mscVctDcLocalNpi": mscVctDcLocalNpi,
       "mscVctDcLocalDna": mscVctDcLocalDna,
       "mscVctDcRemoteNpi": mscVctDcRemoteNpi,
       "mscVctDcRemoteDna": mscVctDcRemoteDna,
       "mscVctDcRemoteLcn": mscVctDcRemoteLcn,
       "mscVctDcType": mscVctDcType,
       "mscVctDcSvcAutoCallRetry": mscVctDcSvcAutoCallRetry,
       "mscVctDcUserData": mscVctDcUserData,
       "mscVctDcDiscardPriority": mscVctDcDiscardPriority,
       "mscVctDcDataPath": mscVctDcDataPath,
       "mscVctDcCugIndex": mscVctDcCugIndex,
       "mscVctDcCugType": mscVctDcCugType,
       "mscVctDcCfaTable": mscVctDcCfaTable,
       "mscVctDcCfaEntry": mscVctDcCfaEntry,
       "mscVctDcCfaIndex": mscVctDcCfaIndex,
       "mscVctDcCfaValue": mscVctDcCfaValue,
       "mscVctDcCfaRowStatus": mscVctDcCfaRowStatus,
       "mscVctDcDfaTable": mscVctDcDfaTable,
       "mscVctDcDfaEntry": mscVctDcDfaEntry,
       "mscVctDcDfaIndex": mscVctDcDfaIndex,
       "mscVctDcDfaValue": mscVctDcDfaValue,
       "mscVctDcDfaRowStatus": mscVctDcDfaRowStatus,
       "mscVctDcNfaTable": mscVctDcNfaTable,
       "mscVctDcNfaEntry": mscVctDcNfaEntry,
       "mscVctDcNfaIndex": mscVctDcNfaIndex,
       "mscVctDcNfaValue": mscVctDcNfaValue,
       "mscVctDcNfaRowStatus": mscVctDcNfaRowStatus,
       "mscVctDcIfaTable": mscVctDcIfaTable,
       "mscVctDcIfaEntry": mscVctDcIfaEntry,
       "mscVctDcIfaIndex": mscVctDcIfaIndex,
       "mscVctDcIfaValue": mscVctDcIfaValue,
       "mscVctDcIfaRowStatus": mscVctDcIfaRowStatus,
       "mscVctVc": mscVctVc,
       "mscVctVcRowStatusTable": mscVctVcRowStatusTable,
       "mscVctVcRowStatusEntry": mscVctVcRowStatusEntry,
       "mscVctVcRowStatus": mscVctVcRowStatus,
       "mscVctVcComponentName": mscVctVcComponentName,
       "mscVctVcStorageType": mscVctVcStorageType,
       "mscVctVcIndex": mscVctVcIndex,
       "mscVctVcCadTable": mscVctVcCadTable,
       "mscVctVcCadEntry": mscVctVcCadEntry,
       "mscVctVcType": mscVctVcType,
       "mscVctVcState": mscVctVcState,
       "mscVctVcPreviousState": mscVctVcPreviousState,
       "mscVctVcDiagnosticCode": mscVctVcDiagnosticCode,
       "mscVctVcPreviousDiagnosticCode": mscVctVcPreviousDiagnosticCode,
       "mscVctVcCalledNpi": mscVctVcCalledNpi,
       "mscVctVcCalledDna": mscVctVcCalledDna,
       "mscVctVcCalledLcn": mscVctVcCalledLcn,
       "mscVctVcCallingNpi": mscVctVcCallingNpi,
       "mscVctVcCallingDna": mscVctVcCallingDna,
       "mscVctVcCallingLcn": mscVctVcCallingLcn,
       "mscVctVcAccountingEnabled": mscVctVcAccountingEnabled,
       "mscVctVcFastSelectCall": mscVctVcFastSelectCall,
       "mscVctVcLocalRxPktSize": mscVctVcLocalRxPktSize,
       "mscVctVcLocalTxPktSize": mscVctVcLocalTxPktSize,
       "mscVctVcLocalTxWindowSize": mscVctVcLocalTxWindowSize,
       "mscVctVcLocalRxWindowSize": mscVctVcLocalRxWindowSize,
       "mscVctVcPathReliability": mscVctVcPathReliability,
       "mscVctVcAccountingEnd": mscVctVcAccountingEnd,
       "mscVctVcPriority": mscVctVcPriority,
       "mscVctVcSegmentSize": mscVctVcSegmentSize,
       "mscVctVcSubnetTxPktSize": mscVctVcSubnetTxPktSize,
       "mscVctVcSubnetTxWindowSize": mscVctVcSubnetTxWindowSize,
       "mscVctVcSubnetRxPktSize": mscVctVcSubnetRxPktSize,
       "mscVctVcSubnetRxWindowSize": mscVctVcSubnetRxWindowSize,
       "mscVctVcMaxSubnetPktSize": mscVctVcMaxSubnetPktSize,
       "mscVctVcTransferPriorityToNetwork": mscVctVcTransferPriorityToNetwork,
       "mscVctVcTransferPriorityFromNetwork": mscVctVcTransferPriorityFromNetwork,
       "mscVctVcIntdTable": mscVctVcIntdTable,
       "mscVctVcIntdEntry": mscVctVcIntdEntry,
       "mscVctVcCallReferenceNumber": mscVctVcCallReferenceNumber,
       "mscVctVcElapsedTimeTillNow": mscVctVcElapsedTimeTillNow,
       "mscVctVcSegmentsRx": mscVctVcSegmentsRx,
       "mscVctVcSegmentsSent": mscVctVcSegmentsSent,
       "mscVctVcStartTime": mscVctVcStartTime,
       "mscVctVcCallReferenceNumberDecimal": mscVctVcCallReferenceNumberDecimal,
       "mscVctVcStatsTable": mscVctVcStatsTable,
       "mscVctVcStatsEntry": mscVctVcStatsEntry,
       "mscVctVcAckStackingTimeouts": mscVctVcAckStackingTimeouts,
       "mscVctVcOutOfRangeFrmFromSubnet": mscVctVcOutOfRangeFrmFromSubnet,
       "mscVctVcDuplicatesFromSubnet": mscVctVcDuplicatesFromSubnet,
       "mscVctVcFrmRetryTimeouts": mscVctVcFrmRetryTimeouts,
       "mscVctVcPeakRetryQueueSize": mscVctVcPeakRetryQueueSize,
       "mscVctVcPeakOoSeqQueueSize": mscVctVcPeakOoSeqQueueSize,
       "mscVctVcPeakOoSeqFrmForwarded": mscVctVcPeakOoSeqFrmForwarded,
       "mscVctVcPeakStackedAcksRx": mscVctVcPeakStackedAcksRx,
       "mscVctVcSubnetRecoveries": mscVctVcSubnetRecoveries,
       "mscVctVcWindowClosuresToSubnet": mscVctVcWindowClosuresToSubnet,
       "mscVctVcWindowClosuresFromSubnet": mscVctVcWindowClosuresFromSubnet,
       "mscVctVcWrTriggers": mscVctVcWrTriggers,
       "mscVctVcfr": mscVctVcfr,
       "mscVctVcfrRowStatusTable": mscVctVcfrRowStatusTable,
       "mscVctVcfrRowStatusEntry": mscVctVcfrRowStatusEntry,
       "mscVctVcfrRowStatus": mscVctVcfrRowStatus,
       "mscVctVcfrComponentName": mscVctVcfrComponentName,
       "mscVctVcfrStorageType": mscVctVcfrStorageType,
       "mscVctVcfrIndex": mscVctVcfrIndex,
       "mscVctVcfrCadTable": mscVctVcfrCadTable,
       "mscVctVcfrCadEntry": mscVctVcfrCadEntry,
       "mscVctVcfrType": mscVctVcfrType,
       "mscVctVcfrState": mscVctVcfrState,
       "mscVctVcfrPreviousState": mscVctVcfrPreviousState,
       "mscVctVcfrDiagnosticCode": mscVctVcfrDiagnosticCode,
       "mscVctVcfrPreviousDiagnosticCode": mscVctVcfrPreviousDiagnosticCode,
       "mscVctVcfrCalledNpi": mscVctVcfrCalledNpi,
       "mscVctVcfrCalledDna": mscVctVcfrCalledDna,
       "mscVctVcfrCalledLcn": mscVctVcfrCalledLcn,
       "mscVctVcfrCallingNpi": mscVctVcfrCallingNpi,
       "mscVctVcfrCallingDna": mscVctVcfrCallingDna,
       "mscVctVcfrCallingLcn": mscVctVcfrCallingLcn,
       "mscVctVcfrAccountingEnabled": mscVctVcfrAccountingEnabled,
       "mscVctVcfrFastSelectCall": mscVctVcfrFastSelectCall,
       "mscVctVcfrPathReliability": mscVctVcfrPathReliability,
       "mscVctVcfrAccountingEnd": mscVctVcfrAccountingEnd,
       "mscVctVcfrPriority": mscVctVcfrPriority,
       "mscVctVcfrSegmentSize": mscVctVcfrSegmentSize,
       "mscVctVcfrMaxSubnetPktSize": mscVctVcfrMaxSubnetPktSize,
       "mscVctVcfrRcosToNetwork": mscVctVcfrRcosToNetwork,
       "mscVctVcfrRcosFromNetwork": mscVctVcfrRcosFromNetwork,
       "mscVctVcfrEmissionPriorityToNetwork": mscVctVcfrEmissionPriorityToNetwork,
       "mscVctVcfrEmissionPriorityFromNetwork": mscVctVcfrEmissionPriorityFromNetwork,
       "mscVctVcfrDataPath": mscVctVcfrDataPath,
       "mscVctVcfrIntdTable": mscVctVcfrIntdTable,
       "mscVctVcfrIntdEntry": mscVctVcfrIntdEntry,
       "mscVctVcfrCallReferenceNumber": mscVctVcfrCallReferenceNumber,
       "mscVctVcfrElapsedTimeTillNow": mscVctVcfrElapsedTimeTillNow,
       "mscVctVcfrSegmentsRx": mscVctVcfrSegmentsRx,
       "mscVctVcfrSegmentsSent": mscVctVcfrSegmentsSent,
       "mscVctVcfrStartTime": mscVctVcfrStartTime,
       "mscVctVcfrCallReferenceNumberDecimal": mscVctVcfrCallReferenceNumberDecimal,
       "mscVctVcfrFrdTable": mscVctVcfrFrdTable,
       "mscVctVcfrFrdEntry": mscVctVcfrFrdEntry,
       "mscVctVcfrFrmCongestedToSubnet": mscVctVcfrFrmCongestedToSubnet,
       "mscVctVcfrCannotForwardToSubnet": mscVctVcfrCannotForwardToSubnet,
       "mscVctVcfrNotDataXferToSubnet": mscVctVcfrNotDataXferToSubnet,
       "mscVctVcfrOutOfRangeFrmFromSubnet": mscVctVcfrOutOfRangeFrmFromSubnet,
       "mscVctVcfrCombErrorsFromSubnet": mscVctVcfrCombErrorsFromSubnet,
       "mscVctVcfrDuplicatesFromSubnet": mscVctVcfrDuplicatesFromSubnet,
       "mscVctVcfrNotDataXferFromSubnet": mscVctVcfrNotDataXferFromSubnet,
       "mscVctVcfrFrmLossTimeouts": mscVctVcfrFrmLossTimeouts,
       "mscVctVcfrOoSeqByteCntExceeded": mscVctVcfrOoSeqByteCntExceeded,
       "mscVctVcfrPeakOoSeqPktCount": mscVctVcfrPeakOoSeqPktCount,
       "mscVctVcfrPeakOoSeqFrmForwarded": mscVctVcfrPeakOoSeqFrmForwarded,
       "mscVctVcfrSendSequenceNumber": mscVctVcfrSendSequenceNumber,
       "mscVctVcfrPktRetryTimeouts": mscVctVcfrPktRetryTimeouts,
       "mscVctVcfrPeakRetryQueueSize": mscVctVcfrPeakRetryQueueSize,
       "mscVctVcfrSubnetRecoveries": mscVctVcfrSubnetRecoveries,
       "mscVctVcfrOoSeqPktCntExceeded": mscVctVcfrOoSeqPktCntExceeded,
       "mscVctVcfrPeakOoSeqByteCount": mscVctVcfrPeakOoSeqByteCount,
       "mscVctVcfrDmepTable": mscVctVcfrDmepTable,
       "mscVctVcfrDmepEntry": mscVctVcfrDmepEntry,
       "mscVctVcfrDmepValue": mscVctVcfrDmepValue,
       "mscVctProvTable": mscVctProvTable,
       "mscVctProvEntry": mscVctProvEntry,
       "mscVctLogicalProcessor": mscVctLogicalProcessor,
       "mscVctVcName": mscVctVcName,
       "vcTesterMIB": vcTesterMIB,
       "vcTesterGroup": vcTesterGroup,
       "vcTesterGroupCA": vcTesterGroupCA,
       "vcTesterGroupCA02": vcTesterGroupCA02,
       "vcTesterGroupCA02A": vcTesterGroupCA02A,
       "vcTesterCapabilities": vcTesterCapabilities,
       "vcTesterCapabilitiesCA": vcTesterCapabilitiesCA,
       "vcTesterCapabilitiesCA02": vcTesterCapabilitiesCA02,
       "vcTesterCapabilitiesCA02A": vcTesterCapabilitiesCA02A}
)
