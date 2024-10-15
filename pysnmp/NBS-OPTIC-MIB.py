# SNMP MIB module (NBS-OPTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-OPTIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:54 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsOpticMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 213)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsOpticPortGrp_ObjectIdentity = ObjectIdentity
nbsOpticPortGrp = _NbsOpticPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 213, 1)
)
if mibBuilder.loadTexts:
    nbsOpticPortGrp.setStatus("current")
_NbsOpticPortTableSize_Type = Integer32
_NbsOpticPortTableSize_Object = MibScalar
nbsOpticPortTableSize = _NbsOpticPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 1),
    _NbsOpticPortTableSize_Type()
)
nbsOpticPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOpticPortTableSize.setStatus("current")
_NbsOpticPortTable_Object = MibTable
nbsOpticPortTable = _NbsOpticPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2)
)
if mibBuilder.loadTexts:
    nbsOpticPortTable.setStatus("current")
_NbsOpticPortEntry_Object = MibTableRow
nbsOpticPortEntry = _NbsOpticPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1)
)
nbsOpticPortEntry.setIndexNames(
    (0, "NBS-OPTIC-MIB", "nbsOpticPortNdx"),
)
if mibBuilder.loadTexts:
    nbsOpticPortEntry.setStatus("current")
_NbsOpticPortNdx_Type = InterfaceIndex
_NbsOpticPortNdx_Object = MibTableColumn
nbsOpticPortNdx = _NbsOpticPortNdx_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 1),
    _NbsOpticPortNdx_Type()
)
nbsOpticPortNdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOpticPortNdx.setStatus("current")


class _NbsOpticPortTxStatusAdmin_Type(Integer32):
    """Custom type nbsOpticPortTxStatusAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 3),
          ("notSupported", 1),
          ("outOfService", 2))
    )


_NbsOpticPortTxStatusAdmin_Type.__name__ = "Integer32"
_NbsOpticPortTxStatusAdmin_Object = MibTableColumn
nbsOpticPortTxStatusAdmin = _NbsOpticPortTxStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 21),
    _NbsOpticPortTxStatusAdmin_Type()
)
nbsOpticPortTxStatusAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOpticPortTxStatusAdmin.setStatus("current")


class _NbsOpticPortTxStatusOper_Type(Integer32):
    """Custom type nbsOpticPortTxStatusOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 3),
          ("notSupported", 1),
          ("outOfService", 2))
    )


_NbsOpticPortTxStatusOper_Type.__name__ = "Integer32"
_NbsOpticPortTxStatusOper_Object = MibTableColumn
nbsOpticPortTxStatusOper = _NbsOpticPortTxStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 22),
    _NbsOpticPortTxStatusOper_Type()
)
nbsOpticPortTxStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOpticPortTxStatusOper.setStatus("current")


class _NbsOpticPortRxStatusAdmin_Type(Integer32):
    """Custom type nbsOpticPortRxStatusAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 3),
          ("notSupported", 1),
          ("outOfService", 2))
    )


_NbsOpticPortRxStatusAdmin_Type.__name__ = "Integer32"
_NbsOpticPortRxStatusAdmin_Object = MibTableColumn
nbsOpticPortRxStatusAdmin = _NbsOpticPortRxStatusAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 31),
    _NbsOpticPortRxStatusAdmin_Type()
)
nbsOpticPortRxStatusAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOpticPortRxStatusAdmin.setStatus("current")


class _NbsOpticPortRxStatusOper_Type(Integer32):
    """Custom type nbsOpticPortRxStatusOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 3),
          ("notSupported", 1),
          ("outOfService", 2))
    )


_NbsOpticPortRxStatusOper_Type.__name__ = "Integer32"
_NbsOpticPortRxStatusOper_Object = MibTableColumn
nbsOpticPortRxStatusOper = _NbsOpticPortRxStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 32),
    _NbsOpticPortRxStatusOper_Type()
)
nbsOpticPortRxStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOpticPortRxStatusOper.setStatus("current")
_NbsOpticPortConnector_Type = Integer32
_NbsOpticPortConnector_Object = MibTableColumn
nbsOpticPortConnector = _NbsOpticPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 41),
    _NbsOpticPortConnector_Type()
)
nbsOpticPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOpticPortConnector.setStatus("current")


class _NbsOpticPortPolish_Type(Integer32):
    """Custom type nbsOpticPortPolish based on Integer32"""
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
        *(("apc", 4),
          ("notSupported", 1),
          ("pc", 2),
          ("upc", 3))
    )


_NbsOpticPortPolish_Type.__name__ = "Integer32"
_NbsOpticPortPolish_Object = MibTableColumn
nbsOpticPortPolish = _NbsOpticPortPolish_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 42),
    _NbsOpticPortPolish_Type()
)
nbsOpticPortPolish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOpticPortPolish.setStatus("current")


class _NbsOpticPortFiberMode_Type(Integer32):
    """Custom type nbsOpticPortFiberMode based on Integer32"""
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
        *(("multiMode", 5),
          ("notSupported", 1),
          ("reserved2", 2),
          ("reserved3", 3),
          ("singleMode", 4))
    )


_NbsOpticPortFiberMode_Type.__name__ = "Integer32"
_NbsOpticPortFiberMode_Object = MibTableColumn
nbsOpticPortFiberMode = _NbsOpticPortFiberMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 213, 1, 2, 1, 51),
    _NbsOpticPortFiberMode_Type()
)
nbsOpticPortFiberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOpticPortFiberMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-OPTIC-MIB",
    **{"nbsOpticMib": nbsOpticMib,
       "nbsOpticPortGrp": nbsOpticPortGrp,
       "nbsOpticPortTableSize": nbsOpticPortTableSize,
       "nbsOpticPortTable": nbsOpticPortTable,
       "nbsOpticPortEntry": nbsOpticPortEntry,
       "nbsOpticPortNdx": nbsOpticPortNdx,
       "nbsOpticPortTxStatusAdmin": nbsOpticPortTxStatusAdmin,
       "nbsOpticPortTxStatusOper": nbsOpticPortTxStatusOper,
       "nbsOpticPortRxStatusAdmin": nbsOpticPortRxStatusAdmin,
       "nbsOpticPortRxStatusOper": nbsOpticPortRxStatusOper,
       "nbsOpticPortConnector": nbsOpticPortConnector,
       "nbsOpticPortPolish": nbsOpticPortPolish,
       "nbsOpticPortFiberMode": nbsOpticPortFiberMode}
)
