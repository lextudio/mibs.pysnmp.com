# SNMP MIB module (PVC-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PVC-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:02 2024
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

(frCircuitDlci,
 frCircuitIfIndex) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "frCircuitDlci",
    "frCircuitIfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pgainDSLAM,) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgainDSLAM")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pgService = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6)
)


# Types definitions



class PgPvcServiceType(Integer32):
    """Custom type PgPvcServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 5),
          ("ipoa", 2),
          ("lant", 3),
          ("null", 6),
          ("other", 1),
          ("ppp", 4),
          ("ramp1483", 7))
    )





class PgXdslFrameType(Integer32):
    """Custom type PgXdslFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 2),
          ("other", 1))
    )





class PgPvcServiceEncapType(Integer32):
    """Custom type PgPvcServiceEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("llc-8023", 8),
          ("llc-8023-crc", 7),
          ("llc-ip", 6),
          ("llc-iso", 5),
          ("llc-ppp", 10),
          ("other", 1),
          ("vc-mux-8023", 4),
          ("vc-mux-ip", 3),
          ("vc-mux-iso", 2),
          ("vc-mux-ppp", 9),
          ("vc-mux-ramp1483", 11))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgServiceObjects_ObjectIdentity = ObjectIdentity
pgServiceObjects = _PgServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1)
)
_PgXdslServiceTable_Object = MibTable
pgXdslServiceTable = _PgXdslServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1)
)
if mibBuilder.loadTexts:
    pgXdslServiceTable.setStatus("current")
_PgXdslServiceEntry_Object = MibTableRow
pgXdslServiceEntry = _PgXdslServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1)
)
pgXdslServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgXdslServiceEntry.setStatus("current")


class _PgXdslServiceSubscriberName_Type(DisplayString):
    """Custom type pgXdslServiceSubscriberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PgXdslServiceSubscriberName_Type.__name__ = "DisplayString"
_PgXdslServiceSubscriberName_Object = MibTableColumn
pgXdslServiceSubscriberName = _PgXdslServiceSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 1),
    _PgXdslServiceSubscriberName_Type()
)
pgXdslServiceSubscriberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgXdslServiceSubscriberName.setStatus("current")
_PgXdslServiceType_Type = PgPvcServiceType
_PgXdslServiceType_Object = MibTableColumn
pgXdslServiceType = _PgXdslServiceType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 2),
    _PgXdslServiceType_Type()
)
pgXdslServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgXdslServiceType.setStatus("current")
_PgXdslServiceMacAddress_Type = MacAddress
_PgXdslServiceMacAddress_Object = MibTableColumn
pgXdslServiceMacAddress = _PgXdslServiceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 3),
    _PgXdslServiceMacAddress_Type()
)
pgXdslServiceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgXdslServiceMacAddress.setStatus("current")
_PgXdslServiceIpAddress_Type = IpAddress
_PgXdslServiceIpAddress_Object = MibTableColumn
pgXdslServiceIpAddress = _PgXdslServiceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 4),
    _PgXdslServiceIpAddress_Type()
)
pgXdslServiceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgXdslServiceIpAddress.setStatus("current")
_PgXdslServiceSubnetMask_Type = IpAddress
_PgXdslServiceSubnetMask_Object = MibTableColumn
pgXdslServiceSubnetMask = _PgXdslServiceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 5),
    _PgXdslServiceSubnetMask_Type()
)
pgXdslServiceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgXdslServiceSubnetMask.setStatus("current")
_PgXdslServiceRowStatus_Type = RowStatus
_PgXdslServiceRowStatus_Object = MibTableColumn
pgXdslServiceRowStatus = _PgXdslServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 1, 1, 6),
    _PgXdslServiceRowStatus_Type()
)
pgXdslServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgXdslServiceRowStatus.setStatus("current")
_PgPvcServiceTable_Object = MibTable
pgPvcServiceTable = _PgPvcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2)
)
if mibBuilder.loadTexts:
    pgPvcServiceTable.setStatus("current")
_PgPvcServiceEntry_Object = MibTableRow
pgPvcServiceEntry = _PgPvcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1)
)
pgPvcServiceEntry.setIndexNames(
    (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVpi"),
    (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVci"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgPvcServiceEntry.setStatus("current")


class _PgPvcServiceSarVpi_Type(Integer32):
    """Custom type pgPvcServiceSarVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgPvcServiceSarVpi_Type.__name__ = "Integer32"
_PgPvcServiceSarVpi_Object = MibTableColumn
pgPvcServiceSarVpi = _PgPvcServiceSarVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 1),
    _PgPvcServiceSarVpi_Type()
)
pgPvcServiceSarVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgPvcServiceSarVpi.setStatus("current")


class _PgPvcServiceSarVci_Type(Integer32):
    """Custom type pgPvcServiceSarVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgPvcServiceSarVci_Type.__name__ = "Integer32"
_PgPvcServiceSarVci_Object = MibTableColumn
pgPvcServiceSarVci = _PgPvcServiceSarVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 2),
    _PgPvcServiceSarVci_Type()
)
pgPvcServiceSarVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgPvcServiceSarVci.setStatus("current")
_PgPvcServiceIpAddress_Type = IpAddress
_PgPvcServiceIpAddress_Object = MibTableColumn
pgPvcServiceIpAddress = _PgPvcServiceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 3),
    _PgPvcServiceIpAddress_Type()
)
pgPvcServiceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgPvcServiceIpAddress.setStatus("deprecated")
_PgPvcServiceSubnetMask_Type = IpAddress
_PgPvcServiceSubnetMask_Object = MibTableColumn
pgPvcServiceSubnetMask = _PgPvcServiceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 4),
    _PgPvcServiceSubnetMask_Type()
)
pgPvcServiceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgPvcServiceSubnetMask.setStatus("deprecated")
_PgPvcServiceEncapType_Type = PgPvcServiceEncapType
_PgPvcServiceEncapType_Object = MibTableColumn
pgPvcServiceEncapType = _PgPvcServiceEncapType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 5),
    _PgPvcServiceEncapType_Type()
)
pgPvcServiceEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgPvcServiceEncapType.setStatus("deprecated")
_PgPvcServiceRowStatus_Type = RowStatus
_PgPvcServiceRowStatus_Object = MibTableColumn
pgPvcServiceRowStatus = _PgPvcServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 2, 1, 6),
    _PgPvcServiceRowStatus_Type()
)
pgPvcServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgPvcServiceRowStatus.setStatus("current")
_PgNextSarVciTable_Object = MibTable
pgNextSarVciTable = _PgNextSarVciTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3)
)
if mibBuilder.loadTexts:
    pgNextSarVciTable.setStatus("current")
_PgNextSarVciEntry_Object = MibTableRow
pgNextSarVciEntry = _PgNextSarVciEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3, 1)
)
pgNextSarVciEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pgNextSarVciEntry.setStatus("current")


class _PgNextSarSlotVci_Type(Integer32):
    """Custom type pgNextSarSlotVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 4095),
    )


_PgNextSarSlotVci_Type.__name__ = "Integer32"
_PgNextSarSlotVci_Object = MibTableColumn
pgNextSarSlotVci = _PgNextSarSlotVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 3, 1, 1),
    _PgNextSarSlotVci_Type()
)
pgNextSarSlotVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgNextSarSlotVci.setStatus("current")
_PgPvcFrServiceTable_Object = MibTable
pgPvcFrServiceTable = _PgPvcFrServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4)
)
if mibBuilder.loadTexts:
    pgPvcFrServiceTable.setStatus("current")
_PgPvcFrServiceEntry_Object = MibTableRow
pgPvcFrServiceEntry = _PgPvcFrServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1)
)
pgPvcFrServiceEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
    (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVpi"),
    (0, "PVC-SERVICE-MIB", "pgPvcServiceSarVci"),
)
if mibBuilder.loadTexts:
    pgPvcFrServiceEntry.setStatus("current")
_PgPvcFrServiceRowStatus_Type = RowStatus
_PgPvcFrServiceRowStatus_Object = MibTableColumn
pgPvcFrServiceRowStatus = _PgPvcFrServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1, 1),
    _PgPvcFrServiceRowStatus_Type()
)
pgPvcFrServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgPvcFrServiceRowStatus.setStatus("current")


class _PgPvcFrSubSystemType_Type(Integer32):
    """Custom type pgPvcFrSubSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("frf5", 5),
          ("frf8", 8))
    )


_PgPvcFrSubSystemType_Type.__name__ = "Integer32"
_PgPvcFrSubSystemType_Object = MibTableColumn
pgPvcFrSubSystemType = _PgPvcFrSubSystemType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 6, 1, 4, 1, 2),
    _PgPvcFrSubSystemType_Type()
)
pgPvcFrSubSystemType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgPvcFrSubSystemType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PVC-SERVICE-MIB",
    **{"PgPvcServiceType": PgPvcServiceType,
       "PgXdslFrameType": PgXdslFrameType,
       "PgPvcServiceEncapType": PgPvcServiceEncapType,
       "pgService": pgService,
       "pgServiceObjects": pgServiceObjects,
       "pgXdslServiceTable": pgXdslServiceTable,
       "pgXdslServiceEntry": pgXdslServiceEntry,
       "pgXdslServiceSubscriberName": pgXdslServiceSubscriberName,
       "pgXdslServiceType": pgXdslServiceType,
       "pgXdslServiceMacAddress": pgXdslServiceMacAddress,
       "pgXdslServiceIpAddress": pgXdslServiceIpAddress,
       "pgXdslServiceSubnetMask": pgXdslServiceSubnetMask,
       "pgXdslServiceRowStatus": pgXdslServiceRowStatus,
       "pgPvcServiceTable": pgPvcServiceTable,
       "pgPvcServiceEntry": pgPvcServiceEntry,
       "pgPvcServiceSarVpi": pgPvcServiceSarVpi,
       "pgPvcServiceSarVci": pgPvcServiceSarVci,
       "pgPvcServiceIpAddress": pgPvcServiceIpAddress,
       "pgPvcServiceSubnetMask": pgPvcServiceSubnetMask,
       "pgPvcServiceEncapType": pgPvcServiceEncapType,
       "pgPvcServiceRowStatus": pgPvcServiceRowStatus,
       "pgNextSarVciTable": pgNextSarVciTable,
       "pgNextSarVciEntry": pgNextSarVciEntry,
       "pgNextSarSlotVci": pgNextSarSlotVci,
       "pgPvcFrServiceTable": pgPvcFrServiceTable,
       "pgPvcFrServiceEntry": pgPvcFrServiceEntry,
       "pgPvcFrServiceRowStatus": pgPvcFrServiceRowStatus,
       "pgPvcFrSubSystemType": pgPvcFrSubSystemType}
)
