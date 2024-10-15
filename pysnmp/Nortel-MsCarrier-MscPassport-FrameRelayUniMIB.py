# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayUniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayUniMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:27 2024
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
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
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
 PassportCounter64,
 Unsigned64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "FixedPoint3",
    "Hex",
    "HexString",
    "Link",
    "NonReplicated",
    "PassportCounter64",
    "Unsigned64")

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

_MscFrUni_ObjectIdentity = ObjectIdentity
mscFrUni = _MscFrUni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71)
)
_MscFrUniRowStatusTable_Object = MibTable
mscFrUniRowStatusTable = _MscFrUniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 1)
)
if mibBuilder.loadTexts:
    mscFrUniRowStatusTable.setStatus("mandatory")
_MscFrUniRowStatusEntry_Object = MibTableRow
mscFrUniRowStatusEntry = _MscFrUniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 1, 1)
)
mscFrUniRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniRowStatusEntry.setStatus("mandatory")
_MscFrUniRowStatus_Type = RowStatus
_MscFrUniRowStatus_Object = MibTableColumn
mscFrUniRowStatus = _MscFrUniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 1, 1, 1),
    _MscFrUniRowStatus_Type()
)
mscFrUniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniRowStatus.setStatus("mandatory")
_MscFrUniComponentName_Type = DisplayString
_MscFrUniComponentName_Object = MibTableColumn
mscFrUniComponentName = _MscFrUniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 1, 1, 2),
    _MscFrUniComponentName_Type()
)
mscFrUniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniComponentName.setStatus("mandatory")
_MscFrUniStorageType_Type = StorageType
_MscFrUniStorageType_Object = MibTableColumn
mscFrUniStorageType = _MscFrUniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 1, 1, 4),
    _MscFrUniStorageType_Type()
)
mscFrUniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniStorageType.setStatus("mandatory")


class _MscFrUniIndex_Type(Integer32):
    """Custom type mscFrUniIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrUniIndex_Type.__name__ = "Integer32"
_MscFrUniIndex_Object = MibTableColumn
mscFrUniIndex = _MscFrUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 1, 1, 10),
    _MscFrUniIndex_Type()
)
mscFrUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniIndex.setStatus("mandatory")
_MscFrUniDna_ObjectIdentity = ObjectIdentity
mscFrUniDna = _MscFrUniDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2)
)
_MscFrUniDnaRowStatusTable_Object = MibTable
mscFrUniDnaRowStatusTable = _MscFrUniDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDnaRowStatusTable.setStatus("mandatory")
_MscFrUniDnaRowStatusEntry_Object = MibTableRow
mscFrUniDnaRowStatusEntry = _MscFrUniDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 1, 1)
)
mscFrUniDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaRowStatusEntry.setStatus("mandatory")
_MscFrUniDnaRowStatus_Type = RowStatus
_MscFrUniDnaRowStatus_Object = MibTableColumn
mscFrUniDnaRowStatus = _MscFrUniDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 1, 1, 1),
    _MscFrUniDnaRowStatus_Type()
)
mscFrUniDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaRowStatus.setStatus("mandatory")
_MscFrUniDnaComponentName_Type = DisplayString
_MscFrUniDnaComponentName_Object = MibTableColumn
mscFrUniDnaComponentName = _MscFrUniDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 1, 1, 2),
    _MscFrUniDnaComponentName_Type()
)
mscFrUniDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaComponentName.setStatus("mandatory")
_MscFrUniDnaStorageType_Type = StorageType
_MscFrUniDnaStorageType_Object = MibTableColumn
mscFrUniDnaStorageType = _MscFrUniDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 1, 1, 4),
    _MscFrUniDnaStorageType_Type()
)
mscFrUniDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaStorageType.setStatus("mandatory")
_MscFrUniDnaIndex_Type = NonReplicated
_MscFrUniDnaIndex_Object = MibTableColumn
mscFrUniDnaIndex = _MscFrUniDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 1, 1, 10),
    _MscFrUniDnaIndex_Type()
)
mscFrUniDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDnaIndex.setStatus("mandatory")
_MscFrUniDnaCug_ObjectIdentity = ObjectIdentity
mscFrUniDnaCug = _MscFrUniDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2)
)
_MscFrUniDnaCugRowStatusTable_Object = MibTable
mscFrUniDnaCugRowStatusTable = _MscFrUniDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDnaCugRowStatusTable.setStatus("mandatory")
_MscFrUniDnaCugRowStatusEntry_Object = MibTableRow
mscFrUniDnaCugRowStatusEntry = _MscFrUniDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 1, 1)
)
mscFrUniDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaCugRowStatusEntry.setStatus("mandatory")
_MscFrUniDnaCugRowStatus_Type = RowStatus
_MscFrUniDnaCugRowStatus_Object = MibTableColumn
mscFrUniDnaCugRowStatus = _MscFrUniDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 1, 1, 1),
    _MscFrUniDnaCugRowStatus_Type()
)
mscFrUniDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaCugRowStatus.setStatus("mandatory")
_MscFrUniDnaCugComponentName_Type = DisplayString
_MscFrUniDnaCugComponentName_Object = MibTableColumn
mscFrUniDnaCugComponentName = _MscFrUniDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 1, 1, 2),
    _MscFrUniDnaCugComponentName_Type()
)
mscFrUniDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaCugComponentName.setStatus("mandatory")
_MscFrUniDnaCugStorageType_Type = StorageType
_MscFrUniDnaCugStorageType_Object = MibTableColumn
mscFrUniDnaCugStorageType = _MscFrUniDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 1, 1, 4),
    _MscFrUniDnaCugStorageType_Type()
)
mscFrUniDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaCugStorageType.setStatus("mandatory")


class _MscFrUniDnaCugIndex_Type(Integer32):
    """Custom type mscFrUniDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniDnaCugIndex_Type.__name__ = "Integer32"
_MscFrUniDnaCugIndex_Object = MibTableColumn
mscFrUniDnaCugIndex = _MscFrUniDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 1, 1, 10),
    _MscFrUniDnaCugIndex_Type()
)
mscFrUniDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDnaCugIndex.setStatus("mandatory")
_MscFrUniDnaCugCugOptionsTable_Object = MibTable
mscFrUniDnaCugCugOptionsTable = _MscFrUniDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDnaCugCugOptionsTable.setStatus("mandatory")
_MscFrUniDnaCugCugOptionsEntry_Object = MibTableRow
mscFrUniDnaCugCugOptionsEntry = _MscFrUniDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10, 1)
)
mscFrUniDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaCugCugOptionsEntry.setStatus("mandatory")


class _MscFrUniDnaCugType_Type(Integer32):
    """Custom type mscFrUniDnaCugType based on Integer32"""
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


_MscFrUniDnaCugType_Type.__name__ = "Integer32"
_MscFrUniDnaCugType_Object = MibTableColumn
mscFrUniDnaCugType = _MscFrUniDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10, 1, 1),
    _MscFrUniDnaCugType_Type()
)
mscFrUniDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaCugType.setStatus("mandatory")


class _MscFrUniDnaCugDnic_Type(DigitString):
    """Custom type mscFrUniDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscFrUniDnaCugDnic_Type.__name__ = "DigitString"
_MscFrUniDnaCugDnic_Object = MibTableColumn
mscFrUniDnaCugDnic = _MscFrUniDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10, 1, 2),
    _MscFrUniDnaCugDnic_Type()
)
mscFrUniDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaCugDnic.setStatus("mandatory")


class _MscFrUniDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscFrUniDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFrUniDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscFrUniDnaCugInterlockCode_Object = MibTableColumn
mscFrUniDnaCugInterlockCode = _MscFrUniDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10, 1, 3),
    _MscFrUniDnaCugInterlockCode_Type()
)
mscFrUniDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaCugInterlockCode.setStatus("mandatory")


class _MscFrUniDnaCugPreferential_Type(Integer32):
    """Custom type mscFrUniDnaCugPreferential based on Integer32"""
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


_MscFrUniDnaCugPreferential_Type.__name__ = "Integer32"
_MscFrUniDnaCugPreferential_Object = MibTableColumn
mscFrUniDnaCugPreferential = _MscFrUniDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10, 1, 4),
    _MscFrUniDnaCugPreferential_Type()
)
mscFrUniDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaCugPreferential.setStatus("mandatory")


class _MscFrUniDnaCugOutCalls_Type(Integer32):
    """Custom type mscFrUniDnaCugOutCalls based on Integer32"""
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


_MscFrUniDnaCugOutCalls_Type.__name__ = "Integer32"
_MscFrUniDnaCugOutCalls_Object = MibTableColumn
mscFrUniDnaCugOutCalls = _MscFrUniDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10, 1, 5),
    _MscFrUniDnaCugOutCalls_Type()
)
mscFrUniDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaCugOutCalls.setStatus("mandatory")


class _MscFrUniDnaCugIncCalls_Type(Integer32):
    """Custom type mscFrUniDnaCugIncCalls based on Integer32"""
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


_MscFrUniDnaCugIncCalls_Type.__name__ = "Integer32"
_MscFrUniDnaCugIncCalls_Object = MibTableColumn
mscFrUniDnaCugIncCalls = _MscFrUniDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 2, 10, 1, 6),
    _MscFrUniDnaCugIncCalls_Type()
)
mscFrUniDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaCugIncCalls.setStatus("mandatory")
_MscFrUniDnaHgM_ObjectIdentity = ObjectIdentity
mscFrUniDnaHgM = _MscFrUniDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3)
)
_MscFrUniDnaHgMRowStatusTable_Object = MibTable
mscFrUniDnaHgMRowStatusTable = _MscFrUniDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMRowStatusTable.setStatus("mandatory")
_MscFrUniDnaHgMRowStatusEntry_Object = MibTableRow
mscFrUniDnaHgMRowStatusEntry = _MscFrUniDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 1, 1)
)
mscFrUniDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMRowStatusEntry.setStatus("mandatory")
_MscFrUniDnaHgMRowStatus_Type = RowStatus
_MscFrUniDnaHgMRowStatus_Object = MibTableColumn
mscFrUniDnaHgMRowStatus = _MscFrUniDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 1, 1, 1),
    _MscFrUniDnaHgMRowStatus_Type()
)
mscFrUniDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMRowStatus.setStatus("mandatory")
_MscFrUniDnaHgMComponentName_Type = DisplayString
_MscFrUniDnaHgMComponentName_Object = MibTableColumn
mscFrUniDnaHgMComponentName = _MscFrUniDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 1, 1, 2),
    _MscFrUniDnaHgMComponentName_Type()
)
mscFrUniDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMComponentName.setStatus("mandatory")
_MscFrUniDnaHgMStorageType_Type = StorageType
_MscFrUniDnaHgMStorageType_Object = MibTableColumn
mscFrUniDnaHgMStorageType = _MscFrUniDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 1, 1, 4),
    _MscFrUniDnaHgMStorageType_Type()
)
mscFrUniDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMStorageType.setStatus("mandatory")
_MscFrUniDnaHgMIndex_Type = NonReplicated
_MscFrUniDnaHgMIndex_Object = MibTableColumn
mscFrUniDnaHgMIndex = _MscFrUniDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 1, 1, 10),
    _MscFrUniDnaHgMIndex_Type()
)
mscFrUniDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMIndex.setStatus("mandatory")
_MscFrUniDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
mscFrUniDnaHgMHgAddr = _MscFrUniDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2)
)
_MscFrUniDnaHgMHgAddrRowStatusTable_Object = MibTable
mscFrUniDnaHgMHgAddrRowStatusTable = _MscFrUniDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_MscFrUniDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
mscFrUniDnaHgMHgAddrRowStatusEntry = _MscFrUniDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 1, 1)
)
mscFrUniDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_MscFrUniDnaHgMHgAddrRowStatus_Type = RowStatus
_MscFrUniDnaHgMHgAddrRowStatus_Object = MibTableColumn
mscFrUniDnaHgMHgAddrRowStatus = _MscFrUniDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 1, 1, 1),
    _MscFrUniDnaHgMHgAddrRowStatus_Type()
)
mscFrUniDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrRowStatus.setStatus("mandatory")
_MscFrUniDnaHgMHgAddrComponentName_Type = DisplayString
_MscFrUniDnaHgMHgAddrComponentName_Object = MibTableColumn
mscFrUniDnaHgMHgAddrComponentName = _MscFrUniDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 1, 1, 2),
    _MscFrUniDnaHgMHgAddrComponentName_Type()
)
mscFrUniDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrComponentName.setStatus("mandatory")
_MscFrUniDnaHgMHgAddrStorageType_Type = StorageType
_MscFrUniDnaHgMHgAddrStorageType_Object = MibTableColumn
mscFrUniDnaHgMHgAddrStorageType = _MscFrUniDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 1, 1, 4),
    _MscFrUniDnaHgMHgAddrStorageType_Type()
)
mscFrUniDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrStorageType.setStatus("mandatory")


class _MscFrUniDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type mscFrUniDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MscFrUniDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_MscFrUniDnaHgMHgAddrIndex_Object = MibTableColumn
mscFrUniDnaHgMHgAddrIndex = _MscFrUniDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 1, 1, 10),
    _MscFrUniDnaHgMHgAddrIndex_Type()
)
mscFrUniDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrIndex.setStatus("mandatory")
_MscFrUniDnaHgMHgAddrAddrTable_Object = MibTable
mscFrUniDnaHgMHgAddrAddrTable = _MscFrUniDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrAddrTable.setStatus("mandatory")
_MscFrUniDnaHgMHgAddrAddrEntry_Object = MibTableRow
mscFrUniDnaHgMHgAddrAddrEntry = _MscFrUniDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 10, 1)
)
mscFrUniDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _MscFrUniDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type mscFrUniDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
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


_MscFrUniDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscFrUniDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
mscFrUniDnaHgMHgAddrNumberingPlanIndicator = _MscFrUniDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 10, 1, 1),
    _MscFrUniDnaHgMHgAddrNumberingPlanIndicator_Type()
)
mscFrUniDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _MscFrUniDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type mscFrUniDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrUniDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_MscFrUniDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
mscFrUniDnaHgMHgAddrDataNetworkAddress = _MscFrUniDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 2, 10, 1, 2),
    _MscFrUniDnaHgMHgAddrDataNetworkAddress_Type()
)
mscFrUniDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_MscFrUniDnaHgMIfTable_Object = MibTable
mscFrUniDnaHgMIfTable = _MscFrUniDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMIfTable.setStatus("mandatory")
_MscFrUniDnaHgMIfEntry_Object = MibTableRow
mscFrUniDnaHgMIfEntry = _MscFrUniDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 10, 1)
)
mscFrUniDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMIfEntry.setStatus("mandatory")


class _MscFrUniDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type mscFrUniDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 16777216),
    )


_MscFrUniDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_MscFrUniDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
mscFrUniDnaHgMAvailabilityUpdateThreshold = _MscFrUniDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 10, 1, 1),
    _MscFrUniDnaHgMAvailabilityUpdateThreshold_Type()
)
mscFrUniDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_MscFrUniDnaHgMOpTable_Object = MibTable
mscFrUniDnaHgMOpTable = _MscFrUniDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMOpTable.setStatus("mandatory")
_MscFrUniDnaHgMOpEntry_Object = MibTableRow
mscFrUniDnaHgMOpEntry = _MscFrUniDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 11, 1)
)
mscFrUniDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaHgMOpEntry.setStatus("mandatory")


class _MscFrUniDnaHgMMaximumAvailableAggregateCir_Type(Unsigned32):
    """Custom type mscFrUniDnaHgMMaximumAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDnaHgMMaximumAvailableAggregateCir_Type.__name__ = "Unsigned32"
_MscFrUniDnaHgMMaximumAvailableAggregateCir_Object = MibTableColumn
mscFrUniDnaHgMMaximumAvailableAggregateCir = _MscFrUniDnaHgMMaximumAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 11, 1, 1),
    _MscFrUniDnaHgMMaximumAvailableAggregateCir_Type()
)
mscFrUniDnaHgMMaximumAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMMaximumAvailableAggregateCir.setStatus("mandatory")


class _MscFrUniDnaHgMAvailableAggregateCir_Type(Unsigned32):
    """Custom type mscFrUniDnaHgMAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDnaHgMAvailableAggregateCir_Type.__name__ = "Unsigned32"
_MscFrUniDnaHgMAvailableAggregateCir_Object = MibTableColumn
mscFrUniDnaHgMAvailableAggregateCir = _MscFrUniDnaHgMAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 11, 1, 2),
    _MscFrUniDnaHgMAvailableAggregateCir_Type()
)
mscFrUniDnaHgMAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMAvailableAggregateCir.setStatus("mandatory")


class _MscFrUniDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type mscFrUniDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16777216, 16777215),
    )


_MscFrUniDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_MscFrUniDnaHgMAvailabilityDelta_Object = MibTableColumn
mscFrUniDnaHgMAvailabilityDelta = _MscFrUniDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 11, 1, 3),
    _MscFrUniDnaHgMAvailabilityDelta_Type()
)
mscFrUniDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMAvailabilityDelta.setStatus("mandatory")


class _MscFrUniDnaHgMAvailableDlcis_Type(Unsigned32):
    """Custom type mscFrUniDnaHgMAvailableDlcis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscFrUniDnaHgMAvailableDlcis_Type.__name__ = "Unsigned32"
_MscFrUniDnaHgMAvailableDlcis_Object = MibTableColumn
mscFrUniDnaHgMAvailableDlcis = _MscFrUniDnaHgMAvailableDlcis_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 3, 11, 1, 5),
    _MscFrUniDnaHgMAvailableDlcis_Type()
)
mscFrUniDnaHgMAvailableDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDnaHgMAvailableDlcis.setStatus("mandatory")
_MscFrUniDnaAddressTable_Object = MibTable
mscFrUniDnaAddressTable = _MscFrUniDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDnaAddressTable.setStatus("mandatory")
_MscFrUniDnaAddressEntry_Object = MibTableRow
mscFrUniDnaAddressEntry = _MscFrUniDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 10, 1)
)
mscFrUniDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaAddressEntry.setStatus("mandatory")


class _MscFrUniDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscFrUniDnaNumberingPlanIndicator based on Integer32"""
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


_MscFrUniDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscFrUniDnaNumberingPlanIndicator_Object = MibTableColumn
mscFrUniDnaNumberingPlanIndicator = _MscFrUniDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 10, 1, 1),
    _MscFrUniDnaNumberingPlanIndicator_Type()
)
mscFrUniDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscFrUniDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscFrUniDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrUniDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscFrUniDnaDataNetworkAddress_Object = MibTableColumn
mscFrUniDnaDataNetworkAddress = _MscFrUniDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 10, 1, 2),
    _MscFrUniDnaDataNetworkAddress_Type()
)
mscFrUniDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaDataNetworkAddress.setStatus("mandatory")
_MscFrUniDnaOutgoingOptionsTable_Object = MibTable
mscFrUniDnaOutgoingOptionsTable = _MscFrUniDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrUniDnaOutgoingOptionsTable.setStatus("mandatory")
_MscFrUniDnaOutgoingOptionsEntry_Object = MibTableRow
mscFrUniDnaOutgoingOptionsEntry = _MscFrUniDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1)
)
mscFrUniDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscFrUniDnaOutDefaultPriority_Type(Integer32):
    """Custom type mscFrUniDnaOutDefaultPriority based on Integer32"""
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


_MscFrUniDnaOutDefaultPriority_Type.__name__ = "Integer32"
_MscFrUniDnaOutDefaultPriority_Object = MibTableColumn
mscFrUniDnaOutDefaultPriority = _MscFrUniDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1, 7),
    _MscFrUniDnaOutDefaultPriority_Type()
)
mscFrUniDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaOutDefaultPriority.setStatus("mandatory")


class _MscFrUniDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type mscFrUniDnaOutDefaultPathSensitivity based on Integer32"""
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


_MscFrUniDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_MscFrUniDnaOutDefaultPathSensitivity_Object = MibTableColumn
mscFrUniDnaOutDefaultPathSensitivity = _MscFrUniDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1, 11),
    _MscFrUniDnaOutDefaultPathSensitivity_Type()
)
mscFrUniDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _MscFrUniDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type mscFrUniDnaOutPathSensitivityOverRide based on Integer32"""
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


_MscFrUniDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_MscFrUniDnaOutPathSensitivityOverRide_Object = MibTableColumn
mscFrUniDnaOutPathSensitivityOverRide = _MscFrUniDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1, 12),
    _MscFrUniDnaOutPathSensitivityOverRide_Type()
)
mscFrUniDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _MscFrUniDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type mscFrUniDnaOutDefaultPathReliability based on Integer32"""
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


_MscFrUniDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_MscFrUniDnaOutDefaultPathReliability_Object = MibTableColumn
mscFrUniDnaOutDefaultPathReliability = _MscFrUniDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1, 14),
    _MscFrUniDnaOutDefaultPathReliability_Type()
)
mscFrUniDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaOutDefaultPathReliability.setStatus("mandatory")


class _MscFrUniDnaOutAccess_Type(Integer32):
    """Custom type mscFrUniDnaOutAccess based on Integer32"""
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


_MscFrUniDnaOutAccess_Type.__name__ = "Integer32"
_MscFrUniDnaOutAccess_Object = MibTableColumn
mscFrUniDnaOutAccess = _MscFrUniDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1, 17),
    _MscFrUniDnaOutAccess_Type()
)
mscFrUniDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaOutAccess.setStatus("mandatory")


class _MscFrUniDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mscFrUniDnaDefaultTransferPriority based on Integer32"""
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


_MscFrUniDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MscFrUniDnaDefaultTransferPriority_Object = MibTableColumn
mscFrUniDnaDefaultTransferPriority = _MscFrUniDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1, 18),
    _MscFrUniDnaDefaultTransferPriority_Type()
)
mscFrUniDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaDefaultTransferPriority.setStatus("mandatory")


class _MscFrUniDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type mscFrUniDnaTransferPriorityOverRide based on Integer32"""
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


_MscFrUniDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_MscFrUniDnaTransferPriorityOverRide_Object = MibTableColumn
mscFrUniDnaTransferPriorityOverRide = _MscFrUniDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 11, 1, 19),
    _MscFrUniDnaTransferPriorityOverRide_Type()
)
mscFrUniDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaTransferPriorityOverRide.setStatus("mandatory")
_MscFrUniDnaIncomingOptionsTable_Object = MibTable
mscFrUniDnaIncomingOptionsTable = _MscFrUniDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrUniDnaIncomingOptionsTable.setStatus("mandatory")
_MscFrUniDnaIncomingOptionsEntry_Object = MibTableRow
mscFrUniDnaIncomingOptionsEntry = _MscFrUniDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 12, 1)
)
mscFrUniDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscFrUniDnaIncAccess_Type(Integer32):
    """Custom type mscFrUniDnaIncAccess based on Integer32"""
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


_MscFrUniDnaIncAccess_Type.__name__ = "Integer32"
_MscFrUniDnaIncAccess_Object = MibTableColumn
mscFrUniDnaIncAccess = _MscFrUniDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 12, 1, 9),
    _MscFrUniDnaIncAccess_Type()
)
mscFrUniDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaIncAccess.setStatus("mandatory")
_MscFrUniDnaCallOptionsTable_Object = MibTable
mscFrUniDnaCallOptionsTable = _MscFrUniDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrUniDnaCallOptionsTable.setStatus("mandatory")
_MscFrUniDnaCallOptionsEntry_Object = MibTableRow
mscFrUniDnaCallOptionsEntry = _MscFrUniDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 13, 1)
)
mscFrUniDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDnaCallOptionsEntry.setStatus("mandatory")


class _MscFrUniDnaAccountClass_Type(Unsigned32):
    """Custom type mscFrUniDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniDnaAccountClass_Type.__name__ = "Unsigned32"
_MscFrUniDnaAccountClass_Object = MibTableColumn
mscFrUniDnaAccountClass = _MscFrUniDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 13, 1, 10),
    _MscFrUniDnaAccountClass_Type()
)
mscFrUniDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaAccountClass.setStatus("mandatory")


class _MscFrUniDnaAccountCollection_Type(OctetString):
    """Custom type mscFrUniDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniDnaAccountCollection_Type.__name__ = "OctetString"
_MscFrUniDnaAccountCollection_Object = MibTableColumn
mscFrUniDnaAccountCollection = _MscFrUniDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 13, 1, 11),
    _MscFrUniDnaAccountCollection_Type()
)
mscFrUniDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaAccountCollection.setStatus("mandatory")


class _MscFrUniDnaServiceExchange_Type(Unsigned32):
    """Custom type mscFrUniDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniDnaServiceExchange_Type.__name__ = "Unsigned32"
_MscFrUniDnaServiceExchange_Object = MibTableColumn
mscFrUniDnaServiceExchange = _MscFrUniDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 13, 1, 12),
    _MscFrUniDnaServiceExchange_Type()
)
mscFrUniDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaServiceExchange.setStatus("mandatory")


class _MscFrUniDnaEgressAccounting_Type(Integer32):
    """Custom type mscFrUniDnaEgressAccounting based on Integer32"""
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


_MscFrUniDnaEgressAccounting_Type.__name__ = "Integer32"
_MscFrUniDnaEgressAccounting_Object = MibTableColumn
mscFrUniDnaEgressAccounting = _MscFrUniDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 13, 1, 13),
    _MscFrUniDnaEgressAccounting_Type()
)
mscFrUniDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaEgressAccounting.setStatus("mandatory")


class _MscFrUniDnaDataPath_Type(Integer32):
    """Custom type mscFrUniDnaDataPath based on Integer32"""
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


_MscFrUniDnaDataPath_Type.__name__ = "Integer32"
_MscFrUniDnaDataPath_Object = MibTableColumn
mscFrUniDnaDataPath = _MscFrUniDnaDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 2, 13, 1, 21),
    _MscFrUniDnaDataPath_Type()
)
mscFrUniDnaDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDnaDataPath.setStatus("mandatory")
_MscFrUniFramer_ObjectIdentity = ObjectIdentity
mscFrUniFramer = _MscFrUniFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3)
)
_MscFrUniFramerRowStatusTable_Object = MibTable
mscFrUniFramerRowStatusTable = _MscFrUniFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrUniFramerRowStatusTable.setStatus("mandatory")
_MscFrUniFramerRowStatusEntry_Object = MibTableRow
mscFrUniFramerRowStatusEntry = _MscFrUniFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 1, 1)
)
mscFrUniFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniFramerRowStatusEntry.setStatus("mandatory")
_MscFrUniFramerRowStatus_Type = RowStatus
_MscFrUniFramerRowStatus_Object = MibTableColumn
mscFrUniFramerRowStatus = _MscFrUniFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 1, 1, 1),
    _MscFrUniFramerRowStatus_Type()
)
mscFrUniFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniFramerRowStatus.setStatus("mandatory")
_MscFrUniFramerComponentName_Type = DisplayString
_MscFrUniFramerComponentName_Object = MibTableColumn
mscFrUniFramerComponentName = _MscFrUniFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 1, 1, 2),
    _MscFrUniFramerComponentName_Type()
)
mscFrUniFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerComponentName.setStatus("mandatory")
_MscFrUniFramerStorageType_Type = StorageType
_MscFrUniFramerStorageType_Object = MibTableColumn
mscFrUniFramerStorageType = _MscFrUniFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 1, 1, 4),
    _MscFrUniFramerStorageType_Type()
)
mscFrUniFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerStorageType.setStatus("mandatory")
_MscFrUniFramerIndex_Type = NonReplicated
_MscFrUniFramerIndex_Object = MibTableColumn
mscFrUniFramerIndex = _MscFrUniFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 1, 1, 10),
    _MscFrUniFramerIndex_Type()
)
mscFrUniFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniFramerIndex.setStatus("mandatory")
_MscFrUniFramerProvTable_Object = MibTable
mscFrUniFramerProvTable = _MscFrUniFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrUniFramerProvTable.setStatus("mandatory")
_MscFrUniFramerProvEntry_Object = MibTableRow
mscFrUniFramerProvEntry = _MscFrUniFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 10, 1)
)
mscFrUniFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniFramerProvEntry.setStatus("mandatory")
_MscFrUniFramerInterfaceName_Type = Link
_MscFrUniFramerInterfaceName_Object = MibTableColumn
mscFrUniFramerInterfaceName = _MscFrUniFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 10, 1, 1),
    _MscFrUniFramerInterfaceName_Type()
)
mscFrUniFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniFramerInterfaceName.setStatus("mandatory")
_MscFrUniFramerLinkTable_Object = MibTable
mscFrUniFramerLinkTable = _MscFrUniFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrUniFramerLinkTable.setStatus("mandatory")
_MscFrUniFramerLinkEntry_Object = MibTableRow
mscFrUniFramerLinkEntry = _MscFrUniFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 11, 1)
)
mscFrUniFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniFramerLinkEntry.setStatus("mandatory")


class _MscFrUniFramerDataInversion_Type(Integer32):
    """Custom type mscFrUniFramerDataInversion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 16))
    )


_MscFrUniFramerDataInversion_Type.__name__ = "Integer32"
_MscFrUniFramerDataInversion_Object = MibTableColumn
mscFrUniFramerDataInversion = _MscFrUniFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 11, 1, 2),
    _MscFrUniFramerDataInversion_Type()
)
mscFrUniFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniFramerDataInversion.setStatus("mandatory")


class _MscFrUniFramerFrameCrcType_Type(Integer32):
    """Custom type mscFrUniFramerFrameCrcType based on Integer32"""
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
        *(("crc16", 0),
          ("crc32", 1),
          ("noCrc", 2))
    )


_MscFrUniFramerFrameCrcType_Type.__name__ = "Integer32"
_MscFrUniFramerFrameCrcType_Object = MibTableColumn
mscFrUniFramerFrameCrcType = _MscFrUniFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 11, 1, 3),
    _MscFrUniFramerFrameCrcType_Type()
)
mscFrUniFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniFramerFrameCrcType.setStatus("mandatory")


class _MscFrUniFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscFrUniFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscFrUniFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscFrUniFramerFlagsBetweenFrames_Object = MibTableColumn
mscFrUniFramerFlagsBetweenFrames = _MscFrUniFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 11, 1, 4),
    _MscFrUniFramerFlagsBetweenFrames_Type()
)
mscFrUniFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniFramerFlagsBetweenFrames.setStatus("mandatory")
_MscFrUniFramerStateTable_Object = MibTable
mscFrUniFramerStateTable = _MscFrUniFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 12)
)
if mibBuilder.loadTexts:
    mscFrUniFramerStateTable.setStatus("mandatory")
_MscFrUniFramerStateEntry_Object = MibTableRow
mscFrUniFramerStateEntry = _MscFrUniFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 12, 1)
)
mscFrUniFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniFramerStateEntry.setStatus("mandatory")


class _MscFrUniFramerAdminState_Type(Integer32):
    """Custom type mscFrUniFramerAdminState based on Integer32"""
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


_MscFrUniFramerAdminState_Type.__name__ = "Integer32"
_MscFrUniFramerAdminState_Object = MibTableColumn
mscFrUniFramerAdminState = _MscFrUniFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 12, 1, 1),
    _MscFrUniFramerAdminState_Type()
)
mscFrUniFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerAdminState.setStatus("mandatory")


class _MscFrUniFramerOperationalState_Type(Integer32):
    """Custom type mscFrUniFramerOperationalState based on Integer32"""
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


_MscFrUniFramerOperationalState_Type.__name__ = "Integer32"
_MscFrUniFramerOperationalState_Object = MibTableColumn
mscFrUniFramerOperationalState = _MscFrUniFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 12, 1, 2),
    _MscFrUniFramerOperationalState_Type()
)
mscFrUniFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerOperationalState.setStatus("mandatory")


class _MscFrUniFramerUsageState_Type(Integer32):
    """Custom type mscFrUniFramerUsageState based on Integer32"""
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


_MscFrUniFramerUsageState_Type.__name__ = "Integer32"
_MscFrUniFramerUsageState_Object = MibTableColumn
mscFrUniFramerUsageState = _MscFrUniFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 12, 1, 3),
    _MscFrUniFramerUsageState_Type()
)
mscFrUniFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerUsageState.setStatus("mandatory")
_MscFrUniFramerStatsTable_Object = MibTable
mscFrUniFramerStatsTable = _MscFrUniFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13)
)
if mibBuilder.loadTexts:
    mscFrUniFramerStatsTable.setStatus("mandatory")
_MscFrUniFramerStatsEntry_Object = MibTableRow
mscFrUniFramerStatsEntry = _MscFrUniFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1)
)
mscFrUniFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniFramerStatsEntry.setStatus("mandatory")
_MscFrUniFramerFrmToIf_Type = Counter32
_MscFrUniFramerFrmToIf_Object = MibTableColumn
mscFrUniFramerFrmToIf = _MscFrUniFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 1),
    _MscFrUniFramerFrmToIf_Type()
)
mscFrUniFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerFrmToIf.setStatus("obsolete")
_MscFrUniFramerFrmFromIf_Type = Counter32
_MscFrUniFramerFrmFromIf_Object = MibTableColumn
mscFrUniFramerFrmFromIf = _MscFrUniFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 2),
    _MscFrUniFramerFrmFromIf_Type()
)
mscFrUniFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerFrmFromIf.setStatus("obsolete")
_MscFrUniFramerOctetFromIf_Type = Counter32
_MscFrUniFramerOctetFromIf_Object = MibTableColumn
mscFrUniFramerOctetFromIf = _MscFrUniFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 3),
    _MscFrUniFramerOctetFromIf_Type()
)
mscFrUniFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerOctetFromIf.setStatus("obsolete")
_MscFrUniFramerAborts_Type = Counter32
_MscFrUniFramerAborts_Object = MibTableColumn
mscFrUniFramerAborts = _MscFrUniFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 4),
    _MscFrUniFramerAborts_Type()
)
mscFrUniFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerAborts.setStatus("mandatory")
_MscFrUniFramerCrcErrors_Type = Counter32
_MscFrUniFramerCrcErrors_Object = MibTableColumn
mscFrUniFramerCrcErrors = _MscFrUniFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 5),
    _MscFrUniFramerCrcErrors_Type()
)
mscFrUniFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerCrcErrors.setStatus("mandatory")
_MscFrUniFramerLrcErrors_Type = Counter32
_MscFrUniFramerLrcErrors_Object = MibTableColumn
mscFrUniFramerLrcErrors = _MscFrUniFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 6),
    _MscFrUniFramerLrcErrors_Type()
)
mscFrUniFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerLrcErrors.setStatus("mandatory")
_MscFrUniFramerNonOctetErrors_Type = Counter32
_MscFrUniFramerNonOctetErrors_Object = MibTableColumn
mscFrUniFramerNonOctetErrors = _MscFrUniFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 7),
    _MscFrUniFramerNonOctetErrors_Type()
)
mscFrUniFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerNonOctetErrors.setStatus("mandatory")
_MscFrUniFramerOverruns_Type = Counter32
_MscFrUniFramerOverruns_Object = MibTableColumn
mscFrUniFramerOverruns = _MscFrUniFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 8),
    _MscFrUniFramerOverruns_Type()
)
mscFrUniFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerOverruns.setStatus("mandatory")
_MscFrUniFramerUnderruns_Type = Counter32
_MscFrUniFramerUnderruns_Object = MibTableColumn
mscFrUniFramerUnderruns = _MscFrUniFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 9),
    _MscFrUniFramerUnderruns_Type()
)
mscFrUniFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerUnderruns.setStatus("mandatory")
_MscFrUniFramerLargeFrmErrors_Type = Counter32
_MscFrUniFramerLargeFrmErrors_Object = MibTableColumn
mscFrUniFramerLargeFrmErrors = _MscFrUniFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 10),
    _MscFrUniFramerLargeFrmErrors_Type()
)
mscFrUniFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerLargeFrmErrors.setStatus("mandatory")
_MscFrUniFramerFrmModeErrors_Type = Counter32
_MscFrUniFramerFrmModeErrors_Object = MibTableColumn
mscFrUniFramerFrmModeErrors = _MscFrUniFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 11),
    _MscFrUniFramerFrmModeErrors_Type()
)
mscFrUniFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerFrmModeErrors.setStatus("mandatory")
_MscFrUniFramerFrmToIf64_Type = PassportCounter64
_MscFrUniFramerFrmToIf64_Object = MibTableColumn
mscFrUniFramerFrmToIf64 = _MscFrUniFramerFrmToIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 14),
    _MscFrUniFramerFrmToIf64_Type()
)
mscFrUniFramerFrmToIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerFrmToIf64.setStatus("mandatory")
_MscFrUniFramerFrmFromIf64_Type = PassportCounter64
_MscFrUniFramerFrmFromIf64_Object = MibTableColumn
mscFrUniFramerFrmFromIf64 = _MscFrUniFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 15),
    _MscFrUniFramerFrmFromIf64_Type()
)
mscFrUniFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerFrmFromIf64.setStatus("mandatory")
_MscFrUniFramerOctetFromIf64_Type = PassportCounter64
_MscFrUniFramerOctetFromIf64_Object = MibTableColumn
mscFrUniFramerOctetFromIf64 = _MscFrUniFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 13, 1, 16),
    _MscFrUniFramerOctetFromIf64_Type()
)
mscFrUniFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerOctetFromIf64.setStatus("mandatory")
_MscFrUniFramerUtilTable_Object = MibTable
mscFrUniFramerUtilTable = _MscFrUniFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 14)
)
if mibBuilder.loadTexts:
    mscFrUniFramerUtilTable.setStatus("mandatory")
_MscFrUniFramerUtilEntry_Object = MibTableRow
mscFrUniFramerUtilEntry = _MscFrUniFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 14, 1)
)
mscFrUniFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniFramerUtilEntry.setStatus("mandatory")


class _MscFrUniFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscFrUniFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrUniFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscFrUniFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscFrUniFramerNormPrioLinkUtilToIf = _MscFrUniFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 14, 1, 1),
    _MscFrUniFramerNormPrioLinkUtilToIf_Type()
)
mscFrUniFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscFrUniFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscFrUniFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrUniFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscFrUniFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscFrUniFramerNormPrioLinkUtilFromIf = _MscFrUniFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 3, 14, 1, 3),
    _MscFrUniFramerNormPrioLinkUtilFromIf_Type()
)
mscFrUniFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscFrUniLmi_ObjectIdentity = ObjectIdentity
mscFrUniLmi = _MscFrUniLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4)
)
_MscFrUniLmiRowStatusTable_Object = MibTable
mscFrUniLmiRowStatusTable = _MscFrUniLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrUniLmiRowStatusTable.setStatus("mandatory")
_MscFrUniLmiRowStatusEntry_Object = MibTableRow
mscFrUniLmiRowStatusEntry = _MscFrUniLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 1, 1)
)
mscFrUniLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLmiRowStatusEntry.setStatus("mandatory")
_MscFrUniLmiRowStatus_Type = RowStatus
_MscFrUniLmiRowStatus_Object = MibTableColumn
mscFrUniLmiRowStatus = _MscFrUniLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 1, 1, 1),
    _MscFrUniLmiRowStatus_Type()
)
mscFrUniLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiRowStatus.setStatus("mandatory")
_MscFrUniLmiComponentName_Type = DisplayString
_MscFrUniLmiComponentName_Object = MibTableColumn
mscFrUniLmiComponentName = _MscFrUniLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 1, 1, 2),
    _MscFrUniLmiComponentName_Type()
)
mscFrUniLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiComponentName.setStatus("mandatory")
_MscFrUniLmiStorageType_Type = StorageType
_MscFrUniLmiStorageType_Object = MibTableColumn
mscFrUniLmiStorageType = _MscFrUniLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 1, 1, 4),
    _MscFrUniLmiStorageType_Type()
)
mscFrUniLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiStorageType.setStatus("mandatory")
_MscFrUniLmiIndex_Type = NonReplicated
_MscFrUniLmiIndex_Object = MibTableColumn
mscFrUniLmiIndex = _MscFrUniLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 1, 1, 10),
    _MscFrUniLmiIndex_Type()
)
mscFrUniLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniLmiIndex.setStatus("mandatory")
_MscFrUniLmiParmsTable_Object = MibTable
mscFrUniLmiParmsTable = _MscFrUniLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrUniLmiParmsTable.setStatus("mandatory")
_MscFrUniLmiParmsEntry_Object = MibTableRow
mscFrUniLmiParmsEntry = _MscFrUniLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1)
)
mscFrUniLmiParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLmiParmsEntry.setStatus("mandatory")


class _MscFrUniLmiProcedures_Type(Integer32):
    """Custom type mscFrUniLmiProcedures based on Integer32"""
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


_MscFrUniLmiProcedures_Type.__name__ = "Integer32"
_MscFrUniLmiProcedures_Object = MibTableColumn
mscFrUniLmiProcedures = _MscFrUniLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 1),
    _MscFrUniLmiProcedures_Type()
)
mscFrUniLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiProcedures.setStatus("mandatory")


class _MscFrUniLmiAsyncStatusReport_Type(Integer32):
    """Custom type mscFrUniLmiAsyncStatusReport based on Integer32"""
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


_MscFrUniLmiAsyncStatusReport_Type.__name__ = "Integer32"
_MscFrUniLmiAsyncStatusReport_Object = MibTableColumn
mscFrUniLmiAsyncStatusReport = _MscFrUniLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 2),
    _MscFrUniLmiAsyncStatusReport_Type()
)
mscFrUniLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiAsyncStatusReport.setStatus("mandatory")


class _MscFrUniLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type mscFrUniLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrUniLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_MscFrUniLmiErrorEventThreshold_Object = MibTableColumn
mscFrUniLmiErrorEventThreshold = _MscFrUniLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 3),
    _MscFrUniLmiErrorEventThreshold_Type()
)
mscFrUniLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiErrorEventThreshold.setStatus("mandatory")


class _MscFrUniLmiEventCount_Type(Unsigned32):
    """Custom type mscFrUniLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrUniLmiEventCount_Type.__name__ = "Unsigned32"
_MscFrUniLmiEventCount_Object = MibTableColumn
mscFrUniLmiEventCount = _MscFrUniLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 4),
    _MscFrUniLmiEventCount_Type()
)
mscFrUniLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiEventCount.setStatus("mandatory")


class _MscFrUniLmiCheckPointTimer_Type(Unsigned32):
    """Custom type mscFrUniLmiCheckPointTimer based on Unsigned32"""
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


_MscFrUniLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_MscFrUniLmiCheckPointTimer_Object = MibTableColumn
mscFrUniLmiCheckPointTimer = _MscFrUniLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 5),
    _MscFrUniLmiCheckPointTimer_Type()
)
mscFrUniLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiCheckPointTimer.setStatus("mandatory")


class _MscFrUniLmiMessageCountTimer_Type(Unsigned32):
    """Custom type mscFrUniLmiMessageCountTimer based on Unsigned32"""
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


_MscFrUniLmiMessageCountTimer_Type.__name__ = "Unsigned32"
_MscFrUniLmiMessageCountTimer_Object = MibTableColumn
mscFrUniLmiMessageCountTimer = _MscFrUniLmiMessageCountTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 6),
    _MscFrUniLmiMessageCountTimer_Type()
)
mscFrUniLmiMessageCountTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiMessageCountTimer.setStatus("mandatory")


class _MscFrUniLmiIgnoreActiveBit_Type(Integer32):
    """Custom type mscFrUniLmiIgnoreActiveBit based on Integer32"""
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


_MscFrUniLmiIgnoreActiveBit_Type.__name__ = "Integer32"
_MscFrUniLmiIgnoreActiveBit_Object = MibTableColumn
mscFrUniLmiIgnoreActiveBit = _MscFrUniLmiIgnoreActiveBit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 7),
    _MscFrUniLmiIgnoreActiveBit_Type()
)
mscFrUniLmiIgnoreActiveBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiIgnoreActiveBit.setStatus("mandatory")


class _MscFrUniLmiSide_Type(Integer32):
    """Custom type mscFrUniLmiSide based on Integer32"""
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


_MscFrUniLmiSide_Type.__name__ = "Integer32"
_MscFrUniLmiSide_Object = MibTableColumn
mscFrUniLmiSide = _MscFrUniLmiSide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 8),
    _MscFrUniLmiSide_Type()
)
mscFrUniLmiSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiSide.setStatus("mandatory")


class _MscFrUniLmiPvcConfigParmsInFsr_Type(Integer32):
    """Custom type mscFrUniLmiPvcConfigParmsInFsr based on Integer32"""
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


_MscFrUniLmiPvcConfigParmsInFsr_Type.__name__ = "Integer32"
_MscFrUniLmiPvcConfigParmsInFsr_Object = MibTableColumn
mscFrUniLmiPvcConfigParmsInFsr = _MscFrUniLmiPvcConfigParmsInFsr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 10, 1, 9),
    _MscFrUniLmiPvcConfigParmsInFsr_Type()
)
mscFrUniLmiPvcConfigParmsInFsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiPvcConfigParmsInFsr.setStatus("mandatory")
_MscFrUniLmiStateTable_Object = MibTable
mscFrUniLmiStateTable = _MscFrUniLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 11)
)
if mibBuilder.loadTexts:
    mscFrUniLmiStateTable.setStatus("mandatory")
_MscFrUniLmiStateEntry_Object = MibTableRow
mscFrUniLmiStateEntry = _MscFrUniLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 11, 1)
)
mscFrUniLmiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLmiStateEntry.setStatus("mandatory")


class _MscFrUniLmiAdminState_Type(Integer32):
    """Custom type mscFrUniLmiAdminState based on Integer32"""
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


_MscFrUniLmiAdminState_Type.__name__ = "Integer32"
_MscFrUniLmiAdminState_Object = MibTableColumn
mscFrUniLmiAdminState = _MscFrUniLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 11, 1, 1),
    _MscFrUniLmiAdminState_Type()
)
mscFrUniLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiAdminState.setStatus("mandatory")


class _MscFrUniLmiOperationalState_Type(Integer32):
    """Custom type mscFrUniLmiOperationalState based on Integer32"""
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


_MscFrUniLmiOperationalState_Type.__name__ = "Integer32"
_MscFrUniLmiOperationalState_Object = MibTableColumn
mscFrUniLmiOperationalState = _MscFrUniLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 11, 1, 2),
    _MscFrUniLmiOperationalState_Type()
)
mscFrUniLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiOperationalState.setStatus("mandatory")


class _MscFrUniLmiUsageState_Type(Integer32):
    """Custom type mscFrUniLmiUsageState based on Integer32"""
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


_MscFrUniLmiUsageState_Type.__name__ = "Integer32"
_MscFrUniLmiUsageState_Object = MibTableColumn
mscFrUniLmiUsageState = _MscFrUniLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 11, 1, 3),
    _MscFrUniLmiUsageState_Type()
)
mscFrUniLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiUsageState.setStatus("mandatory")
_MscFrUniLmiPsiTable_Object = MibTable
mscFrUniLmiPsiTable = _MscFrUniLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 12)
)
if mibBuilder.loadTexts:
    mscFrUniLmiPsiTable.setStatus("mandatory")
_MscFrUniLmiPsiEntry_Object = MibTableRow
mscFrUniLmiPsiEntry = _MscFrUniLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 12, 1)
)
mscFrUniLmiPsiEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLmiPsiEntry.setStatus("mandatory")


class _MscFrUniLmiProtocolStatus_Type(Integer32):
    """Custom type mscFrUniLmiProtocolStatus based on Integer32"""
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


_MscFrUniLmiProtocolStatus_Type.__name__ = "Integer32"
_MscFrUniLmiProtocolStatus_Object = MibTableColumn
mscFrUniLmiProtocolStatus = _MscFrUniLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 12, 1, 1),
    _MscFrUniLmiProtocolStatus_Type()
)
mscFrUniLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiProtocolStatus.setStatus("mandatory")


class _MscFrUniLmiOpProcedures_Type(Integer32):
    """Custom type mscFrUniLmiOpProcedures based on Integer32"""
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


_MscFrUniLmiOpProcedures_Type.__name__ = "Integer32"
_MscFrUniLmiOpProcedures_Object = MibTableColumn
mscFrUniLmiOpProcedures = _MscFrUniLmiOpProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 12, 1, 2),
    _MscFrUniLmiOpProcedures_Type()
)
mscFrUniLmiOpProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiOpProcedures.setStatus("mandatory")
_MscFrUniLmiStatsTable_Object = MibTable
mscFrUniLmiStatsTable = _MscFrUniLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13)
)
if mibBuilder.loadTexts:
    mscFrUniLmiStatsTable.setStatus("mandatory")
_MscFrUniLmiStatsEntry_Object = MibTableRow
mscFrUniLmiStatsEntry = _MscFrUniLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1)
)
mscFrUniLmiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLmiStatsEntry.setStatus("mandatory")
_MscFrUniLmiKeepAliveStatusToIf_Type = Counter32
_MscFrUniLmiKeepAliveStatusToIf_Object = MibTableColumn
mscFrUniLmiKeepAliveStatusToIf = _MscFrUniLmiKeepAliveStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 1),
    _MscFrUniLmiKeepAliveStatusToIf_Type()
)
mscFrUniLmiKeepAliveStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiKeepAliveStatusToIf.setStatus("mandatory")
_MscFrUniLmiFullStatusToIf_Type = Counter32
_MscFrUniLmiFullStatusToIf_Object = MibTableColumn
mscFrUniLmiFullStatusToIf = _MscFrUniLmiFullStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 2),
    _MscFrUniLmiFullStatusToIf_Type()
)
mscFrUniLmiFullStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiFullStatusToIf.setStatus("mandatory")
_MscFrUniLmiKeepAliveStatusEnqFromIf_Type = Counter32
_MscFrUniLmiKeepAliveStatusEnqFromIf_Object = MibTableColumn
mscFrUniLmiKeepAliveStatusEnqFromIf = _MscFrUniLmiKeepAliveStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 3),
    _MscFrUniLmiKeepAliveStatusEnqFromIf_Type()
)
mscFrUniLmiKeepAliveStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiKeepAliveStatusEnqFromIf.setStatus("mandatory")
_MscFrUniLmiFullStatusEnqFromIf_Type = Counter32
_MscFrUniLmiFullStatusEnqFromIf_Object = MibTableColumn
mscFrUniLmiFullStatusEnqFromIf = _MscFrUniLmiFullStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 4),
    _MscFrUniLmiFullStatusEnqFromIf_Type()
)
mscFrUniLmiFullStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiFullStatusEnqFromIf.setStatus("mandatory")


class _MscFrUniLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type mscFrUniLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscFrUniLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_MscFrUniLmiNetworkSideEventHistory_Object = MibTableColumn
mscFrUniLmiNetworkSideEventHistory = _MscFrUniLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 5),
    _MscFrUniLmiNetworkSideEventHistory_Type()
)
mscFrUniLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiNetworkSideEventHistory.setStatus("mandatory")
_MscFrUniLmiProtocolErrors_Type = Counter32
_MscFrUniLmiProtocolErrors_Object = MibTableColumn
mscFrUniLmiProtocolErrors = _MscFrUniLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 6),
    _MscFrUniLmiProtocolErrors_Type()
)
mscFrUniLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiProtocolErrors.setStatus("mandatory")
_MscFrUniLmiUnexpectedIes_Type = Counter32
_MscFrUniLmiUnexpectedIes_Object = MibTableColumn
mscFrUniLmiUnexpectedIes = _MscFrUniLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 7),
    _MscFrUniLmiUnexpectedIes_Type()
)
mscFrUniLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiUnexpectedIes.setStatus("mandatory")
_MscFrUniLmiSequenceErrors_Type = Counter32
_MscFrUniLmiSequenceErrors_Object = MibTableColumn
mscFrUniLmiSequenceErrors = _MscFrUniLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 8),
    _MscFrUniLmiSequenceErrors_Type()
)
mscFrUniLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiSequenceErrors.setStatus("mandatory")
_MscFrUniLmiUnexpectedReports_Type = Counter32
_MscFrUniLmiUnexpectedReports_Object = MibTableColumn
mscFrUniLmiUnexpectedReports = _MscFrUniLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 9),
    _MscFrUniLmiUnexpectedReports_Type()
)
mscFrUniLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiUnexpectedReports.setStatus("mandatory")
_MscFrUniLmiPollingVerifTimeouts_Type = Counter32
_MscFrUniLmiPollingVerifTimeouts_Object = MibTableColumn
mscFrUniLmiPollingVerifTimeouts = _MscFrUniLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 10),
    _MscFrUniLmiPollingVerifTimeouts_Type()
)
mscFrUniLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiPollingVerifTimeouts.setStatus("mandatory")
_MscFrUniLmiKeepAliveEnqToIf_Type = Counter32
_MscFrUniLmiKeepAliveEnqToIf_Object = MibTableColumn
mscFrUniLmiKeepAliveEnqToIf = _MscFrUniLmiKeepAliveEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 11),
    _MscFrUniLmiKeepAliveEnqToIf_Type()
)
mscFrUniLmiKeepAliveEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiKeepAliveEnqToIf.setStatus("mandatory")
_MscFrUniLmiFullStatusEnqToIf_Type = Counter32
_MscFrUniLmiFullStatusEnqToIf_Object = MibTableColumn
mscFrUniLmiFullStatusEnqToIf = _MscFrUniLmiFullStatusEnqToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 12),
    _MscFrUniLmiFullStatusEnqToIf_Type()
)
mscFrUniLmiFullStatusEnqToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiFullStatusEnqToIf.setStatus("mandatory")


class _MscFrUniLmiUserSideEventHistory_Type(AsciiString):
    """Custom type mscFrUniLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscFrUniLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_MscFrUniLmiUserSideEventHistory_Object = MibTableColumn
mscFrUniLmiUserSideEventHistory = _MscFrUniLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 13),
    _MscFrUniLmiUserSideEventHistory_Type()
)
mscFrUniLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiUserSideEventHistory.setStatus("mandatory")
_MscFrUniLmiStatusSequenceErrors_Type = Counter32
_MscFrUniLmiStatusSequenceErrors_Object = MibTableColumn
mscFrUniLmiStatusSequenceErrors = _MscFrUniLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 14),
    _MscFrUniLmiStatusSequenceErrors_Type()
)
mscFrUniLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiStatusSequenceErrors.setStatus("mandatory")
_MscFrUniLmiNoStatusReportCount_Type = Counter32
_MscFrUniLmiNoStatusReportCount_Object = MibTableColumn
mscFrUniLmiNoStatusReportCount = _MscFrUniLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 13, 1, 15),
    _MscFrUniLmiNoStatusReportCount_Type()
)
mscFrUniLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLmiNoStatusReportCount.setStatus("mandatory")
_MscFrUniLmiUspParmsTable_Object = MibTable
mscFrUniLmiUspParmsTable = _MscFrUniLmiUspParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 14)
)
if mibBuilder.loadTexts:
    mscFrUniLmiUspParmsTable.setStatus("mandatory")
_MscFrUniLmiUspParmsEntry_Object = MibTableRow
mscFrUniLmiUspParmsEntry = _MscFrUniLmiUspParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 14, 1)
)
mscFrUniLmiUspParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLmiUspParmsEntry.setStatus("mandatory")


class _MscFrUniLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type mscFrUniLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_MscFrUniLmiFullStatusPollingCycles_Object = MibTableColumn
mscFrUniLmiFullStatusPollingCycles = _MscFrUniLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 14, 1, 1),
    _MscFrUniLmiFullStatusPollingCycles_Type()
)
mscFrUniLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiFullStatusPollingCycles.setStatus("mandatory")


class _MscFrUniLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type mscFrUniLmiLinkVerificationTimer based on Unsigned32"""
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


_MscFrUniLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_MscFrUniLmiLinkVerificationTimer_Object = MibTableColumn
mscFrUniLmiLinkVerificationTimer = _MscFrUniLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 4, 14, 1, 2),
    _MscFrUniLmiLinkVerificationTimer_Type()
)
mscFrUniLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLmiLinkVerificationTimer.setStatus("mandatory")
_MscFrUniDlci_ObjectIdentity = ObjectIdentity
mscFrUniDlci = _MscFrUniDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5)
)
_MscFrUniDlciRowStatusTable_Object = MibTable
mscFrUniDlciRowStatusTable = _MscFrUniDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDlciRowStatusTable.setStatus("mandatory")
_MscFrUniDlciRowStatusEntry_Object = MibTableRow
mscFrUniDlciRowStatusEntry = _MscFrUniDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 1, 1)
)
mscFrUniDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciRowStatusEntry.setStatus("mandatory")
_MscFrUniDlciRowStatus_Type = RowStatus
_MscFrUniDlciRowStatus_Object = MibTableColumn
mscFrUniDlciRowStatus = _MscFrUniDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 1, 1, 1),
    _MscFrUniDlciRowStatus_Type()
)
mscFrUniDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciRowStatus.setStatus("mandatory")
_MscFrUniDlciComponentName_Type = DisplayString
_MscFrUniDlciComponentName_Object = MibTableColumn
mscFrUniDlciComponentName = _MscFrUniDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 1, 1, 2),
    _MscFrUniDlciComponentName_Type()
)
mscFrUniDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciComponentName.setStatus("mandatory")
_MscFrUniDlciStorageType_Type = StorageType
_MscFrUniDlciStorageType_Object = MibTableColumn
mscFrUniDlciStorageType = _MscFrUniDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 1, 1, 4),
    _MscFrUniDlciStorageType_Type()
)
mscFrUniDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciStorageType.setStatus("mandatory")


class _MscFrUniDlciIndex_Type(Integer32):
    """Custom type mscFrUniDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniDlciIndex_Type.__name__ = "Integer32"
_MscFrUniDlciIndex_Object = MibTableColumn
mscFrUniDlciIndex = _MscFrUniDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 1, 1, 10),
    _MscFrUniDlciIndex_Type()
)
mscFrUniDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDlciIndex.setStatus("mandatory")
_MscFrUniDlciDc_ObjectIdentity = ObjectIdentity
mscFrUniDlciDc = _MscFrUniDlciDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2)
)
_MscFrUniDlciDcRowStatusTable_Object = MibTable
mscFrUniDlciDcRowStatusTable = _MscFrUniDlciDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDlciDcRowStatusTable.setStatus("mandatory")
_MscFrUniDlciDcRowStatusEntry_Object = MibTableRow
mscFrUniDlciDcRowStatusEntry = _MscFrUniDlciDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 1, 1)
)
mscFrUniDlciDcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciDcRowStatusEntry.setStatus("mandatory")
_MscFrUniDlciDcRowStatus_Type = RowStatus
_MscFrUniDlciDcRowStatus_Object = MibTableColumn
mscFrUniDlciDcRowStatus = _MscFrUniDlciDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 1, 1, 1),
    _MscFrUniDlciDcRowStatus_Type()
)
mscFrUniDlciDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDcRowStatus.setStatus("mandatory")
_MscFrUniDlciDcComponentName_Type = DisplayString
_MscFrUniDlciDcComponentName_Object = MibTableColumn
mscFrUniDlciDcComponentName = _MscFrUniDlciDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 1, 1, 2),
    _MscFrUniDlciDcComponentName_Type()
)
mscFrUniDlciDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDcComponentName.setStatus("mandatory")
_MscFrUniDlciDcStorageType_Type = StorageType
_MscFrUniDlciDcStorageType_Object = MibTableColumn
mscFrUniDlciDcStorageType = _MscFrUniDlciDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 1, 1, 4),
    _MscFrUniDlciDcStorageType_Type()
)
mscFrUniDlciDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDcStorageType.setStatus("mandatory")
_MscFrUniDlciDcIndex_Type = NonReplicated
_MscFrUniDlciDcIndex_Object = MibTableColumn
mscFrUniDlciDcIndex = _MscFrUniDlciDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 1, 1, 10),
    _MscFrUniDlciDcIndex_Type()
)
mscFrUniDlciDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDlciDcIndex.setStatus("mandatory")
_MscFrUniDlciDcOptionsTable_Object = MibTable
mscFrUniDlciDcOptionsTable = _MscFrUniDlciDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDlciDcOptionsTable.setStatus("mandatory")
_MscFrUniDlciDcOptionsEntry_Object = MibTableRow
mscFrUniDlciDcOptionsEntry = _MscFrUniDlciDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1)
)
mscFrUniDlciDcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciDcOptionsEntry.setStatus("mandatory")


class _MscFrUniDlciDcRemoteNpi_Type(Integer32):
    """Custom type mscFrUniDlciDcRemoteNpi based on Integer32"""
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


_MscFrUniDlciDcRemoteNpi_Type.__name__ = "Integer32"
_MscFrUniDlciDcRemoteNpi_Object = MibTableColumn
mscFrUniDlciDcRemoteNpi = _MscFrUniDlciDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 3),
    _MscFrUniDlciDcRemoteNpi_Type()
)
mscFrUniDlciDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcRemoteNpi.setStatus("mandatory")


class _MscFrUniDlciDcRemoteDna_Type(DigitString):
    """Custom type mscFrUniDlciDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrUniDlciDcRemoteDna_Type.__name__ = "DigitString"
_MscFrUniDlciDcRemoteDna_Object = MibTableColumn
mscFrUniDlciDcRemoteDna = _MscFrUniDlciDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 4),
    _MscFrUniDlciDcRemoteDna_Type()
)
mscFrUniDlciDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcRemoteDna.setStatus("mandatory")


class _MscFrUniDlciDcRemoteDlci_Type(Unsigned32):
    """Custom type mscFrUniDlciDcRemoteDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniDlciDcRemoteDlci_Type.__name__ = "Unsigned32"
_MscFrUniDlciDcRemoteDlci_Object = MibTableColumn
mscFrUniDlciDcRemoteDlci = _MscFrUniDlciDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 5),
    _MscFrUniDlciDcRemoteDlci_Type()
)
mscFrUniDlciDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcRemoteDlci.setStatus("mandatory")


class _MscFrUniDlciDcType_Type(Integer32):
    """Custom type mscFrUniDlciDcType based on Integer32"""
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
          ("spvcSlaveWithBackup", 8))
    )


_MscFrUniDlciDcType_Type.__name__ = "Integer32"
_MscFrUniDlciDcType_Object = MibTableColumn
mscFrUniDlciDcType = _MscFrUniDlciDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 6),
    _MscFrUniDlciDcType_Type()
)
mscFrUniDlciDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcType.setStatus("mandatory")


class _MscFrUniDlciDcTransferPriority_Type(Integer32):
    """Custom type mscFrUniDlciDcTransferPriority based on Integer32"""
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


_MscFrUniDlciDcTransferPriority_Type.__name__ = "Integer32"
_MscFrUniDlciDcTransferPriority_Object = MibTableColumn
mscFrUniDlciDcTransferPriority = _MscFrUniDlciDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 9),
    _MscFrUniDlciDcTransferPriority_Type()
)
mscFrUniDlciDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcTransferPriority.setStatus("mandatory")


class _MscFrUniDlciDcDiscardPriority_Type(Integer32):
    """Custom type mscFrUniDlciDcDiscardPriority based on Integer32"""
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


_MscFrUniDlciDcDiscardPriority_Type.__name__ = "Integer32"
_MscFrUniDlciDcDiscardPriority_Object = MibTableColumn
mscFrUniDlciDcDiscardPriority = _MscFrUniDlciDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 10),
    _MscFrUniDlciDcDiscardPriority_Type()
)
mscFrUniDlciDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcDiscardPriority.setStatus("mandatory")


class _MscFrUniDlciDcDeDiscardPriority_Type(Integer32):
    """Custom type mscFrUniDlciDcDeDiscardPriority based on Integer32"""
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


_MscFrUniDlciDcDeDiscardPriority_Type.__name__ = "Integer32"
_MscFrUniDlciDcDeDiscardPriority_Object = MibTableColumn
mscFrUniDlciDcDeDiscardPriority = _MscFrUniDlciDcDeDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 11),
    _MscFrUniDlciDcDeDiscardPriority_Type()
)
mscFrUniDlciDcDeDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcDeDiscardPriority.setStatus("mandatory")


class _MscFrUniDlciDcDataPath_Type(Integer32):
    """Custom type mscFrUniDlciDcDataPath based on Integer32"""
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


_MscFrUniDlciDcDataPath_Type.__name__ = "Integer32"
_MscFrUniDlciDcDataPath_Object = MibTableColumn
mscFrUniDlciDcDataPath = _MscFrUniDlciDcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 12),
    _MscFrUniDlciDcDataPath_Type()
)
mscFrUniDlciDcDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcDataPath.setStatus("mandatory")


class _MscFrUniDlciDcCugIndex_Type(Unsigned32):
    """Custom type mscFrUniDlciDcCugIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniDlciDcCugIndex_Type.__name__ = "Unsigned32"
_MscFrUniDlciDcCugIndex_Object = MibTableColumn
mscFrUniDlciDcCugIndex = _MscFrUniDlciDcCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 13),
    _MscFrUniDlciDcCugIndex_Type()
)
mscFrUniDlciDcCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcCugIndex.setStatus("mandatory")


class _MscFrUniDlciDcCugType_Type(Integer32):
    """Custom type mscFrUniDlciDcCugType based on Integer32"""
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


_MscFrUniDlciDcCugType_Type.__name__ = "Integer32"
_MscFrUniDlciDcCugType_Object = MibTableColumn
mscFrUniDlciDcCugType = _MscFrUniDlciDcCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 14),
    _MscFrUniDlciDcCugType_Type()
)
mscFrUniDlciDcCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcCugType.setStatus("mandatory")


class _MscFrUniDlciDcMapIpCosToFrQos_Type(Integer32):
    """Custom type mscFrUniDlciDcMapIpCosToFrQos based on Integer32"""
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


_MscFrUniDlciDcMapIpCosToFrQos_Type.__name__ = "Integer32"
_MscFrUniDlciDcMapIpCosToFrQos_Object = MibTableColumn
mscFrUniDlciDcMapIpCosToFrQos = _MscFrUniDlciDcMapIpCosToFrQos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 10, 1, 15),
    _MscFrUniDlciDcMapIpCosToFrQos_Type()
)
mscFrUniDlciDcMapIpCosToFrQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcMapIpCosToFrQos.setStatus("mandatory")
_MscFrUniDlciDcNfaTable_Object = MibTable
mscFrUniDlciDcNfaTable = _MscFrUniDlciDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 202)
)
if mibBuilder.loadTexts:
    mscFrUniDlciDcNfaTable.setStatus("obsolete")
_MscFrUniDlciDcNfaEntry_Object = MibTableRow
mscFrUniDlciDcNfaEntry = _MscFrUniDlciDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 202, 1)
)
mscFrUniDlciDcNfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciDcNfaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciDcNfaEntry.setStatus("obsolete")


class _MscFrUniDlciDcNfaIndex_Type(Integer32):
    """Custom type mscFrUniDlciDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
    )


_MscFrUniDlciDcNfaIndex_Type.__name__ = "Integer32"
_MscFrUniDlciDcNfaIndex_Object = MibTableColumn
mscFrUniDlciDcNfaIndex = _MscFrUniDlciDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 202, 1, 1),
    _MscFrUniDlciDcNfaIndex_Type()
)
mscFrUniDlciDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDlciDcNfaIndex.setStatus("obsolete")


class _MscFrUniDlciDcNfaValue_Type(HexString):
    """Custom type mscFrUniDlciDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscFrUniDlciDcNfaValue_Type.__name__ = "HexString"
_MscFrUniDlciDcNfaValue_Object = MibTableColumn
mscFrUniDlciDcNfaValue = _MscFrUniDlciDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 202, 1, 2),
    _MscFrUniDlciDcNfaValue_Type()
)
mscFrUniDlciDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciDcNfaValue.setStatus("obsolete")
_MscFrUniDlciDcNfaRowStatus_Type = RowStatus
_MscFrUniDlciDcNfaRowStatus_Object = MibTableColumn
mscFrUniDlciDcNfaRowStatus = _MscFrUniDlciDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 2, 202, 1, 3),
    _MscFrUniDlciDcNfaRowStatus_Type()
)
mscFrUniDlciDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDcNfaRowStatus.setStatus("obsolete")
_MscFrUniDlciVc_ObjectIdentity = ObjectIdentity
mscFrUniDlciVc = _MscFrUniDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3)
)
_MscFrUniDlciVcRowStatusTable_Object = MibTable
mscFrUniDlciVcRowStatusTable = _MscFrUniDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcRowStatusTable.setStatus("mandatory")
_MscFrUniDlciVcRowStatusEntry_Object = MibTableRow
mscFrUniDlciVcRowStatusEntry = _MscFrUniDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 1, 1)
)
mscFrUniDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcRowStatusEntry.setStatus("mandatory")
_MscFrUniDlciVcRowStatus_Type = RowStatus
_MscFrUniDlciVcRowStatus_Object = MibTableColumn
mscFrUniDlciVcRowStatus = _MscFrUniDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 1, 1, 1),
    _MscFrUniDlciVcRowStatus_Type()
)
mscFrUniDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcRowStatus.setStatus("mandatory")
_MscFrUniDlciVcComponentName_Type = DisplayString
_MscFrUniDlciVcComponentName_Object = MibTableColumn
mscFrUniDlciVcComponentName = _MscFrUniDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 1, 1, 2),
    _MscFrUniDlciVcComponentName_Type()
)
mscFrUniDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcComponentName.setStatus("mandatory")
_MscFrUniDlciVcStorageType_Type = StorageType
_MscFrUniDlciVcStorageType_Object = MibTableColumn
mscFrUniDlciVcStorageType = _MscFrUniDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 1, 1, 4),
    _MscFrUniDlciVcStorageType_Type()
)
mscFrUniDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcStorageType.setStatus("mandatory")
_MscFrUniDlciVcIndex_Type = NonReplicated
_MscFrUniDlciVcIndex_Object = MibTableColumn
mscFrUniDlciVcIndex = _MscFrUniDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 1, 1, 10),
    _MscFrUniDlciVcIndex_Type()
)
mscFrUniDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDlciVcIndex.setStatus("mandatory")
_MscFrUniDlciVcCadTable_Object = MibTable
mscFrUniDlciVcCadTable = _MscFrUniDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcCadTable.setStatus("mandatory")
_MscFrUniDlciVcCadEntry_Object = MibTableRow
mscFrUniDlciVcCadEntry = _MscFrUniDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1)
)
mscFrUniDlciVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcCadEntry.setStatus("mandatory")


class _MscFrUniDlciVcType_Type(Integer32):
    """Custom type mscFrUniDlciVcType based on Integer32"""
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


_MscFrUniDlciVcType_Type.__name__ = "Integer32"
_MscFrUniDlciVcType_Object = MibTableColumn
mscFrUniDlciVcType = _MscFrUniDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 1),
    _MscFrUniDlciVcType_Type()
)
mscFrUniDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcType.setStatus("mandatory")


class _MscFrUniDlciVcState_Type(Integer32):
    """Custom type mscFrUniDlciVcState based on Integer32"""
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


_MscFrUniDlciVcState_Type.__name__ = "Integer32"
_MscFrUniDlciVcState_Object = MibTableColumn
mscFrUniDlciVcState = _MscFrUniDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 2),
    _MscFrUniDlciVcState_Type()
)
mscFrUniDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcState.setStatus("mandatory")


class _MscFrUniDlciVcPreviousState_Type(Integer32):
    """Custom type mscFrUniDlciVcPreviousState based on Integer32"""
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


_MscFrUniDlciVcPreviousState_Type.__name__ = "Integer32"
_MscFrUniDlciVcPreviousState_Object = MibTableColumn
mscFrUniDlciVcPreviousState = _MscFrUniDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 3),
    _MscFrUniDlciVcPreviousState_Type()
)
mscFrUniDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPreviousState.setStatus("mandatory")


class _MscFrUniDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscFrUniDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcDiagnosticCode_Object = MibTableColumn
mscFrUniDlciVcDiagnosticCode = _MscFrUniDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 4),
    _MscFrUniDlciVcDiagnosticCode_Type()
)
mscFrUniDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcDiagnosticCode.setStatus("mandatory")


class _MscFrUniDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscFrUniDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcPreviousDiagnosticCode_Object = MibTableColumn
mscFrUniDlciVcPreviousDiagnosticCode = _MscFrUniDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 5),
    _MscFrUniDlciVcPreviousDiagnosticCode_Type()
)
mscFrUniDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscFrUniDlciVcCalledNpi_Type(Integer32):
    """Custom type mscFrUniDlciVcCalledNpi based on Integer32"""
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


_MscFrUniDlciVcCalledNpi_Type.__name__ = "Integer32"
_MscFrUniDlciVcCalledNpi_Object = MibTableColumn
mscFrUniDlciVcCalledNpi = _MscFrUniDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 6),
    _MscFrUniDlciVcCalledNpi_Type()
)
mscFrUniDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCalledNpi.setStatus("mandatory")


class _MscFrUniDlciVcCalledDna_Type(DigitString):
    """Custom type mscFrUniDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrUniDlciVcCalledDna_Type.__name__ = "DigitString"
_MscFrUniDlciVcCalledDna_Object = MibTableColumn
mscFrUniDlciVcCalledDna = _MscFrUniDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 7),
    _MscFrUniDlciVcCalledDna_Type()
)
mscFrUniDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCalledDna.setStatus("mandatory")


class _MscFrUniDlciVcCalledLcn_Type(Unsigned32):
    """Custom type mscFrUniDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrUniDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcCalledLcn_Object = MibTableColumn
mscFrUniDlciVcCalledLcn = _MscFrUniDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 8),
    _MscFrUniDlciVcCalledLcn_Type()
)
mscFrUniDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCalledLcn.setStatus("mandatory")


class _MscFrUniDlciVcCallingNpi_Type(Integer32):
    """Custom type mscFrUniDlciVcCallingNpi based on Integer32"""
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


_MscFrUniDlciVcCallingNpi_Type.__name__ = "Integer32"
_MscFrUniDlciVcCallingNpi_Object = MibTableColumn
mscFrUniDlciVcCallingNpi = _MscFrUniDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 9),
    _MscFrUniDlciVcCallingNpi_Type()
)
mscFrUniDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCallingNpi.setStatus("mandatory")


class _MscFrUniDlciVcCallingDna_Type(DigitString):
    """Custom type mscFrUniDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrUniDlciVcCallingDna_Type.__name__ = "DigitString"
_MscFrUniDlciVcCallingDna_Object = MibTableColumn
mscFrUniDlciVcCallingDna = _MscFrUniDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 10),
    _MscFrUniDlciVcCallingDna_Type()
)
mscFrUniDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCallingDna.setStatus("mandatory")


class _MscFrUniDlciVcCallingLcn_Type(Unsigned32):
    """Custom type mscFrUniDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrUniDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcCallingLcn_Object = MibTableColumn
mscFrUniDlciVcCallingLcn = _MscFrUniDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 11),
    _MscFrUniDlciVcCallingLcn_Type()
)
mscFrUniDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCallingLcn.setStatus("mandatory")


class _MscFrUniDlciVcAccountingEnabled_Type(Integer32):
    """Custom type mscFrUniDlciVcAccountingEnabled based on Integer32"""
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


_MscFrUniDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_MscFrUniDlciVcAccountingEnabled_Object = MibTableColumn
mscFrUniDlciVcAccountingEnabled = _MscFrUniDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 12),
    _MscFrUniDlciVcAccountingEnabled_Type()
)
mscFrUniDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcAccountingEnabled.setStatus("mandatory")


class _MscFrUniDlciVcFastSelectCall_Type(Integer32):
    """Custom type mscFrUniDlciVcFastSelectCall based on Integer32"""
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


_MscFrUniDlciVcFastSelectCall_Type.__name__ = "Integer32"
_MscFrUniDlciVcFastSelectCall_Object = MibTableColumn
mscFrUniDlciVcFastSelectCall = _MscFrUniDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 13),
    _MscFrUniDlciVcFastSelectCall_Type()
)
mscFrUniDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcFastSelectCall.setStatus("mandatory")


class _MscFrUniDlciVcPathReliability_Type(Integer32):
    """Custom type mscFrUniDlciVcPathReliability based on Integer32"""
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


_MscFrUniDlciVcPathReliability_Type.__name__ = "Integer32"
_MscFrUniDlciVcPathReliability_Object = MibTableColumn
mscFrUniDlciVcPathReliability = _MscFrUniDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 19),
    _MscFrUniDlciVcPathReliability_Type()
)
mscFrUniDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPathReliability.setStatus("mandatory")


class _MscFrUniDlciVcAccountingEnd_Type(Integer32):
    """Custom type mscFrUniDlciVcAccountingEnd based on Integer32"""
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


_MscFrUniDlciVcAccountingEnd_Type.__name__ = "Integer32"
_MscFrUniDlciVcAccountingEnd_Object = MibTableColumn
mscFrUniDlciVcAccountingEnd = _MscFrUniDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 20),
    _MscFrUniDlciVcAccountingEnd_Type()
)
mscFrUniDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcAccountingEnd.setStatus("mandatory")


class _MscFrUniDlciVcPriority_Type(Integer32):
    """Custom type mscFrUniDlciVcPriority based on Integer32"""
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


_MscFrUniDlciVcPriority_Type.__name__ = "Integer32"
_MscFrUniDlciVcPriority_Object = MibTableColumn
mscFrUniDlciVcPriority = _MscFrUniDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 21),
    _MscFrUniDlciVcPriority_Type()
)
mscFrUniDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPriority.setStatus("mandatory")


class _MscFrUniDlciVcSegmentSize_Type(Unsigned32):
    """Custom type mscFrUniDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscFrUniDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcSegmentSize_Object = MibTableColumn
mscFrUniDlciVcSegmentSize = _MscFrUniDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 22),
    _MscFrUniDlciVcSegmentSize_Type()
)
mscFrUniDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcSegmentSize.setStatus("mandatory")


class _MscFrUniDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscFrUniDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscFrUniDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcMaxSubnetPktSize_Object = MibTableColumn
mscFrUniDlciVcMaxSubnetPktSize = _MscFrUniDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 27),
    _MscFrUniDlciVcMaxSubnetPktSize_Type()
)
mscFrUniDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _MscFrUniDlciVcRcosToNetwork_Type(Integer32):
    """Custom type mscFrUniDlciVcRcosToNetwork based on Integer32"""
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


_MscFrUniDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_MscFrUniDlciVcRcosToNetwork_Object = MibTableColumn
mscFrUniDlciVcRcosToNetwork = _MscFrUniDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 28),
    _MscFrUniDlciVcRcosToNetwork_Type()
)
mscFrUniDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcRcosToNetwork.setStatus("mandatory")


class _MscFrUniDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type mscFrUniDlciVcRcosFromNetwork based on Integer32"""
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


_MscFrUniDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_MscFrUniDlciVcRcosFromNetwork_Object = MibTableColumn
mscFrUniDlciVcRcosFromNetwork = _MscFrUniDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 29),
    _MscFrUniDlciVcRcosFromNetwork_Type()
)
mscFrUniDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcRcosFromNetwork.setStatus("mandatory")


class _MscFrUniDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscFrUniDlciVcEmissionPriorityToNetwork based on Integer32"""
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


_MscFrUniDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscFrUniDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
mscFrUniDlciVcEmissionPriorityToNetwork = _MscFrUniDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 30),
    _MscFrUniDlciVcEmissionPriorityToNetwork_Type()
)
mscFrUniDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MscFrUniDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscFrUniDlciVcEmissionPriorityFromNetwork based on Integer32"""
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


_MscFrUniDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscFrUniDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
mscFrUniDlciVcEmissionPriorityFromNetwork = _MscFrUniDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 31),
    _MscFrUniDlciVcEmissionPriorityFromNetwork_Type()
)
mscFrUniDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscFrUniDlciVcDataPath_Type(AsciiString):
    """Custom type mscFrUniDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscFrUniDlciVcDataPath_Type.__name__ = "AsciiString"
_MscFrUniDlciVcDataPath_Object = MibTableColumn
mscFrUniDlciVcDataPath = _MscFrUniDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 10, 1, 32),
    _MscFrUniDlciVcDataPath_Type()
)
mscFrUniDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcDataPath.setStatus("mandatory")
_MscFrUniDlciVcIntdTable_Object = MibTable
mscFrUniDlciVcIntdTable = _MscFrUniDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcIntdTable.setStatus("mandatory")
_MscFrUniDlciVcIntdEntry_Object = MibTableRow
mscFrUniDlciVcIntdEntry = _MscFrUniDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11, 1)
)
mscFrUniDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcIntdEntry.setStatus("mandatory")


class _MscFrUniDlciVcCallReferenceNumber_Type(Hex):
    """Custom type mscFrUniDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrUniDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_MscFrUniDlciVcCallReferenceNumber_Object = MibTableColumn
mscFrUniDlciVcCallReferenceNumber = _MscFrUniDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11, 1, 1),
    _MscFrUniDlciVcCallReferenceNumber_Type()
)
mscFrUniDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCallReferenceNumber.setStatus("obsolete")


class _MscFrUniDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscFrUniDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrUniDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcElapsedTimeTillNow_Object = MibTableColumn
mscFrUniDlciVcElapsedTimeTillNow = _MscFrUniDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11, 1, 2),
    _MscFrUniDlciVcElapsedTimeTillNow_Type()
)
mscFrUniDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _MscFrUniDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type mscFrUniDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrUniDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcSegmentsRx_Object = MibTableColumn
mscFrUniDlciVcSegmentsRx = _MscFrUniDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11, 1, 3),
    _MscFrUniDlciVcSegmentsRx_Type()
)
mscFrUniDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcSegmentsRx.setStatus("mandatory")


class _MscFrUniDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type mscFrUniDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrUniDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcSegmentsSent_Object = MibTableColumn
mscFrUniDlciVcSegmentsSent = _MscFrUniDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11, 1, 4),
    _MscFrUniDlciVcSegmentsSent_Type()
)
mscFrUniDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcSegmentsSent.setStatus("mandatory")


class _MscFrUniDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrUniDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrUniDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrUniDlciVcStartTime_Object = MibTableColumn
mscFrUniDlciVcStartTime = _MscFrUniDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11, 1, 5),
    _MscFrUniDlciVcStartTime_Type()
)
mscFrUniDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcStartTime.setStatus("mandatory")


class _MscFrUniDlciVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscFrUniDlciVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcCallReferenceNumberDecimal_Object = MibTableColumn
mscFrUniDlciVcCallReferenceNumberDecimal = _MscFrUniDlciVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 11, 1, 7),
    _MscFrUniDlciVcCallReferenceNumberDecimal_Type()
)
mscFrUniDlciVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscFrUniDlciVcFrdTable_Object = MibTable
mscFrUniDlciVcFrdTable = _MscFrUniDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12)
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcFrdTable.setStatus("mandatory")
_MscFrUniDlciVcFrdEntry_Object = MibTableRow
mscFrUniDlciVcFrdEntry = _MscFrUniDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1)
)
mscFrUniDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcFrdEntry.setStatus("mandatory")


class _MscFrUniDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcFrmCongestedToSubnet_Object = MibTableColumn
mscFrUniDlciVcFrmCongestedToSubnet = _MscFrUniDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 2),
    _MscFrUniDlciVcFrmCongestedToSubnet_Type()
)
mscFrUniDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _MscFrUniDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcCannotForwardToSubnet_Object = MibTableColumn
mscFrUniDlciVcCannotForwardToSubnet = _MscFrUniDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 3),
    _MscFrUniDlciVcCannotForwardToSubnet_Type()
)
mscFrUniDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _MscFrUniDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcNotDataXferToSubnet_Object = MibTableColumn
mscFrUniDlciVcNotDataXferToSubnet = _MscFrUniDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 4),
    _MscFrUniDlciVcNotDataXferToSubnet_Type()
)
mscFrUniDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _MscFrUniDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscFrUniDlciVcOutOfRangeFrmFromSubnet = _MscFrUniDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 5),
    _MscFrUniDlciVcOutOfRangeFrmFromSubnet_Type()
)
mscFrUniDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscFrUniDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcCombErrorsFromSubnet_Object = MibTableColumn
mscFrUniDlciVcCombErrorsFromSubnet = _MscFrUniDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 6),
    _MscFrUniDlciVcCombErrorsFromSubnet_Type()
)
mscFrUniDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _MscFrUniDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcDuplicatesFromSubnet_Object = MibTableColumn
mscFrUniDlciVcDuplicatesFromSubnet = _MscFrUniDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 7),
    _MscFrUniDlciVcDuplicatesFromSubnet_Type()
)
mscFrUniDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscFrUniDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcNotDataXferFromSubnet_Object = MibTableColumn
mscFrUniDlciVcNotDataXferFromSubnet = _MscFrUniDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 8),
    _MscFrUniDlciVcNotDataXferFromSubnet_Type()
)
mscFrUniDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _MscFrUniDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscFrUniDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcFrmLossTimeouts_Object = MibTableColumn
mscFrUniDlciVcFrmLossTimeouts = _MscFrUniDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 9),
    _MscFrUniDlciVcFrmLossTimeouts_Type()
)
mscFrUniDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcFrmLossTimeouts.setStatus("mandatory")


class _MscFrUniDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscFrUniDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
mscFrUniDlciVcOoSeqByteCntExceeded = _MscFrUniDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 10),
    _MscFrUniDlciVcOoSeqByteCntExceeded_Type()
)
mscFrUniDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MscFrUniDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscFrUniDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcPeakOoSeqPktCount_Object = MibTableColumn
mscFrUniDlciVcPeakOoSeqPktCount = _MscFrUniDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 11),
    _MscFrUniDlciVcPeakOoSeqPktCount_Type()
)
mscFrUniDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _MscFrUniDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscFrUniDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscFrUniDlciVcPeakOoSeqFrmForwarded = _MscFrUniDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 12),
    _MscFrUniDlciVcPeakOoSeqFrmForwarded_Type()
)
mscFrUniDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscFrUniDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mscFrUniDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcSendSequenceNumber_Object = MibTableColumn
mscFrUniDlciVcSendSequenceNumber = _MscFrUniDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 13),
    _MscFrUniDlciVcSendSequenceNumber_Type()
)
mscFrUniDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcSendSequenceNumber.setStatus("mandatory")


class _MscFrUniDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscFrUniDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcPktRetryTimeouts_Object = MibTableColumn
mscFrUniDlciVcPktRetryTimeouts = _MscFrUniDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 15),
    _MscFrUniDlciVcPktRetryTimeouts_Type()
)
mscFrUniDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPktRetryTimeouts.setStatus("mandatory")


class _MscFrUniDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscFrUniDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcPeakRetryQueueSize_Object = MibTableColumn
mscFrUniDlciVcPeakRetryQueueSize = _MscFrUniDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 16),
    _MscFrUniDlciVcPeakRetryQueueSize_Type()
)
mscFrUniDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _MscFrUniDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscFrUniDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrUniDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcSubnetRecoveries_Object = MibTableColumn
mscFrUniDlciVcSubnetRecoveries = _MscFrUniDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 17),
    _MscFrUniDlciVcSubnetRecoveries_Type()
)
mscFrUniDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcSubnetRecoveries.setStatus("mandatory")


class _MscFrUniDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscFrUniDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
mscFrUniDlciVcOoSeqPktCntExceeded = _MscFrUniDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 19),
    _MscFrUniDlciVcOoSeqPktCntExceeded_Type()
)
mscFrUniDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MscFrUniDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscFrUniDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscFrUniDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscFrUniDlciVcPeakOoSeqByteCount_Object = MibTableColumn
mscFrUniDlciVcPeakOoSeqByteCount = _MscFrUniDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 12, 1, 20),
    _MscFrUniDlciVcPeakOoSeqByteCount_Type()
)
mscFrUniDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_MscFrUniDlciVcDmepTable_Object = MibTable
mscFrUniDlciVcDmepTable = _MscFrUniDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 417)
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcDmepTable.setStatus("mandatory")
_MscFrUniDlciVcDmepEntry_Object = MibTableRow
mscFrUniDlciVcDmepEntry = _MscFrUniDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 417, 1)
)
mscFrUniDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciVcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciVcDmepEntry.setStatus("mandatory")
_MscFrUniDlciVcDmepValue_Type = RowPointer
_MscFrUniDlciVcDmepValue_Object = MibTableColumn
mscFrUniDlciVcDmepValue = _MscFrUniDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 3, 417, 1, 1),
    _MscFrUniDlciVcDmepValue_Type()
)
mscFrUniDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciVcDmepValue.setStatus("mandatory")
_MscFrUniDlciSp_ObjectIdentity = ObjectIdentity
mscFrUniDlciSp = _MscFrUniDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4)
)
_MscFrUniDlciSpRowStatusTable_Object = MibTable
mscFrUniDlciSpRowStatusTable = _MscFrUniDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDlciSpRowStatusTable.setStatus("mandatory")
_MscFrUniDlciSpRowStatusEntry_Object = MibTableRow
mscFrUniDlciSpRowStatusEntry = _MscFrUniDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 1, 1)
)
mscFrUniDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciSpRowStatusEntry.setStatus("mandatory")
_MscFrUniDlciSpRowStatus_Type = RowStatus
_MscFrUniDlciSpRowStatus_Object = MibTableColumn
mscFrUniDlciSpRowStatus = _MscFrUniDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 1, 1, 1),
    _MscFrUniDlciSpRowStatus_Type()
)
mscFrUniDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciSpRowStatus.setStatus("mandatory")
_MscFrUniDlciSpComponentName_Type = DisplayString
_MscFrUniDlciSpComponentName_Object = MibTableColumn
mscFrUniDlciSpComponentName = _MscFrUniDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 1, 1, 2),
    _MscFrUniDlciSpComponentName_Type()
)
mscFrUniDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciSpComponentName.setStatus("mandatory")
_MscFrUniDlciSpStorageType_Type = StorageType
_MscFrUniDlciSpStorageType_Object = MibTableColumn
mscFrUniDlciSpStorageType = _MscFrUniDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 1, 1, 4),
    _MscFrUniDlciSpStorageType_Type()
)
mscFrUniDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciSpStorageType.setStatus("mandatory")
_MscFrUniDlciSpIndex_Type = NonReplicated
_MscFrUniDlciSpIndex_Object = MibTableColumn
mscFrUniDlciSpIndex = _MscFrUniDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 1, 1, 10),
    _MscFrUniDlciSpIndex_Type()
)
mscFrUniDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDlciSpIndex.setStatus("mandatory")
_MscFrUniDlciSpParmsTable_Object = MibTable
mscFrUniDlciSpParmsTable = _MscFrUniDlciSpParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mscFrUniDlciSpParmsTable.setStatus("mandatory")
_MscFrUniDlciSpParmsEntry_Object = MibTableRow
mscFrUniDlciSpParmsEntry = _MscFrUniDlciSpParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1)
)
mscFrUniDlciSpParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciSpParmsEntry.setStatus("mandatory")


class _MscFrUniDlciSpMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrUniDlciSpMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrUniDlciSpMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciSpMaximumFrameSize_Object = MibTableColumn
mscFrUniDlciSpMaximumFrameSize = _MscFrUniDlciSpMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 1),
    _MscFrUniDlciSpMaximumFrameSize_Type()
)
mscFrUniDlciSpMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpMaximumFrameSize.setStatus("mandatory")


class _MscFrUniDlciSpRateEnforcement_Type(Integer32):
    """Custom type mscFrUniDlciSpRateEnforcement based on Integer32"""
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


_MscFrUniDlciSpRateEnforcement_Type.__name__ = "Integer32"
_MscFrUniDlciSpRateEnforcement_Object = MibTableColumn
mscFrUniDlciSpRateEnforcement = _MscFrUniDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 2),
    _MscFrUniDlciSpRateEnforcement_Type()
)
mscFrUniDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpRateEnforcement.setStatus("mandatory")


class _MscFrUniDlciSpCommittedInformationRate_Type(Gauge32):
    """Custom type mscFrUniDlciSpCommittedInformationRate based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrUniDlciSpCommittedInformationRate_Type.__name__ = "Gauge32"
_MscFrUniDlciSpCommittedInformationRate_Object = MibTableColumn
mscFrUniDlciSpCommittedInformationRate = _MscFrUniDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 3),
    _MscFrUniDlciSpCommittedInformationRate_Type()
)
mscFrUniDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpCommittedInformationRate.setStatus("mandatory")


class _MscFrUniDlciSpCommittedBurstSize_Type(Gauge32):
    """Custom type mscFrUniDlciSpCommittedBurstSize based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrUniDlciSpCommittedBurstSize_Type.__name__ = "Gauge32"
_MscFrUniDlciSpCommittedBurstSize_Object = MibTableColumn
mscFrUniDlciSpCommittedBurstSize = _MscFrUniDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 4),
    _MscFrUniDlciSpCommittedBurstSize_Type()
)
mscFrUniDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpCommittedBurstSize.setStatus("mandatory")


class _MscFrUniDlciSpExcessBurstSize_Type(Gauge32):
    """Custom type mscFrUniDlciSpExcessBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrUniDlciSpExcessBurstSize_Type.__name__ = "Gauge32"
_MscFrUniDlciSpExcessBurstSize_Object = MibTableColumn
mscFrUniDlciSpExcessBurstSize = _MscFrUniDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 5),
    _MscFrUniDlciSpExcessBurstSize_Type()
)
mscFrUniDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpExcessBurstSize.setStatus("mandatory")


class _MscFrUniDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrUniDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_MscFrUniDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrUniDlciSpMeasurementInterval_Object = MibTableColumn
mscFrUniDlciSpMeasurementInterval = _MscFrUniDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 6),
    _MscFrUniDlciSpMeasurementInterval_Type()
)
mscFrUniDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpMeasurementInterval.setStatus("mandatory")


class _MscFrUniDlciSpRateAdaptation_Type(Integer32):
    """Custom type mscFrUniDlciSpRateAdaptation based on Integer32"""
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


_MscFrUniDlciSpRateAdaptation_Type.__name__ = "Integer32"
_MscFrUniDlciSpRateAdaptation_Object = MibTableColumn
mscFrUniDlciSpRateAdaptation = _MscFrUniDlciSpRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 7),
    _MscFrUniDlciSpRateAdaptation_Type()
)
mscFrUniDlciSpRateAdaptation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpRateAdaptation.setStatus("mandatory")


class _MscFrUniDlciSpAccounting_Type(Integer32):
    """Custom type mscFrUniDlciSpAccounting based on Integer32"""
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


_MscFrUniDlciSpAccounting_Type.__name__ = "Integer32"
_MscFrUniDlciSpAccounting_Object = MibTableColumn
mscFrUniDlciSpAccounting = _MscFrUniDlciSpAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 8),
    _MscFrUniDlciSpAccounting_Type()
)
mscFrUniDlciSpAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpAccounting.setStatus("mandatory")


class _MscFrUniDlciSpRaSensitivity_Type(Unsigned32):
    """Custom type mscFrUniDlciSpRaSensitivity based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscFrUniDlciSpRaSensitivity_Type.__name__ = "Unsigned32"
_MscFrUniDlciSpRaSensitivity_Object = MibTableColumn
mscFrUniDlciSpRaSensitivity = _MscFrUniDlciSpRaSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 9),
    _MscFrUniDlciSpRaSensitivity_Type()
)
mscFrUniDlciSpRaSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpRaSensitivity.setStatus("mandatory")


class _MscFrUniDlciSpUpdateBCI_Type(Integer32):
    """Custom type mscFrUniDlciSpUpdateBCI based on Integer32"""
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


_MscFrUniDlciSpUpdateBCI_Type.__name__ = "Integer32"
_MscFrUniDlciSpUpdateBCI_Object = MibTableColumn
mscFrUniDlciSpUpdateBCI = _MscFrUniDlciSpUpdateBCI_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 4, 11, 1, 10),
    _MscFrUniDlciSpUpdateBCI_Type()
)
mscFrUniDlciSpUpdateBCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciSpUpdateBCI.setStatus("mandatory")
_MscFrUniDlciLb_ObjectIdentity = ObjectIdentity
mscFrUniDlciLb = _MscFrUniDlciLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5)
)
_MscFrUniDlciLbRowStatusTable_Object = MibTable
mscFrUniDlciLbRowStatusTable = _MscFrUniDlciLbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDlciLbRowStatusTable.setStatus("mandatory")
_MscFrUniDlciLbRowStatusEntry_Object = MibTableRow
mscFrUniDlciLbRowStatusEntry = _MscFrUniDlciLbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 1, 1)
)
mscFrUniDlciLbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciLbRowStatusEntry.setStatus("mandatory")
_MscFrUniDlciLbRowStatus_Type = RowStatus
_MscFrUniDlciLbRowStatus_Object = MibTableColumn
mscFrUniDlciLbRowStatus = _MscFrUniDlciLbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 1, 1, 1),
    _MscFrUniDlciLbRowStatus_Type()
)
mscFrUniDlciLbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbRowStatus.setStatus("mandatory")
_MscFrUniDlciLbComponentName_Type = DisplayString
_MscFrUniDlciLbComponentName_Object = MibTableColumn
mscFrUniDlciLbComponentName = _MscFrUniDlciLbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 1, 1, 2),
    _MscFrUniDlciLbComponentName_Type()
)
mscFrUniDlciLbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbComponentName.setStatus("mandatory")
_MscFrUniDlciLbStorageType_Type = StorageType
_MscFrUniDlciLbStorageType_Object = MibTableColumn
mscFrUniDlciLbStorageType = _MscFrUniDlciLbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 1, 1, 4),
    _MscFrUniDlciLbStorageType_Type()
)
mscFrUniDlciLbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbStorageType.setStatus("mandatory")
_MscFrUniDlciLbIndex_Type = NonReplicated
_MscFrUniDlciLbIndex_Object = MibTableColumn
mscFrUniDlciLbIndex = _MscFrUniDlciLbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 1, 1, 10),
    _MscFrUniDlciLbIndex_Type()
)
mscFrUniDlciLbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDlciLbIndex.setStatus("mandatory")
_MscFrUniDlciLbStatsTable_Object = MibTable
mscFrUniDlciLbStatsTable = _MscFrUniDlciLbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDlciLbStatsTable.setStatus("mandatory")
_MscFrUniDlciLbStatsEntry_Object = MibTableRow
mscFrUniDlciLbStatsEntry = _MscFrUniDlciLbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1)
)
mscFrUniDlciLbStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciLbStatsEntry.setStatus("mandatory")


class _MscFrUniDlciLbLocalTotalFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbLocalTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbLocalTotalFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbLocalTotalFrm_Object = MibTableColumn
mscFrUniDlciLbLocalTotalFrm = _MscFrUniDlciLbLocalTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 1),
    _MscFrUniDlciLbLocalTotalFrm_Type()
)
mscFrUniDlciLbLocalTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbLocalTotalFrm.setStatus("mandatory")


class _MscFrUniDlciLbLocalTotalBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciLbLocalTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbLocalTotalBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbLocalTotalBytes_Object = MibTableColumn
mscFrUniDlciLbLocalTotalBytes = _MscFrUniDlciLbLocalTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 2),
    _MscFrUniDlciLbLocalTotalBytes_Type()
)
mscFrUniDlciLbLocalTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbLocalTotalBytes.setStatus("mandatory")


class _MscFrUniDlciLbLocalFecnFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbLocalFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbLocalFecnFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbLocalFecnFrm_Object = MibTableColumn
mscFrUniDlciLbLocalFecnFrm = _MscFrUniDlciLbLocalFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 3),
    _MscFrUniDlciLbLocalFecnFrm_Type()
)
mscFrUniDlciLbLocalFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbLocalFecnFrm.setStatus("mandatory")


class _MscFrUniDlciLbLocalBecnFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbLocalBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbLocalBecnFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbLocalBecnFrm_Object = MibTableColumn
mscFrUniDlciLbLocalBecnFrm = _MscFrUniDlciLbLocalBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 4),
    _MscFrUniDlciLbLocalBecnFrm_Type()
)
mscFrUniDlciLbLocalBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbLocalBecnFrm.setStatus("mandatory")


class _MscFrUniDlciLbLocalDeFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbLocalDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbLocalDeFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbLocalDeFrm_Object = MibTableColumn
mscFrUniDlciLbLocalDeFrm = _MscFrUniDlciLbLocalDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 5),
    _MscFrUniDlciLbLocalDeFrm_Type()
)
mscFrUniDlciLbLocalDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbLocalDeFrm.setStatus("mandatory")


class _MscFrUniDlciLbLocalDeBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciLbLocalDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbLocalDeBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbLocalDeBytes_Object = MibTableColumn
mscFrUniDlciLbLocalDeBytes = _MscFrUniDlciLbLocalDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 6),
    _MscFrUniDlciLbLocalDeBytes_Type()
)
mscFrUniDlciLbLocalDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbLocalDeBytes.setStatus("mandatory")


class _MscFrUniDlciLbRemoteTotalFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbRemoteTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbRemoteTotalFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbRemoteTotalFrm_Object = MibTableColumn
mscFrUniDlciLbRemoteTotalFrm = _MscFrUniDlciLbRemoteTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 7),
    _MscFrUniDlciLbRemoteTotalFrm_Type()
)
mscFrUniDlciLbRemoteTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbRemoteTotalFrm.setStatus("mandatory")


class _MscFrUniDlciLbRemoteTotalBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciLbRemoteTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbRemoteTotalBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbRemoteTotalBytes_Object = MibTableColumn
mscFrUniDlciLbRemoteTotalBytes = _MscFrUniDlciLbRemoteTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 8),
    _MscFrUniDlciLbRemoteTotalBytes_Type()
)
mscFrUniDlciLbRemoteTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbRemoteTotalBytes.setStatus("mandatory")


class _MscFrUniDlciLbRemoteFecnFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbRemoteFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbRemoteFecnFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbRemoteFecnFrm_Object = MibTableColumn
mscFrUniDlciLbRemoteFecnFrm = _MscFrUniDlciLbRemoteFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 9),
    _MscFrUniDlciLbRemoteFecnFrm_Type()
)
mscFrUniDlciLbRemoteFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbRemoteFecnFrm.setStatus("mandatory")


class _MscFrUniDlciLbRemoteBecnFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbRemoteBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbRemoteBecnFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbRemoteBecnFrm_Object = MibTableColumn
mscFrUniDlciLbRemoteBecnFrm = _MscFrUniDlciLbRemoteBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 10),
    _MscFrUniDlciLbRemoteBecnFrm_Type()
)
mscFrUniDlciLbRemoteBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbRemoteBecnFrm.setStatus("mandatory")


class _MscFrUniDlciLbRemoteDeFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciLbRemoteDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbRemoteDeFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbRemoteDeFrm_Object = MibTableColumn
mscFrUniDlciLbRemoteDeFrm = _MscFrUniDlciLbRemoteDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 13),
    _MscFrUniDlciLbRemoteDeFrm_Type()
)
mscFrUniDlciLbRemoteDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbRemoteDeFrm.setStatus("mandatory")


class _MscFrUniDlciLbRemoteDeBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciLbRemoteDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciLbRemoteDeBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciLbRemoteDeBytes_Object = MibTableColumn
mscFrUniDlciLbRemoteDeBytes = _MscFrUniDlciLbRemoteDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 5, 10, 1, 14),
    _MscFrUniDlciLbRemoteDeBytes_Type()
)
mscFrUniDlciLbRemoteDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLbRemoteDeBytes.setStatus("mandatory")
_MscFrUniDlciEgressSp_ObjectIdentity = ObjectIdentity
mscFrUniDlciEgressSp = _MscFrUniDlciEgressSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6)
)
_MscFrUniDlciEgressSpRowStatusTable_Object = MibTable
mscFrUniDlciEgressSpRowStatusTable = _MscFrUniDlciEgressSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpRowStatusTable.setStatus("mandatory")
_MscFrUniDlciEgressSpRowStatusEntry_Object = MibTableRow
mscFrUniDlciEgressSpRowStatusEntry = _MscFrUniDlciEgressSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 1, 1)
)
mscFrUniDlciEgressSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciEgressSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpRowStatusEntry.setStatus("mandatory")
_MscFrUniDlciEgressSpRowStatus_Type = RowStatus
_MscFrUniDlciEgressSpRowStatus_Object = MibTableColumn
mscFrUniDlciEgressSpRowStatus = _MscFrUniDlciEgressSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 1, 1, 1),
    _MscFrUniDlciEgressSpRowStatus_Type()
)
mscFrUniDlciEgressSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpRowStatus.setStatus("mandatory")
_MscFrUniDlciEgressSpComponentName_Type = DisplayString
_MscFrUniDlciEgressSpComponentName_Object = MibTableColumn
mscFrUniDlciEgressSpComponentName = _MscFrUniDlciEgressSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 1, 1, 2),
    _MscFrUniDlciEgressSpComponentName_Type()
)
mscFrUniDlciEgressSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpComponentName.setStatus("mandatory")
_MscFrUniDlciEgressSpStorageType_Type = StorageType
_MscFrUniDlciEgressSpStorageType_Object = MibTableColumn
mscFrUniDlciEgressSpStorageType = _MscFrUniDlciEgressSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 1, 1, 4),
    _MscFrUniDlciEgressSpStorageType_Type()
)
mscFrUniDlciEgressSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpStorageType.setStatus("mandatory")
_MscFrUniDlciEgressSpIndex_Type = NonReplicated
_MscFrUniDlciEgressSpIndex_Object = MibTableColumn
mscFrUniDlciEgressSpIndex = _MscFrUniDlciEgressSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 1, 1, 10),
    _MscFrUniDlciEgressSpIndex_Type()
)
mscFrUniDlciEgressSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpIndex.setStatus("mandatory")
_MscFrUniDlciEgressSpProvTable_Object = MibTable
mscFrUniDlciEgressSpProvTable = _MscFrUniDlciEgressSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpProvTable.setStatus("mandatory")
_MscFrUniDlciEgressSpProvEntry_Object = MibTableRow
mscFrUniDlciEgressSpProvEntry = _MscFrUniDlciEgressSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 10, 1)
)
mscFrUniDlciEgressSpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciEgressSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpProvEntry.setStatus("mandatory")


class _MscFrUniDlciEgressSpCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrUniDlciEgressSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 50000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
        ValueRangeConstraint(50000001, 50000001),
    )


_MscFrUniDlciEgressSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrUniDlciEgressSpCommittedInformationRate_Object = MibTableColumn
mscFrUniDlciEgressSpCommittedInformationRate = _MscFrUniDlciEgressSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 10, 1, 1),
    _MscFrUniDlciEgressSpCommittedInformationRate_Type()
)
mscFrUniDlciEgressSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpCommittedInformationRate.setStatus("mandatory")


class _MscFrUniDlciEgressSpCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrUniDlciEgressSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 50000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
        ValueRangeConstraint(50000001, 50000001),
    )


_MscFrUniDlciEgressSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciEgressSpCommittedBurstSize_Object = MibTableColumn
mscFrUniDlciEgressSpCommittedBurstSize = _MscFrUniDlciEgressSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 10, 1, 2),
    _MscFrUniDlciEgressSpCommittedBurstSize_Type()
)
mscFrUniDlciEgressSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpCommittedBurstSize.setStatus("mandatory")


class _MscFrUniDlciEgressSpExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrUniDlciEgressSpExcessBurstSize based on Unsigned32"""
    defaultValue = 50000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
        ValueRangeConstraint(50000001, 50000001),
    )


_MscFrUniDlciEgressSpExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciEgressSpExcessBurstSize_Object = MibTableColumn
mscFrUniDlciEgressSpExcessBurstSize = _MscFrUniDlciEgressSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 10, 1, 3),
    _MscFrUniDlciEgressSpExcessBurstSize_Type()
)
mscFrUniDlciEgressSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpExcessBurstSize.setStatus("mandatory")


class _MscFrUniDlciEgressSpMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrUniDlciEgressSpMeasurementInterval based on Unsigned32"""
    defaultValue = 25501

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
        ValueRangeConstraint(25501, 25501),
    )


_MscFrUniDlciEgressSpMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrUniDlciEgressSpMeasurementInterval_Object = MibTableColumn
mscFrUniDlciEgressSpMeasurementInterval = _MscFrUniDlciEgressSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 6, 10, 1, 4),
    _MscFrUniDlciEgressSpMeasurementInterval_Type()
)
mscFrUniDlciEgressSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniDlciEgressSpMeasurementInterval.setStatus("mandatory")
_MscFrUniDlciStateTable_Object = MibTable
mscFrUniDlciStateTable = _MscFrUniDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrUniDlciStateTable.setStatus("mandatory")
_MscFrUniDlciStateEntry_Object = MibTableRow
mscFrUniDlciStateEntry = _MscFrUniDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1)
)
mscFrUniDlciStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciStateEntry.setStatus("mandatory")


class _MscFrUniDlciAdminState_Type(Integer32):
    """Custom type mscFrUniDlciAdminState based on Integer32"""
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


_MscFrUniDlciAdminState_Type.__name__ = "Integer32"
_MscFrUniDlciAdminState_Object = MibTableColumn
mscFrUniDlciAdminState = _MscFrUniDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 1),
    _MscFrUniDlciAdminState_Type()
)
mscFrUniDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciAdminState.setStatus("mandatory")


class _MscFrUniDlciOperationalState_Type(Integer32):
    """Custom type mscFrUniDlciOperationalState based on Integer32"""
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


_MscFrUniDlciOperationalState_Type.__name__ = "Integer32"
_MscFrUniDlciOperationalState_Object = MibTableColumn
mscFrUniDlciOperationalState = _MscFrUniDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 2),
    _MscFrUniDlciOperationalState_Type()
)
mscFrUniDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciOperationalState.setStatus("mandatory")


class _MscFrUniDlciUsageState_Type(Integer32):
    """Custom type mscFrUniDlciUsageState based on Integer32"""
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


_MscFrUniDlciUsageState_Type.__name__ = "Integer32"
_MscFrUniDlciUsageState_Object = MibTableColumn
mscFrUniDlciUsageState = _MscFrUniDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 3),
    _MscFrUniDlciUsageState_Type()
)
mscFrUniDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciUsageState.setStatus("mandatory")


class _MscFrUniDlciAvailabilityStatus_Type(OctetString):
    """Custom type mscFrUniDlciAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFrUniDlciAvailabilityStatus_Type.__name__ = "OctetString"
_MscFrUniDlciAvailabilityStatus_Object = MibTableColumn
mscFrUniDlciAvailabilityStatus = _MscFrUniDlciAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 4),
    _MscFrUniDlciAvailabilityStatus_Type()
)
mscFrUniDlciAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciAvailabilityStatus.setStatus("mandatory")


class _MscFrUniDlciProceduralStatus_Type(OctetString):
    """Custom type mscFrUniDlciProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniDlciProceduralStatus_Type.__name__ = "OctetString"
_MscFrUniDlciProceduralStatus_Object = MibTableColumn
mscFrUniDlciProceduralStatus = _MscFrUniDlciProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 5),
    _MscFrUniDlciProceduralStatus_Type()
)
mscFrUniDlciProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciProceduralStatus.setStatus("mandatory")


class _MscFrUniDlciControlStatus_Type(OctetString):
    """Custom type mscFrUniDlciControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniDlciControlStatus_Type.__name__ = "OctetString"
_MscFrUniDlciControlStatus_Object = MibTableColumn
mscFrUniDlciControlStatus = _MscFrUniDlciControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 6),
    _MscFrUniDlciControlStatus_Type()
)
mscFrUniDlciControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciControlStatus.setStatus("mandatory")


class _MscFrUniDlciAlarmStatus_Type(OctetString):
    """Custom type mscFrUniDlciAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniDlciAlarmStatus_Type.__name__ = "OctetString"
_MscFrUniDlciAlarmStatus_Object = MibTableColumn
mscFrUniDlciAlarmStatus = _MscFrUniDlciAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 7),
    _MscFrUniDlciAlarmStatus_Type()
)
mscFrUniDlciAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciAlarmStatus.setStatus("mandatory")


class _MscFrUniDlciStandbyStatus_Type(Integer32):
    """Custom type mscFrUniDlciStandbyStatus based on Integer32"""
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


_MscFrUniDlciStandbyStatus_Type.__name__ = "Integer32"
_MscFrUniDlciStandbyStatus_Object = MibTableColumn
mscFrUniDlciStandbyStatus = _MscFrUniDlciStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 8),
    _MscFrUniDlciStandbyStatus_Type()
)
mscFrUniDlciStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciStandbyStatus.setStatus("mandatory")


class _MscFrUniDlciUnknownStatus_Type(Integer32):
    """Custom type mscFrUniDlciUnknownStatus based on Integer32"""
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


_MscFrUniDlciUnknownStatus_Type.__name__ = "Integer32"
_MscFrUniDlciUnknownStatus_Object = MibTableColumn
mscFrUniDlciUnknownStatus = _MscFrUniDlciUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 10, 1, 9),
    _MscFrUniDlciUnknownStatus_Type()
)
mscFrUniDlciUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciUnknownStatus.setStatus("mandatory")
_MscFrUniDlciAbitTable_Object = MibTable
mscFrUniDlciAbitTable = _MscFrUniDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 12)
)
if mibBuilder.loadTexts:
    mscFrUniDlciAbitTable.setStatus("mandatory")
_MscFrUniDlciAbitEntry_Object = MibTableRow
mscFrUniDlciAbitEntry = _MscFrUniDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 12, 1)
)
mscFrUniDlciAbitEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciAbitEntry.setStatus("mandatory")


class _MscFrUniDlciABitStatusToIf_Type(Integer32):
    """Custom type mscFrUniDlciABitStatusToIf based on Integer32"""
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


_MscFrUniDlciABitStatusToIf_Type.__name__ = "Integer32"
_MscFrUniDlciABitStatusToIf_Object = MibTableColumn
mscFrUniDlciABitStatusToIf = _MscFrUniDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 12, 1, 1),
    _MscFrUniDlciABitStatusToIf_Type()
)
mscFrUniDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciABitStatusToIf.setStatus("mandatory")


class _MscFrUniDlciABitReasonToIf_Type(Integer32):
    """Custom type mscFrUniDlciABitReasonToIf based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dlciCollisionAtNni", 10),
          ("localLinkDown", 4),
          ("localLmiError", 2),
          ("notApplicable", 0),
          ("pvcSpvcDown", 6),
          ("remoteLinkDown", 5),
          ("remoteLmiError", 3),
          ("remoteUserSignaled", 1),
          ("resourceNotAvailable", 9),
          ("userNotAuthorized", 8))
    )


_MscFrUniDlciABitReasonToIf_Type.__name__ = "Integer32"
_MscFrUniDlciABitReasonToIf_Object = MibTableColumn
mscFrUniDlciABitReasonToIf = _MscFrUniDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 12, 1, 2),
    _MscFrUniDlciABitReasonToIf_Type()
)
mscFrUniDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciABitReasonToIf.setStatus("mandatory")


class _MscFrUniDlciABitStatusFromIf_Type(Integer32):
    """Custom type mscFrUniDlciABitStatusFromIf based on Integer32"""
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


_MscFrUniDlciABitStatusFromIf_Type.__name__ = "Integer32"
_MscFrUniDlciABitStatusFromIf_Object = MibTableColumn
mscFrUniDlciABitStatusFromIf = _MscFrUniDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 12, 1, 3),
    _MscFrUniDlciABitStatusFromIf_Type()
)
mscFrUniDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciABitStatusFromIf.setStatus("mandatory")


class _MscFrUniDlciABitReasonFromIf_Type(Integer32):
    """Custom type mscFrUniDlciABitReasonFromIf based on Integer32"""
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


_MscFrUniDlciABitReasonFromIf_Type.__name__ = "Integer32"
_MscFrUniDlciABitReasonFromIf_Object = MibTableColumn
mscFrUniDlciABitReasonFromIf = _MscFrUniDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 12, 1, 4),
    _MscFrUniDlciABitReasonFromIf_Type()
)
mscFrUniDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciABitReasonFromIf.setStatus("mandatory")


class _MscFrUniDlciLoopbackState_Type(Integer32):
    """Custom type mscFrUniDlciLoopbackState based on Integer32"""
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


_MscFrUniDlciLoopbackState_Type.__name__ = "Integer32"
_MscFrUniDlciLoopbackState_Object = MibTableColumn
mscFrUniDlciLoopbackState = _MscFrUniDlciLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 12, 1, 5),
    _MscFrUniDlciLoopbackState_Type()
)
mscFrUniDlciLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLoopbackState.setStatus("mandatory")
_MscFrUniDlciCalldTable_Object = MibTable
mscFrUniDlciCalldTable = _MscFrUniDlciCalldTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 13)
)
if mibBuilder.loadTexts:
    mscFrUniDlciCalldTable.setStatus("mandatory")
_MscFrUniDlciCalldEntry_Object = MibTableRow
mscFrUniDlciCalldEntry = _MscFrUniDlciCalldEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 13, 1)
)
mscFrUniDlciCalldEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciCalldEntry.setStatus("mandatory")


class _MscFrUniDlciCallType_Type(Integer32):
    """Custom type mscFrUniDlciCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 0),
          ("spvc", 2),
          ("svc", 1))
    )


_MscFrUniDlciCallType_Type.__name__ = "Integer32"
_MscFrUniDlciCallType_Object = MibTableColumn
mscFrUniDlciCallType = _MscFrUniDlciCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 13, 1, 1),
    _MscFrUniDlciCallType_Type()
)
mscFrUniDlciCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCallType.setStatus("mandatory")


class _MscFrUniDlciQstate_Type(Integer32):
    """Custom type mscFrUniDlciQstate based on Integer32"""
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
              20,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("callProceedingReceived", 9),
          ("callProceedingSent", 3),
          ("disconnectIndication", 12),
          ("disconnectRequest", 11),
          ("notApplicable", 20),
          ("null", 0),
          ("releaseRequest", 19),
          ("restart", 62),
          ("restartRequest", 61))
    )


_MscFrUniDlciQstate_Type.__name__ = "Integer32"
_MscFrUniDlciQstate_Object = MibTableColumn
mscFrUniDlciQstate = _MscFrUniDlciQstate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 13, 1, 2),
    _MscFrUniDlciQstate_Type()
)
mscFrUniDlciQstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciQstate.setStatus("mandatory")


class _MscFrUniDlciCallref_Type(Unsigned32):
    """Custom type mscFrUniDlciCallref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscFrUniDlciCallref_Type.__name__ = "Unsigned32"
_MscFrUniDlciCallref_Object = MibTableColumn
mscFrUniDlciCallref = _MscFrUniDlciCallref_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 13, 1, 3),
    _MscFrUniDlciCallref_Type()
)
mscFrUniDlciCallref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCallref.setStatus("mandatory")
_MscFrUniDlciSpOpTable_Object = MibTable
mscFrUniDlciSpOpTable = _MscFrUniDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14)
)
if mibBuilder.loadTexts:
    mscFrUniDlciSpOpTable.setStatus("mandatory")
_MscFrUniDlciSpOpEntry_Object = MibTableRow
mscFrUniDlciSpOpEntry = _MscFrUniDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1)
)
mscFrUniDlciSpOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciSpOpEntry.setStatus("mandatory")


class _MscFrUniDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrUniDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrUniDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciMaximumFrameSize_Object = MibTableColumn
mscFrUniDlciMaximumFrameSize = _MscFrUniDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 1),
    _MscFrUniDlciMaximumFrameSize_Type()
)
mscFrUniDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciMaximumFrameSize.setStatus("mandatory")


class _MscFrUniDlciRateEnforcement_Type(Integer32):
    """Custom type mscFrUniDlciRateEnforcement based on Integer32"""
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


_MscFrUniDlciRateEnforcement_Type.__name__ = "Integer32"
_MscFrUniDlciRateEnforcement_Object = MibTableColumn
mscFrUniDlciRateEnforcement = _MscFrUniDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 2),
    _MscFrUniDlciRateEnforcement_Type()
)
mscFrUniDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciRateEnforcement.setStatus("obsolete")


class _MscFrUniDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrUniDlciCommittedInformationRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrUniDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrUniDlciCommittedInformationRate_Object = MibTableColumn
mscFrUniDlciCommittedInformationRate = _MscFrUniDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 3),
    _MscFrUniDlciCommittedInformationRate_Type()
)
mscFrUniDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCommittedInformationRate.setStatus("mandatory")


class _MscFrUniDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrUniDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrUniDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciCommittedBurstSize_Object = MibTableColumn
mscFrUniDlciCommittedBurstSize = _MscFrUniDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 4),
    _MscFrUniDlciCommittedBurstSize_Type()
)
mscFrUniDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCommittedBurstSize.setStatus("mandatory")


class _MscFrUniDlciExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrUniDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrUniDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrUniDlciExcessBurstSize_Object = MibTableColumn
mscFrUniDlciExcessBurstSize = _MscFrUniDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 5),
    _MscFrUniDlciExcessBurstSize_Type()
)
mscFrUniDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciExcessBurstSize.setStatus("mandatory")


class _MscFrUniDlciMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrUniDlciMeasurementInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrUniDlciMeasurementInterval_Object = MibTableColumn
mscFrUniDlciMeasurementInterval = _MscFrUniDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 6),
    _MscFrUniDlciMeasurementInterval_Type()
)
mscFrUniDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciMeasurementInterval.setStatus("mandatory")


class _MscFrUniDlciRateAdaptation_Type(Integer32):
    """Custom type mscFrUniDlciRateAdaptation based on Integer32"""
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


_MscFrUniDlciRateAdaptation_Type.__name__ = "Integer32"
_MscFrUniDlciRateAdaptation_Object = MibTableColumn
mscFrUniDlciRateAdaptation = _MscFrUniDlciRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 7),
    _MscFrUniDlciRateAdaptation_Type()
)
mscFrUniDlciRateAdaptation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciRateAdaptation.setStatus("obsolete")


class _MscFrUniDlciAccounting_Type(Integer32):
    """Custom type mscFrUniDlciAccounting based on Integer32"""
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


_MscFrUniDlciAccounting_Type.__name__ = "Integer32"
_MscFrUniDlciAccounting_Object = MibTableColumn
mscFrUniDlciAccounting = _MscFrUniDlciAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 8),
    _MscFrUniDlciAccounting_Type()
)
mscFrUniDlciAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciAccounting.setStatus("mandatory")


class _MscFrUniDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrUniDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_MscFrUniDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrUniDlciEmissionPriorityToIf_Object = MibTableColumn
mscFrUniDlciEmissionPriorityToIf = _MscFrUniDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 9),
    _MscFrUniDlciEmissionPriorityToIf_Type()
)
mscFrUniDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEmissionPriorityToIf.setStatus("mandatory")


class _MscFrUniDlciTransferPriToNwk_Type(Unsigned32):
    """Custom type mscFrUniDlciTransferPriToNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniDlciTransferPriToNwk_Type.__name__ = "Unsigned32"
_MscFrUniDlciTransferPriToNwk_Object = MibTableColumn
mscFrUniDlciTransferPriToNwk = _MscFrUniDlciTransferPriToNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 10),
    _MscFrUniDlciTransferPriToNwk_Type()
)
mscFrUniDlciTransferPriToNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTransferPriToNwk.setStatus("mandatory")


class _MscFrUniDlciTransferPriFromNwk_Type(Unsigned32):
    """Custom type mscFrUniDlciTransferPriFromNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniDlciTransferPriFromNwk_Type.__name__ = "Unsigned32"
_MscFrUniDlciTransferPriFromNwk_Object = MibTableColumn
mscFrUniDlciTransferPriFromNwk = _MscFrUniDlciTransferPriFromNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 14, 1, 11),
    _MscFrUniDlciTransferPriFromNwk_Type()
)
mscFrUniDlciTransferPriFromNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTransferPriFromNwk.setStatus("mandatory")
_MscFrUniDlciStatsTable_Object = MibTable
mscFrUniDlciStatsTable = _MscFrUniDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15)
)
if mibBuilder.loadTexts:
    mscFrUniDlciStatsTable.setStatus("mandatory")
_MscFrUniDlciStatsEntry_Object = MibTableRow
mscFrUniDlciStatsEntry = _MscFrUniDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1)
)
mscFrUniDlciStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciStatsEntry.setStatus("mandatory")


class _MscFrUniDlciFrmToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciFrmToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciFrmToIf_Object = MibTableColumn
mscFrUniDlciFrmToIf = _MscFrUniDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 1),
    _MscFrUniDlciFrmToIf_Type()
)
mscFrUniDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciFrmToIf.setStatus("mandatory")


class _MscFrUniDlciFecnFrmToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciFecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciFecnFrmToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciFecnFrmToIf_Object = MibTableColumn
mscFrUniDlciFecnFrmToIf = _MscFrUniDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 2),
    _MscFrUniDlciFecnFrmToIf_Type()
)
mscFrUniDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciFecnFrmToIf.setStatus("mandatory")


class _MscFrUniDlciBecnFrmToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciBecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciBecnFrmToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciBecnFrmToIf_Object = MibTableColumn
mscFrUniDlciBecnFrmToIf = _MscFrUniDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 3),
    _MscFrUniDlciBecnFrmToIf_Type()
)
mscFrUniDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciBecnFrmToIf.setStatus("mandatory")


class _MscFrUniDlciBciToSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciBciToSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciBciToSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciBciToSubnet_Object = MibTableColumn
mscFrUniDlciBciToSubnet = _MscFrUniDlciBciToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 4),
    _MscFrUniDlciBciToSubnet_Type()
)
mscFrUniDlciBciToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciBciToSubnet.setStatus("mandatory")


class _MscFrUniDlciDeFrmToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDeFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDeFrmToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDeFrmToIf_Object = MibTableColumn
mscFrUniDlciDeFrmToIf = _MscFrUniDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 5),
    _MscFrUniDlciDeFrmToIf_Type()
)
mscFrUniDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDeFrmToIf.setStatus("mandatory")


class _MscFrUniDlciDiscCongestedToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscCongestedToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscCongestedToIf_Object = MibTableColumn
mscFrUniDlciDiscCongestedToIf = _MscFrUniDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 6),
    _MscFrUniDlciDiscCongestedToIf_Type()
)
mscFrUniDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscCongestedToIf.setStatus("mandatory")


class _MscFrUniDlciDiscDeCongestedToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscDeCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscDeCongestedToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscDeCongestedToIf_Object = MibTableColumn
mscFrUniDlciDiscDeCongestedToIf = _MscFrUniDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 7),
    _MscFrUniDlciDiscDeCongestedToIf_Type()
)
mscFrUniDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscDeCongestedToIf.setStatus("mandatory")


class _MscFrUniDlciFrmFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciFrmFromIf_Object = MibTableColumn
mscFrUniDlciFrmFromIf = _MscFrUniDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 8),
    _MscFrUniDlciFrmFromIf_Type()
)
mscFrUniDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciFrmFromIf.setStatus("mandatory")


class _MscFrUniDlciFecnFrmFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciFecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciFecnFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciFecnFrmFromIf_Object = MibTableColumn
mscFrUniDlciFecnFrmFromIf = _MscFrUniDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 9),
    _MscFrUniDlciFecnFrmFromIf_Type()
)
mscFrUniDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciFecnFrmFromIf.setStatus("mandatory")


class _MscFrUniDlciBecnFrmFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciBecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciBecnFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciBecnFrmFromIf_Object = MibTableColumn
mscFrUniDlciBecnFrmFromIf = _MscFrUniDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 10),
    _MscFrUniDlciBecnFrmFromIf_Type()
)
mscFrUniDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciBecnFrmFromIf.setStatus("mandatory")


class _MscFrUniDlciFciFromSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciFciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciFciFromSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciFciFromSubnet_Object = MibTableColumn
mscFrUniDlciFciFromSubnet = _MscFrUniDlciFciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 11),
    _MscFrUniDlciFciFromSubnet_Type()
)
mscFrUniDlciFciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciFciFromSubnet.setStatus("mandatory")


class _MscFrUniDlciBciFromSubnet_Type(Unsigned32):
    """Custom type mscFrUniDlciBciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciBciFromSubnet_Type.__name__ = "Unsigned32"
_MscFrUniDlciBciFromSubnet_Object = MibTableColumn
mscFrUniDlciBciFromSubnet = _MscFrUniDlciBciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 12),
    _MscFrUniDlciBciFromSubnet_Type()
)
mscFrUniDlciBciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciBciFromSubnet.setStatus("mandatory")


class _MscFrUniDlciDeFrmFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDeFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDeFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDeFrmFromIf_Object = MibTableColumn
mscFrUniDlciDeFrmFromIf = _MscFrUniDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 13),
    _MscFrUniDlciDeFrmFromIf_Type()
)
mscFrUniDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDeFrmFromIf.setStatus("mandatory")


class _MscFrUniDlciExcessFrmFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciExcessFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciExcessFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciExcessFrmFromIf_Object = MibTableColumn
mscFrUniDlciExcessFrmFromIf = _MscFrUniDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 14),
    _MscFrUniDlciExcessFrmFromIf_Type()
)
mscFrUniDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciExcessFrmFromIf.setStatus("mandatory")


class _MscFrUniDlciDiscExcessFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscExcessFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscExcessFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscExcessFromIf_Object = MibTableColumn
mscFrUniDlciDiscExcessFromIf = _MscFrUniDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 15),
    _MscFrUniDlciDiscExcessFromIf_Type()
)
mscFrUniDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscExcessFromIf.setStatus("mandatory")


class _MscFrUniDlciDiscFrameAbit_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscFrameAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscFrameAbit_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscFrameAbit_Object = MibTableColumn
mscFrUniDlciDiscFrameAbit = _MscFrUniDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 16),
    _MscFrUniDlciDiscFrameAbit_Type()
)
mscFrUniDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscFrameAbit.setStatus("mandatory")


class _MscFrUniDlciDiscCongestedFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscCongestedFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscCongestedFromIf_Object = MibTableColumn
mscFrUniDlciDiscCongestedFromIf = _MscFrUniDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 17),
    _MscFrUniDlciDiscCongestedFromIf_Type()
)
mscFrUniDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscCongestedFromIf.setStatus("mandatory")


class _MscFrUniDlciDiscDeCongestedFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscDeCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscDeCongestedFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscDeCongestedFromIf_Object = MibTableColumn
mscFrUniDlciDiscDeCongestedFromIf = _MscFrUniDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 18),
    _MscFrUniDlciDiscDeCongestedFromIf_Type()
)
mscFrUniDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscDeCongestedFromIf.setStatus("mandatory")


class _MscFrUniDlciErrorShortFrmFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciErrorShortFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciErrorShortFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciErrorShortFrmFromIf_Object = MibTableColumn
mscFrUniDlciErrorShortFrmFromIf = _MscFrUniDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 19),
    _MscFrUniDlciErrorShortFrmFromIf_Type()
)
mscFrUniDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciErrorShortFrmFromIf.setStatus("mandatory")


class _MscFrUniDlciErrorLongFrmFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciErrorLongFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciErrorLongFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciErrorLongFrmFromIf_Object = MibTableColumn
mscFrUniDlciErrorLongFrmFromIf = _MscFrUniDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 20),
    _MscFrUniDlciErrorLongFrmFromIf_Type()
)
mscFrUniDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciErrorLongFrmFromIf.setStatus("mandatory")


class _MscFrUniDlciBecnFrmSetByService_Type(Unsigned32):
    """Custom type mscFrUniDlciBecnFrmSetByService based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciBecnFrmSetByService_Type.__name__ = "Unsigned32"
_MscFrUniDlciBecnFrmSetByService_Object = MibTableColumn
mscFrUniDlciBecnFrmSetByService = _MscFrUniDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 21),
    _MscFrUniDlciBecnFrmSetByService_Type()
)
mscFrUniDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciBecnFrmSetByService.setStatus("mandatory")


class _MscFrUniDlciBytesToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciBytesToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciBytesToIf_Object = MibTableColumn
mscFrUniDlciBytesToIf = _MscFrUniDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 22),
    _MscFrUniDlciBytesToIf_Type()
)
mscFrUniDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciBytesToIf.setStatus("mandatory")


class _MscFrUniDlciDeBytesToIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDeBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDeBytesToIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDeBytesToIf_Object = MibTableColumn
mscFrUniDlciDeBytesToIf = _MscFrUniDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 23),
    _MscFrUniDlciDeBytesToIf_Type()
)
mscFrUniDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDeBytesToIf.setStatus("mandatory")


class _MscFrUniDlciDiscCongestedToIfBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscCongestedToIfBytes_Object = MibTableColumn
mscFrUniDlciDiscCongestedToIfBytes = _MscFrUniDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 24),
    _MscFrUniDlciDiscCongestedToIfBytes_Type()
)
mscFrUniDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscCongestedToIfBytes.setStatus("mandatory")


class _MscFrUniDlciDiscDeCongestedToIfBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscDeCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscDeCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
mscFrUniDlciDiscDeCongestedToIfBytes = _MscFrUniDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 25),
    _MscFrUniDlciDiscDeCongestedToIfBytes_Type()
)
mscFrUniDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscDeCongestedToIfBytes.setStatus("mandatory")


class _MscFrUniDlciBytesFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciBytesFromIf_Object = MibTableColumn
mscFrUniDlciBytesFromIf = _MscFrUniDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 26),
    _MscFrUniDlciBytesFromIf_Type()
)
mscFrUniDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciBytesFromIf.setStatus("mandatory")


class _MscFrUniDlciDeBytesFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciDeBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDeBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciDeBytesFromIf_Object = MibTableColumn
mscFrUniDlciDeBytesFromIf = _MscFrUniDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 27),
    _MscFrUniDlciDeBytesFromIf_Type()
)
mscFrUniDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDeBytesFromIf.setStatus("mandatory")


class _MscFrUniDlciExcessBytesFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciExcessBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciExcessBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciExcessBytesFromIf_Object = MibTableColumn
mscFrUniDlciExcessBytesFromIf = _MscFrUniDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 28),
    _MscFrUniDlciExcessBytesFromIf_Type()
)
mscFrUniDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciExcessBytesFromIf.setStatus("mandatory")


class _MscFrUniDlciDiscExcessFromIfBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscExcessFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscExcessFromIfBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscExcessFromIfBytes_Object = MibTableColumn
mscFrUniDlciDiscExcessFromIfBytes = _MscFrUniDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 29),
    _MscFrUniDlciDiscExcessFromIfBytes_Type()
)
mscFrUniDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscExcessFromIfBytes.setStatus("mandatory")


class _MscFrUniDlciDiscByteAbit_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscByteAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscByteAbit_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscByteAbit_Object = MibTableColumn
mscFrUniDlciDiscByteAbit = _MscFrUniDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 30),
    _MscFrUniDlciDiscByteAbit_Type()
)
mscFrUniDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscByteAbit.setStatus("mandatory")


class _MscFrUniDlciDiscCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscCongestedFromIfBytes_Object = MibTableColumn
mscFrUniDlciDiscCongestedFromIfBytes = _MscFrUniDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 31),
    _MscFrUniDlciDiscCongestedFromIfBytes_Type()
)
mscFrUniDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscCongestedFromIfBytes.setStatus("mandatory")


class _MscFrUniDlciDiscDeCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscDeCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscDeCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
mscFrUniDlciDiscDeCongestedFromIfBytes = _MscFrUniDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 32),
    _MscFrUniDlciDiscDeCongestedFromIfBytes_Type()
)
mscFrUniDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")


class _MscFrUniDlciErrorShortBytesFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciErrorShortBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciErrorShortBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciErrorShortBytesFromIf_Object = MibTableColumn
mscFrUniDlciErrorShortBytesFromIf = _MscFrUniDlciErrorShortBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 33),
    _MscFrUniDlciErrorShortBytesFromIf_Type()
)
mscFrUniDlciErrorShortBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciErrorShortBytesFromIf.setStatus("mandatory")


class _MscFrUniDlciErrorLongBytesFromIf_Type(Unsigned32):
    """Custom type mscFrUniDlciErrorLongBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciErrorLongBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrUniDlciErrorLongBytesFromIf_Object = MibTableColumn
mscFrUniDlciErrorLongBytesFromIf = _MscFrUniDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 34),
    _MscFrUniDlciErrorLongBytesFromIf_Type()
)
mscFrUniDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciErrorLongBytesFromIf.setStatus("mandatory")


class _MscFrUniDlciRateAdaptReduct_Type(Unsigned32):
    """Custom type mscFrUniDlciRateAdaptReduct based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciRateAdaptReduct_Type.__name__ = "Unsigned32"
_MscFrUniDlciRateAdaptReduct_Object = MibTableColumn
mscFrUniDlciRateAdaptReduct = _MscFrUniDlciRateAdaptReduct_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 35),
    _MscFrUniDlciRateAdaptReduct_Type()
)
mscFrUniDlciRateAdaptReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciRateAdaptReduct.setStatus("mandatory")


class _MscFrUniDlciRateAdaptReductPeriod_Type(Unsigned32):
    """Custom type mscFrUniDlciRateAdaptReductPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciRateAdaptReductPeriod_Type.__name__ = "Unsigned32"
_MscFrUniDlciRateAdaptReductPeriod_Object = MibTableColumn
mscFrUniDlciRateAdaptReductPeriod = _MscFrUniDlciRateAdaptReductPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 36),
    _MscFrUniDlciRateAdaptReductPeriod_Type()
)
mscFrUniDlciRateAdaptReductPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciRateAdaptReductPeriod.setStatus("mandatory")


class _MscFrUniDlciTransferPriorityToNetwork_Type(Integer32):
    """Custom type mscFrUniDlciTransferPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniDlciTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MscFrUniDlciTransferPriorityToNetwork_Object = MibTableColumn
mscFrUniDlciTransferPriorityToNetwork = _MscFrUniDlciTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 37),
    _MscFrUniDlciTransferPriorityToNetwork_Type()
)
mscFrUniDlciTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTransferPriorityToNetwork.setStatus("obsolete")


class _MscFrUniDlciTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mscFrUniDlciTransferPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniDlciTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MscFrUniDlciTransferPriorityFromNetwork_Object = MibTableColumn
mscFrUniDlciTransferPriorityFromNetwork = _MscFrUniDlciTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 38),
    _MscFrUniDlciTransferPriorityFromNetwork_Type()
)
mscFrUniDlciTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTransferPriorityFromNetwork.setStatus("obsolete")


class _MscFrUniDlciCirPresent_Type(Unsigned32):
    """Custom type mscFrUniDlciCirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciCirPresent_Type.__name__ = "Unsigned32"
_MscFrUniDlciCirPresent_Object = MibTableColumn
mscFrUniDlciCirPresent = _MscFrUniDlciCirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 39),
    _MscFrUniDlciCirPresent_Type()
)
mscFrUniDlciCirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCirPresent.setStatus("mandatory")


class _MscFrUniDlciEirPresent_Type(Unsigned32):
    """Custom type mscFrUniDlciEirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciEirPresent_Type.__name__ = "Unsigned32"
_MscFrUniDlciEirPresent_Object = MibTableColumn
mscFrUniDlciEirPresent = _MscFrUniDlciEirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 15, 1, 40),
    _MscFrUniDlciEirPresent_Type()
)
mscFrUniDlciEirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEirPresent.setStatus("mandatory")
_MscFrUniDlciIntTable_Object = MibTable
mscFrUniDlciIntTable = _MscFrUniDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16)
)
if mibBuilder.loadTexts:
    mscFrUniDlciIntTable.setStatus("mandatory")
_MscFrUniDlciIntEntry_Object = MibTableRow
mscFrUniDlciIntEntry = _MscFrUniDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1)
)
mscFrUniDlciIntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniDlciIntEntry.setStatus("mandatory")


class _MscFrUniDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrUniDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrUniDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrUniDlciStartTime_Object = MibTableColumn
mscFrUniDlciStartTime = _MscFrUniDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 1),
    _MscFrUniDlciStartTime_Type()
)
mscFrUniDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciStartTime.setStatus("mandatory")


class _MscFrUniDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type mscFrUniDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrUniDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_MscFrUniDlciTotalIngressBytes_Object = MibTableColumn
mscFrUniDlciTotalIngressBytes = _MscFrUniDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 2),
    _MscFrUniDlciTotalIngressBytes_Type()
)
mscFrUniDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTotalIngressBytes.setStatus("mandatory")


class _MscFrUniDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type mscFrUniDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrUniDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_MscFrUniDlciTotalEgressBytes_Object = MibTableColumn
mscFrUniDlciTotalEgressBytes = _MscFrUniDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 3),
    _MscFrUniDlciTotalEgressBytes_Type()
)
mscFrUniDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTotalEgressBytes.setStatus("mandatory")


class _MscFrUniDlciEirIngressBytes_Type(Unsigned64):
    """Custom type mscFrUniDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrUniDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_MscFrUniDlciEirIngressBytes_Object = MibTableColumn
mscFrUniDlciEirIngressBytes = _MscFrUniDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 4),
    _MscFrUniDlciEirIngressBytes_Type()
)
mscFrUniDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEirIngressBytes.setStatus("mandatory")


class _MscFrUniDlciEirEgressBytes_Type(Unsigned64):
    """Custom type mscFrUniDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrUniDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_MscFrUniDlciEirEgressBytes_Object = MibTableColumn
mscFrUniDlciEirEgressBytes = _MscFrUniDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 5),
    _MscFrUniDlciEirEgressBytes_Type()
)
mscFrUniDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEirEgressBytes.setStatus("mandatory")


class _MscFrUniDlciDiscardedBytes_Type(Unsigned64):
    """Custom type mscFrUniDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrUniDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_MscFrUniDlciDiscardedBytes_Object = MibTableColumn
mscFrUniDlciDiscardedBytes = _MscFrUniDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 6),
    _MscFrUniDlciDiscardedBytes_Type()
)
mscFrUniDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscardedBytes.setStatus("mandatory")


class _MscFrUniDlciTotalIngressSegFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciTotalIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciTotalIngressSegFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciTotalIngressSegFrm_Object = MibTableColumn
mscFrUniDlciTotalIngressSegFrm = _MscFrUniDlciTotalIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 7),
    _MscFrUniDlciTotalIngressSegFrm_Type()
)
mscFrUniDlciTotalIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTotalIngressSegFrm.setStatus("mandatory")


class _MscFrUniDlciTotalEgressSegFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciTotalEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciTotalEgressSegFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciTotalEgressSegFrm_Object = MibTableColumn
mscFrUniDlciTotalEgressSegFrm = _MscFrUniDlciTotalEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 8),
    _MscFrUniDlciTotalEgressSegFrm_Type()
)
mscFrUniDlciTotalEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciTotalEgressSegFrm.setStatus("mandatory")


class _MscFrUniDlciEirIngressSegFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciEirIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciEirIngressSegFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciEirIngressSegFrm_Object = MibTableColumn
mscFrUniDlciEirIngressSegFrm = _MscFrUniDlciEirIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 9),
    _MscFrUniDlciEirIngressSegFrm_Type()
)
mscFrUniDlciEirIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEirIngressSegFrm.setStatus("mandatory")


class _MscFrUniDlciEirEgressSegFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciEirEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciEirEgressSegFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciEirEgressSegFrm_Object = MibTableColumn
mscFrUniDlciEirEgressSegFrm = _MscFrUniDlciEirEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 10),
    _MscFrUniDlciEirEgressSegFrm_Type()
)
mscFrUniDlciEirEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEirEgressSegFrm.setStatus("mandatory")


class _MscFrUniDlciDiscardedSegFrm_Type(Unsigned32):
    """Custom type mscFrUniDlciDiscardedSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciDiscardedSegFrm_Type.__name__ = "Unsigned32"
_MscFrUniDlciDiscardedSegFrm_Object = MibTableColumn
mscFrUniDlciDiscardedSegFrm = _MscFrUniDlciDiscardedSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 11),
    _MscFrUniDlciDiscardedSegFrm_Type()
)
mscFrUniDlciDiscardedSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciDiscardedSegFrm.setStatus("mandatory")


class _MscFrUniDlciCirPresentObs_Type(Unsigned32):
    """Custom type mscFrUniDlciCirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciCirPresentObs_Type.__name__ = "Unsigned32"
_MscFrUniDlciCirPresentObs_Object = MibTableColumn
mscFrUniDlciCirPresentObs = _MscFrUniDlciCirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 12),
    _MscFrUniDlciCirPresentObs_Type()
)
mscFrUniDlciCirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCirPresentObs.setStatus("obsolete")


class _MscFrUniDlciEirPresentObs_Type(Unsigned32):
    """Custom type mscFrUniDlciEirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciEirPresentObs_Type.__name__ = "Unsigned32"
_MscFrUniDlciEirPresentObs_Object = MibTableColumn
mscFrUniDlciEirPresentObs = _MscFrUniDlciEirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 13),
    _MscFrUniDlciEirPresentObs_Type()
)
mscFrUniDlciEirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciEirPresentObs.setStatus("obsolete")


class _MscFrUniDlciRateEnforcementPresent_Type(Integer32):
    """Custom type mscFrUniDlciRateEnforcementPresent based on Integer32"""
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


_MscFrUniDlciRateEnforcementPresent_Type.__name__ = "Integer32"
_MscFrUniDlciRateEnforcementPresent_Object = MibTableColumn
mscFrUniDlciRateEnforcementPresent = _MscFrUniDlciRateEnforcementPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 14),
    _MscFrUniDlciRateEnforcementPresent_Type()
)
mscFrUniDlciRateEnforcementPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciRateEnforcementPresent.setStatus("obsolete")


class _MscFrUniDlciRateAdaptationPresent_Type(Integer32):
    """Custom type mscFrUniDlciRateAdaptationPresent based on Integer32"""
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


_MscFrUniDlciRateAdaptationPresent_Type.__name__ = "Integer32"
_MscFrUniDlciRateAdaptationPresent_Object = MibTableColumn
mscFrUniDlciRateAdaptationPresent = _MscFrUniDlciRateAdaptationPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 15),
    _MscFrUniDlciRateAdaptationPresent_Type()
)
mscFrUniDlciRateAdaptationPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciRateAdaptationPresent.setStatus("obsolete")


class _MscFrUniDlciLocalRateAdaptOccurred_Type(Integer32):
    """Custom type mscFrUniDlciLocalRateAdaptOccurred based on Integer32"""
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


_MscFrUniDlciLocalRateAdaptOccurred_Type.__name__ = "Integer32"
_MscFrUniDlciLocalRateAdaptOccurred_Object = MibTableColumn
mscFrUniDlciLocalRateAdaptOccurred = _MscFrUniDlciLocalRateAdaptOccurred_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 16),
    _MscFrUniDlciLocalRateAdaptOccurred_Type()
)
mscFrUniDlciLocalRateAdaptOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciLocalRateAdaptOccurred.setStatus("mandatory")


class _MscFrUniDlciCallReferenceNumber_Type(Hex):
    """Custom type mscFrUniDlciCallReferenceNumber based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrUniDlciCallReferenceNumber_Type.__name__ = "Hex"
_MscFrUniDlciCallReferenceNumber_Object = MibTableColumn
mscFrUniDlciCallReferenceNumber = _MscFrUniDlciCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 17),
    _MscFrUniDlciCallReferenceNumber_Type()
)
mscFrUniDlciCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCallReferenceNumber.setStatus("obsolete")


class _MscFrUniDlciElapsedDifference_Type(Unsigned32):
    """Custom type mscFrUniDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciElapsedDifference_Type.__name__ = "Unsigned32"
_MscFrUniDlciElapsedDifference_Object = MibTableColumn
mscFrUniDlciElapsedDifference = _MscFrUniDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 18),
    _MscFrUniDlciElapsedDifference_Type()
)
mscFrUniDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciElapsedDifference.setStatus("mandatory")


class _MscFrUniDlciCallRefNumber_Type(Unsigned32):
    """Custom type mscFrUniDlciCallRefNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniDlciCallRefNumber_Type.__name__ = "Unsigned32"
_MscFrUniDlciCallRefNumber_Object = MibTableColumn
mscFrUniDlciCallRefNumber = _MscFrUniDlciCallRefNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 5, 16, 1, 20),
    _MscFrUniDlciCallRefNumber_Type()
)
mscFrUniDlciCallRefNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniDlciCallRefNumber.setStatus("mandatory")
_MscFrUniSig_ObjectIdentity = ObjectIdentity
mscFrUniSig = _MscFrUniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6)
)
_MscFrUniSigRowStatusTable_Object = MibTable
mscFrUniSigRowStatusTable = _MscFrUniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 1)
)
if mibBuilder.loadTexts:
    mscFrUniSigRowStatusTable.setStatus("mandatory")
_MscFrUniSigRowStatusEntry_Object = MibTableRow
mscFrUniSigRowStatusEntry = _MscFrUniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 1, 1)
)
mscFrUniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigRowStatusEntry.setStatus("mandatory")
_MscFrUniSigRowStatus_Type = RowStatus
_MscFrUniSigRowStatus_Object = MibTableColumn
mscFrUniSigRowStatus = _MscFrUniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 1, 1, 1),
    _MscFrUniSigRowStatus_Type()
)
mscFrUniSigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigRowStatus.setStatus("mandatory")
_MscFrUniSigComponentName_Type = DisplayString
_MscFrUniSigComponentName_Object = MibTableColumn
mscFrUniSigComponentName = _MscFrUniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 1, 1, 2),
    _MscFrUniSigComponentName_Type()
)
mscFrUniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigComponentName.setStatus("mandatory")
_MscFrUniSigStorageType_Type = StorageType
_MscFrUniSigStorageType_Object = MibTableColumn
mscFrUniSigStorageType = _MscFrUniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 1, 1, 4),
    _MscFrUniSigStorageType_Type()
)
mscFrUniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigStorageType.setStatus("mandatory")
_MscFrUniSigIndex_Type = NonReplicated
_MscFrUniSigIndex_Object = MibTableColumn
mscFrUniSigIndex = _MscFrUniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 1, 1, 10),
    _MscFrUniSigIndex_Type()
)
mscFrUniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniSigIndex.setStatus("mandatory")
_MscFrUniSigRangeTable_Object = MibTable
mscFrUniSigRangeTable = _MscFrUniSigRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 11)
)
if mibBuilder.loadTexts:
    mscFrUniSigRangeTable.setStatus("mandatory")
_MscFrUniSigRangeEntry_Object = MibTableRow
mscFrUniSigRangeEntry = _MscFrUniSigRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 11, 1)
)
mscFrUniSigRangeEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigRangeEntry.setStatus("mandatory")


class _MscFrUniSigHighestPvcDlci_Type(Unsigned32):
    """Custom type mscFrUniSigHighestPvcDlci based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniSigHighestPvcDlci_Type.__name__ = "Unsigned32"
_MscFrUniSigHighestPvcDlci_Object = MibTableColumn
mscFrUniSigHighestPvcDlci = _MscFrUniSigHighestPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 11, 1, 1),
    _MscFrUniSigHighestPvcDlci_Type()
)
mscFrUniSigHighestPvcDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigHighestPvcDlci.setStatus("obsolete")


class _MscFrUniSigHighestPermanentDlci_Type(Unsigned32):
    """Custom type mscFrUniSigHighestPermanentDlci based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniSigHighestPermanentDlci_Type.__name__ = "Unsigned32"
_MscFrUniSigHighestPermanentDlci_Object = MibTableColumn
mscFrUniSigHighestPermanentDlci = _MscFrUniSigHighestPermanentDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 11, 1, 4),
    _MscFrUniSigHighestPermanentDlci_Type()
)
mscFrUniSigHighestPermanentDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigHighestPermanentDlci.setStatus("obsolete")


class _MscFrUniSigHighestFriPvcDlci_Type(Unsigned32):
    """Custom type mscFrUniSigHighestFriPvcDlci based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniSigHighestFriPvcDlci_Type.__name__ = "Unsigned32"
_MscFrUniSigHighestFriPvcDlci_Object = MibTableColumn
mscFrUniSigHighestFriPvcDlci = _MscFrUniSigHighestFriPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 11, 1, 5),
    _MscFrUniSigHighestFriPvcDlci_Type()
)
mscFrUniSigHighestFriPvcDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigHighestFriPvcDlci.setStatus("mandatory")
_MscFrUniSigServParmsTable_Object = MibTable
mscFrUniSigServParmsTable = _MscFrUniSigServParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12)
)
if mibBuilder.loadTexts:
    mscFrUniSigServParmsTable.setStatus("mandatory")
_MscFrUniSigServParmsEntry_Object = MibTableRow
mscFrUniSigServParmsEntry = _MscFrUniSigServParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1)
)
mscFrUniSigServParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigServParmsEntry.setStatus("mandatory")


class _MscFrUniSigMaximumAggregateSvcCir_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcCir based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscFrUniSigMaximumAggregateSvcCir_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcCir_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcCir = _MscFrUniSigMaximumAggregateSvcCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 1),
    _MscFrUniSigMaximumAggregateSvcCir_Type()
)
mscFrUniSigMaximumAggregateSvcCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcCir.setStatus("obsolete")


class _MscFrUniSigMaximumAggregateSvcEir_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcEir based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigMaximumAggregateSvcEir_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcEir_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcEir = _MscFrUniSigMaximumAggregateSvcEir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 2),
    _MscFrUniSigMaximumAggregateSvcEir_Type()
)
mscFrUniSigMaximumAggregateSvcEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcEir.setStatus("obsolete")


class _MscFrUniSigMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumFrameSize based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrUniSigMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumFrameSize_Object = MibTableColumn
mscFrUniSigMaximumFrameSize = _MscFrUniSigMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 3),
    _MscFrUniSigMaximumFrameSize_Type()
)
mscFrUniSigMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumFrameSize.setStatus("mandatory")


class _MscFrUniSigDefaultMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrUniSigDefaultMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrUniSigDefaultMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrUniSigDefaultMaximumFrameSize_Object = MibTableColumn
mscFrUniSigDefaultMaximumFrameSize = _MscFrUniSigDefaultMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 4),
    _MscFrUniSigDefaultMaximumFrameSize_Type()
)
mscFrUniSigDefaultMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigDefaultMaximumFrameSize.setStatus("mandatory")


class _MscFrUniSigDefaultCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrUniSigDefaultCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrUniSigDefaultCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrUniSigDefaultCommittedInformationRate_Object = MibTableColumn
mscFrUniSigDefaultCommittedInformationRate = _MscFrUniSigDefaultCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 5),
    _MscFrUniSigDefaultCommittedInformationRate_Type()
)
mscFrUniSigDefaultCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigDefaultCommittedInformationRate.setStatus("mandatory")


class _MscFrUniSigDefaultCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrUniSigDefaultCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrUniSigDefaultCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrUniSigDefaultCommittedBurstSize_Object = MibTableColumn
mscFrUniSigDefaultCommittedBurstSize = _MscFrUniSigDefaultCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 6),
    _MscFrUniSigDefaultCommittedBurstSize_Type()
)
mscFrUniSigDefaultCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigDefaultCommittedBurstSize.setStatus("mandatory")


class _MscFrUniSigDefaultExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrUniSigDefaultExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrUniSigDefaultExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrUniSigDefaultExcessBurstSize_Object = MibTableColumn
mscFrUniSigDefaultExcessBurstSize = _MscFrUniSigDefaultExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 7),
    _MscFrUniSigDefaultExcessBurstSize_Type()
)
mscFrUniSigDefaultExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigDefaultExcessBurstSize.setStatus("mandatory")


class _MscFrUniSigUnlimitedAggregateEir_Type(Integer32):
    """Custom type mscFrUniSigUnlimitedAggregateEir based on Integer32"""
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


_MscFrUniSigUnlimitedAggregateEir_Type.__name__ = "Integer32"
_MscFrUniSigUnlimitedAggregateEir_Object = MibTableColumn
mscFrUniSigUnlimitedAggregateEir = _MscFrUniSigUnlimitedAggregateEir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 8),
    _MscFrUniSigUnlimitedAggregateEir_Type()
)
mscFrUniSigUnlimitedAggregateEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigUnlimitedAggregateEir.setStatus("obsolete")


class _MscFrUniSigRateEnforcement_Type(Integer32):
    """Custom type mscFrUniSigRateEnforcement based on Integer32"""
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


_MscFrUniSigRateEnforcement_Type.__name__ = "Integer32"
_MscFrUniSigRateEnforcement_Object = MibTableColumn
mscFrUniSigRateEnforcement = _MscFrUniSigRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 9),
    _MscFrUniSigRateEnforcement_Type()
)
mscFrUniSigRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigRateEnforcement.setStatus("mandatory")


class _MscFrUniSigRateAdaptation_Type(Integer32):
    """Custom type mscFrUniSigRateAdaptation based on Integer32"""
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


_MscFrUniSigRateAdaptation_Type.__name__ = "Integer32"
_MscFrUniSigRateAdaptation_Object = MibTableColumn
mscFrUniSigRateAdaptation = _MscFrUniSigRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 10),
    _MscFrUniSigRateAdaptation_Type()
)
mscFrUniSigRateAdaptation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigRateAdaptation.setStatus("mandatory")


class _MscFrUniSigMaximumAggregateSvcCirNormalQ_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcCirNormalQ based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscFrUniSigMaximumAggregateSvcCirNormalQ_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcCirNormalQ_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcCirNormalQ = _MscFrUniSigMaximumAggregateSvcCirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 11),
    _MscFrUniSigMaximumAggregateSvcCirNormalQ_Type()
)
mscFrUniSigMaximumAggregateSvcCirNormalQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcCirNormalQ.setStatus("obsolete")


class _MscFrUniSigMaximumAggregateSvcCirHighQ_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcCirHighQ based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscFrUniSigMaximumAggregateSvcCirHighQ_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcCirHighQ_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcCirHighQ = _MscFrUniSigMaximumAggregateSvcCirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 12),
    _MscFrUniSigMaximumAggregateSvcCirHighQ_Type()
)
mscFrUniSigMaximumAggregateSvcCirHighQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcCirHighQ.setStatus("obsolete")


class _MscFrUniSigMaximumAggregateSvcCirInterruptQ_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcCirInterruptQ based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscFrUniSigMaximumAggregateSvcCirInterruptQ_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcCirInterruptQ_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcCirInterruptQ = _MscFrUniSigMaximumAggregateSvcCirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 13),
    _MscFrUniSigMaximumAggregateSvcCirInterruptQ_Type()
)
mscFrUniSigMaximumAggregateSvcCirInterruptQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcCirInterruptQ.setStatus("obsolete")


class _MscFrUniSigMaximumAggregateSvcEirNormalQ_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcEirNormalQ based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigMaximumAggregateSvcEirNormalQ_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcEirNormalQ_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcEirNormalQ = _MscFrUniSigMaximumAggregateSvcEirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 14),
    _MscFrUniSigMaximumAggregateSvcEirNormalQ_Type()
)
mscFrUniSigMaximumAggregateSvcEirNormalQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcEirNormalQ.setStatus("obsolete")


class _MscFrUniSigMaximumAggregateSvcEirHighQ_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcEirHighQ based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigMaximumAggregateSvcEirHighQ_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcEirHighQ_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcEirHighQ = _MscFrUniSigMaximumAggregateSvcEirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 15),
    _MscFrUniSigMaximumAggregateSvcEirHighQ_Type()
)
mscFrUniSigMaximumAggregateSvcEirHighQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcEirHighQ.setStatus("obsolete")


class _MscFrUniSigMaximumAggregateSvcEirInterruptQ_Type(Unsigned32):
    """Custom type mscFrUniSigMaximumAggregateSvcEirInterruptQ based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigMaximumAggregateSvcEirInterruptQ_Type.__name__ = "Unsigned32"
_MscFrUniSigMaximumAggregateSvcEirInterruptQ_Object = MibTableColumn
mscFrUniSigMaximumAggregateSvcEirInterruptQ = _MscFrUniSigMaximumAggregateSvcEirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 16),
    _MscFrUniSigMaximumAggregateSvcEirInterruptQ_Type()
)
mscFrUniSigMaximumAggregateSvcEirInterruptQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigMaximumAggregateSvcEirInterruptQ.setStatus("obsolete")


class _MscFrUniSigX213IeHandling_Type(Integer32):
    """Custom type mscFrUniSigX213IeHandling based on Integer32"""
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


_MscFrUniSigX213IeHandling_Type.__name__ = "Integer32"
_MscFrUniSigX213IeHandling_Object = MibTableColumn
mscFrUniSigX213IeHandling = _MscFrUniSigX213IeHandling_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 17),
    _MscFrUniSigX213IeHandling_Type()
)
mscFrUniSigX213IeHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigX213IeHandling.setStatus("mandatory")


class _MscFrUniSigRaSensitivity_Type(Unsigned32):
    """Custom type mscFrUniSigRaSensitivity based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscFrUniSigRaSensitivity_Type.__name__ = "Unsigned32"
_MscFrUniSigRaSensitivity_Object = MibTableColumn
mscFrUniSigRaSensitivity = _MscFrUniSigRaSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 18),
    _MscFrUniSigRaSensitivity_Type()
)
mscFrUniSigRaSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigRaSensitivity.setStatus("mandatory")


class _MscFrUniSigUpdateBCI_Type(Integer32):
    """Custom type mscFrUniSigUpdateBCI based on Integer32"""
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


_MscFrUniSigUpdateBCI_Type.__name__ = "Integer32"
_MscFrUniSigUpdateBCI_Object = MibTableColumn
mscFrUniSigUpdateBCI = _MscFrUniSigUpdateBCI_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 19),
    _MscFrUniSigUpdateBCI_Type()
)
mscFrUniSigUpdateBCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigUpdateBCI.setStatus("mandatory")


class _MscFrUniSigDefaultLocCheck_Type(Integer32):
    """Custom type mscFrUniSigDefaultLocCheck based on Integer32"""
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


_MscFrUniSigDefaultLocCheck_Type.__name__ = "Integer32"
_MscFrUniSigDefaultLocCheck_Object = MibTableColumn
mscFrUniSigDefaultLocCheck = _MscFrUniSigDefaultLocCheck_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 12, 1, 20),
    _MscFrUniSigDefaultLocCheck_Type()
)
mscFrUniSigDefaultLocCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigDefaultLocCheck.setStatus("mandatory")
_MscFrUniSigSysParmsTable_Object = MibTable
mscFrUniSigSysParmsTable = _MscFrUniSigSysParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13)
)
if mibBuilder.loadTexts:
    mscFrUniSigSysParmsTable.setStatus("mandatory")
_MscFrUniSigSysParmsEntry_Object = MibTableRow
mscFrUniSigSysParmsEntry = _MscFrUniSigSysParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1)
)
mscFrUniSigSysParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigSysParmsEntry.setStatus("mandatory")


class _MscFrUniSigCallSetupTimer_Type(Unsigned32):
    """Custom type mscFrUniSigCallSetupTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniSigCallSetupTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigCallSetupTimer_Object = MibTableColumn
mscFrUniSigCallSetupTimer = _MscFrUniSigCallSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 1),
    _MscFrUniSigCallSetupTimer_Type()
)
mscFrUniSigCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigCallSetupTimer.setStatus("mandatory")


class _MscFrUniSigDisconnectTimer_Type(Unsigned32):
    """Custom type mscFrUniSigDisconnectTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniSigDisconnectTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigDisconnectTimer_Object = MibTableColumn
mscFrUniSigDisconnectTimer = _MscFrUniSigDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 2),
    _MscFrUniSigDisconnectTimer_Type()
)
mscFrUniSigDisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigDisconnectTimer.setStatus("mandatory")


class _MscFrUniSigReleaseTimer_Type(Unsigned32):
    """Custom type mscFrUniSigReleaseTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniSigReleaseTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigReleaseTimer_Object = MibTableColumn
mscFrUniSigReleaseTimer = _MscFrUniSigReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 3),
    _MscFrUniSigReleaseTimer_Type()
)
mscFrUniSigReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigReleaseTimer.setStatus("mandatory")


class _MscFrUniSigCallProceedingTimer_Type(Unsigned32):
    """Custom type mscFrUniSigCallProceedingTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniSigCallProceedingTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigCallProceedingTimer_Object = MibTableColumn
mscFrUniSigCallProceedingTimer = _MscFrUniSigCallProceedingTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 4),
    _MscFrUniSigCallProceedingTimer_Type()
)
mscFrUniSigCallProceedingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigCallProceedingTimer.setStatus("mandatory")


class _MscFrUniSigNetworkType_Type(Integer32):
    """Custom type mscFrUniSigNetworkType based on Integer32"""
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


_MscFrUniSigNetworkType_Type.__name__ = "Integer32"
_MscFrUniSigNetworkType_Object = MibTableColumn
mscFrUniSigNetworkType = _MscFrUniSigNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 5),
    _MscFrUniSigNetworkType_Type()
)
mscFrUniSigNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigNetworkType.setStatus("mandatory")


class _MscFrUniSigRestartReqTimer_Type(Unsigned32):
    """Custom type mscFrUniSigRestartReqTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniSigRestartReqTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigRestartReqTimer_Object = MibTableColumn
mscFrUniSigRestartReqTimer = _MscFrUniSigRestartReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 6),
    _MscFrUniSigRestartReqTimer_Type()
)
mscFrUniSigRestartReqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigRestartReqTimer.setStatus("mandatory")


class _MscFrUniSigRestartRcvTimer_Type(Unsigned32):
    """Custom type mscFrUniSigRestartRcvTimer based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniSigRestartRcvTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigRestartRcvTimer_Object = MibTableColumn
mscFrUniSigRestartRcvTimer = _MscFrUniSigRestartRcvTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 7),
    _MscFrUniSigRestartRcvTimer_Type()
)
mscFrUniSigRestartRcvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigRestartRcvTimer.setStatus("mandatory")


class _MscFrUniSigStatusEnqTimer_Type(Unsigned32):
    """Custom type mscFrUniSigStatusEnqTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrUniSigStatusEnqTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigStatusEnqTimer_Object = MibTableColumn
mscFrUniSigStatusEnqTimer = _MscFrUniSigStatusEnqTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 13, 1, 8),
    _MscFrUniSigStatusEnqTimer_Type()
)
mscFrUniSigStatusEnqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigStatusEnqTimer.setStatus("mandatory")
_MscFrUniSigLapfSysTable_Object = MibTable
mscFrUniSigLapfSysTable = _MscFrUniSigLapfSysTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 14)
)
if mibBuilder.loadTexts:
    mscFrUniSigLapfSysTable.setStatus("mandatory")
_MscFrUniSigLapfSysEntry_Object = MibTableRow
mscFrUniSigLapfSysEntry = _MscFrUniSigLapfSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 14, 1)
)
mscFrUniSigLapfSysEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigLapfSysEntry.setStatus("mandatory")


class _MscFrUniSigWindowSize_Type(Unsigned32):
    """Custom type mscFrUniSigWindowSize based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscFrUniSigWindowSize_Type.__name__ = "Unsigned32"
_MscFrUniSigWindowSize_Object = MibTableColumn
mscFrUniSigWindowSize = _MscFrUniSigWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 14, 1, 2),
    _MscFrUniSigWindowSize_Type()
)
mscFrUniSigWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigWindowSize.setStatus("mandatory")


class _MscFrUniSigRetransmitLimit_Type(Unsigned32):
    """Custom type mscFrUniSigRetransmitLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MscFrUniSigRetransmitLimit_Type.__name__ = "Unsigned32"
_MscFrUniSigRetransmitLimit_Object = MibTableColumn
mscFrUniSigRetransmitLimit = _MscFrUniSigRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 14, 1, 3),
    _MscFrUniSigRetransmitLimit_Type()
)
mscFrUniSigRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigRetransmitLimit.setStatus("mandatory")


class _MscFrUniSigAckTimer_Type(Unsigned32):
    """Custom type mscFrUniSigAckTimer based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_MscFrUniSigAckTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigAckTimer_Object = MibTableColumn
mscFrUniSigAckTimer = _MscFrUniSigAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 14, 1, 4),
    _MscFrUniSigAckTimer_Type()
)
mscFrUniSigAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigAckTimer.setStatus("mandatory")


class _MscFrUniSigAckDelayTimer_Type(Unsigned32):
    """Custom type mscFrUniSigAckDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscFrUniSigAckDelayTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigAckDelayTimer_Object = MibTableColumn
mscFrUniSigAckDelayTimer = _MscFrUniSigAckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 14, 1, 5),
    _MscFrUniSigAckDelayTimer_Type()
)
mscFrUniSigAckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigAckDelayTimer.setStatus("mandatory")


class _MscFrUniSigIdleProbeTimer_Type(Unsigned32):
    """Custom type mscFrUniSigIdleProbeTimer based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_MscFrUniSigIdleProbeTimer_Type.__name__ = "Unsigned32"
_MscFrUniSigIdleProbeTimer_Object = MibTableColumn
mscFrUniSigIdleProbeTimer = _MscFrUniSigIdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 14, 1, 6),
    _MscFrUniSigIdleProbeTimer_Type()
)
mscFrUniSigIdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigIdleProbeTimer.setStatus("mandatory")
_MscFrUniSigStateTable_Object = MibTable
mscFrUniSigStateTable = _MscFrUniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 15)
)
if mibBuilder.loadTexts:
    mscFrUniSigStateTable.setStatus("mandatory")
_MscFrUniSigStateEntry_Object = MibTableRow
mscFrUniSigStateEntry = _MscFrUniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 15, 1)
)
mscFrUniSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigStateEntry.setStatus("mandatory")


class _MscFrUniSigAdminState_Type(Integer32):
    """Custom type mscFrUniSigAdminState based on Integer32"""
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


_MscFrUniSigAdminState_Type.__name__ = "Integer32"
_MscFrUniSigAdminState_Object = MibTableColumn
mscFrUniSigAdminState = _MscFrUniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 15, 1, 1),
    _MscFrUniSigAdminState_Type()
)
mscFrUniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigAdminState.setStatus("mandatory")


class _MscFrUniSigOperationalState_Type(Integer32):
    """Custom type mscFrUniSigOperationalState based on Integer32"""
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


_MscFrUniSigOperationalState_Type.__name__ = "Integer32"
_MscFrUniSigOperationalState_Object = MibTableColumn
mscFrUniSigOperationalState = _MscFrUniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 15, 1, 2),
    _MscFrUniSigOperationalState_Type()
)
mscFrUniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigOperationalState.setStatus("mandatory")


class _MscFrUniSigUsageState_Type(Integer32):
    """Custom type mscFrUniSigUsageState based on Integer32"""
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


_MscFrUniSigUsageState_Type.__name__ = "Integer32"
_MscFrUniSigUsageState_Object = MibTableColumn
mscFrUniSigUsageState = _MscFrUniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 15, 1, 3),
    _MscFrUniSigUsageState_Type()
)
mscFrUniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigUsageState.setStatus("mandatory")
_MscFrUniSigStatsTable_Object = MibTable
mscFrUniSigStatsTable = _MscFrUniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16)
)
if mibBuilder.loadTexts:
    mscFrUniSigStatsTable.setStatus("mandatory")
_MscFrUniSigStatsEntry_Object = MibTableRow
mscFrUniSigStatsEntry = _MscFrUniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1)
)
mscFrUniSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigStatsEntry.setStatus("mandatory")


class _MscFrUniSigCurrentNumberOfSvcCalls_Type(Gauge32):
    """Custom type mscFrUniSigCurrentNumberOfSvcCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrUniSigCurrentNumberOfSvcCalls_Type.__name__ = "Gauge32"
_MscFrUniSigCurrentNumberOfSvcCalls_Object = MibTableColumn
mscFrUniSigCurrentNumberOfSvcCalls = _MscFrUniSigCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 1),
    _MscFrUniSigCurrentNumberOfSvcCalls_Type()
)
mscFrUniSigCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentNumberOfSvcCalls.setStatus("mandatory")


class _MscFrUniSigInCalls_Type(Gauge32):
    """Custom type mscFrUniSigInCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrUniSigInCalls_Type.__name__ = "Gauge32"
_MscFrUniSigInCalls_Object = MibTableColumn
mscFrUniSigInCalls = _MscFrUniSigInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 4),
    _MscFrUniSigInCalls_Type()
)
mscFrUniSigInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigInCalls.setStatus("mandatory")
_MscFrUniSigInCallsRefused_Type = Counter32
_MscFrUniSigInCallsRefused_Object = MibTableColumn
mscFrUniSigInCallsRefused = _MscFrUniSigInCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 5),
    _MscFrUniSigInCallsRefused_Type()
)
mscFrUniSigInCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigInCallsRefused.setStatus("mandatory")


class _MscFrUniSigOutCalls_Type(Gauge32):
    """Custom type mscFrUniSigOutCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrUniSigOutCalls_Type.__name__ = "Gauge32"
_MscFrUniSigOutCalls_Object = MibTableColumn
mscFrUniSigOutCalls = _MscFrUniSigOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 6),
    _MscFrUniSigOutCalls_Type()
)
mscFrUniSigOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigOutCalls.setStatus("mandatory")
_MscFrUniSigOutCallsFailed_Type = Counter32
_MscFrUniSigOutCallsFailed_Object = MibTableColumn
mscFrUniSigOutCallsFailed = _MscFrUniSigOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 7),
    _MscFrUniSigOutCallsFailed_Type()
)
mscFrUniSigOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigOutCallsFailed.setStatus("mandatory")
_MscFrUniSigProtocolErrors_Type = Counter32
_MscFrUniSigProtocolErrors_Object = MibTableColumn
mscFrUniSigProtocolErrors = _MscFrUniSigProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 8),
    _MscFrUniSigProtocolErrors_Type()
)
mscFrUniSigProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigProtocolErrors.setStatus("mandatory")
_MscFrUniSigQualityOfServiceNotAvailable_Type = Counter32
_MscFrUniSigQualityOfServiceNotAvailable_Object = MibTableColumn
mscFrUniSigQualityOfServiceNotAvailable = _MscFrUniSigQualityOfServiceNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 9),
    _MscFrUniSigQualityOfServiceNotAvailable_Type()
)
mscFrUniSigQualityOfServiceNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigQualityOfServiceNotAvailable.setStatus("mandatory")
_MscFrUniSigSetupTimeout_Type = Counter32
_MscFrUniSigSetupTimeout_Object = MibTableColumn
mscFrUniSigSetupTimeout = _MscFrUniSigSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 10),
    _MscFrUniSigSetupTimeout_Type()
)
mscFrUniSigSetupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigSetupTimeout.setStatus("mandatory")


class _MscFrUniSigLastCauseInStatusMsgReceived_Type(Unsigned32):
    """Custom type mscFrUniSigLastCauseInStatusMsgReceived based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniSigLastCauseInStatusMsgReceived_Type.__name__ = "Unsigned32"
_MscFrUniSigLastCauseInStatusMsgReceived_Object = MibTableColumn
mscFrUniSigLastCauseInStatusMsgReceived = _MscFrUniSigLastCauseInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 11),
    _MscFrUniSigLastCauseInStatusMsgReceived_Type()
)
mscFrUniSigLastCauseInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastCauseInStatusMsgReceived.setStatus("mandatory")


class _MscFrUniSigLastStateInStatusMsgReceived_Type(Integer32):
    """Custom type mscFrUniSigLastStateInStatusMsgReceived based on Integer32"""
    defaultValue = 20

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
          ("n63", 63),
          ("n7", 7),
          ("n8", 8),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseRequest", 19),
          ("restart", 62),
          ("restartRequest", 61))
    )


_MscFrUniSigLastStateInStatusMsgReceived_Type.__name__ = "Integer32"
_MscFrUniSigLastStateInStatusMsgReceived_Object = MibTableColumn
mscFrUniSigLastStateInStatusMsgReceived = _MscFrUniSigLastStateInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 12),
    _MscFrUniSigLastStateInStatusMsgReceived_Type()
)
mscFrUniSigLastStateInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastStateInStatusMsgReceived.setStatus("mandatory")


class _MscFrUniSigLastDlciReceivedStatus_Type(Unsigned32):
    """Custom type mscFrUniSigLastDlciReceivedStatus based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniSigLastDlciReceivedStatus_Type.__name__ = "Unsigned32"
_MscFrUniSigLastDlciReceivedStatus_Object = MibTableColumn
mscFrUniSigLastDlciReceivedStatus = _MscFrUniSigLastDlciReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 13),
    _MscFrUniSigLastDlciReceivedStatus_Type()
)
mscFrUniSigLastDlciReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastDlciReceivedStatus.setStatus("mandatory")


class _MscFrUniSigLastStateReceivedStatus_Type(Integer32):
    """Custom type mscFrUniSigLastStateReceivedStatus based on Integer32"""
    defaultValue = 20

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
              20,
              61,
              62)
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
          ("releaseRequest", 19),
          ("restart", 62),
          ("restartRequest", 61))
    )


_MscFrUniSigLastStateReceivedStatus_Type.__name__ = "Integer32"
_MscFrUniSigLastStateReceivedStatus_Object = MibTableColumn
mscFrUniSigLastStateReceivedStatus = _MscFrUniSigLastStateReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 14),
    _MscFrUniSigLastStateReceivedStatus_Type()
)
mscFrUniSigLastStateReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastStateReceivedStatus.setStatus("obsolete")


class _MscFrUniSigLastTimeMsgBlockCongested_Type(EnterpriseDateAndTime):
    """Custom type mscFrUniSigLastTimeMsgBlockCongested based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_MscFrUniSigLastTimeMsgBlockCongested_Type.__name__ = "EnterpriseDateAndTime"
_MscFrUniSigLastTimeMsgBlockCongested_Object = MibTableColumn
mscFrUniSigLastTimeMsgBlockCongested = _MscFrUniSigLastTimeMsgBlockCongested_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 15),
    _MscFrUniSigLastTimeMsgBlockCongested_Type()
)
mscFrUniSigLastTimeMsgBlockCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastTimeMsgBlockCongested.setStatus("obsolete")


class _MscFrUniSigLastDlciWithMsgBlockCongestion_Type(Unsigned32):
    """Custom type mscFrUniSigLastDlciWithMsgBlockCongestion based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniSigLastDlciWithMsgBlockCongestion_Type.__name__ = "Unsigned32"
_MscFrUniSigLastDlciWithMsgBlockCongestion_Object = MibTableColumn
mscFrUniSigLastDlciWithMsgBlockCongestion = _MscFrUniSigLastDlciWithMsgBlockCongestion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 16),
    _MscFrUniSigLastDlciWithMsgBlockCongestion_Type()
)
mscFrUniSigLastDlciWithMsgBlockCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastDlciWithMsgBlockCongestion.setStatus("obsolete")


class _MscFrUniSigCurrentAggregateSvcCirNormalQ_Type(Unsigned32):
    """Custom type mscFrUniSigCurrentAggregateSvcCirNormalQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigCurrentAggregateSvcCirNormalQ_Type.__name__ = "Unsigned32"
_MscFrUniSigCurrentAggregateSvcCirNormalQ_Object = MibTableColumn
mscFrUniSigCurrentAggregateSvcCirNormalQ = _MscFrUniSigCurrentAggregateSvcCirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 17),
    _MscFrUniSigCurrentAggregateSvcCirNormalQ_Type()
)
mscFrUniSigCurrentAggregateSvcCirNormalQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentAggregateSvcCirNormalQ.setStatus("obsolete")


class _MscFrUniSigCurrentAggregateSvcCirHighQ_Type(Unsigned32):
    """Custom type mscFrUniSigCurrentAggregateSvcCirHighQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigCurrentAggregateSvcCirHighQ_Type.__name__ = "Unsigned32"
_MscFrUniSigCurrentAggregateSvcCirHighQ_Object = MibTableColumn
mscFrUniSigCurrentAggregateSvcCirHighQ = _MscFrUniSigCurrentAggregateSvcCirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 18),
    _MscFrUniSigCurrentAggregateSvcCirHighQ_Type()
)
mscFrUniSigCurrentAggregateSvcCirHighQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentAggregateSvcCirHighQ.setStatus("obsolete")


class _MscFrUniSigCurrentAggregateSvcCirInterruptQ_Type(Unsigned32):
    """Custom type mscFrUniSigCurrentAggregateSvcCirInterruptQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigCurrentAggregateSvcCirInterruptQ_Type.__name__ = "Unsigned32"
_MscFrUniSigCurrentAggregateSvcCirInterruptQ_Object = MibTableColumn
mscFrUniSigCurrentAggregateSvcCirInterruptQ = _MscFrUniSigCurrentAggregateSvcCirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 19),
    _MscFrUniSigCurrentAggregateSvcCirInterruptQ_Type()
)
mscFrUniSigCurrentAggregateSvcCirInterruptQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentAggregateSvcCirInterruptQ.setStatus("obsolete")


class _MscFrUniSigCurrentAggregateSvcEirNormalQ_Type(Unsigned32):
    """Custom type mscFrUniSigCurrentAggregateSvcEirNormalQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigCurrentAggregateSvcEirNormalQ_Type.__name__ = "Unsigned32"
_MscFrUniSigCurrentAggregateSvcEirNormalQ_Object = MibTableColumn
mscFrUniSigCurrentAggregateSvcEirNormalQ = _MscFrUniSigCurrentAggregateSvcEirNormalQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 20),
    _MscFrUniSigCurrentAggregateSvcEirNormalQ_Type()
)
mscFrUniSigCurrentAggregateSvcEirNormalQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentAggregateSvcEirNormalQ.setStatus("obsolete")


class _MscFrUniSigCurrentAggregateSvcEirHighQ_Type(Unsigned32):
    """Custom type mscFrUniSigCurrentAggregateSvcEirHighQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigCurrentAggregateSvcEirHighQ_Type.__name__ = "Unsigned32"
_MscFrUniSigCurrentAggregateSvcEirHighQ_Object = MibTableColumn
mscFrUniSigCurrentAggregateSvcEirHighQ = _MscFrUniSigCurrentAggregateSvcEirHighQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 21),
    _MscFrUniSigCurrentAggregateSvcEirHighQ_Type()
)
mscFrUniSigCurrentAggregateSvcEirHighQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentAggregateSvcEirHighQ.setStatus("obsolete")


class _MscFrUniSigCurrentAggregateSvcEirInterruptQ_Type(Unsigned32):
    """Custom type mscFrUniSigCurrentAggregateSvcEirInterruptQ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniSigCurrentAggregateSvcEirInterruptQ_Type.__name__ = "Unsigned32"
_MscFrUniSigCurrentAggregateSvcEirInterruptQ_Object = MibTableColumn
mscFrUniSigCurrentAggregateSvcEirInterruptQ = _MscFrUniSigCurrentAggregateSvcEirInterruptQ_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 16, 1, 22),
    _MscFrUniSigCurrentAggregateSvcEirInterruptQ_Type()
)
mscFrUniSigCurrentAggregateSvcEirInterruptQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentAggregateSvcEirInterruptQ.setStatus("obsolete")
_MscFrUniSigLapfStatusTable_Object = MibTable
mscFrUniSigLapfStatusTable = _MscFrUniSigLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 17)
)
if mibBuilder.loadTexts:
    mscFrUniSigLapfStatusTable.setStatus("mandatory")
_MscFrUniSigLapfStatusEntry_Object = MibTableRow
mscFrUniSigLapfStatusEntry = _MscFrUniSigLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 17, 1)
)
mscFrUniSigLapfStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigLapfStatusEntry.setStatus("mandatory")


class _MscFrUniSigCurrentState_Type(Integer32):
    """Custom type mscFrUniSigCurrentState based on Integer32"""
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


_MscFrUniSigCurrentState_Type.__name__ = "Integer32"
_MscFrUniSigCurrentState_Object = MibTableColumn
mscFrUniSigCurrentState = _MscFrUniSigCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 17, 1, 1),
    _MscFrUniSigCurrentState_Type()
)
mscFrUniSigCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentState.setStatus("mandatory")


class _MscFrUniSigLastStateChangeReason_Type(Integer32):
    """Custom type mscFrUniSigLastStateChangeReason based on Integer32"""
    defaultValue = 1

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


_MscFrUniSigLastStateChangeReason_Type.__name__ = "Integer32"
_MscFrUniSigLastStateChangeReason_Object = MibTableColumn
mscFrUniSigLastStateChangeReason = _MscFrUniSigLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 17, 1, 2),
    _MscFrUniSigLastStateChangeReason_Type()
)
mscFrUniSigLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastStateChangeReason.setStatus("mandatory")


class _MscFrUniSigFrmrReceive_Type(HexString):
    """Custom type mscFrUniSigFrmrReceive based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscFrUniSigFrmrReceive_Type.__name__ = "HexString"
_MscFrUniSigFrmrReceive_Object = MibTableColumn
mscFrUniSigFrmrReceive = _MscFrUniSigFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 17, 1, 3),
    _MscFrUniSigFrmrReceive_Type()
)
mscFrUniSigFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigFrmrReceive.setStatus("mandatory")
_MscFrUniSigCurrentQueueSize_Type = Counter32
_MscFrUniSigCurrentQueueSize_Object = MibTableColumn
mscFrUniSigCurrentQueueSize = _MscFrUniSigCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 17, 1, 4),
    _MscFrUniSigCurrentQueueSize_Type()
)
mscFrUniSigCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigCurrentQueueSize.setStatus("mandatory")
_MscFrUniSigLapfStatsTable_Object = MibTable
mscFrUniSigLapfStatsTable = _MscFrUniSigLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18)
)
if mibBuilder.loadTexts:
    mscFrUniSigLapfStatsTable.setStatus("mandatory")
_MscFrUniSigLapfStatsEntry_Object = MibTableRow
mscFrUniSigLapfStatsEntry = _MscFrUniSigLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1)
)
mscFrUniSigLapfStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigLapfStatsEntry.setStatus("mandatory")
_MscFrUniSigStateChange_Type = Counter32
_MscFrUniSigStateChange_Object = MibTableColumn
mscFrUniSigStateChange = _MscFrUniSigStateChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 1),
    _MscFrUniSigStateChange_Type()
)
mscFrUniSigStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigStateChange.setStatus("mandatory")
_MscFrUniSigRemoteBusy_Type = Counter32
_MscFrUniSigRemoteBusy_Object = MibTableColumn
mscFrUniSigRemoteBusy = _MscFrUniSigRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 2),
    _MscFrUniSigRemoteBusy_Type()
)
mscFrUniSigRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigRemoteBusy.setStatus("mandatory")
_MscFrUniSigReceiveRejectFrame_Type = Counter32
_MscFrUniSigReceiveRejectFrame_Object = MibTableColumn
mscFrUniSigReceiveRejectFrame = _MscFrUniSigReceiveRejectFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 3),
    _MscFrUniSigReceiveRejectFrame_Type()
)
mscFrUniSigReceiveRejectFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigReceiveRejectFrame.setStatus("mandatory")
_MscFrUniSigAckTimeout_Type = Counter32
_MscFrUniSigAckTimeout_Object = MibTableColumn
mscFrUniSigAckTimeout = _MscFrUniSigAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 4),
    _MscFrUniSigAckTimeout_Type()
)
mscFrUniSigAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigAckTimeout.setStatus("mandatory")
_MscFrUniSigIFramesTransmitted_Type = Counter32
_MscFrUniSigIFramesTransmitted_Object = MibTableColumn
mscFrUniSigIFramesTransmitted = _MscFrUniSigIFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 5),
    _MscFrUniSigIFramesTransmitted_Type()
)
mscFrUniSigIFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigIFramesTransmitted.setStatus("mandatory")
_MscFrUniSigIFramesTxDiscarded_Type = Counter32
_MscFrUniSigIFramesTxDiscarded_Object = MibTableColumn
mscFrUniSigIFramesTxDiscarded = _MscFrUniSigIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 6),
    _MscFrUniSigIFramesTxDiscarded_Type()
)
mscFrUniSigIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigIFramesTxDiscarded.setStatus("mandatory")
_MscFrUniSigIFramesReceived_Type = Counter32
_MscFrUniSigIFramesReceived_Object = MibTableColumn
mscFrUniSigIFramesReceived = _MscFrUniSigIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 7),
    _MscFrUniSigIFramesReceived_Type()
)
mscFrUniSigIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigIFramesReceived.setStatus("mandatory")
_MscFrUniSigIFramesRcvdDiscarded_Type = Counter32
_MscFrUniSigIFramesRcvdDiscarded_Object = MibTableColumn
mscFrUniSigIFramesRcvdDiscarded = _MscFrUniSigIFramesRcvdDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 18, 1, 8),
    _MscFrUniSigIFramesRcvdDiscarded_Type()
)
mscFrUniSigIFramesRcvdDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigIFramesRcvdDiscarded.setStatus("mandatory")
_MscFrUniSigSvcaccTable_Object = MibTable
mscFrUniSigSvcaccTable = _MscFrUniSigSvcaccTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 19)
)
if mibBuilder.loadTexts:
    mscFrUniSigSvcaccTable.setStatus("mandatory")
_MscFrUniSigSvcaccEntry_Object = MibTableRow
mscFrUniSigSvcaccEntry = _MscFrUniSigSvcaccEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 19, 1)
)
mscFrUniSigSvcaccEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigSvcaccEntry.setStatus("mandatory")


class _MscFrUniSigDefaultAccounting_Type(Integer32):
    """Custom type mscFrUniSigDefaultAccounting based on Integer32"""
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


_MscFrUniSigDefaultAccounting_Type.__name__ = "Integer32"
_MscFrUniSigDefaultAccounting_Object = MibTableColumn
mscFrUniSigDefaultAccounting = _MscFrUniSigDefaultAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 19, 1, 1),
    _MscFrUniSigDefaultAccounting_Type()
)
mscFrUniSigDefaultAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniSigDefaultAccounting.setStatus("mandatory")
_MscFrUniSigCodesTable_Object = MibTable
mscFrUniSigCodesTable = _MscFrUniSigCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 20)
)
if mibBuilder.loadTexts:
    mscFrUniSigCodesTable.setStatus("mandatory")
_MscFrUniSigCodesEntry_Object = MibTableRow
mscFrUniSigCodesEntry = _MscFrUniSigCodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 20, 1)
)
mscFrUniSigCodesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigCodesEntry.setStatus("mandatory")


class _MscFrUniSigLastClearRemoteDataNetworkAddress_Type(DigitString):
    """Custom type mscFrUniSigLastClearRemoteDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscFrUniSigLastClearRemoteDataNetworkAddress_Type.__name__ = "DigitString"
_MscFrUniSigLastClearRemoteDataNetworkAddress_Object = MibTableColumn
mscFrUniSigLastClearRemoteDataNetworkAddress = _MscFrUniSigLastClearRemoteDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 20, 1, 1),
    _MscFrUniSigLastClearRemoteDataNetworkAddress_Type()
)
mscFrUniSigLastClearRemoteDataNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastClearRemoteDataNetworkAddress.setStatus("mandatory")


class _MscFrUniSigLastClearCause_Type(Unsigned32):
    """Custom type mscFrUniSigLastClearCause based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniSigLastClearCause_Type.__name__ = "Unsigned32"
_MscFrUniSigLastClearCause_Object = MibTableColumn
mscFrUniSigLastClearCause = _MscFrUniSigLastClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 20, 1, 2),
    _MscFrUniSigLastClearCause_Type()
)
mscFrUniSigLastClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastClearCause.setStatus("mandatory")


class _MscFrUniSigLastDiagnosticCode_Type(Unsigned32):
    """Custom type mscFrUniSigLastDiagnosticCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrUniSigLastDiagnosticCode_Type.__name__ = "Unsigned32"
_MscFrUniSigLastDiagnosticCode_Object = MibTableColumn
mscFrUniSigLastDiagnosticCode = _MscFrUniSigLastDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 20, 1, 3),
    _MscFrUniSigLastDiagnosticCode_Type()
)
mscFrUniSigLastDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigLastDiagnosticCode.setStatus("mandatory")
_MscFrUniSigBandwidthNotAvailableTable_Object = MibTable
mscFrUniSigBandwidthNotAvailableTable = _MscFrUniSigBandwidthNotAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 711)
)
if mibBuilder.loadTexts:
    mscFrUniSigBandwidthNotAvailableTable.setStatus("mandatory")
_MscFrUniSigBandwidthNotAvailableEntry_Object = MibTableRow
mscFrUniSigBandwidthNotAvailableEntry = _MscFrUniSigBandwidthNotAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 711, 1)
)
mscFrUniSigBandwidthNotAvailableEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniSigBandwidthNotAvailableIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniSigBandwidthNotAvailableEntry.setStatus("mandatory")


class _MscFrUniSigBandwidthNotAvailableIndex_Type(Integer32):
    """Custom type mscFrUniSigBandwidthNotAvailableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniSigBandwidthNotAvailableIndex_Type.__name__ = "Integer32"
_MscFrUniSigBandwidthNotAvailableIndex_Object = MibTableColumn
mscFrUniSigBandwidthNotAvailableIndex = _MscFrUniSigBandwidthNotAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 711, 1, 1),
    _MscFrUniSigBandwidthNotAvailableIndex_Type()
)
mscFrUniSigBandwidthNotAvailableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniSigBandwidthNotAvailableIndex.setStatus("mandatory")
_MscFrUniSigBandwidthNotAvailableValue_Type = Counter32
_MscFrUniSigBandwidthNotAvailableValue_Object = MibTableColumn
mscFrUniSigBandwidthNotAvailableValue = _MscFrUniSigBandwidthNotAvailableValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 6, 711, 1, 2),
    _MscFrUniSigBandwidthNotAvailableValue_Type()
)
mscFrUniSigBandwidthNotAvailableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSigBandwidthNotAvailableValue.setStatus("mandatory")
_MscFrUniVFramer_ObjectIdentity = ObjectIdentity
mscFrUniVFramer = _MscFrUniVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8)
)
_MscFrUniVFramerRowStatusTable_Object = MibTable
mscFrUniVFramerRowStatusTable = _MscFrUniVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 1)
)
if mibBuilder.loadTexts:
    mscFrUniVFramerRowStatusTable.setStatus("mandatory")
_MscFrUniVFramerRowStatusEntry_Object = MibTableRow
mscFrUniVFramerRowStatusEntry = _MscFrUniVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 1, 1)
)
mscFrUniVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniVFramerRowStatusEntry.setStatus("mandatory")
_MscFrUniVFramerRowStatus_Type = RowStatus
_MscFrUniVFramerRowStatus_Object = MibTableColumn
mscFrUniVFramerRowStatus = _MscFrUniVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 1, 1, 1),
    _MscFrUniVFramerRowStatus_Type()
)
mscFrUniVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniVFramerRowStatus.setStatus("mandatory")
_MscFrUniVFramerComponentName_Type = DisplayString
_MscFrUniVFramerComponentName_Object = MibTableColumn
mscFrUniVFramerComponentName = _MscFrUniVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 1, 1, 2),
    _MscFrUniVFramerComponentName_Type()
)
mscFrUniVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerComponentName.setStatus("mandatory")
_MscFrUniVFramerStorageType_Type = StorageType
_MscFrUniVFramerStorageType_Object = MibTableColumn
mscFrUniVFramerStorageType = _MscFrUniVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 1, 1, 4),
    _MscFrUniVFramerStorageType_Type()
)
mscFrUniVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerStorageType.setStatus("mandatory")
_MscFrUniVFramerIndex_Type = NonReplicated
_MscFrUniVFramerIndex_Object = MibTableColumn
mscFrUniVFramerIndex = _MscFrUniVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 1, 1, 10),
    _MscFrUniVFramerIndex_Type()
)
mscFrUniVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniVFramerIndex.setStatus("mandatory")
_MscFrUniVFramerProvTable_Object = MibTable
mscFrUniVFramerProvTable = _MscFrUniVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 10)
)
if mibBuilder.loadTexts:
    mscFrUniVFramerProvTable.setStatus("mandatory")
_MscFrUniVFramerProvEntry_Object = MibTableRow
mscFrUniVFramerProvEntry = _MscFrUniVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 10, 1)
)
mscFrUniVFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniVFramerProvEntry.setStatus("mandatory")
_MscFrUniVFramerOtherVirtualFramer_Type = Link
_MscFrUniVFramerOtherVirtualFramer_Object = MibTableColumn
mscFrUniVFramerOtherVirtualFramer = _MscFrUniVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 10, 1, 1),
    _MscFrUniVFramerOtherVirtualFramer_Type()
)
mscFrUniVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniVFramerOtherVirtualFramer.setStatus("mandatory")
_MscFrUniVFramerLogicalProcessor_Type = Link
_MscFrUniVFramerLogicalProcessor_Object = MibTableColumn
mscFrUniVFramerLogicalProcessor = _MscFrUniVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 10, 1, 2),
    _MscFrUniVFramerLogicalProcessor_Type()
)
mscFrUniVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniVFramerLogicalProcessor.setStatus("mandatory")
_MscFrUniVFramerStateTable_Object = MibTable
mscFrUniVFramerStateTable = _MscFrUniVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 11)
)
if mibBuilder.loadTexts:
    mscFrUniVFramerStateTable.setStatus("mandatory")
_MscFrUniVFramerStateEntry_Object = MibTableRow
mscFrUniVFramerStateEntry = _MscFrUniVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 11, 1)
)
mscFrUniVFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniVFramerStateEntry.setStatus("mandatory")


class _MscFrUniVFramerAdminState_Type(Integer32):
    """Custom type mscFrUniVFramerAdminState based on Integer32"""
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


_MscFrUniVFramerAdminState_Type.__name__ = "Integer32"
_MscFrUniVFramerAdminState_Object = MibTableColumn
mscFrUniVFramerAdminState = _MscFrUniVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 11, 1, 1),
    _MscFrUniVFramerAdminState_Type()
)
mscFrUniVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerAdminState.setStatus("mandatory")


class _MscFrUniVFramerOperationalState_Type(Integer32):
    """Custom type mscFrUniVFramerOperationalState based on Integer32"""
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


_MscFrUniVFramerOperationalState_Type.__name__ = "Integer32"
_MscFrUniVFramerOperationalState_Object = MibTableColumn
mscFrUniVFramerOperationalState = _MscFrUniVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 11, 1, 2),
    _MscFrUniVFramerOperationalState_Type()
)
mscFrUniVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerOperationalState.setStatus("mandatory")


class _MscFrUniVFramerUsageState_Type(Integer32):
    """Custom type mscFrUniVFramerUsageState based on Integer32"""
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


_MscFrUniVFramerUsageState_Type.__name__ = "Integer32"
_MscFrUniVFramerUsageState_Object = MibTableColumn
mscFrUniVFramerUsageState = _MscFrUniVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 11, 1, 3),
    _MscFrUniVFramerUsageState_Type()
)
mscFrUniVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerUsageState.setStatus("mandatory")
_MscFrUniVFramerStatsTable_Object = MibTable
mscFrUniVFramerStatsTable = _MscFrUniVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 12)
)
if mibBuilder.loadTexts:
    mscFrUniVFramerStatsTable.setStatus("mandatory")
_MscFrUniVFramerStatsEntry_Object = MibTableRow
mscFrUniVFramerStatsEntry = _MscFrUniVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 12, 1)
)
mscFrUniVFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniVFramerStatsEntry.setStatus("mandatory")
_MscFrUniVFramerFrmToOtherVFramer_Type = PassportCounter64
_MscFrUniVFramerFrmToOtherVFramer_Object = MibTableColumn
mscFrUniVFramerFrmToOtherVFramer = _MscFrUniVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 12, 1, 2),
    _MscFrUniVFramerFrmToOtherVFramer_Type()
)
mscFrUniVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerFrmToOtherVFramer.setStatus("mandatory")
_MscFrUniVFramerFrmFromOtherVFramer_Type = PassportCounter64
_MscFrUniVFramerFrmFromOtherVFramer_Object = MibTableColumn
mscFrUniVFramerFrmFromOtherVFramer = _MscFrUniVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 12, 1, 3),
    _MscFrUniVFramerFrmFromOtherVFramer_Type()
)
mscFrUniVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerFrmFromOtherVFramer.setStatus("mandatory")
_MscFrUniVFramerOctetFromOtherVFramer_Type = PassportCounter64
_MscFrUniVFramerOctetFromOtherVFramer_Object = MibTableColumn
mscFrUniVFramerOctetFromOtherVFramer = _MscFrUniVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 8, 12, 1, 5),
    _MscFrUniVFramerOctetFromOtherVFramer_Type()
)
mscFrUniVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniVFramerOctetFromOtherVFramer.setStatus("mandatory")
_MscFrUniLts_ObjectIdentity = ObjectIdentity
mscFrUniLts = _MscFrUniLts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9)
)
_MscFrUniLtsRowStatusTable_Object = MibTable
mscFrUniLtsRowStatusTable = _MscFrUniLtsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 1)
)
if mibBuilder.loadTexts:
    mscFrUniLtsRowStatusTable.setStatus("mandatory")
_MscFrUniLtsRowStatusEntry_Object = MibTableRow
mscFrUniLtsRowStatusEntry = _MscFrUniLtsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 1, 1)
)
mscFrUniLtsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsRowStatusEntry.setStatus("mandatory")
_MscFrUniLtsRowStatus_Type = RowStatus
_MscFrUniLtsRowStatus_Object = MibTableColumn
mscFrUniLtsRowStatus = _MscFrUniLtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 1, 1, 1),
    _MscFrUniLtsRowStatus_Type()
)
mscFrUniLtsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsRowStatus.setStatus("mandatory")
_MscFrUniLtsComponentName_Type = DisplayString
_MscFrUniLtsComponentName_Object = MibTableColumn
mscFrUniLtsComponentName = _MscFrUniLtsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 1, 1, 2),
    _MscFrUniLtsComponentName_Type()
)
mscFrUniLtsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsComponentName.setStatus("mandatory")
_MscFrUniLtsStorageType_Type = StorageType
_MscFrUniLtsStorageType_Object = MibTableColumn
mscFrUniLtsStorageType = _MscFrUniLtsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 1, 1, 4),
    _MscFrUniLtsStorageType_Type()
)
mscFrUniLtsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsStorageType.setStatus("mandatory")
_MscFrUniLtsIndex_Type = NonReplicated
_MscFrUniLtsIndex_Object = MibTableColumn
mscFrUniLtsIndex = _MscFrUniLtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 1, 1, 10),
    _MscFrUniLtsIndex_Type()
)
mscFrUniLtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniLtsIndex.setStatus("mandatory")
_MscFrUniLtsPat_ObjectIdentity = ObjectIdentity
mscFrUniLtsPat = _MscFrUniLtsPat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2)
)
_MscFrUniLtsPatRowStatusTable_Object = MibTable
mscFrUniLtsPatRowStatusTable = _MscFrUniLtsPatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatRowStatusTable.setStatus("mandatory")
_MscFrUniLtsPatRowStatusEntry_Object = MibTableRow
mscFrUniLtsPatRowStatusEntry = _MscFrUniLtsPatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 1, 1)
)
mscFrUniLtsPatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatRowStatusEntry.setStatus("mandatory")
_MscFrUniLtsPatRowStatus_Type = RowStatus
_MscFrUniLtsPatRowStatus_Object = MibTableColumn
mscFrUniLtsPatRowStatus = _MscFrUniLtsPatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 1, 1, 1),
    _MscFrUniLtsPatRowStatus_Type()
)
mscFrUniLtsPatRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatRowStatus.setStatus("mandatory")
_MscFrUniLtsPatComponentName_Type = DisplayString
_MscFrUniLtsPatComponentName_Object = MibTableColumn
mscFrUniLtsPatComponentName = _MscFrUniLtsPatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 1, 1, 2),
    _MscFrUniLtsPatComponentName_Type()
)
mscFrUniLtsPatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsPatComponentName.setStatus("mandatory")
_MscFrUniLtsPatStorageType_Type = StorageType
_MscFrUniLtsPatStorageType_Object = MibTableColumn
mscFrUniLtsPatStorageType = _MscFrUniLtsPatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 1, 1, 4),
    _MscFrUniLtsPatStorageType_Type()
)
mscFrUniLtsPatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsPatStorageType.setStatus("mandatory")


class _MscFrUniLtsPatIndex_Type(Integer32):
    """Custom type mscFrUniLtsPatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_MscFrUniLtsPatIndex_Type.__name__ = "Integer32"
_MscFrUniLtsPatIndex_Object = MibTableColumn
mscFrUniLtsPatIndex = _MscFrUniLtsPatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 1, 1, 10),
    _MscFrUniLtsPatIndex_Type()
)
mscFrUniLtsPatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniLtsPatIndex.setStatus("mandatory")
_MscFrUniLtsPatDefaultsTable_Object = MibTable
mscFrUniLtsPatDefaultsTable = _MscFrUniLtsPatDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultsTable.setStatus("mandatory")
_MscFrUniLtsPatDefaultsEntry_Object = MibTableRow
mscFrUniLtsPatDefaultsEntry = _MscFrUniLtsPatDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1)
)
mscFrUniLtsPatDefaultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultsEntry.setStatus("mandatory")


class _MscFrUniLtsPatDefaultDlci_Type(Unsigned32):
    """Custom type mscFrUniLtsPatDefaultDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniLtsPatDefaultDlci_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatDefaultDlci_Object = MibTableColumn
mscFrUniLtsPatDefaultDlci = _MscFrUniLtsPatDefaultDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 200),
    _MscFrUniLtsPatDefaultDlci_Type()
)
mscFrUniLtsPatDefaultDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultDlci.setStatus("mandatory")


class _MscFrUniLtsPatDefaultNumFrames_Type(Unsigned32):
    """Custom type mscFrUniLtsPatDefaultNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsPatDefaultNumFrames_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatDefaultNumFrames_Object = MibTableColumn
mscFrUniLtsPatDefaultNumFrames = _MscFrUniLtsPatDefaultNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 201),
    _MscFrUniLtsPatDefaultNumFrames_Type()
)
mscFrUniLtsPatDefaultNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultNumFrames.setStatus("mandatory")


class _MscFrUniLtsPatDefaultDataSize_Type(Unsigned32):
    """Custom type mscFrUniLtsPatDefaultDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_MscFrUniLtsPatDefaultDataSize_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatDefaultDataSize_Object = MibTableColumn
mscFrUniLtsPatDefaultDataSize = _MscFrUniLtsPatDefaultDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 202),
    _MscFrUniLtsPatDefaultDataSize_Type()
)
mscFrUniLtsPatDefaultDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultDataSize.setStatus("mandatory")


class _MscFrUniLtsPatDefaultHeaderBits_Type(OctetString):
    """Custom type mscFrUniLtsPatDefaultHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniLtsPatDefaultHeaderBits_Type.__name__ = "OctetString"
_MscFrUniLtsPatDefaultHeaderBits_Object = MibTableColumn
mscFrUniLtsPatDefaultHeaderBits = _MscFrUniLtsPatDefaultHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 203),
    _MscFrUniLtsPatDefaultHeaderBits_Type()
)
mscFrUniLtsPatDefaultHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultHeaderBits.setStatus("mandatory")


class _MscFrUniLtsPatDefaultHeaderLength_Type(Unsigned32):
    """Custom type mscFrUniLtsPatDefaultHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_MscFrUniLtsPatDefaultHeaderLength_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatDefaultHeaderLength_Object = MibTableColumn
mscFrUniLtsPatDefaultHeaderLength = _MscFrUniLtsPatDefaultHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 204),
    _MscFrUniLtsPatDefaultHeaderLength_Type()
)
mscFrUniLtsPatDefaultHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultHeaderLength.setStatus("mandatory")


class _MscFrUniLtsPatDefaultEABits_Type(Hex):
    """Custom type mscFrUniLtsPatDefaultEABits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniLtsPatDefaultEABits_Type.__name__ = "Hex"
_MscFrUniLtsPatDefaultEABits_Object = MibTableColumn
mscFrUniLtsPatDefaultEABits = _MscFrUniLtsPatDefaultEABits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 205),
    _MscFrUniLtsPatDefaultEABits_Type()
)
mscFrUniLtsPatDefaultEABits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultEABits.setStatus("mandatory")


class _MscFrUniLtsPatDefaultPayloadPattern_Type(HexString):
    """Custom type mscFrUniLtsPatDefaultPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscFrUniLtsPatDefaultPayloadPattern_Type.__name__ = "HexString"
_MscFrUniLtsPatDefaultPayloadPattern_Object = MibTableColumn
mscFrUniLtsPatDefaultPayloadPattern = _MscFrUniLtsPatDefaultPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 206),
    _MscFrUniLtsPatDefaultPayloadPattern_Type()
)
mscFrUniLtsPatDefaultPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultPayloadPattern.setStatus("mandatory")


class _MscFrUniLtsPatDefaultRfc1490Header_Type(Integer32):
    """Custom type mscFrUniLtsPatDefaultRfc1490Header based on Integer32"""
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


_MscFrUniLtsPatDefaultRfc1490Header_Type.__name__ = "Integer32"
_MscFrUniLtsPatDefaultRfc1490Header_Object = MibTableColumn
mscFrUniLtsPatDefaultRfc1490Header = _MscFrUniLtsPatDefaultRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 207),
    _MscFrUniLtsPatDefaultRfc1490Header_Type()
)
mscFrUniLtsPatDefaultRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultRfc1490Header.setStatus("mandatory")


class _MscFrUniLtsPatDefaultUseBadLrc_Type(Integer32):
    """Custom type mscFrUniLtsPatDefaultUseBadLrc based on Integer32"""
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


_MscFrUniLtsPatDefaultUseBadLrc_Type.__name__ = "Integer32"
_MscFrUniLtsPatDefaultUseBadLrc_Object = MibTableColumn
mscFrUniLtsPatDefaultUseBadLrc = _MscFrUniLtsPatDefaultUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 10, 1, 208),
    _MscFrUniLtsPatDefaultUseBadLrc_Type()
)
mscFrUniLtsPatDefaultUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDefaultUseBadLrc.setStatus("mandatory")
_MscFrUniLtsPatSetupTable_Object = MibTable
mscFrUniLtsPatSetupTable = _MscFrUniLtsPatSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatSetupTable.setStatus("mandatory")
_MscFrUniLtsPatSetupEntry_Object = MibTableRow
mscFrUniLtsPatSetupEntry = _MscFrUniLtsPatSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1)
)
mscFrUniLtsPatSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatSetupEntry.setStatus("mandatory")


class _MscFrUniLtsPatDlci_Type(Unsigned32):
    """Custom type mscFrUniLtsPatDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrUniLtsPatDlci_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatDlci_Object = MibTableColumn
mscFrUniLtsPatDlci = _MscFrUniLtsPatDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 200),
    _MscFrUniLtsPatDlci_Type()
)
mscFrUniLtsPatDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDlci.setStatus("mandatory")


class _MscFrUniLtsPatNumFrames_Type(Unsigned32):
    """Custom type mscFrUniLtsPatNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsPatNumFrames_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatNumFrames_Object = MibTableColumn
mscFrUniLtsPatNumFrames = _MscFrUniLtsPatNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 201),
    _MscFrUniLtsPatNumFrames_Type()
)
mscFrUniLtsPatNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatNumFrames.setStatus("mandatory")


class _MscFrUniLtsPatDataSize_Type(Unsigned32):
    """Custom type mscFrUniLtsPatDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_MscFrUniLtsPatDataSize_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatDataSize_Object = MibTableColumn
mscFrUniLtsPatDataSize = _MscFrUniLtsPatDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 202),
    _MscFrUniLtsPatDataSize_Type()
)
mscFrUniLtsPatDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatDataSize.setStatus("mandatory")


class _MscFrUniLtsPatHeaderBits_Type(OctetString):
    """Custom type mscFrUniLtsPatHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniLtsPatHeaderBits_Type.__name__ = "OctetString"
_MscFrUniLtsPatHeaderBits_Object = MibTableColumn
mscFrUniLtsPatHeaderBits = _MscFrUniLtsPatHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 203),
    _MscFrUniLtsPatHeaderBits_Type()
)
mscFrUniLtsPatHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatHeaderBits.setStatus("mandatory")


class _MscFrUniLtsPatHeaderLength_Type(Unsigned32):
    """Custom type mscFrUniLtsPatHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_MscFrUniLtsPatHeaderLength_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatHeaderLength_Object = MibTableColumn
mscFrUniLtsPatHeaderLength = _MscFrUniLtsPatHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 204),
    _MscFrUniLtsPatHeaderLength_Type()
)
mscFrUniLtsPatHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatHeaderLength.setStatus("mandatory")


class _MscFrUniLtsPatEaBits_Type(Hex):
    """Custom type mscFrUniLtsPatEaBits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniLtsPatEaBits_Type.__name__ = "Hex"
_MscFrUniLtsPatEaBits_Object = MibTableColumn
mscFrUniLtsPatEaBits = _MscFrUniLtsPatEaBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 205),
    _MscFrUniLtsPatEaBits_Type()
)
mscFrUniLtsPatEaBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatEaBits.setStatus("mandatory")


class _MscFrUniLtsPatPayloadPattern_Type(HexString):
    """Custom type mscFrUniLtsPatPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscFrUniLtsPatPayloadPattern_Type.__name__ = "HexString"
_MscFrUniLtsPatPayloadPattern_Object = MibTableColumn
mscFrUniLtsPatPayloadPattern = _MscFrUniLtsPatPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 206),
    _MscFrUniLtsPatPayloadPattern_Type()
)
mscFrUniLtsPatPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatPayloadPattern.setStatus("mandatory")


class _MscFrUniLtsPatRfc1490Header_Type(Integer32):
    """Custom type mscFrUniLtsPatRfc1490Header based on Integer32"""
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


_MscFrUniLtsPatRfc1490Header_Type.__name__ = "Integer32"
_MscFrUniLtsPatRfc1490Header_Object = MibTableColumn
mscFrUniLtsPatRfc1490Header = _MscFrUniLtsPatRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 207),
    _MscFrUniLtsPatRfc1490Header_Type()
)
mscFrUniLtsPatRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatRfc1490Header.setStatus("mandatory")


class _MscFrUniLtsPatUseBadLrc_Type(Integer32):
    """Custom type mscFrUniLtsPatUseBadLrc based on Integer32"""
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


_MscFrUniLtsPatUseBadLrc_Type.__name__ = "Integer32"
_MscFrUniLtsPatUseBadLrc_Object = MibTableColumn
mscFrUniLtsPatUseBadLrc = _MscFrUniLtsPatUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 11, 1, 208),
    _MscFrUniLtsPatUseBadLrc_Type()
)
mscFrUniLtsPatUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatUseBadLrc.setStatus("mandatory")
_MscFrUniLtsPatOpDataTable_Object = MibTable
mscFrUniLtsPatOpDataTable = _MscFrUniLtsPatOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatOpDataTable.setStatus("mandatory")
_MscFrUniLtsPatOpDataEntry_Object = MibTableRow
mscFrUniLtsPatOpDataEntry = _MscFrUniLtsPatOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 12, 1)
)
mscFrUniLtsPatOpDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatOpDataEntry.setStatus("mandatory")


class _MscFrUniLtsPatFramePattern_Type(HexString):
    """Custom type mscFrUniLtsPatFramePattern based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 24),
    )


_MscFrUniLtsPatFramePattern_Type.__name__ = "HexString"
_MscFrUniLtsPatFramePattern_Object = MibTableColumn
mscFrUniLtsPatFramePattern = _MscFrUniLtsPatFramePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 12, 1, 200),
    _MscFrUniLtsPatFramePattern_Type()
)
mscFrUniLtsPatFramePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsPatFramePattern.setStatus("mandatory")


class _MscFrUniLtsPatHdlcBitsInserted_Type(Unsigned32):
    """Custom type mscFrUniLtsPatHdlcBitsInserted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFrUniLtsPatHdlcBitsInserted_Type.__name__ = "Unsigned32"
_MscFrUniLtsPatHdlcBitsInserted_Object = MibTableColumn
mscFrUniLtsPatHdlcBitsInserted = _MscFrUniLtsPatHdlcBitsInserted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 12, 1, 201),
    _MscFrUniLtsPatHdlcBitsInserted_Type()
)
mscFrUniLtsPatHdlcBitsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsPatHdlcBitsInserted.setStatus("mandatory")
_MscFrUniLtsPatOpStateTable_Object = MibTable
mscFrUniLtsPatOpStateTable = _MscFrUniLtsPatOpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatOpStateTable.setStatus("mandatory")
_MscFrUniLtsPatOpStateEntry_Object = MibTableRow
mscFrUniLtsPatOpStateEntry = _MscFrUniLtsPatOpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 13, 1)
)
mscFrUniLtsPatOpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsPatOpStateEntry.setStatus("mandatory")


class _MscFrUniLtsPatLoad_Type(FixedPoint3):
    """Custom type mscFrUniLtsPatLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsPatLoad_Type.__name__ = "FixedPoint3"
_MscFrUniLtsPatLoad_Object = MibTableColumn
mscFrUniLtsPatLoad = _MscFrUniLtsPatLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 13, 1, 200),
    _MscFrUniLtsPatLoad_Type()
)
mscFrUniLtsPatLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsPatLoad.setStatus("mandatory")


class _MscFrUniLtsPatStatus_Type(Integer32):
    """Custom type mscFrUniLtsPatStatus based on Integer32"""
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


_MscFrUniLtsPatStatus_Type.__name__ = "Integer32"
_MscFrUniLtsPatStatus_Object = MibTableColumn
mscFrUniLtsPatStatus = _MscFrUniLtsPatStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 2, 13, 1, 201),
    _MscFrUniLtsPatStatus_Type()
)
mscFrUniLtsPatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsPatStatus.setStatus("mandatory")
_MscFrUniLtsSetupTable_Object = MibTable
mscFrUniLtsSetupTable = _MscFrUniLtsSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 10)
)
if mibBuilder.loadTexts:
    mscFrUniLtsSetupTable.setStatus("mandatory")
_MscFrUniLtsSetupEntry_Object = MibTableRow
mscFrUniLtsSetupEntry = _MscFrUniLtsSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 10, 1)
)
mscFrUniLtsSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsSetupEntry.setStatus("mandatory")


class _MscFrUniLtsDuration_Type(Unsigned32):
    """Custom type mscFrUniLtsDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsDuration_Type.__name__ = "Unsigned32"
_MscFrUniLtsDuration_Object = MibTableColumn
mscFrUniLtsDuration = _MscFrUniLtsDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 10, 1, 200),
    _MscFrUniLtsDuration_Type()
)
mscFrUniLtsDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsDuration.setStatus("mandatory")


class _MscFrUniLtsAlgorithm_Type(Integer32):
    """Custom type mscFrUniLtsAlgorithm based on Integer32"""
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


_MscFrUniLtsAlgorithm_Type.__name__ = "Integer32"
_MscFrUniLtsAlgorithm_Object = MibTableColumn
mscFrUniLtsAlgorithm = _MscFrUniLtsAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 10, 1, 201),
    _MscFrUniLtsAlgorithm_Type()
)
mscFrUniLtsAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsAlgorithm.setStatus("mandatory")


class _MscFrUniLtsBurstSize_Type(Unsigned32):
    """Custom type mscFrUniLtsBurstSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MscFrUniLtsBurstSize_Type.__name__ = "Unsigned32"
_MscFrUniLtsBurstSize_Object = MibTableColumn
mscFrUniLtsBurstSize = _MscFrUniLtsBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 10, 1, 204),
    _MscFrUniLtsBurstSize_Type()
)
mscFrUniLtsBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsBurstSize.setStatus("mandatory")


class _MscFrUniLtsTimeInterval_Type(Unsigned32):
    """Custom type mscFrUniLtsTimeInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_MscFrUniLtsTimeInterval_Type.__name__ = "Unsigned32"
_MscFrUniLtsTimeInterval_Object = MibTableColumn
mscFrUniLtsTimeInterval = _MscFrUniLtsTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 10, 1, 205),
    _MscFrUniLtsTimeInterval_Type()
)
mscFrUniLtsTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniLtsTimeInterval.setStatus("mandatory")
_MscFrUniLtsStateTable_Object = MibTable
mscFrUniLtsStateTable = _MscFrUniLtsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 11)
)
if mibBuilder.loadTexts:
    mscFrUniLtsStateTable.setStatus("mandatory")
_MscFrUniLtsStateEntry_Object = MibTableRow
mscFrUniLtsStateEntry = _MscFrUniLtsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 11, 1)
)
mscFrUniLtsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsStateEntry.setStatus("mandatory")


class _MscFrUniLtsGeneratorState_Type(Integer32):
    """Custom type mscFrUniLtsGeneratorState based on Integer32"""
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


_MscFrUniLtsGeneratorState_Type.__name__ = "Integer32"
_MscFrUniLtsGeneratorState_Object = MibTableColumn
mscFrUniLtsGeneratorState = _MscFrUniLtsGeneratorState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 11, 1, 200),
    _MscFrUniLtsGeneratorState_Type()
)
mscFrUniLtsGeneratorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsGeneratorState.setStatus("mandatory")


class _MscFrUniLtsCycleIncomplete_Type(Integer32):
    """Custom type mscFrUniLtsCycleIncomplete based on Integer32"""
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


_MscFrUniLtsCycleIncomplete_Type.__name__ = "Integer32"
_MscFrUniLtsCycleIncomplete_Object = MibTableColumn
mscFrUniLtsCycleIncomplete = _MscFrUniLtsCycleIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 11, 1, 201),
    _MscFrUniLtsCycleIncomplete_Type()
)
mscFrUniLtsCycleIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsCycleIncomplete.setStatus("mandatory")


class _MscFrUniLtsLastActiveInterval_Type(Unsigned32):
    """Custom type mscFrUniLtsLastActiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsLastActiveInterval_Type.__name__ = "Unsigned32"
_MscFrUniLtsLastActiveInterval_Object = MibTableColumn
mscFrUniLtsLastActiveInterval = _MscFrUniLtsLastActiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 11, 1, 202),
    _MscFrUniLtsLastActiveInterval_Type()
)
mscFrUniLtsLastActiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsLastActiveInterval.setStatus("mandatory")


class _MscFrUniLtsLoad_Type(FixedPoint3):
    """Custom type mscFrUniLtsLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsLoad_Type.__name__ = "FixedPoint3"
_MscFrUniLtsLoad_Object = MibTableColumn
mscFrUniLtsLoad = _MscFrUniLtsLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 11, 1, 204),
    _MscFrUniLtsLoad_Type()
)
mscFrUniLtsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsLoad.setStatus("mandatory")


class _MscFrUniLtsElapsedGenerationTime_Type(Unsigned32):
    """Custom type mscFrUniLtsElapsedGenerationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsElapsedGenerationTime_Type.__name__ = "Unsigned32"
_MscFrUniLtsElapsedGenerationTime_Object = MibTableColumn
mscFrUniLtsElapsedGenerationTime = _MscFrUniLtsElapsedGenerationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 11, 1, 205),
    _MscFrUniLtsElapsedGenerationTime_Type()
)
mscFrUniLtsElapsedGenerationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsElapsedGenerationTime.setStatus("mandatory")
_MscFrUniLtsResultsTable_Object = MibTable
mscFrUniLtsResultsTable = _MscFrUniLtsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 12)
)
if mibBuilder.loadTexts:
    mscFrUniLtsResultsTable.setStatus("mandatory")
_MscFrUniLtsResultsEntry_Object = MibTableRow
mscFrUniLtsResultsEntry = _MscFrUniLtsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 12, 1)
)
mscFrUniLtsResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniLtsResultsEntry.setStatus("mandatory")
_MscFrUniLtsFramesTx_Type = Counter32
_MscFrUniLtsFramesTx_Object = MibTableColumn
mscFrUniLtsFramesTx = _MscFrUniLtsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 12, 1, 200),
    _MscFrUniLtsFramesTx_Type()
)
mscFrUniLtsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsFramesTx.setStatus("mandatory")


class _MscFrUniLtsBytesTx_Type(Unsigned32):
    """Custom type mscFrUniLtsBytesTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsBytesTx_Type.__name__ = "Unsigned32"
_MscFrUniLtsBytesTx_Object = MibTableColumn
mscFrUniLtsBytesTx = _MscFrUniLtsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 12, 1, 204),
    _MscFrUniLtsBytesTx_Type()
)
mscFrUniLtsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsBytesTx.setStatus("mandatory")


class _MscFrUniLtsBitRateTx_Type(FixedPoint3):
    """Custom type mscFrUniLtsBitRateTx based on FixedPoint3"""
    defaultValue = 0

    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsBitRateTx_Type.__name__ = "FixedPoint3"
_MscFrUniLtsBitRateTx_Object = MibTableColumn
mscFrUniLtsBitRateTx = _MscFrUniLtsBitRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 12, 1, 208),
    _MscFrUniLtsBitRateTx_Type()
)
mscFrUniLtsBitRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsBitRateTx.setStatus("mandatory")


class _MscFrUniLtsFrameRateTx_Type(Unsigned32):
    """Custom type mscFrUniLtsFrameRateTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniLtsFrameRateTx_Type.__name__ = "Unsigned32"
_MscFrUniLtsFrameRateTx_Object = MibTableColumn
mscFrUniLtsFrameRateTx = _MscFrUniLtsFrameRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 9, 12, 1, 209),
    _MscFrUniLtsFrameRateTx_Type()
)
mscFrUniLtsFrameRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLtsFrameRateTx.setStatus("mandatory")
_MscFrUniCidDataTable_Object = MibTable
mscFrUniCidDataTable = _MscFrUniCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 10)
)
if mibBuilder.loadTexts:
    mscFrUniCidDataTable.setStatus("mandatory")
_MscFrUniCidDataEntry_Object = MibTableRow
mscFrUniCidDataEntry = _MscFrUniCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 10, 1)
)
mscFrUniCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCidDataEntry.setStatus("mandatory")


class _MscFrUniCustomerIdentifier_Type(Unsigned32):
    """Custom type mscFrUniCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscFrUniCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscFrUniCustomerIdentifier_Object = MibTableColumn
mscFrUniCustomerIdentifier = _MscFrUniCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 10, 1, 1),
    _MscFrUniCustomerIdentifier_Type()
)
mscFrUniCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCustomerIdentifier.setStatus("mandatory")
_MscFrUniStateTable_Object = MibTable
mscFrUniStateTable = _MscFrUniStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11)
)
if mibBuilder.loadTexts:
    mscFrUniStateTable.setStatus("mandatory")
_MscFrUniStateEntry_Object = MibTableRow
mscFrUniStateEntry = _MscFrUniStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1)
)
mscFrUniStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniStateEntry.setStatus("mandatory")


class _MscFrUniAdminState_Type(Integer32):
    """Custom type mscFrUniAdminState based on Integer32"""
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


_MscFrUniAdminState_Type.__name__ = "Integer32"
_MscFrUniAdminState_Object = MibTableColumn
mscFrUniAdminState = _MscFrUniAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 1),
    _MscFrUniAdminState_Type()
)
mscFrUniAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniAdminState.setStatus("mandatory")


class _MscFrUniOperationalState_Type(Integer32):
    """Custom type mscFrUniOperationalState based on Integer32"""
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


_MscFrUniOperationalState_Type.__name__ = "Integer32"
_MscFrUniOperationalState_Object = MibTableColumn
mscFrUniOperationalState = _MscFrUniOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 2),
    _MscFrUniOperationalState_Type()
)
mscFrUniOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniOperationalState.setStatus("mandatory")


class _MscFrUniUsageState_Type(Integer32):
    """Custom type mscFrUniUsageState based on Integer32"""
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


_MscFrUniUsageState_Type.__name__ = "Integer32"
_MscFrUniUsageState_Object = MibTableColumn
mscFrUniUsageState = _MscFrUniUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 3),
    _MscFrUniUsageState_Type()
)
mscFrUniUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniUsageState.setStatus("mandatory")


class _MscFrUniAvailabilityStatus_Type(OctetString):
    """Custom type mscFrUniAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFrUniAvailabilityStatus_Type.__name__ = "OctetString"
_MscFrUniAvailabilityStatus_Object = MibTableColumn
mscFrUniAvailabilityStatus = _MscFrUniAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 4),
    _MscFrUniAvailabilityStatus_Type()
)
mscFrUniAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniAvailabilityStatus.setStatus("mandatory")


class _MscFrUniProceduralStatus_Type(OctetString):
    """Custom type mscFrUniProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniProceduralStatus_Type.__name__ = "OctetString"
_MscFrUniProceduralStatus_Object = MibTableColumn
mscFrUniProceduralStatus = _MscFrUniProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 5),
    _MscFrUniProceduralStatus_Type()
)
mscFrUniProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniProceduralStatus.setStatus("mandatory")


class _MscFrUniControlStatus_Type(OctetString):
    """Custom type mscFrUniControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniControlStatus_Type.__name__ = "OctetString"
_MscFrUniControlStatus_Object = MibTableColumn
mscFrUniControlStatus = _MscFrUniControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 6),
    _MscFrUniControlStatus_Type()
)
mscFrUniControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniControlStatus.setStatus("mandatory")


class _MscFrUniAlarmStatus_Type(OctetString):
    """Custom type mscFrUniAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrUniAlarmStatus_Type.__name__ = "OctetString"
_MscFrUniAlarmStatus_Object = MibTableColumn
mscFrUniAlarmStatus = _MscFrUniAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 7),
    _MscFrUniAlarmStatus_Type()
)
mscFrUniAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniAlarmStatus.setStatus("mandatory")


class _MscFrUniStandbyStatus_Type(Integer32):
    """Custom type mscFrUniStandbyStatus based on Integer32"""
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


_MscFrUniStandbyStatus_Type.__name__ = "Integer32"
_MscFrUniStandbyStatus_Object = MibTableColumn
mscFrUniStandbyStatus = _MscFrUniStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 8),
    _MscFrUniStandbyStatus_Type()
)
mscFrUniStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniStandbyStatus.setStatus("mandatory")


class _MscFrUniUnknownStatus_Type(Integer32):
    """Custom type mscFrUniUnknownStatus based on Integer32"""
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


_MscFrUniUnknownStatus_Type.__name__ = "Integer32"
_MscFrUniUnknownStatus_Object = MibTableColumn
mscFrUniUnknownStatus = _MscFrUniUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 11, 1, 9),
    _MscFrUniUnknownStatus_Type()
)
mscFrUniUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniUnknownStatus.setStatus("mandatory")
_MscFrUniStatsTable_Object = MibTable
mscFrUniStatsTable = _MscFrUniStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 12)
)
if mibBuilder.loadTexts:
    mscFrUniStatsTable.setStatus("mandatory")
_MscFrUniStatsEntry_Object = MibTableRow
mscFrUniStatsEntry = _MscFrUniStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 12, 1)
)
mscFrUniStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniStatsEntry.setStatus("mandatory")


class _MscFrUniLastUnknownDlci_Type(Unsigned32):
    """Custom type mscFrUniLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscFrUniLastUnknownDlci_Type.__name__ = "Unsigned32"
_MscFrUniLastUnknownDlci_Object = MibTableColumn
mscFrUniLastUnknownDlci = _MscFrUniLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 12, 1, 1),
    _MscFrUniLastUnknownDlci_Type()
)
mscFrUniLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniLastUnknownDlci.setStatus("mandatory")
_MscFrUniUnknownDlciFramesFromIf_Type = Counter32
_MscFrUniUnknownDlciFramesFromIf_Object = MibTableColumn
mscFrUniUnknownDlciFramesFromIf = _MscFrUniUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 12, 1, 2),
    _MscFrUniUnknownDlciFramesFromIf_Type()
)
mscFrUniUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniUnknownDlciFramesFromIf.setStatus("mandatory")
_MscFrUniInvalidHeaderFramesFromIf_Type = Counter32
_MscFrUniInvalidHeaderFramesFromIf_Object = MibTableColumn
mscFrUniInvalidHeaderFramesFromIf = _MscFrUniInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 12, 1, 3),
    _MscFrUniInvalidHeaderFramesFromIf_Type()
)
mscFrUniInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniInvalidHeaderFramesFromIf.setStatus("mandatory")
_MscFrUniIfEntryTable_Object = MibTable
mscFrUniIfEntryTable = _MscFrUniIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 13)
)
if mibBuilder.loadTexts:
    mscFrUniIfEntryTable.setStatus("mandatory")
_MscFrUniIfEntryEntry_Object = MibTableRow
mscFrUniIfEntryEntry = _MscFrUniIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 13, 1)
)
mscFrUniIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniIfEntryEntry.setStatus("mandatory")


class _MscFrUniIfAdminStatus_Type(Integer32):
    """Custom type mscFrUniIfAdminStatus based on Integer32"""
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


_MscFrUniIfAdminStatus_Type.__name__ = "Integer32"
_MscFrUniIfAdminStatus_Object = MibTableColumn
mscFrUniIfAdminStatus = _MscFrUniIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 13, 1, 1),
    _MscFrUniIfAdminStatus_Type()
)
mscFrUniIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniIfAdminStatus.setStatus("mandatory")


class _MscFrUniIfIndex_Type(InterfaceIndex):
    """Custom type mscFrUniIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrUniIfIndex_Type.__name__ = "InterfaceIndex"
_MscFrUniIfIndex_Object = MibTableColumn
mscFrUniIfIndex = _MscFrUniIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 13, 1, 2),
    _MscFrUniIfIndex_Type()
)
mscFrUniIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniIfIndex.setStatus("mandatory")
_MscFrUniOperStatusTable_Object = MibTable
mscFrUniOperStatusTable = _MscFrUniOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 14)
)
if mibBuilder.loadTexts:
    mscFrUniOperStatusTable.setStatus("mandatory")
_MscFrUniOperStatusEntry_Object = MibTableRow
mscFrUniOperStatusEntry = _MscFrUniOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 14, 1)
)
mscFrUniOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniOperStatusEntry.setStatus("mandatory")


class _MscFrUniSnmpOperStatus_Type(Integer32):
    """Custom type mscFrUniSnmpOperStatus based on Integer32"""
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


_MscFrUniSnmpOperStatus_Type.__name__ = "Integer32"
_MscFrUniSnmpOperStatus_Object = MibTableColumn
mscFrUniSnmpOperStatus = _MscFrUniSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 14, 1, 1),
    _MscFrUniSnmpOperStatus_Type()
)
mscFrUniSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniSnmpOperStatus.setStatus("mandatory")
_MscFrUniEmissionPriorityQsTable_Object = MibTable
mscFrUniEmissionPriorityQsTable = _MscFrUniEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 15)
)
if mibBuilder.loadTexts:
    mscFrUniEmissionPriorityQsTable.setStatus("mandatory")
_MscFrUniEmissionPriorityQsEntry_Object = MibTableRow
mscFrUniEmissionPriorityQsEntry = _MscFrUniEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 15, 1)
)
mscFrUniEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniEmissionPriorityQsEntry.setStatus("mandatory")


class _MscFrUniNumberOfEmissionQs_Type(Unsigned32):
    """Custom type mscFrUniNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_MscFrUniNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_MscFrUniNumberOfEmissionQs_Object = MibTableColumn
mscFrUniNumberOfEmissionQs = _MscFrUniNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 15, 1, 1),
    _MscFrUniNumberOfEmissionQs_Type()
)
mscFrUniNumberOfEmissionQs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniNumberOfEmissionQs.setStatus("mandatory")
_MscFrUniCa_ObjectIdentity = ObjectIdentity
mscFrUniCa = _MscFrUniCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101)
)
_MscFrUniCaRowStatusTable_Object = MibTable
mscFrUniCaRowStatusTable = _MscFrUniCaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 1)
)
if mibBuilder.loadTexts:
    mscFrUniCaRowStatusTable.setStatus("mandatory")
_MscFrUniCaRowStatusEntry_Object = MibTableRow
mscFrUniCaRowStatusEntry = _MscFrUniCaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 1, 1)
)
mscFrUniCaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaRowStatusEntry.setStatus("mandatory")
_MscFrUniCaRowStatus_Type = RowStatus
_MscFrUniCaRowStatus_Object = MibTableColumn
mscFrUniCaRowStatus = _MscFrUniCaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 1, 1, 1),
    _MscFrUniCaRowStatus_Type()
)
mscFrUniCaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaRowStatus.setStatus("mandatory")
_MscFrUniCaComponentName_Type = DisplayString
_MscFrUniCaComponentName_Object = MibTableColumn
mscFrUniCaComponentName = _MscFrUniCaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 1, 1, 2),
    _MscFrUniCaComponentName_Type()
)
mscFrUniCaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaComponentName.setStatus("mandatory")
_MscFrUniCaStorageType_Type = StorageType
_MscFrUniCaStorageType_Object = MibTableColumn
mscFrUniCaStorageType = _MscFrUniCaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 1, 1, 4),
    _MscFrUniCaStorageType_Type()
)
mscFrUniCaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaStorageType.setStatus("mandatory")
_MscFrUniCaIndex_Type = NonReplicated
_MscFrUniCaIndex_Object = MibTableColumn
mscFrUniCaIndex = _MscFrUniCaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 1, 1, 10),
    _MscFrUniCaIndex_Type()
)
mscFrUniCaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaIndex.setStatus("mandatory")
_MscFrUniCaTpm_ObjectIdentity = ObjectIdentity
mscFrUniCaTpm = _MscFrUniCaTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2)
)
_MscFrUniCaTpmRowStatusTable_Object = MibTable
mscFrUniCaTpmRowStatusTable = _MscFrUniCaTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrUniCaTpmRowStatusTable.setStatus("mandatory")
_MscFrUniCaTpmRowStatusEntry_Object = MibTableRow
mscFrUniCaTpmRowStatusEntry = _MscFrUniCaTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 1, 1)
)
mscFrUniCaTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaTpmIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaTpmRowStatusEntry.setStatus("mandatory")
_MscFrUniCaTpmRowStatus_Type = RowStatus
_MscFrUniCaTpmRowStatus_Object = MibTableColumn
mscFrUniCaTpmRowStatus = _MscFrUniCaTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 1, 1, 1),
    _MscFrUniCaTpmRowStatus_Type()
)
mscFrUniCaTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaTpmRowStatus.setStatus("mandatory")
_MscFrUniCaTpmComponentName_Type = DisplayString
_MscFrUniCaTpmComponentName_Object = MibTableColumn
mscFrUniCaTpmComponentName = _MscFrUniCaTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 1, 1, 2),
    _MscFrUniCaTpmComponentName_Type()
)
mscFrUniCaTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaTpmComponentName.setStatus("mandatory")
_MscFrUniCaTpmStorageType_Type = StorageType
_MscFrUniCaTpmStorageType_Object = MibTableColumn
mscFrUniCaTpmStorageType = _MscFrUniCaTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 1, 1, 4),
    _MscFrUniCaTpmStorageType_Type()
)
mscFrUniCaTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaTpmStorageType.setStatus("mandatory")


class _MscFrUniCaTpmIndex_Type(Integer32):
    """Custom type mscFrUniCaTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaTpmIndex_Type.__name__ = "Integer32"
_MscFrUniCaTpmIndex_Object = MibTableColumn
mscFrUniCaTpmIndex = _MscFrUniCaTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 1, 1, 10),
    _MscFrUniCaTpmIndex_Type()
)
mscFrUniCaTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaTpmIndex.setStatus("mandatory")
_MscFrUniCaTpmProvTable_Object = MibTable
mscFrUniCaTpmProvTable = _MscFrUniCaTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrUniCaTpmProvTable.setStatus("mandatory")
_MscFrUniCaTpmProvEntry_Object = MibTableRow
mscFrUniCaTpmProvEntry = _MscFrUniCaTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 10, 1)
)
mscFrUniCaTpmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaTpmIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaTpmProvEntry.setStatus("mandatory")


class _MscFrUniCaTpmAssignedIngressBandwidthPool_Type(Unsigned32):
    """Custom type mscFrUniCaTpmAssignedIngressBandwidthPool based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(16, 16),
    )


_MscFrUniCaTpmAssignedIngressBandwidthPool_Type.__name__ = "Unsigned32"
_MscFrUniCaTpmAssignedIngressBandwidthPool_Object = MibTableColumn
mscFrUniCaTpmAssignedIngressBandwidthPool = _MscFrUniCaTpmAssignedIngressBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 10, 1, 2),
    _MscFrUniCaTpmAssignedIngressBandwidthPool_Type()
)
mscFrUniCaTpmAssignedIngressBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaTpmAssignedIngressBandwidthPool.setStatus("mandatory")


class _MscFrUniCaTpmAssignedEgressBandwidthPool_Type(Unsigned32):
    """Custom type mscFrUniCaTpmAssignedEgressBandwidthPool based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(16, 16),
    )


_MscFrUniCaTpmAssignedEgressBandwidthPool_Type.__name__ = "Unsigned32"
_MscFrUniCaTpmAssignedEgressBandwidthPool_Object = MibTableColumn
mscFrUniCaTpmAssignedEgressBandwidthPool = _MscFrUniCaTpmAssignedEgressBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 2, 10, 1, 3),
    _MscFrUniCaTpmAssignedEgressBandwidthPool_Type()
)
mscFrUniCaTpmAssignedEgressBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaTpmAssignedEgressBandwidthPool.setStatus("mandatory")
_MscFrUniCaProvTable_Object = MibTable
mscFrUniCaProvTable = _MscFrUniCaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 10)
)
if mibBuilder.loadTexts:
    mscFrUniCaProvTable.setStatus("mandatory")
_MscFrUniCaProvEntry_Object = MibTableRow
mscFrUniCaProvEntry = _MscFrUniCaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 10, 1)
)
mscFrUniCaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaProvEntry.setStatus("mandatory")


class _MscFrUniCaOverrideLinkRate_Type(Unsigned32):
    """Custom type mscFrUniCaOverrideLinkRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496729),
    )


_MscFrUniCaOverrideLinkRate_Type.__name__ = "Unsigned32"
_MscFrUniCaOverrideLinkRate_Object = MibTableColumn
mscFrUniCaOverrideLinkRate = _MscFrUniCaOverrideLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 10, 1, 2),
    _MscFrUniCaOverrideLinkRate_Type()
)
mscFrUniCaOverrideLinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaOverrideLinkRate.setStatus("mandatory")


class _MscFrUniCaMaximumBandwidthPerCall_Type(Unsigned32):
    """Custom type mscFrUniCaMaximumBandwidthPerCall based on Unsigned32"""
    defaultValue = 520000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrUniCaMaximumBandwidthPerCall_Type.__name__ = "Unsigned32"
_MscFrUniCaMaximumBandwidthPerCall_Object = MibTableColumn
mscFrUniCaMaximumBandwidthPerCall = _MscFrUniCaMaximumBandwidthPerCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 10, 1, 3),
    _MscFrUniCaMaximumBandwidthPerCall_Type()
)
mscFrUniCaMaximumBandwidthPerCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaMaximumBandwidthPerCall.setStatus("mandatory")
_MscFrUniCaIngressCacTable_Object = MibTable
mscFrUniCaIngressCacTable = _MscFrUniCaIngressCacTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 11)
)
if mibBuilder.loadTexts:
    mscFrUniCaIngressCacTable.setStatus("mandatory")
_MscFrUniCaIngressCacEntry_Object = MibTableRow
mscFrUniCaIngressCacEntry = _MscFrUniCaIngressCacEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 11, 1)
)
mscFrUniCaIngressCacEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaIngressCacEntry.setStatus("mandatory")


class _MscFrUniCaIngressApplyToCos_Type(Integer32):
    """Custom type mscFrUniCaIngressApplyToCos based on Integer32"""
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
        *(("cirAndEir", 2),
          ("cirOnly", 1),
          ("none", 0))
    )


_MscFrUniCaIngressApplyToCos_Type.__name__ = "Integer32"
_MscFrUniCaIngressApplyToCos_Object = MibTableColumn
mscFrUniCaIngressApplyToCos = _MscFrUniCaIngressApplyToCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 11, 1, 2),
    _MscFrUniCaIngressApplyToCos_Type()
)
mscFrUniCaIngressApplyToCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaIngressApplyToCos.setStatus("mandatory")


class _MscFrUniCaIngressMaximumEirOnlyCalls_Type(Unsigned32):
    """Custom type mscFrUniCaIngressMaximumEirOnlyCalls based on Unsigned32"""
    defaultValue = 992

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrUniCaIngressMaximumEirOnlyCalls_Type.__name__ = "Unsigned32"
_MscFrUniCaIngressMaximumEirOnlyCalls_Object = MibTableColumn
mscFrUniCaIngressMaximumEirOnlyCalls = _MscFrUniCaIngressMaximumEirOnlyCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 11, 1, 4),
    _MscFrUniCaIngressMaximumEirOnlyCalls_Type()
)
mscFrUniCaIngressMaximumEirOnlyCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaIngressMaximumEirOnlyCalls.setStatus("mandatory")
_MscFrUniCaEgressCacTable_Object = MibTable
mscFrUniCaEgressCacTable = _MscFrUniCaEgressCacTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 12)
)
if mibBuilder.loadTexts:
    mscFrUniCaEgressCacTable.setStatus("mandatory")
_MscFrUniCaEgressCacEntry_Object = MibTableRow
mscFrUniCaEgressCacEntry = _MscFrUniCaEgressCacEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 12, 1)
)
mscFrUniCaEgressCacEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaEgressCacEntry.setStatus("mandatory")


class _MscFrUniCaEgressApplyToCos_Type(Integer32):
    """Custom type mscFrUniCaEgressApplyToCos based on Integer32"""
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
        *(("cirAndEir", 2),
          ("cirOnly", 1),
          ("none", 0))
    )


_MscFrUniCaEgressApplyToCos_Type.__name__ = "Integer32"
_MscFrUniCaEgressApplyToCos_Object = MibTableColumn
mscFrUniCaEgressApplyToCos = _MscFrUniCaEgressApplyToCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 12, 1, 2),
    _MscFrUniCaEgressApplyToCos_Type()
)
mscFrUniCaEgressApplyToCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaEgressApplyToCos.setStatus("mandatory")


class _MscFrUniCaEgressMaximumEirOnlyCalls_Type(Unsigned32):
    """Custom type mscFrUniCaEgressMaximumEirOnlyCalls based on Unsigned32"""
    defaultValue = 992

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrUniCaEgressMaximumEirOnlyCalls_Type.__name__ = "Unsigned32"
_MscFrUniCaEgressMaximumEirOnlyCalls_Object = MibTableColumn
mscFrUniCaEgressMaximumEirOnlyCalls = _MscFrUniCaEgressMaximumEirOnlyCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 12, 1, 4),
    _MscFrUniCaEgressMaximumEirOnlyCalls_Type()
)
mscFrUniCaEgressMaximumEirOnlyCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaEgressMaximumEirOnlyCalls.setStatus("mandatory")
_MscFrUniCaOpTable_Object = MibTable
mscFrUniCaOpTable = _MscFrUniCaOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 13)
)
if mibBuilder.loadTexts:
    mscFrUniCaOpTable.setStatus("mandatory")
_MscFrUniCaOpEntry_Object = MibTableRow
mscFrUniCaOpEntry = _MscFrUniCaOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 13, 1)
)
mscFrUniCaOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaOpEntry.setStatus("mandatory")


class _MscFrUniCaLinkRate_Type(Unsigned32):
    """Custom type mscFrUniCaLinkRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrUniCaLinkRate_Type.__name__ = "Unsigned32"
_MscFrUniCaLinkRate_Object = MibTableColumn
mscFrUniCaLinkRate = _MscFrUniCaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 13, 1, 2),
    _MscFrUniCaLinkRate_Type()
)
mscFrUniCaLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaLinkRate.setStatus("mandatory")


class _MscFrUniCaNumberRejectedEgressCirPermConn_Type(Gauge32):
    """Custom type mscFrUniCaNumberRejectedEgressCirPermConn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrUniCaNumberRejectedEgressCirPermConn_Type.__name__ = "Gauge32"
_MscFrUniCaNumberRejectedEgressCirPermConn_Object = MibTableColumn
mscFrUniCaNumberRejectedEgressCirPermConn = _MscFrUniCaNumberRejectedEgressCirPermConn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 13, 1, 681),
    _MscFrUniCaNumberRejectedEgressCirPermConn_Type()
)
mscFrUniCaNumberRejectedEgressCirPermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaNumberRejectedEgressCirPermConn.setStatus("mandatory")


class _MscFrUniCaNumberRejectedEgressEirPermConn_Type(Gauge32):
    """Custom type mscFrUniCaNumberRejectedEgressEirPermConn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrUniCaNumberRejectedEgressEirPermConn_Type.__name__ = "Gauge32"
_MscFrUniCaNumberRejectedEgressEirPermConn_Object = MibTableColumn
mscFrUniCaNumberRejectedEgressEirPermConn = _MscFrUniCaNumberRejectedEgressEirPermConn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 13, 1, 682),
    _MscFrUniCaNumberRejectedEgressEirPermConn_Type()
)
mscFrUniCaNumberRejectedEgressEirPermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaNumberRejectedEgressEirPermConn.setStatus("mandatory")
_MscFrUniCaIngCirBPTable_Object = MibTable
mscFrUniCaIngCirBPTable = _MscFrUniCaIngCirBPTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 666)
)
if mibBuilder.loadTexts:
    mscFrUniCaIngCirBPTable.setStatus("mandatory")
_MscFrUniCaIngCirBPEntry_Object = MibTableRow
mscFrUniCaIngCirBPEntry = _MscFrUniCaIngCirBPEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 666, 1)
)
mscFrUniCaIngCirBPEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIngCirBPIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaIngCirBPEntry.setStatus("mandatory")


class _MscFrUniCaIngCirBPIndex_Type(Integer32):
    """Custom type mscFrUniCaIngCirBPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaIngCirBPIndex_Type.__name__ = "Integer32"
_MscFrUniCaIngCirBPIndex_Object = MibTableColumn
mscFrUniCaIngCirBPIndex = _MscFrUniCaIngCirBPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 666, 1, 1),
    _MscFrUniCaIngCirBPIndex_Type()
)
mscFrUniCaIngCirBPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaIngCirBPIndex.setStatus("mandatory")


class _MscFrUniCaIngCirBPValue_Type(Unsigned32):
    """Custom type mscFrUniCaIngCirBPValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrUniCaIngCirBPValue_Type.__name__ = "Unsigned32"
_MscFrUniCaIngCirBPValue_Object = MibTableColumn
mscFrUniCaIngCirBPValue = _MscFrUniCaIngCirBPValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 666, 1, 2),
    _MscFrUniCaIngCirBPValue_Type()
)
mscFrUniCaIngCirBPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaIngCirBPValue.setStatus("mandatory")
_MscFrUniCaEgCirBpTable_Object = MibTable
mscFrUniCaEgCirBpTable = _MscFrUniCaEgCirBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 667)
)
if mibBuilder.loadTexts:
    mscFrUniCaEgCirBpTable.setStatus("mandatory")
_MscFrUniCaEgCirBpEntry_Object = MibTableRow
mscFrUniCaEgCirBpEntry = _MscFrUniCaEgCirBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 667, 1)
)
mscFrUniCaEgCirBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaEgCirBpIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaEgCirBpEntry.setStatus("mandatory")


class _MscFrUniCaEgCirBpIndex_Type(Integer32):
    """Custom type mscFrUniCaEgCirBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaEgCirBpIndex_Type.__name__ = "Integer32"
_MscFrUniCaEgCirBpIndex_Object = MibTableColumn
mscFrUniCaEgCirBpIndex = _MscFrUniCaEgCirBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 667, 1, 1),
    _MscFrUniCaEgCirBpIndex_Type()
)
mscFrUniCaEgCirBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaEgCirBpIndex.setStatus("mandatory")


class _MscFrUniCaEgCirBpValue_Type(Unsigned32):
    """Custom type mscFrUniCaEgCirBpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrUniCaEgCirBpValue_Type.__name__ = "Unsigned32"
_MscFrUniCaEgCirBpValue_Object = MibTableColumn
mscFrUniCaEgCirBpValue = _MscFrUniCaEgCirBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 667, 1, 2),
    _MscFrUniCaEgCirBpValue_Type()
)
mscFrUniCaEgCirBpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaEgCirBpValue.setStatus("mandatory")
_MscFrUniCaIngCirPoolAdmitBwTable_Object = MibTable
mscFrUniCaIngCirPoolAdmitBwTable = _MscFrUniCaIngCirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 668)
)
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAdmitBwTable.setStatus("mandatory")
_MscFrUniCaIngCirPoolAdmitBwEntry_Object = MibTableRow
mscFrUniCaIngCirPoolAdmitBwEntry = _MscFrUniCaIngCirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 668, 1)
)
mscFrUniCaIngCirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIngCirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrUniCaIngCirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrUniCaIngCirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaIngCirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaIngCirPoolAdmitBwIndex_Object = MibTableColumn
mscFrUniCaIngCirPoolAdmitBwIndex = _MscFrUniCaIngCirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 668, 1, 1),
    _MscFrUniCaIngCirPoolAdmitBwIndex_Type()
)
mscFrUniCaIngCirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrUniCaIngCirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrUniCaIngCirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrUniCaIngCirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaIngCirPoolAdmitBwValue_Object = MibTableColumn
mscFrUniCaIngCirPoolAdmitBwValue = _MscFrUniCaIngCirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 668, 1, 2),
    _MscFrUniCaIngCirPoolAdmitBwValue_Type()
)
mscFrUniCaIngCirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAdmitBwValue.setStatus("mandatory")
_MscFrUniCaIngCirPoolAvailBwTable_Object = MibTable
mscFrUniCaIngCirPoolAvailBwTable = _MscFrUniCaIngCirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 669)
)
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAvailBwTable.setStatus("mandatory")
_MscFrUniCaIngCirPoolAvailBwEntry_Object = MibTableRow
mscFrUniCaIngCirPoolAvailBwEntry = _MscFrUniCaIngCirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 669, 1)
)
mscFrUniCaIngCirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIngCirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrUniCaIngCirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrUniCaIngCirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaIngCirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaIngCirPoolAvailBwIndex_Object = MibTableColumn
mscFrUniCaIngCirPoolAvailBwIndex = _MscFrUniCaIngCirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 669, 1, 1),
    _MscFrUniCaIngCirPoolAvailBwIndex_Type()
)
mscFrUniCaIngCirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrUniCaIngCirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrUniCaIngCirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrUniCaIngCirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaIngCirPoolAvailBwValue_Object = MibTableColumn
mscFrUniCaIngCirPoolAvailBwValue = _MscFrUniCaIngCirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 669, 1, 2),
    _MscFrUniCaIngCirPoolAvailBwValue_Type()
)
mscFrUniCaIngCirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaIngCirPoolAvailBwValue.setStatus("mandatory")
_MscFrUniCaEgCirPoolAdmitBwTable_Object = MibTable
mscFrUniCaEgCirPoolAdmitBwTable = _MscFrUniCaEgCirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 670)
)
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAdmitBwTable.setStatus("mandatory")
_MscFrUniCaEgCirPoolAdmitBwEntry_Object = MibTableRow
mscFrUniCaEgCirPoolAdmitBwEntry = _MscFrUniCaEgCirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 670, 1)
)
mscFrUniCaEgCirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaEgCirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrUniCaEgCirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrUniCaEgCirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaEgCirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaEgCirPoolAdmitBwIndex_Object = MibTableColumn
mscFrUniCaEgCirPoolAdmitBwIndex = _MscFrUniCaEgCirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 670, 1, 1),
    _MscFrUniCaEgCirPoolAdmitBwIndex_Type()
)
mscFrUniCaEgCirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrUniCaEgCirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrUniCaEgCirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrUniCaEgCirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaEgCirPoolAdmitBwValue_Object = MibTableColumn
mscFrUniCaEgCirPoolAdmitBwValue = _MscFrUniCaEgCirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 670, 1, 2),
    _MscFrUniCaEgCirPoolAdmitBwValue_Type()
)
mscFrUniCaEgCirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAdmitBwValue.setStatus("mandatory")
_MscFrUniCaEgCirPoolAvailBwTable_Object = MibTable
mscFrUniCaEgCirPoolAvailBwTable = _MscFrUniCaEgCirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 671)
)
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAvailBwTable.setStatus("mandatory")
_MscFrUniCaEgCirPoolAvailBwEntry_Object = MibTableRow
mscFrUniCaEgCirPoolAvailBwEntry = _MscFrUniCaEgCirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 671, 1)
)
mscFrUniCaEgCirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaEgCirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrUniCaEgCirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrUniCaEgCirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaEgCirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaEgCirPoolAvailBwIndex_Object = MibTableColumn
mscFrUniCaEgCirPoolAvailBwIndex = _MscFrUniCaEgCirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 671, 1, 1),
    _MscFrUniCaEgCirPoolAvailBwIndex_Type()
)
mscFrUniCaEgCirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrUniCaEgCirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrUniCaEgCirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrUniCaEgCirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaEgCirPoolAvailBwValue_Object = MibTableColumn
mscFrUniCaEgCirPoolAvailBwValue = _MscFrUniCaEgCirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 671, 1, 2),
    _MscFrUniCaEgCirPoolAvailBwValue_Type()
)
mscFrUniCaEgCirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaEgCirPoolAvailBwValue.setStatus("mandatory")
_MscFrUniCaIngEirBpTable_Object = MibTable
mscFrUniCaIngEirBpTable = _MscFrUniCaIngEirBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 673)
)
if mibBuilder.loadTexts:
    mscFrUniCaIngEirBpTable.setStatus("mandatory")
_MscFrUniCaIngEirBpEntry_Object = MibTableRow
mscFrUniCaIngEirBpEntry = _MscFrUniCaIngEirBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 673, 1)
)
mscFrUniCaIngEirBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIngEirBpIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaIngEirBpEntry.setStatus("mandatory")


class _MscFrUniCaIngEirBpIndex_Type(Integer32):
    """Custom type mscFrUniCaIngEirBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaIngEirBpIndex_Type.__name__ = "Integer32"
_MscFrUniCaIngEirBpIndex_Object = MibTableColumn
mscFrUniCaIngEirBpIndex = _MscFrUniCaIngEirBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 673, 1, 1),
    _MscFrUniCaIngEirBpIndex_Type()
)
mscFrUniCaIngEirBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaIngEirBpIndex.setStatus("mandatory")


class _MscFrUniCaIngEirBpValue_Type(Unsigned32):
    """Custom type mscFrUniCaIngEirBpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrUniCaIngEirBpValue_Type.__name__ = "Unsigned32"
_MscFrUniCaIngEirBpValue_Object = MibTableColumn
mscFrUniCaIngEirBpValue = _MscFrUniCaIngEirBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 673, 1, 2),
    _MscFrUniCaIngEirBpValue_Type()
)
mscFrUniCaIngEirBpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaIngEirBpValue.setStatus("mandatory")
_MscFrUniCaEgEirBpTable_Object = MibTable
mscFrUniCaEgEirBpTable = _MscFrUniCaEgEirBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 674)
)
if mibBuilder.loadTexts:
    mscFrUniCaEgEirBpTable.setStatus("mandatory")
_MscFrUniCaEgEirBpEntry_Object = MibTableRow
mscFrUniCaEgEirBpEntry = _MscFrUniCaEgEirBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 674, 1)
)
mscFrUniCaEgEirBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaEgEirBpIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaEgEirBpEntry.setStatus("mandatory")


class _MscFrUniCaEgEirBpIndex_Type(Integer32):
    """Custom type mscFrUniCaEgEirBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaEgEirBpIndex_Type.__name__ = "Integer32"
_MscFrUniCaEgEirBpIndex_Object = MibTableColumn
mscFrUniCaEgEirBpIndex = _MscFrUniCaEgEirBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 674, 1, 1),
    _MscFrUniCaEgEirBpIndex_Type()
)
mscFrUniCaEgEirBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaEgEirBpIndex.setStatus("mandatory")


class _MscFrUniCaEgEirBpValue_Type(Unsigned32):
    """Custom type mscFrUniCaEgEirBpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrUniCaEgEirBpValue_Type.__name__ = "Unsigned32"
_MscFrUniCaEgEirBpValue_Object = MibTableColumn
mscFrUniCaEgEirBpValue = _MscFrUniCaEgEirBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 674, 1, 2),
    _MscFrUniCaEgEirBpValue_Type()
)
mscFrUniCaEgEirBpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrUniCaEgEirBpValue.setStatus("mandatory")
_MscFrUniCaIngEirPoolAdmitBwTable_Object = MibTable
mscFrUniCaIngEirPoolAdmitBwTable = _MscFrUniCaIngEirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 675)
)
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAdmitBwTable.setStatus("mandatory")
_MscFrUniCaIngEirPoolAdmitBwEntry_Object = MibTableRow
mscFrUniCaIngEirPoolAdmitBwEntry = _MscFrUniCaIngEirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 675, 1)
)
mscFrUniCaIngEirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIngEirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrUniCaIngEirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrUniCaIngEirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaIngEirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaIngEirPoolAdmitBwIndex_Object = MibTableColumn
mscFrUniCaIngEirPoolAdmitBwIndex = _MscFrUniCaIngEirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 675, 1, 1),
    _MscFrUniCaIngEirPoolAdmitBwIndex_Type()
)
mscFrUniCaIngEirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrUniCaIngEirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrUniCaIngEirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrUniCaIngEirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaIngEirPoolAdmitBwValue_Object = MibTableColumn
mscFrUniCaIngEirPoolAdmitBwValue = _MscFrUniCaIngEirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 675, 1, 2),
    _MscFrUniCaIngEirPoolAdmitBwValue_Type()
)
mscFrUniCaIngEirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAdmitBwValue.setStatus("mandatory")
_MscFrUniCaIngEirPoolAvailBwTable_Object = MibTable
mscFrUniCaIngEirPoolAvailBwTable = _MscFrUniCaIngEirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 676)
)
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAvailBwTable.setStatus("mandatory")
_MscFrUniCaIngEirPoolAvailBwEntry_Object = MibTableRow
mscFrUniCaIngEirPoolAvailBwEntry = _MscFrUniCaIngEirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 676, 1)
)
mscFrUniCaIngEirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIngEirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrUniCaIngEirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrUniCaIngEirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaIngEirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaIngEirPoolAvailBwIndex_Object = MibTableColumn
mscFrUniCaIngEirPoolAvailBwIndex = _MscFrUniCaIngEirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 676, 1, 1),
    _MscFrUniCaIngEirPoolAvailBwIndex_Type()
)
mscFrUniCaIngEirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrUniCaIngEirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrUniCaIngEirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrUniCaIngEirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaIngEirPoolAvailBwValue_Object = MibTableColumn
mscFrUniCaIngEirPoolAvailBwValue = _MscFrUniCaIngEirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 676, 1, 2),
    _MscFrUniCaIngEirPoolAvailBwValue_Type()
)
mscFrUniCaIngEirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaIngEirPoolAvailBwValue.setStatus("mandatory")
_MscFrUniCaEgEirPoolAdmitBwTable_Object = MibTable
mscFrUniCaEgEirPoolAdmitBwTable = _MscFrUniCaEgEirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 677)
)
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAdmitBwTable.setStatus("mandatory")
_MscFrUniCaEgEirPoolAdmitBwEntry_Object = MibTableRow
mscFrUniCaEgEirPoolAdmitBwEntry = _MscFrUniCaEgEirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 677, 1)
)
mscFrUniCaEgEirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaEgEirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrUniCaEgEirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrUniCaEgEirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaEgEirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaEgEirPoolAdmitBwIndex_Object = MibTableColumn
mscFrUniCaEgEirPoolAdmitBwIndex = _MscFrUniCaEgEirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 677, 1, 1),
    _MscFrUniCaEgEirPoolAdmitBwIndex_Type()
)
mscFrUniCaEgEirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrUniCaEgEirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrUniCaEgEirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrUniCaEgEirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaEgEirPoolAdmitBwValue_Object = MibTableColumn
mscFrUniCaEgEirPoolAdmitBwValue = _MscFrUniCaEgEirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 677, 1, 2),
    _MscFrUniCaEgEirPoolAdmitBwValue_Type()
)
mscFrUniCaEgEirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAdmitBwValue.setStatus("mandatory")
_MscFrUniCaEgEirPoolAvailBwTable_Object = MibTable
mscFrUniCaEgEirPoolAvailBwTable = _MscFrUniCaEgEirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 678)
)
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAvailBwTable.setStatus("mandatory")
_MscFrUniCaEgEirPoolAvailBwEntry_Object = MibTableRow
mscFrUniCaEgEirPoolAvailBwEntry = _MscFrUniCaEgEirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 678, 1)
)
mscFrUniCaEgEirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniCaEgEirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrUniCaEgEirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrUniCaEgEirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrUniCaEgEirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrUniCaEgEirPoolAvailBwIndex_Object = MibTableColumn
mscFrUniCaEgEirPoolAvailBwIndex = _MscFrUniCaEgEirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 678, 1, 1),
    _MscFrUniCaEgEirPoolAvailBwIndex_Type()
)
mscFrUniCaEgEirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrUniCaEgEirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrUniCaEgEirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrUniCaEgEirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrUniCaEgEirPoolAvailBwValue_Object = MibTableColumn
mscFrUniCaEgEirPoolAvailBwValue = _MscFrUniCaEgEirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 101, 678, 1, 2),
    _MscFrUniCaEgEirPoolAvailBwValue_Type()
)
mscFrUniCaEgEirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniCaEgEirPoolAvailBwValue.setStatus("mandatory")
_MscFrUniFrmToIfByQueueTable_Object = MibTable
mscFrUniFrmToIfByQueueTable = _MscFrUniFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 341)
)
if mibBuilder.loadTexts:
    mscFrUniFrmToIfByQueueTable.setStatus("mandatory")
_MscFrUniFrmToIfByQueueEntry_Object = MibTableRow
mscFrUniFrmToIfByQueueEntry = _MscFrUniFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 341, 1)
)
mscFrUniFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniFrmToIfByQueueEntry.setStatus("mandatory")


class _MscFrUniFrmToIfByQueueIndex_Type(Integer32):
    """Custom type mscFrUniFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrUniFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_MscFrUniFrmToIfByQueueIndex_Object = MibTableColumn
mscFrUniFrmToIfByQueueIndex = _MscFrUniFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 341, 1, 1),
    _MscFrUniFrmToIfByQueueIndex_Type()
)
mscFrUniFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniFrmToIfByQueueIndex.setStatus("mandatory")


class _MscFrUniFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type mscFrUniFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscFrUniFrmToIfByQueueValue_Object = MibTableColumn
mscFrUniFrmToIfByQueueValue = _MscFrUniFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 341, 1, 2),
    _MscFrUniFrmToIfByQueueValue_Type()
)
mscFrUniFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniFrmToIfByQueueValue.setStatus("mandatory")
_MscFrUniOctetToIfByQueueTable_Object = MibTable
mscFrUniOctetToIfByQueueTable = _MscFrUniOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 342)
)
if mibBuilder.loadTexts:
    mscFrUniOctetToIfByQueueTable.setStatus("mandatory")
_MscFrUniOctetToIfByQueueEntry_Object = MibTableRow
mscFrUniOctetToIfByQueueEntry = _MscFrUniOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 342, 1)
)
mscFrUniOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB", "mscFrUniOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscFrUniOctetToIfByQueueEntry.setStatus("mandatory")


class _MscFrUniOctetToIfByQueueIndex_Type(Integer32):
    """Custom type mscFrUniOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrUniOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_MscFrUniOctetToIfByQueueIndex_Object = MibTableColumn
mscFrUniOctetToIfByQueueIndex = _MscFrUniOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 342, 1, 1),
    _MscFrUniOctetToIfByQueueIndex_Type()
)
mscFrUniOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrUniOctetToIfByQueueIndex.setStatus("mandatory")


class _MscFrUniOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type mscFrUniOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrUniOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscFrUniOctetToIfByQueueValue_Object = MibTableColumn
mscFrUniOctetToIfByQueueValue = _MscFrUniOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 71, 342, 1, 2),
    _MscFrUniOctetToIfByQueueValue_Type()
)
mscFrUniOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrUniOctetToIfByQueueValue.setStatus("mandatory")
_FrameRelayUniMIB_ObjectIdentity = ObjectIdentity
frameRelayUniMIB = _FrameRelayUniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24)
)
_FrameRelayUniGroup_ObjectIdentity = ObjectIdentity
frameRelayUniGroup = _FrameRelayUniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 1)
)
_FrameRelayUniGroupCA_ObjectIdentity = ObjectIdentity
frameRelayUniGroupCA = _FrameRelayUniGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 1, 1)
)
_FrameRelayUniGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayUniGroupCA02 = _FrameRelayUniGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 1, 1, 3)
)
_FrameRelayUniGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayUniGroupCA02A = _FrameRelayUniGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 1, 1, 3, 2)
)
_FrameRelayUniCapabilities_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilities = _FrameRelayUniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 3)
)
_FrameRelayUniCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilitiesCA = _FrameRelayUniCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 3, 1)
)
_FrameRelayUniCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilitiesCA02 = _FrameRelayUniCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 3, 1, 3)
)
_FrameRelayUniCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayUniCapabilitiesCA02A = _FrameRelayUniCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 24, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayUniMIB",
    **{"mscFrUni": mscFrUni,
       "mscFrUniRowStatusTable": mscFrUniRowStatusTable,
       "mscFrUniRowStatusEntry": mscFrUniRowStatusEntry,
       "mscFrUniRowStatus": mscFrUniRowStatus,
       "mscFrUniComponentName": mscFrUniComponentName,
       "mscFrUniStorageType": mscFrUniStorageType,
       "mscFrUniIndex": mscFrUniIndex,
       "mscFrUniDna": mscFrUniDna,
       "mscFrUniDnaRowStatusTable": mscFrUniDnaRowStatusTable,
       "mscFrUniDnaRowStatusEntry": mscFrUniDnaRowStatusEntry,
       "mscFrUniDnaRowStatus": mscFrUniDnaRowStatus,
       "mscFrUniDnaComponentName": mscFrUniDnaComponentName,
       "mscFrUniDnaStorageType": mscFrUniDnaStorageType,
       "mscFrUniDnaIndex": mscFrUniDnaIndex,
       "mscFrUniDnaCug": mscFrUniDnaCug,
       "mscFrUniDnaCugRowStatusTable": mscFrUniDnaCugRowStatusTable,
       "mscFrUniDnaCugRowStatusEntry": mscFrUniDnaCugRowStatusEntry,
       "mscFrUniDnaCugRowStatus": mscFrUniDnaCugRowStatus,
       "mscFrUniDnaCugComponentName": mscFrUniDnaCugComponentName,
       "mscFrUniDnaCugStorageType": mscFrUniDnaCugStorageType,
       "mscFrUniDnaCugIndex": mscFrUniDnaCugIndex,
       "mscFrUniDnaCugCugOptionsTable": mscFrUniDnaCugCugOptionsTable,
       "mscFrUniDnaCugCugOptionsEntry": mscFrUniDnaCugCugOptionsEntry,
       "mscFrUniDnaCugType": mscFrUniDnaCugType,
       "mscFrUniDnaCugDnic": mscFrUniDnaCugDnic,
       "mscFrUniDnaCugInterlockCode": mscFrUniDnaCugInterlockCode,
       "mscFrUniDnaCugPreferential": mscFrUniDnaCugPreferential,
       "mscFrUniDnaCugOutCalls": mscFrUniDnaCugOutCalls,
       "mscFrUniDnaCugIncCalls": mscFrUniDnaCugIncCalls,
       "mscFrUniDnaHgM": mscFrUniDnaHgM,
       "mscFrUniDnaHgMRowStatusTable": mscFrUniDnaHgMRowStatusTable,
       "mscFrUniDnaHgMRowStatusEntry": mscFrUniDnaHgMRowStatusEntry,
       "mscFrUniDnaHgMRowStatus": mscFrUniDnaHgMRowStatus,
       "mscFrUniDnaHgMComponentName": mscFrUniDnaHgMComponentName,
       "mscFrUniDnaHgMStorageType": mscFrUniDnaHgMStorageType,
       "mscFrUniDnaHgMIndex": mscFrUniDnaHgMIndex,
       "mscFrUniDnaHgMHgAddr": mscFrUniDnaHgMHgAddr,
       "mscFrUniDnaHgMHgAddrRowStatusTable": mscFrUniDnaHgMHgAddrRowStatusTable,
       "mscFrUniDnaHgMHgAddrRowStatusEntry": mscFrUniDnaHgMHgAddrRowStatusEntry,
       "mscFrUniDnaHgMHgAddrRowStatus": mscFrUniDnaHgMHgAddrRowStatus,
       "mscFrUniDnaHgMHgAddrComponentName": mscFrUniDnaHgMHgAddrComponentName,
       "mscFrUniDnaHgMHgAddrStorageType": mscFrUniDnaHgMHgAddrStorageType,
       "mscFrUniDnaHgMHgAddrIndex": mscFrUniDnaHgMHgAddrIndex,
       "mscFrUniDnaHgMHgAddrAddrTable": mscFrUniDnaHgMHgAddrAddrTable,
       "mscFrUniDnaHgMHgAddrAddrEntry": mscFrUniDnaHgMHgAddrAddrEntry,
       "mscFrUniDnaHgMHgAddrNumberingPlanIndicator": mscFrUniDnaHgMHgAddrNumberingPlanIndicator,
       "mscFrUniDnaHgMHgAddrDataNetworkAddress": mscFrUniDnaHgMHgAddrDataNetworkAddress,
       "mscFrUniDnaHgMIfTable": mscFrUniDnaHgMIfTable,
       "mscFrUniDnaHgMIfEntry": mscFrUniDnaHgMIfEntry,
       "mscFrUniDnaHgMAvailabilityUpdateThreshold": mscFrUniDnaHgMAvailabilityUpdateThreshold,
       "mscFrUniDnaHgMOpTable": mscFrUniDnaHgMOpTable,
       "mscFrUniDnaHgMOpEntry": mscFrUniDnaHgMOpEntry,
       "mscFrUniDnaHgMMaximumAvailableAggregateCir": mscFrUniDnaHgMMaximumAvailableAggregateCir,
       "mscFrUniDnaHgMAvailableAggregateCir": mscFrUniDnaHgMAvailableAggregateCir,
       "mscFrUniDnaHgMAvailabilityDelta": mscFrUniDnaHgMAvailabilityDelta,
       "mscFrUniDnaHgMAvailableDlcis": mscFrUniDnaHgMAvailableDlcis,
       "mscFrUniDnaAddressTable": mscFrUniDnaAddressTable,
       "mscFrUniDnaAddressEntry": mscFrUniDnaAddressEntry,
       "mscFrUniDnaNumberingPlanIndicator": mscFrUniDnaNumberingPlanIndicator,
       "mscFrUniDnaDataNetworkAddress": mscFrUniDnaDataNetworkAddress,
       "mscFrUniDnaOutgoingOptionsTable": mscFrUniDnaOutgoingOptionsTable,
       "mscFrUniDnaOutgoingOptionsEntry": mscFrUniDnaOutgoingOptionsEntry,
       "mscFrUniDnaOutDefaultPriority": mscFrUniDnaOutDefaultPriority,
       "mscFrUniDnaOutDefaultPathSensitivity": mscFrUniDnaOutDefaultPathSensitivity,
       "mscFrUniDnaOutPathSensitivityOverRide": mscFrUniDnaOutPathSensitivityOverRide,
       "mscFrUniDnaOutDefaultPathReliability": mscFrUniDnaOutDefaultPathReliability,
       "mscFrUniDnaOutAccess": mscFrUniDnaOutAccess,
       "mscFrUniDnaDefaultTransferPriority": mscFrUniDnaDefaultTransferPriority,
       "mscFrUniDnaTransferPriorityOverRide": mscFrUniDnaTransferPriorityOverRide,
       "mscFrUniDnaIncomingOptionsTable": mscFrUniDnaIncomingOptionsTable,
       "mscFrUniDnaIncomingOptionsEntry": mscFrUniDnaIncomingOptionsEntry,
       "mscFrUniDnaIncAccess": mscFrUniDnaIncAccess,
       "mscFrUniDnaCallOptionsTable": mscFrUniDnaCallOptionsTable,
       "mscFrUniDnaCallOptionsEntry": mscFrUniDnaCallOptionsEntry,
       "mscFrUniDnaAccountClass": mscFrUniDnaAccountClass,
       "mscFrUniDnaAccountCollection": mscFrUniDnaAccountCollection,
       "mscFrUniDnaServiceExchange": mscFrUniDnaServiceExchange,
       "mscFrUniDnaEgressAccounting": mscFrUniDnaEgressAccounting,
       "mscFrUniDnaDataPath": mscFrUniDnaDataPath,
       "mscFrUniFramer": mscFrUniFramer,
       "mscFrUniFramerRowStatusTable": mscFrUniFramerRowStatusTable,
       "mscFrUniFramerRowStatusEntry": mscFrUniFramerRowStatusEntry,
       "mscFrUniFramerRowStatus": mscFrUniFramerRowStatus,
       "mscFrUniFramerComponentName": mscFrUniFramerComponentName,
       "mscFrUniFramerStorageType": mscFrUniFramerStorageType,
       "mscFrUniFramerIndex": mscFrUniFramerIndex,
       "mscFrUniFramerProvTable": mscFrUniFramerProvTable,
       "mscFrUniFramerProvEntry": mscFrUniFramerProvEntry,
       "mscFrUniFramerInterfaceName": mscFrUniFramerInterfaceName,
       "mscFrUniFramerLinkTable": mscFrUniFramerLinkTable,
       "mscFrUniFramerLinkEntry": mscFrUniFramerLinkEntry,
       "mscFrUniFramerDataInversion": mscFrUniFramerDataInversion,
       "mscFrUniFramerFrameCrcType": mscFrUniFramerFrameCrcType,
       "mscFrUniFramerFlagsBetweenFrames": mscFrUniFramerFlagsBetweenFrames,
       "mscFrUniFramerStateTable": mscFrUniFramerStateTable,
       "mscFrUniFramerStateEntry": mscFrUniFramerStateEntry,
       "mscFrUniFramerAdminState": mscFrUniFramerAdminState,
       "mscFrUniFramerOperationalState": mscFrUniFramerOperationalState,
       "mscFrUniFramerUsageState": mscFrUniFramerUsageState,
       "mscFrUniFramerStatsTable": mscFrUniFramerStatsTable,
       "mscFrUniFramerStatsEntry": mscFrUniFramerStatsEntry,
       "mscFrUniFramerFrmToIf": mscFrUniFramerFrmToIf,
       "mscFrUniFramerFrmFromIf": mscFrUniFramerFrmFromIf,
       "mscFrUniFramerOctetFromIf": mscFrUniFramerOctetFromIf,
       "mscFrUniFramerAborts": mscFrUniFramerAborts,
       "mscFrUniFramerCrcErrors": mscFrUniFramerCrcErrors,
       "mscFrUniFramerLrcErrors": mscFrUniFramerLrcErrors,
       "mscFrUniFramerNonOctetErrors": mscFrUniFramerNonOctetErrors,
       "mscFrUniFramerOverruns": mscFrUniFramerOverruns,
       "mscFrUniFramerUnderruns": mscFrUniFramerUnderruns,
       "mscFrUniFramerLargeFrmErrors": mscFrUniFramerLargeFrmErrors,
       "mscFrUniFramerFrmModeErrors": mscFrUniFramerFrmModeErrors,
       "mscFrUniFramerFrmToIf64": mscFrUniFramerFrmToIf64,
       "mscFrUniFramerFrmFromIf64": mscFrUniFramerFrmFromIf64,
       "mscFrUniFramerOctetFromIf64": mscFrUniFramerOctetFromIf64,
       "mscFrUniFramerUtilTable": mscFrUniFramerUtilTable,
       "mscFrUniFramerUtilEntry": mscFrUniFramerUtilEntry,
       "mscFrUniFramerNormPrioLinkUtilToIf": mscFrUniFramerNormPrioLinkUtilToIf,
       "mscFrUniFramerNormPrioLinkUtilFromIf": mscFrUniFramerNormPrioLinkUtilFromIf,
       "mscFrUniLmi": mscFrUniLmi,
       "mscFrUniLmiRowStatusTable": mscFrUniLmiRowStatusTable,
       "mscFrUniLmiRowStatusEntry": mscFrUniLmiRowStatusEntry,
       "mscFrUniLmiRowStatus": mscFrUniLmiRowStatus,
       "mscFrUniLmiComponentName": mscFrUniLmiComponentName,
       "mscFrUniLmiStorageType": mscFrUniLmiStorageType,
       "mscFrUniLmiIndex": mscFrUniLmiIndex,
       "mscFrUniLmiParmsTable": mscFrUniLmiParmsTable,
       "mscFrUniLmiParmsEntry": mscFrUniLmiParmsEntry,
       "mscFrUniLmiProcedures": mscFrUniLmiProcedures,
       "mscFrUniLmiAsyncStatusReport": mscFrUniLmiAsyncStatusReport,
       "mscFrUniLmiErrorEventThreshold": mscFrUniLmiErrorEventThreshold,
       "mscFrUniLmiEventCount": mscFrUniLmiEventCount,
       "mscFrUniLmiCheckPointTimer": mscFrUniLmiCheckPointTimer,
       "mscFrUniLmiMessageCountTimer": mscFrUniLmiMessageCountTimer,
       "mscFrUniLmiIgnoreActiveBit": mscFrUniLmiIgnoreActiveBit,
       "mscFrUniLmiSide": mscFrUniLmiSide,
       "mscFrUniLmiPvcConfigParmsInFsr": mscFrUniLmiPvcConfigParmsInFsr,
       "mscFrUniLmiStateTable": mscFrUniLmiStateTable,
       "mscFrUniLmiStateEntry": mscFrUniLmiStateEntry,
       "mscFrUniLmiAdminState": mscFrUniLmiAdminState,
       "mscFrUniLmiOperationalState": mscFrUniLmiOperationalState,
       "mscFrUniLmiUsageState": mscFrUniLmiUsageState,
       "mscFrUniLmiPsiTable": mscFrUniLmiPsiTable,
       "mscFrUniLmiPsiEntry": mscFrUniLmiPsiEntry,
       "mscFrUniLmiProtocolStatus": mscFrUniLmiProtocolStatus,
       "mscFrUniLmiOpProcedures": mscFrUniLmiOpProcedures,
       "mscFrUniLmiStatsTable": mscFrUniLmiStatsTable,
       "mscFrUniLmiStatsEntry": mscFrUniLmiStatsEntry,
       "mscFrUniLmiKeepAliveStatusToIf": mscFrUniLmiKeepAliveStatusToIf,
       "mscFrUniLmiFullStatusToIf": mscFrUniLmiFullStatusToIf,
       "mscFrUniLmiKeepAliveStatusEnqFromIf": mscFrUniLmiKeepAliveStatusEnqFromIf,
       "mscFrUniLmiFullStatusEnqFromIf": mscFrUniLmiFullStatusEnqFromIf,
       "mscFrUniLmiNetworkSideEventHistory": mscFrUniLmiNetworkSideEventHistory,
       "mscFrUniLmiProtocolErrors": mscFrUniLmiProtocolErrors,
       "mscFrUniLmiUnexpectedIes": mscFrUniLmiUnexpectedIes,
       "mscFrUniLmiSequenceErrors": mscFrUniLmiSequenceErrors,
       "mscFrUniLmiUnexpectedReports": mscFrUniLmiUnexpectedReports,
       "mscFrUniLmiPollingVerifTimeouts": mscFrUniLmiPollingVerifTimeouts,
       "mscFrUniLmiKeepAliveEnqToIf": mscFrUniLmiKeepAliveEnqToIf,
       "mscFrUniLmiFullStatusEnqToIf": mscFrUniLmiFullStatusEnqToIf,
       "mscFrUniLmiUserSideEventHistory": mscFrUniLmiUserSideEventHistory,
       "mscFrUniLmiStatusSequenceErrors": mscFrUniLmiStatusSequenceErrors,
       "mscFrUniLmiNoStatusReportCount": mscFrUniLmiNoStatusReportCount,
       "mscFrUniLmiUspParmsTable": mscFrUniLmiUspParmsTable,
       "mscFrUniLmiUspParmsEntry": mscFrUniLmiUspParmsEntry,
       "mscFrUniLmiFullStatusPollingCycles": mscFrUniLmiFullStatusPollingCycles,
       "mscFrUniLmiLinkVerificationTimer": mscFrUniLmiLinkVerificationTimer,
       "mscFrUniDlci": mscFrUniDlci,
       "mscFrUniDlciRowStatusTable": mscFrUniDlciRowStatusTable,
       "mscFrUniDlciRowStatusEntry": mscFrUniDlciRowStatusEntry,
       "mscFrUniDlciRowStatus": mscFrUniDlciRowStatus,
       "mscFrUniDlciComponentName": mscFrUniDlciComponentName,
       "mscFrUniDlciStorageType": mscFrUniDlciStorageType,
       "mscFrUniDlciIndex": mscFrUniDlciIndex,
       "mscFrUniDlciDc": mscFrUniDlciDc,
       "mscFrUniDlciDcRowStatusTable": mscFrUniDlciDcRowStatusTable,
       "mscFrUniDlciDcRowStatusEntry": mscFrUniDlciDcRowStatusEntry,
       "mscFrUniDlciDcRowStatus": mscFrUniDlciDcRowStatus,
       "mscFrUniDlciDcComponentName": mscFrUniDlciDcComponentName,
       "mscFrUniDlciDcStorageType": mscFrUniDlciDcStorageType,
       "mscFrUniDlciDcIndex": mscFrUniDlciDcIndex,
       "mscFrUniDlciDcOptionsTable": mscFrUniDlciDcOptionsTable,
       "mscFrUniDlciDcOptionsEntry": mscFrUniDlciDcOptionsEntry,
       "mscFrUniDlciDcRemoteNpi": mscFrUniDlciDcRemoteNpi,
       "mscFrUniDlciDcRemoteDna": mscFrUniDlciDcRemoteDna,
       "mscFrUniDlciDcRemoteDlci": mscFrUniDlciDcRemoteDlci,
       "mscFrUniDlciDcType": mscFrUniDlciDcType,
       "mscFrUniDlciDcTransferPriority": mscFrUniDlciDcTransferPriority,
       "mscFrUniDlciDcDiscardPriority": mscFrUniDlciDcDiscardPriority,
       "mscFrUniDlciDcDeDiscardPriority": mscFrUniDlciDcDeDiscardPriority,
       "mscFrUniDlciDcDataPath": mscFrUniDlciDcDataPath,
       "mscFrUniDlciDcCugIndex": mscFrUniDlciDcCugIndex,
       "mscFrUniDlciDcCugType": mscFrUniDlciDcCugType,
       "mscFrUniDlciDcMapIpCosToFrQos": mscFrUniDlciDcMapIpCosToFrQos,
       "mscFrUniDlciDcNfaTable": mscFrUniDlciDcNfaTable,
       "mscFrUniDlciDcNfaEntry": mscFrUniDlciDcNfaEntry,
       "mscFrUniDlciDcNfaIndex": mscFrUniDlciDcNfaIndex,
       "mscFrUniDlciDcNfaValue": mscFrUniDlciDcNfaValue,
       "mscFrUniDlciDcNfaRowStatus": mscFrUniDlciDcNfaRowStatus,
       "mscFrUniDlciVc": mscFrUniDlciVc,
       "mscFrUniDlciVcRowStatusTable": mscFrUniDlciVcRowStatusTable,
       "mscFrUniDlciVcRowStatusEntry": mscFrUniDlciVcRowStatusEntry,
       "mscFrUniDlciVcRowStatus": mscFrUniDlciVcRowStatus,
       "mscFrUniDlciVcComponentName": mscFrUniDlciVcComponentName,
       "mscFrUniDlciVcStorageType": mscFrUniDlciVcStorageType,
       "mscFrUniDlciVcIndex": mscFrUniDlciVcIndex,
       "mscFrUniDlciVcCadTable": mscFrUniDlciVcCadTable,
       "mscFrUniDlciVcCadEntry": mscFrUniDlciVcCadEntry,
       "mscFrUniDlciVcType": mscFrUniDlciVcType,
       "mscFrUniDlciVcState": mscFrUniDlciVcState,
       "mscFrUniDlciVcPreviousState": mscFrUniDlciVcPreviousState,
       "mscFrUniDlciVcDiagnosticCode": mscFrUniDlciVcDiagnosticCode,
       "mscFrUniDlciVcPreviousDiagnosticCode": mscFrUniDlciVcPreviousDiagnosticCode,
       "mscFrUniDlciVcCalledNpi": mscFrUniDlciVcCalledNpi,
       "mscFrUniDlciVcCalledDna": mscFrUniDlciVcCalledDna,
       "mscFrUniDlciVcCalledLcn": mscFrUniDlciVcCalledLcn,
       "mscFrUniDlciVcCallingNpi": mscFrUniDlciVcCallingNpi,
       "mscFrUniDlciVcCallingDna": mscFrUniDlciVcCallingDna,
       "mscFrUniDlciVcCallingLcn": mscFrUniDlciVcCallingLcn,
       "mscFrUniDlciVcAccountingEnabled": mscFrUniDlciVcAccountingEnabled,
       "mscFrUniDlciVcFastSelectCall": mscFrUniDlciVcFastSelectCall,
       "mscFrUniDlciVcPathReliability": mscFrUniDlciVcPathReliability,
       "mscFrUniDlciVcAccountingEnd": mscFrUniDlciVcAccountingEnd,
       "mscFrUniDlciVcPriority": mscFrUniDlciVcPriority,
       "mscFrUniDlciVcSegmentSize": mscFrUniDlciVcSegmentSize,
       "mscFrUniDlciVcMaxSubnetPktSize": mscFrUniDlciVcMaxSubnetPktSize,
       "mscFrUniDlciVcRcosToNetwork": mscFrUniDlciVcRcosToNetwork,
       "mscFrUniDlciVcRcosFromNetwork": mscFrUniDlciVcRcosFromNetwork,
       "mscFrUniDlciVcEmissionPriorityToNetwork": mscFrUniDlciVcEmissionPriorityToNetwork,
       "mscFrUniDlciVcEmissionPriorityFromNetwork": mscFrUniDlciVcEmissionPriorityFromNetwork,
       "mscFrUniDlciVcDataPath": mscFrUniDlciVcDataPath,
       "mscFrUniDlciVcIntdTable": mscFrUniDlciVcIntdTable,
       "mscFrUniDlciVcIntdEntry": mscFrUniDlciVcIntdEntry,
       "mscFrUniDlciVcCallReferenceNumber": mscFrUniDlciVcCallReferenceNumber,
       "mscFrUniDlciVcElapsedTimeTillNow": mscFrUniDlciVcElapsedTimeTillNow,
       "mscFrUniDlciVcSegmentsRx": mscFrUniDlciVcSegmentsRx,
       "mscFrUniDlciVcSegmentsSent": mscFrUniDlciVcSegmentsSent,
       "mscFrUniDlciVcStartTime": mscFrUniDlciVcStartTime,
       "mscFrUniDlciVcCallReferenceNumberDecimal": mscFrUniDlciVcCallReferenceNumberDecimal,
       "mscFrUniDlciVcFrdTable": mscFrUniDlciVcFrdTable,
       "mscFrUniDlciVcFrdEntry": mscFrUniDlciVcFrdEntry,
       "mscFrUniDlciVcFrmCongestedToSubnet": mscFrUniDlciVcFrmCongestedToSubnet,
       "mscFrUniDlciVcCannotForwardToSubnet": mscFrUniDlciVcCannotForwardToSubnet,
       "mscFrUniDlciVcNotDataXferToSubnet": mscFrUniDlciVcNotDataXferToSubnet,
       "mscFrUniDlciVcOutOfRangeFrmFromSubnet": mscFrUniDlciVcOutOfRangeFrmFromSubnet,
       "mscFrUniDlciVcCombErrorsFromSubnet": mscFrUniDlciVcCombErrorsFromSubnet,
       "mscFrUniDlciVcDuplicatesFromSubnet": mscFrUniDlciVcDuplicatesFromSubnet,
       "mscFrUniDlciVcNotDataXferFromSubnet": mscFrUniDlciVcNotDataXferFromSubnet,
       "mscFrUniDlciVcFrmLossTimeouts": mscFrUniDlciVcFrmLossTimeouts,
       "mscFrUniDlciVcOoSeqByteCntExceeded": mscFrUniDlciVcOoSeqByteCntExceeded,
       "mscFrUniDlciVcPeakOoSeqPktCount": mscFrUniDlciVcPeakOoSeqPktCount,
       "mscFrUniDlciVcPeakOoSeqFrmForwarded": mscFrUniDlciVcPeakOoSeqFrmForwarded,
       "mscFrUniDlciVcSendSequenceNumber": mscFrUniDlciVcSendSequenceNumber,
       "mscFrUniDlciVcPktRetryTimeouts": mscFrUniDlciVcPktRetryTimeouts,
       "mscFrUniDlciVcPeakRetryQueueSize": mscFrUniDlciVcPeakRetryQueueSize,
       "mscFrUniDlciVcSubnetRecoveries": mscFrUniDlciVcSubnetRecoveries,
       "mscFrUniDlciVcOoSeqPktCntExceeded": mscFrUniDlciVcOoSeqPktCntExceeded,
       "mscFrUniDlciVcPeakOoSeqByteCount": mscFrUniDlciVcPeakOoSeqByteCount,
       "mscFrUniDlciVcDmepTable": mscFrUniDlciVcDmepTable,
       "mscFrUniDlciVcDmepEntry": mscFrUniDlciVcDmepEntry,
       "mscFrUniDlciVcDmepValue": mscFrUniDlciVcDmepValue,
       "mscFrUniDlciSp": mscFrUniDlciSp,
       "mscFrUniDlciSpRowStatusTable": mscFrUniDlciSpRowStatusTable,
       "mscFrUniDlciSpRowStatusEntry": mscFrUniDlciSpRowStatusEntry,
       "mscFrUniDlciSpRowStatus": mscFrUniDlciSpRowStatus,
       "mscFrUniDlciSpComponentName": mscFrUniDlciSpComponentName,
       "mscFrUniDlciSpStorageType": mscFrUniDlciSpStorageType,
       "mscFrUniDlciSpIndex": mscFrUniDlciSpIndex,
       "mscFrUniDlciSpParmsTable": mscFrUniDlciSpParmsTable,
       "mscFrUniDlciSpParmsEntry": mscFrUniDlciSpParmsEntry,
       "mscFrUniDlciSpMaximumFrameSize": mscFrUniDlciSpMaximumFrameSize,
       "mscFrUniDlciSpRateEnforcement": mscFrUniDlciSpRateEnforcement,
       "mscFrUniDlciSpCommittedInformationRate": mscFrUniDlciSpCommittedInformationRate,
       "mscFrUniDlciSpCommittedBurstSize": mscFrUniDlciSpCommittedBurstSize,
       "mscFrUniDlciSpExcessBurstSize": mscFrUniDlciSpExcessBurstSize,
       "mscFrUniDlciSpMeasurementInterval": mscFrUniDlciSpMeasurementInterval,
       "mscFrUniDlciSpRateAdaptation": mscFrUniDlciSpRateAdaptation,
       "mscFrUniDlciSpAccounting": mscFrUniDlciSpAccounting,
       "mscFrUniDlciSpRaSensitivity": mscFrUniDlciSpRaSensitivity,
       "mscFrUniDlciSpUpdateBCI": mscFrUniDlciSpUpdateBCI,
       "mscFrUniDlciLb": mscFrUniDlciLb,
       "mscFrUniDlciLbRowStatusTable": mscFrUniDlciLbRowStatusTable,
       "mscFrUniDlciLbRowStatusEntry": mscFrUniDlciLbRowStatusEntry,
       "mscFrUniDlciLbRowStatus": mscFrUniDlciLbRowStatus,
       "mscFrUniDlciLbComponentName": mscFrUniDlciLbComponentName,
       "mscFrUniDlciLbStorageType": mscFrUniDlciLbStorageType,
       "mscFrUniDlciLbIndex": mscFrUniDlciLbIndex,
       "mscFrUniDlciLbStatsTable": mscFrUniDlciLbStatsTable,
       "mscFrUniDlciLbStatsEntry": mscFrUniDlciLbStatsEntry,
       "mscFrUniDlciLbLocalTotalFrm": mscFrUniDlciLbLocalTotalFrm,
       "mscFrUniDlciLbLocalTotalBytes": mscFrUniDlciLbLocalTotalBytes,
       "mscFrUniDlciLbLocalFecnFrm": mscFrUniDlciLbLocalFecnFrm,
       "mscFrUniDlciLbLocalBecnFrm": mscFrUniDlciLbLocalBecnFrm,
       "mscFrUniDlciLbLocalDeFrm": mscFrUniDlciLbLocalDeFrm,
       "mscFrUniDlciLbLocalDeBytes": mscFrUniDlciLbLocalDeBytes,
       "mscFrUniDlciLbRemoteTotalFrm": mscFrUniDlciLbRemoteTotalFrm,
       "mscFrUniDlciLbRemoteTotalBytes": mscFrUniDlciLbRemoteTotalBytes,
       "mscFrUniDlciLbRemoteFecnFrm": mscFrUniDlciLbRemoteFecnFrm,
       "mscFrUniDlciLbRemoteBecnFrm": mscFrUniDlciLbRemoteBecnFrm,
       "mscFrUniDlciLbRemoteDeFrm": mscFrUniDlciLbRemoteDeFrm,
       "mscFrUniDlciLbRemoteDeBytes": mscFrUniDlciLbRemoteDeBytes,
       "mscFrUniDlciEgressSp": mscFrUniDlciEgressSp,
       "mscFrUniDlciEgressSpRowStatusTable": mscFrUniDlciEgressSpRowStatusTable,
       "mscFrUniDlciEgressSpRowStatusEntry": mscFrUniDlciEgressSpRowStatusEntry,
       "mscFrUniDlciEgressSpRowStatus": mscFrUniDlciEgressSpRowStatus,
       "mscFrUniDlciEgressSpComponentName": mscFrUniDlciEgressSpComponentName,
       "mscFrUniDlciEgressSpStorageType": mscFrUniDlciEgressSpStorageType,
       "mscFrUniDlciEgressSpIndex": mscFrUniDlciEgressSpIndex,
       "mscFrUniDlciEgressSpProvTable": mscFrUniDlciEgressSpProvTable,
       "mscFrUniDlciEgressSpProvEntry": mscFrUniDlciEgressSpProvEntry,
       "mscFrUniDlciEgressSpCommittedInformationRate": mscFrUniDlciEgressSpCommittedInformationRate,
       "mscFrUniDlciEgressSpCommittedBurstSize": mscFrUniDlciEgressSpCommittedBurstSize,
       "mscFrUniDlciEgressSpExcessBurstSize": mscFrUniDlciEgressSpExcessBurstSize,
       "mscFrUniDlciEgressSpMeasurementInterval": mscFrUniDlciEgressSpMeasurementInterval,
       "mscFrUniDlciStateTable": mscFrUniDlciStateTable,
       "mscFrUniDlciStateEntry": mscFrUniDlciStateEntry,
       "mscFrUniDlciAdminState": mscFrUniDlciAdminState,
       "mscFrUniDlciOperationalState": mscFrUniDlciOperationalState,
       "mscFrUniDlciUsageState": mscFrUniDlciUsageState,
       "mscFrUniDlciAvailabilityStatus": mscFrUniDlciAvailabilityStatus,
       "mscFrUniDlciProceduralStatus": mscFrUniDlciProceduralStatus,
       "mscFrUniDlciControlStatus": mscFrUniDlciControlStatus,
       "mscFrUniDlciAlarmStatus": mscFrUniDlciAlarmStatus,
       "mscFrUniDlciStandbyStatus": mscFrUniDlciStandbyStatus,
       "mscFrUniDlciUnknownStatus": mscFrUniDlciUnknownStatus,
       "mscFrUniDlciAbitTable": mscFrUniDlciAbitTable,
       "mscFrUniDlciAbitEntry": mscFrUniDlciAbitEntry,
       "mscFrUniDlciABitStatusToIf": mscFrUniDlciABitStatusToIf,
       "mscFrUniDlciABitReasonToIf": mscFrUniDlciABitReasonToIf,
       "mscFrUniDlciABitStatusFromIf": mscFrUniDlciABitStatusFromIf,
       "mscFrUniDlciABitReasonFromIf": mscFrUniDlciABitReasonFromIf,
       "mscFrUniDlciLoopbackState": mscFrUniDlciLoopbackState,
       "mscFrUniDlciCalldTable": mscFrUniDlciCalldTable,
       "mscFrUniDlciCalldEntry": mscFrUniDlciCalldEntry,
       "mscFrUniDlciCallType": mscFrUniDlciCallType,
       "mscFrUniDlciQstate": mscFrUniDlciQstate,
       "mscFrUniDlciCallref": mscFrUniDlciCallref,
       "mscFrUniDlciSpOpTable": mscFrUniDlciSpOpTable,
       "mscFrUniDlciSpOpEntry": mscFrUniDlciSpOpEntry,
       "mscFrUniDlciMaximumFrameSize": mscFrUniDlciMaximumFrameSize,
       "mscFrUniDlciRateEnforcement": mscFrUniDlciRateEnforcement,
       "mscFrUniDlciCommittedInformationRate": mscFrUniDlciCommittedInformationRate,
       "mscFrUniDlciCommittedBurstSize": mscFrUniDlciCommittedBurstSize,
       "mscFrUniDlciExcessBurstSize": mscFrUniDlciExcessBurstSize,
       "mscFrUniDlciMeasurementInterval": mscFrUniDlciMeasurementInterval,
       "mscFrUniDlciRateAdaptation": mscFrUniDlciRateAdaptation,
       "mscFrUniDlciAccounting": mscFrUniDlciAccounting,
       "mscFrUniDlciEmissionPriorityToIf": mscFrUniDlciEmissionPriorityToIf,
       "mscFrUniDlciTransferPriToNwk": mscFrUniDlciTransferPriToNwk,
       "mscFrUniDlciTransferPriFromNwk": mscFrUniDlciTransferPriFromNwk,
       "mscFrUniDlciStatsTable": mscFrUniDlciStatsTable,
       "mscFrUniDlciStatsEntry": mscFrUniDlciStatsEntry,
       "mscFrUniDlciFrmToIf": mscFrUniDlciFrmToIf,
       "mscFrUniDlciFecnFrmToIf": mscFrUniDlciFecnFrmToIf,
       "mscFrUniDlciBecnFrmToIf": mscFrUniDlciBecnFrmToIf,
       "mscFrUniDlciBciToSubnet": mscFrUniDlciBciToSubnet,
       "mscFrUniDlciDeFrmToIf": mscFrUniDlciDeFrmToIf,
       "mscFrUniDlciDiscCongestedToIf": mscFrUniDlciDiscCongestedToIf,
       "mscFrUniDlciDiscDeCongestedToIf": mscFrUniDlciDiscDeCongestedToIf,
       "mscFrUniDlciFrmFromIf": mscFrUniDlciFrmFromIf,
       "mscFrUniDlciFecnFrmFromIf": mscFrUniDlciFecnFrmFromIf,
       "mscFrUniDlciBecnFrmFromIf": mscFrUniDlciBecnFrmFromIf,
       "mscFrUniDlciFciFromSubnet": mscFrUniDlciFciFromSubnet,
       "mscFrUniDlciBciFromSubnet": mscFrUniDlciBciFromSubnet,
       "mscFrUniDlciDeFrmFromIf": mscFrUniDlciDeFrmFromIf,
       "mscFrUniDlciExcessFrmFromIf": mscFrUniDlciExcessFrmFromIf,
       "mscFrUniDlciDiscExcessFromIf": mscFrUniDlciDiscExcessFromIf,
       "mscFrUniDlciDiscFrameAbit": mscFrUniDlciDiscFrameAbit,
       "mscFrUniDlciDiscCongestedFromIf": mscFrUniDlciDiscCongestedFromIf,
       "mscFrUniDlciDiscDeCongestedFromIf": mscFrUniDlciDiscDeCongestedFromIf,
       "mscFrUniDlciErrorShortFrmFromIf": mscFrUniDlciErrorShortFrmFromIf,
       "mscFrUniDlciErrorLongFrmFromIf": mscFrUniDlciErrorLongFrmFromIf,
       "mscFrUniDlciBecnFrmSetByService": mscFrUniDlciBecnFrmSetByService,
       "mscFrUniDlciBytesToIf": mscFrUniDlciBytesToIf,
       "mscFrUniDlciDeBytesToIf": mscFrUniDlciDeBytesToIf,
       "mscFrUniDlciDiscCongestedToIfBytes": mscFrUniDlciDiscCongestedToIfBytes,
       "mscFrUniDlciDiscDeCongestedToIfBytes": mscFrUniDlciDiscDeCongestedToIfBytes,
       "mscFrUniDlciBytesFromIf": mscFrUniDlciBytesFromIf,
       "mscFrUniDlciDeBytesFromIf": mscFrUniDlciDeBytesFromIf,
       "mscFrUniDlciExcessBytesFromIf": mscFrUniDlciExcessBytesFromIf,
       "mscFrUniDlciDiscExcessFromIfBytes": mscFrUniDlciDiscExcessFromIfBytes,
       "mscFrUniDlciDiscByteAbit": mscFrUniDlciDiscByteAbit,
       "mscFrUniDlciDiscCongestedFromIfBytes": mscFrUniDlciDiscCongestedFromIfBytes,
       "mscFrUniDlciDiscDeCongestedFromIfBytes": mscFrUniDlciDiscDeCongestedFromIfBytes,
       "mscFrUniDlciErrorShortBytesFromIf": mscFrUniDlciErrorShortBytesFromIf,
       "mscFrUniDlciErrorLongBytesFromIf": mscFrUniDlciErrorLongBytesFromIf,
       "mscFrUniDlciRateAdaptReduct": mscFrUniDlciRateAdaptReduct,
       "mscFrUniDlciRateAdaptReductPeriod": mscFrUniDlciRateAdaptReductPeriod,
       "mscFrUniDlciTransferPriorityToNetwork": mscFrUniDlciTransferPriorityToNetwork,
       "mscFrUniDlciTransferPriorityFromNetwork": mscFrUniDlciTransferPriorityFromNetwork,
       "mscFrUniDlciCirPresent": mscFrUniDlciCirPresent,
       "mscFrUniDlciEirPresent": mscFrUniDlciEirPresent,
       "mscFrUniDlciIntTable": mscFrUniDlciIntTable,
       "mscFrUniDlciIntEntry": mscFrUniDlciIntEntry,
       "mscFrUniDlciStartTime": mscFrUniDlciStartTime,
       "mscFrUniDlciTotalIngressBytes": mscFrUniDlciTotalIngressBytes,
       "mscFrUniDlciTotalEgressBytes": mscFrUniDlciTotalEgressBytes,
       "mscFrUniDlciEirIngressBytes": mscFrUniDlciEirIngressBytes,
       "mscFrUniDlciEirEgressBytes": mscFrUniDlciEirEgressBytes,
       "mscFrUniDlciDiscardedBytes": mscFrUniDlciDiscardedBytes,
       "mscFrUniDlciTotalIngressSegFrm": mscFrUniDlciTotalIngressSegFrm,
       "mscFrUniDlciTotalEgressSegFrm": mscFrUniDlciTotalEgressSegFrm,
       "mscFrUniDlciEirIngressSegFrm": mscFrUniDlciEirIngressSegFrm,
       "mscFrUniDlciEirEgressSegFrm": mscFrUniDlciEirEgressSegFrm,
       "mscFrUniDlciDiscardedSegFrm": mscFrUniDlciDiscardedSegFrm,
       "mscFrUniDlciCirPresentObs": mscFrUniDlciCirPresentObs,
       "mscFrUniDlciEirPresentObs": mscFrUniDlciEirPresentObs,
       "mscFrUniDlciRateEnforcementPresent": mscFrUniDlciRateEnforcementPresent,
       "mscFrUniDlciRateAdaptationPresent": mscFrUniDlciRateAdaptationPresent,
       "mscFrUniDlciLocalRateAdaptOccurred": mscFrUniDlciLocalRateAdaptOccurred,
       "mscFrUniDlciCallReferenceNumber": mscFrUniDlciCallReferenceNumber,
       "mscFrUniDlciElapsedDifference": mscFrUniDlciElapsedDifference,
       "mscFrUniDlciCallRefNumber": mscFrUniDlciCallRefNumber,
       "mscFrUniSig": mscFrUniSig,
       "mscFrUniSigRowStatusTable": mscFrUniSigRowStatusTable,
       "mscFrUniSigRowStatusEntry": mscFrUniSigRowStatusEntry,
       "mscFrUniSigRowStatus": mscFrUniSigRowStatus,
       "mscFrUniSigComponentName": mscFrUniSigComponentName,
       "mscFrUniSigStorageType": mscFrUniSigStorageType,
       "mscFrUniSigIndex": mscFrUniSigIndex,
       "mscFrUniSigRangeTable": mscFrUniSigRangeTable,
       "mscFrUniSigRangeEntry": mscFrUniSigRangeEntry,
       "mscFrUniSigHighestPvcDlci": mscFrUniSigHighestPvcDlci,
       "mscFrUniSigHighestPermanentDlci": mscFrUniSigHighestPermanentDlci,
       "mscFrUniSigHighestFriPvcDlci": mscFrUniSigHighestFriPvcDlci,
       "mscFrUniSigServParmsTable": mscFrUniSigServParmsTable,
       "mscFrUniSigServParmsEntry": mscFrUniSigServParmsEntry,
       "mscFrUniSigMaximumAggregateSvcCir": mscFrUniSigMaximumAggregateSvcCir,
       "mscFrUniSigMaximumAggregateSvcEir": mscFrUniSigMaximumAggregateSvcEir,
       "mscFrUniSigMaximumFrameSize": mscFrUniSigMaximumFrameSize,
       "mscFrUniSigDefaultMaximumFrameSize": mscFrUniSigDefaultMaximumFrameSize,
       "mscFrUniSigDefaultCommittedInformationRate": mscFrUniSigDefaultCommittedInformationRate,
       "mscFrUniSigDefaultCommittedBurstSize": mscFrUniSigDefaultCommittedBurstSize,
       "mscFrUniSigDefaultExcessBurstSize": mscFrUniSigDefaultExcessBurstSize,
       "mscFrUniSigUnlimitedAggregateEir": mscFrUniSigUnlimitedAggregateEir,
       "mscFrUniSigRateEnforcement": mscFrUniSigRateEnforcement,
       "mscFrUniSigRateAdaptation": mscFrUniSigRateAdaptation,
       "mscFrUniSigMaximumAggregateSvcCirNormalQ": mscFrUniSigMaximumAggregateSvcCirNormalQ,
       "mscFrUniSigMaximumAggregateSvcCirHighQ": mscFrUniSigMaximumAggregateSvcCirHighQ,
       "mscFrUniSigMaximumAggregateSvcCirInterruptQ": mscFrUniSigMaximumAggregateSvcCirInterruptQ,
       "mscFrUniSigMaximumAggregateSvcEirNormalQ": mscFrUniSigMaximumAggregateSvcEirNormalQ,
       "mscFrUniSigMaximumAggregateSvcEirHighQ": mscFrUniSigMaximumAggregateSvcEirHighQ,
       "mscFrUniSigMaximumAggregateSvcEirInterruptQ": mscFrUniSigMaximumAggregateSvcEirInterruptQ,
       "mscFrUniSigX213IeHandling": mscFrUniSigX213IeHandling,
       "mscFrUniSigRaSensitivity": mscFrUniSigRaSensitivity,
       "mscFrUniSigUpdateBCI": mscFrUniSigUpdateBCI,
       "mscFrUniSigDefaultLocCheck": mscFrUniSigDefaultLocCheck,
       "mscFrUniSigSysParmsTable": mscFrUniSigSysParmsTable,
       "mscFrUniSigSysParmsEntry": mscFrUniSigSysParmsEntry,
       "mscFrUniSigCallSetupTimer": mscFrUniSigCallSetupTimer,
       "mscFrUniSigDisconnectTimer": mscFrUniSigDisconnectTimer,
       "mscFrUniSigReleaseTimer": mscFrUniSigReleaseTimer,
       "mscFrUniSigCallProceedingTimer": mscFrUniSigCallProceedingTimer,
       "mscFrUniSigNetworkType": mscFrUniSigNetworkType,
       "mscFrUniSigRestartReqTimer": mscFrUniSigRestartReqTimer,
       "mscFrUniSigRestartRcvTimer": mscFrUniSigRestartRcvTimer,
       "mscFrUniSigStatusEnqTimer": mscFrUniSigStatusEnqTimer,
       "mscFrUniSigLapfSysTable": mscFrUniSigLapfSysTable,
       "mscFrUniSigLapfSysEntry": mscFrUniSigLapfSysEntry,
       "mscFrUniSigWindowSize": mscFrUniSigWindowSize,
       "mscFrUniSigRetransmitLimit": mscFrUniSigRetransmitLimit,
       "mscFrUniSigAckTimer": mscFrUniSigAckTimer,
       "mscFrUniSigAckDelayTimer": mscFrUniSigAckDelayTimer,
       "mscFrUniSigIdleProbeTimer": mscFrUniSigIdleProbeTimer,
       "mscFrUniSigStateTable": mscFrUniSigStateTable,
       "mscFrUniSigStateEntry": mscFrUniSigStateEntry,
       "mscFrUniSigAdminState": mscFrUniSigAdminState,
       "mscFrUniSigOperationalState": mscFrUniSigOperationalState,
       "mscFrUniSigUsageState": mscFrUniSigUsageState,
       "mscFrUniSigStatsTable": mscFrUniSigStatsTable,
       "mscFrUniSigStatsEntry": mscFrUniSigStatsEntry,
       "mscFrUniSigCurrentNumberOfSvcCalls": mscFrUniSigCurrentNumberOfSvcCalls,
       "mscFrUniSigInCalls": mscFrUniSigInCalls,
       "mscFrUniSigInCallsRefused": mscFrUniSigInCallsRefused,
       "mscFrUniSigOutCalls": mscFrUniSigOutCalls,
       "mscFrUniSigOutCallsFailed": mscFrUniSigOutCallsFailed,
       "mscFrUniSigProtocolErrors": mscFrUniSigProtocolErrors,
       "mscFrUniSigQualityOfServiceNotAvailable": mscFrUniSigQualityOfServiceNotAvailable,
       "mscFrUniSigSetupTimeout": mscFrUniSigSetupTimeout,
       "mscFrUniSigLastCauseInStatusMsgReceived": mscFrUniSigLastCauseInStatusMsgReceived,
       "mscFrUniSigLastStateInStatusMsgReceived": mscFrUniSigLastStateInStatusMsgReceived,
       "mscFrUniSigLastDlciReceivedStatus": mscFrUniSigLastDlciReceivedStatus,
       "mscFrUniSigLastStateReceivedStatus": mscFrUniSigLastStateReceivedStatus,
       "mscFrUniSigLastTimeMsgBlockCongested": mscFrUniSigLastTimeMsgBlockCongested,
       "mscFrUniSigLastDlciWithMsgBlockCongestion": mscFrUniSigLastDlciWithMsgBlockCongestion,
       "mscFrUniSigCurrentAggregateSvcCirNormalQ": mscFrUniSigCurrentAggregateSvcCirNormalQ,
       "mscFrUniSigCurrentAggregateSvcCirHighQ": mscFrUniSigCurrentAggregateSvcCirHighQ,
       "mscFrUniSigCurrentAggregateSvcCirInterruptQ": mscFrUniSigCurrentAggregateSvcCirInterruptQ,
       "mscFrUniSigCurrentAggregateSvcEirNormalQ": mscFrUniSigCurrentAggregateSvcEirNormalQ,
       "mscFrUniSigCurrentAggregateSvcEirHighQ": mscFrUniSigCurrentAggregateSvcEirHighQ,
       "mscFrUniSigCurrentAggregateSvcEirInterruptQ": mscFrUniSigCurrentAggregateSvcEirInterruptQ,
       "mscFrUniSigLapfStatusTable": mscFrUniSigLapfStatusTable,
       "mscFrUniSigLapfStatusEntry": mscFrUniSigLapfStatusEntry,
       "mscFrUniSigCurrentState": mscFrUniSigCurrentState,
       "mscFrUniSigLastStateChangeReason": mscFrUniSigLastStateChangeReason,
       "mscFrUniSigFrmrReceive": mscFrUniSigFrmrReceive,
       "mscFrUniSigCurrentQueueSize": mscFrUniSigCurrentQueueSize,
       "mscFrUniSigLapfStatsTable": mscFrUniSigLapfStatsTable,
       "mscFrUniSigLapfStatsEntry": mscFrUniSigLapfStatsEntry,
       "mscFrUniSigStateChange": mscFrUniSigStateChange,
       "mscFrUniSigRemoteBusy": mscFrUniSigRemoteBusy,
       "mscFrUniSigReceiveRejectFrame": mscFrUniSigReceiveRejectFrame,
       "mscFrUniSigAckTimeout": mscFrUniSigAckTimeout,
       "mscFrUniSigIFramesTransmitted": mscFrUniSigIFramesTransmitted,
       "mscFrUniSigIFramesTxDiscarded": mscFrUniSigIFramesTxDiscarded,
       "mscFrUniSigIFramesReceived": mscFrUniSigIFramesReceived,
       "mscFrUniSigIFramesRcvdDiscarded": mscFrUniSigIFramesRcvdDiscarded,
       "mscFrUniSigSvcaccTable": mscFrUniSigSvcaccTable,
       "mscFrUniSigSvcaccEntry": mscFrUniSigSvcaccEntry,
       "mscFrUniSigDefaultAccounting": mscFrUniSigDefaultAccounting,
       "mscFrUniSigCodesTable": mscFrUniSigCodesTable,
       "mscFrUniSigCodesEntry": mscFrUniSigCodesEntry,
       "mscFrUniSigLastClearRemoteDataNetworkAddress": mscFrUniSigLastClearRemoteDataNetworkAddress,
       "mscFrUniSigLastClearCause": mscFrUniSigLastClearCause,
       "mscFrUniSigLastDiagnosticCode": mscFrUniSigLastDiagnosticCode,
       "mscFrUniSigBandwidthNotAvailableTable": mscFrUniSigBandwidthNotAvailableTable,
       "mscFrUniSigBandwidthNotAvailableEntry": mscFrUniSigBandwidthNotAvailableEntry,
       "mscFrUniSigBandwidthNotAvailableIndex": mscFrUniSigBandwidthNotAvailableIndex,
       "mscFrUniSigBandwidthNotAvailableValue": mscFrUniSigBandwidthNotAvailableValue,
       "mscFrUniVFramer": mscFrUniVFramer,
       "mscFrUniVFramerRowStatusTable": mscFrUniVFramerRowStatusTable,
       "mscFrUniVFramerRowStatusEntry": mscFrUniVFramerRowStatusEntry,
       "mscFrUniVFramerRowStatus": mscFrUniVFramerRowStatus,
       "mscFrUniVFramerComponentName": mscFrUniVFramerComponentName,
       "mscFrUniVFramerStorageType": mscFrUniVFramerStorageType,
       "mscFrUniVFramerIndex": mscFrUniVFramerIndex,
       "mscFrUniVFramerProvTable": mscFrUniVFramerProvTable,
       "mscFrUniVFramerProvEntry": mscFrUniVFramerProvEntry,
       "mscFrUniVFramerOtherVirtualFramer": mscFrUniVFramerOtherVirtualFramer,
       "mscFrUniVFramerLogicalProcessor": mscFrUniVFramerLogicalProcessor,
       "mscFrUniVFramerStateTable": mscFrUniVFramerStateTable,
       "mscFrUniVFramerStateEntry": mscFrUniVFramerStateEntry,
       "mscFrUniVFramerAdminState": mscFrUniVFramerAdminState,
       "mscFrUniVFramerOperationalState": mscFrUniVFramerOperationalState,
       "mscFrUniVFramerUsageState": mscFrUniVFramerUsageState,
       "mscFrUniVFramerStatsTable": mscFrUniVFramerStatsTable,
       "mscFrUniVFramerStatsEntry": mscFrUniVFramerStatsEntry,
       "mscFrUniVFramerFrmToOtherVFramer": mscFrUniVFramerFrmToOtherVFramer,
       "mscFrUniVFramerFrmFromOtherVFramer": mscFrUniVFramerFrmFromOtherVFramer,
       "mscFrUniVFramerOctetFromOtherVFramer": mscFrUniVFramerOctetFromOtherVFramer,
       "mscFrUniLts": mscFrUniLts,
       "mscFrUniLtsRowStatusTable": mscFrUniLtsRowStatusTable,
       "mscFrUniLtsRowStatusEntry": mscFrUniLtsRowStatusEntry,
       "mscFrUniLtsRowStatus": mscFrUniLtsRowStatus,
       "mscFrUniLtsComponentName": mscFrUniLtsComponentName,
       "mscFrUniLtsStorageType": mscFrUniLtsStorageType,
       "mscFrUniLtsIndex": mscFrUniLtsIndex,
       "mscFrUniLtsPat": mscFrUniLtsPat,
       "mscFrUniLtsPatRowStatusTable": mscFrUniLtsPatRowStatusTable,
       "mscFrUniLtsPatRowStatusEntry": mscFrUniLtsPatRowStatusEntry,
       "mscFrUniLtsPatRowStatus": mscFrUniLtsPatRowStatus,
       "mscFrUniLtsPatComponentName": mscFrUniLtsPatComponentName,
       "mscFrUniLtsPatStorageType": mscFrUniLtsPatStorageType,
       "mscFrUniLtsPatIndex": mscFrUniLtsPatIndex,
       "mscFrUniLtsPatDefaultsTable": mscFrUniLtsPatDefaultsTable,
       "mscFrUniLtsPatDefaultsEntry": mscFrUniLtsPatDefaultsEntry,
       "mscFrUniLtsPatDefaultDlci": mscFrUniLtsPatDefaultDlci,
       "mscFrUniLtsPatDefaultNumFrames": mscFrUniLtsPatDefaultNumFrames,
       "mscFrUniLtsPatDefaultDataSize": mscFrUniLtsPatDefaultDataSize,
       "mscFrUniLtsPatDefaultHeaderBits": mscFrUniLtsPatDefaultHeaderBits,
       "mscFrUniLtsPatDefaultHeaderLength": mscFrUniLtsPatDefaultHeaderLength,
       "mscFrUniLtsPatDefaultEABits": mscFrUniLtsPatDefaultEABits,
       "mscFrUniLtsPatDefaultPayloadPattern": mscFrUniLtsPatDefaultPayloadPattern,
       "mscFrUniLtsPatDefaultRfc1490Header": mscFrUniLtsPatDefaultRfc1490Header,
       "mscFrUniLtsPatDefaultUseBadLrc": mscFrUniLtsPatDefaultUseBadLrc,
       "mscFrUniLtsPatSetupTable": mscFrUniLtsPatSetupTable,
       "mscFrUniLtsPatSetupEntry": mscFrUniLtsPatSetupEntry,
       "mscFrUniLtsPatDlci": mscFrUniLtsPatDlci,
       "mscFrUniLtsPatNumFrames": mscFrUniLtsPatNumFrames,
       "mscFrUniLtsPatDataSize": mscFrUniLtsPatDataSize,
       "mscFrUniLtsPatHeaderBits": mscFrUniLtsPatHeaderBits,
       "mscFrUniLtsPatHeaderLength": mscFrUniLtsPatHeaderLength,
       "mscFrUniLtsPatEaBits": mscFrUniLtsPatEaBits,
       "mscFrUniLtsPatPayloadPattern": mscFrUniLtsPatPayloadPattern,
       "mscFrUniLtsPatRfc1490Header": mscFrUniLtsPatRfc1490Header,
       "mscFrUniLtsPatUseBadLrc": mscFrUniLtsPatUseBadLrc,
       "mscFrUniLtsPatOpDataTable": mscFrUniLtsPatOpDataTable,
       "mscFrUniLtsPatOpDataEntry": mscFrUniLtsPatOpDataEntry,
       "mscFrUniLtsPatFramePattern": mscFrUniLtsPatFramePattern,
       "mscFrUniLtsPatHdlcBitsInserted": mscFrUniLtsPatHdlcBitsInserted,
       "mscFrUniLtsPatOpStateTable": mscFrUniLtsPatOpStateTable,
       "mscFrUniLtsPatOpStateEntry": mscFrUniLtsPatOpStateEntry,
       "mscFrUniLtsPatLoad": mscFrUniLtsPatLoad,
       "mscFrUniLtsPatStatus": mscFrUniLtsPatStatus,
       "mscFrUniLtsSetupTable": mscFrUniLtsSetupTable,
       "mscFrUniLtsSetupEntry": mscFrUniLtsSetupEntry,
       "mscFrUniLtsDuration": mscFrUniLtsDuration,
       "mscFrUniLtsAlgorithm": mscFrUniLtsAlgorithm,
       "mscFrUniLtsBurstSize": mscFrUniLtsBurstSize,
       "mscFrUniLtsTimeInterval": mscFrUniLtsTimeInterval,
       "mscFrUniLtsStateTable": mscFrUniLtsStateTable,
       "mscFrUniLtsStateEntry": mscFrUniLtsStateEntry,
       "mscFrUniLtsGeneratorState": mscFrUniLtsGeneratorState,
       "mscFrUniLtsCycleIncomplete": mscFrUniLtsCycleIncomplete,
       "mscFrUniLtsLastActiveInterval": mscFrUniLtsLastActiveInterval,
       "mscFrUniLtsLoad": mscFrUniLtsLoad,
       "mscFrUniLtsElapsedGenerationTime": mscFrUniLtsElapsedGenerationTime,
       "mscFrUniLtsResultsTable": mscFrUniLtsResultsTable,
       "mscFrUniLtsResultsEntry": mscFrUniLtsResultsEntry,
       "mscFrUniLtsFramesTx": mscFrUniLtsFramesTx,
       "mscFrUniLtsBytesTx": mscFrUniLtsBytesTx,
       "mscFrUniLtsBitRateTx": mscFrUniLtsBitRateTx,
       "mscFrUniLtsFrameRateTx": mscFrUniLtsFrameRateTx,
       "mscFrUniCidDataTable": mscFrUniCidDataTable,
       "mscFrUniCidDataEntry": mscFrUniCidDataEntry,
       "mscFrUniCustomerIdentifier": mscFrUniCustomerIdentifier,
       "mscFrUniStateTable": mscFrUniStateTable,
       "mscFrUniStateEntry": mscFrUniStateEntry,
       "mscFrUniAdminState": mscFrUniAdminState,
       "mscFrUniOperationalState": mscFrUniOperationalState,
       "mscFrUniUsageState": mscFrUniUsageState,
       "mscFrUniAvailabilityStatus": mscFrUniAvailabilityStatus,
       "mscFrUniProceduralStatus": mscFrUniProceduralStatus,
       "mscFrUniControlStatus": mscFrUniControlStatus,
       "mscFrUniAlarmStatus": mscFrUniAlarmStatus,
       "mscFrUniStandbyStatus": mscFrUniStandbyStatus,
       "mscFrUniUnknownStatus": mscFrUniUnknownStatus,
       "mscFrUniStatsTable": mscFrUniStatsTable,
       "mscFrUniStatsEntry": mscFrUniStatsEntry,
       "mscFrUniLastUnknownDlci": mscFrUniLastUnknownDlci,
       "mscFrUniUnknownDlciFramesFromIf": mscFrUniUnknownDlciFramesFromIf,
       "mscFrUniInvalidHeaderFramesFromIf": mscFrUniInvalidHeaderFramesFromIf,
       "mscFrUniIfEntryTable": mscFrUniIfEntryTable,
       "mscFrUniIfEntryEntry": mscFrUniIfEntryEntry,
       "mscFrUniIfAdminStatus": mscFrUniIfAdminStatus,
       "mscFrUniIfIndex": mscFrUniIfIndex,
       "mscFrUniOperStatusTable": mscFrUniOperStatusTable,
       "mscFrUniOperStatusEntry": mscFrUniOperStatusEntry,
       "mscFrUniSnmpOperStatus": mscFrUniSnmpOperStatus,
       "mscFrUniEmissionPriorityQsTable": mscFrUniEmissionPriorityQsTable,
       "mscFrUniEmissionPriorityQsEntry": mscFrUniEmissionPriorityQsEntry,
       "mscFrUniNumberOfEmissionQs": mscFrUniNumberOfEmissionQs,
       "mscFrUniCa": mscFrUniCa,
       "mscFrUniCaRowStatusTable": mscFrUniCaRowStatusTable,
       "mscFrUniCaRowStatusEntry": mscFrUniCaRowStatusEntry,
       "mscFrUniCaRowStatus": mscFrUniCaRowStatus,
       "mscFrUniCaComponentName": mscFrUniCaComponentName,
       "mscFrUniCaStorageType": mscFrUniCaStorageType,
       "mscFrUniCaIndex": mscFrUniCaIndex,
       "mscFrUniCaTpm": mscFrUniCaTpm,
       "mscFrUniCaTpmRowStatusTable": mscFrUniCaTpmRowStatusTable,
       "mscFrUniCaTpmRowStatusEntry": mscFrUniCaTpmRowStatusEntry,
       "mscFrUniCaTpmRowStatus": mscFrUniCaTpmRowStatus,
       "mscFrUniCaTpmComponentName": mscFrUniCaTpmComponentName,
       "mscFrUniCaTpmStorageType": mscFrUniCaTpmStorageType,
       "mscFrUniCaTpmIndex": mscFrUniCaTpmIndex,
       "mscFrUniCaTpmProvTable": mscFrUniCaTpmProvTable,
       "mscFrUniCaTpmProvEntry": mscFrUniCaTpmProvEntry,
       "mscFrUniCaTpmAssignedIngressBandwidthPool": mscFrUniCaTpmAssignedIngressBandwidthPool,
       "mscFrUniCaTpmAssignedEgressBandwidthPool": mscFrUniCaTpmAssignedEgressBandwidthPool,
       "mscFrUniCaProvTable": mscFrUniCaProvTable,
       "mscFrUniCaProvEntry": mscFrUniCaProvEntry,
       "mscFrUniCaOverrideLinkRate": mscFrUniCaOverrideLinkRate,
       "mscFrUniCaMaximumBandwidthPerCall": mscFrUniCaMaximumBandwidthPerCall,
       "mscFrUniCaIngressCacTable": mscFrUniCaIngressCacTable,
       "mscFrUniCaIngressCacEntry": mscFrUniCaIngressCacEntry,
       "mscFrUniCaIngressApplyToCos": mscFrUniCaIngressApplyToCos,
       "mscFrUniCaIngressMaximumEirOnlyCalls": mscFrUniCaIngressMaximumEirOnlyCalls,
       "mscFrUniCaEgressCacTable": mscFrUniCaEgressCacTable,
       "mscFrUniCaEgressCacEntry": mscFrUniCaEgressCacEntry,
       "mscFrUniCaEgressApplyToCos": mscFrUniCaEgressApplyToCos,
       "mscFrUniCaEgressMaximumEirOnlyCalls": mscFrUniCaEgressMaximumEirOnlyCalls,
       "mscFrUniCaOpTable": mscFrUniCaOpTable,
       "mscFrUniCaOpEntry": mscFrUniCaOpEntry,
       "mscFrUniCaLinkRate": mscFrUniCaLinkRate,
       "mscFrUniCaNumberRejectedEgressCirPermConn": mscFrUniCaNumberRejectedEgressCirPermConn,
       "mscFrUniCaNumberRejectedEgressEirPermConn": mscFrUniCaNumberRejectedEgressEirPermConn,
       "mscFrUniCaIngCirBPTable": mscFrUniCaIngCirBPTable,
       "mscFrUniCaIngCirBPEntry": mscFrUniCaIngCirBPEntry,
       "mscFrUniCaIngCirBPIndex": mscFrUniCaIngCirBPIndex,
       "mscFrUniCaIngCirBPValue": mscFrUniCaIngCirBPValue,
       "mscFrUniCaEgCirBpTable": mscFrUniCaEgCirBpTable,
       "mscFrUniCaEgCirBpEntry": mscFrUniCaEgCirBpEntry,
       "mscFrUniCaEgCirBpIndex": mscFrUniCaEgCirBpIndex,
       "mscFrUniCaEgCirBpValue": mscFrUniCaEgCirBpValue,
       "mscFrUniCaIngCirPoolAdmitBwTable": mscFrUniCaIngCirPoolAdmitBwTable,
       "mscFrUniCaIngCirPoolAdmitBwEntry": mscFrUniCaIngCirPoolAdmitBwEntry,
       "mscFrUniCaIngCirPoolAdmitBwIndex": mscFrUniCaIngCirPoolAdmitBwIndex,
       "mscFrUniCaIngCirPoolAdmitBwValue": mscFrUniCaIngCirPoolAdmitBwValue,
       "mscFrUniCaIngCirPoolAvailBwTable": mscFrUniCaIngCirPoolAvailBwTable,
       "mscFrUniCaIngCirPoolAvailBwEntry": mscFrUniCaIngCirPoolAvailBwEntry,
       "mscFrUniCaIngCirPoolAvailBwIndex": mscFrUniCaIngCirPoolAvailBwIndex,
       "mscFrUniCaIngCirPoolAvailBwValue": mscFrUniCaIngCirPoolAvailBwValue,
       "mscFrUniCaEgCirPoolAdmitBwTable": mscFrUniCaEgCirPoolAdmitBwTable,
       "mscFrUniCaEgCirPoolAdmitBwEntry": mscFrUniCaEgCirPoolAdmitBwEntry,
       "mscFrUniCaEgCirPoolAdmitBwIndex": mscFrUniCaEgCirPoolAdmitBwIndex,
       "mscFrUniCaEgCirPoolAdmitBwValue": mscFrUniCaEgCirPoolAdmitBwValue,
       "mscFrUniCaEgCirPoolAvailBwTable": mscFrUniCaEgCirPoolAvailBwTable,
       "mscFrUniCaEgCirPoolAvailBwEntry": mscFrUniCaEgCirPoolAvailBwEntry,
       "mscFrUniCaEgCirPoolAvailBwIndex": mscFrUniCaEgCirPoolAvailBwIndex,
       "mscFrUniCaEgCirPoolAvailBwValue": mscFrUniCaEgCirPoolAvailBwValue,
       "mscFrUniCaIngEirBpTable": mscFrUniCaIngEirBpTable,
       "mscFrUniCaIngEirBpEntry": mscFrUniCaIngEirBpEntry,
       "mscFrUniCaIngEirBpIndex": mscFrUniCaIngEirBpIndex,
       "mscFrUniCaIngEirBpValue": mscFrUniCaIngEirBpValue,
       "mscFrUniCaEgEirBpTable": mscFrUniCaEgEirBpTable,
       "mscFrUniCaEgEirBpEntry": mscFrUniCaEgEirBpEntry,
       "mscFrUniCaEgEirBpIndex": mscFrUniCaEgEirBpIndex,
       "mscFrUniCaEgEirBpValue": mscFrUniCaEgEirBpValue,
       "mscFrUniCaIngEirPoolAdmitBwTable": mscFrUniCaIngEirPoolAdmitBwTable,
       "mscFrUniCaIngEirPoolAdmitBwEntry": mscFrUniCaIngEirPoolAdmitBwEntry,
       "mscFrUniCaIngEirPoolAdmitBwIndex": mscFrUniCaIngEirPoolAdmitBwIndex,
       "mscFrUniCaIngEirPoolAdmitBwValue": mscFrUniCaIngEirPoolAdmitBwValue,
       "mscFrUniCaIngEirPoolAvailBwTable": mscFrUniCaIngEirPoolAvailBwTable,
       "mscFrUniCaIngEirPoolAvailBwEntry": mscFrUniCaIngEirPoolAvailBwEntry,
       "mscFrUniCaIngEirPoolAvailBwIndex": mscFrUniCaIngEirPoolAvailBwIndex,
       "mscFrUniCaIngEirPoolAvailBwValue": mscFrUniCaIngEirPoolAvailBwValue,
       "mscFrUniCaEgEirPoolAdmitBwTable": mscFrUniCaEgEirPoolAdmitBwTable,
       "mscFrUniCaEgEirPoolAdmitBwEntry": mscFrUniCaEgEirPoolAdmitBwEntry,
       "mscFrUniCaEgEirPoolAdmitBwIndex": mscFrUniCaEgEirPoolAdmitBwIndex,
       "mscFrUniCaEgEirPoolAdmitBwValue": mscFrUniCaEgEirPoolAdmitBwValue,
       "mscFrUniCaEgEirPoolAvailBwTable": mscFrUniCaEgEirPoolAvailBwTable,
       "mscFrUniCaEgEirPoolAvailBwEntry": mscFrUniCaEgEirPoolAvailBwEntry,
       "mscFrUniCaEgEirPoolAvailBwIndex": mscFrUniCaEgEirPoolAvailBwIndex,
       "mscFrUniCaEgEirPoolAvailBwValue": mscFrUniCaEgEirPoolAvailBwValue,
       "mscFrUniFrmToIfByQueueTable": mscFrUniFrmToIfByQueueTable,
       "mscFrUniFrmToIfByQueueEntry": mscFrUniFrmToIfByQueueEntry,
       "mscFrUniFrmToIfByQueueIndex": mscFrUniFrmToIfByQueueIndex,
       "mscFrUniFrmToIfByQueueValue": mscFrUniFrmToIfByQueueValue,
       "mscFrUniOctetToIfByQueueTable": mscFrUniOctetToIfByQueueTable,
       "mscFrUniOctetToIfByQueueEntry": mscFrUniOctetToIfByQueueEntry,
       "mscFrUniOctetToIfByQueueIndex": mscFrUniOctetToIfByQueueIndex,
       "mscFrUniOctetToIfByQueueValue": mscFrUniOctetToIfByQueueValue,
       "frameRelayUniMIB": frameRelayUniMIB,
       "frameRelayUniGroup": frameRelayUniGroup,
       "frameRelayUniGroupCA": frameRelayUniGroupCA,
       "frameRelayUniGroupCA02": frameRelayUniGroupCA02,
       "frameRelayUniGroupCA02A": frameRelayUniGroupCA02A,
       "frameRelayUniCapabilities": frameRelayUniCapabilities,
       "frameRelayUniCapabilitiesCA": frameRelayUniCapabilitiesCA,
       "frameRelayUniCapabilitiesCA02": frameRelayUniCapabilitiesCA02,
       "frameRelayUniCapabilitiesCA02A": frameRelayUniCapabilitiesCA02A}
)
