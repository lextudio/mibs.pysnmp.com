# SNMP MIB module (TPLINK-LLDPINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-LLDPINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:19 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkLldpMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-LLDP-MIB",
    "tplinkLldpMIBObjects")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpInfo_ObjectIdentity = ObjectIdentity
lldpInfo = _LldpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2)
)
_LldpLocalInfoTable_Object = MibTable
lldpLocalInfoTable = _LldpLocalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpLocalInfoTable.setStatus("current")
_LldpLocalInfoEntry_Object = MibTableRow
lldpLocalInfoEntry = _LldpLocalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1)
)
lldpLocalInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lldpLocalInfoEntry.setStatus("current")


class _LldpLocalPortId_Type(OctetString):
    """Custom type lldpLocalPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalPortId_Type.__name__ = "OctetString"
_LldpLocalPortId_Object = MibTableColumn
lldpLocalPortId = _LldpLocalPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 1),
    _LldpLocalPortId_Type()
)
lldpLocalPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortId.setStatus("current")


class _LldpLocalChassisIdType_Type(OctetString):
    """Custom type lldpLocalChassisIdType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalChassisIdType_Type.__name__ = "OctetString"
_LldpLocalChassisIdType_Object = MibTableColumn
lldpLocalChassisIdType = _LldpLocalChassisIdType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 2),
    _LldpLocalChassisIdType_Type()
)
lldpLocalChassisIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalChassisIdType.setStatus("current")


class _LldpLocalChassisId_Type(OctetString):
    """Custom type lldpLocalChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalChassisId_Type.__name__ = "OctetString"
_LldpLocalChassisId_Object = MibTableColumn
lldpLocalChassisId = _LldpLocalChassisId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 3),
    _LldpLocalChassisId_Type()
)
lldpLocalChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalChassisId.setStatus("current")


class _LldpLocalPortIdType_Type(OctetString):
    """Custom type lldpLocalPortIdType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalPortIdType_Type.__name__ = "OctetString"
_LldpLocalPortIdType_Object = MibTableColumn
lldpLocalPortIdType = _LldpLocalPortIdType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 4),
    _LldpLocalPortIdType_Type()
)
lldpLocalPortIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortIdType.setStatus("current")


class _LldpLocalPortIdDescr_Type(OctetString):
    """Custom type lldpLocalPortIdDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalPortIdDescr_Type.__name__ = "OctetString"
_LldpLocalPortIdDescr_Object = MibTableColumn
lldpLocalPortIdDescr = _LldpLocalPortIdDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 5),
    _LldpLocalPortIdDescr_Type()
)
lldpLocalPortIdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortIdDescr.setStatus("current")
_LldpLocalTtl_Type = Integer32
_LldpLocalTtl_Object = MibTableColumn
lldpLocalTtl = _LldpLocalTtl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 6),
    _LldpLocalTtl_Type()
)
lldpLocalTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalTtl.setStatus("current")


class _LldpLocalPortDescr_Type(OctetString):
    """Custom type lldpLocalPortDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalPortDescr_Type.__name__ = "OctetString"
_LldpLocalPortDescr_Object = MibTableColumn
lldpLocalPortDescr = _LldpLocalPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 7),
    _LldpLocalPortDescr_Type()
)
lldpLocalPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortDescr.setStatus("current")


class _LldpLocalDeviceName_Type(OctetString):
    """Custom type lldpLocalDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalDeviceName_Type.__name__ = "OctetString"
_LldpLocalDeviceName_Object = MibTableColumn
lldpLocalDeviceName = _LldpLocalDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 8),
    _LldpLocalDeviceName_Type()
)
lldpLocalDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceName.setStatus("current")


class _LldpLocalDeviceDescr_Type(OctetString):
    """Custom type lldpLocalDeviceDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalDeviceDescr_Type.__name__ = "OctetString"
_LldpLocalDeviceDescr_Object = MibTableColumn
lldpLocalDeviceDescr = _LldpLocalDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 9),
    _LldpLocalDeviceDescr_Type()
)
lldpLocalDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalDeviceDescr.setStatus("current")


class _LldpLocalCapAvailable_Type(OctetString):
    """Custom type lldpLocalCapAvailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalCapAvailable_Type.__name__ = "OctetString"
_LldpLocalCapAvailable_Object = MibTableColumn
lldpLocalCapAvailable = _LldpLocalCapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 10),
    _LldpLocalCapAvailable_Type()
)
lldpLocalCapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalCapAvailable.setStatus("current")


class _LldpLocalCapEnabled_Type(OctetString):
    """Custom type lldpLocalCapEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalCapEnabled_Type.__name__ = "OctetString"
_LldpLocalCapEnabled_Object = MibTableColumn
lldpLocalCapEnabled = _LldpLocalCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 11),
    _LldpLocalCapEnabled_Type()
)
lldpLocalCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalCapEnabled.setStatus("current")
_LldpLocalManageIpAddr_Type = IpAddress
_LldpLocalManageIpAddr_Object = MibTableColumn
lldpLocalManageIpAddr = _LldpLocalManageIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 12),
    _LldpLocalManageIpAddr_Type()
)
lldpLocalManageIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalManageIpAddr.setStatus("current")


class _LldpLocalManageAddrType_Type(OctetString):
    """Custom type lldpLocalManageAddrType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalManageAddrType_Type.__name__ = "OctetString"
_LldpLocalManageAddrType_Object = MibTableColumn
lldpLocalManageAddrType = _LldpLocalManageAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 13),
    _LldpLocalManageAddrType_Type()
)
lldpLocalManageAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalManageAddrType.setStatus("current")


class _LldpLocalManageAddrInterfaceType_Type(OctetString):
    """Custom type lldpLocalManageAddrInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalManageAddrInterfaceType_Type.__name__ = "OctetString"
_LldpLocalManageAddrInterfaceType_Object = MibTableColumn
lldpLocalManageAddrInterfaceType = _LldpLocalManageAddrInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 14),
    _LldpLocalManageAddrInterfaceType_Type()
)
lldpLocalManageAddrInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalManageAddrInterfaceType.setStatus("current")
_LldpLocalManageAddrInterfaceId_Type = Integer32
_LldpLocalManageAddrInterfaceId_Object = MibTableColumn
lldpLocalManageAddrInterfaceId = _LldpLocalManageAddrInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 15),
    _LldpLocalManageAddrInterfaceId_Type()
)
lldpLocalManageAddrInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalManageAddrInterfaceId.setStatus("current")
_LldpLocalManageAddrOID_Type = Integer32
_LldpLocalManageAddrOID_Object = MibTableColumn
lldpLocalManageAddrOID = _LldpLocalManageAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 16),
    _LldpLocalManageAddrOID_Type()
)
lldpLocalManageAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalManageAddrOID.setStatus("current")


class _LldpLocalPortAndProtocolVlanID_Type(OctetString):
    """Custom type lldpLocalPortAndProtocolVlanID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalPortAndProtocolVlanID_Type.__name__ = "OctetString"
_LldpLocalPortAndProtocolVlanID_Object = MibTableColumn
lldpLocalPortAndProtocolVlanID = _LldpLocalPortAndProtocolVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 17),
    _LldpLocalPortAndProtocolVlanID_Type()
)
lldpLocalPortAndProtocolVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPortAndProtocolVlanID.setStatus("current")


class _LldpLocalVlanName_Type(OctetString):
    """Custom type lldpLocalVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalVlanName_Type.__name__ = "OctetString"
_LldpLocalVlanName_Object = MibTableColumn
lldpLocalVlanName = _LldpLocalVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 18),
    _LldpLocalVlanName_Type()
)
lldpLocalVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalVlanName.setStatus("current")


class _LldpLocalAutoNegotiationSupported_Type(Integer32):
    """Custom type lldpLocalAutoNegotiationSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpLocalAutoNegotiationSupported_Type.__name__ = "Integer32"
_LldpLocalAutoNegotiationSupported_Object = MibTableColumn
lldpLocalAutoNegotiationSupported = _LldpLocalAutoNegotiationSupported_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 19),
    _LldpLocalAutoNegotiationSupported_Type()
)
lldpLocalAutoNegotiationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalAutoNegotiationSupported.setStatus("current")


class _LldpLocalAutoNegotiationEnabled_Type(Integer32):
    """Custom type lldpLocalAutoNegotiationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpLocalAutoNegotiationEnabled_Type.__name__ = "Integer32"
_LldpLocalAutoNegotiationEnabled_Object = MibTableColumn
lldpLocalAutoNegotiationEnabled = _LldpLocalAutoNegotiationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 20),
    _LldpLocalAutoNegotiationEnabled_Type()
)
lldpLocalAutoNegotiationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalAutoNegotiationEnabled.setStatus("current")


class _LldpLocalOperMau_Type(OctetString):
    """Custom type lldpLocalOperMau based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalOperMau_Type.__name__ = "OctetString"
_LldpLocalOperMau_Object = MibTableColumn
lldpLocalOperMau = _LldpLocalOperMau_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 21),
    _LldpLocalOperMau_Type()
)
lldpLocalOperMau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalOperMau.setStatus("current")


class _LldpLocalLinkAggregationSupported_Type(Integer32):
    """Custom type lldpLocalLinkAggregationSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpLocalLinkAggregationSupported_Type.__name__ = "Integer32"
_LldpLocalLinkAggregationSupported_Object = MibTableColumn
lldpLocalLinkAggregationSupported = _LldpLocalLinkAggregationSupported_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 22),
    _LldpLocalLinkAggregationSupported_Type()
)
lldpLocalLinkAggregationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalLinkAggregationSupported.setStatus("current")


class _LldpLocalLinkAggregationEnabled_Type(Integer32):
    """Custom type lldpLocalLinkAggregationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpLocalLinkAggregationEnabled_Type.__name__ = "Integer32"
_LldpLocalLinkAggregationEnabled_Object = MibTableColumn
lldpLocalLinkAggregationEnabled = _LldpLocalLinkAggregationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 23),
    _LldpLocalLinkAggregationEnabled_Type()
)
lldpLocalLinkAggregationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalLinkAggregationEnabled.setStatus("current")
_LldpLocalAggregationPortId_Type = Integer32
_LldpLocalAggregationPortId_Object = MibTableColumn
lldpLocalAggregationPortId = _LldpLocalAggregationPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 24),
    _LldpLocalAggregationPortId_Type()
)
lldpLocalAggregationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalAggregationPortId.setStatus("current")


class _LldpLocalPowerPortClass_Type(OctetString):
    """Custom type lldpLocalPowerPortClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpLocalPowerPortClass_Type.__name__ = "OctetString"
_LldpLocalPowerPortClass_Object = MibTableColumn
lldpLocalPowerPortClass = _LldpLocalPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 25),
    _LldpLocalPowerPortClass_Type()
)
lldpLocalPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPowerPortClass.setStatus("current")


class _LldpLocalPsePowerSupported_Type(Integer32):
    """Custom type lldpLocalPsePowerSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpLocalPsePowerSupported_Type.__name__ = "Integer32"
_LldpLocalPsePowerSupported_Object = MibTableColumn
lldpLocalPsePowerSupported = _LldpLocalPsePowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 26),
    _LldpLocalPsePowerSupported_Type()
)
lldpLocalPsePowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPsePowerSupported.setStatus("current")


class _LldpLocalPsePowerEnabled_Type(Integer32):
    """Custom type lldpLocalPsePowerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpLocalPsePowerEnabled_Type.__name__ = "Integer32"
_LldpLocalPsePowerEnabled_Object = MibTableColumn
lldpLocalPsePowerEnabled = _LldpLocalPsePowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 27),
    _LldpLocalPsePowerEnabled_Type()
)
lldpLocalPsePowerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPsePowerEnabled.setStatus("current")


class _LldpLocalPsePairsControlAbility_Type(Integer32):
    """Custom type lldpLocalPsePairsControlAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpLocalPsePairsControlAbility_Type.__name__ = "Integer32"
_LldpLocalPsePairsControlAbility_Object = MibTableColumn
lldpLocalPsePairsControlAbility = _LldpLocalPsePairsControlAbility_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 28),
    _LldpLocalPsePairsControlAbility_Type()
)
lldpLocalPsePairsControlAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalPsePairsControlAbility.setStatus("current")
_LldpLocalMaximumFrameSize_Type = Integer32
_LldpLocalMaximumFrameSize_Object = MibTableColumn
lldpLocalMaximumFrameSize = _LldpLocalMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 1, 1, 29),
    _LldpLocalMaximumFrameSize_Type()
)
lldpLocalMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpLocalMaximumFrameSize.setStatus("current")
_LldpNeighborInfoTable_Object = MibTable
lldpNeighborInfoTable = _LldpNeighborInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2)
)
if mibBuilder.loadTexts:
    lldpNeighborInfoTable.setStatus("current")
_LldpNeighborInfoEntry_Object = MibTableRow
lldpNeighborInfoEntry = _LldpNeighborInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1)
)
lldpNeighborInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-LLDPINFO-MIB", "lldpNeighborPortIndexId"),
)
if mibBuilder.loadTexts:
    lldpNeighborInfoEntry.setStatus("current")


class _LldpNeighborPortId_Type(OctetString):
    """Custom type lldpNeighborPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborPortId_Type.__name__ = "OctetString"
_LldpNeighborPortId_Object = MibTableColumn
lldpNeighborPortId = _LldpNeighborPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 1),
    _LldpNeighborPortId_Type()
)
lldpNeighborPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortId.setStatus("current")
_LldpNeighborPortIndexId_Type = Integer32
_LldpNeighborPortIndexId_Object = MibTableColumn
lldpNeighborPortIndexId = _LldpNeighborPortIndexId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 2),
    _LldpNeighborPortIndexId_Type()
)
lldpNeighborPortIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortIndexId.setStatus("current")


class _LldpNeighborChassisIdType_Type(OctetString):
    """Custom type lldpNeighborChassisIdType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborChassisIdType_Type.__name__ = "OctetString"
_LldpNeighborChassisIdType_Object = MibTableColumn
lldpNeighborChassisIdType = _LldpNeighborChassisIdType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 3),
    _LldpNeighborChassisIdType_Type()
)
lldpNeighborChassisIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborChassisIdType.setStatus("current")


class _LldpNeighborChassisId_Type(OctetString):
    """Custom type lldpNeighborChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborChassisId_Type.__name__ = "OctetString"
_LldpNeighborChassisId_Object = MibTableColumn
lldpNeighborChassisId = _LldpNeighborChassisId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 4),
    _LldpNeighborChassisId_Type()
)
lldpNeighborChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborChassisId.setStatus("current")


class _LldpNeighborPortIdType_Type(OctetString):
    """Custom type lldpNeighborPortIdType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborPortIdType_Type.__name__ = "OctetString"
_LldpNeighborPortIdType_Object = MibTableColumn
lldpNeighborPortIdType = _LldpNeighborPortIdType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 5),
    _LldpNeighborPortIdType_Type()
)
lldpNeighborPortIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortIdType.setStatus("current")


class _LldpNeighborPortIdDescr_Type(OctetString):
    """Custom type lldpNeighborPortIdDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborPortIdDescr_Type.__name__ = "OctetString"
_LldpNeighborPortIdDescr_Object = MibTableColumn
lldpNeighborPortIdDescr = _LldpNeighborPortIdDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 6),
    _LldpNeighborPortIdDescr_Type()
)
lldpNeighborPortIdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortIdDescr.setStatus("current")
_LldpNeighborTtl_Type = Integer32
_LldpNeighborTtl_Object = MibTableColumn
lldpNeighborTtl = _LldpNeighborTtl_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 7),
    _LldpNeighborTtl_Type()
)
lldpNeighborTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborTtl.setStatus("current")


class _LldpNeighborPortDescr_Type(OctetString):
    """Custom type lldpNeighborPortDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborPortDescr_Type.__name__ = "OctetString"
_LldpNeighborPortDescr_Object = MibTableColumn
lldpNeighborPortDescr = _LldpNeighborPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 8),
    _LldpNeighborPortDescr_Type()
)
lldpNeighborPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortDescr.setStatus("current")


class _LldpNeighborDeviceName_Type(OctetString):
    """Custom type lldpNeighborDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborDeviceName_Type.__name__ = "OctetString"
_LldpNeighborDeviceName_Object = MibTableColumn
lldpNeighborDeviceName = _LldpNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 9),
    _LldpNeighborDeviceName_Type()
)
lldpNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborDeviceName.setStatus("current")


class _LldpNeighborDeviceDescr_Type(OctetString):
    """Custom type lldpNeighborDeviceDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborDeviceDescr_Type.__name__ = "OctetString"
_LldpNeighborDeviceDescr_Object = MibTableColumn
lldpNeighborDeviceDescr = _LldpNeighborDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 10),
    _LldpNeighborDeviceDescr_Type()
)
lldpNeighborDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborDeviceDescr.setStatus("current")


class _LldpNeighborCapAvailable_Type(OctetString):
    """Custom type lldpNeighborCapAvailable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborCapAvailable_Type.__name__ = "OctetString"
_LldpNeighborCapAvailable_Object = MibTableColumn
lldpNeighborCapAvailable = _LldpNeighborCapAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 11),
    _LldpNeighborCapAvailable_Type()
)
lldpNeighborCapAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborCapAvailable.setStatus("current")


class _LldpNeighborCapEnabled_Type(OctetString):
    """Custom type lldpNeighborCapEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborCapEnabled_Type.__name__ = "OctetString"
_LldpNeighborCapEnabled_Object = MibTableColumn
lldpNeighborCapEnabled = _LldpNeighborCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 12),
    _LldpNeighborCapEnabled_Type()
)
lldpNeighborCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborCapEnabled.setStatus("current")
_LldpNeighborManageIpAddr_Type = IpAddress
_LldpNeighborManageIpAddr_Object = MibTableColumn
lldpNeighborManageIpAddr = _LldpNeighborManageIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 13),
    _LldpNeighborManageIpAddr_Type()
)
lldpNeighborManageIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborManageIpAddr.setStatus("current")


class _LldpNeighborManageAddrType_Type(OctetString):
    """Custom type lldpNeighborManageAddrType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborManageAddrType_Type.__name__ = "OctetString"
_LldpNeighborManageAddrType_Object = MibTableColumn
lldpNeighborManageAddrType = _LldpNeighborManageAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 14),
    _LldpNeighborManageAddrType_Type()
)
lldpNeighborManageAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborManageAddrType.setStatus("current")


class _LldpNeighborManageAddrInterfaceType_Type(OctetString):
    """Custom type lldpNeighborManageAddrInterfaceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborManageAddrInterfaceType_Type.__name__ = "OctetString"
_LldpNeighborManageAddrInterfaceType_Object = MibTableColumn
lldpNeighborManageAddrInterfaceType = _LldpNeighborManageAddrInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 15),
    _LldpNeighborManageAddrInterfaceType_Type()
)
lldpNeighborManageAddrInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborManageAddrInterfaceType.setStatus("current")
_LldpNeighborManageAddrInterfaceId_Type = Integer32
_LldpNeighborManageAddrInterfaceId_Object = MibTableColumn
lldpNeighborManageAddrInterfaceId = _LldpNeighborManageAddrInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 16),
    _LldpNeighborManageAddrInterfaceId_Type()
)
lldpNeighborManageAddrInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborManageAddrInterfaceId.setStatus("current")
_LldpNeighborManageAddrOID_Type = Integer32
_LldpNeighborManageAddrOID_Object = MibTableColumn
lldpNeighborManageAddrOID = _LldpNeighborManageAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 17),
    _LldpNeighborManageAddrOID_Type()
)
lldpNeighborManageAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborManageAddrOID.setStatus("current")


class _LldpNeighborPortAndProtocolVlanID_Type(OctetString):
    """Custom type lldpNeighborPortAndProtocolVlanID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LldpNeighborPortAndProtocolVlanID_Type.__name__ = "OctetString"
_LldpNeighborPortAndProtocolVlanID_Object = MibTableColumn
lldpNeighborPortAndProtocolVlanID = _LldpNeighborPortAndProtocolVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 18),
    _LldpNeighborPortAndProtocolVlanID_Type()
)
lldpNeighborPortAndProtocolVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPortAndProtocolVlanID.setStatus("current")


class _LldpNeighborVlanName_Type(OctetString):
    """Custom type lldpNeighborVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LldpNeighborVlanName_Type.__name__ = "OctetString"
_LldpNeighborVlanName_Object = MibTableColumn
lldpNeighborVlanName = _LldpNeighborVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 19),
    _LldpNeighborVlanName_Type()
)
lldpNeighborVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborVlanName.setStatus("current")


class _LldpNeighborProtocolIdentity_Type(OctetString):
    """Custom type lldpNeighborProtocolIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LldpNeighborProtocolIdentity_Type.__name__ = "OctetString"
_LldpNeighborProtocolIdentity_Object = MibTableColumn
lldpNeighborProtocolIdentity = _LldpNeighborProtocolIdentity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 20),
    _LldpNeighborProtocolIdentity_Type()
)
lldpNeighborProtocolIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborProtocolIdentity.setStatus("current")


class _LldpNeighborAutoNegotiationSupported_Type(Integer32):
    """Custom type lldpNeighborAutoNegotiationSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpNeighborAutoNegotiationSupported_Type.__name__ = "Integer32"
_LldpNeighborAutoNegotiationSupported_Object = MibTableColumn
lldpNeighborAutoNegotiationSupported = _LldpNeighborAutoNegotiationSupported_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 21),
    _LldpNeighborAutoNegotiationSupported_Type()
)
lldpNeighborAutoNegotiationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborAutoNegotiationSupported.setStatus("current")


class _LldpNeighborAutoNegotiationEnabled_Type(Integer32):
    """Custom type lldpNeighborAutoNegotiationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpNeighborAutoNegotiationEnabled_Type.__name__ = "Integer32"
_LldpNeighborAutoNegotiationEnabled_Object = MibTableColumn
lldpNeighborAutoNegotiationEnabled = _LldpNeighborAutoNegotiationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 22),
    _LldpNeighborAutoNegotiationEnabled_Type()
)
lldpNeighborAutoNegotiationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborAutoNegotiationEnabled.setStatus("current")


class _LldpNeighborOperMau_Type(OctetString):
    """Custom type lldpNeighborOperMau based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborOperMau_Type.__name__ = "OctetString"
_LldpNeighborOperMau_Object = MibTableColumn
lldpNeighborOperMau = _LldpNeighborOperMau_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 23),
    _LldpNeighborOperMau_Type()
)
lldpNeighborOperMau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborOperMau.setStatus("current")


class _LldpNeighborLinkAggregationSupported_Type(Integer32):
    """Custom type lldpNeighborLinkAggregationSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpNeighborLinkAggregationSupported_Type.__name__ = "Integer32"
_LldpNeighborLinkAggregationSupported_Object = MibTableColumn
lldpNeighborLinkAggregationSupported = _LldpNeighborLinkAggregationSupported_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 24),
    _LldpNeighborLinkAggregationSupported_Type()
)
lldpNeighborLinkAggregationSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborLinkAggregationSupported.setStatus("current")


class _LldpNeighborLinkAggregationEnabled_Type(Integer32):
    """Custom type lldpNeighborLinkAggregationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpNeighborLinkAggregationEnabled_Type.__name__ = "Integer32"
_LldpNeighborLinkAggregationEnabled_Object = MibTableColumn
lldpNeighborLinkAggregationEnabled = _LldpNeighborLinkAggregationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 25),
    _LldpNeighborLinkAggregationEnabled_Type()
)
lldpNeighborLinkAggregationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborLinkAggregationEnabled.setStatus("current")
_LldpNeighborAggregationPortId_Type = Integer32
_LldpNeighborAggregationPortId_Object = MibTableColumn
lldpNeighborAggregationPortId = _LldpNeighborAggregationPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 26),
    _LldpNeighborAggregationPortId_Type()
)
lldpNeighborAggregationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborAggregationPortId.setStatus("current")


class _LldpNeighborPowerPortClass_Type(OctetString):
    """Custom type lldpNeighborPowerPortClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpNeighborPowerPortClass_Type.__name__ = "OctetString"
_LldpNeighborPowerPortClass_Object = MibTableColumn
lldpNeighborPowerPortClass = _LldpNeighborPowerPortClass_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 27),
    _LldpNeighborPowerPortClass_Type()
)
lldpNeighborPowerPortClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPowerPortClass.setStatus("current")


class _LldpNeighborPsePowerSupported_Type(Integer32):
    """Custom type lldpNeighborPsePowerSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpNeighborPsePowerSupported_Type.__name__ = "Integer32"
_LldpNeighborPsePowerSupported_Object = MibTableColumn
lldpNeighborPsePowerSupported = _LldpNeighborPsePowerSupported_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 28),
    _LldpNeighborPsePowerSupported_Type()
)
lldpNeighborPsePowerSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPsePowerSupported.setStatus("current")


class _LldpNeighborPsePowerEnabled_Type(Integer32):
    """Custom type lldpNeighborPsePowerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpNeighborPsePowerEnabled_Type.__name__ = "Integer32"
_LldpNeighborPsePowerEnabled_Object = MibTableColumn
lldpNeighborPsePowerEnabled = _LldpNeighborPsePowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 29),
    _LldpNeighborPsePowerEnabled_Type()
)
lldpNeighborPsePowerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPsePowerEnabled.setStatus("current")


class _LldpNeighborPsePairsControlAbility_Type(Integer32):
    """Custom type lldpNeighborPsePairsControlAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpNeighborPsePairsControlAbility_Type.__name__ = "Integer32"
_LldpNeighborPsePairsControlAbility_Object = MibTableColumn
lldpNeighborPsePairsControlAbility = _LldpNeighborPsePairsControlAbility_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 30),
    _LldpNeighborPsePairsControlAbility_Type()
)
lldpNeighborPsePairsControlAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborPsePairsControlAbility.setStatus("current")
_LldpNeighborMaximumFrameSize_Type = Integer32
_LldpNeighborMaximumFrameSize_Object = MibTableColumn
lldpNeighborMaximumFrameSize = _LldpNeighborMaximumFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 2, 2, 1, 31),
    _LldpNeighborMaximumFrameSize_Type()
)
lldpNeighborMaximumFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborMaximumFrameSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-LLDPINFO-MIB",
    **{"lldpInfo": lldpInfo,
       "lldpLocalInfoTable": lldpLocalInfoTable,
       "lldpLocalInfoEntry": lldpLocalInfoEntry,
       "lldpLocalPortId": lldpLocalPortId,
       "lldpLocalChassisIdType": lldpLocalChassisIdType,
       "lldpLocalChassisId": lldpLocalChassisId,
       "lldpLocalPortIdType": lldpLocalPortIdType,
       "lldpLocalPortIdDescr": lldpLocalPortIdDescr,
       "lldpLocalTtl": lldpLocalTtl,
       "lldpLocalPortDescr": lldpLocalPortDescr,
       "lldpLocalDeviceName": lldpLocalDeviceName,
       "lldpLocalDeviceDescr": lldpLocalDeviceDescr,
       "lldpLocalCapAvailable": lldpLocalCapAvailable,
       "lldpLocalCapEnabled": lldpLocalCapEnabled,
       "lldpLocalManageIpAddr": lldpLocalManageIpAddr,
       "lldpLocalManageAddrType": lldpLocalManageAddrType,
       "lldpLocalManageAddrInterfaceType": lldpLocalManageAddrInterfaceType,
       "lldpLocalManageAddrInterfaceId": lldpLocalManageAddrInterfaceId,
       "lldpLocalManageAddrOID": lldpLocalManageAddrOID,
       "lldpLocalPortAndProtocolVlanID": lldpLocalPortAndProtocolVlanID,
       "lldpLocalVlanName": lldpLocalVlanName,
       "lldpLocalAutoNegotiationSupported": lldpLocalAutoNegotiationSupported,
       "lldpLocalAutoNegotiationEnabled": lldpLocalAutoNegotiationEnabled,
       "lldpLocalOperMau": lldpLocalOperMau,
       "lldpLocalLinkAggregationSupported": lldpLocalLinkAggregationSupported,
       "lldpLocalLinkAggregationEnabled": lldpLocalLinkAggregationEnabled,
       "lldpLocalAggregationPortId": lldpLocalAggregationPortId,
       "lldpLocalPowerPortClass": lldpLocalPowerPortClass,
       "lldpLocalPsePowerSupported": lldpLocalPsePowerSupported,
       "lldpLocalPsePowerEnabled": lldpLocalPsePowerEnabled,
       "lldpLocalPsePairsControlAbility": lldpLocalPsePairsControlAbility,
       "lldpLocalMaximumFrameSize": lldpLocalMaximumFrameSize,
       "lldpNeighborInfoTable": lldpNeighborInfoTable,
       "lldpNeighborInfoEntry": lldpNeighborInfoEntry,
       "lldpNeighborPortId": lldpNeighborPortId,
       "lldpNeighborPortIndexId": lldpNeighborPortIndexId,
       "lldpNeighborChassisIdType": lldpNeighborChassisIdType,
       "lldpNeighborChassisId": lldpNeighborChassisId,
       "lldpNeighborPortIdType": lldpNeighborPortIdType,
       "lldpNeighborPortIdDescr": lldpNeighborPortIdDescr,
       "lldpNeighborTtl": lldpNeighborTtl,
       "lldpNeighborPortDescr": lldpNeighborPortDescr,
       "lldpNeighborDeviceName": lldpNeighborDeviceName,
       "lldpNeighborDeviceDescr": lldpNeighborDeviceDescr,
       "lldpNeighborCapAvailable": lldpNeighborCapAvailable,
       "lldpNeighborCapEnabled": lldpNeighborCapEnabled,
       "lldpNeighborManageIpAddr": lldpNeighborManageIpAddr,
       "lldpNeighborManageAddrType": lldpNeighborManageAddrType,
       "lldpNeighborManageAddrInterfaceType": lldpNeighborManageAddrInterfaceType,
       "lldpNeighborManageAddrInterfaceId": lldpNeighborManageAddrInterfaceId,
       "lldpNeighborManageAddrOID": lldpNeighborManageAddrOID,
       "lldpNeighborPortAndProtocolVlanID": lldpNeighborPortAndProtocolVlanID,
       "lldpNeighborVlanName": lldpNeighborVlanName,
       "lldpNeighborProtocolIdentity": lldpNeighborProtocolIdentity,
       "lldpNeighborAutoNegotiationSupported": lldpNeighborAutoNegotiationSupported,
       "lldpNeighborAutoNegotiationEnabled": lldpNeighborAutoNegotiationEnabled,
       "lldpNeighborOperMau": lldpNeighborOperMau,
       "lldpNeighborLinkAggregationSupported": lldpNeighborLinkAggregationSupported,
       "lldpNeighborLinkAggregationEnabled": lldpNeighborLinkAggregationEnabled,
       "lldpNeighborAggregationPortId": lldpNeighborAggregationPortId,
       "lldpNeighborPowerPortClass": lldpNeighborPowerPortClass,
       "lldpNeighborPsePowerSupported": lldpNeighborPsePowerSupported,
       "lldpNeighborPsePowerEnabled": lldpNeighborPsePowerEnabled,
       "lldpNeighborPsePairsControlAbility": lldpNeighborPsePairsControlAbility,
       "lldpNeighborMaximumFrameSize": lldpNeighborMaximumFrameSize}
)
