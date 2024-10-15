# SNMP MIB module (Nortel-Magellan-Passport-IpiVcMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-IpiVcMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:02 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(DigitString,
 EnterpriseDateAndTime,
 Hex,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
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

_Ipivc_ObjectIdentity = ObjectIdentity
ipivc = _Ipivc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51)
)
_IpivcRowStatusTable_Object = MibTable
ipivcRowStatusTable = _IpivcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 1)
)
if mibBuilder.loadTexts:
    ipivcRowStatusTable.setStatus("mandatory")
_IpivcRowStatusEntry_Object = MibTableRow
ipivcRowStatusEntry = _IpivcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 1, 1)
)
ipivcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
)
if mibBuilder.loadTexts:
    ipivcRowStatusEntry.setStatus("mandatory")
_IpivcRowStatus_Type = RowStatus
_IpivcRowStatus_Object = MibTableColumn
ipivcRowStatus = _IpivcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 1, 1, 1),
    _IpivcRowStatus_Type()
)
ipivcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcRowStatus.setStatus("mandatory")
_IpivcComponentName_Type = DisplayString
_IpivcComponentName_Object = MibTableColumn
ipivcComponentName = _IpivcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 1, 1, 2),
    _IpivcComponentName_Type()
)
ipivcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcComponentName.setStatus("mandatory")
_IpivcStorageType_Type = StorageType
_IpivcStorageType_Object = MibTableColumn
ipivcStorageType = _IpivcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 1, 1, 4),
    _IpivcStorageType_Type()
)
ipivcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcStorageType.setStatus("mandatory")
_IpivcIndex_Type = NonReplicated
_IpivcIndex_Object = MibTableColumn
ipivcIndex = _IpivcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 1, 1, 10),
    _IpivcIndex_Type()
)
ipivcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipivcIndex.setStatus("mandatory")
_IpivcDna_ObjectIdentity = ObjectIdentity
ipivcDna = _IpivcDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2)
)
_IpivcDnaRowStatusTable_Object = MibTable
ipivcDnaRowStatusTable = _IpivcDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 1)
)
if mibBuilder.loadTexts:
    ipivcDnaRowStatusTable.setStatus("mandatory")
_IpivcDnaRowStatusEntry_Object = MibTableRow
ipivcDnaRowStatusEntry = _IpivcDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 1, 1)
)
ipivcDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaIndex"),
)
if mibBuilder.loadTexts:
    ipivcDnaRowStatusEntry.setStatus("mandatory")
_IpivcDnaRowStatus_Type = RowStatus
_IpivcDnaRowStatus_Object = MibTableColumn
ipivcDnaRowStatus = _IpivcDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 1, 1, 1),
    _IpivcDnaRowStatus_Type()
)
ipivcDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaRowStatus.setStatus("mandatory")
_IpivcDnaComponentName_Type = DisplayString
_IpivcDnaComponentName_Object = MibTableColumn
ipivcDnaComponentName = _IpivcDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 1, 1, 2),
    _IpivcDnaComponentName_Type()
)
ipivcDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaComponentName.setStatus("mandatory")
_IpivcDnaStorageType_Type = StorageType
_IpivcDnaStorageType_Object = MibTableColumn
ipivcDnaStorageType = _IpivcDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 1, 1, 4),
    _IpivcDnaStorageType_Type()
)
ipivcDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaStorageType.setStatus("mandatory")
_IpivcDnaIndex_Type = NonReplicated
_IpivcDnaIndex_Object = MibTableColumn
ipivcDnaIndex = _IpivcDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 1, 1, 10),
    _IpivcDnaIndex_Type()
)
ipivcDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipivcDnaIndex.setStatus("mandatory")
_IpivcDnaCug_ObjectIdentity = ObjectIdentity
ipivcDnaCug = _IpivcDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2)
)
_IpivcDnaCugRowStatusTable_Object = MibTable
ipivcDnaCugRowStatusTable = _IpivcDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ipivcDnaCugRowStatusTable.setStatus("mandatory")
_IpivcDnaCugRowStatusEntry_Object = MibTableRow
ipivcDnaCugRowStatusEntry = _IpivcDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 1, 1)
)
ipivcDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaCugIndex"),
)
if mibBuilder.loadTexts:
    ipivcDnaCugRowStatusEntry.setStatus("mandatory")
_IpivcDnaCugRowStatus_Type = RowStatus
_IpivcDnaCugRowStatus_Object = MibTableColumn
ipivcDnaCugRowStatus = _IpivcDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 1, 1, 1),
    _IpivcDnaCugRowStatus_Type()
)
ipivcDnaCugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaCugRowStatus.setStatus("mandatory")
_IpivcDnaCugComponentName_Type = DisplayString
_IpivcDnaCugComponentName_Object = MibTableColumn
ipivcDnaCugComponentName = _IpivcDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 1, 1, 2),
    _IpivcDnaCugComponentName_Type()
)
ipivcDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaCugComponentName.setStatus("mandatory")
_IpivcDnaCugStorageType_Type = StorageType
_IpivcDnaCugStorageType_Object = MibTableColumn
ipivcDnaCugStorageType = _IpivcDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 1, 1, 4),
    _IpivcDnaCugStorageType_Type()
)
ipivcDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaCugStorageType.setStatus("mandatory")
_IpivcDnaCugIndex_Type = NonReplicated
_IpivcDnaCugIndex_Object = MibTableColumn
ipivcDnaCugIndex = _IpivcDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 1, 1, 10),
    _IpivcDnaCugIndex_Type()
)
ipivcDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipivcDnaCugIndex.setStatus("mandatory")
_IpivcDnaCugCugOptionsTable_Object = MibTable
ipivcDnaCugCugOptionsTable = _IpivcDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10)
)
if mibBuilder.loadTexts:
    ipivcDnaCugCugOptionsTable.setStatus("mandatory")
_IpivcDnaCugCugOptionsEntry_Object = MibTableRow
ipivcDnaCugCugOptionsEntry = _IpivcDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10, 1)
)
ipivcDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaCugIndex"),
)
if mibBuilder.loadTexts:
    ipivcDnaCugCugOptionsEntry.setStatus("mandatory")


class _IpivcDnaCugType_Type(Integer32):
    """Custom type ipivcDnaCugType based on Integer32"""
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


_IpivcDnaCugType_Type.__name__ = "Integer32"
_IpivcDnaCugType_Object = MibTableColumn
ipivcDnaCugType = _IpivcDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10, 1, 1),
    _IpivcDnaCugType_Type()
)
ipivcDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaCugType.setStatus("mandatory")


class _IpivcDnaCugDnic_Type(DigitString):
    """Custom type ipivcDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpivcDnaCugDnic_Type.__name__ = "DigitString"
_IpivcDnaCugDnic_Object = MibTableColumn
ipivcDnaCugDnic = _IpivcDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10, 1, 2),
    _IpivcDnaCugDnic_Type()
)
ipivcDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaCugDnic.setStatus("mandatory")


class _IpivcDnaCugInterlockCode_Type(Unsigned32):
    """Custom type ipivcDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpivcDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_IpivcDnaCugInterlockCode_Object = MibTableColumn
ipivcDnaCugInterlockCode = _IpivcDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10, 1, 3),
    _IpivcDnaCugInterlockCode_Type()
)
ipivcDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaCugInterlockCode.setStatus("mandatory")


class _IpivcDnaCugOutCalls_Type(Integer32):
    """Custom type ipivcDnaCugOutCalls based on Integer32"""
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


_IpivcDnaCugOutCalls_Type.__name__ = "Integer32"
_IpivcDnaCugOutCalls_Object = MibTableColumn
ipivcDnaCugOutCalls = _IpivcDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10, 1, 5),
    _IpivcDnaCugOutCalls_Type()
)
ipivcDnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaCugOutCalls.setStatus("mandatory")


class _IpivcDnaCugIncCalls_Type(Integer32):
    """Custom type ipivcDnaCugIncCalls based on Integer32"""
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


_IpivcDnaCugIncCalls_Type.__name__ = "Integer32"
_IpivcDnaCugIncCalls_Object = MibTableColumn
ipivcDnaCugIncCalls = _IpivcDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10, 1, 6),
    _IpivcDnaCugIncCalls_Type()
)
ipivcDnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaCugIncCalls.setStatus("mandatory")


class _IpivcDnaCugPrivileged_Type(Integer32):
    """Custom type ipivcDnaCugPrivileged based on Integer32"""
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


_IpivcDnaCugPrivileged_Type.__name__ = "Integer32"
_IpivcDnaCugPrivileged_Object = MibTableColumn
ipivcDnaCugPrivileged = _IpivcDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 2, 10, 1, 7),
    _IpivcDnaCugPrivileged_Type()
)
ipivcDnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaCugPrivileged.setStatus("mandatory")
_IpivcDnaAddressTable_Object = MibTable
ipivcDnaAddressTable = _IpivcDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 10)
)
if mibBuilder.loadTexts:
    ipivcDnaAddressTable.setStatus("mandatory")
_IpivcDnaAddressEntry_Object = MibTableRow
ipivcDnaAddressEntry = _IpivcDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 10, 1)
)
ipivcDnaAddressEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaIndex"),
)
if mibBuilder.loadTexts:
    ipivcDnaAddressEntry.setStatus("mandatory")


class _IpivcDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type ipivcDnaNumberingPlanIndicator based on Integer32"""
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


_IpivcDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_IpivcDnaNumberingPlanIndicator_Object = MibTableColumn
ipivcDnaNumberingPlanIndicator = _IpivcDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 10, 1, 1),
    _IpivcDnaNumberingPlanIndicator_Type()
)
ipivcDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaNumberingPlanIndicator.setStatus("mandatory")


class _IpivcDnaDataNetworkAddress_Type(DigitString):
    """Custom type ipivcDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpivcDnaDataNetworkAddress_Type.__name__ = "DigitString"
_IpivcDnaDataNetworkAddress_Object = MibTableColumn
ipivcDnaDataNetworkAddress = _IpivcDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 10, 1, 2),
    _IpivcDnaDataNetworkAddress_Type()
)
ipivcDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaDataNetworkAddress.setStatus("mandatory")
_IpivcDnaOutgoingOptionsTable_Object = MibTable
ipivcDnaOutgoingOptionsTable = _IpivcDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 11)
)
if mibBuilder.loadTexts:
    ipivcDnaOutgoingOptionsTable.setStatus("mandatory")
_IpivcDnaOutgoingOptionsEntry_Object = MibTableRow
ipivcDnaOutgoingOptionsEntry = _IpivcDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 11, 1)
)
ipivcDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaIndex"),
)
if mibBuilder.loadTexts:
    ipivcDnaOutgoingOptionsEntry.setStatus("mandatory")


class _IpivcDnaOutCalls_Type(Integer32):
    """Custom type ipivcDnaOutCalls based on Integer32"""
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


_IpivcDnaOutCalls_Type.__name__ = "Integer32"
_IpivcDnaOutCalls_Object = MibTableColumn
ipivcDnaOutCalls = _IpivcDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 11, 1, 1),
    _IpivcDnaOutCalls_Type()
)
ipivcDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaOutCalls.setStatus("mandatory")


class _IpivcDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type ipivcDnaOutDefaultPathSensitivity based on Integer32"""
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


_IpivcDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_IpivcDnaOutDefaultPathSensitivity_Object = MibTableColumn
ipivcDnaOutDefaultPathSensitivity = _IpivcDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 11, 1, 11),
    _IpivcDnaOutDefaultPathSensitivity_Type()
)
ipivcDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _IpivcDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type ipivcDnaOutPathSensitivityOverRide based on Integer32"""
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


_IpivcDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_IpivcDnaOutPathSensitivityOverRide_Object = MibTableColumn
ipivcDnaOutPathSensitivityOverRide = _IpivcDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 11, 1, 12),
    _IpivcDnaOutPathSensitivityOverRide_Type()
)
ipivcDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _IpivcDnaDefaultTransferPriority_Type(Integer32):
    """Custom type ipivcDnaDefaultTransferPriority based on Integer32"""
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


_IpivcDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_IpivcDnaDefaultTransferPriority_Object = MibTableColumn
ipivcDnaDefaultTransferPriority = _IpivcDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 11, 1, 18),
    _IpivcDnaDefaultTransferPriority_Type()
)
ipivcDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaDefaultTransferPriority.setStatus("mandatory")


class _IpivcDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type ipivcDnaTransferPriorityOverRide based on Integer32"""
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


_IpivcDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_IpivcDnaTransferPriorityOverRide_Object = MibTableColumn
ipivcDnaTransferPriorityOverRide = _IpivcDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 11, 1, 19),
    _IpivcDnaTransferPriorityOverRide_Type()
)
ipivcDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaTransferPriorityOverRide.setStatus("mandatory")
_IpivcDnaIncomingOptionsTable_Object = MibTable
ipivcDnaIncomingOptionsTable = _IpivcDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12)
)
if mibBuilder.loadTexts:
    ipivcDnaIncomingOptionsTable.setStatus("mandatory")
_IpivcDnaIncomingOptionsEntry_Object = MibTableRow
ipivcDnaIncomingOptionsEntry = _IpivcDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1)
)
ipivcDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaIndex"),
)
if mibBuilder.loadTexts:
    ipivcDnaIncomingOptionsEntry.setStatus("mandatory")


class _IpivcDnaIncCalls_Type(Integer32):
    """Custom type ipivcDnaIncCalls based on Integer32"""
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


_IpivcDnaIncCalls_Type.__name__ = "Integer32"
_IpivcDnaIncCalls_Object = MibTableColumn
ipivcDnaIncCalls = _IpivcDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 1),
    _IpivcDnaIncCalls_Type()
)
ipivcDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncCalls.setStatus("mandatory")


class _IpivcDnaIncHighPriorityReverseCharge_Type(Integer32):
    """Custom type ipivcDnaIncHighPriorityReverseCharge based on Integer32"""
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


_IpivcDnaIncHighPriorityReverseCharge_Type.__name__ = "Integer32"
_IpivcDnaIncHighPriorityReverseCharge_Object = MibTableColumn
ipivcDnaIncHighPriorityReverseCharge = _IpivcDnaIncHighPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 2),
    _IpivcDnaIncHighPriorityReverseCharge_Type()
)
ipivcDnaIncHighPriorityReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncHighPriorityReverseCharge.setStatus("mandatory")


class _IpivcDnaIncNormalPriorityReverseCharge_Type(Integer32):
    """Custom type ipivcDnaIncNormalPriorityReverseCharge based on Integer32"""
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


_IpivcDnaIncNormalPriorityReverseCharge_Type.__name__ = "Integer32"
_IpivcDnaIncNormalPriorityReverseCharge_Object = MibTableColumn
ipivcDnaIncNormalPriorityReverseCharge = _IpivcDnaIncNormalPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 3),
    _IpivcDnaIncNormalPriorityReverseCharge_Type()
)
ipivcDnaIncNormalPriorityReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncNormalPriorityReverseCharge.setStatus("mandatory")


class _IpivcDnaIncIntlNormalCharge_Type(Integer32):
    """Custom type ipivcDnaIncIntlNormalCharge based on Integer32"""
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


_IpivcDnaIncIntlNormalCharge_Type.__name__ = "Integer32"
_IpivcDnaIncIntlNormalCharge_Object = MibTableColumn
ipivcDnaIncIntlNormalCharge = _IpivcDnaIncIntlNormalCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 4),
    _IpivcDnaIncIntlNormalCharge_Type()
)
ipivcDnaIncIntlNormalCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncIntlNormalCharge.setStatus("mandatory")


class _IpivcDnaIncIntlReverseCharge_Type(Integer32):
    """Custom type ipivcDnaIncIntlReverseCharge based on Integer32"""
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


_IpivcDnaIncIntlReverseCharge_Type.__name__ = "Integer32"
_IpivcDnaIncIntlReverseCharge_Object = MibTableColumn
ipivcDnaIncIntlReverseCharge = _IpivcDnaIncIntlReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 5),
    _IpivcDnaIncIntlReverseCharge_Type()
)
ipivcDnaIncIntlReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncIntlReverseCharge.setStatus("mandatory")


class _IpivcDnaIncFastSelect_Type(Integer32):
    """Custom type ipivcDnaIncFastSelect based on Integer32"""
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


_IpivcDnaIncFastSelect_Type.__name__ = "Integer32"
_IpivcDnaIncFastSelect_Object = MibTableColumn
ipivcDnaIncFastSelect = _IpivcDnaIncFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 6),
    _IpivcDnaIncFastSelect_Type()
)
ipivcDnaIncFastSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncFastSelect.setStatus("mandatory")


class _IpivcDnaIncSameService_Type(Integer32):
    """Custom type ipivcDnaIncSameService based on Integer32"""
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


_IpivcDnaIncSameService_Type.__name__ = "Integer32"
_IpivcDnaIncSameService_Object = MibTableColumn
ipivcDnaIncSameService = _IpivcDnaIncSameService_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 7),
    _IpivcDnaIncSameService_Type()
)
ipivcDnaIncSameService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncSameService.setStatus("mandatory")


class _IpivcDnaIncChargeTransfer_Type(Integer32):
    """Custom type ipivcDnaIncChargeTransfer based on Integer32"""
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


_IpivcDnaIncChargeTransfer_Type.__name__ = "Integer32"
_IpivcDnaIncChargeTransfer_Object = MibTableColumn
ipivcDnaIncChargeTransfer = _IpivcDnaIncChargeTransfer_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 8),
    _IpivcDnaIncChargeTransfer_Type()
)
ipivcDnaIncChargeTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncChargeTransfer.setStatus("mandatory")


class _IpivcDnaIncAccess_Type(Integer32):
    """Custom type ipivcDnaIncAccess based on Integer32"""
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


_IpivcDnaIncAccess_Type.__name__ = "Integer32"
_IpivcDnaIncAccess_Object = MibTableColumn
ipivcDnaIncAccess = _IpivcDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 12, 1, 9),
    _IpivcDnaIncAccess_Type()
)
ipivcDnaIncAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaIncAccess.setStatus("mandatory")
_IpivcDnaCallOptionsTable_Object = MibTable
ipivcDnaCallOptionsTable = _IpivcDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13)
)
if mibBuilder.loadTexts:
    ipivcDnaCallOptionsTable.setStatus("mandatory")
_IpivcDnaCallOptionsEntry_Object = MibTableRow
ipivcDnaCallOptionsEntry = _IpivcDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1)
)
ipivcDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDnaIndex"),
)
if mibBuilder.loadTexts:
    ipivcDnaCallOptionsEntry.setStatus("mandatory")


class _IpivcDnaServiceCategory_Type(Integer32):
    """Custom type ipivcDnaServiceCategory based on Integer32"""
    defaultValue = 31

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
              31)
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


_IpivcDnaServiceCategory_Type.__name__ = "Integer32"
_IpivcDnaServiceCategory_Object = MibTableColumn
ipivcDnaServiceCategory = _IpivcDnaServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 1),
    _IpivcDnaServiceCategory_Type()
)
ipivcDnaServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaServiceCategory.setStatus("mandatory")


class _IpivcDnaPacketSizes_Type(OctetString):
    """Custom type ipivcDnaPacketSizes based on OctetString"""
    defaultHexValue = "0100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpivcDnaPacketSizes_Type.__name__ = "OctetString"
_IpivcDnaPacketSizes_Object = MibTableColumn
ipivcDnaPacketSizes = _IpivcDnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 2),
    _IpivcDnaPacketSizes_Type()
)
ipivcDnaPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaPacketSizes.setStatus("mandatory")


class _IpivcDnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type ipivcDnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
    defaultValue = 11

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


_IpivcDnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_IpivcDnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
ipivcDnaDefaultRecvFrmNetworkPacketSize = _IpivcDnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 3),
    _IpivcDnaDefaultRecvFrmNetworkPacketSize_Type()
)
ipivcDnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _IpivcDnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type ipivcDnaDefaultSendToNetworkPacketSize based on Integer32"""
    defaultValue = 11

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


_IpivcDnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_IpivcDnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
ipivcDnaDefaultSendToNetworkPacketSize = _IpivcDnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 4),
    _IpivcDnaDefaultSendToNetworkPacketSize_Type()
)
ipivcDnaDefaultSendToNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _IpivcDnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type ipivcDnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IpivcDnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_IpivcDnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
ipivcDnaDefaultRecvFrmNetworkThruputClass = _IpivcDnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 5),
    _IpivcDnaDefaultRecvFrmNetworkThruputClass_Type()
)
ipivcDnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _IpivcDnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type ipivcDnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IpivcDnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_IpivcDnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
ipivcDnaDefaultSendToNetworkThruputClass = _IpivcDnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 6),
    _IpivcDnaDefaultSendToNetworkThruputClass_Type()
)
ipivcDnaDefaultSendToNetworkThruputClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _IpivcDnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type ipivcDnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IpivcDnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_IpivcDnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
ipivcDnaDefaultRecvFrmNetworkWindowSize = _IpivcDnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 7),
    _IpivcDnaDefaultRecvFrmNetworkWindowSize_Type()
)
ipivcDnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _IpivcDnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type ipivcDnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IpivcDnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_IpivcDnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
ipivcDnaDefaultSendToNetworkWindowSize = _IpivcDnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 8),
    _IpivcDnaDefaultSendToNetworkWindowSize_Type()
)
ipivcDnaDefaultSendToNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _IpivcDnaPacketSizeNegotiation_Type(Integer32):
    """Custom type ipivcDnaPacketSizeNegotiation based on Integer32"""
    defaultValue = 1

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


_IpivcDnaPacketSizeNegotiation_Type.__name__ = "Integer32"
_IpivcDnaPacketSizeNegotiation_Object = MibTableColumn
ipivcDnaPacketSizeNegotiation = _IpivcDnaPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 9),
    _IpivcDnaPacketSizeNegotiation_Type()
)
ipivcDnaPacketSizeNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaPacketSizeNegotiation.setStatus("mandatory")


class _IpivcDnaAccountClass_Type(Unsigned32):
    """Custom type ipivcDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpivcDnaAccountClass_Type.__name__ = "Unsigned32"
_IpivcDnaAccountClass_Object = MibTableColumn
ipivcDnaAccountClass = _IpivcDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 10),
    _IpivcDnaAccountClass_Type()
)
ipivcDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaAccountClass.setStatus("mandatory")


class _IpivcDnaServiceExchange_Type(Unsigned32):
    """Custom type ipivcDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpivcDnaServiceExchange_Type.__name__ = "Unsigned32"
_IpivcDnaServiceExchange_Object = MibTableColumn
ipivcDnaServiceExchange = _IpivcDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 12),
    _IpivcDnaServiceExchange_Type()
)
ipivcDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDnaServiceExchange.setStatus("mandatory")


class _IpivcDnaCugFormat_Type(Integer32):
    """Custom type ipivcDnaCugFormat based on Integer32"""
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


_IpivcDnaCugFormat_Type.__name__ = "Integer32"
_IpivcDnaCugFormat_Object = MibTableColumn
ipivcDnaCugFormat = _IpivcDnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 13),
    _IpivcDnaCugFormat_Type()
)
ipivcDnaCugFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaCugFormat.setStatus("mandatory")


class _IpivcDnaCug0AsNonCugCall_Type(Integer32):
    """Custom type ipivcDnaCug0AsNonCugCall based on Integer32"""
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


_IpivcDnaCug0AsNonCugCall_Type.__name__ = "Integer32"
_IpivcDnaCug0AsNonCugCall_Object = MibTableColumn
ipivcDnaCug0AsNonCugCall = _IpivcDnaCug0AsNonCugCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 14),
    _IpivcDnaCug0AsNonCugCall_Type()
)
ipivcDnaCug0AsNonCugCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaCug0AsNonCugCall.setStatus("mandatory")


class _IpivcDnaFastSelectCallsOnly_Type(Integer32):
    """Custom type ipivcDnaFastSelectCallsOnly based on Integer32"""
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


_IpivcDnaFastSelectCallsOnly_Type.__name__ = "Integer32"
_IpivcDnaFastSelectCallsOnly_Object = MibTableColumn
ipivcDnaFastSelectCallsOnly = _IpivcDnaFastSelectCallsOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 2, 13, 1, 17),
    _IpivcDnaFastSelectCallsOnly_Type()
)
ipivcDnaFastSelectCallsOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDnaFastSelectCallsOnly.setStatus("mandatory")
_IpivcDr_ObjectIdentity = ObjectIdentity
ipivcDr = _IpivcDr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3)
)
_IpivcDrRowStatusTable_Object = MibTable
ipivcDrRowStatusTable = _IpivcDrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 1)
)
if mibBuilder.loadTexts:
    ipivcDrRowStatusTable.setStatus("mandatory")
_IpivcDrRowStatusEntry_Object = MibTableRow
ipivcDrRowStatusEntry = _IpivcDrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 1, 1)
)
ipivcDrRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDrIndex"),
)
if mibBuilder.loadTexts:
    ipivcDrRowStatusEntry.setStatus("mandatory")
_IpivcDrRowStatus_Type = RowStatus
_IpivcDrRowStatus_Object = MibTableColumn
ipivcDrRowStatus = _IpivcDrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 1, 1, 1),
    _IpivcDrRowStatus_Type()
)
ipivcDrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDrRowStatus.setStatus("mandatory")
_IpivcDrComponentName_Type = DisplayString
_IpivcDrComponentName_Object = MibTableColumn
ipivcDrComponentName = _IpivcDrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 1, 1, 2),
    _IpivcDrComponentName_Type()
)
ipivcDrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDrComponentName.setStatus("mandatory")
_IpivcDrStorageType_Type = StorageType
_IpivcDrStorageType_Object = MibTableColumn
ipivcDrStorageType = _IpivcDrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 1, 1, 4),
    _IpivcDrStorageType_Type()
)
ipivcDrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcDrStorageType.setStatus("mandatory")
_IpivcDrIndex_Type = NonReplicated
_IpivcDrIndex_Object = MibTableColumn
ipivcDrIndex = _IpivcDrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 1, 1, 10),
    _IpivcDrIndex_Type()
)
ipivcDrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipivcDrIndex.setStatus("mandatory")
_IpivcDrProvTable_Object = MibTable
ipivcDrProvTable = _IpivcDrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 10)
)
if mibBuilder.loadTexts:
    ipivcDrProvTable.setStatus("mandatory")
_IpivcDrProvEntry_Object = MibTableRow
ipivcDrProvEntry = _IpivcDrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 10, 1)
)
ipivcDrProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcDrIndex"),
)
if mibBuilder.loadTexts:
    ipivcDrProvEntry.setStatus("mandatory")


class _IpivcDrCallingIpAddress_Type(IpAddress):
    """Custom type ipivcDrCallingIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpivcDrCallingIpAddress_Object = MibTableColumn
ipivcDrCallingIpAddress = _IpivcDrCallingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 10, 1, 1),
    _IpivcDrCallingIpAddress_Type()
)
ipivcDrCallingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDrCallingIpAddress.setStatus("mandatory")


class _IpivcDrCallingNumberingPlanIndicator_Type(Integer32):
    """Custom type ipivcDrCallingNumberingPlanIndicator based on Integer32"""
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


_IpivcDrCallingNumberingPlanIndicator_Type.__name__ = "Integer32"
_IpivcDrCallingNumberingPlanIndicator_Object = MibTableColumn
ipivcDrCallingNumberingPlanIndicator = _IpivcDrCallingNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 10, 1, 2),
    _IpivcDrCallingNumberingPlanIndicator_Type()
)
ipivcDrCallingNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDrCallingNumberingPlanIndicator.setStatus("mandatory")


class _IpivcDrCallingDataNetworkAddress_Type(DigitString):
    """Custom type ipivcDrCallingDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpivcDrCallingDataNetworkAddress_Type.__name__ = "DigitString"
_IpivcDrCallingDataNetworkAddress_Object = MibTableColumn
ipivcDrCallingDataNetworkAddress = _IpivcDrCallingDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 3, 10, 1, 3),
    _IpivcDrCallingDataNetworkAddress_Type()
)
ipivcDrCallingDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcDrCallingDataNetworkAddress.setStatus("mandatory")
_IpivcLcn_ObjectIdentity = ObjectIdentity
ipivcLcn = _IpivcLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4)
)
_IpivcLcnRowStatusTable_Object = MibTable
ipivcLcnRowStatusTable = _IpivcLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 1)
)
if mibBuilder.loadTexts:
    ipivcLcnRowStatusTable.setStatus("mandatory")
_IpivcLcnRowStatusEntry_Object = MibTableRow
ipivcLcnRowStatusEntry = _IpivcLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 1, 1)
)
ipivcLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnIndex"),
)
if mibBuilder.loadTexts:
    ipivcLcnRowStatusEntry.setStatus("mandatory")
_IpivcLcnRowStatus_Type = RowStatus
_IpivcLcnRowStatus_Object = MibTableColumn
ipivcLcnRowStatus = _IpivcLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 1, 1, 1),
    _IpivcLcnRowStatus_Type()
)
ipivcLcnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnRowStatus.setStatus("mandatory")
_IpivcLcnComponentName_Type = DisplayString
_IpivcLcnComponentName_Object = MibTableColumn
ipivcLcnComponentName = _IpivcLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 1, 1, 2),
    _IpivcLcnComponentName_Type()
)
ipivcLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnComponentName.setStatus("mandatory")
_IpivcLcnStorageType_Type = StorageType
_IpivcLcnStorageType_Object = MibTableColumn
ipivcLcnStorageType = _IpivcLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 1, 1, 4),
    _IpivcLcnStorageType_Type()
)
ipivcLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnStorageType.setStatus("mandatory")


class _IpivcLcnIndex_Type(Integer32):
    """Custom type ipivcLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 39),
    )


_IpivcLcnIndex_Type.__name__ = "Integer32"
_IpivcLcnIndex_Object = MibTableColumn
ipivcLcnIndex = _IpivcLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 1, 1, 10),
    _IpivcLcnIndex_Type()
)
ipivcLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipivcLcnIndex.setStatus("mandatory")
_IpivcLcnVc_ObjectIdentity = ObjectIdentity
ipivcLcnVc = _IpivcLcnVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2)
)
_IpivcLcnVcRowStatusTable_Object = MibTable
ipivcLcnVcRowStatusTable = _IpivcLcnVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ipivcLcnVcRowStatusTable.setStatus("mandatory")
_IpivcLcnVcRowStatusEntry_Object = MibTableRow
ipivcLcnVcRowStatusEntry = _IpivcLcnVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 1, 1)
)
ipivcLcnVcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipivcLcnVcRowStatusEntry.setStatus("mandatory")
_IpivcLcnVcRowStatus_Type = RowStatus
_IpivcLcnVcRowStatus_Object = MibTableColumn
ipivcLcnVcRowStatus = _IpivcLcnVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 1, 1, 1),
    _IpivcLcnVcRowStatus_Type()
)
ipivcLcnVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcRowStatus.setStatus("mandatory")
_IpivcLcnVcComponentName_Type = DisplayString
_IpivcLcnVcComponentName_Object = MibTableColumn
ipivcLcnVcComponentName = _IpivcLcnVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 1, 1, 2),
    _IpivcLcnVcComponentName_Type()
)
ipivcLcnVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcComponentName.setStatus("mandatory")
_IpivcLcnVcStorageType_Type = StorageType
_IpivcLcnVcStorageType_Object = MibTableColumn
ipivcLcnVcStorageType = _IpivcLcnVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 1, 1, 4),
    _IpivcLcnVcStorageType_Type()
)
ipivcLcnVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcStorageType.setStatus("mandatory")
_IpivcLcnVcIndex_Type = NonReplicated
_IpivcLcnVcIndex_Object = MibTableColumn
ipivcLcnVcIndex = _IpivcLcnVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 1, 1, 10),
    _IpivcLcnVcIndex_Type()
)
ipivcLcnVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipivcLcnVcIndex.setStatus("mandatory")
_IpivcLcnVcCadTable_Object = MibTable
ipivcLcnVcCadTable = _IpivcLcnVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10)
)
if mibBuilder.loadTexts:
    ipivcLcnVcCadTable.setStatus("mandatory")
_IpivcLcnVcCadEntry_Object = MibTableRow
ipivcLcnVcCadEntry = _IpivcLcnVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1)
)
ipivcLcnVcCadEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipivcLcnVcCadEntry.setStatus("mandatory")


class _IpivcLcnVcType_Type(Integer32):
    """Custom type ipivcLcnVcType based on Integer32"""
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


_IpivcLcnVcType_Type.__name__ = "Integer32"
_IpivcLcnVcType_Object = MibTableColumn
ipivcLcnVcType = _IpivcLcnVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 1),
    _IpivcLcnVcType_Type()
)
ipivcLcnVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcType.setStatus("mandatory")


class _IpivcLcnVcState_Type(Integer32):
    """Custom type ipivcLcnVcState based on Integer32"""
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


_IpivcLcnVcState_Type.__name__ = "Integer32"
_IpivcLcnVcState_Object = MibTableColumn
ipivcLcnVcState = _IpivcLcnVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 2),
    _IpivcLcnVcState_Type()
)
ipivcLcnVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcState.setStatus("mandatory")


class _IpivcLcnVcPreviousState_Type(Integer32):
    """Custom type ipivcLcnVcPreviousState based on Integer32"""
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


_IpivcLcnVcPreviousState_Type.__name__ = "Integer32"
_IpivcLcnVcPreviousState_Object = MibTableColumn
ipivcLcnVcPreviousState = _IpivcLcnVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 3),
    _IpivcLcnVcPreviousState_Type()
)
ipivcLcnVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPreviousState.setStatus("mandatory")


class _IpivcLcnVcDiagnosticCode_Type(Unsigned32):
    """Custom type ipivcLcnVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpivcLcnVcDiagnosticCode_Type.__name__ = "Unsigned32"
_IpivcLcnVcDiagnosticCode_Object = MibTableColumn
ipivcLcnVcDiagnosticCode = _IpivcLcnVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 4),
    _IpivcLcnVcDiagnosticCode_Type()
)
ipivcLcnVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcDiagnosticCode.setStatus("mandatory")


class _IpivcLcnVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type ipivcLcnVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpivcLcnVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_IpivcLcnVcPreviousDiagnosticCode_Object = MibTableColumn
ipivcLcnVcPreviousDiagnosticCode = _IpivcLcnVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 5),
    _IpivcLcnVcPreviousDiagnosticCode_Type()
)
ipivcLcnVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPreviousDiagnosticCode.setStatus("mandatory")


class _IpivcLcnVcCalledNpi_Type(Integer32):
    """Custom type ipivcLcnVcCalledNpi based on Integer32"""
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


_IpivcLcnVcCalledNpi_Type.__name__ = "Integer32"
_IpivcLcnVcCalledNpi_Object = MibTableColumn
ipivcLcnVcCalledNpi = _IpivcLcnVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 6),
    _IpivcLcnVcCalledNpi_Type()
)
ipivcLcnVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcCalledNpi.setStatus("mandatory")


class _IpivcLcnVcCalledDna_Type(DigitString):
    """Custom type ipivcLcnVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpivcLcnVcCalledDna_Type.__name__ = "DigitString"
_IpivcLcnVcCalledDna_Object = MibTableColumn
ipivcLcnVcCalledDna = _IpivcLcnVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 7),
    _IpivcLcnVcCalledDna_Type()
)
ipivcLcnVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcCalledDna.setStatus("mandatory")


class _IpivcLcnVcCalledLcn_Type(Unsigned32):
    """Custom type ipivcLcnVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpivcLcnVcCalledLcn_Type.__name__ = "Unsigned32"
_IpivcLcnVcCalledLcn_Object = MibTableColumn
ipivcLcnVcCalledLcn = _IpivcLcnVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 8),
    _IpivcLcnVcCalledLcn_Type()
)
ipivcLcnVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcCalledLcn.setStatus("mandatory")


class _IpivcLcnVcCallingNpi_Type(Integer32):
    """Custom type ipivcLcnVcCallingNpi based on Integer32"""
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


_IpivcLcnVcCallingNpi_Type.__name__ = "Integer32"
_IpivcLcnVcCallingNpi_Object = MibTableColumn
ipivcLcnVcCallingNpi = _IpivcLcnVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 9),
    _IpivcLcnVcCallingNpi_Type()
)
ipivcLcnVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcCallingNpi.setStatus("mandatory")


class _IpivcLcnVcCallingDna_Type(DigitString):
    """Custom type ipivcLcnVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_IpivcLcnVcCallingDna_Type.__name__ = "DigitString"
_IpivcLcnVcCallingDna_Object = MibTableColumn
ipivcLcnVcCallingDna = _IpivcLcnVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 10),
    _IpivcLcnVcCallingDna_Type()
)
ipivcLcnVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcCallingDna.setStatus("mandatory")


class _IpivcLcnVcCallingLcn_Type(Unsigned32):
    """Custom type ipivcLcnVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpivcLcnVcCallingLcn_Type.__name__ = "Unsigned32"
_IpivcLcnVcCallingLcn_Object = MibTableColumn
ipivcLcnVcCallingLcn = _IpivcLcnVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 11),
    _IpivcLcnVcCallingLcn_Type()
)
ipivcLcnVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcCallingLcn.setStatus("mandatory")


class _IpivcLcnVcAccountingEnabled_Type(Integer32):
    """Custom type ipivcLcnVcAccountingEnabled based on Integer32"""
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


_IpivcLcnVcAccountingEnabled_Type.__name__ = "Integer32"
_IpivcLcnVcAccountingEnabled_Object = MibTableColumn
ipivcLcnVcAccountingEnabled = _IpivcLcnVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 12),
    _IpivcLcnVcAccountingEnabled_Type()
)
ipivcLcnVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcAccountingEnabled.setStatus("mandatory")


class _IpivcLcnVcFastSelectCall_Type(Integer32):
    """Custom type ipivcLcnVcFastSelectCall based on Integer32"""
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


_IpivcLcnVcFastSelectCall_Type.__name__ = "Integer32"
_IpivcLcnVcFastSelectCall_Object = MibTableColumn
ipivcLcnVcFastSelectCall = _IpivcLcnVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 13),
    _IpivcLcnVcFastSelectCall_Type()
)
ipivcLcnVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcFastSelectCall.setStatus("mandatory")


class _IpivcLcnVcLocalRxPktSize_Type(Integer32):
    """Custom type ipivcLcnVcLocalRxPktSize based on Integer32"""
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


_IpivcLcnVcLocalRxPktSize_Type.__name__ = "Integer32"
_IpivcLcnVcLocalRxPktSize_Object = MibTableColumn
ipivcLcnVcLocalRxPktSize = _IpivcLcnVcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 14),
    _IpivcLcnVcLocalRxPktSize_Type()
)
ipivcLcnVcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcLocalRxPktSize.setStatus("mandatory")


class _IpivcLcnVcLocalTxPktSize_Type(Integer32):
    """Custom type ipivcLcnVcLocalTxPktSize based on Integer32"""
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


_IpivcLcnVcLocalTxPktSize_Type.__name__ = "Integer32"
_IpivcLcnVcLocalTxPktSize_Object = MibTableColumn
ipivcLcnVcLocalTxPktSize = _IpivcLcnVcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 15),
    _IpivcLcnVcLocalTxPktSize_Type()
)
ipivcLcnVcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcLocalTxPktSize.setStatus("mandatory")


class _IpivcLcnVcLocalTxWindowSize_Type(Unsigned32):
    """Custom type ipivcLcnVcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_IpivcLcnVcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcLocalTxWindowSize_Object = MibTableColumn
ipivcLcnVcLocalTxWindowSize = _IpivcLcnVcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 16),
    _IpivcLcnVcLocalTxWindowSize_Type()
)
ipivcLcnVcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcLocalTxWindowSize.setStatus("mandatory")


class _IpivcLcnVcLocalRxWindowSize_Type(Unsigned32):
    """Custom type ipivcLcnVcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_IpivcLcnVcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcLocalRxWindowSize_Object = MibTableColumn
ipivcLcnVcLocalRxWindowSize = _IpivcLcnVcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 17),
    _IpivcLcnVcLocalRxWindowSize_Type()
)
ipivcLcnVcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcLocalRxWindowSize.setStatus("mandatory")


class _IpivcLcnVcPathReliability_Type(Integer32):
    """Custom type ipivcLcnVcPathReliability based on Integer32"""
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


_IpivcLcnVcPathReliability_Type.__name__ = "Integer32"
_IpivcLcnVcPathReliability_Object = MibTableColumn
ipivcLcnVcPathReliability = _IpivcLcnVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 19),
    _IpivcLcnVcPathReliability_Type()
)
ipivcLcnVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPathReliability.setStatus("mandatory")


class _IpivcLcnVcAccountingEnd_Type(Integer32):
    """Custom type ipivcLcnVcAccountingEnd based on Integer32"""
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


_IpivcLcnVcAccountingEnd_Type.__name__ = "Integer32"
_IpivcLcnVcAccountingEnd_Object = MibTableColumn
ipivcLcnVcAccountingEnd = _IpivcLcnVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 20),
    _IpivcLcnVcAccountingEnd_Type()
)
ipivcLcnVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcAccountingEnd.setStatus("mandatory")


class _IpivcLcnVcPriority_Type(Integer32):
    """Custom type ipivcLcnVcPriority based on Integer32"""
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


_IpivcLcnVcPriority_Type.__name__ = "Integer32"
_IpivcLcnVcPriority_Object = MibTableColumn
ipivcLcnVcPriority = _IpivcLcnVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 21),
    _IpivcLcnVcPriority_Type()
)
ipivcLcnVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPriority.setStatus("mandatory")


class _IpivcLcnVcSegmentSize_Type(Unsigned32):
    """Custom type ipivcLcnVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_IpivcLcnVcSegmentSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcSegmentSize_Object = MibTableColumn
ipivcLcnVcSegmentSize = _IpivcLcnVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 22),
    _IpivcLcnVcSegmentSize_Type()
)
ipivcLcnVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSegmentSize.setStatus("mandatory")


class _IpivcLcnVcSubnetTxPktSize_Type(Integer32):
    """Custom type ipivcLcnVcSubnetTxPktSize based on Integer32"""
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


_IpivcLcnVcSubnetTxPktSize_Type.__name__ = "Integer32"
_IpivcLcnVcSubnetTxPktSize_Object = MibTableColumn
ipivcLcnVcSubnetTxPktSize = _IpivcLcnVcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 23),
    _IpivcLcnVcSubnetTxPktSize_Type()
)
ipivcLcnVcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSubnetTxPktSize.setStatus("mandatory")


class _IpivcLcnVcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type ipivcLcnVcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_IpivcLcnVcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcSubnetTxWindowSize_Object = MibTableColumn
ipivcLcnVcSubnetTxWindowSize = _IpivcLcnVcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 24),
    _IpivcLcnVcSubnetTxWindowSize_Type()
)
ipivcLcnVcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSubnetTxWindowSize.setStatus("mandatory")


class _IpivcLcnVcSubnetRxPktSize_Type(Integer32):
    """Custom type ipivcLcnVcSubnetRxPktSize based on Integer32"""
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


_IpivcLcnVcSubnetRxPktSize_Type.__name__ = "Integer32"
_IpivcLcnVcSubnetRxPktSize_Object = MibTableColumn
ipivcLcnVcSubnetRxPktSize = _IpivcLcnVcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 25),
    _IpivcLcnVcSubnetRxPktSize_Type()
)
ipivcLcnVcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSubnetRxPktSize.setStatus("mandatory")


class _IpivcLcnVcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type ipivcLcnVcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_IpivcLcnVcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcSubnetRxWindowSize_Object = MibTableColumn
ipivcLcnVcSubnetRxWindowSize = _IpivcLcnVcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 26),
    _IpivcLcnVcSubnetRxWindowSize_Type()
)
ipivcLcnVcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSubnetRxWindowSize.setStatus("mandatory")


class _IpivcLcnVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type ipivcLcnVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_IpivcLcnVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcMaxSubnetPktSize_Object = MibTableColumn
ipivcLcnVcMaxSubnetPktSize = _IpivcLcnVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 27),
    _IpivcLcnVcMaxSubnetPktSize_Type()
)
ipivcLcnVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcMaxSubnetPktSize.setStatus("mandatory")


class _IpivcLcnVcTransferPriorityToNetwork_Type(Integer32):
    """Custom type ipivcLcnVcTransferPriorityToNetwork based on Integer32"""
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


_IpivcLcnVcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_IpivcLcnVcTransferPriorityToNetwork_Object = MibTableColumn
ipivcLcnVcTransferPriorityToNetwork = _IpivcLcnVcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 28),
    _IpivcLcnVcTransferPriorityToNetwork_Type()
)
ipivcLcnVcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcTransferPriorityToNetwork.setStatus("mandatory")


class _IpivcLcnVcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type ipivcLcnVcTransferPriorityFromNetwork based on Integer32"""
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


_IpivcLcnVcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_IpivcLcnVcTransferPriorityFromNetwork_Object = MibTableColumn
ipivcLcnVcTransferPriorityFromNetwork = _IpivcLcnVcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 10, 1, 29),
    _IpivcLcnVcTransferPriorityFromNetwork_Type()
)
ipivcLcnVcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcTransferPriorityFromNetwork.setStatus("mandatory")
_IpivcLcnVcIntdTable_Object = MibTable
ipivcLcnVcIntdTable = _IpivcLcnVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 11)
)
if mibBuilder.loadTexts:
    ipivcLcnVcIntdTable.setStatus("mandatory")
_IpivcLcnVcIntdEntry_Object = MibTableRow
ipivcLcnVcIntdEntry = _IpivcLcnVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 11, 1)
)
ipivcLcnVcIntdEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipivcLcnVcIntdEntry.setStatus("mandatory")


class _IpivcLcnVcCallReferenceNumber_Type(Hex):
    """Custom type ipivcLcnVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpivcLcnVcCallReferenceNumber_Type.__name__ = "Hex"
_IpivcLcnVcCallReferenceNumber_Object = MibTableColumn
ipivcLcnVcCallReferenceNumber = _IpivcLcnVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 11, 1, 1),
    _IpivcLcnVcCallReferenceNumber_Type()
)
ipivcLcnVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcCallReferenceNumber.setStatus("mandatory")


class _IpivcLcnVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type ipivcLcnVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpivcLcnVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_IpivcLcnVcElapsedTimeTillNow_Object = MibTableColumn
ipivcLcnVcElapsedTimeTillNow = _IpivcLcnVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 11, 1, 2),
    _IpivcLcnVcElapsedTimeTillNow_Type()
)
ipivcLcnVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcElapsedTimeTillNow.setStatus("mandatory")


class _IpivcLcnVcSegmentsRx_Type(Unsigned32):
    """Custom type ipivcLcnVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpivcLcnVcSegmentsRx_Type.__name__ = "Unsigned32"
_IpivcLcnVcSegmentsRx_Object = MibTableColumn
ipivcLcnVcSegmentsRx = _IpivcLcnVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 11, 1, 3),
    _IpivcLcnVcSegmentsRx_Type()
)
ipivcLcnVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSegmentsRx.setStatus("mandatory")


class _IpivcLcnVcSegmentsSent_Type(Unsigned32):
    """Custom type ipivcLcnVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_IpivcLcnVcSegmentsSent_Type.__name__ = "Unsigned32"
_IpivcLcnVcSegmentsSent_Object = MibTableColumn
ipivcLcnVcSegmentsSent = _IpivcLcnVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 11, 1, 4),
    _IpivcLcnVcSegmentsSent_Type()
)
ipivcLcnVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSegmentsSent.setStatus("mandatory")


class _IpivcLcnVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type ipivcLcnVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_IpivcLcnVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_IpivcLcnVcStartTime_Object = MibTableColumn
ipivcLcnVcStartTime = _IpivcLcnVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 11, 1, 5),
    _IpivcLcnVcStartTime_Type()
)
ipivcLcnVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcStartTime.setStatus("mandatory")
_IpivcLcnVcStatsTable_Object = MibTable
ipivcLcnVcStatsTable = _IpivcLcnVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12)
)
if mibBuilder.loadTexts:
    ipivcLcnVcStatsTable.setStatus("mandatory")
_IpivcLcnVcStatsEntry_Object = MibTableRow
ipivcLcnVcStatsEntry = _IpivcLcnVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1)
)
ipivcLcnVcStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    ipivcLcnVcStatsEntry.setStatus("mandatory")


class _IpivcLcnVcAckStackingTimeouts_Type(Unsigned32):
    """Custom type ipivcLcnVcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_IpivcLcnVcAckStackingTimeouts_Object = MibTableColumn
ipivcLcnVcAckStackingTimeouts = _IpivcLcnVcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 1),
    _IpivcLcnVcAckStackingTimeouts_Type()
)
ipivcLcnVcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcAckStackingTimeouts.setStatus("mandatory")


class _IpivcLcnVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type ipivcLcnVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_IpivcLcnVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
ipivcLcnVcOutOfRangeFrmFromSubnet = _IpivcLcnVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 2),
    _IpivcLcnVcOutOfRangeFrmFromSubnet_Type()
)
ipivcLcnVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _IpivcLcnVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type ipivcLcnVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_IpivcLcnVcDuplicatesFromSubnet_Object = MibTableColumn
ipivcLcnVcDuplicatesFromSubnet = _IpivcLcnVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 3),
    _IpivcLcnVcDuplicatesFromSubnet_Type()
)
ipivcLcnVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcDuplicatesFromSubnet.setStatus("mandatory")


class _IpivcLcnVcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type ipivcLcnVcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_IpivcLcnVcFrmRetryTimeouts_Object = MibTableColumn
ipivcLcnVcFrmRetryTimeouts = _IpivcLcnVcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 4),
    _IpivcLcnVcFrmRetryTimeouts_Type()
)
ipivcLcnVcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcFrmRetryTimeouts.setStatus("mandatory")


class _IpivcLcnVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type ipivcLcnVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcPeakRetryQueueSize_Object = MibTableColumn
ipivcLcnVcPeakRetryQueueSize = _IpivcLcnVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 5),
    _IpivcLcnVcPeakRetryQueueSize_Type()
)
ipivcLcnVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPeakRetryQueueSize.setStatus("mandatory")


class _IpivcLcnVcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type ipivcLcnVcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_IpivcLcnVcPeakOoSeqQueueSize_Object = MibTableColumn
ipivcLcnVcPeakOoSeqQueueSize = _IpivcLcnVcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 6),
    _IpivcLcnVcPeakOoSeqQueueSize_Type()
)
ipivcLcnVcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPeakOoSeqQueueSize.setStatus("mandatory")


class _IpivcLcnVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type ipivcLcnVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_IpivcLcnVcPeakOoSeqFrmForwarded_Object = MibTableColumn
ipivcLcnVcPeakOoSeqFrmForwarded = _IpivcLcnVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 7),
    _IpivcLcnVcPeakOoSeqFrmForwarded_Type()
)
ipivcLcnVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _IpivcLcnVcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type ipivcLcnVcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_IpivcLcnVcPeakStackedAcksRx_Object = MibTableColumn
ipivcLcnVcPeakStackedAcksRx = _IpivcLcnVcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 8),
    _IpivcLcnVcPeakStackedAcksRx_Type()
)
ipivcLcnVcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcPeakStackedAcksRx.setStatus("mandatory")


class _IpivcLcnVcSubnetRecoveries_Type(Unsigned32):
    """Custom type ipivcLcnVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_IpivcLcnVcSubnetRecoveries_Object = MibTableColumn
ipivcLcnVcSubnetRecoveries = _IpivcLcnVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 9),
    _IpivcLcnVcSubnetRecoveries_Type()
)
ipivcLcnVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcSubnetRecoveries.setStatus("mandatory")


class _IpivcLcnVcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type ipivcLcnVcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_IpivcLcnVcWindowClosuresToSubnet_Object = MibTableColumn
ipivcLcnVcWindowClosuresToSubnet = _IpivcLcnVcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 10),
    _IpivcLcnVcWindowClosuresToSubnet_Type()
)
ipivcLcnVcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcWindowClosuresToSubnet.setStatus("mandatory")


class _IpivcLcnVcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type ipivcLcnVcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_IpivcLcnVcWindowClosuresFromSubnet_Object = MibTableColumn
ipivcLcnVcWindowClosuresFromSubnet = _IpivcLcnVcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 11),
    _IpivcLcnVcWindowClosuresFromSubnet_Type()
)
ipivcLcnVcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcWindowClosuresFromSubnet.setStatus("mandatory")


class _IpivcLcnVcWrTriggers_Type(Unsigned32):
    """Custom type ipivcLcnVcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_IpivcLcnVcWrTriggers_Type.__name__ = "Unsigned32"
_IpivcLcnVcWrTriggers_Object = MibTableColumn
ipivcLcnVcWrTriggers = _IpivcLcnVcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 2, 12, 1, 12),
    _IpivcLcnVcWrTriggers_Type()
)
ipivcLcnVcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnVcWrTriggers.setStatus("mandatory")
_IpivcLcnStateTable_Object = MibTable
ipivcLcnStateTable = _IpivcLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10)
)
if mibBuilder.loadTexts:
    ipivcLcnStateTable.setStatus("mandatory")
_IpivcLcnStateEntry_Object = MibTableRow
ipivcLcnStateEntry = _IpivcLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1)
)
ipivcLcnStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnIndex"),
)
if mibBuilder.loadTexts:
    ipivcLcnStateEntry.setStatus("mandatory")


class _IpivcLcnAdminState_Type(Integer32):
    """Custom type ipivcLcnAdminState based on Integer32"""
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


_IpivcLcnAdminState_Type.__name__ = "Integer32"
_IpivcLcnAdminState_Object = MibTableColumn
ipivcLcnAdminState = _IpivcLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 1),
    _IpivcLcnAdminState_Type()
)
ipivcLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnAdminState.setStatus("mandatory")


class _IpivcLcnOperationalState_Type(Integer32):
    """Custom type ipivcLcnOperationalState based on Integer32"""
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


_IpivcLcnOperationalState_Type.__name__ = "Integer32"
_IpivcLcnOperationalState_Object = MibTableColumn
ipivcLcnOperationalState = _IpivcLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 2),
    _IpivcLcnOperationalState_Type()
)
ipivcLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnOperationalState.setStatus("mandatory")


class _IpivcLcnUsageState_Type(Integer32):
    """Custom type ipivcLcnUsageState based on Integer32"""
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


_IpivcLcnUsageState_Type.__name__ = "Integer32"
_IpivcLcnUsageState_Object = MibTableColumn
ipivcLcnUsageState = _IpivcLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 3),
    _IpivcLcnUsageState_Type()
)
ipivcLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnUsageState.setStatus("mandatory")


class _IpivcLcnAvailabilityStatus_Type(OctetString):
    """Custom type ipivcLcnAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpivcLcnAvailabilityStatus_Type.__name__ = "OctetString"
_IpivcLcnAvailabilityStatus_Object = MibTableColumn
ipivcLcnAvailabilityStatus = _IpivcLcnAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 4),
    _IpivcLcnAvailabilityStatus_Type()
)
ipivcLcnAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnAvailabilityStatus.setStatus("mandatory")


class _IpivcLcnProceduralStatus_Type(OctetString):
    """Custom type ipivcLcnProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IpivcLcnProceduralStatus_Type.__name__ = "OctetString"
_IpivcLcnProceduralStatus_Object = MibTableColumn
ipivcLcnProceduralStatus = _IpivcLcnProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 5),
    _IpivcLcnProceduralStatus_Type()
)
ipivcLcnProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnProceduralStatus.setStatus("mandatory")


class _IpivcLcnControlStatus_Type(OctetString):
    """Custom type ipivcLcnControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IpivcLcnControlStatus_Type.__name__ = "OctetString"
_IpivcLcnControlStatus_Object = MibTableColumn
ipivcLcnControlStatus = _IpivcLcnControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 6),
    _IpivcLcnControlStatus_Type()
)
ipivcLcnControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnControlStatus.setStatus("mandatory")


class _IpivcLcnAlarmStatus_Type(OctetString):
    """Custom type ipivcLcnAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IpivcLcnAlarmStatus_Type.__name__ = "OctetString"
_IpivcLcnAlarmStatus_Object = MibTableColumn
ipivcLcnAlarmStatus = _IpivcLcnAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 7),
    _IpivcLcnAlarmStatus_Type()
)
ipivcLcnAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnAlarmStatus.setStatus("mandatory")


class _IpivcLcnStandbyStatus_Type(Integer32):
    """Custom type ipivcLcnStandbyStatus based on Integer32"""
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


_IpivcLcnStandbyStatus_Type.__name__ = "Integer32"
_IpivcLcnStandbyStatus_Object = MibTableColumn
ipivcLcnStandbyStatus = _IpivcLcnStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 8),
    _IpivcLcnStandbyStatus_Type()
)
ipivcLcnStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnStandbyStatus.setStatus("mandatory")


class _IpivcLcnUnknownStatus_Type(Integer32):
    """Custom type ipivcLcnUnknownStatus based on Integer32"""
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


_IpivcLcnUnknownStatus_Type.__name__ = "Integer32"
_IpivcLcnUnknownStatus_Object = MibTableColumn
ipivcLcnUnknownStatus = _IpivcLcnUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 10, 1, 9),
    _IpivcLcnUnknownStatus_Type()
)
ipivcLcnUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnUnknownStatus.setStatus("mandatory")
_IpivcLcnOperTable_Object = MibTable
ipivcLcnOperTable = _IpivcLcnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11)
)
if mibBuilder.loadTexts:
    ipivcLcnOperTable.setStatus("mandatory")
_IpivcLcnOperEntry_Object = MibTableRow
ipivcLcnOperEntry = _IpivcLcnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11, 1)
)
ipivcLcnOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcLcnIndex"),
)
if mibBuilder.loadTexts:
    ipivcLcnOperEntry.setStatus("mandatory")


class _IpivcLcnIpInterfaceDevice_Type(Integer32):
    """Custom type ipivcLcnIpInterfaceDevice based on Integer32"""
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


_IpivcLcnIpInterfaceDevice_Type.__name__ = "Integer32"
_IpivcLcnIpInterfaceDevice_Object = MibTableColumn
ipivcLcnIpInterfaceDevice = _IpivcLcnIpInterfaceDevice_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11, 1, 1),
    _IpivcLcnIpInterfaceDevice_Type()
)
ipivcLcnIpInterfaceDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnIpInterfaceDevice.setStatus("mandatory")


class _IpivcLcnDestinationIpAddress_Type(IpAddress):
    """Custom type ipivcLcnDestinationIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpivcLcnDestinationIpAddress_Object = MibTableColumn
ipivcLcnDestinationIpAddress = _IpivcLcnDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11, 1, 2),
    _IpivcLcnDestinationIpAddress_Type()
)
ipivcLcnDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnDestinationIpAddress.setStatus("mandatory")
_IpivcLcnPacketsSent_Type = Counter32
_IpivcLcnPacketsSent_Object = MibTableColumn
ipivcLcnPacketsSent = _IpivcLcnPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11, 1, 3),
    _IpivcLcnPacketsSent_Type()
)
ipivcLcnPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnPacketsSent.setStatus("mandatory")
_IpivcLcnPacketsReceived_Type = Counter32
_IpivcLcnPacketsReceived_Object = MibTableColumn
ipivcLcnPacketsReceived = _IpivcLcnPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11, 1, 4),
    _IpivcLcnPacketsReceived_Type()
)
ipivcLcnPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnPacketsReceived.setStatus("mandatory")
_IpivcLcnDiscardTxPackets_Type = Counter32
_IpivcLcnDiscardTxPackets_Object = MibTableColumn
ipivcLcnDiscardTxPackets = _IpivcLcnDiscardTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11, 1, 5),
    _IpivcLcnDiscardTxPackets_Type()
)
ipivcLcnDiscardTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnDiscardTxPackets.setStatus("mandatory")
_IpivcLcnDiscardRcvPackets_Type = Counter32
_IpivcLcnDiscardRcvPackets_Object = MibTableColumn
ipivcLcnDiscardRcvPackets = _IpivcLcnDiscardRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 4, 11, 1, 6),
    _IpivcLcnDiscardRcvPackets_Type()
)
ipivcLcnDiscardRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcLcnDiscardRcvPackets.setStatus("mandatory")
_IpivcProvTable_Object = MibTable
ipivcProvTable = _IpivcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 10)
)
if mibBuilder.loadTexts:
    ipivcProvTable.setStatus("mandatory")
_IpivcProvEntry_Object = MibTableRow
ipivcProvEntry = _IpivcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 10, 1)
)
ipivcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-IpiVcMIB", "ipivcIndex"),
)
if mibBuilder.loadTexts:
    ipivcProvEntry.setStatus("mandatory")


class _IpivcIpAddress_Type(IpAddress):
    """Custom type ipivcIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpivcIpAddress_Object = MibTableColumn
ipivcIpAddress = _IpivcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 10, 1, 1),
    _IpivcIpAddress_Type()
)
ipivcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipivcIpAddress.setStatus("mandatory")


class _IpivcMaximumNumberOfLcn_Type(Unsigned32):
    """Custom type ipivcMaximumNumberOfLcn based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 24),
    )


_IpivcMaximumNumberOfLcn_Type.__name__ = "Unsigned32"
_IpivcMaximumNumberOfLcn_Object = MibTableColumn
ipivcMaximumNumberOfLcn = _IpivcMaximumNumberOfLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 51, 10, 1, 2),
    _IpivcMaximumNumberOfLcn_Type()
)
ipivcMaximumNumberOfLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipivcMaximumNumberOfLcn.setStatus("mandatory")
_IpiVcMIB_ObjectIdentity = ObjectIdentity
ipiVcMIB = _IpiVcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53)
)
_IpiVcGroup_ObjectIdentity = ObjectIdentity
ipiVcGroup = _IpiVcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 1)
)
_IpiVcGroupBE_ObjectIdentity = ObjectIdentity
ipiVcGroupBE = _IpiVcGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 1, 5)
)
_IpiVcGroupBE01_ObjectIdentity = ObjectIdentity
ipiVcGroupBE01 = _IpiVcGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 1, 5, 2)
)
_IpiVcGroupBE01A_ObjectIdentity = ObjectIdentity
ipiVcGroupBE01A = _IpiVcGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 1, 5, 2, 2)
)
_IpiVcCapabilities_ObjectIdentity = ObjectIdentity
ipiVcCapabilities = _IpiVcCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 3)
)
_IpiVcCapabilitiesBE_ObjectIdentity = ObjectIdentity
ipiVcCapabilitiesBE = _IpiVcCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 3, 5)
)
_IpiVcCapabilitiesBE01_ObjectIdentity = ObjectIdentity
ipiVcCapabilitiesBE01 = _IpiVcCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 3, 5, 2)
)
_IpiVcCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
ipiVcCapabilitiesBE01A = _IpiVcCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 53, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-IpiVcMIB",
    **{"ipivc": ipivc,
       "ipivcRowStatusTable": ipivcRowStatusTable,
       "ipivcRowStatusEntry": ipivcRowStatusEntry,
       "ipivcRowStatus": ipivcRowStatus,
       "ipivcComponentName": ipivcComponentName,
       "ipivcStorageType": ipivcStorageType,
       "ipivcIndex": ipivcIndex,
       "ipivcDna": ipivcDna,
       "ipivcDnaRowStatusTable": ipivcDnaRowStatusTable,
       "ipivcDnaRowStatusEntry": ipivcDnaRowStatusEntry,
       "ipivcDnaRowStatus": ipivcDnaRowStatus,
       "ipivcDnaComponentName": ipivcDnaComponentName,
       "ipivcDnaStorageType": ipivcDnaStorageType,
       "ipivcDnaIndex": ipivcDnaIndex,
       "ipivcDnaCug": ipivcDnaCug,
       "ipivcDnaCugRowStatusTable": ipivcDnaCugRowStatusTable,
       "ipivcDnaCugRowStatusEntry": ipivcDnaCugRowStatusEntry,
       "ipivcDnaCugRowStatus": ipivcDnaCugRowStatus,
       "ipivcDnaCugComponentName": ipivcDnaCugComponentName,
       "ipivcDnaCugStorageType": ipivcDnaCugStorageType,
       "ipivcDnaCugIndex": ipivcDnaCugIndex,
       "ipivcDnaCugCugOptionsTable": ipivcDnaCugCugOptionsTable,
       "ipivcDnaCugCugOptionsEntry": ipivcDnaCugCugOptionsEntry,
       "ipivcDnaCugType": ipivcDnaCugType,
       "ipivcDnaCugDnic": ipivcDnaCugDnic,
       "ipivcDnaCugInterlockCode": ipivcDnaCugInterlockCode,
       "ipivcDnaCugOutCalls": ipivcDnaCugOutCalls,
       "ipivcDnaCugIncCalls": ipivcDnaCugIncCalls,
       "ipivcDnaCugPrivileged": ipivcDnaCugPrivileged,
       "ipivcDnaAddressTable": ipivcDnaAddressTable,
       "ipivcDnaAddressEntry": ipivcDnaAddressEntry,
       "ipivcDnaNumberingPlanIndicator": ipivcDnaNumberingPlanIndicator,
       "ipivcDnaDataNetworkAddress": ipivcDnaDataNetworkAddress,
       "ipivcDnaOutgoingOptionsTable": ipivcDnaOutgoingOptionsTable,
       "ipivcDnaOutgoingOptionsEntry": ipivcDnaOutgoingOptionsEntry,
       "ipivcDnaOutCalls": ipivcDnaOutCalls,
       "ipivcDnaOutDefaultPathSensitivity": ipivcDnaOutDefaultPathSensitivity,
       "ipivcDnaOutPathSensitivityOverRide": ipivcDnaOutPathSensitivityOverRide,
       "ipivcDnaDefaultTransferPriority": ipivcDnaDefaultTransferPriority,
       "ipivcDnaTransferPriorityOverRide": ipivcDnaTransferPriorityOverRide,
       "ipivcDnaIncomingOptionsTable": ipivcDnaIncomingOptionsTable,
       "ipivcDnaIncomingOptionsEntry": ipivcDnaIncomingOptionsEntry,
       "ipivcDnaIncCalls": ipivcDnaIncCalls,
       "ipivcDnaIncHighPriorityReverseCharge": ipivcDnaIncHighPriorityReverseCharge,
       "ipivcDnaIncNormalPriorityReverseCharge": ipivcDnaIncNormalPriorityReverseCharge,
       "ipivcDnaIncIntlNormalCharge": ipivcDnaIncIntlNormalCharge,
       "ipivcDnaIncIntlReverseCharge": ipivcDnaIncIntlReverseCharge,
       "ipivcDnaIncFastSelect": ipivcDnaIncFastSelect,
       "ipivcDnaIncSameService": ipivcDnaIncSameService,
       "ipivcDnaIncChargeTransfer": ipivcDnaIncChargeTransfer,
       "ipivcDnaIncAccess": ipivcDnaIncAccess,
       "ipivcDnaCallOptionsTable": ipivcDnaCallOptionsTable,
       "ipivcDnaCallOptionsEntry": ipivcDnaCallOptionsEntry,
       "ipivcDnaServiceCategory": ipivcDnaServiceCategory,
       "ipivcDnaPacketSizes": ipivcDnaPacketSizes,
       "ipivcDnaDefaultRecvFrmNetworkPacketSize": ipivcDnaDefaultRecvFrmNetworkPacketSize,
       "ipivcDnaDefaultSendToNetworkPacketSize": ipivcDnaDefaultSendToNetworkPacketSize,
       "ipivcDnaDefaultRecvFrmNetworkThruputClass": ipivcDnaDefaultRecvFrmNetworkThruputClass,
       "ipivcDnaDefaultSendToNetworkThruputClass": ipivcDnaDefaultSendToNetworkThruputClass,
       "ipivcDnaDefaultRecvFrmNetworkWindowSize": ipivcDnaDefaultRecvFrmNetworkWindowSize,
       "ipivcDnaDefaultSendToNetworkWindowSize": ipivcDnaDefaultSendToNetworkWindowSize,
       "ipivcDnaPacketSizeNegotiation": ipivcDnaPacketSizeNegotiation,
       "ipivcDnaAccountClass": ipivcDnaAccountClass,
       "ipivcDnaServiceExchange": ipivcDnaServiceExchange,
       "ipivcDnaCugFormat": ipivcDnaCugFormat,
       "ipivcDnaCug0AsNonCugCall": ipivcDnaCug0AsNonCugCall,
       "ipivcDnaFastSelectCallsOnly": ipivcDnaFastSelectCallsOnly,
       "ipivcDr": ipivcDr,
       "ipivcDrRowStatusTable": ipivcDrRowStatusTable,
       "ipivcDrRowStatusEntry": ipivcDrRowStatusEntry,
       "ipivcDrRowStatus": ipivcDrRowStatus,
       "ipivcDrComponentName": ipivcDrComponentName,
       "ipivcDrStorageType": ipivcDrStorageType,
       "ipivcDrIndex": ipivcDrIndex,
       "ipivcDrProvTable": ipivcDrProvTable,
       "ipivcDrProvEntry": ipivcDrProvEntry,
       "ipivcDrCallingIpAddress": ipivcDrCallingIpAddress,
       "ipivcDrCallingNumberingPlanIndicator": ipivcDrCallingNumberingPlanIndicator,
       "ipivcDrCallingDataNetworkAddress": ipivcDrCallingDataNetworkAddress,
       "ipivcLcn": ipivcLcn,
       "ipivcLcnRowStatusTable": ipivcLcnRowStatusTable,
       "ipivcLcnRowStatusEntry": ipivcLcnRowStatusEntry,
       "ipivcLcnRowStatus": ipivcLcnRowStatus,
       "ipivcLcnComponentName": ipivcLcnComponentName,
       "ipivcLcnStorageType": ipivcLcnStorageType,
       "ipivcLcnIndex": ipivcLcnIndex,
       "ipivcLcnVc": ipivcLcnVc,
       "ipivcLcnVcRowStatusTable": ipivcLcnVcRowStatusTable,
       "ipivcLcnVcRowStatusEntry": ipivcLcnVcRowStatusEntry,
       "ipivcLcnVcRowStatus": ipivcLcnVcRowStatus,
       "ipivcLcnVcComponentName": ipivcLcnVcComponentName,
       "ipivcLcnVcStorageType": ipivcLcnVcStorageType,
       "ipivcLcnVcIndex": ipivcLcnVcIndex,
       "ipivcLcnVcCadTable": ipivcLcnVcCadTable,
       "ipivcLcnVcCadEntry": ipivcLcnVcCadEntry,
       "ipivcLcnVcType": ipivcLcnVcType,
       "ipivcLcnVcState": ipivcLcnVcState,
       "ipivcLcnVcPreviousState": ipivcLcnVcPreviousState,
       "ipivcLcnVcDiagnosticCode": ipivcLcnVcDiagnosticCode,
       "ipivcLcnVcPreviousDiagnosticCode": ipivcLcnVcPreviousDiagnosticCode,
       "ipivcLcnVcCalledNpi": ipivcLcnVcCalledNpi,
       "ipivcLcnVcCalledDna": ipivcLcnVcCalledDna,
       "ipivcLcnVcCalledLcn": ipivcLcnVcCalledLcn,
       "ipivcLcnVcCallingNpi": ipivcLcnVcCallingNpi,
       "ipivcLcnVcCallingDna": ipivcLcnVcCallingDna,
       "ipivcLcnVcCallingLcn": ipivcLcnVcCallingLcn,
       "ipivcLcnVcAccountingEnabled": ipivcLcnVcAccountingEnabled,
       "ipivcLcnVcFastSelectCall": ipivcLcnVcFastSelectCall,
       "ipivcLcnVcLocalRxPktSize": ipivcLcnVcLocalRxPktSize,
       "ipivcLcnVcLocalTxPktSize": ipivcLcnVcLocalTxPktSize,
       "ipivcLcnVcLocalTxWindowSize": ipivcLcnVcLocalTxWindowSize,
       "ipivcLcnVcLocalRxWindowSize": ipivcLcnVcLocalRxWindowSize,
       "ipivcLcnVcPathReliability": ipivcLcnVcPathReliability,
       "ipivcLcnVcAccountingEnd": ipivcLcnVcAccountingEnd,
       "ipivcLcnVcPriority": ipivcLcnVcPriority,
       "ipivcLcnVcSegmentSize": ipivcLcnVcSegmentSize,
       "ipivcLcnVcSubnetTxPktSize": ipivcLcnVcSubnetTxPktSize,
       "ipivcLcnVcSubnetTxWindowSize": ipivcLcnVcSubnetTxWindowSize,
       "ipivcLcnVcSubnetRxPktSize": ipivcLcnVcSubnetRxPktSize,
       "ipivcLcnVcSubnetRxWindowSize": ipivcLcnVcSubnetRxWindowSize,
       "ipivcLcnVcMaxSubnetPktSize": ipivcLcnVcMaxSubnetPktSize,
       "ipivcLcnVcTransferPriorityToNetwork": ipivcLcnVcTransferPriorityToNetwork,
       "ipivcLcnVcTransferPriorityFromNetwork": ipivcLcnVcTransferPriorityFromNetwork,
       "ipivcLcnVcIntdTable": ipivcLcnVcIntdTable,
       "ipivcLcnVcIntdEntry": ipivcLcnVcIntdEntry,
       "ipivcLcnVcCallReferenceNumber": ipivcLcnVcCallReferenceNumber,
       "ipivcLcnVcElapsedTimeTillNow": ipivcLcnVcElapsedTimeTillNow,
       "ipivcLcnVcSegmentsRx": ipivcLcnVcSegmentsRx,
       "ipivcLcnVcSegmentsSent": ipivcLcnVcSegmentsSent,
       "ipivcLcnVcStartTime": ipivcLcnVcStartTime,
       "ipivcLcnVcStatsTable": ipivcLcnVcStatsTable,
       "ipivcLcnVcStatsEntry": ipivcLcnVcStatsEntry,
       "ipivcLcnVcAckStackingTimeouts": ipivcLcnVcAckStackingTimeouts,
       "ipivcLcnVcOutOfRangeFrmFromSubnet": ipivcLcnVcOutOfRangeFrmFromSubnet,
       "ipivcLcnVcDuplicatesFromSubnet": ipivcLcnVcDuplicatesFromSubnet,
       "ipivcLcnVcFrmRetryTimeouts": ipivcLcnVcFrmRetryTimeouts,
       "ipivcLcnVcPeakRetryQueueSize": ipivcLcnVcPeakRetryQueueSize,
       "ipivcLcnVcPeakOoSeqQueueSize": ipivcLcnVcPeakOoSeqQueueSize,
       "ipivcLcnVcPeakOoSeqFrmForwarded": ipivcLcnVcPeakOoSeqFrmForwarded,
       "ipivcLcnVcPeakStackedAcksRx": ipivcLcnVcPeakStackedAcksRx,
       "ipivcLcnVcSubnetRecoveries": ipivcLcnVcSubnetRecoveries,
       "ipivcLcnVcWindowClosuresToSubnet": ipivcLcnVcWindowClosuresToSubnet,
       "ipivcLcnVcWindowClosuresFromSubnet": ipivcLcnVcWindowClosuresFromSubnet,
       "ipivcLcnVcWrTriggers": ipivcLcnVcWrTriggers,
       "ipivcLcnStateTable": ipivcLcnStateTable,
       "ipivcLcnStateEntry": ipivcLcnStateEntry,
       "ipivcLcnAdminState": ipivcLcnAdminState,
       "ipivcLcnOperationalState": ipivcLcnOperationalState,
       "ipivcLcnUsageState": ipivcLcnUsageState,
       "ipivcLcnAvailabilityStatus": ipivcLcnAvailabilityStatus,
       "ipivcLcnProceduralStatus": ipivcLcnProceduralStatus,
       "ipivcLcnControlStatus": ipivcLcnControlStatus,
       "ipivcLcnAlarmStatus": ipivcLcnAlarmStatus,
       "ipivcLcnStandbyStatus": ipivcLcnStandbyStatus,
       "ipivcLcnUnknownStatus": ipivcLcnUnknownStatus,
       "ipivcLcnOperTable": ipivcLcnOperTable,
       "ipivcLcnOperEntry": ipivcLcnOperEntry,
       "ipivcLcnIpInterfaceDevice": ipivcLcnIpInterfaceDevice,
       "ipivcLcnDestinationIpAddress": ipivcLcnDestinationIpAddress,
       "ipivcLcnPacketsSent": ipivcLcnPacketsSent,
       "ipivcLcnPacketsReceived": ipivcLcnPacketsReceived,
       "ipivcLcnDiscardTxPackets": ipivcLcnDiscardTxPackets,
       "ipivcLcnDiscardRcvPackets": ipivcLcnDiscardRcvPackets,
       "ipivcProvTable": ipivcProvTable,
       "ipivcProvEntry": ipivcProvEntry,
       "ipivcIpAddress": ipivcIpAddress,
       "ipivcMaximumNumberOfLcn": ipivcMaximumNumberOfLcn,
       "ipiVcMIB": ipiVcMIB,
       "ipiVcGroup": ipiVcGroup,
       "ipiVcGroupBE": ipiVcGroupBE,
       "ipiVcGroupBE01": ipiVcGroupBE01,
       "ipiVcGroupBE01A": ipiVcGroupBE01A,
       "ipiVcCapabilities": ipiVcCapabilities,
       "ipiVcCapabilitiesBE": ipiVcCapabilitiesBE,
       "ipiVcCapabilitiesBE01": ipiVcCapabilitiesBE01,
       "ipiVcCapabilitiesBE01A": ipiVcCapabilitiesBE01A}
)
