# SNMP MIB module (QLGC-adapterInfo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QLGC-adapterInfo-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:52 2024
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

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qlogic_ObjectIdentity = ObjectIdentity
qlogic = _Qlogic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873)
)
_Enet_ObjectIdentity = ObjectIdentity
enet = _Enet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1)
)
_Qlasp_ObjectIdentity = ObjectIdentity
qlasp = _Qlasp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2)
)
_QlaspConfig_ObjectIdentity = ObjectIdentity
qlaspConfig = _QlaspConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 1)
)
_QlaspStat_ObjectIdentity = ObjectIdentity
qlaspStat = _QlaspStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 2)
)
_QlaspTrap_ObjectIdentity = ObjectIdentity
qlaspTrap = _QlaspTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 2, 3)
)
_IfControllers_ObjectIdentity = ObjectIdentity
ifControllers = _IfControllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3)
)
_IfiNumber_Type = Integer32
_IfiNumber_Object = MibScalar
ifiNumber = _IfiNumber_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 1),
    _IfiNumber_Type()
)
ifiNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifiNumber.setStatus("mandatory")
_IfiTable_Object = MibTable
ifiTable = _IfiTable_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ifiTable.setStatus("mandatory")
_IfiEntry_Object = MibTableRow
ifiEntry = _IfiEntry_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1)
)
ifiEntry.setIndexNames(
    (0, "QLGC-adapterInfo-MIB", "ifiIndex"),
)
if mibBuilder.loadTexts:
    ifiEntry.setStatus("mandatory")


class _IfiIndex_Type(Integer32):
    """Custom type ifiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IfiIndex_Type.__name__ = "Integer32"
_IfiIndex_Object = MibTableColumn
ifiIndex = _IfiIndex_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 1),
    _IfiIndex_Type()
)
ifiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifiIndex.setStatus("mandatory")
_IfName_Type = DisplayString
_IfName_Object = MibTableColumn
ifName = _IfName_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 2),
    _IfName_Type()
)
ifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName.setStatus("mandatory")
_IfiDescr_Type = DisplayString
_IfiDescr_Object = MibTableColumn
ifiDescr = _IfiDescr_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 3),
    _IfiDescr_Type()
)
ifiDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifiDescr.setStatus("mandatory")
_IfNetworkAddress_Type = IpAddress
_IfNetworkAddress_Object = MibTableColumn
ifNetworkAddress = _IfNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 4),
    _IfNetworkAddress_Type()
)
ifNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNetworkAddress.setStatus("mandatory")
_IfSubnetMask_Type = IpAddress
_IfSubnetMask_Object = MibTableColumn
ifSubnetMask = _IfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 5),
    _IfSubnetMask_Type()
)
ifSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSubnetMask.setStatus("mandatory")
_IfiPhysAddress_Type = PhysAddress
_IfiPhysAddress_Object = MibTableColumn
ifiPhysAddress = _IfiPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 6),
    _IfiPhysAddress_Type()
)
ifiPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifiPhysAddress.setStatus("mandatory")
_IfPermPhysAddress_Type = PhysAddress
_IfPermPhysAddress_Object = MibTableColumn
ifPermPhysAddress = _IfPermPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 7),
    _IfPermPhysAddress_Type()
)
ifPermPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPermPhysAddress.setStatus("mandatory")


class _IfLinkStatus_Type(Integer32):
    """Custom type ifLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 2),
          ("link-up", 1))
    )


_IfLinkStatus_Type.__name__ = "Integer32"
_IfLinkStatus_Object = MibTableColumn
ifLinkStatus = _IfLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 8),
    _IfLinkStatus_Type()
)
ifLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLinkStatus.setStatus("mandatory")


class _IfState_Type(Integer32):
    """Custom type ifState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adapter-removed", 3),
          ("diagnotic-mode", 2),
          ("lowpower-mode", 4),
          ("normal-mode", 1))
    )


_IfState_Type.__name__ = "Integer32"
_IfState_Object = MibTableColumn
ifState = _IfState_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 9),
    _IfState_Type()
)
ifState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifState.setStatus("mandatory")


class _IfLineSpeed_Type(Integer32):
    """Custom type ifLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("speed-10-Gbps", 6),
          ("speed-10-Mbps", 2),
          ("speed-100-Mbps", 3),
          ("speed-1000-Mbps", 4),
          ("speed-2500-Mbps", 5),
          ("unknown", 1))
    )


_IfLineSpeed_Type.__name__ = "Integer32"
_IfLineSpeed_Object = MibTableColumn
ifLineSpeed = _IfLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 10),
    _IfLineSpeed_Type()
)
ifLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLineSpeed.setStatus("mandatory")


class _IfDuplexMode_Type(Integer32):
    """Custom type ifDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 3),
          ("half-duplex", 2),
          ("unknown", 1))
    )


_IfDuplexMode_Type.__name__ = "Integer32"
_IfDuplexMode_Object = MibTableColumn
ifDuplexMode = _IfDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 11),
    _IfDuplexMode_Type()
)
ifDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDuplexMode.setStatus("mandatory")
_IfMemBaseLow_Type = DisplayString
_IfMemBaseLow_Object = MibTableColumn
ifMemBaseLow = _IfMemBaseLow_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 12),
    _IfMemBaseLow_Type()
)
ifMemBaseLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMemBaseLow.setStatus("mandatory")
_IfMemBaseHigh_Type = DisplayString
_IfMemBaseHigh_Object = MibTableColumn
ifMemBaseHigh = _IfMemBaseHigh_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 13),
    _IfMemBaseHigh_Type()
)
ifMemBaseHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMemBaseHigh.setStatus("mandatory")
_IfInterrupt_Type = Integer32
_IfInterrupt_Object = MibTableColumn
ifInterrupt = _IfInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 14),
    _IfInterrupt_Type()
)
ifInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInterrupt.setStatus("mandatory")
_IfBusNumber_Type = Integer32
_IfBusNumber_Object = MibTableColumn
ifBusNumber = _IfBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 15),
    _IfBusNumber_Type()
)
ifBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBusNumber.setStatus("mandatory")
_IfDeviceNumber_Type = Integer32
_IfDeviceNumber_Object = MibTableColumn
ifDeviceNumber = _IfDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 16),
    _IfDeviceNumber_Type()
)
ifDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDeviceNumber.setStatus("mandatory")
_IfFunctionNumber_Type = Integer32
_IfFunctionNumber_Object = MibTableColumn
ifFunctionNumber = _IfFunctionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 17),
    _IfFunctionNumber_Type()
)
ifFunctionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFunctionNumber.setStatus("mandatory")
_IfIpv6NetworkAddress_Type = InetAddressIPv6
_IfIpv6NetworkAddress_Object = MibTableColumn
ifIpv6NetworkAddress = _IfIpv6NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 18),
    _IfIpv6NetworkAddress_Type()
)
ifIpv6NetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIpv6NetworkAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QLGC-adapterInfo-MIB",
    **{"qlogic": qlogic,
       "enet": enet,
       "qlasp": qlasp,
       "qlaspConfig": qlaspConfig,
       "qlaspStat": qlaspStat,
       "qlaspTrap": qlaspTrap,
       "ifControllers": ifControllers,
       "ifiNumber": ifiNumber,
       "ifiTable": ifiTable,
       "ifiEntry": ifiEntry,
       "ifiIndex": ifiIndex,
       "ifName": ifName,
       "ifiDescr": ifiDescr,
       "ifNetworkAddress": ifNetworkAddress,
       "ifSubnetMask": ifSubnetMask,
       "ifiPhysAddress": ifiPhysAddress,
       "ifPermPhysAddress": ifPermPhysAddress,
       "ifLinkStatus": ifLinkStatus,
       "ifState": ifState,
       "ifLineSpeed": ifLineSpeed,
       "ifDuplexMode": ifDuplexMode,
       "ifMemBaseLow": ifMemBaseLow,
       "ifMemBaseHigh": ifMemBaseHigh,
       "ifInterrupt": ifInterrupt,
       "ifBusNumber": ifBusNumber,
       "ifDeviceNumber": ifDeviceNumber,
       "ifFunctionNumber": ifFunctionNumber,
       "ifIpv6NetworkAddress": ifIpv6NetworkAddress}
)
