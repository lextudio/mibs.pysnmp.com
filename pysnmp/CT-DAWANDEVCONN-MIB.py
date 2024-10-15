# SNMP MIB module (CT-DAWANDEVCONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-DAWANDEVCONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:05 2024
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

(cabletron,) = mibBuilder.importSymbols(
    "CTRON-OIDS",
    "cabletron")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtSSA_ObjectIdentity = ObjectIdentity
ctSSA = _CtSSA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497)
)
_DaWanDevConn_ObjectIdentity = ObjectIdentity
daWanDevConn = _DaWanDevConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4497, 23)
)
_DaWanDevConnTable_Object = MibTable
daWanDevConnTable = _DaWanDevConnTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 23, 1)
)
if mibBuilder.loadTexts:
    daWanDevConnTable.setStatus("mandatory")
_DaWanDevConnEntry_Object = MibTableRow
daWanDevConnEntry = _DaWanDevConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1)
)
daWanDevConnEntry.setIndexNames(
    (0, "CT-DAWANDEVCONN-MIB", "daWanDeviceIndex"),
    (0, "CT-DAWANDEVCONN-MIB", "daWanConnectionIndex"),
)
if mibBuilder.loadTexts:
    daWanDevConnEntry.setStatus("mandatory")


class _DaWanDeviceIndex_Type(Integer32):
    """Custom type daWanDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DaWanDeviceIndex_Type.__name__ = "Integer32"
_DaWanDeviceIndex_Object = MibTableColumn
daWanDeviceIndex = _DaWanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 1),
    _DaWanDeviceIndex_Type()
)
daWanDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanDeviceIndex.setStatus("mandatory")


class _DaWanConnectionIndex_Type(Integer32):
    """Custom type daWanConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DaWanConnectionIndex_Type.__name__ = "Integer32"
_DaWanConnectionIndex_Object = MibTableColumn
daWanConnectionIndex = _DaWanConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 2),
    _DaWanConnectionIndex_Type()
)
daWanConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daWanConnectionIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-DAWANDEVCONN-MIB",
    **{"ctSSA": ctSSA,
       "daWanDevConn": daWanDevConn,
       "daWanDevConnTable": daWanDevConnTable,
       "daWanDevConnEntry": daWanDevConnEntry,
       "daWanDeviceIndex": daWanDeviceIndex,
       "daWanConnectionIndex": daWanConnectionIndex}
)
