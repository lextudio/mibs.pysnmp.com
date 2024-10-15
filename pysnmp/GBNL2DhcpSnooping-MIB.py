# SNMP MIB module (GBNL2DhcpSnooping-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNL2DhcpSnooping-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:46 2024
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

(gbnL2,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "gbnL2")

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

gbnL3DhcpSnooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5)
)
gbnL3DhcpSnooping.setRevisions(
        ("1901-05-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpsnoopingOnOff_Type = TruthValue
_DhcpsnoopingOnOff_Object = MibScalar
dhcpsnoopingOnOff = _DhcpsnoopingOnOff_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 1),
    _DhcpsnoopingOnOff_Type()
)
dhcpsnoopingOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpsnoopingOnOff.setStatus("current")
_DhcpsnoopingPortTable_Object = MibTable
dhcpsnoopingPortTable = _DhcpsnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    dhcpsnoopingPortTable.setStatus("current")
_DhcpsnoopingPortEntry_Object = MibTableRow
dhcpsnoopingPortEntry = _DhcpsnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1)
)
dhcpsnoopingPortEntry.setIndexNames(
    (0, "GBNL2DhcpSnooping-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dhcpsnoopingPortEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortTrustMode_Type(Integer32):
    """Custom type portTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_PortTrustMode_Type.__name__ = "Integer32"
_PortTrustMode_Object = MibTableColumn
portTrustMode = _PortTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 2),
    _PortTrustMode_Type()
)
portTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrustMode.setStatus("current")
_PortMaxNum_Type = Integer32
_PortMaxNum_Object = MibTableColumn
portMaxNum = _PortMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 3),
    _PortMaxNum_Type()
)
portMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMaxNum.setStatus("current")


class _PortIpSourceGuardMode_Type(Integer32):
    """Custom type portIpSourceGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_PortIpSourceGuardMode_Type.__name__ = "Integer32"
_PortIpSourceGuardMode_Object = MibTableColumn
portIpSourceGuardMode = _PortIpSourceGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 2, 1, 4),
    _PortIpSourceGuardMode_Type()
)
portIpSourceGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIpSourceGuardMode.setStatus("current")
_DhcpsnoopingVlanTable_Object = MibTable
dhcpsnoopingVlanTable = _DhcpsnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3)
)
if mibBuilder.loadTexts:
    dhcpsnoopingVlanTable.setStatus("current")
_DhcpsnoopingVlanEntry_Object = MibTableRow
dhcpsnoopingVlanEntry = _DhcpsnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3, 1)
)
dhcpsnoopingVlanEntry.setIndexNames(
    (0, "GBNL2DhcpSnooping-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpsnoopingVlanEntry.setStatus("current")


class _VlanIndex_Type(Integer32):
    """Custom type vlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanIndex_Type.__name__ = "Integer32"
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")
_VlanMaxNum_Type = Integer32
_VlanMaxNum_Object = MibTableColumn
vlanMaxNum = _VlanMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 4, 5, 3, 1, 2),
    _VlanMaxNum_Type()
)
vlanMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMaxNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNL2DhcpSnooping-MIB",
    **{"gbnL3DhcpSnooping": gbnL3DhcpSnooping,
       "dhcpsnoopingOnOff": dhcpsnoopingOnOff,
       "dhcpsnoopingPortTable": dhcpsnoopingPortTable,
       "dhcpsnoopingPortEntry": dhcpsnoopingPortEntry,
       "portIndex": portIndex,
       "portTrustMode": portTrustMode,
       "portMaxNum": portMaxNum,
       "portIpSourceGuardMode": portIpSourceGuardMode,
       "dhcpsnoopingVlanTable": dhcpsnoopingVlanTable,
       "dhcpsnoopingVlanEntry": dhcpsnoopingVlanEntry,
       "vlanIndex": vlanIndex,
       "vlanMaxNum": vlanMaxNum}
)
