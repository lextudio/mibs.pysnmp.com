# SNMP MIB module (VIDEOFRAME-SIGMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VIDEOFRAME-SIGMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:30 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(vfBoxId,) = mibBuilder.importSymbols(
    "VIDEOFRAME-GENERIC-MIB",
    "vfBoxId")

(vfMIBModules,
 vfProducts,
 vfProductsReg) = mibBuilder.importSymbols(
    "VIDEOFRAME-REGISTRATIONS-MIB",
    "vfMIBModules",
    "vfProducts",
    "vfProductsReg")


# MODULE-IDENTITY

videoframeSigmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 1, 3)
)
videoframeSigmonMIB.setRevisions(
        ("1901-08-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VfSigmonFrame_ObjectIdentity = ObjectIdentity
vfSigmonFrame = _VfSigmonFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2)
)
_VfSigmonFrameModuleTypes_ObjectIdentity = ObjectIdentity
vfSigmonFrameModuleTypes = _VfSigmonFrameModuleTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 1)
)
_VfFrameSlotTable_Object = MibTable
vfFrameSlotTable = _VfFrameSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2)
)
if mibBuilder.loadTexts:
    vfFrameSlotTable.setStatus("current")
_VfFrameSlotEntry_Object = MibTableRow
vfFrameSlotEntry = _VfFrameSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1)
)
vfFrameSlotEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfFrameSlotNumber"),
)
if mibBuilder.loadTexts:
    vfFrameSlotEntry.setStatus("current")


class _VfFrameSlotNumber_Type(Integer32):
    """Custom type vfFrameSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_VfFrameSlotNumber_Type.__name__ = "Integer32"
_VfFrameSlotNumber_Object = MibTableColumn
vfFrameSlotNumber = _VfFrameSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 1),
    _VfFrameSlotNumber_Type()
)
vfFrameSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfFrameSlotNumber.setStatus("current")


class _VfFrameSlotStatus_Type(Integer32):
    """Custom type vfFrameSlotStatus based on Integer32"""
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
        *(("empty", 1),
          ("illegalSlot", 4),
          ("moduleUninitialized", 2),
          ("moduleValid", 3))
    )


_VfFrameSlotStatus_Type.__name__ = "Integer32"
_VfFrameSlotStatus_Object = MibTableColumn
vfFrameSlotStatus = _VfFrameSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 2),
    _VfFrameSlotStatus_Type()
)
vfFrameSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfFrameSlotStatus.setStatus("current")
_VfModuleTypeRegObjectID_Type = ObjectIdentifier
_VfModuleTypeRegObjectID_Object = MibTableColumn
vfModuleTypeRegObjectID = _VfModuleTypeRegObjectID_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 3),
    _VfModuleTypeRegObjectID_Type()
)
vfModuleTypeRegObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfModuleTypeRegObjectID.setStatus("current")
_VfModuleTypeRootOID_Type = ObjectIdentifier
_VfModuleTypeRootOID_Object = MibTableColumn
vfModuleTypeRootOID = _VfModuleTypeRootOID_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 4),
    _VfModuleTypeRootOID_Type()
)
vfModuleTypeRootOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfModuleTypeRootOID.setStatus("current")


class _VfModulePartNo_Type(DisplayString):
    """Custom type vfModulePartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VfModulePartNo_Type.__name__ = "DisplayString"
_VfModulePartNo_Object = MibTableColumn
vfModulePartNo = _VfModulePartNo_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 5),
    _VfModulePartNo_Type()
)
vfModulePartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfModulePartNo.setStatus("current")


class _VfModuleDescription_Type(DisplayString):
    """Custom type vfModuleDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VfModuleDescription_Type.__name__ = "DisplayString"
_VfModuleDescription_Object = MibTableColumn
vfModuleDescription = _VfModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 6),
    _VfModuleDescription_Type()
)
vfModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfModuleDescription.setStatus("current")


class _VfModuleTrapEnable_Type(Integer32):
    """Custom type vfModuleTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VfModuleTrapEnable_Type.__name__ = "Integer32"
_VfModuleTrapEnable_Object = MibTableColumn
vfModuleTrapEnable = _VfModuleTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 7),
    _VfModuleTrapEnable_Type()
)
vfModuleTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfModuleTrapEnable.setStatus("current")


class _VfModuleAlarmAutoReArm_Type(Integer32):
    """Custom type vfModuleAlarmAutoReArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VfModuleAlarmAutoReArm_Type.__name__ = "Integer32"
_VfModuleAlarmAutoReArm_Object = MibTableColumn
vfModuleAlarmAutoReArm = _VfModuleAlarmAutoReArm_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 2, 1, 8),
    _VfModuleAlarmAutoReArm_Type()
)
vfModuleAlarmAutoReArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfModuleAlarmAutoReArm.setStatus("current")


class _VfFrameOfflineSwitch_Type(Integer32):
    """Custom type vfFrameOfflineSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_VfFrameOfflineSwitch_Type.__name__ = "Integer32"
_VfFrameOfflineSwitch_Object = MibScalar
vfFrameOfflineSwitch = _VfFrameOfflineSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 3),
    _VfFrameOfflineSwitch_Type()
)
vfFrameOfflineSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfFrameOfflineSwitch.setStatus("current")


class _VfFrameLocateIndicator_Type(Integer32):
    """Custom type vfFrameLocateIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("off", 2))
    )


_VfFrameLocateIndicator_Type.__name__ = "Integer32"
_VfFrameLocateIndicator_Object = MibScalar
vfFrameLocateIndicator = _VfFrameLocateIndicator_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 4),
    _VfFrameLocateIndicator_Type()
)
vfFrameLocateIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfFrameLocateIndicator.setStatus("current")


class _VfFrameAdminState_Type(Integer32):
    """Custom type vfFrameAdminState based on Integer32"""
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
        *(("vfFrameDisabled", 3),
          ("vfFrameInMaintenance", 2),
          ("vfFrameOnline", 1),
          ("vfFrameResetting", 4))
    )


_VfFrameAdminState_Type.__name__ = "Integer32"
_VfFrameAdminState_Object = MibScalar
vfFrameAdminState = _VfFrameAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 5),
    _VfFrameAdminState_Type()
)
vfFrameAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfFrameAdminState.setStatus("current")


class _VfNumDerivedNotifications_Type(Integer32):
    """Custom type vfNumDerivedNotifications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VfNumDerivedNotifications_Type.__name__ = "Integer32"
_VfNumDerivedNotifications_Object = MibScalar
vfNumDerivedNotifications = _VfNumDerivedNotifications_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 6),
    _VfNumDerivedNotifications_Type()
)
vfNumDerivedNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfNumDerivedNotifications.setStatus("current")
_VfDerivedNotificationTable_Object = MibTable
vfDerivedNotificationTable = _VfDerivedNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7)
)
if mibBuilder.loadTexts:
    vfDerivedNotificationTable.setStatus("current")
_VfDerivedNotificationEntry_Object = MibTableRow
vfDerivedNotificationEntry = _VfDerivedNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1)
)
vfDerivedNotificationEntry.setIndexNames(
    (0, "VIDEOFRAME-SIGMON-MIB", "vfDnFunctionNumber"),
)
if mibBuilder.loadTexts:
    vfDerivedNotificationEntry.setStatus("current")
_VfDnFunctionNumber_Type = Integer32
_VfDnFunctionNumber_Object = MibTableColumn
vfDnFunctionNumber = _VfDnFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1, 1),
    _VfDnFunctionNumber_Type()
)
vfDnFunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfDnFunctionNumber.setStatus("current")


class _VfDnFunctionDescription_Type(DisplayString):
    """Custom type vfDnFunctionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_VfDnFunctionDescription_Type.__name__ = "DisplayString"
_VfDnFunctionDescription_Object = MibTableColumn
vfDnFunctionDescription = _VfDnFunctionDescription_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1, 2),
    _VfDnFunctionDescription_Type()
)
vfDnFunctionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfDnFunctionDescription.setStatus("current")


class _VfDnNotificationLevel_Type(Integer32):
    """Custom type vfDnNotificationLevel based on Integer32"""
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
        *(("levelA", 1),
          ("levelB", 2),
          ("levelC", 3),
          ("levelD", 4))
    )


_VfDnNotificationLevel_Type.__name__ = "Integer32"
_VfDnNotificationLevel_Object = MibTableColumn
vfDnNotificationLevel = _VfDnNotificationLevel_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1, 3),
    _VfDnNotificationLevel_Type()
)
vfDnNotificationLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfDnNotificationLevel.setStatus("current")


class _VfDnNotificationEnable_Type(Integer32):
    """Custom type vfDnNotificationEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VfDnNotificationEnable_Type.__name__ = "Integer32"
_VfDnNotificationEnable_Object = MibTableColumn
vfDnNotificationEnable = _VfDnNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1, 4),
    _VfDnNotificationEnable_Type()
)
vfDnNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfDnNotificationEnable.setStatus("current")


class _VfDnNotificationAutoReArm_Type(Integer32):
    """Custom type vfDnNotificationAutoReArm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VfDnNotificationAutoReArm_Type.__name__ = "Integer32"
_VfDnNotificationAutoReArm_Object = MibTableColumn
vfDnNotificationAutoReArm = _VfDnNotificationAutoReArm_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1, 5),
    _VfDnNotificationAutoReArm_Type()
)
vfDnNotificationAutoReArm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfDnNotificationAutoReArm.setStatus("current")


class _VfDnNotificationState_Type(Integer32):
    """Custom type vfDnNotificationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("triggered", 2))
    )


_VfDnNotificationState_Type.__name__ = "Integer32"
_VfDnNotificationState_Object = MibTableColumn
vfDnNotificationState = _VfDnNotificationState_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1, 6),
    _VfDnNotificationState_Type()
)
vfDnNotificationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfDnNotificationState.setStatus("current")


class _VfDnNotificationAcknowledge_Type(Integer32):
    """Custom type vfDnNotificationAcknowledge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 3),
          ("idle", 1),
          ("unacknowledged", 2))
    )


_VfDnNotificationAcknowledge_Type.__name__ = "Integer32"
_VfDnNotificationAcknowledge_Object = MibTableColumn
vfDnNotificationAcknowledge = _VfDnNotificationAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 7, 1, 7),
    _VfDnNotificationAcknowledge_Type()
)
vfDnNotificationAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vfDnNotificationAcknowledge.setStatus("current")
_VfSigmonFrameEvents_ObjectIdentity = ObjectIdentity
vfSigmonFrameEvents = _VfSigmonFrameEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 8)
)
_VfSigmonFrameEventsV2_ObjectIdentity = ObjectIdentity
vfSigmonFrameEventsV2 = _VfSigmonFrameEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 8, 0)
)
_VfSigmonFrameDerivedEvents_ObjectIdentity = ObjectIdentity
vfSigmonFrameDerivedEvents = _VfSigmonFrameDerivedEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 9)
)
_VfSigmonFrameDerivedEventsV2_ObjectIdentity = ObjectIdentity
vfSigmonFrameDerivedEventsV2 = _VfSigmonFrameDerivedEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 9, 0)
)
_VfProductsSignalMonitoringFrameReg_ObjectIdentity = ObjectIdentity
vfProductsSignalMonitoringFrameReg = _VfProductsSignalMonitoringFrameReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 4)
)
if mibBuilder.loadTexts:
    vfProductsSignalMonitoringFrameReg.setStatus("current")
_VfProductsVF200Reg_ObjectIdentity = ObjectIdentity
vfProductsVF200Reg = _VfProductsVF200Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4596, 6, 2, 5)
)
if mibBuilder.loadTexts:
    vfProductsVF200Reg.setStatus("current")

# Managed Objects groups


# Notification objects

vfFrameSlotStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 8, 0, 1)
)
vfFrameSlotStatusChange.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-MIB", "vfFrameSlotStatus"),
        ("VIDEOFRAME-SIGMON-MIB", "vfModulePartNo"),
        ("VIDEOFRAME-SIGMON-MIB", "vfModuleDescription"))
)
if mibBuilder.loadTexts:
    vfFrameSlotStatusChange.setStatus(
        "current"
    )

derivedNotificationLevelA = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 9, 0, 1)
)
derivedNotificationLevelA.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionNumber"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionDescription"))
)
if mibBuilder.loadTexts:
    derivedNotificationLevelA.setStatus(
        "current"
    )

derivedNotificationLevelB = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 9, 0, 2)
)
derivedNotificationLevelB.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionNumber"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionDescription"))
)
if mibBuilder.loadTexts:
    derivedNotificationLevelB.setStatus(
        "current"
    )

derivedNotificationLevelC = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 9, 0, 3)
)
derivedNotificationLevelC.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionNumber"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionDescription"))
)
if mibBuilder.loadTexts:
    derivedNotificationLevelC.setStatus(
        "current"
    )

derivedNotificationLevelD = NotificationType(
    (1, 3, 6, 1, 4, 1, 4596, 4, 2, 9, 0, 4)
)
derivedNotificationLevelD.setObjects(
      *(("VIDEOFRAME-GENERIC-MIB", "vfBoxId"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionNumber"),
        ("VIDEOFRAME-SIGMON-MIB", "vfDnFunctionDescription"))
)
if mibBuilder.loadTexts:
    derivedNotificationLevelD.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIDEOFRAME-SIGMON-MIB",
    **{"vfSigmonFrame": vfSigmonFrame,
       "vfSigmonFrameModuleTypes": vfSigmonFrameModuleTypes,
       "vfFrameSlotTable": vfFrameSlotTable,
       "vfFrameSlotEntry": vfFrameSlotEntry,
       "vfFrameSlotNumber": vfFrameSlotNumber,
       "vfFrameSlotStatus": vfFrameSlotStatus,
       "vfModuleTypeRegObjectID": vfModuleTypeRegObjectID,
       "vfModuleTypeRootOID": vfModuleTypeRootOID,
       "vfModulePartNo": vfModulePartNo,
       "vfModuleDescription": vfModuleDescription,
       "vfModuleTrapEnable": vfModuleTrapEnable,
       "vfModuleAlarmAutoReArm": vfModuleAlarmAutoReArm,
       "vfFrameOfflineSwitch": vfFrameOfflineSwitch,
       "vfFrameLocateIndicator": vfFrameLocateIndicator,
       "vfFrameAdminState": vfFrameAdminState,
       "vfNumDerivedNotifications": vfNumDerivedNotifications,
       "vfDerivedNotificationTable": vfDerivedNotificationTable,
       "vfDerivedNotificationEntry": vfDerivedNotificationEntry,
       "vfDnFunctionNumber": vfDnFunctionNumber,
       "vfDnFunctionDescription": vfDnFunctionDescription,
       "vfDnNotificationLevel": vfDnNotificationLevel,
       "vfDnNotificationEnable": vfDnNotificationEnable,
       "vfDnNotificationAutoReArm": vfDnNotificationAutoReArm,
       "vfDnNotificationState": vfDnNotificationState,
       "vfDnNotificationAcknowledge": vfDnNotificationAcknowledge,
       "vfSigmonFrameEvents": vfSigmonFrameEvents,
       "vfSigmonFrameEventsV2": vfSigmonFrameEventsV2,
       "vfFrameSlotStatusChange": vfFrameSlotStatusChange,
       "vfSigmonFrameDerivedEvents": vfSigmonFrameDerivedEvents,
       "vfSigmonFrameDerivedEventsV2": vfSigmonFrameDerivedEventsV2,
       "derivedNotificationLevelA": derivedNotificationLevelA,
       "derivedNotificationLevelB": derivedNotificationLevelB,
       "derivedNotificationLevelC": derivedNotificationLevelC,
       "derivedNotificationLevelD": derivedNotificationLevelD,
       "videoframeSigmonMIB": videoframeSigmonMIB,
       "vfProductsSignalMonitoringFrameReg": vfProductsSignalMonitoringFrameReg,
       "vfProductsVF200Reg": vfProductsVF200Reg}
)
