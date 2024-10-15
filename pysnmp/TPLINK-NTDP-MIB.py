# SNMP MIB module (TPLINK-NTDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-NTDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:26 2024
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

(ntdpManage,) = mibBuilder.importSymbols(
    "TPLINK-CLUSTER-MIB",
    "ntdpManage")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtdpGlobalConfig_ObjectIdentity = ObjectIdentity
ntdpGlobalConfig = _NtdpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1)
)


class _NtdpStatus_Type(Integer32):
    """Custom type ntdpStatus based on Integer32"""
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


_NtdpStatus_Type.__name__ = "Integer32"
_NtdpStatus_Object = MibScalar
ntdpStatus = _NtdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 1),
    _NtdpStatus_Type()
)
ntdpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntdpStatus.setStatus("current")


class _NtdpIntervalTime_Type(Integer32):
    """Custom type ntdpIntervalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_NtdpIntervalTime_Type.__name__ = "Integer32"
_NtdpIntervalTime_Object = MibScalar
ntdpIntervalTime = _NtdpIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 2),
    _NtdpIntervalTime_Type()
)
ntdpIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntdpIntervalTime.setStatus("current")


class _NtdpHop_Type(Integer32):
    """Custom type ntdpHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NtdpHop_Type.__name__ = "Integer32"
_NtdpHop_Object = MibScalar
ntdpHop = _NtdpHop_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 3),
    _NtdpHop_Type()
)
ntdpHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntdpHop.setStatus("current")


class _NtdpHopDelay_Type(Integer32):
    """Custom type ntdpHopDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NtdpHopDelay_Type.__name__ = "Integer32"
_NtdpHopDelay_Object = MibScalar
ntdpHopDelay = _NtdpHopDelay_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 4),
    _NtdpHopDelay_Type()
)
ntdpHopDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntdpHopDelay.setStatus("current")


class _NtpdPortDelay_Type(Integer32):
    """Custom type ntpdPortDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NtpdPortDelay_Type.__name__ = "Integer32"
_NtpdPortDelay_Object = MibScalar
ntpdPortDelay = _NtpdPortDelay_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 1, 5),
    _NtpdPortDelay_Type()
)
ntpdPortDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpdPortDelay.setStatus("current")
_NtdpPortTable_Object = MibTable
ntdpPortTable = _NtdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ntdpPortTable.setStatus("current")
_NtdpPortEntry_Object = MibTableRow
ntdpPortEntry = _NtdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 2, 1)
)
ntdpPortEntry.setIndexNames(
    (0, "TPLINK-NTDP-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ntdpPortEntry.setStatus("current")


class _NtdpPortStatus_Type(Integer32):
    """Custom type ntdpPortStatus based on Integer32"""
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


_NtdpPortStatus_Type.__name__ = "Integer32"
_NtdpPortStatus_Object = MibTableColumn
ntdpPortStatus = _NtdpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 2, 1, 2),
    _NtdpPortStatus_Type()
)
ntdpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntdpPortStatus.setStatus("current")


class _NtdpCollectTopo_Type(Integer32):
    """Custom type ntdpCollectTopo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_NtdpCollectTopo_Type.__name__ = "Integer32"
_NtdpCollectTopo_Object = MibScalar
ntdpCollectTopo = _NtdpCollectTopo_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2, 4),
    _NtdpCollectTopo_Type()
)
ntdpCollectTopo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntdpCollectTopo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-NTDP-MIB",
    **{"ntdpGlobalConfig": ntdpGlobalConfig,
       "ntdpStatus": ntdpStatus,
       "ntdpIntervalTime": ntdpIntervalTime,
       "ntdpHop": ntdpHop,
       "ntdpHopDelay": ntdpHopDelay,
       "ntpdPortDelay": ntpdPortDelay,
       "ntdpPortTable": ntdpPortTable,
       "ntdpPortEntry": ntdpPortEntry,
       "ntdpPortStatus": ntdpPortStatus,
       "ntdpCollectTopo": ntdpCollectTopo}
)
