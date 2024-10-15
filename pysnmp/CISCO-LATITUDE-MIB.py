# SNMP MIB module (CISCO-LATITUDE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LATITUDE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:54 2024
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

latitudeComm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7185)
)
latitudeComm.setRevisions(
        ("2004-08-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LatitudeReg_ObjectIdentity = ObjectIdentity
latitudeReg = _LatitudeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 1)
)
_LatitudeModules_ObjectIdentity = ObjectIdentity
latitudeModules = _LatitudeModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 1, 1)
)
_LatitudeGeneric_ObjectIdentity = ObjectIdentity
latitudeGeneric = _LatitudeGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 2)
)
_LatitudeProducts_ObjectIdentity = ObjectIdentity
latitudeProducts = _LatitudeProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3)
)
_Meetingplace_ObjectIdentity = ObjectIdentity
meetingplace = _Meetingplace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1)
)
_MeetingplaceConfs_ObjectIdentity = ObjectIdentity
meetingplaceConfs = _MeetingplaceConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 1)
)
_CiscoLatitudeMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLatitudeMIBCompliances = _CiscoLatitudeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 1)
)
_CiscoLatitudeMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLatitudeMIBGroups = _CiscoLatitudeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 2)
)
_MeetingplaceObjs_ObjectIdentity = ObjectIdentity
meetingplaceObjs = _MeetingplaceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 2)
)
_MeetingplaceEvents_ObjectIdentity = ObjectIdentity
meetingplaceEvents = _MeetingplaceEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3)
)
_MeetingplaceEventsV2_ObjectIdentity = ObjectIdentity
meetingplaceEventsV2 = _MeetingplaceEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0)
)


class _MpExCode_Type(Integer32):
    """Custom type mpExCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MpExCode_Type.__name__ = "Integer32"
_MpExCode_Object = MibScalar
mpExCode = _MpExCode_Object(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 1),
    _MpExCode_Type()
)
mpExCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpExCode.setStatus("current")


class _MpSysUnit_Type(Integer32):
    """Custom type mpSysUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MpSysUnit_Type.__name__ = "Integer32"
_MpSysUnit_Object = MibScalar
mpSysUnit = _MpSysUnit_Object(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 2),
    _MpSysUnit_Type()
)
mpSysUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpSysUnit.setStatus("current")


class _MpHwDev_Type(Integer32):
    """Custom type mpHwDev based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("mpAnalogBlade", 13),
          ("mpDSPMSC", 10),
          ("mpDSPPRC", 11),
          ("mpDisketteDrive", 6),
          ("mpE1Blade", 17),
          ("mpE1Network", 18),
          ("mpEthernet", 7),
          ("mpHardDrive", 5),
          ("mpMainMemory", 16),
          ("mpModem", 8),
          ("mpPowerSupply", 2),
          ("mpSerialPort", 3),
          ("mpSystemIntegrityCard", 15),
          ("mpSystemMisc", 9),
          ("mpT1Blade", 12),
          ("mpT1Network", 14),
          ("mpTapeDrive", 4),
          ("mpTemperature", 1),
          ("mpVoIPBlade", 19))
    )


_MpHwDev_Type.__name__ = "Integer32"
_MpHwDev_Object = MibScalar
mpHwDev = _MpHwDev_Object(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 3),
    _MpHwDev_Type()
)
mpHwDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpHwDev.setStatus("current")


class _MpHwUnit_Type(Integer32):
    """Custom type mpHwUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MpHwUnit_Type.__name__ = "Integer32"
_MpHwUnit_Object = MibScalar
mpHwUnit = _MpHwUnit_Object(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 4),
    _MpHwUnit_Type()
)
mpHwUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpHwUnit.setStatus("current")


class _MpHwSlot_Type(Integer32):
    """Custom type mpHwSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MpHwSlot_Type.__name__ = "Integer32"
_MpHwSlot_Object = MibScalar
mpHwSlot = _MpHwSlot_Object(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 5),
    _MpHwSlot_Type()
)
mpHwSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpHwSlot.setStatus("current")


class _MpHwPort_Type(Integer32):
    """Custom type mpHwPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MpHwPort_Type.__name__ = "Integer32"
_MpHwPort_Object = MibScalar
mpHwPort = _MpHwPort_Object(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 6),
    _MpHwPort_Type()
)
mpHwPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpHwPort.setStatus("current")


class _MpAlarmDesc_Type(DisplayString):
    """Custom type mpAlarmDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MpAlarmDesc_Type.__name__ = "DisplayString"
_MpAlarmDesc_Object = MibScalar
mpAlarmDesc = _MpAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 7),
    _MpAlarmDesc_Type()
)
mpAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpAlarmDesc.setStatus("current")

# Managed Objects groups

ciscoLatitudeAlarmGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 2, 1)
)
ciscoLatitudeAlarmGroupRev1.setObjects(
      *(("CISCO-LATITUDE-MIB", "mpExCode"),
        ("CISCO-LATITUDE-MIB", "mpSysUnit"),
        ("CISCO-LATITUDE-MIB", "mpHwDev"),
        ("CISCO-LATITUDE-MIB", "mpHwUnit"),
        ("CISCO-LATITUDE-MIB", "mpHwSlot"),
        ("CISCO-LATITUDE-MIB", "mpHwPort"),
        ("CISCO-LATITUDE-MIB", "mpAlarmDesc"))
)
if mibBuilder.loadTexts:
    ciscoLatitudeAlarmGroupRev1.setStatus("current")


# Notification objects

mpT1Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    mpT1Down.setStatus(
        "current"
    )

mpGWSimAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    mpGWSimAlarm.setStatus(
        "current"
    )

mpMajHwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 3)
)
mpMajHwAlarm.setObjects(
      *(("CISCO-LATITUDE-MIB", "mpExCode"),
        ("CISCO-LATITUDE-MIB", "mpSysUnit"),
        ("CISCO-LATITUDE-MIB", "mpHwDev"),
        ("CISCO-LATITUDE-MIB", "mpHwUnit"),
        ("CISCO-LATITUDE-MIB", "mpHwSlot"),
        ("CISCO-LATITUDE-MIB", "mpHwPort"))
)
if mibBuilder.loadTexts:
    mpMajHwAlarm.setStatus(
        "current"
    )

mpMinHwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 4)
)
mpMinHwAlarm.setObjects(
      *(("CISCO-LATITUDE-MIB", "mpExCode"),
        ("CISCO-LATITUDE-MIB", "mpSysUnit"),
        ("CISCO-LATITUDE-MIB", "mpHwDev"),
        ("CISCO-LATITUDE-MIB", "mpHwUnit"),
        ("CISCO-LATITUDE-MIB", "mpHwSlot"),
        ("CISCO-LATITUDE-MIB", "mpHwPort"))
)
if mibBuilder.loadTexts:
    mpMinHwAlarm.setStatus(
        "current"
    )

mpMajSwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 5)
)
mpMajSwAlarm.setObjects(
      *(("CISCO-LATITUDE-MIB", "mpExCode"),
        ("CISCO-LATITUDE-MIB", "mpSysUnit"),
        ("CISCO-LATITUDE-MIB", "mpAlarmDesc"))
)
if mibBuilder.loadTexts:
    mpMajSwAlarm.setStatus(
        "current"
    )

mpMinSwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 3, 0, 6)
)
mpMinSwAlarm.setObjects(
      *(("CISCO-LATITUDE-MIB", "mpExCode"),
        ("CISCO-LATITUDE-MIB", "mpSysUnit"),
        ("CISCO-LATITUDE-MIB", "mpAlarmDesc"))
)
if mibBuilder.loadTexts:
    mpMinSwAlarm.setStatus(
        "current"
    )


# Notifications groups

ciscoLatitudeNotifsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 2, 2)
)
ciscoLatitudeNotifsGroupRev1.setObjects(
      *(("CISCO-LATITUDE-MIB", "mpT1Down"),
        ("CISCO-LATITUDE-MIB", "mpGWSimAlarm"),
        ("CISCO-LATITUDE-MIB", "mpMajHwAlarm"),
        ("CISCO-LATITUDE-MIB", "mpMinHwAlarm"),
        ("CISCO-LATITUDE-MIB", "mpMajSwAlarm"),
        ("CISCO-LATITUDE-MIB", "mpMinSwAlarm"))
)
if mibBuilder.loadTexts:
    ciscoLatitudeNotifsGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLatitudeMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7185, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLatitudeMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LATITUDE-MIB",
    **{"latitudeComm": latitudeComm,
       "latitudeReg": latitudeReg,
       "latitudeModules": latitudeModules,
       "latitudeGeneric": latitudeGeneric,
       "latitudeProducts": latitudeProducts,
       "meetingplace": meetingplace,
       "meetingplaceConfs": meetingplaceConfs,
       "ciscoLatitudeMIBCompliances": ciscoLatitudeMIBCompliances,
       "ciscoLatitudeMIBComplianceRev1": ciscoLatitudeMIBComplianceRev1,
       "ciscoLatitudeMIBGroups": ciscoLatitudeMIBGroups,
       "ciscoLatitudeAlarmGroupRev1": ciscoLatitudeAlarmGroupRev1,
       "ciscoLatitudeNotifsGroupRev1": ciscoLatitudeNotifsGroupRev1,
       "meetingplaceObjs": meetingplaceObjs,
       "meetingplaceEvents": meetingplaceEvents,
       "meetingplaceEventsV2": meetingplaceEventsV2,
       "mpT1Down": mpT1Down,
       "mpGWSimAlarm": mpGWSimAlarm,
       "mpMajHwAlarm": mpMajHwAlarm,
       "mpMinHwAlarm": mpMinHwAlarm,
       "mpMajSwAlarm": mpMajSwAlarm,
       "mpMinSwAlarm": mpMinSwAlarm,
       "mpExCode": mpExCode,
       "mpSysUnit": mpSysUnit,
       "mpHwDev": mpHwDev,
       "mpHwUnit": mpHwUnit,
       "mpHwSlot": mpHwSlot,
       "mpHwPort": mpHwPort,
       "mpAlarmDesc": mpAlarmDesc}
)
