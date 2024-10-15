# SNMP MIB module (DLINK-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-EQUIPMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:46 2024
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

(AgentNotifyLevel,
 dlink_common_mgmt) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "AgentNotifyLevel",
    "dlink-common-mgmt")

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

swDlinkEquipmentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDlinkEquipmentMib_ObjectIdentity = ObjectIdentity
swDlinkEquipmentMib = _SwDlinkEquipmentMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1)
)


class _SwDlinkEquipmentCapacity_Type(Bits):
    """Custom type swDlinkEquipmentCapacity based on Bits"""
    namedValues = NamedValues(
        *(("chassisCapable", 4),
          ("fanCapable", 0),
          ("redundantPowerCapable", 1),
          ("stackingCapable", 3),
          ("tempteratureDetection", 2))
    )

_SwDlinkEquipmentCapacity_Type.__name__ = "Bits"
_SwDlinkEquipmentCapacity_Object = MibScalar
swDlinkEquipmentCapacity = _SwDlinkEquipmentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 1),
    _SwDlinkEquipmentCapacity_Type()
)
swDlinkEquipmentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDlinkEquipmentCapacity.setStatus("current")
_SwPowerTable_Object = MibTable
swPowerTable = _SwPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6)
)
if mibBuilder.loadTexts:
    swPowerTable.setStatus("current")
_SwPowerEntry_Object = MibTableRow
swPowerEntry = _SwPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1)
)
swPowerEntry.setIndexNames(
    (0, "DLINK-EQUIPMENT-MIB", "swPowerUnitIndex"),
    (0, "DLINK-EQUIPMENT-MIB", "swPowerID"),
)
if mibBuilder.loadTexts:
    swPowerEntry.setStatus("current")


class _SwPowerUnitIndex_Type(Integer32):
    """Custom type swPowerUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPowerUnitIndex_Type.__name__ = "Integer32"
_SwPowerUnitIndex_Object = MibTableColumn
swPowerUnitIndex = _SwPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 1),
    _SwPowerUnitIndex_Type()
)
swPowerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerUnitIndex.setStatus("current")


class _SwPowerID_Type(Integer32):
    """Custom type swPowerID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwPowerID_Type.__name__ = "Integer32"
_SwPowerID_Object = MibTableColumn
swPowerID = _SwPowerID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 2),
    _SwPowerID_Type()
)
swPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerID.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("connect", 5),
          ("disconnect", 6),
          ("fail", 4),
          ("lowVoltage", 1),
          ("other", 0),
          ("overCurrent", 2),
          ("working", 3))
    )


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 3),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")
_SwUnitMgmt_ObjectIdentity = ObjectIdentity
swUnitMgmt = _SwUnitMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9)
)


class _SwUnitStackingVersion_Type(Integer32):
    """Custom type swUnitStackingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitStackingVersion_Type.__name__ = "Integer32"
_SwUnitStackingVersion_Object = MibScalar
swUnitStackingVersion = _SwUnitStackingVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 1),
    _SwUnitStackingVersion_Type()
)
swUnitStackingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitStackingVersion.setStatus("current")


class _SwUnitMaxSupportedUnits_Type(Integer32):
    """Custom type swUnitMaxSupportedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitMaxSupportedUnits_Type.__name__ = "Integer32"
_SwUnitMaxSupportedUnits_Object = MibScalar
swUnitMaxSupportedUnits = _SwUnitMaxSupportedUnits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 2),
    _SwUnitMaxSupportedUnits_Type()
)
swUnitMaxSupportedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMaxSupportedUnits.setStatus("current")


class _SwUnitNumOfUnit_Type(Integer32):
    """Custom type swUnitNumOfUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitNumOfUnit_Type.__name__ = "Integer32"
_SwUnitNumOfUnit_Object = MibScalar
swUnitNumOfUnit = _SwUnitNumOfUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 3),
    _SwUnitNumOfUnit_Type()
)
swUnitNumOfUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitNumOfUnit.setStatus("current")
_SwUnitMgmtTable_Object = MibTable
swUnitMgmtTable = _SwUnitMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4)
)
if mibBuilder.loadTexts:
    swUnitMgmtTable.setStatus("current")
_SwUnitMgmtEntry_Object = MibTableRow
swUnitMgmtEntry = _SwUnitMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1)
)
swUnitMgmtEntry.setIndexNames(
    (0, "DLINK-EQUIPMENT-MIB", "swUnitMgmtId"),
)
if mibBuilder.loadTexts:
    swUnitMgmtEntry.setStatus("current")


class _SwUnitMgmtId_Type(Integer32):
    """Custom type swUnitMgmtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SwUnitMgmtId_Type.__name__ = "Integer32"
_SwUnitMgmtId_Object = MibTableColumn
swUnitMgmtId = _SwUnitMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 1),
    _SwUnitMgmtId_Type()
)
swUnitMgmtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtId.setStatus("current")
_SwUnitMgmtMacAddr_Type = MacAddress
_SwUnitMgmtMacAddr_Object = MibTableColumn
swUnitMgmtMacAddr = _SwUnitMgmtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 2),
    _SwUnitMgmtMacAddr_Type()
)
swUnitMgmtMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtMacAddr.setStatus("current")


class _SwUnitMgmtStartPort_Type(Integer32):
    """Custom type swUnitMgmtStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwUnitMgmtStartPort_Type.__name__ = "Integer32"
_SwUnitMgmtStartPort_Object = MibTableColumn
swUnitMgmtStartPort = _SwUnitMgmtStartPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 3),
    _SwUnitMgmtStartPort_Type()
)
swUnitMgmtStartPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtStartPort.setStatus("current")


class _SwUnitMgmtPortRange_Type(Integer32):
    """Custom type swUnitMgmtPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwUnitMgmtPortRange_Type.__name__ = "Integer32"
_SwUnitMgmtPortRange_Object = MibTableColumn
swUnitMgmtPortRange = _SwUnitMgmtPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 4),
    _SwUnitMgmtPortRange_Type()
)
swUnitMgmtPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtPortRange.setStatus("current")


class _SwUnitMgmtFrontPanelLedStatus_Type(OctetString):
    """Custom type swUnitMgmtFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwUnitMgmtFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwUnitMgmtFrontPanelLedStatus_Object = MibTableColumn
swUnitMgmtFrontPanelLedStatus = _SwUnitMgmtFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 5),
    _SwUnitMgmtFrontPanelLedStatus_Type()
)
swUnitMgmtFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtFrontPanelLedStatus.setStatus("current")


class _SwUnitMgmtCtrlMode_Type(Integer32):
    """Custom type swUnitMgmtCtrlMode based on Integer32"""
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
        *(("auto", 2),
          ("master", 4),
          ("other", 1),
          ("slave", 5),
          ("stand-alone", 3))
    )


_SwUnitMgmtCtrlMode_Type.__name__ = "Integer32"
_SwUnitMgmtCtrlMode_Object = MibTableColumn
swUnitMgmtCtrlMode = _SwUnitMgmtCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 6),
    _SwUnitMgmtCtrlMode_Type()
)
swUnitMgmtCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUnitMgmtCtrlMode.setStatus("current")


class _SwUnitMgmtCurrentMode_Type(Integer32):
    """Custom type swUnitMgmtCurrentMode based on Integer32"""
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
        *(("auto", 2),
          ("master", 4),
          ("other", 1),
          ("slave", 5),
          ("stand-alone", 3))
    )


_SwUnitMgmtCurrentMode_Type.__name__ = "Integer32"
_SwUnitMgmtCurrentMode_Object = MibTableColumn
swUnitMgmtCurrentMode = _SwUnitMgmtCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 7),
    _SwUnitMgmtCurrentMode_Type()
)
swUnitMgmtCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtCurrentMode.setStatus("current")


class _SwUnitMgmtVersion_Type(DisplayString):
    """Custom type swUnitMgmtVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwUnitMgmtVersion_Type.__name__ = "DisplayString"
_SwUnitMgmtVersion_Object = MibTableColumn
swUnitMgmtVersion = _SwUnitMgmtVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 8),
    _SwUnitMgmtVersion_Type()
)
swUnitMgmtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtVersion.setStatus("current")


class _SwUnitMgmtModuleName_Type(DisplayString):
    """Custom type swUnitMgmtModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwUnitMgmtModuleName_Type.__name__ = "DisplayString"
_SwUnitMgmtModuleName_Object = MibTableColumn
swUnitMgmtModuleName = _SwUnitMgmtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 9),
    _SwUnitMgmtModuleName_Type()
)
swUnitMgmtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swUnitMgmtModuleName.setStatus("current")
_SwDlinkEquipmentNotify_ObjectIdentity = ObjectIdentity
swDlinkEquipmentNotify = _SwDlinkEquipmentNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2)
)
_SwEquipmentNotification_ObjectIdentity = ObjectIdentity
swEquipmentNotification = _SwEquipmentNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2)
)
_SwEquipPowerNotification_ObjectIdentity = ObjectIdentity
swEquipPowerNotification = _SwEquipPowerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2)
)
_SwEquipPowerNotifyPerfix_ObjectIdentity = ObjectIdentity
swEquipPowerNotifyPerfix = _SwEquipPowerNotifyPerfix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0)
)
_SwNotificationBindings_ObjectIdentity = ObjectIdentity
swNotificationBindings = _SwNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3)
)

# Managed Objects groups


# Notification objects

swPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 2)
)
swPowerFailure.setObjects(
      *(("DLINK-EQUIPMENT-MIB", "swPowerUnitIndex"),
        ("DLINK-EQUIPMENT-MIB", "swPowerID"),
        ("DLINK-EQUIPMENT-MIB", "swPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerFailure.setStatus(
        "current"
    )

swPowerRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 3)
)
swPowerRecover.setObjects(
      *(("DLINK-EQUIPMENT-MIB", "swPowerUnitIndex"),
        ("DLINK-EQUIPMENT-MIB", "swPowerID"),
        ("DLINK-EQUIPMENT-MIB", "swPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-EQUIPMENT-MIB",
    **{"MacAddress": MacAddress,
       "swDlinkEquipmentMIB": swDlinkEquipmentMIB,
       "swDlinkEquipmentMib": swDlinkEquipmentMib,
       "swDlinkEquipmentCapacity": swDlinkEquipmentCapacity,
       "swPowerTable": swPowerTable,
       "swPowerEntry": swPowerEntry,
       "swPowerUnitIndex": swPowerUnitIndex,
       "swPowerID": swPowerID,
       "swPowerStatus": swPowerStatus,
       "swUnitMgmt": swUnitMgmt,
       "swUnitStackingVersion": swUnitStackingVersion,
       "swUnitMaxSupportedUnits": swUnitMaxSupportedUnits,
       "swUnitNumOfUnit": swUnitNumOfUnit,
       "swUnitMgmtTable": swUnitMgmtTable,
       "swUnitMgmtEntry": swUnitMgmtEntry,
       "swUnitMgmtId": swUnitMgmtId,
       "swUnitMgmtMacAddr": swUnitMgmtMacAddr,
       "swUnitMgmtStartPort": swUnitMgmtStartPort,
       "swUnitMgmtPortRange": swUnitMgmtPortRange,
       "swUnitMgmtFrontPanelLedStatus": swUnitMgmtFrontPanelLedStatus,
       "swUnitMgmtCtrlMode": swUnitMgmtCtrlMode,
       "swUnitMgmtCurrentMode": swUnitMgmtCurrentMode,
       "swUnitMgmtVersion": swUnitMgmtVersion,
       "swUnitMgmtModuleName": swUnitMgmtModuleName,
       "swDlinkEquipmentNotify": swDlinkEquipmentNotify,
       "swEquipmentNotification": swEquipmentNotification,
       "swEquipPowerNotification": swEquipPowerNotification,
       "swEquipPowerNotifyPerfix": swEquipPowerNotifyPerfix,
       "swPowerFailure": swPowerFailure,
       "swPowerRecover": swPowerRecover,
       "swNotificationBindings": swNotificationBindings}
)
