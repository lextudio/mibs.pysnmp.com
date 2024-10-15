# SNMP MIB module (CTRON-VLAN-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-VLAN-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:53 2024
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

(ctVlanExt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctVlanExt")

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

_CtVlanBridgeConfig_ObjectIdentity = ObjectIdentity
ctVlanBridgeConfig = _CtVlanBridgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1)
)
_CtVlanVersionNumber_Type = Integer32
_CtVlanVersionNumber_Object = MibScalar
ctVlanVersionNumber = _CtVlanVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 1),
    _CtVlanVersionNumber_Type()
)
ctVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanVersionNumber.setStatus("mandatory")


class _CtVlanSupportedOperationalMode_Type(Integer32):
    """Custom type ctVlanSupportedOperationalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurable", 2),
          ("static", 1))
    )


_CtVlanSupportedOperationalMode_Type.__name__ = "Integer32"
_CtVlanSupportedOperationalMode_Object = MibScalar
ctVlanSupportedOperationalMode = _CtVlanSupportedOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 2),
    _CtVlanSupportedOperationalMode_Type()
)
ctVlanSupportedOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanSupportedOperationalMode.setStatus("deprecated")


class _CtVlanCurrentOperationalMode_Type(Integer32):
    """Custom type ctVlanCurrentOperationalMode based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_CtVlanCurrentOperationalMode_Type.__name__ = "Integer32"
_CtVlanCurrentOperationalMode_Object = MibScalar
ctVlanCurrentOperationalMode = _CtVlanCurrentOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 3),
    _CtVlanCurrentOperationalMode_Type()
)
ctVlanCurrentOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanCurrentOperationalMode.setStatus("deprecated")


class _CtVlanResetDefaults_Type(Integer32):
    """Custom type ctVlanResetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("current", 1),
          ("reset", 2))
    )


_CtVlanResetDefaults_Type.__name__ = "Integer32"
_CtVlanResetDefaults_Object = MibScalar
ctVlanResetDefaults = _CtVlanResetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 4),
    _CtVlanResetDefaults_Type()
)
ctVlanResetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanResetDefaults.setStatus("mandatory")


class _CtVlanDefaultVIDStickyEgress_Type(Integer32):
    """Custom type ctVlanDefaultVIDStickyEgress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CtVlanDefaultVIDStickyEgress_Type.__name__ = "Integer32"
_CtVlanDefaultVIDStickyEgress_Object = MibScalar
ctVlanDefaultVIDStickyEgress = _CtVlanDefaultVIDStickyEgress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 5),
    _CtVlanDefaultVIDStickyEgress_Type()
)
ctVlanDefaultVIDStickyEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanDefaultVIDStickyEgress.setStatus("mandatory")
_CtVlanSupportedPortTable_Object = MibTable
ctVlanSupportedPortTable = _CtVlanSupportedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6)
)
if mibBuilder.loadTexts:
    ctVlanSupportedPortTable.setStatus("mandatory")
_CtVlanSupportedPortEntry_Object = MibTableRow
ctVlanSupportedPortEntry = _CtVlanSupportedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1)
)
ctVlanSupportedPortEntry.setIndexNames(
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanSupportedSlotNum"),
)
if mibBuilder.loadTexts:
    ctVlanSupportedPortEntry.setStatus("mandatory")
_CtVlanSupportedSlotNum_Type = Integer32
_CtVlanSupportedSlotNum_Object = MibTableColumn
ctVlanSupportedSlotNum = _CtVlanSupportedSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1, 1),
    _CtVlanSupportedSlotNum_Type()
)
ctVlanSupportedSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanSupportedSlotNum.setStatus("mandatory")
_CtVlanSupportedPortNum_Type = OctetString
_CtVlanSupportedPortNum_Object = MibTableColumn
ctVlanSupportedPortNum = _CtVlanSupportedPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 6, 1, 2),
    _CtVlanSupportedPortNum_Type()
)
ctVlanSupportedPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanSupportedPortNum.setStatus("mandatory")


class _CtVlanLearningMode_Type(Integer32):
    """Custom type ctVlanLearningMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ivl", 1),
          ("svl", 2),
          ("svlivl", 3))
    )


_CtVlanLearningMode_Type.__name__ = "Integer32"
_CtVlanLearningMode_Object = MibScalar
ctVlanLearningMode = _CtVlanLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 1, 7),
    _CtVlanLearningMode_Type()
)
ctVlanLearningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanLearningMode.setStatus("mandatory")
_CtVlanTriggerPortConfig_ObjectIdentity = ObjectIdentity
ctVlanTriggerPortConfig = _CtVlanTriggerPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2)
)
_CtVlanTriggerPortSetTable_Object = MibTable
ctVlanTriggerPortSetTable = _CtVlanTriggerPortSetTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1)
)
if mibBuilder.loadTexts:
    ctVlanTriggerPortSetTable.setStatus("mandatory")
_CtVlanTriggerPortEntry_Object = MibTableRow
ctVlanTriggerPortEntry = _CtVlanTriggerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1)
)
ctVlanTriggerPortEntry.setIndexNames(
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanTriggerSlotNum"),
)
if mibBuilder.loadTexts:
    ctVlanTriggerPortEntry.setStatus("mandatory")
_CtVlanTriggerSlotNum_Type = Integer32
_CtVlanTriggerSlotNum_Object = MibTableColumn
ctVlanTriggerSlotNum = _CtVlanTriggerSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1, 1),
    _CtVlanTriggerSlotNum_Type()
)
ctVlanTriggerSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanTriggerSlotNum.setStatus("mandatory")
_CtVlanTriggerStatus_Type = OctetString
_CtVlanTriggerStatus_Object = MibTableColumn
ctVlanTriggerStatus = _CtVlanTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 2, 1, 1, 2),
    _CtVlanTriggerStatus_Type()
)
ctVlanTriggerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanTriggerStatus.setStatus("mandatory")
_CtVlanPortConfig_ObjectIdentity = ObjectIdentity
ctVlanPortConfig = _CtVlanPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3)
)
_CtVlanPortConfigTable_Object = MibTable
ctVlanPortConfigTable = _CtVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    ctVlanPortConfigTable.setStatus("mandatory")
_CtVlanPortConfigEntry_Object = MibTableRow
ctVlanPortConfigEntry = _CtVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1)
)
ctVlanPortConfigEntry.setIndexNames(
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanPortSlotNum"),
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanPortNum"),
)
if mibBuilder.loadTexts:
    ctVlanPortConfigEntry.setStatus("mandatory")
_CtVlanPortSlotNum_Type = Integer32
_CtVlanPortSlotNum_Object = MibTableColumn
ctVlanPortSlotNum = _CtVlanPortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 1),
    _CtVlanPortSlotNum_Type()
)
ctVlanPortSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanPortSlotNum.setStatus("mandatory")
_CtVlanPortNum_Type = Integer32
_CtVlanPortNum_Object = MibTableColumn
ctVlanPortNum = _CtVlanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 2),
    _CtVlanPortNum_Type()
)
ctVlanPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanPortNum.setStatus("mandatory")


class _CtVlanPortVID_Type(Integer32):
    """Custom type ctVlanPortVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtVlanPortVID_Type.__name__ = "Integer32"
_CtVlanPortVID_Object = MibTableColumn
ctVlanPortVID = _CtVlanPortVID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 3),
    _CtVlanPortVID_Type()
)
ctVlanPortVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanPortVID.setStatus("mandatory")


class _CtVlanPortDiscardFrame_Type(Integer32):
    """Custom type ctVlanPortDiscardFrame based on Integer32"""
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
        *(("discardTagged", 3),
          ("discardUntagged", 2),
          ("noDiscard", 1))
    )


_CtVlanPortDiscardFrame_Type.__name__ = "Integer32"
_CtVlanPortDiscardFrame_Object = MibTableColumn
ctVlanPortDiscardFrame = _CtVlanPortDiscardFrame_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 4),
    _CtVlanPortDiscardFrame_Type()
)
ctVlanPortDiscardFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanPortDiscardFrame.setStatus("mandatory")


class _CtVlanPortOperationalMode_Type(Integer32):
    """Custom type ctVlanPortOperationalMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1QTrunk", 1),
          ("dot1dTrunk", 3),
          ("hybrid", 2))
    )


_CtVlanPortOperationalMode_Type.__name__ = "Integer32"
_CtVlanPortOperationalMode_Object = MibTableColumn
ctVlanPortOperationalMode = _CtVlanPortOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 5),
    _CtVlanPortOperationalMode_Type()
)
ctVlanPortOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanPortOperationalMode.setStatus("mandatory")


class _CtVlanPortIngressFiltering_Type(Integer32):
    """Custom type ctVlanPortIngressFiltering based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CtVlanPortIngressFiltering_Type.__name__ = "Integer32"
_CtVlanPortIngressFiltering_Object = MibTableColumn
ctVlanPortIngressFiltering = _CtVlanPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 3, 1, 1, 6),
    _CtVlanPortIngressFiltering_Type()
)
ctVlanPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanPortIngressFiltering.setStatus("mandatory")
_CtVlanConfig_ObjectIdentity = ObjectIdentity
ctVlanConfig = _CtVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4)
)
_CtVlanNumActiveEntries_Type = Integer32
_CtVlanNumActiveEntries_Object = MibScalar
ctVlanNumActiveEntries = _CtVlanNumActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 1),
    _CtVlanNumActiveEntries_Type()
)
ctVlanNumActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanNumActiveEntries.setStatus("mandatory")
_CtVlanNumConfiguredEntries_Type = Integer32
_CtVlanNumConfiguredEntries_Object = MibScalar
ctVlanNumConfiguredEntries = _CtVlanNumConfiguredEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 2),
    _CtVlanNumConfiguredEntries_Type()
)
ctVlanNumConfiguredEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanNumConfiguredEntries.setStatus("mandatory")
_CtVlanMaxNumEntries_Type = Integer32
_CtVlanMaxNumEntries_Object = MibScalar
ctVlanMaxNumEntries = _CtVlanMaxNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 3),
    _CtVlanMaxNumEntries_Type()
)
ctVlanMaxNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanMaxNumEntries.setStatus("mandatory")
_CtVlanConfigTable_Object = MibTable
ctVlanConfigTable = _CtVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4)
)
if mibBuilder.loadTexts:
    ctVlanConfigTable.setStatus("mandatory")
_CtVlanConfigEntry_Object = MibTableRow
ctVlanConfigEntry = _CtVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1)
)
ctVlanConfigEntry.setIndexNames(
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanVID"),
)
if mibBuilder.loadTexts:
    ctVlanConfigEntry.setStatus("mandatory")


class _CtVlanVID_Type(Integer32):
    """Custom type ctVlanVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtVlanVID_Type.__name__ = "Integer32"
_CtVlanVID_Object = MibTableColumn
ctVlanVID = _CtVlanVID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 1),
    _CtVlanVID_Type()
)
ctVlanVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanVID.setStatus("mandatory")


class _CtVlanName_Type(DisplayString):
    """Custom type ctVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CtVlanName_Type.__name__ = "DisplayString"
_CtVlanName_Object = MibTableColumn
ctVlanName = _CtVlanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 2),
    _CtVlanName_Type()
)
ctVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanName.setStatus("mandatory")


class _CtVlanStatus_Type(Integer32):
    """Custom type ctVlanStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CtVlanStatus_Type.__name__ = "Integer32"
_CtVlanStatus_Object = MibTableColumn
ctVlanStatus = _CtVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 3),
    _CtVlanStatus_Type()
)
ctVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanStatus.setStatus("mandatory")


class _CtVlanEstablish_Type(Integer32):
    """Custom type ctVlanEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_CtVlanEstablish_Type.__name__ = "Integer32"
_CtVlanEstablish_Object = MibTableColumn
ctVlanEstablish = _CtVlanEstablish_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 4),
    _CtVlanEstablish_Type()
)
ctVlanEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanEstablish.setStatus("mandatory")


class _CtVlanIdToFidMapping_Type(Integer32):
    """Custom type ctVlanIdToFidMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtVlanIdToFidMapping_Type.__name__ = "Integer32"
_CtVlanIdToFidMapping_Object = MibTableColumn
ctVlanIdToFidMapping = _CtVlanIdToFidMapping_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 5),
    _CtVlanIdToFidMapping_Type()
)
ctVlanIdToFidMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanIdToFidMapping.setStatus("mandatory")


class _CtVlanType_Type(Integer32):
    """Custom type ctVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 3),
          ("other", 1),
          ("static", 2))
    )


_CtVlanType_Type.__name__ = "Integer32"
_CtVlanType_Object = MibTableColumn
ctVlanType = _CtVlanType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 4, 1, 6),
    _CtVlanType_Type()
)
ctVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanType.setStatus("mandatory")
_CtVlanEgressPortsTable_Object = MibTable
ctVlanEgressPortsTable = _CtVlanEgressPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5)
)
if mibBuilder.loadTexts:
    ctVlanEgressPortsTable.setStatus("mandatory")
_CtVlanEgressPortEntry_Object = MibTableRow
ctVlanEgressPortEntry = _CtVlanEgressPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1)
)
ctVlanEgressPortEntry.setIndexNames(
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanEgressPortSlotNum"),
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanEgressVID"),
)
if mibBuilder.loadTexts:
    ctVlanEgressPortEntry.setStatus("mandatory")
_CtVlanEgressPortSlotNum_Type = Integer32
_CtVlanEgressPortSlotNum_Object = MibTableColumn
ctVlanEgressPortSlotNum = _CtVlanEgressPortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 1),
    _CtVlanEgressPortSlotNum_Type()
)
ctVlanEgressPortSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanEgressPortSlotNum.setStatus("mandatory")


class _CtVlanEgressVID_Type(Integer32):
    """Custom type ctVlanEgressVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtVlanEgressVID_Type.__name__ = "Integer32"
_CtVlanEgressVID_Object = MibTableColumn
ctVlanEgressVID = _CtVlanEgressVID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 2),
    _CtVlanEgressVID_Type()
)
ctVlanEgressVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanEgressVID.setStatus("mandatory")
_CtVlanEgressList_Type = OctetString
_CtVlanEgressList_Object = MibTableColumn
ctVlanEgressList = _CtVlanEgressList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 3),
    _CtVlanEgressList_Type()
)
ctVlanEgressList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanEgressList.setStatus("mandatory")
_CtVlanEgressUntaggedList_Type = OctetString
_CtVlanEgressUntaggedList_Object = MibTableColumn
ctVlanEgressUntaggedList = _CtVlanEgressUntaggedList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 4, 5, 1, 4),
    _CtVlanEgressUntaggedList_Type()
)
ctVlanEgressUntaggedList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanEgressUntaggedList.setStatus("mandatory")
_CtVlanProtocolAssign_ObjectIdentity = ObjectIdentity
ctVlanProtocolAssign = _CtVlanProtocolAssign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5)
)


class _CtVlanProtocolStatus_Type(Integer32):
    """Custom type ctVlanProtocolStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CtVlanProtocolStatus_Type.__name__ = "Integer32"
_CtVlanProtocolStatus_Object = MibScalar
ctVlanProtocolStatus = _CtVlanProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 1),
    _CtVlanProtocolStatus_Type()
)
ctVlanProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanProtocolStatus.setStatus("mandatory")
_CtMaxNumVlanProtoEntries_Type = Integer32
_CtMaxNumVlanProtoEntries_Object = MibScalar
ctMaxNumVlanProtoEntries = _CtMaxNumVlanProtoEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 2),
    _CtMaxNumVlanProtoEntries_Type()
)
ctMaxNumVlanProtoEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctMaxNumVlanProtoEntries.setStatus("mandatory")
_CtVlanProtoAssignTable_Object = MibTable
ctVlanProtoAssignTable = _CtVlanProtoAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3)
)
if mibBuilder.loadTexts:
    ctVlanProtoAssignTable.setStatus("mandatory")
_CtVlanProtoAssignEntry_Object = MibTableRow
ctVlanProtoAssignEntry = _CtVlanProtoAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1)
)
ctVlanProtoAssignEntry.setIndexNames(
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanVID"),
    (0, "CTRON-VLAN-EXTENSIONS-MIB", "ctVlanProtoEtherType"),
)
if mibBuilder.loadTexts:
    ctVlanProtoAssignEntry.setStatus("mandatory")
_CtVlanProtoEtherType_Type = Integer32
_CtVlanProtoEtherType_Object = MibTableColumn
ctVlanProtoEtherType = _CtVlanProtoEtherType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 1),
    _CtVlanProtoEtherType_Type()
)
ctVlanProtoEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctVlanProtoEtherType.setStatus("mandatory")


class _CtVlanProtoEstablish_Type(Integer32):
    """Custom type ctVlanProtoEstablish based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_CtVlanProtoEstablish_Type.__name__ = "Integer32"
_CtVlanProtoEstablish_Object = MibTableColumn
ctVlanProtoEstablish = _CtVlanProtoEstablish_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 2),
    _CtVlanProtoEstablish_Type()
)
ctVlanProtoEstablish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanProtoEstablish.setStatus("mandatory")
_CtVlanProtoPortList_Type = OctetString
_CtVlanProtoPortList_Object = MibTableColumn
ctVlanProtoPortList = _CtVlanProtoPortList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 5, 3, 1, 3),
    _CtVlanProtoPortList_Type()
)
ctVlanProtoPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctVlanProtoPortList.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-VLAN-EXTENSIONS-MIB",
    **{"ctVlanBridgeConfig": ctVlanBridgeConfig,
       "ctVlanVersionNumber": ctVlanVersionNumber,
       "ctVlanSupportedOperationalMode": ctVlanSupportedOperationalMode,
       "ctVlanCurrentOperationalMode": ctVlanCurrentOperationalMode,
       "ctVlanResetDefaults": ctVlanResetDefaults,
       "ctVlanDefaultVIDStickyEgress": ctVlanDefaultVIDStickyEgress,
       "ctVlanSupportedPortTable": ctVlanSupportedPortTable,
       "ctVlanSupportedPortEntry": ctVlanSupportedPortEntry,
       "ctVlanSupportedSlotNum": ctVlanSupportedSlotNum,
       "ctVlanSupportedPortNum": ctVlanSupportedPortNum,
       "ctVlanLearningMode": ctVlanLearningMode,
       "ctVlanTriggerPortConfig": ctVlanTriggerPortConfig,
       "ctVlanTriggerPortSetTable": ctVlanTriggerPortSetTable,
       "ctVlanTriggerPortEntry": ctVlanTriggerPortEntry,
       "ctVlanTriggerSlotNum": ctVlanTriggerSlotNum,
       "ctVlanTriggerStatus": ctVlanTriggerStatus,
       "ctVlanPortConfig": ctVlanPortConfig,
       "ctVlanPortConfigTable": ctVlanPortConfigTable,
       "ctVlanPortConfigEntry": ctVlanPortConfigEntry,
       "ctVlanPortSlotNum": ctVlanPortSlotNum,
       "ctVlanPortNum": ctVlanPortNum,
       "ctVlanPortVID": ctVlanPortVID,
       "ctVlanPortDiscardFrame": ctVlanPortDiscardFrame,
       "ctVlanPortOperationalMode": ctVlanPortOperationalMode,
       "ctVlanPortIngressFiltering": ctVlanPortIngressFiltering,
       "ctVlanConfig": ctVlanConfig,
       "ctVlanNumActiveEntries": ctVlanNumActiveEntries,
       "ctVlanNumConfiguredEntries": ctVlanNumConfiguredEntries,
       "ctVlanMaxNumEntries": ctVlanMaxNumEntries,
       "ctVlanConfigTable": ctVlanConfigTable,
       "ctVlanConfigEntry": ctVlanConfigEntry,
       "ctVlanVID": ctVlanVID,
       "ctVlanName": ctVlanName,
       "ctVlanStatus": ctVlanStatus,
       "ctVlanEstablish": ctVlanEstablish,
       "ctVlanIdToFidMapping": ctVlanIdToFidMapping,
       "ctVlanType": ctVlanType,
       "ctVlanEgressPortsTable": ctVlanEgressPortsTable,
       "ctVlanEgressPortEntry": ctVlanEgressPortEntry,
       "ctVlanEgressPortSlotNum": ctVlanEgressPortSlotNum,
       "ctVlanEgressVID": ctVlanEgressVID,
       "ctVlanEgressList": ctVlanEgressList,
       "ctVlanEgressUntaggedList": ctVlanEgressUntaggedList,
       "ctVlanProtocolAssign": ctVlanProtocolAssign,
       "ctVlanProtocolStatus": ctVlanProtocolStatus,
       "ctMaxNumVlanProtoEntries": ctMaxNumVlanProtoEntries,
       "ctVlanProtoAssignTable": ctVlanProtoAssignTable,
       "ctVlanProtoAssignEntry": ctVlanProtoAssignEntry,
       "ctVlanProtoEtherType": ctVlanProtoEtherType,
       "ctVlanProtoEstablish": ctVlanProtoEstablish,
       "ctVlanProtoPortList": ctVlanProtoPortList}
)
