# SNMP MIB module (Nortel-Magellan-Passport-FrameRelayNniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FrameRelayNniMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:48 2024
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

_FrNni_ObjectIdentity = ObjectIdentity
frNni = _FrNni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70)
)
_FrNniRowStatusTable_Object = MibTable
frNniRowStatusTable = _FrNniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 1)
)
if mibBuilder.loadTexts:
    frNniRowStatusTable.setStatus("mandatory")
_FrNniRowStatusEntry_Object = MibTableRow
frNniRowStatusEntry = _FrNniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 1, 1)
)
frNniRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
)
if mibBuilder.loadTexts:
    frNniRowStatusEntry.setStatus("mandatory")
_FrNniRowStatus_Type = RowStatus
_FrNniRowStatus_Object = MibTableColumn
frNniRowStatus = _FrNniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 1, 1, 1),
    _FrNniRowStatus_Type()
)
frNniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniRowStatus.setStatus("mandatory")
_FrNniComponentName_Type = DisplayString
_FrNniComponentName_Object = MibTableColumn
frNniComponentName = _FrNniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 1, 1, 2),
    _FrNniComponentName_Type()
)
frNniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniComponentName.setStatus("mandatory")
_FrNniStorageType_Type = StorageType
_FrNniStorageType_Object = MibTableColumn
frNniStorageType = _FrNniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 1, 1, 4),
    _FrNniStorageType_Type()
)
frNniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniStorageType.setStatus("mandatory")


class _FrNniIndex_Type(Integer32):
    """Custom type frNniIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrNniIndex_Type.__name__ = "Integer32"
_FrNniIndex_Object = MibTableColumn
frNniIndex = _FrNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 1, 1, 10),
    _FrNniIndex_Type()
)
frNniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniIndex.setStatus("mandatory")
_FrNniDna_ObjectIdentity = ObjectIdentity
frNniDna = _FrNniDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2)
)
_FrNniDnaRowStatusTable_Object = MibTable
frNniDnaRowStatusTable = _FrNniDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 1)
)
if mibBuilder.loadTexts:
    frNniDnaRowStatusTable.setStatus("mandatory")
_FrNniDnaRowStatusEntry_Object = MibTableRow
frNniDnaRowStatusEntry = _FrNniDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 1, 1)
)
frNniDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaRowStatusEntry.setStatus("mandatory")
_FrNniDnaRowStatus_Type = RowStatus
_FrNniDnaRowStatus_Object = MibTableColumn
frNniDnaRowStatus = _FrNniDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 1, 1, 1),
    _FrNniDnaRowStatus_Type()
)
frNniDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaRowStatus.setStatus("mandatory")
_FrNniDnaComponentName_Type = DisplayString
_FrNniDnaComponentName_Object = MibTableColumn
frNniDnaComponentName = _FrNniDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 1, 1, 2),
    _FrNniDnaComponentName_Type()
)
frNniDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaComponentName.setStatus("mandatory")
_FrNniDnaStorageType_Type = StorageType
_FrNniDnaStorageType_Object = MibTableColumn
frNniDnaStorageType = _FrNniDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 1, 1, 4),
    _FrNniDnaStorageType_Type()
)
frNniDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaStorageType.setStatus("mandatory")
_FrNniDnaIndex_Type = NonReplicated
_FrNniDnaIndex_Object = MibTableColumn
frNniDnaIndex = _FrNniDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 1, 1, 10),
    _FrNniDnaIndex_Type()
)
frNniDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDnaIndex.setStatus("mandatory")
_FrNniDnaCug_ObjectIdentity = ObjectIdentity
frNniDnaCug = _FrNniDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2)
)
_FrNniDnaCugRowStatusTable_Object = MibTable
frNniDnaCugRowStatusTable = _FrNniDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 1)
)
if mibBuilder.loadTexts:
    frNniDnaCugRowStatusTable.setStatus("mandatory")
_FrNniDnaCugRowStatusEntry_Object = MibTableRow
frNniDnaCugRowStatusEntry = _FrNniDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 1, 1)
)
frNniDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaCugRowStatusEntry.setStatus("mandatory")
_FrNniDnaCugRowStatus_Type = RowStatus
_FrNniDnaCugRowStatus_Object = MibTableColumn
frNniDnaCugRowStatus = _FrNniDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 1, 1, 1),
    _FrNniDnaCugRowStatus_Type()
)
frNniDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaCugRowStatus.setStatus("mandatory")
_FrNniDnaCugComponentName_Type = DisplayString
_FrNniDnaCugComponentName_Object = MibTableColumn
frNniDnaCugComponentName = _FrNniDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 1, 1, 2),
    _FrNniDnaCugComponentName_Type()
)
frNniDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaCugComponentName.setStatus("mandatory")
_FrNniDnaCugStorageType_Type = StorageType
_FrNniDnaCugStorageType_Object = MibTableColumn
frNniDnaCugStorageType = _FrNniDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 1, 1, 4),
    _FrNniDnaCugStorageType_Type()
)
frNniDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaCugStorageType.setStatus("mandatory")


class _FrNniDnaCugIndex_Type(Integer32):
    """Custom type frNniDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrNniDnaCugIndex_Type.__name__ = "Integer32"
_FrNniDnaCugIndex_Object = MibTableColumn
frNniDnaCugIndex = _FrNniDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 1, 1, 10),
    _FrNniDnaCugIndex_Type()
)
frNniDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDnaCugIndex.setStatus("mandatory")
_FrNniDnaCugCugOptionsTable_Object = MibTable
frNniDnaCugCugOptionsTable = _FrNniDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10)
)
if mibBuilder.loadTexts:
    frNniDnaCugCugOptionsTable.setStatus("mandatory")
_FrNniDnaCugCugOptionsEntry_Object = MibTableRow
frNniDnaCugCugOptionsEntry = _FrNniDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10, 1)
)
frNniDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaCugCugOptionsEntry.setStatus("mandatory")


class _FrNniDnaCugType_Type(Integer32):
    """Custom type frNniDnaCugType based on Integer32"""
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


_FrNniDnaCugType_Type.__name__ = "Integer32"
_FrNniDnaCugType_Object = MibTableColumn
frNniDnaCugType = _FrNniDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10, 1, 1),
    _FrNniDnaCugType_Type()
)
frNniDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaCugType.setStatus("mandatory")


class _FrNniDnaCugDnic_Type(DigitString):
    """Custom type frNniDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_FrNniDnaCugDnic_Type.__name__ = "DigitString"
_FrNniDnaCugDnic_Object = MibTableColumn
frNniDnaCugDnic = _FrNniDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10, 1, 2),
    _FrNniDnaCugDnic_Type()
)
frNniDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaCugDnic.setStatus("mandatory")


class _FrNniDnaCugInterlockCode_Type(Unsigned32):
    """Custom type frNniDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrNniDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_FrNniDnaCugInterlockCode_Object = MibTableColumn
frNniDnaCugInterlockCode = _FrNniDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10, 1, 3),
    _FrNniDnaCugInterlockCode_Type()
)
frNniDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaCugInterlockCode.setStatus("mandatory")


class _FrNniDnaCugPreferential_Type(Integer32):
    """Custom type frNniDnaCugPreferential based on Integer32"""
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


_FrNniDnaCugPreferential_Type.__name__ = "Integer32"
_FrNniDnaCugPreferential_Object = MibTableColumn
frNniDnaCugPreferential = _FrNniDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10, 1, 4),
    _FrNniDnaCugPreferential_Type()
)
frNniDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaCugPreferential.setStatus("mandatory")


class _FrNniDnaCugOutCalls_Type(Integer32):
    """Custom type frNniDnaCugOutCalls based on Integer32"""
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


_FrNniDnaCugOutCalls_Type.__name__ = "Integer32"
_FrNniDnaCugOutCalls_Object = MibTableColumn
frNniDnaCugOutCalls = _FrNniDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10, 1, 5),
    _FrNniDnaCugOutCalls_Type()
)
frNniDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaCugOutCalls.setStatus("mandatory")


class _FrNniDnaCugIncCalls_Type(Integer32):
    """Custom type frNniDnaCugIncCalls based on Integer32"""
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


_FrNniDnaCugIncCalls_Type.__name__ = "Integer32"
_FrNniDnaCugIncCalls_Object = MibTableColumn
frNniDnaCugIncCalls = _FrNniDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 2, 10, 1, 6),
    _FrNniDnaCugIncCalls_Type()
)
frNniDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaCugIncCalls.setStatus("mandatory")
_FrNniDnaHgM_ObjectIdentity = ObjectIdentity
frNniDnaHgM = _FrNniDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3)
)
_FrNniDnaHgMRowStatusTable_Object = MibTable
frNniDnaHgMRowStatusTable = _FrNniDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 1)
)
if mibBuilder.loadTexts:
    frNniDnaHgMRowStatusTable.setStatus("mandatory")
_FrNniDnaHgMRowStatusEntry_Object = MibTableRow
frNniDnaHgMRowStatusEntry = _FrNniDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 1, 1)
)
frNniDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaHgMRowStatusEntry.setStatus("mandatory")
_FrNniDnaHgMRowStatus_Type = RowStatus
_FrNniDnaHgMRowStatus_Object = MibTableColumn
frNniDnaHgMRowStatus = _FrNniDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 1, 1, 1),
    _FrNniDnaHgMRowStatus_Type()
)
frNniDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaHgMRowStatus.setStatus("mandatory")
_FrNniDnaHgMComponentName_Type = DisplayString
_FrNniDnaHgMComponentName_Object = MibTableColumn
frNniDnaHgMComponentName = _FrNniDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 1, 1, 2),
    _FrNniDnaHgMComponentName_Type()
)
frNniDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMComponentName.setStatus("mandatory")
_FrNniDnaHgMStorageType_Type = StorageType
_FrNniDnaHgMStorageType_Object = MibTableColumn
frNniDnaHgMStorageType = _FrNniDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 1, 1, 4),
    _FrNniDnaHgMStorageType_Type()
)
frNniDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMStorageType.setStatus("mandatory")
_FrNniDnaHgMIndex_Type = NonReplicated
_FrNniDnaHgMIndex_Object = MibTableColumn
frNniDnaHgMIndex = _FrNniDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 1, 1, 10),
    _FrNniDnaHgMIndex_Type()
)
frNniDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDnaHgMIndex.setStatus("mandatory")
_FrNniDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
frNniDnaHgMHgAddr = _FrNniDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2)
)
_FrNniDnaHgMHgAddrRowStatusTable_Object = MibTable
frNniDnaHgMHgAddrRowStatusTable = _FrNniDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_FrNniDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
frNniDnaHgMHgAddrRowStatusEntry = _FrNniDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 1, 1)
)
frNniDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_FrNniDnaHgMHgAddrRowStatus_Type = RowStatus
_FrNniDnaHgMHgAddrRowStatus_Object = MibTableColumn
frNniDnaHgMHgAddrRowStatus = _FrNniDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 1, 1, 1),
    _FrNniDnaHgMHgAddrRowStatus_Type()
)
frNniDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrRowStatus.setStatus("mandatory")
_FrNniDnaHgMHgAddrComponentName_Type = DisplayString
_FrNniDnaHgMHgAddrComponentName_Object = MibTableColumn
frNniDnaHgMHgAddrComponentName = _FrNniDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 1, 1, 2),
    _FrNniDnaHgMHgAddrComponentName_Type()
)
frNniDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrComponentName.setStatus("mandatory")
_FrNniDnaHgMHgAddrStorageType_Type = StorageType
_FrNniDnaHgMHgAddrStorageType_Object = MibTableColumn
frNniDnaHgMHgAddrStorageType = _FrNniDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 1, 1, 4),
    _FrNniDnaHgMHgAddrStorageType_Type()
)
frNniDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrStorageType.setStatus("mandatory")


class _FrNniDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type frNniDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FrNniDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_FrNniDnaHgMHgAddrIndex_Object = MibTableColumn
frNniDnaHgMHgAddrIndex = _FrNniDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 1, 1, 10),
    _FrNniDnaHgMHgAddrIndex_Type()
)
frNniDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrIndex.setStatus("mandatory")
_FrNniDnaHgMHgAddrAddrTable_Object = MibTable
frNniDnaHgMHgAddrAddrTable = _FrNniDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrAddrTable.setStatus("mandatory")
_FrNniDnaHgMHgAddrAddrEntry_Object = MibTableRow
frNniDnaHgMHgAddrAddrEntry = _FrNniDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 10, 1)
)
frNniDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaHgMIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _FrNniDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type frNniDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
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


_FrNniDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_FrNniDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
frNniDnaHgMHgAddrNumberingPlanIndicator = _FrNniDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 10, 1, 1),
    _FrNniDnaHgMHgAddrNumberingPlanIndicator_Type()
)
frNniDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _FrNniDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type frNniDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrNniDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_FrNniDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
frNniDnaHgMHgAddrDataNetworkAddress = _FrNniDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 2, 10, 1, 2),
    _FrNniDnaHgMHgAddrDataNetworkAddress_Type()
)
frNniDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_FrNniDnaHgMIfTable_Object = MibTable
frNniDnaHgMIfTable = _FrNniDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 10)
)
if mibBuilder.loadTexts:
    frNniDnaHgMIfTable.setStatus("mandatory")
_FrNniDnaHgMIfEntry_Object = MibTableRow
frNniDnaHgMIfEntry = _FrNniDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 10, 1)
)
frNniDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaHgMIfEntry.setStatus("mandatory")


class _FrNniDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type frNniDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 16777216),
    )


_FrNniDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_FrNniDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
frNniDnaHgMAvailabilityUpdateThreshold = _FrNniDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 10, 1, 1),
    _FrNniDnaHgMAvailabilityUpdateThreshold_Type()
)
frNniDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_FrNniDnaHgMOpTable_Object = MibTable
frNniDnaHgMOpTable = _FrNniDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 11)
)
if mibBuilder.loadTexts:
    frNniDnaHgMOpTable.setStatus("mandatory")
_FrNniDnaHgMOpEntry_Object = MibTableRow
frNniDnaHgMOpEntry = _FrNniDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 11, 1)
)
frNniDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaHgMOpEntry.setStatus("mandatory")


class _FrNniDnaHgMMaximumAvailableAggregateCir_Type(Unsigned32):
    """Custom type frNniDnaHgMMaximumAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDnaHgMMaximumAvailableAggregateCir_Type.__name__ = "Unsigned32"
_FrNniDnaHgMMaximumAvailableAggregateCir_Object = MibTableColumn
frNniDnaHgMMaximumAvailableAggregateCir = _FrNniDnaHgMMaximumAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 11, 1, 1),
    _FrNniDnaHgMMaximumAvailableAggregateCir_Type()
)
frNniDnaHgMMaximumAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMMaximumAvailableAggregateCir.setStatus("mandatory")


class _FrNniDnaHgMAvailableAggregateCir_Type(Unsigned32):
    """Custom type frNniDnaHgMAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDnaHgMAvailableAggregateCir_Type.__name__ = "Unsigned32"
_FrNniDnaHgMAvailableAggregateCir_Object = MibTableColumn
frNniDnaHgMAvailableAggregateCir = _FrNniDnaHgMAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 11, 1, 2),
    _FrNniDnaHgMAvailableAggregateCir_Type()
)
frNniDnaHgMAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMAvailableAggregateCir.setStatus("mandatory")


class _FrNniDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type frNniDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16777216, 16777215),
    )


_FrNniDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_FrNniDnaHgMAvailabilityDelta_Object = MibTableColumn
frNniDnaHgMAvailabilityDelta = _FrNniDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 11, 1, 3),
    _FrNniDnaHgMAvailabilityDelta_Type()
)
frNniDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMAvailabilityDelta.setStatus("mandatory")


class _FrNniDnaHgMAvailableDlcis_Type(Unsigned32):
    """Custom type frNniDnaHgMAvailableDlcis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FrNniDnaHgMAvailableDlcis_Type.__name__ = "Unsigned32"
_FrNniDnaHgMAvailableDlcis_Object = MibTableColumn
frNniDnaHgMAvailableDlcis = _FrNniDnaHgMAvailableDlcis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 3, 11, 1, 5),
    _FrNniDnaHgMAvailableDlcis_Type()
)
frNniDnaHgMAvailableDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDnaHgMAvailableDlcis.setStatus("mandatory")
_FrNniDnaAddressTable_Object = MibTable
frNniDnaAddressTable = _FrNniDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 10)
)
if mibBuilder.loadTexts:
    frNniDnaAddressTable.setStatus("mandatory")
_FrNniDnaAddressEntry_Object = MibTableRow
frNniDnaAddressEntry = _FrNniDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 10, 1)
)
frNniDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaAddressEntry.setStatus("mandatory")


class _FrNniDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type frNniDnaNumberingPlanIndicator based on Integer32"""
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


_FrNniDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_FrNniDnaNumberingPlanIndicator_Object = MibTableColumn
frNniDnaNumberingPlanIndicator = _FrNniDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 10, 1, 1),
    _FrNniDnaNumberingPlanIndicator_Type()
)
frNniDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaNumberingPlanIndicator.setStatus("mandatory")


class _FrNniDnaDataNetworkAddress_Type(DigitString):
    """Custom type frNniDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrNniDnaDataNetworkAddress_Type.__name__ = "DigitString"
_FrNniDnaDataNetworkAddress_Object = MibTableColumn
frNniDnaDataNetworkAddress = _FrNniDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 10, 1, 2),
    _FrNniDnaDataNetworkAddress_Type()
)
frNniDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaDataNetworkAddress.setStatus("mandatory")
_FrNniDnaOutgoingOptionsTable_Object = MibTable
frNniDnaOutgoingOptionsTable = _FrNniDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11)
)
if mibBuilder.loadTexts:
    frNniDnaOutgoingOptionsTable.setStatus("mandatory")
_FrNniDnaOutgoingOptionsEntry_Object = MibTableRow
frNniDnaOutgoingOptionsEntry = _FrNniDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1)
)
frNniDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaOutgoingOptionsEntry.setStatus("mandatory")


class _FrNniDnaOutDefaultPriority_Type(Integer32):
    """Custom type frNniDnaOutDefaultPriority based on Integer32"""
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


_FrNniDnaOutDefaultPriority_Type.__name__ = "Integer32"
_FrNniDnaOutDefaultPriority_Object = MibTableColumn
frNniDnaOutDefaultPriority = _FrNniDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1, 7),
    _FrNniDnaOutDefaultPriority_Type()
)
frNniDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaOutDefaultPriority.setStatus("mandatory")


class _FrNniDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type frNniDnaOutDefaultPathSensitivity based on Integer32"""
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


_FrNniDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_FrNniDnaOutDefaultPathSensitivity_Object = MibTableColumn
frNniDnaOutDefaultPathSensitivity = _FrNniDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1, 11),
    _FrNniDnaOutDefaultPathSensitivity_Type()
)
frNniDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _FrNniDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type frNniDnaOutPathSensitivityOverRide based on Integer32"""
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


_FrNniDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_FrNniDnaOutPathSensitivityOverRide_Object = MibTableColumn
frNniDnaOutPathSensitivityOverRide = _FrNniDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1, 12),
    _FrNniDnaOutPathSensitivityOverRide_Type()
)
frNniDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _FrNniDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type frNniDnaOutDefaultPathReliability based on Integer32"""
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


_FrNniDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_FrNniDnaOutDefaultPathReliability_Object = MibTableColumn
frNniDnaOutDefaultPathReliability = _FrNniDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1, 14),
    _FrNniDnaOutDefaultPathReliability_Type()
)
frNniDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaOutDefaultPathReliability.setStatus("mandatory")


class _FrNniDnaOutAccess_Type(Integer32):
    """Custom type frNniDnaOutAccess based on Integer32"""
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


_FrNniDnaOutAccess_Type.__name__ = "Integer32"
_FrNniDnaOutAccess_Object = MibTableColumn
frNniDnaOutAccess = _FrNniDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1, 17),
    _FrNniDnaOutAccess_Type()
)
frNniDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaOutAccess.setStatus("mandatory")


class _FrNniDnaDefaultTransferPriority_Type(Integer32):
    """Custom type frNniDnaDefaultTransferPriority based on Integer32"""
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


_FrNniDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_FrNniDnaDefaultTransferPriority_Object = MibTableColumn
frNniDnaDefaultTransferPriority = _FrNniDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1, 18),
    _FrNniDnaDefaultTransferPriority_Type()
)
frNniDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaDefaultTransferPriority.setStatus("mandatory")


class _FrNniDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type frNniDnaTransferPriorityOverRide based on Integer32"""
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


_FrNniDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_FrNniDnaTransferPriorityOverRide_Object = MibTableColumn
frNniDnaTransferPriorityOverRide = _FrNniDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 11, 1, 19),
    _FrNniDnaTransferPriorityOverRide_Type()
)
frNniDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaTransferPriorityOverRide.setStatus("mandatory")
_FrNniDnaIncomingOptionsTable_Object = MibTable
frNniDnaIncomingOptionsTable = _FrNniDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 12)
)
if mibBuilder.loadTexts:
    frNniDnaIncomingOptionsTable.setStatus("mandatory")
_FrNniDnaIncomingOptionsEntry_Object = MibTableRow
frNniDnaIncomingOptionsEntry = _FrNniDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 12, 1)
)
frNniDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaIncomingOptionsEntry.setStatus("mandatory")


class _FrNniDnaIncAccess_Type(Integer32):
    """Custom type frNniDnaIncAccess based on Integer32"""
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


_FrNniDnaIncAccess_Type.__name__ = "Integer32"
_FrNniDnaIncAccess_Object = MibTableColumn
frNniDnaIncAccess = _FrNniDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 12, 1, 9),
    _FrNniDnaIncAccess_Type()
)
frNniDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaIncAccess.setStatus("mandatory")
_FrNniDnaCallOptionsTable_Object = MibTable
frNniDnaCallOptionsTable = _FrNniDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 13)
)
if mibBuilder.loadTexts:
    frNniDnaCallOptionsTable.setStatus("mandatory")
_FrNniDnaCallOptionsEntry_Object = MibTableRow
frNniDnaCallOptionsEntry = _FrNniDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 13, 1)
)
frNniDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDnaIndex"),
)
if mibBuilder.loadTexts:
    frNniDnaCallOptionsEntry.setStatus("mandatory")


class _FrNniDnaAccountClass_Type(Unsigned32):
    """Custom type frNniDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrNniDnaAccountClass_Type.__name__ = "Unsigned32"
_FrNniDnaAccountClass_Object = MibTableColumn
frNniDnaAccountClass = _FrNniDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 13, 1, 10),
    _FrNniDnaAccountClass_Type()
)
frNniDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaAccountClass.setStatus("mandatory")


class _FrNniDnaAccountCollection_Type(OctetString):
    """Custom type frNniDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniDnaAccountCollection_Type.__name__ = "OctetString"
_FrNniDnaAccountCollection_Object = MibTableColumn
frNniDnaAccountCollection = _FrNniDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 13, 1, 11),
    _FrNniDnaAccountCollection_Type()
)
frNniDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaAccountCollection.setStatus("mandatory")


class _FrNniDnaServiceExchange_Type(Unsigned32):
    """Custom type frNniDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrNniDnaServiceExchange_Type.__name__ = "Unsigned32"
_FrNniDnaServiceExchange_Object = MibTableColumn
frNniDnaServiceExchange = _FrNniDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 13, 1, 12),
    _FrNniDnaServiceExchange_Type()
)
frNniDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaServiceExchange.setStatus("mandatory")


class _FrNniDnaEgressAccounting_Type(Integer32):
    """Custom type frNniDnaEgressAccounting based on Integer32"""
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


_FrNniDnaEgressAccounting_Type.__name__ = "Integer32"
_FrNniDnaEgressAccounting_Object = MibTableColumn
frNniDnaEgressAccounting = _FrNniDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 13, 1, 13),
    _FrNniDnaEgressAccounting_Type()
)
frNniDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaEgressAccounting.setStatus("mandatory")


class _FrNniDnaDataPath_Type(Integer32):
    """Custom type frNniDnaDataPath based on Integer32"""
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


_FrNniDnaDataPath_Type.__name__ = "Integer32"
_FrNniDnaDataPath_Object = MibTableColumn
frNniDnaDataPath = _FrNniDnaDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 2, 13, 1, 21),
    _FrNniDnaDataPath_Type()
)
frNniDnaDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDnaDataPath.setStatus("mandatory")
_FrNniFramer_ObjectIdentity = ObjectIdentity
frNniFramer = _FrNniFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3)
)
_FrNniFramerRowStatusTable_Object = MibTable
frNniFramerRowStatusTable = _FrNniFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 1)
)
if mibBuilder.loadTexts:
    frNniFramerRowStatusTable.setStatus("mandatory")
_FrNniFramerRowStatusEntry_Object = MibTableRow
frNniFramerRowStatusEntry = _FrNniFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 1, 1)
)
frNniFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniFramerRowStatusEntry.setStatus("mandatory")
_FrNniFramerRowStatus_Type = RowStatus
_FrNniFramerRowStatus_Object = MibTableColumn
frNniFramerRowStatus = _FrNniFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 1, 1, 1),
    _FrNniFramerRowStatus_Type()
)
frNniFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniFramerRowStatus.setStatus("mandatory")
_FrNniFramerComponentName_Type = DisplayString
_FrNniFramerComponentName_Object = MibTableColumn
frNniFramerComponentName = _FrNniFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 1, 1, 2),
    _FrNniFramerComponentName_Type()
)
frNniFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerComponentName.setStatus("mandatory")
_FrNniFramerStorageType_Type = StorageType
_FrNniFramerStorageType_Object = MibTableColumn
frNniFramerStorageType = _FrNniFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 1, 1, 4),
    _FrNniFramerStorageType_Type()
)
frNniFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerStorageType.setStatus("mandatory")
_FrNniFramerIndex_Type = NonReplicated
_FrNniFramerIndex_Object = MibTableColumn
frNniFramerIndex = _FrNniFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 1, 1, 10),
    _FrNniFramerIndex_Type()
)
frNniFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniFramerIndex.setStatus("mandatory")
_FrNniFramerProvTable_Object = MibTable
frNniFramerProvTable = _FrNniFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 10)
)
if mibBuilder.loadTexts:
    frNniFramerProvTable.setStatus("mandatory")
_FrNniFramerProvEntry_Object = MibTableRow
frNniFramerProvEntry = _FrNniFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 10, 1)
)
frNniFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniFramerProvEntry.setStatus("mandatory")
_FrNniFramerInterfaceName_Type = Link
_FrNniFramerInterfaceName_Object = MibTableColumn
frNniFramerInterfaceName = _FrNniFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 10, 1, 1),
    _FrNniFramerInterfaceName_Type()
)
frNniFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniFramerInterfaceName.setStatus("mandatory")
_FrNniFramerLinkTable_Object = MibTable
frNniFramerLinkTable = _FrNniFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 11)
)
if mibBuilder.loadTexts:
    frNniFramerLinkTable.setStatus("mandatory")
_FrNniFramerLinkEntry_Object = MibTableRow
frNniFramerLinkEntry = _FrNniFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 11, 1)
)
frNniFramerLinkEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniFramerLinkEntry.setStatus("mandatory")


class _FrNniFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type frNniFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FrNniFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_FrNniFramerFlagsBetweenFrames_Object = MibTableColumn
frNniFramerFlagsBetweenFrames = _FrNniFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 11, 1, 4),
    _FrNniFramerFlagsBetweenFrames_Type()
)
frNniFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniFramerFlagsBetweenFrames.setStatus("mandatory")
_FrNniFramerStateTable_Object = MibTable
frNniFramerStateTable = _FrNniFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 12)
)
if mibBuilder.loadTexts:
    frNniFramerStateTable.setStatus("mandatory")
_FrNniFramerStateEntry_Object = MibTableRow
frNniFramerStateEntry = _FrNniFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 12, 1)
)
frNniFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniFramerStateEntry.setStatus("mandatory")


class _FrNniFramerAdminState_Type(Integer32):
    """Custom type frNniFramerAdminState based on Integer32"""
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


_FrNniFramerAdminState_Type.__name__ = "Integer32"
_FrNniFramerAdminState_Object = MibTableColumn
frNniFramerAdminState = _FrNniFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 12, 1, 1),
    _FrNniFramerAdminState_Type()
)
frNniFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerAdminState.setStatus("mandatory")


class _FrNniFramerOperationalState_Type(Integer32):
    """Custom type frNniFramerOperationalState based on Integer32"""
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


_FrNniFramerOperationalState_Type.__name__ = "Integer32"
_FrNniFramerOperationalState_Object = MibTableColumn
frNniFramerOperationalState = _FrNniFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 12, 1, 2),
    _FrNniFramerOperationalState_Type()
)
frNniFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerOperationalState.setStatus("mandatory")


class _FrNniFramerUsageState_Type(Integer32):
    """Custom type frNniFramerUsageState based on Integer32"""
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


_FrNniFramerUsageState_Type.__name__ = "Integer32"
_FrNniFramerUsageState_Object = MibTableColumn
frNniFramerUsageState = _FrNniFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 12, 1, 3),
    _FrNniFramerUsageState_Type()
)
frNniFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerUsageState.setStatus("mandatory")
_FrNniFramerStatsTable_Object = MibTable
frNniFramerStatsTable = _FrNniFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13)
)
if mibBuilder.loadTexts:
    frNniFramerStatsTable.setStatus("mandatory")
_FrNniFramerStatsEntry_Object = MibTableRow
frNniFramerStatsEntry = _FrNniFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1)
)
frNniFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniFramerStatsEntry.setStatus("mandatory")
_FrNniFramerFrmToIf_Type = Counter32
_FrNniFramerFrmToIf_Object = MibTableColumn
frNniFramerFrmToIf = _FrNniFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 1),
    _FrNniFramerFrmToIf_Type()
)
frNniFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerFrmToIf.setStatus("mandatory")
_FrNniFramerFrmFromIf_Type = Counter32
_FrNniFramerFrmFromIf_Object = MibTableColumn
frNniFramerFrmFromIf = _FrNniFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 2),
    _FrNniFramerFrmFromIf_Type()
)
frNniFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerFrmFromIf.setStatus("mandatory")
_FrNniFramerOctetFromIf_Type = Counter32
_FrNniFramerOctetFromIf_Object = MibTableColumn
frNniFramerOctetFromIf = _FrNniFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 3),
    _FrNniFramerOctetFromIf_Type()
)
frNniFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerOctetFromIf.setStatus("mandatory")
_FrNniFramerAborts_Type = Counter32
_FrNniFramerAborts_Object = MibTableColumn
frNniFramerAborts = _FrNniFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 4),
    _FrNniFramerAborts_Type()
)
frNniFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerAborts.setStatus("mandatory")
_FrNniFramerCrcErrors_Type = Counter32
_FrNniFramerCrcErrors_Object = MibTableColumn
frNniFramerCrcErrors = _FrNniFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 5),
    _FrNniFramerCrcErrors_Type()
)
frNniFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerCrcErrors.setStatus("mandatory")
_FrNniFramerLrcErrors_Type = Counter32
_FrNniFramerLrcErrors_Object = MibTableColumn
frNniFramerLrcErrors = _FrNniFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 6),
    _FrNniFramerLrcErrors_Type()
)
frNniFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerLrcErrors.setStatus("mandatory")
_FrNniFramerNonOctetErrors_Type = Counter32
_FrNniFramerNonOctetErrors_Object = MibTableColumn
frNniFramerNonOctetErrors = _FrNniFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 7),
    _FrNniFramerNonOctetErrors_Type()
)
frNniFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerNonOctetErrors.setStatus("mandatory")
_FrNniFramerOverruns_Type = Counter32
_FrNniFramerOverruns_Object = MibTableColumn
frNniFramerOverruns = _FrNniFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 8),
    _FrNniFramerOverruns_Type()
)
frNniFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerOverruns.setStatus("mandatory")
_FrNniFramerUnderruns_Type = Counter32
_FrNniFramerUnderruns_Object = MibTableColumn
frNniFramerUnderruns = _FrNniFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 9),
    _FrNniFramerUnderruns_Type()
)
frNniFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerUnderruns.setStatus("mandatory")
_FrNniFramerLargeFrmErrors_Type = Counter32
_FrNniFramerLargeFrmErrors_Object = MibTableColumn
frNniFramerLargeFrmErrors = _FrNniFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 10),
    _FrNniFramerLargeFrmErrors_Type()
)
frNniFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerLargeFrmErrors.setStatus("mandatory")
_FrNniFramerFrmModeErrors_Type = Counter32
_FrNniFramerFrmModeErrors_Object = MibTableColumn
frNniFramerFrmModeErrors = _FrNniFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 13, 1, 11),
    _FrNniFramerFrmModeErrors_Type()
)
frNniFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerFrmModeErrors.setStatus("mandatory")
_FrNniFramerUtilTable_Object = MibTable
frNniFramerUtilTable = _FrNniFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 14)
)
if mibBuilder.loadTexts:
    frNniFramerUtilTable.setStatus("mandatory")
_FrNniFramerUtilEntry_Object = MibTableRow
frNniFramerUtilEntry = _FrNniFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 14, 1)
)
frNniFramerUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniFramerUtilEntry.setStatus("mandatory")


class _FrNniFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type frNniFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrNniFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_FrNniFramerNormPrioLinkUtilToIf_Object = MibTableColumn
frNniFramerNormPrioLinkUtilToIf = _FrNniFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 14, 1, 1),
    _FrNniFramerNormPrioLinkUtilToIf_Type()
)
frNniFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _FrNniFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type frNniFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrNniFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_FrNniFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
frNniFramerNormPrioLinkUtilFromIf = _FrNniFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 3, 14, 1, 3),
    _FrNniFramerNormPrioLinkUtilFromIf_Type()
)
frNniFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_FrNniLmi_ObjectIdentity = ObjectIdentity
frNniLmi = _FrNniLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4)
)
_FrNniLmiRowStatusTable_Object = MibTable
frNniLmiRowStatusTable = _FrNniLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 1)
)
if mibBuilder.loadTexts:
    frNniLmiRowStatusTable.setStatus("mandatory")
_FrNniLmiRowStatusEntry_Object = MibTableRow
frNniLmiRowStatusEntry = _FrNniLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 1, 1)
)
frNniLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLmiIndex"),
)
if mibBuilder.loadTexts:
    frNniLmiRowStatusEntry.setStatus("mandatory")
_FrNniLmiRowStatus_Type = RowStatus
_FrNniLmiRowStatus_Object = MibTableColumn
frNniLmiRowStatus = _FrNniLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 1, 1, 1),
    _FrNniLmiRowStatus_Type()
)
frNniLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiRowStatus.setStatus("mandatory")
_FrNniLmiComponentName_Type = DisplayString
_FrNniLmiComponentName_Object = MibTableColumn
frNniLmiComponentName = _FrNniLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 1, 1, 2),
    _FrNniLmiComponentName_Type()
)
frNniLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiComponentName.setStatus("mandatory")
_FrNniLmiStorageType_Type = StorageType
_FrNniLmiStorageType_Object = MibTableColumn
frNniLmiStorageType = _FrNniLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 1, 1, 4),
    _FrNniLmiStorageType_Type()
)
frNniLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiStorageType.setStatus("mandatory")
_FrNniLmiIndex_Type = NonReplicated
_FrNniLmiIndex_Object = MibTableColumn
frNniLmiIndex = _FrNniLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 1, 1, 10),
    _FrNniLmiIndex_Type()
)
frNniLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniLmiIndex.setStatus("mandatory")
_FrNniLmiParmsTable_Object = MibTable
frNniLmiParmsTable = _FrNniLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10)
)
if mibBuilder.loadTexts:
    frNniLmiParmsTable.setStatus("mandatory")
_FrNniLmiParmsEntry_Object = MibTableRow
frNniLmiParmsEntry = _FrNniLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10, 1)
)
frNniLmiParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLmiIndex"),
)
if mibBuilder.loadTexts:
    frNniLmiParmsEntry.setStatus("mandatory")


class _FrNniLmiProcedures_Type(Integer32):
    """Custom type frNniLmiProcedures based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("autoConfigure", 4),
          ("itu", 3),
          ("none", 0))
    )


_FrNniLmiProcedures_Type.__name__ = "Integer32"
_FrNniLmiProcedures_Object = MibTableColumn
frNniLmiProcedures = _FrNniLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10, 1, 1),
    _FrNniLmiProcedures_Type()
)
frNniLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiProcedures.setStatus("mandatory")


class _FrNniLmiAsyncStatusReport_Type(Integer32):
    """Custom type frNniLmiAsyncStatusReport based on Integer32"""
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


_FrNniLmiAsyncStatusReport_Type.__name__ = "Integer32"
_FrNniLmiAsyncStatusReport_Object = MibTableColumn
frNniLmiAsyncStatusReport = _FrNniLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10, 1, 2),
    _FrNniLmiAsyncStatusReport_Type()
)
frNniLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiAsyncStatusReport.setStatus("mandatory")


class _FrNniLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type frNniLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrNniLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_FrNniLmiErrorEventThreshold_Object = MibTableColumn
frNniLmiErrorEventThreshold = _FrNniLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10, 1, 3),
    _FrNniLmiErrorEventThreshold_Type()
)
frNniLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiErrorEventThreshold.setStatus("mandatory")


class _FrNniLmiEventCount_Type(Unsigned32):
    """Custom type frNniLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrNniLmiEventCount_Type.__name__ = "Unsigned32"
_FrNniLmiEventCount_Object = MibTableColumn
frNniLmiEventCount = _FrNniLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10, 1, 4),
    _FrNniLmiEventCount_Type()
)
frNniLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiEventCount.setStatus("mandatory")


class _FrNniLmiCheckPointTimer_Type(Unsigned32):
    """Custom type frNniLmiCheckPointTimer based on Unsigned32"""
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


_FrNniLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_FrNniLmiCheckPointTimer_Object = MibTableColumn
frNniLmiCheckPointTimer = _FrNniLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10, 1, 5),
    _FrNniLmiCheckPointTimer_Type()
)
frNniLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiCheckPointTimer.setStatus("mandatory")


class _FrNniLmiIgnoreActiveBit_Type(Integer32):
    """Custom type frNniLmiIgnoreActiveBit based on Integer32"""
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


_FrNniLmiIgnoreActiveBit_Type.__name__ = "Integer32"
_FrNniLmiIgnoreActiveBit_Object = MibTableColumn
frNniLmiIgnoreActiveBit = _FrNniLmiIgnoreActiveBit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 10, 1, 7),
    _FrNniLmiIgnoreActiveBit_Type()
)
frNniLmiIgnoreActiveBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiIgnoreActiveBit.setStatus("mandatory")
_FrNniLmiNniParmsTable_Object = MibTable
frNniLmiNniParmsTable = _FrNniLmiNniParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 11)
)
if mibBuilder.loadTexts:
    frNniLmiNniParmsTable.setStatus("mandatory")
_FrNniLmiNniParmsEntry_Object = MibTableRow
frNniLmiNniParmsEntry = _FrNniLmiNniParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 11, 1)
)
frNniLmiNniParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLmiIndex"),
)
if mibBuilder.loadTexts:
    frNniLmiNniParmsEntry.setStatus("mandatory")


class _FrNniLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type frNniLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrNniLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_FrNniLmiFullStatusPollingCycles_Object = MibTableColumn
frNniLmiFullStatusPollingCycles = _FrNniLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 11, 1, 1),
    _FrNniLmiFullStatusPollingCycles_Type()
)
frNniLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiFullStatusPollingCycles.setStatus("mandatory")


class _FrNniLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type frNniLmiLinkVerificationTimer based on Unsigned32"""
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


_FrNniLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_FrNniLmiLinkVerificationTimer_Object = MibTableColumn
frNniLmiLinkVerificationTimer = _FrNniLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 11, 1, 2),
    _FrNniLmiLinkVerificationTimer_Type()
)
frNniLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLmiLinkVerificationTimer.setStatus("mandatory")
_FrNniLmiStateTable_Object = MibTable
frNniLmiStateTable = _FrNniLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 12)
)
if mibBuilder.loadTexts:
    frNniLmiStateTable.setStatus("mandatory")
_FrNniLmiStateEntry_Object = MibTableRow
frNniLmiStateEntry = _FrNniLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 12, 1)
)
frNniLmiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLmiIndex"),
)
if mibBuilder.loadTexts:
    frNniLmiStateEntry.setStatus("mandatory")


class _FrNniLmiAdminState_Type(Integer32):
    """Custom type frNniLmiAdminState based on Integer32"""
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


_FrNniLmiAdminState_Type.__name__ = "Integer32"
_FrNniLmiAdminState_Object = MibTableColumn
frNniLmiAdminState = _FrNniLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 12, 1, 1),
    _FrNniLmiAdminState_Type()
)
frNniLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiAdminState.setStatus("mandatory")


class _FrNniLmiOperationalState_Type(Integer32):
    """Custom type frNniLmiOperationalState based on Integer32"""
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


_FrNniLmiOperationalState_Type.__name__ = "Integer32"
_FrNniLmiOperationalState_Object = MibTableColumn
frNniLmiOperationalState = _FrNniLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 12, 1, 2),
    _FrNniLmiOperationalState_Type()
)
frNniLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiOperationalState.setStatus("mandatory")


class _FrNniLmiUsageState_Type(Integer32):
    """Custom type frNniLmiUsageState based on Integer32"""
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


_FrNniLmiUsageState_Type.__name__ = "Integer32"
_FrNniLmiUsageState_Object = MibTableColumn
frNniLmiUsageState = _FrNniLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 12, 1, 3),
    _FrNniLmiUsageState_Type()
)
frNniLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiUsageState.setStatus("mandatory")
_FrNniLmiPsiTable_Object = MibTable
frNniLmiPsiTable = _FrNniLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 13)
)
if mibBuilder.loadTexts:
    frNniLmiPsiTable.setStatus("mandatory")
_FrNniLmiPsiEntry_Object = MibTableRow
frNniLmiPsiEntry = _FrNniLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 13, 1)
)
frNniLmiPsiEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLmiIndex"),
)
if mibBuilder.loadTexts:
    frNniLmiPsiEntry.setStatus("mandatory")


class _FrNniLmiProtocolStatus_Type(Integer32):
    """Custom type frNniLmiProtocolStatus based on Integer32"""
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


_FrNniLmiProtocolStatus_Type.__name__ = "Integer32"
_FrNniLmiProtocolStatus_Object = MibTableColumn
frNniLmiProtocolStatus = _FrNniLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 13, 1, 1),
    _FrNniLmiProtocolStatus_Type()
)
frNniLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiProtocolStatus.setStatus("mandatory")


class _FrNniLmiOpProcedures_Type(Integer32):
    """Custom type frNniLmiOpProcedures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 2),
          ("itu", 3),
          ("none", 0),
          ("unknown", 4))
    )


_FrNniLmiOpProcedures_Type.__name__ = "Integer32"
_FrNniLmiOpProcedures_Object = MibTableColumn
frNniLmiOpProcedures = _FrNniLmiOpProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 13, 1, 2),
    _FrNniLmiOpProcedures_Type()
)
frNniLmiOpProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiOpProcedures.setStatus("mandatory")
_FrNniLmiStatsTable_Object = MibTable
frNniLmiStatsTable = _FrNniLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14)
)
if mibBuilder.loadTexts:
    frNniLmiStatsTable.setStatus("mandatory")
_FrNniLmiStatsEntry_Object = MibTableRow
frNniLmiStatsEntry = _FrNniLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1)
)
frNniLmiStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLmiIndex"),
)
if mibBuilder.loadTexts:
    frNniLmiStatsEntry.setStatus("mandatory")
_FrNniLmiKeepAliveStatusToIf_Type = Counter32
_FrNniLmiKeepAliveStatusToIf_Object = MibTableColumn
frNniLmiKeepAliveStatusToIf = _FrNniLmiKeepAliveStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 1),
    _FrNniLmiKeepAliveStatusToIf_Type()
)
frNniLmiKeepAliveStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiKeepAliveStatusToIf.setStatus("mandatory")
_FrNniLmiFullStatusToIf_Type = Counter32
_FrNniLmiFullStatusToIf_Object = MibTableColumn
frNniLmiFullStatusToIf = _FrNniLmiFullStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 2),
    _FrNniLmiFullStatusToIf_Type()
)
frNniLmiFullStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiFullStatusToIf.setStatus("mandatory")
_FrNniLmiKeepAliveStatusEnqFromIf_Type = Counter32
_FrNniLmiKeepAliveStatusEnqFromIf_Object = MibTableColumn
frNniLmiKeepAliveStatusEnqFromIf = _FrNniLmiKeepAliveStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 3),
    _FrNniLmiKeepAliveStatusEnqFromIf_Type()
)
frNniLmiKeepAliveStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiKeepAliveStatusEnqFromIf.setStatus("mandatory")
_FrNniLmiFullStatusEnqFromIf_Type = Counter32
_FrNniLmiFullStatusEnqFromIf_Object = MibTableColumn
frNniLmiFullStatusEnqFromIf = _FrNniLmiFullStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 4),
    _FrNniLmiFullStatusEnqFromIf_Type()
)
frNniLmiFullStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiFullStatusEnqFromIf.setStatus("mandatory")


class _FrNniLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type frNniLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrNniLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_FrNniLmiNetworkSideEventHistory_Object = MibTableColumn
frNniLmiNetworkSideEventHistory = _FrNniLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 5),
    _FrNniLmiNetworkSideEventHistory_Type()
)
frNniLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiNetworkSideEventHistory.setStatus("mandatory")


class _FrNniLmiUserSideEventHistory_Type(AsciiString):
    """Custom type frNniLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_FrNniLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_FrNniLmiUserSideEventHistory_Object = MibTableColumn
frNniLmiUserSideEventHistory = _FrNniLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 6),
    _FrNniLmiUserSideEventHistory_Type()
)
frNniLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiUserSideEventHistory.setStatus("mandatory")
_FrNniLmiProtocolErrors_Type = Counter32
_FrNniLmiProtocolErrors_Object = MibTableColumn
frNniLmiProtocolErrors = _FrNniLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 7),
    _FrNniLmiProtocolErrors_Type()
)
frNniLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiProtocolErrors.setStatus("mandatory")
_FrNniLmiUnexpectedIes_Type = Counter32
_FrNniLmiUnexpectedIes_Object = MibTableColumn
frNniLmiUnexpectedIes = _FrNniLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 8),
    _FrNniLmiUnexpectedIes_Type()
)
frNniLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiUnexpectedIes.setStatus("mandatory")
_FrNniLmiSequenceErrors_Type = Counter32
_FrNniLmiSequenceErrors_Object = MibTableColumn
frNniLmiSequenceErrors = _FrNniLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 9),
    _FrNniLmiSequenceErrors_Type()
)
frNniLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiSequenceErrors.setStatus("mandatory")
_FrNniLmiStatusSequenceErrors_Type = Counter32
_FrNniLmiStatusSequenceErrors_Object = MibTableColumn
frNniLmiStatusSequenceErrors = _FrNniLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 10),
    _FrNniLmiStatusSequenceErrors_Type()
)
frNniLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiStatusSequenceErrors.setStatus("mandatory")
_FrNniLmiUnexpectedReports_Type = Counter32
_FrNniLmiUnexpectedReports_Object = MibTableColumn
frNniLmiUnexpectedReports = _FrNniLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 11),
    _FrNniLmiUnexpectedReports_Type()
)
frNniLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiUnexpectedReports.setStatus("mandatory")
_FrNniLmiPollingVerifTimeouts_Type = Counter32
_FrNniLmiPollingVerifTimeouts_Object = MibTableColumn
frNniLmiPollingVerifTimeouts = _FrNniLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 12),
    _FrNniLmiPollingVerifTimeouts_Type()
)
frNniLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiPollingVerifTimeouts.setStatus("mandatory")
_FrNniLmiNoStatusReportCount_Type = Counter32
_FrNniLmiNoStatusReportCount_Object = MibTableColumn
frNniLmiNoStatusReportCount = _FrNniLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 4, 14, 1, 13),
    _FrNniLmiNoStatusReportCount_Type()
)
frNniLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLmiNoStatusReportCount.setStatus("mandatory")
_FrNniDlci_ObjectIdentity = ObjectIdentity
frNniDlci = _FrNniDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5)
)
_FrNniDlciRowStatusTable_Object = MibTable
frNniDlciRowStatusTable = _FrNniDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 1)
)
if mibBuilder.loadTexts:
    frNniDlciRowStatusTable.setStatus("mandatory")
_FrNniDlciRowStatusEntry_Object = MibTableRow
frNniDlciRowStatusEntry = _FrNniDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 1, 1)
)
frNniDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciRowStatusEntry.setStatus("mandatory")
_FrNniDlciRowStatus_Type = RowStatus
_FrNniDlciRowStatus_Object = MibTableColumn
frNniDlciRowStatus = _FrNniDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 1, 1, 1),
    _FrNniDlciRowStatus_Type()
)
frNniDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciRowStatus.setStatus("mandatory")
_FrNniDlciComponentName_Type = DisplayString
_FrNniDlciComponentName_Object = MibTableColumn
frNniDlciComponentName = _FrNniDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 1, 1, 2),
    _FrNniDlciComponentName_Type()
)
frNniDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciComponentName.setStatus("mandatory")
_FrNniDlciStorageType_Type = StorageType
_FrNniDlciStorageType_Object = MibTableColumn
frNniDlciStorageType = _FrNniDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 1, 1, 4),
    _FrNniDlciStorageType_Type()
)
frNniDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciStorageType.setStatus("mandatory")


class _FrNniDlciIndex_Type(Integer32):
    """Custom type frNniDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrNniDlciIndex_Type.__name__ = "Integer32"
_FrNniDlciIndex_Object = MibTableColumn
frNniDlciIndex = _FrNniDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 1, 1, 10),
    _FrNniDlciIndex_Type()
)
frNniDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDlciIndex.setStatus("mandatory")
_FrNniDlciDc_ObjectIdentity = ObjectIdentity
frNniDlciDc = _FrNniDlciDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2)
)
_FrNniDlciDcRowStatusTable_Object = MibTable
frNniDlciDcRowStatusTable = _FrNniDlciDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 1)
)
if mibBuilder.loadTexts:
    frNniDlciDcRowStatusTable.setStatus("mandatory")
_FrNniDlciDcRowStatusEntry_Object = MibTableRow
frNniDlciDcRowStatusEntry = _FrNniDlciDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 1, 1)
)
frNniDlciDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciDcRowStatusEntry.setStatus("mandatory")
_FrNniDlciDcRowStatus_Type = RowStatus
_FrNniDlciDcRowStatus_Object = MibTableColumn
frNniDlciDcRowStatus = _FrNniDlciDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 1, 1, 1),
    _FrNniDlciDcRowStatus_Type()
)
frNniDlciDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDcRowStatus.setStatus("mandatory")
_FrNniDlciDcComponentName_Type = DisplayString
_FrNniDlciDcComponentName_Object = MibTableColumn
frNniDlciDcComponentName = _FrNniDlciDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 1, 1, 2),
    _FrNniDlciDcComponentName_Type()
)
frNniDlciDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDcComponentName.setStatus("mandatory")
_FrNniDlciDcStorageType_Type = StorageType
_FrNniDlciDcStorageType_Object = MibTableColumn
frNniDlciDcStorageType = _FrNniDlciDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 1, 1, 4),
    _FrNniDlciDcStorageType_Type()
)
frNniDlciDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDcStorageType.setStatus("mandatory")
_FrNniDlciDcIndex_Type = NonReplicated
_FrNniDlciDcIndex_Object = MibTableColumn
frNniDlciDcIndex = _FrNniDlciDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 1, 1, 10),
    _FrNniDlciDcIndex_Type()
)
frNniDlciDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDlciDcIndex.setStatus("mandatory")
_FrNniDlciDcOptionsTable_Object = MibTable
frNniDlciDcOptionsTable = _FrNniDlciDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10)
)
if mibBuilder.loadTexts:
    frNniDlciDcOptionsTable.setStatus("mandatory")
_FrNniDlciDcOptionsEntry_Object = MibTableRow
frNniDlciDcOptionsEntry = _FrNniDlciDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1)
)
frNniDlciDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciDcOptionsEntry.setStatus("mandatory")


class _FrNniDlciDcRemoteNpi_Type(Integer32):
    """Custom type frNniDlciDcRemoteNpi based on Integer32"""
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


_FrNniDlciDcRemoteNpi_Type.__name__ = "Integer32"
_FrNniDlciDcRemoteNpi_Object = MibTableColumn
frNniDlciDcRemoteNpi = _FrNniDlciDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 3),
    _FrNniDlciDcRemoteNpi_Type()
)
frNniDlciDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcRemoteNpi.setStatus("mandatory")


class _FrNniDlciDcRemoteDna_Type(DigitString):
    """Custom type frNniDlciDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrNniDlciDcRemoteDna_Type.__name__ = "DigitString"
_FrNniDlciDcRemoteDna_Object = MibTableColumn
frNniDlciDcRemoteDna = _FrNniDlciDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 4),
    _FrNniDlciDcRemoteDna_Type()
)
frNniDlciDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcRemoteDna.setStatus("mandatory")


class _FrNniDlciDcRemoteDlci_Type(Unsigned32):
    """Custom type frNniDlciDcRemoteDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrNniDlciDcRemoteDlci_Type.__name__ = "Unsigned32"
_FrNniDlciDcRemoteDlci_Object = MibTableColumn
frNniDlciDcRemoteDlci = _FrNniDlciDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 5),
    _FrNniDlciDcRemoteDlci_Type()
)
frNniDlciDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcRemoteDlci.setStatus("mandatory")


class _FrNniDlciDcType_Type(Integer32):
    """Custom type frNniDlciDcType based on Integer32"""
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


_FrNniDlciDcType_Type.__name__ = "Integer32"
_FrNniDlciDcType_Object = MibTableColumn
frNniDlciDcType = _FrNniDlciDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 6),
    _FrNniDlciDcType_Type()
)
frNniDlciDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcType.setStatus("mandatory")


class _FrNniDlciDcTransferPriority_Type(Integer32):
    """Custom type frNniDlciDcTransferPriority based on Integer32"""
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


_FrNniDlciDcTransferPriority_Type.__name__ = "Integer32"
_FrNniDlciDcTransferPriority_Object = MibTableColumn
frNniDlciDcTransferPriority = _FrNniDlciDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 9),
    _FrNniDlciDcTransferPriority_Type()
)
frNniDlciDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcTransferPriority.setStatus("mandatory")


class _FrNniDlciDcDiscardPriority_Type(Integer32):
    """Custom type frNniDlciDcDiscardPriority based on Integer32"""
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


_FrNniDlciDcDiscardPriority_Type.__name__ = "Integer32"
_FrNniDlciDcDiscardPriority_Object = MibTableColumn
frNniDlciDcDiscardPriority = _FrNniDlciDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 10),
    _FrNniDlciDcDiscardPriority_Type()
)
frNniDlciDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcDiscardPriority.setStatus("mandatory")


class _FrNniDlciDcDeDiscardPriority_Type(Integer32):
    """Custom type frNniDlciDcDeDiscardPriority based on Integer32"""
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


_FrNniDlciDcDeDiscardPriority_Type.__name__ = "Integer32"
_FrNniDlciDcDeDiscardPriority_Object = MibTableColumn
frNniDlciDcDeDiscardPriority = _FrNniDlciDcDeDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 11),
    _FrNniDlciDcDeDiscardPriority_Type()
)
frNniDlciDcDeDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcDeDiscardPriority.setStatus("mandatory")


class _FrNniDlciDcDataPath_Type(Integer32):
    """Custom type frNniDlciDcDataPath based on Integer32"""
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


_FrNniDlciDcDataPath_Type.__name__ = "Integer32"
_FrNniDlciDcDataPath_Object = MibTableColumn
frNniDlciDcDataPath = _FrNniDlciDcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 12),
    _FrNniDlciDcDataPath_Type()
)
frNniDlciDcDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcDataPath.setStatus("mandatory")


class _FrNniDlciDcCugIndex_Type(Unsigned32):
    """Custom type frNniDlciDcCugIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrNniDlciDcCugIndex_Type.__name__ = "Unsigned32"
_FrNniDlciDcCugIndex_Object = MibTableColumn
frNniDlciDcCugIndex = _FrNniDlciDcCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 13),
    _FrNniDlciDcCugIndex_Type()
)
frNniDlciDcCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcCugIndex.setStatus("mandatory")


class _FrNniDlciDcCugType_Type(Integer32):
    """Custom type frNniDlciDcCugType based on Integer32"""
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


_FrNniDlciDcCugType_Type.__name__ = "Integer32"
_FrNniDlciDcCugType_Object = MibTableColumn
frNniDlciDcCugType = _FrNniDlciDcCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 10, 1, 14),
    _FrNniDlciDcCugType_Type()
)
frNniDlciDcCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcCugType.setStatus("mandatory")
_FrNniDlciDcNfaTable_Object = MibTable
frNniDlciDcNfaTable = _FrNniDlciDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 202)
)
if mibBuilder.loadTexts:
    frNniDlciDcNfaTable.setStatus("obsolete")
_FrNniDlciDcNfaEntry_Object = MibTableRow
frNniDlciDcNfaEntry = _FrNniDlciDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 202, 1)
)
frNniDlciDcNfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciDcIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciDcNfaIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciDcNfaEntry.setStatus("obsolete")


class _FrNniDlciDcNfaIndex_Type(Integer32):
    """Custom type frNniDlciDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
    )


_FrNniDlciDcNfaIndex_Type.__name__ = "Integer32"
_FrNniDlciDcNfaIndex_Object = MibTableColumn
frNniDlciDcNfaIndex = _FrNniDlciDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 202, 1, 1),
    _FrNniDlciDcNfaIndex_Type()
)
frNniDlciDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDlciDcNfaIndex.setStatus("obsolete")


class _FrNniDlciDcNfaValue_Type(HexString):
    """Custom type frNniDlciDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FrNniDlciDcNfaValue_Type.__name__ = "HexString"
_FrNniDlciDcNfaValue_Object = MibTableColumn
frNniDlciDcNfaValue = _FrNniDlciDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 202, 1, 2),
    _FrNniDlciDcNfaValue_Type()
)
frNniDlciDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciDcNfaValue.setStatus("obsolete")
_FrNniDlciDcNfaRowStatus_Type = RowStatus
_FrNniDlciDcNfaRowStatus_Object = MibTableColumn
frNniDlciDcNfaRowStatus = _FrNniDlciDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 2, 202, 1, 3),
    _FrNniDlciDcNfaRowStatus_Type()
)
frNniDlciDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frNniDlciDcNfaRowStatus.setStatus("obsolete")
_FrNniDlciVc_ObjectIdentity = ObjectIdentity
frNniDlciVc = _FrNniDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3)
)
_FrNniDlciVcRowStatusTable_Object = MibTable
frNniDlciVcRowStatusTable = _FrNniDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 1)
)
if mibBuilder.loadTexts:
    frNniDlciVcRowStatusTable.setStatus("mandatory")
_FrNniDlciVcRowStatusEntry_Object = MibTableRow
frNniDlciVcRowStatusEntry = _FrNniDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 1, 1)
)
frNniDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciVcRowStatusEntry.setStatus("mandatory")
_FrNniDlciVcRowStatus_Type = RowStatus
_FrNniDlciVcRowStatus_Object = MibTableColumn
frNniDlciVcRowStatus = _FrNniDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 1, 1, 1),
    _FrNniDlciVcRowStatus_Type()
)
frNniDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcRowStatus.setStatus("mandatory")
_FrNniDlciVcComponentName_Type = DisplayString
_FrNniDlciVcComponentName_Object = MibTableColumn
frNniDlciVcComponentName = _FrNniDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 1, 1, 2),
    _FrNniDlciVcComponentName_Type()
)
frNniDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcComponentName.setStatus("mandatory")
_FrNniDlciVcStorageType_Type = StorageType
_FrNniDlciVcStorageType_Object = MibTableColumn
frNniDlciVcStorageType = _FrNniDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 1, 1, 4),
    _FrNniDlciVcStorageType_Type()
)
frNniDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcStorageType.setStatus("mandatory")
_FrNniDlciVcIndex_Type = NonReplicated
_FrNniDlciVcIndex_Object = MibTableColumn
frNniDlciVcIndex = _FrNniDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 1, 1, 10),
    _FrNniDlciVcIndex_Type()
)
frNniDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDlciVcIndex.setStatus("mandatory")
_FrNniDlciVcCadTable_Object = MibTable
frNniDlciVcCadTable = _FrNniDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10)
)
if mibBuilder.loadTexts:
    frNniDlciVcCadTable.setStatus("mandatory")
_FrNniDlciVcCadEntry_Object = MibTableRow
frNniDlciVcCadEntry = _FrNniDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1)
)
frNniDlciVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciVcCadEntry.setStatus("mandatory")


class _FrNniDlciVcType_Type(Integer32):
    """Custom type frNniDlciVcType based on Integer32"""
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


_FrNniDlciVcType_Type.__name__ = "Integer32"
_FrNniDlciVcType_Object = MibTableColumn
frNniDlciVcType = _FrNniDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 1),
    _FrNniDlciVcType_Type()
)
frNniDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcType.setStatus("mandatory")


class _FrNniDlciVcState_Type(Integer32):
    """Custom type frNniDlciVcState based on Integer32"""
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


_FrNniDlciVcState_Type.__name__ = "Integer32"
_FrNniDlciVcState_Object = MibTableColumn
frNniDlciVcState = _FrNniDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 2),
    _FrNniDlciVcState_Type()
)
frNniDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcState.setStatus("mandatory")


class _FrNniDlciVcPreviousState_Type(Integer32):
    """Custom type frNniDlciVcPreviousState based on Integer32"""
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


_FrNniDlciVcPreviousState_Type.__name__ = "Integer32"
_FrNniDlciVcPreviousState_Object = MibTableColumn
frNniDlciVcPreviousState = _FrNniDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 3),
    _FrNniDlciVcPreviousState_Type()
)
frNniDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPreviousState.setStatus("mandatory")


class _FrNniDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type frNniDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrNniDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_FrNniDlciVcDiagnosticCode_Object = MibTableColumn
frNniDlciVcDiagnosticCode = _FrNniDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 4),
    _FrNniDlciVcDiagnosticCode_Type()
)
frNniDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcDiagnosticCode.setStatus("mandatory")


class _FrNniDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type frNniDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrNniDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_FrNniDlciVcPreviousDiagnosticCode_Object = MibTableColumn
frNniDlciVcPreviousDiagnosticCode = _FrNniDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 5),
    _FrNniDlciVcPreviousDiagnosticCode_Type()
)
frNniDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _FrNniDlciVcCalledNpi_Type(Integer32):
    """Custom type frNniDlciVcCalledNpi based on Integer32"""
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


_FrNniDlciVcCalledNpi_Type.__name__ = "Integer32"
_FrNniDlciVcCalledNpi_Object = MibTableColumn
frNniDlciVcCalledNpi = _FrNniDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 6),
    _FrNniDlciVcCalledNpi_Type()
)
frNniDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCalledNpi.setStatus("mandatory")


class _FrNniDlciVcCalledDna_Type(DigitString):
    """Custom type frNniDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrNniDlciVcCalledDna_Type.__name__ = "DigitString"
_FrNniDlciVcCalledDna_Object = MibTableColumn
frNniDlciVcCalledDna = _FrNniDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 7),
    _FrNniDlciVcCalledDna_Type()
)
frNniDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCalledDna.setStatus("mandatory")


class _FrNniDlciVcCalledLcn_Type(Unsigned32):
    """Custom type frNniDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrNniDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_FrNniDlciVcCalledLcn_Object = MibTableColumn
frNniDlciVcCalledLcn = _FrNniDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 8),
    _FrNniDlciVcCalledLcn_Type()
)
frNniDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCalledLcn.setStatus("mandatory")


class _FrNniDlciVcCallingNpi_Type(Integer32):
    """Custom type frNniDlciVcCallingNpi based on Integer32"""
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


_FrNniDlciVcCallingNpi_Type.__name__ = "Integer32"
_FrNniDlciVcCallingNpi_Object = MibTableColumn
frNniDlciVcCallingNpi = _FrNniDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 9),
    _FrNniDlciVcCallingNpi_Type()
)
frNniDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCallingNpi.setStatus("mandatory")


class _FrNniDlciVcCallingDna_Type(DigitString):
    """Custom type frNniDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_FrNniDlciVcCallingDna_Type.__name__ = "DigitString"
_FrNniDlciVcCallingDna_Object = MibTableColumn
frNniDlciVcCallingDna = _FrNniDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 10),
    _FrNniDlciVcCallingDna_Type()
)
frNniDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCallingDna.setStatus("mandatory")


class _FrNniDlciVcCallingLcn_Type(Unsigned32):
    """Custom type frNniDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrNniDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_FrNniDlciVcCallingLcn_Object = MibTableColumn
frNniDlciVcCallingLcn = _FrNniDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 11),
    _FrNniDlciVcCallingLcn_Type()
)
frNniDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCallingLcn.setStatus("mandatory")


class _FrNniDlciVcAccountingEnabled_Type(Integer32):
    """Custom type frNniDlciVcAccountingEnabled based on Integer32"""
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


_FrNniDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_FrNniDlciVcAccountingEnabled_Object = MibTableColumn
frNniDlciVcAccountingEnabled = _FrNniDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 12),
    _FrNniDlciVcAccountingEnabled_Type()
)
frNniDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcAccountingEnabled.setStatus("mandatory")


class _FrNniDlciVcFastSelectCall_Type(Integer32):
    """Custom type frNniDlciVcFastSelectCall based on Integer32"""
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


_FrNniDlciVcFastSelectCall_Type.__name__ = "Integer32"
_FrNniDlciVcFastSelectCall_Object = MibTableColumn
frNniDlciVcFastSelectCall = _FrNniDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 13),
    _FrNniDlciVcFastSelectCall_Type()
)
frNniDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcFastSelectCall.setStatus("mandatory")


class _FrNniDlciVcPathReliability_Type(Integer32):
    """Custom type frNniDlciVcPathReliability based on Integer32"""
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


_FrNniDlciVcPathReliability_Type.__name__ = "Integer32"
_FrNniDlciVcPathReliability_Object = MibTableColumn
frNniDlciVcPathReliability = _FrNniDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 19),
    _FrNniDlciVcPathReliability_Type()
)
frNniDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPathReliability.setStatus("mandatory")


class _FrNniDlciVcAccountingEnd_Type(Integer32):
    """Custom type frNniDlciVcAccountingEnd based on Integer32"""
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


_FrNniDlciVcAccountingEnd_Type.__name__ = "Integer32"
_FrNniDlciVcAccountingEnd_Object = MibTableColumn
frNniDlciVcAccountingEnd = _FrNniDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 20),
    _FrNniDlciVcAccountingEnd_Type()
)
frNniDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcAccountingEnd.setStatus("mandatory")


class _FrNniDlciVcPriority_Type(Integer32):
    """Custom type frNniDlciVcPriority based on Integer32"""
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


_FrNniDlciVcPriority_Type.__name__ = "Integer32"
_FrNniDlciVcPriority_Object = MibTableColumn
frNniDlciVcPriority = _FrNniDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 21),
    _FrNniDlciVcPriority_Type()
)
frNniDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPriority.setStatus("mandatory")


class _FrNniDlciVcSegmentSize_Type(Unsigned32):
    """Custom type frNniDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FrNniDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_FrNniDlciVcSegmentSize_Object = MibTableColumn
frNniDlciVcSegmentSize = _FrNniDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 22),
    _FrNniDlciVcSegmentSize_Type()
)
frNniDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcSegmentSize.setStatus("mandatory")


class _FrNniDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type frNniDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_FrNniDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_FrNniDlciVcMaxSubnetPktSize_Object = MibTableColumn
frNniDlciVcMaxSubnetPktSize = _FrNniDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 27),
    _FrNniDlciVcMaxSubnetPktSize_Type()
)
frNniDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _FrNniDlciVcRcosToNetwork_Type(Integer32):
    """Custom type frNniDlciVcRcosToNetwork based on Integer32"""
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


_FrNniDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_FrNniDlciVcRcosToNetwork_Object = MibTableColumn
frNniDlciVcRcosToNetwork = _FrNniDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 28),
    _FrNniDlciVcRcosToNetwork_Type()
)
frNniDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcRcosToNetwork.setStatus("mandatory")


class _FrNniDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type frNniDlciVcRcosFromNetwork based on Integer32"""
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


_FrNniDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_FrNniDlciVcRcosFromNetwork_Object = MibTableColumn
frNniDlciVcRcosFromNetwork = _FrNniDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 29),
    _FrNniDlciVcRcosFromNetwork_Type()
)
frNniDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcRcosFromNetwork.setStatus("mandatory")


class _FrNniDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type frNniDlciVcEmissionPriorityToNetwork based on Integer32"""
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


_FrNniDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_FrNniDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
frNniDlciVcEmissionPriorityToNetwork = _FrNniDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 30),
    _FrNniDlciVcEmissionPriorityToNetwork_Type()
)
frNniDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _FrNniDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type frNniDlciVcEmissionPriorityFromNetwork based on Integer32"""
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


_FrNniDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_FrNniDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
frNniDlciVcEmissionPriorityFromNetwork = _FrNniDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 31),
    _FrNniDlciVcEmissionPriorityFromNetwork_Type()
)
frNniDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _FrNniDlciVcDataPath_Type(AsciiString):
    """Custom type frNniDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FrNniDlciVcDataPath_Type.__name__ = "AsciiString"
_FrNniDlciVcDataPath_Object = MibTableColumn
frNniDlciVcDataPath = _FrNniDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 10, 1, 32),
    _FrNniDlciVcDataPath_Type()
)
frNniDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcDataPath.setStatus("mandatory")
_FrNniDlciVcIntdTable_Object = MibTable
frNniDlciVcIntdTable = _FrNniDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 11)
)
if mibBuilder.loadTexts:
    frNniDlciVcIntdTable.setStatus("mandatory")
_FrNniDlciVcIntdEntry_Object = MibTableRow
frNniDlciVcIntdEntry = _FrNniDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 11, 1)
)
frNniDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciVcIntdEntry.setStatus("mandatory")


class _FrNniDlciVcCallReferenceNumber_Type(Hex):
    """Custom type frNniDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrNniDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_FrNniDlciVcCallReferenceNumber_Object = MibTableColumn
frNniDlciVcCallReferenceNumber = _FrNniDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 11, 1, 1),
    _FrNniDlciVcCallReferenceNumber_Type()
)
frNniDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCallReferenceNumber.setStatus("mandatory")


class _FrNniDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type frNniDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrNniDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_FrNniDlciVcElapsedTimeTillNow_Object = MibTableColumn
frNniDlciVcElapsedTimeTillNow = _FrNniDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 11, 1, 2),
    _FrNniDlciVcElapsedTimeTillNow_Type()
)
frNniDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _FrNniDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type frNniDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrNniDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_FrNniDlciVcSegmentsRx_Object = MibTableColumn
frNniDlciVcSegmentsRx = _FrNniDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 11, 1, 3),
    _FrNniDlciVcSegmentsRx_Type()
)
frNniDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcSegmentsRx.setStatus("mandatory")


class _FrNniDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type frNniDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrNniDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_FrNniDlciVcSegmentsSent_Object = MibTableColumn
frNniDlciVcSegmentsSent = _FrNniDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 11, 1, 4),
    _FrNniDlciVcSegmentsSent_Type()
)
frNniDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcSegmentsSent.setStatus("mandatory")


class _FrNniDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type frNniDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrNniDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_FrNniDlciVcStartTime_Object = MibTableColumn
frNniDlciVcStartTime = _FrNniDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 11, 1, 5),
    _FrNniDlciVcStartTime_Type()
)
frNniDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcStartTime.setStatus("mandatory")
_FrNniDlciVcFrdTable_Object = MibTable
frNniDlciVcFrdTable = _FrNniDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12)
)
if mibBuilder.loadTexts:
    frNniDlciVcFrdTable.setStatus("mandatory")
_FrNniDlciVcFrdEntry_Object = MibTableRow
frNniDlciVcFrdEntry = _FrNniDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1)
)
frNniDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciVcFrdEntry.setStatus("mandatory")


class _FrNniDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type frNniDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciVcFrmCongestedToSubnet_Object = MibTableColumn
frNniDlciVcFrmCongestedToSubnet = _FrNniDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 2),
    _FrNniDlciVcFrmCongestedToSubnet_Type()
)
frNniDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _FrNniDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type frNniDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciVcCannotForwardToSubnet_Object = MibTableColumn
frNniDlciVcCannotForwardToSubnet = _FrNniDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 3),
    _FrNniDlciVcCannotForwardToSubnet_Type()
)
frNniDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _FrNniDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type frNniDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciVcNotDataXferToSubnet_Object = MibTableColumn
frNniDlciVcNotDataXferToSubnet = _FrNniDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 4),
    _FrNniDlciVcNotDataXferToSubnet_Type()
)
frNniDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _FrNniDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type frNniDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
frNniDlciVcOutOfRangeFrmFromSubnet = _FrNniDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 5),
    _FrNniDlciVcOutOfRangeFrmFromSubnet_Type()
)
frNniDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _FrNniDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type frNniDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciVcCombErrorsFromSubnet_Object = MibTableColumn
frNniDlciVcCombErrorsFromSubnet = _FrNniDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 6),
    _FrNniDlciVcCombErrorsFromSubnet_Type()
)
frNniDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _FrNniDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type frNniDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciVcDuplicatesFromSubnet_Object = MibTableColumn
frNniDlciVcDuplicatesFromSubnet = _FrNniDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 7),
    _FrNniDlciVcDuplicatesFromSubnet_Type()
)
frNniDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _FrNniDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type frNniDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciVcNotDataXferFromSubnet_Object = MibTableColumn
frNniDlciVcNotDataXferFromSubnet = _FrNniDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 8),
    _FrNniDlciVcNotDataXferFromSubnet_Type()
)
frNniDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _FrNniDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type frNniDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_FrNniDlciVcFrmLossTimeouts_Object = MibTableColumn
frNniDlciVcFrmLossTimeouts = _FrNniDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 9),
    _FrNniDlciVcFrmLossTimeouts_Type()
)
frNniDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcFrmLossTimeouts.setStatus("mandatory")


class _FrNniDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type frNniDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_FrNniDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
frNniDlciVcOoSeqByteCntExceeded = _FrNniDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 10),
    _FrNniDlciVcOoSeqByteCntExceeded_Type()
)
frNniDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _FrNniDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type frNniDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_FrNniDlciVcPeakOoSeqPktCount_Object = MibTableColumn
frNniDlciVcPeakOoSeqPktCount = _FrNniDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 11),
    _FrNniDlciVcPeakOoSeqPktCount_Type()
)
frNniDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _FrNniDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type frNniDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_FrNniDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
frNniDlciVcPeakOoSeqFrmForwarded = _FrNniDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 12),
    _FrNniDlciVcPeakOoSeqFrmForwarded_Type()
)
frNniDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _FrNniDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type frNniDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_FrNniDlciVcSendSequenceNumber_Object = MibTableColumn
frNniDlciVcSendSequenceNumber = _FrNniDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 13),
    _FrNniDlciVcSendSequenceNumber_Type()
)
frNniDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcSendSequenceNumber.setStatus("mandatory")


class _FrNniDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type frNniDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_FrNniDlciVcPktRetryTimeouts_Object = MibTableColumn
frNniDlciVcPktRetryTimeouts = _FrNniDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 15),
    _FrNniDlciVcPktRetryTimeouts_Type()
)
frNniDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPktRetryTimeouts.setStatus("mandatory")


class _FrNniDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type frNniDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_FrNniDlciVcPeakRetryQueueSize_Object = MibTableColumn
frNniDlciVcPeakRetryQueueSize = _FrNniDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 16),
    _FrNniDlciVcPeakRetryQueueSize_Type()
)
frNniDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _FrNniDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type frNniDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FrNniDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_FrNniDlciVcSubnetRecoveries_Object = MibTableColumn
frNniDlciVcSubnetRecoveries = _FrNniDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 17),
    _FrNniDlciVcSubnetRecoveries_Type()
)
frNniDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcSubnetRecoveries.setStatus("mandatory")


class _FrNniDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type frNniDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrNniDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_FrNniDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
frNniDlciVcOoSeqPktCntExceeded = _FrNniDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 19),
    _FrNniDlciVcOoSeqPktCntExceeded_Type()
)
frNniDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _FrNniDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type frNniDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_FrNniDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_FrNniDlciVcPeakOoSeqByteCount_Object = MibTableColumn
frNniDlciVcPeakOoSeqByteCount = _FrNniDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 12, 1, 20),
    _FrNniDlciVcPeakOoSeqByteCount_Type()
)
frNniDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_FrNniDlciVcDmepTable_Object = MibTable
frNniDlciVcDmepTable = _FrNniDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 417)
)
if mibBuilder.loadTexts:
    frNniDlciVcDmepTable.setStatus("mandatory")
_FrNniDlciVcDmepEntry_Object = MibTableRow
frNniDlciVcDmepEntry = _FrNniDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 417, 1)
)
frNniDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciVcIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    frNniDlciVcDmepEntry.setStatus("mandatory")
_FrNniDlciVcDmepValue_Type = RowPointer
_FrNniDlciVcDmepValue_Object = MibTableColumn
frNniDlciVcDmepValue = _FrNniDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 3, 417, 1, 1),
    _FrNniDlciVcDmepValue_Type()
)
frNniDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciVcDmepValue.setStatus("mandatory")
_FrNniDlciSp_ObjectIdentity = ObjectIdentity
frNniDlciSp = _FrNniDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4)
)
_FrNniDlciSpRowStatusTable_Object = MibTable
frNniDlciSpRowStatusTable = _FrNniDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 1)
)
if mibBuilder.loadTexts:
    frNniDlciSpRowStatusTable.setStatus("mandatory")
_FrNniDlciSpRowStatusEntry_Object = MibTableRow
frNniDlciSpRowStatusEntry = _FrNniDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 1, 1)
)
frNniDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciSpRowStatusEntry.setStatus("mandatory")
_FrNniDlciSpRowStatus_Type = RowStatus
_FrNniDlciSpRowStatus_Object = MibTableColumn
frNniDlciSpRowStatus = _FrNniDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 1, 1, 1),
    _FrNniDlciSpRowStatus_Type()
)
frNniDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciSpRowStatus.setStatus("mandatory")
_FrNniDlciSpComponentName_Type = DisplayString
_FrNniDlciSpComponentName_Object = MibTableColumn
frNniDlciSpComponentName = _FrNniDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 1, 1, 2),
    _FrNniDlciSpComponentName_Type()
)
frNniDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciSpComponentName.setStatus("mandatory")
_FrNniDlciSpStorageType_Type = StorageType
_FrNniDlciSpStorageType_Object = MibTableColumn
frNniDlciSpStorageType = _FrNniDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 1, 1, 4),
    _FrNniDlciSpStorageType_Type()
)
frNniDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciSpStorageType.setStatus("mandatory")
_FrNniDlciSpIndex_Type = NonReplicated
_FrNniDlciSpIndex_Object = MibTableColumn
frNniDlciSpIndex = _FrNniDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 1, 1, 10),
    _FrNniDlciSpIndex_Type()
)
frNniDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDlciSpIndex.setStatus("mandatory")
_FrNniDlciSpParmsTable_Object = MibTable
frNniDlciSpParmsTable = _FrNniDlciSpParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11)
)
if mibBuilder.loadTexts:
    frNniDlciSpParmsTable.setStatus("mandatory")
_FrNniDlciSpParmsEntry_Object = MibTableRow
frNniDlciSpParmsEntry = _FrNniDlciSpParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1)
)
frNniDlciSpParmsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciSpParmsEntry.setStatus("mandatory")


class _FrNniDlciSpMaximumFrameSize_Type(Unsigned32):
    """Custom type frNniDlciSpMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrNniDlciSpMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrNniDlciSpMaximumFrameSize_Object = MibTableColumn
frNniDlciSpMaximumFrameSize = _FrNniDlciSpMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 1),
    _FrNniDlciSpMaximumFrameSize_Type()
)
frNniDlciSpMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpMaximumFrameSize.setStatus("mandatory")


class _FrNniDlciSpRateEnforcement_Type(Integer32):
    """Custom type frNniDlciSpRateEnforcement based on Integer32"""
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


_FrNniDlciSpRateEnforcement_Type.__name__ = "Integer32"
_FrNniDlciSpRateEnforcement_Object = MibTableColumn
frNniDlciSpRateEnforcement = _FrNniDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 2),
    _FrNniDlciSpRateEnforcement_Type()
)
frNniDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpRateEnforcement.setStatus("mandatory")


class _FrNniDlciSpCommittedInformationRate_Type(Gauge32):
    """Custom type frNniDlciSpCommittedInformationRate based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrNniDlciSpCommittedInformationRate_Type.__name__ = "Gauge32"
_FrNniDlciSpCommittedInformationRate_Object = MibTableColumn
frNniDlciSpCommittedInformationRate = _FrNniDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 3),
    _FrNniDlciSpCommittedInformationRate_Type()
)
frNniDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpCommittedInformationRate.setStatus("mandatory")


class _FrNniDlciSpCommittedBurstSize_Type(Gauge32):
    """Custom type frNniDlciSpCommittedBurstSize based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrNniDlciSpCommittedBurstSize_Type.__name__ = "Gauge32"
_FrNniDlciSpCommittedBurstSize_Object = MibTableColumn
frNniDlciSpCommittedBurstSize = _FrNniDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 4),
    _FrNniDlciSpCommittedBurstSize_Type()
)
frNniDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpCommittedBurstSize.setStatus("mandatory")


class _FrNniDlciSpExcessBurstSize_Type(Gauge32):
    """Custom type frNniDlciSpExcessBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_FrNniDlciSpExcessBurstSize_Type.__name__ = "Gauge32"
_FrNniDlciSpExcessBurstSize_Object = MibTableColumn
frNniDlciSpExcessBurstSize = _FrNniDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 5),
    _FrNniDlciSpExcessBurstSize_Type()
)
frNniDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpExcessBurstSize.setStatus("mandatory")


class _FrNniDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type frNniDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_FrNniDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_FrNniDlciSpMeasurementInterval_Object = MibTableColumn
frNniDlciSpMeasurementInterval = _FrNniDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 6),
    _FrNniDlciSpMeasurementInterval_Type()
)
frNniDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpMeasurementInterval.setStatus("mandatory")


class _FrNniDlciSpRateAdaptation_Type(Integer32):
    """Custom type frNniDlciSpRateAdaptation based on Integer32"""
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


_FrNniDlciSpRateAdaptation_Type.__name__ = "Integer32"
_FrNniDlciSpRateAdaptation_Object = MibTableColumn
frNniDlciSpRateAdaptation = _FrNniDlciSpRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 7),
    _FrNniDlciSpRateAdaptation_Type()
)
frNniDlciSpRateAdaptation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpRateAdaptation.setStatus("mandatory")


class _FrNniDlciSpAccounting_Type(Integer32):
    """Custom type frNniDlciSpAccounting based on Integer32"""
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


_FrNniDlciSpAccounting_Type.__name__ = "Integer32"
_FrNniDlciSpAccounting_Object = MibTableColumn
frNniDlciSpAccounting = _FrNniDlciSpAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 8),
    _FrNniDlciSpAccounting_Type()
)
frNniDlciSpAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpAccounting.setStatus("mandatory")


class _FrNniDlciSpRaSensitivity_Type(Unsigned32):
    """Custom type frNniDlciSpRaSensitivity based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FrNniDlciSpRaSensitivity_Type.__name__ = "Unsigned32"
_FrNniDlciSpRaSensitivity_Object = MibTableColumn
frNniDlciSpRaSensitivity = _FrNniDlciSpRaSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 9),
    _FrNniDlciSpRaSensitivity_Type()
)
frNniDlciSpRaSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpRaSensitivity.setStatus("mandatory")


class _FrNniDlciSpUpdateBCI_Type(Integer32):
    """Custom type frNniDlciSpUpdateBCI based on Integer32"""
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


_FrNniDlciSpUpdateBCI_Type.__name__ = "Integer32"
_FrNniDlciSpUpdateBCI_Object = MibTableColumn
frNniDlciSpUpdateBCI = _FrNniDlciSpUpdateBCI_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 4, 11, 1, 10),
    _FrNniDlciSpUpdateBCI_Type()
)
frNniDlciSpUpdateBCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniDlciSpUpdateBCI.setStatus("mandatory")
_FrNniDlciLb_ObjectIdentity = ObjectIdentity
frNniDlciLb = _FrNniDlciLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5)
)
_FrNniDlciLbRowStatusTable_Object = MibTable
frNniDlciLbRowStatusTable = _FrNniDlciLbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 1)
)
if mibBuilder.loadTexts:
    frNniDlciLbRowStatusTable.setStatus("mandatory")
_FrNniDlciLbRowStatusEntry_Object = MibTableRow
frNniDlciLbRowStatusEntry = _FrNniDlciLbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 1, 1)
)
frNniDlciLbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciLbRowStatusEntry.setStatus("mandatory")
_FrNniDlciLbRowStatus_Type = RowStatus
_FrNniDlciLbRowStatus_Object = MibTableColumn
frNniDlciLbRowStatus = _FrNniDlciLbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 1, 1, 1),
    _FrNniDlciLbRowStatus_Type()
)
frNniDlciLbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbRowStatus.setStatus("mandatory")
_FrNniDlciLbComponentName_Type = DisplayString
_FrNniDlciLbComponentName_Object = MibTableColumn
frNniDlciLbComponentName = _FrNniDlciLbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 1, 1, 2),
    _FrNniDlciLbComponentName_Type()
)
frNniDlciLbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbComponentName.setStatus("mandatory")
_FrNniDlciLbStorageType_Type = StorageType
_FrNniDlciLbStorageType_Object = MibTableColumn
frNniDlciLbStorageType = _FrNniDlciLbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 1, 1, 4),
    _FrNniDlciLbStorageType_Type()
)
frNniDlciLbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbStorageType.setStatus("mandatory")
_FrNniDlciLbIndex_Type = NonReplicated
_FrNniDlciLbIndex_Object = MibTableColumn
frNniDlciLbIndex = _FrNniDlciLbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 1, 1, 10),
    _FrNniDlciLbIndex_Type()
)
frNniDlciLbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniDlciLbIndex.setStatus("mandatory")
_FrNniDlciLbStatsTable_Object = MibTable
frNniDlciLbStatsTable = _FrNniDlciLbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10)
)
if mibBuilder.loadTexts:
    frNniDlciLbStatsTable.setStatus("mandatory")
_FrNniDlciLbStatsEntry_Object = MibTableRow
frNniDlciLbStatsEntry = _FrNniDlciLbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1)
)
frNniDlciLbStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciLbStatsEntry.setStatus("mandatory")


class _FrNniDlciLbLocalTotalFrm_Type(Unsigned32):
    """Custom type frNniDlciLbLocalTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbLocalTotalFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbLocalTotalFrm_Object = MibTableColumn
frNniDlciLbLocalTotalFrm = _FrNniDlciLbLocalTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 1),
    _FrNniDlciLbLocalTotalFrm_Type()
)
frNniDlciLbLocalTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbLocalTotalFrm.setStatus("mandatory")


class _FrNniDlciLbLocalTotalBytes_Type(Unsigned32):
    """Custom type frNniDlciLbLocalTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbLocalTotalBytes_Type.__name__ = "Unsigned32"
_FrNniDlciLbLocalTotalBytes_Object = MibTableColumn
frNniDlciLbLocalTotalBytes = _FrNniDlciLbLocalTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 2),
    _FrNniDlciLbLocalTotalBytes_Type()
)
frNniDlciLbLocalTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbLocalTotalBytes.setStatus("mandatory")


class _FrNniDlciLbLocalFecnFrm_Type(Unsigned32):
    """Custom type frNniDlciLbLocalFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbLocalFecnFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbLocalFecnFrm_Object = MibTableColumn
frNniDlciLbLocalFecnFrm = _FrNniDlciLbLocalFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 3),
    _FrNniDlciLbLocalFecnFrm_Type()
)
frNniDlciLbLocalFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbLocalFecnFrm.setStatus("mandatory")


class _FrNniDlciLbLocalBecnFrm_Type(Unsigned32):
    """Custom type frNniDlciLbLocalBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbLocalBecnFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbLocalBecnFrm_Object = MibTableColumn
frNniDlciLbLocalBecnFrm = _FrNniDlciLbLocalBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 4),
    _FrNniDlciLbLocalBecnFrm_Type()
)
frNniDlciLbLocalBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbLocalBecnFrm.setStatus("mandatory")


class _FrNniDlciLbLocalDeFrm_Type(Unsigned32):
    """Custom type frNniDlciLbLocalDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbLocalDeFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbLocalDeFrm_Object = MibTableColumn
frNniDlciLbLocalDeFrm = _FrNniDlciLbLocalDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 5),
    _FrNniDlciLbLocalDeFrm_Type()
)
frNniDlciLbLocalDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbLocalDeFrm.setStatus("mandatory")


class _FrNniDlciLbLocalDeBytes_Type(Unsigned32):
    """Custom type frNniDlciLbLocalDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbLocalDeBytes_Type.__name__ = "Unsigned32"
_FrNniDlciLbLocalDeBytes_Object = MibTableColumn
frNniDlciLbLocalDeBytes = _FrNniDlciLbLocalDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 6),
    _FrNniDlciLbLocalDeBytes_Type()
)
frNniDlciLbLocalDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbLocalDeBytes.setStatus("mandatory")


class _FrNniDlciLbRemoteTotalFrm_Type(Unsigned32):
    """Custom type frNniDlciLbRemoteTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbRemoteTotalFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbRemoteTotalFrm_Object = MibTableColumn
frNniDlciLbRemoteTotalFrm = _FrNniDlciLbRemoteTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 7),
    _FrNniDlciLbRemoteTotalFrm_Type()
)
frNniDlciLbRemoteTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbRemoteTotalFrm.setStatus("mandatory")


class _FrNniDlciLbRemoteTotalBytes_Type(Unsigned32):
    """Custom type frNniDlciLbRemoteTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbRemoteTotalBytes_Type.__name__ = "Unsigned32"
_FrNniDlciLbRemoteTotalBytes_Object = MibTableColumn
frNniDlciLbRemoteTotalBytes = _FrNniDlciLbRemoteTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 8),
    _FrNniDlciLbRemoteTotalBytes_Type()
)
frNniDlciLbRemoteTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbRemoteTotalBytes.setStatus("mandatory")


class _FrNniDlciLbRemoteFecnFrm_Type(Unsigned32):
    """Custom type frNniDlciLbRemoteFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbRemoteFecnFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbRemoteFecnFrm_Object = MibTableColumn
frNniDlciLbRemoteFecnFrm = _FrNniDlciLbRemoteFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 9),
    _FrNniDlciLbRemoteFecnFrm_Type()
)
frNniDlciLbRemoteFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbRemoteFecnFrm.setStatus("mandatory")


class _FrNniDlciLbRemoteBecnFrm_Type(Unsigned32):
    """Custom type frNniDlciLbRemoteBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbRemoteBecnFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbRemoteBecnFrm_Object = MibTableColumn
frNniDlciLbRemoteBecnFrm = _FrNniDlciLbRemoteBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 10),
    _FrNniDlciLbRemoteBecnFrm_Type()
)
frNniDlciLbRemoteBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbRemoteBecnFrm.setStatus("mandatory")


class _FrNniDlciLbRemoteDeFrm_Type(Unsigned32):
    """Custom type frNniDlciLbRemoteDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbRemoteDeFrm_Type.__name__ = "Unsigned32"
_FrNniDlciLbRemoteDeFrm_Object = MibTableColumn
frNniDlciLbRemoteDeFrm = _FrNniDlciLbRemoteDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 13),
    _FrNniDlciLbRemoteDeFrm_Type()
)
frNniDlciLbRemoteDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbRemoteDeFrm.setStatus("mandatory")


class _FrNniDlciLbRemoteDeBytes_Type(Unsigned32):
    """Custom type frNniDlciLbRemoteDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciLbRemoteDeBytes_Type.__name__ = "Unsigned32"
_FrNniDlciLbRemoteDeBytes_Object = MibTableColumn
frNniDlciLbRemoteDeBytes = _FrNniDlciLbRemoteDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 5, 10, 1, 14),
    _FrNniDlciLbRemoteDeBytes_Type()
)
frNniDlciLbRemoteDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLbRemoteDeBytes.setStatus("mandatory")
_FrNniDlciStateTable_Object = MibTable
frNniDlciStateTable = _FrNniDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10)
)
if mibBuilder.loadTexts:
    frNniDlciStateTable.setStatus("mandatory")
_FrNniDlciStateEntry_Object = MibTableRow
frNniDlciStateEntry = _FrNniDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1)
)
frNniDlciStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciStateEntry.setStatus("mandatory")


class _FrNniDlciAdminState_Type(Integer32):
    """Custom type frNniDlciAdminState based on Integer32"""
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


_FrNniDlciAdminState_Type.__name__ = "Integer32"
_FrNniDlciAdminState_Object = MibTableColumn
frNniDlciAdminState = _FrNniDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 1),
    _FrNniDlciAdminState_Type()
)
frNniDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciAdminState.setStatus("mandatory")


class _FrNniDlciOperationalState_Type(Integer32):
    """Custom type frNniDlciOperationalState based on Integer32"""
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


_FrNniDlciOperationalState_Type.__name__ = "Integer32"
_FrNniDlciOperationalState_Object = MibTableColumn
frNniDlciOperationalState = _FrNniDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 2),
    _FrNniDlciOperationalState_Type()
)
frNniDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciOperationalState.setStatus("mandatory")


class _FrNniDlciUsageState_Type(Integer32):
    """Custom type frNniDlciUsageState based on Integer32"""
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


_FrNniDlciUsageState_Type.__name__ = "Integer32"
_FrNniDlciUsageState_Object = MibTableColumn
frNniDlciUsageState = _FrNniDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 3),
    _FrNniDlciUsageState_Type()
)
frNniDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciUsageState.setStatus("mandatory")


class _FrNniDlciAvailabilityStatus_Type(OctetString):
    """Custom type frNniDlciAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FrNniDlciAvailabilityStatus_Type.__name__ = "OctetString"
_FrNniDlciAvailabilityStatus_Object = MibTableColumn
frNniDlciAvailabilityStatus = _FrNniDlciAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 4),
    _FrNniDlciAvailabilityStatus_Type()
)
frNniDlciAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciAvailabilityStatus.setStatus("mandatory")


class _FrNniDlciProceduralStatus_Type(OctetString):
    """Custom type frNniDlciProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniDlciProceduralStatus_Type.__name__ = "OctetString"
_FrNniDlciProceduralStatus_Object = MibTableColumn
frNniDlciProceduralStatus = _FrNniDlciProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 5),
    _FrNniDlciProceduralStatus_Type()
)
frNniDlciProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciProceduralStatus.setStatus("mandatory")


class _FrNniDlciControlStatus_Type(OctetString):
    """Custom type frNniDlciControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniDlciControlStatus_Type.__name__ = "OctetString"
_FrNniDlciControlStatus_Object = MibTableColumn
frNniDlciControlStatus = _FrNniDlciControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 6),
    _FrNniDlciControlStatus_Type()
)
frNniDlciControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciControlStatus.setStatus("mandatory")


class _FrNniDlciAlarmStatus_Type(OctetString):
    """Custom type frNniDlciAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniDlciAlarmStatus_Type.__name__ = "OctetString"
_FrNniDlciAlarmStatus_Object = MibTableColumn
frNniDlciAlarmStatus = _FrNniDlciAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 7),
    _FrNniDlciAlarmStatus_Type()
)
frNniDlciAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciAlarmStatus.setStatus("mandatory")


class _FrNniDlciStandbyStatus_Type(Integer32):
    """Custom type frNniDlciStandbyStatus based on Integer32"""
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


_FrNniDlciStandbyStatus_Type.__name__ = "Integer32"
_FrNniDlciStandbyStatus_Object = MibTableColumn
frNniDlciStandbyStatus = _FrNniDlciStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 8),
    _FrNniDlciStandbyStatus_Type()
)
frNniDlciStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciStandbyStatus.setStatus("mandatory")


class _FrNniDlciUnknownStatus_Type(Integer32):
    """Custom type frNniDlciUnknownStatus based on Integer32"""
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


_FrNniDlciUnknownStatus_Type.__name__ = "Integer32"
_FrNniDlciUnknownStatus_Object = MibTableColumn
frNniDlciUnknownStatus = _FrNniDlciUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 10, 1, 9),
    _FrNniDlciUnknownStatus_Type()
)
frNniDlciUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciUnknownStatus.setStatus("mandatory")
_FrNniDlciAbitTable_Object = MibTable
frNniDlciAbitTable = _FrNniDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 12)
)
if mibBuilder.loadTexts:
    frNniDlciAbitTable.setStatus("mandatory")
_FrNniDlciAbitEntry_Object = MibTableRow
frNniDlciAbitEntry = _FrNniDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 12, 1)
)
frNniDlciAbitEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciAbitEntry.setStatus("mandatory")


class _FrNniDlciABitStatusToIf_Type(Integer32):
    """Custom type frNniDlciABitStatusToIf based on Integer32"""
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


_FrNniDlciABitStatusToIf_Type.__name__ = "Integer32"
_FrNniDlciABitStatusToIf_Object = MibTableColumn
frNniDlciABitStatusToIf = _FrNniDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 12, 1, 1),
    _FrNniDlciABitStatusToIf_Type()
)
frNniDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciABitStatusToIf.setStatus("mandatory")


class _FrNniDlciABitReasonToIf_Type(Integer32):
    """Custom type frNniDlciABitReasonToIf based on Integer32"""
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


_FrNniDlciABitReasonToIf_Type.__name__ = "Integer32"
_FrNniDlciABitReasonToIf_Object = MibTableColumn
frNniDlciABitReasonToIf = _FrNniDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 12, 1, 2),
    _FrNniDlciABitReasonToIf_Type()
)
frNniDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciABitReasonToIf.setStatus("mandatory")


class _FrNniDlciABitStatusFromIf_Type(Integer32):
    """Custom type frNniDlciABitStatusFromIf based on Integer32"""
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


_FrNniDlciABitStatusFromIf_Type.__name__ = "Integer32"
_FrNniDlciABitStatusFromIf_Object = MibTableColumn
frNniDlciABitStatusFromIf = _FrNniDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 12, 1, 3),
    _FrNniDlciABitStatusFromIf_Type()
)
frNniDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciABitStatusFromIf.setStatus("mandatory")


class _FrNniDlciABitReasonFromIf_Type(Integer32):
    """Custom type frNniDlciABitReasonFromIf based on Integer32"""
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


_FrNniDlciABitReasonFromIf_Type.__name__ = "Integer32"
_FrNniDlciABitReasonFromIf_Object = MibTableColumn
frNniDlciABitReasonFromIf = _FrNniDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 12, 1, 4),
    _FrNniDlciABitReasonFromIf_Type()
)
frNniDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciABitReasonFromIf.setStatus("mandatory")


class _FrNniDlciLoopbackState_Type(Integer32):
    """Custom type frNniDlciLoopbackState based on Integer32"""
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


_FrNniDlciLoopbackState_Type.__name__ = "Integer32"
_FrNniDlciLoopbackState_Object = MibTableColumn
frNniDlciLoopbackState = _FrNniDlciLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 12, 1, 5),
    _FrNniDlciLoopbackState_Type()
)
frNniDlciLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLoopbackState.setStatus("mandatory")
_FrNniDlciSpOpTable_Object = MibTable
frNniDlciSpOpTable = _FrNniDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13)
)
if mibBuilder.loadTexts:
    frNniDlciSpOpTable.setStatus("mandatory")
_FrNniDlciSpOpEntry_Object = MibTableRow
frNniDlciSpOpEntry = _FrNniDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1)
)
frNniDlciSpOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciSpOpEntry.setStatus("mandatory")


class _FrNniDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type frNniDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_FrNniDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_FrNniDlciMaximumFrameSize_Object = MibTableColumn
frNniDlciMaximumFrameSize = _FrNniDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 1),
    _FrNniDlciMaximumFrameSize_Type()
)
frNniDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciMaximumFrameSize.setStatus("mandatory")


class _FrNniDlciRateEnforcement_Type(Integer32):
    """Custom type frNniDlciRateEnforcement based on Integer32"""
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


_FrNniDlciRateEnforcement_Type.__name__ = "Integer32"
_FrNniDlciRateEnforcement_Object = MibTableColumn
frNniDlciRateEnforcement = _FrNniDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 2),
    _FrNniDlciRateEnforcement_Type()
)
frNniDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciRateEnforcement.setStatus("obsolete")


class _FrNniDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type frNniDlciCommittedInformationRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrNniDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_FrNniDlciCommittedInformationRate_Object = MibTableColumn
frNniDlciCommittedInformationRate = _FrNniDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 3),
    _FrNniDlciCommittedInformationRate_Type()
)
frNniDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciCommittedInformationRate.setStatus("mandatory")


class _FrNniDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type frNniDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrNniDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_FrNniDlciCommittedBurstSize_Object = MibTableColumn
frNniDlciCommittedBurstSize = _FrNniDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 4),
    _FrNniDlciCommittedBurstSize_Type()
)
frNniDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciCommittedBurstSize.setStatus("mandatory")


class _FrNniDlciExcessBurstSize_Type(Unsigned32):
    """Custom type frNniDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_FrNniDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_FrNniDlciExcessBurstSize_Object = MibTableColumn
frNniDlciExcessBurstSize = _FrNniDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 5),
    _FrNniDlciExcessBurstSize_Type()
)
frNniDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciExcessBurstSize.setStatus("mandatory")


class _FrNniDlciMeasurementInterval_Type(Unsigned32):
    """Custom type frNniDlciMeasurementInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciMeasurementInterval_Type.__name__ = "Unsigned32"
_FrNniDlciMeasurementInterval_Object = MibTableColumn
frNniDlciMeasurementInterval = _FrNniDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 6),
    _FrNniDlciMeasurementInterval_Type()
)
frNniDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciMeasurementInterval.setStatus("mandatory")


class _FrNniDlciRateAdaptation_Type(Integer32):
    """Custom type frNniDlciRateAdaptation based on Integer32"""
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


_FrNniDlciRateAdaptation_Type.__name__ = "Integer32"
_FrNniDlciRateAdaptation_Object = MibTableColumn
frNniDlciRateAdaptation = _FrNniDlciRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 7),
    _FrNniDlciRateAdaptation_Type()
)
frNniDlciRateAdaptation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciRateAdaptation.setStatus("obsolete")


class _FrNniDlciAccounting_Type(Integer32):
    """Custom type frNniDlciAccounting based on Integer32"""
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


_FrNniDlciAccounting_Type.__name__ = "Integer32"
_FrNniDlciAccounting_Object = MibTableColumn
frNniDlciAccounting = _FrNniDlciAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 8),
    _FrNniDlciAccounting_Type()
)
frNniDlciAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciAccounting.setStatus("mandatory")


class _FrNniDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type frNniDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_FrNniDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_FrNniDlciEmissionPriorityToIf_Object = MibTableColumn
frNniDlciEmissionPriorityToIf = _FrNniDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 9),
    _FrNniDlciEmissionPriorityToIf_Type()
)
frNniDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciEmissionPriorityToIf.setStatus("mandatory")


class _FrNniDlciTransferPriToNwk_Type(Unsigned32):
    """Custom type frNniDlciTransferPriToNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrNniDlciTransferPriToNwk_Type.__name__ = "Unsigned32"
_FrNniDlciTransferPriToNwk_Object = MibTableColumn
frNniDlciTransferPriToNwk = _FrNniDlciTransferPriToNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 10),
    _FrNniDlciTransferPriToNwk_Type()
)
frNniDlciTransferPriToNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTransferPriToNwk.setStatus("mandatory")


class _FrNniDlciTransferPriFromNwk_Type(Unsigned32):
    """Custom type frNniDlciTransferPriFromNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrNniDlciTransferPriFromNwk_Type.__name__ = "Unsigned32"
_FrNniDlciTransferPriFromNwk_Object = MibTableColumn
frNniDlciTransferPriFromNwk = _FrNniDlciTransferPriFromNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 13, 1, 11),
    _FrNniDlciTransferPriFromNwk_Type()
)
frNniDlciTransferPriFromNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTransferPriFromNwk.setStatus("mandatory")
_FrNniDlciStatsTable_Object = MibTable
frNniDlciStatsTable = _FrNniDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14)
)
if mibBuilder.loadTexts:
    frNniDlciStatsTable.setStatus("mandatory")
_FrNniDlciStatsEntry_Object = MibTableRow
frNniDlciStatsEntry = _FrNniDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1)
)
frNniDlciStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciStatsEntry.setStatus("mandatory")


class _FrNniDlciFrmToIf_Type(Unsigned32):
    """Custom type frNniDlciFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciFrmToIf_Type.__name__ = "Unsigned32"
_FrNniDlciFrmToIf_Object = MibTableColumn
frNniDlciFrmToIf = _FrNniDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 1),
    _FrNniDlciFrmToIf_Type()
)
frNniDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciFrmToIf.setStatus("mandatory")


class _FrNniDlciFecnFrmToIf_Type(Unsigned32):
    """Custom type frNniDlciFecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciFecnFrmToIf_Type.__name__ = "Unsigned32"
_FrNniDlciFecnFrmToIf_Object = MibTableColumn
frNniDlciFecnFrmToIf = _FrNniDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 2),
    _FrNniDlciFecnFrmToIf_Type()
)
frNniDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciFecnFrmToIf.setStatus("mandatory")


class _FrNniDlciBecnFrmToIf_Type(Unsigned32):
    """Custom type frNniDlciBecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciBecnFrmToIf_Type.__name__ = "Unsigned32"
_FrNniDlciBecnFrmToIf_Object = MibTableColumn
frNniDlciBecnFrmToIf = _FrNniDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 3),
    _FrNniDlciBecnFrmToIf_Type()
)
frNniDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciBecnFrmToIf.setStatus("mandatory")


class _FrNniDlciBciToSubnet_Type(Unsigned32):
    """Custom type frNniDlciBciToSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciBciToSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciBciToSubnet_Object = MibTableColumn
frNniDlciBciToSubnet = _FrNniDlciBciToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 4),
    _FrNniDlciBciToSubnet_Type()
)
frNniDlciBciToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciBciToSubnet.setStatus("mandatory")


class _FrNniDlciDeFrmToIf_Type(Unsigned32):
    """Custom type frNniDlciDeFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDeFrmToIf_Type.__name__ = "Unsigned32"
_FrNniDlciDeFrmToIf_Object = MibTableColumn
frNniDlciDeFrmToIf = _FrNniDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 5),
    _FrNniDlciDeFrmToIf_Type()
)
frNniDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDeFrmToIf.setStatus("mandatory")


class _FrNniDlciDiscCongestedToIf_Type(Unsigned32):
    """Custom type frNniDlciDiscCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscCongestedToIf_Type.__name__ = "Unsigned32"
_FrNniDlciDiscCongestedToIf_Object = MibTableColumn
frNniDlciDiscCongestedToIf = _FrNniDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 6),
    _FrNniDlciDiscCongestedToIf_Type()
)
frNniDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscCongestedToIf.setStatus("mandatory")


class _FrNniDlciDiscDeCongestedToIf_Type(Unsigned32):
    """Custom type frNniDlciDiscDeCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscDeCongestedToIf_Type.__name__ = "Unsigned32"
_FrNniDlciDiscDeCongestedToIf_Object = MibTableColumn
frNniDlciDiscDeCongestedToIf = _FrNniDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 7),
    _FrNniDlciDiscDeCongestedToIf_Type()
)
frNniDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscDeCongestedToIf.setStatus("mandatory")


class _FrNniDlciFrmFromIf_Type(Unsigned32):
    """Custom type frNniDlciFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciFrmFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciFrmFromIf_Object = MibTableColumn
frNniDlciFrmFromIf = _FrNniDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 8),
    _FrNniDlciFrmFromIf_Type()
)
frNniDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciFrmFromIf.setStatus("mandatory")


class _FrNniDlciFecnFrmFromIf_Type(Unsigned32):
    """Custom type frNniDlciFecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciFecnFrmFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciFecnFrmFromIf_Object = MibTableColumn
frNniDlciFecnFrmFromIf = _FrNniDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 9),
    _FrNniDlciFecnFrmFromIf_Type()
)
frNniDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciFecnFrmFromIf.setStatus("mandatory")


class _FrNniDlciBecnFrmFromIf_Type(Unsigned32):
    """Custom type frNniDlciBecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciBecnFrmFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciBecnFrmFromIf_Object = MibTableColumn
frNniDlciBecnFrmFromIf = _FrNniDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 10),
    _FrNniDlciBecnFrmFromIf_Type()
)
frNniDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciBecnFrmFromIf.setStatus("mandatory")


class _FrNniDlciFciFromSubnet_Type(Unsigned32):
    """Custom type frNniDlciFciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciFciFromSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciFciFromSubnet_Object = MibTableColumn
frNniDlciFciFromSubnet = _FrNniDlciFciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 11),
    _FrNniDlciFciFromSubnet_Type()
)
frNniDlciFciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciFciFromSubnet.setStatus("mandatory")


class _FrNniDlciBciFromSubnet_Type(Unsigned32):
    """Custom type frNniDlciBciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciBciFromSubnet_Type.__name__ = "Unsigned32"
_FrNniDlciBciFromSubnet_Object = MibTableColumn
frNniDlciBciFromSubnet = _FrNniDlciBciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 12),
    _FrNniDlciBciFromSubnet_Type()
)
frNniDlciBciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciBciFromSubnet.setStatus("mandatory")


class _FrNniDlciDeFrmFromIf_Type(Unsigned32):
    """Custom type frNniDlciDeFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDeFrmFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciDeFrmFromIf_Object = MibTableColumn
frNniDlciDeFrmFromIf = _FrNniDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 13),
    _FrNniDlciDeFrmFromIf_Type()
)
frNniDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDeFrmFromIf.setStatus("mandatory")


class _FrNniDlciExcessFrmFromIf_Type(Unsigned32):
    """Custom type frNniDlciExcessFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciExcessFrmFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciExcessFrmFromIf_Object = MibTableColumn
frNniDlciExcessFrmFromIf = _FrNniDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 14),
    _FrNniDlciExcessFrmFromIf_Type()
)
frNniDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciExcessFrmFromIf.setStatus("mandatory")


class _FrNniDlciDiscExcessFromIf_Type(Unsigned32):
    """Custom type frNniDlciDiscExcessFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscExcessFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciDiscExcessFromIf_Object = MibTableColumn
frNniDlciDiscExcessFromIf = _FrNniDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 15),
    _FrNniDlciDiscExcessFromIf_Type()
)
frNniDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscExcessFromIf.setStatus("mandatory")


class _FrNniDlciDiscFrameAbit_Type(Unsigned32):
    """Custom type frNniDlciDiscFrameAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscFrameAbit_Type.__name__ = "Unsigned32"
_FrNniDlciDiscFrameAbit_Object = MibTableColumn
frNniDlciDiscFrameAbit = _FrNniDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 16),
    _FrNniDlciDiscFrameAbit_Type()
)
frNniDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscFrameAbit.setStatus("mandatory")


class _FrNniDlciDiscCongestedFromIf_Type(Unsigned32):
    """Custom type frNniDlciDiscCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscCongestedFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciDiscCongestedFromIf_Object = MibTableColumn
frNniDlciDiscCongestedFromIf = _FrNniDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 17),
    _FrNniDlciDiscCongestedFromIf_Type()
)
frNniDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscCongestedFromIf.setStatus("mandatory")


class _FrNniDlciDiscDeCongestedFromIf_Type(Unsigned32):
    """Custom type frNniDlciDiscDeCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscDeCongestedFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciDiscDeCongestedFromIf_Object = MibTableColumn
frNniDlciDiscDeCongestedFromIf = _FrNniDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 18),
    _FrNniDlciDiscDeCongestedFromIf_Type()
)
frNniDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscDeCongestedFromIf.setStatus("mandatory")


class _FrNniDlciErrorShortFrmFromIf_Type(Unsigned32):
    """Custom type frNniDlciErrorShortFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciErrorShortFrmFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciErrorShortFrmFromIf_Object = MibTableColumn
frNniDlciErrorShortFrmFromIf = _FrNniDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 19),
    _FrNniDlciErrorShortFrmFromIf_Type()
)
frNniDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciErrorShortFrmFromIf.setStatus("mandatory")


class _FrNniDlciErrorLongFrmFromIf_Type(Unsigned32):
    """Custom type frNniDlciErrorLongFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciErrorLongFrmFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciErrorLongFrmFromIf_Object = MibTableColumn
frNniDlciErrorLongFrmFromIf = _FrNniDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 20),
    _FrNniDlciErrorLongFrmFromIf_Type()
)
frNniDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciErrorLongFrmFromIf.setStatus("mandatory")


class _FrNniDlciBecnFrmSetByService_Type(Unsigned32):
    """Custom type frNniDlciBecnFrmSetByService based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciBecnFrmSetByService_Type.__name__ = "Unsigned32"
_FrNniDlciBecnFrmSetByService_Object = MibTableColumn
frNniDlciBecnFrmSetByService = _FrNniDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 21),
    _FrNniDlciBecnFrmSetByService_Type()
)
frNniDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciBecnFrmSetByService.setStatus("mandatory")


class _FrNniDlciBytesToIf_Type(Unsigned32):
    """Custom type frNniDlciBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciBytesToIf_Type.__name__ = "Unsigned32"
_FrNniDlciBytesToIf_Object = MibTableColumn
frNniDlciBytesToIf = _FrNniDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 22),
    _FrNniDlciBytesToIf_Type()
)
frNniDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciBytesToIf.setStatus("mandatory")


class _FrNniDlciDeBytesToIf_Type(Unsigned32):
    """Custom type frNniDlciDeBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDeBytesToIf_Type.__name__ = "Unsigned32"
_FrNniDlciDeBytesToIf_Object = MibTableColumn
frNniDlciDeBytesToIf = _FrNniDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 23),
    _FrNniDlciDeBytesToIf_Type()
)
frNniDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDeBytesToIf.setStatus("mandatory")


class _FrNniDlciDiscCongestedToIfBytes_Type(Unsigned32):
    """Custom type frNniDlciDiscCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscCongestedToIfBytes_Type.__name__ = "Unsigned32"
_FrNniDlciDiscCongestedToIfBytes_Object = MibTableColumn
frNniDlciDiscCongestedToIfBytes = _FrNniDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 24),
    _FrNniDlciDiscCongestedToIfBytes_Type()
)
frNniDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscCongestedToIfBytes.setStatus("mandatory")


class _FrNniDlciDiscDeCongestedToIfBytes_Type(Unsigned32):
    """Custom type frNniDlciDiscDeCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscDeCongestedToIfBytes_Type.__name__ = "Unsigned32"
_FrNniDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
frNniDlciDiscDeCongestedToIfBytes = _FrNniDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 25),
    _FrNniDlciDiscDeCongestedToIfBytes_Type()
)
frNniDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscDeCongestedToIfBytes.setStatus("mandatory")


class _FrNniDlciBytesFromIf_Type(Unsigned32):
    """Custom type frNniDlciBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciBytesFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciBytesFromIf_Object = MibTableColumn
frNniDlciBytesFromIf = _FrNniDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 26),
    _FrNniDlciBytesFromIf_Type()
)
frNniDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciBytesFromIf.setStatus("mandatory")


class _FrNniDlciDeBytesFromIf_Type(Unsigned32):
    """Custom type frNniDlciDeBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDeBytesFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciDeBytesFromIf_Object = MibTableColumn
frNniDlciDeBytesFromIf = _FrNniDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 27),
    _FrNniDlciDeBytesFromIf_Type()
)
frNniDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDeBytesFromIf.setStatus("mandatory")


class _FrNniDlciExcessBytesFromIf_Type(Unsigned32):
    """Custom type frNniDlciExcessBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciExcessBytesFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciExcessBytesFromIf_Object = MibTableColumn
frNniDlciExcessBytesFromIf = _FrNniDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 28),
    _FrNniDlciExcessBytesFromIf_Type()
)
frNniDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciExcessBytesFromIf.setStatus("mandatory")


class _FrNniDlciDiscExcessFromIfBytes_Type(Unsigned32):
    """Custom type frNniDlciDiscExcessFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscExcessFromIfBytes_Type.__name__ = "Unsigned32"
_FrNniDlciDiscExcessFromIfBytes_Object = MibTableColumn
frNniDlciDiscExcessFromIfBytes = _FrNniDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 29),
    _FrNniDlciDiscExcessFromIfBytes_Type()
)
frNniDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscExcessFromIfBytes.setStatus("mandatory")


class _FrNniDlciDiscByteAbit_Type(Unsigned32):
    """Custom type frNniDlciDiscByteAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscByteAbit_Type.__name__ = "Unsigned32"
_FrNniDlciDiscByteAbit_Object = MibTableColumn
frNniDlciDiscByteAbit = _FrNniDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 30),
    _FrNniDlciDiscByteAbit_Type()
)
frNniDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscByteAbit.setStatus("mandatory")


class _FrNniDlciDiscCongestedFromIfBytes_Type(Unsigned32):
    """Custom type frNniDlciDiscCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_FrNniDlciDiscCongestedFromIfBytes_Object = MibTableColumn
frNniDlciDiscCongestedFromIfBytes = _FrNniDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 31),
    _FrNniDlciDiscCongestedFromIfBytes_Type()
)
frNniDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscCongestedFromIfBytes.setStatus("mandatory")


class _FrNniDlciDiscDeCongestedFromIfBytes_Type(Unsigned32):
    """Custom type frNniDlciDiscDeCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscDeCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_FrNniDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
frNniDlciDiscDeCongestedFromIfBytes = _FrNniDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 32),
    _FrNniDlciDiscDeCongestedFromIfBytes_Type()
)
frNniDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")


class _FrNniDlciErrorShortBytesFromIf_Type(Unsigned32):
    """Custom type frNniDlciErrorShortBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciErrorShortBytesFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciErrorShortBytesFromIf_Object = MibTableColumn
frNniDlciErrorShortBytesFromIf = _FrNniDlciErrorShortBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 33),
    _FrNniDlciErrorShortBytesFromIf_Type()
)
frNniDlciErrorShortBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciErrorShortBytesFromIf.setStatus("mandatory")


class _FrNniDlciErrorLongBytesFromIf_Type(Unsigned32):
    """Custom type frNniDlciErrorLongBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciErrorLongBytesFromIf_Type.__name__ = "Unsigned32"
_FrNniDlciErrorLongBytesFromIf_Object = MibTableColumn
frNniDlciErrorLongBytesFromIf = _FrNniDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 34),
    _FrNniDlciErrorLongBytesFromIf_Type()
)
frNniDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciErrorLongBytesFromIf.setStatus("mandatory")


class _FrNniDlciRateAdaptReduct_Type(Unsigned32):
    """Custom type frNniDlciRateAdaptReduct based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciRateAdaptReduct_Type.__name__ = "Unsigned32"
_FrNniDlciRateAdaptReduct_Object = MibTableColumn
frNniDlciRateAdaptReduct = _FrNniDlciRateAdaptReduct_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 35),
    _FrNniDlciRateAdaptReduct_Type()
)
frNniDlciRateAdaptReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciRateAdaptReduct.setStatus("mandatory")


class _FrNniDlciRateAdaptReductPeriod_Type(Unsigned32):
    """Custom type frNniDlciRateAdaptReductPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciRateAdaptReductPeriod_Type.__name__ = "Unsigned32"
_FrNniDlciRateAdaptReductPeriod_Object = MibTableColumn
frNniDlciRateAdaptReductPeriod = _FrNniDlciRateAdaptReductPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 36),
    _FrNniDlciRateAdaptReductPeriod_Type()
)
frNniDlciRateAdaptReductPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciRateAdaptReductPeriod.setStatus("mandatory")


class _FrNniDlciTransferPriorityToNetwork_Type(Integer32):
    """Custom type frNniDlciTransferPriorityToNetwork based on Integer32"""
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


_FrNniDlciTransferPriorityToNetwork_Type.__name__ = "Integer32"
_FrNniDlciTransferPriorityToNetwork_Object = MibTableColumn
frNniDlciTransferPriorityToNetwork = _FrNniDlciTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 37),
    _FrNniDlciTransferPriorityToNetwork_Type()
)
frNniDlciTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTransferPriorityToNetwork.setStatus("obsolete")


class _FrNniDlciTransferPriorityFromNetwork_Type(Integer32):
    """Custom type frNniDlciTransferPriorityFromNetwork based on Integer32"""
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


_FrNniDlciTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_FrNniDlciTransferPriorityFromNetwork_Object = MibTableColumn
frNniDlciTransferPriorityFromNetwork = _FrNniDlciTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 38),
    _FrNniDlciTransferPriorityFromNetwork_Type()
)
frNniDlciTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTransferPriorityFromNetwork.setStatus("obsolete")


class _FrNniDlciCirPresent_Type(Unsigned32):
    """Custom type frNniDlciCirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciCirPresent_Type.__name__ = "Unsigned32"
_FrNniDlciCirPresent_Object = MibTableColumn
frNniDlciCirPresent = _FrNniDlciCirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 39),
    _FrNniDlciCirPresent_Type()
)
frNniDlciCirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciCirPresent.setStatus("mandatory")


class _FrNniDlciEirPresent_Type(Unsigned32):
    """Custom type frNniDlciEirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciEirPresent_Type.__name__ = "Unsigned32"
_FrNniDlciEirPresent_Object = MibTableColumn
frNniDlciEirPresent = _FrNniDlciEirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 14, 1, 40),
    _FrNniDlciEirPresent_Type()
)
frNniDlciEirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciEirPresent.setStatus("mandatory")
_FrNniDlciIntTable_Object = MibTable
frNniDlciIntTable = _FrNniDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15)
)
if mibBuilder.loadTexts:
    frNniDlciIntTable.setStatus("mandatory")
_FrNniDlciIntEntry_Object = MibTableRow
frNniDlciIntEntry = _FrNniDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1)
)
frNniDlciIntEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniDlciIndex"),
)
if mibBuilder.loadTexts:
    frNniDlciIntEntry.setStatus("mandatory")


class _FrNniDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type frNniDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_FrNniDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_FrNniDlciStartTime_Object = MibTableColumn
frNniDlciStartTime = _FrNniDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 1),
    _FrNniDlciStartTime_Type()
)
frNniDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciStartTime.setStatus("mandatory")


class _FrNniDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type frNniDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrNniDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_FrNniDlciTotalIngressBytes_Object = MibTableColumn
frNniDlciTotalIngressBytes = _FrNniDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 2),
    _FrNniDlciTotalIngressBytes_Type()
)
frNniDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTotalIngressBytes.setStatus("mandatory")


class _FrNniDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type frNniDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrNniDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_FrNniDlciTotalEgressBytes_Object = MibTableColumn
frNniDlciTotalEgressBytes = _FrNniDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 3),
    _FrNniDlciTotalEgressBytes_Type()
)
frNniDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTotalEgressBytes.setStatus("mandatory")


class _FrNniDlciEirIngressBytes_Type(Unsigned64):
    """Custom type frNniDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrNniDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_FrNniDlciEirIngressBytes_Object = MibTableColumn
frNniDlciEirIngressBytes = _FrNniDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 4),
    _FrNniDlciEirIngressBytes_Type()
)
frNniDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciEirIngressBytes.setStatus("mandatory")


class _FrNniDlciEirEgressBytes_Type(Unsigned64):
    """Custom type frNniDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrNniDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_FrNniDlciEirEgressBytes_Object = MibTableColumn
frNniDlciEirEgressBytes = _FrNniDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 5),
    _FrNniDlciEirEgressBytes_Type()
)
frNniDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciEirEgressBytes.setStatus("mandatory")


class _FrNniDlciDiscardedBytes_Type(Unsigned64):
    """Custom type frNniDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_FrNniDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_FrNniDlciDiscardedBytes_Object = MibTableColumn
frNniDlciDiscardedBytes = _FrNniDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 6),
    _FrNniDlciDiscardedBytes_Type()
)
frNniDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscardedBytes.setStatus("mandatory")


class _FrNniDlciTotalIngressSegFrm_Type(Unsigned32):
    """Custom type frNniDlciTotalIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciTotalIngressSegFrm_Type.__name__ = "Unsigned32"
_FrNniDlciTotalIngressSegFrm_Object = MibTableColumn
frNniDlciTotalIngressSegFrm = _FrNniDlciTotalIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 7),
    _FrNniDlciTotalIngressSegFrm_Type()
)
frNniDlciTotalIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTotalIngressSegFrm.setStatus("mandatory")


class _FrNniDlciTotalEgressSegFrm_Type(Unsigned32):
    """Custom type frNniDlciTotalEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciTotalEgressSegFrm_Type.__name__ = "Unsigned32"
_FrNniDlciTotalEgressSegFrm_Object = MibTableColumn
frNniDlciTotalEgressSegFrm = _FrNniDlciTotalEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 8),
    _FrNniDlciTotalEgressSegFrm_Type()
)
frNniDlciTotalEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciTotalEgressSegFrm.setStatus("mandatory")


class _FrNniDlciEirIngressSegFrm_Type(Unsigned32):
    """Custom type frNniDlciEirIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciEirIngressSegFrm_Type.__name__ = "Unsigned32"
_FrNniDlciEirIngressSegFrm_Object = MibTableColumn
frNniDlciEirIngressSegFrm = _FrNniDlciEirIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 9),
    _FrNniDlciEirIngressSegFrm_Type()
)
frNniDlciEirIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciEirIngressSegFrm.setStatus("mandatory")


class _FrNniDlciEirEgressSegFrm_Type(Unsigned32):
    """Custom type frNniDlciEirEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciEirEgressSegFrm_Type.__name__ = "Unsigned32"
_FrNniDlciEirEgressSegFrm_Object = MibTableColumn
frNniDlciEirEgressSegFrm = _FrNniDlciEirEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 10),
    _FrNniDlciEirEgressSegFrm_Type()
)
frNniDlciEirEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciEirEgressSegFrm.setStatus("mandatory")


class _FrNniDlciDiscardedSegFrm_Type(Unsigned32):
    """Custom type frNniDlciDiscardedSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciDiscardedSegFrm_Type.__name__ = "Unsigned32"
_FrNniDlciDiscardedSegFrm_Object = MibTableColumn
frNniDlciDiscardedSegFrm = _FrNniDlciDiscardedSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 11),
    _FrNniDlciDiscardedSegFrm_Type()
)
frNniDlciDiscardedSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciDiscardedSegFrm.setStatus("mandatory")


class _FrNniDlciCirPresentObs_Type(Unsigned32):
    """Custom type frNniDlciCirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciCirPresentObs_Type.__name__ = "Unsigned32"
_FrNniDlciCirPresentObs_Object = MibTableColumn
frNniDlciCirPresentObs = _FrNniDlciCirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 12),
    _FrNniDlciCirPresentObs_Type()
)
frNniDlciCirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciCirPresentObs.setStatus("obsolete")


class _FrNniDlciEirPresentObs_Type(Unsigned32):
    """Custom type frNniDlciEirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciEirPresentObs_Type.__name__ = "Unsigned32"
_FrNniDlciEirPresentObs_Object = MibTableColumn
frNniDlciEirPresentObs = _FrNniDlciEirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 13),
    _FrNniDlciEirPresentObs_Type()
)
frNniDlciEirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciEirPresentObs.setStatus("obsolete")


class _FrNniDlciRateEnforcementPresent_Type(Integer32):
    """Custom type frNniDlciRateEnforcementPresent based on Integer32"""
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


_FrNniDlciRateEnforcementPresent_Type.__name__ = "Integer32"
_FrNniDlciRateEnforcementPresent_Object = MibTableColumn
frNniDlciRateEnforcementPresent = _FrNniDlciRateEnforcementPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 14),
    _FrNniDlciRateEnforcementPresent_Type()
)
frNniDlciRateEnforcementPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciRateEnforcementPresent.setStatus("obsolete")


class _FrNniDlciRateAdaptationPresent_Type(Integer32):
    """Custom type frNniDlciRateAdaptationPresent based on Integer32"""
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


_FrNniDlciRateAdaptationPresent_Type.__name__ = "Integer32"
_FrNniDlciRateAdaptationPresent_Object = MibTableColumn
frNniDlciRateAdaptationPresent = _FrNniDlciRateAdaptationPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 15),
    _FrNniDlciRateAdaptationPresent_Type()
)
frNniDlciRateAdaptationPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciRateAdaptationPresent.setStatus("obsolete")


class _FrNniDlciLocalRateAdaptOccurred_Type(Integer32):
    """Custom type frNniDlciLocalRateAdaptOccurred based on Integer32"""
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


_FrNniDlciLocalRateAdaptOccurred_Type.__name__ = "Integer32"
_FrNniDlciLocalRateAdaptOccurred_Object = MibTableColumn
frNniDlciLocalRateAdaptOccurred = _FrNniDlciLocalRateAdaptOccurred_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 16),
    _FrNniDlciLocalRateAdaptOccurred_Type()
)
frNniDlciLocalRateAdaptOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciLocalRateAdaptOccurred.setStatus("mandatory")


class _FrNniDlciCallReferenceNumber_Type(Hex):
    """Custom type frNniDlciCallReferenceNumber based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrNniDlciCallReferenceNumber_Type.__name__ = "Hex"
_FrNniDlciCallReferenceNumber_Object = MibTableColumn
frNniDlciCallReferenceNumber = _FrNniDlciCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 17),
    _FrNniDlciCallReferenceNumber_Type()
)
frNniDlciCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciCallReferenceNumber.setStatus("mandatory")


class _FrNniDlciElapsedDifference_Type(Unsigned32):
    """Custom type frNniDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniDlciElapsedDifference_Type.__name__ = "Unsigned32"
_FrNniDlciElapsedDifference_Object = MibTableColumn
frNniDlciElapsedDifference = _FrNniDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 5, 15, 1, 18),
    _FrNniDlciElapsedDifference_Type()
)
frNniDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniDlciElapsedDifference.setStatus("mandatory")
_FrNniVFramer_ObjectIdentity = ObjectIdentity
frNniVFramer = _FrNniVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6)
)
_FrNniVFramerRowStatusTable_Object = MibTable
frNniVFramerRowStatusTable = _FrNniVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 1)
)
if mibBuilder.loadTexts:
    frNniVFramerRowStatusTable.setStatus("mandatory")
_FrNniVFramerRowStatusEntry_Object = MibTableRow
frNniVFramerRowStatusEntry = _FrNniVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 1, 1)
)
frNniVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniVFramerRowStatusEntry.setStatus("mandatory")
_FrNniVFramerRowStatus_Type = RowStatus
_FrNniVFramerRowStatus_Object = MibTableColumn
frNniVFramerRowStatus = _FrNniVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 1, 1, 1),
    _FrNniVFramerRowStatus_Type()
)
frNniVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniVFramerRowStatus.setStatus("mandatory")
_FrNniVFramerComponentName_Type = DisplayString
_FrNniVFramerComponentName_Object = MibTableColumn
frNniVFramerComponentName = _FrNniVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 1, 1, 2),
    _FrNniVFramerComponentName_Type()
)
frNniVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerComponentName.setStatus("mandatory")
_FrNniVFramerStorageType_Type = StorageType
_FrNniVFramerStorageType_Object = MibTableColumn
frNniVFramerStorageType = _FrNniVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 1, 1, 4),
    _FrNniVFramerStorageType_Type()
)
frNniVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerStorageType.setStatus("mandatory")
_FrNniVFramerIndex_Type = NonReplicated
_FrNniVFramerIndex_Object = MibTableColumn
frNniVFramerIndex = _FrNniVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 1, 1, 10),
    _FrNniVFramerIndex_Type()
)
frNniVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniVFramerIndex.setStatus("mandatory")
_FrNniVFramerProvTable_Object = MibTable
frNniVFramerProvTable = _FrNniVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 10)
)
if mibBuilder.loadTexts:
    frNniVFramerProvTable.setStatus("mandatory")
_FrNniVFramerProvEntry_Object = MibTableRow
frNniVFramerProvEntry = _FrNniVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 10, 1)
)
frNniVFramerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniVFramerProvEntry.setStatus("mandatory")
_FrNniVFramerOtherVirtualFramer_Type = Link
_FrNniVFramerOtherVirtualFramer_Object = MibTableColumn
frNniVFramerOtherVirtualFramer = _FrNniVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 10, 1, 1),
    _FrNniVFramerOtherVirtualFramer_Type()
)
frNniVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniVFramerOtherVirtualFramer.setStatus("mandatory")
_FrNniVFramerLogicalProcessor_Type = Link
_FrNniVFramerLogicalProcessor_Object = MibTableColumn
frNniVFramerLogicalProcessor = _FrNniVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 10, 1, 2),
    _FrNniVFramerLogicalProcessor_Type()
)
frNniVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniVFramerLogicalProcessor.setStatus("mandatory")
_FrNniVFramerStateTable_Object = MibTable
frNniVFramerStateTable = _FrNniVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 11)
)
if mibBuilder.loadTexts:
    frNniVFramerStateTable.setStatus("mandatory")
_FrNniVFramerStateEntry_Object = MibTableRow
frNniVFramerStateEntry = _FrNniVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 11, 1)
)
frNniVFramerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniVFramerStateEntry.setStatus("mandatory")


class _FrNniVFramerAdminState_Type(Integer32):
    """Custom type frNniVFramerAdminState based on Integer32"""
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


_FrNniVFramerAdminState_Type.__name__ = "Integer32"
_FrNniVFramerAdminState_Object = MibTableColumn
frNniVFramerAdminState = _FrNniVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 11, 1, 1),
    _FrNniVFramerAdminState_Type()
)
frNniVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerAdminState.setStatus("mandatory")


class _FrNniVFramerOperationalState_Type(Integer32):
    """Custom type frNniVFramerOperationalState based on Integer32"""
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


_FrNniVFramerOperationalState_Type.__name__ = "Integer32"
_FrNniVFramerOperationalState_Object = MibTableColumn
frNniVFramerOperationalState = _FrNniVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 11, 1, 2),
    _FrNniVFramerOperationalState_Type()
)
frNniVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerOperationalState.setStatus("mandatory")


class _FrNniVFramerUsageState_Type(Integer32):
    """Custom type frNniVFramerUsageState based on Integer32"""
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


_FrNniVFramerUsageState_Type.__name__ = "Integer32"
_FrNniVFramerUsageState_Object = MibTableColumn
frNniVFramerUsageState = _FrNniVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 11, 1, 3),
    _FrNniVFramerUsageState_Type()
)
frNniVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerUsageState.setStatus("mandatory")
_FrNniVFramerStatsTable_Object = MibTable
frNniVFramerStatsTable = _FrNniVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 12)
)
if mibBuilder.loadTexts:
    frNniVFramerStatsTable.setStatus("mandatory")
_FrNniVFramerStatsEntry_Object = MibTableRow
frNniVFramerStatsEntry = _FrNniVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 12, 1)
)
frNniVFramerStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    frNniVFramerStatsEntry.setStatus("mandatory")
_FrNniVFramerFrmToOtherVFramer_Type = PassportCounter64
_FrNniVFramerFrmToOtherVFramer_Object = MibTableColumn
frNniVFramerFrmToOtherVFramer = _FrNniVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 12, 1, 2),
    _FrNniVFramerFrmToOtherVFramer_Type()
)
frNniVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerFrmToOtherVFramer.setStatus("mandatory")
_FrNniVFramerFrmFromOtherVFramer_Type = PassportCounter64
_FrNniVFramerFrmFromOtherVFramer_Object = MibTableColumn
frNniVFramerFrmFromOtherVFramer = _FrNniVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 12, 1, 3),
    _FrNniVFramerFrmFromOtherVFramer_Type()
)
frNniVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerFrmFromOtherVFramer.setStatus("mandatory")
_FrNniVFramerOctetFromOtherVFramer_Type = PassportCounter64
_FrNniVFramerOctetFromOtherVFramer_Object = MibTableColumn
frNniVFramerOctetFromOtherVFramer = _FrNniVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 6, 12, 1, 5),
    _FrNniVFramerOctetFromOtherVFramer_Type()
)
frNniVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniVFramerOctetFromOtherVFramer.setStatus("mandatory")
_FrNniLts_ObjectIdentity = ObjectIdentity
frNniLts = _FrNniLts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9)
)
_FrNniLtsRowStatusTable_Object = MibTable
frNniLtsRowStatusTable = _FrNniLtsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 1)
)
if mibBuilder.loadTexts:
    frNniLtsRowStatusTable.setStatus("mandatory")
_FrNniLtsRowStatusEntry_Object = MibTableRow
frNniLtsRowStatusEntry = _FrNniLtsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 1, 1)
)
frNniLtsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsRowStatusEntry.setStatus("mandatory")
_FrNniLtsRowStatus_Type = RowStatus
_FrNniLtsRowStatus_Object = MibTableColumn
frNniLtsRowStatus = _FrNniLtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 1, 1, 1),
    _FrNniLtsRowStatus_Type()
)
frNniLtsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsRowStatus.setStatus("mandatory")
_FrNniLtsComponentName_Type = DisplayString
_FrNniLtsComponentName_Object = MibTableColumn
frNniLtsComponentName = _FrNniLtsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 1, 1, 2),
    _FrNniLtsComponentName_Type()
)
frNniLtsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsComponentName.setStatus("mandatory")
_FrNniLtsStorageType_Type = StorageType
_FrNniLtsStorageType_Object = MibTableColumn
frNniLtsStorageType = _FrNniLtsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 1, 1, 4),
    _FrNniLtsStorageType_Type()
)
frNniLtsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsStorageType.setStatus("mandatory")
_FrNniLtsIndex_Type = NonReplicated
_FrNniLtsIndex_Object = MibTableColumn
frNniLtsIndex = _FrNniLtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 1, 1, 10),
    _FrNniLtsIndex_Type()
)
frNniLtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniLtsIndex.setStatus("mandatory")
_FrNniLtsPat_ObjectIdentity = ObjectIdentity
frNniLtsPat = _FrNniLtsPat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2)
)
_FrNniLtsPatRowStatusTable_Object = MibTable
frNniLtsPatRowStatusTable = _FrNniLtsPatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 1)
)
if mibBuilder.loadTexts:
    frNniLtsPatRowStatusTable.setStatus("mandatory")
_FrNniLtsPatRowStatusEntry_Object = MibTableRow
frNniLtsPatRowStatusEntry = _FrNniLtsPatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 1, 1)
)
frNniLtsPatRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsPatRowStatusEntry.setStatus("mandatory")
_FrNniLtsPatRowStatus_Type = RowStatus
_FrNniLtsPatRowStatus_Object = MibTableColumn
frNniLtsPatRowStatus = _FrNniLtsPatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 1, 1, 1),
    _FrNniLtsPatRowStatus_Type()
)
frNniLtsPatRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatRowStatus.setStatus("mandatory")
_FrNniLtsPatComponentName_Type = DisplayString
_FrNniLtsPatComponentName_Object = MibTableColumn
frNniLtsPatComponentName = _FrNniLtsPatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 1, 1, 2),
    _FrNniLtsPatComponentName_Type()
)
frNniLtsPatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsPatComponentName.setStatus("mandatory")
_FrNniLtsPatStorageType_Type = StorageType
_FrNniLtsPatStorageType_Object = MibTableColumn
frNniLtsPatStorageType = _FrNniLtsPatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 1, 1, 4),
    _FrNniLtsPatStorageType_Type()
)
frNniLtsPatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsPatStorageType.setStatus("mandatory")


class _FrNniLtsPatIndex_Type(Integer32):
    """Custom type frNniLtsPatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_FrNniLtsPatIndex_Type.__name__ = "Integer32"
_FrNniLtsPatIndex_Object = MibTableColumn
frNniLtsPatIndex = _FrNniLtsPatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 1, 1, 10),
    _FrNniLtsPatIndex_Type()
)
frNniLtsPatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniLtsPatIndex.setStatus("mandatory")
_FrNniLtsPatDefaultsTable_Object = MibTable
frNniLtsPatDefaultsTable = _FrNniLtsPatDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10)
)
if mibBuilder.loadTexts:
    frNniLtsPatDefaultsTable.setStatus("mandatory")
_FrNniLtsPatDefaultsEntry_Object = MibTableRow
frNniLtsPatDefaultsEntry = _FrNniLtsPatDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1)
)
frNniLtsPatDefaultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsPatDefaultsEntry.setStatus("mandatory")


class _FrNniLtsPatDefaultDlci_Type(Unsigned32):
    """Custom type frNniLtsPatDefaultDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrNniLtsPatDefaultDlci_Type.__name__ = "Unsigned32"
_FrNniLtsPatDefaultDlci_Object = MibTableColumn
frNniLtsPatDefaultDlci = _FrNniLtsPatDefaultDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 200),
    _FrNniLtsPatDefaultDlci_Type()
)
frNniLtsPatDefaultDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultDlci.setStatus("mandatory")


class _FrNniLtsPatDefaultNumFrames_Type(Unsigned32):
    """Custom type frNniLtsPatDefaultNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsPatDefaultNumFrames_Type.__name__ = "Unsigned32"
_FrNniLtsPatDefaultNumFrames_Object = MibTableColumn
frNniLtsPatDefaultNumFrames = _FrNniLtsPatDefaultNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 201),
    _FrNniLtsPatDefaultNumFrames_Type()
)
frNniLtsPatDefaultNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultNumFrames.setStatus("mandatory")


class _FrNniLtsPatDefaultDataSize_Type(Unsigned32):
    """Custom type frNniLtsPatDefaultDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_FrNniLtsPatDefaultDataSize_Type.__name__ = "Unsigned32"
_FrNniLtsPatDefaultDataSize_Object = MibTableColumn
frNniLtsPatDefaultDataSize = _FrNniLtsPatDefaultDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 202),
    _FrNniLtsPatDefaultDataSize_Type()
)
frNniLtsPatDefaultDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultDataSize.setStatus("mandatory")


class _FrNniLtsPatDefaultHeaderBits_Type(OctetString):
    """Custom type frNniLtsPatDefaultHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniLtsPatDefaultHeaderBits_Type.__name__ = "OctetString"
_FrNniLtsPatDefaultHeaderBits_Object = MibTableColumn
frNniLtsPatDefaultHeaderBits = _FrNniLtsPatDefaultHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 203),
    _FrNniLtsPatDefaultHeaderBits_Type()
)
frNniLtsPatDefaultHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultHeaderBits.setStatus("mandatory")


class _FrNniLtsPatDefaultHeaderLength_Type(Unsigned32):
    """Custom type frNniLtsPatDefaultHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_FrNniLtsPatDefaultHeaderLength_Type.__name__ = "Unsigned32"
_FrNniLtsPatDefaultHeaderLength_Object = MibTableColumn
frNniLtsPatDefaultHeaderLength = _FrNniLtsPatDefaultHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 204),
    _FrNniLtsPatDefaultHeaderLength_Type()
)
frNniLtsPatDefaultHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultHeaderLength.setStatus("mandatory")


class _FrNniLtsPatDefaultEABits_Type(Hex):
    """Custom type frNniLtsPatDefaultEABits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrNniLtsPatDefaultEABits_Type.__name__ = "Hex"
_FrNniLtsPatDefaultEABits_Object = MibTableColumn
frNniLtsPatDefaultEABits = _FrNniLtsPatDefaultEABits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 205),
    _FrNniLtsPatDefaultEABits_Type()
)
frNniLtsPatDefaultEABits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultEABits.setStatus("mandatory")


class _FrNniLtsPatDefaultPayloadPattern_Type(HexString):
    """Custom type frNniLtsPatDefaultPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_FrNniLtsPatDefaultPayloadPattern_Type.__name__ = "HexString"
_FrNniLtsPatDefaultPayloadPattern_Object = MibTableColumn
frNniLtsPatDefaultPayloadPattern = _FrNniLtsPatDefaultPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 206),
    _FrNniLtsPatDefaultPayloadPattern_Type()
)
frNniLtsPatDefaultPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultPayloadPattern.setStatus("mandatory")


class _FrNniLtsPatDefaultRfc1490Header_Type(Integer32):
    """Custom type frNniLtsPatDefaultRfc1490Header based on Integer32"""
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


_FrNniLtsPatDefaultRfc1490Header_Type.__name__ = "Integer32"
_FrNniLtsPatDefaultRfc1490Header_Object = MibTableColumn
frNniLtsPatDefaultRfc1490Header = _FrNniLtsPatDefaultRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 207),
    _FrNniLtsPatDefaultRfc1490Header_Type()
)
frNniLtsPatDefaultRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultRfc1490Header.setStatus("mandatory")


class _FrNniLtsPatDefaultUseBadLrc_Type(Integer32):
    """Custom type frNniLtsPatDefaultUseBadLrc based on Integer32"""
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


_FrNniLtsPatDefaultUseBadLrc_Type.__name__ = "Integer32"
_FrNniLtsPatDefaultUseBadLrc_Object = MibTableColumn
frNniLtsPatDefaultUseBadLrc = _FrNniLtsPatDefaultUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 10, 1, 208),
    _FrNniLtsPatDefaultUseBadLrc_Type()
)
frNniLtsPatDefaultUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDefaultUseBadLrc.setStatus("mandatory")
_FrNniLtsPatSetupTable_Object = MibTable
frNniLtsPatSetupTable = _FrNniLtsPatSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11)
)
if mibBuilder.loadTexts:
    frNniLtsPatSetupTable.setStatus("mandatory")
_FrNniLtsPatSetupEntry_Object = MibTableRow
frNniLtsPatSetupEntry = _FrNniLtsPatSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1)
)
frNniLtsPatSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsPatSetupEntry.setStatus("mandatory")


class _FrNniLtsPatDlci_Type(Unsigned32):
    """Custom type frNniLtsPatDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_FrNniLtsPatDlci_Type.__name__ = "Unsigned32"
_FrNniLtsPatDlci_Object = MibTableColumn
frNniLtsPatDlci = _FrNniLtsPatDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 200),
    _FrNniLtsPatDlci_Type()
)
frNniLtsPatDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDlci.setStatus("mandatory")


class _FrNniLtsPatNumFrames_Type(Unsigned32):
    """Custom type frNniLtsPatNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsPatNumFrames_Type.__name__ = "Unsigned32"
_FrNniLtsPatNumFrames_Object = MibTableColumn
frNniLtsPatNumFrames = _FrNniLtsPatNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 201),
    _FrNniLtsPatNumFrames_Type()
)
frNniLtsPatNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatNumFrames.setStatus("mandatory")


class _FrNniLtsPatDataSize_Type(Unsigned32):
    """Custom type frNniLtsPatDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_FrNniLtsPatDataSize_Type.__name__ = "Unsigned32"
_FrNniLtsPatDataSize_Object = MibTableColumn
frNniLtsPatDataSize = _FrNniLtsPatDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 202),
    _FrNniLtsPatDataSize_Type()
)
frNniLtsPatDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatDataSize.setStatus("mandatory")


class _FrNniLtsPatHeaderBits_Type(OctetString):
    """Custom type frNniLtsPatHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniLtsPatHeaderBits_Type.__name__ = "OctetString"
_FrNniLtsPatHeaderBits_Object = MibTableColumn
frNniLtsPatHeaderBits = _FrNniLtsPatHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 203),
    _FrNniLtsPatHeaderBits_Type()
)
frNniLtsPatHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatHeaderBits.setStatus("mandatory")


class _FrNniLtsPatHeaderLength_Type(Unsigned32):
    """Custom type frNniLtsPatHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_FrNniLtsPatHeaderLength_Type.__name__ = "Unsigned32"
_FrNniLtsPatHeaderLength_Object = MibTableColumn
frNniLtsPatHeaderLength = _FrNniLtsPatHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 204),
    _FrNniLtsPatHeaderLength_Type()
)
frNniLtsPatHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatHeaderLength.setStatus("mandatory")


class _FrNniLtsPatEaBits_Type(Hex):
    """Custom type frNniLtsPatEaBits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FrNniLtsPatEaBits_Type.__name__ = "Hex"
_FrNniLtsPatEaBits_Object = MibTableColumn
frNniLtsPatEaBits = _FrNniLtsPatEaBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 205),
    _FrNniLtsPatEaBits_Type()
)
frNniLtsPatEaBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatEaBits.setStatus("mandatory")


class _FrNniLtsPatPayloadPattern_Type(HexString):
    """Custom type frNniLtsPatPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_FrNniLtsPatPayloadPattern_Type.__name__ = "HexString"
_FrNniLtsPatPayloadPattern_Object = MibTableColumn
frNniLtsPatPayloadPattern = _FrNniLtsPatPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 206),
    _FrNniLtsPatPayloadPattern_Type()
)
frNniLtsPatPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatPayloadPattern.setStatus("mandatory")


class _FrNniLtsPatRfc1490Header_Type(Integer32):
    """Custom type frNniLtsPatRfc1490Header based on Integer32"""
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


_FrNniLtsPatRfc1490Header_Type.__name__ = "Integer32"
_FrNniLtsPatRfc1490Header_Object = MibTableColumn
frNniLtsPatRfc1490Header = _FrNniLtsPatRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 207),
    _FrNniLtsPatRfc1490Header_Type()
)
frNniLtsPatRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatRfc1490Header.setStatus("mandatory")


class _FrNniLtsPatUseBadLrc_Type(Integer32):
    """Custom type frNniLtsPatUseBadLrc based on Integer32"""
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


_FrNniLtsPatUseBadLrc_Type.__name__ = "Integer32"
_FrNniLtsPatUseBadLrc_Object = MibTableColumn
frNniLtsPatUseBadLrc = _FrNniLtsPatUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 11, 1, 208),
    _FrNniLtsPatUseBadLrc_Type()
)
frNniLtsPatUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatUseBadLrc.setStatus("mandatory")
_FrNniLtsPatOpDataTable_Object = MibTable
frNniLtsPatOpDataTable = _FrNniLtsPatOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 12)
)
if mibBuilder.loadTexts:
    frNniLtsPatOpDataTable.setStatus("mandatory")
_FrNniLtsPatOpDataEntry_Object = MibTableRow
frNniLtsPatOpDataEntry = _FrNniLtsPatOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 12, 1)
)
frNniLtsPatOpDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsPatOpDataEntry.setStatus("mandatory")


class _FrNniLtsPatFramePattern_Type(HexString):
    """Custom type frNniLtsPatFramePattern based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 24),
    )


_FrNniLtsPatFramePattern_Type.__name__ = "HexString"
_FrNniLtsPatFramePattern_Object = MibTableColumn
frNniLtsPatFramePattern = _FrNniLtsPatFramePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 12, 1, 200),
    _FrNniLtsPatFramePattern_Type()
)
frNniLtsPatFramePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsPatFramePattern.setStatus("mandatory")


class _FrNniLtsPatHdlcBitsInserted_Type(Unsigned32):
    """Custom type frNniLtsPatHdlcBitsInserted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrNniLtsPatHdlcBitsInserted_Type.__name__ = "Unsigned32"
_FrNniLtsPatHdlcBitsInserted_Object = MibTableColumn
frNniLtsPatHdlcBitsInserted = _FrNniLtsPatHdlcBitsInserted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 12, 1, 201),
    _FrNniLtsPatHdlcBitsInserted_Type()
)
frNniLtsPatHdlcBitsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsPatHdlcBitsInserted.setStatus("mandatory")
_FrNniLtsPatOpStateTable_Object = MibTable
frNniLtsPatOpStateTable = _FrNniLtsPatOpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 13)
)
if mibBuilder.loadTexts:
    frNniLtsPatOpStateTable.setStatus("mandatory")
_FrNniLtsPatOpStateEntry_Object = MibTableRow
frNniLtsPatOpStateEntry = _FrNniLtsPatOpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 13, 1)
)
frNniLtsPatOpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsPatOpStateEntry.setStatus("mandatory")


class _FrNniLtsPatLoad_Type(FixedPoint3):
    """Custom type frNniLtsPatLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsPatLoad_Type.__name__ = "FixedPoint3"
_FrNniLtsPatLoad_Object = MibTableColumn
frNniLtsPatLoad = _FrNniLtsPatLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 13, 1, 200),
    _FrNniLtsPatLoad_Type()
)
frNniLtsPatLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsPatLoad.setStatus("mandatory")


class _FrNniLtsPatStatus_Type(Integer32):
    """Custom type frNniLtsPatStatus based on Integer32"""
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


_FrNniLtsPatStatus_Type.__name__ = "Integer32"
_FrNniLtsPatStatus_Object = MibTableColumn
frNniLtsPatStatus = _FrNniLtsPatStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 2, 13, 1, 201),
    _FrNniLtsPatStatus_Type()
)
frNniLtsPatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsPatStatus.setStatus("mandatory")
_FrNniLtsSetupTable_Object = MibTable
frNniLtsSetupTable = _FrNniLtsSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 10)
)
if mibBuilder.loadTexts:
    frNniLtsSetupTable.setStatus("mandatory")
_FrNniLtsSetupEntry_Object = MibTableRow
frNniLtsSetupEntry = _FrNniLtsSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 10, 1)
)
frNniLtsSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsSetupEntry.setStatus("mandatory")


class _FrNniLtsDuration_Type(Unsigned32):
    """Custom type frNniLtsDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsDuration_Type.__name__ = "Unsigned32"
_FrNniLtsDuration_Object = MibTableColumn
frNniLtsDuration = _FrNniLtsDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 10, 1, 200),
    _FrNniLtsDuration_Type()
)
frNniLtsDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsDuration.setStatus("mandatory")


class _FrNniLtsAlgorithm_Type(Integer32):
    """Custom type frNniLtsAlgorithm based on Integer32"""
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


_FrNniLtsAlgorithm_Type.__name__ = "Integer32"
_FrNniLtsAlgorithm_Object = MibTableColumn
frNniLtsAlgorithm = _FrNniLtsAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 10, 1, 201),
    _FrNniLtsAlgorithm_Type()
)
frNniLtsAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsAlgorithm.setStatus("mandatory")


class _FrNniLtsBurstSize_Type(Unsigned32):
    """Custom type frNniLtsBurstSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_FrNniLtsBurstSize_Type.__name__ = "Unsigned32"
_FrNniLtsBurstSize_Object = MibTableColumn
frNniLtsBurstSize = _FrNniLtsBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 10, 1, 204),
    _FrNniLtsBurstSize_Type()
)
frNniLtsBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsBurstSize.setStatus("mandatory")


class _FrNniLtsTimeInterval_Type(Unsigned32):
    """Custom type frNniLtsTimeInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_FrNniLtsTimeInterval_Type.__name__ = "Unsigned32"
_FrNniLtsTimeInterval_Object = MibTableColumn
frNniLtsTimeInterval = _FrNniLtsTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 10, 1, 205),
    _FrNniLtsTimeInterval_Type()
)
frNniLtsTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniLtsTimeInterval.setStatus("mandatory")
_FrNniLtsStateTable_Object = MibTable
frNniLtsStateTable = _FrNniLtsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 11)
)
if mibBuilder.loadTexts:
    frNniLtsStateTable.setStatus("mandatory")
_FrNniLtsStateEntry_Object = MibTableRow
frNniLtsStateEntry = _FrNniLtsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 11, 1)
)
frNniLtsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsStateEntry.setStatus("mandatory")


class _FrNniLtsGeneratorState_Type(Integer32):
    """Custom type frNniLtsGeneratorState based on Integer32"""
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


_FrNniLtsGeneratorState_Type.__name__ = "Integer32"
_FrNniLtsGeneratorState_Object = MibTableColumn
frNniLtsGeneratorState = _FrNniLtsGeneratorState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 11, 1, 200),
    _FrNniLtsGeneratorState_Type()
)
frNniLtsGeneratorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsGeneratorState.setStatus("mandatory")


class _FrNniLtsCycleIncomplete_Type(Integer32):
    """Custom type frNniLtsCycleIncomplete based on Integer32"""
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


_FrNniLtsCycleIncomplete_Type.__name__ = "Integer32"
_FrNniLtsCycleIncomplete_Object = MibTableColumn
frNniLtsCycleIncomplete = _FrNniLtsCycleIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 11, 1, 201),
    _FrNniLtsCycleIncomplete_Type()
)
frNniLtsCycleIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsCycleIncomplete.setStatus("mandatory")


class _FrNniLtsLastActiveInterval_Type(Unsigned32):
    """Custom type frNniLtsLastActiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsLastActiveInterval_Type.__name__ = "Unsigned32"
_FrNniLtsLastActiveInterval_Object = MibTableColumn
frNniLtsLastActiveInterval = _FrNniLtsLastActiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 11, 1, 202),
    _FrNniLtsLastActiveInterval_Type()
)
frNniLtsLastActiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsLastActiveInterval.setStatus("mandatory")


class _FrNniLtsLoad_Type(FixedPoint3):
    """Custom type frNniLtsLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsLoad_Type.__name__ = "FixedPoint3"
_FrNniLtsLoad_Object = MibTableColumn
frNniLtsLoad = _FrNniLtsLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 11, 1, 204),
    _FrNniLtsLoad_Type()
)
frNniLtsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsLoad.setStatus("mandatory")


class _FrNniLtsElapsedGenerationTime_Type(Unsigned32):
    """Custom type frNniLtsElapsedGenerationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsElapsedGenerationTime_Type.__name__ = "Unsigned32"
_FrNniLtsElapsedGenerationTime_Object = MibTableColumn
frNniLtsElapsedGenerationTime = _FrNniLtsElapsedGenerationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 11, 1, 205),
    _FrNniLtsElapsedGenerationTime_Type()
)
frNniLtsElapsedGenerationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsElapsedGenerationTime.setStatus("mandatory")
_FrNniLtsResultsTable_Object = MibTable
frNniLtsResultsTable = _FrNniLtsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 12)
)
if mibBuilder.loadTexts:
    frNniLtsResultsTable.setStatus("mandatory")
_FrNniLtsResultsEntry_Object = MibTableRow
frNniLtsResultsEntry = _FrNniLtsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 12, 1)
)
frNniLtsResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniLtsIndex"),
)
if mibBuilder.loadTexts:
    frNniLtsResultsEntry.setStatus("mandatory")
_FrNniLtsFramesTx_Type = Counter32
_FrNniLtsFramesTx_Object = MibTableColumn
frNniLtsFramesTx = _FrNniLtsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 12, 1, 200),
    _FrNniLtsFramesTx_Type()
)
frNniLtsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsFramesTx.setStatus("mandatory")


class _FrNniLtsBytesTx_Type(Unsigned32):
    """Custom type frNniLtsBytesTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsBytesTx_Type.__name__ = "Unsigned32"
_FrNniLtsBytesTx_Object = MibTableColumn
frNniLtsBytesTx = _FrNniLtsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 12, 1, 204),
    _FrNniLtsBytesTx_Type()
)
frNniLtsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsBytesTx.setStatus("mandatory")


class _FrNniLtsBitRateTx_Type(FixedPoint3):
    """Custom type frNniLtsBitRateTx based on FixedPoint3"""
    defaultValue = 0

    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsBitRateTx_Type.__name__ = "FixedPoint3"
_FrNniLtsBitRateTx_Object = MibTableColumn
frNniLtsBitRateTx = _FrNniLtsBitRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 12, 1, 208),
    _FrNniLtsBitRateTx_Type()
)
frNniLtsBitRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsBitRateTx.setStatus("mandatory")


class _FrNniLtsFrameRateTx_Type(Unsigned32):
    """Custom type frNniLtsFrameRateTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniLtsFrameRateTx_Type.__name__ = "Unsigned32"
_FrNniLtsFrameRateTx_Object = MibTableColumn
frNniLtsFrameRateTx = _FrNniLtsFrameRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 9, 12, 1, 209),
    _FrNniLtsFrameRateTx_Type()
)
frNniLtsFrameRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLtsFrameRateTx.setStatus("mandatory")
_FrNniCidDataTable_Object = MibTable
frNniCidDataTable = _FrNniCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 10)
)
if mibBuilder.loadTexts:
    frNniCidDataTable.setStatus("mandatory")
_FrNniCidDataEntry_Object = MibTableRow
frNniCidDataEntry = _FrNniCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 10, 1)
)
frNniCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
)
if mibBuilder.loadTexts:
    frNniCidDataEntry.setStatus("mandatory")


class _FrNniCustomerIdentifier_Type(Unsigned32):
    """Custom type frNniCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_FrNniCustomerIdentifier_Type.__name__ = "Unsigned32"
_FrNniCustomerIdentifier_Object = MibTableColumn
frNniCustomerIdentifier = _FrNniCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 10, 1, 1),
    _FrNniCustomerIdentifier_Type()
)
frNniCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniCustomerIdentifier.setStatus("mandatory")
_FrNniStateTable_Object = MibTable
frNniStateTable = _FrNniStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11)
)
if mibBuilder.loadTexts:
    frNniStateTable.setStatus("mandatory")
_FrNniStateEntry_Object = MibTableRow
frNniStateEntry = _FrNniStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1)
)
frNniStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
)
if mibBuilder.loadTexts:
    frNniStateEntry.setStatus("mandatory")


class _FrNniAdminState_Type(Integer32):
    """Custom type frNniAdminState based on Integer32"""
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


_FrNniAdminState_Type.__name__ = "Integer32"
_FrNniAdminState_Object = MibTableColumn
frNniAdminState = _FrNniAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 1),
    _FrNniAdminState_Type()
)
frNniAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniAdminState.setStatus("mandatory")


class _FrNniOperationalState_Type(Integer32):
    """Custom type frNniOperationalState based on Integer32"""
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


_FrNniOperationalState_Type.__name__ = "Integer32"
_FrNniOperationalState_Object = MibTableColumn
frNniOperationalState = _FrNniOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 2),
    _FrNniOperationalState_Type()
)
frNniOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniOperationalState.setStatus("mandatory")


class _FrNniUsageState_Type(Integer32):
    """Custom type frNniUsageState based on Integer32"""
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


_FrNniUsageState_Type.__name__ = "Integer32"
_FrNniUsageState_Object = MibTableColumn
frNniUsageState = _FrNniUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 3),
    _FrNniUsageState_Type()
)
frNniUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniUsageState.setStatus("mandatory")


class _FrNniAvailabilityStatus_Type(OctetString):
    """Custom type frNniAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FrNniAvailabilityStatus_Type.__name__ = "OctetString"
_FrNniAvailabilityStatus_Object = MibTableColumn
frNniAvailabilityStatus = _FrNniAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 4),
    _FrNniAvailabilityStatus_Type()
)
frNniAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniAvailabilityStatus.setStatus("mandatory")


class _FrNniProceduralStatus_Type(OctetString):
    """Custom type frNniProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniProceduralStatus_Type.__name__ = "OctetString"
_FrNniProceduralStatus_Object = MibTableColumn
frNniProceduralStatus = _FrNniProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 5),
    _FrNniProceduralStatus_Type()
)
frNniProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniProceduralStatus.setStatus("mandatory")


class _FrNniControlStatus_Type(OctetString):
    """Custom type frNniControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniControlStatus_Type.__name__ = "OctetString"
_FrNniControlStatus_Object = MibTableColumn
frNniControlStatus = _FrNniControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 6),
    _FrNniControlStatus_Type()
)
frNniControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniControlStatus.setStatus("mandatory")


class _FrNniAlarmStatus_Type(OctetString):
    """Custom type frNniAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_FrNniAlarmStatus_Type.__name__ = "OctetString"
_FrNniAlarmStatus_Object = MibTableColumn
frNniAlarmStatus = _FrNniAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 7),
    _FrNniAlarmStatus_Type()
)
frNniAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniAlarmStatus.setStatus("mandatory")


class _FrNniStandbyStatus_Type(Integer32):
    """Custom type frNniStandbyStatus based on Integer32"""
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


_FrNniStandbyStatus_Type.__name__ = "Integer32"
_FrNniStandbyStatus_Object = MibTableColumn
frNniStandbyStatus = _FrNniStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 8),
    _FrNniStandbyStatus_Type()
)
frNniStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniStandbyStatus.setStatus("mandatory")


class _FrNniUnknownStatus_Type(Integer32):
    """Custom type frNniUnknownStatus based on Integer32"""
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


_FrNniUnknownStatus_Type.__name__ = "Integer32"
_FrNniUnknownStatus_Object = MibTableColumn
frNniUnknownStatus = _FrNniUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 11, 1, 9),
    _FrNniUnknownStatus_Type()
)
frNniUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniUnknownStatus.setStatus("mandatory")
_FrNniStatsTable_Object = MibTable
frNniStatsTable = _FrNniStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 12)
)
if mibBuilder.loadTexts:
    frNniStatsTable.setStatus("mandatory")
_FrNniStatsEntry_Object = MibTableRow
frNniStatsEntry = _FrNniStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 12, 1)
)
frNniStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
)
if mibBuilder.loadTexts:
    frNniStatsEntry.setStatus("mandatory")


class _FrNniLastUnknownDlci_Type(Unsigned32):
    """Custom type frNniLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_FrNniLastUnknownDlci_Type.__name__ = "Unsigned32"
_FrNniLastUnknownDlci_Object = MibTableColumn
frNniLastUnknownDlci = _FrNniLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 12, 1, 1),
    _FrNniLastUnknownDlci_Type()
)
frNniLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniLastUnknownDlci.setStatus("mandatory")
_FrNniUnknownDlciFramesFromIf_Type = Counter32
_FrNniUnknownDlciFramesFromIf_Object = MibTableColumn
frNniUnknownDlciFramesFromIf = _FrNniUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 12, 1, 2),
    _FrNniUnknownDlciFramesFromIf_Type()
)
frNniUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniUnknownDlciFramesFromIf.setStatus("mandatory")
_FrNniInvalidHeaderFramesFromIf_Type = Counter32
_FrNniInvalidHeaderFramesFromIf_Object = MibTableColumn
frNniInvalidHeaderFramesFromIf = _FrNniInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 12, 1, 3),
    _FrNniInvalidHeaderFramesFromIf_Type()
)
frNniInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniInvalidHeaderFramesFromIf.setStatus("mandatory")
_FrNniIfEntryTable_Object = MibTable
frNniIfEntryTable = _FrNniIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 13)
)
if mibBuilder.loadTexts:
    frNniIfEntryTable.setStatus("mandatory")
_FrNniIfEntryEntry_Object = MibTableRow
frNniIfEntryEntry = _FrNniIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 13, 1)
)
frNniIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
)
if mibBuilder.loadTexts:
    frNniIfEntryEntry.setStatus("mandatory")


class _FrNniIfAdminStatus_Type(Integer32):
    """Custom type frNniIfAdminStatus based on Integer32"""
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


_FrNniIfAdminStatus_Type.__name__ = "Integer32"
_FrNniIfAdminStatus_Object = MibTableColumn
frNniIfAdminStatus = _FrNniIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 13, 1, 1),
    _FrNniIfAdminStatus_Type()
)
frNniIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniIfAdminStatus.setStatus("mandatory")


class _FrNniIfIndex_Type(InterfaceIndex):
    """Custom type frNniIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FrNniIfIndex_Type.__name__ = "InterfaceIndex"
_FrNniIfIndex_Object = MibTableColumn
frNniIfIndex = _FrNniIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 13, 1, 2),
    _FrNniIfIndex_Type()
)
frNniIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniIfIndex.setStatus("mandatory")
_FrNniOperStatusTable_Object = MibTable
frNniOperStatusTable = _FrNniOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 14)
)
if mibBuilder.loadTexts:
    frNniOperStatusTable.setStatus("mandatory")
_FrNniOperStatusEntry_Object = MibTableRow
frNniOperStatusEntry = _FrNniOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 14, 1)
)
frNniOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
)
if mibBuilder.loadTexts:
    frNniOperStatusEntry.setStatus("mandatory")


class _FrNniSnmpOperStatus_Type(Integer32):
    """Custom type frNniSnmpOperStatus based on Integer32"""
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


_FrNniSnmpOperStatus_Type.__name__ = "Integer32"
_FrNniSnmpOperStatus_Object = MibTableColumn
frNniSnmpOperStatus = _FrNniSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 14, 1, 1),
    _FrNniSnmpOperStatus_Type()
)
frNniSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniSnmpOperStatus.setStatus("mandatory")
_FrNniEmissionPriorityQsTable_Object = MibTable
frNniEmissionPriorityQsTable = _FrNniEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 15)
)
if mibBuilder.loadTexts:
    frNniEmissionPriorityQsTable.setStatus("mandatory")
_FrNniEmissionPriorityQsEntry_Object = MibTableRow
frNniEmissionPriorityQsEntry = _FrNniEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 15, 1)
)
frNniEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
)
if mibBuilder.loadTexts:
    frNniEmissionPriorityQsEntry.setStatus("mandatory")


class _FrNniNumberOfEmissionQs_Type(Unsigned32):
    """Custom type frNniNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_FrNniNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_FrNniNumberOfEmissionQs_Object = MibTableColumn
frNniNumberOfEmissionQs = _FrNniNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 15, 1, 1),
    _FrNniNumberOfEmissionQs_Type()
)
frNniNumberOfEmissionQs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frNniNumberOfEmissionQs.setStatus("mandatory")
_FrNniFrmToIfByQueueTable_Object = MibTable
frNniFrmToIfByQueueTable = _FrNniFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 341)
)
if mibBuilder.loadTexts:
    frNniFrmToIfByQueueTable.setStatus("mandatory")
_FrNniFrmToIfByQueueEntry_Object = MibTableRow
frNniFrmToIfByQueueEntry = _FrNniFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 341, 1)
)
frNniFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    frNniFrmToIfByQueueEntry.setStatus("mandatory")


class _FrNniFrmToIfByQueueIndex_Type(Integer32):
    """Custom type frNniFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrNniFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_FrNniFrmToIfByQueueIndex_Object = MibTableColumn
frNniFrmToIfByQueueIndex = _FrNniFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 341, 1, 1),
    _FrNniFrmToIfByQueueIndex_Type()
)
frNniFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniFrmToIfByQueueIndex.setStatus("mandatory")


class _FrNniFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type frNniFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_FrNniFrmToIfByQueueValue_Object = MibTableColumn
frNniFrmToIfByQueueValue = _FrNniFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 341, 1, 2),
    _FrNniFrmToIfByQueueValue_Type()
)
frNniFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniFrmToIfByQueueValue.setStatus("mandatory")
_FrNniOctetToIfByQueueTable_Object = MibTable
frNniOctetToIfByQueueTable = _FrNniOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 342)
)
if mibBuilder.loadTexts:
    frNniOctetToIfByQueueTable.setStatus("mandatory")
_FrNniOctetToIfByQueueEntry_Object = MibTableRow
frNniOctetToIfByQueueEntry = _FrNniOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 342, 1)
)
frNniOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"),
    (0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    frNniOctetToIfByQueueEntry.setStatus("mandatory")


class _FrNniOctetToIfByQueueIndex_Type(Integer32):
    """Custom type frNniOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FrNniOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_FrNniOctetToIfByQueueIndex_Object = MibTableColumn
frNniOctetToIfByQueueIndex = _FrNniOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 342, 1, 1),
    _FrNniOctetToIfByQueueIndex_Type()
)
frNniOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frNniOctetToIfByQueueIndex.setStatus("mandatory")


class _FrNniOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type frNniOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FrNniOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_FrNniOctetToIfByQueueValue_Object = MibTableColumn
frNniOctetToIfByQueueValue = _FrNniOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 342, 1, 2),
    _FrNniOctetToIfByQueueValue_Type()
)
frNniOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frNniOctetToIfByQueueValue.setStatus("mandatory")
_FrameRelayNniMIB_ObjectIdentity = ObjectIdentity
frameRelayNniMIB = _FrameRelayNniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23)
)
_FrameRelayNniGroup_ObjectIdentity = ObjectIdentity
frameRelayNniGroup = _FrameRelayNniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 1)
)
_FrameRelayNniGroupBE_ObjectIdentity = ObjectIdentity
frameRelayNniGroupBE = _FrameRelayNniGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 1, 5)
)
_FrameRelayNniGroupBE01_ObjectIdentity = ObjectIdentity
frameRelayNniGroupBE01 = _FrameRelayNniGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 1, 5, 2)
)
_FrameRelayNniGroupBE01A_ObjectIdentity = ObjectIdentity
frameRelayNniGroupBE01A = _FrameRelayNniGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 1, 5, 2, 2)
)
_FrameRelayNniCapabilities_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilities = _FrameRelayNniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 3)
)
_FrameRelayNniCapabilitiesBE_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilitiesBE = _FrameRelayNniCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 3, 5)
)
_FrameRelayNniCapabilitiesBE01_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilitiesBE01 = _FrameRelayNniCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 3, 5, 2)
)
_FrameRelayNniCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilitiesBE01A = _FrameRelayNniCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 23, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FrameRelayNniMIB",
    **{"frNni": frNni,
       "frNniRowStatusTable": frNniRowStatusTable,
       "frNniRowStatusEntry": frNniRowStatusEntry,
       "frNniRowStatus": frNniRowStatus,
       "frNniComponentName": frNniComponentName,
       "frNniStorageType": frNniStorageType,
       "frNniIndex": frNniIndex,
       "frNniDna": frNniDna,
       "frNniDnaRowStatusTable": frNniDnaRowStatusTable,
       "frNniDnaRowStatusEntry": frNniDnaRowStatusEntry,
       "frNniDnaRowStatus": frNniDnaRowStatus,
       "frNniDnaComponentName": frNniDnaComponentName,
       "frNniDnaStorageType": frNniDnaStorageType,
       "frNniDnaIndex": frNniDnaIndex,
       "frNniDnaCug": frNniDnaCug,
       "frNniDnaCugRowStatusTable": frNniDnaCugRowStatusTable,
       "frNniDnaCugRowStatusEntry": frNniDnaCugRowStatusEntry,
       "frNniDnaCugRowStatus": frNniDnaCugRowStatus,
       "frNniDnaCugComponentName": frNniDnaCugComponentName,
       "frNniDnaCugStorageType": frNniDnaCugStorageType,
       "frNniDnaCugIndex": frNniDnaCugIndex,
       "frNniDnaCugCugOptionsTable": frNniDnaCugCugOptionsTable,
       "frNniDnaCugCugOptionsEntry": frNniDnaCugCugOptionsEntry,
       "frNniDnaCugType": frNniDnaCugType,
       "frNniDnaCugDnic": frNniDnaCugDnic,
       "frNniDnaCugInterlockCode": frNniDnaCugInterlockCode,
       "frNniDnaCugPreferential": frNniDnaCugPreferential,
       "frNniDnaCugOutCalls": frNniDnaCugOutCalls,
       "frNniDnaCugIncCalls": frNniDnaCugIncCalls,
       "frNniDnaHgM": frNniDnaHgM,
       "frNniDnaHgMRowStatusTable": frNniDnaHgMRowStatusTable,
       "frNniDnaHgMRowStatusEntry": frNniDnaHgMRowStatusEntry,
       "frNniDnaHgMRowStatus": frNniDnaHgMRowStatus,
       "frNniDnaHgMComponentName": frNniDnaHgMComponentName,
       "frNniDnaHgMStorageType": frNniDnaHgMStorageType,
       "frNniDnaHgMIndex": frNniDnaHgMIndex,
       "frNniDnaHgMHgAddr": frNniDnaHgMHgAddr,
       "frNniDnaHgMHgAddrRowStatusTable": frNniDnaHgMHgAddrRowStatusTable,
       "frNniDnaHgMHgAddrRowStatusEntry": frNniDnaHgMHgAddrRowStatusEntry,
       "frNniDnaHgMHgAddrRowStatus": frNniDnaHgMHgAddrRowStatus,
       "frNniDnaHgMHgAddrComponentName": frNniDnaHgMHgAddrComponentName,
       "frNniDnaHgMHgAddrStorageType": frNniDnaHgMHgAddrStorageType,
       "frNniDnaHgMHgAddrIndex": frNniDnaHgMHgAddrIndex,
       "frNniDnaHgMHgAddrAddrTable": frNniDnaHgMHgAddrAddrTable,
       "frNniDnaHgMHgAddrAddrEntry": frNniDnaHgMHgAddrAddrEntry,
       "frNniDnaHgMHgAddrNumberingPlanIndicator": frNniDnaHgMHgAddrNumberingPlanIndicator,
       "frNniDnaHgMHgAddrDataNetworkAddress": frNniDnaHgMHgAddrDataNetworkAddress,
       "frNniDnaHgMIfTable": frNniDnaHgMIfTable,
       "frNniDnaHgMIfEntry": frNniDnaHgMIfEntry,
       "frNniDnaHgMAvailabilityUpdateThreshold": frNniDnaHgMAvailabilityUpdateThreshold,
       "frNniDnaHgMOpTable": frNniDnaHgMOpTable,
       "frNniDnaHgMOpEntry": frNniDnaHgMOpEntry,
       "frNniDnaHgMMaximumAvailableAggregateCir": frNniDnaHgMMaximumAvailableAggregateCir,
       "frNniDnaHgMAvailableAggregateCir": frNniDnaHgMAvailableAggregateCir,
       "frNniDnaHgMAvailabilityDelta": frNniDnaHgMAvailabilityDelta,
       "frNniDnaHgMAvailableDlcis": frNniDnaHgMAvailableDlcis,
       "frNniDnaAddressTable": frNniDnaAddressTable,
       "frNniDnaAddressEntry": frNniDnaAddressEntry,
       "frNniDnaNumberingPlanIndicator": frNniDnaNumberingPlanIndicator,
       "frNniDnaDataNetworkAddress": frNniDnaDataNetworkAddress,
       "frNniDnaOutgoingOptionsTable": frNniDnaOutgoingOptionsTable,
       "frNniDnaOutgoingOptionsEntry": frNniDnaOutgoingOptionsEntry,
       "frNniDnaOutDefaultPriority": frNniDnaOutDefaultPriority,
       "frNniDnaOutDefaultPathSensitivity": frNniDnaOutDefaultPathSensitivity,
       "frNniDnaOutPathSensitivityOverRide": frNniDnaOutPathSensitivityOverRide,
       "frNniDnaOutDefaultPathReliability": frNniDnaOutDefaultPathReliability,
       "frNniDnaOutAccess": frNniDnaOutAccess,
       "frNniDnaDefaultTransferPriority": frNniDnaDefaultTransferPriority,
       "frNniDnaTransferPriorityOverRide": frNniDnaTransferPriorityOverRide,
       "frNniDnaIncomingOptionsTable": frNniDnaIncomingOptionsTable,
       "frNniDnaIncomingOptionsEntry": frNniDnaIncomingOptionsEntry,
       "frNniDnaIncAccess": frNniDnaIncAccess,
       "frNniDnaCallOptionsTable": frNniDnaCallOptionsTable,
       "frNniDnaCallOptionsEntry": frNniDnaCallOptionsEntry,
       "frNniDnaAccountClass": frNniDnaAccountClass,
       "frNniDnaAccountCollection": frNniDnaAccountCollection,
       "frNniDnaServiceExchange": frNniDnaServiceExchange,
       "frNniDnaEgressAccounting": frNniDnaEgressAccounting,
       "frNniDnaDataPath": frNniDnaDataPath,
       "frNniFramer": frNniFramer,
       "frNniFramerRowStatusTable": frNniFramerRowStatusTable,
       "frNniFramerRowStatusEntry": frNniFramerRowStatusEntry,
       "frNniFramerRowStatus": frNniFramerRowStatus,
       "frNniFramerComponentName": frNniFramerComponentName,
       "frNniFramerStorageType": frNniFramerStorageType,
       "frNniFramerIndex": frNniFramerIndex,
       "frNniFramerProvTable": frNniFramerProvTable,
       "frNniFramerProvEntry": frNniFramerProvEntry,
       "frNniFramerInterfaceName": frNniFramerInterfaceName,
       "frNniFramerLinkTable": frNniFramerLinkTable,
       "frNniFramerLinkEntry": frNniFramerLinkEntry,
       "frNniFramerFlagsBetweenFrames": frNniFramerFlagsBetweenFrames,
       "frNniFramerStateTable": frNniFramerStateTable,
       "frNniFramerStateEntry": frNniFramerStateEntry,
       "frNniFramerAdminState": frNniFramerAdminState,
       "frNniFramerOperationalState": frNniFramerOperationalState,
       "frNniFramerUsageState": frNniFramerUsageState,
       "frNniFramerStatsTable": frNniFramerStatsTable,
       "frNniFramerStatsEntry": frNniFramerStatsEntry,
       "frNniFramerFrmToIf": frNniFramerFrmToIf,
       "frNniFramerFrmFromIf": frNniFramerFrmFromIf,
       "frNniFramerOctetFromIf": frNniFramerOctetFromIf,
       "frNniFramerAborts": frNniFramerAborts,
       "frNniFramerCrcErrors": frNniFramerCrcErrors,
       "frNniFramerLrcErrors": frNniFramerLrcErrors,
       "frNniFramerNonOctetErrors": frNniFramerNonOctetErrors,
       "frNniFramerOverruns": frNniFramerOverruns,
       "frNniFramerUnderruns": frNniFramerUnderruns,
       "frNniFramerLargeFrmErrors": frNniFramerLargeFrmErrors,
       "frNniFramerFrmModeErrors": frNniFramerFrmModeErrors,
       "frNniFramerUtilTable": frNniFramerUtilTable,
       "frNniFramerUtilEntry": frNniFramerUtilEntry,
       "frNniFramerNormPrioLinkUtilToIf": frNniFramerNormPrioLinkUtilToIf,
       "frNniFramerNormPrioLinkUtilFromIf": frNniFramerNormPrioLinkUtilFromIf,
       "frNniLmi": frNniLmi,
       "frNniLmiRowStatusTable": frNniLmiRowStatusTable,
       "frNniLmiRowStatusEntry": frNniLmiRowStatusEntry,
       "frNniLmiRowStatus": frNniLmiRowStatus,
       "frNniLmiComponentName": frNniLmiComponentName,
       "frNniLmiStorageType": frNniLmiStorageType,
       "frNniLmiIndex": frNniLmiIndex,
       "frNniLmiParmsTable": frNniLmiParmsTable,
       "frNniLmiParmsEntry": frNniLmiParmsEntry,
       "frNniLmiProcedures": frNniLmiProcedures,
       "frNniLmiAsyncStatusReport": frNniLmiAsyncStatusReport,
       "frNniLmiErrorEventThreshold": frNniLmiErrorEventThreshold,
       "frNniLmiEventCount": frNniLmiEventCount,
       "frNniLmiCheckPointTimer": frNniLmiCheckPointTimer,
       "frNniLmiIgnoreActiveBit": frNniLmiIgnoreActiveBit,
       "frNniLmiNniParmsTable": frNniLmiNniParmsTable,
       "frNniLmiNniParmsEntry": frNniLmiNniParmsEntry,
       "frNniLmiFullStatusPollingCycles": frNniLmiFullStatusPollingCycles,
       "frNniLmiLinkVerificationTimer": frNniLmiLinkVerificationTimer,
       "frNniLmiStateTable": frNniLmiStateTable,
       "frNniLmiStateEntry": frNniLmiStateEntry,
       "frNniLmiAdminState": frNniLmiAdminState,
       "frNniLmiOperationalState": frNniLmiOperationalState,
       "frNniLmiUsageState": frNniLmiUsageState,
       "frNniLmiPsiTable": frNniLmiPsiTable,
       "frNniLmiPsiEntry": frNniLmiPsiEntry,
       "frNniLmiProtocolStatus": frNniLmiProtocolStatus,
       "frNniLmiOpProcedures": frNniLmiOpProcedures,
       "frNniLmiStatsTable": frNniLmiStatsTable,
       "frNniLmiStatsEntry": frNniLmiStatsEntry,
       "frNniLmiKeepAliveStatusToIf": frNniLmiKeepAliveStatusToIf,
       "frNniLmiFullStatusToIf": frNniLmiFullStatusToIf,
       "frNniLmiKeepAliveStatusEnqFromIf": frNniLmiKeepAliveStatusEnqFromIf,
       "frNniLmiFullStatusEnqFromIf": frNniLmiFullStatusEnqFromIf,
       "frNniLmiNetworkSideEventHistory": frNniLmiNetworkSideEventHistory,
       "frNniLmiUserSideEventHistory": frNniLmiUserSideEventHistory,
       "frNniLmiProtocolErrors": frNniLmiProtocolErrors,
       "frNniLmiUnexpectedIes": frNniLmiUnexpectedIes,
       "frNniLmiSequenceErrors": frNniLmiSequenceErrors,
       "frNniLmiStatusSequenceErrors": frNniLmiStatusSequenceErrors,
       "frNniLmiUnexpectedReports": frNniLmiUnexpectedReports,
       "frNniLmiPollingVerifTimeouts": frNniLmiPollingVerifTimeouts,
       "frNniLmiNoStatusReportCount": frNniLmiNoStatusReportCount,
       "frNniDlci": frNniDlci,
       "frNniDlciRowStatusTable": frNniDlciRowStatusTable,
       "frNniDlciRowStatusEntry": frNniDlciRowStatusEntry,
       "frNniDlciRowStatus": frNniDlciRowStatus,
       "frNniDlciComponentName": frNniDlciComponentName,
       "frNniDlciStorageType": frNniDlciStorageType,
       "frNniDlciIndex": frNniDlciIndex,
       "frNniDlciDc": frNniDlciDc,
       "frNniDlciDcRowStatusTable": frNniDlciDcRowStatusTable,
       "frNniDlciDcRowStatusEntry": frNniDlciDcRowStatusEntry,
       "frNniDlciDcRowStatus": frNniDlciDcRowStatus,
       "frNniDlciDcComponentName": frNniDlciDcComponentName,
       "frNniDlciDcStorageType": frNniDlciDcStorageType,
       "frNniDlciDcIndex": frNniDlciDcIndex,
       "frNniDlciDcOptionsTable": frNniDlciDcOptionsTable,
       "frNniDlciDcOptionsEntry": frNniDlciDcOptionsEntry,
       "frNniDlciDcRemoteNpi": frNniDlciDcRemoteNpi,
       "frNniDlciDcRemoteDna": frNniDlciDcRemoteDna,
       "frNniDlciDcRemoteDlci": frNniDlciDcRemoteDlci,
       "frNniDlciDcType": frNniDlciDcType,
       "frNniDlciDcTransferPriority": frNniDlciDcTransferPriority,
       "frNniDlciDcDiscardPriority": frNniDlciDcDiscardPriority,
       "frNniDlciDcDeDiscardPriority": frNniDlciDcDeDiscardPriority,
       "frNniDlciDcDataPath": frNniDlciDcDataPath,
       "frNniDlciDcCugIndex": frNniDlciDcCugIndex,
       "frNniDlciDcCugType": frNniDlciDcCugType,
       "frNniDlciDcNfaTable": frNniDlciDcNfaTable,
       "frNniDlciDcNfaEntry": frNniDlciDcNfaEntry,
       "frNniDlciDcNfaIndex": frNniDlciDcNfaIndex,
       "frNniDlciDcNfaValue": frNniDlciDcNfaValue,
       "frNniDlciDcNfaRowStatus": frNniDlciDcNfaRowStatus,
       "frNniDlciVc": frNniDlciVc,
       "frNniDlciVcRowStatusTable": frNniDlciVcRowStatusTable,
       "frNniDlciVcRowStatusEntry": frNniDlciVcRowStatusEntry,
       "frNniDlciVcRowStatus": frNniDlciVcRowStatus,
       "frNniDlciVcComponentName": frNniDlciVcComponentName,
       "frNniDlciVcStorageType": frNniDlciVcStorageType,
       "frNniDlciVcIndex": frNniDlciVcIndex,
       "frNniDlciVcCadTable": frNniDlciVcCadTable,
       "frNniDlciVcCadEntry": frNniDlciVcCadEntry,
       "frNniDlciVcType": frNniDlciVcType,
       "frNniDlciVcState": frNniDlciVcState,
       "frNniDlciVcPreviousState": frNniDlciVcPreviousState,
       "frNniDlciVcDiagnosticCode": frNniDlciVcDiagnosticCode,
       "frNniDlciVcPreviousDiagnosticCode": frNniDlciVcPreviousDiagnosticCode,
       "frNniDlciVcCalledNpi": frNniDlciVcCalledNpi,
       "frNniDlciVcCalledDna": frNniDlciVcCalledDna,
       "frNniDlciVcCalledLcn": frNniDlciVcCalledLcn,
       "frNniDlciVcCallingNpi": frNniDlciVcCallingNpi,
       "frNniDlciVcCallingDna": frNniDlciVcCallingDna,
       "frNniDlciVcCallingLcn": frNniDlciVcCallingLcn,
       "frNniDlciVcAccountingEnabled": frNniDlciVcAccountingEnabled,
       "frNniDlciVcFastSelectCall": frNniDlciVcFastSelectCall,
       "frNniDlciVcPathReliability": frNniDlciVcPathReliability,
       "frNniDlciVcAccountingEnd": frNniDlciVcAccountingEnd,
       "frNniDlciVcPriority": frNniDlciVcPriority,
       "frNniDlciVcSegmentSize": frNniDlciVcSegmentSize,
       "frNniDlciVcMaxSubnetPktSize": frNniDlciVcMaxSubnetPktSize,
       "frNniDlciVcRcosToNetwork": frNniDlciVcRcosToNetwork,
       "frNniDlciVcRcosFromNetwork": frNniDlciVcRcosFromNetwork,
       "frNniDlciVcEmissionPriorityToNetwork": frNniDlciVcEmissionPriorityToNetwork,
       "frNniDlciVcEmissionPriorityFromNetwork": frNniDlciVcEmissionPriorityFromNetwork,
       "frNniDlciVcDataPath": frNniDlciVcDataPath,
       "frNniDlciVcIntdTable": frNniDlciVcIntdTable,
       "frNniDlciVcIntdEntry": frNniDlciVcIntdEntry,
       "frNniDlciVcCallReferenceNumber": frNniDlciVcCallReferenceNumber,
       "frNniDlciVcElapsedTimeTillNow": frNniDlciVcElapsedTimeTillNow,
       "frNniDlciVcSegmentsRx": frNniDlciVcSegmentsRx,
       "frNniDlciVcSegmentsSent": frNniDlciVcSegmentsSent,
       "frNniDlciVcStartTime": frNniDlciVcStartTime,
       "frNniDlciVcFrdTable": frNniDlciVcFrdTable,
       "frNniDlciVcFrdEntry": frNniDlciVcFrdEntry,
       "frNniDlciVcFrmCongestedToSubnet": frNniDlciVcFrmCongestedToSubnet,
       "frNniDlciVcCannotForwardToSubnet": frNniDlciVcCannotForwardToSubnet,
       "frNniDlciVcNotDataXferToSubnet": frNniDlciVcNotDataXferToSubnet,
       "frNniDlciVcOutOfRangeFrmFromSubnet": frNniDlciVcOutOfRangeFrmFromSubnet,
       "frNniDlciVcCombErrorsFromSubnet": frNniDlciVcCombErrorsFromSubnet,
       "frNniDlciVcDuplicatesFromSubnet": frNniDlciVcDuplicatesFromSubnet,
       "frNniDlciVcNotDataXferFromSubnet": frNniDlciVcNotDataXferFromSubnet,
       "frNniDlciVcFrmLossTimeouts": frNniDlciVcFrmLossTimeouts,
       "frNniDlciVcOoSeqByteCntExceeded": frNniDlciVcOoSeqByteCntExceeded,
       "frNniDlciVcPeakOoSeqPktCount": frNniDlciVcPeakOoSeqPktCount,
       "frNniDlciVcPeakOoSeqFrmForwarded": frNniDlciVcPeakOoSeqFrmForwarded,
       "frNniDlciVcSendSequenceNumber": frNniDlciVcSendSequenceNumber,
       "frNniDlciVcPktRetryTimeouts": frNniDlciVcPktRetryTimeouts,
       "frNniDlciVcPeakRetryQueueSize": frNniDlciVcPeakRetryQueueSize,
       "frNniDlciVcSubnetRecoveries": frNniDlciVcSubnetRecoveries,
       "frNniDlciVcOoSeqPktCntExceeded": frNniDlciVcOoSeqPktCntExceeded,
       "frNniDlciVcPeakOoSeqByteCount": frNniDlciVcPeakOoSeqByteCount,
       "frNniDlciVcDmepTable": frNniDlciVcDmepTable,
       "frNniDlciVcDmepEntry": frNniDlciVcDmepEntry,
       "frNniDlciVcDmepValue": frNniDlciVcDmepValue,
       "frNniDlciSp": frNniDlciSp,
       "frNniDlciSpRowStatusTable": frNniDlciSpRowStatusTable,
       "frNniDlciSpRowStatusEntry": frNniDlciSpRowStatusEntry,
       "frNniDlciSpRowStatus": frNniDlciSpRowStatus,
       "frNniDlciSpComponentName": frNniDlciSpComponentName,
       "frNniDlciSpStorageType": frNniDlciSpStorageType,
       "frNniDlciSpIndex": frNniDlciSpIndex,
       "frNniDlciSpParmsTable": frNniDlciSpParmsTable,
       "frNniDlciSpParmsEntry": frNniDlciSpParmsEntry,
       "frNniDlciSpMaximumFrameSize": frNniDlciSpMaximumFrameSize,
       "frNniDlciSpRateEnforcement": frNniDlciSpRateEnforcement,
       "frNniDlciSpCommittedInformationRate": frNniDlciSpCommittedInformationRate,
       "frNniDlciSpCommittedBurstSize": frNniDlciSpCommittedBurstSize,
       "frNniDlciSpExcessBurstSize": frNniDlciSpExcessBurstSize,
       "frNniDlciSpMeasurementInterval": frNniDlciSpMeasurementInterval,
       "frNniDlciSpRateAdaptation": frNniDlciSpRateAdaptation,
       "frNniDlciSpAccounting": frNniDlciSpAccounting,
       "frNniDlciSpRaSensitivity": frNniDlciSpRaSensitivity,
       "frNniDlciSpUpdateBCI": frNniDlciSpUpdateBCI,
       "frNniDlciLb": frNniDlciLb,
       "frNniDlciLbRowStatusTable": frNniDlciLbRowStatusTable,
       "frNniDlciLbRowStatusEntry": frNniDlciLbRowStatusEntry,
       "frNniDlciLbRowStatus": frNniDlciLbRowStatus,
       "frNniDlciLbComponentName": frNniDlciLbComponentName,
       "frNniDlciLbStorageType": frNniDlciLbStorageType,
       "frNniDlciLbIndex": frNniDlciLbIndex,
       "frNniDlciLbStatsTable": frNniDlciLbStatsTable,
       "frNniDlciLbStatsEntry": frNniDlciLbStatsEntry,
       "frNniDlciLbLocalTotalFrm": frNniDlciLbLocalTotalFrm,
       "frNniDlciLbLocalTotalBytes": frNniDlciLbLocalTotalBytes,
       "frNniDlciLbLocalFecnFrm": frNniDlciLbLocalFecnFrm,
       "frNniDlciLbLocalBecnFrm": frNniDlciLbLocalBecnFrm,
       "frNniDlciLbLocalDeFrm": frNniDlciLbLocalDeFrm,
       "frNniDlciLbLocalDeBytes": frNniDlciLbLocalDeBytes,
       "frNniDlciLbRemoteTotalFrm": frNniDlciLbRemoteTotalFrm,
       "frNniDlciLbRemoteTotalBytes": frNniDlciLbRemoteTotalBytes,
       "frNniDlciLbRemoteFecnFrm": frNniDlciLbRemoteFecnFrm,
       "frNniDlciLbRemoteBecnFrm": frNniDlciLbRemoteBecnFrm,
       "frNniDlciLbRemoteDeFrm": frNniDlciLbRemoteDeFrm,
       "frNniDlciLbRemoteDeBytes": frNniDlciLbRemoteDeBytes,
       "frNniDlciStateTable": frNniDlciStateTable,
       "frNniDlciStateEntry": frNniDlciStateEntry,
       "frNniDlciAdminState": frNniDlciAdminState,
       "frNniDlciOperationalState": frNniDlciOperationalState,
       "frNniDlciUsageState": frNniDlciUsageState,
       "frNniDlciAvailabilityStatus": frNniDlciAvailabilityStatus,
       "frNniDlciProceduralStatus": frNniDlciProceduralStatus,
       "frNniDlciControlStatus": frNniDlciControlStatus,
       "frNniDlciAlarmStatus": frNniDlciAlarmStatus,
       "frNniDlciStandbyStatus": frNniDlciStandbyStatus,
       "frNniDlciUnknownStatus": frNniDlciUnknownStatus,
       "frNniDlciAbitTable": frNniDlciAbitTable,
       "frNniDlciAbitEntry": frNniDlciAbitEntry,
       "frNniDlciABitStatusToIf": frNniDlciABitStatusToIf,
       "frNniDlciABitReasonToIf": frNniDlciABitReasonToIf,
       "frNniDlciABitStatusFromIf": frNniDlciABitStatusFromIf,
       "frNniDlciABitReasonFromIf": frNniDlciABitReasonFromIf,
       "frNniDlciLoopbackState": frNniDlciLoopbackState,
       "frNniDlciSpOpTable": frNniDlciSpOpTable,
       "frNniDlciSpOpEntry": frNniDlciSpOpEntry,
       "frNniDlciMaximumFrameSize": frNniDlciMaximumFrameSize,
       "frNniDlciRateEnforcement": frNniDlciRateEnforcement,
       "frNniDlciCommittedInformationRate": frNniDlciCommittedInformationRate,
       "frNniDlciCommittedBurstSize": frNniDlciCommittedBurstSize,
       "frNniDlciExcessBurstSize": frNniDlciExcessBurstSize,
       "frNniDlciMeasurementInterval": frNniDlciMeasurementInterval,
       "frNniDlciRateAdaptation": frNniDlciRateAdaptation,
       "frNniDlciAccounting": frNniDlciAccounting,
       "frNniDlciEmissionPriorityToIf": frNniDlciEmissionPriorityToIf,
       "frNniDlciTransferPriToNwk": frNniDlciTransferPriToNwk,
       "frNniDlciTransferPriFromNwk": frNniDlciTransferPriFromNwk,
       "frNniDlciStatsTable": frNniDlciStatsTable,
       "frNniDlciStatsEntry": frNniDlciStatsEntry,
       "frNniDlciFrmToIf": frNniDlciFrmToIf,
       "frNniDlciFecnFrmToIf": frNniDlciFecnFrmToIf,
       "frNniDlciBecnFrmToIf": frNniDlciBecnFrmToIf,
       "frNniDlciBciToSubnet": frNniDlciBciToSubnet,
       "frNniDlciDeFrmToIf": frNniDlciDeFrmToIf,
       "frNniDlciDiscCongestedToIf": frNniDlciDiscCongestedToIf,
       "frNniDlciDiscDeCongestedToIf": frNniDlciDiscDeCongestedToIf,
       "frNniDlciFrmFromIf": frNniDlciFrmFromIf,
       "frNniDlciFecnFrmFromIf": frNniDlciFecnFrmFromIf,
       "frNniDlciBecnFrmFromIf": frNniDlciBecnFrmFromIf,
       "frNniDlciFciFromSubnet": frNniDlciFciFromSubnet,
       "frNniDlciBciFromSubnet": frNniDlciBciFromSubnet,
       "frNniDlciDeFrmFromIf": frNniDlciDeFrmFromIf,
       "frNniDlciExcessFrmFromIf": frNniDlciExcessFrmFromIf,
       "frNniDlciDiscExcessFromIf": frNniDlciDiscExcessFromIf,
       "frNniDlciDiscFrameAbit": frNniDlciDiscFrameAbit,
       "frNniDlciDiscCongestedFromIf": frNniDlciDiscCongestedFromIf,
       "frNniDlciDiscDeCongestedFromIf": frNniDlciDiscDeCongestedFromIf,
       "frNniDlciErrorShortFrmFromIf": frNniDlciErrorShortFrmFromIf,
       "frNniDlciErrorLongFrmFromIf": frNniDlciErrorLongFrmFromIf,
       "frNniDlciBecnFrmSetByService": frNniDlciBecnFrmSetByService,
       "frNniDlciBytesToIf": frNniDlciBytesToIf,
       "frNniDlciDeBytesToIf": frNniDlciDeBytesToIf,
       "frNniDlciDiscCongestedToIfBytes": frNniDlciDiscCongestedToIfBytes,
       "frNniDlciDiscDeCongestedToIfBytes": frNniDlciDiscDeCongestedToIfBytes,
       "frNniDlciBytesFromIf": frNniDlciBytesFromIf,
       "frNniDlciDeBytesFromIf": frNniDlciDeBytesFromIf,
       "frNniDlciExcessBytesFromIf": frNniDlciExcessBytesFromIf,
       "frNniDlciDiscExcessFromIfBytes": frNniDlciDiscExcessFromIfBytes,
       "frNniDlciDiscByteAbit": frNniDlciDiscByteAbit,
       "frNniDlciDiscCongestedFromIfBytes": frNniDlciDiscCongestedFromIfBytes,
       "frNniDlciDiscDeCongestedFromIfBytes": frNniDlciDiscDeCongestedFromIfBytes,
       "frNniDlciErrorShortBytesFromIf": frNniDlciErrorShortBytesFromIf,
       "frNniDlciErrorLongBytesFromIf": frNniDlciErrorLongBytesFromIf,
       "frNniDlciRateAdaptReduct": frNniDlciRateAdaptReduct,
       "frNniDlciRateAdaptReductPeriod": frNniDlciRateAdaptReductPeriod,
       "frNniDlciTransferPriorityToNetwork": frNniDlciTransferPriorityToNetwork,
       "frNniDlciTransferPriorityFromNetwork": frNniDlciTransferPriorityFromNetwork,
       "frNniDlciCirPresent": frNniDlciCirPresent,
       "frNniDlciEirPresent": frNniDlciEirPresent,
       "frNniDlciIntTable": frNniDlciIntTable,
       "frNniDlciIntEntry": frNniDlciIntEntry,
       "frNniDlciStartTime": frNniDlciStartTime,
       "frNniDlciTotalIngressBytes": frNniDlciTotalIngressBytes,
       "frNniDlciTotalEgressBytes": frNniDlciTotalEgressBytes,
       "frNniDlciEirIngressBytes": frNniDlciEirIngressBytes,
       "frNniDlciEirEgressBytes": frNniDlciEirEgressBytes,
       "frNniDlciDiscardedBytes": frNniDlciDiscardedBytes,
       "frNniDlciTotalIngressSegFrm": frNniDlciTotalIngressSegFrm,
       "frNniDlciTotalEgressSegFrm": frNniDlciTotalEgressSegFrm,
       "frNniDlciEirIngressSegFrm": frNniDlciEirIngressSegFrm,
       "frNniDlciEirEgressSegFrm": frNniDlciEirEgressSegFrm,
       "frNniDlciDiscardedSegFrm": frNniDlciDiscardedSegFrm,
       "frNniDlciCirPresentObs": frNniDlciCirPresentObs,
       "frNniDlciEirPresentObs": frNniDlciEirPresentObs,
       "frNniDlciRateEnforcementPresent": frNniDlciRateEnforcementPresent,
       "frNniDlciRateAdaptationPresent": frNniDlciRateAdaptationPresent,
       "frNniDlciLocalRateAdaptOccurred": frNniDlciLocalRateAdaptOccurred,
       "frNniDlciCallReferenceNumber": frNniDlciCallReferenceNumber,
       "frNniDlciElapsedDifference": frNniDlciElapsedDifference,
       "frNniVFramer": frNniVFramer,
       "frNniVFramerRowStatusTable": frNniVFramerRowStatusTable,
       "frNniVFramerRowStatusEntry": frNniVFramerRowStatusEntry,
       "frNniVFramerRowStatus": frNniVFramerRowStatus,
       "frNniVFramerComponentName": frNniVFramerComponentName,
       "frNniVFramerStorageType": frNniVFramerStorageType,
       "frNniVFramerIndex": frNniVFramerIndex,
       "frNniVFramerProvTable": frNniVFramerProvTable,
       "frNniVFramerProvEntry": frNniVFramerProvEntry,
       "frNniVFramerOtherVirtualFramer": frNniVFramerOtherVirtualFramer,
       "frNniVFramerLogicalProcessor": frNniVFramerLogicalProcessor,
       "frNniVFramerStateTable": frNniVFramerStateTable,
       "frNniVFramerStateEntry": frNniVFramerStateEntry,
       "frNniVFramerAdminState": frNniVFramerAdminState,
       "frNniVFramerOperationalState": frNniVFramerOperationalState,
       "frNniVFramerUsageState": frNniVFramerUsageState,
       "frNniVFramerStatsTable": frNniVFramerStatsTable,
       "frNniVFramerStatsEntry": frNniVFramerStatsEntry,
       "frNniVFramerFrmToOtherVFramer": frNniVFramerFrmToOtherVFramer,
       "frNniVFramerFrmFromOtherVFramer": frNniVFramerFrmFromOtherVFramer,
       "frNniVFramerOctetFromOtherVFramer": frNniVFramerOctetFromOtherVFramer,
       "frNniLts": frNniLts,
       "frNniLtsRowStatusTable": frNniLtsRowStatusTable,
       "frNniLtsRowStatusEntry": frNniLtsRowStatusEntry,
       "frNniLtsRowStatus": frNniLtsRowStatus,
       "frNniLtsComponentName": frNniLtsComponentName,
       "frNniLtsStorageType": frNniLtsStorageType,
       "frNniLtsIndex": frNniLtsIndex,
       "frNniLtsPat": frNniLtsPat,
       "frNniLtsPatRowStatusTable": frNniLtsPatRowStatusTable,
       "frNniLtsPatRowStatusEntry": frNniLtsPatRowStatusEntry,
       "frNniLtsPatRowStatus": frNniLtsPatRowStatus,
       "frNniLtsPatComponentName": frNniLtsPatComponentName,
       "frNniLtsPatStorageType": frNniLtsPatStorageType,
       "frNniLtsPatIndex": frNniLtsPatIndex,
       "frNniLtsPatDefaultsTable": frNniLtsPatDefaultsTable,
       "frNniLtsPatDefaultsEntry": frNniLtsPatDefaultsEntry,
       "frNniLtsPatDefaultDlci": frNniLtsPatDefaultDlci,
       "frNniLtsPatDefaultNumFrames": frNniLtsPatDefaultNumFrames,
       "frNniLtsPatDefaultDataSize": frNniLtsPatDefaultDataSize,
       "frNniLtsPatDefaultHeaderBits": frNniLtsPatDefaultHeaderBits,
       "frNniLtsPatDefaultHeaderLength": frNniLtsPatDefaultHeaderLength,
       "frNniLtsPatDefaultEABits": frNniLtsPatDefaultEABits,
       "frNniLtsPatDefaultPayloadPattern": frNniLtsPatDefaultPayloadPattern,
       "frNniLtsPatDefaultRfc1490Header": frNniLtsPatDefaultRfc1490Header,
       "frNniLtsPatDefaultUseBadLrc": frNniLtsPatDefaultUseBadLrc,
       "frNniLtsPatSetupTable": frNniLtsPatSetupTable,
       "frNniLtsPatSetupEntry": frNniLtsPatSetupEntry,
       "frNniLtsPatDlci": frNniLtsPatDlci,
       "frNniLtsPatNumFrames": frNniLtsPatNumFrames,
       "frNniLtsPatDataSize": frNniLtsPatDataSize,
       "frNniLtsPatHeaderBits": frNniLtsPatHeaderBits,
       "frNniLtsPatHeaderLength": frNniLtsPatHeaderLength,
       "frNniLtsPatEaBits": frNniLtsPatEaBits,
       "frNniLtsPatPayloadPattern": frNniLtsPatPayloadPattern,
       "frNniLtsPatRfc1490Header": frNniLtsPatRfc1490Header,
       "frNniLtsPatUseBadLrc": frNniLtsPatUseBadLrc,
       "frNniLtsPatOpDataTable": frNniLtsPatOpDataTable,
       "frNniLtsPatOpDataEntry": frNniLtsPatOpDataEntry,
       "frNniLtsPatFramePattern": frNniLtsPatFramePattern,
       "frNniLtsPatHdlcBitsInserted": frNniLtsPatHdlcBitsInserted,
       "frNniLtsPatOpStateTable": frNniLtsPatOpStateTable,
       "frNniLtsPatOpStateEntry": frNniLtsPatOpStateEntry,
       "frNniLtsPatLoad": frNniLtsPatLoad,
       "frNniLtsPatStatus": frNniLtsPatStatus,
       "frNniLtsSetupTable": frNniLtsSetupTable,
       "frNniLtsSetupEntry": frNniLtsSetupEntry,
       "frNniLtsDuration": frNniLtsDuration,
       "frNniLtsAlgorithm": frNniLtsAlgorithm,
       "frNniLtsBurstSize": frNniLtsBurstSize,
       "frNniLtsTimeInterval": frNniLtsTimeInterval,
       "frNniLtsStateTable": frNniLtsStateTable,
       "frNniLtsStateEntry": frNniLtsStateEntry,
       "frNniLtsGeneratorState": frNniLtsGeneratorState,
       "frNniLtsCycleIncomplete": frNniLtsCycleIncomplete,
       "frNniLtsLastActiveInterval": frNniLtsLastActiveInterval,
       "frNniLtsLoad": frNniLtsLoad,
       "frNniLtsElapsedGenerationTime": frNniLtsElapsedGenerationTime,
       "frNniLtsResultsTable": frNniLtsResultsTable,
       "frNniLtsResultsEntry": frNniLtsResultsEntry,
       "frNniLtsFramesTx": frNniLtsFramesTx,
       "frNniLtsBytesTx": frNniLtsBytesTx,
       "frNniLtsBitRateTx": frNniLtsBitRateTx,
       "frNniLtsFrameRateTx": frNniLtsFrameRateTx,
       "frNniCidDataTable": frNniCidDataTable,
       "frNniCidDataEntry": frNniCidDataEntry,
       "frNniCustomerIdentifier": frNniCustomerIdentifier,
       "frNniStateTable": frNniStateTable,
       "frNniStateEntry": frNniStateEntry,
       "frNniAdminState": frNniAdminState,
       "frNniOperationalState": frNniOperationalState,
       "frNniUsageState": frNniUsageState,
       "frNniAvailabilityStatus": frNniAvailabilityStatus,
       "frNniProceduralStatus": frNniProceduralStatus,
       "frNniControlStatus": frNniControlStatus,
       "frNniAlarmStatus": frNniAlarmStatus,
       "frNniStandbyStatus": frNniStandbyStatus,
       "frNniUnknownStatus": frNniUnknownStatus,
       "frNniStatsTable": frNniStatsTable,
       "frNniStatsEntry": frNniStatsEntry,
       "frNniLastUnknownDlci": frNniLastUnknownDlci,
       "frNniUnknownDlciFramesFromIf": frNniUnknownDlciFramesFromIf,
       "frNniInvalidHeaderFramesFromIf": frNniInvalidHeaderFramesFromIf,
       "frNniIfEntryTable": frNniIfEntryTable,
       "frNniIfEntryEntry": frNniIfEntryEntry,
       "frNniIfAdminStatus": frNniIfAdminStatus,
       "frNniIfIndex": frNniIfIndex,
       "frNniOperStatusTable": frNniOperStatusTable,
       "frNniOperStatusEntry": frNniOperStatusEntry,
       "frNniSnmpOperStatus": frNniSnmpOperStatus,
       "frNniEmissionPriorityQsTable": frNniEmissionPriorityQsTable,
       "frNniEmissionPriorityQsEntry": frNniEmissionPriorityQsEntry,
       "frNniNumberOfEmissionQs": frNniNumberOfEmissionQs,
       "frNniFrmToIfByQueueTable": frNniFrmToIfByQueueTable,
       "frNniFrmToIfByQueueEntry": frNniFrmToIfByQueueEntry,
       "frNniFrmToIfByQueueIndex": frNniFrmToIfByQueueIndex,
       "frNniFrmToIfByQueueValue": frNniFrmToIfByQueueValue,
       "frNniOctetToIfByQueueTable": frNniOctetToIfByQueueTable,
       "frNniOctetToIfByQueueEntry": frNniOctetToIfByQueueEntry,
       "frNniOctetToIfByQueueIndex": frNniOctetToIfByQueueIndex,
       "frNniOctetToIfByQueueValue": frNniOctetToIfByQueueValue,
       "frameRelayNniMIB": frameRelayNniMIB,
       "frameRelayNniGroup": frameRelayNniGroup,
       "frameRelayNniGroupBE": frameRelayNniGroupBE,
       "frameRelayNniGroupBE01": frameRelayNniGroupBE01,
       "frameRelayNniGroupBE01A": frameRelayNniGroupBE01A,
       "frameRelayNniCapabilities": frameRelayNniCapabilities,
       "frameRelayNniCapabilitiesBE": frameRelayNniCapabilitiesBE,
       "frameRelayNniCapabilitiesBE01": frameRelayNniCapabilitiesBE01,
       "frameRelayNniCapabilitiesBE01A": frameRelayNniCapabilitiesBE01A}
)
