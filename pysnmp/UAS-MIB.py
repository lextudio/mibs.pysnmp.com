# SNMP MIB module (UAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:12 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

zxUasMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxUas_ObjectIdentity = ObjectIdentity
zxUas = _ZxUas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006)
)
_ZxUasMibObjects_ObjectIdentity = ObjectIdentity
zxUasMibObjects = _ZxUasMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1)
)
_ZxUasSystemGroup_ObjectIdentity = ObjectIdentity
zxUasSystemGroup = _ZxUasSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 1)
)
_ZxUasServiceMgmtGroup_ObjectIdentity = ObjectIdentity
zxUasServiceMgmtGroup = _ZxUasServiceMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2)
)
_ZxUasInterfaceIPPoolTable_Object = MibTable
zxUasInterfaceIPPoolTable = _ZxUasInterfaceIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxUasInterfaceIPPoolTable.setStatus("current")
_ZxUasInterfaceIPPoolEntry_Object = MibTableRow
zxUasInterfaceIPPoolEntry = _ZxUasInterfaceIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1)
)
zxUasInterfaceIPPoolEntry.setIndexNames(
    (0, "UAS-MIB", "zxUasIPPoolName"),
    (0, "UAS-MIB", "zxUasIPPoolVirtualRouteField"),
    (0, "UAS-MIB", "zxUasIPPoolInterfaceName"),
    (0, "UAS-MIB", "zxUasIPPoolID"),
    (0, "UAS-MIB", "zxUasIPPoolStartIPAddr"),
    (0, "UAS-MIB", "zxUasIPPoolEndIPAddr"),
)
if mibBuilder.loadTexts:
    zxUasInterfaceIPPoolEntry.setStatus("current")


class _ZxUasIPPoolName_Type(DisplayString):
    """Custom type zxUasIPPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxUasIPPoolName_Type.__name__ = "DisplayString"
_ZxUasIPPoolName_Object = MibTableColumn
zxUasIPPoolName = _ZxUasIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 1),
    _ZxUasIPPoolName_Type()
)
zxUasIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolName.setStatus("current")


class _ZxUasIPPoolVirtualRouteField_Type(DisplayString):
    """Custom type zxUasIPPoolVirtualRouteField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ZxUasIPPoolVirtualRouteField_Type.__name__ = "DisplayString"
_ZxUasIPPoolVirtualRouteField_Object = MibTableColumn
zxUasIPPoolVirtualRouteField = _ZxUasIPPoolVirtualRouteField_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 2),
    _ZxUasIPPoolVirtualRouteField_Type()
)
zxUasIPPoolVirtualRouteField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolVirtualRouteField.setStatus("current")


class _ZxUasIPPoolInterfaceName_Type(DisplayString):
    """Custom type zxUasIPPoolInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxUasIPPoolInterfaceName_Type.__name__ = "DisplayString"
_ZxUasIPPoolInterfaceName_Object = MibTableColumn
zxUasIPPoolInterfaceName = _ZxUasIPPoolInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 3),
    _ZxUasIPPoolInterfaceName_Type()
)
zxUasIPPoolInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolInterfaceName.setStatus("current")
_ZxUasIPPoolID_Type = Integer32
_ZxUasIPPoolID_Object = MibTableColumn
zxUasIPPoolID = _ZxUasIPPoolID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 4),
    _ZxUasIPPoolID_Type()
)
zxUasIPPoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolID.setStatus("current")
_ZxUasIPPoolStartIPAddr_Type = IpAddress
_ZxUasIPPoolStartIPAddr_Object = MibTableColumn
zxUasIPPoolStartIPAddr = _ZxUasIPPoolStartIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 5),
    _ZxUasIPPoolStartIPAddr_Type()
)
zxUasIPPoolStartIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolStartIPAddr.setStatus("current")
_ZxUasIPPoolEndIPAddr_Type = IpAddress
_ZxUasIPPoolEndIPAddr_Object = MibTableColumn
zxUasIPPoolEndIPAddr = _ZxUasIPPoolEndIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 6),
    _ZxUasIPPoolEndIPAddr_Type()
)
zxUasIPPoolEndIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolEndIPAddr.setStatus("current")


class _ZxUasIPPoolFreeIPNum_Type(Integer32):
    """Custom type zxUasIPPoolFreeIPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ZxUasIPPoolFreeIPNum_Type.__name__ = "Integer32"
_ZxUasIPPoolFreeIPNum_Object = MibTableColumn
zxUasIPPoolFreeIPNum = _ZxUasIPPoolFreeIPNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 7),
    _ZxUasIPPoolFreeIPNum_Type()
)
zxUasIPPoolFreeIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolFreeIPNum.setStatus("current")


class _ZxUasIPPoolUsedIPNum_Type(Integer32):
    """Custom type zxUasIPPoolUsedIPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ZxUasIPPoolUsedIPNum_Type.__name__ = "Integer32"
_ZxUasIPPoolUsedIPNum_Object = MibTableColumn
zxUasIPPoolUsedIPNum = _ZxUasIPPoolUsedIPNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 8),
    _ZxUasIPPoolUsedIPNum_Type()
)
zxUasIPPoolUsedIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolUsedIPNum.setStatus("current")


class _ZxUasIPPoolUnavailableIPNum_Type(Integer32):
    """Custom type zxUasIPPoolUnavailableIPNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ZxUasIPPoolUnavailableIPNum_Type.__name__ = "Integer32"
_ZxUasIPPoolUnavailableIPNum_Object = MibTableColumn
zxUasIPPoolUnavailableIPNum = _ZxUasIPPoolUnavailableIPNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 9),
    _ZxUasIPPoolUnavailableIPNum_Type()
)
zxUasIPPoolUnavailableIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolUnavailableIPNum.setStatus("current")


class _ZxUasIPPoolBindToDomainFlag_Type(Integer32):
    """Custom type zxUasIPPoolBindToDomainFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 2),
          ("unreserved", 1))
    )


_ZxUasIPPoolBindToDomainFlag_Type.__name__ = "Integer32"
_ZxUasIPPoolBindToDomainFlag_Object = MibTableColumn
zxUasIPPoolBindToDomainFlag = _ZxUasIPPoolBindToDomainFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 1, 1, 10),
    _ZxUasIPPoolBindToDomainFlag_Type()
)
zxUasIPPoolBindToDomainFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasIPPoolBindToDomainFlag.setStatus("current")
_ZxUasActiveSubscriberTable_Object = MibTable
zxUasActiveSubscriberTable = _ZxUasActiveSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxUasActiveSubscriberTable.setStatus("current")
_ZxUasActiveSubscriberEntry_Object = MibTableRow
zxUasActiveSubscriberEntry = _ZxUasActiveSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1)
)
zxUasActiveSubscriberEntry.setIndexNames(
    (0, "UAS-MIB", "zxUasActiveSubscriberVirtualRouteField"),
    (0, "UAS-MIB", "zxUasActiveSubscriberIPAddr"),
    (0, "UAS-MIB", "zxUasActiveSubscriberType"),
    (0, "UAS-MIB", "zxUasActiveSubscriberPPPID"),
)
if mibBuilder.loadTexts:
    zxUasActiveSubscriberEntry.setStatus("current")


class _ZxUasActiveSubscriberVirtualRouteField_Type(DisplayString):
    """Custom type zxUasActiveSubscriberVirtualRouteField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ZxUasActiveSubscriberVirtualRouteField_Type.__name__ = "DisplayString"
_ZxUasActiveSubscriberVirtualRouteField_Object = MibTableColumn
zxUasActiveSubscriberVirtualRouteField = _ZxUasActiveSubscriberVirtualRouteField_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 1),
    _ZxUasActiveSubscriberVirtualRouteField_Type()
)
zxUasActiveSubscriberVirtualRouteField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberVirtualRouteField.setStatus("current")
_ZxUasActiveSubscriberIPAddr_Type = IpAddress
_ZxUasActiveSubscriberIPAddr_Object = MibTableColumn
zxUasActiveSubscriberIPAddr = _ZxUasActiveSubscriberIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 2),
    _ZxUasActiveSubscriberIPAddr_Type()
)
zxUasActiveSubscriberIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberIPAddr.setStatus("current")


class _ZxUasActiveSubscriberType_Type(Integer32):
    """Custom type zxUasActiveSubscriberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("brg", 8),
          ("ipdhcp", 2),
          ("ipdhcprelay", 4),
          ("iphost", 5),
          ("ppp", 1),
          ("remotedhcp", 3),
          ("remotehost", 6),
          ("vpn", 7))
    )


_ZxUasActiveSubscriberType_Type.__name__ = "Integer32"
_ZxUasActiveSubscriberType_Object = MibTableColumn
zxUasActiveSubscriberType = _ZxUasActiveSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 3),
    _ZxUasActiveSubscriberType_Type()
)
zxUasActiveSubscriberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberType.setStatus("current")
_ZxUasActiveSubscriberPPPID_Type = Integer32
_ZxUasActiveSubscriberPPPID_Object = MibTableColumn
zxUasActiveSubscriberPPPID = _ZxUasActiveSubscriberPPPID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 4),
    _ZxUasActiveSubscriberPPPID_Type()
)
zxUasActiveSubscriberPPPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberPPPID.setStatus("current")


class _ZxUasActiveSubscriberName_Type(DisplayString):
    """Custom type zxUasActiveSubscriberName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ZxUasActiveSubscriberName_Type.__name__ = "DisplayString"
_ZxUasActiveSubscriberName_Object = MibTableColumn
zxUasActiveSubscriberName = _ZxUasActiveSubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 5),
    _ZxUasActiveSubscriberName_Type()
)
zxUasActiveSubscriberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberName.setStatus("current")


class _ZxUasActiveSubscriberInterfaceName_Type(DisplayString):
    """Custom type zxUasActiveSubscriberInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxUasActiveSubscriberInterfaceName_Type.__name__ = "DisplayString"
_ZxUasActiveSubscriberInterfaceName_Object = MibTableColumn
zxUasActiveSubscriberInterfaceName = _ZxUasActiveSubscriberInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 6),
    _ZxUasActiveSubscriberInterfaceName_Type()
)
zxUasActiveSubscriberInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberInterfaceName.setStatus("current")
_ZxUasActiveSubscriberDoaminID_Type = Integer32
_ZxUasActiveSubscriberDoaminID_Object = MibTableColumn
zxUasActiveSubscriberDoaminID = _ZxUasActiveSubscriberDoaminID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 7),
    _ZxUasActiveSubscriberDoaminID_Type()
)
zxUasActiveSubscriberDoaminID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberDoaminID.setStatus("current")
_ZxUasActiveSubscriberSlot_Type = Integer32
_ZxUasActiveSubscriberSlot_Object = MibTableColumn
zxUasActiveSubscriberSlot = _ZxUasActiveSubscriberSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 8),
    _ZxUasActiveSubscriberSlot_Type()
)
zxUasActiveSubscriberSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberSlot.setStatus("current")
_ZxUasActiveSubscriberPort_Type = Integer32
_ZxUasActiveSubscriberPort_Object = MibTableColumn
zxUasActiveSubscriberPort = _ZxUasActiveSubscriberPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 9),
    _ZxUasActiveSubscriberPort_Type()
)
zxUasActiveSubscriberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberPort.setStatus("current")
_ZxUasActiveSubscriberVlanId_Type = Integer32
_ZxUasActiveSubscriberVlanId_Object = MibTableColumn
zxUasActiveSubscriberVlanId = _ZxUasActiveSubscriberVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 10),
    _ZxUasActiveSubscriberVlanId_Type()
)
zxUasActiveSubscriberVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberVlanId.setStatus("current")
_ZxUasActiveSubscriberVpi_Type = Integer32
_ZxUasActiveSubscriberVpi_Object = MibTableColumn
zxUasActiveSubscriberVpi = _ZxUasActiveSubscriberVpi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 11),
    _ZxUasActiveSubscriberVpi_Type()
)
zxUasActiveSubscriberVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberVpi.setStatus("current")
_ZxUasActiveSubscriberVci_Type = Integer32
_ZxUasActiveSubscriberVci_Object = MibTableColumn
zxUasActiveSubscriberVci = _ZxUasActiveSubscriberVci_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 12),
    _ZxUasActiveSubscriberVci_Type()
)
zxUasActiveSubscriberVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberVci.setStatus("current")
_ZxUasActiveSubscriberMACAddr_Type = PhysAddress
_ZxUasActiveSubscriberMACAddr_Object = MibTableColumn
zxUasActiveSubscriberMACAddr = _ZxUasActiveSubscriberMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 13),
    _ZxUasActiveSubscriberMACAddr_Type()
)
zxUasActiveSubscriberMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberMACAddr.setStatus("current")
_ZxUasActiveSubscriberUpOctets_Type = Counter32
_ZxUasActiveSubscriberUpOctets_Object = MibTableColumn
zxUasActiveSubscriberUpOctets = _ZxUasActiveSubscriberUpOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 14),
    _ZxUasActiveSubscriberUpOctets_Type()
)
zxUasActiveSubscriberUpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberUpOctets.setStatus("current")
_ZxUasActiveSubscriberUpGigaOctets_Type = Counter32
_ZxUasActiveSubscriberUpGigaOctets_Object = MibTableColumn
zxUasActiveSubscriberUpGigaOctets = _ZxUasActiveSubscriberUpGigaOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 15),
    _ZxUasActiveSubscriberUpGigaOctets_Type()
)
zxUasActiveSubscriberUpGigaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberUpGigaOctets.setStatus("current")
_ZxUasActiveSubscriberDownOctets_Type = Counter32
_ZxUasActiveSubscriberDownOctets_Object = MibTableColumn
zxUasActiveSubscriberDownOctets = _ZxUasActiveSubscriberDownOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 16),
    _ZxUasActiveSubscriberDownOctets_Type()
)
zxUasActiveSubscriberDownOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberDownOctets.setStatus("current")
_ZxUasActiveSubscriberDownGigaOctets_Type = Counter32
_ZxUasActiveSubscriberDownGigaOctets_Object = MibTableColumn
zxUasActiveSubscriberDownGigaOctets = _ZxUasActiveSubscriberDownGigaOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 17),
    _ZxUasActiveSubscriberDownGigaOctets_Type()
)
zxUasActiveSubscriberDownGigaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberDownGigaOctets.setStatus("current")
_ZxUasActiveDhcpSubscriberAuthFlag_Type = Integer32
_ZxUasActiveDhcpSubscriberAuthFlag_Object = MibTableColumn
zxUasActiveDhcpSubscriberAuthFlag = _ZxUasActiveDhcpSubscriberAuthFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 18),
    _ZxUasActiveDhcpSubscriberAuthFlag_Type()
)
zxUasActiveDhcpSubscriberAuthFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveDhcpSubscriberAuthFlag.setStatus("current")
_ZxUasActiveSubscriberUpTime_Type = TimeTicks
_ZxUasActiveSubscriberUpTime_Object = MibTableColumn
zxUasActiveSubscriberUpTime = _ZxUasActiveSubscriberUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 2, 1, 19),
    _ZxUasActiveSubscriberUpTime_Type()
)
zxUasActiveSubscriberUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberUpTime.setStatus("current")


class _ZxUasTail_Type(Integer32):
    """Custom type zxUasTail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_ZxUasTail_Type.__name__ = "Integer32"
_ZxUasTail_Object = MibScalar
zxUasTail = _ZxUasTail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 2, 3),
    _ZxUasTail_Type()
)
zxUasTail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxUasTail.setStatus("current")
_ZxUasStaticsGroup_ObjectIdentity = ObjectIdentity
zxUasStaticsGroup = _ZxUasStaticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3)
)
_ZxUasPppStatics_ObjectIdentity = ObjectIdentity
zxUasPppStatics = _ZxUasPppStatics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1)
)
_ZxUasPppCallCount_Type = Counter32
_ZxUasPppCallCount_Object = MibScalar
zxUasPppCallCount = _ZxUasPppCallCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 1),
    _ZxUasPppCallCount_Type()
)
zxUasPppCallCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasPppCallCount.setStatus("current")
_ZxUasPppCallFailedCount_Type = Counter32
_ZxUasPppCallFailedCount_Object = MibScalar
zxUasPppCallFailedCount = _ZxUasPppCallFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 2),
    _ZxUasPppCallFailedCount_Type()
)
zxUasPppCallFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasPppCallFailedCount.setStatus("current")
_ZxUasPppLinkBreakFailedCount_Type = Counter32
_ZxUasPppLinkBreakFailedCount_Object = MibScalar
zxUasPppLinkBreakFailedCount = _ZxUasPppLinkBreakFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 3),
    _ZxUasPppLinkBreakFailedCount_Type()
)
zxUasPppLinkBreakFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasPppLinkBreakFailedCount.setStatus("current")
_ZxUasPppAbnormalCloseCount_Type = Counter32
_ZxUasPppAbnormalCloseCount_Object = MibScalar
zxUasPppAbnormalCloseCount = _ZxUasPppAbnormalCloseCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 1, 4),
    _ZxUasPppAbnormalCloseCount_Type()
)
zxUasPppAbnormalCloseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasPppAbnormalCloseCount.setStatus("current")
_ZxUasActiveSubscriberStaticsTable_Object = MibTable
zxUasActiveSubscriberStaticsTable = _ZxUasActiveSubscriberStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxUasActiveSubscriberStaticsTable.setStatus("current")
_ZxUasActiveSubscriberStaticsEntry_Object = MibTableRow
zxUasActiveSubscriberStaticsEntry = _ZxUasActiveSubscriberStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 2, 1)
)
zxUasActiveSubscriberStaticsEntry.setIndexNames(
    (0, "UAS-MIB", "zxUasActiveSubscriberType"),
)
if mibBuilder.loadTexts:
    zxUasActiveSubscriberStaticsEntry.setStatus("current")
_ZxUasActiveSubscriberNum_Type = Integer32
_ZxUasActiveSubscriberNum_Object = MibTableColumn
zxUasActiveSubscriberNum = _ZxUasActiveSubscriberNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 2, 1, 1),
    _ZxUasActiveSubscriberNum_Type()
)
zxUasActiveSubscriberNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasActiveSubscriberNum.setStatus("current")
_ZxUasMaxSubscriberOnlineCount_Type = Integer32
_ZxUasMaxSubscriberOnlineCount_Object = MibScalar
zxUasMaxSubscriberOnlineCount = _ZxUasMaxSubscriberOnlineCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 3),
    _ZxUasMaxSubscriberOnlineCount_Type()
)
zxUasMaxSubscriberOnlineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasMaxSubscriberOnlineCount.setStatus("current")


class _ZxUasMaxSubscriberOnlineClear_Type(Integer32):
    """Custom type zxUasMaxSubscriberOnlineClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("normal", 0))
    )


_ZxUasMaxSubscriberOnlineClear_Type.__name__ = "Integer32"
_ZxUasMaxSubscriberOnlineClear_Object = MibScalar
zxUasMaxSubscriberOnlineClear = _ZxUasMaxSubscriberOnlineClear_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 4),
    _ZxUasMaxSubscriberOnlineClear_Type()
)
zxUasMaxSubscriberOnlineClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxUasMaxSubscriberOnlineClear.setStatus("current")


class _ZxUasMaxSubscriberOnlineTime_Type(DisplayString):
    """Custom type zxUasMaxSubscriberOnlineTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ZxUasMaxSubscriberOnlineTime_Type.__name__ = "DisplayString"
_ZxUasMaxSubscriberOnlineTime_Object = MibScalar
zxUasMaxSubscriberOnlineTime = _ZxUasMaxSubscriberOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 1, 3, 5),
    _ZxUasMaxSubscriberOnlineTime_Type()
)
zxUasMaxSubscriberOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxUasMaxSubscriberOnlineTime.setStatus("current")
_ZxUasTraps_ObjectIdentity = ObjectIdentity
zxUasTraps = _ZxUasTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1006, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UAS-MIB",
    **{"zte": zte,
       "zxUas": zxUas,
       "zxUasMib": zxUasMib,
       "zxUasMibObjects": zxUasMibObjects,
       "zxUasSystemGroup": zxUasSystemGroup,
       "zxUasServiceMgmtGroup": zxUasServiceMgmtGroup,
       "zxUasInterfaceIPPoolTable": zxUasInterfaceIPPoolTable,
       "zxUasInterfaceIPPoolEntry": zxUasInterfaceIPPoolEntry,
       "zxUasIPPoolName": zxUasIPPoolName,
       "zxUasIPPoolVirtualRouteField": zxUasIPPoolVirtualRouteField,
       "zxUasIPPoolInterfaceName": zxUasIPPoolInterfaceName,
       "zxUasIPPoolID": zxUasIPPoolID,
       "zxUasIPPoolStartIPAddr": zxUasIPPoolStartIPAddr,
       "zxUasIPPoolEndIPAddr": zxUasIPPoolEndIPAddr,
       "zxUasIPPoolFreeIPNum": zxUasIPPoolFreeIPNum,
       "zxUasIPPoolUsedIPNum": zxUasIPPoolUsedIPNum,
       "zxUasIPPoolUnavailableIPNum": zxUasIPPoolUnavailableIPNum,
       "zxUasIPPoolBindToDomainFlag": zxUasIPPoolBindToDomainFlag,
       "zxUasActiveSubscriberTable": zxUasActiveSubscriberTable,
       "zxUasActiveSubscriberEntry": zxUasActiveSubscriberEntry,
       "zxUasActiveSubscriberVirtualRouteField": zxUasActiveSubscriberVirtualRouteField,
       "zxUasActiveSubscriberIPAddr": zxUasActiveSubscriberIPAddr,
       "zxUasActiveSubscriberType": zxUasActiveSubscriberType,
       "zxUasActiveSubscriberPPPID": zxUasActiveSubscriberPPPID,
       "zxUasActiveSubscriberName": zxUasActiveSubscriberName,
       "zxUasActiveSubscriberInterfaceName": zxUasActiveSubscriberInterfaceName,
       "zxUasActiveSubscriberDoaminID": zxUasActiveSubscriberDoaminID,
       "zxUasActiveSubscriberSlot": zxUasActiveSubscriberSlot,
       "zxUasActiveSubscriberPort": zxUasActiveSubscriberPort,
       "zxUasActiveSubscriberVlanId": zxUasActiveSubscriberVlanId,
       "zxUasActiveSubscriberVpi": zxUasActiveSubscriberVpi,
       "zxUasActiveSubscriberVci": zxUasActiveSubscriberVci,
       "zxUasActiveSubscriberMACAddr": zxUasActiveSubscriberMACAddr,
       "zxUasActiveSubscriberUpOctets": zxUasActiveSubscriberUpOctets,
       "zxUasActiveSubscriberUpGigaOctets": zxUasActiveSubscriberUpGigaOctets,
       "zxUasActiveSubscriberDownOctets": zxUasActiveSubscriberDownOctets,
       "zxUasActiveSubscriberDownGigaOctets": zxUasActiveSubscriberDownGigaOctets,
       "zxUasActiveDhcpSubscriberAuthFlag": zxUasActiveDhcpSubscriberAuthFlag,
       "zxUasActiveSubscriberUpTime": zxUasActiveSubscriberUpTime,
       "zxUasTail": zxUasTail,
       "zxUasStaticsGroup": zxUasStaticsGroup,
       "zxUasPppStatics": zxUasPppStatics,
       "zxUasPppCallCount": zxUasPppCallCount,
       "zxUasPppCallFailedCount": zxUasPppCallFailedCount,
       "zxUasPppLinkBreakFailedCount": zxUasPppLinkBreakFailedCount,
       "zxUasPppAbnormalCloseCount": zxUasPppAbnormalCloseCount,
       "zxUasActiveSubscriberStaticsTable": zxUasActiveSubscriberStaticsTable,
       "zxUasActiveSubscriberStaticsEntry": zxUasActiveSubscriberStaticsEntry,
       "zxUasActiveSubscriberNum": zxUasActiveSubscriberNum,
       "zxUasMaxSubscriberOnlineCount": zxUasMaxSubscriberOnlineCount,
       "zxUasMaxSubscriberOnlineClear": zxUasMaxSubscriberOnlineClear,
       "zxUasMaxSubscriberOnlineTime": zxUasMaxSubscriberOnlineTime,
       "zxUasTraps": zxUasTraps}
)
