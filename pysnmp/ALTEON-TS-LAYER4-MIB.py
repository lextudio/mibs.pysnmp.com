# SNMP MIB module (ALTEON-TS-LAYER4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-TS-LAYER4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:00 2024
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

(switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "switch")

(information,
 operCmds,
 stats) = mibBuilder.importSymbols(
    "ALTEON-TIGON-SWITCH-MIB",
    "information",
    "operCmds",
    "stats")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Serverloadbalance_ObjectIdentity = ObjectIdentity
serverloadbalance = _Serverloadbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5)
)
_SlbRealServerMaxSize_Type = Integer32
_SlbRealServerMaxSize_Object = MibScalar
slbRealServerMaxSize = _SlbRealServerMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 1),
    _SlbRealServerMaxSize_Type()
)
slbRealServerMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerMaxSize.setStatus("mandatory")
_SlbCurCfgRealServerTable_Object = MibTable
slbCurCfgRealServerTable = _SlbCurCfgRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgRealServerTable.setStatus("mandatory")
_SlbCurCfgRealServerEntry_Object = MibTableRow
slbCurCfgRealServerEntry = _SlbCurCfgRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1)
)
slbCurCfgRealServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgRealServerEntry.setStatus("mandatory")
_SlbCurCfgRealServerIndex_Type = Integer32
_SlbCurCfgRealServerIndex_Object = MibTableColumn
slbCurCfgRealServerIndex = _SlbCurCfgRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 1),
    _SlbCurCfgRealServerIndex_Type()
)
slbCurCfgRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIndex.setStatus("mandatory")
_SlbCurCfgRealServerIpAddr_Type = IpAddress
_SlbCurCfgRealServerIpAddr_Object = MibTableColumn
slbCurCfgRealServerIpAddr = _SlbCurCfgRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 2),
    _SlbCurCfgRealServerIpAddr_Type()
)
slbCurCfgRealServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerIpAddr.setStatus("mandatory")


class _SlbCurCfgRealServerWeight_Type(Integer32):
    """Custom type slbCurCfgRealServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbCurCfgRealServerWeight_Type.__name__ = "Integer32"
_SlbCurCfgRealServerWeight_Object = MibTableColumn
slbCurCfgRealServerWeight = _SlbCurCfgRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 3),
    _SlbCurCfgRealServerWeight_Type()
)
slbCurCfgRealServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerWeight.setStatus("mandatory")


class _SlbCurCfgRealServerMaxConns_Type(Integer32):
    """Custom type slbCurCfgRealServerMaxConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_SlbCurCfgRealServerMaxConns_Type.__name__ = "Integer32"
_SlbCurCfgRealServerMaxConns_Object = MibTableColumn
slbCurCfgRealServerMaxConns = _SlbCurCfgRealServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 4),
    _SlbCurCfgRealServerMaxConns_Type()
)
slbCurCfgRealServerMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerMaxConns.setStatus("mandatory")


class _SlbCurCfgRealServerTimeOut_Type(Integer32):
    """Custom type slbCurCfgRealServerTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_SlbCurCfgRealServerTimeOut_Type.__name__ = "Integer32"
_SlbCurCfgRealServerTimeOut_Object = MibTableColumn
slbCurCfgRealServerTimeOut = _SlbCurCfgRealServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 5),
    _SlbCurCfgRealServerTimeOut_Type()
)
slbCurCfgRealServerTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerTimeOut.setStatus("mandatory")
_SlbCurCfgRealServerBackUp_Type = Integer32
_SlbCurCfgRealServerBackUp_Object = MibTableColumn
slbCurCfgRealServerBackUp = _SlbCurCfgRealServerBackUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 6),
    _SlbCurCfgRealServerBackUp_Type()
)
slbCurCfgRealServerBackUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerBackUp.setStatus("mandatory")


class _SlbCurCfgRealServerPingInterval_Type(Integer32):
    """Custom type slbCurCfgRealServerPingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SlbCurCfgRealServerPingInterval_Type.__name__ = "Integer32"
_SlbCurCfgRealServerPingInterval_Object = MibTableColumn
slbCurCfgRealServerPingInterval = _SlbCurCfgRealServerPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 7),
    _SlbCurCfgRealServerPingInterval_Type()
)
slbCurCfgRealServerPingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerPingInterval.setStatus("mandatory")


class _SlbCurCfgRealServerFailRetry_Type(Integer32):
    """Custom type slbCurCfgRealServerFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgRealServerFailRetry_Type.__name__ = "Integer32"
_SlbCurCfgRealServerFailRetry_Object = MibTableColumn
slbCurCfgRealServerFailRetry = _SlbCurCfgRealServerFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 8),
    _SlbCurCfgRealServerFailRetry_Type()
)
slbCurCfgRealServerFailRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerFailRetry.setStatus("mandatory")


class _SlbCurCfgRealServerSuccRetry_Type(Integer32):
    """Custom type slbCurCfgRealServerSuccRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgRealServerSuccRetry_Type.__name__ = "Integer32"
_SlbCurCfgRealServerSuccRetry_Object = MibTableColumn
slbCurCfgRealServerSuccRetry = _SlbCurCfgRealServerSuccRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 9),
    _SlbCurCfgRealServerSuccRetry_Type()
)
slbCurCfgRealServerSuccRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerSuccRetry.setStatus("mandatory")


class _SlbCurCfgRealServerState_Type(Integer32):
    """Custom type slbCurCfgRealServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbCurCfgRealServerState_Type.__name__ = "Integer32"
_SlbCurCfgRealServerState_Object = MibTableColumn
slbCurCfgRealServerState = _SlbCurCfgRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 10),
    _SlbCurCfgRealServerState_Type()
)
slbCurCfgRealServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerState.setStatus("mandatory")


class _SlbCurCfgRealServerType_Type(Integer32):
    """Custom type slbCurCfgRealServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-server", 1),
          ("remote-server", 2))
    )


_SlbCurCfgRealServerType_Type.__name__ = "Integer32"
_SlbCurCfgRealServerType_Object = MibTableColumn
slbCurCfgRealServerType = _SlbCurCfgRealServerType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 11),
    _SlbCurCfgRealServerType_Type()
)
slbCurCfgRealServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerType.setStatus("mandatory")


class _SlbCurCfgRealServerName_Type(DisplayString):
    """Custom type slbCurCfgRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbCurCfgRealServerName_Type.__name__ = "DisplayString"
_SlbCurCfgRealServerName_Object = MibTableColumn
slbCurCfgRealServerName = _SlbCurCfgRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 12),
    _SlbCurCfgRealServerName_Type()
)
slbCurCfgRealServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerName.setStatus("mandatory")
_SlbCurCfgRealServerUrlBmap_Type = OctetString
_SlbCurCfgRealServerUrlBmap_Object = MibTableColumn
slbCurCfgRealServerUrlBmap = _SlbCurCfgRealServerUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 13),
    _SlbCurCfgRealServerUrlBmap_Type()
)
slbCurCfgRealServerUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerUrlBmap.setStatus("mandatory")


class _SlbCurCfgRealServerCookie_Type(Integer32):
    """Custom type slbCurCfgRealServerCookie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgRealServerCookie_Type.__name__ = "Integer32"
_SlbCurCfgRealServerCookie_Object = MibTableColumn
slbCurCfgRealServerCookie = _SlbCurCfgRealServerCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 14),
    _SlbCurCfgRealServerCookie_Type()
)
slbCurCfgRealServerCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerCookie.setStatus("mandatory")


class _SlbCurCfgRealServerExcludeStr_Type(Integer32):
    """Custom type slbCurCfgRealServerExcludeStr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgRealServerExcludeStr_Type.__name__ = "Integer32"
_SlbCurCfgRealServerExcludeStr_Object = MibTableColumn
slbCurCfgRealServerExcludeStr = _SlbCurCfgRealServerExcludeStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 15),
    _SlbCurCfgRealServerExcludeStr_Type()
)
slbCurCfgRealServerExcludeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerExcludeStr.setStatus("mandatory")


class _SlbCurCfgRealServerSubmac_Type(Integer32):
    """Custom type slbCurCfgRealServerSubmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgRealServerSubmac_Type.__name__ = "Integer32"
_SlbCurCfgRealServerSubmac_Object = MibTableColumn
slbCurCfgRealServerSubmac = _SlbCurCfgRealServerSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 16),
    _SlbCurCfgRealServerSubmac_Type()
)
slbCurCfgRealServerSubmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerSubmac.setStatus("mandatory")


class _SlbCurCfgRealServerProxy_Type(Integer32):
    """Custom type slbCurCfgRealServerProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgRealServerProxy_Type.__name__ = "Integer32"
_SlbCurCfgRealServerProxy_Object = MibTableColumn
slbCurCfgRealServerProxy = _SlbCurCfgRealServerProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 2, 1, 17),
    _SlbCurCfgRealServerProxy_Type()
)
slbCurCfgRealServerProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServerProxy.setStatus("mandatory")
_SlbNewCfgRealServerTable_Object = MibTable
slbNewCfgRealServerTable = _SlbNewCfgRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgRealServerTable.setStatus("mandatory")
_SlbNewCfgRealServerEntry_Object = MibTableRow
slbNewCfgRealServerEntry = _SlbNewCfgRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1)
)
slbNewCfgRealServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgRealServerEntry.setStatus("mandatory")
_SlbNewCfgRealServerIndex_Type = Integer32
_SlbNewCfgRealServerIndex_Object = MibTableColumn
slbNewCfgRealServerIndex = _SlbNewCfgRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 1),
    _SlbNewCfgRealServerIndex_Type()
)
slbNewCfgRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIndex.setStatus("mandatory")
_SlbNewCfgRealServerIpAddr_Type = IpAddress
_SlbNewCfgRealServerIpAddr_Object = MibTableColumn
slbNewCfgRealServerIpAddr = _SlbNewCfgRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 2),
    _SlbNewCfgRealServerIpAddr_Type()
)
slbNewCfgRealServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerIpAddr.setStatus("mandatory")


class _SlbNewCfgRealServerWeight_Type(Integer32):
    """Custom type slbNewCfgRealServerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlbNewCfgRealServerWeight_Type.__name__ = "Integer32"
_SlbNewCfgRealServerWeight_Object = MibTableColumn
slbNewCfgRealServerWeight = _SlbNewCfgRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 3),
    _SlbNewCfgRealServerWeight_Type()
)
slbNewCfgRealServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerWeight.setStatus("mandatory")


class _SlbNewCfgRealServerMaxConns_Type(Integer32):
    """Custom type slbNewCfgRealServerMaxConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_SlbNewCfgRealServerMaxConns_Type.__name__ = "Integer32"
_SlbNewCfgRealServerMaxConns_Object = MibTableColumn
slbNewCfgRealServerMaxConns = _SlbNewCfgRealServerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 4),
    _SlbNewCfgRealServerMaxConns_Type()
)
slbNewCfgRealServerMaxConns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerMaxConns.setStatus("mandatory")


class _SlbNewCfgRealServerTimeOut_Type(Integer32):
    """Custom type slbNewCfgRealServerTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_SlbNewCfgRealServerTimeOut_Type.__name__ = "Integer32"
_SlbNewCfgRealServerTimeOut_Object = MibTableColumn
slbNewCfgRealServerTimeOut = _SlbNewCfgRealServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 5),
    _SlbNewCfgRealServerTimeOut_Type()
)
slbNewCfgRealServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerTimeOut.setStatus("mandatory")
_SlbNewCfgRealServerBackUp_Type = Integer32
_SlbNewCfgRealServerBackUp_Object = MibTableColumn
slbNewCfgRealServerBackUp = _SlbNewCfgRealServerBackUp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 6),
    _SlbNewCfgRealServerBackUp_Type()
)
slbNewCfgRealServerBackUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerBackUp.setStatus("mandatory")


class _SlbNewCfgRealServerPingInterval_Type(Integer32):
    """Custom type slbNewCfgRealServerPingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SlbNewCfgRealServerPingInterval_Type.__name__ = "Integer32"
_SlbNewCfgRealServerPingInterval_Object = MibTableColumn
slbNewCfgRealServerPingInterval = _SlbNewCfgRealServerPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 7),
    _SlbNewCfgRealServerPingInterval_Type()
)
slbNewCfgRealServerPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerPingInterval.setStatus("mandatory")


class _SlbNewCfgRealServerFailRetry_Type(Integer32):
    """Custom type slbNewCfgRealServerFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgRealServerFailRetry_Type.__name__ = "Integer32"
_SlbNewCfgRealServerFailRetry_Object = MibTableColumn
slbNewCfgRealServerFailRetry = _SlbNewCfgRealServerFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 8),
    _SlbNewCfgRealServerFailRetry_Type()
)
slbNewCfgRealServerFailRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerFailRetry.setStatus("mandatory")


class _SlbNewCfgRealServerSuccRetry_Type(Integer32):
    """Custom type slbNewCfgRealServerSuccRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgRealServerSuccRetry_Type.__name__ = "Integer32"
_SlbNewCfgRealServerSuccRetry_Object = MibTableColumn
slbNewCfgRealServerSuccRetry = _SlbNewCfgRealServerSuccRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 9),
    _SlbNewCfgRealServerSuccRetry_Type()
)
slbNewCfgRealServerSuccRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerSuccRetry.setStatus("mandatory")


class _SlbNewCfgRealServerState_Type(Integer32):
    """Custom type slbNewCfgRealServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbNewCfgRealServerState_Type.__name__ = "Integer32"
_SlbNewCfgRealServerState_Object = MibTableColumn
slbNewCfgRealServerState = _SlbNewCfgRealServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 10),
    _SlbNewCfgRealServerState_Type()
)
slbNewCfgRealServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerState.setStatus("mandatory")


class _SlbNewCfgRealServerDelete_Type(Integer32):
    """Custom type slbNewCfgRealServerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgRealServerDelete_Type.__name__ = "Integer32"
_SlbNewCfgRealServerDelete_Object = MibTableColumn
slbNewCfgRealServerDelete = _SlbNewCfgRealServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 11),
    _SlbNewCfgRealServerDelete_Type()
)
slbNewCfgRealServerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerDelete.setStatus("mandatory")


class _SlbNewCfgRealServerType_Type(Integer32):
    """Custom type slbNewCfgRealServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-server", 1),
          ("remote-server", 2))
    )


_SlbNewCfgRealServerType_Type.__name__ = "Integer32"
_SlbNewCfgRealServerType_Object = MibTableColumn
slbNewCfgRealServerType = _SlbNewCfgRealServerType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 12),
    _SlbNewCfgRealServerType_Type()
)
slbNewCfgRealServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerType.setStatus("mandatory")


class _SlbNewCfgRealServerName_Type(DisplayString):
    """Custom type slbNewCfgRealServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbNewCfgRealServerName_Type.__name__ = "DisplayString"
_SlbNewCfgRealServerName_Object = MibTableColumn
slbNewCfgRealServerName = _SlbNewCfgRealServerName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 13),
    _SlbNewCfgRealServerName_Type()
)
slbNewCfgRealServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerName.setStatus("mandatory")
_SlbNewCfgRealServerUrlBmap_Type = OctetString
_SlbNewCfgRealServerUrlBmap_Object = MibTableColumn
slbNewCfgRealServerUrlBmap = _SlbNewCfgRealServerUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 14),
    _SlbNewCfgRealServerUrlBmap_Type()
)
slbNewCfgRealServerUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServerUrlBmap.setStatus("mandatory")
_SlbNewCfgRealServerAddUrl_Type = Integer32
_SlbNewCfgRealServerAddUrl_Object = MibTableColumn
slbNewCfgRealServerAddUrl = _SlbNewCfgRealServerAddUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 15),
    _SlbNewCfgRealServerAddUrl_Type()
)
slbNewCfgRealServerAddUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerAddUrl.setStatus("mandatory")
_SlbNewCfgRealServerRemUrl_Type = Integer32
_SlbNewCfgRealServerRemUrl_Object = MibTableColumn
slbNewCfgRealServerRemUrl = _SlbNewCfgRealServerRemUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 16),
    _SlbNewCfgRealServerRemUrl_Type()
)
slbNewCfgRealServerRemUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerRemUrl.setStatus("mandatory")


class _SlbNewCfgRealServerCookie_Type(Integer32):
    """Custom type slbNewCfgRealServerCookie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgRealServerCookie_Type.__name__ = "Integer32"
_SlbNewCfgRealServerCookie_Object = MibTableColumn
slbNewCfgRealServerCookie = _SlbNewCfgRealServerCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 17),
    _SlbNewCfgRealServerCookie_Type()
)
slbNewCfgRealServerCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerCookie.setStatus("mandatory")


class _SlbNewCfgRealServerExcludeStr_Type(Integer32):
    """Custom type slbNewCfgRealServerExcludeStr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgRealServerExcludeStr_Type.__name__ = "Integer32"
_SlbNewCfgRealServerExcludeStr_Object = MibTableColumn
slbNewCfgRealServerExcludeStr = _SlbNewCfgRealServerExcludeStr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 18),
    _SlbNewCfgRealServerExcludeStr_Type()
)
slbNewCfgRealServerExcludeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerExcludeStr.setStatus("mandatory")


class _SlbNewCfgRealServerSubmac_Type(Integer32):
    """Custom type slbNewCfgRealServerSubmac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgRealServerSubmac_Type.__name__ = "Integer32"
_SlbNewCfgRealServerSubmac_Object = MibTableColumn
slbNewCfgRealServerSubmac = _SlbNewCfgRealServerSubmac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 19),
    _SlbNewCfgRealServerSubmac_Type()
)
slbNewCfgRealServerSubmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerSubmac.setStatus("mandatory")


class _SlbNewCfgRealServerProxy_Type(Integer32):
    """Custom type slbNewCfgRealServerProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgRealServerProxy_Type.__name__ = "Integer32"
_SlbNewCfgRealServerProxy_Object = MibTableColumn
slbNewCfgRealServerProxy = _SlbNewCfgRealServerProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 3, 1, 20),
    _SlbNewCfgRealServerProxy_Type()
)
slbNewCfgRealServerProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServerProxy.setStatus("mandatory")
_SlbVirtServerTableMaxSize_Type = Integer32
_SlbVirtServerTableMaxSize_Object = MibScalar
slbVirtServerTableMaxSize = _SlbVirtServerTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 4),
    _SlbVirtServerTableMaxSize_Type()
)
slbVirtServerTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServerTableMaxSize.setStatus("mandatory")
_SlbCurCfgVirtServerTable_Object = MibTable
slbCurCfgVirtServerTable = _SlbCurCfgVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServerTable.setStatus("mandatory")
_SlbCurCfgVirtualServerEntry_Object = MibTableRow
slbCurCfgVirtualServerEntry = _SlbCurCfgVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1)
)
slbCurCfgVirtualServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgVirtServerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgVirtualServerEntry.setStatus("mandatory")
_SlbCurCfgVirtServerIndex_Type = Integer32
_SlbCurCfgVirtServerIndex_Object = MibTableColumn
slbCurCfgVirtServerIndex = _SlbCurCfgVirtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 1),
    _SlbCurCfgVirtServerIndex_Type()
)
slbCurCfgVirtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIndex.setStatus("mandatory")
_SlbCurCfgVirtServerIpAddress_Type = IpAddress
_SlbCurCfgVirtServerIpAddress_Object = MibTableColumn
slbCurCfgVirtServerIpAddress = _SlbCurCfgVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 2),
    _SlbCurCfgVirtServerIpAddress_Type()
)
slbCurCfgVirtServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerIpAddress.setStatus("mandatory")


class _SlbCurCfgVirtServerLayer3Only_Type(Integer32):
    """Custom type slbCurCfgVirtServerLayer3Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("layer3Only", 1))
    )


_SlbCurCfgVirtServerLayer3Only_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerLayer3Only_Object = MibTableColumn
slbCurCfgVirtServerLayer3Only = _SlbCurCfgVirtServerLayer3Only_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 3),
    _SlbCurCfgVirtServerLayer3Only_Type()
)
slbCurCfgVirtServerLayer3Only.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerLayer3Only.setStatus("mandatory")


class _SlbCurCfgVirtServerState_Type(Integer32):
    """Custom type slbCurCfgVirtServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbCurCfgVirtServerState_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerState_Object = MibTableColumn
slbCurCfgVirtServerState = _SlbCurCfgVirtServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 4),
    _SlbCurCfgVirtServerState_Type()
)
slbCurCfgVirtServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerState.setStatus("mandatory")


class _SlbCurCfgVirtServerDname_Type(DisplayString):
    """Custom type slbCurCfgVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbCurCfgVirtServerDname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerDname_Object = MibTableColumn
slbCurCfgVirtServerDname = _SlbCurCfgVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 5),
    _SlbCurCfgVirtServerDname_Type()
)
slbCurCfgVirtServerDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerDname.setStatus("mandatory")


class _SlbCurCfgVirtServerCname_Type(DisplayString):
    """Custom type slbCurCfgVirtServerCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbCurCfgVirtServerCname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerCname_Object = MibTableColumn
slbCurCfgVirtServerCname = _SlbCurCfgVirtServerCname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 6),
    _SlbCurCfgVirtServerCname_Type()
)
slbCurCfgVirtServerCname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerCname.setStatus("mandatory")


class _SlbCurCfgVirtServerCoffset_Type(Integer32):
    """Custom type slbCurCfgVirtServerCoffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SlbCurCfgVirtServerCoffset_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerCoffset_Object = MibTableColumn
slbCurCfgVirtServerCoffset = _SlbCurCfgVirtServerCoffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 7),
    _SlbCurCfgVirtServerCoffset_Type()
)
slbCurCfgVirtServerCoffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerCoffset.setStatus("mandatory")


class _SlbCurCfgVirtServerClength_Type(Integer32):
    """Custom type slbCurCfgVirtServerClength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SlbCurCfgVirtServerClength_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerClength_Object = MibTableColumn
slbCurCfgVirtServerClength = _SlbCurCfgVirtServerClength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 8),
    _SlbCurCfgVirtServerClength_Type()
)
slbCurCfgVirtServerClength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerClength.setStatus("mandatory")


class _SlbCurCfgVirtServerUriCookie_Type(Integer32):
    """Custom type slbCurCfgVirtServerUriCookie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtServerUriCookie_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerUriCookie_Object = MibTableColumn
slbCurCfgVirtServerUriCookie = _SlbCurCfgVirtServerUriCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 9),
    _SlbCurCfgVirtServerUriCookie_Type()
)
slbCurCfgVirtServerUriCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerUriCookie.setStatus("mandatory")


class _SlbCurCfgVirtServerFtpParsing_Type(Integer32):
    """Custom type slbCurCfgVirtServerFtpParsing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtServerFtpParsing_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerFtpParsing_Object = MibTableColumn
slbCurCfgVirtServerFtpParsing = _SlbCurCfgVirtServerFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 10),
    _SlbCurCfgVirtServerFtpParsing_Type()
)
slbCurCfgVirtServerFtpParsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerFtpParsing.setStatus("obsolete")


class _SlbCurCfgVirtServerUrlHashLen_Type(Integer32):
    """Custom type slbCurCfgVirtServerUrlHashLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbCurCfgVirtServerUrlHashLen_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerUrlHashLen_Object = MibTableColumn
slbCurCfgVirtServerUrlHashLen = _SlbCurCfgVirtServerUrlHashLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 11),
    _SlbCurCfgVirtServerUrlHashLen_Type()
)
slbCurCfgVirtServerUrlHashLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerUrlHashLen.setStatus("mandatory")


class _SlbCurCfgVirtServerHttpHdrName_Type(DisplayString):
    """Custom type slbCurCfgVirtServerHttpHdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgVirtServerHttpHdrName_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerHttpHdrName_Object = MibTableColumn
slbCurCfgVirtServerHttpHdrName = _SlbCurCfgVirtServerHttpHdrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 12),
    _SlbCurCfgVirtServerHttpHdrName_Type()
)
slbCurCfgVirtServerHttpHdrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerHttpHdrName.setStatus("mandatory")
_SlbCurCfgVirtServerBwmContract_Type = Integer32
_SlbCurCfgVirtServerBwmContract_Object = MibTableColumn
slbCurCfgVirtServerBwmContract = _SlbCurCfgVirtServerBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 13),
    _SlbCurCfgVirtServerBwmContract_Type()
)
slbCurCfgVirtServerBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerBwmContract.setStatus("mandatory")


class _SlbCurCfgVirtServerResponseCount_Type(Integer32):
    """Custom type slbCurCfgVirtServerResponseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SlbCurCfgVirtServerResponseCount_Type.__name__ = "Integer32"
_SlbCurCfgVirtServerResponseCount_Object = MibTableColumn
slbCurCfgVirtServerResponseCount = _SlbCurCfgVirtServerResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 14),
    _SlbCurCfgVirtServerResponseCount_Type()
)
slbCurCfgVirtServerResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerResponseCount.setStatus("mandatory")


class _SlbCurCfgVirtServerCExpire_Type(DisplayString):
    """Custom type slbCurCfgVirtServerCExpire based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbCurCfgVirtServerCExpire_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServerCExpire_Object = MibTableColumn
slbCurCfgVirtServerCExpire = _SlbCurCfgVirtServerCExpire_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 5, 1, 15),
    _SlbCurCfgVirtServerCExpire_Type()
)
slbCurCfgVirtServerCExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServerCExpire.setStatus("mandatory")
_SlbNewCfgVirtServerTable_Object = MibTable
slbNewCfgVirtServerTable = _SlbNewCfgVirtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServerTable.setStatus("mandatory")
_SlbNewCfgVirtualServerEntry_Object = MibTableRow
slbNewCfgVirtualServerEntry = _SlbNewCfgVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1)
)
slbNewCfgVirtualServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgVirtServerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgVirtualServerEntry.setStatus("mandatory")
_SlbNewCfgVirtServerIndex_Type = Integer32
_SlbNewCfgVirtServerIndex_Object = MibTableColumn
slbNewCfgVirtServerIndex = _SlbNewCfgVirtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 1),
    _SlbNewCfgVirtServerIndex_Type()
)
slbNewCfgVirtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIndex.setStatus("mandatory")
_SlbNewCfgVirtServerIpAddress_Type = IpAddress
_SlbNewCfgVirtServerIpAddress_Object = MibTableColumn
slbNewCfgVirtServerIpAddress = _SlbNewCfgVirtServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 2),
    _SlbNewCfgVirtServerIpAddress_Type()
)
slbNewCfgVirtServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerIpAddress.setStatus("mandatory")


class _SlbNewCfgVirtServerLayer3Only_Type(Integer32):
    """Custom type slbNewCfgVirtServerLayer3Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("layer3Only", 1))
    )


_SlbNewCfgVirtServerLayer3Only_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerLayer3Only_Object = MibTableColumn
slbNewCfgVirtServerLayer3Only = _SlbNewCfgVirtServerLayer3Only_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 3),
    _SlbNewCfgVirtServerLayer3Only_Type()
)
slbNewCfgVirtServerLayer3Only.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerLayer3Only.setStatus("mandatory")


class _SlbNewCfgVirtServerState_Type(Integer32):
    """Custom type slbNewCfgVirtServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbNewCfgVirtServerState_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerState_Object = MibTableColumn
slbNewCfgVirtServerState = _SlbNewCfgVirtServerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 4),
    _SlbNewCfgVirtServerState_Type()
)
slbNewCfgVirtServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerState.setStatus("mandatory")


class _SlbNewCfgVirtServerDelete_Type(Integer32):
    """Custom type slbNewCfgVirtServerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgVirtServerDelete_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerDelete_Object = MibTableColumn
slbNewCfgVirtServerDelete = _SlbNewCfgVirtServerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 5),
    _SlbNewCfgVirtServerDelete_Type()
)
slbNewCfgVirtServerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerDelete.setStatus("mandatory")


class _SlbNewCfgVirtServerDname_Type(DisplayString):
    """Custom type slbNewCfgVirtServerDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_SlbNewCfgVirtServerDname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerDname_Object = MibTableColumn
slbNewCfgVirtServerDname = _SlbNewCfgVirtServerDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 6),
    _SlbNewCfgVirtServerDname_Type()
)
slbNewCfgVirtServerDname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerDname.setStatus("mandatory")


class _SlbNewCfgVirtServerCname_Type(DisplayString):
    """Custom type slbNewCfgVirtServerCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbNewCfgVirtServerCname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerCname_Object = MibTableColumn
slbNewCfgVirtServerCname = _SlbNewCfgVirtServerCname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 7),
    _SlbNewCfgVirtServerCname_Type()
)
slbNewCfgVirtServerCname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerCname.setStatus("mandatory")


class _SlbNewCfgVirtServerCoffset_Type(Integer32):
    """Custom type slbNewCfgVirtServerCoffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SlbNewCfgVirtServerCoffset_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerCoffset_Object = MibTableColumn
slbNewCfgVirtServerCoffset = _SlbNewCfgVirtServerCoffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 8),
    _SlbNewCfgVirtServerCoffset_Type()
)
slbNewCfgVirtServerCoffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerCoffset.setStatus("mandatory")


class _SlbNewCfgVirtServerClength_Type(Integer32):
    """Custom type slbNewCfgVirtServerClength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SlbNewCfgVirtServerClength_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerClength_Object = MibTableColumn
slbNewCfgVirtServerClength = _SlbNewCfgVirtServerClength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 9),
    _SlbNewCfgVirtServerClength_Type()
)
slbNewCfgVirtServerClength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerClength.setStatus("mandatory")


class _SlbNewCfgVirtServerUriCookie_Type(Integer32):
    """Custom type slbNewCfgVirtServerUriCookie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtServerUriCookie_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerUriCookie_Object = MibTableColumn
slbNewCfgVirtServerUriCookie = _SlbNewCfgVirtServerUriCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 10),
    _SlbNewCfgVirtServerUriCookie_Type()
)
slbNewCfgVirtServerUriCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerUriCookie.setStatus("mandatory")


class _SlbNewCfgVirtServerFtpParsing_Type(Integer32):
    """Custom type slbNewCfgVirtServerFtpParsing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtServerFtpParsing_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerFtpParsing_Object = MibTableColumn
slbNewCfgVirtServerFtpParsing = _SlbNewCfgVirtServerFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 11),
    _SlbNewCfgVirtServerFtpParsing_Type()
)
slbNewCfgVirtServerFtpParsing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerFtpParsing.setStatus("obsolete")


class _SlbNewCfgVirtServerUrlHashLen_Type(Integer32):
    """Custom type slbNewCfgVirtServerUrlHashLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbNewCfgVirtServerUrlHashLen_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerUrlHashLen_Object = MibTableColumn
slbNewCfgVirtServerUrlHashLen = _SlbNewCfgVirtServerUrlHashLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 12),
    _SlbNewCfgVirtServerUrlHashLen_Type()
)
slbNewCfgVirtServerUrlHashLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerUrlHashLen.setStatus("mandatory")


class _SlbNewCfgVirtServerHttpHdrName_Type(DisplayString):
    """Custom type slbNewCfgVirtServerHttpHdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgVirtServerHttpHdrName_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerHttpHdrName_Object = MibTableColumn
slbNewCfgVirtServerHttpHdrName = _SlbNewCfgVirtServerHttpHdrName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 13),
    _SlbNewCfgVirtServerHttpHdrName_Type()
)
slbNewCfgVirtServerHttpHdrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerHttpHdrName.setStatus("mandatory")
_SlbNewCfgVirtServerBwmContract_Type = Integer32
_SlbNewCfgVirtServerBwmContract_Object = MibTableColumn
slbNewCfgVirtServerBwmContract = _SlbNewCfgVirtServerBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 14),
    _SlbNewCfgVirtServerBwmContract_Type()
)
slbNewCfgVirtServerBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerBwmContract.setStatus("mandatory")


class _SlbNewCfgVirtServerResponseCount_Type(Integer32):
    """Custom type slbNewCfgVirtServerResponseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SlbNewCfgVirtServerResponseCount_Type.__name__ = "Integer32"
_SlbNewCfgVirtServerResponseCount_Object = MibTableColumn
slbNewCfgVirtServerResponseCount = _SlbNewCfgVirtServerResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 15),
    _SlbNewCfgVirtServerResponseCount_Type()
)
slbNewCfgVirtServerResponseCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerResponseCount.setStatus("mandatory")


class _SlbNewCfgVirtServerCExpire_Type(DisplayString):
    """Custom type slbNewCfgVirtServerCExpire based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbNewCfgVirtServerCExpire_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServerCExpire_Object = MibTableColumn
slbNewCfgVirtServerCExpire = _SlbNewCfgVirtServerCExpire_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 6, 1, 16),
    _SlbNewCfgVirtServerCExpire_Type()
)
slbNewCfgVirtServerCExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServerCExpire.setStatus("mandatory")
_SlbCurCfgVirtServicesTable_Object = MibTable
slbCurCfgVirtServicesTable = _SlbCurCfgVirtServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServicesTable.setStatus("mandatory")
_SlbCurCfgVirtServicesEntry_Object = MibTableRow
slbCurCfgVirtServicesEntry = _SlbCurCfgVirtServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1)
)
slbCurCfgVirtServicesEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgVirtServIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgVirtServiceIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgVirtServicesEntry.setStatus("mandatory")
_SlbCurCfgVirtServIndex_Type = Integer32
_SlbCurCfgVirtServIndex_Object = MibTableColumn
slbCurCfgVirtServIndex = _SlbCurCfgVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 1),
    _SlbCurCfgVirtServIndex_Type()
)
slbCurCfgVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServIndex.setStatus("mandatory")
_SlbCurCfgVirtServiceIndex_Type = Integer32
_SlbCurCfgVirtServiceIndex_Object = MibTableColumn
slbCurCfgVirtServiceIndex = _SlbCurCfgVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 2),
    _SlbCurCfgVirtServiceIndex_Type()
)
slbCurCfgVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceIndex.setStatus("mandatory")


class _SlbCurCfgVirtServiceVirtPort_Type(Integer32):
    """Custom type slbCurCfgVirtServiceVirtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbCurCfgVirtServiceVirtPort_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceVirtPort_Object = MibTableColumn
slbCurCfgVirtServiceVirtPort = _SlbCurCfgVirtServiceVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 3),
    _SlbCurCfgVirtServiceVirtPort_Type()
)
slbCurCfgVirtServiceVirtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceVirtPort.setStatus("mandatory")
_SlbCurCfgVirtServiceRealGroup_Type = Integer32
_SlbCurCfgVirtServiceRealGroup_Object = MibTableColumn
slbCurCfgVirtServiceRealGroup = _SlbCurCfgVirtServiceRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 4),
    _SlbCurCfgVirtServiceRealGroup_Type()
)
slbCurCfgVirtServiceRealGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRealGroup.setStatus("mandatory")


class _SlbCurCfgVirtServiceRealPort_Type(Integer32):
    """Custom type slbCurCfgVirtServiceRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgVirtServiceRealPort_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceRealPort_Object = MibTableColumn
slbCurCfgVirtServiceRealPort = _SlbCurCfgVirtServiceRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 5),
    _SlbCurCfgVirtServiceRealPort_Type()
)
slbCurCfgVirtServiceRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRealPort.setStatus("mandatory")


class _SlbCurCfgVirtServiceUDPBalance_Type(Integer32):
    """Custom type slbCurCfgVirtServiceUDPBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("stateless", 4))
    )


_SlbCurCfgVirtServiceUDPBalance_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceUDPBalance_Object = MibTableColumn
slbCurCfgVirtServiceUDPBalance = _SlbCurCfgVirtServiceUDPBalance_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 6),
    _SlbCurCfgVirtServiceUDPBalance_Type()
)
slbCurCfgVirtServiceUDPBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceUDPBalance.setStatus("mandatory")


class _SlbCurCfgVirtServicePBind_Type(Integer32):
    """Custom type slbCurCfgVirtServicePBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cookie", 5),
          ("disabled", 3),
          ("enabled", 2),
          ("sessid", 4))
    )


_SlbCurCfgVirtServicePBind_Type.__name__ = "Integer32"
_SlbCurCfgVirtServicePBind_Object = MibTableColumn
slbCurCfgVirtServicePBind = _SlbCurCfgVirtServicePBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 7),
    _SlbCurCfgVirtServicePBind_Type()
)
slbCurCfgVirtServicePBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServicePBind.setStatus("mandatory")


class _SlbCurCfgVirtServiceHname_Type(DisplayString):
    """Custom type slbCurCfgVirtServiceHname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SlbCurCfgVirtServiceHname_Type.__name__ = "DisplayString"
_SlbCurCfgVirtServiceHname_Object = MibTableColumn
slbCurCfgVirtServiceHname = _SlbCurCfgVirtServiceHname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 8),
    _SlbCurCfgVirtServiceHname_Type()
)
slbCurCfgVirtServiceHname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHname.setStatus("mandatory")


class _SlbCurCfgVirtServiceHttpSlb_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpSlb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("browser", 6),
          ("cookie", 4),
          ("disabled", 1),
          ("headerhash", 8),
          ("host", 5),
          ("others", 7),
          ("urlhash", 3),
          ("urlslb", 2))
    )


_SlbCurCfgVirtServiceHttpSlb_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpSlb_Object = MibTableColumn
slbCurCfgVirtServiceHttpSlb = _SlbCurCfgVirtServiceHttpSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 9),
    _SlbCurCfgVirtServiceHttpSlb_Type()
)
slbCurCfgVirtServiceHttpSlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpSlb.setStatus("mandatory")
_SlbCurCfgVirtServiceBwmContract_Type = Integer32
_SlbCurCfgVirtServiceBwmContract_Object = MibTableColumn
slbCurCfgVirtServiceBwmContract = _SlbCurCfgVirtServiceBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 10),
    _SlbCurCfgVirtServiceBwmContract_Type()
)
slbCurCfgVirtServiceBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceBwmContract.setStatus("mandatory")


class _SlbCurCfgVirtServiceDirServerRtn_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDirServerRtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtServiceDirServerRtn_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDirServerRtn_Object = MibTableColumn
slbCurCfgVirtServiceDirServerRtn = _SlbCurCfgVirtServiceDirServerRtn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 11),
    _SlbCurCfgVirtServiceDirServerRtn_Type()
)
slbCurCfgVirtServiceDirServerRtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDirServerRtn.setStatus("mandatory")


class _SlbCurCfgVirtServiceRtspUrlParse_Type(Integer32):
    """Custom type slbCurCfgVirtServiceRtspUrlParse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("hash", 3),
          ("patternMatch", 4))
    )


_SlbCurCfgVirtServiceRtspUrlParse_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceRtspUrlParse_Object = MibTableColumn
slbCurCfgVirtServiceRtspUrlParse = _SlbCurCfgVirtServiceRtspUrlParse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 12),
    _SlbCurCfgVirtServiceRtspUrlParse_Type()
)
slbCurCfgVirtServiceRtspUrlParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRtspUrlParse.setStatus("mandatory")


class _SlbCurCfgVirtServiceCookieMode_Type(Integer32):
    """Custom type slbCurCfgVirtServiceCookieMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("insert", 3),
          ("passive", 2),
          ("rewrite", 1))
    )


_SlbCurCfgVirtServiceCookieMode_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceCookieMode_Object = MibTableColumn
slbCurCfgVirtServiceCookieMode = _SlbCurCfgVirtServiceCookieMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 13),
    _SlbCurCfgVirtServiceCookieMode_Type()
)
slbCurCfgVirtServiceCookieMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceCookieMode.setStatus("mandatory")


class _SlbCurCfgVirtServiceDBind_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtServiceDBind_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDBind_Object = MibTableColumn
slbCurCfgVirtServiceDBind = _SlbCurCfgVirtServiceDBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 14),
    _SlbCurCfgVirtServiceDBind_Type()
)
slbCurCfgVirtServiceDBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDBind.setStatus("mandatory")


class _SlbCurCfgVirtServiceFtpParsing_Type(Integer32):
    """Custom type slbCurCfgVirtServiceFtpParsing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtServiceFtpParsing_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceFtpParsing_Object = MibTableColumn
slbCurCfgVirtServiceFtpParsing = _SlbCurCfgVirtServiceFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 15),
    _SlbCurCfgVirtServiceFtpParsing_Type()
)
slbCurCfgVirtServiceFtpParsing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceFtpParsing.setStatus("mandatory")


class _SlbCurCfgVirtServiceHttpSlbOption_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpSlbOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("none", 3),
          ("or", 2))
    )


_SlbCurCfgVirtServiceHttpSlbOption_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpSlbOption_Object = MibTableColumn
slbCurCfgVirtServiceHttpSlbOption = _SlbCurCfgVirtServiceHttpSlbOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 16),
    _SlbCurCfgVirtServiceHttpSlbOption_Type()
)
slbCurCfgVirtServiceHttpSlbOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpSlbOption.setStatus("mandatory")


class _SlbCurCfgVirtServiceHttpSlb2_Type(Integer32):
    """Custom type slbCurCfgVirtServiceHttpSlb2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("browser", 6),
          ("cookie", 4),
          ("disabled", 1),
          ("headerhash", 8),
          ("host", 5),
          ("others", 7),
          ("urlhash", 3),
          ("urlslb", 2))
    )


_SlbCurCfgVirtServiceHttpSlb2_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceHttpSlb2_Object = MibTableColumn
slbCurCfgVirtServiceHttpSlb2 = _SlbCurCfgVirtServiceHttpSlb2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 17),
    _SlbCurCfgVirtServiceHttpSlb2_Type()
)
slbCurCfgVirtServiceHttpSlb2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceHttpSlb2.setStatus("mandatory")


class _SlbCurCfgVirtServiceRemapUDPFrags_Type(Integer32):
    """Custom type slbCurCfgVirtServiceRemapUDPFrags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtServiceRemapUDPFrags_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceRemapUDPFrags_Object = MibTableColumn
slbCurCfgVirtServiceRemapUDPFrags = _SlbCurCfgVirtServiceRemapUDPFrags_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 18),
    _SlbCurCfgVirtServiceRemapUDPFrags_Type()
)
slbCurCfgVirtServiceRemapUDPFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceRemapUDPFrags.setStatus("mandatory")


class _SlbCurCfgVirtServiceDnsSlb_Type(Integer32):
    """Custom type slbCurCfgVirtServiceDnsSlb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtServiceDnsSlb_Type.__name__ = "Integer32"
_SlbCurCfgVirtServiceDnsSlb_Object = MibTableColumn
slbCurCfgVirtServiceDnsSlb = _SlbCurCfgVirtServiceDnsSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 7, 1, 19),
    _SlbCurCfgVirtServiceDnsSlb_Type()
)
slbCurCfgVirtServiceDnsSlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtServiceDnsSlb.setStatus("mandatory")
_SlbNewCfgVirtServicesTable_Object = MibTable
slbNewCfgVirtServicesTable = _SlbNewCfgVirtServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServicesTable.setStatus("mandatory")
_SlbNewCfgVirtServicesEntry_Object = MibTableRow
slbNewCfgVirtServicesEntry = _SlbNewCfgVirtServicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1)
)
slbNewCfgVirtServicesEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgVirtServIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgVirtServiceIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgVirtServicesEntry.setStatus("mandatory")
_SlbNewCfgVirtServIndex_Type = Integer32
_SlbNewCfgVirtServIndex_Object = MibTableColumn
slbNewCfgVirtServIndex = _SlbNewCfgVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 1),
    _SlbNewCfgVirtServIndex_Type()
)
slbNewCfgVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServIndex.setStatus("mandatory")
_SlbNewCfgVirtServiceIndex_Type = Integer32
_SlbNewCfgVirtServiceIndex_Object = MibTableColumn
slbNewCfgVirtServiceIndex = _SlbNewCfgVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 2),
    _SlbNewCfgVirtServiceIndex_Type()
)
slbNewCfgVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceIndex.setStatus("mandatory")


class _SlbNewCfgVirtServiceVirtPort_Type(Integer32):
    """Custom type slbNewCfgVirtServiceVirtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbNewCfgVirtServiceVirtPort_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceVirtPort_Object = MibTableColumn
slbNewCfgVirtServiceVirtPort = _SlbNewCfgVirtServiceVirtPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 3),
    _SlbNewCfgVirtServiceVirtPort_Type()
)
slbNewCfgVirtServiceVirtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceVirtPort.setStatus("mandatory")
_SlbNewCfgVirtServiceRealGroup_Type = Integer32
_SlbNewCfgVirtServiceRealGroup_Object = MibTableColumn
slbNewCfgVirtServiceRealGroup = _SlbNewCfgVirtServiceRealGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 4),
    _SlbNewCfgVirtServiceRealGroup_Type()
)
slbNewCfgVirtServiceRealGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRealGroup.setStatus("mandatory")


class _SlbNewCfgVirtServiceRealPort_Type(Integer32):
    """Custom type slbNewCfgVirtServiceRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgVirtServiceRealPort_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceRealPort_Object = MibTableColumn
slbNewCfgVirtServiceRealPort = _SlbNewCfgVirtServiceRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 5),
    _SlbNewCfgVirtServiceRealPort_Type()
)
slbNewCfgVirtServiceRealPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRealPort.setStatus("mandatory")


class _SlbNewCfgVirtServiceUDPBalance_Type(Integer32):
    """Custom type slbNewCfgVirtServiceUDPBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("stateless", 4))
    )


_SlbNewCfgVirtServiceUDPBalance_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceUDPBalance_Object = MibTableColumn
slbNewCfgVirtServiceUDPBalance = _SlbNewCfgVirtServiceUDPBalance_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 6),
    _SlbNewCfgVirtServiceUDPBalance_Type()
)
slbNewCfgVirtServiceUDPBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceUDPBalance.setStatus("mandatory")


class _SlbNewCfgVirtServicePBind_Type(Integer32):
    """Custom type slbNewCfgVirtServicePBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cookie", 5),
          ("disabled", 3),
          ("enabled", 2),
          ("sessid", 4))
    )


_SlbNewCfgVirtServicePBind_Type.__name__ = "Integer32"
_SlbNewCfgVirtServicePBind_Object = MibTableColumn
slbNewCfgVirtServicePBind = _SlbNewCfgVirtServicePBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 7),
    _SlbNewCfgVirtServicePBind_Type()
)
slbNewCfgVirtServicePBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServicePBind.setStatus("mandatory")


class _SlbNewCfgVirtServiceHname_Type(DisplayString):
    """Custom type slbNewCfgVirtServiceHname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SlbNewCfgVirtServiceHname_Type.__name__ = "DisplayString"
_SlbNewCfgVirtServiceHname_Object = MibTableColumn
slbNewCfgVirtServiceHname = _SlbNewCfgVirtServiceHname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 8),
    _SlbNewCfgVirtServiceHname_Type()
)
slbNewCfgVirtServiceHname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHname.setStatus("mandatory")


class _SlbNewCfgVirtServiceHttpSlb_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpSlb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("browser", 6),
          ("cookie", 4),
          ("disabled", 1),
          ("headerhash", 8),
          ("host", 5),
          ("others", 7),
          ("urlhash", 3),
          ("urlslb", 2))
    )


_SlbNewCfgVirtServiceHttpSlb_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpSlb_Object = MibTableColumn
slbNewCfgVirtServiceHttpSlb = _SlbNewCfgVirtServiceHttpSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 9),
    _SlbNewCfgVirtServiceHttpSlb_Type()
)
slbNewCfgVirtServiceHttpSlb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpSlb.setStatus("mandatory")
_SlbNewCfgVirtServiceBwmContract_Type = Integer32
_SlbNewCfgVirtServiceBwmContract_Object = MibTableColumn
slbNewCfgVirtServiceBwmContract = _SlbNewCfgVirtServiceBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 10),
    _SlbNewCfgVirtServiceBwmContract_Type()
)
slbNewCfgVirtServiceBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceBwmContract.setStatus("mandatory")


class _SlbNewCfgVirtServiceDirServerRtn_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDirServerRtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtServiceDirServerRtn_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDirServerRtn_Object = MibTableColumn
slbNewCfgVirtServiceDirServerRtn = _SlbNewCfgVirtServiceDirServerRtn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 11),
    _SlbNewCfgVirtServiceDirServerRtn_Type()
)
slbNewCfgVirtServiceDirServerRtn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDirServerRtn.setStatus("mandatory")


class _SlbNewCfgVirtServiceDelete_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgVirtServiceDelete_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDelete_Object = MibTableColumn
slbNewCfgVirtServiceDelete = _SlbNewCfgVirtServiceDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 12),
    _SlbNewCfgVirtServiceDelete_Type()
)
slbNewCfgVirtServiceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDelete.setStatus("mandatory")


class _SlbNewCfgVirtServiceRtspUrlParse_Type(Integer32):
    """Custom type slbNewCfgVirtServiceRtspUrlParse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("hash", 3),
          ("patternMatch", 4))
    )


_SlbNewCfgVirtServiceRtspUrlParse_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceRtspUrlParse_Object = MibTableColumn
slbNewCfgVirtServiceRtspUrlParse = _SlbNewCfgVirtServiceRtspUrlParse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 13),
    _SlbNewCfgVirtServiceRtspUrlParse_Type()
)
slbNewCfgVirtServiceRtspUrlParse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRtspUrlParse.setStatus("mandatory")


class _SlbNewCfgVirtServiceCookieMode_Type(Integer32):
    """Custom type slbNewCfgVirtServiceCookieMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("insert", 3),
          ("passive", 2),
          ("rewrite", 1))
    )


_SlbNewCfgVirtServiceCookieMode_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceCookieMode_Object = MibTableColumn
slbNewCfgVirtServiceCookieMode = _SlbNewCfgVirtServiceCookieMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 14),
    _SlbNewCfgVirtServiceCookieMode_Type()
)
slbNewCfgVirtServiceCookieMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceCookieMode.setStatus("mandatory")


class _SlbNewCfgVirtServiceDBind_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDBind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtServiceDBind_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDBind_Object = MibTableColumn
slbNewCfgVirtServiceDBind = _SlbNewCfgVirtServiceDBind_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 15),
    _SlbNewCfgVirtServiceDBind_Type()
)
slbNewCfgVirtServiceDBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDBind.setStatus("mandatory")


class _SlbNewCfgVirtServiceFtpParsing_Type(Integer32):
    """Custom type slbNewCfgVirtServiceFtpParsing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtServiceFtpParsing_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceFtpParsing_Object = MibTableColumn
slbNewCfgVirtServiceFtpParsing = _SlbNewCfgVirtServiceFtpParsing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 16),
    _SlbNewCfgVirtServiceFtpParsing_Type()
)
slbNewCfgVirtServiceFtpParsing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceFtpParsing.setStatus("mandatory")


class _SlbNewCfgVirtServiceHttpSlbOption_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpSlbOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("none", 3),
          ("or", 2))
    )


_SlbNewCfgVirtServiceHttpSlbOption_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpSlbOption_Object = MibTableColumn
slbNewCfgVirtServiceHttpSlbOption = _SlbNewCfgVirtServiceHttpSlbOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 17),
    _SlbNewCfgVirtServiceHttpSlbOption_Type()
)
slbNewCfgVirtServiceHttpSlbOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpSlbOption.setStatus("mandatory")


class _SlbNewCfgVirtServiceHttpSlb2_Type(Integer32):
    """Custom type slbNewCfgVirtServiceHttpSlb2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("browser", 6),
          ("cookie", 4),
          ("disabled", 1),
          ("headerhash", 8),
          ("host", 5),
          ("others", 7),
          ("urlhash", 3),
          ("urlslb", 2))
    )


_SlbNewCfgVirtServiceHttpSlb2_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceHttpSlb2_Object = MibTableColumn
slbNewCfgVirtServiceHttpSlb2 = _SlbNewCfgVirtServiceHttpSlb2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 18),
    _SlbNewCfgVirtServiceHttpSlb2_Type()
)
slbNewCfgVirtServiceHttpSlb2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceHttpSlb2.setStatus("mandatory")


class _SlbNewCfgVirtServiceRemapUDPFrags_Type(Integer32):
    """Custom type slbNewCfgVirtServiceRemapUDPFrags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtServiceRemapUDPFrags_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceRemapUDPFrags_Object = MibTableColumn
slbNewCfgVirtServiceRemapUDPFrags = _SlbNewCfgVirtServiceRemapUDPFrags_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 19),
    _SlbNewCfgVirtServiceRemapUDPFrags_Type()
)
slbNewCfgVirtServiceRemapUDPFrags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceRemapUDPFrags.setStatus("mandatory")


class _SlbNewCfgVirtServiceDnsSlb_Type(Integer32):
    """Custom type slbNewCfgVirtServiceDnsSlb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtServiceDnsSlb_Type.__name__ = "Integer32"
_SlbNewCfgVirtServiceDnsSlb_Object = MibTableColumn
slbNewCfgVirtServiceDnsSlb = _SlbNewCfgVirtServiceDnsSlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 8, 1, 20),
    _SlbNewCfgVirtServiceDnsSlb_Type()
)
slbNewCfgVirtServiceDnsSlb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtServiceDnsSlb.setStatus("mandatory")
_SlbGroupTableMaxSize_Type = Integer32
_SlbGroupTableMaxSize_Object = MibScalar
slbGroupTableMaxSize = _SlbGroupTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 9),
    _SlbGroupTableMaxSize_Type()
)
slbGroupTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbGroupTableMaxSize.setStatus("mandatory")
_SlbCurCfgGroupTable_Object = MibTable
slbCurCfgGroupTable = _SlbCurCfgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10)
)
if mibBuilder.loadTexts:
    slbCurCfgGroupTable.setStatus("mandatory")
_SlbCurCfgGroupEntry_Object = MibTableRow
slbCurCfgGroupEntry = _SlbCurCfgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1)
)
slbCurCfgGroupEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgGroupIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgGroupEntry.setStatus("mandatory")
_SlbCurCfgGroupIndex_Type = Integer32
_SlbCurCfgGroupIndex_Object = MibTableColumn
slbCurCfgGroupIndex = _SlbCurCfgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 1),
    _SlbCurCfgGroupIndex_Type()
)
slbCurCfgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupIndex.setStatus("mandatory")


class _SlbCurCfgGroupRealServers_Type(OctetString):
    """Custom type slbCurCfgGroupRealServers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbCurCfgGroupRealServers_Type.__name__ = "OctetString"
_SlbCurCfgGroupRealServers_Object = MibTableColumn
slbCurCfgGroupRealServers = _SlbCurCfgGroupRealServers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 2),
    _SlbCurCfgGroupRealServers_Type()
)
slbCurCfgGroupRealServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealServers.setStatus("mandatory")


class _SlbCurCfgGroupMetric_Type(Integer32):
    """Custom type slbCurCfgGroupMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 6),
          ("hash", 4),
          ("leastConnections", 2),
          ("minMisses", 3),
          ("response", 5),
          ("roundRobin", 1))
    )


_SlbCurCfgGroupMetric_Type.__name__ = "Integer32"
_SlbCurCfgGroupMetric_Object = MibTableColumn
slbCurCfgGroupMetric = _SlbCurCfgGroupMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 3),
    _SlbCurCfgGroupMetric_Type()
)
slbCurCfgGroupMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupMetric.setStatus("mandatory")
_SlbCurCfgGroupBackupServer_Type = Integer32
_SlbCurCfgGroupBackupServer_Object = MibTableColumn
slbCurCfgGroupBackupServer = _SlbCurCfgGroupBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 4),
    _SlbCurCfgGroupBackupServer_Type()
)
slbCurCfgGroupBackupServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupBackupServer.setStatus("mandatory")


class _SlbCurCfgGroupHealthCheckUrl_Type(DisplayString):
    """Custom type slbCurCfgGroupHealthCheckUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbCurCfgGroupHealthCheckUrl_Type.__name__ = "DisplayString"
_SlbCurCfgGroupHealthCheckUrl_Object = MibTableColumn
slbCurCfgGroupHealthCheckUrl = _SlbCurCfgGroupHealthCheckUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 5),
    _SlbCurCfgGroupHealthCheckUrl_Type()
)
slbCurCfgGroupHealthCheckUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupHealthCheckUrl.setStatus("mandatory")


class _SlbCurCfgGroupHealthCheckLayer_Type(Integer32):
    """Custom type slbCurCfgGroupHealthCheckLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("arp", 33),
          ("dns", 4),
          ("ftp", 8),
          ("http", 3),
          ("icmp", 1),
          ("imap", 9),
          ("ldap", 31),
          ("link", 28),
          ("nntp", 7),
          ("pop3", 6),
          ("radius", 10),
          ("script1", 12),
          ("script10", 21),
          ("script11", 22),
          ("script12", 23),
          ("script13", 24),
          ("script14", 25),
          ("script15", 26),
          ("script16", 27),
          ("script2", 13),
          ("script3", 14),
          ("script4", 15),
          ("script5", 16),
          ("script6", 17),
          ("script7", 18),
          ("script8", 19),
          ("script9", 20),
          ("smtp", 5),
          ("sslh", 11),
          ("tcp", 2),
          ("udpdns", 32),
          ("wsp", 29),
          ("wtls", 30))
    )


_SlbCurCfgGroupHealthCheckLayer_Type.__name__ = "Integer32"
_SlbCurCfgGroupHealthCheckLayer_Object = MibTableColumn
slbCurCfgGroupHealthCheckLayer = _SlbCurCfgGroupHealthCheckLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 6),
    _SlbCurCfgGroupHealthCheckLayer_Type()
)
slbCurCfgGroupHealthCheckLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupHealthCheckLayer.setStatus("mandatory")


class _SlbCurCfgGroupName_Type(DisplayString):
    """Custom type slbCurCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbCurCfgGroupName_Type.__name__ = "DisplayString"
_SlbCurCfgGroupName_Object = MibTableColumn
slbCurCfgGroupName = _SlbCurCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 7),
    _SlbCurCfgGroupName_Type()
)
slbCurCfgGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupName.setStatus("mandatory")


class _SlbCurCfgGroupRealThreshold_Type(Integer32):
    """Custom type slbCurCfgGroupRealThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbCurCfgGroupRealThreshold_Type.__name__ = "Integer32"
_SlbCurCfgGroupRealThreshold_Object = MibTableColumn
slbCurCfgGroupRealThreshold = _SlbCurCfgGroupRealThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 8),
    _SlbCurCfgGroupRealThreshold_Type()
)
slbCurCfgGroupRealThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupRealThreshold.setStatus("mandatory")
_SlbCurCfgGroupBackupGroup_Type = Integer32
_SlbCurCfgGroupBackupGroup_Object = MibTableColumn
slbCurCfgGroupBackupGroup = _SlbCurCfgGroupBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 9),
    _SlbCurCfgGroupBackupGroup_Type()
)
slbCurCfgGroupBackupGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupBackupGroup.setStatus("mandatory")


class _SlbCurCfgGroupVipHealthCheck_Type(Integer32):
    """Custom type slbCurCfgGroupVipHealthCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgGroupVipHealthCheck_Type.__name__ = "Integer32"
_SlbCurCfgGroupVipHealthCheck_Object = MibTableColumn
slbCurCfgGroupVipHealthCheck = _SlbCurCfgGroupVipHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 10, 1, 10),
    _SlbCurCfgGroupVipHealthCheck_Type()
)
slbCurCfgGroupVipHealthCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGroupVipHealthCheck.setStatus("mandatory")
_SlbNewCfgGroupTable_Object = MibTable
slbNewCfgGroupTable = _SlbNewCfgGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11)
)
if mibBuilder.loadTexts:
    slbNewCfgGroupTable.setStatus("mandatory")
_SlbNewCfgGroupEntry_Object = MibTableRow
slbNewCfgGroupEntry = _SlbNewCfgGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1)
)
slbNewCfgGroupEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgGroupIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgGroupEntry.setStatus("mandatory")
_SlbNewCfgGroupIndex_Type = Integer32
_SlbNewCfgGroupIndex_Object = MibTableColumn
slbNewCfgGroupIndex = _SlbNewCfgGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 1),
    _SlbNewCfgGroupIndex_Type()
)
slbNewCfgGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgGroupIndex.setStatus("mandatory")


class _SlbNewCfgGroupRealServers_Type(OctetString):
    """Custom type slbNewCfgGroupRealServers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbNewCfgGroupRealServers_Type.__name__ = "OctetString"
_SlbNewCfgGroupRealServers_Object = MibTableColumn
slbNewCfgGroupRealServers = _SlbNewCfgGroupRealServers_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 2),
    _SlbNewCfgGroupRealServers_Type()
)
slbNewCfgGroupRealServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealServers.setStatus("mandatory")
_SlbNewCfgGroupAddServer_Type = Integer32
_SlbNewCfgGroupAddServer_Object = MibTableColumn
slbNewCfgGroupAddServer = _SlbNewCfgGroupAddServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 3),
    _SlbNewCfgGroupAddServer_Type()
)
slbNewCfgGroupAddServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupAddServer.setStatus("mandatory")
_SlbNewCfgGroupRemoveServer_Type = Integer32
_SlbNewCfgGroupRemoveServer_Object = MibTableColumn
slbNewCfgGroupRemoveServer = _SlbNewCfgGroupRemoveServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 4),
    _SlbNewCfgGroupRemoveServer_Type()
)
slbNewCfgGroupRemoveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupRemoveServer.setStatus("mandatory")


class _SlbNewCfgGroupMetric_Type(Integer32):
    """Custom type slbNewCfgGroupMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 6),
          ("hash", 4),
          ("leastConnections", 2),
          ("minMisses", 3),
          ("response", 5),
          ("roundRobin", 1))
    )


_SlbNewCfgGroupMetric_Type.__name__ = "Integer32"
_SlbNewCfgGroupMetric_Object = MibTableColumn
slbNewCfgGroupMetric = _SlbNewCfgGroupMetric_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 5),
    _SlbNewCfgGroupMetric_Type()
)
slbNewCfgGroupMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupMetric.setStatus("mandatory")
_SlbNewCfgGroupBackupServer_Type = Integer32
_SlbNewCfgGroupBackupServer_Object = MibTableColumn
slbNewCfgGroupBackupServer = _SlbNewCfgGroupBackupServer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 6),
    _SlbNewCfgGroupBackupServer_Type()
)
slbNewCfgGroupBackupServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupBackupServer.setStatus("mandatory")


class _SlbNewCfgGroupDelete_Type(Integer32):
    """Custom type slbNewCfgGroupDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgGroupDelete_Type.__name__ = "Integer32"
_SlbNewCfgGroupDelete_Object = MibTableColumn
slbNewCfgGroupDelete = _SlbNewCfgGroupDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 7),
    _SlbNewCfgGroupDelete_Type()
)
slbNewCfgGroupDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupDelete.setStatus("mandatory")


class _SlbNewCfgGroupHealthCheckUrl_Type(DisplayString):
    """Custom type slbNewCfgGroupHealthCheckUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbNewCfgGroupHealthCheckUrl_Type.__name__ = "DisplayString"
_SlbNewCfgGroupHealthCheckUrl_Object = MibTableColumn
slbNewCfgGroupHealthCheckUrl = _SlbNewCfgGroupHealthCheckUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 8),
    _SlbNewCfgGroupHealthCheckUrl_Type()
)
slbNewCfgGroupHealthCheckUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupHealthCheckUrl.setStatus("mandatory")


class _SlbNewCfgGroupHealthCheckLayer_Type(Integer32):
    """Custom type slbNewCfgGroupHealthCheckLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("arp", 33),
          ("dns", 4),
          ("ftp", 8),
          ("http", 3),
          ("icmp", 1),
          ("imap", 9),
          ("ldap", 31),
          ("link", 28),
          ("nntp", 7),
          ("pop3", 6),
          ("radius", 10),
          ("script1", 12),
          ("script10", 21),
          ("script11", 22),
          ("script12", 23),
          ("script13", 24),
          ("script14", 25),
          ("script15", 26),
          ("script16", 27),
          ("script2", 13),
          ("script3", 14),
          ("script4", 15),
          ("script5", 16),
          ("script6", 17),
          ("script7", 18),
          ("script8", 19),
          ("script9", 20),
          ("smtp", 5),
          ("sslh", 11),
          ("tcp", 2),
          ("udpdns", 32),
          ("wsp", 29),
          ("wtls", 30))
    )


_SlbNewCfgGroupHealthCheckLayer_Type.__name__ = "Integer32"
_SlbNewCfgGroupHealthCheckLayer_Object = MibTableColumn
slbNewCfgGroupHealthCheckLayer = _SlbNewCfgGroupHealthCheckLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 9),
    _SlbNewCfgGroupHealthCheckLayer_Type()
)
slbNewCfgGroupHealthCheckLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupHealthCheckLayer.setStatus("mandatory")


class _SlbNewCfgGroupName_Type(DisplayString):
    """Custom type slbNewCfgGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SlbNewCfgGroupName_Type.__name__ = "DisplayString"
_SlbNewCfgGroupName_Object = MibTableColumn
slbNewCfgGroupName = _SlbNewCfgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 10),
    _SlbNewCfgGroupName_Type()
)
slbNewCfgGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupName.setStatus("mandatory")


class _SlbNewCfgGroupRealThreshold_Type(Integer32):
    """Custom type slbNewCfgGroupRealThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbNewCfgGroupRealThreshold_Type.__name__ = "Integer32"
_SlbNewCfgGroupRealThreshold_Object = MibTableColumn
slbNewCfgGroupRealThreshold = _SlbNewCfgGroupRealThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 11),
    _SlbNewCfgGroupRealThreshold_Type()
)
slbNewCfgGroupRealThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupRealThreshold.setStatus("mandatory")
_SlbNewCfgGroupBackupGroup_Type = Integer32
_SlbNewCfgGroupBackupGroup_Object = MibTableColumn
slbNewCfgGroupBackupGroup = _SlbNewCfgGroupBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 12),
    _SlbNewCfgGroupBackupGroup_Type()
)
slbNewCfgGroupBackupGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupBackupGroup.setStatus("mandatory")


class _SlbNewCfgGroupVipHealthCheck_Type(Integer32):
    """Custom type slbNewCfgGroupVipHealthCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgGroupVipHealthCheck_Type.__name__ = "Integer32"
_SlbNewCfgGroupVipHealthCheck_Object = MibTableColumn
slbNewCfgGroupVipHealthCheck = _SlbNewCfgGroupVipHealthCheck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 11, 1, 13),
    _SlbNewCfgGroupVipHealthCheck_Type()
)
slbNewCfgGroupVipHealthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGroupVipHealthCheck.setStatus("mandatory")
_SlbCurCfgPortTable_Object = MibTable
slbCurCfgPortTable = _SlbCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12)
)
if mibBuilder.loadTexts:
    slbCurCfgPortTable.setStatus("mandatory")
_SlbCurCfgPortEntry_Object = MibTableRow
slbCurCfgPortEntry = _SlbCurCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1)
)
slbCurCfgPortEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgPortIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgPortEntry.setStatus("mandatory")
_SlbCurCfgPortIndex_Type = Integer32
_SlbCurCfgPortIndex_Object = MibTableColumn
slbCurCfgPortIndex = _SlbCurCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 1),
    _SlbCurCfgPortIndex_Type()
)
slbCurCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortIndex.setStatus("mandatory")
_SlbCurCfgPortProxyIpAddr_Type = IpAddress
_SlbCurCfgPortProxyIpAddr_Object = MibTableColumn
slbCurCfgPortProxyIpAddr = _SlbCurCfgPortProxyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 2),
    _SlbCurCfgPortProxyIpAddr_Type()
)
slbCurCfgPortProxyIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortProxyIpAddr.setStatus("mandatory")


class _SlbCurCfgPortSlbState_Type(Integer32):
    """Custom type slbCurCfgPortSlbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("client-server", 4),
          ("none", 1),
          ("server", 3))
    )


_SlbCurCfgPortSlbState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbState_Object = MibTableColumn
slbCurCfgPortSlbState = _SlbCurCfgPortSlbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 3),
    _SlbCurCfgPortSlbState_Type()
)
slbCurCfgPortSlbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbState.setStatus("mandatory")


class _SlbCurCfgPortSlbHotStandby_Type(Integer32):
    """Custom type slbCurCfgPortSlbHotStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgPortSlbHotStandby_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbHotStandby_Object = MibTableColumn
slbCurCfgPortSlbHotStandby = _SlbCurCfgPortSlbHotStandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 4),
    _SlbCurCfgPortSlbHotStandby_Type()
)
slbCurCfgPortSlbHotStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbHotStandby.setStatus("mandatory")


class _SlbCurCfgPortSlbInterSwitch_Type(Integer32):
    """Custom type slbCurCfgPortSlbInterSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgPortSlbInterSwitch_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbInterSwitch_Object = MibTableColumn
slbCurCfgPortSlbInterSwitch = _SlbCurCfgPortSlbInterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 5),
    _SlbCurCfgPortSlbInterSwitch_Type()
)
slbCurCfgPortSlbInterSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbInterSwitch.setStatus("mandatory")


class _SlbCurCfgPortSlbPipState_Type(Integer32):
    """Custom type slbCurCfgPortSlbPipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgPortSlbPipState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbPipState_Object = MibTableColumn
slbCurCfgPortSlbPipState = _SlbCurCfgPortSlbPipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 6),
    _SlbCurCfgPortSlbPipState_Type()
)
slbCurCfgPortSlbPipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbPipState.setStatus("mandatory")


class _SlbCurCfgPortSlbRtsState_Type(Integer32):
    """Custom type slbCurCfgPortSlbRtsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgPortSlbRtsState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbRtsState_Object = MibTableColumn
slbCurCfgPortSlbRtsState = _SlbCurCfgPortSlbRtsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 7),
    _SlbCurCfgPortSlbRtsState_Type()
)
slbCurCfgPortSlbRtsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbRtsState.setStatus("mandatory")


class _SlbCurCfgPortSlbIdslbState_Type(Integer32):
    """Custom type slbCurCfgPortSlbIdslbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgPortSlbIdslbState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbIdslbState_Object = MibTableColumn
slbCurCfgPortSlbIdslbState = _SlbCurCfgPortSlbIdslbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 8),
    _SlbCurCfgPortSlbIdslbState_Type()
)
slbCurCfgPortSlbIdslbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbIdslbState.setStatus("mandatory")


class _SlbCurCfgPortSlbNasaState_Type(Integer32):
    """Custom type slbCurCfgPortSlbNasaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgPortSlbNasaState_Type.__name__ = "Integer32"
_SlbCurCfgPortSlbNasaState_Object = MibTableColumn
slbCurCfgPortSlbNasaState = _SlbCurCfgPortSlbNasaState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 12, 1, 9),
    _SlbCurCfgPortSlbNasaState_Type()
)
slbCurCfgPortSlbNasaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPortSlbNasaState.setStatus("mandatory")
_SlbNewCfgPortTable_Object = MibTable
slbNewCfgPortTable = _SlbNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13)
)
if mibBuilder.loadTexts:
    slbNewCfgPortTable.setStatus("mandatory")
_SlbNewCfgPortEntry_Object = MibTableRow
slbNewCfgPortEntry = _SlbNewCfgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1)
)
slbNewCfgPortEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgPortIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgPortEntry.setStatus("mandatory")
_SlbNewCfgPortIndex_Type = Integer32
_SlbNewCfgPortIndex_Object = MibTableColumn
slbNewCfgPortIndex = _SlbNewCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 1),
    _SlbNewCfgPortIndex_Type()
)
slbNewCfgPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgPortIndex.setStatus("mandatory")
_SlbNewCfgPortProxyIpAddr_Type = IpAddress
_SlbNewCfgPortProxyIpAddr_Object = MibTableColumn
slbNewCfgPortProxyIpAddr = _SlbNewCfgPortProxyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 2),
    _SlbNewCfgPortProxyIpAddr_Type()
)
slbNewCfgPortProxyIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortProxyIpAddr.setStatus("mandatory")


class _SlbNewCfgPortSlbState_Type(Integer32):
    """Custom type slbNewCfgPortSlbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("client-server", 4),
          ("none", 1),
          ("server", 3))
    )


_SlbNewCfgPortSlbState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbState_Object = MibTableColumn
slbNewCfgPortSlbState = _SlbNewCfgPortSlbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 3),
    _SlbNewCfgPortSlbState_Type()
)
slbNewCfgPortSlbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbState.setStatus("mandatory")


class _SlbNewCfgPortSlbHotStandby_Type(Integer32):
    """Custom type slbNewCfgPortSlbHotStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgPortSlbHotStandby_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbHotStandby_Object = MibTableColumn
slbNewCfgPortSlbHotStandby = _SlbNewCfgPortSlbHotStandby_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 4),
    _SlbNewCfgPortSlbHotStandby_Type()
)
slbNewCfgPortSlbHotStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbHotStandby.setStatus("mandatory")


class _SlbNewCfgPortSlbInterSwitch_Type(Integer32):
    """Custom type slbNewCfgPortSlbInterSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgPortSlbInterSwitch_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbInterSwitch_Object = MibTableColumn
slbNewCfgPortSlbInterSwitch = _SlbNewCfgPortSlbInterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 5),
    _SlbNewCfgPortSlbInterSwitch_Type()
)
slbNewCfgPortSlbInterSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbInterSwitch.setStatus("mandatory")


class _SlbNewCfgPortSlbPipState_Type(Integer32):
    """Custom type slbNewCfgPortSlbPipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgPortSlbPipState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbPipState_Object = MibTableColumn
slbNewCfgPortSlbPipState = _SlbNewCfgPortSlbPipState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 6),
    _SlbNewCfgPortSlbPipState_Type()
)
slbNewCfgPortSlbPipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbPipState.setStatus("mandatory")


class _SlbNewCfgPortSlbRtsState_Type(Integer32):
    """Custom type slbNewCfgPortSlbRtsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgPortSlbRtsState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbRtsState_Object = MibTableColumn
slbNewCfgPortSlbRtsState = _SlbNewCfgPortSlbRtsState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 7),
    _SlbNewCfgPortSlbRtsState_Type()
)
slbNewCfgPortSlbRtsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbRtsState.setStatus("mandatory")


class _SlbNewCfgPortDelete_Type(Integer32):
    """Custom type slbNewCfgPortDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgPortDelete_Type.__name__ = "Integer32"
_SlbNewCfgPortDelete_Object = MibTableColumn
slbNewCfgPortDelete = _SlbNewCfgPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 8),
    _SlbNewCfgPortDelete_Type()
)
slbNewCfgPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortDelete.setStatus("mandatory")


class _SlbNewCfgPortSlbIdslbState_Type(Integer32):
    """Custom type slbNewCfgPortSlbIdslbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgPortSlbIdslbState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbIdslbState_Object = MibTableColumn
slbNewCfgPortSlbIdslbState = _SlbNewCfgPortSlbIdslbState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 9),
    _SlbNewCfgPortSlbIdslbState_Type()
)
slbNewCfgPortSlbIdslbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbIdslbState.setStatus("mandatory")


class _SlbNewCfgPortSlbNasaState_Type(Integer32):
    """Custom type slbNewCfgPortSlbNasaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgPortSlbNasaState_Type.__name__ = "Integer32"
_SlbNewCfgPortSlbNasaState_Object = MibTableColumn
slbNewCfgPortSlbNasaState = _SlbNewCfgPortSlbNasaState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 13, 1, 10),
    _SlbNewCfgPortSlbNasaState_Type()
)
slbNewCfgPortSlbNasaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPortSlbNasaState.setStatus("mandatory")
_SlbCurCfgImask_Type = IpAddress
_SlbCurCfgImask_Object = MibScalar
slbCurCfgImask = _SlbCurCfgImask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 14),
    _SlbCurCfgImask_Type()
)
slbCurCfgImask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgImask.setStatus("mandatory")
_SlbNewCfgImask_Type = IpAddress
_SlbNewCfgImask_Object = MibScalar
slbNewCfgImask = _SlbNewCfgImask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 15),
    _SlbNewCfgImask_Type()
)
slbNewCfgImask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgImask.setStatus("mandatory")
_Slbfailover_ObjectIdentity = ObjectIdentity
slbfailover = _Slbfailover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16)
)
_SlbCurCfgFailOverTable_Object = MibTable
slbCurCfgFailOverTable = _SlbCurCfgFailOverTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1)
)
if mibBuilder.loadTexts:
    slbCurCfgFailOverTable.setStatus("obsolete")
_SlbCurCfgFailOverTblEntry_Object = MibTableRow
slbCurCfgFailOverTblEntry = _SlbCurCfgFailOverTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1)
)
slbCurCfgFailOverTblEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgFailOverIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgFailOverTblEntry.setStatus("obsolete")
_SlbCurCfgFailOverIndex_Type = Integer32
_SlbCurCfgFailOverIndex_Object = MibTableColumn
slbCurCfgFailOverIndex = _SlbCurCfgFailOverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 1),
    _SlbCurCfgFailOverIndex_Type()
)
slbCurCfgFailOverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverIndex.setStatus("obsolete")
_SlbCurCfgFailOverPrimaryIp_Type = IpAddress
_SlbCurCfgFailOverPrimaryIp_Object = MibTableColumn
slbCurCfgFailOverPrimaryIp = _SlbCurCfgFailOverPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 2),
    _SlbCurCfgFailOverPrimaryIp_Type()
)
slbCurCfgFailOverPrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverPrimaryIp.setStatus("obsolete")
_SlbCurCfgFailOverSecondaryIp_Type = IpAddress
_SlbCurCfgFailOverSecondaryIp_Object = MibTableColumn
slbCurCfgFailOverSecondaryIp = _SlbCurCfgFailOverSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 3),
    _SlbCurCfgFailOverSecondaryIp_Type()
)
slbCurCfgFailOverSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverSecondaryIp.setStatus("obsolete")


class _SlbCurCfgFailOverSilenceInterval_Type(Integer32):
    """Custom type slbCurCfgFailOverSilenceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_SlbCurCfgFailOverSilenceInterval_Type.__name__ = "Integer32"
_SlbCurCfgFailOverSilenceInterval_Object = MibTableColumn
slbCurCfgFailOverSilenceInterval = _SlbCurCfgFailOverSilenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 4),
    _SlbCurCfgFailOverSilenceInterval_Type()
)
slbCurCfgFailOverSilenceInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverSilenceInterval.setStatus("obsolete")


class _SlbCurCfgFailOverState_Type(Integer32):
    """Custom type slbCurCfgFailOverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbCurCfgFailOverState_Type.__name__ = "Integer32"
_SlbCurCfgFailOverState_Object = MibTableColumn
slbCurCfgFailOverState = _SlbCurCfgFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 5),
    _SlbCurCfgFailOverState_Type()
)
slbCurCfgFailOverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverState.setStatus("obsolete")


class _SlbCurCfgFailOverRouteSupply_Type(Integer32):
    """Custom type slbCurCfgFailOverRouteSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgFailOverRouteSupply_Type.__name__ = "Integer32"
_SlbCurCfgFailOverRouteSupply_Object = MibTableColumn
slbCurCfgFailOverRouteSupply = _SlbCurCfgFailOverRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 1, 1, 6),
    _SlbCurCfgFailOverRouteSupply_Type()
)
slbCurCfgFailOverRouteSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFailOverRouteSupply.setStatus("obsolete")
_SlbNewCfgFailOverTable_Object = MibTable
slbNewCfgFailOverTable = _SlbNewCfgFailOverTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2)
)
if mibBuilder.loadTexts:
    slbNewCfgFailOverTable.setStatus("obsolete")
_SlbNewCfgFailOverTblEntry_Object = MibTableRow
slbNewCfgFailOverTblEntry = _SlbNewCfgFailOverTblEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1)
)
slbNewCfgFailOverTblEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgFailOverIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgFailOverTblEntry.setStatus("obsolete")
_SlbNewCfgFailOverIndex_Type = Integer32
_SlbNewCfgFailOverIndex_Object = MibTableColumn
slbNewCfgFailOverIndex = _SlbNewCfgFailOverIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 1),
    _SlbNewCfgFailOverIndex_Type()
)
slbNewCfgFailOverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgFailOverIndex.setStatus("obsolete")
_SlbNewCfgFailOverPrimaryIp_Type = IpAddress
_SlbNewCfgFailOverPrimaryIp_Object = MibTableColumn
slbNewCfgFailOverPrimaryIp = _SlbNewCfgFailOverPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 2),
    _SlbNewCfgFailOverPrimaryIp_Type()
)
slbNewCfgFailOverPrimaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverPrimaryIp.setStatus("obsolete")
_SlbNewCfgFailOverSecondaryIp_Type = IpAddress
_SlbNewCfgFailOverSecondaryIp_Object = MibTableColumn
slbNewCfgFailOverSecondaryIp = _SlbNewCfgFailOverSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 3),
    _SlbNewCfgFailOverSecondaryIp_Type()
)
slbNewCfgFailOverSecondaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverSecondaryIp.setStatus("obsolete")


class _SlbNewCfgFailOverSilenceInterval_Type(Integer32):
    """Custom type slbNewCfgFailOverSilenceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 120),
    )


_SlbNewCfgFailOverSilenceInterval_Type.__name__ = "Integer32"
_SlbNewCfgFailOverSilenceInterval_Object = MibTableColumn
slbNewCfgFailOverSilenceInterval = _SlbNewCfgFailOverSilenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 4),
    _SlbNewCfgFailOverSilenceInterval_Type()
)
slbNewCfgFailOverSilenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverSilenceInterval.setStatus("obsolete")


class _SlbNewCfgFailOverState_Type(Integer32):
    """Custom type slbNewCfgFailOverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbNewCfgFailOverState_Type.__name__ = "Integer32"
_SlbNewCfgFailOverState_Object = MibTableColumn
slbNewCfgFailOverState = _SlbNewCfgFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 5),
    _SlbNewCfgFailOverState_Type()
)
slbNewCfgFailOverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFailOverState.setStatus("obsolete")


class _SlbNewCfgFailOverRouteSupply_Type(Integer32):
    """Custom type slbNewCfgFailOverRouteSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgFailOverRouteSupply_Type.__name__ = "Integer32"
_SlbNewCfgFailOverRouteSupply_Object = MibTableColumn
slbNewCfgFailOverRouteSupply = _SlbNewCfgFailOverRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 16, 2, 1, 6),
    _SlbNewCfgFailOverRouteSupply_Type()
)
slbNewCfgFailOverRouteSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgFailOverRouteSupply.setStatus("obsolete")


class _SlbCurCfgGlobalControl_Type(Integer32):
    """Custom type slbCurCfgGlobalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbCurCfgGlobalControl_Type.__name__ = "Integer32"
_SlbCurCfgGlobalControl_Object = MibScalar
slbCurCfgGlobalControl = _SlbCurCfgGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 17),
    _SlbCurCfgGlobalControl_Type()
)
slbCurCfgGlobalControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGlobalControl.setStatus("mandatory")


class _SlbNewCfgGlobalControl_Type(Integer32):
    """Custom type slbNewCfgGlobalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2))
    )


_SlbNewCfgGlobalControl_Type.__name__ = "Integer32"
_SlbNewCfgGlobalControl_Object = MibScalar
slbNewCfgGlobalControl = _SlbNewCfgGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 18),
    _SlbNewCfgGlobalControl_Type()
)
slbNewCfgGlobalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGlobalControl.setStatus("mandatory")
_SlbCurCfgMnet_Type = IpAddress
_SlbCurCfgMnet_Object = MibScalar
slbCurCfgMnet = _SlbCurCfgMnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 19),
    _SlbCurCfgMnet_Type()
)
slbCurCfgMnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMnet.setStatus("mandatory")
_SlbNewCfgMnet_Type = IpAddress
_SlbNewCfgMnet_Object = MibScalar
slbNewCfgMnet = _SlbNewCfgMnet_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 20),
    _SlbNewCfgMnet_Type()
)
slbNewCfgMnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMnet.setStatus("mandatory")
_SlbCurCfgMmask_Type = IpAddress
_SlbCurCfgMmask_Object = MibScalar
slbCurCfgMmask = _SlbCurCfgMmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 21),
    _SlbCurCfgMmask_Type()
)
slbCurCfgMmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMmask.setStatus("mandatory")
_SlbNewCfgMmask_Type = IpAddress
_SlbNewCfgMmask_Object = MibScalar
slbNewCfgMmask = _SlbNewCfgMmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 22),
    _SlbNewCfgMmask_Type()
)
slbNewCfgMmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMmask.setStatus("mandatory")


class _SlbCurCfgRadiusAuthenString_Type(DisplayString):
    """Custom type slbCurCfgRadiusAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgRadiusAuthenString_Type.__name__ = "DisplayString"
_SlbCurCfgRadiusAuthenString_Object = MibScalar
slbCurCfgRadiusAuthenString = _SlbCurCfgRadiusAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 23),
    _SlbCurCfgRadiusAuthenString_Type()
)
slbCurCfgRadiusAuthenString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRadiusAuthenString.setStatus("mandatory")


class _SlbNewCfgRadiusAuthenString_Type(DisplayString):
    """Custom type slbNewCfgRadiusAuthenString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgRadiusAuthenString_Type.__name__ = "DisplayString"
_SlbNewCfgRadiusAuthenString_Object = MibScalar
slbNewCfgRadiusAuthenString = _SlbNewCfgRadiusAuthenString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 24),
    _SlbNewCfgRadiusAuthenString_Type()
)
slbNewCfgRadiusAuthenString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRadiusAuthenString.setStatus("mandatory")


class _SlbCurCfgDirectMode_Type(Integer32):
    """Custom type slbCurCfgDirectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgDirectMode_Type.__name__ = "Integer32"
_SlbCurCfgDirectMode_Object = MibScalar
slbCurCfgDirectMode = _SlbCurCfgDirectMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 25),
    _SlbCurCfgDirectMode_Type()
)
slbCurCfgDirectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgDirectMode.setStatus("mandatory")


class _SlbNewCfgDirectMode_Type(Integer32):
    """Custom type slbNewCfgDirectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgDirectMode_Type.__name__ = "Integer32"
_SlbNewCfgDirectMode_Object = MibScalar
slbNewCfgDirectMode = _SlbNewCfgDirectMode_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 26),
    _SlbNewCfgDirectMode_Type()
)
slbNewCfgDirectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgDirectMode.setStatus("mandatory")
_SlbUrl_ObjectIdentity = ObjectIdentity
slbUrl = _SlbUrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27)
)
_SlbUrlRedir_ObjectIdentity = ObjectIdentity
slbUrlRedir = _SlbUrlRedir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1)
)
_SlbCurCfgUrlExpTable_Object = MibTable
slbCurCfgUrlExpTable = _SlbCurCfgUrlExpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlExpTable.setStatus("mandatory")
_SlbCurCfgUrlExpTableEntry_Object = MibTableRow
slbCurCfgUrlExpTableEntry = _SlbCurCfgUrlExpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1, 1)
)
slbCurCfgUrlExpTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgUrlExpIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlExpTableEntry.setStatus("mandatory")
_SlbCurCfgUrlExpIndex_Type = Integer32
_SlbCurCfgUrlExpIndex_Object = MibTableColumn
slbCurCfgUrlExpIndex = _SlbCurCfgUrlExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1, 1, 1),
    _SlbCurCfgUrlExpIndex_Type()
)
slbCurCfgUrlExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlExpIndex.setStatus("mandatory")


class _SlbCurCfgUrlExpression_Type(DisplayString):
    """Custom type slbCurCfgUrlExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbCurCfgUrlExpression_Type.__name__ = "DisplayString"
_SlbCurCfgUrlExpression_Object = MibTableColumn
slbCurCfgUrlExpression = _SlbCurCfgUrlExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 1, 1, 2),
    _SlbCurCfgUrlExpression_Type()
)
slbCurCfgUrlExpression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlExpression.setStatus("mandatory")
_SlbNewCfgUrlExpTable_Object = MibTable
slbNewCfgUrlExpTable = _SlbNewCfgUrlExpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlExpTable.setStatus("mandatory")
_SlbNewCfgUrlExpTableEntry_Object = MibTableRow
slbNewCfgUrlExpTableEntry = _SlbNewCfgUrlExpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1)
)
slbNewCfgUrlExpTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgUrlExpIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlExpTableEntry.setStatus("mandatory")
_SlbNewCfgUrlExpIndex_Type = Integer32
_SlbNewCfgUrlExpIndex_Object = MibTableColumn
slbNewCfgUrlExpIndex = _SlbNewCfgUrlExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1, 1),
    _SlbNewCfgUrlExpIndex_Type()
)
slbNewCfgUrlExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlExpIndex.setStatus("mandatory")


class _SlbNewCfgUrlExpression_Type(DisplayString):
    """Custom type slbNewCfgUrlExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlbNewCfgUrlExpression_Type.__name__ = "DisplayString"
_SlbNewCfgUrlExpression_Object = MibTableColumn
slbNewCfgUrlExpression = _SlbNewCfgUrlExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1, 2),
    _SlbNewCfgUrlExpression_Type()
)
slbNewCfgUrlExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlExpression.setStatus("mandatory")


class _SlbNewCfgUrlExpDelete_Type(Integer32):
    """Custom type slbNewCfgUrlExpDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgUrlExpDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlExpDelete_Object = MibTableColumn
slbNewCfgUrlExpDelete = _SlbNewCfgUrlExpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 2, 1, 3),
    _SlbNewCfgUrlExpDelete_Type()
)
slbNewCfgUrlExpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlExpDelete.setStatus("mandatory")


class _SlbCurCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNonGetOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNonGetOrigSrv = _SlbCurCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 3),
    _SlbCurCfgUrlRedirNonGetOrigSrv_Type()
)
slbCurCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNonGetOrigSrv.setStatus("mandatory")


class _SlbNewCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNonGetOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNonGetOrigSrv = _SlbNewCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 4),
    _SlbNewCfgUrlRedirNonGetOrigSrv_Type()
)
slbNewCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNonGetOrigSrv.setStatus("mandatory")


class _SlbCurCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirCookieOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbCurCfgUrlRedirCookieOrigSrv = _SlbCurCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 5),
    _SlbCurCfgUrlRedirCookieOrigSrv_Type()
)
slbCurCfgUrlRedirCookieOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirCookieOrigSrv.setStatus("mandatory")


class _SlbNewCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirCookieOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbNewCfgUrlRedirCookieOrigSrv = _SlbNewCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 6),
    _SlbNewCfgUrlRedirCookieOrigSrv_Type()
)
slbNewCfgUrlRedirCookieOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirCookieOrigSrv.setStatus("mandatory")


class _SlbCurCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNoCacheOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNoCacheOrigSrv = _SlbCurCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 7),
    _SlbCurCfgUrlRedirNoCacheOrigSrv_Type()
)
slbCurCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNoCacheOrigSrv.setStatus("mandatory")


class _SlbNewCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNoCacheOrigSrv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNoCacheOrigSrv = _SlbNewCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 8),
    _SlbNewCfgUrlRedirNoCacheOrigSrv_Type()
)
slbNewCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNoCacheOrigSrv.setStatus("mandatory")


class _SlbCurCfgUrlRedirUriHashLength_Type(Integer32):
    """Custom type slbCurCfgUrlRedirUriHashLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbCurCfgUrlRedirUriHashLength_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirUriHashLength_Object = MibScalar
slbCurCfgUrlRedirUriHashLength = _SlbCurCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 9),
    _SlbCurCfgUrlRedirUriHashLength_Type()
)
slbCurCfgUrlRedirUriHashLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirUriHashLength.setStatus("mandatory")


class _SlbNewCfgUrlRedirUriHashLength_Type(Integer32):
    """Custom type slbNewCfgUrlRedirUriHashLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbNewCfgUrlRedirUriHashLength_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirUriHashLength_Object = MibScalar
slbNewCfgUrlRedirUriHashLength = _SlbNewCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 10),
    _SlbNewCfgUrlRedirUriHashLength_Type()
)
slbNewCfgUrlRedirUriHashLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirUriHashLength.setStatus("mandatory")


class _SlbCurCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbCurCfgUrlRedirHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirHeader_Object = MibScalar
slbCurCfgUrlRedirHeader = _SlbCurCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 11),
    _SlbCurCfgUrlRedirHeader_Type()
)
slbCurCfgUrlRedirHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeader.setStatus("mandatory")


class _SlbNewCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbNewCfgUrlRedirHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirHeader_Object = MibScalar
slbNewCfgUrlRedirHeader = _SlbNewCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 12),
    _SlbNewCfgUrlRedirHeader_Type()
)
slbNewCfgUrlRedirHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeader.setStatus("mandatory")


class _SlbCurCfgUrlRedirHeaderName_Type(DisplayString):
    """Custom type slbCurCfgUrlRedirHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgUrlRedirHeaderName_Type.__name__ = "DisplayString"
_SlbCurCfgUrlRedirHeaderName_Object = MibScalar
slbCurCfgUrlRedirHeaderName = _SlbCurCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 13),
    _SlbCurCfgUrlRedirHeaderName_Type()
)
slbCurCfgUrlRedirHeaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeaderName.setStatus("mandatory")


class _SlbNewCfgUrlRedirHeaderName_Type(DisplayString):
    """Custom type slbNewCfgUrlRedirHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgUrlRedirHeaderName_Type.__name__ = "DisplayString"
_SlbNewCfgUrlRedirHeaderName_Object = MibScalar
slbNewCfgUrlRedirHeaderName = _SlbNewCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 14),
    _SlbNewCfgUrlRedirHeaderName_Type()
)
slbNewCfgUrlRedirHeaderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeaderName.setStatus("mandatory")
_SlbUrlExpTableMaxSize_Type = Integer32
_SlbUrlExpTableMaxSize_Object = MibScalar
slbUrlExpTableMaxSize = _SlbUrlExpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 1, 15),
    _SlbUrlExpTableMaxSize_Type()
)
slbUrlExpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlExpTableMaxSize.setStatus("mandatory")
_SlbUrlBalance_ObjectIdentity = ObjectIdentity
slbUrlBalance = _SlbUrlBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2)
)
_SlbCurCfgUrlLbPathTable_Object = MibTable
slbCurCfgUrlLbPathTable = _SlbCurCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTable.setStatus("mandatory")
_SlbCurCfgUrlLbPathTableEntry_Object = MibTableRow
slbCurCfgUrlLbPathTableEntry = _SlbCurCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1, 1)
)
slbCurCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTableEntry.setStatus("mandatory")
_SlbCurCfgUrlLbPathIndex_Type = Integer32
_SlbCurCfgUrlLbPathIndex_Object = MibTableColumn
slbCurCfgUrlLbPathIndex = _SlbCurCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1, 1, 1),
    _SlbCurCfgUrlLbPathIndex_Type()
)
slbCurCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathIndex.setStatus("mandatory")


class _SlbCurCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlbCurCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathString_Object = MibTableColumn
slbCurCfgUrlLbPathString = _SlbCurCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1, 1, 2),
    _SlbCurCfgUrlLbPathString_Type()
)
slbCurCfgUrlLbPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathString.setStatus("mandatory")
_SlbCurCfgUrlLbBwmContract_Type = Integer32
_SlbCurCfgUrlLbBwmContract_Object = MibTableColumn
slbCurCfgUrlLbBwmContract = _SlbCurCfgUrlLbBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 1, 1, 3),
    _SlbCurCfgUrlLbBwmContract_Type()
)
slbCurCfgUrlLbBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbBwmContract.setStatus("mandatory")
_SlbNewCfgUrlLbPathTable_Object = MibTable
slbNewCfgUrlLbPathTable = _SlbNewCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTable.setStatus("mandatory")
_SlbNewCfgUrlLbPathTableEntry_Object = MibTableRow
slbNewCfgUrlLbPathTableEntry = _SlbNewCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1)
)
slbNewCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTableEntry.setStatus("mandatory")
_SlbNewCfgUrlLbPathIndex_Type = Integer32
_SlbNewCfgUrlLbPathIndex_Object = MibTableColumn
slbNewCfgUrlLbPathIndex = _SlbNewCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1, 1),
    _SlbNewCfgUrlLbPathIndex_Type()
)
slbNewCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathIndex.setStatus("mandatory")


class _SlbNewCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SlbNewCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathString_Object = MibTableColumn
slbNewCfgUrlLbPathString = _SlbNewCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1, 2),
    _SlbNewCfgUrlLbPathString_Type()
)
slbNewCfgUrlLbPathString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathString.setStatus("mandatory")


class _SlbNewCfgUrlLbPathDelete_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgUrlLbPathDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathDelete_Object = MibTableColumn
slbNewCfgUrlLbPathDelete = _SlbNewCfgUrlLbPathDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1, 3),
    _SlbNewCfgUrlLbPathDelete_Type()
)
slbNewCfgUrlLbPathDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDelete.setStatus("mandatory")
_SlbNewCfgUrlLbBwmContract_Type = Integer32
_SlbNewCfgUrlLbBwmContract_Object = MibTableColumn
slbNewCfgUrlLbBwmContract = _SlbNewCfgUrlLbBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 2, 1, 4),
    _SlbNewCfgUrlLbBwmContract_Type()
)
slbNewCfgUrlLbBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbBwmContract.setStatus("mandatory")


class _SlbCurCfgUrlLbErrorMsg_Type(DisplayString):
    """Custom type slbCurCfgUrlLbErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbCurCfgUrlLbErrorMsg_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbErrorMsg_Object = MibScalar
slbCurCfgUrlLbErrorMsg = _SlbCurCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 3),
    _SlbCurCfgUrlLbErrorMsg_Type()
)
slbCurCfgUrlLbErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbErrorMsg.setStatus("mandatory")


class _SlbNewCfgUrlLbErrorMsg_Type(DisplayString):
    """Custom type slbNewCfgUrlLbErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbNewCfgUrlLbErrorMsg_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbErrorMsg_Object = MibScalar
slbNewCfgUrlLbErrorMsg = _SlbNewCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 4),
    _SlbNewCfgUrlLbErrorMsg_Type()
)
slbNewCfgUrlLbErrorMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbErrorMsg.setStatus("mandatory")
_SlbUrlLbPathTableMaxSize_Type = Integer32
_SlbUrlLbPathTableMaxSize_Object = MibScalar
slbUrlLbPathTableMaxSize = _SlbUrlLbPathTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 2, 5),
    _SlbUrlLbPathTableMaxSize_Type()
)
slbUrlLbPathTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlLbPathTableMaxSize.setStatus("mandatory")
_RtspUrlRedir_ObjectIdentity = ObjectIdentity
rtspUrlRedir = _RtspUrlRedir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3)
)
_RtspUrlExpTableMaxSize_Type = Integer32
_RtspUrlExpTableMaxSize_Object = MibScalar
rtspUrlExpTableMaxSize = _RtspUrlExpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 1),
    _RtspUrlExpTableMaxSize_Type()
)
rtspUrlExpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspUrlExpTableMaxSize.setStatus("mandatory")
_RtspCurCfgUrlExpTable_Object = MibTable
rtspCurCfgUrlExpTable = _RtspCurCfgUrlExpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 2)
)
if mibBuilder.loadTexts:
    rtspCurCfgUrlExpTable.setStatus("mandatory")
_RtspCurCfgUrlExpTableEntry_Object = MibTableRow
rtspCurCfgUrlExpTableEntry = _RtspCurCfgUrlExpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 2, 1)
)
rtspCurCfgUrlExpTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "rtspCurCfgUrlExpIndex"),
)
if mibBuilder.loadTexts:
    rtspCurCfgUrlExpTableEntry.setStatus("mandatory")
_RtspCurCfgUrlExpIndex_Type = Integer32
_RtspCurCfgUrlExpIndex_Object = MibTableColumn
rtspCurCfgUrlExpIndex = _RtspCurCfgUrlExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 2, 1, 1),
    _RtspCurCfgUrlExpIndex_Type()
)
rtspCurCfgUrlExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspCurCfgUrlExpIndex.setStatus("mandatory")


class _RtspCurCfgUrlExpression_Type(DisplayString):
    """Custom type rtspCurCfgUrlExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RtspCurCfgUrlExpression_Type.__name__ = "DisplayString"
_RtspCurCfgUrlExpression_Object = MibTableColumn
rtspCurCfgUrlExpression = _RtspCurCfgUrlExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 2, 1, 2),
    _RtspCurCfgUrlExpression_Type()
)
rtspCurCfgUrlExpression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspCurCfgUrlExpression.setStatus("mandatory")
_RtspNewCfgUrlExpTable_Object = MibTable
rtspNewCfgUrlExpTable = _RtspNewCfgUrlExpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 3)
)
if mibBuilder.loadTexts:
    rtspNewCfgUrlExpTable.setStatus("mandatory")
_RtspNewCfgUrlExpTableEntry_Object = MibTableRow
rtspNewCfgUrlExpTableEntry = _RtspNewCfgUrlExpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 3, 1)
)
rtspNewCfgUrlExpTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "rtspNewCfgUrlExpIndex"),
)
if mibBuilder.loadTexts:
    rtspNewCfgUrlExpTableEntry.setStatus("mandatory")
_RtspNewCfgUrlExpIndex_Type = Integer32
_RtspNewCfgUrlExpIndex_Object = MibTableColumn
rtspNewCfgUrlExpIndex = _RtspNewCfgUrlExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 3, 1, 1),
    _RtspNewCfgUrlExpIndex_Type()
)
rtspNewCfgUrlExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspNewCfgUrlExpIndex.setStatus("mandatory")


class _RtspNewCfgUrlExpression_Type(DisplayString):
    """Custom type rtspNewCfgUrlExpression based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RtspNewCfgUrlExpression_Type.__name__ = "DisplayString"
_RtspNewCfgUrlExpression_Object = MibTableColumn
rtspNewCfgUrlExpression = _RtspNewCfgUrlExpression_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 3, 1, 2),
    _RtspNewCfgUrlExpression_Type()
)
rtspNewCfgUrlExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtspNewCfgUrlExpression.setStatus("mandatory")


class _RtspNewCfgUrlExpDelete_Type(Integer32):
    """Custom type rtspNewCfgUrlExpDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_RtspNewCfgUrlExpDelete_Type.__name__ = "Integer32"
_RtspNewCfgUrlExpDelete_Object = MibTableColumn
rtspNewCfgUrlExpDelete = _RtspNewCfgUrlExpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 27, 3, 3, 1, 3),
    _RtspNewCfgUrlExpDelete_Type()
)
rtspNewCfgUrlExpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtspNewCfgUrlExpDelete.setStatus("mandatory")
_SlbCurCfgPmask_Type = IpAddress
_SlbCurCfgPmask_Object = MibScalar
slbCurCfgPmask = _SlbCurCfgPmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 28),
    _SlbCurCfgPmask_Type()
)
slbCurCfgPmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPmask.setStatus("mandatory")
_SlbNewCfgPmask_Type = IpAddress
_SlbNewCfgPmask_Object = MibScalar
slbNewCfgPmask = _SlbNewCfgPmask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 29),
    _SlbNewCfgPmask_Type()
)
slbNewCfgPmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPmask.setStatus("mandatory")


class _SlbCurCfgGrace_Type(Integer32):
    """Custom type slbCurCfgGrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgGrace_Type.__name__ = "Integer32"
_SlbCurCfgGrace_Object = MibScalar
slbCurCfgGrace = _SlbCurCfgGrace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 30),
    _SlbCurCfgGrace_Type()
)
slbCurCfgGrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgGrace.setStatus("mandatory")


class _SlbNewCfgGrace_Type(Integer32):
    """Custom type slbNewCfgGrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgGrace_Type.__name__ = "Integer32"
_SlbNewCfgGrace_Object = MibScalar
slbNewCfgGrace = _SlbNewCfgGrace_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 31),
    _SlbNewCfgGrace_Type()
)
slbNewCfgGrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgGrace.setStatus("mandatory")
_SlbCurCfgPeerTable_Object = MibTable
slbCurCfgPeerTable = _SlbCurCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32)
)
if mibBuilder.loadTexts:
    slbCurCfgPeerTable.setStatus("mandatory")
_SlbCurCfgPeerEntry_Object = MibTableRow
slbCurCfgPeerEntry = _SlbCurCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1)
)
slbCurCfgPeerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgPeerEntry.setStatus("mandatory")
_SlbCurCfgPeerIndex_Type = Integer32
_SlbCurCfgPeerIndex_Object = MibTableColumn
slbCurCfgPeerIndex = _SlbCurCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1, 1),
    _SlbCurCfgPeerIndex_Type()
)
slbCurCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerIndex.setStatus("mandatory")
_SlbCurCfgPeerIpAddr_Type = IpAddress
_SlbCurCfgPeerIpAddr_Object = MibTableColumn
slbCurCfgPeerIpAddr = _SlbCurCfgPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1, 2),
    _SlbCurCfgPeerIpAddr_Type()
)
slbCurCfgPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerIpAddr.setStatus("mandatory")


class _SlbCurCfgPeerState_Type(Integer32):
    """Custom type slbCurCfgPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SlbCurCfgPeerState_Type.__name__ = "Integer32"
_SlbCurCfgPeerState_Object = MibTableColumn
slbCurCfgPeerState = _SlbCurCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 32, 1, 3),
    _SlbCurCfgPeerState_Type()
)
slbCurCfgPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgPeerState.setStatus("mandatory")
_SlbNewCfgPeerTable_Object = MibTable
slbNewCfgPeerTable = _SlbNewCfgPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33)
)
if mibBuilder.loadTexts:
    slbNewCfgPeerTable.setStatus("mandatory")
_SlbNewCfgPeerEntry_Object = MibTableRow
slbNewCfgPeerEntry = _SlbNewCfgPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1)
)
slbNewCfgPeerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgPeerIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgPeerEntry.setStatus("mandatory")
_SlbNewCfgPeerIndex_Type = Integer32
_SlbNewCfgPeerIndex_Object = MibTableColumn
slbNewCfgPeerIndex = _SlbNewCfgPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 1),
    _SlbNewCfgPeerIndex_Type()
)
slbNewCfgPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgPeerIndex.setStatus("mandatory")
_SlbNewCfgPeerIpAddr_Type = IpAddress
_SlbNewCfgPeerIpAddr_Object = MibTableColumn
slbNewCfgPeerIpAddr = _SlbNewCfgPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 2),
    _SlbNewCfgPeerIpAddr_Type()
)
slbNewCfgPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPeerIpAddr.setStatus("mandatory")


class _SlbNewCfgPeerState_Type(Integer32):
    """Custom type slbNewCfgPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SlbNewCfgPeerState_Type.__name__ = "Integer32"
_SlbNewCfgPeerState_Object = MibTableColumn
slbNewCfgPeerState = _SlbNewCfgPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 3),
    _SlbNewCfgPeerState_Type()
)
slbNewCfgPeerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPeerState.setStatus("mandatory")


class _SlbNewCfgPeerDelete_Type(Integer32):
    """Custom type slbNewCfgPeerDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgPeerDelete_Type.__name__ = "Integer32"
_SlbNewCfgPeerDelete_Object = MibTableColumn
slbNewCfgPeerDelete = _SlbNewCfgPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 33, 1, 4),
    _SlbNewCfgPeerDelete_Type()
)
slbNewCfgPeerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgPeerDelete.setStatus("mandatory")


class _SlbCurCfgSyncFilt_Type(Integer32):
    """Custom type slbCurCfgSyncFilt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgSyncFilt_Type.__name__ = "Integer32"
_SlbCurCfgSyncFilt_Object = MibScalar
slbCurCfgSyncFilt = _SlbCurCfgSyncFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 34),
    _SlbCurCfgSyncFilt_Type()
)
slbCurCfgSyncFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncFilt.setStatus("mandatory")


class _SlbNewCfgSyncFilt_Type(Integer32):
    """Custom type slbNewCfgSyncFilt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgSyncFilt_Type.__name__ = "Integer32"
_SlbNewCfgSyncFilt_Object = MibScalar
slbNewCfgSyncFilt = _SlbNewCfgSyncFilt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 35),
    _SlbNewCfgSyncFilt_Type()
)
slbNewCfgSyncFilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncFilt.setStatus("mandatory")


class _SlbCurCfgSyncPort_Type(Integer32):
    """Custom type slbCurCfgSyncPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgSyncPort_Type.__name__ = "Integer32"
_SlbCurCfgSyncPort_Object = MibScalar
slbCurCfgSyncPort = _SlbCurCfgSyncPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 36),
    _SlbCurCfgSyncPort_Type()
)
slbCurCfgSyncPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncPort.setStatus("mandatory")


class _SlbNewCfgSyncPort_Type(Integer32):
    """Custom type slbNewCfgSyncPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgSyncPort_Type.__name__ = "Integer32"
_SlbNewCfgSyncPort_Object = MibScalar
slbNewCfgSyncPort = _SlbNewCfgSyncPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 37),
    _SlbNewCfgSyncPort_Type()
)
slbNewCfgSyncPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncPort.setStatus("mandatory")


class _SlbCurCfgSyncVrrp_Type(Integer32):
    """Custom type slbCurCfgSyncVrrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgSyncVrrp_Type.__name__ = "Integer32"
_SlbCurCfgSyncVrrp_Object = MibScalar
slbCurCfgSyncVrrp = _SlbCurCfgSyncVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 38),
    _SlbCurCfgSyncVrrp_Type()
)
slbCurCfgSyncVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncVrrp.setStatus("mandatory")


class _SlbNewCfgSyncVrrp_Type(Integer32):
    """Custom type slbNewCfgSyncVrrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgSyncVrrp_Type.__name__ = "Integer32"
_SlbNewCfgSyncVrrp_Object = MibScalar
slbNewCfgSyncVrrp = _SlbNewCfgSyncVrrp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 39),
    _SlbNewCfgSyncVrrp_Type()
)
slbNewCfgSyncVrrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncVrrp.setStatus("mandatory")


class _SlbCurCfgSyncPip_Type(Integer32):
    """Custom type slbCurCfgSyncPip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgSyncPip_Type.__name__ = "Integer32"
_SlbCurCfgSyncPip_Object = MibScalar
slbCurCfgSyncPip = _SlbCurCfgSyncPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 40),
    _SlbCurCfgSyncPip_Type()
)
slbCurCfgSyncPip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncPip.setStatus("mandatory")


class _SlbNewCfgSyncPip_Type(Integer32):
    """Custom type slbNewCfgSyncPip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgSyncPip_Type.__name__ = "Integer32"
_SlbNewCfgSyncPip_Object = MibScalar
slbNewCfgSyncPip = _SlbNewCfgSyncPip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 41),
    _SlbNewCfgSyncPip_Type()
)
slbNewCfgSyncPip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncPip.setStatus("mandatory")


class _SlbCurCfgVirtMatrixArch_Type(Integer32):
    """Custom type slbCurCfgVirtMatrixArch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgVirtMatrixArch_Type.__name__ = "Integer32"
_SlbCurCfgVirtMatrixArch_Object = MibScalar
slbCurCfgVirtMatrixArch = _SlbCurCfgVirtMatrixArch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 42),
    _SlbCurCfgVirtMatrixArch_Type()
)
slbCurCfgVirtMatrixArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgVirtMatrixArch.setStatus("mandatory")


class _SlbNewCfgVirtMatrixArch_Type(Integer32):
    """Custom type slbNewCfgVirtMatrixArch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgVirtMatrixArch_Type.__name__ = "Integer32"
_SlbNewCfgVirtMatrixArch_Object = MibScalar
slbNewCfgVirtMatrixArch = _SlbNewCfgVirtMatrixArch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 43),
    _SlbNewCfgVirtMatrixArch_Type()
)
slbNewCfgVirtMatrixArch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgVirtMatrixArch.setStatus("mandatory")


class _SlbCurCfgSyncSfo_Type(Integer32):
    """Custom type slbCurCfgSyncSfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgSyncSfo_Type.__name__ = "Integer32"
_SlbCurCfgSyncSfo_Object = MibScalar
slbCurCfgSyncSfo = _SlbCurCfgSyncSfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 44),
    _SlbCurCfgSyncSfo_Type()
)
slbCurCfgSyncSfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncSfo.setStatus("mandatory")


class _SlbNewCfgSyncSfo_Type(Integer32):
    """Custom type slbNewCfgSyncSfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgSyncSfo_Type.__name__ = "Integer32"
_SlbNewCfgSyncSfo_Object = MibScalar
slbNewCfgSyncSfo = _SlbNewCfgSyncSfo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 45),
    _SlbNewCfgSyncSfo_Type()
)
slbNewCfgSyncSfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncSfo.setStatus("mandatory")


class _SlbCurCfgSyncSfoUpdatePeriod_Type(Integer32):
    """Custom type slbCurCfgSyncSfoUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SlbCurCfgSyncSfoUpdatePeriod_Type.__name__ = "Integer32"
_SlbCurCfgSyncSfoUpdatePeriod_Object = MibScalar
slbCurCfgSyncSfoUpdatePeriod = _SlbCurCfgSyncSfoUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 46),
    _SlbCurCfgSyncSfoUpdatePeriod_Type()
)
slbCurCfgSyncSfoUpdatePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncSfoUpdatePeriod.setStatus("mandatory")


class _SlbNewCfgSyncSfoUpdatePeriod_Type(Integer32):
    """Custom type slbNewCfgSyncSfoUpdatePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SlbNewCfgSyncSfoUpdatePeriod_Type.__name__ = "Integer32"
_SlbNewCfgSyncSfoUpdatePeriod_Object = MibScalar
slbNewCfgSyncSfoUpdatePeriod = _SlbNewCfgSyncSfoUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 47),
    _SlbNewCfgSyncSfoUpdatePeriod_Type()
)
slbNewCfgSyncSfoUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncSfoUpdatePeriod.setStatus("mandatory")
_SlbCurCfgRealServPortTable_Object = MibTable
slbCurCfgRealServPortTable = _SlbCurCfgRealServPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 48)
)
if mibBuilder.loadTexts:
    slbCurCfgRealServPortTable.setStatus("mandatory")
_SlbCurCfgRealServPortEntry_Object = MibTableRow
slbCurCfgRealServPortEntry = _SlbCurCfgRealServPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 48, 1)
)
slbCurCfgRealServPortEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgRealServIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgRealServPortIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgRealServPortEntry.setStatus("mandatory")
_SlbCurCfgRealServIndex_Type = Integer32
_SlbCurCfgRealServIndex_Object = MibTableColumn
slbCurCfgRealServIndex = _SlbCurCfgRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 48, 1, 1),
    _SlbCurCfgRealServIndex_Type()
)
slbCurCfgRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServIndex.setStatus("mandatory")
_SlbCurCfgRealServPortIndex_Type = Integer32
_SlbCurCfgRealServPortIndex_Object = MibTableColumn
slbCurCfgRealServPortIndex = _SlbCurCfgRealServPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 48, 1, 2),
    _SlbCurCfgRealServPortIndex_Type()
)
slbCurCfgRealServPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServPortIndex.setStatus("mandatory")


class _SlbCurCfgRealServRealPort_Type(Integer32):
    """Custom type slbCurCfgRealServRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbCurCfgRealServRealPort_Type.__name__ = "Integer32"
_SlbCurCfgRealServRealPort_Object = MibTableColumn
slbCurCfgRealServRealPort = _SlbCurCfgRealServRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 48, 1, 3),
    _SlbCurCfgRealServRealPort_Type()
)
slbCurCfgRealServRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealServRealPort.setStatus("mandatory")
_SlbNewCfgRealServPortTable_Object = MibTable
slbNewCfgRealServPortTable = _SlbNewCfgRealServPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 49)
)
if mibBuilder.loadTexts:
    slbNewCfgRealServPortTable.setStatus("mandatory")
_SlbNewCfgRealServPortEntry_Object = MibTableRow
slbNewCfgRealServPortEntry = _SlbNewCfgRealServPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 49, 1)
)
slbNewCfgRealServPortEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgRealServIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgRealServPortIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgRealServPortEntry.setStatus("mandatory")
_SlbNewCfgRealServIndex_Type = Integer32
_SlbNewCfgRealServIndex_Object = MibTableColumn
slbNewCfgRealServIndex = _SlbNewCfgRealServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 49, 1, 1),
    _SlbNewCfgRealServIndex_Type()
)
slbNewCfgRealServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServIndex.setStatus("mandatory")
_SlbNewCfgRealServPortIndex_Type = Integer32
_SlbNewCfgRealServPortIndex_Object = MibTableColumn
slbNewCfgRealServPortIndex = _SlbNewCfgRealServPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 49, 1, 2),
    _SlbNewCfgRealServPortIndex_Type()
)
slbNewCfgRealServPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgRealServPortIndex.setStatus("mandatory")


class _SlbNewCfgRealServRealPort_Type(Integer32):
    """Custom type slbNewCfgRealServRealPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_SlbNewCfgRealServRealPort_Type.__name__ = "Integer32"
_SlbNewCfgRealServRealPort_Object = MibTableColumn
slbNewCfgRealServRealPort = _SlbNewCfgRealServRealPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 49, 1, 3),
    _SlbNewCfgRealServRealPort_Type()
)
slbNewCfgRealServRealPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServRealPort.setStatus("mandatory")


class _SlbNewCfgRealServPortDelete_Type(Integer32):
    """Custom type slbNewCfgRealServPortDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgRealServPortDelete_Type.__name__ = "Integer32"
_SlbNewCfgRealServPortDelete_Object = MibTableColumn
slbNewCfgRealServPortDelete = _SlbNewCfgRealServPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 49, 1, 4),
    _SlbNewCfgRealServPortDelete_Type()
)
slbNewCfgRealServPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealServPortDelete.setStatus("mandatory")
_SlbCurCfgUrlBwmTable_Object = MibTable
slbCurCfgUrlBwmTable = _SlbCurCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 50)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmTable.setStatus("mandatory")
_SlbCurCfgUrlBwmEntry_Object = MibTableRow
slbCurCfgUrlBwmEntry = _SlbCurCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 50, 1)
)
slbCurCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgUrlBwmVirtServIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgUrlBwmVirtServiceIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmEntry.setStatus("mandatory")
_SlbCurCfgUrlBwmVirtServIndex_Type = Integer32
_SlbCurCfgUrlBwmVirtServIndex_Object = MibTableColumn
slbCurCfgUrlBwmVirtServIndex = _SlbCurCfgUrlBwmVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 50, 1, 1),
    _SlbCurCfgUrlBwmVirtServIndex_Type()
)
slbCurCfgUrlBwmVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmVirtServIndex.setStatus("mandatory")
_SlbCurCfgUrlBwmVirtServiceIndex_Type = Integer32
_SlbCurCfgUrlBwmVirtServiceIndex_Object = MibTableColumn
slbCurCfgUrlBwmVirtServiceIndex = _SlbCurCfgUrlBwmVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 50, 1, 2),
    _SlbCurCfgUrlBwmVirtServiceIndex_Type()
)
slbCurCfgUrlBwmVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmVirtServiceIndex.setStatus("mandatory")
_SlbCurCfgUrlBwmUrlId_Type = Integer32
_SlbCurCfgUrlBwmUrlId_Object = MibTableColumn
slbCurCfgUrlBwmUrlId = _SlbCurCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 50, 1, 3),
    _SlbCurCfgUrlBwmUrlId_Type()
)
slbCurCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmUrlId.setStatus("mandatory")
_SlbCurCfgUrlBwmContract_Type = Integer32
_SlbCurCfgUrlBwmContract_Object = MibTableColumn
slbCurCfgUrlBwmContract = _SlbCurCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 50, 1, 4),
    _SlbCurCfgUrlBwmContract_Type()
)
slbCurCfgUrlBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlBwmContract.setStatus("mandatory")
_SlbNewCfgUrlBwmTable_Object = MibTable
slbNewCfgUrlBwmTable = _SlbNewCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 51)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmTable.setStatus("mandatory")
_SlbNewCfgUrlBwmEntry_Object = MibTableRow
slbNewCfgUrlBwmEntry = _SlbNewCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 51, 1)
)
slbNewCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgUrlBwmVirtServIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgUrlBwmVirtServiceIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmEntry.setStatus("mandatory")
_SlbNewCfgUrlBwmVirtServIndex_Type = Integer32
_SlbNewCfgUrlBwmVirtServIndex_Object = MibTableColumn
slbNewCfgUrlBwmVirtServIndex = _SlbNewCfgUrlBwmVirtServIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 51, 1, 1),
    _SlbNewCfgUrlBwmVirtServIndex_Type()
)
slbNewCfgUrlBwmVirtServIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmVirtServIndex.setStatus("mandatory")
_SlbNewCfgUrlBwmVirtServiceIndex_Type = Integer32
_SlbNewCfgUrlBwmVirtServiceIndex_Object = MibTableColumn
slbNewCfgUrlBwmVirtServiceIndex = _SlbNewCfgUrlBwmVirtServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 51, 1, 2),
    _SlbNewCfgUrlBwmVirtServiceIndex_Type()
)
slbNewCfgUrlBwmVirtServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmVirtServiceIndex.setStatus("mandatory")
_SlbNewCfgUrlBwmUrlId_Type = Integer32
_SlbNewCfgUrlBwmUrlId_Object = MibTableColumn
slbNewCfgUrlBwmUrlId = _SlbNewCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 51, 1, 3),
    _SlbNewCfgUrlBwmUrlId_Type()
)
slbNewCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmUrlId.setStatus("mandatory")
_SlbNewCfgUrlBwmContract_Type = Integer32
_SlbNewCfgUrlBwmContract_Object = MibTableColumn
slbNewCfgUrlBwmContract = _SlbNewCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 51, 1, 4),
    _SlbNewCfgUrlBwmContract_Type()
)
slbNewCfgUrlBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmContract.setStatus("mandatory")


class _SlbNewCfgUrlBwmDelete_Type(Integer32):
    """Custom type slbNewCfgUrlBwmDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgUrlBwmDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlBwmDelete_Object = MibTableColumn
slbNewCfgUrlBwmDelete = _SlbNewCfgUrlBwmDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 51, 1, 5),
    _SlbNewCfgUrlBwmDelete_Type()
)
slbNewCfgUrlBwmDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlBwmDelete.setStatus("mandatory")
_SlbRurl_ObjectIdentity = ObjectIdentity
slbRurl = _SlbRurl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52)
)
_SlbRurlGeneral_ObjectIdentity = ObjectIdentity
slbRurlGeneral = _SlbRurlGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 1)
)


class _SlbCurCfgRurlGenDeny_Type(Integer32):
    """Custom type slbCurCfgRurlGenDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgRurlGenDeny_Type.__name__ = "Integer32"
_SlbCurCfgRurlGenDeny_Object = MibScalar
slbCurCfgRurlGenDeny = _SlbCurCfgRurlGenDeny_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 1, 1),
    _SlbCurCfgRurlGenDeny_Type()
)
slbCurCfgRurlGenDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRurlGenDeny.setStatus("mandatory")


class _SlbNewCfgRurlGenDeny_Type(Integer32):
    """Custom type slbNewCfgRurlGenDeny based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgRurlGenDeny_Type.__name__ = "Integer32"
_SlbNewCfgRurlGenDeny_Object = MibScalar
slbNewCfgRurlGenDeny = _SlbNewCfgRurlGenDeny_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 1, 2),
    _SlbNewCfgRurlGenDeny_Type()
)
slbNewCfgRurlGenDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRurlGenDeny.setStatus("mandatory")
_SlbRurlDportTableMaxSize_Type = Integer32
_SlbRurlDportTableMaxSize_Object = MibScalar
slbRurlDportTableMaxSize = _SlbRurlDportTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 2),
    _SlbRurlDportTableMaxSize_Type()
)
slbRurlDportTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRurlDportTableMaxSize.setStatus("mandatory")
_SlbCurCfgRurlDportTable_Object = MibTable
slbCurCfgRurlDportTable = _SlbCurCfgRurlDportTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 3)
)
if mibBuilder.loadTexts:
    slbCurCfgRurlDportTable.setStatus("mandatory")
_SlbCurCfgRurlDportTableEntry_Object = MibTableRow
slbCurCfgRurlDportTableEntry = _SlbCurCfgRurlDportTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 3, 1)
)
slbCurCfgRurlDportTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgRurlDportIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgRurlDportTableEntry.setStatus("mandatory")
_SlbCurCfgRurlDportIndex_Type = Integer32
_SlbCurCfgRurlDportIndex_Object = MibTableColumn
slbCurCfgRurlDportIndex = _SlbCurCfgRurlDportIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 3, 1, 1),
    _SlbCurCfgRurlDportIndex_Type()
)
slbCurCfgRurlDportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRurlDportIndex.setStatus("mandatory")


class _SlbCurCfgRurlDportLowPort_Type(Integer32):
    """Custom type slbCurCfgRurlDportLowPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgRurlDportLowPort_Type.__name__ = "Integer32"
_SlbCurCfgRurlDportLowPort_Object = MibTableColumn
slbCurCfgRurlDportLowPort = _SlbCurCfgRurlDportLowPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 3, 1, 2),
    _SlbCurCfgRurlDportLowPort_Type()
)
slbCurCfgRurlDportLowPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRurlDportLowPort.setStatus("mandatory")


class _SlbCurCfgRurlDportHighPort_Type(Integer32):
    """Custom type slbCurCfgRurlDportHighPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgRurlDportHighPort_Type.__name__ = "Integer32"
_SlbCurCfgRurlDportHighPort_Object = MibTableColumn
slbCurCfgRurlDportHighPort = _SlbCurCfgRurlDportHighPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 3, 1, 3),
    _SlbCurCfgRurlDportHighPort_Type()
)
slbCurCfgRurlDportHighPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRurlDportHighPort.setStatus("mandatory")
_SlbNewCfgRurlDportTable_Object = MibTable
slbNewCfgRurlDportTable = _SlbNewCfgRurlDportTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 4)
)
if mibBuilder.loadTexts:
    slbNewCfgRurlDportTable.setStatus("mandatory")
_SlbNewCfgRurlDportTableEntry_Object = MibTableRow
slbNewCfgRurlDportTableEntry = _SlbNewCfgRurlDportTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 4, 1)
)
slbNewCfgRurlDportTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbNewCfgRurlDportIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgRurlDportTableEntry.setStatus("mandatory")
_SlbNewCfgRurlDportIndex_Type = Integer32
_SlbNewCfgRurlDportIndex_Object = MibTableColumn
slbNewCfgRurlDportIndex = _SlbNewCfgRurlDportIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 4, 1, 1),
    _SlbNewCfgRurlDportIndex_Type()
)
slbNewCfgRurlDportIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRurlDportIndex.setStatus("mandatory")


class _SlbNewCfgRurlDportLowPort_Type(Integer32):
    """Custom type slbNewCfgRurlDportLowPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgRurlDportLowPort_Type.__name__ = "Integer32"
_SlbNewCfgRurlDportLowPort_Object = MibTableColumn
slbNewCfgRurlDportLowPort = _SlbNewCfgRurlDportLowPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 4, 1, 2),
    _SlbNewCfgRurlDportLowPort_Type()
)
slbNewCfgRurlDportLowPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRurlDportLowPort.setStatus("mandatory")


class _SlbNewCfgRurlDportHighPort_Type(Integer32):
    """Custom type slbNewCfgRurlDportHighPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgRurlDportHighPort_Type.__name__ = "Integer32"
_SlbNewCfgRurlDportHighPort_Object = MibTableColumn
slbNewCfgRurlDportHighPort = _SlbNewCfgRurlDportHighPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 4, 1, 3),
    _SlbNewCfgRurlDportHighPort_Type()
)
slbNewCfgRurlDportHighPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRurlDportHighPort.setStatus("mandatory")


class _SlbNewCfgRurlDportDelete_Type(Integer32):
    """Custom type slbNewCfgRurlDportDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_SlbNewCfgRurlDportDelete_Type.__name__ = "Integer32"
_SlbNewCfgRurlDportDelete_Object = MibTableColumn
slbNewCfgRurlDportDelete = _SlbNewCfgRurlDportDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 52, 4, 1, 4),
    _SlbNewCfgRurlDportDelete_Type()
)
slbNewCfgRurlDportDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRurlDportDelete.setStatus("mandatory")
_SlbRealServPortTableMaxSize_Type = Integer32
_SlbRealServPortTableMaxSize_Object = MibScalar
slbRealServPortTableMaxSize = _SlbRealServPortTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 53),
    _SlbRealServPortTableMaxSize_Type()
)
slbRealServPortTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServPortTableMaxSize.setStatus("mandatory")
_SlbPortTableMaxSize_Type = Integer32
_SlbPortTableMaxSize_Object = MibScalar
slbPortTableMaxSize = _SlbPortTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 54),
    _SlbPortTableMaxSize_Type()
)
slbPortTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPortTableMaxSize.setStatus("mandatory")
_SlbVirtServicesTableMaxSize_Type = Integer32
_SlbVirtServicesTableMaxSize_Object = MibScalar
slbVirtServicesTableMaxSize = _SlbVirtServicesTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 55),
    _SlbVirtServicesTableMaxSize_Type()
)
slbVirtServicesTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbVirtServicesTableMaxSize.setStatus("mandatory")
_SlbUrlBwmTableMaxSize_Type = Integer32
_SlbUrlBwmTableMaxSize_Object = MibScalar
slbUrlBwmTableMaxSize = _SlbUrlBwmTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 56),
    _SlbUrlBwmTableMaxSize_Type()
)
slbUrlBwmTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlBwmTableMaxSize.setStatus("mandatory")
_SlbPeerTableMaxSize_Type = Integer32
_SlbPeerTableMaxSize_Object = MibScalar
slbPeerTableMaxSize = _SlbPeerTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 57),
    _SlbPeerTableMaxSize_Type()
)
slbPeerTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbPeerTableMaxSize.setStatus("mandatory")


class _SlbCurCfgFastage_Type(Integer32):
    """Custom type slbCurCfgFastage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SlbCurCfgFastage_Type.__name__ = "Integer32"
_SlbCurCfgFastage_Object = MibScalar
slbCurCfgFastage = _SlbCurCfgFastage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 58),
    _SlbCurCfgFastage_Type()
)
slbCurCfgFastage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgFastage.setStatus("mandatory")


class _SlbNewCfgFastage_Type(Integer32):
    """Custom type slbNewCfgFastage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SlbNewCfgFastage_Type.__name__ = "Integer32"
_SlbNewCfgFastage_Object = MibScalar
slbNewCfgFastage = _SlbNewCfgFastage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 59),
    _SlbNewCfgFastage_Type()
)
slbNewCfgFastage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgFastage.setStatus("mandatory")


class _SlbCurCfgSlowage_Type(Integer32):
    """Custom type slbCurCfgSlowage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbCurCfgSlowage_Type.__name__ = "Integer32"
_SlbCurCfgSlowage_Object = MibScalar
slbCurCfgSlowage = _SlbCurCfgSlowage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 60),
    _SlbCurCfgSlowage_Type()
)
slbCurCfgSlowage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSlowage.setStatus("mandatory")


class _SlbNewCfgSlowage_Type(Integer32):
    """Custom type slbNewCfgSlowage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SlbNewCfgSlowage_Type.__name__ = "Integer32"
_SlbNewCfgSlowage_Object = MibScalar
slbNewCfgSlowage = _SlbNewCfgSlowage_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 61),
    _SlbNewCfgSlowage_Type()
)
slbNewCfgSlowage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSlowage.setStatus("mandatory")
_SlbWaphc_ObjectIdentity = ObjectIdentity
slbWaphc = _SlbWaphc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62)
)


class _SlbCurCfgWaphcWSPPort_Type(Integer32):
    """Custom type slbCurCfgWaphcWSPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgWaphcWSPPort_Type.__name__ = "Integer32"
_SlbCurCfgWaphcWSPPort_Object = MibScalar
slbCurCfgWaphcWSPPort = _SlbCurCfgWaphcWSPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 1),
    _SlbCurCfgWaphcWSPPort_Type()
)
slbCurCfgWaphcWSPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWSPPort.setStatus("mandatory")


class _SlbNewCfgWaphcWSPPort_Type(Integer32):
    """Custom type slbNewCfgWaphcWSPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgWaphcWSPPort_Type.__name__ = "Integer32"
_SlbNewCfgWaphcWSPPort_Object = MibScalar
slbNewCfgWaphcWSPPort = _SlbNewCfgWaphcWSPPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 2),
    _SlbNewCfgWaphcWSPPort_Type()
)
slbNewCfgWaphcWSPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWSPPort.setStatus("mandatory")


class _SlbCurCfgWaphcOffset_Type(Integer32):
    """Custom type slbCurCfgWaphcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SlbCurCfgWaphcOffset_Type.__name__ = "Integer32"
_SlbCurCfgWaphcOffset_Object = MibScalar
slbCurCfgWaphcOffset = _SlbCurCfgWaphcOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 3),
    _SlbCurCfgWaphcOffset_Type()
)
slbCurCfgWaphcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcOffset.setStatus("mandatory")


class _SlbNewCfgWaphcOffset_Type(Integer32):
    """Custom type slbNewCfgWaphcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SlbNewCfgWaphcOffset_Type.__name__ = "Integer32"
_SlbNewCfgWaphcOffset_Object = MibScalar
slbNewCfgWaphcOffset = _SlbNewCfgWaphcOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 4),
    _SlbNewCfgWaphcOffset_Type()
)
slbNewCfgWaphcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcOffset.setStatus("mandatory")


class _SlbCurCfgWaphcSndContent_Type(DisplayString):
    """Custom type slbCurCfgWaphcSndContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlbCurCfgWaphcSndContent_Type.__name__ = "DisplayString"
_SlbCurCfgWaphcSndContent_Object = MibScalar
slbCurCfgWaphcSndContent = _SlbCurCfgWaphcSndContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 5),
    _SlbCurCfgWaphcSndContent_Type()
)
slbCurCfgWaphcSndContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcSndContent.setStatus("mandatory")


class _SlbNewCfgWaphcSndContent_Type(DisplayString):
    """Custom type slbNewCfgWaphcSndContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlbNewCfgWaphcSndContent_Type.__name__ = "DisplayString"
_SlbNewCfgWaphcSndContent_Object = MibScalar
slbNewCfgWaphcSndContent = _SlbNewCfgWaphcSndContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 6),
    _SlbNewCfgWaphcSndContent_Type()
)
slbNewCfgWaphcSndContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcSndContent.setStatus("mandatory")


class _SlbCurCfgWaphcRcvContent_Type(DisplayString):
    """Custom type slbCurCfgWaphcRcvContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlbCurCfgWaphcRcvContent_Type.__name__ = "DisplayString"
_SlbCurCfgWaphcRcvContent_Object = MibScalar
slbCurCfgWaphcRcvContent = _SlbCurCfgWaphcRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 7),
    _SlbCurCfgWaphcRcvContent_Type()
)
slbCurCfgWaphcRcvContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcRcvContent.setStatus("mandatory")


class _SlbNewCfgWaphcRcvContent_Type(DisplayString):
    """Custom type slbNewCfgWaphcRcvContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlbNewCfgWaphcRcvContent_Type.__name__ = "DisplayString"
_SlbNewCfgWaphcRcvContent_Object = MibScalar
slbNewCfgWaphcRcvContent = _SlbNewCfgWaphcRcvContent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 8),
    _SlbNewCfgWaphcRcvContent_Type()
)
slbNewCfgWaphcRcvContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcRcvContent.setStatus("mandatory")


class _SlbCurCfgWaphcWTLSPort_Type(Integer32):
    """Custom type slbCurCfgWaphcWTLSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbCurCfgWaphcWTLSPort_Type.__name__ = "Integer32"
_SlbCurCfgWaphcWTLSPort_Object = MibScalar
slbCurCfgWaphcWTLSPort = _SlbCurCfgWaphcWTLSPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 9),
    _SlbCurCfgWaphcWTLSPort_Type()
)
slbCurCfgWaphcWTLSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWaphcWTLSPort.setStatus("mandatory")


class _SlbNewCfgWaphcWTLSPort_Type(Integer32):
    """Custom type slbNewCfgWaphcWTLSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SlbNewCfgWaphcWTLSPort_Type.__name__ = "Integer32"
_SlbNewCfgWaphcWTLSPort_Object = MibScalar
slbNewCfgWaphcWTLSPort = _SlbNewCfgWaphcWTLSPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 62, 10),
    _SlbNewCfgWaphcWTLSPort_Type()
)
slbNewCfgWaphcWTLSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWaphcWTLSPort.setStatus("mandatory")
_SlbWap_ObjectIdentity = ObjectIdentity
slbWap = _SlbWap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 63)
)


class _SlbCurCfgWapTpcp_Type(Integer32):
    """Custom type slbCurCfgWapTpcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgWapTpcp_Type.__name__ = "Integer32"
_SlbCurCfgWapTpcp_Object = MibScalar
slbCurCfgWapTpcp = _SlbCurCfgWapTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 63, 1),
    _SlbCurCfgWapTpcp_Type()
)
slbCurCfgWapTpcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWapTpcp.setStatus("mandatory")


class _SlbNewCfgWapTpcp_Type(Integer32):
    """Custom type slbNewCfgWapTpcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgWapTpcp_Type.__name__ = "Integer32"
_SlbNewCfgWapTpcp_Object = MibScalar
slbNewCfgWapTpcp = _SlbNewCfgWapTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 63, 2),
    _SlbNewCfgWapTpcp_Type()
)
slbNewCfgWapTpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWapTpcp.setStatus("mandatory")


class _SlbCurCfgWapDebug_Type(Integer32):
    """Custom type slbCurCfgWapDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SlbCurCfgWapDebug_Type.__name__ = "Integer32"
_SlbCurCfgWapDebug_Object = MibScalar
slbCurCfgWapDebug = _SlbCurCfgWapDebug_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 63, 3),
    _SlbCurCfgWapDebug_Type()
)
slbCurCfgWapDebug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgWapDebug.setStatus("mandatory")


class _SlbNewCfgWapDebug_Type(Integer32):
    """Custom type slbNewCfgWapDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SlbNewCfgWapDebug_Type.__name__ = "Integer32"
_SlbNewCfgWapDebug_Object = MibScalar
slbNewCfgWapDebug = _SlbNewCfgWapDebug_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 63, 4),
    _SlbNewCfgWapDebug_Type()
)
slbNewCfgWapDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgWapDebug.setStatus("mandatory")


class _SlbCurCfgSyncBwm_Type(Integer32):
    """Custom type slbCurCfgSyncBwm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgSyncBwm_Type.__name__ = "Integer32"
_SlbCurCfgSyncBwm_Object = MibScalar
slbCurCfgSyncBwm = _SlbCurCfgSyncBwm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 64),
    _SlbCurCfgSyncBwm_Type()
)
slbCurCfgSyncBwm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSyncBwm.setStatus("mandatory")


class _SlbNewCfgSyncBwm_Type(Integer32):
    """Custom type slbNewCfgSyncBwm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgSyncBwm_Type.__name__ = "Integer32"
_SlbNewCfgSyncBwm_Object = MibScalar
slbNewCfgSyncBwm = _SlbNewCfgSyncBwm_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 65),
    _SlbNewCfgSyncBwm_Type()
)
slbNewCfgSyncBwm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgSyncBwm.setStatus("mandatory")


class _SlbCurCfgTpcp_Type(Integer32):
    """Custom type slbCurCfgTpcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgTpcp_Type.__name__ = "Integer32"
_SlbCurCfgTpcp_Object = MibScalar
slbCurCfgTpcp = _SlbCurCfgTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 66),
    _SlbCurCfgTpcp_Type()
)
slbCurCfgTpcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgTpcp.setStatus("mandatory")


class _SlbNewCfgTpcp_Type(Integer32):
    """Custom type slbNewCfgTpcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgTpcp_Type.__name__ = "Integer32"
_SlbNewCfgTpcp_Object = MibScalar
slbNewCfgTpcp = _SlbNewCfgTpcp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 67),
    _SlbNewCfgTpcp_Type()
)
slbNewCfgTpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgTpcp.setStatus("mandatory")


class _SlbCurCfgMetricInterval_Type(Integer32):
    """Custom type slbCurCfgMetricInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlbCurCfgMetricInterval_Type.__name__ = "Integer32"
_SlbCurCfgMetricInterval_Object = MibScalar
slbCurCfgMetricInterval = _SlbCurCfgMetricInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 68),
    _SlbCurCfgMetricInterval_Type()
)
slbCurCfgMetricInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgMetricInterval.setStatus("mandatory")


class _SlbNewCfgMetricInterval_Type(Integer32):
    """Custom type slbNewCfgMetricInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlbNewCfgMetricInterval_Type.__name__ = "Integer32"
_SlbNewCfgMetricInterval_Object = MibScalar
slbNewCfgMetricInterval = _SlbNewCfgMetricInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 69),
    _SlbNewCfgMetricInterval_Type()
)
slbNewCfgMetricInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgMetricInterval.setStatus("mandatory")


class _SlbCurCfgRealGroupIdslb_Type(Integer32):
    """Custom type slbCurCfgRealGroupIdslb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlbCurCfgRealGroupIdslb_Type.__name__ = "Integer32"
_SlbCurCfgRealGroupIdslb_Object = MibScalar
slbCurCfgRealGroupIdslb = _SlbCurCfgRealGroupIdslb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 70),
    _SlbCurCfgRealGroupIdslb_Type()
)
slbCurCfgRealGroupIdslb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgRealGroupIdslb.setStatus("mandatory")


class _SlbNewCfgRealGroupIdslb_Type(Integer32):
    """Custom type slbNewCfgRealGroupIdslb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlbNewCfgRealGroupIdslb_Type.__name__ = "Integer32"
_SlbNewCfgRealGroupIdslb_Object = MibScalar
slbNewCfgRealGroupIdslb = _SlbNewCfgRealGroupIdslb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 71),
    _SlbNewCfgRealGroupIdslb_Type()
)
slbNewCfgRealGroupIdslb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgRealGroupIdslb.setStatus("mandatory")


class _SlbCurCfgLdapVersion_Type(Integer32):
    """Custom type slbCurCfgLdapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version2", 1),
          ("version3", 2))
    )


_SlbCurCfgLdapVersion_Type.__name__ = "Integer32"
_SlbCurCfgLdapVersion_Object = MibScalar
slbCurCfgLdapVersion = _SlbCurCfgLdapVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 72),
    _SlbCurCfgLdapVersion_Type()
)
slbCurCfgLdapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgLdapVersion.setStatus("mandatory")


class _SlbNewCfgLdapVersion_Type(Integer32):
    """Custom type slbNewCfgLdapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version2", 1),
          ("version3", 2))
    )


_SlbNewCfgLdapVersion_Type.__name__ = "Integer32"
_SlbNewCfgLdapVersion_Object = MibScalar
slbNewCfgLdapVersion = _SlbNewCfgLdapVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 73),
    _SlbNewCfgLdapVersion_Type()
)
slbNewCfgLdapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgLdapVersion.setStatus("mandatory")


class _SlbCurCfgIsdInterval_Type(Integer32):
    """Custom type slbCurCfgIsdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SlbCurCfgIsdInterval_Type.__name__ = "Integer32"
_SlbCurCfgIsdInterval_Object = MibScalar
slbCurCfgIsdInterval = _SlbCurCfgIsdInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 74),
    _SlbCurCfgIsdInterval_Type()
)
slbCurCfgIsdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgIsdInterval.setStatus("mandatory")


class _SlbNewCfgIsdInterval_Type(Integer32):
    """Custom type slbNewCfgIsdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SlbNewCfgIsdInterval_Type.__name__ = "Integer32"
_SlbNewCfgIsdInterval_Object = MibScalar
slbNewCfgIsdInterval = _SlbNewCfgIsdInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 75),
    _SlbNewCfgIsdInterval_Type()
)
slbNewCfgIsdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgIsdInterval.setStatus("mandatory")


class _SlbCurCfgIsdRetry_Type(Integer32):
    """Custom type slbCurCfgIsdRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgIsdRetry_Type.__name__ = "Integer32"
_SlbCurCfgIsdRetry_Object = MibScalar
slbCurCfgIsdRetry = _SlbCurCfgIsdRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 76),
    _SlbCurCfgIsdRetry_Type()
)
slbCurCfgIsdRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgIsdRetry.setStatus("mandatory")


class _SlbNewCfgIsdRetry_Type(Integer32):
    """Custom type slbNewCfgIsdRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgIsdRetry_Type.__name__ = "Integer32"
_SlbNewCfgIsdRetry_Object = MibScalar
slbNewCfgIsdRetry = _SlbNewCfgIsdRetry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 77),
    _SlbNewCfgIsdRetry_Type()
)
slbNewCfgIsdRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgIsdRetry.setStatus("mandatory")


class _SlbCurCfgIsdRestr_Type(Integer32):
    """Custom type slbCurCfgIsdRestr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbCurCfgIsdRestr_Type.__name__ = "Integer32"
_SlbCurCfgIsdRestr_Object = MibScalar
slbCurCfgIsdRestr = _SlbCurCfgIsdRestr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 78),
    _SlbCurCfgIsdRestr_Type()
)
slbCurCfgIsdRestr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgIsdRestr.setStatus("mandatory")


class _SlbNewCfgIsdRestr_Type(Integer32):
    """Custom type slbNewCfgIsdRestr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SlbNewCfgIsdRestr_Type.__name__ = "Integer32"
_SlbNewCfgIsdRestr_Object = MibScalar
slbNewCfgIsdRestr = _SlbNewCfgIsdRestr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 79),
    _SlbNewCfgIsdRestr_Type()
)
slbNewCfgIsdRestr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgIsdRestr.setStatus("mandatory")


class _SlbCurCfgIsdNumber_Type(Integer32):
    """Custom type slbCurCfgIsdNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SlbCurCfgIsdNumber_Type.__name__ = "Integer32"
_SlbCurCfgIsdNumber_Object = MibScalar
slbCurCfgIsdNumber = _SlbCurCfgIsdNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 80),
    _SlbCurCfgIsdNumber_Type()
)
slbCurCfgIsdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgIsdNumber.setStatus("mandatory")


class _SlbNewCfgIsdNumber_Type(Integer32):
    """Custom type slbNewCfgIsdNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SlbNewCfgIsdNumber_Type.__name__ = "Integer32"
_SlbNewCfgIsdNumber_Object = MibScalar
slbNewCfgIsdNumber = _SlbNewCfgIsdNumber_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 81),
    _SlbNewCfgIsdNumber_Type()
)
slbNewCfgIsdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgIsdNumber.setStatus("mandatory")
_SynAttackDetCfg_ObjectIdentity = ObjectIdentity
synAttackDetCfg = _SynAttackDetCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 82)
)


class _SynAttackCurCfgInterval_Type(Integer32):
    """Custom type synAttackCurCfgInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_SynAttackCurCfgInterval_Type.__name__ = "Integer32"
_SynAttackCurCfgInterval_Object = MibScalar
synAttackCurCfgInterval = _SynAttackCurCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 82, 1),
    _SynAttackCurCfgInterval_Type()
)
synAttackCurCfgInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAttackCurCfgInterval.setStatus("mandatory")


class _SynAttackNewCfgInterval_Type(Integer32):
    """Custom type synAttackNewCfgInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_SynAttackNewCfgInterval_Type.__name__ = "Integer32"
_SynAttackNewCfgInterval_Object = MibScalar
synAttackNewCfgInterval = _SynAttackNewCfgInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 82, 2),
    _SynAttackNewCfgInterval_Type()
)
synAttackNewCfgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synAttackNewCfgInterval.setStatus("mandatory")


class _SynAttackCurCfgThreshhold_Type(Integer32):
    """Custom type synAttackCurCfgThreshhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_SynAttackCurCfgThreshhold_Type.__name__ = "Integer32"
_SynAttackCurCfgThreshhold_Object = MibScalar
synAttackCurCfgThreshhold = _SynAttackCurCfgThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 82, 3),
    _SynAttackCurCfgThreshhold_Type()
)
synAttackCurCfgThreshhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synAttackCurCfgThreshhold.setStatus("mandatory")


class _SynAttackNewCfgThreshhold_Type(Integer32):
    """Custom type synAttackNewCfgThreshhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_SynAttackNewCfgThreshhold_Type.__name__ = "Integer32"
_SynAttackNewCfgThreshhold_Object = MibScalar
synAttackNewCfgThreshhold = _SynAttackNewCfgThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 82, 4),
    _SynAttackNewCfgThreshhold_Type()
)
synAttackNewCfgThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synAttackNewCfgThreshhold.setStatus("mandatory")


class _SlbCurCfgTcpTimeWindow_Type(Integer32):
    """Custom type slbCurCfgTcpTimeWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlbCurCfgTcpTimeWindow_Type.__name__ = "Integer32"
_SlbCurCfgTcpTimeWindow_Object = MibScalar
slbCurCfgTcpTimeWindow = _SlbCurCfgTcpTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 83),
    _SlbCurCfgTcpTimeWindow_Type()
)
slbCurCfgTcpTimeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgTcpTimeWindow.setStatus("mandatory")


class _SlbNewCfgTcpTimeWindow_Type(Integer32):
    """Custom type slbNewCfgTcpTimeWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlbNewCfgTcpTimeWindow_Type.__name__ = "Integer32"
_SlbNewCfgTcpTimeWindow_Object = MibScalar
slbNewCfgTcpTimeWindow = _SlbNewCfgTcpTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 84),
    _SlbNewCfgTcpTimeWindow_Type()
)
slbNewCfgTcpTimeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgTcpTimeWindow.setStatus("mandatory")


class _SlbCurCfgTcpHoldDuration_Type(Integer32):
    """Custom type slbCurCfgTcpHoldDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlbCurCfgTcpHoldDuration_Type.__name__ = "Integer32"
_SlbCurCfgTcpHoldDuration_Object = MibScalar
slbCurCfgTcpHoldDuration = _SlbCurCfgTcpHoldDuration_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 85),
    _SlbCurCfgTcpHoldDuration_Type()
)
slbCurCfgTcpHoldDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgTcpHoldDuration.setStatus("mandatory")


class _SlbNewCfgTcpHoldDuration_Type(Integer32):
    """Custom type slbNewCfgTcpHoldDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlbNewCfgTcpHoldDuration_Type.__name__ = "Integer32"
_SlbNewCfgTcpHoldDuration_Object = MibScalar
slbNewCfgTcpHoldDuration = _SlbNewCfgTcpHoldDuration_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 86),
    _SlbNewCfgTcpHoldDuration_Type()
)
slbNewCfgTcpHoldDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgTcpHoldDuration.setStatus("mandatory")


class _SlbCurCfgAllowHttpHc_Type(Integer32):
    """Custom type slbCurCfgAllowHttpHc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbCurCfgAllowHttpHc_Type.__name__ = "Integer32"
_SlbCurCfgAllowHttpHc_Object = MibScalar
slbCurCfgAllowHttpHc = _SlbCurCfgAllowHttpHc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 87),
    _SlbCurCfgAllowHttpHc_Type()
)
slbCurCfgAllowHttpHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgAllowHttpHc.setStatus("mandatory")


class _SlbNewCfgAllowHttpHc_Type(Integer32):
    """Custom type slbNewCfgAllowHttpHc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlbNewCfgAllowHttpHc_Type.__name__ = "Integer32"
_SlbNewCfgAllowHttpHc_Object = MibScalar
slbNewCfgAllowHttpHc = _SlbNewCfgAllowHttpHc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 5, 88),
    _SlbNewCfgAllowHttpHc_Type()
)
slbNewCfgAllowHttpHc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgAllowHttpHc.setStatus("mandatory")
_SlbStats_ObjectIdentity = ObjectIdentity
slbStats = _SlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2)
)
_SlbStatPortMaintTable_Object = MibTable
slbStatPortMaintTable = _SlbStatPortMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    slbStatPortMaintTable.setStatus("mandatory")
_SlbStatPortMaintEntry_Object = MibTableRow
slbStatPortMaintEntry = _SlbStatPortMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1)
)
slbStatPortMaintEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbStatPortMaintPortIndex"),
)
if mibBuilder.loadTexts:
    slbStatPortMaintEntry.setStatus("mandatory")
_SlbStatPortMaintPortIndex_Type = Integer32
_SlbStatPortMaintPortIndex_Object = MibTableColumn
slbStatPortMaintPortIndex = _SlbStatPortMaintPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 1),
    _SlbStatPortMaintPortIndex_Type()
)
slbStatPortMaintPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintPortIndex.setStatus("mandatory")
_SlbStatPortMaintCurBindings_Type = Gauge32
_SlbStatPortMaintCurBindings_Object = MibTableColumn
slbStatPortMaintCurBindings = _SlbStatPortMaintCurBindings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 2),
    _SlbStatPortMaintCurBindings_Type()
)
slbStatPortMaintCurBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintCurBindings.setStatus("mandatory")
_SlbStatPortMaintBindingFails_Type = Counter32
_SlbStatPortMaintBindingFails_Object = MibTableColumn
slbStatPortMaintBindingFails = _SlbStatPortMaintBindingFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 3),
    _SlbStatPortMaintBindingFails_Type()
)
slbStatPortMaintBindingFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintBindingFails.setStatus("mandatory")
_SlbStatPortMaintNonTcpFrames_Type = Counter32
_SlbStatPortMaintNonTcpFrames_Object = MibTableColumn
slbStatPortMaintNonTcpFrames = _SlbStatPortMaintNonTcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 4),
    _SlbStatPortMaintNonTcpFrames_Type()
)
slbStatPortMaintNonTcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintNonTcpFrames.setStatus("mandatory")
_SlbStatPortMaintTcpFragments_Type = Counter32
_SlbStatPortMaintTcpFragments_Object = MibTableColumn
slbStatPortMaintTcpFragments = _SlbStatPortMaintTcpFragments_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 5),
    _SlbStatPortMaintTcpFragments_Type()
)
slbStatPortMaintTcpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintTcpFragments.setStatus("mandatory")
_SlbStatPortMaintUdpDatagrams_Type = Counter32
_SlbStatPortMaintUdpDatagrams_Object = MibTableColumn
slbStatPortMaintUdpDatagrams = _SlbStatPortMaintUdpDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 6),
    _SlbStatPortMaintUdpDatagrams_Type()
)
slbStatPortMaintUdpDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintUdpDatagrams.setStatus("mandatory")
_SlbStatPortMaintIncorrectVIPs_Type = Counter32
_SlbStatPortMaintIncorrectVIPs_Object = MibTableColumn
slbStatPortMaintIncorrectVIPs = _SlbStatPortMaintIncorrectVIPs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 7),
    _SlbStatPortMaintIncorrectVIPs_Type()
)
slbStatPortMaintIncorrectVIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintIncorrectVIPs.setStatus("mandatory")
_SlbStatPortMaintIncorrectVports_Type = Counter32
_SlbStatPortMaintIncorrectVports_Object = MibTableColumn
slbStatPortMaintIncorrectVports = _SlbStatPortMaintIncorrectVports_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 8),
    _SlbStatPortMaintIncorrectVports_Type()
)
slbStatPortMaintIncorrectVports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintIncorrectVports.setStatus("mandatory")
_SlbStatPortMaintRealServerNoAvails_Type = Counter32
_SlbStatPortMaintRealServerNoAvails_Object = MibTableColumn
slbStatPortMaintRealServerNoAvails = _SlbStatPortMaintRealServerNoAvails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 9),
    _SlbStatPortMaintRealServerNoAvails_Type()
)
slbStatPortMaintRealServerNoAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintRealServerNoAvails.setStatus("mandatory")
_SlbStatPortMaintFilteredDeniedFrames_Type = Counter32
_SlbStatPortMaintFilteredDeniedFrames_Object = MibTableColumn
slbStatPortMaintFilteredDeniedFrames = _SlbStatPortMaintFilteredDeniedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 10),
    _SlbStatPortMaintFilteredDeniedFrames_Type()
)
slbStatPortMaintFilteredDeniedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintFilteredDeniedFrames.setStatus("mandatory")
_SlbStatPortMaintCurBindings4Seconds_Type = Gauge32
_SlbStatPortMaintCurBindings4Seconds_Object = MibTableColumn
slbStatPortMaintCurBindings4Seconds = _SlbStatPortMaintCurBindings4Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 11),
    _SlbStatPortMaintCurBindings4Seconds_Type()
)
slbStatPortMaintCurBindings4Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintCurBindings4Seconds.setStatus("mandatory")
_SlbStatPortMaintCurBindings64Seconds_Type = Gauge32
_SlbStatPortMaintCurBindings64Seconds_Object = MibTableColumn
slbStatPortMaintCurBindings64Seconds = _SlbStatPortMaintCurBindings64Seconds_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 12),
    _SlbStatPortMaintCurBindings64Seconds_Type()
)
slbStatPortMaintCurBindings64Seconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintCurBindings64Seconds.setStatus("mandatory")
_SlbStatPortMaintVMAdiscards_Type = Counter32
_SlbStatPortMaintVMAdiscards_Object = MibTableColumn
slbStatPortMaintVMAdiscards = _SlbStatPortMaintVMAdiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 1, 1, 13),
    _SlbStatPortMaintVMAdiscards_Type()
)
slbStatPortMaintVMAdiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortMaintVMAdiscards.setStatus("mandatory")
_SlbStatPortRealServerTable_Object = MibTable
slbStatPortRealServerTable = _SlbStatPortRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    slbStatPortRealServerTable.setStatus("mandatory")
_SlbStatPortRealServerEntry_Object = MibTableRow
slbStatPortRealServerEntry = _SlbStatPortRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1)
)
slbStatPortRealServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbStatPortRealServerPortIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "slbStatPortRealServerServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatPortRealServerEntry.setStatus("mandatory")
_SlbStatPortRealServerPortIndex_Type = Integer32
_SlbStatPortRealServerPortIndex_Object = MibTableColumn
slbStatPortRealServerPortIndex = _SlbStatPortRealServerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 1),
    _SlbStatPortRealServerPortIndex_Type()
)
slbStatPortRealServerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerPortIndex.setStatus("mandatory")
_SlbStatPortRealServerServerIndex_Type = Integer32
_SlbStatPortRealServerServerIndex_Object = MibTableColumn
slbStatPortRealServerServerIndex = _SlbStatPortRealServerServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 2),
    _SlbStatPortRealServerServerIndex_Type()
)
slbStatPortRealServerServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerServerIndex.setStatus("mandatory")
_SlbStatPortRealServerCurrSessions_Type = Gauge32
_SlbStatPortRealServerCurrSessions_Object = MibTableColumn
slbStatPortRealServerCurrSessions = _SlbStatPortRealServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 3),
    _SlbStatPortRealServerCurrSessions_Type()
)
slbStatPortRealServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerCurrSessions.setStatus("mandatory")
_SlbStatPortRealServerTotalSessions_Type = Counter32
_SlbStatPortRealServerTotalSessions_Object = MibTableColumn
slbStatPortRealServerTotalSessions = _SlbStatPortRealServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 4),
    _SlbStatPortRealServerTotalSessions_Type()
)
slbStatPortRealServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerTotalSessions.setStatus("mandatory")
_SlbStatPortRealServerHCOctets_Type = Counter64
_SlbStatPortRealServerHCOctets_Object = MibTableColumn
slbStatPortRealServerHCOctets = _SlbStatPortRealServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 5),
    _SlbStatPortRealServerHCOctets_Type()
)
slbStatPortRealServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerHCOctets.setStatus("obsolete")
_SlbStatPortRealServerHCOctetsLow32_Type = Counter32
_SlbStatPortRealServerHCOctetsLow32_Object = MibTableColumn
slbStatPortRealServerHCOctetsLow32 = _SlbStatPortRealServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 6),
    _SlbStatPortRealServerHCOctetsLow32_Type()
)
slbStatPortRealServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerHCOctetsLow32.setStatus("mandatory")
_SlbStatPortRealServerHCOctetsHigh32_Type = Counter32
_SlbStatPortRealServerHCOctetsHigh32_Object = MibTableColumn
slbStatPortRealServerHCOctetsHigh32 = _SlbStatPortRealServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 2, 1, 7),
    _SlbStatPortRealServerHCOctetsHigh32_Type()
)
slbStatPortRealServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatPortRealServerHCOctetsHigh32.setStatus("mandatory")
_SlbStatMaintBackupServActs_Type = Counter32
_SlbStatMaintBackupServActs_Object = MibScalar
slbStatMaintBackupServActs = _SlbStatMaintBackupServActs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 3),
    _SlbStatMaintBackupServActs_Type()
)
slbStatMaintBackupServActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintBackupServActs.setStatus("mandatory")
_SlbStatMaintOverflowServActs_Type = Counter32
_SlbStatMaintOverflowServActs_Object = MibScalar
slbStatMaintOverflowServActs = _SlbStatMaintOverflowServActs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 4),
    _SlbStatMaintOverflowServActs_Type()
)
slbStatMaintOverflowServActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatMaintOverflowServActs.setStatus("mandatory")
_SlbStatRServerTable_Object = MibTable
slbStatRServerTable = _SlbStatRServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5)
)
if mibBuilder.loadTexts:
    slbStatRServerTable.setStatus("mandatory")
_SlbStatRServerEntry_Object = MibTableRow
slbStatRServerEntry = _SlbStatRServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1)
)
slbStatRServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbStatRServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatRServerEntry.setStatus("mandatory")
_SlbStatRServerIndex_Type = Integer32
_SlbStatRServerIndex_Object = MibTableColumn
slbStatRServerIndex = _SlbStatRServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 1),
    _SlbStatRServerIndex_Type()
)
slbStatRServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerIndex.setStatus("mandatory")
_SlbStatRServerCurrSessions_Type = Gauge32
_SlbStatRServerCurrSessions_Object = MibTableColumn
slbStatRServerCurrSessions = _SlbStatRServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 2),
    _SlbStatRServerCurrSessions_Type()
)
slbStatRServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerCurrSessions.setStatus("mandatory")
_SlbStatRServerTotalSessions_Type = Counter32
_SlbStatRServerTotalSessions_Object = MibTableColumn
slbStatRServerTotalSessions = _SlbStatRServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 3),
    _SlbStatRServerTotalSessions_Type()
)
slbStatRServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerTotalSessions.setStatus("mandatory")
_SlbStatRServerFailures_Type = Counter32
_SlbStatRServerFailures_Object = MibTableColumn
slbStatRServerFailures = _SlbStatRServerFailures_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 4),
    _SlbStatRServerFailures_Type()
)
slbStatRServerFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerFailures.setStatus("mandatory")
_SlbStatRServerHighestSessions_Type = Counter32
_SlbStatRServerHighestSessions_Object = MibTableColumn
slbStatRServerHighestSessions = _SlbStatRServerHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 5),
    _SlbStatRServerHighestSessions_Type()
)
slbStatRServerHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHighestSessions.setStatus("mandatory")
_SlbStatRServerHCOctets_Type = Counter64
_SlbStatRServerHCOctets_Object = MibTableColumn
slbStatRServerHCOctets = _SlbStatRServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 6),
    _SlbStatRServerHCOctets_Type()
)
slbStatRServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctets.setStatus("obsolete")
_SlbStatRServerHCOctetsLow32_Type = Counter32
_SlbStatRServerHCOctetsLow32_Object = MibTableColumn
slbStatRServerHCOctetsLow32 = _SlbStatRServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 7),
    _SlbStatRServerHCOctetsLow32_Type()
)
slbStatRServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctetsLow32.setStatus("mandatory")
_SlbStatRServerHCOctetsHigh32_Type = Counter32
_SlbStatRServerHCOctetsHigh32_Object = MibTableColumn
slbStatRServerHCOctetsHigh32 = _SlbStatRServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 5, 1, 8),
    _SlbStatRServerHCOctetsHigh32_Type()
)
slbStatRServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatRServerHCOctetsHigh32.setStatus("mandatory")
_SlbStatGroupTable_Object = MibTable
slbStatGroupTable = _SlbStatGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6)
)
if mibBuilder.loadTexts:
    slbStatGroupTable.setStatus("mandatory")
_SlbStatGroupEntry_Object = MibTableRow
slbStatGroupEntry = _SlbStatGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1)
)
slbStatGroupEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbStatGroupIndex"),
)
if mibBuilder.loadTexts:
    slbStatGroupEntry.setStatus("mandatory")
_SlbStatGroupIndex_Type = Integer32
_SlbStatGroupIndex_Object = MibTableColumn
slbStatGroupIndex = _SlbStatGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 1),
    _SlbStatGroupIndex_Type()
)
slbStatGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupIndex.setStatus("mandatory")
_SlbStatGroupCurrSessions_Type = Gauge32
_SlbStatGroupCurrSessions_Object = MibTableColumn
slbStatGroupCurrSessions = _SlbStatGroupCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 2),
    _SlbStatGroupCurrSessions_Type()
)
slbStatGroupCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupCurrSessions.setStatus("mandatory")
_SlbStatGroupTotalSessions_Type = Counter32
_SlbStatGroupTotalSessions_Object = MibTableColumn
slbStatGroupTotalSessions = _SlbStatGroupTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 3),
    _SlbStatGroupTotalSessions_Type()
)
slbStatGroupTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupTotalSessions.setStatus("mandatory")
_SlbStatGroupHighestSessions_Type = Counter32
_SlbStatGroupHighestSessions_Object = MibTableColumn
slbStatGroupHighestSessions = _SlbStatGroupHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 4),
    _SlbStatGroupHighestSessions_Type()
)
slbStatGroupHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHighestSessions.setStatus("mandatory")
_SlbStatGroupHCOctets_Type = Counter64
_SlbStatGroupHCOctets_Object = MibTableColumn
slbStatGroupHCOctets = _SlbStatGroupHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 5),
    _SlbStatGroupHCOctets_Type()
)
slbStatGroupHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctets.setStatus("obsolete")
_SlbStatGroupHCOctetsLow32_Type = Counter32
_SlbStatGroupHCOctetsLow32_Object = MibTableColumn
slbStatGroupHCOctetsLow32 = _SlbStatGroupHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 6),
    _SlbStatGroupHCOctetsLow32_Type()
)
slbStatGroupHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctetsLow32.setStatus("mandatory")
_SlbStatGroupHCOctetsHigh32_Type = Counter32
_SlbStatGroupHCOctetsHigh32_Object = MibTableColumn
slbStatGroupHCOctetsHigh32 = _SlbStatGroupHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 6, 1, 7),
    _SlbStatGroupHCOctetsHigh32_Type()
)
slbStatGroupHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatGroupHCOctetsHigh32.setStatus("mandatory")
_SlbStatVServerTable_Object = MibTable
slbStatVServerTable = _SlbStatVServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7)
)
if mibBuilder.loadTexts:
    slbStatVServerTable.setStatus("mandatory")
_SlbStatVServerEntry_Object = MibTableRow
slbStatVServerEntry = _SlbStatVServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1)
)
slbStatVServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbStatVServerIndex"),
)
if mibBuilder.loadTexts:
    slbStatVServerEntry.setStatus("mandatory")
_SlbStatVServerIndex_Type = Integer32
_SlbStatVServerIndex_Object = MibTableColumn
slbStatVServerIndex = _SlbStatVServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 1),
    _SlbStatVServerIndex_Type()
)
slbStatVServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerIndex.setStatus("mandatory")
_SlbStatVServerCurrSessions_Type = Gauge32
_SlbStatVServerCurrSessions_Object = MibTableColumn
slbStatVServerCurrSessions = _SlbStatVServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 2),
    _SlbStatVServerCurrSessions_Type()
)
slbStatVServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerCurrSessions.setStatus("mandatory")
_SlbStatVServerTotalSessions_Type = Counter32
_SlbStatVServerTotalSessions_Object = MibTableColumn
slbStatVServerTotalSessions = _SlbStatVServerTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 3),
    _SlbStatVServerTotalSessions_Type()
)
slbStatVServerTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerTotalSessions.setStatus("mandatory")
_SlbStatVServerHighestSessions_Type = Counter32
_SlbStatVServerHighestSessions_Object = MibTableColumn
slbStatVServerHighestSessions = _SlbStatVServerHighestSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 4),
    _SlbStatVServerHighestSessions_Type()
)
slbStatVServerHighestSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHighestSessions.setStatus("mandatory")
_SlbStatVServerHCOctets_Type = Counter64
_SlbStatVServerHCOctets_Object = MibTableColumn
slbStatVServerHCOctets = _SlbStatVServerHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 5),
    _SlbStatVServerHCOctets_Type()
)
slbStatVServerHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctets.setStatus("obsolete")
_SlbStatVServerHCOctetsLow32_Type = Counter32
_SlbStatVServerHCOctetsLow32_Object = MibTableColumn
slbStatVServerHCOctetsLow32 = _SlbStatVServerHCOctetsLow32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 6),
    _SlbStatVServerHCOctetsLow32_Type()
)
slbStatVServerHCOctetsLow32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctetsLow32.setStatus("mandatory")
_SlbStatVServerHCOctetsHigh32_Type = Counter32
_SlbStatVServerHCOctetsHigh32_Object = MibTableColumn
slbStatVServerHCOctetsHigh32 = _SlbStatVServerHCOctetsHigh32_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 7),
    _SlbStatVServerHCOctetsHigh32_Type()
)
slbStatVServerHCOctetsHigh32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHCOctetsHigh32.setStatus("mandatory")
_SlbStatVServerHeaderHits_Type = Counter32
_SlbStatVServerHeaderHits_Object = MibTableColumn
slbStatVServerHeaderHits = _SlbStatVServerHeaderHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 8),
    _SlbStatVServerHeaderHits_Type()
)
slbStatVServerHeaderHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderHits.setStatus("mandatory")
_SlbStatVServerHeaderMisses_Type = Counter32
_SlbStatVServerHeaderMisses_Object = MibTableColumn
slbStatVServerHeaderMisses = _SlbStatVServerHeaderMisses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 9),
    _SlbStatVServerHeaderMisses_Type()
)
slbStatVServerHeaderMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderMisses.setStatus("mandatory")
_SlbStatVServerHeaderTotalSessions_Type = Counter32
_SlbStatVServerHeaderTotalSessions_Object = MibTableColumn
slbStatVServerHeaderTotalSessions = _SlbStatVServerHeaderTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 10),
    _SlbStatVServerHeaderTotalSessions_Type()
)
slbStatVServerHeaderTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerHeaderTotalSessions.setStatus("mandatory")
_SlbStatVServerCookieRewrites_Type = Counter32
_SlbStatVServerCookieRewrites_Object = MibTableColumn
slbStatVServerCookieRewrites = _SlbStatVServerCookieRewrites_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 11),
    _SlbStatVServerCookieRewrites_Type()
)
slbStatVServerCookieRewrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerCookieRewrites.setStatus("mandatory")
_SlbStatVServerCookieInserts_Type = Counter32
_SlbStatVServerCookieInserts_Object = MibTableColumn
slbStatVServerCookieInserts = _SlbStatVServerCookieInserts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 7, 1, 12),
    _SlbStatVServerCookieInserts_Type()
)
slbStatVServerCookieInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbStatVServerCookieInserts.setStatus("mandatory")
_SlbMaintStats_ObjectIdentity = ObjectIdentity
slbMaintStats = _SlbMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8)
)
_SlbIncorrectVirtServs_Type = Counter32
_SlbIncorrectVirtServs_Object = MibScalar
slbIncorrectVirtServs = _SlbIncorrectVirtServs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 1),
    _SlbIncorrectVirtServs_Type()
)
slbIncorrectVirtServs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbIncorrectVirtServs.setStatus("mandatory")
_SlbIncorrectVports_Type = Counter32
_SlbIncorrectVports_Object = MibScalar
slbIncorrectVports = _SlbIncorrectVports_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 2),
    _SlbIncorrectVports_Type()
)
slbIncorrectVports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbIncorrectVports.setStatus("mandatory")
_SlbNoRealServs_Type = Counter32
_SlbNoRealServs_Object = MibScalar
slbNoRealServs = _SlbNoRealServs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 3),
    _SlbNoRealServs_Type()
)
slbNoRealServs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNoRealServs.setStatus("mandatory")
_WapMaintStats_ObjectIdentity = ObjectIdentity
wapMaintStats = _WapMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4)
)
_RadiusAcctReqsStats_ObjectIdentity = ObjectIdentity
radiusAcctReqsStats = _RadiusAcctReqsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1)
)
_RadiusAcctReqs_Type = Counter32
_RadiusAcctReqs_Object = MibScalar
radiusAcctReqs = _RadiusAcctReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 1),
    _RadiusAcctReqs_Type()
)
radiusAcctReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqs.setStatus("mandatory")
_RadiusAcctWrapReqs_Type = Counter32
_RadiusAcctWrapReqs_Object = MibScalar
radiusAcctWrapReqs = _RadiusAcctWrapReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 2),
    _RadiusAcctWrapReqs_Type()
)
radiusAcctWrapReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctWrapReqs.setStatus("mandatory")
_RadiusAcctStartReqs_Type = Counter32
_RadiusAcctStartReqs_Object = MibScalar
radiusAcctStartReqs = _RadiusAcctStartReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 3),
    _RadiusAcctStartReqs_Type()
)
radiusAcctStartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctStartReqs.setStatus("mandatory")
_RadiusAcctUpdateReqs_Type = Counter32
_RadiusAcctUpdateReqs_Object = MibScalar
radiusAcctUpdateReqs = _RadiusAcctUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 4),
    _RadiusAcctUpdateReqs_Type()
)
radiusAcctUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctUpdateReqs.setStatus("mandatory")
_RadiusAcctStopReqs_Type = Counter32
_RadiusAcctStopReqs_Object = MibScalar
radiusAcctStopReqs = _RadiusAcctStopReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 5),
    _RadiusAcctStopReqs_Type()
)
radiusAcctStopReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctStopReqs.setStatus("mandatory")
_RadiusAcctBadReqs_Type = Counter32
_RadiusAcctBadReqs_Object = MibScalar
radiusAcctBadReqs = _RadiusAcctBadReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 6),
    _RadiusAcctBadReqs_Type()
)
radiusAcctBadReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctBadReqs.setStatus("mandatory")
_RadiusAcctAddSessionReqs_Type = Counter32
_RadiusAcctAddSessionReqs_Object = MibScalar
radiusAcctAddSessionReqs = _RadiusAcctAddSessionReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 7),
    _RadiusAcctAddSessionReqs_Type()
)
radiusAcctAddSessionReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctAddSessionReqs.setStatus("mandatory")
_RadiusAcctDeleteSessionReqs_Type = Counter32
_RadiusAcctDeleteSessionReqs_Object = MibScalar
radiusAcctDeleteSessionReqs = _RadiusAcctDeleteSessionReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 8),
    _RadiusAcctDeleteSessionReqs_Type()
)
radiusAcctDeleteSessionReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctDeleteSessionReqs.setStatus("mandatory")
_RadiusAcctReqFailsQFull_Type = Counter32
_RadiusAcctReqFailsQFull_Object = MibScalar
radiusAcctReqFailsQFull = _RadiusAcctReqFailsQFull_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 9),
    _RadiusAcctReqFailsQFull_Type()
)
radiusAcctReqFailsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqFailsQFull.setStatus("mandatory")
_RadiusAcctReqFailsSPDead_Type = Counter32
_RadiusAcctReqFailsSPDead_Object = MibScalar
radiusAcctReqFailsSPDead = _RadiusAcctReqFailsSPDead_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 10),
    _RadiusAcctReqFailsSPDead_Type()
)
radiusAcctReqFailsSPDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqFailsSPDead.setStatus("mandatory")
_RadiusAcctReqFailsDMAFails_Type = Counter32
_RadiusAcctReqFailsDMAFails_Object = MibScalar
radiusAcctReqFailsDMAFails = _RadiusAcctReqFailsDMAFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 11),
    _RadiusAcctReqFailsDMAFails_Type()
)
radiusAcctReqFailsDMAFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctReqFailsDMAFails.setStatus("mandatory")
_RadiusAcctMaxEntriesInUse_Type = Counter32
_RadiusAcctMaxEntriesInUse_Object = MibScalar
radiusAcctMaxEntriesInUse = _RadiusAcctMaxEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 1, 12),
    _RadiusAcctMaxEntriesInUse_Type()
)
radiusAcctMaxEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctMaxEntriesInUse.setStatus("mandatory")
_TpcpAddSessReqsStats_ObjectIdentity = ObjectIdentity
tpcpAddSessReqsStats = _TpcpAddSessReqsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 2)
)
_TpcpAddSessReqs_Type = Counter32
_TpcpAddSessReqs_Object = MibScalar
tpcpAddSessReqs = _TpcpAddSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 2, 1),
    _TpcpAddSessReqs_Type()
)
tpcpAddSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpAddSessReqs.setStatus("mandatory")
_TpcpAddSessReqsFailsQFull_Type = Counter32
_TpcpAddSessReqsFailsQFull_Object = MibScalar
tpcpAddSessReqsFailsQFull = _TpcpAddSessReqsFailsQFull_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 2, 2),
    _TpcpAddSessReqsFailsQFull_Type()
)
tpcpAddSessReqsFailsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpAddSessReqsFailsQFull.setStatus("mandatory")
_TpcpAddSessReqsFailsSPDead_Type = Counter32
_TpcpAddSessReqsFailsSPDead_Object = MibScalar
tpcpAddSessReqsFailsSPDead = _TpcpAddSessReqsFailsSPDead_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 2, 3),
    _TpcpAddSessReqsFailsSPDead_Type()
)
tpcpAddSessReqsFailsSPDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpAddSessReqsFailsSPDead.setStatus("mandatory")
_TpcpAddSessReqsEntriesInUse_Type = Counter32
_TpcpAddSessReqsEntriesInUse_Object = MibScalar
tpcpAddSessReqsEntriesInUse = _TpcpAddSessReqsEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 2, 4),
    _TpcpAddSessReqsEntriesInUse_Type()
)
tpcpAddSessReqsEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpAddSessReqsEntriesInUse.setStatus("mandatory")
_TpcpAddSessReqsMaxEntriesInUse_Type = Counter32
_TpcpAddSessReqsMaxEntriesInUse_Object = MibScalar
tpcpAddSessReqsMaxEntriesInUse = _TpcpAddSessReqsMaxEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 2, 5),
    _TpcpAddSessReqsMaxEntriesInUse_Type()
)
tpcpAddSessReqsMaxEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpAddSessReqsMaxEntriesInUse.setStatus("mandatory")
_TpcpDeleteSessReqsStats_ObjectIdentity = ObjectIdentity
tpcpDeleteSessReqsStats = _TpcpDeleteSessReqsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 3)
)
_TpcpDeleteSessReqs_Type = Counter32
_TpcpDeleteSessReqs_Object = MibScalar
tpcpDeleteSessReqs = _TpcpDeleteSessReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 3, 1),
    _TpcpDeleteSessReqs_Type()
)
tpcpDeleteSessReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpDeleteSessReqs.setStatus("mandatory")
_TpcpDeleteSessReqsFailsQFull_Type = Counter32
_TpcpDeleteSessReqsFailsQFull_Object = MibScalar
tpcpDeleteSessReqsFailsQFull = _TpcpDeleteSessReqsFailsQFull_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 3, 2),
    _TpcpDeleteSessReqsFailsQFull_Type()
)
tpcpDeleteSessReqsFailsQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpDeleteSessReqsFailsQFull.setStatus("mandatory")
_TpcpDeleteSessReqsFailsSPDead_Type = Counter32
_TpcpDeleteSessReqsFailsSPDead_Object = MibScalar
tpcpDeleteSessReqsFailsSPDead = _TpcpDeleteSessReqsFailsSPDead_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 3, 3),
    _TpcpDeleteSessReqsFailsSPDead_Type()
)
tpcpDeleteSessReqsFailsSPDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpDeleteSessReqsFailsSPDead.setStatus("mandatory")
_TpcpDeleteSessReqsEntriesInUse_Type = Counter32
_TpcpDeleteSessReqsEntriesInUse_Object = MibScalar
tpcpDeleteSessReqsEntriesInUse = _TpcpDeleteSessReqsEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 3, 4),
    _TpcpDeleteSessReqsEntriesInUse_Type()
)
tpcpDeleteSessReqsEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpDeleteSessReqsEntriesInUse.setStatus("mandatory")
_TpcpDeleteSessReqsMaxEntriesInUse_Type = Counter32
_TpcpDeleteSessReqsMaxEntriesInUse_Object = MibScalar
tpcpDeleteSessReqsMaxEntriesInUse = _TpcpDeleteSessReqsMaxEntriesInUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 3, 5),
    _TpcpDeleteSessReqsMaxEntriesInUse_Type()
)
tpcpDeleteSessReqsMaxEntriesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpcpDeleteSessReqsMaxEntriesInUse.setStatus("mandatory")
_WapRequestToWrongSP_Type = Counter32
_WapRequestToWrongSP_Object = MibScalar
wapRequestToWrongSP = _WapRequestToWrongSP_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 2, 8, 4, 4),
    _WapRequestToWrongSP_Type()
)
wapRequestToWrongSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wapRequestToWrongSP.setStatus("mandatory")
_FilterStats_ObjectIdentity = ObjectIdentity
filterStats = _FilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6)
)
_FltStatTable_Object = MibTable
fltStatTable = _FltStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1)
)
if mibBuilder.loadTexts:
    fltStatTable.setStatus("mandatory")
_FltStatTableEntry_Object = MibTableRow
fltStatTableEntry = _FltStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1, 1)
)
fltStatTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "fltStatFltIndex"),
)
if mibBuilder.loadTexts:
    fltStatTableEntry.setStatus("mandatory")
_FltStatFltIndex_Type = Integer32
_FltStatFltIndex_Object = MibTableColumn
fltStatFltIndex = _FltStatFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1, 1, 1),
    _FltStatFltIndex_Type()
)
fltStatFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatFltIndex.setStatus("mandatory")
_FltStatFltFirings_Type = Counter32
_FltStatFltFirings_Object = MibTableColumn
fltStatFltFirings = _FltStatFltFirings_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 6, 1, 1, 2),
    _FltStatFltFirings_Type()
)
fltStatFltFirings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltStatFltFirings.setStatus("mandatory")
_GslbStats_ObjectIdentity = ObjectIdentity
gslbStats = _GslbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7)
)
_GslbStatRemRealServerTable_Object = MibTable
gslbStatRemRealServerTable = _GslbStatRemRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1)
)
if mibBuilder.loadTexts:
    gslbStatRemRealServerTable.setStatus("mandatory")
_GslbStatRemRealServerEntry_Object = MibTableRow
gslbStatRemRealServerEntry = _GslbStatRemRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1)
)
gslbStatRemRealServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "gslbStatRemRealServerIndex"),
)
if mibBuilder.loadTexts:
    gslbStatRemRealServerEntry.setStatus("mandatory")
_GslbStatRemRealServerIndex_Type = Integer32
_GslbStatRemRealServerIndex_Object = MibTableColumn
gslbStatRemRealServerIndex = _GslbStatRemRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1, 1),
    _GslbStatRemRealServerIndex_Type()
)
gslbStatRemRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerIndex.setStatus("mandatory")
_GslbStatRemRealServerDnsHandoffs_Type = Counter32
_GslbStatRemRealServerDnsHandoffs_Object = MibTableColumn
gslbStatRemRealServerDnsHandoffs = _GslbStatRemRealServerDnsHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1, 2),
    _GslbStatRemRealServerDnsHandoffs_Type()
)
gslbStatRemRealServerDnsHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerDnsHandoffs.setStatus("mandatory")
_GslbStatRemRealServerHttpRedirs_Type = Counter32
_GslbStatRemRealServerHttpRedirs_Object = MibTableColumn
gslbStatRemRealServerHttpRedirs = _GslbStatRemRealServerHttpRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 7, 1, 1, 3),
    _GslbStatRemRealServerHttpRedirs_Type()
)
gslbStatRemRealServerHttpRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatRemRealServerHttpRedirs.setStatus("mandatory")
_GslbMaintStats_ObjectIdentity = ObjectIdentity
gslbMaintStats = _GslbMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 8)
)
_GslbStatMaintInGoodSiteUpdates_Type = Counter32
_GslbStatMaintInGoodSiteUpdates_Object = MibScalar
gslbStatMaintInGoodSiteUpdates = _GslbStatMaintInGoodSiteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 8, 1),
    _GslbStatMaintInGoodSiteUpdates_Type()
)
gslbStatMaintInGoodSiteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInGoodSiteUpdates.setStatus("mandatory")
_GslbStatMaintInBadSiteUpdates_Type = Counter32
_GslbStatMaintInBadSiteUpdates_Object = MibScalar
gslbStatMaintInBadSiteUpdates = _GslbStatMaintInBadSiteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 8, 2),
    _GslbStatMaintInBadSiteUpdates_Type()
)
gslbStatMaintInBadSiteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbStatMaintInBadSiteUpdates.setStatus("mandatory")
_UrlStats_ObjectIdentity = ObjectIdentity
urlStats = _UrlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10)
)
_UrlRedirStats_ObjectIdentity = ObjectIdentity
urlRedirStats = _UrlRedirStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1)
)
_UrlStatRedRedirs_Type = Counter32
_UrlStatRedRedirs_Object = MibScalar
urlStatRedRedirs = _UrlStatRedRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 1),
    _UrlStatRedRedirs_Type()
)
urlStatRedRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRedirs.setStatus("mandatory")
_UrlStatRedOrigSrvs_Type = Counter32
_UrlStatRedOrigSrvs_Object = MibScalar
urlStatRedOrigSrvs = _UrlStatRedOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 2),
    _UrlStatRedOrigSrvs_Type()
)
urlStatRedOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedOrigSrvs.setStatus("mandatory")
_UrlStatRedNonGets_Type = Counter32
_UrlStatRedNonGets_Object = MibScalar
urlStatRedNonGets = _UrlStatRedNonGets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 3),
    _UrlStatRedNonGets_Type()
)
urlStatRedNonGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNonGets.setStatus("mandatory")
_UrlStatRedCookie_Type = Counter32
_UrlStatRedCookie_Object = MibScalar
urlStatRedCookie = _UrlStatRedCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 4),
    _UrlStatRedCookie_Type()
)
urlStatRedCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedCookie.setStatus("mandatory")
_UrlStatRedNoCache_Type = Counter32
_UrlStatRedNoCache_Object = MibScalar
urlStatRedNoCache = _UrlStatRedNoCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 1, 5),
    _UrlStatRedNoCache_Type()
)
urlStatRedNoCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNoCache.setStatus("mandatory")
_UrlSlbStats_ObjectIdentity = ObjectIdentity
urlSlbStats = _UrlSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2)
)
_UrlStatSlbPathTable_Object = MibTable
urlStatSlbPathTable = _UrlStatSlbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1)
)
if mibBuilder.loadTexts:
    urlStatSlbPathTable.setStatus("mandatory")
_UrlStatSlbPathTableEntry_Object = MibTableRow
urlStatSlbPathTableEntry = _UrlStatSlbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1, 1)
)
urlStatSlbPathTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbCurCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    urlStatSlbPathTableEntry.setStatus("mandatory")
_UrlStatSlbPathIndex_Type = Integer32
_UrlStatSlbPathIndex_Object = MibTableColumn
urlStatSlbPathIndex = _UrlStatSlbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1, 1, 1),
    _UrlStatSlbPathIndex_Type()
)
urlStatSlbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathIndex.setStatus("mandatory")
_UrlStatSlbPathHits_Type = Counter32
_UrlStatSlbPathHits_Object = MibTableColumn
urlStatSlbPathHits = _UrlStatSlbPathHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 10, 2, 1, 1, 2),
    _UrlStatSlbPathHits_Type()
)
urlStatSlbPathHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathHits.setStatus("mandatory")
_TcpStats_ObjectIdentity = ObjectIdentity
tcpStats = _TcpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 11)
)
_TcpStatCurConns_Type = Gauge32
_TcpStatCurConns_Object = MibScalar
tcpStatCurConns = _TcpStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 11, 1),
    _TcpStatCurConns_Type()
)
tcpStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpStatCurConns.setStatus("mandatory")
_TcpStatHalfOpens_Type = Gauge32
_TcpStatHalfOpens_Object = MibScalar
tcpStatHalfOpens = _TcpStatHalfOpens_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 11, 2),
    _TcpStatHalfOpens_Type()
)
tcpStatHalfOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpStatHalfOpens.setStatus("mandatory")
_FtpStats_ObjectIdentity = ObjectIdentity
ftpStats = _FtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14)
)
_FtpSlbStats_ObjectIdentity = ObjectIdentity
ftpSlbStats = _FtpSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14, 1)
)
_FtpSlbStatTotal_Type = Counter32
_FtpSlbStatTotal_Object = MibScalar
ftpSlbStatTotal = _FtpSlbStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14, 1, 1),
    _FtpSlbStatTotal_Type()
)
ftpSlbStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpSlbStatTotal.setStatus("mandatory")
_FtpNatStatTotal_Type = Counter32
_FtpNatStatTotal_Object = MibScalar
ftpNatStatTotal = _FtpNatStatTotal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 14, 1, 2),
    _FtpNatStatTotal_Type()
)
ftpNatStatTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpNatStatTotal.setStatus("mandatory")
_RurlStats_ObjectIdentity = ObjectIdentity
rurlStats = _RurlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18)
)
_RurlErrorStats_ObjectIdentity = ObjectIdentity
rurlErrorStats = _RurlErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1)
)
_RurlErrorStatConnect_Type = Counter32
_RurlErrorStatConnect_Object = MibScalar
rurlErrorStatConnect = _RurlErrorStatConnect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1, 1),
    _RurlErrorStatConnect_Type()
)
rurlErrorStatConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlErrorStatConnect.setStatus("mandatory")
_RurlErrorStatPack_Type = Counter32
_RurlErrorStatPack_Object = MibScalar
rurlErrorStatPack = _RurlErrorStatPack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1, 2),
    _RurlErrorStatPack_Type()
)
rurlErrorStatPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlErrorStatPack.setStatus("mandatory")
_RurlErrorStatUnpack_Type = Counter32
_RurlErrorStatUnpack_Object = MibScalar
rurlErrorStatUnpack = _RurlErrorStatUnpack_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1, 3),
    _RurlErrorStatUnpack_Type()
)
rurlErrorStatUnpack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlErrorStatUnpack.setStatus("mandatory")
_RurlErrorStatDma_Type = Counter32
_RurlErrorStatDma_Object = MibScalar
rurlErrorStatDma = _RurlErrorStatDma_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1, 4),
    _RurlErrorStatDma_Type()
)
rurlErrorStatDma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlErrorStatDma.setStatus("mandatory")
_RurlErrorStatBuf_Type = Counter32
_RurlErrorStatBuf_Object = MibScalar
rurlErrorStatBuf = _RurlErrorStatBuf_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1, 5),
    _RurlErrorStatBuf_Type()
)
rurlErrorStatBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlErrorStatBuf.setStatus("mandatory")
_RurlErrorStatBufWrap_Type = Counter32
_RurlErrorStatBufWrap_Object = MibScalar
rurlErrorStatBufWrap = _RurlErrorStatBufWrap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1, 6),
    _RurlErrorStatBufWrap_Type()
)
rurlErrorStatBufWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlErrorStatBufWrap.setStatus("mandatory")
_RurlErrorStatProto_Type = Counter32
_RurlErrorStatProto_Object = MibScalar
rurlErrorStatProto = _RurlErrorStatProto_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 1, 7),
    _RurlErrorStatProto_Type()
)
rurlErrorStatProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlErrorStatProto.setStatus("mandatory")
_RurlInfoStats_ObjectIdentity = ObjectIdentity
rurlInfoStats = _RurlInfoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2)
)
_RurlInfoStatClientWrap_Type = Counter32
_RurlInfoStatClientWrap_Object = MibScalar
rurlInfoStatClientWrap = _RurlInfoStatClientWrap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 1),
    _RurlInfoStatClientWrap_Type()
)
rurlInfoStatClientWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientWrap.setStatus("mandatory")
_RurlInfoStatServerWrap_Type = Counter32
_RurlInfoStatServerWrap_Object = MibScalar
rurlInfoStatServerWrap = _RurlInfoStatServerWrap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 2),
    _RurlInfoStatServerWrap_Type()
)
rurlInfoStatServerWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerWrap.setStatus("mandatory")
_RurlInfoStatBufWrap_Type = Counter32
_RurlInfoStatBufWrap_Object = MibScalar
rurlInfoStatBufWrap = _RurlInfoStatBufWrap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 3),
    _RurlInfoStatBufWrap_Type()
)
rurlInfoStatBufWrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatBufWrap.setStatus("mandatory")
_RurlInfoStatFreeRingCalls_Type = Counter32
_RurlInfoStatFreeRingCalls_Object = MibScalar
rurlInfoStatFreeRingCalls = _RurlInfoStatFreeRingCalls_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 4),
    _RurlInfoStatFreeRingCalls_Type()
)
rurlInfoStatFreeRingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatFreeRingCalls.setStatus("mandatory")
_RurlInfoStatClientResets_Type = Counter32
_RurlInfoStatClientResets_Object = MibScalar
rurlInfoStatClientResets = _RurlInfoStatClientResets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 5),
    _RurlInfoStatClientResets_Type()
)
rurlInfoStatClientResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientResets.setStatus("mandatory")
_RurlInfoStatServerResets_Type = Counter32
_RurlInfoStatServerResets_Object = MibScalar
rurlInfoStatServerResets = _RurlInfoStatServerResets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 6),
    _RurlInfoStatServerResets_Type()
)
rurlInfoStatServerResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerResets.setStatus("mandatory")
_RurlInfoStatFramePassThru_Type = Counter32
_RurlInfoStatFramePassThru_Object = MibScalar
rurlInfoStatFramePassThru = _RurlInfoStatFramePassThru_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 7),
    _RurlInfoStatFramePassThru_Type()
)
rurlInfoStatFramePassThru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatFramePassThru.setStatus("mandatory")
_RurlInfoStatParseFiltMiss_Type = Counter32
_RurlInfoStatParseFiltMiss_Object = MibScalar
rurlInfoStatParseFiltMiss = _RurlInfoStatParseFiltMiss_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 8),
    _RurlInfoStatParseFiltMiss_Type()
)
rurlInfoStatParseFiltMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatParseFiltMiss.setStatus("mandatory")
_RurlInfoStatExceedBufLen_Type = Counter32
_RurlInfoStatExceedBufLen_Object = MibScalar
rurlInfoStatExceedBufLen = _RurlInfoStatExceedBufLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 9),
    _RurlInfoStatExceedBufLen_Type()
)
rurlInfoStatExceedBufLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatExceedBufLen.setStatus("mandatory")
_RurlInfoStatExceedFrameDepth_Type = Counter32
_RurlInfoStatExceedFrameDepth_Object = MibScalar
rurlInfoStatExceedFrameDepth = _RurlInfoStatExceedFrameDepth_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 10),
    _RurlInfoStatExceedFrameDepth_Type()
)
rurlInfoStatExceedFrameDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatExceedFrameDepth.setStatus("mandatory")
_RurlInfoStatZeroContentLen_Type = Counter32
_RurlInfoStatZeroContentLen_Object = MibScalar
rurlInfoStatZeroContentLen = _RurlInfoStatZeroContentLen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 11),
    _RurlInfoStatZeroContentLen_Type()
)
rurlInfoStatZeroContentLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatZeroContentLen.setStatus("mandatory")
_RurlInfoStatNonTypicalOffsets_Type = Counter32
_RurlInfoStatNonTypicalOffsets_Object = MibScalar
rurlInfoStatNonTypicalOffsets = _RurlInfoStatNonTypicalOffsets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 12),
    _RurlInfoStatNonTypicalOffsets_Type()
)
rurlInfoStatNonTypicalOffsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatNonTypicalOffsets.setStatus("mandatory")
_RurlInfoStatFINRSTSessSetup_Type = Counter32
_RurlInfoStatFINRSTSessSetup_Object = MibScalar
rurlInfoStatFINRSTSessSetup = _RurlInfoStatFINRSTSessSetup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 13),
    _RurlInfoStatFINRSTSessSetup_Type()
)
rurlInfoStatFINRSTSessSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatFINRSTSessSetup.setStatus("mandatory")
_RurlInfoStatPSHSessSetup_Type = Counter32
_RurlInfoStatPSHSessSetup_Object = MibScalar
rurlInfoStatPSHSessSetup = _RurlInfoStatPSHSessSetup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 14),
    _RurlInfoStatPSHSessSetup_Type()
)
rurlInfoStatPSHSessSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatPSHSessSetup.setStatus("mandatory")
_RurlInfoStatNonSYNSessSetup_Type = Counter32
_RurlInfoStatNonSYNSessSetup_Object = MibScalar
rurlInfoStatNonSYNSessSetup = _RurlInfoStatNonSYNSessSetup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 15),
    _RurlInfoStatNonSYNSessSetup_Type()
)
rurlInfoStatNonSYNSessSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatNonSYNSessSetup.setStatus("mandatory")
_RurlInfoStatL7BindCalls_Type = Counter32
_RurlInfoStatL7BindCalls_Object = MibScalar
rurlInfoStatL7BindCalls = _RurlInfoStatL7BindCalls_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 16),
    _RurlInfoStatL7BindCalls_Type()
)
rurlInfoStatL7BindCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatL7BindCalls.setStatus("mandatory")
_RurlInfoStatSessSetups_Type = Counter32
_RurlInfoStatSessSetups_Object = MibScalar
rurlInfoStatSessSetups = _RurlInfoStatSessSetups_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 17),
    _RurlInfoStatSessSetups_Type()
)
rurlInfoStatSessSetups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatSessSetups.setStatus("mandatory")
_RurlInfoStatMiscProcess_Type = Counter32
_RurlInfoStatMiscProcess_Object = MibScalar
rurlInfoStatMiscProcess = _RurlInfoStatMiscProcess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 18),
    _RurlInfoStatMiscProcess_Type()
)
rurlInfoStatMiscProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatMiscProcess.setStatus("mandatory")
_RurlInfoStatClientPktsIn_Type = Counter32
_RurlInfoStatClientPktsIn_Object = MibScalar
rurlInfoStatClientPktsIn = _RurlInfoStatClientPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 19),
    _RurlInfoStatClientPktsIn_Type()
)
rurlInfoStatClientPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientPktsIn.setStatus("mandatory")
_RurlInfoStatClientSYNsIn_Type = Counter32
_RurlInfoStatClientSYNsIn_Object = MibScalar
rurlInfoStatClientSYNsIn = _RurlInfoStatClientSYNsIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 20),
    _RurlInfoStatClientSYNsIn_Type()
)
rurlInfoStatClientSYNsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientSYNsIn.setStatus("mandatory")
_RurlInfoStatClientReTXSYNsSeen_Type = Counter32
_RurlInfoStatClientReTXSYNsSeen_Object = MibScalar
rurlInfoStatClientReTXSYNsSeen = _RurlInfoStatClientReTXSYNsSeen_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 21),
    _RurlInfoStatClientReTXSYNsSeen_Type()
)
rurlInfoStatClientReTXSYNsSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientReTXSYNsSeen.setStatus("mandatory")
_RurlInfoStatClientSYNACKsSent_Type = Counter32
_RurlInfoStatClientSYNACKsSent_Object = MibScalar
rurlInfoStatClientSYNACKsSent = _RurlInfoStatClientSYNACKsSent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 22),
    _RurlInfoStatClientSYNACKsSent_Type()
)
rurlInfoStatClientSYNACKsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientSYNACKsSent.setStatus("mandatory")
_RurlInfoStatClientACKsIn_Type = Counter32
_RurlInfoStatClientACKsIn_Object = MibScalar
rurlInfoStatClientACKsIn = _RurlInfoStatClientACKsIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 23),
    _RurlInfoStatClientACKsIn_Type()
)
rurlInfoStatClientACKsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientACKsIn.setStatus("mandatory")
_RurlInfoStatClientDataIn_Type = Counter32
_RurlInfoStatClientDataIn_Object = MibScalar
rurlInfoStatClientDataIn = _RurlInfoStatClientDataIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 24),
    _RurlInfoStatClientDataIn_Type()
)
rurlInfoStatClientDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientDataIn.setStatus("mandatory")
_RurlInfoStatClientDataRetx_Type = Counter32
_RurlInfoStatClientDataRetx_Object = MibScalar
rurlInfoStatClientDataRetx = _RurlInfoStatClientDataRetx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 25),
    _RurlInfoStatClientDataRetx_Type()
)
rurlInfoStatClientDataRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatClientDataRetx.setStatus("mandatory")
_RurlInfoStatServerSYNsSent_Type = Counter32
_RurlInfoStatServerSYNsSent_Object = MibScalar
rurlInfoStatServerSYNsSent = _RurlInfoStatServerSYNsSent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 26),
    _RurlInfoStatServerSYNsSent_Type()
)
rurlInfoStatServerSYNsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerSYNsSent.setStatus("mandatory")
_RurlInfoStatServerSYNACKsIn_Type = Counter32
_RurlInfoStatServerSYNACKsIn_Object = MibScalar
rurlInfoStatServerSYNACKsIn = _RurlInfoStatServerSYNACKsIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 27),
    _RurlInfoStatServerSYNACKsIn_Type()
)
rurlInfoStatServerSYNACKsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerSYNACKsIn.setStatus("mandatory")
_RurlInfoStatServerACKsSent_Type = Counter32
_RurlInfoStatServerACKsSent_Object = MibScalar
rurlInfoStatServerACKsSent = _RurlInfoStatServerACKsSent_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 28),
    _RurlInfoStatServerACKsSent_Type()
)
rurlInfoStatServerACKsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerACKsSent.setStatus("mandatory")
_RurlInfoStatServerACKsIn_Type = Counter32
_RurlInfoStatServerACKsIn_Object = MibScalar
rurlInfoStatServerACKsIn = _RurlInfoStatServerACKsIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 29),
    _RurlInfoStatServerACKsIn_Type()
)
rurlInfoStatServerACKsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerACKsIn.setStatus("mandatory")
_RurlInfoStatServerSYNsRetx_Type = Counter32
_RurlInfoStatServerSYNsRetx_Object = MibScalar
rurlInfoStatServerSYNsRetx = _RurlInfoStatServerSYNsRetx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 30),
    _RurlInfoStatServerSYNsRetx_Type()
)
rurlInfoStatServerSYNsRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerSYNsRetx.setStatus("mandatory")
_RurlInfoStatServerSYNsRetxErrors_Type = Counter32
_RurlInfoStatServerSYNsRetxErrors_Object = MibScalar
rurlInfoStatServerSYNsRetxErrors = _RurlInfoStatServerSYNsRetxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 31),
    _RurlInfoStatServerSYNsRetxErrors_Type()
)
rurlInfoStatServerSYNsRetxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatServerSYNsRetxErrors.setStatus("mandatory")
_RurlInfoStatL7SessionReuse_Type = Counter32
_RurlInfoStatL7SessionReuse_Object = MibScalar
rurlInfoStatL7SessionReuse = _RurlInfoStatL7SessionReuse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 32),
    _RurlInfoStatL7SessionReuse_Type()
)
rurlInfoStatL7SessionReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatL7SessionReuse.setStatus("mandatory")
_RurlInfoStatConnSpliced_Type = Counter32
_RurlInfoStatConnSpliced_Object = MibScalar
rurlInfoStatConnSpliced = _RurlInfoStatConnSpliced_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 2, 33),
    _RurlInfoStatConnSpliced_Type()
)
rurlInfoStatConnSpliced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlInfoStatConnSpliced.setStatus("mandatory")
_RurlMaintStats_ObjectIdentity = ObjectIdentity
rurlMaintStats = _RurlMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3)
)
_RurlMaintStatOrgServerHits_Type = Counter32
_RurlMaintStatOrgServerHits_Object = MibScalar
rurlMaintStatOrgServerHits = _RurlMaintStatOrgServerHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 1),
    _RurlMaintStatOrgServerHits_Type()
)
rurlMaintStatOrgServerHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatOrgServerHits.setStatus("mandatory")
_RurlMaintStatHTTPRedirs_Type = Counter32
_RurlMaintStatHTTPRedirs_Object = MibScalar
rurlMaintStatHTTPRedirs = _RurlMaintStatHTTPRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 2),
    _RurlMaintStatHTTPRedirs_Type()
)
rurlMaintStatHTTPRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatHTTPRedirs.setStatus("mandatory")
_RurlMaintStatServerReqs_Type = Counter32
_RurlMaintStatServerReqs_Object = MibScalar
rurlMaintStatServerReqs = _RurlMaintStatServerReqs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 3),
    _RurlMaintStatServerReqs_Type()
)
rurlMaintStatServerReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatServerReqs.setStatus("mandatory")
_RurlMaintStatServerAcks_Type = Counter32
_RurlMaintStatServerAcks_Object = MibScalar
rurlMaintStatServerAcks = _RurlMaintStatServerAcks_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 4),
    _RurlMaintStatServerAcks_Type()
)
rurlMaintStatServerAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatServerAcks.setStatus("mandatory")
_RurlMaintStatSessCnt_Type = Counter32
_RurlMaintStatSessCnt_Object = MibScalar
rurlMaintStatSessCnt = _RurlMaintStatSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 5),
    _RurlMaintStatSessCnt_Type()
)
rurlMaintStatSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatSessCnt.setStatus("mandatory")
_RurlMaintStatLastFrameCnt_Type = Counter32
_RurlMaintStatLastFrameCnt_Object = MibScalar
rurlMaintStatLastFrameCnt = _RurlMaintStatLastFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 6),
    _RurlMaintStatLastFrameCnt_Type()
)
rurlMaintStatLastFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatLastFrameCnt.setStatus("mandatory")
_RurlMaintStatConnectRxmit_Type = Counter32
_RurlMaintStatConnectRxmit_Object = MibScalar
rurlMaintStatConnectRxmit = _RurlMaintStatConnectRxmit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 7),
    _RurlMaintStatConnectRxmit_Type()
)
rurlMaintStatConnectRxmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatConnectRxmit.setStatus("mandatory")
_RurlMaintStatResetRxmit_Type = Counter32
_RurlMaintStatResetRxmit_Object = MibScalar
rurlMaintStatResetRxmit = _RurlMaintStatResetRxmit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 8),
    _RurlMaintStatResetRxmit_Type()
)
rurlMaintStatResetRxmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatResetRxmit.setStatus("mandatory")
_RurlMaintStatCurRdirIPEntries_Type = Gauge32
_RurlMaintStatCurRdirIPEntries_Object = MibScalar
rurlMaintStatCurRdirIPEntries = _RurlMaintStatCurRdirIPEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 9),
    _RurlMaintStatCurRdirIPEntries_Type()
)
rurlMaintStatCurRdirIPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatCurRdirIPEntries.setStatus("mandatory")
_RurlMaintStatHighRdirIPEntries_Type = Counter32
_RurlMaintStatHighRdirIPEntries_Object = MibScalar
rurlMaintStatHighRdirIPEntries = _RurlMaintStatHighRdirIPEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 10),
    _RurlMaintStatHighRdirIPEntries_Type()
)
rurlMaintStatHighRdirIPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatHighRdirIPEntries.setStatus("mandatory")
_RurlMaintStatCurRdirPORTEntries_Type = Gauge32
_RurlMaintStatCurRdirPORTEntries_Object = MibScalar
rurlMaintStatCurRdirPORTEntries = _RurlMaintStatCurRdirPORTEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 11),
    _RurlMaintStatCurRdirPORTEntries_Type()
)
rurlMaintStatCurRdirPORTEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatCurRdirPORTEntries.setStatus("mandatory")
_RurlMaintStatHighRdirPORTEntries_Type = Counter32
_RurlMaintStatHighRdirPORTEntries_Object = MibScalar
rurlMaintStatHighRdirPORTEntries = _RurlMaintStatHighRdirPORTEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 12),
    _RurlMaintStatHighRdirPORTEntries_Type()
)
rurlMaintStatHighRdirPORTEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatHighRdirPORTEntries.setStatus("mandatory")
_RurlMaintStatCurRdirIPPORTEntries_Type = Gauge32
_RurlMaintStatCurRdirIPPORTEntries_Object = MibScalar
rurlMaintStatCurRdirIPPORTEntries = _RurlMaintStatCurRdirIPPORTEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 13),
    _RurlMaintStatCurRdirIPPORTEntries_Type()
)
rurlMaintStatCurRdirIPPORTEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatCurRdirIPPORTEntries.setStatus("mandatory")
_RurlMaintStatHighRdirIPPORTEntries_Type = Counter32
_RurlMaintStatHighRdirIPPORTEntries_Object = MibScalar
rurlMaintStatHighRdirIPPORTEntries = _RurlMaintStatHighRdirIPPORTEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 14),
    _RurlMaintStatHighRdirIPPORTEntries_Type()
)
rurlMaintStatHighRdirIPPORTEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatHighRdirIPPORTEntries.setStatus("mandatory")
_RurlMaintStatCurRSEQBufEntries_Type = Gauge32
_RurlMaintStatCurRSEQBufEntries_Object = MibScalar
rurlMaintStatCurRSEQBufEntries = _RurlMaintStatCurRSEQBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 15),
    _RurlMaintStatCurRSEQBufEntries_Type()
)
rurlMaintStatCurRSEQBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatCurRSEQBufEntries.setStatus("mandatory")
_RurlMaintStatHighRSEQBufEntries_Type = Counter32
_RurlMaintStatHighRSEQBufEntries_Object = MibScalar
rurlMaintStatHighRSEQBufEntries = _RurlMaintStatHighRSEQBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 16),
    _RurlMaintStatHighRSEQBufEntries_Type()
)
rurlMaintStatHighRSEQBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatHighRSEQBufEntries.setStatus("mandatory")
_RurlMaintStatCurRBUFBufEntries_Type = Gauge32
_RurlMaintStatCurRBUFBufEntries_Object = MibScalar
rurlMaintStatCurRBUFBufEntries = _RurlMaintStatCurRBUFBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 17),
    _RurlMaintStatCurRBUFBufEntries_Type()
)
rurlMaintStatCurRBUFBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatCurRBUFBufEntries.setStatus("mandatory")
_RurlMaintStatHighRBUFBufEntries_Type = Counter32
_RurlMaintStatHighRBUFBufEntries_Object = MibScalar
rurlMaintStatHighRBUFBufEntries = _RurlMaintStatHighRBUFBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 18),
    _RurlMaintStatHighRBUFBufEntries_Type()
)
rurlMaintStatHighRBUFBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatHighRBUFBufEntries.setStatus("mandatory")
_RurlMaintStatRSEQBufAllocs_Type = Counter32
_RurlMaintStatRSEQBufAllocs_Object = MibScalar
rurlMaintStatRSEQBufAllocs = _RurlMaintStatRSEQBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 19),
    _RurlMaintStatRSEQBufAllocs_Type()
)
rurlMaintStatRSEQBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRSEQBufAllocs.setStatus("mandatory")
_RurlMaintStatRSEQBufFrees_Type = Counter32
_RurlMaintStatRSEQBufFrees_Object = MibScalar
rurlMaintStatRSEQBufFrees = _RurlMaintStatRSEQBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 20),
    _RurlMaintStatRSEQBufFrees_Type()
)
rurlMaintStatRSEQBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRSEQBufFrees.setStatus("mandatory")
_RurlMaintStatRSEQFailBufAllocs_Type = Counter32
_RurlMaintStatRSEQFailBufAllocs_Object = MibScalar
rurlMaintStatRSEQFailBufAllocs = _RurlMaintStatRSEQFailBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 21),
    _RurlMaintStatRSEQFailBufAllocs_Type()
)
rurlMaintStatRSEQFailBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRSEQFailBufAllocs.setStatus("mandatory")
_RurlMaintStatRSEQFailBufFrees_Type = Counter32
_RurlMaintStatRSEQFailBufFrees_Object = MibScalar
rurlMaintStatRSEQFailBufFrees = _RurlMaintStatRSEQFailBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 22),
    _RurlMaintStatRSEQFailBufFrees_Type()
)
rurlMaintStatRSEQFailBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRSEQFailBufFrees.setStatus("mandatory")
_RurlMaintStatRBUFBufAllocs_Type = Counter32
_RurlMaintStatRBUFBufAllocs_Object = MibScalar
rurlMaintStatRBUFBufAllocs = _RurlMaintStatRBUFBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 23),
    _RurlMaintStatRBUFBufAllocs_Type()
)
rurlMaintStatRBUFBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRBUFBufAllocs.setStatus("mandatory")
_RurlMaintStatRBUFBufFrees_Type = Counter32
_RurlMaintStatRBUFBufFrees_Object = MibScalar
rurlMaintStatRBUFBufFrees = _RurlMaintStatRBUFBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 24),
    _RurlMaintStatRBUFBufFrees_Type()
)
rurlMaintStatRBUFBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRBUFBufFrees.setStatus("mandatory")
_RurlMaintStatRBUFFailBufAllocs_Type = Counter32
_RurlMaintStatRBUFFailBufAllocs_Object = MibScalar
rurlMaintStatRBUFFailBufAllocs = _RurlMaintStatRBUFFailBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 25),
    _RurlMaintStatRBUFFailBufAllocs_Type()
)
rurlMaintStatRBUFFailBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRBUFFailBufAllocs.setStatus("mandatory")
_RurlMaintStatRBUFFailBufFrees_Type = Counter32
_RurlMaintStatRBUFFailBufFrees_Object = MibScalar
rurlMaintStatRBUFFailBufFrees = _RurlMaintStatRBUFFailBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 26),
    _RurlMaintStatRBUFFailBufFrees_Type()
)
rurlMaintStatRBUFFailBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRBUFFailBufFrees.setStatus("mandatory")
_RurlMaintStatRBUFRetransmit_Type = Counter32
_RurlMaintStatRBUFRetransmit_Object = MibScalar
rurlMaintStatRBUFRetransmit = _RurlMaintStatRBUFRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 27),
    _RurlMaintStatRBUFRetransmit_Type()
)
rurlMaintStatRBUFRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRBUFRetransmit.setStatus("mandatory")
_RurlMaintStatRBUFChanged_Type = Counter32
_RurlMaintStatRBUFChanged_Object = MibScalar
rurlMaintStatRBUFChanged = _RurlMaintStatRBUFChanged_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 18, 3, 28),
    _RurlMaintStatRBUFChanged_Type()
)
rurlMaintStatRBUFChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rurlMaintStatRBUFChanged.setStatus("mandatory")
_RtspStats_ObjectIdentity = ObjectIdentity
rtspStats = _RtspStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 19)
)
_RtspStatControlConns_Type = Gauge32
_RtspStatControlConns_Object = MibScalar
rtspStatControlConns = _RtspStatControlConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 19, 1),
    _RtspStatControlConns_Type()
)
rtspStatControlConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatControlConns.setStatus("mandatory")
_RtspStatUDPStreams_Type = Gauge32
_RtspStatUDPStreams_Object = MibScalar
rtspStatUDPStreams = _RtspStatUDPStreams_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 19, 2),
    _RtspStatUDPStreams_Type()
)
rtspStatUDPStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatUDPStreams.setStatus("mandatory")
_RtspStatRedirects_Type = Counter32
_RtspStatRedirects_Object = MibScalar
rtspStatRedirects = _RtspStatRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 19, 3),
    _RtspStatRedirects_Type()
)
rtspStatRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatRedirects.setStatus("mandatory")
_RtspStatConnDenied_Type = Counter32
_RtspStatConnDenied_Object = MibScalar
rtspStatConnDenied = _RtspStatConnDenied_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 19, 4),
    _RtspStatConnDenied_Type()
)
rtspStatConnDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatConnDenied.setStatus("mandatory")
_RtspStatAllocFails_Type = Counter32
_RtspStatAllocFails_Object = MibScalar
rtspStatAllocFails = _RtspStatAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 19, 5),
    _RtspStatAllocFails_Type()
)
rtspStatAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtspStatAllocFails.setStatus("mandatory")
_TcpLimitStats_ObjectIdentity = ObjectIdentity
tcpLimitStats = _TcpLimitStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 23)
)
_TcpLimitStatHoldDowns_Type = Counter32
_TcpLimitStatHoldDowns_Object = MibScalar
tcpLimitStatHoldDowns = _TcpLimitStatHoldDowns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 23, 1),
    _TcpLimitStatHoldDowns_Type()
)
tcpLimitStatHoldDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpLimitStatHoldDowns.setStatus("mandatory")
_TcpLimitStatClientEntries_Type = Gauge32
_TcpLimitStatClientEntries_Object = MibScalar
tcpLimitStatClientEntries = _TcpLimitStatClientEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 23, 2),
    _TcpLimitStatClientEntries_Type()
)
tcpLimitStatClientEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpLimitStatClientEntries.setStatus("mandatory")
_NasaStats_ObjectIdentity = ObjectIdentity
nasaStats = _NasaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24)
)
_NasaStatSpTable_Object = MibTable
nasaStatSpTable = _NasaStatSpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1)
)
if mibBuilder.loadTexts:
    nasaStatSpTable.setStatus("mandatory")
_NasaStatSpEntry_Object = MibTableRow
nasaStatSpEntry = _NasaStatSpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1)
)
nasaStatSpEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "nasaStatSpPortIndex"),
)
if mibBuilder.loadTexts:
    nasaStatSpEntry.setStatus("mandatory")
_NasaStatSpPortIndex_Type = Integer32
_NasaStatSpPortIndex_Object = MibTableColumn
nasaStatSpPortIndex = _NasaStatSpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 1),
    _NasaStatSpPortIndex_Type()
)
nasaStatSpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpPortIndex.setStatus("mandatory")
_NasaStatSpCtlTunnelIn_Type = Counter32
_NasaStatSpCtlTunnelIn_Object = MibTableColumn
nasaStatSpCtlTunnelIn = _NasaStatSpCtlTunnelIn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 2),
    _NasaStatSpCtlTunnelIn_Type()
)
nasaStatSpCtlTunnelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpCtlTunnelIn.setStatus("mandatory")
_NasaStatSpCtlTunnelInvalidPkt_Type = Counter32
_NasaStatSpCtlTunnelInvalidPkt_Object = MibTableColumn
nasaStatSpCtlTunnelInvalidPkt = _NasaStatSpCtlTunnelInvalidPkt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 3),
    _NasaStatSpCtlTunnelInvalidPkt_Type()
)
nasaStatSpCtlTunnelInvalidPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpCtlTunnelInvalidPkt.setStatus("mandatory")
_NasaStatSpReqSessCnt_Type = Counter32
_NasaStatSpReqSessCnt_Object = MibTableColumn
nasaStatSpReqSessCnt = _NasaStatSpReqSessCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 4),
    _NasaStatSpReqSessCnt_Type()
)
nasaStatSpReqSessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpReqSessCnt.setStatus("mandatory")
_NasaStatSpSessAddCnt_Type = Counter32
_NasaStatSpSessAddCnt_Object = MibTableColumn
nasaStatSpSessAddCnt = _NasaStatSpSessAddCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 5),
    _NasaStatSpSessAddCnt_Type()
)
nasaStatSpSessAddCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpSessAddCnt.setStatus("mandatory")
_NasaStatSpSessDelCnt_Type = Counter32
_NasaStatSpSessDelCnt_Object = MibTableColumn
nasaStatSpSessDelCnt = _NasaStatSpSessDelCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 6),
    _NasaStatSpSessDelCnt_Type()
)
nasaStatSpSessDelCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpSessDelCnt.setStatus("mandatory")
_NasaStatSpSessUpdCnt_Type = Counter32
_NasaStatSpSessUpdCnt_Object = MibTableColumn
nasaStatSpSessUpdCnt = _NasaStatSpSessUpdCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 7),
    _NasaStatSpSessUpdCnt_Type()
)
nasaStatSpSessUpdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpSessUpdCnt.setStatus("mandatory")
_NasaStatSpSessRdCnt_Type = Counter32
_NasaStatSpSessRdCnt_Object = MibTableColumn
nasaStatSpSessRdCnt = _NasaStatSpSessRdCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 8),
    _NasaStatSpSessRdCnt_Type()
)
nasaStatSpSessRdCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpSessRdCnt.setStatus("mandatory")
_NasaStatSpSessCharCnt_Type = Counter32
_NasaStatSpSessCharCnt_Object = MibTableColumn
nasaStatSpSessCharCnt = _NasaStatSpSessCharCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 9),
    _NasaStatSpSessCharCnt_Type()
)
nasaStatSpSessCharCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpSessCharCnt.setStatus("mandatory")
_NasaStatSpReqSessNoIsd_Type = Counter32
_NasaStatSpReqSessNoIsd_Object = MibTableColumn
nasaStatSpReqSessNoIsd = _NasaStatSpReqSessNoIsd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 10),
    _NasaStatSpReqSessNoIsd_Type()
)
nasaStatSpReqSessNoIsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpReqSessNoIsd.setStatus("mandatory")
_NasaStatSpCtlTunnelToMp_Type = Counter32
_NasaStatSpCtlTunnelToMp_Object = MibTableColumn
nasaStatSpCtlTunnelToMp = _NasaStatSpCtlTunnelToMp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 11),
    _NasaStatSpCtlTunnelToMp_Type()
)
nasaStatSpCtlTunnelToMp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpCtlTunnelToMp.setStatus("mandatory")
_NasaStatSpBcastTunnelCnt_Type = Counter32
_NasaStatSpBcastTunnelCnt_Object = MibTableColumn
nasaStatSpBcastTunnelCnt = _NasaStatSpBcastTunnelCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 12),
    _NasaStatSpBcastTunnelCnt_Type()
)
nasaStatSpBcastTunnelCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpBcastTunnelCnt.setStatus("mandatory")
_NasaStatSpBcastTunnelToMp_Type = Counter32
_NasaStatSpBcastTunnelToMp_Object = MibTableColumn
nasaStatSpBcastTunnelToMp = _NasaStatSpBcastTunnelToMp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 13),
    _NasaStatSpBcastTunnelToMp_Type()
)
nasaStatSpBcastTunnelToMp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpBcastTunnelToMp.setStatus("mandatory")
_NasaStatSpBcastTunnelToIsd_Type = Counter32
_NasaStatSpBcastTunnelToIsd_Object = MibTableColumn
nasaStatSpBcastTunnelToIsd = _NasaStatSpBcastTunnelToIsd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 14),
    _NasaStatSpBcastTunnelToIsd_Type()
)
nasaStatSpBcastTunnelToIsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpBcastTunnelToIsd.setStatus("mandatory")
_NasaStatSpRurlTunnelCnt_Type = Counter32
_NasaStatSpRurlTunnelCnt_Object = MibTableColumn
nasaStatSpRurlTunnelCnt = _NasaStatSpRurlTunnelCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 15),
    _NasaStatSpRurlTunnelCnt_Type()
)
nasaStatSpRurlTunnelCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpRurlTunnelCnt.setStatus("mandatory")
_NasaStatSpIpDatagramCnt_Type = Counter32
_NasaStatSpIpDatagramCnt_Object = MibTableColumn
nasaStatSpIpDatagramCnt = _NasaStatSpIpDatagramCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 16),
    _NasaStatSpIpDatagramCnt_Type()
)
nasaStatSpIpDatagramCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpIpDatagramCnt.setStatus("mandatory")
_NasaStatSpCliRedirectCnt_Type = Counter32
_NasaStatSpCliRedirectCnt_Object = MibTableColumn
nasaStatSpCliRedirectCnt = _NasaStatSpCliRedirectCnt_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 17),
    _NasaStatSpCliRedirectCnt_Type()
)
nasaStatSpCliRedirectCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpCliRedirectCnt.setStatus("mandatory")
_NasaStatSpInvalidVersion_Type = Counter32
_NasaStatSpInvalidVersion_Object = MibTableColumn
nasaStatSpInvalidVersion = _NasaStatSpInvalidVersion_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 18),
    _NasaStatSpInvalidVersion_Type()
)
nasaStatSpInvalidVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpInvalidVersion.setStatus("mandatory")
_NasaStatSpAckTx_Type = Counter32
_NasaStatSpAckTx_Object = MibTableColumn
nasaStatSpAckTx = _NasaStatSpAckTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 19),
    _NasaStatSpAckTx_Type()
)
nasaStatSpAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpAckTx.setStatus("mandatory")
_NasaStatSpAckRx_Type = Counter32
_NasaStatSpAckRx_Object = MibTableColumn
nasaStatSpAckRx = _NasaStatSpAckRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 20),
    _NasaStatSpAckRx_Type()
)
nasaStatSpAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpAckRx.setStatus("mandatory")
_NasaStatSpAckAlloc_Type = Counter32
_NasaStatSpAckAlloc_Object = MibTableColumn
nasaStatSpAckAlloc = _NasaStatSpAckAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 21),
    _NasaStatSpAckAlloc_Type()
)
nasaStatSpAckAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpAckAlloc.setStatus("mandatory")
_NasaStatSpAckFree_Type = Counter32
_NasaStatSpAckFree_Object = MibTableColumn
nasaStatSpAckFree = _NasaStatSpAckFree_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 22),
    _NasaStatSpAckFree_Type()
)
nasaStatSpAckFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpAckFree.setStatus("mandatory")
_NasaStatSpAllocAckFail_Type = Counter32
_NasaStatSpAllocAckFail_Object = MibTableColumn
nasaStatSpAllocAckFail = _NasaStatSpAllocAckFail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 23),
    _NasaStatSpAllocAckFail_Type()
)
nasaStatSpAllocAckFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpAllocAckFail.setStatus("mandatory")
_NasaStatSpAllocFrmFail_Type = Counter32
_NasaStatSpAllocFrmFail_Object = MibTableColumn
nasaStatSpAllocFrmFail = _NasaStatSpAllocFrmFail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 24),
    _NasaStatSpAllocFrmFail_Type()
)
nasaStatSpAllocFrmFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpAllocFrmFail.setStatus("mandatory")
_NasaStatSpRexmitFail_Type = Counter32
_NasaStatSpRexmitFail_Object = MibTableColumn
nasaStatSpRexmitFail = _NasaStatSpRexmitFail_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 25),
    _NasaStatSpRexmitFail_Type()
)
nasaStatSpRexmitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpRexmitFail.setStatus("mandatory")
_NasaStatSpInvalidIsd_Type = Counter32
_NasaStatSpInvalidIsd_Object = MibTableColumn
nasaStatSpInvalidIsd = _NasaStatSpInvalidIsd_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 26),
    _NasaStatSpInvalidIsd_Type()
)
nasaStatSpInvalidIsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpInvalidIsd.setStatus("mandatory")
_NasaStatSpInvalidPkts_Type = Counter32
_NasaStatSpInvalidPkts_Object = MibTableColumn
nasaStatSpInvalidPkts = _NasaStatSpInvalidPkts_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 1, 1, 27),
    _NasaStatSpInvalidPkts_Type()
)
nasaStatSpInvalidPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatSpInvalidPkts.setStatus("mandatory")
_NasaMpStats_ObjectIdentity = ObjectIdentity
nasaMpStats = _NasaMpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2)
)
_NasaStatMpTotalRx_Type = Counter32
_NasaStatMpTotalRx_Object = MibScalar
nasaStatMpTotalRx = _NasaStatMpTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 1),
    _NasaStatMpTotalRx_Type()
)
nasaStatMpTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpTotalRx.setStatus("mandatory")
_NasaStatMpTotalTx_Type = Counter32
_NasaStatMpTotalTx_Object = MibScalar
nasaStatMpTotalTx = _NasaStatMpTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 2),
    _NasaStatMpTotalTx_Type()
)
nasaStatMpTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpTotalTx.setStatus("mandatory")
_NasaStatMpBadCksum_Type = Counter32
_NasaStatMpBadCksum_Object = MibScalar
nasaStatMpBadCksum = _NasaStatMpBadCksum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 3),
    _NasaStatMpBadCksum_Type()
)
nasaStatMpBadCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpBadCksum.setStatus("mandatory")
_NasaStatMpInvalidRx_Type = Counter32
_NasaStatMpInvalidRx_Object = MibScalar
nasaStatMpInvalidRx = _NasaStatMpInvalidRx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 4),
    _NasaStatMpInvalidRx_Type()
)
nasaStatMpInvalidRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpInvalidRx.setStatus("mandatory")
_NasaStatMpPingRequests_Type = Counter32
_NasaStatMpPingRequests_Object = MibScalar
nasaStatMpPingRequests = _NasaStatMpPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 5),
    _NasaStatMpPingRequests_Type()
)
nasaStatMpPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpPingRequests.setStatus("mandatory")
_NasaStatMpPingResponses_Type = Counter32
_NasaStatMpPingResponses_Object = MibScalar
nasaStatMpPingResponses = _NasaStatMpPingResponses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 6),
    _NasaStatMpPingResponses_Type()
)
nasaStatMpPingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpPingResponses.setStatus("mandatory")
_NasaStatMpRegRequests_Type = Counter32
_NasaStatMpRegRequests_Object = MibScalar
nasaStatMpRegRequests = _NasaStatMpRegRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 7),
    _NasaStatMpRegRequests_Type()
)
nasaStatMpRegRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpRegRequests.setStatus("mandatory")
_NasaStatMpCapResponses_Type = Counter32
_NasaStatMpCapResponses_Object = MibScalar
nasaStatMpCapResponses = _NasaStatMpCapResponses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 8),
    _NasaStatMpCapResponses_Type()
)
nasaStatMpCapResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpCapResponses.setStatus("mandatory")
_NasaStatMpRegConfirmations_Type = Counter32
_NasaStatMpRegConfirmations_Object = MibScalar
nasaStatMpRegConfirmations = _NasaStatMpRegConfirmations_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 9),
    _NasaStatMpRegConfirmations_Type()
)
nasaStatMpRegConfirmations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpRegConfirmations.setStatus("mandatory")
_NasaStatMpUnregRequests_Type = Counter32
_NasaStatMpUnregRequests_Object = MibScalar
nasaStatMpUnregRequests = _NasaStatMpUnregRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 10),
    _NasaStatMpUnregRequests_Type()
)
nasaStatMpUnregRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpUnregRequests.setStatus("mandatory")
_NasaStatMpHealthRequests_Type = Counter32
_NasaStatMpHealthRequests_Object = MibScalar
nasaStatMpHealthRequests = _NasaStatMpHealthRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 11),
    _NasaStatMpHealthRequests_Type()
)
nasaStatMpHealthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpHealthRequests.setStatus("mandatory")
_NasaStatMpHealthResponses_Type = Counter32
_NasaStatMpHealthResponses_Object = MibScalar
nasaStatMpHealthResponses = _NasaStatMpHealthResponses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 12),
    _NasaStatMpHealthResponses_Type()
)
nasaStatMpHealthResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpHealthResponses.setStatus("mandatory")
_NasaStatMpCmdRequests_Type = Counter32
_NasaStatMpCmdRequests_Object = MibScalar
nasaStatMpCmdRequests = _NasaStatMpCmdRequests_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 13),
    _NasaStatMpCmdRequests_Type()
)
nasaStatMpCmdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpCmdRequests.setStatus("mandatory")
_NasaStatMpCmdResponses_Type = Counter32
_NasaStatMpCmdResponses_Object = MibScalar
nasaStatMpCmdResponses = _NasaStatMpCmdResponses_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 24, 2, 14),
    _NasaStatMpCmdResponses_Type()
)
nasaStatMpCmdResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaStatMpCmdResponses.setStatus("mandatory")
_DnsSlbStats_ObjectIdentity = ObjectIdentity
dnsSlbStats = _DnsSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25)
)
_DnsSlbStatTCPQueries_Type = Counter32
_DnsSlbStatTCPQueries_Object = MibScalar
dnsSlbStatTCPQueries = _DnsSlbStatTCPQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25, 1),
    _DnsSlbStatTCPQueries_Type()
)
dnsSlbStatTCPQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatTCPQueries.setStatus("mandatory")
_DnsSlbStatUDPQueries_Type = Counter32
_DnsSlbStatUDPQueries_Object = MibScalar
dnsSlbStatUDPQueries = _DnsSlbStatUDPQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25, 2),
    _DnsSlbStatUDPQueries_Type()
)
dnsSlbStatUDPQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatUDPQueries.setStatus("mandatory")
_DnsSlbStatInvalidQueries_Type = Counter32
_DnsSlbStatInvalidQueries_Object = MibScalar
dnsSlbStatInvalidQueries = _DnsSlbStatInvalidQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25, 3),
    _DnsSlbStatInvalidQueries_Type()
)
dnsSlbStatInvalidQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatInvalidQueries.setStatus("mandatory")
_DnsSlbStatMultipleQueries_Type = Counter32
_DnsSlbStatMultipleQueries_Object = MibScalar
dnsSlbStatMultipleQueries = _DnsSlbStatMultipleQueries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25, 4),
    _DnsSlbStatMultipleQueries_Type()
)
dnsSlbStatMultipleQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatMultipleQueries.setStatus("mandatory")
_DnsSlbStatDnameParseErrors_Type = Counter32
_DnsSlbStatDnameParseErrors_Object = MibScalar
dnsSlbStatDnameParseErrors = _DnsSlbStatDnameParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25, 5),
    _DnsSlbStatDnameParseErrors_Type()
)
dnsSlbStatDnameParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatDnameParseErrors.setStatus("mandatory")
_DnsSlbStatFailedMatches_Type = Counter32
_DnsSlbStatFailedMatches_Object = MibScalar
dnsSlbStatFailedMatches = _DnsSlbStatFailedMatches_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25, 6),
    _DnsSlbStatFailedMatches_Type()
)
dnsSlbStatFailedMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatFailedMatches.setStatus("mandatory")
_DnsSlbStatInternalErrors_Type = Counter32
_DnsSlbStatInternalErrors_Object = MibScalar
dnsSlbStatInternalErrors = _DnsSlbStatInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 8, 25, 7),
    _DnsSlbStatInternalErrors_Type()
)
dnsSlbStatInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsSlbStatInternalErrors.setStatus("mandatory")
_Slb_info_ObjectIdentity = ObjectIdentity
slb_info = _Slb_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2)
)
_SlbFailOverInfoTable_Object = MibTable
slbFailOverInfoTable = _SlbFailOverInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    slbFailOverInfoTable.setStatus("mandatory")
_SlbFailOverInfoEntry_Object = MibTableRow
slbFailOverInfoEntry = _SlbFailOverInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1)
)
slbFailOverInfoEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbFailOverInfoIndex"),
)
if mibBuilder.loadTexts:
    slbFailOverInfoEntry.setStatus("mandatory")
_SlbFailOverInfoIndex_Type = Integer32
_SlbFailOverInfoIndex_Object = MibTableColumn
slbFailOverInfoIndex = _SlbFailOverInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 1),
    _SlbFailOverInfoIndex_Type()
)
slbFailOverInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoIndex.setStatus("mandatory")
_SlbFailOverInfoPrimaryIp_Type = IpAddress
_SlbFailOverInfoPrimaryIp_Object = MibTableColumn
slbFailOverInfoPrimaryIp = _SlbFailOverInfoPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 2),
    _SlbFailOverInfoPrimaryIp_Type()
)
slbFailOverInfoPrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoPrimaryIp.setStatus("mandatory")


class _SlbFailOverInfoPrimaryStatus_Type(Integer32):
    """Custom type slbFailOverInfoPrimaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SlbFailOverInfoPrimaryStatus_Type.__name__ = "Integer32"
_SlbFailOverInfoPrimaryStatus_Object = MibTableColumn
slbFailOverInfoPrimaryStatus = _SlbFailOverInfoPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 3),
    _SlbFailOverInfoPrimaryStatus_Type()
)
slbFailOverInfoPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoPrimaryStatus.setStatus("mandatory")


class _SlbFailOverInfoPrimaryState_Type(Integer32):
    """Custom type slbFailOverInfoPrimaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_SlbFailOverInfoPrimaryState_Type.__name__ = "Integer32"
_SlbFailOverInfoPrimaryState_Object = MibTableColumn
slbFailOverInfoPrimaryState = _SlbFailOverInfoPrimaryState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 4),
    _SlbFailOverInfoPrimaryState_Type()
)
slbFailOverInfoPrimaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoPrimaryState.setStatus("mandatory")
_SlbFailOverInfoSecondaryIp_Type = IpAddress
_SlbFailOverInfoSecondaryIp_Object = MibTableColumn
slbFailOverInfoSecondaryIp = _SlbFailOverInfoSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 5),
    _SlbFailOverInfoSecondaryIp_Type()
)
slbFailOverInfoSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoSecondaryIp.setStatus("mandatory")


class _SlbFailOverInfoSecondaryStatus_Type(Integer32):
    """Custom type slbFailOverInfoSecondaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SlbFailOverInfoSecondaryStatus_Type.__name__ = "Integer32"
_SlbFailOverInfoSecondaryStatus_Object = MibTableColumn
slbFailOverInfoSecondaryStatus = _SlbFailOverInfoSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 6),
    _SlbFailOverInfoSecondaryStatus_Type()
)
slbFailOverInfoSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoSecondaryStatus.setStatus("mandatory")


class _SlbFailOverInfoSecondaryState_Type(Integer32):
    """Custom type slbFailOverInfoSecondaryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_SlbFailOverInfoSecondaryState_Type.__name__ = "Integer32"
_SlbFailOverInfoSecondaryState_Object = MibTableColumn
slbFailOverInfoSecondaryState = _SlbFailOverInfoSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 1, 1, 7),
    _SlbFailOverInfoSecondaryState_Type()
)
slbFailOverInfoSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbFailOverInfoSecondaryState.setStatus("mandatory")
_SlbRealServerInfoTable_Object = MibTable
slbRealServerInfoTable = _SlbRealServerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    slbRealServerInfoTable.setStatus("mandatory")
_SlbRealServerInfoEntry_Object = MibTableRow
slbRealServerInfoEntry = _SlbRealServerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1)
)
slbRealServerInfoEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbRealServerInfoIndex"),
)
if mibBuilder.loadTexts:
    slbRealServerInfoEntry.setStatus("mandatory")
_SlbRealServerInfoIndex_Type = Integer32
_SlbRealServerInfoIndex_Object = MibTableColumn
slbRealServerInfoIndex = _SlbRealServerInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 1),
    _SlbRealServerInfoIndex_Type()
)
slbRealServerInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoIndex.setStatus("mandatory")
_SlbRealServerInfoIpAddr_Type = IpAddress
_SlbRealServerInfoIpAddr_Object = MibTableColumn
slbRealServerInfoIpAddr = _SlbRealServerInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 2),
    _SlbRealServerInfoIpAddr_Type()
)
slbRealServerInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoIpAddr.setStatus("mandatory")
_SlbRealServerMacAddr_Type = PhysAddress
_SlbRealServerMacAddr_Object = MibTableColumn
slbRealServerMacAddr = _SlbRealServerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 3),
    _SlbRealServerMacAddr_Type()
)
slbRealServerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerMacAddr.setStatus("mandatory")
_SlbRealServerInfoSwitchPort_Type = Integer32
_SlbRealServerInfoSwitchPort_Object = MibTableColumn
slbRealServerInfoSwitchPort = _SlbRealServerInfoSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 4),
    _SlbRealServerInfoSwitchPort_Type()
)
slbRealServerInfoSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoSwitchPort.setStatus("mandatory")


class _SlbRealServerInfoHealthLayer_Type(Integer32):
    """Custom type slbRealServerInfoHealthLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer3", 2),
          ("layer4", 3),
          ("other", 1))
    )


_SlbRealServerInfoHealthLayer_Type.__name__ = "Integer32"
_SlbRealServerInfoHealthLayer_Object = MibTableColumn
slbRealServerInfoHealthLayer = _SlbRealServerInfoHealthLayer_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 5),
    _SlbRealServerInfoHealthLayer_Type()
)
slbRealServerInfoHealthLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoHealthLayer.setStatus("mandatory")


class _SlbRealServerInfoOverflow_Type(Integer32):
    """Custom type slbRealServerInfoOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-overflow", 2),
          ("overflow", 1))
    )


_SlbRealServerInfoOverflow_Type.__name__ = "Integer32"
_SlbRealServerInfoOverflow_Object = MibTableColumn
slbRealServerInfoOverflow = _SlbRealServerInfoOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 6),
    _SlbRealServerInfoOverflow_Type()
)
slbRealServerInfoOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoOverflow.setStatus("mandatory")


class _SlbRealServerInfoState_Type(Integer32):
    """Custom type slbRealServerInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("failed", 3),
          ("running", 2))
    )


_SlbRealServerInfoState_Type.__name__ = "Integer32"
_SlbRealServerInfoState_Object = MibTableColumn
slbRealServerInfoState = _SlbRealServerInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 2, 1, 7),
    _SlbRealServerInfoState_Type()
)
slbRealServerInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbRealServerInfoState.setStatus("mandatory")
_NasaIsdInfoTable_Object = MibTable
nasaIsdInfoTable = _NasaIsdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3)
)
if mibBuilder.loadTexts:
    nasaIsdInfoTable.setStatus("mandatory")
_NasaIsdInfoEntry_Object = MibTableRow
nasaIsdInfoEntry = _NasaIsdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1)
)
nasaIsdInfoEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "nasaIsdInfoIndex"),
)
if mibBuilder.loadTexts:
    nasaIsdInfoEntry.setStatus("mandatory")
_NasaIsdInfoIndex_Type = Integer32
_NasaIsdInfoIndex_Object = MibTableColumn
nasaIsdInfoIndex = _NasaIsdInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1, 1),
    _NasaIsdInfoIndex_Type()
)
nasaIsdInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaIsdInfoIndex.setStatus("mandatory")
_NasaIsdInfoIpAddr_Type = IpAddress
_NasaIsdInfoIpAddr_Object = MibTableColumn
nasaIsdInfoIpAddr = _NasaIsdInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1, 2),
    _NasaIsdInfoIpAddr_Type()
)
nasaIsdInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaIsdInfoIpAddr.setStatus("mandatory")
_NasaIsdMacAddr_Type = PhysAddress
_NasaIsdMacAddr_Object = MibTableColumn
nasaIsdMacAddr = _NasaIsdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1, 3),
    _NasaIsdMacAddr_Type()
)
nasaIsdMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaIsdMacAddr.setStatus("mandatory")
_NasaIsdInfoSwitchPort_Type = Integer32
_NasaIsdInfoSwitchPort_Object = MibTableColumn
nasaIsdInfoSwitchPort = _NasaIsdInfoSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1, 4),
    _NasaIsdInfoSwitchPort_Type()
)
nasaIsdInfoSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaIsdInfoSwitchPort.setStatus("mandatory")
_NasaIsdInfoGdi_Type = Integer32
_NasaIsdInfoGdi_Object = MibTableColumn
nasaIsdInfoGdi = _NasaIsdInfoGdi_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1, 5),
    _NasaIsdInfoGdi_Type()
)
nasaIsdInfoGdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaIsdInfoGdi.setStatus("mandatory")


class _NasaIsdInfoState_Type(Integer32):
    """Custom type nasaIsdInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("isd-access", 3),
          ("isd-down", 5),
          ("isd-invalid", 1),
          ("isd-mip", 6),
          ("isd-unregistered", 2),
          ("isd-up", 4))
    )


_NasaIsdInfoState_Type.__name__ = "Integer32"
_NasaIsdInfoState_Object = MibTableColumn
nasaIsdInfoState = _NasaIsdInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1, 6),
    _NasaIsdInfoState_Type()
)
nasaIsdInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaIsdInfoState.setStatus("mandatory")
_NasaIsdInfoStateChange_Type = Integer32
_NasaIsdInfoStateChange_Object = MibTableColumn
nasaIsdInfoStateChange = _NasaIsdInfoStateChange_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 9, 2, 3, 1, 7),
    _NasaIsdInfoStateChange_Type()
)
nasaIsdInfoStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasaIsdInfoStateChange.setStatus("mandatory")
_Filtering_ObjectIdentity = ObjectIdentity
filtering = _Filtering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10)
)
_FltCfgTableMaxSize_Type = Integer32
_FltCfgTableMaxSize_Object = MibScalar
fltCfgTableMaxSize = _FltCfgTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 1),
    _FltCfgTableMaxSize_Type()
)
fltCfgTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCfgTableMaxSize.setStatus("mandatory")
_FltCurCfgTable_Object = MibTable
fltCurCfgTable = _FltCurCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    fltCurCfgTable.setStatus("mandatory")
_FltCurCfgTableEntry_Object = MibTableRow
fltCurCfgTableEntry = _FltCurCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1)
)
fltCurCfgTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "fltCurCfgIndx"),
)
if mibBuilder.loadTexts:
    fltCurCfgTableEntry.setStatus("mandatory")
_FltCurCfgIndx_Type = Integer32
_FltCurCfgIndx_Object = MibTableColumn
fltCurCfgIndx = _FltCurCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 1),
    _FltCurCfgIndx_Type()
)
fltCurCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIndx.setStatus("mandatory")
_FltCurCfgSrcIp_Type = IpAddress
_FltCurCfgSrcIp_Object = MibTableColumn
fltCurCfgSrcIp = _FltCurCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 2),
    _FltCurCfgSrcIp_Type()
)
fltCurCfgSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIp.setStatus("mandatory")
_FltCurCfgSrcIpMask_Type = IpAddress
_FltCurCfgSrcIpMask_Object = MibTableColumn
fltCurCfgSrcIpMask = _FltCurCfgSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 3),
    _FltCurCfgSrcIpMask_Type()
)
fltCurCfgSrcIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIpMask.setStatus("mandatory")
_FltCurCfgDstIp_Type = IpAddress
_FltCurCfgDstIp_Object = MibTableColumn
fltCurCfgDstIp = _FltCurCfgDstIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 4),
    _FltCurCfgDstIp_Type()
)
fltCurCfgDstIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIp.setStatus("mandatory")
_FltCurCfgDstIpMask_Type = IpAddress
_FltCurCfgDstIpMask_Object = MibTableColumn
fltCurCfgDstIpMask = _FltCurCfgDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 5),
    _FltCurCfgDstIpMask_Type()
)
fltCurCfgDstIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIpMask.setStatus("mandatory")
_FltCurCfgProtocol_Type = Integer32
_FltCurCfgProtocol_Object = MibTableColumn
fltCurCfgProtocol = _FltCurCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 6),
    _FltCurCfgProtocol_Type()
)
fltCurCfgProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgProtocol.setStatus("mandatory")


class _FltCurCfgRangeHighSrcPort_Type(Integer32):
    """Custom type fltCurCfgRangeHighSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeHighSrcPort_Type.__name__ = "Integer32"
_FltCurCfgRangeHighSrcPort_Object = MibTableColumn
fltCurCfgRangeHighSrcPort = _FltCurCfgRangeHighSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 7),
    _FltCurCfgRangeHighSrcPort_Type()
)
fltCurCfgRangeHighSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeHighSrcPort.setStatus("mandatory")


class _FltCurCfgRangeLowSrcPort_Type(Integer32):
    """Custom type fltCurCfgRangeLowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeLowSrcPort_Type.__name__ = "Integer32"
_FltCurCfgRangeLowSrcPort_Object = MibTableColumn
fltCurCfgRangeLowSrcPort = _FltCurCfgRangeLowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 8),
    _FltCurCfgRangeLowSrcPort_Type()
)
fltCurCfgRangeLowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeLowSrcPort.setStatus("mandatory")


class _FltCurCfgRangeLowDstPort_Type(Integer32):
    """Custom type fltCurCfgRangeLowDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeLowDstPort_Type.__name__ = "Integer32"
_FltCurCfgRangeLowDstPort_Object = MibTableColumn
fltCurCfgRangeLowDstPort = _FltCurCfgRangeLowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 9),
    _FltCurCfgRangeLowDstPort_Type()
)
fltCurCfgRangeLowDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeLowDstPort.setStatus("mandatory")


class _FltCurCfgRangeHighDstPort_Type(Integer32):
    """Custom type fltCurCfgRangeHighDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRangeHighDstPort_Type.__name__ = "Integer32"
_FltCurCfgRangeHighDstPort_Object = MibTableColumn
fltCurCfgRangeHighDstPort = _FltCurCfgRangeHighDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 10),
    _FltCurCfgRangeHighDstPort_Type()
)
fltCurCfgRangeHighDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRangeHighDstPort.setStatus("mandatory")


class _FltCurCfgAction_Type(Integer32):
    """Custom type fltCurCfgAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("nat", 4),
          ("redirect", 3))
    )


_FltCurCfgAction_Type.__name__ = "Integer32"
_FltCurCfgAction_Object = MibTableColumn
fltCurCfgAction = _FltCurCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 11),
    _FltCurCfgAction_Type()
)
fltCurCfgAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAction.setStatus("mandatory")


class _FltCurCfgRedirPort_Type(Integer32):
    """Custom type fltCurCfgRedirPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltCurCfgRedirPort_Type.__name__ = "Integer32"
_FltCurCfgRedirPort_Object = MibTableColumn
fltCurCfgRedirPort = _FltCurCfgRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 12),
    _FltCurCfgRedirPort_Type()
)
fltCurCfgRedirPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRedirPort.setStatus("mandatory")
_FltCurCfgRedirGroup_Type = Integer32
_FltCurCfgRedirGroup_Object = MibTableColumn
fltCurCfgRedirGroup = _FltCurCfgRedirGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 13),
    _FltCurCfgRedirGroup_Type()
)
fltCurCfgRedirGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRedirGroup.setStatus("mandatory")


class _FltCurCfgLog_Type(Integer32):
    """Custom type fltCurCfgLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgLog_Type.__name__ = "Integer32"
_FltCurCfgLog_Object = MibTableColumn
fltCurCfgLog = _FltCurCfgLog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 14),
    _FltCurCfgLog_Type()
)
fltCurCfgLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLog.setStatus("mandatory")


class _FltCurCfgState_Type(Integer32):
    """Custom type fltCurCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgState_Type.__name__ = "Integer32"
_FltCurCfgState_Object = MibTableColumn
fltCurCfgState = _FltCurCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 15),
    _FltCurCfgState_Type()
)
fltCurCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgState.setStatus("mandatory")


class _FltCurCfgNat_Type(Integer32):
    """Custom type fltCurCfgNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-address", 1),
          ("source-address", 2))
    )


_FltCurCfgNat_Type.__name__ = "Integer32"
_FltCurCfgNat_Object = MibTableColumn
fltCurCfgNat = _FltCurCfgNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 16),
    _FltCurCfgNat_Type()
)
fltCurCfgNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgNat.setStatus("mandatory")


class _FltCurCfgCache_Type(Integer32):
    """Custom type fltCurCfgCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgCache_Type.__name__ = "Integer32"
_FltCurCfgCache_Object = MibTableColumn
fltCurCfgCache = _FltCurCfgCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 17),
    _FltCurCfgCache_Type()
)
fltCurCfgCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgCache.setStatus("mandatory")


class _FltCurCfgInvert_Type(Integer32):
    """Custom type fltCurCfgInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert-off", 2),
          ("invert-on", 1))
    )


_FltCurCfgInvert_Type.__name__ = "Integer32"
_FltCurCfgInvert_Object = MibTableColumn
fltCurCfgInvert = _FltCurCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 18),
    _FltCurCfgInvert_Type()
)
fltCurCfgInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgInvert.setStatus("mandatory")


class _FltCurCfgClientProxy_Type(Integer32):
    """Custom type fltCurCfgClientProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgClientProxy_Type.__name__ = "Integer32"
_FltCurCfgClientProxy_Object = MibTableColumn
fltCurCfgClientProxy = _FltCurCfgClientProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 19),
    _FltCurCfgClientProxy_Type()
)
fltCurCfgClientProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgClientProxy.setStatus("mandatory")


class _FltCurCfgTcpAck_Type(Integer32):
    """Custom type fltCurCfgTcpAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgTcpAck_Type.__name__ = "Integer32"
_FltCurCfgTcpAck_Object = MibTableColumn
fltCurCfgTcpAck = _FltCurCfgTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 20),
    _FltCurCfgTcpAck_Type()
)
fltCurCfgTcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTcpAck.setStatus("mandatory")


class _FltCurCfgUrlRedir_Type(Integer32):
    """Custom type fltCurCfgUrlRedir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgUrlRedir_Type.__name__ = "Integer32"
_FltCurCfgUrlRedir_Object = MibTableColumn
fltCurCfgUrlRedir = _FltCurCfgUrlRedir_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 21),
    _FltCurCfgUrlRedir_Type()
)
fltCurCfgUrlRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlRedir.setStatus("mandatory")
_FltCurCfgSrcMac_Type = PhysAddress
_FltCurCfgSrcMac_Object = MibTableColumn
fltCurCfgSrcMac = _FltCurCfgSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 22),
    _FltCurCfgSrcMac_Type()
)
fltCurCfgSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcMac.setStatus("mandatory")
_FltCurCfgDstMac_Type = PhysAddress
_FltCurCfgDstMac_Object = MibTableColumn
fltCurCfgDstMac = _FltCurCfgDstMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 23),
    _FltCurCfgDstMac_Type()
)
fltCurCfgDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstMac.setStatus("mandatory")


class _FltCurCfgFtpNatActive_Type(Integer32):
    """Custom type fltCurCfgFtpNatActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgFtpNatActive_Type.__name__ = "Integer32"
_FltCurCfgFtpNatActive_Object = MibTableColumn
fltCurCfgFtpNatActive = _FltCurCfgFtpNatActive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 24),
    _FltCurCfgFtpNatActive_Type()
)
fltCurCfgFtpNatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgFtpNatActive.setStatus("mandatory")


class _FltCurCfgAclTcpUrg_Type(Integer32):
    """Custom type fltCurCfgAclTcpUrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltCurCfgAclTcpUrg_Type.__name__ = "Integer32"
_FltCurCfgAclTcpUrg_Object = MibTableColumn
fltCurCfgAclTcpUrg = _FltCurCfgAclTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 25),
    _FltCurCfgAclTcpUrg_Type()
)
fltCurCfgAclTcpUrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpUrg.setStatus("mandatory")


class _FltCurCfgAclTcpAck_Type(Integer32):
    """Custom type fltCurCfgAclTcpAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltCurCfgAclTcpAck_Type.__name__ = "Integer32"
_FltCurCfgAclTcpAck_Object = MibTableColumn
fltCurCfgAclTcpAck = _FltCurCfgAclTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 26),
    _FltCurCfgAclTcpAck_Type()
)
fltCurCfgAclTcpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpAck.setStatus("mandatory")


class _FltCurCfgAclTcpPsh_Type(Integer32):
    """Custom type fltCurCfgAclTcpPsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltCurCfgAclTcpPsh_Type.__name__ = "Integer32"
_FltCurCfgAclTcpPsh_Object = MibTableColumn
fltCurCfgAclTcpPsh = _FltCurCfgAclTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 27),
    _FltCurCfgAclTcpPsh_Type()
)
fltCurCfgAclTcpPsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpPsh.setStatus("mandatory")


class _FltCurCfgAclTcpRst_Type(Integer32):
    """Custom type fltCurCfgAclTcpRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltCurCfgAclTcpRst_Type.__name__ = "Integer32"
_FltCurCfgAclTcpRst_Object = MibTableColumn
fltCurCfgAclTcpRst = _FltCurCfgAclTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 28),
    _FltCurCfgAclTcpRst_Type()
)
fltCurCfgAclTcpRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpRst.setStatus("mandatory")


class _FltCurCfgAclTcpSyn_Type(Integer32):
    """Custom type fltCurCfgAclTcpSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltCurCfgAclTcpSyn_Type.__name__ = "Integer32"
_FltCurCfgAclTcpSyn_Object = MibTableColumn
fltCurCfgAclTcpSyn = _FltCurCfgAclTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 29),
    _FltCurCfgAclTcpSyn_Type()
)
fltCurCfgAclTcpSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpSyn.setStatus("mandatory")


class _FltCurCfgAclTcpFin_Type(Integer32):
    """Custom type fltCurCfgAclTcpFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltCurCfgAclTcpFin_Type.__name__ = "Integer32"
_FltCurCfgAclTcpFin_Object = MibTableColumn
fltCurCfgAclTcpFin = _FltCurCfgAclTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 30),
    _FltCurCfgAclTcpFin_Type()
)
fltCurCfgAclTcpFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclTcpFin.setStatus("mandatory")


class _FltCurCfgAclIcmp_Type(Integer32):
    """Custom type fltCurCfgAclIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIcmp_Type.__name__ = "Integer32"
_FltCurCfgAclIcmp_Object = MibTableColumn
fltCurCfgAclIcmp = _FltCurCfgAclIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 31),
    _FltCurCfgAclIcmp_Type()
)
fltCurCfgAclIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIcmp.setStatus("mandatory")


class _FltCurCfgAclIpOption_Type(Integer32):
    """Custom type fltCurCfgAclIpOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltCurCfgAclIpOption_Type.__name__ = "Integer32"
_FltCurCfgAclIpOption_Object = MibTableColumn
fltCurCfgAclIpOption = _FltCurCfgAclIpOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 32),
    _FltCurCfgAclIpOption_Type()
)
fltCurCfgAclIpOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpOption.setStatus("mandatory")
_FltCurCfgBwmContract_Type = Integer32
_FltCurCfgBwmContract_Object = MibTableColumn
fltCurCfgBwmContract = _FltCurCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 33),
    _FltCurCfgBwmContract_Type()
)
fltCurCfgBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgBwmContract.setStatus("mandatory")


class _FltCurCfgAclIpTos_Type(Integer32):
    """Custom type fltCurCfgAclIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTos_Type.__name__ = "Integer32"
_FltCurCfgAclIpTos_Object = MibTableColumn
fltCurCfgAclIpTos = _FltCurCfgAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 34),
    _FltCurCfgAclIpTos_Type()
)
fltCurCfgAclIpTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTos.setStatus("mandatory")


class _FltCurCfgAclIpTosMask_Type(Integer32):
    """Custom type fltCurCfgAclIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTosMask_Type.__name__ = "Integer32"
_FltCurCfgAclIpTosMask_Object = MibTableColumn
fltCurCfgAclIpTosMask = _FltCurCfgAclIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 35),
    _FltCurCfgAclIpTosMask_Type()
)
fltCurCfgAclIpTosMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTosMask.setStatus("mandatory")


class _FltCurCfgAclIpTosNew_Type(Integer32):
    """Custom type fltCurCfgAclIpTosNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgAclIpTosNew_Type.__name__ = "Integer32"
_FltCurCfgAclIpTosNew_Object = MibTableColumn
fltCurCfgAclIpTosNew = _FltCurCfgAclIpTosNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 36),
    _FltCurCfgAclIpTosNew_Type()
)
fltCurCfgAclIpTosNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgAclIpTosNew.setStatus("mandatory")


class _FltCurCfgFwlb_Type(Integer32):
    """Custom type fltCurCfgFwlb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgFwlb_Type.__name__ = "Integer32"
_FltCurCfgFwlb_Object = MibTableColumn
fltCurCfgFwlb = _FltCurCfgFwlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 37),
    _FltCurCfgFwlb_Type()
)
fltCurCfgFwlb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgFwlb.setStatus("mandatory")


class _FltCurCfgNatTimeout_Type(Integer32):
    """Custom type fltCurCfgNatTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_FltCurCfgNatTimeout_Type.__name__ = "Integer32"
_FltCurCfgNatTimeout_Object = MibTableColumn
fltCurCfgNatTimeout = _FltCurCfgNatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 38),
    _FltCurCfgNatTimeout_Type()
)
fltCurCfgNatTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgNatTimeout.setStatus("mandatory")


class _FltCurCfgRurl_Type(Integer32):
    """Custom type fltCurCfgRurl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgRurl_Type.__name__ = "Integer32"
_FltCurCfgRurl_Object = MibTableColumn
fltCurCfgRurl = _FltCurCfgRurl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 39),
    _FltCurCfgRurl_Type()
)
fltCurCfgRurl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgRurl.setStatus("mandatory")


class _FltCurCfgLinklb_Type(Integer32):
    """Custom type fltCurCfgLinklb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgLinklb_Type.__name__ = "Integer32"
_FltCurCfgLinklb_Object = MibTableColumn
fltCurCfgLinklb = _FltCurCfgLinklb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 40),
    _FltCurCfgLinklb_Type()
)
fltCurCfgLinklb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLinklb.setStatus("mandatory")


class _FltCurCfgWapRadiusSnoop_Type(Integer32):
    """Custom type fltCurCfgWapRadiusSnoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgWapRadiusSnoop_Type.__name__ = "Integer32"
_FltCurCfgWapRadiusSnoop_Object = MibTableColumn
fltCurCfgWapRadiusSnoop = _FltCurCfgWapRadiusSnoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 41),
    _FltCurCfgWapRadiusSnoop_Type()
)
fltCurCfgWapRadiusSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgWapRadiusSnoop.setStatus("mandatory")


class _FltCurCfgSrcIpMac_Type(Integer32):
    """Custom type fltCurCfgSrcIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltCurCfgSrcIpMac_Type.__name__ = "Integer32"
_FltCurCfgSrcIpMac_Object = MibTableColumn
fltCurCfgSrcIpMac = _FltCurCfgSrcIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 42),
    _FltCurCfgSrcIpMac_Type()
)
fltCurCfgSrcIpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgSrcIpMac.setStatus("mandatory")


class _FltCurCfgDstIpMac_Type(Integer32):
    """Custom type fltCurCfgDstIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltCurCfgDstIpMac_Type.__name__ = "Integer32"
_FltCurCfgDstIpMac_Object = MibTableColumn
fltCurCfgDstIpMac = _FltCurCfgDstIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 43),
    _FltCurCfgDstIpMac_Type()
)
fltCurCfgDstIpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgDstIpMac.setStatus("mandatory")


class _FltCurCfgIdslbHash_Type(Integer32):
    """Custom type fltCurCfgIdslbHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("dip", 2),
          ("sip", 1))
    )


_FltCurCfgIdslbHash_Type.__name__ = "Integer32"
_FltCurCfgIdslbHash_Object = MibTableColumn
fltCurCfgIdslbHash = _FltCurCfgIdslbHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 44),
    _FltCurCfgIdslbHash_Type()
)
fltCurCfgIdslbHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgIdslbHash.setStatus("mandatory")


class _FltCurCfgVlan_Type(Integer32):
    """Custom type fltCurCfgVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FltCurCfgVlan_Type.__name__ = "Integer32"
_FltCurCfgVlan_Object = MibTableColumn
fltCurCfgVlan = _FltCurCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 45),
    _FltCurCfgVlan_Type()
)
fltCurCfgVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgVlan.setStatus("mandatory")


class _FltCurCfgName_Type(DisplayString):
    """Custom type fltCurCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FltCurCfgName_Type.__name__ = "DisplayString"
_FltCurCfgName_Object = MibTableColumn
fltCurCfgName = _FltCurCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 46),
    _FltCurCfgName_Type()
)
fltCurCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgName.setStatus("mandatory")


class _FltCurCfgTcpRateLimit_Type(Integer32):
    """Custom type fltCurCfgTcpRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgTcpRateLimit_Type.__name__ = "Integer32"
_FltCurCfgTcpRateLimit_Object = MibTableColumn
fltCurCfgTcpRateLimit = _FltCurCfgTcpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 47),
    _FltCurCfgTcpRateLimit_Type()
)
fltCurCfgTcpRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTcpRateLimit.setStatus("mandatory")


class _FltCurCfgTcpRateMaxConn_Type(Integer32):
    """Custom type fltCurCfgTcpRateMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltCurCfgTcpRateMaxConn_Type.__name__ = "Integer32"
_FltCurCfgTcpRateMaxConn_Object = MibTableColumn
fltCurCfgTcpRateMaxConn = _FltCurCfgTcpRateMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 48),
    _FltCurCfgTcpRateMaxConn_Type()
)
fltCurCfgTcpRateMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgTcpRateMaxConn.setStatus("mandatory")


class _FltCurCfgHash_Type(Integer32):
    """Custom type fltCurCfgHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("both", 4),
          ("dip", 3),
          ("sip", 2),
          ("sipsport", 5))
    )


_FltCurCfgHash_Type.__name__ = "Integer32"
_FltCurCfgHash_Object = MibTableColumn
fltCurCfgHash = _FltCurCfgHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 49),
    _FltCurCfgHash_Type()
)
fltCurCfgHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgHash.setStatus("mandatory")


class _FltCurCfgNasa_Type(Integer32):
    """Custom type fltCurCfgNasa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgNasa_Type.__name__ = "Integer32"
_FltCurCfgNasa_Object = MibTableColumn
fltCurCfgNasa = _FltCurCfgNasa_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 50),
    _FltCurCfgNasa_Type()
)
fltCurCfgNasa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgNasa.setStatus("mandatory")


class _FltCurCfgLayer7DenyState_Type(Integer32):
    """Custom type fltCurCfgLayer7DenyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgLayer7DenyState_Type.__name__ = "Integer32"
_FltCurCfgLayer7DenyState_Object = MibTableColumn
fltCurCfgLayer7DenyState = _FltCurCfgLayer7DenyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 51),
    _FltCurCfgLayer7DenyState_Type()
)
fltCurCfgLayer7DenyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLayer7DenyState.setStatus("mandatory")
_FltCurCfgLayer7DenyUrlBmap_Type = OctetString
_FltCurCfgLayer7DenyUrlBmap_Object = MibTableColumn
fltCurCfgLayer7DenyUrlBmap = _FltCurCfgLayer7DenyUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 2, 1, 52),
    _FltCurCfgLayer7DenyUrlBmap_Type()
)
fltCurCfgLayer7DenyUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgLayer7DenyUrlBmap.setStatus("mandatory")
_FltNewCfgTable_Object = MibTable
fltNewCfgTable = _FltNewCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    fltNewCfgTable.setStatus("mandatory")
_FltNewCfgTableEntry_Object = MibTableRow
fltNewCfgTableEntry = _FltNewCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1)
)
fltNewCfgTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "fltNewCfgIndx"),
)
if mibBuilder.loadTexts:
    fltNewCfgTableEntry.setStatus("mandatory")
_FltNewCfgIndx_Type = Integer32
_FltNewCfgIndx_Object = MibTableColumn
fltNewCfgIndx = _FltNewCfgIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 1),
    _FltNewCfgIndx_Type()
)
fltNewCfgIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgIndx.setStatus("mandatory")
_FltNewCfgSrcIp_Type = IpAddress
_FltNewCfgSrcIp_Object = MibTableColumn
fltNewCfgSrcIp = _FltNewCfgSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 2),
    _FltNewCfgSrcIp_Type()
)
fltNewCfgSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgSrcIp.setStatus("mandatory")
_FltNewCfgSrcIpMask_Type = IpAddress
_FltNewCfgSrcIpMask_Object = MibTableColumn
fltNewCfgSrcIpMask = _FltNewCfgSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 3),
    _FltNewCfgSrcIpMask_Type()
)
fltNewCfgSrcIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgSrcIpMask.setStatus("mandatory")
_FltNewCfgDstIp_Type = IpAddress
_FltNewCfgDstIp_Object = MibTableColumn
fltNewCfgDstIp = _FltNewCfgDstIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 4),
    _FltNewCfgDstIp_Type()
)
fltNewCfgDstIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDstIp.setStatus("mandatory")
_FltNewCfgDstIpMask_Type = IpAddress
_FltNewCfgDstIpMask_Object = MibTableColumn
fltNewCfgDstIpMask = _FltNewCfgDstIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 5),
    _FltNewCfgDstIpMask_Type()
)
fltNewCfgDstIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDstIpMask.setStatus("mandatory")
_FltNewCfgProtocol_Type = Integer32
_FltNewCfgProtocol_Object = MibTableColumn
fltNewCfgProtocol = _FltNewCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 6),
    _FltNewCfgProtocol_Type()
)
fltNewCfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgProtocol.setStatus("mandatory")


class _FltNewCfgRangeHighSrcPort_Type(Integer32):
    """Custom type fltNewCfgRangeHighSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeHighSrcPort_Type.__name__ = "Integer32"
_FltNewCfgRangeHighSrcPort_Object = MibTableColumn
fltNewCfgRangeHighSrcPort = _FltNewCfgRangeHighSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 7),
    _FltNewCfgRangeHighSrcPort_Type()
)
fltNewCfgRangeHighSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeHighSrcPort.setStatus("mandatory")


class _FltNewCfgRangeLowSrcPort_Type(Integer32):
    """Custom type fltNewCfgRangeLowSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeLowSrcPort_Type.__name__ = "Integer32"
_FltNewCfgRangeLowSrcPort_Object = MibTableColumn
fltNewCfgRangeLowSrcPort = _FltNewCfgRangeLowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 8),
    _FltNewCfgRangeLowSrcPort_Type()
)
fltNewCfgRangeLowSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeLowSrcPort.setStatus("mandatory")


class _FltNewCfgRangeLowDstPort_Type(Integer32):
    """Custom type fltNewCfgRangeLowDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeLowDstPort_Type.__name__ = "Integer32"
_FltNewCfgRangeLowDstPort_Object = MibTableColumn
fltNewCfgRangeLowDstPort = _FltNewCfgRangeLowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 9),
    _FltNewCfgRangeLowDstPort_Type()
)
fltNewCfgRangeLowDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeLowDstPort.setStatus("mandatory")


class _FltNewCfgRangeHighDstPort_Type(Integer32):
    """Custom type fltNewCfgRangeHighDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRangeHighDstPort_Type.__name__ = "Integer32"
_FltNewCfgRangeHighDstPort_Object = MibTableColumn
fltNewCfgRangeHighDstPort = _FltNewCfgRangeHighDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 10),
    _FltNewCfgRangeHighDstPort_Type()
)
fltNewCfgRangeHighDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRangeHighDstPort.setStatus("mandatory")


class _FltNewCfgAction_Type(Integer32):
    """Custom type fltNewCfgAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2),
          ("nat", 4),
          ("redirect", 3))
    )


_FltNewCfgAction_Type.__name__ = "Integer32"
_FltNewCfgAction_Object = MibTableColumn
fltNewCfgAction = _FltNewCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 11),
    _FltNewCfgAction_Type()
)
fltNewCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAction.setStatus("mandatory")


class _FltNewCfgRedirPort_Type(Integer32):
    """Custom type fltNewCfgRedirPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_FltNewCfgRedirPort_Type.__name__ = "Integer32"
_FltNewCfgRedirPort_Object = MibTableColumn
fltNewCfgRedirPort = _FltNewCfgRedirPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 12),
    _FltNewCfgRedirPort_Type()
)
fltNewCfgRedirPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRedirPort.setStatus("mandatory")
_FltNewCfgRedirGroup_Type = Integer32
_FltNewCfgRedirGroup_Object = MibTableColumn
fltNewCfgRedirGroup = _FltNewCfgRedirGroup_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 13),
    _FltNewCfgRedirGroup_Type()
)
fltNewCfgRedirGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRedirGroup.setStatus("mandatory")


class _FltNewCfgLog_Type(Integer32):
    """Custom type fltNewCfgLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgLog_Type.__name__ = "Integer32"
_FltNewCfgLog_Object = MibTableColumn
fltNewCfgLog = _FltNewCfgLog_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 14),
    _FltNewCfgLog_Type()
)
fltNewCfgLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgLog.setStatus("mandatory")


class _FltNewCfgState_Type(Integer32):
    """Custom type fltNewCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgState_Type.__name__ = "Integer32"
_FltNewCfgState_Object = MibTableColumn
fltNewCfgState = _FltNewCfgState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 15),
    _FltNewCfgState_Type()
)
fltNewCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgState.setStatus("mandatory")


class _FltNewCfgDelete_Type(Integer32):
    """Custom type fltNewCfgDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_FltNewCfgDelete_Type.__name__ = "Integer32"
_FltNewCfgDelete_Object = MibTableColumn
fltNewCfgDelete = _FltNewCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 16),
    _FltNewCfgDelete_Type()
)
fltNewCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDelete.setStatus("mandatory")


class _FltNewCfgNat_Type(Integer32):
    """Custom type fltNewCfgNat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-address", 1),
          ("source-address", 2))
    )


_FltNewCfgNat_Type.__name__ = "Integer32"
_FltNewCfgNat_Object = MibTableColumn
fltNewCfgNat = _FltNewCfgNat_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 17),
    _FltNewCfgNat_Type()
)
fltNewCfgNat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgNat.setStatus("mandatory")


class _FltNewCfgCache_Type(Integer32):
    """Custom type fltNewCfgCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgCache_Type.__name__ = "Integer32"
_FltNewCfgCache_Object = MibTableColumn
fltNewCfgCache = _FltNewCfgCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 18),
    _FltNewCfgCache_Type()
)
fltNewCfgCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgCache.setStatus("mandatory")


class _FltNewCfgInvert_Type(Integer32):
    """Custom type fltNewCfgInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert-off", 2),
          ("invert-on", 1))
    )


_FltNewCfgInvert_Type.__name__ = "Integer32"
_FltNewCfgInvert_Object = MibTableColumn
fltNewCfgInvert = _FltNewCfgInvert_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 19),
    _FltNewCfgInvert_Type()
)
fltNewCfgInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgInvert.setStatus("mandatory")


class _FltNewCfgClientProxy_Type(Integer32):
    """Custom type fltNewCfgClientProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgClientProxy_Type.__name__ = "Integer32"
_FltNewCfgClientProxy_Object = MibTableColumn
fltNewCfgClientProxy = _FltNewCfgClientProxy_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 20),
    _FltNewCfgClientProxy_Type()
)
fltNewCfgClientProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgClientProxy.setStatus("mandatory")


class _FltNewCfgTcpAck_Type(Integer32):
    """Custom type fltNewCfgTcpAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgTcpAck_Type.__name__ = "Integer32"
_FltNewCfgTcpAck_Object = MibTableColumn
fltNewCfgTcpAck = _FltNewCfgTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 21),
    _FltNewCfgTcpAck_Type()
)
fltNewCfgTcpAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgTcpAck.setStatus("mandatory")


class _FltNewCfgUrlRedir_Type(Integer32):
    """Custom type fltNewCfgUrlRedir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgUrlRedir_Type.__name__ = "Integer32"
_FltNewCfgUrlRedir_Object = MibTableColumn
fltNewCfgUrlRedir = _FltNewCfgUrlRedir_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 22),
    _FltNewCfgUrlRedir_Type()
)
fltNewCfgUrlRedir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgUrlRedir.setStatus("mandatory")
_FltNewCfgSrcMac_Type = PhysAddress
_FltNewCfgSrcMac_Object = MibTableColumn
fltNewCfgSrcMac = _FltNewCfgSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 23),
    _FltNewCfgSrcMac_Type()
)
fltNewCfgSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgSrcMac.setStatus("mandatory")
_FltNewCfgDstMac_Type = PhysAddress
_FltNewCfgDstMac_Object = MibTableColumn
fltNewCfgDstMac = _FltNewCfgDstMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 24),
    _FltNewCfgDstMac_Type()
)
fltNewCfgDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDstMac.setStatus("mandatory")


class _FltNewCfgFtpNatActive_Type(Integer32):
    """Custom type fltNewCfgFtpNatActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgFtpNatActive_Type.__name__ = "Integer32"
_FltNewCfgFtpNatActive_Object = MibTableColumn
fltNewCfgFtpNatActive = _FltNewCfgFtpNatActive_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 25),
    _FltNewCfgFtpNatActive_Type()
)
fltNewCfgFtpNatActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgFtpNatActive.setStatus("mandatory")


class _FltNewCfgAclTcpUrg_Type(Integer32):
    """Custom type fltNewCfgAclTcpUrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltNewCfgAclTcpUrg_Type.__name__ = "Integer32"
_FltNewCfgAclTcpUrg_Object = MibTableColumn
fltNewCfgAclTcpUrg = _FltNewCfgAclTcpUrg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 26),
    _FltNewCfgAclTcpUrg_Type()
)
fltNewCfgAclTcpUrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpUrg.setStatus("mandatory")


class _FltNewCfgAclTcpAck_Type(Integer32):
    """Custom type fltNewCfgAclTcpAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltNewCfgAclTcpAck_Type.__name__ = "Integer32"
_FltNewCfgAclTcpAck_Object = MibTableColumn
fltNewCfgAclTcpAck = _FltNewCfgAclTcpAck_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 27),
    _FltNewCfgAclTcpAck_Type()
)
fltNewCfgAclTcpAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpAck.setStatus("mandatory")


class _FltNewCfgAclTcpPsh_Type(Integer32):
    """Custom type fltNewCfgAclTcpPsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltNewCfgAclTcpPsh_Type.__name__ = "Integer32"
_FltNewCfgAclTcpPsh_Object = MibTableColumn
fltNewCfgAclTcpPsh = _FltNewCfgAclTcpPsh_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 28),
    _FltNewCfgAclTcpPsh_Type()
)
fltNewCfgAclTcpPsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpPsh.setStatus("mandatory")


class _FltNewCfgAclTcpRst_Type(Integer32):
    """Custom type fltNewCfgAclTcpRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltNewCfgAclTcpRst_Type.__name__ = "Integer32"
_FltNewCfgAclTcpRst_Object = MibTableColumn
fltNewCfgAclTcpRst = _FltNewCfgAclTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 29),
    _FltNewCfgAclTcpRst_Type()
)
fltNewCfgAclTcpRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpRst.setStatus("mandatory")


class _FltNewCfgAclTcpSyn_Type(Integer32):
    """Custom type fltNewCfgAclTcpSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltNewCfgAclTcpSyn_Type.__name__ = "Integer32"
_FltNewCfgAclTcpSyn_Object = MibTableColumn
fltNewCfgAclTcpSyn = _FltNewCfgAclTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 30),
    _FltNewCfgAclTcpSyn_Type()
)
fltNewCfgAclTcpSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpSyn.setStatus("mandatory")


class _FltNewCfgAclTcpFin_Type(Integer32):
    """Custom type fltNewCfgAclTcpFin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltNewCfgAclTcpFin_Type.__name__ = "Integer32"
_FltNewCfgAclTcpFin_Object = MibTableColumn
fltNewCfgAclTcpFin = _FltNewCfgAclTcpFin_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 31),
    _FltNewCfgAclTcpFin_Type()
)
fltNewCfgAclTcpFin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclTcpFin.setStatus("mandatory")


class _FltNewCfgAclIcmp_Type(Integer32):
    """Custom type fltNewCfgAclIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIcmp_Type.__name__ = "Integer32"
_FltNewCfgAclIcmp_Object = MibTableColumn
fltNewCfgAclIcmp = _FltNewCfgAclIcmp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 32),
    _FltNewCfgAclIcmp_Type()
)
fltNewCfgAclIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIcmp.setStatus("mandatory")


class _FltNewCfgAclIpOption_Type(Integer32):
    """Custom type fltNewCfgAclIpOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_FltNewCfgAclIpOption_Type.__name__ = "Integer32"
_FltNewCfgAclIpOption_Object = MibTableColumn
fltNewCfgAclIpOption = _FltNewCfgAclIpOption_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 33),
    _FltNewCfgAclIpOption_Type()
)
fltNewCfgAclIpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpOption.setStatus("mandatory")
_FltNewCfgBwmContract_Type = Integer32
_FltNewCfgBwmContract_Object = MibTableColumn
fltNewCfgBwmContract = _FltNewCfgBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 34),
    _FltNewCfgBwmContract_Type()
)
fltNewCfgBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgBwmContract.setStatus("mandatory")


class _FltNewCfgAclIpTos_Type(Integer32):
    """Custom type fltNewCfgAclIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTos_Type.__name__ = "Integer32"
_FltNewCfgAclIpTos_Object = MibTableColumn
fltNewCfgAclIpTos = _FltNewCfgAclIpTos_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 35),
    _FltNewCfgAclIpTos_Type()
)
fltNewCfgAclIpTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTos.setStatus("mandatory")


class _FltNewCfgAclIpTosMask_Type(Integer32):
    """Custom type fltNewCfgAclIpTosMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTosMask_Type.__name__ = "Integer32"
_FltNewCfgAclIpTosMask_Object = MibTableColumn
fltNewCfgAclIpTosMask = _FltNewCfgAclIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 36),
    _FltNewCfgAclIpTosMask_Type()
)
fltNewCfgAclIpTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTosMask.setStatus("mandatory")


class _FltNewCfgAclIpTosNew_Type(Integer32):
    """Custom type fltNewCfgAclIpTosNew based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgAclIpTosNew_Type.__name__ = "Integer32"
_FltNewCfgAclIpTosNew_Object = MibTableColumn
fltNewCfgAclIpTosNew = _FltNewCfgAclIpTosNew_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 37),
    _FltNewCfgAclIpTosNew_Type()
)
fltNewCfgAclIpTosNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgAclIpTosNew.setStatus("mandatory")


class _FltNewCfgFwlb_Type(Integer32):
    """Custom type fltNewCfgFwlb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgFwlb_Type.__name__ = "Integer32"
_FltNewCfgFwlb_Object = MibTableColumn
fltNewCfgFwlb = _FltNewCfgFwlb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 38),
    _FltNewCfgFwlb_Type()
)
fltNewCfgFwlb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgFwlb.setStatus("mandatory")


class _FltNewCfgNatTimeout_Type(Integer32):
    """Custom type fltNewCfgNatTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_FltNewCfgNatTimeout_Type.__name__ = "Integer32"
_FltNewCfgNatTimeout_Object = MibTableColumn
fltNewCfgNatTimeout = _FltNewCfgNatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 39),
    _FltNewCfgNatTimeout_Type()
)
fltNewCfgNatTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgNatTimeout.setStatus("mandatory")


class _FltNewCfgRurl_Type(Integer32):
    """Custom type fltNewCfgRurl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgRurl_Type.__name__ = "Integer32"
_FltNewCfgRurl_Object = MibTableColumn
fltNewCfgRurl = _FltNewCfgRurl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 40),
    _FltNewCfgRurl_Type()
)
fltNewCfgRurl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgRurl.setStatus("mandatory")


class _FltNewCfgLinklb_Type(Integer32):
    """Custom type fltNewCfgLinklb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgLinklb_Type.__name__ = "Integer32"
_FltNewCfgLinklb_Object = MibTableColumn
fltNewCfgLinklb = _FltNewCfgLinklb_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 41),
    _FltNewCfgLinklb_Type()
)
fltNewCfgLinklb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgLinklb.setStatus("mandatory")


class _FltNewCfgWapRadiusSnoop_Type(Integer32):
    """Custom type fltNewCfgWapRadiusSnoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgWapRadiusSnoop_Type.__name__ = "Integer32"
_FltNewCfgWapRadiusSnoop_Object = MibTableColumn
fltNewCfgWapRadiusSnoop = _FltNewCfgWapRadiusSnoop_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 42),
    _FltNewCfgWapRadiusSnoop_Type()
)
fltNewCfgWapRadiusSnoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgWapRadiusSnoop.setStatus("mandatory")


class _FltNewCfgSrcIpMac_Type(Integer32):
    """Custom type fltNewCfgSrcIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltNewCfgSrcIpMac_Type.__name__ = "Integer32"
_FltNewCfgSrcIpMac_Object = MibTableColumn
fltNewCfgSrcIpMac = _FltNewCfgSrcIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 43),
    _FltNewCfgSrcIpMac_Type()
)
fltNewCfgSrcIpMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgSrcIpMac.setStatus("mandatory")


class _FltNewCfgDstIpMac_Type(Integer32):
    """Custom type fltNewCfgDstIpMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_FltNewCfgDstIpMac_Type.__name__ = "Integer32"
_FltNewCfgDstIpMac_Object = MibTableColumn
fltNewCfgDstIpMac = _FltNewCfgDstIpMac_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 44),
    _FltNewCfgDstIpMac_Type()
)
fltNewCfgDstIpMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgDstIpMac.setStatus("mandatory")


class _FltNewCfgIdslbHash_Type(Integer32):
    """Custom type fltNewCfgIdslbHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("dip", 2),
          ("sip", 1))
    )


_FltNewCfgIdslbHash_Type.__name__ = "Integer32"
_FltNewCfgIdslbHash_Object = MibTableColumn
fltNewCfgIdslbHash = _FltNewCfgIdslbHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 45),
    _FltNewCfgIdslbHash_Type()
)
fltNewCfgIdslbHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgIdslbHash.setStatus("mandatory")


class _FltNewCfgVlan_Type(Integer32):
    """Custom type fltNewCfgVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FltNewCfgVlan_Type.__name__ = "Integer32"
_FltNewCfgVlan_Object = MibTableColumn
fltNewCfgVlan = _FltNewCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 46),
    _FltNewCfgVlan_Type()
)
fltNewCfgVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgVlan.setStatus("mandatory")


class _FltNewCfgName_Type(DisplayString):
    """Custom type fltNewCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FltNewCfgName_Type.__name__ = "DisplayString"
_FltNewCfgName_Object = MibTableColumn
fltNewCfgName = _FltNewCfgName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 47),
    _FltNewCfgName_Type()
)
fltNewCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgName.setStatus("mandatory")


class _FltNewCfgTcpRateLimit_Type(Integer32):
    """Custom type fltNewCfgTcpRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgTcpRateLimit_Type.__name__ = "Integer32"
_FltNewCfgTcpRateLimit_Object = MibTableColumn
fltNewCfgTcpRateLimit = _FltNewCfgTcpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 48),
    _FltNewCfgTcpRateLimit_Type()
)
fltNewCfgTcpRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgTcpRateLimit.setStatus("mandatory")


class _FltNewCfgTcpRateMaxConn_Type(Integer32):
    """Custom type fltNewCfgTcpRateMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FltNewCfgTcpRateMaxConn_Type.__name__ = "Integer32"
_FltNewCfgTcpRateMaxConn_Object = MibTableColumn
fltNewCfgTcpRateMaxConn = _FltNewCfgTcpRateMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 49),
    _FltNewCfgTcpRateMaxConn_Type()
)
fltNewCfgTcpRateMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgTcpRateMaxConn.setStatus("mandatory")


class _FltNewCfgHash_Type(Integer32):
    """Custom type fltNewCfgHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("both", 4),
          ("dip", 3),
          ("sip", 2),
          ("sipsport", 5))
    )


_FltNewCfgHash_Type.__name__ = "Integer32"
_FltNewCfgHash_Object = MibTableColumn
fltNewCfgHash = _FltNewCfgHash_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 50),
    _FltNewCfgHash_Type()
)
fltNewCfgHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgHash.setStatus("mandatory")


class _FltNewCfgNasa_Type(Integer32):
    """Custom type fltNewCfgNasa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgNasa_Type.__name__ = "Integer32"
_FltNewCfgNasa_Object = MibTableColumn
fltNewCfgNasa = _FltNewCfgNasa_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 51),
    _FltNewCfgNasa_Type()
)
fltNewCfgNasa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgNasa.setStatus("mandatory")


class _FltNewCfgLayer7DenyState_Type(Integer32):
    """Custom type fltNewCfgLayer7DenyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgLayer7DenyState_Type.__name__ = "Integer32"
_FltNewCfgLayer7DenyState_Object = MibTableColumn
fltNewCfgLayer7DenyState = _FltNewCfgLayer7DenyState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 52),
    _FltNewCfgLayer7DenyState_Type()
)
fltNewCfgLayer7DenyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyState.setStatus("mandatory")
_FltNewCfgLayer7DenyUrlBmap_Type = OctetString
_FltNewCfgLayer7DenyUrlBmap_Object = MibTableColumn
fltNewCfgLayer7DenyUrlBmap = _FltNewCfgLayer7DenyUrlBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 53),
    _FltNewCfgLayer7DenyUrlBmap_Type()
)
fltNewCfgLayer7DenyUrlBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyUrlBmap.setStatus("mandatory")
_FltNewCfgLayer7DenyAddUrl_Type = Integer32
_FltNewCfgLayer7DenyAddUrl_Object = MibTableColumn
fltNewCfgLayer7DenyAddUrl = _FltNewCfgLayer7DenyAddUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 54),
    _FltNewCfgLayer7DenyAddUrl_Type()
)
fltNewCfgLayer7DenyAddUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyAddUrl.setStatus("mandatory")
_FltNewCfgLayer7DenyRemUrl_Type = Integer32
_FltNewCfgLayer7DenyRemUrl_Object = MibTableColumn
fltNewCfgLayer7DenyRemUrl = _FltNewCfgLayer7DenyRemUrl_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 3, 1, 55),
    _FltNewCfgLayer7DenyRemUrl_Type()
)
fltNewCfgLayer7DenyRemUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgLayer7DenyRemUrl.setStatus("mandatory")
_FltCurCfgPortTable_Object = MibTable
fltCurCfgPortTable = _FltCurCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4)
)
if mibBuilder.loadTexts:
    fltCurCfgPortTable.setStatus("mandatory")
_FltCurCfgPortTableEntry_Object = MibTableRow
fltCurCfgPortTableEntry = _FltCurCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1)
)
fltCurCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "fltCurCfgPortIndx"),
)
if mibBuilder.loadTexts:
    fltCurCfgPortTableEntry.setStatus("mandatory")
_FltCurCfgPortIndx_Type = Integer32
_FltCurCfgPortIndx_Object = MibTableColumn
fltCurCfgPortIndx = _FltCurCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1, 1),
    _FltCurCfgPortIndx_Type()
)
fltCurCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortIndx.setStatus("mandatory")


class _FltCurCfgPortState_Type(Integer32):
    """Custom type fltCurCfgPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltCurCfgPortState_Type.__name__ = "Integer32"
_FltCurCfgPortState_Object = MibTableColumn
fltCurCfgPortState = _FltCurCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1, 2),
    _FltCurCfgPortState_Type()
)
fltCurCfgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortState.setStatus("mandatory")


class _FltCurCfgPortFiltBmap_Type(OctetString):
    """Custom type fltCurCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FltCurCfgPortFiltBmap_Type.__name__ = "OctetString"
_FltCurCfgPortFiltBmap_Object = MibTableColumn
fltCurCfgPortFiltBmap = _FltCurCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 4, 1, 3),
    _FltCurCfgPortFiltBmap_Type()
)
fltCurCfgPortFiltBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgPortFiltBmap.setStatus("mandatory")
_FltNewCfgPortTable_Object = MibTable
fltNewCfgPortTable = _FltNewCfgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5)
)
if mibBuilder.loadTexts:
    fltNewCfgPortTable.setStatus("mandatory")
_FltNewCfgPortTableEntry_Object = MibTableRow
fltNewCfgPortTableEntry = _FltNewCfgPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1)
)
fltNewCfgPortTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "fltNewCfgPortIndx"),
)
if mibBuilder.loadTexts:
    fltNewCfgPortTableEntry.setStatus("mandatory")
_FltNewCfgPortIndx_Type = Integer32
_FltNewCfgPortIndx_Object = MibTableColumn
fltNewCfgPortIndx = _FltNewCfgPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 1),
    _FltNewCfgPortIndx_Type()
)
fltNewCfgPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgPortIndx.setStatus("mandatory")


class _FltNewCfgPortState_Type(Integer32):
    """Custom type fltNewCfgPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_FltNewCfgPortState_Type.__name__ = "Integer32"
_FltNewCfgPortState_Object = MibTableColumn
fltNewCfgPortState = _FltNewCfgPortState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 2),
    _FltNewCfgPortState_Type()
)
fltNewCfgPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgPortState.setStatus("mandatory")


class _FltNewCfgPortFiltBmap_Type(OctetString):
    """Custom type fltNewCfgPortFiltBmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FltNewCfgPortFiltBmap_Type.__name__ = "OctetString"
_FltNewCfgPortFiltBmap_Object = MibTableColumn
fltNewCfgPortFiltBmap = _FltNewCfgPortFiltBmap_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 3),
    _FltNewCfgPortFiltBmap_Type()
)
fltNewCfgPortFiltBmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgPortFiltBmap.setStatus("mandatory")
_FltNewCfgPortAddFiltRule_Type = Integer32
_FltNewCfgPortAddFiltRule_Object = MibTableColumn
fltNewCfgPortAddFiltRule = _FltNewCfgPortAddFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 4),
    _FltNewCfgPortAddFiltRule_Type()
)
fltNewCfgPortAddFiltRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgPortAddFiltRule.setStatus("mandatory")
_FltNewCfgPortRemFiltRule_Type = Integer32
_FltNewCfgPortRemFiltRule_Object = MibTableColumn
fltNewCfgPortRemFiltRule = _FltNewCfgPortRemFiltRule_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 5, 1, 5),
    _FltNewCfgPortRemFiltRule_Type()
)
fltNewCfgPortRemFiltRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgPortRemFiltRule.setStatus("mandatory")
_FltCurCfgUrlBwmTable_Object = MibTable
fltCurCfgUrlBwmTable = _FltCurCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 6)
)
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmTable.setStatus("mandatory")
_FltCurCfgUrlBwmEntry_Object = MibTableRow
fltCurCfgUrlBwmEntry = _FltCurCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 6, 1)
)
fltCurCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "fltCurCfgUrlBwmFltIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "fltCurCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmEntry.setStatus("mandatory")
_FltCurCfgUrlBwmFltIndex_Type = Integer32
_FltCurCfgUrlBwmFltIndex_Object = MibTableColumn
fltCurCfgUrlBwmFltIndex = _FltCurCfgUrlBwmFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 6, 1, 1),
    _FltCurCfgUrlBwmFltIndex_Type()
)
fltCurCfgUrlBwmFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmFltIndex.setStatus("mandatory")
_FltCurCfgUrlBwmUrlId_Type = Integer32
_FltCurCfgUrlBwmUrlId_Object = MibTableColumn
fltCurCfgUrlBwmUrlId = _FltCurCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 6, 1, 2),
    _FltCurCfgUrlBwmUrlId_Type()
)
fltCurCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmUrlId.setStatus("mandatory")
_FltCurCfgUrlBwmContract_Type = Integer32
_FltCurCfgUrlBwmContract_Object = MibTableColumn
fltCurCfgUrlBwmContract = _FltCurCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 6, 1, 3),
    _FltCurCfgUrlBwmContract_Type()
)
fltCurCfgUrlBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltCurCfgUrlBwmContract.setStatus("mandatory")
_FltNewCfgUrlBwmTable_Object = MibTable
fltNewCfgUrlBwmTable = _FltNewCfgUrlBwmTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 7)
)
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmTable.setStatus("mandatory")
_FltNewCfgUrlBwmEntry_Object = MibTableRow
fltNewCfgUrlBwmEntry = _FltNewCfgUrlBwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 7, 1)
)
fltNewCfgUrlBwmEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "fltNewCfgUrlBwmFltIndex"),
    (0, "ALTEON-TS-LAYER4-MIB", "fltNewCfgUrlBwmUrlId"),
)
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmEntry.setStatus("mandatory")
_FltNewCfgUrlBwmFltIndex_Type = Integer32
_FltNewCfgUrlBwmFltIndex_Object = MibTableColumn
fltNewCfgUrlBwmFltIndex = _FltNewCfgUrlBwmFltIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 7, 1, 1),
    _FltNewCfgUrlBwmFltIndex_Type()
)
fltNewCfgUrlBwmFltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmFltIndex.setStatus("mandatory")
_FltNewCfgUrlBwmUrlId_Type = Integer32
_FltNewCfgUrlBwmUrlId_Object = MibTableColumn
fltNewCfgUrlBwmUrlId = _FltNewCfgUrlBwmUrlId_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 7, 1, 2),
    _FltNewCfgUrlBwmUrlId_Type()
)
fltNewCfgUrlBwmUrlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmUrlId.setStatus("mandatory")
_FltNewCfgUrlBwmContract_Type = Integer32
_FltNewCfgUrlBwmContract_Object = MibTableColumn
fltNewCfgUrlBwmContract = _FltNewCfgUrlBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 7, 1, 3),
    _FltNewCfgUrlBwmContract_Type()
)
fltNewCfgUrlBwmContract.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmContract.setStatus("mandatory")


class _FltNewCfgUrlBwmDelete_Type(Integer32):
    """Custom type fltNewCfgUrlBwmDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_FltNewCfgUrlBwmDelete_Type.__name__ = "Integer32"
_FltNewCfgUrlBwmDelete_Object = MibTableColumn
fltNewCfgUrlBwmDelete = _FltNewCfgUrlBwmDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 7, 1, 4),
    _FltNewCfgUrlBwmDelete_Type()
)
fltNewCfgUrlBwmDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fltNewCfgUrlBwmDelete.setStatus("mandatory")
_FltUrlBwmTableMaxSize_Type = Integer32
_FltUrlBwmTableMaxSize_Object = MibScalar
fltUrlBwmTableMaxSize = _FltUrlBwmTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 10, 8),
    _FltUrlBwmTableMaxSize_Type()
)
fltUrlBwmTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fltUrlBwmTableMaxSize.setStatus("mandatory")
_GlobalSLB_ObjectIdentity = ObjectIdentity
globalSLB = _GlobalSLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11)
)
_GslbGeneral_ObjectIdentity = ObjectIdentity
gslbGeneral = _GslbGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1)
)


class _GslbCurCfgGenState_Type(Integer32):
    """Custom type gslbCurCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_GslbCurCfgGenState_Type.__name__ = "Integer32"
_GslbCurCfgGenState_Object = MibScalar
gslbCurCfgGenState = _GslbCurCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 1),
    _GslbCurCfgGenState_Type()
)
gslbCurCfgGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenState.setStatus("mandatory")


class _GslbNewCfgGenState_Type(Integer32):
    """Custom type gslbNewCfgGenState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_GslbNewCfgGenState_Type.__name__ = "Integer32"
_GslbNewCfgGenState_Object = MibScalar
gslbNewCfgGenState = _GslbNewCfgGenState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 2),
    _GslbNewCfgGenState_Type()
)
gslbNewCfgGenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenState.setStatus("mandatory")


class _GslbCurCfgGenDnsHandoff_Type(Integer32):
    """Custom type gslbCurCfgGenDnsHandoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenDnsHandoff_Type.__name__ = "Integer32"
_GslbCurCfgGenDnsHandoff_Object = MibScalar
gslbCurCfgGenDnsHandoff = _GslbCurCfgGenDnsHandoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 3),
    _GslbCurCfgGenDnsHandoff_Type()
)
gslbCurCfgGenDnsHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenDnsHandoff.setStatus("mandatory")


class _GslbNewCfgGenDnsHandoff_Type(Integer32):
    """Custom type gslbNewCfgGenDnsHandoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenDnsHandoff_Type.__name__ = "Integer32"
_GslbNewCfgGenDnsHandoff_Object = MibScalar
gslbNewCfgGenDnsHandoff = _GslbNewCfgGenDnsHandoff_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 4),
    _GslbNewCfgGenDnsHandoff_Type()
)
gslbNewCfgGenDnsHandoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenDnsHandoff.setStatus("mandatory")


class _GslbCurCfgGenDnsTTL_Type(Integer32):
    """Custom type gslbCurCfgGenDnsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbCurCfgGenDnsTTL_Type.__name__ = "Integer32"
_GslbCurCfgGenDnsTTL_Object = MibScalar
gslbCurCfgGenDnsTTL = _GslbCurCfgGenDnsTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 5),
    _GslbCurCfgGenDnsTTL_Type()
)
gslbCurCfgGenDnsTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenDnsTTL.setStatus("mandatory")


class _GslbNewCfgGenDnsTTL_Type(Integer32):
    """Custom type gslbNewCfgGenDnsTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbNewCfgGenDnsTTL_Type.__name__ = "Integer32"
_GslbNewCfgGenDnsTTL_Object = MibScalar
gslbNewCfgGenDnsTTL = _GslbNewCfgGenDnsTTL_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 6),
    _GslbNewCfgGenDnsTTL_Type()
)
gslbNewCfgGenDnsTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenDnsTTL.setStatus("mandatory")


class _GslbCurCfgGenHttpRedirect_Type(Integer32):
    """Custom type gslbCurCfgGenHttpRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenHttpRedirect_Type.__name__ = "Integer32"
_GslbCurCfgGenHttpRedirect_Object = MibScalar
gslbCurCfgGenHttpRedirect = _GslbCurCfgGenHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 7),
    _GslbCurCfgGenHttpRedirect_Type()
)
gslbCurCfgGenHttpRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenHttpRedirect.setStatus("mandatory")


class _GslbNewCfgGenHttpRedirect_Type(Integer32):
    """Custom type gslbNewCfgGenHttpRedirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenHttpRedirect_Type.__name__ = "Integer32"
_GslbNewCfgGenHttpRedirect_Object = MibScalar
gslbNewCfgGenHttpRedirect = _GslbNewCfgGenHttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 8),
    _GslbNewCfgGenHttpRedirect_Type()
)
gslbNewCfgGenHttpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenHttpRedirect.setStatus("mandatory")


class _GslbCurCfgGenRemSiteUpdateInterval_Type(Integer32):
    """Custom type gslbCurCfgGenRemSiteUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_GslbCurCfgGenRemSiteUpdateInterval_Type.__name__ = "Integer32"
_GslbCurCfgGenRemSiteUpdateInterval_Object = MibScalar
gslbCurCfgGenRemSiteUpdateInterval = _GslbCurCfgGenRemSiteUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 9),
    _GslbCurCfgGenRemSiteUpdateInterval_Type()
)
gslbCurCfgGenRemSiteUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenRemSiteUpdateInterval.setStatus("mandatory")


class _GslbNewCfgGenRemSiteUpdateInterval_Type(Integer32):
    """Custom type gslbNewCfgGenRemSiteUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_GslbNewCfgGenRemSiteUpdateInterval_Type.__name__ = "Integer32"
_GslbNewCfgGenRemSiteUpdateInterval_Object = MibScalar
gslbNewCfgGenRemSiteUpdateInterval = _GslbNewCfgGenRemSiteUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 10),
    _GslbNewCfgGenRemSiteUpdateInterval_Type()
)
gslbNewCfgGenRemSiteUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenRemSiteUpdateInterval.setStatus("mandatory")


class _GslbCurCfgGenDnsLocalPref_Type(Integer32):
    """Custom type gslbCurCfgGenDnsLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenDnsLocalPref_Type.__name__ = "Integer32"
_GslbCurCfgGenDnsLocalPref_Object = MibScalar
gslbCurCfgGenDnsLocalPref = _GslbCurCfgGenDnsLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 11),
    _GslbCurCfgGenDnsLocalPref_Type()
)
gslbCurCfgGenDnsLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenDnsLocalPref.setStatus("mandatory")


class _GslbNewCfgGenDnsLocalPref_Type(Integer32):
    """Custom type gslbNewCfgGenDnsLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenDnsLocalPref_Type.__name__ = "Integer32"
_GslbNewCfgGenDnsLocalPref_Object = MibScalar
gslbNewCfgGenDnsLocalPref = _GslbNewCfgGenDnsLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 12),
    _GslbNewCfgGenDnsLocalPref_Type()
)
gslbNewCfgGenDnsLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenDnsLocalPref.setStatus("mandatory")


class _GslbCurCfgGenMinco_Type(Integer32):
    """Custom type gslbCurCfgGenMinco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbCurCfgGenMinco_Type.__name__ = "Integer32"
_GslbCurCfgGenMinco_Object = MibScalar
gslbCurCfgGenMinco = _GslbCurCfgGenMinco_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 13),
    _GslbCurCfgGenMinco_Type()
)
gslbCurCfgGenMinco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenMinco.setStatus("mandatory")


class _GslbNewCfgGenMinco_Type(Integer32):
    """Custom type gslbNewCfgGenMinco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GslbNewCfgGenMinco_Type.__name__ = "Integer32"
_GslbNewCfgGenMinco_Object = MibScalar
gslbNewCfgGenMinco = _GslbNewCfgGenMinco_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 14),
    _GslbNewCfgGenMinco_Type()
)
gslbNewCfgGenMinco.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenMinco.setStatus("mandatory")


class _GslbCurCfgGenOne_Type(Integer32):
    """Custom type gslbCurCfgGenOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenOne_Type.__name__ = "Integer32"
_GslbCurCfgGenOne_Object = MibScalar
gslbCurCfgGenOne = _GslbCurCfgGenOne_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 15),
    _GslbCurCfgGenOne_Type()
)
gslbCurCfgGenOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenOne.setStatus("mandatory")


class _GslbNewCfgGenOne_Type(Integer32):
    """Custom type gslbNewCfgGenOne based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenOne_Type.__name__ = "Integer32"
_GslbNewCfgGenOne_Object = MibScalar
gslbNewCfgGenOne = _GslbNewCfgGenOne_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 16),
    _GslbNewCfgGenOne_Type()
)
gslbNewCfgGenOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenOne.setStatus("mandatory")


class _GslbCurCfgGenUsern_Type(Integer32):
    """Custom type gslbCurCfgGenUsern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenUsern_Type.__name__ = "Integer32"
_GslbCurCfgGenUsern_Object = MibScalar
gslbCurCfgGenUsern = _GslbCurCfgGenUsern_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 17),
    _GslbCurCfgGenUsern_Type()
)
gslbCurCfgGenUsern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenUsern.setStatus("mandatory")


class _GslbNewCfgGenUsern_Type(Integer32):
    """Custom type gslbNewCfgGenUsern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenUsern_Type.__name__ = "Integer32"
_GslbNewCfgGenUsern_Object = MibScalar
gslbNewCfgGenUsern = _GslbNewCfgGenUsern_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 18),
    _GslbNewCfgGenUsern_Type()
)
gslbNewCfgGenUsern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenUsern.setStatus("mandatory")


class _GslbCurCfgGenGeo_Type(Integer32):
    """Custom type gslbCurCfgGenGeo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenGeo_Type.__name__ = "Integer32"
_GslbCurCfgGenGeo_Object = MibScalar
gslbCurCfgGenGeo = _GslbCurCfgGenGeo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 19),
    _GslbCurCfgGenGeo_Type()
)
gslbCurCfgGenGeo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenGeo.setStatus("mandatory")


class _GslbNewCfgGenGeo_Type(Integer32):
    """Custom type gslbNewCfgGenGeo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenGeo_Type.__name__ = "Integer32"
_GslbNewCfgGenGeo_Object = MibScalar
gslbNewCfgGenGeo = _GslbNewCfgGenGeo_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 20),
    _GslbNewCfgGenGeo_Type()
)
gslbNewCfgGenGeo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenGeo.setStatus("mandatory")


class _GslbCurCfgGenAlways_Type(Integer32):
    """Custom type gslbCurCfgGenAlways based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenAlways_Type.__name__ = "Integer32"
_GslbCurCfgGenAlways_Object = MibScalar
gslbCurCfgGenAlways = _GslbCurCfgGenAlways_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 21),
    _GslbCurCfgGenAlways_Type()
)
gslbCurCfgGenAlways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenAlways.setStatus("mandatory")


class _GslbNewCfgGenAlways_Type(Integer32):
    """Custom type gslbNewCfgGenAlways based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenAlways_Type.__name__ = "Integer32"
_GslbNewCfgGenAlways_Object = MibScalar
gslbNewCfgGenAlways = _GslbNewCfgGenAlways_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 22),
    _GslbNewCfgGenAlways_Type()
)
gslbNewCfgGenAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenAlways.setStatus("mandatory")


class _GslbCurCfgGenWeight_Type(Integer32):
    """Custom type gslbCurCfgGenWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_GslbCurCfgGenWeight_Type.__name__ = "Integer32"
_GslbCurCfgGenWeight_Object = MibScalar
gslbCurCfgGenWeight = _GslbCurCfgGenWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 23),
    _GslbCurCfgGenWeight_Type()
)
gslbCurCfgGenWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenWeight.setStatus("mandatory")


class _GslbNewCfgGenWeight_Type(Integer32):
    """Custom type gslbNewCfgGenWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_GslbNewCfgGenWeight_Type.__name__ = "Integer32"
_GslbNewCfgGenWeight_Object = MibScalar
gslbNewCfgGenWeight = _GslbNewCfgGenWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 1, 24),
    _GslbNewCfgGenWeight_Type()
)
gslbNewCfgGenWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenWeight.setStatus("mandatory")
_GslbDNS_ObjectIdentity = ObjectIdentity
gslbDNS = _GslbDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2)
)
_DnsCurCfgPrimaryIpAddr_Type = IpAddress
_DnsCurCfgPrimaryIpAddr_Object = MibScalar
dnsCurCfgPrimaryIpAddr = _DnsCurCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 1),
    _DnsCurCfgPrimaryIpAddr_Type()
)
dnsCurCfgPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgPrimaryIpAddr.setStatus("mandatory")
_DnsNewCfgPrimaryIpAddr_Type = IpAddress
_DnsNewCfgPrimaryIpAddr_Object = MibScalar
dnsNewCfgPrimaryIpAddr = _DnsNewCfgPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 2),
    _DnsNewCfgPrimaryIpAddr_Type()
)
dnsNewCfgPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgPrimaryIpAddr.setStatus("mandatory")
_DnsCurCfgSecondaryIpAddr_Type = IpAddress
_DnsCurCfgSecondaryIpAddr_Object = MibScalar
dnsCurCfgSecondaryIpAddr = _DnsCurCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 3),
    _DnsCurCfgSecondaryIpAddr_Type()
)
dnsCurCfgSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgSecondaryIpAddr.setStatus("mandatory")
_DnsNewCfgSecondaryIpAddr_Type = IpAddress
_DnsNewCfgSecondaryIpAddr_Object = MibScalar
dnsNewCfgSecondaryIpAddr = _DnsNewCfgSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 4),
    _DnsNewCfgSecondaryIpAddr_Type()
)
dnsNewCfgSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgSecondaryIpAddr.setStatus("mandatory")


class _DnsCurCfgDomainName_Type(DisplayString):
    """Custom type dnsCurCfgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 191),
    )


_DnsCurCfgDomainName_Type.__name__ = "DisplayString"
_DnsCurCfgDomainName_Object = MibScalar
dnsCurCfgDomainName = _DnsCurCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 5),
    _DnsCurCfgDomainName_Type()
)
dnsCurCfgDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCurCfgDomainName.setStatus("mandatory")


class _DnsNewCfgDomainName_Type(DisplayString):
    """Custom type dnsNewCfgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 191),
    )


_DnsNewCfgDomainName_Type.__name__ = "DisplayString"
_DnsNewCfgDomainName_Object = MibScalar
dnsNewCfgDomainName = _DnsNewCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 2, 6),
    _DnsNewCfgDomainName_Type()
)
dnsNewCfgDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNewCfgDomainName.setStatus("mandatory")
_GslbSites_ObjectIdentity = ObjectIdentity
gslbSites = _GslbSites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3)
)
_GslbRemSiteTableMaxSize_Type = Integer32
_GslbRemSiteTableMaxSize_Object = MibScalar
gslbRemSiteTableMaxSize = _GslbRemSiteTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 1),
    _GslbRemSiteTableMaxSize_Type()
)
gslbRemSiteTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbRemSiteTableMaxSize.setStatus("mandatory")
_GslbCurCfgRemSiteTable_Object = MibTable
gslbCurCfgRemSiteTable = _GslbCurCfgRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2)
)
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteTable.setStatus("mandatory")
_GslbCurCfgRemSiteTableEntry_Object = MibTableRow
gslbCurCfgRemSiteTableEntry = _GslbCurCfgRemSiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1)
)
gslbCurCfgRemSiteTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "gslbCurCfgRemSiteIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteTableEntry.setStatus("mandatory")
_GslbCurCfgRemSiteIndx_Type = Integer32
_GslbCurCfgRemSiteIndx_Object = MibTableColumn
gslbCurCfgRemSiteIndx = _GslbCurCfgRemSiteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 1),
    _GslbCurCfgRemSiteIndx_Type()
)
gslbCurCfgRemSiteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteIndx.setStatus("mandatory")
_GslbCurCfgRemSitePrimaryIp_Type = IpAddress
_GslbCurCfgRemSitePrimaryIp_Object = MibTableColumn
gslbCurCfgRemSitePrimaryIp = _GslbCurCfgRemSitePrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 2),
    _GslbCurCfgRemSitePrimaryIp_Type()
)
gslbCurCfgRemSitePrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSitePrimaryIp.setStatus("mandatory")
_GslbCurCfgRemSiteSecondaryIp_Type = IpAddress
_GslbCurCfgRemSiteSecondaryIp_Object = MibTableColumn
gslbCurCfgRemSiteSecondaryIp = _GslbCurCfgRemSiteSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 3),
    _GslbCurCfgRemSiteSecondaryIp_Type()
)
gslbCurCfgRemSiteSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteSecondaryIp.setStatus("mandatory")


class _GslbCurCfgRemSiteState_Type(Integer32):
    """Custom type gslbCurCfgRemSiteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgRemSiteState_Type.__name__ = "Integer32"
_GslbCurCfgRemSiteState_Object = MibTableColumn
gslbCurCfgRemSiteState = _GslbCurCfgRemSiteState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 4),
    _GslbCurCfgRemSiteState_Type()
)
gslbCurCfgRemSiteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteState.setStatus("mandatory")


class _GslbCurCfgRemSiteUpdate_Type(Integer32):
    """Custom type gslbCurCfgRemSiteUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgRemSiteUpdate_Type.__name__ = "Integer32"
_GslbCurCfgRemSiteUpdate_Object = MibTableColumn
gslbCurCfgRemSiteUpdate = _GslbCurCfgRemSiteUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 5),
    _GslbCurCfgRemSiteUpdate_Type()
)
gslbCurCfgRemSiteUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteUpdate.setStatus("mandatory")


class _GslbCurCfgRemSiteName_Type(DisplayString):
    """Custom type gslbCurCfgRemSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GslbCurCfgRemSiteName_Type.__name__ = "DisplayString"
_GslbCurCfgRemSiteName_Object = MibTableColumn
gslbCurCfgRemSiteName = _GslbCurCfgRemSiteName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 2, 1, 6),
    _GslbCurCfgRemSiteName_Type()
)
gslbCurCfgRemSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgRemSiteName.setStatus("mandatory")
_GslbNewCfgRemSiteTable_Object = MibTable
gslbNewCfgRemSiteTable = _GslbNewCfgRemSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3)
)
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteTable.setStatus("mandatory")
_GslbNewCfgRemSiteTableEntry_Object = MibTableRow
gslbNewCfgRemSiteTableEntry = _GslbNewCfgRemSiteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1)
)
gslbNewCfgRemSiteTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "gslbNewCfgRemSiteIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteTableEntry.setStatus("mandatory")
_GslbNewCfgRemSiteIndx_Type = Integer32
_GslbNewCfgRemSiteIndx_Object = MibTableColumn
gslbNewCfgRemSiteIndx = _GslbNewCfgRemSiteIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 1),
    _GslbNewCfgRemSiteIndx_Type()
)
gslbNewCfgRemSiteIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteIndx.setStatus("mandatory")
_GslbNewCfgRemSitePrimaryIp_Type = IpAddress
_GslbNewCfgRemSitePrimaryIp_Object = MibTableColumn
gslbNewCfgRemSitePrimaryIp = _GslbNewCfgRemSitePrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 2),
    _GslbNewCfgRemSitePrimaryIp_Type()
)
gslbNewCfgRemSitePrimaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSitePrimaryIp.setStatus("mandatory")
_GslbNewCfgRemSiteSecondaryIp_Type = IpAddress
_GslbNewCfgRemSiteSecondaryIp_Object = MibTableColumn
gslbNewCfgRemSiteSecondaryIp = _GslbNewCfgRemSiteSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 3),
    _GslbNewCfgRemSiteSecondaryIp_Type()
)
gslbNewCfgRemSiteSecondaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteSecondaryIp.setStatus("mandatory")


class _GslbNewCfgRemSiteState_Type(Integer32):
    """Custom type gslbNewCfgRemSiteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgRemSiteState_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteState_Object = MibTableColumn
gslbNewCfgRemSiteState = _GslbNewCfgRemSiteState_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 4),
    _GslbNewCfgRemSiteState_Type()
)
gslbNewCfgRemSiteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteState.setStatus("mandatory")


class _GslbNewCfgRemSiteUpdate_Type(Integer32):
    """Custom type gslbNewCfgRemSiteUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgRemSiteUpdate_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteUpdate_Object = MibTableColumn
gslbNewCfgRemSiteUpdate = _GslbNewCfgRemSiteUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 5),
    _GslbNewCfgRemSiteUpdate_Type()
)
gslbNewCfgRemSiteUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteUpdate.setStatus("mandatory")


class _GslbNewCfgRemSiteDelete_Type(Integer32):
    """Custom type gslbNewCfgRemSiteDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_GslbNewCfgRemSiteDelete_Type.__name__ = "Integer32"
_GslbNewCfgRemSiteDelete_Object = MibTableColumn
gslbNewCfgRemSiteDelete = _GslbNewCfgRemSiteDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 6),
    _GslbNewCfgRemSiteDelete_Type()
)
gslbNewCfgRemSiteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteDelete.setStatus("mandatory")


class _GslbNewCfgRemSiteName_Type(DisplayString):
    """Custom type gslbNewCfgRemSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_GslbNewCfgRemSiteName_Type.__name__ = "DisplayString"
_GslbNewCfgRemSiteName_Object = MibTableColumn
gslbNewCfgRemSiteName = _GslbNewCfgRemSiteName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 3, 3, 1, 7),
    _GslbNewCfgRemSiteName_Type()
)
gslbNewCfgRemSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgRemSiteName.setStatus("mandatory")
_GslbLookup_ObjectIdentity = ObjectIdentity
gslbLookup = _GslbLookup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4)
)


class _GslbCurCfgGenLookups_Type(Integer32):
    """Custom type gslbCurCfgGenLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenLookups_Type.__name__ = "Integer32"
_GslbCurCfgGenLookups_Object = MibScalar
gslbCurCfgGenLookups = _GslbCurCfgGenLookups_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 1),
    _GslbCurCfgGenLookups_Type()
)
gslbCurCfgGenLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookups.setStatus("mandatory")


class _GslbNewCfgGenLookups_Type(Integer32):
    """Custom type gslbNewCfgGenLookups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenLookups_Type.__name__ = "Integer32"
_GslbNewCfgGenLookups_Object = MibScalar
gslbNewCfgGenLookups = _GslbNewCfgGenLookups_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 2),
    _GslbNewCfgGenLookups_Type()
)
gslbNewCfgGenLookups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookups.setStatus("mandatory")


class _GslbCurCfgGenLookupDname_Type(DisplayString):
    """Custom type gslbCurCfgGenLookupDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_GslbCurCfgGenLookupDname_Type.__name__ = "DisplayString"
_GslbCurCfgGenLookupDname_Object = MibScalar
gslbCurCfgGenLookupDname = _GslbCurCfgGenLookupDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 3),
    _GslbCurCfgGenLookupDname_Type()
)
gslbCurCfgGenLookupDname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookupDname.setStatus("mandatory")


class _GslbNewCfgGenLookupDname_Type(DisplayString):
    """Custom type gslbNewCfgGenLookupDname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 34),
    )


_GslbNewCfgGenLookupDname_Type.__name__ = "DisplayString"
_GslbNewCfgGenLookupDname_Object = MibScalar
gslbNewCfgGenLookupDname = _GslbNewCfgGenLookupDname_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 4),
    _GslbNewCfgGenLookupDname_Type()
)
gslbNewCfgGenLookupDname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookupDname.setStatus("mandatory")
_GslbNetwork_ObjectIdentity = ObjectIdentity
gslbNetwork = _GslbNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5)
)
_GslbNetworkTableMaxSize_Type = Integer32
_GslbNetworkTableMaxSize_Object = MibScalar
gslbNetworkTableMaxSize = _GslbNetworkTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 1),
    _GslbNetworkTableMaxSize_Type()
)
gslbNetworkTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNetworkTableMaxSize.setStatus("mandatory")
_GslbCurCfgNetworkTable_Object = MibTable
gslbCurCfgNetworkTable = _GslbCurCfgNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2)
)
if mibBuilder.loadTexts:
    gslbCurCfgNetworkTable.setStatus("mandatory")
_GslbCurCfgNetworkTableEntry_Object = MibTableRow
gslbCurCfgNetworkTableEntry = _GslbCurCfgNetworkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1)
)
gslbCurCfgNetworkTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "gslbCurCfgNetworkIndx"),
)
if mibBuilder.loadTexts:
    gslbCurCfgNetworkTableEntry.setStatus("mandatory")
_GslbCurCfgNetworkIndx_Type = Integer32
_GslbCurCfgNetworkIndx_Object = MibTableColumn
gslbCurCfgNetworkIndx = _GslbCurCfgNetworkIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 1),
    _GslbCurCfgNetworkIndx_Type()
)
gslbCurCfgNetworkIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkIndx.setStatus("mandatory")
_GslbCurCfgNetworkSourceIp_Type = IpAddress
_GslbCurCfgNetworkSourceIp_Object = MibTableColumn
gslbCurCfgNetworkSourceIp = _GslbCurCfgNetworkSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 2),
    _GslbCurCfgNetworkSourceIp_Type()
)
gslbCurCfgNetworkSourceIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkSourceIp.setStatus("mandatory")
_GslbCurCfgNetworkNetMask_Type = IpAddress
_GslbCurCfgNetworkNetMask_Object = MibTableColumn
gslbCurCfgNetworkNetMask = _GslbCurCfgNetworkNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 3),
    _GslbCurCfgNetworkNetMask_Type()
)
gslbCurCfgNetworkNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkNetMask.setStatus("mandatory")
_GslbCurCfgNetworkVip1_Type = IpAddress
_GslbCurCfgNetworkVip1_Object = MibTableColumn
gslbCurCfgNetworkVip1 = _GslbCurCfgNetworkVip1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 4),
    _GslbCurCfgNetworkVip1_Type()
)
gslbCurCfgNetworkVip1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkVip1.setStatus("mandatory")
_GslbCurCfgNetworkVip2_Type = IpAddress
_GslbCurCfgNetworkVip2_Object = MibTableColumn
gslbCurCfgNetworkVip2 = _GslbCurCfgNetworkVip2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 2, 1, 5),
    _GslbCurCfgNetworkVip2_Type()
)
gslbCurCfgNetworkVip2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgNetworkVip2.setStatus("mandatory")
_GslbNewCfgNetworkTable_Object = MibTable
gslbNewCfgNetworkTable = _GslbNewCfgNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3)
)
if mibBuilder.loadTexts:
    gslbNewCfgNetworkTable.setStatus("mandatory")
_GslbNewCfgNetworkTableEntry_Object = MibTableRow
gslbNewCfgNetworkTableEntry = _GslbNewCfgNetworkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1)
)
gslbNewCfgNetworkTableEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "gslbNewCfgNetworkIndx"),
)
if mibBuilder.loadTexts:
    gslbNewCfgNetworkTableEntry.setStatus("mandatory")
_GslbNewCfgNetworkIndx_Type = Integer32
_GslbNewCfgNetworkIndx_Object = MibTableColumn
gslbNewCfgNetworkIndx = _GslbNewCfgNetworkIndx_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 1),
    _GslbNewCfgNetworkIndx_Type()
)
gslbNewCfgNetworkIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkIndx.setStatus("mandatory")
_GslbNewCfgNetworkSourceIp_Type = IpAddress
_GslbNewCfgNetworkSourceIp_Object = MibTableColumn
gslbNewCfgNetworkSourceIp = _GslbNewCfgNetworkSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 2),
    _GslbNewCfgNetworkSourceIp_Type()
)
gslbNewCfgNetworkSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkSourceIp.setStatus("mandatory")
_GslbNewCfgNetworkNetMask_Type = IpAddress
_GslbNewCfgNetworkNetMask_Object = MibTableColumn
gslbNewCfgNetworkNetMask = _GslbNewCfgNetworkNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 3),
    _GslbNewCfgNetworkNetMask_Type()
)
gslbNewCfgNetworkNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkNetMask.setStatus("mandatory")
_GslbNewCfgNetworkVip1_Type = IpAddress
_GslbNewCfgNetworkVip1_Object = MibTableColumn
gslbNewCfgNetworkVip1 = _GslbNewCfgNetworkVip1_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 4),
    _GslbNewCfgNetworkVip1_Type()
)
gslbNewCfgNetworkVip1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkVip1.setStatus("mandatory")
_GslbNewCfgNetworkVip2_Type = IpAddress
_GslbNewCfgNetworkVip2_Object = MibTableColumn
gslbNewCfgNetworkVip2 = _GslbNewCfgNetworkVip2_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 5),
    _GslbNewCfgNetworkVip2_Type()
)
gslbNewCfgNetworkVip2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkVip2.setStatus("mandatory")


class _GslbNewCfgNetworkDelete_Type(Integer32):
    """Custom type gslbNewCfgNetworkDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("other", 1))
    )


_GslbNewCfgNetworkDelete_Type.__name__ = "Integer32"
_GslbNewCfgNetworkDelete_Object = MibTableColumn
gslbNewCfgNetworkDelete = _GslbNewCfgNetworkDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 5, 3, 1, 12),
    _GslbNewCfgNetworkDelete_Type()
)
gslbNewCfgNetworkDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgNetworkDelete.setStatus("mandatory")


class _GslbCurCfgGenExternal_Type(Integer32):
    """Custom type gslbCurCfgGenExternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbCurCfgGenExternal_Type.__name__ = "Integer32"
_GslbCurCfgGenExternal_Object = MibScalar
gslbCurCfgGenExternal = _GslbCurCfgGenExternal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 6),
    _GslbCurCfgGenExternal_Type()
)
gslbCurCfgGenExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenExternal.setStatus("obsolete")


class _GslbNewCfgGenExternal_Type(Integer32):
    """Custom type gslbNewCfgGenExternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_GslbNewCfgGenExternal_Type.__name__ = "Integer32"
_GslbNewCfgGenExternal_Object = MibScalar
gslbNewCfgGenExternal = _GslbNewCfgGenExternal_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 7),
    _GslbNewCfgGenExternal_Type()
)
gslbNewCfgGenExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenExternal.setStatus("obsolete")
_GslbCurCfgGenEip_Type = IpAddress
_GslbCurCfgGenEip_Object = MibScalar
gslbCurCfgGenEip = _GslbCurCfgGenEip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 8),
    _GslbCurCfgGenEip_Type()
)
gslbCurCfgGenEip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenEip.setStatus("obsolete")
_GslbNewCfgGenEip_Type = IpAddress
_GslbNewCfgGenEip_Object = MibScalar
gslbNewCfgGenEip = _GslbNewCfgGenEip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 9),
    _GslbNewCfgGenEip_Type()
)
gslbNewCfgGenEip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenEip.setStatus("obsolete")


class _GslbCurCfgGenLookupPort_Type(Integer32):
    """Custom type gslbCurCfgGenLookupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8100, 9999),
    )


_GslbCurCfgGenLookupPort_Type.__name__ = "Integer32"
_GslbCurCfgGenLookupPort_Object = MibScalar
gslbCurCfgGenLookupPort = _GslbCurCfgGenLookupPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 10),
    _GslbCurCfgGenLookupPort_Type()
)
gslbCurCfgGenLookupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookupPort.setStatus("obsolete")


class _GslbNewCfgGenLookupPort_Type(Integer32):
    """Custom type gslbNewCfgGenLookupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8100, 9999),
    )


_GslbNewCfgGenLookupPort_Type.__name__ = "Integer32"
_GslbNewCfgGenLookupPort_Object = MibScalar
gslbNewCfgGenLookupPort = _GslbNewCfgGenLookupPort_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 11),
    _GslbNewCfgGenLookupPort_Type()
)
gslbNewCfgGenLookupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookupPort.setStatus("obsolete")


class _GslbCurCfgGenLookupTimeout_Type(Integer32):
    """Custom type gslbCurCfgGenLookupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GslbCurCfgGenLookupTimeout_Type.__name__ = "Integer32"
_GslbCurCfgGenLookupTimeout_Object = MibScalar
gslbCurCfgGenLookupTimeout = _GslbCurCfgGenLookupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 12),
    _GslbCurCfgGenLookupTimeout_Type()
)
gslbCurCfgGenLookupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gslbCurCfgGenLookupTimeout.setStatus("obsolete")


class _GslbNewCfgGenLookupTimeout_Type(Integer32):
    """Custom type gslbNewCfgGenLookupTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GslbNewCfgGenLookupTimeout_Type.__name__ = "Integer32"
_GslbNewCfgGenLookupTimeout_Object = MibScalar
gslbNewCfgGenLookupTimeout = _GslbNewCfgGenLookupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 11, 4, 13),
    _GslbNewCfgGenLookupTimeout_Type()
)
gslbNewCfgGenLookupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gslbNewCfgGenLookupTimeout.setStatus("obsolete")
_DynamicSLB_ObjectIdentity = ObjectIdentity
dynamicSLB = _DynamicSLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12)
)
_DynSLBRealServerTable_Object = MibTable
dynSLBRealServerTable = _DynSLBRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    dynSLBRealServerTable.setStatus("obsolete")
_DynSLBRealServerEntry_Object = MibTableRow
dynSLBRealServerEntry = _DynSLBRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1)
)
dynSLBRealServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "dynSLBRealServerIpAddr"),
    (0, "ALTEON-TS-LAYER4-MIB", "dynSLBRealServerPortNum"),
)
if mibBuilder.loadTexts:
    dynSLBRealServerEntry.setStatus("obsolete")
_DynSLBRealServerIpAddr_Type = IpAddress
_DynSLBRealServerIpAddr_Object = MibTableColumn
dynSLBRealServerIpAddr = _DynSLBRealServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1, 1),
    _DynSLBRealServerIpAddr_Type()
)
dynSLBRealServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynSLBRealServerIpAddr.setStatus("obsolete")
_DynSLBRealServerPortNum_Type = Integer32
_DynSLBRealServerPortNum_Object = MibTableColumn
dynSLBRealServerPortNum = _DynSLBRealServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1, 2),
    _DynSLBRealServerPortNum_Type()
)
dynSLBRealServerPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dynSLBRealServerPortNum.setStatus("obsolete")
_DynSLBRealServerWeight_Type = Integer32
_DynSLBRealServerWeight_Object = MibTableColumn
dynSLBRealServerWeight = _DynSLBRealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 12, 1, 1, 3),
    _DynSLBRealServerWeight_Type()
)
dynSLBRealServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynSLBRealServerWeight.setStatus("obsolete")
_OperSlbPortTable_Object = MibTable
operSlbPortTable = _OperSlbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    operSlbPortTable.setStatus("mandatory")
_OperSlbPortEntry_Object = MibTableRow
operSlbPortEntry = _OperSlbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1, 1)
)
operSlbPortEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "operSlbPortIndex"),
)
if mibBuilder.loadTexts:
    operSlbPortEntry.setStatus("mandatory")
_OperSlbPortIndex_Type = Integer32
_OperSlbPortIndex_Object = MibTableColumn
operSlbPortIndex = _OperSlbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1, 1, 1),
    _OperSlbPortIndex_Type()
)
operSlbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operSlbPortIndex.setStatus("mandatory")


class _OperSlbPortClrSessionTab_Type(Integer32):
    """Custom type operSlbPortClrSessionTab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_OperSlbPortClrSessionTab_Type.__name__ = "Integer32"
_OperSlbPortClrSessionTab_Object = MibTableColumn
operSlbPortClrSessionTab = _OperSlbPortClrSessionTab_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 1, 1, 2),
    _OperSlbPortClrSessionTab_Type()
)
operSlbPortClrSessionTab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    operSlbPortClrSessionTab.setStatus("mandatory")
_SlbOper_ObjectIdentity = ObjectIdentity
slbOper = _SlbOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 4)
)
_SlbOperRealServerTable_Object = MibTable
slbOperRealServerTable = _SlbOperRealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 4, 1)
)
if mibBuilder.loadTexts:
    slbOperRealServerTable.setStatus("mandatory")
_SlbOperRealServerEntry_Object = MibTableRow
slbOperRealServerEntry = _SlbOperRealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 4, 1, 1)
)
slbOperRealServerEntry.setIndexNames(
    (0, "ALTEON-TS-LAYER4-MIB", "slbOperRealServerIndex"),
)
if mibBuilder.loadTexts:
    slbOperRealServerEntry.setStatus("mandatory")
_SlbOperRealServerIndex_Type = Integer32
_SlbOperRealServerIndex_Object = MibTableColumn
slbOperRealServerIndex = _SlbOperRealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 4, 1, 1, 1),
    _SlbOperRealServerIndex_Type()
)
slbOperRealServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbOperRealServerIndex.setStatus("mandatory")


class _SlbOperRealServerStatus_Type(Integer32):
    """Custom type slbOperRealServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cookiepersistent", 3),
          ("disable", 2),
          ("enable", 1))
    )


_SlbOperRealServerStatus_Type.__name__ = "Integer32"
_SlbOperRealServerStatus_Object = MibTableColumn
slbOperRealServerStatus = _SlbOperRealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 4, 1, 1, 2),
    _SlbOperRealServerStatus_Type()
)
slbOperRealServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbOperRealServerStatus.setStatus("mandatory")


class _SlbOperConfigSync_Type(Integer32):
    """Custom type slbOperConfigSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("sync", 2))
    )


_SlbOperConfigSync_Type.__name__ = "Integer32"
_SlbOperConfigSync_Object = MibScalar
slbOperConfigSync = _SlbOperConfigSync_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 1, 14, 4, 2),
    _SlbOperConfigSync_Type()
)
slbOperConfigSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbOperConfigSync.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-TS-LAYER4-MIB",
    **{"serverloadbalance": serverloadbalance,
       "slbRealServerMaxSize": slbRealServerMaxSize,
       "slbCurCfgRealServerTable": slbCurCfgRealServerTable,
       "slbCurCfgRealServerEntry": slbCurCfgRealServerEntry,
       "slbCurCfgRealServerIndex": slbCurCfgRealServerIndex,
       "slbCurCfgRealServerIpAddr": slbCurCfgRealServerIpAddr,
       "slbCurCfgRealServerWeight": slbCurCfgRealServerWeight,
       "slbCurCfgRealServerMaxConns": slbCurCfgRealServerMaxConns,
       "slbCurCfgRealServerTimeOut": slbCurCfgRealServerTimeOut,
       "slbCurCfgRealServerBackUp": slbCurCfgRealServerBackUp,
       "slbCurCfgRealServerPingInterval": slbCurCfgRealServerPingInterval,
       "slbCurCfgRealServerFailRetry": slbCurCfgRealServerFailRetry,
       "slbCurCfgRealServerSuccRetry": slbCurCfgRealServerSuccRetry,
       "slbCurCfgRealServerState": slbCurCfgRealServerState,
       "slbCurCfgRealServerType": slbCurCfgRealServerType,
       "slbCurCfgRealServerName": slbCurCfgRealServerName,
       "slbCurCfgRealServerUrlBmap": slbCurCfgRealServerUrlBmap,
       "slbCurCfgRealServerCookie": slbCurCfgRealServerCookie,
       "slbCurCfgRealServerExcludeStr": slbCurCfgRealServerExcludeStr,
       "slbCurCfgRealServerSubmac": slbCurCfgRealServerSubmac,
       "slbCurCfgRealServerProxy": slbCurCfgRealServerProxy,
       "slbNewCfgRealServerTable": slbNewCfgRealServerTable,
       "slbNewCfgRealServerEntry": slbNewCfgRealServerEntry,
       "slbNewCfgRealServerIndex": slbNewCfgRealServerIndex,
       "slbNewCfgRealServerIpAddr": slbNewCfgRealServerIpAddr,
       "slbNewCfgRealServerWeight": slbNewCfgRealServerWeight,
       "slbNewCfgRealServerMaxConns": slbNewCfgRealServerMaxConns,
       "slbNewCfgRealServerTimeOut": slbNewCfgRealServerTimeOut,
       "slbNewCfgRealServerBackUp": slbNewCfgRealServerBackUp,
       "slbNewCfgRealServerPingInterval": slbNewCfgRealServerPingInterval,
       "slbNewCfgRealServerFailRetry": slbNewCfgRealServerFailRetry,
       "slbNewCfgRealServerSuccRetry": slbNewCfgRealServerSuccRetry,
       "slbNewCfgRealServerState": slbNewCfgRealServerState,
       "slbNewCfgRealServerDelete": slbNewCfgRealServerDelete,
       "slbNewCfgRealServerType": slbNewCfgRealServerType,
       "slbNewCfgRealServerName": slbNewCfgRealServerName,
       "slbNewCfgRealServerUrlBmap": slbNewCfgRealServerUrlBmap,
       "slbNewCfgRealServerAddUrl": slbNewCfgRealServerAddUrl,
       "slbNewCfgRealServerRemUrl": slbNewCfgRealServerRemUrl,
       "slbNewCfgRealServerCookie": slbNewCfgRealServerCookie,
       "slbNewCfgRealServerExcludeStr": slbNewCfgRealServerExcludeStr,
       "slbNewCfgRealServerSubmac": slbNewCfgRealServerSubmac,
       "slbNewCfgRealServerProxy": slbNewCfgRealServerProxy,
       "slbVirtServerTableMaxSize": slbVirtServerTableMaxSize,
       "slbCurCfgVirtServerTable": slbCurCfgVirtServerTable,
       "slbCurCfgVirtualServerEntry": slbCurCfgVirtualServerEntry,
       "slbCurCfgVirtServerIndex": slbCurCfgVirtServerIndex,
       "slbCurCfgVirtServerIpAddress": slbCurCfgVirtServerIpAddress,
       "slbCurCfgVirtServerLayer3Only": slbCurCfgVirtServerLayer3Only,
       "slbCurCfgVirtServerState": slbCurCfgVirtServerState,
       "slbCurCfgVirtServerDname": slbCurCfgVirtServerDname,
       "slbCurCfgVirtServerCname": slbCurCfgVirtServerCname,
       "slbCurCfgVirtServerCoffset": slbCurCfgVirtServerCoffset,
       "slbCurCfgVirtServerClength": slbCurCfgVirtServerClength,
       "slbCurCfgVirtServerUriCookie": slbCurCfgVirtServerUriCookie,
       "slbCurCfgVirtServerFtpParsing": slbCurCfgVirtServerFtpParsing,
       "slbCurCfgVirtServerUrlHashLen": slbCurCfgVirtServerUrlHashLen,
       "slbCurCfgVirtServerHttpHdrName": slbCurCfgVirtServerHttpHdrName,
       "slbCurCfgVirtServerBwmContract": slbCurCfgVirtServerBwmContract,
       "slbCurCfgVirtServerResponseCount": slbCurCfgVirtServerResponseCount,
       "slbCurCfgVirtServerCExpire": slbCurCfgVirtServerCExpire,
       "slbNewCfgVirtServerTable": slbNewCfgVirtServerTable,
       "slbNewCfgVirtualServerEntry": slbNewCfgVirtualServerEntry,
       "slbNewCfgVirtServerIndex": slbNewCfgVirtServerIndex,
       "slbNewCfgVirtServerIpAddress": slbNewCfgVirtServerIpAddress,
       "slbNewCfgVirtServerLayer3Only": slbNewCfgVirtServerLayer3Only,
       "slbNewCfgVirtServerState": slbNewCfgVirtServerState,
       "slbNewCfgVirtServerDelete": slbNewCfgVirtServerDelete,
       "slbNewCfgVirtServerDname": slbNewCfgVirtServerDname,
       "slbNewCfgVirtServerCname": slbNewCfgVirtServerCname,
       "slbNewCfgVirtServerCoffset": slbNewCfgVirtServerCoffset,
       "slbNewCfgVirtServerClength": slbNewCfgVirtServerClength,
       "slbNewCfgVirtServerUriCookie": slbNewCfgVirtServerUriCookie,
       "slbNewCfgVirtServerFtpParsing": slbNewCfgVirtServerFtpParsing,
       "slbNewCfgVirtServerUrlHashLen": slbNewCfgVirtServerUrlHashLen,
       "slbNewCfgVirtServerHttpHdrName": slbNewCfgVirtServerHttpHdrName,
       "slbNewCfgVirtServerBwmContract": slbNewCfgVirtServerBwmContract,
       "slbNewCfgVirtServerResponseCount": slbNewCfgVirtServerResponseCount,
       "slbNewCfgVirtServerCExpire": slbNewCfgVirtServerCExpire,
       "slbCurCfgVirtServicesTable": slbCurCfgVirtServicesTable,
       "slbCurCfgVirtServicesEntry": slbCurCfgVirtServicesEntry,
       "slbCurCfgVirtServIndex": slbCurCfgVirtServIndex,
       "slbCurCfgVirtServiceIndex": slbCurCfgVirtServiceIndex,
       "slbCurCfgVirtServiceVirtPort": slbCurCfgVirtServiceVirtPort,
       "slbCurCfgVirtServiceRealGroup": slbCurCfgVirtServiceRealGroup,
       "slbCurCfgVirtServiceRealPort": slbCurCfgVirtServiceRealPort,
       "slbCurCfgVirtServiceUDPBalance": slbCurCfgVirtServiceUDPBalance,
       "slbCurCfgVirtServicePBind": slbCurCfgVirtServicePBind,
       "slbCurCfgVirtServiceHname": slbCurCfgVirtServiceHname,
       "slbCurCfgVirtServiceHttpSlb": slbCurCfgVirtServiceHttpSlb,
       "slbCurCfgVirtServiceBwmContract": slbCurCfgVirtServiceBwmContract,
       "slbCurCfgVirtServiceDirServerRtn": slbCurCfgVirtServiceDirServerRtn,
       "slbCurCfgVirtServiceRtspUrlParse": slbCurCfgVirtServiceRtspUrlParse,
       "slbCurCfgVirtServiceCookieMode": slbCurCfgVirtServiceCookieMode,
       "slbCurCfgVirtServiceDBind": slbCurCfgVirtServiceDBind,
       "slbCurCfgVirtServiceFtpParsing": slbCurCfgVirtServiceFtpParsing,
       "slbCurCfgVirtServiceHttpSlbOption": slbCurCfgVirtServiceHttpSlbOption,
       "slbCurCfgVirtServiceHttpSlb2": slbCurCfgVirtServiceHttpSlb2,
       "slbCurCfgVirtServiceRemapUDPFrags": slbCurCfgVirtServiceRemapUDPFrags,
       "slbCurCfgVirtServiceDnsSlb": slbCurCfgVirtServiceDnsSlb,
       "slbNewCfgVirtServicesTable": slbNewCfgVirtServicesTable,
       "slbNewCfgVirtServicesEntry": slbNewCfgVirtServicesEntry,
       "slbNewCfgVirtServIndex": slbNewCfgVirtServIndex,
       "slbNewCfgVirtServiceIndex": slbNewCfgVirtServiceIndex,
       "slbNewCfgVirtServiceVirtPort": slbNewCfgVirtServiceVirtPort,
       "slbNewCfgVirtServiceRealGroup": slbNewCfgVirtServiceRealGroup,
       "slbNewCfgVirtServiceRealPort": slbNewCfgVirtServiceRealPort,
       "slbNewCfgVirtServiceUDPBalance": slbNewCfgVirtServiceUDPBalance,
       "slbNewCfgVirtServicePBind": slbNewCfgVirtServicePBind,
       "slbNewCfgVirtServiceHname": slbNewCfgVirtServiceHname,
       "slbNewCfgVirtServiceHttpSlb": slbNewCfgVirtServiceHttpSlb,
       "slbNewCfgVirtServiceBwmContract": slbNewCfgVirtServiceBwmContract,
       "slbNewCfgVirtServiceDirServerRtn": slbNewCfgVirtServiceDirServerRtn,
       "slbNewCfgVirtServiceDelete": slbNewCfgVirtServiceDelete,
       "slbNewCfgVirtServiceRtspUrlParse": slbNewCfgVirtServiceRtspUrlParse,
       "slbNewCfgVirtServiceCookieMode": slbNewCfgVirtServiceCookieMode,
       "slbNewCfgVirtServiceDBind": slbNewCfgVirtServiceDBind,
       "slbNewCfgVirtServiceFtpParsing": slbNewCfgVirtServiceFtpParsing,
       "slbNewCfgVirtServiceHttpSlbOption": slbNewCfgVirtServiceHttpSlbOption,
       "slbNewCfgVirtServiceHttpSlb2": slbNewCfgVirtServiceHttpSlb2,
       "slbNewCfgVirtServiceRemapUDPFrags": slbNewCfgVirtServiceRemapUDPFrags,
       "slbNewCfgVirtServiceDnsSlb": slbNewCfgVirtServiceDnsSlb,
       "slbGroupTableMaxSize": slbGroupTableMaxSize,
       "slbCurCfgGroupTable": slbCurCfgGroupTable,
       "slbCurCfgGroupEntry": slbCurCfgGroupEntry,
       "slbCurCfgGroupIndex": slbCurCfgGroupIndex,
       "slbCurCfgGroupRealServers": slbCurCfgGroupRealServers,
       "slbCurCfgGroupMetric": slbCurCfgGroupMetric,
       "slbCurCfgGroupBackupServer": slbCurCfgGroupBackupServer,
       "slbCurCfgGroupHealthCheckUrl": slbCurCfgGroupHealthCheckUrl,
       "slbCurCfgGroupHealthCheckLayer": slbCurCfgGroupHealthCheckLayer,
       "slbCurCfgGroupName": slbCurCfgGroupName,
       "slbCurCfgGroupRealThreshold": slbCurCfgGroupRealThreshold,
       "slbCurCfgGroupBackupGroup": slbCurCfgGroupBackupGroup,
       "slbCurCfgGroupVipHealthCheck": slbCurCfgGroupVipHealthCheck,
       "slbNewCfgGroupTable": slbNewCfgGroupTable,
       "slbNewCfgGroupEntry": slbNewCfgGroupEntry,
       "slbNewCfgGroupIndex": slbNewCfgGroupIndex,
       "slbNewCfgGroupRealServers": slbNewCfgGroupRealServers,
       "slbNewCfgGroupAddServer": slbNewCfgGroupAddServer,
       "slbNewCfgGroupRemoveServer": slbNewCfgGroupRemoveServer,
       "slbNewCfgGroupMetric": slbNewCfgGroupMetric,
       "slbNewCfgGroupBackupServer": slbNewCfgGroupBackupServer,
       "slbNewCfgGroupDelete": slbNewCfgGroupDelete,
       "slbNewCfgGroupHealthCheckUrl": slbNewCfgGroupHealthCheckUrl,
       "slbNewCfgGroupHealthCheckLayer": slbNewCfgGroupHealthCheckLayer,
       "slbNewCfgGroupName": slbNewCfgGroupName,
       "slbNewCfgGroupRealThreshold": slbNewCfgGroupRealThreshold,
       "slbNewCfgGroupBackupGroup": slbNewCfgGroupBackupGroup,
       "slbNewCfgGroupVipHealthCheck": slbNewCfgGroupVipHealthCheck,
       "slbCurCfgPortTable": slbCurCfgPortTable,
       "slbCurCfgPortEntry": slbCurCfgPortEntry,
       "slbCurCfgPortIndex": slbCurCfgPortIndex,
       "slbCurCfgPortProxyIpAddr": slbCurCfgPortProxyIpAddr,
       "slbCurCfgPortSlbState": slbCurCfgPortSlbState,
       "slbCurCfgPortSlbHotStandby": slbCurCfgPortSlbHotStandby,
       "slbCurCfgPortSlbInterSwitch": slbCurCfgPortSlbInterSwitch,
       "slbCurCfgPortSlbPipState": slbCurCfgPortSlbPipState,
       "slbCurCfgPortSlbRtsState": slbCurCfgPortSlbRtsState,
       "slbCurCfgPortSlbIdslbState": slbCurCfgPortSlbIdslbState,
       "slbCurCfgPortSlbNasaState": slbCurCfgPortSlbNasaState,
       "slbNewCfgPortTable": slbNewCfgPortTable,
       "slbNewCfgPortEntry": slbNewCfgPortEntry,
       "slbNewCfgPortIndex": slbNewCfgPortIndex,
       "slbNewCfgPortProxyIpAddr": slbNewCfgPortProxyIpAddr,
       "slbNewCfgPortSlbState": slbNewCfgPortSlbState,
       "slbNewCfgPortSlbHotStandby": slbNewCfgPortSlbHotStandby,
       "slbNewCfgPortSlbInterSwitch": slbNewCfgPortSlbInterSwitch,
       "slbNewCfgPortSlbPipState": slbNewCfgPortSlbPipState,
       "slbNewCfgPortSlbRtsState": slbNewCfgPortSlbRtsState,
       "slbNewCfgPortDelete": slbNewCfgPortDelete,
       "slbNewCfgPortSlbIdslbState": slbNewCfgPortSlbIdslbState,
       "slbNewCfgPortSlbNasaState": slbNewCfgPortSlbNasaState,
       "slbCurCfgImask": slbCurCfgImask,
       "slbNewCfgImask": slbNewCfgImask,
       "slbfailover": slbfailover,
       "slbCurCfgFailOverTable": slbCurCfgFailOverTable,
       "slbCurCfgFailOverTblEntry": slbCurCfgFailOverTblEntry,
       "slbCurCfgFailOverIndex": slbCurCfgFailOverIndex,
       "slbCurCfgFailOverPrimaryIp": slbCurCfgFailOverPrimaryIp,
       "slbCurCfgFailOverSecondaryIp": slbCurCfgFailOverSecondaryIp,
       "slbCurCfgFailOverSilenceInterval": slbCurCfgFailOverSilenceInterval,
       "slbCurCfgFailOverState": slbCurCfgFailOverState,
       "slbCurCfgFailOverRouteSupply": slbCurCfgFailOverRouteSupply,
       "slbNewCfgFailOverTable": slbNewCfgFailOverTable,
       "slbNewCfgFailOverTblEntry": slbNewCfgFailOverTblEntry,
       "slbNewCfgFailOverIndex": slbNewCfgFailOverIndex,
       "slbNewCfgFailOverPrimaryIp": slbNewCfgFailOverPrimaryIp,
       "slbNewCfgFailOverSecondaryIp": slbNewCfgFailOverSecondaryIp,
       "slbNewCfgFailOverSilenceInterval": slbNewCfgFailOverSilenceInterval,
       "slbNewCfgFailOverState": slbNewCfgFailOverState,
       "slbNewCfgFailOverRouteSupply": slbNewCfgFailOverRouteSupply,
       "slbCurCfgGlobalControl": slbCurCfgGlobalControl,
       "slbNewCfgGlobalControl": slbNewCfgGlobalControl,
       "slbCurCfgMnet": slbCurCfgMnet,
       "slbNewCfgMnet": slbNewCfgMnet,
       "slbCurCfgMmask": slbCurCfgMmask,
       "slbNewCfgMmask": slbNewCfgMmask,
       "slbCurCfgRadiusAuthenString": slbCurCfgRadiusAuthenString,
       "slbNewCfgRadiusAuthenString": slbNewCfgRadiusAuthenString,
       "slbCurCfgDirectMode": slbCurCfgDirectMode,
       "slbNewCfgDirectMode": slbNewCfgDirectMode,
       "slbUrl": slbUrl,
       "slbUrlRedir": slbUrlRedir,
       "slbCurCfgUrlExpTable": slbCurCfgUrlExpTable,
       "slbCurCfgUrlExpTableEntry": slbCurCfgUrlExpTableEntry,
       "slbCurCfgUrlExpIndex": slbCurCfgUrlExpIndex,
       "slbCurCfgUrlExpression": slbCurCfgUrlExpression,
       "slbNewCfgUrlExpTable": slbNewCfgUrlExpTable,
       "slbNewCfgUrlExpTableEntry": slbNewCfgUrlExpTableEntry,
       "slbNewCfgUrlExpIndex": slbNewCfgUrlExpIndex,
       "slbNewCfgUrlExpression": slbNewCfgUrlExpression,
       "slbNewCfgUrlExpDelete": slbNewCfgUrlExpDelete,
       "slbCurCfgUrlRedirNonGetOrigSrv": slbCurCfgUrlRedirNonGetOrigSrv,
       "slbNewCfgUrlRedirNonGetOrigSrv": slbNewCfgUrlRedirNonGetOrigSrv,
       "slbCurCfgUrlRedirCookieOrigSrv": slbCurCfgUrlRedirCookieOrigSrv,
       "slbNewCfgUrlRedirCookieOrigSrv": slbNewCfgUrlRedirCookieOrigSrv,
       "slbCurCfgUrlRedirNoCacheOrigSrv": slbCurCfgUrlRedirNoCacheOrigSrv,
       "slbNewCfgUrlRedirNoCacheOrigSrv": slbNewCfgUrlRedirNoCacheOrigSrv,
       "slbCurCfgUrlRedirUriHashLength": slbCurCfgUrlRedirUriHashLength,
       "slbNewCfgUrlRedirUriHashLength": slbNewCfgUrlRedirUriHashLength,
       "slbCurCfgUrlRedirHeader": slbCurCfgUrlRedirHeader,
       "slbNewCfgUrlRedirHeader": slbNewCfgUrlRedirHeader,
       "slbCurCfgUrlRedirHeaderName": slbCurCfgUrlRedirHeaderName,
       "slbNewCfgUrlRedirHeaderName": slbNewCfgUrlRedirHeaderName,
       "slbUrlExpTableMaxSize": slbUrlExpTableMaxSize,
       "slbUrlBalance": slbUrlBalance,
       "slbCurCfgUrlLbPathTable": slbCurCfgUrlLbPathTable,
       "slbCurCfgUrlLbPathTableEntry": slbCurCfgUrlLbPathTableEntry,
       "slbCurCfgUrlLbPathIndex": slbCurCfgUrlLbPathIndex,
       "slbCurCfgUrlLbPathString": slbCurCfgUrlLbPathString,
       "slbCurCfgUrlLbBwmContract": slbCurCfgUrlLbBwmContract,
       "slbNewCfgUrlLbPathTable": slbNewCfgUrlLbPathTable,
       "slbNewCfgUrlLbPathTableEntry": slbNewCfgUrlLbPathTableEntry,
       "slbNewCfgUrlLbPathIndex": slbNewCfgUrlLbPathIndex,
       "slbNewCfgUrlLbPathString": slbNewCfgUrlLbPathString,
       "slbNewCfgUrlLbPathDelete": slbNewCfgUrlLbPathDelete,
       "slbNewCfgUrlLbBwmContract": slbNewCfgUrlLbBwmContract,
       "slbCurCfgUrlLbErrorMsg": slbCurCfgUrlLbErrorMsg,
       "slbNewCfgUrlLbErrorMsg": slbNewCfgUrlLbErrorMsg,
       "slbUrlLbPathTableMaxSize": slbUrlLbPathTableMaxSize,
       "rtspUrlRedir": rtspUrlRedir,
       "rtspUrlExpTableMaxSize": rtspUrlExpTableMaxSize,
       "rtspCurCfgUrlExpTable": rtspCurCfgUrlExpTable,
       "rtspCurCfgUrlExpTableEntry": rtspCurCfgUrlExpTableEntry,
       "rtspCurCfgUrlExpIndex": rtspCurCfgUrlExpIndex,
       "rtspCurCfgUrlExpression": rtspCurCfgUrlExpression,
       "rtspNewCfgUrlExpTable": rtspNewCfgUrlExpTable,
       "rtspNewCfgUrlExpTableEntry": rtspNewCfgUrlExpTableEntry,
       "rtspNewCfgUrlExpIndex": rtspNewCfgUrlExpIndex,
       "rtspNewCfgUrlExpression": rtspNewCfgUrlExpression,
       "rtspNewCfgUrlExpDelete": rtspNewCfgUrlExpDelete,
       "slbCurCfgPmask": slbCurCfgPmask,
       "slbNewCfgPmask": slbNewCfgPmask,
       "slbCurCfgGrace": slbCurCfgGrace,
       "slbNewCfgGrace": slbNewCfgGrace,
       "slbCurCfgPeerTable": slbCurCfgPeerTable,
       "slbCurCfgPeerEntry": slbCurCfgPeerEntry,
       "slbCurCfgPeerIndex": slbCurCfgPeerIndex,
       "slbCurCfgPeerIpAddr": slbCurCfgPeerIpAddr,
       "slbCurCfgPeerState": slbCurCfgPeerState,
       "slbNewCfgPeerTable": slbNewCfgPeerTable,
       "slbNewCfgPeerEntry": slbNewCfgPeerEntry,
       "slbNewCfgPeerIndex": slbNewCfgPeerIndex,
       "slbNewCfgPeerIpAddr": slbNewCfgPeerIpAddr,
       "slbNewCfgPeerState": slbNewCfgPeerState,
       "slbNewCfgPeerDelete": slbNewCfgPeerDelete,
       "slbCurCfgSyncFilt": slbCurCfgSyncFilt,
       "slbNewCfgSyncFilt": slbNewCfgSyncFilt,
       "slbCurCfgSyncPort": slbCurCfgSyncPort,
       "slbNewCfgSyncPort": slbNewCfgSyncPort,
       "slbCurCfgSyncVrrp": slbCurCfgSyncVrrp,
       "slbNewCfgSyncVrrp": slbNewCfgSyncVrrp,
       "slbCurCfgSyncPip": slbCurCfgSyncPip,
       "slbNewCfgSyncPip": slbNewCfgSyncPip,
       "slbCurCfgVirtMatrixArch": slbCurCfgVirtMatrixArch,
       "slbNewCfgVirtMatrixArch": slbNewCfgVirtMatrixArch,
       "slbCurCfgSyncSfo": slbCurCfgSyncSfo,
       "slbNewCfgSyncSfo": slbNewCfgSyncSfo,
       "slbCurCfgSyncSfoUpdatePeriod": slbCurCfgSyncSfoUpdatePeriod,
       "slbNewCfgSyncSfoUpdatePeriod": slbNewCfgSyncSfoUpdatePeriod,
       "slbCurCfgRealServPortTable": slbCurCfgRealServPortTable,
       "slbCurCfgRealServPortEntry": slbCurCfgRealServPortEntry,
       "slbCurCfgRealServIndex": slbCurCfgRealServIndex,
       "slbCurCfgRealServPortIndex": slbCurCfgRealServPortIndex,
       "slbCurCfgRealServRealPort": slbCurCfgRealServRealPort,
       "slbNewCfgRealServPortTable": slbNewCfgRealServPortTable,
       "slbNewCfgRealServPortEntry": slbNewCfgRealServPortEntry,
       "slbNewCfgRealServIndex": slbNewCfgRealServIndex,
       "slbNewCfgRealServPortIndex": slbNewCfgRealServPortIndex,
       "slbNewCfgRealServRealPort": slbNewCfgRealServRealPort,
       "slbNewCfgRealServPortDelete": slbNewCfgRealServPortDelete,
       "slbCurCfgUrlBwmTable": slbCurCfgUrlBwmTable,
       "slbCurCfgUrlBwmEntry": slbCurCfgUrlBwmEntry,
       "slbCurCfgUrlBwmVirtServIndex": slbCurCfgUrlBwmVirtServIndex,
       "slbCurCfgUrlBwmVirtServiceIndex": slbCurCfgUrlBwmVirtServiceIndex,
       "slbCurCfgUrlBwmUrlId": slbCurCfgUrlBwmUrlId,
       "slbCurCfgUrlBwmContract": slbCurCfgUrlBwmContract,
       "slbNewCfgUrlBwmTable": slbNewCfgUrlBwmTable,
       "slbNewCfgUrlBwmEntry": slbNewCfgUrlBwmEntry,
       "slbNewCfgUrlBwmVirtServIndex": slbNewCfgUrlBwmVirtServIndex,
       "slbNewCfgUrlBwmVirtServiceIndex": slbNewCfgUrlBwmVirtServiceIndex,
       "slbNewCfgUrlBwmUrlId": slbNewCfgUrlBwmUrlId,
       "slbNewCfgUrlBwmContract": slbNewCfgUrlBwmContract,
       "slbNewCfgUrlBwmDelete": slbNewCfgUrlBwmDelete,
       "slbRurl": slbRurl,
       "slbRurlGeneral": slbRurlGeneral,
       "slbCurCfgRurlGenDeny": slbCurCfgRurlGenDeny,
       "slbNewCfgRurlGenDeny": slbNewCfgRurlGenDeny,
       "slbRurlDportTableMaxSize": slbRurlDportTableMaxSize,
       "slbCurCfgRurlDportTable": slbCurCfgRurlDportTable,
       "slbCurCfgRurlDportTableEntry": slbCurCfgRurlDportTableEntry,
       "slbCurCfgRurlDportIndex": slbCurCfgRurlDportIndex,
       "slbCurCfgRurlDportLowPort": slbCurCfgRurlDportLowPort,
       "slbCurCfgRurlDportHighPort": slbCurCfgRurlDportHighPort,
       "slbNewCfgRurlDportTable": slbNewCfgRurlDportTable,
       "slbNewCfgRurlDportTableEntry": slbNewCfgRurlDportTableEntry,
       "slbNewCfgRurlDportIndex": slbNewCfgRurlDportIndex,
       "slbNewCfgRurlDportLowPort": slbNewCfgRurlDportLowPort,
       "slbNewCfgRurlDportHighPort": slbNewCfgRurlDportHighPort,
       "slbNewCfgRurlDportDelete": slbNewCfgRurlDportDelete,
       "slbRealServPortTableMaxSize": slbRealServPortTableMaxSize,
       "slbPortTableMaxSize": slbPortTableMaxSize,
       "slbVirtServicesTableMaxSize": slbVirtServicesTableMaxSize,
       "slbUrlBwmTableMaxSize": slbUrlBwmTableMaxSize,
       "slbPeerTableMaxSize": slbPeerTableMaxSize,
       "slbCurCfgFastage": slbCurCfgFastage,
       "slbNewCfgFastage": slbNewCfgFastage,
       "slbCurCfgSlowage": slbCurCfgSlowage,
       "slbNewCfgSlowage": slbNewCfgSlowage,
       "slbWaphc": slbWaphc,
       "slbCurCfgWaphcWSPPort": slbCurCfgWaphcWSPPort,
       "slbNewCfgWaphcWSPPort": slbNewCfgWaphcWSPPort,
       "slbCurCfgWaphcOffset": slbCurCfgWaphcOffset,
       "slbNewCfgWaphcOffset": slbNewCfgWaphcOffset,
       "slbCurCfgWaphcSndContent": slbCurCfgWaphcSndContent,
       "slbNewCfgWaphcSndContent": slbNewCfgWaphcSndContent,
       "slbCurCfgWaphcRcvContent": slbCurCfgWaphcRcvContent,
       "slbNewCfgWaphcRcvContent": slbNewCfgWaphcRcvContent,
       "slbCurCfgWaphcWTLSPort": slbCurCfgWaphcWTLSPort,
       "slbNewCfgWaphcWTLSPort": slbNewCfgWaphcWTLSPort,
       "slbWap": slbWap,
       "slbCurCfgWapTpcp": slbCurCfgWapTpcp,
       "slbNewCfgWapTpcp": slbNewCfgWapTpcp,
       "slbCurCfgWapDebug": slbCurCfgWapDebug,
       "slbNewCfgWapDebug": slbNewCfgWapDebug,
       "slbCurCfgSyncBwm": slbCurCfgSyncBwm,
       "slbNewCfgSyncBwm": slbNewCfgSyncBwm,
       "slbCurCfgTpcp": slbCurCfgTpcp,
       "slbNewCfgTpcp": slbNewCfgTpcp,
       "slbCurCfgMetricInterval": slbCurCfgMetricInterval,
       "slbNewCfgMetricInterval": slbNewCfgMetricInterval,
       "slbCurCfgRealGroupIdslb": slbCurCfgRealGroupIdslb,
       "slbNewCfgRealGroupIdslb": slbNewCfgRealGroupIdslb,
       "slbCurCfgLdapVersion": slbCurCfgLdapVersion,
       "slbNewCfgLdapVersion": slbNewCfgLdapVersion,
       "slbCurCfgIsdInterval": slbCurCfgIsdInterval,
       "slbNewCfgIsdInterval": slbNewCfgIsdInterval,
       "slbCurCfgIsdRetry": slbCurCfgIsdRetry,
       "slbNewCfgIsdRetry": slbNewCfgIsdRetry,
       "slbCurCfgIsdRestr": slbCurCfgIsdRestr,
       "slbNewCfgIsdRestr": slbNewCfgIsdRestr,
       "slbCurCfgIsdNumber": slbCurCfgIsdNumber,
       "slbNewCfgIsdNumber": slbNewCfgIsdNumber,
       "synAttackDetCfg": synAttackDetCfg,
       "synAttackCurCfgInterval": synAttackCurCfgInterval,
       "synAttackNewCfgInterval": synAttackNewCfgInterval,
       "synAttackCurCfgThreshhold": synAttackCurCfgThreshhold,
       "synAttackNewCfgThreshhold": synAttackNewCfgThreshhold,
       "slbCurCfgTcpTimeWindow": slbCurCfgTcpTimeWindow,
       "slbNewCfgTcpTimeWindow": slbNewCfgTcpTimeWindow,
       "slbCurCfgTcpHoldDuration": slbCurCfgTcpHoldDuration,
       "slbNewCfgTcpHoldDuration": slbNewCfgTcpHoldDuration,
       "slbCurCfgAllowHttpHc": slbCurCfgAllowHttpHc,
       "slbNewCfgAllowHttpHc": slbNewCfgAllowHttpHc,
       "slbStats": slbStats,
       "slbStatPortMaintTable": slbStatPortMaintTable,
       "slbStatPortMaintEntry": slbStatPortMaintEntry,
       "slbStatPortMaintPortIndex": slbStatPortMaintPortIndex,
       "slbStatPortMaintCurBindings": slbStatPortMaintCurBindings,
       "slbStatPortMaintBindingFails": slbStatPortMaintBindingFails,
       "slbStatPortMaintNonTcpFrames": slbStatPortMaintNonTcpFrames,
       "slbStatPortMaintTcpFragments": slbStatPortMaintTcpFragments,
       "slbStatPortMaintUdpDatagrams": slbStatPortMaintUdpDatagrams,
       "slbStatPortMaintIncorrectVIPs": slbStatPortMaintIncorrectVIPs,
       "slbStatPortMaintIncorrectVports": slbStatPortMaintIncorrectVports,
       "slbStatPortMaintRealServerNoAvails": slbStatPortMaintRealServerNoAvails,
       "slbStatPortMaintFilteredDeniedFrames": slbStatPortMaintFilteredDeniedFrames,
       "slbStatPortMaintCurBindings4Seconds": slbStatPortMaintCurBindings4Seconds,
       "slbStatPortMaintCurBindings64Seconds": slbStatPortMaintCurBindings64Seconds,
       "slbStatPortMaintVMAdiscards": slbStatPortMaintVMAdiscards,
       "slbStatPortRealServerTable": slbStatPortRealServerTable,
       "slbStatPortRealServerEntry": slbStatPortRealServerEntry,
       "slbStatPortRealServerPortIndex": slbStatPortRealServerPortIndex,
       "slbStatPortRealServerServerIndex": slbStatPortRealServerServerIndex,
       "slbStatPortRealServerCurrSessions": slbStatPortRealServerCurrSessions,
       "slbStatPortRealServerTotalSessions": slbStatPortRealServerTotalSessions,
       "slbStatPortRealServerHCOctets": slbStatPortRealServerHCOctets,
       "slbStatPortRealServerHCOctetsLow32": slbStatPortRealServerHCOctetsLow32,
       "slbStatPortRealServerHCOctetsHigh32": slbStatPortRealServerHCOctetsHigh32,
       "slbStatMaintBackupServActs": slbStatMaintBackupServActs,
       "slbStatMaintOverflowServActs": slbStatMaintOverflowServActs,
       "slbStatRServerTable": slbStatRServerTable,
       "slbStatRServerEntry": slbStatRServerEntry,
       "slbStatRServerIndex": slbStatRServerIndex,
       "slbStatRServerCurrSessions": slbStatRServerCurrSessions,
       "slbStatRServerTotalSessions": slbStatRServerTotalSessions,
       "slbStatRServerFailures": slbStatRServerFailures,
       "slbStatRServerHighestSessions": slbStatRServerHighestSessions,
       "slbStatRServerHCOctets": slbStatRServerHCOctets,
       "slbStatRServerHCOctetsLow32": slbStatRServerHCOctetsLow32,
       "slbStatRServerHCOctetsHigh32": slbStatRServerHCOctetsHigh32,
       "slbStatGroupTable": slbStatGroupTable,
       "slbStatGroupEntry": slbStatGroupEntry,
       "slbStatGroupIndex": slbStatGroupIndex,
       "slbStatGroupCurrSessions": slbStatGroupCurrSessions,
       "slbStatGroupTotalSessions": slbStatGroupTotalSessions,
       "slbStatGroupHighestSessions": slbStatGroupHighestSessions,
       "slbStatGroupHCOctets": slbStatGroupHCOctets,
       "slbStatGroupHCOctetsLow32": slbStatGroupHCOctetsLow32,
       "slbStatGroupHCOctetsHigh32": slbStatGroupHCOctetsHigh32,
       "slbStatVServerTable": slbStatVServerTable,
       "slbStatVServerEntry": slbStatVServerEntry,
       "slbStatVServerIndex": slbStatVServerIndex,
       "slbStatVServerCurrSessions": slbStatVServerCurrSessions,
       "slbStatVServerTotalSessions": slbStatVServerTotalSessions,
       "slbStatVServerHighestSessions": slbStatVServerHighestSessions,
       "slbStatVServerHCOctets": slbStatVServerHCOctets,
       "slbStatVServerHCOctetsLow32": slbStatVServerHCOctetsLow32,
       "slbStatVServerHCOctetsHigh32": slbStatVServerHCOctetsHigh32,
       "slbStatVServerHeaderHits": slbStatVServerHeaderHits,
       "slbStatVServerHeaderMisses": slbStatVServerHeaderMisses,
       "slbStatVServerHeaderTotalSessions": slbStatVServerHeaderTotalSessions,
       "slbStatVServerCookieRewrites": slbStatVServerCookieRewrites,
       "slbStatVServerCookieInserts": slbStatVServerCookieInserts,
       "slbMaintStats": slbMaintStats,
       "slbIncorrectVirtServs": slbIncorrectVirtServs,
       "slbIncorrectVports": slbIncorrectVports,
       "slbNoRealServs": slbNoRealServs,
       "wapMaintStats": wapMaintStats,
       "radiusAcctReqsStats": radiusAcctReqsStats,
       "radiusAcctReqs": radiusAcctReqs,
       "radiusAcctWrapReqs": radiusAcctWrapReqs,
       "radiusAcctStartReqs": radiusAcctStartReqs,
       "radiusAcctUpdateReqs": radiusAcctUpdateReqs,
       "radiusAcctStopReqs": radiusAcctStopReqs,
       "radiusAcctBadReqs": radiusAcctBadReqs,
       "radiusAcctAddSessionReqs": radiusAcctAddSessionReqs,
       "radiusAcctDeleteSessionReqs": radiusAcctDeleteSessionReqs,
       "radiusAcctReqFailsQFull": radiusAcctReqFailsQFull,
       "radiusAcctReqFailsSPDead": radiusAcctReqFailsSPDead,
       "radiusAcctReqFailsDMAFails": radiusAcctReqFailsDMAFails,
       "radiusAcctMaxEntriesInUse": radiusAcctMaxEntriesInUse,
       "tpcpAddSessReqsStats": tpcpAddSessReqsStats,
       "tpcpAddSessReqs": tpcpAddSessReqs,
       "tpcpAddSessReqsFailsQFull": tpcpAddSessReqsFailsQFull,
       "tpcpAddSessReqsFailsSPDead": tpcpAddSessReqsFailsSPDead,
       "tpcpAddSessReqsEntriesInUse": tpcpAddSessReqsEntriesInUse,
       "tpcpAddSessReqsMaxEntriesInUse": tpcpAddSessReqsMaxEntriesInUse,
       "tpcpDeleteSessReqsStats": tpcpDeleteSessReqsStats,
       "tpcpDeleteSessReqs": tpcpDeleteSessReqs,
       "tpcpDeleteSessReqsFailsQFull": tpcpDeleteSessReqsFailsQFull,
       "tpcpDeleteSessReqsFailsSPDead": tpcpDeleteSessReqsFailsSPDead,
       "tpcpDeleteSessReqsEntriesInUse": tpcpDeleteSessReqsEntriesInUse,
       "tpcpDeleteSessReqsMaxEntriesInUse": tpcpDeleteSessReqsMaxEntriesInUse,
       "wapRequestToWrongSP": wapRequestToWrongSP,
       "filterStats": filterStats,
       "fltStatTable": fltStatTable,
       "fltStatTableEntry": fltStatTableEntry,
       "fltStatFltIndex": fltStatFltIndex,
       "fltStatFltFirings": fltStatFltFirings,
       "gslbStats": gslbStats,
       "gslbStatRemRealServerTable": gslbStatRemRealServerTable,
       "gslbStatRemRealServerEntry": gslbStatRemRealServerEntry,
       "gslbStatRemRealServerIndex": gslbStatRemRealServerIndex,
       "gslbStatRemRealServerDnsHandoffs": gslbStatRemRealServerDnsHandoffs,
       "gslbStatRemRealServerHttpRedirs": gslbStatRemRealServerHttpRedirs,
       "gslbMaintStats": gslbMaintStats,
       "gslbStatMaintInGoodSiteUpdates": gslbStatMaintInGoodSiteUpdates,
       "gslbStatMaintInBadSiteUpdates": gslbStatMaintInBadSiteUpdates,
       "urlStats": urlStats,
       "urlRedirStats": urlRedirStats,
       "urlStatRedRedirs": urlStatRedRedirs,
       "urlStatRedOrigSrvs": urlStatRedOrigSrvs,
       "urlStatRedNonGets": urlStatRedNonGets,
       "urlStatRedCookie": urlStatRedCookie,
       "urlStatRedNoCache": urlStatRedNoCache,
       "urlSlbStats": urlSlbStats,
       "urlStatSlbPathTable": urlStatSlbPathTable,
       "urlStatSlbPathTableEntry": urlStatSlbPathTableEntry,
       "urlStatSlbPathIndex": urlStatSlbPathIndex,
       "urlStatSlbPathHits": urlStatSlbPathHits,
       "tcpStats": tcpStats,
       "tcpStatCurConns": tcpStatCurConns,
       "tcpStatHalfOpens": tcpStatHalfOpens,
       "ftpStats": ftpStats,
       "ftpSlbStats": ftpSlbStats,
       "ftpSlbStatTotal": ftpSlbStatTotal,
       "ftpNatStatTotal": ftpNatStatTotal,
       "rurlStats": rurlStats,
       "rurlErrorStats": rurlErrorStats,
       "rurlErrorStatConnect": rurlErrorStatConnect,
       "rurlErrorStatPack": rurlErrorStatPack,
       "rurlErrorStatUnpack": rurlErrorStatUnpack,
       "rurlErrorStatDma": rurlErrorStatDma,
       "rurlErrorStatBuf": rurlErrorStatBuf,
       "rurlErrorStatBufWrap": rurlErrorStatBufWrap,
       "rurlErrorStatProto": rurlErrorStatProto,
       "rurlInfoStats": rurlInfoStats,
       "rurlInfoStatClientWrap": rurlInfoStatClientWrap,
       "rurlInfoStatServerWrap": rurlInfoStatServerWrap,
       "rurlInfoStatBufWrap": rurlInfoStatBufWrap,
       "rurlInfoStatFreeRingCalls": rurlInfoStatFreeRingCalls,
       "rurlInfoStatClientResets": rurlInfoStatClientResets,
       "rurlInfoStatServerResets": rurlInfoStatServerResets,
       "rurlInfoStatFramePassThru": rurlInfoStatFramePassThru,
       "rurlInfoStatParseFiltMiss": rurlInfoStatParseFiltMiss,
       "rurlInfoStatExceedBufLen": rurlInfoStatExceedBufLen,
       "rurlInfoStatExceedFrameDepth": rurlInfoStatExceedFrameDepth,
       "rurlInfoStatZeroContentLen": rurlInfoStatZeroContentLen,
       "rurlInfoStatNonTypicalOffsets": rurlInfoStatNonTypicalOffsets,
       "rurlInfoStatFINRSTSessSetup": rurlInfoStatFINRSTSessSetup,
       "rurlInfoStatPSHSessSetup": rurlInfoStatPSHSessSetup,
       "rurlInfoStatNonSYNSessSetup": rurlInfoStatNonSYNSessSetup,
       "rurlInfoStatL7BindCalls": rurlInfoStatL7BindCalls,
       "rurlInfoStatSessSetups": rurlInfoStatSessSetups,
       "rurlInfoStatMiscProcess": rurlInfoStatMiscProcess,
       "rurlInfoStatClientPktsIn": rurlInfoStatClientPktsIn,
       "rurlInfoStatClientSYNsIn": rurlInfoStatClientSYNsIn,
       "rurlInfoStatClientReTXSYNsSeen": rurlInfoStatClientReTXSYNsSeen,
       "rurlInfoStatClientSYNACKsSent": rurlInfoStatClientSYNACKsSent,
       "rurlInfoStatClientACKsIn": rurlInfoStatClientACKsIn,
       "rurlInfoStatClientDataIn": rurlInfoStatClientDataIn,
       "rurlInfoStatClientDataRetx": rurlInfoStatClientDataRetx,
       "rurlInfoStatServerSYNsSent": rurlInfoStatServerSYNsSent,
       "rurlInfoStatServerSYNACKsIn": rurlInfoStatServerSYNACKsIn,
       "rurlInfoStatServerACKsSent": rurlInfoStatServerACKsSent,
       "rurlInfoStatServerACKsIn": rurlInfoStatServerACKsIn,
       "rurlInfoStatServerSYNsRetx": rurlInfoStatServerSYNsRetx,
       "rurlInfoStatServerSYNsRetxErrors": rurlInfoStatServerSYNsRetxErrors,
       "rurlInfoStatL7SessionReuse": rurlInfoStatL7SessionReuse,
       "rurlInfoStatConnSpliced": rurlInfoStatConnSpliced,
       "rurlMaintStats": rurlMaintStats,
       "rurlMaintStatOrgServerHits": rurlMaintStatOrgServerHits,
       "rurlMaintStatHTTPRedirs": rurlMaintStatHTTPRedirs,
       "rurlMaintStatServerReqs": rurlMaintStatServerReqs,
       "rurlMaintStatServerAcks": rurlMaintStatServerAcks,
       "rurlMaintStatSessCnt": rurlMaintStatSessCnt,
       "rurlMaintStatLastFrameCnt": rurlMaintStatLastFrameCnt,
       "rurlMaintStatConnectRxmit": rurlMaintStatConnectRxmit,
       "rurlMaintStatResetRxmit": rurlMaintStatResetRxmit,
       "rurlMaintStatCurRdirIPEntries": rurlMaintStatCurRdirIPEntries,
       "rurlMaintStatHighRdirIPEntries": rurlMaintStatHighRdirIPEntries,
       "rurlMaintStatCurRdirPORTEntries": rurlMaintStatCurRdirPORTEntries,
       "rurlMaintStatHighRdirPORTEntries": rurlMaintStatHighRdirPORTEntries,
       "rurlMaintStatCurRdirIPPORTEntries": rurlMaintStatCurRdirIPPORTEntries,
       "rurlMaintStatHighRdirIPPORTEntries": rurlMaintStatHighRdirIPPORTEntries,
       "rurlMaintStatCurRSEQBufEntries": rurlMaintStatCurRSEQBufEntries,
       "rurlMaintStatHighRSEQBufEntries": rurlMaintStatHighRSEQBufEntries,
       "rurlMaintStatCurRBUFBufEntries": rurlMaintStatCurRBUFBufEntries,
       "rurlMaintStatHighRBUFBufEntries": rurlMaintStatHighRBUFBufEntries,
       "rurlMaintStatRSEQBufAllocs": rurlMaintStatRSEQBufAllocs,
       "rurlMaintStatRSEQBufFrees": rurlMaintStatRSEQBufFrees,
       "rurlMaintStatRSEQFailBufAllocs": rurlMaintStatRSEQFailBufAllocs,
       "rurlMaintStatRSEQFailBufFrees": rurlMaintStatRSEQFailBufFrees,
       "rurlMaintStatRBUFBufAllocs": rurlMaintStatRBUFBufAllocs,
       "rurlMaintStatRBUFBufFrees": rurlMaintStatRBUFBufFrees,
       "rurlMaintStatRBUFFailBufAllocs": rurlMaintStatRBUFFailBufAllocs,
       "rurlMaintStatRBUFFailBufFrees": rurlMaintStatRBUFFailBufFrees,
       "rurlMaintStatRBUFRetransmit": rurlMaintStatRBUFRetransmit,
       "rurlMaintStatRBUFChanged": rurlMaintStatRBUFChanged,
       "rtspStats": rtspStats,
       "rtspStatControlConns": rtspStatControlConns,
       "rtspStatUDPStreams": rtspStatUDPStreams,
       "rtspStatRedirects": rtspStatRedirects,
       "rtspStatConnDenied": rtspStatConnDenied,
       "rtspStatAllocFails": rtspStatAllocFails,
       "tcpLimitStats": tcpLimitStats,
       "tcpLimitStatHoldDowns": tcpLimitStatHoldDowns,
       "tcpLimitStatClientEntries": tcpLimitStatClientEntries,
       "nasaStats": nasaStats,
       "nasaStatSpTable": nasaStatSpTable,
       "nasaStatSpEntry": nasaStatSpEntry,
       "nasaStatSpPortIndex": nasaStatSpPortIndex,
       "nasaStatSpCtlTunnelIn": nasaStatSpCtlTunnelIn,
       "nasaStatSpCtlTunnelInvalidPkt": nasaStatSpCtlTunnelInvalidPkt,
       "nasaStatSpReqSessCnt": nasaStatSpReqSessCnt,
       "nasaStatSpSessAddCnt": nasaStatSpSessAddCnt,
       "nasaStatSpSessDelCnt": nasaStatSpSessDelCnt,
       "nasaStatSpSessUpdCnt": nasaStatSpSessUpdCnt,
       "nasaStatSpSessRdCnt": nasaStatSpSessRdCnt,
       "nasaStatSpSessCharCnt": nasaStatSpSessCharCnt,
       "nasaStatSpReqSessNoIsd": nasaStatSpReqSessNoIsd,
       "nasaStatSpCtlTunnelToMp": nasaStatSpCtlTunnelToMp,
       "nasaStatSpBcastTunnelCnt": nasaStatSpBcastTunnelCnt,
       "nasaStatSpBcastTunnelToMp": nasaStatSpBcastTunnelToMp,
       "nasaStatSpBcastTunnelToIsd": nasaStatSpBcastTunnelToIsd,
       "nasaStatSpRurlTunnelCnt": nasaStatSpRurlTunnelCnt,
       "nasaStatSpIpDatagramCnt": nasaStatSpIpDatagramCnt,
       "nasaStatSpCliRedirectCnt": nasaStatSpCliRedirectCnt,
       "nasaStatSpInvalidVersion": nasaStatSpInvalidVersion,
       "nasaStatSpAckTx": nasaStatSpAckTx,
       "nasaStatSpAckRx": nasaStatSpAckRx,
       "nasaStatSpAckAlloc": nasaStatSpAckAlloc,
       "nasaStatSpAckFree": nasaStatSpAckFree,
       "nasaStatSpAllocAckFail": nasaStatSpAllocAckFail,
       "nasaStatSpAllocFrmFail": nasaStatSpAllocFrmFail,
       "nasaStatSpRexmitFail": nasaStatSpRexmitFail,
       "nasaStatSpInvalidIsd": nasaStatSpInvalidIsd,
       "nasaStatSpInvalidPkts": nasaStatSpInvalidPkts,
       "nasaMpStats": nasaMpStats,
       "nasaStatMpTotalRx": nasaStatMpTotalRx,
       "nasaStatMpTotalTx": nasaStatMpTotalTx,
       "nasaStatMpBadCksum": nasaStatMpBadCksum,
       "nasaStatMpInvalidRx": nasaStatMpInvalidRx,
       "nasaStatMpPingRequests": nasaStatMpPingRequests,
       "nasaStatMpPingResponses": nasaStatMpPingResponses,
       "nasaStatMpRegRequests": nasaStatMpRegRequests,
       "nasaStatMpCapResponses": nasaStatMpCapResponses,
       "nasaStatMpRegConfirmations": nasaStatMpRegConfirmations,
       "nasaStatMpUnregRequests": nasaStatMpUnregRequests,
       "nasaStatMpHealthRequests": nasaStatMpHealthRequests,
       "nasaStatMpHealthResponses": nasaStatMpHealthResponses,
       "nasaStatMpCmdRequests": nasaStatMpCmdRequests,
       "nasaStatMpCmdResponses": nasaStatMpCmdResponses,
       "dnsSlbStats": dnsSlbStats,
       "dnsSlbStatTCPQueries": dnsSlbStatTCPQueries,
       "dnsSlbStatUDPQueries": dnsSlbStatUDPQueries,
       "dnsSlbStatInvalidQueries": dnsSlbStatInvalidQueries,
       "dnsSlbStatMultipleQueries": dnsSlbStatMultipleQueries,
       "dnsSlbStatDnameParseErrors": dnsSlbStatDnameParseErrors,
       "dnsSlbStatFailedMatches": dnsSlbStatFailedMatches,
       "dnsSlbStatInternalErrors": dnsSlbStatInternalErrors,
       "slb-info": slb_info,
       "slbFailOverInfoTable": slbFailOverInfoTable,
       "slbFailOverInfoEntry": slbFailOverInfoEntry,
       "slbFailOverInfoIndex": slbFailOverInfoIndex,
       "slbFailOverInfoPrimaryIp": slbFailOverInfoPrimaryIp,
       "slbFailOverInfoPrimaryStatus": slbFailOverInfoPrimaryStatus,
       "slbFailOverInfoPrimaryState": slbFailOverInfoPrimaryState,
       "slbFailOverInfoSecondaryIp": slbFailOverInfoSecondaryIp,
       "slbFailOverInfoSecondaryStatus": slbFailOverInfoSecondaryStatus,
       "slbFailOverInfoSecondaryState": slbFailOverInfoSecondaryState,
       "slbRealServerInfoTable": slbRealServerInfoTable,
       "slbRealServerInfoEntry": slbRealServerInfoEntry,
       "slbRealServerInfoIndex": slbRealServerInfoIndex,
       "slbRealServerInfoIpAddr": slbRealServerInfoIpAddr,
       "slbRealServerMacAddr": slbRealServerMacAddr,
       "slbRealServerInfoSwitchPort": slbRealServerInfoSwitchPort,
       "slbRealServerInfoHealthLayer": slbRealServerInfoHealthLayer,
       "slbRealServerInfoOverflow": slbRealServerInfoOverflow,
       "slbRealServerInfoState": slbRealServerInfoState,
       "nasaIsdInfoTable": nasaIsdInfoTable,
       "nasaIsdInfoEntry": nasaIsdInfoEntry,
       "nasaIsdInfoIndex": nasaIsdInfoIndex,
       "nasaIsdInfoIpAddr": nasaIsdInfoIpAddr,
       "nasaIsdMacAddr": nasaIsdMacAddr,
       "nasaIsdInfoSwitchPort": nasaIsdInfoSwitchPort,
       "nasaIsdInfoGdi": nasaIsdInfoGdi,
       "nasaIsdInfoState": nasaIsdInfoState,
       "nasaIsdInfoStateChange": nasaIsdInfoStateChange,
       "filtering": filtering,
       "fltCfgTableMaxSize": fltCfgTableMaxSize,
       "fltCurCfgTable": fltCurCfgTable,
       "fltCurCfgTableEntry": fltCurCfgTableEntry,
       "fltCurCfgIndx": fltCurCfgIndx,
       "fltCurCfgSrcIp": fltCurCfgSrcIp,
       "fltCurCfgSrcIpMask": fltCurCfgSrcIpMask,
       "fltCurCfgDstIp": fltCurCfgDstIp,
       "fltCurCfgDstIpMask": fltCurCfgDstIpMask,
       "fltCurCfgProtocol": fltCurCfgProtocol,
       "fltCurCfgRangeHighSrcPort": fltCurCfgRangeHighSrcPort,
       "fltCurCfgRangeLowSrcPort": fltCurCfgRangeLowSrcPort,
       "fltCurCfgRangeLowDstPort": fltCurCfgRangeLowDstPort,
       "fltCurCfgRangeHighDstPort": fltCurCfgRangeHighDstPort,
       "fltCurCfgAction": fltCurCfgAction,
       "fltCurCfgRedirPort": fltCurCfgRedirPort,
       "fltCurCfgRedirGroup": fltCurCfgRedirGroup,
       "fltCurCfgLog": fltCurCfgLog,
       "fltCurCfgState": fltCurCfgState,
       "fltCurCfgNat": fltCurCfgNat,
       "fltCurCfgCache": fltCurCfgCache,
       "fltCurCfgInvert": fltCurCfgInvert,
       "fltCurCfgClientProxy": fltCurCfgClientProxy,
       "fltCurCfgTcpAck": fltCurCfgTcpAck,
       "fltCurCfgUrlRedir": fltCurCfgUrlRedir,
       "fltCurCfgSrcMac": fltCurCfgSrcMac,
       "fltCurCfgDstMac": fltCurCfgDstMac,
       "fltCurCfgFtpNatActive": fltCurCfgFtpNatActive,
       "fltCurCfgAclTcpUrg": fltCurCfgAclTcpUrg,
       "fltCurCfgAclTcpAck": fltCurCfgAclTcpAck,
       "fltCurCfgAclTcpPsh": fltCurCfgAclTcpPsh,
       "fltCurCfgAclTcpRst": fltCurCfgAclTcpRst,
       "fltCurCfgAclTcpSyn": fltCurCfgAclTcpSyn,
       "fltCurCfgAclTcpFin": fltCurCfgAclTcpFin,
       "fltCurCfgAclIcmp": fltCurCfgAclIcmp,
       "fltCurCfgAclIpOption": fltCurCfgAclIpOption,
       "fltCurCfgBwmContract": fltCurCfgBwmContract,
       "fltCurCfgAclIpTos": fltCurCfgAclIpTos,
       "fltCurCfgAclIpTosMask": fltCurCfgAclIpTosMask,
       "fltCurCfgAclIpTosNew": fltCurCfgAclIpTosNew,
       "fltCurCfgFwlb": fltCurCfgFwlb,
       "fltCurCfgNatTimeout": fltCurCfgNatTimeout,
       "fltCurCfgRurl": fltCurCfgRurl,
       "fltCurCfgLinklb": fltCurCfgLinklb,
       "fltCurCfgWapRadiusSnoop": fltCurCfgWapRadiusSnoop,
       "fltCurCfgSrcIpMac": fltCurCfgSrcIpMac,
       "fltCurCfgDstIpMac": fltCurCfgDstIpMac,
       "fltCurCfgIdslbHash": fltCurCfgIdslbHash,
       "fltCurCfgVlan": fltCurCfgVlan,
       "fltCurCfgName": fltCurCfgName,
       "fltCurCfgTcpRateLimit": fltCurCfgTcpRateLimit,
       "fltCurCfgTcpRateMaxConn": fltCurCfgTcpRateMaxConn,
       "fltCurCfgHash": fltCurCfgHash,
       "fltCurCfgNasa": fltCurCfgNasa,
       "fltCurCfgLayer7DenyState": fltCurCfgLayer7DenyState,
       "fltCurCfgLayer7DenyUrlBmap": fltCurCfgLayer7DenyUrlBmap,
       "fltNewCfgTable": fltNewCfgTable,
       "fltNewCfgTableEntry": fltNewCfgTableEntry,
       "fltNewCfgIndx": fltNewCfgIndx,
       "fltNewCfgSrcIp": fltNewCfgSrcIp,
       "fltNewCfgSrcIpMask": fltNewCfgSrcIpMask,
       "fltNewCfgDstIp": fltNewCfgDstIp,
       "fltNewCfgDstIpMask": fltNewCfgDstIpMask,
       "fltNewCfgProtocol": fltNewCfgProtocol,
       "fltNewCfgRangeHighSrcPort": fltNewCfgRangeHighSrcPort,
       "fltNewCfgRangeLowSrcPort": fltNewCfgRangeLowSrcPort,
       "fltNewCfgRangeLowDstPort": fltNewCfgRangeLowDstPort,
       "fltNewCfgRangeHighDstPort": fltNewCfgRangeHighDstPort,
       "fltNewCfgAction": fltNewCfgAction,
       "fltNewCfgRedirPort": fltNewCfgRedirPort,
       "fltNewCfgRedirGroup": fltNewCfgRedirGroup,
       "fltNewCfgLog": fltNewCfgLog,
       "fltNewCfgState": fltNewCfgState,
       "fltNewCfgDelete": fltNewCfgDelete,
       "fltNewCfgNat": fltNewCfgNat,
       "fltNewCfgCache": fltNewCfgCache,
       "fltNewCfgInvert": fltNewCfgInvert,
       "fltNewCfgClientProxy": fltNewCfgClientProxy,
       "fltNewCfgTcpAck": fltNewCfgTcpAck,
       "fltNewCfgUrlRedir": fltNewCfgUrlRedir,
       "fltNewCfgSrcMac": fltNewCfgSrcMac,
       "fltNewCfgDstMac": fltNewCfgDstMac,
       "fltNewCfgFtpNatActive": fltNewCfgFtpNatActive,
       "fltNewCfgAclTcpUrg": fltNewCfgAclTcpUrg,
       "fltNewCfgAclTcpAck": fltNewCfgAclTcpAck,
       "fltNewCfgAclTcpPsh": fltNewCfgAclTcpPsh,
       "fltNewCfgAclTcpRst": fltNewCfgAclTcpRst,
       "fltNewCfgAclTcpSyn": fltNewCfgAclTcpSyn,
       "fltNewCfgAclTcpFin": fltNewCfgAclTcpFin,
       "fltNewCfgAclIcmp": fltNewCfgAclIcmp,
       "fltNewCfgAclIpOption": fltNewCfgAclIpOption,
       "fltNewCfgBwmContract": fltNewCfgBwmContract,
       "fltNewCfgAclIpTos": fltNewCfgAclIpTos,
       "fltNewCfgAclIpTosMask": fltNewCfgAclIpTosMask,
       "fltNewCfgAclIpTosNew": fltNewCfgAclIpTosNew,
       "fltNewCfgFwlb": fltNewCfgFwlb,
       "fltNewCfgNatTimeout": fltNewCfgNatTimeout,
       "fltNewCfgRurl": fltNewCfgRurl,
       "fltNewCfgLinklb": fltNewCfgLinklb,
       "fltNewCfgWapRadiusSnoop": fltNewCfgWapRadiusSnoop,
       "fltNewCfgSrcIpMac": fltNewCfgSrcIpMac,
       "fltNewCfgDstIpMac": fltNewCfgDstIpMac,
       "fltNewCfgIdslbHash": fltNewCfgIdslbHash,
       "fltNewCfgVlan": fltNewCfgVlan,
       "fltNewCfgName": fltNewCfgName,
       "fltNewCfgTcpRateLimit": fltNewCfgTcpRateLimit,
       "fltNewCfgTcpRateMaxConn": fltNewCfgTcpRateMaxConn,
       "fltNewCfgHash": fltNewCfgHash,
       "fltNewCfgNasa": fltNewCfgNasa,
       "fltNewCfgLayer7DenyState": fltNewCfgLayer7DenyState,
       "fltNewCfgLayer7DenyUrlBmap": fltNewCfgLayer7DenyUrlBmap,
       "fltNewCfgLayer7DenyAddUrl": fltNewCfgLayer7DenyAddUrl,
       "fltNewCfgLayer7DenyRemUrl": fltNewCfgLayer7DenyRemUrl,
       "fltCurCfgPortTable": fltCurCfgPortTable,
       "fltCurCfgPortTableEntry": fltCurCfgPortTableEntry,
       "fltCurCfgPortIndx": fltCurCfgPortIndx,
       "fltCurCfgPortState": fltCurCfgPortState,
       "fltCurCfgPortFiltBmap": fltCurCfgPortFiltBmap,
       "fltNewCfgPortTable": fltNewCfgPortTable,
       "fltNewCfgPortTableEntry": fltNewCfgPortTableEntry,
       "fltNewCfgPortIndx": fltNewCfgPortIndx,
       "fltNewCfgPortState": fltNewCfgPortState,
       "fltNewCfgPortFiltBmap": fltNewCfgPortFiltBmap,
       "fltNewCfgPortAddFiltRule": fltNewCfgPortAddFiltRule,
       "fltNewCfgPortRemFiltRule": fltNewCfgPortRemFiltRule,
       "fltCurCfgUrlBwmTable": fltCurCfgUrlBwmTable,
       "fltCurCfgUrlBwmEntry": fltCurCfgUrlBwmEntry,
       "fltCurCfgUrlBwmFltIndex": fltCurCfgUrlBwmFltIndex,
       "fltCurCfgUrlBwmUrlId": fltCurCfgUrlBwmUrlId,
       "fltCurCfgUrlBwmContract": fltCurCfgUrlBwmContract,
       "fltNewCfgUrlBwmTable": fltNewCfgUrlBwmTable,
       "fltNewCfgUrlBwmEntry": fltNewCfgUrlBwmEntry,
       "fltNewCfgUrlBwmFltIndex": fltNewCfgUrlBwmFltIndex,
       "fltNewCfgUrlBwmUrlId": fltNewCfgUrlBwmUrlId,
       "fltNewCfgUrlBwmContract": fltNewCfgUrlBwmContract,
       "fltNewCfgUrlBwmDelete": fltNewCfgUrlBwmDelete,
       "fltUrlBwmTableMaxSize": fltUrlBwmTableMaxSize,
       "globalSLB": globalSLB,
       "gslbGeneral": gslbGeneral,
       "gslbCurCfgGenState": gslbCurCfgGenState,
       "gslbNewCfgGenState": gslbNewCfgGenState,
       "gslbCurCfgGenDnsHandoff": gslbCurCfgGenDnsHandoff,
       "gslbNewCfgGenDnsHandoff": gslbNewCfgGenDnsHandoff,
       "gslbCurCfgGenDnsTTL": gslbCurCfgGenDnsTTL,
       "gslbNewCfgGenDnsTTL": gslbNewCfgGenDnsTTL,
       "gslbCurCfgGenHttpRedirect": gslbCurCfgGenHttpRedirect,
       "gslbNewCfgGenHttpRedirect": gslbNewCfgGenHttpRedirect,
       "gslbCurCfgGenRemSiteUpdateInterval": gslbCurCfgGenRemSiteUpdateInterval,
       "gslbNewCfgGenRemSiteUpdateInterval": gslbNewCfgGenRemSiteUpdateInterval,
       "gslbCurCfgGenDnsLocalPref": gslbCurCfgGenDnsLocalPref,
       "gslbNewCfgGenDnsLocalPref": gslbNewCfgGenDnsLocalPref,
       "gslbCurCfgGenMinco": gslbCurCfgGenMinco,
       "gslbNewCfgGenMinco": gslbNewCfgGenMinco,
       "gslbCurCfgGenOne": gslbCurCfgGenOne,
       "gslbNewCfgGenOne": gslbNewCfgGenOne,
       "gslbCurCfgGenUsern": gslbCurCfgGenUsern,
       "gslbNewCfgGenUsern": gslbNewCfgGenUsern,
       "gslbCurCfgGenGeo": gslbCurCfgGenGeo,
       "gslbNewCfgGenGeo": gslbNewCfgGenGeo,
       "gslbCurCfgGenAlways": gslbCurCfgGenAlways,
       "gslbNewCfgGenAlways": gslbNewCfgGenAlways,
       "gslbCurCfgGenWeight": gslbCurCfgGenWeight,
       "gslbNewCfgGenWeight": gslbNewCfgGenWeight,
       "gslbDNS": gslbDNS,
       "dnsCurCfgPrimaryIpAddr": dnsCurCfgPrimaryIpAddr,
       "dnsNewCfgPrimaryIpAddr": dnsNewCfgPrimaryIpAddr,
       "dnsCurCfgSecondaryIpAddr": dnsCurCfgSecondaryIpAddr,
       "dnsNewCfgSecondaryIpAddr": dnsNewCfgSecondaryIpAddr,
       "dnsCurCfgDomainName": dnsCurCfgDomainName,
       "dnsNewCfgDomainName": dnsNewCfgDomainName,
       "gslbSites": gslbSites,
       "gslbRemSiteTableMaxSize": gslbRemSiteTableMaxSize,
       "gslbCurCfgRemSiteTable": gslbCurCfgRemSiteTable,
       "gslbCurCfgRemSiteTableEntry": gslbCurCfgRemSiteTableEntry,
       "gslbCurCfgRemSiteIndx": gslbCurCfgRemSiteIndx,
       "gslbCurCfgRemSitePrimaryIp": gslbCurCfgRemSitePrimaryIp,
       "gslbCurCfgRemSiteSecondaryIp": gslbCurCfgRemSiteSecondaryIp,
       "gslbCurCfgRemSiteState": gslbCurCfgRemSiteState,
       "gslbCurCfgRemSiteUpdate": gslbCurCfgRemSiteUpdate,
       "gslbCurCfgRemSiteName": gslbCurCfgRemSiteName,
       "gslbNewCfgRemSiteTable": gslbNewCfgRemSiteTable,
       "gslbNewCfgRemSiteTableEntry": gslbNewCfgRemSiteTableEntry,
       "gslbNewCfgRemSiteIndx": gslbNewCfgRemSiteIndx,
       "gslbNewCfgRemSitePrimaryIp": gslbNewCfgRemSitePrimaryIp,
       "gslbNewCfgRemSiteSecondaryIp": gslbNewCfgRemSiteSecondaryIp,
       "gslbNewCfgRemSiteState": gslbNewCfgRemSiteState,
       "gslbNewCfgRemSiteUpdate": gslbNewCfgRemSiteUpdate,
       "gslbNewCfgRemSiteDelete": gslbNewCfgRemSiteDelete,
       "gslbNewCfgRemSiteName": gslbNewCfgRemSiteName,
       "gslbLookup": gslbLookup,
       "gslbCurCfgGenLookups": gslbCurCfgGenLookups,
       "gslbNewCfgGenLookups": gslbNewCfgGenLookups,
       "gslbCurCfgGenLookupDname": gslbCurCfgGenLookupDname,
       "gslbNewCfgGenLookupDname": gslbNewCfgGenLookupDname,
       "gslbNetwork": gslbNetwork,
       "gslbNetworkTableMaxSize": gslbNetworkTableMaxSize,
       "gslbCurCfgNetworkTable": gslbCurCfgNetworkTable,
       "gslbCurCfgNetworkTableEntry": gslbCurCfgNetworkTableEntry,
       "gslbCurCfgNetworkIndx": gslbCurCfgNetworkIndx,
       "gslbCurCfgNetworkSourceIp": gslbCurCfgNetworkSourceIp,
       "gslbCurCfgNetworkNetMask": gslbCurCfgNetworkNetMask,
       "gslbCurCfgNetworkVip1": gslbCurCfgNetworkVip1,
       "gslbCurCfgNetworkVip2": gslbCurCfgNetworkVip2,
       "gslbNewCfgNetworkTable": gslbNewCfgNetworkTable,
       "gslbNewCfgNetworkTableEntry": gslbNewCfgNetworkTableEntry,
       "gslbNewCfgNetworkIndx": gslbNewCfgNetworkIndx,
       "gslbNewCfgNetworkSourceIp": gslbNewCfgNetworkSourceIp,
       "gslbNewCfgNetworkNetMask": gslbNewCfgNetworkNetMask,
       "gslbNewCfgNetworkVip1": gslbNewCfgNetworkVip1,
       "gslbNewCfgNetworkVip2": gslbNewCfgNetworkVip2,
       "gslbNewCfgNetworkDelete": gslbNewCfgNetworkDelete,
       "gslbCurCfgGenExternal": gslbCurCfgGenExternal,
       "gslbNewCfgGenExternal": gslbNewCfgGenExternal,
       "gslbCurCfgGenEip": gslbCurCfgGenEip,
       "gslbNewCfgGenEip": gslbNewCfgGenEip,
       "gslbCurCfgGenLookupPort": gslbCurCfgGenLookupPort,
       "gslbNewCfgGenLookupPort": gslbNewCfgGenLookupPort,
       "gslbCurCfgGenLookupTimeout": gslbCurCfgGenLookupTimeout,
       "gslbNewCfgGenLookupTimeout": gslbNewCfgGenLookupTimeout,
       "dynamicSLB": dynamicSLB,
       "dynSLBRealServerTable": dynSLBRealServerTable,
       "dynSLBRealServerEntry": dynSLBRealServerEntry,
       "dynSLBRealServerIpAddr": dynSLBRealServerIpAddr,
       "dynSLBRealServerPortNum": dynSLBRealServerPortNum,
       "dynSLBRealServerWeight": dynSLBRealServerWeight,
       "operSlbPortTable": operSlbPortTable,
       "operSlbPortEntry": operSlbPortEntry,
       "operSlbPortIndex": operSlbPortIndex,
       "operSlbPortClrSessionTab": operSlbPortClrSessionTab,
       "slbOper": slbOper,
       "slbOperRealServerTable": slbOperRealServerTable,
       "slbOperRealServerEntry": slbOperRealServerEntry,
       "slbOperRealServerIndex": slbOperRealServerIndex,
       "slbOperRealServerStatus": slbOperRealServerStatus,
       "slbOperConfigSync": slbOperConfigSync}
)
