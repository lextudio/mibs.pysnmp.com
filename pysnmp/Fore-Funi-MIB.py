# SNMP MIB module (Fore-Funi-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Funi-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:01 2024
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

(frameInternetworking,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "frameInternetworking")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

funi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FuniConnTable_Object = MibTable
funiConnTable = _FuniConnTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1)
)
if mibBuilder.loadTexts:
    funiConnTable.setStatus("current")
_FuniConnEntry_Object = MibTableRow
funiConnEntry = _FuniConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1)
)
funiConnEntry.setIndexNames(
    (0, "Fore-Funi-MIB", "funiConnFuniServiceIfIndex"),
    (0, "Fore-Funi-MIB", "funiConnFuniVpi"),
    (0, "Fore-Funi-MIB", "funiConnFuniVci"),
)
if mibBuilder.loadTexts:
    funiConnEntry.setStatus("current")
_FuniConnFuniServiceIfIndex_Type = Integer32
_FuniConnFuniServiceIfIndex_Object = MibTableColumn
funiConnFuniServiceIfIndex = _FuniConnFuniServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 1),
    _FuniConnFuniServiceIfIndex_Type()
)
funiConnFuniServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiConnFuniServiceIfIndex.setStatus("current")
_FuniConnFuniVpi_Type = Integer32
_FuniConnFuniVpi_Object = MibTableColumn
funiConnFuniVpi = _FuniConnFuniVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 2),
    _FuniConnFuniVpi_Type()
)
funiConnFuniVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiConnFuniVpi.setStatus("current")
_FuniConnFuniVci_Type = Integer32
_FuniConnFuniVci_Object = MibTableColumn
funiConnFuniVci = _FuniConnFuniVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 3),
    _FuniConnFuniVci_Type()
)
funiConnFuniVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiConnFuniVci.setStatus("current")
_FuniConnFabricServiceIfIndex_Type = Integer32
_FuniConnFabricServiceIfIndex_Object = MibTableColumn
funiConnFabricServiceIfIndex = _FuniConnFabricServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 4),
    _FuniConnFabricServiceIfIndex_Type()
)
funiConnFabricServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiConnFabricServiceIfIndex.setStatus("current")
_FuniConnFabricVpi_Type = Integer32
_FuniConnFabricVpi_Object = MibTableColumn
funiConnFabricVpi = _FuniConnFabricVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 5),
    _FuniConnFabricVpi_Type()
)
funiConnFabricVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiConnFabricVpi.setStatus("current")
_FuniConnFabricVci_Type = Integer32
_FuniConnFabricVci_Object = MibTableColumn
funiConnFabricVci = _FuniConnFabricVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 6),
    _FuniConnFabricVci_Type()
)
funiConnFabricVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiConnFabricVci.setStatus("current")
_FuniConnRowStatus_Type = RowStatus
_FuniConnRowStatus_Object = MibTableColumn
funiConnRowStatus = _FuniConnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 7),
    _FuniConnRowStatus_Type()
)
funiConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    funiConnRowStatus.setStatus("current")
_FuniConnName_Type = DisplayString
_FuniConnName_Object = MibTableColumn
funiConnName = _FuniConnName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 8),
    _FuniConnName_Type()
)
funiConnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    funiConnName.setStatus("current")


class _FuniConnAdminStatus_Type(Integer32):
    """Custom type funiConnAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_FuniConnAdminStatus_Type.__name__ = "Integer32"
_FuniConnAdminStatus_Object = MibTableColumn
funiConnAdminStatus = _FuniConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 9),
    _FuniConnAdminStatus_Type()
)
funiConnAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    funiConnAdminStatus.setStatus("current")


class _FuniConnOperStatus_Type(Integer32):
    """Custom type funiConnOperStatus based on Integer32"""
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


_FuniConnOperStatus_Type.__name__ = "Integer32"
_FuniConnOperStatus_Object = MibTableColumn
funiConnOperStatus = _FuniConnOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 10),
    _FuniConnOperStatus_Type()
)
funiConnOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiConnOperStatus.setStatus("current")


class _FuniConnProfileEpdPpdIndex_Type(Integer32):
    """Custom type funiConnProfileEpdPpdIndex based on Integer32"""
    defaultValue = 0


_FuniConnProfileEpdPpdIndex_Object = MibTableColumn
funiConnProfileEpdPpdIndex = _FuniConnProfileEpdPpdIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 1, 1, 11),
    _FuniConnProfileEpdPpdIndex_Type()
)
funiConnProfileEpdPpdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    funiConnProfileEpdPpdIndex.setStatus("current")
_FuniIfExtTable_Object = MibTable
funiIfExtTable = _FuniIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2)
)
if mibBuilder.loadTexts:
    funiIfExtTable.setStatus("current")
_FuniIfExtEntry_Object = MibTableRow
funiIfExtEntry = _FuniIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1)
)
funiIfExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    funiIfExtEntry.setStatus("current")
_FuniIfExtProfileFuniIndex_Type = Integer32
_FuniIfExtProfileFuniIndex_Object = MibTableColumn
funiIfExtProfileFuniIndex = _FuniIfExtProfileFuniIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 1),
    _FuniIfExtProfileFuniIndex_Type()
)
funiIfExtProfileFuniIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfExtProfileFuniIndex.setStatus("current")
_FuniIfExtProfileServiceIndex_Type = Integer32
_FuniIfExtProfileServiceIndex_Object = MibTableColumn
funiIfExtProfileServiceIndex = _FuniIfExtProfileServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 2),
    _FuniIfExtProfileServiceIndex_Type()
)
funiIfExtProfileServiceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfExtProfileServiceIndex.setStatus("current")


class _FuniIfExtStatsMonitor_Type(Integer32):
    """Custom type funiIfExtStatsMonitor based on Integer32"""
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


_FuniIfExtStatsMonitor_Type.__name__ = "Integer32"
_FuniIfExtStatsMonitor_Object = MibTableColumn
funiIfExtStatsMonitor = _FuniIfExtStatsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 3),
    _FuniIfExtStatsMonitor_Type()
)
funiIfExtStatsMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfExtStatsMonitor.setStatus("current")
_FuniIfExtNeighborIpAddress_Type = IpAddress
_FuniIfExtNeighborIpAddress_Object = MibTableColumn
funiIfExtNeighborIpAddress = _FuniIfExtNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 4),
    _FuniIfExtNeighborIpAddress_Type()
)
funiIfExtNeighborIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    funiIfExtNeighborIpAddress.setStatus("current")
_FuniIfExtStatsEnabledTimeStamp_Type = TimeTicks
_FuniIfExtStatsEnabledTimeStamp_Object = MibTableColumn
funiIfExtStatsEnabledTimeStamp = _FuniIfExtStatsEnabledTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 5),
    _FuniIfExtStatsEnabledTimeStamp_Type()
)
funiIfExtStatsEnabledTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfExtStatsEnabledTimeStamp.setStatus("current")


class _FuniIfExtSigStatus_Type(Integer32):
    """Custom type funiIfExtSigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("nonexist", 2))
    )


_FuniIfExtSigStatus_Type.__name__ = "Integer32"
_FuniIfExtSigStatus_Object = MibTableColumn
funiIfExtSigStatus = _FuniIfExtSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 6, 2, 1, 6),
    _FuniIfExtSigStatus_Type()
)
funiIfExtSigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    funiIfExtSigStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Funi-MIB",
    **{"funi": funi,
       "funiConnTable": funiConnTable,
       "funiConnEntry": funiConnEntry,
       "funiConnFuniServiceIfIndex": funiConnFuniServiceIfIndex,
       "funiConnFuniVpi": funiConnFuniVpi,
       "funiConnFuniVci": funiConnFuniVci,
       "funiConnFabricServiceIfIndex": funiConnFabricServiceIfIndex,
       "funiConnFabricVpi": funiConnFabricVpi,
       "funiConnFabricVci": funiConnFabricVci,
       "funiConnRowStatus": funiConnRowStatus,
       "funiConnName": funiConnName,
       "funiConnAdminStatus": funiConnAdminStatus,
       "funiConnOperStatus": funiConnOperStatus,
       "funiConnProfileEpdPpdIndex": funiConnProfileEpdPpdIndex,
       "funiIfExtTable": funiIfExtTable,
       "funiIfExtEntry": funiIfExtEntry,
       "funiIfExtProfileFuniIndex": funiIfExtProfileFuniIndex,
       "funiIfExtProfileServiceIndex": funiIfExtProfileServiceIndex,
       "funiIfExtStatsMonitor": funiIfExtStatsMonitor,
       "funiIfExtNeighborIpAddress": funiIfExtNeighborIpAddress,
       "funiIfExtStatsEnabledTimeStamp": funiIfExtStatsEnabledTimeStamp,
       "funiIfExtSigStatus": funiIfExtSigStatus}
)
