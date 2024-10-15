# SNMP MIB module (AT-PVSTPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-PVSTPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:30 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

pvstpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140)
)
pvstpm.setRevisions(
        ("2006-03-29 16:51",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PvstpmEvents_ObjectIdentity = ObjectIdentity
pvstpmEvents = _PvstpmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0)
)
_PvstpmEventVariables_ObjectIdentity = ObjectIdentity
pvstpmEventVariables = _PvstpmEventVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1)
)
_PvstpmBridgeId_Type = OctetString
_PvstpmBridgeId_Object = MibScalar
pvstpmBridgeId = _PvstpmBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 1),
    _PvstpmBridgeId_Type()
)
pvstpmBridgeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmBridgeId.setStatus("current")
_PvstpmTopologyChangeVlan_Type = VlanIndex
_PvstpmTopologyChangeVlan_Object = MibScalar
pvstpmTopologyChangeVlan = _PvstpmTopologyChangeVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 2),
    _PvstpmTopologyChangeVlan_Type()
)
pvstpmTopologyChangeVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmTopologyChangeVlan.setStatus("current")
_PvstpmRxPort_Type = Integer32
_PvstpmRxPort_Object = MibScalar
pvstpmRxPort = _PvstpmRxPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 3),
    _PvstpmRxPort_Type()
)
pvstpmRxPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmRxPort.setStatus("current")
_PvstpmRxVlan_Type = VlanIndex
_PvstpmRxVlan_Object = MibScalar
pvstpmRxVlan = _PvstpmRxVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 4),
    _PvstpmRxVlan_Type()
)
pvstpmRxVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmRxVlan.setStatus("current")
_PvstpmTxVlan_Type = VlanIndex
_PvstpmTxVlan_Object = MibScalar
pvstpmTxVlan = _PvstpmTxVlan_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 1, 5),
    _PvstpmTxVlan_Type()
)
pvstpmTxVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pvstpmTxVlan.setStatus("current")

# Managed Objects groups


# Notification objects

pvstpmTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0, 1)
)
pvstpmTopologyChange.setObjects(
      *(("AT-PVSTPM-MIB", "pvstpmBridgeId"),
        ("AT-PVSTPM-MIB", "pvstpmTopologyChangeVlan"))
)
if mibBuilder.loadTexts:
    pvstpmTopologyChange.setStatus(
        "current"
    )

pvstpmInconsistentBPDU = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 140, 0, 2)
)
pvstpmInconsistentBPDU.setObjects(
      *(("AT-PVSTPM-MIB", "pvstpmBridgeId"),
        ("AT-PVSTPM-MIB", "pvstpmRxPort"),
        ("AT-PVSTPM-MIB", "pvstpmRxVlan"),
        ("AT-PVSTPM-MIB", "pvstpmTxVlan"))
)
if mibBuilder.loadTexts:
    pvstpmInconsistentBPDU.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PVSTPM-MIB",
    **{"pvstpm": pvstpm,
       "pvstpmEvents": pvstpmEvents,
       "pvstpmTopologyChange": pvstpmTopologyChange,
       "pvstpmInconsistentBPDU": pvstpmInconsistentBPDU,
       "pvstpmEventVariables": pvstpmEventVariables,
       "pvstpmBridgeId": pvstpmBridgeId,
       "pvstpmTopologyChangeVlan": pvstpmTopologyChangeVlan,
       "pvstpmRxPort": pvstpmRxPort,
       "pvstpmRxVlan": pvstpmRxVlan,
       "pvstpmTxVlan": pvstpmTxVlan}
)
