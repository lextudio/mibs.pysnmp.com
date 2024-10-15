# SNMP MIB module (Nortel-MsCarrier-MscPassport-FrameRelayNniMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayNniMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:28 2024
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

_MscFrNni_ObjectIdentity = ObjectIdentity
mscFrNni = _MscFrNni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70)
)
_MscFrNniRowStatusTable_Object = MibTable
mscFrNniRowStatusTable = _MscFrNniRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 1)
)
if mibBuilder.loadTexts:
    mscFrNniRowStatusTable.setStatus("mandatory")
_MscFrNniRowStatusEntry_Object = MibTableRow
mscFrNniRowStatusEntry = _MscFrNniRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 1, 1)
)
mscFrNniRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniRowStatusEntry.setStatus("mandatory")
_MscFrNniRowStatus_Type = RowStatus
_MscFrNniRowStatus_Object = MibTableColumn
mscFrNniRowStatus = _MscFrNniRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 1, 1, 1),
    _MscFrNniRowStatus_Type()
)
mscFrNniRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniRowStatus.setStatus("mandatory")
_MscFrNniComponentName_Type = DisplayString
_MscFrNniComponentName_Object = MibTableColumn
mscFrNniComponentName = _MscFrNniComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 1, 1, 2),
    _MscFrNniComponentName_Type()
)
mscFrNniComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniComponentName.setStatus("mandatory")
_MscFrNniStorageType_Type = StorageType
_MscFrNniStorageType_Object = MibTableColumn
mscFrNniStorageType = _MscFrNniStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 1, 1, 4),
    _MscFrNniStorageType_Type()
)
mscFrNniStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniStorageType.setStatus("mandatory")


class _MscFrNniIndex_Type(Integer32):
    """Custom type mscFrNniIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrNniIndex_Type.__name__ = "Integer32"
_MscFrNniIndex_Object = MibTableColumn
mscFrNniIndex = _MscFrNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 1, 1, 10),
    _MscFrNniIndex_Type()
)
mscFrNniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniIndex.setStatus("mandatory")
_MscFrNniDna_ObjectIdentity = ObjectIdentity
mscFrNniDna = _MscFrNniDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2)
)
_MscFrNniDnaRowStatusTable_Object = MibTable
mscFrNniDnaRowStatusTable = _MscFrNniDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDnaRowStatusTable.setStatus("mandatory")
_MscFrNniDnaRowStatusEntry_Object = MibTableRow
mscFrNniDnaRowStatusEntry = _MscFrNniDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 1, 1)
)
mscFrNniDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaRowStatusEntry.setStatus("mandatory")
_MscFrNniDnaRowStatus_Type = RowStatus
_MscFrNniDnaRowStatus_Object = MibTableColumn
mscFrNniDnaRowStatus = _MscFrNniDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 1, 1, 1),
    _MscFrNniDnaRowStatus_Type()
)
mscFrNniDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaRowStatus.setStatus("mandatory")
_MscFrNniDnaComponentName_Type = DisplayString
_MscFrNniDnaComponentName_Object = MibTableColumn
mscFrNniDnaComponentName = _MscFrNniDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 1, 1, 2),
    _MscFrNniDnaComponentName_Type()
)
mscFrNniDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaComponentName.setStatus("mandatory")
_MscFrNniDnaStorageType_Type = StorageType
_MscFrNniDnaStorageType_Object = MibTableColumn
mscFrNniDnaStorageType = _MscFrNniDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 1, 1, 4),
    _MscFrNniDnaStorageType_Type()
)
mscFrNniDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaStorageType.setStatus("mandatory")
_MscFrNniDnaIndex_Type = NonReplicated
_MscFrNniDnaIndex_Object = MibTableColumn
mscFrNniDnaIndex = _MscFrNniDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 1, 1, 10),
    _MscFrNniDnaIndex_Type()
)
mscFrNniDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDnaIndex.setStatus("mandatory")
_MscFrNniDnaCug_ObjectIdentity = ObjectIdentity
mscFrNniDnaCug = _MscFrNniDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2)
)
_MscFrNniDnaCugRowStatusTable_Object = MibTable
mscFrNniDnaCugRowStatusTable = _MscFrNniDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDnaCugRowStatusTable.setStatus("obsolete")
_MscFrNniDnaCugRowStatusEntry_Object = MibTableRow
mscFrNniDnaCugRowStatusEntry = _MscFrNniDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 1, 1)
)
mscFrNniDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaCugRowStatusEntry.setStatus("obsolete")
_MscFrNniDnaCugRowStatus_Type = RowStatus
_MscFrNniDnaCugRowStatus_Object = MibTableColumn
mscFrNniDnaCugRowStatus = _MscFrNniDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 1, 1, 1),
    _MscFrNniDnaCugRowStatus_Type()
)
mscFrNniDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaCugRowStatus.setStatus("obsolete")
_MscFrNniDnaCugComponentName_Type = DisplayString
_MscFrNniDnaCugComponentName_Object = MibTableColumn
mscFrNniDnaCugComponentName = _MscFrNniDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 1, 1, 2),
    _MscFrNniDnaCugComponentName_Type()
)
mscFrNniDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaCugComponentName.setStatus("obsolete")
_MscFrNniDnaCugStorageType_Type = StorageType
_MscFrNniDnaCugStorageType_Object = MibTableColumn
mscFrNniDnaCugStorageType = _MscFrNniDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 1, 1, 4),
    _MscFrNniDnaCugStorageType_Type()
)
mscFrNniDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaCugStorageType.setStatus("obsolete")


class _MscFrNniDnaCugIndex_Type(Integer32):
    """Custom type mscFrNniDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniDnaCugIndex_Type.__name__ = "Integer32"
_MscFrNniDnaCugIndex_Object = MibTableColumn
mscFrNniDnaCugIndex = _MscFrNniDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 1, 1, 10),
    _MscFrNniDnaCugIndex_Type()
)
mscFrNniDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDnaCugIndex.setStatus("obsolete")
_MscFrNniDnaCugCugOptionsTable_Object = MibTable
mscFrNniDnaCugCugOptionsTable = _MscFrNniDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDnaCugCugOptionsTable.setStatus("obsolete")
_MscFrNniDnaCugCugOptionsEntry_Object = MibTableRow
mscFrNniDnaCugCugOptionsEntry = _MscFrNniDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10, 1)
)
mscFrNniDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaCugCugOptionsEntry.setStatus("obsolete")


class _MscFrNniDnaCugType_Type(Integer32):
    """Custom type mscFrNniDnaCugType based on Integer32"""
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


_MscFrNniDnaCugType_Type.__name__ = "Integer32"
_MscFrNniDnaCugType_Object = MibTableColumn
mscFrNniDnaCugType = _MscFrNniDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10, 1, 1),
    _MscFrNniDnaCugType_Type()
)
mscFrNniDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaCugType.setStatus("obsolete")


class _MscFrNniDnaCugDnic_Type(DigitString):
    """Custom type mscFrNniDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscFrNniDnaCugDnic_Type.__name__ = "DigitString"
_MscFrNniDnaCugDnic_Object = MibTableColumn
mscFrNniDnaCugDnic = _MscFrNniDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10, 1, 2),
    _MscFrNniDnaCugDnic_Type()
)
mscFrNniDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaCugDnic.setStatus("obsolete")


class _MscFrNniDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscFrNniDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFrNniDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscFrNniDnaCugInterlockCode_Object = MibTableColumn
mscFrNniDnaCugInterlockCode = _MscFrNniDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10, 1, 3),
    _MscFrNniDnaCugInterlockCode_Type()
)
mscFrNniDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaCugInterlockCode.setStatus("obsolete")


class _MscFrNniDnaCugPreferential_Type(Integer32):
    """Custom type mscFrNniDnaCugPreferential based on Integer32"""
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


_MscFrNniDnaCugPreferential_Type.__name__ = "Integer32"
_MscFrNniDnaCugPreferential_Object = MibTableColumn
mscFrNniDnaCugPreferential = _MscFrNniDnaCugPreferential_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10, 1, 4),
    _MscFrNniDnaCugPreferential_Type()
)
mscFrNniDnaCugPreferential.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaCugPreferential.setStatus("obsolete")


class _MscFrNniDnaCugOutCalls_Type(Integer32):
    """Custom type mscFrNniDnaCugOutCalls based on Integer32"""
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


_MscFrNniDnaCugOutCalls_Type.__name__ = "Integer32"
_MscFrNniDnaCugOutCalls_Object = MibTableColumn
mscFrNniDnaCugOutCalls = _MscFrNniDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10, 1, 5),
    _MscFrNniDnaCugOutCalls_Type()
)
mscFrNniDnaCugOutCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaCugOutCalls.setStatus("obsolete")


class _MscFrNniDnaCugIncCalls_Type(Integer32):
    """Custom type mscFrNniDnaCugIncCalls based on Integer32"""
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


_MscFrNniDnaCugIncCalls_Type.__name__ = "Integer32"
_MscFrNniDnaCugIncCalls_Object = MibTableColumn
mscFrNniDnaCugIncCalls = _MscFrNniDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 2, 10, 1, 6),
    _MscFrNniDnaCugIncCalls_Type()
)
mscFrNniDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaCugIncCalls.setStatus("obsolete")
_MscFrNniDnaHgM_ObjectIdentity = ObjectIdentity
mscFrNniDnaHgM = _MscFrNniDnaHgM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3)
)
_MscFrNniDnaHgMRowStatusTable_Object = MibTable
mscFrNniDnaHgMRowStatusTable = _MscFrNniDnaHgMRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMRowStatusTable.setStatus("mandatory")
_MscFrNniDnaHgMRowStatusEntry_Object = MibTableRow
mscFrNniDnaHgMRowStatusEntry = _MscFrNniDnaHgMRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 1, 1)
)
mscFrNniDnaHgMRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMRowStatusEntry.setStatus("mandatory")
_MscFrNniDnaHgMRowStatus_Type = RowStatus
_MscFrNniDnaHgMRowStatus_Object = MibTableColumn
mscFrNniDnaHgMRowStatus = _MscFrNniDnaHgMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 1, 1, 1),
    _MscFrNniDnaHgMRowStatus_Type()
)
mscFrNniDnaHgMRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMRowStatus.setStatus("mandatory")
_MscFrNniDnaHgMComponentName_Type = DisplayString
_MscFrNniDnaHgMComponentName_Object = MibTableColumn
mscFrNniDnaHgMComponentName = _MscFrNniDnaHgMComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 1, 1, 2),
    _MscFrNniDnaHgMComponentName_Type()
)
mscFrNniDnaHgMComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMComponentName.setStatus("mandatory")
_MscFrNniDnaHgMStorageType_Type = StorageType
_MscFrNniDnaHgMStorageType_Object = MibTableColumn
mscFrNniDnaHgMStorageType = _MscFrNniDnaHgMStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 1, 1, 4),
    _MscFrNniDnaHgMStorageType_Type()
)
mscFrNniDnaHgMStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMStorageType.setStatus("mandatory")
_MscFrNniDnaHgMIndex_Type = NonReplicated
_MscFrNniDnaHgMIndex_Object = MibTableColumn
mscFrNniDnaHgMIndex = _MscFrNniDnaHgMIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 1, 1, 10),
    _MscFrNniDnaHgMIndex_Type()
)
mscFrNniDnaHgMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMIndex.setStatus("mandatory")
_MscFrNniDnaHgMHgAddr_ObjectIdentity = ObjectIdentity
mscFrNniDnaHgMHgAddr = _MscFrNniDnaHgMHgAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2)
)
_MscFrNniDnaHgMHgAddrRowStatusTable_Object = MibTable
mscFrNniDnaHgMHgAddrRowStatusTable = _MscFrNniDnaHgMHgAddrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrRowStatusTable.setStatus("mandatory")
_MscFrNniDnaHgMHgAddrRowStatusEntry_Object = MibTableRow
mscFrNniDnaHgMHgAddrRowStatusEntry = _MscFrNniDnaHgMHgAddrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 1, 1)
)
mscFrNniDnaHgMHgAddrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrRowStatusEntry.setStatus("mandatory")
_MscFrNniDnaHgMHgAddrRowStatus_Type = RowStatus
_MscFrNniDnaHgMHgAddrRowStatus_Object = MibTableColumn
mscFrNniDnaHgMHgAddrRowStatus = _MscFrNniDnaHgMHgAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 1, 1, 1),
    _MscFrNniDnaHgMHgAddrRowStatus_Type()
)
mscFrNniDnaHgMHgAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrRowStatus.setStatus("mandatory")
_MscFrNniDnaHgMHgAddrComponentName_Type = DisplayString
_MscFrNniDnaHgMHgAddrComponentName_Object = MibTableColumn
mscFrNniDnaHgMHgAddrComponentName = _MscFrNniDnaHgMHgAddrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 1, 1, 2),
    _MscFrNniDnaHgMHgAddrComponentName_Type()
)
mscFrNniDnaHgMHgAddrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrComponentName.setStatus("mandatory")
_MscFrNniDnaHgMHgAddrStorageType_Type = StorageType
_MscFrNniDnaHgMHgAddrStorageType_Object = MibTableColumn
mscFrNniDnaHgMHgAddrStorageType = _MscFrNniDnaHgMHgAddrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 1, 1, 4),
    _MscFrNniDnaHgMHgAddrStorageType_Type()
)
mscFrNniDnaHgMHgAddrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrStorageType.setStatus("mandatory")


class _MscFrNniDnaHgMHgAddrIndex_Type(Integer32):
    """Custom type mscFrNniDnaHgMHgAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MscFrNniDnaHgMHgAddrIndex_Type.__name__ = "Integer32"
_MscFrNniDnaHgMHgAddrIndex_Object = MibTableColumn
mscFrNniDnaHgMHgAddrIndex = _MscFrNniDnaHgMHgAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 1, 1, 10),
    _MscFrNniDnaHgMHgAddrIndex_Type()
)
mscFrNniDnaHgMHgAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrIndex.setStatus("mandatory")
_MscFrNniDnaHgMHgAddrAddrTable_Object = MibTable
mscFrNniDnaHgMHgAddrAddrTable = _MscFrNniDnaHgMHgAddrAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrAddrTable.setStatus("mandatory")
_MscFrNniDnaHgMHgAddrAddrEntry_Object = MibTableRow
mscFrNniDnaHgMHgAddrAddrEntry = _MscFrNniDnaHgMHgAddrAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 10, 1)
)
mscFrNniDnaHgMHgAddrAddrEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaHgMIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaHgMHgAddrIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrAddrEntry.setStatus("mandatory")


class _MscFrNniDnaHgMHgAddrNumberingPlanIndicator_Type(Integer32):
    """Custom type mscFrNniDnaHgMHgAddrNumberingPlanIndicator based on Integer32"""
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


_MscFrNniDnaHgMHgAddrNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscFrNniDnaHgMHgAddrNumberingPlanIndicator_Object = MibTableColumn
mscFrNniDnaHgMHgAddrNumberingPlanIndicator = _MscFrNniDnaHgMHgAddrNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 10, 1, 1),
    _MscFrNniDnaHgMHgAddrNumberingPlanIndicator_Type()
)
mscFrNniDnaHgMHgAddrNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrNumberingPlanIndicator.setStatus("mandatory")


class _MscFrNniDnaHgMHgAddrDataNetworkAddress_Type(DigitString):
    """Custom type mscFrNniDnaHgMHgAddrDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrNniDnaHgMHgAddrDataNetworkAddress_Type.__name__ = "DigitString"
_MscFrNniDnaHgMHgAddrDataNetworkAddress_Object = MibTableColumn
mscFrNniDnaHgMHgAddrDataNetworkAddress = _MscFrNniDnaHgMHgAddrDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 2, 10, 1, 2),
    _MscFrNniDnaHgMHgAddrDataNetworkAddress_Type()
)
mscFrNniDnaHgMHgAddrDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMHgAddrDataNetworkAddress.setStatus("mandatory")
_MscFrNniDnaHgMIfTable_Object = MibTable
mscFrNniDnaHgMIfTable = _MscFrNniDnaHgMIfTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMIfTable.setStatus("mandatory")
_MscFrNniDnaHgMIfEntry_Object = MibTableRow
mscFrNniDnaHgMIfEntry = _MscFrNniDnaHgMIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 10, 1)
)
mscFrNniDnaHgMIfEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMIfEntry.setStatus("mandatory")


class _MscFrNniDnaHgMAvailabilityUpdateThreshold_Type(Unsigned32):
    """Custom type mscFrNniDnaHgMAvailabilityUpdateThreshold based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 16777216),
    )


_MscFrNniDnaHgMAvailabilityUpdateThreshold_Type.__name__ = "Unsigned32"
_MscFrNniDnaHgMAvailabilityUpdateThreshold_Object = MibTableColumn
mscFrNniDnaHgMAvailabilityUpdateThreshold = _MscFrNniDnaHgMAvailabilityUpdateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 10, 1, 1),
    _MscFrNniDnaHgMAvailabilityUpdateThreshold_Type()
)
mscFrNniDnaHgMAvailabilityUpdateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMAvailabilityUpdateThreshold.setStatus("mandatory")
_MscFrNniDnaHgMOpTable_Object = MibTable
mscFrNniDnaHgMOpTable = _MscFrNniDnaHgMOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMOpTable.setStatus("mandatory")
_MscFrNniDnaHgMOpEntry_Object = MibTableRow
mscFrNniDnaHgMOpEntry = _MscFrNniDnaHgMOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11, 1)
)
mscFrNniDnaHgMOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaHgMIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaHgMOpEntry.setStatus("mandatory")


class _MscFrNniDnaHgMMaximumAvailableAggregateCir_Type(Unsigned32):
    """Custom type mscFrNniDnaHgMMaximumAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDnaHgMMaximumAvailableAggregateCir_Type.__name__ = "Unsigned32"
_MscFrNniDnaHgMMaximumAvailableAggregateCir_Object = MibTableColumn
mscFrNniDnaHgMMaximumAvailableAggregateCir = _MscFrNniDnaHgMMaximumAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11, 1, 1),
    _MscFrNniDnaHgMMaximumAvailableAggregateCir_Type()
)
mscFrNniDnaHgMMaximumAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMMaximumAvailableAggregateCir.setStatus("obsolete")


class _MscFrNniDnaHgMAvailableAggregateCir_Type(Unsigned32):
    """Custom type mscFrNniDnaHgMAvailableAggregateCir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDnaHgMAvailableAggregateCir_Type.__name__ = "Unsigned32"
_MscFrNniDnaHgMAvailableAggregateCir_Object = MibTableColumn
mscFrNniDnaHgMAvailableAggregateCir = _MscFrNniDnaHgMAvailableAggregateCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11, 1, 2),
    _MscFrNniDnaHgMAvailableAggregateCir_Type()
)
mscFrNniDnaHgMAvailableAggregateCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMAvailableAggregateCir.setStatus("obsolete")


class _MscFrNniDnaHgMAvailabilityDelta_Type(Integer32):
    """Custom type mscFrNniDnaHgMAvailabilityDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16777216, 16777215),
    )


_MscFrNniDnaHgMAvailabilityDelta_Type.__name__ = "Integer32"
_MscFrNniDnaHgMAvailabilityDelta_Object = MibTableColumn
mscFrNniDnaHgMAvailabilityDelta = _MscFrNniDnaHgMAvailabilityDelta_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11, 1, 3),
    _MscFrNniDnaHgMAvailabilityDelta_Type()
)
mscFrNniDnaHgMAvailabilityDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMAvailabilityDelta.setStatus("mandatory")


class _MscFrNniDnaHgMAvailableDlcis_Type(Unsigned32):
    """Custom type mscFrNniDnaHgMAvailableDlcis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscFrNniDnaHgMAvailableDlcis_Type.__name__ = "Unsigned32"
_MscFrNniDnaHgMAvailableDlcis_Object = MibTableColumn
mscFrNniDnaHgMAvailableDlcis = _MscFrNniDnaHgMAvailableDlcis_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11, 1, 5),
    _MscFrNniDnaHgMAvailableDlcis_Type()
)
mscFrNniDnaHgMAvailableDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMAvailableDlcis.setStatus("mandatory")


class _MscFrNniDnaHgMMaximumAvailableAggregateCir64_Type(Unsigned64):
    """Custom type mscFrNniDnaHgMMaximumAvailableAggregateCir64 based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrNniDnaHgMMaximumAvailableAggregateCir64_Type.__name__ = "Unsigned64"
_MscFrNniDnaHgMMaximumAvailableAggregateCir64_Object = MibTableColumn
mscFrNniDnaHgMMaximumAvailableAggregateCir64 = _MscFrNniDnaHgMMaximumAvailableAggregateCir64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11, 1, 6),
    _MscFrNniDnaHgMMaximumAvailableAggregateCir64_Type()
)
mscFrNniDnaHgMMaximumAvailableAggregateCir64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMMaximumAvailableAggregateCir64.setStatus("mandatory")


class _MscFrNniDnaHgMAvailableAggregateCir64_Type(Unsigned64):
    """Custom type mscFrNniDnaHgMAvailableAggregateCir64 based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrNniDnaHgMAvailableAggregateCir64_Type.__name__ = "Unsigned64"
_MscFrNniDnaHgMAvailableAggregateCir64_Object = MibTableColumn
mscFrNniDnaHgMAvailableAggregateCir64 = _MscFrNniDnaHgMAvailableAggregateCir64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 3, 11, 1, 7),
    _MscFrNniDnaHgMAvailableAggregateCir64_Type()
)
mscFrNniDnaHgMAvailableAggregateCir64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDnaHgMAvailableAggregateCir64.setStatus("mandatory")
_MscFrNniDnaAddressTable_Object = MibTable
mscFrNniDnaAddressTable = _MscFrNniDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDnaAddressTable.setStatus("mandatory")
_MscFrNniDnaAddressEntry_Object = MibTableRow
mscFrNniDnaAddressEntry = _MscFrNniDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 10, 1)
)
mscFrNniDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaAddressEntry.setStatus("mandatory")


class _MscFrNniDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscFrNniDnaNumberingPlanIndicator based on Integer32"""
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


_MscFrNniDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscFrNniDnaNumberingPlanIndicator_Object = MibTableColumn
mscFrNniDnaNumberingPlanIndicator = _MscFrNniDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 10, 1, 1),
    _MscFrNniDnaNumberingPlanIndicator_Type()
)
mscFrNniDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscFrNniDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscFrNniDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrNniDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscFrNniDnaDataNetworkAddress_Object = MibTableColumn
mscFrNniDnaDataNetworkAddress = _MscFrNniDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 10, 1, 2),
    _MscFrNniDnaDataNetworkAddress_Type()
)
mscFrNniDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaDataNetworkAddress.setStatus("mandatory")
_MscFrNniDnaOutgoingOptionsTable_Object = MibTable
mscFrNniDnaOutgoingOptionsTable = _MscFrNniDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrNniDnaOutgoingOptionsTable.setStatus("mandatory")
_MscFrNniDnaOutgoingOptionsEntry_Object = MibTableRow
mscFrNniDnaOutgoingOptionsEntry = _MscFrNniDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1)
)
mscFrNniDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscFrNniDnaOutDefaultPriority_Type(Integer32):
    """Custom type mscFrNniDnaOutDefaultPriority based on Integer32"""
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


_MscFrNniDnaOutDefaultPriority_Type.__name__ = "Integer32"
_MscFrNniDnaOutDefaultPriority_Object = MibTableColumn
mscFrNniDnaOutDefaultPriority = _MscFrNniDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1, 7),
    _MscFrNniDnaOutDefaultPriority_Type()
)
mscFrNniDnaOutDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaOutDefaultPriority.setStatus("mandatory")


class _MscFrNniDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type mscFrNniDnaOutDefaultPathSensitivity based on Integer32"""
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


_MscFrNniDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_MscFrNniDnaOutDefaultPathSensitivity_Object = MibTableColumn
mscFrNniDnaOutDefaultPathSensitivity = _MscFrNniDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1, 11),
    _MscFrNniDnaOutDefaultPathSensitivity_Type()
)
mscFrNniDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _MscFrNniDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type mscFrNniDnaOutPathSensitivityOverRide based on Integer32"""
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


_MscFrNniDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_MscFrNniDnaOutPathSensitivityOverRide_Object = MibTableColumn
mscFrNniDnaOutPathSensitivityOverRide = _MscFrNniDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1, 12),
    _MscFrNniDnaOutPathSensitivityOverRide_Type()
)
mscFrNniDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _MscFrNniDnaOutDefaultPathReliability_Type(Integer32):
    """Custom type mscFrNniDnaOutDefaultPathReliability based on Integer32"""
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


_MscFrNniDnaOutDefaultPathReliability_Type.__name__ = "Integer32"
_MscFrNniDnaOutDefaultPathReliability_Object = MibTableColumn
mscFrNniDnaOutDefaultPathReliability = _MscFrNniDnaOutDefaultPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1, 14),
    _MscFrNniDnaOutDefaultPathReliability_Type()
)
mscFrNniDnaOutDefaultPathReliability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaOutDefaultPathReliability.setStatus("mandatory")


class _MscFrNniDnaOutAccess_Type(Integer32):
    """Custom type mscFrNniDnaOutAccess based on Integer32"""
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


_MscFrNniDnaOutAccess_Type.__name__ = "Integer32"
_MscFrNniDnaOutAccess_Object = MibTableColumn
mscFrNniDnaOutAccess = _MscFrNniDnaOutAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1, 17),
    _MscFrNniDnaOutAccess_Type()
)
mscFrNniDnaOutAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaOutAccess.setStatus("obsolete")


class _MscFrNniDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mscFrNniDnaDefaultTransferPriority based on Integer32"""
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


_MscFrNniDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MscFrNniDnaDefaultTransferPriority_Object = MibTableColumn
mscFrNniDnaDefaultTransferPriority = _MscFrNniDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1, 18),
    _MscFrNniDnaDefaultTransferPriority_Type()
)
mscFrNniDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaDefaultTransferPriority.setStatus("mandatory")


class _MscFrNniDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type mscFrNniDnaTransferPriorityOverRide based on Integer32"""
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


_MscFrNniDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_MscFrNniDnaTransferPriorityOverRide_Object = MibTableColumn
mscFrNniDnaTransferPriorityOverRide = _MscFrNniDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 11, 1, 19),
    _MscFrNniDnaTransferPriorityOverRide_Type()
)
mscFrNniDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaTransferPriorityOverRide.setStatus("mandatory")
_MscFrNniDnaIncomingOptionsTable_Object = MibTable
mscFrNniDnaIncomingOptionsTable = _MscFrNniDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrNniDnaIncomingOptionsTable.setStatus("mandatory")
_MscFrNniDnaIncomingOptionsEntry_Object = MibTableRow
mscFrNniDnaIncomingOptionsEntry = _MscFrNniDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 12, 1)
)
mscFrNniDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscFrNniDnaIncAccess_Type(Integer32):
    """Custom type mscFrNniDnaIncAccess based on Integer32"""
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


_MscFrNniDnaIncAccess_Type.__name__ = "Integer32"
_MscFrNniDnaIncAccess_Object = MibTableColumn
mscFrNniDnaIncAccess = _MscFrNniDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 12, 1, 9),
    _MscFrNniDnaIncAccess_Type()
)
mscFrNniDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaIncAccess.setStatus("obsolete")
_MscFrNniDnaCallOptionsTable_Object = MibTable
mscFrNniDnaCallOptionsTable = _MscFrNniDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrNniDnaCallOptionsTable.setStatus("mandatory")
_MscFrNniDnaCallOptionsEntry_Object = MibTableRow
mscFrNniDnaCallOptionsEntry = _MscFrNniDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 13, 1)
)
mscFrNniDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDnaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDnaCallOptionsEntry.setStatus("mandatory")


class _MscFrNniDnaAccountClass_Type(Unsigned32):
    """Custom type mscFrNniDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniDnaAccountClass_Type.__name__ = "Unsigned32"
_MscFrNniDnaAccountClass_Object = MibTableColumn
mscFrNniDnaAccountClass = _MscFrNniDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 13, 1, 10),
    _MscFrNniDnaAccountClass_Type()
)
mscFrNniDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaAccountClass.setStatus("mandatory")


class _MscFrNniDnaAccountCollection_Type(OctetString):
    """Custom type mscFrNniDnaAccountCollection based on OctetString"""
    defaultHexValue = "80"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniDnaAccountCollection_Type.__name__ = "OctetString"
_MscFrNniDnaAccountCollection_Object = MibTableColumn
mscFrNniDnaAccountCollection = _MscFrNniDnaAccountCollection_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 13, 1, 11),
    _MscFrNniDnaAccountCollection_Type()
)
mscFrNniDnaAccountCollection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaAccountCollection.setStatus("mandatory")


class _MscFrNniDnaServiceExchange_Type(Unsigned32):
    """Custom type mscFrNniDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniDnaServiceExchange_Type.__name__ = "Unsigned32"
_MscFrNniDnaServiceExchange_Object = MibTableColumn
mscFrNniDnaServiceExchange = _MscFrNniDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 13, 1, 12),
    _MscFrNniDnaServiceExchange_Type()
)
mscFrNniDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaServiceExchange.setStatus("mandatory")


class _MscFrNniDnaEgressAccounting_Type(Integer32):
    """Custom type mscFrNniDnaEgressAccounting based on Integer32"""
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


_MscFrNniDnaEgressAccounting_Type.__name__ = "Integer32"
_MscFrNniDnaEgressAccounting_Object = MibTableColumn
mscFrNniDnaEgressAccounting = _MscFrNniDnaEgressAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 13, 1, 13),
    _MscFrNniDnaEgressAccounting_Type()
)
mscFrNniDnaEgressAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaEgressAccounting.setStatus("mandatory")


class _MscFrNniDnaDataPath_Type(Integer32):
    """Custom type mscFrNniDnaDataPath based on Integer32"""
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


_MscFrNniDnaDataPath_Type.__name__ = "Integer32"
_MscFrNniDnaDataPath_Object = MibTableColumn
mscFrNniDnaDataPath = _MscFrNniDnaDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 2, 13, 1, 21),
    _MscFrNniDnaDataPath_Type()
)
mscFrNniDnaDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDnaDataPath.setStatus("mandatory")
_MscFrNniFramer_ObjectIdentity = ObjectIdentity
mscFrNniFramer = _MscFrNniFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3)
)
_MscFrNniFramerRowStatusTable_Object = MibTable
mscFrNniFramerRowStatusTable = _MscFrNniFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrNniFramerRowStatusTable.setStatus("mandatory")
_MscFrNniFramerRowStatusEntry_Object = MibTableRow
mscFrNniFramerRowStatusEntry = _MscFrNniFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 1, 1)
)
mscFrNniFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniFramerRowStatusEntry.setStatus("mandatory")
_MscFrNniFramerRowStatus_Type = RowStatus
_MscFrNniFramerRowStatus_Object = MibTableColumn
mscFrNniFramerRowStatus = _MscFrNniFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 1, 1, 1),
    _MscFrNniFramerRowStatus_Type()
)
mscFrNniFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniFramerRowStatus.setStatus("mandatory")
_MscFrNniFramerComponentName_Type = DisplayString
_MscFrNniFramerComponentName_Object = MibTableColumn
mscFrNniFramerComponentName = _MscFrNniFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 1, 1, 2),
    _MscFrNniFramerComponentName_Type()
)
mscFrNniFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerComponentName.setStatus("mandatory")
_MscFrNniFramerStorageType_Type = StorageType
_MscFrNniFramerStorageType_Object = MibTableColumn
mscFrNniFramerStorageType = _MscFrNniFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 1, 1, 4),
    _MscFrNniFramerStorageType_Type()
)
mscFrNniFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerStorageType.setStatus("mandatory")
_MscFrNniFramerIndex_Type = NonReplicated
_MscFrNniFramerIndex_Object = MibTableColumn
mscFrNniFramerIndex = _MscFrNniFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 1, 1, 10),
    _MscFrNniFramerIndex_Type()
)
mscFrNniFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniFramerIndex.setStatus("mandatory")
_MscFrNniFramerProvTable_Object = MibTable
mscFrNniFramerProvTable = _MscFrNniFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrNniFramerProvTable.setStatus("mandatory")
_MscFrNniFramerProvEntry_Object = MibTableRow
mscFrNniFramerProvEntry = _MscFrNniFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 10, 1)
)
mscFrNniFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniFramerProvEntry.setStatus("mandatory")
_MscFrNniFramerInterfaceName_Type = Link
_MscFrNniFramerInterfaceName_Object = MibTableColumn
mscFrNniFramerInterfaceName = _MscFrNniFramerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 10, 1, 1),
    _MscFrNniFramerInterfaceName_Type()
)
mscFrNniFramerInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniFramerInterfaceName.setStatus("mandatory")
_MscFrNniFramerLinkTable_Object = MibTable
mscFrNniFramerLinkTable = _MscFrNniFramerLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrNniFramerLinkTable.setStatus("mandatory")
_MscFrNniFramerLinkEntry_Object = MibTableRow
mscFrNniFramerLinkEntry = _MscFrNniFramerLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 11, 1)
)
mscFrNniFramerLinkEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniFramerLinkEntry.setStatus("mandatory")


class _MscFrNniFramerDataInversion_Type(Integer32):
    """Custom type mscFrNniFramerDataInversion based on Integer32"""
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


_MscFrNniFramerDataInversion_Type.__name__ = "Integer32"
_MscFrNniFramerDataInversion_Object = MibTableColumn
mscFrNniFramerDataInversion = _MscFrNniFramerDataInversion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 11, 1, 2),
    _MscFrNniFramerDataInversion_Type()
)
mscFrNniFramerDataInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniFramerDataInversion.setStatus("mandatory")


class _MscFrNniFramerFrameCrcType_Type(Integer32):
    """Custom type mscFrNniFramerFrameCrcType based on Integer32"""
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


_MscFrNniFramerFrameCrcType_Type.__name__ = "Integer32"
_MscFrNniFramerFrameCrcType_Object = MibTableColumn
mscFrNniFramerFrameCrcType = _MscFrNniFramerFrameCrcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 11, 1, 3),
    _MscFrNniFramerFrameCrcType_Type()
)
mscFrNniFramerFrameCrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniFramerFrameCrcType.setStatus("mandatory")


class _MscFrNniFramerFlagsBetweenFrames_Type(Unsigned32):
    """Custom type mscFrNniFramerFlagsBetweenFrames based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscFrNniFramerFlagsBetweenFrames_Type.__name__ = "Unsigned32"
_MscFrNniFramerFlagsBetweenFrames_Object = MibTableColumn
mscFrNniFramerFlagsBetweenFrames = _MscFrNniFramerFlagsBetweenFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 11, 1, 4),
    _MscFrNniFramerFlagsBetweenFrames_Type()
)
mscFrNniFramerFlagsBetweenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniFramerFlagsBetweenFrames.setStatus("mandatory")
_MscFrNniFramerStateTable_Object = MibTable
mscFrNniFramerStateTable = _MscFrNniFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 12)
)
if mibBuilder.loadTexts:
    mscFrNniFramerStateTable.setStatus("mandatory")
_MscFrNniFramerStateEntry_Object = MibTableRow
mscFrNniFramerStateEntry = _MscFrNniFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 12, 1)
)
mscFrNniFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniFramerStateEntry.setStatus("mandatory")


class _MscFrNniFramerAdminState_Type(Integer32):
    """Custom type mscFrNniFramerAdminState based on Integer32"""
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


_MscFrNniFramerAdminState_Type.__name__ = "Integer32"
_MscFrNniFramerAdminState_Object = MibTableColumn
mscFrNniFramerAdminState = _MscFrNniFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 12, 1, 1),
    _MscFrNniFramerAdminState_Type()
)
mscFrNniFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerAdminState.setStatus("mandatory")


class _MscFrNniFramerOperationalState_Type(Integer32):
    """Custom type mscFrNniFramerOperationalState based on Integer32"""
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


_MscFrNniFramerOperationalState_Type.__name__ = "Integer32"
_MscFrNniFramerOperationalState_Object = MibTableColumn
mscFrNniFramerOperationalState = _MscFrNniFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 12, 1, 2),
    _MscFrNniFramerOperationalState_Type()
)
mscFrNniFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerOperationalState.setStatus("mandatory")


class _MscFrNniFramerUsageState_Type(Integer32):
    """Custom type mscFrNniFramerUsageState based on Integer32"""
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


_MscFrNniFramerUsageState_Type.__name__ = "Integer32"
_MscFrNniFramerUsageState_Object = MibTableColumn
mscFrNniFramerUsageState = _MscFrNniFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 12, 1, 3),
    _MscFrNniFramerUsageState_Type()
)
mscFrNniFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerUsageState.setStatus("mandatory")
_MscFrNniFramerStatsTable_Object = MibTable
mscFrNniFramerStatsTable = _MscFrNniFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13)
)
if mibBuilder.loadTexts:
    mscFrNniFramerStatsTable.setStatus("mandatory")
_MscFrNniFramerStatsEntry_Object = MibTableRow
mscFrNniFramerStatsEntry = _MscFrNniFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1)
)
mscFrNniFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniFramerStatsEntry.setStatus("mandatory")
_MscFrNniFramerFrmToIf_Type = Counter32
_MscFrNniFramerFrmToIf_Object = MibTableColumn
mscFrNniFramerFrmToIf = _MscFrNniFramerFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 1),
    _MscFrNniFramerFrmToIf_Type()
)
mscFrNniFramerFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerFrmToIf.setStatus("obsolete")
_MscFrNniFramerFrmFromIf_Type = Counter32
_MscFrNniFramerFrmFromIf_Object = MibTableColumn
mscFrNniFramerFrmFromIf = _MscFrNniFramerFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 2),
    _MscFrNniFramerFrmFromIf_Type()
)
mscFrNniFramerFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerFrmFromIf.setStatus("obsolete")
_MscFrNniFramerOctetFromIf_Type = Counter32
_MscFrNniFramerOctetFromIf_Object = MibTableColumn
mscFrNniFramerOctetFromIf = _MscFrNniFramerOctetFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 3),
    _MscFrNniFramerOctetFromIf_Type()
)
mscFrNniFramerOctetFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerOctetFromIf.setStatus("obsolete")
_MscFrNniFramerAborts_Type = Counter32
_MscFrNniFramerAborts_Object = MibTableColumn
mscFrNniFramerAborts = _MscFrNniFramerAborts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 4),
    _MscFrNniFramerAborts_Type()
)
mscFrNniFramerAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerAborts.setStatus("mandatory")
_MscFrNniFramerCrcErrors_Type = Counter32
_MscFrNniFramerCrcErrors_Object = MibTableColumn
mscFrNniFramerCrcErrors = _MscFrNniFramerCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 5),
    _MscFrNniFramerCrcErrors_Type()
)
mscFrNniFramerCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerCrcErrors.setStatus("mandatory")
_MscFrNniFramerLrcErrors_Type = Counter32
_MscFrNniFramerLrcErrors_Object = MibTableColumn
mscFrNniFramerLrcErrors = _MscFrNniFramerLrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 6),
    _MscFrNniFramerLrcErrors_Type()
)
mscFrNniFramerLrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerLrcErrors.setStatus("mandatory")
_MscFrNniFramerNonOctetErrors_Type = Counter32
_MscFrNniFramerNonOctetErrors_Object = MibTableColumn
mscFrNniFramerNonOctetErrors = _MscFrNniFramerNonOctetErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 7),
    _MscFrNniFramerNonOctetErrors_Type()
)
mscFrNniFramerNonOctetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerNonOctetErrors.setStatus("mandatory")
_MscFrNniFramerOverruns_Type = Counter32
_MscFrNniFramerOverruns_Object = MibTableColumn
mscFrNniFramerOverruns = _MscFrNniFramerOverruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 8),
    _MscFrNniFramerOverruns_Type()
)
mscFrNniFramerOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerOverruns.setStatus("mandatory")
_MscFrNniFramerUnderruns_Type = Counter32
_MscFrNniFramerUnderruns_Object = MibTableColumn
mscFrNniFramerUnderruns = _MscFrNniFramerUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 9),
    _MscFrNniFramerUnderruns_Type()
)
mscFrNniFramerUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerUnderruns.setStatus("mandatory")
_MscFrNniFramerLargeFrmErrors_Type = Counter32
_MscFrNniFramerLargeFrmErrors_Object = MibTableColumn
mscFrNniFramerLargeFrmErrors = _MscFrNniFramerLargeFrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 10),
    _MscFrNniFramerLargeFrmErrors_Type()
)
mscFrNniFramerLargeFrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerLargeFrmErrors.setStatus("mandatory")
_MscFrNniFramerFrmModeErrors_Type = Counter32
_MscFrNniFramerFrmModeErrors_Object = MibTableColumn
mscFrNniFramerFrmModeErrors = _MscFrNniFramerFrmModeErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 11),
    _MscFrNniFramerFrmModeErrors_Type()
)
mscFrNniFramerFrmModeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerFrmModeErrors.setStatus("mandatory")
_MscFrNniFramerFrmToIf64_Type = PassportCounter64
_MscFrNniFramerFrmToIf64_Object = MibTableColumn
mscFrNniFramerFrmToIf64 = _MscFrNniFramerFrmToIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 14),
    _MscFrNniFramerFrmToIf64_Type()
)
mscFrNniFramerFrmToIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerFrmToIf64.setStatus("mandatory")
_MscFrNniFramerFrmFromIf64_Type = PassportCounter64
_MscFrNniFramerFrmFromIf64_Object = MibTableColumn
mscFrNniFramerFrmFromIf64 = _MscFrNniFramerFrmFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 15),
    _MscFrNniFramerFrmFromIf64_Type()
)
mscFrNniFramerFrmFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerFrmFromIf64.setStatus("mandatory")
_MscFrNniFramerOctetFromIf64_Type = PassportCounter64
_MscFrNniFramerOctetFromIf64_Object = MibTableColumn
mscFrNniFramerOctetFromIf64 = _MscFrNniFramerOctetFromIf64_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 13, 1, 16),
    _MscFrNniFramerOctetFromIf64_Type()
)
mscFrNniFramerOctetFromIf64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerOctetFromIf64.setStatus("mandatory")
_MscFrNniFramerUtilTable_Object = MibTable
mscFrNniFramerUtilTable = _MscFrNniFramerUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 14)
)
if mibBuilder.loadTexts:
    mscFrNniFramerUtilTable.setStatus("mandatory")
_MscFrNniFramerUtilEntry_Object = MibTableRow
mscFrNniFramerUtilEntry = _MscFrNniFramerUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 14, 1)
)
mscFrNniFramerUtilEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniFramerUtilEntry.setStatus("mandatory")


class _MscFrNniFramerNormPrioLinkUtilToIf_Type(Gauge32):
    """Custom type mscFrNniFramerNormPrioLinkUtilToIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrNniFramerNormPrioLinkUtilToIf_Type.__name__ = "Gauge32"
_MscFrNniFramerNormPrioLinkUtilToIf_Object = MibTableColumn
mscFrNniFramerNormPrioLinkUtilToIf = _MscFrNniFramerNormPrioLinkUtilToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 14, 1, 1),
    _MscFrNniFramerNormPrioLinkUtilToIf_Type()
)
mscFrNniFramerNormPrioLinkUtilToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerNormPrioLinkUtilToIf.setStatus("mandatory")


class _MscFrNniFramerNormPrioLinkUtilFromIf_Type(Gauge32):
    """Custom type mscFrNniFramerNormPrioLinkUtilFromIf based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFrNniFramerNormPrioLinkUtilFromIf_Type.__name__ = "Gauge32"
_MscFrNniFramerNormPrioLinkUtilFromIf_Object = MibTableColumn
mscFrNniFramerNormPrioLinkUtilFromIf = _MscFrNniFramerNormPrioLinkUtilFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 3, 14, 1, 3),
    _MscFrNniFramerNormPrioLinkUtilFromIf_Type()
)
mscFrNniFramerNormPrioLinkUtilFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFramerNormPrioLinkUtilFromIf.setStatus("mandatory")
_MscFrNniLmi_ObjectIdentity = ObjectIdentity
mscFrNniLmi = _MscFrNniLmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4)
)
_MscFrNniLmiRowStatusTable_Object = MibTable
mscFrNniLmiRowStatusTable = _MscFrNniLmiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrNniLmiRowStatusTable.setStatus("mandatory")
_MscFrNniLmiRowStatusEntry_Object = MibTableRow
mscFrNniLmiRowStatusEntry = _MscFrNniLmiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 1, 1)
)
mscFrNniLmiRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLmiRowStatusEntry.setStatus("mandatory")
_MscFrNniLmiRowStatus_Type = RowStatus
_MscFrNniLmiRowStatus_Object = MibTableColumn
mscFrNniLmiRowStatus = _MscFrNniLmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 1, 1, 1),
    _MscFrNniLmiRowStatus_Type()
)
mscFrNniLmiRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiRowStatus.setStatus("mandatory")
_MscFrNniLmiComponentName_Type = DisplayString
_MscFrNniLmiComponentName_Object = MibTableColumn
mscFrNniLmiComponentName = _MscFrNniLmiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 1, 1, 2),
    _MscFrNniLmiComponentName_Type()
)
mscFrNniLmiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiComponentName.setStatus("mandatory")
_MscFrNniLmiStorageType_Type = StorageType
_MscFrNniLmiStorageType_Object = MibTableColumn
mscFrNniLmiStorageType = _MscFrNniLmiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 1, 1, 4),
    _MscFrNniLmiStorageType_Type()
)
mscFrNniLmiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiStorageType.setStatus("mandatory")
_MscFrNniLmiIndex_Type = NonReplicated
_MscFrNniLmiIndex_Object = MibTableColumn
mscFrNniLmiIndex = _MscFrNniLmiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 1, 1, 10),
    _MscFrNniLmiIndex_Type()
)
mscFrNniLmiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniLmiIndex.setStatus("mandatory")
_MscFrNniLmiParmsTable_Object = MibTable
mscFrNniLmiParmsTable = _MscFrNniLmiParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10)
)
if mibBuilder.loadTexts:
    mscFrNniLmiParmsTable.setStatus("mandatory")
_MscFrNniLmiParmsEntry_Object = MibTableRow
mscFrNniLmiParmsEntry = _MscFrNniLmiParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10, 1)
)
mscFrNniLmiParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLmiParmsEntry.setStatus("mandatory")


class _MscFrNniLmiProcedures_Type(Integer32):
    """Custom type mscFrNniLmiProcedures based on Integer32"""
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


_MscFrNniLmiProcedures_Type.__name__ = "Integer32"
_MscFrNniLmiProcedures_Object = MibTableColumn
mscFrNniLmiProcedures = _MscFrNniLmiProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10, 1, 1),
    _MscFrNniLmiProcedures_Type()
)
mscFrNniLmiProcedures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiProcedures.setStatus("mandatory")


class _MscFrNniLmiAsyncStatusReport_Type(Integer32):
    """Custom type mscFrNniLmiAsyncStatusReport based on Integer32"""
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


_MscFrNniLmiAsyncStatusReport_Type.__name__ = "Integer32"
_MscFrNniLmiAsyncStatusReport_Object = MibTableColumn
mscFrNniLmiAsyncStatusReport = _MscFrNniLmiAsyncStatusReport_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10, 1, 2),
    _MscFrNniLmiAsyncStatusReport_Type()
)
mscFrNniLmiAsyncStatusReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiAsyncStatusReport.setStatus("mandatory")


class _MscFrNniLmiErrorEventThreshold_Type(Unsigned32):
    """Custom type mscFrNniLmiErrorEventThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrNniLmiErrorEventThreshold_Type.__name__ = "Unsigned32"
_MscFrNniLmiErrorEventThreshold_Object = MibTableColumn
mscFrNniLmiErrorEventThreshold = _MscFrNniLmiErrorEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10, 1, 3),
    _MscFrNniLmiErrorEventThreshold_Type()
)
mscFrNniLmiErrorEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiErrorEventThreshold.setStatus("mandatory")


class _MscFrNniLmiEventCount_Type(Unsigned32):
    """Custom type mscFrNniLmiEventCount based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MscFrNniLmiEventCount_Type.__name__ = "Unsigned32"
_MscFrNniLmiEventCount_Object = MibTableColumn
mscFrNniLmiEventCount = _MscFrNniLmiEventCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10, 1, 4),
    _MscFrNniLmiEventCount_Type()
)
mscFrNniLmiEventCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiEventCount.setStatus("mandatory")


class _MscFrNniLmiCheckPointTimer_Type(Unsigned32):
    """Custom type mscFrNniLmiCheckPointTimer based on Unsigned32"""
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


_MscFrNniLmiCheckPointTimer_Type.__name__ = "Unsigned32"
_MscFrNniLmiCheckPointTimer_Object = MibTableColumn
mscFrNniLmiCheckPointTimer = _MscFrNniLmiCheckPointTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10, 1, 5),
    _MscFrNniLmiCheckPointTimer_Type()
)
mscFrNniLmiCheckPointTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiCheckPointTimer.setStatus("mandatory")


class _MscFrNniLmiIgnoreActiveBit_Type(Integer32):
    """Custom type mscFrNniLmiIgnoreActiveBit based on Integer32"""
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


_MscFrNniLmiIgnoreActiveBit_Type.__name__ = "Integer32"
_MscFrNniLmiIgnoreActiveBit_Object = MibTableColumn
mscFrNniLmiIgnoreActiveBit = _MscFrNniLmiIgnoreActiveBit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 10, 1, 7),
    _MscFrNniLmiIgnoreActiveBit_Type()
)
mscFrNniLmiIgnoreActiveBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiIgnoreActiveBit.setStatus("mandatory")
_MscFrNniLmiNniParmsTable_Object = MibTable
mscFrNniLmiNniParmsTable = _MscFrNniLmiNniParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 11)
)
if mibBuilder.loadTexts:
    mscFrNniLmiNniParmsTable.setStatus("mandatory")
_MscFrNniLmiNniParmsEntry_Object = MibTableRow
mscFrNniLmiNniParmsEntry = _MscFrNniLmiNniParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 11, 1)
)
mscFrNniLmiNniParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLmiNniParmsEntry.setStatus("mandatory")


class _MscFrNniLmiFullStatusPollingCycles_Type(Unsigned32):
    """Custom type mscFrNniLmiFullStatusPollingCycles based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrNniLmiFullStatusPollingCycles_Type.__name__ = "Unsigned32"
_MscFrNniLmiFullStatusPollingCycles_Object = MibTableColumn
mscFrNniLmiFullStatusPollingCycles = _MscFrNniLmiFullStatusPollingCycles_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 11, 1, 1),
    _MscFrNniLmiFullStatusPollingCycles_Type()
)
mscFrNniLmiFullStatusPollingCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiFullStatusPollingCycles.setStatus("mandatory")


class _MscFrNniLmiLinkVerificationTimer_Type(Unsigned32):
    """Custom type mscFrNniLmiLinkVerificationTimer based on Unsigned32"""
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


_MscFrNniLmiLinkVerificationTimer_Type.__name__ = "Unsigned32"
_MscFrNniLmiLinkVerificationTimer_Object = MibTableColumn
mscFrNniLmiLinkVerificationTimer = _MscFrNniLmiLinkVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 11, 1, 2),
    _MscFrNniLmiLinkVerificationTimer_Type()
)
mscFrNniLmiLinkVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLmiLinkVerificationTimer.setStatus("mandatory")
_MscFrNniLmiStateTable_Object = MibTable
mscFrNniLmiStateTable = _MscFrNniLmiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 12)
)
if mibBuilder.loadTexts:
    mscFrNniLmiStateTable.setStatus("mandatory")
_MscFrNniLmiStateEntry_Object = MibTableRow
mscFrNniLmiStateEntry = _MscFrNniLmiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 12, 1)
)
mscFrNniLmiStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLmiStateEntry.setStatus("mandatory")


class _MscFrNniLmiAdminState_Type(Integer32):
    """Custom type mscFrNniLmiAdminState based on Integer32"""
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


_MscFrNniLmiAdminState_Type.__name__ = "Integer32"
_MscFrNniLmiAdminState_Object = MibTableColumn
mscFrNniLmiAdminState = _MscFrNniLmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 12, 1, 1),
    _MscFrNniLmiAdminState_Type()
)
mscFrNniLmiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiAdminState.setStatus("mandatory")


class _MscFrNniLmiOperationalState_Type(Integer32):
    """Custom type mscFrNniLmiOperationalState based on Integer32"""
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


_MscFrNniLmiOperationalState_Type.__name__ = "Integer32"
_MscFrNniLmiOperationalState_Object = MibTableColumn
mscFrNniLmiOperationalState = _MscFrNniLmiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 12, 1, 2),
    _MscFrNniLmiOperationalState_Type()
)
mscFrNniLmiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiOperationalState.setStatus("mandatory")


class _MscFrNniLmiUsageState_Type(Integer32):
    """Custom type mscFrNniLmiUsageState based on Integer32"""
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


_MscFrNniLmiUsageState_Type.__name__ = "Integer32"
_MscFrNniLmiUsageState_Object = MibTableColumn
mscFrNniLmiUsageState = _MscFrNniLmiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 12, 1, 3),
    _MscFrNniLmiUsageState_Type()
)
mscFrNniLmiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiUsageState.setStatus("mandatory")
_MscFrNniLmiPsiTable_Object = MibTable
mscFrNniLmiPsiTable = _MscFrNniLmiPsiTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 13)
)
if mibBuilder.loadTexts:
    mscFrNniLmiPsiTable.setStatus("mandatory")
_MscFrNniLmiPsiEntry_Object = MibTableRow
mscFrNniLmiPsiEntry = _MscFrNniLmiPsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 13, 1)
)
mscFrNniLmiPsiEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLmiPsiEntry.setStatus("mandatory")


class _MscFrNniLmiProtocolStatus_Type(Integer32):
    """Custom type mscFrNniLmiProtocolStatus based on Integer32"""
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


_MscFrNniLmiProtocolStatus_Type.__name__ = "Integer32"
_MscFrNniLmiProtocolStatus_Object = MibTableColumn
mscFrNniLmiProtocolStatus = _MscFrNniLmiProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 13, 1, 1),
    _MscFrNniLmiProtocolStatus_Type()
)
mscFrNniLmiProtocolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiProtocolStatus.setStatus("mandatory")


class _MscFrNniLmiOpProcedures_Type(Integer32):
    """Custom type mscFrNniLmiOpProcedures based on Integer32"""
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


_MscFrNniLmiOpProcedures_Type.__name__ = "Integer32"
_MscFrNniLmiOpProcedures_Object = MibTableColumn
mscFrNniLmiOpProcedures = _MscFrNniLmiOpProcedures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 13, 1, 2),
    _MscFrNniLmiOpProcedures_Type()
)
mscFrNniLmiOpProcedures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiOpProcedures.setStatus("mandatory")
_MscFrNniLmiStatsTable_Object = MibTable
mscFrNniLmiStatsTable = _MscFrNniLmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14)
)
if mibBuilder.loadTexts:
    mscFrNniLmiStatsTable.setStatus("mandatory")
_MscFrNniLmiStatsEntry_Object = MibTableRow
mscFrNniLmiStatsEntry = _MscFrNniLmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1)
)
mscFrNniLmiStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLmiIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLmiStatsEntry.setStatus("mandatory")
_MscFrNniLmiKeepAliveStatusToIf_Type = Counter32
_MscFrNniLmiKeepAliveStatusToIf_Object = MibTableColumn
mscFrNniLmiKeepAliveStatusToIf = _MscFrNniLmiKeepAliveStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 1),
    _MscFrNniLmiKeepAliveStatusToIf_Type()
)
mscFrNniLmiKeepAliveStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiKeepAliveStatusToIf.setStatus("mandatory")
_MscFrNniLmiFullStatusToIf_Type = Counter32
_MscFrNniLmiFullStatusToIf_Object = MibTableColumn
mscFrNniLmiFullStatusToIf = _MscFrNniLmiFullStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 2),
    _MscFrNniLmiFullStatusToIf_Type()
)
mscFrNniLmiFullStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiFullStatusToIf.setStatus("mandatory")
_MscFrNniLmiKeepAliveStatusEnqFromIf_Type = Counter32
_MscFrNniLmiKeepAliveStatusEnqFromIf_Object = MibTableColumn
mscFrNniLmiKeepAliveStatusEnqFromIf = _MscFrNniLmiKeepAliveStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 3),
    _MscFrNniLmiKeepAliveStatusEnqFromIf_Type()
)
mscFrNniLmiKeepAliveStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiKeepAliveStatusEnqFromIf.setStatus("mandatory")
_MscFrNniLmiFullStatusEnqFromIf_Type = Counter32
_MscFrNniLmiFullStatusEnqFromIf_Object = MibTableColumn
mscFrNniLmiFullStatusEnqFromIf = _MscFrNniLmiFullStatusEnqFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 4),
    _MscFrNniLmiFullStatusEnqFromIf_Type()
)
mscFrNniLmiFullStatusEnqFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiFullStatusEnqFromIf.setStatus("mandatory")


class _MscFrNniLmiNetworkSideEventHistory_Type(AsciiString):
    """Custom type mscFrNniLmiNetworkSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscFrNniLmiNetworkSideEventHistory_Type.__name__ = "AsciiString"
_MscFrNniLmiNetworkSideEventHistory_Object = MibTableColumn
mscFrNniLmiNetworkSideEventHistory = _MscFrNniLmiNetworkSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 5),
    _MscFrNniLmiNetworkSideEventHistory_Type()
)
mscFrNniLmiNetworkSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiNetworkSideEventHistory.setStatus("mandatory")


class _MscFrNniLmiUserSideEventHistory_Type(AsciiString):
    """Custom type mscFrNniLmiUserSideEventHistory based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_MscFrNniLmiUserSideEventHistory_Type.__name__ = "AsciiString"
_MscFrNniLmiUserSideEventHistory_Object = MibTableColumn
mscFrNniLmiUserSideEventHistory = _MscFrNniLmiUserSideEventHistory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 6),
    _MscFrNniLmiUserSideEventHistory_Type()
)
mscFrNniLmiUserSideEventHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiUserSideEventHistory.setStatus("mandatory")
_MscFrNniLmiProtocolErrors_Type = Counter32
_MscFrNniLmiProtocolErrors_Object = MibTableColumn
mscFrNniLmiProtocolErrors = _MscFrNniLmiProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 7),
    _MscFrNniLmiProtocolErrors_Type()
)
mscFrNniLmiProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiProtocolErrors.setStatus("mandatory")
_MscFrNniLmiUnexpectedIes_Type = Counter32
_MscFrNniLmiUnexpectedIes_Object = MibTableColumn
mscFrNniLmiUnexpectedIes = _MscFrNniLmiUnexpectedIes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 8),
    _MscFrNniLmiUnexpectedIes_Type()
)
mscFrNniLmiUnexpectedIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiUnexpectedIes.setStatus("mandatory")
_MscFrNniLmiSequenceErrors_Type = Counter32
_MscFrNniLmiSequenceErrors_Object = MibTableColumn
mscFrNniLmiSequenceErrors = _MscFrNniLmiSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 9),
    _MscFrNniLmiSequenceErrors_Type()
)
mscFrNniLmiSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiSequenceErrors.setStatus("mandatory")
_MscFrNniLmiStatusSequenceErrors_Type = Counter32
_MscFrNniLmiStatusSequenceErrors_Object = MibTableColumn
mscFrNniLmiStatusSequenceErrors = _MscFrNniLmiStatusSequenceErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 10),
    _MscFrNniLmiStatusSequenceErrors_Type()
)
mscFrNniLmiStatusSequenceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiStatusSequenceErrors.setStatus("mandatory")
_MscFrNniLmiUnexpectedReports_Type = Counter32
_MscFrNniLmiUnexpectedReports_Object = MibTableColumn
mscFrNniLmiUnexpectedReports = _MscFrNniLmiUnexpectedReports_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 11),
    _MscFrNniLmiUnexpectedReports_Type()
)
mscFrNniLmiUnexpectedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiUnexpectedReports.setStatus("mandatory")
_MscFrNniLmiPollingVerifTimeouts_Type = Counter32
_MscFrNniLmiPollingVerifTimeouts_Object = MibTableColumn
mscFrNniLmiPollingVerifTimeouts = _MscFrNniLmiPollingVerifTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 12),
    _MscFrNniLmiPollingVerifTimeouts_Type()
)
mscFrNniLmiPollingVerifTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiPollingVerifTimeouts.setStatus("mandatory")
_MscFrNniLmiNoStatusReportCount_Type = Counter32
_MscFrNniLmiNoStatusReportCount_Object = MibTableColumn
mscFrNniLmiNoStatusReportCount = _MscFrNniLmiNoStatusReportCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 4, 14, 1, 13),
    _MscFrNniLmiNoStatusReportCount_Type()
)
mscFrNniLmiNoStatusReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLmiNoStatusReportCount.setStatus("mandatory")
_MscFrNniDlci_ObjectIdentity = ObjectIdentity
mscFrNniDlci = _MscFrNniDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5)
)
_MscFrNniDlciRowStatusTable_Object = MibTable
mscFrNniDlciRowStatusTable = _MscFrNniDlciRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDlciRowStatusTable.setStatus("mandatory")
_MscFrNniDlciRowStatusEntry_Object = MibTableRow
mscFrNniDlciRowStatusEntry = _MscFrNniDlciRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 1, 1)
)
mscFrNniDlciRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciRowStatusEntry.setStatus("mandatory")
_MscFrNniDlciRowStatus_Type = RowStatus
_MscFrNniDlciRowStatus_Object = MibTableColumn
mscFrNniDlciRowStatus = _MscFrNniDlciRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 1, 1, 1),
    _MscFrNniDlciRowStatus_Type()
)
mscFrNniDlciRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciRowStatus.setStatus("mandatory")
_MscFrNniDlciComponentName_Type = DisplayString
_MscFrNniDlciComponentName_Object = MibTableColumn
mscFrNniDlciComponentName = _MscFrNniDlciComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 1, 1, 2),
    _MscFrNniDlciComponentName_Type()
)
mscFrNniDlciComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciComponentName.setStatus("mandatory")
_MscFrNniDlciStorageType_Type = StorageType
_MscFrNniDlciStorageType_Object = MibTableColumn
mscFrNniDlciStorageType = _MscFrNniDlciStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 1, 1, 4),
    _MscFrNniDlciStorageType_Type()
)
mscFrNniDlciStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciStorageType.setStatus("mandatory")


class _MscFrNniDlciIndex_Type(Integer32):
    """Custom type mscFrNniDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrNniDlciIndex_Type.__name__ = "Integer32"
_MscFrNniDlciIndex_Object = MibTableColumn
mscFrNniDlciIndex = _MscFrNniDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 1, 1, 10),
    _MscFrNniDlciIndex_Type()
)
mscFrNniDlciIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDlciIndex.setStatus("mandatory")
_MscFrNniDlciDc_ObjectIdentity = ObjectIdentity
mscFrNniDlciDc = _MscFrNniDlciDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2)
)
_MscFrNniDlciDcRowStatusTable_Object = MibTable
mscFrNniDlciDcRowStatusTable = _MscFrNniDlciDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDlciDcRowStatusTable.setStatus("mandatory")
_MscFrNniDlciDcRowStatusEntry_Object = MibTableRow
mscFrNniDlciDcRowStatusEntry = _MscFrNniDlciDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 1, 1)
)
mscFrNniDlciDcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciDcRowStatusEntry.setStatus("mandatory")
_MscFrNniDlciDcRowStatus_Type = RowStatus
_MscFrNniDlciDcRowStatus_Object = MibTableColumn
mscFrNniDlciDcRowStatus = _MscFrNniDlciDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 1, 1, 1),
    _MscFrNniDlciDcRowStatus_Type()
)
mscFrNniDlciDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDcRowStatus.setStatus("mandatory")
_MscFrNniDlciDcComponentName_Type = DisplayString
_MscFrNniDlciDcComponentName_Object = MibTableColumn
mscFrNniDlciDcComponentName = _MscFrNniDlciDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 1, 1, 2),
    _MscFrNniDlciDcComponentName_Type()
)
mscFrNniDlciDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDcComponentName.setStatus("mandatory")
_MscFrNniDlciDcStorageType_Type = StorageType
_MscFrNniDlciDcStorageType_Object = MibTableColumn
mscFrNniDlciDcStorageType = _MscFrNniDlciDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 1, 1, 4),
    _MscFrNniDlciDcStorageType_Type()
)
mscFrNniDlciDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDcStorageType.setStatus("mandatory")
_MscFrNniDlciDcIndex_Type = NonReplicated
_MscFrNniDlciDcIndex_Object = MibTableColumn
mscFrNniDlciDcIndex = _MscFrNniDlciDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 1, 1, 10),
    _MscFrNniDlciDcIndex_Type()
)
mscFrNniDlciDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDlciDcIndex.setStatus("mandatory")
_MscFrNniDlciDcOptionsTable_Object = MibTable
mscFrNniDlciDcOptionsTable = _MscFrNniDlciDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDlciDcOptionsTable.setStatus("mandatory")
_MscFrNniDlciDcOptionsEntry_Object = MibTableRow
mscFrNniDlciDcOptionsEntry = _MscFrNniDlciDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1)
)
mscFrNniDlciDcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciDcIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciDcOptionsEntry.setStatus("mandatory")


class _MscFrNniDlciDcRemoteNpi_Type(Integer32):
    """Custom type mscFrNniDlciDcRemoteNpi based on Integer32"""
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


_MscFrNniDlciDcRemoteNpi_Type.__name__ = "Integer32"
_MscFrNniDlciDcRemoteNpi_Object = MibTableColumn
mscFrNniDlciDcRemoteNpi = _MscFrNniDlciDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 3),
    _MscFrNniDlciDcRemoteNpi_Type()
)
mscFrNniDlciDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcRemoteNpi.setStatus("mandatory")


class _MscFrNniDlciDcRemoteDna_Type(DigitString):
    """Custom type mscFrNniDlciDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrNniDlciDcRemoteDna_Type.__name__ = "DigitString"
_MscFrNniDlciDcRemoteDna_Object = MibTableColumn
mscFrNniDlciDcRemoteDna = _MscFrNniDlciDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 4),
    _MscFrNniDlciDcRemoteDna_Type()
)
mscFrNniDlciDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcRemoteDna.setStatus("mandatory")


class _MscFrNniDlciDcRemoteDlci_Type(Unsigned32):
    """Custom type mscFrNniDlciDcRemoteDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrNniDlciDcRemoteDlci_Type.__name__ = "Unsigned32"
_MscFrNniDlciDcRemoteDlci_Object = MibTableColumn
mscFrNniDlciDcRemoteDlci = _MscFrNniDlciDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 5),
    _MscFrNniDlciDcRemoteDlci_Type()
)
mscFrNniDlciDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcRemoteDlci.setStatus("mandatory")


class _MscFrNniDlciDcType_Type(Integer32):
    """Custom type mscFrNniDlciDcType based on Integer32"""
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


_MscFrNniDlciDcType_Type.__name__ = "Integer32"
_MscFrNniDlciDcType_Object = MibTableColumn
mscFrNniDlciDcType = _MscFrNniDlciDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 6),
    _MscFrNniDlciDcType_Type()
)
mscFrNniDlciDcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcType.setStatus("mandatory")


class _MscFrNniDlciDcTransferPriority_Type(Integer32):
    """Custom type mscFrNniDlciDcTransferPriority based on Integer32"""
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


_MscFrNniDlciDcTransferPriority_Type.__name__ = "Integer32"
_MscFrNniDlciDcTransferPriority_Object = MibTableColumn
mscFrNniDlciDcTransferPriority = _MscFrNniDlciDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 9),
    _MscFrNniDlciDcTransferPriority_Type()
)
mscFrNniDlciDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcTransferPriority.setStatus("mandatory")


class _MscFrNniDlciDcDiscardPriority_Type(Integer32):
    """Custom type mscFrNniDlciDcDiscardPriority based on Integer32"""
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


_MscFrNniDlciDcDiscardPriority_Type.__name__ = "Integer32"
_MscFrNniDlciDcDiscardPriority_Object = MibTableColumn
mscFrNniDlciDcDiscardPriority = _MscFrNniDlciDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 10),
    _MscFrNniDlciDcDiscardPriority_Type()
)
mscFrNniDlciDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcDiscardPriority.setStatus("mandatory")


class _MscFrNniDlciDcDeDiscardPriority_Type(Integer32):
    """Custom type mscFrNniDlciDcDeDiscardPriority based on Integer32"""
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


_MscFrNniDlciDcDeDiscardPriority_Type.__name__ = "Integer32"
_MscFrNniDlciDcDeDiscardPriority_Object = MibTableColumn
mscFrNniDlciDcDeDiscardPriority = _MscFrNniDlciDcDeDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 11),
    _MscFrNniDlciDcDeDiscardPriority_Type()
)
mscFrNniDlciDcDeDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcDeDiscardPriority.setStatus("mandatory")


class _MscFrNniDlciDcDataPath_Type(Integer32):
    """Custom type mscFrNniDlciDcDataPath based on Integer32"""
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


_MscFrNniDlciDcDataPath_Type.__name__ = "Integer32"
_MscFrNniDlciDcDataPath_Object = MibTableColumn
mscFrNniDlciDcDataPath = _MscFrNniDlciDcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 12),
    _MscFrNniDlciDcDataPath_Type()
)
mscFrNniDlciDcDataPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcDataPath.setStatus("mandatory")


class _MscFrNniDlciDcCugIndex_Type(Unsigned32):
    """Custom type mscFrNniDlciDcCugIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniDlciDcCugIndex_Type.__name__ = "Unsigned32"
_MscFrNniDlciDcCugIndex_Object = MibTableColumn
mscFrNniDlciDcCugIndex = _MscFrNniDlciDcCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 13),
    _MscFrNniDlciDcCugIndex_Type()
)
mscFrNniDlciDcCugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcCugIndex.setStatus("mandatory")


class _MscFrNniDlciDcCugType_Type(Integer32):
    """Custom type mscFrNniDlciDcCugType based on Integer32"""
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


_MscFrNniDlciDcCugType_Type.__name__ = "Integer32"
_MscFrNniDlciDcCugType_Object = MibTableColumn
mscFrNniDlciDcCugType = _MscFrNniDlciDcCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 14),
    _MscFrNniDlciDcCugType_Type()
)
mscFrNniDlciDcCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcCugType.setStatus("mandatory")


class _MscFrNniDlciDcMapIpCosToFrQos_Type(Integer32):
    """Custom type mscFrNniDlciDcMapIpCosToFrQos based on Integer32"""
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


_MscFrNniDlciDcMapIpCosToFrQos_Type.__name__ = "Integer32"
_MscFrNniDlciDcMapIpCosToFrQos_Object = MibTableColumn
mscFrNniDlciDcMapIpCosToFrQos = _MscFrNniDlciDcMapIpCosToFrQos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 10, 1, 15),
    _MscFrNniDlciDcMapIpCosToFrQos_Type()
)
mscFrNniDlciDcMapIpCosToFrQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcMapIpCosToFrQos.setStatus("mandatory")
_MscFrNniDlciDcNfaTable_Object = MibTable
mscFrNniDlciDcNfaTable = _MscFrNniDlciDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 202)
)
if mibBuilder.loadTexts:
    mscFrNniDlciDcNfaTable.setStatus("obsolete")
_MscFrNniDlciDcNfaEntry_Object = MibTableRow
mscFrNniDlciDcNfaEntry = _MscFrNniDlciDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 202, 1)
)
mscFrNniDlciDcNfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciDcNfaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciDcNfaEntry.setStatus("obsolete")


class _MscFrNniDlciDcNfaIndex_Type(Integer32):
    """Custom type mscFrNniDlciDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(48, 48),
    )


_MscFrNniDlciDcNfaIndex_Type.__name__ = "Integer32"
_MscFrNniDlciDcNfaIndex_Object = MibTableColumn
mscFrNniDlciDcNfaIndex = _MscFrNniDlciDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 202, 1, 1),
    _MscFrNniDlciDcNfaIndex_Type()
)
mscFrNniDlciDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDlciDcNfaIndex.setStatus("obsolete")


class _MscFrNniDlciDcNfaValue_Type(HexString):
    """Custom type mscFrNniDlciDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscFrNniDlciDcNfaValue_Type.__name__ = "HexString"
_MscFrNniDlciDcNfaValue_Object = MibTableColumn
mscFrNniDlciDcNfaValue = _MscFrNniDlciDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 202, 1, 2),
    _MscFrNniDlciDcNfaValue_Type()
)
mscFrNniDlciDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciDcNfaValue.setStatus("obsolete")
_MscFrNniDlciDcNfaRowStatus_Type = RowStatus
_MscFrNniDlciDcNfaRowStatus_Object = MibTableColumn
mscFrNniDlciDcNfaRowStatus = _MscFrNniDlciDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 2, 202, 1, 3),
    _MscFrNniDlciDcNfaRowStatus_Type()
)
mscFrNniDlciDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDcNfaRowStatus.setStatus("obsolete")
_MscFrNniDlciVc_ObjectIdentity = ObjectIdentity
mscFrNniDlciVc = _MscFrNniDlciVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3)
)
_MscFrNniDlciVcRowStatusTable_Object = MibTable
mscFrNniDlciVcRowStatusTable = _MscFrNniDlciVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcRowStatusTable.setStatus("mandatory")
_MscFrNniDlciVcRowStatusEntry_Object = MibTableRow
mscFrNniDlciVcRowStatusEntry = _MscFrNniDlciVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 1, 1)
)
mscFrNniDlciVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcRowStatusEntry.setStatus("mandatory")
_MscFrNniDlciVcRowStatus_Type = RowStatus
_MscFrNniDlciVcRowStatus_Object = MibTableColumn
mscFrNniDlciVcRowStatus = _MscFrNniDlciVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 1, 1, 1),
    _MscFrNniDlciVcRowStatus_Type()
)
mscFrNniDlciVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcRowStatus.setStatus("mandatory")
_MscFrNniDlciVcComponentName_Type = DisplayString
_MscFrNniDlciVcComponentName_Object = MibTableColumn
mscFrNniDlciVcComponentName = _MscFrNniDlciVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 1, 1, 2),
    _MscFrNniDlciVcComponentName_Type()
)
mscFrNniDlciVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcComponentName.setStatus("mandatory")
_MscFrNniDlciVcStorageType_Type = StorageType
_MscFrNniDlciVcStorageType_Object = MibTableColumn
mscFrNniDlciVcStorageType = _MscFrNniDlciVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 1, 1, 4),
    _MscFrNniDlciVcStorageType_Type()
)
mscFrNniDlciVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcStorageType.setStatus("mandatory")
_MscFrNniDlciVcIndex_Type = NonReplicated
_MscFrNniDlciVcIndex_Object = MibTableColumn
mscFrNniDlciVcIndex = _MscFrNniDlciVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 1, 1, 10),
    _MscFrNniDlciVcIndex_Type()
)
mscFrNniDlciVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDlciVcIndex.setStatus("mandatory")
_MscFrNniDlciVcCadTable_Object = MibTable
mscFrNniDlciVcCadTable = _MscFrNniDlciVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcCadTable.setStatus("mandatory")
_MscFrNniDlciVcCadEntry_Object = MibTableRow
mscFrNniDlciVcCadEntry = _MscFrNniDlciVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1)
)
mscFrNniDlciVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcCadEntry.setStatus("mandatory")


class _MscFrNniDlciVcType_Type(Integer32):
    """Custom type mscFrNniDlciVcType based on Integer32"""
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


_MscFrNniDlciVcType_Type.__name__ = "Integer32"
_MscFrNniDlciVcType_Object = MibTableColumn
mscFrNniDlciVcType = _MscFrNniDlciVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 1),
    _MscFrNniDlciVcType_Type()
)
mscFrNniDlciVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcType.setStatus("mandatory")


class _MscFrNniDlciVcState_Type(Integer32):
    """Custom type mscFrNniDlciVcState based on Integer32"""
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


_MscFrNniDlciVcState_Type.__name__ = "Integer32"
_MscFrNniDlciVcState_Object = MibTableColumn
mscFrNniDlciVcState = _MscFrNniDlciVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 2),
    _MscFrNniDlciVcState_Type()
)
mscFrNniDlciVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcState.setStatus("mandatory")


class _MscFrNniDlciVcPreviousState_Type(Integer32):
    """Custom type mscFrNniDlciVcPreviousState based on Integer32"""
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


_MscFrNniDlciVcPreviousState_Type.__name__ = "Integer32"
_MscFrNniDlciVcPreviousState_Object = MibTableColumn
mscFrNniDlciVcPreviousState = _MscFrNniDlciVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 3),
    _MscFrNniDlciVcPreviousState_Type()
)
mscFrNniDlciVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPreviousState.setStatus("mandatory")


class _MscFrNniDlciVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscFrNniDlciVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniDlciVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcDiagnosticCode_Object = MibTableColumn
mscFrNniDlciVcDiagnosticCode = _MscFrNniDlciVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 4),
    _MscFrNniDlciVcDiagnosticCode_Type()
)
mscFrNniDlciVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcDiagnosticCode.setStatus("mandatory")


class _MscFrNniDlciVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscFrNniDlciVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniDlciVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcPreviousDiagnosticCode_Object = MibTableColumn
mscFrNniDlciVcPreviousDiagnosticCode = _MscFrNniDlciVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 5),
    _MscFrNniDlciVcPreviousDiagnosticCode_Type()
)
mscFrNniDlciVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscFrNniDlciVcCalledNpi_Type(Integer32):
    """Custom type mscFrNniDlciVcCalledNpi based on Integer32"""
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


_MscFrNniDlciVcCalledNpi_Type.__name__ = "Integer32"
_MscFrNniDlciVcCalledNpi_Object = MibTableColumn
mscFrNniDlciVcCalledNpi = _MscFrNniDlciVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 6),
    _MscFrNniDlciVcCalledNpi_Type()
)
mscFrNniDlciVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCalledNpi.setStatus("mandatory")


class _MscFrNniDlciVcCalledDna_Type(DigitString):
    """Custom type mscFrNniDlciVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrNniDlciVcCalledDna_Type.__name__ = "DigitString"
_MscFrNniDlciVcCalledDna_Object = MibTableColumn
mscFrNniDlciVcCalledDna = _MscFrNniDlciVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 7),
    _MscFrNniDlciVcCalledDna_Type()
)
mscFrNniDlciVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCalledDna.setStatus("mandatory")


class _MscFrNniDlciVcCalledLcn_Type(Unsigned32):
    """Custom type mscFrNniDlciVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrNniDlciVcCalledLcn_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcCalledLcn_Object = MibTableColumn
mscFrNniDlciVcCalledLcn = _MscFrNniDlciVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 8),
    _MscFrNniDlciVcCalledLcn_Type()
)
mscFrNniDlciVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCalledLcn.setStatus("mandatory")


class _MscFrNniDlciVcCallingNpi_Type(Integer32):
    """Custom type mscFrNniDlciVcCallingNpi based on Integer32"""
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


_MscFrNniDlciVcCallingNpi_Type.__name__ = "Integer32"
_MscFrNniDlciVcCallingNpi_Object = MibTableColumn
mscFrNniDlciVcCallingNpi = _MscFrNniDlciVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 9),
    _MscFrNniDlciVcCallingNpi_Type()
)
mscFrNniDlciVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCallingNpi.setStatus("mandatory")


class _MscFrNniDlciVcCallingDna_Type(DigitString):
    """Custom type mscFrNniDlciVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscFrNniDlciVcCallingDna_Type.__name__ = "DigitString"
_MscFrNniDlciVcCallingDna_Object = MibTableColumn
mscFrNniDlciVcCallingDna = _MscFrNniDlciVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 10),
    _MscFrNniDlciVcCallingDna_Type()
)
mscFrNniDlciVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCallingDna.setStatus("mandatory")


class _MscFrNniDlciVcCallingLcn_Type(Unsigned32):
    """Custom type mscFrNniDlciVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrNniDlciVcCallingLcn_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcCallingLcn_Object = MibTableColumn
mscFrNniDlciVcCallingLcn = _MscFrNniDlciVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 11),
    _MscFrNniDlciVcCallingLcn_Type()
)
mscFrNniDlciVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCallingLcn.setStatus("mandatory")


class _MscFrNniDlciVcAccountingEnabled_Type(Integer32):
    """Custom type mscFrNniDlciVcAccountingEnabled based on Integer32"""
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


_MscFrNniDlciVcAccountingEnabled_Type.__name__ = "Integer32"
_MscFrNniDlciVcAccountingEnabled_Object = MibTableColumn
mscFrNniDlciVcAccountingEnabled = _MscFrNniDlciVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 12),
    _MscFrNniDlciVcAccountingEnabled_Type()
)
mscFrNniDlciVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcAccountingEnabled.setStatus("mandatory")


class _MscFrNniDlciVcFastSelectCall_Type(Integer32):
    """Custom type mscFrNniDlciVcFastSelectCall based on Integer32"""
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


_MscFrNniDlciVcFastSelectCall_Type.__name__ = "Integer32"
_MscFrNniDlciVcFastSelectCall_Object = MibTableColumn
mscFrNniDlciVcFastSelectCall = _MscFrNniDlciVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 13),
    _MscFrNniDlciVcFastSelectCall_Type()
)
mscFrNniDlciVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcFastSelectCall.setStatus("mandatory")


class _MscFrNniDlciVcPathReliability_Type(Integer32):
    """Custom type mscFrNniDlciVcPathReliability based on Integer32"""
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


_MscFrNniDlciVcPathReliability_Type.__name__ = "Integer32"
_MscFrNniDlciVcPathReliability_Object = MibTableColumn
mscFrNniDlciVcPathReliability = _MscFrNniDlciVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 19),
    _MscFrNniDlciVcPathReliability_Type()
)
mscFrNniDlciVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPathReliability.setStatus("mandatory")


class _MscFrNniDlciVcAccountingEnd_Type(Integer32):
    """Custom type mscFrNniDlciVcAccountingEnd based on Integer32"""
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


_MscFrNniDlciVcAccountingEnd_Type.__name__ = "Integer32"
_MscFrNniDlciVcAccountingEnd_Object = MibTableColumn
mscFrNniDlciVcAccountingEnd = _MscFrNniDlciVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 20),
    _MscFrNniDlciVcAccountingEnd_Type()
)
mscFrNniDlciVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcAccountingEnd.setStatus("mandatory")


class _MscFrNniDlciVcPriority_Type(Integer32):
    """Custom type mscFrNniDlciVcPriority based on Integer32"""
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


_MscFrNniDlciVcPriority_Type.__name__ = "Integer32"
_MscFrNniDlciVcPriority_Object = MibTableColumn
mscFrNniDlciVcPriority = _MscFrNniDlciVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 21),
    _MscFrNniDlciVcPriority_Type()
)
mscFrNniDlciVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPriority.setStatus("mandatory")


class _MscFrNniDlciVcSegmentSize_Type(Unsigned32):
    """Custom type mscFrNniDlciVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscFrNniDlciVcSegmentSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcSegmentSize_Object = MibTableColumn
mscFrNniDlciVcSegmentSize = _MscFrNniDlciVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 22),
    _MscFrNniDlciVcSegmentSize_Type()
)
mscFrNniDlciVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcSegmentSize.setStatus("mandatory")


class _MscFrNniDlciVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscFrNniDlciVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscFrNniDlciVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcMaxSubnetPktSize_Object = MibTableColumn
mscFrNniDlciVcMaxSubnetPktSize = _MscFrNniDlciVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 27),
    _MscFrNniDlciVcMaxSubnetPktSize_Type()
)
mscFrNniDlciVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcMaxSubnetPktSize.setStatus("mandatory")


class _MscFrNniDlciVcRcosToNetwork_Type(Integer32):
    """Custom type mscFrNniDlciVcRcosToNetwork based on Integer32"""
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


_MscFrNniDlciVcRcosToNetwork_Type.__name__ = "Integer32"
_MscFrNniDlciVcRcosToNetwork_Object = MibTableColumn
mscFrNniDlciVcRcosToNetwork = _MscFrNniDlciVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 28),
    _MscFrNniDlciVcRcosToNetwork_Type()
)
mscFrNniDlciVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcRcosToNetwork.setStatus("mandatory")


class _MscFrNniDlciVcRcosFromNetwork_Type(Integer32):
    """Custom type mscFrNniDlciVcRcosFromNetwork based on Integer32"""
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


_MscFrNniDlciVcRcosFromNetwork_Type.__name__ = "Integer32"
_MscFrNniDlciVcRcosFromNetwork_Object = MibTableColumn
mscFrNniDlciVcRcosFromNetwork = _MscFrNniDlciVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 29),
    _MscFrNniDlciVcRcosFromNetwork_Type()
)
mscFrNniDlciVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcRcosFromNetwork.setStatus("mandatory")


class _MscFrNniDlciVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscFrNniDlciVcEmissionPriorityToNetwork based on Integer32"""
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


_MscFrNniDlciVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscFrNniDlciVcEmissionPriorityToNetwork_Object = MibTableColumn
mscFrNniDlciVcEmissionPriorityToNetwork = _MscFrNniDlciVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 30),
    _MscFrNniDlciVcEmissionPriorityToNetwork_Type()
)
mscFrNniDlciVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MscFrNniDlciVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscFrNniDlciVcEmissionPriorityFromNetwork based on Integer32"""
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


_MscFrNniDlciVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscFrNniDlciVcEmissionPriorityFromNetwork_Object = MibTableColumn
mscFrNniDlciVcEmissionPriorityFromNetwork = _MscFrNniDlciVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 31),
    _MscFrNniDlciVcEmissionPriorityFromNetwork_Type()
)
mscFrNniDlciVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscFrNniDlciVcDataPath_Type(AsciiString):
    """Custom type mscFrNniDlciVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscFrNniDlciVcDataPath_Type.__name__ = "AsciiString"
_MscFrNniDlciVcDataPath_Object = MibTableColumn
mscFrNniDlciVcDataPath = _MscFrNniDlciVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 10, 1, 32),
    _MscFrNniDlciVcDataPath_Type()
)
mscFrNniDlciVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcDataPath.setStatus("mandatory")
_MscFrNniDlciVcIntdTable_Object = MibTable
mscFrNniDlciVcIntdTable = _MscFrNniDlciVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11)
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcIntdTable.setStatus("mandatory")
_MscFrNniDlciVcIntdEntry_Object = MibTableRow
mscFrNniDlciVcIntdEntry = _MscFrNniDlciVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11, 1)
)
mscFrNniDlciVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcIntdEntry.setStatus("mandatory")


class _MscFrNniDlciVcCallReferenceNumber_Type(Hex):
    """Custom type mscFrNniDlciVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrNniDlciVcCallReferenceNumber_Type.__name__ = "Hex"
_MscFrNniDlciVcCallReferenceNumber_Object = MibTableColumn
mscFrNniDlciVcCallReferenceNumber = _MscFrNniDlciVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11, 1, 1),
    _MscFrNniDlciVcCallReferenceNumber_Type()
)
mscFrNniDlciVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCallReferenceNumber.setStatus("obsolete")


class _MscFrNniDlciVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscFrNniDlciVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrNniDlciVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcElapsedTimeTillNow_Object = MibTableColumn
mscFrNniDlciVcElapsedTimeTillNow = _MscFrNniDlciVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11, 1, 2),
    _MscFrNniDlciVcElapsedTimeTillNow_Type()
)
mscFrNniDlciVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcElapsedTimeTillNow.setStatus("mandatory")


class _MscFrNniDlciVcSegmentsRx_Type(Unsigned32):
    """Custom type mscFrNniDlciVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrNniDlciVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcSegmentsRx_Object = MibTableColumn
mscFrNniDlciVcSegmentsRx = _MscFrNniDlciVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11, 1, 3),
    _MscFrNniDlciVcSegmentsRx_Type()
)
mscFrNniDlciVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcSegmentsRx.setStatus("mandatory")


class _MscFrNniDlciVcSegmentsSent_Type(Unsigned32):
    """Custom type mscFrNniDlciVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrNniDlciVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcSegmentsSent_Object = MibTableColumn
mscFrNniDlciVcSegmentsSent = _MscFrNniDlciVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11, 1, 4),
    _MscFrNniDlciVcSegmentsSent_Type()
)
mscFrNniDlciVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcSegmentsSent.setStatus("mandatory")


class _MscFrNniDlciVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrNniDlciVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrNniDlciVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrNniDlciVcStartTime_Object = MibTableColumn
mscFrNniDlciVcStartTime = _MscFrNniDlciVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11, 1, 5),
    _MscFrNniDlciVcStartTime_Type()
)
mscFrNniDlciVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcStartTime.setStatus("mandatory")


class _MscFrNniDlciVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscFrNniDlciVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcCallReferenceNumberDecimal_Object = MibTableColumn
mscFrNniDlciVcCallReferenceNumberDecimal = _MscFrNniDlciVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 11, 1, 7),
    _MscFrNniDlciVcCallReferenceNumberDecimal_Type()
)
mscFrNniDlciVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscFrNniDlciVcFrdTable_Object = MibTable
mscFrNniDlciVcFrdTable = _MscFrNniDlciVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12)
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcFrdTable.setStatus("mandatory")
_MscFrNniDlciVcFrdEntry_Object = MibTableRow
mscFrNniDlciVcFrdEntry = _MscFrNniDlciVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1)
)
mscFrNniDlciVcFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciVcIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcFrdEntry.setStatus("mandatory")


class _MscFrNniDlciVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcFrmCongestedToSubnet_Object = MibTableColumn
mscFrNniDlciVcFrmCongestedToSubnet = _MscFrNniDlciVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 2),
    _MscFrNniDlciVcFrmCongestedToSubnet_Type()
)
mscFrNniDlciVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcFrmCongestedToSubnet.setStatus("mandatory")


class _MscFrNniDlciVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcCannotForwardToSubnet_Object = MibTableColumn
mscFrNniDlciVcCannotForwardToSubnet = _MscFrNniDlciVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 3),
    _MscFrNniDlciVcCannotForwardToSubnet_Type()
)
mscFrNniDlciVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCannotForwardToSubnet.setStatus("mandatory")


class _MscFrNniDlciVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcNotDataXferToSubnet_Object = MibTableColumn
mscFrNniDlciVcNotDataXferToSubnet = _MscFrNniDlciVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 4),
    _MscFrNniDlciVcNotDataXferToSubnet_Type()
)
mscFrNniDlciVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcNotDataXferToSubnet.setStatus("mandatory")


class _MscFrNniDlciVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscFrNniDlciVcOutOfRangeFrmFromSubnet = _MscFrNniDlciVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 5),
    _MscFrNniDlciVcOutOfRangeFrmFromSubnet_Type()
)
mscFrNniDlciVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscFrNniDlciVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcCombErrorsFromSubnet_Object = MibTableColumn
mscFrNniDlciVcCombErrorsFromSubnet = _MscFrNniDlciVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 6),
    _MscFrNniDlciVcCombErrorsFromSubnet_Type()
)
mscFrNniDlciVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcCombErrorsFromSubnet.setStatus("mandatory")


class _MscFrNniDlciVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcDuplicatesFromSubnet_Object = MibTableColumn
mscFrNniDlciVcDuplicatesFromSubnet = _MscFrNniDlciVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 7),
    _MscFrNniDlciVcDuplicatesFromSubnet_Type()
)
mscFrNniDlciVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscFrNniDlciVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcNotDataXferFromSubnet_Object = MibTableColumn
mscFrNniDlciVcNotDataXferFromSubnet = _MscFrNniDlciVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 8),
    _MscFrNniDlciVcNotDataXferFromSubnet_Type()
)
mscFrNniDlciVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcNotDataXferFromSubnet.setStatus("mandatory")


class _MscFrNniDlciVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscFrNniDlciVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcFrmLossTimeouts_Object = MibTableColumn
mscFrNniDlciVcFrmLossTimeouts = _MscFrNniDlciVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 9),
    _MscFrNniDlciVcFrmLossTimeouts_Type()
)
mscFrNniDlciVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcFrmLossTimeouts.setStatus("mandatory")


class _MscFrNniDlciVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscFrNniDlciVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcOoSeqByteCntExceeded_Object = MibTableColumn
mscFrNniDlciVcOoSeqByteCntExceeded = _MscFrNniDlciVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 10),
    _MscFrNniDlciVcOoSeqByteCntExceeded_Type()
)
mscFrNniDlciVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MscFrNniDlciVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscFrNniDlciVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcPeakOoSeqPktCount_Object = MibTableColumn
mscFrNniDlciVcPeakOoSeqPktCount = _MscFrNniDlciVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 11),
    _MscFrNniDlciVcPeakOoSeqPktCount_Type()
)
mscFrNniDlciVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPeakOoSeqPktCount.setStatus("mandatory")


class _MscFrNniDlciVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscFrNniDlciVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscFrNniDlciVcPeakOoSeqFrmForwarded = _MscFrNniDlciVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 12),
    _MscFrNniDlciVcPeakOoSeqFrmForwarded_Type()
)
mscFrNniDlciVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscFrNniDlciVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mscFrNniDlciVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcSendSequenceNumber_Object = MibTableColumn
mscFrNniDlciVcSendSequenceNumber = _MscFrNniDlciVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 13),
    _MscFrNniDlciVcSendSequenceNumber_Type()
)
mscFrNniDlciVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcSendSequenceNumber.setStatus("mandatory")


class _MscFrNniDlciVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscFrNniDlciVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcPktRetryTimeouts_Object = MibTableColumn
mscFrNniDlciVcPktRetryTimeouts = _MscFrNniDlciVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 15),
    _MscFrNniDlciVcPktRetryTimeouts_Type()
)
mscFrNniDlciVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPktRetryTimeouts.setStatus("mandatory")


class _MscFrNniDlciVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscFrNniDlciVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcPeakRetryQueueSize_Object = MibTableColumn
mscFrNniDlciVcPeakRetryQueueSize = _MscFrNniDlciVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 16),
    _MscFrNniDlciVcPeakRetryQueueSize_Type()
)
mscFrNniDlciVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPeakRetryQueueSize.setStatus("mandatory")


class _MscFrNniDlciVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscFrNniDlciVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscFrNniDlciVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcSubnetRecoveries_Object = MibTableColumn
mscFrNniDlciVcSubnetRecoveries = _MscFrNniDlciVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 17),
    _MscFrNniDlciVcSubnetRecoveries_Type()
)
mscFrNniDlciVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcSubnetRecoveries.setStatus("mandatory")


class _MscFrNniDlciVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscFrNniDlciVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniDlciVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcOoSeqPktCntExceeded_Object = MibTableColumn
mscFrNniDlciVcOoSeqPktCntExceeded = _MscFrNniDlciVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 19),
    _MscFrNniDlciVcOoSeqPktCntExceeded_Type()
)
mscFrNniDlciVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MscFrNniDlciVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscFrNniDlciVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscFrNniDlciVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscFrNniDlciVcPeakOoSeqByteCount_Object = MibTableColumn
mscFrNniDlciVcPeakOoSeqByteCount = _MscFrNniDlciVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 12, 1, 20),
    _MscFrNniDlciVcPeakOoSeqByteCount_Type()
)
mscFrNniDlciVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcPeakOoSeqByteCount.setStatus("mandatory")
_MscFrNniDlciVcDmepTable_Object = MibTable
mscFrNniDlciVcDmepTable = _MscFrNniDlciVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 417)
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcDmepTable.setStatus("mandatory")
_MscFrNniDlciVcDmepEntry_Object = MibTableRow
mscFrNniDlciVcDmepEntry = _MscFrNniDlciVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 417, 1)
)
mscFrNniDlciVcDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciVcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciVcDmepValue"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciVcDmepEntry.setStatus("mandatory")
_MscFrNniDlciVcDmepValue_Type = RowPointer
_MscFrNniDlciVcDmepValue_Object = MibTableColumn
mscFrNniDlciVcDmepValue = _MscFrNniDlciVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 3, 417, 1, 1),
    _MscFrNniDlciVcDmepValue_Type()
)
mscFrNniDlciVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciVcDmepValue.setStatus("mandatory")
_MscFrNniDlciSp_ObjectIdentity = ObjectIdentity
mscFrNniDlciSp = _MscFrNniDlciSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4)
)
_MscFrNniDlciSpRowStatusTable_Object = MibTable
mscFrNniDlciSpRowStatusTable = _MscFrNniDlciSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDlciSpRowStatusTable.setStatus("mandatory")
_MscFrNniDlciSpRowStatusEntry_Object = MibTableRow
mscFrNniDlciSpRowStatusEntry = _MscFrNniDlciSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 1, 1)
)
mscFrNniDlciSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciSpRowStatusEntry.setStatus("mandatory")
_MscFrNniDlciSpRowStatus_Type = RowStatus
_MscFrNniDlciSpRowStatus_Object = MibTableColumn
mscFrNniDlciSpRowStatus = _MscFrNniDlciSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 1, 1, 1),
    _MscFrNniDlciSpRowStatus_Type()
)
mscFrNniDlciSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciSpRowStatus.setStatus("mandatory")
_MscFrNniDlciSpComponentName_Type = DisplayString
_MscFrNniDlciSpComponentName_Object = MibTableColumn
mscFrNniDlciSpComponentName = _MscFrNniDlciSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 1, 1, 2),
    _MscFrNniDlciSpComponentName_Type()
)
mscFrNniDlciSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciSpComponentName.setStatus("mandatory")
_MscFrNniDlciSpStorageType_Type = StorageType
_MscFrNniDlciSpStorageType_Object = MibTableColumn
mscFrNniDlciSpStorageType = _MscFrNniDlciSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 1, 1, 4),
    _MscFrNniDlciSpStorageType_Type()
)
mscFrNniDlciSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciSpStorageType.setStatus("mandatory")
_MscFrNniDlciSpIndex_Type = NonReplicated
_MscFrNniDlciSpIndex_Object = MibTableColumn
mscFrNniDlciSpIndex = _MscFrNniDlciSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 1, 1, 10),
    _MscFrNniDlciSpIndex_Type()
)
mscFrNniDlciSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDlciSpIndex.setStatus("mandatory")
_MscFrNniDlciSpParmsTable_Object = MibTable
mscFrNniDlciSpParmsTable = _MscFrNniDlciSpParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mscFrNniDlciSpParmsTable.setStatus("mandatory")
_MscFrNniDlciSpParmsEntry_Object = MibTableRow
mscFrNniDlciSpParmsEntry = _MscFrNniDlciSpParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1)
)
mscFrNniDlciSpParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciSpParmsEntry.setStatus("mandatory")


class _MscFrNniDlciSpMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrNniDlciSpMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrNniDlciSpMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciSpMaximumFrameSize_Object = MibTableColumn
mscFrNniDlciSpMaximumFrameSize = _MscFrNniDlciSpMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 1),
    _MscFrNniDlciSpMaximumFrameSize_Type()
)
mscFrNniDlciSpMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpMaximumFrameSize.setStatus("mandatory")


class _MscFrNniDlciSpRateEnforcement_Type(Integer32):
    """Custom type mscFrNniDlciSpRateEnforcement based on Integer32"""
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


_MscFrNniDlciSpRateEnforcement_Type.__name__ = "Integer32"
_MscFrNniDlciSpRateEnforcement_Object = MibTableColumn
mscFrNniDlciSpRateEnforcement = _MscFrNniDlciSpRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 2),
    _MscFrNniDlciSpRateEnforcement_Type()
)
mscFrNniDlciSpRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpRateEnforcement.setStatus("mandatory")


class _MscFrNniDlciSpCommittedInformationRate_Type(Gauge32):
    """Custom type mscFrNniDlciSpCommittedInformationRate based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrNniDlciSpCommittedInformationRate_Type.__name__ = "Gauge32"
_MscFrNniDlciSpCommittedInformationRate_Object = MibTableColumn
mscFrNniDlciSpCommittedInformationRate = _MscFrNniDlciSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 3),
    _MscFrNniDlciSpCommittedInformationRate_Type()
)
mscFrNniDlciSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpCommittedInformationRate.setStatus("mandatory")


class _MscFrNniDlciSpCommittedBurstSize_Type(Gauge32):
    """Custom type mscFrNniDlciSpCommittedBurstSize based on Gauge32"""
    defaultValue = 64000

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrNniDlciSpCommittedBurstSize_Type.__name__ = "Gauge32"
_MscFrNniDlciSpCommittedBurstSize_Object = MibTableColumn
mscFrNniDlciSpCommittedBurstSize = _MscFrNniDlciSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 4),
    _MscFrNniDlciSpCommittedBurstSize_Type()
)
mscFrNniDlciSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpCommittedBurstSize.setStatus("mandatory")


class _MscFrNniDlciSpExcessBurstSize_Type(Gauge32):
    """Custom type mscFrNniDlciSpExcessBurstSize based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
    )


_MscFrNniDlciSpExcessBurstSize_Type.__name__ = "Gauge32"
_MscFrNniDlciSpExcessBurstSize_Object = MibTableColumn
mscFrNniDlciSpExcessBurstSize = _MscFrNniDlciSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 5),
    _MscFrNniDlciSpExcessBurstSize_Type()
)
mscFrNniDlciSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpExcessBurstSize.setStatus("mandatory")


class _MscFrNniDlciSpMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrNniDlciSpMeasurementInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
    )


_MscFrNniDlciSpMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrNniDlciSpMeasurementInterval_Object = MibTableColumn
mscFrNniDlciSpMeasurementInterval = _MscFrNniDlciSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 6),
    _MscFrNniDlciSpMeasurementInterval_Type()
)
mscFrNniDlciSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpMeasurementInterval.setStatus("mandatory")


class _MscFrNniDlciSpRateAdaptation_Type(Integer32):
    """Custom type mscFrNniDlciSpRateAdaptation based on Integer32"""
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


_MscFrNniDlciSpRateAdaptation_Type.__name__ = "Integer32"
_MscFrNniDlciSpRateAdaptation_Object = MibTableColumn
mscFrNniDlciSpRateAdaptation = _MscFrNniDlciSpRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 7),
    _MscFrNniDlciSpRateAdaptation_Type()
)
mscFrNniDlciSpRateAdaptation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpRateAdaptation.setStatus("mandatory")


class _MscFrNniDlciSpAccounting_Type(Integer32):
    """Custom type mscFrNniDlciSpAccounting based on Integer32"""
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


_MscFrNniDlciSpAccounting_Type.__name__ = "Integer32"
_MscFrNniDlciSpAccounting_Object = MibTableColumn
mscFrNniDlciSpAccounting = _MscFrNniDlciSpAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 8),
    _MscFrNniDlciSpAccounting_Type()
)
mscFrNniDlciSpAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpAccounting.setStatus("mandatory")


class _MscFrNniDlciSpRaSensitivity_Type(Unsigned32):
    """Custom type mscFrNniDlciSpRaSensitivity based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscFrNniDlciSpRaSensitivity_Type.__name__ = "Unsigned32"
_MscFrNniDlciSpRaSensitivity_Object = MibTableColumn
mscFrNniDlciSpRaSensitivity = _MscFrNniDlciSpRaSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 9),
    _MscFrNniDlciSpRaSensitivity_Type()
)
mscFrNniDlciSpRaSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpRaSensitivity.setStatus("mandatory")


class _MscFrNniDlciSpUpdateBCI_Type(Integer32):
    """Custom type mscFrNniDlciSpUpdateBCI based on Integer32"""
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


_MscFrNniDlciSpUpdateBCI_Type.__name__ = "Integer32"
_MscFrNniDlciSpUpdateBCI_Object = MibTableColumn
mscFrNniDlciSpUpdateBCI = _MscFrNniDlciSpUpdateBCI_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 4, 11, 1, 10),
    _MscFrNniDlciSpUpdateBCI_Type()
)
mscFrNniDlciSpUpdateBCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciSpUpdateBCI.setStatus("mandatory")
_MscFrNniDlciLb_ObjectIdentity = ObjectIdentity
mscFrNniDlciLb = _MscFrNniDlciLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5)
)
_MscFrNniDlciLbRowStatusTable_Object = MibTable
mscFrNniDlciLbRowStatusTable = _MscFrNniDlciLbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDlciLbRowStatusTable.setStatus("mandatory")
_MscFrNniDlciLbRowStatusEntry_Object = MibTableRow
mscFrNniDlciLbRowStatusEntry = _MscFrNniDlciLbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 1, 1)
)
mscFrNniDlciLbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciLbRowStatusEntry.setStatus("mandatory")
_MscFrNniDlciLbRowStatus_Type = RowStatus
_MscFrNniDlciLbRowStatus_Object = MibTableColumn
mscFrNniDlciLbRowStatus = _MscFrNniDlciLbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 1, 1, 1),
    _MscFrNniDlciLbRowStatus_Type()
)
mscFrNniDlciLbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbRowStatus.setStatus("mandatory")
_MscFrNniDlciLbComponentName_Type = DisplayString
_MscFrNniDlciLbComponentName_Object = MibTableColumn
mscFrNniDlciLbComponentName = _MscFrNniDlciLbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 1, 1, 2),
    _MscFrNniDlciLbComponentName_Type()
)
mscFrNniDlciLbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbComponentName.setStatus("mandatory")
_MscFrNniDlciLbStorageType_Type = StorageType
_MscFrNniDlciLbStorageType_Object = MibTableColumn
mscFrNniDlciLbStorageType = _MscFrNniDlciLbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 1, 1, 4),
    _MscFrNniDlciLbStorageType_Type()
)
mscFrNniDlciLbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbStorageType.setStatus("mandatory")
_MscFrNniDlciLbIndex_Type = NonReplicated
_MscFrNniDlciLbIndex_Object = MibTableColumn
mscFrNniDlciLbIndex = _MscFrNniDlciLbIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 1, 1, 10),
    _MscFrNniDlciLbIndex_Type()
)
mscFrNniDlciLbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDlciLbIndex.setStatus("mandatory")
_MscFrNniDlciLbStatsTable_Object = MibTable
mscFrNniDlciLbStatsTable = _MscFrNniDlciLbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDlciLbStatsTable.setStatus("mandatory")
_MscFrNniDlciLbStatsEntry_Object = MibTableRow
mscFrNniDlciLbStatsEntry = _MscFrNniDlciLbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1)
)
mscFrNniDlciLbStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciLbIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciLbStatsEntry.setStatus("mandatory")


class _MscFrNniDlciLbLocalTotalFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbLocalTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbLocalTotalFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbLocalTotalFrm_Object = MibTableColumn
mscFrNniDlciLbLocalTotalFrm = _MscFrNniDlciLbLocalTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 1),
    _MscFrNniDlciLbLocalTotalFrm_Type()
)
mscFrNniDlciLbLocalTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbLocalTotalFrm.setStatus("mandatory")


class _MscFrNniDlciLbLocalTotalBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciLbLocalTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbLocalTotalBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbLocalTotalBytes_Object = MibTableColumn
mscFrNniDlciLbLocalTotalBytes = _MscFrNniDlciLbLocalTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 2),
    _MscFrNniDlciLbLocalTotalBytes_Type()
)
mscFrNniDlciLbLocalTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbLocalTotalBytes.setStatus("mandatory")


class _MscFrNniDlciLbLocalFecnFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbLocalFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbLocalFecnFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbLocalFecnFrm_Object = MibTableColumn
mscFrNniDlciLbLocalFecnFrm = _MscFrNniDlciLbLocalFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 3),
    _MscFrNniDlciLbLocalFecnFrm_Type()
)
mscFrNniDlciLbLocalFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbLocalFecnFrm.setStatus("mandatory")


class _MscFrNniDlciLbLocalBecnFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbLocalBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbLocalBecnFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbLocalBecnFrm_Object = MibTableColumn
mscFrNniDlciLbLocalBecnFrm = _MscFrNniDlciLbLocalBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 4),
    _MscFrNniDlciLbLocalBecnFrm_Type()
)
mscFrNniDlciLbLocalBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbLocalBecnFrm.setStatus("mandatory")


class _MscFrNniDlciLbLocalDeFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbLocalDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbLocalDeFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbLocalDeFrm_Object = MibTableColumn
mscFrNniDlciLbLocalDeFrm = _MscFrNniDlciLbLocalDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 5),
    _MscFrNniDlciLbLocalDeFrm_Type()
)
mscFrNniDlciLbLocalDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbLocalDeFrm.setStatus("mandatory")


class _MscFrNniDlciLbLocalDeBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciLbLocalDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbLocalDeBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbLocalDeBytes_Object = MibTableColumn
mscFrNniDlciLbLocalDeBytes = _MscFrNniDlciLbLocalDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 6),
    _MscFrNniDlciLbLocalDeBytes_Type()
)
mscFrNniDlciLbLocalDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbLocalDeBytes.setStatus("mandatory")


class _MscFrNniDlciLbRemoteTotalFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbRemoteTotalFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbRemoteTotalFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbRemoteTotalFrm_Object = MibTableColumn
mscFrNniDlciLbRemoteTotalFrm = _MscFrNniDlciLbRemoteTotalFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 7),
    _MscFrNniDlciLbRemoteTotalFrm_Type()
)
mscFrNniDlciLbRemoteTotalFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbRemoteTotalFrm.setStatus("mandatory")


class _MscFrNniDlciLbRemoteTotalBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciLbRemoteTotalBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbRemoteTotalBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbRemoteTotalBytes_Object = MibTableColumn
mscFrNniDlciLbRemoteTotalBytes = _MscFrNniDlciLbRemoteTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 8),
    _MscFrNniDlciLbRemoteTotalBytes_Type()
)
mscFrNniDlciLbRemoteTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbRemoteTotalBytes.setStatus("mandatory")


class _MscFrNniDlciLbRemoteFecnFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbRemoteFecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbRemoteFecnFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbRemoteFecnFrm_Object = MibTableColumn
mscFrNniDlciLbRemoteFecnFrm = _MscFrNniDlciLbRemoteFecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 9),
    _MscFrNniDlciLbRemoteFecnFrm_Type()
)
mscFrNniDlciLbRemoteFecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbRemoteFecnFrm.setStatus("mandatory")


class _MscFrNniDlciLbRemoteBecnFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbRemoteBecnFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbRemoteBecnFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbRemoteBecnFrm_Object = MibTableColumn
mscFrNniDlciLbRemoteBecnFrm = _MscFrNniDlciLbRemoteBecnFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 10),
    _MscFrNniDlciLbRemoteBecnFrm_Type()
)
mscFrNniDlciLbRemoteBecnFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbRemoteBecnFrm.setStatus("mandatory")


class _MscFrNniDlciLbRemoteDeFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciLbRemoteDeFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbRemoteDeFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbRemoteDeFrm_Object = MibTableColumn
mscFrNniDlciLbRemoteDeFrm = _MscFrNniDlciLbRemoteDeFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 13),
    _MscFrNniDlciLbRemoteDeFrm_Type()
)
mscFrNniDlciLbRemoteDeFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbRemoteDeFrm.setStatus("mandatory")


class _MscFrNniDlciLbRemoteDeBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciLbRemoteDeBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciLbRemoteDeBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciLbRemoteDeBytes_Object = MibTableColumn
mscFrNniDlciLbRemoteDeBytes = _MscFrNniDlciLbRemoteDeBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 5, 10, 1, 14),
    _MscFrNniDlciLbRemoteDeBytes_Type()
)
mscFrNniDlciLbRemoteDeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLbRemoteDeBytes.setStatus("mandatory")
_MscFrNniDlciEgressSp_ObjectIdentity = ObjectIdentity
mscFrNniDlciEgressSp = _MscFrNniDlciEgressSp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6)
)
_MscFrNniDlciEgressSpRowStatusTable_Object = MibTable
mscFrNniDlciEgressSpRowStatusTable = _MscFrNniDlciEgressSpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpRowStatusTable.setStatus("mandatory")
_MscFrNniDlciEgressSpRowStatusEntry_Object = MibTableRow
mscFrNniDlciEgressSpRowStatusEntry = _MscFrNniDlciEgressSpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 1, 1)
)
mscFrNniDlciEgressSpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciEgressSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpRowStatusEntry.setStatus("mandatory")
_MscFrNniDlciEgressSpRowStatus_Type = RowStatus
_MscFrNniDlciEgressSpRowStatus_Object = MibTableColumn
mscFrNniDlciEgressSpRowStatus = _MscFrNniDlciEgressSpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 1, 1, 1),
    _MscFrNniDlciEgressSpRowStatus_Type()
)
mscFrNniDlciEgressSpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpRowStatus.setStatus("mandatory")
_MscFrNniDlciEgressSpComponentName_Type = DisplayString
_MscFrNniDlciEgressSpComponentName_Object = MibTableColumn
mscFrNniDlciEgressSpComponentName = _MscFrNniDlciEgressSpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 1, 1, 2),
    _MscFrNniDlciEgressSpComponentName_Type()
)
mscFrNniDlciEgressSpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpComponentName.setStatus("mandatory")
_MscFrNniDlciEgressSpStorageType_Type = StorageType
_MscFrNniDlciEgressSpStorageType_Object = MibTableColumn
mscFrNniDlciEgressSpStorageType = _MscFrNniDlciEgressSpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 1, 1, 4),
    _MscFrNniDlciEgressSpStorageType_Type()
)
mscFrNniDlciEgressSpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpStorageType.setStatus("mandatory")
_MscFrNniDlciEgressSpIndex_Type = NonReplicated
_MscFrNniDlciEgressSpIndex_Object = MibTableColumn
mscFrNniDlciEgressSpIndex = _MscFrNniDlciEgressSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 1, 1, 10),
    _MscFrNniDlciEgressSpIndex_Type()
)
mscFrNniDlciEgressSpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpIndex.setStatus("mandatory")
_MscFrNniDlciEgressSpProvTable_Object = MibTable
mscFrNniDlciEgressSpProvTable = _MscFrNniDlciEgressSpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpProvTable.setStatus("mandatory")
_MscFrNniDlciEgressSpProvEntry_Object = MibTableRow
mscFrNniDlciEgressSpProvEntry = _MscFrNniDlciEgressSpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 10, 1)
)
mscFrNniDlciEgressSpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciEgressSpIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpProvEntry.setStatus("mandatory")


class _MscFrNniDlciEgressSpCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrNniDlciEgressSpCommittedInformationRate based on Unsigned32"""
    defaultValue = 50000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
        ValueRangeConstraint(50000001, 50000001),
    )


_MscFrNniDlciEgressSpCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrNniDlciEgressSpCommittedInformationRate_Object = MibTableColumn
mscFrNniDlciEgressSpCommittedInformationRate = _MscFrNniDlciEgressSpCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 10, 1, 1),
    _MscFrNniDlciEgressSpCommittedInformationRate_Type()
)
mscFrNniDlciEgressSpCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpCommittedInformationRate.setStatus("mandatory")


class _MscFrNniDlciEgressSpCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrNniDlciEgressSpCommittedBurstSize based on Unsigned32"""
    defaultValue = 50000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
        ValueRangeConstraint(50000001, 50000001),
    )


_MscFrNniDlciEgressSpCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciEgressSpCommittedBurstSize_Object = MibTableColumn
mscFrNniDlciEgressSpCommittedBurstSize = _MscFrNniDlciEgressSpCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 10, 1, 2),
    _MscFrNniDlciEgressSpCommittedBurstSize_Type()
)
mscFrNniDlciEgressSpCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpCommittedBurstSize.setStatus("mandatory")


class _MscFrNniDlciEgressSpExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrNniDlciEgressSpExcessBurstSize based on Unsigned32"""
    defaultValue = 50000001

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000000),
        ValueRangeConstraint(50000001, 50000001),
    )


_MscFrNniDlciEgressSpExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciEgressSpExcessBurstSize_Object = MibTableColumn
mscFrNniDlciEgressSpExcessBurstSize = _MscFrNniDlciEgressSpExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 10, 1, 3),
    _MscFrNniDlciEgressSpExcessBurstSize_Type()
)
mscFrNniDlciEgressSpExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpExcessBurstSize.setStatus("mandatory")


class _MscFrNniDlciEgressSpMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrNniDlciEgressSpMeasurementInterval based on Unsigned32"""
    defaultValue = 25501

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25500),
        ValueRangeConstraint(25501, 25501),
    )


_MscFrNniDlciEgressSpMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrNniDlciEgressSpMeasurementInterval_Object = MibTableColumn
mscFrNniDlciEgressSpMeasurementInterval = _MscFrNniDlciEgressSpMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 6, 10, 1, 4),
    _MscFrNniDlciEgressSpMeasurementInterval_Type()
)
mscFrNniDlciEgressSpMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniDlciEgressSpMeasurementInterval.setStatus("mandatory")
_MscFrNniDlciStateTable_Object = MibTable
mscFrNniDlciStateTable = _MscFrNniDlciStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10)
)
if mibBuilder.loadTexts:
    mscFrNniDlciStateTable.setStatus("mandatory")
_MscFrNniDlciStateEntry_Object = MibTableRow
mscFrNniDlciStateEntry = _MscFrNniDlciStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1)
)
mscFrNniDlciStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciStateEntry.setStatus("mandatory")


class _MscFrNniDlciAdminState_Type(Integer32):
    """Custom type mscFrNniDlciAdminState based on Integer32"""
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


_MscFrNniDlciAdminState_Type.__name__ = "Integer32"
_MscFrNniDlciAdminState_Object = MibTableColumn
mscFrNniDlciAdminState = _MscFrNniDlciAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 1),
    _MscFrNniDlciAdminState_Type()
)
mscFrNniDlciAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciAdminState.setStatus("mandatory")


class _MscFrNniDlciOperationalState_Type(Integer32):
    """Custom type mscFrNniDlciOperationalState based on Integer32"""
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


_MscFrNniDlciOperationalState_Type.__name__ = "Integer32"
_MscFrNniDlciOperationalState_Object = MibTableColumn
mscFrNniDlciOperationalState = _MscFrNniDlciOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 2),
    _MscFrNniDlciOperationalState_Type()
)
mscFrNniDlciOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciOperationalState.setStatus("mandatory")


class _MscFrNniDlciUsageState_Type(Integer32):
    """Custom type mscFrNniDlciUsageState based on Integer32"""
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


_MscFrNniDlciUsageState_Type.__name__ = "Integer32"
_MscFrNniDlciUsageState_Object = MibTableColumn
mscFrNniDlciUsageState = _MscFrNniDlciUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 3),
    _MscFrNniDlciUsageState_Type()
)
mscFrNniDlciUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciUsageState.setStatus("mandatory")


class _MscFrNniDlciAvailabilityStatus_Type(OctetString):
    """Custom type mscFrNniDlciAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFrNniDlciAvailabilityStatus_Type.__name__ = "OctetString"
_MscFrNniDlciAvailabilityStatus_Object = MibTableColumn
mscFrNniDlciAvailabilityStatus = _MscFrNniDlciAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 4),
    _MscFrNniDlciAvailabilityStatus_Type()
)
mscFrNniDlciAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciAvailabilityStatus.setStatus("mandatory")


class _MscFrNniDlciProceduralStatus_Type(OctetString):
    """Custom type mscFrNniDlciProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniDlciProceduralStatus_Type.__name__ = "OctetString"
_MscFrNniDlciProceduralStatus_Object = MibTableColumn
mscFrNniDlciProceduralStatus = _MscFrNniDlciProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 5),
    _MscFrNniDlciProceduralStatus_Type()
)
mscFrNniDlciProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciProceduralStatus.setStatus("mandatory")


class _MscFrNniDlciControlStatus_Type(OctetString):
    """Custom type mscFrNniDlciControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniDlciControlStatus_Type.__name__ = "OctetString"
_MscFrNniDlciControlStatus_Object = MibTableColumn
mscFrNniDlciControlStatus = _MscFrNniDlciControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 6),
    _MscFrNniDlciControlStatus_Type()
)
mscFrNniDlciControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciControlStatus.setStatus("mandatory")


class _MscFrNniDlciAlarmStatus_Type(OctetString):
    """Custom type mscFrNniDlciAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniDlciAlarmStatus_Type.__name__ = "OctetString"
_MscFrNniDlciAlarmStatus_Object = MibTableColumn
mscFrNniDlciAlarmStatus = _MscFrNniDlciAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 7),
    _MscFrNniDlciAlarmStatus_Type()
)
mscFrNniDlciAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciAlarmStatus.setStatus("mandatory")


class _MscFrNniDlciStandbyStatus_Type(Integer32):
    """Custom type mscFrNniDlciStandbyStatus based on Integer32"""
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


_MscFrNniDlciStandbyStatus_Type.__name__ = "Integer32"
_MscFrNniDlciStandbyStatus_Object = MibTableColumn
mscFrNniDlciStandbyStatus = _MscFrNniDlciStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 8),
    _MscFrNniDlciStandbyStatus_Type()
)
mscFrNniDlciStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciStandbyStatus.setStatus("mandatory")


class _MscFrNniDlciUnknownStatus_Type(Integer32):
    """Custom type mscFrNniDlciUnknownStatus based on Integer32"""
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


_MscFrNniDlciUnknownStatus_Type.__name__ = "Integer32"
_MscFrNniDlciUnknownStatus_Object = MibTableColumn
mscFrNniDlciUnknownStatus = _MscFrNniDlciUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 10, 1, 9),
    _MscFrNniDlciUnknownStatus_Type()
)
mscFrNniDlciUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciUnknownStatus.setStatus("mandatory")
_MscFrNniDlciAbitTable_Object = MibTable
mscFrNniDlciAbitTable = _MscFrNniDlciAbitTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 12)
)
if mibBuilder.loadTexts:
    mscFrNniDlciAbitTable.setStatus("mandatory")
_MscFrNniDlciAbitEntry_Object = MibTableRow
mscFrNniDlciAbitEntry = _MscFrNniDlciAbitEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 12, 1)
)
mscFrNniDlciAbitEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciAbitEntry.setStatus("mandatory")


class _MscFrNniDlciABitStatusToIf_Type(Integer32):
    """Custom type mscFrNniDlciABitStatusToIf based on Integer32"""
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


_MscFrNniDlciABitStatusToIf_Type.__name__ = "Integer32"
_MscFrNniDlciABitStatusToIf_Object = MibTableColumn
mscFrNniDlciABitStatusToIf = _MscFrNniDlciABitStatusToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 12, 1, 1),
    _MscFrNniDlciABitStatusToIf_Type()
)
mscFrNniDlciABitStatusToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciABitStatusToIf.setStatus("mandatory")


class _MscFrNniDlciABitReasonToIf_Type(Integer32):
    """Custom type mscFrNniDlciABitReasonToIf based on Integer32"""
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


_MscFrNniDlciABitReasonToIf_Type.__name__ = "Integer32"
_MscFrNniDlciABitReasonToIf_Object = MibTableColumn
mscFrNniDlciABitReasonToIf = _MscFrNniDlciABitReasonToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 12, 1, 2),
    _MscFrNniDlciABitReasonToIf_Type()
)
mscFrNniDlciABitReasonToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciABitReasonToIf.setStatus("mandatory")


class _MscFrNniDlciABitStatusFromIf_Type(Integer32):
    """Custom type mscFrNniDlciABitStatusFromIf based on Integer32"""
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


_MscFrNniDlciABitStatusFromIf_Type.__name__ = "Integer32"
_MscFrNniDlciABitStatusFromIf_Object = MibTableColumn
mscFrNniDlciABitStatusFromIf = _MscFrNniDlciABitStatusFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 12, 1, 3),
    _MscFrNniDlciABitStatusFromIf_Type()
)
mscFrNniDlciABitStatusFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciABitStatusFromIf.setStatus("mandatory")


class _MscFrNniDlciABitReasonFromIf_Type(Integer32):
    """Custom type mscFrNniDlciABitReasonFromIf based on Integer32"""
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


_MscFrNniDlciABitReasonFromIf_Type.__name__ = "Integer32"
_MscFrNniDlciABitReasonFromIf_Object = MibTableColumn
mscFrNniDlciABitReasonFromIf = _MscFrNniDlciABitReasonFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 12, 1, 4),
    _MscFrNniDlciABitReasonFromIf_Type()
)
mscFrNniDlciABitReasonFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciABitReasonFromIf.setStatus("mandatory")


class _MscFrNniDlciLoopbackState_Type(Integer32):
    """Custom type mscFrNniDlciLoopbackState based on Integer32"""
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


_MscFrNniDlciLoopbackState_Type.__name__ = "Integer32"
_MscFrNniDlciLoopbackState_Object = MibTableColumn
mscFrNniDlciLoopbackState = _MscFrNniDlciLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 12, 1, 5),
    _MscFrNniDlciLoopbackState_Type()
)
mscFrNniDlciLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLoopbackState.setStatus("mandatory")
_MscFrNniDlciSpOpTable_Object = MibTable
mscFrNniDlciSpOpTable = _MscFrNniDlciSpOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13)
)
if mibBuilder.loadTexts:
    mscFrNniDlciSpOpTable.setStatus("mandatory")
_MscFrNniDlciSpOpEntry_Object = MibTableRow
mscFrNniDlciSpOpEntry = _MscFrNniDlciSpOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1)
)
mscFrNniDlciSpOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciSpOpEntry.setStatus("mandatory")


class _MscFrNniDlciMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrNniDlciMaximumFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrNniDlciMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciMaximumFrameSize_Object = MibTableColumn
mscFrNniDlciMaximumFrameSize = _MscFrNniDlciMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 1),
    _MscFrNniDlciMaximumFrameSize_Type()
)
mscFrNniDlciMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciMaximumFrameSize.setStatus("mandatory")


class _MscFrNniDlciRateEnforcement_Type(Integer32):
    """Custom type mscFrNniDlciRateEnforcement based on Integer32"""
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


_MscFrNniDlciRateEnforcement_Type.__name__ = "Integer32"
_MscFrNniDlciRateEnforcement_Object = MibTableColumn
mscFrNniDlciRateEnforcement = _MscFrNniDlciRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 2),
    _MscFrNniDlciRateEnforcement_Type()
)
mscFrNniDlciRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciRateEnforcement.setStatus("obsolete")


class _MscFrNniDlciCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrNniDlciCommittedInformationRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrNniDlciCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrNniDlciCommittedInformationRate_Object = MibTableColumn
mscFrNniDlciCommittedInformationRate = _MscFrNniDlciCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 3),
    _MscFrNniDlciCommittedInformationRate_Type()
)
mscFrNniDlciCommittedInformationRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCommittedInformationRate.setStatus("mandatory")


class _MscFrNniDlciCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrNniDlciCommittedBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrNniDlciCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciCommittedBurstSize_Object = MibTableColumn
mscFrNniDlciCommittedBurstSize = _MscFrNniDlciCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 4),
    _MscFrNniDlciCommittedBurstSize_Type()
)
mscFrNniDlciCommittedBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCommittedBurstSize.setStatus("mandatory")


class _MscFrNniDlciExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrNniDlciExcessBurstSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_MscFrNniDlciExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrNniDlciExcessBurstSize_Object = MibTableColumn
mscFrNniDlciExcessBurstSize = _MscFrNniDlciExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 5),
    _MscFrNniDlciExcessBurstSize_Type()
)
mscFrNniDlciExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciExcessBurstSize.setStatus("mandatory")


class _MscFrNniDlciMeasurementInterval_Type(Unsigned32):
    """Custom type mscFrNniDlciMeasurementInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciMeasurementInterval_Type.__name__ = "Unsigned32"
_MscFrNniDlciMeasurementInterval_Object = MibTableColumn
mscFrNniDlciMeasurementInterval = _MscFrNniDlciMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 6),
    _MscFrNniDlciMeasurementInterval_Type()
)
mscFrNniDlciMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciMeasurementInterval.setStatus("mandatory")


class _MscFrNniDlciRateAdaptation_Type(Integer32):
    """Custom type mscFrNniDlciRateAdaptation based on Integer32"""
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


_MscFrNniDlciRateAdaptation_Type.__name__ = "Integer32"
_MscFrNniDlciRateAdaptation_Object = MibTableColumn
mscFrNniDlciRateAdaptation = _MscFrNniDlciRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 7),
    _MscFrNniDlciRateAdaptation_Type()
)
mscFrNniDlciRateAdaptation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciRateAdaptation.setStatus("obsolete")


class _MscFrNniDlciAccounting_Type(Integer32):
    """Custom type mscFrNniDlciAccounting based on Integer32"""
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


_MscFrNniDlciAccounting_Type.__name__ = "Integer32"
_MscFrNniDlciAccounting_Object = MibTableColumn
mscFrNniDlciAccounting = _MscFrNniDlciAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 8),
    _MscFrNniDlciAccounting_Type()
)
mscFrNniDlciAccounting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciAccounting.setStatus("mandatory")


class _MscFrNniDlciEmissionPriorityToIf_Type(Integer32):
    """Custom type mscFrNniDlciEmissionPriorityToIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_MscFrNniDlciEmissionPriorityToIf_Type.__name__ = "Integer32"
_MscFrNniDlciEmissionPriorityToIf_Object = MibTableColumn
mscFrNniDlciEmissionPriorityToIf = _MscFrNniDlciEmissionPriorityToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 9),
    _MscFrNniDlciEmissionPriorityToIf_Type()
)
mscFrNniDlciEmissionPriorityToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEmissionPriorityToIf.setStatus("mandatory")


class _MscFrNniDlciTransferPriToNwk_Type(Unsigned32):
    """Custom type mscFrNniDlciTransferPriToNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniDlciTransferPriToNwk_Type.__name__ = "Unsigned32"
_MscFrNniDlciTransferPriToNwk_Object = MibTableColumn
mscFrNniDlciTransferPriToNwk = _MscFrNniDlciTransferPriToNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 10),
    _MscFrNniDlciTransferPriToNwk_Type()
)
mscFrNniDlciTransferPriToNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTransferPriToNwk.setStatus("mandatory")


class _MscFrNniDlciTransferPriFromNwk_Type(Unsigned32):
    """Custom type mscFrNniDlciTransferPriFromNwk based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniDlciTransferPriFromNwk_Type.__name__ = "Unsigned32"
_MscFrNniDlciTransferPriFromNwk_Object = MibTableColumn
mscFrNniDlciTransferPriFromNwk = _MscFrNniDlciTransferPriFromNwk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 13, 1, 11),
    _MscFrNniDlciTransferPriFromNwk_Type()
)
mscFrNniDlciTransferPriFromNwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTransferPriFromNwk.setStatus("mandatory")
_MscFrNniDlciStatsTable_Object = MibTable
mscFrNniDlciStatsTable = _MscFrNniDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14)
)
if mibBuilder.loadTexts:
    mscFrNniDlciStatsTable.setStatus("mandatory")
_MscFrNniDlciStatsEntry_Object = MibTableRow
mscFrNniDlciStatsEntry = _MscFrNniDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1)
)
mscFrNniDlciStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciStatsEntry.setStatus("mandatory")


class _MscFrNniDlciFrmToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciFrmToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciFrmToIf_Object = MibTableColumn
mscFrNniDlciFrmToIf = _MscFrNniDlciFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 1),
    _MscFrNniDlciFrmToIf_Type()
)
mscFrNniDlciFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciFrmToIf.setStatus("mandatory")


class _MscFrNniDlciFecnFrmToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciFecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciFecnFrmToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciFecnFrmToIf_Object = MibTableColumn
mscFrNniDlciFecnFrmToIf = _MscFrNniDlciFecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 2),
    _MscFrNniDlciFecnFrmToIf_Type()
)
mscFrNniDlciFecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciFecnFrmToIf.setStatus("mandatory")


class _MscFrNniDlciBecnFrmToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciBecnFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciBecnFrmToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciBecnFrmToIf_Object = MibTableColumn
mscFrNniDlciBecnFrmToIf = _MscFrNniDlciBecnFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 3),
    _MscFrNniDlciBecnFrmToIf_Type()
)
mscFrNniDlciBecnFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciBecnFrmToIf.setStatus("mandatory")


class _MscFrNniDlciBciToSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciBciToSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciBciToSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciBciToSubnet_Object = MibTableColumn
mscFrNniDlciBciToSubnet = _MscFrNniDlciBciToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 4),
    _MscFrNniDlciBciToSubnet_Type()
)
mscFrNniDlciBciToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciBciToSubnet.setStatus("mandatory")


class _MscFrNniDlciDeFrmToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDeFrmToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDeFrmToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDeFrmToIf_Object = MibTableColumn
mscFrNniDlciDeFrmToIf = _MscFrNniDlciDeFrmToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 5),
    _MscFrNniDlciDeFrmToIf_Type()
)
mscFrNniDlciDeFrmToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDeFrmToIf.setStatus("mandatory")


class _MscFrNniDlciDiscCongestedToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscCongestedToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscCongestedToIf_Object = MibTableColumn
mscFrNniDlciDiscCongestedToIf = _MscFrNniDlciDiscCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 6),
    _MscFrNniDlciDiscCongestedToIf_Type()
)
mscFrNniDlciDiscCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscCongestedToIf.setStatus("mandatory")


class _MscFrNniDlciDiscDeCongestedToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscDeCongestedToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscDeCongestedToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscDeCongestedToIf_Object = MibTableColumn
mscFrNniDlciDiscDeCongestedToIf = _MscFrNniDlciDiscDeCongestedToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 7),
    _MscFrNniDlciDiscDeCongestedToIf_Type()
)
mscFrNniDlciDiscDeCongestedToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscDeCongestedToIf.setStatus("mandatory")


class _MscFrNniDlciFrmFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciFrmFromIf_Object = MibTableColumn
mscFrNniDlciFrmFromIf = _MscFrNniDlciFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 8),
    _MscFrNniDlciFrmFromIf_Type()
)
mscFrNniDlciFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciFrmFromIf.setStatus("mandatory")


class _MscFrNniDlciFecnFrmFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciFecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciFecnFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciFecnFrmFromIf_Object = MibTableColumn
mscFrNniDlciFecnFrmFromIf = _MscFrNniDlciFecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 9),
    _MscFrNniDlciFecnFrmFromIf_Type()
)
mscFrNniDlciFecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciFecnFrmFromIf.setStatus("mandatory")


class _MscFrNniDlciBecnFrmFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciBecnFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciBecnFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciBecnFrmFromIf_Object = MibTableColumn
mscFrNniDlciBecnFrmFromIf = _MscFrNniDlciBecnFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 10),
    _MscFrNniDlciBecnFrmFromIf_Type()
)
mscFrNniDlciBecnFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciBecnFrmFromIf.setStatus("mandatory")


class _MscFrNniDlciFciFromSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciFciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciFciFromSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciFciFromSubnet_Object = MibTableColumn
mscFrNniDlciFciFromSubnet = _MscFrNniDlciFciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 11),
    _MscFrNniDlciFciFromSubnet_Type()
)
mscFrNniDlciFciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciFciFromSubnet.setStatus("mandatory")


class _MscFrNniDlciBciFromSubnet_Type(Unsigned32):
    """Custom type mscFrNniDlciBciFromSubnet based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciBciFromSubnet_Type.__name__ = "Unsigned32"
_MscFrNniDlciBciFromSubnet_Object = MibTableColumn
mscFrNniDlciBciFromSubnet = _MscFrNniDlciBciFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 12),
    _MscFrNniDlciBciFromSubnet_Type()
)
mscFrNniDlciBciFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciBciFromSubnet.setStatus("mandatory")


class _MscFrNniDlciDeFrmFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDeFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDeFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDeFrmFromIf_Object = MibTableColumn
mscFrNniDlciDeFrmFromIf = _MscFrNniDlciDeFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 13),
    _MscFrNniDlciDeFrmFromIf_Type()
)
mscFrNniDlciDeFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDeFrmFromIf.setStatus("mandatory")


class _MscFrNniDlciExcessFrmFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciExcessFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciExcessFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciExcessFrmFromIf_Object = MibTableColumn
mscFrNniDlciExcessFrmFromIf = _MscFrNniDlciExcessFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 14),
    _MscFrNniDlciExcessFrmFromIf_Type()
)
mscFrNniDlciExcessFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciExcessFrmFromIf.setStatus("mandatory")


class _MscFrNniDlciDiscExcessFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscExcessFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscExcessFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscExcessFromIf_Object = MibTableColumn
mscFrNniDlciDiscExcessFromIf = _MscFrNniDlciDiscExcessFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 15),
    _MscFrNniDlciDiscExcessFromIf_Type()
)
mscFrNniDlciDiscExcessFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscExcessFromIf.setStatus("mandatory")


class _MscFrNniDlciDiscFrameAbit_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscFrameAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscFrameAbit_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscFrameAbit_Object = MibTableColumn
mscFrNniDlciDiscFrameAbit = _MscFrNniDlciDiscFrameAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 16),
    _MscFrNniDlciDiscFrameAbit_Type()
)
mscFrNniDlciDiscFrameAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscFrameAbit.setStatus("mandatory")


class _MscFrNniDlciDiscCongestedFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscCongestedFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscCongestedFromIf_Object = MibTableColumn
mscFrNniDlciDiscCongestedFromIf = _MscFrNniDlciDiscCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 17),
    _MscFrNniDlciDiscCongestedFromIf_Type()
)
mscFrNniDlciDiscCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscCongestedFromIf.setStatus("mandatory")


class _MscFrNniDlciDiscDeCongestedFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscDeCongestedFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscDeCongestedFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscDeCongestedFromIf_Object = MibTableColumn
mscFrNniDlciDiscDeCongestedFromIf = _MscFrNniDlciDiscDeCongestedFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 18),
    _MscFrNniDlciDiscDeCongestedFromIf_Type()
)
mscFrNniDlciDiscDeCongestedFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscDeCongestedFromIf.setStatus("mandatory")


class _MscFrNniDlciErrorShortFrmFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciErrorShortFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciErrorShortFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciErrorShortFrmFromIf_Object = MibTableColumn
mscFrNniDlciErrorShortFrmFromIf = _MscFrNniDlciErrorShortFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 19),
    _MscFrNniDlciErrorShortFrmFromIf_Type()
)
mscFrNniDlciErrorShortFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciErrorShortFrmFromIf.setStatus("mandatory")


class _MscFrNniDlciErrorLongFrmFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciErrorLongFrmFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciErrorLongFrmFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciErrorLongFrmFromIf_Object = MibTableColumn
mscFrNniDlciErrorLongFrmFromIf = _MscFrNniDlciErrorLongFrmFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 20),
    _MscFrNniDlciErrorLongFrmFromIf_Type()
)
mscFrNniDlciErrorLongFrmFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciErrorLongFrmFromIf.setStatus("mandatory")


class _MscFrNniDlciBecnFrmSetByService_Type(Unsigned32):
    """Custom type mscFrNniDlciBecnFrmSetByService based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciBecnFrmSetByService_Type.__name__ = "Unsigned32"
_MscFrNniDlciBecnFrmSetByService_Object = MibTableColumn
mscFrNniDlciBecnFrmSetByService = _MscFrNniDlciBecnFrmSetByService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 21),
    _MscFrNniDlciBecnFrmSetByService_Type()
)
mscFrNniDlciBecnFrmSetByService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciBecnFrmSetByService.setStatus("mandatory")


class _MscFrNniDlciBytesToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciBytesToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciBytesToIf_Object = MibTableColumn
mscFrNniDlciBytesToIf = _MscFrNniDlciBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 22),
    _MscFrNniDlciBytesToIf_Type()
)
mscFrNniDlciBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciBytesToIf.setStatus("mandatory")


class _MscFrNniDlciDeBytesToIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDeBytesToIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDeBytesToIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDeBytesToIf_Object = MibTableColumn
mscFrNniDlciDeBytesToIf = _MscFrNniDlciDeBytesToIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 23),
    _MscFrNniDlciDeBytesToIf_Type()
)
mscFrNniDlciDeBytesToIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDeBytesToIf.setStatus("mandatory")


class _MscFrNniDlciDiscCongestedToIfBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscCongestedToIfBytes_Object = MibTableColumn
mscFrNniDlciDiscCongestedToIfBytes = _MscFrNniDlciDiscCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 24),
    _MscFrNniDlciDiscCongestedToIfBytes_Type()
)
mscFrNniDlciDiscCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscCongestedToIfBytes.setStatus("mandatory")


class _MscFrNniDlciDiscDeCongestedToIfBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscDeCongestedToIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscDeCongestedToIfBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscDeCongestedToIfBytes_Object = MibTableColumn
mscFrNniDlciDiscDeCongestedToIfBytes = _MscFrNniDlciDiscDeCongestedToIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 25),
    _MscFrNniDlciDiscDeCongestedToIfBytes_Type()
)
mscFrNniDlciDiscDeCongestedToIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscDeCongestedToIfBytes.setStatus("mandatory")


class _MscFrNniDlciBytesFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciBytesFromIf_Object = MibTableColumn
mscFrNniDlciBytesFromIf = _MscFrNniDlciBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 26),
    _MscFrNniDlciBytesFromIf_Type()
)
mscFrNniDlciBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciBytesFromIf.setStatus("mandatory")


class _MscFrNniDlciDeBytesFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciDeBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDeBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciDeBytesFromIf_Object = MibTableColumn
mscFrNniDlciDeBytesFromIf = _MscFrNniDlciDeBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 27),
    _MscFrNniDlciDeBytesFromIf_Type()
)
mscFrNniDlciDeBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDeBytesFromIf.setStatus("mandatory")


class _MscFrNniDlciExcessBytesFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciExcessBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciExcessBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciExcessBytesFromIf_Object = MibTableColumn
mscFrNniDlciExcessBytesFromIf = _MscFrNniDlciExcessBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 28),
    _MscFrNniDlciExcessBytesFromIf_Type()
)
mscFrNniDlciExcessBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciExcessBytesFromIf.setStatus("mandatory")


class _MscFrNniDlciDiscExcessFromIfBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscExcessFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscExcessFromIfBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscExcessFromIfBytes_Object = MibTableColumn
mscFrNniDlciDiscExcessFromIfBytes = _MscFrNniDlciDiscExcessFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 29),
    _MscFrNniDlciDiscExcessFromIfBytes_Type()
)
mscFrNniDlciDiscExcessFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscExcessFromIfBytes.setStatus("mandatory")


class _MscFrNniDlciDiscByteAbit_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscByteAbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscByteAbit_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscByteAbit_Object = MibTableColumn
mscFrNniDlciDiscByteAbit = _MscFrNniDlciDiscByteAbit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 30),
    _MscFrNniDlciDiscByteAbit_Type()
)
mscFrNniDlciDiscByteAbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscByteAbit.setStatus("mandatory")


class _MscFrNniDlciDiscCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscCongestedFromIfBytes_Object = MibTableColumn
mscFrNniDlciDiscCongestedFromIfBytes = _MscFrNniDlciDiscCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 31),
    _MscFrNniDlciDiscCongestedFromIfBytes_Type()
)
mscFrNniDlciDiscCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscCongestedFromIfBytes.setStatus("mandatory")


class _MscFrNniDlciDiscDeCongestedFromIfBytes_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscDeCongestedFromIfBytes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscDeCongestedFromIfBytes_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscDeCongestedFromIfBytes_Object = MibTableColumn
mscFrNniDlciDiscDeCongestedFromIfBytes = _MscFrNniDlciDiscDeCongestedFromIfBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 32),
    _MscFrNniDlciDiscDeCongestedFromIfBytes_Type()
)
mscFrNniDlciDiscDeCongestedFromIfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscDeCongestedFromIfBytes.setStatus("mandatory")


class _MscFrNniDlciErrorShortBytesFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciErrorShortBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciErrorShortBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciErrorShortBytesFromIf_Object = MibTableColumn
mscFrNniDlciErrorShortBytesFromIf = _MscFrNniDlciErrorShortBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 33),
    _MscFrNniDlciErrorShortBytesFromIf_Type()
)
mscFrNniDlciErrorShortBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciErrorShortBytesFromIf.setStatus("mandatory")


class _MscFrNniDlciErrorLongBytesFromIf_Type(Unsigned32):
    """Custom type mscFrNniDlciErrorLongBytesFromIf based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciErrorLongBytesFromIf_Type.__name__ = "Unsigned32"
_MscFrNniDlciErrorLongBytesFromIf_Object = MibTableColumn
mscFrNniDlciErrorLongBytesFromIf = _MscFrNniDlciErrorLongBytesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 34),
    _MscFrNniDlciErrorLongBytesFromIf_Type()
)
mscFrNniDlciErrorLongBytesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciErrorLongBytesFromIf.setStatus("mandatory")


class _MscFrNniDlciRateAdaptReduct_Type(Unsigned32):
    """Custom type mscFrNniDlciRateAdaptReduct based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciRateAdaptReduct_Type.__name__ = "Unsigned32"
_MscFrNniDlciRateAdaptReduct_Object = MibTableColumn
mscFrNniDlciRateAdaptReduct = _MscFrNniDlciRateAdaptReduct_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 35),
    _MscFrNniDlciRateAdaptReduct_Type()
)
mscFrNniDlciRateAdaptReduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciRateAdaptReduct.setStatus("mandatory")


class _MscFrNniDlciRateAdaptReductPeriod_Type(Unsigned32):
    """Custom type mscFrNniDlciRateAdaptReductPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciRateAdaptReductPeriod_Type.__name__ = "Unsigned32"
_MscFrNniDlciRateAdaptReductPeriod_Object = MibTableColumn
mscFrNniDlciRateAdaptReductPeriod = _MscFrNniDlciRateAdaptReductPeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 36),
    _MscFrNniDlciRateAdaptReductPeriod_Type()
)
mscFrNniDlciRateAdaptReductPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciRateAdaptReductPeriod.setStatus("mandatory")


class _MscFrNniDlciTransferPriorityToNetwork_Type(Integer32):
    """Custom type mscFrNniDlciTransferPriorityToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniDlciTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MscFrNniDlciTransferPriorityToNetwork_Object = MibTableColumn
mscFrNniDlciTransferPriorityToNetwork = _MscFrNniDlciTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 37),
    _MscFrNniDlciTransferPriorityToNetwork_Type()
)
mscFrNniDlciTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTransferPriorityToNetwork.setStatus("obsolete")


class _MscFrNniDlciTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mscFrNniDlciTransferPriorityFromNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniDlciTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MscFrNniDlciTransferPriorityFromNetwork_Object = MibTableColumn
mscFrNniDlciTransferPriorityFromNetwork = _MscFrNniDlciTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 38),
    _MscFrNniDlciTransferPriorityFromNetwork_Type()
)
mscFrNniDlciTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTransferPriorityFromNetwork.setStatus("obsolete")


class _MscFrNniDlciCirPresent_Type(Unsigned32):
    """Custom type mscFrNniDlciCirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciCirPresent_Type.__name__ = "Unsigned32"
_MscFrNniDlciCirPresent_Object = MibTableColumn
mscFrNniDlciCirPresent = _MscFrNniDlciCirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 39),
    _MscFrNniDlciCirPresent_Type()
)
mscFrNniDlciCirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCirPresent.setStatus("mandatory")


class _MscFrNniDlciEirPresent_Type(Unsigned32):
    """Custom type mscFrNniDlciEirPresent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciEirPresent_Type.__name__ = "Unsigned32"
_MscFrNniDlciEirPresent_Object = MibTableColumn
mscFrNniDlciEirPresent = _MscFrNniDlciEirPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 14, 1, 40),
    _MscFrNniDlciEirPresent_Type()
)
mscFrNniDlciEirPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEirPresent.setStatus("mandatory")
_MscFrNniDlciIntTable_Object = MibTable
mscFrNniDlciIntTable = _MscFrNniDlciIntTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15)
)
if mibBuilder.loadTexts:
    mscFrNniDlciIntTable.setStatus("mandatory")
_MscFrNniDlciIntEntry_Object = MibTableRow
mscFrNniDlciIntEntry = _MscFrNniDlciIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1)
)
mscFrNniDlciIntEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciIntEntry.setStatus("mandatory")


class _MscFrNniDlciStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscFrNniDlciStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscFrNniDlciStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscFrNniDlciStartTime_Object = MibTableColumn
mscFrNniDlciStartTime = _MscFrNniDlciStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 1),
    _MscFrNniDlciStartTime_Type()
)
mscFrNniDlciStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciStartTime.setStatus("mandatory")


class _MscFrNniDlciTotalIngressBytes_Type(Unsigned64):
    """Custom type mscFrNniDlciTotalIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrNniDlciTotalIngressBytes_Type.__name__ = "Unsigned64"
_MscFrNniDlciTotalIngressBytes_Object = MibTableColumn
mscFrNniDlciTotalIngressBytes = _MscFrNniDlciTotalIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 2),
    _MscFrNniDlciTotalIngressBytes_Type()
)
mscFrNniDlciTotalIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTotalIngressBytes.setStatus("mandatory")


class _MscFrNniDlciTotalEgressBytes_Type(Unsigned64):
    """Custom type mscFrNniDlciTotalEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrNniDlciTotalEgressBytes_Type.__name__ = "Unsigned64"
_MscFrNniDlciTotalEgressBytes_Object = MibTableColumn
mscFrNniDlciTotalEgressBytes = _MscFrNniDlciTotalEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 3),
    _MscFrNniDlciTotalEgressBytes_Type()
)
mscFrNniDlciTotalEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTotalEgressBytes.setStatus("mandatory")


class _MscFrNniDlciEirIngressBytes_Type(Unsigned64):
    """Custom type mscFrNniDlciEirIngressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrNniDlciEirIngressBytes_Type.__name__ = "Unsigned64"
_MscFrNniDlciEirIngressBytes_Object = MibTableColumn
mscFrNniDlciEirIngressBytes = _MscFrNniDlciEirIngressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 4),
    _MscFrNniDlciEirIngressBytes_Type()
)
mscFrNniDlciEirIngressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEirIngressBytes.setStatus("mandatory")


class _MscFrNniDlciEirEgressBytes_Type(Unsigned64):
    """Custom type mscFrNniDlciEirEgressBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrNniDlciEirEgressBytes_Type.__name__ = "Unsigned64"
_MscFrNniDlciEirEgressBytes_Object = MibTableColumn
mscFrNniDlciEirEgressBytes = _MscFrNniDlciEirEgressBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 5),
    _MscFrNniDlciEirEgressBytes_Type()
)
mscFrNniDlciEirEgressBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEirEgressBytes.setStatus("mandatory")


class _MscFrNniDlciDiscardedBytes_Type(Unsigned64):
    """Custom type mscFrNniDlciDiscardedBytes based on Unsigned64"""
    subtypeSpec = Unsigned64.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_MscFrNniDlciDiscardedBytes_Type.__name__ = "Unsigned64"
_MscFrNniDlciDiscardedBytes_Object = MibTableColumn
mscFrNniDlciDiscardedBytes = _MscFrNniDlciDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 6),
    _MscFrNniDlciDiscardedBytes_Type()
)
mscFrNniDlciDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscardedBytes.setStatus("mandatory")


class _MscFrNniDlciTotalIngressSegFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciTotalIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciTotalIngressSegFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciTotalIngressSegFrm_Object = MibTableColumn
mscFrNniDlciTotalIngressSegFrm = _MscFrNniDlciTotalIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 7),
    _MscFrNniDlciTotalIngressSegFrm_Type()
)
mscFrNniDlciTotalIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTotalIngressSegFrm.setStatus("mandatory")


class _MscFrNniDlciTotalEgressSegFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciTotalEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciTotalEgressSegFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciTotalEgressSegFrm_Object = MibTableColumn
mscFrNniDlciTotalEgressSegFrm = _MscFrNniDlciTotalEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 8),
    _MscFrNniDlciTotalEgressSegFrm_Type()
)
mscFrNniDlciTotalEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciTotalEgressSegFrm.setStatus("mandatory")


class _MscFrNniDlciEirIngressSegFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciEirIngressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciEirIngressSegFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciEirIngressSegFrm_Object = MibTableColumn
mscFrNniDlciEirIngressSegFrm = _MscFrNniDlciEirIngressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 9),
    _MscFrNniDlciEirIngressSegFrm_Type()
)
mscFrNniDlciEirIngressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEirIngressSegFrm.setStatus("mandatory")


class _MscFrNniDlciEirEgressSegFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciEirEgressSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciEirEgressSegFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciEirEgressSegFrm_Object = MibTableColumn
mscFrNniDlciEirEgressSegFrm = _MscFrNniDlciEirEgressSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 10),
    _MscFrNniDlciEirEgressSegFrm_Type()
)
mscFrNniDlciEirEgressSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEirEgressSegFrm.setStatus("mandatory")


class _MscFrNniDlciDiscardedSegFrm_Type(Unsigned32):
    """Custom type mscFrNniDlciDiscardedSegFrm based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciDiscardedSegFrm_Type.__name__ = "Unsigned32"
_MscFrNniDlciDiscardedSegFrm_Object = MibTableColumn
mscFrNniDlciDiscardedSegFrm = _MscFrNniDlciDiscardedSegFrm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 11),
    _MscFrNniDlciDiscardedSegFrm_Type()
)
mscFrNniDlciDiscardedSegFrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciDiscardedSegFrm.setStatus("mandatory")


class _MscFrNniDlciCirPresentObs_Type(Unsigned32):
    """Custom type mscFrNniDlciCirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciCirPresentObs_Type.__name__ = "Unsigned32"
_MscFrNniDlciCirPresentObs_Object = MibTableColumn
mscFrNniDlciCirPresentObs = _MscFrNniDlciCirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 12),
    _MscFrNniDlciCirPresentObs_Type()
)
mscFrNniDlciCirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCirPresentObs.setStatus("obsolete")


class _MscFrNniDlciEirPresentObs_Type(Unsigned32):
    """Custom type mscFrNniDlciEirPresentObs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciEirPresentObs_Type.__name__ = "Unsigned32"
_MscFrNniDlciEirPresentObs_Object = MibTableColumn
mscFrNniDlciEirPresentObs = _MscFrNniDlciEirPresentObs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 13),
    _MscFrNniDlciEirPresentObs_Type()
)
mscFrNniDlciEirPresentObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciEirPresentObs.setStatus("obsolete")


class _MscFrNniDlciRateEnforcementPresent_Type(Integer32):
    """Custom type mscFrNniDlciRateEnforcementPresent based on Integer32"""
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


_MscFrNniDlciRateEnforcementPresent_Type.__name__ = "Integer32"
_MscFrNniDlciRateEnforcementPresent_Object = MibTableColumn
mscFrNniDlciRateEnforcementPresent = _MscFrNniDlciRateEnforcementPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 14),
    _MscFrNniDlciRateEnforcementPresent_Type()
)
mscFrNniDlciRateEnforcementPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciRateEnforcementPresent.setStatus("obsolete")


class _MscFrNniDlciRateAdaptationPresent_Type(Integer32):
    """Custom type mscFrNniDlciRateAdaptationPresent based on Integer32"""
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


_MscFrNniDlciRateAdaptationPresent_Type.__name__ = "Integer32"
_MscFrNniDlciRateAdaptationPresent_Object = MibTableColumn
mscFrNniDlciRateAdaptationPresent = _MscFrNniDlciRateAdaptationPresent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 15),
    _MscFrNniDlciRateAdaptationPresent_Type()
)
mscFrNniDlciRateAdaptationPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciRateAdaptationPresent.setStatus("obsolete")


class _MscFrNniDlciLocalRateAdaptOccurred_Type(Integer32):
    """Custom type mscFrNniDlciLocalRateAdaptOccurred based on Integer32"""
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


_MscFrNniDlciLocalRateAdaptOccurred_Type.__name__ = "Integer32"
_MscFrNniDlciLocalRateAdaptOccurred_Object = MibTableColumn
mscFrNniDlciLocalRateAdaptOccurred = _MscFrNniDlciLocalRateAdaptOccurred_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 16),
    _MscFrNniDlciLocalRateAdaptOccurred_Type()
)
mscFrNniDlciLocalRateAdaptOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciLocalRateAdaptOccurred.setStatus("mandatory")


class _MscFrNniDlciCallReferenceNumber_Type(Hex):
    """Custom type mscFrNniDlciCallReferenceNumber based on Hex"""
    defaultValue = 0

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscFrNniDlciCallReferenceNumber_Type.__name__ = "Hex"
_MscFrNniDlciCallReferenceNumber_Object = MibTableColumn
mscFrNniDlciCallReferenceNumber = _MscFrNniDlciCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 17),
    _MscFrNniDlciCallReferenceNumber_Type()
)
mscFrNniDlciCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCallReferenceNumber.setStatus("obsolete")


class _MscFrNniDlciElapsedDifference_Type(Unsigned32):
    """Custom type mscFrNniDlciElapsedDifference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciElapsedDifference_Type.__name__ = "Unsigned32"
_MscFrNniDlciElapsedDifference_Object = MibTableColumn
mscFrNniDlciElapsedDifference = _MscFrNniDlciElapsedDifference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 18),
    _MscFrNniDlciElapsedDifference_Type()
)
mscFrNniDlciElapsedDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciElapsedDifference.setStatus("mandatory")


class _MscFrNniDlciCallRefNumber_Type(Unsigned32):
    """Custom type mscFrNniDlciCallRefNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniDlciCallRefNumber_Type.__name__ = "Unsigned32"
_MscFrNniDlciCallRefNumber_Object = MibTableColumn
mscFrNniDlciCallRefNumber = _MscFrNniDlciCallRefNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 15, 1, 20),
    _MscFrNniDlciCallRefNumber_Type()
)
mscFrNniDlciCallRefNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCallRefNumber.setStatus("mandatory")
_MscFrNniDlciCalldTable_Object = MibTable
mscFrNniDlciCalldTable = _MscFrNniDlciCalldTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 16)
)
if mibBuilder.loadTexts:
    mscFrNniDlciCalldTable.setStatus("mandatory")
_MscFrNniDlciCalldEntry_Object = MibTableRow
mscFrNniDlciCalldEntry = _MscFrNniDlciCalldEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 16, 1)
)
mscFrNniDlciCalldEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniDlciIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniDlciCalldEntry.setStatus("mandatory")


class _MscFrNniDlciCallType_Type(Integer32):
    """Custom type mscFrNniDlciCallType based on Integer32"""
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


_MscFrNniDlciCallType_Type.__name__ = "Integer32"
_MscFrNniDlciCallType_Object = MibTableColumn
mscFrNniDlciCallType = _MscFrNniDlciCallType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 16, 1, 1),
    _MscFrNniDlciCallType_Type()
)
mscFrNniDlciCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCallType.setStatus("mandatory")


class _MscFrNniDlciCallState_Type(Integer32):
    """Custom type mscFrNniDlciCallState based on Integer32"""
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
          ("notApplicable", 20),
          ("null", 0),
          ("releaseIndication", 12),
          ("releaseRequest", 11),
          ("restart", 62),
          ("restartRequest", 61))
    )


_MscFrNniDlciCallState_Type.__name__ = "Integer32"
_MscFrNniDlciCallState_Object = MibTableColumn
mscFrNniDlciCallState = _MscFrNniDlciCallState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 16, 1, 2),
    _MscFrNniDlciCallState_Type()
)
mscFrNniDlciCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCallState.setStatus("mandatory")


class _MscFrNniDlciCallReference_Type(Unsigned32):
    """Custom type mscFrNniDlciCallReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_MscFrNniDlciCallReference_Type.__name__ = "Unsigned32"
_MscFrNniDlciCallReference_Object = MibTableColumn
mscFrNniDlciCallReference = _MscFrNniDlciCallReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 5, 16, 1, 3),
    _MscFrNniDlciCallReference_Type()
)
mscFrNniDlciCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniDlciCallReference.setStatus("mandatory")
_MscFrNniVFramer_ObjectIdentity = ObjectIdentity
mscFrNniVFramer = _MscFrNniVFramer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6)
)
_MscFrNniVFramerRowStatusTable_Object = MibTable
mscFrNniVFramerRowStatusTable = _MscFrNniVFramerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 1)
)
if mibBuilder.loadTexts:
    mscFrNniVFramerRowStatusTable.setStatus("mandatory")
_MscFrNniVFramerRowStatusEntry_Object = MibTableRow
mscFrNniVFramerRowStatusEntry = _MscFrNniVFramerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 1, 1)
)
mscFrNniVFramerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniVFramerRowStatusEntry.setStatus("mandatory")
_MscFrNniVFramerRowStatus_Type = RowStatus
_MscFrNniVFramerRowStatus_Object = MibTableColumn
mscFrNniVFramerRowStatus = _MscFrNniVFramerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 1, 1, 1),
    _MscFrNniVFramerRowStatus_Type()
)
mscFrNniVFramerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniVFramerRowStatus.setStatus("mandatory")
_MscFrNniVFramerComponentName_Type = DisplayString
_MscFrNniVFramerComponentName_Object = MibTableColumn
mscFrNniVFramerComponentName = _MscFrNniVFramerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 1, 1, 2),
    _MscFrNniVFramerComponentName_Type()
)
mscFrNniVFramerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerComponentName.setStatus("mandatory")
_MscFrNniVFramerStorageType_Type = StorageType
_MscFrNniVFramerStorageType_Object = MibTableColumn
mscFrNniVFramerStorageType = _MscFrNniVFramerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 1, 1, 4),
    _MscFrNniVFramerStorageType_Type()
)
mscFrNniVFramerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerStorageType.setStatus("mandatory")
_MscFrNniVFramerIndex_Type = NonReplicated
_MscFrNniVFramerIndex_Object = MibTableColumn
mscFrNniVFramerIndex = _MscFrNniVFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 1, 1, 10),
    _MscFrNniVFramerIndex_Type()
)
mscFrNniVFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniVFramerIndex.setStatus("mandatory")
_MscFrNniVFramerProvTable_Object = MibTable
mscFrNniVFramerProvTable = _MscFrNniVFramerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 10)
)
if mibBuilder.loadTexts:
    mscFrNniVFramerProvTable.setStatus("mandatory")
_MscFrNniVFramerProvEntry_Object = MibTableRow
mscFrNniVFramerProvEntry = _MscFrNniVFramerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 10, 1)
)
mscFrNniVFramerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniVFramerProvEntry.setStatus("mandatory")
_MscFrNniVFramerOtherVirtualFramer_Type = Link
_MscFrNniVFramerOtherVirtualFramer_Object = MibTableColumn
mscFrNniVFramerOtherVirtualFramer = _MscFrNniVFramerOtherVirtualFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 10, 1, 1),
    _MscFrNniVFramerOtherVirtualFramer_Type()
)
mscFrNniVFramerOtherVirtualFramer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniVFramerOtherVirtualFramer.setStatus("mandatory")
_MscFrNniVFramerLogicalProcessor_Type = Link
_MscFrNniVFramerLogicalProcessor_Object = MibTableColumn
mscFrNniVFramerLogicalProcessor = _MscFrNniVFramerLogicalProcessor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 10, 1, 2),
    _MscFrNniVFramerLogicalProcessor_Type()
)
mscFrNniVFramerLogicalProcessor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniVFramerLogicalProcessor.setStatus("mandatory")
_MscFrNniVFramerStateTable_Object = MibTable
mscFrNniVFramerStateTable = _MscFrNniVFramerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 11)
)
if mibBuilder.loadTexts:
    mscFrNniVFramerStateTable.setStatus("mandatory")
_MscFrNniVFramerStateEntry_Object = MibTableRow
mscFrNniVFramerStateEntry = _MscFrNniVFramerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 11, 1)
)
mscFrNniVFramerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniVFramerStateEntry.setStatus("mandatory")


class _MscFrNniVFramerAdminState_Type(Integer32):
    """Custom type mscFrNniVFramerAdminState based on Integer32"""
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


_MscFrNniVFramerAdminState_Type.__name__ = "Integer32"
_MscFrNniVFramerAdminState_Object = MibTableColumn
mscFrNniVFramerAdminState = _MscFrNniVFramerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 11, 1, 1),
    _MscFrNniVFramerAdminState_Type()
)
mscFrNniVFramerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerAdminState.setStatus("mandatory")


class _MscFrNniVFramerOperationalState_Type(Integer32):
    """Custom type mscFrNniVFramerOperationalState based on Integer32"""
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


_MscFrNniVFramerOperationalState_Type.__name__ = "Integer32"
_MscFrNniVFramerOperationalState_Object = MibTableColumn
mscFrNniVFramerOperationalState = _MscFrNniVFramerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 11, 1, 2),
    _MscFrNniVFramerOperationalState_Type()
)
mscFrNniVFramerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerOperationalState.setStatus("mandatory")


class _MscFrNniVFramerUsageState_Type(Integer32):
    """Custom type mscFrNniVFramerUsageState based on Integer32"""
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


_MscFrNniVFramerUsageState_Type.__name__ = "Integer32"
_MscFrNniVFramerUsageState_Object = MibTableColumn
mscFrNniVFramerUsageState = _MscFrNniVFramerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 11, 1, 3),
    _MscFrNniVFramerUsageState_Type()
)
mscFrNniVFramerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerUsageState.setStatus("mandatory")
_MscFrNniVFramerStatsTable_Object = MibTable
mscFrNniVFramerStatsTable = _MscFrNniVFramerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 12)
)
if mibBuilder.loadTexts:
    mscFrNniVFramerStatsTable.setStatus("mandatory")
_MscFrNniVFramerStatsEntry_Object = MibTableRow
mscFrNniVFramerStatsEntry = _MscFrNniVFramerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 12, 1)
)
mscFrNniVFramerStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniVFramerIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniVFramerStatsEntry.setStatus("mandatory")
_MscFrNniVFramerFrmToOtherVFramer_Type = PassportCounter64
_MscFrNniVFramerFrmToOtherVFramer_Object = MibTableColumn
mscFrNniVFramerFrmToOtherVFramer = _MscFrNniVFramerFrmToOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 12, 1, 2),
    _MscFrNniVFramerFrmToOtherVFramer_Type()
)
mscFrNniVFramerFrmToOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerFrmToOtherVFramer.setStatus("mandatory")
_MscFrNniVFramerFrmFromOtherVFramer_Type = PassportCounter64
_MscFrNniVFramerFrmFromOtherVFramer_Object = MibTableColumn
mscFrNniVFramerFrmFromOtherVFramer = _MscFrNniVFramerFrmFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 12, 1, 3),
    _MscFrNniVFramerFrmFromOtherVFramer_Type()
)
mscFrNniVFramerFrmFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerFrmFromOtherVFramer.setStatus("mandatory")
_MscFrNniVFramerOctetFromOtherVFramer_Type = PassportCounter64
_MscFrNniVFramerOctetFromOtherVFramer_Object = MibTableColumn
mscFrNniVFramerOctetFromOtherVFramer = _MscFrNniVFramerOctetFromOtherVFramer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 6, 12, 1, 5),
    _MscFrNniVFramerOctetFromOtherVFramer_Type()
)
mscFrNniVFramerOctetFromOtherVFramer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniVFramerOctetFromOtherVFramer.setStatus("mandatory")
_MscFrNniSig_ObjectIdentity = ObjectIdentity
mscFrNniSig = _MscFrNniSig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8)
)
_MscFrNniSigRowStatusTable_Object = MibTable
mscFrNniSigRowStatusTable = _MscFrNniSigRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 1)
)
if mibBuilder.loadTexts:
    mscFrNniSigRowStatusTable.setStatus("mandatory")
_MscFrNniSigRowStatusEntry_Object = MibTableRow
mscFrNniSigRowStatusEntry = _MscFrNniSigRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 1, 1)
)
mscFrNniSigRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigRowStatusEntry.setStatus("mandatory")
_MscFrNniSigRowStatus_Type = RowStatus
_MscFrNniSigRowStatus_Object = MibTableColumn
mscFrNniSigRowStatus = _MscFrNniSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 1, 1, 1),
    _MscFrNniSigRowStatus_Type()
)
mscFrNniSigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigRowStatus.setStatus("mandatory")
_MscFrNniSigComponentName_Type = DisplayString
_MscFrNniSigComponentName_Object = MibTableColumn
mscFrNniSigComponentName = _MscFrNniSigComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 1, 1, 2),
    _MscFrNniSigComponentName_Type()
)
mscFrNniSigComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigComponentName.setStatus("mandatory")
_MscFrNniSigStorageType_Type = StorageType
_MscFrNniSigStorageType_Object = MibTableColumn
mscFrNniSigStorageType = _MscFrNniSigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 1, 1, 4),
    _MscFrNniSigStorageType_Type()
)
mscFrNniSigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigStorageType.setStatus("mandatory")
_MscFrNniSigIndex_Type = NonReplicated
_MscFrNniSigIndex_Object = MibTableColumn
mscFrNniSigIndex = _MscFrNniSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 1, 1, 10),
    _MscFrNniSigIndex_Type()
)
mscFrNniSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniSigIndex.setStatus("mandatory")
_MscFrNniSigProvTable_Object = MibTable
mscFrNniSigProvTable = _MscFrNniSigProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 11)
)
if mibBuilder.loadTexts:
    mscFrNniSigProvTable.setStatus("mandatory")
_MscFrNniSigProvEntry_Object = MibTableRow
mscFrNniSigProvEntry = _MscFrNniSigProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 11, 1)
)
mscFrNniSigProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigProvEntry.setStatus("mandatory")


class _MscFrNniSigDlciAllocation_Type(Integer32):
    """Custom type mscFrNniSigDlciAllocation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fromHighEnd", 1),
          ("fromLowEnd", 0))
    )


_MscFrNniSigDlciAllocation_Type.__name__ = "Integer32"
_MscFrNniSigDlciAllocation_Object = MibTableColumn
mscFrNniSigDlciAllocation = _MscFrNniSigDlciAllocation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 11, 1, 3),
    _MscFrNniSigDlciAllocation_Type()
)
mscFrNniSigDlciAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigDlciAllocation.setStatus("mandatory")


class _MscFrNniSigHighestPermanentDlci_Type(Unsigned32):
    """Custom type mscFrNniSigHighestPermanentDlci based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrNniSigHighestPermanentDlci_Type.__name__ = "Unsigned32"
_MscFrNniSigHighestPermanentDlci_Object = MibTableColumn
mscFrNniSigHighestPermanentDlci = _MscFrNniSigHighestPermanentDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 11, 1, 4),
    _MscFrNniSigHighestPermanentDlci_Type()
)
mscFrNniSigHighestPermanentDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigHighestPermanentDlci.setStatus("obsolete")


class _MscFrNniSigHighestPvcDlci_Type(Unsigned32):
    """Custom type mscFrNniSigHighestPvcDlci based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrNniSigHighestPvcDlci_Type.__name__ = "Unsigned32"
_MscFrNniSigHighestPvcDlci_Object = MibTableColumn
mscFrNniSigHighestPvcDlci = _MscFrNniSigHighestPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 11, 1, 5),
    _MscFrNniSigHighestPvcDlci_Type()
)
mscFrNniSigHighestPvcDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigHighestPvcDlci.setStatus("mandatory")
_MscFrNniSigServParmsTable_Object = MibTable
mscFrNniSigServParmsTable = _MscFrNniSigServParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12)
)
if mibBuilder.loadTexts:
    mscFrNniSigServParmsTable.setStatus("mandatory")
_MscFrNniSigServParmsEntry_Object = MibTableRow
mscFrNniSigServParmsEntry = _MscFrNniSigServParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1)
)
mscFrNniSigServParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigServParmsEntry.setStatus("mandatory")


class _MscFrNniSigMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrNniSigMaximumFrameSize based on Unsigned32"""
    defaultValue = 4096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrNniSigMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrNniSigMaximumFrameSize_Object = MibTableColumn
mscFrNniSigMaximumFrameSize = _MscFrNniSigMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 1),
    _MscFrNniSigMaximumFrameSize_Type()
)
mscFrNniSigMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigMaximumFrameSize.setStatus("mandatory")


class _MscFrNniSigDefaultMaximumFrameSize_Type(Unsigned32):
    """Custom type mscFrNniSigDefaultMaximumFrameSize based on Unsigned32"""
    defaultValue = 2100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8187),
    )


_MscFrNniSigDefaultMaximumFrameSize_Type.__name__ = "Unsigned32"
_MscFrNniSigDefaultMaximumFrameSize_Object = MibTableColumn
mscFrNniSigDefaultMaximumFrameSize = _MscFrNniSigDefaultMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 2),
    _MscFrNniSigDefaultMaximumFrameSize_Type()
)
mscFrNniSigDefaultMaximumFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigDefaultMaximumFrameSize.setStatus("mandatory")


class _MscFrNniSigDefaultCommittedInformationRate_Type(Unsigned32):
    """Custom type mscFrNniSigDefaultCommittedInformationRate based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrNniSigDefaultCommittedInformationRate_Type.__name__ = "Unsigned32"
_MscFrNniSigDefaultCommittedInformationRate_Object = MibTableColumn
mscFrNniSigDefaultCommittedInformationRate = _MscFrNniSigDefaultCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 3),
    _MscFrNniSigDefaultCommittedInformationRate_Type()
)
mscFrNniSigDefaultCommittedInformationRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigDefaultCommittedInformationRate.setStatus("mandatory")


class _MscFrNniSigDefaultCommittedBurstSize_Type(Unsigned32):
    """Custom type mscFrNniSigDefaultCommittedBurstSize based on Unsigned32"""
    defaultValue = 64000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrNniSigDefaultCommittedBurstSize_Type.__name__ = "Unsigned32"
_MscFrNniSigDefaultCommittedBurstSize_Object = MibTableColumn
mscFrNniSigDefaultCommittedBurstSize = _MscFrNniSigDefaultCommittedBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 4),
    _MscFrNniSigDefaultCommittedBurstSize_Type()
)
mscFrNniSigDefaultCommittedBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigDefaultCommittedBurstSize.setStatus("mandatory")


class _MscFrNniSigDefaultExcessBurstSize_Type(Unsigned32):
    """Custom type mscFrNniSigDefaultExcessBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrNniSigDefaultExcessBurstSize_Type.__name__ = "Unsigned32"
_MscFrNniSigDefaultExcessBurstSize_Object = MibTableColumn
mscFrNniSigDefaultExcessBurstSize = _MscFrNniSigDefaultExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 5),
    _MscFrNniSigDefaultExcessBurstSize_Type()
)
mscFrNniSigDefaultExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigDefaultExcessBurstSize.setStatus("mandatory")


class _MscFrNniSigRateEnforcement_Type(Integer32):
    """Custom type mscFrNniSigRateEnforcement based on Integer32"""
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


_MscFrNniSigRateEnforcement_Type.__name__ = "Integer32"
_MscFrNniSigRateEnforcement_Object = MibTableColumn
mscFrNniSigRateEnforcement = _MscFrNniSigRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 6),
    _MscFrNniSigRateEnforcement_Type()
)
mscFrNniSigRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigRateEnforcement.setStatus("mandatory")


class _MscFrNniSigRateAdaptation_Type(Integer32):
    """Custom type mscFrNniSigRateAdaptation based on Integer32"""
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


_MscFrNniSigRateAdaptation_Type.__name__ = "Integer32"
_MscFrNniSigRateAdaptation_Object = MibTableColumn
mscFrNniSigRateAdaptation = _MscFrNniSigRateAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 7),
    _MscFrNniSigRateAdaptation_Type()
)
mscFrNniSigRateAdaptation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigRateAdaptation.setStatus("mandatory")


class _MscFrNniSigRaSensitivity_Type(Unsigned32):
    """Custom type mscFrNniSigRaSensitivity based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MscFrNniSigRaSensitivity_Type.__name__ = "Unsigned32"
_MscFrNniSigRaSensitivity_Object = MibTableColumn
mscFrNniSigRaSensitivity = _MscFrNniSigRaSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 8),
    _MscFrNniSigRaSensitivity_Type()
)
mscFrNniSigRaSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigRaSensitivity.setStatus("mandatory")


class _MscFrNniSigUpdateBCI_Type(Integer32):
    """Custom type mscFrNniSigUpdateBCI based on Integer32"""
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


_MscFrNniSigUpdateBCI_Type.__name__ = "Integer32"
_MscFrNniSigUpdateBCI_Object = MibTableColumn
mscFrNniSigUpdateBCI = _MscFrNniSigUpdateBCI_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 12, 1, 9),
    _MscFrNniSigUpdateBCI_Type()
)
mscFrNniSigUpdateBCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigUpdateBCI.setStatus("mandatory")
_MscFrNniSigSysParmsTable_Object = MibTable
mscFrNniSigSysParmsTable = _MscFrNniSigSysParmsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13)
)
if mibBuilder.loadTexts:
    mscFrNniSigSysParmsTable.setStatus("mandatory")
_MscFrNniSigSysParmsEntry_Object = MibTableRow
mscFrNniSigSysParmsEntry = _MscFrNniSigSysParmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1)
)
mscFrNniSigSysParmsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigSysParmsEntry.setStatus("mandatory")


class _MscFrNniSigCallSetupTimer_Type(Unsigned32):
    """Custom type mscFrNniSigCallSetupTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrNniSigCallSetupTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigCallSetupTimer_Object = MibTableColumn
mscFrNniSigCallSetupTimer = _MscFrNniSigCallSetupTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1, 1),
    _MscFrNniSigCallSetupTimer_Type()
)
mscFrNniSigCallSetupTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigCallSetupTimer.setStatus("mandatory")


class _MscFrNniSigReleaseTimer_Type(Unsigned32):
    """Custom type mscFrNniSigReleaseTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrNniSigReleaseTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigReleaseTimer_Object = MibTableColumn
mscFrNniSigReleaseTimer = _MscFrNniSigReleaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1, 2),
    _MscFrNniSigReleaseTimer_Type()
)
mscFrNniSigReleaseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigReleaseTimer.setStatus("mandatory")


class _MscFrNniSigCallProceedingTimer_Type(Unsigned32):
    """Custom type mscFrNniSigCallProceedingTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrNniSigCallProceedingTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigCallProceedingTimer_Object = MibTableColumn
mscFrNniSigCallProceedingTimer = _MscFrNniSigCallProceedingTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1, 3),
    _MscFrNniSigCallProceedingTimer_Type()
)
mscFrNniSigCallProceedingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigCallProceedingTimer.setStatus("mandatory")


class _MscFrNniSigRestartReqTimer_Type(Unsigned32):
    """Custom type mscFrNniSigRestartReqTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniSigRestartReqTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigRestartReqTimer_Object = MibTableColumn
mscFrNniSigRestartReqTimer = _MscFrNniSigRestartReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1, 4),
    _MscFrNniSigRestartReqTimer_Type()
)
mscFrNniSigRestartReqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigRestartReqTimer.setStatus("mandatory")


class _MscFrNniSigRestartRcvTimer_Type(Unsigned32):
    """Custom type mscFrNniSigRestartRcvTimer based on Unsigned32"""
    defaultValue = 110

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrNniSigRestartRcvTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigRestartRcvTimer_Object = MibTableColumn
mscFrNniSigRestartRcvTimer = _MscFrNniSigRestartRcvTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1, 5),
    _MscFrNniSigRestartRcvTimer_Type()
)
mscFrNniSigRestartRcvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigRestartRcvTimer.setStatus("mandatory")


class _MscFrNniSigStatusEnqTimer_Type(Unsigned32):
    """Custom type mscFrNniSigStatusEnqTimer based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MscFrNniSigStatusEnqTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigStatusEnqTimer_Object = MibTableColumn
mscFrNniSigStatusEnqTimer = _MscFrNniSigStatusEnqTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1, 6),
    _MscFrNniSigStatusEnqTimer_Type()
)
mscFrNniSigStatusEnqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigStatusEnqTimer.setStatus("mandatory")


class _MscFrNniSigNetworkType_Type(Integer32):
    """Custom type mscFrNniSigNetworkType based on Integer32"""
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


_MscFrNniSigNetworkType_Type.__name__ = "Integer32"
_MscFrNniSigNetworkType_Object = MibTableColumn
mscFrNniSigNetworkType = _MscFrNniSigNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 13, 1, 7),
    _MscFrNniSigNetworkType_Type()
)
mscFrNniSigNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigNetworkType.setStatus("mandatory")
_MscFrNniSigLapfSysTable_Object = MibTable
mscFrNniSigLapfSysTable = _MscFrNniSigLapfSysTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 14)
)
if mibBuilder.loadTexts:
    mscFrNniSigLapfSysTable.setStatus("mandatory")
_MscFrNniSigLapfSysEntry_Object = MibTableRow
mscFrNniSigLapfSysEntry = _MscFrNniSigLapfSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 14, 1)
)
mscFrNniSigLapfSysEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigLapfSysEntry.setStatus("mandatory")


class _MscFrNniSigWindowSize_Type(Unsigned32):
    """Custom type mscFrNniSigWindowSize based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MscFrNniSigWindowSize_Type.__name__ = "Unsigned32"
_MscFrNniSigWindowSize_Object = MibTableColumn
mscFrNniSigWindowSize = _MscFrNniSigWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 14, 1, 2),
    _MscFrNniSigWindowSize_Type()
)
mscFrNniSigWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigWindowSize.setStatus("mandatory")


class _MscFrNniSigRetransmitLimit_Type(Unsigned32):
    """Custom type mscFrNniSigRetransmitLimit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MscFrNniSigRetransmitLimit_Type.__name__ = "Unsigned32"
_MscFrNniSigRetransmitLimit_Object = MibTableColumn
mscFrNniSigRetransmitLimit = _MscFrNniSigRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 14, 1, 3),
    _MscFrNniSigRetransmitLimit_Type()
)
mscFrNniSigRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigRetransmitLimit.setStatus("mandatory")


class _MscFrNniSigAckTimer_Type(Unsigned32):
    """Custom type mscFrNniSigAckTimer based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_MscFrNniSigAckTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigAckTimer_Object = MibTableColumn
mscFrNniSigAckTimer = _MscFrNniSigAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 14, 1, 4),
    _MscFrNniSigAckTimer_Type()
)
mscFrNniSigAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigAckTimer.setStatus("mandatory")


class _MscFrNniSigAckDelayTimer_Type(Unsigned32):
    """Custom type mscFrNniSigAckDelayTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MscFrNniSigAckDelayTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigAckDelayTimer_Object = MibTableColumn
mscFrNniSigAckDelayTimer = _MscFrNniSigAckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 14, 1, 5),
    _MscFrNniSigAckDelayTimer_Type()
)
mscFrNniSigAckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigAckDelayTimer.setStatus("mandatory")


class _MscFrNniSigIdleProbeTimer_Type(Unsigned32):
    """Custom type mscFrNniSigIdleProbeTimer based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535000),
    )


_MscFrNniSigIdleProbeTimer_Type.__name__ = "Unsigned32"
_MscFrNniSigIdleProbeTimer_Object = MibTableColumn
mscFrNniSigIdleProbeTimer = _MscFrNniSigIdleProbeTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 14, 1, 6),
    _MscFrNniSigIdleProbeTimer_Type()
)
mscFrNniSigIdleProbeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigIdleProbeTimer.setStatus("mandatory")
_MscFrNniSigCodesTable_Object = MibTable
mscFrNniSigCodesTable = _MscFrNniSigCodesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 15)
)
if mibBuilder.loadTexts:
    mscFrNniSigCodesTable.setStatus("mandatory")
_MscFrNniSigCodesEntry_Object = MibTableRow
mscFrNniSigCodesEntry = _MscFrNniSigCodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 15, 1)
)
mscFrNniSigCodesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigCodesEntry.setStatus("mandatory")


class _MscFrNniSigLastClearRemoteDataNetworkAddress_Type(DigitString):
    """Custom type mscFrNniSigLastClearRemoteDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscFrNniSigLastClearRemoteDataNetworkAddress_Type.__name__ = "DigitString"
_MscFrNniSigLastClearRemoteDataNetworkAddress_Object = MibTableColumn
mscFrNniSigLastClearRemoteDataNetworkAddress = _MscFrNniSigLastClearRemoteDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 15, 1, 1),
    _MscFrNniSigLastClearRemoteDataNetworkAddress_Type()
)
mscFrNniSigLastClearRemoteDataNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastClearRemoteDataNetworkAddress.setStatus("mandatory")


class _MscFrNniSigLastClearCause_Type(Unsigned32):
    """Custom type mscFrNniSigLastClearCause based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniSigLastClearCause_Type.__name__ = "Unsigned32"
_MscFrNniSigLastClearCause_Object = MibTableColumn
mscFrNniSigLastClearCause = _MscFrNniSigLastClearCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 15, 1, 2),
    _MscFrNniSigLastClearCause_Type()
)
mscFrNniSigLastClearCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastClearCause.setStatus("mandatory")


class _MscFrNniSigLastDiagnosticCode_Type(Unsigned32):
    """Custom type mscFrNniSigLastDiagnosticCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniSigLastDiagnosticCode_Type.__name__ = "Unsigned32"
_MscFrNniSigLastDiagnosticCode_Object = MibTableColumn
mscFrNniSigLastDiagnosticCode = _MscFrNniSigLastDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 15, 1, 3),
    _MscFrNniSigLastDiagnosticCode_Type()
)
mscFrNniSigLastDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastDiagnosticCode.setStatus("mandatory")
_MscFrNniSigStateTable_Object = MibTable
mscFrNniSigStateTable = _MscFrNniSigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 16)
)
if mibBuilder.loadTexts:
    mscFrNniSigStateTable.setStatus("mandatory")
_MscFrNniSigStateEntry_Object = MibTableRow
mscFrNniSigStateEntry = _MscFrNniSigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 16, 1)
)
mscFrNniSigStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigStateEntry.setStatus("mandatory")


class _MscFrNniSigAdminState_Type(Integer32):
    """Custom type mscFrNniSigAdminState based on Integer32"""
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


_MscFrNniSigAdminState_Type.__name__ = "Integer32"
_MscFrNniSigAdminState_Object = MibTableColumn
mscFrNniSigAdminState = _MscFrNniSigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 16, 1, 1),
    _MscFrNniSigAdminState_Type()
)
mscFrNniSigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigAdminState.setStatus("mandatory")


class _MscFrNniSigOperationalState_Type(Integer32):
    """Custom type mscFrNniSigOperationalState based on Integer32"""
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


_MscFrNniSigOperationalState_Type.__name__ = "Integer32"
_MscFrNniSigOperationalState_Object = MibTableColumn
mscFrNniSigOperationalState = _MscFrNniSigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 16, 1, 2),
    _MscFrNniSigOperationalState_Type()
)
mscFrNniSigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigOperationalState.setStatus("mandatory")


class _MscFrNniSigUsageState_Type(Integer32):
    """Custom type mscFrNniSigUsageState based on Integer32"""
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


_MscFrNniSigUsageState_Type.__name__ = "Integer32"
_MscFrNniSigUsageState_Object = MibTableColumn
mscFrNniSigUsageState = _MscFrNniSigUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 16, 1, 3),
    _MscFrNniSigUsageState_Type()
)
mscFrNniSigUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigUsageState.setStatus("mandatory")
_MscFrNniSigStatsTable_Object = MibTable
mscFrNniSigStatsTable = _MscFrNniSigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17)
)
if mibBuilder.loadTexts:
    mscFrNniSigStatsTable.setStatus("mandatory")
_MscFrNniSigStatsEntry_Object = MibTableRow
mscFrNniSigStatsEntry = _MscFrNniSigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1)
)
mscFrNniSigStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigStatsEntry.setStatus("mandatory")


class _MscFrNniSigCurrentNumberOfSvcCalls_Type(Gauge32):
    """Custom type mscFrNniSigCurrentNumberOfSvcCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrNniSigCurrentNumberOfSvcCalls_Type.__name__ = "Gauge32"
_MscFrNniSigCurrentNumberOfSvcCalls_Object = MibTableColumn
mscFrNniSigCurrentNumberOfSvcCalls = _MscFrNniSigCurrentNumberOfSvcCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 1),
    _MscFrNniSigCurrentNumberOfSvcCalls_Type()
)
mscFrNniSigCurrentNumberOfSvcCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigCurrentNumberOfSvcCalls.setStatus("mandatory")


class _MscFrNniSigInCalls_Type(Gauge32):
    """Custom type mscFrNniSigInCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrNniSigInCalls_Type.__name__ = "Gauge32"
_MscFrNniSigInCalls_Object = MibTableColumn
mscFrNniSigInCalls = _MscFrNniSigInCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 2),
    _MscFrNniSigInCalls_Type()
)
mscFrNniSigInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigInCalls.setStatus("mandatory")
_MscFrNniSigInCallsRefused_Type = Counter32
_MscFrNniSigInCallsRefused_Object = MibTableColumn
mscFrNniSigInCallsRefused = _MscFrNniSigInCallsRefused_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 3),
    _MscFrNniSigInCallsRefused_Type()
)
mscFrNniSigInCallsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigInCallsRefused.setStatus("mandatory")


class _MscFrNniSigOutCalls_Type(Gauge32):
    """Custom type mscFrNniSigOutCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrNniSigOutCalls_Type.__name__ = "Gauge32"
_MscFrNniSigOutCalls_Object = MibTableColumn
mscFrNniSigOutCalls = _MscFrNniSigOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 4),
    _MscFrNniSigOutCalls_Type()
)
mscFrNniSigOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigOutCalls.setStatus("mandatory")
_MscFrNniSigOutCallsFailed_Type = Counter32
_MscFrNniSigOutCallsFailed_Object = MibTableColumn
mscFrNniSigOutCallsFailed = _MscFrNniSigOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 5),
    _MscFrNniSigOutCallsFailed_Type()
)
mscFrNniSigOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigOutCallsFailed.setStatus("mandatory")
_MscFrNniSigProtocolErrors_Type = Counter32
_MscFrNniSigProtocolErrors_Object = MibTableColumn
mscFrNniSigProtocolErrors = _MscFrNniSigProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 6),
    _MscFrNniSigProtocolErrors_Type()
)
mscFrNniSigProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigProtocolErrors.setStatus("mandatory")
_MscFrNniSigQualityOfServiceNotAvailable_Type = Counter32
_MscFrNniSigQualityOfServiceNotAvailable_Object = MibTableColumn
mscFrNniSigQualityOfServiceNotAvailable = _MscFrNniSigQualityOfServiceNotAvailable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 7),
    _MscFrNniSigQualityOfServiceNotAvailable_Type()
)
mscFrNniSigQualityOfServiceNotAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigQualityOfServiceNotAvailable.setStatus("mandatory")
_MscFrNniSigSetupTimeout_Type = Counter32
_MscFrNniSigSetupTimeout_Object = MibTableColumn
mscFrNniSigSetupTimeout = _MscFrNniSigSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 8),
    _MscFrNniSigSetupTimeout_Type()
)
mscFrNniSigSetupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigSetupTimeout.setStatus("mandatory")


class _MscFrNniSigLastCauseInStatusMsgReceived_Type(Unsigned32):
    """Custom type mscFrNniSigLastCauseInStatusMsgReceived based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscFrNniSigLastCauseInStatusMsgReceived_Type.__name__ = "Unsigned32"
_MscFrNniSigLastCauseInStatusMsgReceived_Object = MibTableColumn
mscFrNniSigLastCauseInStatusMsgReceived = _MscFrNniSigLastCauseInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 9),
    _MscFrNniSigLastCauseInStatusMsgReceived_Type()
)
mscFrNniSigLastCauseInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastCauseInStatusMsgReceived.setStatus("mandatory")


class _MscFrNniSigLastStateInStatusMsgReceived_Type(Integer32):
    """Custom type mscFrNniSigLastStateInStatusMsgReceived based on Integer32"""
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
          ("incomingCallProceeding", 9),
          ("n13", 13),
          ("n14", 14),
          ("n15", 15),
          ("n16", 16),
          ("n17", 17),
          ("n18", 18),
          ("n19", 19),
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
          ("releaseIndication", 12),
          ("releaseRequest", 11),
          ("restart", 62),
          ("restartRequest", 61))
    )


_MscFrNniSigLastStateInStatusMsgReceived_Type.__name__ = "Integer32"
_MscFrNniSigLastStateInStatusMsgReceived_Object = MibTableColumn
mscFrNniSigLastStateInStatusMsgReceived = _MscFrNniSigLastStateInStatusMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 10),
    _MscFrNniSigLastStateInStatusMsgReceived_Type()
)
mscFrNniSigLastStateInStatusMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastStateInStatusMsgReceived.setStatus("mandatory")


class _MscFrNniSigLastDlciReceivedStatus_Type(Unsigned32):
    """Custom type mscFrNniSigLastDlciReceivedStatus based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1007),
    )


_MscFrNniSigLastDlciReceivedStatus_Type.__name__ = "Unsigned32"
_MscFrNniSigLastDlciReceivedStatus_Object = MibTableColumn
mscFrNniSigLastDlciReceivedStatus = _MscFrNniSigLastDlciReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 11),
    _MscFrNniSigLastDlciReceivedStatus_Type()
)
mscFrNniSigLastDlciReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastDlciReceivedStatus.setStatus("mandatory")


class _MscFrNniSigLastStateReceivedStatus_Type(Integer32):
    """Custom type mscFrNniSigLastStateReceivedStatus based on Integer32"""
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
              20,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("active", 10),
          ("callInitiated", 1),
          ("callPresent", 6),
          ("incomingCallProceeding", 9),
          ("notApplicable", 20),
          ("null", 0),
          ("outgoingCallProceeding", 3),
          ("releaseIndication", 12),
          ("releaseRequest", 11),
          ("restart", 62),
          ("restartRequest", 61))
    )


_MscFrNniSigLastStateReceivedStatus_Type.__name__ = "Integer32"
_MscFrNniSigLastStateReceivedStatus_Object = MibTableColumn
mscFrNniSigLastStateReceivedStatus = _MscFrNniSigLastStateReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 12),
    _MscFrNniSigLastStateReceivedStatus_Type()
)
mscFrNniSigLastStateReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastStateReceivedStatus.setStatus("mandatory")
_MscFrNniSigDlciCollisions_Type = Counter32
_MscFrNniSigDlciCollisions_Object = MibTableColumn
mscFrNniSigDlciCollisions = _MscFrNniSigDlciCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 17, 1, 15),
    _MscFrNniSigDlciCollisions_Type()
)
mscFrNniSigDlciCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigDlciCollisions.setStatus("mandatory")
_MscFrNniSigLapfStatusTable_Object = MibTable
mscFrNniSigLapfStatusTable = _MscFrNniSigLapfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 18)
)
if mibBuilder.loadTexts:
    mscFrNniSigLapfStatusTable.setStatus("mandatory")
_MscFrNniSigLapfStatusEntry_Object = MibTableRow
mscFrNniSigLapfStatusEntry = _MscFrNniSigLapfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 18, 1)
)
mscFrNniSigLapfStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigLapfStatusEntry.setStatus("mandatory")


class _MscFrNniSigCurrentState_Type(Integer32):
    """Custom type mscFrNniSigCurrentState based on Integer32"""
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


_MscFrNniSigCurrentState_Type.__name__ = "Integer32"
_MscFrNniSigCurrentState_Object = MibTableColumn
mscFrNniSigCurrentState = _MscFrNniSigCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 18, 1, 1),
    _MscFrNniSigCurrentState_Type()
)
mscFrNniSigCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigCurrentState.setStatus("mandatory")


class _MscFrNniSigLastStateChangeReason_Type(Integer32):
    """Custom type mscFrNniSigLastStateChangeReason based on Integer32"""
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


_MscFrNniSigLastStateChangeReason_Type.__name__ = "Integer32"
_MscFrNniSigLastStateChangeReason_Object = MibTableColumn
mscFrNniSigLastStateChangeReason = _MscFrNniSigLastStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 18, 1, 2),
    _MscFrNniSigLastStateChangeReason_Type()
)
mscFrNniSigLastStateChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigLastStateChangeReason.setStatus("mandatory")


class _MscFrNniSigFrmrReceive_Type(HexString):
    """Custom type mscFrNniSigFrmrReceive based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_MscFrNniSigFrmrReceive_Type.__name__ = "HexString"
_MscFrNniSigFrmrReceive_Object = MibTableColumn
mscFrNniSigFrmrReceive = _MscFrNniSigFrmrReceive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 18, 1, 3),
    _MscFrNniSigFrmrReceive_Type()
)
mscFrNniSigFrmrReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigFrmrReceive.setStatus("mandatory")
_MscFrNniSigCurrentQueueSize_Type = Counter32
_MscFrNniSigCurrentQueueSize_Object = MibTableColumn
mscFrNniSigCurrentQueueSize = _MscFrNniSigCurrentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 18, 1, 4),
    _MscFrNniSigCurrentQueueSize_Type()
)
mscFrNniSigCurrentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigCurrentQueueSize.setStatus("mandatory")
_MscFrNniSigLapfStatsTable_Object = MibTable
mscFrNniSigLapfStatsTable = _MscFrNniSigLapfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19)
)
if mibBuilder.loadTexts:
    mscFrNniSigLapfStatsTable.setStatus("mandatory")
_MscFrNniSigLapfStatsEntry_Object = MibTableRow
mscFrNniSigLapfStatsEntry = _MscFrNniSigLapfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1)
)
mscFrNniSigLapfStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigLapfStatsEntry.setStatus("mandatory")
_MscFrNniSigRemoteBusy_Type = Counter32
_MscFrNniSigRemoteBusy_Object = MibTableColumn
mscFrNniSigRemoteBusy = _MscFrNniSigRemoteBusy_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 2),
    _MscFrNniSigRemoteBusy_Type()
)
mscFrNniSigRemoteBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigRemoteBusy.setStatus("mandatory")
_MscFrNniSigReceiveRejectFrame_Type = Counter32
_MscFrNniSigReceiveRejectFrame_Object = MibTableColumn
mscFrNniSigReceiveRejectFrame = _MscFrNniSigReceiveRejectFrame_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 3),
    _MscFrNniSigReceiveRejectFrame_Type()
)
mscFrNniSigReceiveRejectFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigReceiveRejectFrame.setStatus("mandatory")
_MscFrNniSigAckTimeout_Type = Counter32
_MscFrNniSigAckTimeout_Object = MibTableColumn
mscFrNniSigAckTimeout = _MscFrNniSigAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 4),
    _MscFrNniSigAckTimeout_Type()
)
mscFrNniSigAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigAckTimeout.setStatus("mandatory")
_MscFrNniSigIFramesTransmitted_Type = Counter32
_MscFrNniSigIFramesTransmitted_Object = MibTableColumn
mscFrNniSigIFramesTransmitted = _MscFrNniSigIFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 5),
    _MscFrNniSigIFramesTransmitted_Type()
)
mscFrNniSigIFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigIFramesTransmitted.setStatus("mandatory")
_MscFrNniSigIFramesTxDiscarded_Type = Counter32
_MscFrNniSigIFramesTxDiscarded_Object = MibTableColumn
mscFrNniSigIFramesTxDiscarded = _MscFrNniSigIFramesTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 6),
    _MscFrNniSigIFramesTxDiscarded_Type()
)
mscFrNniSigIFramesTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigIFramesTxDiscarded.setStatus("mandatory")
_MscFrNniSigIFramesReceived_Type = Counter32
_MscFrNniSigIFramesReceived_Object = MibTableColumn
mscFrNniSigIFramesReceived = _MscFrNniSigIFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 7),
    _MscFrNniSigIFramesReceived_Type()
)
mscFrNniSigIFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigIFramesReceived.setStatus("mandatory")
_MscFrNniSigIFramesRcvdDiscarded_Type = Counter32
_MscFrNniSigIFramesRcvdDiscarded_Object = MibTableColumn
mscFrNniSigIFramesRcvdDiscarded = _MscFrNniSigIFramesRcvdDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 8),
    _MscFrNniSigIFramesRcvdDiscarded_Type()
)
mscFrNniSigIFramesRcvdDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigIFramesRcvdDiscarded.setStatus("mandatory")
_MscFrNniSigStateChange_Type = Counter32
_MscFrNniSigStateChange_Object = MibTableColumn
mscFrNniSigStateChange = _MscFrNniSigStateChange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 19, 1, 8650),
    _MscFrNniSigStateChange_Type()
)
mscFrNniSigStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigStateChange.setStatus("mandatory")
_MscFrNniSigSvcaccTable_Object = MibTable
mscFrNniSigSvcaccTable = _MscFrNniSigSvcaccTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 20)
)
if mibBuilder.loadTexts:
    mscFrNniSigSvcaccTable.setStatus("mandatory")
_MscFrNniSigSvcaccEntry_Object = MibTableRow
mscFrNniSigSvcaccEntry = _MscFrNniSigSvcaccEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 20, 1)
)
mscFrNniSigSvcaccEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigSvcaccEntry.setStatus("mandatory")


class _MscFrNniSigDefaultAccounting_Type(Integer32):
    """Custom type mscFrNniSigDefaultAccounting based on Integer32"""
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


_MscFrNniSigDefaultAccounting_Type.__name__ = "Integer32"
_MscFrNniSigDefaultAccounting_Object = MibTableColumn
mscFrNniSigDefaultAccounting = _MscFrNniSigDefaultAccounting_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 20, 1, 1),
    _MscFrNniSigDefaultAccounting_Type()
)
mscFrNniSigDefaultAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniSigDefaultAccounting.setStatus("mandatory")
_MscFrNniSigBandwidthNotAvailableTable_Object = MibTable
mscFrNniSigBandwidthNotAvailableTable = _MscFrNniSigBandwidthNotAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 672)
)
if mibBuilder.loadTexts:
    mscFrNniSigBandwidthNotAvailableTable.setStatus("mandatory")
_MscFrNniSigBandwidthNotAvailableEntry_Object = MibTableRow
mscFrNniSigBandwidthNotAvailableEntry = _MscFrNniSigBandwidthNotAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 672, 1)
)
mscFrNniSigBandwidthNotAvailableEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniSigBandwidthNotAvailableIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniSigBandwidthNotAvailableEntry.setStatus("mandatory")


class _MscFrNniSigBandwidthNotAvailableIndex_Type(Integer32):
    """Custom type mscFrNniSigBandwidthNotAvailableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniSigBandwidthNotAvailableIndex_Type.__name__ = "Integer32"
_MscFrNniSigBandwidthNotAvailableIndex_Object = MibTableColumn
mscFrNniSigBandwidthNotAvailableIndex = _MscFrNniSigBandwidthNotAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 672, 1, 1),
    _MscFrNniSigBandwidthNotAvailableIndex_Type()
)
mscFrNniSigBandwidthNotAvailableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniSigBandwidthNotAvailableIndex.setStatus("mandatory")
_MscFrNniSigBandwidthNotAvailableValue_Type = Counter32
_MscFrNniSigBandwidthNotAvailableValue_Object = MibTableColumn
mscFrNniSigBandwidthNotAvailableValue = _MscFrNniSigBandwidthNotAvailableValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 8, 672, 1, 2),
    _MscFrNniSigBandwidthNotAvailableValue_Type()
)
mscFrNniSigBandwidthNotAvailableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSigBandwidthNotAvailableValue.setStatus("mandatory")
_MscFrNniLts_ObjectIdentity = ObjectIdentity
mscFrNniLts = _MscFrNniLts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9)
)
_MscFrNniLtsRowStatusTable_Object = MibTable
mscFrNniLtsRowStatusTable = _MscFrNniLtsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 1)
)
if mibBuilder.loadTexts:
    mscFrNniLtsRowStatusTable.setStatus("mandatory")
_MscFrNniLtsRowStatusEntry_Object = MibTableRow
mscFrNniLtsRowStatusEntry = _MscFrNniLtsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 1, 1)
)
mscFrNniLtsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsRowStatusEntry.setStatus("mandatory")
_MscFrNniLtsRowStatus_Type = RowStatus
_MscFrNniLtsRowStatus_Object = MibTableColumn
mscFrNniLtsRowStatus = _MscFrNniLtsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 1, 1, 1),
    _MscFrNniLtsRowStatus_Type()
)
mscFrNniLtsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsRowStatus.setStatus("mandatory")
_MscFrNniLtsComponentName_Type = DisplayString
_MscFrNniLtsComponentName_Object = MibTableColumn
mscFrNniLtsComponentName = _MscFrNniLtsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 1, 1, 2),
    _MscFrNniLtsComponentName_Type()
)
mscFrNniLtsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsComponentName.setStatus("mandatory")
_MscFrNniLtsStorageType_Type = StorageType
_MscFrNniLtsStorageType_Object = MibTableColumn
mscFrNniLtsStorageType = _MscFrNniLtsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 1, 1, 4),
    _MscFrNniLtsStorageType_Type()
)
mscFrNniLtsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsStorageType.setStatus("mandatory")
_MscFrNniLtsIndex_Type = NonReplicated
_MscFrNniLtsIndex_Object = MibTableColumn
mscFrNniLtsIndex = _MscFrNniLtsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 1, 1, 10),
    _MscFrNniLtsIndex_Type()
)
mscFrNniLtsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniLtsIndex.setStatus("mandatory")
_MscFrNniLtsPat_ObjectIdentity = ObjectIdentity
mscFrNniLtsPat = _MscFrNniLtsPat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2)
)
_MscFrNniLtsPatRowStatusTable_Object = MibTable
mscFrNniLtsPatRowStatusTable = _MscFrNniLtsPatRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatRowStatusTable.setStatus("mandatory")
_MscFrNniLtsPatRowStatusEntry_Object = MibTableRow
mscFrNniLtsPatRowStatusEntry = _MscFrNniLtsPatRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 1, 1)
)
mscFrNniLtsPatRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatRowStatusEntry.setStatus("mandatory")
_MscFrNniLtsPatRowStatus_Type = RowStatus
_MscFrNniLtsPatRowStatus_Object = MibTableColumn
mscFrNniLtsPatRowStatus = _MscFrNniLtsPatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 1, 1, 1),
    _MscFrNniLtsPatRowStatus_Type()
)
mscFrNniLtsPatRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatRowStatus.setStatus("mandatory")
_MscFrNniLtsPatComponentName_Type = DisplayString
_MscFrNniLtsPatComponentName_Object = MibTableColumn
mscFrNniLtsPatComponentName = _MscFrNniLtsPatComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 1, 1, 2),
    _MscFrNniLtsPatComponentName_Type()
)
mscFrNniLtsPatComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsPatComponentName.setStatus("mandatory")
_MscFrNniLtsPatStorageType_Type = StorageType
_MscFrNniLtsPatStorageType_Object = MibTableColumn
mscFrNniLtsPatStorageType = _MscFrNniLtsPatStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 1, 1, 4),
    _MscFrNniLtsPatStorageType_Type()
)
mscFrNniLtsPatStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsPatStorageType.setStatus("mandatory")


class _MscFrNniLtsPatIndex_Type(Integer32):
    """Custom type mscFrNniLtsPatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_MscFrNniLtsPatIndex_Type.__name__ = "Integer32"
_MscFrNniLtsPatIndex_Object = MibTableColumn
mscFrNniLtsPatIndex = _MscFrNniLtsPatIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 1, 1, 10),
    _MscFrNniLtsPatIndex_Type()
)
mscFrNniLtsPatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniLtsPatIndex.setStatus("mandatory")
_MscFrNniLtsPatDefaultsTable_Object = MibTable
mscFrNniLtsPatDefaultsTable = _MscFrNniLtsPatDefaultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultsTable.setStatus("mandatory")
_MscFrNniLtsPatDefaultsEntry_Object = MibTableRow
mscFrNniLtsPatDefaultsEntry = _MscFrNniLtsPatDefaultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1)
)
mscFrNniLtsPatDefaultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultsEntry.setStatus("mandatory")


class _MscFrNniLtsPatDefaultDlci_Type(Unsigned32):
    """Custom type mscFrNniLtsPatDefaultDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrNniLtsPatDefaultDlci_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatDefaultDlci_Object = MibTableColumn
mscFrNniLtsPatDefaultDlci = _MscFrNniLtsPatDefaultDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 200),
    _MscFrNniLtsPatDefaultDlci_Type()
)
mscFrNniLtsPatDefaultDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultDlci.setStatus("mandatory")


class _MscFrNniLtsPatDefaultNumFrames_Type(Unsigned32):
    """Custom type mscFrNniLtsPatDefaultNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsPatDefaultNumFrames_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatDefaultNumFrames_Object = MibTableColumn
mscFrNniLtsPatDefaultNumFrames = _MscFrNniLtsPatDefaultNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 201),
    _MscFrNniLtsPatDefaultNumFrames_Type()
)
mscFrNniLtsPatDefaultNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultNumFrames.setStatus("mandatory")


class _MscFrNniLtsPatDefaultDataSize_Type(Unsigned32):
    """Custom type mscFrNniLtsPatDefaultDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_MscFrNniLtsPatDefaultDataSize_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatDefaultDataSize_Object = MibTableColumn
mscFrNniLtsPatDefaultDataSize = _MscFrNniLtsPatDefaultDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 202),
    _MscFrNniLtsPatDefaultDataSize_Type()
)
mscFrNniLtsPatDefaultDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultDataSize.setStatus("mandatory")


class _MscFrNniLtsPatDefaultHeaderBits_Type(OctetString):
    """Custom type mscFrNniLtsPatDefaultHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniLtsPatDefaultHeaderBits_Type.__name__ = "OctetString"
_MscFrNniLtsPatDefaultHeaderBits_Object = MibTableColumn
mscFrNniLtsPatDefaultHeaderBits = _MscFrNniLtsPatDefaultHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 203),
    _MscFrNniLtsPatDefaultHeaderBits_Type()
)
mscFrNniLtsPatDefaultHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultHeaderBits.setStatus("mandatory")


class _MscFrNniLtsPatDefaultHeaderLength_Type(Unsigned32):
    """Custom type mscFrNniLtsPatDefaultHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_MscFrNniLtsPatDefaultHeaderLength_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatDefaultHeaderLength_Object = MibTableColumn
mscFrNniLtsPatDefaultHeaderLength = _MscFrNniLtsPatDefaultHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 204),
    _MscFrNniLtsPatDefaultHeaderLength_Type()
)
mscFrNniLtsPatDefaultHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultHeaderLength.setStatus("mandatory")


class _MscFrNniLtsPatDefaultEABits_Type(Hex):
    """Custom type mscFrNniLtsPatDefaultEABits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniLtsPatDefaultEABits_Type.__name__ = "Hex"
_MscFrNniLtsPatDefaultEABits_Object = MibTableColumn
mscFrNniLtsPatDefaultEABits = _MscFrNniLtsPatDefaultEABits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 205),
    _MscFrNniLtsPatDefaultEABits_Type()
)
mscFrNniLtsPatDefaultEABits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultEABits.setStatus("mandatory")


class _MscFrNniLtsPatDefaultPayloadPattern_Type(HexString):
    """Custom type mscFrNniLtsPatDefaultPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscFrNniLtsPatDefaultPayloadPattern_Type.__name__ = "HexString"
_MscFrNniLtsPatDefaultPayloadPattern_Object = MibTableColumn
mscFrNniLtsPatDefaultPayloadPattern = _MscFrNniLtsPatDefaultPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 206),
    _MscFrNniLtsPatDefaultPayloadPattern_Type()
)
mscFrNniLtsPatDefaultPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultPayloadPattern.setStatus("mandatory")


class _MscFrNniLtsPatDefaultRfc1490Header_Type(Integer32):
    """Custom type mscFrNniLtsPatDefaultRfc1490Header based on Integer32"""
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


_MscFrNniLtsPatDefaultRfc1490Header_Type.__name__ = "Integer32"
_MscFrNniLtsPatDefaultRfc1490Header_Object = MibTableColumn
mscFrNniLtsPatDefaultRfc1490Header = _MscFrNniLtsPatDefaultRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 207),
    _MscFrNniLtsPatDefaultRfc1490Header_Type()
)
mscFrNniLtsPatDefaultRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultRfc1490Header.setStatus("mandatory")


class _MscFrNniLtsPatDefaultUseBadLrc_Type(Integer32):
    """Custom type mscFrNniLtsPatDefaultUseBadLrc based on Integer32"""
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


_MscFrNniLtsPatDefaultUseBadLrc_Type.__name__ = "Integer32"
_MscFrNniLtsPatDefaultUseBadLrc_Object = MibTableColumn
mscFrNniLtsPatDefaultUseBadLrc = _MscFrNniLtsPatDefaultUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 10, 1, 208),
    _MscFrNniLtsPatDefaultUseBadLrc_Type()
)
mscFrNniLtsPatDefaultUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDefaultUseBadLrc.setStatus("mandatory")
_MscFrNniLtsPatSetupTable_Object = MibTable
mscFrNniLtsPatSetupTable = _MscFrNniLtsPatSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11)
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatSetupTable.setStatus("mandatory")
_MscFrNniLtsPatSetupEntry_Object = MibTableRow
mscFrNniLtsPatSetupEntry = _MscFrNniLtsPatSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1)
)
mscFrNniLtsPatSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatSetupEntry.setStatus("mandatory")


class _MscFrNniLtsPatDlci_Type(Unsigned32):
    """Custom type mscFrNniLtsPatDlci based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscFrNniLtsPatDlci_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatDlci_Object = MibTableColumn
mscFrNniLtsPatDlci = _MscFrNniLtsPatDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 200),
    _MscFrNniLtsPatDlci_Type()
)
mscFrNniLtsPatDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDlci.setStatus("mandatory")


class _MscFrNniLtsPatNumFrames_Type(Unsigned32):
    """Custom type mscFrNniLtsPatNumFrames based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsPatNumFrames_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatNumFrames_Object = MibTableColumn
mscFrNniLtsPatNumFrames = _MscFrNniLtsPatNumFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 201),
    _MscFrNniLtsPatNumFrames_Type()
)
mscFrNniLtsPatNumFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatNumFrames.setStatus("mandatory")


class _MscFrNniLtsPatDataSize_Type(Unsigned32):
    """Custom type mscFrNniLtsPatDataSize based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8200),
    )


_MscFrNniLtsPatDataSize_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatDataSize_Object = MibTableColumn
mscFrNniLtsPatDataSize = _MscFrNniLtsPatDataSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 202),
    _MscFrNniLtsPatDataSize_Type()
)
mscFrNniLtsPatDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatDataSize.setStatus("mandatory")


class _MscFrNniLtsPatHeaderBits_Type(OctetString):
    """Custom type mscFrNniLtsPatHeaderBits based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniLtsPatHeaderBits_Type.__name__ = "OctetString"
_MscFrNniLtsPatHeaderBits_Object = MibTableColumn
mscFrNniLtsPatHeaderBits = _MscFrNniLtsPatHeaderBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 203),
    _MscFrNniLtsPatHeaderBits_Type()
)
mscFrNniLtsPatHeaderBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatHeaderBits.setStatus("mandatory")


class _MscFrNniLtsPatHeaderLength_Type(Unsigned32):
    """Custom type mscFrNniLtsPatHeaderLength based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4),
    )


_MscFrNniLtsPatHeaderLength_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatHeaderLength_Object = MibTableColumn
mscFrNniLtsPatHeaderLength = _MscFrNniLtsPatHeaderLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 204),
    _MscFrNniLtsPatHeaderLength_Type()
)
mscFrNniLtsPatHeaderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatHeaderLength.setStatus("mandatory")


class _MscFrNniLtsPatEaBits_Type(Hex):
    """Custom type mscFrNniLtsPatEaBits based on Hex"""
    defaultValue = 4

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniLtsPatEaBits_Type.__name__ = "Hex"
_MscFrNniLtsPatEaBits_Object = MibTableColumn
mscFrNniLtsPatEaBits = _MscFrNniLtsPatEaBits_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 205),
    _MscFrNniLtsPatEaBits_Type()
)
mscFrNniLtsPatEaBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatEaBits.setStatus("mandatory")


class _MscFrNniLtsPatPayloadPattern_Type(HexString):
    """Custom type mscFrNniLtsPatPayloadPattern based on HexString"""
    defaultHexValue = "55"

    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MscFrNniLtsPatPayloadPattern_Type.__name__ = "HexString"
_MscFrNniLtsPatPayloadPattern_Object = MibTableColumn
mscFrNniLtsPatPayloadPattern = _MscFrNniLtsPatPayloadPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 206),
    _MscFrNniLtsPatPayloadPattern_Type()
)
mscFrNniLtsPatPayloadPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatPayloadPattern.setStatus("mandatory")


class _MscFrNniLtsPatRfc1490Header_Type(Integer32):
    """Custom type mscFrNniLtsPatRfc1490Header based on Integer32"""
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


_MscFrNniLtsPatRfc1490Header_Type.__name__ = "Integer32"
_MscFrNniLtsPatRfc1490Header_Object = MibTableColumn
mscFrNniLtsPatRfc1490Header = _MscFrNniLtsPatRfc1490Header_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 207),
    _MscFrNniLtsPatRfc1490Header_Type()
)
mscFrNniLtsPatRfc1490Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatRfc1490Header.setStatus("mandatory")


class _MscFrNniLtsPatUseBadLrc_Type(Integer32):
    """Custom type mscFrNniLtsPatUseBadLrc based on Integer32"""
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


_MscFrNniLtsPatUseBadLrc_Type.__name__ = "Integer32"
_MscFrNniLtsPatUseBadLrc_Object = MibTableColumn
mscFrNniLtsPatUseBadLrc = _MscFrNniLtsPatUseBadLrc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 11, 1, 208),
    _MscFrNniLtsPatUseBadLrc_Type()
)
mscFrNniLtsPatUseBadLrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatUseBadLrc.setStatus("mandatory")
_MscFrNniLtsPatOpDataTable_Object = MibTable
mscFrNniLtsPatOpDataTable = _MscFrNniLtsPatOpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 12)
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatOpDataTable.setStatus("mandatory")
_MscFrNniLtsPatOpDataEntry_Object = MibTableRow
mscFrNniLtsPatOpDataEntry = _MscFrNniLtsPatOpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 12, 1)
)
mscFrNniLtsPatOpDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatOpDataEntry.setStatus("mandatory")


class _MscFrNniLtsPatFramePattern_Type(HexString):
    """Custom type mscFrNniLtsPatFramePattern based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 24),
    )


_MscFrNniLtsPatFramePattern_Type.__name__ = "HexString"
_MscFrNniLtsPatFramePattern_Object = MibTableColumn
mscFrNniLtsPatFramePattern = _MscFrNniLtsPatFramePattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 12, 1, 200),
    _MscFrNniLtsPatFramePattern_Type()
)
mscFrNniLtsPatFramePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsPatFramePattern.setStatus("mandatory")


class _MscFrNniLtsPatHdlcBitsInserted_Type(Unsigned32):
    """Custom type mscFrNniLtsPatHdlcBitsInserted based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscFrNniLtsPatHdlcBitsInserted_Type.__name__ = "Unsigned32"
_MscFrNniLtsPatHdlcBitsInserted_Object = MibTableColumn
mscFrNniLtsPatHdlcBitsInserted = _MscFrNniLtsPatHdlcBitsInserted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 12, 1, 201),
    _MscFrNniLtsPatHdlcBitsInserted_Type()
)
mscFrNniLtsPatHdlcBitsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsPatHdlcBitsInserted.setStatus("mandatory")
_MscFrNniLtsPatOpStateTable_Object = MibTable
mscFrNniLtsPatOpStateTable = _MscFrNniLtsPatOpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 13)
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatOpStateTable.setStatus("mandatory")
_MscFrNniLtsPatOpStateEntry_Object = MibTableRow
mscFrNniLtsPatOpStateEntry = _MscFrNniLtsPatOpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 13, 1)
)
mscFrNniLtsPatOpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsPatIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsPatOpStateEntry.setStatus("mandatory")


class _MscFrNniLtsPatLoad_Type(FixedPoint3):
    """Custom type mscFrNniLtsPatLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsPatLoad_Type.__name__ = "FixedPoint3"
_MscFrNniLtsPatLoad_Object = MibTableColumn
mscFrNniLtsPatLoad = _MscFrNniLtsPatLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 13, 1, 200),
    _MscFrNniLtsPatLoad_Type()
)
mscFrNniLtsPatLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsPatLoad.setStatus("mandatory")


class _MscFrNniLtsPatStatus_Type(Integer32):
    """Custom type mscFrNniLtsPatStatus based on Integer32"""
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


_MscFrNniLtsPatStatus_Type.__name__ = "Integer32"
_MscFrNniLtsPatStatus_Object = MibTableColumn
mscFrNniLtsPatStatus = _MscFrNniLtsPatStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 2, 13, 1, 201),
    _MscFrNniLtsPatStatus_Type()
)
mscFrNniLtsPatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsPatStatus.setStatus("mandatory")
_MscFrNniLtsSetupTable_Object = MibTable
mscFrNniLtsSetupTable = _MscFrNniLtsSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 10)
)
if mibBuilder.loadTexts:
    mscFrNniLtsSetupTable.setStatus("mandatory")
_MscFrNniLtsSetupEntry_Object = MibTableRow
mscFrNniLtsSetupEntry = _MscFrNniLtsSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 10, 1)
)
mscFrNniLtsSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsSetupEntry.setStatus("mandatory")


class _MscFrNniLtsDuration_Type(Unsigned32):
    """Custom type mscFrNniLtsDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsDuration_Type.__name__ = "Unsigned32"
_MscFrNniLtsDuration_Object = MibTableColumn
mscFrNniLtsDuration = _MscFrNniLtsDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 10, 1, 200),
    _MscFrNniLtsDuration_Type()
)
mscFrNniLtsDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsDuration.setStatus("mandatory")


class _MscFrNniLtsAlgorithm_Type(Integer32):
    """Custom type mscFrNniLtsAlgorithm based on Integer32"""
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


_MscFrNniLtsAlgorithm_Type.__name__ = "Integer32"
_MscFrNniLtsAlgorithm_Object = MibTableColumn
mscFrNniLtsAlgorithm = _MscFrNniLtsAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 10, 1, 201),
    _MscFrNniLtsAlgorithm_Type()
)
mscFrNniLtsAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsAlgorithm.setStatus("mandatory")


class _MscFrNniLtsBurstSize_Type(Unsigned32):
    """Custom type mscFrNniLtsBurstSize based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_MscFrNniLtsBurstSize_Type.__name__ = "Unsigned32"
_MscFrNniLtsBurstSize_Object = MibTableColumn
mscFrNniLtsBurstSize = _MscFrNniLtsBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 10, 1, 204),
    _MscFrNniLtsBurstSize_Type()
)
mscFrNniLtsBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsBurstSize.setStatus("mandatory")


class _MscFrNniLtsTimeInterval_Type(Unsigned32):
    """Custom type mscFrNniLtsTimeInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_MscFrNniLtsTimeInterval_Type.__name__ = "Unsigned32"
_MscFrNniLtsTimeInterval_Object = MibTableColumn
mscFrNniLtsTimeInterval = _MscFrNniLtsTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 10, 1, 205),
    _MscFrNniLtsTimeInterval_Type()
)
mscFrNniLtsTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniLtsTimeInterval.setStatus("mandatory")
_MscFrNniLtsStateTable_Object = MibTable
mscFrNniLtsStateTable = _MscFrNniLtsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 11)
)
if mibBuilder.loadTexts:
    mscFrNniLtsStateTable.setStatus("mandatory")
_MscFrNniLtsStateEntry_Object = MibTableRow
mscFrNniLtsStateEntry = _MscFrNniLtsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 11, 1)
)
mscFrNniLtsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsStateEntry.setStatus("mandatory")


class _MscFrNniLtsGeneratorState_Type(Integer32):
    """Custom type mscFrNniLtsGeneratorState based on Integer32"""
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


_MscFrNniLtsGeneratorState_Type.__name__ = "Integer32"
_MscFrNniLtsGeneratorState_Object = MibTableColumn
mscFrNniLtsGeneratorState = _MscFrNniLtsGeneratorState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 11, 1, 200),
    _MscFrNniLtsGeneratorState_Type()
)
mscFrNniLtsGeneratorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsGeneratorState.setStatus("mandatory")


class _MscFrNniLtsCycleIncomplete_Type(Integer32):
    """Custom type mscFrNniLtsCycleIncomplete based on Integer32"""
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


_MscFrNniLtsCycleIncomplete_Type.__name__ = "Integer32"
_MscFrNniLtsCycleIncomplete_Object = MibTableColumn
mscFrNniLtsCycleIncomplete = _MscFrNniLtsCycleIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 11, 1, 201),
    _MscFrNniLtsCycleIncomplete_Type()
)
mscFrNniLtsCycleIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsCycleIncomplete.setStatus("mandatory")


class _MscFrNniLtsLastActiveInterval_Type(Unsigned32):
    """Custom type mscFrNniLtsLastActiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsLastActiveInterval_Type.__name__ = "Unsigned32"
_MscFrNniLtsLastActiveInterval_Object = MibTableColumn
mscFrNniLtsLastActiveInterval = _MscFrNniLtsLastActiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 11, 1, 202),
    _MscFrNniLtsLastActiveInterval_Type()
)
mscFrNniLtsLastActiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsLastActiveInterval.setStatus("mandatory")


class _MscFrNniLtsLoad_Type(FixedPoint3):
    """Custom type mscFrNniLtsLoad based on FixedPoint3"""
    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsLoad_Type.__name__ = "FixedPoint3"
_MscFrNniLtsLoad_Object = MibTableColumn
mscFrNniLtsLoad = _MscFrNniLtsLoad_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 11, 1, 204),
    _MscFrNniLtsLoad_Type()
)
mscFrNniLtsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsLoad.setStatus("mandatory")


class _MscFrNniLtsElapsedGenerationTime_Type(Unsigned32):
    """Custom type mscFrNniLtsElapsedGenerationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsElapsedGenerationTime_Type.__name__ = "Unsigned32"
_MscFrNniLtsElapsedGenerationTime_Object = MibTableColumn
mscFrNniLtsElapsedGenerationTime = _MscFrNniLtsElapsedGenerationTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 11, 1, 205),
    _MscFrNniLtsElapsedGenerationTime_Type()
)
mscFrNniLtsElapsedGenerationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsElapsedGenerationTime.setStatus("mandatory")
_MscFrNniLtsResultsTable_Object = MibTable
mscFrNniLtsResultsTable = _MscFrNniLtsResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 12)
)
if mibBuilder.loadTexts:
    mscFrNniLtsResultsTable.setStatus("mandatory")
_MscFrNniLtsResultsEntry_Object = MibTableRow
mscFrNniLtsResultsEntry = _MscFrNniLtsResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 12, 1)
)
mscFrNniLtsResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniLtsIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniLtsResultsEntry.setStatus("mandatory")
_MscFrNniLtsFramesTx_Type = Counter32
_MscFrNniLtsFramesTx_Object = MibTableColumn
mscFrNniLtsFramesTx = _MscFrNniLtsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 12, 1, 200),
    _MscFrNniLtsFramesTx_Type()
)
mscFrNniLtsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsFramesTx.setStatus("mandatory")


class _MscFrNniLtsBytesTx_Type(Unsigned32):
    """Custom type mscFrNniLtsBytesTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsBytesTx_Type.__name__ = "Unsigned32"
_MscFrNniLtsBytesTx_Object = MibTableColumn
mscFrNniLtsBytesTx = _MscFrNniLtsBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 12, 1, 204),
    _MscFrNniLtsBytesTx_Type()
)
mscFrNniLtsBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsBytesTx.setStatus("mandatory")


class _MscFrNniLtsBitRateTx_Type(FixedPoint3):
    """Custom type mscFrNniLtsBitRateTx based on FixedPoint3"""
    defaultValue = 0

    subtypeSpec = FixedPoint3.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsBitRateTx_Type.__name__ = "FixedPoint3"
_MscFrNniLtsBitRateTx_Object = MibTableColumn
mscFrNniLtsBitRateTx = _MscFrNniLtsBitRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 12, 1, 208),
    _MscFrNniLtsBitRateTx_Type()
)
mscFrNniLtsBitRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsBitRateTx.setStatus("mandatory")


class _MscFrNniLtsFrameRateTx_Type(Unsigned32):
    """Custom type mscFrNniLtsFrameRateTx based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniLtsFrameRateTx_Type.__name__ = "Unsigned32"
_MscFrNniLtsFrameRateTx_Object = MibTableColumn
mscFrNniLtsFrameRateTx = _MscFrNniLtsFrameRateTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 9, 12, 1, 209),
    _MscFrNniLtsFrameRateTx_Type()
)
mscFrNniLtsFrameRateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLtsFrameRateTx.setStatus("mandatory")
_MscFrNniCidDataTable_Object = MibTable
mscFrNniCidDataTable = _MscFrNniCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 10)
)
if mibBuilder.loadTexts:
    mscFrNniCidDataTable.setStatus("mandatory")
_MscFrNniCidDataEntry_Object = MibTableRow
mscFrNniCidDataEntry = _MscFrNniCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 10, 1)
)
mscFrNniCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCidDataEntry.setStatus("mandatory")


class _MscFrNniCustomerIdentifier_Type(Unsigned32):
    """Custom type mscFrNniCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscFrNniCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscFrNniCustomerIdentifier_Object = MibTableColumn
mscFrNniCustomerIdentifier = _MscFrNniCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 10, 1, 1),
    _MscFrNniCustomerIdentifier_Type()
)
mscFrNniCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCustomerIdentifier.setStatus("mandatory")
_MscFrNniStateTable_Object = MibTable
mscFrNniStateTable = _MscFrNniStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11)
)
if mibBuilder.loadTexts:
    mscFrNniStateTable.setStatus("mandatory")
_MscFrNniStateEntry_Object = MibTableRow
mscFrNniStateEntry = _MscFrNniStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1)
)
mscFrNniStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniStateEntry.setStatus("mandatory")


class _MscFrNniAdminState_Type(Integer32):
    """Custom type mscFrNniAdminState based on Integer32"""
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


_MscFrNniAdminState_Type.__name__ = "Integer32"
_MscFrNniAdminState_Object = MibTableColumn
mscFrNniAdminState = _MscFrNniAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 1),
    _MscFrNniAdminState_Type()
)
mscFrNniAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniAdminState.setStatus("mandatory")


class _MscFrNniOperationalState_Type(Integer32):
    """Custom type mscFrNniOperationalState based on Integer32"""
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


_MscFrNniOperationalState_Type.__name__ = "Integer32"
_MscFrNniOperationalState_Object = MibTableColumn
mscFrNniOperationalState = _MscFrNniOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 2),
    _MscFrNniOperationalState_Type()
)
mscFrNniOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniOperationalState.setStatus("mandatory")


class _MscFrNniUsageState_Type(Integer32):
    """Custom type mscFrNniUsageState based on Integer32"""
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


_MscFrNniUsageState_Type.__name__ = "Integer32"
_MscFrNniUsageState_Object = MibTableColumn
mscFrNniUsageState = _MscFrNniUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 3),
    _MscFrNniUsageState_Type()
)
mscFrNniUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniUsageState.setStatus("mandatory")


class _MscFrNniAvailabilityStatus_Type(OctetString):
    """Custom type mscFrNniAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscFrNniAvailabilityStatus_Type.__name__ = "OctetString"
_MscFrNniAvailabilityStatus_Object = MibTableColumn
mscFrNniAvailabilityStatus = _MscFrNniAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 4),
    _MscFrNniAvailabilityStatus_Type()
)
mscFrNniAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniAvailabilityStatus.setStatus("mandatory")


class _MscFrNniProceduralStatus_Type(OctetString):
    """Custom type mscFrNniProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniProceduralStatus_Type.__name__ = "OctetString"
_MscFrNniProceduralStatus_Object = MibTableColumn
mscFrNniProceduralStatus = _MscFrNniProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 5),
    _MscFrNniProceduralStatus_Type()
)
mscFrNniProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniProceduralStatus.setStatus("mandatory")


class _MscFrNniControlStatus_Type(OctetString):
    """Custom type mscFrNniControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniControlStatus_Type.__name__ = "OctetString"
_MscFrNniControlStatus_Object = MibTableColumn
mscFrNniControlStatus = _MscFrNniControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 6),
    _MscFrNniControlStatus_Type()
)
mscFrNniControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniControlStatus.setStatus("mandatory")


class _MscFrNniAlarmStatus_Type(OctetString):
    """Custom type mscFrNniAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscFrNniAlarmStatus_Type.__name__ = "OctetString"
_MscFrNniAlarmStatus_Object = MibTableColumn
mscFrNniAlarmStatus = _MscFrNniAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 7),
    _MscFrNniAlarmStatus_Type()
)
mscFrNniAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniAlarmStatus.setStatus("mandatory")


class _MscFrNniStandbyStatus_Type(Integer32):
    """Custom type mscFrNniStandbyStatus based on Integer32"""
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


_MscFrNniStandbyStatus_Type.__name__ = "Integer32"
_MscFrNniStandbyStatus_Object = MibTableColumn
mscFrNniStandbyStatus = _MscFrNniStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 8),
    _MscFrNniStandbyStatus_Type()
)
mscFrNniStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniStandbyStatus.setStatus("mandatory")


class _MscFrNniUnknownStatus_Type(Integer32):
    """Custom type mscFrNniUnknownStatus based on Integer32"""
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


_MscFrNniUnknownStatus_Type.__name__ = "Integer32"
_MscFrNniUnknownStatus_Object = MibTableColumn
mscFrNniUnknownStatus = _MscFrNniUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 11, 1, 9),
    _MscFrNniUnknownStatus_Type()
)
mscFrNniUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniUnknownStatus.setStatus("mandatory")
_MscFrNniStatsTable_Object = MibTable
mscFrNniStatsTable = _MscFrNniStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 12)
)
if mibBuilder.loadTexts:
    mscFrNniStatsTable.setStatus("mandatory")
_MscFrNniStatsEntry_Object = MibTableRow
mscFrNniStatsEntry = _MscFrNniStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 12, 1)
)
mscFrNniStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniStatsEntry.setStatus("mandatory")


class _MscFrNniLastUnknownDlci_Type(Unsigned32):
    """Custom type mscFrNniLastUnknownDlci based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MscFrNniLastUnknownDlci_Type.__name__ = "Unsigned32"
_MscFrNniLastUnknownDlci_Object = MibTableColumn
mscFrNniLastUnknownDlci = _MscFrNniLastUnknownDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 12, 1, 1),
    _MscFrNniLastUnknownDlci_Type()
)
mscFrNniLastUnknownDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniLastUnknownDlci.setStatus("mandatory")
_MscFrNniUnknownDlciFramesFromIf_Type = Counter32
_MscFrNniUnknownDlciFramesFromIf_Object = MibTableColumn
mscFrNniUnknownDlciFramesFromIf = _MscFrNniUnknownDlciFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 12, 1, 2),
    _MscFrNniUnknownDlciFramesFromIf_Type()
)
mscFrNniUnknownDlciFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniUnknownDlciFramesFromIf.setStatus("mandatory")
_MscFrNniInvalidHeaderFramesFromIf_Type = Counter32
_MscFrNniInvalidHeaderFramesFromIf_Object = MibTableColumn
mscFrNniInvalidHeaderFramesFromIf = _MscFrNniInvalidHeaderFramesFromIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 12, 1, 3),
    _MscFrNniInvalidHeaderFramesFromIf_Type()
)
mscFrNniInvalidHeaderFramesFromIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniInvalidHeaderFramesFromIf.setStatus("mandatory")
_MscFrNniIfEntryTable_Object = MibTable
mscFrNniIfEntryTable = _MscFrNniIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 13)
)
if mibBuilder.loadTexts:
    mscFrNniIfEntryTable.setStatus("mandatory")
_MscFrNniIfEntryEntry_Object = MibTableRow
mscFrNniIfEntryEntry = _MscFrNniIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 13, 1)
)
mscFrNniIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniIfEntryEntry.setStatus("mandatory")


class _MscFrNniIfAdminStatus_Type(Integer32):
    """Custom type mscFrNniIfAdminStatus based on Integer32"""
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


_MscFrNniIfAdminStatus_Type.__name__ = "Integer32"
_MscFrNniIfAdminStatus_Object = MibTableColumn
mscFrNniIfAdminStatus = _MscFrNniIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 13, 1, 1),
    _MscFrNniIfAdminStatus_Type()
)
mscFrNniIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniIfAdminStatus.setStatus("mandatory")


class _MscFrNniIfIndex_Type(InterfaceIndex):
    """Custom type mscFrNniIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscFrNniIfIndex_Type.__name__ = "InterfaceIndex"
_MscFrNniIfIndex_Object = MibTableColumn
mscFrNniIfIndex = _MscFrNniIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 13, 1, 2),
    _MscFrNniIfIndex_Type()
)
mscFrNniIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniIfIndex.setStatus("mandatory")
_MscFrNniOperStatusTable_Object = MibTable
mscFrNniOperStatusTable = _MscFrNniOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 14)
)
if mibBuilder.loadTexts:
    mscFrNniOperStatusTable.setStatus("mandatory")
_MscFrNniOperStatusEntry_Object = MibTableRow
mscFrNniOperStatusEntry = _MscFrNniOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 14, 1)
)
mscFrNniOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniOperStatusEntry.setStatus("mandatory")


class _MscFrNniSnmpOperStatus_Type(Integer32):
    """Custom type mscFrNniSnmpOperStatus based on Integer32"""
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


_MscFrNniSnmpOperStatus_Type.__name__ = "Integer32"
_MscFrNniSnmpOperStatus_Object = MibTableColumn
mscFrNniSnmpOperStatus = _MscFrNniSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 14, 1, 1),
    _MscFrNniSnmpOperStatus_Type()
)
mscFrNniSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniSnmpOperStatus.setStatus("mandatory")
_MscFrNniEmissionPriorityQsTable_Object = MibTable
mscFrNniEmissionPriorityQsTable = _MscFrNniEmissionPriorityQsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 15)
)
if mibBuilder.loadTexts:
    mscFrNniEmissionPriorityQsTable.setStatus("mandatory")
_MscFrNniEmissionPriorityQsEntry_Object = MibTableRow
mscFrNniEmissionPriorityQsEntry = _MscFrNniEmissionPriorityQsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 15, 1)
)
mscFrNniEmissionPriorityQsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniEmissionPriorityQsEntry.setStatus("mandatory")


class _MscFrNniNumberOfEmissionQs_Type(Unsigned32):
    """Custom type mscFrNniNumberOfEmissionQs based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_MscFrNniNumberOfEmissionQs_Type.__name__ = "Unsigned32"
_MscFrNniNumberOfEmissionQs_Object = MibTableColumn
mscFrNniNumberOfEmissionQs = _MscFrNniNumberOfEmissionQs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 15, 1, 1),
    _MscFrNniNumberOfEmissionQs_Type()
)
mscFrNniNumberOfEmissionQs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniNumberOfEmissionQs.setStatus("mandatory")
_MscFrNniCa_ObjectIdentity = ObjectIdentity
mscFrNniCa = _MscFrNniCa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101)
)
_MscFrNniCaRowStatusTable_Object = MibTable
mscFrNniCaRowStatusTable = _MscFrNniCaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 1)
)
if mibBuilder.loadTexts:
    mscFrNniCaRowStatusTable.setStatus("mandatory")
_MscFrNniCaRowStatusEntry_Object = MibTableRow
mscFrNniCaRowStatusEntry = _MscFrNniCaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 1, 1)
)
mscFrNniCaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaRowStatusEntry.setStatus("mandatory")
_MscFrNniCaRowStatus_Type = RowStatus
_MscFrNniCaRowStatus_Object = MibTableColumn
mscFrNniCaRowStatus = _MscFrNniCaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 1, 1, 1),
    _MscFrNniCaRowStatus_Type()
)
mscFrNniCaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaRowStatus.setStatus("mandatory")
_MscFrNniCaComponentName_Type = DisplayString
_MscFrNniCaComponentName_Object = MibTableColumn
mscFrNniCaComponentName = _MscFrNniCaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 1, 1, 2),
    _MscFrNniCaComponentName_Type()
)
mscFrNniCaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaComponentName.setStatus("mandatory")
_MscFrNniCaStorageType_Type = StorageType
_MscFrNniCaStorageType_Object = MibTableColumn
mscFrNniCaStorageType = _MscFrNniCaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 1, 1, 4),
    _MscFrNniCaStorageType_Type()
)
mscFrNniCaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaStorageType.setStatus("mandatory")
_MscFrNniCaIndex_Type = NonReplicated
_MscFrNniCaIndex_Object = MibTableColumn
mscFrNniCaIndex = _MscFrNniCaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 1, 1, 10),
    _MscFrNniCaIndex_Type()
)
mscFrNniCaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaIndex.setStatus("mandatory")
_MscFrNniCaTpm_ObjectIdentity = ObjectIdentity
mscFrNniCaTpm = _MscFrNniCaTpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2)
)
_MscFrNniCaTpmRowStatusTable_Object = MibTable
mscFrNniCaTpmRowStatusTable = _MscFrNniCaTpmRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 1)
)
if mibBuilder.loadTexts:
    mscFrNniCaTpmRowStatusTable.setStatus("mandatory")
_MscFrNniCaTpmRowStatusEntry_Object = MibTableRow
mscFrNniCaTpmRowStatusEntry = _MscFrNniCaTpmRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 1, 1)
)
mscFrNniCaTpmRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaTpmIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaTpmRowStatusEntry.setStatus("mandatory")
_MscFrNniCaTpmRowStatus_Type = RowStatus
_MscFrNniCaTpmRowStatus_Object = MibTableColumn
mscFrNniCaTpmRowStatus = _MscFrNniCaTpmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 1, 1, 1),
    _MscFrNniCaTpmRowStatus_Type()
)
mscFrNniCaTpmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaTpmRowStatus.setStatus("mandatory")
_MscFrNniCaTpmComponentName_Type = DisplayString
_MscFrNniCaTpmComponentName_Object = MibTableColumn
mscFrNniCaTpmComponentName = _MscFrNniCaTpmComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 1, 1, 2),
    _MscFrNniCaTpmComponentName_Type()
)
mscFrNniCaTpmComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaTpmComponentName.setStatus("mandatory")
_MscFrNniCaTpmStorageType_Type = StorageType
_MscFrNniCaTpmStorageType_Object = MibTableColumn
mscFrNniCaTpmStorageType = _MscFrNniCaTpmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 1, 1, 4),
    _MscFrNniCaTpmStorageType_Type()
)
mscFrNniCaTpmStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaTpmStorageType.setStatus("mandatory")


class _MscFrNniCaTpmIndex_Type(Integer32):
    """Custom type mscFrNniCaTpmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaTpmIndex_Type.__name__ = "Integer32"
_MscFrNniCaTpmIndex_Object = MibTableColumn
mscFrNniCaTpmIndex = _MscFrNniCaTpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 1, 1, 10),
    _MscFrNniCaTpmIndex_Type()
)
mscFrNniCaTpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaTpmIndex.setStatus("mandatory")
_MscFrNniCaTpmProvTable_Object = MibTable
mscFrNniCaTpmProvTable = _MscFrNniCaTpmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 10)
)
if mibBuilder.loadTexts:
    mscFrNniCaTpmProvTable.setStatus("mandatory")
_MscFrNniCaTpmProvEntry_Object = MibTableRow
mscFrNniCaTpmProvEntry = _MscFrNniCaTpmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 10, 1)
)
mscFrNniCaTpmProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaTpmIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaTpmProvEntry.setStatus("mandatory")


class _MscFrNniCaTpmAssignedIngressBandwidthPool_Type(Unsigned32):
    """Custom type mscFrNniCaTpmAssignedIngressBandwidthPool based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(16, 16),
    )


_MscFrNniCaTpmAssignedIngressBandwidthPool_Type.__name__ = "Unsigned32"
_MscFrNniCaTpmAssignedIngressBandwidthPool_Object = MibTableColumn
mscFrNniCaTpmAssignedIngressBandwidthPool = _MscFrNniCaTpmAssignedIngressBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 10, 1, 2),
    _MscFrNniCaTpmAssignedIngressBandwidthPool_Type()
)
mscFrNniCaTpmAssignedIngressBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaTpmAssignedIngressBandwidthPool.setStatus("mandatory")


class _MscFrNniCaTpmAssignedEgressBandwidthPool_Type(Unsigned32):
    """Custom type mscFrNniCaTpmAssignedEgressBandwidthPool based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(16, 16),
    )


_MscFrNniCaTpmAssignedEgressBandwidthPool_Type.__name__ = "Unsigned32"
_MscFrNniCaTpmAssignedEgressBandwidthPool_Object = MibTableColumn
mscFrNniCaTpmAssignedEgressBandwidthPool = _MscFrNniCaTpmAssignedEgressBandwidthPool_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 2, 10, 1, 3),
    _MscFrNniCaTpmAssignedEgressBandwidthPool_Type()
)
mscFrNniCaTpmAssignedEgressBandwidthPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaTpmAssignedEgressBandwidthPool.setStatus("mandatory")
_MscFrNniCaProvTable_Object = MibTable
mscFrNniCaProvTable = _MscFrNniCaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 10)
)
if mibBuilder.loadTexts:
    mscFrNniCaProvTable.setStatus("mandatory")
_MscFrNniCaProvEntry_Object = MibTableRow
mscFrNniCaProvEntry = _MscFrNniCaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 10, 1)
)
mscFrNniCaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaProvEntry.setStatus("mandatory")


class _MscFrNniCaOverrideLinkRate_Type(Unsigned32):
    """Custom type mscFrNniCaOverrideLinkRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496729),
    )


_MscFrNniCaOverrideLinkRate_Type.__name__ = "Unsigned32"
_MscFrNniCaOverrideLinkRate_Object = MibTableColumn
mscFrNniCaOverrideLinkRate = _MscFrNniCaOverrideLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 10, 1, 2),
    _MscFrNniCaOverrideLinkRate_Type()
)
mscFrNniCaOverrideLinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaOverrideLinkRate.setStatus("mandatory")


class _MscFrNniCaMaximumBandwidthPerCall_Type(Unsigned32):
    """Custom type mscFrNniCaMaximumBandwidthPerCall based on Unsigned32"""
    defaultValue = 520000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrNniCaMaximumBandwidthPerCall_Type.__name__ = "Unsigned32"
_MscFrNniCaMaximumBandwidthPerCall_Object = MibTableColumn
mscFrNniCaMaximumBandwidthPerCall = _MscFrNniCaMaximumBandwidthPerCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 10, 1, 3),
    _MscFrNniCaMaximumBandwidthPerCall_Type()
)
mscFrNniCaMaximumBandwidthPerCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaMaximumBandwidthPerCall.setStatus("mandatory")
_MscFrNniCaIngressCacTable_Object = MibTable
mscFrNniCaIngressCacTable = _MscFrNniCaIngressCacTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 11)
)
if mibBuilder.loadTexts:
    mscFrNniCaIngressCacTable.setStatus("mandatory")
_MscFrNniCaIngressCacEntry_Object = MibTableRow
mscFrNniCaIngressCacEntry = _MscFrNniCaIngressCacEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 11, 1)
)
mscFrNniCaIngressCacEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaIngressCacEntry.setStatus("mandatory")


class _MscFrNniCaIngressApplyToCos_Type(Integer32):
    """Custom type mscFrNniCaIngressApplyToCos based on Integer32"""
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


_MscFrNniCaIngressApplyToCos_Type.__name__ = "Integer32"
_MscFrNniCaIngressApplyToCos_Object = MibTableColumn
mscFrNniCaIngressApplyToCos = _MscFrNniCaIngressApplyToCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 11, 1, 2),
    _MscFrNniCaIngressApplyToCos_Type()
)
mscFrNniCaIngressApplyToCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaIngressApplyToCos.setStatus("mandatory")


class _MscFrNniCaIngressMaximumEirOnlyCalls_Type(Unsigned32):
    """Custom type mscFrNniCaIngressMaximumEirOnlyCalls based on Unsigned32"""
    defaultValue = 992

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrNniCaIngressMaximumEirOnlyCalls_Type.__name__ = "Unsigned32"
_MscFrNniCaIngressMaximumEirOnlyCalls_Object = MibTableColumn
mscFrNniCaIngressMaximumEirOnlyCalls = _MscFrNniCaIngressMaximumEirOnlyCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 11, 1, 4),
    _MscFrNniCaIngressMaximumEirOnlyCalls_Type()
)
mscFrNniCaIngressMaximumEirOnlyCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaIngressMaximumEirOnlyCalls.setStatus("mandatory")
_MscFrNniCaEgressCacTable_Object = MibTable
mscFrNniCaEgressCacTable = _MscFrNniCaEgressCacTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 12)
)
if mibBuilder.loadTexts:
    mscFrNniCaEgressCacTable.setStatus("mandatory")
_MscFrNniCaEgressCacEntry_Object = MibTableRow
mscFrNniCaEgressCacEntry = _MscFrNniCaEgressCacEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 12, 1)
)
mscFrNniCaEgressCacEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaEgressCacEntry.setStatus("mandatory")


class _MscFrNniCaEgressApplyToCos_Type(Integer32):
    """Custom type mscFrNniCaEgressApplyToCos based on Integer32"""
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


_MscFrNniCaEgressApplyToCos_Type.__name__ = "Integer32"
_MscFrNniCaEgressApplyToCos_Object = MibTableColumn
mscFrNniCaEgressApplyToCos = _MscFrNniCaEgressApplyToCos_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 12, 1, 2),
    _MscFrNniCaEgressApplyToCos_Type()
)
mscFrNniCaEgressApplyToCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaEgressApplyToCos.setStatus("mandatory")


class _MscFrNniCaEgressMaximumEirOnlyCalls_Type(Unsigned32):
    """Custom type mscFrNniCaEgressMaximumEirOnlyCalls based on Unsigned32"""
    defaultValue = 992

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrNniCaEgressMaximumEirOnlyCalls_Type.__name__ = "Unsigned32"
_MscFrNniCaEgressMaximumEirOnlyCalls_Object = MibTableColumn
mscFrNniCaEgressMaximumEirOnlyCalls = _MscFrNniCaEgressMaximumEirOnlyCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 12, 1, 4),
    _MscFrNniCaEgressMaximumEirOnlyCalls_Type()
)
mscFrNniCaEgressMaximumEirOnlyCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaEgressMaximumEirOnlyCalls.setStatus("mandatory")
_MscFrNniCaOpTable_Object = MibTable
mscFrNniCaOpTable = _MscFrNniCaOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 13)
)
if mibBuilder.loadTexts:
    mscFrNniCaOpTable.setStatus("mandatory")
_MscFrNniCaOpEntry_Object = MibTableRow
mscFrNniCaOpEntry = _MscFrNniCaOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 13, 1)
)
mscFrNniCaOpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaOpEntry.setStatus("mandatory")


class _MscFrNniCaLinkRate_Type(Unsigned32):
    """Custom type mscFrNniCaLinkRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrNniCaLinkRate_Type.__name__ = "Unsigned32"
_MscFrNniCaLinkRate_Object = MibTableColumn
mscFrNniCaLinkRate = _MscFrNniCaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 13, 1, 2),
    _MscFrNniCaLinkRate_Type()
)
mscFrNniCaLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaLinkRate.setStatus("mandatory")


class _MscFrNniCaNumberRejectedEgressCirPermConn_Type(Gauge32):
    """Custom type mscFrNniCaNumberRejectedEgressCirPermConn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrNniCaNumberRejectedEgressCirPermConn_Type.__name__ = "Gauge32"
_MscFrNniCaNumberRejectedEgressCirPermConn_Object = MibTableColumn
mscFrNniCaNumberRejectedEgressCirPermConn = _MscFrNniCaNumberRejectedEgressCirPermConn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 13, 1, 681),
    _MscFrNniCaNumberRejectedEgressCirPermConn_Type()
)
mscFrNniCaNumberRejectedEgressCirPermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaNumberRejectedEgressCirPermConn.setStatus("mandatory")


class _MscFrNniCaNumberRejectedEgressEirPermConn_Type(Gauge32):
    """Custom type mscFrNniCaNumberRejectedEgressEirPermConn based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 992),
    )


_MscFrNniCaNumberRejectedEgressEirPermConn_Type.__name__ = "Gauge32"
_MscFrNniCaNumberRejectedEgressEirPermConn_Object = MibTableColumn
mscFrNniCaNumberRejectedEgressEirPermConn = _MscFrNniCaNumberRejectedEgressEirPermConn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 13, 1, 682),
    _MscFrNniCaNumberRejectedEgressEirPermConn_Type()
)
mscFrNniCaNumberRejectedEgressEirPermConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaNumberRejectedEgressEirPermConn.setStatus("mandatory")
_MscFrNniCaIngCirBPTable_Object = MibTable
mscFrNniCaIngCirBPTable = _MscFrNniCaIngCirBPTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 666)
)
if mibBuilder.loadTexts:
    mscFrNniCaIngCirBPTable.setStatus("mandatory")
_MscFrNniCaIngCirBPEntry_Object = MibTableRow
mscFrNniCaIngCirBPEntry = _MscFrNniCaIngCirBPEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 666, 1)
)
mscFrNniCaIngCirBPEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIngCirBPIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaIngCirBPEntry.setStatus("mandatory")


class _MscFrNniCaIngCirBPIndex_Type(Integer32):
    """Custom type mscFrNniCaIngCirBPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaIngCirBPIndex_Type.__name__ = "Integer32"
_MscFrNniCaIngCirBPIndex_Object = MibTableColumn
mscFrNniCaIngCirBPIndex = _MscFrNniCaIngCirBPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 666, 1, 1),
    _MscFrNniCaIngCirBPIndex_Type()
)
mscFrNniCaIngCirBPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaIngCirBPIndex.setStatus("mandatory")


class _MscFrNniCaIngCirBPValue_Type(Unsigned32):
    """Custom type mscFrNniCaIngCirBPValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrNniCaIngCirBPValue_Type.__name__ = "Unsigned32"
_MscFrNniCaIngCirBPValue_Object = MibTableColumn
mscFrNniCaIngCirBPValue = _MscFrNniCaIngCirBPValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 666, 1, 2),
    _MscFrNniCaIngCirBPValue_Type()
)
mscFrNniCaIngCirBPValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaIngCirBPValue.setStatus("mandatory")
_MscFrNniCaEgCirBpTable_Object = MibTable
mscFrNniCaEgCirBpTable = _MscFrNniCaEgCirBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 667)
)
if mibBuilder.loadTexts:
    mscFrNniCaEgCirBpTable.setStatus("mandatory")
_MscFrNniCaEgCirBpEntry_Object = MibTableRow
mscFrNniCaEgCirBpEntry = _MscFrNniCaEgCirBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 667, 1)
)
mscFrNniCaEgCirBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaEgCirBpIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaEgCirBpEntry.setStatus("mandatory")


class _MscFrNniCaEgCirBpIndex_Type(Integer32):
    """Custom type mscFrNniCaEgCirBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaEgCirBpIndex_Type.__name__ = "Integer32"
_MscFrNniCaEgCirBpIndex_Object = MibTableColumn
mscFrNniCaEgCirBpIndex = _MscFrNniCaEgCirBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 667, 1, 1),
    _MscFrNniCaEgCirBpIndex_Type()
)
mscFrNniCaEgCirBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaEgCirBpIndex.setStatus("mandatory")


class _MscFrNniCaEgCirBpValue_Type(Unsigned32):
    """Custom type mscFrNniCaEgCirBpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrNniCaEgCirBpValue_Type.__name__ = "Unsigned32"
_MscFrNniCaEgCirBpValue_Object = MibTableColumn
mscFrNniCaEgCirBpValue = _MscFrNniCaEgCirBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 667, 1, 2),
    _MscFrNniCaEgCirBpValue_Type()
)
mscFrNniCaEgCirBpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaEgCirBpValue.setStatus("mandatory")
_MscFrNniCaIngCirPoolAdmitBwTable_Object = MibTable
mscFrNniCaIngCirPoolAdmitBwTable = _MscFrNniCaIngCirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 668)
)
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAdmitBwTable.setStatus("mandatory")
_MscFrNniCaIngCirPoolAdmitBwEntry_Object = MibTableRow
mscFrNniCaIngCirPoolAdmitBwEntry = _MscFrNniCaIngCirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 668, 1)
)
mscFrNniCaIngCirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIngCirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrNniCaIngCirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrNniCaIngCirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaIngCirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaIngCirPoolAdmitBwIndex_Object = MibTableColumn
mscFrNniCaIngCirPoolAdmitBwIndex = _MscFrNniCaIngCirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 668, 1, 1),
    _MscFrNniCaIngCirPoolAdmitBwIndex_Type()
)
mscFrNniCaIngCirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrNniCaIngCirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrNniCaIngCirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrNniCaIngCirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaIngCirPoolAdmitBwValue_Object = MibTableColumn
mscFrNniCaIngCirPoolAdmitBwValue = _MscFrNniCaIngCirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 668, 1, 2),
    _MscFrNniCaIngCirPoolAdmitBwValue_Type()
)
mscFrNniCaIngCirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAdmitBwValue.setStatus("mandatory")
_MscFrNniCaIngCirPoolAvailBwTable_Object = MibTable
mscFrNniCaIngCirPoolAvailBwTable = _MscFrNniCaIngCirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 669)
)
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAvailBwTable.setStatus("mandatory")
_MscFrNniCaIngCirPoolAvailBwEntry_Object = MibTableRow
mscFrNniCaIngCirPoolAvailBwEntry = _MscFrNniCaIngCirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 669, 1)
)
mscFrNniCaIngCirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIngCirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrNniCaIngCirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrNniCaIngCirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaIngCirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaIngCirPoolAvailBwIndex_Object = MibTableColumn
mscFrNniCaIngCirPoolAvailBwIndex = _MscFrNniCaIngCirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 669, 1, 1),
    _MscFrNniCaIngCirPoolAvailBwIndex_Type()
)
mscFrNniCaIngCirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrNniCaIngCirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrNniCaIngCirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrNniCaIngCirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaIngCirPoolAvailBwValue_Object = MibTableColumn
mscFrNniCaIngCirPoolAvailBwValue = _MscFrNniCaIngCirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 669, 1, 2),
    _MscFrNniCaIngCirPoolAvailBwValue_Type()
)
mscFrNniCaIngCirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaIngCirPoolAvailBwValue.setStatus("mandatory")
_MscFrNniCaEgCirPoolAdmitBwTable_Object = MibTable
mscFrNniCaEgCirPoolAdmitBwTable = _MscFrNniCaEgCirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 670)
)
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAdmitBwTable.setStatus("mandatory")
_MscFrNniCaEgCirPoolAdmitBwEntry_Object = MibTableRow
mscFrNniCaEgCirPoolAdmitBwEntry = _MscFrNniCaEgCirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 670, 1)
)
mscFrNniCaEgCirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaEgCirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrNniCaEgCirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrNniCaEgCirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaEgCirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaEgCirPoolAdmitBwIndex_Object = MibTableColumn
mscFrNniCaEgCirPoolAdmitBwIndex = _MscFrNniCaEgCirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 670, 1, 1),
    _MscFrNniCaEgCirPoolAdmitBwIndex_Type()
)
mscFrNniCaEgCirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrNniCaEgCirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrNniCaEgCirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrNniCaEgCirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaEgCirPoolAdmitBwValue_Object = MibTableColumn
mscFrNniCaEgCirPoolAdmitBwValue = _MscFrNniCaEgCirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 670, 1, 2),
    _MscFrNniCaEgCirPoolAdmitBwValue_Type()
)
mscFrNniCaEgCirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAdmitBwValue.setStatus("mandatory")
_MscFrNniCaEgCirPoolAvailBwTable_Object = MibTable
mscFrNniCaEgCirPoolAvailBwTable = _MscFrNniCaEgCirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 671)
)
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAvailBwTable.setStatus("mandatory")
_MscFrNniCaEgCirPoolAvailBwEntry_Object = MibTableRow
mscFrNniCaEgCirPoolAvailBwEntry = _MscFrNniCaEgCirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 671, 1)
)
mscFrNniCaEgCirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaEgCirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrNniCaEgCirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrNniCaEgCirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaEgCirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaEgCirPoolAvailBwIndex_Object = MibTableColumn
mscFrNniCaEgCirPoolAvailBwIndex = _MscFrNniCaEgCirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 671, 1, 1),
    _MscFrNniCaEgCirPoolAvailBwIndex_Type()
)
mscFrNniCaEgCirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrNniCaEgCirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrNniCaEgCirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrNniCaEgCirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaEgCirPoolAvailBwValue_Object = MibTableColumn
mscFrNniCaEgCirPoolAvailBwValue = _MscFrNniCaEgCirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 671, 1, 2),
    _MscFrNniCaEgCirPoolAvailBwValue_Type()
)
mscFrNniCaEgCirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaEgCirPoolAvailBwValue.setStatus("mandatory")
_MscFrNniCaIngEirBpTable_Object = MibTable
mscFrNniCaIngEirBpTable = _MscFrNniCaIngEirBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 673)
)
if mibBuilder.loadTexts:
    mscFrNniCaIngEirBpTable.setStatus("mandatory")
_MscFrNniCaIngEirBpEntry_Object = MibTableRow
mscFrNniCaIngEirBpEntry = _MscFrNniCaIngEirBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 673, 1)
)
mscFrNniCaIngEirBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIngEirBpIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaIngEirBpEntry.setStatus("mandatory")


class _MscFrNniCaIngEirBpIndex_Type(Integer32):
    """Custom type mscFrNniCaIngEirBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaIngEirBpIndex_Type.__name__ = "Integer32"
_MscFrNniCaIngEirBpIndex_Object = MibTableColumn
mscFrNniCaIngEirBpIndex = _MscFrNniCaIngEirBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 673, 1, 1),
    _MscFrNniCaIngEirBpIndex_Type()
)
mscFrNniCaIngEirBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaIngEirBpIndex.setStatus("mandatory")


class _MscFrNniCaIngEirBpValue_Type(Unsigned32):
    """Custom type mscFrNniCaIngEirBpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrNniCaIngEirBpValue_Type.__name__ = "Unsigned32"
_MscFrNniCaIngEirBpValue_Object = MibTableColumn
mscFrNniCaIngEirBpValue = _MscFrNniCaIngEirBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 673, 1, 2),
    _MscFrNniCaIngEirBpValue_Type()
)
mscFrNniCaIngEirBpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaIngEirBpValue.setStatus("mandatory")
_MscFrNniCaEgEirBpTable_Object = MibTable
mscFrNniCaEgEirBpTable = _MscFrNniCaEgEirBpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 674)
)
if mibBuilder.loadTexts:
    mscFrNniCaEgEirBpTable.setStatus("mandatory")
_MscFrNniCaEgEirBpEntry_Object = MibTableRow
mscFrNniCaEgEirBpEntry = _MscFrNniCaEgEirBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 674, 1)
)
mscFrNniCaEgEirBpEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaEgEirBpIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaEgEirBpEntry.setStatus("mandatory")


class _MscFrNniCaEgEirBpIndex_Type(Integer32):
    """Custom type mscFrNniCaEgEirBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaEgEirBpIndex_Type.__name__ = "Integer32"
_MscFrNniCaEgEirBpIndex_Object = MibTableColumn
mscFrNniCaEgEirBpIndex = _MscFrNniCaEgEirBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 674, 1, 1),
    _MscFrNniCaEgEirBpIndex_Type()
)
mscFrNniCaEgEirBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaEgEirBpIndex.setStatus("mandatory")


class _MscFrNniCaEgEirBpValue_Type(Unsigned32):
    """Custom type mscFrNniCaEgEirBpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscFrNniCaEgEirBpValue_Type.__name__ = "Unsigned32"
_MscFrNniCaEgEirBpValue_Object = MibTableColumn
mscFrNniCaEgEirBpValue = _MscFrNniCaEgEirBpValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 674, 1, 2),
    _MscFrNniCaEgEirBpValue_Type()
)
mscFrNniCaEgEirBpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFrNniCaEgEirBpValue.setStatus("mandatory")
_MscFrNniCaIngEirPoolAdmitBwTable_Object = MibTable
mscFrNniCaIngEirPoolAdmitBwTable = _MscFrNniCaIngEirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 675)
)
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAdmitBwTable.setStatus("mandatory")
_MscFrNniCaIngEirPoolAdmitBwEntry_Object = MibTableRow
mscFrNniCaIngEirPoolAdmitBwEntry = _MscFrNniCaIngEirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 675, 1)
)
mscFrNniCaIngEirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIngEirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrNniCaIngEirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrNniCaIngEirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaIngEirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaIngEirPoolAdmitBwIndex_Object = MibTableColumn
mscFrNniCaIngEirPoolAdmitBwIndex = _MscFrNniCaIngEirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 675, 1, 1),
    _MscFrNniCaIngEirPoolAdmitBwIndex_Type()
)
mscFrNniCaIngEirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrNniCaIngEirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrNniCaIngEirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrNniCaIngEirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaIngEirPoolAdmitBwValue_Object = MibTableColumn
mscFrNniCaIngEirPoolAdmitBwValue = _MscFrNniCaIngEirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 675, 1, 2),
    _MscFrNniCaIngEirPoolAdmitBwValue_Type()
)
mscFrNniCaIngEirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAdmitBwValue.setStatus("mandatory")
_MscFrNniCaIngEirPoolAvailBwTable_Object = MibTable
mscFrNniCaIngEirPoolAvailBwTable = _MscFrNniCaIngEirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 676)
)
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAvailBwTable.setStatus("mandatory")
_MscFrNniCaIngEirPoolAvailBwEntry_Object = MibTableRow
mscFrNniCaIngEirPoolAvailBwEntry = _MscFrNniCaIngEirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 676, 1)
)
mscFrNniCaIngEirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIngEirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrNniCaIngEirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrNniCaIngEirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaIngEirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaIngEirPoolAvailBwIndex_Object = MibTableColumn
mscFrNniCaIngEirPoolAvailBwIndex = _MscFrNniCaIngEirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 676, 1, 1),
    _MscFrNniCaIngEirPoolAvailBwIndex_Type()
)
mscFrNniCaIngEirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrNniCaIngEirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrNniCaIngEirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrNniCaIngEirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaIngEirPoolAvailBwValue_Object = MibTableColumn
mscFrNniCaIngEirPoolAvailBwValue = _MscFrNniCaIngEirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 676, 1, 2),
    _MscFrNniCaIngEirPoolAvailBwValue_Type()
)
mscFrNniCaIngEirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaIngEirPoolAvailBwValue.setStatus("mandatory")
_MscFrNniCaEgEirPoolAdmitBwTable_Object = MibTable
mscFrNniCaEgEirPoolAdmitBwTable = _MscFrNniCaEgEirPoolAdmitBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 677)
)
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAdmitBwTable.setStatus("mandatory")
_MscFrNniCaEgEirPoolAdmitBwEntry_Object = MibTableRow
mscFrNniCaEgEirPoolAdmitBwEntry = _MscFrNniCaEgEirPoolAdmitBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 677, 1)
)
mscFrNniCaEgEirPoolAdmitBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaEgEirPoolAdmitBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAdmitBwEntry.setStatus("mandatory")


class _MscFrNniCaEgEirPoolAdmitBwIndex_Type(Integer32):
    """Custom type mscFrNniCaEgEirPoolAdmitBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaEgEirPoolAdmitBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaEgEirPoolAdmitBwIndex_Object = MibTableColumn
mscFrNniCaEgEirPoolAdmitBwIndex = _MscFrNniCaEgEirPoolAdmitBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 677, 1, 1),
    _MscFrNniCaEgEirPoolAdmitBwIndex_Type()
)
mscFrNniCaEgEirPoolAdmitBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAdmitBwIndex.setStatus("mandatory")


class _MscFrNniCaEgEirPoolAdmitBwValue_Type(Gauge32):
    """Custom type mscFrNniCaEgEirPoolAdmitBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 520000000),
    )


_MscFrNniCaEgEirPoolAdmitBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaEgEirPoolAdmitBwValue_Object = MibTableColumn
mscFrNniCaEgEirPoolAdmitBwValue = _MscFrNniCaEgEirPoolAdmitBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 677, 1, 2),
    _MscFrNniCaEgEirPoolAdmitBwValue_Type()
)
mscFrNniCaEgEirPoolAdmitBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAdmitBwValue.setStatus("mandatory")
_MscFrNniCaEgEirPoolAvailBwTable_Object = MibTable
mscFrNniCaEgEirPoolAvailBwTable = _MscFrNniCaEgEirPoolAvailBwTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 678)
)
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAvailBwTable.setStatus("mandatory")
_MscFrNniCaEgEirPoolAvailBwEntry_Object = MibTableRow
mscFrNniCaEgEirPoolAvailBwEntry = _MscFrNniCaEgEirPoolAvailBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 678, 1)
)
mscFrNniCaEgEirPoolAvailBwEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniCaEgEirPoolAvailBwIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAvailBwEntry.setStatus("mandatory")


class _MscFrNniCaEgEirPoolAvailBwIndex_Type(Integer32):
    """Custom type mscFrNniCaEgEirPoolAvailBwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFrNniCaEgEirPoolAvailBwIndex_Type.__name__ = "Integer32"
_MscFrNniCaEgEirPoolAvailBwIndex_Object = MibTableColumn
mscFrNniCaEgEirPoolAvailBwIndex = _MscFrNniCaEgEirPoolAvailBwIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 678, 1, 1),
    _MscFrNniCaEgEirPoolAvailBwIndex_Type()
)
mscFrNniCaEgEirPoolAvailBwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAvailBwIndex.setStatus("mandatory")


class _MscFrNniCaEgEirPoolAvailBwValue_Type(Gauge32):
    """Custom type mscFrNniCaEgEirPoolAvailBwValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_MscFrNniCaEgEirPoolAvailBwValue_Type.__name__ = "Gauge32"
_MscFrNniCaEgEirPoolAvailBwValue_Object = MibTableColumn
mscFrNniCaEgEirPoolAvailBwValue = _MscFrNniCaEgEirPoolAvailBwValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 101, 678, 1, 2),
    _MscFrNniCaEgEirPoolAvailBwValue_Type()
)
mscFrNniCaEgEirPoolAvailBwValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniCaEgEirPoolAvailBwValue.setStatus("mandatory")
_MscFrNniFrmToIfByQueueTable_Object = MibTable
mscFrNniFrmToIfByQueueTable = _MscFrNniFrmToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 341)
)
if mibBuilder.loadTexts:
    mscFrNniFrmToIfByQueueTable.setStatus("mandatory")
_MscFrNniFrmToIfByQueueEntry_Object = MibTableRow
mscFrNniFrmToIfByQueueEntry = _MscFrNniFrmToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 341, 1)
)
mscFrNniFrmToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniFrmToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniFrmToIfByQueueEntry.setStatus("mandatory")


class _MscFrNniFrmToIfByQueueIndex_Type(Integer32):
    """Custom type mscFrNniFrmToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrNniFrmToIfByQueueIndex_Type.__name__ = "Integer32"
_MscFrNniFrmToIfByQueueIndex_Object = MibTableColumn
mscFrNniFrmToIfByQueueIndex = _MscFrNniFrmToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 341, 1, 1),
    _MscFrNniFrmToIfByQueueIndex_Type()
)
mscFrNniFrmToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniFrmToIfByQueueIndex.setStatus("mandatory")


class _MscFrNniFrmToIfByQueueValue_Type(Unsigned32):
    """Custom type mscFrNniFrmToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniFrmToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscFrNniFrmToIfByQueueValue_Object = MibTableColumn
mscFrNniFrmToIfByQueueValue = _MscFrNniFrmToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 341, 1, 2),
    _MscFrNniFrmToIfByQueueValue_Type()
)
mscFrNniFrmToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniFrmToIfByQueueValue.setStatus("mandatory")
_MscFrNniOctetToIfByQueueTable_Object = MibTable
mscFrNniOctetToIfByQueueTable = _MscFrNniOctetToIfByQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 342)
)
if mibBuilder.loadTexts:
    mscFrNniOctetToIfByQueueTable.setStatus("mandatory")
_MscFrNniOctetToIfByQueueEntry_Object = MibTableRow
mscFrNniOctetToIfByQueueEntry = _MscFrNniOctetToIfByQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 342, 1)
)
mscFrNniOctetToIfByQueueEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniOctetToIfByQueueIndex"),
)
if mibBuilder.loadTexts:
    mscFrNniOctetToIfByQueueEntry.setStatus("mandatory")


class _MscFrNniOctetToIfByQueueIndex_Type(Integer32):
    """Custom type mscFrNniOctetToIfByQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MscFrNniOctetToIfByQueueIndex_Type.__name__ = "Integer32"
_MscFrNniOctetToIfByQueueIndex_Object = MibTableColumn
mscFrNniOctetToIfByQueueIndex = _MscFrNniOctetToIfByQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 342, 1, 1),
    _MscFrNniOctetToIfByQueueIndex_Type()
)
mscFrNniOctetToIfByQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFrNniOctetToIfByQueueIndex.setStatus("mandatory")


class _MscFrNniOctetToIfByQueueValue_Type(Unsigned32):
    """Custom type mscFrNniOctetToIfByQueueValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFrNniOctetToIfByQueueValue_Type.__name__ = "Unsigned32"
_MscFrNniOctetToIfByQueueValue_Object = MibTableColumn
mscFrNniOctetToIfByQueueValue = _MscFrNniOctetToIfByQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 342, 1, 2),
    _MscFrNniOctetToIfByQueueValue_Type()
)
mscFrNniOctetToIfByQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFrNniOctetToIfByQueueValue.setStatus("mandatory")
_FrameRelayNniMIB_ObjectIdentity = ObjectIdentity
frameRelayNniMIB = _FrameRelayNniMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23)
)
_FrameRelayNniGroup_ObjectIdentity = ObjectIdentity
frameRelayNniGroup = _FrameRelayNniGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 1)
)
_FrameRelayNniGroupCA_ObjectIdentity = ObjectIdentity
frameRelayNniGroupCA = _FrameRelayNniGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 1, 1)
)
_FrameRelayNniGroupCA02_ObjectIdentity = ObjectIdentity
frameRelayNniGroupCA02 = _FrameRelayNniGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 1, 1, 3)
)
_FrameRelayNniGroupCA02A_ObjectIdentity = ObjectIdentity
frameRelayNniGroupCA02A = _FrameRelayNniGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 1, 1, 3, 2)
)
_FrameRelayNniCapabilities_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilities = _FrameRelayNniCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 3)
)
_FrameRelayNniCapabilitiesCA_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilitiesCA = _FrameRelayNniCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 3, 1)
)
_FrameRelayNniCapabilitiesCA02_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilitiesCA02 = _FrameRelayNniCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 3, 1, 3)
)
_FrameRelayNniCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
frameRelayNniCapabilitiesCA02A = _FrameRelayNniCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 23, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB",
    **{"mscFrNni": mscFrNni,
       "mscFrNniRowStatusTable": mscFrNniRowStatusTable,
       "mscFrNniRowStatusEntry": mscFrNniRowStatusEntry,
       "mscFrNniRowStatus": mscFrNniRowStatus,
       "mscFrNniComponentName": mscFrNniComponentName,
       "mscFrNniStorageType": mscFrNniStorageType,
       "mscFrNniIndex": mscFrNniIndex,
       "mscFrNniDna": mscFrNniDna,
       "mscFrNniDnaRowStatusTable": mscFrNniDnaRowStatusTable,
       "mscFrNniDnaRowStatusEntry": mscFrNniDnaRowStatusEntry,
       "mscFrNniDnaRowStatus": mscFrNniDnaRowStatus,
       "mscFrNniDnaComponentName": mscFrNniDnaComponentName,
       "mscFrNniDnaStorageType": mscFrNniDnaStorageType,
       "mscFrNniDnaIndex": mscFrNniDnaIndex,
       "mscFrNniDnaCug": mscFrNniDnaCug,
       "mscFrNniDnaCugRowStatusTable": mscFrNniDnaCugRowStatusTable,
       "mscFrNniDnaCugRowStatusEntry": mscFrNniDnaCugRowStatusEntry,
       "mscFrNniDnaCugRowStatus": mscFrNniDnaCugRowStatus,
       "mscFrNniDnaCugComponentName": mscFrNniDnaCugComponentName,
       "mscFrNniDnaCugStorageType": mscFrNniDnaCugStorageType,
       "mscFrNniDnaCugIndex": mscFrNniDnaCugIndex,
       "mscFrNniDnaCugCugOptionsTable": mscFrNniDnaCugCugOptionsTable,
       "mscFrNniDnaCugCugOptionsEntry": mscFrNniDnaCugCugOptionsEntry,
       "mscFrNniDnaCugType": mscFrNniDnaCugType,
       "mscFrNniDnaCugDnic": mscFrNniDnaCugDnic,
       "mscFrNniDnaCugInterlockCode": mscFrNniDnaCugInterlockCode,
       "mscFrNniDnaCugPreferential": mscFrNniDnaCugPreferential,
       "mscFrNniDnaCugOutCalls": mscFrNniDnaCugOutCalls,
       "mscFrNniDnaCugIncCalls": mscFrNniDnaCugIncCalls,
       "mscFrNniDnaHgM": mscFrNniDnaHgM,
       "mscFrNniDnaHgMRowStatusTable": mscFrNniDnaHgMRowStatusTable,
       "mscFrNniDnaHgMRowStatusEntry": mscFrNniDnaHgMRowStatusEntry,
       "mscFrNniDnaHgMRowStatus": mscFrNniDnaHgMRowStatus,
       "mscFrNniDnaHgMComponentName": mscFrNniDnaHgMComponentName,
       "mscFrNniDnaHgMStorageType": mscFrNniDnaHgMStorageType,
       "mscFrNniDnaHgMIndex": mscFrNniDnaHgMIndex,
       "mscFrNniDnaHgMHgAddr": mscFrNniDnaHgMHgAddr,
       "mscFrNniDnaHgMHgAddrRowStatusTable": mscFrNniDnaHgMHgAddrRowStatusTable,
       "mscFrNniDnaHgMHgAddrRowStatusEntry": mscFrNniDnaHgMHgAddrRowStatusEntry,
       "mscFrNniDnaHgMHgAddrRowStatus": mscFrNniDnaHgMHgAddrRowStatus,
       "mscFrNniDnaHgMHgAddrComponentName": mscFrNniDnaHgMHgAddrComponentName,
       "mscFrNniDnaHgMHgAddrStorageType": mscFrNniDnaHgMHgAddrStorageType,
       "mscFrNniDnaHgMHgAddrIndex": mscFrNniDnaHgMHgAddrIndex,
       "mscFrNniDnaHgMHgAddrAddrTable": mscFrNniDnaHgMHgAddrAddrTable,
       "mscFrNniDnaHgMHgAddrAddrEntry": mscFrNniDnaHgMHgAddrAddrEntry,
       "mscFrNniDnaHgMHgAddrNumberingPlanIndicator": mscFrNniDnaHgMHgAddrNumberingPlanIndicator,
       "mscFrNniDnaHgMHgAddrDataNetworkAddress": mscFrNniDnaHgMHgAddrDataNetworkAddress,
       "mscFrNniDnaHgMIfTable": mscFrNniDnaHgMIfTable,
       "mscFrNniDnaHgMIfEntry": mscFrNniDnaHgMIfEntry,
       "mscFrNniDnaHgMAvailabilityUpdateThreshold": mscFrNniDnaHgMAvailabilityUpdateThreshold,
       "mscFrNniDnaHgMOpTable": mscFrNniDnaHgMOpTable,
       "mscFrNniDnaHgMOpEntry": mscFrNniDnaHgMOpEntry,
       "mscFrNniDnaHgMMaximumAvailableAggregateCir": mscFrNniDnaHgMMaximumAvailableAggregateCir,
       "mscFrNniDnaHgMAvailableAggregateCir": mscFrNniDnaHgMAvailableAggregateCir,
       "mscFrNniDnaHgMAvailabilityDelta": mscFrNniDnaHgMAvailabilityDelta,
       "mscFrNniDnaHgMAvailableDlcis": mscFrNniDnaHgMAvailableDlcis,
       "mscFrNniDnaHgMMaximumAvailableAggregateCir64": mscFrNniDnaHgMMaximumAvailableAggregateCir64,
       "mscFrNniDnaHgMAvailableAggregateCir64": mscFrNniDnaHgMAvailableAggregateCir64,
       "mscFrNniDnaAddressTable": mscFrNniDnaAddressTable,
       "mscFrNniDnaAddressEntry": mscFrNniDnaAddressEntry,
       "mscFrNniDnaNumberingPlanIndicator": mscFrNniDnaNumberingPlanIndicator,
       "mscFrNniDnaDataNetworkAddress": mscFrNniDnaDataNetworkAddress,
       "mscFrNniDnaOutgoingOptionsTable": mscFrNniDnaOutgoingOptionsTable,
       "mscFrNniDnaOutgoingOptionsEntry": mscFrNniDnaOutgoingOptionsEntry,
       "mscFrNniDnaOutDefaultPriority": mscFrNniDnaOutDefaultPriority,
       "mscFrNniDnaOutDefaultPathSensitivity": mscFrNniDnaOutDefaultPathSensitivity,
       "mscFrNniDnaOutPathSensitivityOverRide": mscFrNniDnaOutPathSensitivityOverRide,
       "mscFrNniDnaOutDefaultPathReliability": mscFrNniDnaOutDefaultPathReliability,
       "mscFrNniDnaOutAccess": mscFrNniDnaOutAccess,
       "mscFrNniDnaDefaultTransferPriority": mscFrNniDnaDefaultTransferPriority,
       "mscFrNniDnaTransferPriorityOverRide": mscFrNniDnaTransferPriorityOverRide,
       "mscFrNniDnaIncomingOptionsTable": mscFrNniDnaIncomingOptionsTable,
       "mscFrNniDnaIncomingOptionsEntry": mscFrNniDnaIncomingOptionsEntry,
       "mscFrNniDnaIncAccess": mscFrNniDnaIncAccess,
       "mscFrNniDnaCallOptionsTable": mscFrNniDnaCallOptionsTable,
       "mscFrNniDnaCallOptionsEntry": mscFrNniDnaCallOptionsEntry,
       "mscFrNniDnaAccountClass": mscFrNniDnaAccountClass,
       "mscFrNniDnaAccountCollection": mscFrNniDnaAccountCollection,
       "mscFrNniDnaServiceExchange": mscFrNniDnaServiceExchange,
       "mscFrNniDnaEgressAccounting": mscFrNniDnaEgressAccounting,
       "mscFrNniDnaDataPath": mscFrNniDnaDataPath,
       "mscFrNniFramer": mscFrNniFramer,
       "mscFrNniFramerRowStatusTable": mscFrNniFramerRowStatusTable,
       "mscFrNniFramerRowStatusEntry": mscFrNniFramerRowStatusEntry,
       "mscFrNniFramerRowStatus": mscFrNniFramerRowStatus,
       "mscFrNniFramerComponentName": mscFrNniFramerComponentName,
       "mscFrNniFramerStorageType": mscFrNniFramerStorageType,
       "mscFrNniFramerIndex": mscFrNniFramerIndex,
       "mscFrNniFramerProvTable": mscFrNniFramerProvTable,
       "mscFrNniFramerProvEntry": mscFrNniFramerProvEntry,
       "mscFrNniFramerInterfaceName": mscFrNniFramerInterfaceName,
       "mscFrNniFramerLinkTable": mscFrNniFramerLinkTable,
       "mscFrNniFramerLinkEntry": mscFrNniFramerLinkEntry,
       "mscFrNniFramerDataInversion": mscFrNniFramerDataInversion,
       "mscFrNniFramerFrameCrcType": mscFrNniFramerFrameCrcType,
       "mscFrNniFramerFlagsBetweenFrames": mscFrNniFramerFlagsBetweenFrames,
       "mscFrNniFramerStateTable": mscFrNniFramerStateTable,
       "mscFrNniFramerStateEntry": mscFrNniFramerStateEntry,
       "mscFrNniFramerAdminState": mscFrNniFramerAdminState,
       "mscFrNniFramerOperationalState": mscFrNniFramerOperationalState,
       "mscFrNniFramerUsageState": mscFrNniFramerUsageState,
       "mscFrNniFramerStatsTable": mscFrNniFramerStatsTable,
       "mscFrNniFramerStatsEntry": mscFrNniFramerStatsEntry,
       "mscFrNniFramerFrmToIf": mscFrNniFramerFrmToIf,
       "mscFrNniFramerFrmFromIf": mscFrNniFramerFrmFromIf,
       "mscFrNniFramerOctetFromIf": mscFrNniFramerOctetFromIf,
       "mscFrNniFramerAborts": mscFrNniFramerAborts,
       "mscFrNniFramerCrcErrors": mscFrNniFramerCrcErrors,
       "mscFrNniFramerLrcErrors": mscFrNniFramerLrcErrors,
       "mscFrNniFramerNonOctetErrors": mscFrNniFramerNonOctetErrors,
       "mscFrNniFramerOverruns": mscFrNniFramerOverruns,
       "mscFrNniFramerUnderruns": mscFrNniFramerUnderruns,
       "mscFrNniFramerLargeFrmErrors": mscFrNniFramerLargeFrmErrors,
       "mscFrNniFramerFrmModeErrors": mscFrNniFramerFrmModeErrors,
       "mscFrNniFramerFrmToIf64": mscFrNniFramerFrmToIf64,
       "mscFrNniFramerFrmFromIf64": mscFrNniFramerFrmFromIf64,
       "mscFrNniFramerOctetFromIf64": mscFrNniFramerOctetFromIf64,
       "mscFrNniFramerUtilTable": mscFrNniFramerUtilTable,
       "mscFrNniFramerUtilEntry": mscFrNniFramerUtilEntry,
       "mscFrNniFramerNormPrioLinkUtilToIf": mscFrNniFramerNormPrioLinkUtilToIf,
       "mscFrNniFramerNormPrioLinkUtilFromIf": mscFrNniFramerNormPrioLinkUtilFromIf,
       "mscFrNniLmi": mscFrNniLmi,
       "mscFrNniLmiRowStatusTable": mscFrNniLmiRowStatusTable,
       "mscFrNniLmiRowStatusEntry": mscFrNniLmiRowStatusEntry,
       "mscFrNniLmiRowStatus": mscFrNniLmiRowStatus,
       "mscFrNniLmiComponentName": mscFrNniLmiComponentName,
       "mscFrNniLmiStorageType": mscFrNniLmiStorageType,
       "mscFrNniLmiIndex": mscFrNniLmiIndex,
       "mscFrNniLmiParmsTable": mscFrNniLmiParmsTable,
       "mscFrNniLmiParmsEntry": mscFrNniLmiParmsEntry,
       "mscFrNniLmiProcedures": mscFrNniLmiProcedures,
       "mscFrNniLmiAsyncStatusReport": mscFrNniLmiAsyncStatusReport,
       "mscFrNniLmiErrorEventThreshold": mscFrNniLmiErrorEventThreshold,
       "mscFrNniLmiEventCount": mscFrNniLmiEventCount,
       "mscFrNniLmiCheckPointTimer": mscFrNniLmiCheckPointTimer,
       "mscFrNniLmiIgnoreActiveBit": mscFrNniLmiIgnoreActiveBit,
       "mscFrNniLmiNniParmsTable": mscFrNniLmiNniParmsTable,
       "mscFrNniLmiNniParmsEntry": mscFrNniLmiNniParmsEntry,
       "mscFrNniLmiFullStatusPollingCycles": mscFrNniLmiFullStatusPollingCycles,
       "mscFrNniLmiLinkVerificationTimer": mscFrNniLmiLinkVerificationTimer,
       "mscFrNniLmiStateTable": mscFrNniLmiStateTable,
       "mscFrNniLmiStateEntry": mscFrNniLmiStateEntry,
       "mscFrNniLmiAdminState": mscFrNniLmiAdminState,
       "mscFrNniLmiOperationalState": mscFrNniLmiOperationalState,
       "mscFrNniLmiUsageState": mscFrNniLmiUsageState,
       "mscFrNniLmiPsiTable": mscFrNniLmiPsiTable,
       "mscFrNniLmiPsiEntry": mscFrNniLmiPsiEntry,
       "mscFrNniLmiProtocolStatus": mscFrNniLmiProtocolStatus,
       "mscFrNniLmiOpProcedures": mscFrNniLmiOpProcedures,
       "mscFrNniLmiStatsTable": mscFrNniLmiStatsTable,
       "mscFrNniLmiStatsEntry": mscFrNniLmiStatsEntry,
       "mscFrNniLmiKeepAliveStatusToIf": mscFrNniLmiKeepAliveStatusToIf,
       "mscFrNniLmiFullStatusToIf": mscFrNniLmiFullStatusToIf,
       "mscFrNniLmiKeepAliveStatusEnqFromIf": mscFrNniLmiKeepAliveStatusEnqFromIf,
       "mscFrNniLmiFullStatusEnqFromIf": mscFrNniLmiFullStatusEnqFromIf,
       "mscFrNniLmiNetworkSideEventHistory": mscFrNniLmiNetworkSideEventHistory,
       "mscFrNniLmiUserSideEventHistory": mscFrNniLmiUserSideEventHistory,
       "mscFrNniLmiProtocolErrors": mscFrNniLmiProtocolErrors,
       "mscFrNniLmiUnexpectedIes": mscFrNniLmiUnexpectedIes,
       "mscFrNniLmiSequenceErrors": mscFrNniLmiSequenceErrors,
       "mscFrNniLmiStatusSequenceErrors": mscFrNniLmiStatusSequenceErrors,
       "mscFrNniLmiUnexpectedReports": mscFrNniLmiUnexpectedReports,
       "mscFrNniLmiPollingVerifTimeouts": mscFrNniLmiPollingVerifTimeouts,
       "mscFrNniLmiNoStatusReportCount": mscFrNniLmiNoStatusReportCount,
       "mscFrNniDlci": mscFrNniDlci,
       "mscFrNniDlciRowStatusTable": mscFrNniDlciRowStatusTable,
       "mscFrNniDlciRowStatusEntry": mscFrNniDlciRowStatusEntry,
       "mscFrNniDlciRowStatus": mscFrNniDlciRowStatus,
       "mscFrNniDlciComponentName": mscFrNniDlciComponentName,
       "mscFrNniDlciStorageType": mscFrNniDlciStorageType,
       "mscFrNniDlciIndex": mscFrNniDlciIndex,
       "mscFrNniDlciDc": mscFrNniDlciDc,
       "mscFrNniDlciDcRowStatusTable": mscFrNniDlciDcRowStatusTable,
       "mscFrNniDlciDcRowStatusEntry": mscFrNniDlciDcRowStatusEntry,
       "mscFrNniDlciDcRowStatus": mscFrNniDlciDcRowStatus,
       "mscFrNniDlciDcComponentName": mscFrNniDlciDcComponentName,
       "mscFrNniDlciDcStorageType": mscFrNniDlciDcStorageType,
       "mscFrNniDlciDcIndex": mscFrNniDlciDcIndex,
       "mscFrNniDlciDcOptionsTable": mscFrNniDlciDcOptionsTable,
       "mscFrNniDlciDcOptionsEntry": mscFrNniDlciDcOptionsEntry,
       "mscFrNniDlciDcRemoteNpi": mscFrNniDlciDcRemoteNpi,
       "mscFrNniDlciDcRemoteDna": mscFrNniDlciDcRemoteDna,
       "mscFrNniDlciDcRemoteDlci": mscFrNniDlciDcRemoteDlci,
       "mscFrNniDlciDcType": mscFrNniDlciDcType,
       "mscFrNniDlciDcTransferPriority": mscFrNniDlciDcTransferPriority,
       "mscFrNniDlciDcDiscardPriority": mscFrNniDlciDcDiscardPriority,
       "mscFrNniDlciDcDeDiscardPriority": mscFrNniDlciDcDeDiscardPriority,
       "mscFrNniDlciDcDataPath": mscFrNniDlciDcDataPath,
       "mscFrNniDlciDcCugIndex": mscFrNniDlciDcCugIndex,
       "mscFrNniDlciDcCugType": mscFrNniDlciDcCugType,
       "mscFrNniDlciDcMapIpCosToFrQos": mscFrNniDlciDcMapIpCosToFrQos,
       "mscFrNniDlciDcNfaTable": mscFrNniDlciDcNfaTable,
       "mscFrNniDlciDcNfaEntry": mscFrNniDlciDcNfaEntry,
       "mscFrNniDlciDcNfaIndex": mscFrNniDlciDcNfaIndex,
       "mscFrNniDlciDcNfaValue": mscFrNniDlciDcNfaValue,
       "mscFrNniDlciDcNfaRowStatus": mscFrNniDlciDcNfaRowStatus,
       "mscFrNniDlciVc": mscFrNniDlciVc,
       "mscFrNniDlciVcRowStatusTable": mscFrNniDlciVcRowStatusTable,
       "mscFrNniDlciVcRowStatusEntry": mscFrNniDlciVcRowStatusEntry,
       "mscFrNniDlciVcRowStatus": mscFrNniDlciVcRowStatus,
       "mscFrNniDlciVcComponentName": mscFrNniDlciVcComponentName,
       "mscFrNniDlciVcStorageType": mscFrNniDlciVcStorageType,
       "mscFrNniDlciVcIndex": mscFrNniDlciVcIndex,
       "mscFrNniDlciVcCadTable": mscFrNniDlciVcCadTable,
       "mscFrNniDlciVcCadEntry": mscFrNniDlciVcCadEntry,
       "mscFrNniDlciVcType": mscFrNniDlciVcType,
       "mscFrNniDlciVcState": mscFrNniDlciVcState,
       "mscFrNniDlciVcPreviousState": mscFrNniDlciVcPreviousState,
       "mscFrNniDlciVcDiagnosticCode": mscFrNniDlciVcDiagnosticCode,
       "mscFrNniDlciVcPreviousDiagnosticCode": mscFrNniDlciVcPreviousDiagnosticCode,
       "mscFrNniDlciVcCalledNpi": mscFrNniDlciVcCalledNpi,
       "mscFrNniDlciVcCalledDna": mscFrNniDlciVcCalledDna,
       "mscFrNniDlciVcCalledLcn": mscFrNniDlciVcCalledLcn,
       "mscFrNniDlciVcCallingNpi": mscFrNniDlciVcCallingNpi,
       "mscFrNniDlciVcCallingDna": mscFrNniDlciVcCallingDna,
       "mscFrNniDlciVcCallingLcn": mscFrNniDlciVcCallingLcn,
       "mscFrNniDlciVcAccountingEnabled": mscFrNniDlciVcAccountingEnabled,
       "mscFrNniDlciVcFastSelectCall": mscFrNniDlciVcFastSelectCall,
       "mscFrNniDlciVcPathReliability": mscFrNniDlciVcPathReliability,
       "mscFrNniDlciVcAccountingEnd": mscFrNniDlciVcAccountingEnd,
       "mscFrNniDlciVcPriority": mscFrNniDlciVcPriority,
       "mscFrNniDlciVcSegmentSize": mscFrNniDlciVcSegmentSize,
       "mscFrNniDlciVcMaxSubnetPktSize": mscFrNniDlciVcMaxSubnetPktSize,
       "mscFrNniDlciVcRcosToNetwork": mscFrNniDlciVcRcosToNetwork,
       "mscFrNniDlciVcRcosFromNetwork": mscFrNniDlciVcRcosFromNetwork,
       "mscFrNniDlciVcEmissionPriorityToNetwork": mscFrNniDlciVcEmissionPriorityToNetwork,
       "mscFrNniDlciVcEmissionPriorityFromNetwork": mscFrNniDlciVcEmissionPriorityFromNetwork,
       "mscFrNniDlciVcDataPath": mscFrNniDlciVcDataPath,
       "mscFrNniDlciVcIntdTable": mscFrNniDlciVcIntdTable,
       "mscFrNniDlciVcIntdEntry": mscFrNniDlciVcIntdEntry,
       "mscFrNniDlciVcCallReferenceNumber": mscFrNniDlciVcCallReferenceNumber,
       "mscFrNniDlciVcElapsedTimeTillNow": mscFrNniDlciVcElapsedTimeTillNow,
       "mscFrNniDlciVcSegmentsRx": mscFrNniDlciVcSegmentsRx,
       "mscFrNniDlciVcSegmentsSent": mscFrNniDlciVcSegmentsSent,
       "mscFrNniDlciVcStartTime": mscFrNniDlciVcStartTime,
       "mscFrNniDlciVcCallReferenceNumberDecimal": mscFrNniDlciVcCallReferenceNumberDecimal,
       "mscFrNniDlciVcFrdTable": mscFrNniDlciVcFrdTable,
       "mscFrNniDlciVcFrdEntry": mscFrNniDlciVcFrdEntry,
       "mscFrNniDlciVcFrmCongestedToSubnet": mscFrNniDlciVcFrmCongestedToSubnet,
       "mscFrNniDlciVcCannotForwardToSubnet": mscFrNniDlciVcCannotForwardToSubnet,
       "mscFrNniDlciVcNotDataXferToSubnet": mscFrNniDlciVcNotDataXferToSubnet,
       "mscFrNniDlciVcOutOfRangeFrmFromSubnet": mscFrNniDlciVcOutOfRangeFrmFromSubnet,
       "mscFrNniDlciVcCombErrorsFromSubnet": mscFrNniDlciVcCombErrorsFromSubnet,
       "mscFrNniDlciVcDuplicatesFromSubnet": mscFrNniDlciVcDuplicatesFromSubnet,
       "mscFrNniDlciVcNotDataXferFromSubnet": mscFrNniDlciVcNotDataXferFromSubnet,
       "mscFrNniDlciVcFrmLossTimeouts": mscFrNniDlciVcFrmLossTimeouts,
       "mscFrNniDlciVcOoSeqByteCntExceeded": mscFrNniDlciVcOoSeqByteCntExceeded,
       "mscFrNniDlciVcPeakOoSeqPktCount": mscFrNniDlciVcPeakOoSeqPktCount,
       "mscFrNniDlciVcPeakOoSeqFrmForwarded": mscFrNniDlciVcPeakOoSeqFrmForwarded,
       "mscFrNniDlciVcSendSequenceNumber": mscFrNniDlciVcSendSequenceNumber,
       "mscFrNniDlciVcPktRetryTimeouts": mscFrNniDlciVcPktRetryTimeouts,
       "mscFrNniDlciVcPeakRetryQueueSize": mscFrNniDlciVcPeakRetryQueueSize,
       "mscFrNniDlciVcSubnetRecoveries": mscFrNniDlciVcSubnetRecoveries,
       "mscFrNniDlciVcOoSeqPktCntExceeded": mscFrNniDlciVcOoSeqPktCntExceeded,
       "mscFrNniDlciVcPeakOoSeqByteCount": mscFrNniDlciVcPeakOoSeqByteCount,
       "mscFrNniDlciVcDmepTable": mscFrNniDlciVcDmepTable,
       "mscFrNniDlciVcDmepEntry": mscFrNniDlciVcDmepEntry,
       "mscFrNniDlciVcDmepValue": mscFrNniDlciVcDmepValue,
       "mscFrNniDlciSp": mscFrNniDlciSp,
       "mscFrNniDlciSpRowStatusTable": mscFrNniDlciSpRowStatusTable,
       "mscFrNniDlciSpRowStatusEntry": mscFrNniDlciSpRowStatusEntry,
       "mscFrNniDlciSpRowStatus": mscFrNniDlciSpRowStatus,
       "mscFrNniDlciSpComponentName": mscFrNniDlciSpComponentName,
       "mscFrNniDlciSpStorageType": mscFrNniDlciSpStorageType,
       "mscFrNniDlciSpIndex": mscFrNniDlciSpIndex,
       "mscFrNniDlciSpParmsTable": mscFrNniDlciSpParmsTable,
       "mscFrNniDlciSpParmsEntry": mscFrNniDlciSpParmsEntry,
       "mscFrNniDlciSpMaximumFrameSize": mscFrNniDlciSpMaximumFrameSize,
       "mscFrNniDlciSpRateEnforcement": mscFrNniDlciSpRateEnforcement,
       "mscFrNniDlciSpCommittedInformationRate": mscFrNniDlciSpCommittedInformationRate,
       "mscFrNniDlciSpCommittedBurstSize": mscFrNniDlciSpCommittedBurstSize,
       "mscFrNniDlciSpExcessBurstSize": mscFrNniDlciSpExcessBurstSize,
       "mscFrNniDlciSpMeasurementInterval": mscFrNniDlciSpMeasurementInterval,
       "mscFrNniDlciSpRateAdaptation": mscFrNniDlciSpRateAdaptation,
       "mscFrNniDlciSpAccounting": mscFrNniDlciSpAccounting,
       "mscFrNniDlciSpRaSensitivity": mscFrNniDlciSpRaSensitivity,
       "mscFrNniDlciSpUpdateBCI": mscFrNniDlciSpUpdateBCI,
       "mscFrNniDlciLb": mscFrNniDlciLb,
       "mscFrNniDlciLbRowStatusTable": mscFrNniDlciLbRowStatusTable,
       "mscFrNniDlciLbRowStatusEntry": mscFrNniDlciLbRowStatusEntry,
       "mscFrNniDlciLbRowStatus": mscFrNniDlciLbRowStatus,
       "mscFrNniDlciLbComponentName": mscFrNniDlciLbComponentName,
       "mscFrNniDlciLbStorageType": mscFrNniDlciLbStorageType,
       "mscFrNniDlciLbIndex": mscFrNniDlciLbIndex,
       "mscFrNniDlciLbStatsTable": mscFrNniDlciLbStatsTable,
       "mscFrNniDlciLbStatsEntry": mscFrNniDlciLbStatsEntry,
       "mscFrNniDlciLbLocalTotalFrm": mscFrNniDlciLbLocalTotalFrm,
       "mscFrNniDlciLbLocalTotalBytes": mscFrNniDlciLbLocalTotalBytes,
       "mscFrNniDlciLbLocalFecnFrm": mscFrNniDlciLbLocalFecnFrm,
       "mscFrNniDlciLbLocalBecnFrm": mscFrNniDlciLbLocalBecnFrm,
       "mscFrNniDlciLbLocalDeFrm": mscFrNniDlciLbLocalDeFrm,
       "mscFrNniDlciLbLocalDeBytes": mscFrNniDlciLbLocalDeBytes,
       "mscFrNniDlciLbRemoteTotalFrm": mscFrNniDlciLbRemoteTotalFrm,
       "mscFrNniDlciLbRemoteTotalBytes": mscFrNniDlciLbRemoteTotalBytes,
       "mscFrNniDlciLbRemoteFecnFrm": mscFrNniDlciLbRemoteFecnFrm,
       "mscFrNniDlciLbRemoteBecnFrm": mscFrNniDlciLbRemoteBecnFrm,
       "mscFrNniDlciLbRemoteDeFrm": mscFrNniDlciLbRemoteDeFrm,
       "mscFrNniDlciLbRemoteDeBytes": mscFrNniDlciLbRemoteDeBytes,
       "mscFrNniDlciEgressSp": mscFrNniDlciEgressSp,
       "mscFrNniDlciEgressSpRowStatusTable": mscFrNniDlciEgressSpRowStatusTable,
       "mscFrNniDlciEgressSpRowStatusEntry": mscFrNniDlciEgressSpRowStatusEntry,
       "mscFrNniDlciEgressSpRowStatus": mscFrNniDlciEgressSpRowStatus,
       "mscFrNniDlciEgressSpComponentName": mscFrNniDlciEgressSpComponentName,
       "mscFrNniDlciEgressSpStorageType": mscFrNniDlciEgressSpStorageType,
       "mscFrNniDlciEgressSpIndex": mscFrNniDlciEgressSpIndex,
       "mscFrNniDlciEgressSpProvTable": mscFrNniDlciEgressSpProvTable,
       "mscFrNniDlciEgressSpProvEntry": mscFrNniDlciEgressSpProvEntry,
       "mscFrNniDlciEgressSpCommittedInformationRate": mscFrNniDlciEgressSpCommittedInformationRate,
       "mscFrNniDlciEgressSpCommittedBurstSize": mscFrNniDlciEgressSpCommittedBurstSize,
       "mscFrNniDlciEgressSpExcessBurstSize": mscFrNniDlciEgressSpExcessBurstSize,
       "mscFrNniDlciEgressSpMeasurementInterval": mscFrNniDlciEgressSpMeasurementInterval,
       "mscFrNniDlciStateTable": mscFrNniDlciStateTable,
       "mscFrNniDlciStateEntry": mscFrNniDlciStateEntry,
       "mscFrNniDlciAdminState": mscFrNniDlciAdminState,
       "mscFrNniDlciOperationalState": mscFrNniDlciOperationalState,
       "mscFrNniDlciUsageState": mscFrNniDlciUsageState,
       "mscFrNniDlciAvailabilityStatus": mscFrNniDlciAvailabilityStatus,
       "mscFrNniDlciProceduralStatus": mscFrNniDlciProceduralStatus,
       "mscFrNniDlciControlStatus": mscFrNniDlciControlStatus,
       "mscFrNniDlciAlarmStatus": mscFrNniDlciAlarmStatus,
       "mscFrNniDlciStandbyStatus": mscFrNniDlciStandbyStatus,
       "mscFrNniDlciUnknownStatus": mscFrNniDlciUnknownStatus,
       "mscFrNniDlciAbitTable": mscFrNniDlciAbitTable,
       "mscFrNniDlciAbitEntry": mscFrNniDlciAbitEntry,
       "mscFrNniDlciABitStatusToIf": mscFrNniDlciABitStatusToIf,
       "mscFrNniDlciABitReasonToIf": mscFrNniDlciABitReasonToIf,
       "mscFrNniDlciABitStatusFromIf": mscFrNniDlciABitStatusFromIf,
       "mscFrNniDlciABitReasonFromIf": mscFrNniDlciABitReasonFromIf,
       "mscFrNniDlciLoopbackState": mscFrNniDlciLoopbackState,
       "mscFrNniDlciSpOpTable": mscFrNniDlciSpOpTable,
       "mscFrNniDlciSpOpEntry": mscFrNniDlciSpOpEntry,
       "mscFrNniDlciMaximumFrameSize": mscFrNniDlciMaximumFrameSize,
       "mscFrNniDlciRateEnforcement": mscFrNniDlciRateEnforcement,
       "mscFrNniDlciCommittedInformationRate": mscFrNniDlciCommittedInformationRate,
       "mscFrNniDlciCommittedBurstSize": mscFrNniDlciCommittedBurstSize,
       "mscFrNniDlciExcessBurstSize": mscFrNniDlciExcessBurstSize,
       "mscFrNniDlciMeasurementInterval": mscFrNniDlciMeasurementInterval,
       "mscFrNniDlciRateAdaptation": mscFrNniDlciRateAdaptation,
       "mscFrNniDlciAccounting": mscFrNniDlciAccounting,
       "mscFrNniDlciEmissionPriorityToIf": mscFrNniDlciEmissionPriorityToIf,
       "mscFrNniDlciTransferPriToNwk": mscFrNniDlciTransferPriToNwk,
       "mscFrNniDlciTransferPriFromNwk": mscFrNniDlciTransferPriFromNwk,
       "mscFrNniDlciStatsTable": mscFrNniDlciStatsTable,
       "mscFrNniDlciStatsEntry": mscFrNniDlciStatsEntry,
       "mscFrNniDlciFrmToIf": mscFrNniDlciFrmToIf,
       "mscFrNniDlciFecnFrmToIf": mscFrNniDlciFecnFrmToIf,
       "mscFrNniDlciBecnFrmToIf": mscFrNniDlciBecnFrmToIf,
       "mscFrNniDlciBciToSubnet": mscFrNniDlciBciToSubnet,
       "mscFrNniDlciDeFrmToIf": mscFrNniDlciDeFrmToIf,
       "mscFrNniDlciDiscCongestedToIf": mscFrNniDlciDiscCongestedToIf,
       "mscFrNniDlciDiscDeCongestedToIf": mscFrNniDlciDiscDeCongestedToIf,
       "mscFrNniDlciFrmFromIf": mscFrNniDlciFrmFromIf,
       "mscFrNniDlciFecnFrmFromIf": mscFrNniDlciFecnFrmFromIf,
       "mscFrNniDlciBecnFrmFromIf": mscFrNniDlciBecnFrmFromIf,
       "mscFrNniDlciFciFromSubnet": mscFrNniDlciFciFromSubnet,
       "mscFrNniDlciBciFromSubnet": mscFrNniDlciBciFromSubnet,
       "mscFrNniDlciDeFrmFromIf": mscFrNniDlciDeFrmFromIf,
       "mscFrNniDlciExcessFrmFromIf": mscFrNniDlciExcessFrmFromIf,
       "mscFrNniDlciDiscExcessFromIf": mscFrNniDlciDiscExcessFromIf,
       "mscFrNniDlciDiscFrameAbit": mscFrNniDlciDiscFrameAbit,
       "mscFrNniDlciDiscCongestedFromIf": mscFrNniDlciDiscCongestedFromIf,
       "mscFrNniDlciDiscDeCongestedFromIf": mscFrNniDlciDiscDeCongestedFromIf,
       "mscFrNniDlciErrorShortFrmFromIf": mscFrNniDlciErrorShortFrmFromIf,
       "mscFrNniDlciErrorLongFrmFromIf": mscFrNniDlciErrorLongFrmFromIf,
       "mscFrNniDlciBecnFrmSetByService": mscFrNniDlciBecnFrmSetByService,
       "mscFrNniDlciBytesToIf": mscFrNniDlciBytesToIf,
       "mscFrNniDlciDeBytesToIf": mscFrNniDlciDeBytesToIf,
       "mscFrNniDlciDiscCongestedToIfBytes": mscFrNniDlciDiscCongestedToIfBytes,
       "mscFrNniDlciDiscDeCongestedToIfBytes": mscFrNniDlciDiscDeCongestedToIfBytes,
       "mscFrNniDlciBytesFromIf": mscFrNniDlciBytesFromIf,
       "mscFrNniDlciDeBytesFromIf": mscFrNniDlciDeBytesFromIf,
       "mscFrNniDlciExcessBytesFromIf": mscFrNniDlciExcessBytesFromIf,
       "mscFrNniDlciDiscExcessFromIfBytes": mscFrNniDlciDiscExcessFromIfBytes,
       "mscFrNniDlciDiscByteAbit": mscFrNniDlciDiscByteAbit,
       "mscFrNniDlciDiscCongestedFromIfBytes": mscFrNniDlciDiscCongestedFromIfBytes,
       "mscFrNniDlciDiscDeCongestedFromIfBytes": mscFrNniDlciDiscDeCongestedFromIfBytes,
       "mscFrNniDlciErrorShortBytesFromIf": mscFrNniDlciErrorShortBytesFromIf,
       "mscFrNniDlciErrorLongBytesFromIf": mscFrNniDlciErrorLongBytesFromIf,
       "mscFrNniDlciRateAdaptReduct": mscFrNniDlciRateAdaptReduct,
       "mscFrNniDlciRateAdaptReductPeriod": mscFrNniDlciRateAdaptReductPeriod,
       "mscFrNniDlciTransferPriorityToNetwork": mscFrNniDlciTransferPriorityToNetwork,
       "mscFrNniDlciTransferPriorityFromNetwork": mscFrNniDlciTransferPriorityFromNetwork,
       "mscFrNniDlciCirPresent": mscFrNniDlciCirPresent,
       "mscFrNniDlciEirPresent": mscFrNniDlciEirPresent,
       "mscFrNniDlciIntTable": mscFrNniDlciIntTable,
       "mscFrNniDlciIntEntry": mscFrNniDlciIntEntry,
       "mscFrNniDlciStartTime": mscFrNniDlciStartTime,
       "mscFrNniDlciTotalIngressBytes": mscFrNniDlciTotalIngressBytes,
       "mscFrNniDlciTotalEgressBytes": mscFrNniDlciTotalEgressBytes,
       "mscFrNniDlciEirIngressBytes": mscFrNniDlciEirIngressBytes,
       "mscFrNniDlciEirEgressBytes": mscFrNniDlciEirEgressBytes,
       "mscFrNniDlciDiscardedBytes": mscFrNniDlciDiscardedBytes,
       "mscFrNniDlciTotalIngressSegFrm": mscFrNniDlciTotalIngressSegFrm,
       "mscFrNniDlciTotalEgressSegFrm": mscFrNniDlciTotalEgressSegFrm,
       "mscFrNniDlciEirIngressSegFrm": mscFrNniDlciEirIngressSegFrm,
       "mscFrNniDlciEirEgressSegFrm": mscFrNniDlciEirEgressSegFrm,
       "mscFrNniDlciDiscardedSegFrm": mscFrNniDlciDiscardedSegFrm,
       "mscFrNniDlciCirPresentObs": mscFrNniDlciCirPresentObs,
       "mscFrNniDlciEirPresentObs": mscFrNniDlciEirPresentObs,
       "mscFrNniDlciRateEnforcementPresent": mscFrNniDlciRateEnforcementPresent,
       "mscFrNniDlciRateAdaptationPresent": mscFrNniDlciRateAdaptationPresent,
       "mscFrNniDlciLocalRateAdaptOccurred": mscFrNniDlciLocalRateAdaptOccurred,
       "mscFrNniDlciCallReferenceNumber": mscFrNniDlciCallReferenceNumber,
       "mscFrNniDlciElapsedDifference": mscFrNniDlciElapsedDifference,
       "mscFrNniDlciCallRefNumber": mscFrNniDlciCallRefNumber,
       "mscFrNniDlciCalldTable": mscFrNniDlciCalldTable,
       "mscFrNniDlciCalldEntry": mscFrNniDlciCalldEntry,
       "mscFrNniDlciCallType": mscFrNniDlciCallType,
       "mscFrNniDlciCallState": mscFrNniDlciCallState,
       "mscFrNniDlciCallReference": mscFrNniDlciCallReference,
       "mscFrNniVFramer": mscFrNniVFramer,
       "mscFrNniVFramerRowStatusTable": mscFrNniVFramerRowStatusTable,
       "mscFrNniVFramerRowStatusEntry": mscFrNniVFramerRowStatusEntry,
       "mscFrNniVFramerRowStatus": mscFrNniVFramerRowStatus,
       "mscFrNniVFramerComponentName": mscFrNniVFramerComponentName,
       "mscFrNniVFramerStorageType": mscFrNniVFramerStorageType,
       "mscFrNniVFramerIndex": mscFrNniVFramerIndex,
       "mscFrNniVFramerProvTable": mscFrNniVFramerProvTable,
       "mscFrNniVFramerProvEntry": mscFrNniVFramerProvEntry,
       "mscFrNniVFramerOtherVirtualFramer": mscFrNniVFramerOtherVirtualFramer,
       "mscFrNniVFramerLogicalProcessor": mscFrNniVFramerLogicalProcessor,
       "mscFrNniVFramerStateTable": mscFrNniVFramerStateTable,
       "mscFrNniVFramerStateEntry": mscFrNniVFramerStateEntry,
       "mscFrNniVFramerAdminState": mscFrNniVFramerAdminState,
       "mscFrNniVFramerOperationalState": mscFrNniVFramerOperationalState,
       "mscFrNniVFramerUsageState": mscFrNniVFramerUsageState,
       "mscFrNniVFramerStatsTable": mscFrNniVFramerStatsTable,
       "mscFrNniVFramerStatsEntry": mscFrNniVFramerStatsEntry,
       "mscFrNniVFramerFrmToOtherVFramer": mscFrNniVFramerFrmToOtherVFramer,
       "mscFrNniVFramerFrmFromOtherVFramer": mscFrNniVFramerFrmFromOtherVFramer,
       "mscFrNniVFramerOctetFromOtherVFramer": mscFrNniVFramerOctetFromOtherVFramer,
       "mscFrNniSig": mscFrNniSig,
       "mscFrNniSigRowStatusTable": mscFrNniSigRowStatusTable,
       "mscFrNniSigRowStatusEntry": mscFrNniSigRowStatusEntry,
       "mscFrNniSigRowStatus": mscFrNniSigRowStatus,
       "mscFrNniSigComponentName": mscFrNniSigComponentName,
       "mscFrNniSigStorageType": mscFrNniSigStorageType,
       "mscFrNniSigIndex": mscFrNniSigIndex,
       "mscFrNniSigProvTable": mscFrNniSigProvTable,
       "mscFrNniSigProvEntry": mscFrNniSigProvEntry,
       "mscFrNniSigDlciAllocation": mscFrNniSigDlciAllocation,
       "mscFrNniSigHighestPermanentDlci": mscFrNniSigHighestPermanentDlci,
       "mscFrNniSigHighestPvcDlci": mscFrNniSigHighestPvcDlci,
       "mscFrNniSigServParmsTable": mscFrNniSigServParmsTable,
       "mscFrNniSigServParmsEntry": mscFrNniSigServParmsEntry,
       "mscFrNniSigMaximumFrameSize": mscFrNniSigMaximumFrameSize,
       "mscFrNniSigDefaultMaximumFrameSize": mscFrNniSigDefaultMaximumFrameSize,
       "mscFrNniSigDefaultCommittedInformationRate": mscFrNniSigDefaultCommittedInformationRate,
       "mscFrNniSigDefaultCommittedBurstSize": mscFrNniSigDefaultCommittedBurstSize,
       "mscFrNniSigDefaultExcessBurstSize": mscFrNniSigDefaultExcessBurstSize,
       "mscFrNniSigRateEnforcement": mscFrNniSigRateEnforcement,
       "mscFrNniSigRateAdaptation": mscFrNniSigRateAdaptation,
       "mscFrNniSigRaSensitivity": mscFrNniSigRaSensitivity,
       "mscFrNniSigUpdateBCI": mscFrNniSigUpdateBCI,
       "mscFrNniSigSysParmsTable": mscFrNniSigSysParmsTable,
       "mscFrNniSigSysParmsEntry": mscFrNniSigSysParmsEntry,
       "mscFrNniSigCallSetupTimer": mscFrNniSigCallSetupTimer,
       "mscFrNniSigReleaseTimer": mscFrNniSigReleaseTimer,
       "mscFrNniSigCallProceedingTimer": mscFrNniSigCallProceedingTimer,
       "mscFrNniSigRestartReqTimer": mscFrNniSigRestartReqTimer,
       "mscFrNniSigRestartRcvTimer": mscFrNniSigRestartRcvTimer,
       "mscFrNniSigStatusEnqTimer": mscFrNniSigStatusEnqTimer,
       "mscFrNniSigNetworkType": mscFrNniSigNetworkType,
       "mscFrNniSigLapfSysTable": mscFrNniSigLapfSysTable,
       "mscFrNniSigLapfSysEntry": mscFrNniSigLapfSysEntry,
       "mscFrNniSigWindowSize": mscFrNniSigWindowSize,
       "mscFrNniSigRetransmitLimit": mscFrNniSigRetransmitLimit,
       "mscFrNniSigAckTimer": mscFrNniSigAckTimer,
       "mscFrNniSigAckDelayTimer": mscFrNniSigAckDelayTimer,
       "mscFrNniSigIdleProbeTimer": mscFrNniSigIdleProbeTimer,
       "mscFrNniSigCodesTable": mscFrNniSigCodesTable,
       "mscFrNniSigCodesEntry": mscFrNniSigCodesEntry,
       "mscFrNniSigLastClearRemoteDataNetworkAddress": mscFrNniSigLastClearRemoteDataNetworkAddress,
       "mscFrNniSigLastClearCause": mscFrNniSigLastClearCause,
       "mscFrNniSigLastDiagnosticCode": mscFrNniSigLastDiagnosticCode,
       "mscFrNniSigStateTable": mscFrNniSigStateTable,
       "mscFrNniSigStateEntry": mscFrNniSigStateEntry,
       "mscFrNniSigAdminState": mscFrNniSigAdminState,
       "mscFrNniSigOperationalState": mscFrNniSigOperationalState,
       "mscFrNniSigUsageState": mscFrNniSigUsageState,
       "mscFrNniSigStatsTable": mscFrNniSigStatsTable,
       "mscFrNniSigStatsEntry": mscFrNniSigStatsEntry,
       "mscFrNniSigCurrentNumberOfSvcCalls": mscFrNniSigCurrentNumberOfSvcCalls,
       "mscFrNniSigInCalls": mscFrNniSigInCalls,
       "mscFrNniSigInCallsRefused": mscFrNniSigInCallsRefused,
       "mscFrNniSigOutCalls": mscFrNniSigOutCalls,
       "mscFrNniSigOutCallsFailed": mscFrNniSigOutCallsFailed,
       "mscFrNniSigProtocolErrors": mscFrNniSigProtocolErrors,
       "mscFrNniSigQualityOfServiceNotAvailable": mscFrNniSigQualityOfServiceNotAvailable,
       "mscFrNniSigSetupTimeout": mscFrNniSigSetupTimeout,
       "mscFrNniSigLastCauseInStatusMsgReceived": mscFrNniSigLastCauseInStatusMsgReceived,
       "mscFrNniSigLastStateInStatusMsgReceived": mscFrNniSigLastStateInStatusMsgReceived,
       "mscFrNniSigLastDlciReceivedStatus": mscFrNniSigLastDlciReceivedStatus,
       "mscFrNniSigLastStateReceivedStatus": mscFrNniSigLastStateReceivedStatus,
       "mscFrNniSigDlciCollisions": mscFrNniSigDlciCollisions,
       "mscFrNniSigLapfStatusTable": mscFrNniSigLapfStatusTable,
       "mscFrNniSigLapfStatusEntry": mscFrNniSigLapfStatusEntry,
       "mscFrNniSigCurrentState": mscFrNniSigCurrentState,
       "mscFrNniSigLastStateChangeReason": mscFrNniSigLastStateChangeReason,
       "mscFrNniSigFrmrReceive": mscFrNniSigFrmrReceive,
       "mscFrNniSigCurrentQueueSize": mscFrNniSigCurrentQueueSize,
       "mscFrNniSigLapfStatsTable": mscFrNniSigLapfStatsTable,
       "mscFrNniSigLapfStatsEntry": mscFrNniSigLapfStatsEntry,
       "mscFrNniSigRemoteBusy": mscFrNniSigRemoteBusy,
       "mscFrNniSigReceiveRejectFrame": mscFrNniSigReceiveRejectFrame,
       "mscFrNniSigAckTimeout": mscFrNniSigAckTimeout,
       "mscFrNniSigIFramesTransmitted": mscFrNniSigIFramesTransmitted,
       "mscFrNniSigIFramesTxDiscarded": mscFrNniSigIFramesTxDiscarded,
       "mscFrNniSigIFramesReceived": mscFrNniSigIFramesReceived,
       "mscFrNniSigIFramesRcvdDiscarded": mscFrNniSigIFramesRcvdDiscarded,
       "mscFrNniSigStateChange": mscFrNniSigStateChange,
       "mscFrNniSigSvcaccTable": mscFrNniSigSvcaccTable,
       "mscFrNniSigSvcaccEntry": mscFrNniSigSvcaccEntry,
       "mscFrNniSigDefaultAccounting": mscFrNniSigDefaultAccounting,
       "mscFrNniSigBandwidthNotAvailableTable": mscFrNniSigBandwidthNotAvailableTable,
       "mscFrNniSigBandwidthNotAvailableEntry": mscFrNniSigBandwidthNotAvailableEntry,
       "mscFrNniSigBandwidthNotAvailableIndex": mscFrNniSigBandwidthNotAvailableIndex,
       "mscFrNniSigBandwidthNotAvailableValue": mscFrNniSigBandwidthNotAvailableValue,
       "mscFrNniLts": mscFrNniLts,
       "mscFrNniLtsRowStatusTable": mscFrNniLtsRowStatusTable,
       "mscFrNniLtsRowStatusEntry": mscFrNniLtsRowStatusEntry,
       "mscFrNniLtsRowStatus": mscFrNniLtsRowStatus,
       "mscFrNniLtsComponentName": mscFrNniLtsComponentName,
       "mscFrNniLtsStorageType": mscFrNniLtsStorageType,
       "mscFrNniLtsIndex": mscFrNniLtsIndex,
       "mscFrNniLtsPat": mscFrNniLtsPat,
       "mscFrNniLtsPatRowStatusTable": mscFrNniLtsPatRowStatusTable,
       "mscFrNniLtsPatRowStatusEntry": mscFrNniLtsPatRowStatusEntry,
       "mscFrNniLtsPatRowStatus": mscFrNniLtsPatRowStatus,
       "mscFrNniLtsPatComponentName": mscFrNniLtsPatComponentName,
       "mscFrNniLtsPatStorageType": mscFrNniLtsPatStorageType,
       "mscFrNniLtsPatIndex": mscFrNniLtsPatIndex,
       "mscFrNniLtsPatDefaultsTable": mscFrNniLtsPatDefaultsTable,
       "mscFrNniLtsPatDefaultsEntry": mscFrNniLtsPatDefaultsEntry,
       "mscFrNniLtsPatDefaultDlci": mscFrNniLtsPatDefaultDlci,
       "mscFrNniLtsPatDefaultNumFrames": mscFrNniLtsPatDefaultNumFrames,
       "mscFrNniLtsPatDefaultDataSize": mscFrNniLtsPatDefaultDataSize,
       "mscFrNniLtsPatDefaultHeaderBits": mscFrNniLtsPatDefaultHeaderBits,
       "mscFrNniLtsPatDefaultHeaderLength": mscFrNniLtsPatDefaultHeaderLength,
       "mscFrNniLtsPatDefaultEABits": mscFrNniLtsPatDefaultEABits,
       "mscFrNniLtsPatDefaultPayloadPattern": mscFrNniLtsPatDefaultPayloadPattern,
       "mscFrNniLtsPatDefaultRfc1490Header": mscFrNniLtsPatDefaultRfc1490Header,
       "mscFrNniLtsPatDefaultUseBadLrc": mscFrNniLtsPatDefaultUseBadLrc,
       "mscFrNniLtsPatSetupTable": mscFrNniLtsPatSetupTable,
       "mscFrNniLtsPatSetupEntry": mscFrNniLtsPatSetupEntry,
       "mscFrNniLtsPatDlci": mscFrNniLtsPatDlci,
       "mscFrNniLtsPatNumFrames": mscFrNniLtsPatNumFrames,
       "mscFrNniLtsPatDataSize": mscFrNniLtsPatDataSize,
       "mscFrNniLtsPatHeaderBits": mscFrNniLtsPatHeaderBits,
       "mscFrNniLtsPatHeaderLength": mscFrNniLtsPatHeaderLength,
       "mscFrNniLtsPatEaBits": mscFrNniLtsPatEaBits,
       "mscFrNniLtsPatPayloadPattern": mscFrNniLtsPatPayloadPattern,
       "mscFrNniLtsPatRfc1490Header": mscFrNniLtsPatRfc1490Header,
       "mscFrNniLtsPatUseBadLrc": mscFrNniLtsPatUseBadLrc,
       "mscFrNniLtsPatOpDataTable": mscFrNniLtsPatOpDataTable,
       "mscFrNniLtsPatOpDataEntry": mscFrNniLtsPatOpDataEntry,
       "mscFrNniLtsPatFramePattern": mscFrNniLtsPatFramePattern,
       "mscFrNniLtsPatHdlcBitsInserted": mscFrNniLtsPatHdlcBitsInserted,
       "mscFrNniLtsPatOpStateTable": mscFrNniLtsPatOpStateTable,
       "mscFrNniLtsPatOpStateEntry": mscFrNniLtsPatOpStateEntry,
       "mscFrNniLtsPatLoad": mscFrNniLtsPatLoad,
       "mscFrNniLtsPatStatus": mscFrNniLtsPatStatus,
       "mscFrNniLtsSetupTable": mscFrNniLtsSetupTable,
       "mscFrNniLtsSetupEntry": mscFrNniLtsSetupEntry,
       "mscFrNniLtsDuration": mscFrNniLtsDuration,
       "mscFrNniLtsAlgorithm": mscFrNniLtsAlgorithm,
       "mscFrNniLtsBurstSize": mscFrNniLtsBurstSize,
       "mscFrNniLtsTimeInterval": mscFrNniLtsTimeInterval,
       "mscFrNniLtsStateTable": mscFrNniLtsStateTable,
       "mscFrNniLtsStateEntry": mscFrNniLtsStateEntry,
       "mscFrNniLtsGeneratorState": mscFrNniLtsGeneratorState,
       "mscFrNniLtsCycleIncomplete": mscFrNniLtsCycleIncomplete,
       "mscFrNniLtsLastActiveInterval": mscFrNniLtsLastActiveInterval,
       "mscFrNniLtsLoad": mscFrNniLtsLoad,
       "mscFrNniLtsElapsedGenerationTime": mscFrNniLtsElapsedGenerationTime,
       "mscFrNniLtsResultsTable": mscFrNniLtsResultsTable,
       "mscFrNniLtsResultsEntry": mscFrNniLtsResultsEntry,
       "mscFrNniLtsFramesTx": mscFrNniLtsFramesTx,
       "mscFrNniLtsBytesTx": mscFrNniLtsBytesTx,
       "mscFrNniLtsBitRateTx": mscFrNniLtsBitRateTx,
       "mscFrNniLtsFrameRateTx": mscFrNniLtsFrameRateTx,
       "mscFrNniCidDataTable": mscFrNniCidDataTable,
       "mscFrNniCidDataEntry": mscFrNniCidDataEntry,
       "mscFrNniCustomerIdentifier": mscFrNniCustomerIdentifier,
       "mscFrNniStateTable": mscFrNniStateTable,
       "mscFrNniStateEntry": mscFrNniStateEntry,
       "mscFrNniAdminState": mscFrNniAdminState,
       "mscFrNniOperationalState": mscFrNniOperationalState,
       "mscFrNniUsageState": mscFrNniUsageState,
       "mscFrNniAvailabilityStatus": mscFrNniAvailabilityStatus,
       "mscFrNniProceduralStatus": mscFrNniProceduralStatus,
       "mscFrNniControlStatus": mscFrNniControlStatus,
       "mscFrNniAlarmStatus": mscFrNniAlarmStatus,
       "mscFrNniStandbyStatus": mscFrNniStandbyStatus,
       "mscFrNniUnknownStatus": mscFrNniUnknownStatus,
       "mscFrNniStatsTable": mscFrNniStatsTable,
       "mscFrNniStatsEntry": mscFrNniStatsEntry,
       "mscFrNniLastUnknownDlci": mscFrNniLastUnknownDlci,
       "mscFrNniUnknownDlciFramesFromIf": mscFrNniUnknownDlciFramesFromIf,
       "mscFrNniInvalidHeaderFramesFromIf": mscFrNniInvalidHeaderFramesFromIf,
       "mscFrNniIfEntryTable": mscFrNniIfEntryTable,
       "mscFrNniIfEntryEntry": mscFrNniIfEntryEntry,
       "mscFrNniIfAdminStatus": mscFrNniIfAdminStatus,
       "mscFrNniIfIndex": mscFrNniIfIndex,
       "mscFrNniOperStatusTable": mscFrNniOperStatusTable,
       "mscFrNniOperStatusEntry": mscFrNniOperStatusEntry,
       "mscFrNniSnmpOperStatus": mscFrNniSnmpOperStatus,
       "mscFrNniEmissionPriorityQsTable": mscFrNniEmissionPriorityQsTable,
       "mscFrNniEmissionPriorityQsEntry": mscFrNniEmissionPriorityQsEntry,
       "mscFrNniNumberOfEmissionQs": mscFrNniNumberOfEmissionQs,
       "mscFrNniCa": mscFrNniCa,
       "mscFrNniCaRowStatusTable": mscFrNniCaRowStatusTable,
       "mscFrNniCaRowStatusEntry": mscFrNniCaRowStatusEntry,
       "mscFrNniCaRowStatus": mscFrNniCaRowStatus,
       "mscFrNniCaComponentName": mscFrNniCaComponentName,
       "mscFrNniCaStorageType": mscFrNniCaStorageType,
       "mscFrNniCaIndex": mscFrNniCaIndex,
       "mscFrNniCaTpm": mscFrNniCaTpm,
       "mscFrNniCaTpmRowStatusTable": mscFrNniCaTpmRowStatusTable,
       "mscFrNniCaTpmRowStatusEntry": mscFrNniCaTpmRowStatusEntry,
       "mscFrNniCaTpmRowStatus": mscFrNniCaTpmRowStatus,
       "mscFrNniCaTpmComponentName": mscFrNniCaTpmComponentName,
       "mscFrNniCaTpmStorageType": mscFrNniCaTpmStorageType,
       "mscFrNniCaTpmIndex": mscFrNniCaTpmIndex,
       "mscFrNniCaTpmProvTable": mscFrNniCaTpmProvTable,
       "mscFrNniCaTpmProvEntry": mscFrNniCaTpmProvEntry,
       "mscFrNniCaTpmAssignedIngressBandwidthPool": mscFrNniCaTpmAssignedIngressBandwidthPool,
       "mscFrNniCaTpmAssignedEgressBandwidthPool": mscFrNniCaTpmAssignedEgressBandwidthPool,
       "mscFrNniCaProvTable": mscFrNniCaProvTable,
       "mscFrNniCaProvEntry": mscFrNniCaProvEntry,
       "mscFrNniCaOverrideLinkRate": mscFrNniCaOverrideLinkRate,
       "mscFrNniCaMaximumBandwidthPerCall": mscFrNniCaMaximumBandwidthPerCall,
       "mscFrNniCaIngressCacTable": mscFrNniCaIngressCacTable,
       "mscFrNniCaIngressCacEntry": mscFrNniCaIngressCacEntry,
       "mscFrNniCaIngressApplyToCos": mscFrNniCaIngressApplyToCos,
       "mscFrNniCaIngressMaximumEirOnlyCalls": mscFrNniCaIngressMaximumEirOnlyCalls,
       "mscFrNniCaEgressCacTable": mscFrNniCaEgressCacTable,
       "mscFrNniCaEgressCacEntry": mscFrNniCaEgressCacEntry,
       "mscFrNniCaEgressApplyToCos": mscFrNniCaEgressApplyToCos,
       "mscFrNniCaEgressMaximumEirOnlyCalls": mscFrNniCaEgressMaximumEirOnlyCalls,
       "mscFrNniCaOpTable": mscFrNniCaOpTable,
       "mscFrNniCaOpEntry": mscFrNniCaOpEntry,
       "mscFrNniCaLinkRate": mscFrNniCaLinkRate,
       "mscFrNniCaNumberRejectedEgressCirPermConn": mscFrNniCaNumberRejectedEgressCirPermConn,
       "mscFrNniCaNumberRejectedEgressEirPermConn": mscFrNniCaNumberRejectedEgressEirPermConn,
       "mscFrNniCaIngCirBPTable": mscFrNniCaIngCirBPTable,
       "mscFrNniCaIngCirBPEntry": mscFrNniCaIngCirBPEntry,
       "mscFrNniCaIngCirBPIndex": mscFrNniCaIngCirBPIndex,
       "mscFrNniCaIngCirBPValue": mscFrNniCaIngCirBPValue,
       "mscFrNniCaEgCirBpTable": mscFrNniCaEgCirBpTable,
       "mscFrNniCaEgCirBpEntry": mscFrNniCaEgCirBpEntry,
       "mscFrNniCaEgCirBpIndex": mscFrNniCaEgCirBpIndex,
       "mscFrNniCaEgCirBpValue": mscFrNniCaEgCirBpValue,
       "mscFrNniCaIngCirPoolAdmitBwTable": mscFrNniCaIngCirPoolAdmitBwTable,
       "mscFrNniCaIngCirPoolAdmitBwEntry": mscFrNniCaIngCirPoolAdmitBwEntry,
       "mscFrNniCaIngCirPoolAdmitBwIndex": mscFrNniCaIngCirPoolAdmitBwIndex,
       "mscFrNniCaIngCirPoolAdmitBwValue": mscFrNniCaIngCirPoolAdmitBwValue,
       "mscFrNniCaIngCirPoolAvailBwTable": mscFrNniCaIngCirPoolAvailBwTable,
       "mscFrNniCaIngCirPoolAvailBwEntry": mscFrNniCaIngCirPoolAvailBwEntry,
       "mscFrNniCaIngCirPoolAvailBwIndex": mscFrNniCaIngCirPoolAvailBwIndex,
       "mscFrNniCaIngCirPoolAvailBwValue": mscFrNniCaIngCirPoolAvailBwValue,
       "mscFrNniCaEgCirPoolAdmitBwTable": mscFrNniCaEgCirPoolAdmitBwTable,
       "mscFrNniCaEgCirPoolAdmitBwEntry": mscFrNniCaEgCirPoolAdmitBwEntry,
       "mscFrNniCaEgCirPoolAdmitBwIndex": mscFrNniCaEgCirPoolAdmitBwIndex,
       "mscFrNniCaEgCirPoolAdmitBwValue": mscFrNniCaEgCirPoolAdmitBwValue,
       "mscFrNniCaEgCirPoolAvailBwTable": mscFrNniCaEgCirPoolAvailBwTable,
       "mscFrNniCaEgCirPoolAvailBwEntry": mscFrNniCaEgCirPoolAvailBwEntry,
       "mscFrNniCaEgCirPoolAvailBwIndex": mscFrNniCaEgCirPoolAvailBwIndex,
       "mscFrNniCaEgCirPoolAvailBwValue": mscFrNniCaEgCirPoolAvailBwValue,
       "mscFrNniCaIngEirBpTable": mscFrNniCaIngEirBpTable,
       "mscFrNniCaIngEirBpEntry": mscFrNniCaIngEirBpEntry,
       "mscFrNniCaIngEirBpIndex": mscFrNniCaIngEirBpIndex,
       "mscFrNniCaIngEirBpValue": mscFrNniCaIngEirBpValue,
       "mscFrNniCaEgEirBpTable": mscFrNniCaEgEirBpTable,
       "mscFrNniCaEgEirBpEntry": mscFrNniCaEgEirBpEntry,
       "mscFrNniCaEgEirBpIndex": mscFrNniCaEgEirBpIndex,
       "mscFrNniCaEgEirBpValue": mscFrNniCaEgEirBpValue,
       "mscFrNniCaIngEirPoolAdmitBwTable": mscFrNniCaIngEirPoolAdmitBwTable,
       "mscFrNniCaIngEirPoolAdmitBwEntry": mscFrNniCaIngEirPoolAdmitBwEntry,
       "mscFrNniCaIngEirPoolAdmitBwIndex": mscFrNniCaIngEirPoolAdmitBwIndex,
       "mscFrNniCaIngEirPoolAdmitBwValue": mscFrNniCaIngEirPoolAdmitBwValue,
       "mscFrNniCaIngEirPoolAvailBwTable": mscFrNniCaIngEirPoolAvailBwTable,
       "mscFrNniCaIngEirPoolAvailBwEntry": mscFrNniCaIngEirPoolAvailBwEntry,
       "mscFrNniCaIngEirPoolAvailBwIndex": mscFrNniCaIngEirPoolAvailBwIndex,
       "mscFrNniCaIngEirPoolAvailBwValue": mscFrNniCaIngEirPoolAvailBwValue,
       "mscFrNniCaEgEirPoolAdmitBwTable": mscFrNniCaEgEirPoolAdmitBwTable,
       "mscFrNniCaEgEirPoolAdmitBwEntry": mscFrNniCaEgEirPoolAdmitBwEntry,
       "mscFrNniCaEgEirPoolAdmitBwIndex": mscFrNniCaEgEirPoolAdmitBwIndex,
       "mscFrNniCaEgEirPoolAdmitBwValue": mscFrNniCaEgEirPoolAdmitBwValue,
       "mscFrNniCaEgEirPoolAvailBwTable": mscFrNniCaEgEirPoolAvailBwTable,
       "mscFrNniCaEgEirPoolAvailBwEntry": mscFrNniCaEgEirPoolAvailBwEntry,
       "mscFrNniCaEgEirPoolAvailBwIndex": mscFrNniCaEgEirPoolAvailBwIndex,
       "mscFrNniCaEgEirPoolAvailBwValue": mscFrNniCaEgEirPoolAvailBwValue,
       "mscFrNniFrmToIfByQueueTable": mscFrNniFrmToIfByQueueTable,
       "mscFrNniFrmToIfByQueueEntry": mscFrNniFrmToIfByQueueEntry,
       "mscFrNniFrmToIfByQueueIndex": mscFrNniFrmToIfByQueueIndex,
       "mscFrNniFrmToIfByQueueValue": mscFrNniFrmToIfByQueueValue,
       "mscFrNniOctetToIfByQueueTable": mscFrNniOctetToIfByQueueTable,
       "mscFrNniOctetToIfByQueueEntry": mscFrNniOctetToIfByQueueEntry,
       "mscFrNniOctetToIfByQueueIndex": mscFrNniOctetToIfByQueueIndex,
       "mscFrNniOctetToIfByQueueValue": mscFrNniOctetToIfByQueueValue,
       "frameRelayNniMIB": frameRelayNniMIB,
       "frameRelayNniGroup": frameRelayNniGroup,
       "frameRelayNniGroupCA": frameRelayNniGroupCA,
       "frameRelayNniGroupCA02": frameRelayNniGroupCA02,
       "frameRelayNniGroupCA02A": frameRelayNniGroupCA02A,
       "frameRelayNniCapabilities": frameRelayNniCapabilities,
       "frameRelayNniCapabilitiesCA": frameRelayNniCapabilitiesCA,
       "frameRelayNniCapabilitiesCA02": frameRelayNniCapabilitiesCA02,
       "frameRelayNniCapabilitiesCA02A": frameRelayNniCapabilitiesCA02A}
)
