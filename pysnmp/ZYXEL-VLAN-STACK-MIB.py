# SNMP MIB module (ZYXEL-VLAN-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-VLAN-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:04 2024
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

zyxelVlanStack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelVlanStackSetup_ObjectIdentity = ObjectIdentity
zyxelVlanStackSetup = _ZyxelVlanStackSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1)
)
_ZyVlanStackState_Type = EnabledStatus
_ZyVlanStackState_Object = MibScalar
zyVlanStackState = _ZyVlanStackState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 1),
    _ZyVlanStackState_Type()
)
zyVlanStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanStackState.setStatus("current")
_ZyxelVlanStackPortTable_Object = MibTable
zyxelVlanStackPortTable = _ZyxelVlanStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelVlanStackPortTable.setStatus("current")
_ZyxelVlanStackPortEntry_Object = MibTableRow
zyxelVlanStackPortEntry = _ZyxelVlanStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1)
)
zyxelVlanStackPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelVlanStackPortEntry.setStatus("current")


class _ZyVlanStackPortMode_Type(Integer32):
    """Custom type zyVlanStackPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 2),
          ("normal", 1),
          ("tunnel", 3))
    )


_ZyVlanStackPortMode_Type.__name__ = "Integer32"
_ZyVlanStackPortMode_Object = MibTableColumn
zyVlanStackPortMode = _ZyVlanStackPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 1),
    _ZyVlanStackPortMode_Type()
)
zyVlanStackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanStackPortMode.setStatus("current")
_ZyVlanStackPortVid_Type = Integer32
_ZyVlanStackPortVid_Object = MibTableColumn
zyVlanStackPortVid = _ZyVlanStackPortVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 2),
    _ZyVlanStackPortVid_Type()
)
zyVlanStackPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanStackPortVid.setStatus("current")


class _ZyVlanStackPortPriority_Type(Integer32):
    """Custom type zyVlanStackPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_ZyVlanStackPortPriority_Type.__name__ = "Integer32"
_ZyVlanStackPortPriority_Object = MibTableColumn
zyVlanStackPortPriority = _ZyVlanStackPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 3),
    _ZyVlanStackPortPriority_Type()
)
zyVlanStackPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanStackPortPriority.setStatus("current")
_ZyVlanStackTunnelPortTpid_Type = Integer32
_ZyVlanStackTunnelPortTpid_Object = MibTableColumn
zyVlanStackTunnelPortTpid = _ZyVlanStackTunnelPortTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 2, 1, 4),
    _ZyVlanStackTunnelPortTpid_Type()
)
zyVlanStackTunnelPortTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanStackTunnelPortTpid.setStatus("current")
_ZySelectiveQinQMaxNumberOfRules_Type = Integer32
_ZySelectiveQinQMaxNumberOfRules_Object = MibScalar
zySelectiveQinQMaxNumberOfRules = _ZySelectiveQinQMaxNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 3),
    _ZySelectiveQinQMaxNumberOfRules_Type()
)
zySelectiveQinQMaxNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySelectiveQinQMaxNumberOfRules.setStatus("current")
_ZyxelSelectiveQinQTable_Object = MibTable
zyxelSelectiveQinQTable = _ZyxelSelectiveQinQTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelSelectiveQinQTable.setStatus("current")
_ZyxelSelectiveQinQEntry_Object = MibTableRow
zyxelSelectiveQinQEntry = _ZyxelSelectiveQinQEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1)
)
zyxelSelectiveQinQEntry.setIndexNames(
    (0, "ZYXEL-VLAN-STACK-MIB", "zySelectiveQinQPort"),
    (0, "ZYXEL-VLAN-STACK-MIB", "zySelectiveQinQCvid"),
)
if mibBuilder.loadTexts:
    zyxelSelectiveQinQEntry.setStatus("current")
_ZySelectiveQinQName_Type = DisplayString
_ZySelectiveQinQName_Object = MibTableColumn
zySelectiveQinQName = _ZySelectiveQinQName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 1),
    _ZySelectiveQinQName_Type()
)
zySelectiveQinQName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySelectiveQinQName.setStatus("current")
_ZySelectiveQinQPort_Type = Integer32
_ZySelectiveQinQPort_Object = MibTableColumn
zySelectiveQinQPort = _ZySelectiveQinQPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 2),
    _ZySelectiveQinQPort_Type()
)
zySelectiveQinQPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySelectiveQinQPort.setStatus("current")
_ZySelectiveQinQCvid_Type = Integer32
_ZySelectiveQinQCvid_Object = MibTableColumn
zySelectiveQinQCvid = _ZySelectiveQinQCvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 3),
    _ZySelectiveQinQCvid_Type()
)
zySelectiveQinQCvid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySelectiveQinQCvid.setStatus("current")
_ZySelectiveQinQSpvid_Type = Integer32
_ZySelectiveQinQSpvid_Object = MibTableColumn
zySelectiveQinQSpvid = _ZySelectiveQinQSpvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 4),
    _ZySelectiveQinQSpvid_Type()
)
zySelectiveQinQSpvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySelectiveQinQSpvid.setStatus("current")


class _ZySelectiveQinQPriority_Type(Integer32):
    """Custom type zySelectiveQinQPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_ZySelectiveQinQPriority_Type.__name__ = "Integer32"
_ZySelectiveQinQPriority_Object = MibTableColumn
zySelectiveQinQPriority = _ZySelectiveQinQPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 5),
    _ZySelectiveQinQPriority_Type()
)
zySelectiveQinQPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySelectiveQinQPriority.setStatus("current")
_ZySelectiveQinQRowStatus_Type = RowStatus
_ZySelectiveQinQRowStatus_Object = MibTableColumn
zySelectiveQinQRowStatus = _ZySelectiveQinQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 89, 1, 4, 1, 6),
    _ZySelectiveQinQRowStatus_Type()
)
zySelectiveQinQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zySelectiveQinQRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VLAN-STACK-MIB",
    **{"zyxelVlanStack": zyxelVlanStack,
       "zyxelVlanStackSetup": zyxelVlanStackSetup,
       "zyVlanStackState": zyVlanStackState,
       "zyxelVlanStackPortTable": zyxelVlanStackPortTable,
       "zyxelVlanStackPortEntry": zyxelVlanStackPortEntry,
       "zyVlanStackPortMode": zyVlanStackPortMode,
       "zyVlanStackPortVid": zyVlanStackPortVid,
       "zyVlanStackPortPriority": zyVlanStackPortPriority,
       "zyVlanStackTunnelPortTpid": zyVlanStackTunnelPortTpid,
       "zySelectiveQinQMaxNumberOfRules": zySelectiveQinQMaxNumberOfRules,
       "zyxelSelectiveQinQTable": zyxelSelectiveQinQTable,
       "zyxelSelectiveQinQEntry": zyxelSelectiveQinQEntry,
       "zySelectiveQinQName": zySelectiveQinQName,
       "zySelectiveQinQPort": zySelectiveQinQPort,
       "zySelectiveQinQCvid": zySelectiveQinQCvid,
       "zySelectiveQinQSpvid": zySelectiveQinQSpvid,
       "zySelectiveQinQPriority": zySelectiveQinQPriority,
       "zySelectiveQinQRowStatus": zySelectiveQinQRowStatus}
)
