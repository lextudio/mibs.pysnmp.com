# SNMP MIB module (NETSCREEN-SET-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-LOG-MIB
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

netscreenSetLogMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 8)
)
netscreenSetLogMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetLog_ObjectIdentity = ObjectIdentity
nsSetLog = _NsSetLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8)
)


class _NsSetLogEnable_Type(Integer32):
    """Custom type nsSetLogEnable based on Integer32"""
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


_NsSetLogEnable_Type.__name__ = "Integer32"
_NsSetLogEnable_Object = MibScalar
nsSetLogEnable = _NsSetLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 1),
    _NsSetLogEnable_Type()
)
nsSetLogEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogEnable.setStatus("current")


class _NsSetLogVPNEnable_Type(Integer32):
    """Custom type nsSetLogVPNEnable based on Integer32"""
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


_NsSetLogVPNEnable_Type.__name__ = "Integer32"
_NsSetLogVPNEnable_Object = MibScalar
nsSetLogVPNEnable = _NsSetLogVPNEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 2),
    _NsSetLogVPNEnable_Type()
)
nsSetLogVPNEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogVPNEnable.setStatus("current")


class _NsSetLogTraffic_Type(Integer32):
    """Custom type nsSetLogTraffic based on Integer32"""
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


_NsSetLogTraffic_Type.__name__ = "Integer32"
_NsSetLogTraffic_Object = MibScalar
nsSetLogTraffic = _NsSetLogTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 3),
    _NsSetLogTraffic_Type()
)
nsSetLogTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogTraffic.setStatus("current")


class _NsSetLogHostName_Type(DisplayString):
    """Custom type nsSetLogHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetLogHostName_Type.__name__ = "DisplayString"
_NsSetLogHostName_Object = MibScalar
nsSetLogHostName = _NsSetLogHostName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 4),
    _NsSetLogHostName_Type()
)
nsSetLogHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogHostName.setStatus("current")
_NsSetLogPort_Type = Integer32
_NsSetLogPort_Object = MibScalar
nsSetLogPort = _NsSetLogPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 5),
    _NsSetLogPort_Type()
)
nsSetLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogPort.setStatus("current")


class _NsSetLogSecFacility_Type(Integer32):
    """Custom type nsSetLogSecFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("auth-sec", 4),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )


_NsSetLogSecFacility_Type.__name__ = "Integer32"
_NsSetLogSecFacility_Object = MibScalar
nsSetLogSecFacility = _NsSetLogSecFacility_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 6),
    _NsSetLogSecFacility_Type()
)
nsSetLogSecFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogSecFacility.setStatus("current")


class _NsSetLogFacility_Type(Integer32):
    """Custom type nsSetLogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("auth-sec", 4),
          ("lcoal5", 21),
          ("loca7", 23),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local6", 22))
    )


_NsSetLogFacility_Type.__name__ = "Integer32"
_NsSetLogFacility_Object = MibScalar
nsSetLogFacility = _NsSetLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 7),
    _NsSetLogFacility_Type()
)
nsSetLogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogFacility.setStatus("current")


class _NsSetLogLevel_Type(Integer32):
    """Custom type nsSetLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aleart", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_NsSetLogLevel_Type.__name__ = "Integer32"
_NsSetLogLevel_Object = MibScalar
nsSetLogLevel = _NsSetLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 8),
    _NsSetLogLevel_Type()
)
nsSetLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogLevel.setStatus("current")


class _NsSetLogWebTrendsEnable_Type(Integer32):
    """Custom type nsSetLogWebTrendsEnable based on Integer32"""
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


_NsSetLogWebTrendsEnable_Type.__name__ = "Integer32"
_NsSetLogWebTrendsEnable_Object = MibScalar
nsSetLogWebTrendsEnable = _NsSetLogWebTrendsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 9),
    _NsSetLogWebTrendsEnable_Type()
)
nsSetLogWebTrendsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogWebTrendsEnable.setStatus("current")


class _NsSetLogWebTrendsVPNEnable_Type(Integer32):
    """Custom type nsSetLogWebTrendsVPNEnable based on Integer32"""
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


_NsSetLogWebTrendsVPNEnable_Type.__name__ = "Integer32"
_NsSetLogWebTrendsVPNEnable_Object = MibScalar
nsSetLogWebTrendsVPNEnable = _NsSetLogWebTrendsVPNEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 10),
    _NsSetLogWebTrendsVPNEnable_Type()
)
nsSetLogWebTrendsVPNEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogWebTrendsVPNEnable.setStatus("current")


class _NsSetLogWebTrendsHostName_Type(DisplayString):
    """Custom type nsSetLogWebTrendsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetLogWebTrendsHostName_Type.__name__ = "DisplayString"
_NsSetLogWebTrendsHostName_Object = MibScalar
nsSetLogWebTrendsHostName = _NsSetLogWebTrendsHostName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 11),
    _NsSetLogWebTrendsHostName_Type()
)
nsSetLogWebTrendsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogWebTrendsHostName.setStatus("current")
_NsSetLogWebTrendsPort_Type = Integer32
_NsSetLogWebTrendsPort_Object = MibScalar
nsSetLogWebTrendsPort = _NsSetLogWebTrendsPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 8, 12),
    _NsSetLogWebTrendsPort_Type()
)
nsSetLogWebTrendsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetLogWebTrendsPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-LOG-MIB",
    **{"netscreenSetLogMibModule": netscreenSetLogMibModule,
       "nsSetLog": nsSetLog,
       "nsSetLogEnable": nsSetLogEnable,
       "nsSetLogVPNEnable": nsSetLogVPNEnable,
       "nsSetLogTraffic": nsSetLogTraffic,
       "nsSetLogHostName": nsSetLogHostName,
       "nsSetLogPort": nsSetLogPort,
       "nsSetLogSecFacility": nsSetLogSecFacility,
       "nsSetLogFacility": nsSetLogFacility,
       "nsSetLogLevel": nsSetLogLevel,
       "nsSetLogWebTrendsEnable": nsSetLogWebTrendsEnable,
       "nsSetLogWebTrendsVPNEnable": nsSetLogWebTrendsVPNEnable,
       "nsSetLogWebTrendsHostName": nsSetLogWebTrendsHostName,
       "nsSetLogWebTrendsPort": nsSetLogWebTrendsPort}
)
