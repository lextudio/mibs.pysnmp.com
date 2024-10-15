# SNMP MIB module (HP-ICF-MVRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-MVRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:50 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

hpicfMvrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117)
)
hpicfMvrpMIB.setRevisions(
        ("2015-04-20 00:00",
         "2015-03-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfMvrpNotifications_ObjectIdentity = ObjectIdentity
hpicfMvrpNotifications = _HpicfMvrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 0)
)
_HpicfMvrpObjects_ObjectIdentity = ObjectIdentity
hpicfMvrpObjects = _HpicfMvrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1)
)
_HpicfMvrpConfig_ObjectIdentity = ObjectIdentity
hpicfMvrpConfig = _HpicfMvrpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1)
)
_HpicfMvrpGlobalClearStats_Type = TruthValue
_HpicfMvrpGlobalClearStats_Object = MibScalar
hpicfMvrpGlobalClearStats = _HpicfMvrpGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 1),
    _HpicfMvrpGlobalClearStats_Type()
)
hpicfMvrpGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMvrpGlobalClearStats.setStatus("current")
_HpicfMvrpMaxVlanLimit_Type = Integer32
_HpicfMvrpMaxVlanLimit_Object = MibScalar
hpicfMvrpMaxVlanLimit = _HpicfMvrpMaxVlanLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 2),
    _HpicfMvrpMaxVlanLimit_Type()
)
hpicfMvrpMaxVlanLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMvrpMaxVlanLimit.setStatus("current")
_HpicfMvrpPortConfigTable_Object = MibTable
hpicfMvrpPortConfigTable = _HpicfMvrpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfMvrpPortConfigTable.setStatus("current")
_HpicfMvrpPortConfigEntry_Object = MibTableRow
hpicfMvrpPortConfigEntry = _HpicfMvrpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 3, 1)
)
hpicfMvrpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfMvrpPortConfigEntry.setStatus("current")


class _HpicfMvrpPortConfigRegistrarMode_Type(Integer32):
    """Custom type hpicfMvrpPortConfigRegistrarMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("normal", 1))
    )


_HpicfMvrpPortConfigRegistrarMode_Type.__name__ = "Integer32"
_HpicfMvrpPortConfigRegistrarMode_Object = MibTableColumn
hpicfMvrpPortConfigRegistrarMode = _HpicfMvrpPortConfigRegistrarMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 3, 1, 1),
    _HpicfMvrpPortConfigRegistrarMode_Type()
)
hpicfMvrpPortConfigRegistrarMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMvrpPortConfigRegistrarMode.setStatus("current")


class _HpicfMvrpPortConfigPeriodicTimer_Type(TimeInterval):
    """Custom type hpicfMvrpPortConfigPeriodicTimer based on TimeInterval"""
    defaultValue = 100

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000000),
    )


_HpicfMvrpPortConfigPeriodicTimer_Type.__name__ = "TimeInterval"
_HpicfMvrpPortConfigPeriodicTimer_Object = MibTableColumn
hpicfMvrpPortConfigPeriodicTimer = _HpicfMvrpPortConfigPeriodicTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 3, 1, 2),
    _HpicfMvrpPortConfigPeriodicTimer_Type()
)
hpicfMvrpPortConfigPeriodicTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMvrpPortConfigPeriodicTimer.setStatus("current")
if mibBuilder.loadTexts:
    hpicfMvrpPortConfigPeriodicTimer.setUnits("centi-seconds")


class _HpicfMvrpPortConfigPeriodicTransmissionStatus_Type(EnabledStatus):
    """Custom type hpicfMvrpPortConfigPeriodicTransmissionStatus based on EnabledStatus"""


_HpicfMvrpPortConfigPeriodicTransmissionStatus_Object = MibTableColumn
hpicfMvrpPortConfigPeriodicTransmissionStatus = _HpicfMvrpPortConfigPeriodicTransmissionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 3, 1, 3),
    _HpicfMvrpPortConfigPeriodicTransmissionStatus_Type()
)
hpicfMvrpPortConfigPeriodicTransmissionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMvrpPortConfigPeriodicTransmissionStatus.setStatus("current")
_HpicfMvrpPortStatsClearStats_Type = TruthValue
_HpicfMvrpPortStatsClearStats_Object = MibTableColumn
hpicfMvrpPortStatsClearStats = _HpicfMvrpPortStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 1, 3, 1, 4),
    _HpicfMvrpPortStatsClearStats_Type()
)
hpicfMvrpPortStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsClearStats.setStatus("current")
_HpicfMvrpStats_ObjectIdentity = ObjectIdentity
hpicfMvrpStats = _HpicfMvrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2)
)
_HpicfMvrpPortStatsTable_Object = MibTable
hpicfMvrpPortStatsTable = _HpicfMvrpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsTable.setStatus("current")
_HpicfMvrpPortStatsEntry_Object = MibTableRow
hpicfMvrpPortStatsEntry = _HpicfMvrpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1)
)
hpicfMvrpPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsEntry.setStatus("current")
_HpicfMvrpPortStatsNewReceived_Type = Counter32
_HpicfMvrpPortStatsNewReceived_Object = MibTableColumn
hpicfMvrpPortStatsNewReceived = _HpicfMvrpPortStatsNewReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 1),
    _HpicfMvrpPortStatsNewReceived_Type()
)
hpicfMvrpPortStatsNewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsNewReceived.setStatus("current")
_HpicfMvrpPortStatsJoinInReceived_Type = Counter32
_HpicfMvrpPortStatsJoinInReceived_Object = MibTableColumn
hpicfMvrpPortStatsJoinInReceived = _HpicfMvrpPortStatsJoinInReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 2),
    _HpicfMvrpPortStatsJoinInReceived_Type()
)
hpicfMvrpPortStatsJoinInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsJoinInReceived.setStatus("current")
_HpicfMvrpPortStatsJoinEmptyReceived_Type = Counter32
_HpicfMvrpPortStatsJoinEmptyReceived_Object = MibTableColumn
hpicfMvrpPortStatsJoinEmptyReceived = _HpicfMvrpPortStatsJoinEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 3),
    _HpicfMvrpPortStatsJoinEmptyReceived_Type()
)
hpicfMvrpPortStatsJoinEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsJoinEmptyReceived.setStatus("current")
_HpicfMvrpPortStatsLeaveReceived_Type = Counter32
_HpicfMvrpPortStatsLeaveReceived_Object = MibTableColumn
hpicfMvrpPortStatsLeaveReceived = _HpicfMvrpPortStatsLeaveReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 4),
    _HpicfMvrpPortStatsLeaveReceived_Type()
)
hpicfMvrpPortStatsLeaveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsLeaveReceived.setStatus("current")
_HpicfMvrpPortStatsInReceived_Type = Counter32
_HpicfMvrpPortStatsInReceived_Object = MibTableColumn
hpicfMvrpPortStatsInReceived = _HpicfMvrpPortStatsInReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 5),
    _HpicfMvrpPortStatsInReceived_Type()
)
hpicfMvrpPortStatsInReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsInReceived.setStatus("current")
_HpicfMvrpPortStatsEmptyReceived_Type = Counter32
_HpicfMvrpPortStatsEmptyReceived_Object = MibTableColumn
hpicfMvrpPortStatsEmptyReceived = _HpicfMvrpPortStatsEmptyReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 6),
    _HpicfMvrpPortStatsEmptyReceived_Type()
)
hpicfMvrpPortStatsEmptyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsEmptyReceived.setStatus("current")
_HpicfMvrpPortStatsLeaveAllReceived_Type = Counter32
_HpicfMvrpPortStatsLeaveAllReceived_Object = MibTableColumn
hpicfMvrpPortStatsLeaveAllReceived = _HpicfMvrpPortStatsLeaveAllReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 7),
    _HpicfMvrpPortStatsLeaveAllReceived_Type()
)
hpicfMvrpPortStatsLeaveAllReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsLeaveAllReceived.setStatus("current")
_HpicfMvrpPortStatsNewTransmitted_Type = Counter32
_HpicfMvrpPortStatsNewTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsNewTransmitted = _HpicfMvrpPortStatsNewTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 8),
    _HpicfMvrpPortStatsNewTransmitted_Type()
)
hpicfMvrpPortStatsNewTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsNewTransmitted.setStatus("current")
_HpicfMvrpPortStatsJoinInTransmitted_Type = Counter32
_HpicfMvrpPortStatsJoinInTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsJoinInTransmitted = _HpicfMvrpPortStatsJoinInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 9),
    _HpicfMvrpPortStatsJoinInTransmitted_Type()
)
hpicfMvrpPortStatsJoinInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsJoinInTransmitted.setStatus("current")
_HpicfMvrpPortStatsJoinEmptyTransmitted_Type = Counter32
_HpicfMvrpPortStatsJoinEmptyTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsJoinEmptyTransmitted = _HpicfMvrpPortStatsJoinEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 10),
    _HpicfMvrpPortStatsJoinEmptyTransmitted_Type()
)
hpicfMvrpPortStatsJoinEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsJoinEmptyTransmitted.setStatus("current")
_HpicfMvrpPortStatsLeaveTransmitted_Type = Counter32
_HpicfMvrpPortStatsLeaveTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsLeaveTransmitted = _HpicfMvrpPortStatsLeaveTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 11),
    _HpicfMvrpPortStatsLeaveTransmitted_Type()
)
hpicfMvrpPortStatsLeaveTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsLeaveTransmitted.setStatus("current")
_HpicfMvrpPortStatsInTransmitted_Type = Counter32
_HpicfMvrpPortStatsInTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsInTransmitted = _HpicfMvrpPortStatsInTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 12),
    _HpicfMvrpPortStatsInTransmitted_Type()
)
hpicfMvrpPortStatsInTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsInTransmitted.setStatus("current")
_HpicfMvrpPortStatsEmptyTransmitted_Type = Counter32
_HpicfMvrpPortStatsEmptyTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsEmptyTransmitted = _HpicfMvrpPortStatsEmptyTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 13),
    _HpicfMvrpPortStatsEmptyTransmitted_Type()
)
hpicfMvrpPortStatsEmptyTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsEmptyTransmitted.setStatus("current")
_HpicfMvrpPortStatsLeaveAllTransmitted_Type = Counter32
_HpicfMvrpPortStatsLeaveAllTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsLeaveAllTransmitted = _HpicfMvrpPortStatsLeaveAllTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 14),
    _HpicfMvrpPortStatsLeaveAllTransmitted_Type()
)
hpicfMvrpPortStatsLeaveAllTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsLeaveAllTransmitted.setStatus("current")
_HpicfMvrpPortStatsTotalPDUReceived_Type = Counter32
_HpicfMvrpPortStatsTotalPDUReceived_Object = MibTableColumn
hpicfMvrpPortStatsTotalPDUReceived = _HpicfMvrpPortStatsTotalPDUReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 15),
    _HpicfMvrpPortStatsTotalPDUReceived_Type()
)
hpicfMvrpPortStatsTotalPDUReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsTotalPDUReceived.setStatus("current")
_HpicfMvrpPortStatsTotalPDUTransmitted_Type = Counter32
_HpicfMvrpPortStatsTotalPDUTransmitted_Object = MibTableColumn
hpicfMvrpPortStatsTotalPDUTransmitted = _HpicfMvrpPortStatsTotalPDUTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 16),
    _HpicfMvrpPortStatsTotalPDUTransmitted_Type()
)
hpicfMvrpPortStatsTotalPDUTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsTotalPDUTransmitted.setStatus("current")
_HpicfMvrpPortStatsFramesDiscarded_Type = Counter32
_HpicfMvrpPortStatsFramesDiscarded_Object = MibTableColumn
hpicfMvrpPortStatsFramesDiscarded = _HpicfMvrpPortStatsFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 1, 1, 17),
    _HpicfMvrpPortStatsFramesDiscarded_Type()
)
hpicfMvrpPortStatsFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsFramesDiscarded.setStatus("current")
_HpicfBridgeMvrpStateTable_Object = MibTable
hpicfBridgeMvrpStateTable = _HpicfBridgeMvrpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfBridgeMvrpStateTable.setStatus("current")
_HpicfBridgeMvrpStateEntry_Object = MibTableRow
hpicfBridgeMvrpStateEntry = _HpicfBridgeMvrpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 2, 1)
)
hpicfBridgeMvrpStateEntry.setIndexNames(
    (0, "HP-ICF-MVRP-MIB", "hpicfMvrpVlanId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfBridgeMvrpStateEntry.setStatus("current")
_HpicfMvrpVlanId_Type = VlanId
_HpicfMvrpVlanId_Object = MibTableColumn
hpicfMvrpVlanId = _HpicfMvrpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 2, 1, 1),
    _HpicfMvrpVlanId_Type()
)
hpicfMvrpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMvrpVlanId.setStatus("current")


class _HpicfMvrpApplicantState_Type(Integer32):
    """Custom type hpicfMvrpApplicantState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("aa", 0),
          ("an", 11),
          ("ao", 7),
          ("ap", 4),
          ("la", 2),
          ("lo", 9),
          ("qa", 1),
          ("qo", 8),
          ("qp", 5),
          ("vn", 10),
          ("vo", 6),
          ("vp", 3))
    )


_HpicfMvrpApplicantState_Type.__name__ = "Integer32"
_HpicfMvrpApplicantState_Object = MibTableColumn
hpicfMvrpApplicantState = _HpicfMvrpApplicantState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 2, 1, 2),
    _HpicfMvrpApplicantState_Type()
)
hpicfMvrpApplicantState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpApplicantState.setStatus("current")


class _HpicfMvrpRegistrarState_Type(Integer32):
    """Custom type hpicfMvrpRegistrarState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("lv", 2),
          ("mt", 3))
    )


_HpicfMvrpRegistrarState_Type.__name__ = "Integer32"
_HpicfMvrpRegistrarState_Object = MibTableColumn
hpicfMvrpRegistrarState = _HpicfMvrpRegistrarState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 1, 2, 2, 1, 3),
    _HpicfMvrpRegistrarState_Type()
)
hpicfMvrpRegistrarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMvrpRegistrarState.setStatus("current")
_HpicfMvrpConformance_ObjectIdentity = ObjectIdentity
hpicfMvrpConformance = _HpicfMvrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3)
)
_HpicfMvrpCompliances_ObjectIdentity = ObjectIdentity
hpicfMvrpCompliances = _HpicfMvrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 1)
)
_HpicfMvrpGroups_ObjectIdentity = ObjectIdentity
hpicfMvrpGroups = _HpicfMvrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 2)
)

# Managed Objects groups

hpicfMvrpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 2, 1)
)
hpicfMvrpBaseGroup.setObjects(
      *(("HP-ICF-MVRP-MIB", "hpicfMvrpGlobalClearStats"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpMaxVlanLimit"))
)
if mibBuilder.loadTexts:
    hpicfMvrpBaseGroup.setStatus("current")

hpicfMvrpPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 2, 2)
)
hpicfMvrpPortConfigGroup.setObjects(
      *(("HP-ICF-MVRP-MIB", "hpicfMvrpPortConfigRegistrarMode"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortConfigPeriodicTimer"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortConfigPeriodicTransmissionStatus"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsClearStats"))
)
if mibBuilder.loadTexts:
    hpicfMvrpPortConfigGroup.setStatus("current")

hpicfMvrpPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 2, 3)
)
hpicfMvrpPortStatsGroup.setObjects(
      *(("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsNewReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsJoinInReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsJoinEmptyReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsLeaveReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsInReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsEmptyReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsLeaveAllReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsNewTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsJoinInTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsJoinEmptyTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsLeaveTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsInTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsEmptyTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsLeaveAllTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsTotalPDUReceived"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsTotalPDUTransmitted"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpPortStatsFramesDiscarded"))
)
if mibBuilder.loadTexts:
    hpicfMvrpPortStatsGroup.setStatus("current")

hpicfMvrpPortStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 2, 4)
)
hpicfMvrpPortStateGroup.setObjects(
      *(("HP-ICF-MVRP-MIB", "hpicfMvrpApplicantState"),
        ("HP-ICF-MVRP-MIB", "hpicfMvrpRegistrarState"))
)
if mibBuilder.loadTexts:
    hpicfMvrpPortStateGroup.setStatus("current")


# Notification objects

hpicfMvrpVlanLimitReachedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 0, 1)
)
hpicfMvrpVlanLimitReachedEvent.setObjects(
    ("HP-ICF-MVRP-MIB", "hpicfMvrpMaxVlanLimit")
)
if mibBuilder.loadTexts:
    hpicfMvrpVlanLimitReachedEvent.setStatus(
        "current"
    )


# Notifications groups

hpicfMvrpNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 2, 5)
)
hpicfMvrpNotifyGroup.setObjects(
    ("HP-ICF-MVRP-MIB", "hpicfMvrpVlanLimitReachedEvent")
)
if mibBuilder.loadTexts:
    hpicfMvrpNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfMvrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfMvrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-MVRP-MIB",
    **{"hpicfMvrpMIB": hpicfMvrpMIB,
       "hpicfMvrpNotifications": hpicfMvrpNotifications,
       "hpicfMvrpVlanLimitReachedEvent": hpicfMvrpVlanLimitReachedEvent,
       "hpicfMvrpObjects": hpicfMvrpObjects,
       "hpicfMvrpConfig": hpicfMvrpConfig,
       "hpicfMvrpGlobalClearStats": hpicfMvrpGlobalClearStats,
       "hpicfMvrpMaxVlanLimit": hpicfMvrpMaxVlanLimit,
       "hpicfMvrpPortConfigTable": hpicfMvrpPortConfigTable,
       "hpicfMvrpPortConfigEntry": hpicfMvrpPortConfigEntry,
       "hpicfMvrpPortConfigRegistrarMode": hpicfMvrpPortConfigRegistrarMode,
       "hpicfMvrpPortConfigPeriodicTimer": hpicfMvrpPortConfigPeriodicTimer,
       "hpicfMvrpPortConfigPeriodicTransmissionStatus": hpicfMvrpPortConfigPeriodicTransmissionStatus,
       "hpicfMvrpPortStatsClearStats": hpicfMvrpPortStatsClearStats,
       "hpicfMvrpStats": hpicfMvrpStats,
       "hpicfMvrpPortStatsTable": hpicfMvrpPortStatsTable,
       "hpicfMvrpPortStatsEntry": hpicfMvrpPortStatsEntry,
       "hpicfMvrpPortStatsNewReceived": hpicfMvrpPortStatsNewReceived,
       "hpicfMvrpPortStatsJoinInReceived": hpicfMvrpPortStatsJoinInReceived,
       "hpicfMvrpPortStatsJoinEmptyReceived": hpicfMvrpPortStatsJoinEmptyReceived,
       "hpicfMvrpPortStatsLeaveReceived": hpicfMvrpPortStatsLeaveReceived,
       "hpicfMvrpPortStatsInReceived": hpicfMvrpPortStatsInReceived,
       "hpicfMvrpPortStatsEmptyReceived": hpicfMvrpPortStatsEmptyReceived,
       "hpicfMvrpPortStatsLeaveAllReceived": hpicfMvrpPortStatsLeaveAllReceived,
       "hpicfMvrpPortStatsNewTransmitted": hpicfMvrpPortStatsNewTransmitted,
       "hpicfMvrpPortStatsJoinInTransmitted": hpicfMvrpPortStatsJoinInTransmitted,
       "hpicfMvrpPortStatsJoinEmptyTransmitted": hpicfMvrpPortStatsJoinEmptyTransmitted,
       "hpicfMvrpPortStatsLeaveTransmitted": hpicfMvrpPortStatsLeaveTransmitted,
       "hpicfMvrpPortStatsInTransmitted": hpicfMvrpPortStatsInTransmitted,
       "hpicfMvrpPortStatsEmptyTransmitted": hpicfMvrpPortStatsEmptyTransmitted,
       "hpicfMvrpPortStatsLeaveAllTransmitted": hpicfMvrpPortStatsLeaveAllTransmitted,
       "hpicfMvrpPortStatsTotalPDUReceived": hpicfMvrpPortStatsTotalPDUReceived,
       "hpicfMvrpPortStatsTotalPDUTransmitted": hpicfMvrpPortStatsTotalPDUTransmitted,
       "hpicfMvrpPortStatsFramesDiscarded": hpicfMvrpPortStatsFramesDiscarded,
       "hpicfBridgeMvrpStateTable": hpicfBridgeMvrpStateTable,
       "hpicfBridgeMvrpStateEntry": hpicfBridgeMvrpStateEntry,
       "hpicfMvrpVlanId": hpicfMvrpVlanId,
       "hpicfMvrpApplicantState": hpicfMvrpApplicantState,
       "hpicfMvrpRegistrarState": hpicfMvrpRegistrarState,
       "hpicfMvrpConformance": hpicfMvrpConformance,
       "hpicfMvrpCompliances": hpicfMvrpCompliances,
       "hpicfMvrpCompliance": hpicfMvrpCompliance,
       "hpicfMvrpGroups": hpicfMvrpGroups,
       "hpicfMvrpBaseGroup": hpicfMvrpBaseGroup,
       "hpicfMvrpPortConfigGroup": hpicfMvrpPortConfigGroup,
       "hpicfMvrpPortStatsGroup": hpicfMvrpPortStatsGroup,
       "hpicfMvrpPortStateGroup": hpicfMvrpPortStateGroup,
       "hpicfMvrpNotifyGroup": hpicfMvrpNotifyGroup}
)
