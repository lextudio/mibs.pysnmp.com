# SNMP MIB module (NETSCREEN-SET-URL-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-SET-URL-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:59 2024
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

netscreenSetUrlFilterMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 0, 4)
)
netscreenSetUrlFilterMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-12 00:00",
         "2001-09-28 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsSetURLFilter_ObjectIdentity = ObjectIdentity
nsSetURLFilter = _NsSetURLFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4)
)


class _NsSetUrlFilterViaWebsense_Type(Integer32):
    """Custom type nsSetUrlFilterViaWebsense based on Integer32"""
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


_NsSetUrlFilterViaWebsense_Type.__name__ = "Integer32"
_NsSetUrlFilterViaWebsense_Object = MibScalar
nsSetUrlFilterViaWebsense = _NsSetUrlFilterViaWebsense_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 1),
    _NsSetUrlFilterViaWebsense_Type()
)
nsSetUrlFilterViaWebsense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlFilterViaWebsense.setStatus("current")


class _NsSetUrlServerName_Type(DisplayString):
    """Custom type nsSetUrlServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsSetUrlServerName_Type.__name__ = "DisplayString"
_NsSetUrlServerName_Object = MibScalar
nsSetUrlServerName = _NsSetUrlServerName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 2),
    _NsSetUrlServerName_Type()
)
nsSetUrlServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlServerName.setStatus("current")
_NsSetUrlServerPort_Type = Integer32
_NsSetUrlServerPort_Object = MibScalar
nsSetUrlServerPort = _NsSetUrlServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 3),
    _NsSetUrlServerPort_Type()
)
nsSetUrlServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlServerPort.setStatus("current")


class _NsSetUrlCommTimeout_Type(Integer32):
    """Custom type nsSetUrlCommTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_NsSetUrlCommTimeout_Type.__name__ = "Integer32"
_NsSetUrlCommTimeout_Object = MibScalar
nsSetUrlCommTimeout = _NsSetUrlCommTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 4),
    _NsSetUrlCommTimeout_Type()
)
nsSetUrlCommTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlCommTimeout.setStatus("current")


class _NsSetUrlServerStatus_Type(Integer32):
    """Custom type nsSetUrlServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("not-applicable", 0),
          ("running", 1))
    )


_NsSetUrlServerStatus_Type.__name__ = "Integer32"
_NsSetUrlServerStatus_Object = MibScalar
nsSetUrlServerStatus = _NsSetUrlServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 5),
    _NsSetUrlServerStatus_Type()
)
nsSetUrlServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlServerStatus.setStatus("current")


class _NsSetUrlSerLostHdlWay_Type(Integer32):
    """Custom type nsSetUrlSerLostHdlWay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block-all", 0),
          ("permit-all", 1))
    )


_NsSetUrlSerLostHdlWay_Type.__name__ = "Integer32"
_NsSetUrlSerLostHdlWay_Object = MibScalar
nsSetUrlSerLostHdlWay = _NsSetUrlSerLostHdlWay_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 6),
    _NsSetUrlSerLostHdlWay_Type()
)
nsSetUrlSerLostHdlWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlSerLostHdlWay.setStatus("current")


class _NsSetUrlBlockMsgType_Type(Integer32):
    """Custom type nsSetUrlBlockMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("netscreen", 1),
          ("websense", 0))
    )


_NsSetUrlBlockMsgType_Type.__name__ = "Integer32"
_NsSetUrlBlockMsgType_Object = MibScalar
nsSetUrlBlockMsgType = _NsSetUrlBlockMsgType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 7),
    _NsSetUrlBlockMsgType_Type()
)
nsSetUrlBlockMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlBlockMsgType.setStatus("current")


class _NsSetUrlNsBlockMsg_Type(DisplayString):
    """Custom type nsSetUrlNsBlockMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 220),
    )


_NsSetUrlNsBlockMsg_Type.__name__ = "DisplayString"
_NsSetUrlNsBlockMsg_Object = MibScalar
nsSetUrlNsBlockMsg = _NsSetUrlNsBlockMsg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 7, 4, 8),
    _NsSetUrlNsBlockMsg_Type()
)
nsSetUrlNsBlockMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsSetUrlNsBlockMsg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-SET-URL-FILTER-MIB",
    **{"netscreenSetUrlFilterMibModule": netscreenSetUrlFilterMibModule,
       "nsSetURLFilter": nsSetURLFilter,
       "nsSetUrlFilterViaWebsense": nsSetUrlFilterViaWebsense,
       "nsSetUrlServerName": nsSetUrlServerName,
       "nsSetUrlServerPort": nsSetUrlServerPort,
       "nsSetUrlCommTimeout": nsSetUrlCommTimeout,
       "nsSetUrlServerStatus": nsSetUrlServerStatus,
       "nsSetUrlSerLostHdlWay": nsSetUrlSerLostHdlWay,
       "nsSetUrlBlockMsgType": nsSetUrlBlockMsgType,
       "nsSetUrlNsBlockMsg": nsSetUrlNsBlockMsg}
)
