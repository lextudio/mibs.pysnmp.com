# SNMP MIB module (ZYXEL-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-SFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:47 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

zyxelSflow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelSflowSetup_ObjectIdentity = ObjectIdentity
zyxelSflowSetup = _ZyxelSflowSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1)
)
_ZySflowState_Type = EnabledStatus
_ZySflowState_Object = MibScalar
zySflowState = _ZySflowState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 1),
    _ZySflowState_Type()
)
zySflowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySflowState.setStatus("current")
_ZySflowMaxNumberOfCollectors_Type = Integer32
_ZySflowMaxNumberOfCollectors_Object = MibScalar
zySflowMaxNumberOfCollectors = _ZySflowMaxNumberOfCollectors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 2),
    _ZySflowMaxNumberOfCollectors_Type()
)
zySflowMaxNumberOfCollectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySflowMaxNumberOfCollectors.setStatus("current")
_ZyxelSflowCollectorTable_Object = MibTable
zyxelSflowCollectorTable = _ZyxelSflowCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelSflowCollectorTable.setStatus("current")
_ZyxelSflowCollectorEntry_Object = MibTableRow
zyxelSflowCollectorEntry = _ZyxelSflowCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 3, 1)
)
zyxelSflowCollectorEntry.setIndexNames(
    (0, "ZYXEL-SFLOW-MIB", "zySflowCollectorIpAddressType"),
    (0, "ZYXEL-SFLOW-MIB", "zySflowCollectorIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelSflowCollectorEntry.setStatus("current")
_ZySflowCollectorIpAddressType_Type = InetAddressType
_ZySflowCollectorIpAddressType_Object = MibTableColumn
zySflowCollectorIpAddressType = _ZySflowCollectorIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 3, 1, 1),
    _ZySflowCollectorIpAddressType_Type()
)
zySflowCollectorIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySflowCollectorIpAddressType.setStatus("current")
_ZySflowCollectorIpAddress_Type = InetAddress
_ZySflowCollectorIpAddress_Object = MibTableColumn
zySflowCollectorIpAddress = _ZySflowCollectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 3, 1, 2),
    _ZySflowCollectorIpAddress_Type()
)
zySflowCollectorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySflowCollectorIpAddress.setStatus("current")
_ZySflowCollectorUdpPort_Type = Integer32
_ZySflowCollectorUdpPort_Object = MibTableColumn
zySflowCollectorUdpPort = _ZySflowCollectorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 3, 1, 3),
    _ZySflowCollectorUdpPort_Type()
)
zySflowCollectorUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySflowCollectorUdpPort.setStatus("current")
_ZySflowCollectorRowStatus_Type = RowStatus
_ZySflowCollectorRowStatus_Object = MibTableColumn
zySflowCollectorRowStatus = _ZySflowCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 3, 1, 4),
    _ZySflowCollectorRowStatus_Type()
)
zySflowCollectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zySflowCollectorRowStatus.setStatus("current")
_ZyxelSflowPortTable_Object = MibTable
zyxelSflowPortTable = _ZyxelSflowPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelSflowPortTable.setStatus("current")
_ZyxelSflowPortEntry_Object = MibTableRow
zyxelSflowPortEntry = _ZyxelSflowPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 4, 1)
)
zyxelSflowPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelSflowPortEntry.setStatus("current")
_ZySflowPortState_Type = EnabledStatus
_ZySflowPortState_Object = MibTableColumn
zySflowPortState = _ZySflowPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 4, 1, 1),
    _ZySflowPortState_Type()
)
zySflowPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySflowPortState.setStatus("current")
_ZySflowMaxNumberOfPortCollectors_Type = Integer32
_ZySflowMaxNumberOfPortCollectors_Object = MibScalar
zySflowMaxNumberOfPortCollectors = _ZySflowMaxNumberOfPortCollectors_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 5),
    _ZySflowMaxNumberOfPortCollectors_Type()
)
zySflowMaxNumberOfPortCollectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySflowMaxNumberOfPortCollectors.setStatus("current")
_ZyxelSflowPortCollectorTable_Object = MibTable
zyxelSflowPortCollectorTable = _ZyxelSflowPortCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelSflowPortCollectorTable.setStatus("current")
_ZyxelSflowPortCollectorEntry_Object = MibTableRow
zyxelSflowPortCollectorEntry = _ZyxelSflowPortCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 6, 1)
)
zyxelSflowPortCollectorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-SFLOW-MIB", "zySflowPortCollectorIpAddressType"),
    (0, "ZYXEL-SFLOW-MIB", "zySflowPortCollectorIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelSflowPortCollectorEntry.setStatus("current")
_ZySflowPortCollectorIpAddressType_Type = InetAddressType
_ZySflowPortCollectorIpAddressType_Object = MibTableColumn
zySflowPortCollectorIpAddressType = _ZySflowPortCollectorIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 6, 1, 1),
    _ZySflowPortCollectorIpAddressType_Type()
)
zySflowPortCollectorIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySflowPortCollectorIpAddressType.setStatus("current")
_ZySflowPortCollectorIpAddress_Type = InetAddress
_ZySflowPortCollectorIpAddress_Object = MibTableColumn
zySflowPortCollectorIpAddress = _ZySflowPortCollectorIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 6, 1, 2),
    _ZySflowPortCollectorIpAddress_Type()
)
zySflowPortCollectorIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySflowPortCollectorIpAddress.setStatus("current")
_ZySflowPortCollectorSampleRate_Type = Integer32
_ZySflowPortCollectorSampleRate_Object = MibTableColumn
zySflowPortCollectorSampleRate = _ZySflowPortCollectorSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 6, 1, 3),
    _ZySflowPortCollectorSampleRate_Type()
)
zySflowPortCollectorSampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySflowPortCollectorSampleRate.setStatus("current")
_ZySflowPortCollectorPollInterval_Type = Integer32
_ZySflowPortCollectorPollInterval_Object = MibTableColumn
zySflowPortCollectorPollInterval = _ZySflowPortCollectorPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 6, 1, 4),
    _ZySflowPortCollectorPollInterval_Type()
)
zySflowPortCollectorPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySflowPortCollectorPollInterval.setStatus("current")
_ZySflowPortCollectorRowStatus_Type = RowStatus
_ZySflowPortCollectorRowStatus_Object = MibTableColumn
zySflowPortCollectorRowStatus = _ZySflowPortCollectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 75, 1, 6, 1, 5),
    _ZySflowPortCollectorRowStatus_Type()
)
zySflowPortCollectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zySflowPortCollectorRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SFLOW-MIB",
    **{"zyxelSflow": zyxelSflow,
       "zyxelSflowSetup": zyxelSflowSetup,
       "zySflowState": zySflowState,
       "zySflowMaxNumberOfCollectors": zySflowMaxNumberOfCollectors,
       "zyxelSflowCollectorTable": zyxelSflowCollectorTable,
       "zyxelSflowCollectorEntry": zyxelSflowCollectorEntry,
       "zySflowCollectorIpAddressType": zySflowCollectorIpAddressType,
       "zySflowCollectorIpAddress": zySflowCollectorIpAddress,
       "zySflowCollectorUdpPort": zySflowCollectorUdpPort,
       "zySflowCollectorRowStatus": zySflowCollectorRowStatus,
       "zyxelSflowPortTable": zyxelSflowPortTable,
       "zyxelSflowPortEntry": zyxelSflowPortEntry,
       "zySflowPortState": zySflowPortState,
       "zySflowMaxNumberOfPortCollectors": zySflowMaxNumberOfPortCollectors,
       "zyxelSflowPortCollectorTable": zyxelSflowPortCollectorTable,
       "zyxelSflowPortCollectorEntry": zyxelSflowPortCollectorEntry,
       "zySflowPortCollectorIpAddressType": zySflowPortCollectorIpAddressType,
       "zySflowPortCollectorIpAddress": zySflowPortCollectorIpAddress,
       "zySflowPortCollectorSampleRate": zySflowPortCollectorSampleRate,
       "zySflowPortCollectorPollInterval": zySflowPortCollectorPollInterval,
       "zySflowPortCollectorRowStatus": zySflowPortCollectorRowStatus}
)
