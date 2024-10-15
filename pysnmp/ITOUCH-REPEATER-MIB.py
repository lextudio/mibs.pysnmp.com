# SNMP MIB module (ITOUCH-REPEATER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-REPEATER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:21 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(TypedAddress,
 iTouch) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "TypedAddress",
    "iTouch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Segment(Integer32):
    """Custom type Segment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("disabled", 27),
          ("e", 5),
          ("f", 6),
          ("g", 7),
          ("h", 8),
          ("i", 9),
          ("j", 10),
          ("k", 11),
          ("l", 12),
          ("m", 13),
          ("n", 14),
          ("notApplicable", 28),
          ("o", 15),
          ("p", 16),
          ("q", 17),
          ("r", 18),
          ("s", 19),
          ("t", 20),
          ("u", 21),
          ("v", 22),
          ("w", 23),
          ("x", 24),
          ("y", 25),
          ("z", 26))
    )





class Repeater(Integer32):
    """Custom type Repeater based on Integer32"""
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
        *(("notApplicable", 1),
          ("repeater1", 2),
          ("repeater2", 3),
          ("repeater3", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HubDeprecated_ObjectIdentity = ObjectIdentity
hubDeprecated = _HubDeprecated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 9)
)
_XRepeater_ObjectIdentity = ObjectIdentity
xRepeater = _XRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17)
)
_XRepeaterInfo_ObjectIdentity = ObjectIdentity
xRepeaterInfo = _XRepeaterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17, 1)
)


class _RepeaterAccessViolation_Type(Integer32):
    """Custom type repeaterAccessViolation based on Integer32"""
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
        *(("both", 1),
          ("disable", 2),
          ("trap", 3))
    )


_RepeaterAccessViolation_Type.__name__ = "Integer32"
_RepeaterAccessViolation_Object = MibScalar
repeaterAccessViolation = _RepeaterAccessViolation_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 1),
    _RepeaterAccessViolation_Type()
)
repeaterAccessViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterAccessViolation.setStatus("mandatory")
_RepeaterMyGroup_Type = Integer32
_RepeaterMyGroup_Object = MibScalar
repeaterMyGroup = _RepeaterMyGroup_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 2),
    _RepeaterMyGroup_Type()
)
repeaterMyGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterMyGroup.setStatus("mandatory")
_RepeaterFifoOverflows_Type = Counter32
_RepeaterFifoOverflows_Object = MibScalar
repeaterFifoOverflows = _RepeaterFifoOverflows_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 3),
    _RepeaterFifoOverflows_Type()
)
repeaterFifoOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterFifoOverflows.setStatus("deprecated")


class _RepeaterLEDDisplay_Type(Integer32):
    """Custom type repeaterLEDDisplay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activity", 1),
          ("collisions", 2))
    )


_RepeaterLEDDisplay_Type.__name__ = "Integer32"
_RepeaterLEDDisplay_Object = MibScalar
repeaterLEDDisplay = _RepeaterLEDDisplay_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 4),
    _RepeaterLEDDisplay_Type()
)
repeaterLEDDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterLEDDisplay.setStatus("mandatory")


class _RepeaterReports_Type(Integer32):
    """Custom type repeaterReports based on Integer32"""
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


_RepeaterReports_Type.__name__ = "Integer32"
_RepeaterReports_Object = MibScalar
repeaterReports = _RepeaterReports_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 5),
    _RepeaterReports_Type()
)
repeaterReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterReports.setStatus("deprecated")


class _RepeaterHealthTrap_Type(Integer32):
    """Custom type repeaterHealthTrap based on Integer32"""
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


_RepeaterHealthTrap_Type.__name__ = "Integer32"
_RepeaterHealthTrap_Object = MibScalar
repeaterHealthTrap = _RepeaterHealthTrap_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 6),
    _RepeaterHealthTrap_Type()
)
repeaterHealthTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterHealthTrap.setStatus("mandatory")


class _RepeaterStatusChangeTrap_Type(Integer32):
    """Custom type repeaterStatusChangeTrap based on Integer32"""
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


_RepeaterStatusChangeTrap_Type.__name__ = "Integer32"
_RepeaterStatusChangeTrap_Object = MibScalar
repeaterStatusChangeTrap = _RepeaterStatusChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 7),
    _RepeaterStatusChangeTrap_Type()
)
repeaterStatusChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterStatusChangeTrap.setStatus("mandatory")


class _RepeaterAccessViolationTrap_Type(Integer32):
    """Custom type repeaterAccessViolationTrap based on Integer32"""
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


_RepeaterAccessViolationTrap_Type.__name__ = "Integer32"
_RepeaterAccessViolationTrap_Object = MibScalar
repeaterAccessViolationTrap = _RepeaterAccessViolationTrap_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 8),
    _RepeaterAccessViolationTrap_Type()
)
repeaterAccessViolationTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterAccessViolationTrap.setStatus("mandatory")


class _RepeaterIntegrityLossTrap_Type(Integer32):
    """Custom type repeaterIntegrityLossTrap based on Integer32"""
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


_RepeaterIntegrityLossTrap_Type.__name__ = "Integer32"
_RepeaterIntegrityLossTrap_Object = MibScalar
repeaterIntegrityLossTrap = _RepeaterIntegrityLossTrap_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 9),
    _RepeaterIntegrityLossTrap_Type()
)
repeaterIntegrityLossTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterIntegrityLossTrap.setStatus("mandatory")


class _RepeaterRedundancyPathChangeTrap_Type(Integer32):
    """Custom type repeaterRedundancyPathChangeTrap based on Integer32"""
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


_RepeaterRedundancyPathChangeTrap_Type.__name__ = "Integer32"
_RepeaterRedundancyPathChangeTrap_Object = MibScalar
repeaterRedundancyPathChangeTrap = _RepeaterRedundancyPathChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 1, 10),
    _RepeaterRedundancyPathChangeTrap_Type()
)
repeaterRedundancyPathChangeTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathChangeTrap.setStatus("mandatory")
_XRepeaterGroupInfo_ObjectIdentity = ObjectIdentity
xRepeaterGroupInfo = _XRepeaterGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17, 2)
)
_RepeaterGroupTable_Object = MibTable
repeaterGroupTable = _RepeaterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1)
)
if mibBuilder.loadTexts:
    repeaterGroupTable.setStatus("mandatory")
_RepeaterGroupEntry_Object = MibTableRow
repeaterGroupEntry = _RepeaterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1)
)
repeaterGroupEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterGroupIndex"),
)
if mibBuilder.loadTexts:
    repeaterGroupEntry.setStatus("mandatory")
_RepeaterGroupIndex_Type = Integer32
_RepeaterGroupIndex_Object = MibTableColumn
repeaterGroupIndex = _RepeaterGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 1),
    _RepeaterGroupIndex_Type()
)
repeaterGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupIndex.setStatus("mandatory")
_RepeaterGroupSQE_Type = Counter32
_RepeaterGroupSQE_Object = MibTableColumn
repeaterGroupSQE = _RepeaterGroupSQE_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 2),
    _RepeaterGroupSQE_Type()
)
repeaterGroupSQE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupSQE.setStatus("deprecated")
_RepeaterGroupJabbers_Type = Counter32
_RepeaterGroupJabbers_Object = MibTableColumn
repeaterGroupJabbers = _RepeaterGroupJabbers_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 3),
    _RepeaterGroupJabbers_Type()
)
repeaterGroupJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupJabbers.setStatus("deprecated")
_RepeaterGroupSegment_Type = Segment
_RepeaterGroupSegment_Object = MibTableColumn
repeaterGroupSegment = _RepeaterGroupSegment_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 4),
    _RepeaterGroupSegment_Type()
)
repeaterGroupSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterGroupSegment.setStatus("deprecated")


class _RepeaterGroupSecurityLock_Type(Integer32):
    """Custom type repeaterGroupSecurityLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_RepeaterGroupSecurityLock_Type.__name__ = "Integer32"
_RepeaterGroupSecurityLock_Object = MibTableColumn
repeaterGroupSecurityLock = _RepeaterGroupSecurityLock_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 5),
    _RepeaterGroupSecurityLock_Type()
)
repeaterGroupSecurityLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterGroupSecurityLock.setStatus("mandatory")
_RepeaterGroupIOCardType_Type = Integer32
_RepeaterGroupIOCardType_Object = MibTableColumn
repeaterGroupIOCardType = _RepeaterGroupIOCardType_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 6),
    _RepeaterGroupIOCardType_Type()
)
repeaterGroupIOCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupIOCardType.setStatus("mandatory")
_RepeaterGroupIOCardFirmwareVersion_Type = Integer32
_RepeaterGroupIOCardFirmwareVersion_Object = MibTableColumn
repeaterGroupIOCardFirmwareVersion = _RepeaterGroupIOCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 7),
    _RepeaterGroupIOCardFirmwareVersion_Type()
)
repeaterGroupIOCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupIOCardFirmwareVersion.setStatus("mandatory")


class _RepeaterGroupIOCardOperStatus_Type(Integer32):
    """Custom type repeaterGroupIOCardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("attended", 9),
          ("dumpRequested", 3),
          ("dumping", 4),
          ("inhibited", 12),
          ("initializing", 8),
          ("internal10", 10),
          ("internal11", 11),
          ("invalidConfigStorage", 14),
          ("loadRequested", 1),
          ("loading", 2),
          ("maxserverCard", 13),
          ("paramLoading", 6),
          ("paramRequested", 5),
          ("running", 7),
          ("securityLockdown", 15))
    )


_RepeaterGroupIOCardOperStatus_Type.__name__ = "Integer32"
_RepeaterGroupIOCardOperStatus_Object = MibTableColumn
repeaterGroupIOCardOperStatus = _RepeaterGroupIOCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 8),
    _RepeaterGroupIOCardOperStatus_Type()
)
repeaterGroupIOCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupIOCardOperStatus.setStatus("mandatory")


class _RepeaterGroupManagement_Type(Integer32):
    """Custom type repeaterGroupManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("minimal", 1))
    )


_RepeaterGroupManagement_Type.__name__ = "Integer32"
_RepeaterGroupManagement_Object = MibTableColumn
repeaterGroupManagement = _RepeaterGroupManagement_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 9),
    _RepeaterGroupManagement_Type()
)
repeaterGroupManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupManagement.setStatus("mandatory")
_RepeaterGroupRepeaterNumber_Type = Integer32
_RepeaterGroupRepeaterNumber_Object = MibTableColumn
repeaterGroupRepeaterNumber = _RepeaterGroupRepeaterNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 10),
    _RepeaterGroupRepeaterNumber_Type()
)
repeaterGroupRepeaterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupRepeaterNumber.setStatus("mandatory")
_RepeaterGroupRepeaterHardwareVersion_Type = Integer32
_RepeaterGroupRepeaterHardwareVersion_Object = MibTableColumn
repeaterGroupRepeaterHardwareVersion = _RepeaterGroupRepeaterHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 11),
    _RepeaterGroupRepeaterHardwareVersion_Type()
)
repeaterGroupRepeaterHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupRepeaterHardwareVersion.setStatus("mandatory")
_RepeaterGroupManagerRepeater_Type = Repeater
_RepeaterGroupManagerRepeater_Object = MibTableColumn
repeaterGroupManagerRepeater = _RepeaterGroupManagerRepeater_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 12),
    _RepeaterGroupManagerRepeater_Type()
)
repeaterGroupManagerRepeater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterGroupManagerRepeater.setStatus("mandatory")
_RepeaterGroupFifoErrors_Type = Counter32
_RepeaterGroupFifoErrors_Object = MibTableColumn
repeaterGroupFifoErrors = _RepeaterGroupFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 13),
    _RepeaterGroupFifoErrors_Type()
)
repeaterGroupFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupFifoErrors.setStatus("mandatory")


class _RepeaterGroupCpuUtilization_Type(Integer32):
    """Custom type repeaterGroupCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterGroupCpuUtilization_Type.__name__ = "Integer32"
_RepeaterGroupCpuUtilization_Object = MibTableColumn
repeaterGroupCpuUtilization = _RepeaterGroupCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 14),
    _RepeaterGroupCpuUtilization_Type()
)
repeaterGroupCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupCpuUtilization.setStatus("mandatory")


class _RepeaterGroupMemoryUtilization_Type(Integer32):
    """Custom type repeaterGroupMemoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterGroupMemoryUtilization_Type.__name__ = "Integer32"
_RepeaterGroupMemoryUtilization_Object = MibTableColumn
repeaterGroupMemoryUtilization = _RepeaterGroupMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 15),
    _RepeaterGroupMemoryUtilization_Type()
)
repeaterGroupMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupMemoryUtilization.setStatus("mandatory")
_RepeaterGroupAlarmCount_Type = Integer32
_RepeaterGroupAlarmCount_Object = MibTableColumn
repeaterGroupAlarmCount = _RepeaterGroupAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 2, 1, 1, 16),
    _RepeaterGroupAlarmCount_Type()
)
repeaterGroupAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterGroupAlarmCount.setStatus("mandatory")
_XRepeaterPortInfo_ObjectIdentity = ObjectIdentity
xRepeaterPortInfo = _XRepeaterPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17, 3)
)
_RepeaterPortTable_Object = MibTable
repeaterPortTable = _RepeaterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1)
)
if mibBuilder.loadTexts:
    repeaterPortTable.setStatus("mandatory")
_RepeaterPortEntry_Object = MibTableRow
repeaterPortEntry = _RepeaterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1)
)
repeaterPortEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortIndex"),
)
if mibBuilder.loadTexts:
    repeaterPortEntry.setStatus("mandatory")
_RepeaterPortGroupIndex_Type = Integer32
_RepeaterPortGroupIndex_Object = MibTableColumn
repeaterPortGroupIndex = _RepeaterPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 1),
    _RepeaterPortGroupIndex_Type()
)
repeaterPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortGroupIndex.setStatus("mandatory")
_RepeaterPortIndex_Type = Integer32
_RepeaterPortIndex_Object = MibTableColumn
repeaterPortIndex = _RepeaterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 2),
    _RepeaterPortIndex_Type()
)
repeaterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortIndex.setStatus("mandatory")


class _RepeaterPortName_Type(DisplayString):
    """Custom type repeaterPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RepeaterPortName_Type.__name__ = "DisplayString"
_RepeaterPortName_Object = MibTableColumn
repeaterPortName = _RepeaterPortName_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 3),
    _RepeaterPortName_Type()
)
repeaterPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortName.setStatus("mandatory")


class _RepeaterPortAutoPolarity_Type(Integer32):
    """Custom type repeaterPortAutoPolarity based on Integer32"""
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


_RepeaterPortAutoPolarity_Type.__name__ = "Integer32"
_RepeaterPortAutoPolarity_Object = MibTableColumn
repeaterPortAutoPolarity = _RepeaterPortAutoPolarity_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 4),
    _RepeaterPortAutoPolarity_Type()
)
repeaterPortAutoPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAutoPolarity.setStatus("mandatory")


class _RepeaterPortPolarityDirection_Type(Integer32):
    """Custom type repeaterPortPolarityDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("reversed", 1),
          ("unknown", 3))
    )


_RepeaterPortPolarityDirection_Type.__name__ = "Integer32"
_RepeaterPortPolarityDirection_Object = MibTableColumn
repeaterPortPolarityDirection = _RepeaterPortPolarityDirection_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 5),
    _RepeaterPortPolarityDirection_Type()
)
repeaterPortPolarityDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortPolarityDirection.setStatus("mandatory")


class _RepeaterPortPulse_Type(Integer32):
    """Custom type repeaterPortPulse based on Integer32"""
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


_RepeaterPortPulse_Type.__name__ = "Integer32"
_RepeaterPortPulse_Object = MibTableColumn
repeaterPortPulse = _RepeaterPortPulse_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 6),
    _RepeaterPortPulse_Type()
)
repeaterPortPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortPulse.setStatus("mandatory")


class _RepeaterPortPulseStatus_Type(Integer32):
    """Custom type repeaterPortPulseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 2),
          ("notDetected", 1))
    )


_RepeaterPortPulseStatus_Type.__name__ = "Integer32"
_RepeaterPortPulseStatus_Object = MibTableColumn
repeaterPortPulseStatus = _RepeaterPortPulseStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 7),
    _RepeaterPortPulseStatus_Type()
)
repeaterPortPulseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortPulseStatus.setStatus("mandatory")
_RepeaterPortPulseLosses_Type = Counter32
_RepeaterPortPulseLosses_Object = MibTableColumn
repeaterPortPulseLosses = _RepeaterPortPulseLosses_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 8),
    _RepeaterPortPulseLosses_Type()
)
repeaterPortPulseLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortPulseLosses.setStatus("mandatory")


class _RepeaterPortDistance_Type(Integer32):
    """Custom type repeaterPortDistance based on Integer32"""
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


_RepeaterPortDistance_Type.__name__ = "Integer32"
_RepeaterPortDistance_Object = MibTableColumn
repeaterPortDistance = _RepeaterPortDistance_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 9),
    _RepeaterPortDistance_Type()
)
repeaterPortDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortDistance.setStatus("mandatory")
_RepeaterPortSofMissing_Type = Counter32
_RepeaterPortSofMissing_Object = MibTableColumn
repeaterPortSofMissing = _RepeaterPortSofMissing_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 10),
    _RepeaterPortSofMissing_Type()
)
repeaterPortSofMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortSofMissing.setStatus("mandatory")
_RepeaterPortMCVs_Type = Counter32
_RepeaterPortMCVs_Object = MibTableColumn
repeaterPortMCVs = _RepeaterPortMCVs_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 11),
    _RepeaterPortMCVs_Type()
)
repeaterPortMCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortMCVs.setStatus("mandatory")


class _RepeaterPortZero_Type(Integer32):
    """Custom type repeaterPortZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_RepeaterPortZero_Type.__name__ = "Integer32"
_RepeaterPortZero_Object = MibTableColumn
repeaterPortZero = _RepeaterPortZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 12),
    _RepeaterPortZero_Type()
)
repeaterPortZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortZero.setStatus("mandatory")
_RepeaterPortSinceZero_Type = TimeTicks
_RepeaterPortSinceZero_Object = MibTableColumn
repeaterPortSinceZero = _RepeaterPortSinceZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 13),
    _RepeaterPortSinceZero_Type()
)
repeaterPortSinceZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortSinceZero.setStatus("mandatory")


class _RepeaterPortAccessAction_Type(Integer32):
    """Custom type repeaterPortAccessAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_RepeaterPortAccessAction_Type.__name__ = "Integer32"
_RepeaterPortAccessAction_Object = MibTableColumn
repeaterPortAccessAction = _RepeaterPortAccessAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 14),
    _RepeaterPortAccessAction_Type()
)
repeaterPortAccessAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessAction.setStatus("mandatory")


class _RepeaterPortAccessState_Type(Integer32):
    """Custom type repeaterPortAccessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("notDisabled", 2))
    )


_RepeaterPortAccessState_Type.__name__ = "Integer32"
_RepeaterPortAccessState_Object = MibTableColumn
repeaterPortAccessState = _RepeaterPortAccessState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 15),
    _RepeaterPortAccessState_Type()
)
repeaterPortAccessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortAccessState.setStatus("mandatory")


class _RepeaterPortAccessType_Type(Integer32):
    """Custom type repeaterPortAccessType based on Integer32"""
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
        *(("aui", 2),
          ("foirl", 3),
          ("lanbus", 5),
          ("mac", 4),
          ("tenBase2", 6),
          ("tenBaseFL", 7),
          ("tenBaseT", 1))
    )


_RepeaterPortAccessType_Type.__name__ = "Integer32"
_RepeaterPortAccessType_Object = MibTableColumn
repeaterPortAccessType = _RepeaterPortAccessType_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 16),
    _RepeaterPortAccessType_Type()
)
repeaterPortAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortAccessType.setStatus("mandatory")


class _RepeaterPortAccessAllStatus_Type(Integer32):
    """Custom type repeaterPortAccessAllStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterPortAccessAllStatus_Type.__name__ = "Integer32"
_RepeaterPortAccessAllStatus_Object = MibTableColumn
repeaterPortAccessAllStatus = _RepeaterPortAccessAllStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 17),
    _RepeaterPortAccessAllStatus_Type()
)
repeaterPortAccessAllStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessAllStatus.setStatus("mandatory")
_RepeaterPortPortLastViolationAddress_Type = MacAddress
_RepeaterPortPortLastViolationAddress_Object = MibTableColumn
repeaterPortPortLastViolationAddress = _RepeaterPortPortLastViolationAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 18),
    _RepeaterPortPortLastViolationAddress_Type()
)
repeaterPortPortLastViolationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortPortLastViolationAddress.setStatus("mandatory")
_RepeaterPortPortAddressViolations_Type = Counter32
_RepeaterPortPortAddressViolations_Object = MibTableColumn
repeaterPortPortAddressViolations = _RepeaterPortPortAddressViolations_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 19),
    _RepeaterPortPortAddressViolations_Type()
)
repeaterPortPortAddressViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortPortAddressViolations.setStatus("mandatory")
_RepeaterPortSegment_Type = Segment
_RepeaterPortSegment_Object = MibTableColumn
repeaterPortSegment = _RepeaterPortSegment_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 20),
    _RepeaterPortSegment_Type()
)
repeaterPortSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortSegment.setStatus("mandatory")


class _RepeaterPortAccessLearn_Type(Integer32):
    """Custom type repeaterPortAccessLearn based on Integer32"""
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
        *(("continuous", 3),
          ("disabled", 1),
          ("single", 2))
    )


_RepeaterPortAccessLearn_Type.__name__ = "Integer32"
_RepeaterPortAccessLearn_Object = MibTableColumn
repeaterPortAccessLearn = _RepeaterPortAccessLearn_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 21),
    _RepeaterPortAccessLearn_Type()
)
repeaterPortAccessLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessLearn.setStatus("mandatory")


class _RepeaterPortEthernetRepeater_Type(Integer32):
    """Custom type repeaterPortEthernetRepeater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("repeater1", 1),
          ("repeater2", 2),
          ("repeater3", 3))
    )


_RepeaterPortEthernetRepeater_Type.__name__ = "Integer32"
_RepeaterPortEthernetRepeater_Object = MibTableColumn
repeaterPortEthernetRepeater = _RepeaterPortEthernetRepeater_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 22),
    _RepeaterPortEthernetRepeater_Type()
)
repeaterPortEthernetRepeater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortEthernetRepeater.setStatus("mandatory")
_RepeaterPortRepeatersAllowed_Type = OctetString
_RepeaterPortRepeatersAllowed_Object = MibTableColumn
repeaterPortRepeatersAllowed = _RepeaterPortRepeatersAllowed_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 23),
    _RepeaterPortRepeatersAllowed_Type()
)
repeaterPortRepeatersAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortRepeatersAllowed.setStatus("mandatory")
_RepeaterPortGlobalSecurityAddress_Type = MacAddress
_RepeaterPortGlobalSecurityAddress_Object = MibTableColumn
repeaterPortGlobalSecurityAddress = _RepeaterPortGlobalSecurityAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 24),
    _RepeaterPortGlobalSecurityAddress_Type()
)
repeaterPortGlobalSecurityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortGlobalSecurityAddress.setStatus("mandatory")
_RepeaterPortGlobalAddressChanges_Type = Counter32
_RepeaterPortGlobalAddressChanges_Object = MibTableColumn
repeaterPortGlobalAddressChanges = _RepeaterPortGlobalAddressChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 25),
    _RepeaterPortGlobalAddressChanges_Type()
)
repeaterPortGlobalAddressChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortGlobalAddressChanges.setStatus("mandatory")
_RepeaterPortPercentUtilization_Type = Gauge32
_RepeaterPortPercentUtilization_Object = MibTableColumn
repeaterPortPercentUtilization = _RepeaterPortPercentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 1, 1, 26),
    _RepeaterPortPercentUtilization_Type()
)
repeaterPortPercentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortPercentUtilization.setStatus("mandatory")
_RepeaterPortAccessTable_Object = MibTable
repeaterPortAccessTable = _RepeaterPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 2)
)
if mibBuilder.loadTexts:
    repeaterPortAccessTable.setStatus("mandatory")
_RepeaterPortAccessEntry_Object = MibTableRow
repeaterPortAccessEntry = _RepeaterPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 2, 1)
)
repeaterPortAccessEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortAccessGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortAccessPortIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortAccessAddress"),
)
if mibBuilder.loadTexts:
    repeaterPortAccessEntry.setStatus("mandatory")
_RepeaterPortAccessGroupIndex_Type = Integer32
_RepeaterPortAccessGroupIndex_Object = MibTableColumn
repeaterPortAccessGroupIndex = _RepeaterPortAccessGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 2, 1, 1),
    _RepeaterPortAccessGroupIndex_Type()
)
repeaterPortAccessGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortAccessGroupIndex.setStatus("mandatory")
_RepeaterPortAccessPortIndex_Type = Integer32
_RepeaterPortAccessPortIndex_Object = MibTableColumn
repeaterPortAccessPortIndex = _RepeaterPortAccessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 2, 1, 2),
    _RepeaterPortAccessPortIndex_Type()
)
repeaterPortAccessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortAccessPortIndex.setStatus("mandatory")
_RepeaterPortAccessAddress_Type = MacAddress
_RepeaterPortAccessAddress_Object = MibTableColumn
repeaterPortAccessAddress = _RepeaterPortAccessAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 2, 1, 3),
    _RepeaterPortAccessAddress_Type()
)
repeaterPortAccessAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPortAccessAddress.setStatus("mandatory")


class _RepeaterPortAccessStatus_Type(Integer32):
    """Custom type repeaterPortAccessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterPortAccessStatus_Type.__name__ = "Integer32"
_RepeaterPortAccessStatus_Object = MibTableColumn
repeaterPortAccessStatus = _RepeaterPortAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 2, 1, 4),
    _RepeaterPortAccessStatus_Type()
)
repeaterPortAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessStatus.setStatus("mandatory")
_RepeaterPortAccessGroupIndexShadow_Type = Integer32
_RepeaterPortAccessGroupIndexShadow_Object = MibScalar
repeaterPortAccessGroupIndexShadow = _RepeaterPortAccessGroupIndexShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 3),
    _RepeaterPortAccessGroupIndexShadow_Type()
)
repeaterPortAccessGroupIndexShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessGroupIndexShadow.setStatus("mandatory")
_RepeaterPortAccessPortIndexShadow_Type = Integer32
_RepeaterPortAccessPortIndexShadow_Object = MibScalar
repeaterPortAccessPortIndexShadow = _RepeaterPortAccessPortIndexShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 4),
    _RepeaterPortAccessPortIndexShadow_Type()
)
repeaterPortAccessPortIndexShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessPortIndexShadow.setStatus("mandatory")
_RepeaterPortAccessAddressShadow_Type = MacAddress
_RepeaterPortAccessAddressShadow_Object = MibScalar
repeaterPortAccessAddressShadow = _RepeaterPortAccessAddressShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 5),
    _RepeaterPortAccessAddressShadow_Type()
)
repeaterPortAccessAddressShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessAddressShadow.setStatus("mandatory")


class _RepeaterPortAccessStatusShadow_Type(Integer32):
    """Custom type repeaterPortAccessStatusShadow based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_RepeaterPortAccessStatusShadow_Type.__name__ = "Integer32"
_RepeaterPortAccessStatusShadow_Object = MibScalar
repeaterPortAccessStatusShadow = _RepeaterPortAccessStatusShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 6),
    _RepeaterPortAccessStatusShadow_Type()
)
repeaterPortAccessStatusShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterPortAccessStatusShadow.setStatus("mandatory")
_RepeaterPort2Table_Object = MibTable
repeaterPort2Table = _RepeaterPort2Table_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7)
)
if mibBuilder.loadTexts:
    repeaterPort2Table.setStatus("mandatory")
_RepeaterPort2Entry_Object = MibTableRow
repeaterPort2Entry = _RepeaterPort2Entry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1)
)
repeaterPort2Entry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortIndex"),
)
if mibBuilder.loadTexts:
    repeaterPort2Entry.setStatus("mandatory")
_RepeaterPort2RmonOctets_Type = Counter32
_RepeaterPort2RmonOctets_Object = MibTableColumn
repeaterPort2RmonOctets = _RepeaterPort2RmonOctets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 1),
    _RepeaterPort2RmonOctets_Type()
)
repeaterPort2RmonOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonOctets.setStatus("mandatory")
_RepeaterPort2RmonPkts_Type = Counter32
_RepeaterPort2RmonPkts_Object = MibTableColumn
repeaterPort2RmonPkts = _RepeaterPort2RmonPkts_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 2),
    _RepeaterPort2RmonPkts_Type()
)
repeaterPort2RmonPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonPkts.setStatus("mandatory")
_RepeaterPort2RmonBroadcastPkts_Type = Counter32
_RepeaterPort2RmonBroadcastPkts_Object = MibTableColumn
repeaterPort2RmonBroadcastPkts = _RepeaterPort2RmonBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 3),
    _RepeaterPort2RmonBroadcastPkts_Type()
)
repeaterPort2RmonBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonBroadcastPkts.setStatus("mandatory")
_RepeaterPort2RmonMulticastPkts_Type = Counter32
_RepeaterPort2RmonMulticastPkts_Object = MibTableColumn
repeaterPort2RmonMulticastPkts = _RepeaterPort2RmonMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 4),
    _RepeaterPort2RmonMulticastPkts_Type()
)
repeaterPort2RmonMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonMulticastPkts.setStatus("mandatory")
_RepeaterPort2RmonCRCAlignErrors_Type = Counter32
_RepeaterPort2RmonCRCAlignErrors_Object = MibTableColumn
repeaterPort2RmonCRCAlignErrors = _RepeaterPort2RmonCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 5),
    _RepeaterPort2RmonCRCAlignErrors_Type()
)
repeaterPort2RmonCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonCRCAlignErrors.setStatus("mandatory")
_RepeaterPort2RmonPkts64Octets_Type = Counter32
_RepeaterPort2RmonPkts64Octets_Object = MibTableColumn
repeaterPort2RmonPkts64Octets = _RepeaterPort2RmonPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 6),
    _RepeaterPort2RmonPkts64Octets_Type()
)
repeaterPort2RmonPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonPkts64Octets.setStatus("mandatory")
_RepeaterPort2RmonPkts65to127Octets_Type = Counter32
_RepeaterPort2RmonPkts65to127Octets_Object = MibTableColumn
repeaterPort2RmonPkts65to127Octets = _RepeaterPort2RmonPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 7),
    _RepeaterPort2RmonPkts65to127Octets_Type()
)
repeaterPort2RmonPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonPkts65to127Octets.setStatus("mandatory")
_RepeaterPort2RmonPkts128to255Octets_Type = Counter32
_RepeaterPort2RmonPkts128to255Octets_Object = MibTableColumn
repeaterPort2RmonPkts128to255Octets = _RepeaterPort2RmonPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 8),
    _RepeaterPort2RmonPkts128to255Octets_Type()
)
repeaterPort2RmonPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonPkts128to255Octets.setStatus("mandatory")
_RepeaterPort2RmonPkts256to511Octets_Type = Counter32
_RepeaterPort2RmonPkts256to511Octets_Object = MibTableColumn
repeaterPort2RmonPkts256to511Octets = _RepeaterPort2RmonPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 9),
    _RepeaterPort2RmonPkts256to511Octets_Type()
)
repeaterPort2RmonPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonPkts256to511Octets.setStatus("mandatory")
_RepeaterPort2RmonPkts512to1023Octets_Type = Counter32
_RepeaterPort2RmonPkts512to1023Octets_Object = MibTableColumn
repeaterPort2RmonPkts512to1023Octets = _RepeaterPort2RmonPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 10),
    _RepeaterPort2RmonPkts512to1023Octets_Type()
)
repeaterPort2RmonPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonPkts512to1023Octets.setStatus("mandatory")
_RepeaterPort2RmonPkts1024to1518Octets_Type = Counter32
_RepeaterPort2RmonPkts1024to1518Octets_Object = MibTableColumn
repeaterPort2RmonPkts1024to1518Octets = _RepeaterPort2RmonPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 11),
    _RepeaterPort2RmonPkts1024to1518Octets_Type()
)
repeaterPort2RmonPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2RmonPkts1024to1518Octets.setStatus("mandatory")


class _RepeaterPort2TrafficRatio_Type(Integer32):
    """Custom type repeaterPort2TrafficRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterPort2TrafficRatio_Type.__name__ = "Integer32"
_RepeaterPort2TrafficRatio_Object = MibTableColumn
repeaterPort2TrafficRatio = _RepeaterPort2TrafficRatio_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 12),
    _RepeaterPort2TrafficRatio_Type()
)
repeaterPort2TrafficRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2TrafficRatio.setStatus("mandatory")


class _RepeaterPort2CollisionRatio_Type(Integer32):
    """Custom type repeaterPort2CollisionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterPort2CollisionRatio_Type.__name__ = "Integer32"
_RepeaterPort2CollisionRatio_Object = MibTableColumn
repeaterPort2CollisionRatio = _RepeaterPort2CollisionRatio_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 13),
    _RepeaterPort2CollisionRatio_Type()
)
repeaterPort2CollisionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2CollisionRatio.setStatus("mandatory")


class _RepeaterPort2ErrorRatio_Type(Integer32):
    """Custom type repeaterPort2ErrorRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterPort2ErrorRatio_Type.__name__ = "Integer32"
_RepeaterPort2ErrorRatio_Object = MibTableColumn
repeaterPort2ErrorRatio = _RepeaterPort2ErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 14),
    _RepeaterPort2ErrorRatio_Type()
)
repeaterPort2ErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2ErrorRatio.setStatus("mandatory")


class _RepeaterPort2BroadcastRatio_Type(Integer32):
    """Custom type repeaterPort2BroadcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterPort2BroadcastRatio_Type.__name__ = "Integer32"
_RepeaterPort2BroadcastRatio_Object = MibTableColumn
repeaterPort2BroadcastRatio = _RepeaterPort2BroadcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 15),
    _RepeaterPort2BroadcastRatio_Type()
)
repeaterPort2BroadcastRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2BroadcastRatio.setStatus("mandatory")


class _RepeaterPort2MulticastRatio_Type(Integer32):
    """Custom type repeaterPort2MulticastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterPort2MulticastRatio_Type.__name__ = "Integer32"
_RepeaterPort2MulticastRatio_Object = MibTableColumn
repeaterPort2MulticastRatio = _RepeaterPort2MulticastRatio_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 16),
    _RepeaterPort2MulticastRatio_Type()
)
repeaterPort2MulticastRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2MulticastRatio.setStatus("mandatory")


class _RepeaterPort2UnicastRatio_Type(Integer32):
    """Custom type repeaterPort2UnicastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RepeaterPort2UnicastRatio_Type.__name__ = "Integer32"
_RepeaterPort2UnicastRatio_Object = MibTableColumn
repeaterPort2UnicastRatio = _RepeaterPort2UnicastRatio_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 3, 7, 1, 17),
    _RepeaterPort2UnicastRatio_Type()
)
repeaterPort2UnicastRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterPort2UnicastRatio.setStatus("mandatory")
_XRepeaterSlotInfo_ObjectIdentity = ObjectIdentity
xRepeaterSlotInfo = _XRepeaterSlotInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17, 4)
)
_RepeaterSlotSegmentTable_Object = MibTable
repeaterSlotSegmentTable = _RepeaterSlotSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 4, 1)
)
if mibBuilder.loadTexts:
    repeaterSlotSegmentTable.setStatus("deprecated")
_RepeaterSlotSegmentEntry_Object = MibTableRow
repeaterSlotSegmentEntry = _RepeaterSlotSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 4, 1, 1)
)
repeaterSlotSegmentEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterSlotIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterSlotSegment"),
)
if mibBuilder.loadTexts:
    repeaterSlotSegmentEntry.setStatus("deprecated")
_RepeaterSlotIndex_Type = Integer32
_RepeaterSlotIndex_Object = MibTableColumn
repeaterSlotIndex = _RepeaterSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 4, 1, 1, 1),
    _RepeaterSlotIndex_Type()
)
repeaterSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSlotIndex.setStatus("deprecated")
_RepeaterSlotSegment_Type = Segment
_RepeaterSlotSegment_Object = MibTableColumn
repeaterSlotSegment = _RepeaterSlotSegment_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 4, 1, 1, 2),
    _RepeaterSlotSegment_Type()
)
repeaterSlotSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSlotSegment.setStatus("deprecated")


class _RepeaterSlotSegmentStatus_Type(Integer32):
    """Custom type repeaterSlotSegmentStatus based on Integer32"""
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


_RepeaterSlotSegmentStatus_Type.__name__ = "Integer32"
_RepeaterSlotSegmentStatus_Object = MibTableColumn
repeaterSlotSegmentStatus = _RepeaterSlotSegmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 4, 1, 1, 3),
    _RepeaterSlotSegmentStatus_Type()
)
repeaterSlotSegmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSlotSegmentStatus.setStatus("deprecated")
_XRepeaterSecurity_ObjectIdentity = ObjectIdentity
xRepeaterSecurity = _XRepeaterSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17, 5)
)


class _RepeaterSecurityState_Type(Integer32):
    """Custom type repeaterSecurityState based on Integer32"""
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


_RepeaterSecurityState_Type.__name__ = "Integer32"
_RepeaterSecurityState_Object = MibScalar
repeaterSecurityState = _RepeaterSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 1),
    _RepeaterSecurityState_Type()
)
repeaterSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityState.setStatus("mandatory")
_RepeaterSecurityPortTable_Object = MibTable
repeaterSecurityPortTable = _RepeaterSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 2)
)
if mibBuilder.loadTexts:
    repeaterSecurityPortTable.setStatus("mandatory")
_RepeaterSecurityPortEntry_Object = MibTableRow
repeaterSecurityPortEntry = _RepeaterSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 2, 1)
)
repeaterSecurityPortEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterPortIndex"),
)
if mibBuilder.loadTexts:
    repeaterSecurityPortEntry.setStatus("mandatory")


class _RepeaterSecurityPortUnicast_Type(Integer32):
    """Custom type repeaterSecurityPortUnicast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("jam", 1))
    )


_RepeaterSecurityPortUnicast_Type.__name__ = "Integer32"
_RepeaterSecurityPortUnicast_Object = MibTableColumn
repeaterSecurityPortUnicast = _RepeaterSecurityPortUnicast_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 2, 1, 1),
    _RepeaterSecurityPortUnicast_Type()
)
repeaterSecurityPortUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityPortUnicast.setStatus("mandatory")


class _RepeaterSecurityPortMulticast_Type(Integer32):
    """Custom type repeaterSecurityPortMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("jam", 1))
    )


_RepeaterSecurityPortMulticast_Type.__name__ = "Integer32"
_RepeaterSecurityPortMulticast_Object = MibTableColumn
repeaterSecurityPortMulticast = _RepeaterSecurityPortMulticast_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 2, 1, 2),
    _RepeaterSecurityPortMulticast_Type()
)
repeaterSecurityPortMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityPortMulticast.setStatus("mandatory")


class _RepeaterSecurityPortAllStatus_Type(Integer32):
    """Custom type repeaterSecurityPortAllStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterSecurityPortAllStatus_Type.__name__ = "Integer32"
_RepeaterSecurityPortAllStatus_Object = MibTableColumn
repeaterSecurityPortAllStatus = _RepeaterSecurityPortAllStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 2, 1, 3),
    _RepeaterSecurityPortAllStatus_Type()
)
repeaterSecurityPortAllStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityPortAllStatus.setStatus("mandatory")


class _RepeaterSecurityPortSecurityLearn_Type(Integer32):
    """Custom type repeaterSecurityPortSecurityLearn based on Integer32"""
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
        *(("continuous", 3),
          ("disabled", 1),
          ("single", 2))
    )


_RepeaterSecurityPortSecurityLearn_Type.__name__ = "Integer32"
_RepeaterSecurityPortSecurityLearn_Object = MibTableColumn
repeaterSecurityPortSecurityLearn = _RepeaterSecurityPortSecurityLearn_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 2, 1, 4),
    _RepeaterSecurityPortSecurityLearn_Type()
)
repeaterSecurityPortSecurityLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityPortSecurityLearn.setStatus("mandatory")
_RepeaterSecurityTable_Object = MibTable
repeaterSecurityTable = _RepeaterSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 3)
)
if mibBuilder.loadTexts:
    repeaterSecurityTable.setStatus("mandatory")
_RepeaterSecurityEntry_Object = MibTableRow
repeaterSecurityEntry = _RepeaterSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 3, 1)
)
repeaterSecurityEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterSecurityGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterSecurityPortIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterSecurityAddress"),
)
if mibBuilder.loadTexts:
    repeaterSecurityEntry.setStatus("mandatory")
_RepeaterSecurityGroupIndex_Type = Integer32
_RepeaterSecurityGroupIndex_Object = MibTableColumn
repeaterSecurityGroupIndex = _RepeaterSecurityGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 3, 1, 1),
    _RepeaterSecurityGroupIndex_Type()
)
repeaterSecurityGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSecurityGroupIndex.setStatus("mandatory")
_RepeaterSecurityPortIndex_Type = Integer32
_RepeaterSecurityPortIndex_Object = MibTableColumn
repeaterSecurityPortIndex = _RepeaterSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 3, 1, 2),
    _RepeaterSecurityPortIndex_Type()
)
repeaterSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSecurityPortIndex.setStatus("mandatory")
_RepeaterSecurityAddress_Type = MacAddress
_RepeaterSecurityAddress_Object = MibTableColumn
repeaterSecurityAddress = _RepeaterSecurityAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 3, 1, 3),
    _RepeaterSecurityAddress_Type()
)
repeaterSecurityAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSecurityAddress.setStatus("mandatory")


class _RepeaterSecurityStatus_Type(Integer32):
    """Custom type repeaterSecurityStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterSecurityStatus_Type.__name__ = "Integer32"
_RepeaterSecurityStatus_Object = MibTableColumn
repeaterSecurityStatus = _RepeaterSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 3, 1, 4),
    _RepeaterSecurityStatus_Type()
)
repeaterSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityStatus.setStatus("mandatory")


class _RepeaterSecurityAction_Type(Integer32):
    """Custom type repeaterSecurityAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("jam", 1))
    )


_RepeaterSecurityAction_Type.__name__ = "Integer32"
_RepeaterSecurityAction_Object = MibTableColumn
repeaterSecurityAction = _RepeaterSecurityAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 3, 1, 5),
    _RepeaterSecurityAction_Type()
)
repeaterSecurityAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityAction.setStatus("mandatory")
_RepeaterSecurityGroupIndexShadow_Type = Integer32
_RepeaterSecurityGroupIndexShadow_Object = MibScalar
repeaterSecurityGroupIndexShadow = _RepeaterSecurityGroupIndexShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 4),
    _RepeaterSecurityGroupIndexShadow_Type()
)
repeaterSecurityGroupIndexShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityGroupIndexShadow.setStatus("mandatory")
_RepeaterSecurityPortIndexShadow_Type = Integer32
_RepeaterSecurityPortIndexShadow_Object = MibScalar
repeaterSecurityPortIndexShadow = _RepeaterSecurityPortIndexShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 5),
    _RepeaterSecurityPortIndexShadow_Type()
)
repeaterSecurityPortIndexShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityPortIndexShadow.setStatus("mandatory")
_RepeaterSecurityAddressShadow_Type = MacAddress
_RepeaterSecurityAddressShadow_Object = MibScalar
repeaterSecurityAddressShadow = _RepeaterSecurityAddressShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 6),
    _RepeaterSecurityAddressShadow_Type()
)
repeaterSecurityAddressShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityAddressShadow.setStatus("mandatory")


class _RepeaterSecurityStatusShadow_Type(Integer32):
    """Custom type repeaterSecurityStatusShadow based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_RepeaterSecurityStatusShadow_Type.__name__ = "Integer32"
_RepeaterSecurityStatusShadow_Object = MibScalar
repeaterSecurityStatusShadow = _RepeaterSecurityStatusShadow_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 7),
    _RepeaterSecurityStatusShadow_Type()
)
repeaterSecurityStatusShadow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityStatusShadow.setStatus("mandatory")
_RepeaterSecurityGlobalAddressTable_Object = MibTable
repeaterSecurityGlobalAddressTable = _RepeaterSecurityGlobalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 8)
)
if mibBuilder.loadTexts:
    repeaterSecurityGlobalAddressTable.setStatus("mandatory")
_RepeaterSecurityGlobalAddressEntry_Object = MibTableRow
repeaterSecurityGlobalAddressEntry = _RepeaterSecurityGlobalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 8, 1)
)
repeaterSecurityGlobalAddressEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterSecurityGlobalAddress"),
)
if mibBuilder.loadTexts:
    repeaterSecurityGlobalAddressEntry.setStatus("mandatory")
_RepeaterSecurityGlobalAddress_Type = MacAddress
_RepeaterSecurityGlobalAddress_Object = MibTableColumn
repeaterSecurityGlobalAddress = _RepeaterSecurityGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 8, 1, 1),
    _RepeaterSecurityGlobalAddress_Type()
)
repeaterSecurityGlobalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSecurityGlobalAddress.setStatus("mandatory")


class _RepeaterSecurityGlobalAddressStatus_Type(Integer32):
    """Custom type repeaterSecurityGlobalAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterSecurityGlobalAddressStatus_Type.__name__ = "Integer32"
_RepeaterSecurityGlobalAddressStatus_Object = MibTableColumn
repeaterSecurityGlobalAddressStatus = _RepeaterSecurityGlobalAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 8, 1, 2),
    _RepeaterSecurityGlobalAddressStatus_Type()
)
repeaterSecurityGlobalAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityGlobalAddressStatus.setStatus("mandatory")


class _RepeaterSecurityGlobalAddressAction_Type(Integer32):
    """Custom type repeaterSecurityGlobalAddressAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 2),
          ("jam", 1))
    )


_RepeaterSecurityGlobalAddressAction_Type.__name__ = "Integer32"
_RepeaterSecurityGlobalAddressAction_Object = MibTableColumn
repeaterSecurityGlobalAddressAction = _RepeaterSecurityGlobalAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 8, 1, 3),
    _RepeaterSecurityGlobalAddressAction_Type()
)
repeaterSecurityGlobalAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityGlobalAddressAction.setStatus("mandatory")
_RepeaterSecurityGlobalDBID_Type = Integer32
_RepeaterSecurityGlobalDBID_Object = MibScalar
repeaterSecurityGlobalDBID = _RepeaterSecurityGlobalDBID_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 9),
    _RepeaterSecurityGlobalDBID_Type()
)
repeaterSecurityGlobalDBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSecurityGlobalDBID.setStatus("mandatory")


class _RepeaterSecurityGlobalSecurityAdminState_Type(Integer32):
    """Custom type repeaterSecurityGlobalSecurityAdminState based on Integer32"""
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


_RepeaterSecurityGlobalSecurityAdminState_Type.__name__ = "Integer32"
_RepeaterSecurityGlobalSecurityAdminState_Object = MibScalar
repeaterSecurityGlobalSecurityAdminState = _RepeaterSecurityGlobalSecurityAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 10),
    _RepeaterSecurityGlobalSecurityAdminState_Type()
)
repeaterSecurityGlobalSecurityAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterSecurityGlobalSecurityAdminState.setStatus("mandatory")


class _RepeaterSecurityGlobalSecurityOperState_Type(Integer32):
    """Custom type repeaterSecurityGlobalSecurityOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("securityDisabled", 3))
    )


_RepeaterSecurityGlobalSecurityOperState_Type.__name__ = "Integer32"
_RepeaterSecurityGlobalSecurityOperState_Object = MibScalar
repeaterSecurityGlobalSecurityOperState = _RepeaterSecurityGlobalSecurityOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 5, 11),
    _RepeaterSecurityGlobalSecurityOperState_Type()
)
repeaterSecurityGlobalSecurityOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterSecurityGlobalSecurityOperState.setStatus("mandatory")
_XRepeaterRepeater_ObjectIdentity = ObjectIdentity
xRepeaterRepeater = _XRepeaterRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17, 6)
)
_RepeaterRepeaterTable_Object = MibTable
repeaterRepeaterTable = _RepeaterRepeaterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1)
)
if mibBuilder.loadTexts:
    repeaterRepeaterTable.setStatus("mandatory")
_RepeaterRepeaterEntry_Object = MibTableRow
repeaterRepeaterEntry = _RepeaterRepeaterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1)
)
repeaterRepeaterEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterRepeaterGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterRepeaterIndex"),
)
if mibBuilder.loadTexts:
    repeaterRepeaterEntry.setStatus("mandatory")
_RepeaterRepeaterGroupIndex_Type = Integer32
_RepeaterRepeaterGroupIndex_Object = MibTableColumn
repeaterRepeaterGroupIndex = _RepeaterRepeaterGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 1),
    _RepeaterRepeaterGroupIndex_Type()
)
repeaterRepeaterGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterGroupIndex.setStatus("mandatory")
_RepeaterRepeaterIndex_Type = Integer32
_RepeaterRepeaterIndex_Object = MibTableColumn
repeaterRepeaterIndex = _RepeaterRepeaterIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 2),
    _RepeaterRepeaterIndex_Type()
)
repeaterRepeaterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterIndex.setStatus("mandatory")
_RepeaterRepeaterSegment_Type = Segment
_RepeaterRepeaterSegment_Object = MibTableColumn
repeaterRepeaterSegment = _RepeaterRepeaterSegment_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 3),
    _RepeaterRepeaterSegment_Type()
)
repeaterRepeaterSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRepeaterSegment.setStatus("mandatory")


class _RepeaterRepeaterReports_Type(Integer32):
    """Custom type repeaterRepeaterReports based on Integer32"""
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


_RepeaterRepeaterReports_Type.__name__ = "Integer32"
_RepeaterRepeaterReports_Object = MibTableColumn
repeaterRepeaterReports = _RepeaterRepeaterReports_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 4),
    _RepeaterRepeaterReports_Type()
)
repeaterRepeaterReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRepeaterReports.setStatus("mandatory")
_RepeaterRepeaterCollisions_Type = Counter32
_RepeaterRepeaterCollisions_Object = MibTableColumn
repeaterRepeaterCollisions = _RepeaterRepeaterCollisions_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 5),
    _RepeaterRepeaterCollisions_Type()
)
repeaterRepeaterCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterCollisions.setStatus("mandatory")
_RepeaterRepeaterJabbers_Type = Counter32
_RepeaterRepeaterJabbers_Object = MibTableColumn
repeaterRepeaterJabbers = _RepeaterRepeaterJabbers_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 6),
    _RepeaterRepeaterJabbers_Type()
)
repeaterRepeaterJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterJabbers.setStatus("mandatory")
_RepeaterRepeaterSQE_Type = Counter32
_RepeaterRepeaterSQE_Object = MibTableColumn
repeaterRepeaterSQE = _RepeaterRepeaterSQE_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 7),
    _RepeaterRepeaterSQE_Type()
)
repeaterRepeaterSQE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterSQE.setStatus("mandatory")
_RepeaterRepeaterFifoOverflows_Type = Counter32
_RepeaterRepeaterFifoOverflows_Object = MibTableColumn
repeaterRepeaterFifoOverflows = _RepeaterRepeaterFifoOverflows_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 8),
    _RepeaterRepeaterFifoOverflows_Type()
)
repeaterRepeaterFifoOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterFifoOverflows.setStatus("mandatory")


class _RepeaterRepeaterZero_Type(Integer32):
    """Custom type repeaterRepeaterZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_RepeaterRepeaterZero_Type.__name__ = "Integer32"
_RepeaterRepeaterZero_Object = MibTableColumn
repeaterRepeaterZero = _RepeaterRepeaterZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 9),
    _RepeaterRepeaterZero_Type()
)
repeaterRepeaterZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRepeaterZero.setStatus("mandatory")
_RepeaterRepeaterSinceZero_Type = TimeTicks
_RepeaterRepeaterSinceZero_Object = MibTableColumn
repeaterRepeaterSinceZero = _RepeaterRepeaterSinceZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 10),
    _RepeaterRepeaterSinceZero_Type()
)
repeaterRepeaterSinceZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterSinceZero.setStatus("mandatory")
_RepeaterRepeaterSegmentsAllowed_Type = OctetString
_RepeaterRepeaterSegmentsAllowed_Object = MibTableColumn
repeaterRepeaterSegmentsAllowed = _RepeaterRepeaterSegmentsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 11),
    _RepeaterRepeaterSegmentsAllowed_Type()
)
repeaterRepeaterSegmentsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterSegmentsAllowed.setStatus("mandatory")
_RepeaterRepeaterTotalOctets_Type = Counter32
_RepeaterRepeaterTotalOctets_Object = MibTableColumn
repeaterRepeaterTotalOctets = _RepeaterRepeaterTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 12),
    _RepeaterRepeaterTotalOctets_Type()
)
repeaterRepeaterTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterTotalOctets.setStatus("mandatory")
_RepeaterRepeaterTotalFrames_Type = Counter32
_RepeaterRepeaterTotalFrames_Object = MibTableColumn
repeaterRepeaterTotalFrames = _RepeaterRepeaterTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 13),
    _RepeaterRepeaterTotalFrames_Type()
)
repeaterRepeaterTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterTotalFrames.setStatus("mandatory")
_RepeaterRepeaterPercentUtilization_Type = Gauge32
_RepeaterRepeaterPercentUtilization_Object = MibTableColumn
repeaterRepeaterPercentUtilization = _RepeaterRepeaterPercentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 6, 1, 1, 14),
    _RepeaterRepeaterPercentUtilization_Type()
)
repeaterRepeaterPercentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRepeaterPercentUtilization.setStatus("mandatory")
_XRepeaterRedundancy_ObjectIdentity = ObjectIdentity
xRepeaterRedundancy = _XRepeaterRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 17, 7)
)


class _RepeaterRedundancyState_Type(Integer32):
    """Custom type repeaterRedundancyState based on Integer32"""
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


_RepeaterRedundancyState_Type.__name__ = "Integer32"
_RepeaterRedundancyState_Object = MibScalar
repeaterRedundancyState = _RepeaterRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 1),
    _RepeaterRedundancyState_Type()
)
repeaterRedundancyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyState.setStatus("mandatory")
_RepeaterRedundancyGroupTable_Object = MibTable
repeaterRedundancyGroupTable = _RepeaterRedundancyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2)
)
if mibBuilder.loadTexts:
    repeaterRedundancyGroupTable.setStatus("mandatory")
_RepeaterRedundancyGroupEntry_Object = MibTableRow
repeaterRedundancyGroupEntry = _RepeaterRedundancyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1)
)
repeaterRedundancyGroupEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterRedundancyGroupGroupIndex"),
)
if mibBuilder.loadTexts:
    repeaterRedundancyGroupEntry.setStatus("mandatory")
_RepeaterRedundancyGroupGroupIndex_Type = Integer32
_RepeaterRedundancyGroupGroupIndex_Object = MibTableColumn
repeaterRedundancyGroupGroupIndex = _RepeaterRedundancyGroupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 1),
    _RepeaterRedundancyGroupGroupIndex_Type()
)
repeaterRedundancyGroupGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupGroupIndex.setStatus("mandatory")


class _RepeaterRedundancyGroupStatus_Type(Integer32):
    """Custom type repeaterRedundancyGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterRedundancyGroupStatus_Type.__name__ = "Integer32"
_RepeaterRedundancyGroupStatus_Object = MibTableColumn
repeaterRedundancyGroupStatus = _RepeaterRedundancyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 2),
    _RepeaterRedundancyGroupStatus_Type()
)
repeaterRedundancyGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupStatus.setStatus("mandatory")


class _RepeaterRedundancyGroupName_Type(DisplayString):
    """Custom type repeaterRedundancyGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RepeaterRedundancyGroupName_Type.__name__ = "DisplayString"
_RepeaterRedundancyGroupName_Object = MibTableColumn
repeaterRedundancyGroupName = _RepeaterRedundancyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 3),
    _RepeaterRedundancyGroupName_Type()
)
repeaterRedundancyGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupName.setStatus("mandatory")


class _RepeaterRedundancyGroupAdminState_Type(Integer32):
    """Custom type repeaterRedundancyGroupAdminState based on Integer32"""
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


_RepeaterRedundancyGroupAdminState_Type.__name__ = "Integer32"
_RepeaterRedundancyGroupAdminState_Object = MibTableColumn
repeaterRedundancyGroupAdminState = _RepeaterRedundancyGroupAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 4),
    _RepeaterRedundancyGroupAdminState_Type()
)
repeaterRedundancyGroupAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupAdminState.setStatus("mandatory")


class _RepeaterRedundancyGroupTestInterval_Type(Integer32):
    """Custom type repeaterRedundancyGroupTestInterval based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 180000),
    )


_RepeaterRedundancyGroupTestInterval_Type.__name__ = "Integer32"
_RepeaterRedundancyGroupTestInterval_Object = MibTableColumn
repeaterRedundancyGroupTestInterval = _RepeaterRedundancyGroupTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 5),
    _RepeaterRedundancyGroupTestInterval_Type()
)
repeaterRedundancyGroupTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupTestInterval.setStatus("mandatory")


class _RepeaterRedundancyGroupRollbackAdminState_Type(Integer32):
    """Custom type repeaterRedundancyGroupRollbackAdminState based on Integer32"""
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


_RepeaterRedundancyGroupRollbackAdminState_Type.__name__ = "Integer32"
_RepeaterRedundancyGroupRollbackAdminState_Object = MibTableColumn
repeaterRedundancyGroupRollbackAdminState = _RepeaterRedundancyGroupRollbackAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 6),
    _RepeaterRedundancyGroupRollbackAdminState_Type()
)
repeaterRedundancyGroupRollbackAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupRollbackAdminState.setStatus("mandatory")


class _RepeaterRedundancyGroupRollbackInterval_Type(Integer32):
    """Custom type repeaterRedundancyGroupRollbackInterval based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 180000),
    )


_RepeaterRedundancyGroupRollbackInterval_Type.__name__ = "Integer32"
_RepeaterRedundancyGroupRollbackInterval_Object = MibTableColumn
repeaterRedundancyGroupRollbackInterval = _RepeaterRedundancyGroupRollbackInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 7),
    _RepeaterRedundancyGroupRollbackInterval_Type()
)
repeaterRedundancyGroupRollbackInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupRollbackInterval.setStatus("mandatory")
_RepeaterRedundancyGroupOperPath_Type = Integer32
_RepeaterRedundancyGroupOperPath_Object = MibTableColumn
repeaterRedundancyGroupOperPath = _RepeaterRedundancyGroupOperPath_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 8),
    _RepeaterRedundancyGroupOperPath_Type()
)
repeaterRedundancyGroupOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupOperPath.setStatus("mandatory")
_RepeaterRedundancyGroupPathChanges_Type = Counter32
_RepeaterRedundancyGroupPathChanges_Object = MibTableColumn
repeaterRedundancyGroupPathChanges = _RepeaterRedundancyGroupPathChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 9),
    _RepeaterRedundancyGroupPathChanges_Type()
)
repeaterRedundancyGroupPathChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupPathChanges.setStatus("mandatory")
_RepeaterRedundancyGroupRollbackAttempts_Type = Counter32
_RepeaterRedundancyGroupRollbackAttempts_Object = MibTableColumn
repeaterRedundancyGroupRollbackAttempts = _RepeaterRedundancyGroupRollbackAttempts_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 10),
    _RepeaterRedundancyGroupRollbackAttempts_Type()
)
repeaterRedundancyGroupRollbackAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupRollbackAttempts.setStatus("mandatory")


class _RepeaterRedundancyGroupZero_Type(Integer32):
    """Custom type repeaterRedundancyGroupZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_RepeaterRedundancyGroupZero_Type.__name__ = "Integer32"
_RepeaterRedundancyGroupZero_Object = MibTableColumn
repeaterRedundancyGroupZero = _RepeaterRedundancyGroupZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 11),
    _RepeaterRedundancyGroupZero_Type()
)
repeaterRedundancyGroupZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupZero.setStatus("mandatory")
_RepeaterRedundancyGroupSinceZero_Type = TimeTicks
_RepeaterRedundancyGroupSinceZero_Object = MibTableColumn
repeaterRedundancyGroupSinceZero = _RepeaterRedundancyGroupSinceZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 12),
    _RepeaterRedundancyGroupSinceZero_Type()
)
repeaterRedundancyGroupSinceZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupSinceZero.setStatus("mandatory")


class _RepeaterRedundancyGroupConfigStatus_Type(Integer32):
    """Custom type repeaterRedundancyGroupConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("incomplete", 1))
    )


_RepeaterRedundancyGroupConfigStatus_Type.__name__ = "Integer32"
_RepeaterRedundancyGroupConfigStatus_Object = MibTableColumn
repeaterRedundancyGroupConfigStatus = _RepeaterRedundancyGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 2, 1, 13),
    _RepeaterRedundancyGroupConfigStatus_Type()
)
repeaterRedundancyGroupConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyGroupConfigStatus.setStatus("mandatory")
_RepeaterRedundancyPathTable_Object = MibTable
repeaterRedundancyPathTable = _RepeaterRedundancyPathTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3)
)
if mibBuilder.loadTexts:
    repeaterRedundancyPathTable.setStatus("mandatory")
_RepeaterRedundancyPathEntry_Object = MibTableRow
repeaterRedundancyPathEntry = _RepeaterRedundancyPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1)
)
repeaterRedundancyPathEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterRedundancyPathGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterRedundancyPathPathIndex"),
)
if mibBuilder.loadTexts:
    repeaterRedundancyPathEntry.setStatus("mandatory")
_RepeaterRedundancyPathGroupIndex_Type = Integer32
_RepeaterRedundancyPathGroupIndex_Object = MibTableColumn
repeaterRedundancyPathGroupIndex = _RepeaterRedundancyPathGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 1),
    _RepeaterRedundancyPathGroupIndex_Type()
)
repeaterRedundancyPathGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyPathGroupIndex.setStatus("mandatory")
_RepeaterRedundancyPathPathIndex_Type = Integer32
_RepeaterRedundancyPathPathIndex_Object = MibTableColumn
repeaterRedundancyPathPathIndex = _RepeaterRedundancyPathPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 2),
    _RepeaterRedundancyPathPathIndex_Type()
)
repeaterRedundancyPathPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyPathPathIndex.setStatus("mandatory")


class _RepeaterRedundancyPathStatus_Type(Integer32):
    """Custom type repeaterRedundancyPathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterRedundancyPathStatus_Type.__name__ = "Integer32"
_RepeaterRedundancyPathStatus_Object = MibTableColumn
repeaterRedundancyPathStatus = _RepeaterRedundancyPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 3),
    _RepeaterRedundancyPathStatus_Type()
)
repeaterRedundancyPathStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathStatus.setStatus("mandatory")
_RepeaterRedundancyPathSlot_Type = Integer32
_RepeaterRedundancyPathSlot_Object = MibTableColumn
repeaterRedundancyPathSlot = _RepeaterRedundancyPathSlot_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 4),
    _RepeaterRedundancyPathSlot_Type()
)
repeaterRedundancyPathSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathSlot.setStatus("mandatory")
_RepeaterRedundancyPathPort_Type = Integer32
_RepeaterRedundancyPathPort_Object = MibTableColumn
repeaterRedundancyPathPort = _RepeaterRedundancyPathPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 5),
    _RepeaterRedundancyPathPort_Type()
)
repeaterRedundancyPathPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathPort.setStatus("mandatory")


class _RepeaterRedundancyPathPriority_Type(Integer32):
    """Custom type repeaterRedundancyPathPriority based on Integer32"""
    defaultValue = 5


_RepeaterRedundancyPathPriority_Object = MibTableColumn
repeaterRedundancyPathPriority = _RepeaterRedundancyPathPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 6),
    _RepeaterRedundancyPathPriority_Type()
)
repeaterRedundancyPathPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathPriority.setStatus("mandatory")


class _RepeaterRedundancyPathActivate_Type(Integer32):
    """Custom type repeaterRedundancyPathActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_RepeaterRedundancyPathActivate_Type.__name__ = "Integer32"
_RepeaterRedundancyPathActivate_Object = MibTableColumn
repeaterRedundancyPathActivate = _RepeaterRedundancyPathActivate_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 7),
    _RepeaterRedundancyPathActivate_Type()
)
repeaterRedundancyPathActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathActivate.setStatus("mandatory")


class _RepeaterRedundancyPathTimeout_Type(Integer32):
    """Custom type repeaterRedundancyPathTimeout based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_RepeaterRedundancyPathTimeout_Type.__name__ = "Integer32"
_RepeaterRedundancyPathTimeout_Object = MibTableColumn
repeaterRedundancyPathTimeout = _RepeaterRedundancyPathTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 8),
    _RepeaterRedundancyPathTimeout_Type()
)
repeaterRedundancyPathTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathTimeout.setStatus("mandatory")


class _RepeaterRedundancyPathRetryCount_Type(Integer32):
    """Custom type repeaterRedundancyPathRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_RepeaterRedundancyPathRetryCount_Type.__name__ = "Integer32"
_RepeaterRedundancyPathRetryCount_Object = MibTableColumn
repeaterRedundancyPathRetryCount = _RepeaterRedundancyPathRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 9),
    _RepeaterRedundancyPathRetryCount_Type()
)
repeaterRedundancyPathRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathRetryCount.setStatus("mandatory")
_RepeaterRedundancyPathTestAttempts_Type = Counter32
_RepeaterRedundancyPathTestAttempts_Object = MibTableColumn
repeaterRedundancyPathTestAttempts = _RepeaterRedundancyPathTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 10),
    _RepeaterRedundancyPathTestAttempts_Type()
)
repeaterRedundancyPathTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyPathTestAttempts.setStatus("mandatory")


class _RepeaterRedundancyPathLastTestStatus_Type(Integer32):
    """Custom type repeaterRedundancyPathLastTestStatus based on Integer32"""
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
        *(("noIntegrity", 4),
          ("notTested", 1),
          ("responded", 2),
          ("timeout", 3))
    )


_RepeaterRedundancyPathLastTestStatus_Type.__name__ = "Integer32"
_RepeaterRedundancyPathLastTestStatus_Object = MibTableColumn
repeaterRedundancyPathLastTestStatus = _RepeaterRedundancyPathLastTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 11),
    _RepeaterRedundancyPathLastTestStatus_Type()
)
repeaterRedundancyPathLastTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyPathLastTestStatus.setStatus("mandatory")


class _RepeaterRedundancyPathDisposition_Type(Integer32):
    """Custom type repeaterRedundancyPathDisposition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("null", 2))
    )


_RepeaterRedundancyPathDisposition_Type.__name__ = "Integer32"
_RepeaterRedundancyPathDisposition_Object = MibTableColumn
repeaterRedundancyPathDisposition = _RepeaterRedundancyPathDisposition_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 12),
    _RepeaterRedundancyPathDisposition_Type()
)
repeaterRedundancyPathDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathDisposition.setStatus("mandatory")


class _RepeaterRedundancyPathConfigStatus_Type(Integer32):
    """Custom type repeaterRedundancyPathConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("incomplete", 1))
    )


_RepeaterRedundancyPathConfigStatus_Type.__name__ = "Integer32"
_RepeaterRedundancyPathConfigStatus_Object = MibTableColumn
repeaterRedundancyPathConfigStatus = _RepeaterRedundancyPathConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 13),
    _RepeaterRedundancyPathConfigStatus_Type()
)
repeaterRedundancyPathConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyPathConfigStatus.setStatus("mandatory")


class _RepeaterRedundancyPathAdminState_Type(Integer32):
    """Custom type repeaterRedundancyPathAdminState based on Integer32"""
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


_RepeaterRedundancyPathAdminState_Type.__name__ = "Integer32"
_RepeaterRedundancyPathAdminState_Object = MibTableColumn
repeaterRedundancyPathAdminState = _RepeaterRedundancyPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 3, 1, 14),
    _RepeaterRedundancyPathAdminState_Type()
)
repeaterRedundancyPathAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyPathAdminState.setStatus("mandatory")
_RepeaterRedundancyAddressTable_Object = MibTable
repeaterRedundancyAddressTable = _RepeaterRedundancyAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4)
)
if mibBuilder.loadTexts:
    repeaterRedundancyAddressTable.setStatus("mandatory")
_RepeaterRedundancyAddressEntry_Object = MibTableRow
repeaterRedundancyAddressEntry = _RepeaterRedundancyAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4, 1)
)
repeaterRedundancyAddressEntry.setIndexNames(
    (0, "ITOUCH-REPEATER-MIB", "repeaterRedundancyAddressGroupIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterRedundancyAddressPathIndex"),
    (0, "ITOUCH-REPEATER-MIB", "repeaterRedundancyAddressAddress"),
)
if mibBuilder.loadTexts:
    repeaterRedundancyAddressEntry.setStatus("mandatory")
_RepeaterRedundancyAddressGroupIndex_Type = Integer32
_RepeaterRedundancyAddressGroupIndex_Object = MibTableColumn
repeaterRedundancyAddressGroupIndex = _RepeaterRedundancyAddressGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4, 1, 1),
    _RepeaterRedundancyAddressGroupIndex_Type()
)
repeaterRedundancyAddressGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyAddressGroupIndex.setStatus("mandatory")
_RepeaterRedundancyAddressPathIndex_Type = Integer32
_RepeaterRedundancyAddressPathIndex_Object = MibTableColumn
repeaterRedundancyAddressPathIndex = _RepeaterRedundancyAddressPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4, 1, 2),
    _RepeaterRedundancyAddressPathIndex_Type()
)
repeaterRedundancyAddressPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyAddressPathIndex.setStatus("mandatory")
_RepeaterRedundancyAddressAddress_Type = TypedAddress
_RepeaterRedundancyAddressAddress_Object = MibTableColumn
repeaterRedundancyAddressAddress = _RepeaterRedundancyAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4, 1, 3),
    _RepeaterRedundancyAddressAddress_Type()
)
repeaterRedundancyAddressAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyAddressAddress.setStatus("mandatory")


class _RepeaterRedundancyAddressStatus_Type(Integer32):
    """Custom type repeaterRedundancyAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RepeaterRedundancyAddressStatus_Type.__name__ = "Integer32"
_RepeaterRedundancyAddressStatus_Object = MibTableColumn
repeaterRedundancyAddressStatus = _RepeaterRedundancyAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4, 1, 4),
    _RepeaterRedundancyAddressStatus_Type()
)
repeaterRedundancyAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    repeaterRedundancyAddressStatus.setStatus("mandatory")
_RepeaterRedundancyAddressResponses_Type = Counter32
_RepeaterRedundancyAddressResponses_Object = MibTableColumn
repeaterRedundancyAddressResponses = _RepeaterRedundancyAddressResponses_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4, 1, 5),
    _RepeaterRedundancyAddressResponses_Type()
)
repeaterRedundancyAddressResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyAddressResponses.setStatus("mandatory")


class _RepeaterRedundancyAddressLastTestStatus_Type(Integer32):
    """Custom type repeaterRedundancyAddressLastTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notTested", 1),
          ("responded", 2),
          ("timeout", 3))
    )


_RepeaterRedundancyAddressLastTestStatus_Type.__name__ = "Integer32"
_RepeaterRedundancyAddressLastTestStatus_Object = MibTableColumn
repeaterRedundancyAddressLastTestStatus = _RepeaterRedundancyAddressLastTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 17, 7, 4, 1, 6),
    _RepeaterRedundancyAddressLastTestStatus_Type()
)
repeaterRedundancyAddressLastTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    repeaterRedundancyAddressLastTestStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accessViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 17, 0, 1)
)
accessViolation.setObjects(
    ("ITOUCH-REPEATER-MIB", "repeaterPortIndex")
)
if mibBuilder.loadTexts:
    accessViolation.setStatus(
        ""
    )

integrityLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 17, 0, 2)
)
integrityLoss.setObjects(
      *(("ITOUCH-REPEATER-MIB", "repeaterPortIndex"),
        ("ITOUCH-REPEATER-MIB", "repeaterPortGroupIndex"))
)
if mibBuilder.loadTexts:
    integrityLoss.setStatus(
        ""
    )

redundancyPathChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 17, 0, 3)
)
redundancyPathChange.setObjects(
      *(("ITOUCH-REPEATER-MIB", "repeaterRedundancyGroupGroupIndex"),
        ("ITOUCH-REPEATER-MIB", "repeaterRedundancyGroupOperPath"))
)
if mibBuilder.loadTexts:
    redundancyPathChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-REPEATER-MIB",
    **{"Segment": Segment,
       "Repeater": Repeater,
       "hubDeprecated": hubDeprecated,
       "xRepeater": xRepeater,
       "accessViolation": accessViolation,
       "integrityLoss": integrityLoss,
       "redundancyPathChange": redundancyPathChange,
       "xRepeaterInfo": xRepeaterInfo,
       "repeaterAccessViolation": repeaterAccessViolation,
       "repeaterMyGroup": repeaterMyGroup,
       "repeaterFifoOverflows": repeaterFifoOverflows,
       "repeaterLEDDisplay": repeaterLEDDisplay,
       "repeaterReports": repeaterReports,
       "repeaterHealthTrap": repeaterHealthTrap,
       "repeaterStatusChangeTrap": repeaterStatusChangeTrap,
       "repeaterAccessViolationTrap": repeaterAccessViolationTrap,
       "repeaterIntegrityLossTrap": repeaterIntegrityLossTrap,
       "repeaterRedundancyPathChangeTrap": repeaterRedundancyPathChangeTrap,
       "xRepeaterGroupInfo": xRepeaterGroupInfo,
       "repeaterGroupTable": repeaterGroupTable,
       "repeaterGroupEntry": repeaterGroupEntry,
       "repeaterGroupIndex": repeaterGroupIndex,
       "repeaterGroupSQE": repeaterGroupSQE,
       "repeaterGroupJabbers": repeaterGroupJabbers,
       "repeaterGroupSegment": repeaterGroupSegment,
       "repeaterGroupSecurityLock": repeaterGroupSecurityLock,
       "repeaterGroupIOCardType": repeaterGroupIOCardType,
       "repeaterGroupIOCardFirmwareVersion": repeaterGroupIOCardFirmwareVersion,
       "repeaterGroupIOCardOperStatus": repeaterGroupIOCardOperStatus,
       "repeaterGroupManagement": repeaterGroupManagement,
       "repeaterGroupRepeaterNumber": repeaterGroupRepeaterNumber,
       "repeaterGroupRepeaterHardwareVersion": repeaterGroupRepeaterHardwareVersion,
       "repeaterGroupManagerRepeater": repeaterGroupManagerRepeater,
       "repeaterGroupFifoErrors": repeaterGroupFifoErrors,
       "repeaterGroupCpuUtilization": repeaterGroupCpuUtilization,
       "repeaterGroupMemoryUtilization": repeaterGroupMemoryUtilization,
       "repeaterGroupAlarmCount": repeaterGroupAlarmCount,
       "xRepeaterPortInfo": xRepeaterPortInfo,
       "repeaterPortTable": repeaterPortTable,
       "repeaterPortEntry": repeaterPortEntry,
       "repeaterPortGroupIndex": repeaterPortGroupIndex,
       "repeaterPortIndex": repeaterPortIndex,
       "repeaterPortName": repeaterPortName,
       "repeaterPortAutoPolarity": repeaterPortAutoPolarity,
       "repeaterPortPolarityDirection": repeaterPortPolarityDirection,
       "repeaterPortPulse": repeaterPortPulse,
       "repeaterPortPulseStatus": repeaterPortPulseStatus,
       "repeaterPortPulseLosses": repeaterPortPulseLosses,
       "repeaterPortDistance": repeaterPortDistance,
       "repeaterPortSofMissing": repeaterPortSofMissing,
       "repeaterPortMCVs": repeaterPortMCVs,
       "repeaterPortZero": repeaterPortZero,
       "repeaterPortSinceZero": repeaterPortSinceZero,
       "repeaterPortAccessAction": repeaterPortAccessAction,
       "repeaterPortAccessState": repeaterPortAccessState,
       "repeaterPortAccessType": repeaterPortAccessType,
       "repeaterPortAccessAllStatus": repeaterPortAccessAllStatus,
       "repeaterPortPortLastViolationAddress": repeaterPortPortLastViolationAddress,
       "repeaterPortPortAddressViolations": repeaterPortPortAddressViolations,
       "repeaterPortSegment": repeaterPortSegment,
       "repeaterPortAccessLearn": repeaterPortAccessLearn,
       "repeaterPortEthernetRepeater": repeaterPortEthernetRepeater,
       "repeaterPortRepeatersAllowed": repeaterPortRepeatersAllowed,
       "repeaterPortGlobalSecurityAddress": repeaterPortGlobalSecurityAddress,
       "repeaterPortGlobalAddressChanges": repeaterPortGlobalAddressChanges,
       "repeaterPortPercentUtilization": repeaterPortPercentUtilization,
       "repeaterPortAccessTable": repeaterPortAccessTable,
       "repeaterPortAccessEntry": repeaterPortAccessEntry,
       "repeaterPortAccessGroupIndex": repeaterPortAccessGroupIndex,
       "repeaterPortAccessPortIndex": repeaterPortAccessPortIndex,
       "repeaterPortAccessAddress": repeaterPortAccessAddress,
       "repeaterPortAccessStatus": repeaterPortAccessStatus,
       "repeaterPortAccessGroupIndexShadow": repeaterPortAccessGroupIndexShadow,
       "repeaterPortAccessPortIndexShadow": repeaterPortAccessPortIndexShadow,
       "repeaterPortAccessAddressShadow": repeaterPortAccessAddressShadow,
       "repeaterPortAccessStatusShadow": repeaterPortAccessStatusShadow,
       "repeaterPort2Table": repeaterPort2Table,
       "repeaterPort2Entry": repeaterPort2Entry,
       "repeaterPort2RmonOctets": repeaterPort2RmonOctets,
       "repeaterPort2RmonPkts": repeaterPort2RmonPkts,
       "repeaterPort2RmonBroadcastPkts": repeaterPort2RmonBroadcastPkts,
       "repeaterPort2RmonMulticastPkts": repeaterPort2RmonMulticastPkts,
       "repeaterPort2RmonCRCAlignErrors": repeaterPort2RmonCRCAlignErrors,
       "repeaterPort2RmonPkts64Octets": repeaterPort2RmonPkts64Octets,
       "repeaterPort2RmonPkts65to127Octets": repeaterPort2RmonPkts65to127Octets,
       "repeaterPort2RmonPkts128to255Octets": repeaterPort2RmonPkts128to255Octets,
       "repeaterPort2RmonPkts256to511Octets": repeaterPort2RmonPkts256to511Octets,
       "repeaterPort2RmonPkts512to1023Octets": repeaterPort2RmonPkts512to1023Octets,
       "repeaterPort2RmonPkts1024to1518Octets": repeaterPort2RmonPkts1024to1518Octets,
       "repeaterPort2TrafficRatio": repeaterPort2TrafficRatio,
       "repeaterPort2CollisionRatio": repeaterPort2CollisionRatio,
       "repeaterPort2ErrorRatio": repeaterPort2ErrorRatio,
       "repeaterPort2BroadcastRatio": repeaterPort2BroadcastRatio,
       "repeaterPort2MulticastRatio": repeaterPort2MulticastRatio,
       "repeaterPort2UnicastRatio": repeaterPort2UnicastRatio,
       "xRepeaterSlotInfo": xRepeaterSlotInfo,
       "repeaterSlotSegmentTable": repeaterSlotSegmentTable,
       "repeaterSlotSegmentEntry": repeaterSlotSegmentEntry,
       "repeaterSlotIndex": repeaterSlotIndex,
       "repeaterSlotSegment": repeaterSlotSegment,
       "repeaterSlotSegmentStatus": repeaterSlotSegmentStatus,
       "xRepeaterSecurity": xRepeaterSecurity,
       "repeaterSecurityState": repeaterSecurityState,
       "repeaterSecurityPortTable": repeaterSecurityPortTable,
       "repeaterSecurityPortEntry": repeaterSecurityPortEntry,
       "repeaterSecurityPortUnicast": repeaterSecurityPortUnicast,
       "repeaterSecurityPortMulticast": repeaterSecurityPortMulticast,
       "repeaterSecurityPortAllStatus": repeaterSecurityPortAllStatus,
       "repeaterSecurityPortSecurityLearn": repeaterSecurityPortSecurityLearn,
       "repeaterSecurityTable": repeaterSecurityTable,
       "repeaterSecurityEntry": repeaterSecurityEntry,
       "repeaterSecurityGroupIndex": repeaterSecurityGroupIndex,
       "repeaterSecurityPortIndex": repeaterSecurityPortIndex,
       "repeaterSecurityAddress": repeaterSecurityAddress,
       "repeaterSecurityStatus": repeaterSecurityStatus,
       "repeaterSecurityAction": repeaterSecurityAction,
       "repeaterSecurityGroupIndexShadow": repeaterSecurityGroupIndexShadow,
       "repeaterSecurityPortIndexShadow": repeaterSecurityPortIndexShadow,
       "repeaterSecurityAddressShadow": repeaterSecurityAddressShadow,
       "repeaterSecurityStatusShadow": repeaterSecurityStatusShadow,
       "repeaterSecurityGlobalAddressTable": repeaterSecurityGlobalAddressTable,
       "repeaterSecurityGlobalAddressEntry": repeaterSecurityGlobalAddressEntry,
       "repeaterSecurityGlobalAddress": repeaterSecurityGlobalAddress,
       "repeaterSecurityGlobalAddressStatus": repeaterSecurityGlobalAddressStatus,
       "repeaterSecurityGlobalAddressAction": repeaterSecurityGlobalAddressAction,
       "repeaterSecurityGlobalDBID": repeaterSecurityGlobalDBID,
       "repeaterSecurityGlobalSecurityAdminState": repeaterSecurityGlobalSecurityAdminState,
       "repeaterSecurityGlobalSecurityOperState": repeaterSecurityGlobalSecurityOperState,
       "xRepeaterRepeater": xRepeaterRepeater,
       "repeaterRepeaterTable": repeaterRepeaterTable,
       "repeaterRepeaterEntry": repeaterRepeaterEntry,
       "repeaterRepeaterGroupIndex": repeaterRepeaterGroupIndex,
       "repeaterRepeaterIndex": repeaterRepeaterIndex,
       "repeaterRepeaterSegment": repeaterRepeaterSegment,
       "repeaterRepeaterReports": repeaterRepeaterReports,
       "repeaterRepeaterCollisions": repeaterRepeaterCollisions,
       "repeaterRepeaterJabbers": repeaterRepeaterJabbers,
       "repeaterRepeaterSQE": repeaterRepeaterSQE,
       "repeaterRepeaterFifoOverflows": repeaterRepeaterFifoOverflows,
       "repeaterRepeaterZero": repeaterRepeaterZero,
       "repeaterRepeaterSinceZero": repeaterRepeaterSinceZero,
       "repeaterRepeaterSegmentsAllowed": repeaterRepeaterSegmentsAllowed,
       "repeaterRepeaterTotalOctets": repeaterRepeaterTotalOctets,
       "repeaterRepeaterTotalFrames": repeaterRepeaterTotalFrames,
       "repeaterRepeaterPercentUtilization": repeaterRepeaterPercentUtilization,
       "xRepeaterRedundancy": xRepeaterRedundancy,
       "repeaterRedundancyState": repeaterRedundancyState,
       "repeaterRedundancyGroupTable": repeaterRedundancyGroupTable,
       "repeaterRedundancyGroupEntry": repeaterRedundancyGroupEntry,
       "repeaterRedundancyGroupGroupIndex": repeaterRedundancyGroupGroupIndex,
       "repeaterRedundancyGroupStatus": repeaterRedundancyGroupStatus,
       "repeaterRedundancyGroupName": repeaterRedundancyGroupName,
       "repeaterRedundancyGroupAdminState": repeaterRedundancyGroupAdminState,
       "repeaterRedundancyGroupTestInterval": repeaterRedundancyGroupTestInterval,
       "repeaterRedundancyGroupRollbackAdminState": repeaterRedundancyGroupRollbackAdminState,
       "repeaterRedundancyGroupRollbackInterval": repeaterRedundancyGroupRollbackInterval,
       "repeaterRedundancyGroupOperPath": repeaterRedundancyGroupOperPath,
       "repeaterRedundancyGroupPathChanges": repeaterRedundancyGroupPathChanges,
       "repeaterRedundancyGroupRollbackAttempts": repeaterRedundancyGroupRollbackAttempts,
       "repeaterRedundancyGroupZero": repeaterRedundancyGroupZero,
       "repeaterRedundancyGroupSinceZero": repeaterRedundancyGroupSinceZero,
       "repeaterRedundancyGroupConfigStatus": repeaterRedundancyGroupConfigStatus,
       "repeaterRedundancyPathTable": repeaterRedundancyPathTable,
       "repeaterRedundancyPathEntry": repeaterRedundancyPathEntry,
       "repeaterRedundancyPathGroupIndex": repeaterRedundancyPathGroupIndex,
       "repeaterRedundancyPathPathIndex": repeaterRedundancyPathPathIndex,
       "repeaterRedundancyPathStatus": repeaterRedundancyPathStatus,
       "repeaterRedundancyPathSlot": repeaterRedundancyPathSlot,
       "repeaterRedundancyPathPort": repeaterRedundancyPathPort,
       "repeaterRedundancyPathPriority": repeaterRedundancyPathPriority,
       "repeaterRedundancyPathActivate": repeaterRedundancyPathActivate,
       "repeaterRedundancyPathTimeout": repeaterRedundancyPathTimeout,
       "repeaterRedundancyPathRetryCount": repeaterRedundancyPathRetryCount,
       "repeaterRedundancyPathTestAttempts": repeaterRedundancyPathTestAttempts,
       "repeaterRedundancyPathLastTestStatus": repeaterRedundancyPathLastTestStatus,
       "repeaterRedundancyPathDisposition": repeaterRedundancyPathDisposition,
       "repeaterRedundancyPathConfigStatus": repeaterRedundancyPathConfigStatus,
       "repeaterRedundancyPathAdminState": repeaterRedundancyPathAdminState,
       "repeaterRedundancyAddressTable": repeaterRedundancyAddressTable,
       "repeaterRedundancyAddressEntry": repeaterRedundancyAddressEntry,
       "repeaterRedundancyAddressGroupIndex": repeaterRedundancyAddressGroupIndex,
       "repeaterRedundancyAddressPathIndex": repeaterRedundancyAddressPathIndex,
       "repeaterRedundancyAddressAddress": repeaterRedundancyAddressAddress,
       "repeaterRedundancyAddressStatus": repeaterRedundancyAddressStatus,
       "repeaterRedundancyAddressResponses": repeaterRedundancyAddressResponses,
       "repeaterRedundancyAddressLastTestStatus": repeaterRedundancyAddressLastTestStatus}
)
