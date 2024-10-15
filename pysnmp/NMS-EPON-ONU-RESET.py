# SNMP MIB module (NMS-EPON-ONU-RESET) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-ONU-RESET
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:51 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

_NmsEponOnuReset_ObjectIdentity = ObjectIdentity
nmsEponOnuReset = _NmsEponOnuReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 25)
)
_NmsEponOnuResetTable_Object = MibTable
nmsEponOnuResetTable = _NmsEponOnuResetTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1)
)
if mibBuilder.loadTexts:
    nmsEponOnuResetTable.setStatus("mandatory")
_NmsEponOnuResetEntry_Object = MibTableRow
nmsEponOnuResetEntry = _NmsEponOnuResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1)
)
nmsEponOnuResetEntry.setIndexNames(
    (0, "NMS-EPON-ONU-RESET", "onuLlid"),
)
if mibBuilder.loadTexts:
    nmsEponOnuResetEntry.setStatus("mandatory")
_OnuLlid_Type = Integer32
_OnuLlid_Object = MibTableColumn
onuLlid = _OnuLlid_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1, 1),
    _OnuLlid_Type()
)
onuLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLlid.setStatus("mandatory")


class _OnuReset_Type(Integer32):
    """Custom type onuReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no_action", 0),
          ("reset", 1))
    )


_OnuReset_Type.__name__ = "Integer32"
_OnuReset_Object = MibTableColumn
onuReset = _OnuReset_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 25, 1, 1, 2),
    _OnuReset_Type()
)
onuReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    onuReset.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-ONU-RESET",
    **{"nmsEponOnuReset": nmsEponOnuReset,
       "nmsEponOnuResetTable": nmsEponOnuResetTable,
       "nmsEponOnuResetEntry": nmsEponOnuResetEntry,
       "onuLlid": onuLlid,
       "onuReset": onuReset}
)
