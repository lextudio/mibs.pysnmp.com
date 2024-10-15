# SNMP MIB module (FIBRONICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FIBRONICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:52 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibronics_ObjectIdentity = ObjectIdentity
fibronics = _Fibronics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_Fbr101_ObjectIdentity = ObjectIdentity
fbr101 = _Fbr101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101)
)
_Fbr2_ObjectIdentity = ObjectIdentity
fbr2 = _Fbr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2)
)
_FbrStack_ObjectIdentity = ObjectIdentity
fbrStack = _FbrStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7)
)


class _ChHWType_Type(Integer32):
    """Custom type chHWType based on Integer32"""
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
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fdx100", 7),
          ("lert40", 5),
          ("let10", 6),
          ("let18", 1),
          ("let18Extended", 4),
          ("let3", 2),
          ("let36", 3),
          ("stack", 8),
          ("unknown", 255))
    )


_ChHWType_Type.__name__ = "Integer32"
_ChHWType_Object = MibScalar
chHWType = _ChHWType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 1),
    _ChHWType_Type()
)
chHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWType.setStatus("mandatory")


class _ChNumberOfSlots_Type(Integer32):
    """Custom type chNumberOfSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChNumberOfSlots_Type.__name__ = "Integer32"
_ChNumberOfSlots_Object = MibScalar
chNumberOfSlots = _ChNumberOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 2),
    _ChNumberOfSlots_Type()
)
chNumberOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumberOfSlots.setStatus("mandatory")


class _ChNumberOfEthernetBuses_Type(Integer32):
    """Custom type chNumberOfEthernetBuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChNumberOfEthernetBuses_Type.__name__ = "Integer32"
_ChNumberOfEthernetBuses_Object = MibScalar
chNumberOfEthernetBuses = _ChNumberOfEthernetBuses_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 3),
    _ChNumberOfEthernetBuses_Type()
)
chNumberOfEthernetBuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumberOfEthernetBuses.setStatus("mandatory")


class _ChNumberOfTRBuses_Type(Integer32):
    """Custom type chNumberOfTRBuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChNumberOfTRBuses_Type.__name__ = "Integer32"
_ChNumberOfTRBuses_Object = MibScalar
chNumberOfTRBuses = _ChNumberOfTRBuses_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 4),
    _ChNumberOfTRBuses_Type()
)
chNumberOfTRBuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumberOfTRBuses.setStatus("mandatory")


class _ChNumberOfFDDIBuses_Type(Integer32):
    """Custom type chNumberOfFDDIBuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChNumberOfFDDIBuses_Type.__name__ = "Integer32"
_ChNumberOfFDDIBuses_Object = MibScalar
chNumberOfFDDIBuses = _ChNumberOfFDDIBuses_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 5),
    _ChNumberOfFDDIBuses_Type()
)
chNumberOfFDDIBuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumberOfFDDIBuses.setStatus("mandatory")


class _ChNumberOfLocalTalkBuses_Type(Integer32):
    """Custom type chNumberOfLocalTalkBuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChNumberOfLocalTalkBuses_Type.__name__ = "Integer32"
_ChNumberOfLocalTalkBuses_Object = MibScalar
chNumberOfLocalTalkBuses = _ChNumberOfLocalTalkBuses_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 6),
    _ChNumberOfLocalTalkBuses_Type()
)
chNumberOfLocalTalkBuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumberOfLocalTalkBuses.setStatus("mandatory")


class _ChReset_Type(Integer32):
    """Custom type chReset based on Integer32"""
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


_ChReset_Type.__name__ = "Integer32"
_ChReset_Object = MibScalar
chReset = _ChReset_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 7),
    _ChReset_Type()
)
chReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chReset.setStatus("mandatory")
_ChFullConfig_Type = OctetString
_ChFullConfig_Object = MibScalar
chFullConfig = _ChFullConfig_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 8),
    _ChFullConfig_Type()
)
chFullConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFullConfig.setStatus("mandatory")
_ChAg_ObjectIdentity = ObjectIdentity
chAg = _ChAg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9)
)
_ChGenAgTable_Object = MibTable
chGenAgTable = _ChGenAgTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 1)
)
if mibBuilder.loadTexts:
    chGenAgTable.setStatus("mandatory")
_ChGenAgEntry_Object = MibTableRow
chGenAgEntry = _ChGenAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 1, 1)
)
chGenAgEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "chGenAgId"),
)
if mibBuilder.loadTexts:
    chGenAgEntry.setStatus("mandatory")


class _ChGenAgId_Type(Integer32):
    """Custom type chGenAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChGenAgId_Type.__name__ = "Integer32"
_ChGenAgId_Object = MibTableColumn
chGenAgId = _ChGenAgId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 1, 1, 1),
    _ChGenAgId_Type()
)
chGenAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chGenAgId.setStatus("mandatory")


class _ChGenAgType_Type(Integer32):
    """Custom type chGenAgType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              255)
        )
    )
    namedValues = NamedValues(
        *(("iefn", 11),
          ("ielb", 7),
          ("ierp", 10),
          ("itfn", 12),
          ("itlb", 8),
          ("lts16", 9),
          ("nm2069", 13),
          ("nma-rt", 14),
          ("nma1-et", 1),
          ("nma1-et-e", 2),
          ("nma1-tr", 3),
          ("nma2-et", 4),
          ("nma2-fddi", 6),
          ("nma2-tr", 5),
          ("unknown", 255))
    )


_ChGenAgType_Type.__name__ = "Integer32"
_ChGenAgType_Object = MibTableColumn
chGenAgType = _ChGenAgType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 1, 1, 2),
    _ChGenAgType_Type()
)
chGenAgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chGenAgType.setStatus("mandatory")


class _ChGenAgMgmtIfType_Type(Integer32):
    """Custom type chGenAgMgmtIfType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              255)
        )
    )
    namedValues = NamedValues(
        *(("basicIsdn", 20),
          ("cept", 19),
          ("ddn-x25", 4),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("ip", 255),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("none", 1),
          ("nsip", 27),
          ("ppp", 23),
          ("primaryIsdn", 21),
          ("propPointToPointSerial", 22),
          ("proteon-10MBit", 12),
          ("proteon-80MBit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("sdlc", 17),
          ("slip", 28),
          ("softwareLoopback", 24),
          ("starLan", 11),
          ("t1-carrier", 18))
    )


_ChGenAgMgmtIfType_Type.__name__ = "Integer32"
_ChGenAgMgmtIfType_Object = MibTableColumn
chGenAgMgmtIfType = _ChGenAgMgmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 1, 1, 3),
    _ChGenAgMgmtIfType_Type()
)
chGenAgMgmtIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chGenAgMgmtIfType.setStatus("mandatory")


class _ChGenAgAddr_Type(OctetString):
    """Custom type chGenAgAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChGenAgAddr_Type.__name__ = "OctetString"
_ChGenAgAddr_Object = MibTableColumn
chGenAgAddr = _ChGenAgAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 1, 1, 4),
    _ChGenAgAddr_Type()
)
chGenAgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chGenAgAddr.setStatus("mandatory")
_ChGenAgSpecificOID_Type = ObjectIdentifier
_ChGenAgSpecificOID_Object = MibTableColumn
chGenAgSpecificOID = _ChGenAgSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 1, 1, 5),
    _ChGenAgSpecificOID_Type()
)
chGenAgSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chGenAgSpecificOID.setStatus("mandatory")
_ChFbrAgTable_Object = MibTable
chFbrAgTable = _ChFbrAgTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2)
)
if mibBuilder.loadTexts:
    chFbrAgTable.setStatus("mandatory")
_ChFbrAgEntry_Object = MibTableRow
chFbrAgEntry = _ChFbrAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1)
)
chFbrAgEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "chFbrAgId"),
)
if mibBuilder.loadTexts:
    chFbrAgEntry.setStatus("mandatory")


class _ChFbrAgId_Type(Integer32):
    """Custom type chFbrAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChFbrAgId_Type.__name__ = "Integer32"
_ChFbrAgId_Object = MibTableColumn
chFbrAgId = _ChFbrAgId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 1),
    _ChFbrAgId_Type()
)
chFbrAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgId.setStatus("mandatory")
_ChFbrAgSLIPAddress_Type = IpAddress
_ChFbrAgSLIPAddress_Object = MibTableColumn
chFbrAgSLIPAddress = _ChFbrAgSLIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 2),
    _ChFbrAgSLIPAddress_Type()
)
chFbrAgSLIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgSLIPAddress.setStatus("mandatory")
_ChFbrAgSWVersion_Type = DisplayString
_ChFbrAgSWVersion_Object = MibTableColumn
chFbrAgSWVersion = _ChFbrAgSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 3),
    _ChFbrAgSWVersion_Type()
)
chFbrAgSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgSWVersion.setStatus("mandatory")
_ChFbrAgKernelVersion_Type = DisplayString
_ChFbrAgKernelVersion_Object = MibTableColumn
chFbrAgKernelVersion = _ChFbrAgKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 4),
    _ChFbrAgKernelVersion_Type()
)
chFbrAgKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgKernelVersion.setStatus("mandatory")
_ChFbrAgCoprocSWVersion_Type = DisplayString
_ChFbrAgCoprocSWVersion_Object = MibTableColumn
chFbrAgCoprocSWVersion = _ChFbrAgCoprocSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 5),
    _ChFbrAgCoprocSWVersion_Type()
)
chFbrAgCoprocSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgCoprocSWVersion.setStatus("mandatory")
_ChFbrAgSWFault_Type = DisplayString
_ChFbrAgSWFault_Object = MibTableColumn
chFbrAgSWFault = _ChFbrAgSWFault_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 6),
    _ChFbrAgSWFault_Type()
)
chFbrAgSWFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgSWFault.setStatus("mandatory")
_ChFbrAgMgmtBusSelection_Type = Integer32
_ChFbrAgMgmtBusSelection_Object = MibTableColumn
chFbrAgMgmtBusSelection = _ChFbrAgMgmtBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 7),
    _ChFbrAgMgmtBusSelection_Type()
)
chFbrAgMgmtBusSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgMgmtBusSelection.setStatus("mandatory")


class _ChFbrAgCoprocCommStatus_Type(Integer32):
    """Custom type chFbrAgCoprocCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commProblems", 2),
          ("ok", 1),
          ("timeout", 3))
    )


_ChFbrAgCoprocCommStatus_Type.__name__ = "Integer32"
_ChFbrAgCoprocCommStatus_Object = MibTableColumn
chFbrAgCoprocCommStatus = _ChFbrAgCoprocCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 8),
    _ChFbrAgCoprocCommStatus_Type()
)
chFbrAgCoprocCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgCoprocCommStatus.setStatus("mandatory")


class _ChFbrAgCommDebugMode_Type(Integer32):
    """Custom type chFbrAgCommDebugMode based on Integer32"""
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


_ChFbrAgCommDebugMode_Type.__name__ = "Integer32"
_ChFbrAgCommDebugMode_Object = MibTableColumn
chFbrAgCommDebugMode = _ChFbrAgCommDebugMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 9),
    _ChFbrAgCommDebugMode_Type()
)
chFbrAgCommDebugMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgCommDebugMode.setStatus("mandatory")


class _ChFbrAgConfigChangeTraps_Type(Integer32):
    """Custom type chFbrAgConfigChangeTraps based on Integer32"""
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


_ChFbrAgConfigChangeTraps_Type.__name__ = "Integer32"
_ChFbrAgConfigChangeTraps_Object = MibTableColumn
chFbrAgConfigChangeTraps = _ChFbrAgConfigChangeTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 10),
    _ChFbrAgConfigChangeTraps_Type()
)
chFbrAgConfigChangeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgConfigChangeTraps.setStatus("mandatory")


class _ChFbrAgFaultTraps_Type(Integer32):
    """Custom type chFbrAgFaultTraps based on Integer32"""
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


_ChFbrAgFaultTraps_Type.__name__ = "Integer32"
_ChFbrAgFaultTraps_Object = MibTableColumn
chFbrAgFaultTraps = _ChFbrAgFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 11),
    _ChFbrAgFaultTraps_Type()
)
chFbrAgFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgFaultTraps.setStatus("mandatory")


class _ChFbrAgTrafficThreshTraps_Type(Integer32):
    """Custom type chFbrAgTrafficThreshTraps based on Integer32"""
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


_ChFbrAgTrafficThreshTraps_Type.__name__ = "Integer32"
_ChFbrAgTrafficThreshTraps_Object = MibTableColumn
chFbrAgTrafficThreshTraps = _ChFbrAgTrafficThreshTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 12),
    _ChFbrAgTrafficThreshTraps_Type()
)
chFbrAgTrafficThreshTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgTrafficThreshTraps.setStatus("mandatory")


class _ChFbrAgGroupEnrollDeenrollTraps_Type(Integer32):
    """Custom type chFbrAgGroupEnrollDeenrollTraps based on Integer32"""
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


_ChFbrAgGroupEnrollDeenrollTraps_Type.__name__ = "Integer32"
_ChFbrAgGroupEnrollDeenrollTraps_Object = MibTableColumn
chFbrAgGroupEnrollDeenrollTraps = _ChFbrAgGroupEnrollDeenrollTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 13),
    _ChFbrAgGroupEnrollDeenrollTraps_Type()
)
chFbrAgGroupEnrollDeenrollTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgGroupEnrollDeenrollTraps.setStatus("mandatory")


class _ChFbrAgSoftFaultTraps_Type(Integer32):
    """Custom type chFbrAgSoftFaultTraps based on Integer32"""
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


_ChFbrAgSoftFaultTraps_Type.__name__ = "Integer32"
_ChFbrAgSoftFaultTraps_Object = MibTableColumn
chFbrAgSoftFaultTraps = _ChFbrAgSoftFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 14),
    _ChFbrAgSoftFaultTraps_Type()
)
chFbrAgSoftFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgSoftFaultTraps.setStatus("mandatory")


class _ChFbrAgHubEnrollTraps_Type(Integer32):
    """Custom type chFbrAgHubEnrollTraps based on Integer32"""
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


_ChFbrAgHubEnrollTraps_Type.__name__ = "Integer32"
_ChFbrAgHubEnrollTraps_Object = MibTableColumn
chFbrAgHubEnrollTraps = _ChFbrAgHubEnrollTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 15),
    _ChFbrAgHubEnrollTraps_Type()
)
chFbrAgHubEnrollTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgHubEnrollTraps.setStatus("obsolete")


class _ChFbrAgTempThreshTraps_Type(Integer32):
    """Custom type chFbrAgTempThreshTraps based on Integer32"""
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


_ChFbrAgTempThreshTraps_Type.__name__ = "Integer32"
_ChFbrAgTempThreshTraps_Object = MibTableColumn
chFbrAgTempThreshTraps = _ChFbrAgTempThreshTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 16),
    _ChFbrAgTempThreshTraps_Type()
)
chFbrAgTempThreshTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgTempThreshTraps.setStatus("mandatory")
_ChFbrAgSpecificOID_Type = ObjectIdentifier
_ChFbrAgSpecificOID_Object = MibTableColumn
chFbrAgSpecificOID = _ChFbrAgSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 17),
    _ChFbrAgSpecificOID_Type()
)
chFbrAgSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgSpecificOID.setStatus("mandatory")
_ChFbrAgLastAddrConfig_Type = OctetString
_ChFbrAgLastAddrConfig_Object = MibTableColumn
chFbrAgLastAddrConfig = _ChFbrAgLastAddrConfig_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 18),
    _ChFbrAgLastAddrConfig_Type()
)
chFbrAgLastAddrConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgLastAddrConfig.setStatus("mandatory")
_ChFbrAgSecAddrConfig_Type = OctetString
_ChFbrAgSecAddrConfig_Object = MibTableColumn
chFbrAgSecAddrConfig = _ChFbrAgSecAddrConfig_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 19),
    _ChFbrAgSecAddrConfig_Type()
)
chFbrAgSecAddrConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgSecAddrConfig.setStatus("mandatory")


class _ChFbrAgSoftwareStatus_Type(Integer32):
    """Custom type chFbrAgSoftwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downLoading", 3),
          ("loaded", 2),
          ("unLoadable", 1))
    )


_ChFbrAgSoftwareStatus_Type.__name__ = "Integer32"
_ChFbrAgSoftwareStatus_Object = MibTableColumn
chFbrAgSoftwareStatus = _ChFbrAgSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 20),
    _ChFbrAgSoftwareStatus_Type()
)
chFbrAgSoftwareStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgSoftwareStatus.setStatus("mandatory")


class _ChFbrAgConfigurationSymbol_Type(DisplayString):
    """Custom type chFbrAgConfigurationSymbol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ChFbrAgConfigurationSymbol_Type.__name__ = "DisplayString"
_ChFbrAgConfigurationSymbol_Object = MibTableColumn
chFbrAgConfigurationSymbol = _ChFbrAgConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 21),
    _ChFbrAgConfigurationSymbol_Type()
)
chFbrAgConfigurationSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgConfigurationSymbol.setStatus("mandatory")
_ChFbrAgIntTemp_Type = Integer32
_ChFbrAgIntTemp_Object = MibTableColumn
chFbrAgIntTemp = _ChFbrAgIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 22),
    _ChFbrAgIntTemp_Type()
)
chFbrAgIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgIntTemp.setStatus("mandatory")
_ChFbrAgBootVersion_Type = DisplayString
_ChFbrAgBootVersion_Object = MibTableColumn
chFbrAgBootVersion = _ChFbrAgBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 23),
    _ChFbrAgBootVersion_Type()
)
chFbrAgBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgBootVersion.setStatus("mandatory")
_ChFbrAgSensorFault_Type = Integer32
_ChFbrAgSensorFault_Object = MibTableColumn
chFbrAgSensorFault = _ChFbrAgSensorFault_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 24),
    _ChFbrAgSensorFault_Type()
)
chFbrAgSensorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgSensorFault.setStatus("mandatory")


class _ChFbrAgSensorFaultTraps_Type(Integer32):
    """Custom type chFbrAgSensorFaultTraps based on Integer32"""
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


_ChFbrAgSensorFaultTraps_Type.__name__ = "Integer32"
_ChFbrAgSensorFaultTraps_Object = MibTableColumn
chFbrAgSensorFaultTraps = _ChFbrAgSensorFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 25),
    _ChFbrAgSensorFaultTraps_Type()
)
chFbrAgSensorFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgSensorFaultTraps.setStatus("mandatory")
_ChFbrAgInterProcFault_Type = Integer32
_ChFbrAgInterProcFault_Object = MibTableColumn
chFbrAgInterProcFault = _ChFbrAgInterProcFault_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 26),
    _ChFbrAgInterProcFault_Type()
)
chFbrAgInterProcFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgInterProcFault.setStatus("mandatory")
_ChFbrAgInterProcFaultTraps_Type = Integer32
_ChFbrAgInterProcFaultTraps_Object = MibTableColumn
chFbrAgInterProcFaultTraps = _ChFbrAgInterProcFaultTraps_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 2, 1, 27),
    _ChFbrAgInterProcFaultTraps_Type()
)
chFbrAgInterProcFaultTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgInterProcFaultTraps.setStatus("mandatory")
_ChFbrAgSetup_ObjectIdentity = ObjectIdentity
chFbrAgSetup = _ChFbrAgSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3)
)
_ChFbrAgMaxNmbOfMngrs_Type = Integer32
_ChFbrAgMaxNmbOfMngrs_Object = MibScalar
chFbrAgMaxNmbOfMngrs = _ChFbrAgMaxNmbOfMngrs_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 1),
    _ChFbrAgMaxNmbOfMngrs_Type()
)
chFbrAgMaxNmbOfMngrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgMaxNmbOfMngrs.setStatus("mandatory")
_ChFbrAgPermMngrTable_Object = MibTable
chFbrAgPermMngrTable = _ChFbrAgPermMngrTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 2)
)
if mibBuilder.loadTexts:
    chFbrAgPermMngrTable.setStatus("mandatory")
_ChFbrAgPermMngrEntry_Object = MibTableRow
chFbrAgPermMngrEntry = _ChFbrAgPermMngrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 2, 1)
)
chFbrAgPermMngrEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "chFbrAgPermMngrId"),
)
if mibBuilder.loadTexts:
    chFbrAgPermMngrEntry.setStatus("mandatory")
_ChFbrAgPermMngrId_Type = Integer32
_ChFbrAgPermMngrId_Object = MibTableColumn
chFbrAgPermMngrId = _ChFbrAgPermMngrId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 2, 1, 1),
    _ChFbrAgPermMngrId_Type()
)
chFbrAgPermMngrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgPermMngrId.setStatus("mandatory")
_ChFbrAgPermMngrAddr_Type = IpAddress
_ChFbrAgPermMngrAddr_Object = MibTableColumn
chFbrAgPermMngrAddr = _ChFbrAgPermMngrAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 2, 1, 2),
    _ChFbrAgPermMngrAddr_Type()
)
chFbrAgPermMngrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgPermMngrAddr.setStatus("mandatory")
_ChFbrAgMaxNmbOfNets_Type = Integer32
_ChFbrAgMaxNmbOfNets_Object = MibScalar
chFbrAgMaxNmbOfNets = _ChFbrAgMaxNmbOfNets_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 3),
    _ChFbrAgMaxNmbOfNets_Type()
)
chFbrAgMaxNmbOfNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgMaxNmbOfNets.setStatus("mandatory")
_ChFbrAgRmtNetTable_Object = MibTable
chFbrAgRmtNetTable = _ChFbrAgRmtNetTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 4)
)
if mibBuilder.loadTexts:
    chFbrAgRmtNetTable.setStatus("mandatory")
_ChFbrAgRmtNetEntry_Object = MibTableRow
chFbrAgRmtNetEntry = _ChFbrAgRmtNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 4, 1)
)
chFbrAgRmtNetEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "chFbrAgRmtNetId"),
)
if mibBuilder.loadTexts:
    chFbrAgRmtNetEntry.setStatus("mandatory")
_ChFbrAgRmtNetId_Type = Integer32
_ChFbrAgRmtNetId_Object = MibTableColumn
chFbrAgRmtNetId = _ChFbrAgRmtNetId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 4, 1, 1),
    _ChFbrAgRmtNetId_Type()
)
chFbrAgRmtNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chFbrAgRmtNetId.setStatus("mandatory")
_ChFbrAgRmtNetAddr_Type = IpAddress
_ChFbrAgRmtNetAddr_Object = MibTableColumn
chFbrAgRmtNetAddr = _ChFbrAgRmtNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 4, 1, 2),
    _ChFbrAgRmtNetAddr_Type()
)
chFbrAgRmtNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgRmtNetAddr.setStatus("mandatory")
_ChFbrAgRmtNetMask_Type = IpAddress
_ChFbrAgRmtNetMask_Object = MibTableColumn
chFbrAgRmtNetMask = _ChFbrAgRmtNetMask_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 4, 1, 3),
    _ChFbrAgRmtNetMask_Type()
)
chFbrAgRmtNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgRmtNetMask.setStatus("mandatory")


class _ChFbrAgDateTime_Type(DisplayString):
    """Custom type chFbrAgDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_ChFbrAgDateTime_Type.__name__ = "DisplayString"
_ChFbrAgDateTime_Object = MibScalar
chFbrAgDateTime = _ChFbrAgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 5),
    _ChFbrAgDateTime_Type()
)
chFbrAgDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgDateTime.setStatus("mandatory")


class _ChFbrAgReset_Type(Integer32):
    """Custom type chFbrAgReset based on Integer32"""
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


_ChFbrAgReset_Type.__name__ = "Integer32"
_ChFbrAgReset_Object = MibScalar
chFbrAgReset = _ChFbrAgReset_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 9, 3, 6),
    _ChFbrAgReset_Type()
)
chFbrAgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chFbrAgReset.setStatus("mandatory")
_ChMgr_ObjectIdentity = ObjectIdentity
chMgr = _ChMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 10)
)


class _ChMgrTrapRepStatus_Type(Integer32):
    """Custom type chMgrTrapRepStatus based on Integer32"""
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


_ChMgrTrapRepStatus_Type.__name__ = "Integer32"
_ChMgrTrapRepStatus_Object = MibScalar
chMgrTrapRepStatus = _ChMgrTrapRepStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 10, 1),
    _ChMgrTrapRepStatus_Type()
)
chMgrTrapRepStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chMgrTrapRepStatus.setStatus("mandatory")


class _ChMgrContPerfRep_Type(Integer32):
    """Custom type chMgrContPerfRep based on Integer32"""
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


_ChMgrContPerfRep_Type.__name__ = "Integer32"
_ChMgrContPerfRep_Object = MibScalar
chMgrContPerfRep = _ChMgrContPerfRep_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 10, 2),
    _ChMgrContPerfRep_Type()
)
chMgrContPerfRep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chMgrContPerfRep.setStatus("mandatory")


class _ChMgrMngmtState_Type(Integer32):
    """Custom type chMgrMngmtState based on Integer32"""
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


_ChMgrMngmtState_Type.__name__ = "Integer32"
_ChMgrMngmtState_Object = MibScalar
chMgrMngmtState = _ChMgrMngmtState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 10, 3),
    _ChMgrMngmtState_Type()
)
chMgrMngmtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chMgrMngmtState.setStatus("mandatory")


class _ChMgrPollInterval_Type(Integer32):
    """Custom type chMgrPollInterval based on Integer32"""
    defaultValue = 5


_ChMgrPollInterval_Object = MibScalar
chMgrPollInterval = _ChMgrPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 10, 4),
    _ChMgrPollInterval_Type()
)
chMgrPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chMgrPollInterval.setStatus("mandatory")
_ChHW_ObjectIdentity = ObjectIdentity
chHW = _ChHW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11)
)
_ChHWPSUTable_Object = MibTable
chHWPSUTable = _ChHWPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 1)
)
if mibBuilder.loadTexts:
    chHWPSUTable.setStatus("mandatory")
_ChHWPSUEntry_Object = MibTableRow
chHWPSUEntry = _ChHWPSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 1, 1)
)
chHWPSUEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "chHWPSUId"),
)
if mibBuilder.loadTexts:
    chHWPSUEntry.setStatus("mandatory")


class _ChHWPSUId_Type(Integer32):
    """Custom type chHWPSUId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChHWPSUId_Type.__name__ = "Integer32"
_ChHWPSUId_Object = MibTableColumn
chHWPSUId = _ChHWPSUId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 1, 1, 1),
    _ChHWPSUId_Type()
)
chHWPSUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWPSUId.setStatus("mandatory")


class _ChHWPSUActivityStatus_Type(Integer32):
    """Custom type chHWPSUActivityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("dormant", 2),
          ("notActive", 1))
    )


_ChHWPSUActivityStatus_Type.__name__ = "Integer32"
_ChHWPSUActivityStatus_Object = MibTableColumn
chHWPSUActivityStatus = _ChHWPSUActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 1, 1, 2),
    _ChHWPSUActivityStatus_Type()
)
chHWPSUActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWPSUActivityStatus.setStatus("mandatory")


class _ChHWPSULocation_Type(Integer32):
    """Custom type chHWPSULocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("other", 1))
    )


_ChHWPSULocation_Type.__name__ = "Integer32"
_ChHWPSULocation_Object = MibTableColumn
chHWPSULocation = _ChHWPSULocation_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 1, 1, 3),
    _ChHWPSULocation_Type()
)
chHWPSULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWPSULocation.setStatus("mandatory")
_ChHWPSUVoltage_Type = Integer32
_ChHWPSUVoltage_Object = MibTableColumn
chHWPSUVoltage = _ChHWPSUVoltage_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 1, 1, 4),
    _ChHWPSUVoltage_Type()
)
chHWPSUVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWPSUVoltage.setStatus("mandatory")


class _ChHWIntTempWarning_Type(Integer32):
    """Custom type chHWIntTempWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exceeded", 2),
          ("ok", 1))
    )


_ChHWIntTempWarning_Type.__name__ = "Integer32"
_ChHWIntTempWarning_Object = MibScalar
chHWIntTempWarning = _ChHWIntTempWarning_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 2),
    _ChHWIntTempWarning_Type()
)
chHWIntTempWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWIntTempWarning.setStatus("mandatory")
_ChHWIntTempThresh_Type = Integer32
_ChHWIntTempThresh_Object = MibScalar
chHWIntTempThresh = _ChHWIntTempThresh_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 3),
    _ChHWIntTempThresh_Type()
)
chHWIntTempThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chHWIntTempThresh.setStatus("mandatory")
_ChHWPeakIntTemp_Type = Integer32
_ChHWPeakIntTemp_Object = MibScalar
chHWPeakIntTemp = _ChHWPeakIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 11, 4),
    _ChHWPeakIntTemp_Type()
)
chHWPeakIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chHWPeakIntTemp.setStatus("mandatory")
_ChSlotLastChange_Type = TimeTicks
_ChSlotLastChange_Object = MibScalar
chSlotLastChange = _ChSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 7, 12),
    _ChSlotLastChange_Type()
)
chSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlotLastChange.setStatus("mandatory")
_GenGroup_ObjectIdentity = ObjectIdentity
genGroup = _GenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8)
)
_GenGroupTable_Object = MibTable
genGroupTable = _GenGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    genGroupTable.setStatus("mandatory")
_GenGroupEntry_Object = MibTableRow
genGroupEntry = _GenGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1)
)
genGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "genGroupId"),
)
if mibBuilder.loadTexts:
    genGroupEntry.setStatus("mandatory")


class _GenGroupId_Type(Integer32):
    """Custom type genGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GenGroupId_Type.__name__ = "Integer32"
_GenGroupId_Object = MibTableColumn
genGroupId = _GenGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 1),
    _GenGroupId_Type()
)
genGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupId.setStatus("mandatory")
_GenGroupSWVersion_Type = DisplayString
_GenGroupSWVersion_Object = MibTableColumn
genGroupSWVersion = _GenGroupSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 2),
    _GenGroupSWVersion_Type()
)
genGroupSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupSWVersion.setStatus("mandatory")
_GenGroupKernelVersion_Type = DisplayString
_GenGroupKernelVersion_Object = MibTableColumn
genGroupKernelVersion = _GenGroupKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 3),
    _GenGroupKernelVersion_Type()
)
genGroupKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupKernelVersion.setStatus("mandatory")


class _GenGroupType_Type(Integer32):
    """Custom type genGroupType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fer2061", 92),
          ("iefn", 80),
          ("ielb", 29),
          ("ierb", 79),
          ("ierp", 86),
          ("ietlb", 85),
          ("iftc", 84),
          ("istc1", 83),
          ("istc2", 91),
          ("itfn", 81),
          ("itlb", 44),
          ("itng", 99),
          ("itre1", 82),
          ("itre2", 90),
          ("lace100", 100),
          ("lcl100", 51),
          ("le10b", 1),
          ("le10b-2", 2),
          ("le10b-2r", 25),
          ("le10b2n", 38),
          ("le10c", 3),
          ("le10c-2", 4),
          ("le10c-2r", 26),
          ("le110b", 49),
          ("le110bq", 50),
          ("le110cq", 89),
          ("le115q", 93),
          ("le120q", 69),
          ("le120q-fb", 72),
          ("le120r", 46),
          ("le120r-2", 47),
          ("le120sq2", 70),
          ("le120sq2-fb", 73),
          ("le120sq5", 71),
          ("le120sq5-fb", 74),
          ("le140xt", 28),
          ("le140xtc", 48),
          ("le140xtf", 45),
          ("le140xtf-fb", 55),
          ("le140xtn", 67),
          ("le140xtq", 52),
          ("le140xts", 101),
          ("le15", 5),
          ("le15-2", 6),
          ("le20", 7),
          ("le20n", 33),
          ("le20n-fb", 53),
          ("le20r", 35),
          ("le20s", 37),
          ("le20s-fb", 54),
          ("le30x", 8),
          ("le30x-2", 9),
          ("le30xd", 10),
          ("le40x", 11),
          ("le40xt", 12),
          ("le40xtn", 102),
          ("le80xt", 27),
          ("le80xtn", 103),
          ("lert40-10BASET", 58),
          ("lert40-AUI", 57),
          ("lfd102-mic", 64),
          ("lfd102-stm", 65),
          ("lfd102-sts", 66),
          ("lfd104-mic", 59),
          ("lfd104-stl", 61),
          ("lfd104-stm", 60),
          ("lfd104-stp", 62),
          ("lfd104-utp", 63),
          ("lhb", 96),
          ("lhs", 78),
          ("llt8", 36),
          ("lse108", 87),
          ("lse208", 88),
          ("lse808", 77),
          ("ltr104-D25", 40),
          ("ltr104-D9", 39),
          ("ltr104-RJ45", 34),
          ("ltr104a", 68),
          ("ltr104f", 43),
          ("ltr104s", 56),
          ("ltr108f", 76),
          ("ltr108t", 75),
          ("ltr4-D25", 15),
          ("ltr4-D9", 14),
          ("ltr4-FO", 16),
          ("ltr4-RJ45", 13),
          ("ltrf16", 31),
          ("ltrf4", 30),
          ("ltrio-Con1", 23),
          ("ltrio-Con2", 24),
          ("ltrio-D25", 21),
          ("ltrio-D9", 20),
          ("ltrio-FO", 22),
          ("ltrio-RJ45", 19),
          ("ltrt-D9", 42),
          ("ltrt-RJ45", 41),
          ("lts16", 32),
          ("sh-e8", 95),
          ("sh-efn", 97),
          ("sh-t16", 94),
          ("sh-tfn", 98),
          ("unknown", 255))
    )


_GenGroupType_Type.__name__ = "Integer32"
_GenGroupType_Object = MibTableColumn
genGroupType = _GenGroupType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 4),
    _GenGroupType_Type()
)
genGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupType.setStatus("mandatory")


class _GenGroupDescr_Type(DisplayString):
    """Custom type genGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenGroupDescr_Type.__name__ = "DisplayString"
_GenGroupDescr_Object = MibTableColumn
genGroupDescr = _GenGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 5),
    _GenGroupDescr_Type()
)
genGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupDescr.setStatus("mandatory")


class _GenGroupNumberOfPorts_Type(Integer32):
    """Custom type genGroupNumberOfPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GenGroupNumberOfPorts_Type.__name__ = "Integer32"
_GenGroupNumberOfPorts_Object = MibTableColumn
genGroupNumberOfPorts = _GenGroupNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 6),
    _GenGroupNumberOfPorts_Type()
)
genGroupNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupNumberOfPorts.setStatus("mandatory")


class _GenGroupNumberOfIntPorts_Type(Integer32):
    """Custom type genGroupNumberOfIntPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GenGroupNumberOfIntPorts_Type.__name__ = "Integer32"
_GenGroupNumberOfIntPorts_Object = MibTableColumn
genGroupNumberOfIntPorts = _GenGroupNumberOfIntPorts_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 7),
    _GenGroupNumberOfIntPorts_Type()
)
genGroupNumberOfIntPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupNumberOfIntPorts.setStatus("mandatory")


class _GenGroupReset_Type(Integer32):
    """Custom type genGroupReset based on Integer32"""
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


_GenGroupReset_Type.__name__ = "Integer32"
_GenGroupReset_Object = MibTableColumn
genGroupReset = _GenGroupReset_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 8),
    _GenGroupReset_Type()
)
genGroupReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genGroupReset.setStatus("mandatory")


class _GenGroupAutoMan_Type(Integer32):
    """Custom type genGroupAutoMan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("man", 2))
    )


_GenGroupAutoMan_Type.__name__ = "Integer32"
_GenGroupAutoMan_Object = MibTableColumn
genGroupAutoMan = _GenGroupAutoMan_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 9),
    _GenGroupAutoMan_Type()
)
genGroupAutoMan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupAutoMan.setStatus("mandatory")
_GenGroupFullConfig_Type = OctetString
_GenGroupFullConfig_Object = MibTableColumn
genGroupFullConfig = _GenGroupFullConfig_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 10),
    _GenGroupFullConfig_Type()
)
genGroupFullConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupFullConfig.setStatus("mandatory")


class _GenGroupRedun12_Type(Integer32):
    """Custom type genGroupRedun12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_GenGroupRedun12_Type.__name__ = "Integer32"
_GenGroupRedun12_Object = MibTableColumn
genGroupRedun12 = _GenGroupRedun12_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 11),
    _GenGroupRedun12_Type()
)
genGroupRedun12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genGroupRedun12.setStatus("mandatory")


class _GenGroupRedun34_Type(Integer32):
    """Custom type genGroupRedun34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_GenGroupRedun34_Type.__name__ = "Integer32"
_GenGroupRedun34_Object = MibTableColumn
genGroupRedun34 = _GenGroupRedun34_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 12),
    _GenGroupRedun34_Type()
)
genGroupRedun34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genGroupRedun34.setStatus("mandatory")


class _GenGroupRedun13_14_Type(Integer32):
    """Custom type genGroupRedun13_14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_GenGroupRedun13_14_Type.__name__ = "Integer32"
_GenGroupRedun13_14_Object = MibScalar
genGroupRedun13_14 = _GenGroupRedun13_14_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 13),
    _GenGroupRedun13_14_Type()
)
genGroupRedun13_14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genGroupRedun13_14.setStatus("mandatory")


class _GenGroupStandAloneMode_Type(Integer32):
    """Custom type genGroupStandAloneMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_GenGroupStandAloneMode_Type.__name__ = "Integer32"
_GenGroupStandAloneMode_Object = MibTableColumn
genGroupStandAloneMode = _GenGroupStandAloneMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 14),
    _GenGroupStandAloneMode_Type()
)
genGroupStandAloneMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genGroupStandAloneMode.setStatus("mandatory")


class _GenGroupInterProcCommStatus_Type(Integer32):
    """Custom type genGroupInterProcCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("commProblems", 2),
          ("noCommunication", 3),
          ("notSupported", 255),
          ("ok", 1))
    )


_GenGroupInterProcCommStatus_Type.__name__ = "Integer32"
_GenGroupInterProcCommStatus_Object = MibTableColumn
genGroupInterProcCommStatus = _GenGroupInterProcCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 15),
    _GenGroupInterProcCommStatus_Type()
)
genGroupInterProcCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupInterProcCommStatus.setStatus("mandatory")


class _GenGroupCommStatus_Type(Integer32):
    """Custom type genGroupCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("commProblems", 2),
          ("noCommunication", 3),
          ("notSupported", 255),
          ("ok", 1))
    )


_GenGroupCommStatus_Type.__name__ = "Integer32"
_GenGroupCommStatus_Object = MibTableColumn
genGroupCommStatus = _GenGroupCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 16),
    _GenGroupCommStatus_Type()
)
genGroupCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupCommStatus.setStatus("mandatory")


class _GenGroupHWStatus_Type(Integer32):
    """Custom type genGroupHWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hardwareProblems", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_GenGroupHWStatus_Type.__name__ = "Integer32"
_GenGroupHWStatus_Object = MibTableColumn
genGroupHWStatus = _GenGroupHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 17),
    _GenGroupHWStatus_Type()
)
genGroupHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWStatus.setStatus("mandatory")


class _GenGroupSupplyVoltageFault_Type(Integer32):
    """Custom type genGroupSupplyVoltageFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_GenGroupSupplyVoltageFault_Type.__name__ = "Integer32"
_GenGroupSupplyVoltageFault_Object = MibTableColumn
genGroupSupplyVoltageFault = _GenGroupSupplyVoltageFault_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 18),
    _GenGroupSupplyVoltageFault_Type()
)
genGroupSupplyVoltageFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupSupplyVoltageFault.setStatus("mandatory")
_GenGroupIntTemp_Type = Integer32
_GenGroupIntTemp_Object = MibTableColumn
genGroupIntTemp = _GenGroupIntTemp_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 19),
    _GenGroupIntTemp_Type()
)
genGroupIntTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupIntTemp.setStatus("mandatory")
_GenGroupSpecificOID_Type = ObjectIdentifier
_GenGroupSpecificOID_Object = MibTableColumn
genGroupSpecificOID = _GenGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 20),
    _GenGroupSpecificOID_Type()
)
genGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupSpecificOID.setStatus("mandatory")


class _GenGroupConfigurationSymbol_Type(DisplayString):
    """Custom type genGroupConfigurationSymbol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GenGroupConfigurationSymbol_Type.__name__ = "DisplayString"
_GenGroupConfigurationSymbol_Object = MibTableColumn
genGroupConfigurationSymbol = _GenGroupConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 21),
    _GenGroupConfigurationSymbol_Type()
)
genGroupConfigurationSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genGroupConfigurationSymbol.setStatus("mandatory")
_GenGroupLastChange_Type = TimeTicks
_GenGroupLastChange_Object = MibTableColumn
genGroupLastChange = _GenGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 8, 1, 1, 22),
    _GenGroupLastChange_Type()
)
genGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupLastChange.setStatus("mandatory")
_GenPort_ObjectIdentity = ObjectIdentity
genPort = _GenPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9)
)
_GenPortTable_Object = MibTable
genPortTable = _GenPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    genPortTable.setStatus("mandatory")
_GenPortEntry_Object = MibTableRow
genPortEntry = _GenPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1)
)
genPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "genPortGroupId"),
    (0, "FIBRONICS-MIB", "genPortId"),
)
if mibBuilder.loadTexts:
    genPortEntry.setStatus("mandatory")


class _GenPortGroupId_Type(Integer32):
    """Custom type genPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GenPortGroupId_Type.__name__ = "Integer32"
_GenPortGroupId_Object = MibTableColumn
genPortGroupId = _GenPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 1),
    _GenPortGroupId_Type()
)
genPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortGroupId.setStatus("mandatory")


class _GenPortId_Type(Integer32):
    """Custom type genPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GenPortId_Type.__name__ = "Integer32"
_GenPortId_Object = MibTableColumn
genPortId = _GenPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 2),
    _GenPortId_Type()
)
genPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortId.setStatus("mandatory")


class _GenPortFunctionality_Type(Integer32):
    """Custom type genPortFunctionality based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("activeLobe", 17),
          ("activeRI", 24),
          ("activeRO", 25),
          ("clock", 14),
          ("dte", 16),
          ("fddi", 13),
          ("foirl", 6),
          ("genActiveTokenRing", 18),
          ("genTokenRing", 15),
          ("lhsFiber", 21),
          ("lobe", 8),
          ("localTalk", 12),
          ("lse10BaseT", 20),
          ("private", 1),
          ("repeater10BaseT", 4),
          ("repeaterAUI", 2),
          ("repeaterThin", 3),
          ("ri", 9),
          ("ro", 10),
          ("serial", 11),
          ("star", 23),
          ("tenBaseFB", 19),
          ("tenBaseFSyncAct", 5),
          ("wan", 22),
          ("xcvr", 7))
    )


_GenPortFunctionality_Type.__name__ = "Integer32"
_GenPortFunctionality_Object = MibTableColumn
genPortFunctionality = _GenPortFunctionality_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 3),
    _GenPortFunctionality_Type()
)
genPortFunctionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortFunctionality.setStatus("mandatory")


class _GenPortType_Type(Integer32):
    """Custom type genPortType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clock-ext", 51),
          ("clock-int", 50),
          ("fddi-micPort1", 57),
          ("fddi-micPort2", 58),
          ("fddi-micPort3", 59),
          ("fddi-stlPort1", 63),
          ("fddi-stlPort2", 64),
          ("fddi-stlPort3", 65),
          ("fddi-stmPort1", 60),
          ("fddi-stmPort2", 61),
          ("fddi-stmPort3", 62),
          ("fddi-stpPort1", 66),
          ("fddi-stpPort2", 67),
          ("fddi-stpPort3", 68),
          ("fddi-stsPort1", 72),
          ("fddi-stsPort2", 73),
          ("fddi-stsPort3", 74),
          ("fddi-utpPort1", 69),
          ("fddi-utpPort2", 70),
          ("fddi-utpPort3", 71),
          ("fer2061-10btPort", 112),
          ("fer2061-AUIPort", 113),
          ("fer2061-FOPort", 114),
          ("fer2061-FOSyncPort", 115),
          ("iefnPort", 98),
          ("ielb-10btPort", 30),
          ("ielb-AUIPort", 29),
          ("ierbPort", 97),
          ("ierpPort", 107),
          ("ietlb-10BaseTPort", 106),
          ("ietlb-lobePort", 103),
          ("ietlb-riPort", 104),
          ("ietlb-roPort", 105),
          ("iftcPort", 102),
          ("istcPort", 101),
          ("itfnPort", 99),
          ("itlbDTEPort", 38),
          ("itlbRiPort", 37),
          ("itlbRoPort", 36),
          ("itngPort", 125),
          ("itrePort", 100),
          ("le10bPort", 1),
          ("le10bnPort", 40),
          ("le10cPort", 2),
          ("le110bPort", 45),
          ("le110bqPort", 46),
          ("le110cqPort", 110),
          ("le115qPort", 116),
          ("le120q-fbPort", 83),
          ("le120qPort", 79),
          ("le120rPort", 41),
          ("le120sq2-fbPortM", 85),
          ("le120sq2-fbPortS", 84),
          ("le120sq2PortM", 81),
          ("le120sq2PortS", 80),
          ("le120sq5-fbPort", 86),
          ("le120sq5Port", 82),
          ("le140xtPort", 28),
          ("le140xtcPort", 44),
          ("le140xtf-10btPort", 43),
          ("le140xtf-foPort", 42),
          ("le140xtf-fofbPort", 56),
          ("le140xtnPort", 75),
          ("le140xtqPort", 47),
          ("le140xtsPort", 126),
          ("le15Port", 3),
          ("le20Port", 4),
          ("le20fbPort", 55),
          ("le20rPort", 35),
          ("le30xPort", 5),
          ("le30xdPort", 6),
          ("le40xPort", 7),
          ("le40xtPort", 8),
          ("le40xtnPort", 127),
          ("le80xtPort", 27),
          ("le80xtnPort", 128),
          ("lert40-10btPort", 49),
          ("lert40-AUIPort", 48),
          ("lhbPort", 124),
          ("lhsPort", 96),
          ("llt8Port", 34),
          ("lobe104RJ45S", 54),
          ("lobeD25", 11),
          ("lobeD9", 10),
          ("lobeFO", 12),
          ("lobeRJ45", 9),
          ("lse108Port", 108),
          ("lse208Port", 109),
          ("lse808Port", 95),
          ("ltr104a-lobePort", 76),
          ("ltr104a-riPort", 77),
          ("ltr104a-roPort", 78),
          ("ltr108f-lobePort", 91),
          ("ltr108f-riPortFO", 93),
          ("ltr108f-roPortFO", 94),
          ("ltr108f-starPortFO", 92),
          ("ltr108t-lobePort", 90),
          ("ltr108t-lobePort1", 87),
          ("ltr108t-riPort1", 88),
          ("ltr108t-roPort1", 89),
          ("ltr108t-starPort1", 111),
          ("ltrf16Port", 32),
          ("ltrf4Port", 31),
          ("lts16Port", 33),
          ("r0104RJ45S", 53),
          ("ri104D25", 13),
          ("ri104D9", 20),
          ("ri104RJ45", 19),
          ("ri104RJ45S", 52),
          ("riD25", 17),
          ("riD9", 16),
          ("riFO", 18),
          ("riRJ45", 15),
          ("ro104D25", 14),
          ("ro104D9", 26),
          ("ro104RJ45", 25),
          ("roD25", 23),
          ("roD9", 22),
          ("roFO", 24),
          ("roRJ45", 21),
          ("sht-lobePort", 117),
          ("sht-riD9Port", 119),
          ("sht-riFOPort", 120),
          ("sht-riRJ45Port", 118),
          ("sht-roD9Port", 122),
          ("sht-roFOPort", 123),
          ("sht-roRJ45Port", 121),
          ("starFO", 39),
          ("unknownPort", 255))
    )


_GenPortType_Type.__name__ = "Integer32"
_GenPortType_Object = MibTableColumn
genPortType = _GenPortType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 4),
    _GenPortType_Type()
)
genPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortType.setStatus("mandatory")


class _GenPortDescr_Type(DisplayString):
    """Custom type genPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GenPortDescr_Type.__name__ = "DisplayString"
_GenPortDescr_Object = MibTableColumn
genPortDescr = _GenPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 5),
    _GenPortDescr_Type()
)
genPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortDescr.setStatus("mandatory")


class _GenPortActivityStatus_Type(Integer32):
    """Custom type genPortActivityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("dormant", 2),
          ("notActive", 1),
          ("notSupported", 255))
    )


_GenPortActivityStatus_Type.__name__ = "Integer32"
_GenPortActivityStatus_Object = MibTableColumn
genPortActivityStatus = _GenPortActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 6),
    _GenPortActivityStatus_Type()
)
genPortActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortActivityStatus.setStatus("mandatory")
_GenPortSecurityPolicy_Type = OctetString
_GenPortSecurityPolicy_Object = MibTableColumn
genPortSecurityPolicy = _GenPortSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 7),
    _GenPortSecurityPolicy_Type()
)
genPortSecurityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genPortSecurityPolicy.setStatus("mandatory")
_GenPortSecureAddresses_Type = OctetString
_GenPortSecureAddresses_Object = MibTableColumn
genPortSecureAddresses = _GenPortSecureAddresses_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 8),
    _GenPortSecureAddresses_Type()
)
genPortSecureAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genPortSecureAddresses.setStatus("mandatory")


class _GenPortIntPortConnection_Type(Integer32):
    """Custom type genPortIntPortConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GenPortIntPortConnection_Type.__name__ = "Integer32"
_GenPortIntPortConnection_Object = MibTableColumn
genPortIntPortConnection = _GenPortIntPortConnection_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 9),
    _GenPortIntPortConnection_Type()
)
genPortIntPortConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortIntPortConnection.setStatus("mandatory")


class _GenPortAdminStatus_Type(Integer32):
    """Custom type genPortAdminStatus based on Integer32"""
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


_GenPortAdminStatus_Type.__name__ = "Integer32"
_GenPortAdminStatus_Object = MibTableColumn
genPortAdminStatus = _GenPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 10),
    _GenPortAdminStatus_Type()
)
genPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genPortAdminStatus.setStatus("mandatory")
_GenPortSpecificOID_Type = ObjectIdentifier
_GenPortSpecificOID_Object = MibTableColumn
genPortSpecificOID = _GenPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 9, 1, 1, 11),
    _GenPortSpecificOID_Type()
)
genPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPortSpecificOID.setStatus("mandatory")
_GenIntPort_ObjectIdentity = ObjectIdentity
genIntPort = _GenIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10)
)
_GenIntPortTable_Object = MibTable
genIntPortTable = _GenIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    genIntPortTable.setStatus("mandatory")
_GenIntPortEntry_Object = MibTableRow
genIntPortEntry = _GenIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1)
)
genIntPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "genIntPortGroupId"),
    (0, "FIBRONICS-MIB", "genIntPortId"),
)
if mibBuilder.loadTexts:
    genIntPortEntry.setStatus("mandatory")


class _GenIntPortGroupId_Type(Integer32):
    """Custom type genIntPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GenIntPortGroupId_Type.__name__ = "Integer32"
_GenIntPortGroupId_Object = MibTableColumn
genIntPortGroupId = _GenIntPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 1),
    _GenIntPortGroupId_Type()
)
genIntPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortGroupId.setStatus("mandatory")


class _GenIntPortId_Type(Integer32):
    """Custom type genIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_GenIntPortId_Type.__name__ = "Integer32"
_GenIntPortId_Object = MibTableColumn
genIntPortId = _GenIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 2),
    _GenIntPortId_Type()
)
genIntPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortId.setStatus("mandatory")


class _GenIntPortAdminStatus_Type(Integer32):
    """Custom type genIntPortAdminStatus based on Integer32"""
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


_GenIntPortAdminStatus_Type.__name__ = "Integer32"
_GenIntPortAdminStatus_Object = MibTableColumn
genIntPortAdminStatus = _GenIntPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 3),
    _GenIntPortAdminStatus_Type()
)
genIntPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genIntPortAdminStatus.setStatus("mandatory")


class _GenIntPortActivityStatus_Type(Integer32):
    """Custom type genIntPortActivityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("dormant", 2),
          ("notActive", 1),
          ("notSupported", 255))
    )


_GenIntPortActivityStatus_Type.__name__ = "Integer32"
_GenIntPortActivityStatus_Object = MibTableColumn
genIntPortActivityStatus = _GenIntPortActivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 4),
    _GenIntPortActivityStatus_Type()
)
genIntPortActivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortActivityStatus.setStatus("mandatory")


class _GenIntPortBusConnNumber_Type(Integer32):
    """Custom type genIntPortBusConnNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GenIntPortBusConnNumber_Type.__name__ = "Integer32"
_GenIntPortBusConnNumber_Object = MibTableColumn
genIntPortBusConnNumber = _GenIntPortBusConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 5),
    _GenIntPortBusConnNumber_Type()
)
genIntPortBusConnNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genIntPortBusConnNumber.setStatus("mandatory")


class _GenIntPortBusConnType_Type(Integer32):
    """Custom type genIntPortBusConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("fddi", 4),
          ("high-speed", 5),
          ("local-talk", 3),
          ("other", 255),
          ("token-ring", 2))
    )


_GenIntPortBusConnType_Type.__name__ = "Integer32"
_GenIntPortBusConnType_Object = MibTableColumn
genIntPortBusConnType = _GenIntPortBusConnType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 6),
    _GenIntPortBusConnType_Type()
)
genIntPortBusConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortBusConnType.setStatus("mandatory")
_GenIntPortSpecificOID_Type = ObjectIdentifier
_GenIntPortSpecificOID_Object = MibTableColumn
genIntPortSpecificOID = _GenIntPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 7),
    _GenIntPortSpecificOID_Type()
)
genIntPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genIntPortSpecificOID.setStatus("mandatory")


class _GenIntPortMonitorMode_Type(Integer32):
    """Custom type genIntPortMonitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_GenIntPortMonitorMode_Type.__name__ = "Integer32"
_GenIntPortMonitorMode_Object = MibTableColumn
genIntPortMonitorMode = _GenIntPortMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 10, 1, 1, 8),
    _GenIntPortMonitorMode_Type()
)
genIntPortMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genIntPortMonitorMode.setStatus("mandatory")
_SoftRedundancy_ObjectIdentity = ObjectIdentity
softRedundancy = _SoftRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11)
)
_SoftRedundancyTable_Object = MibTable
softRedundancyTable = _SoftRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1)
)
if mibBuilder.loadTexts:
    softRedundancyTable.setStatus("mandatory")
_SoftRedundancyEntry_Object = MibTableRow
softRedundancyEntry = _SoftRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1)
)
softRedundancyEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "softRedundancyId"),
)
if mibBuilder.loadTexts:
    softRedundancyEntry.setStatus("mandatory")


class _SoftRedundancyId_Type(Integer32):
    """Custom type softRedundancyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SoftRedundancyId_Type.__name__ = "Integer32"
_SoftRedundancyId_Object = MibTableColumn
softRedundancyId = _SoftRedundancyId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1, 1),
    _SoftRedundancyId_Type()
)
softRedundancyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softRedundancyId.setStatus("mandatory")


class _SoftRedundancyName_Type(DisplayString):
    """Custom type softRedundancyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_SoftRedundancyName_Type.__name__ = "DisplayString"
_SoftRedundancyName_Object = MibTableColumn
softRedundancyName = _SoftRedundancyName_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1, 2),
    _SoftRedundancyName_Type()
)
softRedundancyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softRedundancyName.setStatus("mandatory")


class _SoftRedundancyGroupId1_Type(Integer32):
    """Custom type softRedundancyGroupId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SoftRedundancyGroupId1_Type.__name__ = "Integer32"
_SoftRedundancyGroupId1_Object = MibTableColumn
softRedundancyGroupId1 = _SoftRedundancyGroupId1_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1, 3),
    _SoftRedundancyGroupId1_Type()
)
softRedundancyGroupId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softRedundancyGroupId1.setStatus("mandatory")


class _SoftRedundancyPortId1_Type(Integer32):
    """Custom type softRedundancyPortId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SoftRedundancyPortId1_Type.__name__ = "Integer32"
_SoftRedundancyPortId1_Object = MibTableColumn
softRedundancyPortId1 = _SoftRedundancyPortId1_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1, 4),
    _SoftRedundancyPortId1_Type()
)
softRedundancyPortId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softRedundancyPortId1.setStatus("mandatory")


class _SoftRedundancyGroupId2_Type(Integer32):
    """Custom type softRedundancyGroupId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SoftRedundancyGroupId2_Type.__name__ = "Integer32"
_SoftRedundancyGroupId2_Object = MibTableColumn
softRedundancyGroupId2 = _SoftRedundancyGroupId2_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1, 5),
    _SoftRedundancyGroupId2_Type()
)
softRedundancyGroupId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softRedundancyGroupId2.setStatus("mandatory")


class _SoftRedundancyPortId2_Type(Integer32):
    """Custom type softRedundancyPortId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SoftRedundancyPortId2_Type.__name__ = "Integer32"
_SoftRedundancyPortId2_Object = MibTableColumn
softRedundancyPortId2 = _SoftRedundancyPortId2_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1, 6),
    _SoftRedundancyPortId2_Type()
)
softRedundancyPortId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softRedundancyPortId2.setStatus("mandatory")


class _SoftRedundancyStatus_Type(Integer32):
    """Custom type softRedundancyStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_SoftRedundancyStatus_Type.__name__ = "Integer32"
_SoftRedundancyStatus_Object = MibTableColumn
softRedundancyStatus = _SoftRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 11, 1, 1, 7),
    _SoftRedundancyStatus_Type()
)
softRedundancyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    softRedundancyStatus.setStatus("mandatory")
_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12)
)
_EthAg_ObjectIdentity = ObjectIdentity
ethAg = _EthAg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 1)
)
_EthAgTable_Object = MibTable
ethAgTable = _EthAgTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ethAgTable.setStatus("mandatory")
_EthAgEntry_Object = MibTableRow
ethAgEntry = _EthAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 1, 1, 1)
)
ethAgEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "ethAgId"),
)
if mibBuilder.loadTexts:
    ethAgEntry.setStatus("mandatory")


class _EthAgId_Type(Integer32):
    """Custom type ethAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthAgId_Type.__name__ = "Integer32"
_EthAgId_Object = MibTableColumn
ethAgId = _EthAgId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 1, 1, 1, 1),
    _EthAgId_Type()
)
ethAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethAgId.setStatus("mandatory")
_EthAgPerfBusSelection_Type = Integer32
_EthAgPerfBusSelection_Object = MibTableColumn
ethAgPerfBusSelection = _EthAgPerfBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 1, 1, 1, 2),
    _EthAgPerfBusSelection_Type()
)
ethAgPerfBusSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethAgPerfBusSelection.setStatus("mandatory")
_EthGroup_ObjectIdentity = ObjectIdentity
ethGroup = _EthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2)
)
_EthGroupTable_Object = MibTable
ethGroupTable = _EthGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1)
)
if mibBuilder.loadTexts:
    ethGroupTable.setStatus("mandatory")
_EthGroupEntry_Object = MibTableRow
ethGroupEntry = _EthGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1)
)
ethGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "ethGroupId"),
)
if mibBuilder.loadTexts:
    ethGroupEntry.setStatus("mandatory")


class _EthGroupId_Type(Integer32):
    """Custom type ethGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthGroupId_Type.__name__ = "Integer32"
_EthGroupId_Object = MibTableColumn
ethGroupId = _EthGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 1),
    _EthGroupId_Type()
)
ethGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupId.setStatus("mandatory")


class _EthGroupFIFO_Type(Integer32):
    """Custom type ethGroupFIFO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupFIFO_Type.__name__ = "Integer32"
_EthGroupFIFO_Object = MibTableColumn
ethGroupFIFO = _EthGroupFIFO_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 2),
    _EthGroupFIFO_Type()
)
ethGroupFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupFIFO.setStatus("mandatory")


class _EthGroup10BTPlus_Type(Integer32):
    """Custom type ethGroup10BTPlus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroup10BTPlus_Type.__name__ = "Integer32"
_EthGroup10BTPlus_Object = MibTableColumn
ethGroup10BTPlus = _EthGroup10BTPlus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 3),
    _EthGroup10BTPlus_Type()
)
ethGroup10BTPlus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroup10BTPlus.setStatus("mandatory")


class _EthGroupIntPortsRedundancy_Type(Integer32):
    """Custom type ethGroupIntPortsRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupIntPortsRedundancy_Type.__name__ = "Integer32"
_EthGroupIntPortsRedundancy_Object = MibTableColumn
ethGroupIntPortsRedundancy = _EthGroupIntPortsRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 4),
    _EthGroupIntPortsRedundancy_Type()
)
ethGroupIntPortsRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupIntPortsRedundancy.setStatus("mandatory")


class _EthGroupBackboneMode_Type(Integer32):
    """Custom type ethGroupBackboneMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupBackboneMode_Type.__name__ = "Integer32"
_EthGroupBackboneMode_Object = MibTableColumn
ethGroupBackboneMode = _EthGroupBackboneMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 5),
    _EthGroupBackboneMode_Type()
)
ethGroupBackboneMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupBackboneMode.setStatus("mandatory")


class _EthGroupFOIRLPlusMode_Type(Integer32):
    """Custom type ethGroupFOIRLPlusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupFOIRLPlusMode_Type.__name__ = "Integer32"
_EthGroupFOIRLPlusMode_Object = MibTableColumn
ethGroupFOIRLPlusMode = _EthGroupFOIRLPlusMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 6),
    _EthGroupFOIRLPlusMode_Type()
)
ethGroupFOIRLPlusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupFOIRLPlusMode.setStatus("mandatory")


class _EthGroupWrongPortSelection_Type(Integer32):
    """Custom type ethGroupWrongPortSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupWrongPortSelection_Type.__name__ = "Integer32"
_EthGroupWrongPortSelection_Object = MibTableColumn
ethGroupWrongPortSelection = _EthGroupWrongPortSelection_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 7),
    _EthGroupWrongPortSelection_Type()
)
ethGroupWrongPortSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupWrongPortSelection.setStatus("mandatory")


class _EthGroupBackupBus_Type(Integer32):
    """Custom type ethGroupBackupBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EthGroupBackupBus_Type.__name__ = "Integer32"
_EthGroupBackupBus_Object = MibTableColumn
ethGroupBackupBus = _EthGroupBackupBus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 8),
    _EthGroupBackupBus_Type()
)
ethGroupBackupBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupBackupBus.setStatus("mandatory")


class _EthGroupSingleBusMode_Type(Integer32):
    """Custom type ethGroupSingleBusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupSingleBusMode_Type.__name__ = "Integer32"
_EthGroupSingleBusMode_Object = MibTableColumn
ethGroupSingleBusMode = _EthGroupSingleBusMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 9),
    _EthGroupSingleBusMode_Type()
)
ethGroupSingleBusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupSingleBusMode.setStatus("mandatory")
_EthGroupSpecificOID_Type = ObjectIdentifier
_EthGroupSpecificOID_Object = MibTableColumn
ethGroupSpecificOID = _EthGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 10),
    _EthGroupSpecificOID_Type()
)
ethGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupSpecificOID.setStatus("mandatory")


class _EthGroup10FBPlus_Type(Integer32):
    """Custom type ethGroup10FBPlus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroup10FBPlus_Type.__name__ = "Integer32"
_EthGroup10FBPlus_Object = MibTableColumn
ethGroup10FBPlus = _EthGroup10FBPlus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 11),
    _EthGroup10FBPlus_Type()
)
ethGroup10FBPlus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroup10FBPlus.setStatus("mandatory")


class _EthGroupMasterClock_Type(Integer32):
    """Custom type ethGroupMasterClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupMasterClock_Type.__name__ = "Integer32"
_EthGroupMasterClock_Object = MibTableColumn
ethGroupMasterClock = _EthGroupMasterClock_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 12),
    _EthGroupMasterClock_Type()
)
ethGroupMasterClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupMasterClock.setStatus("mandatory")


class _EthGroupIdleTrx_Type(Integer32):
    """Custom type ethGroupIdleTrx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupIdleTrx_Type.__name__ = "Integer32"
_EthGroupIdleTrx_Object = MibTableColumn
ethGroupIdleTrx = _EthGroupIdleTrx_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 13),
    _EthGroupIdleTrx_Type()
)
ethGroupIdleTrx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethGroupIdleTrx.setStatus("mandatory")


class _EthGroupMJLPStatus_Type(Integer32):
    """Custom type ethGroupMJLPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthGroupMJLPStatus_Type.__name__ = "Integer32"
_EthGroupMJLPStatus_Object = MibTableColumn
ethGroupMJLPStatus = _EthGroupMJLPStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 2, 1, 1, 14),
    _EthGroupMJLPStatus_Type()
)
ethGroupMJLPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethGroupMJLPStatus.setStatus("mandatory")
_EthPort_ObjectIdentity = ObjectIdentity
ethPort = _EthPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3)
)
_EthPortTable_Object = MibTable
ethPortTable = _EthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1)
)
if mibBuilder.loadTexts:
    ethPortTable.setStatus("mandatory")
_EthPortEntry_Object = MibTableRow
ethPortEntry = _EthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1)
)
ethPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "ethPortGroupId"),
    (0, "FIBRONICS-MIB", "ethPortId"),
)
if mibBuilder.loadTexts:
    ethPortEntry.setStatus("mandatory")
_EthPortGroupId_Type = Integer32
_EthPortGroupId_Object = MibTableColumn
ethPortGroupId = _EthPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 1),
    _EthPortGroupId_Type()
)
ethPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortGroupId.setStatus("mandatory")
_EthPortId_Type = Integer32
_EthPortId_Object = MibTableColumn
ethPortId = _EthPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 2),
    _EthPortId_Type()
)
ethPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortId.setStatus("mandatory")


class _EthPortFunctionalStatus_Type(Integer32):
    """Custom type ethPortFunctionalStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("illSeq", 6),
          ("localJabber", 3),
          ("lockLost", 11),
          ("notSupported", 255),
          ("ok", 1),
          ("partitionOrLocalJabber", 8),
          ("remoteFault", 10),
          ("remoteFaultOrLockLost", 9),
          ("remoteJabber", 5),
          ("rld", 2),
          ("shortCirc", 7),
          ("tld", 4))
    )


_EthPortFunctionalStatus_Type.__name__ = "Integer32"
_EthPortFunctionalStatus_Object = MibTableColumn
ethPortFunctionalStatus = _EthPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 3),
    _EthPortFunctionalStatus_Type()
)
ethPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFunctionalStatus.setStatus("mandatory")


class _EthPortManPart_Type(Integer32):
    """Custom type ethPortManPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthPortManPart_Type.__name__ = "Integer32"
_EthPortManPart_Object = MibTableColumn
ethPortManPart = _EthPortManPart_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 4),
    _EthPortManPart_Type()
)
ethPortManPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortManPart.setStatus("mandatory")


class _EthPortJabber_Type(Integer32):
    """Custom type ethPortJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthPortJabber_Type.__name__ = "Integer32"
_EthPortJabber_Object = MibTableColumn
ethPortJabber = _EthPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 5),
    _EthPortJabber_Type()
)
ethPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortJabber.setStatus("mandatory")


class _EthPortNoAUILoop_Type(Integer32):
    """Custom type ethPortNoAUILoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthPortNoAUILoop_Type.__name__ = "Integer32"
_EthPortNoAUILoop_Object = MibTableColumn
ethPortNoAUILoop = _EthPortNoAUILoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 6),
    _EthPortNoAUILoop_Type()
)
ethPortNoAUILoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortNoAUILoop.setStatus("mandatory")


class _EthPortMJLP_Type(Integer32):
    """Custom type ethPortMJLP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthPortMJLP_Type.__name__ = "Integer32"
_EthPortMJLP_Object = MibTableColumn
ethPortMJLP = _EthPortMJLP_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 7),
    _EthPortMJLP_Type()
)
ethPortMJLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortMJLP.setStatus("mandatory")


class _EthPortFIFO_Type(Integer32):
    """Custom type ethPortFIFO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthPortFIFO_Type.__name__ = "Integer32"
_EthPortFIFO_Object = MibTableColumn
ethPortFIFO = _EthPortFIFO_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 8),
    _EthPortFIFO_Type()
)
ethPortFIFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFIFO.setStatus("mandatory")


class _EthPortAutoPartitionState_Type(Integer32):
    """Custom type ethPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoPartition", 1),
          ("notAutoPartition", 2),
          ("notSupported", 255))
    )


_EthPortAutoPartitionState_Type.__name__ = "Integer32"
_EthPortAutoPartitionState_Object = MibTableColumn
ethPortAutoPartitionState = _EthPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 9),
    _EthPortAutoPartitionState_Type()
)
ethPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortAutoPartitionState.setStatus("mandatory")


class _EthPortSQETest_Type(Integer32):
    """Custom type ethPortSQETest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notSupported", 255))
    )


_EthPortSQETest_Type.__name__ = "Integer32"
_EthPortSQETest_Object = MibTableColumn
ethPortSQETest = _EthPortSQETest_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 10),
    _EthPortSQETest_Type()
)
ethPortSQETest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortSQETest.setStatus("mandatory")
_EthPortLastSourceAddr_Type = OctetString
_EthPortLastSourceAddr_Object = MibTableColumn
ethPortLastSourceAddr = _EthPortLastSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 11),
    _EthPortLastSourceAddr_Type()
)
ethPortLastSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortLastSourceAddr.setStatus("mandatory")


class _EthPortUserStatus_Type(Integer32):
    """Custom type ethPortUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("multiUser", 2),
          ("notSupported", 255),
          ("singleUser", 1))
    )


_EthPortUserStatus_Type.__name__ = "Integer32"
_EthPortUserStatus_Object = MibTableColumn
ethPortUserStatus = _EthPortUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 12),
    _EthPortUserStatus_Type()
)
ethPortUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortUserStatus.setStatus("mandatory")
_EthPortMainBusSelection_Type = Integer32
_EthPortMainBusSelection_Object = MibTableColumn
ethPortMainBusSelection = _EthPortMainBusSelection_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 13),
    _EthPortMainBusSelection_Type()
)
ethPortMainBusSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethPortMainBusSelection.setStatus("mandatory")
_EthPortTraffic_Type = Counter32
_EthPortTraffic_Object = MibTableColumn
ethPortTraffic = _EthPortTraffic_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 14),
    _EthPortTraffic_Type()
)
ethPortTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortTraffic.setStatus("mandatory")
_EthPortFramesReceivedOK_Type = Counter32
_EthPortFramesReceivedOK_Object = MibTableColumn
ethPortFramesReceivedOK = _EthPortFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 15),
    _EthPortFramesReceivedOK_Type()
)
ethPortFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortFramesReceivedOK.setStatus("mandatory")
_EthPortRunts_Type = Counter32
_EthPortRunts_Object = MibTableColumn
ethPortRunts = _EthPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 16),
    _EthPortRunts_Type()
)
ethPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortRunts.setStatus("mandatory")
_EthPortPacketErrors_Type = Counter32
_EthPortPacketErrors_Object = MibTableColumn
ethPortPacketErrors = _EthPortPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 17),
    _EthPortPacketErrors_Type()
)
ethPortPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPacketErrors.setStatus("mandatory")
_EthPortSpecificOID_Type = ObjectIdentifier
_EthPortSpecificOID_Object = MibTableColumn
ethPortSpecificOID = _EthPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 18),
    _EthPortSpecificOID_Type()
)
ethPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortSpecificOID.setStatus("mandatory")
_EthPortCollisions_Type = Counter32
_EthPortCollisions_Object = MibTableColumn
ethPortCollisions = _EthPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 19),
    _EthPortCollisions_Type()
)
ethPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortCollisions.setStatus("mandatory")
_EthPortPartitions_Type = Counter32
_EthPortPartitions_Object = MibTableColumn
ethPortPartitions = _EthPortPartitions_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 20),
    _EthPortPartitions_Type()
)
ethPortPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPartitions.setStatus("mandatory")
_EthPortPygmys_Type = Counter32
_EthPortPygmys_Object = MibTableColumn
ethPortPygmys = _EthPortPygmys_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 3, 1, 1, 21),
    _EthPortPygmys_Type()
)
ethPortPygmys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortPygmys.setStatus("mandatory")
_EthIntPort_ObjectIdentity = ObjectIdentity
ethIntPort = _EthIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4)
)
_EthIntPortTable_Object = MibTable
ethIntPortTable = _EthIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4, 1)
)
if mibBuilder.loadTexts:
    ethIntPortTable.setStatus("mandatory")
_EthIntPortEntry_Object = MibTableRow
ethIntPortEntry = _EthIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4, 1, 1)
)
ethIntPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "ethIntPortGroupId"),
    (0, "FIBRONICS-MIB", "ethIntPortId"),
)
if mibBuilder.loadTexts:
    ethIntPortEntry.setStatus("mandatory")


class _EthIntPortGroupId_Type(Integer32):
    """Custom type ethIntPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthIntPortGroupId_Type.__name__ = "Integer32"
_EthIntPortGroupId_Object = MibTableColumn
ethIntPortGroupId = _EthIntPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4, 1, 1, 1),
    _EthIntPortGroupId_Type()
)
ethIntPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortGroupId.setStatus("mandatory")


class _EthIntPortId_Type(Integer32):
    """Custom type ethIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthIntPortId_Type.__name__ = "Integer32"
_EthIntPortId_Object = MibTableColumn
ethIntPortId = _EthIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4, 1, 1, 2),
    _EthIntPortId_Type()
)
ethIntPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortId.setStatus("mandatory")


class _EthIntPortPartition_Type(Integer32):
    """Custom type ethIntPortPartition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthIntPortPartition_Type.__name__ = "Integer32"
_EthIntPortPartition_Object = MibTableColumn
ethIntPortPartition = _EthIntPortPartition_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4, 1, 1, 3),
    _EthIntPortPartition_Type()
)
ethIntPortPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortPartition.setStatus("mandatory")


class _EthIntPortJabber_Type(Integer32):
    """Custom type ethIntPortJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthIntPortJabber_Type.__name__ = "Integer32"
_EthIntPortJabber_Object = MibTableColumn
ethIntPortJabber = _EthIntPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4, 1, 1, 4),
    _EthIntPortJabber_Type()
)
ethIntPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIntPortJabber.setStatus("mandatory")


class _EthIntPortBackedUp_Type(Integer32):
    """Custom type ethIntPortBackedUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_EthIntPortBackedUp_Type.__name__ = "Integer32"
_EthIntPortBackedUp_Object = MibTableColumn
ethIntPortBackedUp = _EthIntPortBackedUp_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 4, 1, 1, 5),
    _EthIntPortBackedUp_Type()
)
ethIntPortBackedUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIntPortBackedUp.setStatus("mandatory")
_EthBus_ObjectIdentity = ObjectIdentity
ethBus = _EthBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5)
)
_EthBusPerfTable_Object = MibTable
ethBusPerfTable = _EthBusPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1)
)
if mibBuilder.loadTexts:
    ethBusPerfTable.setStatus("mandatory")
_EthBusPerfEntry_Object = MibTableRow
ethBusPerfEntry = _EthBusPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1)
)
ethBusPerfEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "ethBusPerfAgId"),
    (0, "FIBRONICS-MIB", "ethBusPerfId"),
)
if mibBuilder.loadTexts:
    ethBusPerfEntry.setStatus("mandatory")


class _EthBusPerfAgId_Type(Integer32):
    """Custom type ethBusPerfAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusPerfAgId_Type.__name__ = "Integer32"
_EthBusPerfAgId_Object = MibTableColumn
ethBusPerfAgId = _EthBusPerfAgId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 1),
    _EthBusPerfAgId_Type()
)
ethBusPerfAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPerfAgId.setStatus("mandatory")


class _EthBusPerfId_Type(Integer32):
    """Custom type ethBusPerfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusPerfId_Type.__name__ = "Integer32"
_EthBusPerfId_Object = MibTableColumn
ethBusPerfId = _EthBusPerfId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 2),
    _EthBusPerfId_Type()
)
ethBusPerfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPerfId.setStatus("mandatory")
_EthBusTrafficBuffer_Type = OctetString
_EthBusTrafficBuffer_Object = MibTableColumn
ethBusTrafficBuffer = _EthBusTrafficBuffer_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 3),
    _EthBusTrafficBuffer_Type()
)
ethBusTrafficBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTrafficBuffer.setStatus("mandatory")
_EthBusTrafficThresh_Type = Integer32
_EthBusTrafficThresh_Object = MibTableColumn
ethBusTrafficThresh = _EthBusTrafficThresh_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 4),
    _EthBusTrafficThresh_Type()
)
ethBusTrafficThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBusTrafficThresh.setStatus("mandatory")
_EthBusPeakTraffic_Type = Integer32
_EthBusPeakTraffic_Object = MibTableColumn
ethBusPeakTraffic = _EthBusPeakTraffic_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 5),
    _EthBusPeakTraffic_Type()
)
ethBusPeakTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPeakTraffic.setStatus("mandatory")
_EthBusTotalCollisions_Type = Counter32
_EthBusTotalCollisions_Object = MibTableColumn
ethBusTotalCollisions = _EthBusTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 6),
    _EthBusTotalCollisions_Type()
)
ethBusTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalCollisions.setStatus("mandatory")
_EthBusTotalPackets_Type = Counter32
_EthBusTotalPackets_Object = MibTableColumn
ethBusTotalPackets = _EthBusTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 7),
    _EthBusTotalPackets_Type()
)
ethBusTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalPackets.setStatus("mandatory")
_EthBusTotalErrors_Type = Counter32
_EthBusTotalErrors_Object = MibTableColumn
ethBusTotalErrors = _EthBusTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 8),
    _EthBusTotalErrors_Type()
)
ethBusTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTotalErrors.setStatus("mandatory")
_EthBusTraffic_Type = Integer32
_EthBusTraffic_Object = MibTableColumn
ethBusTraffic = _EthBusTraffic_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 9),
    _EthBusTraffic_Type()
)
ethBusTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusTraffic.setStatus("mandatory")
_EthBusUtilization_Type = Integer32
_EthBusUtilization_Object = MibTableColumn
ethBusUtilization = _EthBusUtilization_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 10),
    _EthBusUtilization_Type()
)
ethBusUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusUtilization.setStatus("mandatory")
_EthBusPeakUtilization_Type = Integer32
_EthBusPeakUtilization_Object = MibTableColumn
ethBusPeakUtilization = _EthBusPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 1, 1, 11),
    _EthBusPeakUtilization_Type()
)
ethBusPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusPeakUtilization.setStatus("mandatory")
_EthBusClockTable_Object = MibTable
ethBusClockTable = _EthBusClockTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 2)
)
if mibBuilder.loadTexts:
    ethBusClockTable.setStatus("mandatory")
_EthBusClockEntry_Object = MibTableRow
ethBusClockEntry = _EthBusClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 2, 1)
)
ethBusClockEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "ethBusClockBusId"),
    (0, "FIBRONICS-MIB", "ethBusClockId"),
)
if mibBuilder.loadTexts:
    ethBusClockEntry.setStatus("mandatory")


class _EthBusClockBusId_Type(Integer32):
    """Custom type ethBusClockBusId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusClockBusId_Type.__name__ = "Integer32"
_EthBusClockBusId_Object = MibTableColumn
ethBusClockBusId = _EthBusClockBusId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 2, 1, 1),
    _EthBusClockBusId_Type()
)
ethBusClockBusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusClockBusId.setStatus("mandatory")


class _EthBusClockId_Type(Integer32):
    """Custom type ethBusClockId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthBusClockId_Type.__name__ = "Integer32"
_EthBusClockId_Object = MibTableColumn
ethBusClockId = _EthBusClockId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 2, 1, 2),
    _EthBusClockId_Type()
)
ethBusClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusClockId.setStatus("mandatory")


class _EthBusClockTestResult_Type(Integer32):
    """Custom type ethBusClockTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("busFailure", 3),
          ("clockFailure", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_EthBusClockTestResult_Type.__name__ = "Integer32"
_EthBusClockTestResult_Object = MibTableColumn
ethBusClockTestResult = _EthBusClockTestResult_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 12, 5, 2, 1, 3),
    _EthBusClockTestResult_Type()
)
ethBusClockTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethBusClockTestResult.setStatus("mandatory")
_Tok_ObjectIdentity = ObjectIdentity
tok = _Tok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13)
)
_TokRing_ObjectIdentity = ObjectIdentity
tokRing = _TokRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1)
)
_TokRingTable_Object = MibTable
tokRingTable = _TokRingTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tokRingTable.setStatus("mandatory")
_TokRingEntry_Object = MibTableRow
tokRingEntry = _TokRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1)
)
tokRingEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "tokRingAgId"),
    (0, "FIBRONICS-MIB", "tokRingId"),
)
if mibBuilder.loadTexts:
    tokRingEntry.setStatus("mandatory")


class _TokRingAgId_Type(Integer32):
    """Custom type tokRingAgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingAgId_Type.__name__ = "Integer32"
_TokRingAgId_Object = MibTableColumn
tokRingAgId = _TokRingAgId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 1),
    _TokRingAgId_Type()
)
tokRingAgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingAgId.setStatus("mandatory")


class _TokRingId_Type(Integer32):
    """Custom type tokRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingId_Type.__name__ = "Integer32"
_TokRingId_Object = MibTableColumn
tokRingId = _TokRingId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 2),
    _TokRingId_Type()
)
tokRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingId.setStatus("mandatory")


class _TokRingLeftSlot_Type(Integer32):
    """Custom type tokRingLeftSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingLeftSlot_Type.__name__ = "Integer32"
_TokRingLeftSlot_Object = MibTableColumn
tokRingLeftSlot = _TokRingLeftSlot_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 3),
    _TokRingLeftSlot_Type()
)
tokRingLeftSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingLeftSlot.setStatus("mandatory")


class _TokRingRightSlot_Type(Integer32):
    """Custom type tokRingRightSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokRingRightSlot_Type.__name__ = "Integer32"
_TokRingRightSlot_Object = MibTableColumn
tokRingRightSlot = _TokRingRightSlot_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 4),
    _TokRingRightSlot_Type()
)
tokRingRightSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingRightSlot.setStatus("mandatory")
_TokRingTrafficBuffer_Type = OctetString
_TokRingTrafficBuffer_Object = MibTableColumn
tokRingTrafficBuffer = _TokRingTrafficBuffer_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 5),
    _TokRingTrafficBuffer_Type()
)
tokRingTrafficBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingTrafficBuffer.setStatus("mandatory")
_TokRingTrafficThresh_Type = Integer32
_TokRingTrafficThresh_Object = MibTableColumn
tokRingTrafficThresh = _TokRingTrafficThresh_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 6),
    _TokRingTrafficThresh_Type()
)
tokRingTrafficThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingTrafficThresh.setStatus("mandatory")
_TokRingPeakTraffic_Type = Integer32
_TokRingPeakTraffic_Object = MibTableColumn
tokRingPeakTraffic = _TokRingPeakTraffic_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 7),
    _TokRingPeakTraffic_Type()
)
tokRingPeakTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingPeakTraffic.setStatus("mandatory")
_TokRingNumberOfStations_Type = Integer32
_TokRingNumberOfStations_Object = MibTableColumn
tokRingNumberOfStations = _TokRingNumberOfStations_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 8),
    _TokRingNumberOfStations_Type()
)
tokRingNumberOfStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingNumberOfStations.setStatus("mandatory")
_TokRingConfiguration_Type = OctetString
_TokRingConfiguration_Object = MibTableColumn
tokRingConfiguration = _TokRingConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 9),
    _TokRingConfiguration_Type()
)
tokRingConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingConfiguration.setStatus("mandatory")


class _TokRingBeaconing_Type(Integer32):
    """Custom type tokRingBeaconing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokRingBeaconing_Type.__name__ = "Integer32"
_TokRingBeaconing_Object = MibTableColumn
tokRingBeaconing = _TokRingBeaconing_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 10),
    _TokRingBeaconing_Type()
)
tokRingBeaconing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingBeaconing.setStatus("mandatory")
_TokRingBeaconingStation_Type = OctetString
_TokRingBeaconingStation_Object = MibTableColumn
tokRingBeaconingStation = _TokRingBeaconingStation_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 11),
    _TokRingBeaconingStation_Type()
)
tokRingBeaconingStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingBeaconingStation.setStatus("mandatory")


class _TokRingStationsMatch_Type(Integer32):
    """Custom type tokRingStationsMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokRingStationsMatch_Type.__name__ = "Integer32"
_TokRingStationsMatch_Object = MibTableColumn
tokRingStationsMatch = _TokRingStationsMatch_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 12),
    _TokRingStationsMatch_Type()
)
tokRingStationsMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingStationsMatch.setStatus("mandatory")
_TokRingTraffic_Type = Integer32
_TokRingTraffic_Object = MibTableColumn
tokRingTraffic = _TokRingTraffic_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 13),
    _TokRingTraffic_Type()
)
tokRingTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingTraffic.setStatus("mandatory")


class _TokRingSecurityMethod_Type(Integer32):
    """Custom type tokRingSecurityMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("notSupported", 255),
          ("perPort", 1),
          ("perRing", 2))
    )


_TokRingSecurityMethod_Type.__name__ = "Integer32"
_TokRingSecurityMethod_Object = MibTableColumn
tokRingSecurityMethod = _TokRingSecurityMethod_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 14),
    _TokRingSecurityMethod_Type()
)
tokRingSecurityMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingSecurityMethod.setStatus("mandatory")


class _TokRingSecurityPolicy_Type(OctetString):
    """Custom type tokRingSecurityPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TokRingSecurityPolicy_Type.__name__ = "OctetString"
_TokRingSecurityPolicy_Object = MibTableColumn
tokRingSecurityPolicy = _TokRingSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 15),
    _TokRingSecurityPolicy_Type()
)
tokRingSecurityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingSecurityPolicy.setStatus("mandatory")
_TokRingSecureAddr_Type = OctetString
_TokRingSecureAddr_Object = MibTableColumn
tokRingSecureAddr = _TokRingSecureAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 16),
    _TokRingSecureAddr_Type()
)
tokRingSecureAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokRingSecureAddr.setStatus("mandatory")
_TokRingLastViolation_Type = OctetString
_TokRingLastViolation_Object = MibTableColumn
tokRingLastViolation = _TokRingLastViolation_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 17),
    _TokRingLastViolation_Type()
)
tokRingLastViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingLastViolation.setStatus("mandatory")
_TokRingUtilization_Type = Integer32
_TokRingUtilization_Object = MibTableColumn
tokRingUtilization = _TokRingUtilization_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 18),
    _TokRingUtilization_Type()
)
tokRingUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingUtilization.setStatus("mandatory")
_TokRingPeakUtilization_Type = Integer32
_TokRingPeakUtilization_Object = MibTableColumn
tokRingPeakUtilization = _TokRingPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 1, 1, 1, 19),
    _TokRingPeakUtilization_Type()
)
tokRingPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokRingPeakUtilization.setStatus("mandatory")
_TokGroup_ObjectIdentity = ObjectIdentity
tokGroup = _TokGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2)
)
_TokGroupTable_Object = MibTable
tokGroupTable = _TokGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1)
)
if mibBuilder.loadTexts:
    tokGroupTable.setStatus("mandatory")
_TokGroupEntry_Object = MibTableRow
tokGroupEntry = _TokGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1)
)
tokGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "tokGroupId"),
)
if mibBuilder.loadTexts:
    tokGroupEntry.setStatus("mandatory")


class _TokGroupId_Type(Integer32):
    """Custom type tokGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokGroupId_Type.__name__ = "Integer32"
_TokGroupId_Object = MibTableColumn
tokGroupId = _TokGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 1),
    _TokGroupId_Type()
)
tokGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupId.setStatus("mandatory")


class _TokGroupAutoRightLoop_Type(Integer32):
    """Custom type tokGroupAutoRightLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupAutoRightLoop_Type.__name__ = "Integer32"
_TokGroupAutoRightLoop_Object = MibTableColumn
tokGroupAutoRightLoop = _TokGroupAutoRightLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 2),
    _TokGroupAutoRightLoop_Type()
)
tokGroupAutoRightLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoRightLoop.setStatus("mandatory")


class _TokGroupAutoLeftLoop_Type(Integer32):
    """Custom type tokGroupAutoLeftLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupAutoLeftLoop_Type.__name__ = "Integer32"
_TokGroupAutoLeftLoop_Object = MibTableColumn
tokGroupAutoLeftLoop = _TokGroupAutoLeftLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 3),
    _TokGroupAutoLeftLoop_Type()
)
tokGroupAutoLeftLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoLeftLoop.setStatus("mandatory")


class _TokGroupManRightLoop_Type(Integer32):
    """Custom type tokGroupManRightLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupManRightLoop_Type.__name__ = "Integer32"
_TokGroupManRightLoop_Object = MibTableColumn
tokGroupManRightLoop = _TokGroupManRightLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 4),
    _TokGroupManRightLoop_Type()
)
tokGroupManRightLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManRightLoop.setStatus("mandatory")


class _TokGroupManLeftLoop_Type(Integer32):
    """Custom type tokGroupManLeftLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupManLeftLoop_Type.__name__ = "Integer32"
_TokGroupManLeftLoop_Object = MibTableColumn
tokGroupManLeftLoop = _TokGroupManLeftLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 5),
    _TokGroupManLeftLoop_Type()
)
tokGroupManLeftLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManLeftLoop.setStatus("mandatory")


class _TokGroupRightNeighbor_Type(Integer32):
    """Custom type tokGroupRightNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_TokGroupRightNeighbor_Type.__name__ = "Integer32"
_TokGroupRightNeighbor_Object = MibTableColumn
tokGroupRightNeighbor = _TokGroupRightNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 6),
    _TokGroupRightNeighbor_Type()
)
tokGroupRightNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRightNeighbor.setStatus("mandatory")


class _TokGroupLeftNeighbor_Type(Integer32):
    """Custom type tokGroupLeftNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_TokGroupLeftNeighbor_Type.__name__ = "Integer32"
_TokGroupLeftNeighbor_Object = MibTableColumn
tokGroupLeftNeighbor = _TokGroupLeftNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 7),
    _TokGroupLeftNeighbor_Type()
)
tokGroupLeftNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupLeftNeighbor.setStatus("mandatory")


class _TokGroupIOMode_Type(Integer32):
    """Custom type tokGroupIOMode based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("dualRingIn", 2),
          ("dualRingOut", 3),
          ("illegalMode", 4),
          ("intRepeater", 6),
          ("lobe", 5),
          ("notSupported", 255),
          ("single", 1),
          ("star", 7))
    )


_TokGroupIOMode_Type.__name__ = "Integer32"
_TokGroupIOMode_Object = MibTableColumn
tokGroupIOMode = _TokGroupIOMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 8),
    _TokGroupIOMode_Type()
)
tokGroupIOMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupIOMode.setStatus("mandatory")


class _TokGroupBridgeMode_Type(Integer32):
    """Custom type tokGroupBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("modeA", 1),
          ("modeB", 2),
          ("modeC", 3),
          ("notSupported", 255))
    )


_TokGroupBridgeMode_Type.__name__ = "Integer32"
_TokGroupBridgeMode_Object = MibTableColumn
tokGroupBridgeMode = _TokGroupBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 9),
    _TokGroupBridgeMode_Type()
)
tokGroupBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupBridgeMode.setStatus("mandatory")


class _TokGroupManLinkLoop_Type(Integer32):
    """Custom type tokGroupManLinkLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupManLinkLoop_Type.__name__ = "Integer32"
_TokGroupManLinkLoop_Object = MibTableColumn
tokGroupManLinkLoop = _TokGroupManLinkLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 10),
    _TokGroupManLinkLoop_Type()
)
tokGroupManLinkLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManLinkLoop.setStatus("mandatory")


class _TokGroupManBusLoop_Type(Integer32):
    """Custom type tokGroupManBusLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupManBusLoop_Type.__name__ = "Integer32"
_TokGroupManBusLoop_Object = MibTableColumn
tokGroupManBusLoop = _TokGroupManBusLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 11),
    _TokGroupManBusLoop_Type()
)
tokGroupManBusLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupManBusLoop.setStatus("mandatory")


class _TokGroupAutoLinkLoop_Type(Integer32):
    """Custom type tokGroupAutoLinkLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupAutoLinkLoop_Type.__name__ = "Integer32"
_TokGroupAutoLinkLoop_Object = MibTableColumn
tokGroupAutoLinkLoop = _TokGroupAutoLinkLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 12),
    _TokGroupAutoLinkLoop_Type()
)
tokGroupAutoLinkLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoLinkLoop.setStatus("mandatory")


class _TokGroupAutoBusLoop_Type(Integer32):
    """Custom type tokGroupAutoBusLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokGroupAutoBusLoop_Type.__name__ = "Integer32"
_TokGroupAutoBusLoop_Object = MibTableColumn
tokGroupAutoBusLoop = _TokGroupAutoBusLoop_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 13),
    _TokGroupAutoBusLoop_Type()
)
tokGroupAutoBusLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupAutoBusLoop.setStatus("mandatory")
_TokGroupSpecificOID_Type = ObjectIdentifier
_TokGroupSpecificOID_Object = MibTableColumn
tokGroupSpecificOID = _TokGroupSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 1, 1, 14),
    _TokGroupSpecificOID_Type()
)
tokGroupSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupSpecificOID.setStatus("mandatory")
_TokGroupRingTable_Object = MibTable
tokGroupRingTable = _TokGroupRingTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 2)
)
if mibBuilder.loadTexts:
    tokGroupRingTable.setStatus("mandatory")
_TokGroupRingEntry_Object = MibTableRow
tokGroupRingEntry = _TokGroupRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 2, 1)
)
tokGroupRingEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "tokGroupRingGroupId"),
    (0, "FIBRONICS-MIB", "tokGroupRingId"),
)
if mibBuilder.loadTexts:
    tokGroupRingEntry.setStatus("mandatory")


class _TokGroupRingGroupId_Type(Integer32):
    """Custom type tokGroupRingGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokGroupRingGroupId_Type.__name__ = "Integer32"
_TokGroupRingGroupId_Object = MibTableColumn
tokGroupRingGroupId = _TokGroupRingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 2, 1, 1),
    _TokGroupRingGroupId_Type()
)
tokGroupRingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRingGroupId.setStatus("mandatory")


class _TokGroupRingId_Type(Integer32):
    """Custom type tokGroupRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokGroupRingId_Type.__name__ = "Integer32"
_TokGroupRingId_Object = MibTableColumn
tokGroupRingId = _TokGroupRingId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 2, 1, 2),
    _TokGroupRingId_Type()
)
tokGroupRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRingId.setStatus("mandatory")


class _TokGroupRingSpeed_Type(Integer32):
    """Custom type tokGroupRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 3),
          ("oneMegabit", 2),
          ("sixteenMegabit", 4),
          ("sixteenMgbEarly", 5),
          ("unknown", 1))
    )


_TokGroupRingSpeed_Type.__name__ = "Integer32"
_TokGroupRingSpeed_Object = MibTableColumn
tokGroupRingSpeed = _TokGroupRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 2, 1, 3),
    _TokGroupRingSpeed_Type()
)
tokGroupRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokGroupRingSpeed.setStatus("mandatory")


class _TokGroupRingInserted_Type(Integer32):
    """Custom type tokGroupRingInserted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 2),
          ("notInserted", 1))
    )


_TokGroupRingInserted_Type.__name__ = "Integer32"
_TokGroupRingInserted_Object = MibTableColumn
tokGroupRingInserted = _TokGroupRingInserted_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 2, 2, 1, 4),
    _TokGroupRingInserted_Type()
)
tokGroupRingInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokGroupRingInserted.setStatus("mandatory")
_TokPort_ObjectIdentity = ObjectIdentity
tokPort = _TokPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3)
)
_TokPortTable_Object = MibTable
tokPortTable = _TokPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1)
)
if mibBuilder.loadTexts:
    tokPortTable.setStatus("mandatory")
_TokPortEntry_Object = MibTableRow
tokPortEntry = _TokPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1)
)
tokPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "tokPortGroupId"),
    (0, "FIBRONICS-MIB", "tokPortId"),
)
if mibBuilder.loadTexts:
    tokPortEntry.setStatus("mandatory")


class _TokPortGroupId_Type(Integer32):
    """Custom type tokPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokPortGroupId_Type.__name__ = "Integer32"
_TokPortGroupId_Object = MibTableColumn
tokPortGroupId = _TokPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 1),
    _TokPortGroupId_Type()
)
tokPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortGroupId.setStatus("mandatory")


class _TokPortId_Type(Integer32):
    """Custom type tokPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokPortId_Type.__name__ = "Integer32"
_TokPortId_Object = MibTableColumn
tokPortId = _TokPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 2),
    _TokPortId_Type()
)
tokPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortId.setStatus("mandatory")


class _TokPortBypass_Type(Integer32):
    """Custom type tokPortBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokPortBypass_Type.__name__ = "Integer32"
_TokPortBypass_Object = MibTableColumn
tokPortBypass = _TokPortBypass_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 3),
    _TokPortBypass_Type()
)
tokPortBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokPortBypass.setStatus("mandatory")


class _TokPortConnected_Type(Integer32):
    """Custom type tokPortConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2),
          ("notSupported", 255))
    )


_TokPortConnected_Type.__name__ = "Integer32"
_TokPortConnected_Object = MibTableColumn
tokPortConnected = _TokPortConnected_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 4),
    _TokPortConnected_Type()
)
tokPortConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortConnected.setStatus("mandatory")


class _TokPortTCP_Type(Integer32):
    """Custom type tokPortTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokPortTCP_Type.__name__ = "Integer32"
_TokPortTCP_Object = MibTableColumn
tokPortTCP = _TokPortTCP_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 5),
    _TokPortTCP_Type()
)
tokPortTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokPortTCP.setStatus("mandatory")


class _TokPortCableFault_Type(Integer32):
    """Custom type tokPortCableFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokPortCableFault_Type.__name__ = "Integer32"
_TokPortCableFault_Object = MibTableColumn
tokPortCableFault = _TokPortCableFault_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 6),
    _TokPortCableFault_Type()
)
tokPortCableFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortCableFault.setStatus("mandatory")


class _TokPortFunctionalStatus_Type(Integer32):
    """Custom type tokPortFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("ok", 1),
          ("rld", 2),
          ("tld", 4))
    )


_TokPortFunctionalStatus_Type.__name__ = "Integer32"
_TokPortFunctionalStatus_Object = MibTableColumn
tokPortFunctionalStatus = _TokPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 7),
    _TokPortFunctionalStatus_Type()
)
tokPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortFunctionalStatus.setStatus("mandatory")
_TokPortLastSourceAddr_Type = OctetString
_TokPortLastSourceAddr_Object = MibTableColumn
tokPortLastSourceAddr = _TokPortLastSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 8),
    _TokPortLastSourceAddr_Type()
)
tokPortLastSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortLastSourceAddr.setStatus("mandatory")
_TokPortSpecificOID_Type = ObjectIdentifier
_TokPortSpecificOID_Object = MibTableColumn
tokPortSpecificOID = _TokPortSpecificOID_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 9),
    _TokPortSpecificOID_Type()
)
tokPortSpecificOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortSpecificOID.setStatus("mandatory")


class _TokPortRingSpeedError_Type(Integer32):
    """Custom type tokPortRingSpeedError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_TokPortRingSpeedError_Type.__name__ = "Integer32"
_TokPortRingSpeedError_Object = MibTableColumn
tokPortRingSpeedError = _TokPortRingSpeedError_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 13, 3, 1, 1, 10),
    _TokPortRingSpeedError_Type()
)
tokPortRingSpeedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokPortRingSpeedError.setStatus("mandatory")
_Ts_ObjectIdentity = ObjectIdentity
ts = _Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 14)
)
_TsGroup_ObjectIdentity = ObjectIdentity
tsGroup = _TsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 14, 1)
)
_TsGroupTable_Object = MibTable
tsGroupTable = _TsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    tsGroupTable.setStatus("mandatory")
_TsGroupEntry_Object = MibTableRow
tsGroupEntry = _TsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 14, 1, 1, 1)
)
tsGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "tsGroupId"),
)
if mibBuilder.loadTexts:
    tsGroupEntry.setStatus("mandatory")


class _TsGroupId_Type(Integer32):
    """Custom type tsGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TsGroupId_Type.__name__ = "Integer32"
_TsGroupId_Object = MibTableColumn
tsGroupId = _TsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 14, 1, 1, 1, 1),
    _TsGroupId_Type()
)
tsGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsGroupId.setStatus("mandatory")


class _TsGroupLATStatus_Type(Integer32):
    """Custom type tsGroupLATStatus based on Integer32"""
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


_TsGroupLATStatus_Type.__name__ = "Integer32"
_TsGroupLATStatus_Object = MibTableColumn
tsGroupLATStatus = _TsGroupLATStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 14, 1, 1, 1, 2),
    _TsGroupLATStatus_Type()
)
tsGroupLATStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsGroupLATStatus.setStatus("mandatory")


class _TsGroupOperationMode_Type(Integer32):
    """Custom type tsGroupOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("diagnostics", 1),
          ("diagnosticsFailure", 2),
          ("loading", 3),
          ("loadingFailure", 4),
          ("operational", 5))
    )


_TsGroupOperationMode_Type.__name__ = "Integer32"
_TsGroupOperationMode_Object = MibTableColumn
tsGroupOperationMode = _TsGroupOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 14, 1, 1, 1, 3),
    _TsGroupOperationMode_Type()
)
tsGroupOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsGroupOperationMode.setStatus("mandatory")
_Ltalk_ObjectIdentity = ObjectIdentity
ltalk = _Ltalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15)
)
_LtalkPort_ObjectIdentity = ObjectIdentity
ltalkPort = _LtalkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1)
)
_LtalkPortTable_Object = MibTable
ltalkPortTable = _LtalkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1, 1)
)
if mibBuilder.loadTexts:
    ltalkPortTable.setStatus("mandatory")
_LtalkPortEntry_Object = MibTableRow
ltalkPortEntry = _LtalkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1, 1, 1)
)
ltalkPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "ltalkPortGroupId"),
    (0, "FIBRONICS-MIB", "ltalkPortId"),
)
if mibBuilder.loadTexts:
    ltalkPortEntry.setStatus("mandatory")


class _LtalkPortGroupId_Type(Integer32):
    """Custom type ltalkPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LtalkPortGroupId_Type.__name__ = "Integer32"
_LtalkPortGroupId_Object = MibTableColumn
ltalkPortGroupId = _LtalkPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1, 1, 1, 1),
    _LtalkPortGroupId_Type()
)
ltalkPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortGroupId.setStatus("mandatory")


class _LtalkPortId_Type(Integer32):
    """Custom type ltalkPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LtalkPortId_Type.__name__ = "Integer32"
_LtalkPortId_Object = MibTableColumn
ltalkPortId = _LtalkPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1, 1, 1, 2),
    _LtalkPortId_Type()
)
ltalkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortId.setStatus("mandatory")


class _LtalkPortTest_Type(Integer32):
    """Custom type ltalkPortTest based on Integer32"""
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


_LtalkPortTest_Type.__name__ = "Integer32"
_LtalkPortTest_Object = MibTableColumn
ltalkPortTest = _LtalkPortTest_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1, 1, 1, 3),
    _LtalkPortTest_Type()
)
ltalkPortTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltalkPortTest.setStatus("mandatory")


class _LtalkPortTestResult_Type(Integer32):
    """Custom type ltalkPortTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("ok", 1))
    )


_LtalkPortTestResult_Type.__name__ = "Integer32"
_LtalkPortTestResult_Object = MibTableColumn
ltalkPortTestResult = _LtalkPortTestResult_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1, 1, 1, 4),
    _LtalkPortTestResult_Type()
)
ltalkPortTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortTestResult.setStatus("mandatory")


class _LtalkPortJam_Type(Integer32):
    """Custom type ltalkPortJam based on Integer32"""
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


_LtalkPortJam_Type.__name__ = "Integer32"
_LtalkPortJam_Object = MibTableColumn
ltalkPortJam = _LtalkPortJam_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 15, 1, 1, 1, 5),
    _LtalkPortJam_Type()
)
ltalkPortJam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltalkPortJam.setStatus("mandatory")
_Cl_ObjectIdentity = ObjectIdentity
cl = _Cl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16)
)
_ClGroup_ObjectIdentity = ObjectIdentity
clGroup = _ClGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 1)
)
_ClGroupTable_Object = MibTable
clGroupTable = _ClGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    clGroupTable.setStatus("mandatory")
_ClGroupEntry_Object = MibTableRow
clGroupEntry = _ClGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 1, 1, 1)
)
clGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "clGroupId"),
)
if mibBuilder.loadTexts:
    clGroupEntry.setStatus("mandatory")


class _ClGroupId_Type(Integer32):
    """Custom type clGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClGroupId_Type.__name__ = "Integer32"
_ClGroupId_Object = MibTableColumn
clGroupId = _ClGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 1, 1, 1, 1),
    _ClGroupId_Type()
)
clGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clGroupId.setStatus("mandatory")


class _ClGroupClockRedundancy_Type(Integer32):
    """Custom type clGroupClockRedundancy based on Integer32"""
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


_ClGroupClockRedundancy_Type.__name__ = "Integer32"
_ClGroupClockRedundancy_Object = MibTableColumn
clGroupClockRedundancy = _ClGroupClockRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 1, 1, 1, 2),
    _ClGroupClockRedundancy_Type()
)
clGroupClockRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupClockRedundancy.setStatus("mandatory")
_ClGroupMainClock_Type = Integer32
_ClGroupMainClock_Object = MibTableColumn
clGroupMainClock = _ClGroupMainClock_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 1, 1, 1, 3),
    _ClGroupMainClock_Type()
)
clGroupMainClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupMainClock.setStatus("mandatory")


class _ClGroupTestClocks_Type(Integer32):
    """Custom type clGroupTestClocks based on Integer32"""
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


_ClGroupTestClocks_Type.__name__ = "Integer32"
_ClGroupTestClocks_Object = MibTableColumn
clGroupTestClocks = _ClGroupTestClocks_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 1, 1, 1, 4),
    _ClGroupTestClocks_Type()
)
clGroupTestClocks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clGroupTestClocks.setStatus("mandatory")
_ClPort_ObjectIdentity = ObjectIdentity
clPort = _ClPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 2)
)
_ClPortTable_Object = MibTable
clPortTable = _ClPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 2, 1)
)
if mibBuilder.loadTexts:
    clPortTable.setStatus("mandatory")
_ClPortEntry_Object = MibTableRow
clPortEntry = _ClPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 2, 1, 1)
)
clPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "clPortGroupId"),
    (0, "FIBRONICS-MIB", "clPortId"),
)
if mibBuilder.loadTexts:
    clPortEntry.setStatus("mandatory")


class _ClPortGroupId_Type(Integer32):
    """Custom type clPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClPortGroupId_Type.__name__ = "Integer32"
_ClPortGroupId_Object = MibTableColumn
clPortGroupId = _ClPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 2, 1, 1, 1),
    _ClPortGroupId_Type()
)
clPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortGroupId.setStatus("mandatory")


class _ClPortId_Type(Integer32):
    """Custom type clPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClPortId_Type.__name__ = "Integer32"
_ClPortId_Object = MibTableColumn
clPortId = _ClPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 2, 1, 1, 2),
    _ClPortId_Type()
)
clPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortId.setStatus("mandatory")


class _ClPortFunctionalStatus_Type(Integer32):
    """Custom type clPortFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("ok", 1))
    )


_ClPortFunctionalStatus_Type.__name__ = "Integer32"
_ClPortFunctionalStatus_Object = MibTableColumn
clPortFunctionalStatus = _ClPortFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 16, 2, 1, 1, 3),
    _ClPortFunctionalStatus_Type()
)
clPortFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clPortFunctionalStatus.setStatus("mandatory")
_FbrOID_ObjectIdentity = ObjectIdentity
fbrOID = _FbrOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17)
)
_LBoxOID_ObjectIdentity = ObjectIdentity
lBoxOID = _LBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1)
)
_LUnknownBoxOID_ObjectIdentity = ObjectIdentity
lUnknownBoxOID = _LUnknownBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 1)
)
_LLET18BoxOID_ObjectIdentity = ObjectIdentity
lLET18BoxOID = _LLET18BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 2)
)
_LLET3BoxOID_ObjectIdentity = ObjectIdentity
lLET3BoxOID = _LLET3BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 3)
)
_LLET36BoxOID_ObjectIdentity = ObjectIdentity
lLET36BoxOID = _LLET36BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 4)
)
_LLET18EBoxOID_ObjectIdentity = ObjectIdentity
lLET18EBoxOID = _LLET18EBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 5)
)
_LLERT40BoxOID_ObjectIdentity = ObjectIdentity
lLERT40BoxOID = _LLERT40BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 6)
)
_LLET10BoxOID_ObjectIdentity = ObjectIdentity
lLET10BoxOID = _LLET10BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 7)
)
_LFDX100BoxOID_ObjectIdentity = ObjectIdentity
lFDX100BoxOID = _LFDX100BoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 8)
)
_LSTACKBoxOID_ObjectIdentity = ObjectIdentity
lSTACKBoxOID = _LSTACKBoxOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 17, 1, 9)
)
_FbrSecurity_ObjectIdentity = ObjectIdentity
fbrSecurity = _FbrSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 18)
)
_FbrLanSwitch_ObjectIdentity = ObjectIdentity
fbrLanSwitch = _FbrLanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19)
)
_Lse_ObjectIdentity = ObjectIdentity
lse = _Lse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1)
)
_LseGroupTable_Object = MibTable
lseGroupTable = _LseGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    lseGroupTable.setStatus("mandatory")
_LseGroupEntry_Object = MibTableRow
lseGroupEntry = _LseGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1)
)
lseGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "lseGroupId"),
)
if mibBuilder.loadTexts:
    lseGroupEntry.setStatus("mandatory")
_LseGroupId_Type = Integer32
_LseGroupId_Object = MibTableColumn
lseGroupId = _LseGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 1),
    _LseGroupId_Type()
)
lseGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseGroupId.setStatus("mandatory")


class _LseGroupFastOpen_Type(Integer32):
    """Custom type lseGroupFastOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupFastOpen_Type.__name__ = "Integer32"
_LseGroupFastOpen_Object = MibTableColumn
lseGroupFastOpen = _LseGroupFastOpen_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 2),
    _LseGroupFastOpen_Type()
)
lseGroupFastOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupFastOpen.setStatus("mandatory")


class _LseGroup10MSqlt_Type(Integer32):
    """Custom type lseGroup10MSqlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroup10MSqlt_Type.__name__ = "Integer32"
_LseGroup10MSqlt_Object = MibTableColumn
lseGroup10MSqlt = _LseGroup10MSqlt_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 3),
    _LseGroup10MSqlt_Type()
)
lseGroup10MSqlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroup10MSqlt.setStatus("mandatory")


class _LseGroupSmartSqlt_Type(Integer32):
    """Custom type lseGroupSmartSqlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupSmartSqlt_Type.__name__ = "Integer32"
_LseGroupSmartSqlt_Object = MibTableColumn
lseGroupSmartSqlt = _LseGroupSmartSqlt_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 4),
    _LseGroupSmartSqlt_Type()
)
lseGroupSmartSqlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupSmartSqlt.setStatus("mandatory")


class _LseGroupCParameter_Type(Integer32):
    """Custom type lseGroupCParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LseGroupCParameter_Type.__name__ = "Integer32"
_LseGroupCParameter_Object = MibTableColumn
lseGroupCParameter = _LseGroupCParameter_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 5),
    _LseGroupCParameter_Type()
)
lseGroupCParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupCParameter.setStatus("mandatory")


class _LseGroupIPGJamLength_Type(Integer32):
    """Custom type lseGroupIPGJamLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 112),
    )


_LseGroupIPGJamLength_Type.__name__ = "Integer32"
_LseGroupIPGJamLength_Object = MibTableColumn
lseGroupIPGJamLength = _LseGroupIPGJamLength_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 6),
    _LseGroupIPGJamLength_Type()
)
lseGroupIPGJamLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupIPGJamLength.setStatus("mandatory")


class _LseGroupJamLength_Type(Integer32):
    """Custom type lseGroupJamLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 120),
    )


_LseGroupJamLength_Type.__name__ = "Integer32"
_LseGroupJamLength_Object = MibTableColumn
lseGroupJamLength = _LseGroupJamLength_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 7),
    _LseGroupJamLength_Type()
)
lseGroupJamLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupJamLength.setStatus("mandatory")


class _LseGroupDataBlinderLength_Type(Integer32):
    """Custom type lseGroupDataBlinderLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 120),
    )


_LseGroupDataBlinderLength_Type.__name__ = "Integer32"
_LseGroupDataBlinderLength_Object = MibTableColumn
lseGroupDataBlinderLength = _LseGroupDataBlinderLength_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 8),
    _LseGroupDataBlinderLength_Type()
)
lseGroupDataBlinderLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupDataBlinderLength.setStatus("mandatory")


class _LseGroupIPGDataLength_Type(Integer32):
    """Custom type lseGroupIPGDataLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 120),
    )


_LseGroupIPGDataLength_Type.__name__ = "Integer32"
_LseGroupIPGDataLength_Object = MibTableColumn
lseGroupIPGDataLength = _LseGroupIPGDataLength_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 9),
    _LseGroupIPGDataLength_Type()
)
lseGroupIPGDataLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupIPGDataLength.setStatus("mandatory")


class _LseGroupActiveMonitor_Type(Integer32):
    """Custom type lseGroupActiveMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupActiveMonitor_Type.__name__ = "Integer32"
_LseGroupActiveMonitor_Object = MibTableColumn
lseGroupActiveMonitor = _LseGroupActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 10),
    _LseGroupActiveMonitor_Type()
)
lseGroupActiveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseGroupActiveMonitor.setStatus("mandatory")


class _LseGroupBackBone_Type(Integer32):
    """Custom type lseGroupBackBone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupBackBone_Type.__name__ = "Integer32"
_LseGroupBackBone_Object = MibTableColumn
lseGroupBackBone = _LseGroupBackBone_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 11),
    _LseGroupBackBone_Type()
)
lseGroupBackBone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupBackBone.setStatus("mandatory")


class _LseGroupSetDefaults_Type(Integer32):
    """Custom type lseGroupSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseGroupSetDefaults_Type.__name__ = "Integer32"
_LseGroupSetDefaults_Object = MibTableColumn
lseGroupSetDefaults = _LseGroupSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 1, 1, 12),
    _LseGroupSetDefaults_Type()
)
lseGroupSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseGroupSetDefaults.setStatus("mandatory")
_LseIntPort_ObjectIdentity = ObjectIdentity
lseIntPort = _LseIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2)
)
_LseIntPortTable_Object = MibTable
lseIntPortTable = _LseIntPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lseIntPortTable.setStatus("mandatory")
_LseIntPortEntry_Object = MibTableRow
lseIntPortEntry = _LseIntPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1)
)
lseIntPortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "lseIntPortGroupId"),
    (0, "FIBRONICS-MIB", "lseIntPortId"),
)
if mibBuilder.loadTexts:
    lseIntPortEntry.setStatus("mandatory")


class _LseIntPortGroupId_Type(Integer32):
    """Custom type lseIntPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortGroupId_Type.__name__ = "Integer32"
_LseIntPortGroupId_Object = MibTableColumn
lseIntPortGroupId = _LseIntPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 1),
    _LseIntPortGroupId_Type()
)
lseIntPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortGroupId.setStatus("mandatory")


class _LseIntPortId_Type(Integer32):
    """Custom type lseIntPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LseIntPortId_Type.__name__ = "Integer32"
_LseIntPortId_Object = MibTableColumn
lseIntPortId = _LseIntPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 2),
    _LseIntPortId_Type()
)
lseIntPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortId.setStatus("mandatory")


class _LseIntPortIOMode_Type(Integer32):
    """Custom type lseIntPortIOMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortIOMode_Type.__name__ = "Integer32"
_LseIntPortIOMode_Object = MibTableColumn
lseIntPortIOMode = _LseIntPortIOMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 3),
    _LseIntPortIOMode_Type()
)
lseIntPortIOMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortIOMode.setStatus("mandatory")


class _LseIntPortResetSwitchCAM_Type(Integer32):
    """Custom type lseIntPortResetSwitchCAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortResetSwitchCAM_Type.__name__ = "Integer32"
_LseIntPortResetSwitchCAM_Object = MibTableColumn
lseIntPortResetSwitchCAM = _LseIntPortResetSwitchCAM_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 4),
    _LseIntPortResetSwitchCAM_Type()
)
lseIntPortResetSwitchCAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortResetSwitchCAM.setStatus("mandatory")


class _LseIntPortVideoPacket_Type(Integer32):
    """Custom type lseIntPortVideoPacket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortVideoPacket_Type.__name__ = "Integer32"
_LseIntPortVideoPacket_Object = MibTableColumn
lseIntPortVideoPacket = _LseIntPortVideoPacket_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 5),
    _LseIntPortVideoPacket_Type()
)
lseIntPortVideoPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortVideoPacket.setStatus("mandatory")


class _LseIntPortPriorityStateMachine_Type(Integer32):
    """Custom type lseIntPortPriorityStateMachine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortPriorityStateMachine_Type.__name__ = "Integer32"
_LseIntPortPriorityStateMachine_Object = MibTableColumn
lseIntPortPriorityStateMachine = _LseIntPortPriorityStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 6),
    _LseIntPortPriorityStateMachine_Type()
)
lseIntPortPriorityStateMachine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortPriorityStateMachine.setStatus("mandatory")


class _LseIntPortActiveBroadcastPriority_Type(Integer32):
    """Custom type lseIntPortActiveBroadcastPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortActiveBroadcastPriority_Type.__name__ = "Integer32"
_LseIntPortActiveBroadcastPriority_Object = MibTableColumn
lseIntPortActiveBroadcastPriority = _LseIntPortActiveBroadcastPriority_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 7),
    _LseIntPortActiveBroadcastPriority_Type()
)
lseIntPortActiveBroadcastPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortActiveBroadcastPriority.setStatus("mandatory")


class _LseIntPortPriorityLevel_Type(Integer32):
    """Custom type lseIntPortPriorityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("default", 5),
          ("mngrTerminal", 6),
          ("multicast", 2),
          ("notSupported", 255),
          ("regular", 4),
          ("video", 3))
    )


_LseIntPortPriorityLevel_Type.__name__ = "Integer32"
_LseIntPortPriorityLevel_Object = MibTableColumn
lseIntPortPriorityLevel = _LseIntPortPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 8),
    _LseIntPortPriorityLevel_Type()
)
lseIntPortPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortPriorityLevel.setStatus("mandatory")


class _LseIntPortSuperPriorityEnable_Type(Integer32):
    """Custom type lseIntPortSuperPriorityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortSuperPriorityEnable_Type.__name__ = "Integer32"
_LseIntPortSuperPriorityEnable_Object = MibTableColumn
lseIntPortSuperPriorityEnable = _LseIntPortSuperPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 9),
    _LseIntPortSuperPriorityEnable_Type()
)
lseIntPortSuperPriorityEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortSuperPriorityEnable.setStatus("mandatory")


class _LseIntPortRoutingMode_Type(Integer32):
    """Custom type lseIntPortRoutingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dstPort", 3),
          ("generic", 1),
          ("net", 2),
          ("notSupported", 255))
    )


_LseIntPortRoutingMode_Type.__name__ = "Integer32"
_LseIntPortRoutingMode_Object = MibTableColumn
lseIntPortRoutingMode = _LseIntPortRoutingMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 10),
    _LseIntPortRoutingMode_Type()
)
lseIntPortRoutingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRoutingMode.setStatus("mandatory")


class _LseIntPortGlobal_Type(Integer32):
    """Custom type lseIntPortGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortGlobal_Type.__name__ = "Integer32"
_LseIntPortGlobal_Object = MibTableColumn
lseIntPortGlobal = _LseIntPortGlobal_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 11),
    _LseIntPortGlobal_Type()
)
lseIntPortGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortGlobal.setStatus("mandatory")


class _LseIntPortLearnIOCAM_Type(Integer32):
    """Custom type lseIntPortLearnIOCAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortLearnIOCAM_Type.__name__ = "Integer32"
_LseIntPortLearnIOCAM_Object = MibTableColumn
lseIntPortLearnIOCAM = _LseIntPortLearnIOCAM_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 12),
    _LseIntPortLearnIOCAM_Type()
)
lseIntPortLearnIOCAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortLearnIOCAM.setStatus("mandatory")


class _LseIntPortSecurity_Type(Integer32):
    """Custom type lseIntPortSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortSecurity_Type.__name__ = "Integer32"
_LseIntPortSecurity_Object = MibTableColumn
lseIntPortSecurity = _LseIntPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 13),
    _LseIntPortSecurity_Type()
)
lseIntPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortSecurity.setStatus("mandatory")


class _LseIntPortIgnoreBusy_Type(Integer32):
    """Custom type lseIntPortIgnoreBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortIgnoreBusy_Type.__name__ = "Integer32"
_LseIntPortIgnoreBusy_Object = MibTableColumn
lseIntPortIgnoreBusy = _LseIntPortIgnoreBusy_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 14),
    _LseIntPortIgnoreBusy_Type()
)
lseIntPortIgnoreBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortIgnoreBusy.setStatus("mandatory")


class _LseIntPortRetryPriorityLevel1_Type(Integer32):
    """Custom type lseIntPortRetryPriorityLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LseIntPortRetryPriorityLevel1_Type.__name__ = "Integer32"
_LseIntPortRetryPriorityLevel1_Object = MibTableColumn
lseIntPortRetryPriorityLevel1 = _LseIntPortRetryPriorityLevel1_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 15),
    _LseIntPortRetryPriorityLevel1_Type()
)
lseIntPortRetryPriorityLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRetryPriorityLevel1.setStatus("mandatory")


class _LseIntPortRetryPriorityLevel2_Type(Integer32):
    """Custom type lseIntPortRetryPriorityLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LseIntPortRetryPriorityLevel2_Type.__name__ = "Integer32"
_LseIntPortRetryPriorityLevel2_Object = MibTableColumn
lseIntPortRetryPriorityLevel2 = _LseIntPortRetryPriorityLevel2_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 16),
    _LseIntPortRetryPriorityLevel2_Type()
)
lseIntPortRetryPriorityLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRetryPriorityLevel2.setStatus("mandatory")


class _LseIntPortRetryPriorityLevel3_Type(Integer32):
    """Custom type lseIntPortRetryPriorityLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_LseIntPortRetryPriorityLevel3_Type.__name__ = "Integer32"
_LseIntPortRetryPriorityLevel3_Object = MibTableColumn
lseIntPortRetryPriorityLevel3 = _LseIntPortRetryPriorityLevel3_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 17),
    _LseIntPortRetryPriorityLevel3_Type()
)
lseIntPortRetryPriorityLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRetryPriorityLevel3.setStatus("mandatory")


class _LseIntPortIgnoreProtocolType_Type(Integer32):
    """Custom type lseIntPortIgnoreProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("not-ignore", 2),
          ("notSupported", 255))
    )


_LseIntPortIgnoreProtocolType_Type.__name__ = "Integer32"
_LseIntPortIgnoreProtocolType_Object = MibTableColumn
lseIntPortIgnoreProtocolType = _LseIntPortIgnoreProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 18),
    _LseIntPortIgnoreProtocolType_Type()
)
lseIntPortIgnoreProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortIgnoreProtocolType.setStatus("mandatory")
_LseIntPortCompanyMAC_Type = OctetString
_LseIntPortCompanyMAC_Object = MibTableColumn
lseIntPortCompanyMAC = _LseIntPortCompanyMAC_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 19),
    _LseIntPortCompanyMAC_Type()
)
lseIntPortCompanyMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortCompanyMAC.setStatus("mandatory")


class _LseIntPortTxSafetyZone_Type(Integer32):
    """Custom type lseIntPortTxSafetyZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_LseIntPortTxSafetyZone_Type.__name__ = "Integer32"
_LseIntPortTxSafetyZone_Object = MibTableColumn
lseIntPortTxSafetyZone = _LseIntPortTxSafetyZone_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 20),
    _LseIntPortTxSafetyZone_Type()
)
lseIntPortTxSafetyZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortTxSafetyZone.setStatus("mandatory")


class _LseIntPortRxSafetyZone_Type(Integer32):
    """Custom type lseIntPortRxSafetyZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_LseIntPortRxSafetyZone_Type.__name__ = "Integer32"
_LseIntPortRxSafetyZone_Object = MibTableColumn
lseIntPortRxSafetyZone = _LseIntPortRxSafetyZone_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 21),
    _LseIntPortRxSafetyZone_Type()
)
lseIntPortRxSafetyZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortRxSafetyZone.setStatus("mandatory")


class _LseIntPortTxBurstLength_Type(Integer32):
    """Custom type lseIntPortTxBurstLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_LseIntPortTxBurstLength_Type.__name__ = "Integer32"
_LseIntPortTxBurstLength_Object = MibTableColumn
lseIntPortTxBurstLength = _LseIntPortTxBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 22),
    _LseIntPortTxBurstLength_Type()
)
lseIntPortTxBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortTxBurstLength.setStatus("mandatory")


class _LseIntPortSecurityIntruder_Type(Integer32):
    """Custom type lseIntPortSecurityIntruder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortSecurityIntruder_Type.__name__ = "Integer32"
_LseIntPortSecurityIntruder_Object = MibTableColumn
lseIntPortSecurityIntruder = _LseIntPortSecurityIntruder_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 23),
    _LseIntPortSecurityIntruder_Type()
)
lseIntPortSecurityIntruder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortSecurityIntruder.setStatus("mandatory")


class _LseIntPortJabber_Type(Integer32):
    """Custom type lseIntPortJabber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortJabber_Type.__name__ = "Integer32"
_LseIntPortJabber_Object = MibTableColumn
lseIntPortJabber = _LseIntPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 24),
    _LseIntPortJabber_Type()
)
lseIntPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lseIntPortJabber.setStatus("mandatory")


class _LseIntPortCAM_Type(OctetString):
    """Custom type lseIntPortCAM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(56, 56),
    )


_LseIntPortCAM_Type.__name__ = "OctetString"
_LseIntPortCAM_Object = MibTableColumn
lseIntPortCAM = _LseIntPortCAM_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 25),
    _LseIntPortCAM_Type()
)
lseIntPortCAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortCAM.setStatus("mandatory")


class _LseIntPortVideoStateMachine_Type(Integer32):
    """Custom type lseIntPortVideoStateMachine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LseIntPortVideoStateMachine_Type.__name__ = "Integer32"
_LseIntPortVideoStateMachine_Object = MibTableColumn
lseIntPortVideoStateMachine = _LseIntPortVideoStateMachine_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 26),
    _LseIntPortVideoStateMachine_Type()
)
lseIntPortVideoStateMachine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortVideoStateMachine.setStatus("mandatory")


class _LseIntPortTransmitWeight_Type(Integer32):
    """Custom type lseIntPortTransmitWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LseIntPortTransmitWeight_Type.__name__ = "Integer32"
_LseIntPortTransmitWeight_Object = MibTableColumn
lseIntPortTransmitWeight = _LseIntPortTransmitWeight_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 2, 1, 1, 27),
    _LseIntPortTransmitWeight_Type()
)
lseIntPortTransmitWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lseIntPortTransmitWeight.setStatus("mandatory")
_LsePort_ObjectIdentity = ObjectIdentity
lsePort = _LsePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 3)
)
_LsePortTable_Object = MibTable
lsePortTable = _LsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lsePortTable.setStatus("mandatory")
_LsePortEntry_Object = MibTableRow
lsePortEntry = _LsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 3, 1, 1)
)
lsePortEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "lsePortGroupId"),
    (0, "FIBRONICS-MIB", "lsePortId"),
)
if mibBuilder.loadTexts:
    lsePortEntry.setStatus("mandatory")


class _LsePortGroupId_Type(Integer32):
    """Custom type lsePortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LsePortGroupId_Type.__name__ = "Integer32"
_LsePortGroupId_Object = MibTableColumn
lsePortGroupId = _LsePortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 3, 1, 1, 1),
    _LsePortGroupId_Type()
)
lsePortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsePortGroupId.setStatus("mandatory")


class _LsePortId_Type(Integer32):
    """Custom type lsePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LsePortId_Type.__name__ = "Integer32"
_LsePortId_Object = MibTableColumn
lsePortId = _LsePortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 3, 1, 1, 2),
    _LsePortId_Type()
)
lsePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsePortId.setStatus("mandatory")


class _LsePortPolarity_Type(Integer32):
    """Custom type lsePortPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_LsePortPolarity_Type.__name__ = "Integer32"
_LsePortPolarity_Object = MibTableColumn
lsePortPolarity = _LsePortPolarity_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 19, 1, 3, 1, 1, 3),
    _LsePortPolarity_Type()
)
lsePortPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsePortPolarity.setStatus("mandatory")
_DeviceMgr_ObjectIdentity = ObjectIdentity
deviceMgr = _DeviceMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 20)
)
_BRouter_ObjectIdentity = ObjectIdentity
bRouter = _BRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21)
)
_Iwb_ObjectIdentity = ObjectIdentity
iwb = _Iwb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 1)
)
_Iwr_ObjectIdentity = ObjectIdentity
iwr = _Iwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2)
)
_IwrGroupTable_Object = MibTable
iwrGroupTable = _IwrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 1)
)
if mibBuilder.loadTexts:
    iwrGroupTable.setStatus("mandatory")
_IwrGroupEntry_Object = MibTableRow
iwrGroupEntry = _IwrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 1, 1)
)
iwrGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "iwrGroupId"),
)
if mibBuilder.loadTexts:
    iwrGroupEntry.setStatus("mandatory")
_IwrGroupId_Type = Integer32
_IwrGroupId_Object = MibTableColumn
iwrGroupId = _IwrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 1, 1, 1),
    _IwrGroupId_Type()
)
iwrGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrGroupId.setStatus("mandatory")


class _IwrOperState_Type(Integer32):
    """Custom type iwrOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("boot", 2),
          ("fail", 3),
          ("run", 1))
    )


_IwrOperState_Type.__name__ = "Integer32"
_IwrOperState_Object = MibTableColumn
iwrOperState = _IwrOperState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 1, 1, 2),
    _IwrOperState_Type()
)
iwrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrOperState.setStatus("mandatory")


class _IwrPMState_Type(Integer32):
    """Custom type iwrPMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_IwrPMState_Type.__name__ = "Integer32"
_IwrPMState_Object = MibTableColumn
iwrPMState = _IwrPMState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 1, 1, 3),
    _IwrPMState_Type()
)
iwrPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrPMState.setStatus("mandatory")


class _IwrIOMState_Type(Integer32):
    """Custom type iwrIOMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_IwrIOMState_Type.__name__ = "Integer32"
_IwrIOMState_Object = MibTableColumn
iwrIOMState = _IwrIOMState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 1, 1, 4),
    _IwrIOMState_Type()
)
iwrIOMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrIOMState.setStatus("mandatory")
_IwrWANTable_Object = MibTable
iwrWANTable = _IwrWANTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 2)
)
if mibBuilder.loadTexts:
    iwrWANTable.setStatus("mandatory")
_IwrWANEntry_Object = MibTableRow
iwrWANEntry = _IwrWANEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 2, 1)
)
iwrWANEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "iwrWANGroupId"),
    (0, "FIBRONICS-MIB", "iwrWANPortId"),
)
if mibBuilder.loadTexts:
    iwrWANEntry.setStatus("mandatory")
_IwrWANGroupId_Type = Integer32
_IwrWANGroupId_Object = MibTableColumn
iwrWANGroupId = _IwrWANGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 2, 1, 1),
    _IwrWANGroupId_Type()
)
iwrWANGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANGroupId.setStatus("mandatory")
_IwrWANPortId_Type = Integer32
_IwrWANPortId_Object = MibTableColumn
iwrWANPortId = _IwrWANPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 2, 1, 2),
    _IwrWANPortId_Type()
)
iwrWANPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANPortId.setStatus("mandatory")


class _IwrWANConnection_Type(Integer32):
    """Custom type iwrWANConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_IwrWANConnection_Type.__name__ = "Integer32"
_IwrWANConnection_Object = MibTableColumn
iwrWANConnection = _IwrWANConnection_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 2, 1, 3),
    _IwrWANConnection_Type()
)
iwrWANConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANConnection.setStatus("mandatory")


class _IwrWANPortCableType_Type(Integer32):
    """Custom type iwrWANPortCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 2),
          ("v35", 3),
          ("x21", 1))
    )


_IwrWANPortCableType_Type.__name__ = "Integer32"
_IwrWANPortCableType_Object = MibTableColumn
iwrWANPortCableType = _IwrWANPortCableType_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 2, 2, 1, 4),
    _IwrWANPortCableType_Type()
)
iwrWANPortCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iwrWANPortCableType.setStatus("mandatory")
_Itr_ObjectIdentity = ObjectIdentity
itr = _Itr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3)
)
_ItrGroupTable_Object = MibTable
itrGroupTable = _ItrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 1)
)
if mibBuilder.loadTexts:
    itrGroupTable.setStatus("mandatory")
_ItrGroupEntry_Object = MibTableRow
itrGroupEntry = _ItrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 1, 1)
)
itrGroupEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "itrGroupId"),
)
if mibBuilder.loadTexts:
    itrGroupEntry.setStatus("mandatory")
_ItrGroupId_Type = Integer32
_ItrGroupId_Object = MibTableColumn
itrGroupId = _ItrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 1, 1, 1),
    _ItrGroupId_Type()
)
itrGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrGroupId.setStatus("mandatory")
_ItrMainSWVersion_Type = DisplayString
_ItrMainSWVersion_Object = MibTableColumn
itrMainSWVersion = _ItrMainSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 1, 1, 2),
    _ItrMainSWVersion_Type()
)
itrMainSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrMainSWVersion.setStatus("mandatory")


class _ItrConfigState_Type(Integer32):
    """Custom type itrConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("notSupported", 255),
          ("remote", 2))
    )


_ItrConfigState_Type.__name__ = "Integer32"
_ItrConfigState_Object = MibTableColumn
itrConfigState = _ItrConfigState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 1, 1, 3),
    _ItrConfigState_Type()
)
itrConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrConfigState.setStatus("mandatory")


class _ItrModuleState_Type(Integer32):
    """Custom type itrModuleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("load", 2),
          ("notSupported", 255),
          ("oper", 1),
          ("setup", 3))
    )


_ItrModuleState_Type.__name__ = "Integer32"
_ItrModuleState_Object = MibTableColumn
itrModuleState = _ItrModuleState_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 1, 1, 4),
    _ItrModuleState_Type()
)
itrModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrModuleState.setStatus("mandatory")
_ItrLinkTable_Object = MibTable
itrLinkTable = _ItrLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2)
)
if mibBuilder.loadTexts:
    itrLinkTable.setStatus("mandatory")
_ItrLinkEntry_Object = MibTableRow
itrLinkEntry = _ItrLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1)
)
itrLinkEntry.setIndexNames(
    (0, "FIBRONICS-MIB", "itrLinkGroupId"),
    (0, "FIBRONICS-MIB", "itrLinkPortId"),
)
if mibBuilder.loadTexts:
    itrLinkEntry.setStatus("mandatory")
_ItrLinkGroupId_Type = Integer32
_ItrLinkGroupId_Object = MibTableColumn
itrLinkGroupId = _ItrLinkGroupId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 1),
    _ItrLinkGroupId_Type()
)
itrLinkGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkGroupId.setStatus("mandatory")
_ItrLinkPortId_Type = Integer32
_ItrLinkPortId_Object = MibTableColumn
itrLinkPortId = _ItrLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 2),
    _ItrLinkPortId_Type()
)
itrLinkPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkPortId.setStatus("mandatory")


class _ItrLinkIf_Type(Integer32):
    """Custom type itrLinkIf based on Integer32"""
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
        *(("dte-dce", 4),
          ("v11", 1),
          ("v24", 2),
          ("v35", 3))
    )


_ItrLinkIf_Type.__name__ = "Integer32"
_ItrLinkIf_Object = MibTableColumn
itrLinkIf = _ItrLinkIf_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 3),
    _ItrLinkIf_Type()
)
itrLinkIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkIf.setStatus("mandatory")


class _ItrLinkMode_Type(Integer32):
    """Custom type itrLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("sync", 1))
    )


_ItrLinkMode_Type.__name__ = "Integer32"
_ItrLinkMode_Object = MibTableColumn
itrLinkMode = _ItrLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 4),
    _ItrLinkMode_Type()
)
itrLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkMode.setStatus("mandatory")


class _ItrLinkAsyncRate_Type(Integer32):
    """Custom type itrLinkAsyncRate based on Integer32"""
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
              8,
              9,
              10,
              255)
        )
    )
    namedValues = NamedValues(
        *(("r112000", 10),
          ("r14400", 4),
          ("r19200", 5),
          ("r2400", 1),
          ("r38400", 6),
          ("r4800", 2),
          ("r56000", 7),
          ("r57600", 8),
          ("r64000", 9),
          ("r9600", 3),
          ("unknown", 255))
    )


_ItrLinkAsyncRate_Type.__name__ = "Integer32"
_ItrLinkAsyncRate_Object = MibTableColumn
itrLinkAsyncRate = _ItrLinkAsyncRate_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 5),
    _ItrLinkAsyncRate_Type()
)
itrLinkAsyncRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkAsyncRate.setStatus("mandatory")


class _ItrLinkSyncRate_Type(Integer32):
    """Custom type itrLinkSyncRate based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              255)
        )
    )
    namedValues = NamedValues(
        *(("r1024000", 18),
          ("r112000", 12),
          ("r1200", 1),
          ("r128000", 13),
          ("r14400", 5),
          ("r1544000", 19),
          ("r19200", 6),
          ("r2048000", 20),
          ("r2400", 2),
          ("r256000", 14),
          ("r38400", 7),
          ("r384000", 15),
          ("r4800", 3),
          ("r48000", 8),
          ("r512000", 16),
          ("r56000", 9),
          ("r57600", 10),
          ("r64000", 11),
          ("r786000", 17),
          ("r9600", 4),
          ("unknown", 255))
    )


_ItrLinkSyncRate_Type.__name__ = "Integer32"
_ItrLinkSyncRate_Object = MibTableColumn
itrLinkSyncRate = _ItrLinkSyncRate_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 6),
    _ItrLinkSyncRate_Type()
)
itrLinkSyncRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkSyncRate.setStatus("mandatory")


class _ItrLinkParity_Type(Integer32):
    """Custom type itrLinkParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 255),
          ("off", 2),
          ("on", 1))
    )


_ItrLinkParity_Type.__name__ = "Integer32"
_ItrLinkParity_Object = MibTableColumn
itrLinkParity = _ItrLinkParity_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 7),
    _ItrLinkParity_Type()
)
itrLinkParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkParity.setStatus("mandatory")


class _ItrLinkParityEvenOdd_Type(Integer32):
    """Custom type itrLinkParityEvenOdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("notSupported", 255),
          ("odd", 2))
    )


_ItrLinkParityEvenOdd_Type.__name__ = "Integer32"
_ItrLinkParityEvenOdd_Object = MibTableColumn
itrLinkParityEvenOdd = _ItrLinkParityEvenOdd_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 8),
    _ItrLinkParityEvenOdd_Type()
)
itrLinkParityEvenOdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkParityEvenOdd.setStatus("mandatory")


class _ItrLinkStopBit_Type(Integer32):
    """Custom type itrLinkStopBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("notSupported", 255),
          ("one", 1),
          ("two", 2))
    )


_ItrLinkStopBit_Type.__name__ = "Integer32"
_ItrLinkStopBit_Object = MibTableColumn
itrLinkStopBit = _ItrLinkStopBit_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 9),
    _ItrLinkStopBit_Type()
)
itrLinkStopBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itrLinkStopBit.setStatus("mandatory")


class _ItrLinkRemoteLANConn_Type(Integer32):
    """Custom type itrLinkRemoteLANConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2),
          ("notSupported", 255))
    )


_ItrLinkRemoteLANConn_Type.__name__ = "Integer32"
_ItrLinkRemoteLANConn_Object = MibTableColumn
itrLinkRemoteLANConn = _ItrLinkRemoteLANConn_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 10),
    _ItrLinkRemoteLANConn_Type()
)
itrLinkRemoteLANConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkRemoteLANConn.setStatus("mandatory")


class _ItrLinkFunctionalStatus_Type(Integer32):
    """Custom type itrLinkFunctionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("noRxClk", 3),
          ("ok", 1))
    )


_ItrLinkFunctionalStatus_Type.__name__ = "Integer32"
_ItrLinkFunctionalStatus_Object = MibTableColumn
itrLinkFunctionalStatus = _ItrLinkFunctionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 21, 3, 2, 1, 11),
    _ItrLinkFunctionalStatus_Type()
)
itrLinkFunctionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itrLinkFunctionalStatus.setStatus("mandatory")
_Probe_ObjectIdentity = ObjectIdentity
probe = _Probe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 101, 2, 2, 22)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBRONICS-MIB",
    **{"fibronics": fibronics,
       "fbr101": fbr101,
       "fbr2": fbr2,
       "fbrStack": fbrStack,
       "chassis": chassis,
       "chHWType": chHWType,
       "chNumberOfSlots": chNumberOfSlots,
       "chNumberOfEthernetBuses": chNumberOfEthernetBuses,
       "chNumberOfTRBuses": chNumberOfTRBuses,
       "chNumberOfFDDIBuses": chNumberOfFDDIBuses,
       "chNumberOfLocalTalkBuses": chNumberOfLocalTalkBuses,
       "chReset": chReset,
       "chFullConfig": chFullConfig,
       "chAg": chAg,
       "chGenAgTable": chGenAgTable,
       "chGenAgEntry": chGenAgEntry,
       "chGenAgId": chGenAgId,
       "chGenAgType": chGenAgType,
       "chGenAgMgmtIfType": chGenAgMgmtIfType,
       "chGenAgAddr": chGenAgAddr,
       "chGenAgSpecificOID": chGenAgSpecificOID,
       "chFbrAgTable": chFbrAgTable,
       "chFbrAgEntry": chFbrAgEntry,
       "chFbrAgId": chFbrAgId,
       "chFbrAgSLIPAddress": chFbrAgSLIPAddress,
       "chFbrAgSWVersion": chFbrAgSWVersion,
       "chFbrAgKernelVersion": chFbrAgKernelVersion,
       "chFbrAgCoprocSWVersion": chFbrAgCoprocSWVersion,
       "chFbrAgSWFault": chFbrAgSWFault,
       "chFbrAgMgmtBusSelection": chFbrAgMgmtBusSelection,
       "chFbrAgCoprocCommStatus": chFbrAgCoprocCommStatus,
       "chFbrAgCommDebugMode": chFbrAgCommDebugMode,
       "chFbrAgConfigChangeTraps": chFbrAgConfigChangeTraps,
       "chFbrAgFaultTraps": chFbrAgFaultTraps,
       "chFbrAgTrafficThreshTraps": chFbrAgTrafficThreshTraps,
       "chFbrAgGroupEnrollDeenrollTraps": chFbrAgGroupEnrollDeenrollTraps,
       "chFbrAgSoftFaultTraps": chFbrAgSoftFaultTraps,
       "chFbrAgHubEnrollTraps": chFbrAgHubEnrollTraps,
       "chFbrAgTempThreshTraps": chFbrAgTempThreshTraps,
       "chFbrAgSpecificOID": chFbrAgSpecificOID,
       "chFbrAgLastAddrConfig": chFbrAgLastAddrConfig,
       "chFbrAgSecAddrConfig": chFbrAgSecAddrConfig,
       "chFbrAgSoftwareStatus": chFbrAgSoftwareStatus,
       "chFbrAgConfigurationSymbol": chFbrAgConfigurationSymbol,
       "chFbrAgIntTemp": chFbrAgIntTemp,
       "chFbrAgBootVersion": chFbrAgBootVersion,
       "chFbrAgSensorFault": chFbrAgSensorFault,
       "chFbrAgSensorFaultTraps": chFbrAgSensorFaultTraps,
       "chFbrAgInterProcFault": chFbrAgInterProcFault,
       "chFbrAgInterProcFaultTraps": chFbrAgInterProcFaultTraps,
       "chFbrAgSetup": chFbrAgSetup,
       "chFbrAgMaxNmbOfMngrs": chFbrAgMaxNmbOfMngrs,
       "chFbrAgPermMngrTable": chFbrAgPermMngrTable,
       "chFbrAgPermMngrEntry": chFbrAgPermMngrEntry,
       "chFbrAgPermMngrId": chFbrAgPermMngrId,
       "chFbrAgPermMngrAddr": chFbrAgPermMngrAddr,
       "chFbrAgMaxNmbOfNets": chFbrAgMaxNmbOfNets,
       "chFbrAgRmtNetTable": chFbrAgRmtNetTable,
       "chFbrAgRmtNetEntry": chFbrAgRmtNetEntry,
       "chFbrAgRmtNetId": chFbrAgRmtNetId,
       "chFbrAgRmtNetAddr": chFbrAgRmtNetAddr,
       "chFbrAgRmtNetMask": chFbrAgRmtNetMask,
       "chFbrAgDateTime": chFbrAgDateTime,
       "chFbrAgReset": chFbrAgReset,
       "chMgr": chMgr,
       "chMgrTrapRepStatus": chMgrTrapRepStatus,
       "chMgrContPerfRep": chMgrContPerfRep,
       "chMgrMngmtState": chMgrMngmtState,
       "chMgrPollInterval": chMgrPollInterval,
       "chHW": chHW,
       "chHWPSUTable": chHWPSUTable,
       "chHWPSUEntry": chHWPSUEntry,
       "chHWPSUId": chHWPSUId,
       "chHWPSUActivityStatus": chHWPSUActivityStatus,
       "chHWPSULocation": chHWPSULocation,
       "chHWPSUVoltage": chHWPSUVoltage,
       "chHWIntTempWarning": chHWIntTempWarning,
       "chHWIntTempThresh": chHWIntTempThresh,
       "chHWPeakIntTemp": chHWPeakIntTemp,
       "chSlotLastChange": chSlotLastChange,
       "genGroup": genGroup,
       "genGroupTable": genGroupTable,
       "genGroupEntry": genGroupEntry,
       "genGroupId": genGroupId,
       "genGroupSWVersion": genGroupSWVersion,
       "genGroupKernelVersion": genGroupKernelVersion,
       "genGroupType": genGroupType,
       "genGroupDescr": genGroupDescr,
       "genGroupNumberOfPorts": genGroupNumberOfPorts,
       "genGroupNumberOfIntPorts": genGroupNumberOfIntPorts,
       "genGroupReset": genGroupReset,
       "genGroupAutoMan": genGroupAutoMan,
       "genGroupFullConfig": genGroupFullConfig,
       "genGroupRedun12": genGroupRedun12,
       "genGroupRedun34": genGroupRedun34,
       "genGroupRedun13-14": genGroupRedun13_14,
       "genGroupStandAloneMode": genGroupStandAloneMode,
       "genGroupInterProcCommStatus": genGroupInterProcCommStatus,
       "genGroupCommStatus": genGroupCommStatus,
       "genGroupHWStatus": genGroupHWStatus,
       "genGroupSupplyVoltageFault": genGroupSupplyVoltageFault,
       "genGroupIntTemp": genGroupIntTemp,
       "genGroupSpecificOID": genGroupSpecificOID,
       "genGroupConfigurationSymbol": genGroupConfigurationSymbol,
       "genGroupLastChange": genGroupLastChange,
       "genPort": genPort,
       "genPortTable": genPortTable,
       "genPortEntry": genPortEntry,
       "genPortGroupId": genPortGroupId,
       "genPortId": genPortId,
       "genPortFunctionality": genPortFunctionality,
       "genPortType": genPortType,
       "genPortDescr": genPortDescr,
       "genPortActivityStatus": genPortActivityStatus,
       "genPortSecurityPolicy": genPortSecurityPolicy,
       "genPortSecureAddresses": genPortSecureAddresses,
       "genPortIntPortConnection": genPortIntPortConnection,
       "genPortAdminStatus": genPortAdminStatus,
       "genPortSpecificOID": genPortSpecificOID,
       "genIntPort": genIntPort,
       "genIntPortTable": genIntPortTable,
       "genIntPortEntry": genIntPortEntry,
       "genIntPortGroupId": genIntPortGroupId,
       "genIntPortId": genIntPortId,
       "genIntPortAdminStatus": genIntPortAdminStatus,
       "genIntPortActivityStatus": genIntPortActivityStatus,
       "genIntPortBusConnNumber": genIntPortBusConnNumber,
       "genIntPortBusConnType": genIntPortBusConnType,
       "genIntPortSpecificOID": genIntPortSpecificOID,
       "genIntPortMonitorMode": genIntPortMonitorMode,
       "softRedundancy": softRedundancy,
       "softRedundancyTable": softRedundancyTable,
       "softRedundancyEntry": softRedundancyEntry,
       "softRedundancyId": softRedundancyId,
       "softRedundancyName": softRedundancyName,
       "softRedundancyGroupId1": softRedundancyGroupId1,
       "softRedundancyPortId1": softRedundancyPortId1,
       "softRedundancyGroupId2": softRedundancyGroupId2,
       "softRedundancyPortId2": softRedundancyPortId2,
       "softRedundancyStatus": softRedundancyStatus,
       "eth": eth,
       "ethAg": ethAg,
       "ethAgTable": ethAgTable,
       "ethAgEntry": ethAgEntry,
       "ethAgId": ethAgId,
       "ethAgPerfBusSelection": ethAgPerfBusSelection,
       "ethGroup": ethGroup,
       "ethGroupTable": ethGroupTable,
       "ethGroupEntry": ethGroupEntry,
       "ethGroupId": ethGroupId,
       "ethGroupFIFO": ethGroupFIFO,
       "ethGroup10BTPlus": ethGroup10BTPlus,
       "ethGroupIntPortsRedundancy": ethGroupIntPortsRedundancy,
       "ethGroupBackboneMode": ethGroupBackboneMode,
       "ethGroupFOIRLPlusMode": ethGroupFOIRLPlusMode,
       "ethGroupWrongPortSelection": ethGroupWrongPortSelection,
       "ethGroupBackupBus": ethGroupBackupBus,
       "ethGroupSingleBusMode": ethGroupSingleBusMode,
       "ethGroupSpecificOID": ethGroupSpecificOID,
       "ethGroup10FBPlus": ethGroup10FBPlus,
       "ethGroupMasterClock": ethGroupMasterClock,
       "ethGroupIdleTrx": ethGroupIdleTrx,
       "ethGroupMJLPStatus": ethGroupMJLPStatus,
       "ethPort": ethPort,
       "ethPortTable": ethPortTable,
       "ethPortEntry": ethPortEntry,
       "ethPortGroupId": ethPortGroupId,
       "ethPortId": ethPortId,
       "ethPortFunctionalStatus": ethPortFunctionalStatus,
       "ethPortManPart": ethPortManPart,
       "ethPortJabber": ethPortJabber,
       "ethPortNoAUILoop": ethPortNoAUILoop,
       "ethPortMJLP": ethPortMJLP,
       "ethPortFIFO": ethPortFIFO,
       "ethPortAutoPartitionState": ethPortAutoPartitionState,
       "ethPortSQETest": ethPortSQETest,
       "ethPortLastSourceAddr": ethPortLastSourceAddr,
       "ethPortUserStatus": ethPortUserStatus,
       "ethPortMainBusSelection": ethPortMainBusSelection,
       "ethPortTraffic": ethPortTraffic,
       "ethPortFramesReceivedOK": ethPortFramesReceivedOK,
       "ethPortRunts": ethPortRunts,
       "ethPortPacketErrors": ethPortPacketErrors,
       "ethPortSpecificOID": ethPortSpecificOID,
       "ethPortCollisions": ethPortCollisions,
       "ethPortPartitions": ethPortPartitions,
       "ethPortPygmys": ethPortPygmys,
       "ethIntPort": ethIntPort,
       "ethIntPortTable": ethIntPortTable,
       "ethIntPortEntry": ethIntPortEntry,
       "ethIntPortGroupId": ethIntPortGroupId,
       "ethIntPortId": ethIntPortId,
       "ethIntPortPartition": ethIntPortPartition,
       "ethIntPortJabber": ethIntPortJabber,
       "ethIntPortBackedUp": ethIntPortBackedUp,
       "ethBus": ethBus,
       "ethBusPerfTable": ethBusPerfTable,
       "ethBusPerfEntry": ethBusPerfEntry,
       "ethBusPerfAgId": ethBusPerfAgId,
       "ethBusPerfId": ethBusPerfId,
       "ethBusTrafficBuffer": ethBusTrafficBuffer,
       "ethBusTrafficThresh": ethBusTrafficThresh,
       "ethBusPeakTraffic": ethBusPeakTraffic,
       "ethBusTotalCollisions": ethBusTotalCollisions,
       "ethBusTotalPackets": ethBusTotalPackets,
       "ethBusTotalErrors": ethBusTotalErrors,
       "ethBusTraffic": ethBusTraffic,
       "ethBusUtilization": ethBusUtilization,
       "ethBusPeakUtilization": ethBusPeakUtilization,
       "ethBusClockTable": ethBusClockTable,
       "ethBusClockEntry": ethBusClockEntry,
       "ethBusClockBusId": ethBusClockBusId,
       "ethBusClockId": ethBusClockId,
       "ethBusClockTestResult": ethBusClockTestResult,
       "tok": tok,
       "tokRing": tokRing,
       "tokRingTable": tokRingTable,
       "tokRingEntry": tokRingEntry,
       "tokRingAgId": tokRingAgId,
       "tokRingId": tokRingId,
       "tokRingLeftSlot": tokRingLeftSlot,
       "tokRingRightSlot": tokRingRightSlot,
       "tokRingTrafficBuffer": tokRingTrafficBuffer,
       "tokRingTrafficThresh": tokRingTrafficThresh,
       "tokRingPeakTraffic": tokRingPeakTraffic,
       "tokRingNumberOfStations": tokRingNumberOfStations,
       "tokRingConfiguration": tokRingConfiguration,
       "tokRingBeaconing": tokRingBeaconing,
       "tokRingBeaconingStation": tokRingBeaconingStation,
       "tokRingStationsMatch": tokRingStationsMatch,
       "tokRingTraffic": tokRingTraffic,
       "tokRingSecurityMethod": tokRingSecurityMethod,
       "tokRingSecurityPolicy": tokRingSecurityPolicy,
       "tokRingSecureAddr": tokRingSecureAddr,
       "tokRingLastViolation": tokRingLastViolation,
       "tokRingUtilization": tokRingUtilization,
       "tokRingPeakUtilization": tokRingPeakUtilization,
       "tokGroup": tokGroup,
       "tokGroupTable": tokGroupTable,
       "tokGroupEntry": tokGroupEntry,
       "tokGroupId": tokGroupId,
       "tokGroupAutoRightLoop": tokGroupAutoRightLoop,
       "tokGroupAutoLeftLoop": tokGroupAutoLeftLoop,
       "tokGroupManRightLoop": tokGroupManRightLoop,
       "tokGroupManLeftLoop": tokGroupManLeftLoop,
       "tokGroupRightNeighbor": tokGroupRightNeighbor,
       "tokGroupLeftNeighbor": tokGroupLeftNeighbor,
       "tokGroupIOMode": tokGroupIOMode,
       "tokGroupBridgeMode": tokGroupBridgeMode,
       "tokGroupManLinkLoop": tokGroupManLinkLoop,
       "tokGroupManBusLoop": tokGroupManBusLoop,
       "tokGroupAutoLinkLoop": tokGroupAutoLinkLoop,
       "tokGroupAutoBusLoop": tokGroupAutoBusLoop,
       "tokGroupSpecificOID": tokGroupSpecificOID,
       "tokGroupRingTable": tokGroupRingTable,
       "tokGroupRingEntry": tokGroupRingEntry,
       "tokGroupRingGroupId": tokGroupRingGroupId,
       "tokGroupRingId": tokGroupRingId,
       "tokGroupRingSpeed": tokGroupRingSpeed,
       "tokGroupRingInserted": tokGroupRingInserted,
       "tokPort": tokPort,
       "tokPortTable": tokPortTable,
       "tokPortEntry": tokPortEntry,
       "tokPortGroupId": tokPortGroupId,
       "tokPortId": tokPortId,
       "tokPortBypass": tokPortBypass,
       "tokPortConnected": tokPortConnected,
       "tokPortTCP": tokPortTCP,
       "tokPortCableFault": tokPortCableFault,
       "tokPortFunctionalStatus": tokPortFunctionalStatus,
       "tokPortLastSourceAddr": tokPortLastSourceAddr,
       "tokPortSpecificOID": tokPortSpecificOID,
       "tokPortRingSpeedError": tokPortRingSpeedError,
       "ts": ts,
       "tsGroup": tsGroup,
       "tsGroupTable": tsGroupTable,
       "tsGroupEntry": tsGroupEntry,
       "tsGroupId": tsGroupId,
       "tsGroupLATStatus": tsGroupLATStatus,
       "tsGroupOperationMode": tsGroupOperationMode,
       "ltalk": ltalk,
       "ltalkPort": ltalkPort,
       "ltalkPortTable": ltalkPortTable,
       "ltalkPortEntry": ltalkPortEntry,
       "ltalkPortGroupId": ltalkPortGroupId,
       "ltalkPortId": ltalkPortId,
       "ltalkPortTest": ltalkPortTest,
       "ltalkPortTestResult": ltalkPortTestResult,
       "ltalkPortJam": ltalkPortJam,
       "cl": cl,
       "clGroup": clGroup,
       "clGroupTable": clGroupTable,
       "clGroupEntry": clGroupEntry,
       "clGroupId": clGroupId,
       "clGroupClockRedundancy": clGroupClockRedundancy,
       "clGroupMainClock": clGroupMainClock,
       "clGroupTestClocks": clGroupTestClocks,
       "clPort": clPort,
       "clPortTable": clPortTable,
       "clPortEntry": clPortEntry,
       "clPortGroupId": clPortGroupId,
       "clPortId": clPortId,
       "clPortFunctionalStatus": clPortFunctionalStatus,
       "fbrOID": fbrOID,
       "lBoxOID": lBoxOID,
       "lUnknownBoxOID": lUnknownBoxOID,
       "lLET18BoxOID": lLET18BoxOID,
       "lLET3BoxOID": lLET3BoxOID,
       "lLET36BoxOID": lLET36BoxOID,
       "lLET18EBoxOID": lLET18EBoxOID,
       "lLERT40BoxOID": lLERT40BoxOID,
       "lLET10BoxOID": lLET10BoxOID,
       "lFDX100BoxOID": lFDX100BoxOID,
       "lSTACKBoxOID": lSTACKBoxOID,
       "fbrSecurity": fbrSecurity,
       "fbrLanSwitch": fbrLanSwitch,
       "lse": lse,
       "lseGroupTable": lseGroupTable,
       "lseGroupEntry": lseGroupEntry,
       "lseGroupId": lseGroupId,
       "lseGroupFastOpen": lseGroupFastOpen,
       "lseGroup10MSqlt": lseGroup10MSqlt,
       "lseGroupSmartSqlt": lseGroupSmartSqlt,
       "lseGroupCParameter": lseGroupCParameter,
       "lseGroupIPGJamLength": lseGroupIPGJamLength,
       "lseGroupJamLength": lseGroupJamLength,
       "lseGroupDataBlinderLength": lseGroupDataBlinderLength,
       "lseGroupIPGDataLength": lseGroupIPGDataLength,
       "lseGroupActiveMonitor": lseGroupActiveMonitor,
       "lseGroupBackBone": lseGroupBackBone,
       "lseGroupSetDefaults": lseGroupSetDefaults,
       "lseIntPort": lseIntPort,
       "lseIntPortTable": lseIntPortTable,
       "lseIntPortEntry": lseIntPortEntry,
       "lseIntPortGroupId": lseIntPortGroupId,
       "lseIntPortId": lseIntPortId,
       "lseIntPortIOMode": lseIntPortIOMode,
       "lseIntPortResetSwitchCAM": lseIntPortResetSwitchCAM,
       "lseIntPortVideoPacket": lseIntPortVideoPacket,
       "lseIntPortPriorityStateMachine": lseIntPortPriorityStateMachine,
       "lseIntPortActiveBroadcastPriority": lseIntPortActiveBroadcastPriority,
       "lseIntPortPriorityLevel": lseIntPortPriorityLevel,
       "lseIntPortSuperPriorityEnable": lseIntPortSuperPriorityEnable,
       "lseIntPortRoutingMode": lseIntPortRoutingMode,
       "lseIntPortGlobal": lseIntPortGlobal,
       "lseIntPortLearnIOCAM": lseIntPortLearnIOCAM,
       "lseIntPortSecurity": lseIntPortSecurity,
       "lseIntPortIgnoreBusy": lseIntPortIgnoreBusy,
       "lseIntPortRetryPriorityLevel1": lseIntPortRetryPriorityLevel1,
       "lseIntPortRetryPriorityLevel2": lseIntPortRetryPriorityLevel2,
       "lseIntPortRetryPriorityLevel3": lseIntPortRetryPriorityLevel3,
       "lseIntPortIgnoreProtocolType": lseIntPortIgnoreProtocolType,
       "lseIntPortCompanyMAC": lseIntPortCompanyMAC,
       "lseIntPortTxSafetyZone": lseIntPortTxSafetyZone,
       "lseIntPortRxSafetyZone": lseIntPortRxSafetyZone,
       "lseIntPortTxBurstLength": lseIntPortTxBurstLength,
       "lseIntPortSecurityIntruder": lseIntPortSecurityIntruder,
       "lseIntPortJabber": lseIntPortJabber,
       "lseIntPortCAM": lseIntPortCAM,
       "lseIntPortVideoStateMachine": lseIntPortVideoStateMachine,
       "lseIntPortTransmitWeight": lseIntPortTransmitWeight,
       "lsePort": lsePort,
       "lsePortTable": lsePortTable,
       "lsePortEntry": lsePortEntry,
       "lsePortGroupId": lsePortGroupId,
       "lsePortId": lsePortId,
       "lsePortPolarity": lsePortPolarity,
       "deviceMgr": deviceMgr,
       "bRouter": bRouter,
       "iwb": iwb,
       "iwr": iwr,
       "iwrGroupTable": iwrGroupTable,
       "iwrGroupEntry": iwrGroupEntry,
       "iwrGroupId": iwrGroupId,
       "iwrOperState": iwrOperState,
       "iwrPMState": iwrPMState,
       "iwrIOMState": iwrIOMState,
       "iwrWANTable": iwrWANTable,
       "iwrWANEntry": iwrWANEntry,
       "iwrWANGroupId": iwrWANGroupId,
       "iwrWANPortId": iwrWANPortId,
       "iwrWANConnection": iwrWANConnection,
       "iwrWANPortCableType": iwrWANPortCableType,
       "itr": itr,
       "itrGroupTable": itrGroupTable,
       "itrGroupEntry": itrGroupEntry,
       "itrGroupId": itrGroupId,
       "itrMainSWVersion": itrMainSWVersion,
       "itrConfigState": itrConfigState,
       "itrModuleState": itrModuleState,
       "itrLinkTable": itrLinkTable,
       "itrLinkEntry": itrLinkEntry,
       "itrLinkGroupId": itrLinkGroupId,
       "itrLinkPortId": itrLinkPortId,
       "itrLinkIf": itrLinkIf,
       "itrLinkMode": itrLinkMode,
       "itrLinkAsyncRate": itrLinkAsyncRate,
       "itrLinkSyncRate": itrLinkSyncRate,
       "itrLinkParity": itrLinkParity,
       "itrLinkParityEvenOdd": itrLinkParityEvenOdd,
       "itrLinkStopBit": itrLinkStopBit,
       "itrLinkRemoteLANConn": itrLinkRemoteLANConn,
       "itrLinkFunctionalStatus": itrLinkFunctionalStatus,
       "probe": probe}
)
