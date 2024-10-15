# SNMP MIB module (Nortel-Magellan-Passport-VncsCallServerMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-VncsCallServerMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:34 2024
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
 FixedPoint1,
 Link,
 WildcardedDigitString) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "DigitString",
    "FixedPoint1",
    "Link",
    "WildcardedDigitString")

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

_Vncs_ObjectIdentity = ObjectIdentity
vncs = _Vncs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44)
)
_VncsRowStatusTable_Object = MibTable
vncsRowStatusTable = _VncsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 1)
)
if mibBuilder.loadTexts:
    vncsRowStatusTable.setStatus("mandatory")
_VncsRowStatusEntry_Object = MibTableRow
vncsRowStatusEntry = _VncsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 1, 1)
)
vncsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
)
if mibBuilder.loadTexts:
    vncsRowStatusEntry.setStatus("mandatory")
_VncsRowStatus_Type = RowStatus
_VncsRowStatus_Object = MibTableColumn
vncsRowStatus = _VncsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 1, 1, 1),
    _VncsRowStatus_Type()
)
vncsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsRowStatus.setStatus("mandatory")
_VncsComponentName_Type = DisplayString
_VncsComponentName_Object = MibTableColumn
vncsComponentName = _VncsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 1, 1, 2),
    _VncsComponentName_Type()
)
vncsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsComponentName.setStatus("mandatory")
_VncsStorageType_Type = StorageType
_VncsStorageType_Object = MibTableColumn
vncsStorageType = _VncsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 1, 1, 4),
    _VncsStorageType_Type()
)
vncsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsStorageType.setStatus("mandatory")


class _VncsIndex_Type(Integer32):
    """Custom type vncsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VncsIndex_Type.__name__ = "Integer32"
_VncsIndex_Object = MibTableColumn
vncsIndex = _VncsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 1, 1, 10),
    _VncsIndex_Type()
)
vncsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsIndex.setStatus("mandatory")
_VncsDP_ObjectIdentity = ObjectIdentity
vncsDP = _VncsDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2)
)
_VncsDPRowStatusTable_Object = MibTable
vncsDPRowStatusTable = _VncsDPRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 1)
)
if mibBuilder.loadTexts:
    vncsDPRowStatusTable.setStatus("mandatory")
_VncsDPRowStatusEntry_Object = MibTableRow
vncsDPRowStatusEntry = _VncsDPRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 1, 1)
)
vncsDPRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsDPIndex"),
)
if mibBuilder.loadTexts:
    vncsDPRowStatusEntry.setStatus("mandatory")
_VncsDPRowStatus_Type = RowStatus
_VncsDPRowStatus_Object = MibTableColumn
vncsDPRowStatus = _VncsDPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 1, 1, 1),
    _VncsDPRowStatus_Type()
)
vncsDPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsDPRowStatus.setStatus("mandatory")
_VncsDPComponentName_Type = DisplayString
_VncsDPComponentName_Object = MibTableColumn
vncsDPComponentName = _VncsDPComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 1, 1, 2),
    _VncsDPComponentName_Type()
)
vncsDPComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsDPComponentName.setStatus("mandatory")
_VncsDPStorageType_Type = StorageType
_VncsDPStorageType_Object = MibTableColumn
vncsDPStorageType = _VncsDPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 1, 1, 4),
    _VncsDPStorageType_Type()
)
vncsDPStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsDPStorageType.setStatus("mandatory")


class _VncsDPIndex_Type(Integer32):
    """Custom type vncsDPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VncsDPIndex_Type.__name__ = "Integer32"
_VncsDPIndex_Object = MibTableColumn
vncsDPIndex = _VncsDPIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 1, 1, 10),
    _VncsDPIndex_Type()
)
vncsDPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsDPIndex.setStatus("mandatory")
_VncsDPDn_ObjectIdentity = ObjectIdentity
vncsDPDn = _VncsDPDn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2)
)
_VncsDPDnRowStatusTable_Object = MibTable
vncsDPDnRowStatusTable = _VncsDPDnRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vncsDPDnRowStatusTable.setStatus("mandatory")
_VncsDPDnRowStatusEntry_Object = MibTableRow
vncsDPDnRowStatusEntry = _VncsDPDnRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 1, 1)
)
vncsDPDnRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsDPIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsDPDnIndex"),
)
if mibBuilder.loadTexts:
    vncsDPDnRowStatusEntry.setStatus("mandatory")
_VncsDPDnRowStatus_Type = RowStatus
_VncsDPDnRowStatus_Object = MibTableColumn
vncsDPDnRowStatus = _VncsDPDnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 1, 1, 1),
    _VncsDPDnRowStatus_Type()
)
vncsDPDnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsDPDnRowStatus.setStatus("mandatory")
_VncsDPDnComponentName_Type = DisplayString
_VncsDPDnComponentName_Object = MibTableColumn
vncsDPDnComponentName = _VncsDPDnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 1, 1, 2),
    _VncsDPDnComponentName_Type()
)
vncsDPDnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsDPDnComponentName.setStatus("mandatory")
_VncsDPDnStorageType_Type = StorageType
_VncsDPDnStorageType_Object = MibTableColumn
vncsDPDnStorageType = _VncsDPDnStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 1, 1, 4),
    _VncsDPDnStorageType_Type()
)
vncsDPDnStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsDPDnStorageType.setStatus("mandatory")


class _VncsDPDnIndex_Type(WildcardedDigitString):
    """Custom type vncsDPDnIndex based on WildcardedDigitString"""
    subtypeSpec = WildcardedDigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_VncsDPDnIndex_Type.__name__ = "WildcardedDigitString"
_VncsDPDnIndex_Object = MibTableColumn
vncsDPDnIndex = _VncsDPDnIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 1, 1, 10),
    _VncsDPDnIndex_Type()
)
vncsDPDnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsDPDnIndex.setStatus("mandatory")
_VncsDPDnProvTable_Object = MibTable
vncsDPDnProvTable = _VncsDPDnProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 10)
)
if mibBuilder.loadTexts:
    vncsDPDnProvTable.setStatus("mandatory")
_VncsDPDnProvEntry_Object = MibTableRow
vncsDPDnProvEntry = _VncsDPDnProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 10, 1)
)
vncsDPDnProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsDPIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsDPDnIndex"),
)
if mibBuilder.loadTexts:
    vncsDPDnProvEntry.setStatus("mandatory")


class _VncsDPDnDestinationNodeId_Type(Unsigned32):
    """Custom type vncsDPDnDestinationNodeId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VncsDPDnDestinationNodeId_Type.__name__ = "Unsigned32"
_VncsDPDnDestinationNodeId_Object = MibTableColumn
vncsDPDnDestinationNodeId = _VncsDPDnDestinationNodeId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 10, 1, 1),
    _VncsDPDnDestinationNodeId_Type()
)
vncsDPDnDestinationNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsDPDnDestinationNodeId.setStatus("mandatory")
_VncsDPDnDestinationComponentId_Type = RowPointer
_VncsDPDnDestinationComponentId_Object = MibTableColumn
vncsDPDnDestinationComponentId = _VncsDPDnDestinationComponentId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 10, 1, 2),
    _VncsDPDnDestinationComponentId_Type()
)
vncsDPDnDestinationComponentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsDPDnDestinationComponentId.setStatus("mandatory")


class _VncsDPDnVoiceProfileNumber_Type(Unsigned32):
    """Custom type vncsDPDnVoiceProfileNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VncsDPDnVoiceProfileNumber_Type.__name__ = "Unsigned32"
_VncsDPDnVoiceProfileNumber_Object = MibTableColumn
vncsDPDnVoiceProfileNumber = _VncsDPDnVoiceProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 10, 1, 3),
    _VncsDPDnVoiceProfileNumber_Type()
)
vncsDPDnVoiceProfileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsDPDnVoiceProfileNumber.setStatus("mandatory")


class _VncsDPDnNumberingPlanIndicator_Type(Integer32):
    """Custom type vncsDPDnNumberingPlanIndicator based on Integer32"""
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


_VncsDPDnNumberingPlanIndicator_Type.__name__ = "Integer32"
_VncsDPDnNumberingPlanIndicator_Object = MibTableColumn
vncsDPDnNumberingPlanIndicator = _VncsDPDnNumberingPlanIndicator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 10, 1, 4),
    _VncsDPDnNumberingPlanIndicator_Type()
)
vncsDPDnNumberingPlanIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsDPDnNumberingPlanIndicator.setStatus("mandatory")


class _VncsDPDnDataNetworkAddress_Type(DigitString):
    """Custom type vncsDPDnDataNetworkAddress based on DigitString"""
    subtypeSpec = DigitString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VncsDPDnDataNetworkAddress_Type.__name__ = "DigitString"
_VncsDPDnDataNetworkAddress_Object = MibTableColumn
vncsDPDnDataNetworkAddress = _VncsDPDnDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 2, 10, 1, 5),
    _VncsDPDnDataNetworkAddress_Type()
)
vncsDPDnDataNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsDPDnDataNetworkAddress.setStatus("mandatory")
_VncsDPStatsTable_Object = MibTable
vncsDPStatsTable = _VncsDPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 10)
)
if mibBuilder.loadTexts:
    vncsDPStatsTable.setStatus("mandatory")
_VncsDPStatsEntry_Object = MibTableRow
vncsDPStatsEntry = _VncsDPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 10, 1)
)
vncsDPStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsDPIndex"),
)
if mibBuilder.loadTexts:
    vncsDPStatsEntry.setStatus("mandatory")
_VncsDPCompleteTranslations_Type = Counter32
_VncsDPCompleteTranslations_Object = MibTableColumn
vncsDPCompleteTranslations = _VncsDPCompleteTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 10, 1, 1),
    _VncsDPCompleteTranslations_Type()
)
vncsDPCompleteTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsDPCompleteTranslations.setStatus("mandatory")
_VncsDPIncompleteTranslations_Type = Counter32
_VncsDPIncompleteTranslations_Object = MibTableColumn
vncsDPIncompleteTranslations = _VncsDPIncompleteTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 10, 1, 2),
    _VncsDPIncompleteTranslations_Type()
)
vncsDPIncompleteTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsDPIncompleteTranslations.setStatus("mandatory")
_VncsDPFailedTranslations_Type = Counter32
_VncsDPFailedTranslations_Object = MibTableColumn
vncsDPFailedTranslations = _VncsDPFailedTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 2, 10, 1, 3),
    _VncsDPFailedTranslations_Type()
)
vncsDPFailedTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsDPFailedTranslations.setStatus("mandatory")
_VncsVp_ObjectIdentity = ObjectIdentity
vncsVp = _VncsVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3)
)
_VncsVpRowStatusTable_Object = MibTable
vncsVpRowStatusTable = _VncsVpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 1)
)
if mibBuilder.loadTexts:
    vncsVpRowStatusTable.setStatus("mandatory")
_VncsVpRowStatusEntry_Object = MibTableRow
vncsVpRowStatusEntry = _VncsVpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 1, 1)
)
vncsVpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
)
if mibBuilder.loadTexts:
    vncsVpRowStatusEntry.setStatus("mandatory")
_VncsVpRowStatus_Type = RowStatus
_VncsVpRowStatus_Object = MibTableColumn
vncsVpRowStatus = _VncsVpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 1, 1, 1),
    _VncsVpRowStatus_Type()
)
vncsVpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpRowStatus.setStatus("mandatory")
_VncsVpComponentName_Type = DisplayString
_VncsVpComponentName_Object = MibTableColumn
vncsVpComponentName = _VncsVpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 1, 1, 2),
    _VncsVpComponentName_Type()
)
vncsVpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsVpComponentName.setStatus("mandatory")
_VncsVpStorageType_Type = StorageType
_VncsVpStorageType_Object = MibTableColumn
vncsVpStorageType = _VncsVpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 1, 1, 4),
    _VncsVpStorageType_Type()
)
vncsVpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsVpStorageType.setStatus("mandatory")


class _VncsVpIndex_Type(Integer32):
    """Custom type vncsVpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VncsVpIndex_Type.__name__ = "Integer32"
_VncsVpIndex_Object = MibTableColumn
vncsVpIndex = _VncsVpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 1, 1, 10),
    _VncsVpIndex_Type()
)
vncsVpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpIndex.setStatus("mandatory")
_VncsVpLCOpsTable_Object = MibTable
vncsVpLCOpsTable = _VncsVpLCOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2)
)
if mibBuilder.loadTexts:
    vncsVpLCOpsTable.setStatus("mandatory")
_VncsVpLCOpsEntry_Object = MibTableRow
vncsVpLCOpsEntry = _VncsVpLCOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1)
)
vncsVpLCOpsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
)
if mibBuilder.loadTexts:
    vncsVpLCOpsEntry.setStatus("mandatory")


class _VncsVpSetupPriority_Type(Unsigned32):
    """Custom type vncsVpSetupPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VncsVpSetupPriority_Type.__name__ = "Unsigned32"
_VncsVpSetupPriority_Object = MibTableColumn
vncsVpSetupPriority = _VncsVpSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 1),
    _VncsVpSetupPriority_Type()
)
vncsVpSetupPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpSetupPriority.setStatus("mandatory")


class _VncsVpHoldingPriority_Type(Unsigned32):
    """Custom type vncsVpHoldingPriority based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VncsVpHoldingPriority_Type.__name__ = "Unsigned32"
_VncsVpHoldingPriority_Object = MibTableColumn
vncsVpHoldingPriority = _VncsVpHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 2),
    _VncsVpHoldingPriority_Type()
)
vncsVpHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpHoldingPriority.setStatus("mandatory")


class _VncsVpBumpPreference_Type(Integer32):
    """Custom type vncsVpBumpPreference based on Integer32"""
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


_VncsVpBumpPreference_Type.__name__ = "Integer32"
_VncsVpBumpPreference_Object = MibTableColumn
vncsVpBumpPreference = _VncsVpBumpPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 3),
    _VncsVpBumpPreference_Type()
)
vncsVpBumpPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpBumpPreference.setStatus("mandatory")


class _VncsVpRequiredTrafficType_Type(Integer32):
    """Custom type vncsVpRequiredTrafficType based on Integer32"""
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


_VncsVpRequiredTrafficType_Type.__name__ = "Integer32"
_VncsVpRequiredTrafficType_Object = MibTableColumn
vncsVpRequiredTrafficType = _VncsVpRequiredTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 6),
    _VncsVpRequiredTrafficType_Type()
)
vncsVpRequiredTrafficType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpRequiredTrafficType.setStatus("mandatory")


class _VncsVpPermittedTrunkTypes_Type(OctetString):
    """Custom type vncsVpPermittedTrunkTypes based on OctetString"""
    defaultHexValue = "f8"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_VncsVpPermittedTrunkTypes_Type.__name__ = "OctetString"
_VncsVpPermittedTrunkTypes_Object = MibTableColumn
vncsVpPermittedTrunkTypes = _VncsVpPermittedTrunkTypes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 7),
    _VncsVpPermittedTrunkTypes_Type()
)
vncsVpPermittedTrunkTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpPermittedTrunkTypes.setStatus("mandatory")


class _VncsVpRequiredSecurity_Type(Unsigned32):
    """Custom type vncsVpRequiredSecurity based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VncsVpRequiredSecurity_Type.__name__ = "Unsigned32"
_VncsVpRequiredSecurity_Object = MibTableColumn
vncsVpRequiredSecurity = _VncsVpRequiredSecurity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 8),
    _VncsVpRequiredSecurity_Type()
)
vncsVpRequiredSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpRequiredSecurity.setStatus("mandatory")


class _VncsVpRequiredCustomerParm_Type(Unsigned32):
    """Custom type vncsVpRequiredCustomerParm based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VncsVpRequiredCustomerParm_Type.__name__ = "Unsigned32"
_VncsVpRequiredCustomerParm_Object = MibTableColumn
vncsVpRequiredCustomerParm = _VncsVpRequiredCustomerParm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 9),
    _VncsVpRequiredCustomerParm_Type()
)
vncsVpRequiredCustomerParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpRequiredCustomerParm.setStatus("mandatory")


class _VncsVpPathAttributeToMinimize_Type(Integer32):
    """Custom type vncsVpPathAttributeToMinimize based on Integer32"""
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


_VncsVpPathAttributeToMinimize_Type.__name__ = "Integer32"
_VncsVpPathAttributeToMinimize_Object = MibTableColumn
vncsVpPathAttributeToMinimize = _VncsVpPathAttributeToMinimize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 10),
    _VncsVpPathAttributeToMinimize_Type()
)
vncsVpPathAttributeToMinimize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpPathAttributeToMinimize.setStatus("mandatory")


class _VncsVpMaximumAcceptableCost_Type(Unsigned32):
    """Custom type vncsVpMaximumAcceptableCost based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VncsVpMaximumAcceptableCost_Type.__name__ = "Unsigned32"
_VncsVpMaximumAcceptableCost_Object = MibTableColumn
vncsVpMaximumAcceptableCost = _VncsVpMaximumAcceptableCost_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 11),
    _VncsVpMaximumAcceptableCost_Type()
)
vncsVpMaximumAcceptableCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpMaximumAcceptableCost.setStatus("mandatory")


class _VncsVpMaximumAcceptableDelay_Type(Unsigned32):
    """Custom type vncsVpMaximumAcceptableDelay based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VncsVpMaximumAcceptableDelay_Type.__name__ = "Unsigned32"
_VncsVpMaximumAcceptableDelay_Object = MibTableColumn
vncsVpMaximumAcceptableDelay = _VncsVpMaximumAcceptableDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 12),
    _VncsVpMaximumAcceptableDelay_Type()
)
vncsVpMaximumAcceptableDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpMaximumAcceptableDelay.setStatus("mandatory")


class _VncsVpEmissionPriority_Type(Unsigned32):
    """Custom type vncsVpEmissionPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VncsVpEmissionPriority_Type.__name__ = "Unsigned32"
_VncsVpEmissionPriority_Object = MibTableColumn
vncsVpEmissionPriority = _VncsVpEmissionPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 13),
    _VncsVpEmissionPriority_Type()
)
vncsVpEmissionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpEmissionPriority.setStatus("mandatory")


class _VncsVpDiscardPriority_Type(Unsigned32):
    """Custom type vncsVpDiscardPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_VncsVpDiscardPriority_Type.__name__ = "Unsigned32"
_VncsVpDiscardPriority_Object = MibTableColumn
vncsVpDiscardPriority = _VncsVpDiscardPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 14),
    _VncsVpDiscardPriority_Type()
)
vncsVpDiscardPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpDiscardPriority.setStatus("mandatory")


class _VncsVpPathFailureAction_Type(Integer32):
    """Custom type vncsVpPathFailureAction based on Integer32"""
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


_VncsVpPathFailureAction_Type.__name__ = "Integer32"
_VncsVpPathFailureAction_Object = MibTableColumn
vncsVpPathFailureAction = _VncsVpPathFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 15),
    _VncsVpPathFailureAction_Type()
)
vncsVpPathFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpPathFailureAction.setStatus("mandatory")


class _VncsVpOptimization_Type(Integer32):
    """Custom type vncsVpOptimization based on Integer32"""
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


_VncsVpOptimization_Type.__name__ = "Integer32"
_VncsVpOptimization_Object = MibTableColumn
vncsVpOptimization = _VncsVpOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 2, 1, 16),
    _VncsVpOptimization_Type()
)
vncsVpOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpOptimization.setStatus("mandatory")
_VncsVpFrOpsTable_Object = MibTable
vncsVpFrOpsTable = _VncsVpFrOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3)
)
if mibBuilder.loadTexts:
    vncsVpFrOpsTable.setStatus("mandatory")
_VncsVpFrOpsEntry_Object = MibTableRow
vncsVpFrOpsEntry = _VncsVpFrOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1)
)
vncsVpFrOpsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
)
if mibBuilder.loadTexts:
    vncsVpFrOpsEntry.setStatus("mandatory")


class _VncsVpMaxVoiceBitRate_Type(Integer32):
    """Custom type vncsVpMaxVoiceBitRate based on Integer32"""
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


_VncsVpMaxVoiceBitRate_Type.__name__ = "Integer32"
_VncsVpMaxVoiceBitRate_Object = MibTableColumn
vncsVpMaxVoiceBitRate = _VncsVpMaxVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 1),
    _VncsVpMaxVoiceBitRate_Type()
)
vncsVpMaxVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpMaxVoiceBitRate.setStatus("obsolete")


class _VncsVpMinVoiceBitRate_Type(Integer32):
    """Custom type vncsVpMinVoiceBitRate based on Integer32"""
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


_VncsVpMinVoiceBitRate_Type.__name__ = "Integer32"
_VncsVpMinVoiceBitRate_Object = MibTableColumn
vncsVpMinVoiceBitRate = _VncsVpMinVoiceBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 2),
    _VncsVpMinVoiceBitRate_Type()
)
vncsVpMinVoiceBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpMinVoiceBitRate.setStatus("obsolete")


class _VncsVpMaxModemBitRate_Type(Integer32):
    """Custom type vncsVpMaxModemBitRate based on Integer32"""
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


_VncsVpMaxModemBitRate_Type.__name__ = "Integer32"
_VncsVpMaxModemBitRate_Object = MibTableColumn
vncsVpMaxModemBitRate = _VncsVpMaxModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 3),
    _VncsVpMaxModemBitRate_Type()
)
vncsVpMaxModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpMaxModemBitRate.setStatus("obsolete")


class _VncsVpMinModemBitRate_Type(Integer32):
    """Custom type vncsVpMinModemBitRate based on Integer32"""
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


_VncsVpMinModemBitRate_Type.__name__ = "Integer32"
_VncsVpMinModemBitRate_Object = MibTableColumn
vncsVpMinModemBitRate = _VncsVpMinModemBitRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 4),
    _VncsVpMinModemBitRate_Type()
)
vncsVpMinModemBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpMinModemBitRate.setStatus("obsolete")


class _VncsVpAudioGain_Type(Integer32):
    """Custom type vncsVpAudioGain based on Integer32"""
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


_VncsVpAudioGain_Type.__name__ = "Integer32"
_VncsVpAudioGain_Object = MibTableColumn
vncsVpAudioGain = _VncsVpAudioGain_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 5),
    _VncsVpAudioGain_Type()
)
vncsVpAudioGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpAudioGain.setStatus("obsolete")


class _VncsVpSilenceSuppression_Type(Integer32):
    """Custom type vncsVpSilenceSuppression based on Integer32"""
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


_VncsVpSilenceSuppression_Type.__name__ = "Integer32"
_VncsVpSilenceSuppression_Object = MibTableColumn
vncsVpSilenceSuppression = _VncsVpSilenceSuppression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 6),
    _VncsVpSilenceSuppression_Type()
)
vncsVpSilenceSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpSilenceSuppression.setStatus("mandatory")


class _VncsVpEchoCancellation_Type(Integer32):
    """Custom type vncsVpEchoCancellation based on Integer32"""
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


_VncsVpEchoCancellation_Type.__name__ = "Integer32"
_VncsVpEchoCancellation_Object = MibTableColumn
vncsVpEchoCancellation = _VncsVpEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 7),
    _VncsVpEchoCancellation_Type()
)
vncsVpEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpEchoCancellation.setStatus("obsolete")


class _VncsVpSilenceSuppressionFactor_Type(Unsigned32):
    """Custom type vncsVpSilenceSuppressionFactor based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_VncsVpSilenceSuppressionFactor_Type.__name__ = "Unsigned32"
_VncsVpSilenceSuppressionFactor_Object = MibTableColumn
vncsVpSilenceSuppressionFactor = _VncsVpSilenceSuppressionFactor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 8),
    _VncsVpSilenceSuppressionFactor_Type()
)
vncsVpSilenceSuppressionFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpSilenceSuppressionFactor.setStatus("mandatory")


class _VncsVpDataCallsAccepted_Type(Integer32):
    """Custom type vncsVpDataCallsAccepted based on Integer32"""
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


_VncsVpDataCallsAccepted_Type.__name__ = "Integer32"
_VncsVpDataCallsAccepted_Object = MibTableColumn
vncsVpDataCallsAccepted = _VncsVpDataCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 9),
    _VncsVpDataCallsAccepted_Type()
)
vncsVpDataCallsAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpDataCallsAccepted.setStatus("mandatory")


class _VncsVpFaxIdleSuppressionG711G726_Type(Integer32):
    """Custom type vncsVpFaxIdleSuppressionG711G726 based on Integer32"""
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


_VncsVpFaxIdleSuppressionG711G726_Type.__name__ = "Integer32"
_VncsVpFaxIdleSuppressionG711G726_Object = MibTableColumn
vncsVpFaxIdleSuppressionG711G726 = _VncsVpFaxIdleSuppressionG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 15),
    _VncsVpFaxIdleSuppressionG711G726_Type()
)
vncsVpFaxIdleSuppressionG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpFaxIdleSuppressionG711G726.setStatus("mandatory")


class _VncsVpInsertedOutputDelay_Type(Integer32):
    """Custom type vncsVpInsertedOutputDelay based on Integer32"""
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


_VncsVpInsertedOutputDelay_Type.__name__ = "Integer32"
_VncsVpInsertedOutputDelay_Object = MibTableColumn
vncsVpInsertedOutputDelay = _VncsVpInsertedOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 17),
    _VncsVpInsertedOutputDelay_Type()
)
vncsVpInsertedOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpInsertedOutputDelay.setStatus("mandatory")


class _VncsVpVoiceTrafficOptimization_Type(Integer32):
    """Custom type vncsVpVoiceTrafficOptimization based on Integer32"""
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


_VncsVpVoiceTrafficOptimization_Type.__name__ = "Integer32"
_VncsVpVoiceTrafficOptimization_Object = MibTableColumn
vncsVpVoiceTrafficOptimization = _VncsVpVoiceTrafficOptimization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 18),
    _VncsVpVoiceTrafficOptimization_Type()
)
vncsVpVoiceTrafficOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpVoiceTrafficOptimization.setStatus("obsolete")


class _VncsVpDtmfRegeneration_Type(Integer32):
    """Custom type vncsVpDtmfRegeneration based on Integer32"""
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


_VncsVpDtmfRegeneration_Type.__name__ = "Integer32"
_VncsVpDtmfRegeneration_Object = MibTableColumn
vncsVpDtmfRegeneration = _VncsVpDtmfRegeneration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 19),
    _VncsVpDtmfRegeneration_Type()
)
vncsVpDtmfRegeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpDtmfRegeneration.setStatus("mandatory")


class _VncsVpV17EncodedAsG711G726_Type(Integer32):
    """Custom type vncsVpV17EncodedAsG711G726 based on Integer32"""
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


_VncsVpV17EncodedAsG711G726_Type.__name__ = "Integer32"
_VncsVpV17EncodedAsG711G726_Object = MibTableColumn
vncsVpV17EncodedAsG711G726 = _VncsVpV17EncodedAsG711G726_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 3, 1, 20),
    _VncsVpV17EncodedAsG711G726_Type()
)
vncsVpV17EncodedAsG711G726.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpV17EncodedAsG711G726.setStatus("mandatory")
_VncsVpStatsTable_Object = MibTable
vncsVpStatsTable = _VncsVpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 4)
)
if mibBuilder.loadTexts:
    vncsVpStatsTable.setStatus("mandatory")
_VncsVpStatsEntry_Object = MibTableRow
vncsVpStatsEntry = _VncsVpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 4, 1)
)
vncsVpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
)
if mibBuilder.loadTexts:
    vncsVpStatsEntry.setStatus("mandatory")


class _VncsVpUsageCount_Type(Unsigned32):
    """Custom type vncsVpUsageCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VncsVpUsageCount_Type.__name__ = "Unsigned32"
_VncsVpUsageCount_Object = MibTableColumn
vncsVpUsageCount = _VncsVpUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 4, 1, 1),
    _VncsVpUsageCount_Type()
)
vncsVpUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsVpUsageCount.setStatus("mandatory")
_VncsVpVoiceRatesTable_Object = MibTable
vncsVpVoiceRatesTable = _VncsVpVoiceRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 322)
)
if mibBuilder.loadTexts:
    vncsVpVoiceRatesTable.setStatus("obsolete")
_VncsVpVoiceRatesEntry_Object = MibTableRow
vncsVpVoiceRatesEntry = _VncsVpVoiceRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 322, 1)
)
vncsVpVoiceRatesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpVoiceRatesEncodingIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpVoiceRatesRateIndex"),
)
if mibBuilder.loadTexts:
    vncsVpVoiceRatesEntry.setStatus("obsolete")


class _VncsVpVoiceRatesEncodingIndex_Type(Integer32):
    """Custom type vncsVpVoiceRatesEncodingIndex based on Integer32"""
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


_VncsVpVoiceRatesEncodingIndex_Type.__name__ = "Integer32"
_VncsVpVoiceRatesEncodingIndex_Object = MibTableColumn
vncsVpVoiceRatesEncodingIndex = _VncsVpVoiceRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 322, 1, 1),
    _VncsVpVoiceRatesEncodingIndex_Type()
)
vncsVpVoiceRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpVoiceRatesEncodingIndex.setStatus("obsolete")


class _VncsVpVoiceRatesRateIndex_Type(Integer32):
    """Custom type vncsVpVoiceRatesRateIndex based on Integer32"""
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


_VncsVpVoiceRatesRateIndex_Type.__name__ = "Integer32"
_VncsVpVoiceRatesRateIndex_Object = MibTableColumn
vncsVpVoiceRatesRateIndex = _VncsVpVoiceRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 322, 1, 2),
    _VncsVpVoiceRatesRateIndex_Type()
)
vncsVpVoiceRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpVoiceRatesRateIndex.setStatus("obsolete")


class _VncsVpVoiceRatesValue_Type(FixedPoint1):
    """Custom type vncsVpVoiceRatesValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(640, 640),
    )


_VncsVpVoiceRatesValue_Type.__name__ = "FixedPoint1"
_VncsVpVoiceRatesValue_Object = MibTableColumn
vncsVpVoiceRatesValue = _VncsVpVoiceRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 322, 1, 3),
    _VncsVpVoiceRatesValue_Type()
)
vncsVpVoiceRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpVoiceRatesValue.setStatus("obsolete")
_VncsVpVoiceEncodingChoiceTable_Object = MibTable
vncsVpVoiceEncodingChoiceTable = _VncsVpVoiceEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 323)
)
if mibBuilder.loadTexts:
    vncsVpVoiceEncodingChoiceTable.setStatus("obsolete")
_VncsVpVoiceEncodingChoiceEntry_Object = MibTableRow
vncsVpVoiceEncodingChoiceEntry = _VncsVpVoiceEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 323, 1)
)
vncsVpVoiceEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpVoiceEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    vncsVpVoiceEncodingChoiceEntry.setStatus("obsolete")


class _VncsVpVoiceEncodingChoiceIndex_Type(Integer32):
    """Custom type vncsVpVoiceEncodingChoiceIndex based on Integer32"""
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


_VncsVpVoiceEncodingChoiceIndex_Type.__name__ = "Integer32"
_VncsVpVoiceEncodingChoiceIndex_Object = MibTableColumn
vncsVpVoiceEncodingChoiceIndex = _VncsVpVoiceEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 323, 1, 1),
    _VncsVpVoiceEncodingChoiceIndex_Type()
)
vncsVpVoiceEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpVoiceEncodingChoiceIndex.setStatus("obsolete")


class _VncsVpVoiceEncodingChoiceValue_Type(Integer32):
    """Custom type vncsVpVoiceEncodingChoiceValue based on Integer32"""
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


_VncsVpVoiceEncodingChoiceValue_Type.__name__ = "Integer32"
_VncsVpVoiceEncodingChoiceValue_Object = MibTableColumn
vncsVpVoiceEncodingChoiceValue = _VncsVpVoiceEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 323, 1, 2),
    _VncsVpVoiceEncodingChoiceValue_Type()
)
vncsVpVoiceEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpVoiceEncodingChoiceValue.setStatus("obsolete")
_VncsVpModemFaxRatesTable_Object = MibTable
vncsVpModemFaxRatesTable = _VncsVpModemFaxRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 324)
)
if mibBuilder.loadTexts:
    vncsVpModemFaxRatesTable.setStatus("obsolete")
_VncsVpModemFaxRatesEntry_Object = MibTableRow
vncsVpModemFaxRatesEntry = _VncsVpModemFaxRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 324, 1)
)
vncsVpModemFaxRatesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpModemFaxRatesEncodingIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpModemFaxRatesRateIndex"),
)
if mibBuilder.loadTexts:
    vncsVpModemFaxRatesEntry.setStatus("obsolete")


class _VncsVpModemFaxRatesEncodingIndex_Type(Integer32):
    """Custom type vncsVpModemFaxRatesEncodingIndex based on Integer32"""
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


_VncsVpModemFaxRatesEncodingIndex_Type.__name__ = "Integer32"
_VncsVpModemFaxRatesEncodingIndex_Object = MibTableColumn
vncsVpModemFaxRatesEncodingIndex = _VncsVpModemFaxRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 324, 1, 1),
    _VncsVpModemFaxRatesEncodingIndex_Type()
)
vncsVpModemFaxRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpModemFaxRatesEncodingIndex.setStatus("obsolete")


class _VncsVpModemFaxRatesRateIndex_Type(Integer32):
    """Custom type vncsVpModemFaxRatesRateIndex based on Integer32"""
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


_VncsVpModemFaxRatesRateIndex_Type.__name__ = "Integer32"
_VncsVpModemFaxRatesRateIndex_Object = MibTableColumn
vncsVpModemFaxRatesRateIndex = _VncsVpModemFaxRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 324, 1, 2),
    _VncsVpModemFaxRatesRateIndex_Type()
)
vncsVpModemFaxRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpModemFaxRatesRateIndex.setStatus("obsolete")


class _VncsVpModemFaxRatesValue_Type(FixedPoint1):
    """Custom type vncsVpModemFaxRatesValue based on FixedPoint1"""
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


_VncsVpModemFaxRatesValue_Type.__name__ = "FixedPoint1"
_VncsVpModemFaxRatesValue_Object = MibTableColumn
vncsVpModemFaxRatesValue = _VncsVpModemFaxRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 324, 1, 3),
    _VncsVpModemFaxRatesValue_Type()
)
vncsVpModemFaxRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpModemFaxRatesValue.setStatus("obsolete")
_VncsVpModemFaxEncodingChoiceTable_Object = MibTable
vncsVpModemFaxEncodingChoiceTable = _VncsVpModemFaxEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 325)
)
if mibBuilder.loadTexts:
    vncsVpModemFaxEncodingChoiceTable.setStatus("obsolete")
_VncsVpModemFaxEncodingChoiceEntry_Object = MibTableRow
vncsVpModemFaxEncodingChoiceEntry = _VncsVpModemFaxEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 325, 1)
)
vncsVpModemFaxEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpModemFaxEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    vncsVpModemFaxEncodingChoiceEntry.setStatus("obsolete")


class _VncsVpModemFaxEncodingChoiceIndex_Type(Integer32):
    """Custom type vncsVpModemFaxEncodingChoiceIndex based on Integer32"""
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


_VncsVpModemFaxEncodingChoiceIndex_Type.__name__ = "Integer32"
_VncsVpModemFaxEncodingChoiceIndex_Object = MibTableColumn
vncsVpModemFaxEncodingChoiceIndex = _VncsVpModemFaxEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 325, 1, 1),
    _VncsVpModemFaxEncodingChoiceIndex_Type()
)
vncsVpModemFaxEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpModemFaxEncodingChoiceIndex.setStatus("obsolete")


class _VncsVpModemFaxEncodingChoiceValue_Type(Integer32):
    """Custom type vncsVpModemFaxEncodingChoiceValue based on Integer32"""
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


_VncsVpModemFaxEncodingChoiceValue_Type.__name__ = "Integer32"
_VncsVpModemFaxEncodingChoiceValue_Object = MibTableColumn
vncsVpModemFaxEncodingChoiceValue = _VncsVpModemFaxEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 325, 1, 2),
    _VncsVpModemFaxEncodingChoiceValue_Type()
)
vncsVpModemFaxEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpModemFaxEncodingChoiceValue.setStatus("obsolete")
_VncsVpNewVoiceRatesTable_Object = MibTable
vncsVpNewVoiceRatesTable = _VncsVpNewVoiceRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 381)
)
if mibBuilder.loadTexts:
    vncsVpNewVoiceRatesTable.setStatus("mandatory")
_VncsVpNewVoiceRatesEntry_Object = MibTableRow
vncsVpNewVoiceRatesEntry = _VncsVpNewVoiceRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 381, 1)
)
vncsVpNewVoiceRatesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpNewVoiceRatesEncodingIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpNewVoiceRatesRateIndex"),
)
if mibBuilder.loadTexts:
    vncsVpNewVoiceRatesEntry.setStatus("mandatory")


class _VncsVpNewVoiceRatesEncodingIndex_Type(Integer32):
    """Custom type vncsVpNewVoiceRatesEncodingIndex based on Integer32"""
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


_VncsVpNewVoiceRatesEncodingIndex_Type.__name__ = "Integer32"
_VncsVpNewVoiceRatesEncodingIndex_Object = MibTableColumn
vncsVpNewVoiceRatesEncodingIndex = _VncsVpNewVoiceRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 381, 1, 1),
    _VncsVpNewVoiceRatesEncodingIndex_Type()
)
vncsVpNewVoiceRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpNewVoiceRatesEncodingIndex.setStatus("mandatory")


class _VncsVpNewVoiceRatesRateIndex_Type(Integer32):
    """Custom type vncsVpNewVoiceRatesRateIndex based on Integer32"""
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


_VncsVpNewVoiceRatesRateIndex_Type.__name__ = "Integer32"
_VncsVpNewVoiceRatesRateIndex_Object = MibTableColumn
vncsVpNewVoiceRatesRateIndex = _VncsVpNewVoiceRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 381, 1, 2),
    _VncsVpNewVoiceRatesRateIndex_Type()
)
vncsVpNewVoiceRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpNewVoiceRatesRateIndex.setStatus("mandatory")


class _VncsVpNewVoiceRatesValue_Type(FixedPoint1):
    """Custom type vncsVpNewVoiceRatesValue based on FixedPoint1"""
    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(160, 160),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(320, 320),
        ValueRangeConstraint(640, 640),
    )


_VncsVpNewVoiceRatesValue_Type.__name__ = "FixedPoint1"
_VncsVpNewVoiceRatesValue_Object = MibTableColumn
vncsVpNewVoiceRatesValue = _VncsVpNewVoiceRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 381, 1, 3),
    _VncsVpNewVoiceRatesValue_Type()
)
vncsVpNewVoiceRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpNewVoiceRatesValue.setStatus("mandatory")
_VncsVpNewVoiceEncodingChoiceTable_Object = MibTable
vncsVpNewVoiceEncodingChoiceTable = _VncsVpNewVoiceEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 382)
)
if mibBuilder.loadTexts:
    vncsVpNewVoiceEncodingChoiceTable.setStatus("mandatory")
_VncsVpNewVoiceEncodingChoiceEntry_Object = MibTableRow
vncsVpNewVoiceEncodingChoiceEntry = _VncsVpNewVoiceEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 382, 1)
)
vncsVpNewVoiceEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpNewVoiceEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    vncsVpNewVoiceEncodingChoiceEntry.setStatus("mandatory")


class _VncsVpNewVoiceEncodingChoiceIndex_Type(Integer32):
    """Custom type vncsVpNewVoiceEncodingChoiceIndex based on Integer32"""
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


_VncsVpNewVoiceEncodingChoiceIndex_Type.__name__ = "Integer32"
_VncsVpNewVoiceEncodingChoiceIndex_Object = MibTableColumn
vncsVpNewVoiceEncodingChoiceIndex = _VncsVpNewVoiceEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 382, 1, 1),
    _VncsVpNewVoiceEncodingChoiceIndex_Type()
)
vncsVpNewVoiceEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpNewVoiceEncodingChoiceIndex.setStatus("mandatory")


class _VncsVpNewVoiceEncodingChoiceValue_Type(Integer32):
    """Custom type vncsVpNewVoiceEncodingChoiceValue based on Integer32"""
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


_VncsVpNewVoiceEncodingChoiceValue_Type.__name__ = "Integer32"
_VncsVpNewVoiceEncodingChoiceValue_Object = MibTableColumn
vncsVpNewVoiceEncodingChoiceValue = _VncsVpNewVoiceEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 382, 1, 2),
    _VncsVpNewVoiceEncodingChoiceValue_Type()
)
vncsVpNewVoiceEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpNewVoiceEncodingChoiceValue.setStatus("mandatory")
_VncsVpNewModemFaxRatesTable_Object = MibTable
vncsVpNewModemFaxRatesTable = _VncsVpNewModemFaxRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 383)
)
if mibBuilder.loadTexts:
    vncsVpNewModemFaxRatesTable.setStatus("mandatory")
_VncsVpNewModemFaxRatesEntry_Object = MibTableRow
vncsVpNewModemFaxRatesEntry = _VncsVpNewModemFaxRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 383, 1)
)
vncsVpNewModemFaxRatesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpNewModemFaxRatesEncodingIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpNewModemFaxRatesRateIndex"),
)
if mibBuilder.loadTexts:
    vncsVpNewModemFaxRatesEntry.setStatus("mandatory")


class _VncsVpNewModemFaxRatesEncodingIndex_Type(Integer32):
    """Custom type vncsVpNewModemFaxRatesEncodingIndex based on Integer32"""
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


_VncsVpNewModemFaxRatesEncodingIndex_Type.__name__ = "Integer32"
_VncsVpNewModemFaxRatesEncodingIndex_Object = MibTableColumn
vncsVpNewModemFaxRatesEncodingIndex = _VncsVpNewModemFaxRatesEncodingIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 383, 1, 1),
    _VncsVpNewModemFaxRatesEncodingIndex_Type()
)
vncsVpNewModemFaxRatesEncodingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpNewModemFaxRatesEncodingIndex.setStatus("mandatory")


class _VncsVpNewModemFaxRatesRateIndex_Type(Integer32):
    """Custom type vncsVpNewModemFaxRatesRateIndex based on Integer32"""
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


_VncsVpNewModemFaxRatesRateIndex_Type.__name__ = "Integer32"
_VncsVpNewModemFaxRatesRateIndex_Object = MibTableColumn
vncsVpNewModemFaxRatesRateIndex = _VncsVpNewModemFaxRatesRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 383, 1, 2),
    _VncsVpNewModemFaxRatesRateIndex_Type()
)
vncsVpNewModemFaxRatesRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpNewModemFaxRatesRateIndex.setStatus("mandatory")


class _VncsVpNewModemFaxRatesValue_Type(FixedPoint1):
    """Custom type vncsVpNewModemFaxRatesValue based on FixedPoint1"""
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


_VncsVpNewModemFaxRatesValue_Type.__name__ = "FixedPoint1"
_VncsVpNewModemFaxRatesValue_Object = MibTableColumn
vncsVpNewModemFaxRatesValue = _VncsVpNewModemFaxRatesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 383, 1, 3),
    _VncsVpNewModemFaxRatesValue_Type()
)
vncsVpNewModemFaxRatesValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpNewModemFaxRatesValue.setStatus("mandatory")
_VncsVpNewModemFaxEncodingChoiceTable_Object = MibTable
vncsVpNewModemFaxEncodingChoiceTable = _VncsVpNewModemFaxEncodingChoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 384)
)
if mibBuilder.loadTexts:
    vncsVpNewModemFaxEncodingChoiceTable.setStatus("mandatory")
_VncsVpNewModemFaxEncodingChoiceEntry_Object = MibTableRow
vncsVpNewModemFaxEncodingChoiceEntry = _VncsVpNewModemFaxEncodingChoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 384, 1)
)
vncsVpNewModemFaxEncodingChoiceEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVpNewModemFaxEncodingChoiceIndex"),
)
if mibBuilder.loadTexts:
    vncsVpNewModemFaxEncodingChoiceEntry.setStatus("mandatory")


class _VncsVpNewModemFaxEncodingChoiceIndex_Type(Integer32):
    """Custom type vncsVpNewModemFaxEncodingChoiceIndex based on Integer32"""
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


_VncsVpNewModemFaxEncodingChoiceIndex_Type.__name__ = "Integer32"
_VncsVpNewModemFaxEncodingChoiceIndex_Object = MibTableColumn
vncsVpNewModemFaxEncodingChoiceIndex = _VncsVpNewModemFaxEncodingChoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 384, 1, 1),
    _VncsVpNewModemFaxEncodingChoiceIndex_Type()
)
vncsVpNewModemFaxEncodingChoiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vncsVpNewModemFaxEncodingChoiceIndex.setStatus("mandatory")


class _VncsVpNewModemFaxEncodingChoiceValue_Type(Integer32):
    """Custom type vncsVpNewModemFaxEncodingChoiceValue based on Integer32"""
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


_VncsVpNewModemFaxEncodingChoiceValue_Type.__name__ = "Integer32"
_VncsVpNewModemFaxEncodingChoiceValue_Object = MibTableColumn
vncsVpNewModemFaxEncodingChoiceValue = _VncsVpNewModemFaxEncodingChoiceValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 3, 384, 1, 2),
    _VncsVpNewModemFaxEncodingChoiceValue_Type()
)
vncsVpNewModemFaxEncodingChoiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsVpNewModemFaxEncodingChoiceValue.setStatus("mandatory")
_VncsProvTable_Object = MibTable
vncsProvTable = _VncsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 10)
)
if mibBuilder.loadTexts:
    vncsProvTable.setStatus("mandatory")
_VncsProvEntry_Object = MibTableRow
vncsProvEntry = _VncsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 10, 1)
)
vncsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
)
if mibBuilder.loadTexts:
    vncsProvEntry.setStatus("mandatory")


class _VncsCommentText_Type(AsciiString):
    """Custom type vncsCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VncsCommentText_Type.__name__ = "AsciiString"
_VncsCommentText_Object = MibTableColumn
vncsCommentText = _VncsCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 10, 1, 1),
    _VncsCommentText_Type()
)
vncsCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vncsCommentText.setStatus("mandatory")
_VncsStatsTable_Object = MibTable
vncsStatsTable = _VncsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 11)
)
if mibBuilder.loadTexts:
    vncsStatsTable.setStatus("mandatory")
_VncsStatsEntry_Object = MibTableRow
vncsStatsEntry = _VncsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 11, 1)
)
vncsStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
)
if mibBuilder.loadTexts:
    vncsStatsEntry.setStatus("mandatory")
_VncsTotalTranslations_Type = Counter32
_VncsTotalTranslations_Object = MibTableColumn
vncsTotalTranslations = _VncsTotalTranslations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 11, 1, 1),
    _VncsTotalTranslations_Type()
)
vncsTotalTranslations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsTotalTranslations.setStatus("mandatory")
_VncsVRoutesTable_Object = MibTable
vncsVRoutesTable = _VncsVRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 305)
)
if mibBuilder.loadTexts:
    vncsVRoutesTable.setStatus("mandatory")
_VncsVRoutesEntry_Object = MibTableRow
vncsVRoutesEntry = _VncsVRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 305, 1)
)
vncsVRoutesEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsIndex"),
    (0, "Nortel-Magellan-Passport-VncsCallServerMIB", "vncsVRoutesValue"),
)
if mibBuilder.loadTexts:
    vncsVRoutesEntry.setStatus("mandatory")
_VncsVRoutesValue_Type = Link
_VncsVRoutesValue_Object = MibTableColumn
vncsVRoutesValue = _VncsVRoutesValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 44, 305, 1, 1),
    _VncsVRoutesValue_Type()
)
vncsVRoutesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vncsVRoutesValue.setStatus("mandatory")
_VncsCallServerMIB_ObjectIdentity = ObjectIdentity
vncsCallServerMIB = _VncsCallServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66)
)
_VncsCallServerGroup_ObjectIdentity = ObjectIdentity
vncsCallServerGroup = _VncsCallServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 1)
)
_VncsCallServerGroupBE_ObjectIdentity = ObjectIdentity
vncsCallServerGroupBE = _VncsCallServerGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 1, 5)
)
_VncsCallServerGroupBE01_ObjectIdentity = ObjectIdentity
vncsCallServerGroupBE01 = _VncsCallServerGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 1, 5, 2)
)
_VncsCallServerGroupBE01A_ObjectIdentity = ObjectIdentity
vncsCallServerGroupBE01A = _VncsCallServerGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 1, 5, 2, 2)
)
_VncsCallServerCapabilities_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilities = _VncsCallServerCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 3)
)
_VncsCallServerCapabilitiesBE_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilitiesBE = _VncsCallServerCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 3, 5)
)
_VncsCallServerCapabilitiesBE01_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilitiesBE01 = _VncsCallServerCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 3, 5, 2)
)
_VncsCallServerCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
vncsCallServerCapabilitiesBE01A = _VncsCallServerCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 66, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-VncsCallServerMIB",
    **{"vncs": vncs,
       "vncsRowStatusTable": vncsRowStatusTable,
       "vncsRowStatusEntry": vncsRowStatusEntry,
       "vncsRowStatus": vncsRowStatus,
       "vncsComponentName": vncsComponentName,
       "vncsStorageType": vncsStorageType,
       "vncsIndex": vncsIndex,
       "vncsDP": vncsDP,
       "vncsDPRowStatusTable": vncsDPRowStatusTable,
       "vncsDPRowStatusEntry": vncsDPRowStatusEntry,
       "vncsDPRowStatus": vncsDPRowStatus,
       "vncsDPComponentName": vncsDPComponentName,
       "vncsDPStorageType": vncsDPStorageType,
       "vncsDPIndex": vncsDPIndex,
       "vncsDPDn": vncsDPDn,
       "vncsDPDnRowStatusTable": vncsDPDnRowStatusTable,
       "vncsDPDnRowStatusEntry": vncsDPDnRowStatusEntry,
       "vncsDPDnRowStatus": vncsDPDnRowStatus,
       "vncsDPDnComponentName": vncsDPDnComponentName,
       "vncsDPDnStorageType": vncsDPDnStorageType,
       "vncsDPDnIndex": vncsDPDnIndex,
       "vncsDPDnProvTable": vncsDPDnProvTable,
       "vncsDPDnProvEntry": vncsDPDnProvEntry,
       "vncsDPDnDestinationNodeId": vncsDPDnDestinationNodeId,
       "vncsDPDnDestinationComponentId": vncsDPDnDestinationComponentId,
       "vncsDPDnVoiceProfileNumber": vncsDPDnVoiceProfileNumber,
       "vncsDPDnNumberingPlanIndicator": vncsDPDnNumberingPlanIndicator,
       "vncsDPDnDataNetworkAddress": vncsDPDnDataNetworkAddress,
       "vncsDPStatsTable": vncsDPStatsTable,
       "vncsDPStatsEntry": vncsDPStatsEntry,
       "vncsDPCompleteTranslations": vncsDPCompleteTranslations,
       "vncsDPIncompleteTranslations": vncsDPIncompleteTranslations,
       "vncsDPFailedTranslations": vncsDPFailedTranslations,
       "vncsVp": vncsVp,
       "vncsVpRowStatusTable": vncsVpRowStatusTable,
       "vncsVpRowStatusEntry": vncsVpRowStatusEntry,
       "vncsVpRowStatus": vncsVpRowStatus,
       "vncsVpComponentName": vncsVpComponentName,
       "vncsVpStorageType": vncsVpStorageType,
       "vncsVpIndex": vncsVpIndex,
       "vncsVpLCOpsTable": vncsVpLCOpsTable,
       "vncsVpLCOpsEntry": vncsVpLCOpsEntry,
       "vncsVpSetupPriority": vncsVpSetupPriority,
       "vncsVpHoldingPriority": vncsVpHoldingPriority,
       "vncsVpBumpPreference": vncsVpBumpPreference,
       "vncsVpRequiredTrafficType": vncsVpRequiredTrafficType,
       "vncsVpPermittedTrunkTypes": vncsVpPermittedTrunkTypes,
       "vncsVpRequiredSecurity": vncsVpRequiredSecurity,
       "vncsVpRequiredCustomerParm": vncsVpRequiredCustomerParm,
       "vncsVpPathAttributeToMinimize": vncsVpPathAttributeToMinimize,
       "vncsVpMaximumAcceptableCost": vncsVpMaximumAcceptableCost,
       "vncsVpMaximumAcceptableDelay": vncsVpMaximumAcceptableDelay,
       "vncsVpEmissionPriority": vncsVpEmissionPriority,
       "vncsVpDiscardPriority": vncsVpDiscardPriority,
       "vncsVpPathFailureAction": vncsVpPathFailureAction,
       "vncsVpOptimization": vncsVpOptimization,
       "vncsVpFrOpsTable": vncsVpFrOpsTable,
       "vncsVpFrOpsEntry": vncsVpFrOpsEntry,
       "vncsVpMaxVoiceBitRate": vncsVpMaxVoiceBitRate,
       "vncsVpMinVoiceBitRate": vncsVpMinVoiceBitRate,
       "vncsVpMaxModemBitRate": vncsVpMaxModemBitRate,
       "vncsVpMinModemBitRate": vncsVpMinModemBitRate,
       "vncsVpAudioGain": vncsVpAudioGain,
       "vncsVpSilenceSuppression": vncsVpSilenceSuppression,
       "vncsVpEchoCancellation": vncsVpEchoCancellation,
       "vncsVpSilenceSuppressionFactor": vncsVpSilenceSuppressionFactor,
       "vncsVpDataCallsAccepted": vncsVpDataCallsAccepted,
       "vncsVpFaxIdleSuppressionG711G726": vncsVpFaxIdleSuppressionG711G726,
       "vncsVpInsertedOutputDelay": vncsVpInsertedOutputDelay,
       "vncsVpVoiceTrafficOptimization": vncsVpVoiceTrafficOptimization,
       "vncsVpDtmfRegeneration": vncsVpDtmfRegeneration,
       "vncsVpV17EncodedAsG711G726": vncsVpV17EncodedAsG711G726,
       "vncsVpStatsTable": vncsVpStatsTable,
       "vncsVpStatsEntry": vncsVpStatsEntry,
       "vncsVpUsageCount": vncsVpUsageCount,
       "vncsVpVoiceRatesTable": vncsVpVoiceRatesTable,
       "vncsVpVoiceRatesEntry": vncsVpVoiceRatesEntry,
       "vncsVpVoiceRatesEncodingIndex": vncsVpVoiceRatesEncodingIndex,
       "vncsVpVoiceRatesRateIndex": vncsVpVoiceRatesRateIndex,
       "vncsVpVoiceRatesValue": vncsVpVoiceRatesValue,
       "vncsVpVoiceEncodingChoiceTable": vncsVpVoiceEncodingChoiceTable,
       "vncsVpVoiceEncodingChoiceEntry": vncsVpVoiceEncodingChoiceEntry,
       "vncsVpVoiceEncodingChoiceIndex": vncsVpVoiceEncodingChoiceIndex,
       "vncsVpVoiceEncodingChoiceValue": vncsVpVoiceEncodingChoiceValue,
       "vncsVpModemFaxRatesTable": vncsVpModemFaxRatesTable,
       "vncsVpModemFaxRatesEntry": vncsVpModemFaxRatesEntry,
       "vncsVpModemFaxRatesEncodingIndex": vncsVpModemFaxRatesEncodingIndex,
       "vncsVpModemFaxRatesRateIndex": vncsVpModemFaxRatesRateIndex,
       "vncsVpModemFaxRatesValue": vncsVpModemFaxRatesValue,
       "vncsVpModemFaxEncodingChoiceTable": vncsVpModemFaxEncodingChoiceTable,
       "vncsVpModemFaxEncodingChoiceEntry": vncsVpModemFaxEncodingChoiceEntry,
       "vncsVpModemFaxEncodingChoiceIndex": vncsVpModemFaxEncodingChoiceIndex,
       "vncsVpModemFaxEncodingChoiceValue": vncsVpModemFaxEncodingChoiceValue,
       "vncsVpNewVoiceRatesTable": vncsVpNewVoiceRatesTable,
       "vncsVpNewVoiceRatesEntry": vncsVpNewVoiceRatesEntry,
       "vncsVpNewVoiceRatesEncodingIndex": vncsVpNewVoiceRatesEncodingIndex,
       "vncsVpNewVoiceRatesRateIndex": vncsVpNewVoiceRatesRateIndex,
       "vncsVpNewVoiceRatesValue": vncsVpNewVoiceRatesValue,
       "vncsVpNewVoiceEncodingChoiceTable": vncsVpNewVoiceEncodingChoiceTable,
       "vncsVpNewVoiceEncodingChoiceEntry": vncsVpNewVoiceEncodingChoiceEntry,
       "vncsVpNewVoiceEncodingChoiceIndex": vncsVpNewVoiceEncodingChoiceIndex,
       "vncsVpNewVoiceEncodingChoiceValue": vncsVpNewVoiceEncodingChoiceValue,
       "vncsVpNewModemFaxRatesTable": vncsVpNewModemFaxRatesTable,
       "vncsVpNewModemFaxRatesEntry": vncsVpNewModemFaxRatesEntry,
       "vncsVpNewModemFaxRatesEncodingIndex": vncsVpNewModemFaxRatesEncodingIndex,
       "vncsVpNewModemFaxRatesRateIndex": vncsVpNewModemFaxRatesRateIndex,
       "vncsVpNewModemFaxRatesValue": vncsVpNewModemFaxRatesValue,
       "vncsVpNewModemFaxEncodingChoiceTable": vncsVpNewModemFaxEncodingChoiceTable,
       "vncsVpNewModemFaxEncodingChoiceEntry": vncsVpNewModemFaxEncodingChoiceEntry,
       "vncsVpNewModemFaxEncodingChoiceIndex": vncsVpNewModemFaxEncodingChoiceIndex,
       "vncsVpNewModemFaxEncodingChoiceValue": vncsVpNewModemFaxEncodingChoiceValue,
       "vncsProvTable": vncsProvTable,
       "vncsProvEntry": vncsProvEntry,
       "vncsCommentText": vncsCommentText,
       "vncsStatsTable": vncsStatsTable,
       "vncsStatsEntry": vncsStatsEntry,
       "vncsTotalTranslations": vncsTotalTranslations,
       "vncsVRoutesTable": vncsVRoutesTable,
       "vncsVRoutesEntry": vncsVRoutesEntry,
       "vncsVRoutesValue": vncsVRoutesValue,
       "vncsCallServerMIB": vncsCallServerMIB,
       "vncsCallServerGroup": vncsCallServerGroup,
       "vncsCallServerGroupBE": vncsCallServerGroupBE,
       "vncsCallServerGroupBE01": vncsCallServerGroupBE01,
       "vncsCallServerGroupBE01A": vncsCallServerGroupBE01A,
       "vncsCallServerCapabilities": vncsCallServerCapabilities,
       "vncsCallServerCapabilitiesBE": vncsCallServerCapabilitiesBE,
       "vncsCallServerCapabilitiesBE01": vncsCallServerCapabilitiesBE01,
       "vncsCallServerCapabilitiesBE01A": vncsCallServerCapabilitiesBE01A}
)
