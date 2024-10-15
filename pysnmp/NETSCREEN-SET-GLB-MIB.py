# SNMP MIB module (NETSCREEN-SET-GLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-GLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:57 2024
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

(netscreenSetting,
 netscreenSettingMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenSetting",
    "netscreenSettingMibModule")

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

netscreenSetGlbMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 10)
)
netscreenSetGlbMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetGlbMng_ObjectIdentity = ObjectIdentity
nsSetGlbMng = _NsSetGlbMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10)
)


class _NsSetGlbMngVPNEnable_Type(Integer32):
    """Custom type nsSetGlbMngVPNEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngVPNEnable_Type.__name__ = "Integer32"
_NsSetGlbMngVPNEnable_Object = MibScalar
nsSetGlbMngVPNEnable = _NsSetGlbMngVPNEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 1),
    _NsSetGlbMngVPNEnable_Type()
)
nsSetGlbMngVPNEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngVPNEnable.setStatus("current")


class _NsSetGlbMngEnable_Type(Integer32):
    """Custom type nsSetGlbMngEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngEnable_Type.__name__ = "Integer32"
_NsSetGlbMngEnable_Object = MibScalar
nsSetGlbMngEnable = _NsSetGlbMngEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 2),
    _NsSetGlbMngEnable_Type()
)
nsSetGlbMngEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngEnable.setStatus("current")


class _NsSetGlbProEnable_Type(Integer32):
    """Custom type nsSetGlbProEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbProEnable_Type.__name__ = "Integer32"
_NsSetGlbProEnable_Object = MibScalar
nsSetGlbProEnable = _NsSetGlbProEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 3),
    _NsSetGlbProEnable_Type()
)
nsSetGlbProEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbProEnable.setStatus("current")
_NsSetGlbManagerSetting_ObjectIdentity = ObjectIdentity
nsSetGlbManagerSetting = _NsSetGlbManagerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 4)
)


class _NsSetGlbMngSerName_Type(DisplayString):
    """Custom type nsSetGlbMngSerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetGlbMngSerName_Type.__name__ = "DisplayString"
_NsSetGlbMngSerName_Object = MibScalar
nsSetGlbMngSerName = _NsSetGlbMngSerName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 1),
    _NsSetGlbMngSerName_Type()
)
nsSetGlbMngSerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngSerName.setStatus("current")
_NsSetGlbMngSerTCP_Type = Integer32
_NsSetGlbMngSerTCP_Object = MibScalar
nsSetGlbMngSerTCP = _NsSetGlbMngSerTCP_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 2),
    _NsSetGlbMngSerTCP_Type()
)
nsSetGlbMngSerTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngSerTCP.setStatus("current")
_NsSetGlbMngSerUDP_Type = Integer32
_NsSetGlbMngSerUDP_Object = MibScalar
nsSetGlbMngSerUDP = _NsSetGlbMngSerUDP_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 3),
    _NsSetGlbMngSerUDP_Type()
)
nsSetGlbMngSerUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngSerUDP.setStatus("current")
_NsSetGlbMngLocal_Type = Integer32
_NsSetGlbMngLocal_Object = MibScalar
nsSetGlbMngLocal = _NsSetGlbMngLocal_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 4, 4),
    _NsSetGlbMngLocal_Type()
)
nsSetGlbMngLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngLocal.setStatus("current")
_NsSetGlbProManagerSetting_ObjectIdentity = ObjectIdentity
nsSetGlbProManagerSetting = _NsSetGlbProManagerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 5)
)
_NsSetGlbProPriSer_Type = IpAddress
_NsSetGlbProPriSer_Object = MibScalar
nsSetGlbProPriSer = _NsSetGlbProPriSer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 5, 1),
    _NsSetGlbProPriSer_Type()
)
nsSetGlbProPriSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbProPriSer.setStatus("current")
_NsSetGlbProSecSer_Type = IpAddress
_NsSetGlbProSecSer_Object = MibScalar
nsSetGlbProSecSer = _NsSetGlbProSecSer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 5, 2),
    _NsSetGlbProSecSer_Type()
)
nsSetGlbProSecSer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbProSecSer.setStatus("current")
_NsSetGlbMngSetting_ObjectIdentity = ObjectIdentity
nsSetGlbMngSetting = _NsSetGlbMngSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6)
)


class _NsSetGlbMngProtDist_Type(Integer32):
    """Custom type nsSetGlbMngProtDist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngProtDist_Type.__name__ = "Integer32"
_NsSetGlbMngProtDist_Object = MibScalar
nsSetGlbMngProtDist = _NsSetGlbMngProtDist_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 1),
    _NsSetGlbMngProtDist_Type()
)
nsSetGlbMngProtDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngProtDist.setStatus("current")


class _NsSetGlbMngEthStatis_Type(Integer32):
    """Custom type nsSetGlbMngEthStatis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngEthStatis_Type.__name__ = "Integer32"
_NsSetGlbMngEthStatis_Object = MibScalar
nsSetGlbMngEthStatis = _NsSetGlbMngEthStatis_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 2),
    _NsSetGlbMngEthStatis_Type()
)
nsSetGlbMngEthStatis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngEthStatis.setStatus("current")


class _NsSetGlbMngAttStatis_Type(Integer32):
    """Custom type nsSetGlbMngAttStatis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngAttStatis_Type.__name__ = "Integer32"
_NsSetGlbMngAttStatis_Object = MibScalar
nsSetGlbMngAttStatis = _NsSetGlbMngAttStatis_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 3),
    _NsSetGlbMngAttStatis_Type()
)
nsSetGlbMngAttStatis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngAttStatis.setStatus("current")


class _NsSetGlbMngPlyStatis_Type(Integer32):
    """Custom type nsSetGlbMngPlyStatis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngPlyStatis_Type.__name__ = "Integer32"
_NsSetGlbMngPlyStatis_Object = MibScalar
nsSetGlbMngPlyStatis = _NsSetGlbMngPlyStatis_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 4),
    _NsSetGlbMngPlyStatis_Type()
)
nsSetGlbMngPlyStatis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngPlyStatis.setStatus("current")


class _NsSetGlbMngFlowStatis_Type(Integer32):
    """Custom type nsSetGlbMngFlowStatis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngFlowStatis_Type.__name__ = "Integer32"
_NsSetGlbMngFlowStatis_Object = MibScalar
nsSetGlbMngFlowStatis = _NsSetGlbMngFlowStatis_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 5),
    _NsSetGlbMngFlowStatis_Type()
)
nsSetGlbMngFlowStatis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngFlowStatis.setStatus("current")


class _NsSetGlbMngTrafAlm_Type(Integer32):
    """Custom type nsSetGlbMngTrafAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngTrafAlm_Type.__name__ = "Integer32"
_NsSetGlbMngTrafAlm_Object = MibScalar
nsSetGlbMngTrafAlm = _NsSetGlbMngTrafAlm_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 6),
    _NsSetGlbMngTrafAlm_Type()
)
nsSetGlbMngTrafAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngTrafAlm.setStatus("current")


class _NsSetGlbMngAttAlm_Type(Integer32):
    """Custom type nsSetGlbMngAttAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngAttAlm_Type.__name__ = "Integer32"
_NsSetGlbMngAttAlm_Object = MibScalar
nsSetGlbMngAttAlm = _NsSetGlbMngAttAlm_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 7),
    _NsSetGlbMngAttAlm_Type()
)
nsSetGlbMngAttAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngAttAlm.setStatus("current")


class _NsSetGlbMngEvtAlm_Type(Integer32):
    """Custom type nsSetGlbMngEvtAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngEvtAlm_Type.__name__ = "Integer32"
_NsSetGlbMngEvtAlm_Object = MibScalar
nsSetGlbMngEvtAlm = _NsSetGlbMngEvtAlm_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 8),
    _NsSetGlbMngEvtAlm_Type()
)
nsSetGlbMngEvtAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngEvtAlm.setStatus("current")


class _NsSetGlbMngCfgLog_Type(Integer32):
    """Custom type nsSetGlbMngCfgLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngCfgLog_Type.__name__ = "Integer32"
_NsSetGlbMngCfgLog_Object = MibScalar
nsSetGlbMngCfgLog = _NsSetGlbMngCfgLog_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 9),
    _NsSetGlbMngCfgLog_Type()
)
nsSetGlbMngCfgLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngCfgLog.setStatus("current")


class _NsSetGlbMngTrafLog_Type(Integer32):
    """Custom type nsSetGlbMngTrafLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngTrafLog_Type.__name__ = "Integer32"
_NsSetGlbMngTrafLog_Object = MibScalar
nsSetGlbMngTrafLog = _NsSetGlbMngTrafLog_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 10),
    _NsSetGlbMngTrafLog_Type()
)
nsSetGlbMngTrafLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngTrafLog.setStatus("current")


class _NsSetGlbMngInfoLog_Type(Integer32):
    """Custom type nsSetGlbMngInfoLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngInfoLog_Type.__name__ = "Integer32"
_NsSetGlbMngInfoLog_Object = MibScalar
nsSetGlbMngInfoLog = _NsSetGlbMngInfoLog_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 11),
    _NsSetGlbMngInfoLog_Type()
)
nsSetGlbMngInfoLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngInfoLog.setStatus("current")


class _NsSetGlbMngSelfLog_Type(Integer32):
    """Custom type nsSetGlbMngSelfLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsSetGlbMngSelfLog_Type.__name__ = "Integer32"
_NsSetGlbMngSelfLog_Object = MibScalar
nsSetGlbMngSelfLog = _NsSetGlbMngSelfLog_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 10, 6, 12),
    _NsSetGlbMngSelfLog_Type()
)
nsSetGlbMngSelfLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetGlbMngSelfLog.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-GLB-MIB",
    **{"netscreenSetGlbMibModule": netscreenSetGlbMibModule,
       "nsSetGlbMng": nsSetGlbMng,
       "nsSetGlbMngVPNEnable": nsSetGlbMngVPNEnable,
       "nsSetGlbMngEnable": nsSetGlbMngEnable,
       "nsSetGlbProEnable": nsSetGlbProEnable,
       "nsSetGlbManagerSetting": nsSetGlbManagerSetting,
       "nsSetGlbMngSerName": nsSetGlbMngSerName,
       "nsSetGlbMngSerTCP": nsSetGlbMngSerTCP,
       "nsSetGlbMngSerUDP": nsSetGlbMngSerUDP,
       "nsSetGlbMngLocal": nsSetGlbMngLocal,
       "nsSetGlbProManagerSetting": nsSetGlbProManagerSetting,
       "nsSetGlbProPriSer": nsSetGlbProPriSer,
       "nsSetGlbProSecSer": nsSetGlbProSecSer,
       "nsSetGlbMngSetting": nsSetGlbMngSetting,
       "nsSetGlbMngProtDist": nsSetGlbMngProtDist,
       "nsSetGlbMngEthStatis": nsSetGlbMngEthStatis,
       "nsSetGlbMngAttStatis": nsSetGlbMngAttStatis,
       "nsSetGlbMngPlyStatis": nsSetGlbMngPlyStatis,
       "nsSetGlbMngFlowStatis": nsSetGlbMngFlowStatis,
       "nsSetGlbMngTrafAlm": nsSetGlbMngTrafAlm,
       "nsSetGlbMngAttAlm": nsSetGlbMngAttAlm,
       "nsSetGlbMngEvtAlm": nsSetGlbMngEvtAlm,
       "nsSetGlbMngCfgLog": nsSetGlbMngCfgLog,
       "nsSetGlbMngTrafLog": nsSetGlbMngTrafLog,
       "nsSetGlbMngInfoLog": nsSetGlbMngInfoLog,
       "nsSetGlbMngSelfLog": nsSetGlbMngSelfLog}
)
