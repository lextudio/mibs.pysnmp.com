# SNMP MIB module (Nortel-MsCarrier-MscPassport-VncsCallServerMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-VncsCallServerMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:16 2024
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
 FixedPoint1,
 Link,
 WildcardedDigitString) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "FixedPoint1",
    "Link",
    "WildcardedDigitString")

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

_MscVncs_ObjectIdentity = ObjectIdentity
mscVncs = _MscVncs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44)
)
_MscVncsRowStatusTable_Object = MibTable
mscVncsRowStatusTable = _MscVncsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 1)
)
if mibBuilder.loadTexts:
    mscVncsRowStatusTable.setStatus("mandatory")
_MscVncsRowStatusEntry_Object = MibTableRow
mscVncsRowStatusEntry = _MscVncsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 1, 1)
)
mscVncsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
)
if mibBuilder.loadTexts:
    mscVncsRowStatusEntry.setStatus("mandatory")
_MscVncsRowStatus_Type = RowStatus
_MscVncsRowStatus_Object = MibTableColumn
mscVncsRowStatus = _MscVncsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 1, 1, 1),
    _MscVncsRowStatus_Type()
)
mscVncsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsRowStatus.setStatus("mandatory")
_MscVncsComponentName_Type = DisplayString
_MscVncsComponentName_Object = MibTableColumn
mscVncsComponentName = _MscVncsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 1, 1, 2),
    _MscVncsComponentName_Type()
)
mscVncsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsComponentName.setStatus("mandatory")
_MscVncsStorageType_Type = StorageType
_MscVncsStorageType_Object = MibTableColumn
mscVncsStorageType = _MscVncsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 1, 1, 4),
    _MscVncsStorageType_Type()
)
mscVncsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsStorageType.setStatus("mandatory")


class _MscVncsIndex_Type(Integer32):
    """Custom type mscVncsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVncsIndex_Type.__name__ = "Integer32"
_MscVncsIndex_Object = MibTableColumn
mscVncsIndex = _MscVncsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 1, 1, 10),
    _MscVncsIndex_Type()
)
mscVncsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsIndex.setStatus("mandatory")
_MscVncsDP_ObjectIdentity = ObjectIdentity
mscVncsDP = _MscVncsDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2)
)
_MscVncsDPRowStatusTable_Object = MibTable
mscVncsDPRowStatusTable = _MscVncsDPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 1)
)
if mibBuilder.loadTexts:
    mscVncsDPRowStatusTable.setStatus("mandatory")
_MscVncsDPRowStatusEntry_Object = MibTableRow
mscVncsDPRowStatusEntry = _MscVncsDPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 1, 1)
)
mscVncsDPRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsDPIndex"),
)
if mibBuilder.loadTexts:
    mscVncsDPRowStatusEntry.setStatus("mandatory")
_MscVncsDPRowStatus_Type = RowStatus
_MscVncsDPRowStatus_Object = MibTableColumn
mscVncsDPRowStatus = _MscVncsDPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 1, 1, 1),
    _MscVncsDPRowStatus_Type()
)
mscVncsDPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsDPRowStatus.setStatus("mandatory")
_MscVncsDPComponentName_Type = DisplayString
_MscVncsDPComponentName_Object = MibTableColumn
mscVncsDPComponentName = _MscVncsDPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 1, 1, 2),
    _MscVncsDPComponentName_Type()
)
mscVncsDPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsDPComponentName.setStatus("mandatory")
_MscVncsDPStorageType_Type = StorageType
_MscVncsDPStorageType_Object = MibTableColumn
mscVncsDPStorageType = _MscVncsDPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 1, 1, 4),
    _MscVncsDPStorageType_Type()
)
mscVncsDPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsDPStorageType.setStatus("mandatory")


class _MscVncsDPIndex_Type(Integer32):
    """Custom type mscVncsDPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscVncsDPIndex_Type.__name__ = "Integer32"
_MscVncsDPIndex_Object = MibTableColumn
mscVncsDPIndex = _MscVncsDPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 1, 1, 10),
    _MscVncsDPIndex_Type()
)
mscVncsDPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsDPIndex.setStatus("mandatory")
_MscVncsDPDn_ObjectIdentity = ObjectIdentity
mscVncsDPDn = _MscVncsDPDn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2)
)
_MscVncsDPDnRowStatusTable_Object = MibTable
mscVncsDPDnRowStatusTable = _MscVncsDPDnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscVncsDPDnRowStatusTable.setStatus("mandatory")
_MscVncsDPDnRowStatusEntry_Object = MibTableRow
mscVncsDPDnRowStatusEntry = _MscVncsDPDnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 1, 1)
)
mscVncsDPDnRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsDPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsDPDnIndex"),
)
if mibBuilder.loadTexts:
    mscVncsDPDnRowStatusEntry.setStatus("mandatory")
_MscVncsDPDnRowStatus_Type = RowStatus
_MscVncsDPDnRowStatus_Object = MibTableColumn
mscVncsDPDnRowStatus = _MscVncsDPDnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 1, 1, 1),
    _MscVncsDPDnRowStatus_Type()
)
mscVncsDPDnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsDPDnRowStatus.setStatus("mandatory")
_MscVncsDPDnComponentName_Type = DisplayString
_MscVncsDPDnComponentName_Object = MibTableColumn
mscVncsDPDnComponentName = _MscVncsDPDnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 1, 1, 2),
    _MscVncsDPDnComponentName_Type()
)
mscVncsDPDnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsDPDnComponentName.setStatus("mandatory")
_MscVncsDPDnStorageType_Type = StorageType
_MscVncsDPDnStorageType_Object = MibTableColumn
mscVncsDPDnStorageType = _MscVncsDPDnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 1, 1, 4),
    _MscVncsDPDnStorageType_Type()
)
mscVncsDPDnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsDPDnStorageType.setStatus("mandatory")


class _MscVncsDPDnIndex_Type(WildcardedDigitString):
    """Custom type mscVncsDPDnIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MscVncsDPDnIndex_Type.__name__ = "WildcardedDigitString"
_MscVncsDPDnIndex_Object = MibTableColumn
mscVncsDPDnIndex = _MscVncsDPDnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 1, 1, 10),
    _MscVncsDPDnIndex_Type()
)
mscVncsDPDnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsDPDnIndex.setStatus("mandatory")
_MscVncsDPDnProvTable_Object = MibTable
mscVncsDPDnProvTable = _MscVncsDPDnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscVncsDPDnProvTable.setStatus("mandatory")
_MscVncsDPDnProvEntry_Object = MibTableRow
mscVncsDPDnProvEntry = _MscVncsDPDnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 10, 1)
)
mscVncsDPDnProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsDPIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsDPDnIndex"),
)
if mibBuilder.loadTexts:
    mscVncsDPDnProvEntry.setStatus("mandatory")


class _MscVncsDPDnDestinationNodeId_Type(Unsigned32):
    """Custom type mscVncsDPDnDestinationNodeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MscVncsDPDnDestinationNodeId_Type.__name__ = "Unsigned32"
_MscVncsDPDnDestinationNodeId_Object = MibTableColumn
mscVncsDPDnDestinationNodeId = _MscVncsDPDnDestinationNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 10, 1, 1),
    _MscVncsDPDnDestinationNodeId_Type()
)
mscVncsDPDnDestinationNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsDPDnDestinationNodeId.setStatus("mandatory")
_MscVncsDPDnDestinationComponentId_Type = RowPointer
_MscVncsDPDnDestinationComponentId_Object = MibTableColumn
mscVncsDPDnDestinationComponentId = _MscVncsDPDnDestinationComponentId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 10, 1, 2),
    _MscVncsDPDnDestinationComponentId_Type()
)
mscVncsDPDnDestinationComponentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsDPDnDestinationComponentId.setStatus("mandatory")


class _MscVncsDPDnVoiceProfileNumber_Type(Unsigned32):
    """Custom type mscVncsDPDnVoiceProfileNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVncsDPDnVoiceProfileNumber_Type.__name__ = "Unsigned32"
_MscVncsDPDnVoiceProfileNumber_Object = MibTableColumn
mscVncsDPDnVoiceProfileNumber = _MscVncsDPDnVoiceProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 10, 1, 3),
    _MscVncsDPDnVoiceProfileNumber_Type()
)
mscVncsDPDnVoiceProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsDPDnVoiceProfileNumber.setStatus("mandatory")


class _MscVncsDPDnNumberingPlanIndicator_Type(Integer32):
    """Custom type mscVncsDPDnNumberingPlanIndicator based on Integer32"""
    defaultValue = 1

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


_MscVncsDPDnNumberingPlanIndicator_Type.__name__ = "Integer32"
_MscVncsDPDnNumberingPlanIndicator_Object = MibTableColumn
mscVncsDPDnNumberingPlanIndicator = _MscVncsDPDnNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 10, 1, 4),
    _MscVncsDPDnNumberingPlanIndicator_Type()
)
mscVncsDPDnNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsDPDnNumberingPlanIndicator.setStatus("mandatory")


class _MscVncsDPDnDataNetworkAddress_Type(DigitString):
    """Custom type mscVncsDPDnDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_MscVncsDPDnDataNetworkAddress_Type.__name__ = "DigitString"
_MscVncsDPDnDataNetworkAddress_Object = MibTableColumn
mscVncsDPDnDataNetworkAddress = _MscVncsDPDnDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 2, 10, 1, 5),
    _MscVncsDPDnDataNetworkAddress_Type()
)
mscVncsDPDnDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsDPDnDataNetworkAddress.setStatus("mandatory")
_MscVncsDPStatsTable_Object = MibTable
mscVncsDPStatsTable = _MscVncsDPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 10)
)
if mibBuilder.loadTexts:
    mscVncsDPStatsTable.setStatus("mandatory")
_MscVncsDPStatsEntry_Object = MibTableRow
mscVncsDPStatsEntry = _MscVncsDPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 10, 1)
)
mscVncsDPStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsDPIndex"),
)
if mibBuilder.loadTexts:
    mscVncsDPStatsEntry.setStatus("mandatory")
_MscVncsDPCompleteTranslations_Type = Counter32
_MscVncsDPCompleteTranslations_Object = MibTableColumn
mscVncsDPCompleteTranslations = _MscVncsDPCompleteTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 10, 1, 1),
    _MscVncsDPCompleteTranslations_Type()
)
mscVncsDPCompleteTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsDPCompleteTranslations.setStatus("mandatory")
_MscVncsDPIncompleteTranslations_Type = Counter32
_MscVncsDPIncompleteTranslations_Object = MibTableColumn
mscVncsDPIncompleteTranslations = _MscVncsDPIncompleteTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 10, 1, 2),
    _MscVncsDPIncompleteTranslations_Type()
)
mscVncsDPIncompleteTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsDPIncompleteTranslations.setStatus("mandatory")
_MscVncsDPFailedTranslations_Type = Counter32
_MscVncsDPFailedTranslations_Object = MibTableColumn
mscVncsDPFailedTranslations = _MscVncsDPFailedTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 2, 10, 1, 3),
    _MscVncsDPFailedTranslations_Type()
)
mscVncsDPFailedTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsDPFailedTranslations.setStatus("mandatory")
_MscVncsVp_ObjectIdentity = ObjectIdentity
mscVncsVp = _MscVncsVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3)
)
_MscVncsVpRowStatusTable_Object = MibTable
mscVncsVpRowStatusTable = _MscVncsVpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 1)
)
if mibBuilder.loadTexts:
    mscVncsVpRowStatusTable.setStatus("mandatory")
_MscVncsVpRowStatusEntry_Object = MibTableRow
mscVncsVpRowStatusEntry = _MscVncsVpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 1, 1)
)
mscVncsVpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpRowStatusEntry.setStatus("mandatory")
_MscVncsVpRowStatus_Type = RowStatus
_MscVncsVpRowStatus_Object = MibTableColumn
mscVncsVpRowStatus = _MscVncsVpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 1, 1, 1),
    _MscVncsVpRowStatus_Type()
)
mscVncsVpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpRowStatus.setStatus("mandatory")
_MscVncsVpComponentName_Type = DisplayString
_MscVncsVpComponentName_Object = MibTableColumn
mscVncsVpComponentName = _MscVncsVpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 1, 1, 2),
    _MscVncsVpComponentName_Type()
)
mscVncsVpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsVpComponentName.setStatus("mandatory")
_MscVncsVpStorageType_Type = StorageType
_MscVncsVpStorageType_Object = MibTableColumn
mscVncsVpStorageType = _MscVncsVpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 1, 1, 4),
    _MscVncsVpStorageType_Type()
)
mscVncsVpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsVpStorageType.setStatus("mandatory")


class _MscVncsVpIndex_Type(Integer32):
    """Custom type mscVncsVpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MscVncsVpIndex_Type.__name__ = "Integer32"
_MscVncsVpIndex_Object = MibTableColumn
mscVncsVpIndex = _MscVncsVpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 1, 1, 10),
    _MscVncsVpIndex_Type()
)
mscVncsVpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpIndex.setStatus("mandatory")
_MscVncsVpLCOpsTable_Object = MibTable
mscVncsVpLCOpsTable = _MscVncsVpLCOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2)
)
if mibBuilder.loadTexts:
    mscVncsVpLCOpsTable.setStatus("mandatory")
_MscVncsVpLCOpsEntry_Object = MibTableRow
mscVncsVpLCOpsEntry = _MscVncsVpLCOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1)
)
mscVncsVpLCOpsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpLCOpsEntry.setStatus("mandatory")


class _MscVncsVpSetupPriority_Type(Unsigned32):
    """Custom type mscVncsVpSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVncsVpSetupPriority_Type.__name__ = "Unsigned32"
_MscVncsVpSetupPriority_Object = MibTableColumn
mscVncsVpSetupPriority = _MscVncsVpSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 1),
    _MscVncsVpSetupPriority_Type()
)
mscVncsVpSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpSetupPriority.setStatus("mandatory")


class _MscVncsVpHoldingPriority_Type(Unsigned32):
    """Custom type mscVncsVpHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVncsVpHoldingPriority_Type.__name__ = "Unsigned32"
_MscVncsVpHoldingPriority_Object = MibTableColumn
mscVncsVpHoldingPriority = _MscVncsVpHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 2),
    _MscVncsVpHoldingPriority_Type()
)
mscVncsVpHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpHoldingPriority.setStatus("mandatory")


class _MscVncsVpBumpPreference_Type(Integer32):
    """Custom type mscVncsVpBumpPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bumpToObtainBestRoute", 1),
          ("bumpWhenNecessary", 0))
    )


_MscVncsVpBumpPreference_Type.__name__ = "Integer32"
_MscVncsVpBumpPreference_Object = MibTableColumn
mscVncsVpBumpPreference = _MscVncsVpBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 3),
    _MscVncsVpBumpPreference_Type()
)
mscVncsVpBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpBumpPreference.setStatus("mandatory")


class _MscVncsVpRequiredTrafficType_Type(Integer32):
    """Custom type mscVncsVpRequiredTrafficType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("trafficType1", 3),
          ("trafficType2", 4),
          ("trafficType3", 5),
          ("trafficType4", 6),
          ("trafficType5", 7),
          ("video", 2),
          ("voice", 0))
    )


_MscVncsVpRequiredTrafficType_Type.__name__ = "Integer32"
_MscVncsVpRequiredTrafficType_Object = MibTableColumn
mscVncsVpRequiredTrafficType = _MscVncsVpRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 6),
    _MscVncsVpRequiredTrafficType_Type()
)
mscVncsVpRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpRequiredTrafficType.setStatus("mandatory")


class _MscVncsVpPermittedTrunkTypes_Type(OctetString):
    """Custom type mscVncsVpPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscVncsVpPermittedTrunkTypes_Type.__name__ = "OctetString"
_MscVncsVpPermittedTrunkTypes_Object = MibTableColumn
mscVncsVpPermittedTrunkTypes = _MscVncsVpPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 7),
    _MscVncsVpPermittedTrunkTypes_Type()
)
mscVncsVpPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpPermittedTrunkTypes.setStatus("mandatory")


class _MscVncsVpRequiredSecurity_Type(Unsigned32):
    """Custom type mscVncsVpRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVncsVpRequiredSecurity_Type.__name__ = "Unsigned32"
_MscVncsVpRequiredSecurity_Object = MibTableColumn
mscVncsVpRequiredSecurity = _MscVncsVpRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 8),
    _MscVncsVpRequiredSecurity_Type()
)
mscVncsVpRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpRequiredSecurity.setStatus("mandatory")


class _MscVncsVpRequiredCustomerParm_Type(Unsigned32):
    """Custom type mscVncsVpRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MscVncsVpRequiredCustomerParm_Type.__name__ = "Unsigned32"
_MscVncsVpRequiredCustomerParm_Object = MibTableColumn
mscVncsVpRequiredCustomerParm = _MscVncsVpRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 9),
    _MscVncsVpRequiredCustomerParm_Type()
)
mscVncsVpRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpRequiredCustomerParm.setStatus("mandatory")


class _MscVncsVpPathAttributeToMinimize_Type(Integer32):
    """Custom type mscVncsVpPathAttributeToMinimize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cost", 0),
          ("delay", 1))
    )


_MscVncsVpPathAttributeToMinimize_Type.__name__ = "Integer32"
_MscVncsVpPathAttributeToMinimize_Object = MibTableColumn
mscVncsVpPathAttributeToMinimize = _MscVncsVpPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 10),
    _MscVncsVpPathAttributeToMinimize_Type()
)
mscVncsVpPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpPathAttributeToMinimize.setStatus("mandatory")


class _MscVncsVpMaximumAcceptableCost_Type(Unsigned32):
    """Custom type mscVncsVpMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVncsVpMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_MscVncsVpMaximumAcceptableCost_Object = MibTableColumn
mscVncsVpMaximumAcceptableCost = _MscVncsVpMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 11),
    _MscVncsVpMaximumAcceptableCost_Type()
)
mscVncsVpMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpMaximumAcceptableCost.setStatus("mandatory")


class _MscVncsVpMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type mscVncsVpMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MscVncsVpMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_MscVncsVpMaximumAcceptableDelay_Object = MibTableColumn
mscVncsVpMaximumAcceptableDelay = _MscVncsVpMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 12),
    _MscVncsVpMaximumAcceptableDelay_Type()
)
mscVncsVpMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpMaximumAcceptableDelay.setStatus("mandatory")


class _MscVncsVpEmissionPriority_Type(Unsigned32):
    """Custom type mscVncsVpEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MscVncsVpEmissionPriority_Type.__name__ = "Unsigned32"
_MscVncsVpEmissionPriority_Object = MibTableColumn
mscVncsVpEmissionPriority = _MscVncsVpEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 13),
    _MscVncsVpEmissionPriority_Type()
)
mscVncsVpEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpEmissionPriority.setStatus("mandatory")


class _MscVncsVpDiscardPriority_Type(Unsigned32):
    """Custom type mscVncsVpDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MscVncsVpDiscardPriority_Type.__name__ = "Unsigned32"
_MscVncsVpDiscardPriority_Object = MibTableColumn
mscVncsVpDiscardPriority = _MscVncsVpDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 14),
    _MscVncsVpDiscardPriority_Type()
)
mscVncsVpDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpDiscardPriority.setStatus("mandatory")


class _MscVncsVpPathFailureAction_Type(Integer32):
    """Custom type mscVncsVpPathFailureAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnectConnection", 0),
          ("reRoutePath", 1))
    )


_MscVncsVpPathFailureAction_Type.__name__ = "Integer32"
_MscVncsVpPathFailureAction_Object = MibTableColumn
mscVncsVpPathFailureAction = _MscVncsVpPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 15),
    _MscVncsVpPathFailureAction_Type()
)
mscVncsVpPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpPathFailureAction.setStatus("mandatory")


class _MscVncsVpOptimization_Type(Integer32):
    """Custom type mscVncsVpOptimization based on Integer32"""
    defaultValue = 1

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


_MscVncsVpOptimization_Type.__name__ = "Integer32"
_MscVncsVpOptimization_Object = MibTableColumn
mscVncsVpOptimization = _MscVncsVpOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 16),
    _MscVncsVpOptimization_Type()
)
mscVncsVpOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpOptimization.setStatus("mandatory")


class _MscVncsVpMaximumAcceptableGatewayCost_Type(Unsigned32):
    """Custom type mscVncsVpMaximumAcceptableGatewayCost based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVncsVpMaximumAcceptableGatewayCost_Type.__name__ = "Unsigned32"
_MscVncsVpMaximumAcceptableGatewayCost_Object = MibTableColumn
mscVncsVpMaximumAcceptableGatewayCost = _MscVncsVpMaximumAcceptableGatewayCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 2, 1, 17),
    _MscVncsVpMaximumAcceptableGatewayCost_Type()
)
mscVncsVpMaximumAcceptableGatewayCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpMaximumAcceptableGatewayCost.setStatus("mandatory")
_MscVncsVpFrOpsTable_Object = MibTable
mscVncsVpFrOpsTable = _MscVncsVpFrOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3)
)
if mibBuilder.loadTexts:
    mscVncsVpFrOpsTable.setStatus("mandatory")
_MscVncsVpFrOpsEntry_Object = MibTableRow
mscVncsVpFrOpsEntry = _MscVncsVpFrOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1)
)
mscVncsVpFrOpsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpFrOpsEntry.setStatus("mandatory")


class _MscVncsVpMaxVoiceBitRate_Type(Integer32):
    """Custom type mscVncsVpMaxVoiceBitRate based on Integer32"""
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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVncsVpMaxVoiceBitRate_Type.__name__ = "Integer32"
_MscVncsVpMaxVoiceBitRate_Object = MibTableColumn
mscVncsVpMaxVoiceBitRate = _MscVncsVpMaxVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 1),
    _MscVncsVpMaxVoiceBitRate_Type()
)
mscVncsVpMaxVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpMaxVoiceBitRate.setStatus("obsolete")


class _MscVncsVpMinVoiceBitRate_Type(Integer32):
    """Custom type mscVncsVpMinVoiceBitRate based on Integer32"""
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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVncsVpMinVoiceBitRate_Type.__name__ = "Integer32"
_MscVncsVpMinVoiceBitRate_Object = MibTableColumn
mscVncsVpMinVoiceBitRate = _MscVncsVpMinVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 2),
    _MscVncsVpMinVoiceBitRate_Type()
)
mscVncsVpMinVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpMinVoiceBitRate.setStatus("obsolete")


class _MscVncsVpMaxModemBitRate_Type(Integer32):
    """Custom type mscVncsVpMaxModemBitRate based on Integer32"""
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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVncsVpMaxModemBitRate_Type.__name__ = "Integer32"
_MscVncsVpMaxModemBitRate_Object = MibTableColumn
mscVncsVpMaxModemBitRate = _MscVncsVpMaxModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 3),
    _MscVncsVpMaxModemBitRate_Type()
)
mscVncsVpMaxModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpMaxModemBitRate.setStatus("obsolete")


class _MscVncsVpMinModemBitRate_Type(Integer32):
    """Custom type mscVncsVpMinModemBitRate based on Integer32"""
    defaultValue = 1

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
        *(("n16", 3),
          ("n24", 2),
          ("n32", 1),
          ("n64", 0))
    )


_MscVncsVpMinModemBitRate_Type.__name__ = "Integer32"
_MscVncsVpMinModemBitRate_Object = MibTableColumn
mscVncsVpMinModemBitRate = _MscVncsVpMinModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 4),
    _MscVncsVpMinModemBitRate_Type()
)
mscVncsVpMinModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpMinModemBitRate.setStatus("obsolete")


class _MscVncsVpAudioGain_Type(Integer32):
    """Custom type mscVncsVpAudioGain based on Integer32"""
    defaultValue = 3

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
        *(("minus2", 2),
          ("minus4", 1),
          ("minus6", 0),
          ("n0", 3),
          ("n2", 4),
          ("n4", 5),
          ("n6", 6))
    )


_MscVncsVpAudioGain_Type.__name__ = "Integer32"
_MscVncsVpAudioGain_Object = MibTableColumn
mscVncsVpAudioGain = _MscVncsVpAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 5),
    _MscVncsVpAudioGain_Type()
)
mscVncsVpAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpAudioGain.setStatus("obsolete")


class _MscVncsVpSilenceSuppression_Type(Integer32):
    """Custom type mscVncsVpSilenceSuppression based on Integer32"""
    defaultValue = 1

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
        *(("congested", 2),
          ("off", 0),
          ("on", 1),
          ("slow", 3),
          ("slowAndCongested", 4))
    )


_MscVncsVpSilenceSuppression_Type.__name__ = "Integer32"
_MscVncsVpSilenceSuppression_Object = MibTableColumn
mscVncsVpSilenceSuppression = _MscVncsVpSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 6),
    _MscVncsVpSilenceSuppression_Type()
)
mscVncsVpSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpSilenceSuppression.setStatus("mandatory")


class _MscVncsVpEchoCancellation_Type(Integer32):
    """Custom type mscVncsVpEchoCancellation based on Integer32"""
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


_MscVncsVpEchoCancellation_Type.__name__ = "Integer32"
_MscVncsVpEchoCancellation_Object = MibTableColumn
mscVncsVpEchoCancellation = _MscVncsVpEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 7),
    _MscVncsVpEchoCancellation_Type()
)
mscVncsVpEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpEchoCancellation.setStatus("obsolete")


class _MscVncsVpSilenceSuppressionFactor_Type(Unsigned32):
    """Custom type mscVncsVpSilenceSuppressionFactor based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MscVncsVpSilenceSuppressionFactor_Type.__name__ = "Unsigned32"
_MscVncsVpSilenceSuppressionFactor_Object = MibTableColumn
mscVncsVpSilenceSuppressionFactor = _MscVncsVpSilenceSuppressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 8),
    _MscVncsVpSilenceSuppressionFactor_Type()
)
mscVncsVpSilenceSuppressionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpSilenceSuppressionFactor.setStatus("mandatory")


class _MscVncsVpDataCallsAccepted_Type(Integer32):
    """Custom type mscVncsVpDataCallsAccepted based on Integer32"""
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


_MscVncsVpDataCallsAccepted_Type.__name__ = "Integer32"
_MscVncsVpDataCallsAccepted_Object = MibTableColumn
mscVncsVpDataCallsAccepted = _MscVncsVpDataCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 9),
    _MscVncsVpDataCallsAccepted_Type()
)
mscVncsVpDataCallsAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpDataCallsAccepted.setStatus("mandatory")


class _MscVncsVpFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type mscVncsVpFaxIdleSuppressionG711G726 based on Integer32"""
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


_MscVncsVpFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_MscVncsVpFaxIdleSuppressionG711G726_Object = MibTableColumn
mscVncsVpFaxIdleSuppressionG711G726 = _MscVncsVpFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 15),
    _MscVncsVpFaxIdleSuppressionG711G726_Type()
)
mscVncsVpFaxIdleSuppressionG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpFaxIdleSuppressionG711G726.setStatus("mandatory")


class _MscVncsVpInsertedOutputDelay_Type(Integer32):
    """Custom type mscVncsVpInsertedOutputDelay based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              15,
              22,
              30,
              35,
              40,
              45,
              50,
              75,
              100,
              125,
              150)
        )
    )
    namedValues = NamedValues(
        *(("n100", 100),
          ("n125", 125),
          ("n15", 15),
          ("n150", 150),
          ("n22", 22),
          ("n30", 30),
          ("n35", 35),
          ("n40", 40),
          ("n45", 45),
          ("n5", 5),
          ("n50", 50),
          ("n75", 75))
    )


_MscVncsVpInsertedOutputDelay_Type.__name__ = "Integer32"
_MscVncsVpInsertedOutputDelay_Object = MibTableColumn
mscVncsVpInsertedOutputDelay = _MscVncsVpInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 17),
    _MscVncsVpInsertedOutputDelay_Type()
)
mscVncsVpInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpInsertedOutputDelay.setStatus("mandatory")


class _MscVncsVpVoiceTrafficOptimization_Type(Integer32):
    """Custom type mscVncsVpVoiceTrafficOptimization based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 0),
          ("delay", 1))
    )


_MscVncsVpVoiceTrafficOptimization_Type.__name__ = "Integer32"
_MscVncsVpVoiceTrafficOptimization_Object = MibTableColumn
mscVncsVpVoiceTrafficOptimization = _MscVncsVpVoiceTrafficOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 18),
    _MscVncsVpVoiceTrafficOptimization_Type()
)
mscVncsVpVoiceTrafficOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpVoiceTrafficOptimization.setStatus("obsolete")


class _MscVncsVpDtmfRegeneration_Type(Integer32):
    """Custom type mscVncsVpDtmfRegeneration based on Integer32"""
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


_MscVncsVpDtmfRegeneration_Type.__name__ = "Integer32"
_MscVncsVpDtmfRegeneration_Object = MibTableColumn
mscVncsVpDtmfRegeneration = _MscVncsVpDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 19),
    _MscVncsVpDtmfRegeneration_Type()
)
mscVncsVpDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpDtmfRegeneration.setStatus("mandatory")


class _MscVncsVpV17EncodedAsG711G726_Type(Integer32):
    """Custom type mscVncsVpV17EncodedAsG711G726 based on Integer32"""
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


_MscVncsVpV17EncodedAsG711G726_Type.__name__ = "Integer32"
_MscVncsVpV17EncodedAsG711G726_Object = MibTableColumn
mscVncsVpV17EncodedAsG711G726 = _MscVncsVpV17EncodedAsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 3, 1, 20),
    _MscVncsVpV17EncodedAsG711G726_Type()
)
mscVncsVpV17EncodedAsG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpV17EncodedAsG711G726.setStatus("mandatory")
_MscVncsVpStatsTable_Object = MibTable
mscVncsVpStatsTable = _MscVncsVpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 4)
)
if mibBuilder.loadTexts:
    mscVncsVpStatsTable.setStatus("mandatory")
_MscVncsVpStatsEntry_Object = MibTableRow
mscVncsVpStatsEntry = _MscVncsVpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 4, 1)
)
mscVncsVpStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpStatsEntry.setStatus("mandatory")


class _MscVncsVpUsageCount_Type(Unsigned32):
    """Custom type mscVncsVpUsageCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVncsVpUsageCount_Type.__name__ = "Unsigned32"
_MscVncsVpUsageCount_Object = MibTableColumn
mscVncsVpUsageCount = _MscVncsVpUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 4, 1, 1),
    _MscVncsVpUsageCount_Type()
)
mscVncsVpUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsVpUsageCount.setStatus("mandatory")
_MscVncsVpVoiceRatesTable_Object = MibTable
mscVncsVpVoiceRatesTable = _MscVncsVpVoiceRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 322)
)
if mibBuilder.loadTexts:
    mscVncsVpVoiceRatesTable.setStatus("obsolete")
_MscVncsVpVoiceRatesEntry_Object = MibTableRow
mscVncsVpVoiceRatesEntry = _MscVncsVpVoiceRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 322, 1)
)
mscVncsVpVoiceRatesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpVoiceRatesEncodingIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpVoiceRatesRateIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpVoiceRatesEntry.setStatus("obsolete")


class _MscVncsVpVoiceRatesEncodingIndex_Type(Integer32):
    """Custom type mscVncsVpVoiceRatesEncodingIndex based on Integer32"""
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
        *(("g711G726", 1),
          ("g711Only", 0),
          ("g728Only", 2),
          ("g729Only", 3))
    )


_MscVncsVpVoiceRatesEncodingIndex_Type.__name__ = "Integer32"
_MscVncsVpVoiceRatesEncodingIndex_Object = MibTableColumn
mscVncsVpVoiceRatesEncodingIndex = _MscVncsVpVoiceRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 322, 1, 1),
    _MscVncsVpVoiceRatesEncodingIndex_Type()
)
mscVncsVpVoiceRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpVoiceRatesEncodingIndex.setStatus("obsolete")


class _MscVncsVpVoiceRatesRateIndex_Type(Integer32):
    """Custom type mscVncsVpVoiceRatesRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("min", 0))
    )


_MscVncsVpVoiceRatesRateIndex_Type.__name__ = "Integer32"
_MscVncsVpVoiceRatesRateIndex_Object = MibTableColumn
mscVncsVpVoiceRatesRateIndex = _MscVncsVpVoiceRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 322, 1, 2),
    _MscVncsVpVoiceRatesRateIndex_Type()
)
mscVncsVpVoiceRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpVoiceRatesRateIndex.setStatus("obsolete")


class _MscVncsVpVoiceRatesValue_Type(FixedPoint1):
    """Custom type mscVncsVpVoiceRatesValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(640, 640),
    )


_MscVncsVpVoiceRatesValue_Type.__name__ = "FixedPoint1"
_MscVncsVpVoiceRatesValue_Object = MibTableColumn
mscVncsVpVoiceRatesValue = _MscVncsVpVoiceRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 322, 1, 3),
    _MscVncsVpVoiceRatesValue_Type()
)
mscVncsVpVoiceRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpVoiceRatesValue.setStatus("obsolete")
_MscVncsVpVoiceEncodingChoiceTable_Object = MibTable
mscVncsVpVoiceEncodingChoiceTable = _MscVncsVpVoiceEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 323)
)
if mibBuilder.loadTexts:
    mscVncsVpVoiceEncodingChoiceTable.setStatus("obsolete")
_MscVncsVpVoiceEncodingChoiceEntry_Object = MibTableRow
mscVncsVpVoiceEncodingChoiceEntry = _MscVncsVpVoiceEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 323, 1)
)
mscVncsVpVoiceEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpVoiceEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpVoiceEncodingChoiceEntry.setStatus("obsolete")


class _MscVncsVpVoiceEncodingChoiceIndex_Type(Integer32):
    """Custom type mscVncsVpVoiceEncodingChoiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 0),
          ("second", 1),
          ("third", 2))
    )


_MscVncsVpVoiceEncodingChoiceIndex_Type.__name__ = "Integer32"
_MscVncsVpVoiceEncodingChoiceIndex_Object = MibTableColumn
mscVncsVpVoiceEncodingChoiceIndex = _MscVncsVpVoiceEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 323, 1, 1),
    _MscVncsVpVoiceEncodingChoiceIndex_Type()
)
mscVncsVpVoiceEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpVoiceEncodingChoiceIndex.setStatus("obsolete")


class _MscVncsVpVoiceEncodingChoiceValue_Type(Integer32):
    """Custom type mscVncsVpVoiceEncodingChoiceValue based on Integer32"""
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
        *(("g711G726", 1),
          ("g711Only", 0),
          ("g728Only", 2),
          ("g729Only", 3),
          ("none", 4))
    )


_MscVncsVpVoiceEncodingChoiceValue_Type.__name__ = "Integer32"
_MscVncsVpVoiceEncodingChoiceValue_Object = MibTableColumn
mscVncsVpVoiceEncodingChoiceValue = _MscVncsVpVoiceEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 323, 1, 2),
    _MscVncsVpVoiceEncodingChoiceValue_Type()
)
mscVncsVpVoiceEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpVoiceEncodingChoiceValue.setStatus("obsolete")
_MscVncsVpModemFaxRatesTable_Object = MibTable
mscVncsVpModemFaxRatesTable = _MscVncsVpModemFaxRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 324)
)
if mibBuilder.loadTexts:
    mscVncsVpModemFaxRatesTable.setStatus("obsolete")
_MscVncsVpModemFaxRatesEntry_Object = MibTableRow
mscVncsVpModemFaxRatesEntry = _MscVncsVpModemFaxRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 324, 1)
)
mscVncsVpModemFaxRatesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpModemFaxRatesEncodingIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpModemFaxRatesRateIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpModemFaxRatesEntry.setStatus("obsolete")


class _MscVncsVpModemFaxRatesEncodingIndex_Type(Integer32):
    """Custom type mscVncsVpModemFaxRatesEncodingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711G726", 1),
          ("g711Only", 0),
          ("relay", 2))
    )


_MscVncsVpModemFaxRatesEncodingIndex_Type.__name__ = "Integer32"
_MscVncsVpModemFaxRatesEncodingIndex_Object = MibTableColumn
mscVncsVpModemFaxRatesEncodingIndex = _MscVncsVpModemFaxRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 324, 1, 1),
    _MscVncsVpModemFaxRatesEncodingIndex_Type()
)
mscVncsVpModemFaxRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpModemFaxRatesEncodingIndex.setStatus("obsolete")


class _MscVncsVpModemFaxRatesRateIndex_Type(Integer32):
    """Custom type mscVncsVpModemFaxRatesRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("min", 0))
    )


_MscVncsVpModemFaxRatesRateIndex_Type.__name__ = "Integer32"
_MscVncsVpModemFaxRatesRateIndex_Object = MibTableColumn
mscVncsVpModemFaxRatesRateIndex = _MscVncsVpModemFaxRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 324, 1, 2),
    _MscVncsVpModemFaxRatesRateIndex_Type()
)
mscVncsVpModemFaxRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpModemFaxRatesRateIndex.setStatus("obsolete")


class _MscVncsVpModemFaxRatesValue_Type(FixedPoint1):
    """Custom type mscVncsVpModemFaxRatesValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(640, 640),
    )


_MscVncsVpModemFaxRatesValue_Type.__name__ = "FixedPoint1"
_MscVncsVpModemFaxRatesValue_Object = MibTableColumn
mscVncsVpModemFaxRatesValue = _MscVncsVpModemFaxRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 324, 1, 3),
    _MscVncsVpModemFaxRatesValue_Type()
)
mscVncsVpModemFaxRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpModemFaxRatesValue.setStatus("obsolete")
_MscVncsVpModemFaxEncodingChoiceTable_Object = MibTable
mscVncsVpModemFaxEncodingChoiceTable = _MscVncsVpModemFaxEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 325)
)
if mibBuilder.loadTexts:
    mscVncsVpModemFaxEncodingChoiceTable.setStatus("obsolete")
_MscVncsVpModemFaxEncodingChoiceEntry_Object = MibTableRow
mscVncsVpModemFaxEncodingChoiceEntry = _MscVncsVpModemFaxEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 325, 1)
)
mscVncsVpModemFaxEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpModemFaxEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpModemFaxEncodingChoiceEntry.setStatus("obsolete")


class _MscVncsVpModemFaxEncodingChoiceIndex_Type(Integer32):
    """Custom type mscVncsVpModemFaxEncodingChoiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 0),
          ("second", 1),
          ("third", 2))
    )


_MscVncsVpModemFaxEncodingChoiceIndex_Type.__name__ = "Integer32"
_MscVncsVpModemFaxEncodingChoiceIndex_Object = MibTableColumn
mscVncsVpModemFaxEncodingChoiceIndex = _MscVncsVpModemFaxEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 325, 1, 1),
    _MscVncsVpModemFaxEncodingChoiceIndex_Type()
)
mscVncsVpModemFaxEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpModemFaxEncodingChoiceIndex.setStatus("obsolete")


class _MscVncsVpModemFaxEncodingChoiceValue_Type(Integer32):
    """Custom type mscVncsVpModemFaxEncodingChoiceValue based on Integer32"""
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
        *(("g711G726", 1),
          ("g711Only", 0),
          ("none", 3),
          ("relay", 2))
    )


_MscVncsVpModemFaxEncodingChoiceValue_Type.__name__ = "Integer32"
_MscVncsVpModemFaxEncodingChoiceValue_Object = MibTableColumn
mscVncsVpModemFaxEncodingChoiceValue = _MscVncsVpModemFaxEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 325, 1, 2),
    _MscVncsVpModemFaxEncodingChoiceValue_Type()
)
mscVncsVpModemFaxEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpModemFaxEncodingChoiceValue.setStatus("obsolete")
_MscVncsVpNewVoiceRatesTable_Object = MibTable
mscVncsVpNewVoiceRatesTable = _MscVncsVpNewVoiceRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 381)
)
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceRatesTable.setStatus("mandatory")
_MscVncsVpNewVoiceRatesEntry_Object = MibTableRow
mscVncsVpNewVoiceRatesEntry = _MscVncsVpNewVoiceRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 381, 1)
)
mscVncsVpNewVoiceRatesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpNewVoiceRatesEncodingIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpNewVoiceRatesRateIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceRatesEntry.setStatus("mandatory")


class _MscVncsVpNewVoiceRatesEncodingIndex_Type(Integer32):
    """Custom type mscVncsVpNewVoiceRatesEncodingIndex based on Integer32"""
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
        *(("g711G726", 1),
          ("g711Only", 0),
          ("g728Only", 2),
          ("g729Only", 3))
    )


_MscVncsVpNewVoiceRatesEncodingIndex_Type.__name__ = "Integer32"
_MscVncsVpNewVoiceRatesEncodingIndex_Object = MibTableColumn
mscVncsVpNewVoiceRatesEncodingIndex = _MscVncsVpNewVoiceRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 381, 1, 1),
    _MscVncsVpNewVoiceRatesEncodingIndex_Type()
)
mscVncsVpNewVoiceRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceRatesEncodingIndex.setStatus("mandatory")


class _MscVncsVpNewVoiceRatesRateIndex_Type(Integer32):
    """Custom type mscVncsVpNewVoiceRatesRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("min", 0))
    )


_MscVncsVpNewVoiceRatesRateIndex_Type.__name__ = "Integer32"
_MscVncsVpNewVoiceRatesRateIndex_Object = MibTableColumn
mscVncsVpNewVoiceRatesRateIndex = _MscVncsVpNewVoiceRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 381, 1, 2),
    _MscVncsVpNewVoiceRatesRateIndex_Type()
)
mscVncsVpNewVoiceRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceRatesRateIndex.setStatus("mandatory")


class _MscVncsVpNewVoiceRatesValue_Type(FixedPoint1):
    """Custom type mscVncsVpNewVoiceRatesValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(640, 640),
    )


_MscVncsVpNewVoiceRatesValue_Type.__name__ = "FixedPoint1"
_MscVncsVpNewVoiceRatesValue_Object = MibTableColumn
mscVncsVpNewVoiceRatesValue = _MscVncsVpNewVoiceRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 381, 1, 3),
    _MscVncsVpNewVoiceRatesValue_Type()
)
mscVncsVpNewVoiceRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceRatesValue.setStatus("mandatory")
_MscVncsVpNewVoiceEncodingChoiceTable_Object = MibTable
mscVncsVpNewVoiceEncodingChoiceTable = _MscVncsVpNewVoiceEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 382)
)
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceEncodingChoiceTable.setStatus("mandatory")
_MscVncsVpNewVoiceEncodingChoiceEntry_Object = MibTableRow
mscVncsVpNewVoiceEncodingChoiceEntry = _MscVncsVpNewVoiceEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 382, 1)
)
mscVncsVpNewVoiceEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpNewVoiceEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceEncodingChoiceEntry.setStatus("mandatory")


class _MscVncsVpNewVoiceEncodingChoiceIndex_Type(Integer32):
    """Custom type mscVncsVpNewVoiceEncodingChoiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 0),
          ("second", 1),
          ("third", 2))
    )


_MscVncsVpNewVoiceEncodingChoiceIndex_Type.__name__ = "Integer32"
_MscVncsVpNewVoiceEncodingChoiceIndex_Object = MibTableColumn
mscVncsVpNewVoiceEncodingChoiceIndex = _MscVncsVpNewVoiceEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 382, 1, 1),
    _MscVncsVpNewVoiceEncodingChoiceIndex_Type()
)
mscVncsVpNewVoiceEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceEncodingChoiceIndex.setStatus("mandatory")


class _MscVncsVpNewVoiceEncodingChoiceValue_Type(Integer32):
    """Custom type mscVncsVpNewVoiceEncodingChoiceValue based on Integer32"""
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
        *(("g711G726", 1),
          ("g711Only", 0),
          ("g728Only", 2),
          ("g729Only", 3),
          ("none", 4))
    )


_MscVncsVpNewVoiceEncodingChoiceValue_Type.__name__ = "Integer32"
_MscVncsVpNewVoiceEncodingChoiceValue_Object = MibTableColumn
mscVncsVpNewVoiceEncodingChoiceValue = _MscVncsVpNewVoiceEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 382, 1, 2),
    _MscVncsVpNewVoiceEncodingChoiceValue_Type()
)
mscVncsVpNewVoiceEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpNewVoiceEncodingChoiceValue.setStatus("mandatory")
_MscVncsVpNewModemFaxRatesTable_Object = MibTable
mscVncsVpNewModemFaxRatesTable = _MscVncsVpNewModemFaxRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 383)
)
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxRatesTable.setStatus("mandatory")
_MscVncsVpNewModemFaxRatesEntry_Object = MibTableRow
mscVncsVpNewModemFaxRatesEntry = _MscVncsVpNewModemFaxRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 383, 1)
)
mscVncsVpNewModemFaxRatesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpNewModemFaxRatesEncodingIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpNewModemFaxRatesRateIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxRatesEntry.setStatus("mandatory")


class _MscVncsVpNewModemFaxRatesEncodingIndex_Type(Integer32):
    """Custom type mscVncsVpNewModemFaxRatesEncodingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g711G726", 1),
          ("g711Only", 0),
          ("relay", 2))
    )


_MscVncsVpNewModemFaxRatesEncodingIndex_Type.__name__ = "Integer32"
_MscVncsVpNewModemFaxRatesEncodingIndex_Object = MibTableColumn
mscVncsVpNewModemFaxRatesEncodingIndex = _MscVncsVpNewModemFaxRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 383, 1, 1),
    _MscVncsVpNewModemFaxRatesEncodingIndex_Type()
)
mscVncsVpNewModemFaxRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxRatesEncodingIndex.setStatus("mandatory")


class _MscVncsVpNewModemFaxRatesRateIndex_Type(Integer32):
    """Custom type mscVncsVpNewModemFaxRatesRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("max", 1),
          ("min", 0))
    )


_MscVncsVpNewModemFaxRatesRateIndex_Type.__name__ = "Integer32"
_MscVncsVpNewModemFaxRatesRateIndex_Object = MibTableColumn
mscVncsVpNewModemFaxRatesRateIndex = _MscVncsVpNewModemFaxRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 383, 1, 2),
    _MscVncsVpNewModemFaxRatesRateIndex_Type()
)
mscVncsVpNewModemFaxRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxRatesRateIndex.setStatus("mandatory")


class _MscVncsVpNewModemFaxRatesValue_Type(FixedPoint1):
    """Custom type mscVncsVpNewModemFaxRatesValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(72, 72),
        ValueRangeConstraint(96, 96),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(144, 144),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(640, 640),
    )


_MscVncsVpNewModemFaxRatesValue_Type.__name__ = "FixedPoint1"
_MscVncsVpNewModemFaxRatesValue_Object = MibTableColumn
mscVncsVpNewModemFaxRatesValue = _MscVncsVpNewModemFaxRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 383, 1, 3),
    _MscVncsVpNewModemFaxRatesValue_Type()
)
mscVncsVpNewModemFaxRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxRatesValue.setStatus("mandatory")
_MscVncsVpNewModemFaxEncodingChoiceTable_Object = MibTable
mscVncsVpNewModemFaxEncodingChoiceTable = _MscVncsVpNewModemFaxEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 384)
)
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxEncodingChoiceTable.setStatus("mandatory")
_MscVncsVpNewModemFaxEncodingChoiceEntry_Object = MibTableRow
mscVncsVpNewModemFaxEncodingChoiceEntry = _MscVncsVpNewModemFaxEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 384, 1)
)
mscVncsVpNewModemFaxEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVpNewModemFaxEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxEncodingChoiceEntry.setStatus("mandatory")


class _MscVncsVpNewModemFaxEncodingChoiceIndex_Type(Integer32):
    """Custom type mscVncsVpNewModemFaxEncodingChoiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 0),
          ("second", 1),
          ("third", 2))
    )


_MscVncsVpNewModemFaxEncodingChoiceIndex_Type.__name__ = "Integer32"
_MscVncsVpNewModemFaxEncodingChoiceIndex_Object = MibTableColumn
mscVncsVpNewModemFaxEncodingChoiceIndex = _MscVncsVpNewModemFaxEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 384, 1, 1),
    _MscVncsVpNewModemFaxEncodingChoiceIndex_Type()
)
mscVncsVpNewModemFaxEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxEncodingChoiceIndex.setStatus("mandatory")


class _MscVncsVpNewModemFaxEncodingChoiceValue_Type(Integer32):
    """Custom type mscVncsVpNewModemFaxEncodingChoiceValue based on Integer32"""
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
        *(("g711G726", 1),
          ("g711Only", 0),
          ("none", 3),
          ("relay", 2))
    )


_MscVncsVpNewModemFaxEncodingChoiceValue_Type.__name__ = "Integer32"
_MscVncsVpNewModemFaxEncodingChoiceValue_Object = MibTableColumn
mscVncsVpNewModemFaxEncodingChoiceValue = _MscVncsVpNewModemFaxEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 3, 384, 1, 2),
    _MscVncsVpNewModemFaxEncodingChoiceValue_Type()
)
mscVncsVpNewModemFaxEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsVpNewModemFaxEncodingChoiceValue.setStatus("mandatory")
_MscVncsProvTable_Object = MibTable
mscVncsProvTable = _MscVncsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 10)
)
if mibBuilder.loadTexts:
    mscVncsProvTable.setStatus("mandatory")
_MscVncsProvEntry_Object = MibTableRow
mscVncsProvEntry = _MscVncsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 10, 1)
)
mscVncsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
)
if mibBuilder.loadTexts:
    mscVncsProvEntry.setStatus("mandatory")


class _MscVncsCommentText_Type(AsciiString):
    """Custom type mscVncsCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscVncsCommentText_Type.__name__ = "AsciiString"
_MscVncsCommentText_Object = MibTableColumn
mscVncsCommentText = _MscVncsCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 10, 1, 1),
    _MscVncsCommentText_Type()
)
mscVncsCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVncsCommentText.setStatus("mandatory")
_MscVncsStatsTable_Object = MibTable
mscVncsStatsTable = _MscVncsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 11)
)
if mibBuilder.loadTexts:
    mscVncsStatsTable.setStatus("mandatory")
_MscVncsStatsEntry_Object = MibTableRow
mscVncsStatsEntry = _MscVncsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 11, 1)
)
mscVncsStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
)
if mibBuilder.loadTexts:
    mscVncsStatsEntry.setStatus("mandatory")
_MscVncsTotalTranslations_Type = Counter32
_MscVncsTotalTranslations_Object = MibTableColumn
mscVncsTotalTranslations = _MscVncsTotalTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 11, 1, 1),
    _MscVncsTotalTranslations_Type()
)
mscVncsTotalTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsTotalTranslations.setStatus("mandatory")
_MscVncsVRoutesTable_Object = MibTable
mscVncsVRoutesTable = _MscVncsVRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 305)
)
if mibBuilder.loadTexts:
    mscVncsVRoutesTable.setStatus("mandatory")
_MscVncsVRoutesEntry_Object = MibTableRow
mscVncsVRoutesEntry = _MscVncsVRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 305, 1)
)
mscVncsVRoutesEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-VncsCallServerMIB", "mscVncsVRoutesValue"),
)
if mibBuilder.loadTexts:
    mscVncsVRoutesEntry.setStatus("mandatory")
_MscVncsVRoutesValue_Type = Link
_MscVncsVRoutesValue_Object = MibTableColumn
mscVncsVRoutesValue = _MscVncsVRoutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 44, 305, 1, 1),
    _MscVncsVRoutesValue_Type()
)
mscVncsVRoutesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVncsVRoutesValue.setStatus("mandatory")
_VncsCallServerMIB_ObjectIdentity = ObjectIdentity
vncsCallServerMIB = _VncsCallServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66)
)
_VncsCallServerGroup_ObjectIdentity = ObjectIdentity
vncsCallServerGroup = _VncsCallServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 1)
)
_VncsCallServerGroupCA_ObjectIdentity = ObjectIdentity
vncsCallServerGroupCA = _VncsCallServerGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 1, 1)
)
_VncsCallServerGroupCA02_ObjectIdentity = ObjectIdentity
vncsCallServerGroupCA02 = _VncsCallServerGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 1, 1, 3)
)
_VncsCallServerGroupCA02A_ObjectIdentity = ObjectIdentity
vncsCallServerGroupCA02A = _VncsCallServerGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 1, 1, 3, 2)
)
_VncsCallServerCapabilities_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilities = _VncsCallServerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 3)
)
_VncsCallServerCapabilitiesCA_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilitiesCA = _VncsCallServerCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 3, 1)
)
_VncsCallServerCapabilitiesCA02_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilitiesCA02 = _VncsCallServerCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 3, 1, 3)
)
_VncsCallServerCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilitiesCA02A = _VncsCallServerCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 66, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-VncsCallServerMIB",
    **{"mscVncs": mscVncs,
       "mscVncsRowStatusTable": mscVncsRowStatusTable,
       "mscVncsRowStatusEntry": mscVncsRowStatusEntry,
       "mscVncsRowStatus": mscVncsRowStatus,
       "mscVncsComponentName": mscVncsComponentName,
       "mscVncsStorageType": mscVncsStorageType,
       "mscVncsIndex": mscVncsIndex,
       "mscVncsDP": mscVncsDP,
       "mscVncsDPRowStatusTable": mscVncsDPRowStatusTable,
       "mscVncsDPRowStatusEntry": mscVncsDPRowStatusEntry,
       "mscVncsDPRowStatus": mscVncsDPRowStatus,
       "mscVncsDPComponentName": mscVncsDPComponentName,
       "mscVncsDPStorageType": mscVncsDPStorageType,
       "mscVncsDPIndex": mscVncsDPIndex,
       "mscVncsDPDn": mscVncsDPDn,
       "mscVncsDPDnRowStatusTable": mscVncsDPDnRowStatusTable,
       "mscVncsDPDnRowStatusEntry": mscVncsDPDnRowStatusEntry,
       "mscVncsDPDnRowStatus": mscVncsDPDnRowStatus,
       "mscVncsDPDnComponentName": mscVncsDPDnComponentName,
       "mscVncsDPDnStorageType": mscVncsDPDnStorageType,
       "mscVncsDPDnIndex": mscVncsDPDnIndex,
       "mscVncsDPDnProvTable": mscVncsDPDnProvTable,
       "mscVncsDPDnProvEntry": mscVncsDPDnProvEntry,
       "mscVncsDPDnDestinationNodeId": mscVncsDPDnDestinationNodeId,
       "mscVncsDPDnDestinationComponentId": mscVncsDPDnDestinationComponentId,
       "mscVncsDPDnVoiceProfileNumber": mscVncsDPDnVoiceProfileNumber,
       "mscVncsDPDnNumberingPlanIndicator": mscVncsDPDnNumberingPlanIndicator,
       "mscVncsDPDnDataNetworkAddress": mscVncsDPDnDataNetworkAddress,
       "mscVncsDPStatsTable": mscVncsDPStatsTable,
       "mscVncsDPStatsEntry": mscVncsDPStatsEntry,
       "mscVncsDPCompleteTranslations": mscVncsDPCompleteTranslations,
       "mscVncsDPIncompleteTranslations": mscVncsDPIncompleteTranslations,
       "mscVncsDPFailedTranslations": mscVncsDPFailedTranslations,
       "mscVncsVp": mscVncsVp,
       "mscVncsVpRowStatusTable": mscVncsVpRowStatusTable,
       "mscVncsVpRowStatusEntry": mscVncsVpRowStatusEntry,
       "mscVncsVpRowStatus": mscVncsVpRowStatus,
       "mscVncsVpComponentName": mscVncsVpComponentName,
       "mscVncsVpStorageType": mscVncsVpStorageType,
       "mscVncsVpIndex": mscVncsVpIndex,
       "mscVncsVpLCOpsTable": mscVncsVpLCOpsTable,
       "mscVncsVpLCOpsEntry": mscVncsVpLCOpsEntry,
       "mscVncsVpSetupPriority": mscVncsVpSetupPriority,
       "mscVncsVpHoldingPriority": mscVncsVpHoldingPriority,
       "mscVncsVpBumpPreference": mscVncsVpBumpPreference,
       "mscVncsVpRequiredTrafficType": mscVncsVpRequiredTrafficType,
       "mscVncsVpPermittedTrunkTypes": mscVncsVpPermittedTrunkTypes,
       "mscVncsVpRequiredSecurity": mscVncsVpRequiredSecurity,
       "mscVncsVpRequiredCustomerParm": mscVncsVpRequiredCustomerParm,
       "mscVncsVpPathAttributeToMinimize": mscVncsVpPathAttributeToMinimize,
       "mscVncsVpMaximumAcceptableCost": mscVncsVpMaximumAcceptableCost,
       "mscVncsVpMaximumAcceptableDelay": mscVncsVpMaximumAcceptableDelay,
       "mscVncsVpEmissionPriority": mscVncsVpEmissionPriority,
       "mscVncsVpDiscardPriority": mscVncsVpDiscardPriority,
       "mscVncsVpPathFailureAction": mscVncsVpPathFailureAction,
       "mscVncsVpOptimization": mscVncsVpOptimization,
       "mscVncsVpMaximumAcceptableGatewayCost": mscVncsVpMaximumAcceptableGatewayCost,
       "mscVncsVpFrOpsTable": mscVncsVpFrOpsTable,
       "mscVncsVpFrOpsEntry": mscVncsVpFrOpsEntry,
       "mscVncsVpMaxVoiceBitRate": mscVncsVpMaxVoiceBitRate,
       "mscVncsVpMinVoiceBitRate": mscVncsVpMinVoiceBitRate,
       "mscVncsVpMaxModemBitRate": mscVncsVpMaxModemBitRate,
       "mscVncsVpMinModemBitRate": mscVncsVpMinModemBitRate,
       "mscVncsVpAudioGain": mscVncsVpAudioGain,
       "mscVncsVpSilenceSuppression": mscVncsVpSilenceSuppression,
       "mscVncsVpEchoCancellation": mscVncsVpEchoCancellation,
       "mscVncsVpSilenceSuppressionFactor": mscVncsVpSilenceSuppressionFactor,
       "mscVncsVpDataCallsAccepted": mscVncsVpDataCallsAccepted,
       "mscVncsVpFaxIdleSuppressionG711G726": mscVncsVpFaxIdleSuppressionG711G726,
       "mscVncsVpInsertedOutputDelay": mscVncsVpInsertedOutputDelay,
       "mscVncsVpVoiceTrafficOptimization": mscVncsVpVoiceTrafficOptimization,
       "mscVncsVpDtmfRegeneration": mscVncsVpDtmfRegeneration,
       "mscVncsVpV17EncodedAsG711G726": mscVncsVpV17EncodedAsG711G726,
       "mscVncsVpStatsTable": mscVncsVpStatsTable,
       "mscVncsVpStatsEntry": mscVncsVpStatsEntry,
       "mscVncsVpUsageCount": mscVncsVpUsageCount,
       "mscVncsVpVoiceRatesTable": mscVncsVpVoiceRatesTable,
       "mscVncsVpVoiceRatesEntry": mscVncsVpVoiceRatesEntry,
       "mscVncsVpVoiceRatesEncodingIndex": mscVncsVpVoiceRatesEncodingIndex,
       "mscVncsVpVoiceRatesRateIndex": mscVncsVpVoiceRatesRateIndex,
       "mscVncsVpVoiceRatesValue": mscVncsVpVoiceRatesValue,
       "mscVncsVpVoiceEncodingChoiceTable": mscVncsVpVoiceEncodingChoiceTable,
       "mscVncsVpVoiceEncodingChoiceEntry": mscVncsVpVoiceEncodingChoiceEntry,
       "mscVncsVpVoiceEncodingChoiceIndex": mscVncsVpVoiceEncodingChoiceIndex,
       "mscVncsVpVoiceEncodingChoiceValue": mscVncsVpVoiceEncodingChoiceValue,
       "mscVncsVpModemFaxRatesTable": mscVncsVpModemFaxRatesTable,
       "mscVncsVpModemFaxRatesEntry": mscVncsVpModemFaxRatesEntry,
       "mscVncsVpModemFaxRatesEncodingIndex": mscVncsVpModemFaxRatesEncodingIndex,
       "mscVncsVpModemFaxRatesRateIndex": mscVncsVpModemFaxRatesRateIndex,
       "mscVncsVpModemFaxRatesValue": mscVncsVpModemFaxRatesValue,
       "mscVncsVpModemFaxEncodingChoiceTable": mscVncsVpModemFaxEncodingChoiceTable,
       "mscVncsVpModemFaxEncodingChoiceEntry": mscVncsVpModemFaxEncodingChoiceEntry,
       "mscVncsVpModemFaxEncodingChoiceIndex": mscVncsVpModemFaxEncodingChoiceIndex,
       "mscVncsVpModemFaxEncodingChoiceValue": mscVncsVpModemFaxEncodingChoiceValue,
       "mscVncsVpNewVoiceRatesTable": mscVncsVpNewVoiceRatesTable,
       "mscVncsVpNewVoiceRatesEntry": mscVncsVpNewVoiceRatesEntry,
       "mscVncsVpNewVoiceRatesEncodingIndex": mscVncsVpNewVoiceRatesEncodingIndex,
       "mscVncsVpNewVoiceRatesRateIndex": mscVncsVpNewVoiceRatesRateIndex,
       "mscVncsVpNewVoiceRatesValue": mscVncsVpNewVoiceRatesValue,
       "mscVncsVpNewVoiceEncodingChoiceTable": mscVncsVpNewVoiceEncodingChoiceTable,
       "mscVncsVpNewVoiceEncodingChoiceEntry": mscVncsVpNewVoiceEncodingChoiceEntry,
       "mscVncsVpNewVoiceEncodingChoiceIndex": mscVncsVpNewVoiceEncodingChoiceIndex,
       "mscVncsVpNewVoiceEncodingChoiceValue": mscVncsVpNewVoiceEncodingChoiceValue,
       "mscVncsVpNewModemFaxRatesTable": mscVncsVpNewModemFaxRatesTable,
       "mscVncsVpNewModemFaxRatesEntry": mscVncsVpNewModemFaxRatesEntry,
       "mscVncsVpNewModemFaxRatesEncodingIndex": mscVncsVpNewModemFaxRatesEncodingIndex,
       "mscVncsVpNewModemFaxRatesRateIndex": mscVncsVpNewModemFaxRatesRateIndex,
       "mscVncsVpNewModemFaxRatesValue": mscVncsVpNewModemFaxRatesValue,
       "mscVncsVpNewModemFaxEncodingChoiceTable": mscVncsVpNewModemFaxEncodingChoiceTable,
       "mscVncsVpNewModemFaxEncodingChoiceEntry": mscVncsVpNewModemFaxEncodingChoiceEntry,
       "mscVncsVpNewModemFaxEncodingChoiceIndex": mscVncsVpNewModemFaxEncodingChoiceIndex,
       "mscVncsVpNewModemFaxEncodingChoiceValue": mscVncsVpNewModemFaxEncodingChoiceValue,
       "mscVncsProvTable": mscVncsProvTable,
       "mscVncsProvEntry": mscVncsProvEntry,
       "mscVncsCommentText": mscVncsCommentText,
       "mscVncsStatsTable": mscVncsStatsTable,
       "mscVncsStatsEntry": mscVncsStatsEntry,
       "mscVncsTotalTranslations": mscVncsTotalTranslations,
       "mscVncsVRoutesTable": mscVncsVRoutesTable,
       "mscVncsVRoutesEntry": mscVncsVRoutesEntry,
       "mscVncsVRoutesValue": mscVncsVRoutesValue,
       "vncsCallServerMIB": vncsCallServerMIB,
       "vncsCallServerGroup": vncsCallServerGroup,
       "vncsCallServerGroupCA": vncsCallServerGroupCA,
       "vncsCallServerGroupCA02": vncsCallServerGroupCA02,
       "vncsCallServerGroupCA02A": vncsCallServerGroupCA02A,
       "vncsCallServerCapabilities": vncsCallServerCapabilities,
       "vncsCallServerCapabilitiesCA": vncsCallServerCapabilitiesCA,
       "vncsCallServerCapabilitiesCA02": vncsCallServerCapabilitiesCA02,
       "vncsCallServerCapabilitiesCA02A": vncsCallServerCapabilitiesCA02A}
)
