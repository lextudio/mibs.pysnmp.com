# SNMP MIB module (MOBANetClocksV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MOBANetClocksV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:35 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

mbnscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100)
)
mbnscMIB.setRevisions(
        ("2014-06-17 12:02",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MOBAAlarm64(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x1x1x1x.1x1x1x1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class MOBAFlags64(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x1x1x1x.1x1x1x1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class MOBANetworkName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



# MIB Managed Objects in the order of their OIDs

_Mobatime_ObjectIdentity = ObjectIdentity
mobatime = _Mobatime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842)
)
_MobaNetClocks_ObjectIdentity = ObjectIdentity
mobaNetClocks = _MobaNetClocks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6)
)
_MobaNetClocksV2_ObjectIdentity = ObjectIdentity
mobaNetClocksV2 = _MobaNetClocksV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2)
)
_MbnscNet_ObjectIdentity = ObjectIdentity
mbnscNet = _MbnscNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1)
)
_MbnscNetGen_ObjectIdentity = ObjectIdentity
mbnscNetGen = _MbnscNetGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1)
)


class _MbnscNetGenMAC_Type(OctetString):
    """Custom type mbnscNetGenMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MbnscNetGenMAC_Type.__name__ = "OctetString"
_MbnscNetGenMAC_Object = MibScalar
mbnscNetGenMAC = _MbnscNetGenMAC_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 1),
    _MbnscNetGenMAC_Type()
)
mbnscNetGenMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetGenMAC.setStatus("current")


class _MbnscNetGenIPMode_Type(Integer32):
    """Custom type mbnscNetGenIPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("ipv4only", 1),
          ("ipv6only", 2))
    )


_MbnscNetGenIPMode_Type.__name__ = "Integer32"
_MbnscNetGenIPMode_Object = MibScalar
mbnscNetGenIPMode = _MbnscNetGenIPMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 2),
    _MbnscNetGenIPMode_Type()
)
mbnscNetGenIPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenIPMode.setStatus("current")


class _MbnscNetGenIPNameserver_Type(DisplayString):
    """Custom type mbnscNetGenIPNameserver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscNetGenIPNameserver_Type.__name__ = "DisplayString"
_MbnscNetGenIPNameserver_Object = MibScalar
mbnscNetGenIPNameserver = _MbnscNetGenIPNameserver_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 3),
    _MbnscNetGenIPNameserver_Type()
)
mbnscNetGenIPNameserver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenIPNameserver.setStatus("current")


class _MbnscNetGenTZClientPort_Type(Unsigned32):
    """Custom type mbnscNetGenTZClientPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MbnscNetGenTZClientPort_Type.__name__ = "Unsigned32"
_MbnscNetGenTZClientPort_Object = MibScalar
mbnscNetGenTZClientPort = _MbnscNetGenTZClientPort_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 4),
    _MbnscNetGenTZClientPort_Type()
)
mbnscNetGenTZClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenTZClientPort.setStatus("current")


class _MbnscNetGenConfigPort_Type(Unsigned32):
    """Custom type mbnscNetGenConfigPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MbnscNetGenConfigPort_Type.__name__ = "Unsigned32"
_MbnscNetGenConfigPort_Object = MibScalar
mbnscNetGenConfigPort = _MbnscNetGenConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 5),
    _MbnscNetGenConfigPort_Type()
)
mbnscNetGenConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenConfigPort.setStatus("current")


class _MbnscNetGenSnmpMode_Type(Unsigned32):
    """Custom type mbnscNetGenSnmpMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscNetGenSnmpMode_Type.__name__ = "Unsigned32"
_MbnscNetGenSnmpMode_Object = MibScalar
mbnscNetGenSnmpMode = _MbnscNetGenSnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 6),
    _MbnscNetGenSnmpMode_Type()
)
mbnscNetGenSnmpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetGenSnmpMode.setStatus("current")


class _MbnscNetGenMulticastMode_Type(Unsigned32):
    """Custom type mbnscNetGenMulticastMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscNetGenMulticastMode_Type.__name__ = "Unsigned32"
_MbnscNetGenMulticastMode_Object = MibScalar
mbnscNetGenMulticastMode = _MbnscNetGenMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 7),
    _MbnscNetGenMulticastMode_Type()
)
mbnscNetGenMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenMulticastMode.setStatus("current")


class _MbnscNetGenHostname_Type(DisplayString):
    """Custom type mbnscNetGenHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MbnscNetGenHostname_Type.__name__ = "DisplayString"
_MbnscNetGenHostname_Object = MibScalar
mbnscNetGenHostname = _MbnscNetGenHostname_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 8),
    _MbnscNetGenHostname_Type()
)
mbnscNetGenHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenHostname.setStatus("current")


class _MbnscNetGenCommMode_Type(Unsigned32):
    """Custom type mbnscNetGenCommMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscNetGenCommMode_Type.__name__ = "Unsigned32"
_MbnscNetGenCommMode_Object = MibScalar
mbnscNetGenCommMode = _MbnscNetGenCommMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 9),
    _MbnscNetGenCommMode_Type()
)
mbnscNetGenCommMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetGenCommMode.setStatus("current")
_MbnscNetGenMCastGrpIP_Type = IpAddress
_MbnscNetGenMCastGrpIP_Object = MibScalar
mbnscNetGenMCastGrpIP = _MbnscNetGenMCastGrpIP_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 10),
    _MbnscNetGenMCastGrpIP_Type()
)
mbnscNetGenMCastGrpIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenMCastGrpIP.setStatus("current")


class _MbnscNetGenConfigCmd_Type(Unsigned32):
    """Custom type mbnscNetGenConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscNetGenConfigCmd_Type.__name__ = "Unsigned32"
_MbnscNetGenConfigCmd_Object = MibScalar
mbnscNetGenConfigCmd = _MbnscNetGenConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 100),
    _MbnscNetGenConfigCmd_Type()
)
mbnscNetGenConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetGenConfigCmd.setStatus("current")
_MbnscNetGenConfigChangedTime_Type = TimeTicks
_MbnscNetGenConfigChangedTime_Object = MibScalar
mbnscNetGenConfigChangedTime = _MbnscNetGenConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 1, 101),
    _MbnscNetGenConfigChangedTime_Type()
)
mbnscNetGenConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetGenConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscNetGenConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscNetIPv4_ObjectIdentity = ObjectIdentity
mbnscNetIPv4 = _MbnscNetIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 2)
)
_MbnscNetIPv4Addr_Type = IpAddress
_MbnscNetIPv4Addr_Object = MibScalar
mbnscNetIPv4Addr = _MbnscNetIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 2, 1),
    _MbnscNetIPv4Addr_Type()
)
mbnscNetIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv4Addr.setStatus("current")
_MbnscNetIPv4Mask_Type = IpAddress
_MbnscNetIPv4Mask_Object = MibScalar
mbnscNetIPv4Mask = _MbnscNetIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 2, 2),
    _MbnscNetIPv4Mask_Type()
)
mbnscNetIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv4Mask.setStatus("current")
_MbnscNetIPv4Gateway_Type = IpAddress
_MbnscNetIPv4Gateway_Object = MibScalar
mbnscNetIPv4Gateway = _MbnscNetIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 2, 3),
    _MbnscNetIPv4Gateway_Type()
)
mbnscNetIPv4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv4Gateway.setStatus("current")


class _MbnscNetIPv4DHCPMode_Type(Unsigned32):
    """Custom type mbnscNetIPv4DHCPMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscNetIPv4DHCPMode_Type.__name__ = "Unsigned32"
_MbnscNetIPv4DHCPMode_Object = MibScalar
mbnscNetIPv4DHCPMode = _MbnscNetIPv4DHCPMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 2, 4),
    _MbnscNetIPv4DHCPMode_Type()
)
mbnscNetIPv4DHCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv4DHCPMode.setStatus("current")


class _MbnscNetIPv4ConfigCmd_Type(Unsigned32):
    """Custom type mbnscNetIPv4ConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscNetIPv4ConfigCmd_Type.__name__ = "Unsigned32"
_MbnscNetIPv4ConfigCmd_Object = MibScalar
mbnscNetIPv4ConfigCmd = _MbnscNetIPv4ConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 2, 100),
    _MbnscNetIPv4ConfigCmd_Type()
)
mbnscNetIPv4ConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv4ConfigCmd.setStatus("current")
_MbnscNetIPv4ConfigChangedTime_Type = TimeTicks
_MbnscNetIPv4ConfigChangedTime_Object = MibScalar
mbnscNetIPv4ConfigChangedTime = _MbnscNetIPv4ConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 2, 101),
    _MbnscNetIPv4ConfigChangedTime_Type()
)
mbnscNetIPv4ConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetIPv4ConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscNetIPv4ConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscNetIPv6_ObjectIdentity = ObjectIdentity
mbnscNetIPv6 = _MbnscNetIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3)
)


class _MbnscNetIPv6AddrLocal_Type(DisplayString):
    """Custom type mbnscNetIPv6AddrLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscNetIPv6AddrLocal_Type.__name__ = "DisplayString"
_MbnscNetIPv6AddrLocal_Object = MibScalar
mbnscNetIPv6AddrLocal = _MbnscNetIPv6AddrLocal_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 1),
    _MbnscNetIPv6AddrLocal_Type()
)
mbnscNetIPv6AddrLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetIPv6AddrLocal.setStatus("current")


class _MbnscNetIPv6AddrAuto_Type(DisplayString):
    """Custom type mbnscNetIPv6AddrAuto based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscNetIPv6AddrAuto_Type.__name__ = "DisplayString"
_MbnscNetIPv6AddrAuto_Object = MibScalar
mbnscNetIPv6AddrAuto = _MbnscNetIPv6AddrAuto_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 2),
    _MbnscNetIPv6AddrAuto_Type()
)
mbnscNetIPv6AddrAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetIPv6AddrAuto.setStatus("current")


class _MbnscNetIPv6AddrDHCP_Type(DisplayString):
    """Custom type mbnscNetIPv6AddrDHCP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscNetIPv6AddrDHCP_Type.__name__ = "DisplayString"
_MbnscNetIPv6AddrDHCP_Object = MibScalar
mbnscNetIPv6AddrDHCP = _MbnscNetIPv6AddrDHCP_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 3),
    _MbnscNetIPv6AddrDHCP_Type()
)
mbnscNetIPv6AddrDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetIPv6AddrDHCP.setStatus("current")


class _MbnscNetIPv6AddrFix_Type(MOBANetworkName):
    """Custom type mbnscNetIPv6AddrFix based on MOBANetworkName"""
    subtypeSpec = MOBANetworkName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_MbnscNetIPv6AddrFix_Type.__name__ = "MOBANetworkName"
_MbnscNetIPv6AddrFix_Object = MibScalar
mbnscNetIPv6AddrFix = _MbnscNetIPv6AddrFix_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 4),
    _MbnscNetIPv6AddrFix_Type()
)
mbnscNetIPv6AddrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv6AddrFix.setStatus("current")


class _MbnscNetIPv6Prefix_Type(Unsigned32):
    """Custom type mbnscNetIPv6Prefix based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MbnscNetIPv6Prefix_Type.__name__ = "Unsigned32"
_MbnscNetIPv6Prefix_Object = MibScalar
mbnscNetIPv6Prefix = _MbnscNetIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 5),
    _MbnscNetIPv6Prefix_Type()
)
mbnscNetIPv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv6Prefix.setStatus("current")


class _MbnscNetIPv6Gateway_Type(DisplayString):
    """Custom type mbnscNetIPv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscNetIPv6Gateway_Type.__name__ = "DisplayString"
_MbnscNetIPv6Gateway_Object = MibScalar
mbnscNetIPv6Gateway = _MbnscNetIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 6),
    _MbnscNetIPv6Gateway_Type()
)
mbnscNetIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetIPv6Gateway.setStatus("current")


class _MbnscNetIPv6Config_Type(Integer32):
    """Custom type mbnscNetIPv6Config based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoonly", 1),
          ("both", 0),
          ("dhcpv6only", 2),
          ("none", 3))
    )


_MbnscNetIPv6Config_Type.__name__ = "Integer32"
_MbnscNetIPv6Config_Object = MibScalar
mbnscNetIPv6Config = _MbnscNetIPv6Config_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 7),
    _MbnscNetIPv6Config_Type()
)
mbnscNetIPv6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv6Config.setStatus("current")


class _MbnscNetIPv6ConfigCmd_Type(Unsigned32):
    """Custom type mbnscNetIPv6ConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscNetIPv6ConfigCmd_Type.__name__ = "Unsigned32"
_MbnscNetIPv6ConfigCmd_Object = MibScalar
mbnscNetIPv6ConfigCmd = _MbnscNetIPv6ConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 100),
    _MbnscNetIPv6ConfigCmd_Type()
)
mbnscNetIPv6ConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNetIPv6ConfigCmd.setStatus("current")
_MbnscNetIPv6ConfigChangedTime_Type = TimeTicks
_MbnscNetIPv6ConfigChangedTime_Object = MibScalar
mbnscNetIPv6ConfigChangedTime = _MbnscNetIPv6ConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 1, 3, 101),
    _MbnscNetIPv6ConfigChangedTime_Type()
)
mbnscNetIPv6ConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNetIPv6ConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscNetIPv6ConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscTime_ObjectIdentity = ObjectIdentity
mbnscTime = _MbnscTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2)
)


class _MbnscTimeNTP1_Type(DisplayString):
    """Custom type mbnscTimeNTP1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscTimeNTP1_Type.__name__ = "DisplayString"
_MbnscTimeNTP1_Object = MibScalar
mbnscTimeNTP1 = _MbnscTimeNTP1_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 1),
    _MbnscTimeNTP1_Type()
)
mbnscTimeNTP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeNTP1.setStatus("current")


class _MbnscTimeNTP2_Type(DisplayString):
    """Custom type mbnscTimeNTP2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscTimeNTP2_Type.__name__ = "DisplayString"
_MbnscTimeNTP2_Object = MibScalar
mbnscTimeNTP2 = _MbnscTimeNTP2_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 2),
    _MbnscTimeNTP2_Type()
)
mbnscTimeNTP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeNTP2.setStatus("current")


class _MbnscTimeNTP3_Type(DisplayString):
    """Custom type mbnscTimeNTP3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscTimeNTP3_Type.__name__ = "DisplayString"
_MbnscTimeNTP3_Object = MibScalar
mbnscTimeNTP3 = _MbnscTimeNTP3_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 3),
    _MbnscTimeNTP3_Type()
)
mbnscTimeNTP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeNTP3.setStatus("current")


class _MbnscTimeNTP4_Type(DisplayString):
    """Custom type mbnscTimeNTP4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscTimeNTP4_Type.__name__ = "DisplayString"
_MbnscTimeNTP4_Object = MibScalar
mbnscTimeNTP4 = _MbnscTimeNTP4_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 4),
    _MbnscTimeNTP4_Type()
)
mbnscTimeNTP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeNTP4.setStatus("current")


class _MbnscTimeNTPcurrent_Type(DisplayString):
    """Custom type mbnscTimeNTPcurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscTimeNTPcurrent_Type.__name__ = "DisplayString"
_MbnscTimeNTPcurrent_Object = MibScalar
mbnscTimeNTPcurrent = _MbnscTimeNTPcurrent_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 5),
    _MbnscTimeNTPcurrent_Type()
)
mbnscTimeNTPcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeNTPcurrent.setStatus("current")


class _MbnscTimeNTPpollIntervall_Type(Unsigned32):
    """Custom type mbnscTimeNTPpollIntervall based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 999),
    )


_MbnscTimeNTPpollIntervall_Type.__name__ = "Unsigned32"
_MbnscTimeNTPpollIntervall_Object = MibScalar
mbnscTimeNTPpollIntervall = _MbnscTimeNTPpollIntervall_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 6),
    _MbnscTimeNTPpollIntervall_Type()
)
mbnscTimeNTPpollIntervall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeNTPpollIntervall.setStatus("current")
_MbnscTimeDeviceTime_Type = Unsigned32
_MbnscTimeDeviceTime_Object = MibScalar
mbnscTimeDeviceTime = _MbnscTimeDeviceTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 7),
    _MbnscTimeDeviceTime_Type()
)
mbnscTimeDeviceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeDeviceTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscTimeDeviceTime.setUnits("Seconds")


class _MbnscTimeLocOffset_Type(Integer32):
    """Custom type mbnscTimeLocOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_MbnscTimeLocOffset_Type.__name__ = "Integer32"
_MbnscTimeLocOffset_Object = MibScalar
mbnscTimeLocOffset = _MbnscTimeLocOffset_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 8),
    _MbnscTimeLocOffset_Type()
)
mbnscTimeLocOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeLocOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbnscTimeLocOffset.setUnits("minutes (min)")
_MbnscTimeLastReception_Type = Unsigned32
_MbnscTimeLastReception_Object = MibScalar
mbnscTimeLastReception = _MbnscTimeLastReception_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 9),
    _MbnscTimeLastReception_Type()
)
mbnscTimeLastReception.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeLastReception.setStatus("current")
if mibBuilder.loadTexts:
    mbnscTimeLastReception.setUnits("Seconds")


class _MbnscTimeConfigCmd_Type(Unsigned32):
    """Custom type mbnscTimeConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscTimeConfigCmd_Type.__name__ = "Unsigned32"
_MbnscTimeConfigCmd_Object = MibScalar
mbnscTimeConfigCmd = _MbnscTimeConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 100),
    _MbnscTimeConfigCmd_Type()
)
mbnscTimeConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeConfigCmd.setStatus("current")
_MbnscTimeConfigChangedTime_Type = TimeTicks
_MbnscTimeConfigChangedTime_Object = MibScalar
mbnscTimeConfigChangedTime = _MbnscTimeConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 2, 101),
    _MbnscTimeConfigChangedTime_Type()
)
mbnscTimeConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscTimeConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscTimeZone_ObjectIdentity = ObjectIdentity
mbnscTimeZone = _MbnscTimeZone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3)
)


class _MbnscTimeZoneVersion_Type(Integer32):
    """Custom type mbnscTimeZoneVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MbnscTimeZoneVersion_Type.__name__ = "Integer32"
_MbnscTimeZoneVersion_Object = MibScalar
mbnscTimeZoneVersion = _MbnscTimeZoneVersion_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 1),
    _MbnscTimeZoneVersion_Type()
)
mbnscTimeZoneVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneVersion.setStatus("current")


class _MbnscTimeZoneNumber_Type(Integer32):
    """Custom type mbnscTimeZoneNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbnscTimeZoneNumber_Type.__name__ = "Integer32"
_MbnscTimeZoneNumber_Object = MibScalar
mbnscTimeZoneNumber = _MbnscTimeZoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 2),
    _MbnscTimeZoneNumber_Type()
)
mbnscTimeZoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeZoneNumber.setStatus("current")


class _MbnscTimeZoneEntry1_Type(OctetString):
    """Custom type mbnscTimeZoneEntry1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_MbnscTimeZoneEntry1_Type.__name__ = "OctetString"
_MbnscTimeZoneEntry1_Object = MibScalar
mbnscTimeZoneEntry1 = _MbnscTimeZoneEntry1_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 3),
    _MbnscTimeZoneEntry1_Type()
)
mbnscTimeZoneEntry1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneEntry1.setStatus("current")


class _MbnscTimeZoneEntry2_Type(OctetString):
    """Custom type mbnscTimeZoneEntry2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_MbnscTimeZoneEntry2_Type.__name__ = "OctetString"
_MbnscTimeZoneEntry2_Object = MibScalar
mbnscTimeZoneEntry2 = _MbnscTimeZoneEntry2_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 4),
    _MbnscTimeZoneEntry2_Type()
)
mbnscTimeZoneEntry2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneEntry2.setStatus("current")


class _MbnscTimeZoneEntry3_Type(OctetString):
    """Custom type mbnscTimeZoneEntry3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_MbnscTimeZoneEntry3_Type.__name__ = "OctetString"
_MbnscTimeZoneEntry3_Object = MibScalar
mbnscTimeZoneEntry3 = _MbnscTimeZoneEntry3_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 5),
    _MbnscTimeZoneEntry3_Type()
)
mbnscTimeZoneEntry3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneEntry3.setStatus("current")


class _MbnscTimeZoneEntry4_Type(OctetString):
    """Custom type mbnscTimeZoneEntry4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_MbnscTimeZoneEntry4_Type.__name__ = "OctetString"
_MbnscTimeZoneEntry4_Object = MibScalar
mbnscTimeZoneEntry4 = _MbnscTimeZoneEntry4_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 6),
    _MbnscTimeZoneEntry4_Type()
)
mbnscTimeZoneEntry4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneEntry4.setStatus("current")


class _MbnscTimeZoneEntry5_Type(OctetString):
    """Custom type mbnscTimeZoneEntry5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_MbnscTimeZoneEntry5_Type.__name__ = "OctetString"
_MbnscTimeZoneEntry5_Object = MibScalar
mbnscTimeZoneEntry5 = _MbnscTimeZoneEntry5_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 7),
    _MbnscTimeZoneEntry5_Type()
)
mbnscTimeZoneEntry5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneEntry5.setStatus("current")


class _MbnscTimeZoneEntry6_Type(OctetString):
    """Custom type mbnscTimeZoneEntry6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_MbnscTimeZoneEntry6_Type.__name__ = "OctetString"
_MbnscTimeZoneEntry6_Object = MibScalar
mbnscTimeZoneEntry6 = _MbnscTimeZoneEntry6_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 8),
    _MbnscTimeZoneEntry6_Type()
)
mbnscTimeZoneEntry6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneEntry6.setStatus("current")


class _MbnscTimeZoneEntry7_Type(OctetString):
    """Custom type mbnscTimeZoneEntry7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )


_MbnscTimeZoneEntry7_Type.__name__ = "OctetString"
_MbnscTimeZoneEntry7_Object = MibScalar
mbnscTimeZoneEntry7 = _MbnscTimeZoneEntry7_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 9),
    _MbnscTimeZoneEntry7_Type()
)
mbnscTimeZoneEntry7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneEntry7.setStatus("current")


class _MbnscTimeZoneConfigCmd_Type(Unsigned32):
    """Custom type mbnscTimeZoneConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscTimeZoneConfigCmd_Type.__name__ = "Unsigned32"
_MbnscTimeZoneConfigCmd_Object = MibScalar
mbnscTimeZoneConfigCmd = _MbnscTimeZoneConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 100),
    _MbnscTimeZoneConfigCmd_Type()
)
mbnscTimeZoneConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscTimeZoneConfigCmd.setStatus("current")
_MbnscTimeZoneConfigChangedTime_Type = TimeTicks
_MbnscTimeZoneConfigChangedTime_Object = MibScalar
mbnscTimeZoneConfigChangedTime = _MbnscTimeZoneConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 3, 101),
    _MbnscTimeZoneConfigChangedTime_Type()
)
mbnscTimeZoneConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscTimeZoneConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscTimeZoneConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscMode_ObjectIdentity = ObjectIdentity
mbnscMode = _MbnscMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4)
)
_MbnscModeSwitchInfo_Type = Integer32
_MbnscModeSwitchInfo_Object = MibScalar
mbnscModeSwitchInfo = _MbnscModeSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 1),
    _MbnscModeSwitchInfo_Type()
)
mbnscModeSwitchInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscModeSwitchInfo.setStatus("current")


class _MbnscModeDisplayBrightness_Type(DisplayString):
    """Custom type mbnscModeDisplayBrightness based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeDisplayBrightness_Type.__name__ = "DisplayString"
_MbnscModeDisplayBrightness_Object = MibScalar
mbnscModeDisplayBrightness = _MbnscModeDisplayBrightness_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 2),
    _MbnscModeDisplayBrightness_Type()
)
mbnscModeDisplayBrightness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeDisplayBrightness.setStatus("current")


class _MbnscModeDisplayFormat_Type(DisplayString):
    """Custom type mbnscModeDisplayFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeDisplayFormat_Type.__name__ = "DisplayString"
_MbnscModeDisplayFormat_Object = MibScalar
mbnscModeDisplayFormat = _MbnscModeDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 3),
    _MbnscModeDisplayFormat_Type()
)
mbnscModeDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeDisplayFormat.setStatus("current")


class _MbnscModeDisplayAlternate_Type(DisplayString):
    """Custom type mbnscModeDisplayAlternate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeDisplayAlternate_Type.__name__ = "DisplayString"
_MbnscModeDisplayAlternate_Object = MibScalar
mbnscModeDisplayAlternate = _MbnscModeDisplayAlternate_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 4),
    _MbnscModeDisplayAlternate_Type()
)
mbnscModeDisplayAlternate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeDisplayAlternate.setStatus("current")


class _MbnscModeNTP_Type(DisplayString):
    """Custom type mbnscModeNTP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeNTP_Type.__name__ = "DisplayString"
_MbnscModeNTP_Object = MibScalar
mbnscModeNTP = _MbnscModeNTP_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 5),
    _MbnscModeNTP_Type()
)
mbnscModeNTP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbnscModeNTP.setStatus("obsolete")


class _MbnscModeIRlock_Type(DisplayString):
    """Custom type mbnscModeIRlock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeIRlock_Type.__name__ = "DisplayString"
_MbnscModeIRlock_Object = MibScalar
mbnscModeIRlock = _MbnscModeIRlock_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 6),
    _MbnscModeIRlock_Type()
)
mbnscModeIRlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeIRlock.setStatus("current")


class _MbnscModeTimeDispZeros_Type(DisplayString):
    """Custom type mbnscModeTimeDispZeros based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeTimeDispZeros_Type.__name__ = "DisplayString"
_MbnscModeTimeDispZeros_Object = MibScalar
mbnscModeTimeDispZeros = _MbnscModeTimeDispZeros_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 7),
    _MbnscModeTimeDispZeros_Type()
)
mbnscModeTimeDispZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeTimeDispZeros.setStatus("current")


class _MbnscModeDateDispZeros_Type(DisplayString):
    """Custom type mbnscModeDateDispZeros based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeDateDispZeros_Type.__name__ = "DisplayString"
_MbnscModeDateDispZeros_Object = MibScalar
mbnscModeDateDispZeros = _MbnscModeDateDispZeros_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 8),
    _MbnscModeDateDispZeros_Type()
)
mbnscModeDateDispZeros.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeDateDispZeros.setStatus("current")


class _MbnscModeTempUnit_Type(DisplayString):
    """Custom type mbnscModeTempUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeTempUnit_Type.__name__ = "DisplayString"
_MbnscModeTempUnit_Object = MibScalar
mbnscModeTempUnit = _MbnscModeTempUnit_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 9),
    _MbnscModeTempUnit_Type()
)
mbnscModeTempUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeTempUnit.setStatus("current")


class _MbnscModeClockOpMode_Type(DisplayString):
    """Custom type mbnscModeClockOpMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeClockOpMode_Type.__name__ = "DisplayString"
_MbnscModeClockOpMode_Object = MibScalar
mbnscModeClockOpMode = _MbnscModeClockOpMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 10),
    _MbnscModeClockOpMode_Type()
)
mbnscModeClockOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeClockOpMode.setStatus("current")


class _MbnscModeNWParam_Type(DisplayString):
    """Custom type mbnscModeNWParam based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeNWParam_Type.__name__ = "DisplayString"
_MbnscModeNWParam_Object = MibScalar
mbnscModeNWParam = _MbnscModeNWParam_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 11),
    _MbnscModeNWParam_Type()
)
mbnscModeNWParam.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbnscModeNWParam.setStatus("obsolete")


class _MbnscModeDispDerating_Type(DisplayString):
    """Custom type mbnscModeDispDerating based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeDispDerating_Type.__name__ = "DisplayString"
_MbnscModeDispDerating_Object = MibScalar
mbnscModeDispDerating = _MbnscModeDispDerating_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 12),
    _MbnscModeDispDerating_Type()
)
mbnscModeDispDerating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeDispDerating.setStatus("current")


class _MbnscModeLightCorr_Type(DisplayString):
    """Custom type mbnscModeLightCorr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscModeLightCorr_Type.__name__ = "DisplayString"
_MbnscModeLightCorr_Object = MibScalar
mbnscModeLightCorr = _MbnscModeLightCorr_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 13),
    _MbnscModeLightCorr_Type()
)
mbnscModeLightCorr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeLightCorr.setStatus("current")
_MbnscAdditionalDigitalClockModes_ObjectIdentity = ObjectIdentity
mbnscAdditionalDigitalClockModes = _MbnscAdditionalDigitalClockModes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30)
)
_MbnscSensors_ObjectIdentity = ObjectIdentity
mbnscSensors = _MbnscSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 1)
)


class _MbnscSensorsTempActivation_Type(DisplayString):
    """Custom type mbnscSensorsTempActivation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscSensorsTempActivation_Type.__name__ = "DisplayString"
_MbnscSensorsTempActivation_Object = MibScalar
mbnscSensorsTempActivation = _MbnscSensorsTempActivation_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 1, 1),
    _MbnscSensorsTempActivation_Type()
)
mbnscSensorsTempActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSensorsTempActivation.setStatus("current")
_MbnscSensorsTemp1IPAddr_Type = IpAddress
_MbnscSensorsTemp1IPAddr_Object = MibScalar
mbnscSensorsTemp1IPAddr = _MbnscSensorsTemp1IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 1, 2),
    _MbnscSensorsTemp1IPAddr_Type()
)
mbnscSensorsTemp1IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSensorsTemp1IPAddr.setStatus("current")
_MbnscSensorsTemp2IPAddr_Type = IpAddress
_MbnscSensorsTemp2IPAddr_Object = MibScalar
mbnscSensorsTemp2IPAddr = _MbnscSensorsTemp2IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 1, 3),
    _MbnscSensorsTemp2IPAddr_Type()
)
mbnscSensorsTemp2IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSensorsTemp2IPAddr.setStatus("current")


class _MbnscSensorsConfigCmd_Type(Unsigned32):
    """Custom type mbnscSensorsConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscSensorsConfigCmd_Type.__name__ = "Unsigned32"
_MbnscSensorsConfigCmd_Object = MibScalar
mbnscSensorsConfigCmd = _MbnscSensorsConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 1, 100),
    _MbnscSensorsConfigCmd_Type()
)
mbnscSensorsConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSensorsConfigCmd.setStatus("current")
_MbnscSensorsConfigChangedTime_Type = TimeTicks
_MbnscSensorsConfigChangedTime_Object = MibScalar
mbnscSensorsConfigChangedTime = _MbnscSensorsConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 1, 101),
    _MbnscSensorsConfigChangedTime_Type()
)
mbnscSensorsConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscSensorsConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscSensorsConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscDA_ObjectIdentity = ObjectIdentity
mbnscDA = _MbnscDA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 2)
)


class _MbnscDASecondCircleDisplay_Type(DisplayString):
    """Custom type mbnscDASecondCircleDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDASecondCircleDisplay_Type.__name__ = "DisplayString"
_MbnscDASecondCircleDisplay_Object = MibScalar
mbnscDASecondCircleDisplay = _MbnscDASecondCircleDisplay_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 2, 1),
    _MbnscDASecondCircleDisplay_Type()
)
mbnscDASecondCircleDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDASecondCircleDisplay.setStatus("current")


class _MbnscDAConfigCmd_Type(Unsigned32):
    """Custom type mbnscDAConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscDAConfigCmd_Type.__name__ = "Unsigned32"
_MbnscDAConfigCmd_Object = MibScalar
mbnscDAConfigCmd = _MbnscDAConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 2, 100),
    _MbnscDAConfigCmd_Type()
)
mbnscDAConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDAConfigCmd.setStatus("current")
_MbnscDAConfigChangedTime_Type = TimeTicks
_MbnscDAConfigChangedTime_Object = MibScalar
mbnscDAConfigChangedTime = _MbnscDAConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 2, 101),
    _MbnscDAConfigChangedTime_Type()
)
mbnscDAConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscDAConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscDAConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscDK_ObjectIdentity = ObjectIdentity
mbnscDK = _MbnscDK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3)
)


class _MbnscDKFirstLanguage_Type(DisplayString):
    """Custom type mbnscDKFirstLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKFirstLanguage_Type.__name__ = "DisplayString"
_MbnscDKFirstLanguage_Object = MibScalar
mbnscDKFirstLanguage = _MbnscDKFirstLanguage_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 1),
    _MbnscDKFirstLanguage_Type()
)
mbnscDKFirstLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKFirstLanguage.setStatus("current")


class _MbnscDKSecondLanguage_Type(DisplayString):
    """Custom type mbnscDKSecondLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKSecondLanguage_Type.__name__ = "DisplayString"
_MbnscDKSecondLanguage_Object = MibScalar
mbnscDKSecondLanguage = _MbnscDKSecondLanguage_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 2),
    _MbnscDKSecondLanguage_Type()
)
mbnscDKSecondLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKSecondLanguage.setStatus("current")


class _MbnscDKThirdLanguage_Type(DisplayString):
    """Custom type mbnscDKThirdLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKThirdLanguage_Type.__name__ = "DisplayString"
_MbnscDKThirdLanguage_Object = MibScalar
mbnscDKThirdLanguage = _MbnscDKThirdLanguage_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 3),
    _MbnscDKThirdLanguage_Type()
)
mbnscDKThirdLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKThirdLanguage.setStatus("current")


class _MbnscDKTempUnitSecondLang_Type(DisplayString):
    """Custom type mbnscDKTempUnitSecondLang based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKTempUnitSecondLang_Type.__name__ = "DisplayString"
_MbnscDKTempUnitSecondLang_Object = MibScalar
mbnscDKTempUnitSecondLang = _MbnscDKTempUnitSecondLang_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 4),
    _MbnscDKTempUnitSecondLang_Type()
)
mbnscDKTempUnitSecondLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKTempUnitSecondLang.setStatus("current")


class _MbnscDKTempUnitThirdLang_Type(DisplayString):
    """Custom type mbnscDKTempUnitThirdLang based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKTempUnitThirdLang_Type.__name__ = "DisplayString"
_MbnscDKTempUnitThirdLang_Object = MibScalar
mbnscDKTempUnitThirdLang = _MbnscDKTempUnitThirdLang_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 5),
    _MbnscDKTempUnitThirdLang_Type()
)
mbnscDKTempUnitThirdLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKTempUnitThirdLang.setStatus("current")


class _MbnscDKAutoLangSwitchOver_Type(DisplayString):
    """Custom type mbnscDKAutoLangSwitchOver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKAutoLangSwitchOver_Type.__name__ = "DisplayString"
_MbnscDKAutoLangSwitchOver_Object = MibScalar
mbnscDKAutoLangSwitchOver = _MbnscDKAutoLangSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 6),
    _MbnscDKAutoLangSwitchOver_Type()
)
mbnscDKAutoLangSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKAutoLangSwitchOver.setStatus("current")


class _MbnscDKNumOfCharsForWeekday_Type(DisplayString):
    """Custom type mbnscDKNumOfCharsForWeekday based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKNumOfCharsForWeekday_Type.__name__ = "DisplayString"
_MbnscDKNumOfCharsForWeekday_Object = MibScalar
mbnscDKNumOfCharsForWeekday = _MbnscDKNumOfCharsForWeekday_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 7),
    _MbnscDKNumOfCharsForWeekday_Type()
)
mbnscDKNumOfCharsForWeekday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKNumOfCharsForWeekday.setStatus("current")


class _MbnscDKNamesFormatDisplay_Type(DisplayString):
    """Custom type mbnscDKNamesFormatDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKNamesFormatDisplay_Type.__name__ = "DisplayString"
_MbnscDKNamesFormatDisplay_Object = MibScalar
mbnscDKNamesFormatDisplay = _MbnscDKNamesFormatDisplay_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 8),
    _MbnscDKNamesFormatDisplay_Type()
)
mbnscDKNamesFormatDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKNamesFormatDisplay.setStatus("current")


class _MbnscDKTemp1DescriptEnable_Type(DisplayString):
    """Custom type mbnscDKTemp1DescriptEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKTemp1DescriptEnable_Type.__name__ = "DisplayString"
_MbnscDKTemp1DescriptEnable_Object = MibScalar
mbnscDKTemp1DescriptEnable = _MbnscDKTemp1DescriptEnable_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 9),
    _MbnscDKTemp1DescriptEnable_Type()
)
mbnscDKTemp1DescriptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKTemp1DescriptEnable.setStatus("current")


class _MbnscDKTemp1Description_Type(DisplayString):
    """Custom type mbnscDKTemp1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MbnscDKTemp1Description_Type.__name__ = "DisplayString"
_MbnscDKTemp1Description_Object = MibScalar
mbnscDKTemp1Description = _MbnscDKTemp1Description_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 10),
    _MbnscDKTemp1Description_Type()
)
mbnscDKTemp1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKTemp1Description.setStatus("current")


class _MbnscDKTemp2DescriptEnable_Type(DisplayString):
    """Custom type mbnscDKTemp2DescriptEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKTemp2DescriptEnable_Type.__name__ = "DisplayString"
_MbnscDKTemp2DescriptEnable_Object = MibScalar
mbnscDKTemp2DescriptEnable = _MbnscDKTemp2DescriptEnable_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 11),
    _MbnscDKTemp2DescriptEnable_Type()
)
mbnscDKTemp2DescriptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKTemp2DescriptEnable.setStatus("current")


class _MbnscDKTemp2Description_Type(DisplayString):
    """Custom type mbnscDKTemp2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_MbnscDKTemp2Description_Type.__name__ = "DisplayString"
_MbnscDKTemp2Description_Object = MibScalar
mbnscDKTemp2Description = _MbnscDKTemp2Description_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 12),
    _MbnscDKTemp2Description_Type()
)
mbnscDKTemp2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKTemp2Description.setStatus("current")


class _MbnscDKWorldTimeZone1_Type(Integer32):
    """Custom type mbnscDKWorldTimeZone1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbnscDKWorldTimeZone1_Type.__name__ = "Integer32"
_MbnscDKWorldTimeZone1_Object = MibScalar
mbnscDKWorldTimeZone1 = _MbnscDKWorldTimeZone1_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 13),
    _MbnscDKWorldTimeZone1_Type()
)
mbnscDKWorldTimeZone1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone1.setStatus("current")


class _MbnscDKWorldTimeZone1Description_Type(DisplayString):
    """Custom type mbnscDKWorldTimeZone1Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MbnscDKWorldTimeZone1Description_Type.__name__ = "DisplayString"
_MbnscDKWorldTimeZone1Description_Object = MibScalar
mbnscDKWorldTimeZone1Description = _MbnscDKWorldTimeZone1Description_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 14),
    _MbnscDKWorldTimeZone1Description_Type()
)
mbnscDKWorldTimeZone1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone1Description.setStatus("current")


class _MbnscDKWorldTimeZone2_Type(Integer32):
    """Custom type mbnscDKWorldTimeZone2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbnscDKWorldTimeZone2_Type.__name__ = "Integer32"
_MbnscDKWorldTimeZone2_Object = MibScalar
mbnscDKWorldTimeZone2 = _MbnscDKWorldTimeZone2_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 15),
    _MbnscDKWorldTimeZone2_Type()
)
mbnscDKWorldTimeZone2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone2.setStatus("current")


class _MbnscDKWorldTimeZone2Description_Type(DisplayString):
    """Custom type mbnscDKWorldTimeZone2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MbnscDKWorldTimeZone2Description_Type.__name__ = "DisplayString"
_MbnscDKWorldTimeZone2Description_Object = MibScalar
mbnscDKWorldTimeZone2Description = _MbnscDKWorldTimeZone2Description_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 16),
    _MbnscDKWorldTimeZone2Description_Type()
)
mbnscDKWorldTimeZone2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone2Description.setStatus("current")


class _MbnscDKWorldTimeZone3_Type(Integer32):
    """Custom type mbnscDKWorldTimeZone3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbnscDKWorldTimeZone3_Type.__name__ = "Integer32"
_MbnscDKWorldTimeZone3_Object = MibScalar
mbnscDKWorldTimeZone3 = _MbnscDKWorldTimeZone3_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 17),
    _MbnscDKWorldTimeZone3_Type()
)
mbnscDKWorldTimeZone3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone3.setStatus("current")


class _MbnscDKWorldTimeZone3Description_Type(DisplayString):
    """Custom type mbnscDKWorldTimeZone3Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MbnscDKWorldTimeZone3Description_Type.__name__ = "DisplayString"
_MbnscDKWorldTimeZone3Description_Object = MibScalar
mbnscDKWorldTimeZone3Description = _MbnscDKWorldTimeZone3Description_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 18),
    _MbnscDKWorldTimeZone3Description_Type()
)
mbnscDKWorldTimeZone3Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone3Description.setStatus("current")


class _MbnscDKWorldTimeZone4_Type(Integer32):
    """Custom type mbnscDKWorldTimeZone4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbnscDKWorldTimeZone4_Type.__name__ = "Integer32"
_MbnscDKWorldTimeZone4_Object = MibScalar
mbnscDKWorldTimeZone4 = _MbnscDKWorldTimeZone4_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 19),
    _MbnscDKWorldTimeZone4_Type()
)
mbnscDKWorldTimeZone4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone4.setStatus("current")


class _MbnscDKWorldTimeZone4Description_Type(DisplayString):
    """Custom type mbnscDKWorldTimeZone4Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MbnscDKWorldTimeZone4Description_Type.__name__ = "DisplayString"
_MbnscDKWorldTimeZone4Description_Object = MibScalar
mbnscDKWorldTimeZone4Description = _MbnscDKWorldTimeZone4Description_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 20),
    _MbnscDKWorldTimeZone4Description_Type()
)
mbnscDKWorldTimeZone4Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone4Description.setStatus("current")


class _MbnscDKWorldTimeZone5_Type(Integer32):
    """Custom type mbnscDKWorldTimeZone5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MbnscDKWorldTimeZone5_Type.__name__ = "Integer32"
_MbnscDKWorldTimeZone5_Object = MibScalar
mbnscDKWorldTimeZone5 = _MbnscDKWorldTimeZone5_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 21),
    _MbnscDKWorldTimeZone5_Type()
)
mbnscDKWorldTimeZone5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone5.setStatus("current")


class _MbnscDKWorldTimeZone5Description_Type(DisplayString):
    """Custom type mbnscDKWorldTimeZone5Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_MbnscDKWorldTimeZone5Description_Type.__name__ = "DisplayString"
_MbnscDKWorldTimeZone5Description_Object = MibScalar
mbnscDKWorldTimeZone5Description = _MbnscDKWorldTimeZone5Description_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 22),
    _MbnscDKWorldTimeZone5Description_Type()
)
mbnscDKWorldTimeZone5Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKWorldTimeZone5Description.setStatus("current")


class _MbnscDKAutoTimeZoneSwitchOver_Type(DisplayString):
    """Custom type mbnscDKAutoTimeZoneSwitchOver based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MbnscDKAutoTimeZoneSwitchOver_Type.__name__ = "DisplayString"
_MbnscDKAutoTimeZoneSwitchOver_Object = MibScalar
mbnscDKAutoTimeZoneSwitchOver = _MbnscDKAutoTimeZoneSwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 23),
    _MbnscDKAutoTimeZoneSwitchOver_Type()
)
mbnscDKAutoTimeZoneSwitchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKAutoTimeZoneSwitchOver.setStatus("current")


class _MbnscDKConfigCmd_Type(Unsigned32):
    """Custom type mbnscDKConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscDKConfigCmd_Type.__name__ = "Unsigned32"
_MbnscDKConfigCmd_Object = MibScalar
mbnscDKConfigCmd = _MbnscDKConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 100),
    _MbnscDKConfigCmd_Type()
)
mbnscDKConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscDKConfigCmd.setStatus("current")
_MbnscDKConfigChangedTime_Type = TimeTicks
_MbnscDKConfigChangedTime_Object = MibScalar
mbnscDKConfigChangedTime = _MbnscDKConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 30, 3, 101),
    _MbnscDKConfigChangedTime_Type()
)
mbnscDKConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscDKConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscDKConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscAdditionalInterfaceModes_ObjectIdentity = ObjectIdentity
mbnscAdditionalInterfaceModes = _MbnscAdditionalInterfaceModes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40)
)
_MbnscNMI_ObjectIdentity = ObjectIdentity
mbnscNMI = _MbnscNMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1)
)


class _MbnscNMIDCFCurrentLoop_Type(Integer32):
    """Custom type mbnscNMIDCFCurrentLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MbnscNMIDCFCurrentLoop_Type.__name__ = "Integer32"
_MbnscNMIDCFCurrentLoop_Object = MibScalar
mbnscNMIDCFCurrentLoop = _MbnscNMIDCFCurrentLoop_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 1),
    _MbnscNMIDCFCurrentLoop_Type()
)
mbnscNMIDCFCurrentLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNMIDCFCurrentLoop.setStatus("current")


class _MbnscNMILineDriver_Type(Integer32):
    """Custom type mbnscNMILineDriver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activdcf", 2),
          ("mobaline", 1),
          ("off", 0))
    )


_MbnscNMILineDriver_Type.__name__ = "Integer32"
_MbnscNMILineDriver_Object = MibScalar
mbnscNMILineDriver = _MbnscNMILineDriver_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 2),
    _MbnscNMILineDriver_Type()
)
mbnscNMILineDriver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNMILineDriver.setStatus("current")


class _MbnscNMIMOBALineMode_Type(Integer32):
    """Custom type mbnscNMIMOBALineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockidcommand", 2),
          ("command12h", 1),
          ("normal", 0))
    )


_MbnscNMIMOBALineMode_Type.__name__ = "Integer32"
_MbnscNMIMOBALineMode_Object = MibScalar
mbnscNMIMOBALineMode = _MbnscNMIMOBALineMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 3),
    _MbnscNMIMOBALineMode_Type()
)
mbnscNMIMOBALineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNMIMOBALineMode.setStatus("current")


class _MbnscNMIMOBALineMinuteHandMode_Type(Integer32):
    """Custom type mbnscNMIMOBALineMinuteHandMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("halfminutestep", 1),
          ("minutestep", 0))
    )


_MbnscNMIMOBALineMinuteHandMode_Type.__name__ = "Integer32"
_MbnscNMIMOBALineMinuteHandMode_Object = MibScalar
mbnscNMIMOBALineMinuteHandMode = _MbnscNMIMOBALineMinuteHandMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 4),
    _MbnscNMIMOBALineMinuteHandMode_Type()
)
mbnscNMIMOBALineMinuteHandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNMIMOBALineMinuteHandMode.setStatus("current")


class _MbnscNMIActiveDCFMode_Type(Integer32):
    """Custom type mbnscNMIActiveDCFMode based on Integer32"""
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
        *(("mode1", 1),
          ("mode2", 2),
          ("mode3", 3),
          ("mode4", 4),
          ("mode5", 5),
          ("mode6", 6))
    )


_MbnscNMIActiveDCFMode_Type.__name__ = "Integer32"
_MbnscNMIActiveDCFMode_Object = MibScalar
mbnscNMIActiveDCFMode = _MbnscNMIActiveDCFMode_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 5),
    _MbnscNMIActiveDCFMode_Type()
)
mbnscNMIActiveDCFMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNMIActiveDCFMode.setStatus("current")
_MbnscNMISideClockState_ObjectIdentity = ObjectIdentity
mbnscNMISideClockState = _MbnscNMISideClockState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20)
)


class _MbnscNMISideClock1_Type(Integer32):
    """Custom type mbnscNMISideClock1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock1_Type.__name__ = "Integer32"
_MbnscNMISideClock1_Object = MibScalar
mbnscNMISideClock1 = _MbnscNMISideClock1_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 1),
    _MbnscNMISideClock1_Type()
)
mbnscNMISideClock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock1.setStatus("current")


class _MbnscNMISideClock2_Type(Integer32):
    """Custom type mbnscNMISideClock2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock2_Type.__name__ = "Integer32"
_MbnscNMISideClock2_Object = MibScalar
mbnscNMISideClock2 = _MbnscNMISideClock2_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 2),
    _MbnscNMISideClock2_Type()
)
mbnscNMISideClock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock2.setStatus("current")


class _MbnscNMISideClock3_Type(Integer32):
    """Custom type mbnscNMISideClock3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock3_Type.__name__ = "Integer32"
_MbnscNMISideClock3_Object = MibScalar
mbnscNMISideClock3 = _MbnscNMISideClock3_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 3),
    _MbnscNMISideClock3_Type()
)
mbnscNMISideClock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock3.setStatus("current")


class _MbnscNMISideClock4_Type(Integer32):
    """Custom type mbnscNMISideClock4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock4_Type.__name__ = "Integer32"
_MbnscNMISideClock4_Object = MibScalar
mbnscNMISideClock4 = _MbnscNMISideClock4_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 4),
    _MbnscNMISideClock4_Type()
)
mbnscNMISideClock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock4.setStatus("current")


class _MbnscNMISideClock5_Type(Integer32):
    """Custom type mbnscNMISideClock5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock5_Type.__name__ = "Integer32"
_MbnscNMISideClock5_Object = MibScalar
mbnscNMISideClock5 = _MbnscNMISideClock5_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 5),
    _MbnscNMISideClock5_Type()
)
mbnscNMISideClock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock5.setStatus("current")


class _MbnscNMISideClock6_Type(Integer32):
    """Custom type mbnscNMISideClock6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock6_Type.__name__ = "Integer32"
_MbnscNMISideClock6_Object = MibScalar
mbnscNMISideClock6 = _MbnscNMISideClock6_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 6),
    _MbnscNMISideClock6_Type()
)
mbnscNMISideClock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock6.setStatus("current")


class _MbnscNMISideClock7_Type(Integer32):
    """Custom type mbnscNMISideClock7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock7_Type.__name__ = "Integer32"
_MbnscNMISideClock7_Object = MibScalar
mbnscNMISideClock7 = _MbnscNMISideClock7_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 7),
    _MbnscNMISideClock7_Type()
)
mbnscNMISideClock7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock7.setStatus("current")


class _MbnscNMISideClock8_Type(Integer32):
    """Custom type mbnscNMISideClock8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock8_Type.__name__ = "Integer32"
_MbnscNMISideClock8_Object = MibScalar
mbnscNMISideClock8 = _MbnscNMISideClock8_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 8),
    _MbnscNMISideClock8_Type()
)
mbnscNMISideClock8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock8.setStatus("current")


class _MbnscNMISideClock9_Type(Integer32):
    """Custom type mbnscNMISideClock9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock9_Type.__name__ = "Integer32"
_MbnscNMISideClock9_Object = MibScalar
mbnscNMISideClock9 = _MbnscNMISideClock9_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 9),
    _MbnscNMISideClock9_Type()
)
mbnscNMISideClock9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock9.setStatus("current")


class _MbnscNMISideClock10_Type(Integer32):
    """Custom type mbnscNMISideClock10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock10_Type.__name__ = "Integer32"
_MbnscNMISideClock10_Object = MibScalar
mbnscNMISideClock10 = _MbnscNMISideClock10_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 10),
    _MbnscNMISideClock10_Type()
)
mbnscNMISideClock10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock10.setStatus("current")


class _MbnscNMISideClock11_Type(Integer32):
    """Custom type mbnscNMISideClock11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock11_Type.__name__ = "Integer32"
_MbnscNMISideClock11_Object = MibScalar
mbnscNMISideClock11 = _MbnscNMISideClock11_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 11),
    _MbnscNMISideClock11_Type()
)
mbnscNMISideClock11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock11.setStatus("current")


class _MbnscNMISideClock12_Type(Integer32):
    """Custom type mbnscNMISideClock12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clockerror", 5),
          ("clockok", 3),
          ("notconfigured", 0))
    )


_MbnscNMISideClock12_Type.__name__ = "Integer32"
_MbnscNMISideClock12_Object = MibScalar
mbnscNMISideClock12 = _MbnscNMISideClock12_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 20, 12),
    _MbnscNMISideClock12_Type()
)
mbnscNMISideClock12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMISideClock12.setStatus("current")


class _MbnscNMIConfigCmd_Type(Unsigned32):
    """Custom type mbnscNMIConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscNMIConfigCmd_Type.__name__ = "Unsigned32"
_MbnscNMIConfigCmd_Object = MibScalar
mbnscNMIConfigCmd = _MbnscNMIConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 100),
    _MbnscNMIConfigCmd_Type()
)
mbnscNMIConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscNMIConfigCmd.setStatus("current")
_MbnscNMIConfigChangedTime_Type = TimeTicks
_MbnscNMIConfigChangedTime_Object = MibScalar
mbnscNMIConfigChangedTime = _MbnscNMIConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 40, 1, 101),
    _MbnscNMIConfigChangedTime_Type()
)
mbnscNMIConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscNMIConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscNMIConfigChangedTime.setUnits("Time ticks in 1/100th seconds")


class _MbnscModeConfigCmd_Type(Unsigned32):
    """Custom type mbnscModeConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscModeConfigCmd_Type.__name__ = "Unsigned32"
_MbnscModeConfigCmd_Object = MibScalar
mbnscModeConfigCmd = _MbnscModeConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 100),
    _MbnscModeConfigCmd_Type()
)
mbnscModeConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscModeConfigCmd.setStatus("current")
_MbnscModeConfigChangedTime_Type = TimeTicks
_MbnscModeConfigChangedTime_Object = MibScalar
mbnscModeConfigChangedTime = _MbnscModeConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 4, 101),
    _MbnscModeConfigChangedTime_Type()
)
mbnscModeConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscModeConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscModeConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscGeneral_ObjectIdentity = ObjectIdentity
mbnscGeneral = _MbnscGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5)
)


class _MbnscGeneralType_Type(Integer32):
    """Custom type mbnscGeneralType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_MbnscGeneralType_Type.__name__ = "Integer32"
_MbnscGeneralType_Object = MibScalar
mbnscGeneralType = _MbnscGeneralType_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 1),
    _MbnscGeneralType_Type()
)
mbnscGeneralType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralType.setStatus("current")


class _MbnscGeneralName_Type(DisplayString):
    """Custom type mbnscGeneralName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MbnscGeneralName_Type.__name__ = "DisplayString"
_MbnscGeneralName_Object = MibScalar
mbnscGeneralName = _MbnscGeneralName_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 2),
    _MbnscGeneralName_Type()
)
mbnscGeneralName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscGeneralName.setStatus("current")


class _MbnscGeneralFirmwareNumber_Type(DisplayString):
    """Custom type mbnscGeneralFirmwareNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MbnscGeneralFirmwareNumber_Type.__name__ = "DisplayString"
_MbnscGeneralFirmwareNumber_Object = MibScalar
mbnscGeneralFirmwareNumber = _MbnscGeneralFirmwareNumber_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 3),
    _MbnscGeneralFirmwareNumber_Type()
)
mbnscGeneralFirmwareNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralFirmwareNumber.setStatus("current")


class _MbnscGeneralFirmwareVer_Type(DisplayString):
    """Custom type mbnscGeneralFirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MbnscGeneralFirmwareVer_Type.__name__ = "DisplayString"
_MbnscGeneralFirmwareVer_Object = MibScalar
mbnscGeneralFirmwareVer = _MbnscGeneralFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 4),
    _MbnscGeneralFirmwareVer_Type()
)
mbnscGeneralFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralFirmwareVer.setStatus("current")
_MbnscGeneralStatus_Type = MOBAFlags64
_MbnscGeneralStatus_Object = MibScalar
mbnscGeneralStatus = _MbnscGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 5),
    _MbnscGeneralStatus_Type()
)
mbnscGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralStatus.setStatus("current")
_MbnscGeneralAlarms_Type = MOBAAlarm64
_MbnscGeneralAlarms_Object = MibScalar
mbnscGeneralAlarms = _MbnscGeneralAlarms_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 6),
    _MbnscGeneralAlarms_Type()
)
mbnscGeneralAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralAlarms.setStatus("current")


class _MbnscGeneralSlaveInfo1_Type(OctetString):
    """Custom type mbnscGeneralSlaveInfo1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_MbnscGeneralSlaveInfo1_Type.__name__ = "OctetString"
_MbnscGeneralSlaveInfo1_Object = MibScalar
mbnscGeneralSlaveInfo1 = _MbnscGeneralSlaveInfo1_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 7),
    _MbnscGeneralSlaveInfo1_Type()
)
mbnscGeneralSlaveInfo1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralSlaveInfo1.setStatus("current")


class _MbnscGeneralSlaveInfo2_Type(OctetString):
    """Custom type mbnscGeneralSlaveInfo2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_MbnscGeneralSlaveInfo2_Type.__name__ = "OctetString"
_MbnscGeneralSlaveInfo2_Object = MibScalar
mbnscGeneralSlaveInfo2 = _MbnscGeneralSlaveInfo2_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 8),
    _MbnscGeneralSlaveInfo2_Type()
)
mbnscGeneralSlaveInfo2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralSlaveInfo2.setStatus("current")


class _MbnscGeneralSlaveInfo3_Type(OctetString):
    """Custom type mbnscGeneralSlaveInfo3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(26, 26),
    )


_MbnscGeneralSlaveInfo3_Type.__name__ = "OctetString"
_MbnscGeneralSlaveInfo3_Object = MibScalar
mbnscGeneralSlaveInfo3 = _MbnscGeneralSlaveInfo3_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 9),
    _MbnscGeneralSlaveInfo3_Type()
)
mbnscGeneralSlaveInfo3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralSlaveInfo3.setStatus("current")


class _MbnscGeneralConfigCmd_Type(Unsigned32):
    """Custom type mbnscGeneralConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscGeneralConfigCmd_Type.__name__ = "Unsigned32"
_MbnscGeneralConfigCmd_Object = MibScalar
mbnscGeneralConfigCmd = _MbnscGeneralConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 100),
    _MbnscGeneralConfigCmd_Type()
)
mbnscGeneralConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscGeneralConfigCmd.setStatus("current")
_MbnscGeneralConfigChangedTime_Type = TimeTicks
_MbnscGeneralConfigChangedTime_Object = MibScalar
mbnscGeneralConfigChangedTime = _MbnscGeneralConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 5, 101),
    _MbnscGeneralConfigChangedTime_Type()
)
mbnscGeneralConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscGeneralConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscGeneralConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscSupervision_ObjectIdentity = ObjectIdentity
mbnscSupervision = _MbnscSupervision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 6)
)


class _MbnscSNMPManager1_Type(DisplayString):
    """Custom type mbnscSNMPManager1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscSNMPManager1_Type.__name__ = "DisplayString"
_MbnscSNMPManager1_Object = MibScalar
mbnscSNMPManager1 = _MbnscSNMPManager1_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 6, 1),
    _MbnscSNMPManager1_Type()
)
mbnscSNMPManager1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSNMPManager1.setStatus("current")


class _MbnscSNMPManager2_Type(DisplayString):
    """Custom type mbnscSNMPManager2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MbnscSNMPManager2_Type.__name__ = "DisplayString"
_MbnscSNMPManager2_Object = MibScalar
mbnscSNMPManager2 = _MbnscSNMPManager2_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 6, 2),
    _MbnscSNMPManager2_Type()
)
mbnscSNMPManager2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSNMPManager2.setStatus("current")


class _MbnscSNMPTrapAliveMsgInterval_Type(Unsigned32):
    """Custom type mbnscSNMPTrapAliveMsgInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1440),
    )


_MbnscSNMPTrapAliveMsgInterval_Type.__name__ = "Unsigned32"
_MbnscSNMPTrapAliveMsgInterval_Object = MibScalar
mbnscSNMPTrapAliveMsgInterval = _MbnscSNMPTrapAliveMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 6, 3),
    _MbnscSNMPTrapAliveMsgInterval_Type()
)
mbnscSNMPTrapAliveMsgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSNMPTrapAliveMsgInterval.setStatus("current")
if mibBuilder.loadTexts:
    mbnscSNMPTrapAliveMsgInterval.setUnits("minutes (min)")


class _MbnscSNMPConfigCmd_Type(Unsigned32):
    """Custom type mbnscSNMPConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscSNMPConfigCmd_Type.__name__ = "Unsigned32"
_MbnscSNMPConfigCmd_Object = MibScalar
mbnscSNMPConfigCmd = _MbnscSNMPConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 6, 100),
    _MbnscSNMPConfigCmd_Type()
)
mbnscSNMPConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscSNMPConfigCmd.setStatus("current")
_MbnscSNMPConfigChangedTime_Type = TimeTicks
_MbnscSNMPConfigChangedTime_Object = MibScalar
mbnscSNMPConfigChangedTime = _MbnscSNMPConfigChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 6, 101),
    _MbnscSNMPConfigChangedTime_Type()
)
mbnscSNMPConfigChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscSNMPConfigChangedTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscSNMPConfigChangedTime.setUnits("Time ticks in 1/100th seconds")
_MbnscCommand_ObjectIdentity = ObjectIdentity
mbnscCommand = _MbnscCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 7)
)


class _MbnscCommand12Pos_Type(Unsigned32):
    """Custom type mbnscCommand12Pos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscCommand12Pos_Type.__name__ = "Unsigned32"
_MbnscCommand12Pos_Object = MibScalar
mbnscCommand12Pos = _MbnscCommand12Pos_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 7, 1),
    _MbnscCommand12Pos_Type()
)
mbnscCommand12Pos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscCommand12Pos.setStatus("current")


class _MbnscCommandSWReset_Type(Unsigned32):
    """Custom type mbnscCommandSWReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscCommandSWReset_Type.__name__ = "Unsigned32"
_MbnscCommandSWReset_Object = MibScalar
mbnscCommandSWReset = _MbnscCommandSWReset_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 7, 2),
    _MbnscCommandSWReset_Type()
)
mbnscCommandSWReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscCommandSWReset.setStatus("current")


class _MbnscCommandFactorySetting_Type(Unsigned32):
    """Custom type mbnscCommandFactorySetting based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscCommandFactorySetting_Type.__name__ = "Unsigned32"
_MbnscCommandFactorySetting_Object = MibScalar
mbnscCommandFactorySetting = _MbnscCommandFactorySetting_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 7, 3),
    _MbnscCommandFactorySetting_Type()
)
mbnscCommandFactorySetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscCommandFactorySetting.setStatus("current")


class _MbnscCommandFirmwUpd_Type(OctetString):
    """Custom type mbnscCommandFirmwUpd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_MbnscCommandFirmwUpd_Type.__name__ = "OctetString"
_MbnscCommandFirmwUpd_Object = MibScalar
mbnscCommandFirmwUpd = _MbnscCommandFirmwUpd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 7, 4),
    _MbnscCommandFirmwUpd_Type()
)
mbnscCommandFirmwUpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscCommandFirmwUpd.setStatus("current")


class _MbnscCommandExtContact_Type(Integer32):
    """Custom type mbnscCommandExtContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscCommandExtContact_Type.__name__ = "Integer32"
_MbnscCommandExtContact_Object = MibScalar
mbnscCommandExtContact = _MbnscCommandExtContact_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 7, 5),
    _MbnscCommandExtContact_Type()
)
mbnscCommandExtContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbnscCommandExtContact.setStatus("current")


class _MbnscCommandConfigCmd_Type(Unsigned32):
    """Custom type mbnscCommandConfigCmd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_MbnscCommandConfigCmd_Type.__name__ = "Unsigned32"
_MbnscCommandConfigCmd_Object = MibScalar
mbnscCommandConfigCmd = _MbnscCommandConfigCmd_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 7, 100),
    _MbnscCommandConfigCmd_Type()
)
mbnscCommandConfigCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbnscCommandConfigCmd.setStatus("current")
_MbnscSnmpConfig_ObjectIdentity = ObjectIdentity
mbnscSnmpConfig = _MbnscSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 9)
)
_MbnscSnmpCurrentAlarmInfo_ObjectIdentity = ObjectIdentity
mbnscSnmpCurrentAlarmInfo = _MbnscSnmpCurrentAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 9, 1)
)


class _MbnscTrapAlMsgErrorNr_Type(Unsigned32):
    """Custom type mbnscTrapAlMsgErrorNr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MbnscTrapAlMsgErrorNr_Type.__name__ = "Unsigned32"
_MbnscTrapAlMsgErrorNr_Object = MibScalar
mbnscTrapAlMsgErrorNr = _MbnscTrapAlMsgErrorNr_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 9, 1, 1),
    _MbnscTrapAlMsgErrorNr_Type()
)
mbnscTrapAlMsgErrorNr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mbnscTrapAlMsgErrorNr.setStatus("current")


class _MbnscTrapAlMsgErrorState_Type(Unsigned32):
    """Custom type mbnscTrapAlMsgErrorState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MbnscTrapAlMsgErrorState_Type.__name__ = "Unsigned32"
_MbnscTrapAlMsgErrorState_Object = MibScalar
mbnscTrapAlMsgErrorState = _MbnscTrapAlMsgErrorState_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 9, 1, 2),
    _MbnscTrapAlMsgErrorState_Type()
)
mbnscTrapAlMsgErrorState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mbnscTrapAlMsgErrorState.setStatus("current")
_MbnscTrapAlMsgErrorTime_Type = Unsigned32
_MbnscTrapAlMsgErrorTime_Object = MibScalar
mbnscTrapAlMsgErrorTime = _MbnscTrapAlMsgErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 9, 1, 3),
    _MbnscTrapAlMsgErrorTime_Type()
)
mbnscTrapAlMsgErrorTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mbnscTrapAlMsgErrorTime.setStatus("current")
if mibBuilder.loadTexts:
    mbnscTrapAlMsgErrorTime.setUnits("Seconds")
_MbnscTraps_ObjectIdentity = ObjectIdentity
mbnscTraps = _MbnscTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 10)
)
_MbnscMIBCompliance_ObjectIdentity = ObjectIdentity
mbnscMIBCompliance = _MbnscMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 1)
)
_MbnscMIBGroups_ObjectIdentity = ObjectIdentity
mbnscMIBGroups = _MbnscMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2)
)

# Managed Objects groups

mbnscGrpNBU190 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 2)
)
mbnscGrpNBU190.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscNetGenMAC"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPNameserver"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenTZClientPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenSnmpMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMulticastMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenHostname"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenCommMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMCastGrpIP"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Addr"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Mask"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4DHCPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrLocal"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrAuto"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrDHCP"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrFix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Prefix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Config"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPcurrent"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPpollIntervall"),
        ("MOBANetClocksV2-MIB", "mbnscTimeDeviceTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLocOffset"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLastReception"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneVersion"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneNumber"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralType"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralName"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareNumber"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareVer"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralSlaveInfo1"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralSlaveInfo2"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralSlaveInfo3"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager1"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager2"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPTrapAliveMsgInterval"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscCommand12Pos"),
        ("MOBANetClocksV2-MIB", "mbnscCommandSWReset"),
        ("MOBANetClocksV2-MIB", "mbnscCommandConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscGrpNBU190.setStatus("current")

mbnscGrpSEN40 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 3)
)
mbnscGrpSEN40.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscNetGenMAC"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPNameserver"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenTZClientPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenSnmpMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMulticastMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenHostname"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenCommMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMCastGrpIP"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Addr"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Mask"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4DHCPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrLocal"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrAuto"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrDHCP"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrFix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Prefix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Config"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPcurrent"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPpollIntervall"),
        ("MOBANetClocksV2-MIB", "mbnscTimeDeviceTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLocOffset"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLastReception"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneVersion"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneNumber"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralType"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralName"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareNumber"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareVer"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralSlaveInfo1"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager1"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager2"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPTrapAliveMsgInterval"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscCommand12Pos"),
        ("MOBANetClocksV2-MIB", "mbnscCommandSWReset"),
        ("MOBANetClocksV2-MIB", "mbnscCommandConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscGrpSEN40.setStatus("current")

mbnscGrpDC = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 4)
)
mbnscGrpDC.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscNetGenMAC"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPNameserver"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenTZClientPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenSnmpMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMulticastMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenHostname"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenCommMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMCastGrpIP"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Addr"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Mask"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4DHCPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrLocal"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrAuto"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrDHCP"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrFix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Prefix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Config"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPcurrent"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPpollIntervall"),
        ("MOBANetClocksV2-MIB", "mbnscTimeDeviceTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLocOffset"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLastReception"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneVersion"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneNumber"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayBrightness"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayFormat"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayAlternate"),
        ("MOBANetClocksV2-MIB", "mbnscModeIRlock"),
        ("MOBANetClocksV2-MIB", "mbnscModeTimeDispZeros"),
        ("MOBANetClocksV2-MIB", "mbnscModeDateDispZeros"),
        ("MOBANetClocksV2-MIB", "mbnscModeTempUnit"),
        ("MOBANetClocksV2-MIB", "mbnscModeClockOpMode"),
        ("MOBANetClocksV2-MIB", "mbnscModeDispDerating"),
        ("MOBANetClocksV2-MIB", "mbnscModeLightCorr"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTempActivation"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTemp1IPAddr"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTemp2IPAddr"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralType"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralName"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareNumber"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareVer"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager1"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager2"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPTrapAliveMsgInterval"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscCommandSWReset"),
        ("MOBANetClocksV2-MIB", "mbnscCommandConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscGrpDC.setStatus("current")

mbnscGrpECODC = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 5)
)
mbnscGrpECODC.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscNetGenMAC"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPNameserver"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenTZClientPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenSnmpMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMulticastMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenHostname"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenCommMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMCastGrpIP"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Addr"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Mask"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4DHCPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrLocal"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrAuto"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrDHCP"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrFix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Prefix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Config"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPcurrent"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPpollIntervall"),
        ("MOBANetClocksV2-MIB", "mbnscTimeDeviceTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLocOffset"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLastReception"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneVersion"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneNumber"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayBrightness"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayFormat"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayAlternate"),
        ("MOBANetClocksV2-MIB", "mbnscModeDispDerating"),
        ("MOBANetClocksV2-MIB", "mbnscModeLightCorr"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralType"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralName"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareNumber"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareVer"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager1"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager2"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPTrapAliveMsgInterval"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscCommandSWReset"),
        ("MOBANetClocksV2-MIB", "mbnscCommandConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscGrpECODC.setStatus("current")

mbnscGrpDA = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 6)
)
mbnscGrpDA.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscNetGenMAC"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPNameserver"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenTZClientPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenSnmpMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMulticastMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenHostname"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenCommMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMCastGrpIP"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Addr"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Mask"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4DHCPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrLocal"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrAuto"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrDHCP"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrFix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Prefix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Config"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPcurrent"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPpollIntervall"),
        ("MOBANetClocksV2-MIB", "mbnscTimeDeviceTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLocOffset"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLastReception"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneVersion"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneNumber"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayBrightness"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayFormat"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayAlternate"),
        ("MOBANetClocksV2-MIB", "mbnscModeIRlock"),
        ("MOBANetClocksV2-MIB", "mbnscModeTimeDispZeros"),
        ("MOBANetClocksV2-MIB", "mbnscModeDateDispZeros"),
        ("MOBANetClocksV2-MIB", "mbnscModeTempUnit"),
        ("MOBANetClocksV2-MIB", "mbnscModeClockOpMode"),
        ("MOBANetClocksV2-MIB", "mbnscModeDispDerating"),
        ("MOBANetClocksV2-MIB", "mbnscModeLightCorr"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTempActivation"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTemp1IPAddr"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTemp2IPAddr"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscDASecondCircleDisplay"),
        ("MOBANetClocksV2-MIB", "mbnscDAConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscDAConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralType"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralName"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareNumber"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareVer"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager1"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager2"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPTrapAliveMsgInterval"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscCommandSWReset"),
        ("MOBANetClocksV2-MIB", "mbnscCommandConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscGrpDA.setStatus("current")

mbnscGrpDK = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 7)
)
mbnscGrpDK.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscNetGenMAC"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPNameserver"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenTZClientPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenSnmpMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMulticastMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenHostname"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenCommMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMCastGrpIP"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Addr"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Mask"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4DHCPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrLocal"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrAuto"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrDHCP"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrFix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Prefix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Config"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPcurrent"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPpollIntervall"),
        ("MOBANetClocksV2-MIB", "mbnscTimeDeviceTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLocOffset"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLastReception"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneVersion"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneNumber"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayBrightness"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayFormat"),
        ("MOBANetClocksV2-MIB", "mbnscModeDisplayAlternate"),
        ("MOBANetClocksV2-MIB", "mbnscModeIRlock"),
        ("MOBANetClocksV2-MIB", "mbnscModeTimeDispZeros"),
        ("MOBANetClocksV2-MIB", "mbnscModeDateDispZeros"),
        ("MOBANetClocksV2-MIB", "mbnscModeTempUnit"),
        ("MOBANetClocksV2-MIB", "mbnscModeClockOpMode"),
        ("MOBANetClocksV2-MIB", "mbnscModeDispDerating"),
        ("MOBANetClocksV2-MIB", "mbnscModeLightCorr"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTempActivation"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTemp1IPAddr"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsTemp2IPAddr"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSensorsConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscDKFirstLanguage"),
        ("MOBANetClocksV2-MIB", "mbnscDKSecondLanguage"),
        ("MOBANetClocksV2-MIB", "mbnscDKThirdLanguage"),
        ("MOBANetClocksV2-MIB", "mbnscDKTempUnitSecondLang"),
        ("MOBANetClocksV2-MIB", "mbnscDKTempUnitThirdLang"),
        ("MOBANetClocksV2-MIB", "mbnscDKAutoLangSwitchOver"),
        ("MOBANetClocksV2-MIB", "mbnscDKNumOfCharsForWeekday"),
        ("MOBANetClocksV2-MIB", "mbnscDKNamesFormatDisplay"),
        ("MOBANetClocksV2-MIB", "mbnscDKTemp1DescriptEnable"),
        ("MOBANetClocksV2-MIB", "mbnscDKTemp1Description"),
        ("MOBANetClocksV2-MIB", "mbnscDKTemp2DescriptEnable"),
        ("MOBANetClocksV2-MIB", "mbnscDKTemp2Description"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone1"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone1Description"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone2"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone2Description"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone3"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone3Description"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone4"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone4Description"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone5"),
        ("MOBANetClocksV2-MIB", "mbnscDKWorldTimeZone5Description"),
        ("MOBANetClocksV2-MIB", "mbnscDKAutoTimeZoneSwitchOver"),
        ("MOBANetClocksV2-MIB", "mbnscDKConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscDKConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralType"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralName"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareNumber"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareVer"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager1"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager2"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPTrapAliveMsgInterval"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscCommandSWReset"),
        ("MOBANetClocksV2-MIB", "mbnscCommandConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscGrpDK.setStatus("current")

mbnscGrpNMI = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 8)
)
mbnscGrpNMI.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscNetGenMAC"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenIPNameserver"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenTZClientPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigPort"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenSnmpMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMulticastMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenHostname"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenCommMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenMCastGrpIP"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetGenConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Addr"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Mask"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4DHCPMode"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv4ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrLocal"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrAuto"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrDHCP"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6AddrFix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Prefix"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Gateway"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6Config"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNetIPv6ConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTP4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPcurrent"),
        ("MOBANetClocksV2-MIB", "mbnscTimeNTPpollIntervall"),
        ("MOBANetClocksV2-MIB", "mbnscTimeDeviceTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLocOffset"),
        ("MOBANetClocksV2-MIB", "mbnscTimeLastReception"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneVersion"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneNumber"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscModeConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNMIDCFCurrentLoop"),
        ("MOBANetClocksV2-MIB", "mbnscNMILineDriver"),
        ("MOBANetClocksV2-MIB", "mbnscNMIMOBALineMode"),
        ("MOBANetClocksV2-MIB", "mbnscNMIMOBALineMinuteHandMode"),
        ("MOBANetClocksV2-MIB", "mbnscNMIActiveDCFMode"),
        ("MOBANetClocksV2-MIB", "mbnscNMIConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscNMIConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock1"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock2"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock3"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock4"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock5"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock6"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock7"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock8"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock9"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock10"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock11"),
        ("MOBANetClocksV2-MIB", "mbnscNMISideClock12"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralType"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralName"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareNumber"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralFirmwareVer"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager1"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPManager2"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPTrapAliveMsgInterval"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscSNMPConfigChangedTime"),
        ("MOBANetClocksV2-MIB", "mbnscCommand12Pos"),
        ("MOBANetClocksV2-MIB", "mbnscCommandSWReset"),
        ("MOBANetClocksV2-MIB", "mbnscCommandConfigCmd"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscGrpNMI.setStatus("current")

mbnscGrpNotUsedParameters = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 100)
)
mbnscGrpNotUsedParameters.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscTimeZoneEntry1"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneEntry2"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneEntry3"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneEntry4"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneEntry5"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneEntry6"),
        ("MOBANetClocksV2-MIB", "mbnscTimeZoneEntry7"),
        ("MOBANetClocksV2-MIB", "mbnscModeSwitchInfo"),
        ("MOBANetClocksV2-MIB", "mbnscCommandFactorySetting"),
        ("MOBANetClocksV2-MIB", "mbnscCommandFirmwUpd"),
        ("MOBANetClocksV2-MIB", "mbnscCommandExtContact"))
)
if mibBuilder.loadTexts:
    mbnscGrpNotUsedParameters.setStatus("current")


# Notification objects

mbnscTrapsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 10, 1)
)
mbnscTrapsAlarm.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorNr"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorState"),
        ("MOBANetClocksV2-MIB", "mbnscTrapAlMsgErrorTime"))
)
if mibBuilder.loadTexts:
    mbnscTrapsAlarm.setStatus(
        "current"
    )

mbnscTrapsAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 13842, 6, 2, 10, 2)
)
mbnscTrapsAlive.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscGeneralStatus"),
        ("MOBANetClocksV2-MIB", "mbnscGeneralAlarms"))
)
if mibBuilder.loadTexts:
    mbnscTrapsAlive.setStatus(
        "current"
    )


# Notifications groups

mbnscAllNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 2, 1)
)
mbnscAllNotifications.setObjects(
      *(("MOBANetClocksV2-MIB", "mbnscTrapsAlarm"),
        ("MOBANetClocksV2-MIB", "mbnscTrapsAlive"))
)
if mibBuilder.loadTexts:
    mbnscAllNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbnscMIBCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13842, 6, 100, 1, 1)
)
if mibBuilder.loadTexts:
    mbnscMIBCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOBANetClocksV2-MIB",
    **{"MOBAAlarm64": MOBAAlarm64,
       "MOBAFlags64": MOBAFlags64,
       "MOBANetworkName": MOBANetworkName,
       "mobatime": mobatime,
       "mobaNetClocks": mobaNetClocks,
       "mobaNetClocksV2": mobaNetClocksV2,
       "mbnscNet": mbnscNet,
       "mbnscNetGen": mbnscNetGen,
       "mbnscNetGenMAC": mbnscNetGenMAC,
       "mbnscNetGenIPMode": mbnscNetGenIPMode,
       "mbnscNetGenIPNameserver": mbnscNetGenIPNameserver,
       "mbnscNetGenTZClientPort": mbnscNetGenTZClientPort,
       "mbnscNetGenConfigPort": mbnscNetGenConfigPort,
       "mbnscNetGenSnmpMode": mbnscNetGenSnmpMode,
       "mbnscNetGenMulticastMode": mbnscNetGenMulticastMode,
       "mbnscNetGenHostname": mbnscNetGenHostname,
       "mbnscNetGenCommMode": mbnscNetGenCommMode,
       "mbnscNetGenMCastGrpIP": mbnscNetGenMCastGrpIP,
       "mbnscNetGenConfigCmd": mbnscNetGenConfigCmd,
       "mbnscNetGenConfigChangedTime": mbnscNetGenConfigChangedTime,
       "mbnscNetIPv4": mbnscNetIPv4,
       "mbnscNetIPv4Addr": mbnscNetIPv4Addr,
       "mbnscNetIPv4Mask": mbnscNetIPv4Mask,
       "mbnscNetIPv4Gateway": mbnscNetIPv4Gateway,
       "mbnscNetIPv4DHCPMode": mbnscNetIPv4DHCPMode,
       "mbnscNetIPv4ConfigCmd": mbnscNetIPv4ConfigCmd,
       "mbnscNetIPv4ConfigChangedTime": mbnscNetIPv4ConfigChangedTime,
       "mbnscNetIPv6": mbnscNetIPv6,
       "mbnscNetIPv6AddrLocal": mbnscNetIPv6AddrLocal,
       "mbnscNetIPv6AddrAuto": mbnscNetIPv6AddrAuto,
       "mbnscNetIPv6AddrDHCP": mbnscNetIPv6AddrDHCP,
       "mbnscNetIPv6AddrFix": mbnscNetIPv6AddrFix,
       "mbnscNetIPv6Prefix": mbnscNetIPv6Prefix,
       "mbnscNetIPv6Gateway": mbnscNetIPv6Gateway,
       "mbnscNetIPv6Config": mbnscNetIPv6Config,
       "mbnscNetIPv6ConfigCmd": mbnscNetIPv6ConfigCmd,
       "mbnscNetIPv6ConfigChangedTime": mbnscNetIPv6ConfigChangedTime,
       "mbnscTime": mbnscTime,
       "mbnscTimeNTP1": mbnscTimeNTP1,
       "mbnscTimeNTP2": mbnscTimeNTP2,
       "mbnscTimeNTP3": mbnscTimeNTP3,
       "mbnscTimeNTP4": mbnscTimeNTP4,
       "mbnscTimeNTPcurrent": mbnscTimeNTPcurrent,
       "mbnscTimeNTPpollIntervall": mbnscTimeNTPpollIntervall,
       "mbnscTimeDeviceTime": mbnscTimeDeviceTime,
       "mbnscTimeLocOffset": mbnscTimeLocOffset,
       "mbnscTimeLastReception": mbnscTimeLastReception,
       "mbnscTimeConfigCmd": mbnscTimeConfigCmd,
       "mbnscTimeConfigChangedTime": mbnscTimeConfigChangedTime,
       "mbnscTimeZone": mbnscTimeZone,
       "mbnscTimeZoneVersion": mbnscTimeZoneVersion,
       "mbnscTimeZoneNumber": mbnscTimeZoneNumber,
       "mbnscTimeZoneEntry1": mbnscTimeZoneEntry1,
       "mbnscTimeZoneEntry2": mbnscTimeZoneEntry2,
       "mbnscTimeZoneEntry3": mbnscTimeZoneEntry3,
       "mbnscTimeZoneEntry4": mbnscTimeZoneEntry4,
       "mbnscTimeZoneEntry5": mbnscTimeZoneEntry5,
       "mbnscTimeZoneEntry6": mbnscTimeZoneEntry6,
       "mbnscTimeZoneEntry7": mbnscTimeZoneEntry7,
       "mbnscTimeZoneConfigCmd": mbnscTimeZoneConfigCmd,
       "mbnscTimeZoneConfigChangedTime": mbnscTimeZoneConfigChangedTime,
       "mbnscMode": mbnscMode,
       "mbnscModeSwitchInfo": mbnscModeSwitchInfo,
       "mbnscModeDisplayBrightness": mbnscModeDisplayBrightness,
       "mbnscModeDisplayFormat": mbnscModeDisplayFormat,
       "mbnscModeDisplayAlternate": mbnscModeDisplayAlternate,
       "mbnscModeNTP": mbnscModeNTP,
       "mbnscModeIRlock": mbnscModeIRlock,
       "mbnscModeTimeDispZeros": mbnscModeTimeDispZeros,
       "mbnscModeDateDispZeros": mbnscModeDateDispZeros,
       "mbnscModeTempUnit": mbnscModeTempUnit,
       "mbnscModeClockOpMode": mbnscModeClockOpMode,
       "mbnscModeNWParam": mbnscModeNWParam,
       "mbnscModeDispDerating": mbnscModeDispDerating,
       "mbnscModeLightCorr": mbnscModeLightCorr,
       "mbnscAdditionalDigitalClockModes": mbnscAdditionalDigitalClockModes,
       "mbnscSensors": mbnscSensors,
       "mbnscSensorsTempActivation": mbnscSensorsTempActivation,
       "mbnscSensorsTemp1IPAddr": mbnscSensorsTemp1IPAddr,
       "mbnscSensorsTemp2IPAddr": mbnscSensorsTemp2IPAddr,
       "mbnscSensorsConfigCmd": mbnscSensorsConfigCmd,
       "mbnscSensorsConfigChangedTime": mbnscSensorsConfigChangedTime,
       "mbnscDA": mbnscDA,
       "mbnscDASecondCircleDisplay": mbnscDASecondCircleDisplay,
       "mbnscDAConfigCmd": mbnscDAConfigCmd,
       "mbnscDAConfigChangedTime": mbnscDAConfigChangedTime,
       "mbnscDK": mbnscDK,
       "mbnscDKFirstLanguage": mbnscDKFirstLanguage,
       "mbnscDKSecondLanguage": mbnscDKSecondLanguage,
       "mbnscDKThirdLanguage": mbnscDKThirdLanguage,
       "mbnscDKTempUnitSecondLang": mbnscDKTempUnitSecondLang,
       "mbnscDKTempUnitThirdLang": mbnscDKTempUnitThirdLang,
       "mbnscDKAutoLangSwitchOver": mbnscDKAutoLangSwitchOver,
       "mbnscDKNumOfCharsForWeekday": mbnscDKNumOfCharsForWeekday,
       "mbnscDKNamesFormatDisplay": mbnscDKNamesFormatDisplay,
       "mbnscDKTemp1DescriptEnable": mbnscDKTemp1DescriptEnable,
       "mbnscDKTemp1Description": mbnscDKTemp1Description,
       "mbnscDKTemp2DescriptEnable": mbnscDKTemp2DescriptEnable,
       "mbnscDKTemp2Description": mbnscDKTemp2Description,
       "mbnscDKWorldTimeZone1": mbnscDKWorldTimeZone1,
       "mbnscDKWorldTimeZone1Description": mbnscDKWorldTimeZone1Description,
       "mbnscDKWorldTimeZone2": mbnscDKWorldTimeZone2,
       "mbnscDKWorldTimeZone2Description": mbnscDKWorldTimeZone2Description,
       "mbnscDKWorldTimeZone3": mbnscDKWorldTimeZone3,
       "mbnscDKWorldTimeZone3Description": mbnscDKWorldTimeZone3Description,
       "mbnscDKWorldTimeZone4": mbnscDKWorldTimeZone4,
       "mbnscDKWorldTimeZone4Description": mbnscDKWorldTimeZone4Description,
       "mbnscDKWorldTimeZone5": mbnscDKWorldTimeZone5,
       "mbnscDKWorldTimeZone5Description": mbnscDKWorldTimeZone5Description,
       "mbnscDKAutoTimeZoneSwitchOver": mbnscDKAutoTimeZoneSwitchOver,
       "mbnscDKConfigCmd": mbnscDKConfigCmd,
       "mbnscDKConfigChangedTime": mbnscDKConfigChangedTime,
       "mbnscAdditionalInterfaceModes": mbnscAdditionalInterfaceModes,
       "mbnscNMI": mbnscNMI,
       "mbnscNMIDCFCurrentLoop": mbnscNMIDCFCurrentLoop,
       "mbnscNMILineDriver": mbnscNMILineDriver,
       "mbnscNMIMOBALineMode": mbnscNMIMOBALineMode,
       "mbnscNMIMOBALineMinuteHandMode": mbnscNMIMOBALineMinuteHandMode,
       "mbnscNMIActiveDCFMode": mbnscNMIActiveDCFMode,
       "mbnscNMISideClockState": mbnscNMISideClockState,
       "mbnscNMISideClock1": mbnscNMISideClock1,
       "mbnscNMISideClock2": mbnscNMISideClock2,
       "mbnscNMISideClock3": mbnscNMISideClock3,
       "mbnscNMISideClock4": mbnscNMISideClock4,
       "mbnscNMISideClock5": mbnscNMISideClock5,
       "mbnscNMISideClock6": mbnscNMISideClock6,
       "mbnscNMISideClock7": mbnscNMISideClock7,
       "mbnscNMISideClock8": mbnscNMISideClock8,
       "mbnscNMISideClock9": mbnscNMISideClock9,
       "mbnscNMISideClock10": mbnscNMISideClock10,
       "mbnscNMISideClock11": mbnscNMISideClock11,
       "mbnscNMISideClock12": mbnscNMISideClock12,
       "mbnscNMIConfigCmd": mbnscNMIConfigCmd,
       "mbnscNMIConfigChangedTime": mbnscNMIConfigChangedTime,
       "mbnscModeConfigCmd": mbnscModeConfigCmd,
       "mbnscModeConfigChangedTime": mbnscModeConfigChangedTime,
       "mbnscGeneral": mbnscGeneral,
       "mbnscGeneralType": mbnscGeneralType,
       "mbnscGeneralName": mbnscGeneralName,
       "mbnscGeneralFirmwareNumber": mbnscGeneralFirmwareNumber,
       "mbnscGeneralFirmwareVer": mbnscGeneralFirmwareVer,
       "mbnscGeneralStatus": mbnscGeneralStatus,
       "mbnscGeneralAlarms": mbnscGeneralAlarms,
       "mbnscGeneralSlaveInfo1": mbnscGeneralSlaveInfo1,
       "mbnscGeneralSlaveInfo2": mbnscGeneralSlaveInfo2,
       "mbnscGeneralSlaveInfo3": mbnscGeneralSlaveInfo3,
       "mbnscGeneralConfigCmd": mbnscGeneralConfigCmd,
       "mbnscGeneralConfigChangedTime": mbnscGeneralConfigChangedTime,
       "mbnscSupervision": mbnscSupervision,
       "mbnscSNMPManager1": mbnscSNMPManager1,
       "mbnscSNMPManager2": mbnscSNMPManager2,
       "mbnscSNMPTrapAliveMsgInterval": mbnscSNMPTrapAliveMsgInterval,
       "mbnscSNMPConfigCmd": mbnscSNMPConfigCmd,
       "mbnscSNMPConfigChangedTime": mbnscSNMPConfigChangedTime,
       "mbnscCommand": mbnscCommand,
       "mbnscCommand12Pos": mbnscCommand12Pos,
       "mbnscCommandSWReset": mbnscCommandSWReset,
       "mbnscCommandFactorySetting": mbnscCommandFactorySetting,
       "mbnscCommandFirmwUpd": mbnscCommandFirmwUpd,
       "mbnscCommandExtContact": mbnscCommandExtContact,
       "mbnscCommandConfigCmd": mbnscCommandConfigCmd,
       "mbnscSnmpConfig": mbnscSnmpConfig,
       "mbnscSnmpCurrentAlarmInfo": mbnscSnmpCurrentAlarmInfo,
       "mbnscTrapAlMsgErrorNr": mbnscTrapAlMsgErrorNr,
       "mbnscTrapAlMsgErrorState": mbnscTrapAlMsgErrorState,
       "mbnscTrapAlMsgErrorTime": mbnscTrapAlMsgErrorTime,
       "mbnscTraps": mbnscTraps,
       "mbnscTrapsAlarm": mbnscTrapsAlarm,
       "mbnscTrapsAlive": mbnscTrapsAlive,
       "mbnscMIB": mbnscMIB,
       "mbnscMIBCompliance": mbnscMIBCompliance,
       "mbnscMIBCompliances": mbnscMIBCompliances,
       "mbnscMIBGroups": mbnscMIBGroups,
       "mbnscAllNotifications": mbnscAllNotifications,
       "mbnscGrpNBU190": mbnscGrpNBU190,
       "mbnscGrpSEN40": mbnscGrpSEN40,
       "mbnscGrpDC": mbnscGrpDC,
       "mbnscGrpECODC": mbnscGrpECODC,
       "mbnscGrpDA": mbnscGrpDA,
       "mbnscGrpDK": mbnscGrpDK,
       "mbnscGrpNMI": mbnscGrpNMI,
       "mbnscGrpNotUsedParameters": mbnscGrpNotUsedParameters}
)
