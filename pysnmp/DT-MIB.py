# SNMP MIB module (DT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:44 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpSwitchDt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27)
)
hpSwitchDt.setRevisions(
        ("2012-05-22 18:00",
         "2011-08-09 00:00",
         "2011-03-22 18:00",
         "2007-10-27 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpConfig_ObjectIdentity = ObjectIdentity
hpConfig = _HpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7)
)
_HpSwitchConfig_ObjectIdentity = ObjectIdentity
hpSwitchConfig = _HpSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1)
)


class _HpSwitchISCPortIndex_Type(Integer32):
    """Custom type hpSwitchISCPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchISCPortIndex_Type.__name__ = "Integer32"
_HpSwitchISCPortIndex_Object = MibScalar
hpSwitchISCPortIndex = _HpSwitchISCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 1),
    _HpSwitchISCPortIndex_Type()
)
hpSwitchISCPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchISCPortIndex.setStatus("current")


class _HpSwitchRemoteISCPortIndex_Type(Integer32):
    """Custom type hpSwitchRemoteISCPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchRemoteISCPortIndex_Type.__name__ = "Integer32"
_HpSwitchRemoteISCPortIndex_Object = MibScalar
hpSwitchRemoteISCPortIndex = _HpSwitchRemoteISCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 2),
    _HpSwitchRemoteISCPortIndex_Type()
)
hpSwitchRemoteISCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRemoteISCPortIndex.setStatus("current")
_HpSwitchDtLacpStatus_ObjectIdentity = ObjectIdentity
hpSwitchDtLacpStatus = _HpSwitchDtLacpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3)
)
_HpSwitchDtLacpStatusLocalTable_Object = MibTable
hpSwitchDtLacpStatusLocalTable = _HpSwitchDtLacpStatusLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1)
)
if mibBuilder.loadTexts:
    hpSwitchDtLacpStatusLocalTable.setStatus("current")
_HpSwitchDtLacpStatusLocalEntry_Object = MibTableRow
hpSwitchDtLacpStatusLocalEntry = _HpSwitchDtLacpStatusLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1)
)
hpSwitchDtLacpStatusLocalEntry.setIndexNames(
    (0, "DT-MIB", "hpSwitchDtLacpLocalIfIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchDtLacpStatusLocalEntry.setStatus("current")


class _HpSwitchDtLacpLocalIfIndex_Type(Integer32):
    """Custom type hpSwitchDtLacpLocalIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchDtLacpLocalIfIndex_Type.__name__ = "Integer32"
_HpSwitchDtLacpLocalIfIndex_Object = MibTableColumn
hpSwitchDtLacpLocalIfIndex = _HpSwitchDtLacpLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 1),
    _HpSwitchDtLacpLocalIfIndex_Type()
)
hpSwitchDtLacpLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfIndex.setStatus("current")
_HpSwitchDtLacpLocalIfName_Type = DisplayString
_HpSwitchDtLacpLocalIfName_Object = MibTableColumn
hpSwitchDtLacpLocalIfName = _HpSwitchDtLacpLocalIfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 2),
    _HpSwitchDtLacpLocalIfName_Type()
)
hpSwitchDtLacpLocalIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfName.setStatus("current")
_HpSwitchDtLacpLocalIfLacpEnable_Type = Integer32
_HpSwitchDtLacpLocalIfLacpEnable_Object = MibTableColumn
hpSwitchDtLacpLocalIfLacpEnable = _HpSwitchDtLacpLocalIfLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 3),
    _HpSwitchDtLacpLocalIfLacpEnable_Type()
)
hpSwitchDtLacpLocalIfLacpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfLacpEnable.setStatus("current")
_HpSwitchDtLacpLocalIfTrunkGroup_Type = Integer32
_HpSwitchDtLacpLocalIfTrunkGroup_Object = MibTableColumn
hpSwitchDtLacpLocalIfTrunkGroup = _HpSwitchDtLacpLocalIfTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 4),
    _HpSwitchDtLacpLocalIfTrunkGroup_Type()
)
hpSwitchDtLacpLocalIfTrunkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfTrunkGroup.setStatus("current")
_HpSwitchDtLacpLocalIfLacpPortStatus_Type = Integer32
_HpSwitchDtLacpLocalIfLacpPortStatus_Object = MibTableColumn
hpSwitchDtLacpLocalIfLacpPortStatus = _HpSwitchDtLacpLocalIfLacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 5),
    _HpSwitchDtLacpLocalIfLacpPortStatus_Type()
)
hpSwitchDtLacpLocalIfLacpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfLacpPortStatus.setStatus("current")
_HpSwitchDtLacpLocalIfLacpPartner_Type = Integer32
_HpSwitchDtLacpLocalIfLacpPartner_Object = MibTableColumn
hpSwitchDtLacpLocalIfLacpPartner = _HpSwitchDtLacpLocalIfLacpPartner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 6),
    _HpSwitchDtLacpLocalIfLacpPartner_Type()
)
hpSwitchDtLacpLocalIfLacpPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfLacpPartner.setStatus("current")
_HpSwitchDtLacpLocalIfLacpStatus_Type = Integer32
_HpSwitchDtLacpLocalIfLacpStatus_Object = MibTableColumn
hpSwitchDtLacpLocalIfLacpStatus = _HpSwitchDtLacpLocalIfLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 7),
    _HpSwitchDtLacpLocalIfLacpStatus_Type()
)
hpSwitchDtLacpLocalIfLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfLacpStatus.setStatus("current")
_HpSwitchDtLacpLocalIfLacpAdminKey_Type = Integer32
_HpSwitchDtLacpLocalIfLacpAdminKey_Object = MibTableColumn
hpSwitchDtLacpLocalIfLacpAdminKey = _HpSwitchDtLacpLocalIfLacpAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 8),
    _HpSwitchDtLacpLocalIfLacpAdminKey_Type()
)
hpSwitchDtLacpLocalIfLacpAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfLacpAdminKey.setStatus("current")
_HpSwitchDtLacpLocalIfLacpOperKey_Type = Integer32
_HpSwitchDtLacpLocalIfLacpOperKey_Object = MibTableColumn
hpSwitchDtLacpLocalIfLacpOperKey = _HpSwitchDtLacpLocalIfLacpOperKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 1, 1, 9),
    _HpSwitchDtLacpLocalIfLacpOperKey_Type()
)
hpSwitchDtLacpLocalIfLacpOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpLocalIfLacpOperKey.setStatus("current")
_HpSwitchDtLacpStatusPeerTable_Object = MibTable
hpSwitchDtLacpStatusPeerTable = _HpSwitchDtLacpStatusPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2)
)
if mibBuilder.loadTexts:
    hpSwitchDtLacpStatusPeerTable.setStatus("current")
_HpSwitchDtLacpStatusPeerEntry_Object = MibTableRow
hpSwitchDtLacpStatusPeerEntry = _HpSwitchDtLacpStatusPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1)
)
hpSwitchDtLacpStatusPeerEntry.setIndexNames(
    (0, "DT-MIB", "hpSwitchDtLacpPeerIfIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchDtLacpStatusPeerEntry.setStatus("current")


class _HpSwitchDtLacpPeerIfIndex_Type(Integer32):
    """Custom type hpSwitchDtLacpPeerIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSwitchDtLacpPeerIfIndex_Type.__name__ = "Integer32"
_HpSwitchDtLacpPeerIfIndex_Object = MibTableColumn
hpSwitchDtLacpPeerIfIndex = _HpSwitchDtLacpPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1, 1),
    _HpSwitchDtLacpPeerIfIndex_Type()
)
hpSwitchDtLacpPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpPeerIfIndex.setStatus("current")
_HpSwitchDtLacpPeerIfName_Type = DisplayString
_HpSwitchDtLacpPeerIfName_Object = MibTableColumn
hpSwitchDtLacpPeerIfName = _HpSwitchDtLacpPeerIfName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1, 2),
    _HpSwitchDtLacpPeerIfName_Type()
)
hpSwitchDtLacpPeerIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpPeerIfName.setStatus("current")
_HpSwitchDtLacpPeerIfLacpEnable_Type = Integer32
_HpSwitchDtLacpPeerIfLacpEnable_Object = MibTableColumn
hpSwitchDtLacpPeerIfLacpEnable = _HpSwitchDtLacpPeerIfLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1, 3),
    _HpSwitchDtLacpPeerIfLacpEnable_Type()
)
hpSwitchDtLacpPeerIfLacpEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpPeerIfLacpEnable.setStatus("current")
_HpSwitchDtLacpPeerIfTrunkGroup_Type = Integer32
_HpSwitchDtLacpPeerIfTrunkGroup_Object = MibTableColumn
hpSwitchDtLacpPeerIfTrunkGroup = _HpSwitchDtLacpPeerIfTrunkGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1, 4),
    _HpSwitchDtLacpPeerIfTrunkGroup_Type()
)
hpSwitchDtLacpPeerIfTrunkGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpPeerIfTrunkGroup.setStatus("current")
_HpSwitchDtLacpPeerIfLacpPortStatus_Type = Integer32
_HpSwitchDtLacpPeerIfLacpPortStatus_Object = MibTableColumn
hpSwitchDtLacpPeerIfLacpPortStatus = _HpSwitchDtLacpPeerIfLacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1, 5),
    _HpSwitchDtLacpPeerIfLacpPortStatus_Type()
)
hpSwitchDtLacpPeerIfLacpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpPeerIfLacpPortStatus.setStatus("current")
_HpSwitchDtLacpPeerIfLacpPartner_Type = Integer32
_HpSwitchDtLacpPeerIfLacpPartner_Object = MibTableColumn
hpSwitchDtLacpPeerIfLacpPartner = _HpSwitchDtLacpPeerIfLacpPartner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1, 6),
    _HpSwitchDtLacpPeerIfLacpPartner_Type()
)
hpSwitchDtLacpPeerIfLacpPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpPeerIfLacpPartner.setStatus("current")
_HpSwitchDtLacpPeerIfLacpStatus_Type = Integer32
_HpSwitchDtLacpPeerIfLacpStatus_Object = MibTableColumn
hpSwitchDtLacpPeerIfLacpStatus = _HpSwitchDtLacpPeerIfLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 3, 2, 1, 7),
    _HpSwitchDtLacpPeerIfLacpStatus_Type()
)
hpSwitchDtLacpPeerIfLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtLacpPeerIfLacpStatus.setStatus("current")
_HpSwitchDtConfig_ObjectIdentity = ObjectIdentity
hpSwitchDtConfig = _HpSwitchDtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4)
)
_HpSwitchDtPeerKeepAliveConfig_ObjectIdentity = ObjectIdentity
hpSwitchDtPeerKeepAliveConfig = _HpSwitchDtPeerKeepAliveConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1)
)
_HpSwitchDtPeerKeepAliveDestAddressType_Type = InetAddressType
_HpSwitchDtPeerKeepAliveDestAddressType_Object = MibScalar
hpSwitchDtPeerKeepAliveDestAddressType = _HpSwitchDtPeerKeepAliveDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1, 1),
    _HpSwitchDtPeerKeepAliveDestAddressType_Type()
)
hpSwitchDtPeerKeepAliveDestAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveDestAddressType.setStatus("current")
_HpSwitchDtPeerKeepAliveDestAddress_Type = InetAddress
_HpSwitchDtPeerKeepAliveDestAddress_Object = MibScalar
hpSwitchDtPeerKeepAliveDestAddress = _HpSwitchDtPeerKeepAliveDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1, 2),
    _HpSwitchDtPeerKeepAliveDestAddress_Type()
)
hpSwitchDtPeerKeepAliveDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveDestAddress.setStatus("current")


class _HpSwitchDtPeerKeepAliveVlanId_Type(Integer32):
    """Custom type hpSwitchDtPeerKeepAliveVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HpSwitchDtPeerKeepAliveVlanId_Type.__name__ = "Integer32"
_HpSwitchDtPeerKeepAliveVlanId_Object = MibScalar
hpSwitchDtPeerKeepAliveVlanId = _HpSwitchDtPeerKeepAliveVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1, 3),
    _HpSwitchDtPeerKeepAliveVlanId_Type()
)
hpSwitchDtPeerKeepAliveVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveVlanId.setStatus("current")


class _HpSwitchDtPeerKeepAliveDestUdpPort_Type(InetPortNumber):
    """Custom type hpSwitchDtPeerKeepAliveDestUdpPort based on InetPortNumber"""
    defaultValue = 1024


_HpSwitchDtPeerKeepAliveDestUdpPort_Object = MibScalar
hpSwitchDtPeerKeepAliveDestUdpPort = _HpSwitchDtPeerKeepAliveDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1, 4),
    _HpSwitchDtPeerKeepAliveDestUdpPort_Type()
)
hpSwitchDtPeerKeepAliveDestUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveDestUdpPort.setStatus("current")


class _HpSwitchDtPeerKeepAliveInterval_Type(Integer32):
    """Custom type hpSwitchDtPeerKeepAliveInterval based on Integer32"""
    defaultValue = 1000


_HpSwitchDtPeerKeepAliveInterval_Object = MibScalar
hpSwitchDtPeerKeepAliveInterval = _HpSwitchDtPeerKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1, 5),
    _HpSwitchDtPeerKeepAliveInterval_Type()
)
hpSwitchDtPeerKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveInterval.setUnits("milliseconds")


class _HpSwitchDtPeerKeepAliveTimeout_Type(Integer32):
    """Custom type hpSwitchDtPeerKeepAliveTimeout based on Integer32"""
    defaultValue = 5


_HpSwitchDtPeerKeepAliveTimeout_Object = MibScalar
hpSwitchDtPeerKeepAliveTimeout = _HpSwitchDtPeerKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1, 6),
    _HpSwitchDtPeerKeepAliveTimeout_Type()
)
hpSwitchDtPeerKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveTimeout.setUnits("seconds")


class _HpSwitchDtPeerKeepAliveHoldTime_Type(Integer32):
    """Custom type hpSwitchDtPeerKeepAliveHoldTime based on Integer32"""
    defaultValue = 3


_HpSwitchDtPeerKeepAliveHoldTime_Object = MibScalar
hpSwitchDtPeerKeepAliveHoldTime = _HpSwitchDtPeerKeepAliveHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 4, 1, 7),
    _HpSwitchDtPeerKeepAliveHoldTime_Type()
)
hpSwitchDtPeerKeepAliveHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveHoldTime.setUnits("seconds")
_HpSwitchDtStats_ObjectIdentity = ObjectIdentity
hpSwitchDtStats = _HpSwitchDtStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5)
)
_HpSwitchDtIscProtocolStats_ObjectIdentity = ObjectIdentity
hpSwitchDtIscProtocolStats = _HpSwitchDtIscProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 1)
)
_HpSwitchDtIscHelloPktsSent_Type = Counter32
_HpSwitchDtIscHelloPktsSent_Object = MibScalar
hpSwitchDtIscHelloPktsSent = _HpSwitchDtIscHelloPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 1, 1),
    _HpSwitchDtIscHelloPktsSent_Type()
)
hpSwitchDtIscHelloPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtIscHelloPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtIscHelloPktsSent.setUnits("Packets")
_HpSwitchDtIscHelloPktsRecv_Type = Counter32
_HpSwitchDtIscHelloPktsRecv_Object = MibScalar
hpSwitchDtIscHelloPktsRecv = _HpSwitchDtIscHelloPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 1, 2),
    _HpSwitchDtIscHelloPktsRecv_Type()
)
hpSwitchDtIscHelloPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtIscHelloPktsRecv.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtIscHelloPktsRecv.setUnits("Packets")
_HpSwitchDtIscMACLearnPktsSent_Type = Counter32
_HpSwitchDtIscMACLearnPktsSent_Object = MibScalar
hpSwitchDtIscMACLearnPktsSent = _HpSwitchDtIscMACLearnPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 1, 3),
    _HpSwitchDtIscMACLearnPktsSent_Type()
)
hpSwitchDtIscMACLearnPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACLearnPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACLearnPktsSent.setUnits("Packets")
_HpSwitchDtIscMACLearnPktsRecv_Type = Counter32
_HpSwitchDtIscMACLearnPktsRecv_Object = MibScalar
hpSwitchDtIscMACLearnPktsRecv = _HpSwitchDtIscMACLearnPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 1, 4),
    _HpSwitchDtIscMACLearnPktsRecv_Type()
)
hpSwitchDtIscMACLearnPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACLearnPktsRecv.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACLearnPktsRecv.setUnits("Packets")
_HpSwitchDtIscMACAgedPktsSent_Type = Counter32
_HpSwitchDtIscMACAgedPktsSent_Object = MibScalar
hpSwitchDtIscMACAgedPktsSent = _HpSwitchDtIscMACAgedPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 1, 5),
    _HpSwitchDtIscMACAgedPktsSent_Type()
)
hpSwitchDtIscMACAgedPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACAgedPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACAgedPktsSent.setUnits("Packets")
_HpSwitchDtIscMACAgedPktsRecv_Type = Counter32
_HpSwitchDtIscMACAgedPktsRecv_Object = MibScalar
hpSwitchDtIscMACAgedPktsRecv = _HpSwitchDtIscMACAgedPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 1, 6),
    _HpSwitchDtIscMACAgedPktsRecv_Type()
)
hpSwitchDtIscMACAgedPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACAgedPktsRecv.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtIscMACAgedPktsRecv.setUnits("Packets")
_HpSwitchDtPeerKeepAliveStats_ObjectIdentity = ObjectIdentity
hpSwitchDtPeerKeepAliveStats = _HpSwitchDtPeerKeepAliveStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 2)
)
_HpSwitchDtPeerKeepAlivePktsSent_Type = Counter32
_HpSwitchDtPeerKeepAlivePktsSent_Object = MibScalar
hpSwitchDtPeerKeepAlivePktsSent = _HpSwitchDtPeerKeepAlivePktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 2, 1),
    _HpSwitchDtPeerKeepAlivePktsSent_Type()
)
hpSwitchDtPeerKeepAlivePktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAlivePktsSent.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAlivePktsSent.setUnits("Packets")
_HpSwitchDtPeerKeepAlivePktsRecv_Type = Counter32
_HpSwitchDtPeerKeepAlivePktsRecv_Object = MibScalar
hpSwitchDtPeerKeepAlivePktsRecv = _HpSwitchDtPeerKeepAlivePktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 5, 2, 2),
    _HpSwitchDtPeerKeepAlivePktsRecv_Type()
)
hpSwitchDtPeerKeepAlivePktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAlivePktsRecv.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAlivePktsRecv.setUnits("Packets")
_HpSwitchDtSystemInfo_ObjectIdentity = ObjectIdentity
hpSwitchDtSystemInfo = _HpSwitchDtSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 6)
)


class _HpSwitchDtSystemISCProtocolState_Type(Integer32):
    """Custom type hpSwitchDtSystemISCProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 2),
          ("outOfSync", 3),
          ("unknown", 1))
    )


_HpSwitchDtSystemISCProtocolState_Type.__name__ = "Integer32"
_HpSwitchDtSystemISCProtocolState_Object = MibScalar
hpSwitchDtSystemISCProtocolState = _HpSwitchDtSystemISCProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 6, 1),
    _HpSwitchDtSystemISCProtocolState_Type()
)
hpSwitchDtSystemISCProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtSystemISCProtocolState.setStatus("current")
_HpSwitchDtSystemDtLacpSystemID_Type = MacAddress
_HpSwitchDtSystemDtLacpSystemID_Object = MibScalar
hpSwitchDtSystemDtLacpSystemID = _HpSwitchDtSystemDtLacpSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 6, 2),
    _HpSwitchDtSystemDtLacpSystemID_Type()
)
hpSwitchDtSystemDtLacpSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtSystemDtLacpSystemID.setStatus("current")


class _HpSwitchDtSystemAdminRolePriority_Type(Integer32):
    """Custom type hpSwitchDtSystemAdminRolePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchDtSystemAdminRolePriority_Type.__name__ = "Integer32"
_HpSwitchDtSystemAdminRolePriority_Object = MibScalar
hpSwitchDtSystemAdminRolePriority = _HpSwitchDtSystemAdminRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 6, 3),
    _HpSwitchDtSystemAdminRolePriority_Type()
)
hpSwitchDtSystemAdminRolePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDtSystemAdminRolePriority.setStatus("current")


class _HpSwitchDtSystemOperRolePriority_Type(Integer32):
    """Custom type hpSwitchDtSystemOperRolePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchDtSystemOperRolePriority_Type.__name__ = "Integer32"
_HpSwitchDtSystemOperRolePriority_Object = MibScalar
hpSwitchDtSystemOperRolePriority = _HpSwitchDtSystemOperRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 6, 4),
    _HpSwitchDtSystemOperRolePriority_Type()
)
hpSwitchDtSystemOperRolePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtSystemOperRolePriority.setStatus("current")


class _HpSwitchDtSystemPeerOperRolePriority_Type(Integer32):
    """Custom type hpSwitchDtSystemPeerOperRolePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchDtSystemPeerOperRolePriority_Type.__name__ = "Integer32"
_HpSwitchDtSystemPeerOperRolePriority_Object = MibScalar
hpSwitchDtSystemPeerOperRolePriority = _HpSwitchDtSystemPeerOperRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 6, 5),
    _HpSwitchDtSystemPeerOperRolePriority_Type()
)
hpSwitchDtSystemPeerOperRolePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtSystemPeerOperRolePriority.setStatus("current")


class _HpSwitchDtSystemRole_Type(Integer32):
    """Custom type hpSwitchDtSystemRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("secondary", 3),
          ("unknown", 1))
    )


_HpSwitchDtSystemRole_Type.__name__ = "Integer32"
_HpSwitchDtSystemRole_Object = MibScalar
hpSwitchDtSystemRole = _HpSwitchDtSystemRole_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 6, 6),
    _HpSwitchDtSystemRole_Type()
)
hpSwitchDtSystemRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchDtSystemRole.setStatus("current")
_HpSwitchDtConformance_ObjectIdentity = ObjectIdentity
hpSwitchDtConformance = _HpSwitchDtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256)
)
_HpSwitchDtCompliances_ObjectIdentity = ObjectIdentity
hpSwitchDtCompliances = _HpSwitchDtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 1)
)
_HpSwitchDtGroups_ObjectIdentity = ObjectIdentity
hpSwitchDtGroups = _HpSwitchDtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2)
)

# Managed Objects groups

hpSwitchDtIscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2, 1)
)
hpSwitchDtIscGroup.setObjects(
      *(("DT-MIB", "hpSwitchISCPortIndex"),
        ("DT-MIB", "hpSwitchRemoteISCPortIndex"))
)
if mibBuilder.loadTexts:
    hpSwitchDtIscGroup.setStatus("current")

hpSwitchDtLocalLacpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2, 2)
)
hpSwitchDtLocalLacpGroup.setObjects(
      *(("DT-MIB", "hpSwitchDtLacpLocalIfIndex"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfName"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfLacpEnable"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfTrunkGroup"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfLacpPortStatus"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfLacpPartner"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfLacpStatus"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfLacpAdminKey"),
        ("DT-MIB", "hpSwitchDtLacpLocalIfLacpOperKey"))
)
if mibBuilder.loadTexts:
    hpSwitchDtLocalLacpGroup.setStatus("current")

hpSwitchDtRemoteLacpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2, 3)
)
hpSwitchDtRemoteLacpGroup.setObjects(
      *(("DT-MIB", "hpSwitchDtLacpPeerIfIndex"),
        ("DT-MIB", "hpSwitchDtLacpPeerIfName"),
        ("DT-MIB", "hpSwitchDtLacpPeerIfLacpEnable"),
        ("DT-MIB", "hpSwitchDtLacpPeerIfTrunkGroup"),
        ("DT-MIB", "hpSwitchDtLacpPeerIfLacpPortStatus"),
        ("DT-MIB", "hpSwitchDtLacpPeerIfLacpPartner"),
        ("DT-MIB", "hpSwitchDtLacpPeerIfLacpStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchDtRemoteLacpGroup.setStatus("current")

hpSwitchDtPeerKeepAliveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2, 4)
)
hpSwitchDtPeerKeepAliveGroup.setObjects(
      *(("DT-MIB", "hpSwitchDtPeerKeepAliveDestAddressType"),
        ("DT-MIB", "hpSwitchDtPeerKeepAliveDestAddress"),
        ("DT-MIB", "hpSwitchDtPeerKeepAliveVlanId"),
        ("DT-MIB", "hpSwitchDtPeerKeepAliveDestUdpPort"),
        ("DT-MIB", "hpSwitchDtPeerKeepAliveInterval"),
        ("DT-MIB", "hpSwitchDtPeerKeepAliveTimeout"),
        ("DT-MIB", "hpSwitchDtPeerKeepAliveHoldTime"))
)
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveGroup.setStatus("current")

hpSwitchDtIscStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2, 5)
)
hpSwitchDtIscStatsGroup.setObjects(
      *(("DT-MIB", "hpSwitchDtIscHelloPktsSent"),
        ("DT-MIB", "hpSwitchDtIscHelloPktsRecv"),
        ("DT-MIB", "hpSwitchDtIscMACLearnPktsSent"),
        ("DT-MIB", "hpSwitchDtIscMACLearnPktsRecv"),
        ("DT-MIB", "hpSwitchDtIscMACAgedPktsSent"),
        ("DT-MIB", "hpSwitchDtIscMACAgedPktsRecv"))
)
if mibBuilder.loadTexts:
    hpSwitchDtIscStatsGroup.setStatus("current")

hpSwitchDtPeerKeepAliveStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2, 6)
)
hpSwitchDtPeerKeepAliveStatsGroup.setObjects(
      *(("DT-MIB", "hpSwitchDtPeerKeepAlivePktsSent"),
        ("DT-MIB", "hpSwitchDtPeerKeepAlivePktsRecv"))
)
if mibBuilder.loadTexts:
    hpSwitchDtPeerKeepAliveStatsGroup.setStatus("current")

hpSwitchDtSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 2, 7)
)
hpSwitchDtSystemInfoGroup.setObjects(
      *(("DT-MIB", "hpSwitchDtSystemISCProtocolState"),
        ("DT-MIB", "hpSwitchDtSystemDtLacpSystemID"),
        ("DT-MIB", "hpSwitchDtSystemAdminRolePriority"),
        ("DT-MIB", "hpSwitchDtSystemOperRolePriority"),
        ("DT-MIB", "hpSwitchDtSystemPeerOperRolePriority"),
        ("DT-MIB", "hpSwitchDtSystemRole"))
)
if mibBuilder.loadTexts:
    hpSwitchDtSystemInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSwitchDtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchDtCompliance.setStatus(
        "deprecated"
    )

hpSwitchDtCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 27, 256, 1, 2)
)
if mibBuilder.loadTexts:
    hpSwitchDtCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DT-MIB",
    **{"hpConfig": hpConfig,
       "hpSwitchConfig": hpSwitchConfig,
       "hpSwitchDt": hpSwitchDt,
       "hpSwitchISCPortIndex": hpSwitchISCPortIndex,
       "hpSwitchRemoteISCPortIndex": hpSwitchRemoteISCPortIndex,
       "hpSwitchDtLacpStatus": hpSwitchDtLacpStatus,
       "hpSwitchDtLacpStatusLocalTable": hpSwitchDtLacpStatusLocalTable,
       "hpSwitchDtLacpStatusLocalEntry": hpSwitchDtLacpStatusLocalEntry,
       "hpSwitchDtLacpLocalIfIndex": hpSwitchDtLacpLocalIfIndex,
       "hpSwitchDtLacpLocalIfName": hpSwitchDtLacpLocalIfName,
       "hpSwitchDtLacpLocalIfLacpEnable": hpSwitchDtLacpLocalIfLacpEnable,
       "hpSwitchDtLacpLocalIfTrunkGroup": hpSwitchDtLacpLocalIfTrunkGroup,
       "hpSwitchDtLacpLocalIfLacpPortStatus": hpSwitchDtLacpLocalIfLacpPortStatus,
       "hpSwitchDtLacpLocalIfLacpPartner": hpSwitchDtLacpLocalIfLacpPartner,
       "hpSwitchDtLacpLocalIfLacpStatus": hpSwitchDtLacpLocalIfLacpStatus,
       "hpSwitchDtLacpLocalIfLacpAdminKey": hpSwitchDtLacpLocalIfLacpAdminKey,
       "hpSwitchDtLacpLocalIfLacpOperKey": hpSwitchDtLacpLocalIfLacpOperKey,
       "hpSwitchDtLacpStatusPeerTable": hpSwitchDtLacpStatusPeerTable,
       "hpSwitchDtLacpStatusPeerEntry": hpSwitchDtLacpStatusPeerEntry,
       "hpSwitchDtLacpPeerIfIndex": hpSwitchDtLacpPeerIfIndex,
       "hpSwitchDtLacpPeerIfName": hpSwitchDtLacpPeerIfName,
       "hpSwitchDtLacpPeerIfLacpEnable": hpSwitchDtLacpPeerIfLacpEnable,
       "hpSwitchDtLacpPeerIfTrunkGroup": hpSwitchDtLacpPeerIfTrunkGroup,
       "hpSwitchDtLacpPeerIfLacpPortStatus": hpSwitchDtLacpPeerIfLacpPortStatus,
       "hpSwitchDtLacpPeerIfLacpPartner": hpSwitchDtLacpPeerIfLacpPartner,
       "hpSwitchDtLacpPeerIfLacpStatus": hpSwitchDtLacpPeerIfLacpStatus,
       "hpSwitchDtConfig": hpSwitchDtConfig,
       "hpSwitchDtPeerKeepAliveConfig": hpSwitchDtPeerKeepAliveConfig,
       "hpSwitchDtPeerKeepAliveDestAddressType": hpSwitchDtPeerKeepAliveDestAddressType,
       "hpSwitchDtPeerKeepAliveDestAddress": hpSwitchDtPeerKeepAliveDestAddress,
       "hpSwitchDtPeerKeepAliveVlanId": hpSwitchDtPeerKeepAliveVlanId,
       "hpSwitchDtPeerKeepAliveDestUdpPort": hpSwitchDtPeerKeepAliveDestUdpPort,
       "hpSwitchDtPeerKeepAliveInterval": hpSwitchDtPeerKeepAliveInterval,
       "hpSwitchDtPeerKeepAliveTimeout": hpSwitchDtPeerKeepAliveTimeout,
       "hpSwitchDtPeerKeepAliveHoldTime": hpSwitchDtPeerKeepAliveHoldTime,
       "hpSwitchDtStats": hpSwitchDtStats,
       "hpSwitchDtIscProtocolStats": hpSwitchDtIscProtocolStats,
       "hpSwitchDtIscHelloPktsSent": hpSwitchDtIscHelloPktsSent,
       "hpSwitchDtIscHelloPktsRecv": hpSwitchDtIscHelloPktsRecv,
       "hpSwitchDtIscMACLearnPktsSent": hpSwitchDtIscMACLearnPktsSent,
       "hpSwitchDtIscMACLearnPktsRecv": hpSwitchDtIscMACLearnPktsRecv,
       "hpSwitchDtIscMACAgedPktsSent": hpSwitchDtIscMACAgedPktsSent,
       "hpSwitchDtIscMACAgedPktsRecv": hpSwitchDtIscMACAgedPktsRecv,
       "hpSwitchDtPeerKeepAliveStats": hpSwitchDtPeerKeepAliveStats,
       "hpSwitchDtPeerKeepAlivePktsSent": hpSwitchDtPeerKeepAlivePktsSent,
       "hpSwitchDtPeerKeepAlivePktsRecv": hpSwitchDtPeerKeepAlivePktsRecv,
       "hpSwitchDtSystemInfo": hpSwitchDtSystemInfo,
       "hpSwitchDtSystemISCProtocolState": hpSwitchDtSystemISCProtocolState,
       "hpSwitchDtSystemDtLacpSystemID": hpSwitchDtSystemDtLacpSystemID,
       "hpSwitchDtSystemAdminRolePriority": hpSwitchDtSystemAdminRolePriority,
       "hpSwitchDtSystemOperRolePriority": hpSwitchDtSystemOperRolePriority,
       "hpSwitchDtSystemPeerOperRolePriority": hpSwitchDtSystemPeerOperRolePriority,
       "hpSwitchDtSystemRole": hpSwitchDtSystemRole,
       "hpSwitchDtConformance": hpSwitchDtConformance,
       "hpSwitchDtCompliances": hpSwitchDtCompliances,
       "hpSwitchDtCompliance": hpSwitchDtCompliance,
       "hpSwitchDtCompliance1": hpSwitchDtCompliance1,
       "hpSwitchDtGroups": hpSwitchDtGroups,
       "hpSwitchDtIscGroup": hpSwitchDtIscGroup,
       "hpSwitchDtLocalLacpGroup": hpSwitchDtLocalLacpGroup,
       "hpSwitchDtRemoteLacpGroup": hpSwitchDtRemoteLacpGroup,
       "hpSwitchDtPeerKeepAliveGroup": hpSwitchDtPeerKeepAliveGroup,
       "hpSwitchDtIscStatsGroup": hpSwitchDtIscStatsGroup,
       "hpSwitchDtPeerKeepAliveStatsGroup": hpSwitchDtPeerKeepAliveStatsGroup,
       "hpSwitchDtSystemInfoGroup": hpSwitchDtSystemInfoGroup}
)
