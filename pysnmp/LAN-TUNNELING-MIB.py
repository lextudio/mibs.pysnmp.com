# SNMP MIB module (LAN-TUNNELING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LAN-TUNNELING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:54 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pgLantMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2)
)


# Types definitions



class PgLantEncapType(Integer32):
    """Custom type PgLantEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("llc-snap", 2),
          ("other", 1),
          ("vc-mux", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgLantObjects_ObjectIdentity = ObjectIdentity
pgLantObjects = _PgLantObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1)
)
_PgLantTable_Object = MibTable
pgLantTable = _PgLantTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pgLantTable.setStatus("current")
_PgLantEntry_Object = MibTableRow
pgLantEntry = _PgLantEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1)
)
pgLantEntry.setIndexNames(
    (0, "LAN-TUNNELING-MIB", "pgLantChannelPortIfIndex"),
)
if mibBuilder.loadTexts:
    pgLantEntry.setStatus("current")


class _PgLantChannelPortIfIndex_Type(Integer32):
    """Custom type pgLantChannelPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_PgLantChannelPortIfIndex_Type.__name__ = "Integer32"
_PgLantChannelPortIfIndex_Object = MibTableColumn
pgLantChannelPortIfIndex = _PgLantChannelPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 1),
    _PgLantChannelPortIfIndex_Type()
)
pgLantChannelPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLantChannelPortIfIndex.setStatus("current")


class _PgLantLinePortIfIndex_Type(Integer32):
    """Custom type pgLantLinePortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2047),
    )


_PgLantLinePortIfIndex_Type.__name__ = "Integer32"
_PgLantLinePortIfIndex_Object = MibTableColumn
pgLantLinePortIfIndex = _PgLantLinePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 2),
    _PgLantLinePortIfIndex_Type()
)
pgLantLinePortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLantLinePortIfIndex.setStatus("current")


class _PgLantVpi_Type(Integer32):
    """Custom type pgLantVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PgLantVpi_Type.__name__ = "Integer32"
_PgLantVpi_Object = MibTableColumn
pgLantVpi = _PgLantVpi_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 3),
    _PgLantVpi_Type()
)
pgLantVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLantVpi.setStatus("current")


class _PgLantVci_Type(Integer32):
    """Custom type pgLantVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PgLantVci_Type.__name__ = "Integer32"
_PgLantVci_Object = MibTableColumn
pgLantVci = _PgLantVci_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 4),
    _PgLantVci_Type()
)
pgLantVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLantVci.setStatus("current")
_PgLantEncapMode_Type = PgLantEncapType
_PgLantEncapMode_Object = MibTableColumn
pgLantEncapMode = _PgLantEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 5),
    _PgLantEncapMode_Type()
)
pgLantEncapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLantEncapMode.setStatus("current")
_PgLantRowStatus_Type = RowStatus
_PgLantRowStatus_Object = MibTableColumn
pgLantRowStatus = _PgLantRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 9, 2, 1, 1, 1, 6),
    _PgLantRowStatus_Type()
)
pgLantRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pgLantRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN-TUNNELING-MIB",
    **{"PgLantEncapType": PgLantEncapType,
       "pgLantMIB": pgLantMIB,
       "pgLantObjects": pgLantObjects,
       "pgLantTable": pgLantTable,
       "pgLantEntry": pgLantEntry,
       "pgLantChannelPortIfIndex": pgLantChannelPortIfIndex,
       "pgLantLinePortIfIndex": pgLantLinePortIfIndex,
       "pgLantVpi": pgLantVpi,
       "pgLantVci": pgLantVci,
       "pgLantEncapMode": pgLantEncapMode,
       "pgLantRowStatus": pgLantRowStatus}
)
