# SNMP MIB module (TPLINK-BANDWIDTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-BANDWIDTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:50 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkBandWidthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23)
)
tplinkBandWidthMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkBandWidthMIBObjects_ObjectIdentity = ObjectIdentity
tplinkBandWidthMIBObjects = _TplinkBandWidthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1)
)
_TpRateLimit_ObjectIdentity = ObjectIdentity
tpRateLimit = _TpRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1)
)
_TpRateLimitTable_Object = MibTable
tpRateLimitTable = _TpRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpRateLimitTable.setStatus("current")
_TpRateLimitEntry_Object = MibTableRow
tpRateLimitEntry = _TpRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1)
)
tpRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpRateLimitEntry.setStatus("current")
_TpRateLimitPort_Type = DisplayString
_TpRateLimitPort_Object = MibTableColumn
tpRateLimitPort = _TpRateLimitPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 1),
    _TpRateLimitPort_Type()
)
tpRateLimitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRateLimitPort.setStatus("current")


class _TpRateLimitIngressRate_Type(Integer32):
    """Custom type tpRateLimitIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TpRateLimitIngressRate_Type.__name__ = "Integer32"
_TpRateLimitIngressRate_Object = MibTableColumn
tpRateLimitIngressRate = _TpRateLimitIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 2),
    _TpRateLimitIngressRate_Type()
)
tpRateLimitIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRateLimitIngressRate.setStatus("current")


class _TpRateLimitEgressRate_Type(Integer32):
    """Custom type tpRateLimitEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TpRateLimitEgressRate_Type.__name__ = "Integer32"
_TpRateLimitEgressRate_Object = MibTableColumn
tpRateLimitEgressRate = _TpRateLimitEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 3),
    _TpRateLimitEgressRate_Type()
)
tpRateLimitEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRateLimitEgressRate.setStatus("current")


class _TpRateLimitPortLag_Type(OctetString):
    """Custom type tpRateLimitPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpRateLimitPortLag_Type.__name__ = "OctetString"
_TpRateLimitPortLag_Object = MibTableColumn
tpRateLimitPortLag = _TpRateLimitPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 1, 1, 1, 4),
    _TpRateLimitPortLag_Type()
)
tpRateLimitPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpRateLimitPortLag.setStatus("current")
_TpStormControl_ObjectIdentity = ObjectIdentity
tpStormControl = _TpStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2)
)
_TpStormControlEnPPSTable_Object = MibTable
tpStormControlEnPPSTable = _TpStormControlEnPPSTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpStormControlEnPPSTable.setStatus("current")
_TpStormControlEnPPSEntry_Object = MibTableRow
tpStormControlEnPPSEntry = _TpStormControlEnPPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1)
)
tpStormControlEnPPSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpStormControlEnPPSEntry.setStatus("current")
_TpStormControlEnPPSPort_Type = DisplayString
_TpStormControlEnPPSPort_Object = MibTableColumn
tpStormControlEnPPSPort = _TpStormControlEnPPSPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 1),
    _TpStormControlEnPPSPort_Type()
)
tpStormControlEnPPSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlEnPPSPort.setStatus("current")


class _TpStormControlEnablePPS_Type(Integer32):
    """Custom type tpStormControlEnablePPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStormControlEnablePPS_Type.__name__ = "Integer32"
_TpStormControlEnablePPS_Object = MibTableColumn
tpStormControlEnablePPS = _TpStormControlEnablePPS_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 2),
    _TpStormControlEnablePPS_Type()
)
tpStormControlEnablePPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlEnablePPS.setStatus("current")


class _TpStormControlEnPPSPortLag_Type(OctetString):
    """Custom type tpStormControlEnPPSPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpStormControlEnPPSPortLag_Type.__name__ = "OctetString"
_TpStormControlEnPPSPortLag_Object = MibTableColumn
tpStormControlEnPPSPortLag = _TpStormControlEnPPSPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 1, 1, 3),
    _TpStormControlEnPPSPortLag_Type()
)
tpStormControlEnPPSPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlEnPPSPortLag.setStatus("current")
_TpStormControlModeTable_Object = MibTable
tpStormControlModeTable = _TpStormControlModeTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tpStormControlModeTable.setStatus("current")
_TpStormControlModeEntry_Object = MibTableRow
tpStormControlModeEntry = _TpStormControlModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 2, 1)
)
tpStormControlModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpStormControlModeEntry.setStatus("current")
_TpStormControlModePort_Type = DisplayString
_TpStormControlModePort_Object = MibTableColumn
tpStormControlModePort = _TpStormControlModePort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 2, 1, 1),
    _TpStormControlModePort_Type()
)
tpStormControlModePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlModePort.setStatus("current")


class _TpStormControlBroadCastRateMode_Type(Integer32):
    """Custom type tpStormControlBroadCastRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("pps", 2),
          ("ratio", 1))
    )


_TpStormControlBroadCastRateMode_Type.__name__ = "Integer32"
_TpStormControlBroadCastRateMode_Object = MibTableColumn
tpStormControlBroadCastRateMode = _TpStormControlBroadCastRateMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 2, 1, 2),
    _TpStormControlBroadCastRateMode_Type()
)
tpStormControlBroadCastRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlBroadCastRateMode.setStatus("current")


class _TpStormControlMultiCastRateMode_Type(Integer32):
    """Custom type tpStormControlMultiCastRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("pps", 2),
          ("ratio", 1))
    )


_TpStormControlMultiCastRateMode_Type.__name__ = "Integer32"
_TpStormControlMultiCastRateMode_Object = MibTableColumn
tpStormControlMultiCastRateMode = _TpStormControlMultiCastRateMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 2, 1, 3),
    _TpStormControlMultiCastRateMode_Type()
)
tpStormControlMultiCastRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlMultiCastRateMode.setStatus("current")


class _TpStormControlULRateMode_Type(Integer32):
    """Custom type tpStormControlULRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("pps", 2),
          ("ratio", 1))
    )


_TpStormControlULRateMode_Type.__name__ = "Integer32"
_TpStormControlULRateMode_Object = MibTableColumn
tpStormControlULRateMode = _TpStormControlULRateMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 2, 1, 4),
    _TpStormControlULRateMode_Type()
)
tpStormControlULRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlULRateMode.setStatus("current")


class _TpStormControlModePortLag_Type(OctetString):
    """Custom type tpStormControlModePortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpStormControlModePortLag_Type.__name__ = "OctetString"
_TpStormControlModePortLag_Object = MibTableColumn
tpStormControlModePortLag = _TpStormControlModePortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 2, 1, 5),
    _TpStormControlModePortLag_Type()
)
tpStormControlModePortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlModePortLag.setStatus("current")
_TpStormControlTable_Object = MibTable
tpStormControlTable = _TpStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tpStormControlTable.setStatus("current")
_TpStormControlEntry_Object = MibTableRow
tpStormControlEntry = _TpStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 3, 1)
)
tpStormControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpStormControlEntry.setStatus("current")
_TpStormControlPort_Type = DisplayString
_TpStormControlPort_Object = MibTableColumn
tpStormControlPort = _TpStormControlPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 3, 1, 1),
    _TpStormControlPort_Type()
)
tpStormControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlPort.setStatus("current")


class _TpStormControlBroadCastRate_Type(Integer32):
    """Custom type tpStormControlBroadCastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1488000),
    )


_TpStormControlBroadCastRate_Type.__name__ = "Integer32"
_TpStormControlBroadCastRate_Object = MibTableColumn
tpStormControlBroadCastRate = _TpStormControlBroadCastRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 3, 1, 2),
    _TpStormControlBroadCastRate_Type()
)
tpStormControlBroadCastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlBroadCastRate.setStatus("current")


class _TpStormControlMultiCastRate_Type(Integer32):
    """Custom type tpStormControlMultiCastRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1488000),
    )


_TpStormControlMultiCastRate_Type.__name__ = "Integer32"
_TpStormControlMultiCastRate_Object = MibTableColumn
tpStormControlMultiCastRate = _TpStormControlMultiCastRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 3, 1, 3),
    _TpStormControlMultiCastRate_Type()
)
tpStormControlMultiCastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlMultiCastRate.setStatus("current")


class _TpStormControlULRate_Type(Integer32):
    """Custom type tpStormControlULRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1488000),
    )


_TpStormControlULRate_Type.__name__ = "Integer32"
_TpStormControlULRate_Object = MibTableColumn
tpStormControlULRate = _TpStormControlULRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 3, 1, 4),
    _TpStormControlULRate_Type()
)
tpStormControlULRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStormControlULRate.setStatus("current")


class _TpStormControlPortLag_Type(OctetString):
    """Custom type tpStormControlPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpStormControlPortLag_Type.__name__ = "OctetString"
_TpStormControlPortLag_Object = MibTableColumn
tpStormControlPortLag = _TpStormControlPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 1, 2, 3, 1, 5),
    _TpStormControlPortLag_Type()
)
tpStormControlPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStormControlPortLag.setStatus("current")
_TplinkBandWidthNotifications_ObjectIdentity = ObjectIdentity
tplinkBandWidthNotifications = _TplinkBandWidthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2)
)

# Managed Objects groups


# Notification objects

tpBroadcastRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 1)
)
tpBroadcastRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpStormControlPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpStormControlBroadCastRate"))
)
if mibBuilder.loadTexts:
    tpBroadcastRateExceed.setStatus(
        "current"
    )

tpMulticastRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 2)
)
tpMulticastRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpStormControlPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpStormControlMultiCastRate"))
)
if mibBuilder.loadTexts:
    tpMulticastRateExceed.setStatus(
        "current"
    )

tpIngressRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 3)
)
tpIngressRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpRateLimitPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpRateLimitIngressRate"))
)
if mibBuilder.loadTexts:
    tpIngressRateExceed.setStatus(
        "current"
    )

tpEgressRateExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 23, 2, 4)
)
tpEgressRateExceed.setObjects(
      *(("TPLINK-BANDWIDTH-MIB", "tpRateLimitPort"),
        ("TPLINK-BANDWIDTH-MIB", "tpRateLimitEgressRate"))
)
if mibBuilder.loadTexts:
    tpEgressRateExceed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-BANDWIDTH-MIB",
    **{"tplinkBandWidthMIB": tplinkBandWidthMIB,
       "tplinkBandWidthMIBObjects": tplinkBandWidthMIBObjects,
       "tpRateLimit": tpRateLimit,
       "tpRateLimitTable": tpRateLimitTable,
       "tpRateLimitEntry": tpRateLimitEntry,
       "tpRateLimitPort": tpRateLimitPort,
       "tpRateLimitIngressRate": tpRateLimitIngressRate,
       "tpRateLimitEgressRate": tpRateLimitEgressRate,
       "tpRateLimitPortLag": tpRateLimitPortLag,
       "tpStormControl": tpStormControl,
       "tpStormControlEnPPSTable": tpStormControlEnPPSTable,
       "tpStormControlEnPPSEntry": tpStormControlEnPPSEntry,
       "tpStormControlEnPPSPort": tpStormControlEnPPSPort,
       "tpStormControlEnablePPS": tpStormControlEnablePPS,
       "tpStormControlEnPPSPortLag": tpStormControlEnPPSPortLag,
       "tpStormControlModeTable": tpStormControlModeTable,
       "tpStormControlModeEntry": tpStormControlModeEntry,
       "tpStormControlModePort": tpStormControlModePort,
       "tpStormControlBroadCastRateMode": tpStormControlBroadCastRateMode,
       "tpStormControlMultiCastRateMode": tpStormControlMultiCastRateMode,
       "tpStormControlULRateMode": tpStormControlULRateMode,
       "tpStormControlModePortLag": tpStormControlModePortLag,
       "tpStormControlTable": tpStormControlTable,
       "tpStormControlEntry": tpStormControlEntry,
       "tpStormControlPort": tpStormControlPort,
       "tpStormControlBroadCastRate": tpStormControlBroadCastRate,
       "tpStormControlMultiCastRate": tpStormControlMultiCastRate,
       "tpStormControlULRate": tpStormControlULRate,
       "tpStormControlPortLag": tpStormControlPortLag,
       "tplinkBandWidthNotifications": tplinkBandWidthNotifications,
       "tpBroadcastRateExceed": tpBroadcastRateExceed,
       "tpMulticastRateExceed": tpMulticastRateExceed,
       "tpIngressRateExceed": tpIngressRateExceed,
       "tpEgressRateExceed": tpEgressRateExceed}
)
