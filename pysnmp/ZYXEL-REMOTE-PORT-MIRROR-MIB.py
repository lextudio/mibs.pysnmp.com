# SNMP MIB module (ZYXEL-REMOTE-PORT-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-REMOTE-PORT-MIRROR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:43 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelRemotePortMirror = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelRemotePortMirrorSetup_ObjectIdentity = ObjectIdentity
zyxelRemotePortMirrorSetup = _ZyxelRemotePortMirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1)
)
_ZyRemotePortMirrorMaxNumberOfVlans_Type = Integer32
_ZyRemotePortMirrorMaxNumberOfVlans_Object = MibScalar
zyRemotePortMirrorMaxNumberOfVlans = _ZyRemotePortMirrorMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 1),
    _ZyRemotePortMirrorMaxNumberOfVlans_Type()
)
zyRemotePortMirrorMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyRemotePortMirrorMaxNumberOfVlans.setStatus("current")
_ZyxelRemotePortMirrorTable_Object = MibTable
zyxelRemotePortMirrorTable = _ZyxelRemotePortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelRemotePortMirrorTable.setStatus("current")
_ZyxelRemotePortMirrorEntry_Object = MibTableRow
zyxelRemotePortMirrorEntry = _ZyxelRemotePortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1)
)
zyxelRemotePortMirrorEntry.setIndexNames(
    (0, "ZYXEL-REMOTE-PORT-MIRROR-MIB", "zyRemotePortMirrorVid"),
)
if mibBuilder.loadTexts:
    zyxelRemotePortMirrorEntry.setStatus("current")


class _ZyRemotePortMirrorVid_Type(Integer32):
    """Custom type zyRemotePortMirrorVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyRemotePortMirrorVid_Type.__name__ = "Integer32"
_ZyRemotePortMirrorVid_Object = MibTableColumn
zyRemotePortMirrorVid = _ZyRemotePortMirrorVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 1),
    _ZyRemotePortMirrorVid_Type()
)
zyRemotePortMirrorVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyRemotePortMirrorVid.setStatus("current")


class _ZyRemotePortMirrorSource8021pPriority_Type(Integer32):
    """Custom type zyRemotePortMirrorSource8021pPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZyRemotePortMirrorSource8021pPriority_Type.__name__ = "Integer32"
_ZyRemotePortMirrorSource8021pPriority_Object = MibTableColumn
zyRemotePortMirrorSource8021pPriority = _ZyRemotePortMirrorSource8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 2),
    _ZyRemotePortMirrorSource8021pPriority_Type()
)
zyRemotePortMirrorSource8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorSource8021pPriority.setStatus("current")
_ZyRemotePortMirrorSourceIngressMirrorPorts_Type = PortList
_ZyRemotePortMirrorSourceIngressMirrorPorts_Object = MibTableColumn
zyRemotePortMirrorSourceIngressMirrorPorts = _ZyRemotePortMirrorSourceIngressMirrorPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 3),
    _ZyRemotePortMirrorSourceIngressMirrorPorts_Type()
)
zyRemotePortMirrorSourceIngressMirrorPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorSourceIngressMirrorPorts.setStatus("current")
_ZyRemotePortMirrorSourceEgressMirrorPorts_Type = PortList
_ZyRemotePortMirrorSourceEgressMirrorPorts_Object = MibTableColumn
zyRemotePortMirrorSourceEgressMirrorPorts = _ZyRemotePortMirrorSourceEgressMirrorPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 4),
    _ZyRemotePortMirrorSourceEgressMirrorPorts_Type()
)
zyRemotePortMirrorSourceEgressMirrorPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorSourceEgressMirrorPorts.setStatus("current")
_ZyRemotePortMirrorSourceReflectorPortState_Type = EnabledStatus
_ZyRemotePortMirrorSourceReflectorPortState_Object = MibTableColumn
zyRemotePortMirrorSourceReflectorPortState = _ZyRemotePortMirrorSourceReflectorPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 5),
    _ZyRemotePortMirrorSourceReflectorPortState_Type()
)
zyRemotePortMirrorSourceReflectorPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorSourceReflectorPortState.setStatus("current")
_ZyRemotePortMirrorSourceReflectorPort_Type = Integer32
_ZyRemotePortMirrorSourceReflectorPort_Object = MibTableColumn
zyRemotePortMirrorSourceReflectorPort = _ZyRemotePortMirrorSourceReflectorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 6),
    _ZyRemotePortMirrorSourceReflectorPort_Type()
)
zyRemotePortMirrorSourceReflectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorSourceReflectorPort.setStatus("current")
_ZyRemotePortMirrorDestinationMonitorPort_Type = Integer32
_ZyRemotePortMirrorDestinationMonitorPort_Object = MibTableColumn
zyRemotePortMirrorDestinationMonitorPort = _ZyRemotePortMirrorDestinationMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 7),
    _ZyRemotePortMirrorDestinationMonitorPort_Type()
)
zyRemotePortMirrorDestinationMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorDestinationMonitorPort.setStatus("current")
_ZyRemotePortMirrorDestinationMonitorPortTagging_Type = EnabledStatus
_ZyRemotePortMirrorDestinationMonitorPortTagging_Object = MibTableColumn
zyRemotePortMirrorDestinationMonitorPortTagging = _ZyRemotePortMirrorDestinationMonitorPortTagging_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 8),
    _ZyRemotePortMirrorDestinationMonitorPortTagging_Type()
)
zyRemotePortMirrorDestinationMonitorPortTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorDestinationMonitorPortTagging.setStatus("current")
_ZyRemotePortMirrorConnectedPorts_Type = PortList
_ZyRemotePortMirrorConnectedPorts_Object = MibTableColumn
zyRemotePortMirrorConnectedPorts = _ZyRemotePortMirrorConnectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 9),
    _ZyRemotePortMirrorConnectedPorts_Type()
)
zyRemotePortMirrorConnectedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRemotePortMirrorConnectedPorts.setStatus("current")
_ZyRemotePortMirrorRowStatus_Type = RowStatus
_ZyRemotePortMirrorRowStatus_Object = MibTableColumn
zyRemotePortMirrorRowStatus = _ZyRemotePortMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 73, 1, 2, 1, 10),
    _ZyRemotePortMirrorRowStatus_Type()
)
zyRemotePortMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyRemotePortMirrorRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-REMOTE-PORT-MIRROR-MIB",
    **{"zyxelRemotePortMirror": zyxelRemotePortMirror,
       "zyxelRemotePortMirrorSetup": zyxelRemotePortMirrorSetup,
       "zyRemotePortMirrorMaxNumberOfVlans": zyRemotePortMirrorMaxNumberOfVlans,
       "zyxelRemotePortMirrorTable": zyxelRemotePortMirrorTable,
       "zyxelRemotePortMirrorEntry": zyxelRemotePortMirrorEntry,
       "zyRemotePortMirrorVid": zyRemotePortMirrorVid,
       "zyRemotePortMirrorSource8021pPriority": zyRemotePortMirrorSource8021pPriority,
       "zyRemotePortMirrorSourceIngressMirrorPorts": zyRemotePortMirrorSourceIngressMirrorPorts,
       "zyRemotePortMirrorSourceEgressMirrorPorts": zyRemotePortMirrorSourceEgressMirrorPorts,
       "zyRemotePortMirrorSourceReflectorPortState": zyRemotePortMirrorSourceReflectorPortState,
       "zyRemotePortMirrorSourceReflectorPort": zyRemotePortMirrorSourceReflectorPort,
       "zyRemotePortMirrorDestinationMonitorPort": zyRemotePortMirrorDestinationMonitorPort,
       "zyRemotePortMirrorDestinationMonitorPortTagging": zyRemotePortMirrorDestinationMonitorPortTagging,
       "zyRemotePortMirrorConnectedPorts": zyRemotePortMirrorConnectedPorts,
       "zyRemotePortMirrorRowStatus": zyRemotePortMirrorRowStatus}
)
