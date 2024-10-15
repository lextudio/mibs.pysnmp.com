# SNMP MIB module (NETSCREEN-VPN-PHASETWO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-PHASETWO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:07 2024
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

(netscreenVpn,
 netscreenVpnMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn",
    "netscreenVpnMibModule")

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

netscreenVpnPhasetwoMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 6)
)
netscreenVpnPhasetwoMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnPhaseTwoCfg_ObjectIdentity = ObjectIdentity
nsVpnPhaseTwoCfg = _NsVpnPhaseTwoCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6)
)
_NsVpnPhTwoTable_Object = MibTable
nsVpnPhTwoTable = _NsVpnPhTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1)
)
if mibBuilder.loadTexts:
    nsVpnPhTwoTable.setStatus("current")
_NsVpnPhTwoEntry_Object = MibTableRow
nsVpnPhTwoEntry = _NsVpnPhTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1)
)
nsVpnPhTwoEntry.setIndexNames(
    (0, "NETSCREEN-VPN-PHASETWO-MIB", "nsVpnPhTwoIndex"),
)
if mibBuilder.loadTexts:
    nsVpnPhTwoEntry.setStatus("current")


class _NsVpnPhTwoIndex_Type(Integer32):
    """Custom type nsVpnPhTwoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnPhTwoIndex_Type.__name__ = "Integer32"
_NsVpnPhTwoIndex_Object = MibTableColumn
nsVpnPhTwoIndex = _NsVpnPhTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 1),
    _NsVpnPhTwoIndex_Type()
)
nsVpnPhTwoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoIndex.setStatus("current")


class _NsVpnPhTwoName_Type(DisplayString):
    """Custom type nsVpnPhTwoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnPhTwoName_Type.__name__ = "DisplayString"
_NsVpnPhTwoName_Object = MibTableColumn
nsVpnPhTwoName = _NsVpnPhTwoName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 2),
    _NsVpnPhTwoName_Type()
)
nsVpnPhTwoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoName.setStatus("current")
_NsVpnPhTwoPFS_Type = Integer32
_NsVpnPhTwoPFS_Object = MibTableColumn
nsVpnPhTwoPFS = _NsVpnPhTwoPFS_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 3),
    _NsVpnPhTwoPFS_Type()
)
nsVpnPhTwoPFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoPFS.setStatus("current")


class _NsVpnPhTwoEncapMethod_Type(Integer32):
    """Custom type nsVpnPhTwoEncapMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ah", 0),
          ("esp", 1))
    )


_NsVpnPhTwoEncapMethod_Type.__name__ = "Integer32"
_NsVpnPhTwoEncapMethod_Object = MibTableColumn
nsVpnPhTwoEncapMethod = _NsVpnPhTwoEncapMethod_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 4),
    _NsVpnPhTwoEncapMethod_Type()
)
nsVpnPhTwoEncapMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoEncapMethod.setStatus("current")


class _NsVpnPhTwoESPEncryp_Type(Integer32):
    """Custom type nsVpnPhTwoESPEncryp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("aes-192", 4),
          ("aes-256", 5),
          ("des", 1),
          ("null", 0),
          ("triple-des", 2))
    )


_NsVpnPhTwoESPEncryp_Type.__name__ = "Integer32"
_NsVpnPhTwoESPEncryp_Object = MibTableColumn
nsVpnPhTwoESPEncryp = _NsVpnPhTwoESPEncryp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 5),
    _NsVpnPhTwoESPEncryp_Type()
)
nsVpnPhTwoESPEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoESPEncryp.setStatus("current")


class _NsVpnPhTwoESPAuth_Type(Integer32):
    """Custom type nsVpnPhTwoESPAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("null", 0),
          ("sha", 2),
          ("sha-256", 3))
    )


_NsVpnPhTwoESPAuth_Type.__name__ = "Integer32"
_NsVpnPhTwoESPAuth_Object = MibTableColumn
nsVpnPhTwoESPAuth = _NsVpnPhTwoESPAuth_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 6),
    _NsVpnPhTwoESPAuth_Type()
)
nsVpnPhTwoESPAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoESPAuth.setStatus("current")


class _NsVpnPhTwoAhAuth_Type(Integer32):
    """Custom type nsVpnPhTwoAhAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("null", 0),
          ("sha", 2))
    )


_NsVpnPhTwoAhAuth_Type.__name__ = "Integer32"
_NsVpnPhTwoAhAuth_Object = MibTableColumn
nsVpnPhTwoAhAuth = _NsVpnPhTwoAhAuth_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 7),
    _NsVpnPhTwoAhAuth_Type()
)
nsVpnPhTwoAhAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoAhAuth.setStatus("current")
_NsVpnPhTwoLifetime_Type = Integer32
_NsVpnPhTwoLifetime_Object = MibTableColumn
nsVpnPhTwoLifetime = _NsVpnPhTwoLifetime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 8),
    _NsVpnPhTwoLifetime_Type()
)
nsVpnPhTwoLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoLifetime.setStatus("current")


class _NsVpnPhTwoLifetimeMeasure_Type(Integer32):
    """Custom type nsVpnPhTwoLifetimeMeasure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("days", 3),
          ("hours", 2),
          ("minute", 1),
          ("second", 0))
    )


_NsVpnPhTwoLifetimeMeasure_Type.__name__ = "Integer32"
_NsVpnPhTwoLifetimeMeasure_Object = MibTableColumn
nsVpnPhTwoLifetimeMeasure = _NsVpnPhTwoLifetimeMeasure_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 9),
    _NsVpnPhTwoLifetimeMeasure_Type()
)
nsVpnPhTwoLifetimeMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoLifetimeMeasure.setStatus("current")
_NsVpnPhTwoLifetimeKb_Type = Integer32
_NsVpnPhTwoLifetimeKb_Object = MibTableColumn
nsVpnPhTwoLifetimeKb = _NsVpnPhTwoLifetimeKb_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 10),
    _NsVpnPhTwoLifetimeKb_Type()
)
nsVpnPhTwoLifetimeKb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoLifetimeKb.setStatus("current")
_NsVpnPhTwoVsys_Type = Integer32
_NsVpnPhTwoVsys_Object = MibTableColumn
nsVpnPhTwoVsys = _NsVpnPhTwoVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 6, 1, 1, 11),
    _NsVpnPhTwoVsys_Type()
)
nsVpnPhTwoVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhTwoVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-PHASETWO-MIB",
    **{"netscreenVpnPhasetwoMibModule": netscreenVpnPhasetwoMibModule,
       "nsVpnPhaseTwoCfg": nsVpnPhaseTwoCfg,
       "nsVpnPhTwoTable": nsVpnPhTwoTable,
       "nsVpnPhTwoEntry": nsVpnPhTwoEntry,
       "nsVpnPhTwoIndex": nsVpnPhTwoIndex,
       "nsVpnPhTwoName": nsVpnPhTwoName,
       "nsVpnPhTwoPFS": nsVpnPhTwoPFS,
       "nsVpnPhTwoEncapMethod": nsVpnPhTwoEncapMethod,
       "nsVpnPhTwoESPEncryp": nsVpnPhTwoESPEncryp,
       "nsVpnPhTwoESPAuth": nsVpnPhTwoESPAuth,
       "nsVpnPhTwoAhAuth": nsVpnPhTwoAhAuth,
       "nsVpnPhTwoLifetime": nsVpnPhTwoLifetime,
       "nsVpnPhTwoLifetimeMeasure": nsVpnPhTwoLifetimeMeasure,
       "nsVpnPhTwoLifetimeKb": nsVpnPhTwoLifetimeKb,
       "nsVpnPhTwoVsys": nsVpnPhTwoVsys}
)
