# SNMP MIB module (DGS3000-28SC-LED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS3000-28SC-LED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:20 2024
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

(dlink_Dgs3000Proj_DGS3000_28SCax,) = mibBuilder.importSymbols(
    "SWDGS3000PRIMGMT-MIB",
    "dlink-Dgs3000Proj-DGS3000-28SCax")


# MODULE-IDENTITY

swLedMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwLedMIBObject_ObjectIdentity = ObjectIdentity
swLedMIBObject = _SwLedMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1)
)
_SwLedInfoTable_Object = MibTable
swLedInfoTable = _SwLedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    swLedInfoTable.setStatus("current")
_SwLedInfoEntry_Object = MibTableRow
swLedInfoEntry = _SwLedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1, 1)
)
swLedInfoEntry.setIndexNames(
    (0, "DGS3000-28SC-LED-MIB", "swLedInfoUnitId"),
)
if mibBuilder.loadTexts:
    swLedInfoEntry.setStatus("current")


class _SwLedInfoUnitId_Type(Integer32):
    """Custom type swLedInfoUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_SwLedInfoUnitId_Type.__name__ = "Integer32"
_SwLedInfoUnitId_Object = MibTableColumn
swLedInfoUnitId = _SwLedInfoUnitId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1, 1, 1),
    _SwLedInfoUnitId_Type()
)
swLedInfoUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLedInfoUnitId.setStatus("current")
_SwLedInfoFrontPanelLedStatus_Type = OctetString
_SwLedInfoFrontPanelLedStatus_Object = MibTableColumn
swLedInfoFrontPanelLedStatus = _SwLedInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 133, 5, 1, 4, 1, 1, 1, 2),
    _SwLedInfoFrontPanelLedStatus_Type()
)
swLedInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLedInfoFrontPanelLedStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS3000-28SC-LED-MIB",
    **{"swLedMIB": swLedMIB,
       "swLedMIBObject": swLedMIBObject,
       "swLedInfoTable": swLedInfoTable,
       "swLedInfoEntry": swLedInfoEntry,
       "swLedInfoUnitId": swLedInfoUnitId,
       "swLedInfoFrontPanelLedStatus": swLedInfoFrontPanelLedStatus}
)
