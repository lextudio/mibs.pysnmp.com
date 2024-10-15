# SNMP MIB module (POLYCOM-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLYCOM-VIDEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:14 2024
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
 enterprises,
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
    "enterprises",
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

_Polycom_ObjectIdentity = ObjectIdentity
polycom = _Polycom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2684)
)
_PolycomVideo_ObjectIdentity = ObjectIdentity
polycomVideo = _PolycomVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2684, 1)
)
_PolycomViewStation_ObjectIdentity = ObjectIdentity
polycomViewStation = _PolycomViewStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1)
)
_PolycomVSAuthLocation_Type = Integer32
_PolycomVSAuthLocation_Object = MibScalar
polycomVSAuthLocation = _PolycomVSAuthLocation_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 1),
    _PolycomVSAuthLocation_Type()
)
polycomVSAuthLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSAuthLocation.setStatus("mandatory")
_PolycomVSPhoneNumber_Type = DisplayString
_PolycomVSPhoneNumber_Object = MibScalar
polycomVSPhoneNumber = _PolycomVSPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 2),
    _PolycomVSPhoneNumber_Type()
)
polycomVSPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSPhoneNumber.setStatus("mandatory")
_PolycomVSReason_Type = DisplayString
_PolycomVSReason_Object = MibScalar
polycomVSReason = _PolycomVSReason_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 3),
    _PolycomVSReason_Type()
)
polycomVSReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSReason.setStatus("mandatory")
_PolycomVSPlead_Type = DisplayString
_PolycomVSPlead_Object = MibScalar
polycomVSPlead = _PolycomVSPlead_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 4),
    _PolycomVSPlead_Type()
)
polycomVSPlead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSPlead.setStatus("mandatory")
_PolycomVSMicData_Type = DisplayString
_PolycomVSMicData_Object = MibScalar
polycomVSMicData = _PolycomVSMicData_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 5),
    _PolycomVSMicData_Type()
)
polycomVSMicData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSMicData.setStatus("mandatory")
_PolycomVSAutoAnswerSetting_Type = DisplayString
_PolycomVSAutoAnswerSetting_Object = MibScalar
polycomVSAutoAnswerSetting = _PolycomVSAutoAnswerSetting_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 6),
    _PolycomVSAutoAnswerSetting_Type()
)
polycomVSAutoAnswerSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSAutoAnswerSetting.setStatus("mandatory")
_PolycomVSTimeServerAddress_Type = DisplayString
_PolycomVSTimeServerAddress_Object = MibScalar
polycomVSTimeServerAddress = _PolycomVSTimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 7),
    _PolycomVSTimeServerAddress_Type()
)
polycomVSTimeServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSTimeServerAddress.setStatus("mandatory")
_PolycomVSTimeServerSetting_Type = DisplayString
_PolycomVSTimeServerSetting_Object = MibScalar
polycomVSTimeServerSetting = _PolycomVSTimeServerSetting_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 8),
    _PolycomVSTimeServerSetting_Type()
)
polycomVSTimeServerSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSTimeServerSetting.setStatus("mandatory")
_PolycomVSGDSAddress_Type = DisplayString
_PolycomVSGDSAddress_Object = MibScalar
polycomVSGDSAddress = _PolycomVSGDSAddress_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 9),
    _PolycomVSGDSAddress_Type()
)
polycomVSGDSAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSGDSAddress.setStatus("mandatory")
_PolycomVSGatekeeperAddress_Type = DisplayString
_PolycomVSGatekeeperAddress_Object = MibScalar
polycomVSGatekeeperAddress = _PolycomVSGatekeeperAddress_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 10),
    _PolycomVSGatekeeperAddress_Type()
)
polycomVSGatekeeperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSGatekeeperAddress.setStatus("mandatory")
_PolycomVSPreviousIPAddress_Type = DisplayString
_PolycomVSPreviousIPAddress_Object = MibScalar
polycomVSPreviousIPAddress = _PolycomVSPreviousIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 11),
    _PolycomVSPreviousIPAddress_Type()
)
polycomVSPreviousIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSPreviousIPAddress.setStatus("mandatory")
_PolycomVSCurrentIPAddress_Type = DisplayString
_PolycomVSCurrentIPAddress_Object = MibScalar
polycomVSCurrentIPAddress = _PolycomVSCurrentIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 12),
    _PolycomVSCurrentIPAddress_Type()
)
polycomVSCurrentIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSCurrentIPAddress.setStatus("mandatory")
_PolycomVSPreviousNicType_Type = DisplayString
_PolycomVSPreviousNicType_Object = MibScalar
polycomVSPreviousNicType = _PolycomVSPreviousNicType_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 13),
    _PolycomVSPreviousNicType_Type()
)
polycomVSPreviousNicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSPreviousNicType.setStatus("mandatory")
_PolycomVSCurrentNicType_Type = DisplayString
_PolycomVSCurrentNicType_Object = MibScalar
polycomVSCurrentNicType = _PolycomVSCurrentNicType_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 14),
    _PolycomVSCurrentNicType_Type()
)
polycomVSCurrentNicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSCurrentNicType.setStatus("mandatory")
_PolycomVSNicLineNumber_Type = DisplayString
_PolycomVSNicLineNumber_Object = MibScalar
polycomVSNicLineNumber = _PolycomVSNicLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 15),
    _PolycomVSNicLineNumber_Type()
)
polycomVSNicLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSNicLineNumber.setStatus("mandatory")
_PolycomVSPreviousNicLineCount_Type = DisplayString
_PolycomVSPreviousNicLineCount_Object = MibScalar
polycomVSPreviousNicLineCount = _PolycomVSPreviousNicLineCount_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 16),
    _PolycomVSPreviousNicLineCount_Type()
)
polycomVSPreviousNicLineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSPreviousNicLineCount.setStatus("mandatory")
_PolycomVSCurrentNicLineCount_Type = DisplayString
_PolycomVSCurrentNicLineCount_Object = MibScalar
polycomVSCurrentNicLineCount = _PolycomVSCurrentNicLineCount_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 17),
    _PolycomVSCurrentNicLineCount_Type()
)
polycomVSCurrentNicLineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSCurrentNicLineCount.setStatus("mandatory")
_PolycomVSV35PortsEnabled_Type = DisplayString
_PolycomVSV35PortsEnabled_Object = MibScalar
polycomVSV35PortsEnabled = _PolycomVSV35PortsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 18),
    _PolycomVSV35PortsEnabled_Type()
)
polycomVSV35PortsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSV35PortsEnabled.setStatus("mandatory")
_PolycomVSAuthClientAddress_Type = DisplayString
_PolycomVSAuthClientAddress_Object = MibScalar
polycomVSAuthClientAddress = _PolycomVSAuthClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 19),
    _PolycomVSAuthClientAddress_Type()
)
polycomVSAuthClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSAuthClientAddress.setStatus("mandatory")
_PolycomVSUPnPStatus_Type = DisplayString
_PolycomVSUPnPStatus_Object = MibScalar
polycomVSUPnPStatus = _PolycomVSUPnPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 20),
    _PolycomVSUPnPStatus_Type()
)
polycomVSUPnPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSUPnPStatus.setStatus("mandatory")
_PolycomVSPercentPacketLoss_Type = DisplayString
_PolycomVSPercentPacketLoss_Object = MibScalar
polycomVSPercentPacketLoss = _PolycomVSPercentPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 21),
    _PolycomVSPercentPacketLoss_Type()
)
polycomVSPercentPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSPercentPacketLoss.setStatus("mandatory")
_PolycomVSJitter_Type = DisplayString
_PolycomVSJitter_Object = MibScalar
polycomVSJitter = _PolycomVSJitter_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 22),
    _PolycomVSJitter_Type()
)
polycomVSJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSJitter.setStatus("mandatory")
_PolycomVSLatency_Type = DisplayString
_PolycomVSLatency_Object = MibScalar
polycomVSLatency = _PolycomVSLatency_Object(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 23),
    _PolycomVSLatency_Type()
)
polycomVSLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polycomVSLatency.setStatus("mandatory")
_PolycomAudio_ObjectIdentity = ObjectIdentity
polycomAudio = _PolycomAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2684, 2)
)
_PolycomData_ObjectIdentity = ObjectIdentity
polycomData = _PolycomData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2684, 3)
)

# Managed Objects groups


# Notification objects

loginOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 1)
)
loginOK.setObjects(
      *(("POLYCOM-VIDEO-MIB", "polycomVSAuthLocation"),
        ("POLYCOM-VIDEO-MIB", "polycomVSAuthClientAddress"))
)
if mibBuilder.loadTexts:
    loginOK.setStatus(
        ""
    )

loginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 2)
)
loginFail.setObjects(
      *(("POLYCOM-VIDEO-MIB", "polycomVSAuthLocation"),
        ("POLYCOM-VIDEO-MIB", "polycomVSAuthClientAddress"))
)
if mibBuilder.loadTexts:
    loginFail.setStatus(
        ""
    )

lowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 3)
)
if mibBuilder.loadTexts:
    lowBattery.setStatus(
        ""
    )

callUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 4)
)
callUp.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSPhoneNumber")
)
if mibBuilder.loadTexts:
    callUp.setStatus(
        ""
    )

callDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 5)
)
callDown.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSPhoneNumber")
)
if mibBuilder.loadTexts:
    callDown.setStatus(
        ""
    )

callFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 6)
)
callFail.setObjects(
      *(("POLYCOM-VIDEO-MIB", "polycomVSReason"),
        ("POLYCOM-VIDEO-MIB", "polycomVSPhoneNumber"))
)
if mibBuilder.loadTexts:
    callFail.setStatus(
        ""
    )

userAssist = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 7)
)
userAssist.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSPlead")
)
if mibBuilder.loadTexts:
    userAssist.setStatus(
        ""
    )

visualConcertUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 8)
)
if mibBuilder.loadTexts:
    visualConcertUp.setStatus(
        ""
    )

visualConcertOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 9)
)
if mibBuilder.loadTexts:
    visualConcertOff.setStatus(
        ""
    )

micChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 10)
)
micChange.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSMicData")
)
if mibBuilder.loadTexts:
    micChange.setStatus(
        ""
    )

autoAnswerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 11)
)
autoAnswerChange.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSAutoAnswerSetting")
)
if mibBuilder.loadTexts:
    autoAnswerChange.setStatus(
        ""
    )

timeServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 12)
)
timeServerUp.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSTimeServerAddress")
)
if mibBuilder.loadTexts:
    timeServerUp.setStatus(
        ""
    )

timeServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 13)
)
timeServerDown.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSTimeServerAddress")
)
if mibBuilder.loadTexts:
    timeServerDown.setStatus(
        ""
    )

timeServerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 14)
)
timeServerOn.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSTimeServerSetting")
)
if mibBuilder.loadTexts:
    timeServerOn.setStatus(
        ""
    )

timeServerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 15)
)
if mibBuilder.loadTexts:
    timeServerOff.setStatus(
        ""
    )

gdsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 16)
)
gdsUp.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSGDSAddress")
)
if mibBuilder.loadTexts:
    gdsUp.setStatus(
        ""
    )

gdsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 17)
)
gdsDown.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSGDSAddress")
)
if mibBuilder.loadTexts:
    gdsDown.setStatus(
        ""
    )

gdsOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 18)
)
gdsOff.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSGDSAddress")
)
if mibBuilder.loadTexts:
    gdsOff.setStatus(
        ""
    )

gatekeeperReg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 19)
)
gatekeeperReg.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSGatekeeperAddress")
)
if mibBuilder.loadTexts:
    gatekeeperReg.setStatus(
        ""
    )

gatekeeperDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 20)
)
gatekeeperDown.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSGatekeeperAddress")
)
if mibBuilder.loadTexts:
    gatekeeperDown.setStatus(
        ""
    )

gatekeeperOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 21)
)
if mibBuilder.loadTexts:
    gatekeeperOff.setStatus(
        ""
    )

ipAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 22)
)
ipAddressChange.setObjects(
      *(("POLYCOM-VIDEO-MIB", "polycomVSPreviousIPAddress"),
        ("POLYCOM-VIDEO-MIB", "polycomVSCurrentIPAddress"))
)
if mibBuilder.loadTexts:
    ipAddressChange.setStatus(
        ""
    )

interfaceTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 23)
)
interfaceTypeChange.setObjects(
      *(("POLYCOM-VIDEO-MIB", "polycomVSPreviousNicType"),
        ("POLYCOM-VIDEO-MIB", "polycomVSCurrentNicType"))
)
if mibBuilder.loadTexts:
    interfaceTypeChange.setStatus(
        ""
    )

lineEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 24)
)
lineEnabled.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSNicLineNumber")
)
if mibBuilder.loadTexts:
    lineEnabled.setStatus(
        ""
    )

lineDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 25)
)
lineDisabled.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSNicLineNumber")
)
if mibBuilder.loadTexts:
    lineDisabled.setStatus(
        ""
    )

lineUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 26)
)
lineUp.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSNicLineNumber")
)
if mibBuilder.loadTexts:
    lineUp.setStatus(
        ""
    )

lineDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 27)
)
lineDown.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSNicLineNumber")
)
if mibBuilder.loadTexts:
    lineDown.setStatus(
        ""
    )

v35PortsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 28)
)
v35PortsEnabled.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSV35PortsEnabled")
)
if mibBuilder.loadTexts:
    v35PortsEnabled.setStatus(
        ""
    )

lineCountChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 29)
)
lineCountChange.setObjects(
      *(("POLYCOM-VIDEO-MIB", "polycomVSPreviousNicLineCount"),
        ("POLYCOM-VIDEO-MIB", "polycomVSCurrentNicLineCount"))
)
if mibBuilder.loadTexts:
    lineCountChange.setStatus(
        ""
    )

mainCameraUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 30)
)
if mibBuilder.loadTexts:
    mainCameraUp.setStatus(
        ""
    )

mainCameraDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 31)
)
if mibBuilder.loadTexts:
    mainCameraDown.setStatus(
        ""
    )

upnpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 32)
)
upnpChange.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSUPnPStatus")
)
if mibBuilder.loadTexts:
    upnpChange.setStatus(
        ""
    )

percentPacketLossExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 33)
)
percentPacketLossExcessive.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSPercentPacketLoss")
)
if mibBuilder.loadTexts:
    percentPacketLossExcessive.setStatus(
        ""
    )

jitterExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 34)
)
jitterExcessive.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSJitter")
)
if mibBuilder.loadTexts:
    jitterExcessive.setStatus(
        ""
    )

latencyExcessive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2684, 1, 1, 0, 35)
)
latencyExcessive.setObjects(
    ("POLYCOM-VIDEO-MIB", "polycomVSLatency")
)
if mibBuilder.loadTexts:
    latencyExcessive.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLYCOM-VIDEO-MIB",
    **{"polycom": polycom,
       "polycomVideo": polycomVideo,
       "polycomViewStation": polycomViewStation,
       "loginOK": loginOK,
       "loginFail": loginFail,
       "lowBattery": lowBattery,
       "callUp": callUp,
       "callDown": callDown,
       "callFail": callFail,
       "userAssist": userAssist,
       "visualConcertUp": visualConcertUp,
       "visualConcertOff": visualConcertOff,
       "micChange": micChange,
       "autoAnswerChange": autoAnswerChange,
       "timeServerUp": timeServerUp,
       "timeServerDown": timeServerDown,
       "timeServerOn": timeServerOn,
       "timeServerOff": timeServerOff,
       "gdsUp": gdsUp,
       "gdsDown": gdsDown,
       "gdsOff": gdsOff,
       "gatekeeperReg": gatekeeperReg,
       "gatekeeperDown": gatekeeperDown,
       "gatekeeperOff": gatekeeperOff,
       "ipAddressChange": ipAddressChange,
       "interfaceTypeChange": interfaceTypeChange,
       "lineEnabled": lineEnabled,
       "lineDisabled": lineDisabled,
       "lineUp": lineUp,
       "lineDown": lineDown,
       "v35PortsEnabled": v35PortsEnabled,
       "lineCountChange": lineCountChange,
       "mainCameraUp": mainCameraUp,
       "mainCameraDown": mainCameraDown,
       "upnpChange": upnpChange,
       "percentPacketLossExcessive": percentPacketLossExcessive,
       "jitterExcessive": jitterExcessive,
       "latencyExcessive": latencyExcessive,
       "polycomVSAuthLocation": polycomVSAuthLocation,
       "polycomVSPhoneNumber": polycomVSPhoneNumber,
       "polycomVSReason": polycomVSReason,
       "polycomVSPlead": polycomVSPlead,
       "polycomVSMicData": polycomVSMicData,
       "polycomVSAutoAnswerSetting": polycomVSAutoAnswerSetting,
       "polycomVSTimeServerAddress": polycomVSTimeServerAddress,
       "polycomVSTimeServerSetting": polycomVSTimeServerSetting,
       "polycomVSGDSAddress": polycomVSGDSAddress,
       "polycomVSGatekeeperAddress": polycomVSGatekeeperAddress,
       "polycomVSPreviousIPAddress": polycomVSPreviousIPAddress,
       "polycomVSCurrentIPAddress": polycomVSCurrentIPAddress,
       "polycomVSPreviousNicType": polycomVSPreviousNicType,
       "polycomVSCurrentNicType": polycomVSCurrentNicType,
       "polycomVSNicLineNumber": polycomVSNicLineNumber,
       "polycomVSPreviousNicLineCount": polycomVSPreviousNicLineCount,
       "polycomVSCurrentNicLineCount": polycomVSCurrentNicLineCount,
       "polycomVSV35PortsEnabled": polycomVSV35PortsEnabled,
       "polycomVSAuthClientAddress": polycomVSAuthClientAddress,
       "polycomVSUPnPStatus": polycomVSUPnPStatus,
       "polycomVSPercentPacketLoss": polycomVSPercentPacketLoss,
       "polycomVSJitter": polycomVSJitter,
       "polycomVSLatency": polycomVSLatency,
       "polycomAudio": polycomAudio,
       "polycomData": polycomData}
)
