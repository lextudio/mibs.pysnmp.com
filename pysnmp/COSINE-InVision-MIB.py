# SNMP MIB module (COSINE-InVision-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COSINE-InVision-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:07 2024
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

(csInVisionMIB,
 csModules,
 csOrionMIB) = mibBuilder.importSymbols(
    "COSINE-GLOBAL-REG",
    "csInVisionMIB",
    "csModules",
    "csOrionMIB")

(csOrionBladeType,
 csOrionRestoreNumVRs,
 csOrionRestoreSlotIndex,
 csOrionSystemIpAddress) = mibBuilder.importSymbols(
    "COSINE-ORION-MIB",
    "csOrionBladeType",
    "csOrionRestoreNumVRs",
    "csOrionRestoreSlotIndex",
    "csOrionSystemIpAddress")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cosineInVisionMod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 1, 1, 3)
)
cosineInVisionMod.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CsInVisionEvents_ObjectIdentity = ObjectIdentity
csInVisionEvents = _CsInVisionEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1)
)
_CsInVisionEventsInfo_ObjectIdentity = ObjectIdentity
csInVisionEventsInfo = _CsInVisionEventsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1)
)
_CsInVisionBladeInfo_ObjectIdentity = ObjectIdentity
csInVisionBladeInfo = _CsInVisionBladeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2)
)
_CsInVisionBladeTable_Object = MibTable
csInVisionBladeTable = _CsInVisionBladeTable_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    csInVisionBladeTable.setStatus("current")
_CsInVisionBladeEntry_Object = MibTableRow
csInVisionBladeEntry = _CsInVisionBladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1)
)
csInVisionBladeEntry.setIndexNames(
    (0, "COSINE-InVision-MIB", "csInVisionBladeSlotLocation"),
)
if mibBuilder.loadTexts:
    csInVisionBladeEntry.setStatus("current")


class _CsInVisionBladeSlotLocation_Type(Integer32):
    """Custom type csInVisionBladeSlotLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_CsInVisionBladeSlotLocation_Type.__name__ = "Integer32"
_CsInVisionBladeSlotLocation_Object = MibTableColumn
csInVisionBladeSlotLocation = _CsInVisionBladeSlotLocation_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 1),
    _CsInVisionBladeSlotLocation_Type()
)
csInVisionBladeSlotLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csInVisionBladeSlotLocation.setStatus("current")


class _CsInVisionBladeDescr_Type(DisplayString):
    """Custom type csInVisionBladeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsInVisionBladeDescr_Type.__name__ = "DisplayString"
_CsInVisionBladeDescr_Object = MibTableColumn
csInVisionBladeDescr = _CsInVisionBladeDescr_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 2),
    _CsInVisionBladeDescr_Type()
)
csInVisionBladeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladeDescr.setStatus("current")


class _CsInVisionBladeType_Type(Integer32):
    """Custom type csInVisionBladeType based on Integer32"""
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
        *(("control", 2),
          ("ds3Unchannelized", 4),
          ("ds3channelized", 5),
          ("ethernet", 3),
          ("oc3Atm", 6),
          ("oc3Pos", 7),
          ("process", 1))
    )


_CsInVisionBladeType_Type.__name__ = "Integer32"
_CsInVisionBladeType_Object = MibTableColumn
csInVisionBladeType = _CsInVisionBladeType_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 3),
    _CsInVisionBladeType_Type()
)
csInVisionBladeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladeType.setStatus("current")


class _CsInVisionBladeState_Type(Integer32):
    """Custom type csInVisionBladeState based on Integer32"""
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
        *(("active", 3),
          ("backup", 9),
          ("failedWithBackup", 7),
          ("failedWithOutBackup", 8),
          ("inactive", 2),
          ("nonOperational", 6),
          ("notPresent", 1),
          ("operational", 5),
          ("reboot", 11),
          ("softwareLoading", 4),
          ("standby", 10))
    )


_CsInVisionBladeState_Type.__name__ = "Integer32"
_CsInVisionBladeState_Object = MibTableColumn
csInVisionBladeState = _CsInVisionBladeState_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 4),
    _CsInVisionBladeState_Type()
)
csInVisionBladeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladeState.setStatus("current")
_CsInVisionBladeEnginesNumb_Type = Integer32
_CsInVisionBladeEnginesNumb_Object = MibTableColumn
csInVisionBladeEnginesNumb = _CsInVisionBladeEnginesNumb_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 5),
    _CsInVisionBladeEnginesNumb_Type()
)
csInVisionBladeEnginesNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladeEnginesNumb.setStatus("current")


class _CsInVisionBladePortNumb_Type(Integer32):
    """Custom type csInVisionBladePortNumb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_CsInVisionBladePortNumb_Type.__name__ = "Integer32"
_CsInVisionBladePortNumb_Object = MibTableColumn
csInVisionBladePortNumb = _CsInVisionBladePortNumb_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 6),
    _CsInVisionBladePortNumb_Type()
)
csInVisionBladePortNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladePortNumb.setStatus("current")
_CsInVisionBladeSerialNumb_Type = DisplayString
_CsInVisionBladeSerialNumb_Object = MibTableColumn
csInVisionBladeSerialNumb = _CsInVisionBladeSerialNumb_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 7),
    _CsInVisionBladeSerialNumb_Type()
)
csInVisionBladeSerialNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladeSerialNumb.setStatus("current")
_CsInVisionBladeHwVer_Type = DisplayString
_CsInVisionBladeHwVer_Object = MibTableColumn
csInVisionBladeHwVer = _CsInVisionBladeHwVer_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 8),
    _CsInVisionBladeHwVer_Type()
)
csInVisionBladeHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladeHwVer.setStatus("current")
_CsInVisionBladeSwVer_Type = DisplayString
_CsInVisionBladeSwVer_Object = MibTableColumn
csInVisionBladeSwVer = _CsInVisionBladeSwVer_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 9),
    _CsInVisionBladeSwVer_Type()
)
csInVisionBladeSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csInVisionBladeSwVer.setStatus("current")


class _CsInVisionBladeReset_Type(Integer32):
    """Custom type csInVisionBladeReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reset", 2))
    )


_CsInVisionBladeReset_Type.__name__ = "Integer32"
_CsInVisionBladeReset_Object = MibTableColumn
csInVisionBladeReset = _CsInVisionBladeReset_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 2, 1, 1, 10),
    _CsInVisionBladeReset_Type()
)
csInVisionBladeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csInVisionBladeReset.setStatus("current")
_CsInVisionObjects_ObjectIdentity = ObjectIdentity
csInVisionObjects = _CsInVisionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 3)
)


class _CsInVisionServerName_Type(DisplayString):
    """Custom type csInVisionServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CsInVisionServerName_Type.__name__ = "DisplayString"
_CsInVisionServerName_Object = MibScalar
csInVisionServerName = _CsInVisionServerName_Object(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 3, 1),
    _CsInVisionServerName_Type()
)
csInVisionServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csInVisionServerName.setStatus("current")

# Managed Objects groups


# Notification objects

csInVisionBladeResyncedInInVision = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 1)
)
csInVisionBladeResyncedInInVision.setObjects(
      *(("COSINE-ORION-MIB", "csOrionRestoreSlotIndex"),
        ("COSINE-ORION-MIB", "csOrionBladeType"))
)
if mibBuilder.loadTexts:
    csInVisionBladeResyncedInInVision.setStatus(
        "current"
    )

csInVisionBladeInconsistentInInVision = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 2)
)
csInVisionBladeInconsistentInInVision.setObjects(
      *(("COSINE-ORION-MIB", "csOrionRestoreSlotIndex"),
        ("COSINE-InVision-MIB", "csInVisionBladeType"),
        ("COSINE-ORION-MIB", "csOrionBladeType"))
)
if mibBuilder.loadTexts:
    csInVisionBladeInconsistentInInVision.setStatus(
        "current"
    )

csInVisionBladeRestoreOnDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 3)
)
csInVisionBladeRestoreOnDevice.setObjects(
      *(("COSINE-ORION-MIB", "csOrionRestoreSlotIndex"),
        ("COSINE-ORION-MIB", "csOrionBladeType"))
)
if mibBuilder.loadTexts:
    csInVisionBladeRestoreOnDevice.setStatus(
        "current"
    )

csInVisionVRRestoreSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 4)
)
csInVisionVRRestoreSuccess.setObjects(
    ("COSINE-ORION-MIB", "csOrionRestoreNumVRs")
)
if mibBuilder.loadTexts:
    csInVisionVRRestoreSuccess.setStatus(
        "current"
    )

csInVisionVRRestoreFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 5)
)
csInVisionVRRestoreFail.setObjects(
    ("COSINE-ORION-MIB", "csOrionRestoreNumVRs")
)
if mibBuilder.loadTexts:
    csInVisionVRRestoreFail.setStatus(
        "current"
    )

csInVisionDeviceVRRestoreFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 6)
)
csInVisionDeviceVRRestoreFail.setObjects(
    ("COSINE-ORION-MIB", "csOrionRestoreNumVRs")
)
if mibBuilder.loadTexts:
    csInVisionDeviceVRRestoreFail.setStatus(
        "current"
    )

csInVisionFailToRegisterForTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 7)
)
csInVisionFailToRegisterForTrap.setObjects(
    ("COSINE-ORION-MIB", "csOrionSystemIpAddress")
)
if mibBuilder.loadTexts:
    csInVisionFailToRegisterForTrap.setStatus(
        "current"
    )

csInVisionServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 8)
)
csInVisionServerDown.setObjects(
    ("COSINE-InVision-MIB", "csInVisionServerName")
)
if mibBuilder.loadTexts:
    csInVisionServerDown.setStatus(
        "current"
    )

csInVisionFailToUnRegisterForTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2, 1, 1, 9)
)
csInVisionFailToUnRegisterForTrap.setObjects(
    ("COSINE-ORION-MIB", "csOrionSystemIpAddress")
)
if mibBuilder.loadTexts:
    csInVisionFailToUnRegisterForTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COSINE-InVision-MIB",
    **{"cosineInVisionMod": cosineInVisionMod,
       "csInVisionEvents": csInVisionEvents,
       "csInVisionEventsInfo": csInVisionEventsInfo,
       "csInVisionBladeResyncedInInVision": csInVisionBladeResyncedInInVision,
       "csInVisionBladeInconsistentInInVision": csInVisionBladeInconsistentInInVision,
       "csInVisionBladeRestoreOnDevice": csInVisionBladeRestoreOnDevice,
       "csInVisionVRRestoreSuccess": csInVisionVRRestoreSuccess,
       "csInVisionVRRestoreFail": csInVisionVRRestoreFail,
       "csInVisionDeviceVRRestoreFail": csInVisionDeviceVRRestoreFail,
       "csInVisionFailToRegisterForTrap": csInVisionFailToRegisterForTrap,
       "csInVisionServerDown": csInVisionServerDown,
       "csInVisionFailToUnRegisterForTrap": csInVisionFailToUnRegisterForTrap,
       "csInVisionBladeInfo": csInVisionBladeInfo,
       "csInVisionBladeTable": csInVisionBladeTable,
       "csInVisionBladeEntry": csInVisionBladeEntry,
       "csInVisionBladeSlotLocation": csInVisionBladeSlotLocation,
       "csInVisionBladeDescr": csInVisionBladeDescr,
       "csInVisionBladeType": csInVisionBladeType,
       "csInVisionBladeState": csInVisionBladeState,
       "csInVisionBladeEnginesNumb": csInVisionBladeEnginesNumb,
       "csInVisionBladePortNumb": csInVisionBladePortNumb,
       "csInVisionBladeSerialNumb": csInVisionBladeSerialNumb,
       "csInVisionBladeHwVer": csInVisionBladeHwVer,
       "csInVisionBladeSwVer": csInVisionBladeSwVer,
       "csInVisionBladeReset": csInVisionBladeReset,
       "csInVisionObjects": csInVisionObjects,
       "csInVisionServerName": csInVisionServerName}
)
