# SNMP MIB module (BAY-STACK-ADAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-ADAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:48 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackAdacMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 9)
)
bayStackAdacMib.setRevisions(
        ("2014-04-14 00:00",
         "2009-05-20 00:00",
         "2006-10-16 00:00",
         "2006-05-24 00:00",
         "2006-03-13 00:00",
         "2005-04-12 00:00",
         "2004-12-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsAdacNotifications_ObjectIdentity = ObjectIdentity
bsAdacNotifications = _BsAdacNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 0)
)
_BsAdacObjects_ObjectIdentity = ObjectIdentity
bsAdacObjects = _BsAdacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1)
)
_BsAdacScalars_ObjectIdentity = ObjectIdentity
bsAdacScalars = _BsAdacScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1)
)
_BsAdacAdminEnable_Type = TruthValue
_BsAdacAdminEnable_Object = MibScalar
bsAdacAdminEnable = _BsAdacAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 2),
    _BsAdacAdminEnable_Type()
)
bsAdacAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacAdminEnable.setStatus("current")


class _BsAdacOperatingMode_Type(Integer32):
    """Custom type bsAdacOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("taggedFrames", 3),
          ("untaggedFramesAdvanced", 2),
          ("untaggedFramesBasic", 1))
    )


_BsAdacOperatingMode_Type.__name__ = "Integer32"
_BsAdacOperatingMode_Object = MibScalar
bsAdacOperatingMode = _BsAdacOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 3),
    _BsAdacOperatingMode_Type()
)
bsAdacOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacOperatingMode.setStatus("current")
_BsAdacCallServerPort_Type = InterfaceIndexOrZero
_BsAdacCallServerPort_Object = MibScalar
bsAdacCallServerPort = _BsAdacCallServerPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 4),
    _BsAdacCallServerPort_Type()
)
bsAdacCallServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacCallServerPort.setStatus("current")
_BsAdacUplinkPort_Type = InterfaceIndexOrZero
_BsAdacUplinkPort_Object = MibScalar
bsAdacUplinkPort = _BsAdacUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 5),
    _BsAdacUplinkPort_Type()
)
bsAdacUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacUplinkPort.setStatus("current")
_BsAdacVoiceVlan_Type = VlanIdOrNone
_BsAdacVoiceVlan_Object = MibScalar
bsAdacVoiceVlan = _BsAdacVoiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 6),
    _BsAdacVoiceVlan_Type()
)
bsAdacVoiceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacVoiceVlan.setStatus("current")
_BsAdacNotificationControlEnable_Type = TruthValue
_BsAdacNotificationControlEnable_Object = MibScalar
bsAdacNotificationControlEnable = _BsAdacNotificationControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 7),
    _BsAdacNotificationControlEnable_Type()
)
bsAdacNotificationControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacNotificationControlEnable.setStatus("current")


class _BsAdacMacAddrRangeControl_Type(Integer32):
    """Custom type bsAdacMacAddrRangeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearTable", 2),
          ("defaultTable", 3),
          ("none", 1))
    )


_BsAdacMacAddrRangeControl_Type.__name__ = "Integer32"
_BsAdacMacAddrRangeControl_Object = MibScalar
bsAdacMacAddrRangeControl = _BsAdacMacAddrRangeControl_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 8),
    _BsAdacMacAddrRangeControl_Type()
)
bsAdacMacAddrRangeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacMacAddrRangeControl.setStatus("current")
_BsAdacOperEnable_Type = TruthValue
_BsAdacOperEnable_Object = MibScalar
bsAdacOperEnable = _BsAdacOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 9),
    _BsAdacOperEnable_Type()
)
bsAdacOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsAdacOperEnable.setStatus("current")
_BsAdacCallServerPortList_Type = PortList
_BsAdacCallServerPortList_Object = MibScalar
bsAdacCallServerPortList = _BsAdacCallServerPortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 10),
    _BsAdacCallServerPortList_Type()
)
bsAdacCallServerPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacCallServerPortList.setStatus("current")
_BsAdacUplinkPortList_Type = PortList
_BsAdacUplinkPortList_Object = MibScalar
bsAdacUplinkPortList = _BsAdacUplinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 11),
    _BsAdacUplinkPortList_Type()
)
bsAdacUplinkPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacUplinkPortList.setStatus("current")


class _BsAdacUplinkType_Type(Integer32):
    """Custom type bsAdacUplinkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("spbm", 2))
    )


_BsAdacUplinkType_Type.__name__ = "Integer32"
_BsAdacUplinkType_Object = MibScalar
bsAdacUplinkType = _BsAdacUplinkType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 1, 12),
    _BsAdacUplinkType_Type()
)
bsAdacUplinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacUplinkType.setStatus("current")
_BsAdacPortTable_Object = MibTable
bsAdacPortTable = _BsAdacPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2)
)
if mibBuilder.loadTexts:
    bsAdacPortTable.setStatus("current")
_BsAdacPortEntry_Object = MibTableRow
bsAdacPortEntry = _BsAdacPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1)
)
bsAdacPortEntry.setIndexNames(
    (0, "BAY-STACK-ADAC-MIB", "bsAdacPortIndex"),
)
if mibBuilder.loadTexts:
    bsAdacPortEntry.setStatus("current")
_BsAdacPortIndex_Type = InterfaceIndex
_BsAdacPortIndex_Object = MibTableColumn
bsAdacPortIndex = _BsAdacPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 1),
    _BsAdacPortIndex_Type()
)
bsAdacPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsAdacPortIndex.setStatus("current")
_BsAdacPortAdminEnable_Type = TruthValue
_BsAdacPortAdminEnable_Object = MibTableColumn
bsAdacPortAdminEnable = _BsAdacPortAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 2),
    _BsAdacPortAdminEnable_Type()
)
bsAdacPortAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacPortAdminEnable.setStatus("current")


class _BsAdacPortConfigStatus_Type(Integer32):
    """Custom type bsAdacPortConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configApplied", 1),
          ("configNotApplied", 2))
    )


_BsAdacPortConfigStatus_Type.__name__ = "Integer32"
_BsAdacPortConfigStatus_Object = MibTableColumn
bsAdacPortConfigStatus = _BsAdacPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 3),
    _BsAdacPortConfigStatus_Type()
)
bsAdacPortConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsAdacPortConfigStatus.setStatus("current")


class _BsAdacPortTaggedFramesPvid_Type(Integer32):
    """Custom type bsAdacPortTaggedFramesPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_BsAdacPortTaggedFramesPvid_Type.__name__ = "Integer32"
_BsAdacPortTaggedFramesPvid_Object = MibTableColumn
bsAdacPortTaggedFramesPvid = _BsAdacPortTaggedFramesPvid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 4),
    _BsAdacPortTaggedFramesPvid_Type()
)
bsAdacPortTaggedFramesPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacPortTaggedFramesPvid.setStatus("current")


class _BsAdacPortTaggedFramesTagging_Type(Integer32):
    """Custom type bsAdacPortTaggedFramesTagging based on Integer32"""
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
        *(("noChange", 4),
          ("tagAll", 1),
          ("tagPvidOnly", 2),
          ("untagPvidOnly", 3))
    )


_BsAdacPortTaggedFramesTagging_Type.__name__ = "Integer32"
_BsAdacPortTaggedFramesTagging_Object = MibTableColumn
bsAdacPortTaggedFramesTagging = _BsAdacPortTaggedFramesTagging_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 5),
    _BsAdacPortTaggedFramesTagging_Type()
)
bsAdacPortTaggedFramesTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacPortTaggedFramesTagging.setStatus("current")


class _BsAdacPortType_Type(Integer32):
    """Custom type bsAdacPortType based on Integer32"""
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
        *(("callServer", 2),
          ("other", 4),
          ("telephony", 1),
          ("uplink", 3))
    )


_BsAdacPortType_Type.__name__ = "Integer32"
_BsAdacPortType_Object = MibTableColumn
bsAdacPortType = _BsAdacPortType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 6),
    _BsAdacPortType_Type()
)
bsAdacPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsAdacPortType.setStatus("current")
_BsAdacPortOperEnable_Type = TruthValue
_BsAdacPortOperEnable_Object = MibTableColumn
bsAdacPortOperEnable = _BsAdacPortOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 7),
    _BsAdacPortOperEnable_Type()
)
bsAdacPortOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsAdacPortOperEnable.setStatus("current")
_BsAdacPortMacDetectionEnable_Type = TruthValue
_BsAdacPortMacDetectionEnable_Object = MibTableColumn
bsAdacPortMacDetectionEnable = _BsAdacPortMacDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 8),
    _BsAdacPortMacDetectionEnable_Type()
)
bsAdacPortMacDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacPortMacDetectionEnable.setStatus("current")
_BsAdacPortLldpDetectionEnable_Type = TruthValue
_BsAdacPortLldpDetectionEnable_Object = MibTableColumn
bsAdacPortLldpDetectionEnable = _BsAdacPortLldpDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 2, 1, 9),
    _BsAdacPortLldpDetectionEnable_Type()
)
bsAdacPortLldpDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsAdacPortLldpDetectionEnable.setStatus("current")
_BsAdacMacAddrRangeTable_Object = MibTable
bsAdacMacAddrRangeTable = _BsAdacMacAddrRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3)
)
if mibBuilder.loadTexts:
    bsAdacMacAddrRangeTable.setStatus("current")
_BsAdacMacAddrRangeEntry_Object = MibTableRow
bsAdacMacAddrRangeEntry = _BsAdacMacAddrRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1)
)
bsAdacMacAddrRangeEntry.setIndexNames(
    (0, "BAY-STACK-ADAC-MIB", "bsAdacMacAddrRangeLowEndIndex"),
    (0, "BAY-STACK-ADAC-MIB", "bsAdacMacAddrRangeHighEndIndex"),
)
if mibBuilder.loadTexts:
    bsAdacMacAddrRangeEntry.setStatus("current")
_BsAdacMacAddrRangeLowEndIndex_Type = MacAddress
_BsAdacMacAddrRangeLowEndIndex_Object = MibTableColumn
bsAdacMacAddrRangeLowEndIndex = _BsAdacMacAddrRangeLowEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1, 1),
    _BsAdacMacAddrRangeLowEndIndex_Type()
)
bsAdacMacAddrRangeLowEndIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsAdacMacAddrRangeLowEndIndex.setStatus("current")
_BsAdacMacAddrRangeHighEndIndex_Type = MacAddress
_BsAdacMacAddrRangeHighEndIndex_Object = MibTableColumn
bsAdacMacAddrRangeHighEndIndex = _BsAdacMacAddrRangeHighEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1, 2),
    _BsAdacMacAddrRangeHighEndIndex_Type()
)
bsAdacMacAddrRangeHighEndIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsAdacMacAddrRangeHighEndIndex.setStatus("current")
_BsAdacMacAddrRangeRowStatus_Type = RowStatus
_BsAdacMacAddrRangeRowStatus_Object = MibTableColumn
bsAdacMacAddrRangeRowStatus = _BsAdacMacAddrRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 1, 3, 1, 3),
    _BsAdacMacAddrRangeRowStatus_Type()
)
bsAdacMacAddrRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsAdacMacAddrRangeRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

bsAdacPortConfigNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 0, 1)
)
bsAdacPortConfigNotification.setObjects(
    ("BAY-STACK-ADAC-MIB", "bsAdacPortConfigStatus")
)
if mibBuilder.loadTexts:
    bsAdacPortConfigNotification.setStatus(
        "current"
    )

bsAdacPortOperDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 9, 0, 2)
)
bsAdacPortOperDisabledNotification.setObjects(
    ("BAY-STACK-ADAC-MIB", "bsAdacPortOperEnable")
)
if mibBuilder.loadTexts:
    bsAdacPortOperDisabledNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-ADAC-MIB",
    **{"bayStackAdacMib": bayStackAdacMib,
       "bsAdacNotifications": bsAdacNotifications,
       "bsAdacPortConfigNotification": bsAdacPortConfigNotification,
       "bsAdacPortOperDisabledNotification": bsAdacPortOperDisabledNotification,
       "bsAdacObjects": bsAdacObjects,
       "bsAdacScalars": bsAdacScalars,
       "bsAdacAdminEnable": bsAdacAdminEnable,
       "bsAdacOperatingMode": bsAdacOperatingMode,
       "bsAdacCallServerPort": bsAdacCallServerPort,
       "bsAdacUplinkPort": bsAdacUplinkPort,
       "bsAdacVoiceVlan": bsAdacVoiceVlan,
       "bsAdacNotificationControlEnable": bsAdacNotificationControlEnable,
       "bsAdacMacAddrRangeControl": bsAdacMacAddrRangeControl,
       "bsAdacOperEnable": bsAdacOperEnable,
       "bsAdacCallServerPortList": bsAdacCallServerPortList,
       "bsAdacUplinkPortList": bsAdacUplinkPortList,
       "bsAdacUplinkType": bsAdacUplinkType,
       "bsAdacPortTable": bsAdacPortTable,
       "bsAdacPortEntry": bsAdacPortEntry,
       "bsAdacPortIndex": bsAdacPortIndex,
       "bsAdacPortAdminEnable": bsAdacPortAdminEnable,
       "bsAdacPortConfigStatus": bsAdacPortConfigStatus,
       "bsAdacPortTaggedFramesPvid": bsAdacPortTaggedFramesPvid,
       "bsAdacPortTaggedFramesTagging": bsAdacPortTaggedFramesTagging,
       "bsAdacPortType": bsAdacPortType,
       "bsAdacPortOperEnable": bsAdacPortOperEnable,
       "bsAdacPortMacDetectionEnable": bsAdacPortMacDetectionEnable,
       "bsAdacPortLldpDetectionEnable": bsAdacPortLldpDetectionEnable,
       "bsAdacMacAddrRangeTable": bsAdacMacAddrRangeTable,
       "bsAdacMacAddrRangeEntry": bsAdacMacAddrRangeEntry,
       "bsAdacMacAddrRangeLowEndIndex": bsAdacMacAddrRangeLowEndIndex,
       "bsAdacMacAddrRangeHighEndIndex": bsAdacMacAddrRangeHighEndIndex,
       "bsAdacMacAddrRangeRowStatus": bsAdacMacAddrRangeRowStatus}
)
