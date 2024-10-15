# SNMP MIB module (ZXR10-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:01 2024
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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_Zxr10switch_ObjectIdentity = ObjectIdentity
zxr10switch = _Zxr10switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102)
)
_Zxr10ethernetOam_ObjectIdentity = ObjectIdentity
zxr10ethernetOam = _Zxr10ethernetOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20)
)
_Zxr10ethernetOamGlobalConfig_ObjectIdentity = ObjectIdentity
zxr10ethernetOamGlobalConfig = _Zxr10ethernetOamGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 1)
)


class _Zxr10ethernetOamGlobalEnable_Type(Integer32):
    """Custom type zxr10ethernetOamGlobalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disnable", 0),
          ("enable", 1))
    )


_Zxr10ethernetOamGlobalEnable_Type.__name__ = "Integer32"
_Zxr10ethernetOamGlobalEnable_Object = MibScalar
zxr10ethernetOamGlobalEnable = _Zxr10ethernetOamGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 1, 1),
    _Zxr10ethernetOamGlobalEnable_Type()
)
zxr10ethernetOamGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamGlobalEnable.setStatus("current")


class _Zxr10ethernetOamOuiInformation_Type(DisplayString):
    """Custom type zxr10ethernetOamOuiInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_Zxr10ethernetOamOuiInformation_Type.__name__ = "DisplayString"
_Zxr10ethernetOamOuiInformation_Object = MibScalar
zxr10ethernetOamOuiInformation = _Zxr10ethernetOamOuiInformation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 1, 2),
    _Zxr10ethernetOamOuiInformation_Type()
)
zxr10ethernetOamOuiInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamOuiInformation.setStatus("current")


class _Zxr10ethernetOamRemoteLoopbackTimeout_Type(Unsigned32):
    """Custom type zxr10ethernetOamRemoteLoopbackTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Zxr10ethernetOamRemoteLoopbackTimeout_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamRemoteLoopbackTimeout_Object = MibScalar
zxr10ethernetOamRemoteLoopbackTimeout = _Zxr10ethernetOamRemoteLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 1, 3),
    _Zxr10ethernetOamRemoteLoopbackTimeout_Type()
)
zxr10ethernetOamRemoteLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamRemoteLoopbackTimeout.setStatus("current")
_Zxr10ethernetOamIfConfigTable_Object = MibTable
zxr10ethernetOamIfConfigTable = _Zxr10ethernetOamIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2)
)
if mibBuilder.loadTexts:
    zxr10ethernetOamIfConfigTable.setStatus("current")
_Zxr10ethernetOamIfConfigEntry_Object = MibTableRow
zxr10ethernetOamIfConfigEntry = _Zxr10ethernetOamIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1)
)
zxr10ethernetOamIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10ethernetOamIfConfigEntry.setStatus("current")


class _Zxr10ethernetOamIfEnable_Type(Integer32):
    """Custom type zxr10ethernetOamIfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disnable", 0),
          ("enable", 1))
    )


_Zxr10ethernetOamIfEnable_Type.__name__ = "Integer32"
_Zxr10ethernetOamIfEnable_Object = MibTableColumn
zxr10ethernetOamIfEnable = _Zxr10ethernetOamIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 1),
    _Zxr10ethernetOamIfEnable_Type()
)
zxr10ethernetOamIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamIfEnable.setStatus("current")


class _Zxr10ethernetOamRemoteLoopbackEnable_Type(Integer32):
    """Custom type zxr10ethernetOamRemoteLoopbackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disnable", 0),
          ("enable", 1))
    )


_Zxr10ethernetOamRemoteLoopbackEnable_Type.__name__ = "Integer32"
_Zxr10ethernetOamRemoteLoopbackEnable_Object = MibTableColumn
zxr10ethernetOamRemoteLoopbackEnable = _Zxr10ethernetOamRemoteLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 2),
    _Zxr10ethernetOamRemoteLoopbackEnable_Type()
)
zxr10ethernetOamRemoteLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamRemoteLoopbackEnable.setStatus("current")


class _Zxr10ethernetOamifperiod_Type(Unsigned32):
    """Custom type zxr10ethernetOamifperiod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Zxr10ethernetOamifperiod_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifperiod_Object = MibTableColumn
zxr10ethernetOamifperiod = _Zxr10ethernetOamifperiod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 3),
    _Zxr10ethernetOamifperiod_Type()
)
zxr10ethernetOamifperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifperiod.setStatus("current")


class _Zxr10ethernetOamifmode_Type(Unsigned32):
    """Custom type zxr10ethernetOamifmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Zxr10ethernetOamifmode_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifmode_Object = MibTableColumn
zxr10ethernetOamifmode = _Zxr10ethernetOamifmode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 4),
    _Zxr10ethernetOamifmode_Type()
)
zxr10ethernetOamifmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifmode.setStatus("current")


class _Zxr10ethernetOamiftimeout_Type(Unsigned32):
    """Custom type zxr10ethernetOamiftimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_Zxr10ethernetOamiftimeout_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamiftimeout_Object = MibTableColumn
zxr10ethernetOamiftimeout = _Zxr10ethernetOamiftimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 5),
    _Zxr10ethernetOamiftimeout_Type()
)
zxr10ethernetOamiftimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamiftimeout.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorEnable_Type(Integer32):
    """Custom type zxr10ethernetOamifLinkMonitorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disnable", 0),
          ("enable", 1))
    )


_Zxr10ethernetOamifLinkMonitorEnable_Type.__name__ = "Integer32"
_Zxr10ethernetOamifLinkMonitorEnable_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorEnable = _Zxr10ethernetOamifLinkMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 6),
    _Zxr10ethernetOamifLinkMonitorEnable_Type()
)
zxr10ethernetOamifLinkMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorEnable.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold = _Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 7),
    _Zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold_Type()
)
zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorSymbolPeriodwindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorSymbolPeriodwindow = _Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 8),
    _Zxr10ethernetOamifLinkMonitorSymbolPeriodwindow_Type()
)
zxr10ethernetOamifLinkMonitorSymbolPeriodwindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorSymbolPeriodwindow.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorFramethreshold_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorFramethreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Zxr10ethernetOamifLinkMonitorFramethreshold_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorFramethreshold_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorFramethreshold = _Zxr10ethernetOamifLinkMonitorFramethreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 9),
    _Zxr10ethernetOamifLinkMonitorFramethreshold_Type()
)
zxr10ethernetOamifLinkMonitorFramethreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorFramethreshold.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorFramewindow_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorFramewindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Zxr10ethernetOamifLinkMonitorFramewindow_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorFramewindow_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorFramewindow = _Zxr10ethernetOamifLinkMonitorFramewindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 10),
    _Zxr10ethernetOamifLinkMonitorFramewindow_Type()
)
zxr10ethernetOamifLinkMonitorFramewindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorFramewindow.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorFramePeriodthreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorFramePeriodthreshold = _Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 11),
    _Zxr10ethernetOamifLinkMonitorFramePeriodthreshold_Type()
)
zxr10ethernetOamifLinkMonitorFramePeriodthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorFramePeriodthreshold.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorFramePeriodwindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600000),
    )


_Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorFramePeriodwindow = _Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 12),
    _Zxr10ethernetOamifLinkMonitorFramePeriodwindow_Type()
)
zxr10ethernetOamifLinkMonitorFramePeriodwindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorFramePeriodwindow.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorFrameSecondsthreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorFrameSecondsthreshold = _Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 13),
    _Zxr10ethernetOamifLinkMonitorFrameSecondsthreshold_Type()
)
zxr10ethernetOamifLinkMonitorFrameSecondsthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorFrameSecondsthreshold.setStatus("current")


class _Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Type(Unsigned32):
    """Custom type zxr10ethernetOamifLinkMonitorFrameSecondswindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 900),
    )


_Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Type.__name__ = "Unsigned32"
_Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Object = MibTableColumn
zxr10ethernetOamifLinkMonitorFrameSecondswindow = _Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 14),
    _Zxr10ethernetOamifLinkMonitorFrameSecondswindow_Type()
)
zxr10ethernetOamifLinkMonitorFrameSecondswindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10ethernetOamifLinkMonitorFrameSecondswindow.setStatus("current")
_Zxr10ethernetOamifName_Type = DisplayString
_Zxr10ethernetOamifName_Object = MibTableColumn
zxr10ethernetOamifName = _Zxr10ethernetOamifName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 2, 1, 15),
    _Zxr10ethernetOamifName_Type()
)
zxr10ethernetOamifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ethernetOamifName.setStatus("current")
_Zxr10ethernetOamShowTable_Object = MibTable
zxr10ethernetOamShowTable = _Zxr10ethernetOamShowTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 3)
)
if mibBuilder.loadTexts:
    zxr10ethernetOamShowTable.setStatus("current")
_Zxr10ethernetOamShowEntry_Object = MibTableRow
zxr10ethernetOamShowEntry = _Zxr10ethernetOamShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 3, 1)
)
zxr10ethernetOamShowEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10ethernetOamShowEntry.setStatus("current")
_Zxr10ethernetOamShowDiscovery_Type = DisplayString
_Zxr10ethernetOamShowDiscovery_Object = MibTableColumn
zxr10ethernetOamShowDiscovery = _Zxr10ethernetOamShowDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 3, 1, 1),
    _Zxr10ethernetOamShowDiscovery_Type()
)
zxr10ethernetOamShowDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ethernetOamShowDiscovery.setStatus("current")
_Zxr10ethernetOamShowLinkMonitor_Type = DisplayString
_Zxr10ethernetOamShowLinkMonitor_Object = MibTableColumn
zxr10ethernetOamShowLinkMonitor = _Zxr10ethernetOamShowLinkMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 3, 1, 2),
    _Zxr10ethernetOamShowLinkMonitor_Type()
)
zxr10ethernetOamShowLinkMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ethernetOamShowLinkMonitor.setStatus("current")
_Zxr10ethernetOamShowStatistics_Type = DisplayString
_Zxr10ethernetOamShowStatistics_Object = MibTableColumn
zxr10ethernetOamShowStatistics = _Zxr10ethernetOamShowStatistics_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 20, 3, 1, 3),
    _Zxr10ethernetOamShowStatistics_Type()
)
zxr10ethernetOamShowStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ethernetOamShowStatistics.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-OAM-MIB",
    **{"DisplayString": DisplayString,
       "zte": zte,
       "zxr10": zxr10,
       "zxr10switch": zxr10switch,
       "zxr10ethernetOam": zxr10ethernetOam,
       "zxr10ethernetOamGlobalConfig": zxr10ethernetOamGlobalConfig,
       "zxr10ethernetOamGlobalEnable": zxr10ethernetOamGlobalEnable,
       "zxr10ethernetOamOuiInformation": zxr10ethernetOamOuiInformation,
       "zxr10ethernetOamRemoteLoopbackTimeout": zxr10ethernetOamRemoteLoopbackTimeout,
       "zxr10ethernetOamIfConfigTable": zxr10ethernetOamIfConfigTable,
       "zxr10ethernetOamIfConfigEntry": zxr10ethernetOamIfConfigEntry,
       "zxr10ethernetOamIfEnable": zxr10ethernetOamIfEnable,
       "zxr10ethernetOamRemoteLoopbackEnable": zxr10ethernetOamRemoteLoopbackEnable,
       "zxr10ethernetOamifperiod": zxr10ethernetOamifperiod,
       "zxr10ethernetOamifmode": zxr10ethernetOamifmode,
       "zxr10ethernetOamiftimeout": zxr10ethernetOamiftimeout,
       "zxr10ethernetOamifLinkMonitorEnable": zxr10ethernetOamifLinkMonitorEnable,
       "zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold": zxr10ethernetOamifLinkMonitorSymbolPeriodthreshold,
       "zxr10ethernetOamifLinkMonitorSymbolPeriodwindow": zxr10ethernetOamifLinkMonitorSymbolPeriodwindow,
       "zxr10ethernetOamifLinkMonitorFramethreshold": zxr10ethernetOamifLinkMonitorFramethreshold,
       "zxr10ethernetOamifLinkMonitorFramewindow": zxr10ethernetOamifLinkMonitorFramewindow,
       "zxr10ethernetOamifLinkMonitorFramePeriodthreshold": zxr10ethernetOamifLinkMonitorFramePeriodthreshold,
       "zxr10ethernetOamifLinkMonitorFramePeriodwindow": zxr10ethernetOamifLinkMonitorFramePeriodwindow,
       "zxr10ethernetOamifLinkMonitorFrameSecondsthreshold": zxr10ethernetOamifLinkMonitorFrameSecondsthreshold,
       "zxr10ethernetOamifLinkMonitorFrameSecondswindow": zxr10ethernetOamifLinkMonitorFrameSecondswindow,
       "zxr10ethernetOamifName": zxr10ethernetOamifName,
       "zxr10ethernetOamShowTable": zxr10ethernetOamShowTable,
       "zxr10ethernetOamShowEntry": zxr10ethernetOamShowEntry,
       "zxr10ethernetOamShowDiscovery": zxr10ethernetOamShowDiscovery,
       "zxr10ethernetOamShowLinkMonitor": zxr10ethernetOamShowLinkMonitor,
       "zxr10ethernetOamShowStatistics": zxr10ethernetOamShowStatistics}
)
