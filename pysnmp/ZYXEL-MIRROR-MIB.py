# SNMP MIB module (ZYXEL-MIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MIRROR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:20 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMirror = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMirrorSetup_ObjectIdentity = ObjectIdentity
zyxelMirrorSetup = _ZyxelMirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1)
)
_ZyMirrorState_Type = EnabledStatus
_ZyMirrorState_Object = MibScalar
zyMirrorState = _ZyMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 1),
    _ZyMirrorState_Type()
)
zyMirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMirrorState.setStatus("current")
_ZyMirrorMonitorPort_Type = Integer32
_ZyMirrorMonitorPort_Object = MibScalar
zyMirrorMonitorPort = _ZyMirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 2),
    _ZyMirrorMonitorPort_Type()
)
zyMirrorMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMirrorMonitorPort.setStatus("current")
_ZyxelMirrorTable_Object = MibTable
zyxelMirrorTable = _ZyxelMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelMirrorTable.setStatus("current")
_ZyxelMirrorEntry_Object = MibTableRow
zyxelMirrorEntry = _ZyxelMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1)
)
zyxelMirrorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMirrorEntry.setStatus("current")
_ZyMirrorMirroredState_Type = EnabledStatus
_ZyMirrorMirroredState_Object = MibTableColumn
zyMirrorMirroredState = _ZyMirrorMirroredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1, 1),
    _ZyMirrorMirroredState_Type()
)
zyMirrorMirroredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMirrorMirroredState.setStatus("current")


class _ZyMirrorDirection_Type(Integer32):
    """Custom type zyMirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("egress", 1),
          ("ingress", 0))
    )


_ZyMirrorDirection_Type.__name__ = "Integer32"
_ZyMirrorDirection_Object = MibTableColumn
zyMirrorDirection = _ZyMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 65, 1, 3, 1, 2),
    _ZyMirrorDirection_Type()
)
zyMirrorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMirrorDirection.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MIRROR-MIB",
    **{"zyxelMirror": zyxelMirror,
       "zyxelMirrorSetup": zyxelMirrorSetup,
       "zyMirrorState": zyMirrorState,
       "zyMirrorMonitorPort": zyMirrorMonitorPort,
       "zyxelMirrorTable": zyxelMirrorTable,
       "zyxelMirrorEntry": zyxelMirrorEntry,
       "zyMirrorMirroredState": zyMirrorMirroredState,
       "zyMirrorDirection": zyMirrorDirection}
)
