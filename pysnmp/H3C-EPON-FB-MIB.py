# SNMP MIB module (H3C-EPON-FB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-EPON-FB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:28 2024
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

(h3cEpon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cEpon")

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

h3cEponFBMibObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEponFBMIB_ObjectIdentity = ObjectIdentity
h3cEponFBMIB = _H3cEponFBMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1)
)
_H3cEponFBMIBTable_Object = MibTable
h3cEponFBMIBTable = _H3cEponFBMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEponFBMIBTable.setStatus("current")
_H3cEponFBMIBEntry_Object = MibTableRow
h3cEponFBMIBEntry = _H3cEponFBMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1)
)
h3cEponFBMIBEntry.setIndexNames(
    (0, "H3C-EPON-FB-MIB", "h3cEponFBGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cEponFBMIBEntry.setStatus("current")
_H3cEponFBGroupIndex_Type = Integer32
_H3cEponFBGroupIndex_Object = MibTableColumn
h3cEponFBGroupIndex = _H3cEponFBGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1, 1),
    _H3cEponFBGroupIndex_Type()
)
h3cEponFBGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponFBGroupIndex.setStatus("current")
_H3cEponFBGroupRowStatus_Type = RowStatus
_H3cEponFBGroupRowStatus_Object = MibTableColumn
h3cEponFBGroupRowStatus = _H3cEponFBGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1, 2),
    _H3cEponFBGroupRowStatus_Type()
)
h3cEponFBGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponFBGroupRowStatus.setStatus("current")
_H3cEponFBMasterPort_Type = Integer32
_H3cEponFBMasterPort_Object = MibTableColumn
h3cEponFBMasterPort = _H3cEponFBMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1, 3),
    _H3cEponFBMasterPort_Type()
)
h3cEponFBMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponFBMasterPort.setStatus("current")
_H3cEponFBSlavePort_Type = Integer32
_H3cEponFBSlavePort_Object = MibTableColumn
h3cEponFBSlavePort = _H3cEponFBSlavePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1, 4),
    _H3cEponFBSlavePort_Type()
)
h3cEponFBSlavePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponFBSlavePort.setStatus("current")


class _H3cEponFBMasterPortStatus_Type(Integer32):
    """Custom type h3cEponFBMasterPortStatus based on Integer32"""
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


_H3cEponFBMasterPortStatus_Type.__name__ = "Integer32"
_H3cEponFBMasterPortStatus_Object = MibTableColumn
h3cEponFBMasterPortStatus = _H3cEponFBMasterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1, 5),
    _H3cEponFBMasterPortStatus_Type()
)
h3cEponFBMasterPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponFBMasterPortStatus.setStatus("current")


class _H3cEponFBSlavePortStatus_Type(Integer32):
    """Custom type h3cEponFBSlavePortStatus based on Integer32"""
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


_H3cEponFBSlavePortStatus_Type.__name__ = "Integer32"
_H3cEponFBSlavePortStatus_Object = MibTableColumn
h3cEponFBSlavePortStatus = _H3cEponFBSlavePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1, 6),
    _H3cEponFBSlavePortStatus_Type()
)
h3cEponFBSlavePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponFBSlavePortStatus.setStatus("current")


class _H3cEponFBSwitchover_Type(Integer32):
    """Custom type h3cEponFBSwitchover based on Integer32"""
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


_H3cEponFBSwitchover_Type.__name__ = "Integer32"
_H3cEponFBSwitchover_Object = MibTableColumn
h3cEponFBSwitchover = _H3cEponFBSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 42, 6, 1, 1, 1, 7),
    _H3cEponFBSwitchover_Type()
)
h3cEponFBSwitchover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponFBSwitchover.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-EPON-FB-MIB",
    **{"h3cEponFBMibObjects": h3cEponFBMibObjects,
       "h3cEponFBMIB": h3cEponFBMIB,
       "h3cEponFBMIBTable": h3cEponFBMIBTable,
       "h3cEponFBMIBEntry": h3cEponFBMIBEntry,
       "h3cEponFBGroupIndex": h3cEponFBGroupIndex,
       "h3cEponFBGroupRowStatus": h3cEponFBGroupRowStatus,
       "h3cEponFBMasterPort": h3cEponFBMasterPort,
       "h3cEponFBSlavePort": h3cEponFBSlavePort,
       "h3cEponFBMasterPortStatus": h3cEponFBMasterPortStatus,
       "h3cEponFBSlavePortStatus": h3cEponFBSlavePortStatus,
       "h3cEponFBSwitchover": h3cEponFBSwitchover}
)
