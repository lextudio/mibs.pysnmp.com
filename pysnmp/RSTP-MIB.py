# SNMP MIB module (RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:30 2024
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

(dot1dStp,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStp",
    "dot1dStpPortEntry")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 134)
)
rstpMIB.setRevisions(
        ("2005-12-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Dot1dStpVersion_Type(Integer32):
    """Custom type dot1dStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 2),
          ("stpCompatible", 0))
    )


_Dot1dStpVersion_Type.__name__ = "Integer32"
_Dot1dStpVersion_Object = MibScalar
dot1dStpVersion = _Dot1dStpVersion_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 16),
    _Dot1dStpVersion_Type()
)
dot1dStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpVersion.setStatus("current")


class _Dot1dStpTxHoldCount_Type(Integer32):
    """Custom type dot1dStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1dStpTxHoldCount_Type.__name__ = "Integer32"
_Dot1dStpTxHoldCount_Object = MibScalar
dot1dStpTxHoldCount = _Dot1dStpTxHoldCount_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 17),
    _Dot1dStpTxHoldCount_Type()
)
dot1dStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpTxHoldCount.setStatus("current")
_Dot1dStpExtPortTable_Object = MibTable
dot1dStpExtPortTable = _Dot1dStpExtPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19)
)
if mibBuilder.loadTexts:
    dot1dStpExtPortTable.setStatus("current")
_Dot1dStpExtPortEntry_Object = MibTableRow
dot1dStpExtPortEntry = _Dot1dStpExtPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19, 1)
)
if mibBuilder.loadTexts:
    dot1dStpExtPortEntry.setStatus("current")
_Dot1dStpPortProtocolMigration_Type = TruthValue
_Dot1dStpPortProtocolMigration_Object = MibTableColumn
dot1dStpPortProtocolMigration = _Dot1dStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 1),
    _Dot1dStpPortProtocolMigration_Type()
)
dot1dStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortProtocolMigration.setStatus("current")
_Dot1dStpPortAdminEdgePort_Type = TruthValue
_Dot1dStpPortAdminEdgePort_Object = MibTableColumn
dot1dStpPortAdminEdgePort = _Dot1dStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 2),
    _Dot1dStpPortAdminEdgePort_Type()
)
dot1dStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortAdminEdgePort.setStatus("current")
_Dot1dStpPortOperEdgePort_Type = TruthValue
_Dot1dStpPortOperEdgePort_Object = MibTableColumn
dot1dStpPortOperEdgePort = _Dot1dStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 3),
    _Dot1dStpPortOperEdgePort_Type()
)
dot1dStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortOperEdgePort.setStatus("current")


class _Dot1dStpPortAdminPointToPoint_Type(Integer32):
    """Custom type dot1dStpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_Dot1dStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_Dot1dStpPortAdminPointToPoint_Object = MibTableColumn
dot1dStpPortAdminPointToPoint = _Dot1dStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 4),
    _Dot1dStpPortAdminPointToPoint_Type()
)
dot1dStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortAdminPointToPoint.setStatus("current")
_Dot1dStpPortOperPointToPoint_Type = TruthValue
_Dot1dStpPortOperPointToPoint_Object = MibTableColumn
dot1dStpPortOperPointToPoint = _Dot1dStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 5),
    _Dot1dStpPortOperPointToPoint_Type()
)
dot1dStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dStpPortOperPointToPoint.setStatus("current")


class _Dot1dStpPortAdminPathCost_Type(Integer32):
    """Custom type dot1dStpPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Dot1dStpPortAdminPathCost_Type.__name__ = "Integer32"
_Dot1dStpPortAdminPathCost_Object = MibTableColumn
dot1dStpPortAdminPathCost = _Dot1dStpPortAdminPathCost_Object(
    (1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 6),
    _Dot1dStpPortAdminPathCost_Type()
)
dot1dStpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dStpPortAdminPathCost.setStatus("current")
_RstpNotifications_ObjectIdentity = ObjectIdentity
rstpNotifications = _RstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 134, 0)
)
_RstpObjects_ObjectIdentity = ObjectIdentity
rstpObjects = _RstpObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 134, 1)
)
_RstpConformance_ObjectIdentity = ObjectIdentity
rstpConformance = _RstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 134, 2)
)
_RstpGroups_ObjectIdentity = ObjectIdentity
rstpGroups = _RstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 134, 2, 1)
)
_RstpCompliances_ObjectIdentity = ObjectIdentity
rstpCompliances = _RstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 134, 2, 2)
)
dot1dStpPortEntry.registerAugmentions(
    ("RSTP-MIB",
     "dot1dStpExtPortEntry")
)
dot1dStpExtPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups

rstpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 134, 2, 1, 1)
)
rstpBridgeGroup.setObjects(
      *(("RSTP-MIB", "dot1dStpVersion"),
        ("RSTP-MIB", "dot1dStpTxHoldCount"))
)
if mibBuilder.loadTexts:
    rstpBridgeGroup.setStatus("current")

rstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 134, 2, 1, 2)
)
rstpPortGroup.setObjects(
      *(("RSTP-MIB", "dot1dStpPortProtocolMigration"),
        ("RSTP-MIB", "dot1dStpPortAdminEdgePort"),
        ("RSTP-MIB", "dot1dStpPortOperEdgePort"),
        ("RSTP-MIB", "dot1dStpPortAdminPointToPoint"),
        ("RSTP-MIB", "dot1dStpPortOperPointToPoint"),
        ("RSTP-MIB", "dot1dStpPortAdminPathCost"))
)
if mibBuilder.loadTexts:
    rstpPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 134, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RSTP-MIB",
    **{"dot1dStpVersion": dot1dStpVersion,
       "dot1dStpTxHoldCount": dot1dStpTxHoldCount,
       "dot1dStpExtPortTable": dot1dStpExtPortTable,
       "dot1dStpExtPortEntry": dot1dStpExtPortEntry,
       "dot1dStpPortProtocolMigration": dot1dStpPortProtocolMigration,
       "dot1dStpPortAdminEdgePort": dot1dStpPortAdminEdgePort,
       "dot1dStpPortOperEdgePort": dot1dStpPortOperEdgePort,
       "dot1dStpPortAdminPointToPoint": dot1dStpPortAdminPointToPoint,
       "dot1dStpPortOperPointToPoint": dot1dStpPortOperPointToPoint,
       "dot1dStpPortAdminPathCost": dot1dStpPortAdminPathCost,
       "rstpMIB": rstpMIB,
       "rstpNotifications": rstpNotifications,
       "rstpObjects": rstpObjects,
       "rstpConformance": rstpConformance,
       "rstpGroups": rstpGroups,
       "rstpBridgeGroup": rstpBridgeGroup,
       "rstpPortGroup": rstpPortGroup,
       "rstpCompliances": rstpCompliances,
       "rstpCompliance": rstpCompliance}
)
