# SNMP MIB module (APTIS-V2TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-V2TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:10 2024
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

(policyConfigChassisModemThresholdWarning,
 policyConfigSlotModemThresholdWarning) = mibBuilder.importSymbols(
    "APTIS-CONFIG-MIB",
    "policyConfigChassisModemThresholdWarning",
    "policyConfigSlotModemThresholdWarning")

(Boolean,
 aptis_traps) = mibBuilder.importSymbols(
    "APTIS-MIB",
    "Boolean",
    "aptis-traps")

(aptis_modules,) = mibBuilder.importSymbols(
    "APTIS-REG-MIB",
    "aptis-modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(egpNeighAddr,) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "egpNeighAddr")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

aptisTrapsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 1, 1, 7)
)
aptisTrapsModule.setRevisions(
        ("1900-04-25 00:00",
         "1900-03-20 00:00",
         "1900-03-17 00:00",
         "1900-03-07 00:00",
         "1900-02-09 00:00",
         "1900-01-27 12:00",
         "1900-01-27 00:00",
         "1900-01-20 00:00",
         "1900-01-14 00:00",
         "1900-01-10 00:00",
         "1999-12-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AptisProtraps_ObjectIdentity = ObjectIdentity
aptisProtraps = _AptisProtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1)
)
if mibBuilder.loadTexts:
    aptisProtraps.setStatus("current")
_AptisProtrapsV2_ObjectIdentity = ObjectIdentity
aptisProtrapsV2 = _AptisProtrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0)
)
if mibBuilder.loadTexts:
    aptisProtrapsV2.setStatus("current")


class _TrapGenNum_Type(Integer32):
    """Custom type trapGenNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TrapGenNum_Type.__name__ = "Integer32"
_TrapGenNum_Object = MibScalar
trapGenNum = _TrapGenNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 2),
    _TrapGenNum_Type()
)
trapGenNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapGenNum.setStatus("current")
_TrapPath_Type = OctetString
_TrapPath_Object = MibScalar
trapPath = _TrapPath_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 3),
    _TrapPath_Type()
)
trapPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapPath.setStatus("current")


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 4),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_TrapString_Type = OctetString
_TrapString_Object = MibScalar
trapString = _TrapString_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 5),
    _TrapString_Type()
)
trapString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapString.setStatus("current")
_TrapIpAddr_Type = IpAddress
_TrapIpAddr_Object = MibScalar
trapIpAddr = _TrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 6),
    _TrapIpAddr_Type()
)
trapIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIpAddr.setStatus("current")
_TrapSlotNum_Type = Integer32
_TrapSlotNum_Object = MibScalar
trapSlotNum = _TrapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 7),
    _TrapSlotNum_Type()
)
trapSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSlotNum.setStatus("current")
_TrapPortNum_Type = Integer32
_TrapPortNum_Object = MibScalar
trapPortNum = _TrapPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 8),
    _TrapPortNum_Type()
)
trapPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapPortNum.setStatus("current")


class _TrapTunnelType_Type(Integer32):
    """Custom type trapTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l2f", 3),
          ("l2tp", 4),
          ("none", 1),
          ("other", 2),
          ("unknown", 0))
    )


_TrapTunnelType_Type.__name__ = "Integer32"
_TrapTunnelType_Object = MibScalar
trapTunnelType = _TrapTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 9),
    _TrapTunnelType_Type()
)
trapTunnelType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapTunnelType.setStatus("current")
_TrapUserName_Type = OctetString
_TrapUserName_Object = MibScalar
trapUserName = _TrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 10),
    _TrapUserName_Type()
)
trapUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapUserName.setStatus("current")
_TrapAuthThreshold_Type = Integer32
_TrapAuthThreshold_Object = MibScalar
trapAuthThreshold = _TrapAuthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 11),
    _TrapAuthThreshold_Type()
)
trapAuthThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAuthThreshold.setStatus("current")
_TrapFilterName_Type = OctetString
_TrapFilterName_Object = MibScalar
trapFilterName = _TrapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 12),
    _TrapFilterName_Type()
)
trapFilterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapFilterName.setStatus("current")
_TrapTempCurrent_Type = Integer32
_TrapTempCurrent_Object = MibScalar
trapTempCurrent = _TrapTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 13),
    _TrapTempCurrent_Type()
)
trapTempCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapTempCurrent.setStatus("current")
if mibBuilder.loadTexts:
    trapTempCurrent.setUnits("Degrees Celsius")
_TrapTempConfigWarningLevel_Type = Integer32
_TrapTempConfigWarningLevel_Object = MibScalar
trapTempConfigWarningLevel = _TrapTempConfigWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 14),
    _TrapTempConfigWarningLevel_Type()
)
trapTempConfigWarningLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapTempConfigWarningLevel.setStatus("current")
if mibBuilder.loadTexts:
    trapTempConfigWarningLevel.setUnits("Degrees Celsius")
_TrapSessionId_Type = Integer32
_TrapSessionId_Object = MibScalar
trapSessionId = _TrapSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 15),
    _TrapSessionId_Type()
)
trapSessionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSessionId.setStatus("current")
_TrapVpopId_Type = Integer32
_TrapVpopId_Object = MibScalar
trapVpopId = _TrapVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 16),
    _TrapVpopId_Type()
)
trapVpopId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVpopId.setStatus("current")
_TrapModemCount_Type = Integer32
_TrapModemCount_Object = MibScalar
trapModemCount = _TrapModemCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 17),
    _TrapModemCount_Type()
)
trapModemCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapModemCount.setStatus("current")

# Managed Objects groups


# Notification objects

aptis_fandown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 1)
)
aptis_fandown.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_fandown.setStatus(
        "current"
    )

aptis_dc1down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 2)
)
aptis_dc1down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_dc1down.setStatus(
        "current"
    )

aptis_dc2down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 3)
)
aptis_dc2down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_dc2down.setStatus(
        "current"
    )

aptis_ac1down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 4)
)
aptis_ac1down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ac1down.setStatus(
        "obsolete"
    )

aptis_ac2down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 5)
)
aptis_ac2down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ac2down.setStatus(
        "obsolete"
    )

aptis_acdc1down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 6)
)
aptis_acdc1down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_acdc1down.setStatus(
        "current"
    )

aptis_acdc2down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 7)
)
aptis_acdc2down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_acdc2down.setStatus(
        "current"
    )

aptis_acdc3down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 8)
)
aptis_acdc3down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_acdc3down.setStatus(
        "current"
    )

aptis_flashmount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 9)
)
aptis_flashmount.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_flashmount.setStatus(
        "current"
    )

aptis_flashdismount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 10)
)
aptis_flashdismount.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_flashdismount.setStatus(
        "current"
    )

aptis_coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 11)
)
aptis_coldStart.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_coldStart.setStatus(
        "current"
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 12)
)
warmStart.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        "current"
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 13)
)
linkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        "obsolete"
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 14)
)
linkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        "obsolete"
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 15)
)
authenticationFailure.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        "obsolete"
    )

aptis_radius_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 16)
)
aptis_radius_fail.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_radius_fail.setStatus(
        "current"
    )

aptis_slot_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 17)
)
aptis_slot_up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_slot_up.setStatus(
        "current"
    )

aptis_slot_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 18)
)
aptis_slot_down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_slot_down.setStatus(
        "current"
    )

aptis_slot_cfg_chng = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 19)
)
aptis_slot_cfg_chng.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_slot_cfg_chng.setStatus(
        "current"
    )

aptis_ds1_red_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 20)
)
aptis_ds1_red_alarm.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds1_red_alarm.setStatus(
        "current"
    )

aptis_ds1_yellow_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 21)
)
aptis_ds1_yellow_alarm.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds1_yellow_alarm.setStatus(
        "current"
    )

aptis_ds1_alarm_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 22)
)
aptis_ds1_alarm_clear.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds1_alarm_clear.setStatus(
        "current"
    )

aptis_ds3_red_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 23)
)
aptis_ds3_red_alarm.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds3_red_alarm.setStatus(
        "current"
    )

aptis_ds3_yellow_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 24)
)
aptis_ds3_yellow_alarm.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds3_yellow_alarm.setStatus(
        "current"
    )

aptis_ds3_alarm_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 25)
)
aptis_ds3_alarm_clear.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds3_alarm_clear.setStatus(
        "current"
    )

aptis_isdn_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 26)
)
aptis_isdn_link_up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_isdn_link_up.setStatus(
        "current"
    )

aptis_isdn_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 27)
)
aptis_isdn_link_down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_isdn_link_down.setStatus(
        "current"
    )

aptis_isdn_link_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 28)
)
aptis_isdn_link_reset.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_isdn_link_reset.setStatus(
        "current"
    )

aptis_temp_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 29)
)
aptis_temp_exceeded.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_temp_exceeded.setStatus(
        "current"
    )

aptis_cvx_ss7_gateway_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 30)
)
aptis_cvx_ss7_gateway_failover.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_cvx_ss7_gateway_failover.setStatus(
        "current"
    )

aptis_l2f_tunnel_start = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 31)
)
aptis_l2f_tunnel_start.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    aptis_l2f_tunnel_start.setStatus(
        "obsolete"
    )

aptis_l2f_tunnel_stop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 32)
)
aptis_l2f_tunnel_stop.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    aptis_l2f_tunnel_stop.setStatus(
        "obsolete"
    )

aptis_l2f_tunnel_reject = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 33)
)
aptis_l2f_tunnel_reject.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    aptis_l2f_tunnel_reject.setStatus(
        "obsolete"
    )

cvx_MAC_modems_below_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 34)
)
cvx_MAC_modems_below_threshold.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"),
        ("APTIS-CONFIG-MIB", "policyConfigSlotModemThresholdWarning"),
        ("APTIS-V2TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_MAC_modems_below_threshold.setStatus(
        "current"
    )

cvx_MAC_modems_above_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 35)
)
cvx_MAC_modems_above_threshold.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"),
        ("APTIS-CONFIG-MIB", "policyConfigSlotModemThresholdWarning"),
        ("APTIS-V2TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_MAC_modems_above_threshold.setStatus(
        "current"
    )

cvx_total_modems_below_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 36)
)
cvx_total_modems_below_threshold.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-CONFIG-MIB", "policyConfigChassisModemThresholdWarning"),
        ("APTIS-V2TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_total_modems_below_threshold.setStatus(
        "current"
    )

cvx_total_modems_above_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 37)
)
cvx_total_modems_above_threshold.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-CONFIG-MIB", "policyConfigChassisModemThresholdWarning"),
        ("APTIS-V2TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_total_modems_above_threshold.setStatus(
        "current"
    )

cvx_local_pswd_change = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 38)
)
cvx_local_pswd_change.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapUserName"))
)
if mibBuilder.loadTexts:
    cvx_local_pswd_change.setStatus(
        "current"
    )

cvx_auth_server_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 39)
)
cvx_auth_server_failover.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_auth_server_failover.setStatus(
        "current"
    )

cvx_acct_server_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 40)
)
cvx_acct_server_failure.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_acct_server_failure.setStatus(
        "current"
    )

cvx_acct_server_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 41)
)
cvx_acct_server_failover.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_acct_server_failover.setStatus(
        "current"
    )

cvx_ss7_gateway_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 42)
)
cvx_ss7_gateway_down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_ss7_gateway_down.setStatus(
        "current"
    )

cvx_ss7_gateway_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 43)
)
cvx_ss7_gateway_up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_ss7_gateway_up.setStatus(
        "current"
    )

cvx_Ds3_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 44)
)
cvx_Ds3_failover.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvx_Ds3_failover.setStatus(
        "current"
    )

cvx_Scc_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 45)
)
cvx_Scc_failover.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvx_Scc_failover.setStatus(
        "current"
    )

cvx_ethernet_port_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 46)
)
cvx_ethernet_port_up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_ethernet_port_up.setStatus(
        "current"
    )

cvx_ethernet_port_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 47)
)
cvx_ethernet_port_down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_ethernet_port_down.setStatus(
        "current"
    )

cvx_Hssi_port_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 48)
)
cvx_Hssi_port_up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_Hssi_port_up.setStatus(
        "current"
    )

cvx_Hssi_port_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 49)
)
cvx_Hssi_port_down.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_Hssi_port_down.setStatus(
        "current"
    )

cvx_local_auth_failure_threshold_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 50)
)
cvx_local_auth_failure_threshold_exceeded.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapAuthThreshold"),
        ("APTIS-V2TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    cvx_local_auth_failure_threshold_exceeded.setStatus(
        "current"
    )

cvx_preAuth_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 51)
)
cvx_preAuth_fail.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_preAuth_fail.setStatus(
        "current"
    )

cvx_auth_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 52)
)
cvx_auth_fail.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_auth_fail.setStatus(
        "current"
    )

cvx_tunnel_start = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 53)
)
cvx_tunnel_start.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapTunnelType"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_tunnel_start.setStatus(
        "current"
    )

cvx_tunnel_stop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 54)
)
cvx_tunnel_stop.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapTunnelType"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_tunnel_stop.setStatus(
        "current"
    )

cvx_tunnel_reject = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 55)
)
cvx_tunnel_reject.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapTunnelType"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_tunnel_reject.setStatus(
        "current"
    )

cvx_radius_packet_discard = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 56)
)
cvx_radius_packet_discard.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    cvx_radius_packet_discard.setStatus(
        "current"
    )

cvx_fanup = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 57)
)
cvx_fanup.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_fanup.setStatus(
        "current"
    )

cvx_dc1up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 58)
)
cvx_dc1up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_dc1up.setStatus(
        "current"
    )

cvx_dc2up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 59)
)
cvx_dc2up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_dc2up.setStatus(
        "current"
    )

cvx_acdc1up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 62)
)
cvx_acdc1up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_acdc1up.setStatus(
        "current"
    )

cvx_acdc2up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 63)
)
cvx_acdc2up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_acdc2up.setStatus(
        "current"
    )

cvx_acdc3up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 64)
)
cvx_acdc3up.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_acdc3up.setStatus(
        "current"
    )

cvx_filter_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 65)
)
cvx_filter_error.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapFilterName"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_filter_error.setStatus(
        "current"
    )

cvx_slave_flash_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 66)
)
cvx_slave_flash_missing.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_slave_flash_missing.setStatus(
        "current"
    )

cvxSlaveSccFlashDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 67)
)
cvxSlaveSccFlashDetected.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFlashDetected.setStatus(
        "current"
    )

cvxAuthServerRevived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 68)
)
cvxAuthServerRevived.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxAuthServerRevived.setStatus(
        "current"
    )

cvxPrimaryDhcpServerContactFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 69)
)
cvxPrimaryDhcpServerContactFailed.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxPrimaryDhcpServerContactFailed.setStatus(
        "current"
    )

cvxPrimaryDhcpServerContactRevived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 70)
)
cvxPrimaryDhcpServerContactRevived.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxPrimaryDhcpServerContactRevived.setStatus(
        "current"
    )

cvxSecondaryDhcpServerContactFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 71)
)
cvxSecondaryDhcpServerContactFailed.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxSecondaryDhcpServerContactFailed.setStatus(
        "current"
    )

cvxSlotTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 73)
)
cvxSlotTempWarning.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"),
        ("APTIS-V2TRAPS-MIB", "trapTempCurrent"),
        ("APTIS-V2TRAPS-MIB", "trapTempConfigWarningLevel"))
)
if mibBuilder.loadTexts:
    cvxSlotTempWarning.setStatus(
        "current"
    )

cvxSlotTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 74)
)
cvxSlotTempNormal.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"),
        ("APTIS-V2TRAPS-MIB", "trapTempCurrent"),
        ("APTIS-V2TRAPS-MIB", "trapTempConfigWarningLevel"))
)
if mibBuilder.loadTexts:
    cvxSlotTempNormal.setStatus(
        "current"
    )

cvxSlaveSccRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 75)
)
cvxSlaveSccRemoved.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccRemoved.setStatus(
        "current"
    )

cvxSlaveSccInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 76)
)
cvxSlaveSccInserted.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccInserted.setStatus(
        "current"
    )

cvxFailedSlaveSccRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 77)
)
cvxFailedSlaveSccRemoved.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxFailedSlaveSccRemoved.setStatus(
        "current"
    )

cvxCardCrashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 79)
)
cvxCardCrashed.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvxCardCrashed.setStatus(
        "current"
    )

cvxCardNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 80)
)
cvxCardNotResponding.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvxCardNotResponding.setStatus(
        "current"
    )

cvxLocalAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 81)
)
cvxLocalAuthenticationFailure.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapUserName"))
)
if mibBuilder.loadTexts:
    cvxLocalAuthenticationFailure.setStatus(
        "current"
    )

cvxSessionAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 82)
)
cvxSessionAuthenticationFailure.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapSessionId"),
        ("APTIS-V2TRAPS-MIB", "trapVpopId"))
)
if mibBuilder.loadTexts:
    cvxSessionAuthenticationFailure.setStatus(
        "current"
    )

encryptionNotAllowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 83)
)
encryptionNotAllowed.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    encryptionNotAllowed.setStatus(
        "current"
    )

cvxRadiusdSessionDisc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 84)
)
cvxRadiusdSessionDisc.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxRadiusdSessionDisc.setStatus(
        "current"
    )

cvxRadiusdUnknownClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 85)
)
cvxRadiusdUnknownClient.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxRadiusdUnknownClient.setStatus(
        "current"
    )

cvxRadiusdClientAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 86)
)
cvxRadiusdClientAuthFailed.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"),
        ("APTIS-V2TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxRadiusdClientAuthFailed.setStatus(
        "current"
    )

cvxSlaveSccFileSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 87)
)
cvxSlaveSccFileSyncFailed.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFileSyncFailed.setStatus(
        "current"
    )

cvxSlaveSccFileSyncCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 88)
)
cvxSlaveSccFileSyncCompleted.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFileSyncCompleted.setStatus(
        "current"
    )

cvxSlaveSccFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 89)
)
cvxSlaveSccFailed.setObjects(
      *(("APTIS-V2TRAPS-MIB", "trapGenNum"),
        ("APTIS-V2TRAPS-MIB", "trapPath"),
        ("APTIS-V2TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-V2TRAPS-MIB",
    **{"aptisTrapsModule": aptisTrapsModule,
       "aptisProtraps": aptisProtraps,
       "aptisProtrapsV2": aptisProtrapsV2,
       "aptis-fandown": aptis_fandown,
       "aptis-dc1down": aptis_dc1down,
       "aptis-dc2down": aptis_dc2down,
       "aptis-ac1down": aptis_ac1down,
       "aptis-ac2down": aptis_ac2down,
       "aptis-acdc1down": aptis_acdc1down,
       "aptis-acdc2down": aptis_acdc2down,
       "aptis-acdc3down": aptis_acdc3down,
       "aptis-flashmount": aptis_flashmount,
       "aptis-flashdismount": aptis_flashdismount,
       "aptis-coldStart": aptis_coldStart,
       "warmStart": warmStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "authenticationFailure": authenticationFailure,
       "aptis-radius-fail": aptis_radius_fail,
       "aptis-slot-up": aptis_slot_up,
       "aptis-slot-down": aptis_slot_down,
       "aptis-slot-cfg-chng": aptis_slot_cfg_chng,
       "aptis-ds1-red-alarm": aptis_ds1_red_alarm,
       "aptis-ds1-yellow-alarm": aptis_ds1_yellow_alarm,
       "aptis-ds1-alarm-clear": aptis_ds1_alarm_clear,
       "aptis-ds3-red-alarm": aptis_ds3_red_alarm,
       "aptis-ds3-yellow-alarm": aptis_ds3_yellow_alarm,
       "aptis-ds3-alarm-clear": aptis_ds3_alarm_clear,
       "aptis-isdn-link-up": aptis_isdn_link_up,
       "aptis-isdn-link-down": aptis_isdn_link_down,
       "aptis-isdn-link-reset": aptis_isdn_link_reset,
       "aptis-temp-exceeded": aptis_temp_exceeded,
       "aptis-cvx-ss7-gateway-failover": aptis_cvx_ss7_gateway_failover,
       "aptis-l2f-tunnel-start": aptis_l2f_tunnel_start,
       "aptis-l2f-tunnel-stop": aptis_l2f_tunnel_stop,
       "aptis-l2f-tunnel-reject": aptis_l2f_tunnel_reject,
       "cvx-MAC-modems-below-threshold": cvx_MAC_modems_below_threshold,
       "cvx-MAC-modems-above-threshold": cvx_MAC_modems_above_threshold,
       "cvx-total-modems-below-threshold": cvx_total_modems_below_threshold,
       "cvx-total-modems-above-threshold": cvx_total_modems_above_threshold,
       "cvx-local-pswd-change": cvx_local_pswd_change,
       "cvx-auth-server-failover": cvx_auth_server_failover,
       "cvx-acct-server-failure": cvx_acct_server_failure,
       "cvx-acct-server-failover": cvx_acct_server_failover,
       "cvx-ss7-gateway-down": cvx_ss7_gateway_down,
       "cvx-ss7-gateway-up": cvx_ss7_gateway_up,
       "cvx-Ds3-failover": cvx_Ds3_failover,
       "cvx-Scc-failover": cvx_Scc_failover,
       "cvx-ethernet-port-up": cvx_ethernet_port_up,
       "cvx-ethernet-port-down": cvx_ethernet_port_down,
       "cvx-Hssi-port-up": cvx_Hssi_port_up,
       "cvx-Hssi-port-down": cvx_Hssi_port_down,
       "cvx-local-auth-failure-threshold-exceeded": cvx_local_auth_failure_threshold_exceeded,
       "cvx-preAuth-fail": cvx_preAuth_fail,
       "cvx-auth-fail": cvx_auth_fail,
       "cvx-tunnel-start": cvx_tunnel_start,
       "cvx-tunnel-stop": cvx_tunnel_stop,
       "cvx-tunnel-reject": cvx_tunnel_reject,
       "cvx-radius-packet-discard": cvx_radius_packet_discard,
       "cvx-fanup": cvx_fanup,
       "cvx-dc1up": cvx_dc1up,
       "cvx-dc2up": cvx_dc2up,
       "cvx-acdc1up": cvx_acdc1up,
       "cvx-acdc2up": cvx_acdc2up,
       "cvx-acdc3up": cvx_acdc3up,
       "cvx-filter-error": cvx_filter_error,
       "cvx-slave-flash-missing": cvx_slave_flash_missing,
       "cvxSlaveSccFlashDetected": cvxSlaveSccFlashDetected,
       "cvxAuthServerRevived": cvxAuthServerRevived,
       "cvxPrimaryDhcpServerContactFailed": cvxPrimaryDhcpServerContactFailed,
       "cvxPrimaryDhcpServerContactRevived": cvxPrimaryDhcpServerContactRevived,
       "cvxSecondaryDhcpServerContactFailed": cvxSecondaryDhcpServerContactFailed,
       "cvxSlotTempWarning": cvxSlotTempWarning,
       "cvxSlotTempNormal": cvxSlotTempNormal,
       "cvxSlaveSccRemoved": cvxSlaveSccRemoved,
       "cvxSlaveSccInserted": cvxSlaveSccInserted,
       "cvxFailedSlaveSccRemoved": cvxFailedSlaveSccRemoved,
       "cvxCardCrashed": cvxCardCrashed,
       "cvxCardNotResponding": cvxCardNotResponding,
       "cvxLocalAuthenticationFailure": cvxLocalAuthenticationFailure,
       "cvxSessionAuthenticationFailure": cvxSessionAuthenticationFailure,
       "encryptionNotAllowed": encryptionNotAllowed,
       "cvxRadiusdSessionDisc": cvxRadiusdSessionDisc,
       "cvxRadiusdUnknownClient": cvxRadiusdUnknownClient,
       "cvxRadiusdClientAuthFailed": cvxRadiusdClientAuthFailed,
       "cvxSlaveSccFileSyncFailed": cvxSlaveSccFileSyncFailed,
       "cvxSlaveSccFileSyncCompleted": cvxSlaveSccFileSyncCompleted,
       "cvxSlaveSccFailed": cvxSlaveSccFailed,
       "trapGenNum": trapGenNum,
       "trapPath": trapPath,
       "trapSeverity": trapSeverity,
       "trapString": trapString,
       "trapIpAddr": trapIpAddr,
       "trapSlotNum": trapSlotNum,
       "trapPortNum": trapPortNum,
       "trapTunnelType": trapTunnelType,
       "trapUserName": trapUserName,
       "trapAuthThreshold": trapAuthThreshold,
       "trapFilterName": trapFilterName,
       "trapTempCurrent": trapTempCurrent,
       "trapTempConfigWarningLevel": trapTempConfigWarningLevel,
       "trapSessionId": trapSessionId,
       "trapVpopId": trapVpopId,
       "trapModemCount": trapModemCount}
)
