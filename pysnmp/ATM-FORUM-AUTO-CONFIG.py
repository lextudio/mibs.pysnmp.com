# SNMP MIB module (ATM-FORUM-AUTO-CONFIG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM-FORUM-AUTO-CONFIG
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:50 2024
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

(atmForum,
 atmForumUni) = mibBuilder.importSymbols(
    "ATM-FORUM-TC-MIB",
    "atmForum",
    "atmForumUni")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmfAutoConfigGroup_ObjectIdentity = ObjectIdentity
atmfAutoConfigGroup = _AtmfAutoConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 2, 12)
)
_AtmfAtmServiceTypeTable_Object = MibTable
atmfAtmServiceTypeTable = _AtmfAtmServiceTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1)
)
if mibBuilder.loadTexts:
    atmfAtmServiceTypeTable.setStatus("current")
_AtmfAtmServiceTypeEntry_Object = MibTableRow
atmfAtmServiceTypeEntry = _AtmfAtmServiceTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1)
)
atmfAtmServiceTypeEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAtmServiceTypeIndex"),
)
if mibBuilder.loadTexts:
    atmfAtmServiceTypeEntry.setStatus("current")


class _AtmfAtmServiceTypeIndex_Type(Integer32):
    """Custom type atmfAtmServiceTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfAtmServiceTypeIndex_Type.__name__ = "Integer32"
_AtmfAtmServiceTypeIndex_Object = MibTableColumn
atmfAtmServiceTypeIndex = _AtmfAtmServiceTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1, 1),
    _AtmfAtmServiceTypeIndex_Type()
)
atmfAtmServiceTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceTypeIndex.setStatus("current")
_AtmfAtmServiceProviderName_Type = DisplayString
_AtmfAtmServiceProviderName_Object = MibTableColumn
atmfAtmServiceProviderName = _AtmfAtmServiceProviderName_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1, 2),
    _AtmfAtmServiceProviderName_Type()
)
atmfAtmServiceProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceProviderName.setStatus("current")
_AtmfAtmServiceName_Type = DisplayString
_AtmfAtmServiceName_Object = MibTableColumn
atmfAtmServiceName = _AtmfAtmServiceName_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1, 3),
    _AtmfAtmServiceName_Type()
)
atmfAtmServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceName.setStatus("current")
_AtmfAtmServiceSubName_Type = DisplayString
_AtmfAtmServiceSubName_Object = MibTableColumn
atmfAtmServiceSubName = _AtmfAtmServiceSubName_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1, 4),
    _AtmfAtmServiceSubName_Type()
)
atmfAtmServiceSubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceSubName.setStatus("current")
_AtmfAtmServiceClient_Type = DisplayString
_AtmfAtmServiceClient_Object = MibTableColumn
atmfAtmServiceClient = _AtmfAtmServiceClient_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1, 5),
    _AtmfAtmServiceClient_Type()
)
atmfAtmServiceClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceClient.setStatus("current")


class _AtmfAtmServiceTMCategory_Type(Integer32):
    """Custom type atmfAtmServiceTMCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abr", 5),
          ("cbr", 2),
          ("gfr", 7),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )


_AtmfAtmServiceTMCategory_Type.__name__ = "Integer32"
_AtmfAtmServiceTMCategory_Object = MibTableColumn
atmfAtmServiceTMCategory = _AtmfAtmServiceTMCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1, 6),
    _AtmfAtmServiceTMCategory_Type()
)
atmfAtmServiceTMCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceTMCategory.setStatus("current")


class _AtmfAtmServiceTMConformanceDef_Type(Integer32):
    """Custom type atmfAtmServiceTMConformanceDef based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("abr", 8),
          ("cbr1", 2),
          ("gfr1", 9),
          ("gfr2", 10),
          ("none", 0),
          ("other", 1),
          ("ubr1", 6),
          ("ubr2", 7),
          ("vbr1", 3),
          ("vbr2", 4),
          ("vbr3", 5))
    )


_AtmfAtmServiceTMConformanceDef_Type.__name__ = "Integer32"
_AtmfAtmServiceTMConformanceDef_Object = MibTableColumn
atmfAtmServiceTMConformanceDef = _AtmfAtmServiceTMConformanceDef_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 1, 1, 7),
    _AtmfAtmServiceTMConformanceDef_Type()
)
atmfAtmServiceTMConformanceDef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceTMConformanceDef.setStatus("current")
_AtmfAtmServiceConnInfoTable_Object = MibTable
atmfAtmServiceConnInfoTable = _AtmfAtmServiceConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2)
)
if mibBuilder.loadTexts:
    atmfAtmServiceConnInfoTable.setStatus("current")
_AtmfAtmServiceConnInfoEntry_Object = MibTableRow
atmfAtmServiceConnInfoEntry = _AtmfAtmServiceConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1)
)
atmfAtmServiceConnInfoEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAtmServicePortIndex"),
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAtmServiceVpi"),
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAtmServiceVci"),
)
if mibBuilder.loadTexts:
    atmfAtmServiceConnInfoEntry.setStatus("current")


class _AtmfAtmServicePortIndex_Type(Integer32):
    """Custom type atmfAtmServicePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AtmfAtmServicePortIndex_Type.__name__ = "Integer32"
_AtmfAtmServicePortIndex_Object = MibTableColumn
atmfAtmServicePortIndex = _AtmfAtmServicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 1),
    _AtmfAtmServicePortIndex_Type()
)
atmfAtmServicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServicePortIndex.setStatus("current")


class _AtmfAtmServiceVpi_Type(Integer32):
    """Custom type atmfAtmServiceVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmfAtmServiceVpi_Type.__name__ = "Integer32"
_AtmfAtmServiceVpi_Object = MibTableColumn
atmfAtmServiceVpi = _AtmfAtmServiceVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 2),
    _AtmfAtmServiceVpi_Type()
)
atmfAtmServiceVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceVpi.setStatus("current")


class _AtmfAtmServiceVci_Type(Integer32):
    """Custom type atmfAtmServiceVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmfAtmServiceVci_Type.__name__ = "Integer32"
_AtmfAtmServiceVci_Object = MibTableColumn
atmfAtmServiceVci = _AtmfAtmServiceVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 3),
    _AtmfAtmServiceVci_Type()
)
atmfAtmServiceVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceVci.setStatus("current")


class _AtmfAtmServiceSignalId_Type(Integer32):
    """Custom type atmfAtmServiceSignalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vcCI", 0),
          ("vpCI", 1))
    )


_AtmfAtmServiceSignalId_Type.__name__ = "Integer32"
_AtmfAtmServiceSignalId_Object = MibTableColumn
atmfAtmServiceSignalId = _AtmfAtmServiceSignalId_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 4),
    _AtmfAtmServiceSignalId_Type()
)
atmfAtmServiceSignalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceSignalId.setStatus("current")
_AtmfAtmServiceConnServiceIndex_Type = Integer32
_AtmfAtmServiceConnServiceIndex_Object = MibTableColumn
atmfAtmServiceConnServiceIndex = _AtmfAtmServiceConnServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 5),
    _AtmfAtmServiceConnServiceIndex_Type()
)
atmfAtmServiceConnServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceConnServiceIndex.setStatus("current")
_AtmfAtmServiceConnName_Type = DisplayString
_AtmfAtmServiceConnName_Object = MibTableColumn
atmfAtmServiceConnName = _AtmfAtmServiceConnName_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 6),
    _AtmfAtmServiceConnName_Type()
)
atmfAtmServiceConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceConnName.setStatus("current")


class _AtmfAtmServiceConnAALType_Type(Integer32):
    """Custom type atmfAtmServiceConnAALType based on Integer32"""
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
        *(("aal1", 1),
          ("aal2", 6),
          ("aal34", 2),
          ("aal5", 3),
          ("none", 0),
          ("other", 4),
          ("unknown", 5))
    )


_AtmfAtmServiceConnAALType_Type.__name__ = "Integer32"
_AtmfAtmServiceConnAALType_Object = MibTableColumn
atmfAtmServiceConnAALType = _AtmfAtmServiceConnAALType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 7),
    _AtmfAtmServiceConnAALType_Type()
)
atmfAtmServiceConnAALType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceConnAALType.setStatus("current")
_AtmfAtmServiceConnAALIndex_Type = Integer32
_AtmfAtmServiceConnAALIndex_Object = MibTableColumn
atmfAtmServiceConnAALIndex = _AtmfAtmServiceConnAALIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 2, 1, 8),
    _AtmfAtmServiceConnAALIndex_Type()
)
atmfAtmServiceConnAALIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceConnAALIndex.setStatus("current")
_AtmfAAL1ProfileTable_Object = MibTable
atmfAAL1ProfileTable = _AtmfAAL1ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3)
)
if mibBuilder.loadTexts:
    atmfAAL1ProfileTable.setStatus("current")
_AtmfAAL1ProfileEntry_Object = MibTableRow
atmfAAL1ProfileEntry = _AtmfAAL1ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1)
)
atmfAAL1ProfileEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAAL1ProfileIndex"),
)
if mibBuilder.loadTexts:
    atmfAAL1ProfileEntry.setStatus("current")


class _AtmfAAL1ProfileIndex_Type(Integer32):
    """Custom type atmfAAL1ProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfAAL1ProfileIndex_Type.__name__ = "Integer32"
_AtmfAAL1ProfileIndex_Object = MibTableColumn
atmfAAL1ProfileIndex = _AtmfAAL1ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 1),
    _AtmfAAL1ProfileIndex_Type()
)
atmfAAL1ProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1ProfileIndex.setStatus("current")


class _AtmfAAL1Subtype_Type(Integer32):
    """Custom type atmfAAL1Subtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("circuitEmulationAsynchronous", 3),
          ("circuitEmulationSynchronous", 2),
          ("highQualityAuto", 4),
          ("null", 0),
          ("video", 5),
          ("voiceBand", 1))
    )


_AtmfAAL1Subtype_Type.__name__ = "Integer32"
_AtmfAAL1Subtype_Object = MibTableColumn
atmfAAL1Subtype = _AtmfAAL1Subtype_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 2),
    _AtmfAAL1Subtype_Type()
)
atmfAAL1Subtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1Subtype.setStatus("current")
_AtmfAAL1CBRRate_Type = Integer32
_AtmfAAL1CBRRate_Object = MibTableColumn
atmfAAL1CBRRate = _AtmfAAL1CBRRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 3),
    _AtmfAAL1CBRRate_Type()
)
atmfAAL1CBRRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1CBRRate.setStatus("current")


class _AtmfAAL1ClkRecoveryType_Type(Integer32):
    """Custom type atmfAAL1ClkRecoveryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("srts", 1),
          ("synchronous", 0))
    )


_AtmfAAL1ClkRecoveryType_Type.__name__ = "Integer32"
_AtmfAAL1ClkRecoveryType_Object = MibTableColumn
atmfAAL1ClkRecoveryType = _AtmfAAL1ClkRecoveryType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 4),
    _AtmfAAL1ClkRecoveryType_Type()
)
atmfAAL1ClkRecoveryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1ClkRecoveryType.setStatus("current")


class _AtmfAAL1FEC_Type(Integer32):
    """Custom type atmfAAL1FEC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delaySensitiveSignalFEC", 2),
          ("lossSensitiveSignalFEC", 1),
          ("noFEC", 0))
    )


_AtmfAAL1FEC_Type.__name__ = "Integer32"
_AtmfAAL1FEC_Object = MibTableColumn
atmfAAL1FEC = _AtmfAAL1FEC_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 5),
    _AtmfAAL1FEC_Type()
)
atmfAAL1FEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1FEC.setStatus("current")


class _AtmfAAL1SDT_Type(Integer32):
    """Custom type atmfAAL1SDT based on Integer32"""
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


_AtmfAAL1SDT_Type.__name__ = "Integer32"
_AtmfAAL1SDT_Object = MibTableColumn
atmfAAL1SDT = _AtmfAAL1SDT_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 6),
    _AtmfAAL1SDT_Type()
)
atmfAAL1SDT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1SDT.setStatus("current")
_AtmfAAL1PartiallyFilledCells_Type = Integer32
_AtmfAAL1PartiallyFilledCells_Object = MibTableColumn
atmfAAL1PartiallyFilledCells = _AtmfAAL1PartiallyFilledCells_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 7),
    _AtmfAAL1PartiallyFilledCells_Type()
)
atmfAAL1PartiallyFilledCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1PartiallyFilledCells.setStatus("current")
_AtmfAAL1CellLossIntegrPeriod_Type = Integer32
_AtmfAAL1CellLossIntegrPeriod_Object = MibTableColumn
atmfAAL1CellLossIntegrPeriod = _AtmfAAL1CellLossIntegrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 3, 1, 8),
    _AtmfAAL1CellLossIntegrPeriod_Type()
)
atmfAAL1CellLossIntegrPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL1CellLossIntegrPeriod.setStatus("current")
_AtmfAAL34ProfileTable_Object = MibTable
atmfAAL34ProfileTable = _AtmfAAL34ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4)
)
if mibBuilder.loadTexts:
    atmfAAL34ProfileTable.setStatus("current")
_AtmfAAL34ProfileEntry_Object = MibTableRow
atmfAAL34ProfileEntry = _AtmfAAL34ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1)
)
atmfAAL34ProfileEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAAL34ProfileIndex"),
)
if mibBuilder.loadTexts:
    atmfAAL34ProfileEntry.setStatus("current")


class _AtmfAAL34ProfileIndex_Type(Integer32):
    """Custom type atmfAAL34ProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfAAL34ProfileIndex_Type.__name__ = "Integer32"
_AtmfAAL34ProfileIndex_Object = MibTableColumn
atmfAAL34ProfileIndex = _AtmfAAL34ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1, 1),
    _AtmfAAL34ProfileIndex_Type()
)
atmfAAL34ProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL34ProfileIndex.setStatus("current")


class _AtmfAAL34MaxCpcsSduSizeForward_Type(Integer32):
    """Custom type atmfAAL34MaxCpcsSduSizeForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmfAAL34MaxCpcsSduSizeForward_Type.__name__ = "Integer32"
_AtmfAAL34MaxCpcsSduSizeForward_Object = MibTableColumn
atmfAAL34MaxCpcsSduSizeForward = _AtmfAAL34MaxCpcsSduSizeForward_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1, 2),
    _AtmfAAL34MaxCpcsSduSizeForward_Type()
)
atmfAAL34MaxCpcsSduSizeForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL34MaxCpcsSduSizeForward.setStatus("current")


class _AtmfAAL34MaxCpcsSduSizeBackward_Type(Integer32):
    """Custom type atmfAAL34MaxCpcsSduSizeBackward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmfAAL34MaxCpcsSduSizeBackward_Type.__name__ = "Integer32"
_AtmfAAL34MaxCpcsSduSizeBackward_Object = MibTableColumn
atmfAAL34MaxCpcsSduSizeBackward = _AtmfAAL34MaxCpcsSduSizeBackward_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1, 3),
    _AtmfAAL34MaxCpcsSduSizeBackward_Type()
)
atmfAAL34MaxCpcsSduSizeBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL34MaxCpcsSduSizeBackward.setStatus("current")


class _AtmfAAL34MIDRangeLow_Type(Integer32):
    """Custom type atmfAAL34MIDRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 66536),
    )


_AtmfAAL34MIDRangeLow_Type.__name__ = "Integer32"
_AtmfAAL34MIDRangeLow_Object = MibTableColumn
atmfAAL34MIDRangeLow = _AtmfAAL34MIDRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1, 4),
    _AtmfAAL34MIDRangeLow_Type()
)
atmfAAL34MIDRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL34MIDRangeLow.setStatus("current")


class _AtmfAAL34MIDRangeHigh_Type(Integer32):
    """Custom type atmfAAL34MIDRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 66536),
    )


_AtmfAAL34MIDRangeHigh_Type.__name__ = "Integer32"
_AtmfAAL34MIDRangeHigh_Object = MibTableColumn
atmfAAL34MIDRangeHigh = _AtmfAAL34MIDRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1, 5),
    _AtmfAAL34MIDRangeHigh_Type()
)
atmfAAL34MIDRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL34MIDRangeHigh.setStatus("current")


class _AtmfAAL34AALMode_Type(Integer32):
    """Custom type atmfAAL34AALMode based on Integer32"""
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
        *(("messageAssured", 0),
          ("messageUnassured", 1),
          ("streamingAssured", 2),
          ("streamingUnassured", 3))
    )


_AtmfAAL34AALMode_Type.__name__ = "Integer32"
_AtmfAAL34AALMode_Object = MibTableColumn
atmfAAL34AALMode = _AtmfAAL34AALMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1, 6),
    _AtmfAAL34AALMode_Type()
)
atmfAAL34AALMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL34AALMode.setStatus("current")


class _AtmfAAL34SscsType_Type(Integer32):
    """Custom type atmfAAL34SscsType based on Integer32"""
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
        *(("dataAssured", 1),
          ("dataNonAssured", 2),
          ("frameRelay", 3),
          ("null", 0))
    )


_AtmfAAL34SscsType_Type.__name__ = "Integer32"
_AtmfAAL34SscsType_Object = MibTableColumn
atmfAAL34SscsType = _AtmfAAL34SscsType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 4, 1, 7),
    _AtmfAAL34SscsType_Type()
)
atmfAAL34SscsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL34SscsType.setStatus("current")
_AtmfAAL5ProfileTable_Object = MibTable
atmfAAL5ProfileTable = _AtmfAAL5ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 5)
)
if mibBuilder.loadTexts:
    atmfAAL5ProfileTable.setStatus("current")
_AtmfAAL5ProfileEntry_Object = MibTableRow
atmfAAL5ProfileEntry = _AtmfAAL5ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 5, 1)
)
atmfAAL5ProfileEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAAL5ProfileIndex"),
)
if mibBuilder.loadTexts:
    atmfAAL5ProfileEntry.setStatus("current")


class _AtmfAAL5ProfileIndex_Type(Integer32):
    """Custom type atmfAAL5ProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmfAAL5ProfileIndex_Type.__name__ = "Integer32"
_AtmfAAL5ProfileIndex_Object = MibTableColumn
atmfAAL5ProfileIndex = _AtmfAAL5ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 5, 1, 1),
    _AtmfAAL5ProfileIndex_Type()
)
atmfAAL5ProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL5ProfileIndex.setStatus("current")


class _AtmfAAL5MaxCpcsSduSizeForward_Type(Integer32):
    """Custom type atmfAAL5MaxCpcsSduSizeForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmfAAL5MaxCpcsSduSizeForward_Type.__name__ = "Integer32"
_AtmfAAL5MaxCpcsSduSizeForward_Object = MibTableColumn
atmfAAL5MaxCpcsSduSizeForward = _AtmfAAL5MaxCpcsSduSizeForward_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 5, 1, 2),
    _AtmfAAL5MaxCpcsSduSizeForward_Type()
)
atmfAAL5MaxCpcsSduSizeForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL5MaxCpcsSduSizeForward.setStatus("current")


class _AtmfAAL5MaxCpcsSduSizeBackward_Type(Integer32):
    """Custom type atmfAAL5MaxCpcsSduSizeBackward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmfAAL5MaxCpcsSduSizeBackward_Type.__name__ = "Integer32"
_AtmfAAL5MaxCpcsSduSizeBackward_Object = MibTableColumn
atmfAAL5MaxCpcsSduSizeBackward = _AtmfAAL5MaxCpcsSduSizeBackward_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 5, 1, 3),
    _AtmfAAL5MaxCpcsSduSizeBackward_Type()
)
atmfAAL5MaxCpcsSduSizeBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL5MaxCpcsSduSizeBackward.setStatus("current")


class _AtmfAAL5AALMode_Type(Integer32):
    """Custom type atmfAAL5AALMode based on Integer32"""
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
        *(("messageAssured", 0),
          ("messageUnassured", 1),
          ("streamingAssured", 2),
          ("streamingUnassured", 3))
    )


_AtmfAAL5AALMode_Type.__name__ = "Integer32"
_AtmfAAL5AALMode_Object = MibTableColumn
atmfAAL5AALMode = _AtmfAAL5AALMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 5, 1, 4),
    _AtmfAAL5AALMode_Type()
)
atmfAAL5AALMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL5AALMode.setStatus("current")


class _AtmfAAL5SscsType_Type(Integer32):
    """Custom type atmfAAL5SscsType based on Integer32"""
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
        *(("dataAssured", 1),
          ("dataNonAssured", 2),
          ("frameRelay", 3),
          ("null", 0))
    )


_AtmfAAL5SscsType_Type.__name__ = "Integer32"
_AtmfAAL5SscsType_Object = MibTableColumn
atmfAAL5SscsType = _AtmfAAL5SscsType_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 5, 1, 5),
    _AtmfAAL5SscsType_Type()
)
atmfAAL5SscsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL5SscsType.setStatus("current")
_AtmfAAL2CommonProfileTable_Object = MibTable
atmfAAL2CommonProfileTable = _AtmfAAL2CommonProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6)
)
if mibBuilder.loadTexts:
    atmfAAL2CommonProfileTable.setStatus("current")
_AtmfAAL2CommonProfileEntry_Object = MibTableRow
atmfAAL2CommonProfileEntry = _AtmfAAL2CommonProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1)
)
atmfAAL2CommonProfileEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAAL2ProfileIndex"),
)
if mibBuilder.loadTexts:
    atmfAAL2CommonProfileEntry.setStatus("current")
_AtmfAAL2ProfileIndex_Type = Integer32
_AtmfAAL2ProfileIndex_Object = MibTableColumn
atmfAAL2ProfileIndex = _AtmfAAL2ProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 1),
    _AtmfAAL2ProfileIndex_Type()
)
atmfAAL2ProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2ProfileIndex.setStatus("current")
_AtmfAAL2ApplicationIdentifier_Type = Integer32
_AtmfAAL2ApplicationIdentifier_Object = MibTableColumn
atmfAAL2ApplicationIdentifier = _AtmfAAL2ApplicationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 2),
    _AtmfAAL2ApplicationIdentifier_Type()
)
atmfAAL2ApplicationIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2ApplicationIdentifier.setStatus("current")


class _AtmfAAL2ConfigResponsibility_Type(Integer32):
    """Custom type atmfAAL2ConfigResponsibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ilmi", 1),
          ("lesEoc", 2),
          ("other", 3))
    )


_AtmfAAL2ConfigResponsibility_Type.__name__ = "Integer32"
_AtmfAAL2ConfigResponsibility_Object = MibTableColumn
atmfAAL2ConfigResponsibility = _AtmfAAL2ConfigResponsibility_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 3),
    _AtmfAAL2ConfigResponsibility_Type()
)
atmfAAL2ConfigResponsibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2ConfigResponsibility.setStatus("current")


class _AtmfAAL2CpsMaxMultiplexedChannels_Type(Integer32):
    """Custom type atmfAAL2CpsMaxMultiplexedChannels based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AtmfAAL2CpsMaxMultiplexedChannels_Type.__name__ = "Integer32"
_AtmfAAL2CpsMaxMultiplexedChannels_Object = MibTableColumn
atmfAAL2CpsMaxMultiplexedChannels = _AtmfAAL2CpsMaxMultiplexedChannels_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 4),
    _AtmfAAL2CpsMaxMultiplexedChannels_Type()
)
atmfAAL2CpsMaxMultiplexedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2CpsMaxMultiplexedChannels.setStatus("current")


class _AtmfAAL2CpsMaxSduLength_Type(Integer32):
    """Custom type atmfAAL2CpsMaxSduLength based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(64, 64),
    )


_AtmfAAL2CpsMaxSduLength_Type.__name__ = "Integer32"
_AtmfAAL2CpsMaxSduLength_Object = MibTableColumn
atmfAAL2CpsMaxSduLength = _AtmfAAL2CpsMaxSduLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 5),
    _AtmfAAL2CpsMaxSduLength_Type()
)
atmfAAL2CpsMaxSduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2CpsMaxSduLength.setStatus("current")


class _AtmfAAL2SscsMaxSssarSduLength_Type(Integer32):
    """Custom type atmfAAL2SscsMaxSssarSduLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65568),
    )


_AtmfAAL2SscsMaxSssarSduLength_Type.__name__ = "Integer32"
_AtmfAAL2SscsMaxSssarSduLength_Object = MibTableColumn
atmfAAL2SscsMaxSssarSduLength = _AtmfAAL2SscsMaxSssarSduLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 6),
    _AtmfAAL2SscsMaxSssarSduLength_Type()
)
atmfAAL2SscsMaxSssarSduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsMaxSssarSduLength.setStatus("current")


class _AtmfAAL2SscsSstedStatus_Type(Integer32):
    """Custom type atmfAAL2SscsSstedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSelected", 2),
          ("selected", 1))
    )


_AtmfAAL2SscsSstedStatus_Type.__name__ = "Integer32"
_AtmfAAL2SscsSstedStatus_Object = MibTableColumn
atmfAAL2SscsSstedStatus = _AtmfAAL2SscsSstedStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 7),
    _AtmfAAL2SscsSstedStatus_Type()
)
atmfAAL2SscsSstedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsSstedStatus.setStatus("current")


class _AtmfAAL2SscsSsadtStatus_Type(Integer32):
    """Custom type atmfAAL2SscsSsadtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSelected", 2),
          ("selected", 1))
    )


_AtmfAAL2SscsSsadtStatus_Type.__name__ = "Integer32"
_AtmfAAL2SscsSsadtStatus_Object = MibTableColumn
atmfAAL2SscsSsadtStatus = _AtmfAAL2SscsSsadtStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 8),
    _AtmfAAL2SscsSsadtStatus_Type()
)
atmfAAL2SscsSsadtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsSsadtStatus.setStatus("current")


class _AtmfAAL2SscsServiceCategory_Type(Integer32):
    """Custom type atmfAAL2SscsServiceCategory based on Integer32"""
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
        *(("audio", 1),
          ("audioAndMultiRate", 3),
          ("multirate", 2))
    )


_AtmfAAL2SscsServiceCategory_Type.__name__ = "Integer32"
_AtmfAAL2SscsServiceCategory_Object = MibTableColumn
atmfAAL2SscsServiceCategory = _AtmfAAL2SscsServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 9),
    _AtmfAAL2SscsServiceCategory_Type()
)
atmfAAL2SscsServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsServiceCategory.setStatus("current")


class _AtmfAAL2SscsAudioServiceTransport_Type(Integer32):
    """Custom type atmfAAL2SscsAudioServiceTransport based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsAudioServiceTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsAudioServiceTransport_Object = MibTableColumn
atmfAAL2SscsAudioServiceTransport = _AtmfAAL2SscsAudioServiceTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 10),
    _AtmfAAL2SscsAudioServiceTransport_Type()
)
atmfAAL2SscsAudioServiceTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsAudioServiceTransport.setStatus("current")


class _AtmfAAL2SscsProfileSource_Type(Integer32):
    """Custom type atmfAAL2SscsProfileSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("itut", 1),
          ("other", 2))
    )


_AtmfAAL2SscsProfileSource_Type.__name__ = "Integer32"
_AtmfAAL2SscsProfileSource_Object = MibTableColumn
atmfAAL2SscsProfileSource = _AtmfAAL2SscsProfileSource_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 11),
    _AtmfAAL2SscsProfileSource_Type()
)
atmfAAL2SscsProfileSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsProfileSource.setStatus("current")
_AtmfAAL2SscsIeeeOui_Type = Integer32
_AtmfAAL2SscsIeeeOui_Object = MibTableColumn
atmfAAL2SscsIeeeOui = _AtmfAAL2SscsIeeeOui_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 12),
    _AtmfAAL2SscsIeeeOui_Type()
)
atmfAAL2SscsIeeeOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsIeeeOui.setStatus("current")


class _AtmfAAL2SscsPredefinedProfileIdentifier_Type(Integer32):
    """Custom type atmfAAL2SscsPredefinedProfileIdentifier based on Integer32"""
    defaultValue = 1


_AtmfAAL2SscsPredefinedProfileIdentifier_Object = MibTableColumn
atmfAAL2SscsPredefinedProfileIdentifier = _AtmfAAL2SscsPredefinedProfileIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 13),
    _AtmfAAL2SscsPredefinedProfileIdentifier_Type()
)
atmfAAL2SscsPredefinedProfileIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsPredefinedProfileIdentifier.setStatus("current")


class _AtmfAAL2SscsPcmEncoding_Type(Integer32):
    """Custom type atmfAAL2SscsPcmEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 1),
          ("ulaw", 2))
    )


_AtmfAAL2SscsPcmEncoding_Type.__name__ = "Integer32"
_AtmfAAL2SscsPcmEncoding_Object = MibTableColumn
atmfAAL2SscsPcmEncoding = _AtmfAAL2SscsPcmEncoding_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 14),
    _AtmfAAL2SscsPcmEncoding_Type()
)
atmfAAL2SscsPcmEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsPcmEncoding.setStatus("current")


class _AtmfAAL2SscsFaxDemodulationTransport_Type(Integer32):
    """Custom type atmfAAL2SscsFaxDemodulationTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsFaxDemodulationTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsFaxDemodulationTransport_Object = MibTableColumn
atmfAAL2SscsFaxDemodulationTransport = _AtmfAAL2SscsFaxDemodulationTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 15),
    _AtmfAAL2SscsFaxDemodulationTransport_Type()
)
atmfAAL2SscsFaxDemodulationTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsFaxDemodulationTransport.setStatus("current")


class _AtmfAAL2SscsCasSignalingTransport_Type(Integer32):
    """Custom type atmfAAL2SscsCasSignalingTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsCasSignalingTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsCasSignalingTransport_Object = MibTableColumn
atmfAAL2SscsCasSignalingTransport = _AtmfAAL2SscsCasSignalingTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 16),
    _AtmfAAL2SscsCasSignalingTransport_Type()
)
atmfAAL2SscsCasSignalingTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsCasSignalingTransport.setStatus("current")


class _AtmfAAL2SscsDtmfDigitPacketTransport_Type(Integer32):
    """Custom type atmfAAL2SscsDtmfDigitPacketTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsDtmfDigitPacketTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsDtmfDigitPacketTransport_Object = MibTableColumn
atmfAAL2SscsDtmfDigitPacketTransport = _AtmfAAL2SscsDtmfDigitPacketTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 17),
    _AtmfAAL2SscsDtmfDigitPacketTransport_Type()
)
atmfAAL2SscsDtmfDigitPacketTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsDtmfDigitPacketTransport.setStatus("current")


class _AtmfAAL2SscsMfR1DigitPacketTransport_Type(Integer32):
    """Custom type atmfAAL2SscsMfR1DigitPacketTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsMfR1DigitPacketTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsMfR1DigitPacketTransport_Object = MibTableColumn
atmfAAL2SscsMfR1DigitPacketTransport = _AtmfAAL2SscsMfR1DigitPacketTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 18),
    _AtmfAAL2SscsMfR1DigitPacketTransport_Type()
)
atmfAAL2SscsMfR1DigitPacketTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsMfR1DigitPacketTransport.setStatus("current")


class _AtmfAAL2SscsMfR2DigitPacketTransport_Type(Integer32):
    """Custom type atmfAAL2SscsMfR2DigitPacketTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsMfR2DigitPacketTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsMfR2DigitPacketTransport_Object = MibTableColumn
atmfAAL2SscsMfR2DigitPacketTransport = _AtmfAAL2SscsMfR2DigitPacketTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 19),
    _AtmfAAL2SscsMfR2DigitPacketTransport_Type()
)
atmfAAL2SscsMfR2DigitPacketTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsMfR2DigitPacketTransport.setStatus("current")


class _AtmfAAL2SscsCircuitModeDataTransport_Type(Integer32):
    """Custom type atmfAAL2SscsCircuitModeDataTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsCircuitModeDataTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsCircuitModeDataTransport_Object = MibTableColumn
atmfAAL2SscsCircuitModeDataTransport = _AtmfAAL2SscsCircuitModeDataTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 20),
    _AtmfAAL2SscsCircuitModeDataTransport_Type()
)
atmfAAL2SscsCircuitModeDataTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsCircuitModeDataTransport.setStatus("current")


class _AtmfAAL2SscsCircuitModeDataNumChannels_Type(Integer32):
    """Custom type atmfAAL2SscsCircuitModeDataNumChannels based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AtmfAAL2SscsCircuitModeDataNumChannels_Type.__name__ = "Integer32"
_AtmfAAL2SscsCircuitModeDataNumChannels_Object = MibTableColumn
atmfAAL2SscsCircuitModeDataNumChannels = _AtmfAAL2SscsCircuitModeDataNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 21),
    _AtmfAAL2SscsCircuitModeDataNumChannels_Type()
)
atmfAAL2SscsCircuitModeDataNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsCircuitModeDataNumChannels.setStatus("current")


class _AtmfAAL2SscsFrameModeDataTransport_Type(Integer32):
    """Custom type atmfAAL2SscsFrameModeDataTransport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtmfAAL2SscsFrameModeDataTransport_Type.__name__ = "Integer32"
_AtmfAAL2SscsFrameModeDataTransport_Object = MibTableColumn
atmfAAL2SscsFrameModeDataTransport = _AtmfAAL2SscsFrameModeDataTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 22),
    _AtmfAAL2SscsFrameModeDataTransport_Type()
)
atmfAAL2SscsFrameModeDataTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsFrameModeDataTransport.setStatus("current")


class _AtmfAAL2SscsFrameModeDataMaxLength_Type(Integer32):
    """Custom type atmfAAL2SscsFrameModeDataMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmfAAL2SscsFrameModeDataMaxLength_Type.__name__ = "Integer32"
_AtmfAAL2SscsFrameModeDataMaxLength_Object = MibTableColumn
atmfAAL2SscsFrameModeDataMaxLength = _AtmfAAL2SscsFrameModeDataMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 23),
    _AtmfAAL2SscsFrameModeDataMaxLength_Type()
)
atmfAAL2SscsFrameModeDataMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscsFrameModeDataMaxLength.setStatus("current")


class _AtmfAAL2SscopSduLength_Type(Integer32):
    """Custom type atmfAAL2SscopSduLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65524),
    )


_AtmfAAL2SscopSduLength_Type.__name__ = "Integer32"
_AtmfAAL2SscopSduLength_Object = MibTableColumn
atmfAAL2SscopSduLength = _AtmfAAL2SscopSduLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 24),
    _AtmfAAL2SscopSduLength_Type()
)
atmfAAL2SscopSduLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscopSduLength.setStatus("current")


class _AtmfAAL2SscopUuFieldLength_Type(Integer32):
    """Custom type atmfAAL2SscopUuFieldLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65524),
    )


_AtmfAAL2SscopUuFieldLength_Type.__name__ = "Integer32"
_AtmfAAL2SscopUuFieldLength_Object = MibTableColumn
atmfAAL2SscopUuFieldLength = _AtmfAAL2SscopUuFieldLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 6, 1, 25),
    _AtmfAAL2SscopUuFieldLength_Type()
)
atmfAAL2SscopUuFieldLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SscopUuFieldLength.setStatus("current")
_AtmfAAL2TrunkingProfileTable_Object = MibTable
atmfAAL2TrunkingProfileTable = _AtmfAAL2TrunkingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 7)
)
if mibBuilder.loadTexts:
    atmfAAL2TrunkingProfileTable.setStatus("current")
_AtmfAAL2TrunkingProfileEntry_Object = MibTableRow
atmfAAL2TrunkingProfileEntry = _AtmfAAL2TrunkingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 7, 1)
)
atmfAAL2TrunkingProfileEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAAL2ProfileIndex"),
)
if mibBuilder.loadTexts:
    atmfAAL2TrunkingProfileEntry.setStatus("current")
_AtmfAAL2Vcci_Type = Integer32
_AtmfAAL2Vcci_Object = MibTableColumn
atmfAAL2Vcci = _AtmfAAL2Vcci_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 7, 1, 1),
    _AtmfAAL2Vcci_Type()
)
atmfAAL2Vcci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2Vcci.setStatus("current")
_AtmfAAL2SignalingVcci_Type = Integer32
_AtmfAAL2SignalingVcci_Object = MibTableColumn
atmfAAL2SignalingVcci = _AtmfAAL2SignalingVcci_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 7, 1, 2),
    _AtmfAAL2SignalingVcci_Type()
)
atmfAAL2SignalingVcci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2SignalingVcci.setStatus("current")
_AtmfAAL2LESProfileTable_Object = MibTable
atmfAAL2LESProfileTable = _AtmfAAL2LESProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 8)
)
if mibBuilder.loadTexts:
    atmfAAL2LESProfileTable.setStatus("current")
_AtmfAAL2LESProfileEntry_Object = MibTableRow
atmfAAL2LESProfileEntry = _AtmfAAL2LESProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 8, 1)
)
atmfAAL2LESProfileEntry.setIndexNames(
    (0, "ATM-FORUM-AUTO-CONFIG", "atmfAAL2ProfileIndex"),
)
if mibBuilder.loadTexts:
    atmfAAL2LESProfileEntry.setStatus("current")


class _AtmfAAL2CpsCIDLowerLimit_Type(Integer32):
    """Custom type atmfAAL2CpsCIDLowerLimit based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 223),
    )


_AtmfAAL2CpsCIDLowerLimit_Type.__name__ = "Integer32"
_AtmfAAL2CpsCIDLowerLimit_Object = MibTableColumn
atmfAAL2CpsCIDLowerLimit = _AtmfAAL2CpsCIDLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 8, 1, 1),
    _AtmfAAL2CpsCIDLowerLimit_Type()
)
atmfAAL2CpsCIDLowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2CpsCIDLowerLimit.setStatus("current")


class _AtmfAAL2CpsCIDUpperLimit_Type(Integer32):
    """Custom type atmfAAL2CpsCIDUpperLimit based on Integer32"""
    defaultValue = 223

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 223),
    )


_AtmfAAL2CpsCIDUpperLimit_Type.__name__ = "Integer32"
_AtmfAAL2CpsCIDUpperLimit_Object = MibTableColumn
atmfAAL2CpsCIDUpperLimit = _AtmfAAL2CpsCIDUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 8, 1, 2),
    _AtmfAAL2CpsCIDUpperLimit_Type()
)
atmfAAL2CpsCIDUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2CpsCIDUpperLimit.setStatus("current")


class _AtmfAAL2CpsOptimisation_Type(Integer32):
    """Custom type atmfAAL2CpsOptimisation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleCpsPacketsPerCpsPduWithOverlap", 2),
          ("singleCpsPacketPerCpsPduNoOverlap", 1))
    )


_AtmfAAL2CpsOptimisation_Type.__name__ = "Integer32"
_AtmfAAL2CpsOptimisation_Object = MibTableColumn
atmfAAL2CpsOptimisation = _AtmfAAL2CpsOptimisation_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 8, 1, 3),
    _AtmfAAL2CpsOptimisation_Type()
)
atmfAAL2CpsOptimisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL2CpsOptimisation.setStatus("current")
_AtmfAtmServiceConnInfoExtensionTable_Object = MibTable
atmfAtmServiceConnInfoExtensionTable = _AtmfAtmServiceConnInfoExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 9)
)
if mibBuilder.loadTexts:
    atmfAtmServiceConnInfoExtensionTable.setStatus("current")
_AtmfAtmServiceConnInfoExtensionEntry_Object = MibTableRow
atmfAtmServiceConnInfoExtensionEntry = _AtmfAtmServiceConnInfoExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 9, 1)
)
if mibBuilder.loadTexts:
    atmfAtmServiceConnInfoExtensionEntry.setStatus("current")
_AtmfAtmServicePhyMacIdentifier_Type = Integer32
_AtmfAtmServicePhyMacIdentifier_Object = MibTableColumn
atmfAtmServicePhyMacIdentifier = _AtmfAtmServicePhyMacIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 9, 1, 1),
    _AtmfAtmServicePhyMacIdentifier_Type()
)
atmfAtmServicePhyMacIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServicePhyMacIdentifier.setStatus("current")
_AtmfAtmServiceTypeExtensionTable_Object = MibTable
atmfAtmServiceTypeExtensionTable = _AtmfAtmServiceTypeExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 10)
)
if mibBuilder.loadTexts:
    atmfAtmServiceTypeExtensionTable.setStatus("current")
_AtmfAtmServiceTypeExtensionEntry_Object = MibTableRow
atmfAtmServiceTypeExtensionEntry = _AtmfAtmServiceTypeExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 10, 1)
)
if mibBuilder.loadTexts:
    atmfAtmServiceTypeExtensionEntry.setStatus("current")
_AtmfAtmServiceLayer2ProtocolId_Type = OctetString
_AtmfAtmServiceLayer2ProtocolId_Object = MibTableColumn
atmfAtmServiceLayer2ProtocolId = _AtmfAtmServiceLayer2ProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 10, 1, 1),
    _AtmfAtmServiceLayer2ProtocolId_Type()
)
atmfAtmServiceLayer2ProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceLayer2ProtocolId.setStatus("current")
_AtmfAtmServiceLayer3ProtocolId_Type = OctetString
_AtmfAtmServiceLayer3ProtocolId_Object = MibTableColumn
atmfAtmServiceLayer3ProtocolId = _AtmfAtmServiceLayer3ProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 10, 1, 2),
    _AtmfAtmServiceLayer3ProtocolId_Type()
)
atmfAtmServiceLayer3ProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceLayer3ProtocolId.setStatus("current")
_AtmfAAL5ProfileExtensionTable_Object = MibTable
atmfAAL5ProfileExtensionTable = _AtmfAAL5ProfileExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 11)
)
if mibBuilder.loadTexts:
    atmfAAL5ProfileExtensionTable.setStatus("current")
_AtmfAAL5ProfileExtensionEntry_Object = MibTableRow
atmfAAL5ProfileExtensionEntry = _AtmfAAL5ProfileExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 11, 1)
)
if mibBuilder.loadTexts:
    atmfAAL5ProfileExtensionEntry.setStatus("current")
_AtmfAAL5Vcci_Type = Integer32
_AtmfAAL5Vcci_Object = MibTableColumn
atmfAAL5Vcci = _AtmfAAL5Vcci_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 11, 1, 1),
    _AtmfAAL5Vcci_Type()
)
atmfAAL5Vcci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAAL5Vcci.setStatus("current")


class _AtmfAtmServiceConfFailReason_Type(Integer32):
    """Custom type atmfAtmServiceConfFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("incompleteConfigurationInformation", 6),
          ("inconsistentConfigurationInformation", 7),
          ("invalidVPIVCIValue", 4),
          ("tooManyPVCs", 5),
          ("unsupportedAAL", 3),
          ("unsupportedClientProtocol", 1),
          ("unsupportedServiceCategory", 2))
    )


_AtmfAtmServiceConfFailReason_Type.__name__ = "Integer32"
_AtmfAtmServiceConfFailReason_Object = MibScalar
atmfAtmServiceConfFailReason = _AtmfAtmServiceConfFailReason_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 12),
    _AtmfAtmServiceConfFailReason_Type()
)
atmfAtmServiceConfFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceConfFailReason.setStatus("current")
_AtmfAtmServiceConfFailOID_Type = RowPointer
_AtmfAtmServiceConfFailOID_Object = MibScalar
atmfAtmServiceConfFailOID = _AtmfAtmServiceConfFailOID_Object(
    (1, 3, 6, 1, 4, 1, 353, 2, 12, 13),
    _AtmfAtmServiceConfFailOID_Type()
)
atmfAtmServiceConfFailOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmfAtmServiceConfFailOID.setStatus("current")
atmfAtmServiceConnInfoEntry.registerAugmentions(
    ("ATM-FORUM-AUTO-CONFIG",
     "atmfAtmServiceConnInfoExtensionEntry")
)
atmfAtmServiceConnInfoExtensionEntry.setIndexNames(*atmfAtmServiceConnInfoEntry.getIndexNames())
atmfAtmServiceTypeEntry.registerAugmentions(
    ("ATM-FORUM-AUTO-CONFIG",
     "atmfAtmServiceTypeExtensionEntry")
)
atmfAtmServiceTypeExtensionEntry.setIndexNames(*atmfAtmServiceTypeEntry.getIndexNames())
atmfAAL5ProfileEntry.registerAugmentions(
    ("ATM-FORUM-AUTO-CONFIG",
     "atmfAAL5ProfileExtensionEntry")
)
atmfAAL5ProfileExtensionEntry.setIndexNames(*atmfAAL5ProfileEntry.getIndexNames())

# Managed Objects groups


# Notification objects

atmfAtmServiceConfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 0, 3)
)
atmfAtmServiceConfFail.setObjects(
      *(("ATM-FORUM-AUTO-CONFIG", "atmfAtmServiceConfFailReason"),
        ("ATM-FORUM-AUTO-CONFIG", "atmfAtmServiceConfFailOID"))
)
if mibBuilder.loadTexts:
    atmfAtmServiceConfFail.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM-FORUM-AUTO-CONFIG",
    **{"atmfAtmServiceConfFail": atmfAtmServiceConfFail,
       "atmfAutoConfigGroup": atmfAutoConfigGroup,
       "atmfAtmServiceTypeTable": atmfAtmServiceTypeTable,
       "atmfAtmServiceTypeEntry": atmfAtmServiceTypeEntry,
       "atmfAtmServiceTypeIndex": atmfAtmServiceTypeIndex,
       "atmfAtmServiceProviderName": atmfAtmServiceProviderName,
       "atmfAtmServiceName": atmfAtmServiceName,
       "atmfAtmServiceSubName": atmfAtmServiceSubName,
       "atmfAtmServiceClient": atmfAtmServiceClient,
       "atmfAtmServiceTMCategory": atmfAtmServiceTMCategory,
       "atmfAtmServiceTMConformanceDef": atmfAtmServiceTMConformanceDef,
       "atmfAtmServiceConnInfoTable": atmfAtmServiceConnInfoTable,
       "atmfAtmServiceConnInfoEntry": atmfAtmServiceConnInfoEntry,
       "atmfAtmServicePortIndex": atmfAtmServicePortIndex,
       "atmfAtmServiceVpi": atmfAtmServiceVpi,
       "atmfAtmServiceVci": atmfAtmServiceVci,
       "atmfAtmServiceSignalId": atmfAtmServiceSignalId,
       "atmfAtmServiceConnServiceIndex": atmfAtmServiceConnServiceIndex,
       "atmfAtmServiceConnName": atmfAtmServiceConnName,
       "atmfAtmServiceConnAALType": atmfAtmServiceConnAALType,
       "atmfAtmServiceConnAALIndex": atmfAtmServiceConnAALIndex,
       "atmfAAL1ProfileTable": atmfAAL1ProfileTable,
       "atmfAAL1ProfileEntry": atmfAAL1ProfileEntry,
       "atmfAAL1ProfileIndex": atmfAAL1ProfileIndex,
       "atmfAAL1Subtype": atmfAAL1Subtype,
       "atmfAAL1CBRRate": atmfAAL1CBRRate,
       "atmfAAL1ClkRecoveryType": atmfAAL1ClkRecoveryType,
       "atmfAAL1FEC": atmfAAL1FEC,
       "atmfAAL1SDT": atmfAAL1SDT,
       "atmfAAL1PartiallyFilledCells": atmfAAL1PartiallyFilledCells,
       "atmfAAL1CellLossIntegrPeriod": atmfAAL1CellLossIntegrPeriod,
       "atmfAAL34ProfileTable": atmfAAL34ProfileTable,
       "atmfAAL34ProfileEntry": atmfAAL34ProfileEntry,
       "atmfAAL34ProfileIndex": atmfAAL34ProfileIndex,
       "atmfAAL34MaxCpcsSduSizeForward": atmfAAL34MaxCpcsSduSizeForward,
       "atmfAAL34MaxCpcsSduSizeBackward": atmfAAL34MaxCpcsSduSizeBackward,
       "atmfAAL34MIDRangeLow": atmfAAL34MIDRangeLow,
       "atmfAAL34MIDRangeHigh": atmfAAL34MIDRangeHigh,
       "atmfAAL34AALMode": atmfAAL34AALMode,
       "atmfAAL34SscsType": atmfAAL34SscsType,
       "atmfAAL5ProfileTable": atmfAAL5ProfileTable,
       "atmfAAL5ProfileEntry": atmfAAL5ProfileEntry,
       "atmfAAL5ProfileIndex": atmfAAL5ProfileIndex,
       "atmfAAL5MaxCpcsSduSizeForward": atmfAAL5MaxCpcsSduSizeForward,
       "atmfAAL5MaxCpcsSduSizeBackward": atmfAAL5MaxCpcsSduSizeBackward,
       "atmfAAL5AALMode": atmfAAL5AALMode,
       "atmfAAL5SscsType": atmfAAL5SscsType,
       "atmfAAL2CommonProfileTable": atmfAAL2CommonProfileTable,
       "atmfAAL2CommonProfileEntry": atmfAAL2CommonProfileEntry,
       "atmfAAL2ProfileIndex": atmfAAL2ProfileIndex,
       "atmfAAL2ApplicationIdentifier": atmfAAL2ApplicationIdentifier,
       "atmfAAL2ConfigResponsibility": atmfAAL2ConfigResponsibility,
       "atmfAAL2CpsMaxMultiplexedChannels": atmfAAL2CpsMaxMultiplexedChannels,
       "atmfAAL2CpsMaxSduLength": atmfAAL2CpsMaxSduLength,
       "atmfAAL2SscsMaxSssarSduLength": atmfAAL2SscsMaxSssarSduLength,
       "atmfAAL2SscsSstedStatus": atmfAAL2SscsSstedStatus,
       "atmfAAL2SscsSsadtStatus": atmfAAL2SscsSsadtStatus,
       "atmfAAL2SscsServiceCategory": atmfAAL2SscsServiceCategory,
       "atmfAAL2SscsAudioServiceTransport": atmfAAL2SscsAudioServiceTransport,
       "atmfAAL2SscsProfileSource": atmfAAL2SscsProfileSource,
       "atmfAAL2SscsIeeeOui": atmfAAL2SscsIeeeOui,
       "atmfAAL2SscsPredefinedProfileIdentifier": atmfAAL2SscsPredefinedProfileIdentifier,
       "atmfAAL2SscsPcmEncoding": atmfAAL2SscsPcmEncoding,
       "atmfAAL2SscsFaxDemodulationTransport": atmfAAL2SscsFaxDemodulationTransport,
       "atmfAAL2SscsCasSignalingTransport": atmfAAL2SscsCasSignalingTransport,
       "atmfAAL2SscsDtmfDigitPacketTransport": atmfAAL2SscsDtmfDigitPacketTransport,
       "atmfAAL2SscsMfR1DigitPacketTransport": atmfAAL2SscsMfR1DigitPacketTransport,
       "atmfAAL2SscsMfR2DigitPacketTransport": atmfAAL2SscsMfR2DigitPacketTransport,
       "atmfAAL2SscsCircuitModeDataTransport": atmfAAL2SscsCircuitModeDataTransport,
       "atmfAAL2SscsCircuitModeDataNumChannels": atmfAAL2SscsCircuitModeDataNumChannels,
       "atmfAAL2SscsFrameModeDataTransport": atmfAAL2SscsFrameModeDataTransport,
       "atmfAAL2SscsFrameModeDataMaxLength": atmfAAL2SscsFrameModeDataMaxLength,
       "atmfAAL2SscopSduLength": atmfAAL2SscopSduLength,
       "atmfAAL2SscopUuFieldLength": atmfAAL2SscopUuFieldLength,
       "atmfAAL2TrunkingProfileTable": atmfAAL2TrunkingProfileTable,
       "atmfAAL2TrunkingProfileEntry": atmfAAL2TrunkingProfileEntry,
       "atmfAAL2Vcci": atmfAAL2Vcci,
       "atmfAAL2SignalingVcci": atmfAAL2SignalingVcci,
       "atmfAAL2LESProfileTable": atmfAAL2LESProfileTable,
       "atmfAAL2LESProfileEntry": atmfAAL2LESProfileEntry,
       "atmfAAL2CpsCIDLowerLimit": atmfAAL2CpsCIDLowerLimit,
       "atmfAAL2CpsCIDUpperLimit": atmfAAL2CpsCIDUpperLimit,
       "atmfAAL2CpsOptimisation": atmfAAL2CpsOptimisation,
       "atmfAtmServiceConnInfoExtensionTable": atmfAtmServiceConnInfoExtensionTable,
       "atmfAtmServiceConnInfoExtensionEntry": atmfAtmServiceConnInfoExtensionEntry,
       "atmfAtmServicePhyMacIdentifier": atmfAtmServicePhyMacIdentifier,
       "atmfAtmServiceTypeExtensionTable": atmfAtmServiceTypeExtensionTable,
       "atmfAtmServiceTypeExtensionEntry": atmfAtmServiceTypeExtensionEntry,
       "atmfAtmServiceLayer2ProtocolId": atmfAtmServiceLayer2ProtocolId,
       "atmfAtmServiceLayer3ProtocolId": atmfAtmServiceLayer3ProtocolId,
       "atmfAAL5ProfileExtensionTable": atmfAAL5ProfileExtensionTable,
       "atmfAAL5ProfileExtensionEntry": atmfAAL5ProfileExtensionEntry,
       "atmfAAL5Vcci": atmfAAL5Vcci,
       "atmfAtmServiceConfFailReason": atmfAtmServiceConfFailReason,
       "atmfAtmServiceConfFailOID": atmfAtmServiceConfFailOID}
)
