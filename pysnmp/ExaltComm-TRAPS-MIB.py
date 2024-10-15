# SNMP MIB module (ExaltComm-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ExaltComm-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:16 2024
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

(locLinkState,
 modelName,
 productsMIBNotifications) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "locLinkState",
    "modelName",
    "productsMIBNotifications")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Notifs_ObjectIdentity = ObjectIdentity
notifs = _Notifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1)
)
_NotifObjects_ObjectIdentity = ObjectIdentity
notifObjects = _NotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2)
)
_LocRadioStat_Type = Integer32
_LocRadioStat_Object = MibScalar
locRadioStat = _LocRadioStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 1),
    _LocRadioStat_Type()
)
locRadioStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locRadioStat.setStatus("current")
_RemRadioStat_Type = Integer32
_RemRadioStat_Object = MibScalar
remRadioStat = _RemRadioStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 2),
    _RemRadioStat_Type()
)
remRadioStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    remRadioStat.setStatus("current")
_LocRSLStat_Type = Integer32
_LocRSLStat_Object = MibScalar
locRSLStat = _LocRSLStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 3),
    _LocRSLStat_Type()
)
locRSLStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locRSLStat.setStatus("current")
_LocTempStat_Type = Integer32
_LocTempStat_Object = MibScalar
locTempStat = _LocTempStat_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 4),
    _LocTempStat_Type()
)
locTempStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locTempStat.setStatus("current")
_LocRSLStatVert_Type = Integer32
_LocRSLStatVert_Object = MibScalar
locRSLStatVert = _LocRSLStatVert_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 5),
    _LocRSLStatVert_Type()
)
locRSLStatVert.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locRSLStatVert.setStatus("current")


class _LocEthWtmkHitDurationETH1_Type(Integer32):
    """Custom type locEthWtmkHitDurationETH1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_LocEthWtmkHitDurationETH1_Type.__name__ = "Integer32"
_LocEthWtmkHitDurationETH1_Object = MibScalar
locEthWtmkHitDurationETH1 = _LocEthWtmkHitDurationETH1_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 6),
    _LocEthWtmkHitDurationETH1_Type()
)
locEthWtmkHitDurationETH1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locEthWtmkHitDurationETH1.setStatus("current")


class _LocEthWtmkHitDurationETH2_Type(Integer32):
    """Custom type locEthWtmkHitDurationETH2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_LocEthWtmkHitDurationETH2_Type.__name__ = "Integer32"
_LocEthWtmkHitDurationETH2_Object = MibScalar
locEthWtmkHitDurationETH2 = _LocEthWtmkHitDurationETH2_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 7),
    _LocEthWtmkHitDurationETH2_Type()
)
locEthWtmkHitDurationETH2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locEthWtmkHitDurationETH2.setStatus("current")


class _LocEthWtmkHitDurationETH3_Type(Integer32):
    """Custom type locEthWtmkHitDurationETH3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_LocEthWtmkHitDurationETH3_Type.__name__ = "Integer32"
_LocEthWtmkHitDurationETH3_Object = MibScalar
locEthWtmkHitDurationETH3 = _LocEthWtmkHitDurationETH3_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 8),
    _LocEthWtmkHitDurationETH3_Type()
)
locEthWtmkHitDurationETH3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locEthWtmkHitDurationETH3.setStatus("current")


class _LocEthWtmkHitDurationETH4_Type(Integer32):
    """Custom type locEthWtmkHitDurationETH4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_LocEthWtmkHitDurationETH4_Type.__name__ = "Integer32"
_LocEthWtmkHitDurationETH4_Object = MibScalar
locEthWtmkHitDurationETH4 = _LocEthWtmkHitDurationETH4_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 9),
    _LocEthWtmkHitDurationETH4_Type()
)
locEthWtmkHitDurationETH4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locEthWtmkHitDurationETH4.setStatus("current")
_LocRSLStatHoriz_Type = Integer32
_LocRSLStatHoriz_Object = MibScalar
locRSLStatHoriz = _LocRSLStatHoriz_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 2, 10),
    _LocRSLStatHoriz_Type()
)
locRSLStatHoriz.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    locRSLStatHoriz.setStatus("current")

# Managed Objects groups


# Notification objects

cold_start_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 1)
)
cold_start_notif.setObjects(
    ("ExaltComProducts", "modelName")
)
if mibBuilder.loadTexts:
    cold_start_notif.setStatus(
        "current"
    )

radio_syn_alm_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 2)
)
radio_syn_alm_notif.setObjects(
    ("ExaltComProducts", "locLinkState")
)
if mibBuilder.loadTexts:
    radio_syn_alm_notif.setStatus(
        "current"
    )

loc_radio_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 3)
)
loc_radio_stat_notif.setObjects(
    ("ExaltComm-TRAPS-MIB", "locRadioStat")
)
if mibBuilder.loadTexts:
    loc_radio_stat_notif.setStatus(
        "current"
    )

rem_radio_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 4)
)
rem_radio_stat_notif.setObjects(
    ("ExaltComm-TRAPS-MIB", "remRadioStat")
)
if mibBuilder.loadTexts:
    rem_radio_stat_notif.setStatus(
        "current"
    )

loc_rsl_stat_horiz_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 5)
)
loc_rsl_stat_horiz_notif.setObjects(
    ("ExaltComm-TRAPS-MIB", "locRSLStatHoriz")
)
if mibBuilder.loadTexts:
    loc_rsl_stat_horiz_notif.setStatus(
        "current"
    )

loc_temp_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 6)
)
loc_temp_stat_notif.setObjects(
    ("ExaltComm-TRAPS-MIB", "locTempStat")
)
if mibBuilder.loadTexts:
    loc_temp_stat_notif.setStatus(
        "current"
    )

loc_rsl_stat_vert_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 7)
)
loc_rsl_stat_vert_notif.setObjects(
    ("ExaltComm-TRAPS-MIB", "locRSLStatVert")
)
if mibBuilder.loadTexts:
    loc_rsl_stat_vert_notif.setStatus(
        "current"
    )

chan_syn_alm_v_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 8)
)
chan_syn_alm_v_notif.setObjects(
    ("ExaltComProducts", "locLinkState")
)
if mibBuilder.loadTexts:
    chan_syn_alm_v_notif.setStatus(
        "current"
    )

chan_syn_alm_h_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 9)
)
chan_syn_alm_h_notif.setObjects(
    ("ExaltComProducts", "locLinkState")
)
if mibBuilder.loadTexts:
    chan_syn_alm_h_notif.setStatus(
        "current"
    )

loc_rsl_stat_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 10)
)
loc_rsl_stat_notif.setObjects(
    ("ExaltComm-TRAPS-MIB", "locRSLStat")
)
if mibBuilder.loadTexts:
    loc_rsl_stat_notif.setStatus(
        "current"
    )

eth_watermark_hit_duration_notif = NotificationType(
    (1, 3, 6, 1, 4, 1, 25651, 1, 1, 1, 11)
)
eth_watermark_hit_duration_notif.setObjects(
      *(("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH1"),
        ("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH2"),
        ("ExaltComm-TRAPS-MIB", "locEthWtmkHitDurationETH3"))
)
if mibBuilder.loadTexts:
    eth_watermark_hit_duration_notif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ExaltComm-TRAPS-MIB",
    **{"notifs": notifs,
       "cold-start-notif": cold_start_notif,
       "radio-syn-alm-notif": radio_syn_alm_notif,
       "loc-radio-stat-notif": loc_radio_stat_notif,
       "rem-radio-stat-notif": rem_radio_stat_notif,
       "loc-rsl-stat-horiz-notif": loc_rsl_stat_horiz_notif,
       "loc-temp-stat-notif": loc_temp_stat_notif,
       "loc-rsl-stat-vert-notif": loc_rsl_stat_vert_notif,
       "chan-syn-alm-v-notif": chan_syn_alm_v_notif,
       "chan-syn-alm-h-notif": chan_syn_alm_h_notif,
       "loc-rsl-stat-notif": loc_rsl_stat_notif,
       "eth-watermark-hit-duration-notif": eth_watermark_hit_duration_notif,
       "notifObjects": notifObjects,
       "locRadioStat": locRadioStat,
       "remRadioStat": remRadioStat,
       "locRSLStat": locRSLStat,
       "locTempStat": locTempStat,
       "locRSLStatVert": locRSLStatVert,
       "locEthWtmkHitDurationETH1": locEthWtmkHitDurationETH1,
       "locEthWtmkHitDurationETH2": locEthWtmkHitDurationETH2,
       "locEthWtmkHitDurationETH3": locEthWtmkHitDurationETH3,
       "locEthWtmkHitDurationETH4": locEthWtmkHitDurationETH4,
       "locRSLStatHoriz": locRSLStatHoriz}
)
