# SNMP MIB module (ADTRAN-AOS-POWER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-POWER
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:12 2024
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

(adGenAOSConformance,
 adGenAOSPower) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSConformance",
    "adGenAOSPower")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenAOSPowerMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1)
)
adGenAOSPowerMonitor.setRevisions(
        ("2010-09-10 00:00",
         "2013-02-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdEpsPowerDeliveryStateTC(Integer32, TextualConvention):
    status = "current"
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
        *(("delivering", 1),
          ("failed", 3),
          ("notDelivering", 2),
          ("unknown", 4))
    )



class AdRpsPowerDeliveryStateTC(Integer32, TextualConvention):
    status = "current"
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
        *(("available", 4),
          ("busy", 2),
          ("delivering", 3),
          ("failed", 1),
          ("unknown", 5))
    )



class AdPowerConnectionStateTC(Integer32, TextualConvention):
    status = "current"
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
        *(("connected", 1),
          ("notApplicable", 3),
          ("notConnected", 2),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenAOSPowerTraps_ObjectIdentity = ObjectIdentity
adGenAOSPowerTraps = _AdGenAOSPowerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0)
)
_AdGenAOSPowerRollOverCtl_ObjectIdentity = ObjectIdentity
adGenAOSPowerRollOverCtl = _AdGenAOSPowerRollOverCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1)
)
_AdGenAOSPowerRolloverOnAC_Type = TruthValue
_AdGenAOSPowerRolloverOnAC_Object = MibScalar
adGenAOSPowerRolloverOnAC = _AdGenAOSPowerRolloverOnAC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 1),
    _AdGenAOSPowerRolloverOnAC_Type()
)
adGenAOSPowerRolloverOnAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPowerRolloverOnAC.setStatus("current")
_AdGenAOSPwrRollOvrEvntSecSinceEpoch_Type = Unsigned32
_AdGenAOSPwrRollOvrEvntSecSinceEpoch_Object = MibScalar
adGenAOSPwrRollOvrEvntSecSinceEpoch = _AdGenAOSPwrRollOvrEvntSecSinceEpoch_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 1, 2),
    _AdGenAOSPwrRollOvrEvntSecSinceEpoch_Type()
)
adGenAOSPwrRollOvrEvntSecSinceEpoch.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adGenAOSPwrRollOvrEvntSecSinceEpoch.setStatus("current")
_AdGenAOSPowerEpsRps_ObjectIdentity = ObjectIdentity
adGenAOSPowerEpsRps = _AdGenAOSPowerEpsRps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2)
)
_AdGenAOSPowerEpsRpsTable_Object = MibTable
adGenAOSPowerEpsRpsTable = _AdGenAOSPowerEpsRpsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSPowerEpsRpsTable.setStatus("current")
_AdGenAOSPowerEpsRpsEntry_Object = MibTableRow
adGenAOSPowerEpsRpsEntry = _AdGenAOSPowerEpsRpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1)
)
adGenAOSPowerEpsRpsEntry.setIndexNames(
    (0, "ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"),
)
if mibBuilder.loadTexts:
    adGenAOSPowerEpsRpsEntry.setStatus("current")
_AdGenAOSPowerEpsRpsInstanceId_Type = Unsigned32
_AdGenAOSPowerEpsRpsInstanceId_Object = MibTableColumn
adGenAOSPowerEpsRpsInstanceId = _AdGenAOSPowerEpsRpsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 1),
    _AdGenAOSPowerEpsRpsInstanceId_Type()
)
adGenAOSPowerEpsRpsInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPowerEpsRpsInstanceId.setStatus("current")
_AdGenAOSPowerEpsConnectionState_Type = AdPowerConnectionStateTC
_AdGenAOSPowerEpsConnectionState_Object = MibTableColumn
adGenAOSPowerEpsConnectionState = _AdGenAOSPowerEpsConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 2),
    _AdGenAOSPowerEpsConnectionState_Type()
)
adGenAOSPowerEpsConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPowerEpsConnectionState.setStatus("current")
_AdGenAOSPowerEpsDeliveryState_Type = AdEpsPowerDeliveryStateTC
_AdGenAOSPowerEpsDeliveryState_Object = MibTableColumn
adGenAOSPowerEpsDeliveryState = _AdGenAOSPowerEpsDeliveryState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 3),
    _AdGenAOSPowerEpsDeliveryState_Type()
)
adGenAOSPowerEpsDeliveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPowerEpsDeliveryState.setStatus("current")
_AdGenAOSPowerRpsConnectionState_Type = AdPowerConnectionStateTC
_AdGenAOSPowerRpsConnectionState_Object = MibTableColumn
adGenAOSPowerRpsConnectionState = _AdGenAOSPowerRpsConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 4),
    _AdGenAOSPowerRpsConnectionState_Type()
)
adGenAOSPowerRpsConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPowerRpsConnectionState.setStatus("current")
_AdGenAOSPowerRpsDeliveryState_Type = AdRpsPowerDeliveryStateTC
_AdGenAOSPowerRpsDeliveryState_Object = MibTableColumn
adGenAOSPowerRpsDeliveryState = _AdGenAOSPowerRpsDeliveryState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 1, 2, 1, 1, 5),
    _AdGenAOSPowerRpsDeliveryState_Type()
)
adGenAOSPowerRpsDeliveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSPowerRpsDeliveryState.setStatus("current")
_AdGenAOSPowerConformance_ObjectIdentity = ObjectIdentity
adGenAOSPowerConformance = _AdGenAOSPowerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11)
)
_AdGenAOSPowerGroups_ObjectIdentity = ObjectIdentity
adGenAOSPowerGroups = _AdGenAOSPowerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1)
)
_AdGenAOSPowerCompliances_ObjectIdentity = ObjectIdentity
adGenAOSPowerCompliances = _AdGenAOSPowerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2)
)

# Managed Objects groups

adGenAOSPowerRollOverCtlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 2)
)
adGenAOSPowerRollOverCtlGroup.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"))
)
if mibBuilder.loadTexts:
    adGenAOSPowerRollOverCtlGroup.setStatus("current")

adGenAOSEpsRpsConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 5)
)
adGenAOSEpsRpsConfigurationGroup.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
)
if mibBuilder.loadTexts:
    adGenAOSEpsRpsConfigurationGroup.setStatus("current")


# Notification objects

adGenAOSPowerRollover = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 1)
)
adGenAOSPowerRollover.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSPowerRolloverOnAC"),
        ("ADTRAN-AOS-POWER", "adGenAOSPwrRollOvrEvntSecSinceEpoch"))
)
if mibBuilder.loadTexts:
    adGenAOSPowerRollover.setStatus(
        "current"
    )

adGenAOSEpsConnectionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 2)
)
adGenAOSEpsConnectionChange.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsConnectionState"))
)
if mibBuilder.loadTexts:
    adGenAOSEpsConnectionChange.setStatus(
        "current"
    )

adGenAOSEpsDeliveryChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 3)
)
adGenAOSEpsDeliveryChange.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerEpsDeliveryState"))
)
if mibBuilder.loadTexts:
    adGenAOSEpsDeliveryChange.setStatus(
        "current"
    )

adGenAOSRpsConnectionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 4)
)
adGenAOSRpsConnectionChange.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsConnectionState"))
)
if mibBuilder.loadTexts:
    adGenAOSRpsConnectionChange.setStatus(
        "current"
    )

adGenAOSRpsDeliveryChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 7, 0, 5)
)
adGenAOSRpsDeliveryChange.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSPowerEpsRpsInstanceId"),
        ("ADTRAN-AOS-POWER", "adGenAOSPowerRpsDeliveryState"))
)
if mibBuilder.loadTexts:
    adGenAOSRpsDeliveryChange.setStatus(
        "current"
    )


# Notifications groups

adGenAOSPowerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 1)
)
adGenAOSPowerNotificationGroup.setObjects(
    ("ADTRAN-AOS-POWER", "adGenAOSPowerRollover")
)
if mibBuilder.loadTexts:
    adGenAOSPowerNotificationGroup.setStatus(
        "current"
    )

adGenAOSEpsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 3)
)
adGenAOSEpsNotificationGroup.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSEpsConnectionChange"),
        ("ADTRAN-AOS-POWER", "adGenAOSEpsDeliveryChange"))
)
if mibBuilder.loadTexts:
    adGenAOSEpsNotificationGroup.setStatus(
        "current"
    )

adGenAOSRpsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 1, 4)
)
adGenAOSRpsNotificationGroup.setObjects(
      *(("ADTRAN-AOS-POWER", "adGenAOSRpsConnectionChange"),
        ("ADTRAN-AOS-POWER", "adGenAOSRpsDeliveryChange"))
)
if mibBuilder.loadTexts:
    adGenAOSRpsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adGenAOSPowerFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 11, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSPowerFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-POWER",
    **{"AdEpsPowerDeliveryStateTC": AdEpsPowerDeliveryStateTC,
       "AdRpsPowerDeliveryStateTC": AdRpsPowerDeliveryStateTC,
       "AdPowerConnectionStateTC": AdPowerConnectionStateTC,
       "adGenAOSPowerTraps": adGenAOSPowerTraps,
       "adGenAOSPowerRollover": adGenAOSPowerRollover,
       "adGenAOSEpsConnectionChange": adGenAOSEpsConnectionChange,
       "adGenAOSEpsDeliveryChange": adGenAOSEpsDeliveryChange,
       "adGenAOSRpsConnectionChange": adGenAOSRpsConnectionChange,
       "adGenAOSRpsDeliveryChange": adGenAOSRpsDeliveryChange,
       "adGenAOSPowerMonitor": adGenAOSPowerMonitor,
       "adGenAOSPowerRollOverCtl": adGenAOSPowerRollOverCtl,
       "adGenAOSPowerRolloverOnAC": adGenAOSPowerRolloverOnAC,
       "adGenAOSPwrRollOvrEvntSecSinceEpoch": adGenAOSPwrRollOvrEvntSecSinceEpoch,
       "adGenAOSPowerEpsRps": adGenAOSPowerEpsRps,
       "adGenAOSPowerEpsRpsTable": adGenAOSPowerEpsRpsTable,
       "adGenAOSPowerEpsRpsEntry": adGenAOSPowerEpsRpsEntry,
       "adGenAOSPowerEpsRpsInstanceId": adGenAOSPowerEpsRpsInstanceId,
       "adGenAOSPowerEpsConnectionState": adGenAOSPowerEpsConnectionState,
       "adGenAOSPowerEpsDeliveryState": adGenAOSPowerEpsDeliveryState,
       "adGenAOSPowerRpsConnectionState": adGenAOSPowerRpsConnectionState,
       "adGenAOSPowerRpsDeliveryState": adGenAOSPowerRpsDeliveryState,
       "adGenAOSPowerConformance": adGenAOSPowerConformance,
       "adGenAOSPowerGroups": adGenAOSPowerGroups,
       "adGenAOSPowerNotificationGroup": adGenAOSPowerNotificationGroup,
       "adGenAOSPowerRollOverCtlGroup": adGenAOSPowerRollOverCtlGroup,
       "adGenAOSEpsNotificationGroup": adGenAOSEpsNotificationGroup,
       "adGenAOSRpsNotificationGroup": adGenAOSRpsNotificationGroup,
       "adGenAOSEpsRpsConfigurationGroup": adGenAOSEpsRpsConfigurationGroup,
       "adGenAOSPowerCompliances": adGenAOSPowerCompliances,
       "adGenAOSPowerFullCompliance": adGenAOSPowerFullCompliance}
)
