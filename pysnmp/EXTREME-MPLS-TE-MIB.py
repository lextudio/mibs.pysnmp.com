# SNMP MIB module (EXTREME-MPLS-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-MPLS-TE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:54 2024
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

(extremeMplsMIB,) = mibBuilder.importSymbols(
    "EXTREME-MPLS-MIB",
    "extremeMplsMIB")

(mplsTunnelEgressLSRId,
 mplsTunnelIndex,
 mplsTunnelIngressLSRId,
 mplsTunnelInstance) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelEgressLSRId",
    "mplsTunnelIndex",
    "mplsTunnelIngressLSRId",
    "mplsTunnelInstance")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

extremeMplsTeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeMplsTeScalars_ObjectIdentity = ObjectIdentity
extremeMplsTeScalars = _ExtremeMplsTeScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 1)
)
_ExtremeMplsTeObjects_ObjectIdentity = ObjectIdentity
extremeMplsTeObjects = _ExtremeMplsTeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2)
)
_ExtremeMplsTunnelTable_Object = MibTable
extremeMplsTunnelTable = _ExtremeMplsTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1)
)
if mibBuilder.loadTexts:
    extremeMplsTunnelTable.setStatus("current")
_ExtremeMplsTunnelEntry_Object = MibTableRow
extremeMplsTunnelEntry = _ExtremeMplsTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1)
)
extremeMplsTunnelEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelInstance"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelIngressLSRId"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    extremeMplsTunnelEntry.setStatus("current")


class _MplsTunnelRedundancyType_Type(Integer32):
    """Custom type mplsTunnelRedundancyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_MplsTunnelRedundancyType_Type.__name__ = "Integer32"
_MplsTunnelRedundancyType_Object = MibTableColumn
mplsTunnelRedundancyType = _MplsTunnelRedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1, 1),
    _MplsTunnelRedundancyType_Type()
)
mplsTunnelRedundancyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelRedundancyType.setStatus("current")


class _MplsTunnelRedundancyStatus_Type(Integer32):
    """Custom type mplsTunnelRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_MplsTunnelRedundancyStatus_Type.__name__ = "Integer32"
_MplsTunnelRedundancyStatus_Object = MibTableColumn
mplsTunnelRedundancyStatus = _MplsTunnelRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1, 2),
    _MplsTunnelRedundancyStatus_Type()
)
mplsTunnelRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsTunnelRedundancyStatus.setStatus("current")


class _MplsTunnelTransportStatus_Type(Bits):
    """Custom type mplsTunnelTransportStatus based on Bits"""
    namedValues = NamedValues(
        *(("allowAllIp", 0),
          ("allowAllLayer2Vpn", 2),
          ("allowAsignedLayer2VpnOnly", 3),
          ("allowAssignedIpOnly", 1))
    )

_MplsTunnelTransportStatus_Type.__name__ = "Bits"
_MplsTunnelTransportStatus_Object = MibTableColumn
mplsTunnelTransportStatus = _MplsTunnelTransportStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 2, 1, 1, 3),
    _MplsTunnelTransportStatus_Type()
)
mplsTunnelTransportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsTunnelTransportStatus.setStatus("current")
_ExtremeMplsTeConformance_ObjectIdentity = ObjectIdentity
extremeMplsTeConformance = _ExtremeMplsTeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 37, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-MPLS-TE-MIB",
    **{"extremeMplsTeMIB": extremeMplsTeMIB,
       "extremeMplsTeScalars": extremeMplsTeScalars,
       "extremeMplsTeObjects": extremeMplsTeObjects,
       "extremeMplsTunnelTable": extremeMplsTunnelTable,
       "extremeMplsTunnelEntry": extremeMplsTunnelEntry,
       "mplsTunnelRedundancyType": mplsTunnelRedundancyType,
       "mplsTunnelRedundancyStatus": mplsTunnelRedundancyStatus,
       "mplsTunnelTransportStatus": mplsTunnelTransportStatus,
       "extremeMplsTeConformance": extremeMplsTeConformance}
)
