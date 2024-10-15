# SNMP MIB module (ELTEX-MES-VLAN-AGGREGATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-VLAN-AGGREGATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:06 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

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

eltMesIpUnnumbered = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7)
)
eltMesIpUnnumbered.setRevisions(
        ("2014-05-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltIpUnnumberedInterfaceTable_Object = MibTable
eltIpUnnumberedInterfaceTable = _EltIpUnnumberedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1)
)
if mibBuilder.loadTexts:
    eltIpUnnumberedInterfaceTable.setStatus("current")
_EltIpUnnumberedInterfaceEntry_Object = MibTableRow
eltIpUnnumberedInterfaceEntry = _EltIpUnnumberedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1)
)
eltIpUnnumberedInterfaceEntry.setIndexNames(
    (0, "ELTEX-MES-VLAN-AGGREGATE-MIB", "eltIpUnnumberedIfIndex"),
)
if mibBuilder.loadTexts:
    eltIpUnnumberedInterfaceEntry.setStatus("current")
_EltIpUnnumberedIfIndex_Type = Integer32
_EltIpUnnumberedIfIndex_Object = MibTableColumn
eltIpUnnumberedIfIndex = _EltIpUnnumberedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 1),
    _EltIpUnnumberedIfIndex_Type()
)
eltIpUnnumberedIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpUnnumberedIfIndex.setStatus("current")
_EltIpUnnumberedAggrIfIndex_Type = Integer32
_EltIpUnnumberedAggrIfIndex_Object = MibTableColumn
eltIpUnnumberedAggrIfIndex = _EltIpUnnumberedAggrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 2),
    _EltIpUnnumberedAggrIfIndex_Type()
)
eltIpUnnumberedAggrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltIpUnnumberedAggrIfIndex.setStatus("current")


class _EltIpUnnumberedVlan1to1024_Type(OctetString):
    """Custom type eltIpUnnumberedVlan1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltIpUnnumberedVlan1to1024_Type.__name__ = "OctetString"
_EltIpUnnumberedVlan1to1024_Object = MibTableColumn
eltIpUnnumberedVlan1to1024 = _EltIpUnnumberedVlan1to1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 3),
    _EltIpUnnumberedVlan1to1024_Type()
)
eltIpUnnumberedVlan1to1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpUnnumberedVlan1to1024.setStatus("current")


class _EltIpUnnumberedVlan1025to2048_Type(OctetString):
    """Custom type eltIpUnnumberedVlan1025to2048 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltIpUnnumberedVlan1025to2048_Type.__name__ = "OctetString"
_EltIpUnnumberedVlan1025to2048_Object = MibTableColumn
eltIpUnnumberedVlan1025to2048 = _EltIpUnnumberedVlan1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 4),
    _EltIpUnnumberedVlan1025to2048_Type()
)
eltIpUnnumberedVlan1025to2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpUnnumberedVlan1025to2048.setStatus("current")


class _EltIpUnnumberedVlan2049to3072_Type(OctetString):
    """Custom type eltIpUnnumberedVlan2049to3072 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltIpUnnumberedVlan2049to3072_Type.__name__ = "OctetString"
_EltIpUnnumberedVlan2049to3072_Object = MibTableColumn
eltIpUnnumberedVlan2049to3072 = _EltIpUnnumberedVlan2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 5),
    _EltIpUnnumberedVlan2049to3072_Type()
)
eltIpUnnumberedVlan2049to3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpUnnumberedVlan2049to3072.setStatus("current")


class _EltIpUnnumberedVlan3073to4094_Type(OctetString):
    """Custom type eltIpUnnumberedVlan3073to4094 based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltIpUnnumberedVlan3073to4094_Type.__name__ = "OctetString"
_EltIpUnnumberedVlan3073to4094_Object = MibTableColumn
eltIpUnnumberedVlan3073to4094 = _EltIpUnnumberedVlan3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 6),
    _EltIpUnnumberedVlan3073to4094_Type()
)
eltIpUnnumberedVlan3073to4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltIpUnnumberedVlan3073to4094.setStatus("current")
_EltIpUnnumberedStatus_Type = RowStatus
_EltIpUnnumberedStatus_Object = MibTableColumn
eltIpUnnumberedStatus = _EltIpUnnumberedStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 7, 1, 1, 7),
    _EltIpUnnumberedStatus_Type()
)
eltIpUnnumberedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltIpUnnumberedStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-VLAN-AGGREGATE-MIB",
    **{"eltMesIpUnnumbered": eltMesIpUnnumbered,
       "eltIpUnnumberedInterfaceTable": eltIpUnnumberedInterfaceTable,
       "eltIpUnnumberedInterfaceEntry": eltIpUnnumberedInterfaceEntry,
       "eltIpUnnumberedIfIndex": eltIpUnnumberedIfIndex,
       "eltIpUnnumberedAggrIfIndex": eltIpUnnumberedAggrIfIndex,
       "eltIpUnnumberedVlan1to1024": eltIpUnnumberedVlan1to1024,
       "eltIpUnnumberedVlan1025to2048": eltIpUnnumberedVlan1025to2048,
       "eltIpUnnumberedVlan2049to3072": eltIpUnnumberedVlan2049to3072,
       "eltIpUnnumberedVlan3073to4094": eltIpUnnumberedVlan3073to4094,
       "eltIpUnnumberedStatus": eltIpUnnumberedStatus}
)
