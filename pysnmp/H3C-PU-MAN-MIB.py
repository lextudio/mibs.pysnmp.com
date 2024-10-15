# SNMP MIB module (H3C-PU-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-PU-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:13 2024
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

(h3cSurveillanceMIB,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cSurveillanceMIB")

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

h3cPUMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPUCommonMan_ObjectIdentity = ObjectIdentity
h3cPUCommonMan = _H3cPUCommonMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1)
)
_H3cPUCommonManObjects_ObjectIdentity = ObjectIdentity
h3cPUCommonManObjects = _H3cPUCommonManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1)
)
_H3cPUisOnline_Type = TruthValue
_H3cPUisOnline_Object = MibScalar
h3cPUisOnline = _H3cPUisOnline_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1, 1),
    _H3cPUisOnline_Type()
)
h3cPUisOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUisOnline.setStatus("current")
_H3cPUCMSAddr_Type = IpAddress
_H3cPUCMSAddr_Object = MibScalar
h3cPUCMSAddr = _H3cPUCMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1, 2),
    _H3cPUCMSAddr_Type()
)
h3cPUCMSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUCMSAddr.setStatus("current")
_H3cPUVersionServerAddr_Type = IpAddress
_H3cPUVersionServerAddr_Object = MibScalar
h3cPUVersionServerAddr = _H3cPUVersionServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 1, 3),
    _H3cPUVersionServerAddr_Type()
)
h3cPUVersionServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUVersionServerAddr.setStatus("current")
_H3cPUCommonManTables_ObjectIdentity = ObjectIdentity
h3cPUCommonManTables = _H3cPUCommonManTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2)
)
_H3cPUExternalInputAlarmTable_Object = MibTable
h3cPUExternalInputAlarmTable = _H3cPUExternalInputAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cPUExternalInputAlarmTable.setStatus("current")
_H3cPUExternalInputAlarmEntry_Object = MibTableRow
h3cPUExternalInputAlarmEntry = _H3cPUExternalInputAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1, 1)
)
h3cPUExternalInputAlarmEntry.setIndexNames(
    (0, "H3C-PU-MAN-MIB", "h3cPUExternalInputAlarmChannelID"),
)
if mibBuilder.loadTexts:
    h3cPUExternalInputAlarmEntry.setStatus("current")
_H3cPUExternalInputAlarmChannelID_Type = Unsigned32
_H3cPUExternalInputAlarmChannelID_Object = MibTableColumn
h3cPUExternalInputAlarmChannelID = _H3cPUExternalInputAlarmChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1, 1, 1),
    _H3cPUExternalInputAlarmChannelID_Type()
)
h3cPUExternalInputAlarmChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPUExternalInputAlarmChannelID.setStatus("current")
_H3cPUExternalInputAlarmStatus_Type = TruthValue
_H3cPUExternalInputAlarmStatus_Object = MibTableColumn
h3cPUExternalInputAlarmStatus = _H3cPUExternalInputAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 1, 1, 2),
    _H3cPUExternalInputAlarmStatus_Type()
)
h3cPUExternalInputAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUExternalInputAlarmStatus.setStatus("current")
_H3cPUExternalOutputAlarmTable_Object = MibTable
h3cPUExternalOutputAlarmTable = _H3cPUExternalOutputAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cPUExternalOutputAlarmTable.setStatus("current")
_H3cPUExternalOutputAlarmEntry_Object = MibTableRow
h3cPUExternalOutputAlarmEntry = _H3cPUExternalOutputAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2, 1)
)
h3cPUExternalOutputAlarmEntry.setIndexNames(
    (0, "H3C-PU-MAN-MIB", "h3cPUExternalOutputAlarmChannelID"),
)
if mibBuilder.loadTexts:
    h3cPUExternalOutputAlarmEntry.setStatus("current")
_H3cPUExternalOutputAlarmChannelID_Type = Unsigned32
_H3cPUExternalOutputAlarmChannelID_Object = MibTableColumn
h3cPUExternalOutputAlarmChannelID = _H3cPUExternalOutputAlarmChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2, 1, 1),
    _H3cPUExternalOutputAlarmChannelID_Type()
)
h3cPUExternalOutputAlarmChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPUExternalOutputAlarmChannelID.setStatus("current")
_H3cPUExternalOutputAlarmStatus_Type = TruthValue
_H3cPUExternalOutputAlarmStatus_Object = MibTableColumn
h3cPUExternalOutputAlarmStatus = _H3cPUExternalOutputAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 1, 2, 2, 1, 2),
    _H3cPUExternalOutputAlarmStatus_Type()
)
h3cPUExternalOutputAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUExternalOutputAlarmStatus.setStatus("current")
_H3cPUECMan_ObjectIdentity = ObjectIdentity
h3cPUECMan = _H3cPUECMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2)
)
_H3cPUECManObjects_ObjectIdentity = ObjectIdentity
h3cPUECManObjects = _H3cPUECManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 1)
)


class _H3cPUECCameraOnlines_Type(Unsigned32):
    """Custom type h3cPUECCameraOnlines based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cPUECCameraOnlines_Type.__name__ = "Unsigned32"
_H3cPUECCameraOnlines_Object = MibScalar
h3cPUECCameraOnlines = _H3cPUECCameraOnlines_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 1, 1),
    _H3cPUECCameraOnlines_Type()
)
h3cPUECCameraOnlines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUECCameraOnlines.setStatus("current")


class _H3cPUECCameraAvailRate_Type(Unsigned32):
    """Custom type h3cPUECCameraAvailRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cPUECCameraAvailRate_Type.__name__ = "Unsigned32"
_H3cPUECCameraAvailRate_Object = MibScalar
h3cPUECCameraAvailRate = _H3cPUECCameraAvailRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 1, 2),
    _H3cPUECCameraAvailRate_Type()
)
h3cPUECCameraAvailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUECCameraAvailRate.setStatus("current")
_H3cPUECManTables_ObjectIdentity = ObjectIdentity
h3cPUECManTables = _H3cPUECManTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2)
)
_H3cPUECVideoChannelTable_Object = MibTable
h3cPUECVideoChannelTable = _H3cPUECVideoChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cPUECVideoChannelTable.setStatus("current")
_H3cPUECVideoChannelEntry_Object = MibTableRow
h3cPUECVideoChannelEntry = _H3cPUECVideoChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1)
)
h3cPUECVideoChannelEntry.setIndexNames(
    (0, "H3C-PU-MAN-MIB", "h3cPUECVideoChannelID"),
)
if mibBuilder.loadTexts:
    h3cPUECVideoChannelEntry.setStatus("current")
_H3cPUECVideoChannelID_Type = Unsigned32
_H3cPUECVideoChannelID_Object = MibTableColumn
h3cPUECVideoChannelID = _H3cPUECVideoChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1, 1),
    _H3cPUECVideoChannelID_Type()
)
h3cPUECVideoChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPUECVideoChannelID.setStatus("current")


class _H3cPUECVideoChannelName_Type(DisplayString):
    """Custom type h3cPUECVideoChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cPUECVideoChannelName_Type.__name__ = "DisplayString"
_H3cPUECVideoChannelName_Object = MibTableColumn
h3cPUECVideoChannelName = _H3cPUECVideoChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1, 2),
    _H3cPUECVideoChannelName_Type()
)
h3cPUECVideoChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUECVideoChannelName.setStatus("current")


class _H3cPUECVideoChannelServiceStatus_Type(Bits):
    """Custom type h3cPUECVideoChannelServiceStatus based on Bits"""
    namedValues = NamedValues(
        *(("kinescope", 2),
          ("snapshot", 3),
          ("unknown", 0),
          ("unused", 1))
    )

_H3cPUECVideoChannelServiceStatus_Type.__name__ = "Bits"
_H3cPUECVideoChannelServiceStatus_Object = MibTableColumn
h3cPUECVideoChannelServiceStatus = _H3cPUECVideoChannelServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 2, 1, 1, 3),
    _H3cPUECVideoChannelServiceStatus_Type()
)
h3cPUECVideoChannelServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUECVideoChannelServiceStatus.setStatus("current")
_H3cPUECManMIBTrap_ObjectIdentity = ObjectIdentity
h3cPUECManMIBTrap = _H3cPUECManMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3)
)
_H3cPUECManTrapPrex_ObjectIdentity = ObjectIdentity
h3cPUECManTrapPrex = _H3cPUECManTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0)
)
_H3cPUECManTrapObjects_ObjectIdentity = ObjectIdentity
h3cPUECManTrapObjects = _H3cPUECManTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1)
)
_H3cPUECRegionCoordinateX1_Type = Unsigned32
_H3cPUECRegionCoordinateX1_Object = MibScalar
h3cPUECRegionCoordinateX1 = _H3cPUECRegionCoordinateX1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 1),
    _H3cPUECRegionCoordinateX1_Type()
)
h3cPUECRegionCoordinateX1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPUECRegionCoordinateX1.setStatus("current")
_H3cPUECRegionCoordinateY1_Type = Unsigned32
_H3cPUECRegionCoordinateY1_Object = MibScalar
h3cPUECRegionCoordinateY1 = _H3cPUECRegionCoordinateY1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 2),
    _H3cPUECRegionCoordinateY1_Type()
)
h3cPUECRegionCoordinateY1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPUECRegionCoordinateY1.setStatus("current")
_H3cPUECRegionCoordinateX2_Type = Unsigned32
_H3cPUECRegionCoordinateX2_Object = MibScalar
h3cPUECRegionCoordinateX2 = _H3cPUECRegionCoordinateX2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 3),
    _H3cPUECRegionCoordinateX2_Type()
)
h3cPUECRegionCoordinateX2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPUECRegionCoordinateX2.setStatus("current")
_H3cPUECRegionCoordinateY2_Type = Unsigned32
_H3cPUECRegionCoordinateY2_Object = MibScalar
h3cPUECRegionCoordinateY2 = _H3cPUECRegionCoordinateY2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 1, 4),
    _H3cPUECRegionCoordinateY2_Type()
)
h3cPUECRegionCoordinateY2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPUECRegionCoordinateY2.setStatus("current")
_H3cPUDCMan_ObjectIdentity = ObjectIdentity
h3cPUDCMan = _H3cPUDCMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3)
)
_H3cPUDCManObjects_ObjectIdentity = ObjectIdentity
h3cPUDCManObjects = _H3cPUDCManObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1)
)
_H3cPUDCRcvVideoPackets_Type = Counter32
_H3cPUDCRcvVideoPackets_Object = MibScalar
h3cPUDCRcvVideoPackets = _H3cPUDCRcvVideoPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 1),
    _H3cPUDCRcvVideoPackets_Type()
)
h3cPUDCRcvVideoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUDCRcvVideoPackets.setStatus("current")
_H3cPUDCRcvVideoRefFrames_Type = Counter32
_H3cPUDCRcvVideoRefFrames_Object = MibScalar
h3cPUDCRcvVideoRefFrames = _H3cPUDCRcvVideoRefFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 2),
    _H3cPUDCRcvVideoRefFrames_Type()
)
h3cPUDCRcvVideoRefFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUDCRcvVideoRefFrames.setStatus("current")
_H3cPUDCVideoPacketsLoss_Type = Counter32
_H3cPUDCVideoPacketsLoss_Object = MibScalar
h3cPUDCVideoPacketsLoss = _H3cPUDCVideoPacketsLoss_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 3),
    _H3cPUDCVideoPacketsLoss_Type()
)
h3cPUDCVideoPacketsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUDCVideoPacketsLoss.setStatus("current")
_H3cPUDCVideoRefFramesLoss_Type = Counter32
_H3cPUDCVideoRefFramesLoss_Object = MibScalar
h3cPUDCVideoRefFramesLoss = _H3cPUDCVideoRefFramesLoss_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 3, 1, 4),
    _H3cPUDCVideoRefFramesLoss_Type()
)
h3cPUDCVideoRefFramesLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPUDCVideoRefFramesLoss.setStatus("current")

# Managed Objects groups


# Notification objects

h3cPUECManExternalSemaphoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 1)
)
h3cPUECManExternalSemaphoreTrap.setObjects(
    ("H3C-PU-MAN-MIB", "h3cPUExternalInputAlarmChannelID")
)
if mibBuilder.loadTexts:
    h3cPUECManExternalSemaphoreTrap.setStatus(
        "current"
    )

h3cPUECManVideoLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 2)
)
h3cPUECManVideoLossTrap.setObjects(
    ("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName")
)
if mibBuilder.loadTexts:
    h3cPUECManVideoLossTrap.setStatus(
        "current"
    )

h3cPUECManVideoRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 3)
)
h3cPUECManVideoRecoverTrap.setObjects(
    ("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName")
)
if mibBuilder.loadTexts:
    h3cPUECManVideoRecoverTrap.setStatus(
        "current"
    )

h3cPUECManMotionDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 4)
)
h3cPUECManMotionDetectTrap.setObjects(
      *(("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX1"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY1"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX2"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    h3cPUECManMotionDetectTrap.setStatus(
        "current"
    )

h3cPUECManOnLineFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 5)
)
h3cPUECManOnLineFailureTrap.setObjects(
    ("H3C-PU-MAN-MIB", "h3cPUCMSAddr")
)
if mibBuilder.loadTexts:
    h3cPUECManOnLineFailureTrap.setStatus(
        "current"
    )

h3cPUECManConnectionCMSFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 6)
)
h3cPUECManConnectionCMSFailureTrap.setObjects(
    ("H3C-PU-MAN-MIB", "h3cPUCMSAddr")
)
if mibBuilder.loadTexts:
    h3cPUECManConnectionCMSFailureTrap.setStatus(
        "current"
    )

h3cPUECManConnectionVerSrvFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 7)
)
h3cPUECManConnectionVerSrvFailureTrap.setObjects(
    ("H3C-PU-MAN-MIB", "h3cPUVersionServerAddr")
)
if mibBuilder.loadTexts:
    h3cPUECManConnectionVerSrvFailureTrap.setStatus(
        "current"
    )

h3cPUECManFlashFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 8)
)
if mibBuilder.loadTexts:
    h3cPUECManFlashFailureTrap.setStatus(
        "current"
    )

h3cPUECManCameraShelterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 2, 2, 3, 0, 9)
)
h3cPUECManCameraShelterTrap.setObjects(
      *(("H3C-PU-MAN-MIB", "h3cPUECVideoChannelName"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX1"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY1"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateX2"),
        ("H3C-PU-MAN-MIB", "h3cPUECRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    h3cPUECManCameraShelterTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PU-MAN-MIB",
    **{"h3cPUMan": h3cPUMan,
       "h3cPUCommonMan": h3cPUCommonMan,
       "h3cPUCommonManObjects": h3cPUCommonManObjects,
       "h3cPUisOnline": h3cPUisOnline,
       "h3cPUCMSAddr": h3cPUCMSAddr,
       "h3cPUVersionServerAddr": h3cPUVersionServerAddr,
       "h3cPUCommonManTables": h3cPUCommonManTables,
       "h3cPUExternalInputAlarmTable": h3cPUExternalInputAlarmTable,
       "h3cPUExternalInputAlarmEntry": h3cPUExternalInputAlarmEntry,
       "h3cPUExternalInputAlarmChannelID": h3cPUExternalInputAlarmChannelID,
       "h3cPUExternalInputAlarmStatus": h3cPUExternalInputAlarmStatus,
       "h3cPUExternalOutputAlarmTable": h3cPUExternalOutputAlarmTable,
       "h3cPUExternalOutputAlarmEntry": h3cPUExternalOutputAlarmEntry,
       "h3cPUExternalOutputAlarmChannelID": h3cPUExternalOutputAlarmChannelID,
       "h3cPUExternalOutputAlarmStatus": h3cPUExternalOutputAlarmStatus,
       "h3cPUECMan": h3cPUECMan,
       "h3cPUECManObjects": h3cPUECManObjects,
       "h3cPUECCameraOnlines": h3cPUECCameraOnlines,
       "h3cPUECCameraAvailRate": h3cPUECCameraAvailRate,
       "h3cPUECManTables": h3cPUECManTables,
       "h3cPUECVideoChannelTable": h3cPUECVideoChannelTable,
       "h3cPUECVideoChannelEntry": h3cPUECVideoChannelEntry,
       "h3cPUECVideoChannelID": h3cPUECVideoChannelID,
       "h3cPUECVideoChannelName": h3cPUECVideoChannelName,
       "h3cPUECVideoChannelServiceStatus": h3cPUECVideoChannelServiceStatus,
       "h3cPUECManMIBTrap": h3cPUECManMIBTrap,
       "h3cPUECManTrapPrex": h3cPUECManTrapPrex,
       "h3cPUECManExternalSemaphoreTrap": h3cPUECManExternalSemaphoreTrap,
       "h3cPUECManVideoLossTrap": h3cPUECManVideoLossTrap,
       "h3cPUECManVideoRecoverTrap": h3cPUECManVideoRecoverTrap,
       "h3cPUECManMotionDetectTrap": h3cPUECManMotionDetectTrap,
       "h3cPUECManOnLineFailureTrap": h3cPUECManOnLineFailureTrap,
       "h3cPUECManConnectionCMSFailureTrap": h3cPUECManConnectionCMSFailureTrap,
       "h3cPUECManConnectionVerSrvFailureTrap": h3cPUECManConnectionVerSrvFailureTrap,
       "h3cPUECManFlashFailureTrap": h3cPUECManFlashFailureTrap,
       "h3cPUECManCameraShelterTrap": h3cPUECManCameraShelterTrap,
       "h3cPUECManTrapObjects": h3cPUECManTrapObjects,
       "h3cPUECRegionCoordinateX1": h3cPUECRegionCoordinateX1,
       "h3cPUECRegionCoordinateY1": h3cPUECRegionCoordinateY1,
       "h3cPUECRegionCoordinateX2": h3cPUECRegionCoordinateX2,
       "h3cPUECRegionCoordinateY2": h3cPUECRegionCoordinateY2,
       "h3cPUDCMan": h3cPUDCMan,
       "h3cPUDCManObjects": h3cPUDCManObjects,
       "h3cPUDCRcvVideoPackets": h3cPUDCRcvVideoPackets,
       "h3cPUDCRcvVideoRefFrames": h3cPUDCRcvVideoRefFrames,
       "h3cPUDCVideoPacketsLoss": h3cPUDCVideoPacketsLoss,
       "h3cPUDCVideoRefFramesLoss": h3cPUDCVideoRefFramesLoss}
)
