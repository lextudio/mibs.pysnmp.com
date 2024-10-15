# SNMP MIB module (ELTEX-MES-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-LBD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:51 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesLbd_ObjectIdentity = ObjectIdentity
eltMesLbd = _EltMesLbd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127)
)
_EltMesLbdNotif_ObjectIdentity = ObjectIdentity
eltMesLbdNotif = _EltMesLbdNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 0)
)
_EltLbdVlanBased_Type = TruthValue
_EltLbdVlanBased_Object = MibScalar
eltLbdVlanBased = _EltLbdVlanBased_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 1),
    _EltLbdVlanBased_Type()
)
eltLbdVlanBased.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLbdVlanBased.setStatus("current")
_EltLbdVlanBasedRecoveryTime_Type = Integer32
_EltLbdVlanBasedRecoveryTime_Object = MibScalar
eltLbdVlanBasedRecoveryTime = _EltLbdVlanBasedRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 2),
    _EltLbdVlanBasedRecoveryTime_Type()
)
eltLbdVlanBasedRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLbdVlanBasedRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    eltLbdVlanBasedRecoveryTime.setUnits("seconds")
_EltLbdVlanBasedPortTable_Object = MibTable
eltLbdVlanBasedPortTable = _EltLbdVlanBasedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3)
)
if mibBuilder.loadTexts:
    eltLbdVlanBasedPortTable.setStatus("current")
_EltLbdVlanBasedPortEntry_Object = MibTableRow
eltLbdVlanBasedPortEntry = _EltLbdVlanBasedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1)
)
eltLbdVlanBasedPortEntry.setIndexNames(
    (0, "ELTEX-MES-LBD-MIB", "eltLbdVlanBasedPort"),
)
if mibBuilder.loadTexts:
    eltLbdVlanBasedPortEntry.setStatus("current")
_EltLbdVlanBasedPort_Type = InterfaceIndex
_EltLbdVlanBasedPort_Object = MibTableColumn
eltLbdVlanBasedPort = _EltLbdVlanBasedPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 1),
    _EltLbdVlanBasedPort_Type()
)
eltLbdVlanBasedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedPort.setStatus("current")


class _EltLbdVlanBasedVlanId1To1024_Type(OctetString):
    """Custom type eltLbdVlanBasedVlanId1To1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltLbdVlanBasedVlanId1To1024_Type.__name__ = "OctetString"
_EltLbdVlanBasedVlanId1To1024_Object = MibTableColumn
eltLbdVlanBasedVlanId1To1024 = _EltLbdVlanBasedVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 2),
    _EltLbdVlanBasedVlanId1To1024_Type()
)
eltLbdVlanBasedVlanId1To1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanId1To1024.setStatus("current")


class _EltLbdVlanBasedVlanId1025To2048_Type(OctetString):
    """Custom type eltLbdVlanBasedVlanId1025To2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltLbdVlanBasedVlanId1025To2048_Type.__name__ = "OctetString"
_EltLbdVlanBasedVlanId1025To2048_Object = MibTableColumn
eltLbdVlanBasedVlanId1025To2048 = _EltLbdVlanBasedVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 3),
    _EltLbdVlanBasedVlanId1025To2048_Type()
)
eltLbdVlanBasedVlanId1025To2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanId1025To2048.setStatus("current")


class _EltLbdVlanBasedVlanId2049To3072_Type(OctetString):
    """Custom type eltLbdVlanBasedVlanId2049To3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltLbdVlanBasedVlanId2049To3072_Type.__name__ = "OctetString"
_EltLbdVlanBasedVlanId2049To3072_Object = MibTableColumn
eltLbdVlanBasedVlanId2049To3072 = _EltLbdVlanBasedVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 4),
    _EltLbdVlanBasedVlanId2049To3072_Type()
)
eltLbdVlanBasedVlanId2049To3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanId2049To3072.setStatus("current")


class _EltLbdVlanBasedVlanId3073To4094_Type(OctetString):
    """Custom type eltLbdVlanBasedVlanId3073To4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltLbdVlanBasedVlanId3073To4094_Type.__name__ = "OctetString"
_EltLbdVlanBasedVlanId3073To4094_Object = MibTableColumn
eltLbdVlanBasedVlanId3073To4094 = _EltLbdVlanBasedVlanId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 3, 1, 5),
    _EltLbdVlanBasedVlanId3073To4094_Type()
)
eltLbdVlanBasedVlanId3073To4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanId3073To4094.setStatus("current")
_EltLbdVlanBasedVlanStateTable_Object = MibTable
eltLbdVlanBasedVlanStateTable = _EltLbdVlanBasedVlanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4)
)
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanStateTable.setStatus("current")
_EltLbdVlanBasedVlanStateEntry_Object = MibTableRow
eltLbdVlanBasedVlanStateEntry = _EltLbdVlanBasedVlanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1)
)
eltLbdVlanBasedVlanStateEntry.setIndexNames(
    (0, "ELTEX-MES-LBD-MIB", "eltLbdVlanBasedVlanStatePort"),
    (0, "ELTEX-MES-LBD-MIB", "eltLbdVlanBasedVlanStateVlan"),
)
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanStateEntry.setStatus("current")
_EltLbdVlanBasedVlanStatePort_Type = InterfaceIndex
_EltLbdVlanBasedVlanStatePort_Object = MibTableColumn
eltLbdVlanBasedVlanStatePort = _EltLbdVlanBasedVlanStatePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1, 1),
    _EltLbdVlanBasedVlanStatePort_Type()
)
eltLbdVlanBasedVlanStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanStatePort.setStatus("current")
_EltLbdVlanBasedVlanStateVlan_Type = VlanIndex
_EltLbdVlanBasedVlanStateVlan_Object = MibTableColumn
eltLbdVlanBasedVlanStateVlan = _EltLbdVlanBasedVlanStateVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1, 2),
    _EltLbdVlanBasedVlanStateVlan_Type()
)
eltLbdVlanBasedVlanStateVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanStateVlan.setStatus("current")


class _EltLbdVlanBasedVlanState_Type(Integer32):
    """Custom type eltLbdVlanBasedVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("blocked", 2))
    )


_EltLbdVlanBasedVlanState_Type.__name__ = "Integer32"
_EltLbdVlanBasedVlanState_Object = MibTableColumn
eltLbdVlanBasedVlanState = _EltLbdVlanBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 4, 1, 3),
    _EltLbdVlanBasedVlanState_Type()
)
eltLbdVlanBasedVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanState.setStatus("current")

# Managed Objects groups


# Notification objects

eltLbdVlanBasedVlanNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 127, 0, 1)
)
eltLbdVlanBasedVlanNotif.setObjects(
    ("ELTEX-MES-LBD-MIB", "eltLbdVlanBasedVlanState")
)
if mibBuilder.loadTexts:
    eltLbdVlanBasedVlanNotif.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-LBD-MIB",
    **{"eltMesLbd": eltMesLbd,
       "eltMesLbdNotif": eltMesLbdNotif,
       "eltLbdVlanBasedVlanNotif": eltLbdVlanBasedVlanNotif,
       "eltLbdVlanBased": eltLbdVlanBased,
       "eltLbdVlanBasedRecoveryTime": eltLbdVlanBasedRecoveryTime,
       "eltLbdVlanBasedPortTable": eltLbdVlanBasedPortTable,
       "eltLbdVlanBasedPortEntry": eltLbdVlanBasedPortEntry,
       "eltLbdVlanBasedPort": eltLbdVlanBasedPort,
       "eltLbdVlanBasedVlanId1To1024": eltLbdVlanBasedVlanId1To1024,
       "eltLbdVlanBasedVlanId1025To2048": eltLbdVlanBasedVlanId1025To2048,
       "eltLbdVlanBasedVlanId2049To3072": eltLbdVlanBasedVlanId2049To3072,
       "eltLbdVlanBasedVlanId3073To4094": eltLbdVlanBasedVlanId3073To4094,
       "eltLbdVlanBasedVlanStateTable": eltLbdVlanBasedVlanStateTable,
       "eltLbdVlanBasedVlanStateEntry": eltLbdVlanBasedVlanStateEntry,
       "eltLbdVlanBasedVlanStatePort": eltLbdVlanBasedVlanStatePort,
       "eltLbdVlanBasedVlanStateVlan": eltLbdVlanBasedVlanStateVlan,
       "eltLbdVlanBasedVlanState": eltLbdVlanBasedVlanState}
)
