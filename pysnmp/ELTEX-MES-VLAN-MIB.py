# SNMP MIB module (ELTEX-MES-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:07 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(PortList,
 VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qVlanIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

(vlanMulticastTvEntry,) = mibBuilder.importSymbols(
    "RADLAN-vlan-MIB",
    "vlanMulticastTvEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5)
)
eltMesVlan.setRevisions(
        ("2013-11-18 00:00",
         "2013-11-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltVlanMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("tr101", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltVlanMulticastTvTable_Object = MibTable
eltVlanMulticastTvTable = _EltVlanMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1)
)
if mibBuilder.loadTexts:
    eltVlanMulticastTvTable.setStatus("current")
_EltVlanMulticastTvEntry_Object = MibTableRow
eltVlanMulticastTvEntry = _EltVlanMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1, 1)
)
if mibBuilder.loadTexts:
    eltVlanMulticastTvEntry.setStatus("current")
_EltVlanMulticastTvVIDIsTagged_Type = TruthValue
_EltVlanMulticastTvVIDIsTagged_Object = MibTableColumn
eltVlanMulticastTvVIDIsTagged = _EltVlanMulticastTvVIDIsTagged_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 1, 1, 1),
    _EltVlanMulticastTvVIDIsTagged_Type()
)
eltVlanMulticastTvVIDIsTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltVlanMulticastTvVIDIsTagged.setStatus("current")
_EltVlanMode_Type = EltVlanMode
_EltVlanMode_Object = MibScalar
eltVlanMode = _EltVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 2),
    _EltVlanMode_Type()
)
eltVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltVlanMode.setStatus("current")
_Eltdot1qPortVlanCurrentTable_Object = MibTable
eltdot1qPortVlanCurrentTable = _Eltdot1qPortVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3)
)
if mibBuilder.loadTexts:
    eltdot1qPortVlanCurrentTable.setStatus("current")
_Eltdot1qPortVlanCurrentEntry_Object = MibTableRow
eltdot1qPortVlanCurrentEntry = _Eltdot1qPortVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1)
)
eltdot1qPortVlanCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltdot1qPortVlanCurrentEntry.setStatus("current")


class _Eltdot1qPortVlanCurrentEgressList1to1024_Type(OctetString):
    """Custom type eltdot1qPortVlanCurrentEgressList1to1024 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1qPortVlanCurrentEgressList1to1024_Type.__name__ = "OctetString"
_Eltdot1qPortVlanCurrentEgressList1to1024_Object = MibTableColumn
eltdot1qPortVlanCurrentEgressList1to1024 = _Eltdot1qPortVlanCurrentEgressList1to1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 1),
    _Eltdot1qPortVlanCurrentEgressList1to1024_Type()
)
eltdot1qPortVlanCurrentEgressList1to1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1qPortVlanCurrentEgressList1to1024.setStatus("current")


class _Eltdot1qPortVlanCurrentEgressList1025to2048_Type(OctetString):
    """Custom type eltdot1qPortVlanCurrentEgressList1025to2048 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1qPortVlanCurrentEgressList1025to2048_Type.__name__ = "OctetString"
_Eltdot1qPortVlanCurrentEgressList1025to2048_Object = MibTableColumn
eltdot1qPortVlanCurrentEgressList1025to2048 = _Eltdot1qPortVlanCurrentEgressList1025to2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 2),
    _Eltdot1qPortVlanCurrentEgressList1025to2048_Type()
)
eltdot1qPortVlanCurrentEgressList1025to2048.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1qPortVlanCurrentEgressList1025to2048.setStatus("current")


class _Eltdot1qPortVlanCurrentEgressList2049to3072_Type(OctetString):
    """Custom type eltdot1qPortVlanCurrentEgressList2049to3072 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1qPortVlanCurrentEgressList2049to3072_Type.__name__ = "OctetString"
_Eltdot1qPortVlanCurrentEgressList2049to3072_Object = MibTableColumn
eltdot1qPortVlanCurrentEgressList2049to3072 = _Eltdot1qPortVlanCurrentEgressList2049to3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 3),
    _Eltdot1qPortVlanCurrentEgressList2049to3072_Type()
)
eltdot1qPortVlanCurrentEgressList2049to3072.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1qPortVlanCurrentEgressList2049to3072.setStatus("current")


class _Eltdot1qPortVlanCurrentEgressList3073to4094_Type(OctetString):
    """Custom type eltdot1qPortVlanCurrentEgressList3073to4094 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Eltdot1qPortVlanCurrentEgressList3073to4094_Type.__name__ = "OctetString"
_Eltdot1qPortVlanCurrentEgressList3073to4094_Object = MibTableColumn
eltdot1qPortVlanCurrentEgressList3073to4094 = _Eltdot1qPortVlanCurrentEgressList3073to4094_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 5, 3, 1, 4),
    _Eltdot1qPortVlanCurrentEgressList3073to4094_Type()
)
eltdot1qPortVlanCurrentEgressList3073to4094.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1qPortVlanCurrentEgressList3073to4094.setStatus("current")
vlanMulticastTvEntry.registerAugmentions(
    ("ELTEX-MES-VLAN-MIB",
     "eltVlanMulticastTvEntry")
)
eltVlanMulticastTvEntry.setIndexNames(*vlanMulticastTvEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-VLAN-MIB",
    **{"EltVlanMode": EltVlanMode,
       "eltMesVlan": eltMesVlan,
       "eltVlanMulticastTvTable": eltVlanMulticastTvTable,
       "eltVlanMulticastTvEntry": eltVlanMulticastTvEntry,
       "eltVlanMulticastTvVIDIsTagged": eltVlanMulticastTvVIDIsTagged,
       "eltVlanMode": eltVlanMode,
       "eltdot1qPortVlanCurrentTable": eltdot1qPortVlanCurrentTable,
       "eltdot1qPortVlanCurrentEntry": eltdot1qPortVlanCurrentEntry,
       "eltdot1qPortVlanCurrentEgressList1to1024": eltdot1qPortVlanCurrentEgressList1to1024,
       "eltdot1qPortVlanCurrentEgressList1025to2048": eltdot1qPortVlanCurrentEgressList1025to2048,
       "eltdot1qPortVlanCurrentEgressList2049to3072": eltdot1qPortVlanCurrentEgressList2049to3072,
       "eltdot1qPortVlanCurrentEgressList3073to4094": eltdot1qPortVlanCurrentEgressList3073to4094}
)
