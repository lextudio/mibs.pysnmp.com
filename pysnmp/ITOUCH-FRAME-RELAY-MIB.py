# SNMP MIB module (ITOUCH-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:12 2024
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

(iTouch,) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "iTouch")

(frCircuitDlci,
 frCircuitIfIndex) = mibBuilder.importSymbols(
    "RFC1315-MIB",
    "frCircuitDlci",
    "frCircuitIfIndex")

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

_XFrameRelay_ObjectIdentity = ObjectIdentity
xFrameRelay = _XFrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 23)
)
_XFrCircuitTable_Object = MibTable
xFrCircuitTable = _XFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 23, 1)
)
if mibBuilder.loadTexts:
    xFrCircuitTable.setStatus("mandatory")
_XFrCircuitEntry_Object = MibTableRow
xFrCircuitEntry = _XFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 23, 1, 1)
)
xFrCircuitEntry.setIndexNames(
    (0, "RFC1315-MIB", "frCircuitIfIndex"),
    (0, "RFC1315-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    xFrCircuitEntry.setStatus("mandatory")
_XFrCircuitIf_Type = Integer32
_XFrCircuitIf_Object = MibTableColumn
xFrCircuitIf = _XFrCircuitIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 23, 1, 1, 1),
    _XFrCircuitIf_Type()
)
xFrCircuitIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xFrCircuitIf.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-FRAME-RELAY-MIB",
    **{"xFrameRelay": xFrameRelay,
       "xFrCircuitTable": xFrCircuitTable,
       "xFrCircuitEntry": xFrCircuitEntry,
       "xFrCircuitIf": xFrCircuitIf}
)
