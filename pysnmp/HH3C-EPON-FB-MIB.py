# SNMP MIB module (HH3C-EPON-FB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EPON-FB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:08 2024
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

(hh3cEpon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cEpon")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cEponFBMibObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEponFBMIB_ObjectIdentity = ObjectIdentity
hh3cEponFBMIB = _Hh3cEponFBMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1)
)
_Hh3cEponFBMIBTable_Object = MibTable
hh3cEponFBMIBTable = _Hh3cEponFBMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEponFBMIBTable.setStatus("current")
_Hh3cEponFBMIBEntry_Object = MibTableRow
hh3cEponFBMIBEntry = _Hh3cEponFBMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1)
)
hh3cEponFBMIBEntry.setIndexNames(
    (0, "HH3C-EPON-FB-MIB", "hh3cEponFBGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponFBMIBEntry.setStatus("current")
_Hh3cEponFBGroupIndex_Type = Integer32
_Hh3cEponFBGroupIndex_Object = MibTableColumn
hh3cEponFBGroupIndex = _Hh3cEponFBGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1, 1),
    _Hh3cEponFBGroupIndex_Type()
)
hh3cEponFBGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponFBGroupIndex.setStatus("current")
_Hh3cEponFBGroupRowStatus_Type = RowStatus
_Hh3cEponFBGroupRowStatus_Object = MibTableColumn
hh3cEponFBGroupRowStatus = _Hh3cEponFBGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1, 2),
    _Hh3cEponFBGroupRowStatus_Type()
)
hh3cEponFBGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponFBGroupRowStatus.setStatus("current")
_Hh3cEponFBMasterPort_Type = Integer32
_Hh3cEponFBMasterPort_Object = MibTableColumn
hh3cEponFBMasterPort = _Hh3cEponFBMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1, 3),
    _Hh3cEponFBMasterPort_Type()
)
hh3cEponFBMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponFBMasterPort.setStatus("current")
_Hh3cEponFBSlavePort_Type = Integer32
_Hh3cEponFBSlavePort_Object = MibTableColumn
hh3cEponFBSlavePort = _Hh3cEponFBSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1, 4),
    _Hh3cEponFBSlavePort_Type()
)
hh3cEponFBSlavePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponFBSlavePort.setStatus("current")


class _Hh3cEponFBMasterPortStatus_Type(Integer32):
    """Custom type hh3cEponFBMasterPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 2))
    )


_Hh3cEponFBMasterPortStatus_Type.__name__ = "Integer32"
_Hh3cEponFBMasterPortStatus_Object = MibTableColumn
hh3cEponFBMasterPortStatus = _Hh3cEponFBMasterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1, 5),
    _Hh3cEponFBMasterPortStatus_Type()
)
hh3cEponFBMasterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponFBMasterPortStatus.setStatus("current")


class _Hh3cEponFBSlavePortStatus_Type(Integer32):
    """Custom type hh3cEponFBSlavePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("ready", 1))
    )


_Hh3cEponFBSlavePortStatus_Type.__name__ = "Integer32"
_Hh3cEponFBSlavePortStatus_Object = MibTableColumn
hh3cEponFBSlavePortStatus = _Hh3cEponFBSlavePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1, 6),
    _Hh3cEponFBSlavePortStatus_Type()
)
hh3cEponFBSlavePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponFBSlavePortStatus.setStatus("current")


class _Hh3cEponFBSwitchover_Type(Integer32):
    """Custom type hh3cEponFBSwitchover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Hh3cEponFBSwitchover_Type.__name__ = "Integer32"
_Hh3cEponFBSwitchover_Object = MibTableColumn
hh3cEponFBSwitchover = _Hh3cEponFBSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 6, 1, 1, 1, 7),
    _Hh3cEponFBSwitchover_Type()
)
hh3cEponFBSwitchover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponFBSwitchover.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EPON-FB-MIB",
    **{"hh3cEponFBMibObjects": hh3cEponFBMibObjects,
       "hh3cEponFBMIB": hh3cEponFBMIB,
       "hh3cEponFBMIBTable": hh3cEponFBMIBTable,
       "hh3cEponFBMIBEntry": hh3cEponFBMIBEntry,
       "hh3cEponFBGroupIndex": hh3cEponFBGroupIndex,
       "hh3cEponFBGroupRowStatus": hh3cEponFBGroupRowStatus,
       "hh3cEponFBMasterPort": hh3cEponFBMasterPort,
       "hh3cEponFBSlavePort": hh3cEponFBSlavePort,
       "hh3cEponFBMasterPortStatus": hh3cEponFBMasterPortStatus,
       "hh3cEponFBSlavePortStatus": hh3cEponFBSlavePortStatus,
       "hh3cEponFBSwitchover": hh3cEponFBSwitchover}
)
