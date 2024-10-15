# SNMP MIB module (Nortel-MsCarrier-MscPassport-IpiFrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-IpiFrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:41 2024
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
 DigitString,
 EnterpriseDateAndTime,
 Hex,
 HexString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
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

_MscIpiFr_ObjectIdentity = ObjectIdentity
mscIpiFr = _MscIpiFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50)
)
_MscIpiFrRowStatusTable_Object = MibTable
mscIpiFrRowStatusTable = _MscIpiFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrRowStatusTable.setStatus("mandatory")
_MscIpiFrRowStatusEntry_Object = MibTableRow
mscIpiFrRowStatusEntry = _MscIpiFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 1, 1)
)
mscIpiFrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrRowStatusEntry.setStatus("mandatory")
_MscIpiFrRowStatus_Type = RowStatus
_MscIpiFrRowStatus_Object = MibTableColumn
mscIpiFrRowStatus = _MscIpiFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 1, 1, 1),
    _MscIpiFrRowStatus_Type()
)
mscIpiFrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrRowStatus.setStatus("mandatory")
_MscIpiFrComponentName_Type = DisplayString
_MscIpiFrComponentName_Object = MibTableColumn
mscIpiFrComponentName = _MscIpiFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 1, 1, 2),
    _MscIpiFrComponentName_Type()
)
mscIpiFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrComponentName.setStatus("mandatory")
_MscIpiFrStorageType_Type = StorageType
_MscIpiFrStorageType_Object = MibTableColumn
mscIpiFrStorageType = _MscIpiFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 1, 1, 4),
    _MscIpiFrStorageType_Type()
)
mscIpiFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrStorageType.setStatus("mandatory")
_MscIpiFrIndex_Type = NonReplicated
_MscIpiFrIndex_Object = MibTableColumn
mscIpiFrIndex = _MscIpiFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 1, 1, 10),
    _MscIpiFrIndex_Type()
)
mscIpiFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrIndex.setStatus("mandatory")
_MscIpiFrDna_ObjectIdentity = ObjectIdentity
mscIpiFrDna = _MscIpiFrDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2)
)
_MscIpiFrDnaRowStatusTable_Object = MibTable
mscIpiFrDnaRowStatusTable = _MscIpiFrDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrDnaRowStatusTable.setStatus("mandatory")
_MscIpiFrDnaRowStatusEntry_Object = MibTableRow
mscIpiFrDnaRowStatusEntry = _MscIpiFrDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 1, 1)
)
mscIpiFrDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrDnaRowStatusEntry.setStatus("mandatory")
_MscIpiFrDnaRowStatus_Type = RowStatus
_MscIpiFrDnaRowStatus_Object = MibTableColumn
mscIpiFrDnaRowStatus = _MscIpiFrDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 1, 1, 1),
    _MscIpiFrDnaRowStatus_Type()
)
mscIpiFrDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaRowStatus.setStatus("mandatory")
_MscIpiFrDnaComponentName_Type = DisplayString
_MscIpiFrDnaComponentName_Object = MibTableColumn
mscIpiFrDnaComponentName = _MscIpiFrDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 1, 1, 2),
    _MscIpiFrDnaComponentName_Type()
)
mscIpiFrDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaComponentName.setStatus("mandatory")
_MscIpiFrDnaStorageType_Type = StorageType
_MscIpiFrDnaStorageType_Object = MibTableColumn
mscIpiFrDnaStorageType = _MscIpiFrDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 1, 1, 4),
    _MscIpiFrDnaStorageType_Type()
)
mscIpiFrDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaStorageType.setStatus("mandatory")
_MscIpiFrDnaIndex_Type = NonReplicated
_MscIpiFrDnaIndex_Object = MibTableColumn
mscIpiFrDnaIndex = _MscIpiFrDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 1, 1, 10),
    _MscIpiFrDnaIndex_Type()
)
mscIpiFrDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrDnaIndex.setStatus("mandatory")
_MscIpiFrDnaCug_ObjectIdentity = ObjectIdentity
mscIpiFrDnaCug = _MscIpiFrDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2)
)
_MscIpiFrDnaCugRowStatusTable_Object = MibTable
mscIpiFrDnaCugRowStatusTable = _MscIpiFrDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrDnaCugRowStatusTable.setStatus("mandatory")
_MscIpiFrDnaCugRowStatusEntry_Object = MibTableRow
mscIpiFrDnaCugRowStatusEntry = _MscIpiFrDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 1, 1)
)
mscIpiFrDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrDnaCugRowStatusEntry.setStatus("mandatory")
_MscIpiFrDnaCugRowStatus_Type = RowStatus
_MscIpiFrDnaCugRowStatus_Object = MibTableColumn
mscIpiFrDnaCugRowStatus = _MscIpiFrDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 1, 1, 1),
    _MscIpiFrDnaCugRowStatus_Type()
)
mscIpiFrDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugRowStatus.setStatus("mandatory")
_MscIpiFrDnaCugComponentName_Type = DisplayString
_MscIpiFrDnaCugComponentName_Object = MibTableColumn
mscIpiFrDnaCugComponentName = _MscIpiFrDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 1, 1, 2),
    _MscIpiFrDnaCugComponentName_Type()
)
mscIpiFrDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugComponentName.setStatus("mandatory")
_MscIpiFrDnaCugStorageType_Type = StorageType
_MscIpiFrDnaCugStorageType_Object = MibTableColumn
mscIpiFrDnaCugStorageType = _MscIpiFrDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 1, 1, 4),
    _MscIpiFrDnaCugStorageType_Type()
)
mscIpiFrDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugStorageType.setStatus("mandatory")


class _MscIpiFrDnaCugIndex_Type(Integer32):
    """Custom type mscIpiFrDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpiFrDnaCugIndex_Type.__name__ = "Integer32"
_MscIpiFrDnaCugIndex_Object = MibTableColumn
mscIpiFrDnaCugIndex = _MscIpiFrDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 1, 1, 10),
    _MscIpiFrDnaCugIndex_Type()
)
mscIpiFrDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugIndex.setStatus("mandatory")
_MscIpiFrDnaCugCugOptionsTable_Object = MibTable
mscIpiFrDnaCugCugOptionsTable = _MscIpiFrDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrDnaCugCugOptionsTable.setStatus("mandatory")
_MscIpiFrDnaCugCugOptionsEntry_Object = MibTableRow
mscIpiFrDnaCugCugOptionsEntry = _MscIpiFrDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 10, 1)
)
mscIpiFrDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrDnaCugCugOptionsEntry.setStatus("mandatory")


class _MscIpiFrDnaCugType_Type(Integer32):
    """Custom type mscIpiFrDnaCugType based on Integer32"""
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


_MscIpiFrDnaCugType_Type.__name__ = "Integer32"
_MscIpiFrDnaCugType_Object = MibTableColumn
mscIpiFrDnaCugType = _MscIpiFrDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 10, 1, 1),
    _MscIpiFrDnaCugType_Type()
)
mscIpiFrDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugType.setStatus("mandatory")


class _MscIpiFrDnaCugDnic_Type(DigitString):
    """Custom type mscIpiFrDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscIpiFrDnaCugDnic_Type.__name__ = "DigitString"
_MscIpiFrDnaCugDnic_Object = MibTableColumn
mscIpiFrDnaCugDnic = _MscIpiFrDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 10, 1, 2),
    _MscIpiFrDnaCugDnic_Type()
)
mscIpiFrDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugDnic.setStatus("mandatory")


class _MscIpiFrDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscIpiFrDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscIpiFrDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscIpiFrDnaCugInterlockCode_Object = MibTableColumn
mscIpiFrDnaCugInterlockCode = _MscIpiFrDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 10, 1, 3),
    _MscIpiFrDnaCugInterlockCode_Type()
)
mscIpiFrDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugInterlockCode.setStatus("mandatory")


class _MscIpiFrDnaCugIncCalls_Type(Integer32):
    """Custom type mscIpiFrDnaCugIncCalls based on Integer32"""
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


_MscIpiFrDnaCugIncCalls_Type.__name__ = "Integer32"
_MscIpiFrDnaCugIncCalls_Object = MibTableColumn
mscIpiFrDnaCugIncCalls = _MscIpiFrDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 2, 10, 1, 6),
    _MscIpiFrDnaCugIncCalls_Type()
)
mscIpiFrDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaCugIncCalls.setStatus("mandatory")
_MscIpiFrDnaAddressTable_Object = MibTable
mscIpiFrDnaAddressTable = _MscIpiFrDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrDnaAddressTable.setStatus("mandatory")
_MscIpiFrDnaAddressEntry_Object = MibTableRow
mscIpiFrDnaAddressEntry = _MscIpiFrDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 10, 1)
)
mscIpiFrDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrDnaAddressEntry.setStatus("mandatory")


class _MscIpiFrDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscIpiFrDnaNumberingPlanIndicator based on Integer32"""
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


_MscIpiFrDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscIpiFrDnaNumberingPlanIndicator_Object = MibTableColumn
mscIpiFrDnaNumberingPlanIndicator = _MscIpiFrDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 10, 1, 1),
    _MscIpiFrDnaNumberingPlanIndicator_Type()
)
mscIpiFrDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscIpiFrDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscIpiFrDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpiFrDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscIpiFrDnaDataNetworkAddress_Object = MibTableColumn
mscIpiFrDnaDataNetworkAddress = _MscIpiFrDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 10, 1, 2),
    _MscIpiFrDnaDataNetworkAddress_Type()
)
mscIpiFrDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaDataNetworkAddress.setStatus("mandatory")
_MscIpiFrDnaOutgoingOptionsTable_Object = MibTable
mscIpiFrDnaOutgoingOptionsTable = _MscIpiFrDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11)
)
if mibBuilder.loadTexts:
    mscIpiFrDnaOutgoingOptionsTable.setStatus("mandatory")
_MscIpiFrDnaOutgoingOptionsEntry_Object = MibTableRow
mscIpiFrDnaOutgoingOptionsEntry = _MscIpiFrDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11, 1)
)
mscIpiFrDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscIpiFrDnaOutCalls_Type(Integer32):
    """Custom type mscIpiFrDnaOutCalls based on Integer32"""
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


_MscIpiFrDnaOutCalls_Type.__name__ = "Integer32"
_MscIpiFrDnaOutCalls_Object = MibTableColumn
mscIpiFrDnaOutCalls = _MscIpiFrDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11, 1, 1),
    _MscIpiFrDnaOutCalls_Type()
)
mscIpiFrDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaOutCalls.setStatus("mandatory")


class _MscIpiFrDnaOutDefaultPriority_Type(Integer32):
    """Custom type mscIpiFrDnaOutDefaultPriority based on Integer32"""
    defaultValue = 1

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


_MscIpiFrDnaOutDefaultPriority_Type.__name__ = "Integer32"
_MscIpiFrDnaOutDefaultPriority_Object = MibTableColumn
mscIpiFrDnaOutDefaultPriority = _MscIpiFrDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11, 1, 7),
    _MscIpiFrDnaOutDefaultPriority_Type()
)
mscIpiFrDnaOutDefaultPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaOutDefaultPriority.setStatus("mandatory")


class _MscIpiFrDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type mscIpiFrDnaOutDefaultPathSensitivity based on Integer32"""
    defaultValue = 1

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


_MscIpiFrDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_MscIpiFrDnaOutDefaultPathSensitivity_Object = MibTableColumn
mscIpiFrDnaOutDefaultPathSensitivity = _MscIpiFrDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11, 1, 11),
    _MscIpiFrDnaOutDefaultPathSensitivity_Type()
)
mscIpiFrDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _MscIpiFrDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type mscIpiFrDnaOutPathSensitivityOverRide based on Integer32"""
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


_MscIpiFrDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_MscIpiFrDnaOutPathSensitivityOverRide_Object = MibTableColumn
mscIpiFrDnaOutPathSensitivityOverRide = _MscIpiFrDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11, 1, 12),
    _MscIpiFrDnaOutPathSensitivityOverRide_Type()
)
mscIpiFrDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _MscIpiFrDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mscIpiFrDnaDefaultTransferPriority based on Integer32"""
    defaultValue = 9

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


_MscIpiFrDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MscIpiFrDnaDefaultTransferPriority_Object = MibTableColumn
mscIpiFrDnaDefaultTransferPriority = _MscIpiFrDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11, 1, 18),
    _MscIpiFrDnaDefaultTransferPriority_Type()
)
mscIpiFrDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaDefaultTransferPriority.setStatus("mandatory")


class _MscIpiFrDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type mscIpiFrDnaTransferPriorityOverRide based on Integer32"""
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


_MscIpiFrDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_MscIpiFrDnaTransferPriorityOverRide_Object = MibTableColumn
mscIpiFrDnaTransferPriorityOverRide = _MscIpiFrDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 11, 1, 19),
    _MscIpiFrDnaTransferPriorityOverRide_Type()
)
mscIpiFrDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaTransferPriorityOverRide.setStatus("mandatory")
_MscIpiFrDnaIncomingOptionsTable_Object = MibTable
mscIpiFrDnaIncomingOptionsTable = _MscIpiFrDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 12)
)
if mibBuilder.loadTexts:
    mscIpiFrDnaIncomingOptionsTable.setStatus("mandatory")
_MscIpiFrDnaIncomingOptionsEntry_Object = MibTableRow
mscIpiFrDnaIncomingOptionsEntry = _MscIpiFrDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 12, 1)
)
mscIpiFrDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscIpiFrDnaIncCalls_Type(Integer32):
    """Custom type mscIpiFrDnaIncCalls based on Integer32"""
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


_MscIpiFrDnaIncCalls_Type.__name__ = "Integer32"
_MscIpiFrDnaIncCalls_Object = MibTableColumn
mscIpiFrDnaIncCalls = _MscIpiFrDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 12, 1, 1),
    _MscIpiFrDnaIncCalls_Type()
)
mscIpiFrDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaIncCalls.setStatus("mandatory")


class _MscIpiFrDnaIncAccess_Type(Integer32):
    """Custom type mscIpiFrDnaIncAccess based on Integer32"""
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


_MscIpiFrDnaIncAccess_Type.__name__ = "Integer32"
_MscIpiFrDnaIncAccess_Object = MibTableColumn
mscIpiFrDnaIncAccess = _MscIpiFrDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 12, 1, 9),
    _MscIpiFrDnaIncAccess_Type()
)
mscIpiFrDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaIncAccess.setStatus("mandatory")
_MscIpiFrDnaCallOptionsTable_Object = MibTable
mscIpiFrDnaCallOptionsTable = _MscIpiFrDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 13)
)
if mibBuilder.loadTexts:
    mscIpiFrDnaCallOptionsTable.setStatus("mandatory")
_MscIpiFrDnaCallOptionsEntry_Object = MibTableRow
mscIpiFrDnaCallOptionsEntry = _MscIpiFrDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 13, 1)
)
mscIpiFrDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrDnaCallOptionsEntry.setStatus("mandatory")


class _MscIpiFrDnaServiceCategory_Type(Integer32):
    """Custom type mscIpiFrDnaServiceCategory based on Integer32"""
    defaultValue = 32

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
          ("hdsp3270", 16),
          ("hostIti", 14),
          ("iam", 8),
          ("ici", 6),
          ("ipiFr", 32),
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


_MscIpiFrDnaServiceCategory_Type.__name__ = "Integer32"
_MscIpiFrDnaServiceCategory_Object = MibTableColumn
mscIpiFrDnaServiceCategory = _MscIpiFrDnaServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 13, 1, 1),
    _MscIpiFrDnaServiceCategory_Type()
)
mscIpiFrDnaServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrDnaServiceCategory.setStatus("mandatory")


class _MscIpiFrDnaAccountClass_Type(Unsigned32):
    """Custom type mscIpiFrDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpiFrDnaAccountClass_Type.__name__ = "Unsigned32"
_MscIpiFrDnaAccountClass_Object = MibTableColumn
mscIpiFrDnaAccountClass = _MscIpiFrDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 13, 1, 10),
    _MscIpiFrDnaAccountClass_Type()
)
mscIpiFrDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaAccountClass.setStatus("mandatory")


class _MscIpiFrDnaServiceExchange_Type(Unsigned32):
    """Custom type mscIpiFrDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpiFrDnaServiceExchange_Type.__name__ = "Unsigned32"
_MscIpiFrDnaServiceExchange_Object = MibTableColumn
mscIpiFrDnaServiceExchange = _MscIpiFrDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 2, 13, 1, 12),
    _MscIpiFrDnaServiceExchange_Type()
)
mscIpiFrDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrDnaServiceExchange.setStatus("mandatory")
_MscIpiFrLcn_ObjectIdentity = ObjectIdentity
mscIpiFrLcn = _MscIpiFrLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4)
)
_MscIpiFrLcnRowStatusTable_Object = MibTable
mscIpiFrLcnRowStatusTable = _MscIpiFrLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnRowStatusTable.setStatus("mandatory")
_MscIpiFrLcnRowStatusEntry_Object = MibTableRow
mscIpiFrLcnRowStatusEntry = _MscIpiFrLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 1, 1)
)
mscIpiFrLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnRowStatusEntry.setStatus("mandatory")
_MscIpiFrLcnRowStatus_Type = RowStatus
_MscIpiFrLcnRowStatus_Object = MibTableColumn
mscIpiFrLcnRowStatus = _MscIpiFrLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 1, 1, 1),
    _MscIpiFrLcnRowStatus_Type()
)
mscIpiFrLcnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnRowStatus.setStatus("mandatory")
_MscIpiFrLcnComponentName_Type = DisplayString
_MscIpiFrLcnComponentName_Object = MibTableColumn
mscIpiFrLcnComponentName = _MscIpiFrLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 1, 1, 2),
    _MscIpiFrLcnComponentName_Type()
)
mscIpiFrLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnComponentName.setStatus("mandatory")
_MscIpiFrLcnStorageType_Type = StorageType
_MscIpiFrLcnStorageType_Object = MibTableColumn
mscIpiFrLcnStorageType = _MscIpiFrLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 1, 1, 4),
    _MscIpiFrLcnStorageType_Type()
)
mscIpiFrLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnStorageType.setStatus("mandatory")


class _MscIpiFrLcnIndex_Type(Integer32):
    """Custom type mscIpiFrLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 39),
    )


_MscIpiFrLcnIndex_Type.__name__ = "Integer32"
_MscIpiFrLcnIndex_Object = MibTableColumn
mscIpiFrLcnIndex = _MscIpiFrLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 1, 1, 10),
    _MscIpiFrLcnIndex_Type()
)
mscIpiFrLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrLcnIndex.setStatus("mandatory")
_MscIpiFrLcnDc_ObjectIdentity = ObjectIdentity
mscIpiFrLcnDc = _MscIpiFrLcnDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2)
)
_MscIpiFrLcnDcRowStatusTable_Object = MibTable
mscIpiFrLcnDcRowStatusTable = _MscIpiFrLcnDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnDcRowStatusTable.setStatus("mandatory")
_MscIpiFrLcnDcRowStatusEntry_Object = MibTableRow
mscIpiFrLcnDcRowStatusEntry = _MscIpiFrLcnDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 1, 1)
)
mscIpiFrLcnDcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnDcIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnDcRowStatusEntry.setStatus("mandatory")
_MscIpiFrLcnDcRowStatus_Type = RowStatus
_MscIpiFrLcnDcRowStatus_Object = MibTableColumn
mscIpiFrLcnDcRowStatus = _MscIpiFrLcnDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 1, 1, 1),
    _MscIpiFrLcnDcRowStatus_Type()
)
mscIpiFrLcnDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcRowStatus.setStatus("mandatory")
_MscIpiFrLcnDcComponentName_Type = DisplayString
_MscIpiFrLcnDcComponentName_Object = MibTableColumn
mscIpiFrLcnDcComponentName = _MscIpiFrLcnDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 1, 1, 2),
    _MscIpiFrLcnDcComponentName_Type()
)
mscIpiFrLcnDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcComponentName.setStatus("mandatory")
_MscIpiFrLcnDcStorageType_Type = StorageType
_MscIpiFrLcnDcStorageType_Object = MibTableColumn
mscIpiFrLcnDcStorageType = _MscIpiFrLcnDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 1, 1, 4),
    _MscIpiFrLcnDcStorageType_Type()
)
mscIpiFrLcnDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcStorageType.setStatus("mandatory")
_MscIpiFrLcnDcIndex_Type = NonReplicated
_MscIpiFrLcnDcIndex_Object = MibTableColumn
mscIpiFrLcnDcIndex = _MscIpiFrLcnDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 1, 1, 10),
    _MscIpiFrLcnDcIndex_Type()
)
mscIpiFrLcnDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcIndex.setStatus("mandatory")
_MscIpiFrLcnDcOptionsTable_Object = MibTable
mscIpiFrLcnDcOptionsTable = _MscIpiFrLcnDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnDcOptionsTable.setStatus("mandatory")
_MscIpiFrLcnDcOptionsEntry_Object = MibTableRow
mscIpiFrLcnDcOptionsEntry = _MscIpiFrLcnDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10, 1)
)
mscIpiFrLcnDcOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnDcIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnDcOptionsEntry.setStatus("mandatory")


class _MscIpiFrLcnDcRemoteNpi_Type(Integer32):
    """Custom type mscIpiFrLcnDcRemoteNpi based on Integer32"""
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


_MscIpiFrLcnDcRemoteNpi_Type.__name__ = "Integer32"
_MscIpiFrLcnDcRemoteNpi_Object = MibTableColumn
mscIpiFrLcnDcRemoteNpi = _MscIpiFrLcnDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10, 1, 3),
    _MscIpiFrLcnDcRemoteNpi_Type()
)
mscIpiFrLcnDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcRemoteNpi.setStatus("mandatory")


class _MscIpiFrLcnDcRemoteDna_Type(DigitString):
    """Custom type mscIpiFrLcnDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpiFrLcnDcRemoteDna_Type.__name__ = "DigitString"
_MscIpiFrLcnDcRemoteDna_Object = MibTableColumn
mscIpiFrLcnDcRemoteDna = _MscIpiFrLcnDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10, 1, 4),
    _MscIpiFrLcnDcRemoteDna_Type()
)
mscIpiFrLcnDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcRemoteDna.setStatus("mandatory")


class _MscIpiFrLcnDcRemoteDlci_Type(Unsigned32):
    """Custom type mscIpiFrLcnDcRemoteDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_MscIpiFrLcnDcRemoteDlci_Type.__name__ = "Unsigned32"
_MscIpiFrLcnDcRemoteDlci_Object = MibTableColumn
mscIpiFrLcnDcRemoteDlci = _MscIpiFrLcnDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10, 1, 5),
    _MscIpiFrLcnDcRemoteDlci_Type()
)
mscIpiFrLcnDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcRemoteDlci.setStatus("mandatory")


class _MscIpiFrLcnDcType_Type(Integer32):
    """Custom type mscIpiFrLcnDcType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanentMaster", 1),
          ("permanentSlave", 2))
    )


_MscIpiFrLcnDcType_Type.__name__ = "Integer32"
_MscIpiFrLcnDcType_Object = MibTableColumn
mscIpiFrLcnDcType = _MscIpiFrLcnDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10, 1, 6),
    _MscIpiFrLcnDcType_Type()
)
mscIpiFrLcnDcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcType.setStatus("mandatory")


class _MscIpiFrLcnDcTransferPriority_Type(Integer32):
    """Custom type mscIpiFrLcnDcTransferPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 9),
          ("normal", 0),
          ("useDnaDefTP", 255))
    )


_MscIpiFrLcnDcTransferPriority_Type.__name__ = "Integer32"
_MscIpiFrLcnDcTransferPriority_Object = MibTableColumn
mscIpiFrLcnDcTransferPriority = _MscIpiFrLcnDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10, 1, 9),
    _MscIpiFrLcnDcTransferPriority_Type()
)
mscIpiFrLcnDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcTransferPriority.setStatus("mandatory")


class _MscIpiFrLcnDcDiscardPriority_Type(Integer32):
    """Custom type mscIpiFrLcnDcDiscardPriority based on Integer32"""
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


_MscIpiFrLcnDcDiscardPriority_Type.__name__ = "Integer32"
_MscIpiFrLcnDcDiscardPriority_Object = MibTableColumn
mscIpiFrLcnDcDiscardPriority = _MscIpiFrLcnDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 10, 1, 10),
    _MscIpiFrLcnDcDiscardPriority_Type()
)
mscIpiFrLcnDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcDiscardPriority.setStatus("mandatory")
_MscIpiFrLcnDcNfaTable_Object = MibTable
mscIpiFrLcnDcNfaTable = _MscIpiFrLcnDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 222)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnDcNfaTable.setStatus("obsolete")
_MscIpiFrLcnDcNfaEntry_Object = MibTableRow
mscIpiFrLcnDcNfaEntry = _MscIpiFrLcnDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 222, 1)
)
mscIpiFrLcnDcNfaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnDcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnDcNfaIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnDcNfaEntry.setStatus("obsolete")


class _MscIpiFrLcnDcNfaIndex_Type(Integer32):
    """Custom type mscIpiFrLcnDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MscIpiFrLcnDcNfaIndex_Type.__name__ = "Integer32"
_MscIpiFrLcnDcNfaIndex_Object = MibTableColumn
mscIpiFrLcnDcNfaIndex = _MscIpiFrLcnDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 222, 1, 1),
    _MscIpiFrLcnDcNfaIndex_Type()
)
mscIpiFrLcnDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcNfaIndex.setStatus("obsolete")


class _MscIpiFrLcnDcNfaValue_Type(HexString):
    """Custom type mscIpiFrLcnDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MscIpiFrLcnDcNfaValue_Type.__name__ = "HexString"
_MscIpiFrLcnDcNfaValue_Object = MibTableColumn
mscIpiFrLcnDcNfaValue = _MscIpiFrLcnDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 222, 1, 2),
    _MscIpiFrLcnDcNfaValue_Type()
)
mscIpiFrLcnDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcNfaValue.setStatus("obsolete")
_MscIpiFrLcnDcNfaRowStatus_Type = RowStatus
_MscIpiFrLcnDcNfaRowStatus_Object = MibTableColumn
mscIpiFrLcnDcNfaRowStatus = _MscIpiFrLcnDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 2, 222, 1, 3),
    _MscIpiFrLcnDcNfaRowStatus_Type()
)
mscIpiFrLcnDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnDcNfaRowStatus.setStatus("obsolete")
_MscIpiFrLcnVc_ObjectIdentity = ObjectIdentity
mscIpiFrLcnVc = _MscIpiFrLcnVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3)
)
_MscIpiFrLcnVcRowStatusTable_Object = MibTable
mscIpiFrLcnVcRowStatusTable = _MscIpiFrLcnVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcRowStatusTable.setStatus("mandatory")
_MscIpiFrLcnVcRowStatusEntry_Object = MibTableRow
mscIpiFrLcnVcRowStatusEntry = _MscIpiFrLcnVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 1, 1)
)
mscIpiFrLcnVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcRowStatusEntry.setStatus("mandatory")
_MscIpiFrLcnVcRowStatus_Type = RowStatus
_MscIpiFrLcnVcRowStatus_Object = MibTableColumn
mscIpiFrLcnVcRowStatus = _MscIpiFrLcnVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 1, 1, 1),
    _MscIpiFrLcnVcRowStatus_Type()
)
mscIpiFrLcnVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcRowStatus.setStatus("mandatory")
_MscIpiFrLcnVcComponentName_Type = DisplayString
_MscIpiFrLcnVcComponentName_Object = MibTableColumn
mscIpiFrLcnVcComponentName = _MscIpiFrLcnVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 1, 1, 2),
    _MscIpiFrLcnVcComponentName_Type()
)
mscIpiFrLcnVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcComponentName.setStatus("mandatory")
_MscIpiFrLcnVcStorageType_Type = StorageType
_MscIpiFrLcnVcStorageType_Object = MibTableColumn
mscIpiFrLcnVcStorageType = _MscIpiFrLcnVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 1, 1, 4),
    _MscIpiFrLcnVcStorageType_Type()
)
mscIpiFrLcnVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcStorageType.setStatus("mandatory")
_MscIpiFrLcnVcIndex_Type = NonReplicated
_MscIpiFrLcnVcIndex_Object = MibTableColumn
mscIpiFrLcnVcIndex = _MscIpiFrLcnVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 1, 1, 10),
    _MscIpiFrLcnVcIndex_Type()
)
mscIpiFrLcnVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcIndex.setStatus("mandatory")
_MscIpiFrLcnVcCadTable_Object = MibTable
mscIpiFrLcnVcCadTable = _MscIpiFrLcnVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCadTable.setStatus("mandatory")
_MscIpiFrLcnVcCadEntry_Object = MibTableRow
mscIpiFrLcnVcCadEntry = _MscIpiFrLcnVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1)
)
mscIpiFrLcnVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCadEntry.setStatus("mandatory")


class _MscIpiFrLcnVcType_Type(Integer32):
    """Custom type mscIpiFrLcnVcType based on Integer32"""
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


_MscIpiFrLcnVcType_Type.__name__ = "Integer32"
_MscIpiFrLcnVcType_Object = MibTableColumn
mscIpiFrLcnVcType = _MscIpiFrLcnVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 1),
    _MscIpiFrLcnVcType_Type()
)
mscIpiFrLcnVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcType.setStatus("mandatory")


class _MscIpiFrLcnVcState_Type(Integer32):
    """Custom type mscIpiFrLcnVcState based on Integer32"""
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


_MscIpiFrLcnVcState_Type.__name__ = "Integer32"
_MscIpiFrLcnVcState_Object = MibTableColumn
mscIpiFrLcnVcState = _MscIpiFrLcnVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 2),
    _MscIpiFrLcnVcState_Type()
)
mscIpiFrLcnVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcState.setStatus("mandatory")


class _MscIpiFrLcnVcPreviousState_Type(Integer32):
    """Custom type mscIpiFrLcnVcPreviousState based on Integer32"""
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


_MscIpiFrLcnVcPreviousState_Type.__name__ = "Integer32"
_MscIpiFrLcnVcPreviousState_Object = MibTableColumn
mscIpiFrLcnVcPreviousState = _MscIpiFrLcnVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 3),
    _MscIpiFrLcnVcPreviousState_Type()
)
mscIpiFrLcnVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPreviousState.setStatus("mandatory")


class _MscIpiFrLcnVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpiFrLcnVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcDiagnosticCode_Object = MibTableColumn
mscIpiFrLcnVcDiagnosticCode = _MscIpiFrLcnVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 4),
    _MscIpiFrLcnVcDiagnosticCode_Type()
)
mscIpiFrLcnVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcDiagnosticCode.setStatus("mandatory")


class _MscIpiFrLcnVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpiFrLcnVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcPreviousDiagnosticCode_Object = MibTableColumn
mscIpiFrLcnVcPreviousDiagnosticCode = _MscIpiFrLcnVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 5),
    _MscIpiFrLcnVcPreviousDiagnosticCode_Type()
)
mscIpiFrLcnVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscIpiFrLcnVcCalledNpi_Type(Integer32):
    """Custom type mscIpiFrLcnVcCalledNpi based on Integer32"""
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


_MscIpiFrLcnVcCalledNpi_Type.__name__ = "Integer32"
_MscIpiFrLcnVcCalledNpi_Object = MibTableColumn
mscIpiFrLcnVcCalledNpi = _MscIpiFrLcnVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 6),
    _MscIpiFrLcnVcCalledNpi_Type()
)
mscIpiFrLcnVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCalledNpi.setStatus("mandatory")


class _MscIpiFrLcnVcCalledDna_Type(DigitString):
    """Custom type mscIpiFrLcnVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpiFrLcnVcCalledDna_Type.__name__ = "DigitString"
_MscIpiFrLcnVcCalledDna_Object = MibTableColumn
mscIpiFrLcnVcCalledDna = _MscIpiFrLcnVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 7),
    _MscIpiFrLcnVcCalledDna_Type()
)
mscIpiFrLcnVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCalledDna.setStatus("mandatory")


class _MscIpiFrLcnVcCalledLcn_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscIpiFrLcnVcCalledLcn_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcCalledLcn_Object = MibTableColumn
mscIpiFrLcnVcCalledLcn = _MscIpiFrLcnVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 8),
    _MscIpiFrLcnVcCalledLcn_Type()
)
mscIpiFrLcnVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCalledLcn.setStatus("mandatory")


class _MscIpiFrLcnVcCallingNpi_Type(Integer32):
    """Custom type mscIpiFrLcnVcCallingNpi based on Integer32"""
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


_MscIpiFrLcnVcCallingNpi_Type.__name__ = "Integer32"
_MscIpiFrLcnVcCallingNpi_Object = MibTableColumn
mscIpiFrLcnVcCallingNpi = _MscIpiFrLcnVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 9),
    _MscIpiFrLcnVcCallingNpi_Type()
)
mscIpiFrLcnVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCallingNpi.setStatus("mandatory")


class _MscIpiFrLcnVcCallingDna_Type(DigitString):
    """Custom type mscIpiFrLcnVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpiFrLcnVcCallingDna_Type.__name__ = "DigitString"
_MscIpiFrLcnVcCallingDna_Object = MibTableColumn
mscIpiFrLcnVcCallingDna = _MscIpiFrLcnVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 10),
    _MscIpiFrLcnVcCallingDna_Type()
)
mscIpiFrLcnVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCallingDna.setStatus("mandatory")


class _MscIpiFrLcnVcCallingLcn_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscIpiFrLcnVcCallingLcn_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcCallingLcn_Object = MibTableColumn
mscIpiFrLcnVcCallingLcn = _MscIpiFrLcnVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 11),
    _MscIpiFrLcnVcCallingLcn_Type()
)
mscIpiFrLcnVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCallingLcn.setStatus("mandatory")


class _MscIpiFrLcnVcAccountingEnabled_Type(Integer32):
    """Custom type mscIpiFrLcnVcAccountingEnabled based on Integer32"""
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


_MscIpiFrLcnVcAccountingEnabled_Type.__name__ = "Integer32"
_MscIpiFrLcnVcAccountingEnabled_Object = MibTableColumn
mscIpiFrLcnVcAccountingEnabled = _MscIpiFrLcnVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 12),
    _MscIpiFrLcnVcAccountingEnabled_Type()
)
mscIpiFrLcnVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcAccountingEnabled.setStatus("mandatory")


class _MscIpiFrLcnVcFastSelectCall_Type(Integer32):
    """Custom type mscIpiFrLcnVcFastSelectCall based on Integer32"""
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


_MscIpiFrLcnVcFastSelectCall_Type.__name__ = "Integer32"
_MscIpiFrLcnVcFastSelectCall_Object = MibTableColumn
mscIpiFrLcnVcFastSelectCall = _MscIpiFrLcnVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 13),
    _MscIpiFrLcnVcFastSelectCall_Type()
)
mscIpiFrLcnVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcFastSelectCall.setStatus("mandatory")


class _MscIpiFrLcnVcPathReliability_Type(Integer32):
    """Custom type mscIpiFrLcnVcPathReliability based on Integer32"""
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


_MscIpiFrLcnVcPathReliability_Type.__name__ = "Integer32"
_MscIpiFrLcnVcPathReliability_Object = MibTableColumn
mscIpiFrLcnVcPathReliability = _MscIpiFrLcnVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 19),
    _MscIpiFrLcnVcPathReliability_Type()
)
mscIpiFrLcnVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPathReliability.setStatus("mandatory")


class _MscIpiFrLcnVcAccountingEnd_Type(Integer32):
    """Custom type mscIpiFrLcnVcAccountingEnd based on Integer32"""
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


_MscIpiFrLcnVcAccountingEnd_Type.__name__ = "Integer32"
_MscIpiFrLcnVcAccountingEnd_Object = MibTableColumn
mscIpiFrLcnVcAccountingEnd = _MscIpiFrLcnVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 20),
    _MscIpiFrLcnVcAccountingEnd_Type()
)
mscIpiFrLcnVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcAccountingEnd.setStatus("mandatory")


class _MscIpiFrLcnVcPriority_Type(Integer32):
    """Custom type mscIpiFrLcnVcPriority based on Integer32"""
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


_MscIpiFrLcnVcPriority_Type.__name__ = "Integer32"
_MscIpiFrLcnVcPriority_Object = MibTableColumn
mscIpiFrLcnVcPriority = _MscIpiFrLcnVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 21),
    _MscIpiFrLcnVcPriority_Type()
)
mscIpiFrLcnVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPriority.setStatus("mandatory")


class _MscIpiFrLcnVcSegmentSize_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscIpiFrLcnVcSegmentSize_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcSegmentSize_Object = MibTableColumn
mscIpiFrLcnVcSegmentSize = _MscIpiFrLcnVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 22),
    _MscIpiFrLcnVcSegmentSize_Type()
)
mscIpiFrLcnVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcSegmentSize.setStatus("mandatory")


class _MscIpiFrLcnVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscIpiFrLcnVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcMaxSubnetPktSize_Object = MibTableColumn
mscIpiFrLcnVcMaxSubnetPktSize = _MscIpiFrLcnVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 27),
    _MscIpiFrLcnVcMaxSubnetPktSize_Type()
)
mscIpiFrLcnVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcMaxSubnetPktSize.setStatus("mandatory")


class _MscIpiFrLcnVcRcosToNetwork_Type(Integer32):
    """Custom type mscIpiFrLcnVcRcosToNetwork based on Integer32"""
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


_MscIpiFrLcnVcRcosToNetwork_Type.__name__ = "Integer32"
_MscIpiFrLcnVcRcosToNetwork_Object = MibTableColumn
mscIpiFrLcnVcRcosToNetwork = _MscIpiFrLcnVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 28),
    _MscIpiFrLcnVcRcosToNetwork_Type()
)
mscIpiFrLcnVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcRcosToNetwork.setStatus("mandatory")


class _MscIpiFrLcnVcRcosFromNetwork_Type(Integer32):
    """Custom type mscIpiFrLcnVcRcosFromNetwork based on Integer32"""
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


_MscIpiFrLcnVcRcosFromNetwork_Type.__name__ = "Integer32"
_MscIpiFrLcnVcRcosFromNetwork_Object = MibTableColumn
mscIpiFrLcnVcRcosFromNetwork = _MscIpiFrLcnVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 29),
    _MscIpiFrLcnVcRcosFromNetwork_Type()
)
mscIpiFrLcnVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcRcosFromNetwork.setStatus("mandatory")


class _MscIpiFrLcnVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type mscIpiFrLcnVcEmissionPriorityToNetwork based on Integer32"""
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


_MscIpiFrLcnVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_MscIpiFrLcnVcEmissionPriorityToNetwork_Object = MibTableColumn
mscIpiFrLcnVcEmissionPriorityToNetwork = _MscIpiFrLcnVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 30),
    _MscIpiFrLcnVcEmissionPriorityToNetwork_Type()
)
mscIpiFrLcnVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcEmissionPriorityToNetwork.setStatus("mandatory")


class _MscIpiFrLcnVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type mscIpiFrLcnVcEmissionPriorityFromNetwork based on Integer32"""
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


_MscIpiFrLcnVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_MscIpiFrLcnVcEmissionPriorityFromNetwork_Object = MibTableColumn
mscIpiFrLcnVcEmissionPriorityFromNetwork = _MscIpiFrLcnVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 31),
    _MscIpiFrLcnVcEmissionPriorityFromNetwork_Type()
)
mscIpiFrLcnVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _MscIpiFrLcnVcDataPath_Type(AsciiString):
    """Custom type mscIpiFrLcnVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MscIpiFrLcnVcDataPath_Type.__name__ = "AsciiString"
_MscIpiFrLcnVcDataPath_Object = MibTableColumn
mscIpiFrLcnVcDataPath = _MscIpiFrLcnVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 10, 1, 32),
    _MscIpiFrLcnVcDataPath_Type()
)
mscIpiFrLcnVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcDataPath.setStatus("mandatory")
_MscIpiFrLcnVcIntdTable_Object = MibTable
mscIpiFrLcnVcIntdTable = _MscIpiFrLcnVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcIntdTable.setStatus("mandatory")
_MscIpiFrLcnVcIntdEntry_Object = MibTableRow
mscIpiFrLcnVcIntdEntry = _MscIpiFrLcnVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11, 1)
)
mscIpiFrLcnVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcIntdEntry.setStatus("mandatory")


class _MscIpiFrLcnVcCallReferenceNumber_Type(Hex):
    """Custom type mscIpiFrLcnVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpiFrLcnVcCallReferenceNumber_Type.__name__ = "Hex"
_MscIpiFrLcnVcCallReferenceNumber_Object = MibTableColumn
mscIpiFrLcnVcCallReferenceNumber = _MscIpiFrLcnVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11, 1, 1),
    _MscIpiFrLcnVcCallReferenceNumber_Type()
)
mscIpiFrLcnVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCallReferenceNumber.setStatus("obsolete")


class _MscIpiFrLcnVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpiFrLcnVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcElapsedTimeTillNow_Object = MibTableColumn
mscIpiFrLcnVcElapsedTimeTillNow = _MscIpiFrLcnVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11, 1, 2),
    _MscIpiFrLcnVcElapsedTimeTillNow_Type()
)
mscIpiFrLcnVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcElapsedTimeTillNow.setStatus("mandatory")


class _MscIpiFrLcnVcSegmentsRx_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpiFrLcnVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcSegmentsRx_Object = MibTableColumn
mscIpiFrLcnVcSegmentsRx = _MscIpiFrLcnVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11, 1, 3),
    _MscIpiFrLcnVcSegmentsRx_Type()
)
mscIpiFrLcnVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcSegmentsRx.setStatus("mandatory")


class _MscIpiFrLcnVcSegmentsSent_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpiFrLcnVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcSegmentsSent_Object = MibTableColumn
mscIpiFrLcnVcSegmentsSent = _MscIpiFrLcnVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11, 1, 4),
    _MscIpiFrLcnVcSegmentsSent_Type()
)
mscIpiFrLcnVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcSegmentsSent.setStatus("mandatory")


class _MscIpiFrLcnVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscIpiFrLcnVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscIpiFrLcnVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscIpiFrLcnVcStartTime_Object = MibTableColumn
mscIpiFrLcnVcStartTime = _MscIpiFrLcnVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11, 1, 5),
    _MscIpiFrLcnVcStartTime_Type()
)
mscIpiFrLcnVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcStartTime.setStatus("mandatory")


class _MscIpiFrLcnVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscIpiFrLcnVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcCallReferenceNumberDecimal_Object = MibTableColumn
mscIpiFrLcnVcCallReferenceNumberDecimal = _MscIpiFrLcnVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 11, 1, 7),
    _MscIpiFrLcnVcCallReferenceNumberDecimal_Type()
)
mscIpiFrLcnVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscIpiFrLcnVcFrdTable_Object = MibTable
mscIpiFrLcnVcFrdTable = _MscIpiFrLcnVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcFrdTable.setStatus("mandatory")
_MscIpiFrLcnVcFrdEntry_Object = MibTableRow
mscIpiFrLcnVcFrdEntry = _MscIpiFrLcnVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1)
)
mscIpiFrLcnVcFrdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcFrdEntry.setStatus("mandatory")


class _MscIpiFrLcnVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcFrmCongestedToSubnet_Object = MibTableColumn
mscIpiFrLcnVcFrmCongestedToSubnet = _MscIpiFrLcnVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 2),
    _MscIpiFrLcnVcFrmCongestedToSubnet_Type()
)
mscIpiFrLcnVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcFrmCongestedToSubnet.setStatus("mandatory")


class _MscIpiFrLcnVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcCannotForwardToSubnet_Object = MibTableColumn
mscIpiFrLcnVcCannotForwardToSubnet = _MscIpiFrLcnVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 3),
    _MscIpiFrLcnVcCannotForwardToSubnet_Type()
)
mscIpiFrLcnVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCannotForwardToSubnet.setStatus("mandatory")


class _MscIpiFrLcnVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcNotDataXferToSubnet_Object = MibTableColumn
mscIpiFrLcnVcNotDataXferToSubnet = _MscIpiFrLcnVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 4),
    _MscIpiFrLcnVcNotDataXferToSubnet_Type()
)
mscIpiFrLcnVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcNotDataXferToSubnet.setStatus("mandatory")


class _MscIpiFrLcnVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscIpiFrLcnVcOutOfRangeFrmFromSubnet = _MscIpiFrLcnVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 5),
    _MscIpiFrLcnVcOutOfRangeFrmFromSubnet_Type()
)
mscIpiFrLcnVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscIpiFrLcnVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcCombErrorsFromSubnet_Object = MibTableColumn
mscIpiFrLcnVcCombErrorsFromSubnet = _MscIpiFrLcnVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 6),
    _MscIpiFrLcnVcCombErrorsFromSubnet_Type()
)
mscIpiFrLcnVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcCombErrorsFromSubnet.setStatus("mandatory")


class _MscIpiFrLcnVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcDuplicatesFromSubnet_Object = MibTableColumn
mscIpiFrLcnVcDuplicatesFromSubnet = _MscIpiFrLcnVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 7),
    _MscIpiFrLcnVcDuplicatesFromSubnet_Type()
)
mscIpiFrLcnVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscIpiFrLcnVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcNotDataXferFromSubnet_Object = MibTableColumn
mscIpiFrLcnVcNotDataXferFromSubnet = _MscIpiFrLcnVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 8),
    _MscIpiFrLcnVcNotDataXferFromSubnet_Type()
)
mscIpiFrLcnVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcNotDataXferFromSubnet.setStatus("mandatory")


class _MscIpiFrLcnVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcFrmLossTimeouts_Object = MibTableColumn
mscIpiFrLcnVcFrmLossTimeouts = _MscIpiFrLcnVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 9),
    _MscIpiFrLcnVcFrmLossTimeouts_Type()
)
mscIpiFrLcnVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcFrmLossTimeouts.setStatus("mandatory")


class _MscIpiFrLcnVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcOoSeqByteCntExceeded_Object = MibTableColumn
mscIpiFrLcnVcOoSeqByteCntExceeded = _MscIpiFrLcnVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 10),
    _MscIpiFrLcnVcOoSeqByteCntExceeded_Type()
)
mscIpiFrLcnVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcOoSeqByteCntExceeded.setStatus("mandatory")


class _MscIpiFrLcnVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcPeakOoSeqPktCount_Object = MibTableColumn
mscIpiFrLcnVcPeakOoSeqPktCount = _MscIpiFrLcnVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 11),
    _MscIpiFrLcnVcPeakOoSeqPktCount_Type()
)
mscIpiFrLcnVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPeakOoSeqPktCount.setStatus("mandatory")


class _MscIpiFrLcnVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscIpiFrLcnVcPeakOoSeqFrmForwarded = _MscIpiFrLcnVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 12),
    _MscIpiFrLcnVcPeakOoSeqFrmForwarded_Type()
)
mscIpiFrLcnVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscIpiFrLcnVcSendSequenceNumber_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcSendSequenceNumber_Object = MibTableColumn
mscIpiFrLcnVcSendSequenceNumber = _MscIpiFrLcnVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 13),
    _MscIpiFrLcnVcSendSequenceNumber_Type()
)
mscIpiFrLcnVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcSendSequenceNumber.setStatus("mandatory")


class _MscIpiFrLcnVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcPktRetryTimeouts_Object = MibTableColumn
mscIpiFrLcnVcPktRetryTimeouts = _MscIpiFrLcnVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 15),
    _MscIpiFrLcnVcPktRetryTimeouts_Type()
)
mscIpiFrLcnVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPktRetryTimeouts.setStatus("mandatory")


class _MscIpiFrLcnVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcPeakRetryQueueSize_Object = MibTableColumn
mscIpiFrLcnVcPeakRetryQueueSize = _MscIpiFrLcnVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 16),
    _MscIpiFrLcnVcPeakRetryQueueSize_Type()
)
mscIpiFrLcnVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPeakRetryQueueSize.setStatus("mandatory")


class _MscIpiFrLcnVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpiFrLcnVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcSubnetRecoveries_Object = MibTableColumn
mscIpiFrLcnVcSubnetRecoveries = _MscIpiFrLcnVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 17),
    _MscIpiFrLcnVcSubnetRecoveries_Type()
)
mscIpiFrLcnVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcSubnetRecoveries.setStatus("mandatory")


class _MscIpiFrLcnVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpiFrLcnVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcOoSeqPktCntExceeded_Object = MibTableColumn
mscIpiFrLcnVcOoSeqPktCntExceeded = _MscIpiFrLcnVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 19),
    _MscIpiFrLcnVcOoSeqPktCntExceeded_Type()
)
mscIpiFrLcnVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcOoSeqPktCntExceeded.setStatus("mandatory")


class _MscIpiFrLcnVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type mscIpiFrLcnVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_MscIpiFrLcnVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_MscIpiFrLcnVcPeakOoSeqByteCount_Object = MibTableColumn
mscIpiFrLcnVcPeakOoSeqByteCount = _MscIpiFrLcnVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 12, 1, 20),
    _MscIpiFrLcnVcPeakOoSeqByteCount_Type()
)
mscIpiFrLcnVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcPeakOoSeqByteCount.setStatus("mandatory")
_MscIpiFrLcnVcDmepTable_Object = MibTable
mscIpiFrLcnVcDmepTable = _MscIpiFrLcnVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 417)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcDmepTable.setStatus("mandatory")
_MscIpiFrLcnVcDmepEntry_Object = MibTableRow
mscIpiFrLcnVcDmepEntry = _MscIpiFrLcnVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 417, 1)
)
mscIpiFrLcnVcDmepEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnVcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnVcDmepValue"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnVcDmepEntry.setStatus("mandatory")
_MscIpiFrLcnVcDmepValue_Type = RowPointer
_MscIpiFrLcnVcDmepValue_Object = MibTableColumn
mscIpiFrLcnVcDmepValue = _MscIpiFrLcnVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 3, 417, 1, 1),
    _MscIpiFrLcnVcDmepValue_Type()
)
mscIpiFrLcnVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnVcDmepValue.setStatus("mandatory")
_MscIpiFrLcnStateTable_Object = MibTable
mscIpiFrLcnStateTable = _MscIpiFrLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnStateTable.setStatus("mandatory")
_MscIpiFrLcnStateEntry_Object = MibTableRow
mscIpiFrLcnStateEntry = _MscIpiFrLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1)
)
mscIpiFrLcnStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnStateEntry.setStatus("mandatory")


class _MscIpiFrLcnAdminState_Type(Integer32):
    """Custom type mscIpiFrLcnAdminState based on Integer32"""
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


_MscIpiFrLcnAdminState_Type.__name__ = "Integer32"
_MscIpiFrLcnAdminState_Object = MibTableColumn
mscIpiFrLcnAdminState = _MscIpiFrLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 1),
    _MscIpiFrLcnAdminState_Type()
)
mscIpiFrLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnAdminState.setStatus("mandatory")


class _MscIpiFrLcnOperationalState_Type(Integer32):
    """Custom type mscIpiFrLcnOperationalState based on Integer32"""
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


_MscIpiFrLcnOperationalState_Type.__name__ = "Integer32"
_MscIpiFrLcnOperationalState_Object = MibTableColumn
mscIpiFrLcnOperationalState = _MscIpiFrLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 2),
    _MscIpiFrLcnOperationalState_Type()
)
mscIpiFrLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnOperationalState.setStatus("mandatory")


class _MscIpiFrLcnUsageState_Type(Integer32):
    """Custom type mscIpiFrLcnUsageState based on Integer32"""
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


_MscIpiFrLcnUsageState_Type.__name__ = "Integer32"
_MscIpiFrLcnUsageState_Object = MibTableColumn
mscIpiFrLcnUsageState = _MscIpiFrLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 3),
    _MscIpiFrLcnUsageState_Type()
)
mscIpiFrLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnUsageState.setStatus("mandatory")


class _MscIpiFrLcnAvailabilityStatus_Type(OctetString):
    """Custom type mscIpiFrLcnAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscIpiFrLcnAvailabilityStatus_Type.__name__ = "OctetString"
_MscIpiFrLcnAvailabilityStatus_Object = MibTableColumn
mscIpiFrLcnAvailabilityStatus = _MscIpiFrLcnAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 4),
    _MscIpiFrLcnAvailabilityStatus_Type()
)
mscIpiFrLcnAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnAvailabilityStatus.setStatus("mandatory")


class _MscIpiFrLcnProceduralStatus_Type(OctetString):
    """Custom type mscIpiFrLcnProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscIpiFrLcnProceduralStatus_Type.__name__ = "OctetString"
_MscIpiFrLcnProceduralStatus_Object = MibTableColumn
mscIpiFrLcnProceduralStatus = _MscIpiFrLcnProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 5),
    _MscIpiFrLcnProceduralStatus_Type()
)
mscIpiFrLcnProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnProceduralStatus.setStatus("mandatory")


class _MscIpiFrLcnControlStatus_Type(OctetString):
    """Custom type mscIpiFrLcnControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscIpiFrLcnControlStatus_Type.__name__ = "OctetString"
_MscIpiFrLcnControlStatus_Object = MibTableColumn
mscIpiFrLcnControlStatus = _MscIpiFrLcnControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 6),
    _MscIpiFrLcnControlStatus_Type()
)
mscIpiFrLcnControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnControlStatus.setStatus("mandatory")


class _MscIpiFrLcnAlarmStatus_Type(OctetString):
    """Custom type mscIpiFrLcnAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscIpiFrLcnAlarmStatus_Type.__name__ = "OctetString"
_MscIpiFrLcnAlarmStatus_Object = MibTableColumn
mscIpiFrLcnAlarmStatus = _MscIpiFrLcnAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 7),
    _MscIpiFrLcnAlarmStatus_Type()
)
mscIpiFrLcnAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnAlarmStatus.setStatus("mandatory")


class _MscIpiFrLcnStandbyStatus_Type(Integer32):
    """Custom type mscIpiFrLcnStandbyStatus based on Integer32"""
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


_MscIpiFrLcnStandbyStatus_Type.__name__ = "Integer32"
_MscIpiFrLcnStandbyStatus_Object = MibTableColumn
mscIpiFrLcnStandbyStatus = _MscIpiFrLcnStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 8),
    _MscIpiFrLcnStandbyStatus_Type()
)
mscIpiFrLcnStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnStandbyStatus.setStatus("mandatory")


class _MscIpiFrLcnUnknownStatus_Type(Integer32):
    """Custom type mscIpiFrLcnUnknownStatus based on Integer32"""
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


_MscIpiFrLcnUnknownStatus_Type.__name__ = "Integer32"
_MscIpiFrLcnUnknownStatus_Object = MibTableColumn
mscIpiFrLcnUnknownStatus = _MscIpiFrLcnUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 10, 1, 9),
    _MscIpiFrLcnUnknownStatus_Type()
)
mscIpiFrLcnUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnUnknownStatus.setStatus("mandatory")
_MscIpiFrLcnOperTable_Object = MibTable
mscIpiFrLcnOperTable = _MscIpiFrLcnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnOperTable.setStatus("mandatory")
_MscIpiFrLcnOperEntry_Object = MibTableRow
mscIpiFrLcnOperEntry = _MscIpiFrLcnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11, 1)
)
mscIpiFrLcnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnOperEntry.setStatus("mandatory")


class _MscIpiFrLcnIpInterfaceDevice_Type(Integer32):
    """Custom type mscIpiFrLcnIpInterfaceDevice based on Integer32"""
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


_MscIpiFrLcnIpInterfaceDevice_Type.__name__ = "Integer32"
_MscIpiFrLcnIpInterfaceDevice_Object = MibTableColumn
mscIpiFrLcnIpInterfaceDevice = _MscIpiFrLcnIpInterfaceDevice_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11, 1, 1),
    _MscIpiFrLcnIpInterfaceDevice_Type()
)
mscIpiFrLcnIpInterfaceDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnIpInterfaceDevice.setStatus("mandatory")


class _MscIpiFrLcnOpRemoteIpAddress_Type(IpAddress):
    """Custom type mscIpiFrLcnOpRemoteIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpiFrLcnOpRemoteIpAddress_Object = MibTableColumn
mscIpiFrLcnOpRemoteIpAddress = _MscIpiFrLcnOpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11, 1, 2),
    _MscIpiFrLcnOpRemoteIpAddress_Type()
)
mscIpiFrLcnOpRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnOpRemoteIpAddress.setStatus("mandatory")
_MscIpiFrLcnPacketsSent_Type = Counter32
_MscIpiFrLcnPacketsSent_Object = MibTableColumn
mscIpiFrLcnPacketsSent = _MscIpiFrLcnPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11, 1, 3),
    _MscIpiFrLcnPacketsSent_Type()
)
mscIpiFrLcnPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnPacketsSent.setStatus("mandatory")
_MscIpiFrLcnPacketsReceived_Type = Counter32
_MscIpiFrLcnPacketsReceived_Object = MibTableColumn
mscIpiFrLcnPacketsReceived = _MscIpiFrLcnPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11, 1, 4),
    _MscIpiFrLcnPacketsReceived_Type()
)
mscIpiFrLcnPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnPacketsReceived.setStatus("mandatory")
_MscIpiFrLcnDiscardTxPackets_Type = Counter32
_MscIpiFrLcnDiscardTxPackets_Object = MibTableColumn
mscIpiFrLcnDiscardTxPackets = _MscIpiFrLcnDiscardTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11, 1, 5),
    _MscIpiFrLcnDiscardTxPackets_Type()
)
mscIpiFrLcnDiscardTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnDiscardTxPackets.setStatus("mandatory")
_MscIpiFrLcnDiscardRcvPackets_Type = Counter32
_MscIpiFrLcnDiscardRcvPackets_Object = MibTableColumn
mscIpiFrLcnDiscardRcvPackets = _MscIpiFrLcnDiscardRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 11, 1, 6),
    _MscIpiFrLcnDiscardRcvPackets_Type()
)
mscIpiFrLcnDiscardRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrLcnDiscardRcvPackets.setStatus("mandatory")
_MscIpiFrLcnProvTable_Object = MibTable
mscIpiFrLcnProvTable = _MscIpiFrLcnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 12)
)
if mibBuilder.loadTexts:
    mscIpiFrLcnProvTable.setStatus("mandatory")
_MscIpiFrLcnProvEntry_Object = MibTableRow
mscIpiFrLcnProvEntry = _MscIpiFrLcnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 12, 1)
)
mscIpiFrLcnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrLcnProvEntry.setStatus("mandatory")


class _MscIpiFrLcnRemoteIpAddress_Type(IpAddress):
    """Custom type mscIpiFrLcnRemoteIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpiFrLcnRemoteIpAddress_Object = MibTableColumn
mscIpiFrLcnRemoteIpAddress = _MscIpiFrLcnRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 4, 12, 1, 1),
    _MscIpiFrLcnRemoteIpAddress_Type()
)
mscIpiFrLcnRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrLcnRemoteIpAddress.setStatus("mandatory")
_MscIpiFrSr_ObjectIdentity = ObjectIdentity
mscIpiFrSr = _MscIpiFrSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5)
)
_MscIpiFrSrRowStatusTable_Object = MibTable
mscIpiFrSrRowStatusTable = _MscIpiFrSrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrSrRowStatusTable.setStatus("mandatory")
_MscIpiFrSrRowStatusEntry_Object = MibTableRow
mscIpiFrSrRowStatusEntry = _MscIpiFrSrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 1, 1)
)
mscIpiFrSrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrSrIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrSrRowStatusEntry.setStatus("mandatory")
_MscIpiFrSrRowStatus_Type = RowStatus
_MscIpiFrSrRowStatus_Object = MibTableColumn
mscIpiFrSrRowStatus = _MscIpiFrSrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 1, 1, 1),
    _MscIpiFrSrRowStatus_Type()
)
mscIpiFrSrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrSrRowStatus.setStatus("mandatory")
_MscIpiFrSrComponentName_Type = DisplayString
_MscIpiFrSrComponentName_Object = MibTableColumn
mscIpiFrSrComponentName = _MscIpiFrSrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 1, 1, 2),
    _MscIpiFrSrComponentName_Type()
)
mscIpiFrSrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrSrComponentName.setStatus("mandatory")
_MscIpiFrSrStorageType_Type = StorageType
_MscIpiFrSrStorageType_Object = MibTableColumn
mscIpiFrSrStorageType = _MscIpiFrSrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 1, 1, 4),
    _MscIpiFrSrStorageType_Type()
)
mscIpiFrSrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrSrStorageType.setStatus("mandatory")
_MscIpiFrSrIndex_Type = IpAddress
_MscIpiFrSrIndex_Object = MibTableColumn
mscIpiFrSrIndex = _MscIpiFrSrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 1, 1, 10),
    _MscIpiFrSrIndex_Type()
)
mscIpiFrSrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrSrIndex.setStatus("mandatory")
_MscIpiFrSrProvTable_Object = MibTable
mscIpiFrSrProvTable = _MscIpiFrSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrSrProvTable.setStatus("mandatory")
_MscIpiFrSrProvEntry_Object = MibTableRow
mscIpiFrSrProvEntry = _MscIpiFrSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 10, 1)
)
mscIpiFrSrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrSrIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrSrProvEntry.setStatus("mandatory")


class _MscIpiFrSrGatewayIpAddress_Type(IpAddress):
    """Custom type mscIpiFrSrGatewayIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpiFrSrGatewayIpAddress_Object = MibTableColumn
mscIpiFrSrGatewayIpAddress = _MscIpiFrSrGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 10, 1, 1),
    _MscIpiFrSrGatewayIpAddress_Type()
)
mscIpiFrSrGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrSrGatewayIpAddress.setStatus("mandatory")
_MscIpiFrSrBGtyIpaTable_Object = MibTable
mscIpiFrSrBGtyIpaTable = _MscIpiFrSrBGtyIpaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 327)
)
if mibBuilder.loadTexts:
    mscIpiFrSrBGtyIpaTable.setStatus("mandatory")
_MscIpiFrSrBGtyIpaEntry_Object = MibTableRow
mscIpiFrSrBGtyIpaEntry = _MscIpiFrSrBGtyIpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 327, 1)
)
mscIpiFrSrBGtyIpaEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrSrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrSrBGtyIpaIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrSrBGtyIpaEntry.setStatus("mandatory")


class _MscIpiFrSrBGtyIpaIndex_Type(Integer32):
    """Custom type mscIpiFrSrBGtyIpaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_MscIpiFrSrBGtyIpaIndex_Type.__name__ = "Integer32"
_MscIpiFrSrBGtyIpaIndex_Object = MibTableColumn
mscIpiFrSrBGtyIpaIndex = _MscIpiFrSrBGtyIpaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 327, 1, 1),
    _MscIpiFrSrBGtyIpaIndex_Type()
)
mscIpiFrSrBGtyIpaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrSrBGtyIpaIndex.setStatus("mandatory")
_MscIpiFrSrBGtyIpaValue_Type = IpAddress
_MscIpiFrSrBGtyIpaValue_Object = MibTableColumn
mscIpiFrSrBGtyIpaValue = _MscIpiFrSrBGtyIpaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 327, 1, 2),
    _MscIpiFrSrBGtyIpaValue_Type()
)
mscIpiFrSrBGtyIpaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrSrBGtyIpaValue.setStatus("mandatory")
_MscIpiFrSrBGtyIpaRowStatus_Type = RowStatus
_MscIpiFrSrBGtyIpaRowStatus_Object = MibTableColumn
mscIpiFrSrBGtyIpaRowStatus = _MscIpiFrSrBGtyIpaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 5, 327, 1, 3),
    _MscIpiFrSrBGtyIpaRowStatus_Type()
)
mscIpiFrSrBGtyIpaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscIpiFrSrBGtyIpaRowStatus.setStatus("mandatory")
_MscIpiFrR_ObjectIdentity = ObjectIdentity
mscIpiFrR = _MscIpiFrR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6)
)
_MscIpiFrRRowStatusTable_Object = MibTable
mscIpiFrRRowStatusTable = _MscIpiFrRRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 1)
)
if mibBuilder.loadTexts:
    mscIpiFrRRowStatusTable.setStatus("mandatory")
_MscIpiFrRRowStatusEntry_Object = MibTableRow
mscIpiFrRRowStatusEntry = _MscIpiFrRRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 1, 1)
)
mscIpiFrRRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrRIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrRRowStatusEntry.setStatus("mandatory")
_MscIpiFrRRowStatus_Type = RowStatus
_MscIpiFrRRowStatus_Object = MibTableColumn
mscIpiFrRRowStatus = _MscIpiFrRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 1, 1, 1),
    _MscIpiFrRRowStatus_Type()
)
mscIpiFrRRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrRRowStatus.setStatus("mandatory")
_MscIpiFrRComponentName_Type = DisplayString
_MscIpiFrRComponentName_Object = MibTableColumn
mscIpiFrRComponentName = _MscIpiFrRComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 1, 1, 2),
    _MscIpiFrRComponentName_Type()
)
mscIpiFrRComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrRComponentName.setStatus("mandatory")
_MscIpiFrRStorageType_Type = StorageType
_MscIpiFrRStorageType_Object = MibTableColumn
mscIpiFrRStorageType = _MscIpiFrRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 1, 1, 4),
    _MscIpiFrRStorageType_Type()
)
mscIpiFrRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrRStorageType.setStatus("mandatory")
_MscIpiFrRIndex_Type = IpAddress
_MscIpiFrRIndex_Object = MibTableColumn
mscIpiFrRIndex = _MscIpiFrRIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 1, 1, 10),
    _MscIpiFrRIndex_Type()
)
mscIpiFrRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpiFrRIndex.setStatus("mandatory")
_MscIpiFrROperTable_Object = MibTable
mscIpiFrROperTable = _MscIpiFrROperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrROperTable.setStatus("mandatory")
_MscIpiFrROperEntry_Object = MibTableRow
mscIpiFrROperEntry = _MscIpiFrROperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 10, 1)
)
mscIpiFrROperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrRIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrROperEntry.setStatus("mandatory")


class _MscIpiFrRGtyIpAddr_Type(IpAddress):
    """Custom type mscIpiFrRGtyIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpiFrRGtyIpAddr_Object = MibTableColumn
mscIpiFrRGtyIpAddr = _MscIpiFrRGtyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 10, 1, 1),
    _MscIpiFrRGtyIpAddr_Type()
)
mscIpiFrRGtyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrRGtyIpAddr.setStatus("mandatory")


class _MscIpiFrRLcnIf_Type(Unsigned32):
    """Custom type mscIpiFrRLcnIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 39),
    )


_MscIpiFrRLcnIf_Type.__name__ = "Unsigned32"
_MscIpiFrRLcnIf_Object = MibTableColumn
mscIpiFrRLcnIf = _MscIpiFrRLcnIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 10, 1, 3),
    _MscIpiFrRLcnIf_Type()
)
mscIpiFrRLcnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrRLcnIf.setStatus("mandatory")


class _MscIpiFrRType_Type(Integer32):
    """Custom type mscIpiFrRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("network", 3),
          ("subnet", 2))
    )


_MscIpiFrRType_Type.__name__ = "Integer32"
_MscIpiFrRType_Object = MibTableColumn
mscIpiFrRType = _MscIpiFrRType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 6, 10, 1, 4),
    _MscIpiFrRType_Type()
)
mscIpiFrRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrRType.setStatus("mandatory")
_MscIpiFrProvTable_Object = MibTable
mscIpiFrProvTable = _MscIpiFrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 10)
)
if mibBuilder.loadTexts:
    mscIpiFrProvTable.setStatus("mandatory")
_MscIpiFrProvEntry_Object = MibTableRow
mscIpiFrProvEntry = _MscIpiFrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 10, 1)
)
mscIpiFrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiFrMIB", "mscIpiFrIndex"),
)
if mibBuilder.loadTexts:
    mscIpiFrProvEntry.setStatus("mandatory")


class _MscIpiFrIpAddress_Type(IpAddress):
    """Custom type mscIpiFrIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpiFrIpAddress_Object = MibTableColumn
mscIpiFrIpAddress = _MscIpiFrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 10, 1, 1),
    _MscIpiFrIpAddress_Type()
)
mscIpiFrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrIpAddress.setStatus("mandatory")


class _MscIpiFrMaximumNumberOfLcn_Type(Unsigned32):
    """Custom type mscIpiFrMaximumNumberOfLcn based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 24),
    )


_MscIpiFrMaximumNumberOfLcn_Type.__name__ = "Unsigned32"
_MscIpiFrMaximumNumberOfLcn_Object = MibTableColumn
mscIpiFrMaximumNumberOfLcn = _MscIpiFrMaximumNumberOfLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 10, 1, 2),
    _MscIpiFrMaximumNumberOfLcn_Type()
)
mscIpiFrMaximumNumberOfLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpiFrMaximumNumberOfLcn.setStatus("mandatory")


class _MscIpiFrSubnetMask_Type(IpAddress):
    """Custom type mscIpiFrSubnetMask based on IpAddress"""
    defaultHexValue = "ff000000"


_MscIpiFrSubnetMask_Object = MibTableColumn
mscIpiFrSubnetMask = _MscIpiFrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 50, 10, 1, 3),
    _MscIpiFrSubnetMask_Type()
)
mscIpiFrSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpiFrSubnetMask.setStatus("mandatory")
_IpiFrMIB_ObjectIdentity = ObjectIdentity
ipiFrMIB = _IpiFrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35)
)
_IpiFrGroup_ObjectIdentity = ObjectIdentity
ipiFrGroup = _IpiFrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 1)
)
_IpiFrGroupCA_ObjectIdentity = ObjectIdentity
ipiFrGroupCA = _IpiFrGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 1, 1)
)
_IpiFrGroupCA02_ObjectIdentity = ObjectIdentity
ipiFrGroupCA02 = _IpiFrGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 1, 1, 3)
)
_IpiFrGroupCA02A_ObjectIdentity = ObjectIdentity
ipiFrGroupCA02A = _IpiFrGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 1, 1, 3, 2)
)
_IpiFrCapabilities_ObjectIdentity = ObjectIdentity
ipiFrCapabilities = _IpiFrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 3)
)
_IpiFrCapabilitiesCA_ObjectIdentity = ObjectIdentity
ipiFrCapabilitiesCA = _IpiFrCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 3, 1)
)
_IpiFrCapabilitiesCA02_ObjectIdentity = ObjectIdentity
ipiFrCapabilitiesCA02 = _IpiFrCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 3, 1, 3)
)
_IpiFrCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
ipiFrCapabilitiesCA02A = _IpiFrCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 35, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-IpiFrMIB",
    **{"mscIpiFr": mscIpiFr,
       "mscIpiFrRowStatusTable": mscIpiFrRowStatusTable,
       "mscIpiFrRowStatusEntry": mscIpiFrRowStatusEntry,
       "mscIpiFrRowStatus": mscIpiFrRowStatus,
       "mscIpiFrComponentName": mscIpiFrComponentName,
       "mscIpiFrStorageType": mscIpiFrStorageType,
       "mscIpiFrIndex": mscIpiFrIndex,
       "mscIpiFrDna": mscIpiFrDna,
       "mscIpiFrDnaRowStatusTable": mscIpiFrDnaRowStatusTable,
       "mscIpiFrDnaRowStatusEntry": mscIpiFrDnaRowStatusEntry,
       "mscIpiFrDnaRowStatus": mscIpiFrDnaRowStatus,
       "mscIpiFrDnaComponentName": mscIpiFrDnaComponentName,
       "mscIpiFrDnaStorageType": mscIpiFrDnaStorageType,
       "mscIpiFrDnaIndex": mscIpiFrDnaIndex,
       "mscIpiFrDnaCug": mscIpiFrDnaCug,
       "mscIpiFrDnaCugRowStatusTable": mscIpiFrDnaCugRowStatusTable,
       "mscIpiFrDnaCugRowStatusEntry": mscIpiFrDnaCugRowStatusEntry,
       "mscIpiFrDnaCugRowStatus": mscIpiFrDnaCugRowStatus,
       "mscIpiFrDnaCugComponentName": mscIpiFrDnaCugComponentName,
       "mscIpiFrDnaCugStorageType": mscIpiFrDnaCugStorageType,
       "mscIpiFrDnaCugIndex": mscIpiFrDnaCugIndex,
       "mscIpiFrDnaCugCugOptionsTable": mscIpiFrDnaCugCugOptionsTable,
       "mscIpiFrDnaCugCugOptionsEntry": mscIpiFrDnaCugCugOptionsEntry,
       "mscIpiFrDnaCugType": mscIpiFrDnaCugType,
       "mscIpiFrDnaCugDnic": mscIpiFrDnaCugDnic,
       "mscIpiFrDnaCugInterlockCode": mscIpiFrDnaCugInterlockCode,
       "mscIpiFrDnaCugIncCalls": mscIpiFrDnaCugIncCalls,
       "mscIpiFrDnaAddressTable": mscIpiFrDnaAddressTable,
       "mscIpiFrDnaAddressEntry": mscIpiFrDnaAddressEntry,
       "mscIpiFrDnaNumberingPlanIndicator": mscIpiFrDnaNumberingPlanIndicator,
       "mscIpiFrDnaDataNetworkAddress": mscIpiFrDnaDataNetworkAddress,
       "mscIpiFrDnaOutgoingOptionsTable": mscIpiFrDnaOutgoingOptionsTable,
       "mscIpiFrDnaOutgoingOptionsEntry": mscIpiFrDnaOutgoingOptionsEntry,
       "mscIpiFrDnaOutCalls": mscIpiFrDnaOutCalls,
       "mscIpiFrDnaOutDefaultPriority": mscIpiFrDnaOutDefaultPriority,
       "mscIpiFrDnaOutDefaultPathSensitivity": mscIpiFrDnaOutDefaultPathSensitivity,
       "mscIpiFrDnaOutPathSensitivityOverRide": mscIpiFrDnaOutPathSensitivityOverRide,
       "mscIpiFrDnaDefaultTransferPriority": mscIpiFrDnaDefaultTransferPriority,
       "mscIpiFrDnaTransferPriorityOverRide": mscIpiFrDnaTransferPriorityOverRide,
       "mscIpiFrDnaIncomingOptionsTable": mscIpiFrDnaIncomingOptionsTable,
       "mscIpiFrDnaIncomingOptionsEntry": mscIpiFrDnaIncomingOptionsEntry,
       "mscIpiFrDnaIncCalls": mscIpiFrDnaIncCalls,
       "mscIpiFrDnaIncAccess": mscIpiFrDnaIncAccess,
       "mscIpiFrDnaCallOptionsTable": mscIpiFrDnaCallOptionsTable,
       "mscIpiFrDnaCallOptionsEntry": mscIpiFrDnaCallOptionsEntry,
       "mscIpiFrDnaServiceCategory": mscIpiFrDnaServiceCategory,
       "mscIpiFrDnaAccountClass": mscIpiFrDnaAccountClass,
       "mscIpiFrDnaServiceExchange": mscIpiFrDnaServiceExchange,
       "mscIpiFrLcn": mscIpiFrLcn,
       "mscIpiFrLcnRowStatusTable": mscIpiFrLcnRowStatusTable,
       "mscIpiFrLcnRowStatusEntry": mscIpiFrLcnRowStatusEntry,
       "mscIpiFrLcnRowStatus": mscIpiFrLcnRowStatus,
       "mscIpiFrLcnComponentName": mscIpiFrLcnComponentName,
       "mscIpiFrLcnStorageType": mscIpiFrLcnStorageType,
       "mscIpiFrLcnIndex": mscIpiFrLcnIndex,
       "mscIpiFrLcnDc": mscIpiFrLcnDc,
       "mscIpiFrLcnDcRowStatusTable": mscIpiFrLcnDcRowStatusTable,
       "mscIpiFrLcnDcRowStatusEntry": mscIpiFrLcnDcRowStatusEntry,
       "mscIpiFrLcnDcRowStatus": mscIpiFrLcnDcRowStatus,
       "mscIpiFrLcnDcComponentName": mscIpiFrLcnDcComponentName,
       "mscIpiFrLcnDcStorageType": mscIpiFrLcnDcStorageType,
       "mscIpiFrLcnDcIndex": mscIpiFrLcnDcIndex,
       "mscIpiFrLcnDcOptionsTable": mscIpiFrLcnDcOptionsTable,
       "mscIpiFrLcnDcOptionsEntry": mscIpiFrLcnDcOptionsEntry,
       "mscIpiFrLcnDcRemoteNpi": mscIpiFrLcnDcRemoteNpi,
       "mscIpiFrLcnDcRemoteDna": mscIpiFrLcnDcRemoteDna,
       "mscIpiFrLcnDcRemoteDlci": mscIpiFrLcnDcRemoteDlci,
       "mscIpiFrLcnDcType": mscIpiFrLcnDcType,
       "mscIpiFrLcnDcTransferPriority": mscIpiFrLcnDcTransferPriority,
       "mscIpiFrLcnDcDiscardPriority": mscIpiFrLcnDcDiscardPriority,
       "mscIpiFrLcnDcNfaTable": mscIpiFrLcnDcNfaTable,
       "mscIpiFrLcnDcNfaEntry": mscIpiFrLcnDcNfaEntry,
       "mscIpiFrLcnDcNfaIndex": mscIpiFrLcnDcNfaIndex,
       "mscIpiFrLcnDcNfaValue": mscIpiFrLcnDcNfaValue,
       "mscIpiFrLcnDcNfaRowStatus": mscIpiFrLcnDcNfaRowStatus,
       "mscIpiFrLcnVc": mscIpiFrLcnVc,
       "mscIpiFrLcnVcRowStatusTable": mscIpiFrLcnVcRowStatusTable,
       "mscIpiFrLcnVcRowStatusEntry": mscIpiFrLcnVcRowStatusEntry,
       "mscIpiFrLcnVcRowStatus": mscIpiFrLcnVcRowStatus,
       "mscIpiFrLcnVcComponentName": mscIpiFrLcnVcComponentName,
       "mscIpiFrLcnVcStorageType": mscIpiFrLcnVcStorageType,
       "mscIpiFrLcnVcIndex": mscIpiFrLcnVcIndex,
       "mscIpiFrLcnVcCadTable": mscIpiFrLcnVcCadTable,
       "mscIpiFrLcnVcCadEntry": mscIpiFrLcnVcCadEntry,
       "mscIpiFrLcnVcType": mscIpiFrLcnVcType,
       "mscIpiFrLcnVcState": mscIpiFrLcnVcState,
       "mscIpiFrLcnVcPreviousState": mscIpiFrLcnVcPreviousState,
       "mscIpiFrLcnVcDiagnosticCode": mscIpiFrLcnVcDiagnosticCode,
       "mscIpiFrLcnVcPreviousDiagnosticCode": mscIpiFrLcnVcPreviousDiagnosticCode,
       "mscIpiFrLcnVcCalledNpi": mscIpiFrLcnVcCalledNpi,
       "mscIpiFrLcnVcCalledDna": mscIpiFrLcnVcCalledDna,
       "mscIpiFrLcnVcCalledLcn": mscIpiFrLcnVcCalledLcn,
       "mscIpiFrLcnVcCallingNpi": mscIpiFrLcnVcCallingNpi,
       "mscIpiFrLcnVcCallingDna": mscIpiFrLcnVcCallingDna,
       "mscIpiFrLcnVcCallingLcn": mscIpiFrLcnVcCallingLcn,
       "mscIpiFrLcnVcAccountingEnabled": mscIpiFrLcnVcAccountingEnabled,
       "mscIpiFrLcnVcFastSelectCall": mscIpiFrLcnVcFastSelectCall,
       "mscIpiFrLcnVcPathReliability": mscIpiFrLcnVcPathReliability,
       "mscIpiFrLcnVcAccountingEnd": mscIpiFrLcnVcAccountingEnd,
       "mscIpiFrLcnVcPriority": mscIpiFrLcnVcPriority,
       "mscIpiFrLcnVcSegmentSize": mscIpiFrLcnVcSegmentSize,
       "mscIpiFrLcnVcMaxSubnetPktSize": mscIpiFrLcnVcMaxSubnetPktSize,
       "mscIpiFrLcnVcRcosToNetwork": mscIpiFrLcnVcRcosToNetwork,
       "mscIpiFrLcnVcRcosFromNetwork": mscIpiFrLcnVcRcosFromNetwork,
       "mscIpiFrLcnVcEmissionPriorityToNetwork": mscIpiFrLcnVcEmissionPriorityToNetwork,
       "mscIpiFrLcnVcEmissionPriorityFromNetwork": mscIpiFrLcnVcEmissionPriorityFromNetwork,
       "mscIpiFrLcnVcDataPath": mscIpiFrLcnVcDataPath,
       "mscIpiFrLcnVcIntdTable": mscIpiFrLcnVcIntdTable,
       "mscIpiFrLcnVcIntdEntry": mscIpiFrLcnVcIntdEntry,
       "mscIpiFrLcnVcCallReferenceNumber": mscIpiFrLcnVcCallReferenceNumber,
       "mscIpiFrLcnVcElapsedTimeTillNow": mscIpiFrLcnVcElapsedTimeTillNow,
       "mscIpiFrLcnVcSegmentsRx": mscIpiFrLcnVcSegmentsRx,
       "mscIpiFrLcnVcSegmentsSent": mscIpiFrLcnVcSegmentsSent,
       "mscIpiFrLcnVcStartTime": mscIpiFrLcnVcStartTime,
       "mscIpiFrLcnVcCallReferenceNumberDecimal": mscIpiFrLcnVcCallReferenceNumberDecimal,
       "mscIpiFrLcnVcFrdTable": mscIpiFrLcnVcFrdTable,
       "mscIpiFrLcnVcFrdEntry": mscIpiFrLcnVcFrdEntry,
       "mscIpiFrLcnVcFrmCongestedToSubnet": mscIpiFrLcnVcFrmCongestedToSubnet,
       "mscIpiFrLcnVcCannotForwardToSubnet": mscIpiFrLcnVcCannotForwardToSubnet,
       "mscIpiFrLcnVcNotDataXferToSubnet": mscIpiFrLcnVcNotDataXferToSubnet,
       "mscIpiFrLcnVcOutOfRangeFrmFromSubnet": mscIpiFrLcnVcOutOfRangeFrmFromSubnet,
       "mscIpiFrLcnVcCombErrorsFromSubnet": mscIpiFrLcnVcCombErrorsFromSubnet,
       "mscIpiFrLcnVcDuplicatesFromSubnet": mscIpiFrLcnVcDuplicatesFromSubnet,
       "mscIpiFrLcnVcNotDataXferFromSubnet": mscIpiFrLcnVcNotDataXferFromSubnet,
       "mscIpiFrLcnVcFrmLossTimeouts": mscIpiFrLcnVcFrmLossTimeouts,
       "mscIpiFrLcnVcOoSeqByteCntExceeded": mscIpiFrLcnVcOoSeqByteCntExceeded,
       "mscIpiFrLcnVcPeakOoSeqPktCount": mscIpiFrLcnVcPeakOoSeqPktCount,
       "mscIpiFrLcnVcPeakOoSeqFrmForwarded": mscIpiFrLcnVcPeakOoSeqFrmForwarded,
       "mscIpiFrLcnVcSendSequenceNumber": mscIpiFrLcnVcSendSequenceNumber,
       "mscIpiFrLcnVcPktRetryTimeouts": mscIpiFrLcnVcPktRetryTimeouts,
       "mscIpiFrLcnVcPeakRetryQueueSize": mscIpiFrLcnVcPeakRetryQueueSize,
       "mscIpiFrLcnVcSubnetRecoveries": mscIpiFrLcnVcSubnetRecoveries,
       "mscIpiFrLcnVcOoSeqPktCntExceeded": mscIpiFrLcnVcOoSeqPktCntExceeded,
       "mscIpiFrLcnVcPeakOoSeqByteCount": mscIpiFrLcnVcPeakOoSeqByteCount,
       "mscIpiFrLcnVcDmepTable": mscIpiFrLcnVcDmepTable,
       "mscIpiFrLcnVcDmepEntry": mscIpiFrLcnVcDmepEntry,
       "mscIpiFrLcnVcDmepValue": mscIpiFrLcnVcDmepValue,
       "mscIpiFrLcnStateTable": mscIpiFrLcnStateTable,
       "mscIpiFrLcnStateEntry": mscIpiFrLcnStateEntry,
       "mscIpiFrLcnAdminState": mscIpiFrLcnAdminState,
       "mscIpiFrLcnOperationalState": mscIpiFrLcnOperationalState,
       "mscIpiFrLcnUsageState": mscIpiFrLcnUsageState,
       "mscIpiFrLcnAvailabilityStatus": mscIpiFrLcnAvailabilityStatus,
       "mscIpiFrLcnProceduralStatus": mscIpiFrLcnProceduralStatus,
       "mscIpiFrLcnControlStatus": mscIpiFrLcnControlStatus,
       "mscIpiFrLcnAlarmStatus": mscIpiFrLcnAlarmStatus,
       "mscIpiFrLcnStandbyStatus": mscIpiFrLcnStandbyStatus,
       "mscIpiFrLcnUnknownStatus": mscIpiFrLcnUnknownStatus,
       "mscIpiFrLcnOperTable": mscIpiFrLcnOperTable,
       "mscIpiFrLcnOperEntry": mscIpiFrLcnOperEntry,
       "mscIpiFrLcnIpInterfaceDevice": mscIpiFrLcnIpInterfaceDevice,
       "mscIpiFrLcnOpRemoteIpAddress": mscIpiFrLcnOpRemoteIpAddress,
       "mscIpiFrLcnPacketsSent": mscIpiFrLcnPacketsSent,
       "mscIpiFrLcnPacketsReceived": mscIpiFrLcnPacketsReceived,
       "mscIpiFrLcnDiscardTxPackets": mscIpiFrLcnDiscardTxPackets,
       "mscIpiFrLcnDiscardRcvPackets": mscIpiFrLcnDiscardRcvPackets,
       "mscIpiFrLcnProvTable": mscIpiFrLcnProvTable,
       "mscIpiFrLcnProvEntry": mscIpiFrLcnProvEntry,
       "mscIpiFrLcnRemoteIpAddress": mscIpiFrLcnRemoteIpAddress,
       "mscIpiFrSr": mscIpiFrSr,
       "mscIpiFrSrRowStatusTable": mscIpiFrSrRowStatusTable,
       "mscIpiFrSrRowStatusEntry": mscIpiFrSrRowStatusEntry,
       "mscIpiFrSrRowStatus": mscIpiFrSrRowStatus,
       "mscIpiFrSrComponentName": mscIpiFrSrComponentName,
       "mscIpiFrSrStorageType": mscIpiFrSrStorageType,
       "mscIpiFrSrIndex": mscIpiFrSrIndex,
       "mscIpiFrSrProvTable": mscIpiFrSrProvTable,
       "mscIpiFrSrProvEntry": mscIpiFrSrProvEntry,
       "mscIpiFrSrGatewayIpAddress": mscIpiFrSrGatewayIpAddress,
       "mscIpiFrSrBGtyIpaTable": mscIpiFrSrBGtyIpaTable,
       "mscIpiFrSrBGtyIpaEntry": mscIpiFrSrBGtyIpaEntry,
       "mscIpiFrSrBGtyIpaIndex": mscIpiFrSrBGtyIpaIndex,
       "mscIpiFrSrBGtyIpaValue": mscIpiFrSrBGtyIpaValue,
       "mscIpiFrSrBGtyIpaRowStatus": mscIpiFrSrBGtyIpaRowStatus,
       "mscIpiFrR": mscIpiFrR,
       "mscIpiFrRRowStatusTable": mscIpiFrRRowStatusTable,
       "mscIpiFrRRowStatusEntry": mscIpiFrRRowStatusEntry,
       "mscIpiFrRRowStatus": mscIpiFrRRowStatus,
       "mscIpiFrRComponentName": mscIpiFrRComponentName,
       "mscIpiFrRStorageType": mscIpiFrRStorageType,
       "mscIpiFrRIndex": mscIpiFrRIndex,
       "mscIpiFrROperTable": mscIpiFrROperTable,
       "mscIpiFrROperEntry": mscIpiFrROperEntry,
       "mscIpiFrRGtyIpAddr": mscIpiFrRGtyIpAddr,
       "mscIpiFrRLcnIf": mscIpiFrRLcnIf,
       "mscIpiFrRType": mscIpiFrRType,
       "mscIpiFrProvTable": mscIpiFrProvTable,
       "mscIpiFrProvEntry": mscIpiFrProvEntry,
       "mscIpiFrIpAddress": mscIpiFrIpAddress,
       "mscIpiFrMaximumNumberOfLcn": mscIpiFrMaximumNumberOfLcn,
       "mscIpiFrSubnetMask": mscIpiFrSubnetMask,
       "ipiFrMIB": ipiFrMIB,
       "ipiFrGroup": ipiFrGroup,
       "ipiFrGroupCA": ipiFrGroupCA,
       "ipiFrGroupCA02": ipiFrGroupCA02,
       "ipiFrGroupCA02A": ipiFrGroupCA02A,
       "ipiFrCapabilities": ipiFrCapabilities,
       "ipiFrCapabilitiesCA": ipiFrCapabilitiesCA,
       "ipiFrCapabilitiesCA02": ipiFrCapabilitiesCA02,
       "ipiFrCapabilitiesCA02A": ipiFrCapabilitiesCA02A}
)
