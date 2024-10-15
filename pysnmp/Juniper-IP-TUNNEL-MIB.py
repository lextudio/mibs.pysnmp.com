# SNMP MIB module (Juniper-IP-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IP-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:33 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniName,
 JuniNextIfIndex) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniName",
    "JuniNextIfIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniIpTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51)
)
juniIpTunnelMIB.setRevisions(
        ("2003-09-29 17:29",
         "2002-09-16 21:44",
         "2002-01-14 18:16",
         "2001-07-23 20:57")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniIpTunnelInterfaceObjects_ObjectIdentity = ObjectIdentity
juniIpTunnelInterfaceObjects = _JuniIpTunnelInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1)
)
_JuniIpTunnelNextIfIndex_Type = JuniNextIfIndex
_JuniIpTunnelNextIfIndex_Object = MibScalar
juniIpTunnelNextIfIndex = _JuniIpTunnelNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 1),
    _JuniIpTunnelNextIfIndex_Type()
)
juniIpTunnelNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIpTunnelNextIfIndex.setStatus("current")
_JuniIpTunnelInterfaceTable_Object = MibTable
juniIpTunnelInterfaceTable = _JuniIpTunnelInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpTunnelInterfaceTable.setStatus("current")
_JuniIpTunnelInterfaceEntry_Object = MibTableRow
juniIpTunnelInterfaceEntry = _JuniIpTunnelInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1)
)
juniIpTunnelInterfaceEntry.setIndexNames(
    (0, "Juniper-IP-TUNNEL-MIB", "juniIpTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    juniIpTunnelInterfaceEntry.setStatus("current")
_JuniIpTunnelIfIndex_Type = InterfaceIndex
_JuniIpTunnelIfIndex_Object = MibTableColumn
juniIpTunnelIfIndex = _JuniIpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 1),
    _JuniIpTunnelIfIndex_Type()
)
juniIpTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIpTunnelIfIndex.setStatus("current")


class _JuniIpTunnelName_Type(DisplayString):
    """Custom type juniIpTunnelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIpTunnelName_Type.__name__ = "DisplayString"
_JuniIpTunnelName_Object = MibTableColumn
juniIpTunnelName = _JuniIpTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 2),
    _JuniIpTunnelName_Type()
)
juniIpTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelName.setStatus("current")


class _JuniIpTunnelMode_Type(Integer32):
    """Custom type juniIpTunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipTunnelModeDvmrp", 1),
          ("ipTunnelModeGre", 0))
    )


_JuniIpTunnelMode_Type.__name__ = "Integer32"
_JuniIpTunnelMode_Object = MibTableColumn
juniIpTunnelMode = _JuniIpTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 3),
    _JuniIpTunnelMode_Type()
)
juniIpTunnelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelMode.setStatus("current")


class _JuniIpTunnelVirtualRouter_Type(JuniName):
    """Custom type juniIpTunnelVirtualRouter based on JuniName"""
    defaultValue = OctetString("default")


_JuniIpTunnelVirtualRouter_Object = MibTableColumn
juniIpTunnelVirtualRouter = _JuniIpTunnelVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 4),
    _JuniIpTunnelVirtualRouter_Type()
)
juniIpTunnelVirtualRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelVirtualRouter.setStatus("current")


class _JuniIpTunnelChecksum_Type(TruthValue):
    """Custom type juniIpTunnelChecksum based on TruthValue"""


_JuniIpTunnelChecksum_Object = MibTableColumn
juniIpTunnelChecksum = _JuniIpTunnelChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 5),
    _JuniIpTunnelChecksum_Type()
)
juniIpTunnelChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelChecksum.setStatus("current")


class _JuniIpTunnelMtu_Type(Integer32):
    """Custom type juniIpTunnelMtu based on Integer32"""
    defaultValue = 10240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 10240),
    )


_JuniIpTunnelMtu_Type.__name__ = "Integer32"
_JuniIpTunnelMtu_Object = MibTableColumn
juniIpTunnelMtu = _JuniIpTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 6),
    _JuniIpTunnelMtu_Type()
)
juniIpTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelMtu.setStatus("current")


class _JuniIpTunnelDestination_Type(IpAddress):
    """Custom type juniIpTunnelDestination based on IpAddress"""
    defaultValue = 0


_JuniIpTunnelDestination_Object = MibTableColumn
juniIpTunnelDestination = _JuniIpTunnelDestination_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 7),
    _JuniIpTunnelDestination_Type()
)
juniIpTunnelDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelDestination.setStatus("current")


class _JuniIpTunnelSource_Type(IpAddress):
    """Custom type juniIpTunnelSource based on IpAddress"""
    defaultValue = 0


_JuniIpTunnelSource_Object = MibTableColumn
juniIpTunnelSource = _JuniIpTunnelSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 8),
    _JuniIpTunnelSource_Type()
)
juniIpTunnelSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelSource.setStatus("current")
_JuniIpTunnelRowStatus_Type = RowStatus
_JuniIpTunnelRowStatus_Object = MibTableColumn
juniIpTunnelRowStatus = _JuniIpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 9),
    _JuniIpTunnelRowStatus_Type()
)
juniIpTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelRowStatus.setStatus("current")


class _JuniIpTunnelSequenceNumbers_Type(TruthValue):
    """Custom type juniIpTunnelSequenceNumbers based on TruthValue"""


_JuniIpTunnelSequenceNumbers_Object = MibTableColumn
juniIpTunnelSequenceNumbers = _JuniIpTunnelSequenceNumbers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 1, 2, 1, 10),
    _JuniIpTunnelSequenceNumbers_Type()
)
juniIpTunnelSequenceNumbers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIpTunnelSequenceNumbers.setStatus("current")
_JuniIpTunnelConformance_ObjectIdentity = ObjectIdentity
juniIpTunnelConformance = _JuniIpTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2)
)
_JuniIpTunnelCompliances_ObjectIdentity = ObjectIdentity
juniIpTunnelCompliances = _JuniIpTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 1)
)
_JuniIpTunnelGroups_ObjectIdentity = ObjectIdentity
juniIpTunnelGroups = _JuniIpTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 2)
)

# Managed Objects groups

juniIpTunnelInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 2, 1)
)
juniIpTunnelInterfaceGroup.setObjects(
      *(("Juniper-IP-TUNNEL-MIB", "juniIpTunnelNextIfIndex"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelName"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelMode"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelVirtualRouter"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelChecksum"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelMtu"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelSource"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelDestination"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    juniIpTunnelInterfaceGroup.setStatus("obsolete")

juniIpTunnelInterfaceGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 2, 2)
)
juniIpTunnelInterfaceGroup2.setObjects(
      *(("Juniper-IP-TUNNEL-MIB", "juniIpTunnelNextIfIndex"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelName"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelMode"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelVirtualRouter"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelChecksum"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelMtu"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelSource"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelDestination"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelRowStatus"),
        ("Juniper-IP-TUNNEL-MIB", "juniIpTunnelSequenceNumbers"))
)
if mibBuilder.loadTexts:
    juniIpTunnelInterfaceGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIpTunnnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniIpTunnnelCompliance.setStatus(
        "obsolete"
    )

juniIpTunnnelCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 51, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniIpTunnnelCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IP-TUNNEL-MIB",
    **{"juniIpTunnelMIB": juniIpTunnelMIB,
       "juniIpTunnelInterfaceObjects": juniIpTunnelInterfaceObjects,
       "juniIpTunnelNextIfIndex": juniIpTunnelNextIfIndex,
       "juniIpTunnelInterfaceTable": juniIpTunnelInterfaceTable,
       "juniIpTunnelInterfaceEntry": juniIpTunnelInterfaceEntry,
       "juniIpTunnelIfIndex": juniIpTunnelIfIndex,
       "juniIpTunnelName": juniIpTunnelName,
       "juniIpTunnelMode": juniIpTunnelMode,
       "juniIpTunnelVirtualRouter": juniIpTunnelVirtualRouter,
       "juniIpTunnelChecksum": juniIpTunnelChecksum,
       "juniIpTunnelMtu": juniIpTunnelMtu,
       "juniIpTunnelDestination": juniIpTunnelDestination,
       "juniIpTunnelSource": juniIpTunnelSource,
       "juniIpTunnelRowStatus": juniIpTunnelRowStatus,
       "juniIpTunnelSequenceNumbers": juniIpTunnelSequenceNumbers,
       "juniIpTunnelConformance": juniIpTunnelConformance,
       "juniIpTunnelCompliances": juniIpTunnelCompliances,
       "juniIpTunnnelCompliance": juniIpTunnnelCompliance,
       "juniIpTunnnelCompliance2": juniIpTunnnelCompliance2,
       "juniIpTunnelGroups": juniIpTunnelGroups,
       "juniIpTunnelInterfaceGroup": juniIpTunnelInterfaceGroup,
       "juniIpTunnelInterfaceGroup2": juniIpTunnelInterfaceGroup2}
)
