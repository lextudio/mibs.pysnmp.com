# SNMP MIB module (GBNL3DhcpRelay-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNL3DhcpRelay-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:51 2024
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

(gbnL3,) = mibBuilder.importSymbols(
    "GREENTECH-MASTER-MIB",
    "gbnL3")

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

gbnL3DhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5)
)
gbnL3DhcpRelay.setRevisions(
        ("1901-05-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _DhcpRelayEnableStatus_Type(Integer32):
    """Custom type dhcpRelayEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DhcpRelayEnableStatus_Type.__name__ = "Integer32"
_DhcpRelayEnableStatus_Object = MibScalar
dhcpRelayEnableStatus = _DhcpRelayEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 1),
    _DhcpRelayEnableStatus_Type()
)
dhcpRelayEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnableStatus.setStatus("current")


class _DhcpRelayDebugStatus_Type(Integer32):
    """Custom type dhcpRelayDebugStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DhcpRelayDebugStatus_Type.__name__ = "Integer32"
_DhcpRelayDebugStatus_Object = MibScalar
dhcpRelayDebugStatus = _DhcpRelayDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 2),
    _DhcpRelayDebugStatus_Type()
)
dhcpRelayDebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayDebugStatus.setStatus("obsolete")
_DhcpRelayGroupTable_Object = MibTable
dhcpRelayGroupTable = _DhcpRelayGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 3)
)
if mibBuilder.loadTexts:
    dhcpRelayGroupTable.setStatus("current")
_DhcpRelayGroupEntry_Object = MibTableRow
dhcpRelayGroupEntry = _DhcpRelayGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 3, 1)
)
dhcpRelayGroupEntry.setIndexNames(
    (0, "GBNL3DhcpRelay-MIB", "dhcpRelaySvrGroupNo"),
)
if mibBuilder.loadTexts:
    dhcpRelayGroupEntry.setStatus("current")


class _DhcpRelaySvrGroupNo_Type(Integer32):
    """Custom type dhcpRelaySvrGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DhcpRelaySvrGroupNo_Type.__name__ = "Integer32"
_DhcpRelaySvrGroupNo_Object = MibTableColumn
dhcpRelaySvrGroupNo = _DhcpRelaySvrGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 3, 1, 1),
    _DhcpRelaySvrGroupNo_Type()
)
dhcpRelaySvrGroupNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelaySvrGroupNo.setStatus("current")
_DhcpRelayServerIp_Type = IpAddress
_DhcpRelayServerIp_Object = MibTableColumn
dhcpRelayServerIp = _DhcpRelayServerIp_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 3, 1, 2),
    _DhcpRelayServerIp_Type()
)
dhcpRelayServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServerIp.setStatus("current")
_DhcpRelayIfaceTable_Object = MibTable
dhcpRelayIfaceTable = _DhcpRelayIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayIfaceTable.setStatus("current")
_DhcpRelayIfaceEntry_Object = MibTableRow
dhcpRelayIfaceEntry = _DhcpRelayIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 4, 1)
)
dhcpRelayIfaceEntry.setIndexNames(
    (0, "GBNL3DhcpRelay-MIB", "dhcpRelaySvrVlanIfaceNo"),
)
if mibBuilder.loadTexts:
    dhcpRelayIfaceEntry.setStatus("current")


class _DhcpRelaySvrVlanIfaceNo_Type(Integer32):
    """Custom type dhcpRelaySvrVlanIfaceNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DhcpRelaySvrVlanIfaceNo_Type.__name__ = "Integer32"
_DhcpRelaySvrVlanIfaceNo_Object = MibTableColumn
dhcpRelaySvrVlanIfaceNo = _DhcpRelaySvrVlanIfaceNo_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 4, 1, 1),
    _DhcpRelaySvrVlanIfaceNo_Type()
)
dhcpRelaySvrVlanIfaceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelaySvrVlanIfaceNo.setStatus("current")


class _DhcpRelayVlanIfaceGroupNo_Type(Integer32):
    """Custom type dhcpRelayVlanIfaceGroupNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DhcpRelayVlanIfaceGroupNo_Type.__name__ = "Integer32"
_DhcpRelayVlanIfaceGroupNo_Object = MibTableColumn
dhcpRelayVlanIfaceGroupNo = _DhcpRelayVlanIfaceGroupNo_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 4, 1, 2),
    _DhcpRelayVlanIfaceGroupNo_Type()
)
dhcpRelayVlanIfaceGroupNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayVlanIfaceGroupNo.setStatus("current")


class _DhcpRelayHideServerIp_Type(Integer32):
    """Custom type dhcpRelayHideServerIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DhcpRelayHideServerIp_Type.__name__ = "Integer32"
_DhcpRelayHideServerIp_Object = MibScalar
dhcpRelayHideServerIp = _DhcpRelayHideServerIp_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 5, 5, 5),
    _DhcpRelayHideServerIp_Type()
)
dhcpRelayHideServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayHideServerIp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNL3DhcpRelay-MIB",
    **{"gbnL3DhcpRelay": gbnL3DhcpRelay,
       "dhcpRelayEnableStatus": dhcpRelayEnableStatus,
       "dhcpRelayDebugStatus": dhcpRelayDebugStatus,
       "dhcpRelayGroupTable": dhcpRelayGroupTable,
       "dhcpRelayGroupEntry": dhcpRelayGroupEntry,
       "dhcpRelaySvrGroupNo": dhcpRelaySvrGroupNo,
       "dhcpRelayServerIp": dhcpRelayServerIp,
       "dhcpRelayIfaceTable": dhcpRelayIfaceTable,
       "dhcpRelayIfaceEntry": dhcpRelayIfaceEntry,
       "dhcpRelaySvrVlanIfaceNo": dhcpRelaySvrVlanIfaceNo,
       "dhcpRelayVlanIfaceGroupNo": dhcpRelayVlanIfaceGroupNo,
       "dhcpRelayHideServerIp": dhcpRelayHideServerIp}
)
