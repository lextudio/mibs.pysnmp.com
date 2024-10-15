# SNMP MIB module (HUAWEI-8040IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-8040IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:41 2024
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

(mlsr,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "mlsr")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hw8040If = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hw8040IfTable_Object = MibTable
hw8040IfTable = _Hw8040IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1)
)
if mibBuilder.loadTexts:
    hw8040IfTable.setStatus("current")
_Hw8040IfEntry_Object = MibTableRow
hw8040IfEntry = _Hw8040IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1)
)
hw8040IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hw8040IfEntry.setStatus("current")
_Hw8040IfInPerSecBits_Type = Integer32
_Hw8040IfInPerSecBits_Object = MibTableColumn
hw8040IfInPerSecBits = _Hw8040IfInPerSecBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 1),
    _Hw8040IfInPerSecBits_Type()
)
hw8040IfInPerSecBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8040IfInPerSecBits.setStatus("current")
_Hw8040IfOutPerSecBits_Type = Integer32
_Hw8040IfOutPerSecBits_Object = MibTableColumn
hw8040IfOutPerSecBits = _Hw8040IfOutPerSecBits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 2),
    _Hw8040IfOutPerSecBits_Type()
)
hw8040IfOutPerSecBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8040IfOutPerSecBits.setStatus("current")
_Hw8040CRCIfInputErr_Type = Integer32
_Hw8040CRCIfInputErr_Object = MibTableColumn
hw8040CRCIfInputErr = _Hw8040CRCIfInputErr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 3),
    _Hw8040CRCIfInputErr_Type()
)
hw8040CRCIfInputErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8040CRCIfInputErr.setStatus("current")
_Hw8040IfOutCollisions_Type = Integer32
_Hw8040IfOutCollisions_Object = MibTableColumn
hw8040IfOutCollisions = _Hw8040IfOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 4),
    _Hw8040IfOutCollisions_Type()
)
hw8040IfOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hw8040IfOutCollisions.setStatus("current")


class _Hw8040IfDescCfg_Type(DisplayString):
    """Custom type hw8040IfDescCfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hw8040IfDescCfg_Type.__name__ = "DisplayString"
_Hw8040IfDescCfg_Object = MibTableColumn
hw8040IfDescCfg = _Hw8040IfDescCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 7, 1, 1, 5),
    _Hw8040IfDescCfg_Type()
)
hw8040IfDescCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hw8040IfDescCfg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-8040IF-MIB",
    **{"hw8040If": hw8040If,
       "hw8040IfTable": hw8040IfTable,
       "hw8040IfEntry": hw8040IfEntry,
       "hw8040IfInPerSecBits": hw8040IfInPerSecBits,
       "hw8040IfOutPerSecBits": hw8040IfOutPerSecBits,
       "hw8040CRCIfInputErr": hw8040CRCIfInputErr,
       "hw8040IfOutCollisions": hw8040IfOutCollisions,
       "hw8040IfDescCfg": hw8040IfDescCfg}
)
