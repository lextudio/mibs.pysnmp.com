# SNMP MIB module (XEDIA-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:49 2024
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

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xdvmrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XdvmrpMIBObjects_ObjectIdentity = ObjectIdentity
xdvmrpMIBObjects = _XdvmrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1)
)
_Xdvmrp_ObjectIdentity = ObjectIdentity
xdvmrp = _Xdvmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1, 1)
)
_XdvmrpInterfaceTable_Object = MibTable
xdvmrpInterfaceTable = _XdvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xdvmrpInterfaceTable.setStatus("current")
_XdvmrpInterfaceEntry_Object = MibTableRow
xdvmrpInterfaceEntry = _XdvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1, 1, 1, 1)
)
xdvmrpInterfaceEntry.setIndexNames(
    (0, "XEDIA-DVMRP-MIB", "xdvmrpInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    xdvmrpInterfaceEntry.setStatus("current")
_XdvmrpInterfaceIfIndex_Type = Integer32
_XdvmrpInterfaceIfIndex_Object = MibTableColumn
xdvmrpInterfaceIfIndex = _XdvmrpInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1, 1, 1, 1, 1),
    _XdvmrpInterfaceIfIndex_Type()
)
xdvmrpInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdvmrpInterfaceIfIndex.setStatus("current")


class _XdvmrpInterfaceState_Type(Integer32):
    """Custom type xdvmrpInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XdvmrpInterfaceState_Type.__name__ = "Integer32"
_XdvmrpInterfaceState_Object = MibTableColumn
xdvmrpInterfaceState = _XdvmrpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1, 1, 1, 1, 2),
    _XdvmrpInterfaceState_Type()
)
xdvmrpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdvmrpInterfaceState.setStatus("current")


class _XdvmrpInterfaceDefaultInformation_Type(Integer32):
    """Custom type xdvmrpInterfaceDefaultInformation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("only", 3),
          ("originate", 2))
    )


_XdvmrpInterfaceDefaultInformation_Type.__name__ = "Integer32"
_XdvmrpInterfaceDefaultInformation_Object = MibTableColumn
xdvmrpInterfaceDefaultInformation = _XdvmrpInterfaceDefaultInformation_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1, 1, 1, 1, 3),
    _XdvmrpInterfaceDefaultInformation_Type()
)
xdvmrpInterfaceDefaultInformation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdvmrpInterfaceDefaultInformation.setStatus("current")


class _XdvmrpInterfaceUnicastTunnel_Type(Integer32):
    """Custom type xdvmrpInterfaceUnicastTunnel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_XdvmrpInterfaceUnicastTunnel_Type.__name__ = "Integer32"
_XdvmrpInterfaceUnicastTunnel_Object = MibTableColumn
xdvmrpInterfaceUnicastTunnel = _XdvmrpInterfaceUnicastTunnel_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 32, 1, 1, 1, 1, 4),
    _XdvmrpInterfaceUnicastTunnel_Type()
)
xdvmrpInterfaceUnicastTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdvmrpInterfaceUnicastTunnel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-DVMRP-MIB",
    **{"xdvmrpMIB": xdvmrpMIB,
       "xdvmrpMIBObjects": xdvmrpMIBObjects,
       "xdvmrp": xdvmrp,
       "xdvmrpInterfaceTable": xdvmrpInterfaceTable,
       "xdvmrpInterfaceEntry": xdvmrpInterfaceEntry,
       "xdvmrpInterfaceIfIndex": xdvmrpInterfaceIfIndex,
       "xdvmrpInterfaceState": xdvmrpInterfaceState,
       "xdvmrpInterfaceDefaultInformation": xdvmrpInterfaceDefaultInformation,
       "xdvmrpInterfaceUnicastTunnel": xdvmrpInterfaceUnicastTunnel}
)
