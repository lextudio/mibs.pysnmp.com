# SNMP MIB module (NETSCREEN-VPN-PHASEONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-PHASEONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:06 2024
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

netscreenVpnPhaseoneMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 5)
)
netscreenVpnPhaseoneMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-13 00:00",
         "2001-09-28 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnPhaseOneCfg_ObjectIdentity = ObjectIdentity
nsVpnPhaseOneCfg = _NsVpnPhaseOneCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5)
)
_NsVpnPhOneTable_Object = MibTable
nsVpnPhOneTable = _NsVpnPhOneTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1)
)
if mibBuilder.loadTexts:
    nsVpnPhOneTable.setStatus("current")
_NsVpnPhOneEntry_Object = MibTableRow
nsVpnPhOneEntry = _NsVpnPhOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1)
)
nsVpnPhOneEntry.setIndexNames(
    (0, "NETSCREEN-VPN-PHASEONE-MIB", "nsVpnPhOneIndex"),
)
if mibBuilder.loadTexts:
    nsVpnPhOneEntry.setStatus("current")


class _NsVpnPhOneIndex_Type(Integer32):
    """Custom type nsVpnPhOneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnPhOneIndex_Type.__name__ = "Integer32"
_NsVpnPhOneIndex_Object = MibTableColumn
nsVpnPhOneIndex = _NsVpnPhOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 1),
    _NsVpnPhOneIndex_Type()
)
nsVpnPhOneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneIndex.setStatus("current")


class _NsVpnPhOneName_Type(DisplayString):
    """Custom type nsVpnPhOneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnPhOneName_Type.__name__ = "DisplayString"
_NsVpnPhOneName_Object = MibTableColumn
nsVpnPhOneName = _NsVpnPhOneName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 2),
    _NsVpnPhOneName_Type()
)
nsVpnPhOneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneName.setStatus("current")


class _NsVpnPhOneAuthMethod_Type(Integer32):
    """Custom type nsVpnPhOneAuthMethod based on Integer32"""
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
        *(("dsa-sig", 2),
          ("preshare", 0),
          ("rsa-enc", 3),
          ("rsa-rev", 4),
          ("rsa-sig", 1))
    )


_NsVpnPhOneAuthMethod_Type.__name__ = "Integer32"
_NsVpnPhOneAuthMethod_Object = MibTableColumn
nsVpnPhOneAuthMethod = _NsVpnPhOneAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 3),
    _NsVpnPhOneAuthMethod_Type()
)
nsVpnPhOneAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneAuthMethod.setStatus("current")
_NsVpnPhOneDhGroup_Type = Integer32
_NsVpnPhOneDhGroup_Object = MibTableColumn
nsVpnPhOneDhGroup = _NsVpnPhOneDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 4),
    _NsVpnPhOneDhGroup_Type()
)
nsVpnPhOneDhGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneDhGroup.setStatus("current")


class _NsVpnPhOneEncryp_Type(Integer32):
    """Custom type nsVpnPhOneEncryp based on Integer32"""
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
          ("des3", 2),
          ("null", 0))
    )


_NsVpnPhOneEncryp_Type.__name__ = "Integer32"
_NsVpnPhOneEncryp_Object = MibTableColumn
nsVpnPhOneEncryp = _NsVpnPhOneEncryp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 5),
    _NsVpnPhOneEncryp_Type()
)
nsVpnPhOneEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneEncryp.setStatus("current")


class _NsVpnPhOneHash_Type(Integer32):
    """Custom type nsVpnPhOneHash based on Integer32"""
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


_NsVpnPhOneHash_Type.__name__ = "Integer32"
_NsVpnPhOneHash_Object = MibTableColumn
nsVpnPhOneHash = _NsVpnPhOneHash_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 6),
    _NsVpnPhOneHash_Type()
)
nsVpnPhOneHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneHash.setStatus("current")
_NsVpnPhOneLifetime_Type = Integer32
_NsVpnPhOneLifetime_Object = MibTableColumn
nsVpnPhOneLifetime = _NsVpnPhOneLifetime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 7),
    _NsVpnPhOneLifetime_Type()
)
nsVpnPhOneLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneLifetime.setStatus("current")


class _NsVpnPhOneLifetimeMeasure_Type(Integer32):
    """Custom type nsVpnPhOneLifetimeMeasure based on Integer32"""
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


_NsVpnPhOneLifetimeMeasure_Type.__name__ = "Integer32"
_NsVpnPhOneLifetimeMeasure_Object = MibTableColumn
nsVpnPhOneLifetimeMeasure = _NsVpnPhOneLifetimeMeasure_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 8),
    _NsVpnPhOneLifetimeMeasure_Type()
)
nsVpnPhOneLifetimeMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneLifetimeMeasure.setStatus("current")
_NsVpnPhOneVsys_Type = Integer32
_NsVpnPhOneVsys_Object = MibTableColumn
nsVpnPhOneVsys = _NsVpnPhOneVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 9),
    _NsVpnPhOneVsys_Type()
)
nsVpnPhOneVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnPhOneVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-PHASEONE-MIB",
    **{"netscreenVpnPhaseoneMibModule": netscreenVpnPhaseoneMibModule,
       "nsVpnPhaseOneCfg": nsVpnPhaseOneCfg,
       "nsVpnPhOneTable": nsVpnPhOneTable,
       "nsVpnPhOneEntry": nsVpnPhOneEntry,
       "nsVpnPhOneIndex": nsVpnPhOneIndex,
       "nsVpnPhOneName": nsVpnPhOneName,
       "nsVpnPhOneAuthMethod": nsVpnPhOneAuthMethod,
       "nsVpnPhOneDhGroup": nsVpnPhOneDhGroup,
       "nsVpnPhOneEncryp": nsVpnPhOneEncryp,
       "nsVpnPhOneHash": nsVpnPhOneHash,
       "nsVpnPhOneLifetime": nsVpnPhOneLifetime,
       "nsVpnPhOneLifetimeMeasure": nsVpnPhOneLifetimeMeasure,
       "nsVpnPhOneVsys": nsVpnPhOneVsys}
)
