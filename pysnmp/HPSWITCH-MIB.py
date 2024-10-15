# SNMP MIB module (HPSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPSWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:33 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddr(OctetString):
    """Custom type MacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Icf_ObjectIdentity = ObjectIdentity
icf = _Icf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14)
)
_IcfEswitch_ObjectIdentity = ObjectIdentity
icfEswitch = _IcfEswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6)
)
_HpEs_ObjectIdentity = ObjectIdentity
hpEs = _HpEs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1)
)
_HpEsMain_ObjectIdentity = ObjectIdentity
hpEsMain = _HpEsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1)
)
_HpEsConfig_ObjectIdentity = ObjectIdentity
hpEsConfig = _HpEsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1)
)
_HpEsFwVer_Type = DisplayString
_HpEsFwVer_Object = MibScalar
hpEsFwVer = _HpEsFwVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 1),
    _HpEsFwVer_Type()
)
hpEsFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsFwVer.setStatus("mandatory")
_HpEsHwVer_Type = DisplayString
_HpEsHwVer_Object = MibScalar
hpEsHwVer = _HpEsHwVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 2),
    _HpEsHwVer_Type()
)
hpEsHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsHwVer.setStatus("mandatory")
_HpEsIpAddr_Type = IpAddress
_HpEsIpAddr_Object = MibScalar
hpEsIpAddr = _HpEsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 3),
    _HpEsIpAddr_Type()
)
hpEsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsIpAddr.setStatus("mandatory")
_HpEsNetMask_Type = IpAddress
_HpEsNetMask_Object = MibScalar
hpEsNetMask = _HpEsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 4),
    _HpEsNetMask_Type()
)
hpEsNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsNetMask.setStatus("mandatory")
_HpEsDefaultGateway_Type = IpAddress
_HpEsDefaultGateway_Object = MibScalar
hpEsDefaultGateway = _HpEsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 5),
    _HpEsDefaultGateway_Type()
)
hpEsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsDefaultGateway.setStatus("mandatory")
_HpEsTrapRcvrMaxEnt_Type = Integer32
_HpEsTrapRcvrMaxEnt_Object = MibScalar
hpEsTrapRcvrMaxEnt = _HpEsTrapRcvrMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 6),
    _HpEsTrapRcvrMaxEnt_Type()
)
hpEsTrapRcvrMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsTrapRcvrMaxEnt.setStatus("mandatory")
_HpEsTrapRcvrCurEnt_Type = Integer32
_HpEsTrapRcvrCurEnt_Object = MibScalar
hpEsTrapRcvrCurEnt = _HpEsTrapRcvrCurEnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 7),
    _HpEsTrapRcvrCurEnt_Type()
)
hpEsTrapRcvrCurEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsTrapRcvrCurEnt.setStatus("mandatory")


class _HpEsTrapRcvrNext_Type(Integer32):
    """Custom type hpEsTrapRcvrNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655535),
    )


_HpEsTrapRcvrNext_Type.__name__ = "Integer32"
_HpEsTrapRcvrNext_Object = MibScalar
hpEsTrapRcvrNext = _HpEsTrapRcvrNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 8),
    _HpEsTrapRcvrNext_Type()
)
hpEsTrapRcvrNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsTrapRcvrNext.setStatus("mandatory")
_HpEsTrapRcvrTable_Object = MibTable
hpEsTrapRcvrTable = _HpEsTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpEsTrapRcvrTable.setStatus("mandatory")
_HpEsTrapRcvrEntry_Object = MibTableRow
hpEsTrapRcvrEntry = _HpEsTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 9, 1)
)
hpEsTrapRcvrEntry.setIndexNames(
    (0, "HPSWITCH-MIB", "hpEsTrapRcvrIndex"),
)
if mibBuilder.loadTexts:
    hpEsTrapRcvrEntry.setStatus("mandatory")


class _HpEsTrapRcvrIndex_Type(Integer32):
    """Custom type hpEsTrapRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpEsTrapRcvrIndex_Type.__name__ = "Integer32"
_HpEsTrapRcvrIndex_Object = MibTableColumn
hpEsTrapRcvrIndex = _HpEsTrapRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 9, 1, 1),
    _HpEsTrapRcvrIndex_Type()
)
hpEsTrapRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsTrapRcvrIndex.setStatus("mandatory")


class _HpEsTrapRcvrStatus_Type(Integer32):
    """Custom type hpEsTrapRcvrStatus based on Integer32"""
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
        *(("create", 4),
          ("invalid", 3),
          ("other", 1),
          ("valid", 2))
    )


_HpEsTrapRcvrStatus_Type.__name__ = "Integer32"
_HpEsTrapRcvrStatus_Object = MibTableColumn
hpEsTrapRcvrStatus = _HpEsTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 9, 1, 2),
    _HpEsTrapRcvrStatus_Type()
)
hpEsTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsTrapRcvrStatus.setStatus("mandatory")
_HpEsTrapRcvrIpAddress_Type = IpAddress
_HpEsTrapRcvrIpAddress_Object = MibTableColumn
hpEsTrapRcvrIpAddress = _HpEsTrapRcvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 9, 1, 3),
    _HpEsTrapRcvrIpAddress_Type()
)
hpEsTrapRcvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsTrapRcvrIpAddress.setStatus("mandatory")
_HpEsTrapRcvrComm_Type = DisplayString
_HpEsTrapRcvrComm_Object = MibTableColumn
hpEsTrapRcvrComm = _HpEsTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 1, 9, 1, 4),
    _HpEsTrapRcvrComm_Type()
)
hpEsTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsTrapRcvrComm.setStatus("mandatory")
_HpEsSys_ObjectIdentity = ObjectIdentity
hpEsSys = _HpEsSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2)
)
_HpEsNumPorts_Type = Integer32
_HpEsNumPorts_Object = MibScalar
hpEsNumPorts = _HpEsNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 1),
    _HpEsNumPorts_Type()
)
hpEsNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsNumPorts.setStatus("mandatory")
_HpEsNumStations_Type = Integer32
_HpEsNumStations_Object = MibScalar
hpEsNumStations = _HpEsNumStations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 2),
    _HpEsNumStations_Type()
)
hpEsNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsNumStations.setStatus("mandatory")
_HpEsMostStations_Type = Integer32
_HpEsMostStations_Object = MibScalar
hpEsMostStations = _HpEsMostStations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 3),
    _HpEsMostStations_Type()
)
hpEsMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsMostStations.setStatus("mandatory")
_HpEsMaxStations_Type = Integer32
_HpEsMaxStations_Object = MibScalar
hpEsMaxStations = _HpEsMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 4),
    _HpEsMaxStations_Type()
)
hpEsMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsMaxStations.setStatus("mandatory")


class _HpEsReset_Type(Integer32):
    """Custom type hpEsReset based on Integer32"""
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
        *(("hardReset", 4),
          ("other", 1),
          ("running", 2),
          ("softReset", 3))
    )


_HpEsReset_Type.__name__ = "Integer32"
_HpEsReset_Object = MibScalar
hpEsReset = _HpEsReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 5),
    _HpEsReset_Type()
)
hpEsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsReset.setStatus("mandatory")
_HpEsNumResets_Type = Counter32
_HpEsNumResets_Object = MibScalar
hpEsNumResets = _HpEsNumResets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 6),
    _HpEsNumResets_Type()
)
hpEsNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsNumResets.setStatus("mandatory")


class _HpEsAddrAgingTime_Type(Integer32):
    """Custom type hpEsAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_HpEsAddrAgingTime_Type.__name__ = "Integer32"
_HpEsAddrAgingTime_Object = MibScalar
hpEsAddrAgingTime = _HpEsAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 7),
    _HpEsAddrAgingTime_Type()
)
hpEsAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsAddrAgingTime.setStatus("mandatory")
_HpEsSysStaTable_Object = MibTable
hpEsSysStaTable = _HpEsSysStaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    hpEsSysStaTable.setStatus("mandatory")
_HpEsSysStaEntry_Object = MibTableRow
hpEsSysStaEntry = _HpEsSysStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 9, 1)
)
hpEsSysStaEntry.setIndexNames(
    (0, "HPSWITCH-MIB", "hpEsSysStaMacAddr"),
)
if mibBuilder.loadTexts:
    hpEsSysStaEntry.setStatus("mandatory")


class _HpEsSysStaMacAddr_Type(OctetString):
    """Custom type hpEsSysStaMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpEsSysStaMacAddr_Type.__name__ = "OctetString"
_HpEsSysStaMacAddr_Object = MibTableColumn
hpEsSysStaMacAddr = _HpEsSysStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 9, 1, 1),
    _HpEsSysStaMacAddr_Type()
)
hpEsSysStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsSysStaMacAddr.setStatus("mandatory")
_HpEsSysStaPort_Type = Integer32
_HpEsSysStaPort_Object = MibTableColumn
hpEsSysStaPort = _HpEsSysStaPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 9, 1, 2),
    _HpEsSysStaPort_Type()
)
hpEsSysStaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsSysStaPort.setStatus("mandatory")
_HpEsSysStaTraffic_Type = OctetString
_HpEsSysStaTraffic_Object = MibTableColumn
hpEsSysStaTraffic = _HpEsSysStaTraffic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 1, 2, 9, 1, 3),
    _HpEsSysStaTraffic_Type()
)
hpEsSysStaTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsSysStaTraffic.setStatus("mandatory")
_HpEsTop_ObjectIdentity = ObjectIdentity
hpEsTop = _HpEsTop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 2)
)
_HpEsPort_ObjectIdentity = ObjectIdentity
hpEsPort = _HpEsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3)
)
_HpEsPortTable_Object = MibTable
hpEsPortTable = _HpEsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpEsPortTable.setStatus("mandatory")
_HpEsPortEntry_Object = MibTableRow
hpEsPortEntry = _HpEsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1)
)
hpEsPortEntry.setIndexNames(
    (0, "HPSWITCH-MIB", "hpEsPortIndex"),
)
if mibBuilder.loadTexts:
    hpEsPortEntry.setStatus("mandatory")


class _HpEsPortIndex_Type(Integer32):
    """Custom type hpEsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpEsPortIndex_Type.__name__ = "Integer32"
_HpEsPortIndex_Object = MibTableColumn
hpEsPortIndex = _HpEsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 1),
    _HpEsPortIndex_Type()
)
hpEsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortIndex.setStatus("mandatory")


class _HpEsPortOprStatus_Type(Integer32):
    """Custom type hpEsPortOprStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpEsPortOprStatus_Type.__name__ = "Integer32"
_HpEsPortOprStatus_Object = MibTableColumn
hpEsPortOprStatus = _HpEsPortOprStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 2),
    _HpEsPortOprStatus_Type()
)
hpEsPortOprStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsPortOprStatus.setStatus("mandatory")


class _HpEsPortExtConn_Type(Integer32):
    """Custom type hpEsPortExtConn based on Integer32"""
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
        *(("aui", 2),
          ("noExternal", 4),
          ("other", 1),
          ("rj45", 3))
    )


_HpEsPortExtConn_Type.__name__ = "Integer32"
_HpEsPortExtConn_Object = MibTableColumn
hpEsPortExtConn = _HpEsPortExtConn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 5),
    _HpEsPortExtConn_Type()
)
hpEsPortExtConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortExtConn.setStatus("mandatory")


class _HpEsPortDuplex_Type(Integer32):
    """Custom type hpEsPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 1),
          ("halfDuplex", 2))
    )


_HpEsPortDuplex_Type.__name__ = "Integer32"
_HpEsPortDuplex_Object = MibTableColumn
hpEsPortDuplex = _HpEsPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 6),
    _HpEsPortDuplex_Type()
)
hpEsPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortDuplex.setStatus("mandatory")
_HpEsPortRcvLocalFrames_Type = Counter32
_HpEsPortRcvLocalFrames_Object = MibTableColumn
hpEsPortRcvLocalFrames = _HpEsPortRcvLocalFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 7),
    _HpEsPortRcvLocalFrames_Type()
)
hpEsPortRcvLocalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortRcvLocalFrames.setStatus("mandatory")
_HpEsPortForwardedFrames_Type = Counter32
_HpEsPortForwardedFrames_Object = MibTableColumn
hpEsPortForwardedFrames = _HpEsPortForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 8),
    _HpEsPortForwardedFrames_Type()
)
hpEsPortForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortForwardedFrames.setStatus("mandatory")
_HpEsPortMostStations_Type = Counter32
_HpEsPortMostStations_Object = MibTableColumn
hpEsPortMostStations = _HpEsPortMostStations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 10),
    _HpEsPortMostStations_Type()
)
hpEsPortMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortMostStations.setStatus("mandatory")
_HpEsPortMaxStations_Type = Counter32
_HpEsPortMaxStations_Object = MibTableColumn
hpEsPortMaxStations = _HpEsPortMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 11),
    _HpEsPortMaxStations_Type()
)
hpEsPortMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortMaxStations.setStatus("mandatory")
_HpEsPortSWHandledFrames_Type = Counter32
_HpEsPortSWHandledFrames_Object = MibTableColumn
hpEsPortSWHandledFrames = _HpEsPortSWHandledFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 12),
    _HpEsPortSWHandledFrames_Type()
)
hpEsPortSWHandledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortSWHandledFrames.setStatus("mandatory")
_HpEsPortLocalStations_Type = Counter32
_HpEsPortLocalStations_Object = MibTableColumn
hpEsPortLocalStations = _HpEsPortLocalStations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 13),
    _HpEsPortLocalStations_Type()
)
hpEsPortLocalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortLocalStations.setStatus("mandatory")
_HpEsPortRemoteStations_Type = Counter32
_HpEsPortRemoteStations_Object = MibTableColumn
hpEsPortRemoteStations = _HpEsPortRemoteStations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 14),
    _HpEsPortRemoteStations_Type()
)
hpEsPortRemoteStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortRemoteStations.setStatus("mandatory")
_HpEsPortUnknownStaFrames_Type = Counter32
_HpEsPortUnknownStaFrames_Object = MibTableColumn
hpEsPortUnknownStaFrames = _HpEsPortUnknownStaFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 15),
    _HpEsPortUnknownStaFrames_Type()
)
hpEsPortUnknownStaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortUnknownStaFrames.setStatus("mandatory")


class _HpEsPortResetStats_Type(Integer32):
    """Custom type hpEsPortResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_HpEsPortResetStats_Type.__name__ = "Integer32"
_HpEsPortResetStats_Object = MibTableColumn
hpEsPortResetStats = _HpEsPortResetStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 16),
    _HpEsPortResetStats_Type()
)
hpEsPortResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsPortResetStats.setStatus("mandatory")
_HpEsPortResetTimer_Type = TimeTicks
_HpEsPortResetTimer_Object = MibTableColumn
hpEsPortResetTimer = _HpEsPortResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 17),
    _HpEsPortResetTimer_Type()
)
hpEsPortResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortResetTimer.setStatus("mandatory")


class _HpEsPortResetAddrs_Type(Integer32):
    """Custom type hpEsPortResetAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_HpEsPortResetAddrs_Type.__name__ = "Integer32"
_HpEsPortResetAddrs_Object = MibTableColumn
hpEsPortResetAddrs = _HpEsPortResetAddrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 18),
    _HpEsPortResetAddrs_Type()
)
hpEsPortResetAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEsPortResetAddrs.setStatus("mandatory")
_HpEsPortRcvBcasts_Type = Counter32
_HpEsPortRcvBcasts_Object = MibTableColumn
hpEsPortRcvBcasts = _HpEsPortRcvBcasts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 20),
    _HpEsPortRcvBcasts_Type()
)
hpEsPortRcvBcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortRcvBcasts.setStatus("mandatory")
_HpEsPortSwitchedFrames_Type = Counter32
_HpEsPortSwitchedFrames_Object = MibTableColumn
hpEsPortSwitchedFrames = _HpEsPortSwitchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1, 3, 1, 1, 25),
    _HpEsPortSwitchedFrames_Type()
)
hpEsPortSwitchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEsPortSwitchedFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPSWITCH-MIB",
    **{"MacAddr": MacAddr,
       "hp": hp,
       "nm": nm,
       "icf": icf,
       "icfEswitch": icfEswitch,
       "hpEs": hpEs,
       "hpEsMain": hpEsMain,
       "hpEsConfig": hpEsConfig,
       "hpEsFwVer": hpEsFwVer,
       "hpEsHwVer": hpEsHwVer,
       "hpEsIpAddr": hpEsIpAddr,
       "hpEsNetMask": hpEsNetMask,
       "hpEsDefaultGateway": hpEsDefaultGateway,
       "hpEsTrapRcvrMaxEnt": hpEsTrapRcvrMaxEnt,
       "hpEsTrapRcvrCurEnt": hpEsTrapRcvrCurEnt,
       "hpEsTrapRcvrNext": hpEsTrapRcvrNext,
       "hpEsTrapRcvrTable": hpEsTrapRcvrTable,
       "hpEsTrapRcvrEntry": hpEsTrapRcvrEntry,
       "hpEsTrapRcvrIndex": hpEsTrapRcvrIndex,
       "hpEsTrapRcvrStatus": hpEsTrapRcvrStatus,
       "hpEsTrapRcvrIpAddress": hpEsTrapRcvrIpAddress,
       "hpEsTrapRcvrComm": hpEsTrapRcvrComm,
       "hpEsSys": hpEsSys,
       "hpEsNumPorts": hpEsNumPorts,
       "hpEsNumStations": hpEsNumStations,
       "hpEsMostStations": hpEsMostStations,
       "hpEsMaxStations": hpEsMaxStations,
       "hpEsReset": hpEsReset,
       "hpEsNumResets": hpEsNumResets,
       "hpEsAddrAgingTime": hpEsAddrAgingTime,
       "hpEsSysStaTable": hpEsSysStaTable,
       "hpEsSysStaEntry": hpEsSysStaEntry,
       "hpEsSysStaMacAddr": hpEsSysStaMacAddr,
       "hpEsSysStaPort": hpEsSysStaPort,
       "hpEsSysStaTraffic": hpEsSysStaTraffic,
       "hpEsTop": hpEsTop,
       "hpEsPort": hpEsPort,
       "hpEsPortTable": hpEsPortTable,
       "hpEsPortEntry": hpEsPortEntry,
       "hpEsPortIndex": hpEsPortIndex,
       "hpEsPortOprStatus": hpEsPortOprStatus,
       "hpEsPortExtConn": hpEsPortExtConn,
       "hpEsPortDuplex": hpEsPortDuplex,
       "hpEsPortRcvLocalFrames": hpEsPortRcvLocalFrames,
       "hpEsPortForwardedFrames": hpEsPortForwardedFrames,
       "hpEsPortMostStations": hpEsPortMostStations,
       "hpEsPortMaxStations": hpEsPortMaxStations,
       "hpEsPortSWHandledFrames": hpEsPortSWHandledFrames,
       "hpEsPortLocalStations": hpEsPortLocalStations,
       "hpEsPortRemoteStations": hpEsPortRemoteStations,
       "hpEsPortUnknownStaFrames": hpEsPortUnknownStaFrames,
       "hpEsPortResetStats": hpEsPortResetStats,
       "hpEsPortResetTimer": hpEsPortResetTimer,
       "hpEsPortResetAddrs": hpEsPortResetAddrs,
       "hpEsPortRcvBcasts": hpEsPortRcvBcasts,
       "hpEsPortSwitchedFrames": hpEsPortSwitchedFrames}
)
