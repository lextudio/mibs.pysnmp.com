# SNMP MIB module (ENTERASYS-MAC-LOCKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MAC-LOCKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:08 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysMACLockingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21)
)
etsysMACLockingMIB.setRevisions(
        ("2011-03-08 19:47",
         "2007-05-21 13:04",
         "2007-05-17 12:55",
         "2007-05-09 19:24",
         "2007-04-16 15:26",
         "2003-07-30 15:45",
         "2003-01-17 21:14",
         "2002-08-05 20:30",
         "2002-08-01 14:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysMACLockingObjects_ObjectIdentity = ObjectIdentity
etsysMACLockingObjects = _EtsysMACLockingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1)
)
_EtsysMACLockingTrapBranch_ObjectIdentity = ObjectIdentity
etsysMACLockingTrapBranch = _EtsysMACLockingTrapBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0)
)
_EtsysMACLockingSystemBranch_ObjectIdentity = ObjectIdentity
etsysMACLockingSystemBranch = _EtsysMACLockingSystemBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 1)
)


class _EtsysMACLockingSystemEnable_Type(EnabledStatus):
    """Custom type etsysMACLockingSystemEnable based on EnabledStatus"""


_EtsysMACLockingSystemEnable_Object = MibScalar
etsysMACLockingSystemEnable = _EtsysMACLockingSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 1, 1),
    _EtsysMACLockingSystemEnable_Type()
)
etsysMACLockingSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingSystemEnable.setStatus("current")
_EtsysMACLockingPortConfigBranch_ObjectIdentity = ObjectIdentity
etsysMACLockingPortConfigBranch = _EtsysMACLockingPortConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2)
)
_EtsysMACLockingPortTable_Object = MibTable
etsysMACLockingPortTable = _EtsysMACLockingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMACLockingPortTable.setStatus("current")
_EtsysMACLockingPortEntry_Object = MibTableRow
etsysMACLockingPortEntry = _EtsysMACLockingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1)
)
etsysMACLockingPortEntry.setIndexNames(
    (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"),
)
if mibBuilder.loadTexts:
    etsysMACLockingPortEntry.setStatus("current")
_EtsysMACLockingPort_Type = InterfaceIndex
_EtsysMACLockingPort_Object = MibTableColumn
etsysMACLockingPort = _EtsysMACLockingPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 1),
    _EtsysMACLockingPort_Type()
)
etsysMACLockingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMACLockingPort.setStatus("current")


class _EtsysMACLockingEnable_Type(EnabledStatus):
    """Custom type etsysMACLockingEnable based on EnabledStatus"""


_EtsysMACLockingEnable_Object = MibTableColumn
etsysMACLockingEnable = _EtsysMACLockingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 2),
    _EtsysMACLockingEnable_Type()
)
etsysMACLockingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingEnable.setStatus("current")


class _EtsysMACLockingViolationEnable_Type(EnabledStatus):
    """Custom type etsysMACLockingViolationEnable based on EnabledStatus"""


_EtsysMACLockingViolationEnable_Object = MibTableColumn
etsysMACLockingViolationEnable = _EtsysMACLockingViolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 3),
    _EtsysMACLockingViolationEnable_Type()
)
etsysMACLockingViolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingViolationEnable.setStatus("current")
_EtsysMACLockingLastViolationAddress_Type = MacAddress
_EtsysMACLockingLastViolationAddress_Object = MibTableColumn
etsysMACLockingLastViolationAddress = _EtsysMACLockingLastViolationAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 4),
    _EtsysMACLockingLastViolationAddress_Type()
)
etsysMACLockingLastViolationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACLockingLastViolationAddress.setStatus("current")
_EtsysMACLockingFirstArrivalStationsAllowed_Type = Unsigned32
_EtsysMACLockingFirstArrivalStationsAllowed_Object = MibTableColumn
etsysMACLockingFirstArrivalStationsAllowed = _EtsysMACLockingFirstArrivalStationsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 5),
    _EtsysMACLockingFirstArrivalStationsAllowed_Type()
)
etsysMACLockingFirstArrivalStationsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACLockingFirstArrivalStationsAllowed.setStatus("current")
_EtsysMACLockingFirstArrivalStationsAllocated_Type = Unsigned32
_EtsysMACLockingFirstArrivalStationsAllocated_Object = MibTableColumn
etsysMACLockingFirstArrivalStationsAllocated = _EtsysMACLockingFirstArrivalStationsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 6),
    _EtsysMACLockingFirstArrivalStationsAllocated_Type()
)
etsysMACLockingFirstArrivalStationsAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingFirstArrivalStationsAllocated.setStatus("current")
_EtsysMACLockingStaticStationsAllowed_Type = Unsigned32
_EtsysMACLockingStaticStationsAllowed_Object = MibTableColumn
etsysMACLockingStaticStationsAllowed = _EtsysMACLockingStaticStationsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 7),
    _EtsysMACLockingStaticStationsAllowed_Type()
)
etsysMACLockingStaticStationsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACLockingStaticStationsAllowed.setStatus("current")
_EtsysMACLockingStaticStationsAllocated_Type = Unsigned32
_EtsysMACLockingStaticStationsAllocated_Object = MibTableColumn
etsysMACLockingStaticStationsAllocated = _EtsysMACLockingStaticStationsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 8),
    _EtsysMACLockingStaticStationsAllocated_Type()
)
etsysMACLockingStaticStationsAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingStaticStationsAllocated.setStatus("current")
_EtsysMACLockingMoveFirstArrivalToStatic_Type = TruthValue
_EtsysMACLockingMoveFirstArrivalToStatic_Object = MibTableColumn
etsysMACLockingMoveFirstArrivalToStatic = _EtsysMACLockingMoveFirstArrivalToStatic_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 9),
    _EtsysMACLockingMoveFirstArrivalToStatic_Type()
)
etsysMACLockingMoveFirstArrivalToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingMoveFirstArrivalToStatic.setStatus("current")
_EtsysMACLockingStaticStationsCount_Type = Unsigned32
_EtsysMACLockingStaticStationsCount_Object = MibTableColumn
etsysMACLockingStaticStationsCount = _EtsysMACLockingStaticStationsCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 10),
    _EtsysMACLockingStaticStationsCount_Type()
)
etsysMACLockingStaticStationsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACLockingStaticStationsCount.setStatus("current")
_EtsysMACLockingClearStaticStations_Type = TruthValue
_EtsysMACLockingClearStaticStations_Object = MibTableColumn
etsysMACLockingClearStaticStations = _EtsysMACLockingClearStaticStations_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 11),
    _EtsysMACLockingClearStaticStations_Type()
)
etsysMACLockingClearStaticStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingClearStaticStations.setStatus("current")
_EtsysMACLockingFirstArrivalAging_Type = TruthValue
_EtsysMACLockingFirstArrivalAging_Object = MibTableColumn
etsysMACLockingFirstArrivalAging = _EtsysMACLockingFirstArrivalAging_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 12),
    _EtsysMACLockingFirstArrivalAging_Type()
)
etsysMACLockingFirstArrivalAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingFirstArrivalAging.setStatus("current")


class _EtsysMACLockingViolationSyslogEnable_Type(EnabledStatus):
    """Custom type etsysMACLockingViolationSyslogEnable based on EnabledStatus"""


_EtsysMACLockingViolationSyslogEnable_Object = MibTableColumn
etsysMACLockingViolationSyslogEnable = _EtsysMACLockingViolationSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 13),
    _EtsysMACLockingViolationSyslogEnable_Type()
)
etsysMACLockingViolationSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingViolationSyslogEnable.setStatus("current")


class _EtsysMACLockingThresholdEnable_Type(EnabledStatus):
    """Custom type etsysMACLockingThresholdEnable based on EnabledStatus"""


_EtsysMACLockingThresholdEnable_Object = MibTableColumn
etsysMACLockingThresholdEnable = _EtsysMACLockingThresholdEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 14),
    _EtsysMACLockingThresholdEnable_Type()
)
etsysMACLockingThresholdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingThresholdEnable.setStatus("current")


class _EtsysMACLockingThresholdSyslogEnable_Type(EnabledStatus):
    """Custom type etsysMACLockingThresholdSyslogEnable based on EnabledStatus"""


_EtsysMACLockingThresholdSyslogEnable_Object = MibTableColumn
etsysMACLockingThresholdSyslogEnable = _EtsysMACLockingThresholdSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 15),
    _EtsysMACLockingThresholdSyslogEnable_Type()
)
etsysMACLockingThresholdSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingThresholdSyslogEnable.setStatus("current")
_EtsysMACLockingStaticStationBranch_ObjectIdentity = ObjectIdentity
etsysMACLockingStaticStationBranch = _EtsysMACLockingStaticStationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3)
)
_EtsysMACLockingStaticStationTable_Object = MibTable
etsysMACLockingStaticStationTable = _EtsysMACLockingStaticStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMACLockingStaticStationTable.setStatus("current")
_EtsysMACLockingStaticStationEntry_Object = MibTableRow
etsysMACLockingStaticStationEntry = _EtsysMACLockingStaticStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1)
)
etsysMACLockingStaticStationEntry.setIndexNames(
    (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"),
    (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedAddress"),
)
if mibBuilder.loadTexts:
    etsysMACLockingStaticStationEntry.setStatus("current")
_EtsysMACLockingLockedAddress_Type = MacAddress
_EtsysMACLockingLockedAddress_Object = MibTableColumn
etsysMACLockingLockedAddress = _EtsysMACLockingLockedAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1, 1),
    _EtsysMACLockingLockedAddress_Type()
)
etsysMACLockingLockedAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMACLockingLockedAddress.setStatus("current")
_EtsysMACLockingStaticEntryRowStatus_Type = RowStatus
_EtsysMACLockingStaticEntryRowStatus_Object = MibTableColumn
etsysMACLockingStaticEntryRowStatus = _EtsysMACLockingStaticEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1, 2),
    _EtsysMACLockingStaticEntryRowStatus_Type()
)
etsysMACLockingStaticEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMACLockingStaticEntryRowStatus.setStatus("current")
_EtsysMACLockingStationBranch_ObjectIdentity = ObjectIdentity
etsysMACLockingStationBranch = _EtsysMACLockingStationBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4)
)
_EtsysMACLockingStationTable_Object = MibTable
etsysMACLockingStationTable = _EtsysMACLockingStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMACLockingStationTable.setStatus("current")
_EtsysMACLockingStationEntry_Object = MibTableRow
etsysMACLockingStationEntry = _EtsysMACLockingStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1)
)
etsysMACLockingStationEntry.setIndexNames(
    (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"),
    (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedAddress"),
)
if mibBuilder.loadTexts:
    etsysMACLockingStationEntry.setStatus("current")


class _EtsysMACLockingLockedEntryCause_Type(Integer32):
    """Custom type etsysMACLockingLockedEntryCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agingFirstArrival", 3),
          ("firstArrival", 2),
          ("static", 1))
    )


_EtsysMACLockingLockedEntryCause_Type.__name__ = "Integer32"
_EtsysMACLockingLockedEntryCause_Object = MibTableColumn
etsysMACLockingLockedEntryCause = _EtsysMACLockingLockedEntryCause_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1, 1),
    _EtsysMACLockingLockedEntryCause_Type()
)
etsysMACLockingLockedEntryCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMACLockingLockedEntryCause.setStatus("current")


class _EtsysMACLockingRemoveStation_Type(TruthValue):
    """Custom type etsysMACLockingRemoveStation based on TruthValue"""


_EtsysMACLockingRemoveStation_Object = MibTableColumn
etsysMACLockingRemoveStation = _EtsysMACLockingRemoveStation_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1, 2),
    _EtsysMACLockingRemoveStation_Type()
)
etsysMACLockingRemoveStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMACLockingRemoveStation.setStatus("current")
_EtsysMACLockingConformance_ObjectIdentity = ObjectIdentity
etsysMACLockingConformance = _EtsysMACLockingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2)
)
_EtsysMACLockingGroups_ObjectIdentity = ObjectIdentity
etsysMACLockingGroups = _EtsysMACLockingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1)
)
_EtsysMACLockingCompliances_ObjectIdentity = ObjectIdentity
etsysMACLockingCompliances = _EtsysMACLockingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2)
)

# Managed Objects groups

etsysMACLockingSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 1)
)
etsysMACLockingSystemGroup.setObjects(
    ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingSystemEnable")
)
if mibBuilder.loadTexts:
    etsysMACLockingSystemGroup.setStatus("current")

etsysMACLockingPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 2)
)
etsysMACLockingPortGroup.setObjects(
      *(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingEnable"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingViolationEnable"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLastViolationAddress"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllowed"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllocated"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsAllowed"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsAllocated"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMoveFirstArrivalToStatic"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsCount"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingClearStaticStations"))
)
if mibBuilder.loadTexts:
    etsysMACLockingPortGroup.setStatus("current")

etsysMACLockingStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 3)
)
etsysMACLockingStationGroup.setObjects(
    ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedEntryCause")
)
if mibBuilder.loadTexts:
    etsysMACLockingStationGroup.setStatus("deprecated")

etsysMACLockingStaticStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 4)
)
etsysMACLockingStaticStationGroup.setObjects(
    ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticEntryRowStatus")
)
if mibBuilder.loadTexts:
    etsysMACLockingStaticStationGroup.setStatus("current")

etsysMACLockingPortFirstArrivalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 5)
)
etsysMACLockingPortFirstArrivalGroup.setObjects(
    ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalAging")
)
if mibBuilder.loadTexts:
    etsysMACLockingPortFirstArrivalGroup.setStatus("current")

etsysMACLockingStationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 6)
)
etsysMACLockingStationGroup2.setObjects(
      *(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedEntryCause"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingRemoveStation"))
)
if mibBuilder.loadTexts:
    etsysMACLockingStationGroup2.setStatus("current")

etsysMACLockingPortMessageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 8)
)
etsysMACLockingPortMessageGroup.setObjects(
      *(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingViolationSyslogEnable"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingThresholdEnable"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingThresholdSyslogEnable"))
)
if mibBuilder.loadTexts:
    etsysMACLockingPortMessageGroup.setStatus("current")


# Notification objects

etsysMACLockingMACViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0, 1)
)
etsysMACLockingMACViolation.setObjects(
    ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLastViolationAddress")
)
if mibBuilder.loadTexts:
    etsysMACLockingMACViolation.setStatus(
        "current"
    )

etsysMACLockingMACThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0, 2)
)
etsysMACLockingMACThreshold.setObjects(
    ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllocated")
)
if mibBuilder.loadTexts:
    etsysMACLockingMACThreshold.setStatus(
        "current"
    )


# Notifications groups

etsysMACLockingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 7)
)
etsysMACLockingNotificationGroup.setObjects(
      *(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMACViolation"),
        ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMACThreshold"))
)
if mibBuilder.loadTexts:
    etsysMACLockingNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysMACLockingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMACLockingCompliance.setStatus(
        "deprecated"
    )

etsysMACLockingNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    etsysMACLockingNotificationCompliance.setStatus(
        "current"
    )

etsysMACLockingPortFirstArrivalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMACLockingPortFirstArrivalCompliance.setStatus(
        "current"
    )

etsysMACLockingCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 3)
)
if mibBuilder.loadTexts:
    etsysMACLockingCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MAC-LOCKING-MIB",
    **{"etsysMACLockingMIB": etsysMACLockingMIB,
       "etsysMACLockingObjects": etsysMACLockingObjects,
       "etsysMACLockingTrapBranch": etsysMACLockingTrapBranch,
       "etsysMACLockingMACViolation": etsysMACLockingMACViolation,
       "etsysMACLockingMACThreshold": etsysMACLockingMACThreshold,
       "etsysMACLockingSystemBranch": etsysMACLockingSystemBranch,
       "etsysMACLockingSystemEnable": etsysMACLockingSystemEnable,
       "etsysMACLockingPortConfigBranch": etsysMACLockingPortConfigBranch,
       "etsysMACLockingPortTable": etsysMACLockingPortTable,
       "etsysMACLockingPortEntry": etsysMACLockingPortEntry,
       "etsysMACLockingPort": etsysMACLockingPort,
       "etsysMACLockingEnable": etsysMACLockingEnable,
       "etsysMACLockingViolationEnable": etsysMACLockingViolationEnable,
       "etsysMACLockingLastViolationAddress": etsysMACLockingLastViolationAddress,
       "etsysMACLockingFirstArrivalStationsAllowed": etsysMACLockingFirstArrivalStationsAllowed,
       "etsysMACLockingFirstArrivalStationsAllocated": etsysMACLockingFirstArrivalStationsAllocated,
       "etsysMACLockingStaticStationsAllowed": etsysMACLockingStaticStationsAllowed,
       "etsysMACLockingStaticStationsAllocated": etsysMACLockingStaticStationsAllocated,
       "etsysMACLockingMoveFirstArrivalToStatic": etsysMACLockingMoveFirstArrivalToStatic,
       "etsysMACLockingStaticStationsCount": etsysMACLockingStaticStationsCount,
       "etsysMACLockingClearStaticStations": etsysMACLockingClearStaticStations,
       "etsysMACLockingFirstArrivalAging": etsysMACLockingFirstArrivalAging,
       "etsysMACLockingViolationSyslogEnable": etsysMACLockingViolationSyslogEnable,
       "etsysMACLockingThresholdEnable": etsysMACLockingThresholdEnable,
       "etsysMACLockingThresholdSyslogEnable": etsysMACLockingThresholdSyslogEnable,
       "etsysMACLockingStaticStationBranch": etsysMACLockingStaticStationBranch,
       "etsysMACLockingStaticStationTable": etsysMACLockingStaticStationTable,
       "etsysMACLockingStaticStationEntry": etsysMACLockingStaticStationEntry,
       "etsysMACLockingLockedAddress": etsysMACLockingLockedAddress,
       "etsysMACLockingStaticEntryRowStatus": etsysMACLockingStaticEntryRowStatus,
       "etsysMACLockingStationBranch": etsysMACLockingStationBranch,
       "etsysMACLockingStationTable": etsysMACLockingStationTable,
       "etsysMACLockingStationEntry": etsysMACLockingStationEntry,
       "etsysMACLockingLockedEntryCause": etsysMACLockingLockedEntryCause,
       "etsysMACLockingRemoveStation": etsysMACLockingRemoveStation,
       "etsysMACLockingConformance": etsysMACLockingConformance,
       "etsysMACLockingGroups": etsysMACLockingGroups,
       "etsysMACLockingSystemGroup": etsysMACLockingSystemGroup,
       "etsysMACLockingPortGroup": etsysMACLockingPortGroup,
       "etsysMACLockingStationGroup": etsysMACLockingStationGroup,
       "etsysMACLockingStaticStationGroup": etsysMACLockingStaticStationGroup,
       "etsysMACLockingPortFirstArrivalGroup": etsysMACLockingPortFirstArrivalGroup,
       "etsysMACLockingStationGroup2": etsysMACLockingStationGroup2,
       "etsysMACLockingNotificationGroup": etsysMACLockingNotificationGroup,
       "etsysMACLockingPortMessageGroup": etsysMACLockingPortMessageGroup,
       "etsysMACLockingCompliances": etsysMACLockingCompliances,
       "etsysMACLockingCompliance": etsysMACLockingCompliance,
       "etsysMACLockingNotificationCompliance": etsysMACLockingNotificationCompliance,
       "etsysMACLockingPortFirstArrivalCompliance": etsysMACLockingPortFirstArrivalCompliance,
       "etsysMACLockingCompliance2": etsysMACLockingCompliance2}
)
