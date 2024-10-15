# SNMP MIB module (TPLINK-L2PROTOCOL-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-L2PROTOCOL-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:15 2024
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

tplinkL2protocolTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81)
)
tplinkL2protocolTunnelMIB.setRevisions(
        ("2009-08-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkL2protocolTunnelMIBObjects_ObjectIdentity = ObjectIdentity
tplinkL2protocolTunnelMIBObjects = _TplinkL2protocolTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1)
)
_TpL2ptGlobalCfg_ObjectIdentity = ObjectIdentity
tpL2ptGlobalCfg = _TpL2ptGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 1)
)


class _TpL2ptEnable_Type(Integer32):
    """Custom type tpL2ptEnable based on Integer32"""
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


_TpL2ptEnable_Type.__name__ = "Integer32"
_TpL2ptEnable_Object = MibScalar
tpL2ptEnable = _TpL2ptEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 1, 1),
    _TpL2ptEnable_Type()
)
tpL2ptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpL2ptEnable.setStatus("current")
_TpL2ptPortCfg_ObjectIdentity = ObjectIdentity
tpL2ptPortCfg = _TpL2ptPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2)
)
_TpL2ptPortTable_Object = MibTable
tpL2ptPortTable = _TpL2ptPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpL2ptPortTable.setStatus("current")
_TpL2ptPortEntry_Object = MibTableRow
tpL2ptPortEntry = _TpL2ptPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1)
)
tpL2ptPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpL2ptPortEntry.setStatus("current")


class _TpL2ptPort_Type(OctetString):
    """Custom type tpL2ptPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpL2ptPort_Type.__name__ = "OctetString"
_TpL2ptPort_Object = MibTableColumn
tpL2ptPort = _TpL2ptPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 1),
    _TpL2ptPort_Type()
)
tpL2ptPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpL2ptPort.setStatus("current")


class _TpL2ptType_Type(Integer32):
    """Custom type tpL2ptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("none", 0),
          ("uni", 1))
    )


_TpL2ptType_Type.__name__ = "Integer32"
_TpL2ptType_Object = MibTableColumn
tpL2ptType = _TpL2ptType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 2),
    _TpL2ptType_Type()
)
tpL2ptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpL2ptType.setStatus("current")


class _TpL2ptProtocol_Type(OctetString):
    """Custom type tpL2ptProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpL2ptProtocol_Type.__name__ = "OctetString"
_TpL2ptProtocol_Object = MibTableColumn
tpL2ptProtocol = _TpL2ptProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 3),
    _TpL2ptProtocol_Type()
)
tpL2ptProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpL2ptProtocol.setStatus("current")


class _TpL2ptThreshold_Type(OctetString):
    """Custom type tpL2ptThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpL2ptThreshold_Type.__name__ = "OctetString"
_TpL2ptThreshold_Object = MibTableColumn
tpL2ptThreshold = _TpL2ptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 4),
    _TpL2ptThreshold_Type()
)
tpL2ptThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpL2ptThreshold.setStatus("current")


class _TpL2ptLag_Type(OctetString):
    """Custom type tpL2ptLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpL2ptLag_Type.__name__ = "OctetString"
_TpL2ptLag_Object = MibTableColumn
tpL2ptLag = _TpL2ptLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 1, 2, 1, 1, 5),
    _TpL2ptLag_Type()
)
tpL2ptLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpL2ptLag.setStatus("current")
_TplinkL2protocolTunnelNotifications_ObjectIdentity = ObjectIdentity
tplinkL2protocolTunnelNotifications = _TplinkL2protocolTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 81, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-L2PROTOCOL-TUNNEL-MIB",
    **{"tplinkL2protocolTunnelMIB": tplinkL2protocolTunnelMIB,
       "tplinkL2protocolTunnelMIBObjects": tplinkL2protocolTunnelMIBObjects,
       "tpL2ptGlobalCfg": tpL2ptGlobalCfg,
       "tpL2ptEnable": tpL2ptEnable,
       "tpL2ptPortCfg": tpL2ptPortCfg,
       "tpL2ptPortTable": tpL2ptPortTable,
       "tpL2ptPortEntry": tpL2ptPortEntry,
       "tpL2ptPort": tpL2ptPort,
       "tpL2ptType": tpL2ptType,
       "tpL2ptProtocol": tpL2ptProtocol,
       "tpL2ptThreshold": tpL2ptThreshold,
       "tpL2ptLag": tpL2ptLag,
       "tplinkL2protocolTunnelNotifications": tplinkL2protocolTunnelNotifications}
)
