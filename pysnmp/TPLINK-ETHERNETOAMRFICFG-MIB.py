# SNMP MIB module (TPLINK-ETHERNETOAMRFICFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ETHERNETOAMRFICFG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:05 2024
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

(ethernetOamRfiConfig,) = mibBuilder.importSymbols(
    "TPLINK-ETHERNETOAM-MIB",
    "ethernetOamRfiConfig")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthernetOamRfiCfgTable_Object = MibTable
ethernetOamRfiCfgTable = _EthernetOamRfiCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ethernetOamRfiCfgTable.setStatus("current")
_EthernetOamRfiCfgEntry_Object = MibTableRow
ethernetOamRfiCfgEntry = _EthernetOamRfiCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1)
)
ethernetOamRfiCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethernetOamRfiCfgEntry.setStatus("current")
_EthernetOamRfiCfgPort_Type = DisplayString
_EthernetOamRfiCfgPort_Object = MibTableColumn
ethernetOamRfiCfgPort = _EthernetOamRfiCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 1),
    _EthernetOamRfiCfgPort_Type()
)
ethernetOamRfiCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamRfiCfgPort.setStatus("current")


class _EthernetOamRfiCfgDyingGaspNotify_Type(Integer32):
    """Custom type ethernetOamRfiCfgDyingGaspNotify based on Integer32"""
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


_EthernetOamRfiCfgDyingGaspNotify_Type.__name__ = "Integer32"
_EthernetOamRfiCfgDyingGaspNotify_Object = MibTableColumn
ethernetOamRfiCfgDyingGaspNotify = _EthernetOamRfiCfgDyingGaspNotify_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 2),
    _EthernetOamRfiCfgDyingGaspNotify_Type()
)
ethernetOamRfiCfgDyingGaspNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamRfiCfgDyingGaspNotify.setStatus("current")


class _EthernetOamRfiCfgCriticalEventNotify_Type(Integer32):
    """Custom type ethernetOamRfiCfgCriticalEventNotify based on Integer32"""
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


_EthernetOamRfiCfgCriticalEventNotify_Type.__name__ = "Integer32"
_EthernetOamRfiCfgCriticalEventNotify_Object = MibTableColumn
ethernetOamRfiCfgCriticalEventNotify = _EthernetOamRfiCfgCriticalEventNotify_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 3),
    _EthernetOamRfiCfgCriticalEventNotify_Type()
)
ethernetOamRfiCfgCriticalEventNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamRfiCfgCriticalEventNotify.setStatus("current")


class _EthernetOamRfiCfgLAG_Type(OctetString):
    """Custom type ethernetOamRfiCfgLAG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_EthernetOamRfiCfgLAG_Type.__name__ = "OctetString"
_EthernetOamRfiCfgLAG_Object = MibTableColumn
ethernetOamRfiCfgLAG = _EthernetOamRfiCfgLAG_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 60, 1, 3, 1, 1, 4),
    _EthernetOamRfiCfgLAG_Type()
)
ethernetOamRfiCfgLAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamRfiCfgLAG.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ETHERNETOAMRFICFG-MIB",
    **{"ethernetOamRfiCfgTable": ethernetOamRfiCfgTable,
       "ethernetOamRfiCfgEntry": ethernetOamRfiCfgEntry,
       "ethernetOamRfiCfgPort": ethernetOamRfiCfgPort,
       "ethernetOamRfiCfgDyingGaspNotify": ethernetOamRfiCfgDyingGaspNotify,
       "ethernetOamRfiCfgCriticalEventNotify": ethernetOamRfiCfgCriticalEventNotify,
       "ethernetOamRfiCfgLAG": ethernetOamRfiCfgLAG}
)
