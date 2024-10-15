# SNMP MIB module (ITOUCH-CONCENTRATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-CONCENTRATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:09 2024
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

(Letter,) = mibBuilder.importSymbols(
    "ITOUCH-CHASSIS-MIB",
    "Letter")

(IOType,
 iTouch) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "IOType",
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

_XConcentrator_ObjectIdentity = ObjectIdentity
xConcentrator = _XConcentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 25)
)


class _ConcentratorMode_Type(Integer32):
    """Custom type concentratorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourRing", 2),
          ("twoRing", 1))
    )


_ConcentratorMode_Type.__name__ = "Integer32"
_ConcentratorMode_Object = MibScalar
concentratorMode = _ConcentratorMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 1),
    _ConcentratorMode_Type()
)
concentratorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorMode.setStatus("mandatory")


class _ConcentratorManagement_Type(Integer32):
    """Custom type concentratorManagement based on Integer32"""
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


_ConcentratorManagement_Type.__name__ = "Integer32"
_ConcentratorManagement_Object = MibScalar
concentratorManagement = _ConcentratorManagement_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 2),
    _ConcentratorManagement_Type()
)
concentratorManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorManagement.setStatus("mandatory")


class _ConcentratorBuildTopology_Type(Integer32):
    """Custom type concentratorBuildTopology based on Integer32"""
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


_ConcentratorBuildTopology_Type.__name__ = "Integer32"
_ConcentratorBuildTopology_Object = MibScalar
concentratorBuildTopology = _ConcentratorBuildTopology_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 3),
    _ConcentratorBuildTopology_Type()
)
concentratorBuildTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorBuildTopology.setStatus("mandatory")
_ConcentratorTopologyLastBuild_Type = TimeTicks
_ConcentratorTopologyLastBuild_Object = MibScalar
concentratorTopologyLastBuild = _ConcentratorTopologyLastBuild_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 4),
    _ConcentratorTopologyLastBuild_Type()
)
concentratorTopologyLastBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorTopologyLastBuild.setStatus("mandatory")


class _ConcentratorChassisRingDefaults_Type(Integer32):
    """Custom type concentratorChassisRingDefaults based on Integer32"""
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


_ConcentratorChassisRingDefaults_Type.__name__ = "Integer32"
_ConcentratorChassisRingDefaults_Object = MibScalar
concentratorChassisRingDefaults = _ConcentratorChassisRingDefaults_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 5),
    _ConcentratorChassisRingDefaults_Type()
)
concentratorChassisRingDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorChassisRingDefaults.setStatus("mandatory")
_ConcentratorSlotTable_Object = MibTable
concentratorSlotTable = _ConcentratorSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6)
)
if mibBuilder.loadTexts:
    concentratorSlotTable.setStatus("mandatory")
_ConcentratorSlotEntry_Object = MibTableRow
concentratorSlotEntry = _ConcentratorSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6, 1)
)
concentratorSlotEntry.setIndexNames(
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorSlotIndex"),
)
if mibBuilder.loadTexts:
    concentratorSlotEntry.setStatus("mandatory")
_ConcentratorSlotIndex_Type = Integer32
_ConcentratorSlotIndex_Object = MibTableColumn
concentratorSlotIndex = _ConcentratorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6, 1, 1),
    _ConcentratorSlotIndex_Type()
)
concentratorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotIndex.setStatus("mandatory")
_ConcentratorSlotIOType_Type = IOType
_ConcentratorSlotIOType_Object = MibTableColumn
concentratorSlotIOType = _ConcentratorSlotIOType_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6, 1, 2),
    _ConcentratorSlotIOType_Type()
)
concentratorSlotIOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotIOType.setStatus("mandatory")
_ConcentratorSlotIOFirmwareVersion_Type = Integer32
_ConcentratorSlotIOFirmwareVersion_Object = MibTableColumn
concentratorSlotIOFirmwareVersion = _ConcentratorSlotIOFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6, 1, 3),
    _ConcentratorSlotIOFirmwareVersion_Type()
)
concentratorSlotIOFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotIOFirmwareVersion.setStatus("mandatory")


class _ConcentratorSlotIOOperStatus_Type(Integer32):
    """Custom type concentratorSlotIOOperStatus based on Integer32"""
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


_ConcentratorSlotIOOperStatus_Type.__name__ = "Integer32"
_ConcentratorSlotIOOperStatus_Object = MibTableColumn
concentratorSlotIOOperStatus = _ConcentratorSlotIOOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6, 1, 4),
    _ConcentratorSlotIOOperStatus_Type()
)
concentratorSlotIOOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotIOOperStatus.setStatus("mandatory")
_ConcentratorSlotUptime_Type = TimeTicks
_ConcentratorSlotUptime_Object = MibTableColumn
concentratorSlotUptime = _ConcentratorSlotUptime_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6, 1, 5),
    _ConcentratorSlotUptime_Type()
)
concentratorSlotUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotUptime.setStatus("mandatory")
_ConcentratorSlotNumPorts_Type = Integer32
_ConcentratorSlotNumPorts_Object = MibTableColumn
concentratorSlotNumPorts = _ConcentratorSlotNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 6, 1, 6),
    _ConcentratorSlotNumPorts_Type()
)
concentratorSlotNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotNumPorts.setStatus("mandatory")
_ConcentratorSlotRingTable_Object = MibTable
concentratorSlotRingTable = _ConcentratorSlotRingTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7)
)
if mibBuilder.loadTexts:
    concentratorSlotRingTable.setStatus("mandatory")
_ConcentratorSlotRingEntry_Object = MibTableRow
concentratorSlotRingEntry = _ConcentratorSlotRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1)
)
concentratorSlotRingEntry.setIndexNames(
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorSlotIndex"),
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorSlotRingIndex"),
)
if mibBuilder.loadTexts:
    concentratorSlotRingEntry.setStatus("mandatory")
_ConcentratorSlotSlotIndex_Type = Integer32
_ConcentratorSlotSlotIndex_Object = MibTableColumn
concentratorSlotSlotIndex = _ConcentratorSlotSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 1),
    _ConcentratorSlotSlotIndex_Type()
)
concentratorSlotSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotSlotIndex.setStatus("mandatory")
_ConcentratorSlotRingIndex_Type = Integer32
_ConcentratorSlotRingIndex_Object = MibTableColumn
concentratorSlotRingIndex = _ConcentratorSlotRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 2),
    _ConcentratorSlotRingIndex_Type()
)
concentratorSlotRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotRingIndex.setStatus("mandatory")


class _ConcentratorSlotRingAdminName_Type(DisplayString):
    """Custom type concentratorSlotRingAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConcentratorSlotRingAdminName_Type.__name__ = "DisplayString"
_ConcentratorSlotRingAdminName_Object = MibTableColumn
concentratorSlotRingAdminName = _ConcentratorSlotRingAdminName_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 3),
    _ConcentratorSlotRingAdminName_Type()
)
concentratorSlotRingAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorSlotRingAdminName.setStatus("mandatory")


class _ConcentratorSlotRingAdminSpeed_Type(Integer32):
    """Custom type concentratorSlotRingAdminSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 2),
          ("mbps4", 1))
    )


_ConcentratorSlotRingAdminSpeed_Type.__name__ = "Integer32"
_ConcentratorSlotRingAdminSpeed_Object = MibTableColumn
concentratorSlotRingAdminSpeed = _ConcentratorSlotRingAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 4),
    _ConcentratorSlotRingAdminSpeed_Type()
)
concentratorSlotRingAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorSlotRingAdminSpeed.setStatus("mandatory")


class _ConcentratorSlotRingAdminState_Type(Integer32):
    """Custom type concentratorSlotRingAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 2),
          ("isolated", 1))
    )


_ConcentratorSlotRingAdminState_Type.__name__ = "Integer32"
_ConcentratorSlotRingAdminState_Object = MibTableColumn
concentratorSlotRingAdminState = _ConcentratorSlotRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 5),
    _ConcentratorSlotRingAdminState_Type()
)
concentratorSlotRingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorSlotRingAdminState.setStatus("mandatory")


class _ConcentratorSlotRingZero_Type(Integer32):
    """Custom type concentratorSlotRingZero based on Integer32"""
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


_ConcentratorSlotRingZero_Type.__name__ = "Integer32"
_ConcentratorSlotRingZero_Object = MibTableColumn
concentratorSlotRingZero = _ConcentratorSlotRingZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 6),
    _ConcentratorSlotRingZero_Type()
)
concentratorSlotRingZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorSlotRingZero.setStatus("mandatory")
_ConcentratorSlotRingSinceZero_Type = TimeTicks
_ConcentratorSlotRingSinceZero_Object = MibTableColumn
concentratorSlotRingSinceZero = _ConcentratorSlotRingSinceZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 7),
    _ConcentratorSlotRingSinceZero_Type()
)
concentratorSlotRingSinceZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotRingSinceZero.setStatus("mandatory")
_ConcentratorSlotRingChassisRing_Type = Letter
_ConcentratorSlotRingChassisRing_Object = MibTableColumn
concentratorSlotRingChassisRing = _ConcentratorSlotRingChassisRing_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 8),
    _ConcentratorSlotRingChassisRing_Type()
)
concentratorSlotRingChassisRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorSlotRingChassisRing.setStatus("mandatory")


class _ConcentratorSlotRingOperName_Type(DisplayString):
    """Custom type concentratorSlotRingOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConcentratorSlotRingOperName_Type.__name__ = "DisplayString"
_ConcentratorSlotRingOperName_Object = MibTableColumn
concentratorSlotRingOperName = _ConcentratorSlotRingOperName_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 9),
    _ConcentratorSlotRingOperName_Type()
)
concentratorSlotRingOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotRingOperName.setStatus("mandatory")


class _ConcentratorSlotRingOperSpeed_Type(Integer32):
    """Custom type concentratorSlotRingOperSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 2),
          ("mbps4", 1))
    )


_ConcentratorSlotRingOperSpeed_Type.__name__ = "Integer32"
_ConcentratorSlotRingOperSpeed_Object = MibTableColumn
concentratorSlotRingOperSpeed = _ConcentratorSlotRingOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 10),
    _ConcentratorSlotRingOperSpeed_Type()
)
concentratorSlotRingOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotRingOperSpeed.setStatus("mandatory")


class _ConcentratorSlotRingOperState_Type(Integer32):
    """Custom type concentratorSlotRingOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 2),
          ("isolated", 1))
    )


_ConcentratorSlotRingOperState_Type.__name__ = "Integer32"
_ConcentratorSlotRingOperState_Object = MibTableColumn
concentratorSlotRingOperState = _ConcentratorSlotRingOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 11),
    _ConcentratorSlotRingOperState_Type()
)
concentratorSlotRingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotRingOperState.setStatus("mandatory")
_ConcentratorSlotRingChassisRingsAllowed_Type = OctetString
_ConcentratorSlotRingChassisRingsAllowed_Object = MibTableColumn
concentratorSlotRingChassisRingsAllowed = _ConcentratorSlotRingChassisRingsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 7, 1, 12),
    _ConcentratorSlotRingChassisRingsAllowed_Type()
)
concentratorSlotRingChassisRingsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSlotRingChassisRingsAllowed.setStatus("mandatory")
_ConcentratorChassisRingTable_Object = MibTable
concentratorChassisRingTable = _ConcentratorChassisRingTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8)
)
if mibBuilder.loadTexts:
    concentratorChassisRingTable.setStatus("mandatory")
_ConcentratorChassisRingEntry_Object = MibTableRow
concentratorChassisRingEntry = _ConcentratorChassisRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8, 1)
)
concentratorChassisRingEntry.setIndexNames(
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorChassisRingIndex"),
)
if mibBuilder.loadTexts:
    concentratorChassisRingEntry.setStatus("mandatory")
_ConcentratorChassisRingIndex_Type = Letter
_ConcentratorChassisRingIndex_Object = MibTableColumn
concentratorChassisRingIndex = _ConcentratorChassisRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8, 1, 1),
    _ConcentratorChassisRingIndex_Type()
)
concentratorChassisRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingIndex.setStatus("mandatory")


class _ConcentratorChassisRingName_Type(DisplayString):
    """Custom type concentratorChassisRingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ConcentratorChassisRingName_Type.__name__ = "DisplayString"
_ConcentratorChassisRingName_Object = MibTableColumn
concentratorChassisRingName = _ConcentratorChassisRingName_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8, 1, 2),
    _ConcentratorChassisRingName_Type()
)
concentratorChassisRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorChassisRingName.setStatus("mandatory")


class _ConcentratorChassisRingSpeed_Type(Integer32):
    """Custom type concentratorChassisRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 2),
          ("mbps4", 1))
    )


_ConcentratorChassisRingSpeed_Type.__name__ = "Integer32"
_ConcentratorChassisRingSpeed_Object = MibTableColumn
concentratorChassisRingSpeed = _ConcentratorChassisRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8, 1, 3),
    _ConcentratorChassisRingSpeed_Type()
)
concentratorChassisRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorChassisRingSpeed.setStatus("mandatory")
_ConcentratorChassisRingTopologyChanges_Type = Counter32
_ConcentratorChassisRingTopologyChanges_Object = MibTableColumn
concentratorChassisRingTopologyChanges = _ConcentratorChassisRingTopologyChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8, 1, 4),
    _ConcentratorChassisRingTopologyChanges_Type()
)
concentratorChassisRingTopologyChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyChanges.setStatus("mandatory")


class _ConcentratorChassisRingZero_Type(Integer32):
    """Custom type concentratorChassisRingZero based on Integer32"""
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


_ConcentratorChassisRingZero_Type.__name__ = "Integer32"
_ConcentratorChassisRingZero_Object = MibTableColumn
concentratorChassisRingZero = _ConcentratorChassisRingZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8, 1, 5),
    _ConcentratorChassisRingZero_Type()
)
concentratorChassisRingZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorChassisRingZero.setStatus("mandatory")
_ConcentratorChassisRingSinceZero_Type = TimeTicks
_ConcentratorChassisRingSinceZero_Object = MibTableColumn
concentratorChassisRingSinceZero = _ConcentratorChassisRingSinceZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 8, 1, 6),
    _ConcentratorChassisRingSinceZero_Type()
)
concentratorChassisRingSinceZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingSinceZero.setStatus("mandatory")
_ConcentratorChassisRingTopologyTable_Object = MibTable
concentratorChassisRingTopologyTable = _ConcentratorChassisRingTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9)
)
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyTable.setStatus("mandatory")
_ConcentratorChassisRingTopologyEntry_Object = MibTableRow
concentratorChassisRingTopologyEntry = _ConcentratorChassisRingTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1)
)
concentratorChassisRingTopologyEntry.setIndexNames(
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorChassisRingTopologySlotIndex"),
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorChassisRingTopologyRingIndex"),
)
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyEntry.setStatus("mandatory")
_ConcentratorChassisRingTopologySlotIndex_Type = Integer32
_ConcentratorChassisRingTopologySlotIndex_Object = MibTableColumn
concentratorChassisRingTopologySlotIndex = _ConcentratorChassisRingTopologySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 1),
    _ConcentratorChassisRingTopologySlotIndex_Type()
)
concentratorChassisRingTopologySlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologySlotIndex.setStatus("mandatory")
_ConcentratorChassisRingTopologyRingIndex_Type = Letter
_ConcentratorChassisRingTopologyRingIndex_Object = MibTableColumn
concentratorChassisRingTopologyRingIndex = _ConcentratorChassisRingTopologyRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 2),
    _ConcentratorChassisRingTopologyRingIndex_Type()
)
concentratorChassisRingTopologyRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyRingIndex.setStatus("mandatory")


class _ConcentratorChassisRingTopologyWrapUp_Type(Integer32):
    """Custom type concentratorChassisRingTopologyWrapUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unwrap", 1),
          ("wrap", 2))
    )


_ConcentratorChassisRingTopologyWrapUp_Type.__name__ = "Integer32"
_ConcentratorChassisRingTopologyWrapUp_Object = MibTableColumn
concentratorChassisRingTopologyWrapUp = _ConcentratorChassisRingTopologyWrapUp_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 3),
    _ConcentratorChassisRingTopologyWrapUp_Type()
)
concentratorChassisRingTopologyWrapUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyWrapUp.setStatus("mandatory")


class _ConcentratorChassisRingTopologyWrapDown_Type(Integer32):
    """Custom type concentratorChassisRingTopologyWrapDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unwrap", 1),
          ("wrap", 2))
    )


_ConcentratorChassisRingTopologyWrapDown_Type.__name__ = "Integer32"
_ConcentratorChassisRingTopologyWrapDown_Object = MibTableColumn
concentratorChassisRingTopologyWrapDown = _ConcentratorChassisRingTopologyWrapDown_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 4),
    _ConcentratorChassisRingTopologyWrapDown_Type()
)
concentratorChassisRingTopologyWrapDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyWrapDown.setStatus("mandatory")


class _ConcentratorChassisRingTopologyUpState_Type(Integer32):
    """Custom type concentratorChassisRingTopologyUpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ConcentratorChassisRingTopologyUpState_Type.__name__ = "Integer32"
_ConcentratorChassisRingTopologyUpState_Object = MibTableColumn
concentratorChassisRingTopologyUpState = _ConcentratorChassisRingTopologyUpState_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 5),
    _ConcentratorChassisRingTopologyUpState_Type()
)
concentratorChassisRingTopologyUpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyUpState.setStatus("mandatory")


class _ConcentratorChassisRingTopologyDownState_Type(Integer32):
    """Custom type concentratorChassisRingTopologyDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_ConcentratorChassisRingTopologyDownState_Type.__name__ = "Integer32"
_ConcentratorChassisRingTopologyDownState_Object = MibTableColumn
concentratorChassisRingTopologyDownState = _ConcentratorChassisRingTopologyDownState_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 6),
    _ConcentratorChassisRingTopologyDownState_Type()
)
concentratorChassisRingTopologyDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyDownState.setStatus("mandatory")
_ConcentratorChassisRingTopologySegment_Type = Integer32
_ConcentratorChassisRingTopologySegment_Object = MibTableColumn
concentratorChassisRingTopologySegment = _ConcentratorChassisRingTopologySegment_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 7),
    _ConcentratorChassisRingTopologySegment_Type()
)
concentratorChassisRingTopologySegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologySegment.setStatus("mandatory")


class _ConcentratorChassisRingTopologyName_Type(DisplayString):
    """Custom type concentratorChassisRingTopologyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConcentratorChassisRingTopologyName_Type.__name__ = "DisplayString"
_ConcentratorChassisRingTopologyName_Object = MibTableColumn
concentratorChassisRingTopologyName = _ConcentratorChassisRingTopologyName_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 8),
    _ConcentratorChassisRingTopologyName_Type()
)
concentratorChassisRingTopologyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyName.setStatus("mandatory")


class _ConcentratorChassisRingTopologySpeed_Type(Integer32):
    """Custom type concentratorChassisRingTopologySpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbps16", 2),
          ("mbps4", 1))
    )


_ConcentratorChassisRingTopologySpeed_Type.__name__ = "Integer32"
_ConcentratorChassisRingTopologySpeed_Object = MibTableColumn
concentratorChassisRingTopologySpeed = _ConcentratorChassisRingTopologySpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 9),
    _ConcentratorChassisRingTopologySpeed_Type()
)
concentratorChassisRingTopologySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologySpeed.setStatus("mandatory")
_ConcentratorChassisRingTopologyCardType_Type = IOType
_ConcentratorChassisRingTopologyCardType_Object = MibTableColumn
concentratorChassisRingTopologyCardType = _ConcentratorChassisRingTopologyCardType_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 10),
    _ConcentratorChassisRingTopologyCardType_Type()
)
concentratorChassisRingTopologyCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyCardType.setStatus("mandatory")
_ConcentratorChassisRingTopologyAutoUpChanges_Type = Counter32
_ConcentratorChassisRingTopologyAutoUpChanges_Object = MibTableColumn
concentratorChassisRingTopologyAutoUpChanges = _ConcentratorChassisRingTopologyAutoUpChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 11),
    _ConcentratorChassisRingTopologyAutoUpChanges_Type()
)
concentratorChassisRingTopologyAutoUpChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyAutoUpChanges.setStatus("mandatory")
_ConcentratorChassisRingTopologyAutoDownChanges_Type = Counter32
_ConcentratorChassisRingTopologyAutoDownChanges_Object = MibTableColumn
concentratorChassisRingTopologyAutoDownChanges = _ConcentratorChassisRingTopologyAutoDownChanges_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 9, 1, 12),
    _ConcentratorChassisRingTopologyAutoDownChanges_Type()
)
concentratorChassisRingTopologyAutoDownChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorChassisRingTopologyAutoDownChanges.setStatus("mandatory")
_ConcentratorPortTable_Object = MibTable
concentratorPortTable = _ConcentratorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10)
)
if mibBuilder.loadTexts:
    concentratorPortTable.setStatus("mandatory")
_ConcentratorPortEntry_Object = MibTableRow
concentratorPortEntry = _ConcentratorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1)
)
concentratorPortEntry.setIndexNames(
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorSlotIndex"),
    (0, "ITOUCH-CONCENTRATOR-MIB", "concentratorPortIndex"),
)
if mibBuilder.loadTexts:
    concentratorPortEntry.setStatus("mandatory")
_ConcentratorPortSlotIndex_Type = Integer32
_ConcentratorPortSlotIndex_Object = MibTableColumn
concentratorPortSlotIndex = _ConcentratorPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 1),
    _ConcentratorPortSlotIndex_Type()
)
concentratorPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortSlotIndex.setStatus("mandatory")
_ConcentratorPortIndex_Type = Integer32
_ConcentratorPortIndex_Object = MibTableColumn
concentratorPortIndex = _ConcentratorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 2),
    _ConcentratorPortIndex_Type()
)
concentratorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortIndex.setStatus("mandatory")


class _ConcentratorPortName_Type(DisplayString):
    """Custom type concentratorPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConcentratorPortName_Type.__name__ = "DisplayString"
_ConcentratorPortName_Object = MibTableColumn
concentratorPortName = _ConcentratorPortName_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 3),
    _ConcentratorPortName_Type()
)
concentratorPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorPortName.setStatus("mandatory")


class _ConcentratorPortType_Type(Integer32):
    """Custom type concentratorPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 2),
          ("rj45", 1))
    )


_ConcentratorPortType_Type.__name__ = "Integer32"
_ConcentratorPortType_Object = MibTableColumn
concentratorPortType = _ConcentratorPortType_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 4),
    _ConcentratorPortType_Type()
)
concentratorPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortType.setStatus("mandatory")


class _ConcentratorPortZero_Type(Integer32):
    """Custom type concentratorPortZero based on Integer32"""
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


_ConcentratorPortZero_Type.__name__ = "Integer32"
_ConcentratorPortZero_Object = MibTableColumn
concentratorPortZero = _ConcentratorPortZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 5),
    _ConcentratorPortZero_Type()
)
concentratorPortZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorPortZero.setStatus("mandatory")
_ConcentratorPortSinceZero_Type = TimeTicks
_ConcentratorPortSinceZero_Object = MibTableColumn
concentratorPortSinceZero = _ConcentratorPortSinceZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 6),
    _ConcentratorPortSinceZero_Type()
)
concentratorPortSinceZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortSinceZero.setStatus("mandatory")


class _ConcentratorPortAdminState_Type(Integer32):
    """Custom type concentratorPortAdminState based on Integer32"""
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


_ConcentratorPortAdminState_Type.__name__ = "Integer32"
_ConcentratorPortAdminState_Object = MibTableColumn
concentratorPortAdminState = _ConcentratorPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 7),
    _ConcentratorPortAdminState_Type()
)
concentratorPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorPortAdminState.setStatus("mandatory")


class _ConcentratorPortOperState_Type(Integer32):
    """Custom type concentratorPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("notInserted", 2),
          ("rateMismatch", 3))
    )


_ConcentratorPortOperState_Type.__name__ = "Integer32"
_ConcentratorPortOperState_Object = MibTableColumn
concentratorPortOperState = _ConcentratorPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 8),
    _ConcentratorPortOperState_Type()
)
concentratorPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortOperState.setStatus("mandatory")
_ConcentratorPortInsertions_Type = Counter32
_ConcentratorPortInsertions_Object = MibTableColumn
concentratorPortInsertions = _ConcentratorPortInsertions_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 9),
    _ConcentratorPortInsertions_Type()
)
concentratorPortInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortInsertions.setStatus("mandatory")
_ConcentratorPortInsertFailures_Type = Counter32
_ConcentratorPortInsertFailures_Object = MibTableColumn
concentratorPortInsertFailures = _ConcentratorPortInsertFailures_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 10),
    _ConcentratorPortInsertFailures_Type()
)
concentratorPortInsertFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortInsertFailures.setStatus("mandatory")


class _ConcentratorPortAdminInsert_Type(Integer32):
    """Custom type concentratorPortAdminInsert based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("ring1", 2),
          ("ring10", 11),
          ("ring2", 3),
          ("ring3", 4),
          ("ring4", 5),
          ("ring5", 6),
          ("ring6", 7),
          ("ring7", 8),
          ("ring8", 9),
          ("ring9", 10))
    )


_ConcentratorPortAdminInsert_Type.__name__ = "Integer32"
_ConcentratorPortAdminInsert_Object = MibTableColumn
concentratorPortAdminInsert = _ConcentratorPortAdminInsert_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 11),
    _ConcentratorPortAdminInsert_Type()
)
concentratorPortAdminInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorPortAdminInsert.setStatus("mandatory")


class _ConcentratorPortOperInsert_Type(Integer32):
    """Custom type concentratorPortOperInsert based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("notInserted", 1),
          ("ring1", 2),
          ("ring10", 11),
          ("ring2", 3),
          ("ring3", 4),
          ("ring4", 5),
          ("ring5", 6),
          ("ring6", 7),
          ("ring7", 8),
          ("ring8", 9),
          ("ring9", 10))
    )


_ConcentratorPortOperInsert_Type.__name__ = "Integer32"
_ConcentratorPortOperInsert_Object = MibTableColumn
concentratorPortOperInsert = _ConcentratorPortOperInsert_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 12),
    _ConcentratorPortOperInsert_Type()
)
concentratorPortOperInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortOperInsert.setStatus("mandatory")


class _ConcentratorPortSpeed_Type(Integer32):
    """Custom type concentratorPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mbs16", 2),
          ("mbs4", 1))
    )


_ConcentratorPortSpeed_Type.__name__ = "Integer32"
_ConcentratorPortSpeed_Object = MibTableColumn
concentratorPortSpeed = _ConcentratorPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 13),
    _ConcentratorPortSpeed_Type()
)
concentratorPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortSpeed.setStatus("mandatory")


class _ConcentratorPortAdminLoopback_Type(Integer32):
    """Custom type concentratorPortAdminLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("loopback", 2))
    )


_ConcentratorPortAdminLoopback_Type.__name__ = "Integer32"
_ConcentratorPortAdminLoopback_Object = MibTableColumn
concentratorPortAdminLoopback = _ConcentratorPortAdminLoopback_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 14),
    _ConcentratorPortAdminLoopback_Type()
)
concentratorPortAdminLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorPortAdminLoopback.setStatus("mandatory")


class _ConcentratorPortStationType_Type(Integer32):
    """Custom type concentratorPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("station", 1),
          ("trunk", 2))
    )


_ConcentratorPortStationType_Type.__name__ = "Integer32"
_ConcentratorPortStationType_Object = MibTableColumn
concentratorPortStationType = _ConcentratorPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 15),
    _ConcentratorPortStationType_Type()
)
concentratorPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorPortStationType.setStatus("mandatory")


class _ConcentratorPortAdminTrunkInsert_Type(Integer32):
    """Custom type concentratorPortAdminTrunkInsert based on Integer32"""
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


_ConcentratorPortAdminTrunkInsert_Type.__name__ = "Integer32"
_ConcentratorPortAdminTrunkInsert_Object = MibTableColumn
concentratorPortAdminTrunkInsert = _ConcentratorPortAdminTrunkInsert_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 16),
    _ConcentratorPortAdminTrunkInsert_Type()
)
concentratorPortAdminTrunkInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorPortAdminTrunkInsert.setStatus("mandatory")
_ConcentratorPortSlotRingsAllowed_Type = OctetString
_ConcentratorPortSlotRingsAllowed_Object = MibTableColumn
concentratorPortSlotRingsAllowed = _ConcentratorPortSlotRingsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 33, 25, 10, 1, 17),
    _ConcentratorPortSlotRingsAllowed_Type()
)
concentratorPortSlotRingsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPortSlotRingsAllowed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-CONCENTRATOR-MIB",
    **{"xConcentrator": xConcentrator,
       "concentratorMode": concentratorMode,
       "concentratorManagement": concentratorManagement,
       "concentratorBuildTopology": concentratorBuildTopology,
       "concentratorTopologyLastBuild": concentratorTopologyLastBuild,
       "concentratorChassisRingDefaults": concentratorChassisRingDefaults,
       "concentratorSlotTable": concentratorSlotTable,
       "concentratorSlotEntry": concentratorSlotEntry,
       "concentratorSlotIndex": concentratorSlotIndex,
       "concentratorSlotIOType": concentratorSlotIOType,
       "concentratorSlotIOFirmwareVersion": concentratorSlotIOFirmwareVersion,
       "concentratorSlotIOOperStatus": concentratorSlotIOOperStatus,
       "concentratorSlotUptime": concentratorSlotUptime,
       "concentratorSlotNumPorts": concentratorSlotNumPorts,
       "concentratorSlotRingTable": concentratorSlotRingTable,
       "concentratorSlotRingEntry": concentratorSlotRingEntry,
       "concentratorSlotSlotIndex": concentratorSlotSlotIndex,
       "concentratorSlotRingIndex": concentratorSlotRingIndex,
       "concentratorSlotRingAdminName": concentratorSlotRingAdminName,
       "concentratorSlotRingAdminSpeed": concentratorSlotRingAdminSpeed,
       "concentratorSlotRingAdminState": concentratorSlotRingAdminState,
       "concentratorSlotRingZero": concentratorSlotRingZero,
       "concentratorSlotRingSinceZero": concentratorSlotRingSinceZero,
       "concentratorSlotRingChassisRing": concentratorSlotRingChassisRing,
       "concentratorSlotRingOperName": concentratorSlotRingOperName,
       "concentratorSlotRingOperSpeed": concentratorSlotRingOperSpeed,
       "concentratorSlotRingOperState": concentratorSlotRingOperState,
       "concentratorSlotRingChassisRingsAllowed": concentratorSlotRingChassisRingsAllowed,
       "concentratorChassisRingTable": concentratorChassisRingTable,
       "concentratorChassisRingEntry": concentratorChassisRingEntry,
       "concentratorChassisRingIndex": concentratorChassisRingIndex,
       "concentratorChassisRingName": concentratorChassisRingName,
       "concentratorChassisRingSpeed": concentratorChassisRingSpeed,
       "concentratorChassisRingTopologyChanges": concentratorChassisRingTopologyChanges,
       "concentratorChassisRingZero": concentratorChassisRingZero,
       "concentratorChassisRingSinceZero": concentratorChassisRingSinceZero,
       "concentratorChassisRingTopologyTable": concentratorChassisRingTopologyTable,
       "concentratorChassisRingTopologyEntry": concentratorChassisRingTopologyEntry,
       "concentratorChassisRingTopologySlotIndex": concentratorChassisRingTopologySlotIndex,
       "concentratorChassisRingTopologyRingIndex": concentratorChassisRingTopologyRingIndex,
       "concentratorChassisRingTopologyWrapUp": concentratorChassisRingTopologyWrapUp,
       "concentratorChassisRingTopologyWrapDown": concentratorChassisRingTopologyWrapDown,
       "concentratorChassisRingTopologyUpState": concentratorChassisRingTopologyUpState,
       "concentratorChassisRingTopologyDownState": concentratorChassisRingTopologyDownState,
       "concentratorChassisRingTopologySegment": concentratorChassisRingTopologySegment,
       "concentratorChassisRingTopologyName": concentratorChassisRingTopologyName,
       "concentratorChassisRingTopologySpeed": concentratorChassisRingTopologySpeed,
       "concentratorChassisRingTopologyCardType": concentratorChassisRingTopologyCardType,
       "concentratorChassisRingTopologyAutoUpChanges": concentratorChassisRingTopologyAutoUpChanges,
       "concentratorChassisRingTopologyAutoDownChanges": concentratorChassisRingTopologyAutoDownChanges,
       "concentratorPortTable": concentratorPortTable,
       "concentratorPortEntry": concentratorPortEntry,
       "concentratorPortSlotIndex": concentratorPortSlotIndex,
       "concentratorPortIndex": concentratorPortIndex,
       "concentratorPortName": concentratorPortName,
       "concentratorPortType": concentratorPortType,
       "concentratorPortZero": concentratorPortZero,
       "concentratorPortSinceZero": concentratorPortSinceZero,
       "concentratorPortAdminState": concentratorPortAdminState,
       "concentratorPortOperState": concentratorPortOperState,
       "concentratorPortInsertions": concentratorPortInsertions,
       "concentratorPortInsertFailures": concentratorPortInsertFailures,
       "concentratorPortAdminInsert": concentratorPortAdminInsert,
       "concentratorPortOperInsert": concentratorPortOperInsert,
       "concentratorPortSpeed": concentratorPortSpeed,
       "concentratorPortAdminLoopback": concentratorPortAdminLoopback,
       "concentratorPortStationType": concentratorPortStationType,
       "concentratorPortAdminTrunkInsert": concentratorPortAdminTrunkInsert,
       "concentratorPortSlotRingsAllowed": concentratorPortSlotRingsAllowed}
)
