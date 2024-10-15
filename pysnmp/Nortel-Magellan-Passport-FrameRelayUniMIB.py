# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayUniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayUniMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:47 2024
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
 Gauge32,
 Integer32,
 InterfaceIndex,
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
    "InterfaceIndex",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 DigitString,
 EnterpriseDateAndTime,
 FixedPoint3,
 Hex,
 HexString,
 Link,
 NonReplicated,
 Unsigned64) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "FixedPoint3",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated",
    "Unsigned64")

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

_FrUni_ObjectIdentity = ObjectIdentity
frUni = _FrUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71)
)
_FrUniRowStatusTable_Object = MibTable
frUniRowStatusTable = _FrUniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 1)
)
if mibBuilder.loadTexts:
    frUniRowStatusTable.setStatus("mandatory")
_FrUniRowStatusEntry_Object = MibTableRow
frUniRowStatusEntry = _FrUniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 1, 1)
)
frUniRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
)
if mibBuilder.loadTexts:
    frUniRowStatusEntry.setStatus("mandatory")
_FrUniRowStatus_Type = RowStatus
_FrUniRowStatus_Object = MibTableColumn
frUniRowStatus = _FrUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 1, 1, 1),
    _FrUniRowStatus_Type()
)
frUniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniRowStatus.setStatus("mandatory")
_FrUniComponentName_Type = DisplayString
_FrUniComponentName_Object = MibTableColumn
frUniComponentName = _FrUniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 1, 1, 2),
    _FrUniComponentName_Type()
)
frUniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniComponentName.setStatus("mandatory")
_FrUniStorageType_Type = StorageType
_FrUniStorageType_Object = MibTableColumn
frUniStorageType = _FrUniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 1, 1, 4),
    _FrUniStorageType_Type()
)
frUniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniStorageType.setStatus("mandatory")


class _FrUniIndex_Type(Integer32):
    """Custom type frUniIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrUniIndex_Type.__name__ = "Integer32"
_FrUniIndex_Object = MibTableColumn
frUniIndex = _FrUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 1, 1, 10),
    _FrUniIndex_Type()
)
frUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniIndex.setStatus("mandatory")
_FrUniDna_ObjectIdentity = ObjectIdentity
frUniDna = _FrUniDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2)
)
_FrUniDnaRowStatusTable_Object = MibTable
frUniDnaRowStatusTable = _FrUniDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 1)
)
if mibBuilder.loadTexts:
    frUniDnaRowStatusTable.setStatus("mandatory")
_FrUniDnaRowStatusEntry_Object = MibTableRow
frUniDnaRowStatusEntry = _FrUniDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 1, 1)
)
frUniDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaRowStatusEntry.setStatus("mandatory")
_FrUniDnaRowStatus_Type = RowStatus
_FrUniDnaRowStatus_Object = MibTableColumn
frUniDnaRowStatus = _FrUniDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 1, 1, 1),
    _FrUniDnaRowStatus_Type()
)
frUniDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaRowStatus.setStatus("mandatory")
_FrUniDnaComponentName_Type = DisplayString
_FrUniDnaComponentName_Object = MibTableColumn
frUniDnaComponentName = _FrUniDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 1, 1, 2),
    _FrUniDnaComponentName_Type()
)
frUniDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaComponentName.setStatus("mandatory")
_FrUniDnaStorageType_Type = StorageType
_FrUniDnaStorageType_Object = MibTableColumn
frUniDnaStorageType = _FrUniDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 1, 1, 4),
    _FrUniDnaStorageType_Type()
)
frUniDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaStorageType.setStatus("mandatory")
_FrUniDnaIndex_Type = NonReplicated
_FrUniDnaIndex_Object = MibTableColumn
frUniDnaIndex = _FrUniDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 1, 1, 10),
    _FrUniDnaIndex_Type()
)
frUniDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDnaIndex.setStatus("mandatory")
_FrUniDnaCug_ObjectIdentity = ObjectIdentity
frUniDnaCug = _FrUniDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2)
)
_FrUniDnaCugRowStatusTable_Object = MibTable
frUniDnaCugRowStatusTable = _FrUniDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 1)
)
if mibBuilder.loadTexts:
    frUniDnaCugRowStatusTable.setStatus("mandatory")
_FrUniDnaCugRowStatusEntry_Object = MibTableRow
frUniDnaCugRowStatusEntry = _FrUniDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 1, 1)
)
frUniDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaCugRowStatusEntry.setStatus("mandatory")
_FrUniDnaCugRowStatus_Type = RowStatus
_FrUniDnaCugRowStatus_Object = MibTableColumn
frUniDnaCugRowStatus = _FrUniDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 1, 1, 1),
    _FrUniDnaCugRowStatus_Type()
)
frUniDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaCugRowStatus.setStatus("mandatory")
_FrUniDnaCugComponentName_Type = DisplayString
_FrUniDnaCugComponentName_Object = MibTableColumn
frUniDnaCugComponentName = _FrUniDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 1, 1, 2),
    _FrUniDnaCugComponentName_Type()
)
frUniDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaCugComponentName.setStatus("mandatory")
_FrUniDnaCugStorageType_Type = StorageType
_FrUniDnaCugStorageType_Object = MibTableColumn
frUniDnaCugStorageType = _FrUniDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 1, 1, 4),
    _FrUniDnaCugStorageType_Type()
)
frUniDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaCugStorageType.setStatus("mandatory")


class _FrUniDnaCugIndex_Type(Integer32):
    """Custom type frUniDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniDnaCugIndex_Type.__name__ = "Integer32"
_FrUniDnaCugIndex_Object = MibTableColumn
frUniDnaCugIndex = _FrUniDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 1, 1, 10),
    _FrUniDnaCugIndex_Type()
)
frUniDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDnaCugIndex.setStatus("mandatory")
_FrUniDnaCugCugOptionsTable_Object = MibTable
frUniDnaCugCugOptionsTable = _FrUniDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10)
)
if mibBuilder.loadTexts:
    frUniDnaCugCugOptionsTable.setStatus("mandatory")
_FrUniDnaCugCugOptionsEntry_Object = MibTableRow
frUniDnaCugCugOptionsEntry = _FrUniDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10, 1)
)
frUniDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaCugCugOptionsEntry.setStatus("mandatory")


class _FrUniDnaCugType_Type(Integer32):
    """Custom type frUniDnaCugType based on Integer32"""
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


_FrUniDnaCugType_Type.__name__ = "Integer32"
_FrUniDnaCugType_Object = MibTableColumn
frUniDnaCugType = _FrUniDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10, 1, 1),
    _FrUniDnaCugType_Type()
)
frUniDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaCugType.setStatus("mandatory")


class _FrUniDnaCugDnic_Type(DigitString):
    """Custom type frUniDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_FrUniDnaCugDnic_Type.__name__ = "DigitString"
_FrUniDnaCugDnic_Object = MibTableColumn
frUniDnaCugDnic = _FrUniDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10, 1, 2),
    _FrUniDnaCugDnic_Type()
)
frUniDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaCugDnic.setStatus("mandatory")


class _FrUniDnaCugInterlockCode_Type(Unsigned32):
    """Custom type frUniDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrUniDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_FrUniDnaCugInterlockCode_Object = MibTableColumn
frUniDnaCugInterlockCode = _FrUniDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10, 1, 3),
    _FrUniDnaCugInterlockCode_Type()
)
frUniDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaCugInterlockCode.setStatus("mandatory")


class _FrUniDnaCugPreferential_Type(Integer32):
    """Custom type frUniDnaCugPreferential based on Integer32"""
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


_FrUniDnaCugPreferential_Type.__name__ = "Integer32"
_FrUniDnaCugPreferential_Object = MibTableColumn
frUniDnaCugPreferential = _FrUniDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10, 1, 4),
    _FrUniDnaCugPreferential_Type()
)
frUniDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaCugPreferential.setStatus("mandatory")


class _FrUniDnaCugOutCalls_Type(Integer32):
    """Custom type frUniDnaCugOutCalls based on Integer32"""
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


_FrUniDnaCugOutCalls_Type.__name__ = "Integer32"
_FrUniDnaCugOutCalls_Object = MibTableColumn
frUniDnaCugOutCalls = _FrUniDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10, 1, 5),
    _FrUniDnaCugOutCalls_Type()
)
frUniDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaCugOutCalls.setStatus("mandatory")


class _FrUniDnaCugIncCalls_Type(Integer32):
    """Custom type frUniDnaCugIncCalls based on Integer32"""
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


_FrUniDnaCugIncCalls_Type.__name__ = "Integer32"
_FrUniDnaCugIncCalls_Object = MibTableColumn
frUniDnaCugIncCalls = _FrUniDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 2, 10, 1, 6),
    _FrUniDnaCugIncCalls_Type()
)
frUniDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaCugIncCalls.setStatus("mandatory")
_FrUniDnaHgM_ObjectIdentity = ObjectIdentity
frUniDnaHgM = _FrUniDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3)
)
_FrUniDnaHgMRowStatusTable_Object = MibTable
frUniDnaHgMRowStatusTable = _FrUniDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 1)
)
if mibBuilder.loadTexts:
    frUniDnaHgMRowStatusTable.setStatus("mandatory")
_FrUniDnaHgMRowStatusEntry_Object = MibTableRow
frUniDnaHgMRowStatusEntry = _FrUniDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 1, 1)
)
frUniDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaHgMRowStatusEntry.setStatus("mandatory")
_FrUniDnaHgMRowStatus_Type = RowStatus
_FrUniDnaHgMRowStatus_Object = MibTableColumn
frUniDnaHgMRowStatus = _FrUniDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 1, 1, 1),
    _FrUniDnaHgMRowStatus_Type()
)
frUniDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaHgMRowStatus.setStatus("mandatory")
_FrUniDnaHgMComponentName_Type = DisplayString
_FrUniDnaHgMComponentName_Object = MibTableColumn
frUniDnaHgMComponentName = _FrUniDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 1, 1, 2),
    _FrUniDnaHgMComponentName_Type()
)
frUniDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMComponentName.setStatus("mandatory")
_FrUniDnaHgMStorageType_Type = StorageType
_FrUniDnaHgMStorageType_Object = MibTableColumn
frUniDnaHgMStorageType = _FrUniDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 1, 1, 4),
    _FrUniDnaHgMStorageType_Type()
)
frUniDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMStorageType.setStatus("mandatory")
_FrUniDnaHgMIndex_Type = NonReplicated
_FrUniDnaHgMIndex_Object = MibTableColumn
frUniDnaHgMIndex = _FrUniDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 1, 1, 10),
    _FrUniDnaHgMIndex_Type()
)
frUniDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDnaHgMIndex.setStatus("mandatory")
_FrUniDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
frUniDnaHgMHgAddr = _FrUniDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2)
)
_FrUniDnaHgMHgAddrRowStatusTable_Object = MibTable
frUniDnaHgMHgAddrRowStatusTable = _FrUniDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_FrUniDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
frUniDnaHgMHgAddrRowStatusEntry = _FrUniDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 1, 1)
)
frUniDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_FrUniDnaHgMHgAddrRowStatus_Type = RowStatus
_FrUniDnaHgMHgAddrRowStatus_Object = MibTableColumn
frUniDnaHgMHgAddrRowStatus = _FrUniDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 1, 1, 1),
    _FrUniDnaHgMHgAddrRowStatus_Type()
)
frUniDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrRowStatus.setStatus("mandatory")
_FrUniDnaHgMHgAddrComponentName_Type = DisplayString
_FrUniDnaHgMHgAddrComponentName_Object = MibTableColumn
frUniDnaHgMHgAddrComponentName = _FrUniDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 1, 1, 2),
    _FrUniDnaHgMHgAddrComponentName_Type()
)
frUniDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrComponentName.setStatus("mandatory")
_FrUniDnaHgMHgAddrStorageType_Type = StorageType
_FrUniDnaHgMHgAddrStorageType_Object = MibTableColumn
frUniDnaHgMHgAddrStorageType = _FrUniDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 1, 1, 4),
    _FrUniDnaHgMHgAddrStorageType_Type()
)
frUniDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrStorageType.setStatus("mandatory")


class _FrUniDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type frUniDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FrUniDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_FrUniDnaHgMHgAddrIndex_Object = MibTableColumn
frUniDnaHgMHgAddrIndex = _FrUniDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 1, 1, 10),
    _FrUniDnaHgMHgAddrIndex_Type()
)
frUniDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrIndex.setStatus("mandatory")
_FrUniDnaHgMHgAddrAddrTable_Object = MibTable
frUniDnaHgMHgAddrAddrTable = _FrUniDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrAddrTable.setStatus("mandatory")
_FrUniDnaHgMHgAddrAddrEntry_Object = MibTableRow
frUniDnaHgMHgAddrAddrEntry = _FrUniDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 10, 1)
)
frUniDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _FrUniDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type frUniDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
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


_FrUniDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_FrUniDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
frUniDnaHgMHgAddrNumberingPlanIndicator = _FrUniDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 10, 1, 1),
    _FrUniDnaHgMHgAddrNumberingPlanIndicator_Type()
)
frUniDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _FrUniDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type frUniDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrUniDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_FrUniDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
frUniDnaHgMHgAddrDataNetworkAddress = _FrUniDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 2, 10, 1, 2),
    _FrUniDnaHgMHgAddrDataNetworkAddress_Type()
)
frUniDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_FrUniDnaHgMIfTable_Object = MibTable
frUniDnaHgMIfTable = _FrUniDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 10)
)
if mibBuilder.loadTexts:
    frUniDnaHgMIfTable.setStatus("mandatory")
_FrUniDnaHgMIfEntry_Object = MibTableRow
frUniDnaHgMIfEntry = _FrUniDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 10, 1)
)
frUniDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaHgMIfEntry.setStatus("mandatory")


class _FrUniDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type frUniDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 16777216),
    )


_FrUniDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_FrUniDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
frUniDnaHgMAvailabilityUpdateThreshold = _FrUniDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 10, 1, 1),
    _FrUniDnaHgMAvailabilityUpdateThreshold_Type()
)
frUniDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_FrUniDnaHgMOpTable_Object = MibTable
frUniDnaHgMOpTable = _FrUniDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 11)
)
if mibBuilder.loadTexts:
    frUniDnaHgMOpTable.setStatus("mandatory")
_FrUniDnaHgMOpEntry_Object = MibTableRow
frUniDnaHgMOpEntry = _FrUniDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 11, 1)
)
frUniDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaHgMOpEntry.setStatus("mandatory")


class _FrUniDnaHgMMaximumAvailableAggregateCir_Type(Unsigned32):
    """Custom type frUniDnaHgMMaximumAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDnaHgMMaximumAvailableAggregateCir_Type.__name__ = "Unsigned32"
_FrUniDnaHgMMaximumAvailableAggregateCir_Object = MibTableColumn
frUniDnaHgMMaximumAvailableAggregateCir = _FrUniDnaHgMMaximumAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 11, 1, 1),
    _FrUniDnaHgMMaximumAvailableAggregateCir_Type()
)
frUniDnaHgMMaximumAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMMaximumAvailableAggregateCir.setStatus("mandatory")


class _FrUniDnaHgMAvailableAggregateCir_Type(Unsigned32):
    """Custom type frUniDnaHgMAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDnaHgMAvailableAggregateCir_Type.__name__ = "Unsigned32"
_FrUniDnaHgMAvailableAggregateCir_Object = MibTableColumn
frUniDnaHgMAvailableAggregateCir = _FrUniDnaHgMAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 11, 1, 2),
    _FrUniDnaHgMAvailableAggregateCir_Type()
)
frUniDnaHgMAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMAvailableAggregateCir.setStatus("mandatory")


class _FrUniDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type frUniDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16777216, 16777215),
    )


_FrUniDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_FrUniDnaHgMAvailabilityDelta_Object = MibTableColumn
frUniDnaHgMAvailabilityDelta = _FrUniDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 11, 1, 3),
    _FrUniDnaHgMAvailabilityDelta_Type()
)
frUniDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMAvailabilityDelta.setStatus("mandatory")


class _FrUniDnaHgMAvailableDlcis_Type(Unsigned32):
    """Custom type frUniDnaHgMAvailableDlcis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FrUniDnaHgMAvailableDlcis_Type.__name__ = "Unsigned32"
_FrUniDnaHgMAvailableDlcis_Object = MibTableColumn
frUniDnaHgMAvailableDlcis = _FrUniDnaHgMAvailableDlcis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 3, 11, 1, 5),
    _FrUniDnaHgMAvailableDlcis_Type()
)
frUniDnaHgMAvailableDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDnaHgMAvailableDlcis.setStatus("mandatory")
_FrUniDnaAddressTable_Object = MibTable
frUniDnaAddressTable = _FrUniDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 10)
)
if mibBuilder.loadTexts:
    frUniDnaAddressTable.setStatus("mandatory")
_FrUniDnaAddressEntry_Object = MibTableRow
frUniDnaAddressEntry = _FrUniDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 10, 1)
)
frUniDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaAddressEntry.setStatus("mandatory")


class _FrUniDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type frUniDnaNumberingPlanIndicator based on Integer32"""
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


_FrUniDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_FrUniDnaNumberingPlanIndicator_Object = MibTableColumn
frUniDnaNumberingPlanIndicator = _FrUniDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 10, 1, 1),
    _FrUniDnaNumberingPlanIndicator_Type()
)
frUniDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaNumberingPlanIndicator.setStatus("mandatory")


class _FrUniDnaDataNetworkAddress_Type(DigitString):
    """Custom type frUniDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrUniDnaDataNetworkAddress_Type.__name__ = "DigitString"
_FrUniDnaDataNetworkAddress_Object = MibTableColumn
frUniDnaDataNetworkAddress = _FrUniDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 10, 1, 2),
    _FrUniDnaDataNetworkAddress_Type()
)
frUniDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaDataNetworkAddress.setStatus("mandatory")
_FrUniDnaOutgoingOptionsTable_Object = MibTable
frUniDnaOutgoingOptionsTable = _FrUniDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11)
)
if mibBuilder.loadTexts:
    frUniDnaOutgoingOptionsTable.setStatus("mandatory")
_FrUniDnaOutgoingOptionsEntry_Object = MibTableRow
frUniDnaOutgoingOptionsEntry = _FrUniDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1)
)
frUniDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaOutgoingOptionsEntry.setStatus("mandatory")


class _FrUniDnaOutDefaultPriority_Type(Integer32):
    """Custom type frUniDnaOutDefaultPriority based on Integer32"""
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


_FrUniDnaOutDefaultPriority_Type.__name__ = "Integer32"
_FrUniDnaOutDefaultPriority_Object = MibTableColumn
frUniDnaOutDefaultPriority = _FrUniDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1, 7),
    _FrUniDnaOutDefaultPriority_Type()
)
frUniDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaOutDefaultPriority.setStatus("mandatory")


class _FrUniDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type frUniDnaOutDefaultPathSensitivity based on Integer32"""
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


_FrUniDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_FrUniDnaOutDefaultPathSensitivity_Object = MibTableColumn
frUniDnaOutDefaultPathSensitivity = _FrUniDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1, 11),
    _FrUniDnaOutDefaultPathSensitivity_Type()
)
frUniDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _FrUniDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type frUniDnaOutPathSensitivityOverRide based on Integer32"""
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


_FrUniDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_FrUniDnaOutPathSensitivityOverRide_Object = MibTableColumn
frUniDnaOutPathSensitivityOverRide = _FrUniDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1, 12),
    _FrUniDnaOutPathSensitivityOverRide_Type()
)
frUniDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _FrUniDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type frUniDnaOutDefaultPathReliability based on Integer32"""
    defaultValue = 1

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


_FrUniDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_FrUniDnaOutDefaultPathReliability_Object = MibTableColumn
frUniDnaOutDefaultPathReliability = _FrUniDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1, 14),
    _FrUniDnaOutDefaultPathReliability_Type()
)
frUniDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaOutDefaultPathReliability.setStatus("mandatory")


class _FrUniDnaOutAccess_Type(Integer32):
    """Custom type frUniDnaOutAccess based on Integer32"""
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


_FrUniDnaOutAccess_Type.__name__ = "Integer32"
_FrUniDnaOutAccess_Object = MibTableColumn
frUniDnaOutAccess = _FrUniDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1, 17),
    _FrUniDnaOutAccess_Type()
)
frUniDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaOutAccess.setStatus("mandatory")


class _FrUniDnaDefaultTransferPriority_Type(Integer32):
    """Custom type frUniDnaDefaultTransferPriority based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_FrUniDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_FrUniDnaDefaultTransferPriority_Object = MibTableColumn
frUniDnaDefaultTransferPriority = _FrUniDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1, 18),
    _FrUniDnaDefaultTransferPriority_Type()
)
frUniDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaDefaultTransferPriority.setStatus("mandatory")


class _FrUniDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type frUniDnaTransferPriorityOverRide based on Integer32"""
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


_FrUniDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_FrUniDnaTransferPriorityOverRide_Object = MibTableColumn
frUniDnaTransferPriorityOverRide = _FrUniDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 11, 1, 19),
    _FrUniDnaTransferPriorityOverRide_Type()
)
frUniDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaTransferPriorityOverRide.setStatus("mandatory")
_FrUniDnaIncomingOptionsTable_Object = MibTable
frUniDnaIncomingOptionsTable = _FrUniDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 12)
)
if mibBuilder.loadTexts:
    frUniDnaIncomingOptionsTable.setStatus("mandatory")
_FrUniDnaIncomingOptionsEntry_Object = MibTableRow
frUniDnaIncomingOptionsEntry = _FrUniDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 12, 1)
)
frUniDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaIncomingOptionsEntry.setStatus("mandatory")


class _FrUniDnaIncAccess_Type(Integer32):
    """Custom type frUniDnaIncAccess based on Integer32"""
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


_FrUniDnaIncAccess_Type.__name__ = "Integer32"
_FrUniDnaIncAccess_Object = MibTableColumn
frUniDnaIncAccess = _FrUniDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 12, 1, 9),
    _FrUniDnaIncAccess_Type()
)
frUniDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaIncAccess.setStatus("mandatory")
_FrUniDnaCallOptionsTable_Object = MibTable
frUniDnaCallOptionsTable = _FrUniDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 13)
)
if mibBuilder.loadTexts:
    frUniDnaCallOptionsTable.setStatus("mandatory")
_FrUniDnaCallOptionsEntry_Object = MibTableRow
frUniDnaCallOptionsEntry = _FrUniDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 13, 1)
)
frUniDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDnaIndex"),
)
if mibBuilder.loadTexts:
    frUniDnaCallOptionsEntry.setStatus("mandatory")


class _FrUniDnaAccountClass_Type(Unsigned32):
    """Custom type frUniDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniDnaAccountClass_Type.__name__ = "Unsigned32"
_FrUniDnaAccountClass_Object = MibTableColumn
frUniDnaAccountClass = _FrUniDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 13, 1, 10),
    _FrUniDnaAccountClass_Type()
)
frUniDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaAccountClass.setStatus("mandatory")


class _FrUniDnaAccountCollection_Type(OctetString):
    """Custom type frUniDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniDnaAccountCollection_Type.__name__ = "OctetString"
_FrUniDnaAccountCollection_Object = MibTableColumn
frUniDnaAccountCollection = _FrUniDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 13, 1, 11),
    _FrUniDnaAccountCollection_Type()
)
frUniDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaAccountCollection.setStatus("mandatory")


class _FrUniDnaServiceExchange_Type(Unsigned32):
    """Custom type frUniDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniDnaServiceExchange_Type.__name__ = "Unsigned32"
_FrUniDnaServiceExchange_Object = MibTableColumn
frUniDnaServiceExchange = _FrUniDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 13, 1, 12),
    _FrUniDnaServiceExchange_Type()
)
frUniDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaServiceExchange.setStatus("mandatory")


class _FrUniDnaEgressAccounting_Type(Integer32):
    """Custom type frUniDnaEgressAccounting based on Integer32"""
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


_FrUniDnaEgressAccounting_Type.__name__ = "Integer32"
_FrUniDnaEgressAccounting_Object = MibTableColumn
frUniDnaEgressAccounting = _FrUniDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 13, 1, 13),
    _FrUniDnaEgressAccounting_Type()
)
frUniDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaEgressAccounting.setStatus("mandatory")


class _FrUniDnaDataPath_Type(Integer32):
    """Custom type frUniDnaDataPath based on Integer32"""
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


_FrUniDnaDataPath_Type.__name__ = "Integer32"
_FrUniDnaDataPath_Object = MibTableColumn
frUniDnaDataPath = _FrUniDnaDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 2, 13, 1, 21),
    _FrUniDnaDataPath_Type()
)
frUniDnaDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDnaDataPath.setStatus("mandatory")
_FrUniFramer_ObjectIdentity = ObjectIdentity
frUniFramer = _FrUniFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3)
)
_FrUniFramerRowStatusTable_Object = MibTable
frUniFramerRowStatusTable = _FrUniFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 1)
)
if mibBuilder.loadTexts:
    frUniFramerRowStatusTable.setStatus("mandatory")
_FrUniFramerRowStatusEntry_Object = MibTableRow
frUniFramerRowStatusEntry = _FrUniFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 1, 1)
)
frUniFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniFramerRowStatusEntry.setStatus("mandatory")
_FrUniFramerRowStatus_Type = RowStatus
_FrUniFramerRowStatus_Object = MibTableColumn
frUniFramerRowStatus = _FrUniFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 1, 1, 1),
    _FrUniFramerRowStatus_Type()
)
frUniFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniFramerRowStatus.setStatus("mandatory")
_FrUniFramerComponentName_Type = DisplayString
_FrUniFramerComponentName_Object = MibTableColumn
frUniFramerComponentName = _FrUniFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 1, 1, 2),
    _FrUniFramerComponentName_Type()
)
frUniFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerComponentName.setStatus("mandatory")
_FrUniFramerStorageType_Type = StorageType
_FrUniFramerStorageType_Object = MibTableColumn
frUniFramerStorageType = _FrUniFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 1, 1, 4),
    _FrUniFramerStorageType_Type()
)
frUniFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerStorageType.setStatus("mandatory")
_FrUniFramerIndex_Type = NonReplicated
_FrUniFramerIndex_Object = MibTableColumn
frUniFramerIndex = _FrUniFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 1, 1, 10),
    _FrUniFramerIndex_Type()
)
frUniFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniFramerIndex.setStatus("mandatory")
_FrUniFramerProvTable_Object = MibTable
frUniFramerProvTable = _FrUniFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 10)
)
if mibBuilder.loadTexts:
    frUniFramerProvTable.setStatus("mandatory")
_FrUniFramerProvEntry_Object = MibTableRow
frUniFramerProvEntry = _FrUniFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 10, 1)
)
frUniFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniFramerProvEntry.setStatus("mandatory")
_FrUniFramerInterfaceName_Type = Link
_FrUniFramerInterfaceName_Object = MibTableColumn
frUniFramerInterfaceName = _FrUniFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 10, 1, 1),
    _FrUniFramerInterfaceName_Type()
)
frUniFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniFramerInterfaceName.setStatus("mandatory")
_FrUniFramerLinkTable_Object = MibTable
frUniFramerLinkTable = _FrUniFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 11)
)
if mibBuilder.loadTexts:
    frUniFramerLinkTable.setStatus("mandatory")
_FrUniFramerLinkEntry_Object = MibTableRow
frUniFramerLinkEntry = _FrUniFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 11, 1)
)
frUniFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniFramerLinkEntry.setStatus("mandatory")


class _FrUniFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type frUniFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FrUniFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_FrUniFramerFlagsBetweenFrames_Object = MibTableColumn
frUniFramerFlagsBetweenFrames = _FrUniFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 11, 1, 4),
    _FrUniFramerFlagsBetweenFrames_Type()
)
frUniFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniFramerFlagsBetweenFrames.setStatus("mandatory")
_FrUniFramerStateTable_Object = MibTable
frUniFramerStateTable = _FrUniFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 12)
)
if mibBuilder.loadTexts:
    frUniFramerStateTable.setStatus("mandatory")
_FrUniFramerStateEntry_Object = MibTableRow
frUniFramerStateEntry = _FrUniFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 12, 1)
)
frUniFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniFramerStateEntry.setStatus("mandatory")


class _FrUniFramerAdminState_Type(Integer32):
    """Custom type frUniFramerAdminState based on Integer32"""
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


_FrUniFramerAdminState_Type.__name__ = "Integer32"
_FrUniFramerAdminState_Object = MibTableColumn
frUniFramerAdminState = _FrUniFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 12, 1, 1),
    _FrUniFramerAdminState_Type()
)
frUniFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerAdminState.setStatus("mandatory")


class _FrUniFramerOperationalState_Type(Integer32):
    """Custom type frUniFramerOperationalState based on Integer32"""
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


_FrUniFramerOperationalState_Type.__name__ = "Integer32"
_FrUniFramerOperationalState_Object = MibTableColumn
frUniFramerOperationalState = _FrUniFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 12, 1, 2),
    _FrUniFramerOperationalState_Type()
)
frUniFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerOperationalState.setStatus("mandatory")


class _FrUniFramerUsageState_Type(Integer32):
    """Custom type frUniFramerUsageState based on Integer32"""
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


_FrUniFramerUsageState_Type.__name__ = "Integer32"
_FrUniFramerUsageState_Object = MibTableColumn
frUniFramerUsageState = _FrUniFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 12, 1, 3),
    _FrUniFramerUsageState_Type()
)
frUniFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerUsageState.setStatus("mandatory")
_FrUniFramerStatsTable_Object = MibTable
frUniFramerStatsTable = _FrUniFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13)
)
if mibBuilder.loadTexts:
    frUniFramerStatsTable.setStatus("mandatory")
_FrUniFramerStatsEntry_Object = MibTableRow
frUniFramerStatsEntry = _FrUniFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1)
)
frUniFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniFramerStatsEntry.setStatus("mandatory")
_FrUniFramerFrmToIf_Type = Counter32
_FrUniFramerFrmToIf_Object = MibTableColumn
frUniFramerFrmToIf = _FrUniFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 1),
    _FrUniFramerFrmToIf_Type()
)
frUniFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerFrmToIf.setStatus("mandatory")
_FrUniFramerFrmFromIf_Type = Counter32
_FrUniFramerFrmFromIf_Object = MibTableColumn
frUniFramerFrmFromIf = _FrUniFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 2),
    _FrUniFramerFrmFromIf_Type()
)
frUniFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerFrmFromIf.setStatus("mandatory")
_FrUniFramerOctetFromIf_Type = Counter32
_FrUniFramerOctetFromIf_Object = MibTableColumn
frUniFramerOctetFromIf = _FrUniFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 3),
    _FrUniFramerOctetFromIf_Type()
)
frUniFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerOctetFromIf.setStatus("mandatory")
_FrUniFramerAborts_Type = Counter32
_FrUniFramerAborts_Object = MibTableColumn
frUniFramerAborts = _FrUniFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 4),
    _FrUniFramerAborts_Type()
)
frUniFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerAborts.setStatus("mandatory")
_FrUniFramerCrcErrors_Type = Counter32
_FrUniFramerCrcErrors_Object = MibTableColumn
frUniFramerCrcErrors = _FrUniFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 5),
    _FrUniFramerCrcErrors_Type()
)
frUniFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerCrcErrors.setStatus("mandatory")
_FrUniFramerLrcErrors_Type = Counter32
_FrUniFramerLrcErrors_Object = MibTableColumn
frUniFramerLrcErrors = _FrUniFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 6),
    _FrUniFramerLrcErrors_Type()
)
frUniFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerLrcErrors.setStatus("mandatory")
_FrUniFramerNonOctetErrors_Type = Counter32
_FrUniFramerNonOctetErrors_Object = MibTableColumn
frUniFramerNonOctetErrors = _FrUniFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 7),
    _FrUniFramerNonOctetErrors_Type()
)
frUniFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerNonOctetErrors.setStatus("mandatory")
_FrUniFramerOverruns_Type = Counter32
_FrUniFramerOverruns_Object = MibTableColumn
frUniFramerOverruns = _FrUniFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 8),
    _FrUniFramerOverruns_Type()
)
frUniFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerOverruns.setStatus("mandatory")
_FrUniFramerUnderruns_Type = Counter32
_FrUniFramerUnderruns_Object = MibTableColumn
frUniFramerUnderruns = _FrUniFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 9),
    _FrUniFramerUnderruns_Type()
)
frUniFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerUnderruns.setStatus("mandatory")
_FrUniFramerLargeFrmErrors_Type = Counter32
_FrUniFramerLargeFrmErrors_Object = MibTableColumn
frUniFramerLargeFrmErrors = _FrUniFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 10),
    _FrUniFramerLargeFrmErrors_Type()
)
frUniFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerLargeFrmErrors.setStatus("mandatory")
_FrUniFramerFrmModeErrors_Type = Counter32
_FrUniFramerFrmModeErrors_Object = MibTableColumn
frUniFramerFrmModeErrors = _FrUniFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 13, 1, 11),
    _FrUniFramerFrmModeErrors_Type()
)
frUniFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerFrmModeErrors.setStatus("mandatory")
_FrUniFramerUtilTable_Object = MibTable
frUniFramerUtilTable = _FrUniFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 14)
)
if mibBuilder.loadTexts:
    frUniFramerUtilTable.setStatus("mandatory")
_FrUniFramerUtilEntry_Object = MibTableRow
frUniFramerUtilEntry = _FrUniFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 14, 1)
)
frUniFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniFramerUtilEntry.setStatus("mandatory")


class _FrUniFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type frUniFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrUniFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_FrUniFramerNormPrioLinkUtilToIf_Object = MibTableColumn
frUniFramerNormPrioLinkUtilToIf = _FrUniFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 14, 1, 1),
    _FrUniFramerNormPrioLinkUtilToIf_Type()
)
frUniFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _FrUniFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type frUniFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrUniFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_FrUniFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
frUniFramerNormPrioLinkUtilFromIf = _FrUniFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 3, 14, 1, 3),
    _FrUniFramerNormPrioLinkUtilFromIf_Type()
)
frUniFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_FrUniLmi_ObjectIdentity = ObjectIdentity
frUniLmi = _FrUniLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4)
)
_FrUniLmiRowStatusTable_Object = MibTable
frUniLmiRowStatusTable = _FrUniLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 1)
)
if mibBuilder.loadTexts:
    frUniLmiRowStatusTable.setStatus("mandatory")
_FrUniLmiRowStatusEntry_Object = MibTableRow
frUniLmiRowStatusEntry = _FrUniLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 1, 1)
)
frUniLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLmiIndex"),
)
if mibBuilder.loadTexts:
    frUniLmiRowStatusEntry.setStatus("mandatory")
_FrUniLmiRowStatus_Type = RowStatus
_FrUniLmiRowStatus_Object = MibTableColumn
frUniLmiRowStatus = _FrUniLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 1, 1, 1),
    _FrUniLmiRowStatus_Type()
)
frUniLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiRowStatus.setStatus("mandatory")
_FrUniLmiComponentName_Type = DisplayString
_FrUniLmiComponentName_Object = MibTableColumn
frUniLmiComponentName = _FrUniLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 1, 1, 2),
    _FrUniLmiComponentName_Type()
)
frUniLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiComponentName.setStatus("mandatory")
_FrUniLmiStorageType_Type = StorageType
_FrUniLmiStorageType_Object = MibTableColumn
frUniLmiStorageType = _FrUniLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 1, 1, 4),
    _FrUniLmiStorageType_Type()
)
frUniLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiStorageType.setStatus("mandatory")
_FrUniLmiIndex_Type = NonReplicated
_FrUniLmiIndex_Object = MibTableColumn
frUniLmiIndex = _FrUniLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 1, 1, 10),
    _FrUniLmiIndex_Type()
)
frUniLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniLmiIndex.setStatus("mandatory")
_FrUniLmiParmsTable_Object = MibTable
frUniLmiParmsTable = _FrUniLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10)
)
if mibBuilder.loadTexts:
    frUniLmiParmsTable.setStatus("mandatory")
_FrUniLmiParmsEntry_Object = MibTableRow
frUniLmiParmsEntry = _FrUniLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1)
)
frUniLmiParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLmiIndex"),
)
if mibBuilder.loadTexts:
    frUniLmiParmsEntry.setStatus("mandatory")


class _FrUniLmiProcedures_Type(Integer32):
    """Custom type frUniLmiProcedures based on Integer32"""
    defaultValue = 4

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
        *(("ansi", 2),
          ("autoConfigure", 4),
          ("itu", 3),
          ("none", 0),
          ("vendorForum", 1))
    )


_FrUniLmiProcedures_Type.__name__ = "Integer32"
_FrUniLmiProcedures_Object = MibTableColumn
frUniLmiProcedures = _FrUniLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 1),
    _FrUniLmiProcedures_Type()
)
frUniLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiProcedures.setStatus("mandatory")


class _FrUniLmiAsyncStatusReport_Type(Integer32):
    """Custom type frUniLmiAsyncStatusReport based on Integer32"""
    defaultValue = 0

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


_FrUniLmiAsyncStatusReport_Type.__name__ = "Integer32"
_FrUniLmiAsyncStatusReport_Object = MibTableColumn
frUniLmiAsyncStatusReport = _FrUniLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 2),
    _FrUniLmiAsyncStatusReport_Type()
)
frUniLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiAsyncStatusReport.setStatus("mandatory")


class _FrUniLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type frUniLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrUniLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_FrUniLmiErrorEventThreshold_Object = MibTableColumn
frUniLmiErrorEventThreshold = _FrUniLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 3),
    _FrUniLmiErrorEventThreshold_Type()
)
frUniLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiErrorEventThreshold.setStatus("mandatory")


class _FrUniLmiEventCount_Type(Unsigned32):
    """Custom type frUniLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrUniLmiEventCount_Type.__name__ = "Unsigned32"
_FrUniLmiEventCount_Object = MibTableColumn
frUniLmiEventCount = _FrUniLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 4),
    _FrUniLmiEventCount_Type()
)
frUniLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiEventCount.setStatus("mandatory")


class _FrUniLmiCheckPointTimer_Type(Unsigned32):
    """Custom type frUniLmiCheckPointTimer based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrUniLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_FrUniLmiCheckPointTimer_Object = MibTableColumn
frUniLmiCheckPointTimer = _FrUniLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 5),
    _FrUniLmiCheckPointTimer_Type()
)
frUniLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiCheckPointTimer.setStatus("mandatory")


class _FrUniLmiMessageCountTimer_Type(Unsigned32):
    """Custom type frUniLmiMessageCountTimer based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrUniLmiMessageCountTimer_Type.__name__ = "Unsigned32"
_FrUniLmiMessageCountTimer_Object = MibTableColumn
frUniLmiMessageCountTimer = _FrUniLmiMessageCountTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 6),
    _FrUniLmiMessageCountTimer_Type()
)
frUniLmiMessageCountTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiMessageCountTimer.setStatus("mandatory")


class _FrUniLmiIgnoreActiveBit_Type(Integer32):
    """Custom type frUniLmiIgnoreActiveBit based on Integer32"""
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


_FrUniLmiIgnoreActiveBit_Type.__name__ = "Integer32"
_FrUniLmiIgnoreActiveBit_Object = MibTableColumn
frUniLmiIgnoreActiveBit = _FrUniLmiIgnoreActiveBit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 7),
    _FrUniLmiIgnoreActiveBit_Type()
)
frUniLmiIgnoreActiveBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiIgnoreActiveBit.setStatus("mandatory")


class _FrUniLmiSide_Type(Integer32):
    """Custom type frUniLmiSide based on Integer32"""
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
        *(("both", 2),
          ("network", 0),
          ("user", 1))
    )


_FrUniLmiSide_Type.__name__ = "Integer32"
_FrUniLmiSide_Object = MibTableColumn
frUniLmiSide = _FrUniLmiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 8),
    _FrUniLmiSide_Type()
)
frUniLmiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiSide.setStatus("mandatory")


class _FrUniLmiPvcConfigParmsInFsr_Type(Integer32):
    """Custom type frUniLmiPvcConfigParmsInFsr based on Integer32"""
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


_FrUniLmiPvcConfigParmsInFsr_Type.__name__ = "Integer32"
_FrUniLmiPvcConfigParmsInFsr_Object = MibTableColumn
frUniLmiPvcConfigParmsInFsr = _FrUniLmiPvcConfigParmsInFsr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 10, 1, 9),
    _FrUniLmiPvcConfigParmsInFsr_Type()
)
frUniLmiPvcConfigParmsInFsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiPvcConfigParmsInFsr.setStatus("mandatory")
_FrUniLmiStateTable_Object = MibTable
frUniLmiStateTable = _FrUniLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 11)
)
if mibBuilder.loadTexts:
    frUniLmiStateTable.setStatus("mandatory")
_FrUniLmiStateEntry_Object = MibTableRow
frUniLmiStateEntry = _FrUniLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 11, 1)
)
frUniLmiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLmiIndex"),
)
if mibBuilder.loadTexts:
    frUniLmiStateEntry.setStatus("mandatory")


class _FrUniLmiAdminState_Type(Integer32):
    """Custom type frUniLmiAdminState based on Integer32"""
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


_FrUniLmiAdminState_Type.__name__ = "Integer32"
_FrUniLmiAdminState_Object = MibTableColumn
frUniLmiAdminState = _FrUniLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 11, 1, 1),
    _FrUniLmiAdminState_Type()
)
frUniLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiAdminState.setStatus("mandatory")


class _FrUniLmiOperationalState_Type(Integer32):
    """Custom type frUniLmiOperationalState based on Integer32"""
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


_FrUniLmiOperationalState_Type.__name__ = "Integer32"
_FrUniLmiOperationalState_Object = MibTableColumn
frUniLmiOperationalState = _FrUniLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 11, 1, 2),
    _FrUniLmiOperationalState_Type()
)
frUniLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiOperationalState.setStatus("mandatory")


class _FrUniLmiUsageState_Type(Integer32):
    """Custom type frUniLmiUsageState based on Integer32"""
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


_FrUniLmiUsageState_Type.__name__ = "Integer32"
_FrUniLmiUsageState_Object = MibTableColumn
frUniLmiUsageState = _FrUniLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 11, 1, 3),
    _FrUniLmiUsageState_Type()
)
frUniLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiUsageState.setStatus("mandatory")
_FrUniLmiPsiTable_Object = MibTable
frUniLmiPsiTable = _FrUniLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 12)
)
if mibBuilder.loadTexts:
    frUniLmiPsiTable.setStatus("mandatory")
_FrUniLmiPsiEntry_Object = MibTableRow
frUniLmiPsiEntry = _FrUniLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 12, 1)
)
frUniLmiPsiEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLmiIndex"),
)
if mibBuilder.loadTexts:
    frUniLmiPsiEntry.setStatus("mandatory")


class _FrUniLmiProtocolStatus_Type(Integer32):
    """Custom type frUniLmiProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuring", 2),
          ("errorCondition", 0),
          ("normalCondition", 1))
    )


_FrUniLmiProtocolStatus_Type.__name__ = "Integer32"
_FrUniLmiProtocolStatus_Object = MibTableColumn
frUniLmiProtocolStatus = _FrUniLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 12, 1, 1),
    _FrUniLmiProtocolStatus_Type()
)
frUniLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiProtocolStatus.setStatus("mandatory")


class _FrUniLmiOpProcedures_Type(Integer32):
    """Custom type frUniLmiOpProcedures based on Integer32"""
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
        *(("ansi", 2),
          ("itu", 3),
          ("none", 0),
          ("unknown", 4),
          ("vendorForum", 1))
    )


_FrUniLmiOpProcedures_Type.__name__ = "Integer32"
_FrUniLmiOpProcedures_Object = MibTableColumn
frUniLmiOpProcedures = _FrUniLmiOpProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 12, 1, 2),
    _FrUniLmiOpProcedures_Type()
)
frUniLmiOpProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiOpProcedures.setStatus("mandatory")
_FrUniLmiStatsTable_Object = MibTable
frUniLmiStatsTable = _FrUniLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13)
)
if mibBuilder.loadTexts:
    frUniLmiStatsTable.setStatus("mandatory")
_FrUniLmiStatsEntry_Object = MibTableRow
frUniLmiStatsEntry = _FrUniLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1)
)
frUniLmiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLmiIndex"),
)
if mibBuilder.loadTexts:
    frUniLmiStatsEntry.setStatus("mandatory")
_FrUniLmiKeepAliveStatusToIf_Type = Counter32
_FrUniLmiKeepAliveStatusToIf_Object = MibTableColumn
frUniLmiKeepAliveStatusToIf = _FrUniLmiKeepAliveStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 1),
    _FrUniLmiKeepAliveStatusToIf_Type()
)
frUniLmiKeepAliveStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiKeepAliveStatusToIf.setStatus("mandatory")
_FrUniLmiFullStatusToIf_Type = Counter32
_FrUniLmiFullStatusToIf_Object = MibTableColumn
frUniLmiFullStatusToIf = _FrUniLmiFullStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 2),
    _FrUniLmiFullStatusToIf_Type()
)
frUniLmiFullStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiFullStatusToIf.setStatus("mandatory")
_FrUniLmiKeepAliveStatusEnqFromIf_Type = Counter32
_FrUniLmiKeepAliveStatusEnqFromIf_Object = MibTableColumn
frUniLmiKeepAliveStatusEnqFromIf = _FrUniLmiKeepAliveStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 3),
    _FrUniLmiKeepAliveStatusEnqFromIf_Type()
)
frUniLmiKeepAliveStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiKeepAliveStatusEnqFromIf.setStatus("mandatory")
_FrUniLmiFullStatusEnqFromIf_Type = Counter32
_FrUniLmiFullStatusEnqFromIf_Object = MibTableColumn
frUniLmiFullStatusEnqFromIf = _FrUniLmiFullStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 4),
    _FrUniLmiFullStatusEnqFromIf_Type()
)
frUniLmiFullStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiFullStatusEnqFromIf.setStatus("mandatory")


class _FrUniLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type frUniLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrUniLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_FrUniLmiNetworkSideEventHistory_Object = MibTableColumn
frUniLmiNetworkSideEventHistory = _FrUniLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 5),
    _FrUniLmiNetworkSideEventHistory_Type()
)
frUniLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiNetworkSideEventHistory.setStatus("mandatory")
_FrUniLmiProtocolErrors_Type = Counter32
_FrUniLmiProtocolErrors_Object = MibTableColumn
frUniLmiProtocolErrors = _FrUniLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 6),
    _FrUniLmiProtocolErrors_Type()
)
frUniLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiProtocolErrors.setStatus("mandatory")
_FrUniLmiUnexpectedIes_Type = Counter32
_FrUniLmiUnexpectedIes_Object = MibTableColumn
frUniLmiUnexpectedIes = _FrUniLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 7),
    _FrUniLmiUnexpectedIes_Type()
)
frUniLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiUnexpectedIes.setStatus("mandatory")
_FrUniLmiSequenceErrors_Type = Counter32
_FrUniLmiSequenceErrors_Object = MibTableColumn
frUniLmiSequenceErrors = _FrUniLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 8),
    _FrUniLmiSequenceErrors_Type()
)
frUniLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiSequenceErrors.setStatus("mandatory")
_FrUniLmiUnexpectedReports_Type = Counter32
_FrUniLmiUnexpectedReports_Object = MibTableColumn
frUniLmiUnexpectedReports = _FrUniLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 9),
    _FrUniLmiUnexpectedReports_Type()
)
frUniLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiUnexpectedReports.setStatus("mandatory")
_FrUniLmiPollingVerifTimeouts_Type = Counter32
_FrUniLmiPollingVerifTimeouts_Object = MibTableColumn
frUniLmiPollingVerifTimeouts = _FrUniLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 10),
    _FrUniLmiPollingVerifTimeouts_Type()
)
frUniLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiPollingVerifTimeouts.setStatus("mandatory")
_FrUniLmiKeepAliveEnqToIf_Type = Counter32
_FrUniLmiKeepAliveEnqToIf_Object = MibTableColumn
frUniLmiKeepAliveEnqToIf = _FrUniLmiKeepAliveEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 11),
    _FrUniLmiKeepAliveEnqToIf_Type()
)
frUniLmiKeepAliveEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiKeepAliveEnqToIf.setStatus("mandatory")
_FrUniLmiFullStatusEnqToIf_Type = Counter32
_FrUniLmiFullStatusEnqToIf_Object = MibTableColumn
frUniLmiFullStatusEnqToIf = _FrUniLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 12),
    _FrUniLmiFullStatusEnqToIf_Type()
)
frUniLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiFullStatusEnqToIf.setStatus("mandatory")


class _FrUniLmiUserSideEventHistory_Type(AsciiString):
    """Custom type frUniLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrUniLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_FrUniLmiUserSideEventHistory_Object = MibTableColumn
frUniLmiUserSideEventHistory = _FrUniLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 13),
    _FrUniLmiUserSideEventHistory_Type()
)
frUniLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiUserSideEventHistory.setStatus("mandatory")
_FrUniLmiStatusSequenceErrors_Type = Counter32
_FrUniLmiStatusSequenceErrors_Object = MibTableColumn
frUniLmiStatusSequenceErrors = _FrUniLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 14),
    _FrUniLmiStatusSequenceErrors_Type()
)
frUniLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiStatusSequenceErrors.setStatus("mandatory")
_FrUniLmiNoStatusReportCount_Type = Counter32
_FrUniLmiNoStatusReportCount_Object = MibTableColumn
frUniLmiNoStatusReportCount = _FrUniLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 13, 1, 15),
    _FrUniLmiNoStatusReportCount_Type()
)
frUniLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLmiNoStatusReportCount.setStatus("mandatory")
_FrUniLmiUspParmsTable_Object = MibTable
frUniLmiUspParmsTable = _FrUniLmiUspParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 14)
)
if mibBuilder.loadTexts:
    frUniLmiUspParmsTable.setStatus("mandatory")
_FrUniLmiUspParmsEntry_Object = MibTableRow
frUniLmiUspParmsEntry = _FrUniLmiUspParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 14, 1)
)
frUniLmiUspParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLmiIndex"),
)
if mibBuilder.loadTexts:
    frUniLmiUspParmsEntry.setStatus("mandatory")


class _FrUniLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type frUniLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrUniLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_FrUniLmiFullStatusPollingCycles_Object = MibTableColumn
frUniLmiFullStatusPollingCycles = _FrUniLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 14, 1, 1),
    _FrUniLmiFullStatusPollingCycles_Type()
)
frUniLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiFullStatusPollingCycles.setStatus("mandatory")


class _FrUniLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type frUniLmiLinkVerificationTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
    )


_FrUniLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_FrUniLmiLinkVerificationTimer_Object = MibTableColumn
frUniLmiLinkVerificationTimer = _FrUniLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 4, 14, 1, 2),
    _FrUniLmiLinkVerificationTimer_Type()
)
frUniLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLmiLinkVerificationTimer.setStatus("mandatory")
_FrUniDlci_ObjectIdentity = ObjectIdentity
frUniDlci = _FrUniDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5)
)
_FrUniDlciRowStatusTable_Object = MibTable
frUniDlciRowStatusTable = _FrUniDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 1)
)
if mibBuilder.loadTexts:
    frUniDlciRowStatusTable.setStatus("mandatory")
_FrUniDlciRowStatusEntry_Object = MibTableRow
frUniDlciRowStatusEntry = _FrUniDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 1, 1)
)
frUniDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciRowStatusEntry.setStatus("mandatory")
_FrUniDlciRowStatus_Type = RowStatus
_FrUniDlciRowStatus_Object = MibTableColumn
frUniDlciRowStatus = _FrUniDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 1, 1, 1),
    _FrUniDlciRowStatus_Type()
)
frUniDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciRowStatus.setStatus("mandatory")
_FrUniDlciComponentName_Type = DisplayString
_FrUniDlciComponentName_Object = MibTableColumn
frUniDlciComponentName = _FrUniDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 1, 1, 2),
    _FrUniDlciComponentName_Type()
)
frUniDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciComponentName.setStatus("mandatory")
_FrUniDlciStorageType_Type = StorageType
_FrUniDlciStorageType_Object = MibTableColumn
frUniDlciStorageType = _FrUniDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 1, 1, 4),
    _FrUniDlciStorageType_Type()
)
frUniDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciStorageType.setStatus("mandatory")


class _FrUniDlciIndex_Type(Integer32):
    """Custom type frUniDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrUniDlciIndex_Type.__name__ = "Integer32"
_FrUniDlciIndex_Object = MibTableColumn
frUniDlciIndex = _FrUniDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 1, 1, 10),
    _FrUniDlciIndex_Type()
)
frUniDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDlciIndex.setStatus("mandatory")
_FrUniDlciDc_ObjectIdentity = ObjectIdentity
frUniDlciDc = _FrUniDlciDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2)
)
_FrUniDlciDcRowStatusTable_Object = MibTable
frUniDlciDcRowStatusTable = _FrUniDlciDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 1)
)
if mibBuilder.loadTexts:
    frUniDlciDcRowStatusTable.setStatus("mandatory")
_FrUniDlciDcRowStatusEntry_Object = MibTableRow
frUniDlciDcRowStatusEntry = _FrUniDlciDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 1, 1)
)
frUniDlciDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciDcRowStatusEntry.setStatus("mandatory")
_FrUniDlciDcRowStatus_Type = RowStatus
_FrUniDlciDcRowStatus_Object = MibTableColumn
frUniDlciDcRowStatus = _FrUniDlciDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 1, 1, 1),
    _FrUniDlciDcRowStatus_Type()
)
frUniDlciDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDcRowStatus.setStatus("mandatory")
_FrUniDlciDcComponentName_Type = DisplayString
_FrUniDlciDcComponentName_Object = MibTableColumn
frUniDlciDcComponentName = _FrUniDlciDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 1, 1, 2),
    _FrUniDlciDcComponentName_Type()
)
frUniDlciDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDcComponentName.setStatus("mandatory")
_FrUniDlciDcStorageType_Type = StorageType
_FrUniDlciDcStorageType_Object = MibTableColumn
frUniDlciDcStorageType = _FrUniDlciDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 1, 1, 4),
    _FrUniDlciDcStorageType_Type()
)
frUniDlciDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDcStorageType.setStatus("mandatory")
_FrUniDlciDcIndex_Type = NonReplicated
_FrUniDlciDcIndex_Object = MibTableColumn
frUniDlciDcIndex = _FrUniDlciDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 1, 1, 10),
    _FrUniDlciDcIndex_Type()
)
frUniDlciDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDlciDcIndex.setStatus("mandatory")
_FrUniDlciDcOptionsTable_Object = MibTable
frUniDlciDcOptionsTable = _FrUniDlciDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10)
)
if mibBuilder.loadTexts:
    frUniDlciDcOptionsTable.setStatus("mandatory")
_FrUniDlciDcOptionsEntry_Object = MibTableRow
frUniDlciDcOptionsEntry = _FrUniDlciDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1)
)
frUniDlciDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciDcOptionsEntry.setStatus("mandatory")


class _FrUniDlciDcRemoteNpi_Type(Integer32):
    """Custom type frUniDlciDcRemoteNpi based on Integer32"""
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


_FrUniDlciDcRemoteNpi_Type.__name__ = "Integer32"
_FrUniDlciDcRemoteNpi_Object = MibTableColumn
frUniDlciDcRemoteNpi = _FrUniDlciDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 3),
    _FrUniDlciDcRemoteNpi_Type()
)
frUniDlciDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcRemoteNpi.setStatus("mandatory")


class _FrUniDlciDcRemoteDna_Type(DigitString):
    """Custom type frUniDlciDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrUniDlciDcRemoteDna_Type.__name__ = "DigitString"
_FrUniDlciDcRemoteDna_Object = MibTableColumn
frUniDlciDcRemoteDna = _FrUniDlciDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 4),
    _FrUniDlciDcRemoteDna_Type()
)
frUniDlciDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcRemoteDna.setStatus("mandatory")


class _FrUniDlciDcRemoteDlci_Type(Unsigned32):
    """Custom type frUniDlciDcRemoteDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrUniDlciDcRemoteDlci_Type.__name__ = "Unsigned32"
_FrUniDlciDcRemoteDlci_Object = MibTableColumn
frUniDlciDcRemoteDlci = _FrUniDlciDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 5),
    _FrUniDlciDcRemoteDlci_Type()
)
frUniDlciDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcRemoteDlci.setStatus("mandatory")


class _FrUniDlciDcType_Type(Integer32):
    """Custom type frUniDlciDcType based on Integer32"""
    defaultValue = 1

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
        *(("permanentBackupSlave", 3),
          ("permanentMaster", 1),
          ("permanentSlave", 2),
          ("permanentSlaveWithBackup", 4))
    )


_FrUniDlciDcType_Type.__name__ = "Integer32"
_FrUniDlciDcType_Object = MibTableColumn
frUniDlciDcType = _FrUniDlciDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 6),
    _FrUniDlciDcType_Type()
)
frUniDlciDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcType.setStatus("mandatory")


class _FrUniDlciDcTransferPriority_Type(Integer32):
    """Custom type frUniDlciDcTransferPriority based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("useDnaDefTP", 255))
    )


_FrUniDlciDcTransferPriority_Type.__name__ = "Integer32"
_FrUniDlciDcTransferPriority_Object = MibTableColumn
frUniDlciDcTransferPriority = _FrUniDlciDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 9),
    _FrUniDlciDcTransferPriority_Type()
)
frUniDlciDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcTransferPriority.setStatus("mandatory")


class _FrUniDlciDcDiscardPriority_Type(Integer32):
    """Custom type frUniDlciDcDiscardPriority based on Integer32"""
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


_FrUniDlciDcDiscardPriority_Type.__name__ = "Integer32"
_FrUniDlciDcDiscardPriority_Object = MibTableColumn
frUniDlciDcDiscardPriority = _FrUniDlciDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 10),
    _FrUniDlciDcDiscardPriority_Type()
)
frUniDlciDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcDiscardPriority.setStatus("mandatory")


class _FrUniDlciDcDeDiscardPriority_Type(Integer32):
    """Custom type frUniDlciDcDeDiscardPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("determinedByDiscardPriority", 1),
          ("lowest", 0))
    )


_FrUniDlciDcDeDiscardPriority_Type.__name__ = "Integer32"
_FrUniDlciDcDeDiscardPriority_Object = MibTableColumn
frUniDlciDcDeDiscardPriority = _FrUniDlciDcDeDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 11),
    _FrUniDlciDcDeDiscardPriority_Type()
)
frUniDlciDcDeDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcDeDiscardPriority.setStatus("mandatory")


class _FrUniDlciDcDataPath_Type(Integer32):
    """Custom type frUniDlciDcDataPath based on Integer32"""
    defaultValue = 3

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


_FrUniDlciDcDataPath_Type.__name__ = "Integer32"
_FrUniDlciDcDataPath_Object = MibTableColumn
frUniDlciDcDataPath = _FrUniDlciDcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 12),
    _FrUniDlciDcDataPath_Type()
)
frUniDlciDcDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcDataPath.setStatus("mandatory")


class _FrUniDlciDcCugIndex_Type(Unsigned32):
    """Custom type frUniDlciDcCugIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniDlciDcCugIndex_Type.__name__ = "Unsigned32"
_FrUniDlciDcCugIndex_Object = MibTableColumn
frUniDlciDcCugIndex = _FrUniDlciDcCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 13),
    _FrUniDlciDcCugIndex_Type()
)
frUniDlciDcCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcCugIndex.setStatus("mandatory")


class _FrUniDlciDcCugType_Type(Integer32):
    """Custom type frUniDlciDcCugType based on Integer32"""
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


_FrUniDlciDcCugType_Type.__name__ = "Integer32"
_FrUniDlciDcCugType_Object = MibTableColumn
frUniDlciDcCugType = _FrUniDlciDcCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 10, 1, 14),
    _FrUniDlciDcCugType_Type()
)
frUniDlciDcCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcCugType.setStatus("mandatory")
_FrUniDlciDcNfaTable_Object = MibTable
frUniDlciDcNfaTable = _FrUniDlciDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 202)
)
if mibBuilder.loadTexts:
    frUniDlciDcNfaTable.setStatus("obsolete")
_FrUniDlciDcNfaEntry_Object = MibTableRow
frUniDlciDcNfaEntry = _FrUniDlciDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 202, 1)
)
frUniDlciDcNfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciDcIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciDcNfaIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciDcNfaEntry.setStatus("obsolete")


class _FrUniDlciDcNfaIndex_Type(Integer32):
    """Custom type frUniDlciDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
    )


_FrUniDlciDcNfaIndex_Type.__name__ = "Integer32"
_FrUniDlciDcNfaIndex_Object = MibTableColumn
frUniDlciDcNfaIndex = _FrUniDlciDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 202, 1, 1),
    _FrUniDlciDcNfaIndex_Type()
)
frUniDlciDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDlciDcNfaIndex.setStatus("obsolete")


class _FrUniDlciDcNfaValue_Type(HexString):
    """Custom type frUniDlciDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FrUniDlciDcNfaValue_Type.__name__ = "HexString"
_FrUniDlciDcNfaValue_Object = MibTableColumn
frUniDlciDcNfaValue = _FrUniDlciDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 202, 1, 2),
    _FrUniDlciDcNfaValue_Type()
)
frUniDlciDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciDcNfaValue.setStatus("obsolete")
_FrUniDlciDcNfaRowStatus_Type = RowStatus
_FrUniDlciDcNfaRowStatus_Object = MibTableColumn
frUniDlciDcNfaRowStatus = _FrUniDlciDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 2, 202, 1, 3),
    _FrUniDlciDcNfaRowStatus_Type()
)
frUniDlciDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frUniDlciDcNfaRowStatus.setStatus("obsolete")
_FrUniDlciVc_ObjectIdentity = ObjectIdentity
frUniDlciVc = _FrUniDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3)
)
_FrUniDlciVcRowStatusTable_Object = MibTable
frUniDlciVcRowStatusTable = _FrUniDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 1)
)
if mibBuilder.loadTexts:
    frUniDlciVcRowStatusTable.setStatus("mandatory")
_FrUniDlciVcRowStatusEntry_Object = MibTableRow
frUniDlciVcRowStatusEntry = _FrUniDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 1, 1)
)
frUniDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciVcRowStatusEntry.setStatus("mandatory")
_FrUniDlciVcRowStatus_Type = RowStatus
_FrUniDlciVcRowStatus_Object = MibTableColumn
frUniDlciVcRowStatus = _FrUniDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 1, 1, 1),
    _FrUniDlciVcRowStatus_Type()
)
frUniDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcRowStatus.setStatus("mandatory")
_FrUniDlciVcComponentName_Type = DisplayString
_FrUniDlciVcComponentName_Object = MibTableColumn
frUniDlciVcComponentName = _FrUniDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 1, 1, 2),
    _FrUniDlciVcComponentName_Type()
)
frUniDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcComponentName.setStatus("mandatory")
_FrUniDlciVcStorageType_Type = StorageType
_FrUniDlciVcStorageType_Object = MibTableColumn
frUniDlciVcStorageType = _FrUniDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 1, 1, 4),
    _FrUniDlciVcStorageType_Type()
)
frUniDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcStorageType.setStatus("mandatory")
_FrUniDlciVcIndex_Type = NonReplicated
_FrUniDlciVcIndex_Object = MibTableColumn
frUniDlciVcIndex = _FrUniDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 1, 1, 10),
    _FrUniDlciVcIndex_Type()
)
frUniDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDlciVcIndex.setStatus("mandatory")
_FrUniDlciVcCadTable_Object = MibTable
frUniDlciVcCadTable = _FrUniDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10)
)
if mibBuilder.loadTexts:
    frUniDlciVcCadTable.setStatus("mandatory")
_FrUniDlciVcCadEntry_Object = MibTableRow
frUniDlciVcCadEntry = _FrUniDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1)
)
frUniDlciVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciVcCadEntry.setStatus("mandatory")


class _FrUniDlciVcType_Type(Integer32):
    """Custom type frUniDlciVcType based on Integer32"""
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


_FrUniDlciVcType_Type.__name__ = "Integer32"
_FrUniDlciVcType_Object = MibTableColumn
frUniDlciVcType = _FrUniDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 1),
    _FrUniDlciVcType_Type()
)
frUniDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcType.setStatus("mandatory")


class _FrUniDlciVcState_Type(Integer32):
    """Custom type frUniDlciVcState based on Integer32"""
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


_FrUniDlciVcState_Type.__name__ = "Integer32"
_FrUniDlciVcState_Object = MibTableColumn
frUniDlciVcState = _FrUniDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 2),
    _FrUniDlciVcState_Type()
)
frUniDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcState.setStatus("mandatory")


class _FrUniDlciVcPreviousState_Type(Integer32):
    """Custom type frUniDlciVcPreviousState based on Integer32"""
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


_FrUniDlciVcPreviousState_Type.__name__ = "Integer32"
_FrUniDlciVcPreviousState_Object = MibTableColumn
frUniDlciVcPreviousState = _FrUniDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 3),
    _FrUniDlciVcPreviousState_Type()
)
frUniDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPreviousState.setStatus("mandatory")


class _FrUniDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type frUniDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_FrUniDlciVcDiagnosticCode_Object = MibTableColumn
frUniDlciVcDiagnosticCode = _FrUniDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 4),
    _FrUniDlciVcDiagnosticCode_Type()
)
frUniDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcDiagnosticCode.setStatus("mandatory")


class _FrUniDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type frUniDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_FrUniDlciVcPreviousDiagnosticCode_Object = MibTableColumn
frUniDlciVcPreviousDiagnosticCode = _FrUniDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 5),
    _FrUniDlciVcPreviousDiagnosticCode_Type()
)
frUniDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _FrUniDlciVcCalledNpi_Type(Integer32):
    """Custom type frUniDlciVcCalledNpi based on Integer32"""
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


_FrUniDlciVcCalledNpi_Type.__name__ = "Integer32"
_FrUniDlciVcCalledNpi_Object = MibTableColumn
frUniDlciVcCalledNpi = _FrUniDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 6),
    _FrUniDlciVcCalledNpi_Type()
)
frUniDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCalledNpi.setStatus("mandatory")


class _FrUniDlciVcCalledDna_Type(DigitString):
    """Custom type frUniDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrUniDlciVcCalledDna_Type.__name__ = "DigitString"
_FrUniDlciVcCalledDna_Object = MibTableColumn
frUniDlciVcCalledDna = _FrUniDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 7),
    _FrUniDlciVcCalledDna_Type()
)
frUniDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCalledDna.setStatus("mandatory")


class _FrUniDlciVcCalledLcn_Type(Unsigned32):
    """Custom type frUniDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrUniDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_FrUniDlciVcCalledLcn_Object = MibTableColumn
frUniDlciVcCalledLcn = _FrUniDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 8),
    _FrUniDlciVcCalledLcn_Type()
)
frUniDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCalledLcn.setStatus("mandatory")


class _FrUniDlciVcCallingNpi_Type(Integer32):
    """Custom type frUniDlciVcCallingNpi based on Integer32"""
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


_FrUniDlciVcCallingNpi_Type.__name__ = "Integer32"
_FrUniDlciVcCallingNpi_Object = MibTableColumn
frUniDlciVcCallingNpi = _FrUniDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 9),
    _FrUniDlciVcCallingNpi_Type()
)
frUniDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCallingNpi.setStatus("mandatory")


class _FrUniDlciVcCallingDna_Type(DigitString):
    """Custom type frUniDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrUniDlciVcCallingDna_Type.__name__ = "DigitString"
_FrUniDlciVcCallingDna_Object = MibTableColumn
frUniDlciVcCallingDna = _FrUniDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 10),
    _FrUniDlciVcCallingDna_Type()
)
frUniDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCallingDna.setStatus("mandatory")


class _FrUniDlciVcCallingLcn_Type(Unsigned32):
    """Custom type frUniDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrUniDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_FrUniDlciVcCallingLcn_Object = MibTableColumn
frUniDlciVcCallingLcn = _FrUniDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 11),
    _FrUniDlciVcCallingLcn_Type()
)
frUniDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCallingLcn.setStatus("mandatory")


class _FrUniDlciVcAccountingEnabled_Type(Integer32):
    """Custom type frUniDlciVcAccountingEnabled based on Integer32"""
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


_FrUniDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_FrUniDlciVcAccountingEnabled_Object = MibTableColumn
frUniDlciVcAccountingEnabled = _FrUniDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 12),
    _FrUniDlciVcAccountingEnabled_Type()
)
frUniDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcAccountingEnabled.setStatus("mandatory")


class _FrUniDlciVcFastSelectCall_Type(Integer32):
    """Custom type frUniDlciVcFastSelectCall based on Integer32"""
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


_FrUniDlciVcFastSelectCall_Type.__name__ = "Integer32"
_FrUniDlciVcFastSelectCall_Object = MibTableColumn
frUniDlciVcFastSelectCall = _FrUniDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 13),
    _FrUniDlciVcFastSelectCall_Type()
)
frUniDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcFastSelectCall.setStatus("mandatory")


class _FrUniDlciVcPathReliability_Type(Integer32):
    """Custom type frUniDlciVcPathReliability based on Integer32"""
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


_FrUniDlciVcPathReliability_Type.__name__ = "Integer32"
_FrUniDlciVcPathReliability_Object = MibTableColumn
frUniDlciVcPathReliability = _FrUniDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 19),
    _FrUniDlciVcPathReliability_Type()
)
frUniDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPathReliability.setStatus("mandatory")


class _FrUniDlciVcAccountingEnd_Type(Integer32):
    """Custom type frUniDlciVcAccountingEnd based on Integer32"""
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


_FrUniDlciVcAccountingEnd_Type.__name__ = "Integer32"
_FrUniDlciVcAccountingEnd_Object = MibTableColumn
frUniDlciVcAccountingEnd = _FrUniDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 20),
    _FrUniDlciVcAccountingEnd_Type()
)
frUniDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcAccountingEnd.setStatus("mandatory")


class _FrUniDlciVcPriority_Type(Integer32):
    """Custom type frUniDlciVcPriority based on Integer32"""
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


_FrUniDlciVcPriority_Type.__name__ = "Integer32"
_FrUniDlciVcPriority_Object = MibTableColumn
frUniDlciVcPriority = _FrUniDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 21),
    _FrUniDlciVcPriority_Type()
)
frUniDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPriority.setStatus("mandatory")


class _FrUniDlciVcSegmentSize_Type(Unsigned32):
    """Custom type frUniDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FrUniDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_FrUniDlciVcSegmentSize_Object = MibTableColumn
frUniDlciVcSegmentSize = _FrUniDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 22),
    _FrUniDlciVcSegmentSize_Type()
)
frUniDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcSegmentSize.setStatus("mandatory")


class _FrUniDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type frUniDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FrUniDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_FrUniDlciVcMaxSubnetPktSize_Object = MibTableColumn
frUniDlciVcMaxSubnetPktSize = _FrUniDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 27),
    _FrUniDlciVcMaxSubnetPktSize_Type()
)
frUniDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _FrUniDlciVcRcosToNetwork_Type(Integer32):
    """Custom type frUniDlciVcRcosToNetwork based on Integer32"""
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


_FrUniDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_FrUniDlciVcRcosToNetwork_Object = MibTableColumn
frUniDlciVcRcosToNetwork = _FrUniDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 28),
    _FrUniDlciVcRcosToNetwork_Type()
)
frUniDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcRcosToNetwork.setStatus("mandatory")


class _FrUniDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type frUniDlciVcRcosFromNetwork based on Integer32"""
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


_FrUniDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_FrUniDlciVcRcosFromNetwork_Object = MibTableColumn
frUniDlciVcRcosFromNetwork = _FrUniDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 29),
    _FrUniDlciVcRcosFromNetwork_Type()
)
frUniDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcRcosFromNetwork.setStatus("mandatory")


class _FrUniDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type frUniDlciVcEmissionPriorityToNetwork based on Integer32"""
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


_FrUniDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_FrUniDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
frUniDlciVcEmissionPriorityToNetwork = _FrUniDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 30),
    _FrUniDlciVcEmissionPriorityToNetwork_Type()
)
frUniDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _FrUniDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type frUniDlciVcEmissionPriorityFromNetwork based on Integer32"""
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


_FrUniDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_FrUniDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
frUniDlciVcEmissionPriorityFromNetwork = _FrUniDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 31),
    _FrUniDlciVcEmissionPriorityFromNetwork_Type()
)
frUniDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _FrUniDlciVcDataPath_Type(AsciiString):
    """Custom type frUniDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FrUniDlciVcDataPath_Type.__name__ = "AsciiString"
_FrUniDlciVcDataPath_Object = MibTableColumn
frUniDlciVcDataPath = _FrUniDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 10, 1, 32),
    _FrUniDlciVcDataPath_Type()
)
frUniDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcDataPath.setStatus("mandatory")
_FrUniDlciVcIntdTable_Object = MibTable
frUniDlciVcIntdTable = _FrUniDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 11)
)
if mibBuilder.loadTexts:
    frUniDlciVcIntdTable.setStatus("mandatory")
_FrUniDlciVcIntdEntry_Object = MibTableRow
frUniDlciVcIntdEntry = _FrUniDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 11, 1)
)
frUniDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciVcIntdEntry.setStatus("mandatory")


class _FrUniDlciVcCallReferenceNumber_Type(Hex):
    """Custom type frUniDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrUniDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_FrUniDlciVcCallReferenceNumber_Object = MibTableColumn
frUniDlciVcCallReferenceNumber = _FrUniDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 11, 1, 1),
    _FrUniDlciVcCallReferenceNumber_Type()
)
frUniDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCallReferenceNumber.setStatus("mandatory")


class _FrUniDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type frUniDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrUniDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_FrUniDlciVcElapsedTimeTillNow_Object = MibTableColumn
frUniDlciVcElapsedTimeTillNow = _FrUniDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 11, 1, 2),
    _FrUniDlciVcElapsedTimeTillNow_Type()
)
frUniDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _FrUniDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type frUniDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrUniDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_FrUniDlciVcSegmentsRx_Object = MibTableColumn
frUniDlciVcSegmentsRx = _FrUniDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 11, 1, 3),
    _FrUniDlciVcSegmentsRx_Type()
)
frUniDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcSegmentsRx.setStatus("mandatory")


class _FrUniDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type frUniDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrUniDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_FrUniDlciVcSegmentsSent_Object = MibTableColumn
frUniDlciVcSegmentsSent = _FrUniDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 11, 1, 4),
    _FrUniDlciVcSegmentsSent_Type()
)
frUniDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcSegmentsSent.setStatus("mandatory")


class _FrUniDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type frUniDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrUniDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_FrUniDlciVcStartTime_Object = MibTableColumn
frUniDlciVcStartTime = _FrUniDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 11, 1, 5),
    _FrUniDlciVcStartTime_Type()
)
frUniDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcStartTime.setStatus("mandatory")
_FrUniDlciVcFrdTable_Object = MibTable
frUniDlciVcFrdTable = _FrUniDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12)
)
if mibBuilder.loadTexts:
    frUniDlciVcFrdTable.setStatus("mandatory")
_FrUniDlciVcFrdEntry_Object = MibTableRow
frUniDlciVcFrdEntry = _FrUniDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1)
)
frUniDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciVcFrdEntry.setStatus("mandatory")


class _FrUniDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type frUniDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciVcFrmCongestedToSubnet_Object = MibTableColumn
frUniDlciVcFrmCongestedToSubnet = _FrUniDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 2),
    _FrUniDlciVcFrmCongestedToSubnet_Type()
)
frUniDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _FrUniDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type frUniDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciVcCannotForwardToSubnet_Object = MibTableColumn
frUniDlciVcCannotForwardToSubnet = _FrUniDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 3),
    _FrUniDlciVcCannotForwardToSubnet_Type()
)
frUniDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _FrUniDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type frUniDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciVcNotDataXferToSubnet_Object = MibTableColumn
frUniDlciVcNotDataXferToSubnet = _FrUniDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 4),
    _FrUniDlciVcNotDataXferToSubnet_Type()
)
frUniDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _FrUniDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type frUniDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
frUniDlciVcOutOfRangeFrmFromSubnet = _FrUniDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 5),
    _FrUniDlciVcOutOfRangeFrmFromSubnet_Type()
)
frUniDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _FrUniDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type frUniDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciVcCombErrorsFromSubnet_Object = MibTableColumn
frUniDlciVcCombErrorsFromSubnet = _FrUniDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 6),
    _FrUniDlciVcCombErrorsFromSubnet_Type()
)
frUniDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _FrUniDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type frUniDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciVcDuplicatesFromSubnet_Object = MibTableColumn
frUniDlciVcDuplicatesFromSubnet = _FrUniDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 7),
    _FrUniDlciVcDuplicatesFromSubnet_Type()
)
frUniDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _FrUniDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type frUniDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciVcNotDataXferFromSubnet_Object = MibTableColumn
frUniDlciVcNotDataXferFromSubnet = _FrUniDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 8),
    _FrUniDlciVcNotDataXferFromSubnet_Type()
)
frUniDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _FrUniDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type frUniDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_FrUniDlciVcFrmLossTimeouts_Object = MibTableColumn
frUniDlciVcFrmLossTimeouts = _FrUniDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 9),
    _FrUniDlciVcFrmLossTimeouts_Type()
)
frUniDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcFrmLossTimeouts.setStatus("mandatory")


class _FrUniDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type frUniDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_FrUniDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
frUniDlciVcOoSeqByteCntExceeded = _FrUniDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 10),
    _FrUniDlciVcOoSeqByteCntExceeded_Type()
)
frUniDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _FrUniDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type frUniDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_FrUniDlciVcPeakOoSeqPktCount_Object = MibTableColumn
frUniDlciVcPeakOoSeqPktCount = _FrUniDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 11),
    _FrUniDlciVcPeakOoSeqPktCount_Type()
)
frUniDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _FrUniDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type frUniDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_FrUniDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
frUniDlciVcPeakOoSeqFrmForwarded = _FrUniDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 12),
    _FrUniDlciVcPeakOoSeqFrmForwarded_Type()
)
frUniDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _FrUniDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type frUniDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_FrUniDlciVcSendSequenceNumber_Object = MibTableColumn
frUniDlciVcSendSequenceNumber = _FrUniDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 13),
    _FrUniDlciVcSendSequenceNumber_Type()
)
frUniDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcSendSequenceNumber.setStatus("mandatory")


class _FrUniDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type frUniDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_FrUniDlciVcPktRetryTimeouts_Object = MibTableColumn
frUniDlciVcPktRetryTimeouts = _FrUniDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 15),
    _FrUniDlciVcPktRetryTimeouts_Type()
)
frUniDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPktRetryTimeouts.setStatus("mandatory")


class _FrUniDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type frUniDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_FrUniDlciVcPeakRetryQueueSize_Object = MibTableColumn
frUniDlciVcPeakRetryQueueSize = _FrUniDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 16),
    _FrUniDlciVcPeakRetryQueueSize_Type()
)
frUniDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _FrUniDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type frUniDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrUniDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_FrUniDlciVcSubnetRecoveries_Object = MibTableColumn
frUniDlciVcSubnetRecoveries = _FrUniDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 17),
    _FrUniDlciVcSubnetRecoveries_Type()
)
frUniDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcSubnetRecoveries.setStatus("mandatory")


class _FrUniDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type frUniDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_FrUniDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
frUniDlciVcOoSeqPktCntExceeded = _FrUniDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 19),
    _FrUniDlciVcOoSeqPktCntExceeded_Type()
)
frUniDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _FrUniDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type frUniDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_FrUniDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_FrUniDlciVcPeakOoSeqByteCount_Object = MibTableColumn
frUniDlciVcPeakOoSeqByteCount = _FrUniDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 12, 1, 20),
    _FrUniDlciVcPeakOoSeqByteCount_Type()
)
frUniDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_FrUniDlciVcDmepTable_Object = MibTable
frUniDlciVcDmepTable = _FrUniDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 417)
)
if mibBuilder.loadTexts:
    frUniDlciVcDmepTable.setStatus("mandatory")
_FrUniDlciVcDmepEntry_Object = MibTableRow
frUniDlciVcDmepEntry = _FrUniDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 417, 1)
)
frUniDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciVcIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    frUniDlciVcDmepEntry.setStatus("mandatory")
_FrUniDlciVcDmepValue_Type = RowPointer
_FrUniDlciVcDmepValue_Object = MibTableColumn
frUniDlciVcDmepValue = _FrUniDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 3, 417, 1, 1),
    _FrUniDlciVcDmepValue_Type()
)
frUniDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciVcDmepValue.setStatus("mandatory")
_FrUniDlciSp_ObjectIdentity = ObjectIdentity
frUniDlciSp = _FrUniDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4)
)
_FrUniDlciSpRowStatusTable_Object = MibTable
frUniDlciSpRowStatusTable = _FrUniDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 1)
)
if mibBuilder.loadTexts:
    frUniDlciSpRowStatusTable.setStatus("mandatory")
_FrUniDlciSpRowStatusEntry_Object = MibTableRow
frUniDlciSpRowStatusEntry = _FrUniDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 1, 1)
)
frUniDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciSpRowStatusEntry.setStatus("mandatory")
_FrUniDlciSpRowStatus_Type = RowStatus
_FrUniDlciSpRowStatus_Object = MibTableColumn
frUniDlciSpRowStatus = _FrUniDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 1, 1, 1),
    _FrUniDlciSpRowStatus_Type()
)
frUniDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciSpRowStatus.setStatus("mandatory")
_FrUniDlciSpComponentName_Type = DisplayString
_FrUniDlciSpComponentName_Object = MibTableColumn
frUniDlciSpComponentName = _FrUniDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 1, 1, 2),
    _FrUniDlciSpComponentName_Type()
)
frUniDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciSpComponentName.setStatus("mandatory")
_FrUniDlciSpStorageType_Type = StorageType
_FrUniDlciSpStorageType_Object = MibTableColumn
frUniDlciSpStorageType = _FrUniDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 1, 1, 4),
    _FrUniDlciSpStorageType_Type()
)
frUniDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciSpStorageType.setStatus("mandatory")
_FrUniDlciSpIndex_Type = NonReplicated
_FrUniDlciSpIndex_Object = MibTableColumn
frUniDlciSpIndex = _FrUniDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 1, 1, 10),
    _FrUniDlciSpIndex_Type()
)
frUniDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDlciSpIndex.setStatus("mandatory")
_FrUniDlciSpParmsTable_Object = MibTable
frUniDlciSpParmsTable = _FrUniDlciSpParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11)
)
if mibBuilder.loadTexts:
    frUniDlciSpParmsTable.setStatus("mandatory")
_FrUniDlciSpParmsEntry_Object = MibTableRow
frUniDlciSpParmsEntry = _FrUniDlciSpParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1)
)
frUniDlciSpParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciSpParmsEntry.setStatus("mandatory")


class _FrUniDlciSpMaximumFrameSize_Type(Unsigned32):
    """Custom type frUniDlciSpMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrUniDlciSpMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrUniDlciSpMaximumFrameSize_Object = MibTableColumn
frUniDlciSpMaximumFrameSize = _FrUniDlciSpMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 1),
    _FrUniDlciSpMaximumFrameSize_Type()
)
frUniDlciSpMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpMaximumFrameSize.setStatus("mandatory")


class _FrUniDlciSpRateEnforcement_Type(Integer32):
    """Custom type frUniDlciSpRateEnforcement based on Integer32"""
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


_FrUniDlciSpRateEnforcement_Type.__name__ = "Integer32"
_FrUniDlciSpRateEnforcement_Object = MibTableColumn
frUniDlciSpRateEnforcement = _FrUniDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 2),
    _FrUniDlciSpRateEnforcement_Type()
)
frUniDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpRateEnforcement.setStatus("mandatory")


class _FrUniDlciSpCommittedInformationRate_Type(Gauge32):
    """Custom type frUniDlciSpCommittedInformationRate based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrUniDlciSpCommittedInformationRate_Type.__name__ = "Gauge32"
_FrUniDlciSpCommittedInformationRate_Object = MibTableColumn
frUniDlciSpCommittedInformationRate = _FrUniDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 3),
    _FrUniDlciSpCommittedInformationRate_Type()
)
frUniDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpCommittedInformationRate.setStatus("mandatory")


class _FrUniDlciSpCommittedBurstSize_Type(Gauge32):
    """Custom type frUniDlciSpCommittedBurstSize based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrUniDlciSpCommittedBurstSize_Type.__name__ = "Gauge32"
_FrUniDlciSpCommittedBurstSize_Object = MibTableColumn
frUniDlciSpCommittedBurstSize = _FrUniDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 4),
    _FrUniDlciSpCommittedBurstSize_Type()
)
frUniDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpCommittedBurstSize.setStatus("mandatory")


class _FrUniDlciSpExcessBurstSize_Type(Gauge32):
    """Custom type frUniDlciSpExcessBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrUniDlciSpExcessBurstSize_Type.__name__ = "Gauge32"
_FrUniDlciSpExcessBurstSize_Object = MibTableColumn
frUniDlciSpExcessBurstSize = _FrUniDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 5),
    _FrUniDlciSpExcessBurstSize_Type()
)
frUniDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpExcessBurstSize.setStatus("mandatory")


class _FrUniDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type frUniDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_FrUniDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_FrUniDlciSpMeasurementInterval_Object = MibTableColumn
frUniDlciSpMeasurementInterval = _FrUniDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 6),
    _FrUniDlciSpMeasurementInterval_Type()
)
frUniDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpMeasurementInterval.setStatus("mandatory")


class _FrUniDlciSpRateAdaptation_Type(Integer32):
    """Custom type frUniDlciSpRateAdaptation based on Integer32"""
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
        *(("cirProportionate", 3),
          ("eirOnly", 2),
          ("off", 0),
          ("on", 1))
    )


_FrUniDlciSpRateAdaptation_Type.__name__ = "Integer32"
_FrUniDlciSpRateAdaptation_Object = MibTableColumn
frUniDlciSpRateAdaptation = _FrUniDlciSpRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 7),
    _FrUniDlciSpRateAdaptation_Type()
)
frUniDlciSpRateAdaptation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpRateAdaptation.setStatus("mandatory")


class _FrUniDlciSpAccounting_Type(Integer32):
    """Custom type frUniDlciSpAccounting based on Integer32"""
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


_FrUniDlciSpAccounting_Type.__name__ = "Integer32"
_FrUniDlciSpAccounting_Object = MibTableColumn
frUniDlciSpAccounting = _FrUniDlciSpAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 8),
    _FrUniDlciSpAccounting_Type()
)
frUniDlciSpAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpAccounting.setStatus("mandatory")


class _FrUniDlciSpRaSensitivity_Type(Unsigned32):
    """Custom type frUniDlciSpRaSensitivity based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FrUniDlciSpRaSensitivity_Type.__name__ = "Unsigned32"
_FrUniDlciSpRaSensitivity_Object = MibTableColumn
frUniDlciSpRaSensitivity = _FrUniDlciSpRaSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 9),
    _FrUniDlciSpRaSensitivity_Type()
)
frUniDlciSpRaSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpRaSensitivity.setStatus("mandatory")


class _FrUniDlciSpUpdateBCI_Type(Integer32):
    """Custom type frUniDlciSpUpdateBCI based on Integer32"""
    defaultValue = 0

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


_FrUniDlciSpUpdateBCI_Type.__name__ = "Integer32"
_FrUniDlciSpUpdateBCI_Object = MibTableColumn
frUniDlciSpUpdateBCI = _FrUniDlciSpUpdateBCI_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 4, 11, 1, 10),
    _FrUniDlciSpUpdateBCI_Type()
)
frUniDlciSpUpdateBCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniDlciSpUpdateBCI.setStatus("mandatory")
_FrUniDlciLb_ObjectIdentity = ObjectIdentity
frUniDlciLb = _FrUniDlciLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5)
)
_FrUniDlciLbRowStatusTable_Object = MibTable
frUniDlciLbRowStatusTable = _FrUniDlciLbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 1)
)
if mibBuilder.loadTexts:
    frUniDlciLbRowStatusTable.setStatus("mandatory")
_FrUniDlciLbRowStatusEntry_Object = MibTableRow
frUniDlciLbRowStatusEntry = _FrUniDlciLbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 1, 1)
)
frUniDlciLbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciLbRowStatusEntry.setStatus("mandatory")
_FrUniDlciLbRowStatus_Type = RowStatus
_FrUniDlciLbRowStatus_Object = MibTableColumn
frUniDlciLbRowStatus = _FrUniDlciLbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 1, 1, 1),
    _FrUniDlciLbRowStatus_Type()
)
frUniDlciLbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbRowStatus.setStatus("mandatory")
_FrUniDlciLbComponentName_Type = DisplayString
_FrUniDlciLbComponentName_Object = MibTableColumn
frUniDlciLbComponentName = _FrUniDlciLbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 1, 1, 2),
    _FrUniDlciLbComponentName_Type()
)
frUniDlciLbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbComponentName.setStatus("mandatory")
_FrUniDlciLbStorageType_Type = StorageType
_FrUniDlciLbStorageType_Object = MibTableColumn
frUniDlciLbStorageType = _FrUniDlciLbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 1, 1, 4),
    _FrUniDlciLbStorageType_Type()
)
frUniDlciLbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbStorageType.setStatus("mandatory")
_FrUniDlciLbIndex_Type = NonReplicated
_FrUniDlciLbIndex_Object = MibTableColumn
frUniDlciLbIndex = _FrUniDlciLbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 1, 1, 10),
    _FrUniDlciLbIndex_Type()
)
frUniDlciLbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniDlciLbIndex.setStatus("mandatory")
_FrUniDlciLbStatsTable_Object = MibTable
frUniDlciLbStatsTable = _FrUniDlciLbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10)
)
if mibBuilder.loadTexts:
    frUniDlciLbStatsTable.setStatus("mandatory")
_FrUniDlciLbStatsEntry_Object = MibTableRow
frUniDlciLbStatsEntry = _FrUniDlciLbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1)
)
frUniDlciLbStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciLbStatsEntry.setStatus("mandatory")


class _FrUniDlciLbLocalTotalFrm_Type(Unsigned32):
    """Custom type frUniDlciLbLocalTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbLocalTotalFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbLocalTotalFrm_Object = MibTableColumn
frUniDlciLbLocalTotalFrm = _FrUniDlciLbLocalTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 1),
    _FrUniDlciLbLocalTotalFrm_Type()
)
frUniDlciLbLocalTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbLocalTotalFrm.setStatus("mandatory")


class _FrUniDlciLbLocalTotalBytes_Type(Unsigned32):
    """Custom type frUniDlciLbLocalTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbLocalTotalBytes_Type.__name__ = "Unsigned32"
_FrUniDlciLbLocalTotalBytes_Object = MibTableColumn
frUniDlciLbLocalTotalBytes = _FrUniDlciLbLocalTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 2),
    _FrUniDlciLbLocalTotalBytes_Type()
)
frUniDlciLbLocalTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbLocalTotalBytes.setStatus("mandatory")


class _FrUniDlciLbLocalFecnFrm_Type(Unsigned32):
    """Custom type frUniDlciLbLocalFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbLocalFecnFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbLocalFecnFrm_Object = MibTableColumn
frUniDlciLbLocalFecnFrm = _FrUniDlciLbLocalFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 3),
    _FrUniDlciLbLocalFecnFrm_Type()
)
frUniDlciLbLocalFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbLocalFecnFrm.setStatus("mandatory")


class _FrUniDlciLbLocalBecnFrm_Type(Unsigned32):
    """Custom type frUniDlciLbLocalBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbLocalBecnFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbLocalBecnFrm_Object = MibTableColumn
frUniDlciLbLocalBecnFrm = _FrUniDlciLbLocalBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 4),
    _FrUniDlciLbLocalBecnFrm_Type()
)
frUniDlciLbLocalBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbLocalBecnFrm.setStatus("mandatory")


class _FrUniDlciLbLocalDeFrm_Type(Unsigned32):
    """Custom type frUniDlciLbLocalDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbLocalDeFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbLocalDeFrm_Object = MibTableColumn
frUniDlciLbLocalDeFrm = _FrUniDlciLbLocalDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 5),
    _FrUniDlciLbLocalDeFrm_Type()
)
frUniDlciLbLocalDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbLocalDeFrm.setStatus("mandatory")


class _FrUniDlciLbLocalDeBytes_Type(Unsigned32):
    """Custom type frUniDlciLbLocalDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbLocalDeBytes_Type.__name__ = "Unsigned32"
_FrUniDlciLbLocalDeBytes_Object = MibTableColumn
frUniDlciLbLocalDeBytes = _FrUniDlciLbLocalDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 6),
    _FrUniDlciLbLocalDeBytes_Type()
)
frUniDlciLbLocalDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbLocalDeBytes.setStatus("mandatory")


class _FrUniDlciLbRemoteTotalFrm_Type(Unsigned32):
    """Custom type frUniDlciLbRemoteTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbRemoteTotalFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbRemoteTotalFrm_Object = MibTableColumn
frUniDlciLbRemoteTotalFrm = _FrUniDlciLbRemoteTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 7),
    _FrUniDlciLbRemoteTotalFrm_Type()
)
frUniDlciLbRemoteTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbRemoteTotalFrm.setStatus("mandatory")


class _FrUniDlciLbRemoteTotalBytes_Type(Unsigned32):
    """Custom type frUniDlciLbRemoteTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbRemoteTotalBytes_Type.__name__ = "Unsigned32"
_FrUniDlciLbRemoteTotalBytes_Object = MibTableColumn
frUniDlciLbRemoteTotalBytes = _FrUniDlciLbRemoteTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 8),
    _FrUniDlciLbRemoteTotalBytes_Type()
)
frUniDlciLbRemoteTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbRemoteTotalBytes.setStatus("mandatory")


class _FrUniDlciLbRemoteFecnFrm_Type(Unsigned32):
    """Custom type frUniDlciLbRemoteFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbRemoteFecnFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbRemoteFecnFrm_Object = MibTableColumn
frUniDlciLbRemoteFecnFrm = _FrUniDlciLbRemoteFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 9),
    _FrUniDlciLbRemoteFecnFrm_Type()
)
frUniDlciLbRemoteFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbRemoteFecnFrm.setStatus("mandatory")


class _FrUniDlciLbRemoteBecnFrm_Type(Unsigned32):
    """Custom type frUniDlciLbRemoteBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbRemoteBecnFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbRemoteBecnFrm_Object = MibTableColumn
frUniDlciLbRemoteBecnFrm = _FrUniDlciLbRemoteBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 10),
    _FrUniDlciLbRemoteBecnFrm_Type()
)
frUniDlciLbRemoteBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbRemoteBecnFrm.setStatus("mandatory")


class _FrUniDlciLbRemoteDeFrm_Type(Unsigned32):
    """Custom type frUniDlciLbRemoteDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbRemoteDeFrm_Type.__name__ = "Unsigned32"
_FrUniDlciLbRemoteDeFrm_Object = MibTableColumn
frUniDlciLbRemoteDeFrm = _FrUniDlciLbRemoteDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 13),
    _FrUniDlciLbRemoteDeFrm_Type()
)
frUniDlciLbRemoteDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbRemoteDeFrm.setStatus("mandatory")


class _FrUniDlciLbRemoteDeBytes_Type(Unsigned32):
    """Custom type frUniDlciLbRemoteDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciLbRemoteDeBytes_Type.__name__ = "Unsigned32"
_FrUniDlciLbRemoteDeBytes_Object = MibTableColumn
frUniDlciLbRemoteDeBytes = _FrUniDlciLbRemoteDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 5, 10, 1, 14),
    _FrUniDlciLbRemoteDeBytes_Type()
)
frUniDlciLbRemoteDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLbRemoteDeBytes.setStatus("mandatory")
_FrUniDlciStateTable_Object = MibTable
frUniDlciStateTable = _FrUniDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10)
)
if mibBuilder.loadTexts:
    frUniDlciStateTable.setStatus("mandatory")
_FrUniDlciStateEntry_Object = MibTableRow
frUniDlciStateEntry = _FrUniDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1)
)
frUniDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciStateEntry.setStatus("mandatory")


class _FrUniDlciAdminState_Type(Integer32):
    """Custom type frUniDlciAdminState based on Integer32"""
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


_FrUniDlciAdminState_Type.__name__ = "Integer32"
_FrUniDlciAdminState_Object = MibTableColumn
frUniDlciAdminState = _FrUniDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 1),
    _FrUniDlciAdminState_Type()
)
frUniDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciAdminState.setStatus("mandatory")


class _FrUniDlciOperationalState_Type(Integer32):
    """Custom type frUniDlciOperationalState based on Integer32"""
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


_FrUniDlciOperationalState_Type.__name__ = "Integer32"
_FrUniDlciOperationalState_Object = MibTableColumn
frUniDlciOperationalState = _FrUniDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 2),
    _FrUniDlciOperationalState_Type()
)
frUniDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciOperationalState.setStatus("mandatory")


class _FrUniDlciUsageState_Type(Integer32):
    """Custom type frUniDlciUsageState based on Integer32"""
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


_FrUniDlciUsageState_Type.__name__ = "Integer32"
_FrUniDlciUsageState_Object = MibTableColumn
frUniDlciUsageState = _FrUniDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 3),
    _FrUniDlciUsageState_Type()
)
frUniDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciUsageState.setStatus("mandatory")


class _FrUniDlciAvailabilityStatus_Type(OctetString):
    """Custom type frUniDlciAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FrUniDlciAvailabilityStatus_Type.__name__ = "OctetString"
_FrUniDlciAvailabilityStatus_Object = MibTableColumn
frUniDlciAvailabilityStatus = _FrUniDlciAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 4),
    _FrUniDlciAvailabilityStatus_Type()
)
frUniDlciAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciAvailabilityStatus.setStatus("mandatory")


class _FrUniDlciProceduralStatus_Type(OctetString):
    """Custom type frUniDlciProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniDlciProceduralStatus_Type.__name__ = "OctetString"
_FrUniDlciProceduralStatus_Object = MibTableColumn
frUniDlciProceduralStatus = _FrUniDlciProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 5),
    _FrUniDlciProceduralStatus_Type()
)
frUniDlciProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciProceduralStatus.setStatus("mandatory")


class _FrUniDlciControlStatus_Type(OctetString):
    """Custom type frUniDlciControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniDlciControlStatus_Type.__name__ = "OctetString"
_FrUniDlciControlStatus_Object = MibTableColumn
frUniDlciControlStatus = _FrUniDlciControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 6),
    _FrUniDlciControlStatus_Type()
)
frUniDlciControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciControlStatus.setStatus("mandatory")


class _FrUniDlciAlarmStatus_Type(OctetString):
    """Custom type frUniDlciAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniDlciAlarmStatus_Type.__name__ = "OctetString"
_FrUniDlciAlarmStatus_Object = MibTableColumn
frUniDlciAlarmStatus = _FrUniDlciAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 7),
    _FrUniDlciAlarmStatus_Type()
)
frUniDlciAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciAlarmStatus.setStatus("mandatory")


class _FrUniDlciStandbyStatus_Type(Integer32):
    """Custom type frUniDlciStandbyStatus based on Integer32"""
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


_FrUniDlciStandbyStatus_Type.__name__ = "Integer32"
_FrUniDlciStandbyStatus_Object = MibTableColumn
frUniDlciStandbyStatus = _FrUniDlciStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 8),
    _FrUniDlciStandbyStatus_Type()
)
frUniDlciStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciStandbyStatus.setStatus("mandatory")


class _FrUniDlciUnknownStatus_Type(Integer32):
    """Custom type frUniDlciUnknownStatus based on Integer32"""
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


_FrUniDlciUnknownStatus_Type.__name__ = "Integer32"
_FrUniDlciUnknownStatus_Object = MibTableColumn
frUniDlciUnknownStatus = _FrUniDlciUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 10, 1, 9),
    _FrUniDlciUnknownStatus_Type()
)
frUniDlciUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciUnknownStatus.setStatus("mandatory")
_FrUniDlciAbitTable_Object = MibTable
frUniDlciAbitTable = _FrUniDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 12)
)
if mibBuilder.loadTexts:
    frUniDlciAbitTable.setStatus("mandatory")
_FrUniDlciAbitEntry_Object = MibTableRow
frUniDlciAbitEntry = _FrUniDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 12, 1)
)
frUniDlciAbitEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciAbitEntry.setStatus("mandatory")


class _FrUniDlciABitStatusToIf_Type(Integer32):
    """Custom type frUniDlciABitStatusToIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_FrUniDlciABitStatusToIf_Type.__name__ = "Integer32"
_FrUniDlciABitStatusToIf_Object = MibTableColumn
frUniDlciABitStatusToIf = _FrUniDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 12, 1, 1),
    _FrUniDlciABitStatusToIf_Type()
)
frUniDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciABitStatusToIf.setStatus("mandatory")


class _FrUniDlciABitReasonToIf_Type(Integer32):
    """Custom type frUniDlciABitReasonToIf based on Integer32"""
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


_FrUniDlciABitReasonToIf_Type.__name__ = "Integer32"
_FrUniDlciABitReasonToIf_Object = MibTableColumn
frUniDlciABitReasonToIf = _FrUniDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 12, 1, 2),
    _FrUniDlciABitReasonToIf_Type()
)
frUniDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciABitReasonToIf.setStatus("mandatory")


class _FrUniDlciABitStatusFromIf_Type(Integer32):
    """Custom type frUniDlciABitStatusFromIf based on Integer32"""
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
          ("inactive", 0),
          ("notApplicable", 2))
    )


_FrUniDlciABitStatusFromIf_Type.__name__ = "Integer32"
_FrUniDlciABitStatusFromIf_Object = MibTableColumn
frUniDlciABitStatusFromIf = _FrUniDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 12, 1, 3),
    _FrUniDlciABitStatusFromIf_Type()
)
frUniDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciABitStatusFromIf.setStatus("mandatory")


class _FrUniDlciABitReasonFromIf_Type(Integer32):
    """Custom type frUniDlciABitReasonFromIf based on Integer32"""
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
          ("remoteUserSignaled", 1))
    )


_FrUniDlciABitReasonFromIf_Type.__name__ = "Integer32"
_FrUniDlciABitReasonFromIf_Object = MibTableColumn
frUniDlciABitReasonFromIf = _FrUniDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 12, 1, 4),
    _FrUniDlciABitReasonFromIf_Type()
)
frUniDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciABitReasonFromIf.setStatus("mandatory")


class _FrUniDlciLoopbackState_Type(Integer32):
    """Custom type frUniDlciLoopbackState based on Integer32"""
    defaultValue = 0

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


_FrUniDlciLoopbackState_Type.__name__ = "Integer32"
_FrUniDlciLoopbackState_Object = MibTableColumn
frUniDlciLoopbackState = _FrUniDlciLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 12, 1, 5),
    _FrUniDlciLoopbackState_Type()
)
frUniDlciLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLoopbackState.setStatus("mandatory")
_FrUniDlciCalldTable_Object = MibTable
frUniDlciCalldTable = _FrUniDlciCalldTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 13)
)
if mibBuilder.loadTexts:
    frUniDlciCalldTable.setStatus("mandatory")
_FrUniDlciCalldEntry_Object = MibTableRow
frUniDlciCalldEntry = _FrUniDlciCalldEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 13, 1)
)
frUniDlciCalldEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciCalldEntry.setStatus("mandatory")


class _FrUniDlciCallType_Type(Integer32):
    """Custom type frUniDlciCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 0),
          ("svc", 1))
    )


_FrUniDlciCallType_Type.__name__ = "Integer32"
_FrUniDlciCallType_Object = MibTableColumn
frUniDlciCallType = _FrUniDlciCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 13, 1, 1),
    _FrUniDlciCallType_Type()
)
frUniDlciCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciCallType.setStatus("mandatory")


class _FrUniDlciQ933CallState_Type(Integer32):
    """Custom type frUniDlciQ933CallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              6,
              9,
              10,
              11,
              12,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("disconnectIndication", 12),
          ("disconnectRequest", 11),
          ("incomingCallProceeding", 9),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseRequest", 19))
    )


_FrUniDlciQ933CallState_Type.__name__ = "Integer32"
_FrUniDlciQ933CallState_Object = MibTableColumn
frUniDlciQ933CallState = _FrUniDlciQ933CallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 13, 1, 2),
    _FrUniDlciQ933CallState_Type()
)
frUniDlciQ933CallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciQ933CallState.setStatus("mandatory")


class _FrUniDlciQ933CallReference_Type(Unsigned32):
    """Custom type frUniDlciQ933CallReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_FrUniDlciQ933CallReference_Type.__name__ = "Unsigned32"
_FrUniDlciQ933CallReference_Object = MibTableColumn
frUniDlciQ933CallReference = _FrUniDlciQ933CallReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 13, 1, 3),
    _FrUniDlciQ933CallReference_Type()
)
frUniDlciQ933CallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciQ933CallReference.setStatus("mandatory")
_FrUniDlciSpOpTable_Object = MibTable
frUniDlciSpOpTable = _FrUniDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14)
)
if mibBuilder.loadTexts:
    frUniDlciSpOpTable.setStatus("mandatory")
_FrUniDlciSpOpEntry_Object = MibTableRow
frUniDlciSpOpEntry = _FrUniDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1)
)
frUniDlciSpOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciSpOpEntry.setStatus("mandatory")


class _FrUniDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type frUniDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrUniDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrUniDlciMaximumFrameSize_Object = MibTableColumn
frUniDlciMaximumFrameSize = _FrUniDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 1),
    _FrUniDlciMaximumFrameSize_Type()
)
frUniDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciMaximumFrameSize.setStatus("mandatory")


class _FrUniDlciRateEnforcement_Type(Integer32):
    """Custom type frUniDlciRateEnforcement based on Integer32"""
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


_FrUniDlciRateEnforcement_Type.__name__ = "Integer32"
_FrUniDlciRateEnforcement_Object = MibTableColumn
frUniDlciRateEnforcement = _FrUniDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 2),
    _FrUniDlciRateEnforcement_Type()
)
frUniDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciRateEnforcement.setStatus("obsolete")


class _FrUniDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type frUniDlciCommittedInformationRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrUniDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrUniDlciCommittedInformationRate_Object = MibTableColumn
frUniDlciCommittedInformationRate = _FrUniDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 3),
    _FrUniDlciCommittedInformationRate_Type()
)
frUniDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciCommittedInformationRate.setStatus("mandatory")


class _FrUniDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type frUniDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrUniDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_FrUniDlciCommittedBurstSize_Object = MibTableColumn
frUniDlciCommittedBurstSize = _FrUniDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 4),
    _FrUniDlciCommittedBurstSize_Type()
)
frUniDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciCommittedBurstSize.setStatus("mandatory")


class _FrUniDlciExcessBurstSize_Type(Unsigned32):
    """Custom type frUniDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrUniDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_FrUniDlciExcessBurstSize_Object = MibTableColumn
frUniDlciExcessBurstSize = _FrUniDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 5),
    _FrUniDlciExcessBurstSize_Type()
)
frUniDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciExcessBurstSize.setStatus("mandatory")


class _FrUniDlciMeasurementInterval_Type(Unsigned32):
    """Custom type frUniDlciMeasurementInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciMeasurementInterval_Type.__name__ = "Unsigned32"
_FrUniDlciMeasurementInterval_Object = MibTableColumn
frUniDlciMeasurementInterval = _FrUniDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 6),
    _FrUniDlciMeasurementInterval_Type()
)
frUniDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciMeasurementInterval.setStatus("mandatory")


class _FrUniDlciRateAdaptation_Type(Integer32):
    """Custom type frUniDlciRateAdaptation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eirOnly", 2),
          ("off", 0),
          ("on", 1))
    )


_FrUniDlciRateAdaptation_Type.__name__ = "Integer32"
_FrUniDlciRateAdaptation_Object = MibTableColumn
frUniDlciRateAdaptation = _FrUniDlciRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 7),
    _FrUniDlciRateAdaptation_Type()
)
frUniDlciRateAdaptation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciRateAdaptation.setStatus("obsolete")


class _FrUniDlciAccounting_Type(Integer32):
    """Custom type frUniDlciAccounting based on Integer32"""
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


_FrUniDlciAccounting_Type.__name__ = "Integer32"
_FrUniDlciAccounting_Object = MibTableColumn
frUniDlciAccounting = _FrUniDlciAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 8),
    _FrUniDlciAccounting_Type()
)
frUniDlciAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciAccounting.setStatus("mandatory")


class _FrUniDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type frUniDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_FrUniDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrUniDlciEmissionPriorityToIf_Object = MibTableColumn
frUniDlciEmissionPriorityToIf = _FrUniDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 9),
    _FrUniDlciEmissionPriorityToIf_Type()
)
frUniDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciEmissionPriorityToIf.setStatus("mandatory")


class _FrUniDlciTransferPriToNwk_Type(Unsigned32):
    """Custom type frUniDlciTransferPriToNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrUniDlciTransferPriToNwk_Type.__name__ = "Unsigned32"
_FrUniDlciTransferPriToNwk_Object = MibTableColumn
frUniDlciTransferPriToNwk = _FrUniDlciTransferPriToNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 10),
    _FrUniDlciTransferPriToNwk_Type()
)
frUniDlciTransferPriToNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTransferPriToNwk.setStatus("mandatory")


class _FrUniDlciTransferPriFromNwk_Type(Unsigned32):
    """Custom type frUniDlciTransferPriFromNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrUniDlciTransferPriFromNwk_Type.__name__ = "Unsigned32"
_FrUniDlciTransferPriFromNwk_Object = MibTableColumn
frUniDlciTransferPriFromNwk = _FrUniDlciTransferPriFromNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 14, 1, 11),
    _FrUniDlciTransferPriFromNwk_Type()
)
frUniDlciTransferPriFromNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTransferPriFromNwk.setStatus("mandatory")
_FrUniDlciStatsTable_Object = MibTable
frUniDlciStatsTable = _FrUniDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15)
)
if mibBuilder.loadTexts:
    frUniDlciStatsTable.setStatus("mandatory")
_FrUniDlciStatsEntry_Object = MibTableRow
frUniDlciStatsEntry = _FrUniDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1)
)
frUniDlciStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciStatsEntry.setStatus("mandatory")


class _FrUniDlciFrmToIf_Type(Unsigned32):
    """Custom type frUniDlciFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciFrmToIf_Type.__name__ = "Unsigned32"
_FrUniDlciFrmToIf_Object = MibTableColumn
frUniDlciFrmToIf = _FrUniDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 1),
    _FrUniDlciFrmToIf_Type()
)
frUniDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciFrmToIf.setStatus("mandatory")


class _FrUniDlciFecnFrmToIf_Type(Unsigned32):
    """Custom type frUniDlciFecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciFecnFrmToIf_Type.__name__ = "Unsigned32"
_FrUniDlciFecnFrmToIf_Object = MibTableColumn
frUniDlciFecnFrmToIf = _FrUniDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 2),
    _FrUniDlciFecnFrmToIf_Type()
)
frUniDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciFecnFrmToIf.setStatus("mandatory")


class _FrUniDlciBecnFrmToIf_Type(Unsigned32):
    """Custom type frUniDlciBecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciBecnFrmToIf_Type.__name__ = "Unsigned32"
_FrUniDlciBecnFrmToIf_Object = MibTableColumn
frUniDlciBecnFrmToIf = _FrUniDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 3),
    _FrUniDlciBecnFrmToIf_Type()
)
frUniDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciBecnFrmToIf.setStatus("mandatory")


class _FrUniDlciBciToSubnet_Type(Unsigned32):
    """Custom type frUniDlciBciToSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciBciToSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciBciToSubnet_Object = MibTableColumn
frUniDlciBciToSubnet = _FrUniDlciBciToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 4),
    _FrUniDlciBciToSubnet_Type()
)
frUniDlciBciToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciBciToSubnet.setStatus("mandatory")


class _FrUniDlciDeFrmToIf_Type(Unsigned32):
    """Custom type frUniDlciDeFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDeFrmToIf_Type.__name__ = "Unsigned32"
_FrUniDlciDeFrmToIf_Object = MibTableColumn
frUniDlciDeFrmToIf = _FrUniDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 5),
    _FrUniDlciDeFrmToIf_Type()
)
frUniDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDeFrmToIf.setStatus("mandatory")


class _FrUniDlciDiscCongestedToIf_Type(Unsigned32):
    """Custom type frUniDlciDiscCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscCongestedToIf_Type.__name__ = "Unsigned32"
_FrUniDlciDiscCongestedToIf_Object = MibTableColumn
frUniDlciDiscCongestedToIf = _FrUniDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 6),
    _FrUniDlciDiscCongestedToIf_Type()
)
frUniDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscCongestedToIf.setStatus("mandatory")


class _FrUniDlciDiscDeCongestedToIf_Type(Unsigned32):
    """Custom type frUniDlciDiscDeCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscDeCongestedToIf_Type.__name__ = "Unsigned32"
_FrUniDlciDiscDeCongestedToIf_Object = MibTableColumn
frUniDlciDiscDeCongestedToIf = _FrUniDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 7),
    _FrUniDlciDiscDeCongestedToIf_Type()
)
frUniDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscDeCongestedToIf.setStatus("mandatory")


class _FrUniDlciFrmFromIf_Type(Unsigned32):
    """Custom type frUniDlciFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciFrmFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciFrmFromIf_Object = MibTableColumn
frUniDlciFrmFromIf = _FrUniDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 8),
    _FrUniDlciFrmFromIf_Type()
)
frUniDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciFrmFromIf.setStatus("mandatory")


class _FrUniDlciFecnFrmFromIf_Type(Unsigned32):
    """Custom type frUniDlciFecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciFecnFrmFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciFecnFrmFromIf_Object = MibTableColumn
frUniDlciFecnFrmFromIf = _FrUniDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 9),
    _FrUniDlciFecnFrmFromIf_Type()
)
frUniDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciFecnFrmFromIf.setStatus("mandatory")


class _FrUniDlciBecnFrmFromIf_Type(Unsigned32):
    """Custom type frUniDlciBecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciBecnFrmFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciBecnFrmFromIf_Object = MibTableColumn
frUniDlciBecnFrmFromIf = _FrUniDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 10),
    _FrUniDlciBecnFrmFromIf_Type()
)
frUniDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciBecnFrmFromIf.setStatus("mandatory")


class _FrUniDlciFciFromSubnet_Type(Unsigned32):
    """Custom type frUniDlciFciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciFciFromSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciFciFromSubnet_Object = MibTableColumn
frUniDlciFciFromSubnet = _FrUniDlciFciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 11),
    _FrUniDlciFciFromSubnet_Type()
)
frUniDlciFciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciFciFromSubnet.setStatus("mandatory")


class _FrUniDlciBciFromSubnet_Type(Unsigned32):
    """Custom type frUniDlciBciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciBciFromSubnet_Type.__name__ = "Unsigned32"
_FrUniDlciBciFromSubnet_Object = MibTableColumn
frUniDlciBciFromSubnet = _FrUniDlciBciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 12),
    _FrUniDlciBciFromSubnet_Type()
)
frUniDlciBciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciBciFromSubnet.setStatus("mandatory")


class _FrUniDlciDeFrmFromIf_Type(Unsigned32):
    """Custom type frUniDlciDeFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDeFrmFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciDeFrmFromIf_Object = MibTableColumn
frUniDlciDeFrmFromIf = _FrUniDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 13),
    _FrUniDlciDeFrmFromIf_Type()
)
frUniDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDeFrmFromIf.setStatus("mandatory")


class _FrUniDlciExcessFrmFromIf_Type(Unsigned32):
    """Custom type frUniDlciExcessFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciExcessFrmFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciExcessFrmFromIf_Object = MibTableColumn
frUniDlciExcessFrmFromIf = _FrUniDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 14),
    _FrUniDlciExcessFrmFromIf_Type()
)
frUniDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciExcessFrmFromIf.setStatus("mandatory")


class _FrUniDlciDiscExcessFromIf_Type(Unsigned32):
    """Custom type frUniDlciDiscExcessFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscExcessFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciDiscExcessFromIf_Object = MibTableColumn
frUniDlciDiscExcessFromIf = _FrUniDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 15),
    _FrUniDlciDiscExcessFromIf_Type()
)
frUniDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscExcessFromIf.setStatus("mandatory")


class _FrUniDlciDiscFrameAbit_Type(Unsigned32):
    """Custom type frUniDlciDiscFrameAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscFrameAbit_Type.__name__ = "Unsigned32"
_FrUniDlciDiscFrameAbit_Object = MibTableColumn
frUniDlciDiscFrameAbit = _FrUniDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 16),
    _FrUniDlciDiscFrameAbit_Type()
)
frUniDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscFrameAbit.setStatus("mandatory")


class _FrUniDlciDiscCongestedFromIf_Type(Unsigned32):
    """Custom type frUniDlciDiscCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscCongestedFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciDiscCongestedFromIf_Object = MibTableColumn
frUniDlciDiscCongestedFromIf = _FrUniDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 17),
    _FrUniDlciDiscCongestedFromIf_Type()
)
frUniDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscCongestedFromIf.setStatus("mandatory")


class _FrUniDlciDiscDeCongestedFromIf_Type(Unsigned32):
    """Custom type frUniDlciDiscDeCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscDeCongestedFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciDiscDeCongestedFromIf_Object = MibTableColumn
frUniDlciDiscDeCongestedFromIf = _FrUniDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 18),
    _FrUniDlciDiscDeCongestedFromIf_Type()
)
frUniDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscDeCongestedFromIf.setStatus("mandatory")


class _FrUniDlciErrorShortFrmFromIf_Type(Unsigned32):
    """Custom type frUniDlciErrorShortFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciErrorShortFrmFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciErrorShortFrmFromIf_Object = MibTableColumn
frUniDlciErrorShortFrmFromIf = _FrUniDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 19),
    _FrUniDlciErrorShortFrmFromIf_Type()
)
frUniDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciErrorShortFrmFromIf.setStatus("mandatory")


class _FrUniDlciErrorLongFrmFromIf_Type(Unsigned32):
    """Custom type frUniDlciErrorLongFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciErrorLongFrmFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciErrorLongFrmFromIf_Object = MibTableColumn
frUniDlciErrorLongFrmFromIf = _FrUniDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 20),
    _FrUniDlciErrorLongFrmFromIf_Type()
)
frUniDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciErrorLongFrmFromIf.setStatus("mandatory")


class _FrUniDlciBecnFrmSetByService_Type(Unsigned32):
    """Custom type frUniDlciBecnFrmSetByService based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciBecnFrmSetByService_Type.__name__ = "Unsigned32"
_FrUniDlciBecnFrmSetByService_Object = MibTableColumn
frUniDlciBecnFrmSetByService = _FrUniDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 21),
    _FrUniDlciBecnFrmSetByService_Type()
)
frUniDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciBecnFrmSetByService.setStatus("mandatory")


class _FrUniDlciBytesToIf_Type(Unsigned32):
    """Custom type frUniDlciBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciBytesToIf_Type.__name__ = "Unsigned32"
_FrUniDlciBytesToIf_Object = MibTableColumn
frUniDlciBytesToIf = _FrUniDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 22),
    _FrUniDlciBytesToIf_Type()
)
frUniDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciBytesToIf.setStatus("mandatory")


class _FrUniDlciDeBytesToIf_Type(Unsigned32):
    """Custom type frUniDlciDeBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDeBytesToIf_Type.__name__ = "Unsigned32"
_FrUniDlciDeBytesToIf_Object = MibTableColumn
frUniDlciDeBytesToIf = _FrUniDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 23),
    _FrUniDlciDeBytesToIf_Type()
)
frUniDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDeBytesToIf.setStatus("mandatory")


class _FrUniDlciDiscCongestedToIfBytes_Type(Unsigned32):
    """Custom type frUniDlciDiscCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscCongestedToIfBytes_Type.__name__ = "Unsigned32"
_FrUniDlciDiscCongestedToIfBytes_Object = MibTableColumn
frUniDlciDiscCongestedToIfBytes = _FrUniDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 24),
    _FrUniDlciDiscCongestedToIfBytes_Type()
)
frUniDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscCongestedToIfBytes.setStatus("mandatory")


class _FrUniDlciDiscDeCongestedToIfBytes_Type(Unsigned32):
    """Custom type frUniDlciDiscDeCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscDeCongestedToIfBytes_Type.__name__ = "Unsigned32"
_FrUniDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
frUniDlciDiscDeCongestedToIfBytes = _FrUniDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 25),
    _FrUniDlciDiscDeCongestedToIfBytes_Type()
)
frUniDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscDeCongestedToIfBytes.setStatus("mandatory")


class _FrUniDlciBytesFromIf_Type(Unsigned32):
    """Custom type frUniDlciBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciBytesFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciBytesFromIf_Object = MibTableColumn
frUniDlciBytesFromIf = _FrUniDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 26),
    _FrUniDlciBytesFromIf_Type()
)
frUniDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciBytesFromIf.setStatus("mandatory")


class _FrUniDlciDeBytesFromIf_Type(Unsigned32):
    """Custom type frUniDlciDeBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDeBytesFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciDeBytesFromIf_Object = MibTableColumn
frUniDlciDeBytesFromIf = _FrUniDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 27),
    _FrUniDlciDeBytesFromIf_Type()
)
frUniDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDeBytesFromIf.setStatus("mandatory")


class _FrUniDlciExcessBytesFromIf_Type(Unsigned32):
    """Custom type frUniDlciExcessBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciExcessBytesFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciExcessBytesFromIf_Object = MibTableColumn
frUniDlciExcessBytesFromIf = _FrUniDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 28),
    _FrUniDlciExcessBytesFromIf_Type()
)
frUniDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciExcessBytesFromIf.setStatus("mandatory")


class _FrUniDlciDiscExcessFromIfBytes_Type(Unsigned32):
    """Custom type frUniDlciDiscExcessFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscExcessFromIfBytes_Type.__name__ = "Unsigned32"
_FrUniDlciDiscExcessFromIfBytes_Object = MibTableColumn
frUniDlciDiscExcessFromIfBytes = _FrUniDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 29),
    _FrUniDlciDiscExcessFromIfBytes_Type()
)
frUniDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscExcessFromIfBytes.setStatus("mandatory")


class _FrUniDlciDiscByteAbit_Type(Unsigned32):
    """Custom type frUniDlciDiscByteAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscByteAbit_Type.__name__ = "Unsigned32"
_FrUniDlciDiscByteAbit_Object = MibTableColumn
frUniDlciDiscByteAbit = _FrUniDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 30),
    _FrUniDlciDiscByteAbit_Type()
)
frUniDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscByteAbit.setStatus("mandatory")


class _FrUniDlciDiscCongestedFromIfBytes_Type(Unsigned32):
    """Custom type frUniDlciDiscCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_FrUniDlciDiscCongestedFromIfBytes_Object = MibTableColumn
frUniDlciDiscCongestedFromIfBytes = _FrUniDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 31),
    _FrUniDlciDiscCongestedFromIfBytes_Type()
)
frUniDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscCongestedFromIfBytes.setStatus("mandatory")


class _FrUniDlciDiscDeCongestedFromIfBytes_Type(Unsigned32):
    """Custom type frUniDlciDiscDeCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscDeCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_FrUniDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
frUniDlciDiscDeCongestedFromIfBytes = _FrUniDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 32),
    _FrUniDlciDiscDeCongestedFromIfBytes_Type()
)
frUniDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")


class _FrUniDlciErrorShortBytesFromIf_Type(Unsigned32):
    """Custom type frUniDlciErrorShortBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciErrorShortBytesFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciErrorShortBytesFromIf_Object = MibTableColumn
frUniDlciErrorShortBytesFromIf = _FrUniDlciErrorShortBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 33),
    _FrUniDlciErrorShortBytesFromIf_Type()
)
frUniDlciErrorShortBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciErrorShortBytesFromIf.setStatus("mandatory")


class _FrUniDlciErrorLongBytesFromIf_Type(Unsigned32):
    """Custom type frUniDlciErrorLongBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciErrorLongBytesFromIf_Type.__name__ = "Unsigned32"
_FrUniDlciErrorLongBytesFromIf_Object = MibTableColumn
frUniDlciErrorLongBytesFromIf = _FrUniDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 34),
    _FrUniDlciErrorLongBytesFromIf_Type()
)
frUniDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciErrorLongBytesFromIf.setStatus("mandatory")


class _FrUniDlciRateAdaptReduct_Type(Unsigned32):
    """Custom type frUniDlciRateAdaptReduct based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciRateAdaptReduct_Type.__name__ = "Unsigned32"
_FrUniDlciRateAdaptReduct_Object = MibTableColumn
frUniDlciRateAdaptReduct = _FrUniDlciRateAdaptReduct_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 35),
    _FrUniDlciRateAdaptReduct_Type()
)
frUniDlciRateAdaptReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciRateAdaptReduct.setStatus("mandatory")


class _FrUniDlciRateAdaptReductPeriod_Type(Unsigned32):
    """Custom type frUniDlciRateAdaptReductPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciRateAdaptReductPeriod_Type.__name__ = "Unsigned32"
_FrUniDlciRateAdaptReductPeriod_Object = MibTableColumn
frUniDlciRateAdaptReductPeriod = _FrUniDlciRateAdaptReductPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 36),
    _FrUniDlciRateAdaptReductPeriod_Type()
)
frUniDlciRateAdaptReductPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciRateAdaptReductPeriod.setStatus("mandatory")


class _FrUniDlciTransferPriorityToNetwork_Type(Integer32):
    """Custom type frUniDlciTransferPriorityToNetwork based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_FrUniDlciTransferPriorityToNetwork_Type.__name__ = "Integer32"
_FrUniDlciTransferPriorityToNetwork_Object = MibTableColumn
frUniDlciTransferPriorityToNetwork = _FrUniDlciTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 37),
    _FrUniDlciTransferPriorityToNetwork_Type()
)
frUniDlciTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTransferPriorityToNetwork.setStatus("obsolete")


class _FrUniDlciTransferPriorityFromNetwork_Type(Integer32):
    """Custom type frUniDlciTransferPriorityFromNetwork based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9))
    )


_FrUniDlciTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_FrUniDlciTransferPriorityFromNetwork_Object = MibTableColumn
frUniDlciTransferPriorityFromNetwork = _FrUniDlciTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 38),
    _FrUniDlciTransferPriorityFromNetwork_Type()
)
frUniDlciTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTransferPriorityFromNetwork.setStatus("obsolete")


class _FrUniDlciCirPresent_Type(Unsigned32):
    """Custom type frUniDlciCirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciCirPresent_Type.__name__ = "Unsigned32"
_FrUniDlciCirPresent_Object = MibTableColumn
frUniDlciCirPresent = _FrUniDlciCirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 39),
    _FrUniDlciCirPresent_Type()
)
frUniDlciCirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciCirPresent.setStatus("mandatory")


class _FrUniDlciEirPresent_Type(Unsigned32):
    """Custom type frUniDlciEirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciEirPresent_Type.__name__ = "Unsigned32"
_FrUniDlciEirPresent_Object = MibTableColumn
frUniDlciEirPresent = _FrUniDlciEirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 15, 1, 40),
    _FrUniDlciEirPresent_Type()
)
frUniDlciEirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciEirPresent.setStatus("mandatory")
_FrUniDlciIntTable_Object = MibTable
frUniDlciIntTable = _FrUniDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16)
)
if mibBuilder.loadTexts:
    frUniDlciIntTable.setStatus("mandatory")
_FrUniDlciIntEntry_Object = MibTableRow
frUniDlciIntEntry = _FrUniDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1)
)
frUniDlciIntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniDlciIndex"),
)
if mibBuilder.loadTexts:
    frUniDlciIntEntry.setStatus("mandatory")


class _FrUniDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type frUniDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrUniDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_FrUniDlciStartTime_Object = MibTableColumn
frUniDlciStartTime = _FrUniDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 1),
    _FrUniDlciStartTime_Type()
)
frUniDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciStartTime.setStatus("mandatory")


class _FrUniDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type frUniDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrUniDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_FrUniDlciTotalIngressBytes_Object = MibTableColumn
frUniDlciTotalIngressBytes = _FrUniDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 2),
    _FrUniDlciTotalIngressBytes_Type()
)
frUniDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTotalIngressBytes.setStatus("mandatory")


class _FrUniDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type frUniDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrUniDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_FrUniDlciTotalEgressBytes_Object = MibTableColumn
frUniDlciTotalEgressBytes = _FrUniDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 3),
    _FrUniDlciTotalEgressBytes_Type()
)
frUniDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTotalEgressBytes.setStatus("mandatory")


class _FrUniDlciEirIngressBytes_Type(Unsigned64):
    """Custom type frUniDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrUniDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_FrUniDlciEirIngressBytes_Object = MibTableColumn
frUniDlciEirIngressBytes = _FrUniDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 4),
    _FrUniDlciEirIngressBytes_Type()
)
frUniDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciEirIngressBytes.setStatus("mandatory")


class _FrUniDlciEirEgressBytes_Type(Unsigned64):
    """Custom type frUniDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrUniDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_FrUniDlciEirEgressBytes_Object = MibTableColumn
frUniDlciEirEgressBytes = _FrUniDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 5),
    _FrUniDlciEirEgressBytes_Type()
)
frUniDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciEirEgressBytes.setStatus("mandatory")


class _FrUniDlciDiscardedBytes_Type(Unsigned64):
    """Custom type frUniDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrUniDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_FrUniDlciDiscardedBytes_Object = MibTableColumn
frUniDlciDiscardedBytes = _FrUniDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 6),
    _FrUniDlciDiscardedBytes_Type()
)
frUniDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscardedBytes.setStatus("mandatory")


class _FrUniDlciTotalIngressSegFrm_Type(Unsigned32):
    """Custom type frUniDlciTotalIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciTotalIngressSegFrm_Type.__name__ = "Unsigned32"
_FrUniDlciTotalIngressSegFrm_Object = MibTableColumn
frUniDlciTotalIngressSegFrm = _FrUniDlciTotalIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 7),
    _FrUniDlciTotalIngressSegFrm_Type()
)
frUniDlciTotalIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTotalIngressSegFrm.setStatus("mandatory")


class _FrUniDlciTotalEgressSegFrm_Type(Unsigned32):
    """Custom type frUniDlciTotalEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciTotalEgressSegFrm_Type.__name__ = "Unsigned32"
_FrUniDlciTotalEgressSegFrm_Object = MibTableColumn
frUniDlciTotalEgressSegFrm = _FrUniDlciTotalEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 8),
    _FrUniDlciTotalEgressSegFrm_Type()
)
frUniDlciTotalEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciTotalEgressSegFrm.setStatus("mandatory")


class _FrUniDlciEirIngressSegFrm_Type(Unsigned32):
    """Custom type frUniDlciEirIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciEirIngressSegFrm_Type.__name__ = "Unsigned32"
_FrUniDlciEirIngressSegFrm_Object = MibTableColumn
frUniDlciEirIngressSegFrm = _FrUniDlciEirIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 9),
    _FrUniDlciEirIngressSegFrm_Type()
)
frUniDlciEirIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciEirIngressSegFrm.setStatus("mandatory")


class _FrUniDlciEirEgressSegFrm_Type(Unsigned32):
    """Custom type frUniDlciEirEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciEirEgressSegFrm_Type.__name__ = "Unsigned32"
_FrUniDlciEirEgressSegFrm_Object = MibTableColumn
frUniDlciEirEgressSegFrm = _FrUniDlciEirEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 10),
    _FrUniDlciEirEgressSegFrm_Type()
)
frUniDlciEirEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciEirEgressSegFrm.setStatus("mandatory")


class _FrUniDlciDiscardedSegFrm_Type(Unsigned32):
    """Custom type frUniDlciDiscardedSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciDiscardedSegFrm_Type.__name__ = "Unsigned32"
_FrUniDlciDiscardedSegFrm_Object = MibTableColumn
frUniDlciDiscardedSegFrm = _FrUniDlciDiscardedSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 11),
    _FrUniDlciDiscardedSegFrm_Type()
)
frUniDlciDiscardedSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciDiscardedSegFrm.setStatus("mandatory")


class _FrUniDlciCirPresentObs_Type(Unsigned32):
    """Custom type frUniDlciCirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciCirPresentObs_Type.__name__ = "Unsigned32"
_FrUniDlciCirPresentObs_Object = MibTableColumn
frUniDlciCirPresentObs = _FrUniDlciCirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 12),
    _FrUniDlciCirPresentObs_Type()
)
frUniDlciCirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciCirPresentObs.setStatus("obsolete")


class _FrUniDlciEirPresentObs_Type(Unsigned32):
    """Custom type frUniDlciEirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciEirPresentObs_Type.__name__ = "Unsigned32"
_FrUniDlciEirPresentObs_Object = MibTableColumn
frUniDlciEirPresentObs = _FrUniDlciEirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 13),
    _FrUniDlciEirPresentObs_Type()
)
frUniDlciEirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciEirPresentObs.setStatus("obsolete")


class _FrUniDlciRateEnforcementPresent_Type(Integer32):
    """Custom type frUniDlciRateEnforcementPresent based on Integer32"""
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


_FrUniDlciRateEnforcementPresent_Type.__name__ = "Integer32"
_FrUniDlciRateEnforcementPresent_Object = MibTableColumn
frUniDlciRateEnforcementPresent = _FrUniDlciRateEnforcementPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 14),
    _FrUniDlciRateEnforcementPresent_Type()
)
frUniDlciRateEnforcementPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciRateEnforcementPresent.setStatus("obsolete")


class _FrUniDlciRateAdaptationPresent_Type(Integer32):
    """Custom type frUniDlciRateAdaptationPresent based on Integer32"""
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


_FrUniDlciRateAdaptationPresent_Type.__name__ = "Integer32"
_FrUniDlciRateAdaptationPresent_Object = MibTableColumn
frUniDlciRateAdaptationPresent = _FrUniDlciRateAdaptationPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 15),
    _FrUniDlciRateAdaptationPresent_Type()
)
frUniDlciRateAdaptationPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciRateAdaptationPresent.setStatus("obsolete")


class _FrUniDlciLocalRateAdaptOccurred_Type(Unsigned32):
    """Custom type frUniDlciLocalRateAdaptOccurred based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FrUniDlciLocalRateAdaptOccurred_Type.__name__ = "Unsigned32"
_FrUniDlciLocalRateAdaptOccurred_Object = MibTableColumn
frUniDlciLocalRateAdaptOccurred = _FrUniDlciLocalRateAdaptOccurred_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 16),
    _FrUniDlciLocalRateAdaptOccurred_Type()
)
frUniDlciLocalRateAdaptOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciLocalRateAdaptOccurred.setStatus("mandatory")


class _FrUniDlciCallReferenceNumber_Type(Unsigned32):
    """Custom type frUniDlciCallReferenceNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciCallReferenceNumber_Type.__name__ = "Unsigned32"
_FrUniDlciCallReferenceNumber_Object = MibTableColumn
frUniDlciCallReferenceNumber = _FrUniDlciCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 17),
    _FrUniDlciCallReferenceNumber_Type()
)
frUniDlciCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciCallReferenceNumber.setStatus("mandatory")


class _FrUniDlciElapsedDifference_Type(Unsigned32):
    """Custom type frUniDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniDlciElapsedDifference_Type.__name__ = "Unsigned32"
_FrUniDlciElapsedDifference_Object = MibTableColumn
frUniDlciElapsedDifference = _FrUniDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 5, 16, 1, 18),
    _FrUniDlciElapsedDifference_Type()
)
frUniDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniDlciElapsedDifference.setStatus("mandatory")
_FrUniSig_ObjectIdentity = ObjectIdentity
frUniSig = _FrUniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6)
)
_FrUniSigRowStatusTable_Object = MibTable
frUniSigRowStatusTable = _FrUniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 1)
)
if mibBuilder.loadTexts:
    frUniSigRowStatusTable.setStatus("mandatory")
_FrUniSigRowStatusEntry_Object = MibTableRow
frUniSigRowStatusEntry = _FrUniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 1, 1)
)
frUniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigRowStatusEntry.setStatus("mandatory")
_FrUniSigRowStatus_Type = RowStatus
_FrUniSigRowStatus_Object = MibTableColumn
frUniSigRowStatus = _FrUniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 1, 1, 1),
    _FrUniSigRowStatus_Type()
)
frUniSigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigRowStatus.setStatus("mandatory")
_FrUniSigComponentName_Type = DisplayString
_FrUniSigComponentName_Object = MibTableColumn
frUniSigComponentName = _FrUniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 1, 1, 2),
    _FrUniSigComponentName_Type()
)
frUniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigComponentName.setStatus("mandatory")
_FrUniSigStorageType_Type = StorageType
_FrUniSigStorageType_Object = MibTableColumn
frUniSigStorageType = _FrUniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 1, 1, 4),
    _FrUniSigStorageType_Type()
)
frUniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigStorageType.setStatus("mandatory")
_FrUniSigIndex_Type = NonReplicated
_FrUniSigIndex_Object = MibTableColumn
frUniSigIndex = _FrUniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 1, 1, 10),
    _FrUniSigIndex_Type()
)
frUniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniSigIndex.setStatus("mandatory")
_FrUniSigRangeTable_Object = MibTable
frUniSigRangeTable = _FrUniSigRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 11)
)
if mibBuilder.loadTexts:
    frUniSigRangeTable.setStatus("mandatory")
_FrUniSigRangeEntry_Object = MibTableRow
frUniSigRangeEntry = _FrUniSigRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 11, 1)
)
frUniSigRangeEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigRangeEntry.setStatus("mandatory")


class _FrUniSigHighestPvcDlci_Type(Unsigned32):
    """Custom type frUniSigHighestPvcDlci based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_FrUniSigHighestPvcDlci_Type.__name__ = "Unsigned32"
_FrUniSigHighestPvcDlci_Object = MibTableColumn
frUniSigHighestPvcDlci = _FrUniSigHighestPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 11, 1, 1),
    _FrUniSigHighestPvcDlci_Type()
)
frUniSigHighestPvcDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigHighestPvcDlci.setStatus("mandatory")
_FrUniSigServParmsTable_Object = MibTable
frUniSigServParmsTable = _FrUniSigServParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12)
)
if mibBuilder.loadTexts:
    frUniSigServParmsTable.setStatus("mandatory")
_FrUniSigServParmsEntry_Object = MibTableRow
frUniSigServParmsEntry = _FrUniSigServParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1)
)
frUniSigServParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigServParmsEntry.setStatus("mandatory")


class _FrUniSigMaximumAggregateSvcCir_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcCir based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FrUniSigMaximumAggregateSvcCir_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcCir_Object = MibTableColumn
frUniSigMaximumAggregateSvcCir = _FrUniSigMaximumAggregateSvcCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 1),
    _FrUniSigMaximumAggregateSvcCir_Type()
)
frUniSigMaximumAggregateSvcCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcCir.setStatus("obsolete")


class _FrUniSigMaximumAggregateSvcEir_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcEir based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigMaximumAggregateSvcEir_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcEir_Object = MibTableColumn
frUniSigMaximumAggregateSvcEir = _FrUniSigMaximumAggregateSvcEir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 2),
    _FrUniSigMaximumAggregateSvcEir_Type()
)
frUniSigMaximumAggregateSvcEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcEir.setStatus("obsolete")


class _FrUniSigMaximumFrameSize_Type(Unsigned32):
    """Custom type frUniSigMaximumFrameSize based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrUniSigMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrUniSigMaximumFrameSize_Object = MibTableColumn
frUniSigMaximumFrameSize = _FrUniSigMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 3),
    _FrUniSigMaximumFrameSize_Type()
)
frUniSigMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumFrameSize.setStatus("mandatory")


class _FrUniSigDefaultMaximumFrameSize_Type(Unsigned32):
    """Custom type frUniSigDefaultMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrUniSigDefaultMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrUniSigDefaultMaximumFrameSize_Object = MibTableColumn
frUniSigDefaultMaximumFrameSize = _FrUniSigDefaultMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 4),
    _FrUniSigDefaultMaximumFrameSize_Type()
)
frUniSigDefaultMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigDefaultMaximumFrameSize.setStatus("mandatory")


class _FrUniSigDefaultCommittedInformationRate_Type(Unsigned32):
    """Custom type frUniSigDefaultCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_FrUniSigDefaultCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrUniSigDefaultCommittedInformationRate_Object = MibTableColumn
frUniSigDefaultCommittedInformationRate = _FrUniSigDefaultCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 5),
    _FrUniSigDefaultCommittedInformationRate_Type()
)
frUniSigDefaultCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigDefaultCommittedInformationRate.setStatus("mandatory")


class _FrUniSigDefaultCommittedBurstSize_Type(Unsigned32):
    """Custom type frUniSigDefaultCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_FrUniSigDefaultCommittedBurstSize_Type.__name__ = "Unsigned32"
_FrUniSigDefaultCommittedBurstSize_Object = MibTableColumn
frUniSigDefaultCommittedBurstSize = _FrUniSigDefaultCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 6),
    _FrUniSigDefaultCommittedBurstSize_Type()
)
frUniSigDefaultCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigDefaultCommittedBurstSize.setStatus("mandatory")


class _FrUniSigDefaultExcessBurstSize_Type(Unsigned32):
    """Custom type frUniSigDefaultExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_FrUniSigDefaultExcessBurstSize_Type.__name__ = "Unsigned32"
_FrUniSigDefaultExcessBurstSize_Object = MibTableColumn
frUniSigDefaultExcessBurstSize = _FrUniSigDefaultExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 7),
    _FrUniSigDefaultExcessBurstSize_Type()
)
frUniSigDefaultExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigDefaultExcessBurstSize.setStatus("mandatory")


class _FrUniSigUnlimitedAggregateEir_Type(Integer32):
    """Custom type frUniSigUnlimitedAggregateEir based on Integer32"""
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


_FrUniSigUnlimitedAggregateEir_Type.__name__ = "Integer32"
_FrUniSigUnlimitedAggregateEir_Object = MibTableColumn
frUniSigUnlimitedAggregateEir = _FrUniSigUnlimitedAggregateEir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 8),
    _FrUniSigUnlimitedAggregateEir_Type()
)
frUniSigUnlimitedAggregateEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigUnlimitedAggregateEir.setStatus("mandatory")


class _FrUniSigRateEnforcement_Type(Integer32):
    """Custom type frUniSigRateEnforcement based on Integer32"""
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


_FrUniSigRateEnforcement_Type.__name__ = "Integer32"
_FrUniSigRateEnforcement_Object = MibTableColumn
frUniSigRateEnforcement = _FrUniSigRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 9),
    _FrUniSigRateEnforcement_Type()
)
frUniSigRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigRateEnforcement.setStatus("mandatory")


class _FrUniSigRateAdaptation_Type(Integer32):
    """Custom type frUniSigRateAdaptation based on Integer32"""
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
        *(("cirProportionate", 3),
          ("eirOnly", 2),
          ("off", 0),
          ("on", 1))
    )


_FrUniSigRateAdaptation_Type.__name__ = "Integer32"
_FrUniSigRateAdaptation_Object = MibTableColumn
frUniSigRateAdaptation = _FrUniSigRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 10),
    _FrUniSigRateAdaptation_Type()
)
frUniSigRateAdaptation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigRateAdaptation.setStatus("mandatory")


class _FrUniSigMaximumAggregateSvcCirNormalQ_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcCirNormalQ based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FrUniSigMaximumAggregateSvcCirNormalQ_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcCirNormalQ_Object = MibTableColumn
frUniSigMaximumAggregateSvcCirNormalQ = _FrUniSigMaximumAggregateSvcCirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 11),
    _FrUniSigMaximumAggregateSvcCirNormalQ_Type()
)
frUniSigMaximumAggregateSvcCirNormalQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcCirNormalQ.setStatus("mandatory")


class _FrUniSigMaximumAggregateSvcCirHighQ_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcCirHighQ based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FrUniSigMaximumAggregateSvcCirHighQ_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcCirHighQ_Object = MibTableColumn
frUniSigMaximumAggregateSvcCirHighQ = _FrUniSigMaximumAggregateSvcCirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 12),
    _FrUniSigMaximumAggregateSvcCirHighQ_Type()
)
frUniSigMaximumAggregateSvcCirHighQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcCirHighQ.setStatus("mandatory")


class _FrUniSigMaximumAggregateSvcCirInterruptQ_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcCirInterruptQ based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FrUniSigMaximumAggregateSvcCirInterruptQ_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcCirInterruptQ_Object = MibTableColumn
frUniSigMaximumAggregateSvcCirInterruptQ = _FrUniSigMaximumAggregateSvcCirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 13),
    _FrUniSigMaximumAggregateSvcCirInterruptQ_Type()
)
frUniSigMaximumAggregateSvcCirInterruptQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcCirInterruptQ.setStatus("mandatory")


class _FrUniSigMaximumAggregateSvcEirNormalQ_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcEirNormalQ based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigMaximumAggregateSvcEirNormalQ_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcEirNormalQ_Object = MibTableColumn
frUniSigMaximumAggregateSvcEirNormalQ = _FrUniSigMaximumAggregateSvcEirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 14),
    _FrUniSigMaximumAggregateSvcEirNormalQ_Type()
)
frUniSigMaximumAggregateSvcEirNormalQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcEirNormalQ.setStatus("mandatory")


class _FrUniSigMaximumAggregateSvcEirHighQ_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcEirHighQ based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigMaximumAggregateSvcEirHighQ_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcEirHighQ_Object = MibTableColumn
frUniSigMaximumAggregateSvcEirHighQ = _FrUniSigMaximumAggregateSvcEirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 15),
    _FrUniSigMaximumAggregateSvcEirHighQ_Type()
)
frUniSigMaximumAggregateSvcEirHighQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcEirHighQ.setStatus("mandatory")


class _FrUniSigMaximumAggregateSvcEirInterruptQ_Type(Unsigned32):
    """Custom type frUniSigMaximumAggregateSvcEirInterruptQ based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigMaximumAggregateSvcEirInterruptQ_Type.__name__ = "Unsigned32"
_FrUniSigMaximumAggregateSvcEirInterruptQ_Object = MibTableColumn
frUniSigMaximumAggregateSvcEirInterruptQ = _FrUniSigMaximumAggregateSvcEirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 16),
    _FrUniSigMaximumAggregateSvcEirInterruptQ_Type()
)
frUniSigMaximumAggregateSvcEirInterruptQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigMaximumAggregateSvcEirInterruptQ.setStatus("mandatory")


class _FrUniSigX213IeHandling_Type(Integer32):
    """Custom type frUniSigX213IeHandling based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("proprietary", 1))
    )


_FrUniSigX213IeHandling_Type.__name__ = "Integer32"
_FrUniSigX213IeHandling_Object = MibTableColumn
frUniSigX213IeHandling = _FrUniSigX213IeHandling_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 17),
    _FrUniSigX213IeHandling_Type()
)
frUniSigX213IeHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigX213IeHandling.setStatus("mandatory")


class _FrUniSigRaSensitivity_Type(Unsigned32):
    """Custom type frUniSigRaSensitivity based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FrUniSigRaSensitivity_Type.__name__ = "Unsigned32"
_FrUniSigRaSensitivity_Object = MibTableColumn
frUniSigRaSensitivity = _FrUniSigRaSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 18),
    _FrUniSigRaSensitivity_Type()
)
frUniSigRaSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigRaSensitivity.setStatus("mandatory")


class _FrUniSigUpdateBCI_Type(Integer32):
    """Custom type frUniSigUpdateBCI based on Integer32"""
    defaultValue = 0

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


_FrUniSigUpdateBCI_Type.__name__ = "Integer32"
_FrUniSigUpdateBCI_Object = MibTableColumn
frUniSigUpdateBCI = _FrUniSigUpdateBCI_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 19),
    _FrUniSigUpdateBCI_Type()
)
frUniSigUpdateBCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigUpdateBCI.setStatus("mandatory")


class _FrUniSigDefaultLocCheck_Type(Integer32):
    """Custom type frUniSigDefaultLocCheck based on Integer32"""
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


_FrUniSigDefaultLocCheck_Type.__name__ = "Integer32"
_FrUniSigDefaultLocCheck_Object = MibTableColumn
frUniSigDefaultLocCheck = _FrUniSigDefaultLocCheck_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 12, 1, 20),
    _FrUniSigDefaultLocCheck_Type()
)
frUniSigDefaultLocCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigDefaultLocCheck.setStatus("mandatory")
_FrUniSigSysParmsTable_Object = MibTable
frUniSigSysParmsTable = _FrUniSigSysParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 13)
)
if mibBuilder.loadTexts:
    frUniSigSysParmsTable.setStatus("mandatory")
_FrUniSigSysParmsEntry_Object = MibTableRow
frUniSigSysParmsEntry = _FrUniSigSysParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 13, 1)
)
frUniSigSysParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigSysParmsEntry.setStatus("mandatory")


class _FrUniSigCallSetupTimer_Type(Unsigned32):
    """Custom type frUniSigCallSetupTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrUniSigCallSetupTimer_Type.__name__ = "Unsigned32"
_FrUniSigCallSetupTimer_Object = MibTableColumn
frUniSigCallSetupTimer = _FrUniSigCallSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 13, 1, 1),
    _FrUniSigCallSetupTimer_Type()
)
frUniSigCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigCallSetupTimer.setStatus("mandatory")


class _FrUniSigDisconnectTimer_Type(Unsigned32):
    """Custom type frUniSigDisconnectTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrUniSigDisconnectTimer_Type.__name__ = "Unsigned32"
_FrUniSigDisconnectTimer_Object = MibTableColumn
frUniSigDisconnectTimer = _FrUniSigDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 13, 1, 2),
    _FrUniSigDisconnectTimer_Type()
)
frUniSigDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigDisconnectTimer.setStatus("mandatory")


class _FrUniSigReleaseTimer_Type(Unsigned32):
    """Custom type frUniSigReleaseTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrUniSigReleaseTimer_Type.__name__ = "Unsigned32"
_FrUniSigReleaseTimer_Object = MibTableColumn
frUniSigReleaseTimer = _FrUniSigReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 13, 1, 3),
    _FrUniSigReleaseTimer_Type()
)
frUniSigReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigReleaseTimer.setStatus("mandatory")


class _FrUniSigCallProceedingTimer_Type(Unsigned32):
    """Custom type frUniSigCallProceedingTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrUniSigCallProceedingTimer_Type.__name__ = "Unsigned32"
_FrUniSigCallProceedingTimer_Object = MibTableColumn
frUniSigCallProceedingTimer = _FrUniSigCallProceedingTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 13, 1, 4),
    _FrUniSigCallProceedingTimer_Type()
)
frUniSigCallProceedingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigCallProceedingTimer.setStatus("mandatory")


class _FrUniSigNetworkType_Type(Integer32):
    """Custom type frUniSigNetworkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("public", 2))
    )


_FrUniSigNetworkType_Type.__name__ = "Integer32"
_FrUniSigNetworkType_Object = MibTableColumn
frUniSigNetworkType = _FrUniSigNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 13, 1, 5),
    _FrUniSigNetworkType_Type()
)
frUniSigNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigNetworkType.setStatus("mandatory")
_FrUniSigLapfSysTable_Object = MibTable
frUniSigLapfSysTable = _FrUniSigLapfSysTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 14)
)
if mibBuilder.loadTexts:
    frUniSigLapfSysTable.setStatus("mandatory")
_FrUniSigLapfSysEntry_Object = MibTableRow
frUniSigLapfSysEntry = _FrUniSigLapfSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 14, 1)
)
frUniSigLapfSysEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigLapfSysEntry.setStatus("mandatory")


class _FrUniSigWindowSize_Type(Unsigned32):
    """Custom type frUniSigWindowSize based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_FrUniSigWindowSize_Type.__name__ = "Unsigned32"
_FrUniSigWindowSize_Object = MibTableColumn
frUniSigWindowSize = _FrUniSigWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 14, 1, 2),
    _FrUniSigWindowSize_Type()
)
frUniSigWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigWindowSize.setStatus("mandatory")


class _FrUniSigRetransmitLimit_Type(Unsigned32):
    """Custom type frUniSigRetransmitLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_FrUniSigRetransmitLimit_Type.__name__ = "Unsigned32"
_FrUniSigRetransmitLimit_Object = MibTableColumn
frUniSigRetransmitLimit = _FrUniSigRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 14, 1, 3),
    _FrUniSigRetransmitLimit_Type()
)
frUniSigRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigRetransmitLimit.setStatus("mandatory")


class _FrUniSigAckTimer_Type(Unsigned32):
    """Custom type frUniSigAckTimer based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_FrUniSigAckTimer_Type.__name__ = "Unsigned32"
_FrUniSigAckTimer_Object = MibTableColumn
frUniSigAckTimer = _FrUniSigAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 14, 1, 4),
    _FrUniSigAckTimer_Type()
)
frUniSigAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigAckTimer.setStatus("mandatory")


class _FrUniSigAckDelayTimer_Type(Unsigned32):
    """Custom type frUniSigAckDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_FrUniSigAckDelayTimer_Type.__name__ = "Unsigned32"
_FrUniSigAckDelayTimer_Object = MibTableColumn
frUniSigAckDelayTimer = _FrUniSigAckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 14, 1, 5),
    _FrUniSigAckDelayTimer_Type()
)
frUniSigAckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigAckDelayTimer.setStatus("mandatory")


class _FrUniSigIdleProbeTimer_Type(Unsigned32):
    """Custom type frUniSigIdleProbeTimer based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_FrUniSigIdleProbeTimer_Type.__name__ = "Unsigned32"
_FrUniSigIdleProbeTimer_Object = MibTableColumn
frUniSigIdleProbeTimer = _FrUniSigIdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 14, 1, 6),
    _FrUniSigIdleProbeTimer_Type()
)
frUniSigIdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigIdleProbeTimer.setStatus("mandatory")
_FrUniSigStateTable_Object = MibTable
frUniSigStateTable = _FrUniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 15)
)
if mibBuilder.loadTexts:
    frUniSigStateTable.setStatus("mandatory")
_FrUniSigStateEntry_Object = MibTableRow
frUniSigStateEntry = _FrUniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 15, 1)
)
frUniSigStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigStateEntry.setStatus("mandatory")


class _FrUniSigAdminState_Type(Integer32):
    """Custom type frUniSigAdminState based on Integer32"""
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


_FrUniSigAdminState_Type.__name__ = "Integer32"
_FrUniSigAdminState_Object = MibTableColumn
frUniSigAdminState = _FrUniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 15, 1, 1),
    _FrUniSigAdminState_Type()
)
frUniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigAdminState.setStatus("mandatory")


class _FrUniSigOperationalState_Type(Integer32):
    """Custom type frUniSigOperationalState based on Integer32"""
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


_FrUniSigOperationalState_Type.__name__ = "Integer32"
_FrUniSigOperationalState_Object = MibTableColumn
frUniSigOperationalState = _FrUniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 15, 1, 2),
    _FrUniSigOperationalState_Type()
)
frUniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigOperationalState.setStatus("mandatory")


class _FrUniSigUsageState_Type(Integer32):
    """Custom type frUniSigUsageState based on Integer32"""
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


_FrUniSigUsageState_Type.__name__ = "Integer32"
_FrUniSigUsageState_Object = MibTableColumn
frUniSigUsageState = _FrUniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 15, 1, 3),
    _FrUniSigUsageState_Type()
)
frUniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigUsageState.setStatus("mandatory")
_FrUniSigStatsTable_Object = MibTable
frUniSigStatsTable = _FrUniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16)
)
if mibBuilder.loadTexts:
    frUniSigStatsTable.setStatus("mandatory")
_FrUniSigStatsEntry_Object = MibTableRow
frUniSigStatsEntry = _FrUniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1)
)
frUniSigStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigStatsEntry.setStatus("mandatory")


class _FrUniSigCurrentNumberOfSvcCalls_Type(Unsigned32):
    """Custom type frUniSigCurrentNumberOfSvcCalls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_FrUniSigCurrentNumberOfSvcCalls_Type.__name__ = "Unsigned32"
_FrUniSigCurrentNumberOfSvcCalls_Object = MibTableColumn
frUniSigCurrentNumberOfSvcCalls = _FrUniSigCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 1),
    _FrUniSigCurrentNumberOfSvcCalls_Type()
)
frUniSigCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentNumberOfSvcCalls.setStatus("mandatory")
_FrUniSigInCalls_Type = Counter32
_FrUniSigInCalls_Object = MibTableColumn
frUniSigInCalls = _FrUniSigInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 4),
    _FrUniSigInCalls_Type()
)
frUniSigInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigInCalls.setStatus("mandatory")
_FrUniSigInCallsRefused_Type = Counter32
_FrUniSigInCallsRefused_Object = MibTableColumn
frUniSigInCallsRefused = _FrUniSigInCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 5),
    _FrUniSigInCallsRefused_Type()
)
frUniSigInCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigInCallsRefused.setStatus("mandatory")
_FrUniSigOutCalls_Type = Counter32
_FrUniSigOutCalls_Object = MibTableColumn
frUniSigOutCalls = _FrUniSigOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 6),
    _FrUniSigOutCalls_Type()
)
frUniSigOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigOutCalls.setStatus("mandatory")
_FrUniSigOutCallsFailed_Type = Counter32
_FrUniSigOutCallsFailed_Object = MibTableColumn
frUniSigOutCallsFailed = _FrUniSigOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 7),
    _FrUniSigOutCallsFailed_Type()
)
frUniSigOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigOutCallsFailed.setStatus("mandatory")
_FrUniSigProtocolErrors_Type = Counter32
_FrUniSigProtocolErrors_Object = MibTableColumn
frUniSigProtocolErrors = _FrUniSigProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 8),
    _FrUniSigProtocolErrors_Type()
)
frUniSigProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigProtocolErrors.setStatus("mandatory")
_FrUniSigQualityOfServiceNotAvailable_Type = Counter32
_FrUniSigQualityOfServiceNotAvailable_Object = MibTableColumn
frUniSigQualityOfServiceNotAvailable = _FrUniSigQualityOfServiceNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 9),
    _FrUniSigQualityOfServiceNotAvailable_Type()
)
frUniSigQualityOfServiceNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigQualityOfServiceNotAvailable.setStatus("mandatory")
_FrUniSigSetupTimeout_Type = Counter32
_FrUniSigSetupTimeout_Object = MibTableColumn
frUniSigSetupTimeout = _FrUniSigSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 10),
    _FrUniSigSetupTimeout_Type()
)
frUniSigSetupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigSetupTimeout.setStatus("mandatory")


class _FrUniSigLastCauseInStatusMsgReceived_Type(Unsigned32):
    """Custom type frUniSigLastCauseInStatusMsgReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniSigLastCauseInStatusMsgReceived_Type.__name__ = "Unsigned32"
_FrUniSigLastCauseInStatusMsgReceived_Object = MibTableColumn
frUniSigLastCauseInStatusMsgReceived = _FrUniSigLastCauseInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 11),
    _FrUniSigLastCauseInStatusMsgReceived_Type()
)
frUniSigLastCauseInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastCauseInStatusMsgReceived.setStatus("mandatory")


class _FrUniSigLastStateInStatusMsgReceived_Type(Integer32):
    """Custom type frUniSigLastStateInStatusMsgReceived based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("disconnectIndication", 12),
          ("disconnectRequest", 11),
          ("incomingCallProceeding", 9),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n16", 16),
          ("n17", 17),
          ("n18", 18),
          ("n2", 2),
          ("n21", 21),
          ("n22", 22),
          ("n23", 23),
          ("n24", 24),
          ("n25", 25),
          ("n26", 26),
          ("n27", 27),
          ("n28", 28),
          ("n29", 29),
          ("n30", 30),
          ("n31", 31),
          ("n32", 32),
          ("n33", 33),
          ("n34", 34),
          ("n35", 35),
          ("n36", 36),
          ("n37", 37),
          ("n38", 38),
          ("n39", 39),
          ("n4", 4),
          ("n40", 40),
          ("n41", 41),
          ("n42", 42),
          ("n43", 43),
          ("n44", 44),
          ("n45", 45),
          ("n46", 46),
          ("n47", 47),
          ("n48", 48),
          ("n49", 49),
          ("n5", 5),
          ("n50", 50),
          ("n51", 51),
          ("n52", 52),
          ("n53", 53),
          ("n54", 54),
          ("n55", 55),
          ("n56", 56),
          ("n57", 57),
          ("n58", 58),
          ("n59", 59),
          ("n60", 60),
          ("n61", 61),
          ("n62", 62),
          ("n63", 63),
          ("n7", 7),
          ("n8", 8),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseRequest", 19))
    )


_FrUniSigLastStateInStatusMsgReceived_Type.__name__ = "Integer32"
_FrUniSigLastStateInStatusMsgReceived_Object = MibTableColumn
frUniSigLastStateInStatusMsgReceived = _FrUniSigLastStateInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 12),
    _FrUniSigLastStateInStatusMsgReceived_Type()
)
frUniSigLastStateInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastStateInStatusMsgReceived.setStatus("mandatory")


class _FrUniSigLastDlciReceivedStatus_Type(Unsigned32):
    """Custom type frUniSigLastDlciReceivedStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_FrUniSigLastDlciReceivedStatus_Type.__name__ = "Unsigned32"
_FrUniSigLastDlciReceivedStatus_Object = MibTableColumn
frUniSigLastDlciReceivedStatus = _FrUniSigLastDlciReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 13),
    _FrUniSigLastDlciReceivedStatus_Type()
)
frUniSigLastDlciReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastDlciReceivedStatus.setStatus("mandatory")


class _FrUniSigLastQ933StateReceivedStatus_Type(Integer32):
    """Custom type frUniSigLastQ933StateReceivedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              6,
              9,
              10,
              11,
              12,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("disconnectIndication", 12),
          ("disconnectRequest", 11),
          ("incomingCallProceeding", 9),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseRequest", 19))
    )


_FrUniSigLastQ933StateReceivedStatus_Type.__name__ = "Integer32"
_FrUniSigLastQ933StateReceivedStatus_Object = MibTableColumn
frUniSigLastQ933StateReceivedStatus = _FrUniSigLastQ933StateReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 14),
    _FrUniSigLastQ933StateReceivedStatus_Type()
)
frUniSigLastQ933StateReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastQ933StateReceivedStatus.setStatus("mandatory")


class _FrUniSigLastTimeMsgBlockCongested_Type(EnterpriseDateAndTime):
    """Custom type frUniSigLastTimeMsgBlockCongested based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_FrUniSigLastTimeMsgBlockCongested_Type.__name__ = "EnterpriseDateAndTime"
_FrUniSigLastTimeMsgBlockCongested_Object = MibTableColumn
frUniSigLastTimeMsgBlockCongested = _FrUniSigLastTimeMsgBlockCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 15),
    _FrUniSigLastTimeMsgBlockCongested_Type()
)
frUniSigLastTimeMsgBlockCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastTimeMsgBlockCongested.setStatus("mandatory")


class _FrUniSigLastDlciWithMsgBlockCongestion_Type(Unsigned32):
    """Custom type frUniSigLastDlciWithMsgBlockCongestion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_FrUniSigLastDlciWithMsgBlockCongestion_Type.__name__ = "Unsigned32"
_FrUniSigLastDlciWithMsgBlockCongestion_Object = MibTableColumn
frUniSigLastDlciWithMsgBlockCongestion = _FrUniSigLastDlciWithMsgBlockCongestion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 16),
    _FrUniSigLastDlciWithMsgBlockCongestion_Type()
)
frUniSigLastDlciWithMsgBlockCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastDlciWithMsgBlockCongestion.setStatus("mandatory")


class _FrUniSigCurrentAggregateSvcCirNormalQ_Type(Unsigned32):
    """Custom type frUniSigCurrentAggregateSvcCirNormalQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigCurrentAggregateSvcCirNormalQ_Type.__name__ = "Unsigned32"
_FrUniSigCurrentAggregateSvcCirNormalQ_Object = MibTableColumn
frUniSigCurrentAggregateSvcCirNormalQ = _FrUniSigCurrentAggregateSvcCirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 17),
    _FrUniSigCurrentAggregateSvcCirNormalQ_Type()
)
frUniSigCurrentAggregateSvcCirNormalQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentAggregateSvcCirNormalQ.setStatus("mandatory")


class _FrUniSigCurrentAggregateSvcCirHighQ_Type(Unsigned32):
    """Custom type frUniSigCurrentAggregateSvcCirHighQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigCurrentAggregateSvcCirHighQ_Type.__name__ = "Unsigned32"
_FrUniSigCurrentAggregateSvcCirHighQ_Object = MibTableColumn
frUniSigCurrentAggregateSvcCirHighQ = _FrUniSigCurrentAggregateSvcCirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 18),
    _FrUniSigCurrentAggregateSvcCirHighQ_Type()
)
frUniSigCurrentAggregateSvcCirHighQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentAggregateSvcCirHighQ.setStatus("mandatory")


class _FrUniSigCurrentAggregateSvcCirInterruptQ_Type(Unsigned32):
    """Custom type frUniSigCurrentAggregateSvcCirInterruptQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigCurrentAggregateSvcCirInterruptQ_Type.__name__ = "Unsigned32"
_FrUniSigCurrentAggregateSvcCirInterruptQ_Object = MibTableColumn
frUniSigCurrentAggregateSvcCirInterruptQ = _FrUniSigCurrentAggregateSvcCirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 19),
    _FrUniSigCurrentAggregateSvcCirInterruptQ_Type()
)
frUniSigCurrentAggregateSvcCirInterruptQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentAggregateSvcCirInterruptQ.setStatus("mandatory")


class _FrUniSigCurrentAggregateSvcEirNormalQ_Type(Unsigned32):
    """Custom type frUniSigCurrentAggregateSvcEirNormalQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigCurrentAggregateSvcEirNormalQ_Type.__name__ = "Unsigned32"
_FrUniSigCurrentAggregateSvcEirNormalQ_Object = MibTableColumn
frUniSigCurrentAggregateSvcEirNormalQ = _FrUniSigCurrentAggregateSvcEirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 20),
    _FrUniSigCurrentAggregateSvcEirNormalQ_Type()
)
frUniSigCurrentAggregateSvcEirNormalQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentAggregateSvcEirNormalQ.setStatus("mandatory")


class _FrUniSigCurrentAggregateSvcEirHighQ_Type(Unsigned32):
    """Custom type frUniSigCurrentAggregateSvcEirHighQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigCurrentAggregateSvcEirHighQ_Type.__name__ = "Unsigned32"
_FrUniSigCurrentAggregateSvcEirHighQ_Object = MibTableColumn
frUniSigCurrentAggregateSvcEirHighQ = _FrUniSigCurrentAggregateSvcEirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 21),
    _FrUniSigCurrentAggregateSvcEirHighQ_Type()
)
frUniSigCurrentAggregateSvcEirHighQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentAggregateSvcEirHighQ.setStatus("mandatory")


class _FrUniSigCurrentAggregateSvcEirInterruptQ_Type(Unsigned32):
    """Custom type frUniSigCurrentAggregateSvcEirInterruptQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniSigCurrentAggregateSvcEirInterruptQ_Type.__name__ = "Unsigned32"
_FrUniSigCurrentAggregateSvcEirInterruptQ_Object = MibTableColumn
frUniSigCurrentAggregateSvcEirInterruptQ = _FrUniSigCurrentAggregateSvcEirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 16, 1, 22),
    _FrUniSigCurrentAggregateSvcEirInterruptQ_Type()
)
frUniSigCurrentAggregateSvcEirInterruptQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentAggregateSvcEirInterruptQ.setStatus("mandatory")
_FrUniSigLapfStatusTable_Object = MibTable
frUniSigLapfStatusTable = _FrUniSigLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 17)
)
if mibBuilder.loadTexts:
    frUniSigLapfStatusTable.setStatus("mandatory")
_FrUniSigLapfStatusEntry_Object = MibTableRow
frUniSigLapfStatusEntry = _FrUniSigLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 17, 1)
)
frUniSigLapfStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigLapfStatusEntry.setStatus("mandatory")


class _FrUniSigCurrentState_Type(Integer32):
    """Custom type frUniSigCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disconnectRequest", 4),
          ("disconnected", 1),
          ("informationTransfer", 5),
          ("linkSetup", 2),
          ("waitingAck", 7))
    )


_FrUniSigCurrentState_Type.__name__ = "Integer32"
_FrUniSigCurrentState_Object = MibTableColumn
frUniSigCurrentState = _FrUniSigCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 17, 1, 1),
    _FrUniSigCurrentState_Type()
)
frUniSigCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentState.setStatus("mandatory")


class _FrUniSigLastStateChangeReason_Type(Integer32):
    """Custom type frUniSigLastStateChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("abmeEntered", 3),
          ("abmeReset", 5),
          ("discReceived", 8),
          ("discSent", 9),
          ("dmReceived", 6),
          ("dmSent", 7),
          ("frmrReceived", 10),
          ("n200RetranTimeOut", 12),
          ("notStarted", 1),
          ("other", 13))
    )


_FrUniSigLastStateChangeReason_Type.__name__ = "Integer32"
_FrUniSigLastStateChangeReason_Object = MibTableColumn
frUniSigLastStateChangeReason = _FrUniSigLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 17, 1, 2),
    _FrUniSigLastStateChangeReason_Type()
)
frUniSigLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastStateChangeReason.setStatus("mandatory")


class _FrUniSigFrmrReceive_Type(HexString):
    """Custom type frUniSigFrmrReceive based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FrUniSigFrmrReceive_Type.__name__ = "HexString"
_FrUniSigFrmrReceive_Object = MibTableColumn
frUniSigFrmrReceive = _FrUniSigFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 17, 1, 3),
    _FrUniSigFrmrReceive_Type()
)
frUniSigFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigFrmrReceive.setStatus("mandatory")
_FrUniSigCurrentQueueSize_Type = Counter32
_FrUniSigCurrentQueueSize_Object = MibTableColumn
frUniSigCurrentQueueSize = _FrUniSigCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 17, 1, 4),
    _FrUniSigCurrentQueueSize_Type()
)
frUniSigCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigCurrentQueueSize.setStatus("mandatory")
_FrUniSigLapfStatsTable_Object = MibTable
frUniSigLapfStatsTable = _FrUniSigLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18)
)
if mibBuilder.loadTexts:
    frUniSigLapfStatsTable.setStatus("mandatory")
_FrUniSigLapfStatsEntry_Object = MibTableRow
frUniSigLapfStatsEntry = _FrUniSigLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1)
)
frUniSigLapfStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigLapfStatsEntry.setStatus("mandatory")
_FrUniSigStateChange_Type = Counter32
_FrUniSigStateChange_Object = MibTableColumn
frUniSigStateChange = _FrUniSigStateChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 1),
    _FrUniSigStateChange_Type()
)
frUniSigStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigStateChange.setStatus("mandatory")
_FrUniSigRemoteBusy_Type = Counter32
_FrUniSigRemoteBusy_Object = MibTableColumn
frUniSigRemoteBusy = _FrUniSigRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 2),
    _FrUniSigRemoteBusy_Type()
)
frUniSigRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigRemoteBusy.setStatus("mandatory")
_FrUniSigReceiveRejectFrame_Type = Counter32
_FrUniSigReceiveRejectFrame_Object = MibTableColumn
frUniSigReceiveRejectFrame = _FrUniSigReceiveRejectFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 3),
    _FrUniSigReceiveRejectFrame_Type()
)
frUniSigReceiveRejectFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigReceiveRejectFrame.setStatus("mandatory")
_FrUniSigAckTimeout_Type = Counter32
_FrUniSigAckTimeout_Object = MibTableColumn
frUniSigAckTimeout = _FrUniSigAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 4),
    _FrUniSigAckTimeout_Type()
)
frUniSigAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigAckTimeout.setStatus("mandatory")
_FrUniSigIFramesTransmitted_Type = Counter32
_FrUniSigIFramesTransmitted_Object = MibTableColumn
frUniSigIFramesTransmitted = _FrUniSigIFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 5),
    _FrUniSigIFramesTransmitted_Type()
)
frUniSigIFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigIFramesTransmitted.setStatus("mandatory")
_FrUniSigIFramesTxDiscarded_Type = Counter32
_FrUniSigIFramesTxDiscarded_Object = MibTableColumn
frUniSigIFramesTxDiscarded = _FrUniSigIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 6),
    _FrUniSigIFramesTxDiscarded_Type()
)
frUniSigIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigIFramesTxDiscarded.setStatus("mandatory")
_FrUniSigIFramesReceived_Type = Counter32
_FrUniSigIFramesReceived_Object = MibTableColumn
frUniSigIFramesReceived = _FrUniSigIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 7),
    _FrUniSigIFramesReceived_Type()
)
frUniSigIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigIFramesReceived.setStatus("mandatory")
_FrUniSigIFramesRcvdDiscarded_Type = Counter32
_FrUniSigIFramesRcvdDiscarded_Object = MibTableColumn
frUniSigIFramesRcvdDiscarded = _FrUniSigIFramesRcvdDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 18, 1, 8),
    _FrUniSigIFramesRcvdDiscarded_Type()
)
frUniSigIFramesRcvdDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigIFramesRcvdDiscarded.setStatus("mandatory")
_FrUniSigSvcaccTable_Object = MibTable
frUniSigSvcaccTable = _FrUniSigSvcaccTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 19)
)
if mibBuilder.loadTexts:
    frUniSigSvcaccTable.setStatus("mandatory")
_FrUniSigSvcaccEntry_Object = MibTableRow
frUniSigSvcaccEntry = _FrUniSigSvcaccEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 19, 1)
)
frUniSigSvcaccEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigSvcaccEntry.setStatus("mandatory")


class _FrUniSigDefaultAccounting_Type(Integer32):
    """Custom type frUniSigDefaultAccounting based on Integer32"""
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


_FrUniSigDefaultAccounting_Type.__name__ = "Integer32"
_FrUniSigDefaultAccounting_Object = MibTableColumn
frUniSigDefaultAccounting = _FrUniSigDefaultAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 19, 1, 1),
    _FrUniSigDefaultAccounting_Type()
)
frUniSigDefaultAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniSigDefaultAccounting.setStatus("mandatory")
_FrUniSigCodesTable_Object = MibTable
frUniSigCodesTable = _FrUniSigCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 20)
)
if mibBuilder.loadTexts:
    frUniSigCodesTable.setStatus("mandatory")
_FrUniSigCodesEntry_Object = MibTableRow
frUniSigCodesEntry = _FrUniSigCodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 20, 1)
)
frUniSigCodesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniSigIndex"),
)
if mibBuilder.loadTexts:
    frUniSigCodesEntry.setStatus("mandatory")


class _FrUniSigLastClearRemoteDataNetworkAddress_Type(DigitString):
    """Custom type frUniSigLastClearRemoteDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_FrUniSigLastClearRemoteDataNetworkAddress_Type.__name__ = "DigitString"
_FrUniSigLastClearRemoteDataNetworkAddress_Object = MibTableColumn
frUniSigLastClearRemoteDataNetworkAddress = _FrUniSigLastClearRemoteDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 20, 1, 1),
    _FrUniSigLastClearRemoteDataNetworkAddress_Type()
)
frUniSigLastClearRemoteDataNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastClearRemoteDataNetworkAddress.setStatus("mandatory")


class _FrUniSigLastClearCause_Type(Unsigned32):
    """Custom type frUniSigLastClearCause based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniSigLastClearCause_Type.__name__ = "Unsigned32"
_FrUniSigLastClearCause_Object = MibTableColumn
frUniSigLastClearCause = _FrUniSigLastClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 20, 1, 2),
    _FrUniSigLastClearCause_Type()
)
frUniSigLastClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastClearCause.setStatus("mandatory")


class _FrUniSigLastDiagnosticCode_Type(Unsigned32):
    """Custom type frUniSigLastDiagnosticCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrUniSigLastDiagnosticCode_Type.__name__ = "Unsigned32"
_FrUniSigLastDiagnosticCode_Object = MibTableColumn
frUniSigLastDiagnosticCode = _FrUniSigLastDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 6, 20, 1, 3),
    _FrUniSigLastDiagnosticCode_Type()
)
frUniSigLastDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSigLastDiagnosticCode.setStatus("mandatory")
_FrUniVFramer_ObjectIdentity = ObjectIdentity
frUniVFramer = _FrUniVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8)
)
_FrUniVFramerRowStatusTable_Object = MibTable
frUniVFramerRowStatusTable = _FrUniVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 1)
)
if mibBuilder.loadTexts:
    frUniVFramerRowStatusTable.setStatus("mandatory")
_FrUniVFramerRowStatusEntry_Object = MibTableRow
frUniVFramerRowStatusEntry = _FrUniVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 1, 1)
)
frUniVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniVFramerRowStatusEntry.setStatus("mandatory")
_FrUniVFramerRowStatus_Type = RowStatus
_FrUniVFramerRowStatus_Object = MibTableColumn
frUniVFramerRowStatus = _FrUniVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 1, 1, 1),
    _FrUniVFramerRowStatus_Type()
)
frUniVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniVFramerRowStatus.setStatus("mandatory")
_FrUniVFramerComponentName_Type = DisplayString
_FrUniVFramerComponentName_Object = MibTableColumn
frUniVFramerComponentName = _FrUniVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 1, 1, 2),
    _FrUniVFramerComponentName_Type()
)
frUniVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerComponentName.setStatus("mandatory")
_FrUniVFramerStorageType_Type = StorageType
_FrUniVFramerStorageType_Object = MibTableColumn
frUniVFramerStorageType = _FrUniVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 1, 1, 4),
    _FrUniVFramerStorageType_Type()
)
frUniVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerStorageType.setStatus("mandatory")
_FrUniVFramerIndex_Type = NonReplicated
_FrUniVFramerIndex_Object = MibTableColumn
frUniVFramerIndex = _FrUniVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 1, 1, 10),
    _FrUniVFramerIndex_Type()
)
frUniVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniVFramerIndex.setStatus("mandatory")
_FrUniVFramerProvTable_Object = MibTable
frUniVFramerProvTable = _FrUniVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 10)
)
if mibBuilder.loadTexts:
    frUniVFramerProvTable.setStatus("mandatory")
_FrUniVFramerProvEntry_Object = MibTableRow
frUniVFramerProvEntry = _FrUniVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 10, 1)
)
frUniVFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniVFramerProvEntry.setStatus("mandatory")
_FrUniVFramerOtherVirtualFramer_Type = Link
_FrUniVFramerOtherVirtualFramer_Object = MibTableColumn
frUniVFramerOtherVirtualFramer = _FrUniVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 10, 1, 1),
    _FrUniVFramerOtherVirtualFramer_Type()
)
frUniVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniVFramerOtherVirtualFramer.setStatus("mandatory")
_FrUniVFramerLogicalProcessor_Type = Link
_FrUniVFramerLogicalProcessor_Object = MibTableColumn
frUniVFramerLogicalProcessor = _FrUniVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 10, 1, 2),
    _FrUniVFramerLogicalProcessor_Type()
)
frUniVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniVFramerLogicalProcessor.setStatus("mandatory")
_FrUniVFramerStateTable_Object = MibTable
frUniVFramerStateTable = _FrUniVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 11)
)
if mibBuilder.loadTexts:
    frUniVFramerStateTable.setStatus("mandatory")
_FrUniVFramerStateEntry_Object = MibTableRow
frUniVFramerStateEntry = _FrUniVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 11, 1)
)
frUniVFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniVFramerStateEntry.setStatus("mandatory")


class _FrUniVFramerAdminState_Type(Integer32):
    """Custom type frUniVFramerAdminState based on Integer32"""
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


_FrUniVFramerAdminState_Type.__name__ = "Integer32"
_FrUniVFramerAdminState_Object = MibTableColumn
frUniVFramerAdminState = _FrUniVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 11, 1, 1),
    _FrUniVFramerAdminState_Type()
)
frUniVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerAdminState.setStatus("mandatory")


class _FrUniVFramerOperationalState_Type(Integer32):
    """Custom type frUniVFramerOperationalState based on Integer32"""
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


_FrUniVFramerOperationalState_Type.__name__ = "Integer32"
_FrUniVFramerOperationalState_Object = MibTableColumn
frUniVFramerOperationalState = _FrUniVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 11, 1, 2),
    _FrUniVFramerOperationalState_Type()
)
frUniVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerOperationalState.setStatus("mandatory")


class _FrUniVFramerUsageState_Type(Integer32):
    """Custom type frUniVFramerUsageState based on Integer32"""
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


_FrUniVFramerUsageState_Type.__name__ = "Integer32"
_FrUniVFramerUsageState_Object = MibTableColumn
frUniVFramerUsageState = _FrUniVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 11, 1, 3),
    _FrUniVFramerUsageState_Type()
)
frUniVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerUsageState.setStatus("mandatory")
_FrUniVFramerStatsTable_Object = MibTable
frUniVFramerStatsTable = _FrUniVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 12)
)
if mibBuilder.loadTexts:
    frUniVFramerStatsTable.setStatus("mandatory")
_FrUniVFramerStatsEntry_Object = MibTableRow
frUniVFramerStatsEntry = _FrUniVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 12, 1)
)
frUniVFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frUniVFramerStatsEntry.setStatus("mandatory")
_FrUniVFramerFrmToOtherVFramer_Type = PassportCounter64
_FrUniVFramerFrmToOtherVFramer_Object = MibTableColumn
frUniVFramerFrmToOtherVFramer = _FrUniVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 12, 1, 2),
    _FrUniVFramerFrmToOtherVFramer_Type()
)
frUniVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerFrmToOtherVFramer.setStatus("mandatory")
_FrUniVFramerFrmFromOtherVFramer_Type = PassportCounter64
_FrUniVFramerFrmFromOtherVFramer_Object = MibTableColumn
frUniVFramerFrmFromOtherVFramer = _FrUniVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 12, 1, 3),
    _FrUniVFramerFrmFromOtherVFramer_Type()
)
frUniVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerFrmFromOtherVFramer.setStatus("mandatory")
_FrUniVFramerOctetFromOtherVFramer_Type = PassportCounter64
_FrUniVFramerOctetFromOtherVFramer_Object = MibTableColumn
frUniVFramerOctetFromOtherVFramer = _FrUniVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 8, 12, 1, 5),
    _FrUniVFramerOctetFromOtherVFramer_Type()
)
frUniVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniVFramerOctetFromOtherVFramer.setStatus("mandatory")
_FrUniLts_ObjectIdentity = ObjectIdentity
frUniLts = _FrUniLts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9)
)
_FrUniLtsRowStatusTable_Object = MibTable
frUniLtsRowStatusTable = _FrUniLtsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 1)
)
if mibBuilder.loadTexts:
    frUniLtsRowStatusTable.setStatus("mandatory")
_FrUniLtsRowStatusEntry_Object = MibTableRow
frUniLtsRowStatusEntry = _FrUniLtsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 1, 1)
)
frUniLtsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsRowStatusEntry.setStatus("mandatory")
_FrUniLtsRowStatus_Type = RowStatus
_FrUniLtsRowStatus_Object = MibTableColumn
frUniLtsRowStatus = _FrUniLtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 1, 1, 1),
    _FrUniLtsRowStatus_Type()
)
frUniLtsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsRowStatus.setStatus("mandatory")
_FrUniLtsComponentName_Type = DisplayString
_FrUniLtsComponentName_Object = MibTableColumn
frUniLtsComponentName = _FrUniLtsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 1, 1, 2),
    _FrUniLtsComponentName_Type()
)
frUniLtsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsComponentName.setStatus("mandatory")
_FrUniLtsStorageType_Type = StorageType
_FrUniLtsStorageType_Object = MibTableColumn
frUniLtsStorageType = _FrUniLtsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 1, 1, 4),
    _FrUniLtsStorageType_Type()
)
frUniLtsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsStorageType.setStatus("mandatory")
_FrUniLtsIndex_Type = NonReplicated
_FrUniLtsIndex_Object = MibTableColumn
frUniLtsIndex = _FrUniLtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 1, 1, 10),
    _FrUniLtsIndex_Type()
)
frUniLtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniLtsIndex.setStatus("mandatory")
_FrUniLtsPat_ObjectIdentity = ObjectIdentity
frUniLtsPat = _FrUniLtsPat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2)
)
_FrUniLtsPatRowStatusTable_Object = MibTable
frUniLtsPatRowStatusTable = _FrUniLtsPatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 1)
)
if mibBuilder.loadTexts:
    frUniLtsPatRowStatusTable.setStatus("mandatory")
_FrUniLtsPatRowStatusEntry_Object = MibTableRow
frUniLtsPatRowStatusEntry = _FrUniLtsPatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 1, 1)
)
frUniLtsPatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsPatRowStatusEntry.setStatus("mandatory")
_FrUniLtsPatRowStatus_Type = RowStatus
_FrUniLtsPatRowStatus_Object = MibTableColumn
frUniLtsPatRowStatus = _FrUniLtsPatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 1, 1, 1),
    _FrUniLtsPatRowStatus_Type()
)
frUniLtsPatRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatRowStatus.setStatus("mandatory")
_FrUniLtsPatComponentName_Type = DisplayString
_FrUniLtsPatComponentName_Object = MibTableColumn
frUniLtsPatComponentName = _FrUniLtsPatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 1, 1, 2),
    _FrUniLtsPatComponentName_Type()
)
frUniLtsPatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsPatComponentName.setStatus("mandatory")
_FrUniLtsPatStorageType_Type = StorageType
_FrUniLtsPatStorageType_Object = MibTableColumn
frUniLtsPatStorageType = _FrUniLtsPatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 1, 1, 4),
    _FrUniLtsPatStorageType_Type()
)
frUniLtsPatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsPatStorageType.setStatus("mandatory")


class _FrUniLtsPatIndex_Type(Integer32):
    """Custom type frUniLtsPatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_FrUniLtsPatIndex_Type.__name__ = "Integer32"
_FrUniLtsPatIndex_Object = MibTableColumn
frUniLtsPatIndex = _FrUniLtsPatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 1, 1, 10),
    _FrUniLtsPatIndex_Type()
)
frUniLtsPatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniLtsPatIndex.setStatus("mandatory")
_FrUniLtsPatDefaultsTable_Object = MibTable
frUniLtsPatDefaultsTable = _FrUniLtsPatDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10)
)
if mibBuilder.loadTexts:
    frUniLtsPatDefaultsTable.setStatus("mandatory")
_FrUniLtsPatDefaultsEntry_Object = MibTableRow
frUniLtsPatDefaultsEntry = _FrUniLtsPatDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1)
)
frUniLtsPatDefaultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsPatDefaultsEntry.setStatus("mandatory")


class _FrUniLtsPatDefaultDlci_Type(Unsigned32):
    """Custom type frUniLtsPatDefaultDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrUniLtsPatDefaultDlci_Type.__name__ = "Unsigned32"
_FrUniLtsPatDefaultDlci_Object = MibTableColumn
frUniLtsPatDefaultDlci = _FrUniLtsPatDefaultDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 200),
    _FrUniLtsPatDefaultDlci_Type()
)
frUniLtsPatDefaultDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultDlci.setStatus("mandatory")


class _FrUniLtsPatDefaultNumFrames_Type(Unsigned32):
    """Custom type frUniLtsPatDefaultNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsPatDefaultNumFrames_Type.__name__ = "Unsigned32"
_FrUniLtsPatDefaultNumFrames_Object = MibTableColumn
frUniLtsPatDefaultNumFrames = _FrUniLtsPatDefaultNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 201),
    _FrUniLtsPatDefaultNumFrames_Type()
)
frUniLtsPatDefaultNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultNumFrames.setStatus("mandatory")


class _FrUniLtsPatDefaultDataSize_Type(Unsigned32):
    """Custom type frUniLtsPatDefaultDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_FrUniLtsPatDefaultDataSize_Type.__name__ = "Unsigned32"
_FrUniLtsPatDefaultDataSize_Object = MibTableColumn
frUniLtsPatDefaultDataSize = _FrUniLtsPatDefaultDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 202),
    _FrUniLtsPatDefaultDataSize_Type()
)
frUniLtsPatDefaultDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultDataSize.setStatus("mandatory")


class _FrUniLtsPatDefaultHeaderBits_Type(OctetString):
    """Custom type frUniLtsPatDefaultHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniLtsPatDefaultHeaderBits_Type.__name__ = "OctetString"
_FrUniLtsPatDefaultHeaderBits_Object = MibTableColumn
frUniLtsPatDefaultHeaderBits = _FrUniLtsPatDefaultHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 203),
    _FrUniLtsPatDefaultHeaderBits_Type()
)
frUniLtsPatDefaultHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultHeaderBits.setStatus("mandatory")


class _FrUniLtsPatDefaultHeaderLength_Type(Unsigned32):
    """Custom type frUniLtsPatDefaultHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_FrUniLtsPatDefaultHeaderLength_Type.__name__ = "Unsigned32"
_FrUniLtsPatDefaultHeaderLength_Object = MibTableColumn
frUniLtsPatDefaultHeaderLength = _FrUniLtsPatDefaultHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 204),
    _FrUniLtsPatDefaultHeaderLength_Type()
)
frUniLtsPatDefaultHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultHeaderLength.setStatus("mandatory")


class _FrUniLtsPatDefaultEABits_Type(Hex):
    """Custom type frUniLtsPatDefaultEABits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrUniLtsPatDefaultEABits_Type.__name__ = "Hex"
_FrUniLtsPatDefaultEABits_Object = MibTableColumn
frUniLtsPatDefaultEABits = _FrUniLtsPatDefaultEABits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 205),
    _FrUniLtsPatDefaultEABits_Type()
)
frUniLtsPatDefaultEABits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultEABits.setStatus("mandatory")


class _FrUniLtsPatDefaultPayloadPattern_Type(HexString):
    """Custom type frUniLtsPatDefaultPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_FrUniLtsPatDefaultPayloadPattern_Type.__name__ = "HexString"
_FrUniLtsPatDefaultPayloadPattern_Object = MibTableColumn
frUniLtsPatDefaultPayloadPattern = _FrUniLtsPatDefaultPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 206),
    _FrUniLtsPatDefaultPayloadPattern_Type()
)
frUniLtsPatDefaultPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultPayloadPattern.setStatus("mandatory")


class _FrUniLtsPatDefaultRfc1490Header_Type(Integer32):
    """Custom type frUniLtsPatDefaultRfc1490Header based on Integer32"""
    defaultValue = 18

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
              18)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n16", 16),
          ("n17", 17),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("none", 18))
    )


_FrUniLtsPatDefaultRfc1490Header_Type.__name__ = "Integer32"
_FrUniLtsPatDefaultRfc1490Header_Object = MibTableColumn
frUniLtsPatDefaultRfc1490Header = _FrUniLtsPatDefaultRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 207),
    _FrUniLtsPatDefaultRfc1490Header_Type()
)
frUniLtsPatDefaultRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultRfc1490Header.setStatus("mandatory")


class _FrUniLtsPatDefaultUseBadLrc_Type(Integer32):
    """Custom type frUniLtsPatDefaultUseBadLrc based on Integer32"""
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


_FrUniLtsPatDefaultUseBadLrc_Type.__name__ = "Integer32"
_FrUniLtsPatDefaultUseBadLrc_Object = MibTableColumn
frUniLtsPatDefaultUseBadLrc = _FrUniLtsPatDefaultUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 10, 1, 208),
    _FrUniLtsPatDefaultUseBadLrc_Type()
)
frUniLtsPatDefaultUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDefaultUseBadLrc.setStatus("mandatory")
_FrUniLtsPatSetupTable_Object = MibTable
frUniLtsPatSetupTable = _FrUniLtsPatSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11)
)
if mibBuilder.loadTexts:
    frUniLtsPatSetupTable.setStatus("mandatory")
_FrUniLtsPatSetupEntry_Object = MibTableRow
frUniLtsPatSetupEntry = _FrUniLtsPatSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1)
)
frUniLtsPatSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsPatSetupEntry.setStatus("mandatory")


class _FrUniLtsPatDlci_Type(Unsigned32):
    """Custom type frUniLtsPatDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrUniLtsPatDlci_Type.__name__ = "Unsigned32"
_FrUniLtsPatDlci_Object = MibTableColumn
frUniLtsPatDlci = _FrUniLtsPatDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 200),
    _FrUniLtsPatDlci_Type()
)
frUniLtsPatDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDlci.setStatus("mandatory")


class _FrUniLtsPatNumFrames_Type(Unsigned32):
    """Custom type frUniLtsPatNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsPatNumFrames_Type.__name__ = "Unsigned32"
_FrUniLtsPatNumFrames_Object = MibTableColumn
frUniLtsPatNumFrames = _FrUniLtsPatNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 201),
    _FrUniLtsPatNumFrames_Type()
)
frUniLtsPatNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatNumFrames.setStatus("mandatory")


class _FrUniLtsPatDataSize_Type(Unsigned32):
    """Custom type frUniLtsPatDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_FrUniLtsPatDataSize_Type.__name__ = "Unsigned32"
_FrUniLtsPatDataSize_Object = MibTableColumn
frUniLtsPatDataSize = _FrUniLtsPatDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 202),
    _FrUniLtsPatDataSize_Type()
)
frUniLtsPatDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatDataSize.setStatus("mandatory")


class _FrUniLtsPatHeaderBits_Type(OctetString):
    """Custom type frUniLtsPatHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniLtsPatHeaderBits_Type.__name__ = "OctetString"
_FrUniLtsPatHeaderBits_Object = MibTableColumn
frUniLtsPatHeaderBits = _FrUniLtsPatHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 203),
    _FrUniLtsPatHeaderBits_Type()
)
frUniLtsPatHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatHeaderBits.setStatus("mandatory")


class _FrUniLtsPatHeaderLength_Type(Unsigned32):
    """Custom type frUniLtsPatHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_FrUniLtsPatHeaderLength_Type.__name__ = "Unsigned32"
_FrUniLtsPatHeaderLength_Object = MibTableColumn
frUniLtsPatHeaderLength = _FrUniLtsPatHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 204),
    _FrUniLtsPatHeaderLength_Type()
)
frUniLtsPatHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatHeaderLength.setStatus("mandatory")


class _FrUniLtsPatEaBits_Type(Hex):
    """Custom type frUniLtsPatEaBits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrUniLtsPatEaBits_Type.__name__ = "Hex"
_FrUniLtsPatEaBits_Object = MibTableColumn
frUniLtsPatEaBits = _FrUniLtsPatEaBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 205),
    _FrUniLtsPatEaBits_Type()
)
frUniLtsPatEaBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatEaBits.setStatus("mandatory")


class _FrUniLtsPatPayloadPattern_Type(HexString):
    """Custom type frUniLtsPatPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_FrUniLtsPatPayloadPattern_Type.__name__ = "HexString"
_FrUniLtsPatPayloadPattern_Object = MibTableColumn
frUniLtsPatPayloadPattern = _FrUniLtsPatPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 206),
    _FrUniLtsPatPayloadPattern_Type()
)
frUniLtsPatPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatPayloadPattern.setStatus("mandatory")


class _FrUniLtsPatRfc1490Header_Type(Integer32):
    """Custom type frUniLtsPatRfc1490Header based on Integer32"""
    defaultValue = 18

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
              18)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n10", 10),
          ("n11", 11),
          ("n12", 12),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n16", 16),
          ("n17", 17),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("n5", 5),
          ("n6", 6),
          ("n7", 7),
          ("n8", 8),
          ("n9", 9),
          ("none", 18))
    )


_FrUniLtsPatRfc1490Header_Type.__name__ = "Integer32"
_FrUniLtsPatRfc1490Header_Object = MibTableColumn
frUniLtsPatRfc1490Header = _FrUniLtsPatRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 207),
    _FrUniLtsPatRfc1490Header_Type()
)
frUniLtsPatRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatRfc1490Header.setStatus("mandatory")


class _FrUniLtsPatUseBadLrc_Type(Integer32):
    """Custom type frUniLtsPatUseBadLrc based on Integer32"""
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


_FrUniLtsPatUseBadLrc_Type.__name__ = "Integer32"
_FrUniLtsPatUseBadLrc_Object = MibTableColumn
frUniLtsPatUseBadLrc = _FrUniLtsPatUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 11, 1, 208),
    _FrUniLtsPatUseBadLrc_Type()
)
frUniLtsPatUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatUseBadLrc.setStatus("mandatory")
_FrUniLtsPatOpDataTable_Object = MibTable
frUniLtsPatOpDataTable = _FrUniLtsPatOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 12)
)
if mibBuilder.loadTexts:
    frUniLtsPatOpDataTable.setStatus("mandatory")
_FrUniLtsPatOpDataEntry_Object = MibTableRow
frUniLtsPatOpDataEntry = _FrUniLtsPatOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 12, 1)
)
frUniLtsPatOpDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsPatOpDataEntry.setStatus("mandatory")


class _FrUniLtsPatFramePattern_Type(HexString):
    """Custom type frUniLtsPatFramePattern based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 24),
    )


_FrUniLtsPatFramePattern_Type.__name__ = "HexString"
_FrUniLtsPatFramePattern_Object = MibTableColumn
frUniLtsPatFramePattern = _FrUniLtsPatFramePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 12, 1, 200),
    _FrUniLtsPatFramePattern_Type()
)
frUniLtsPatFramePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsPatFramePattern.setStatus("mandatory")


class _FrUniLtsPatHdlcBitsInserted_Type(Unsigned32):
    """Custom type frUniLtsPatHdlcBitsInserted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrUniLtsPatHdlcBitsInserted_Type.__name__ = "Unsigned32"
_FrUniLtsPatHdlcBitsInserted_Object = MibTableColumn
frUniLtsPatHdlcBitsInserted = _FrUniLtsPatHdlcBitsInserted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 12, 1, 201),
    _FrUniLtsPatHdlcBitsInserted_Type()
)
frUniLtsPatHdlcBitsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsPatHdlcBitsInserted.setStatus("mandatory")
_FrUniLtsPatOpStateTable_Object = MibTable
frUniLtsPatOpStateTable = _FrUniLtsPatOpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 13)
)
if mibBuilder.loadTexts:
    frUniLtsPatOpStateTable.setStatus("mandatory")
_FrUniLtsPatOpStateEntry_Object = MibTableRow
frUniLtsPatOpStateEntry = _FrUniLtsPatOpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 13, 1)
)
frUniLtsPatOpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsPatOpStateEntry.setStatus("mandatory")


class _FrUniLtsPatLoad_Type(FixedPoint3):
    """Custom type frUniLtsPatLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsPatLoad_Type.__name__ = "FixedPoint3"
_FrUniLtsPatLoad_Object = MibTableColumn
frUniLtsPatLoad = _FrUniLtsPatLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 13, 1, 200),
    _FrUniLtsPatLoad_Type()
)
frUniLtsPatLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsPatLoad.setStatus("mandatory")


class _FrUniLtsPatStatus_Type(Integer32):
    """Custom type frUniLtsPatStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_FrUniLtsPatStatus_Type.__name__ = "Integer32"
_FrUniLtsPatStatus_Object = MibTableColumn
frUniLtsPatStatus = _FrUniLtsPatStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 2, 13, 1, 201),
    _FrUniLtsPatStatus_Type()
)
frUniLtsPatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsPatStatus.setStatus("mandatory")
_FrUniLtsSetupTable_Object = MibTable
frUniLtsSetupTable = _FrUniLtsSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 10)
)
if mibBuilder.loadTexts:
    frUniLtsSetupTable.setStatus("mandatory")
_FrUniLtsSetupEntry_Object = MibTableRow
frUniLtsSetupEntry = _FrUniLtsSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 10, 1)
)
frUniLtsSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsSetupEntry.setStatus("mandatory")


class _FrUniLtsDuration_Type(Unsigned32):
    """Custom type frUniLtsDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsDuration_Type.__name__ = "Unsigned32"
_FrUniLtsDuration_Object = MibTableColumn
frUniLtsDuration = _FrUniLtsDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 10, 1, 200),
    _FrUniLtsDuration_Type()
)
frUniLtsDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsDuration.setStatus("mandatory")


class _FrUniLtsAlgorithm_Type(Integer32):
    """Custom type frUniLtsAlgorithm based on Integer32"""
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
        *(("continousBurst", 0),
          ("delayBurst", 2),
          ("fixedBurst", 3),
          ("intervalBurst", 1))
    )


_FrUniLtsAlgorithm_Type.__name__ = "Integer32"
_FrUniLtsAlgorithm_Object = MibTableColumn
frUniLtsAlgorithm = _FrUniLtsAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 10, 1, 201),
    _FrUniLtsAlgorithm_Type()
)
frUniLtsAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsAlgorithm.setStatus("mandatory")


class _FrUniLtsBurstSize_Type(Unsigned32):
    """Custom type frUniLtsBurstSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_FrUniLtsBurstSize_Type.__name__ = "Unsigned32"
_FrUniLtsBurstSize_Object = MibTableColumn
frUniLtsBurstSize = _FrUniLtsBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 10, 1, 204),
    _FrUniLtsBurstSize_Type()
)
frUniLtsBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsBurstSize.setStatus("mandatory")


class _FrUniLtsTimeInterval_Type(Unsigned32):
    """Custom type frUniLtsTimeInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_FrUniLtsTimeInterval_Type.__name__ = "Unsigned32"
_FrUniLtsTimeInterval_Object = MibTableColumn
frUniLtsTimeInterval = _FrUniLtsTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 10, 1, 205),
    _FrUniLtsTimeInterval_Type()
)
frUniLtsTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniLtsTimeInterval.setStatus("mandatory")
_FrUniLtsStateTable_Object = MibTable
frUniLtsStateTable = _FrUniLtsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 11)
)
if mibBuilder.loadTexts:
    frUniLtsStateTable.setStatus("mandatory")
_FrUniLtsStateEntry_Object = MibTableRow
frUniLtsStateEntry = _FrUniLtsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 11, 1)
)
frUniLtsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsStateEntry.setStatus("mandatory")


class _FrUniLtsGeneratorState_Type(Integer32):
    """Custom type frUniLtsGeneratorState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("stopped", 0))
    )


_FrUniLtsGeneratorState_Type.__name__ = "Integer32"
_FrUniLtsGeneratorState_Object = MibTableColumn
frUniLtsGeneratorState = _FrUniLtsGeneratorState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 11, 1, 200),
    _FrUniLtsGeneratorState_Type()
)
frUniLtsGeneratorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsGeneratorState.setStatus("mandatory")


class _FrUniLtsCycleIncomplete_Type(Integer32):
    """Custom type frUniLtsCycleIncomplete based on Integer32"""
    defaultValue = 1

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


_FrUniLtsCycleIncomplete_Type.__name__ = "Integer32"
_FrUniLtsCycleIncomplete_Object = MibTableColumn
frUniLtsCycleIncomplete = _FrUniLtsCycleIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 11, 1, 201),
    _FrUniLtsCycleIncomplete_Type()
)
frUniLtsCycleIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsCycleIncomplete.setStatus("mandatory")


class _FrUniLtsLastActiveInterval_Type(Unsigned32):
    """Custom type frUniLtsLastActiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsLastActiveInterval_Type.__name__ = "Unsigned32"
_FrUniLtsLastActiveInterval_Object = MibTableColumn
frUniLtsLastActiveInterval = _FrUniLtsLastActiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 11, 1, 202),
    _FrUniLtsLastActiveInterval_Type()
)
frUniLtsLastActiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsLastActiveInterval.setStatus("mandatory")


class _FrUniLtsLoad_Type(FixedPoint3):
    """Custom type frUniLtsLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsLoad_Type.__name__ = "FixedPoint3"
_FrUniLtsLoad_Object = MibTableColumn
frUniLtsLoad = _FrUniLtsLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 11, 1, 204),
    _FrUniLtsLoad_Type()
)
frUniLtsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsLoad.setStatus("mandatory")


class _FrUniLtsElapsedGenerationTime_Type(Unsigned32):
    """Custom type frUniLtsElapsedGenerationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsElapsedGenerationTime_Type.__name__ = "Unsigned32"
_FrUniLtsElapsedGenerationTime_Object = MibTableColumn
frUniLtsElapsedGenerationTime = _FrUniLtsElapsedGenerationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 11, 1, 205),
    _FrUniLtsElapsedGenerationTime_Type()
)
frUniLtsElapsedGenerationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsElapsedGenerationTime.setStatus("mandatory")
_FrUniLtsResultsTable_Object = MibTable
frUniLtsResultsTable = _FrUniLtsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 12)
)
if mibBuilder.loadTexts:
    frUniLtsResultsTable.setStatus("mandatory")
_FrUniLtsResultsEntry_Object = MibTableRow
frUniLtsResultsEntry = _FrUniLtsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 12, 1)
)
frUniLtsResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniLtsIndex"),
)
if mibBuilder.loadTexts:
    frUniLtsResultsEntry.setStatus("mandatory")
_FrUniLtsFramesTx_Type = Counter32
_FrUniLtsFramesTx_Object = MibTableColumn
frUniLtsFramesTx = _FrUniLtsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 12, 1, 200),
    _FrUniLtsFramesTx_Type()
)
frUniLtsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsFramesTx.setStatus("mandatory")


class _FrUniLtsBytesTx_Type(Unsigned32):
    """Custom type frUniLtsBytesTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsBytesTx_Type.__name__ = "Unsigned32"
_FrUniLtsBytesTx_Object = MibTableColumn
frUniLtsBytesTx = _FrUniLtsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 12, 1, 204),
    _FrUniLtsBytesTx_Type()
)
frUniLtsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsBytesTx.setStatus("mandatory")


class _FrUniLtsBitRateTx_Type(FixedPoint3):
    """Custom type frUniLtsBitRateTx based on FixedPoint3"""
    defaultValue = 0

    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsBitRateTx_Type.__name__ = "FixedPoint3"
_FrUniLtsBitRateTx_Object = MibTableColumn
frUniLtsBitRateTx = _FrUniLtsBitRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 12, 1, 208),
    _FrUniLtsBitRateTx_Type()
)
frUniLtsBitRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsBitRateTx.setStatus("mandatory")


class _FrUniLtsFrameRateTx_Type(Unsigned32):
    """Custom type frUniLtsFrameRateTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniLtsFrameRateTx_Type.__name__ = "Unsigned32"
_FrUniLtsFrameRateTx_Object = MibTableColumn
frUniLtsFrameRateTx = _FrUniLtsFrameRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 9, 12, 1, 209),
    _FrUniLtsFrameRateTx_Type()
)
frUniLtsFrameRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLtsFrameRateTx.setStatus("mandatory")
_FrUniCidDataTable_Object = MibTable
frUniCidDataTable = _FrUniCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 10)
)
if mibBuilder.loadTexts:
    frUniCidDataTable.setStatus("mandatory")
_FrUniCidDataEntry_Object = MibTableRow
frUniCidDataEntry = _FrUniCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 10, 1)
)
frUniCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
)
if mibBuilder.loadTexts:
    frUniCidDataEntry.setStatus("mandatory")


class _FrUniCustomerIdentifier_Type(Unsigned32):
    """Custom type frUniCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_FrUniCustomerIdentifier_Type.__name__ = "Unsigned32"
_FrUniCustomerIdentifier_Object = MibTableColumn
frUniCustomerIdentifier = _FrUniCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 10, 1, 1),
    _FrUniCustomerIdentifier_Type()
)
frUniCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniCustomerIdentifier.setStatus("mandatory")
_FrUniStateTable_Object = MibTable
frUniStateTable = _FrUniStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11)
)
if mibBuilder.loadTexts:
    frUniStateTable.setStatus("mandatory")
_FrUniStateEntry_Object = MibTableRow
frUniStateEntry = _FrUniStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1)
)
frUniStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
)
if mibBuilder.loadTexts:
    frUniStateEntry.setStatus("mandatory")


class _FrUniAdminState_Type(Integer32):
    """Custom type frUniAdminState based on Integer32"""
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


_FrUniAdminState_Type.__name__ = "Integer32"
_FrUniAdminState_Object = MibTableColumn
frUniAdminState = _FrUniAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 1),
    _FrUniAdminState_Type()
)
frUniAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniAdminState.setStatus("mandatory")


class _FrUniOperationalState_Type(Integer32):
    """Custom type frUniOperationalState based on Integer32"""
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


_FrUniOperationalState_Type.__name__ = "Integer32"
_FrUniOperationalState_Object = MibTableColumn
frUniOperationalState = _FrUniOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 2),
    _FrUniOperationalState_Type()
)
frUniOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniOperationalState.setStatus("mandatory")


class _FrUniUsageState_Type(Integer32):
    """Custom type frUniUsageState based on Integer32"""
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


_FrUniUsageState_Type.__name__ = "Integer32"
_FrUniUsageState_Object = MibTableColumn
frUniUsageState = _FrUniUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 3),
    _FrUniUsageState_Type()
)
frUniUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniUsageState.setStatus("mandatory")


class _FrUniAvailabilityStatus_Type(OctetString):
    """Custom type frUniAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FrUniAvailabilityStatus_Type.__name__ = "OctetString"
_FrUniAvailabilityStatus_Object = MibTableColumn
frUniAvailabilityStatus = _FrUniAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 4),
    _FrUniAvailabilityStatus_Type()
)
frUniAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniAvailabilityStatus.setStatus("mandatory")


class _FrUniProceduralStatus_Type(OctetString):
    """Custom type frUniProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniProceduralStatus_Type.__name__ = "OctetString"
_FrUniProceduralStatus_Object = MibTableColumn
frUniProceduralStatus = _FrUniProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 5),
    _FrUniProceduralStatus_Type()
)
frUniProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniProceduralStatus.setStatus("mandatory")


class _FrUniControlStatus_Type(OctetString):
    """Custom type frUniControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniControlStatus_Type.__name__ = "OctetString"
_FrUniControlStatus_Object = MibTableColumn
frUniControlStatus = _FrUniControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 6),
    _FrUniControlStatus_Type()
)
frUniControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniControlStatus.setStatus("mandatory")


class _FrUniAlarmStatus_Type(OctetString):
    """Custom type frUniAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrUniAlarmStatus_Type.__name__ = "OctetString"
_FrUniAlarmStatus_Object = MibTableColumn
frUniAlarmStatus = _FrUniAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 7),
    _FrUniAlarmStatus_Type()
)
frUniAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniAlarmStatus.setStatus("mandatory")


class _FrUniStandbyStatus_Type(Integer32):
    """Custom type frUniStandbyStatus based on Integer32"""
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


_FrUniStandbyStatus_Type.__name__ = "Integer32"
_FrUniStandbyStatus_Object = MibTableColumn
frUniStandbyStatus = _FrUniStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 8),
    _FrUniStandbyStatus_Type()
)
frUniStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniStandbyStatus.setStatus("mandatory")


class _FrUniUnknownStatus_Type(Integer32):
    """Custom type frUniUnknownStatus based on Integer32"""
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


_FrUniUnknownStatus_Type.__name__ = "Integer32"
_FrUniUnknownStatus_Object = MibTableColumn
frUniUnknownStatus = _FrUniUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 11, 1, 9),
    _FrUniUnknownStatus_Type()
)
frUniUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniUnknownStatus.setStatus("mandatory")
_FrUniStatsTable_Object = MibTable
frUniStatsTable = _FrUniStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 12)
)
if mibBuilder.loadTexts:
    frUniStatsTable.setStatus("mandatory")
_FrUniStatsEntry_Object = MibTableRow
frUniStatsEntry = _FrUniStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 12, 1)
)
frUniStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
)
if mibBuilder.loadTexts:
    frUniStatsEntry.setStatus("mandatory")


class _FrUniLastUnknownDlci_Type(Unsigned32):
    """Custom type frUniLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FrUniLastUnknownDlci_Type.__name__ = "Unsigned32"
_FrUniLastUnknownDlci_Object = MibTableColumn
frUniLastUnknownDlci = _FrUniLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 12, 1, 1),
    _FrUniLastUnknownDlci_Type()
)
frUniLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniLastUnknownDlci.setStatus("mandatory")
_FrUniUnknownDlciFramesFromIf_Type = Counter32
_FrUniUnknownDlciFramesFromIf_Object = MibTableColumn
frUniUnknownDlciFramesFromIf = _FrUniUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 12, 1, 2),
    _FrUniUnknownDlciFramesFromIf_Type()
)
frUniUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniUnknownDlciFramesFromIf.setStatus("mandatory")
_FrUniInvalidHeaderFramesFromIf_Type = Counter32
_FrUniInvalidHeaderFramesFromIf_Object = MibTableColumn
frUniInvalidHeaderFramesFromIf = _FrUniInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 12, 1, 3),
    _FrUniInvalidHeaderFramesFromIf_Type()
)
frUniInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniInvalidHeaderFramesFromIf.setStatus("mandatory")
_FrUniIfEntryTable_Object = MibTable
frUniIfEntryTable = _FrUniIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 13)
)
if mibBuilder.loadTexts:
    frUniIfEntryTable.setStatus("mandatory")
_FrUniIfEntryEntry_Object = MibTableRow
frUniIfEntryEntry = _FrUniIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 13, 1)
)
frUniIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
)
if mibBuilder.loadTexts:
    frUniIfEntryEntry.setStatus("mandatory")


class _FrUniIfAdminStatus_Type(Integer32):
    """Custom type frUniIfAdminStatus based on Integer32"""
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


_FrUniIfAdminStatus_Type.__name__ = "Integer32"
_FrUniIfAdminStatus_Object = MibTableColumn
frUniIfAdminStatus = _FrUniIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 13, 1, 1),
    _FrUniIfAdminStatus_Type()
)
frUniIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniIfAdminStatus.setStatus("mandatory")


class _FrUniIfIndex_Type(InterfaceIndex):
    """Custom type frUniIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrUniIfIndex_Type.__name__ = "InterfaceIndex"
_FrUniIfIndex_Object = MibTableColumn
frUniIfIndex = _FrUniIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 13, 1, 2),
    _FrUniIfIndex_Type()
)
frUniIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniIfIndex.setStatus("mandatory")
_FrUniOperStatusTable_Object = MibTable
frUniOperStatusTable = _FrUniOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 14)
)
if mibBuilder.loadTexts:
    frUniOperStatusTable.setStatus("mandatory")
_FrUniOperStatusEntry_Object = MibTableRow
frUniOperStatusEntry = _FrUniOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 14, 1)
)
frUniOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
)
if mibBuilder.loadTexts:
    frUniOperStatusEntry.setStatus("mandatory")


class _FrUniSnmpOperStatus_Type(Integer32):
    """Custom type frUniSnmpOperStatus based on Integer32"""
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


_FrUniSnmpOperStatus_Type.__name__ = "Integer32"
_FrUniSnmpOperStatus_Object = MibTableColumn
frUniSnmpOperStatus = _FrUniSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 14, 1, 1),
    _FrUniSnmpOperStatus_Type()
)
frUniSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniSnmpOperStatus.setStatus("mandatory")
_FrUniEmissionPriorityQsTable_Object = MibTable
frUniEmissionPriorityQsTable = _FrUniEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 15)
)
if mibBuilder.loadTexts:
    frUniEmissionPriorityQsTable.setStatus("mandatory")
_FrUniEmissionPriorityQsEntry_Object = MibTableRow
frUniEmissionPriorityQsEntry = _FrUniEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 15, 1)
)
frUniEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
)
if mibBuilder.loadTexts:
    frUniEmissionPriorityQsEntry.setStatus("mandatory")


class _FrUniNumberOfEmissionQs_Type(Unsigned32):
    """Custom type frUniNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_FrUniNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_FrUniNumberOfEmissionQs_Object = MibTableColumn
frUniNumberOfEmissionQs = _FrUniNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 15, 1, 1),
    _FrUniNumberOfEmissionQs_Type()
)
frUniNumberOfEmissionQs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frUniNumberOfEmissionQs.setStatus("mandatory")
_FrUniFrmToIfByQueueTable_Object = MibTable
frUniFrmToIfByQueueTable = _FrUniFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 341)
)
if mibBuilder.loadTexts:
    frUniFrmToIfByQueueTable.setStatus("mandatory")
_FrUniFrmToIfByQueueEntry_Object = MibTableRow
frUniFrmToIfByQueueEntry = _FrUniFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 341, 1)
)
frUniFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    frUniFrmToIfByQueueEntry.setStatus("mandatory")


class _FrUniFrmToIfByQueueIndex_Type(Integer32):
    """Custom type frUniFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrUniFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_FrUniFrmToIfByQueueIndex_Object = MibTableColumn
frUniFrmToIfByQueueIndex = _FrUniFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 341, 1, 1),
    _FrUniFrmToIfByQueueIndex_Type()
)
frUniFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniFrmToIfByQueueIndex.setStatus("mandatory")


class _FrUniFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type frUniFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_FrUniFrmToIfByQueueValue_Object = MibTableColumn
frUniFrmToIfByQueueValue = _FrUniFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 341, 1, 2),
    _FrUniFrmToIfByQueueValue_Type()
)
frUniFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniFrmToIfByQueueValue.setStatus("mandatory")
_FrUniOctetToIfByQueueTable_Object = MibTable
frUniOctetToIfByQueueTable = _FrUniOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 342)
)
if mibBuilder.loadTexts:
    frUniOctetToIfByQueueTable.setStatus("mandatory")
_FrUniOctetToIfByQueueEntry_Object = MibTableRow
frUniOctetToIfByQueueEntry = _FrUniOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 342, 1)
)
frUniOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayUniMIB", "frUniOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    frUniOctetToIfByQueueEntry.setStatus("mandatory")


class _FrUniOctetToIfByQueueIndex_Type(Integer32):
    """Custom type frUniOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrUniOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_FrUniOctetToIfByQueueIndex_Object = MibTableColumn
frUniOctetToIfByQueueIndex = _FrUniOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 342, 1, 1),
    _FrUniOctetToIfByQueueIndex_Type()
)
frUniOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frUniOctetToIfByQueueIndex.setStatus("mandatory")


class _FrUniOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type frUniOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrUniOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_FrUniOctetToIfByQueueValue_Object = MibTableColumn
frUniOctetToIfByQueueValue = _FrUniOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 71, 342, 1, 2),
    _FrUniOctetToIfByQueueValue_Type()
)
frUniOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frUniOctetToIfByQueueValue.setStatus("mandatory")
_FrameRelayUniMIB_ObjectIdentity = ObjectIdentity
frameRelayUniMIB = _FrameRelayUniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24)
)
_FrameRelayUniGroup_ObjectIdentity = ObjectIdentity
frameRelayUniGroup = _FrameRelayUniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 1)
)
_FrameRelayUniGroupBE_ObjectIdentity = ObjectIdentity
frameRelayUniGroupBE = _FrameRelayUniGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 1, 5)
)
_FrameRelayUniGroupBE01_ObjectIdentity = ObjectIdentity
frameRelayUniGroupBE01 = _FrameRelayUniGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 1, 5, 2)
)
_FrameRelayUniGroupBE01A_ObjectIdentity = ObjectIdentity
frameRelayUniGroupBE01A = _FrameRelayUniGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 1, 5, 2, 2)
)
_FrameRelayUniCapabilities_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilities = _FrameRelayUniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 3)
)
_FrameRelayUniCapabilitiesBE_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilitiesBE = _FrameRelayUniCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 3, 5)
)
_FrameRelayUniCapabilitiesBE01_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilitiesBE01 = _FrameRelayUniCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 3, 5, 2)
)
_FrameRelayUniCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilitiesBE01A = _FrameRelayUniCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 24, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayUniMIB",
    **{"frUni": frUni,
       "frUniRowStatusTable": frUniRowStatusTable,
       "frUniRowStatusEntry": frUniRowStatusEntry,
       "frUniRowStatus": frUniRowStatus,
       "frUniComponentName": frUniComponentName,
       "frUniStorageType": frUniStorageType,
       "frUniIndex": frUniIndex,
       "frUniDna": frUniDna,
       "frUniDnaRowStatusTable": frUniDnaRowStatusTable,
       "frUniDnaRowStatusEntry": frUniDnaRowStatusEntry,
       "frUniDnaRowStatus": frUniDnaRowStatus,
       "frUniDnaComponentName": frUniDnaComponentName,
       "frUniDnaStorageType": frUniDnaStorageType,
       "frUniDnaIndex": frUniDnaIndex,
       "frUniDnaCug": frUniDnaCug,
       "frUniDnaCugRowStatusTable": frUniDnaCugRowStatusTable,
       "frUniDnaCugRowStatusEntry": frUniDnaCugRowStatusEntry,
       "frUniDnaCugRowStatus": frUniDnaCugRowStatus,
       "frUniDnaCugComponentName": frUniDnaCugComponentName,
       "frUniDnaCugStorageType": frUniDnaCugStorageType,
       "frUniDnaCugIndex": frUniDnaCugIndex,
       "frUniDnaCugCugOptionsTable": frUniDnaCugCugOptionsTable,
       "frUniDnaCugCugOptionsEntry": frUniDnaCugCugOptionsEntry,
       "frUniDnaCugType": frUniDnaCugType,
       "frUniDnaCugDnic": frUniDnaCugDnic,
       "frUniDnaCugInterlockCode": frUniDnaCugInterlockCode,
       "frUniDnaCugPreferential": frUniDnaCugPreferential,
       "frUniDnaCugOutCalls": frUniDnaCugOutCalls,
       "frUniDnaCugIncCalls": frUniDnaCugIncCalls,
       "frUniDnaHgM": frUniDnaHgM,
       "frUniDnaHgMRowStatusTable": frUniDnaHgMRowStatusTable,
       "frUniDnaHgMRowStatusEntry": frUniDnaHgMRowStatusEntry,
       "frUniDnaHgMRowStatus": frUniDnaHgMRowStatus,
       "frUniDnaHgMComponentName": frUniDnaHgMComponentName,
       "frUniDnaHgMStorageType": frUniDnaHgMStorageType,
       "frUniDnaHgMIndex": frUniDnaHgMIndex,
       "frUniDnaHgMHgAddr": frUniDnaHgMHgAddr,
       "frUniDnaHgMHgAddrRowStatusTable": frUniDnaHgMHgAddrRowStatusTable,
       "frUniDnaHgMHgAddrRowStatusEntry": frUniDnaHgMHgAddrRowStatusEntry,
       "frUniDnaHgMHgAddrRowStatus": frUniDnaHgMHgAddrRowStatus,
       "frUniDnaHgMHgAddrComponentName": frUniDnaHgMHgAddrComponentName,
       "frUniDnaHgMHgAddrStorageType": frUniDnaHgMHgAddrStorageType,
       "frUniDnaHgMHgAddrIndex": frUniDnaHgMHgAddrIndex,
       "frUniDnaHgMHgAddrAddrTable": frUniDnaHgMHgAddrAddrTable,
       "frUniDnaHgMHgAddrAddrEntry": frUniDnaHgMHgAddrAddrEntry,
       "frUniDnaHgMHgAddrNumberingPlanIndicator": frUniDnaHgMHgAddrNumberingPlanIndicator,
       "frUniDnaHgMHgAddrDataNetworkAddress": frUniDnaHgMHgAddrDataNetworkAddress,
       "frUniDnaHgMIfTable": frUniDnaHgMIfTable,
       "frUniDnaHgMIfEntry": frUniDnaHgMIfEntry,
       "frUniDnaHgMAvailabilityUpdateThreshold": frUniDnaHgMAvailabilityUpdateThreshold,
       "frUniDnaHgMOpTable": frUniDnaHgMOpTable,
       "frUniDnaHgMOpEntry": frUniDnaHgMOpEntry,
       "frUniDnaHgMMaximumAvailableAggregateCir": frUniDnaHgMMaximumAvailableAggregateCir,
       "frUniDnaHgMAvailableAggregateCir": frUniDnaHgMAvailableAggregateCir,
       "frUniDnaHgMAvailabilityDelta": frUniDnaHgMAvailabilityDelta,
       "frUniDnaHgMAvailableDlcis": frUniDnaHgMAvailableDlcis,
       "frUniDnaAddressTable": frUniDnaAddressTable,
       "frUniDnaAddressEntry": frUniDnaAddressEntry,
       "frUniDnaNumberingPlanIndicator": frUniDnaNumberingPlanIndicator,
       "frUniDnaDataNetworkAddress": frUniDnaDataNetworkAddress,
       "frUniDnaOutgoingOptionsTable": frUniDnaOutgoingOptionsTable,
       "frUniDnaOutgoingOptionsEntry": frUniDnaOutgoingOptionsEntry,
       "frUniDnaOutDefaultPriority": frUniDnaOutDefaultPriority,
       "frUniDnaOutDefaultPathSensitivity": frUniDnaOutDefaultPathSensitivity,
       "frUniDnaOutPathSensitivityOverRide": frUniDnaOutPathSensitivityOverRide,
       "frUniDnaOutDefaultPathReliability": frUniDnaOutDefaultPathReliability,
       "frUniDnaOutAccess": frUniDnaOutAccess,
       "frUniDnaDefaultTransferPriority": frUniDnaDefaultTransferPriority,
       "frUniDnaTransferPriorityOverRide": frUniDnaTransferPriorityOverRide,
       "frUniDnaIncomingOptionsTable": frUniDnaIncomingOptionsTable,
       "frUniDnaIncomingOptionsEntry": frUniDnaIncomingOptionsEntry,
       "frUniDnaIncAccess": frUniDnaIncAccess,
       "frUniDnaCallOptionsTable": frUniDnaCallOptionsTable,
       "frUniDnaCallOptionsEntry": frUniDnaCallOptionsEntry,
       "frUniDnaAccountClass": frUniDnaAccountClass,
       "frUniDnaAccountCollection": frUniDnaAccountCollection,
       "frUniDnaServiceExchange": frUniDnaServiceExchange,
       "frUniDnaEgressAccounting": frUniDnaEgressAccounting,
       "frUniDnaDataPath": frUniDnaDataPath,
       "frUniFramer": frUniFramer,
       "frUniFramerRowStatusTable": frUniFramerRowStatusTable,
       "frUniFramerRowStatusEntry": frUniFramerRowStatusEntry,
       "frUniFramerRowStatus": frUniFramerRowStatus,
       "frUniFramerComponentName": frUniFramerComponentName,
       "frUniFramerStorageType": frUniFramerStorageType,
       "frUniFramerIndex": frUniFramerIndex,
       "frUniFramerProvTable": frUniFramerProvTable,
       "frUniFramerProvEntry": frUniFramerProvEntry,
       "frUniFramerInterfaceName": frUniFramerInterfaceName,
       "frUniFramerLinkTable": frUniFramerLinkTable,
       "frUniFramerLinkEntry": frUniFramerLinkEntry,
       "frUniFramerFlagsBetweenFrames": frUniFramerFlagsBetweenFrames,
       "frUniFramerStateTable": frUniFramerStateTable,
       "frUniFramerStateEntry": frUniFramerStateEntry,
       "frUniFramerAdminState": frUniFramerAdminState,
       "frUniFramerOperationalState": frUniFramerOperationalState,
       "frUniFramerUsageState": frUniFramerUsageState,
       "frUniFramerStatsTable": frUniFramerStatsTable,
       "frUniFramerStatsEntry": frUniFramerStatsEntry,
       "frUniFramerFrmToIf": frUniFramerFrmToIf,
       "frUniFramerFrmFromIf": frUniFramerFrmFromIf,
       "frUniFramerOctetFromIf": frUniFramerOctetFromIf,
       "frUniFramerAborts": frUniFramerAborts,
       "frUniFramerCrcErrors": frUniFramerCrcErrors,
       "frUniFramerLrcErrors": frUniFramerLrcErrors,
       "frUniFramerNonOctetErrors": frUniFramerNonOctetErrors,
       "frUniFramerOverruns": frUniFramerOverruns,
       "frUniFramerUnderruns": frUniFramerUnderruns,
       "frUniFramerLargeFrmErrors": frUniFramerLargeFrmErrors,
       "frUniFramerFrmModeErrors": frUniFramerFrmModeErrors,
       "frUniFramerUtilTable": frUniFramerUtilTable,
       "frUniFramerUtilEntry": frUniFramerUtilEntry,
       "frUniFramerNormPrioLinkUtilToIf": frUniFramerNormPrioLinkUtilToIf,
       "frUniFramerNormPrioLinkUtilFromIf": frUniFramerNormPrioLinkUtilFromIf,
       "frUniLmi": frUniLmi,
       "frUniLmiRowStatusTable": frUniLmiRowStatusTable,
       "frUniLmiRowStatusEntry": frUniLmiRowStatusEntry,
       "frUniLmiRowStatus": frUniLmiRowStatus,
       "frUniLmiComponentName": frUniLmiComponentName,
       "frUniLmiStorageType": frUniLmiStorageType,
       "frUniLmiIndex": frUniLmiIndex,
       "frUniLmiParmsTable": frUniLmiParmsTable,
       "frUniLmiParmsEntry": frUniLmiParmsEntry,
       "frUniLmiProcedures": frUniLmiProcedures,
       "frUniLmiAsyncStatusReport": frUniLmiAsyncStatusReport,
       "frUniLmiErrorEventThreshold": frUniLmiErrorEventThreshold,
       "frUniLmiEventCount": frUniLmiEventCount,
       "frUniLmiCheckPointTimer": frUniLmiCheckPointTimer,
       "frUniLmiMessageCountTimer": frUniLmiMessageCountTimer,
       "frUniLmiIgnoreActiveBit": frUniLmiIgnoreActiveBit,
       "frUniLmiSide": frUniLmiSide,
       "frUniLmiPvcConfigParmsInFsr": frUniLmiPvcConfigParmsInFsr,
       "frUniLmiStateTable": frUniLmiStateTable,
       "frUniLmiStateEntry": frUniLmiStateEntry,
       "frUniLmiAdminState": frUniLmiAdminState,
       "frUniLmiOperationalState": frUniLmiOperationalState,
       "frUniLmiUsageState": frUniLmiUsageState,
       "frUniLmiPsiTable": frUniLmiPsiTable,
       "frUniLmiPsiEntry": frUniLmiPsiEntry,
       "frUniLmiProtocolStatus": frUniLmiProtocolStatus,
       "frUniLmiOpProcedures": frUniLmiOpProcedures,
       "frUniLmiStatsTable": frUniLmiStatsTable,
       "frUniLmiStatsEntry": frUniLmiStatsEntry,
       "frUniLmiKeepAliveStatusToIf": frUniLmiKeepAliveStatusToIf,
       "frUniLmiFullStatusToIf": frUniLmiFullStatusToIf,
       "frUniLmiKeepAliveStatusEnqFromIf": frUniLmiKeepAliveStatusEnqFromIf,
       "frUniLmiFullStatusEnqFromIf": frUniLmiFullStatusEnqFromIf,
       "frUniLmiNetworkSideEventHistory": frUniLmiNetworkSideEventHistory,
       "frUniLmiProtocolErrors": frUniLmiProtocolErrors,
       "frUniLmiUnexpectedIes": frUniLmiUnexpectedIes,
       "frUniLmiSequenceErrors": frUniLmiSequenceErrors,
       "frUniLmiUnexpectedReports": frUniLmiUnexpectedReports,
       "frUniLmiPollingVerifTimeouts": frUniLmiPollingVerifTimeouts,
       "frUniLmiKeepAliveEnqToIf": frUniLmiKeepAliveEnqToIf,
       "frUniLmiFullStatusEnqToIf": frUniLmiFullStatusEnqToIf,
       "frUniLmiUserSideEventHistory": frUniLmiUserSideEventHistory,
       "frUniLmiStatusSequenceErrors": frUniLmiStatusSequenceErrors,
       "frUniLmiNoStatusReportCount": frUniLmiNoStatusReportCount,
       "frUniLmiUspParmsTable": frUniLmiUspParmsTable,
       "frUniLmiUspParmsEntry": frUniLmiUspParmsEntry,
       "frUniLmiFullStatusPollingCycles": frUniLmiFullStatusPollingCycles,
       "frUniLmiLinkVerificationTimer": frUniLmiLinkVerificationTimer,
       "frUniDlci": frUniDlci,
       "frUniDlciRowStatusTable": frUniDlciRowStatusTable,
       "frUniDlciRowStatusEntry": frUniDlciRowStatusEntry,
       "frUniDlciRowStatus": frUniDlciRowStatus,
       "frUniDlciComponentName": frUniDlciComponentName,
       "frUniDlciStorageType": frUniDlciStorageType,
       "frUniDlciIndex": frUniDlciIndex,
       "frUniDlciDc": frUniDlciDc,
       "frUniDlciDcRowStatusTable": frUniDlciDcRowStatusTable,
       "frUniDlciDcRowStatusEntry": frUniDlciDcRowStatusEntry,
       "frUniDlciDcRowStatus": frUniDlciDcRowStatus,
       "frUniDlciDcComponentName": frUniDlciDcComponentName,
       "frUniDlciDcStorageType": frUniDlciDcStorageType,
       "frUniDlciDcIndex": frUniDlciDcIndex,
       "frUniDlciDcOptionsTable": frUniDlciDcOptionsTable,
       "frUniDlciDcOptionsEntry": frUniDlciDcOptionsEntry,
       "frUniDlciDcRemoteNpi": frUniDlciDcRemoteNpi,
       "frUniDlciDcRemoteDna": frUniDlciDcRemoteDna,
       "frUniDlciDcRemoteDlci": frUniDlciDcRemoteDlci,
       "frUniDlciDcType": frUniDlciDcType,
       "frUniDlciDcTransferPriority": frUniDlciDcTransferPriority,
       "frUniDlciDcDiscardPriority": frUniDlciDcDiscardPriority,
       "frUniDlciDcDeDiscardPriority": frUniDlciDcDeDiscardPriority,
       "frUniDlciDcDataPath": frUniDlciDcDataPath,
       "frUniDlciDcCugIndex": frUniDlciDcCugIndex,
       "frUniDlciDcCugType": frUniDlciDcCugType,
       "frUniDlciDcNfaTable": frUniDlciDcNfaTable,
       "frUniDlciDcNfaEntry": frUniDlciDcNfaEntry,
       "frUniDlciDcNfaIndex": frUniDlciDcNfaIndex,
       "frUniDlciDcNfaValue": frUniDlciDcNfaValue,
       "frUniDlciDcNfaRowStatus": frUniDlciDcNfaRowStatus,
       "frUniDlciVc": frUniDlciVc,
       "frUniDlciVcRowStatusTable": frUniDlciVcRowStatusTable,
       "frUniDlciVcRowStatusEntry": frUniDlciVcRowStatusEntry,
       "frUniDlciVcRowStatus": frUniDlciVcRowStatus,
       "frUniDlciVcComponentName": frUniDlciVcComponentName,
       "frUniDlciVcStorageType": frUniDlciVcStorageType,
       "frUniDlciVcIndex": frUniDlciVcIndex,
       "frUniDlciVcCadTable": frUniDlciVcCadTable,
       "frUniDlciVcCadEntry": frUniDlciVcCadEntry,
       "frUniDlciVcType": frUniDlciVcType,
       "frUniDlciVcState": frUniDlciVcState,
       "frUniDlciVcPreviousState": frUniDlciVcPreviousState,
       "frUniDlciVcDiagnosticCode": frUniDlciVcDiagnosticCode,
       "frUniDlciVcPreviousDiagnosticCode": frUniDlciVcPreviousDiagnosticCode,
       "frUniDlciVcCalledNpi": frUniDlciVcCalledNpi,
       "frUniDlciVcCalledDna": frUniDlciVcCalledDna,
       "frUniDlciVcCalledLcn": frUniDlciVcCalledLcn,
       "frUniDlciVcCallingNpi": frUniDlciVcCallingNpi,
       "frUniDlciVcCallingDna": frUniDlciVcCallingDna,
       "frUniDlciVcCallingLcn": frUniDlciVcCallingLcn,
       "frUniDlciVcAccountingEnabled": frUniDlciVcAccountingEnabled,
       "frUniDlciVcFastSelectCall": frUniDlciVcFastSelectCall,
       "frUniDlciVcPathReliability": frUniDlciVcPathReliability,
       "frUniDlciVcAccountingEnd": frUniDlciVcAccountingEnd,
       "frUniDlciVcPriority": frUniDlciVcPriority,
       "frUniDlciVcSegmentSize": frUniDlciVcSegmentSize,
       "frUniDlciVcMaxSubnetPktSize": frUniDlciVcMaxSubnetPktSize,
       "frUniDlciVcRcosToNetwork": frUniDlciVcRcosToNetwork,
       "frUniDlciVcRcosFromNetwork": frUniDlciVcRcosFromNetwork,
       "frUniDlciVcEmissionPriorityToNetwork": frUniDlciVcEmissionPriorityToNetwork,
       "frUniDlciVcEmissionPriorityFromNetwork": frUniDlciVcEmissionPriorityFromNetwork,
       "frUniDlciVcDataPath": frUniDlciVcDataPath,
       "frUniDlciVcIntdTable": frUniDlciVcIntdTable,
       "frUniDlciVcIntdEntry": frUniDlciVcIntdEntry,
       "frUniDlciVcCallReferenceNumber": frUniDlciVcCallReferenceNumber,
       "frUniDlciVcElapsedTimeTillNow": frUniDlciVcElapsedTimeTillNow,
       "frUniDlciVcSegmentsRx": frUniDlciVcSegmentsRx,
       "frUniDlciVcSegmentsSent": frUniDlciVcSegmentsSent,
       "frUniDlciVcStartTime": frUniDlciVcStartTime,
       "frUniDlciVcFrdTable": frUniDlciVcFrdTable,
       "frUniDlciVcFrdEntry": frUniDlciVcFrdEntry,
       "frUniDlciVcFrmCongestedToSubnet": frUniDlciVcFrmCongestedToSubnet,
       "frUniDlciVcCannotForwardToSubnet": frUniDlciVcCannotForwardToSubnet,
       "frUniDlciVcNotDataXferToSubnet": frUniDlciVcNotDataXferToSubnet,
       "frUniDlciVcOutOfRangeFrmFromSubnet": frUniDlciVcOutOfRangeFrmFromSubnet,
       "frUniDlciVcCombErrorsFromSubnet": frUniDlciVcCombErrorsFromSubnet,
       "frUniDlciVcDuplicatesFromSubnet": frUniDlciVcDuplicatesFromSubnet,
       "frUniDlciVcNotDataXferFromSubnet": frUniDlciVcNotDataXferFromSubnet,
       "frUniDlciVcFrmLossTimeouts": frUniDlciVcFrmLossTimeouts,
       "frUniDlciVcOoSeqByteCntExceeded": frUniDlciVcOoSeqByteCntExceeded,
       "frUniDlciVcPeakOoSeqPktCount": frUniDlciVcPeakOoSeqPktCount,
       "frUniDlciVcPeakOoSeqFrmForwarded": frUniDlciVcPeakOoSeqFrmForwarded,
       "frUniDlciVcSendSequenceNumber": frUniDlciVcSendSequenceNumber,
       "frUniDlciVcPktRetryTimeouts": frUniDlciVcPktRetryTimeouts,
       "frUniDlciVcPeakRetryQueueSize": frUniDlciVcPeakRetryQueueSize,
       "frUniDlciVcSubnetRecoveries": frUniDlciVcSubnetRecoveries,
       "frUniDlciVcOoSeqPktCntExceeded": frUniDlciVcOoSeqPktCntExceeded,
       "frUniDlciVcPeakOoSeqByteCount": frUniDlciVcPeakOoSeqByteCount,
       "frUniDlciVcDmepTable": frUniDlciVcDmepTable,
       "frUniDlciVcDmepEntry": frUniDlciVcDmepEntry,
       "frUniDlciVcDmepValue": frUniDlciVcDmepValue,
       "frUniDlciSp": frUniDlciSp,
       "frUniDlciSpRowStatusTable": frUniDlciSpRowStatusTable,
       "frUniDlciSpRowStatusEntry": frUniDlciSpRowStatusEntry,
       "frUniDlciSpRowStatus": frUniDlciSpRowStatus,
       "frUniDlciSpComponentName": frUniDlciSpComponentName,
       "frUniDlciSpStorageType": frUniDlciSpStorageType,
       "frUniDlciSpIndex": frUniDlciSpIndex,
       "frUniDlciSpParmsTable": frUniDlciSpParmsTable,
       "frUniDlciSpParmsEntry": frUniDlciSpParmsEntry,
       "frUniDlciSpMaximumFrameSize": frUniDlciSpMaximumFrameSize,
       "frUniDlciSpRateEnforcement": frUniDlciSpRateEnforcement,
       "frUniDlciSpCommittedInformationRate": frUniDlciSpCommittedInformationRate,
       "frUniDlciSpCommittedBurstSize": frUniDlciSpCommittedBurstSize,
       "frUniDlciSpExcessBurstSize": frUniDlciSpExcessBurstSize,
       "frUniDlciSpMeasurementInterval": frUniDlciSpMeasurementInterval,
       "frUniDlciSpRateAdaptation": frUniDlciSpRateAdaptation,
       "frUniDlciSpAccounting": frUniDlciSpAccounting,
       "frUniDlciSpRaSensitivity": frUniDlciSpRaSensitivity,
       "frUniDlciSpUpdateBCI": frUniDlciSpUpdateBCI,
       "frUniDlciLb": frUniDlciLb,
       "frUniDlciLbRowStatusTable": frUniDlciLbRowStatusTable,
       "frUniDlciLbRowStatusEntry": frUniDlciLbRowStatusEntry,
       "frUniDlciLbRowStatus": frUniDlciLbRowStatus,
       "frUniDlciLbComponentName": frUniDlciLbComponentName,
       "frUniDlciLbStorageType": frUniDlciLbStorageType,
       "frUniDlciLbIndex": frUniDlciLbIndex,
       "frUniDlciLbStatsTable": frUniDlciLbStatsTable,
       "frUniDlciLbStatsEntry": frUniDlciLbStatsEntry,
       "frUniDlciLbLocalTotalFrm": frUniDlciLbLocalTotalFrm,
       "frUniDlciLbLocalTotalBytes": frUniDlciLbLocalTotalBytes,
       "frUniDlciLbLocalFecnFrm": frUniDlciLbLocalFecnFrm,
       "frUniDlciLbLocalBecnFrm": frUniDlciLbLocalBecnFrm,
       "frUniDlciLbLocalDeFrm": frUniDlciLbLocalDeFrm,
       "frUniDlciLbLocalDeBytes": frUniDlciLbLocalDeBytes,
       "frUniDlciLbRemoteTotalFrm": frUniDlciLbRemoteTotalFrm,
       "frUniDlciLbRemoteTotalBytes": frUniDlciLbRemoteTotalBytes,
       "frUniDlciLbRemoteFecnFrm": frUniDlciLbRemoteFecnFrm,
       "frUniDlciLbRemoteBecnFrm": frUniDlciLbRemoteBecnFrm,
       "frUniDlciLbRemoteDeFrm": frUniDlciLbRemoteDeFrm,
       "frUniDlciLbRemoteDeBytes": frUniDlciLbRemoteDeBytes,
       "frUniDlciStateTable": frUniDlciStateTable,
       "frUniDlciStateEntry": frUniDlciStateEntry,
       "frUniDlciAdminState": frUniDlciAdminState,
       "frUniDlciOperationalState": frUniDlciOperationalState,
       "frUniDlciUsageState": frUniDlciUsageState,
       "frUniDlciAvailabilityStatus": frUniDlciAvailabilityStatus,
       "frUniDlciProceduralStatus": frUniDlciProceduralStatus,
       "frUniDlciControlStatus": frUniDlciControlStatus,
       "frUniDlciAlarmStatus": frUniDlciAlarmStatus,
       "frUniDlciStandbyStatus": frUniDlciStandbyStatus,
       "frUniDlciUnknownStatus": frUniDlciUnknownStatus,
       "frUniDlciAbitTable": frUniDlciAbitTable,
       "frUniDlciAbitEntry": frUniDlciAbitEntry,
       "frUniDlciABitStatusToIf": frUniDlciABitStatusToIf,
       "frUniDlciABitReasonToIf": frUniDlciABitReasonToIf,
       "frUniDlciABitStatusFromIf": frUniDlciABitStatusFromIf,
       "frUniDlciABitReasonFromIf": frUniDlciABitReasonFromIf,
       "frUniDlciLoopbackState": frUniDlciLoopbackState,
       "frUniDlciCalldTable": frUniDlciCalldTable,
       "frUniDlciCalldEntry": frUniDlciCalldEntry,
       "frUniDlciCallType": frUniDlciCallType,
       "frUniDlciQ933CallState": frUniDlciQ933CallState,
       "frUniDlciQ933CallReference": frUniDlciQ933CallReference,
       "frUniDlciSpOpTable": frUniDlciSpOpTable,
       "frUniDlciSpOpEntry": frUniDlciSpOpEntry,
       "frUniDlciMaximumFrameSize": frUniDlciMaximumFrameSize,
       "frUniDlciRateEnforcement": frUniDlciRateEnforcement,
       "frUniDlciCommittedInformationRate": frUniDlciCommittedInformationRate,
       "frUniDlciCommittedBurstSize": frUniDlciCommittedBurstSize,
       "frUniDlciExcessBurstSize": frUniDlciExcessBurstSize,
       "frUniDlciMeasurementInterval": frUniDlciMeasurementInterval,
       "frUniDlciRateAdaptation": frUniDlciRateAdaptation,
       "frUniDlciAccounting": frUniDlciAccounting,
       "frUniDlciEmissionPriorityToIf": frUniDlciEmissionPriorityToIf,
       "frUniDlciTransferPriToNwk": frUniDlciTransferPriToNwk,
       "frUniDlciTransferPriFromNwk": frUniDlciTransferPriFromNwk,
       "frUniDlciStatsTable": frUniDlciStatsTable,
       "frUniDlciStatsEntry": frUniDlciStatsEntry,
       "frUniDlciFrmToIf": frUniDlciFrmToIf,
       "frUniDlciFecnFrmToIf": frUniDlciFecnFrmToIf,
       "frUniDlciBecnFrmToIf": frUniDlciBecnFrmToIf,
       "frUniDlciBciToSubnet": frUniDlciBciToSubnet,
       "frUniDlciDeFrmToIf": frUniDlciDeFrmToIf,
       "frUniDlciDiscCongestedToIf": frUniDlciDiscCongestedToIf,
       "frUniDlciDiscDeCongestedToIf": frUniDlciDiscDeCongestedToIf,
       "frUniDlciFrmFromIf": frUniDlciFrmFromIf,
       "frUniDlciFecnFrmFromIf": frUniDlciFecnFrmFromIf,
       "frUniDlciBecnFrmFromIf": frUniDlciBecnFrmFromIf,
       "frUniDlciFciFromSubnet": frUniDlciFciFromSubnet,
       "frUniDlciBciFromSubnet": frUniDlciBciFromSubnet,
       "frUniDlciDeFrmFromIf": frUniDlciDeFrmFromIf,
       "frUniDlciExcessFrmFromIf": frUniDlciExcessFrmFromIf,
       "frUniDlciDiscExcessFromIf": frUniDlciDiscExcessFromIf,
       "frUniDlciDiscFrameAbit": frUniDlciDiscFrameAbit,
       "frUniDlciDiscCongestedFromIf": frUniDlciDiscCongestedFromIf,
       "frUniDlciDiscDeCongestedFromIf": frUniDlciDiscDeCongestedFromIf,
       "frUniDlciErrorShortFrmFromIf": frUniDlciErrorShortFrmFromIf,
       "frUniDlciErrorLongFrmFromIf": frUniDlciErrorLongFrmFromIf,
       "frUniDlciBecnFrmSetByService": frUniDlciBecnFrmSetByService,
       "frUniDlciBytesToIf": frUniDlciBytesToIf,
       "frUniDlciDeBytesToIf": frUniDlciDeBytesToIf,
       "frUniDlciDiscCongestedToIfBytes": frUniDlciDiscCongestedToIfBytes,
       "frUniDlciDiscDeCongestedToIfBytes": frUniDlciDiscDeCongestedToIfBytes,
       "frUniDlciBytesFromIf": frUniDlciBytesFromIf,
       "frUniDlciDeBytesFromIf": frUniDlciDeBytesFromIf,
       "frUniDlciExcessBytesFromIf": frUniDlciExcessBytesFromIf,
       "frUniDlciDiscExcessFromIfBytes": frUniDlciDiscExcessFromIfBytes,
       "frUniDlciDiscByteAbit": frUniDlciDiscByteAbit,
       "frUniDlciDiscCongestedFromIfBytes": frUniDlciDiscCongestedFromIfBytes,
       "frUniDlciDiscDeCongestedFromIfBytes": frUniDlciDiscDeCongestedFromIfBytes,
       "frUniDlciErrorShortBytesFromIf": frUniDlciErrorShortBytesFromIf,
       "frUniDlciErrorLongBytesFromIf": frUniDlciErrorLongBytesFromIf,
       "frUniDlciRateAdaptReduct": frUniDlciRateAdaptReduct,
       "frUniDlciRateAdaptReductPeriod": frUniDlciRateAdaptReductPeriod,
       "frUniDlciTransferPriorityToNetwork": frUniDlciTransferPriorityToNetwork,
       "frUniDlciTransferPriorityFromNetwork": frUniDlciTransferPriorityFromNetwork,
       "frUniDlciCirPresent": frUniDlciCirPresent,
       "frUniDlciEirPresent": frUniDlciEirPresent,
       "frUniDlciIntTable": frUniDlciIntTable,
       "frUniDlciIntEntry": frUniDlciIntEntry,
       "frUniDlciStartTime": frUniDlciStartTime,
       "frUniDlciTotalIngressBytes": frUniDlciTotalIngressBytes,
       "frUniDlciTotalEgressBytes": frUniDlciTotalEgressBytes,
       "frUniDlciEirIngressBytes": frUniDlciEirIngressBytes,
       "frUniDlciEirEgressBytes": frUniDlciEirEgressBytes,
       "frUniDlciDiscardedBytes": frUniDlciDiscardedBytes,
       "frUniDlciTotalIngressSegFrm": frUniDlciTotalIngressSegFrm,
       "frUniDlciTotalEgressSegFrm": frUniDlciTotalEgressSegFrm,
       "frUniDlciEirIngressSegFrm": frUniDlciEirIngressSegFrm,
       "frUniDlciEirEgressSegFrm": frUniDlciEirEgressSegFrm,
       "frUniDlciDiscardedSegFrm": frUniDlciDiscardedSegFrm,
       "frUniDlciCirPresentObs": frUniDlciCirPresentObs,
       "frUniDlciEirPresentObs": frUniDlciEirPresentObs,
       "frUniDlciRateEnforcementPresent": frUniDlciRateEnforcementPresent,
       "frUniDlciRateAdaptationPresent": frUniDlciRateAdaptationPresent,
       "frUniDlciLocalRateAdaptOccurred": frUniDlciLocalRateAdaptOccurred,
       "frUniDlciCallReferenceNumber": frUniDlciCallReferenceNumber,
       "frUniDlciElapsedDifference": frUniDlciElapsedDifference,
       "frUniSig": frUniSig,
       "frUniSigRowStatusTable": frUniSigRowStatusTable,
       "frUniSigRowStatusEntry": frUniSigRowStatusEntry,
       "frUniSigRowStatus": frUniSigRowStatus,
       "frUniSigComponentName": frUniSigComponentName,
       "frUniSigStorageType": frUniSigStorageType,
       "frUniSigIndex": frUniSigIndex,
       "frUniSigRangeTable": frUniSigRangeTable,
       "frUniSigRangeEntry": frUniSigRangeEntry,
       "frUniSigHighestPvcDlci": frUniSigHighestPvcDlci,
       "frUniSigServParmsTable": frUniSigServParmsTable,
       "frUniSigServParmsEntry": frUniSigServParmsEntry,
       "frUniSigMaximumAggregateSvcCir": frUniSigMaximumAggregateSvcCir,
       "frUniSigMaximumAggregateSvcEir": frUniSigMaximumAggregateSvcEir,
       "frUniSigMaximumFrameSize": frUniSigMaximumFrameSize,
       "frUniSigDefaultMaximumFrameSize": frUniSigDefaultMaximumFrameSize,
       "frUniSigDefaultCommittedInformationRate": frUniSigDefaultCommittedInformationRate,
       "frUniSigDefaultCommittedBurstSize": frUniSigDefaultCommittedBurstSize,
       "frUniSigDefaultExcessBurstSize": frUniSigDefaultExcessBurstSize,
       "frUniSigUnlimitedAggregateEir": frUniSigUnlimitedAggregateEir,
       "frUniSigRateEnforcement": frUniSigRateEnforcement,
       "frUniSigRateAdaptation": frUniSigRateAdaptation,
       "frUniSigMaximumAggregateSvcCirNormalQ": frUniSigMaximumAggregateSvcCirNormalQ,
       "frUniSigMaximumAggregateSvcCirHighQ": frUniSigMaximumAggregateSvcCirHighQ,
       "frUniSigMaximumAggregateSvcCirInterruptQ": frUniSigMaximumAggregateSvcCirInterruptQ,
       "frUniSigMaximumAggregateSvcEirNormalQ": frUniSigMaximumAggregateSvcEirNormalQ,
       "frUniSigMaximumAggregateSvcEirHighQ": frUniSigMaximumAggregateSvcEirHighQ,
       "frUniSigMaximumAggregateSvcEirInterruptQ": frUniSigMaximumAggregateSvcEirInterruptQ,
       "frUniSigX213IeHandling": frUniSigX213IeHandling,
       "frUniSigRaSensitivity": frUniSigRaSensitivity,
       "frUniSigUpdateBCI": frUniSigUpdateBCI,
       "frUniSigDefaultLocCheck": frUniSigDefaultLocCheck,
       "frUniSigSysParmsTable": frUniSigSysParmsTable,
       "frUniSigSysParmsEntry": frUniSigSysParmsEntry,
       "frUniSigCallSetupTimer": frUniSigCallSetupTimer,
       "frUniSigDisconnectTimer": frUniSigDisconnectTimer,
       "frUniSigReleaseTimer": frUniSigReleaseTimer,
       "frUniSigCallProceedingTimer": frUniSigCallProceedingTimer,
       "frUniSigNetworkType": frUniSigNetworkType,
       "frUniSigLapfSysTable": frUniSigLapfSysTable,
       "frUniSigLapfSysEntry": frUniSigLapfSysEntry,
       "frUniSigWindowSize": frUniSigWindowSize,
       "frUniSigRetransmitLimit": frUniSigRetransmitLimit,
       "frUniSigAckTimer": frUniSigAckTimer,
       "frUniSigAckDelayTimer": frUniSigAckDelayTimer,
       "frUniSigIdleProbeTimer": frUniSigIdleProbeTimer,
       "frUniSigStateTable": frUniSigStateTable,
       "frUniSigStateEntry": frUniSigStateEntry,
       "frUniSigAdminState": frUniSigAdminState,
       "frUniSigOperationalState": frUniSigOperationalState,
       "frUniSigUsageState": frUniSigUsageState,
       "frUniSigStatsTable": frUniSigStatsTable,
       "frUniSigStatsEntry": frUniSigStatsEntry,
       "frUniSigCurrentNumberOfSvcCalls": frUniSigCurrentNumberOfSvcCalls,
       "frUniSigInCalls": frUniSigInCalls,
       "frUniSigInCallsRefused": frUniSigInCallsRefused,
       "frUniSigOutCalls": frUniSigOutCalls,
       "frUniSigOutCallsFailed": frUniSigOutCallsFailed,
       "frUniSigProtocolErrors": frUniSigProtocolErrors,
       "frUniSigQualityOfServiceNotAvailable": frUniSigQualityOfServiceNotAvailable,
       "frUniSigSetupTimeout": frUniSigSetupTimeout,
       "frUniSigLastCauseInStatusMsgReceived": frUniSigLastCauseInStatusMsgReceived,
       "frUniSigLastStateInStatusMsgReceived": frUniSigLastStateInStatusMsgReceived,
       "frUniSigLastDlciReceivedStatus": frUniSigLastDlciReceivedStatus,
       "frUniSigLastQ933StateReceivedStatus": frUniSigLastQ933StateReceivedStatus,
       "frUniSigLastTimeMsgBlockCongested": frUniSigLastTimeMsgBlockCongested,
       "frUniSigLastDlciWithMsgBlockCongestion": frUniSigLastDlciWithMsgBlockCongestion,
       "frUniSigCurrentAggregateSvcCirNormalQ": frUniSigCurrentAggregateSvcCirNormalQ,
       "frUniSigCurrentAggregateSvcCirHighQ": frUniSigCurrentAggregateSvcCirHighQ,
       "frUniSigCurrentAggregateSvcCirInterruptQ": frUniSigCurrentAggregateSvcCirInterruptQ,
       "frUniSigCurrentAggregateSvcEirNormalQ": frUniSigCurrentAggregateSvcEirNormalQ,
       "frUniSigCurrentAggregateSvcEirHighQ": frUniSigCurrentAggregateSvcEirHighQ,
       "frUniSigCurrentAggregateSvcEirInterruptQ": frUniSigCurrentAggregateSvcEirInterruptQ,
       "frUniSigLapfStatusTable": frUniSigLapfStatusTable,
       "frUniSigLapfStatusEntry": frUniSigLapfStatusEntry,
       "frUniSigCurrentState": frUniSigCurrentState,
       "frUniSigLastStateChangeReason": frUniSigLastStateChangeReason,
       "frUniSigFrmrReceive": frUniSigFrmrReceive,
       "frUniSigCurrentQueueSize": frUniSigCurrentQueueSize,
       "frUniSigLapfStatsTable": frUniSigLapfStatsTable,
       "frUniSigLapfStatsEntry": frUniSigLapfStatsEntry,
       "frUniSigStateChange": frUniSigStateChange,
       "frUniSigRemoteBusy": frUniSigRemoteBusy,
       "frUniSigReceiveRejectFrame": frUniSigReceiveRejectFrame,
       "frUniSigAckTimeout": frUniSigAckTimeout,
       "frUniSigIFramesTransmitted": frUniSigIFramesTransmitted,
       "frUniSigIFramesTxDiscarded": frUniSigIFramesTxDiscarded,
       "frUniSigIFramesReceived": frUniSigIFramesReceived,
       "frUniSigIFramesRcvdDiscarded": frUniSigIFramesRcvdDiscarded,
       "frUniSigSvcaccTable": frUniSigSvcaccTable,
       "frUniSigSvcaccEntry": frUniSigSvcaccEntry,
       "frUniSigDefaultAccounting": frUniSigDefaultAccounting,
       "frUniSigCodesTable": frUniSigCodesTable,
       "frUniSigCodesEntry": frUniSigCodesEntry,
       "frUniSigLastClearRemoteDataNetworkAddress": frUniSigLastClearRemoteDataNetworkAddress,
       "frUniSigLastClearCause": frUniSigLastClearCause,
       "frUniSigLastDiagnosticCode": frUniSigLastDiagnosticCode,
       "frUniVFramer": frUniVFramer,
       "frUniVFramerRowStatusTable": frUniVFramerRowStatusTable,
       "frUniVFramerRowStatusEntry": frUniVFramerRowStatusEntry,
       "frUniVFramerRowStatus": frUniVFramerRowStatus,
       "frUniVFramerComponentName": frUniVFramerComponentName,
       "frUniVFramerStorageType": frUniVFramerStorageType,
       "frUniVFramerIndex": frUniVFramerIndex,
       "frUniVFramerProvTable": frUniVFramerProvTable,
       "frUniVFramerProvEntry": frUniVFramerProvEntry,
       "frUniVFramerOtherVirtualFramer": frUniVFramerOtherVirtualFramer,
       "frUniVFramerLogicalProcessor": frUniVFramerLogicalProcessor,
       "frUniVFramerStateTable": frUniVFramerStateTable,
       "frUniVFramerStateEntry": frUniVFramerStateEntry,
       "frUniVFramerAdminState": frUniVFramerAdminState,
       "frUniVFramerOperationalState": frUniVFramerOperationalState,
       "frUniVFramerUsageState": frUniVFramerUsageState,
       "frUniVFramerStatsTable": frUniVFramerStatsTable,
       "frUniVFramerStatsEntry": frUniVFramerStatsEntry,
       "frUniVFramerFrmToOtherVFramer": frUniVFramerFrmToOtherVFramer,
       "frUniVFramerFrmFromOtherVFramer": frUniVFramerFrmFromOtherVFramer,
       "frUniVFramerOctetFromOtherVFramer": frUniVFramerOctetFromOtherVFramer,
       "frUniLts": frUniLts,
       "frUniLtsRowStatusTable": frUniLtsRowStatusTable,
       "frUniLtsRowStatusEntry": frUniLtsRowStatusEntry,
       "frUniLtsRowStatus": frUniLtsRowStatus,
       "frUniLtsComponentName": frUniLtsComponentName,
       "frUniLtsStorageType": frUniLtsStorageType,
       "frUniLtsIndex": frUniLtsIndex,
       "frUniLtsPat": frUniLtsPat,
       "frUniLtsPatRowStatusTable": frUniLtsPatRowStatusTable,
       "frUniLtsPatRowStatusEntry": frUniLtsPatRowStatusEntry,
       "frUniLtsPatRowStatus": frUniLtsPatRowStatus,
       "frUniLtsPatComponentName": frUniLtsPatComponentName,
       "frUniLtsPatStorageType": frUniLtsPatStorageType,
       "frUniLtsPatIndex": frUniLtsPatIndex,
       "frUniLtsPatDefaultsTable": frUniLtsPatDefaultsTable,
       "frUniLtsPatDefaultsEntry": frUniLtsPatDefaultsEntry,
       "frUniLtsPatDefaultDlci": frUniLtsPatDefaultDlci,
       "frUniLtsPatDefaultNumFrames": frUniLtsPatDefaultNumFrames,
       "frUniLtsPatDefaultDataSize": frUniLtsPatDefaultDataSize,
       "frUniLtsPatDefaultHeaderBits": frUniLtsPatDefaultHeaderBits,
       "frUniLtsPatDefaultHeaderLength": frUniLtsPatDefaultHeaderLength,
       "frUniLtsPatDefaultEABits": frUniLtsPatDefaultEABits,
       "frUniLtsPatDefaultPayloadPattern": frUniLtsPatDefaultPayloadPattern,
       "frUniLtsPatDefaultRfc1490Header": frUniLtsPatDefaultRfc1490Header,
       "frUniLtsPatDefaultUseBadLrc": frUniLtsPatDefaultUseBadLrc,
       "frUniLtsPatSetupTable": frUniLtsPatSetupTable,
       "frUniLtsPatSetupEntry": frUniLtsPatSetupEntry,
       "frUniLtsPatDlci": frUniLtsPatDlci,
       "frUniLtsPatNumFrames": frUniLtsPatNumFrames,
       "frUniLtsPatDataSize": frUniLtsPatDataSize,
       "frUniLtsPatHeaderBits": frUniLtsPatHeaderBits,
       "frUniLtsPatHeaderLength": frUniLtsPatHeaderLength,
       "frUniLtsPatEaBits": frUniLtsPatEaBits,
       "frUniLtsPatPayloadPattern": frUniLtsPatPayloadPattern,
       "frUniLtsPatRfc1490Header": frUniLtsPatRfc1490Header,
       "frUniLtsPatUseBadLrc": frUniLtsPatUseBadLrc,
       "frUniLtsPatOpDataTable": frUniLtsPatOpDataTable,
       "frUniLtsPatOpDataEntry": frUniLtsPatOpDataEntry,
       "frUniLtsPatFramePattern": frUniLtsPatFramePattern,
       "frUniLtsPatHdlcBitsInserted": frUniLtsPatHdlcBitsInserted,
       "frUniLtsPatOpStateTable": frUniLtsPatOpStateTable,
       "frUniLtsPatOpStateEntry": frUniLtsPatOpStateEntry,
       "frUniLtsPatLoad": frUniLtsPatLoad,
       "frUniLtsPatStatus": frUniLtsPatStatus,
       "frUniLtsSetupTable": frUniLtsSetupTable,
       "frUniLtsSetupEntry": frUniLtsSetupEntry,
       "frUniLtsDuration": frUniLtsDuration,
       "frUniLtsAlgorithm": frUniLtsAlgorithm,
       "frUniLtsBurstSize": frUniLtsBurstSize,
       "frUniLtsTimeInterval": frUniLtsTimeInterval,
       "frUniLtsStateTable": frUniLtsStateTable,
       "frUniLtsStateEntry": frUniLtsStateEntry,
       "frUniLtsGeneratorState": frUniLtsGeneratorState,
       "frUniLtsCycleIncomplete": frUniLtsCycleIncomplete,
       "frUniLtsLastActiveInterval": frUniLtsLastActiveInterval,
       "frUniLtsLoad": frUniLtsLoad,
       "frUniLtsElapsedGenerationTime": frUniLtsElapsedGenerationTime,
       "frUniLtsResultsTable": frUniLtsResultsTable,
       "frUniLtsResultsEntry": frUniLtsResultsEntry,
       "frUniLtsFramesTx": frUniLtsFramesTx,
       "frUniLtsBytesTx": frUniLtsBytesTx,
       "frUniLtsBitRateTx": frUniLtsBitRateTx,
       "frUniLtsFrameRateTx": frUniLtsFrameRateTx,
       "frUniCidDataTable": frUniCidDataTable,
       "frUniCidDataEntry": frUniCidDataEntry,
       "frUniCustomerIdentifier": frUniCustomerIdentifier,
       "frUniStateTable": frUniStateTable,
       "frUniStateEntry": frUniStateEntry,
       "frUniAdminState": frUniAdminState,
       "frUniOperationalState": frUniOperationalState,
       "frUniUsageState": frUniUsageState,
       "frUniAvailabilityStatus": frUniAvailabilityStatus,
       "frUniProceduralStatus": frUniProceduralStatus,
       "frUniControlStatus": frUniControlStatus,
       "frUniAlarmStatus": frUniAlarmStatus,
       "frUniStandbyStatus": frUniStandbyStatus,
       "frUniUnknownStatus": frUniUnknownStatus,
       "frUniStatsTable": frUniStatsTable,
       "frUniStatsEntry": frUniStatsEntry,
       "frUniLastUnknownDlci": frUniLastUnknownDlci,
       "frUniUnknownDlciFramesFromIf": frUniUnknownDlciFramesFromIf,
       "frUniInvalidHeaderFramesFromIf": frUniInvalidHeaderFramesFromIf,
       "frUniIfEntryTable": frUniIfEntryTable,
       "frUniIfEntryEntry": frUniIfEntryEntry,
       "frUniIfAdminStatus": frUniIfAdminStatus,
       "frUniIfIndex": frUniIfIndex,
       "frUniOperStatusTable": frUniOperStatusTable,
       "frUniOperStatusEntry": frUniOperStatusEntry,
       "frUniSnmpOperStatus": frUniSnmpOperStatus,
       "frUniEmissionPriorityQsTable": frUniEmissionPriorityQsTable,
       "frUniEmissionPriorityQsEntry": frUniEmissionPriorityQsEntry,
       "frUniNumberOfEmissionQs": frUniNumberOfEmissionQs,
       "frUniFrmToIfByQueueTable": frUniFrmToIfByQueueTable,
       "frUniFrmToIfByQueueEntry": frUniFrmToIfByQueueEntry,
       "frUniFrmToIfByQueueIndex": frUniFrmToIfByQueueIndex,
       "frUniFrmToIfByQueueValue": frUniFrmToIfByQueueValue,
       "frUniOctetToIfByQueueTable": frUniOctetToIfByQueueTable,
       "frUniOctetToIfByQueueEntry": frUniOctetToIfByQueueEntry,
       "frUniOctetToIfByQueueIndex": frUniOctetToIfByQueueIndex,
       "frUniOctetToIfByQueueValue": frUniOctetToIfByQueueValue,
       "frameRelayUniMIB": frameRelayUniMIB,
       "frameRelayUniGroup": frameRelayUniGroup,
       "frameRelayUniGroupBE": frameRelayUniGroupBE,
       "frameRelayUniGroupBE01": frameRelayUniGroupBE01,
       "frameRelayUniGroupBE01A": frameRelayUniGroupBE01A,
       "frameRelayUniCapabilities": frameRelayUniCapabilities,
       "frameRelayUniCapabilitiesBE": frameRelayUniCapabilitiesBE,
       "frameRelayUniCapabilitiesBE01": frameRelayUniCapabilitiesBE01,
       "frameRelayUniCapabilitiesBE01A": frameRelayUniCapabilitiesBE01A}
)
