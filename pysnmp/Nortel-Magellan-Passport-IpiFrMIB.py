# SNMP MIB module (Nortel-Magellan-Passport-IpiFrMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-IpiFrMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:01 2024
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
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
    "HexString",
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

_IpiFr_ObjectIdentity = ObjectIdentity
ipiFr = _IpiFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50)
)
_IpiFrRowStatusTable_Object = MibTable
ipiFrRowStatusTable = _IpiFrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 1)
)
if mibBuilder.loadTexts:
    ipiFrRowStatusTable.setStatus("mandatory")
_IpiFrRowStatusEntry_Object = MibTableRow
ipiFrRowStatusEntry = _IpiFrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 1, 1)
)
ipiFrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
)
if mibBuilder.loadTexts:
    ipiFrRowStatusEntry.setStatus("mandatory")
_IpiFrRowStatus_Type = RowStatus
_IpiFrRowStatus_Object = MibTableColumn
ipiFrRowStatus = _IpiFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 1, 1, 1),
    _IpiFrRowStatus_Type()
)
ipiFrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrRowStatus.setStatus("mandatory")
_IpiFrComponentName_Type = DisplayString
_IpiFrComponentName_Object = MibTableColumn
ipiFrComponentName = _IpiFrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 1, 1, 2),
    _IpiFrComponentName_Type()
)
ipiFrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrComponentName.setStatus("mandatory")
_IpiFrStorageType_Type = StorageType
_IpiFrStorageType_Object = MibTableColumn
ipiFrStorageType = _IpiFrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 1, 1, 4),
    _IpiFrStorageType_Type()
)
ipiFrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrStorageType.setStatus("mandatory")
_IpiFrIndex_Type = NonReplicated
_IpiFrIndex_Object = MibTableColumn
ipiFrIndex = _IpiFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 1, 1, 10),
    _IpiFrIndex_Type()
)
ipiFrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrIndex.setStatus("mandatory")
_IpiFrDna_ObjectIdentity = ObjectIdentity
ipiFrDna = _IpiFrDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2)
)
_IpiFrDnaRowStatusTable_Object = MibTable
ipiFrDnaRowStatusTable = _IpiFrDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 1)
)
if mibBuilder.loadTexts:
    ipiFrDnaRowStatusTable.setStatus("mandatory")
_IpiFrDnaRowStatusEntry_Object = MibTableRow
ipiFrDnaRowStatusEntry = _IpiFrDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 1, 1)
)
ipiFrDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    ipiFrDnaRowStatusEntry.setStatus("mandatory")
_IpiFrDnaRowStatus_Type = RowStatus
_IpiFrDnaRowStatus_Object = MibTableColumn
ipiFrDnaRowStatus = _IpiFrDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 1, 1, 1),
    _IpiFrDnaRowStatus_Type()
)
ipiFrDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaRowStatus.setStatus("mandatory")
_IpiFrDnaComponentName_Type = DisplayString
_IpiFrDnaComponentName_Object = MibTableColumn
ipiFrDnaComponentName = _IpiFrDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 1, 1, 2),
    _IpiFrDnaComponentName_Type()
)
ipiFrDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaComponentName.setStatus("mandatory")
_IpiFrDnaStorageType_Type = StorageType
_IpiFrDnaStorageType_Object = MibTableColumn
ipiFrDnaStorageType = _IpiFrDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 1, 1, 4),
    _IpiFrDnaStorageType_Type()
)
ipiFrDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaStorageType.setStatus("mandatory")
_IpiFrDnaIndex_Type = NonReplicated
_IpiFrDnaIndex_Object = MibTableColumn
ipiFrDnaIndex = _IpiFrDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 1, 1, 10),
    _IpiFrDnaIndex_Type()
)
ipiFrDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrDnaIndex.setStatus("mandatory")
_IpiFrDnaCug_ObjectIdentity = ObjectIdentity
ipiFrDnaCug = _IpiFrDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2)
)
_IpiFrDnaCugRowStatusTable_Object = MibTable
ipiFrDnaCugRowStatusTable = _IpiFrDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipiFrDnaCugRowStatusTable.setStatus("mandatory")
_IpiFrDnaCugRowStatusEntry_Object = MibTableRow
ipiFrDnaCugRowStatusEntry = _IpiFrDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 1, 1)
)
ipiFrDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    ipiFrDnaCugRowStatusEntry.setStatus("mandatory")
_IpiFrDnaCugRowStatus_Type = RowStatus
_IpiFrDnaCugRowStatus_Object = MibTableColumn
ipiFrDnaCugRowStatus = _IpiFrDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 1, 1, 1),
    _IpiFrDnaCugRowStatus_Type()
)
ipiFrDnaCugRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaCugRowStatus.setStatus("mandatory")
_IpiFrDnaCugComponentName_Type = DisplayString
_IpiFrDnaCugComponentName_Object = MibTableColumn
ipiFrDnaCugComponentName = _IpiFrDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 1, 1, 2),
    _IpiFrDnaCugComponentName_Type()
)
ipiFrDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaCugComponentName.setStatus("mandatory")
_IpiFrDnaCugStorageType_Type = StorageType
_IpiFrDnaCugStorageType_Object = MibTableColumn
ipiFrDnaCugStorageType = _IpiFrDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 1, 1, 4),
    _IpiFrDnaCugStorageType_Type()
)
ipiFrDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaCugStorageType.setStatus("mandatory")


class _IpiFrDnaCugIndex_Type(Integer32):
    """Custom type ipiFrDnaCugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiFrDnaCugIndex_Type.__name__ = "Integer32"
_IpiFrDnaCugIndex_Object = MibTableColumn
ipiFrDnaCugIndex = _IpiFrDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 1, 1, 10),
    _IpiFrDnaCugIndex_Type()
)
ipiFrDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrDnaCugIndex.setStatus("mandatory")
_IpiFrDnaCugCugOptionsTable_Object = MibTable
ipiFrDnaCugCugOptionsTable = _IpiFrDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 10)
)
if mibBuilder.loadTexts:
    ipiFrDnaCugCugOptionsTable.setStatus("mandatory")
_IpiFrDnaCugCugOptionsEntry_Object = MibTableRow
ipiFrDnaCugCugOptionsEntry = _IpiFrDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 10, 1)
)
ipiFrDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaCugIndex"),
)
if mibBuilder.loadTexts:
    ipiFrDnaCugCugOptionsEntry.setStatus("mandatory")


class _IpiFrDnaCugType_Type(Integer32):
    """Custom type ipiFrDnaCugType based on Integer32"""
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


_IpiFrDnaCugType_Type.__name__ = "Integer32"
_IpiFrDnaCugType_Object = MibTableColumn
ipiFrDnaCugType = _IpiFrDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 10, 1, 1),
    _IpiFrDnaCugType_Type()
)
ipiFrDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaCugType.setStatus("mandatory")


class _IpiFrDnaCugDnic_Type(DigitString):
    """Custom type ipiFrDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpiFrDnaCugDnic_Type.__name__ = "DigitString"
_IpiFrDnaCugDnic_Object = MibTableColumn
ipiFrDnaCugDnic = _IpiFrDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 10, 1, 2),
    _IpiFrDnaCugDnic_Type()
)
ipiFrDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaCugDnic.setStatus("mandatory")


class _IpiFrDnaCugInterlockCode_Type(Unsigned32):
    """Custom type ipiFrDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpiFrDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_IpiFrDnaCugInterlockCode_Object = MibTableColumn
ipiFrDnaCugInterlockCode = _IpiFrDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 10, 1, 3),
    _IpiFrDnaCugInterlockCode_Type()
)
ipiFrDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaCugInterlockCode.setStatus("mandatory")


class _IpiFrDnaCugIncCalls_Type(Integer32):
    """Custom type ipiFrDnaCugIncCalls based on Integer32"""
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


_IpiFrDnaCugIncCalls_Type.__name__ = "Integer32"
_IpiFrDnaCugIncCalls_Object = MibTableColumn
ipiFrDnaCugIncCalls = _IpiFrDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 2, 10, 1, 6),
    _IpiFrDnaCugIncCalls_Type()
)
ipiFrDnaCugIncCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaCugIncCalls.setStatus("mandatory")
_IpiFrDnaAddressTable_Object = MibTable
ipiFrDnaAddressTable = _IpiFrDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 10)
)
if mibBuilder.loadTexts:
    ipiFrDnaAddressTable.setStatus("mandatory")
_IpiFrDnaAddressEntry_Object = MibTableRow
ipiFrDnaAddressEntry = _IpiFrDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 10, 1)
)
ipiFrDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    ipiFrDnaAddressEntry.setStatus("mandatory")


class _IpiFrDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type ipiFrDnaNumberingPlanIndicator based on Integer32"""
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


_IpiFrDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_IpiFrDnaNumberingPlanIndicator_Object = MibTableColumn
ipiFrDnaNumberingPlanIndicator = _IpiFrDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 10, 1, 1),
    _IpiFrDnaNumberingPlanIndicator_Type()
)
ipiFrDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaNumberingPlanIndicator.setStatus("mandatory")


class _IpiFrDnaDataNetworkAddress_Type(DigitString):
    """Custom type ipiFrDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpiFrDnaDataNetworkAddress_Type.__name__ = "DigitString"
_IpiFrDnaDataNetworkAddress_Object = MibTableColumn
ipiFrDnaDataNetworkAddress = _IpiFrDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 10, 1, 2),
    _IpiFrDnaDataNetworkAddress_Type()
)
ipiFrDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaDataNetworkAddress.setStatus("mandatory")
_IpiFrDnaOutgoingOptionsTable_Object = MibTable
ipiFrDnaOutgoingOptionsTable = _IpiFrDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11)
)
if mibBuilder.loadTexts:
    ipiFrDnaOutgoingOptionsTable.setStatus("mandatory")
_IpiFrDnaOutgoingOptionsEntry_Object = MibTableRow
ipiFrDnaOutgoingOptionsEntry = _IpiFrDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11, 1)
)
ipiFrDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    ipiFrDnaOutgoingOptionsEntry.setStatus("mandatory")


class _IpiFrDnaOutCalls_Type(Integer32):
    """Custom type ipiFrDnaOutCalls based on Integer32"""
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


_IpiFrDnaOutCalls_Type.__name__ = "Integer32"
_IpiFrDnaOutCalls_Object = MibTableColumn
ipiFrDnaOutCalls = _IpiFrDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11, 1, 1),
    _IpiFrDnaOutCalls_Type()
)
ipiFrDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaOutCalls.setStatus("mandatory")


class _IpiFrDnaOutDefaultPriority_Type(Integer32):
    """Custom type ipiFrDnaOutDefaultPriority based on Integer32"""
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


_IpiFrDnaOutDefaultPriority_Type.__name__ = "Integer32"
_IpiFrDnaOutDefaultPriority_Object = MibTableColumn
ipiFrDnaOutDefaultPriority = _IpiFrDnaOutDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11, 1, 7),
    _IpiFrDnaOutDefaultPriority_Type()
)
ipiFrDnaOutDefaultPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaOutDefaultPriority.setStatus("mandatory")


class _IpiFrDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type ipiFrDnaOutDefaultPathSensitivity based on Integer32"""
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


_IpiFrDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_IpiFrDnaOutDefaultPathSensitivity_Object = MibTableColumn
ipiFrDnaOutDefaultPathSensitivity = _IpiFrDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11, 1, 11),
    _IpiFrDnaOutDefaultPathSensitivity_Type()
)
ipiFrDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _IpiFrDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type ipiFrDnaOutPathSensitivityOverRide based on Integer32"""
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


_IpiFrDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_IpiFrDnaOutPathSensitivityOverRide_Object = MibTableColumn
ipiFrDnaOutPathSensitivityOverRide = _IpiFrDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11, 1, 12),
    _IpiFrDnaOutPathSensitivityOverRide_Type()
)
ipiFrDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _IpiFrDnaDefaultTransferPriority_Type(Integer32):
    """Custom type ipiFrDnaDefaultTransferPriority based on Integer32"""
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


_IpiFrDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_IpiFrDnaDefaultTransferPriority_Object = MibTableColumn
ipiFrDnaDefaultTransferPriority = _IpiFrDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11, 1, 18),
    _IpiFrDnaDefaultTransferPriority_Type()
)
ipiFrDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaDefaultTransferPriority.setStatus("mandatory")


class _IpiFrDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type ipiFrDnaTransferPriorityOverRide based on Integer32"""
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


_IpiFrDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_IpiFrDnaTransferPriorityOverRide_Object = MibTableColumn
ipiFrDnaTransferPriorityOverRide = _IpiFrDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 11, 1, 19),
    _IpiFrDnaTransferPriorityOverRide_Type()
)
ipiFrDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaTransferPriorityOverRide.setStatus("mandatory")
_IpiFrDnaIncomingOptionsTable_Object = MibTable
ipiFrDnaIncomingOptionsTable = _IpiFrDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 12)
)
if mibBuilder.loadTexts:
    ipiFrDnaIncomingOptionsTable.setStatus("mandatory")
_IpiFrDnaIncomingOptionsEntry_Object = MibTableRow
ipiFrDnaIncomingOptionsEntry = _IpiFrDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 12, 1)
)
ipiFrDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    ipiFrDnaIncomingOptionsEntry.setStatus("mandatory")


class _IpiFrDnaIncCalls_Type(Integer32):
    """Custom type ipiFrDnaIncCalls based on Integer32"""
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


_IpiFrDnaIncCalls_Type.__name__ = "Integer32"
_IpiFrDnaIncCalls_Object = MibTableColumn
ipiFrDnaIncCalls = _IpiFrDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 12, 1, 1),
    _IpiFrDnaIncCalls_Type()
)
ipiFrDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaIncCalls.setStatus("mandatory")


class _IpiFrDnaIncAccess_Type(Integer32):
    """Custom type ipiFrDnaIncAccess based on Integer32"""
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


_IpiFrDnaIncAccess_Type.__name__ = "Integer32"
_IpiFrDnaIncAccess_Object = MibTableColumn
ipiFrDnaIncAccess = _IpiFrDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 12, 1, 9),
    _IpiFrDnaIncAccess_Type()
)
ipiFrDnaIncAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaIncAccess.setStatus("mandatory")
_IpiFrDnaCallOptionsTable_Object = MibTable
ipiFrDnaCallOptionsTable = _IpiFrDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 13)
)
if mibBuilder.loadTexts:
    ipiFrDnaCallOptionsTable.setStatus("mandatory")
_IpiFrDnaCallOptionsEntry_Object = MibTableRow
ipiFrDnaCallOptionsEntry = _IpiFrDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 13, 1)
)
ipiFrDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrDnaIndex"),
)
if mibBuilder.loadTexts:
    ipiFrDnaCallOptionsEntry.setStatus("mandatory")


class _IpiFrDnaServiceCategory_Type(Integer32):
    """Custom type ipiFrDnaServiceCategory based on Integer32"""
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


_IpiFrDnaServiceCategory_Type.__name__ = "Integer32"
_IpiFrDnaServiceCategory_Object = MibTableColumn
ipiFrDnaServiceCategory = _IpiFrDnaServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 13, 1, 1),
    _IpiFrDnaServiceCategory_Type()
)
ipiFrDnaServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrDnaServiceCategory.setStatus("mandatory")


class _IpiFrDnaAccountClass_Type(Unsigned32):
    """Custom type ipiFrDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiFrDnaAccountClass_Type.__name__ = "Unsigned32"
_IpiFrDnaAccountClass_Object = MibTableColumn
ipiFrDnaAccountClass = _IpiFrDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 13, 1, 10),
    _IpiFrDnaAccountClass_Type()
)
ipiFrDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaAccountClass.setStatus("mandatory")


class _IpiFrDnaServiceExchange_Type(Unsigned32):
    """Custom type ipiFrDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiFrDnaServiceExchange_Type.__name__ = "Unsigned32"
_IpiFrDnaServiceExchange_Object = MibTableColumn
ipiFrDnaServiceExchange = _IpiFrDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 2, 13, 1, 12),
    _IpiFrDnaServiceExchange_Type()
)
ipiFrDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrDnaServiceExchange.setStatus("mandatory")
_IpiFrLcn_ObjectIdentity = ObjectIdentity
ipiFrLcn = _IpiFrLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4)
)
_IpiFrLcnRowStatusTable_Object = MibTable
ipiFrLcnRowStatusTable = _IpiFrLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 1)
)
if mibBuilder.loadTexts:
    ipiFrLcnRowStatusTable.setStatus("mandatory")
_IpiFrLcnRowStatusEntry_Object = MibTableRow
ipiFrLcnRowStatusEntry = _IpiFrLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 1, 1)
)
ipiFrLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnRowStatusEntry.setStatus("mandatory")
_IpiFrLcnRowStatus_Type = RowStatus
_IpiFrLcnRowStatus_Object = MibTableColumn
ipiFrLcnRowStatus = _IpiFrLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 1, 1, 1),
    _IpiFrLcnRowStatus_Type()
)
ipiFrLcnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnRowStatus.setStatus("mandatory")
_IpiFrLcnComponentName_Type = DisplayString
_IpiFrLcnComponentName_Object = MibTableColumn
ipiFrLcnComponentName = _IpiFrLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 1, 1, 2),
    _IpiFrLcnComponentName_Type()
)
ipiFrLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnComponentName.setStatus("mandatory")
_IpiFrLcnStorageType_Type = StorageType
_IpiFrLcnStorageType_Object = MibTableColumn
ipiFrLcnStorageType = _IpiFrLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 1, 1, 4),
    _IpiFrLcnStorageType_Type()
)
ipiFrLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnStorageType.setStatus("mandatory")


class _IpiFrLcnIndex_Type(Integer32):
    """Custom type ipiFrLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 39),
    )


_IpiFrLcnIndex_Type.__name__ = "Integer32"
_IpiFrLcnIndex_Object = MibTableColumn
ipiFrLcnIndex = _IpiFrLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 1, 1, 10),
    _IpiFrLcnIndex_Type()
)
ipiFrLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrLcnIndex.setStatus("mandatory")
_IpiFrLcnDc_ObjectIdentity = ObjectIdentity
ipiFrLcnDc = _IpiFrLcnDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2)
)
_IpiFrLcnDcRowStatusTable_Object = MibTable
ipiFrLcnDcRowStatusTable = _IpiFrLcnDcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ipiFrLcnDcRowStatusTable.setStatus("mandatory")
_IpiFrLcnDcRowStatusEntry_Object = MibTableRow
ipiFrLcnDcRowStatusEntry = _IpiFrLcnDcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 1, 1)
)
ipiFrLcnDcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnDcIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnDcRowStatusEntry.setStatus("mandatory")
_IpiFrLcnDcRowStatus_Type = RowStatus
_IpiFrLcnDcRowStatus_Object = MibTableColumn
ipiFrLcnDcRowStatus = _IpiFrLcnDcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 1, 1, 1),
    _IpiFrLcnDcRowStatus_Type()
)
ipiFrLcnDcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnDcRowStatus.setStatus("mandatory")
_IpiFrLcnDcComponentName_Type = DisplayString
_IpiFrLcnDcComponentName_Object = MibTableColumn
ipiFrLcnDcComponentName = _IpiFrLcnDcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 1, 1, 2),
    _IpiFrLcnDcComponentName_Type()
)
ipiFrLcnDcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnDcComponentName.setStatus("mandatory")
_IpiFrLcnDcStorageType_Type = StorageType
_IpiFrLcnDcStorageType_Object = MibTableColumn
ipiFrLcnDcStorageType = _IpiFrLcnDcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 1, 1, 4),
    _IpiFrLcnDcStorageType_Type()
)
ipiFrLcnDcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnDcStorageType.setStatus("mandatory")
_IpiFrLcnDcIndex_Type = NonReplicated
_IpiFrLcnDcIndex_Object = MibTableColumn
ipiFrLcnDcIndex = _IpiFrLcnDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 1, 1, 10),
    _IpiFrLcnDcIndex_Type()
)
ipiFrLcnDcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrLcnDcIndex.setStatus("mandatory")
_IpiFrLcnDcOptionsTable_Object = MibTable
ipiFrLcnDcOptionsTable = _IpiFrLcnDcOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10)
)
if mibBuilder.loadTexts:
    ipiFrLcnDcOptionsTable.setStatus("mandatory")
_IpiFrLcnDcOptionsEntry_Object = MibTableRow
ipiFrLcnDcOptionsEntry = _IpiFrLcnDcOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10, 1)
)
ipiFrLcnDcOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnDcIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnDcOptionsEntry.setStatus("mandatory")


class _IpiFrLcnDcRemoteNpi_Type(Integer32):
    """Custom type ipiFrLcnDcRemoteNpi based on Integer32"""
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


_IpiFrLcnDcRemoteNpi_Type.__name__ = "Integer32"
_IpiFrLcnDcRemoteNpi_Object = MibTableColumn
ipiFrLcnDcRemoteNpi = _IpiFrLcnDcRemoteNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10, 1, 3),
    _IpiFrLcnDcRemoteNpi_Type()
)
ipiFrLcnDcRemoteNpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnDcRemoteNpi.setStatus("mandatory")


class _IpiFrLcnDcRemoteDna_Type(DigitString):
    """Custom type ipiFrLcnDcRemoteDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpiFrLcnDcRemoteDna_Type.__name__ = "DigitString"
_IpiFrLcnDcRemoteDna_Object = MibTableColumn
ipiFrLcnDcRemoteDna = _IpiFrLcnDcRemoteDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10, 1, 4),
    _IpiFrLcnDcRemoteDna_Type()
)
ipiFrLcnDcRemoteDna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnDcRemoteDna.setStatus("mandatory")


class _IpiFrLcnDcRemoteDlci_Type(Unsigned32):
    """Custom type ipiFrLcnDcRemoteDlci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_IpiFrLcnDcRemoteDlci_Type.__name__ = "Unsigned32"
_IpiFrLcnDcRemoteDlci_Object = MibTableColumn
ipiFrLcnDcRemoteDlci = _IpiFrLcnDcRemoteDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10, 1, 5),
    _IpiFrLcnDcRemoteDlci_Type()
)
ipiFrLcnDcRemoteDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnDcRemoteDlci.setStatus("mandatory")


class _IpiFrLcnDcType_Type(Integer32):
    """Custom type ipiFrLcnDcType based on Integer32"""
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


_IpiFrLcnDcType_Type.__name__ = "Integer32"
_IpiFrLcnDcType_Object = MibTableColumn
ipiFrLcnDcType = _IpiFrLcnDcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10, 1, 6),
    _IpiFrLcnDcType_Type()
)
ipiFrLcnDcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnDcType.setStatus("mandatory")


class _IpiFrLcnDcTransferPriority_Type(Integer32):
    """Custom type ipiFrLcnDcTransferPriority based on Integer32"""
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


_IpiFrLcnDcTransferPriority_Type.__name__ = "Integer32"
_IpiFrLcnDcTransferPriority_Object = MibTableColumn
ipiFrLcnDcTransferPriority = _IpiFrLcnDcTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10, 1, 9),
    _IpiFrLcnDcTransferPriority_Type()
)
ipiFrLcnDcTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnDcTransferPriority.setStatus("mandatory")


class _IpiFrLcnDcDiscardPriority_Type(Integer32):
    """Custom type ipiFrLcnDcDiscardPriority based on Integer32"""
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


_IpiFrLcnDcDiscardPriority_Type.__name__ = "Integer32"
_IpiFrLcnDcDiscardPriority_Object = MibTableColumn
ipiFrLcnDcDiscardPriority = _IpiFrLcnDcDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 10, 1, 10),
    _IpiFrLcnDcDiscardPriority_Type()
)
ipiFrLcnDcDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnDcDiscardPriority.setStatus("mandatory")
_IpiFrLcnDcNfaTable_Object = MibTable
ipiFrLcnDcNfaTable = _IpiFrLcnDcNfaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 222)
)
if mibBuilder.loadTexts:
    ipiFrLcnDcNfaTable.setStatus("obsolete")
_IpiFrLcnDcNfaEntry_Object = MibTableRow
ipiFrLcnDcNfaEntry = _IpiFrLcnDcNfaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 222, 1)
)
ipiFrLcnDcNfaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnDcIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnDcNfaIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnDcNfaEntry.setStatus("obsolete")


class _IpiFrLcnDcNfaIndex_Type(Integer32):
    """Custom type ipiFrLcnDcNfaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IpiFrLcnDcNfaIndex_Type.__name__ = "Integer32"
_IpiFrLcnDcNfaIndex_Object = MibTableColumn
ipiFrLcnDcNfaIndex = _IpiFrLcnDcNfaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 222, 1, 1),
    _IpiFrLcnDcNfaIndex_Type()
)
ipiFrLcnDcNfaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrLcnDcNfaIndex.setStatus("obsolete")


class _IpiFrLcnDcNfaValue_Type(HexString):
    """Custom type ipiFrLcnDcNfaValue based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_IpiFrLcnDcNfaValue_Type.__name__ = "HexString"
_IpiFrLcnDcNfaValue_Object = MibTableColumn
ipiFrLcnDcNfaValue = _IpiFrLcnDcNfaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 222, 1, 2),
    _IpiFrLcnDcNfaValue_Type()
)
ipiFrLcnDcNfaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnDcNfaValue.setStatus("obsolete")
_IpiFrLcnDcNfaRowStatus_Type = RowStatus
_IpiFrLcnDcNfaRowStatus_Object = MibTableColumn
ipiFrLcnDcNfaRowStatus = _IpiFrLcnDcNfaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 2, 222, 1, 3),
    _IpiFrLcnDcNfaRowStatus_Type()
)
ipiFrLcnDcNfaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ipiFrLcnDcNfaRowStatus.setStatus("obsolete")
_IpiFrLcnVc_ObjectIdentity = ObjectIdentity
ipiFrLcnVc = _IpiFrLcnVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3)
)
_IpiFrLcnVcRowStatusTable_Object = MibTable
ipiFrLcnVcRowStatusTable = _IpiFrLcnVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ipiFrLcnVcRowStatusTable.setStatus("mandatory")
_IpiFrLcnVcRowStatusEntry_Object = MibTableRow
ipiFrLcnVcRowStatusEntry = _IpiFrLcnVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 1, 1)
)
ipiFrLcnVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnVcRowStatusEntry.setStatus("mandatory")
_IpiFrLcnVcRowStatus_Type = RowStatus
_IpiFrLcnVcRowStatus_Object = MibTableColumn
ipiFrLcnVcRowStatus = _IpiFrLcnVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 1, 1, 1),
    _IpiFrLcnVcRowStatus_Type()
)
ipiFrLcnVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcRowStatus.setStatus("mandatory")
_IpiFrLcnVcComponentName_Type = DisplayString
_IpiFrLcnVcComponentName_Object = MibTableColumn
ipiFrLcnVcComponentName = _IpiFrLcnVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 1, 1, 2),
    _IpiFrLcnVcComponentName_Type()
)
ipiFrLcnVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcComponentName.setStatus("mandatory")
_IpiFrLcnVcStorageType_Type = StorageType
_IpiFrLcnVcStorageType_Object = MibTableColumn
ipiFrLcnVcStorageType = _IpiFrLcnVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 1, 1, 4),
    _IpiFrLcnVcStorageType_Type()
)
ipiFrLcnVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcStorageType.setStatus("mandatory")
_IpiFrLcnVcIndex_Type = NonReplicated
_IpiFrLcnVcIndex_Object = MibTableColumn
ipiFrLcnVcIndex = _IpiFrLcnVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 1, 1, 10),
    _IpiFrLcnVcIndex_Type()
)
ipiFrLcnVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrLcnVcIndex.setStatus("mandatory")
_IpiFrLcnVcCadTable_Object = MibTable
ipiFrLcnVcCadTable = _IpiFrLcnVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10)
)
if mibBuilder.loadTexts:
    ipiFrLcnVcCadTable.setStatus("mandatory")
_IpiFrLcnVcCadEntry_Object = MibTableRow
ipiFrLcnVcCadEntry = _IpiFrLcnVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1)
)
ipiFrLcnVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnVcCadEntry.setStatus("mandatory")


class _IpiFrLcnVcType_Type(Integer32):
    """Custom type ipiFrLcnVcType based on Integer32"""
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


_IpiFrLcnVcType_Type.__name__ = "Integer32"
_IpiFrLcnVcType_Object = MibTableColumn
ipiFrLcnVcType = _IpiFrLcnVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 1),
    _IpiFrLcnVcType_Type()
)
ipiFrLcnVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcType.setStatus("mandatory")


class _IpiFrLcnVcState_Type(Integer32):
    """Custom type ipiFrLcnVcState based on Integer32"""
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


_IpiFrLcnVcState_Type.__name__ = "Integer32"
_IpiFrLcnVcState_Object = MibTableColumn
ipiFrLcnVcState = _IpiFrLcnVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 2),
    _IpiFrLcnVcState_Type()
)
ipiFrLcnVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcState.setStatus("mandatory")


class _IpiFrLcnVcPreviousState_Type(Integer32):
    """Custom type ipiFrLcnVcPreviousState based on Integer32"""
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


_IpiFrLcnVcPreviousState_Type.__name__ = "Integer32"
_IpiFrLcnVcPreviousState_Object = MibTableColumn
ipiFrLcnVcPreviousState = _IpiFrLcnVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 3),
    _IpiFrLcnVcPreviousState_Type()
)
ipiFrLcnVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPreviousState.setStatus("mandatory")


class _IpiFrLcnVcDiagnosticCode_Type(Unsigned32):
    """Custom type ipiFrLcnVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiFrLcnVcDiagnosticCode_Type.__name__ = "Unsigned32"
_IpiFrLcnVcDiagnosticCode_Object = MibTableColumn
ipiFrLcnVcDiagnosticCode = _IpiFrLcnVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 4),
    _IpiFrLcnVcDiagnosticCode_Type()
)
ipiFrLcnVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcDiagnosticCode.setStatus("mandatory")


class _IpiFrLcnVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type ipiFrLcnVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiFrLcnVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_IpiFrLcnVcPreviousDiagnosticCode_Object = MibTableColumn
ipiFrLcnVcPreviousDiagnosticCode = _IpiFrLcnVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 5),
    _IpiFrLcnVcPreviousDiagnosticCode_Type()
)
ipiFrLcnVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPreviousDiagnosticCode.setStatus("mandatory")


class _IpiFrLcnVcCalledNpi_Type(Integer32):
    """Custom type ipiFrLcnVcCalledNpi based on Integer32"""
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


_IpiFrLcnVcCalledNpi_Type.__name__ = "Integer32"
_IpiFrLcnVcCalledNpi_Object = MibTableColumn
ipiFrLcnVcCalledNpi = _IpiFrLcnVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 6),
    _IpiFrLcnVcCalledNpi_Type()
)
ipiFrLcnVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCalledNpi.setStatus("mandatory")


class _IpiFrLcnVcCalledDna_Type(DigitString):
    """Custom type ipiFrLcnVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpiFrLcnVcCalledDna_Type.__name__ = "DigitString"
_IpiFrLcnVcCalledDna_Object = MibTableColumn
ipiFrLcnVcCalledDna = _IpiFrLcnVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 7),
    _IpiFrLcnVcCalledDna_Type()
)
ipiFrLcnVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCalledDna.setStatus("mandatory")


class _IpiFrLcnVcCalledLcn_Type(Unsigned32):
    """Custom type ipiFrLcnVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpiFrLcnVcCalledLcn_Type.__name__ = "Unsigned32"
_IpiFrLcnVcCalledLcn_Object = MibTableColumn
ipiFrLcnVcCalledLcn = _IpiFrLcnVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 8),
    _IpiFrLcnVcCalledLcn_Type()
)
ipiFrLcnVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCalledLcn.setStatus("mandatory")


class _IpiFrLcnVcCallingNpi_Type(Integer32):
    """Custom type ipiFrLcnVcCallingNpi based on Integer32"""
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


_IpiFrLcnVcCallingNpi_Type.__name__ = "Integer32"
_IpiFrLcnVcCallingNpi_Object = MibTableColumn
ipiFrLcnVcCallingNpi = _IpiFrLcnVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 9),
    _IpiFrLcnVcCallingNpi_Type()
)
ipiFrLcnVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCallingNpi.setStatus("mandatory")


class _IpiFrLcnVcCallingDna_Type(DigitString):
    """Custom type ipiFrLcnVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpiFrLcnVcCallingDna_Type.__name__ = "DigitString"
_IpiFrLcnVcCallingDna_Object = MibTableColumn
ipiFrLcnVcCallingDna = _IpiFrLcnVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 10),
    _IpiFrLcnVcCallingDna_Type()
)
ipiFrLcnVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCallingDna.setStatus("mandatory")


class _IpiFrLcnVcCallingLcn_Type(Unsigned32):
    """Custom type ipiFrLcnVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpiFrLcnVcCallingLcn_Type.__name__ = "Unsigned32"
_IpiFrLcnVcCallingLcn_Object = MibTableColumn
ipiFrLcnVcCallingLcn = _IpiFrLcnVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 11),
    _IpiFrLcnVcCallingLcn_Type()
)
ipiFrLcnVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCallingLcn.setStatus("mandatory")


class _IpiFrLcnVcAccountingEnabled_Type(Integer32):
    """Custom type ipiFrLcnVcAccountingEnabled based on Integer32"""
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


_IpiFrLcnVcAccountingEnabled_Type.__name__ = "Integer32"
_IpiFrLcnVcAccountingEnabled_Object = MibTableColumn
ipiFrLcnVcAccountingEnabled = _IpiFrLcnVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 12),
    _IpiFrLcnVcAccountingEnabled_Type()
)
ipiFrLcnVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcAccountingEnabled.setStatus("mandatory")


class _IpiFrLcnVcFastSelectCall_Type(Integer32):
    """Custom type ipiFrLcnVcFastSelectCall based on Integer32"""
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


_IpiFrLcnVcFastSelectCall_Type.__name__ = "Integer32"
_IpiFrLcnVcFastSelectCall_Object = MibTableColumn
ipiFrLcnVcFastSelectCall = _IpiFrLcnVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 13),
    _IpiFrLcnVcFastSelectCall_Type()
)
ipiFrLcnVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcFastSelectCall.setStatus("mandatory")


class _IpiFrLcnVcPathReliability_Type(Integer32):
    """Custom type ipiFrLcnVcPathReliability based on Integer32"""
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


_IpiFrLcnVcPathReliability_Type.__name__ = "Integer32"
_IpiFrLcnVcPathReliability_Object = MibTableColumn
ipiFrLcnVcPathReliability = _IpiFrLcnVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 19),
    _IpiFrLcnVcPathReliability_Type()
)
ipiFrLcnVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPathReliability.setStatus("mandatory")


class _IpiFrLcnVcAccountingEnd_Type(Integer32):
    """Custom type ipiFrLcnVcAccountingEnd based on Integer32"""
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


_IpiFrLcnVcAccountingEnd_Type.__name__ = "Integer32"
_IpiFrLcnVcAccountingEnd_Object = MibTableColumn
ipiFrLcnVcAccountingEnd = _IpiFrLcnVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 20),
    _IpiFrLcnVcAccountingEnd_Type()
)
ipiFrLcnVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcAccountingEnd.setStatus("mandatory")


class _IpiFrLcnVcPriority_Type(Integer32):
    """Custom type ipiFrLcnVcPriority based on Integer32"""
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


_IpiFrLcnVcPriority_Type.__name__ = "Integer32"
_IpiFrLcnVcPriority_Object = MibTableColumn
ipiFrLcnVcPriority = _IpiFrLcnVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 21),
    _IpiFrLcnVcPriority_Type()
)
ipiFrLcnVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPriority.setStatus("mandatory")


class _IpiFrLcnVcSegmentSize_Type(Unsigned32):
    """Custom type ipiFrLcnVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_IpiFrLcnVcSegmentSize_Type.__name__ = "Unsigned32"
_IpiFrLcnVcSegmentSize_Object = MibTableColumn
ipiFrLcnVcSegmentSize = _IpiFrLcnVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 22),
    _IpiFrLcnVcSegmentSize_Type()
)
ipiFrLcnVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcSegmentSize.setStatus("mandatory")


class _IpiFrLcnVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type ipiFrLcnVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_IpiFrLcnVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_IpiFrLcnVcMaxSubnetPktSize_Object = MibTableColumn
ipiFrLcnVcMaxSubnetPktSize = _IpiFrLcnVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 27),
    _IpiFrLcnVcMaxSubnetPktSize_Type()
)
ipiFrLcnVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcMaxSubnetPktSize.setStatus("mandatory")


class _IpiFrLcnVcRcosToNetwork_Type(Integer32):
    """Custom type ipiFrLcnVcRcosToNetwork based on Integer32"""
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


_IpiFrLcnVcRcosToNetwork_Type.__name__ = "Integer32"
_IpiFrLcnVcRcosToNetwork_Object = MibTableColumn
ipiFrLcnVcRcosToNetwork = _IpiFrLcnVcRcosToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 28),
    _IpiFrLcnVcRcosToNetwork_Type()
)
ipiFrLcnVcRcosToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcRcosToNetwork.setStatus("mandatory")


class _IpiFrLcnVcRcosFromNetwork_Type(Integer32):
    """Custom type ipiFrLcnVcRcosFromNetwork based on Integer32"""
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


_IpiFrLcnVcRcosFromNetwork_Type.__name__ = "Integer32"
_IpiFrLcnVcRcosFromNetwork_Object = MibTableColumn
ipiFrLcnVcRcosFromNetwork = _IpiFrLcnVcRcosFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 29),
    _IpiFrLcnVcRcosFromNetwork_Type()
)
ipiFrLcnVcRcosFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcRcosFromNetwork.setStatus("mandatory")


class _IpiFrLcnVcEmissionPriorityToNetwork_Type(Integer32):
    """Custom type ipiFrLcnVcEmissionPriorityToNetwork based on Integer32"""
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


_IpiFrLcnVcEmissionPriorityToNetwork_Type.__name__ = "Integer32"
_IpiFrLcnVcEmissionPriorityToNetwork_Object = MibTableColumn
ipiFrLcnVcEmissionPriorityToNetwork = _IpiFrLcnVcEmissionPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 30),
    _IpiFrLcnVcEmissionPriorityToNetwork_Type()
)
ipiFrLcnVcEmissionPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcEmissionPriorityToNetwork.setStatus("mandatory")


class _IpiFrLcnVcEmissionPriorityFromNetwork_Type(Integer32):
    """Custom type ipiFrLcnVcEmissionPriorityFromNetwork based on Integer32"""
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


_IpiFrLcnVcEmissionPriorityFromNetwork_Type.__name__ = "Integer32"
_IpiFrLcnVcEmissionPriorityFromNetwork_Object = MibTableColumn
ipiFrLcnVcEmissionPriorityFromNetwork = _IpiFrLcnVcEmissionPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 31),
    _IpiFrLcnVcEmissionPriorityFromNetwork_Type()
)
ipiFrLcnVcEmissionPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcEmissionPriorityFromNetwork.setStatus("mandatory")


class _IpiFrLcnVcDataPath_Type(AsciiString):
    """Custom type ipiFrLcnVcDataPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpiFrLcnVcDataPath_Type.__name__ = "AsciiString"
_IpiFrLcnVcDataPath_Object = MibTableColumn
ipiFrLcnVcDataPath = _IpiFrLcnVcDataPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 10, 1, 32),
    _IpiFrLcnVcDataPath_Type()
)
ipiFrLcnVcDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcDataPath.setStatus("mandatory")
_IpiFrLcnVcIntdTable_Object = MibTable
ipiFrLcnVcIntdTable = _IpiFrLcnVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 11)
)
if mibBuilder.loadTexts:
    ipiFrLcnVcIntdTable.setStatus("mandatory")
_IpiFrLcnVcIntdEntry_Object = MibTableRow
ipiFrLcnVcIntdEntry = _IpiFrLcnVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 11, 1)
)
ipiFrLcnVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnVcIntdEntry.setStatus("mandatory")


class _IpiFrLcnVcCallReferenceNumber_Type(Hex):
    """Custom type ipiFrLcnVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpiFrLcnVcCallReferenceNumber_Type.__name__ = "Hex"
_IpiFrLcnVcCallReferenceNumber_Object = MibTableColumn
ipiFrLcnVcCallReferenceNumber = _IpiFrLcnVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 11, 1, 1),
    _IpiFrLcnVcCallReferenceNumber_Type()
)
ipiFrLcnVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCallReferenceNumber.setStatus("mandatory")


class _IpiFrLcnVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type ipiFrLcnVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpiFrLcnVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_IpiFrLcnVcElapsedTimeTillNow_Object = MibTableColumn
ipiFrLcnVcElapsedTimeTillNow = _IpiFrLcnVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 11, 1, 2),
    _IpiFrLcnVcElapsedTimeTillNow_Type()
)
ipiFrLcnVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcElapsedTimeTillNow.setStatus("mandatory")


class _IpiFrLcnVcSegmentsRx_Type(Unsigned32):
    """Custom type ipiFrLcnVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpiFrLcnVcSegmentsRx_Type.__name__ = "Unsigned32"
_IpiFrLcnVcSegmentsRx_Object = MibTableColumn
ipiFrLcnVcSegmentsRx = _IpiFrLcnVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 11, 1, 3),
    _IpiFrLcnVcSegmentsRx_Type()
)
ipiFrLcnVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcSegmentsRx.setStatus("mandatory")


class _IpiFrLcnVcSegmentsSent_Type(Unsigned32):
    """Custom type ipiFrLcnVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpiFrLcnVcSegmentsSent_Type.__name__ = "Unsigned32"
_IpiFrLcnVcSegmentsSent_Object = MibTableColumn
ipiFrLcnVcSegmentsSent = _IpiFrLcnVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 11, 1, 4),
    _IpiFrLcnVcSegmentsSent_Type()
)
ipiFrLcnVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcSegmentsSent.setStatus("mandatory")


class _IpiFrLcnVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type ipiFrLcnVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_IpiFrLcnVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_IpiFrLcnVcStartTime_Object = MibTableColumn
ipiFrLcnVcStartTime = _IpiFrLcnVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 11, 1, 5),
    _IpiFrLcnVcStartTime_Type()
)
ipiFrLcnVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcStartTime.setStatus("mandatory")
_IpiFrLcnVcFrdTable_Object = MibTable
ipiFrLcnVcFrdTable = _IpiFrLcnVcFrdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12)
)
if mibBuilder.loadTexts:
    ipiFrLcnVcFrdTable.setStatus("mandatory")
_IpiFrLcnVcFrdEntry_Object = MibTableRow
ipiFrLcnVcFrdEntry = _IpiFrLcnVcFrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1)
)
ipiFrLcnVcFrdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnVcFrdEntry.setStatus("mandatory")


class _IpiFrLcnVcFrmCongestedToSubnet_Type(Unsigned32):
    """Custom type ipiFrLcnVcFrmCongestedToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcFrmCongestedToSubnet_Type.__name__ = "Unsigned32"
_IpiFrLcnVcFrmCongestedToSubnet_Object = MibTableColumn
ipiFrLcnVcFrmCongestedToSubnet = _IpiFrLcnVcFrmCongestedToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 2),
    _IpiFrLcnVcFrmCongestedToSubnet_Type()
)
ipiFrLcnVcFrmCongestedToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcFrmCongestedToSubnet.setStatus("mandatory")


class _IpiFrLcnVcCannotForwardToSubnet_Type(Unsigned32):
    """Custom type ipiFrLcnVcCannotForwardToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcCannotForwardToSubnet_Type.__name__ = "Unsigned32"
_IpiFrLcnVcCannotForwardToSubnet_Object = MibTableColumn
ipiFrLcnVcCannotForwardToSubnet = _IpiFrLcnVcCannotForwardToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 3),
    _IpiFrLcnVcCannotForwardToSubnet_Type()
)
ipiFrLcnVcCannotForwardToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCannotForwardToSubnet.setStatus("mandatory")


class _IpiFrLcnVcNotDataXferToSubnet_Type(Unsigned32):
    """Custom type ipiFrLcnVcNotDataXferToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcNotDataXferToSubnet_Type.__name__ = "Unsigned32"
_IpiFrLcnVcNotDataXferToSubnet_Object = MibTableColumn
ipiFrLcnVcNotDataXferToSubnet = _IpiFrLcnVcNotDataXferToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 4),
    _IpiFrLcnVcNotDataXferToSubnet_Type()
)
ipiFrLcnVcNotDataXferToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcNotDataXferToSubnet.setStatus("mandatory")


class _IpiFrLcnVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type ipiFrLcnVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_IpiFrLcnVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
ipiFrLcnVcOutOfRangeFrmFromSubnet = _IpiFrLcnVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 5),
    _IpiFrLcnVcOutOfRangeFrmFromSubnet_Type()
)
ipiFrLcnVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _IpiFrLcnVcCombErrorsFromSubnet_Type(Unsigned32):
    """Custom type ipiFrLcnVcCombErrorsFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcCombErrorsFromSubnet_Type.__name__ = "Unsigned32"
_IpiFrLcnVcCombErrorsFromSubnet_Object = MibTableColumn
ipiFrLcnVcCombErrorsFromSubnet = _IpiFrLcnVcCombErrorsFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 6),
    _IpiFrLcnVcCombErrorsFromSubnet_Type()
)
ipiFrLcnVcCombErrorsFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcCombErrorsFromSubnet.setStatus("mandatory")


class _IpiFrLcnVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type ipiFrLcnVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_IpiFrLcnVcDuplicatesFromSubnet_Object = MibTableColumn
ipiFrLcnVcDuplicatesFromSubnet = _IpiFrLcnVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 7),
    _IpiFrLcnVcDuplicatesFromSubnet_Type()
)
ipiFrLcnVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcDuplicatesFromSubnet.setStatus("mandatory")


class _IpiFrLcnVcNotDataXferFromSubnet_Type(Unsigned32):
    """Custom type ipiFrLcnVcNotDataXferFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcNotDataXferFromSubnet_Type.__name__ = "Unsigned32"
_IpiFrLcnVcNotDataXferFromSubnet_Object = MibTableColumn
ipiFrLcnVcNotDataXferFromSubnet = _IpiFrLcnVcNotDataXferFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 8),
    _IpiFrLcnVcNotDataXferFromSubnet_Type()
)
ipiFrLcnVcNotDataXferFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcNotDataXferFromSubnet.setStatus("mandatory")


class _IpiFrLcnVcFrmLossTimeouts_Type(Unsigned32):
    """Custom type ipiFrLcnVcFrmLossTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcFrmLossTimeouts_Type.__name__ = "Unsigned32"
_IpiFrLcnVcFrmLossTimeouts_Object = MibTableColumn
ipiFrLcnVcFrmLossTimeouts = _IpiFrLcnVcFrmLossTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 9),
    _IpiFrLcnVcFrmLossTimeouts_Type()
)
ipiFrLcnVcFrmLossTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcFrmLossTimeouts.setStatus("mandatory")


class _IpiFrLcnVcOoSeqByteCntExceeded_Type(Unsigned32):
    """Custom type ipiFrLcnVcOoSeqByteCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcOoSeqByteCntExceeded_Type.__name__ = "Unsigned32"
_IpiFrLcnVcOoSeqByteCntExceeded_Object = MibTableColumn
ipiFrLcnVcOoSeqByteCntExceeded = _IpiFrLcnVcOoSeqByteCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 10),
    _IpiFrLcnVcOoSeqByteCntExceeded_Type()
)
ipiFrLcnVcOoSeqByteCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcOoSeqByteCntExceeded.setStatus("mandatory")


class _IpiFrLcnVcPeakOoSeqPktCount_Type(Unsigned32):
    """Custom type ipiFrLcnVcPeakOoSeqPktCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcPeakOoSeqPktCount_Type.__name__ = "Unsigned32"
_IpiFrLcnVcPeakOoSeqPktCount_Object = MibTableColumn
ipiFrLcnVcPeakOoSeqPktCount = _IpiFrLcnVcPeakOoSeqPktCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 11),
    _IpiFrLcnVcPeakOoSeqPktCount_Type()
)
ipiFrLcnVcPeakOoSeqPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPeakOoSeqPktCount.setStatus("mandatory")


class _IpiFrLcnVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type ipiFrLcnVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_IpiFrLcnVcPeakOoSeqFrmForwarded_Object = MibTableColumn
ipiFrLcnVcPeakOoSeqFrmForwarded = _IpiFrLcnVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 12),
    _IpiFrLcnVcPeakOoSeqFrmForwarded_Type()
)
ipiFrLcnVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _IpiFrLcnVcSendSequenceNumber_Type(Unsigned32):
    """Custom type ipiFrLcnVcSendSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcSendSequenceNumber_Type.__name__ = "Unsigned32"
_IpiFrLcnVcSendSequenceNumber_Object = MibTableColumn
ipiFrLcnVcSendSequenceNumber = _IpiFrLcnVcSendSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 13),
    _IpiFrLcnVcSendSequenceNumber_Type()
)
ipiFrLcnVcSendSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcSendSequenceNumber.setStatus("mandatory")


class _IpiFrLcnVcPktRetryTimeouts_Type(Unsigned32):
    """Custom type ipiFrLcnVcPktRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcPktRetryTimeouts_Type.__name__ = "Unsigned32"
_IpiFrLcnVcPktRetryTimeouts_Object = MibTableColumn
ipiFrLcnVcPktRetryTimeouts = _IpiFrLcnVcPktRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 15),
    _IpiFrLcnVcPktRetryTimeouts_Type()
)
ipiFrLcnVcPktRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPktRetryTimeouts.setStatus("mandatory")


class _IpiFrLcnVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type ipiFrLcnVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_IpiFrLcnVcPeakRetryQueueSize_Object = MibTableColumn
ipiFrLcnVcPeakRetryQueueSize = _IpiFrLcnVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 16),
    _IpiFrLcnVcPeakRetryQueueSize_Type()
)
ipiFrLcnVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPeakRetryQueueSize.setStatus("mandatory")


class _IpiFrLcnVcSubnetRecoveries_Type(Unsigned32):
    """Custom type ipiFrLcnVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpiFrLcnVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_IpiFrLcnVcSubnetRecoveries_Object = MibTableColumn
ipiFrLcnVcSubnetRecoveries = _IpiFrLcnVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 17),
    _IpiFrLcnVcSubnetRecoveries_Type()
)
ipiFrLcnVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcSubnetRecoveries.setStatus("mandatory")


class _IpiFrLcnVcOoSeqPktCntExceeded_Type(Unsigned32):
    """Custom type ipiFrLcnVcOoSeqPktCntExceeded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiFrLcnVcOoSeqPktCntExceeded_Type.__name__ = "Unsigned32"
_IpiFrLcnVcOoSeqPktCntExceeded_Object = MibTableColumn
ipiFrLcnVcOoSeqPktCntExceeded = _IpiFrLcnVcOoSeqPktCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 19),
    _IpiFrLcnVcOoSeqPktCntExceeded_Type()
)
ipiFrLcnVcOoSeqPktCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcOoSeqPktCntExceeded.setStatus("mandatory")


class _IpiFrLcnVcPeakOoSeqByteCount_Type(Unsigned32):
    """Custom type ipiFrLcnVcPeakOoSeqByteCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_IpiFrLcnVcPeakOoSeqByteCount_Type.__name__ = "Unsigned32"
_IpiFrLcnVcPeakOoSeqByteCount_Object = MibTableColumn
ipiFrLcnVcPeakOoSeqByteCount = _IpiFrLcnVcPeakOoSeqByteCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 12, 1, 20),
    _IpiFrLcnVcPeakOoSeqByteCount_Type()
)
ipiFrLcnVcPeakOoSeqByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcPeakOoSeqByteCount.setStatus("mandatory")
_IpiFrLcnVcDmepTable_Object = MibTable
ipiFrLcnVcDmepTable = _IpiFrLcnVcDmepTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 417)
)
if mibBuilder.loadTexts:
    ipiFrLcnVcDmepTable.setStatus("mandatory")
_IpiFrLcnVcDmepEntry_Object = MibTableRow
ipiFrLcnVcDmepEntry = _IpiFrLcnVcDmepEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 417, 1)
)
ipiFrLcnVcDmepEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnVcIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnVcDmepValue"),
)
if mibBuilder.loadTexts:
    ipiFrLcnVcDmepEntry.setStatus("mandatory")
_IpiFrLcnVcDmepValue_Type = RowPointer
_IpiFrLcnVcDmepValue_Object = MibTableColumn
ipiFrLcnVcDmepValue = _IpiFrLcnVcDmepValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 3, 417, 1, 1),
    _IpiFrLcnVcDmepValue_Type()
)
ipiFrLcnVcDmepValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnVcDmepValue.setStatus("mandatory")
_IpiFrLcnStateTable_Object = MibTable
ipiFrLcnStateTable = _IpiFrLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10)
)
if mibBuilder.loadTexts:
    ipiFrLcnStateTable.setStatus("mandatory")
_IpiFrLcnStateEntry_Object = MibTableRow
ipiFrLcnStateEntry = _IpiFrLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1)
)
ipiFrLcnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnStateEntry.setStatus("mandatory")


class _IpiFrLcnAdminState_Type(Integer32):
    """Custom type ipiFrLcnAdminState based on Integer32"""
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


_IpiFrLcnAdminState_Type.__name__ = "Integer32"
_IpiFrLcnAdminState_Object = MibTableColumn
ipiFrLcnAdminState = _IpiFrLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 1),
    _IpiFrLcnAdminState_Type()
)
ipiFrLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnAdminState.setStatus("mandatory")


class _IpiFrLcnOperationalState_Type(Integer32):
    """Custom type ipiFrLcnOperationalState based on Integer32"""
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


_IpiFrLcnOperationalState_Type.__name__ = "Integer32"
_IpiFrLcnOperationalState_Object = MibTableColumn
ipiFrLcnOperationalState = _IpiFrLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 2),
    _IpiFrLcnOperationalState_Type()
)
ipiFrLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnOperationalState.setStatus("mandatory")


class _IpiFrLcnUsageState_Type(Integer32):
    """Custom type ipiFrLcnUsageState based on Integer32"""
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


_IpiFrLcnUsageState_Type.__name__ = "Integer32"
_IpiFrLcnUsageState_Object = MibTableColumn
ipiFrLcnUsageState = _IpiFrLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 3),
    _IpiFrLcnUsageState_Type()
)
ipiFrLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnUsageState.setStatus("mandatory")


class _IpiFrLcnAvailabilityStatus_Type(OctetString):
    """Custom type ipiFrLcnAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpiFrLcnAvailabilityStatus_Type.__name__ = "OctetString"
_IpiFrLcnAvailabilityStatus_Object = MibTableColumn
ipiFrLcnAvailabilityStatus = _IpiFrLcnAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 4),
    _IpiFrLcnAvailabilityStatus_Type()
)
ipiFrLcnAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnAvailabilityStatus.setStatus("mandatory")


class _IpiFrLcnProceduralStatus_Type(OctetString):
    """Custom type ipiFrLcnProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IpiFrLcnProceduralStatus_Type.__name__ = "OctetString"
_IpiFrLcnProceduralStatus_Object = MibTableColumn
ipiFrLcnProceduralStatus = _IpiFrLcnProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 5),
    _IpiFrLcnProceduralStatus_Type()
)
ipiFrLcnProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnProceduralStatus.setStatus("mandatory")


class _IpiFrLcnControlStatus_Type(OctetString):
    """Custom type ipiFrLcnControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IpiFrLcnControlStatus_Type.__name__ = "OctetString"
_IpiFrLcnControlStatus_Object = MibTableColumn
ipiFrLcnControlStatus = _IpiFrLcnControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 6),
    _IpiFrLcnControlStatus_Type()
)
ipiFrLcnControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnControlStatus.setStatus("mandatory")


class _IpiFrLcnAlarmStatus_Type(OctetString):
    """Custom type ipiFrLcnAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IpiFrLcnAlarmStatus_Type.__name__ = "OctetString"
_IpiFrLcnAlarmStatus_Object = MibTableColumn
ipiFrLcnAlarmStatus = _IpiFrLcnAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 7),
    _IpiFrLcnAlarmStatus_Type()
)
ipiFrLcnAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnAlarmStatus.setStatus("mandatory")


class _IpiFrLcnStandbyStatus_Type(Integer32):
    """Custom type ipiFrLcnStandbyStatus based on Integer32"""
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


_IpiFrLcnStandbyStatus_Type.__name__ = "Integer32"
_IpiFrLcnStandbyStatus_Object = MibTableColumn
ipiFrLcnStandbyStatus = _IpiFrLcnStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 8),
    _IpiFrLcnStandbyStatus_Type()
)
ipiFrLcnStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnStandbyStatus.setStatus("mandatory")


class _IpiFrLcnUnknownStatus_Type(Integer32):
    """Custom type ipiFrLcnUnknownStatus based on Integer32"""
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


_IpiFrLcnUnknownStatus_Type.__name__ = "Integer32"
_IpiFrLcnUnknownStatus_Object = MibTableColumn
ipiFrLcnUnknownStatus = _IpiFrLcnUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 10, 1, 9),
    _IpiFrLcnUnknownStatus_Type()
)
ipiFrLcnUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnUnknownStatus.setStatus("mandatory")
_IpiFrLcnOperTable_Object = MibTable
ipiFrLcnOperTable = _IpiFrLcnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11)
)
if mibBuilder.loadTexts:
    ipiFrLcnOperTable.setStatus("mandatory")
_IpiFrLcnOperEntry_Object = MibTableRow
ipiFrLcnOperEntry = _IpiFrLcnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11, 1)
)
ipiFrLcnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnOperEntry.setStatus("mandatory")


class _IpiFrLcnIpInterfaceDevice_Type(Integer32):
    """Custom type ipiFrLcnIpInterfaceDevice based on Integer32"""
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


_IpiFrLcnIpInterfaceDevice_Type.__name__ = "Integer32"
_IpiFrLcnIpInterfaceDevice_Object = MibTableColumn
ipiFrLcnIpInterfaceDevice = _IpiFrLcnIpInterfaceDevice_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11, 1, 1),
    _IpiFrLcnIpInterfaceDevice_Type()
)
ipiFrLcnIpInterfaceDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnIpInterfaceDevice.setStatus("mandatory")


class _IpiFrLcnOpRemoteIpAddress_Type(IpAddress):
    """Custom type ipiFrLcnOpRemoteIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpiFrLcnOpRemoteIpAddress_Object = MibTableColumn
ipiFrLcnOpRemoteIpAddress = _IpiFrLcnOpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11, 1, 2),
    _IpiFrLcnOpRemoteIpAddress_Type()
)
ipiFrLcnOpRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnOpRemoteIpAddress.setStatus("mandatory")
_IpiFrLcnPacketsSent_Type = Counter32
_IpiFrLcnPacketsSent_Object = MibTableColumn
ipiFrLcnPacketsSent = _IpiFrLcnPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11, 1, 3),
    _IpiFrLcnPacketsSent_Type()
)
ipiFrLcnPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnPacketsSent.setStatus("mandatory")
_IpiFrLcnPacketsReceived_Type = Counter32
_IpiFrLcnPacketsReceived_Object = MibTableColumn
ipiFrLcnPacketsReceived = _IpiFrLcnPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11, 1, 4),
    _IpiFrLcnPacketsReceived_Type()
)
ipiFrLcnPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnPacketsReceived.setStatus("mandatory")
_IpiFrLcnDiscardTxPackets_Type = Counter32
_IpiFrLcnDiscardTxPackets_Object = MibTableColumn
ipiFrLcnDiscardTxPackets = _IpiFrLcnDiscardTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11, 1, 5),
    _IpiFrLcnDiscardTxPackets_Type()
)
ipiFrLcnDiscardTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnDiscardTxPackets.setStatus("mandatory")
_IpiFrLcnDiscardRcvPackets_Type = Counter32
_IpiFrLcnDiscardRcvPackets_Object = MibTableColumn
ipiFrLcnDiscardRcvPackets = _IpiFrLcnDiscardRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 11, 1, 6),
    _IpiFrLcnDiscardRcvPackets_Type()
)
ipiFrLcnDiscardRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrLcnDiscardRcvPackets.setStatus("mandatory")
_IpiFrLcnProvTable_Object = MibTable
ipiFrLcnProvTable = _IpiFrLcnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 12)
)
if mibBuilder.loadTexts:
    ipiFrLcnProvTable.setStatus("mandatory")
_IpiFrLcnProvEntry_Object = MibTableRow
ipiFrLcnProvEntry = _IpiFrLcnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 12, 1)
)
ipiFrLcnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrLcnIndex"),
)
if mibBuilder.loadTexts:
    ipiFrLcnProvEntry.setStatus("mandatory")


class _IpiFrLcnRemoteIpAddress_Type(IpAddress):
    """Custom type ipiFrLcnRemoteIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpiFrLcnRemoteIpAddress_Object = MibTableColumn
ipiFrLcnRemoteIpAddress = _IpiFrLcnRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 4, 12, 1, 1),
    _IpiFrLcnRemoteIpAddress_Type()
)
ipiFrLcnRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrLcnRemoteIpAddress.setStatus("mandatory")
_IpiFrSr_ObjectIdentity = ObjectIdentity
ipiFrSr = _IpiFrSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5)
)
_IpiFrSrRowStatusTable_Object = MibTable
ipiFrSrRowStatusTable = _IpiFrSrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 1)
)
if mibBuilder.loadTexts:
    ipiFrSrRowStatusTable.setStatus("mandatory")
_IpiFrSrRowStatusEntry_Object = MibTableRow
ipiFrSrRowStatusEntry = _IpiFrSrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 1, 1)
)
ipiFrSrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrSrIndex"),
)
if mibBuilder.loadTexts:
    ipiFrSrRowStatusEntry.setStatus("mandatory")
_IpiFrSrRowStatus_Type = RowStatus
_IpiFrSrRowStatus_Object = MibTableColumn
ipiFrSrRowStatus = _IpiFrSrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 1, 1, 1),
    _IpiFrSrRowStatus_Type()
)
ipiFrSrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrSrRowStatus.setStatus("mandatory")
_IpiFrSrComponentName_Type = DisplayString
_IpiFrSrComponentName_Object = MibTableColumn
ipiFrSrComponentName = _IpiFrSrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 1, 1, 2),
    _IpiFrSrComponentName_Type()
)
ipiFrSrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrSrComponentName.setStatus("mandatory")
_IpiFrSrStorageType_Type = StorageType
_IpiFrSrStorageType_Object = MibTableColumn
ipiFrSrStorageType = _IpiFrSrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 1, 1, 4),
    _IpiFrSrStorageType_Type()
)
ipiFrSrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrSrStorageType.setStatus("mandatory")
_IpiFrSrIndex_Type = IpAddress
_IpiFrSrIndex_Object = MibTableColumn
ipiFrSrIndex = _IpiFrSrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 1, 1, 10),
    _IpiFrSrIndex_Type()
)
ipiFrSrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrSrIndex.setStatus("mandatory")
_IpiFrSrProvTable_Object = MibTable
ipiFrSrProvTable = _IpiFrSrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 10)
)
if mibBuilder.loadTexts:
    ipiFrSrProvTable.setStatus("mandatory")
_IpiFrSrProvEntry_Object = MibTableRow
ipiFrSrProvEntry = _IpiFrSrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 10, 1)
)
ipiFrSrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrSrIndex"),
)
if mibBuilder.loadTexts:
    ipiFrSrProvEntry.setStatus("mandatory")


class _IpiFrSrGatewayIpAddress_Type(IpAddress):
    """Custom type ipiFrSrGatewayIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpiFrSrGatewayIpAddress_Object = MibTableColumn
ipiFrSrGatewayIpAddress = _IpiFrSrGatewayIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 10, 1, 1),
    _IpiFrSrGatewayIpAddress_Type()
)
ipiFrSrGatewayIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrSrGatewayIpAddress.setStatus("mandatory")
_IpiFrSrBGtyIpaTable_Object = MibTable
ipiFrSrBGtyIpaTable = _IpiFrSrBGtyIpaTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 327)
)
if mibBuilder.loadTexts:
    ipiFrSrBGtyIpaTable.setStatus("mandatory")
_IpiFrSrBGtyIpaEntry_Object = MibTableRow
ipiFrSrBGtyIpaEntry = _IpiFrSrBGtyIpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 327, 1)
)
ipiFrSrBGtyIpaEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrSrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrSrBGtyIpaIndex"),
)
if mibBuilder.loadTexts:
    ipiFrSrBGtyIpaEntry.setStatus("mandatory")


class _IpiFrSrBGtyIpaIndex_Type(Integer32):
    """Custom type ipiFrSrBGtyIpaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_IpiFrSrBGtyIpaIndex_Type.__name__ = "Integer32"
_IpiFrSrBGtyIpaIndex_Object = MibTableColumn
ipiFrSrBGtyIpaIndex = _IpiFrSrBGtyIpaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 327, 1, 1),
    _IpiFrSrBGtyIpaIndex_Type()
)
ipiFrSrBGtyIpaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrSrBGtyIpaIndex.setStatus("mandatory")
_IpiFrSrBGtyIpaValue_Type = IpAddress
_IpiFrSrBGtyIpaValue_Object = MibTableColumn
ipiFrSrBGtyIpaValue = _IpiFrSrBGtyIpaValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 327, 1, 2),
    _IpiFrSrBGtyIpaValue_Type()
)
ipiFrSrBGtyIpaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrSrBGtyIpaValue.setStatus("mandatory")
_IpiFrSrBGtyIpaRowStatus_Type = RowStatus
_IpiFrSrBGtyIpaRowStatus_Object = MibTableColumn
ipiFrSrBGtyIpaRowStatus = _IpiFrSrBGtyIpaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 5, 327, 1, 3),
    _IpiFrSrBGtyIpaRowStatus_Type()
)
ipiFrSrBGtyIpaRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ipiFrSrBGtyIpaRowStatus.setStatus("mandatory")
_IpiFrR_ObjectIdentity = ObjectIdentity
ipiFrR = _IpiFrR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6)
)
_IpiFrRRowStatusTable_Object = MibTable
ipiFrRRowStatusTable = _IpiFrRRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 1)
)
if mibBuilder.loadTexts:
    ipiFrRRowStatusTable.setStatus("mandatory")
_IpiFrRRowStatusEntry_Object = MibTableRow
ipiFrRRowStatusEntry = _IpiFrRRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 1, 1)
)
ipiFrRRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrRIndex"),
)
if mibBuilder.loadTexts:
    ipiFrRRowStatusEntry.setStatus("mandatory")
_IpiFrRRowStatus_Type = RowStatus
_IpiFrRRowStatus_Object = MibTableColumn
ipiFrRRowStatus = _IpiFrRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 1, 1, 1),
    _IpiFrRRowStatus_Type()
)
ipiFrRRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrRRowStatus.setStatus("mandatory")
_IpiFrRComponentName_Type = DisplayString
_IpiFrRComponentName_Object = MibTableColumn
ipiFrRComponentName = _IpiFrRComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 1, 1, 2),
    _IpiFrRComponentName_Type()
)
ipiFrRComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrRComponentName.setStatus("mandatory")
_IpiFrRStorageType_Type = StorageType
_IpiFrRStorageType_Object = MibTableColumn
ipiFrRStorageType = _IpiFrRStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 1, 1, 4),
    _IpiFrRStorageType_Type()
)
ipiFrRStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrRStorageType.setStatus("mandatory")
_IpiFrRIndex_Type = IpAddress
_IpiFrRIndex_Object = MibTableColumn
ipiFrRIndex = _IpiFrRIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 1, 1, 10),
    _IpiFrRIndex_Type()
)
ipiFrRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiFrRIndex.setStatus("mandatory")
_IpiFrROperTable_Object = MibTable
ipiFrROperTable = _IpiFrROperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 10)
)
if mibBuilder.loadTexts:
    ipiFrROperTable.setStatus("mandatory")
_IpiFrROperEntry_Object = MibTableRow
ipiFrROperEntry = _IpiFrROperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 10, 1)
)
ipiFrROperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrRIndex"),
)
if mibBuilder.loadTexts:
    ipiFrROperEntry.setStatus("mandatory")


class _IpiFrRGtyIpAddr_Type(IpAddress):
    """Custom type ipiFrRGtyIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpiFrRGtyIpAddr_Object = MibTableColumn
ipiFrRGtyIpAddr = _IpiFrRGtyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 10, 1, 1),
    _IpiFrRGtyIpAddr_Type()
)
ipiFrRGtyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrRGtyIpAddr.setStatus("mandatory")


class _IpiFrRLcnIf_Type(Unsigned32):
    """Custom type ipiFrRLcnIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 39),
    )


_IpiFrRLcnIf_Type.__name__ = "Unsigned32"
_IpiFrRLcnIf_Object = MibTableColumn
ipiFrRLcnIf = _IpiFrRLcnIf_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 10, 1, 3),
    _IpiFrRLcnIf_Type()
)
ipiFrRLcnIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrRLcnIf.setStatus("mandatory")


class _IpiFrRType_Type(Integer32):
    """Custom type ipiFrRType based on Integer32"""
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


_IpiFrRType_Type.__name__ = "Integer32"
_IpiFrRType_Object = MibTableColumn
ipiFrRType = _IpiFrRType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 6, 10, 1, 4),
    _IpiFrRType_Type()
)
ipiFrRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrRType.setStatus("mandatory")
_IpiFrProvTable_Object = MibTable
ipiFrProvTable = _IpiFrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 10)
)
if mibBuilder.loadTexts:
    ipiFrProvTable.setStatus("mandatory")
_IpiFrProvEntry_Object = MibTableRow
ipiFrProvEntry = _IpiFrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 10, 1)
)
ipiFrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiFrMIB", "ipiFrIndex"),
)
if mibBuilder.loadTexts:
    ipiFrProvEntry.setStatus("mandatory")


class _IpiFrIpAddress_Type(IpAddress):
    """Custom type ipiFrIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpiFrIpAddress_Object = MibTableColumn
ipiFrIpAddress = _IpiFrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 10, 1, 1),
    _IpiFrIpAddress_Type()
)
ipiFrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrIpAddress.setStatus("mandatory")


class _IpiFrMaximumNumberOfLcn_Type(Unsigned32):
    """Custom type ipiFrMaximumNumberOfLcn based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 24),
    )


_IpiFrMaximumNumberOfLcn_Type.__name__ = "Unsigned32"
_IpiFrMaximumNumberOfLcn_Object = MibTableColumn
ipiFrMaximumNumberOfLcn = _IpiFrMaximumNumberOfLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 10, 1, 2),
    _IpiFrMaximumNumberOfLcn_Type()
)
ipiFrMaximumNumberOfLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiFrMaximumNumberOfLcn.setStatus("mandatory")


class _IpiFrSubnetMask_Type(IpAddress):
    """Custom type ipiFrSubnetMask based on IpAddress"""
    defaultHexValue = "ff000000"


_IpiFrSubnetMask_Object = MibTableColumn
ipiFrSubnetMask = _IpiFrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 50, 10, 1, 3),
    _IpiFrSubnetMask_Type()
)
ipiFrSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipiFrSubnetMask.setStatus("mandatory")
_IpiFrMIB_ObjectIdentity = ObjectIdentity
ipiFrMIB = _IpiFrMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35)
)
_IpiFrGroup_ObjectIdentity = ObjectIdentity
ipiFrGroup = _IpiFrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 1)
)
_IpiFrGroupBE_ObjectIdentity = ObjectIdentity
ipiFrGroupBE = _IpiFrGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 1, 5)
)
_IpiFrGroupBE01_ObjectIdentity = ObjectIdentity
ipiFrGroupBE01 = _IpiFrGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 1, 5, 2)
)
_IpiFrGroupBE01A_ObjectIdentity = ObjectIdentity
ipiFrGroupBE01A = _IpiFrGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 1, 5, 2, 2)
)
_IpiFrCapabilities_ObjectIdentity = ObjectIdentity
ipiFrCapabilities = _IpiFrCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 3)
)
_IpiFrCapabilitiesBE_ObjectIdentity = ObjectIdentity
ipiFrCapabilitiesBE = _IpiFrCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 3, 5)
)
_IpiFrCapabilitiesBE01_ObjectIdentity = ObjectIdentity
ipiFrCapabilitiesBE01 = _IpiFrCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 3, 5, 2)
)
_IpiFrCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
ipiFrCapabilitiesBE01A = _IpiFrCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 35, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-IpiFrMIB",
    **{"ipiFr": ipiFr,
       "ipiFrRowStatusTable": ipiFrRowStatusTable,
       "ipiFrRowStatusEntry": ipiFrRowStatusEntry,
       "ipiFrRowStatus": ipiFrRowStatus,
       "ipiFrComponentName": ipiFrComponentName,
       "ipiFrStorageType": ipiFrStorageType,
       "ipiFrIndex": ipiFrIndex,
       "ipiFrDna": ipiFrDna,
       "ipiFrDnaRowStatusTable": ipiFrDnaRowStatusTable,
       "ipiFrDnaRowStatusEntry": ipiFrDnaRowStatusEntry,
       "ipiFrDnaRowStatus": ipiFrDnaRowStatus,
       "ipiFrDnaComponentName": ipiFrDnaComponentName,
       "ipiFrDnaStorageType": ipiFrDnaStorageType,
       "ipiFrDnaIndex": ipiFrDnaIndex,
       "ipiFrDnaCug": ipiFrDnaCug,
       "ipiFrDnaCugRowStatusTable": ipiFrDnaCugRowStatusTable,
       "ipiFrDnaCugRowStatusEntry": ipiFrDnaCugRowStatusEntry,
       "ipiFrDnaCugRowStatus": ipiFrDnaCugRowStatus,
       "ipiFrDnaCugComponentName": ipiFrDnaCugComponentName,
       "ipiFrDnaCugStorageType": ipiFrDnaCugStorageType,
       "ipiFrDnaCugIndex": ipiFrDnaCugIndex,
       "ipiFrDnaCugCugOptionsTable": ipiFrDnaCugCugOptionsTable,
       "ipiFrDnaCugCugOptionsEntry": ipiFrDnaCugCugOptionsEntry,
       "ipiFrDnaCugType": ipiFrDnaCugType,
       "ipiFrDnaCugDnic": ipiFrDnaCugDnic,
       "ipiFrDnaCugInterlockCode": ipiFrDnaCugInterlockCode,
       "ipiFrDnaCugIncCalls": ipiFrDnaCugIncCalls,
       "ipiFrDnaAddressTable": ipiFrDnaAddressTable,
       "ipiFrDnaAddressEntry": ipiFrDnaAddressEntry,
       "ipiFrDnaNumberingPlanIndicator": ipiFrDnaNumberingPlanIndicator,
       "ipiFrDnaDataNetworkAddress": ipiFrDnaDataNetworkAddress,
       "ipiFrDnaOutgoingOptionsTable": ipiFrDnaOutgoingOptionsTable,
       "ipiFrDnaOutgoingOptionsEntry": ipiFrDnaOutgoingOptionsEntry,
       "ipiFrDnaOutCalls": ipiFrDnaOutCalls,
       "ipiFrDnaOutDefaultPriority": ipiFrDnaOutDefaultPriority,
       "ipiFrDnaOutDefaultPathSensitivity": ipiFrDnaOutDefaultPathSensitivity,
       "ipiFrDnaOutPathSensitivityOverRide": ipiFrDnaOutPathSensitivityOverRide,
       "ipiFrDnaDefaultTransferPriority": ipiFrDnaDefaultTransferPriority,
       "ipiFrDnaTransferPriorityOverRide": ipiFrDnaTransferPriorityOverRide,
       "ipiFrDnaIncomingOptionsTable": ipiFrDnaIncomingOptionsTable,
       "ipiFrDnaIncomingOptionsEntry": ipiFrDnaIncomingOptionsEntry,
       "ipiFrDnaIncCalls": ipiFrDnaIncCalls,
       "ipiFrDnaIncAccess": ipiFrDnaIncAccess,
       "ipiFrDnaCallOptionsTable": ipiFrDnaCallOptionsTable,
       "ipiFrDnaCallOptionsEntry": ipiFrDnaCallOptionsEntry,
       "ipiFrDnaServiceCategory": ipiFrDnaServiceCategory,
       "ipiFrDnaAccountClass": ipiFrDnaAccountClass,
       "ipiFrDnaServiceExchange": ipiFrDnaServiceExchange,
       "ipiFrLcn": ipiFrLcn,
       "ipiFrLcnRowStatusTable": ipiFrLcnRowStatusTable,
       "ipiFrLcnRowStatusEntry": ipiFrLcnRowStatusEntry,
       "ipiFrLcnRowStatus": ipiFrLcnRowStatus,
       "ipiFrLcnComponentName": ipiFrLcnComponentName,
       "ipiFrLcnStorageType": ipiFrLcnStorageType,
       "ipiFrLcnIndex": ipiFrLcnIndex,
       "ipiFrLcnDc": ipiFrLcnDc,
       "ipiFrLcnDcRowStatusTable": ipiFrLcnDcRowStatusTable,
       "ipiFrLcnDcRowStatusEntry": ipiFrLcnDcRowStatusEntry,
       "ipiFrLcnDcRowStatus": ipiFrLcnDcRowStatus,
       "ipiFrLcnDcComponentName": ipiFrLcnDcComponentName,
       "ipiFrLcnDcStorageType": ipiFrLcnDcStorageType,
       "ipiFrLcnDcIndex": ipiFrLcnDcIndex,
       "ipiFrLcnDcOptionsTable": ipiFrLcnDcOptionsTable,
       "ipiFrLcnDcOptionsEntry": ipiFrLcnDcOptionsEntry,
       "ipiFrLcnDcRemoteNpi": ipiFrLcnDcRemoteNpi,
       "ipiFrLcnDcRemoteDna": ipiFrLcnDcRemoteDna,
       "ipiFrLcnDcRemoteDlci": ipiFrLcnDcRemoteDlci,
       "ipiFrLcnDcType": ipiFrLcnDcType,
       "ipiFrLcnDcTransferPriority": ipiFrLcnDcTransferPriority,
       "ipiFrLcnDcDiscardPriority": ipiFrLcnDcDiscardPriority,
       "ipiFrLcnDcNfaTable": ipiFrLcnDcNfaTable,
       "ipiFrLcnDcNfaEntry": ipiFrLcnDcNfaEntry,
       "ipiFrLcnDcNfaIndex": ipiFrLcnDcNfaIndex,
       "ipiFrLcnDcNfaValue": ipiFrLcnDcNfaValue,
       "ipiFrLcnDcNfaRowStatus": ipiFrLcnDcNfaRowStatus,
       "ipiFrLcnVc": ipiFrLcnVc,
       "ipiFrLcnVcRowStatusTable": ipiFrLcnVcRowStatusTable,
       "ipiFrLcnVcRowStatusEntry": ipiFrLcnVcRowStatusEntry,
       "ipiFrLcnVcRowStatus": ipiFrLcnVcRowStatus,
       "ipiFrLcnVcComponentName": ipiFrLcnVcComponentName,
       "ipiFrLcnVcStorageType": ipiFrLcnVcStorageType,
       "ipiFrLcnVcIndex": ipiFrLcnVcIndex,
       "ipiFrLcnVcCadTable": ipiFrLcnVcCadTable,
       "ipiFrLcnVcCadEntry": ipiFrLcnVcCadEntry,
       "ipiFrLcnVcType": ipiFrLcnVcType,
       "ipiFrLcnVcState": ipiFrLcnVcState,
       "ipiFrLcnVcPreviousState": ipiFrLcnVcPreviousState,
       "ipiFrLcnVcDiagnosticCode": ipiFrLcnVcDiagnosticCode,
       "ipiFrLcnVcPreviousDiagnosticCode": ipiFrLcnVcPreviousDiagnosticCode,
       "ipiFrLcnVcCalledNpi": ipiFrLcnVcCalledNpi,
       "ipiFrLcnVcCalledDna": ipiFrLcnVcCalledDna,
       "ipiFrLcnVcCalledLcn": ipiFrLcnVcCalledLcn,
       "ipiFrLcnVcCallingNpi": ipiFrLcnVcCallingNpi,
       "ipiFrLcnVcCallingDna": ipiFrLcnVcCallingDna,
       "ipiFrLcnVcCallingLcn": ipiFrLcnVcCallingLcn,
       "ipiFrLcnVcAccountingEnabled": ipiFrLcnVcAccountingEnabled,
       "ipiFrLcnVcFastSelectCall": ipiFrLcnVcFastSelectCall,
       "ipiFrLcnVcPathReliability": ipiFrLcnVcPathReliability,
       "ipiFrLcnVcAccountingEnd": ipiFrLcnVcAccountingEnd,
       "ipiFrLcnVcPriority": ipiFrLcnVcPriority,
       "ipiFrLcnVcSegmentSize": ipiFrLcnVcSegmentSize,
       "ipiFrLcnVcMaxSubnetPktSize": ipiFrLcnVcMaxSubnetPktSize,
       "ipiFrLcnVcRcosToNetwork": ipiFrLcnVcRcosToNetwork,
       "ipiFrLcnVcRcosFromNetwork": ipiFrLcnVcRcosFromNetwork,
       "ipiFrLcnVcEmissionPriorityToNetwork": ipiFrLcnVcEmissionPriorityToNetwork,
       "ipiFrLcnVcEmissionPriorityFromNetwork": ipiFrLcnVcEmissionPriorityFromNetwork,
       "ipiFrLcnVcDataPath": ipiFrLcnVcDataPath,
       "ipiFrLcnVcIntdTable": ipiFrLcnVcIntdTable,
       "ipiFrLcnVcIntdEntry": ipiFrLcnVcIntdEntry,
       "ipiFrLcnVcCallReferenceNumber": ipiFrLcnVcCallReferenceNumber,
       "ipiFrLcnVcElapsedTimeTillNow": ipiFrLcnVcElapsedTimeTillNow,
       "ipiFrLcnVcSegmentsRx": ipiFrLcnVcSegmentsRx,
       "ipiFrLcnVcSegmentsSent": ipiFrLcnVcSegmentsSent,
       "ipiFrLcnVcStartTime": ipiFrLcnVcStartTime,
       "ipiFrLcnVcFrdTable": ipiFrLcnVcFrdTable,
       "ipiFrLcnVcFrdEntry": ipiFrLcnVcFrdEntry,
       "ipiFrLcnVcFrmCongestedToSubnet": ipiFrLcnVcFrmCongestedToSubnet,
       "ipiFrLcnVcCannotForwardToSubnet": ipiFrLcnVcCannotForwardToSubnet,
       "ipiFrLcnVcNotDataXferToSubnet": ipiFrLcnVcNotDataXferToSubnet,
       "ipiFrLcnVcOutOfRangeFrmFromSubnet": ipiFrLcnVcOutOfRangeFrmFromSubnet,
       "ipiFrLcnVcCombErrorsFromSubnet": ipiFrLcnVcCombErrorsFromSubnet,
       "ipiFrLcnVcDuplicatesFromSubnet": ipiFrLcnVcDuplicatesFromSubnet,
       "ipiFrLcnVcNotDataXferFromSubnet": ipiFrLcnVcNotDataXferFromSubnet,
       "ipiFrLcnVcFrmLossTimeouts": ipiFrLcnVcFrmLossTimeouts,
       "ipiFrLcnVcOoSeqByteCntExceeded": ipiFrLcnVcOoSeqByteCntExceeded,
       "ipiFrLcnVcPeakOoSeqPktCount": ipiFrLcnVcPeakOoSeqPktCount,
       "ipiFrLcnVcPeakOoSeqFrmForwarded": ipiFrLcnVcPeakOoSeqFrmForwarded,
       "ipiFrLcnVcSendSequenceNumber": ipiFrLcnVcSendSequenceNumber,
       "ipiFrLcnVcPktRetryTimeouts": ipiFrLcnVcPktRetryTimeouts,
       "ipiFrLcnVcPeakRetryQueueSize": ipiFrLcnVcPeakRetryQueueSize,
       "ipiFrLcnVcSubnetRecoveries": ipiFrLcnVcSubnetRecoveries,
       "ipiFrLcnVcOoSeqPktCntExceeded": ipiFrLcnVcOoSeqPktCntExceeded,
       "ipiFrLcnVcPeakOoSeqByteCount": ipiFrLcnVcPeakOoSeqByteCount,
       "ipiFrLcnVcDmepTable": ipiFrLcnVcDmepTable,
       "ipiFrLcnVcDmepEntry": ipiFrLcnVcDmepEntry,
       "ipiFrLcnVcDmepValue": ipiFrLcnVcDmepValue,
       "ipiFrLcnStateTable": ipiFrLcnStateTable,
       "ipiFrLcnStateEntry": ipiFrLcnStateEntry,
       "ipiFrLcnAdminState": ipiFrLcnAdminState,
       "ipiFrLcnOperationalState": ipiFrLcnOperationalState,
       "ipiFrLcnUsageState": ipiFrLcnUsageState,
       "ipiFrLcnAvailabilityStatus": ipiFrLcnAvailabilityStatus,
       "ipiFrLcnProceduralStatus": ipiFrLcnProceduralStatus,
       "ipiFrLcnControlStatus": ipiFrLcnControlStatus,
       "ipiFrLcnAlarmStatus": ipiFrLcnAlarmStatus,
       "ipiFrLcnStandbyStatus": ipiFrLcnStandbyStatus,
       "ipiFrLcnUnknownStatus": ipiFrLcnUnknownStatus,
       "ipiFrLcnOperTable": ipiFrLcnOperTable,
       "ipiFrLcnOperEntry": ipiFrLcnOperEntry,
       "ipiFrLcnIpInterfaceDevice": ipiFrLcnIpInterfaceDevice,
       "ipiFrLcnOpRemoteIpAddress": ipiFrLcnOpRemoteIpAddress,
       "ipiFrLcnPacketsSent": ipiFrLcnPacketsSent,
       "ipiFrLcnPacketsReceived": ipiFrLcnPacketsReceived,
       "ipiFrLcnDiscardTxPackets": ipiFrLcnDiscardTxPackets,
       "ipiFrLcnDiscardRcvPackets": ipiFrLcnDiscardRcvPackets,
       "ipiFrLcnProvTable": ipiFrLcnProvTable,
       "ipiFrLcnProvEntry": ipiFrLcnProvEntry,
       "ipiFrLcnRemoteIpAddress": ipiFrLcnRemoteIpAddress,
       "ipiFrSr": ipiFrSr,
       "ipiFrSrRowStatusTable": ipiFrSrRowStatusTable,
       "ipiFrSrRowStatusEntry": ipiFrSrRowStatusEntry,
       "ipiFrSrRowStatus": ipiFrSrRowStatus,
       "ipiFrSrComponentName": ipiFrSrComponentName,
       "ipiFrSrStorageType": ipiFrSrStorageType,
       "ipiFrSrIndex": ipiFrSrIndex,
       "ipiFrSrProvTable": ipiFrSrProvTable,
       "ipiFrSrProvEntry": ipiFrSrProvEntry,
       "ipiFrSrGatewayIpAddress": ipiFrSrGatewayIpAddress,
       "ipiFrSrBGtyIpaTable": ipiFrSrBGtyIpaTable,
       "ipiFrSrBGtyIpaEntry": ipiFrSrBGtyIpaEntry,
       "ipiFrSrBGtyIpaIndex": ipiFrSrBGtyIpaIndex,
       "ipiFrSrBGtyIpaValue": ipiFrSrBGtyIpaValue,
       "ipiFrSrBGtyIpaRowStatus": ipiFrSrBGtyIpaRowStatus,
       "ipiFrR": ipiFrR,
       "ipiFrRRowStatusTable": ipiFrRRowStatusTable,
       "ipiFrRRowStatusEntry": ipiFrRRowStatusEntry,
       "ipiFrRRowStatus": ipiFrRRowStatus,
       "ipiFrRComponentName": ipiFrRComponentName,
       "ipiFrRStorageType": ipiFrRStorageType,
       "ipiFrRIndex": ipiFrRIndex,
       "ipiFrROperTable": ipiFrROperTable,
       "ipiFrROperEntry": ipiFrROperEntry,
       "ipiFrRGtyIpAddr": ipiFrRGtyIpAddr,
       "ipiFrRLcnIf": ipiFrRLcnIf,
       "ipiFrRType": ipiFrRType,
       "ipiFrProvTable": ipiFrProvTable,
       "ipiFrProvEntry": ipiFrProvEntry,
       "ipiFrIpAddress": ipiFrIpAddress,
       "ipiFrMaximumNumberOfLcn": ipiFrMaximumNumberOfLcn,
       "ipiFrSubnetMask": ipiFrSubnetMask,
       "ipiFrMIB": ipiFrMIB,
       "ipiFrGroup": ipiFrGroup,
       "ipiFrGroupBE": ipiFrGroupBE,
       "ipiFrGroupBE01": ipiFrGroupBE01,
       "ipiFrGroupBE01A": ipiFrGroupBE01A,
       "ipiFrCapabilities": ipiFrCapabilities,
       "ipiFrCapabilitiesBE": ipiFrCapabilitiesBE,
       "ipiFrCapabilitiesBE01": ipiFrCapabilitiesBE01,
       "ipiFrCapabilitiesBE01A": ipiFrCapabilitiesBE01A}
)
