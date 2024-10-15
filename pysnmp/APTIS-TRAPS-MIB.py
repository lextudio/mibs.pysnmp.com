# SNMP MIB module (APTIS-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:09 2024
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

(aptis_traps,) = mibBuilder.importSymbols(
    "APTIS-MIB",
    "aptis-traps")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AptisProtraps_ObjectIdentity = ObjectIdentity
aptisProtraps = _AptisProtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1)
)


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
trapGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapGenNum.setStatus("mandatory")
_TrapPath_Type = OctetString
_TrapPath_Object = MibScalar
trapPath = _TrapPath_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 3),
    _TrapPath_Type()
)
trapPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPath.setStatus("mandatory")


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
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")
_TrapString_Type = OctetString
_TrapString_Object = MibScalar
trapString = _TrapString_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 5),
    _TrapString_Type()
)
trapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapString.setStatus("mandatory")
_TrapIpAddr_Type = IpAddress
_TrapIpAddr_Object = MibScalar
trapIpAddr = _TrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 6),
    _TrapIpAddr_Type()
)
trapIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIpAddr.setStatus("mandatory")
_TrapSlotNum_Type = Integer32
_TrapSlotNum_Object = MibScalar
trapSlotNum = _TrapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 7),
    _TrapSlotNum_Type()
)
trapSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSlotNum.setStatus("mandatory")
_TrapPortNum_Type = Integer32
_TrapPortNum_Object = MibScalar
trapPortNum = _TrapPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 8),
    _TrapPortNum_Type()
)
trapPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPortNum.setStatus("mandatory")


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
trapTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTunnelType.setStatus("mandatory")
_TrapUserName_Type = OctetString
_TrapUserName_Object = MibScalar
trapUserName = _TrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 10),
    _TrapUserName_Type()
)
trapUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapUserName.setStatus("mandatory")
_TrapAuthThreshold_Type = Integer32
_TrapAuthThreshold_Object = MibScalar
trapAuthThreshold = _TrapAuthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 11),
    _TrapAuthThreshold_Type()
)
trapAuthThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAuthThreshold.setStatus("mandatory")
_TrapFilterName_Type = OctetString
_TrapFilterName_Object = MibScalar
trapFilterName = _TrapFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 12),
    _TrapFilterName_Type()
)
trapFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFilterName.setStatus("mandatory")
_TrapTempCurrent_Type = Integer32
_TrapTempCurrent_Object = MibScalar
trapTempCurrent = _TrapTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 13),
    _TrapTempCurrent_Type()
)
trapTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTempCurrent.setStatus("mandatory")
_TrapTempConfigWarningLevel_Type = Integer32
_TrapTempConfigWarningLevel_Object = MibScalar
trapTempConfigWarningLevel = _TrapTempConfigWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 14),
    _TrapTempConfigWarningLevel_Type()
)
trapTempConfigWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTempConfigWarningLevel.setStatus("mandatory")
_TrapSessionId_Type = Integer32
_TrapSessionId_Object = MibScalar
trapSessionId = _TrapSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 15),
    _TrapSessionId_Type()
)
trapSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSessionId.setStatus("mandatory")
_TrapVpopId_Type = Integer32
_TrapVpopId_Object = MibScalar
trapVpopId = _TrapVpopId_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 16),
    _TrapVpopId_Type()
)
trapVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapVpopId.setStatus("mandatory")
_TrapModemCount_Type = Integer32
_TrapModemCount_Object = MibScalar
trapModemCount = _TrapModemCount_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 17),
    _TrapModemCount_Type()
)
trapModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapModemCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

aptis_fandown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 1)
)
aptis_fandown.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_fandown.setStatus(
        ""
    )

aptis_dc1down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 2)
)
aptis_dc1down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_dc1down.setStatus(
        ""
    )

aptis_dc2down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 3)
)
aptis_dc2down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_dc2down.setStatus(
        ""
    )

aptis_ac1down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 4)
)
aptis_ac1down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ac1down.setStatus(
        ""
    )

aptis_ac2down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 5)
)
aptis_ac2down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ac2down.setStatus(
        ""
    )

aptis_acdc1down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 6)
)
aptis_acdc1down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_acdc1down.setStatus(
        ""
    )

aptis_acdc2down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 7)
)
aptis_acdc2down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_acdc2down.setStatus(
        ""
    )

aptis_acdc3down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 8)
)
aptis_acdc3down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_acdc3down.setStatus(
        ""
    )

aptis_flashmount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 9)
)
aptis_flashmount.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_flashmount.setStatus(
        ""
    )

aptis_flashdismount = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 10)
)
aptis_flashdismount.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_flashdismount.setStatus(
        ""
    )

aptis_coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 11)
)
aptis_coldStart.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_coldStart.setStatus(
        ""
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 12)
)
warmStart.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 13)
)
linkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 14)
)
linkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 15)
)
authenticationFailure.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

aptis_radius_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 16)
)
aptis_radius_fail.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_radius_fail.setStatus(
        ""
    )

aptis_slot_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 17)
)
aptis_slot_up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_slot_up.setStatus(
        ""
    )

aptis_slot_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 18)
)
aptis_slot_down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_slot_down.setStatus(
        ""
    )

aptis_slot_cfg_chng = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 19)
)
aptis_slot_cfg_chng.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_slot_cfg_chng.setStatus(
        ""
    )

aptis_ds1_red_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 20)
)
aptis_ds1_red_alarm.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds1_red_alarm.setStatus(
        ""
    )

aptis_ds1_yellow_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 21)
)
aptis_ds1_yellow_alarm.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds1_yellow_alarm.setStatus(
        ""
    )

aptis_ds1_alarm_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 22)
)
aptis_ds1_alarm_clear.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds1_alarm_clear.setStatus(
        ""
    )

aptis_ds3_red_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 23)
)
aptis_ds3_red_alarm.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds3_red_alarm.setStatus(
        ""
    )

aptis_ds3_yellow_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 24)
)
aptis_ds3_yellow_alarm.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds3_yellow_alarm.setStatus(
        ""
    )

aptis_ds3_alarm_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 25)
)
aptis_ds3_alarm_clear.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_ds3_alarm_clear.setStatus(
        ""
    )

aptis_isdn_link_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 26)
)
aptis_isdn_link_up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_isdn_link_up.setStatus(
        ""
    )

aptis_isdn_link_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 27)
)
aptis_isdn_link_down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_isdn_link_down.setStatus(
        ""
    )

aptis_isdn_link_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 28)
)
aptis_isdn_link_reset.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_isdn_link_reset.setStatus(
        ""
    )

aptis_temp_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 29)
)
aptis_temp_exceeded.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_temp_exceeded.setStatus(
        ""
    )

aptis_cvx_ss7_gateway_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 30)
)
aptis_cvx_ss7_gateway_failover.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    aptis_cvx_ss7_gateway_failover.setStatus(
        ""
    )

aptis_l2f_tunnel_start = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 31)
)
aptis_l2f_tunnel_start.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    aptis_l2f_tunnel_start.setStatus(
        ""
    )

aptis_l2f_tunnel_stop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 32)
)
aptis_l2f_tunnel_stop.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    aptis_l2f_tunnel_stop.setStatus(
        ""
    )

aptis_l2f_tunnel_reject = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 33)
)
aptis_l2f_tunnel_reject.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    aptis_l2f_tunnel_reject.setStatus(
        ""
    )

cvx_MAC_modems_below_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 34)
)
cvx_MAC_modems_below_threshold.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"),
        ("APTIS-CONFIG-MIB", "policyConfigSlotModemThresholdWarning"),
        ("APTIS-TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_MAC_modems_below_threshold.setStatus(
        ""
    )

cvx_MAC_modems_above_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 35)
)
cvx_MAC_modems_above_threshold.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"),
        ("APTIS-CONFIG-MIB", "policyConfigSlotModemThresholdWarning"),
        ("APTIS-TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_MAC_modems_above_threshold.setStatus(
        ""
    )

cvx_total_modems_below_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 36)
)
cvx_total_modems_below_threshold.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-CONFIG-MIB", "policyConfigChassisModemThresholdWarning"),
        ("APTIS-TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_total_modems_below_threshold.setStatus(
        ""
    )

cvx_total_modems_above_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 37)
)
cvx_total_modems_above_threshold.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-CONFIG-MIB", "policyConfigChassisModemThresholdWarning"),
        ("APTIS-TRAPS-MIB", "trapModemCount"))
)
if mibBuilder.loadTexts:
    cvx_total_modems_above_threshold.setStatus(
        ""
    )

cvx_local_pswd_change = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 38)
)
cvx_local_pswd_change.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapUserName"))
)
if mibBuilder.loadTexts:
    cvx_local_pswd_change.setStatus(
        ""
    )

cvx_auth_server_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 39)
)
cvx_auth_server_failover.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_auth_server_failover.setStatus(
        ""
    )

cvx_acct_server_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 40)
)
cvx_acct_server_failure.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_acct_server_failure.setStatus(
        ""
    )

cvx_acct_server_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 41)
)
cvx_acct_server_failover.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_acct_server_failover.setStatus(
        ""
    )

cvx_ss7_gateway_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 42)
)
cvx_ss7_gateway_down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_ss7_gateway_down.setStatus(
        ""
    )

cvx_ss7_gateway_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 43)
)
cvx_ss7_gateway_up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_ss7_gateway_up.setStatus(
        ""
    )

cvx_Ds3_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 44)
)
cvx_Ds3_failover.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvx_Ds3_failover.setStatus(
        ""
    )

cvx_Scc_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 45)
)
cvx_Scc_failover.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvx_Scc_failover.setStatus(
        ""
    )

cvx_ethernet_port_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 46)
)
cvx_ethernet_port_up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_ethernet_port_up.setStatus(
        ""
    )

cvx_ethernet_port_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 47)
)
cvx_ethernet_port_down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_ethernet_port_down.setStatus(
        ""
    )

cvx_Hssi_port_up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 48)
)
cvx_Hssi_port_up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_Hssi_port_up.setStatus(
        ""
    )

cvx_Hssi_port_down = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 49)
)
cvx_Hssi_port_down.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapPortNum"))
)
if mibBuilder.loadTexts:
    cvx_Hssi_port_down.setStatus(
        ""
    )

cvx_local_auth_failure_threshold_exceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 50)
)
cvx_local_auth_failure_threshold_exceeded.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapAuthThreshold"),
        ("APTIS-TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    cvx_local_auth_failure_threshold_exceeded.setStatus(
        ""
    )

cvx_preAuth_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 51)
)
cvx_preAuth_fail.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_preAuth_fail.setStatus(
        ""
    )

cvx_auth_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 52)
)
cvx_auth_fail.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_auth_fail.setStatus(
        ""
    )

cvx_tunnel_start = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 53)
)
cvx_tunnel_start.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapTunnelType"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_tunnel_start.setStatus(
        ""
    )

cvx_tunnel_stop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 54)
)
cvx_tunnel_stop.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapTunnelType"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_tunnel_stop.setStatus(
        ""
    )

cvx_tunnel_reject = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 55)
)
cvx_tunnel_reject.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapTunnelType"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_tunnel_reject.setStatus(
        ""
    )

cvx_radius_packet_discard = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 56)
)
cvx_radius_packet_discard.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapString"))
)
if mibBuilder.loadTexts:
    cvx_radius_packet_discard.setStatus(
        ""
    )

cvx_fanup = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 57)
)
cvx_fanup.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_fanup.setStatus(
        ""
    )

cvx_dc1up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 58)
)
cvx_dc1up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_dc1up.setStatus(
        ""
    )

cvx_dc2up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 59)
)
cvx_dc2up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_dc2up.setStatus(
        ""
    )

cvx_acdc1up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 62)
)
cvx_acdc1up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_acdc1up.setStatus(
        ""
    )

cvx_acdc2up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 63)
)
cvx_acdc2up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_acdc2up.setStatus(
        ""
    )

cvx_acdc3up = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 64)
)
cvx_acdc3up.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_acdc3up.setStatus(
        ""
    )

cvx_filter_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 65)
)
cvx_filter_error.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapFilterName"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvx_filter_error.setStatus(
        ""
    )

cvx_slave_flash_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 66)
)
cvx_slave_flash_missing.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvx_slave_flash_missing.setStatus(
        ""
    )

cvxSlaveSccFlashDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 67)
)
cvxSlaveSccFlashDetected.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFlashDetected.setStatus(
        ""
    )

cvxAuthServerRevived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 68)
)
cvxAuthServerRevived.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxAuthServerRevived.setStatus(
        ""
    )

cvxPrimaryDhcpServerContactFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 69)
)
cvxPrimaryDhcpServerContactFailed.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxPrimaryDhcpServerContactFailed.setStatus(
        ""
    )

cvxPrimaryDhcpServerContactRevived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 70)
)
cvxPrimaryDhcpServerContactRevived.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxPrimaryDhcpServerContactRevived.setStatus(
        ""
    )

cvxSecondaryDhcpServerContactFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 71)
)
cvxSecondaryDhcpServerContactFailed.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxSecondaryDhcpServerContactFailed.setStatus(
        ""
    )

cvxSlotTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 73)
)
cvxSlotTempWarning.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"),
        ("APTIS-TRAPS-MIB", "trapTempCurrent"),
        ("APTIS-TRAPS-MIB", "trapTempConfigWarningLevel"))
)
if mibBuilder.loadTexts:
    cvxSlotTempWarning.setStatus(
        ""
    )

cvxSlotTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 74)
)
cvxSlotTempNormal.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"),
        ("APTIS-TRAPS-MIB", "trapTempCurrent"),
        ("APTIS-TRAPS-MIB", "trapTempConfigWarningLevel"))
)
if mibBuilder.loadTexts:
    cvxSlotTempNormal.setStatus(
        ""
    )

cvxSlaveSccRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 75)
)
cvxSlaveSccRemoved.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccRemoved.setStatus(
        ""
    )

cvxSlaveSccInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 76)
)
cvxSlaveSccInserted.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccInserted.setStatus(
        ""
    )

cvxFailedSlaveSccRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 77)
)
cvxFailedSlaveSccRemoved.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxFailedSlaveSccRemoved.setStatus(
        ""
    )

cvxCardCrashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 79)
)
cvxCardCrashed.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvxCardCrashed.setStatus(
        ""
    )

cvxCardNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 80)
)
cvxCardNotResponding.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSlotNum"))
)
if mibBuilder.loadTexts:
    cvxCardNotResponding.setStatus(
        ""
    )

cvxLocalAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 81)
)
cvxLocalAuthenticationFailure.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapUserName"))
)
if mibBuilder.loadTexts:
    cvxLocalAuthenticationFailure.setStatus(
        ""
    )

cvxSessionAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 82)
)
cvxSessionAuthenticationFailure.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapSessionId"),
        ("APTIS-TRAPS-MIB", "trapVpopId"))
)
if mibBuilder.loadTexts:
    cvxSessionAuthenticationFailure.setStatus(
        ""
    )

encryptionNotAllowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 83)
)
encryptionNotAllowed.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    encryptionNotAllowed.setStatus(
        ""
    )

cvxRadiusdSessionDisc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 84)
)
cvxRadiusdSessionDisc.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxRadiusdSessionDisc.setStatus(
        ""
    )

cvxRadiusdUnknownClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 85)
)
cvxRadiusdUnknownClient.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxRadiusdUnknownClient.setStatus(
        ""
    )

cvxRadiusdClientAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 86)
)
cvxRadiusdClientAuthFailed.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"),
        ("APTIS-TRAPS-MIB", "trapIpAddr"))
)
if mibBuilder.loadTexts:
    cvxRadiusdClientAuthFailed.setStatus(
        ""
    )

cvxSlaveSccFileSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 87)
)
cvxSlaveSccFileSyncFailed.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFileSyncFailed.setStatus(
        ""
    )

cvxSlaveSccFileSyncCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 88)
)
cvxSlaveSccFileSyncCompleted.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFileSyncCompleted.setStatus(
        ""
    )

cvxSlaveSccFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2637, 2, 5, 1, 0, 89)
)
cvxSlaveSccFailed.setObjects(
      *(("APTIS-TRAPS-MIB", "trapGenNum"),
        ("APTIS-TRAPS-MIB", "trapPath"),
        ("APTIS-TRAPS-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    cvxSlaveSccFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-TRAPS-MIB",
    **{"aptisProtraps": aptisProtraps,
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
