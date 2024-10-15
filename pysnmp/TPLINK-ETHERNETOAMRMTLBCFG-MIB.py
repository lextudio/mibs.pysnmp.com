# SNMP MIB module (TPLINK-ETHERNETOAMRMTLBCFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ETHERNETOAMRMTLBCFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:06 2024
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

(ethernetOamRmtLbConfig,) = mibBuilder.importSymbols(
    "TPLINK-ETHERNETOAM-MIB",
    "ethernetOamRmtLbConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthernetOamRmtLbCfgTable_Object = MibTable
ethernetOamRmtLbCfgTable = _EthernetOamRmtLbCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ethernetOamRmtLbCfgTable.setStatus("current")
_EthernetOamRmtLbCfgEntry_Object = MibTableRow
ethernetOamRmtLbCfgEntry = _EthernetOamRmtLbCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1)
)
ethernetOamRmtLbCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethernetOamRmtLbCfgEntry.setStatus("current")
_EthernetOamRmtLbCfgPort_Type = DisplayString
_EthernetOamRmtLbCfgPort_Object = MibTableColumn
ethernetOamRmtLbCfgPort = _EthernetOamRmtLbCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 1),
    _EthernetOamRmtLbCfgPort_Type()
)
ethernetOamRmtLbCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamRmtLbCfgPort.setStatus("current")


class _EthernetOamRmtLbCfgReceivedRemoteLoopback_Type(Integer32):
    """Custom type ethernetOamRmtLbCfgReceivedRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 0),
          ("process", 1))
    )


_EthernetOamRmtLbCfgReceivedRemoteLoopback_Type.__name__ = "Integer32"
_EthernetOamRmtLbCfgReceivedRemoteLoopback_Object = MibTableColumn
ethernetOamRmtLbCfgReceivedRemoteLoopback = _EthernetOamRmtLbCfgReceivedRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 2),
    _EthernetOamRmtLbCfgReceivedRemoteLoopback_Type()
)
ethernetOamRmtLbCfgReceivedRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamRmtLbCfgReceivedRemoteLoopback.setStatus("current")


class _EthernetOamRmtLbCfgRemoteLoopback_Type(Integer32):
    """Custom type ethernetOamRmtLbCfgRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 0),
          ("unchanged", 2))
    )


_EthernetOamRmtLbCfgRemoteLoopback_Type.__name__ = "Integer32"
_EthernetOamRmtLbCfgRemoteLoopback_Object = MibTableColumn
ethernetOamRmtLbCfgRemoteLoopback = _EthernetOamRmtLbCfgRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 3),
    _EthernetOamRmtLbCfgRemoteLoopback_Type()
)
ethernetOamRmtLbCfgRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamRmtLbCfgRemoteLoopback.setStatus("current")


class _EthernetOamRmtLbCfgLAG_Type(OctetString):
    """Custom type ethernetOamRmtLbCfgLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EthernetOamRmtLbCfgLAG_Type.__name__ = "OctetString"
_EthernetOamRmtLbCfgLAG_Object = MibTableColumn
ethernetOamRmtLbCfgLAG = _EthernetOamRmtLbCfgLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 4, 1, 1, 4),
    _EthernetOamRmtLbCfgLAG_Type()
)
ethernetOamRmtLbCfgLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamRmtLbCfgLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ETHERNETOAMRMTLBCFG-MIB",
    **{"ethernetOamRmtLbCfgTable": ethernetOamRmtLbCfgTable,
       "ethernetOamRmtLbCfgEntry": ethernetOamRmtLbCfgEntry,
       "ethernetOamRmtLbCfgPort": ethernetOamRmtLbCfgPort,
       "ethernetOamRmtLbCfgReceivedRemoteLoopback": ethernetOamRmtLbCfgReceivedRemoteLoopback,
       "ethernetOamRmtLbCfgRemoteLoopback": ethernetOamRmtLbCfgRemoteLoopback,
       "ethernetOamRmtLbCfgLAG": ethernetOamRmtLbCfgLAG}
)
