# SNMP MIB module (APPIAN-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:32 2024
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

(AcAdminStatus,
 AcMibVersion,
 AcNodeArchitecture,
 AcNodeId,
 AcOpStatus,
 AcRingId,
 acOsap) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcMibVersion",
    "AcNodeArchitecture",
    "AcNodeId",
    "AcOpStatus",
    "AcRingId",
    "acOsap")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acChassis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1)
)
acChassis.setRevisions(
        ("1900-04-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AcFanStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 4),
          ("fast", 1),
          ("medium", 2),
          ("slow", 3),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_AcChassisTraps_ObjectIdentity = ObjectIdentity
acChassisTraps = _AcChassisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 0)
)
_AcGlobals_ObjectIdentity = ObjectIdentity
acGlobals = _AcGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 1)
)
_AcNodeId_Type = AcNodeId
_AcNodeId_Object = MibScalar
acNodeId = _AcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 1, 1),
    _AcNodeId_Type()
)
acNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNodeId.setStatus("current")
_AcChassisTable_Object = MibTable
acChassisTable = _AcChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2)
)
if mibBuilder.loadTexts:
    acChassisTable.setStatus("current")
_AcChassisEntry_Object = MibTableRow
acChassisEntry = _AcChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1)
)
acChassisEntry.setIndexNames(
    (0, "APPIAN-CHASSIS-MIB", "acChassisNodeId"),
)
if mibBuilder.loadTexts:
    acChassisEntry.setStatus("current")
_AcChassisNodeId_Type = AcNodeId
_AcChassisNodeId_Object = MibTableColumn
acChassisNodeId = _AcChassisNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 1),
    _AcChassisNodeId_Type()
)
acChassisNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acChassisNodeId.setStatus("current")


class _AcChassisAdminStatus_Type(AcAdminStatus):
    """Custom type acChassisAdminStatus based on AcAdminStatus"""


_AcChassisAdminStatus_Object = MibTableColumn
acChassisAdminStatus = _AcChassisAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 2),
    _AcChassisAdminStatus_Type()
)
acChassisAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisAdminStatus.setStatus("current")
_AcChassisOpStatus_Type = AcOpStatus
_AcChassisOpStatus_Object = MibTableColumn
acChassisOpStatus = _AcChassisOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 3),
    _AcChassisOpStatus_Type()
)
acChassisOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisOpStatus.setStatus("current")


class _AcChassisCfgType_Type(Integer32):
    """Custom type acChassisCfgType based on Integer32"""
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
        *(("osap-10G", 3),
          ("osap-1600", 1),
          ("osap-4800", 2),
          ("unknown", 0))
    )


_AcChassisCfgType_Type.__name__ = "Integer32"
_AcChassisCfgType_Object = MibTableColumn
acChassisCfgType = _AcChassisCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 4),
    _AcChassisCfgType_Type()
)
acChassisCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisCfgType.setStatus("current")


class _AcChassisModelNumber_Type(Integer32):
    """Custom type acChassisModelNumber based on Integer32"""
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
        *(("osap-10G", 3),
          ("osap-1600", 1),
          ("osap-4800", 2),
          ("unknown", 0))
    )


_AcChassisModelNumber_Type.__name__ = "Integer32"
_AcChassisModelNumber_Object = MibTableColumn
acChassisModelNumber = _AcChassisModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 5),
    _AcChassisModelNumber_Type()
)
acChassisModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisModelNumber.setStatus("current")


class _AcChassisSerialNumber_Type(DisplayString):
    """Custom type acChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcChassisSerialNumber_Type.__name__ = "DisplayString"
_AcChassisSerialNumber_Object = MibTableColumn
acChassisSerialNumber = _AcChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 6),
    _AcChassisSerialNumber_Type()
)
acChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisSerialNumber.setStatus("current")


class _AcChassisProductionDate_Type(DisplayString):
    """Custom type acChassisProductionDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_AcChassisProductionDate_Type.__name__ = "DisplayString"
_AcChassisProductionDate_Object = MibTableColumn
acChassisProductionDate = _AcChassisProductionDate_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 7),
    _AcChassisProductionDate_Type()
)
acChassisProductionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisProductionDate.setStatus("current")


class _AcChassisRevision_Type(Integer32):
    """Custom type acChassisRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcChassisRevision_Type.__name__ = "Integer32"
_AcChassisRevision_Object = MibTableColumn
acChassisRevision = _AcChassisRevision_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 8),
    _AcChassisRevision_Type()
)
acChassisRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisRevision.setStatus("current")


class _AcChassisTemperature_Type(Integer32):
    """Custom type acChassisTemperature based on Integer32"""
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
        *(("normal", 1),
          ("tooCold", 2),
          ("tooHot", 3),
          ("unknown", 0))
    )


_AcChassisTemperature_Type.__name__ = "Integer32"
_AcChassisTemperature_Object = MibTableColumn
acChassisTemperature = _AcChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 9),
    _AcChassisTemperature_Type()
)
acChassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisTemperature.setStatus("current")
_AcChassisFanSpeed_Type = AcFanStatus
_AcChassisFanSpeed_Object = MibTableColumn
acChassisFanSpeed = _AcChassisFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 10),
    _AcChassisFanSpeed_Type()
)
acChassisFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisFanSpeed.setStatus("current")
_AcChassisFan1Status_Type = AcFanStatus
_AcChassisFan1Status_Object = MibTableColumn
acChassisFan1Status = _AcChassisFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 11),
    _AcChassisFan1Status_Type()
)
acChassisFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisFan1Status.setStatus("current")
_AcChassisFan2Status_Type = AcFanStatus
_AcChassisFan2Status_Object = MibTableColumn
acChassisFan2Status = _AcChassisFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 12),
    _AcChassisFan2Status_Type()
)
acChassisFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisFan2Status.setStatus("current")
_AcChassisFan3Status_Type = AcFanStatus
_AcChassisFan3Status_Object = MibTableColumn
acChassisFan3Status = _AcChassisFan3Status_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 13),
    _AcChassisFan3Status_Type()
)
acChassisFan3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisFan3Status.setStatus("current")
_AcChassisFan4Status_Type = AcFanStatus
_AcChassisFan4Status_Object = MibTableColumn
acChassisFan4Status = _AcChassisFan4Status_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 14),
    _AcChassisFan4Status_Type()
)
acChassisFan4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisFan4Status.setStatus("current")
_AcChassisFan5Status_Type = AcFanStatus
_AcChassisFan5Status_Object = MibTableColumn
acChassisFan5Status = _AcChassisFan5Status_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 15),
    _AcChassisFan5Status_Type()
)
acChassisFan5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisFan5Status.setStatus("current")
_AcChassisFan6Status_Type = AcFanStatus
_AcChassisFan6Status_Object = MibTableColumn
acChassisFan6Status = _AcChassisFan6Status_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 16),
    _AcChassisFan6Status_Type()
)
acChassisFan6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisFan6Status.setStatus("current")
_AcChassisPowerAStatus_Type = AcOpStatus
_AcChassisPowerAStatus_Object = MibTableColumn
acChassisPowerAStatus = _AcChassisPowerAStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 17),
    _AcChassisPowerAStatus_Type()
)
acChassisPowerAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisPowerAStatus.setStatus("current")
_AcChassisPowerBStatus_Type = AcOpStatus
_AcChassisPowerBStatus_Object = MibTableColumn
acChassisPowerBStatus = _AcChassisPowerBStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 18),
    _AcChassisPowerBStatus_Type()
)
acChassisPowerBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisPowerBStatus.setStatus("current")


class _AcChassisContact_Type(DisplayString):
    """Custom type acChassisContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcChassisContact_Type.__name__ = "DisplayString"
_AcChassisContact_Object = MibTableColumn
acChassisContact = _AcChassisContact_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 19),
    _AcChassisContact_Type()
)
acChassisContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisContact.setStatus("current")


class _AcChassisName_Type(DisplayString):
    """Custom type acChassisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcChassisName_Type.__name__ = "DisplayString"
_AcChassisName_Object = MibTableColumn
acChassisName = _AcChassisName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 20),
    _AcChassisName_Type()
)
acChassisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisName.setStatus("current")


class _AcChassisLocation_Type(DisplayString):
    """Custom type acChassisLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcChassisLocation_Type.__name__ = "DisplayString"
_AcChassisLocation_Object = MibTableColumn
acChassisLocation = _AcChassisLocation_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 21),
    _AcChassisLocation_Type()
)
acChassisLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisLocation.setStatus("current")


class _AcChassisDescription_Type(DisplayString):
    """Custom type acChassisDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcChassisDescription_Type.__name__ = "DisplayString"
_AcChassisDescription_Object = MibTableColumn
acChassisDescription = _AcChassisDescription_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 22),
    _AcChassisDescription_Type()
)
acChassisDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisDescription.setStatus("current")


class _AcChassisMaxSlots_Type(Integer32):
    """Custom type acChassisMaxSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AcChassisMaxSlots_Type.__name__ = "Integer32"
_AcChassisMaxSlots_Object = MibTableColumn
acChassisMaxSlots = _AcChassisMaxSlots_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 23),
    _AcChassisMaxSlots_Type()
)
acChassisMaxSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisMaxSlots.setStatus("current")
_AcChassisSysUpTime_Type = TimeTicks
_AcChassisSysUpTime_Object = MibTableColumn
acChassisSysUpTime = _AcChassisSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 24),
    _AcChassisSysUpTime_Type()
)
acChassisSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisSysUpTime.setStatus("current")
_AcChassisCurrentTime_Type = DateAndTime
_AcChassisCurrentTime_Object = MibTableColumn
acChassisCurrentTime = _AcChassisCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 25),
    _AcChassisCurrentTime_Type()
)
acChassisCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisCurrentTime.setStatus("current")


class _AcChassisMaxSerialPorts_Type(Integer32):
    """Custom type acChassisMaxSerialPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcChassisMaxSerialPorts_Type.__name__ = "Integer32"
_AcChassisMaxSerialPorts_Object = MibTableColumn
acChassisMaxSerialPorts = _AcChassisMaxSerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 26),
    _AcChassisMaxSerialPorts_Type()
)
acChassisMaxSerialPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisMaxSerialPorts.setStatus("current")
_AcChassisRingId_Type = AcRingId
_AcChassisRingId_Object = MibTableColumn
acChassisRingId = _AcChassisRingId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 27),
    _AcChassisRingId_Type()
)
acChassisRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisRingId.setStatus("current")


class _AcChassisRingName_Type(DisplayString):
    """Custom type acChassisRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcChassisRingName_Type.__name__ = "DisplayString"
_AcChassisRingName_Object = MibTableColumn
acChassisRingName = _AcChassisRingName_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 28),
    _AcChassisRingName_Type()
)
acChassisRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisRingName.setStatus("current")
_AcChassisMibVersion_Type = AcMibVersion
_AcChassisMibVersion_Object = MibTableColumn
acChassisMibVersion = _AcChassisMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 29),
    _AcChassisMibVersion_Type()
)
acChassisMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisMibVersion.setStatus("current")
_AcChassisNodeArchitecture_Type = AcNodeArchitecture
_AcChassisNodeArchitecture_Object = MibTableColumn
acChassisNodeArchitecture = _AcChassisNodeArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 30),
    _AcChassisNodeArchitecture_Type()
)
acChassisNodeArchitecture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisNodeArchitecture.setStatus("current")
_AcChassisNodePoll_Type = OctetString
_AcChassisNodePoll_Object = MibTableColumn
acChassisNodePoll = _AcChassisNodePoll_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 31),
    _AcChassisNodePoll_Type()
)
acChassisNodePoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisNodePoll.setStatus("current")
_AcChassisModulePoll_Type = OctetString
_AcChassisModulePoll_Object = MibTableColumn
acChassisModulePoll = _AcChassisModulePoll_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 32),
    _AcChassisModulePoll_Type()
)
acChassisModulePoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisModulePoll.setStatus("current")
_AcChassisPortPoll_Type = OctetString
_AcChassisPortPoll_Object = MibTableColumn
acChassisPortPoll = _AcChassisPortPoll_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 33),
    _AcChassisPortPoll_Type()
)
acChassisPortPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acChassisPortPoll.setStatus("current")
_AcChassisReset_Type = TruthValue
_AcChassisReset_Object = MibTableColumn
acChassisReset = _AcChassisReset_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 34),
    _AcChassisReset_Type()
)
acChassisReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisReset.setStatus("current")


class _AcChassisTdmAccessRedundancyMode_Type(Integer32):
    """Custom type acChassisTdmAccessRedundancyMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("n-to-one", 0),
          ("one-to-one", 1))
    )


_AcChassisTdmAccessRedundancyMode_Type.__name__ = "Integer32"
_AcChassisTdmAccessRedundancyMode_Object = MibTableColumn
acChassisTdmAccessRedundancyMode = _AcChassisTdmAccessRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 2, 1, 35),
    _AcChassisTdmAccessRedundancyMode_Type()
)
acChassisTdmAccessRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acChassisTdmAccessRedundancyMode.setStatus("current")
_AcMgmtAccessTable_Object = MibTable
acMgmtAccessTable = _AcMgmtAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3)
)
if mibBuilder.loadTexts:
    acMgmtAccessTable.setStatus("current")
_AcMgmtAccessEntry_Object = MibTableRow
acMgmtAccessEntry = _AcMgmtAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1)
)
acMgmtAccessEntry.setIndexNames(
    (0, "APPIAN-CHASSIS-MIB", "acMgmtAccessNodeId"),
    (0, "APPIAN-CHASSIS-MIB", "acMgmtAccessIndex"),
)
if mibBuilder.loadTexts:
    acMgmtAccessEntry.setStatus("current")
_AcMgmtAccessNodeId_Type = AcNodeId
_AcMgmtAccessNodeId_Object = MibTableColumn
acMgmtAccessNodeId = _AcMgmtAccessNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 1),
    _AcMgmtAccessNodeId_Type()
)
acMgmtAccessNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acMgmtAccessNodeId.setStatus("current")
_AcMgmtAccessIndex_Type = Integer32
_AcMgmtAccessIndex_Object = MibTableColumn
acMgmtAccessIndex = _AcMgmtAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 2),
    _AcMgmtAccessIndex_Type()
)
acMgmtAccessIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acMgmtAccessIndex.setStatus("current")


class _AcMgmtAccessInterfaceType_Type(Integer32):
    """Custom type acMgmtAccessInterfaceType based on Integer32"""
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
        *(("appian-dcc", 2),
          ("ethernet", 1),
          ("frame-relay", 4),
          ("oob-ppp", 3),
          ("ppp", 5),
          ("sonet-1-dbg", 6),
          ("sonet-2-dbg", 7),
          ("unknown", 0))
    )


_AcMgmtAccessInterfaceType_Type.__name__ = "Integer32"
_AcMgmtAccessInterfaceType_Object = MibTableColumn
acMgmtAccessInterfaceType = _AcMgmtAccessInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 3),
    _AcMgmtAccessInterfaceType_Type()
)
acMgmtAccessInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acMgmtAccessInterfaceType.setStatus("current")
_AcMgmtAccessAdminStatus_Type = AcAdminStatus
_AcMgmtAccessAdminStatus_Object = MibTableColumn
acMgmtAccessAdminStatus = _AcMgmtAccessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 4),
    _AcMgmtAccessAdminStatus_Type()
)
acMgmtAccessAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acMgmtAccessAdminStatus.setStatus("current")
_AcMgmtAccessOpStatus_Type = AcOpStatus
_AcMgmtAccessOpStatus_Object = MibTableColumn
acMgmtAccessOpStatus = _AcMgmtAccessOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 5),
    _AcMgmtAccessOpStatus_Type()
)
acMgmtAccessOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acMgmtAccessOpStatus.setStatus("current")
_AcMgmtAccessIpAddress_Type = IpAddress
_AcMgmtAccessIpAddress_Object = MibTableColumn
acMgmtAccessIpAddress = _AcMgmtAccessIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 6),
    _AcMgmtAccessIpAddress_Type()
)
acMgmtAccessIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acMgmtAccessIpAddress.setStatus("current")


class _AcMgmtAccessIpSubnet_Type(IpAddress):
    """Custom type acMgmtAccessIpSubnet based on IpAddress"""
    defaultValue = 0


_AcMgmtAccessIpSubnet_Object = MibTableColumn
acMgmtAccessIpSubnet = _AcMgmtAccessIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 7),
    _AcMgmtAccessIpSubnet_Type()
)
acMgmtAccessIpSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acMgmtAccessIpSubnet.setStatus("current")
_AcMgmtAccessTrunk_Type = Integer32
_AcMgmtAccessTrunk_Object = MibTableColumn
acMgmtAccessTrunk = _AcMgmtAccessTrunk_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 8),
    _AcMgmtAccessTrunk_Type()
)
acMgmtAccessTrunk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acMgmtAccessTrunk.setStatus("current")


class _AcMgmtAccessFrDlci_Type(Integer32):
    """Custom type acMgmtAccessFrDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1022),
    )


_AcMgmtAccessFrDlci_Type.__name__ = "Integer32"
_AcMgmtAccessFrDlci_Object = MibTableColumn
acMgmtAccessFrDlci = _AcMgmtAccessFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 3, 1, 9),
    _AcMgmtAccessFrDlci_Type()
)
acMgmtAccessFrDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acMgmtAccessFrDlci.setStatus("current")

# Managed Objects groups


# Notification objects

acChassisCfgMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 0, 1)
)
acChassisCfgMismatchTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-CHASSIS-MIB", "acChassisNodeId"),
        ("APPIAN-CHASSIS-MIB", "acChassisModelNumber"),
        ("APPIAN-CHASSIS-MIB", "acChassisCfgType"))
)
if mibBuilder.loadTexts:
    acChassisCfgMismatchTrap.setStatus(
        "current"
    )

acChassisTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 0, 2)
)
acChassisTemperatureTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-CHASSIS-MIB", "acChassisNodeId"),
        ("APPIAN-CHASSIS-MIB", "acChassisTemperature"))
)
if mibBuilder.loadTexts:
    acChassisTemperatureTrap.setStatus(
        "current"
    )

acChassisFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 0, 3)
)
acChassisFanFailureTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-CHASSIS-MIB", "acChassisNodeId"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan1Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan2Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan3Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan4Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan5Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan6Status"))
)
if mibBuilder.loadTexts:
    acChassisFanFailureTrap.setStatus(
        "current"
    )

acChassisTemperatureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 0, 4)
)
acChassisTemperatureClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-CHASSIS-MIB", "acChassisNodeId"),
        ("APPIAN-CHASSIS-MIB", "acChassisTemperature"))
)
if mibBuilder.loadTexts:
    acChassisTemperatureClearTrap.setStatus(
        "current"
    )

acChassisFanFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 1, 0, 5)
)
acChassisFanFailureClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-CHASSIS-MIB", "acChassisNodeId"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan1Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan2Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan3Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan4Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan5Status"),
        ("APPIAN-CHASSIS-MIB", "acChassisFan6Status"))
)
if mibBuilder.loadTexts:
    acChassisFanFailureClearTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-CHASSIS-MIB",
    **{"AcFanStatus": AcFanStatus,
       "acChassis": acChassis,
       "acChassisTraps": acChassisTraps,
       "acChassisCfgMismatchTrap": acChassisCfgMismatchTrap,
       "acChassisTemperatureTrap": acChassisTemperatureTrap,
       "acChassisFanFailureTrap": acChassisFanFailureTrap,
       "acChassisTemperatureClearTrap": acChassisTemperatureClearTrap,
       "acChassisFanFailureClearTrap": acChassisFanFailureClearTrap,
       "acGlobals": acGlobals,
       "acNodeId": acNodeId,
       "acChassisTable": acChassisTable,
       "acChassisEntry": acChassisEntry,
       "acChassisNodeId": acChassisNodeId,
       "acChassisAdminStatus": acChassisAdminStatus,
       "acChassisOpStatus": acChassisOpStatus,
       "acChassisCfgType": acChassisCfgType,
       "acChassisModelNumber": acChassisModelNumber,
       "acChassisSerialNumber": acChassisSerialNumber,
       "acChassisProductionDate": acChassisProductionDate,
       "acChassisRevision": acChassisRevision,
       "acChassisTemperature": acChassisTemperature,
       "acChassisFanSpeed": acChassisFanSpeed,
       "acChassisFan1Status": acChassisFan1Status,
       "acChassisFan2Status": acChassisFan2Status,
       "acChassisFan3Status": acChassisFan3Status,
       "acChassisFan4Status": acChassisFan4Status,
       "acChassisFan5Status": acChassisFan5Status,
       "acChassisFan6Status": acChassisFan6Status,
       "acChassisPowerAStatus": acChassisPowerAStatus,
       "acChassisPowerBStatus": acChassisPowerBStatus,
       "acChassisContact": acChassisContact,
       "acChassisName": acChassisName,
       "acChassisLocation": acChassisLocation,
       "acChassisDescription": acChassisDescription,
       "acChassisMaxSlots": acChassisMaxSlots,
       "acChassisSysUpTime": acChassisSysUpTime,
       "acChassisCurrentTime": acChassisCurrentTime,
       "acChassisMaxSerialPorts": acChassisMaxSerialPorts,
       "acChassisRingId": acChassisRingId,
       "acChassisRingName": acChassisRingName,
       "acChassisMibVersion": acChassisMibVersion,
       "acChassisNodeArchitecture": acChassisNodeArchitecture,
       "acChassisNodePoll": acChassisNodePoll,
       "acChassisModulePoll": acChassisModulePoll,
       "acChassisPortPoll": acChassisPortPoll,
       "acChassisReset": acChassisReset,
       "acChassisTdmAccessRedundancyMode": acChassisTdmAccessRedundancyMode,
       "acMgmtAccessTable": acMgmtAccessTable,
       "acMgmtAccessEntry": acMgmtAccessEntry,
       "acMgmtAccessNodeId": acMgmtAccessNodeId,
       "acMgmtAccessIndex": acMgmtAccessIndex,
       "acMgmtAccessInterfaceType": acMgmtAccessInterfaceType,
       "acMgmtAccessAdminStatus": acMgmtAccessAdminStatus,
       "acMgmtAccessOpStatus": acMgmtAccessOpStatus,
       "acMgmtAccessIpAddress": acMgmtAccessIpAddress,
       "acMgmtAccessIpSubnet": acMgmtAccessIpSubnet,
       "acMgmtAccessTrunk": acMgmtAccessTrunk,
       "acMgmtAccessFrDlci": acMgmtAccessFrDlci}
)
