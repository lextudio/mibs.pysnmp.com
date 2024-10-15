# SNMP MIB module (TPLINK-NDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-NDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:24 2024
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

(ndpManage,) = mibBuilder.importSymbols(
    "TPLINK-CLUSTER-MIB",
    "ndpManage")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NdpGlobalConfig_ObjectIdentity = ObjectIdentity
ndpGlobalConfig = _NdpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1)
)


class _NdpStatus_Type(Integer32):
    """Custom type ndpStatus based on Integer32"""
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


_NdpStatus_Type.__name__ = "Integer32"
_NdpStatus_Object = MibScalar
ndpStatus = _NdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1, 1),
    _NdpStatus_Type()
)
ndpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndpStatus.setStatus("current")


class _NdpAgingTime_Type(Integer32):
    """Custom type ndpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_NdpAgingTime_Type.__name__ = "Integer32"
_NdpAgingTime_Object = MibScalar
ndpAgingTime = _NdpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1, 2),
    _NdpAgingTime_Type()
)
ndpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndpAgingTime.setStatus("current")


class _NdpHelloTime_Type(Integer32):
    """Custom type ndpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_NdpHelloTime_Type.__name__ = "Integer32"
_NdpHelloTime_Object = MibScalar
ndpHelloTime = _NdpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 1, 3),
    _NdpHelloTime_Type()
)
ndpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndpHelloTime.setStatus("current")
_NdpPortTable_Object = MibTable
ndpPortTable = _NdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ndpPortTable.setStatus("current")
_NdpPortEntry_Object = MibTableRow
ndpPortEntry = _NdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1)
)
ndpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ndpPortEntry.setStatus("current")


class _NdpPortStatus_Type(Integer32):
    """Custom type ndpPortStatus based on Integer32"""
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


_NdpPortStatus_Type.__name__ = "Integer32"
_NdpPortStatus_Object = MibTableColumn
ndpPortStatus = _NdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 2),
    _NdpPortStatus_Type()
)
ndpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ndpPortStatus.setStatus("current")
_NdpPortRecvPkt_Type = Integer32
_NdpPortRecvPkt_Object = MibTableColumn
ndpPortRecvPkt = _NdpPortRecvPkt_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 3),
    _NdpPortRecvPkt_Type()
)
ndpPortRecvPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndpPortRecvPkt.setStatus("current")
_NdpPortSendPkt_Type = Integer32
_NdpPortSendPkt_Object = MibTableColumn
ndpPortSendPkt = _NdpPortSendPkt_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 4),
    _NdpPortSendPkt_Type()
)
ndpPortSendPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndpPortSendPkt.setStatus("current")
_NdpPortErrPkt_Type = Integer32
_NdpPortErrPkt_Object = MibTableColumn
ndpPortErrPkt = _NdpPortErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 5),
    _NdpPortErrPkt_Type()
)
ndpPortErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndpPortErrPkt.setStatus("current")
_NdpPortNeighborNum_Type = Integer32
_NdpPortNeighborNum_Object = MibTableColumn
ndpPortNeighborNum = _NdpPortNeighborNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1, 2, 1, 6),
    _NdpPortNeighborNum_Type()
)
ndpPortNeighborNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndpPortNeighborNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-NDP-MIB",
    **{"ndpGlobalConfig": ndpGlobalConfig,
       "ndpStatus": ndpStatus,
       "ndpAgingTime": ndpAgingTime,
       "ndpHelloTime": ndpHelloTime,
       "ndpPortTable": ndpPortTable,
       "ndpPortEntry": ndpPortEntry,
       "ndpPortStatus": ndpPortStatus,
       "ndpPortRecvPkt": ndpPortRecvPkt,
       "ndpPortSendPkt": ndpPortSendPkt,
       "ndpPortErrPkt": ndpPortErrPkt,
       "ndpPortNeighborNum": ndpPortNeighborNum}
)
