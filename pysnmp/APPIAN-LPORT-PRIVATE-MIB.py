# SNMP MIB module (APPIAN-LPORT-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-LPORT-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:36 2024
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

(AcNodeId,
 AcOpStatus,
 acLport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcNodeId",
    "AcOpStatus",
    "acLport")

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

acLportPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcLportTable_Object = MibTable
acLportTable = _AcLportTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    acLportTable.setStatus("current")
_AcLportEntry_Object = MibTableRow
acLportEntry = _AcLportEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 1, 1, 1)
)
acLportEntry.setIndexNames(
    (0, "APPIAN-LPORT-PRIVATE-MIB", "acLportNodeId"),
    (0, "APPIAN-LPORT-PRIVATE-MIB", "acLportIndex"),
)
if mibBuilder.loadTexts:
    acLportEntry.setStatus("current")
_AcLportNodeId_Type = AcNodeId
_AcLportNodeId_Object = MibTableColumn
acLportNodeId = _AcLportNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 1, 1, 1, 1),
    _AcLportNodeId_Type()
)
acLportNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLportNodeId.setStatus("current")
_AcLportIndex_Type = Integer32
_AcLportIndex_Object = MibTableColumn
acLportIndex = _AcLportIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 1, 1, 1, 2),
    _AcLportIndex_Type()
)
acLportIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLportIndex.setStatus("current")
_AcLportOpStatus_Type = AcOpStatus
_AcLportOpStatus_Object = MibTableColumn
acLportOpStatus = _AcLportOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 1, 1, 1, 3),
    _AcLportOpStatus_Type()
)
acLportOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLportOpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-LPORT-PRIVATE-MIB",
    **{"acLportPrivate": acLportPrivate,
       "acLportTable": acLportTable,
       "acLportEntry": acLportEntry,
       "acLportNodeId": acLportNodeId,
       "acLportIndex": acLportIndex,
       "acLportOpStatus": acLportOpStatus}
)
