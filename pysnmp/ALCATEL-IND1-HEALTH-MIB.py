# SNMP MIB module (ALCATEL-IND1-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-HEALTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:08 2024
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

(softentIND1Health,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Health")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1HealthMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1)
)
alcatelIND1HealthMonitorMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1HealthMonitorMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBNotifications = _AlcatelIND1HealthMonitorMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBNotifications.setStatus("current")
_AlcatelIND1HealthMonitorMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBObjects = _AlcatelIND1HealthMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBObjects.setStatus("current")
_HealthModuleInfo_ObjectIdentity = ObjectIdentity
healthModuleInfo = _HealthModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1)
)
_HealthModuleTable_Object = MibTable
healthModuleTable = _HealthModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    healthModuleTable.setStatus("current")
_HealthModuleEntry_Object = MibTableRow
healthModuleEntry = _HealthModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1)
)
healthModuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthModuleSlot"),
)
if mibBuilder.loadTexts:
    healthModuleEntry.setStatus("current")


class _HealthModuleSlot_Type(Integer32):
    """Custom type healthModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7016),
    )


_HealthModuleSlot_Type.__name__ = "Integer32"
_HealthModuleSlot_Object = MibTableColumn
healthModuleSlot = _HealthModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 1),
    _HealthModuleSlot_Type()
)
healthModuleSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthModuleSlot.setStatus("current")


class _HealthModuleRx1MinAvg_Type(Integer32):
    """Custom type healthModuleRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRx1MinAvg_Type.__name__ = "Integer32"
_HealthModuleRx1MinAvg_Object = MibTableColumn
healthModuleRx1MinAvg = _HealthModuleRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 2),
    _HealthModuleRx1MinAvg_Type()
)
healthModuleRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRx1MinAvg.setStatus("current")


class _HealthModuleRx1HrAvg_Type(Integer32):
    """Custom type healthModuleRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRx1HrAvg_Type.__name__ = "Integer32"
_HealthModuleRx1HrAvg_Object = MibTableColumn
healthModuleRx1HrAvg = _HealthModuleRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 3),
    _HealthModuleRx1HrAvg_Type()
)
healthModuleRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRx1HrAvg.setStatus("current")


class _HealthModuleRx1DayAvg_Type(Integer32):
    """Custom type healthModuleRx1DayAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRx1DayAvg_Type.__name__ = "Integer32"
_HealthModuleRx1DayAvg_Object = MibTableColumn
healthModuleRx1DayAvg = _HealthModuleRx1DayAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 4),
    _HealthModuleRx1DayAvg_Type()
)
healthModuleRx1DayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRx1DayAvg.setStatus("current")


class _HealthModuleRxTx1MinAvg_Type(Integer32):
    """Custom type healthModuleRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxTx1MinAvg_Type.__name__ = "Integer32"
_HealthModuleRxTx1MinAvg_Object = MibTableColumn
healthModuleRxTx1MinAvg = _HealthModuleRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 5),
    _HealthModuleRxTx1MinAvg_Type()
)
healthModuleRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTx1MinAvg.setStatus("current")


class _HealthModuleRxTx1HrAvg_Type(Integer32):
    """Custom type healthModuleRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxTx1HrAvg_Type.__name__ = "Integer32"
_HealthModuleRxTx1HrAvg_Object = MibTableColumn
healthModuleRxTx1HrAvg = _HealthModuleRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 6),
    _HealthModuleRxTx1HrAvg_Type()
)
healthModuleRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTx1HrAvg.setStatus("current")


class _HealthModuleRxTx1DayAvg_Type(Integer32):
    """Custom type healthModuleRxTx1DayAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleRxTx1DayAvg_Type.__name__ = "Integer32"
_HealthModuleRxTx1DayAvg_Object = MibTableColumn
healthModuleRxTx1DayAvg = _HealthModuleRxTx1DayAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 7),
    _HealthModuleRxTx1DayAvg_Type()
)
healthModuleRxTx1DayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleRxTx1DayAvg.setStatus("current")


class _HealthModuleMemory1MinAvg_Type(Integer32):
    """Custom type healthModuleMemory1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleMemory1MinAvg_Type.__name__ = "Integer32"
_HealthModuleMemory1MinAvg_Object = MibTableColumn
healthModuleMemory1MinAvg = _HealthModuleMemory1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 8),
    _HealthModuleMemory1MinAvg_Type()
)
healthModuleMemory1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleMemory1MinAvg.setStatus("current")


class _HealthModuleMemory1HrAvg_Type(Integer32):
    """Custom type healthModuleMemory1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleMemory1HrAvg_Type.__name__ = "Integer32"
_HealthModuleMemory1HrAvg_Object = MibTableColumn
healthModuleMemory1HrAvg = _HealthModuleMemory1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 9),
    _HealthModuleMemory1HrAvg_Type()
)
healthModuleMemory1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleMemory1HrAvg.setStatus("current")


class _HealthModuleMemory1DayAvg_Type(Integer32):
    """Custom type healthModuleMemory1DayAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleMemory1DayAvg_Type.__name__ = "Integer32"
_HealthModuleMemory1DayAvg_Object = MibTableColumn
healthModuleMemory1DayAvg = _HealthModuleMemory1DayAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 10),
    _HealthModuleMemory1DayAvg_Type()
)
healthModuleMemory1DayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleMemory1DayAvg.setStatus("current")


class _HealthModuleCpu1MinAvg_Type(Integer32):
    """Custom type healthModuleCpu1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleCpu1MinAvg_Type.__name__ = "Integer32"
_HealthModuleCpu1MinAvg_Object = MibTableColumn
healthModuleCpu1MinAvg = _HealthModuleCpu1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 11),
    _HealthModuleCpu1MinAvg_Type()
)
healthModuleCpu1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCpu1MinAvg.setStatus("current")


class _HealthModuleCpu1HrAvg_Type(Integer32):
    """Custom type healthModuleCpu1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleCpu1HrAvg_Type.__name__ = "Integer32"
_HealthModuleCpu1HrAvg_Object = MibTableColumn
healthModuleCpu1HrAvg = _HealthModuleCpu1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 12),
    _HealthModuleCpu1HrAvg_Type()
)
healthModuleCpu1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCpu1HrAvg.setStatus("current")


class _HealthModuleCpu1DayAvg_Type(Integer32):
    """Custom type healthModuleCpu1DayAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthModuleCpu1DayAvg_Type.__name__ = "Integer32"
_HealthModuleCpu1DayAvg_Object = MibTableColumn
healthModuleCpu1DayAvg = _HealthModuleCpu1DayAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 13),
    _HealthModuleCpu1DayAvg_Type()
)
healthModuleCpu1DayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleCpu1DayAvg.setStatus("current")


class _HealthModuleChassisId_Type(Integer32):
    """Custom type healthModuleChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HealthModuleChassisId_Type.__name__ = "Integer32"
_HealthModuleChassisId_Object = MibTableColumn
healthModuleChassisId = _HealthModuleChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 1, 1, 1, 14),
    _HealthModuleChassisId_Type()
)
healthModuleChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthModuleChassisId.setStatus("current")
_HealthPortInfo_ObjectIdentity = ObjectIdentity
healthPortInfo = _HealthPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2)
)
_HealthPortTable_Object = MibTable
healthPortTable = _HealthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    healthPortTable.setStatus("current")
_HealthPortEntry_Object = MibTableRow
healthPortEntry = _HealthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1)
)
healthPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-HEALTH-MIB", "healthPortIfIndex"),
)
if mibBuilder.loadTexts:
    healthPortEntry.setStatus("current")


class _HealthPortIfIndex_Type(Integer32):
    """Custom type healthPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HealthPortIfIndex_Type.__name__ = "Integer32"
_HealthPortIfIndex_Object = MibTableColumn
healthPortIfIndex = _HealthPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1, 1),
    _HealthPortIfIndex_Type()
)
healthPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    healthPortIfIndex.setStatus("current")


class _HealthPortRx1MinAvg_Type(Integer32):
    """Custom type healthPortRx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRx1MinAvg_Type.__name__ = "Integer32"
_HealthPortRx1MinAvg_Object = MibTableColumn
healthPortRx1MinAvg = _HealthPortRx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1, 2),
    _HealthPortRx1MinAvg_Type()
)
healthPortRx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRx1MinAvg.setStatus("current")


class _HealthPortRx1HrAvg_Type(Integer32):
    """Custom type healthPortRx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRx1HrAvg_Type.__name__ = "Integer32"
_HealthPortRx1HrAvg_Object = MibTableColumn
healthPortRx1HrAvg = _HealthPortRx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1, 3),
    _HealthPortRx1HrAvg_Type()
)
healthPortRx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRx1HrAvg.setStatus("current")


class _HealthPortRx1DayAvg_Type(Integer32):
    """Custom type healthPortRx1DayAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRx1DayAvg_Type.__name__ = "Integer32"
_HealthPortRx1DayAvg_Object = MibTableColumn
healthPortRx1DayAvg = _HealthPortRx1DayAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1, 4),
    _HealthPortRx1DayAvg_Type()
)
healthPortRx1DayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRx1DayAvg.setStatus("current")


class _HealthPortRxTx1MinAvg_Type(Integer32):
    """Custom type healthPortRxTx1MinAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxTx1MinAvg_Type.__name__ = "Integer32"
_HealthPortRxTx1MinAvg_Object = MibTableColumn
healthPortRxTx1MinAvg = _HealthPortRxTx1MinAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1, 5),
    _HealthPortRxTx1MinAvg_Type()
)
healthPortRxTx1MinAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTx1MinAvg.setStatus("current")


class _HealthPortRxTx1HrAvg_Type(Integer32):
    """Custom type healthPortRxTx1HrAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxTx1HrAvg_Type.__name__ = "Integer32"
_HealthPortRxTx1HrAvg_Object = MibTableColumn
healthPortRxTx1HrAvg = _HealthPortRxTx1HrAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1, 6),
    _HealthPortRxTx1HrAvg_Type()
)
healthPortRxTx1HrAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTx1HrAvg.setStatus("current")


class _HealthPortRxTx1DayAvg_Type(Integer32):
    """Custom type healthPortRxTx1DayAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthPortRxTx1DayAvg_Type.__name__ = "Integer32"
_HealthPortRxTx1DayAvg_Object = MibTableColumn
healthPortRxTx1DayAvg = _HealthPortRxTx1DayAvg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 2, 1, 1, 7),
    _HealthPortRxTx1DayAvg_Type()
)
healthPortRxTx1DayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthPortRxTx1DayAvg.setStatus("current")
_HealthControlInfo_ObjectIdentity = ObjectIdentity
healthControlInfo = _HealthControlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 3)
)


class _HealthSamplingInterval_Type(Integer32):
    """Custom type healthSamplingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HealthSamplingInterval_Type.__name__ = "Integer32"
_HealthSamplingInterval_Object = MibScalar
healthSamplingInterval = _HealthSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 3, 1),
    _HealthSamplingInterval_Type()
)
healthSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthSamplingInterval.setStatus("current")
_HealthThreshInfo_ObjectIdentity = ObjectIdentity
healthThreshInfo = _HealthThreshInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 4)
)


class _HealthThreshRxLimit_Type(Integer32):
    """Custom type healthThreshRxLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshRxLimit_Type.__name__ = "Integer32"
_HealthThreshRxLimit_Object = MibScalar
healthThreshRxLimit = _HealthThreshRxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 4, 1),
    _HealthThreshRxLimit_Type()
)
healthThreshRxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshRxLimit.setStatus("current")


class _HealthThreshRxTxLimit_Type(Integer32):
    """Custom type healthThreshRxTxLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshRxTxLimit_Type.__name__ = "Integer32"
_HealthThreshRxTxLimit_Object = MibScalar
healthThreshRxTxLimit = _HealthThreshRxTxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 4, 2),
    _HealthThreshRxTxLimit_Type()
)
healthThreshRxTxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshRxTxLimit.setStatus("current")


class _HealthThreshMemoryLimit_Type(Integer32):
    """Custom type healthThreshMemoryLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshMemoryLimit_Type.__name__ = "Integer32"
_HealthThreshMemoryLimit_Object = MibScalar
healthThreshMemoryLimit = _HealthThreshMemoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 4, 3),
    _HealthThreshMemoryLimit_Type()
)
healthThreshMemoryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshMemoryLimit.setStatus("current")


class _HealthThreshCpuLimit_Type(Integer32):
    """Custom type healthThreshCpuLimit based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HealthThreshCpuLimit_Type.__name__ = "Integer32"
_HealthThreshCpuLimit_Object = MibScalar
healthThreshCpuLimit = _HealthThreshCpuLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 4, 4),
    _HealthThreshCpuLimit_Type()
)
healthThreshCpuLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    healthThreshCpuLimit.setStatus("current")
_HealthTrapInfo_ObjectIdentity = ObjectIdentity
healthTrapInfo = _HealthTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 5)
)


class _HealthMonRxStatus_Type(Integer32):
    """Custom type healthMonRxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedAboveThreshold", 3),
          ("crossedBelowThreshold", 1),
          ("noChange", 2))
    )


_HealthMonRxStatus_Type.__name__ = "Integer32"
_HealthMonRxStatus_Object = MibScalar
healthMonRxStatus = _HealthMonRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 5, 1),
    _HealthMonRxStatus_Type()
)
healthMonRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonRxStatus.setStatus("current")


class _HealthMonRxTxStatus_Type(Integer32):
    """Custom type healthMonRxTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedAboveThreshold", 3),
          ("crossedBelowThreshold", 1),
          ("noChange", 2))
    )


_HealthMonRxTxStatus_Type.__name__ = "Integer32"
_HealthMonRxTxStatus_Object = MibScalar
healthMonRxTxStatus = _HealthMonRxTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 5, 2),
    _HealthMonRxTxStatus_Type()
)
healthMonRxTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonRxTxStatus.setStatus("current")


class _HealthMonMemoryStatus_Type(Integer32):
    """Custom type healthMonMemoryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedAboveThreshold", 3),
          ("crossedBelowThreshold", 1),
          ("noChange", 2))
    )


_HealthMonMemoryStatus_Type.__name__ = "Integer32"
_HealthMonMemoryStatus_Object = MibScalar
healthMonMemoryStatus = _HealthMonMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 5, 3),
    _HealthMonMemoryStatus_Type()
)
healthMonMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonMemoryStatus.setStatus("current")


class _HealthMonCpuStatus_Type(Integer32):
    """Custom type healthMonCpuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedAboveThreshold", 3),
          ("crossedBelowThreshold", 1),
          ("noChange", 2))
    )


_HealthMonCpuStatus_Type.__name__ = "Integer32"
_HealthMonCpuStatus_Object = MibScalar
healthMonCpuStatus = _HealthMonCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 1, 5, 4),
    _HealthMonCpuStatus_Type()
)
healthMonCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    healthMonCpuStatus.setStatus("current")
_AlcatelIND1HealthMonitorMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBConformance = _AlcatelIND1HealthMonitorMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBConformance.setStatus("current")
_AlcatelIND1HealthMonitorMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBGroups = _AlcatelIND1HealthMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBGroups.setStatus("current")
_AlcatelIND1HealthMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1HealthMonitorMIBCompliances = _AlcatelIND1HealthMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBCompliances.setStatus("current")

# Managed Objects groups

healthModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 1, 1)
)
healthModuleGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthModuleRx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRx1DayAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleRxTx1DayAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleMemory1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleMemory1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleMemory1DayAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpu1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpu1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleCpu1DayAvg"))
)
if mibBuilder.loadTexts:
    healthModuleGroup.setStatus("current")

healthPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 1, 2)
)
healthPortGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthPortRx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRx1DayAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTx1MinAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTx1HrAvg"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortRxTx1DayAvg"))
)
if mibBuilder.loadTexts:
    healthPortGroup.setStatus("current")

healthControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 1, 3)
)
healthControlGroup.setObjects(
    ("ALCATEL-IND1-HEALTH-MIB", "healthSamplingInterval")
)
if mibBuilder.loadTexts:
    healthControlGroup.setStatus("current")

healthThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 1, 4)
)
healthThreshGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthThreshRxLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshRxTxLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshMemoryLimit"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthThreshCpuLimit"))
)
if mibBuilder.loadTexts:
    healthThreshGroup.setStatus("current")

healthTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 1, 5)
)
healthTrapObjectsGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthMonRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxTxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonMemoryStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCpuStatus"))
)
if mibBuilder.loadTexts:
    healthTrapObjectsGroup.setStatus("current")


# Notification objects

healthMonModuleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 0, 1)
)
healthMonModuleTrap.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthModuleChassisId"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleSlot"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxTxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonMemoryStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCpuStatus"))
)
if mibBuilder.loadTexts:
    healthMonModuleTrap.setStatus(
        "current"
    )

healthMonPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 0, 2)
)
healthMonPortTrap.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthModuleChassisId"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthModuleSlot"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthPortIfIndex"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonRxTxStatus"))
)
if mibBuilder.loadTexts:
    healthMonPortTrap.setStatus(
        "current"
    )

healthMonCmmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 0, 3)
)
healthMonCmmTrap.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthMonMemoryStatus"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCpuStatus"))
)
if mibBuilder.loadTexts:
    healthMonCmmTrap.setStatus(
        "current"
    )


# Notifications groups

healthTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 1, 6)
)
healthTrapsGroup.setObjects(
      *(("ALCATEL-IND1-HEALTH-MIB", "healthMonModuleTrap"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonPortTrap"),
        ("ALCATEL-IND1-HEALTH-MIB", "healthMonCmmTrap"))
)
if mibBuilder.loadTexts:
    healthTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1HealthMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 16, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1HealthMonitorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-HEALTH-MIB",
    **{"alcatelIND1HealthMonitorMIB": alcatelIND1HealthMonitorMIB,
       "alcatelIND1HealthMonitorMIBNotifications": alcatelIND1HealthMonitorMIBNotifications,
       "healthMonModuleTrap": healthMonModuleTrap,
       "healthMonPortTrap": healthMonPortTrap,
       "healthMonCmmTrap": healthMonCmmTrap,
       "alcatelIND1HealthMonitorMIBObjects": alcatelIND1HealthMonitorMIBObjects,
       "healthModuleInfo": healthModuleInfo,
       "healthModuleTable": healthModuleTable,
       "healthModuleEntry": healthModuleEntry,
       "healthModuleSlot": healthModuleSlot,
       "healthModuleRx1MinAvg": healthModuleRx1MinAvg,
       "healthModuleRx1HrAvg": healthModuleRx1HrAvg,
       "healthModuleRx1DayAvg": healthModuleRx1DayAvg,
       "healthModuleRxTx1MinAvg": healthModuleRxTx1MinAvg,
       "healthModuleRxTx1HrAvg": healthModuleRxTx1HrAvg,
       "healthModuleRxTx1DayAvg": healthModuleRxTx1DayAvg,
       "healthModuleMemory1MinAvg": healthModuleMemory1MinAvg,
       "healthModuleMemory1HrAvg": healthModuleMemory1HrAvg,
       "healthModuleMemory1DayAvg": healthModuleMemory1DayAvg,
       "healthModuleCpu1MinAvg": healthModuleCpu1MinAvg,
       "healthModuleCpu1HrAvg": healthModuleCpu1HrAvg,
       "healthModuleCpu1DayAvg": healthModuleCpu1DayAvg,
       "healthModuleChassisId": healthModuleChassisId,
       "healthPortInfo": healthPortInfo,
       "healthPortTable": healthPortTable,
       "healthPortEntry": healthPortEntry,
       "healthPortIfIndex": healthPortIfIndex,
       "healthPortRx1MinAvg": healthPortRx1MinAvg,
       "healthPortRx1HrAvg": healthPortRx1HrAvg,
       "healthPortRx1DayAvg": healthPortRx1DayAvg,
       "healthPortRxTx1MinAvg": healthPortRxTx1MinAvg,
       "healthPortRxTx1HrAvg": healthPortRxTx1HrAvg,
       "healthPortRxTx1DayAvg": healthPortRxTx1DayAvg,
       "healthControlInfo": healthControlInfo,
       "healthSamplingInterval": healthSamplingInterval,
       "healthThreshInfo": healthThreshInfo,
       "healthThreshRxLimit": healthThreshRxLimit,
       "healthThreshRxTxLimit": healthThreshRxTxLimit,
       "healthThreshMemoryLimit": healthThreshMemoryLimit,
       "healthThreshCpuLimit": healthThreshCpuLimit,
       "healthTrapInfo": healthTrapInfo,
       "healthMonRxStatus": healthMonRxStatus,
       "healthMonRxTxStatus": healthMonRxTxStatus,
       "healthMonMemoryStatus": healthMonMemoryStatus,
       "healthMonCpuStatus": healthMonCpuStatus,
       "alcatelIND1HealthMonitorMIBConformance": alcatelIND1HealthMonitorMIBConformance,
       "alcatelIND1HealthMonitorMIBGroups": alcatelIND1HealthMonitorMIBGroups,
       "healthModuleGroup": healthModuleGroup,
       "healthPortGroup": healthPortGroup,
       "healthControlGroup": healthControlGroup,
       "healthThreshGroup": healthThreshGroup,
       "healthTrapObjectsGroup": healthTrapObjectsGroup,
       "healthTrapsGroup": healthTrapsGroup,
       "alcatelIND1HealthMonitorMIBCompliances": alcatelIND1HealthMonitorMIBCompliances,
       "alcatelIND1HealthMonitorMIBCompliance": alcatelIND1HealthMonitorMIBCompliance}
)
