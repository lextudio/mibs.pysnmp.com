# SNMP MIB module (ECHANNEL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ECHANNEL
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:25 2024
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

(xylanVportArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanVportArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VirtualPort_ObjectIdentity = ObjectIdentity
virtualPort = _VirtualPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 1)
)
_LogicalPort_ObjectIdentity = ObjectIdentity
logicalPort = _LogicalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 2)
)
_PhysicalPort_ObjectIdentity = ObjectIdentity
physicalPort = _PhysicalPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 3)
)
_MirrorPort_ObjectIdentity = ObjectIdentity
mirrorPort = _MirrorPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 4)
)
_EchannelPort_ObjectIdentity = ObjectIdentity
echannelPort = _EchannelPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5)
)
_EthChnlPriPortTable_Object = MibTable
ethChnlPriPortTable = _EthChnlPriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    ethChnlPriPortTable.setStatus("mandatory")
_EthChnlPriPortEntry_Object = MibTableRow
ethChnlPriPortEntry = _EthChnlPriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 1, 1)
)
ethChnlPriPortEntry.setIndexNames(
    (0, "ECHANNEL", "ethChannelId"),
)
if mibBuilder.loadTexts:
    ethChnlPriPortEntry.setStatus("mandatory")


class _EthChannelId_Type(Integer32):
    """Custom type ethChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_EthChannelId_Type.__name__ = "Integer32"
_EthChannelId_Object = MibTableColumn
ethChannelId = _EthChannelId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 1, 1, 1),
    _EthChannelId_Type()
)
ethChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethChannelId.setStatus("mandatory")


class _PriPortSlot_Type(Integer32):
    """Custom type priPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_PriPortSlot_Type.__name__ = "Integer32"
_PriPortSlot_Object = MibTableColumn
priPortSlot = _PriPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 1, 1, 2),
    _PriPortSlot_Type()
)
priPortSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priPortSlot.setStatus("mandatory")


class _PriPortPhysIntf_Type(Integer32):
    """Custom type priPortPhysIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_PriPortPhysIntf_Type.__name__ = "Integer32"
_PriPortPhysIntf_Object = MibTableColumn
priPortPhysIntf = _PriPortPhysIntf_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 1, 1, 3),
    _PriPortPhysIntf_Type()
)
priPortPhysIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priPortPhysIntf.setStatus("mandatory")


class _AdminStatus_Type(Integer32):
    """Custom type adminStatus based on Integer32"""
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


_AdminStatus_Type.__name__ = "Integer32"
_AdminStatus_Object = MibTableColumn
adminStatus = _AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 1, 1, 4),
    _AdminStatus_Type()
)
adminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminStatus.setStatus("mandatory")
_EthChnlSecPortTable_Object = MibTable
ethChnlSecPortTable = _EthChnlSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    ethChnlSecPortTable.setStatus("mandatory")
_EthChnlSecPortEntry_Object = MibTableRow
ethChnlSecPortEntry = _EthChnlSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 2, 1)
)
ethChnlSecPortEntry.setIndexNames(
    (0, "ECHANNEL", "secethChannelId"),
    (0, "ECHANNEL", "secPortSlot"),
    (0, "ECHANNEL", "secPortPhysIntf"),
)
if mibBuilder.loadTexts:
    ethChnlSecPortEntry.setStatus("mandatory")


class _SecethChannelId_Type(Integer32):
    """Custom type secethChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SecethChannelId_Type.__name__ = "Integer32"
_SecethChannelId_Object = MibTableColumn
secethChannelId = _SecethChannelId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 2, 1, 1),
    _SecethChannelId_Type()
)
secethChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secethChannelId.setStatus("mandatory")


class _SecPortSlot_Type(Integer32):
    """Custom type secPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SecPortSlot_Type.__name__ = "Integer32"
_SecPortSlot_Object = MibTableColumn
secPortSlot = _SecPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 2, 1, 2),
    _SecPortSlot_Type()
)
secPortSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secPortSlot.setStatus("mandatory")


class _SecPortPhysIntf_Type(Integer32):
    """Custom type secPortPhysIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SecPortPhysIntf_Type.__name__ = "Integer32"
_SecPortPhysIntf_Object = MibTableColumn
secPortPhysIntf = _SecPortPhysIntf_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 2, 1, 3),
    _SecPortPhysIntf_Type()
)
secPortPhysIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secPortPhysIntf.setStatus("mandatory")


class _SecadminStatus_Type(Integer32):
    """Custom type secadminStatus based on Integer32"""
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


_SecadminStatus_Type.__name__ = "Integer32"
_SecadminStatus_Object = MibTableColumn
secadminStatus = _SecadminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 3, 5, 2, 1, 4),
    _SecadminStatus_Type()
)
secadminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secadminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECHANNEL",
    **{"virtualPort": virtualPort,
       "logicalPort": logicalPort,
       "physicalPort": physicalPort,
       "mirrorPort": mirrorPort,
       "echannelPort": echannelPort,
       "ethChnlPriPortTable": ethChnlPriPortTable,
       "ethChnlPriPortEntry": ethChnlPriPortEntry,
       "ethChannelId": ethChannelId,
       "priPortSlot": priPortSlot,
       "priPortPhysIntf": priPortPhysIntf,
       "adminStatus": adminStatus,
       "ethChnlSecPortTable": ethChnlSecPortTable,
       "ethChnlSecPortEntry": ethChnlSecPortEntry,
       "secethChannelId": secethChannelId,
       "secPortSlot": secPortSlot,
       "secPortPhysIntf": secPortPhysIntf,
       "secadminStatus": secadminStatus}
)
