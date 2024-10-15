# SNMP MIB module (Nortel-MsCarrier-MscPassport-IpiVcMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-IpiVcMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:42 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
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
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "DigitString",
    "EnterpriseDateAndTime",
    "Hex",
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

_MscIpivc_ObjectIdentity = ObjectIdentity
mscIpivc = _MscIpivc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51)
)
_MscIpivcRowStatusTable_Object = MibTable
mscIpivcRowStatusTable = _MscIpivcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 1)
)
if mibBuilder.loadTexts:
    mscIpivcRowStatusTable.setStatus("mandatory")
_MscIpivcRowStatusEntry_Object = MibTableRow
mscIpivcRowStatusEntry = _MscIpivcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 1, 1)
)
mscIpivcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcRowStatusEntry.setStatus("mandatory")
_MscIpivcRowStatus_Type = RowStatus
_MscIpivcRowStatus_Object = MibTableColumn
mscIpivcRowStatus = _MscIpivcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 1, 1, 1),
    _MscIpivcRowStatus_Type()
)
mscIpivcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcRowStatus.setStatus("mandatory")
_MscIpivcComponentName_Type = DisplayString
_MscIpivcComponentName_Object = MibTableColumn
mscIpivcComponentName = _MscIpivcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 1, 1, 2),
    _MscIpivcComponentName_Type()
)
mscIpivcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcComponentName.setStatus("mandatory")
_MscIpivcStorageType_Type = StorageType
_MscIpivcStorageType_Object = MibTableColumn
mscIpivcStorageType = _MscIpivcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 1, 1, 4),
    _MscIpivcStorageType_Type()
)
mscIpivcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcStorageType.setStatus("mandatory")
_MscIpivcIndex_Type = NonReplicated
_MscIpivcIndex_Object = MibTableColumn
mscIpivcIndex = _MscIpivcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 1, 1, 10),
    _MscIpivcIndex_Type()
)
mscIpivcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpivcIndex.setStatus("mandatory")
_MscIpivcDna_ObjectIdentity = ObjectIdentity
mscIpivcDna = _MscIpivcDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2)
)
_MscIpivcDnaRowStatusTable_Object = MibTable
mscIpivcDnaRowStatusTable = _MscIpivcDnaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 1)
)
if mibBuilder.loadTexts:
    mscIpivcDnaRowStatusTable.setStatus("mandatory")
_MscIpivcDnaRowStatusEntry_Object = MibTableRow
mscIpivcDnaRowStatusEntry = _MscIpivcDnaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 1, 1)
)
mscIpivcDnaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDnaRowStatusEntry.setStatus("mandatory")
_MscIpivcDnaRowStatus_Type = RowStatus
_MscIpivcDnaRowStatus_Object = MibTableColumn
mscIpivcDnaRowStatus = _MscIpivcDnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 1, 1, 1),
    _MscIpivcDnaRowStatus_Type()
)
mscIpivcDnaRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaRowStatus.setStatus("mandatory")
_MscIpivcDnaComponentName_Type = DisplayString
_MscIpivcDnaComponentName_Object = MibTableColumn
mscIpivcDnaComponentName = _MscIpivcDnaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 1, 1, 2),
    _MscIpivcDnaComponentName_Type()
)
mscIpivcDnaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaComponentName.setStatus("mandatory")
_MscIpivcDnaStorageType_Type = StorageType
_MscIpivcDnaStorageType_Object = MibTableColumn
mscIpivcDnaStorageType = _MscIpivcDnaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 1, 1, 4),
    _MscIpivcDnaStorageType_Type()
)
mscIpivcDnaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaStorageType.setStatus("mandatory")
_MscIpivcDnaIndex_Type = NonReplicated
_MscIpivcDnaIndex_Object = MibTableColumn
mscIpivcDnaIndex = _MscIpivcDnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 1, 1, 10),
    _MscIpivcDnaIndex_Type()
)
mscIpivcDnaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpivcDnaIndex.setStatus("mandatory")
_MscIpivcDnaCug_ObjectIdentity = ObjectIdentity
mscIpivcDnaCug = _MscIpivcDnaCug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2)
)
_MscIpivcDnaCugRowStatusTable_Object = MibTable
mscIpivcDnaCugRowStatusTable = _MscIpivcDnaCugRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscIpivcDnaCugRowStatusTable.setStatus("mandatory")
_MscIpivcDnaCugRowStatusEntry_Object = MibTableRow
mscIpivcDnaCugRowStatusEntry = _MscIpivcDnaCugRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 1, 1)
)
mscIpivcDnaCugRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDnaCugRowStatusEntry.setStatus("mandatory")
_MscIpivcDnaCugRowStatus_Type = RowStatus
_MscIpivcDnaCugRowStatus_Object = MibTableColumn
mscIpivcDnaCugRowStatus = _MscIpivcDnaCugRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 1, 1, 1),
    _MscIpivcDnaCugRowStatus_Type()
)
mscIpivcDnaCugRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaCugRowStatus.setStatus("mandatory")
_MscIpivcDnaCugComponentName_Type = DisplayString
_MscIpivcDnaCugComponentName_Object = MibTableColumn
mscIpivcDnaCugComponentName = _MscIpivcDnaCugComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 1, 1, 2),
    _MscIpivcDnaCugComponentName_Type()
)
mscIpivcDnaCugComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaCugComponentName.setStatus("mandatory")
_MscIpivcDnaCugStorageType_Type = StorageType
_MscIpivcDnaCugStorageType_Object = MibTableColumn
mscIpivcDnaCugStorageType = _MscIpivcDnaCugStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 1, 1, 4),
    _MscIpivcDnaCugStorageType_Type()
)
mscIpivcDnaCugStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaCugStorageType.setStatus("mandatory")
_MscIpivcDnaCugIndex_Type = NonReplicated
_MscIpivcDnaCugIndex_Object = MibTableColumn
mscIpivcDnaCugIndex = _MscIpivcDnaCugIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 1, 1, 10),
    _MscIpivcDnaCugIndex_Type()
)
mscIpivcDnaCugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpivcDnaCugIndex.setStatus("mandatory")
_MscIpivcDnaCugCugOptionsTable_Object = MibTable
mscIpivcDnaCugCugOptionsTable = _MscIpivcDnaCugCugOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscIpivcDnaCugCugOptionsTable.setStatus("mandatory")
_MscIpivcDnaCugCugOptionsEntry_Object = MibTableRow
mscIpivcDnaCugCugOptionsEntry = _MscIpivcDnaCugCugOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10, 1)
)
mscIpivcDnaCugCugOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaCugIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDnaCugCugOptionsEntry.setStatus("mandatory")


class _MscIpivcDnaCugType_Type(Integer32):
    """Custom type mscIpivcDnaCugType based on Integer32"""
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


_MscIpivcDnaCugType_Type.__name__ = "Integer32"
_MscIpivcDnaCugType_Object = MibTableColumn
mscIpivcDnaCugType = _MscIpivcDnaCugType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10, 1, 1),
    _MscIpivcDnaCugType_Type()
)
mscIpivcDnaCugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaCugType.setStatus("mandatory")


class _MscIpivcDnaCugDnic_Type(DigitString):
    """Custom type mscIpivcDnaCugDnic based on DigitString"""
    defaultHexValue = "30303030"

    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscIpivcDnaCugDnic_Type.__name__ = "DigitString"
_MscIpivcDnaCugDnic_Object = MibTableColumn
mscIpivcDnaCugDnic = _MscIpivcDnaCugDnic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10, 1, 2),
    _MscIpivcDnaCugDnic_Type()
)
mscIpivcDnaCugDnic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaCugDnic.setStatus("mandatory")


class _MscIpivcDnaCugInterlockCode_Type(Unsigned32):
    """Custom type mscIpivcDnaCugInterlockCode based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscIpivcDnaCugInterlockCode_Type.__name__ = "Unsigned32"
_MscIpivcDnaCugInterlockCode_Object = MibTableColumn
mscIpivcDnaCugInterlockCode = _MscIpivcDnaCugInterlockCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10, 1, 3),
    _MscIpivcDnaCugInterlockCode_Type()
)
mscIpivcDnaCugInterlockCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaCugInterlockCode.setStatus("mandatory")


class _MscIpivcDnaCugOutCalls_Type(Integer32):
    """Custom type mscIpivcDnaCugOutCalls based on Integer32"""
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


_MscIpivcDnaCugOutCalls_Type.__name__ = "Integer32"
_MscIpivcDnaCugOutCalls_Object = MibTableColumn
mscIpivcDnaCugOutCalls = _MscIpivcDnaCugOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10, 1, 5),
    _MscIpivcDnaCugOutCalls_Type()
)
mscIpivcDnaCugOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaCugOutCalls.setStatus("mandatory")


class _MscIpivcDnaCugIncCalls_Type(Integer32):
    """Custom type mscIpivcDnaCugIncCalls based on Integer32"""
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


_MscIpivcDnaCugIncCalls_Type.__name__ = "Integer32"
_MscIpivcDnaCugIncCalls_Object = MibTableColumn
mscIpivcDnaCugIncCalls = _MscIpivcDnaCugIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10, 1, 6),
    _MscIpivcDnaCugIncCalls_Type()
)
mscIpivcDnaCugIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaCugIncCalls.setStatus("mandatory")


class _MscIpivcDnaCugPrivileged_Type(Integer32):
    """Custom type mscIpivcDnaCugPrivileged based on Integer32"""
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


_MscIpivcDnaCugPrivileged_Type.__name__ = "Integer32"
_MscIpivcDnaCugPrivileged_Object = MibTableColumn
mscIpivcDnaCugPrivileged = _MscIpivcDnaCugPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 2, 10, 1, 7),
    _MscIpivcDnaCugPrivileged_Type()
)
mscIpivcDnaCugPrivileged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaCugPrivileged.setStatus("mandatory")
_MscIpivcDnaAddressTable_Object = MibTable
mscIpivcDnaAddressTable = _MscIpivcDnaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 10)
)
if mibBuilder.loadTexts:
    mscIpivcDnaAddressTable.setStatus("mandatory")
_MscIpivcDnaAddressEntry_Object = MibTableRow
mscIpivcDnaAddressEntry = _MscIpivcDnaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 10, 1)
)
mscIpivcDnaAddressEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDnaAddressEntry.setStatus("mandatory")


class _MscIpivcDnaNumberingPlanIndicator_Type(Integer32):
    """Custom type mscIpivcDnaNumberingPlanIndicator based on Integer32"""
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


_MscIpivcDnaNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscIpivcDnaNumberingPlanIndicator_Object = MibTableColumn
mscIpivcDnaNumberingPlanIndicator = _MscIpivcDnaNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 10, 1, 1),
    _MscIpivcDnaNumberingPlanIndicator_Type()
)
mscIpivcDnaNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaNumberingPlanIndicator.setStatus("mandatory")


class _MscIpivcDnaDataNetworkAddress_Type(DigitString):
    """Custom type mscIpivcDnaDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpivcDnaDataNetworkAddress_Type.__name__ = "DigitString"
_MscIpivcDnaDataNetworkAddress_Object = MibTableColumn
mscIpivcDnaDataNetworkAddress = _MscIpivcDnaDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 10, 1, 2),
    _MscIpivcDnaDataNetworkAddress_Type()
)
mscIpivcDnaDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaDataNetworkAddress.setStatus("mandatory")
_MscIpivcDnaOutgoingOptionsTable_Object = MibTable
mscIpivcDnaOutgoingOptionsTable = _MscIpivcDnaOutgoingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 11)
)
if mibBuilder.loadTexts:
    mscIpivcDnaOutgoingOptionsTable.setStatus("mandatory")
_MscIpivcDnaOutgoingOptionsEntry_Object = MibTableRow
mscIpivcDnaOutgoingOptionsEntry = _MscIpivcDnaOutgoingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 11, 1)
)
mscIpivcDnaOutgoingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDnaOutgoingOptionsEntry.setStatus("mandatory")


class _MscIpivcDnaOutCalls_Type(Integer32):
    """Custom type mscIpivcDnaOutCalls based on Integer32"""
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


_MscIpivcDnaOutCalls_Type.__name__ = "Integer32"
_MscIpivcDnaOutCalls_Object = MibTableColumn
mscIpivcDnaOutCalls = _MscIpivcDnaOutCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 11, 1, 1),
    _MscIpivcDnaOutCalls_Type()
)
mscIpivcDnaOutCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaOutCalls.setStatus("mandatory")


class _MscIpivcDnaOutDefaultPathSensitivity_Type(Integer32):
    """Custom type mscIpivcDnaOutDefaultPathSensitivity based on Integer32"""
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


_MscIpivcDnaOutDefaultPathSensitivity_Type.__name__ = "Integer32"
_MscIpivcDnaOutDefaultPathSensitivity_Object = MibTableColumn
mscIpivcDnaOutDefaultPathSensitivity = _MscIpivcDnaOutDefaultPathSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 11, 1, 11),
    _MscIpivcDnaOutDefaultPathSensitivity_Type()
)
mscIpivcDnaOutDefaultPathSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaOutDefaultPathSensitivity.setStatus("obsolete")


class _MscIpivcDnaOutPathSensitivityOverRide_Type(Integer32):
    """Custom type mscIpivcDnaOutPathSensitivityOverRide based on Integer32"""
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


_MscIpivcDnaOutPathSensitivityOverRide_Type.__name__ = "Integer32"
_MscIpivcDnaOutPathSensitivityOverRide_Object = MibTableColumn
mscIpivcDnaOutPathSensitivityOverRide = _MscIpivcDnaOutPathSensitivityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 11, 1, 12),
    _MscIpivcDnaOutPathSensitivityOverRide_Type()
)
mscIpivcDnaOutPathSensitivityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaOutPathSensitivityOverRide.setStatus("obsolete")


class _MscIpivcDnaDefaultTransferPriority_Type(Integer32):
    """Custom type mscIpivcDnaDefaultTransferPriority based on Integer32"""
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


_MscIpivcDnaDefaultTransferPriority_Type.__name__ = "Integer32"
_MscIpivcDnaDefaultTransferPriority_Object = MibTableColumn
mscIpivcDnaDefaultTransferPriority = _MscIpivcDnaDefaultTransferPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 11, 1, 18),
    _MscIpivcDnaDefaultTransferPriority_Type()
)
mscIpivcDnaDefaultTransferPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaDefaultTransferPriority.setStatus("mandatory")


class _MscIpivcDnaTransferPriorityOverRide_Type(Integer32):
    """Custom type mscIpivcDnaTransferPriorityOverRide based on Integer32"""
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


_MscIpivcDnaTransferPriorityOverRide_Type.__name__ = "Integer32"
_MscIpivcDnaTransferPriorityOverRide_Object = MibTableColumn
mscIpivcDnaTransferPriorityOverRide = _MscIpivcDnaTransferPriorityOverRide_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 11, 1, 19),
    _MscIpivcDnaTransferPriorityOverRide_Type()
)
mscIpivcDnaTransferPriorityOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaTransferPriorityOverRide.setStatus("mandatory")
_MscIpivcDnaIncomingOptionsTable_Object = MibTable
mscIpivcDnaIncomingOptionsTable = _MscIpivcDnaIncomingOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12)
)
if mibBuilder.loadTexts:
    mscIpivcDnaIncomingOptionsTable.setStatus("mandatory")
_MscIpivcDnaIncomingOptionsEntry_Object = MibTableRow
mscIpivcDnaIncomingOptionsEntry = _MscIpivcDnaIncomingOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1)
)
mscIpivcDnaIncomingOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDnaIncomingOptionsEntry.setStatus("mandatory")


class _MscIpivcDnaIncCalls_Type(Integer32):
    """Custom type mscIpivcDnaIncCalls based on Integer32"""
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


_MscIpivcDnaIncCalls_Type.__name__ = "Integer32"
_MscIpivcDnaIncCalls_Object = MibTableColumn
mscIpivcDnaIncCalls = _MscIpivcDnaIncCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 1),
    _MscIpivcDnaIncCalls_Type()
)
mscIpivcDnaIncCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncCalls.setStatus("mandatory")


class _MscIpivcDnaIncHighPriorityReverseCharge_Type(Integer32):
    """Custom type mscIpivcDnaIncHighPriorityReverseCharge based on Integer32"""
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


_MscIpivcDnaIncHighPriorityReverseCharge_Type.__name__ = "Integer32"
_MscIpivcDnaIncHighPriorityReverseCharge_Object = MibTableColumn
mscIpivcDnaIncHighPriorityReverseCharge = _MscIpivcDnaIncHighPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 2),
    _MscIpivcDnaIncHighPriorityReverseCharge_Type()
)
mscIpivcDnaIncHighPriorityReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncHighPriorityReverseCharge.setStatus("mandatory")


class _MscIpivcDnaIncNormalPriorityReverseCharge_Type(Integer32):
    """Custom type mscIpivcDnaIncNormalPriorityReverseCharge based on Integer32"""
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


_MscIpivcDnaIncNormalPriorityReverseCharge_Type.__name__ = "Integer32"
_MscIpivcDnaIncNormalPriorityReverseCharge_Object = MibTableColumn
mscIpivcDnaIncNormalPriorityReverseCharge = _MscIpivcDnaIncNormalPriorityReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 3),
    _MscIpivcDnaIncNormalPriorityReverseCharge_Type()
)
mscIpivcDnaIncNormalPriorityReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncNormalPriorityReverseCharge.setStatus("mandatory")


class _MscIpivcDnaIncIntlNormalCharge_Type(Integer32):
    """Custom type mscIpivcDnaIncIntlNormalCharge based on Integer32"""
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


_MscIpivcDnaIncIntlNormalCharge_Type.__name__ = "Integer32"
_MscIpivcDnaIncIntlNormalCharge_Object = MibTableColumn
mscIpivcDnaIncIntlNormalCharge = _MscIpivcDnaIncIntlNormalCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 4),
    _MscIpivcDnaIncIntlNormalCharge_Type()
)
mscIpivcDnaIncIntlNormalCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncIntlNormalCharge.setStatus("mandatory")


class _MscIpivcDnaIncIntlReverseCharge_Type(Integer32):
    """Custom type mscIpivcDnaIncIntlReverseCharge based on Integer32"""
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


_MscIpivcDnaIncIntlReverseCharge_Type.__name__ = "Integer32"
_MscIpivcDnaIncIntlReverseCharge_Object = MibTableColumn
mscIpivcDnaIncIntlReverseCharge = _MscIpivcDnaIncIntlReverseCharge_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 5),
    _MscIpivcDnaIncIntlReverseCharge_Type()
)
mscIpivcDnaIncIntlReverseCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncIntlReverseCharge.setStatus("mandatory")


class _MscIpivcDnaIncFastSelect_Type(Integer32):
    """Custom type mscIpivcDnaIncFastSelect based on Integer32"""
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


_MscIpivcDnaIncFastSelect_Type.__name__ = "Integer32"
_MscIpivcDnaIncFastSelect_Object = MibTableColumn
mscIpivcDnaIncFastSelect = _MscIpivcDnaIncFastSelect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 6),
    _MscIpivcDnaIncFastSelect_Type()
)
mscIpivcDnaIncFastSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncFastSelect.setStatus("mandatory")


class _MscIpivcDnaIncSameService_Type(Integer32):
    """Custom type mscIpivcDnaIncSameService based on Integer32"""
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


_MscIpivcDnaIncSameService_Type.__name__ = "Integer32"
_MscIpivcDnaIncSameService_Object = MibTableColumn
mscIpivcDnaIncSameService = _MscIpivcDnaIncSameService_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 7),
    _MscIpivcDnaIncSameService_Type()
)
mscIpivcDnaIncSameService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncSameService.setStatus("mandatory")


class _MscIpivcDnaIncChargeTransfer_Type(Integer32):
    """Custom type mscIpivcDnaIncChargeTransfer based on Integer32"""
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


_MscIpivcDnaIncChargeTransfer_Type.__name__ = "Integer32"
_MscIpivcDnaIncChargeTransfer_Object = MibTableColumn
mscIpivcDnaIncChargeTransfer = _MscIpivcDnaIncChargeTransfer_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 8),
    _MscIpivcDnaIncChargeTransfer_Type()
)
mscIpivcDnaIncChargeTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncChargeTransfer.setStatus("mandatory")


class _MscIpivcDnaIncAccess_Type(Integer32):
    """Custom type mscIpivcDnaIncAccess based on Integer32"""
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


_MscIpivcDnaIncAccess_Type.__name__ = "Integer32"
_MscIpivcDnaIncAccess_Object = MibTableColumn
mscIpivcDnaIncAccess = _MscIpivcDnaIncAccess_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 12, 1, 9),
    _MscIpivcDnaIncAccess_Type()
)
mscIpivcDnaIncAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaIncAccess.setStatus("mandatory")
_MscIpivcDnaCallOptionsTable_Object = MibTable
mscIpivcDnaCallOptionsTable = _MscIpivcDnaCallOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13)
)
if mibBuilder.loadTexts:
    mscIpivcDnaCallOptionsTable.setStatus("mandatory")
_MscIpivcDnaCallOptionsEntry_Object = MibTableRow
mscIpivcDnaCallOptionsEntry = _MscIpivcDnaCallOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1)
)
mscIpivcDnaCallOptionsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDnaIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDnaCallOptionsEntry.setStatus("mandatory")


class _MscIpivcDnaServiceCategory_Type(Integer32):
    """Custom type mscIpivcDnaServiceCategory based on Integer32"""
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


_MscIpivcDnaServiceCategory_Type.__name__ = "Integer32"
_MscIpivcDnaServiceCategory_Object = MibTableColumn
mscIpivcDnaServiceCategory = _MscIpivcDnaServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 1),
    _MscIpivcDnaServiceCategory_Type()
)
mscIpivcDnaServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaServiceCategory.setStatus("mandatory")


class _MscIpivcDnaPacketSizes_Type(OctetString):
    """Custom type mscIpivcDnaPacketSizes based on OctetString"""
    defaultHexValue = "0100"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscIpivcDnaPacketSizes_Type.__name__ = "OctetString"
_MscIpivcDnaPacketSizes_Object = MibTableColumn
mscIpivcDnaPacketSizes = _MscIpivcDnaPacketSizes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 2),
    _MscIpivcDnaPacketSizes_Type()
)
mscIpivcDnaPacketSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaPacketSizes.setStatus("mandatory")


class _MscIpivcDnaDefaultRecvFrmNetworkPacketSize_Type(Integer32):
    """Custom type mscIpivcDnaDefaultRecvFrmNetworkPacketSize based on Integer32"""
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


_MscIpivcDnaDefaultRecvFrmNetworkPacketSize_Type.__name__ = "Integer32"
_MscIpivcDnaDefaultRecvFrmNetworkPacketSize_Object = MibTableColumn
mscIpivcDnaDefaultRecvFrmNetworkPacketSize = _MscIpivcDnaDefaultRecvFrmNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 3),
    _MscIpivcDnaDefaultRecvFrmNetworkPacketSize_Type()
)
mscIpivcDnaDefaultRecvFrmNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaDefaultRecvFrmNetworkPacketSize.setStatus("mandatory")


class _MscIpivcDnaDefaultSendToNetworkPacketSize_Type(Integer32):
    """Custom type mscIpivcDnaDefaultSendToNetworkPacketSize based on Integer32"""
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


_MscIpivcDnaDefaultSendToNetworkPacketSize_Type.__name__ = "Integer32"
_MscIpivcDnaDefaultSendToNetworkPacketSize_Object = MibTableColumn
mscIpivcDnaDefaultSendToNetworkPacketSize = _MscIpivcDnaDefaultSendToNetworkPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 4),
    _MscIpivcDnaDefaultSendToNetworkPacketSize_Type()
)
mscIpivcDnaDefaultSendToNetworkPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaDefaultSendToNetworkPacketSize.setStatus("mandatory")


class _MscIpivcDnaDefaultRecvFrmNetworkThruputClass_Type(Unsigned32):
    """Custom type mscIpivcDnaDefaultRecvFrmNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscIpivcDnaDefaultRecvFrmNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscIpivcDnaDefaultRecvFrmNetworkThruputClass_Object = MibTableColumn
mscIpivcDnaDefaultRecvFrmNetworkThruputClass = _MscIpivcDnaDefaultRecvFrmNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 5),
    _MscIpivcDnaDefaultRecvFrmNetworkThruputClass_Type()
)
mscIpivcDnaDefaultRecvFrmNetworkThruputClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaDefaultRecvFrmNetworkThruputClass.setStatus("mandatory")


class _MscIpivcDnaDefaultSendToNetworkThruputClass_Type(Unsigned32):
    """Custom type mscIpivcDnaDefaultSendToNetworkThruputClass based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscIpivcDnaDefaultSendToNetworkThruputClass_Type.__name__ = "Unsigned32"
_MscIpivcDnaDefaultSendToNetworkThruputClass_Object = MibTableColumn
mscIpivcDnaDefaultSendToNetworkThruputClass = _MscIpivcDnaDefaultSendToNetworkThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 6),
    _MscIpivcDnaDefaultSendToNetworkThruputClass_Type()
)
mscIpivcDnaDefaultSendToNetworkThruputClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaDefaultSendToNetworkThruputClass.setStatus("mandatory")


class _MscIpivcDnaDefaultRecvFrmNetworkWindowSize_Type(Unsigned32):
    """Custom type mscIpivcDnaDefaultRecvFrmNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscIpivcDnaDefaultRecvFrmNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscIpivcDnaDefaultRecvFrmNetworkWindowSize_Object = MibTableColumn
mscIpivcDnaDefaultRecvFrmNetworkWindowSize = _MscIpivcDnaDefaultRecvFrmNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 7),
    _MscIpivcDnaDefaultRecvFrmNetworkWindowSize_Type()
)
mscIpivcDnaDefaultRecvFrmNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaDefaultRecvFrmNetworkWindowSize.setStatus("mandatory")


class _MscIpivcDnaDefaultSendToNetworkWindowSize_Type(Unsigned32):
    """Custom type mscIpivcDnaDefaultSendToNetworkWindowSize based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MscIpivcDnaDefaultSendToNetworkWindowSize_Type.__name__ = "Unsigned32"
_MscIpivcDnaDefaultSendToNetworkWindowSize_Object = MibTableColumn
mscIpivcDnaDefaultSendToNetworkWindowSize = _MscIpivcDnaDefaultSendToNetworkWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 8),
    _MscIpivcDnaDefaultSendToNetworkWindowSize_Type()
)
mscIpivcDnaDefaultSendToNetworkWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaDefaultSendToNetworkWindowSize.setStatus("mandatory")


class _MscIpivcDnaPacketSizeNegotiation_Type(Integer32):
    """Custom type mscIpivcDnaPacketSizeNegotiation based on Integer32"""
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


_MscIpivcDnaPacketSizeNegotiation_Type.__name__ = "Integer32"
_MscIpivcDnaPacketSizeNegotiation_Object = MibTableColumn
mscIpivcDnaPacketSizeNegotiation = _MscIpivcDnaPacketSizeNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 9),
    _MscIpivcDnaPacketSizeNegotiation_Type()
)
mscIpivcDnaPacketSizeNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaPacketSizeNegotiation.setStatus("mandatory")


class _MscIpivcDnaAccountClass_Type(Unsigned32):
    """Custom type mscIpivcDnaAccountClass based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpivcDnaAccountClass_Type.__name__ = "Unsigned32"
_MscIpivcDnaAccountClass_Object = MibTableColumn
mscIpivcDnaAccountClass = _MscIpivcDnaAccountClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 10),
    _MscIpivcDnaAccountClass_Type()
)
mscIpivcDnaAccountClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaAccountClass.setStatus("mandatory")


class _MscIpivcDnaServiceExchange_Type(Unsigned32):
    """Custom type mscIpivcDnaServiceExchange based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpivcDnaServiceExchange_Type.__name__ = "Unsigned32"
_MscIpivcDnaServiceExchange_Object = MibTableColumn
mscIpivcDnaServiceExchange = _MscIpivcDnaServiceExchange_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 12),
    _MscIpivcDnaServiceExchange_Type()
)
mscIpivcDnaServiceExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDnaServiceExchange.setStatus("mandatory")


class _MscIpivcDnaCugFormat_Type(Integer32):
    """Custom type mscIpivcDnaCugFormat based on Integer32"""
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


_MscIpivcDnaCugFormat_Type.__name__ = "Integer32"
_MscIpivcDnaCugFormat_Object = MibTableColumn
mscIpivcDnaCugFormat = _MscIpivcDnaCugFormat_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 13),
    _MscIpivcDnaCugFormat_Type()
)
mscIpivcDnaCugFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaCugFormat.setStatus("mandatory")


class _MscIpivcDnaCug0AsNonCugCall_Type(Integer32):
    """Custom type mscIpivcDnaCug0AsNonCugCall based on Integer32"""
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


_MscIpivcDnaCug0AsNonCugCall_Type.__name__ = "Integer32"
_MscIpivcDnaCug0AsNonCugCall_Object = MibTableColumn
mscIpivcDnaCug0AsNonCugCall = _MscIpivcDnaCug0AsNonCugCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 14),
    _MscIpivcDnaCug0AsNonCugCall_Type()
)
mscIpivcDnaCug0AsNonCugCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaCug0AsNonCugCall.setStatus("mandatory")


class _MscIpivcDnaFastSelectCallsOnly_Type(Integer32):
    """Custom type mscIpivcDnaFastSelectCallsOnly based on Integer32"""
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


_MscIpivcDnaFastSelectCallsOnly_Type.__name__ = "Integer32"
_MscIpivcDnaFastSelectCallsOnly_Object = MibTableColumn
mscIpivcDnaFastSelectCallsOnly = _MscIpivcDnaFastSelectCallsOnly_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 2, 13, 1, 17),
    _MscIpivcDnaFastSelectCallsOnly_Type()
)
mscIpivcDnaFastSelectCallsOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDnaFastSelectCallsOnly.setStatus("mandatory")
_MscIpivcDr_ObjectIdentity = ObjectIdentity
mscIpivcDr = _MscIpivcDr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3)
)
_MscIpivcDrRowStatusTable_Object = MibTable
mscIpivcDrRowStatusTable = _MscIpivcDrRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 1)
)
if mibBuilder.loadTexts:
    mscIpivcDrRowStatusTable.setStatus("mandatory")
_MscIpivcDrRowStatusEntry_Object = MibTableRow
mscIpivcDrRowStatusEntry = _MscIpivcDrRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 1, 1)
)
mscIpivcDrRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDrIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDrRowStatusEntry.setStatus("mandatory")
_MscIpivcDrRowStatus_Type = RowStatus
_MscIpivcDrRowStatus_Object = MibTableColumn
mscIpivcDrRowStatus = _MscIpivcDrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 1, 1, 1),
    _MscIpivcDrRowStatus_Type()
)
mscIpivcDrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDrRowStatus.setStatus("mandatory")
_MscIpivcDrComponentName_Type = DisplayString
_MscIpivcDrComponentName_Object = MibTableColumn
mscIpivcDrComponentName = _MscIpivcDrComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 1, 1, 2),
    _MscIpivcDrComponentName_Type()
)
mscIpivcDrComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDrComponentName.setStatus("mandatory")
_MscIpivcDrStorageType_Type = StorageType
_MscIpivcDrStorageType_Object = MibTableColumn
mscIpivcDrStorageType = _MscIpivcDrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 1, 1, 4),
    _MscIpivcDrStorageType_Type()
)
mscIpivcDrStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcDrStorageType.setStatus("mandatory")
_MscIpivcDrIndex_Type = NonReplicated
_MscIpivcDrIndex_Object = MibTableColumn
mscIpivcDrIndex = _MscIpivcDrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 1, 1, 10),
    _MscIpivcDrIndex_Type()
)
mscIpivcDrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpivcDrIndex.setStatus("mandatory")
_MscIpivcDrProvTable_Object = MibTable
mscIpivcDrProvTable = _MscIpivcDrProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 10)
)
if mibBuilder.loadTexts:
    mscIpivcDrProvTable.setStatus("mandatory")
_MscIpivcDrProvEntry_Object = MibTableRow
mscIpivcDrProvEntry = _MscIpivcDrProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 10, 1)
)
mscIpivcDrProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcDrIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcDrProvEntry.setStatus("mandatory")


class _MscIpivcDrCallingIpAddress_Type(IpAddress):
    """Custom type mscIpivcDrCallingIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpivcDrCallingIpAddress_Object = MibTableColumn
mscIpivcDrCallingIpAddress = _MscIpivcDrCallingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 10, 1, 1),
    _MscIpivcDrCallingIpAddress_Type()
)
mscIpivcDrCallingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDrCallingIpAddress.setStatus("mandatory")


class _MscIpivcDrCallingNumberingPlanIndicator_Type(Integer32):
    """Custom type mscIpivcDrCallingNumberingPlanIndicator based on Integer32"""
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


_MscIpivcDrCallingNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscIpivcDrCallingNumberingPlanIndicator_Object = MibTableColumn
mscIpivcDrCallingNumberingPlanIndicator = _MscIpivcDrCallingNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 10, 1, 2),
    _MscIpivcDrCallingNumberingPlanIndicator_Type()
)
mscIpivcDrCallingNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDrCallingNumberingPlanIndicator.setStatus("mandatory")


class _MscIpivcDrCallingDataNetworkAddress_Type(DigitString):
    """Custom type mscIpivcDrCallingDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpivcDrCallingDataNetworkAddress_Type.__name__ = "DigitString"
_MscIpivcDrCallingDataNetworkAddress_Object = MibTableColumn
mscIpivcDrCallingDataNetworkAddress = _MscIpivcDrCallingDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 3, 10, 1, 3),
    _MscIpivcDrCallingDataNetworkAddress_Type()
)
mscIpivcDrCallingDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcDrCallingDataNetworkAddress.setStatus("mandatory")
_MscIpivcLcn_ObjectIdentity = ObjectIdentity
mscIpivcLcn = _MscIpivcLcn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4)
)
_MscIpivcLcnRowStatusTable_Object = MibTable
mscIpivcLcnRowStatusTable = _MscIpivcLcnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 1)
)
if mibBuilder.loadTexts:
    mscIpivcLcnRowStatusTable.setStatus("mandatory")
_MscIpivcLcnRowStatusEntry_Object = MibTableRow
mscIpivcLcnRowStatusEntry = _MscIpivcLcnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 1, 1)
)
mscIpivcLcnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcLcnRowStatusEntry.setStatus("mandatory")
_MscIpivcLcnRowStatus_Type = RowStatus
_MscIpivcLcnRowStatus_Object = MibTableColumn
mscIpivcLcnRowStatus = _MscIpivcLcnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 1, 1, 1),
    _MscIpivcLcnRowStatus_Type()
)
mscIpivcLcnRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnRowStatus.setStatus("mandatory")
_MscIpivcLcnComponentName_Type = DisplayString
_MscIpivcLcnComponentName_Object = MibTableColumn
mscIpivcLcnComponentName = _MscIpivcLcnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 1, 1, 2),
    _MscIpivcLcnComponentName_Type()
)
mscIpivcLcnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnComponentName.setStatus("mandatory")
_MscIpivcLcnStorageType_Type = StorageType
_MscIpivcLcnStorageType_Object = MibTableColumn
mscIpivcLcnStorageType = _MscIpivcLcnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 1, 1, 4),
    _MscIpivcLcnStorageType_Type()
)
mscIpivcLcnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnStorageType.setStatus("mandatory")


class _MscIpivcLcnIndex_Type(Integer32):
    """Custom type mscIpivcLcnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 39),
    )


_MscIpivcLcnIndex_Type.__name__ = "Integer32"
_MscIpivcLcnIndex_Object = MibTableColumn
mscIpivcLcnIndex = _MscIpivcLcnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 1, 1, 10),
    _MscIpivcLcnIndex_Type()
)
mscIpivcLcnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpivcLcnIndex.setStatus("mandatory")
_MscIpivcLcnVc_ObjectIdentity = ObjectIdentity
mscIpivcLcnVc = _MscIpivcLcnVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2)
)
_MscIpivcLcnVcRowStatusTable_Object = MibTable
mscIpivcLcnVcRowStatusTable = _MscIpivcLcnVcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcRowStatusTable.setStatus("mandatory")
_MscIpivcLcnVcRowStatusEntry_Object = MibTableRow
mscIpivcLcnVcRowStatusEntry = _MscIpivcLcnVcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 1, 1)
)
mscIpivcLcnVcRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcRowStatusEntry.setStatus("mandatory")
_MscIpivcLcnVcRowStatus_Type = RowStatus
_MscIpivcLcnVcRowStatus_Object = MibTableColumn
mscIpivcLcnVcRowStatus = _MscIpivcLcnVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 1, 1, 1),
    _MscIpivcLcnVcRowStatus_Type()
)
mscIpivcLcnVcRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcRowStatus.setStatus("mandatory")
_MscIpivcLcnVcComponentName_Type = DisplayString
_MscIpivcLcnVcComponentName_Object = MibTableColumn
mscIpivcLcnVcComponentName = _MscIpivcLcnVcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 1, 1, 2),
    _MscIpivcLcnVcComponentName_Type()
)
mscIpivcLcnVcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcComponentName.setStatus("mandatory")
_MscIpivcLcnVcStorageType_Type = StorageType
_MscIpivcLcnVcStorageType_Object = MibTableColumn
mscIpivcLcnVcStorageType = _MscIpivcLcnVcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 1, 1, 4),
    _MscIpivcLcnVcStorageType_Type()
)
mscIpivcLcnVcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcStorageType.setStatus("mandatory")
_MscIpivcLcnVcIndex_Type = NonReplicated
_MscIpivcLcnVcIndex_Object = MibTableColumn
mscIpivcLcnVcIndex = _MscIpivcLcnVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 1, 1, 10),
    _MscIpivcLcnVcIndex_Type()
)
mscIpivcLcnVcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscIpivcLcnVcIndex.setStatus("mandatory")
_MscIpivcLcnVcCadTable_Object = MibTable
mscIpivcLcnVcCadTable = _MscIpivcLcnVcCadTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcCadTable.setStatus("mandatory")
_MscIpivcLcnVcCadEntry_Object = MibTableRow
mscIpivcLcnVcCadEntry = _MscIpivcLcnVcCadEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1)
)
mscIpivcLcnVcCadEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcCadEntry.setStatus("mandatory")


class _MscIpivcLcnVcType_Type(Integer32):
    """Custom type mscIpivcLcnVcType based on Integer32"""
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


_MscIpivcLcnVcType_Type.__name__ = "Integer32"
_MscIpivcLcnVcType_Object = MibTableColumn
mscIpivcLcnVcType = _MscIpivcLcnVcType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 1),
    _MscIpivcLcnVcType_Type()
)
mscIpivcLcnVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcType.setStatus("mandatory")


class _MscIpivcLcnVcState_Type(Integer32):
    """Custom type mscIpivcLcnVcState based on Integer32"""
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


_MscIpivcLcnVcState_Type.__name__ = "Integer32"
_MscIpivcLcnVcState_Object = MibTableColumn
mscIpivcLcnVcState = _MscIpivcLcnVcState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 2),
    _MscIpivcLcnVcState_Type()
)
mscIpivcLcnVcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcState.setStatus("mandatory")


class _MscIpivcLcnVcPreviousState_Type(Integer32):
    """Custom type mscIpivcLcnVcPreviousState based on Integer32"""
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


_MscIpivcLcnVcPreviousState_Type.__name__ = "Integer32"
_MscIpivcLcnVcPreviousState_Object = MibTableColumn
mscIpivcLcnVcPreviousState = _MscIpivcLcnVcPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 3),
    _MscIpivcLcnVcPreviousState_Type()
)
mscIpivcLcnVcPreviousState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPreviousState.setStatus("mandatory")


class _MscIpivcLcnVcDiagnosticCode_Type(Unsigned32):
    """Custom type mscIpivcLcnVcDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpivcLcnVcDiagnosticCode_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcDiagnosticCode_Object = MibTableColumn
mscIpivcLcnVcDiagnosticCode = _MscIpivcLcnVcDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 4),
    _MscIpivcLcnVcDiagnosticCode_Type()
)
mscIpivcLcnVcDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcDiagnosticCode.setStatus("mandatory")


class _MscIpivcLcnVcPreviousDiagnosticCode_Type(Unsigned32):
    """Custom type mscIpivcLcnVcPreviousDiagnosticCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscIpivcLcnVcPreviousDiagnosticCode_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcPreviousDiagnosticCode_Object = MibTableColumn
mscIpivcLcnVcPreviousDiagnosticCode = _MscIpivcLcnVcPreviousDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 5),
    _MscIpivcLcnVcPreviousDiagnosticCode_Type()
)
mscIpivcLcnVcPreviousDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPreviousDiagnosticCode.setStatus("mandatory")


class _MscIpivcLcnVcCalledNpi_Type(Integer32):
    """Custom type mscIpivcLcnVcCalledNpi based on Integer32"""
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


_MscIpivcLcnVcCalledNpi_Type.__name__ = "Integer32"
_MscIpivcLcnVcCalledNpi_Object = MibTableColumn
mscIpivcLcnVcCalledNpi = _MscIpivcLcnVcCalledNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 6),
    _MscIpivcLcnVcCalledNpi_Type()
)
mscIpivcLcnVcCalledNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCalledNpi.setStatus("mandatory")


class _MscIpivcLcnVcCalledDna_Type(DigitString):
    """Custom type mscIpivcLcnVcCalledDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpivcLcnVcCalledDna_Type.__name__ = "DigitString"
_MscIpivcLcnVcCalledDna_Object = MibTableColumn
mscIpivcLcnVcCalledDna = _MscIpivcLcnVcCalledDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 7),
    _MscIpivcLcnVcCalledDna_Type()
)
mscIpivcLcnVcCalledDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCalledDna.setStatus("mandatory")


class _MscIpivcLcnVcCalledLcn_Type(Unsigned32):
    """Custom type mscIpivcLcnVcCalledLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscIpivcLcnVcCalledLcn_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcCalledLcn_Object = MibTableColumn
mscIpivcLcnVcCalledLcn = _MscIpivcLcnVcCalledLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 8),
    _MscIpivcLcnVcCalledLcn_Type()
)
mscIpivcLcnVcCalledLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCalledLcn.setStatus("mandatory")


class _MscIpivcLcnVcCallingNpi_Type(Integer32):
    """Custom type mscIpivcLcnVcCallingNpi based on Integer32"""
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


_MscIpivcLcnVcCallingNpi_Type.__name__ = "Integer32"
_MscIpivcLcnVcCallingNpi_Object = MibTableColumn
mscIpivcLcnVcCallingNpi = _MscIpivcLcnVcCallingNpi_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 9),
    _MscIpivcLcnVcCallingNpi_Type()
)
mscIpivcLcnVcCallingNpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCallingNpi.setStatus("mandatory")


class _MscIpivcLcnVcCallingDna_Type(DigitString):
    """Custom type mscIpivcLcnVcCallingDna based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MscIpivcLcnVcCallingDna_Type.__name__ = "DigitString"
_MscIpivcLcnVcCallingDna_Object = MibTableColumn
mscIpivcLcnVcCallingDna = _MscIpivcLcnVcCallingDna_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 10),
    _MscIpivcLcnVcCallingDna_Type()
)
mscIpivcLcnVcCallingDna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCallingDna.setStatus("mandatory")


class _MscIpivcLcnVcCallingLcn_Type(Unsigned32):
    """Custom type mscIpivcLcnVcCallingLcn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscIpivcLcnVcCallingLcn_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcCallingLcn_Object = MibTableColumn
mscIpivcLcnVcCallingLcn = _MscIpivcLcnVcCallingLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 11),
    _MscIpivcLcnVcCallingLcn_Type()
)
mscIpivcLcnVcCallingLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCallingLcn.setStatus("mandatory")


class _MscIpivcLcnVcAccountingEnabled_Type(Integer32):
    """Custom type mscIpivcLcnVcAccountingEnabled based on Integer32"""
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


_MscIpivcLcnVcAccountingEnabled_Type.__name__ = "Integer32"
_MscIpivcLcnVcAccountingEnabled_Object = MibTableColumn
mscIpivcLcnVcAccountingEnabled = _MscIpivcLcnVcAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 12),
    _MscIpivcLcnVcAccountingEnabled_Type()
)
mscIpivcLcnVcAccountingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcAccountingEnabled.setStatus("mandatory")


class _MscIpivcLcnVcFastSelectCall_Type(Integer32):
    """Custom type mscIpivcLcnVcFastSelectCall based on Integer32"""
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


_MscIpivcLcnVcFastSelectCall_Type.__name__ = "Integer32"
_MscIpivcLcnVcFastSelectCall_Object = MibTableColumn
mscIpivcLcnVcFastSelectCall = _MscIpivcLcnVcFastSelectCall_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 13),
    _MscIpivcLcnVcFastSelectCall_Type()
)
mscIpivcLcnVcFastSelectCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcFastSelectCall.setStatus("mandatory")


class _MscIpivcLcnVcLocalRxPktSize_Type(Integer32):
    """Custom type mscIpivcLcnVcLocalRxPktSize based on Integer32"""
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


_MscIpivcLcnVcLocalRxPktSize_Type.__name__ = "Integer32"
_MscIpivcLcnVcLocalRxPktSize_Object = MibTableColumn
mscIpivcLcnVcLocalRxPktSize = _MscIpivcLcnVcLocalRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 14),
    _MscIpivcLcnVcLocalRxPktSize_Type()
)
mscIpivcLcnVcLocalRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcLocalRxPktSize.setStatus("mandatory")


class _MscIpivcLcnVcLocalTxPktSize_Type(Integer32):
    """Custom type mscIpivcLcnVcLocalTxPktSize based on Integer32"""
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


_MscIpivcLcnVcLocalTxPktSize_Type.__name__ = "Integer32"
_MscIpivcLcnVcLocalTxPktSize_Object = MibTableColumn
mscIpivcLcnVcLocalTxPktSize = _MscIpivcLcnVcLocalTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 15),
    _MscIpivcLcnVcLocalTxPktSize_Type()
)
mscIpivcLcnVcLocalTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcLocalTxPktSize.setStatus("mandatory")


class _MscIpivcLcnVcLocalTxWindowSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcLocalTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscIpivcLcnVcLocalTxWindowSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcLocalTxWindowSize_Object = MibTableColumn
mscIpivcLcnVcLocalTxWindowSize = _MscIpivcLcnVcLocalTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 16),
    _MscIpivcLcnVcLocalTxWindowSize_Type()
)
mscIpivcLcnVcLocalTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcLocalTxWindowSize.setStatus("mandatory")


class _MscIpivcLcnVcLocalRxWindowSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcLocalRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MscIpivcLcnVcLocalRxWindowSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcLocalRxWindowSize_Object = MibTableColumn
mscIpivcLcnVcLocalRxWindowSize = _MscIpivcLcnVcLocalRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 17),
    _MscIpivcLcnVcLocalRxWindowSize_Type()
)
mscIpivcLcnVcLocalRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcLocalRxWindowSize.setStatus("mandatory")


class _MscIpivcLcnVcPathReliability_Type(Integer32):
    """Custom type mscIpivcLcnVcPathReliability based on Integer32"""
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


_MscIpivcLcnVcPathReliability_Type.__name__ = "Integer32"
_MscIpivcLcnVcPathReliability_Object = MibTableColumn
mscIpivcLcnVcPathReliability = _MscIpivcLcnVcPathReliability_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 19),
    _MscIpivcLcnVcPathReliability_Type()
)
mscIpivcLcnVcPathReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPathReliability.setStatus("mandatory")


class _MscIpivcLcnVcAccountingEnd_Type(Integer32):
    """Custom type mscIpivcLcnVcAccountingEnd based on Integer32"""
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


_MscIpivcLcnVcAccountingEnd_Type.__name__ = "Integer32"
_MscIpivcLcnVcAccountingEnd_Object = MibTableColumn
mscIpivcLcnVcAccountingEnd = _MscIpivcLcnVcAccountingEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 20),
    _MscIpivcLcnVcAccountingEnd_Type()
)
mscIpivcLcnVcAccountingEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcAccountingEnd.setStatus("mandatory")


class _MscIpivcLcnVcPriority_Type(Integer32):
    """Custom type mscIpivcLcnVcPriority based on Integer32"""
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


_MscIpivcLcnVcPriority_Type.__name__ = "Integer32"
_MscIpivcLcnVcPriority_Object = MibTableColumn
mscIpivcLcnVcPriority = _MscIpivcLcnVcPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 21),
    _MscIpivcLcnVcPriority_Type()
)
mscIpivcLcnVcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPriority.setStatus("mandatory")


class _MscIpivcLcnVcSegmentSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcSegmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscIpivcLcnVcSegmentSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcSegmentSize_Object = MibTableColumn
mscIpivcLcnVcSegmentSize = _MscIpivcLcnVcSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 22),
    _MscIpivcLcnVcSegmentSize_Type()
)
mscIpivcLcnVcSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSegmentSize.setStatus("mandatory")


class _MscIpivcLcnVcSubnetTxPktSize_Type(Integer32):
    """Custom type mscIpivcLcnVcSubnetTxPktSize based on Integer32"""
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


_MscIpivcLcnVcSubnetTxPktSize_Type.__name__ = "Integer32"
_MscIpivcLcnVcSubnetTxPktSize_Object = MibTableColumn
mscIpivcLcnVcSubnetTxPktSize = _MscIpivcLcnVcSubnetTxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 23),
    _MscIpivcLcnVcSubnetTxPktSize_Type()
)
mscIpivcLcnVcSubnetTxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSubnetTxPktSize.setStatus("mandatory")


class _MscIpivcLcnVcSubnetTxWindowSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcSubnetTxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscIpivcLcnVcSubnetTxWindowSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcSubnetTxWindowSize_Object = MibTableColumn
mscIpivcLcnVcSubnetTxWindowSize = _MscIpivcLcnVcSubnetTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 24),
    _MscIpivcLcnVcSubnetTxWindowSize_Type()
)
mscIpivcLcnVcSubnetTxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSubnetTxWindowSize.setStatus("mandatory")


class _MscIpivcLcnVcSubnetRxPktSize_Type(Integer32):
    """Custom type mscIpivcLcnVcSubnetRxPktSize based on Integer32"""
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


_MscIpivcLcnVcSubnetRxPktSize_Type.__name__ = "Integer32"
_MscIpivcLcnVcSubnetRxPktSize_Object = MibTableColumn
mscIpivcLcnVcSubnetRxPktSize = _MscIpivcLcnVcSubnetRxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 25),
    _MscIpivcLcnVcSubnetRxPktSize_Type()
)
mscIpivcLcnVcSubnetRxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSubnetRxPktSize.setStatus("mandatory")


class _MscIpivcLcnVcSubnetRxWindowSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcSubnetRxWindowSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscIpivcLcnVcSubnetRxWindowSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcSubnetRxWindowSize_Object = MibTableColumn
mscIpivcLcnVcSubnetRxWindowSize = _MscIpivcLcnVcSubnetRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 26),
    _MscIpivcLcnVcSubnetRxWindowSize_Type()
)
mscIpivcLcnVcSubnetRxWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSubnetRxWindowSize.setStatus("mandatory")


class _MscIpivcLcnVcMaxSubnetPktSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcMaxSubnetPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MscIpivcLcnVcMaxSubnetPktSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcMaxSubnetPktSize_Object = MibTableColumn
mscIpivcLcnVcMaxSubnetPktSize = _MscIpivcLcnVcMaxSubnetPktSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 27),
    _MscIpivcLcnVcMaxSubnetPktSize_Type()
)
mscIpivcLcnVcMaxSubnetPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcMaxSubnetPktSize.setStatus("mandatory")


class _MscIpivcLcnVcTransferPriorityToNetwork_Type(Integer32):
    """Custom type mscIpivcLcnVcTransferPriorityToNetwork based on Integer32"""
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


_MscIpivcLcnVcTransferPriorityToNetwork_Type.__name__ = "Integer32"
_MscIpivcLcnVcTransferPriorityToNetwork_Object = MibTableColumn
mscIpivcLcnVcTransferPriorityToNetwork = _MscIpivcLcnVcTransferPriorityToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 28),
    _MscIpivcLcnVcTransferPriorityToNetwork_Type()
)
mscIpivcLcnVcTransferPriorityToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcTransferPriorityToNetwork.setStatus("mandatory")


class _MscIpivcLcnVcTransferPriorityFromNetwork_Type(Integer32):
    """Custom type mscIpivcLcnVcTransferPriorityFromNetwork based on Integer32"""
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


_MscIpivcLcnVcTransferPriorityFromNetwork_Type.__name__ = "Integer32"
_MscIpivcLcnVcTransferPriorityFromNetwork_Object = MibTableColumn
mscIpivcLcnVcTransferPriorityFromNetwork = _MscIpivcLcnVcTransferPriorityFromNetwork_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 10, 1, 29),
    _MscIpivcLcnVcTransferPriorityFromNetwork_Type()
)
mscIpivcLcnVcTransferPriorityFromNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcTransferPriorityFromNetwork.setStatus("mandatory")
_MscIpivcLcnVcIntdTable_Object = MibTable
mscIpivcLcnVcIntdTable = _MscIpivcLcnVcIntdTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11)
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcIntdTable.setStatus("mandatory")
_MscIpivcLcnVcIntdEntry_Object = MibTableRow
mscIpivcLcnVcIntdEntry = _MscIpivcLcnVcIntdEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11, 1)
)
mscIpivcLcnVcIntdEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcIntdEntry.setStatus("mandatory")


class _MscIpivcLcnVcCallReferenceNumber_Type(Hex):
    """Custom type mscIpivcLcnVcCallReferenceNumber based on Hex"""
    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpivcLcnVcCallReferenceNumber_Type.__name__ = "Hex"
_MscIpivcLcnVcCallReferenceNumber_Object = MibTableColumn
mscIpivcLcnVcCallReferenceNumber = _MscIpivcLcnVcCallReferenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11, 1, 1),
    _MscIpivcLcnVcCallReferenceNumber_Type()
)
mscIpivcLcnVcCallReferenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCallReferenceNumber.setStatus("obsolete")


class _MscIpivcLcnVcElapsedTimeTillNow_Type(Unsigned32):
    """Custom type mscIpivcLcnVcElapsedTimeTillNow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpivcLcnVcElapsedTimeTillNow_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcElapsedTimeTillNow_Object = MibTableColumn
mscIpivcLcnVcElapsedTimeTillNow = _MscIpivcLcnVcElapsedTimeTillNow_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11, 1, 2),
    _MscIpivcLcnVcElapsedTimeTillNow_Type()
)
mscIpivcLcnVcElapsedTimeTillNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcElapsedTimeTillNow.setStatus("mandatory")


class _MscIpivcLcnVcSegmentsRx_Type(Unsigned32):
    """Custom type mscIpivcLcnVcSegmentsRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpivcLcnVcSegmentsRx_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcSegmentsRx_Object = MibTableColumn
mscIpivcLcnVcSegmentsRx = _MscIpivcLcnVcSegmentsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11, 1, 3),
    _MscIpivcLcnVcSegmentsRx_Type()
)
mscIpivcLcnVcSegmentsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSegmentsRx.setStatus("mandatory")


class _MscIpivcLcnVcSegmentsSent_Type(Unsigned32):
    """Custom type mscIpivcLcnVcSegmentsSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_MscIpivcLcnVcSegmentsSent_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcSegmentsSent_Object = MibTableColumn
mscIpivcLcnVcSegmentsSent = _MscIpivcLcnVcSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11, 1, 4),
    _MscIpivcLcnVcSegmentsSent_Type()
)
mscIpivcLcnVcSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSegmentsSent.setStatus("mandatory")


class _MscIpivcLcnVcStartTime_Type(EnterpriseDateAndTime):
    """Custom type mscIpivcLcnVcStartTime based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(19, 19),
    )


_MscIpivcLcnVcStartTime_Type.__name__ = "EnterpriseDateAndTime"
_MscIpivcLcnVcStartTime_Object = MibTableColumn
mscIpivcLcnVcStartTime = _MscIpivcLcnVcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11, 1, 5),
    _MscIpivcLcnVcStartTime_Type()
)
mscIpivcLcnVcStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcStartTime.setStatus("mandatory")


class _MscIpivcLcnVcCallReferenceNumberDecimal_Type(Unsigned32):
    """Custom type mscIpivcLcnVcCallReferenceNumberDecimal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscIpivcLcnVcCallReferenceNumberDecimal_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcCallReferenceNumberDecimal_Object = MibTableColumn
mscIpivcLcnVcCallReferenceNumberDecimal = _MscIpivcLcnVcCallReferenceNumberDecimal_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 11, 1, 7),
    _MscIpivcLcnVcCallReferenceNumberDecimal_Type()
)
mscIpivcLcnVcCallReferenceNumberDecimal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcCallReferenceNumberDecimal.setStatus("mandatory")
_MscIpivcLcnVcStatsTable_Object = MibTable
mscIpivcLcnVcStatsTable = _MscIpivcLcnVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12)
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcStatsTable.setStatus("mandatory")
_MscIpivcLcnVcStatsEntry_Object = MibTableRow
mscIpivcLcnVcStatsEntry = _MscIpivcLcnVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1)
)
mscIpivcLcnVcStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnVcIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcLcnVcStatsEntry.setStatus("mandatory")


class _MscIpivcLcnVcAckStackingTimeouts_Type(Unsigned32):
    """Custom type mscIpivcLcnVcAckStackingTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcAckStackingTimeouts_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcAckStackingTimeouts_Object = MibTableColumn
mscIpivcLcnVcAckStackingTimeouts = _MscIpivcLcnVcAckStackingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 1),
    _MscIpivcLcnVcAckStackingTimeouts_Type()
)
mscIpivcLcnVcAckStackingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcAckStackingTimeouts.setStatus("mandatory")


class _MscIpivcLcnVcOutOfRangeFrmFromSubnet_Type(Unsigned32):
    """Custom type mscIpivcLcnVcOutOfRangeFrmFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcOutOfRangeFrmFromSubnet_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcOutOfRangeFrmFromSubnet_Object = MibTableColumn
mscIpivcLcnVcOutOfRangeFrmFromSubnet = _MscIpivcLcnVcOutOfRangeFrmFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 2),
    _MscIpivcLcnVcOutOfRangeFrmFromSubnet_Type()
)
mscIpivcLcnVcOutOfRangeFrmFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcOutOfRangeFrmFromSubnet.setStatus("mandatory")


class _MscIpivcLcnVcDuplicatesFromSubnet_Type(Unsigned32):
    """Custom type mscIpivcLcnVcDuplicatesFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcDuplicatesFromSubnet_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcDuplicatesFromSubnet_Object = MibTableColumn
mscIpivcLcnVcDuplicatesFromSubnet = _MscIpivcLcnVcDuplicatesFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 3),
    _MscIpivcLcnVcDuplicatesFromSubnet_Type()
)
mscIpivcLcnVcDuplicatesFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcDuplicatesFromSubnet.setStatus("mandatory")


class _MscIpivcLcnVcFrmRetryTimeouts_Type(Unsigned32):
    """Custom type mscIpivcLcnVcFrmRetryTimeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcFrmRetryTimeouts_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcFrmRetryTimeouts_Object = MibTableColumn
mscIpivcLcnVcFrmRetryTimeouts = _MscIpivcLcnVcFrmRetryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 4),
    _MscIpivcLcnVcFrmRetryTimeouts_Type()
)
mscIpivcLcnVcFrmRetryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcFrmRetryTimeouts.setStatus("mandatory")


class _MscIpivcLcnVcPeakRetryQueueSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcPeakRetryQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcPeakRetryQueueSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcPeakRetryQueueSize_Object = MibTableColumn
mscIpivcLcnVcPeakRetryQueueSize = _MscIpivcLcnVcPeakRetryQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 5),
    _MscIpivcLcnVcPeakRetryQueueSize_Type()
)
mscIpivcLcnVcPeakRetryQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPeakRetryQueueSize.setStatus("mandatory")


class _MscIpivcLcnVcPeakOoSeqQueueSize_Type(Unsigned32):
    """Custom type mscIpivcLcnVcPeakOoSeqQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcPeakOoSeqQueueSize_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcPeakOoSeqQueueSize_Object = MibTableColumn
mscIpivcLcnVcPeakOoSeqQueueSize = _MscIpivcLcnVcPeakOoSeqQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 6),
    _MscIpivcLcnVcPeakOoSeqQueueSize_Type()
)
mscIpivcLcnVcPeakOoSeqQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPeakOoSeqQueueSize.setStatus("mandatory")


class _MscIpivcLcnVcPeakOoSeqFrmForwarded_Type(Unsigned32):
    """Custom type mscIpivcLcnVcPeakOoSeqFrmForwarded based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcPeakOoSeqFrmForwarded_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcPeakOoSeqFrmForwarded_Object = MibTableColumn
mscIpivcLcnVcPeakOoSeqFrmForwarded = _MscIpivcLcnVcPeakOoSeqFrmForwarded_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 7),
    _MscIpivcLcnVcPeakOoSeqFrmForwarded_Type()
)
mscIpivcLcnVcPeakOoSeqFrmForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPeakOoSeqFrmForwarded.setStatus("mandatory")


class _MscIpivcLcnVcPeakStackedAcksRx_Type(Unsigned32):
    """Custom type mscIpivcLcnVcPeakStackedAcksRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcPeakStackedAcksRx_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcPeakStackedAcksRx_Object = MibTableColumn
mscIpivcLcnVcPeakStackedAcksRx = _MscIpivcLcnVcPeakStackedAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 8),
    _MscIpivcLcnVcPeakStackedAcksRx_Type()
)
mscIpivcLcnVcPeakStackedAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcPeakStackedAcksRx.setStatus("mandatory")


class _MscIpivcLcnVcSubnetRecoveries_Type(Unsigned32):
    """Custom type mscIpivcLcnVcSubnetRecoveries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcSubnetRecoveries_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcSubnetRecoveries_Object = MibTableColumn
mscIpivcLcnVcSubnetRecoveries = _MscIpivcLcnVcSubnetRecoveries_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 9),
    _MscIpivcLcnVcSubnetRecoveries_Type()
)
mscIpivcLcnVcSubnetRecoveries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcSubnetRecoveries.setStatus("mandatory")


class _MscIpivcLcnVcWindowClosuresToSubnet_Type(Unsigned32):
    """Custom type mscIpivcLcnVcWindowClosuresToSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcWindowClosuresToSubnet_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcWindowClosuresToSubnet_Object = MibTableColumn
mscIpivcLcnVcWindowClosuresToSubnet = _MscIpivcLcnVcWindowClosuresToSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 10),
    _MscIpivcLcnVcWindowClosuresToSubnet_Type()
)
mscIpivcLcnVcWindowClosuresToSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcWindowClosuresToSubnet.setStatus("mandatory")


class _MscIpivcLcnVcWindowClosuresFromSubnet_Type(Unsigned32):
    """Custom type mscIpivcLcnVcWindowClosuresFromSubnet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcWindowClosuresFromSubnet_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcWindowClosuresFromSubnet_Object = MibTableColumn
mscIpivcLcnVcWindowClosuresFromSubnet = _MscIpivcLcnVcWindowClosuresFromSubnet_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 11),
    _MscIpivcLcnVcWindowClosuresFromSubnet_Type()
)
mscIpivcLcnVcWindowClosuresFromSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcWindowClosuresFromSubnet.setStatus("mandatory")


class _MscIpivcLcnVcWrTriggers_Type(Unsigned32):
    """Custom type mscIpivcLcnVcWrTriggers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_MscIpivcLcnVcWrTriggers_Type.__name__ = "Unsigned32"
_MscIpivcLcnVcWrTriggers_Object = MibTableColumn
mscIpivcLcnVcWrTriggers = _MscIpivcLcnVcWrTriggers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 2, 12, 1, 12),
    _MscIpivcLcnVcWrTriggers_Type()
)
mscIpivcLcnVcWrTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnVcWrTriggers.setStatus("mandatory")
_MscIpivcLcnStateTable_Object = MibTable
mscIpivcLcnStateTable = _MscIpivcLcnStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10)
)
if mibBuilder.loadTexts:
    mscIpivcLcnStateTable.setStatus("mandatory")
_MscIpivcLcnStateEntry_Object = MibTableRow
mscIpivcLcnStateEntry = _MscIpivcLcnStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1)
)
mscIpivcLcnStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcLcnStateEntry.setStatus("mandatory")


class _MscIpivcLcnAdminState_Type(Integer32):
    """Custom type mscIpivcLcnAdminState based on Integer32"""
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


_MscIpivcLcnAdminState_Type.__name__ = "Integer32"
_MscIpivcLcnAdminState_Object = MibTableColumn
mscIpivcLcnAdminState = _MscIpivcLcnAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 1),
    _MscIpivcLcnAdminState_Type()
)
mscIpivcLcnAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnAdminState.setStatus("mandatory")


class _MscIpivcLcnOperationalState_Type(Integer32):
    """Custom type mscIpivcLcnOperationalState based on Integer32"""
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


_MscIpivcLcnOperationalState_Type.__name__ = "Integer32"
_MscIpivcLcnOperationalState_Object = MibTableColumn
mscIpivcLcnOperationalState = _MscIpivcLcnOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 2),
    _MscIpivcLcnOperationalState_Type()
)
mscIpivcLcnOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnOperationalState.setStatus("mandatory")


class _MscIpivcLcnUsageState_Type(Integer32):
    """Custom type mscIpivcLcnUsageState based on Integer32"""
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


_MscIpivcLcnUsageState_Type.__name__ = "Integer32"
_MscIpivcLcnUsageState_Object = MibTableColumn
mscIpivcLcnUsageState = _MscIpivcLcnUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 3),
    _MscIpivcLcnUsageState_Type()
)
mscIpivcLcnUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnUsageState.setStatus("mandatory")


class _MscIpivcLcnAvailabilityStatus_Type(OctetString):
    """Custom type mscIpivcLcnAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscIpivcLcnAvailabilityStatus_Type.__name__ = "OctetString"
_MscIpivcLcnAvailabilityStatus_Object = MibTableColumn
mscIpivcLcnAvailabilityStatus = _MscIpivcLcnAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 4),
    _MscIpivcLcnAvailabilityStatus_Type()
)
mscIpivcLcnAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnAvailabilityStatus.setStatus("mandatory")


class _MscIpivcLcnProceduralStatus_Type(OctetString):
    """Custom type mscIpivcLcnProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscIpivcLcnProceduralStatus_Type.__name__ = "OctetString"
_MscIpivcLcnProceduralStatus_Object = MibTableColumn
mscIpivcLcnProceduralStatus = _MscIpivcLcnProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 5),
    _MscIpivcLcnProceduralStatus_Type()
)
mscIpivcLcnProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnProceduralStatus.setStatus("mandatory")


class _MscIpivcLcnControlStatus_Type(OctetString):
    """Custom type mscIpivcLcnControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscIpivcLcnControlStatus_Type.__name__ = "OctetString"
_MscIpivcLcnControlStatus_Object = MibTableColumn
mscIpivcLcnControlStatus = _MscIpivcLcnControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 6),
    _MscIpivcLcnControlStatus_Type()
)
mscIpivcLcnControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnControlStatus.setStatus("mandatory")


class _MscIpivcLcnAlarmStatus_Type(OctetString):
    """Custom type mscIpivcLcnAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscIpivcLcnAlarmStatus_Type.__name__ = "OctetString"
_MscIpivcLcnAlarmStatus_Object = MibTableColumn
mscIpivcLcnAlarmStatus = _MscIpivcLcnAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 7),
    _MscIpivcLcnAlarmStatus_Type()
)
mscIpivcLcnAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnAlarmStatus.setStatus("mandatory")


class _MscIpivcLcnStandbyStatus_Type(Integer32):
    """Custom type mscIpivcLcnStandbyStatus based on Integer32"""
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


_MscIpivcLcnStandbyStatus_Type.__name__ = "Integer32"
_MscIpivcLcnStandbyStatus_Object = MibTableColumn
mscIpivcLcnStandbyStatus = _MscIpivcLcnStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 8),
    _MscIpivcLcnStandbyStatus_Type()
)
mscIpivcLcnStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnStandbyStatus.setStatus("mandatory")


class _MscIpivcLcnUnknownStatus_Type(Integer32):
    """Custom type mscIpivcLcnUnknownStatus based on Integer32"""
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


_MscIpivcLcnUnknownStatus_Type.__name__ = "Integer32"
_MscIpivcLcnUnknownStatus_Object = MibTableColumn
mscIpivcLcnUnknownStatus = _MscIpivcLcnUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 10, 1, 9),
    _MscIpivcLcnUnknownStatus_Type()
)
mscIpivcLcnUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnUnknownStatus.setStatus("mandatory")
_MscIpivcLcnOperTable_Object = MibTable
mscIpivcLcnOperTable = _MscIpivcLcnOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11)
)
if mibBuilder.loadTexts:
    mscIpivcLcnOperTable.setStatus("mandatory")
_MscIpivcLcnOperEntry_Object = MibTableRow
mscIpivcLcnOperEntry = _MscIpivcLcnOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11, 1)
)
mscIpivcLcnOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcLcnIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcLcnOperEntry.setStatus("mandatory")


class _MscIpivcLcnIpInterfaceDevice_Type(Integer32):
    """Custom type mscIpivcLcnIpInterfaceDevice based on Integer32"""
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


_MscIpivcLcnIpInterfaceDevice_Type.__name__ = "Integer32"
_MscIpivcLcnIpInterfaceDevice_Object = MibTableColumn
mscIpivcLcnIpInterfaceDevice = _MscIpivcLcnIpInterfaceDevice_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11, 1, 1),
    _MscIpivcLcnIpInterfaceDevice_Type()
)
mscIpivcLcnIpInterfaceDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnIpInterfaceDevice.setStatus("mandatory")


class _MscIpivcLcnDestinationIpAddress_Type(IpAddress):
    """Custom type mscIpivcLcnDestinationIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpivcLcnDestinationIpAddress_Object = MibTableColumn
mscIpivcLcnDestinationIpAddress = _MscIpivcLcnDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11, 1, 2),
    _MscIpivcLcnDestinationIpAddress_Type()
)
mscIpivcLcnDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnDestinationIpAddress.setStatus("mandatory")
_MscIpivcLcnPacketsSent_Type = Counter32
_MscIpivcLcnPacketsSent_Object = MibTableColumn
mscIpivcLcnPacketsSent = _MscIpivcLcnPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11, 1, 3),
    _MscIpivcLcnPacketsSent_Type()
)
mscIpivcLcnPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnPacketsSent.setStatus("mandatory")
_MscIpivcLcnPacketsReceived_Type = Counter32
_MscIpivcLcnPacketsReceived_Object = MibTableColumn
mscIpivcLcnPacketsReceived = _MscIpivcLcnPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11, 1, 4),
    _MscIpivcLcnPacketsReceived_Type()
)
mscIpivcLcnPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnPacketsReceived.setStatus("mandatory")
_MscIpivcLcnDiscardTxPackets_Type = Counter32
_MscIpivcLcnDiscardTxPackets_Object = MibTableColumn
mscIpivcLcnDiscardTxPackets = _MscIpivcLcnDiscardTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11, 1, 5),
    _MscIpivcLcnDiscardTxPackets_Type()
)
mscIpivcLcnDiscardTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnDiscardTxPackets.setStatus("mandatory")
_MscIpivcLcnDiscardRcvPackets_Type = Counter32
_MscIpivcLcnDiscardRcvPackets_Object = MibTableColumn
mscIpivcLcnDiscardRcvPackets = _MscIpivcLcnDiscardRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 4, 11, 1, 6),
    _MscIpivcLcnDiscardRcvPackets_Type()
)
mscIpivcLcnDiscardRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcLcnDiscardRcvPackets.setStatus("mandatory")
_MscIpivcProvTable_Object = MibTable
mscIpivcProvTable = _MscIpivcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 10)
)
if mibBuilder.loadTexts:
    mscIpivcProvTable.setStatus("mandatory")
_MscIpivcProvEntry_Object = MibTableRow
mscIpivcProvEntry = _MscIpivcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 10, 1)
)
mscIpivcProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-IpiVcMIB", "mscIpivcIndex"),
)
if mibBuilder.loadTexts:
    mscIpivcProvEntry.setStatus("mandatory")


class _MscIpivcIpAddress_Type(IpAddress):
    """Custom type mscIpivcIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscIpivcIpAddress_Object = MibTableColumn
mscIpivcIpAddress = _MscIpivcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 10, 1, 1),
    _MscIpivcIpAddress_Type()
)
mscIpivcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscIpivcIpAddress.setStatus("mandatory")


class _MscIpivcMaximumNumberOfLcn_Type(Unsigned32):
    """Custom type mscIpivcMaximumNumberOfLcn based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 24),
    )


_MscIpivcMaximumNumberOfLcn_Type.__name__ = "Unsigned32"
_MscIpivcMaximumNumberOfLcn_Object = MibTableColumn
mscIpivcMaximumNumberOfLcn = _MscIpivcMaximumNumberOfLcn_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 51, 10, 1, 2),
    _MscIpivcMaximumNumberOfLcn_Type()
)
mscIpivcMaximumNumberOfLcn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscIpivcMaximumNumberOfLcn.setStatus("mandatory")
_IpiVcMIB_ObjectIdentity = ObjectIdentity
ipiVcMIB = _IpiVcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53)
)
_IpiVcGroup_ObjectIdentity = ObjectIdentity
ipiVcGroup = _IpiVcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 1)
)
_IpiVcGroupCA_ObjectIdentity = ObjectIdentity
ipiVcGroupCA = _IpiVcGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 1, 1)
)
_IpiVcGroupCA02_ObjectIdentity = ObjectIdentity
ipiVcGroupCA02 = _IpiVcGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 1, 1, 3)
)
_IpiVcGroupCA02A_ObjectIdentity = ObjectIdentity
ipiVcGroupCA02A = _IpiVcGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 1, 1, 3, 2)
)
_IpiVcCapabilities_ObjectIdentity = ObjectIdentity
ipiVcCapabilities = _IpiVcCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 3)
)
_IpiVcCapabilitiesCA_ObjectIdentity = ObjectIdentity
ipiVcCapabilitiesCA = _IpiVcCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 3, 1)
)
_IpiVcCapabilitiesCA02_ObjectIdentity = ObjectIdentity
ipiVcCapabilitiesCA02 = _IpiVcCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 3, 1, 3)
)
_IpiVcCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
ipiVcCapabilitiesCA02A = _IpiVcCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 53, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-IpiVcMIB",
    **{"mscIpivc": mscIpivc,
       "mscIpivcRowStatusTable": mscIpivcRowStatusTable,
       "mscIpivcRowStatusEntry": mscIpivcRowStatusEntry,
       "mscIpivcRowStatus": mscIpivcRowStatus,
       "mscIpivcComponentName": mscIpivcComponentName,
       "mscIpivcStorageType": mscIpivcStorageType,
       "mscIpivcIndex": mscIpivcIndex,
       "mscIpivcDna": mscIpivcDna,
       "mscIpivcDnaRowStatusTable": mscIpivcDnaRowStatusTable,
       "mscIpivcDnaRowStatusEntry": mscIpivcDnaRowStatusEntry,
       "mscIpivcDnaRowStatus": mscIpivcDnaRowStatus,
       "mscIpivcDnaComponentName": mscIpivcDnaComponentName,
       "mscIpivcDnaStorageType": mscIpivcDnaStorageType,
       "mscIpivcDnaIndex": mscIpivcDnaIndex,
       "mscIpivcDnaCug": mscIpivcDnaCug,
       "mscIpivcDnaCugRowStatusTable": mscIpivcDnaCugRowStatusTable,
       "mscIpivcDnaCugRowStatusEntry": mscIpivcDnaCugRowStatusEntry,
       "mscIpivcDnaCugRowStatus": mscIpivcDnaCugRowStatus,
       "mscIpivcDnaCugComponentName": mscIpivcDnaCugComponentName,
       "mscIpivcDnaCugStorageType": mscIpivcDnaCugStorageType,
       "mscIpivcDnaCugIndex": mscIpivcDnaCugIndex,
       "mscIpivcDnaCugCugOptionsTable": mscIpivcDnaCugCugOptionsTable,
       "mscIpivcDnaCugCugOptionsEntry": mscIpivcDnaCugCugOptionsEntry,
       "mscIpivcDnaCugType": mscIpivcDnaCugType,
       "mscIpivcDnaCugDnic": mscIpivcDnaCugDnic,
       "mscIpivcDnaCugInterlockCode": mscIpivcDnaCugInterlockCode,
       "mscIpivcDnaCugOutCalls": mscIpivcDnaCugOutCalls,
       "mscIpivcDnaCugIncCalls": mscIpivcDnaCugIncCalls,
       "mscIpivcDnaCugPrivileged": mscIpivcDnaCugPrivileged,
       "mscIpivcDnaAddressTable": mscIpivcDnaAddressTable,
       "mscIpivcDnaAddressEntry": mscIpivcDnaAddressEntry,
       "mscIpivcDnaNumberingPlanIndicator": mscIpivcDnaNumberingPlanIndicator,
       "mscIpivcDnaDataNetworkAddress": mscIpivcDnaDataNetworkAddress,
       "mscIpivcDnaOutgoingOptionsTable": mscIpivcDnaOutgoingOptionsTable,
       "mscIpivcDnaOutgoingOptionsEntry": mscIpivcDnaOutgoingOptionsEntry,
       "mscIpivcDnaOutCalls": mscIpivcDnaOutCalls,
       "mscIpivcDnaOutDefaultPathSensitivity": mscIpivcDnaOutDefaultPathSensitivity,
       "mscIpivcDnaOutPathSensitivityOverRide": mscIpivcDnaOutPathSensitivityOverRide,
       "mscIpivcDnaDefaultTransferPriority": mscIpivcDnaDefaultTransferPriority,
       "mscIpivcDnaTransferPriorityOverRide": mscIpivcDnaTransferPriorityOverRide,
       "mscIpivcDnaIncomingOptionsTable": mscIpivcDnaIncomingOptionsTable,
       "mscIpivcDnaIncomingOptionsEntry": mscIpivcDnaIncomingOptionsEntry,
       "mscIpivcDnaIncCalls": mscIpivcDnaIncCalls,
       "mscIpivcDnaIncHighPriorityReverseCharge": mscIpivcDnaIncHighPriorityReverseCharge,
       "mscIpivcDnaIncNormalPriorityReverseCharge": mscIpivcDnaIncNormalPriorityReverseCharge,
       "mscIpivcDnaIncIntlNormalCharge": mscIpivcDnaIncIntlNormalCharge,
       "mscIpivcDnaIncIntlReverseCharge": mscIpivcDnaIncIntlReverseCharge,
       "mscIpivcDnaIncFastSelect": mscIpivcDnaIncFastSelect,
       "mscIpivcDnaIncSameService": mscIpivcDnaIncSameService,
       "mscIpivcDnaIncChargeTransfer": mscIpivcDnaIncChargeTransfer,
       "mscIpivcDnaIncAccess": mscIpivcDnaIncAccess,
       "mscIpivcDnaCallOptionsTable": mscIpivcDnaCallOptionsTable,
       "mscIpivcDnaCallOptionsEntry": mscIpivcDnaCallOptionsEntry,
       "mscIpivcDnaServiceCategory": mscIpivcDnaServiceCategory,
       "mscIpivcDnaPacketSizes": mscIpivcDnaPacketSizes,
       "mscIpivcDnaDefaultRecvFrmNetworkPacketSize": mscIpivcDnaDefaultRecvFrmNetworkPacketSize,
       "mscIpivcDnaDefaultSendToNetworkPacketSize": mscIpivcDnaDefaultSendToNetworkPacketSize,
       "mscIpivcDnaDefaultRecvFrmNetworkThruputClass": mscIpivcDnaDefaultRecvFrmNetworkThruputClass,
       "mscIpivcDnaDefaultSendToNetworkThruputClass": mscIpivcDnaDefaultSendToNetworkThruputClass,
       "mscIpivcDnaDefaultRecvFrmNetworkWindowSize": mscIpivcDnaDefaultRecvFrmNetworkWindowSize,
       "mscIpivcDnaDefaultSendToNetworkWindowSize": mscIpivcDnaDefaultSendToNetworkWindowSize,
       "mscIpivcDnaPacketSizeNegotiation": mscIpivcDnaPacketSizeNegotiation,
       "mscIpivcDnaAccountClass": mscIpivcDnaAccountClass,
       "mscIpivcDnaServiceExchange": mscIpivcDnaServiceExchange,
       "mscIpivcDnaCugFormat": mscIpivcDnaCugFormat,
       "mscIpivcDnaCug0AsNonCugCall": mscIpivcDnaCug0AsNonCugCall,
       "mscIpivcDnaFastSelectCallsOnly": mscIpivcDnaFastSelectCallsOnly,
       "mscIpivcDr": mscIpivcDr,
       "mscIpivcDrRowStatusTable": mscIpivcDrRowStatusTable,
       "mscIpivcDrRowStatusEntry": mscIpivcDrRowStatusEntry,
       "mscIpivcDrRowStatus": mscIpivcDrRowStatus,
       "mscIpivcDrComponentName": mscIpivcDrComponentName,
       "mscIpivcDrStorageType": mscIpivcDrStorageType,
       "mscIpivcDrIndex": mscIpivcDrIndex,
       "mscIpivcDrProvTable": mscIpivcDrProvTable,
       "mscIpivcDrProvEntry": mscIpivcDrProvEntry,
       "mscIpivcDrCallingIpAddress": mscIpivcDrCallingIpAddress,
       "mscIpivcDrCallingNumberingPlanIndicator": mscIpivcDrCallingNumberingPlanIndicator,
       "mscIpivcDrCallingDataNetworkAddress": mscIpivcDrCallingDataNetworkAddress,
       "mscIpivcLcn": mscIpivcLcn,
       "mscIpivcLcnRowStatusTable": mscIpivcLcnRowStatusTable,
       "mscIpivcLcnRowStatusEntry": mscIpivcLcnRowStatusEntry,
       "mscIpivcLcnRowStatus": mscIpivcLcnRowStatus,
       "mscIpivcLcnComponentName": mscIpivcLcnComponentName,
       "mscIpivcLcnStorageType": mscIpivcLcnStorageType,
       "mscIpivcLcnIndex": mscIpivcLcnIndex,
       "mscIpivcLcnVc": mscIpivcLcnVc,
       "mscIpivcLcnVcRowStatusTable": mscIpivcLcnVcRowStatusTable,
       "mscIpivcLcnVcRowStatusEntry": mscIpivcLcnVcRowStatusEntry,
       "mscIpivcLcnVcRowStatus": mscIpivcLcnVcRowStatus,
       "mscIpivcLcnVcComponentName": mscIpivcLcnVcComponentName,
       "mscIpivcLcnVcStorageType": mscIpivcLcnVcStorageType,
       "mscIpivcLcnVcIndex": mscIpivcLcnVcIndex,
       "mscIpivcLcnVcCadTable": mscIpivcLcnVcCadTable,
       "mscIpivcLcnVcCadEntry": mscIpivcLcnVcCadEntry,
       "mscIpivcLcnVcType": mscIpivcLcnVcType,
       "mscIpivcLcnVcState": mscIpivcLcnVcState,
       "mscIpivcLcnVcPreviousState": mscIpivcLcnVcPreviousState,
       "mscIpivcLcnVcDiagnosticCode": mscIpivcLcnVcDiagnosticCode,
       "mscIpivcLcnVcPreviousDiagnosticCode": mscIpivcLcnVcPreviousDiagnosticCode,
       "mscIpivcLcnVcCalledNpi": mscIpivcLcnVcCalledNpi,
       "mscIpivcLcnVcCalledDna": mscIpivcLcnVcCalledDna,
       "mscIpivcLcnVcCalledLcn": mscIpivcLcnVcCalledLcn,
       "mscIpivcLcnVcCallingNpi": mscIpivcLcnVcCallingNpi,
       "mscIpivcLcnVcCallingDna": mscIpivcLcnVcCallingDna,
       "mscIpivcLcnVcCallingLcn": mscIpivcLcnVcCallingLcn,
       "mscIpivcLcnVcAccountingEnabled": mscIpivcLcnVcAccountingEnabled,
       "mscIpivcLcnVcFastSelectCall": mscIpivcLcnVcFastSelectCall,
       "mscIpivcLcnVcLocalRxPktSize": mscIpivcLcnVcLocalRxPktSize,
       "mscIpivcLcnVcLocalTxPktSize": mscIpivcLcnVcLocalTxPktSize,
       "mscIpivcLcnVcLocalTxWindowSize": mscIpivcLcnVcLocalTxWindowSize,
       "mscIpivcLcnVcLocalRxWindowSize": mscIpivcLcnVcLocalRxWindowSize,
       "mscIpivcLcnVcPathReliability": mscIpivcLcnVcPathReliability,
       "mscIpivcLcnVcAccountingEnd": mscIpivcLcnVcAccountingEnd,
       "mscIpivcLcnVcPriority": mscIpivcLcnVcPriority,
       "mscIpivcLcnVcSegmentSize": mscIpivcLcnVcSegmentSize,
       "mscIpivcLcnVcSubnetTxPktSize": mscIpivcLcnVcSubnetTxPktSize,
       "mscIpivcLcnVcSubnetTxWindowSize": mscIpivcLcnVcSubnetTxWindowSize,
       "mscIpivcLcnVcSubnetRxPktSize": mscIpivcLcnVcSubnetRxPktSize,
       "mscIpivcLcnVcSubnetRxWindowSize": mscIpivcLcnVcSubnetRxWindowSize,
       "mscIpivcLcnVcMaxSubnetPktSize": mscIpivcLcnVcMaxSubnetPktSize,
       "mscIpivcLcnVcTransferPriorityToNetwork": mscIpivcLcnVcTransferPriorityToNetwork,
       "mscIpivcLcnVcTransferPriorityFromNetwork": mscIpivcLcnVcTransferPriorityFromNetwork,
       "mscIpivcLcnVcIntdTable": mscIpivcLcnVcIntdTable,
       "mscIpivcLcnVcIntdEntry": mscIpivcLcnVcIntdEntry,
       "mscIpivcLcnVcCallReferenceNumber": mscIpivcLcnVcCallReferenceNumber,
       "mscIpivcLcnVcElapsedTimeTillNow": mscIpivcLcnVcElapsedTimeTillNow,
       "mscIpivcLcnVcSegmentsRx": mscIpivcLcnVcSegmentsRx,
       "mscIpivcLcnVcSegmentsSent": mscIpivcLcnVcSegmentsSent,
       "mscIpivcLcnVcStartTime": mscIpivcLcnVcStartTime,
       "mscIpivcLcnVcCallReferenceNumberDecimal": mscIpivcLcnVcCallReferenceNumberDecimal,
       "mscIpivcLcnVcStatsTable": mscIpivcLcnVcStatsTable,
       "mscIpivcLcnVcStatsEntry": mscIpivcLcnVcStatsEntry,
       "mscIpivcLcnVcAckStackingTimeouts": mscIpivcLcnVcAckStackingTimeouts,
       "mscIpivcLcnVcOutOfRangeFrmFromSubnet": mscIpivcLcnVcOutOfRangeFrmFromSubnet,
       "mscIpivcLcnVcDuplicatesFromSubnet": mscIpivcLcnVcDuplicatesFromSubnet,
       "mscIpivcLcnVcFrmRetryTimeouts": mscIpivcLcnVcFrmRetryTimeouts,
       "mscIpivcLcnVcPeakRetryQueueSize": mscIpivcLcnVcPeakRetryQueueSize,
       "mscIpivcLcnVcPeakOoSeqQueueSize": mscIpivcLcnVcPeakOoSeqQueueSize,
       "mscIpivcLcnVcPeakOoSeqFrmForwarded": mscIpivcLcnVcPeakOoSeqFrmForwarded,
       "mscIpivcLcnVcPeakStackedAcksRx": mscIpivcLcnVcPeakStackedAcksRx,
       "mscIpivcLcnVcSubnetRecoveries": mscIpivcLcnVcSubnetRecoveries,
       "mscIpivcLcnVcWindowClosuresToSubnet": mscIpivcLcnVcWindowClosuresToSubnet,
       "mscIpivcLcnVcWindowClosuresFromSubnet": mscIpivcLcnVcWindowClosuresFromSubnet,
       "mscIpivcLcnVcWrTriggers": mscIpivcLcnVcWrTriggers,
       "mscIpivcLcnStateTable": mscIpivcLcnStateTable,
       "mscIpivcLcnStateEntry": mscIpivcLcnStateEntry,
       "mscIpivcLcnAdminState": mscIpivcLcnAdminState,
       "mscIpivcLcnOperationalState": mscIpivcLcnOperationalState,
       "mscIpivcLcnUsageState": mscIpivcLcnUsageState,
       "mscIpivcLcnAvailabilityStatus": mscIpivcLcnAvailabilityStatus,
       "mscIpivcLcnProceduralStatus": mscIpivcLcnProceduralStatus,
       "mscIpivcLcnControlStatus": mscIpivcLcnControlStatus,
       "mscIpivcLcnAlarmStatus": mscIpivcLcnAlarmStatus,
       "mscIpivcLcnStandbyStatus": mscIpivcLcnStandbyStatus,
       "mscIpivcLcnUnknownStatus": mscIpivcLcnUnknownStatus,
       "mscIpivcLcnOperTable": mscIpivcLcnOperTable,
       "mscIpivcLcnOperEntry": mscIpivcLcnOperEntry,
       "mscIpivcLcnIpInterfaceDevice": mscIpivcLcnIpInterfaceDevice,
       "mscIpivcLcnDestinationIpAddress": mscIpivcLcnDestinationIpAddress,
       "mscIpivcLcnPacketsSent": mscIpivcLcnPacketsSent,
       "mscIpivcLcnPacketsReceived": mscIpivcLcnPacketsReceived,
       "mscIpivcLcnDiscardTxPackets": mscIpivcLcnDiscardTxPackets,
       "mscIpivcLcnDiscardRcvPackets": mscIpivcLcnDiscardRcvPackets,
       "mscIpivcProvTable": mscIpivcProvTable,
       "mscIpivcProvEntry": mscIpivcProvEntry,
       "mscIpivcIpAddress": mscIpivcIpAddress,
       "mscIpivcMaximumNumberOfLcn": mscIpivcMaximumNumberOfLcn,
       "ipiVcMIB": ipiVcMIB,
       "ipiVcGroup": ipiVcGroup,
       "ipiVcGroupCA": ipiVcGroupCA,
       "ipiVcGroupCA02": ipiVcGroupCA02,
       "ipiVcGroupCA02A": ipiVcGroupCA02A,
       "ipiVcCapabilities": ipiVcCapabilities,
       "ipiVcCapabilitiesCA": ipiVcCapabilitiesCA,
       "ipiVcCapabilitiesCA02": ipiVcCapabilitiesCA02,
       "ipiVcCapabilitiesCA02A": ipiVcCapabilitiesCA02A}
)
