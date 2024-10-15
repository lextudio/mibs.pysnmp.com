# SNMP MIB module (DULD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DULD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:48 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swDULDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 87)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDULDMgmt_ObjectIdentity = ObjectIdentity
swDULDMgmt = _SwDULDMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1)
)
_SwDULDTable_Object = MibTable
swDULDTable = _SwDULDTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1)
)
if mibBuilder.loadTexts:
    swDULDTable.setStatus("current")
_SwDULDEntry_Object = MibTableRow
swDULDEntry = _SwDULDEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1)
)
swDULDEntry.setIndexNames(
    (0, "DULD-MIB", "swDULDPort"),
)
if mibBuilder.loadTexts:
    swDULDEntry.setStatus("current")
_SwDULDPort_Type = Integer32
_SwDULDPort_Object = MibTableColumn
swDULDPort = _SwDULDPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 1),
    _SwDULDPort_Type()
)
swDULDPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDULDPort.setStatus("current")


class _SwDULDAdminState_Type(Integer32):
    """Custom type swDULDAdminState based on Integer32"""
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


_SwDULDAdminState_Type.__name__ = "Integer32"
_SwDULDAdminState_Object = MibTableColumn
swDULDAdminState = _SwDULDAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 2),
    _SwDULDAdminState_Type()
)
swDULDAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDULDAdminState.setStatus("current")


class _SwDULDOperStatus_Type(Integer32):
    """Custom type swDULDOperStatus based on Integer32"""
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


_SwDULDOperStatus_Type.__name__ = "Integer32"
_SwDULDOperStatus_Object = MibTableColumn
swDULDOperStatus = _SwDULDOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 3),
    _SwDULDOperStatus_Type()
)
swDULDOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDULDOperStatus.setStatus("current")


class _SwDULDMode_Type(Integer32):
    """Custom type swDULDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("shutdown", 1))
    )


_SwDULDMode_Type.__name__ = "Integer32"
_SwDULDMode_Object = MibTableColumn
swDULDMode = _SwDULDMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 4),
    _SwDULDMode_Type()
)
swDULDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDULDMode.setStatus("current")


class _SwDULDDiscoveryTime_Type(Integer32):
    """Custom type swDULDDiscoveryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_SwDULDDiscoveryTime_Type.__name__ = "Integer32"
_SwDULDDiscoveryTime_Object = MibTableColumn
swDULDDiscoveryTime = _SwDULDDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 5),
    _SwDULDDiscoveryTime_Type()
)
swDULDDiscoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDULDDiscoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    swDULDDiscoveryTime.setUnits("seconds")


class _SwDULDLinkStatus_Type(Integer32):
    """Custom type swDULDLinkStatus based on Integer32"""
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
        *(("bidirectional", 2),
          ("link-down", 5),
          ("rx-fault", 4),
          ("tx-fault", 3),
          ("unknown", 1))
    )


_SwDULDLinkStatus_Type.__name__ = "Integer32"
_SwDULDLinkStatus_Object = MibTableColumn
swDULDLinkStatus = _SwDULDLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 87, 1, 1, 1, 6),
    _SwDULDLinkStatus_Type()
)
swDULDLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDULDLinkStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DULD-MIB",
    **{"swDULDMIB": swDULDMIB,
       "swDULDMgmt": swDULDMgmt,
       "swDULDTable": swDULDTable,
       "swDULDEntry": swDULDEntry,
       "swDULDPort": swDULDPort,
       "swDULDAdminState": swDULDAdminState,
       "swDULDOperStatus": swDULDOperStatus,
       "swDULDMode": swDULDMode,
       "swDULDDiscoveryTime": swDULDDiscoveryTime,
       "swDULDLinkStatus": swDULDLinkStatus}
)
