# SNMP MIB module (NETSCREEN-VPN-IKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-IKE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:03 2024
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

netscreenVpnIkeMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 3)
)
netscreenVpnIkeMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnIke_ObjectIdentity = ObjectIdentity
nsVpnIke = _NsVpnIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3)
)
_NsVpnIkeTable_Object = MibTable
nsVpnIkeTable = _NsVpnIkeTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1)
)
if mibBuilder.loadTexts:
    nsVpnIkeTable.setStatus("current")
_NsVpnIkeEntry_Object = MibTableRow
nsVpnIkeEntry = _NsVpnIkeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1)
)
nsVpnIkeEntry.setIndexNames(
    (0, "NETSCREEN-VPN-IKE-MIB", "nsVpnIkeIndex"),
)
if mibBuilder.loadTexts:
    nsVpnIkeEntry.setStatus("current")


class _NsVpnIkeIndex_Type(Integer32):
    """Custom type nsVpnIkeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnIkeIndex_Type.__name__ = "Integer32"
_NsVpnIkeIndex_Object = MibTableColumn
nsVpnIkeIndex = _NsVpnIkeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 1),
    _NsVpnIkeIndex_Type()
)
nsVpnIkeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkeIndex.setStatus("current")


class _NsVpnIkeName_Type(DisplayString):
    """Custom type nsVpnIkeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIkeName_Type.__name__ = "DisplayString"
_NsVpnIkeName_Object = MibTableColumn
nsVpnIkeName = _NsVpnIkeName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 2),
    _NsVpnIkeName_Type()
)
nsVpnIkeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkeName.setStatus("current")


class _NsVpnIkeReplayProc_Type(Integer32):
    """Custom type nsVpnIkeReplayProc based on Integer32"""
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


_NsVpnIkeReplayProc_Type.__name__ = "Integer32"
_NsVpnIkeReplayProc_Object = MibTableColumn
nsVpnIkeReplayProc = _NsVpnIkeReplayProc_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 3),
    _NsVpnIkeReplayProc_Type()
)
nsVpnIkeReplayProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkeReplayProc.setStatus("current")


class _NsVpnIkeGWTun_Type(DisplayString):
    """Custom type nsVpnIkeGWTun based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIkeGWTun_Type.__name__ = "DisplayString"
_NsVpnIkeGWTun_Object = MibTableColumn
nsVpnIkeGWTun = _NsVpnIkeGWTun_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 4),
    _NsVpnIkeGWTun_Type()
)
nsVpnIkeGWTun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkeGWTun.setStatus("current")


class _NsVpnIkePh2ProOne_Type(DisplayString):
    """Custom type nsVpnIkePh2ProOne based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIkePh2ProOne_Type.__name__ = "DisplayString"
_NsVpnIkePh2ProOne_Object = MibTableColumn
nsVpnIkePh2ProOne = _NsVpnIkePh2ProOne_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 5),
    _NsVpnIkePh2ProOne_Type()
)
nsVpnIkePh2ProOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkePh2ProOne.setStatus("current")


class _NsVpnIkePh2ProTwo_Type(DisplayString):
    """Custom type nsVpnIkePh2ProTwo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIkePh2ProTwo_Type.__name__ = "DisplayString"
_NsVpnIkePh2ProTwo_Object = MibTableColumn
nsVpnIkePh2ProTwo = _NsVpnIkePh2ProTwo_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 6),
    _NsVpnIkePh2ProTwo_Type()
)
nsVpnIkePh2ProTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkePh2ProTwo.setStatus("current")


class _NsVpnIkePh2ProThree_Type(DisplayString):
    """Custom type nsVpnIkePh2ProThree based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIkePh2ProThree_Type.__name__ = "DisplayString"
_NsVpnIkePh2ProThree_Object = MibTableColumn
nsVpnIkePh2ProThree = _NsVpnIkePh2ProThree_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 7),
    _NsVpnIkePh2ProThree_Type()
)
nsVpnIkePh2ProThree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkePh2ProThree.setStatus("current")


class _NsVpnIkePh2ProFour_Type(DisplayString):
    """Custom type nsVpnIkePh2ProFour based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnIkePh2ProFour_Type.__name__ = "DisplayString"
_NsVpnIkePh2ProFour_Object = MibTableColumn
nsVpnIkePh2ProFour = _NsVpnIkePh2ProFour_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 8),
    _NsVpnIkePh2ProFour_Type()
)
nsVpnIkePh2ProFour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkePh2ProFour.setStatus("current")


class _NsVpnIkeMonitorEnable_Type(Integer32):
    """Custom type nsVpnIkeMonitorEnable based on Integer32"""
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


_NsVpnIkeMonitorEnable_Type.__name__ = "Integer32"
_NsVpnIkeMonitorEnable_Object = MibTableColumn
nsVpnIkeMonitorEnable = _NsVpnIkeMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 9),
    _NsVpnIkeMonitorEnable_Type()
)
nsVpnIkeMonitorEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkeMonitorEnable.setStatus("current")


class _NsVpnIkeTransMode_Type(Integer32):
    """Custom type nsVpnIkeTransMode based on Integer32"""
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


_NsVpnIkeTransMode_Type.__name__ = "Integer32"
_NsVpnIkeTransMode_Object = MibTableColumn
nsVpnIkeTransMode = _NsVpnIkeTransMode_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 10),
    _NsVpnIkeTransMode_Type()
)
nsVpnIkeTransMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkeTransMode.setStatus("current")
_NsVpnIkeVsys_Type = Integer32
_NsVpnIkeVsys_Object = MibTableColumn
nsVpnIkeVsys = _NsVpnIkeVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 3, 1, 1, 11),
    _NsVpnIkeVsys_Type()
)
nsVpnIkeVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnIkeVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-IKE-MIB",
    **{"netscreenVpnIkeMibModule": netscreenVpnIkeMibModule,
       "nsVpnIke": nsVpnIke,
       "nsVpnIkeTable": nsVpnIkeTable,
       "nsVpnIkeEntry": nsVpnIkeEntry,
       "nsVpnIkeIndex": nsVpnIkeIndex,
       "nsVpnIkeName": nsVpnIkeName,
       "nsVpnIkeReplayProc": nsVpnIkeReplayProc,
       "nsVpnIkeGWTun": nsVpnIkeGWTun,
       "nsVpnIkePh2ProOne": nsVpnIkePh2ProOne,
       "nsVpnIkePh2ProTwo": nsVpnIkePh2ProTwo,
       "nsVpnIkePh2ProThree": nsVpnIkePh2ProThree,
       "nsVpnIkePh2ProFour": nsVpnIkePh2ProFour,
       "nsVpnIkeMonitorEnable": nsVpnIkeMonitorEnable,
       "nsVpnIkeTransMode": nsVpnIkeTransMode,
       "nsVpnIkeVsys": nsVpnIkeVsys}
)
