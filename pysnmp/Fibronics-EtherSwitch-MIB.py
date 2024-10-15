# SNMP MIB module (Fibronics-EtherSwitch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fibronics-EtherSwitch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:46 2024
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

_Fibronics_ObjectIdentity = ObjectIdentity
fibronics = _Fibronics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100)
)
_Eth_switch_ObjectIdentity = ObjectIdentity
eth_switch = _Eth_switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9)
)
_Xm516_card_ObjectIdentity = ObjectIdentity
xm516_card = _Xm516_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 3)
)
_Xm517_card_ObjectIdentity = ObjectIdentity
xm517_card = _Xm517_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 4)
)
_Xm518_card_ObjectIdentity = ObjectIdentity
xm518_card = _Xm518_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 5)
)
_Xm519_card_ObjectIdentity = ObjectIdentity
xm519_card = _Xm519_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 6)
)
_Xm5110_card_ObjectIdentity = ObjectIdentity
xm5110_card = _Xm5110_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 7)
)
_Xm5111_card_ObjectIdentity = ObjectIdentity
xm5111_card = _Xm5111_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 8)
)
_Xm5112_card_ObjectIdentity = ObjectIdentity
xm5112_card = _Xm5112_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 9)
)
_Xm5113_card_ObjectIdentity = ObjectIdentity
xm5113_card = _Xm5113_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 10)
)
_Xm5114_card_ObjectIdentity = ObjectIdentity
xm5114_card = _Xm5114_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 11)
)
_Xm5115_card_ObjectIdentity = ObjectIdentity
xm5115_card = _Xm5115_card_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 100, 9, 12)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101)
)
_Mibsbridges_ObjectIdentity = ObjectIdentity
mibsbridges = _Mibsbridges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9)
)
_Mibbridges_specific_ObjectIdentity = ObjectIdentity
mibbridges_specific = _Mibbridges_specific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1)
)
_Mibeth2eth_ObjectIdentity = ObjectIdentity
mibeth2eth = _Mibeth2eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2)
)
_Mib_eps_ObjectIdentity = ObjectIdentity
mib_eps = _Mib_eps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1)
)
_FibEsObjects_ObjectIdentity = ObjectIdentity
fibEsObjects = _FibEsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1)
)
_FibEsMain_ObjectIdentity = ObjectIdentity
fibEsMain = _FibEsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1)
)
_FibEsConfig_ObjectIdentity = ObjectIdentity
fibEsConfig = _FibEsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1)
)
_FibEsFwVer_Type = DisplayString
_FibEsFwVer_Object = MibScalar
fibEsFwVer = _FibEsFwVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 1),
    _FibEsFwVer_Type()
)
fibEsFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsFwVer.setStatus("mandatory")
_FibEsHwVer_Type = DisplayString
_FibEsHwVer_Object = MibScalar
fibEsHwVer = _FibEsHwVer_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 2),
    _FibEsHwVer_Type()
)
fibEsHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsHwVer.setStatus("mandatory")
_FibEsIpAddr_Type = IpAddress
_FibEsIpAddr_Object = MibScalar
fibEsIpAddr = _FibEsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 3),
    _FibEsIpAddr_Type()
)
fibEsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsIpAddr.setStatus("mandatory")
_FibEsNetMask_Type = IpAddress
_FibEsNetMask_Object = MibScalar
fibEsNetMask = _FibEsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 4),
    _FibEsNetMask_Type()
)
fibEsNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsNetMask.setStatus("mandatory")
_FibEsDefaultGateway_Type = IpAddress
_FibEsDefaultGateway_Object = MibScalar
fibEsDefaultGateway = _FibEsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 5),
    _FibEsDefaultGateway_Type()
)
fibEsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsDefaultGateway.setStatus("mandatory")
_FibEsTrapRcvrMaxEnt_Type = Integer32
_FibEsTrapRcvrMaxEnt_Object = MibScalar
fibEsTrapRcvrMaxEnt = _FibEsTrapRcvrMaxEnt_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 6),
    _FibEsTrapRcvrMaxEnt_Type()
)
fibEsTrapRcvrMaxEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsTrapRcvrMaxEnt.setStatus("mandatory")
_FibEsTrapRcvrCurEnt_Type = Integer32
_FibEsTrapRcvrCurEnt_Object = MibScalar
fibEsTrapRcvrCurEnt = _FibEsTrapRcvrCurEnt_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 7),
    _FibEsTrapRcvrCurEnt_Type()
)
fibEsTrapRcvrCurEnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsTrapRcvrCurEnt.setStatus("mandatory")


class _FibEsTrapRcvrNext_Type(Integer32):
    """Custom type fibEsTrapRcvrNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655535),
    )


_FibEsTrapRcvrNext_Type.__name__ = "Integer32"
_FibEsTrapRcvrNext_Object = MibScalar
fibEsTrapRcvrNext = _FibEsTrapRcvrNext_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 8),
    _FibEsTrapRcvrNext_Type()
)
fibEsTrapRcvrNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsTrapRcvrNext.setStatus("mandatory")
_FibEsTrapRcvrTable_Object = MibTable
fibEsTrapRcvrTable = _FibEsTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    fibEsTrapRcvrTable.setStatus("mandatory")
_FibEsTrapRcvrEntry_Object = MibTableRow
fibEsTrapRcvrEntry = _FibEsTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 9, 1)
)
fibEsTrapRcvrEntry.setIndexNames(
    (0, "Fibronics-EtherSwitch-MIB", "fibEsTrapRcvrIndex"),
)
if mibBuilder.loadTexts:
    fibEsTrapRcvrEntry.setStatus("mandatory")


class _FibEsTrapRcvrIndex_Type(Integer32):
    """Custom type fibEsTrapRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FibEsTrapRcvrIndex_Type.__name__ = "Integer32"
_FibEsTrapRcvrIndex_Object = MibTableColumn
fibEsTrapRcvrIndex = _FibEsTrapRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 9, 1, 1),
    _FibEsTrapRcvrIndex_Type()
)
fibEsTrapRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsTrapRcvrIndex.setStatus("mandatory")


class _FibEsTrapRcvrStatus_Type(Integer32):
    """Custom type fibEsTrapRcvrStatus based on Integer32"""
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


_FibEsTrapRcvrStatus_Type.__name__ = "Integer32"
_FibEsTrapRcvrStatus_Object = MibTableColumn
fibEsTrapRcvrStatus = _FibEsTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 9, 1, 2),
    _FibEsTrapRcvrStatus_Type()
)
fibEsTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsTrapRcvrStatus.setStatus("mandatory")
_FibEsTrapRcvrIpAddress_Type = IpAddress
_FibEsTrapRcvrIpAddress_Object = MibTableColumn
fibEsTrapRcvrIpAddress = _FibEsTrapRcvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 9, 1, 3),
    _FibEsTrapRcvrIpAddress_Type()
)
fibEsTrapRcvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsTrapRcvrIpAddress.setStatus("mandatory")
_FibEsTrapRcvrComm_Type = DisplayString
_FibEsTrapRcvrComm_Object = MibTableColumn
fibEsTrapRcvrComm = _FibEsTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 1, 9, 1, 4),
    _FibEsTrapRcvrComm_Type()
)
fibEsTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsTrapRcvrComm.setStatus("mandatory")
_FibEsSys_ObjectIdentity = ObjectIdentity
fibEsSys = _FibEsSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2)
)
_FibEsNumPorts_Type = Integer32
_FibEsNumPorts_Object = MibScalar
fibEsNumPorts = _FibEsNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 1),
    _FibEsNumPorts_Type()
)
fibEsNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsNumPorts.setStatus("mandatory")
_FibEsNumStations_Type = Integer32
_FibEsNumStations_Object = MibScalar
fibEsNumStations = _FibEsNumStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 2),
    _FibEsNumStations_Type()
)
fibEsNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsNumStations.setStatus("mandatory")
_FibEsMostStations_Type = Integer32
_FibEsMostStations_Object = MibScalar
fibEsMostStations = _FibEsMostStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 3),
    _FibEsMostStations_Type()
)
fibEsMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsMostStations.setStatus("mandatory")
_FibEsMaxStations_Type = Integer32
_FibEsMaxStations_Object = MibScalar
fibEsMaxStations = _FibEsMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 4),
    _FibEsMaxStations_Type()
)
fibEsMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsMaxStations.setStatus("mandatory")


class _FibEsReset_Type(Integer32):
    """Custom type fibEsReset based on Integer32"""
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


_FibEsReset_Type.__name__ = "Integer32"
_FibEsReset_Object = MibScalar
fibEsReset = _FibEsReset_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 5),
    _FibEsReset_Type()
)
fibEsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsReset.setStatus("mandatory")
_FibEsNumResets_Type = Counter32
_FibEsNumResets_Object = MibScalar
fibEsNumResets = _FibEsNumResets_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 6),
    _FibEsNumResets_Type()
)
fibEsNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsNumResets.setStatus("mandatory")


class _FibEsAddrAgingTime_Type(Integer32):
    """Custom type fibEsAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_FibEsAddrAgingTime_Type.__name__ = "Integer32"
_FibEsAddrAgingTime_Object = MibScalar
fibEsAddrAgingTime = _FibEsAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 7),
    _FibEsAddrAgingTime_Type()
)
fibEsAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsAddrAgingTime.setStatus("mandatory")
_FibEsSysStaTable_Object = MibTable
fibEsSysStaTable = _FibEsSysStaTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fibEsSysStaTable.setStatus("mandatory")
_FibEsSysStaEntry_Object = MibTableRow
fibEsSysStaEntry = _FibEsSysStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 9, 1)
)
fibEsSysStaEntry.setIndexNames(
    (0, "Fibronics-EtherSwitch-MIB", "fibEsSysStaMacAddr"),
)
if mibBuilder.loadTexts:
    fibEsSysStaEntry.setStatus("mandatory")
_FibEsSysStaMacAddr_Type = MacAddr
_FibEsSysStaMacAddr_Object = MibTableColumn
fibEsSysStaMacAddr = _FibEsSysStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 9, 1, 1),
    _FibEsSysStaMacAddr_Type()
)
fibEsSysStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsSysStaMacAddr.setStatus("mandatory")
_FibEsSysStaPort_Type = Integer32
_FibEsSysStaPort_Object = MibTableColumn
fibEsSysStaPort = _FibEsSysStaPort_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 9, 1, 2),
    _FibEsSysStaPort_Type()
)
fibEsSysStaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsSysStaPort.setStatus("mandatory")
_FibEsSysStaTraffic_Type = OctetString
_FibEsSysStaTraffic_Object = MibTableColumn
fibEsSysStaTraffic = _FibEsSysStaTraffic_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 1, 2, 9, 1, 3),
    _FibEsSysStaTraffic_Type()
)
fibEsSysStaTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsSysStaTraffic.setStatus("mandatory")
_FibEsPort_ObjectIdentity = ObjectIdentity
fibEsPort = _FibEsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2)
)
_FibEsPortTable_Object = MibTable
fibEsPortTable = _FibEsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fibEsPortTable.setStatus("mandatory")
_FibEsPortEntry_Object = MibTableRow
fibEsPortEntry = _FibEsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1)
)
fibEsPortEntry.setIndexNames(
    (0, "Fibronics-EtherSwitch-MIB", "fibEsPortIndex"),
)
if mibBuilder.loadTexts:
    fibEsPortEntry.setStatus("mandatory")


class _FibEsPortIndex_Type(Integer32):
    """Custom type fibEsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FibEsPortIndex_Type.__name__ = "Integer32"
_FibEsPortIndex_Object = MibTableColumn
fibEsPortIndex = _FibEsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 1),
    _FibEsPortIndex_Type()
)
fibEsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortIndex.setStatus("mandatory")


class _FibEsPortOprStatus_Type(Integer32):
    """Custom type fibEsPortOprStatus based on Integer32"""
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


_FibEsPortOprStatus_Type.__name__ = "Integer32"
_FibEsPortOprStatus_Object = MibTableColumn
fibEsPortOprStatus = _FibEsPortOprStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 2),
    _FibEsPortOprStatus_Type()
)
fibEsPortOprStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsPortOprStatus.setStatus("mandatory")


class _FibEsPortDuplex_Type(Integer32):
    """Custom type fibEsPortDuplex based on Integer32"""
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


_FibEsPortDuplex_Type.__name__ = "Integer32"
_FibEsPortDuplex_Object = MibTableColumn
fibEsPortDuplex = _FibEsPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 3),
    _FibEsPortDuplex_Type()
)
fibEsPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortDuplex.setStatus("mandatory")
_FibEsPortRcvLocalFrames_Type = Counter32
_FibEsPortRcvLocalFrames_Object = MibTableColumn
fibEsPortRcvLocalFrames = _FibEsPortRcvLocalFrames_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 4),
    _FibEsPortRcvLocalFrames_Type()
)
fibEsPortRcvLocalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortRcvLocalFrames.setStatus("mandatory")
_FibEsPortForwardedFrames_Type = Counter32
_FibEsPortForwardedFrames_Object = MibTableColumn
fibEsPortForwardedFrames = _FibEsPortForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 5),
    _FibEsPortForwardedFrames_Type()
)
fibEsPortForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortForwardedFrames.setStatus("mandatory")
_FibEsPortMostStations_Type = Counter32
_FibEsPortMostStations_Object = MibTableColumn
fibEsPortMostStations = _FibEsPortMostStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 6),
    _FibEsPortMostStations_Type()
)
fibEsPortMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortMostStations.setStatus("mandatory")
_FibEsPortMaxStations_Type = Counter32
_FibEsPortMaxStations_Object = MibTableColumn
fibEsPortMaxStations = _FibEsPortMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 7),
    _FibEsPortMaxStations_Type()
)
fibEsPortMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortMaxStations.setStatus("mandatory")
_FibEsPortSWHandledFrames_Type = Counter32
_FibEsPortSWHandledFrames_Object = MibTableColumn
fibEsPortSWHandledFrames = _FibEsPortSWHandledFrames_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 8),
    _FibEsPortSWHandledFrames_Type()
)
fibEsPortSWHandledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortSWHandledFrames.setStatus("mandatory")
_FibEsPortLocalStations_Type = Counter32
_FibEsPortLocalStations_Object = MibTableColumn
fibEsPortLocalStations = _FibEsPortLocalStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 9),
    _FibEsPortLocalStations_Type()
)
fibEsPortLocalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortLocalStations.setStatus("mandatory")
_FibEsPortRemoteStations_Type = Counter32
_FibEsPortRemoteStations_Object = MibTableColumn
fibEsPortRemoteStations = _FibEsPortRemoteStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 10),
    _FibEsPortRemoteStations_Type()
)
fibEsPortRemoteStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortRemoteStations.setStatus("mandatory")
_FibEsPortUnknownStaFrames_Type = Counter32
_FibEsPortUnknownStaFrames_Object = MibTableColumn
fibEsPortUnknownStaFrames = _FibEsPortUnknownStaFrames_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 11),
    _FibEsPortUnknownStaFrames_Type()
)
fibEsPortUnknownStaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortUnknownStaFrames.setStatus("mandatory")


class _FibEsPortResetStats_Type(Integer32):
    """Custom type fibEsPortResetStats based on Integer32"""
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


_FibEsPortResetStats_Type.__name__ = "Integer32"
_FibEsPortResetStats_Object = MibTableColumn
fibEsPortResetStats = _FibEsPortResetStats_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 12),
    _FibEsPortResetStats_Type()
)
fibEsPortResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsPortResetStats.setStatus("mandatory")
_FibEsPortResetTimer_Type = TimeTicks
_FibEsPortResetTimer_Object = MibTableColumn
fibEsPortResetTimer = _FibEsPortResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 13),
    _FibEsPortResetTimer_Type()
)
fibEsPortResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortResetTimer.setStatus("mandatory")


class _FibEsPortResetAddrs_Type(Integer32):
    """Custom type fibEsPortResetAddrs based on Integer32"""
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


_FibEsPortResetAddrs_Type.__name__ = "Integer32"
_FibEsPortResetAddrs_Object = MibTableColumn
fibEsPortResetAddrs = _FibEsPortResetAddrs_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 14),
    _FibEsPortResetAddrs_Type()
)
fibEsPortResetAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fibEsPortResetAddrs.setStatus("mandatory")
_FibEsPortRcvBcasts_Type = Counter32
_FibEsPortRcvBcasts_Object = MibTableColumn
fibEsPortRcvBcasts = _FibEsPortRcvBcasts_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 15),
    _FibEsPortRcvBcasts_Type()
)
fibEsPortRcvBcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortRcvBcasts.setStatus("mandatory")
_FibEsPortSwitchedFrames_Type = Counter32
_FibEsPortSwitchedFrames_Object = MibTableColumn
fibEsPortSwitchedFrames = _FibEsPortSwitchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 9, 1, 2, 1, 1, 2, 1, 1, 16),
    _FibEsPortSwitchedFrames_Type()
)
fibEsPortSwitchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibEsPortSwitchedFrames.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fibronics-EtherSwitch-MIB",
    **{"MacAddr": MacAddr,
       "fibronics": fibronics,
       "products": products,
       "eth-switch": eth_switch,
       "xm516-card": xm516_card,
       "xm517-card": xm517_card,
       "xm518-card": xm518_card,
       "xm519-card": xm519_card,
       "xm5110-card": xm5110_card,
       "xm5111-card": xm5111_card,
       "xm5112-card": xm5112_card,
       "xm5113-card": xm5113_card,
       "xm5114-card": xm5114_card,
       "xm5115-card": xm5115_card,
       "mibs": mibs,
       "mibsbridges": mibsbridges,
       "mibbridges-specific": mibbridges_specific,
       "mibeth2eth": mibeth2eth,
       "mib-eps": mib_eps,
       "fibEsObjects": fibEsObjects,
       "fibEsMain": fibEsMain,
       "fibEsConfig": fibEsConfig,
       "fibEsFwVer": fibEsFwVer,
       "fibEsHwVer": fibEsHwVer,
       "fibEsIpAddr": fibEsIpAddr,
       "fibEsNetMask": fibEsNetMask,
       "fibEsDefaultGateway": fibEsDefaultGateway,
       "fibEsTrapRcvrMaxEnt": fibEsTrapRcvrMaxEnt,
       "fibEsTrapRcvrCurEnt": fibEsTrapRcvrCurEnt,
       "fibEsTrapRcvrNext": fibEsTrapRcvrNext,
       "fibEsTrapRcvrTable": fibEsTrapRcvrTable,
       "fibEsTrapRcvrEntry": fibEsTrapRcvrEntry,
       "fibEsTrapRcvrIndex": fibEsTrapRcvrIndex,
       "fibEsTrapRcvrStatus": fibEsTrapRcvrStatus,
       "fibEsTrapRcvrIpAddress": fibEsTrapRcvrIpAddress,
       "fibEsTrapRcvrComm": fibEsTrapRcvrComm,
       "fibEsSys": fibEsSys,
       "fibEsNumPorts": fibEsNumPorts,
       "fibEsNumStations": fibEsNumStations,
       "fibEsMostStations": fibEsMostStations,
       "fibEsMaxStations": fibEsMaxStations,
       "fibEsReset": fibEsReset,
       "fibEsNumResets": fibEsNumResets,
       "fibEsAddrAgingTime": fibEsAddrAgingTime,
       "fibEsSysStaTable": fibEsSysStaTable,
       "fibEsSysStaEntry": fibEsSysStaEntry,
       "fibEsSysStaMacAddr": fibEsSysStaMacAddr,
       "fibEsSysStaPort": fibEsSysStaPort,
       "fibEsSysStaTraffic": fibEsSysStaTraffic,
       "fibEsPort": fibEsPort,
       "fibEsPortTable": fibEsPortTable,
       "fibEsPortEntry": fibEsPortEntry,
       "fibEsPortIndex": fibEsPortIndex,
       "fibEsPortOprStatus": fibEsPortOprStatus,
       "fibEsPortDuplex": fibEsPortDuplex,
       "fibEsPortRcvLocalFrames": fibEsPortRcvLocalFrames,
       "fibEsPortForwardedFrames": fibEsPortForwardedFrames,
       "fibEsPortMostStations": fibEsPortMostStations,
       "fibEsPortMaxStations": fibEsPortMaxStations,
       "fibEsPortSWHandledFrames": fibEsPortSWHandledFrames,
       "fibEsPortLocalStations": fibEsPortLocalStations,
       "fibEsPortRemoteStations": fibEsPortRemoteStations,
       "fibEsPortUnknownStaFrames": fibEsPortUnknownStaFrames,
       "fibEsPortResetStats": fibEsPortResetStats,
       "fibEsPortResetTimer": fibEsPortResetTimer,
       "fibEsPortResetAddrs": fibEsPortResetAddrs,
       "fibEsPortRcvBcasts": fibEsPortRcvBcasts,
       "fibEsPortSwitchedFrames": fibEsPortSwitchedFrames}
)
