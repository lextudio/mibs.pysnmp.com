# SNMP MIB module (HH3C-PU-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PU-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:35 2024
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

(hh3cSurveillanceMIB,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cSurveillanceMIB")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cPUMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPUCommonMan_ObjectIdentity = ObjectIdentity
hh3cPUCommonMan = _Hh3cPUCommonMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1)
)
_Hh3cPUCommonManObjects_ObjectIdentity = ObjectIdentity
hh3cPUCommonManObjects = _Hh3cPUCommonManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 1)
)
_Hh3cPUisOnline_Type = TruthValue
_Hh3cPUisOnline_Object = MibScalar
hh3cPUisOnline = _Hh3cPUisOnline_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 1, 1),
    _Hh3cPUisOnline_Type()
)
hh3cPUisOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUisOnline.setStatus("current")
_Hh3cPUCMSAddr_Type = IpAddress
_Hh3cPUCMSAddr_Object = MibScalar
hh3cPUCMSAddr = _Hh3cPUCMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 1, 2),
    _Hh3cPUCMSAddr_Type()
)
hh3cPUCMSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUCMSAddr.setStatus("current")
_Hh3cPUVersionServerAddr_Type = IpAddress
_Hh3cPUVersionServerAddr_Object = MibScalar
hh3cPUVersionServerAddr = _Hh3cPUVersionServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 1, 3),
    _Hh3cPUVersionServerAddr_Type()
)
hh3cPUVersionServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUVersionServerAddr.setStatus("current")
_Hh3cPUCommonManTables_ObjectIdentity = ObjectIdentity
hh3cPUCommonManTables = _Hh3cPUCommonManTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2)
)
_Hh3cPUExternalInputAlarmTable_Object = MibTable
hh3cPUExternalInputAlarmTable = _Hh3cPUExternalInputAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cPUExternalInputAlarmTable.setStatus("current")
_Hh3cPUExternalInputAlarmEntry_Object = MibTableRow
hh3cPUExternalInputAlarmEntry = _Hh3cPUExternalInputAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 1, 1)
)
hh3cPUExternalInputAlarmEntry.setIndexNames(
    (0, "HH3C-PU-MAN-MIB", "hh3cPUExternalInputAlarmChannelID"),
)
if mibBuilder.loadTexts:
    hh3cPUExternalInputAlarmEntry.setStatus("current")
_Hh3cPUExternalInputAlarmChannelID_Type = Unsigned32
_Hh3cPUExternalInputAlarmChannelID_Object = MibTableColumn
hh3cPUExternalInputAlarmChannelID = _Hh3cPUExternalInputAlarmChannelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 1, 1, 1),
    _Hh3cPUExternalInputAlarmChannelID_Type()
)
hh3cPUExternalInputAlarmChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPUExternalInputAlarmChannelID.setStatus("current")
_Hh3cPUExternalInputAlarmStatus_Type = TruthValue
_Hh3cPUExternalInputAlarmStatus_Object = MibTableColumn
hh3cPUExternalInputAlarmStatus = _Hh3cPUExternalInputAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 1, 1, 2),
    _Hh3cPUExternalInputAlarmStatus_Type()
)
hh3cPUExternalInputAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUExternalInputAlarmStatus.setStatus("current")
_Hh3cPUExternalOutputAlarmTable_Object = MibTable
hh3cPUExternalOutputAlarmTable = _Hh3cPUExternalOutputAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cPUExternalOutputAlarmTable.setStatus("current")
_Hh3cPUExternalOutputAlarmEntry_Object = MibTableRow
hh3cPUExternalOutputAlarmEntry = _Hh3cPUExternalOutputAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 2, 1)
)
hh3cPUExternalOutputAlarmEntry.setIndexNames(
    (0, "HH3C-PU-MAN-MIB", "hh3cPUExternalOutputAlarmChannelID"),
)
if mibBuilder.loadTexts:
    hh3cPUExternalOutputAlarmEntry.setStatus("current")
_Hh3cPUExternalOutputAlarmChannelID_Type = Unsigned32
_Hh3cPUExternalOutputAlarmChannelID_Object = MibTableColumn
hh3cPUExternalOutputAlarmChannelID = _Hh3cPUExternalOutputAlarmChannelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 2, 1, 1),
    _Hh3cPUExternalOutputAlarmChannelID_Type()
)
hh3cPUExternalOutputAlarmChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPUExternalOutputAlarmChannelID.setStatus("current")
_Hh3cPUExternalOutputAlarmStatus_Type = TruthValue
_Hh3cPUExternalOutputAlarmStatus_Object = MibTableColumn
hh3cPUExternalOutputAlarmStatus = _Hh3cPUExternalOutputAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 1, 2, 2, 1, 2),
    _Hh3cPUExternalOutputAlarmStatus_Type()
)
hh3cPUExternalOutputAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUExternalOutputAlarmStatus.setStatus("current")
_Hh3cPUECMan_ObjectIdentity = ObjectIdentity
hh3cPUECMan = _Hh3cPUECMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2)
)
_Hh3cPUECManObjects_ObjectIdentity = ObjectIdentity
hh3cPUECManObjects = _Hh3cPUECManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 1)
)


class _Hh3cPUECCameraOnlines_Type(Unsigned32):
    """Custom type hh3cPUECCameraOnlines based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cPUECCameraOnlines_Type.__name__ = "Unsigned32"
_Hh3cPUECCameraOnlines_Object = MibScalar
hh3cPUECCameraOnlines = _Hh3cPUECCameraOnlines_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 1, 1),
    _Hh3cPUECCameraOnlines_Type()
)
hh3cPUECCameraOnlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUECCameraOnlines.setStatus("current")


class _Hh3cPUECCameraAvailRate_Type(Unsigned32):
    """Custom type hh3cPUECCameraAvailRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cPUECCameraAvailRate_Type.__name__ = "Unsigned32"
_Hh3cPUECCameraAvailRate_Object = MibScalar
hh3cPUECCameraAvailRate = _Hh3cPUECCameraAvailRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 1, 2),
    _Hh3cPUECCameraAvailRate_Type()
)
hh3cPUECCameraAvailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUECCameraAvailRate.setStatus("current")
_Hh3cPUECManTables_ObjectIdentity = ObjectIdentity
hh3cPUECManTables = _Hh3cPUECManTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 2)
)
_Hh3cPUECVideoChannelTable_Object = MibTable
hh3cPUECVideoChannelTable = _Hh3cPUECVideoChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cPUECVideoChannelTable.setStatus("current")
_Hh3cPUECVideoChannelEntry_Object = MibTableRow
hh3cPUECVideoChannelEntry = _Hh3cPUECVideoChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 2, 1, 1)
)
hh3cPUECVideoChannelEntry.setIndexNames(
    (0, "HH3C-PU-MAN-MIB", "hh3cPUECVideoChannelID"),
)
if mibBuilder.loadTexts:
    hh3cPUECVideoChannelEntry.setStatus("current")
_Hh3cPUECVideoChannelID_Type = Unsigned32
_Hh3cPUECVideoChannelID_Object = MibTableColumn
hh3cPUECVideoChannelID = _Hh3cPUECVideoChannelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 2, 1, 1, 1),
    _Hh3cPUECVideoChannelID_Type()
)
hh3cPUECVideoChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPUECVideoChannelID.setStatus("current")


class _Hh3cPUECVideoChannelName_Type(DisplayString):
    """Custom type hh3cPUECVideoChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cPUECVideoChannelName_Type.__name__ = "DisplayString"
_Hh3cPUECVideoChannelName_Object = MibTableColumn
hh3cPUECVideoChannelName = _Hh3cPUECVideoChannelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 2, 1, 1, 2),
    _Hh3cPUECVideoChannelName_Type()
)
hh3cPUECVideoChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUECVideoChannelName.setStatus("current")


class _Hh3cPUECVideoChannelServiceStatus_Type(Bits):
    """Custom type hh3cPUECVideoChannelServiceStatus based on Bits"""
    namedValues = NamedValues(
        *(("kinescope", 2),
          ("snapshot", 3),
          ("unknown", 0),
          ("unused", 1))
    )

_Hh3cPUECVideoChannelServiceStatus_Type.__name__ = "Bits"
_Hh3cPUECVideoChannelServiceStatus_Object = MibTableColumn
hh3cPUECVideoChannelServiceStatus = _Hh3cPUECVideoChannelServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 2, 1, 1, 3),
    _Hh3cPUECVideoChannelServiceStatus_Type()
)
hh3cPUECVideoChannelServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUECVideoChannelServiceStatus.setStatus("current")
_Hh3cPUECManMIBTrap_ObjectIdentity = ObjectIdentity
hh3cPUECManMIBTrap = _Hh3cPUECManMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3)
)
_Hh3cPUECManTrapPrex_ObjectIdentity = ObjectIdentity
hh3cPUECManTrapPrex = _Hh3cPUECManTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0)
)
_Hh3cPUECManTrapObjects_ObjectIdentity = ObjectIdentity
hh3cPUECManTrapObjects = _Hh3cPUECManTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 1)
)
_Hh3cPUECRegionCoordinateX1_Type = Unsigned32
_Hh3cPUECRegionCoordinateX1_Object = MibScalar
hh3cPUECRegionCoordinateX1 = _Hh3cPUECRegionCoordinateX1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 1, 1),
    _Hh3cPUECRegionCoordinateX1_Type()
)
hh3cPUECRegionCoordinateX1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPUECRegionCoordinateX1.setStatus("current")
_Hh3cPUECRegionCoordinateY1_Type = Unsigned32
_Hh3cPUECRegionCoordinateY1_Object = MibScalar
hh3cPUECRegionCoordinateY1 = _Hh3cPUECRegionCoordinateY1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 1, 2),
    _Hh3cPUECRegionCoordinateY1_Type()
)
hh3cPUECRegionCoordinateY1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPUECRegionCoordinateY1.setStatus("current")
_Hh3cPUECRegionCoordinateX2_Type = Unsigned32
_Hh3cPUECRegionCoordinateX2_Object = MibScalar
hh3cPUECRegionCoordinateX2 = _Hh3cPUECRegionCoordinateX2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 1, 3),
    _Hh3cPUECRegionCoordinateX2_Type()
)
hh3cPUECRegionCoordinateX2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPUECRegionCoordinateX2.setStatus("current")
_Hh3cPUECRegionCoordinateY2_Type = Unsigned32
_Hh3cPUECRegionCoordinateY2_Object = MibScalar
hh3cPUECRegionCoordinateY2 = _Hh3cPUECRegionCoordinateY2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 1, 4),
    _Hh3cPUECRegionCoordinateY2_Type()
)
hh3cPUECRegionCoordinateY2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPUECRegionCoordinateY2.setStatus("current")
_Hh3cPUDCMan_ObjectIdentity = ObjectIdentity
hh3cPUDCMan = _Hh3cPUDCMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 3)
)
_Hh3cPUDCManObjects_ObjectIdentity = ObjectIdentity
hh3cPUDCManObjects = _Hh3cPUDCManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 3, 1)
)
_Hh3cPUDCRcvVideoPackets_Type = Counter32
_Hh3cPUDCRcvVideoPackets_Object = MibScalar
hh3cPUDCRcvVideoPackets = _Hh3cPUDCRcvVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 3, 1, 1),
    _Hh3cPUDCRcvVideoPackets_Type()
)
hh3cPUDCRcvVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUDCRcvVideoPackets.setStatus("current")
_Hh3cPUDCRcvVideoRefFrames_Type = Counter32
_Hh3cPUDCRcvVideoRefFrames_Object = MibScalar
hh3cPUDCRcvVideoRefFrames = _Hh3cPUDCRcvVideoRefFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 3, 1, 2),
    _Hh3cPUDCRcvVideoRefFrames_Type()
)
hh3cPUDCRcvVideoRefFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUDCRcvVideoRefFrames.setStatus("current")
_Hh3cPUDCVideoPacketsLoss_Type = Counter32
_Hh3cPUDCVideoPacketsLoss_Object = MibScalar
hh3cPUDCVideoPacketsLoss = _Hh3cPUDCVideoPacketsLoss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 3, 1, 3),
    _Hh3cPUDCVideoPacketsLoss_Type()
)
hh3cPUDCVideoPacketsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUDCVideoPacketsLoss.setStatus("current")
_Hh3cPUDCVideoRefFramesLoss_Type = Counter32
_Hh3cPUDCVideoRefFramesLoss_Object = MibScalar
hh3cPUDCVideoRefFramesLoss = _Hh3cPUDCVideoRefFramesLoss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 3, 1, 4),
    _Hh3cPUDCVideoRefFramesLoss_Type()
)
hh3cPUDCVideoRefFramesLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPUDCVideoRefFramesLoss.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cPUECManExternalSemaphoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 1)
)
hh3cPUECManExternalSemaphoreTrap.setObjects(
    ("HH3C-PU-MAN-MIB", "hh3cPUExternalInputAlarmChannelID")
)
if mibBuilder.loadTexts:
    hh3cPUECManExternalSemaphoreTrap.setStatus(
        "current"
    )

hh3cPUECManVideoLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 2)
)
hh3cPUECManVideoLossTrap.setObjects(
    ("HH3C-PU-MAN-MIB", "hh3cPUECVideoChannelName")
)
if mibBuilder.loadTexts:
    hh3cPUECManVideoLossTrap.setStatus(
        "current"
    )

hh3cPUECManVideoRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 3)
)
hh3cPUECManVideoRecoverTrap.setObjects(
    ("HH3C-PU-MAN-MIB", "hh3cPUECVideoChannelName")
)
if mibBuilder.loadTexts:
    hh3cPUECManVideoRecoverTrap.setStatus(
        "current"
    )

hh3cPUECManMotionDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 4)
)
hh3cPUECManMotionDetectTrap.setObjects(
      *(("HH3C-PU-MAN-MIB", "hh3cPUECVideoChannelName"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateX1"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateY1"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateX2"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    hh3cPUECManMotionDetectTrap.setStatus(
        "current"
    )

hh3cPUECManOnLineFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 5)
)
hh3cPUECManOnLineFailureTrap.setObjects(
    ("HH3C-PU-MAN-MIB", "hh3cPUCMSAddr")
)
if mibBuilder.loadTexts:
    hh3cPUECManOnLineFailureTrap.setStatus(
        "current"
    )

hh3cPUECManConnectionCMSFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 6)
)
hh3cPUECManConnectionCMSFailureTrap.setObjects(
    ("HH3C-PU-MAN-MIB", "hh3cPUCMSAddr")
)
if mibBuilder.loadTexts:
    hh3cPUECManConnectionCMSFailureTrap.setStatus(
        "current"
    )

hh3cPUECManConnectionVerSrvFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 7)
)
hh3cPUECManConnectionVerSrvFailureTrap.setObjects(
    ("HH3C-PU-MAN-MIB", "hh3cPUVersionServerAddr")
)
if mibBuilder.loadTexts:
    hh3cPUECManConnectionVerSrvFailureTrap.setStatus(
        "current"
    )

hh3cPUECManFlashFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 8)
)
if mibBuilder.loadTexts:
    hh3cPUECManFlashFailureTrap.setStatus(
        "current"
    )

hh3cPUECManCameraShelterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 2, 2, 3, 0, 9)
)
hh3cPUECManCameraShelterTrap.setObjects(
      *(("HH3C-PU-MAN-MIB", "hh3cPUECVideoChannelName"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateX1"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateY1"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateX2"),
        ("HH3C-PU-MAN-MIB", "hh3cPUECRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    hh3cPUECManCameraShelterTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PU-MAN-MIB",
    **{"hh3cPUMan": hh3cPUMan,
       "hh3cPUCommonMan": hh3cPUCommonMan,
       "hh3cPUCommonManObjects": hh3cPUCommonManObjects,
       "hh3cPUisOnline": hh3cPUisOnline,
       "hh3cPUCMSAddr": hh3cPUCMSAddr,
       "hh3cPUVersionServerAddr": hh3cPUVersionServerAddr,
       "hh3cPUCommonManTables": hh3cPUCommonManTables,
       "hh3cPUExternalInputAlarmTable": hh3cPUExternalInputAlarmTable,
       "hh3cPUExternalInputAlarmEntry": hh3cPUExternalInputAlarmEntry,
       "hh3cPUExternalInputAlarmChannelID": hh3cPUExternalInputAlarmChannelID,
       "hh3cPUExternalInputAlarmStatus": hh3cPUExternalInputAlarmStatus,
       "hh3cPUExternalOutputAlarmTable": hh3cPUExternalOutputAlarmTable,
       "hh3cPUExternalOutputAlarmEntry": hh3cPUExternalOutputAlarmEntry,
       "hh3cPUExternalOutputAlarmChannelID": hh3cPUExternalOutputAlarmChannelID,
       "hh3cPUExternalOutputAlarmStatus": hh3cPUExternalOutputAlarmStatus,
       "hh3cPUECMan": hh3cPUECMan,
       "hh3cPUECManObjects": hh3cPUECManObjects,
       "hh3cPUECCameraOnlines": hh3cPUECCameraOnlines,
       "hh3cPUECCameraAvailRate": hh3cPUECCameraAvailRate,
       "hh3cPUECManTables": hh3cPUECManTables,
       "hh3cPUECVideoChannelTable": hh3cPUECVideoChannelTable,
       "hh3cPUECVideoChannelEntry": hh3cPUECVideoChannelEntry,
       "hh3cPUECVideoChannelID": hh3cPUECVideoChannelID,
       "hh3cPUECVideoChannelName": hh3cPUECVideoChannelName,
       "hh3cPUECVideoChannelServiceStatus": hh3cPUECVideoChannelServiceStatus,
       "hh3cPUECManMIBTrap": hh3cPUECManMIBTrap,
       "hh3cPUECManTrapPrex": hh3cPUECManTrapPrex,
       "hh3cPUECManExternalSemaphoreTrap": hh3cPUECManExternalSemaphoreTrap,
       "hh3cPUECManVideoLossTrap": hh3cPUECManVideoLossTrap,
       "hh3cPUECManVideoRecoverTrap": hh3cPUECManVideoRecoverTrap,
       "hh3cPUECManMotionDetectTrap": hh3cPUECManMotionDetectTrap,
       "hh3cPUECManOnLineFailureTrap": hh3cPUECManOnLineFailureTrap,
       "hh3cPUECManConnectionCMSFailureTrap": hh3cPUECManConnectionCMSFailureTrap,
       "hh3cPUECManConnectionVerSrvFailureTrap": hh3cPUECManConnectionVerSrvFailureTrap,
       "hh3cPUECManFlashFailureTrap": hh3cPUECManFlashFailureTrap,
       "hh3cPUECManCameraShelterTrap": hh3cPUECManCameraShelterTrap,
       "hh3cPUECManTrapObjects": hh3cPUECManTrapObjects,
       "hh3cPUECRegionCoordinateX1": hh3cPUECRegionCoordinateX1,
       "hh3cPUECRegionCoordinateY1": hh3cPUECRegionCoordinateY1,
       "hh3cPUECRegionCoordinateX2": hh3cPUECRegionCoordinateX2,
       "hh3cPUECRegionCoordinateY2": hh3cPUECRegionCoordinateY2,
       "hh3cPUDCMan": hh3cPUDCMan,
       "hh3cPUDCManObjects": hh3cPUDCManObjects,
       "hh3cPUDCRcvVideoPackets": hh3cPUDCRcvVideoPackets,
       "hh3cPUDCRcvVideoRefFrames": hh3cPUDCRcvVideoRefFrames,
       "hh3cPUDCVideoPacketsLoss": hh3cPUDCVideoPacketsLoss,
       "hh3cPUDCVideoRefFramesLoss": hh3cPUDCVideoRefFramesLoss}
)
