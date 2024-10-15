# SNMP MIB module (ALU-POWER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALU-POWER-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:27 2024
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

(softentIND1InLinePower,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1InLinePower")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

powerEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999)
)
powerEthernetMIB.setRevisions(
        ("2002-12-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PethNotifications_ObjectIdentity = ObjectIdentity
pethNotifications = _PethNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0)
)
_PethObjects_ObjectIdentity = ObjectIdentity
pethObjects = _PethObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1)
)
_PethPsePortTable_Object = MibTable
pethPsePortTable = _PethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1)
)
if mibBuilder.loadTexts:
    pethPsePortTable.setStatus("current")
_PethPsePortEntry_Object = MibTableRow
pethPsePortEntry = _PethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1)
)
pethPsePortEntry.setIndexNames(
    (0, "ALU-POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "ALU-POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    pethPsePortEntry.setStatus("current")


class _PethPsePortGroupIndex_Type(Integer32):
    """Custom type pethPsePortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethPsePortGroupIndex_Type.__name__ = "Integer32"
_PethPsePortGroupIndex_Object = MibTableColumn
pethPsePortGroupIndex = _PethPsePortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 1),
    _PethPsePortGroupIndex_Type()
)
pethPsePortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethPsePortGroupIndex.setStatus("current")


class _PethPsePortIndex_Type(Integer32):
    """Custom type pethPsePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethPsePortIndex_Type.__name__ = "Integer32"
_PethPsePortIndex_Object = MibTableColumn
pethPsePortIndex = _PethPsePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 2),
    _PethPsePortIndex_Type()
)
pethPsePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethPsePortIndex.setStatus("current")


class _PethPsePortAdminEnable_Type(Integer32):
    """Custom type pethPsePortAdminEnable based on Integer32"""
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


_PethPsePortAdminEnable_Type.__name__ = "Integer32"
_PethPsePortAdminEnable_Object = MibTableColumn
pethPsePortAdminEnable = _PethPsePortAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 3),
    _PethPsePortAdminEnable_Type()
)
pethPsePortAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortAdminEnable.setStatus("current")
_PethPsePortPowerPairsControlAbility_Type = TruthValue
_PethPsePortPowerPairsControlAbility_Object = MibTableColumn
pethPsePortPowerPairsControlAbility = _PethPsePortPowerPairsControlAbility_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 4),
    _PethPsePortPowerPairsControlAbility_Type()
)
pethPsePortPowerPairsControlAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortPowerPairsControlAbility.setStatus("current")


class _PethPsePortPowerPairs_Type(Integer32):
    """Custom type pethPsePortPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("spare", 2))
    )


_PethPsePortPowerPairs_Type.__name__ = "Integer32"
_PethPsePortPowerPairs_Object = MibTableColumn
pethPsePortPowerPairs = _PethPsePortPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 5),
    _PethPsePortPowerPairs_Type()
)
pethPsePortPowerPairs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortPowerPairs.setStatus("current")


class _PethPsePortPowerDetectionControl_Type(Integer32):
    """Custom type pethPsePortPowerDetectionControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("test", 2))
    )


_PethPsePortPowerDetectionControl_Type.__name__ = "Integer32"
_PethPsePortPowerDetectionControl_Object = MibTableColumn
pethPsePortPowerDetectionControl = _PethPsePortPowerDetectionControl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 6),
    _PethPsePortPowerDetectionControl_Type()
)
pethPsePortPowerDetectionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortPowerDetectionControl.setStatus("current")


class _PethPsePortDetectionStatus_Type(Integer32):
    """Custom type pethPsePortDetectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("deliveringPower", 4),
          ("denyLowPriority", 8),
          ("disabled", 1),
          ("fault", 5),
          ("searching", 2),
          ("test", 7))
    )


_PethPsePortDetectionStatus_Type.__name__ = "Integer32"
_PethPsePortDetectionStatus_Object = MibTableColumn
pethPsePortDetectionStatus = _PethPsePortDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 7),
    _PethPsePortDetectionStatus_Type()
)
pethPsePortDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortDetectionStatus.setStatus("current")


class _PethPsePortPowerPriority_Type(Integer32):
    """Custom type pethPsePortPowerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_PethPsePortPowerPriority_Type.__name__ = "Integer32"
_PethPsePortPowerPriority_Object = MibTableColumn
pethPsePortPowerPriority = _PethPsePortPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 8),
    _PethPsePortPowerPriority_Type()
)
pethPsePortPowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortPowerPriority.setStatus("current")


class _PethPsePortPowerMaintenanceStatus_Type(Integer32):
    """Custom type pethPsePortPowerMaintenanceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mPSAbsent", 3),
          ("ok", 1),
          ("underCurrent", 2))
    )


_PethPsePortPowerMaintenanceStatus_Type.__name__ = "Integer32"
_PethPsePortPowerMaintenanceStatus_Object = MibTableColumn
pethPsePortPowerMaintenanceStatus = _PethPsePortPowerMaintenanceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 10),
    _PethPsePortPowerMaintenanceStatus_Type()
)
pethPsePortPowerMaintenanceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortPowerMaintenanceStatus.setStatus("current")
_PethPsePortMPSAbsentCounter_Type = Counter32
_PethPsePortMPSAbsentCounter_Object = MibTableColumn
pethPsePortMPSAbsentCounter = _PethPsePortMPSAbsentCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 11),
    _PethPsePortMPSAbsentCounter_Type()
)
pethPsePortMPSAbsentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortMPSAbsentCounter.setStatus("current")
_PethPsePortOverCurrentCounter_Type = Counter32
_PethPsePortOverCurrentCounter_Object = MibTableColumn
pethPsePortOverCurrentCounter = _PethPsePortOverCurrentCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 12),
    _PethPsePortOverCurrentCounter_Type()
)
pethPsePortOverCurrentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortOverCurrentCounter.setStatus("current")


class _PethPsePortType_Type(Integer32):
    """Custom type pethPsePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("telephone", 2),
          ("webcam", 3),
          ("wireless", 4))
    )


_PethPsePortType_Type.__name__ = "Integer32"
_PethPsePortType_Object = MibTableColumn
pethPsePortType = _PethPsePortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 13),
    _PethPsePortType_Type()
)
pethPsePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPsePortType.setStatus("current")


class _PethPsePortPowerClassifications_Type(Integer32):
    """Custom type pethPsePortPowerClassifications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )


_PethPsePortPowerClassifications_Type.__name__ = "Integer32"
_PethPsePortPowerClassifications_Object = MibTableColumn
pethPsePortPowerClassifications = _PethPsePortPowerClassifications_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 1, 1, 14),
    _PethPsePortPowerClassifications_Type()
)
pethPsePortPowerClassifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethPsePortPowerClassifications.setStatus("current")
_PethPdPortTable_Object = MibTable
pethPdPortTable = _PethPdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2)
)
if mibBuilder.loadTexts:
    pethPdPortTable.setStatus("current")
_PethPdPortEntry_Object = MibTableRow
pethPdPortEntry = _PethPdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2, 1)
)
pethPdPortEntry.setIndexNames(
    (0, "ALU-POWER-ETHERNET-MIB", "pethPdPortIndex"),
)
if mibBuilder.loadTexts:
    pethPdPortEntry.setStatus("current")
_PethPdPortIndex_Type = InterfaceIndex
_PethPdPortIndex_Object = MibTableColumn
pethPdPortIndex = _PethPdPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2, 1, 1),
    _PethPdPortIndex_Type()
)
pethPdPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethPdPortIndex.setStatus("current")


class _PethPdPortAdminEnable_Type(Integer32):
    """Custom type pethPdPortAdminEnable based on Integer32"""
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


_PethPdPortAdminEnable_Type.__name__ = "Integer32"
_PethPdPortAdminEnable_Object = MibTableColumn
pethPdPortAdminEnable = _PethPdPortAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 2, 1, 2),
    _PethPdPortAdminEnable_Type()
)
pethPdPortAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethPdPortAdminEnable.setStatus("current")
_PethMainPseObjects_ObjectIdentity = ObjectIdentity
pethMainPseObjects = _PethMainPseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3)
)
_PethMainPseTable_Object = MibTable
pethMainPseTable = _PethMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pethMainPseTable.setStatus("current")
_PethMainPseEntry_Object = MibTableRow
pethMainPseEntry = _PethMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1)
)
pethMainPseEntry.setIndexNames(
    (0, "ALU-POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    pethMainPseEntry.setStatus("current")


class _PethMainPseGroupIndex_Type(Integer32):
    """Custom type pethMainPseGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethMainPseGroupIndex_Type.__name__ = "Integer32"
_PethMainPseGroupIndex_Object = MibTableColumn
pethMainPseGroupIndex = _PethMainPseGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 1),
    _PethMainPseGroupIndex_Type()
)
pethMainPseGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethMainPseGroupIndex.setStatus("current")


class _PethMainPsePower_Type(Gauge32):
    """Custom type pethMainPsePower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PethMainPsePower_Type.__name__ = "Gauge32"
_PethMainPsePower_Object = MibTableColumn
pethMainPsePower = _PethMainPsePower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 2),
    _PethMainPsePower_Type()
)
pethMainPsePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethMainPsePower.setStatus("current")
if mibBuilder.loadTexts:
    pethMainPsePower.setUnits("Watts")


class _PethMainPseOperStatus_Type(Integer32):
    """Custom type pethMainPseOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 3),
          ("off", 2),
          ("on", 1))
    )


_PethMainPseOperStatus_Type.__name__ = "Integer32"
_PethMainPseOperStatus_Object = MibTableColumn
pethMainPseOperStatus = _PethMainPseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 3),
    _PethMainPseOperStatus_Type()
)
pethMainPseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethMainPseOperStatus.setStatus("current")
_PethMainPseConsumptionPower_Type = Gauge32
_PethMainPseConsumptionPower_Object = MibTableColumn
pethMainPseConsumptionPower = _PethMainPseConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 4),
    _PethMainPseConsumptionPower_Type()
)
pethMainPseConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pethMainPseConsumptionPower.setStatus("current")
if mibBuilder.loadTexts:
    pethMainPseConsumptionPower.setUnits("Watts")


class _PethMainPseUsageThreshold_Type(Integer32):
    """Custom type pethMainPseUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PethMainPseUsageThreshold_Type.__name__ = "Integer32"
_PethMainPseUsageThreshold_Object = MibTableColumn
pethMainPseUsageThreshold = _PethMainPseUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 3, 1, 1, 7),
    _PethMainPseUsageThreshold_Type()
)
pethMainPseUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethMainPseUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    pethMainPseUsageThreshold.setUnits("%")
_PethNotificationControl_ObjectIdentity = ObjectIdentity
pethNotificationControl = _PethNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4)
)
_PethNotificationControlTable_Object = MibTable
pethNotificationControlTable = _PethNotificationControlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pethNotificationControlTable.setStatus("current")
_PethNotificationControlEntry_Object = MibTableRow
pethNotificationControlEntry = _PethNotificationControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1, 1)
)
pethNotificationControlEntry.setIndexNames(
    (0, "ALU-POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"),
)
if mibBuilder.loadTexts:
    pethNotificationControlEntry.setStatus("current")


class _PethNotificationControlGroupIndex_Type(Integer32):
    """Custom type pethNotificationControlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PethNotificationControlGroupIndex_Type.__name__ = "Integer32"
_PethNotificationControlGroupIndex_Object = MibTableColumn
pethNotificationControlGroupIndex = _PethNotificationControlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1, 1, 1),
    _PethNotificationControlGroupIndex_Type()
)
pethNotificationControlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pethNotificationControlGroupIndex.setStatus("current")


class _PethNotificationControlEnable_Type(Integer32):
    """Custom type pethNotificationControlEnable based on Integer32"""
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


_PethNotificationControlEnable_Type.__name__ = "Integer32"
_PethNotificationControlEnable_Object = MibTableColumn
pethNotificationControlEnable = _PethNotificationControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 1, 4, 1, 1, 2),
    _PethNotificationControlEnable_Type()
)
pethNotificationControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pethNotificationControlEnable.setStatus("current")
_PethConformance_ObjectIdentity = ObjectIdentity
pethConformance = _PethConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2)
)
_PethCompliances_ObjectIdentity = ObjectIdentity
pethCompliances = _PethCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1)
)
_PethGroups_ObjectIdentity = ObjectIdentity
pethGroups = _PethGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2)
)

# Managed Objects groups

pethPsePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 1)
)
pethPsePortGroup.setObjects(
      *(("ALU-POWER-ETHERNET-MIB", "pethPsePortAdminEnable"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerDetectionControl"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerPairs"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerPriority"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatus"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortOverCurrentCounter"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortType"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"))
)
if mibBuilder.loadTexts:
    pethPsePortGroup.setStatus("current")

pethPdPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 2)
)
pethPdPortGroup.setObjects(
    ("ALU-POWER-ETHERNET-MIB", "pethPdPortAdminEnable")
)
if mibBuilder.loadTexts:
    pethPdPortGroup.setStatus("current")

pethMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 3)
)
pethMainPseGroup.setObjects(
      *(("ALU-POWER-ETHERNET-MIB", "pethMainPsePower"),
        ("ALU-POWER-ETHERNET-MIB", "pethMainPseOperStatus"),
        ("ALU-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"),
        ("ALU-POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"))
)
if mibBuilder.loadTexts:
    pethMainPseGroup.setStatus("current")

pethNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 2, 4)
)
pethNotificationControlGroup.setObjects(
    ("ALU-POWER-ETHERNET-MIB", "pethNotificationControlEnable")
)
if mibBuilder.loadTexts:
    pethNotificationControlGroup.setStatus("current")


# Notification objects

pethPsePortOnOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 1)
)
pethPsePortOnOffNotification.setObjects(
    ("ALU-POWER-ETHERNET-MIB", "pethPsePortDetectionStatus")
)
if mibBuilder.loadTexts:
    pethPsePortOnOffNotification.setStatus(
        "current"
    )

pethPsePortPowerMaintenanceStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 2)
)
pethPsePortPowerMaintenanceStatusNotification.setObjects(
    ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatus")
)
if mibBuilder.loadTexts:
    pethPsePortPowerMaintenanceStatusNotification.setStatus(
        "current"
    )

pethMainPowerUsageOnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 4)
)
pethMainPowerUsageOnNotification.setObjects(
    ("ALU-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower")
)
if mibBuilder.loadTexts:
    pethMainPowerUsageOnNotification.setStatus(
        "current"
    )

pethMainPowerUsageOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 0, 5)
)
pethMainPowerUsageOffNotification.setObjects(
    ("ALU-POWER-ETHERNET-MIB", "pethMainPseConsumptionPower")
)
if mibBuilder.loadTexts:
    pethMainPowerUsageOffNotification.setStatus(
        "current"
    )


# Notifications groups

pethPsePortNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 4)
)
pethPsePortNotificationGroup.setObjects(
      *(("ALU-POWER-ETHERNET-MIB", "pethPsePortOnOffNotification"),
        ("ALU-POWER-ETHERNET-MIB", "pethPsePortPowerMaintenanceStatusNotification"))
)
if mibBuilder.loadTexts:
    pethPsePortNotificationGroup.setStatus(
        "current"
    )

pethMainPowerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 5)
)
pethMainPowerNotificationGroup.setObjects(
      *(("ALU-POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"),
        ("ALU-POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"))
)
if mibBuilder.loadTexts:
    pethMainPowerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pethCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pethCompliance.setStatus(
        "current"
    )

pethPseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pethPseCompliance.setStatus(
        "current"
    )

pethPdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 27, 999, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pethPdCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-POWER-ETHERNET-MIB",
    **{"powerEthernetMIB": powerEthernetMIB,
       "pethNotifications": pethNotifications,
       "pethPsePortOnOffNotification": pethPsePortOnOffNotification,
       "pethPsePortPowerMaintenanceStatusNotification": pethPsePortPowerMaintenanceStatusNotification,
       "pethMainPowerUsageOnNotification": pethMainPowerUsageOnNotification,
       "pethMainPowerUsageOffNotification": pethMainPowerUsageOffNotification,
       "pethObjects": pethObjects,
       "pethPsePortTable": pethPsePortTable,
       "pethPsePortEntry": pethPsePortEntry,
       "pethPsePortGroupIndex": pethPsePortGroupIndex,
       "pethPsePortIndex": pethPsePortIndex,
       "pethPsePortAdminEnable": pethPsePortAdminEnable,
       "pethPsePortPowerPairsControlAbility": pethPsePortPowerPairsControlAbility,
       "pethPsePortPowerPairs": pethPsePortPowerPairs,
       "pethPsePortPowerDetectionControl": pethPsePortPowerDetectionControl,
       "pethPsePortDetectionStatus": pethPsePortDetectionStatus,
       "pethPsePortPowerPriority": pethPsePortPowerPriority,
       "pethPsePortPowerMaintenanceStatus": pethPsePortPowerMaintenanceStatus,
       "pethPsePortMPSAbsentCounter": pethPsePortMPSAbsentCounter,
       "pethPsePortOverCurrentCounter": pethPsePortOverCurrentCounter,
       "pethPsePortType": pethPsePortType,
       "pethPsePortPowerClassifications": pethPsePortPowerClassifications,
       "pethPdPortTable": pethPdPortTable,
       "pethPdPortEntry": pethPdPortEntry,
       "pethPdPortIndex": pethPdPortIndex,
       "pethPdPortAdminEnable": pethPdPortAdminEnable,
       "pethMainPseObjects": pethMainPseObjects,
       "pethMainPseTable": pethMainPseTable,
       "pethMainPseEntry": pethMainPseEntry,
       "pethMainPseGroupIndex": pethMainPseGroupIndex,
       "pethMainPsePower": pethMainPsePower,
       "pethMainPseOperStatus": pethMainPseOperStatus,
       "pethMainPseConsumptionPower": pethMainPseConsumptionPower,
       "pethMainPseUsageThreshold": pethMainPseUsageThreshold,
       "pethNotificationControl": pethNotificationControl,
       "pethNotificationControlTable": pethNotificationControlTable,
       "pethNotificationControlEntry": pethNotificationControlEntry,
       "pethNotificationControlGroupIndex": pethNotificationControlGroupIndex,
       "pethNotificationControlEnable": pethNotificationControlEnable,
       "pethConformance": pethConformance,
       "pethCompliances": pethCompliances,
       "pethCompliance": pethCompliance,
       "pethPseCompliance": pethPseCompliance,
       "pethPdCompliance": pethPdCompliance,
       "pethPsePortNotificationGroup": pethPsePortNotificationGroup,
       "pethMainPowerNotificationGroup": pethMainPowerNotificationGroup,
       "pethGroups": pethGroups,
       "pethPsePortGroup": pethPsePortGroup,
       "pethPdPortGroup": pethPdPortGroup,
       "pethMainPseGroup": pethMainPseGroup,
       "pethNotificationControlGroup": pethNotificationControlGroup}
)
